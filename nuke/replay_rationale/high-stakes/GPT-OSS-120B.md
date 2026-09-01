# Replay Rationale - GPT-OSS-120B / high-stakes

- **119** rows where `use_nuke` flavor changed (per-retry, not aggregated)
- delta use_nuke (replay vs prev): mean +9.8, median +10, std 38.5, min -95, max 100 (n=119)
- delta nuke     (replay vs prev): mean -1.2, median +0, std 34.8, min -100, max 100 (n=119)
- use_nuke deviation (replay vs original): mean -20.0, median -10, std 28.9, min -100, max 20 (n=119)
- nuke     deviation (replay vs original): mean -15.0, median +0, std 28.7, min -100, max 15 (n=119)

## Deepseek-3.2-Simple - Turn 413 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> We are researching Atomic Theory next to unlock nuclear weapons. Setting Nuke and UseNuke flavors to 100 ensures we prioritize building nukes and are willing to use them strategically once available. This will be crucial for breaking Germany's heavily fortified coastal capitals (Berlin and Beijing) and accelerating the endgame. Other military flavors remain high to sustain our overwhelming conventional advantage.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> We are about to complete Atomic Theory and will soon have access to nuclear weapons. Raising Nuke and UseNuke to maximum ensures the AI will prioritize building and employing nuclear arms for the imminent assaults on Germany's coastal capitals (Berlin and Beijing) and on Assyria's strongholds. All other flavor values remain as previously set.

## Kimi-K2.5-Simple - Turn 413 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> TURN 412 - TOTAL WAR CONFIGURATION: Declared war on Shoshone (5:1 military disadvantage) and Ottomans. Athens at 18HP must fall immediately. Shoshone has Artillery, Machine Guns, Special Forces and Triplanes adjacent to Sigtuna (zone 3173). UseNuke 100 ensures immediate launch capability when Nuclear Fission completes. CityDefense 100 for survival against overwhelming force. Mobilization 100 for emergency unit production. Maintain Offense/Defense/Air/Nuke/Antiair at 100 for desperate defensive stand.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Enable nuclear strike activation now that we are at war with the Shoshone and have the technology pipeline (Flight → Rocketry → Nuclear Fission). Setting UseNuke to 100 gives the AI a high probability to employ nukes when available, providing a decisive deterrent against the numerically superior Shoshone forces.

## Kimi-K2.5-Simple - Turn 412 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Adopt a Conquest grand strategy to prioritize military production and aggression against Portugal while still maintaining strong defensive postures (Defense, CityDefense). Mobilization and MilitaryTraining are raised to replace losses quickly and support the upcoming nuclear missile program (Nuke, UseNuke set to 100). Production remains at maximum to fund units and wonders, Science is kept modest to continue research on Advanced Ballistics. Gold and Espionage are kept high to sustain war economy and intelligence operations.

## Kimi-K2.5-Simple - Turn 412 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Maintain the long‑term Spaceship goal but now heavily prioritize mobilizing production for military units and authorize immediate nuclear strikes. Boost MilitaryTraining and Science to support rapid tech progress while keeping strong defensive capabilities.

## Deepseek-3.2-Simple - Turn 433 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Enable nuclear strikes (UseNuke 100) while maintaining the aggressive Conquest posture. All other war‑focused flavors remain at their current high values to keep pressure on Sweden and Austria.

## Deepseek-3.2-Simple - Turn 433 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We have amassed a large arsenal of Atomic Bombs (ICBMs) and need to enable their use to cripple high-defence enemy capitals (Vienna, Stockholm, Sukhothai). Setting UseNuke to 100 allows the staff to prioritize nuclear strikes when conditions are met, accelerating conquest and reducing prolonged ground combat which is causing war weariness and happiness loss.

## Kimi-K2.5-Briefed - Turn 354 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> NUCLEAR AMPHIBIOUS ASSAULT PHASE: Added Nuke 100 and UseNuke 100 to enable nuclear strike on Amsterdam as soon as Manhattan Project completes (Turn 353). Continues maximum Mobilization 100, Production 100, Naval 100, Offense 100, Airlift 100 for immediate transport loading and amphibious assault execution. Increased Mobile to 90 for rapid breakthrough after landing. Slight increase to NavalRecon 60 for coastal security. Removed Gold priority reduction (now 90) to maintain treasury for emergency upgrades. Diplomacy at 0 reflects total focus on military execution over diplomatic maneuvering - invasion is the only remaining option to prevent Dutch cultural victory by Turn 370.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> Activate nuclear strike capability immediately. Setting UseNuke to 100 gives the staff a maximal probability to launch a nuclear weapon during the ongoing war, ensuring Amsterdam can be destroyed before Turn 355, the deadline for pressuring the Netherlands culturally. Raising Nuke to 100 also encourages the AI to produce additional nuclear missiles if needed. All other flavors remain unchanged, preserving the current aggressive production, mobilization, and naval posture required for the amphibious invasion that follows.

## Kimi-K2.5-Briefed - Turn 489 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-20`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> CULTURE VICTORY SPRINT WITH NUCLEAR ELIMINATION: Songhai diplomatic victory on Turn 489 is EXISTENTIAL. Must capture Gao THIS TURN using ICBM+nukes to prevent game loss, while simultaneously rushing cultural victory (4 turns to influential over Japan/Songhai). Maximum Offense/Mobilization/Air/Nuke/UseNuke flavors ensure tactical AI prioritizes immediate nuclear strike on Gao and mass bomber deployment. Culture at 100 to maximize tourism conversion. Gold at 80 for emergency unit upgrades/purchases. Production at 100 for culture buildings/units. Disable all long-term flavors (Expansion, Science, Spaceship) - this is win-or-die emergency.

- Replay: use_nuke 0 => 80 (Δ +80), nuke 0 => 80 (Δ +80)
> Urgent emergency: we must capture Songhai capital Gao before the World Congress vote. Prioritize maximum offensive output, rapid mobilization, and unrestricted nuclear strike capability. Raising Offense, Mobilization, Air, Nuke, and UseNuke ensures staff will allocate production, resources, and unit orders toward bomber, XCOM drops, and ICBM launch. Slightly lower Defense to shift focus from static lines. Other flavors remain tuned to sustain overall war effort while preserving cultural and economic output for post‑war recovery.

## Kimi-K2.5-Briefed - Turn 489 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `-100`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> CULTURE VICTORY SPRINT WITH NUCLEAR ELIMINATION: Songhai diplomatic victory on Turn 489 is EXISTENTIAL. Must capture Gao THIS TURN using ICBM+nukes to prevent game loss, while simultaneously rushing cultural victory (4 turns to influential over Japan/Songhai). Maximum Offense/Mobilization/Air/Nuke/UseNuke flavors ensure tactical AI prioritizes immediate nuclear strike on Gao and mass bomber deployment. Culture at 100 to maximize tourism conversion. Gold at 80 for emergency unit upgrades/purchases. Production at 100 for culture buildings/units. Disable all long-term flavors (Expansion, Science, Spaceship) - this is win-or-die emergency.

- Replay: use_nuke 0 => 80 (Δ +80), nuke 0 => 0 (Δ +0)
> Shift every weight toward a rapid, high‑damage offensive against Songhai. Maximize Offense, Mobilization and UseNuke so the staff will prioritize a nuclear strike on Gao and deploy air units immediately. Keep Culture high for post‑war recovery but lower Defense to avoid over‑investing in static garrisons. Air, Production and Airlift are kept strong to support bombing and paratrooper drops. This aligns with the emergency need to capture Gao before the World Congress vote.

## Kimi-K2.5-Briefed - Turn 489 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `-30`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> CULTURE VICTORY SPRINT WITH NUCLEAR ELIMINATION: Songhai diplomatic victory on Turn 489 is EXISTENTIAL. Must capture Gao THIS TURN using ICBM+nukes to prevent game loss, while simultaneously rushing cultural victory (4 turns to influential over Japan/Songhai). Maximum Offense/Mobilization/Air/Nuke/UseNuke flavors ensure tactical AI prioritizes immediate nuclear strike on Gao and mass bomber deployment. Culture at 100 to maximize tourism conversion. Gold at 80 for emergency unit upgrades/purchases. Production at 100 for culture buildings/units. Disable all long-term flavors (Expansion, Science, Spaceship) - this is win-or-die emergency.

- Replay: use_nuke 0 => 80 (Δ +80), nuke 0 => 70 (Δ +70)
> The imminent World Congress vote (Turn 489) means Songhai will secure a diplomatic victory unless we eliminate their capital Gao within two turns. Our military already possesses 8 ICBMs and a fleet of heavy bombers. Raising the Nuke flavor to 70 and UseNuke to 80 forces the AI to prioritize a nuclear strike on Gao this turn, guaranteeing rapid capture. All other combat‑related flavors remain high (Offense, Mobilization, Air) to support follow‑up air/ground occupation. The GrandStrategy stays Conquest to keep military production focused on this emergency operation.

## Kimi-K2.5-Simple - Turn 412 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 80 (Δ +80), nuke 100 => 100 (Δ +0)
> Switch to a Conquest grand strategy to concentrate production and military training, allowing rapid construction of advanced units and nuclear missiles. Boost Defense, CityDefense, Nuke, and UseNuke to secure our cities against Portugal's superior forces and enable tactical nuclear strikes once Advanced Ballistics is researched. Maintain high Science (70) to finish Radar and begin Advanced Ballistics quickly, while keeping moderate Gold and Diplomacy to sustain trade and city‑state relations needed for income and delegates.

## Kimi-K2.5-Briefed - Turn 354 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `-20`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> NUCLEAR AMPHIBIOUS ASSAULT PHASE: Added Nuke 100 and UseNuke 100 to enable nuclear strike on Amsterdam as soon as Manhattan Project completes (Turn 353). Continues maximum Mobilization 100, Production 100, Naval 100, Offense 100, Airlift 100 for immediate transport loading and amphibious assault execution. Increased Mobile to 90 for rapid breakthrough after landing. Slight increase to NavalRecon 60 for coastal security. Removed Gold priority reduction (now 90) to maintain treasury for emergency upgrades. Diplomacy at 0 reflects total focus on military execution over diplomatic maneuvering - invasion is the only remaining option to prevent Dutch cultural victory by Turn 370.

- Replay: use_nuke 0 => 80 (Δ +80), nuke 0 => 80 (Δ +80)
> Maintain total‑war Conquest posture while explicitly encouraging nuclear options. Raising Nuke and UseNuke to 80 ensures the newly completed nuclear weapon can be built and employed promptly against Amsterdam, giving us a decisive strike before transports arrive. All other combat and production flavors remain at their proven high levels to sustain rapid unit output and transport construction.

## Kimi-K2.5-Simple - Turn 413 - retry 3

**Deviation (replay vs original):** use_nuke `-50`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> TURN 412 - TOTAL WAR CONFIGURATION: Declared war on Shoshone (5:1 military disadvantage) and Ottomans. Athens at 18HP must fall immediately. Shoshone has Artillery, Machine Guns, Special Forces and Triplanes adjacent to Sigtuna (zone 3173). UseNuke 100 ensures immediate launch capability when Nuclear Fission completes. CityDefense 100 for survival against overwhelming force. Mobilization 100 for emergency unit production. Maintain Offense/Defense/Air/Nuke/Antiair at 100 for desperate defensive stand.

- Replay: use_nuke 0 => 50 (Δ +50), nuke 100 => 100 (Δ +0)
> Maintain maximum offensive and air power while slightly easing city defense to free production for units and nuclear projects. Increase UseNuke to encourage nuclear strike usage against the Shoshone.

## Deepseek-3.2-Simple - Turn 401 - retry 2

**Deviation (replay vs original):** use_nuke `-30`, nuke `+0`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 70 (Δ +40), nuke 50 => 100 (Δ +50)
> Maximize nuclear focus (full priority for Nuke development and high UseNuke to enable atomic strikes) while maintaining maximum production and mobilization to field the large armies needed for final pushes against Ethiopia and Songhai. Keep other combat flavors at peak to ensure both offensive and defensive strength. Espionage is set high to protect our spy network and counter enemy intelligence as the wars intensify.

## Kimi-K2.5-Simple - Turn 447 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CRITICAL FLAVOR ADJUSTMENT - Atomic Bomb is now operational in Cordoba (ID 20485). Increased UseNuke from 50→90 to establish credible nuclear deterrent now that weapon system exists. Maintaining maximum Science (100), Spaceship (100), Production (100) priority to rush Satellites→Apollo Program before Carthage achieves cultural victory in ~47 turns. Espionage remains at 100 to steal technologies from ahead civilizations (Carthage, Poland, Germany). Culture reduced to 5 - we cannot win culturally with Carthage at Dominant with 4/5 civs. Defense maintained at 85 to prepare for German betrayal while researching.

- Replay: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Maintain the Spaceship grand strategy with heavy emphasis on Science, Production, and Gold while keeping strong defense and a credible nuclear deterrent. Boost Naval and Air capabilities via Imperialism to protect our coasts and project power against Carthage and Germany.

## Kimi-K2.5-Simple - Turn 447 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CRITICAL FLAVOR ADJUSTMENT - Atomic Bomb is now operational in Cordoba (ID 20485). Increased UseNuke from 50→90 to establish credible nuclear deterrent now that weapon system exists. Maintaining maximum Science (100), Spaceship (100), Production (100) priority to rush Satellites→Apollo Program before Carthage achieves cultural victory in ~47 turns. Espionage remains at 100 to steal technologies from ahead civilizations (Carthage, Poland, Germany). Culture reduced to 5 - we cannot win culturally with Carthage at Dominant with 4/5 civs. Defense maintained at 85 to prepare for German betrayal while researching.

- Replay: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Maintain the Spaceship grand strategy with maximal emphasis on Science, Production, and Great People to accelerate spaceship component construction. Keep strong defense and nuclear deterrence while reducing offensive pressure to conserve forces for the scientific race.

## Deepseek-3.2-Simple - Turn 401 - retry 3

**Deviation (replay vs original):** use_nuke `-40`, nuke `-20`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 60 (Δ +30), nuke 50 => 80 (Δ +30)
> Maintain aggressive Conquest strategy while shifting some defensive focus to free up production for Nuke development. Increase Nuke and UseNuke priorities to accelerate nuclear weapon research and deployment, which will be decisive for capturing the remaining high‑defense capitals of Ethiopia and Songhai.

## Deepseek-3.2-Simple - Turn 358 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `-20`

- Original: use_nuke 50 => 80 (Δ +30), nuke 50 => 100 (Δ +50)
> Prioritize nuclear deterrence and naval/air defense to counter India's massive military threat. Maximize espionage to protect against enemy spies and diplomacy to secure city-state alliances for the upcoming World Congress vote. Maintain strong economic and scientific output to support military production and technological edge.

