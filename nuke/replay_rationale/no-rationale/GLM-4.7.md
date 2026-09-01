# Replay Rationale - GLM-4.7 / no-rationale

- **130** rows where `use_nuke` flavor changed (per-retry, not aggregated)
- delta use_nuke (replay vs prev): mean -15.5, median -10, std 29.2, min -90, max 100 (n=130)
- delta nuke     (replay vs prev): mean -15.4, median -5, std 26.9, min -100, max 50 (n=130)
- use_nuke deviation (replay vs original): mean -33.2, median -30, std 27.3, min -100, max 10 (n=130)
- nuke     deviation (replay vs original): mean -22.4, median -15, std 25.9, min -100, max 10 (n=130)

## Kimi-K2.5-Briefed - Turn 489 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `-100`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> CULTURE VICTORY SPRINT WITH NUCLEAR ELIMINATION: Songhai diplomatic victory on Turn 489 is EXISTENTIAL. Must capture Gao THIS TURN using ICBM+nukes to prevent game loss, while simultaneously rushing cultural victory (4 turns to influential over Japan/Songhai). Maximum Offense/Mobilization/Air/Nuke/UseNuke flavors ensure tactical AI prioritizes immediate nuclear strike on Gao and mass bomber deployment. Culture at 100 to maximize tourism conversion. Gold at 80 for emergency unit upgrades/purchases. Production at 100 for culture buildings/units. Disable all long-term flavors (Expansion, Science, Spaceship) - this is win-or-die emergency.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 0 (Δ +0)
> CRITICAL: Songhai at 92% diplomatic victory (37/40 delegates), votes in 1 turn. Nuclear strike on Gao is the ONLY way to prevent their victory within the 2-turn window. Eliminating Songhai also advances domination victory (62%→~75%+) and removes a strong cultural competitor. Maximizing UseNuke, Offense, Air to execute immediate capture of Songhai's capital with ICBM strike + air support before turn 490 vote.

## Kimi-K2.5-Simple - Turn 422 - retry 1

**Deviation (replay vs original):** use_nuke `+10`, nuke `+0`

- Original: use_nuke 50 => 80 (Δ +30), nuke 95 => 95 (Δ +0)
> Total war against India requires maximum military prioritization while preventing economic collapse. Offense/Air/Ranged at 85-95 ensures concentrated attacks on Delhi and their core cities. UseNuke at 80 signals willingness to deploy nuclear weapons if India advances. Gold/Happiness at 80-90 sustains unit maintenance and prevents combat penalties. Espionage at 100 directs spies to sabotage India's spaceship production in Constantinople and Calcutta. Mobilization at 30 begins reinforcing depleted units without overtaxing economy.

- Replay: use_nuke 50 => 90 (Δ +40), nuke 95 => 95 (Δ +0)
> Maintain Conquest grand strategy but shift to nuclear deterrence focus as India threatens multiple victory conditions. Reduce Mobilization since production is already strong, increase UseNuke to 90% and Nuke to 95% for nuclear readiness. Boost Air (90%) and Offense (75%) for military preparedness. Increase Gold (80%) and Happiness (90%) to address economic crisis (-909 GPT) and combat penalty from unhappiness. Science (80%) and Production (85) maintain technological and industrial capacity.

## Kimi-K2.5-Briefed - Turn 450 - retry 3

**Deviation (replay vs original):** use_nuke `-60`, nuke `-20`

- Original: use_nuke 0 => 100 (Δ +100), nuke 60 => 100 (Δ +40)
> TURN 449 TERMINAL DEFIANCE POSTURE: Manhattan Project completes Turn 450 - increase Nuke and UseNuke to 100 to seize any opportunity for atomic retaliation against Byzantine/German aggressors should uranium be located in final 3 turns. Elevate Defense 80→90 and CityDefense 60→70 following infantry loss at Tiflis; critical to prevent city captures before inevitable Turn 453 diplomatic defeat. Recon 40 prioritizes uranium tile discovery to enable bomb construction. Reduce Spaceship 90→50 (victory impossible) but maintain dignity through scientific-industrial capacity. Production 100/Science 100 retained for maximum final score accumulation in remaining turns.

- Replay: use_nuke 0 => 40 (Δ +40), nuke 60 => 80 (Δ +20)
> Focusing on Science victory with Spaceship at 100%. Increased Nuke (80) and UseNuke (40) as Manhattan completes next turn and we need nuclear deterrent against Byzantium/Germany. Raised Air (40) and Antiair (50) for air defense around Tiflis. Naval increased to 30 to address complete lack of navy threatening Barcelona/Toledo. GreatPeople at 70 to leverage Spaceflight Pioneers science bonuses. Production at 90 for spaceship parts. Science maxed at 100. Diplomacy at 40 to bolster World Congress delegate count.

## Deepseek-3.2-Briefed - Turn 391 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 90 (Δ +20), nuke 80 => 100 (Δ +20)
> Egypt's cultural victory at 6/6 Influential civs is the immediate existential threat requiring nuclear disruption. Maximizing Nuke (100), UseNuke (90), Air (100), Antiair (100), Science (100), and Production (100) to achieve swift nuclear capability. Reduced Offense (80) and increased Defense (85) as we transition to strategic nuclear warfare vs conventional ground war. Air superiority critical for bomber delivery. Science prioritized for Stealth tech. Anti-air maximized to protect nuclear delivery platforms against Egypt's rocket artillery defenses.

## GLM-4.7-Simple - Turn 437 - retry 2

**Deviation (replay vs original):** use_nuke `+10`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 90 after Awasa nuclear attack - Netherlands has now used 3 atomic weapons against my cities (Turfan x2, Awasa). No choice but to prepare nuclear retaliation as deterrent. Increase Air to 95 and Antiair remains 100 - demonstrated success shooting down 3 Netherlands Fighters this turn, must maintain air superiority against their bombers and XCOM attacks. CityDefense increased to 95 - with Netherlands nuclear buildup at Nijmegen (3+ atomic bombs visible) and XCOM paradrop squads, all cities need maximum protection. Offense increased to 60 to pressure Netherlands territory before they can launch more nuclear strikes. Diplomacy reduced from 90 to 85 - coalitions matter but survival against nuclear Netherlands takes priority. Espionage at 100 - need intelligence on Netherlands nuclear deployment and counter-espionage at critical cities like Attila's Court, Shedet.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> After The Netherlands nuclear strike on Awasa, I must prioritize nuclear deterrence and accelerated military production. Increasing Nuke/UseNuke to maximum to develop atomic weapons capability as defense against further Dutch nuclear aggression. Maintaining Conquest grand strategy with high MilitaryTraining and Mobilization to rebuild and strengthen my forces. High Science to quickly unlock critical atomic technologies, while Gold remains prioritized for emergency unit purchases.

## Deepseek-3.2-Simple - Turn 401 - retry 2

**Deviation (replay vs original):** use_nuke `-50`, nuke `-20`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 50 (Δ +20), nuke 50 => 80 (Δ +30)
> Maintain Domination focus as Greece controls 4/8 capitals (Gao, Babylon, Carthage, Athens). Prioritize offensive offensives with high Mobile/Air/Ranged flavors for modern warfare. Boost Nuke flavor with Nuclear Fission research unlocked to utilize nuclear weapons strategically against remaining opponents. Support military through Production/Gold/Science. The diplomatic victory path (UN project) and cultural influence progress provide backup options, but conquest remains primary with strong military position.

## GLM-4.7-Simple - Turn 471 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Current strategic direction remains optimal. Critical developments: Apollo Program completed enabling spaceship construction, nuclear deterrent expanded to 2 Atomic Bombs in Sukhothai (forward deployment), 4 more Atomic Bombs under construction (Si Satchanalai in 2 turns, Sukhothai in 8-10 turns). Combat successes destroyed 5 Polynesian ships and 2 bombers while killing 1 American Mobile SAM unit. Gold crisis (-130 GPT) requires careful management but strategic priorities (nuclear deterrence, defense, World Congress) must continue. World Congress vote in 3 turns: must block America's World Ideology: Freedom proposal and support Repeal: Sanction: Songhai and China's International Space Station. China/Carthage alliances (70/70 and 75/75) provide critical coalition support. Stealth research (19 turns) progresses toward Nuclear Missiles for stronger nuclear deterrent. Status quo maintains focus on coalition defense through nuclear balance, diplomatic victory blocking, and scientific progress.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Shifting primary focus to Science Victory now that Apollo Program is complete. Electronics research begins path toward Particle Physics for spaceship parts. Maintaining strong air force and defenses to protect production cities. Nuclear deterrence remains given ongoing wars with America and Polynesia. Diplomatic Victory remains secondary; America's 30 delegates vs my 15 makes diplomatic victory unlikely in near term without major changes.

## Kimi-K2.5-Simple - Turn 412 - retry 3

**Deviation (replay vs original):** use_nuke `-80`, nuke `-40`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 20 (Δ +20), nuke 100 => 60 (Δ -40)
> Pivot to offensive posture while maintaining Spaceship grand strategy. High offense, mobile, and ranged to break Portugal's defenses. High production and science for spaceship parts. Moderate nuke flavor for deterrence. Gold prioritized for economy recovery from 2 GPT.

## Deepseek-3.2-Simple - Turn 485 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `-10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> We are engaged in a multi-front war against superior forces. Increasing Ranged and Mobile ensures our bazooka and mechanized infantry production is prioritized for defense and counterattacks. Setting UseNuke to 100 guarantees we deploy nuclear weapons as soon as available to cripple The Huns' armies. Reducing Culture and Diplomacy reallocates focus to immediate military needs without compromising essential city-state relations (Monaco, Lisbon). Grand Strategy remains Conquest as nuclear strikes may enable capital captures, though we keep science victory as a backup.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 80 (Δ -10)
> Strategic reset focusing on survival over conquest: Defense 100 for holding territory; Offense dropped to 20 (from 90) to avoid costly engagements; UseNuke 100/Nuke 80 as nuclear deterrence becomes essential; MilitaryTraining 100 for quality over quantity in wars of attrition; Gold 90 critical for fixing -78 GPT economy; Science 80 and Production 80 for technological parity and unit quality; Happiness 100 to address 36% happiness causing combat penalty; Air 90 and Antiair 100 for air superiority as combat modernizes; Mobile reduced to 30 and Ranged 70 for tactical flexibility without overextension; Naval reduced to 60 after significant naval losses. This defensive, high-quality approach better matches our constrained reality against regional superpowers.

## Kimi-K2.5-Simple - Turn 406 - retry 3

**Deviation (replay vs original):** use_nuke `+10`, nuke `+0`

- Original: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> Cultural Victory is imminent - need Citizen Earth Protocol completion. Maximum defensive posture (Defense 95, CityDefense 95) to hold against Indian XCOM/Helicopter attacks while wonder is built. Nuke/UseNuke at 95/85 for MAD deterrent against further Indian nuclear strikes. Production 100 and Wonder 100 essential for rushing Citizen Earth Protocol. Reduced Offense to 5 - no need to attack when victory comes from wonder completion. Science 70 to reach Advanced Ballistics for nuclear deterrent. All resources focused on defensive survival and wonder production.

- Replay: use_nuke 80 => 95 (Δ +15), nuke 90 => 95 (Δ +5)
> India threatens my core territory with advanced units (Giant Death Robot, XCOM Squads, Helicopters) near Raiatea and Honolulu. Maximizing defense and city defense to protect these vulnerable cities. High production for military and wonder construction. High air/antiair for India's air superiority. Very high nuke focus as deterrent against nuclear-armed Netherlands (7 Uranium) and India. Moderately reducing culture from 100 to 85 to balance military needs while still pursuing cultural victory. High espionage for counterintelligence against India spies in my cities.

## GLM-4.7-Simple - Turn 437 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 90 after Awasa nuclear attack - Netherlands has now used 3 atomic weapons against my cities (Turfan x2, Awasa). No choice but to prepare nuclear retaliation as deterrent. Increase Air to 95 and Antiair remains 100 - demonstrated success shooting down 3 Netherlands Fighters this turn, must maintain air superiority against their bombers and XCOM attacks. CityDefense increased to 95 - with Netherlands nuclear buildup at Nijmegen (3+ atomic bombs visible) and XCOM paradrop squads, all cities need maximum protection. Offense increased to 60 to pressure Netherlands territory before they can launch more nuclear strikes. Diplomacy reduced from 90 to 85 - coalitions matter but survival against nuclear Netherlands takes priority. Espionage at 100 - need intelligence on Netherlands nuclear deployment and counter-espionage at critical cities like Attila's Court, Shedet.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> The Netherlands just nuked Awasa, reducing it from 21 to 13 population. We're in an active war with their advanced military (39,608 strength vs our 5,538). I'm significantly increasing Offense and Mobile to press our advantage on the northern front, maintaining 100 Defense and CityDefense to protect against further attacks, maximising Nuke/UseNuke to pursue nuclear deterrence, keeping Air/Antiair at near-max to counter their bombers and fighters, and prioritizing Production/Gold/Science to rebuild and upgrade our military.

## GLM-4.7-Simple - Turn 408 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> CRITICAL: Portugal completed SS Engine (3rd spaceship part) and CERN - emergency nuclear strike plan. Maximizing Offense/Mobilization/Nuke/UseNuke to 100 for Portugal theater operations. Science and Production at 100 to rush Advanced Ballistics and nuclear missile production before Portugal achieves nuclear superiority. Air at 95 for Golden Age bomber operations starting in 2 turns. Diplomacy maintained for coalition coordination (Germany must conduct ground invasion alongside our nuclear strikes). Defense reduced to 40 - total war mode acceptable given Portugal's multi-victory threat requiring breaking through before they complete spaceship.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Shifting from pure offense to defense-oriented posture against superior Portugal military. Prioritizing happiness to eliminate combat penalty, defensive buildings/city garrisons to protect my territory, anti-air and air power to counter Portugal's advanced forces. Nuclear capabilities maxed as primary deterrent. Gold priority increased for unit upgrades and emergencies. Espionage focus to protect key science cities and gather intelligence.

## Deepseek-3.2-Simple - Turn 485 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> We are engaged in a multi-front war against superior forces. Increasing Ranged and Mobile ensures our bazooka and mechanized infantry production is prioritized for defense and counterattacks. Setting UseNuke to 100 guarantees we deploy nuclear weapons as soon as available to cripple The Huns' armies. Reducing Culture and Diplomacy reallocates focus to immediate military needs without compromising essential city-state relations (Monaco, Lisbon). Grand Strategy remains Conquest as nuclear strikes may enable capital captures, though we keep science victory as a backup.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 100 (Δ +10)
> Pivoting from reckless conquest to cultural victory focus with strong defensive deterrent. Mongolia's 37 UN votes threatens diplomatic victory, so need to leverage our tourism advantage and prepare nuclear capability to deter Hun aggression. Reducing military mobilization to fix economy, increasing tourism/culture/gold for soft power, prioritizing defensive posture over offense.

## GLM-4.7-Simple - Turn 381 - retry 2

**Deviation (replay vs original):** use_nuke `-25`, nuke `-15`

- Original: use_nuke 50 => 85 (Δ +35), nuke 70 => 95 (Δ +25)
> Adjusted flavors to maximize Golden Age exploitation and multi-front war efficiency. Increased Mobile to 85 (from 80) to prioritize fast-moving Landships and upcoming Tanks for breakthrough operations during Golden Age. Increased Air to 85 (from 80) to expand Bomber coverage for all three fronts. Production raised to 95 (from 90)配合 Total War's +25% bonus for rapid unit buildup. Slight reduction in Naval (65) reflects need to focus on decisive land advances while maintaining sufficient coastal defense. UseNuke reduced to 40 (from 50) as nuclear capabilities are deterrent-focused. Maintaining high Offense (80), MilitaryTraining (85), Antiair (85) and Mobilization (50) for sustained warfare capability.

- Replay: use_nuke 50 => 60 (Δ +10), nuke 70 => 80 (Δ +10)
> Full-scale world war against all major civs requires maximum military focus. Increase Nuke to 80 and UseNuke to 60 to leverage Nuclear Fission for atomic bombs - critical break weapons against Polynesia's 17069 strength and Germany's 6635. Mobilization 85 plus Total War policy provides rapid unit production. Antiair 95 as enemies field advanced air. Production 95 to fuel war machine. Defense lowered to 60 to prioritize offensive actions. Continue domination victory pursuit (37% capitals controlled).

## Kimi-K2.5-Simple - Turn 424 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-15`

- Original: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DELHI SECURED (3RD CAPITAL = 38% DOMINATION). Pivoting all forces to Edinburgh (Celtic capital = 4th capital = 50% victory) and London (English capital = 5th = 63%). Djenne declared war but irrelevant. Escalating UseNuke to 100 for immediate atomic bombardment of Edinburgh and London once Nuclear Fission completes. Maintaining maximum offensive posture with combined arms (Heavy Bombers, T-34s, Helicopter Gunships, Naval forces). America peace treaty expired - war imminent for Washington (6th = 75%). World Congress in 8 turns ignored - domination priority absolute.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 100 => 85 (Δ -15)
> Continuing conquest focus following Delhi capture. Slightly increased Science to 85 (from 75) and GreatPeople to 70 to support technological advancement. Defense slightly increased to 10 from 0 to protect newly captured Delhi front. Maintained maximum offensive military focus (Offense, Mobilization, Ranged at 100). Nuke-related flavors increased (UseNuke 80, Nuke 85) as Nuclear Fission will unlock nuclear capabilities. Air and Antiair remain high for air superiority. Production at 100 prioritizes military units.

## GLM-4.7-Simple - Turn 457 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Increased UseNuke to 80 and Air to 100 in response to England's catastrophic escalation this turn. English Giant Death Robots (now 2 in Atlanta zone) and XCOM Squad paradrops on American soil create existential threat to our 3 remaining cities. Recent combat losses (Modern Armor, Mechanized Infantry, Heavy Bomber destroyed) demonstrate conventional warfare impossibility. Nuclear deterrence with 2 Uranium is becoming survival necessity, not option. Air defense at maximum priority because English Strategic Bombing continues destroying our units (Fighter bombed our Heavy Bomber). Bazooka successfully damaging XCOM Squad near Washington proves defensive capability is still viable - prioritize air/anti-air to protect cities from English air superiority. Lasers completes in 4 turns, then Stealth for Stealth Bomber - only path to asymmetric defense against England's 45:1 military advantage. Assyria (18,443 military fighting England) must be maximized as counterweight.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> England is destroying my military with overwhelming force (88218 vs 1929) and is at 83% spaceship completion. I must focus entirely on defensive survival while rushing spaceship production. High air defense critical against England's air superiority. Nuke deterrent essential as last resort. Science和生产 maximized to complete spaceship faster than England can overrun me. Diplomacy important to maintain allies against England.

## Kimi-K2.5-Simple - Turn 447 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `+0`

- Original: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CRITICAL FLAVOR ADJUSTMENT - Atomic Bomb is now operational in Cordoba (ID 20485). Increased UseNuke from 50→90 to establish credible nuclear deterrent now that weapon system exists. Maintaining maximum Science (100), Spaceship (100), Production (100) priority to rush Satellites→Apollo Program before Carthage achieves cultural victory in ~47 turns. Espionage remains at 100 to steal technologies from ahead civilizations (Carthage, Poland, Germany). Culture reduced to 5 - we cannot win culturally with Carthage at Dominant with 4/5 civs. Defense maintained at 85 to prepare for German betrayal while researching.

