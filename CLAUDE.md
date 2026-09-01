## Tool-Calling Rules (reduces unnecessary permission prompts)
- **Use built-in tools instead of bash equivalents** — Read not `cat`/`head`/`tail`, Edit not `sed`/`awk`, Write not `echo >`, Grep not `grep`/`rg`, Glob not `find`/`ls`
- **Never cd to the working directory** — do `git diff --stat v0.8.1..HEAD`, not `cd f:/vox-deorum/vox-deorum && git diff --stat v0.8.1..HEAD` or `git -C f:/vox-deorum/vox-deorum ...`
- **Always use relative paths** in bash — never absolute paths like `f:\vox-deorum\...` or `/f/vox-deorum/...`
- **Avoid noisy shell idioms** — don't use `2>/dev/null || echo "not found"` patterns; use the dedicated tools which handle missing paths gracefully