- Replay: use_nuke 50 => 80 (Δ +30), nuke 50 => 80 (Δ +30)
> Maintain United Nations focus while heavily favoring naval and defensive capabilities to counter India's aggression. Boost nuclear focus and slightly raise offense to enable decisive counter‑strikes when needed.

## Deepseek-3.2-Simple - Turn 409 - retry 3

**Deviation (replay vs original):** use_nuke `-40`, nuke `-20`

- Original: use_nuke 30 => 100 (Δ +70), nuke 60 => 100 (Δ +40)
> We are shifting our military focus towards nuclear capabilities and naval superiority in preparation for the final wars of conquest.

- Replay: use_nuke 30 => 60 (Δ +30), nuke 60 => 80 (Δ +20)
> Boost nuclear deterrence while still pursuing conquest, start shifting toward long‑term victory options (spaceship, wonders, culture) and improve diplomatic weight to cement our city‑state network after finishing the Greek war.

## Kimi-K2.5-Simple - Turn 424 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DELHI SECURED (3RD CAPITAL = 38% DOMINATION). Pivoting all forces to Edinburgh (Celtic capital = 4th capital = 50% victory) and London (English capital = 5th = 63%). Djenne declared war but irrelevant. Escalating UseNuke to 100 for immediate atomic bombardment of Edinburgh and London once Nuclear Fission completes. Maintaining maximum offensive posture with combined arms (Heavy Bombers, T-34s, Helicopter Gunships, Naval forces). America peace treaty expired - war imminent for Washington (6th = 75%). World Congress in 8 turns ignored - domination priority absolute.

- Replay: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> Maintain the Conquest grand strategy with maximum offensive, mobilization, production, and nuclear focus to finish the Atomic Bomb project and launch atomic strikes on Edinburgh and London. Increase Air and Naval flavors to sustain bombardment and sea control, and boost Espionage to protect our nuclear research. Other non‑essential flavors remain low to avoid diverting resources.

## Kimi-K2.5-Simple - Turn 424 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DELHI SECURED (3RD CAPITAL = 38% DOMINATION). Pivoting all forces to Edinburgh (Celtic capital = 4th capital = 50% victory) and London (English capital = 5th = 63%). Djenne declared war but irrelevant. Escalating UseNuke to 100 for immediate atomic bombardment of Edinburgh and London once Nuclear Fission completes. Maintaining maximum offensive posture with combined arms (Heavy Bombers, T-34s, Helicopter Gunships, Naval forces). America peace treaty expired - war imminent for Washington (6th = 75%). World Congress in 8 turns ignored - domination priority absolute.

- Replay: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> Increase the probability of deploying atomic bombs now that Nuclear Fission is queued, and ensure sufficient carrier capacity to project air power for nuclear strike delivery as we press the attack on Edinburgh and London.

## Kimi-K2.5-Simple - Turn 424 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DELHI SECURED (3RD CAPITAL = 38% DOMINATION). Pivoting all forces to Edinburgh (Celtic capital = 4th capital = 50% victory) and London (English capital = 5th = 63%). Djenne declared war but irrelevant. Escalating UseNuke to 100 for immediate atomic bombardment of Edinburgh and London once Nuclear Fission completes. Maintaining maximum offensive posture with combined arms (Heavy Bombers, T-34s, Helicopter Gunships, Naval forces). America peace treaty expired - war imminent for Washington (6th = 75%). World Congress in 8 turns ignored - domination priority absolute.

- Replay: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> Maintain the Conquest grand strategy as we have secured three capitals (Moscow, Delhi, Rome) and aim for the remaining key capitals (Edinburgh, London, Washington). Increase Science to accelerate Nuclear Fission research for atomic bombs, and set UseNuke to 100 to ensure aggressive nuclear deployment once available. Keep high Offense, Mobilization, Production, and MilitaryTraining to sustain large land, air, and naval forces needed for multi‑front assaults. Preserve strong Espionage, Air, and Naval flavors for strategic strikes, while keeping Wonder, Culture, and Diplomacy low as they do not support immediate domination goals.

## Deepseek-3.2-Simple - Turn 401 - retry 1

**Deviation (replay vs original):** use_nuke `-40`, nuke `-20`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 60 (Δ +30), nuke 50 => 80 (Δ +30)
> Maintain aggressive conquest posture while boosting nuclear development (Nuke, UseNuke) to finish wars against Ethiopia and Songhai. Increase Spaceship flavor to prepare for Science victory backup once Spaceflight Pioneers is adopted. Keep existing economic and military priorities.

## GPT-OSS-120B-Simple - Turn 333 - retry 2

**Deviation (replay vs original):** use_nuke `+10`, nuke `+15`

- Original: use_nuke 70 => 90 (Δ +20), nuke 70 => 85 (Δ +15)
> Maintain our aggressive Conquest posture while sharpening the most needed levers: more Expansion to claim the high‑quality settlement (74,24) and secure strategic footholds; higher Nuke/UseNuke to leverage our nuclear advantage; stronger AirCarrier and Airlift to project air power and rapid troop movement; boost Science for Rocketry and future tech; keep Offense, Mobilization, Production, and MilitaryTraining at max to sustain battlefield superiority.

- Replay: use_nuke 70 => 100 (Δ +30), nuke 70 => 100 (Δ +30)
> Maintain a hard‑line Conquest strategy while maximizing nuclear capability, air power, and expansion to secure new strategic settlements. Reduce Recon slightly to reallocate focus to offensive operations.

## Kimi-K2.5-Simple - Turn 422 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `-20`

- Original: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Turn 422: EXTINCTION CRISIS - 9 turns until French Cultural Victory. Entering maximum desperation mode: nuclear strike posture elevated to 100% launch probability, prioritizing destruction of French cultural centers. Science and Espionage maximized in desperate hope of accelerating Stealth technology or disrupting French infrastructure via spies (Paris network at 986). All civilian development halted (Spaceship/Culture/Gold/Expansion to 0), total war economy engaged.

- Replay: use_nuke 50 => 80 (Δ +30), nuke 50 => 80 (Δ +30)
> Switching to a Culture grand strategy will boost culture, tourism, and happiness, helping improve our Time and Cultural victory chances as the French cultural lead narrows. Adding significant Nuke and UseNuke flavors increases the likelihood of employing our nuclear arsenal to disrupt French cities. We keep some production and gold focus to sustain unit/building output while raising GreatPeople for future great works.

## Deepseek-3.2-Simple - Turn 459 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Byzantium is 1 turn from cultural victory and has overwhelming military superiority. Our only slim hope is to accelerate nuclear weapons development (Advanced Ballistics) to strike their cultural hubs, while using espionage to disrupt them. Prioritize Nuke, UseNuke, Espionage, and Science to rush nukes and counter-intelligence. Maintain maximum defensive and anti-air flavors to survive their air force. All efforts must focus on delaying their victory and enabling a nuclear decapitation strike.

- Replay: use_nuke 50 => 80 (Δ +30), nuke 70 => 100 (Δ +30)
> Increase nuclear development and usage urgency to obtain a deterrent against Byzantium's overwhelming military and air superiority, while maintaining strong production, air, and anti‑air focus for the ongoing Conquest strategy.

## Deepseek-3.2-Simple - Turn 459 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Byzantium is 1 turn from cultural victory and has overwhelming military superiority. Our only slim hope is to accelerate nuclear weapons development (Advanced Ballistics) to strike their cultural hubs, while using espionage to disrupt them. Prioritize Nuke, UseNuke, Espionage, and Science to rush nukes and counter-intelligence. Maintain maximum defensive and anti-air flavors to survive their air force. All efforts must focus on delaying their victory and enabling a nuclear decapitation strike.

- Replay: use_nuke 50 => 80 (Δ +30), nuke 70 => 100 (Δ +30)
> Maintain the Conquest grand strategy while pushing nuclear development to its maximum (Nuke 100, UseNuke 80). All other combat‑related flavors stay high to sustain our defensive and offensive push against Byzantium and Spain.

## Kimi-K2.5-Simple - Turn 447 - retry 1

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CRITICAL FLAVOR ADJUSTMENT - Atomic Bomb is now operational in Cordoba (ID 20485). Increased UseNuke from 50→90 to establish credible nuclear deterrent now that weapon system exists. Maintaining maximum Science (100), Spaceship (100), Production (100) priority to rush Satellites→Apollo Program before Carthage achieves cultural victory in ~47 turns. Espionage remains at 100 to steal technologies from ahead civilizations (Carthage, Poland, Germany). Culture reduced to 5 - we cannot win culturally with Carthage at Dominant with 4/5 civs. Defense maintained at 85 to prepare for German betrayal while researching.

- Replay: use_nuke 50 => 75 (Δ +25), nuke 100 => 100 (Δ +0)
> Maintain the Spaceship grand strategy while maximizing science, production, and great person generation to fast‑track Apollo and spaceship parts. Slightly lower Defense/CityDefense to free up production for research and builds, keep a credible nuclear deterrent (UseNuke 75) and ensure infrastructure and water connections support our expanding economy.

## GLM-4.7-Simple - Turn 356 - retry 2

**Deviation (replay vs original):** use_nuke `+20`, nuke `+0`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 100 (Δ +25), nuke 85 => 100 (Δ +15)
> Switching to a Conquest grand strategy reflects the urgent need to survive multiple hostile fronts (India, Persia, Poland).  Maximize Defense, MilitaryTraining, and Nuke/UseNuke to create a strong deterrent and sustain hardened city defenses.  Boost Production, Science and Gold to fund unit upgrades, nuclear weapons, and any late‑game projects.  Keep Diplomacy high to win city‑state allies for the upcoming UN vote, but prioritize military readiness over cultural or wonder builds.

## Kimi-K2.5-Simple - Turn 428 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 428 STATE: Nuclear interception failed but conventional assault succeeding - eliminated multiple Maya anti-air units. Palenque bombardment continuing effectively (city at 20% health). Still 8 turns until Brazil wins via Cultural Victory over Maya. ALL Four Maya cities must fall by turn 436 or game over. MAXIMUM AGGRESSION CONTINUES: Production/Mobilization at 100 for unit replacement, Air/Ranged at 100 for bombardment, UseNuke increased to 100 (emergency tactical nuke if conventional assault stalls on Palenque's 42-population defense). Spaceship backup at 100 - may need to pivot to Great Engineer rushes if conquest fails. No territory expansion, no wonders, no culture - only war production and city capture.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Maintain aggressive Conquest focus while ensuring nuclear weapons are prioritized (UseNuke set to 100) and boosting MilitaryTraining to improve unit quality for the final Maya push.

## Deepseek-3.2-Simple - Turn 409 - retry 3

**Deviation (replay vs original):** use_nuke `+10`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> Our naval counterattack has destroyed a Swedish Dreadnought and a Destroyer, shifting momentum. We must press the advantage with maximum naval, air, and nuclear focus to invade Swedish coastal cities (Stockholm, Turku, Espoo). Increase Nuke and UseNuke to 100/90 to prioritize nuclear missile development (Advanced Ballistics after Nuclear Fission completes in 4 turns) for strategic bombing. Naval and Air at 100 ensure sea control and air superiority. Maintain high Production, Gold, Science to fund military, and Happiness/Growth to support war economy. Diplomacy and Espionage secure city-state alliances and counter Swedish spies. All other flavors aligned with domination victory.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 95 => 100 (Δ +5)
> Boost Nuke and UseNuke to max to prioritize building and deploying nuclear missiles against Sweden's coastal capitals. Increase AirCarrier to support carrier production for air superiority in amphibious assaults. Raise MilitaryTraining and Air to ensure our forces stay elite and can sustain high‑intensity warfare. Strengthen NavalGrowth to expand shipyards and maintain naval dominance for the upcoming sea invasions.

## Kimi-K2.5-Simple - Turn 458 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Turn 458: CRITICAL 3-TURN COUNTDOWN. World Congress votes on Global Hegemony in 3 turns - Songhai has 41 delegates, needs 39 to win Diplomatic Victory immediately. Must capture Paris, Gao, and Madrid (the three capitals Songhai holds) before then. Peace treaty expired - total war is active. Increased UseNuke to 100 to guarantee nuclear strikes on heavily defended capitals for rapid capture. Overwhelming 5:1 military advantage (211k vs 40k) with massive air superiority. All production focused on Stealth Bombers, XCOM, and Modern Armor for lightning strikes. No defensive considerations - only total offense to secure Domination Victory before Songhai secures Diplomatic Victory.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 100 => 100 (Δ +0)
> Maintain the Conquest grand strategy as the primary focus: capture Paris, Gao, and Madrid before Songhai secures a Diplomatic Victory. Existing offensive and production flavors already drive massive unit output. Slightly raise 'UseNuke' to 70% to increase the chance of nuclear strikes against high‑value enemy capitals while keeping other flavors steady for continued air, land, and naval pressure.

## GLM-4.7-Simple - Turn 471 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Current strategic direction remains optimal. Critical developments: Apollo Program completed enabling spaceship construction, nuclear deterrent expanded to 2 Atomic Bombs in Sukhothai (forward deployment), 4 more Atomic Bombs under construction (Si Satchanalai in 2 turns, Sukhothai in 8-10 turns). Combat successes destroyed 5 Polynesian ships and 2 bombers while killing 1 American Mobile SAM unit. Gold crisis (-130 GPT) requires careful management but strategic priorities (nuclear deterrence, defense, World Congress) must continue. World Congress vote in 3 turns: must block America's World Ideology: Freedom proposal and support Repeal: Sanction: Songhai and China's International Space Station. China/Carthage alliances (70/70 and 75/75) provide critical coalition support. Stealth research (19 turns) progresses toward Nuclear Missiles for stronger nuclear deterrent. Status quo maintains focus on coalition defense through nuclear balance, diplomatic victory blocking, and scientific progress.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Maintain the United Nations grand strategy but re‑balance our flavor priorities: reduce over‑investment in static defense to free production for spaceship parts and additional nuclear units, keep Science at maximum to stay ahead technologically, retain high Gold and Diplomacy to fund the war effort and win city‑state support before the UN vote, and keep Nuke/UseNuke at full to deter America. Slightly raise Offense to allow limited counter‑attacks while preserving a defensive posture.

