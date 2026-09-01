"""Shared multiple-comparison utilities (Benjamini-Hochberg FDR).

Kept separate from ``plot_utilities`` / ``regression_utilities`` so it is a leaf
module with no intra-repo imports: both of those modules and the analysis
notebooks can import it with zero circular-import risk, and statistics stay
separate from plotting.

Design notes
------------
* Significance *stars* (``pvalue_to_stars`` in ``shared.plot_utilities``) are
  intentionally left driving the raw, uncorrected p-values.  FDR is *augmented*
  on top: :func:`benjamini_hochberg` produces q-values and :func:`fdr_marker`
  renders a single dagger for cells that survive correction.  Because BH
  guarantees ``q >= p``, a dagger can only ever appear on a cell that already
  carries a raw star -- a useful visual invariant.
* Each call treats its whole input as one BH *family* (per table / per figure).
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from statsmodels.stats.multitest import multipletests


#: Marker appended to a coefficient that survives Benjamini-Hochberg FDR.
FDR_MARKER = "†"  # dagger


def benjamini_hochberg(pvals, alpha: float = 0.05):
    """Benjamini-Hochberg FDR-adjust a family of p-values.

    The entire input is treated as a single family: a 2-D ``DataFrame`` is
    corrected across every cell at once (the per-figure semantics used by the
    coefficient and odds-ratio heatmaps).  Only *finite* p-values enter the
    family; ``NaN``/``inf`` entries are preserved in place and excluded from the
    correction (mirroring how blank/failed-fit cells are handled elsewhere).

    Accepts a scalar, list/tuple, :class:`numpy.ndarray`, :class:`pandas.Series`
    or :class:`pandas.DataFrame` and returns adjusted q-values in the *same*
    shape and (for pandas objects) index / columns / name.

    A family of size 1 is a no-op (``q == p``); a family of size 0 yields
    all-``NaN``.
    """
    # Scalar fast path (single-test family -> q == p).
    if np.isscalar(pvals) or (isinstance(pvals, np.ndarray) and pvals.ndim == 0):
        p = float(pvals)
        return p if np.isfinite(p) else float("nan")

    # Remember the container so the q-values can be rebuilt in the same shape.
    index = columns = name = None
    if isinstance(pvals, pd.DataFrame):
        index, columns = pvals.index, pvals.columns
        values = pvals.to_numpy(dtype=float)
    elif isinstance(pvals, pd.Series):
        index, name = pvals.index, pvals.name
        values = pvals.to_numpy(dtype=float)
    else:
        values = np.asarray(pvals, dtype=float)

    shape = values.shape
    flat = values.ravel()
    q = np.full(flat.shape, np.nan, dtype=float)

    mask = np.isfinite(flat)
    if mask.any():
        q[mask] = multipletests(flat[mask], alpha=alpha, method="fdr_bh")[1]

    q = q.reshape(shape)

    if columns is not None:
        return pd.DataFrame(q, index=index, columns=columns)
    if index is not None:
        return pd.Series(q, index=index, name=name)
    return q


def fdr_marker(q, alpha: float = 0.05, symbol: str = FDR_MARKER) -> str:
    """Return ``symbol`` when a BH q-value survives ``alpha``, else ``''``.

    Mirrors ``pvalue_to_stars``' NaN handling: a missing or non-finite q-value
    yields ``''`` (no marker).  Keep the glyph centralized here so switching to
    an ASCII fallback (e.g. ``'+'``) is a one-line change.
    """
    if q is None:
        return ""
    q = float(q)
    if not np.isfinite(q):
        return ""
    return symbol if q < alpha else ""