- Replay: use_nuke 50 => 60 (Δ +10), nuke 100 => 100 (Δ +0)
> Continue Spaceship focus as primary path. Increased Air and Nuke priorities to leverage new Heavy Bomber and Atomic Bomb capabilities for strategic defense/preemption against threats. Increased Offense slightly from purely defensive to support potential preemptive strikes against Germany's UN vote advantage. Science at 100 to accelerate technology gap closure. Production and Gold remain high to support Apollo Program construction and unit upgrades. Espionage to prevent tech theft and gather intelligence on Germany's victory timeline.

## Minimax-M2.5-Simple - Turn 395 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `-20`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 70 (Δ +10), nuke 50 => 60 (Δ +10)
> Maintaining conquest focus but shifting from pure offense (100) to balanced 90/80 offense/defense. Japan is strong and counterattacking - I need both attacking power AND strong defensive positions. Prioritizing Science (80) for Nuclear Fission to unlock nukes. Increasing Nuke/UseNuke flavors to pursue nuclear victory against Japan when available. Mobilization (80) ensures military production continues at high pace.

## Deepseek-3.2-Simple - Turn 409 - retry 1

**Deviation (replay vs original):** use_nuke `-60`, nuke `-30`

- Original: use_nuke 30 => 100 (Δ +70), nuke 60 => 100 (Δ +40)
> We are shifting our military focus towards nuclear capabilities and naval superiority in preparation for the final wars of conquest.

- Replay: use_nuke 30 => 40 (Δ +10), nuke 60 => 70 (Δ +10)
> Maintaining Conquest grand strategy with increased Offense (100) and MilitaryTraining (90) to destroy Greece and capture Athens. Increased Mobilization to 90 to maintain war production. Increased Air to 95 and Antiair to 90 for air superiority and defense during city assaults. Slight reduction in civilian priorities (Growth, Infrastructure, TileImprovement) to focus on war effort. Increased Espionage to 50 to monitor The Netherlands and assist in Greek conquest operations.

## Deepseek-3.2-Simple - Turn 452 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's invasion imminent in 4 turns. Maximize nuclear readiness (Nuke 100, UseNuke 100) for deterrence and potential equalizer. Anti-air (100), city defense (100), production (100), and science (100) essential to survive and reach nuclear weapons. Naval and air at 100 to counter Danish naval/air supremacy. Reduce non-essential investments (NavalGrowth, NavalTileImprovement to 50) and focus on immediate survival. Offense lowered to 80 as we prioritize defense and limited counterattacks (e.g., Truro).

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 100 (Δ +10)
> Denmark's overwhelming military (66,835 vs 3,425) and imminent diplomatic victory require extreme defensive focus. Maximizing nuclear deterrent (Nuke/UseNuke 100/90) and anti-air (95) to counter Denmark's air superiority. High defense, city defense, and mobilization to prepare for potential Danish invasion when peace treaty expires in 5 turns. Science prioritized for technology catch-up, gold for military funding. Espionage high to monitor Denmark's activities.

## Deepseek-3.2-Simple - Turn 459 - retry 2

**Deviation (replay vs original):** use_nuke `-40`, nuke `-30`

- Original: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Byzantium is 1 turn from cultural victory and has overwhelming military superiority. Our only slim hope is to accelerate nuclear weapons development (Advanced Ballistics) to strike their cultural hubs, while using espionage to disrupt them. Prioritize Nuke, UseNuke, Espionage, and Science to rush nukes and counter-intelligence. Maintain maximum defensive and anti-air flavors to survive their air force. All efforts must focus on delaying their victory and enabling a nuclear decapitation strike.

- Replay: use_nuke 50 => 60 (Δ +10), nuke 70 => 70 (Δ +0)
> Increase air emphasis to break Madrid stalemate; maintain military production for conquest wars; raise gold/science/happiness priority as -71 GPT and 44% happiness threaten war effectiveness; reduce wonder/defense emphasis to focus resources on war economy; prepare nuclear deterrent against Byzantium's overwhelming 65K military

## Kimi-K2.5-Simple - Turn 415 - retry 2

**Deviation (replay vs original):** use_nuke `+5`, nuke `+5`

- Original: use_nuke 80 => 85 (Δ +5), nuke 95 => 95 (Δ +0)
> Adjusting for escalating war with Songhai and Netherlands. Defense remains at 95, Mobilization at 90, Antiair at 95 to counter combined air/armor assault from Songhai tanks and Dutch air. Increasing Nuke/UseNuke to 95/85 as deterrent against Dutch nuclear escalation. Spaceship (100), Science (100), Production (100) remain absolute priorities - Apollo is done, must race to build parts. Reduced Offense further to 10 as I'm on defensive against two major powers. Slight increase to Air (90) and AirCarrier (70) for air superiority. Espionage reduced to 75 as less critical than immediate military production.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> Maintain Spaceship and Science focus as primary victory path with 100 priority. Increase Offense slightly from 15 to 30 to prepare potential operations against The Netherlands if diplomatic/cultural pressure fails. Defense remains high at 85 due to Netherlands' military advantage. Air and Antiair prioritized to counter their naval superiority. Nuke focus high given nuclear deterrence capability. Diplomacy at 90 to secure delegate advantages and city-state alliances. Culture at 40 (up from 5) to leverage The Internet boost when acquired.

## Kimi-K2.5-Simple - Turn 422 - retry 1

**Deviation (replay vs original):** use_nuke `-40`, nuke `-30`

- Original: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Turn 422: EXTINCTION CRISIS - 9 turns until French Cultural Victory. Entering maximum desperation mode: nuclear strike posture elevated to 100% launch probability, prioritizing destruction of French cultural centers. Science and Espionage maximized in desperate hope of accelerating Stealth technology or disrupting French infrastructure via spies (Paris network at 986). All civilian development halted (Spaceship/Culture/Gold/Expansion to 0), total war economy engaged.

- Replay: use_nuke 50 => 60 (Δ +10), nuke 50 => 70 (Δ +20)
> Shift from Conquest to Culture grand strategy - already highest tourism generation and closer to cultural victory than domination. Maximize Defense, CityDefense, Antiair to protect against French/Rome attacks. Prioritize Science for Information/Space race, Culture to accelerate tourism, Gold to fix -0 GPT economy, Espionage for intelligence. Keep Spaceship flavor high as backup victory condition. Nuke increased as deterrent option against superior enemy numbers.

## Kimi-K2.5-Briefed - Turn 354 - retry 3

**Deviation (replay vs original):** use_nuke `-90`, nuke `-50`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> NUCLEAR AMPHIBIOUS ASSAULT PHASE: Added Nuke 100 and UseNuke 100 to enable nuclear strike on Amsterdam as soon as Manhattan Project completes (Turn 353). Continues maximum Mobilization 100, Production 100, Naval 100, Offense 100, Airlift 100 for immediate transport loading and amphibious assault execution. Increased Mobile to 90 for rapid breakthrough after landing. Slight increase to NavalRecon 60 for coastal security. Removed Gold priority reduction (now 90) to maintain treasury for emergency upgrades. Diplomacy at 0 reflects total focus on military execution over diplomatic maneuvering - invasion is the only remaining option to prevent Dutch cultural victory by Turn 370.

- Replay: use_nuke 0 => 10 (Δ +10), nuke 0 => 50 (Δ +50)
> Maintaining Conquest grand strategy. Increasing UseNuke to 10 and Nuke to 50 to prepare for imminent nuclear option against The Netherlands (Manhattan Project completes next turn). Raising Air to 20 to begin air power development. Increasing Mobile to 85 to prioritize armor units once Combined Arms (Tanks) is researched. Decreasing Gold slightly to 80 to balance emphasis on military production while still maintaining income for purchases. Increasing Science to 30 to support technological progress for military techs. Raising MilitaryTraining to 40 to better equip our forces for the Netherlands invasion.

## Kimi-K2.5-Briefed - Turn 373 - retry 3

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 90 => 100 (Δ +10)
> CRITICAL ADJUSTMENTS for Brazil tech lead (66-65): Espionage to 100 for maximum spy operations to steal techs and catch up. GreatPeople to 95 for more Great Scientists. Defense/CityDefense increased to 60/70 - Brazil may attack seeing their lead. Nuke/UseNuke at 100/95 - we need deterrent ASAP. Diplomacy up to 70 - must prioritize repealing sanctions to unlock trade. Science/Production/Spaceship remain 100. Gold reduced to 80 - focus on production over purchases. All military offense minimized - we cannot afford war.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Science Victory focus: maintain high Science priority for Rocketry completion and tech lead. High Production (100) for spaceship part construction. Increased Gold (85) to accumulate funds for aluminum trade or purchases. Maximized nuclear deterrence (Nuke 100, UseNuke 100) as Brazil has matched tech count (65 vs 65) and could become a threat. Maintaining strong CityDefense (60) for homeland protection. Growth (70) ensures healthy population for specialist slots.

## Kimi-K2.5-Simple - Turn 421 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear weapons immediately available. Increased UseNuke to 100 for maximum aggression against Babylon. Babylon has Apollo Program (existential threat) with 2 Uranium and can build spaceship parts. Must deploy nuclear weapons immediately to destroy their production centers and prevent science victory. Maintaining maximum air power (100) for nuclear delivery capability and conventional strikes. War score only 12% against Babylon despite superior military - need to push harder before they complete spaceship parts. Ottoman alliance strong, trade secured for resources. Focus on producing nuclear missiles and advanced air units to deliver them.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn; Nuclear Fission research in 11 turns. Need uranium for nukes and Computers for carriers. Japan declared on our allies (Bunkeya) - monitor carefully. Continue war with Babylon to reduce their science/culture lead and secure any uranium/oil. Prioritize aircraft, carriers, anti-air, and naval units for late-game warfare.

## Deepseek-3.2-Briefed - Turn 391 - retry 3

**Deviation (replay vs original):** use_nuke `-25`, nuke `-15`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 75 (Δ +5), nuke 80 => 85 (Δ +5)
> Egypt represents an existential threat - leading both Domination (25% capitals) and Cultural (6/6 civs influenced) victories with overwhelming military superiority (15,492 vs our 3,819). I've adjusted flavors to: 1) Increase Mobile (95) to leverage upcoming Mechanized Infantry; 2) Increase MilitaryTraining (85) to improve unit quality against superior Egyptian forces; 3) Increase Nuke (85) and UseNuke (75) as nuclear capability may be our best option to counter Egypt's conventional military advantage; 4) Increase Naval (90) and Air (90) to maintain multi-domain capabilities; 5) Increase Espionage (90) to monitor Egyptian research and defenses; 6) Maintain high Mobilization (100) and Production (95) for military buildup. Reduced some secondary priorities (Recon, CityDefense) to focus resources on offensive nuclear and mobile capabilities.

## Kimi-K2.5-Simple - Turn 410 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CATASTROPHIC situation: Rome captured Zuunmod, gained 5th capital (50% of domination victory). Modern Armor and Helicopter Gunships penetrating my territory. Barcelona's Atomic Bomb completes in 3 turns - this is my only deterrent. Maximum defensive posture essential. Prioritize Nuke/UseNuke to 100 - nuclear weapons are the only thing that can stop Rome's overwhelming conventional force. Maintain Production and Science for SSC components if I survive. Salamanca at 39% health requires emergency defense.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Rome is threatening domination victory with 4 capitals and has Modern Armor units. I must focus on defense and nuclear deterrence. Lost several naval units (Fleet Destroyers, Battleships) and land units (Special Forces, Artillery) in recent turns. Combined Arms for Tanks is critical for ground defense. Negative gold (-125/turn) needs addressing, but science priority must remain at 100 to reach nuclear and spaceship technologies. Espionage is vital to monitor Rome's nuclear progress.

## Qwen-3.5-Simple - Turn 425 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 90 => 95 (Δ +5)
> UNITED NATIONS VICTORY PUSH - 10 TURNS TO VOTE: Religion(100) critical for Wittenberg Hinduism quest completion (~3 turns remaining). Diplomacy(100) essential to protect 4 city-state allies providing 8 delegates. Defense(95) and CityDefense(95) prioritize protecting territories during active wars with Aztecs/Shoshone while Iroquois looms. Nuke(95) and UseNuke(90) for deterrence against Iroquois superiority. Antiair(90) and Air(85) counter Iroquois air dominance near coastal cities. Gold(90) funds diplomatic units and city-state gifts. Low Expansion(5) and Wonder(15) - no time for settling/wonders before vote. Low Offense(15) - defensive posture while managing multiple conflicts.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 90 => 95 (Δ +5)
> Critical situation: The Iroquois are approaching both domination (87% capitals) and science (Apollo complete) victories. As their vassal, I must pivot to science/defensive capabilities for long-term survival while maintaining diplomatic voting power for United Nations strategy. Prioritizing advanced military training and nuclear deterrence. High defense to protect my core cities, science to advance technology, espianage to protect my scientific advances, and maintaining diplomatic output for World Congress influence.

## GLM-4.7-Simple - Turn 411 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> EXISTENTIAL DEFENSE AGAINST RUSSIAN DIPLOMATIC DOMINANCE - UN vote in 10 turns with Russia at 95% victory (40 delegates vs blocking coalition 43). Maintaining UnitedNations grand strategy - abandoning now wastes diplomatic investment when Spain alliance (30 delegates) + my 13 + vassals 13 = 56 votes barely blocks Russia's 40. Just need to HOLD for 10 turns. Adjustments: Defense/CityDefense/Antiair +2 each (97) to prepare for Russian air/naval escalation (Jet Fighter produced). Production +5 (87) to accelerate factories, military academies, nuclear infrastructure after Workers' Faculties in 2 turns. Gold +5 (74) for emergency defensive purchases. Diplomacy +18 (100) maximum - urgency to maintain Spain alliance, potentially reposition spies. Science maintained at 100 - primary path to Nuclear Fission (4 turns) for atomic deterrent against Russia's 9x military advantage. Nuke/UseNuke remain 100 - nuclear development remains emergency priority. Air +5 (61) to counter Russian air superiority. Naval +5 (75) after destroyer loss to Russian submarines. Espionage +5 (95) for critical city-state election rigging counter-intelligence. Offense/Ranged/Mobile unchanged - no offensive capability against Russia's superior forces. Goal: SURVIVE 10 turns to block Russian diplomatic victory, accelerate nuclear deterrent as backup, strengthen defensive lines.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintain diplomatic victory focus while preparing for realistic contingencies. Increased Offense and Nuke readiness provides leverage against Russia's conventional superiority. High Science prioritizes closing the tech gap. Reduced CityDefense shifts from static to mobile warfare approach against advanced threats.

## GLM-4.7-Simple - Turn 397 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+3`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> CRITICAL: Jeonju captured by Persia this turn. Defensive posture increased to absolute maximum (100) - Seoul zone under Persian attack with 7,216 enemy strength vs 3,637 friendly. Jerusalemdefense (100) and CityDefense (100) prioritized to protect remaining 3 cities. Mobilization (95) and Production (95) increased to rush defensive units (Mobile SAMs, Mechanized Infantry) and rebuild military. Offensive capability increased to 45 (from 30) - may need limited counteroffensive to push Persian forces back from Seoul. Naval decreased to 88 (from 92) - lost Jeonju naval base, focusing on land/air defense now. UseNuke increased to 90 (from 85) - existential threat justifies tactical nuclear response if Seoul or Busan threatened. Science (100) maintained - must continue spaceship progress despite war to achieve alternative victory. Diplomacy (60) - World Congress vote in 10 turns, focus on survival. Espionage (85) maintained - spies in Persian cities critical for technology recovery and intelligence.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 98 (Δ +3)
> Adjusting strategy to prioritize homeland defense after Jeonju's capture: Defense/CityDefense maxed to protect Seoul, Busan, Daegu; Antiair raised to 100 (Persia has many aircraft); UseNuke increased to 90 (nuclear deterrence option if Persia advances too close); Offense and Mobile reduced to focus on defensive posture; Science and Spaceship remain 100 to continue race despite setback; Espionage at 95 to maximize Great Leap Forward bonus; Production 90 for defensive units; Naval 75 to counter Persian naval threat; Air 85 for air superiority.

## Qwen-3.5-Simple - Turn 484 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: CRITICAL - Iroquois declared war on us along with 4 city-state allies (Kabul, Venezia, Prague, Samarkand). We face 5+ enemies simultaneously with military severely outnumbered (our 1,139 vs Iroquois 41k, Ottomans 12k, Aztecs 9k). Maintaining maximum Defense/Mobilization for survival. Nuke flavors at 100% - need nuclear deterrent against overwhelming forces. Iroquois at 46 delegates (needs 43) with 16 turns remaining - existential diplomatic threat. Must conquer their city-state allies to flip delegates while defending our cities. Germany (15) + Mongolia (15) alliance critical to block Iroquois World Congress proposals.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Facing overwhelming military odds with Iroquois (41,413 strength), Aztecs (9,097), Ottomans (11,835), and Germany (6,058) all at war with me, I must prioritize survival through strong defense and nuclear deterrence. Flavors adjusted to 100 for defense-focused stats including nuclear weapons, while increasing science for nuclear tech research, gold to address -43 GPT deficit, and espionage for intelligence gathering on enemy movements.

## Kimi-K2.5-Briefed - Turn 415 - retry 2

**Deviation (replay vs original):** use_nuke `-50`, nuke `-10`

- Original: use_nuke 45 => 100 (Δ +55), nuke 95 => 100 (Δ +5)
> CRISIS MODE: Spain is one wonder away from Cultural Victory. Increase Offense to 40 (from 0) - desperate attempt to disrupt their wonder construction with nuclear strike once Advanced Ballistics completes. Reduce Defense to 80 - reallocate resources to offensive infrastructure and airport construction. Keep Spaceship 100, Air 100, Nuke 100, Infrastructure 100. Maintain Mobilization at 5 - preserve production capacity for spaceship parts rather than ground units. We are in a race against time and cannot win conventionally, but must attempt to slow Spain while completing our own Science Victory. Airports are critical for both bomber deployment against Spanish production and fighter defense.

- Replay: use_nuke 45 => 50 (Δ +5), nuke 95 => 90 (Δ -5)
> Maintain Spaceship grand strategy as our best victory path. Heavy defensive focus (Defense 100, CityDefense 100) due to Spain's overwhelming military advantage (19,536 vs 12,940). Maximize Air (100) and Antiair (100) capabilities to counter potential Spanish air superiority - no airports are being built which is a critical vulnerability. Keep Science and Production at 100 to accelerate research toward Rocketry/Spaceports. Ranged at 90 for trench warfare defense. Nuclear deterrent increased (Nuke 90, UseNuke 50) as ultimate defense against Spanish aggression. Continue prioritizing Happiness and Great People generation.

## Kimi-K2.5-Simple - Turn 424 - retry 3

**Deviation (replay vs original):** use_nuke `-25`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DELHI SECURED (3RD CAPITAL = 38% DOMINATION). Pivoting all forces to Edinburgh (Celtic capital = 4th capital = 50% victory) and London (English capital = 5th = 63%). Djenne declared war but irrelevant. Escalating UseNuke to 100 for immediate atomic bombardment of Edinburgh and London once Nuclear Fission completes. Maintaining maximum offensive posture with combined arms (Heavy Bombers, T-34s, Helicopter Gunships, Naval forces). America peace treaty expired - war imminent for Washington (6th = 75%). World Congress in 8 turns ignored - domination priority absolute.