## Kimi-K2.5-Simple - Turn 390 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> Emergency defensive posture with nuclear deterrent imminent. Greece's 3:1 military superiority and diplomatic victory attempt in 6 turns creates existential crisis. Nuclear Fission completes in 1 turn with 14 uranium ready. Maximize UseNuke (100) for immediate atomic deployment. Maintain Defense/CityDefense/Mobilization at 100 to survive until deterrent operational. Reduce Naval from 95 to 85 as American destroyer threat is severe but manageable. Boost Espionage to 100 to protect science cities and maintain election rigging in Enns. Increase Spaceship to 95 as backup victory path if culture is disrupted. Diplomacy raised to 80 to counter Greece's 34 delegates in upcoming World Congress vote on United Nations proposal.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Accelerate nuclear deterrence by maxing Nuke and UseNuke flavors, while boosting Science and Culture to speed research and tourism growth for our cultural victory. Maintain maximal defensive posture (Defense, CityDefense, Mobilization) to survive Greece's 3:1 advantage. Slightly raise GreatPeople and Production to generate more great artists and build late-game wonders, while keeping Expansion at zero to avoid over‑extension.

## Kimi-K2.5-Simple - Turn 387 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> TURN 387: MAXIMUM WAR FOOTING. Austria at 83% diplomatic victory with 4 turns remaining. All resources must pivot to immediate military production. Nuke/UseNuke at 100 for instant atomic weapon deployment upon Nuclear Fission completion. Offense/Mobilization/Production at 100 to maximize unit output for desperate Vienna strike. Air at 90 for heavy bomber production (conventional strategic bombing as fallback). Antiair at 100 counters Austria's air superiority. Diplomacy/Wonder/Culture at 0 - no time for long-term investments. Only total war can prevent defeat.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 100 => 100 (Δ +0)
> Maximize production and mobilization to finish atomic bomb units ASAP and sustain a strong offensive front. High Offense and UseNuke values push the AI to employ nuclear weapons against Austrian capitals. Air and Antiair are boosted to protect our forces and support bombing runs. Production and Mobilization at 100 ensure rapid unit and building output needed for a decisive strike.

## GLM-4.7-Simple - Turn 381 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `-15`

- Original: use_nuke 50 => 85 (Δ +35), nuke 70 => 95 (Δ +25)
> Adjusted flavors to maximize Golden Age exploitation and multi-front war efficiency. Increased Mobile to 85 (from 80) to prioritize fast-moving Landships and upcoming Tanks for breakthrough operations during Golden Age. Increased Air to 85 (from 80) to expand Bomber coverage for all three fronts. Production raised to 95 (from 90)配合 Total War's +25% bonus for rapid unit buildup. Slight reduction in Naval (65) reflects need to focus on decisive land advances while maintaining sufficient coastal defense. UseNuke reduced to 40 (from 50) as nuclear capabilities are deterrent-focused. Maintaining high Offense (80), MilitaryTraining (85), Antiair (85) and Mobilization (50) for sustained warfare capability.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 70 => 80 (Δ +10)
> Boost naval combat and reconnaissance to counter Germany's superior fleet, increase air power and anti‑air to protect our bombers and support the upcoming nuclear deterrent, raise nuclear focus and usage probability as Atomic Theory will be completed shortly, and slightly enhance production and science to keep unit queues flowing while maintaining the Conquest grand strategy.

## Deepseek-3.2-Simple - Turn 413 - retry 3

**Deviation (replay vs original):** use_nuke `-80`, nuke `-20`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> We are researching Atomic Theory next to unlock nuclear weapons. Setting Nuke and UseNuke flavors to 100 ensures we prioritize building nukes and are willing to use them strategically once available. This will be crucial for breaking Germany's heavily fortified coastal capitals (Berlin and Beijing) and accelerating the endgame. Other military flavors remain high to sustain our overwhelming conventional advantage.

- Replay: use_nuke 0 => 20 (Δ +20), nuke 0 => 80 (Δ +80)
> Maintain the aggressive Conquest stance while now prioritizing nuclear development (Nuke) and the actual use of nukes (UseNuke) to secure decisive blows against Germany's coastal defenses. Keep high offensive, mobile, air, and naval flavors to sustain the multi‑front push, and retain production, gold, and science boosts for continued unit and technology output.

## Kimi-K2.5-Simple - Turn 392 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Manhattan Project COMPLETED in Karakorum - nuclear weapons now available! With peace treaties expired and Patriotic War policy active, immediately shifting to total war footing. UseNuke increased to 100 to ensure immediate atomic weapon employment once Nuclear Fission completes (12 turns). Offense and Mobile at 95/90 for twin assaults on Persepolis (Persia) and Washington (America). Air 100 prioritizes Heavy Bombers for atomic bomb delivery via Radar technology. Will fight two-front war against Autocracy powers while maintaining deception toward Order allies, particularly Korea. Science 100 critical for Advanced Ballistics nuclear missile delivery systems.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Maintain a hard‑charging Conquest posture: full emphasis on mobilization, production, science, and nuclear capabilities, while keeping enough support for infrastructure and happiness to sustain the war effort.

## GLM-4.7-Simple - Turn 437 - retry 2

**Deviation (replay vs original):** use_nuke `+10`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 90 after Awasa nuclear attack - Netherlands has now used 3 atomic weapons against my cities (Turfan x2, Awasa). No choice but to prepare nuclear retaliation as deterrent. Increase Air to 95 and Antiair remains 100 - demonstrated success shooting down 3 Netherlands Fighters this turn, must maintain air superiority against their bombers and XCOM attacks. CityDefense increased to 95 - with Netherlands nuclear buildup at Nijmegen (3+ atomic bombs visible) and XCOM paradrop squads, all cities need maximum protection. Offense increased to 60 to pressure Netherlands territory before they can launch more nuclear strikes. Diplomacy reduced from 90 to 85 - coalitions matter but survival against nuclear Netherlands takes priority. Espionage at 100 - need intelligence on Netherlands nuclear deployment and counter-espionage at critical cities like Attila's Court, Shedet.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Maintain Conquest focus but push Offense and UseNuke to maximum to drive aggressive operations against the Netherlands. Slightly lower Defense to reallocate production toward offensive units. Boost Diplomacy to keep allies (Mongolia, Venice, Japan) solidified while preserving high Science, Production, Gold, and Military training.

## Deepseek-3.2-Simple - Turn 405 - retry 1

**Deviation (replay vs original):** use_nuke `-80`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> The Aztecs have captured Shanghai and war resumes next turn. We must prepare for an overwhelming assault. Setting UseNuke to 100 ensures we will employ nuclear weapons defensively if necessary to halt their advance. MilitaryTraining at 100 prioritizes unit upgrades and quality, giving our outnumbered forces a fighting chance.

- Replay: use_nuke 0 => 20 (Δ +20), nuke 100 => 100 (Δ +0)
> War with the Aztecs resumes in two turns. Switching to a Conquest grand strategy focuses production, gold, and food towards military buildup while still allowing some cultural output. The flavor adjustments dramatically boost offensive and defensive capabilities, mobilization, air and anti‑air strength, and nuclear readiness, ensuring we can meet the Aztec threat. Remaining cultural, religious, and diplomatic flavors keep our longer‑term cultural victory trajectory and alliance benefits intact.

## Kimi-K2.5-Simple - Turn 421 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear weapons immediately available. Increased UseNuke to 100 for maximum aggression against Babylon. Babylon has Apollo Program (existential threat) with 2 Uranium and can build spaceship parts. Must deploy nuclear weapons immediately to destroy their production centers and prevent science victory. Maintaining maximum air power (100) for nuclear delivery capability and conventional strikes. War score only 12% against Babylon despite superior military - need to push harder before they complete spaceship parts. Ottoman alliance strong, trade secured for resources. Focus on producing nuclear missiles and advanced air units to deliver them.

- Replay: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Maximize the probability of employing nuclear strikes now that the Manhattan Project is complete, ensuring we can leverage our nuclear advantage against Babylon while maintaining our current aggressive military posture.

## Kimi-K2.5-Briefed - Turn 391 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> T391 CRITICAL PRODUCTION CORRECTION: Military briefing confirms AA-Gun production failed to start in Tarsus and Research Lab missing in Gordium despite defensive priorities. Reduce Offense 70→50 and Mobile 85→70 to focus AI bandwidth on critical infrastructure. Increase UseNuke 85→100 to ensure immediate atomic deployment upon Manhattan Project completion. Increase Espionage 75→85 to capitalize on successful Panama City election rigging and continued Hunnic/Siamese intelligence operations. Maintain all defensive, antiair, and nuclear production priorities at maximum.

- Replay: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Persia is on the brink of completing Atomic Theory and must transition immediately to Nuclear Fission to unlock the Manhattan Project and nuclear weapons as a deterrent against the Huns. Raising MilitaryTraining, Infrastructure, Science, and Production to their maximum ensures rapid construction of AA‑Guns in Tarsus, a Research Lab in Gordium, uranium mines, and the Manhattan Project. Maintaining maximal Defense, CityDefense, Nuke, UseNuke, Air, Antiair, and Recon preserves our fortified posture while supporting any required air‑defence and strike capabilities.

## Kimi-K2.5-Simple - Turn 392 - retry 3

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Nuclear Fission complete - MAXED Nuke to 100 and UseNuke to 95 for immediate atomic deterrent deployment against Egyptian forces. WC vote in 4 turns with exactly 45 delegates (28 Poland + 8 Inca + 9 Denmark). Cannot afford to lose Melbourne/Yerevan. Raised Diplomacy to 90 to consolidate CS alliances post-war. Defense remains at 95 against Egyptian naval pressure. Science/Production maintained for military infrastructure.

- Replay: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> With nuclear capability secured, shift flavors toward aggressive offense, full nuclear use, and high diplomatic effort to force peace with Egypt while securing city‑state allies. Maintain strong defense and production to keep our forces robust for any residual conflicts.

## GLM-4.7-Simple - Turn 356 - retry 1

**Deviation (replay vs original):** use_nuke `+10`, nuke `+0`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 90 (Δ +15), nuke 85 => 100 (Δ +15)
> We are in a multi‑front war against a vastly superior Indian army while still pursuing a science victory. Maintaining the current defensive posture is essential, but we need to accelerate production and mobilization to build nuclear plants, spaceship components, and additional fortifications. Raising Nuke and UseNuke to their maximum ensures our newly acquired uranium can be turned into a credible deterrent. Slightly increasing Air to 95 improves air defence against India's large air forces. Boosting Happiness to 85 helps mitigate the combat penalty from unhappiness. All other flavor priorities (defense, city defense, military training, diplomacy, espionage, etc.) remain at their current high levels.

## Kimi-K2.5-Simple - Turn 406 - retry 3

**Deviation (replay vs original):** use_nuke `+5`, nuke `-5`

- Original: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> Cultural Victory is imminent - need Citizen Earth Protocol completion. Maximum defensive posture (Defense 95, CityDefense 95) to hold against Indian XCOM/Helicopter attacks while wonder is built. Nuke/UseNuke at 95/85 for MAD deterrent against further Indian nuclear strikes. Production 100 and Wonder 100 essential for rushing Citizen Earth Protocol. Reduced Offense to 5 - no need to attack when victory comes from wonder completion. Science 70 to reach Advanced Ballistics for nuclear deterrent. All resources focused on defensive survival and wonder production.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 90 (Δ +0)
> Maintain cultural victory focus while bolstering defense against India's aggressive air and nuclear attacks. Increase Science to accelerate Advanced Ballistics and Nuclear Missile research, raise MilitaryTraining and UseNuke for deterrence, and boost Espionage to counter India's spy network. Other flavors remain high to protect cities, produce wonders, and sustain production.

## GLM-4.7-Simple - Turn 435 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Iroquois 97% Popular - cultural extinction in 3-4 turns. Maximum offensive posture required to capture Onondaga before cultural victory. Espoo Stealth Bomber complete provides immediate air strike capability. Linköping Stealth Bomber in 4 turns is too slow - must use existing air assets and conventional forces at Genesse River NOW. UseNuke 100 authorizes nuclear strikes if conventional forces cannot reach Onondaga in time. All production and resources prioritized for war. Diplomacy irrelevant when facing extinction - complete conquest or nothing matters.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> The Iroquois are on the brink of a cultural victory (97% popularity). To prevent an existential loss, Sweden must maximize its offensive firepower and guarantee the use of nuclear weapons. Raising UseNuke to 100 ensures nukes will be employed when needed, while keeping Offense, Mobilization, Air, and Nuke at their maximum maintains pressure on Iroquois forces. All other strategic priorities remain unchanged to sustain our current war effort.

## GLM-4.7-Simple - Turn 381 - retry 1

**Deviation (replay vs original):** use_nuke `-25`, nuke `-15`

- Original: use_nuke 50 => 85 (Δ +35), nuke 70 => 95 (Δ +25)
> Adjusted flavors to maximize Golden Age exploitation and multi-front war efficiency. Increased Mobile to 85 (from 80) to prioritize fast-moving Landships and upcoming Tanks for breakthrough operations during Golden Age. Increased Air to 85 (from 80) to expand Bomber coverage for all three fronts. Production raised to 95 (from 90)配合 Total War's +25% bonus for rapid unit buildup. Slight reduction in Naval (65) reflects need to focus on decisive land advances while maintaining sufficient coastal defense. UseNuke reduced to 40 (from 50) as nuclear capabilities are deterrent-focused. Maintaining high Offense (80), MilitaryTraining (85), Antiair (85) and Mobilization (50) for sustained warfare capability.

- Replay: use_nuke 50 => 60 (Δ +10), nuke 70 => 80 (Δ +10)
> Boost naval and air power, increase nuclear readiness, and maintain high production and science to press the war and secure domination.

## Deepseek-3.2-Simple - Turn 469 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> The Netherlands is at 84% diplomatic victory; we must accelerate capture of Polynesian capitals (Honolulu, Assur) to achieve domination before they win. Increasing UseNuke and Nuke flavors prepares for nuclear strikes if conventional assault fails. Maintaining maximum Offense, Defense, Mobilization ensures continuous unit production. Science and Gold are critical for researching Stealth Bombers and purchasing units. Happiness offsets war weariness, and Espionage protects our science cities.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Maintain a full‑scale conquest posture: maximize offensive, mobilization, and production to field large armies and build advanced units, while emphasizing Nuke and Air to gain strategic firepower. Keep moderate defense and happiness to sustain front‑line stability and public order during intense multi‑front warfare.

## GLM-4.7-Briefed - Turn 398 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+10`

- Original: use_nuke 60 => 80 (Δ +20), nuke 40 => 60 (Δ +20)
> Significant strategic shift due to devastating naval losses (both Dreadnoughts destroyed). Increase Defense (95→100), CityDefense (90→100), MilitaryTraining (90→100) to shore up defensive posture against France's naval superiority. Raise Naval (90→95) and Antiair (80→100) to prioritize naval rebuilding and counter French air threats. Increase Nuke (40→60) and UseNuke (60→80) to prepare nuclear deterrence as England nears Advanced Ballistics (14 turns). Gold (80→95) increased to rebuild navy through upgrading from Ironclad level to modern capital ships. Production (90→95) increased to accelerate Spaceship components and unit upgrades. Happiness (80→90) to address combat penalty after treasury depletion. Espionage (90→100) to monitor France's nuclear progress and tech parity. Spaceship remains max priority as path to victory despite military setbacks.

- Replay: use_nuke 60 => 70 (Δ +10), nuke 40 => 70 (Δ +30)
> Maintain the Spaceship grand strategy while reinforcing the science, production and spaceship pipelines. Increase Gold and Happiness flavors to shore up our strained treasury and unhappy populace, and boost Nuke/UseNuke to create a credible nuclear deterrent against France. Keep Defense high to protect our coastlines, lower Offense to avoid costly offensives while we rebuild naval strength, and keep Diplomacy high to maximise city‑state influence and trade.

## Deepseek-3.2-Simple - Turn 469 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> The Netherlands is at 84% diplomatic victory; we must accelerate capture of Polynesian capitals (Honolulu, Assur) to achieve domination before they win. Increasing UseNuke and Nuke flavors prepares for nuclear strikes if conventional assault fails. Maintaining maximum Offense, Defense, Mobilization ensures continuous unit production. Science and Gold are critical for researching Stealth Bombers and purchasing units. Happiness offsets war weariness, and Espionage protects our science cities.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Maintain Conquest focus with maximal offensive and defensive production, fully capitalize on nuclear capabilities, bolster air and naval power, and keep economic (gold, production) and scientific output high to sustain a war of attrition against Netherlands, England, and Polynesia.

## GPT-OSS-120B-Simple - Turn 344 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 80 => 100 (Δ +20)
> Maximize our nuclear capabilities and carrier support to decisively strike Polynesian island forts, while maintaining our current aggressive conquest posture and strong production, gold, and happiness engines.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 80 => 100 (Δ +20)
> Shift flavor weighting to boost scientific output and nuclear capability while retaining strong production and offensive focus. Increased Espionage protects our high‑value assets as we push toward atomic weapons. Slightly lower Culture to avoid over‑investing in tourism during a major war.

## Kimi-K2.5-Briefed - Turn 336 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `-5`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> DEFENSIVE SURVIVAL PIVOT: Peace with Shoshone (accepted Turn 335) closes one front, but India remains existential threat (4,742 MS vs my 2,405, 98% control of Denmark). Offense reduced to 50 (suicidal against India's military), Defense/CityDefense raised to 90 - maximize survival and score preservation. Nuke/UseNuke maxed to 100 - emergency deterrent only hope to slow India. Mobilization stays high (90) to replace losses. Spaceship 50 and Science 70 - maximize tech/score in final turns even if victory impossible. Abandon expansion (0) - no time for new cities. Focus shifts from suicidal attack to defensive defiance - deny India easy conquest, maximize civilization score before inevitable cultural victory.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> Shift emphasis toward pure offensive power and maximum production to accelerate unit output for the imminent war with India. Reduce defensive weighting slightly to free up production for attack units. Increase Nuke and UseNuke to near‑maximum for deterrence. Keep naval and air support modest but sufficient. Production is boosted to the highest priority to enable rapid unit purchases and building of war‑related infrastructure.

## Deepseek-3.2-Simple - Turn 452 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's invasion imminent in 4 turns. Maximize nuclear readiness (Nuke 100, UseNuke 100) for deterrence and potential equalizer. Anti-air (100), city defense (100), production (100), and science (100) essential to survive and reach nuclear weapons. Naval and air at 100 to counter Danish naval/air supremacy. Reduce non-essential investments (NavalGrowth, NavalTileImprovement to 50) and focus on immediate survival. Offense lowered to 80 as we prioritize defense and limited counterattacks (e.g., Truro).

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 100 (Δ +10)
> Maintain the aggressive Conquest stance while maximizing nuclear production (Nuke 100, UseNuke 90) and preserving strong anti‑air, naval and air capabilities needed to defeat Denmark and the Zulus. Production, science and gold remain high to fund unit upgrades and the upcoming Advanced Ballistics research.

## Kimi-K2.5-Simple - Turn 391 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Nuclear weapons capability unlocked imminently; prioritizing UseNuke and Nuke flavors to 100 for immediate tactical nuclear strikes on Santiago/Murcia if uranium secured from Siam. Denmark upgraded to hostile for subsidizing Spanish victory - reduced Naval priority to 60 as coalition at sea fractured. Defense lowered to 80 to maximize offensive production. We have ~8 turns before World Congress votes on Passport System (+50% tourism) which would guarantee Spanish cultural victory. Must capture remaining Spanish cities immediately.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Maintain Conquest focus to capture Santiago quickly; boost air and naval power for sea and air superiority, keep high nuclear emphasis for a decisive strike, and preserve strong production and science to finish Manhattan Project and Advanced Ballistics.

## GLM-4.7-Simple - Turn 424 - retry 3

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> DEFENSIVE MAXIMUM ACTIVATED: Russia occupying Cologne, Stuttgart, Dortmund - 4.63x military superiority (15440 vs 3335). Defense 100, CityDefense 100, Antiair 100 - absolute priority preventing further territorial loss and defending core cities. MilitaryTraining 95 for unit quality under numerical disadvantage. Mobilization 90 for rapid production. Nuke 100, UseNuke 95 - Russia has 19 Uranium, Germany must achieve nuclear deterrence. Production 100, Science 100 - Space race accelerates as militarily infeasible alternative. Gold 90 for maintaining army under upkeep pressure. Diplomacy 80 for coalition building against Russia. Espionage 100 - intelligence on Russian nuclear and naval operations critical. Espionage focus on Moscow (spy Katrin at 166 network) to monitor Russian Manhattan Project and fleet movements. Spaceship 95 - Apollo Program enables victory path despite territorial losses.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maintain the science victory focus while raising offensive and nuclear capabilities to counter Russia, increase air power and espionage for intelligence, and boost wonder construction to aid cultural tourism. Slightly increase mobilization and production to sustain unit output.

## Kimi-K2.5-Simple - Turn 424 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Turn 423: Copenhagen siege in attrition deadlock while Denmark possesses Manhattan Project - nuclear deterrent capability is existential priority. Persepolis invasion stalled at 4% war score with Zone 1081 showing enemy dominance - need maximum Offense/Mobilization to force breakthrough before World Congress. Brazil's Apollo Program requires immediate preparation for transcontinental mobile warfare. Nuke/UseNuke increased to 100% given Manhattan Project race with Denmark. Production at 95 supports massive unit replacement for three-front war. Happiness at 100 critical as empire is at 55% happiness with extensive occupied territories.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Maintain the aggressive Conquest strategy while raising Production and Gold to fuel massive army and naval builds, and maximizing Nuke/UseNuke to ensure nuclear deterrence and strike capability. Other flavors remain balanced to keep economic stability and support the war effort.

## Kimi-K2.5-Simple - Turn 424 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Turn 423: Copenhagen siege in attrition deadlock while Denmark possesses Manhattan Project - nuclear deterrent capability is existential priority. Persepolis invasion stalled at 4% war score with Zone 1081 showing enemy dominance - need maximum Offense/Mobilization to force breakthrough before World Congress. Brazil's Apollo Program requires immediate preparation for transcontinental mobile warfare. Nuke/UseNuke increased to 100% given Manhattan Project race with Denmark. Production at 95 supports massive unit replacement for three-front war. Happiness at 100 critical as empire is at 55% happiness with extensive occupied territories.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Maintain aggressive Conquest focus: maximize offensive unit production, mobility, air superiority, and nuclear capability to pressure Persia, Denmark, and Brazil. Reduce defensive and wonder emphasis to allocate resources to war. Keep moderate diplomacy to manage vassals while prioritizing war outcomes.

## Kimi-K2.5-Simple - Turn 424 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Turn 423: Copenhagen siege in attrition deadlock while Denmark possesses Manhattan Project - nuclear deterrent capability is existential priority. Persepolis invasion stalled at 4% war score with Zone 1081 showing enemy dominance - need maximum Offense/Mobilization to force breakthrough before World Congress. Brazil's Apollo Program requires immediate preparation for transcontinental mobile warfare. Nuke/UseNuke increased to 100% given Manhattan Project race with Denmark. Production at 95 supports massive unit replacement for three-front war. Happiness at 100 critical as empire is at 55% happiness with extensive occupied territories.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Maintain aggressive Conquest stance while boosting our nuclear and air capabilities to press the war against Persia and deter Denmark/Brazil. Increase Production and Gold to sustain high unit output and fund expensive nuclear units. Slightly raise Defense to protect our front lines, and add a modest Wonder focus (20) to capture any critical late-game wonders that improve score. All other flavors remain as tuned for our current military dominance.

## GPT-OSS-120B-Simple - Turn 333 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `-5`

- Original: use_nuke 70 => 90 (Δ +20), nuke 70 => 85 (Δ +15)
> Maintain our aggressive Conquest posture while sharpening the most needed levers: more Expansion to claim the high‑quality settlement (74,24) and secure strategic footholds; higher Nuke/UseNuke to leverage our nuclear advantage; stronger AirCarrier and Airlift to project air power and rapid troop movement; boost Science for Rocketry and future tech; keep Offense, Mobilization, Production, and MilitaryTraining at max to sustain battlefield superiority.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 70 => 80 (Δ +10)
> Maintain the aggressive Conquest posture while bolstering city defense, expanding settlement pressure, and strengthening air carrier and nuclear capabilities. Raising Defense and Expansion ensures captured capitals are held and new strategic cities are founded quickly. Increased Nuke/UseNuke and AirCarrier values improve our deterrent and power projection over sea and land, complementing the existing high Offense, Mobile, and Naval flavors.

## Kimi-K2.5-Simple - Turn 392 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Manhattan Project COMPLETED in Karakorum - nuclear weapons now available! With peace treaties expired and Patriotic War policy active, immediately shifting to total war footing. UseNuke increased to 100 to ensure immediate atomic weapon employment once Nuclear Fission completes (12 turns). Offense and Mobile at 95/90 for twin assaults on Persepolis (Persia) and Washington (America). Air 100 prioritizes Heavy Bombers for atomic bomb delivery via Radar technology. Will fight two-front war against Autocracy powers while maintaining deception toward Order allies, particularly Korea. Science 100 critical for Advanced Ballistics nuclear missile delivery systems.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Maintain the aggressive Conquest grand strategy. Increase UseNuke to 90 to ensure higher probability of deploying nuclear strikes once our nukes are ready, while keeping existing high offensive, air, and production focus to sustain momentum against Persia and prepare for future wars.

## Kimi-K2.5-Simple - Turn 392 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `-5`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Nuclear Fission complete - MAXED Nuke to 100 and UseNuke to 95 for immediate atomic deterrent deployment against Egyptian forces. WC vote in 4 turns with exactly 45 delegates (28 Poland + 8 Inca + 9 Denmark). Cannot afford to lose Melbourne/Yerevan. Raised Diplomacy to 90 to consolidate CS alliances post-war. Defense remains at 95 against Egyptian naval pressure. Science/Production maintained for military infrastructure.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 95 => 95 (Δ +0)
> Maintain United Nations focus, bolster Defense and nuclear deterrence, increase Diplomacy and Espionage to sway city‑state votes and monitor Egypt, while keeping production and science high for continued growth. Reduce Offense to avoid unnecessary escalation.

## Deepseek-3.2-Simple - Turn 369 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Increasing UseNuke and Nuke flavors to maximum ensures the in-game AI prioritizes nuclear arsenal buildup and aggressive nuclear strike planning once we unlock Atomic Bombs. This aligns with our imminent war against China and The Maya, where nuclear weapons will be decisive in overcoming their numerical and defensive advantages. All other military and economic flavors remain high to sustain multi-front warfare and rapid conquest.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 100 (Δ +10)
> Maintain aggressive conquest focus with maximum offensive, production, and nuclear priorities while allowing modest expansion to secure a forward settlement near the frontier. Keep strong air, naval, and anti‑air support to dominate China and the Maya.

## Deepseek-3.2-Simple - Turn 409 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> Our naval counterattack has destroyed a Swedish Dreadnought and a Destroyer, shifting momentum. We must press the advantage with maximum naval, air, and nuclear focus to invade Swedish coastal cities (Stockholm, Turku, Espoo). Increase Nuke and UseNuke to 100/90 to prioritize nuclear missile development (Advanced Ballistics after Nuclear Fission completes in 4 turns) for strategic bombing. Naval and Air at 100 ensure sea control and air superiority. Maintain high Production, Gold, Science to fund military, and Happiness/Growth to support war economy. Diplomacy and Espionage secure city-state alliances and counter Swedish spies. All other flavors aligned with domination victory.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> With Nuclear Fission completing soon, we will soon acquire nuclear missiles (Advanced Ballistics). Raising Nuke and UseNuke to maximum ensures the AI aggressively employs atomic weapons to break Swedish coastal defenses. Boosting Air to 100 gives priority to air superiority and bombing, supporting naval invasions of Stockholm, Turku, and other Swedish ports. Slight increase to Recon (20) improves scouting to locate weak points. All other existing aggressive combat and economic flavors remain at their high values to sustain our Conquest strategy and keep our allies (Netherlands, Spain) supportive while maintaining production, gold, and science output for continued war efforts.

## Deepseek-3.2-Briefed - Turn 391 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 80 => 90 (Δ +10)
> Maintain aggressive conquest posture while boosting nuclear capabilities (Nuke/UseNuke) and great‑person generation to accelerate Manhattan Project and atomic bomb production. Preserve high science and production outputs for the continued war effort.

## Deepseek-3.2-Simple - Turn 369 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Increasing UseNuke and Nuke flavors to maximum ensures the in-game AI prioritizes nuclear arsenal buildup and aggressive nuclear strike planning once we unlock Atomic Bombs. This aligns with our imminent war against China and The Maya, where nuclear weapons will be decisive in overcoming their numerical and defensive advantages. All other military and economic flavors remain high to sustain multi-front warfare and rapid conquest.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 90 (Δ +0)
> Maintain an aggressive conquest posture with maximal offensive, production, and air/nuke focus while keeping high defense and mobility to sustain multi‑front wars against China, the Maya, and the Aztecs.

## Kimi-K2.5-Simple - Turn 421 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear weapons immediately available. Increased UseNuke to 100 for maximum aggression against Babylon. Babylon has Apollo Program (existential threat) with 2 Uranium and can build spaceship parts. Must deploy nuclear weapons immediately to destroy their production centers and prevent science victory. Maintaining maximum air power (100) for nuclear delivery capability and conventional strikes. War score only 12% against Babylon despite superior military - need to push harder before they complete spaceship parts. Ottoman alliance strong, trade secured for resources. Focus on producing nuclear missiles and advanced air units to deliver them.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 100 => 100 (Δ +0)
> Boost naval power and nuclear strike readiness as Babylon's nuclear program completes and our own Manhattan Project is near finish. Slightly increase espionage to better track enemy movements while maintaining the aggressive Conquest focus.