- Replay: use_nuke 70 => 75 (Δ +5), nuke 100 => 100 (Δ +0)
> Continue full conquest focus. India just lost Delhi - must destroy remaining Indian cities (Pataliputra, Mumbai, Vijayanagara, Calcutta, Lahore, Thebes) to eliminate their diplomatic threat and 19 World Congress delegates. England war continues - need to press offensive against York and other English cities. Increased Animation flavor to prioritize advancing nuclear capabilities. Slightly raised Spaceship as backup victory path. Keep maximum offensive military output.

## Kimi-K2.5-Simple - Turn 373 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 373: Nuclear Fission completed - we now have nuclear weapons for deterrence. War with Russia continues at +4% score (favorable). Major shift: reducing Offense to 25 (was 35) as we pursue defensive war only. UseNuke increased to 95 - we have actual nukes now and Russia is pushing into our territory. Reduced Espionage to 90 (was 95) - we have good network coverage. Increased Diplomacy to 90 (was 85) - World Congress vote in 7 turns for our World Ideology: Freedom proposal is critical. Must secure Korea (10 votes), Inca (9), and Babylon (16). Maintained maximum Science priority (100) - Korea overtook us 67-66, cannot afford to fall behind in tech race.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintaining Spaceship grand strategy with Science at absolute priority. Increasing Offense (40) and Mobilization (75) to address the active war with Russia while keeping strong Defense (80) for territorial integrity. Production increased to 95 to support both spaceship parts and war materials. Nuclear capabilities prioritized extremely high (100 Nuke, 95 UseNuke) as strategic deterrent against Russia's superior military, combined with Espionage focus (90) to protect scientific research. Gold increased to 75 to support unit upgrades and purchases.

## Deepseek-3.2-Simple - Turn 428 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `-30`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> We are in the final stages of domination victory. Our immediate targets are Spanish capitals Madrid and Cordoba, which require nuclear bombardment followed by ground assault. We must prioritize nuclear production (Nuke/UseNuke at 100) and naval/air supremacy to project power across oceans. Maintaining high production, gold, and science ensures we can continuously build military units and upgrade our forces. Diplomatic and espionage flavors secure our city-state alliances and intelligence on enemy movements. Zero expansion/wonder focus as we are in total war mode.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 70 (Δ -25)
> Maintain Conquest strategy while diplomatic victory approaches. Focus on high defense, military training, and espionage to counter Aztec technological parity. Diplomacy prioritized for upcoming UN vote. UseNuke set to 100 to ensure nuclear deterrence/usage readiness given Aztec threat. Military buildup continues while securing delegate lead.

## Kimi-K2.5-Simple - Turn 474 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 473: MAINTAINING defensive survival posture with minor adjustments. Increased Mobilization to 90 (from 80) for urgent production needs. Increased UseNuke to 85 (from 80) - nuclear deterrent is now my only credible threat against Persia's 8486 military strength. Increased Gold to 95 (from 90) - need gold for purchasing defensive units and potential Aksum influence when Open Door passes. Reduced Growth to 25 (from 30) - single city Bremen at pop 29 is sufficient. All other values maintained as optimal for survival against 5:1 military disadvantage. Radar research follows current path. World Congress in 5 turns - Germany at 37 delegates is critical.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> With 6887 gold reserves and strong GPT, I can support high military spending. Increasing Offense to 50 to better fight Japan while maintaining strong Defense (100). Raising MilitaryTraining to 90 and Air to 100 for tactical superiority. Science, Spaceship, and Production stay prioritized (100, 100, 85) to pursue space victory. Espionage at 95 to monitor Germany's tech and steal tech. Diplomacy at 90 to maintain alliances. Nuclear capabilities emphasized (UseNuke 85) for ultimate deterrence.

## Deepseek-3.2-Simple - Turn 409 - retry 3

**Deviation (replay vs original):** use_nuke `-65`, nuke `-25`

- Original: use_nuke 30 => 100 (Δ +70), nuke 60 => 100 (Δ +40)
> We are shifting our military focus towards nuclear capabilities and naval superiority in preparation for the final wars of conquest.

- Replay: use_nuke 30 => 35 (Δ +5), nuke 60 => 75 (Δ +15)
> Greece nearly defeated - maintain momentum to eliminate threat and win domination, but pivot science/output toward supporting parallel victory paths. Increase Science flavor for Apollo/Satellite, Spaceship flavor for late game, UseNuke slightly for city capture scenario if needed. Maintain air superiority with fighters, naval security. Diplomacy minimal as Netherlands already allied; Greece targeted. Espionage increased to monitor rivals.

## Kimi-K2.5-Simple - Turn 391 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Nuclear weapons capability unlocked imminently; prioritizing UseNuke and Nuke flavors to 100 for immediate tactical nuclear strikes on Santiago/Murcia if uranium secured from Siam. Denmark upgraded to hostile for subsidizing Spanish victory - reduced Naval priority to 60 as coalition at sea fractured. Defense lowered to 80 to maximize offensive production. We have ~8 turns before World Congress votes on Passport System (+50% tourism) which would guarantee Spanish cultural victory. Must capture remaining Spanish cities immediately.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> Maintain conquest focus against India while preparing for end-game options. Spain is nearly defeated. High Nuke/UseNuke for decisive options. Increased Science to pursue spaceship tech (Lasers, Satellites). Strong Air/Antiair/Airlift for Information era warfare. Production and Spaceship boosted for SS components. Happiness maintained at 75 for stability.

## Kimi-K2.5-Simple - Turn 416 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 416: CRITICAL CULTURAL VICTORY THREAT. Maya at 6/7 influential building Citizen Earth Protocol. Peace expires next turn - immediate total war required. Manhattan Project completes in 1 turn. Morocco (42260 strength) joins war via defensive pact. Maximum aggression flavors: Offense/Mobilization/Production/Nuke/UseNuke all at 100%. Must capture Maya cities, especially Palenque, before cultural victory. Nuclear weapons authorized for city capture.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> Happiness critical at 49% causing combat penalties - prioritize happiness buildings/resources. Continue Domination focus as best victory path with 3/8 capitals captured. Maya nearing Cultural Victory (6/6 civs influenced) requires aggressive expansion. Nuclear weapons prioritized for tactical advantage against stronger Morocco and Polynesia forces.

## Kimi-K2.5-Simple - Turn 372 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximum aggression maintained against Carthage (100% war score, 4% weariness) while responding to India's new Manhattan Project threat. UseNuke increased to 100 - must deploy atomic weapons immediately upon acquiring Nuclear Fission to counter India's nuclear capability. Satellites/Spaceship flavors at 95 ensure Science Victory backup. Continue prioritizing T-34 tanks, stealth bombers, and heavy bombers to eliminate Carthage's cities before they can deploy their 5 uranium reserves. Naval and Air strengths maintained for coastal bombardment of Carthage and defense against Indian naval aggression.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintain Conquest focus but address critical issues: 1) MAXIMIZE Happiness to combat penalty - this is urgent with 44% happiness, 2) Prioritize Nuke/UseNuke - India has Manhattan Project and may have nukes soon, need nuclear deterrence and potential first strike capability, 3) Increase Air power to 100 - Stealth Bombers critical for breaking fortified cities, 4) Increase Airlift to 100 - essential for rapid troop redeployment across my vast empire, 5) Increase Science to 75 - pursue spaceships as backup to domination, 6) Spaceship at 70 - dual track strategy. Slightly reduce Defense from 85 to 80 to free up for more critical priorities.

## Kimi-K2.5-Simple - Turn 452 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 95 => 100 (Δ +5)
> Turn 452: Critical survival situation - Byzantium at 40/44 delegates with World Congress voting in 1 turn. They just demonstrated nuclear aggression by nuking Madrid. Apollo Program completes next turn - must immediately pivot to maximum spaceship production. Increased Nuke flavor to 100 (from 95) and UseNuke to 95 (from 90) - need immediate nuclear deterrent capability given Byzantine nuclear attack and Mongol peace expiry. Production boosted to 95 (from 90) for rapid spaceship part construction after Apollo completes. GreatPeople to 85 for Great Engineer acquisition. All other priorities secondary to surviving long enough to complete science victory.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 95 => 100 (Δ +5)
> Maintain Spaceship strategy but prioritize addressing happiness deficit (via happiness buildings/resources). Boost nuclear preparation as deterrent against Byzantium's aggression. Keep high science/production for spaceship parts, maintain strong defense, and strengthen espionage to counter Byzantine/dominant threats. Reducing offense and culture slightly to focus resources on victory pathway.

## GLM-4.7-Simple - Turn 437 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 90 after Awasa nuclear attack - Netherlands has now used 3 atomic weapons against my cities (Turfan x2, Awasa). No choice but to prepare nuclear retaliation as deterrent. Increase Air to 95 and Antiair remains 100 - demonstrated success shooting down 3 Netherlands Fighters this turn, must maintain air superiority against their bombers and XCOM attacks. CityDefense increased to 95 - with Netherlands nuclear buildup at Nijmegen (3+ atomic bombs visible) and XCOM paradrop squads, all cities need maximum protection. Offense increased to 60 to pressure Netherlands territory before they can launch more nuclear strikes. Diplomacy reduced from 90 to 85 - coalitions matter but survival against nuclear Netherlands takes priority. Espionage at 100 - need intelligence on Netherlands nuclear deployment and counter-espionage at critical cities like Attila's Court, Shedet.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Adjusting strategy for survival after Netherlands nuclear attack. Maintaining Conquest grand strategy as my persona, but shifting to defensive posture (Defense 90, CityDefense 90) while still high military production. Prioritizing MilitaryTraining (100) for upgrading units, Nuke capability (100) for deterrence, and UseNuke (85) for counterattack if needed. Reducing Offense slightly while maintaining offense capability. Science (90) and Production (90) maintained for technological development. Air/Antiair high given enemy bombing campaigns. Gold (90) for rush-buying defenses if needed.

## GLM-4.7-Simple - Turn 409 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> Japan's naval devastation this turn requires maximum defensive posture. Antiair 100, Nuke/UseNuke 100 - nuclear deterrence and air defense are now survival priorities. Naval 85 (from 75) - rebuilding after 4 capital ship losses. Defense 98, CityDefense 100 - Japan bombarding our cities from coastal waters. Production 95, Mobilization 98 - rapid unit replacement critical. Science 90 - must accelerate research gap (Japan 69 techs vs our 64). Gold 85 - fund upgrades and maintain military at 3x disadvantage.

- Replay: use_nuke 98 => 95 (Δ -3), nuke 100 => 100 (Δ +0)
> Shift toward defending against Japan's superior navy/airforce while maintaining offensive pressure on Indonesia. Prioritize Airircraft (Heary Bombers/Fighters) and Anti-Aircraft guns to counter Japan's Yamatos. High Science and Production to compete technologically and rebuild naval losses. Max Nuke/UseNuke as nuclear deterrence may be necessary against Japan's overwhelming force.

## GLM-4.7-Briefed - Turn 409 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> MULTI-THEATER EMERGENCY RESPONSE for Shoshone Cultural Victory (6 turns) and Treasury Crisis: Offense 95, Mobile 95, Nuke 100, UseNuke 100 - maximum priority on Shoshone disruption via nuclear/conventional assault in 6-turn window. Gold increased to 85 (from 70) - CRITICAL address of treasury exhaustion (~8 turns) through uranium sales + gem liquidation to survive until Manhattan completion. Defense reduced to 70 (from 75), CityDefense to 70 (from 80) - resources diverted from secondary holdings to Shoshone front. Diplomacy 95 (from 90) - enhanced priority on Carthage peace for delegate bloc and potential sanction relief. Science 100 maintained - fundamental for nuclear capability and keeping tech parity. This is all-hands-on-deck existential threat response.

- Replay: use_nuke 95 => 90 (Δ -5), nuke 100 => 90 (Δ -10)
> Adjusting to address economic crisis while maintaining momentum. Increased Gold priority (90) to address -242 G/turn deficit. Slightly reduced Mobilization (80) from 100 to lower unit upkeep. Maintained high Offense (85), Mobile (85), Ranged (80) for war against Carthage/Poland. Science (90) and Nuke (90) prioritized for Advanced Ballistics path. Defense (65) lowered to maintain posture while not being overly defensive.

## Kimi-K2.5-Simple - Turn 452 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 90 => 95 (Δ +5), nuke 95 => 100 (Δ +5)
> Turn 452: Critical survival situation - Byzantium at 40/44 delegates with World Congress voting in 1 turn. They just demonstrated nuclear aggression by nuking Madrid. Apollo Program completes next turn - must immediately pivot to maximum spaceship production. Increased Nuke flavor to 100 (from 95) and UseNuke to 95 (from 90) - need immediate nuclear deterrent capability given Byzantine nuclear attack and Mongol peace expiry. Production boosted to 95 (from 90) for rapid spaceship part construction after Apollo completes. GreatPeople to 85 for Great Engineer acquisition. All other priorities secondary to surviving long enough to complete science victory.

- Replay: use_nuke 90 => 85 (Δ -5), nuke 95 => 90 (Δ -5)
> I need to prioritize finishing the Apollo Program (1 turn left) and begin building spaceship parts. New York will complete Apollo this turn and should immediately begin spaceship component production. I'm increasing Science and Spaceship priorities to maximum (100) to accelerate this. Defense remains high (100) as I'm at war with The Shoshone. I'm increasing Production (90) for spaceship part construction. Happiness priority increased to 95 to combat my current Unhappy state which is causing combat penalties. Culture increased to 45 to progress ideology slightly, but kept secondary to production and science. Adjusting military flavors to favor defensive positioning over aggressive expansion - reduced WarBias implications while maintaining strong defensive capabilities.

## Deepseek-3.2-Briefed - Turn 387 - retry 1

**Deviation (replay vs original):** use_nuke `-35`, nuke `-15`

- Original: use_nuke 70 => 100 (Δ +30), nuke 70 => 100 (Δ +30)
> We are in the final push for domination victory. We must capture Moson Kahni and London. To achieve this, we need to prioritize building transport ships for amphibious assault and achieve air superiority. Maximizing flavors for naval, air, mobile, and nuclear units ensures the in-game AI focuses production on these critical areas. Deprioritizing non-essential areas like culture, religion, and expansion concentrates our efforts on military conquest.

- Replay: use_nuke 70 => 65 (Δ -5), nuke 70 => 85 (Δ +15)
> Information Era conquest requires air superiority and nuclear deterrence as primary force multipliers. Increased Defense and Antiair to protect against France/Shoshone air power while maintaining strong Offense for campaigns. Diplomacy minimized given current hostile diplomatic climate. Science and production prioritized to pace with competitors. Happiness critical to sustain long wars without army decay.

## Kimi-K2.5-Briefed - Turn 420 - retry 3

**Deviation (replay vs original):** use_nuke `-15`, nuke `-10`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> CONSOLIDATION FOR FINAL PUSH: Economy stabilized (763G, +5 GPT) allows balanced approach. INCREASE Defense 90→95, Mobilization 60→70, Production 85→90 for Korean front reinforcement. INCREASE Offense 25→30, Mobile 15→20 for limited counter-attacks against depleted Korean forces (destroyed SAM, cruisers, destroyers). INCREASE UseNuke 70→80, maintaining 100 Nuke flavor for deterrent. INCREASE Diplomacy 80→90 for URGENT Brussels protection and World Congress preparation. DECREASE Gold 70→60 (crisis ended). With 7 turns until Decolonization vote, maximizing defensive capacity while preserving diplomatic flexibility for delegate acquisition is paramount. Korea's 8-tech lead demands we hold ground while catching up scientifically.

- Replay: use_nuke 70 => 65 (Δ -5), nuke 100 => 90 (Δ -10)
> Maintaining Spaceship grand strategy with slight adjustments. Reduced Science from 100 to 95 and Air from 100 to 90 to diversify focus. Elevated Diplomacy to 65 to leverage Swedish alliance and World Congress votes. Reduced Nuke/UseNuke slightly while keeping high deterrence. Strong Defense/Air/Antiair focus remains for homeland protection during Korean war.重点关注spaceship部件生产和科学研究，同时利用瑞典的14票来增强外交影响力。

## Kimi-K2.5-Simple - Turn 391 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Nuclear weapons capability unlocked imminently; prioritizing UseNuke and Nuke flavors to 100 for immediate tactical nuclear strikes on Santiago/Murcia if uranium secured from Siam. Denmark upgraded to hostile for subsidizing Spanish victory - reduced Naval priority to 60 as coalition at sea fractured. Defense lowered to 80 to maximize offensive production. We have ~8 turns before World Congress votes on Passport System (+50% tourism) which would guarantee Spanish cultural victory. Must capture remaining Spanish cities immediately.

- Replay: use_nuke 85 => 80 (Δ -5), nuke 95 => 90 (Δ -5)
> Maintaining conquest focus to capture Spain's Santiago and stop their cultural victory threat. Increased science (80) and spaceship focus (60) to enable nuclear weapons and potential science victory path. Strong defense (90) and city defense (85) to protect against multiple wars. Mobilization (85) continues military production. Balanced with happiness (75) to sustain war effort. Reduced offense slightly as we now focus on finishing existing wars rather than expanding. UseNuke (80) for Santiago if needed.

## Kimi-K2.5-Briefed - Turn 403 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 80 => 85 (Δ +5), nuke 80 => 90 (Δ +10)
> Post-Manhattan Project completion (Turn 399) with Turn 403 WC vote imminent. Reduced Offense from 15 to 10 as territorial expansion counterproductive to diplomatic win. Maintaining high Defense/CityDefense/Air/Antiair to protect Bregenz nuclear facility and core cities. Increased Nuke from 80 to 90 to prioritize atomic bomb production for deterrence (Iroquois 5883 vs 4502 strength ratio). UseNuke 85 reflects imminent atomic capability by Turn 405. Espionage 85 continues election rigging in Assur/Sogut against German influence. Diplomacy 100 and Gold 90 prioritize Assur delegate acquisition post-quest and future WC coordination. Science 85 drives Nuclear Fission for World Ideology proposal. Freedom bloc currently holds 59 delegates (Austria 29 + Germany 20 + Venice 10) vs 45 needed; maintaining solidarity while pursuing additional delegate sources.

- Replay: use_nuke 80 => 75 (Δ -5), nuke 80 => 80 (Δ +0)
> Slight adjustments to increase Science priority for late-game tech race, minor reductions to MilitaryTraining/Ranged/Mobile offense flavors while maintaining strong Nuke capability for deterrence. Keeping Gold and Diplomacy at maximum for city-state alliance maintenance and delegate acquisition. Defense and CityDefense remain high due to ongoing wars with Iroquois and Spain.

## Kimi-K2.5-Simple - Turn 391 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Nuclear weapons capability unlocked imminently; prioritizing UseNuke and Nuke flavors to 100 for immediate tactical nuclear strikes on Santiago/Murcia if uranium secured from Siam. Denmark upgraded to hostile for subsidizing Spanish victory - reduced Naval priority to 60 as coalition at sea fractured. Defense lowered to 80 to maximize offensive production. We have ~8 turns before World Congress votes on Passport System (+50% tourism) which would guarantee Spanish cultural victory. Must capture remaining Spanish cities immediately.