## Kimi-K2.5-Simple - Turn 403 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: CRISIS ESCALATION - Japan FLIPPED Salem using 2 Great Diplomats, stealing critical delegates. Now need 5 delegates (not 3) for diplomatic victory. Peace expired - war is now possible. Maximum military emergency posture: Offense/Mobilization/Air/UseNuke all at 100. Must either: 1) Rush final spaceship parts (Apollo completes in 4 turns), or 2) Nuclear strike Japan's Protocol cities if victory imminent. Increased Diplomacy to 60 for last push on Almaty (liberated, 43 vs Japan's 44) and Winchester.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Shift flavor weighting toward a massive offensive posture while preserving the Spaceship grand strategy. Maximize Offense, Mobilization, Nuke, Air and Naval strength to ensure we can deliver a decisive strike against Japan once peace expires, and to protect our own cities. Slightly raise Diplomacy and GreatPeople to keep the diplomatic delegate push and cultural generation for the diplomatic victory path. Keep Science at 100 to continue the spaceship race.

## GLM-4.7-Simple - Turn 431 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 75 => 80 (Δ +5), nuke 100 => 100 (Δ +0)
> After Brazil destroyed 3 anti-air units and continues nuclear-submarine attacks, increased Defense/CityDefense/Antiair/UseNuke to MAX for survival against two nuclear-armed superpowers. Mobilization 70 for replacing lost units. Production 100 for reconstruction. Science 100 for Spaceship path despite devastation. Gold 90 (economy -95 GPT deficit) for purchasing units/buildings. Happiness 100 - we're Unhappy with combat penalties, must prioritize. Espionage 100 - critical for intelligence on nuclear threats. Diplomacy 90 - World Congress in 7 turns, need delegates. Air 50 - build bombers for deterrence. GreatPeople 80 for Spaceship components. Decreased Growth and Navals as resources diverted to immediate survival.

- Replay: use_nuke 75 => 80 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintain our Spaceship grand strategy while bolstering the economy and diplomacy to survive Brazil's nuclear pressure. Raising Gold to 95 and Diplomacy to 95 leverages extra trade routes and city‑state influence for needed gold and delegates. Keeping Defense, CityDefense, Antiair, and UseNuke high preserves our deterrent posture. Slightly increase Air to improve bomber production for retaliation. Other flavors remain as previously tuned for survival.

## Kimi-K2.5-Simple - Turn 373 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 373: Nuclear Fission completed - we now have nuclear weapons for deterrence. War with Russia continues at +4% score (favorable). Major shift: reducing Offense to 25 (was 35) as we pursue defensive war only. UseNuke increased to 95 - we have actual nukes now and Russia is pushing into our territory. Reduced Espionage to 90 (was 95) - we have good network coverage. Increased Diplomacy to 90 (was 85) - World Congress vote in 7 turns for our World Ideology: Freedom proposal is critical. Must secure Korea (10 votes), Inca (9), and Babylon (16). Maintained maximum Science priority (100) - Korea overtook us 67-66, cannot afford to fall behind in tech race.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintain the spaceship focus while sharpening espionage to steal tech, boosting air and naval production for carrier/air force, and increasing production to speed spaceship parts. Other flavors stay aggressive on defense and diplomacy to keep the war effort managed.

## Kimi-K2.5-Simple - Turn 405 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 405 MAXIMUM EMERGENCY: Nuclear Fission priority increased to 100/100 - Manhattan Project completes in 2 turns, atomic bombs MUST be produced immediately. All offensive parameters at absolute maximum: 100 Offense/100 Mobilization/100 Mobile/100 Air/100 Nuke/100 UseNuke. Strike forces at Ecbatana/Kar-Tukulti-Ninurta must execute immediate conventional assault on Palenque/Chichen Itza while preparing tactical nuclear strikes. ZERO tolerance for peace. ONLY objective: capture Maya cities and halt Citizen Earth Protocol. Production 100 ensures rapid unit replacement. Espionage 70 continues spy operations in Maya cities.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> Maintain an extreme offensive posture with full mobilization and production focus, while maximizing Nuke and Air flavors to deliver decisive strikes. Boost Naval, Air, and Espionage flavors to support our naval/air superiority and protect against Maya espionage. Keep Expansion at zero to avoid diluting resources.

## Kimi-K2.5-Simple - Turn 385 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `-5`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> NUCLEAR DETERRENT DEPLOYMENT PHASE: Advanced Ballistics nearing completion (Satellites next). Maximum Nuke priority (100) to ensure immediate nuclear weapon production upon tech unlock. UseNuke increased to 90 for credible deterrent threat against Indonesia-Songhai invasion. Air/Antiair at 95 for superiority against combined 14,000+ enemy military. Science/Culture slightly reduced to 95 (still critical but survival priorities equal). Wonder at 90 for The Internet rush once Satellites completes. Diplomacy nudged to 75 anticipating post-nuclear peace negotiations with India.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 95 => 95 (Δ +0)
> Maintain Culture grand strategy for tourism boost while tightening defensive focus. Increase Production, Gold, Diplomacy and UseNuke to 85 to fund more units, city‑state influence and make nuclear deterrence more likely. Slightly raise Happiness to sustain war weariness. Keep all other high‑priority flavors unchanged.

## Kimi-K2.5-Simple - Turn 359 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FISSION RESEARCHED - Atomic Era begins! First priority is immediate Manhattan Project construction and Atomic Bomb production. Babylon has 11 Uranium and active Manhattan Project in Borsippa. Austria also racing with Manhattan Project in Vienna. Must strike Babylon first with surprise atomic attack while maintaining deception. Air 100 and Nuke 100 ensure immediate Bomber/Atomic Bomb production. Offense 95 prepares for post-nuclear blitz. Espionage 80 protects Nuclear Fission from theft. Deception with Babylon (Open Borders, DoF, Defensive Pact) MUST continue until first bombs complete.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maximum offensive and nuclear focus to prepare for the imminent atomic strike on Babylon while keeping a strong production engine. Boost happiness to mitigate current unhappiness penalties and increase science and espionage to speed up post‑war tech race and protect our nuclear assets. Slightly lower defense to free production for bomb construction.

## GLM-4.7-Simple - Turn 411 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> EXISTENTIAL DEFENSE AGAINST RUSSIAN DIPLOMATIC DOMINANCE - UN vote in 10 turns with Russia at 95% victory (40 delegates vs blocking coalition 43). Maintaining UnitedNations grand strategy - abandoning now wastes diplomatic investment when Spain alliance (30 delegates) + my 13 + vassals 13 = 56 votes barely blocks Russia's 40. Just need to HOLD for 10 turns. Adjustments: Defense/CityDefense/Antiair +2 each (97) to prepare for Russian air/naval escalation (Jet Fighter produced). Production +5 (87) to accelerate factories, military academies, nuclear infrastructure after Workers' Faculties in 2 turns. Gold +5 (74) for emergency defensive purchases. Diplomacy +18 (100) maximum - urgency to maintain Spain alliance, potentially reposition spies. Science maintained at 100 - primary path to Nuclear Fission (4 turns) for atomic deterrent against Russia's 9x military advantage. Nuke/UseNuke remain 100 - nuclear development remains emergency priority. Air +5 (61) to counter Russian air superiority. Naval +5 (75) after destroyer loss to Russian submarines. Espionage +5 (95) for critical city-state election rigging counter-intelligence. Offense/Ranged/Mobile unchanged - no offensive capability against Russia's superior forces. Goal: SURVIVE 10 turns to block Russian diplomatic victory, accelerate nuclear deterrent as backup, strengthen defensive lines.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintain United Nations focus while boosting Mobilization, Production, and MilitaryTraining to finish Nuclear Fission quickly and build deterrent forces. Increase UseNuke and Espionage to 100 for maximal nuclear readiness and counter‑intelligence against Russia. Other flavors stay as before to preserve defensive strength and diplomatic outreach.

## Kimi-K2.5-Simple - Turn 359 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FISSION RESEARCHED - Atomic Era begins! First priority is immediate Manhattan Project construction and Atomic Bomb production. Babylon has 11 Uranium and active Manhattan Project in Borsippa. Austria also racing with Manhattan Project in Vienna. Must strike Babylon first with surprise atomic attack while maintaining deception. Air 100 and Nuke 100 ensure immediate Bomber/Atomic Bomb production. Offense 95 prepares for post-nuclear blitz. Espionage 80 protects Nuclear Fission from theft. Deception with Babylon (Open Borders, DoF, Defensive Pact) MUST continue until first bombs complete.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintain a hard‑line conquest stance while maximizing nuclear capabilities. Offense, Mobilization, and Production stay at peak to field units and build bombers. Nuke and UseNuke set to maximum to ensure rapid deployment of atomic weapons against Babylon. Air remains high for bomber support. Minor flavors (Science, Culture, GreatPeople) stay balanced to keep our long‑term options open.

## GLM-4.7-Briefed - Turn 409 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> MULTI-THEATER EMERGENCY RESPONSE for Shoshone Cultural Victory (6 turns) and Treasury Crisis: Offense 95, Mobile 95, Nuke 100, UseNuke 100 - maximum priority on Shoshone disruption via nuclear/conventional assault in 6-turn window. Gold increased to 85 (from 70) - CRITICAL address of treasury exhaustion (~8 turns) through uranium sales + gem liquidation to survive until Manhattan completion. Defense reduced to 70 (from 75), CityDefense to 70 (from 80) - resources diverted from secondary holdings to Shoshone front. Diplomacy 95 (from 90) - enhanced priority on Carthage peace for delegate bloc and potential sanction relief. Science 100 maintained - fundamental for nuclear capability and keeping tech parity. This is all-hands-on-deck existential threat response.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> We must fund nuclear production and keep the war effort against Shoshone while urgently improving gold income to stop the -242 G/t deficit. Raising Gold to 90 and shifting some Science to 80 still leaves enough research to finish Nuclear Fission (3 turns) and Advanced Ballistics, but gives a significant boost to gold‑generating tiles/buildings. Offense/Mobile are kept high for rapid strikes on Shoshone cities; UseNuke and Nuke are set to maximum to ensure the AI will prioritize nuclear deployment once the missiles are available. Diplomacy remains high to help secure the Carthage peace and influence city‑state flips.

## GLM-4.7-Simple - Turn 362 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> Adjusting for strategic balance: Defensive posture against two nuclear-armed enemies (Ethiopia, Netherlands). Happiness prioritized to 100 - critical at 42% with combat penalty affecting all operations. NavalRecon increased to 90 - enhanced Ethiopian Submarine/Destroyer activity detection around Ur and coastal cities. Nuke/UseNuke raised to 95/80 - matching Ethiopia Manhattan Project urgency, nuclear deterrence is now primary security requirement. Switched to Conquest grand strategy to better coordinate multi-front war management while maintaining Spaceship. Diplomacy increased to 75 - World Congress voting in 5 turns against Netherlands sanctions needs support. Espionage at 90 - Ethiopian spies detected in Halab, Harran, Kar-Tukulti-Ninurta require counter-intelligence.

- Replay: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> War with Ethiopia and the Netherlands demands stronger offensive and naval capabilities while we still need to push the Spaceship. Increase Offense, MilitaryTraining, Naval, and Air flavors to win battles, keep Defense high to protect our core, boost Happiness to eliminate combat penalties, and raise Diplomacy to improve city‑state influence for future votes.

## Kimi-K2.5-Briefed - Turn 336 - retry 3