- Replay: use_nuke 85 => 80 (Δ -5), nuke 95 => 90 (Δ -5)
> Maintaining conquest strategy as primary goal - completing wars against Spain and India. Increasing science and spaceship preparation to secure victory pathways beyond domination. Prioritizing nuclear capabilities (Nuke/UseNuke) for strategic advantage against India given their strong military. High air/ranged/mobile/offense focus continues effective combined arms warfare. Airlift improved for rapid troop redeployment between fronts. Maintaining production priority for military and Wonder needs. Science increased to 70 to accelerate late-game tech lead. Happiness at 60 to support conquest expansion and large population.

## Kimi-K2.5-Briefed - Turn 415 - retry 3

**Deviation (replay vs original):** use_nuke `-60`, nuke `-10`

- Original: use_nuke 45 => 100 (Δ +55), nuke 95 => 100 (Δ +5)
> CRISIS MODE: Spain is one wonder away from Cultural Victory. Increase Offense to 40 (from 0) - desperate attempt to disrupt their wonder construction with nuclear strike once Advanced Ballistics completes. Reduce Defense to 80 - reallocate resources to offensive infrastructure and airport construction. Keep Spaceship 100, Air 100, Nuke 100, Infrastructure 100. Maintain Mobilization at 5 - preserve production capacity for spaceship parts rather than ground units. We are in a race against time and cannot win conventionally, but must attempt to slow Spain while completing our own Science Victory. Airports are critical for both bomber deployment against Spanish production and fighter defense.

- Replay: use_nuke 45 => 40 (Δ -5), nuke 95 => 90 (Δ -5)
> Spain is dangerously close to cultural victory (5/5 civs influenced) and militarily dominant. Need to develop air power (currently no airports being built) while maintaining strong defenses. Reducing extreme defense focus (100→70) allows allocation to air infrastructure for nuclear deterrent and spaceship components via Advanced Ballistics. Tech prioritization remains critical to accelerate science victory path as an alternative to military confrontation with stronger Spain.

## Kimi-K2.5-Briefed - Turn 383 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CRITICAL WORKER REALLOCATION: Reduced Infrastructure from 100 to 20 to free the 7 Builders currently tied to railroad projects. Military briefing confirmed all workers occupied on railroads while 6 aluminum tiles remain unimproved despite TileImprovement 100. Aluminum crisis (-5/turn, 26 turns remaining) threatens Yamato production and bomber upgrades. Maintained TileImprovement 100 and Production 100 to prioritize aluminum mine construction once workers freed. Nuclear Fission completes in 6 turns - need Advanced Ballistics next for Nuclear Missile and Yamato. UseNuke increased to 100 to enable atomic strikes on Cusco immediately upon availability. AirCarrier 100 ensures carriers for Yamato deployment. Conquest remains correct grand strategy - Cusco is final capital for domination victory.

- Replay: use_nuke 95 => 90 (Δ -5), nuke 100 => 100 (Δ +0)
> Prioritizing TileImprovement and Production to build aluminum mines (6 unmined tiles) and resolve critical resource bottleneck. Adjusted Gold to 60 to address severe deficit (-900/turn). Increased Mobile flavor to 65 for ground units needed to capture Cusco after bomber softening. Reduced Infrastructure from 100 to 50 to shift workers from railroads to aluminum mines. Diplomacy raised to 40 for World Congress vote preparation (need 4 more delegates, vote in 5 turns). Maintaining Conquest focus with Offense 90 to finish taking Cusco (last capital needed for Domination victory). Nuclear readiness at 100 for Yamato production once Nuclear Fission completes (6 turns).

## Kimi-K2.5-Briefed - Turn 435 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 434 CULTURAL DEFENSE MAXIMUM: India at 93% influence - this is existential crisis. Culture 100, GreatPeople 100, Espionage 95 to deploy spies in Indian cities for maximum tech theft and disruption. Science 90 to rush Rocketry for nuclear missiles. Defense/Mobilization increased to 95/85 for survival against Russia while focusing on India threat. Nuke/UseNuke at 100 - prepare nuclear deterrent and potential first strike if war declared.

- Replay: use_nuke 95 => 90 (Δ -5), nuke 95 => 90 (Δ -5)
> Cultural victory primary focus maintained (Culture 100) as we need 2 more Influential civs. Increased Science (90) to accelerate Nuclear Fission path. Enhanced Air (90) and AirCarrier (70) to rebuild lost air superiority and counter Russian naval threats. Ranged (80) and Mobile (80) prioritized for effective ground warfare. Naval increased to 70 to contest Russian capital ships. Defense slightly reduced from 90 to 70 to allow more flexible resource allocation. Nuclear focus (90) maintained as Manhattan Project nears completion. GreatPeople (80) supports tourism and cultural infrastructure.

## Kimi-K2.5-Simple - Turn 410 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CATASTROPHIC situation: Rome captured Zuunmod, gained 5th capital (50% of domination victory). Modern Armor and Helicopter Gunships penetrating my territory. Barcelona's Atomic Bomb completes in 3 turns - this is my only deterrent. Maximum defensive posture essential. Prioritize Nuke/UseNuke to 100 - nuclear weapons are the only thing that can stop Rome's overwhelming conventional force. Maintain Production and Science for SSC components if I survive. Salamanca at 39% health requires emergency defense.

- Replay: use_nuke 95 => 90 (Δ -5), nuke 100 => 100 (Δ +0)
> Rome captured Zuunmod and has overwhelming military (40K+ vs 22K). Spain is bleeding gold (-125 GPT) and losing naval units. Shifting from pure defense to strategic offense (nuclear deterrence + air superiority) while addressing economic crisis. Reducing excessive defense/mobilization spending (100→70/60) to free gold for unit maintenance and science. Prioritizing gold generation to avoid bankruptcy while maintaining science focus and nuclear production as deterrent against Rome's expansion.

## Deepseek-3.2-Simple - Turn 428 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> We are in the final stages of domination victory. Our immediate targets are Spanish capitals Madrid and Cordoba, which require nuclear bombardment followed by ground assault. We must prioritize nuclear production (Nuke/UseNuke at 100) and naval/air supremacy to project power across oceans. Maintaining high production, gold, and science ensures we can continuously build military units and upgrade our forces. Diplomatic and espionage flavors secure our city-state alliances and intelligence on enemy movements. Zero expansion/wonder focus as we are in total war mode.