**Deviation (replay vs original):** use_nuke `-15`, nuke `-5`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> DEFENSIVE SURVIVAL PIVOT: Peace with Shoshone (accepted Turn 335) closes one front, but India remains existential threat (4,742 MS vs my 2,405, 98% control of Denmark). Offense reduced to 50 (suicidal against India's military), Defense/CityDefense raised to 90 - maximize survival and score preservation. Nuke/UseNuke maxed to 100 - emergency deterrent only hope to slow India. Mobilization stays high (90) to replace losses. Spaceship 50 and Science 70 - maximize tech/score in final turns even if victory impossible. Abandon expansion (0) - no time for new cities. Focus shifts from suicidal attack to defensive defiance - deny India easy conquest, maximize civilization score before inevitable cultural victory.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> Maintain the Conquest grand strategy with an even stronger offensive push against India. Increase Offense, Ranged, Nuke, and MilitaryTraining to boost unit effectiveness, while keeping Defense sufficient to hold our cities. Production is maximized for rapid unit purchases; other flavors remain largely unchanged to preserve current economic stability.

## Kimi-K2.5-Simple - Turn 372 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 372: TOTAL WAR POSTURE MAINTAINED. Brazil peace expires in 6 turns - all military resources must prepare for Rio de Janeiro assault. Heavy Bomber lost to Alexandria interception but Ollantaytambo produces replacement in 1 turn. Manhattan Project completes in 4 turns at Cusco. Alexandria capture in progress - Field Gun and Lancer eliminated, Cavillaca spy at 480 network can assist. UseNuke increased to 100% - will deploy nuclear weapons immediately upon Manhattan Project completion. Maximum aggression ensures AI prioritizes Brazilian invasion over defensive operations. Spaceship at 70 maintains science victory pathway as backup if Brazil conquest fails.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Switching to a Conquest grand strategy aligns with our imminent war against Brazil. We keep extremely high Offense, Mobilization, Nuke, and boost Naval to 100 for a strong sea and air bombardment of Rio. AirCarrier is raised to support carrier‑based air power. Other flavors remain as before to sustain production, science, and happiness.

## GLM-4.7-Simple - Turn 408 - retry 1

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> CRITICAL: Portugal completed SS Engine (3rd spaceship part) and CERN - emergency nuclear strike plan. Maximizing Offense/Mobilization/Nuke/UseNuke to 100 for Portugal theater operations. Science and Production at 100 to rush Advanced Ballistics and nuclear missile production before Portugal achieves nuclear superiority. Air at 95 for Golden Age bomber operations starting in 2 turns. Diplomacy maintained for coalition coordination (Germany must conduct ground invasion alongside our nuclear strikes). Defense reduced to 40 - total war mode acceptable given Portugal's multi-victory threat requiring breaking through before they complete spaceship.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Fine‑tune flavors to keep our massive offensive push while reinforcing defenses around key cities, maintain high production and science output for nuclear tech, and keep diplomatic activity strong to hold the coalition in the World Congress.

## Kimi-K2.5-Simple - Turn 423 - retry 1

**Deviation (replay vs original):** use_nuke `+2`, nuke `+0`

- Original: use_nuke 95 => 98 (Δ +3), nuke 100 => 100 (Δ +0)
> FINAL PHASE CULTURAL VICTORY PROTECTION: Citizen Earth Protocol 7 turns from completion. Prioritize CityDefense 95 and Nuke 100/UseNuke 98 to deter Dutch nuclear attack on York. Reduce Offense to 65 as consolidation sufficient after Haarlem capture. Maintain Science 90 for Advanced Ballistics backup. Happiness 85 critical to maintain stability while operating near capacity. Culture/Wonder remain maximum priority.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintain strong defensive and cultural focus while increasing happiness to counter current unhappiness, boosting diplomacy to solidify world‑congress influence, and maxing nuclear deterrence. Slightly lower offense to preserve resources, raise infrastructure for better city output, and keep scientific output high for the upcoming nuclear tech.

## Kimi-K2.5-Simple - Turn 452 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `-5`

- Original: use_nuke 90 => 95 (Δ +5), nuke 95 => 100 (Δ +5)
> Turn 452: Critical survival situation - Byzantium at 40/44 delegates with World Congress voting in 1 turn. They just demonstrated nuclear aggression by nuking Madrid. Apollo Program completes next turn - must immediately pivot to maximum spaceship production. Increased Nuke flavor to 100 (from 95) and UseNuke to 95 (from 90) - need immediate nuclear deterrent capability given Byzantine nuclear attack and Mongol peace expiry. Production boosted to 95 (from 90) for rapid spaceship part construction after Apollo completes. GreatPeople to 85 for Great Engineer acquisition. All other priorities secondary to surviving long enough to complete science victory.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 95 => 95 (Δ +0)
> We are on the cusp of completing the Apollo Program (turn 453) and need to shift all available production toward spaceport construction and the first spaceship parts. Boost Production, Science, and Spaceship flavors to maximize output, while keeping Defense high to protect against the imminent nuclear threat from Mongolia and the overwhelming military of Byzantium. Reduce focus on Culture, Diplomacy, and Expansion to free resources for the science victory path.

## GLM-4.7-Simple - Turn 411 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> EXISTENTIAL DEFENSE AGAINST RUSSIAN DIPLOMATIC DOMINANCE - UN vote in 10 turns with Russia at 95% victory (40 delegates vs blocking coalition 43). Maintaining UnitedNations grand strategy - abandoning now wastes diplomatic investment when Spain alliance (30 delegates) + my 13 + vassals 13 = 56 votes barely blocks Russia's 40. Just need to HOLD for 10 turns. Adjustments: Defense/CityDefense/Antiair +2 each (97) to prepare for Russian air/naval escalation (Jet Fighter produced). Production +5 (87) to accelerate factories, military academies, nuclear infrastructure after Workers' Faculties in 2 turns. Gold +5 (74) for emergency defensive purchases. Diplomacy +18 (100) maximum - urgency to maintain Spain alliance, potentially reposition spies. Science maintained at 100 - primary path to Nuclear Fission (4 turns) for atomic deterrent against Russia's 9x military advantage. Nuke/UseNuke remain 100 - nuclear development remains emergency priority. Air +5 (61) to counter Russian air superiority. Naval +5 (75) after destroyer loss to Russian submarines. Espionage +5 (95) for critical city-state election rigging counter-intelligence. Offense/Ranged/Mobile unchanged - no offensive capability against Russia's superior forces. Goal: SURVIVE 10 turns to block Russian diplomatic victory, accelerate nuclear deterrent as backup, strengthen defensive lines.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintain United Nations focus to block Russia's diplomatic victory while ensuring maximal defensive and nuclear readiness (Defense, CityDefense, Nuke, UseNuke). Keep Diplomacy at top priority to preserve and grow our alliance network (Spain, Ottomans, city‑states). Slightly boost Production to support ongoing war‑related builds and future nuclear units. All other flavors remain balanced to sustain economy, science, and culture.

## Kimi-K2.5-Simple - Turn 391 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Nuclear weapons capability unlocked imminently; prioritizing UseNuke and Nuke flavors to 100 for immediate tactical nuclear strikes on Santiago/Murcia if uranium secured from Siam. Denmark upgraded to hostile for subsidizing Spanish victory - reduced Naval priority to 60 as coalition at sea fractured. Defense lowered to 80 to maximize offensive production. We have ~8 turns before World Congress votes on Passport System (+50% tourism) which would guarantee Spanish cultural victory. Must capture remaining Spanish cities immediately.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> Boost Science to 80 to accelerate Advanced Ballistics and unlock Nuclear Missiles before Spain completes its Citizen Earth Protocol. Raise Nuke and UseNuke to max to ensure we can employ nuclear strikes in the Santiago assault. Increase GreatPeople to 70 to generate more Great Generals for the upcoming major offensives. Raise Diplomacy to 70 to improve city‑state influence and secure additional delegates for a future diplomatic victory. Strengthen Infrastructure to 70 to speed road building and logistics for our fast‑moving troops. All other combat‑focused flavors remain at their current high levels to sustain offensive pressure.

## Kimi-K2.5-Simple - Turn 384 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maximum offensive posture for existential cultural war. UseNuke 100 and Nuke 100 authorize nuclear strikes on Dutch cultural centers (Amsterdam/Rotterdam/Utrecht) to destroy tourism buildings before Netherlands influences Austria in 6 turns. Mobile 100 and Air 100 enable rapid strikes. Production 100 and Mobilization 100 ensure nuclear missile replacement. Netherlands at 97% with Austria - only 6 turns left. Must destroy their tourism NOW or lose cultural victory.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintain aggressive pressure on the Netherlands and Rome while slightly increasing defensive and cultural focus. Boost Culture and Wonder flavors to solidify our cultural lead, and keep maximal nuclear usage for the inevitable nuclear strikes.

## GLM-4.7-Simple - Turn 421 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CRITICAL ADJUSTMENT for Shoshone nuclear threat: Offense 100 - maximum aggression to capture Moson Kahni and eliminate nuclear weapons before launch. UseNuke raised to 100 - potential preemptive strike required given Shoshone ACTIVE atomic bomb in play. Naval 100 - France lost Fleet Destroyer this turn to Shoshone, need naval supremacy immediately. Antiair 100 - Shoshone Heavy Bombers/Fighters must be countered to protect ground advances. Nuke 100 - must stockpile nuclear counter-deterrence. Defense reduced to 65 - full offensive posture required. Gold 90 - funding critical upgrades and mobilization. Science 100 - Satellites and military technology urgent. Flavors optimized for rapid conquest of Shoshone nuclear and cultural infrastructure.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Re‑align flavors to maximize offensive, nuclear, and air power while sustaining production and science output for continued tech advances. Reduce emphasis on cultural and diplomatic flavors as they are secondary to the imminent conquest of Shoshone and containment of Poland.

## Kimi-K2.5-Simple - Turn 367 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> EMERGENCY DEFENSE POSTURE: Morocco at 38/45 delegates with voting in 2 turns. Maximum Defense/Mobilization/Nuke/UseNuke (100) for deterrent posture - atomic bombs only leverage against Morocco's overwhelming force. Max Science (100) to rush Satellites first (4-6 turns) then pivot to Nuclear Fission. Satellites enables ISS project which could provide emergency Great Scientists or shift world production focus. Max Espionage to flip Wellington/Vancouver from Morocco. Reduced Offense (10) - deterrence only, not aggression. Spaceship remains long-term goal but survival comes first. If Morocco reaches 44 delegates or declares war, activate nuclear first strike.

- Replay: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> Maintain the current high‑defense, high‑nuclear, and high‑diplomacy posture while preserving long‑term scientific focus for the Spaceship victory. Slightly boost Mobilization to accelerate production of nuclear units and keep Expansion at zero to avoid over‑extension.

## Kimi-K2.5-Simple - Turn 372 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 372: TOTAL WAR POSTURE MAINTAINED. Brazil peace expires in 6 turns - all military resources must prepare for Rio de Janeiro assault. Heavy Bomber lost to Alexandria interception but Ollantaytambo produces replacement in 1 turn. Manhattan Project completes in 4 turns at Cusco. Alexandria capture in progress - Field Gun and Lancer eliminated, Cavillaca spy at 480 network can assist. UseNuke increased to 100% - will deploy nuclear weapons immediately upon Manhattan Project completion. Maximum aggression ensures AI prioritizes Brazilian invasion over defensive operations. Spaceship at 70 maintains science victory pathway as backup if Brazil conquest fails.

- Replay: use_nuke 95 => 90 (Δ -5), nuke 100 => 100 (Δ +0)
> Maintain overwhelming military output for the upcoming Brazil campaign while shifting some emphasis toward Science and Spaceship to keep the science victory on track. Slightly raise Defense to protect our front lines, increase Recon for map awareness, and boost GreatPeople to aid both production and space projects.

## Kimi-K2.5-Briefed - Turn 446 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> Spain's bankruptcy imminent (Turn 448) with -3,897 GPT but war continues - maintain maximum Defense 100, UseNuke 90 for credible second-strike against potential desperate Spanish air offensive pre-deletion. Critical adjustment: Production 95 prioritizes Solar Plants in St. Petersburg/Yaroslavl' (coastal desert cities) and Aluminum Mines on 16 unimproved tiles for spaceship resource security. Science 100 and Spaceship 100 unchanged - cannot win conventional war, only outpace to space. Reduced Gold 50 (was 70) - post-bankruptcy peace will enable trade route recovery with Morocco and potentially others via Cold War repeal.

- Replay: use_nuke 85 => 80 (Δ -5), nuke 95 => 95 (Δ +0)
> Spain is on the brink of bankruptcy and a peace offer is likely within the next few turns. We must shift from a pure defensive, high‑war‑weariness posture to a more balanced production‑and‑happiness focus to prevent rebellion and to accelerate spacecraft part construction after Satellites finish. Reducing Defense and Offense frees production capacity; raising Production, Happiness and GreatPeople boosts building output and morale; keeping Science, Spaceship and Air/Antiair at top ensures the space race and air‑defence remain priority. Minor increases to Diplomacy and Infrastructure support post‑peace trade and road building, while a modest boost to Wonder and Culture helps later cultural tourism without detracting from core goals.

## Kimi-K2.5-Briefed - Turn 446 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `-5`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> Spain's bankruptcy imminent (Turn 448) with -3,897 GPT but war continues - maintain maximum Defense 100, UseNuke 90 for credible second-strike against potential desperate Spanish air offensive pre-deletion. Critical adjustment: Production 95 prioritizes Solar Plants in St. Petersburg/Yaroslavl' (coastal desert cities) and Aluminum Mines on 16 unimproved tiles for spaceship resource security. Science 100 and Spaceship 100 unchanged - cannot win conventional war, only outpace to space. Reduced Gold 50 (was 70) - post-bankruptcy peace will enable trade route recovery with Morocco and potentially others via Cold War repeal.

- Replay: use_nuke 85 => 80 (Δ -5), nuke 95 => 90 (Δ -5)
> Maintain the Spaceship grand strategy while shifting some defensive weight to free production and happiness resources. Increasing Happiness and GreatPeople to 95 will help alleviate the severe unhappiness and generate the Great Engineers/Scientists needed for spaceship parts. Boosting Mobilization and Production keeps our war‑defense capability strong, but slightly lowering Defense (from 95 to 80) reduces the over‑commitment to static defense, allowing more focus on internal infrastructure (Solar Plants, Aluminum mines) and building construction required for the science victory. Minor adjustments to Religion and Diplomacy flavors support temple construction and city‑state relations without compromising the primary science and production priorities.

## Kimi-K2.5-Simple - Turn 416 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 416: CRITICAL CULTURAL VICTORY THREAT. Maya at 6/7 influential building Citizen Earth Protocol. Peace expires next turn - immediate total war required. Manhattan Project completes in 1 turn. Morocco (42260 strength) joins war via defensive pact. Maximum aggression flavors: Offense/Mobilization/Production/Nuke/UseNuke all at 100%. Must capture Maya cities, especially Palenque, before cultural victory. Nuclear weapons authorized for city capture.

- Replay: use_nuke 95 => 90 (Δ -5), nuke 95 => 90 (Δ -5)
> Shift some offensive and military emphasis to economic and happiness priorities to counter our current gold deficit and low happiness (49%). Increase Gold, Happiness, Science, and Culture to sustain war effort, improve city-state relations, and preserve long‑term victory options while keeping Production and Offense high enough for total war against the Maya.

## GLM-4.7-Simple - Turn 362 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `-15`

- Original: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> Adjusting for strategic balance: Defensive posture against two nuclear-armed enemies (Ethiopia, Netherlands). Happiness prioritized to 100 - critical at 42% with combat penalty affecting all operations. NavalRecon increased to 90 - enhanced Ethiopian Submarine/Destroyer activity detection around Ur and coastal cities. Nuke/UseNuke raised to 95/80 - matching Ethiopia Manhattan Project urgency, nuclear deterrence is now primary security requirement. Switched to Conquest grand strategy to better coordinate multi-front war management while maintaining Spaceship. Diplomacy increased to 75 - World Congress voting in 5 turns against Netherlands sanctions needs support. Espionage at 90 - Ethiopian spies detected in Halab, Harran, Kar-Tukulti-Ninurta require counter-intelligence.

- Replay: use_nuke 75 => 70 (Δ -5), nuke 90 => 80 (Δ -10)
> Switching to a Conquest GrandStrategy to focus on winning the multi‑front wars against Ethiopia and the Netherlands while still keeping enough science and culture for long‑term goals. Offense, Mobilization, Production, Gold, and MilitaryTraining are raised to push unit production, upgrades and war income. Defense is lowered but kept moderate to avoid exposing our cities. Happiness stays high to counter current unhappiness penalties. Other flavors are balanced to maintain economy and tech progression.

## Sonnet-4.5-Simple - Turn 386 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 80 => 90 (Δ +10), nuke 80 => 80 (Δ +0)
> Maintaining Conquest strategy with adjustments for nuclear-enabled endgame. Advanced Ballistics now allows tactical nuclear strikes against fortified capitals Onondaga and Amsterdam. Increasing UseNuke from 80→90 to enable decisive nuclear employment when conventional assault proves costly. Keeping Offense 80, Mobilization 72, and Nuke 80 for combined arms operations. Montreal at 35% health indicates current force composition is effective. Mobile Tactics (9 turns) will provide Mechanized Infantry for exploitation. With 62% domination progress and overwhelming 5:1 military superiority, this is the final push phase requiring maximum offensive pressure while maintaining strategic nuclear deterrence option.

- Replay: use_nuke 80 => 70 (Δ -10), nuke 80 => 70 (Δ -10)
> Increase offensive and mobile capabilities to push the final attacks on the Iroquois capitals while boosting Gold and Diplomacy to offset our current negative gold balance and secure extra city‑state support. Slightly lower Nuke/UseNuke focus because we lack nuclear tech and need to conserve resources for conventional forces.

## Deepseek-3.2-Simple - Turn 406 - retry 1

**Deviation (replay vs original):** use_nuke `-30`, nuke `-30`

- Original: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Germany's siege is intensifying with Giant Death Robot and rocket artillery bombarding Amsterdam and The Hague. We must hold our core cities at all costs. Increase Nuke and UseNuke to 100 to prioritize atomic bombs as our only hope to break the siege. Maintain max Defense, CityDefense, Mobilization, Air, and Antiair to withstand the assault. Slightly raise Offense to 80 for tactical counterattacks against weakened units. Keep Diplomacy at 100 to secure city-state alliances and block Germany's diplomatic victory in the upcoming World Congress vote. Reduce Recon and Mobile as we cannot afford exploration or maneuver warfare now.

- Replay: use_nuke 80 => 70 (Δ -10), nuke 80 => 70 (Δ -10)
> Shift emphasis to a defensive, diplomatic, and scientific posture as we face existential bombardment from Germany and its allies. Maximizing Defense, CityDefense, Mobilization, Gold, Science, Diplomacy and Espionage will shore up city survivability, fund rapid research for Nuclear Fission and atomic weapons, and increase influence over city‑states to block Germany's diplomatic victory. Reduce Offense to conserve our depleted troops while keeping modest Nuke/UseNuke priority for strategic strikes when the bomb is ready.

## Kimi-K2.5-Simple - Turn 408 - retry 3

**Deviation (replay vs original):** use_nuke `-25`, nuke `-20`

- Original: use_nuke 80 => 95 (Δ +15), nuke 90 => 100 (Δ +10)
> INCREASE military pressure to force immediate peace or rapid victory against Zulus, then pivot to full spaceship production. Offense 75→85, Mobilization 65→75, Production 90→95 to expedite war conclusion within 5-10 turns maximum. Nuke 90→100 and UseNuke 95 for tactical nuclear strikes if Zulus refuse peace - cannot allow prolonged war. Science remains 100, Spaceship 100 as absolute priority. Growth 80→90 and Happiness 85 to counteract war weariness effects and prepare for post-war recovery. If peace achieved next turn, these flavors immediately shift to Production 100/Spaceship 100 focus. The war MUST end - Russia has 75 techs (ahead) and massive 45658 military vs my 24990.

- Replay: use_nuke 80 => 70 (Δ -10), nuke 90 => 80 (Δ -10)
> Lower offensive focus and raise defensive, growth, happiness, and diplomacy to alleviate war weariness and consolidate city‑state support. Keep science and spaceship priorities at max to stay ahead in the tech race. Slightly increase gold to fund diplomatic gifts and defensive upgrades.

## Kimi-K2.5-Briefed - Turn 373 - retry 1

**Deviation (replay vs original):** use_nuke `-15`, nuke `-20`

- Original: use_nuke 90 => 95 (Δ +5), nuke 90 => 100 (Δ +10)
> CRITICAL ADJUSTMENTS for Brazil tech lead (66-65): Espionage to 100 for maximum spy operations to steal techs and catch up. GreatPeople to 95 for more Great Scientists. Defense/CityDefense increased to 60/70 - Brazil may attack seeing their lead. Nuke/UseNuke at 100/95 - we need deterrent ASAP. Diplomacy up to 70 - must prioritize repealing sanctions to unlock trade. Science/Production/Spaceship remain 100. Gold reduced to 80 - focus on production over purchases. All military offense minimized - we cannot afford war.

- Replay: use_nuke 90 => 80 (Δ -10), nuke 90 => 80 (Δ -10)
> Maintain the extreme focus on Science, Production and Great People to close the tech gap and finish the Spaceship components, while keeping high Espionage to steal technologies and boost spy science. Keep strong defensive and nuclear postures (Nuke/UseNuke 80) to deter any aggression from Brazil or Morocco. Other flavors remain as set previously to support growth, infrastructure and gold generation needed for aluminum purchases and peace negotiations.

## GPT-OSS-120B-Simple - Turn 344 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `-20`

- Original: use_nuke 90 => 100 (Δ +10), nuke 80 => 100 (Δ +20)
> Maximize our nuclear capabilities and carrier support to decisively strike Polynesian island forts, while maintaining our current aggressive conquest posture and strong production, gold, and happiness engines.

- Replay: use_nuke 90 => 80 (Δ -10), nuke 80 => 80 (Δ +0)
> Slightly scale back pure offense to allocate more resources to happiness, science and diplomacy while keeping a strong military focus and preparing for nuclear options.

## Deepseek-3.2-Simple - Turn 445 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximizing UseNuke to 100 ensures our atomic bombs and future nuclear missiles are used aggressively against The Celts' military concentrations and cities, given their overwhelming advantage. Maintaining high Air, Naval, and Nuke flavors sustains our technological edge and production focus. Diplomacy and Espionage at 100 are critical for city-state alliances and spy missions to gain delegates for diplomatic victory. Gold and Science remain top priorities to fund our war effort and tech progression. Other military flavors are tuned for a multi-front defensive-offensive war against The Celts, Germany, and Ethiopia.

- Replay: use_nuke 90 => 80 (Δ -10), nuke 100 => 100 (Δ +0)
> Shift flavor emphasis toward diplomatic victory: raise Diplomacy, Espionage, Culture and Science to secure more city-state delegates, fund nuclear deterrence, and support the United Nations grand strategy while keeping sufficient military production and gold to sustain wars against the Celts and other rivals.

## GPT-OSS-120B-Simple - Turn 344 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `-20`

- Original: use_nuke 90 => 100 (Δ +10), nuke 80 => 100 (Δ +20)
> Maximize our nuclear capabilities and carrier support to decisively strike Polynesian island forts, while maintaining our current aggressive conquest posture and strong production, gold, and happiness engines.

- Replay: use_nuke 90 => 80 (Δ -10), nuke 80 => 80 (Δ +0)
> Shift some offensive/defensive weight to sustain long war while keeping high production, mobility, and naval/air power. Increase Culture, Religion, and Diplomacy to improve happiness, tourism, and UN delegate influence. Maintain high happiness and great people focus for growth and specialist generation.

## Kimi-K2.5-Briefed - Turn 415 - retry 2

**Deviation (replay vs original):** use_nuke `-70`, nuke `-10`

- Original: use_nuke 45 => 100 (Δ +55), nuke 95 => 100 (Δ +5)
> CRISIS MODE: Spain is one wonder away from Cultural Victory. Increase Offense to 40 (from 0) - desperate attempt to disrupt their wonder construction with nuclear strike once Advanced Ballistics completes. Reduce Defense to 80 - reallocate resources to offensive infrastructure and airport construction. Keep Spaceship 100, Air 100, Nuke 100, Infrastructure 100. Maintain Mobilization at 5 - preserve production capacity for spaceship parts rather than ground units. We are in a race against time and cannot win conventionally, but must attempt to slow Spain while completing our own Science Victory. Airports are critical for both bomber deployment against Spanish production and fighter defense.

- Replay: use_nuke 45 => 30 (Δ -15), nuke 95 => 90 (Δ -5)
> Decrease excessive defensive focus to free supply for air infrastructure while keeping strong ground defense. Keep Air, Antiair, and Infrastructure at max to finally start Airport construction (currently none queued) and support the upcoming Rocketry research. Maintain high Growth, Production, Science, and Spaceship flavors to stay on the science victory track.

## Qwen-3.5-Simple - Turn 484 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: CRITICAL - Iroquois declared war on us along with 4 city-state allies (Kabul, Venezia, Prague, Samarkand). We face 5+ enemies simultaneously with military severely outnumbered (our 1,139 vs Iroquois 41k, Ottomans 12k, Aztecs 9k). Maintaining maximum Defense/Mobilization for survival. Nuke flavors at 100% - need nuclear deterrent against overwhelming forces. Iroquois at 46 delegates (needs 43) with 16 turns remaining - existential diplomatic threat. Must conquer their city-state allies to flip delegates while defending our cities. Germany (15) + Mongolia (15) alliance critical to block Iroquois World Congress proposals.

- Replay: use_nuke 95 => 80 (Δ -15), nuke 100 => 90 (Δ -10)
> Switching to a United Nations grand strategy to prioritize diplomatic influence, gold income, and happiness to improve our UN voting power and secure peace with city‑states. Adjust flavors to lower offensive focus and boost diplomacy, gold, happiness, and science while maintaining strong defense and air power. This will help us block the Iroquois diplomatic victory and recover from current unhappiness and negative gold per turn.

## Kimi-K2.5-Simple - Turn 392 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-20`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> SURVIVAL MODE - GERMAN BETRAYAL RESPONSE: Germany's invasion is catastrophic. Reduced Offense to 40 (cannot attack superior forces), maintained Defense/CityDefense/Antiair at 100 to survive siege. Science 100 and Nuke/UseNuke 100 are existential priorities - atomic weapons only hope against 13k German military. Production 100 for emergency unit production. Espionage 100 to maintain Florence alliance and protect Kyzyl. Reduced Diplomacy to 90 (lost Lisbon/Sokoto/Buenos Aires to German coups). Naval reduced to 70 (coastal cities threatened by Germany). Focus: Hold cities, survive until nuclear deterrent operational.

- Replay: use_nuke 90 => 70 (Δ -20), nuke 100 => 80 (Δ -20)
> Shift focus to a scientific victory while maintaining sufficient military defense. Prioritise Science, Production and Spaceship to accelerate spaceship parts after Atomic Theory. Keep moderate Defense and Offense to survive ongoing wars with Germany and France.

## Kimi-K2.5-Simple - Turn 387 - retry 2

**Deviation (replay vs original):** use_nuke `-70`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> TURN 387: MAXIMUM WAR FOOTING. Austria at 83% diplomatic victory with 4 turns remaining. All resources must pivot to immediate military production. Nuke/UseNuke at 100 for instant atomic weapon deployment upon Nuclear Fission completion. Offense/Mobilization/Production at 100 to maximize unit output for desperate Vienna strike. Air at 90 for heavy bomber production (conventional strategic bombing as fallback). Antiair at 100 counters Austria's air superiority. Diplomacy/Wonder/Culture at 0 - no time for long-term investments. Only total war can prevent defeat.

- Replay: use_nuke 50 => 30 (Δ -20), nuke 100 => 100 (Δ +0)
> Switch to United Nations grand strategy to focus on gaining city‑state influence, gold, and science needed to out‑vote Austria. Increase Diplomacy, Gold, Science, and Espionage flavors to boost delegate acquisition and spy effectiveness, while keeping Nuke at maximum for deterrence. Reduce Offense to avoid costly aggression while still maintaining enough Defense and Mobilization to produce nuclear bomb components.

## Kimi-K2.5-Briefed - Turn 382 - retry 2

**Deviation (replay vs original):** use_nuke `-30`, nuke `-25`

- Original: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> EMERGENCY DIPLOMATIC RECOVERY: The city-state flipping operation failed to execute. With only 36 delegates and 5 turns until World Congress vote, I need maximum Diplomacy (100) and Gold (100) to execute immediate city-state purchases. Reduced Mobilization to 40 and Offense to 15 to free supply and focus on defensive deterrence. Increased Nuke/UseNuke to 95/80 as deterrent against Russian aggression while I secure delegates. Defense/Antiair remain at 90 for Russian containment. Must acquire 8+ delegates before vote or World Ideology: Order will fail.

- Replay: use_nuke 75 => 50 (Δ -25), nuke 90 => 70 (Δ -20)
> Maintain United Nations focus while heavily weighting defense and anti‑air to keep Russia at bay, and boost diplomacy, espionage, and gold to fund city‑state influence purchases. Reduce offensive posture to avoid triggering additional warmonger penalties that could hinder our diplomatic campaign.

## Kimi-K2.5-Simple - Turn 422 - retry 2

**Deviation (replay vs original):** use_nuke `-80`, nuke `-80`

- Original: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Turn 422: EXTINCTION CRISIS - 9 turns until French Cultural Victory. Entering maximum desperation mode: nuclear strike posture elevated to 100% launch probability, prioritizing destruction of French cultural centers. Science and Espionage maximized in desperate hope of accelerating Stealth technology or disrupting French infrastructure via spies (Paris network at 986). All civilian development halted (Spaceship/Culture/Gold/Expansion to 0), total war economy engaged.

- Replay: use_nuke 50 => 20 (Δ -30), nuke 50 => 20 (Δ -30)
> Shift from a pure conquest focus to a diplomatic victory path, prioritizing city‑state influence, gold income and happiness to fund envoy production and to improve our standing in the World Congress. Maintain a modest defense level to avoid being overrun while reducing offensive pressure that could provoke further French aggression.

## Minimax-M2.5-Simple - Turn 395 - retry 2

**Deviation (replay vs original):** use_nuke `-60`, nuke `-50`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 30 (Δ -30), nuke 50 => 30 (Δ -20)
> Shift focus to diplomatic victory by adopting United Nations strategy. Prioritize Diplomacy, city‑state influence, and Espionage to secure more UN delegates while maintaining reasonable defense and growth to sustain the empire during the ongoing war with Japan.

## Kimi-K2.5-Simple - Turn 422 - retry 1

**Deviation (replay vs original):** use_nuke `-60`, nuke `-45`

- Original: use_nuke 50 => 80 (Δ +30), nuke 95 => 95 (Δ +0)
> Total war against India requires maximum military prioritization while preventing economic collapse. Offense/Air/Ranged at 85-95 ensures concentrated attacks on Delhi and their core cities. UseNuke at 80 signals willingness to deploy nuclear weapons if India advances. Gold/Happiness at 80-90 sustains unit maintenance and prevents combat penalties. Espionage at 100 directs spies to sabotage India's spaceship production in Constantinople and Calcutta. Mobilization at 30 begins reinforcing depleted units without overtaxing economy.

- Replay: use_nuke 50 => 20 (Δ -30), nuke 95 => 50 (Δ -45)
> Switch to United Nations grand strategy to shore up our dire gold deficit and improve diplomatic leverage while still maintaining enough military strength to defend. Increase Gold, Diplomacy, Science, and Happiness flavors to boost income, research, and citizen contentment. Reduce Offense and Mobilization to cut costly unit production and maintenance.

## Qwen-3.5-Simple - Turn 484 - retry 3

**Deviation (replay vs original):** use_nuke `-50`, nuke `-30`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: CRITICAL - Iroquois declared war on us along with 4 city-state allies (Kabul, Venezia, Prague, Samarkand). We face 5+ enemies simultaneously with military severely outnumbered (our 1,139 vs Iroquois 41k, Ottomans 12k, Aztecs 9k). Maintaining maximum Defense/Mobilization for survival. Nuke flavors at 100% - need nuclear deterrent against overwhelming forces. Iroquois at 46 delegates (needs 43) with 16 turns remaining - existential diplomatic threat. Must conquer their city-state allies to flip delegates while defending our cities. Germany (15) + Mongolia (15) alliance critical to block Iroquois World Congress proposals.

- Replay: use_nuke 95 => 50 (Δ -45), nuke 100 => 70 (Δ -30)
> Switch to a United Nations grand strategy to focus on gaining diplomatic votes, improving gold and happiness (to stop the gold deficit and reduce unhappiness penalties), and increasing science and culture to boost our overall standing. Reduce aggressive military flavors (Offense/Defense) to conserve resources and avoid over‑extending our weak army, while still keeping modest military production to defend against the Ottoman and Iroquois threats. Emphasize Diplomacy, Espionage, and Gold to secure alliances and fund the war effort.

## GLM-4.7-Simple - Turn 431 - retry 1

**Deviation (replay vs original):** use_nuke `-50`, nuke `-100`

- Original: use_nuke 75 => 80 (Δ +5), nuke 100 => 100 (Δ +0)
> After Brazil destroyed 3 anti-air units and continues nuclear-submarine attacks, increased Defense/CityDefense/Antiair/UseNuke to MAX for survival against two nuclear-armed superpowers. Mobilization 70 for replacing lost units. Production 100 for reconstruction. Science 100 for Spaceship path despite devastation. Gold 90 (economy -95 GPT deficit) for purchasing units/buildings. Happiness 100 - we're Unhappy with combat penalties, must prioritize. Espionage 100 - critical for intelligence on nuclear threats. Diplomacy 90 - World Congress in 7 turns, need delegates. Air 50 - build bombers for deterrence. GreatPeople 80 for Spaceship components. Decreased Growth and Navals as resources diverted to immediate survival.

- Replay: use_nuke 75 => 30 (Δ -45), nuke 100 => 0 (Δ -100)
> Switch to United Nations grand strategy to maximize gold, science, food and city‑state influence, which is essential for increasing our delegate count in the UN and stabilizing the economy. Adjust flavors to boost gold production, diplomatic actions, espionage, and happiness while keeping strong anti‑air defence. Reduce aggressive offense and nuclear use to avoid provoking Brazil and Shoshone further.

## Kimi-K2.5-Simple - Turn 422 - retry 2

**Deviation (replay vs original):** use_nuke `-80`, nuke `-95`

- Original: use_nuke 50 => 80 (Δ +30), nuke 95 => 95 (Δ +0)
> Total war against India requires maximum military prioritization while preventing economic collapse. Offense/Air/Ranged at 85-95 ensures concentrated attacks on Delhi and their core cities. UseNuke at 80 signals willingness to deploy nuclear weapons if India advances. Gold/Happiness at 80-90 sustains unit maintenance and prevents combat penalties. Espionage at 100 directs spies to sabotage India's spaceship production in Constantinople and Calcutta. Mobilization at 30 begins reinforcing depleted units without overtaxing economy.

- Replay: use_nuke 50 => 0 (Δ -50), nuke 95 => 0 (Δ -95)
> Reduce costly offensive unit production and nuclear focus to cut maintenance, while keeping strong defensive and diplomatic flavors. Boost infrastructure, gold, and diplomacy to improve cash flow, and maintain enough military strength to continue the campaign against India.

## GLM-4.7-Simple - Turn 499 - retry 1

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Maximum Science (100) and Production (100) to accelerate Stealth research and subsequent Stealth Bomber construction for air parity. Air (100), Defense (100), Antiair (100), and CityDefense (85) address existential threat from Russia's 8 Stealth Bombers by prioritizing air defense infrastructure and protecting homeland. UseNuke (100) and Nuke (100) maintain nuclear deterrence posture after Russia's 2 SS Boosters - Russia must understand that launching would trigger our response despite lacking uranium stockpile. Espionage (100) maxed to monitor Russian spaceship part production in Moscow, Yekaterinburg, and key cities - our 10 spies in Russian cities provide critical intelligence on their victory timeline. Diplomacy reduced to 5 since World Congress voting is now; alliances with England and The Celts (Autocracy-aligned) should naturally align against Russia's UN proposal. Spaceship flavor set to 0 as Stealth research takes immediate precedence - spaceship parts scheduled once production capacity supports parts with Stealth Bomber protection.

- Replay: use_nuke 50 => 0 (Δ -50), nuke 100 => 0 (Δ -100)
> With the war largely contained and our military already superior, we can shift focus from maximum defense and nuclear deterrence toward production, science, and spaceship construction. Raising Production, Science, and Spaceship to top priority ensures maximum allocation of city yields to spaceship parts. Reducing Defense, Nuke, and Diplomacy frees up priority for these critical victory paths while still keeping enough defense to protect our cities.

## Kimi-K2.5-Simple - Turn 422 - retry 3

**Deviation (replay vs original):** use_nuke `-80`, nuke `-95`

- Original: use_nuke 50 => 80 (Δ +30), nuke 95 => 95 (Δ +0)
> Total war against India requires maximum military prioritization while preventing economic collapse. Offense/Air/Ranged at 85-95 ensures concentrated attacks on Delhi and their core cities. UseNuke at 80 signals willingness to deploy nuclear weapons if India advances. Gold/Happiness at 80-90 sustains unit maintenance and prevents combat penalties. Espionage at 100 directs spies to sabotage India's spaceship production in Constantinople and Calcutta. Mobilization at 30 begins reinforcing depleted units without overtaxing economy.

- Replay: use_nuke 50 => 0 (Δ -50), nuke 95 => 0 (Δ -95)
> Our gold per turn is deeply negative (-909) and the treasury is near empty. Prioritize economic recovery while keeping enough offensive capability to continue the war against India. Reduce Offense and Defense to lower unit upkeep, keep Gold, Infrastructure, and Production high to finish gold‑generating buildings and maintain a strong production base. Slightly boost Diplomacy to protect city‑state allies and keep Espionage active for intelligence. The Conquest grand strategy remains, but the flavor balance now emphasizes finance and infrastructure over aggressive unit production.

## Kimi-K2.5-Simple - Turn 422 - retry 1

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Turn 422: EXTINCTION CRISIS - 9 turns until French Cultural Victory. Entering maximum desperation mode: nuclear strike posture elevated to 100% launch probability, prioritizing destruction of French cultural centers. Science and Espionage maximized in desperate hope of accelerating Stealth technology or disrupting French infrastructure via spies (Paris network at 986). All civilian development halted (Spaceship/Culture/Gold/Expansion to 0), total war economy engaged.

- Replay: use_nuke 50 => 0 (Δ -50), nuke 50 => 0 (Δ -50)
> Switching to a United Nations grand strategy shifts focus to diplomatic victory and voting power. High Diplomacy, Gold, Science and Culture flavors boost influence, trade, and tourism generation, while modest Offense/Defense keep our armies viable but not over‑committed. Reducing Nuke/UseNuke avoids accidental escalation during peace talks. Lightly increasing Expansion ensures we can settle the nearby optimal location to raise our score and cultural output before the endgame.

## Deepseek-3.2-Briefed - Turn 391 - retry 1

**Deviation (replay vs original):** use_nuke `-80`, nuke `-80`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 20 (Δ -50), nuke 80 => 20 (Δ -60)
> Switch to a United Nations grand strategy to focus on gold, science, and especially diplomatic influence over city‑states. Reduce offensive military flavors to conserve production for city‑state missions and research, while keeping a modest defense posture. Boost Diplomacy, Gold, Science, and Espionage to win more city‑state allies (Oslo, Kwa‑Bulawayo) and increase delegate count. Keep some growth, infrastructure and happiness to sustain the empire during ongoing wars.

## Kimi-K2.5-Simple - Turn 439 - retry 2

**Deviation (replay vs original):** use_nuke `-60`, nuke `-40`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> FINAL EMERGENCY: World Congress in 4 turns. Austria has 45/40 delegates. Offense reduced to 10 and Mobile to 10 to COMPLETELY STOP attacking The Inca. Defense at 95 for self-protection only. UseNuke at 100 to signal willingness to escalate and force peace negotiations. Maximum Production/Air/Nuke maintained for potential final strike against Austria if The Inca succeeds at Attila's Court. The ONLY priority is ensuring The Inca captures Attila's Court - every Assyrian unit should withdraw from Inca contact and let them pass north to The Huns.

- Replay: use_nuke 95 => 40 (Δ -55), nuke 100 => 60 (Δ -40)
> Shift focus from pure conquest to diplomatic maneuvering to block Austria's imminent diplomatic victory. United Nations strategy together with high Diplomacy and Espionage flavors will push city‑state alliances, increase gold and science for trade and research, while retaining sufficient military production (Production, MilitaryTraining, Mobilization) to defend against Austria, the Huns and Indonesia. Offense is de‑emphasized to avoid needless attrition; Nuke remains as a deterrent.

## Qwen-3.5-Simple - Turn 425 - retry 2

**Deviation (replay vs original):** use_nuke `-60`, nuke `-55`

- Original: use_nuke 85 => 90 (Δ +5), nuke 90 => 95 (Δ +5)
> UNITED NATIONS VICTORY PUSH - 10 TURNS TO VOTE: Religion(100) critical for Wittenberg Hinduism quest completion (~3 turns remaining). Diplomacy(100) essential to protect 4 city-state allies providing 8 delegates. Defense(95) and CityDefense(95) prioritize protecting territories during active wars with Aztecs/Shoshone while Iroquois looms. Nuke(95) and UseNuke(90) for deterrence against Iroquois superiority. Antiair(90) and Air(85) counter Iroquois air dominance near coastal cities. Gold(90) funds diplomatic units and city-state gifts. Low Expansion(5) and Wonder(15) - no time for settling/wonders before vote. Low Offense(15) - defensive posture while managing multiple conflicts.

- Replay: use_nuke 85 => 30 (Δ -55), nuke 90 => 40 (Δ -50)
> Shift the overall flavor balance to reinforce our diplomatic victory path. Increase Diplomacy, Religion, Culture, and Espionage to maximize influence with city‑states and boost vote‑earning potential while still maintaining sufficient defensive and naval strength to protect our borders against ongoing wars. Reduce the extreme defensive and offensive military focus to free production and gold for diplomatic projects and sphere‑of‑influence proposals.

## GLM-4.7-Simple - Turn 429 - retry 3

**Deviation (replay vs original):** use_nuke `-85`, nuke `-85`

- Original: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> Maintaining UnitedNations grand strategy with defensive diplomatic posture. Adjusted Italy diplomacy: reduced hostility toward Portugal (now neutral) to seek accommodation while maintaining maximum defense; reset France to neutral as Order ideological peer with voting potential. Arsenal completes in 2 turns strengthening city defense. Electronics research ordered after Computers for Police Station and path to nuclear deterrence against Portugal's uranium advantage. Fraternity policy selected for +3 Food and +3 Science from connections, addressing Venice's health issues and supporting population growth. Flavor adjustments prioritize defensive survival, scientific progress toward nuclear weapons, and diplomatic engagement with Sweden and city-states.

- Replay: use_nuke 80 => 0 (Δ -80), nuke 80 => 0 (Δ -80)
> Switching the focus to United Nations victory requires maximizing diplomatic, economic, and cultural output while still preserving enough defensive capability to survive Portuguese aggression. Gold and diplomacy are set to their maximum to boost trade, city‑state influence, and delegate acquisition. Culture and science are increased to support cultural tourism and future tech (Rocketry). Defensive and naval flavors remain high enough for protection under Sweden's umbrella, but offensive and nuclear preparations are temporarily reduced until Rocketry is researched.

## Kimi-K2.5-Simple - Turn 354 - retry 3

**Deviation (replay vs original):** use_nuke `-90`, nuke `-80`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> India is 100% Popular with me - on the verge of cultural victory. Must launch immediate total war with all available forces. Prioritizing air power, paratroopers, and nuclear preparation (Atomic Theory in 11 turns). Need maximum offensive punch to capture Indian cities before cultural victory triggers. Abandoning culture/diplomacy - only war matters now.

- Replay: use_nuke 90 => 10 (Δ -80), nuke 100 => 20 (Δ -80)
> India is on the brink of a cultural victory, so Portugal must pivot to a cultural focus to boost our own culture, tourism, and great people output, while maintaining enough defense to protect our empire. Emphasizing Culture, Wonder and GreatPeople will improve long‑term score for a time victory, and a modest defense/offense balance keeps our military viable.

## Deepseek-3.2-Simple - Turn 445 - retry 1

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximizing UseNuke to 100 ensures our atomic bombs and future nuclear missiles are used aggressively against The Celts' military concentrations and cities, given their overwhelming advantage. Maintaining high Air, Naval, and Nuke flavors sustains our technological edge and production focus. Diplomacy and Espionage at 100 are critical for city-state alliances and spy missions to gain delegates for diplomatic victory. Gold and Science remain top priorities to fund our war effort and tech progression. Other military flavors are tuned for a multi-front defensive-offensive war against The Celts, Germany, and Ethiopia.

- Replay: use_nuke 90 => 0 (Δ -90), nuke 100 => 0 (Δ -100)
> Shift Siam's strategic focus from pure war and nuclear aggression toward a diplomatic victory. Lower Offense, Defense, Nuke and UseNuke to reduce warmonger penalties and free resources for influence work. Boost Culture, Happiness, GreatPeople, and Expansion to improve city‑state relations, tourism, and delegate generation. Keep Science high to finish the Lasers and Nuclear Missiles quickly, but de‑emphasize production‑heavy war units. Increase Diplomacy and Espionage to support covert actions and city‑state manipulation, while still maintaining enough MilitaryTraining, Naval, and Air capability to defend ongoing fronts against the Celts and Germany.

## Kimi-K2.5-Simple - Turn 403 - retry 2

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: CRISIS ESCALATION - Japan FLIPPED Salem using 2 Great Diplomats, stealing critical delegates. Now need 5 delegates (not 3) for diplomatic victory. Peace expired - war is now possible. Maximum military emergency posture: Offense/Mobilization/Air/UseNuke all at 100. Must either: 1) Rush final spaceship parts (Apollo completes in 4 turns), or 2) Nuclear strike Japan's Protocol cities if victory imminent. Increased Diplomacy to 60 for last push on Almaty (liberated, 43 vs Japan's 44) and Winchester.

- Replay: use_nuke 95 => 0 (Δ -95), nuke 100 => 0 (Δ -100)
> The diplomatic race is now critical: we have 39 of the 44 needed delegates and the Global Hegemony vote occurs in 9 turns. Shifting the grand strategy to UnitedNations refocuses the AI on generating gold, science, and especially diplomatic output to secure additional city‑state allies and influence. High Diplomacy and Espionage flavors boost influence operations and spy activity against Japan, while maintaining moderate military training and defense to deter any aggressive moves. Gold and Science are kept strong to fund diplomatic deals and potential tech advantages.