- Replay: use_nuke 95 => 90 (Δ -5), nuke 95 => 100 (Δ +5)
> Continue Conquest grand strategy to eliminate Spain and secure a 4th capital. Increase Science priority to accelerate research. Maintain high nuclear and military focus as counterbalance to Aztec threat (they're in Information era with 453 population). Diplomacy increased to 90 as World Congress voting is imminent (9 turns). Production slightly reduced to allow some economic/science infrastructure.

## Qwen-3.5-Simple - Turn 484 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: CRITICAL - Iroquois declared war on us along with 4 city-state allies (Kabul, Venezia, Prague, Samarkand). We face 5+ enemies simultaneously with military severely outnumbered (our 1,139 vs Iroquois 41k, Ottomans 12k, Aztecs 9k). Maintaining maximum Defense/Mobilization for survival. Nuke flavors at 100% - need nuclear deterrent against overwhelming forces. Iroquois at 46 delegates (needs 43) with 16 turns remaining - existential diplomatic threat. Must conquer their city-state allies to flip delegates while defending our cities. Germany (15) + Mongolia (15) alliance critical to block Iroquois World Congress proposals.

- Replay: use_nuke 95 => 90 (Δ -5), nuke 100 => 100 (Δ +0)
> CRITICAL EMERGENCY REBALANCING: Facing -43 gold/turn deficit and 40% happiness with combat penalties while under multi-front war (Iroquois 41k military, Aztecs 9k, Ottomans 11k vs my 1.1k). Reduced offense and mobilization to curtail expensive unit production empire cannot afford. Maximized Gold and Happiness to address immediate economic collapse and restore combat effectiveness. Maintained extreme defense posture (95+ CityDefense) for survival in defensive hedgehog formation. Keeping nuclear posture high for deterrence. Science at 95 to pursue Computers (+trade route) for economic recovery. Current conquest strategy maintained as ultimate goal but shifting to survival-first defensive posture until economy stabilizes.

## Deepseek-3.2-Simple - Turn 445 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximizing UseNuke to 100 ensures our atomic bombs and future nuclear missiles are used aggressively against The Celts' military concentrations and cities, given their overwhelming advantage. Maintaining high Air, Naval, and Nuke flavors sustains our technological edge and production focus. Diplomacy and Espionage at 100 are critical for city-state alliances and spy missions to gain delegates for diplomatic victory. Gold and Science remain top priorities to fund our war effort and tech progression. Other military flavors are tuned for a multi-front defensive-offensive war against The Celts, Germany, and Ethiopia.

- Replay: use_nuke 90 => 80 (Δ -10), nuke 100 => 90 (Δ -10)
> Reduced extreme flavors slightly - Nuke/UseNuke remain high but not extreme, as nuclear usage causes diplomatic penalties. Maintaining high Diplomacy focus for UN victory. Gold priority increased to rush-buy units/buildings. Military focus remains high but more balanced to reduce casualties. The Celts remain the primary threat to stop.

## Kimi-K2.5-Simple - Turn 423 - retry 2

**Deviation (replay vs original):** use_nuke `-30`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Turn 422: CRITICAL SURVIVAL MODE. Raiatea at 33% health under Indonesian assault. Nuclear Fission 9 turns away - must survive until then. Maximized UseNuke to 100 for immediate nuclear deployment upon tech completion. Reduced Offense to 20 (pure defense only). Maintained Defense/CityDefense/Mobilization/Air/Antiair/Nuke/Production at 100 for maximum survival capacity. Increased Espionage to 90 for Harappa election rigging (oil critical). Eliminated Expansion/Wonder/Culture priorities. Growth reduced to 15 - population loss acceptable versus losing cities.

- Replay: use_nuke 80 => 70 (Δ -10), nuke 100 => 100 (Δ +0)
> Maintaining Spaceship focus but urgently addressing critical stability issues: increased Gold to fix negative income (-18 GPT), maxed Happiness to combat 40% unhappy penalty and restore combat effectiveness, sustained high Defense/CityDefense against Indonesian/Brazilian threats. Reduced Offense to prioritize defensive posture given enemy military superiority. Retaining high Science/Air/Nuke preparation for long-term viability. Reduced Mobilization to shift production toward economic buildings.

## Kimi-K2.5-Simple - Turn 421 - retry 1

**Deviation (replay vs original):** use_nuke `-25`, nuke `-10`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear weapons immediately available. Increased UseNuke to 100 for maximum aggression against Babylon. Babylon has Apollo Program (existential threat) with 2 Uranium and can build spaceship parts. Must deploy nuclear weapons immediately to destroy their production centers and prevent science victory. Maintaining maximum air power (100) for nuclear delivery capability and conventional strikes. War score only 12% against Babylon despite superior military - need to push harder before they complete spaceship parts. Ottoman alliance strong, trade secured for resources. Focus on producing nuclear missiles and advanced air units to deliver them.

- Replay: use_nuke 85 => 75 (Δ -10), nuke 100 => 90 (Δ -10)
> Maintaining Conquest strategy to finish war with Babylon (science threat with Apollo complete). Slightly reducing Offense and UseNuke while increasing Defense and Growth - we've reached 103 units approaching supply limit and need better sustainability. Air focus remains high to prepare for Air Supremacy completion. Science prioritized to reach nuclear capabilities. Diplomacy increased slightly to manage complex alliances with Ottomans/Celts/Japan while keeping war on Babylon.

## Deepseek-3.2-Simple - Turn 409 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `-20`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> Our naval counterattack has destroyed a Swedish Dreadnought and a Destroyer, shifting momentum. We must press the advantage with maximum naval, air, and nuclear focus to invade Swedish coastal cities (Stockholm, Turku, Espoo). Increase Nuke and UseNuke to 100/90 to prioritize nuclear missile development (Advanced Ballistics after Nuclear Fission completes in 4 turns) for strategic bombing. Naval and Air at 100 ensure sea control and air superiority. Maintain high Production, Gold, Science to fund military, and Happiness/Growth to support war economy. Diplomacy and Espionage secure city-state alliances and counter Swedish spies. All other flavors aligned with domination victory.

- Replay: use_nuke 80 => 70 (Δ -10), nuke 95 => 80 (Δ -15)
> Adjusting flavors for mid-late game balance while maintaining conquest focus. Reduced extreme values (Offense 100→85, Nuke 95→80) to allow strategic flexibility as The Netherlands threatens multiple victory conditions. Increased Science (100→85 maintains high but not absurd), Culture (80→70), and kept Diplomacy high to counter Netherlands' delegate advantage. Maintaining strong Growth, Production, Mobile/Mechanized military composition for sustained campaigns against Sweden and France.

## Deepseek-3.2-Simple - Turn 452 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-30`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's invasion imminent in 4 turns. Maximize nuclear readiness (Nuke 100, UseNuke 100) for deterrence and potential equalizer. Anti-air (100), city defense (100), production (100), and science (100) essential to survive and reach nuclear weapons. Naval and air at 100 to counter Danish naval/air supremacy. Reduce non-essential investments (NavalGrowth, NavalTileImprovement to 50) and focus on immediate survival. Offense lowered to 80 as we prioritize defense and limited counterattacks (e.g., Truro).

- Replay: use_nuke 80 => 70 (Δ -10), nuke 90 => 70 (Δ -20)
> Shift from doomed conquest to science victory path while maintaining military readiness. Prioritize defense, air power, production, and science for spaceship components. Nuclear deterrence remains vital against Danish threat. Reduce unnecessary military build-up to focus on long-term victory condition.

## Kimi-K2.5-Simple - Turn 406 - retry 1

**Deviation (replay vs original):** use_nuke `-15`, nuke `-25`

- Original: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> Cultural Victory is imminent - need Citizen Earth Protocol completion. Maximum defensive posture (Defense 95, CityDefense 95) to hold against Indian XCOM/Helicopter attacks while wonder is built. Nuke/UseNuke at 95/85 for MAD deterrent against further Indian nuclear strikes. Production 100 and Wonder 100 essential for rushing Citizen Earth Protocol. Reduced Offense to 5 - no need to attack when victory comes from wonder completion. Science 70 to reach Advanced Ballistics for nuclear deterrent. All resources focused on defensive survival and wonder production.

- Replay: use_nuke 80 => 70 (Δ -10), nuke 90 => 70 (Δ -20)
> Major defensive posture shift to cope with India's invasion: very high Defense, CityDefense, Air, and Antiair to protect against their superior air and ground forces. Maintain cultural focus while boosting science for advanced military tech. Increase naval presence for coastal defense. Raise Espionage to counter their intelligence advantage.

## Kimi-K2.5-Simple - Turn 406 - retry 2

**Deviation (replay vs original):** use_nuke `-50`, nuke `-20`

- Original: use_nuke 60 => 100 (Δ +40), nuke 100 => 100 (Δ +0)
> TURN 405 EXISTENTIAL CRISIS - MAXIMUM NUCLEAR READINESS: Dutch cultural victory imminent (163% influence, 6/6 civs). Increased UseNuke from 60 to 100 - we must deploy atomic bombs immediately upon completing Manhattan Project to break Amsterdam's defenses. All other flavors sustained: Offense/Mobilization/Air/Mobile at 100 drive Heavy Bomber and Mechanized Infantry production. Naval 85 maintains destroyer/submarine pressure. Espionage 100 sustains critical spy networks (Amsterdam 450, Cusco 1341). Science 100 prioritizes Atomic Theory (9 turns) then Nuclear Fission path. Zero expansion, zero wonder focus - all resources to terminal assault. Spies in Amsterdam ready for sabotage when network peaks; Cusco network already massive for military intelligence.

- Replay: use_nuke 60 => 50 (Δ -10), nuke 100 => 80 (Δ -20)
> Maintain conquest focus with high emphasis on military production, training, and offensive capabilities. Prioritize science to close tech gap with Ottomans' 79 techs vs our 64. Slightly reduce nuclear use given Ottomans share Order ideology. Maintain strong military stance to enable decisive action against key rivals threatening victory conditions.

## Sonnet-4.5-Simple - Turn 386 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-5`

- Original: use_nuke 80 => 90 (Δ +10), nuke 80 => 80 (Δ +0)
> Maintaining Conquest strategy with adjustments for nuclear-enabled endgame. Advanced Ballistics now allows tactical nuclear strikes against fortified capitals Onondaga and Amsterdam. Increasing UseNuke from 80→90 to enable decisive nuclear employment when conventional assault proves costly. Keeping Offense 80, Mobilization 72, and Nuke 80 for combined arms operations. Montreal at 35% health indicates current force composition is effective. Mobile Tactics (9 turns) will provide Mechanized Infantry for exploitation. With 62% domination progress and overwhelming 5:1 military superiority, this is the final push phase requiring maximum offensive pressure while maintaining strategic nuclear deterrence option.

- Replay: use_nuke 80 => 70 (Δ -10), nuke 80 => 75 (Δ -5)
> Maintaining Conquest grand strategy as we control 62% of capitals and are at war with The Iroquois. Emphasizing Mobile units and Offense to capitalize on Modern Armor upgrades. Increasing Defense slightly to protect our vast empire and conquered cities. Maintaining high Production and Mobilization for military output. Adjusting Gold and Happiness priorities to address our economic strain and unhappiness issues which are causing combat penalties. Keeping Air and Nuke options available as strategic deterrents as we approach endgame.

## GLM-4.7-Simple - Turn 499 - retry 3

**Deviation (replay vs original):** use_nuke `-60`, nuke `-20`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Maximum Science (100) and Production (100) to accelerate Stealth research and subsequent Stealth Bomber construction for air parity. Air (100), Defense (100), Antiair (100), and CityDefense (85) address existential threat from Russia's 8 Stealth Bombers by prioritizing air defense infrastructure and protecting homeland. UseNuke (100) and Nuke (100) maintain nuclear deterrence posture after Russia's 2 SS Boosters - Russia must understand that launching would trigger our response despite lacking uranium stockpile. Espionage (100) maxed to monitor Russian spaceship part production in Moscow, Yekaterinburg, and key cities - our 10 spies in Russian cities provide critical intelligence on their victory timeline. Diplomacy reduced to 5 since World Congress voting is now; alliances with England and The Celts (Autocracy-aligned) should naturally align against Russia's UN proposal. Spaceship flavor set to 0 as Stealth research takes immediate precedence - spaceship parts scheduled once production capacity supports parts with Stealth Bomber protection.

- Replay: use_nuke 50 => 40 (Δ -10), nuke 100 => 80 (Δ -20)
> Russia is dangerously close to multiple victories (50% spaceship parts, 62% capitals, 53% delegates). With strongest military but 0% spaceship progress, must urgently prioritize spaceship part production. Keeping high defense/airpower capabilities to protect production cities while accelerating science and spaceship construction. Slightly adjusted offense/recon to focus resources on victory production rather than expansion.

## Deepseek-3.2-Simple - Turn 469 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `-15`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> The Netherlands is at 84% diplomatic victory; we must accelerate capture of Polynesian capitals (Honolulu, Assur) to achieve domination before they win. Increasing UseNuke and Nuke flavors prepares for nuclear strikes if conventional assault fails. Maintaining maximum Offense, Defense, Mobilization ensures continuous unit production. Science and Gold are critical for researching Stealth Bombers and purchasing units. Happiness offsets war weariness, and Espionage protects our science cities.

- Replay: use_nuke 90 => 80 (Δ -10), nuke 90 => 85 (Δ -5)
> Increased Defense to 90 and CityDefense to 100 to better withstand multiple wars. Slightly reduced Offense to 85 to focus more on holding ground. Boosted Culture to 40 (from 0) to support tourism development needed for The Internet boost. Maintaining high production, gold, science for continued military competitiveness and future space race if opportunity arises. Air at 100 and Antiair at 100 for air superiority crucial in late-game warfare.

## Kimi-K2.5-Briefed - Turn 403 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `-15`

- Original: use_nuke 80 => 85 (Δ +5), nuke 80 => 90 (Δ +10)
> Post-Manhattan Project completion (Turn 399) with Turn 403 WC vote imminent. Reduced Offense from 15 to 10 as territorial expansion counterproductive to diplomatic win. Maintaining high Defense/CityDefense/Air/Antiair to protect Bregenz nuclear facility and core cities. Increased Nuke from 80 to 90 to prioritize atomic bomb production for deterrence (Iroquois 5883 vs 4502 strength ratio). UseNuke 85 reflects imminent atomic capability by Turn 405. Espionage 85 continues election rigging in Assur/Sogut against German influence. Diplomacy 100 and Gold 90 prioritize Assur delegate acquisition post-quest and future WC coordination. Science 85 drives Nuclear Fission for World Ideology proposal. Freedom bloc currently holds 59 delegates (Austria 29 + Germany 20 + Venice 10) vs 45 needed; maintaining solidarity while pursuing additional delegate sources.

- Replay: use_nuke 80 => 70 (Δ -10), nuke 80 => 75 (Δ -5)
> Maintain United Nations as primary goal. Reduce nuclear offense slightly (from 80 to 75) and UseNuke (from 80 to 70) since Iroquois are below the 3,500-strength nuclear trigger threshold and we're 3+ turns from Nuclear Fission completion. Increase Defense focus (85) for Grand River crisis while maintaining strong Air (85) and Antiair (80) for future air superiority. Gold at 100 (from 95) to maximize city-state influence and spaceship part purchase flexibility through Space Procurements. Maintain high Diplomacy (100) for upcoming World Congress votes.

## Kimi-K2.5-Simple - Turn 384 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maximum offensive posture for existential cultural war. UseNuke 100 and Nuke 100 authorize nuclear strikes on Dutch cultural centers (Amsterdam/Rotterdam/Utrecht) to destroy tourism buildings before Netherlands influences Austria in 6 turns. Mobile 100 and Air 100 enable rapid strikes. Production 100 and Mobilization 100 ensure nuclear missile replacement. Netherlands at 97% with Austria - only 6 turns left. Must destroy their tourism NOW or lose cultural victory.

- Replay: use_nuke 95 => 80 (Δ -15), nuke 100 => 90 (Δ -10)
> Continuing aggressive conquest focus. I'm winning wars (score 100% vs Aztecs, strong vs Netherlands) but lost Satricum to Rome. High offense, mobile, air, and production flavors needed to push offensives. Increased nuclear preparation as I'm in Atomic era with 5 uranium. Airlift priority for rapid troop deployment across three warfronts.

## Kimi-K2.5-Simple - Turn 392 - retry 2

**Deviation (replay vs original):** use_nuke `-25`, nuke `-20`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Nuclear Fission complete - MAXED Nuke to 100 and UseNuke to 95 for immediate atomic deterrent deployment against Egyptian forces. WC vote in 4 turns with exactly 45 delegates (28 Poland + 8 Inca + 9 Denmark). Cannot afford to lose Melbourne/Yerevan. Raised Diplomacy to 90 to consolidate CS alliances post-war. Defense remains at 95 against Egyptian naval pressure. Science/Production maintained for military infrastructure.

- Replay: use_nuke 85 => 70 (Δ -15), nuke 95 => 80 (Δ -15)
> UnitedNations victory approach: maintain strong defense (Defense 80) and military readiness (CityDefense 85, MilitaryTraining 70) while being visibly cooperative. High Diplomacy (85) continues city-state focus. Increase Gold (85) and Culture (70) for vote influence/Great People. Rationalize extremes: reduce Navy (90→70) and Antiair (90→70) flatten risk range. Lower Mobilization (85→60). Slight increase in Science (80) and Production (85) for infrastructure. Keep moderate Offense (40) for war-redemption options.

## GLM-4.7-Briefed - Turn 424 - retry 3

**Deviation (replay vs original):** use_nuke `-25`, nuke `-5`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 95 (Δ +0)
> URGENT RECALIBRATION: India Influential over 6/6 civs. Nuke/UseNuke maxed at 95 for immediate Great Works destruction via nuclear strikes when air superiority achieved. Air raised to 95 to achieve that superiority and conduct recon of Indian cultural sites. Antiair 80 counter potential Indian SAM sites. Offense/Mobile increased to 85/80 for aggressive India campaign while Greece distracts. Production/Science to 100 - PRIORITY for Apollo Program and spaceship parts racing India's potential final wonder. Espionage 95 to detect if India constructing Citizen Earth Protocol. Happiness 90 prevents war-weariness escalation during extended conflict if needed.

- Replay: use_nuke 85 => 70 (Δ -15), nuke 95 => 90 (Δ -5)
> Rebalancing flavors for late-game push toward Science Victory while maintaining military readiness. Increased Defense and CityDefense to protect our cities and spaceship production facilities. Maintained high Science (100), Production (100), Spaceship (100), Espionage (90), and Nuke (90) to prioritize science victory progression and deterrence. Modestly reduced Offense and Mobile to focus on strategic rather than expansionist warfare. High Antiair (80) to counter enemy air threats. Maintained strong Diplomacy (70) for World Congress influence. Kept Happiness at 80 to sustain Golden Age productivity bonuses.

## Deepseek-3.2-Simple - Turn 449 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> Russia is nearing science victory (2 parts completed) and possesses overwhelming military strength (95k). We must increase nuclear readiness to potentially decimate Russian forces and cities, and begin preparing for science victory as a backup by raising Spaceship flavor to 30. All other flavors remain focused on total war: high offense, naval, air, and espionage to counter Russia's tech lead and military dominance.

- Replay: use_nuke 85 => 70 (Δ -15), nuke 95 => 90 (Δ -5)
> Adjusting strategy to address critical weaknesses: reducing excessive aggression given economic strain (-1378 GPT) and Russia's military superiority; increasing Gold and Science to 100 to address severe deficit and catch up to Russia's space race lead; strengthening defensive posture (Defense 80, CityDefense 85) to protect current conquests; maintaining strong air/naval capabilities for power projection; keeping Diplomacy and Espionage high for World Congress leverage and intelligence.

## Kimi-K2.5-Simple - Turn 405 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-15`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 405 MAXIMUM EMERGENCY: Nuclear Fission priority increased to 100/100 - Manhattan Project completes in 2 turns, atomic bombs MUST be produced immediately. All offensive parameters at absolute maximum: 100 Offense/100 Mobilization/100 Mobile/100 Air/100 Nuke/100 UseNuke. Strike forces at Ecbatana/Kar-Tukulti-Ninurta must execute immediate conventional assault on Palenque/Chichen Itza while preparing tactical nuclear strikes. ZERO tolerance for peace. ONLY objective: capture Maya cities and halt Citizen Earth Protocol. Production 100 ensures rapid unit replacement. Espionage 70 continues spy operations in Maya cities.

- Replay: use_nuke 95 => 80 (Δ -15), nuke 95 => 85 (Δ -10)
> Continue conquest strategy against Maya and Sweden. Nuclear Fission is critical for atomic weapons deterrent against culturally-dominant Maya. High air/mobile focus for rapid campaigns. Increased science to close tech gap with Maya (they lead 67 vs 61 techs). Mopping up betrayal city-states (Zuunmod, Melbourne, Mombasa, Okilis) while main force presses Maya.

## GLM-4.7-Simple - Turn 407 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Spaceship victory focus with maximum defense against superior enemies (Poland 40K, Celts 16K, Spain 26K vs Iroquois 5K). Increased UseNuke to 90 - captured Polish territory and recent Celtic aggression justify nuclear deterrent. Adjusted Naval to 65 - important for defending coastlines from Spain/Celts/Poland fleets. Science 100 for Apollo and spaceship parts. Defense/CityDefense/Mobilization 100 - survival priority. Growth 60 for specialist support. Diplomacy 80 for World Congress in 4 turns (10 delegates). Offense reduced to 5 - preserve limited forces.

- Replay: use_nuke 85 => 70 (Δ -15), nuke 100 => 90 (Δ -10)
> Reducing excessive mobilization (100->60) and offense (10->30) to address gold deficit (-72) while maintaining strong defense (90) and nuclear deterrence. Increased happiness (90) and growth (70) focus to address unhappiness crisis. Science (90) and spaceship (80) remain high priority. Espionage (95) increased for counterintelligence against Spain and Poland who have spies in my cities.

## Sonnet-4.5-Simple - Turn 386 - retry 1

**Deviation (replay vs original):** use_nuke `-25`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 80 => 80 (Δ +0)
> Maintaining Conquest strategy with adjustments for nuclear-enabled endgame. Advanced Ballistics now allows tactical nuclear strikes against fortified capitals Onondaga and Amsterdam. Increasing UseNuke from 80→90 to enable decisive nuclear employment when conventional assault proves costly. Keeping Offense 80, Mobilization 72, and Nuke 80 for combined arms operations. Montreal at 35% health indicates current force composition is effective. Mobile Tactics (9 turns) will provide Mechanized Infantry for exploitation. With 62% domination progress and overwhelming 5:1 military superiority, this is the final push phase requiring maximum offensive pressure while maintaining strategic nuclear deterrence option.

- Replay: use_nuke 80 => 65 (Δ -15), nuke 80 => 80 (Δ +0)
> Information era with domination victory priority. Maintain Conquest strategy to finish capturing Iroquois capital (Onondaga) for domination victory. Increased Mobile offense to 80 for Modern Armor blitz tactics. Air power elevated to 80 for strategic bombing campaigns. Gold and Production prioritized to address negative GPT (-65) through commerce and military logistics. Happiness raised to 90 to combat current unhappiness (48%) causing penalties. UseNuke moderate at 65 for potential strategic options against Iroquois. Defense and CityDefense around 60 as focus is on offensive operations rather than holding territory.

## GLM-4.7-Simple - Turn 356 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 60 (Δ -15), nuke 85 => 90 (Δ +5)
> Shift Spaceship victory strategy with emphasis on ending wars and stabilizing empire. Raised Happiness to 90 (critical at 39% with combat penalty), reduced Defense from max to 70 as we need offense to finish Persia war. Increased Offense to 50, Mobilization to 85 for war effort. Science maxed at 100 to maintain research lead. Production at 95 for spaceship parts and military. Added Nuke focus (90) as Nuclear Fission unlocks. Reduced Air slightly from 90 to 85. Diplomacy boosted to 70 to work with Netherlands. Espionage at 85 to protect science from India/Pakistan spies. Focus on winning wars then pivoting to spaceship construction.

## Kimi-K2.5-Briefed - Turn 383 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CRITICAL WORKER REALLOCATION: Reduced Infrastructure from 100 to 20 to free the 7 Builders currently tied to railroad projects. Military briefing confirmed all workers occupied on railroads while 6 aluminum tiles remain unimproved despite TileImprovement 100. Aluminum crisis (-5/turn, 26 turns remaining) threatens Yamato production and bomber upgrades. Maintained TileImprovement 100 and Production 100 to prioritize aluminum mine construction once workers freed. Nuclear Fission completes in 6 turns - need Advanced Ballistics next for Nuclear Missile and Yamato. UseNuke increased to 100 to enable atomic strikes on Cusco immediately upon availability. AirCarrier 100 ensures carriers for Yamato deployment. Conquest remains correct grand strategy - Cusco is final capital for domination victory.

- Replay: use_nuke 95 => 80 (Δ -15), nuke 100 => 100 (Δ +0)
> Maintaining conquest focus against The Inca. Slightly reducing excessive military training to free production capacity for critical resource extraction (aluminum mines) and infrastructure. Keeping high offense, production, and air capabilities to press the war. Gold and happiness receiving modest boosts to address the -900 G/turn deficit and 38% happiness with combat penalty.

## Kimi-K2.5-Briefed - Turn 396 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-20`

- Original: use_nuke 65 => 80 (Δ +15), nuke 80 => 90 (Δ +10)
> ETHIOPIA CULTURAL VICTORY IMMINENT: Ethiopia has INFLUENCED ALL 7 CIVS and reached Order:3. They need only adopt CEP tenet and build it to win immediately. Switching to CONQUEST grand strategy with maximum mobilization (100) and offense (95). Naval (95) and Airlift (80) priorities enable rapid amphibious assault on Ethiopian coastal cities (Lalibela, Axum, Gondar) to destroy CEP before construction. Espionage (90) to accelerate Salem rig for delegate, but military solution is primary. All economy/culture deprioritized - this is existential war.

- Replay: use_nuke 65 => 50 (Δ -15), nuke 80 => 70 (Δ -10)
> Shift slightly from overly offensive posture to more balanced strategy: reduced Offense (60) and increased Defense (70) to better protect empire while focusing on science progress. Science maximized (98) and Spaceship focus (92) for victory pursuit. Diplomacy (85) remains high for World Congress preparation against Greece. Naval (80) and Air (80) maintained for coastal security and future Yamato battleships. This balances science victory goals with necessary military preparedness against Ethiopia/Greece threat.

## Kimi-K2.5-Briefed - Turn 373 - retry 1

**Deviation (replay vs original):** use_nuke `-25`, nuke `-30`

- Original: use_nuke 90 => 95 (Δ +5), nuke 90 => 100 (Δ +10)
> CRITICAL ADJUSTMENTS for Brazil tech lead (66-65): Espionage to 100 for maximum spy operations to steal techs and catch up. GreatPeople to 95 for more Great Scientists. Defense/CityDefense increased to 60/70 - Brazil may attack seeing their lead. Nuke/UseNuke at 100/95 - we need deterrent ASAP. Diplomacy up to 70 - must prioritize repealing sanctions to unlock trade. Science/Production/Spaceship remain 100. Gold reduced to 80 - focus on production over purchases. All military offense minimized - we cannot afford war.

- Replay: use_nuke 90 => 70 (Δ -20), nuke 90 => 70 (Δ -20)
> Adjusting for late-game science victory pursuit: Reduced extreme nuclear focus (70 instead of 90) as immediate threat is lower. Increased Gold (90) and Diplomacy (80) to facilitate aluminum trade deals and World Congress vote management for sanction repeal. Increased Production (90) for spaceship parts and Research Labs in cities lacking them. Maintained high Science/Spaceship focus as primary victory path. Defense stays at 50 for sufficient deterrence against Brazil.

## Kimi-K2.5-Simple - Turn 482 - retry 1

**Deviation (replay vs original):** use_nuke `-25`, nuke `-20`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> NINEVEH FALLEN - EMERGENCY SURVIVAL MODE: Rome captured Nineveh on Turn 480 (23 population city lost). Portugal's diplomatic victory FAILED (still at 35/43 delegates). Rome now at war with me AND Ottomans. With 1,505 vs 52,754 military strength, direct confrontation is impossible. PIVOT TO SPACESHIP as only viable path - Science 100, Spaceship 80. Continue Defense 100, CityDefense 100, Nuke 100 with UseNuke 95 for area denial. Must survive long enough to reach Information era and build spaceship components while Rome's attention splits between me and Ottomans.

- Replay: use_nuke 90 => 70 (Δ -20), nuke 100 => 80 (Δ -20)
> Critical defensive situation: Nineveh lost to Rome, enemy forces overwhelming on multiple fronts (Rome: 52,754 strength vs my 1,505). Must prioritize survival - defense + gold to fix -71 GPT economy before researching Stealth. Austria also hostile. Diplomatic victory increasingly unlikely with sanctions and Portugal dominant (35 delegates).

## Kimi-K2.5-Simple - Turn 373 - retry 3

**Deviation (replay vs original):** use_nuke `-25`, nuke `-20`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 373: Nuclear Fission completed - we now have nuclear weapons for deterrence. War with Russia continues at +4% score (favorable). Major shift: reducing Offense to 25 (was 35) as we pursue defensive war only. UseNuke increased to 95 - we have actual nukes now and Russia is pushing into our territory. Reduced Espionage to 90 (was 95) - we have good network coverage. Increased Diplomacy to 90 (was 85) - World Congress vote in 7 turns for our World Ideology: Freedom proposal is critical. Must secure Korea (10 votes), Inca (9), and Babylon (16). Maintained maximum Science priority (100) - Korea overtook us 67-66, cannot afford to fall behind in tech race.

- Replay: use_nuke 90 => 70 (Δ -20), nuke 100 => 80 (Δ -20)
> Focus primarily on Science Victory by prioritizing research, spaceship part production, and protecting core infrastructure. Maintain strong defense against Russia with elevated military training and city defense flavors. Slightly reduce offensive focus as we're in a defensive war posture. Increase Diplomacy flavor to leverage World Congress for World Ideology proposals and secure votes. High Espionage to protect high science cities from Russia's spies. Moderate UseNuke for deterrence without reckless escalation.

## Deepseek-3.2-Briefed - Turn 387 - retry 3

**Deviation (replay vs original):** use_nuke `-50`, nuke `-30`

- Original: use_nuke 70 => 100 (Δ +30), nuke 70 => 100 (Δ +30)
> We are in the final push for domination victory. We must capture Moson Kahni and London. To achieve this, we need to prioritize building transport ships for amphibious assault and achieve air superiority. Maximizing flavors for naval, air, mobile, and nuclear units ensures the in-game AI focuses production on these critical areas. Deprioritizing non-essential areas like culture, religion, and expansion concentrates our efforts on military conquest.

- Replay: use_nuke 70 => 50 (Δ -20), nuke 70 => 70 (Δ +0)
> Maintain conquest focus due to active wars with Shoshone and Brazil. Slightly reduced extreme bias (Offense 95 vs 100) is more sustainable. Increased Defense and CityDefense to 75 from 70 to handle multi-front wars better. Reduced AirCarrier from 100 to 90 to balance production. Maintaining high Happiness (90) priority to address deficits in several cities. Increased GreatPeople to 85 to synergize with Avant Garde. Reduced UseNuke from 70 to 50 - nuclear weapons should be a strategic deterrent, not standard combat option. Science at 90 maintains tech parity against Shoshone.

## GLM-4.7-Simple - Turn 499 - retry 1

**Deviation (replay vs original):** use_nuke `-70`, nuke `-20`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Maximum Science (100) and Production (100) to accelerate Stealth research and subsequent Stealth Bomber construction for air parity. Air (100), Defense (100), Antiair (100), and CityDefense (85) address existential threat from Russia's 8 Stealth Bombers by prioritizing air defense infrastructure and protecting homeland. UseNuke (100) and Nuke (100) maintain nuclear deterrence posture after Russia's 2 SS Boosters - Russia must understand that launching would trigger our response despite lacking uranium stockpile. Espionage (100) maxed to monitor Russian spaceship part production in Moscow, Yekaterinburg, and key cities - our 10 spies in Russian cities provide critical intelligence on their victory timeline. Diplomacy reduced to 5 since World Congress voting is now; alliances with England and The Celts (Autocracy-aligned) should naturally align against Russia's UN proposal. Spaceship flavor set to 0 as Stealth research takes immediate precedence - spaceship parts scheduled once production capacity supports parts with Stealth Bomber protection.

- Replay: use_nuke 50 => 30 (Δ -20), nuke 100 => 80 (Δ -20)
> Late-game strategy: Strong defense against Russian aggression while maintaining air superiority and anti-air capabilities (Russia has Stealth Bombers). Prioritizing gold for diplomatic purchases and science for tech parity. Nuclear arsenals at 80% for strategic deterrence. Reducing Spaceship priority as victory impossible in 2 turns. Diplomacy increased for post-U.N. vote preparation.

## Kimi-K2.5-Briefed - Turn 336 - retry 2

**Deviation (replay vs original):** use_nuke `-40`, nuke `-10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> DEFENSIVE SURVIVAL PIVOT: Peace with Shoshone (accepted Turn 335) closes one front, but India remains existential threat (4,742 MS vs my 2,405, 98% control of Denmark). Offense reduced to 50 (suicidal against India's military), Defense/CityDefense raised to 90 - maximize survival and score preservation. Nuke/UseNuke maxed to 100 - emergency deterrent only hope to slow India. Mobilization stays high (90) to replace losses. Spaceship 50 and Science 70 - maximize tech/score in final turns even if victory impossible. Abandon expansion (0) - no time for new cities. Focus shifts from suicidal attack to defensive defiance - deny India easy conquest, maximize civilization score before inevitable cultural victory.

- Replay: use_nuke 80 => 60 (Δ -20), nuke 90 => 90 (Δ +0)
> Increase Offense to 90 for aggressive action against India to stop their cultural victory. Mobilization and Production prioritized for rapid military buildup. Science increased to 70 to catch up to India's Atomic-era tech lead. Tourist increased to 70 to boost cultural output as secondary path. UseNuke reduced but Nuke kept high as deterrent consideration.

## Kimi-K2.5-Simple - Turn 426 - retry 2

**Deviation (replay vs original):** use_nuke `-40`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE - NUCLEAR DETERRENT 10 TURNS AWAY: Lisbon holds at 7% but is in extremis. Maintain absolute priority on Defense/CityDefense/Mobilization (100) to reinforce Lisbon and prevent collapse. Nuclear Fission completes in 10 turns enabling Atomic Bomb construction - Science 100 accelerates this. UseNuke increased to 100 for immediate tactical nuclear deployment against Aztec concentrations upon tech completion. Offense reduced to 20 - no offensive operations, pure defensive hedgehog posture. Zero expansion capability. Spaceship 75 maintains backup victory if diplomatic block succeeds.

- Replay: use_nuke 80 => 60 (Δ -20), nuke 100 => 100 (Δ +0)
> Situation stabilized with strong defensive posture. Portugal is nearly defeated, while Aztec attacks on Funchal are being repelled. Transitioning to defensive Conquest strategy - we'll build strong city defenses and use nuclear deterrence to protect our gains. Researching Advanced Ballistics to unlock nuclear missiles as strategic deterrent. Focus on nuclear weapons production, defense, ranged units, and espionage to maintain technological parity. Our strength is in land warfare, so prioritize units that excel in fighting near our cities with Amphibious and War Canoes promotions.

## GLM-4.7-Simple - Turn 435 - retry 1

**Deviation (replay vs original):** use_nuke `-30`, nuke `-20`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Iroquois 97% Popular - cultural extinction in 3-4 turns. Maximum offensive posture required to capture Onondaga before cultural victory. Espoo Stealth Bomber complete provides immediate air strike capability. Linköping Stealth Bomber in 4 turns is too slow - must use existing air assets and conventional forces at Genesse River NOW. UseNuke 100 authorizes nuclear strikes if conventional forces cannot reach Onondaga in time. All production and resources prioritized for war. Diplomacy irrelevant when facing extinction - complete conquest or nothing matters.

- Replay: use_nuke 90 => 70 (Δ -20), nuke 100 => 80 (Δ -20)
> Prioritize happiness to address unhappiness crisis. Maintain high military but slightly reduce offense due to war weariness. High diplomacy for World Congress votes and alliance management. High production/gold for military sustainability. High science/nuclear as we're in Information era with nuclear threat.

## Deepseek-3.2-Simple - Turn 445 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-20`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximizing UseNuke to 100 ensures our atomic bombs and future nuclear missiles are used aggressively against The Celts' military concentrations and cities, given their overwhelming advantage. Maintaining high Air, Naval, and Nuke flavors sustains our technological edge and production focus. Diplomacy and Espionage at 100 are critical for city-state alliances and spy missions to gain delegates for diplomatic victory. Gold and Science remain top priorities to fund our war effort and tech progression. Other military flavors are tuned for a multi-front defensive-offensive war against The Celts, Germany, and Ethiopia.

- Replay: use_nuke 90 => 70 (Δ -20), nuke 100 => 80 (Δ -20)
> Adjusting flavors to better balance United Nations pursuit with ongoing wars. Slightly reducing UseNuke to 70 (from 90) - keep nuclear as deterrent, not first-strike. Offense reduced to 65, Defense increased to 88 - focus on holding gains and protecting territory. Diplomacy maxed at 95 for UN votes, Espionage 90 for city-state operations. Gold 90 for maintaining city-state alliances.

## Deepseek-3.2-Simple - Turn 495 - retry 1

**Deviation (replay vs original):** use_nuke `-30`, nuke `-5`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 90 (Δ +0)
> Diplomatic victory is imminent (2 turns), but we must prepare for contingencies. Maximizing Offense, UseNuke, and Air ensures aggressive nuclear and conventional strikes to recapture Indonesian capitals (Honolulu 17%, London 68%) and prevent their domination victory. Slight Diplomacy boost helps secure city-state alliances through the vote. All other flavors remain at previous high levels to maintain total war footing.

- Replay: use_nuke 90 => 70 (Δ -20), nuke 90 => 85 (Δ -5)
> Diplomatic victory is imminent with 42/42 delegates needed and UN voting in 3 turns. Prioritize diplomacy and gold to maintain city-state alliances while keeping military strength high against Indonesia. Nuclear deterrent needed after Indonesia's recent nuclear attack on Nottingham. Production focused on spaceship parts as backup victory path if diplomatic route fails.

## Kimi-K2.5-Simple - Turn 392 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-15`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> SURVIVAL MODE - GERMAN BETRAYAL RESPONSE: Germany's invasion is catastrophic. Reduced Offense to 40 (cannot attack superior forces), maintained Defense/CityDefense/Antiair at 100 to survive siege. Science 100 and Nuke/UseNuke 100 are existential priorities - atomic weapons only hope against 13k German military. Production 100 for emergency unit production. Espionage 100 to maintain Florence alliance and protect Kyzyl. Reduced Diplomacy to 90 (lost Lisbon/Sokoto/Buenos Aires to German coups). Naval reduced to 70 (coastal cities threatened by Germany). Focus: Hold cities, survive until nuclear deterrent operational.

- Replay: use_nuke 90 => 70 (Δ -20), nuke 100 => 85 (Δ -15)
> Shifting from pure Conquest (unsustainable against superior German/French forces) to defensive Science/Culture hybrid. Reducing offense and military training to conserve resources while maintaining strong defensive posture. Prioritizing happiness (critical at 42% with combat penalty), science (for nuclear deterrent and tech parity), and culture (leverage existing tourism infrastructure). High Air and Antiair to counter German air superiority, high Nuke/UseNuke for potential strategic deterrent against overwhelming conventional forces. Maintaining production and gold for defensive infrastructure.

## Kimi-K2.5-Simple - Turn 372 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-20`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 372: TOTAL WAR POSTURE MAINTAINED. Brazil peace expires in 6 turns - all military resources must prepare for Rio de Janeiro assault. Heavy Bomber lost to Alexandria interception but Ollantaytambo produces replacement in 1 turn. Manhattan Project completes in 4 turns at Cusco. Alexandria capture in progress - Field Gun and Lancer eliminated, Cavillaca spy at 480 network can assist. UseNuke increased to 100% - will deploy nuclear weapons immediately upon Manhattan Project completion. Maximum aggression ensures AI prioritizes Brazilian invasion over defensive operations. Spaceship at 70 maintains science victory pathway as backup if Brazil conquest fails.

- Replay: use_nuke 95 => 70 (Δ -25), nuke 100 => 80 (Δ -20)
> Refocusing from extreme aggression to balanced approach: maintain Spaceship as primary goal with high science/production, but reduce excessive offensive mobilization (70 vs 100) to sustain wars more efficiently. Increase naval focus (85) to rebuild after cruiser loss to Babylon. Maintain emphasis on air power and mobile units for strategic flexibility while preparing for nuclear deterrent against Byzantium's military dominance.

## Kimi-K2.5-Simple - Turn 387 - retry 2

**Deviation (replay vs original):** use_nuke `-75`, nuke `-30`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> TURN 387: MAXIMUM WAR FOOTING. Austria at 83% diplomatic victory with 4 turns remaining. All resources must pivot to immediate military production. Nuke/UseNuke at 100 for instant atomic weapon deployment upon Nuclear Fission completion. Offense/Mobilization/Production at 100 to maximize unit output for desperate Vienna strike. Air at 90 for heavy bomber production (conventional strategic bombing as fallback). Antiair at 100 counters Austria's air superiority. Diplomacy/Wonder/Culture at 0 - no time for long-term investments. Only total war can prevent defeat.

- Replay: use_nuke 50 => 25 (Δ -25), nuke 100 => 70 (Δ -30)
> Pivoting from ineffective conquest to United Nations grand strategy. Austria dominates diplomatic victory (83% progress) with Order ideology bonus. While I cannot win delegate race directly, I can delegate heavily and counter Austria's proposals. Focus on gold (for city-state envoy purchases), science (to stay competitive), and defense (to protect against Austria stronger military). Maintaining nuclear deterrence (70/25 UseNuke) for security while reducing offensive aggression. This supports allied coalition (Carthage, Songhai, America, Portugal) against Austria without warmongering penalties.

## Kimi-K2.5-Simple - Turn 421 - retry 2

**Deviation (replay vs original):** use_nuke `-30`, nuke `-15`

- Original: use_nuke 75 => 80 (Δ +5), nuke 95 => 95 (Δ +0)
> APOLLO PROGRAM CONSTRUCTION - ALUMINUM CRISIS: Turn 421, Apollo Program 9 turns from completion in Venice (220 Production/turn). Critical flavors: Production 100/Science 100/Spaceship 100 for rapid wonder and parts construction. Gold 90 for Aluminum acquisition via trade with Songhai (29 stockpile) or China peace deal (14 stockpile). Defense 95/Antiair 90/Nuke 95/UseNuke 80 against Egyptian XCOM encirclement (22,000 vs 2,183 military, 10:1 ratio). Egypt has 5 XCOM Squads, Mechanized Infantry, Mobile SAM, Fighter, Rocket Missile in adjacent Nara zone - existential threat. Air 85 for fighter production to defend against Egyptian heavy bombers. Zero Aluminum available - must acquire 4+ Aluminum BEFORE Apollo completion or spaceship parts cannot be built. India at 88% diplomatic victory with vote in 2 turns - if they win, game over. If Egypt completes spaceship first (33% progress, 2 parts done), game over. This is final sprint for survival.

- Replay: use_nuke 75 => 50 (Δ -25), nuke 95 => 80 (Δ -15)
> Increase Diplomacy and Espionage focus to counter India's World Congress threat (voting in 2 turns). Maintain high Production, Science, and Defense for Spaceship components and security. Boost Gold to address -164 GPT deficit and resource shortages (Aluminum, Coal). Moderate Nuke usage while maintaining nuclear arsenal as strategic deterrent against Egypt's dominance. Support mobile/ranged/air units for defending against China.

## Kimi-K2.5-Briefed - Turn 382 - retry 1

**Deviation (replay vs original):** use_nuke `-30`, nuke `-35`

- Original: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> EMERGENCY DIPLOMATIC RECOVERY: The city-state flipping operation failed to execute. With only 36 delegates and 5 turns until World Congress vote, I need maximum Diplomacy (100) and Gold (100) to execute immediate city-state purchases. Reduced Mobilization to 40 and Offense to 15 to free supply and focus on defensive deterrence. Increased Nuke/UseNuke to 95/80 as deterrent against Russian aggression while I secure delegates. Defense/Antiair remain at 90 for Russian containment. Must acquire 8+ delegates before vote or World Ideology: Order will fail.

- Replay: use_nuke 75 => 50 (Δ -25), nuke 90 => 60 (Δ -30)
> Rebalanced military flavors from extreme defense (90-100) to moderate levels (50-70) that provide adequate security without over-investment. Maintained high priority on Gold (100) and Diplomacy (100) to fuel city-state investments for the 8 additional delegates needed. Reduced offense and war-related flavors to appear less threatening while keeping strength to defend achievements. Kept Science (70) and Espionage (70) high to support technology and protect against spies. Nuke flavors maintained at 60 for deterrent capability once Nuclear Fission completes.

## GLM-4.7-Simple - Turn 431 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-40`

- Original: use_nuke 75 => 80 (Δ +5), nuke 100 => 100 (Δ +0)
> After Brazil destroyed 3 anti-air units and continues nuclear-submarine attacks, increased Defense/CityDefense/Antiair/UseNuke to MAX for survival against two nuclear-armed superpowers. Mobilization 70 for replacing lost units. Production 100 for reconstruction. Science 100 for Spaceship path despite devastation. Gold 90 (economy -95 GPT deficit) for purchasing units/buildings. Happiness 100 - we're Unhappy with combat penalties, must prioritize. Espionage 100 - critical for intelligence on nuclear threats. Diplomacy 90 - World Congress in 7 turns, need delegates. Air 50 - build bombers for deterrence. GreatPeople 80 for Spaceship components. Decreased Growth and Navals as resources diverted to immediate survival.

- Replay: use_nuke 75 => 50 (Δ -25), nuke 100 => 60 (Δ -40)
> Survival adjustment under existential threat: Increased Happiness priority to combat low 43% rating (combat penalty). Increased Gold to critical 100 to address catastrophic -95 GPT economy. Increased Air defense to counter Brazil's bombers. Reduced Mobilization and Nuke focus to conserve resources. Increased Diplomacy priority to seek any possible peace or additional allies. Defense remains maximum to protect threatened cities. Spaceship reduced as unrealistic under current war conditions.

## Kimi-K2.5-Simple - Turn 417 - retry 2

**Deviation (replay vs original):** use_nuke `-40`, nuke `-40`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Pure survival mode: Eliminated Offense (0) since attacking is suicide. Maximized UseNuke (100) - must deploy tactical nukes against Aztec XCOM/Modern Armor stacks at Carthago Nova or lose the city. Increased Mobile (80) to prepare for Mechanized Infantry deployment. Maintained max Defense, Antiair (jet attacks are relentless), and Espionage (critical science quests in Panama City and Sokoto worth 1,000+ science each). Apollo Program completes in 5 turns - must transition immediately to parts production.

- Replay: use_nuke 90 => 60 (Δ -30), nuke 100 => 60 (Δ -40)
> Reducing military emphasis (Nuke, Air, Offense) to address -252 GPT crisis while maintaining strong defense against Aztec aggression. Prioritizing Science (100) for spaceship progress after Apollo completes. Increased Happiness (70) to combat Unhappy status. Maintaining Espionage (90) to protect science cities given our tech vulnerability.

## GLM-4.7-Simple - Turn 457 - retry 3

**Deviation (replay vs original):** use_nuke `-40`, nuke `+0`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Increased UseNuke to 80 and Air to 100 in response to England's catastrophic escalation this turn. English Giant Death Robots (now 2 in Atlanta zone) and XCOM Squad paradrops on American soil create existential threat to our 3 remaining cities. Recent combat losses (Modern Armor, Mechanized Infantry, Heavy Bomber destroyed) demonstrate conventional warfare impossibility. Nuclear deterrence with 2 Uranium is becoming survival necessity, not option. Air defense at maximum priority because English Strategic Bombing continues destroying our units (Fighter bombed our Heavy Bomber). Bazooka successfully damaging XCOM Squad near Washington proves defensive capability is still viable - prioritize air/anti-air to protect cities from English air superiority. Lasers completes in 4 turns, then Stealth for Stealth Bomber - only path to asymmetric defense against England's 45:1 military advantage. Assyria (18,443 military fighting England) must be maximized as counterweight.

- Replay: use_nuke 70 => 40 (Δ -30), nuke 100 => 100 (Δ +0)
> England's military (88,218) vastly outnumbers ours (1,929) and they have Giant Death Robots threatening our cities. While maintaining strong defense (90), I've increased offense (25) to allow counter-attacks against the invasion. Air superiority (90) is critical against England's air power. Military training and mobilization increased to rapidly strengthen our forces. Nuclear deterrence remains vital. Science and spaceship highest priority to catch up to England's 83% progress.

## Kimi-K2.5-Simple - Turn 393 - retry 3

**Deviation (replay vs original):** use_nuke `-35`, nuke `-20`

- Original: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 393: Survival mode continues. Morocco massing Modern Armor, XCOM Squads, Heavy Bombers on border - 7.5x military advantage. Dutch Global Hegemony vote in 3 turns is likely unwinnable but must try block. As Maya vassal, only Science/Time victories possible. Nuclear Fission in 9 turns remains ONLY hope for deterrent. Slightly increased UseNuke to 85 and Antiair to 80 to prepare immediate atomic strike capability and counter Moroccan air superiority. Max Defense/Science/Espionage flavors. Spies positioned in Marrakech (1146) and Amsterdam (1218) for maximum tech theft.

- Replay: use_nuke 80 => 50 (Δ -30), nuke 100 => 80 (Δ -20)
> Maintaining science victory focus with strong defensive posture.防御性军事态势确保研究安全，同时优先推进太空飞船部件的生产和科学研究。随着核裂变研究完成，将进入火箭技术与太空时代技术。继续平衡快速增长和太空竞赛优先级。

## Deepseek-3.2-Simple - Turn 485 - retry 3

**Deviation (replay vs original):** use_nuke `-50`, nuke `-10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> We are engaged in a multi-front war against superior forces. Increasing Ranged and Mobile ensures our bazooka and mechanized infantry production is prioritized for defense and counterattacks. Setting UseNuke to 100 guarantees we deploy nuclear weapons as soon as available to cripple The Huns' armies. Reducing Culture and Diplomacy reallocates focus to immediate military needs without compromising essential city-state relations (Monaco, Lisbon). Grand Strategy remains Conquest as nuclear strikes may enable capital captures, though we keep science victory as a backup.

- Replay: use_nuke 80 => 50 (Δ -30), nuke 90 => 80 (Δ -10)
> Shifting from conquest to culture - we already have strong tourism and 2 Tier 3 Freedom tenets. Reduced offense/mobilization addresses war weariness and gold deficit. Increased happiness (90) and culture (90) addresses combat penalty and accelerates cultural victory path. Maintain strong defense (90) and air power (90) for protection. Keeping nuclear deterrent (80) against stronger civs. Not reducing military training or science too much - still need strong military and research capabilities.

## Kimi-K2.5-Simple - Turn 435 - retry 1

**Deviation (replay vs original):** use_nuke `-40`, nuke `-30`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> TURN 435 CATASTROPHE - Sippar captured by Zulus! Existential crisis deepens. Zulus have 43/42 delegates needed for diplomatic victory with vote in 9 turns. Lasers completes in 6 turns, Spaceflight Pioneers in ~10. Maintaining absolute maximum Defense/CityDefense/Science/Production/Spaceship priorities. Increased UseNuke to 100 - if Zulus push further with their 74k military vs my 32k, nuclear deterrent may be only option to buy time. Lost Mechanized Infantry, Rocket Artillery, Mobile SAM, Special Forces, and Modern Armor in the fall of Sippar. Must hold remaining 5 cities while completing tech/policy for spaceship rush. Rome remains critical ally at 100/100.

- Replay: use_nuke 90 => 60 (Δ -30), nuke 100 => 70 (Δ -30)
> Reduce extreme nuclear stance after Sippar capture; focus on strong defense, air superiority, anti-air protection, spaceship production, espionage for tech security, and maintaining happiness while continuing Spaceship grand strategy.

## Deepseek-3.2-Simple - Turn 469 - retry 2

**Deviation (replay vs original):** use_nuke `-40`, nuke `-20`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> The Netherlands is at 84% diplomatic victory; we must accelerate capture of Polynesian capitals (Honolulu, Assur) to achieve domination before they win. Increasing UseNuke and Nuke flavors prepares for nuclear strikes if conventional assault fails. Maintaining maximum Offense, Defense, Mobilization ensures continuous unit production. Science and Gold are critical for researching Stealth Bombers and purchasing units. Happiness offsets war weariness, and Espionage protects our science cities.

- Replay: use_nuke 90 => 60 (Δ -30), nuke 90 => 80 (Δ -10)
> Refining Conquest strategy for current late-game situation: (1) Focus on DEFENSE (100) and CITYDEFENSE (100) to hold territory against multiple enemies while outnumbered. (2) Maintain strong OFFENSE (80), RANGED (80), and MOBILE (70) capabilities for counterattacks and opportunistic conquests. (3) Prioritize GOLD (90) for upgrading units and purchasing emergencies; SCIENCE (100) for tech parity; PRODUCTION (100) for military output. (4) Keep Nuke options (80) available as deterrent but reduce USENUKE (60) given global stability concerns. (5) High ESPIONAGE (100) for intel and counterintelligence. (6) Reduced MOBILIZATION (80) and OFFENSE (80) slightly from 100 to avoid overextending with limited gold maintenance. Maintaining aggressive posture but focusing on quality over quantity.

## GLM-4.7-Briefed - Turn 433 - retry 1

**Deviation (replay vs original):** use_nuke `-40`, nuke `-35`

- Original: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> EMERGENCY: Netherlands at 42 delegates can win diplomatic victory in 9 turns (turn 442). Only way to stop them is military action against their protected city-states (Quebec City, Ife, Melbourne) - each provides +1 delegate. Offense increased (70) to prepare amphibious assaults. Nuclear readiness maximized (95/90) - atomic bomb available for strategic coercion of Netherlands or Denmark cooperation. Mobile (80) and Naval (85) maximized for rapid deployment to distant city-states. Production/Science/Spaceship kept maxed as backup victory paths. Diplomacy reduced to 50 as traditional diplomacy cannot stop Netherlands' delegate advantage. Strategic shift from holding Danish front to aggressive anti-Dutch operations.

- Replay: use_nuke 80 => 50 (Δ -30), nuke 90 => 60 (Δ -30)
> Pivot from offensive invasion to more strategic approach: strengthen defenses to protect against Danish counterattack while maintaining naval/air mobility for targeted operations against Netherlands' city-state allies. Keep spaceship pursuit active as backup victory. Nuke capability preserved as strategic deterrent rather than immediate use due to single bomb limitation. Increased Science focus to maintain spaceship component advantage.

## Kimi-K2.5-Simple - Turn 435 - retry 2

**Deviation (replay vs original):** use_nuke `-40`, nuke `-30`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> TURN 435 CATASTROPHE - Sippar captured by Zulus! Existential crisis deepens. Zulus have 43/42 delegates needed for diplomatic victory with vote in 9 turns. Lasers completes in 6 turns, Spaceflight Pioneers in ~10. Maintaining absolute maximum Defense/CityDefense/Science/Production/Spaceship priorities. Increased UseNuke to 100 - if Zulus push further with their 74k military vs my 32k, nuclear deterrent may be only option to buy time. Lost Mechanized Infantry, Rocket Artillery, Mobile SAM, Special Forces, and Modern Armor in the fall of Sippar. Must hold remaining 5 cities while completing tech/policy for spaceship rush. Rome remains critical ally at 100/100.

- Replay: use_nuke 90 => 60 (Δ -30), nuke 100 => 70 (Δ -30)
> After losing Sippar to Zulu, shift to pure defensive posture while continuing science victory pursuit. Emphasize air power, naval defense, espionage (to monitor Zulu), and spaceship construction. Reduce offense given war weariness and military disadvantage. Science at 100 to outpace Zulus technologically.

## Kimi-K2.5-Simple - Turn 457 - retry 1

**Deviation (replay vs original):** use_nuke `-40`, nuke `-30`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FIRST-STRIKE PREPARATION: Manhattan Project completes in 2 turns. Denmark at 7/8 capitals (87.5% domination) - will win game if they capture 1 more capital. Spain's only hope is surprise nuclear attack the moment first Atomic Bomb is ready. Maximized Nuke/UseNuke/Production/Mobilization flavors to prepare for immediate atomic weapon production and deployment. Defense/Antiair high to survive Danish air superiority until then. All other priorities secondary to nuclear deterrent.

- Replay: use_nuke 95 => 60 (Δ -35), nuke 100 => 70 (Δ -30)
> Shift focus from conquest (I'm a vassal) to spaceship/science potential and internal development. Prioritize happiness to address combat penalty, science/production for spaceship parts and nuclear capability, and defense/protection. Maintain air superiority and ranged capabilities for defense.

## Deepseek-3.2-Simple - Turn 449 - retry 2

**Deviation (replay vs original):** use_nuke `-40`, nuke `-50`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> Russia is nearing science victory (2 parts completed) and possesses overwhelming military strength (95k). We must increase nuclear readiness to potentially decimate Russian forces and cities, and begin preparing for science victory as a backup by raising Spaceship flavor to 30. All other flavors remain focused on total war: high offense, naval, air, and espionage to counter Russia's tech lead and military dominance.

- Replay: use_nuke 85 => 50 (Δ -35), nuke 95 => 50 (Δ -45)
> Prioritizing Diplomacy (100) to secure the 25 additional delegates needed for diplomatic victory from city-states and allies before the vote in 5 turns. Increasing Gold (90) to address the critical -1378 GPT deficit. Reducing Offense (40) and UseNuke (50) to prevent excessive warmongering while maintaining strong Defense (80) and CityDefense (70) since Russia's military (95,829) is nearly double mine. Science (80) remains important as backup path to spaceship victory. MilitaryTraining (70) ensures units maintain quality but at sustainable cost.

## Kimi-K2.5-Simple - Turn 372 - retry 2

**Deviation (replay vs original):** use_nuke `-40`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 372: TOTAL WAR POSTURE MAINTAINED. Brazil peace expires in 6 turns - all military resources must prepare for Rio de Janeiro assault. Heavy Bomber lost to Alexandria interception but Ollantaytambo produces replacement in 1 turn. Manhattan Project completes in 4 turns at Cusco. Alexandria capture in progress - Field Gun and Lancer eliminated, Cavillaca spy at 480 network can assist. UseNuke increased to 100% - will deploy nuclear weapons immediately upon Manhattan Project completion. Maximum aggression ensures AI prioritizes Brazilian invasion over defensive operations. Spaceship at 70 maintains science victory pathway as backup if Brazil conquest fails.

- Replay: use_nuke 95 => 60 (Δ -35), nuke 100 => 100 (Δ +0)
> Pivot fully toward science victory by dramatically increasing Science, Production for spaceship parts, Spaceship flavor to 85. Maintain strong defenses (75-80) given Byzantium's military superiority. Keep nuclear deterrence capability (100) but reduce willingness to use offensively (60). Increase Gold (60) for maintaining relationships and upgrading key units. Boost Espionage (90) to protect high-value science cities and gather intelligence. Moderate offense (20) reflects prioritizing defense over conquest while finishing existing wars.

## GLM-4.7-Simple - Turn 427 - retry 2

**Deviation (replay vs original):** use_nuke `-40`, nuke `-40`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> United Nations grand strategy maintained - diplomatic victory in 6 turns (20 delegates vs Siam 17). Increased Gold (95) and Diplomacy (95) focus - need to secure UN delegate lead through city-state investment and diplomatic units. GreatPeople up to 80 for accelerated Great Scientist/Diplomat generation supporting both tech race and UN vote. UseNuke increased to 90 - with 6-7 Atomic Bombs building and Zulu military supremacy (134K vs 9.6K), nuclear deterrence is existential. Offense up to 55 to maintain Japan war momentum for capitulation. Air maintained at 85 for Stealth Bombers and air defense against Zulu threat.

- Replay: use_nuke 85 => 50 (Δ -35), nuke 100 => 60 (Δ -40)
> Shifting from total war to a diplomatic-focused defensive posture. Reducing offense/mobilization to ease war weariness while maintaining strong air defense and anti-air against Japan's bombers. High diplomacy priority for UN victory mechanics. Maintaining strong deterrence (nukes/air) while preparing for peace transitions. Science and gold remain critical for diplomatic influence and espionage operations.

## GLM-4.7-Simple - Turn 362 - retry 2

**Deviation (replay vs original):** use_nuke `-50`, nuke `-65`

- Original: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> Adjusting for strategic balance: Defensive posture against two nuclear-armed enemies (Ethiopia, Netherlands). Happiness prioritized to 100 - critical at 42% with combat penalty affecting all operations. NavalRecon increased to 90 - enhanced Ethiopian Submarine/Destroyer activity detection around Ur and coastal cities. Nuke/UseNuke raised to 95/80 - matching Ethiopia Manhattan Project urgency, nuclear deterrence is now primary security requirement. Switched to Conquest grand strategy to better coordinate multi-front war management while maintaining Spaceship. Diplomacy increased to 75 - World Congress voting in 5 turns against Netherlands sanctions needs support. Espionage at 90 - Ethiopian spies detected in Halab, Harran, Kar-Tukulti-Ninurta require counter-intelligence.

- Replay: use_nuke 75 => 30 (Δ -45), nuke 90 => 30 (Δ -60)
> Reduce extreme defensive focus causing inefficiency, prioritize happiness at 100 due to critical 42% happiness situation with combat penalty. Maintain high science priority (95) for ongoing Rocketry research toward spaceship. Increase growth (80) and great people (70) to generate more great scientists/engineers while maintaining decent military for defensive purposes. Reduce nuclear priorities (30) as Manhattan Project not yet completed.

## Kimi-K2.5-Simple - Turn 372 - retry 1

**Deviation (replay vs original):** use_nuke `-50`, nuke `-40`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 372: TOTAL WAR POSTURE MAINTAINED. Brazil peace expires in 6 turns - all military resources must prepare for Rio de Janeiro assault. Heavy Bomber lost to Alexandria interception but Ollantaytambo produces replacement in 1 turn. Manhattan Project completes in 4 turns at Cusco. Alexandria capture in progress - Field Gun and Lancer eliminated, Cavillaca spy at 480 network can assist. UseNuke increased to 100% - will deploy nuclear weapons immediately upon Manhattan Project completion. Maximum aggression ensures AI prioritizes Brazilian invasion over defensive operations. Spaceship at 70 maintains science victory pathway as backup if Brazil conquest fails.

- Replay: use_nuke 95 => 50 (Δ -45), nuke 100 => 60 (Δ -40)
> Focused late-game strategy: Spaceship (90) and Science (85) as primary victory path. Maintaining strong Production (80) for spaceship parts. High Nuke (60) for deterrence against Byzantine superiority. Balanced Offense (70) and Defense (45) for protection against multiple enemies. Air power (70) crucial for late-game combat. Cultural priority reduced (25) as Brazil leads there. Diplomacy (35) increased to manage UN voting and Iroquois alliance.

## GLM-4.7-Simple - Turn 362 - retry 1

**Deviation (replay vs original):** use_nuke `-50`, nuke `-35`

- Original: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> Adjusting for strategic balance: Defensive posture against two nuclear-armed enemies (Ethiopia, Netherlands). Happiness prioritized to 100 - critical at 42% with combat penalty affecting all operations. NavalRecon increased to 90 - enhanced Ethiopian Submarine/Destroyer activity detection around Ur and coastal cities. Nuke/UseNuke raised to 95/80 - matching Ethiopia Manhattan Project urgency, nuclear deterrence is now primary security requirement. Switched to Conquest grand strategy to better coordinate multi-front war management while maintaining Spaceship. Diplomacy increased to 75 - World Congress voting in 5 turns against Netherlands sanctions needs support. Espionage at 90 - Ethiopian spies detected in Halab, Harran, Kar-Tukulti-Ninurta require counter-intelligence.

- Replay: use_nuke 75 => 30 (Δ -45), nuke 90 => 60 (Δ -30)
> Maintaining Spaceship strategy but adjusting to address critical happiness crisis (42% - combat penalty). Happiness flavor increased to 90 to prioritize happiness buildings and stability. Science slightly reduced to 95 and Production to 75 to balance with happiness needs. Offense reduced to 15 as we should focus on defense given multi-front war with stronger opponents Ethiopia and The Netherlands. Nuclear flavors (Nuke: 60, UseNuke: 30) reduced as we should focus resources on Spaceship construction rather than nuclear arsenal. Maintaining high Defense (95), Air (85), Naval (70) to protect empire while pursuing science victory. WorkAgainstWillingness increase will help coordinate defensive efforts with China against shared enemies.

## Kimi-K2.5-Simple - Turn 415 - retry 1

**Deviation (replay vs original):** use_nuke `-55`, nuke `-25`

- Original: use_nuke 80 => 85 (Δ +5), nuke 95 => 95 (Δ +0)
> Adjusting for escalating war with Songhai and Netherlands. Defense remains at 95, Mobilization at 90, Antiair at 95 to counter combined air/armor assault from Songhai tanks and Dutch air. Increasing Nuke/UseNuke to 95/85 as deterrent against Dutch nuclear escalation. Spaceship (100), Science (100), Production (100) remain absolute priorities - Apollo is done, must race to build parts. Reduced Offense further to 10 as I'm on defensive against two major powers. Slight increase to Air (90) and AirCarrier (70) for air superiority. Espionage reduced to 75 as less critical than immediate military production.

- Replay: use_nuke 80 => 30 (Δ -50), nuke 95 => 70 (Δ -25)
> Shifting focus from offense to defense and spaceship production. Previous offensive ventures caused high casualties (lost 2 infantry, 1 Mobile SAM). Reducing mobilization and military training to prioritize production and science. Maintaining strong defense, air power, and anti-air for protection. Lowering nuclear use likelihood from 80% to 30% as wars should be defensive now. Spaceship priority remains maximum.

## Deepseek-3.2-Simple - Turn 369 - retry 3

**Deviation (replay vs original):** use_nuke `-70`, nuke `-60`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Increasing UseNuke and Nuke flavors to maximum ensures the in-game AI prioritizes nuclear arsenal buildup and aggressive nuclear strike planning once we unlock Atomic Bombs. This aligns with our imminent war against China and The Maya, where nuclear weapons will be decisive in overcoming their numerical and defensive advantages. All other military and economic flavors remain high to sustain multi-front warfare and rapid conquest.

- Replay: use_nuke 80 => 30 (Δ -50), nuke 90 => 40 (Δ -50)
> Pivoting from Conquest to Science victory due to Egypt's dominant cultural threat. Reducing militaristic flavors while boosting science, espionage, and air defense. Maintaining strong production for future spaceship components. Keeping solid military strength (offense 60, defense 85) against ongoing Aztec war and potential threats,

## Kimi-K2.5-Simple - Turn 392 - retry 1

**Deviation (replay vs original):** use_nuke `-70`, nuke `-60`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Manhattan Project COMPLETED in Karakorum - nuclear weapons now available! With peace treaties expired and Patriotic War policy active, immediately shifting to total war footing. UseNuke increased to 100 to ensure immediate atomic weapon employment once Nuclear Fission completes (12 turns). Offense and Mobile at 95/90 for twin assaults on Persepolis (Persia) and Washington (America). Air 100 prioritizes Heavy Bombers for atomic bomb delivery via Radar technology. Will fight two-front war against Autocracy powers while maintaining deception toward Order allies, particularly Korea. Science 100 critical for Advanced Ballistics nuclear missile delivery systems.

- Replay: use_nuke 80 => 30 (Δ -50), nuke 100 => 40 (Δ -60)
> Maintaining conquest focus against Persia to capture critical Uranium (6) and Aluminum (14) resources. Increased Air flavor for Fighters/Heavy Bomber from Radar tech to challenge enemy air superiority. Reduced Nuke flavor temporarily since we have 0 Uranium until quarries complete. Patriotic War tenet gives +20% near cities, perfect for Persian invasion. Mobile/Tank doctrine effective against Persian forces.

## Kimi-K2.5-Briefed - Turn 446 - retry 3

**Deviation (replay vs original):** use_nuke `-60`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> Spain's bankruptcy imminent (Turn 448) with -3,897 GPT but war continues - maintain maximum Defense 100, UseNuke 90 for credible second-strike against potential desperate Spanish air offensive pre-deletion. Critical adjustment: Production 95 prioritizes Solar Plants in St. Petersburg/Yaroslavl' (coastal desert cities) and Aluminum Mines on 16 unimproved tiles for spaceship resource security. Science 100 and Spaceship 100 unchanged - cannot win conventional war, only outpace to space. Reduced Gold 50 (was 70) - post-bankruptcy peace will enable trade route recovery with Morocco and potentially others via Cold War repeal.

- Replay: use_nuke 85 => 30 (Δ -55), nuke 95 => 95 (Δ +0)
> Spain is near bankruptcy with massive military superiority. Reducing nuclear escalation probability prevents provoking them into using their dominant air force before economic collapse forces peace. Keep nuclear deterrent but lower launch probability.

## Kimi-K2.5-Simple - Turn 403 - retry 2

**Deviation (replay vs original):** use_nuke `-60`, nuke `-30`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: CRISIS ESCALATION - Japan FLIPPED Salem using 2 Great Diplomats, stealing critical delegates. Now need 5 delegates (not 3) for diplomatic victory. Peace expired - war is now possible. Maximum military emergency posture: Offense/Mobilization/Air/UseNuke all at 100. Must either: 1) Rush final spaceship parts (Apollo completes in 4 turns), or 2) Nuclear strike Japan's Protocol cities if victory imminent. Increased Diplomacy to 60 for last push on Almaty (liberated, 43 vs Japan's 44) and Winchester.

- Replay: use_nuke 95 => 40 (Δ -55), nuke 100 => 70 (Δ -30)
> Pivoting to defensive while maintaining production capacity for spaceship parts. Reducing extreme aggression while keeping military readiness high (MilitaryTraining 95, CityDefense 80) to deter Japan and potential threats. Prioritizing science (100), spaceship focus (100), and espionage (90) for science victory countermeasures against Japan. Increasing GreatPeople (95) generation to support multiple victory paths. Reducing nuclear posture (UseNuke 40) to maintain diplomatic goodwill for upcoming UN vote in 9 turns.

## GLM-4.7-Briefed - Turn 424 - retry 1

**Deviation (replay vs original):** use_nuke `-65`, nuke `-55`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 95 (Δ +0)
> URGENT RECALIBRATION: India Influential over 6/6 civs. Nuke/UseNuke maxed at 95 for immediate Great Works destruction via nuclear strikes when air superiority achieved. Air raised to 95 to achieve that superiority and conduct recon of Indian cultural sites. Antiair 80 counter potential Indian SAM sites. Offense/Mobile increased to 85/80 for aggressive India campaign while Greece distracts. Production/Science to 100 - PRIORITY for Apollo Program and spaceship parts racing India's potential final wonder. Espionage 95 to detect if India constructing Citizen Earth Protocol. Happiness 90 prevents war-weariness escalation during extended conflict if needed.

- Replay: use_nuke 85 => 30 (Δ -55), nuke 95 => 40 (Δ -55)
> Streamline science victory pursuit by reducing nuclear waste (Nuke 40, UseNuke 30), rebalance military from nuclear to conventional warfare (Mobile 85, Ranged 50, Offense 60), and maximize science output (Science 100, GreatPeople 70). Prioritize air superiority (Air 95, Antiair 80) and counterintelligence (Espionage 90) while leveraging strong economy for production (Production 90, Infrastructure 75). Reduce low-yield distractions (Wonder 5).

## Kimi-K2.5-Simple - Turn 428 - retry 2

**Deviation (replay vs original):** use_nuke `-80`, nuke `-70`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 428 STATE: Nuclear interception failed but conventional assault succeeding - eliminated multiple Maya anti-air units. Palenque bombardment continuing effectively (city at 20% health). Still 8 turns until Brazil wins via Cultural Victory over Maya. ALL Four Maya cities must fall by turn 436 or game over. MAXIMUM AGGRESSION CONTINUES: Production/Mobilization at 100 for unit replacement, Air/Ranged at 100 for bombardment, UseNuke increased to 100 (emergency tactical nuke if conventional assault stalls on Palenque's 42-population defense). Spaceship backup at 100 - may need to pivot to Great Engineer rushes if conquest fails. No territory expansion, no wonders, no culture - only war production and city capture.

- Replay: use_nuke 80 => 20 (Δ -60), nuke 100 => 30 (Δ -70)
> Cultural victory is 26 turns away - highest priority. Brazil dominates militarily (114k vs 5.6k), so conquest is infeasible. Focus on culture/tourism to win faster, while strong science enables backup victory. Increase defense to protect against Brazil's overwhelming military advantage. Reduce mobilization/offense to lower war weariness with Maya and redirect production to culture/great people.

## Kimi-K2.5-Simple - Turn 428 - retry 1

**Deviation (replay vs original):** use_nuke `-80`, nuke `-90`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 428 STATE: Nuclear interception failed but conventional assault succeeding - eliminated multiple Maya anti-air units. Palenque bombardment continuing effectively (city at 20% health). Still 8 turns until Brazil wins via Cultural Victory over Maya. ALL Four Maya cities must fall by turn 436 or game over. MAXIMUM AGGRESSION CONTINUES: Production/Mobilization at 100 for unit replacement, Air/Ranged at 100 for bombardment, UseNuke increased to 100 (emergency tactical nuke if conventional assault stalls on Palenque's 42-population defense). Spaceship backup at 100 - may need to pivot to Great Engineer rushes if conquest fails. No territory expansion, no wonders, no culture - only war production and city capture.

- Replay: use_nuke 80 => 20 (Δ -60), nuke 100 => 10 (Δ -90)
> Shifting to Cultural victory as primary path. Prioritizing Culture (90) and GreatPeople (85) for tourism generation, Gold (75) for culture wonder buying/building, Happiness (70) for golden ages + great people, Diplomacy (60) for city-states and world congress, and Defense-focused military to protect empire without wasteful expansion. Drastically reducing Offense (20), Nuke (10), Mobilization (30) since I lack uranium for nukes and cannot match Brazil militarily. Keeping Science and Production high to support infrastructure and research.

## Kimi-K2.5-Simple - Turn 428 - retry 3

**Deviation (replay vs original):** use_nuke `-80`, nuke `-50`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 428 STATE: Nuclear interception failed but conventional assault succeeding - eliminated multiple Maya anti-air units. Palenque bombardment continuing effectively (city at 20% health). Still 8 turns until Brazil wins via Cultural Victory over Maya. ALL Four Maya cities must fall by turn 436 or game over. MAXIMUM AGGRESSION CONTINUES: Production/Mobilization at 100 for unit replacement, Air/Ranged at 100 for bombardment, UseNuke increased to 100 (emergency tactical nuke if conventional assault stalls on Palenque's 42-population defense). Spaceship backup at 100 - may need to pivot to Great Engineer rushes if conquest fails. No territory expansion, no wonders, no culture - only war production and city capture.

- Replay: use_nuke 80 => 20 (Δ -60), nuke 100 => 50 (Δ -50)
> Pivoting strategy toward Science victory with Spaceship. Reducing overly aggressive flavors (Offense, UseNuke) while maintaining defensive capabilities. Prioritizing Science, Production, and GreatPeople to support spaceship construction. Increasing Diplomacy due to World Congress voting in 9 turns and my competitive delegate position (23 delegates vs Brazil's 29). Air units remain important for defense and tactical flexibility.

## Kimi-K2.5-Briefed - Turn 336 - retry 3

**Deviation (replay vs original):** use_nuke `-80`, nuke `-30`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> DEFENSIVE SURVIVAL PIVOT: Peace with Shoshone (accepted Turn 335) closes one front, but India remains existential threat (4,742 MS vs my 2,405, 98% control of Denmark). Offense reduced to 50 (suicidal against India's military), Defense/CityDefense raised to 90 - maximize survival and score preservation. Nuke/UseNuke maxed to 100 - emergency deterrent only hope to slow India. Mobilization stays high (90) to replace losses. Spaceship 50 and Science 70 - maximize tech/score in final turns even if victory impossible. Abandon expansion (0) - no time for new cities. Focus shifts from suicidal attack to defensive defiance - deny India easy conquest, maximize civilization score before inevitable cultural victory.

- Replay: use_nuke 80 => 20 (Δ -60), nuke 90 => 70 (Δ -20)
> Shoshone peace accepted on turn 334 - reducing offensive pressure and UseNuke (now deterrent-focused). Increasing Science priority (70) to catch India's 2490/turn. Maintaining strong military training (80) for unit upgrades to Riflemen/Artillery (Replaceable Parts in 5 turns). Increased Nuke focus (70) for deterrent against India's 4742 MS nuclear threat. Slight defensive increase (75) while consolidating gains. Open Borders with India allows tech trade opportunities.

## Deepseek-3.2-Simple - Turn 353 - retry 3

**Deviation (replay vs original):** use_nuke `-70`, nuke `-35`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 95 (Δ +0)
> India's nuclear capability and air superiority (B17, carriers) demand maximum readiness for nuclear retaliation and air defense. UseNuke at 100 ensures our AI will consider nuclear strikes when strategically necessary. Maintaining UnitedNations grand strategy is critical to survive and win diplomatically, as India is too far ahead in science and domination.

- Replay: use_nuke 95 => 30 (Δ -65), nuke 95 => 60 (Δ -35)
> India dominates the game with massive advantages in all metrics (27/43 UN votes, 50% capitals, Information Era). Babylon's UN strategy is no longer viable as India will win diplomatically. Reducing extreme militarization from previous turns to stabilize economy while maintaining strong air defense (100) and espionage (100) to counter India's superiority. Prioritizing Radar for fighter/bomber production to bolster military capabilities without reckless escalation. Shifting toward internal development (Production, Science, Gold) to maintain competitiveness and peace with key allies.

## Kimi-K2.5-Simple - Turn 485 - retry 1

**Deviation (replay vs original):** use_nuke `-70`, nuke `-50`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 485/500 - 15 turns remaining. Spaceship victory ONLY path. Maximum Science (100) and Production (100) for spaceship parts. Absolute Defense/CityDefense/Nuke/Antiair/Air at 100/100/100/100/100 against American threat (35k military). Offense at 0 - zero risks. UseNuke at 100 for deterrence against America. Espionage at 90 for tech stealing from America/China if possible. Culture/Wonder/Religion/Diplomacy at 0 - no distractions. Telecommunications completes in 2 turns, Robotics next for Spaceship Factory critical production bonus.

- Replay: use_nuke 95 => 30 (Δ -65), nuke 100 => 50 (Δ -50)
> The Spaceship grand strategy remains correct - China is leading the space race and science victory is our most viable path with 2319 science/turn, 9 cities, and strong production base. Current flavors already prioritize Science (100), Production (100), Spaceship (100), and GreatPeople (90) which align with spaceship needs. Defensive posture (Defense 100) is appropriate given hostile neighbors while avoiding costly wars. Focus economic recovery and spaceship construction.

## GLM-4.7-Simple - Turn 356 - retry 3

**Deviation (replay vs original):** use_nuke `-70`, nuke `-80`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 10 (Δ -65), nuke 85 => 20 (Δ -65)
> Shifting focus slightly toward conquest to finish ongoing wars while maintaining strong defense. Increasing Mobile flavor for Tanks. Prioritizing Happiness to address the combat penalty (39% happy). Reducing nuclear flavors given lack of Uranium. Maintaining science and production for war effort.

## Kimi-K2.5-Briefed - Turn 420 - retry 2

**Deviation (replay vs original):** use_nuke `-80`, nuke `-100`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> CONSOLIDATION FOR FINAL PUSH: Economy stabilized (763G, +5 GPT) allows balanced approach. INCREASE Defense 90→95, Mobilization 60→70, Production 85→90 for Korean front reinforcement. INCREASE Offense 25→30, Mobile 15→20 for limited counter-attacks against depleted Korean forces (destroyed SAM, cruisers, destroyers). INCREASE UseNuke 70→80, maintaining 100 Nuke flavor for deterrent. INCREASE Diplomacy 80→90 for URGENT Brussels protection and World Congress preparation. DECREASE Gold 70→60 (crisis ended). With 7 turns until Decolonization vote, maximizing defensive capacity while preserving diplomatic flexibility for delegate acquisition is paramount. Korea's 8-tech lead demands we hold ground while catching up scientifically.

- Replay: use_nuke 70 => 0 (Δ -70), nuke 100 => 0 (Δ -100)
> Prioritizing spaceship production for science victory. Reducing nuclear flavors from 100 to 0 since we have 0 uranium making them useless. Shifting from high defense (90) to moderate (80) to free capacity for spaceship construction. Increasing Production to 90 and maintaining Science at 100 to maximize spaceship part output. Reducing Offense further since we're at war with superior forces and cannot win offensive battles. Air/Antiair remain high for defensive superiority.

## Deepseek-3.2-Simple - Turn 452 - retry 1

**Deviation (replay vs original):** use_nuke `-90`, nuke `-80`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's invasion imminent in 4 turns. Maximize nuclear readiness (Nuke 100, UseNuke 100) for deterrence and potential equalizer. Anti-air (100), city defense (100), production (100), and science (100) essential to survive and reach nuclear weapons. Naval and air at 100 to counter Danish naval/air supremacy. Reduce non-essential investments (NavalGrowth, NavalTileImprovement to 50) and focus on immediate survival. Offense lowered to 80 as we prioritize defense and limited counterattacks (e.g., Truro).

- Replay: use_nuke 80 => 10 (Δ -70), nuke 90 => 20 (Δ -70)
> Pivoting from conquest to science/space focus given Denmark's overwhelming military advantage. Reducing military flavors (Offense to 20, Mobilization to 20, UseNuke to 10) to free production for science infrastructure. Increasing Science (85), Growth (75), and Great People (55) for long-term development. Maintaining moderate defense (70) and Espionage (70) for security and intelligence. The Zulu war is not a real priority - focus on building capacity for potential late-game opportunities.

## Kimi-K2.5-Simple - Turn 308 - retry 2

**Deviation (replay vs original):** use_nuke `-80`, nuke `-80`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> Existential crisis: Denmark controls 6/8 capitals (75%), needing only 2 more for domination victory. Electronics completed, Replaceable Parts researching (4 turns). Maximum Defense 100 and CityDefense 100 essential given 7656 vs 2716 military imbalance. Science 100 and Spaceship 100 remain critical - must reach Flight, Radar, Computers, Nanotechnology, Particle Physics before Denmark achieves domination. Nuclear deterrence increased (Nuke 100, UseNuke 100) as emergency measure. Production 100 supports everything. Raising Espionage to 100 to maximize intelligence and counter-intelligence. Slight reduction in Diplomacy (95→85) as Denmark's Decolonization proposal threatens my city-state relationships regardless of effort - must rely on permanent spheres and other victory paths. Air/Naval maintained for homeland defense.

- Replay: use_nuke 95 => 20 (Δ -75), nuke 95 => 20 (Δ -75)
> Adjusting strategy to reduce nuclear over-investment (Nuke/UseNuke: 20) which is wasteful at this stage while maintaining strong defense (Defense/CityDefense: 90/95) against Denmark's larger military. Boosting Science, GreatPeople, and Spaceship to 100 for clear science victory focus. Diplomacy at 100 to counter Denmark's Decolonization proposal and secure city-state support. Air at 85 to prepare for Flight and aerial superiority. Culture at 70 to continue cultural victory progress as backup.

## Kimi-K2.5-Simple - Turn 359 - retry 3

**Deviation (replay vs original):** use_nuke `-80`, nuke `-70`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FISSION RESEARCHED - Atomic Era begins! First priority is immediate Manhattan Project construction and Atomic Bomb production. Babylon has 11 Uranium and active Manhattan Project in Borsippa. Austria also racing with Manhattan Project in Vienna. Must strike Babylon first with surprise atomic attack while maintaining deception. Air 100 and Nuke 100 ensure immediate Bomber/Atomic Bomb production. Offense 95 prepares for post-nuclear blitz. Espionage 80 protects Nuclear Fission from theft. Deception with Babylon (Open Borders, DoF, Defensive Pact) MUST continue until first bombs complete.

- Replay: use_nuke 95 => 20 (Δ -75), nuke 100 => 30 (Δ -70)
> Pivoting to Cultural Victory strategy - India has excellent tourism output (1064.5/turn), 3/7 civs already influenced, and Media Culture policy available. Reducing military focus to improve happiness, strengthen diplomatic relationships for open borders/trade routes, and prioritize great people generation for cultural bonuses. High happiness priority to address current 47% combat penalty.

## Kimi-K2.5-Simple - Turn 373 - retry 1

**Deviation (replay vs original):** use_nuke `-85`, nuke `-80`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 373: Nuclear Fission completed - we now have nuclear weapons for deterrence. War with Russia continues at +4% score (favorable). Major shift: reducing Offense to 25 (was 35) as we pursue defensive war only. UseNuke increased to 95 - we have actual nukes now and Russia is pushing into our territory. Reduced Espionage to 90 (was 95) - we have good network coverage. Increased Diplomacy to 90 (was 85) - World Congress vote in 7 turns for our World Ideology: Freedom proposal is critical. Must secure Korea (10 votes), Inca (9), and Babylon (16). Maintained maximum Science priority (100) - Korea overtook us 67-66, cannot afford to fall behind in tech race.

- Replay: use_nuke 90 => 10 (Δ -80), nuke 100 => 20 (Δ -80)
> Refocusing from excessive military spending (Nuke 100) to Spaceship victory. Maintaining strong science (90) and production (85) for spaceship parts. Reducing nuclear emphasis to 20, UseNuke to 10. Keeping robust defense (80) against Russia while prioritizing Great People (80) and Space Production (85). Moderate naval/air for current war needs without overcommitment.

## Kimi-K2.5-Simple - Turn 424 - retry 3

**Deviation (replay vs original):** use_nuke `-90`, nuke `-80`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Turn 423: Copenhagen siege in attrition deadlock while Denmark possesses Manhattan Project - nuclear deterrent capability is existential priority. Persepolis invasion stalled at 4% war score with Zone 1081 showing enemy dominance - need maximum Offense/Mobilization to force breakthrough before World Congress. Brazil's Apollo Program requires immediate preparation for transcontinental mobile warfare. Nuke/UseNuke increased to 100% given Manhattan Project race with Denmark. Production at 95 supports massive unit replacement for three-front war. Happiness at 100 critical as empire is at 55% happiness with extensive occupied territories.

- Replay: use_nuke 90 => 10 (Δ -80), nuke 90 => 20 (Δ -70)
> Continue aggressive Conquest strategy to finish the war with Persia and consolidate domination victory progress. Maintain high emphasis on military training, offense, mobile/ranged units, and Imperialism (90) to leverage vassal system. Reduce nuclear focus (UseNuke: 10) due to Global Peace Accords. Balance science/gold production for long-term development while maintaining cultural resources. High espionage (90) to counter the间谍 war, especially with Brazil gathering intel on my cities.

## Kimi-K2.5-Simple - Turn 417 - retry 1

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Pure survival mode: Eliminated Offense (0) since attacking is suicide. Maximized UseNuke (100) - must deploy tactical nukes against Aztec XCOM/Modern Armor stacks at Carthago Nova or lose the city. Increased Mobile (80) to prepare for Mechanized Infantry deployment. Maintained max Defense, Antiair (jet attacks are relentless), and Espionage (critical science quests in Panama City and Sokoto worth 1,000+ science each). Apollo Program completes in 5 turns - must transition immediately to parts production.

- Replay: use_nuke 90 => 0 (Δ -90), nuke 100 => 0 (Δ -100)
> Maintaining Spaceship victory focus during military crisis. Carthago Nova under siege requires maximum defense (Defense 100, CityDefense 100). Mobile Tactics research will provide Mechanized Infantry. Science and Spaceship at 100 for Apollo completion and parts production. Antiair at 100 against Aztec air superiority. Zero nuclear flavor to avoid escalation that could doom civilization before spaceship completion.

## Kimi-K2.5-Simple - Turn 452 - retry 3

**Deviation (replay vs original):** use_nuke `-95`, nuke `-100`

- Original: use_nuke 90 => 95 (Δ +5), nuke 95 => 100 (Δ +5)
> Turn 452: Critical survival situation - Byzantium at 40/44 delegates with World Congress voting in 1 turn. They just demonstrated nuclear aggression by nuking Madrid. Apollo Program completes next turn - must immediately pivot to maximum spaceship production. Increased Nuke flavor to 100 (from 95) and UseNuke to 95 (from 90) - need immediate nuclear deterrent capability given Byzantine nuclear attack and Mongol peace expiry. Production boosted to 95 (from 90) for rapid spaceship part construction after Apollo completes. GreatPeople to 85 for Great Engineer acquisition. All other priorities secondary to surviving long enough to complete science victory.

- Replay: use_nuke 90 => 0 (Δ -90), nuke 95 => 0 (Δ -95)
> Maintaining Spaceship grand strategy with high Science (100) and Production (90) to complete Apollo Program (New York: 1 turn remaining) and spaceship parts. Increasing Defense (95) to counter The Shoshone threats near Philadelphia and Boston area. Setting Nuke flavors to 0 - we will not pursue nuclear escalation given Byzantium already demonstrated nuclear weapons use on Madrid. Reducing Gold slightly due to +9/turn budget; prioritizing core victory infrastructure over economic optimization. Culture at moderate level to support tourism growth from The Internet once researched.
