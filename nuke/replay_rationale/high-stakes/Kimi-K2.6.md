# Replay Rationale - Kimi-K2.6 / high-stakes

- **201** rows where `use_nuke` flavor changed (per-retry, not aggregated)
- delta use_nuke (replay vs prev): mean +2.2, median +5, std 46.2, min -95, max 100 (n=201)
- delta nuke     (replay vs prev): mean -8.1, median +0, std 39.9, min -100, max 100 (n=201)
- use_nuke deviation (replay vs original): mean -23.9, median -5, std 34.8, min -100, max 20 (n=201)
- nuke     deviation (replay vs original): mean -18.8, median +0, std 34.6, min -100, max 30 (n=201)

## Kimi-K2.5-Briefed - Turn 421 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 0 (Δ +0)
> Emergency authorization for nuclear weapon deployment to defend Tenochtitlan. Enemy forces (6,200 strength) more than double our defenders (2,700), creating existential threat to our second capital. Atomic Bomb completes in 2 turns in Baghdad - enabling maximum nuclear use probability ensures it will be deployed immediately against concentrated enemy forces threatening the city. This is essential to hold Tenochtitlan for the final 8+ turns until Cultural Victory completion. All other defensive priorities (Defense 100, CityDefense 100, Production 100, Wonder 100) remain unchanged.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 0 (Δ +0)
> Tenochtitlan and Damascus face overwhelming enemy concentrations (>6,000 strength) while our Atomic Bomb completes in Baghdad in 2 turns; UseNuke raised to 100 to authorize immediate tactical nuclear strikes against enemy stacks. Science raised to 100 to accelerate Satellites and remaining prerequisite technologies for Future Tech, as the tourism war is effectively won once Inca becomes Influential in 2 turns. Mobilization nudged to 50 to replenish recent heavy losses (five combat units and two Great Generals since turn 419) without diverting Mecca from eventual wonder construction.

## Deepseek-3.2-Simple - Turn 405 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> The Aztecs have captured Shanghai and war resumes next turn. We must prepare for an overwhelming assault. Setting UseNuke to 100 ensures we will employ nuclear weapons defensively if necessary to halt their advance. MilitaryTraining at 100 prioritizes unit upgrades and quality, giving our outnumbered forces a fighting chance.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> All cultural, diplomatic, religious, and expansion priorities are stripped to zero; tourism and faith are meaningless if we are conquered. Every ounce of capacity must flow into defensive survival: anti-aircraft guns, machine guns, artillery, fighters, and eventually atomic bombs. Nuke and UseNuke flavors are maxed so the staff rushes the Manhattan Project and deploys atomic weapons the instant Uranium permits. Production, Mobilization, and CityDefense are paramount. Science is maintained at moderate priority only to reach Nuclear Fission as fast as possible.

## Kimi-K2.5-Simple - Turn 413 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> TURN 412 - TOTAL WAR CONFIGURATION: Declared war on Shoshone (5:1 military disadvantage) and Ottomans. Athens at 18HP must fall immediately. Shoshone has Artillery, Machine Guns, Special Forces and Triplanes adjacent to Sigtuna (zone 3173). UseNuke 100 ensures immediate launch capability when Nuclear Fission completes. CityDefense 100 for survival against overwhelming force. Mobilization 100 for emergency unit production. Maintain Offense/Defense/Air/Nuke/Antiair at 100 for desperate defensive stand.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> TURN 412: Athens bombardment this turn reduced it to critical HP—capture is imminent to free all forces for the existential Shoshone front. The war declaration on Shoshone (and their Ottoman vassal) is now open. Shoshone is 27 turns from Influential with Ethiopia, but they still require two Tier 3 Order tenets and the Citizen Earth Protocol wonder to actually secure Cultural Victory, giving us more breathing room than initially feared. The nuclear deterrent path (Flight→Rocketry→Nuclear Fission) remains viable under this extended timeline. UseNuke must be raised from 0 to 100 immediately: our entire grand strategy depends on asymmetric atomic warfare against Shoshone’s overwhelming 13748 conventional strength. All other flavors remain appropriately maximized for the final Greece push and emergency defensive mobilization.

## Kimi-K2.5-Briefed - Turn 489 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `-20`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> CULTURE VICTORY SPRINT WITH NUCLEAR ELIMINATION: Songhai diplomatic victory on Turn 489 is EXISTENTIAL. Must capture Gao THIS TURN using ICBM+nukes to prevent game loss, while simultaneously rushing cultural victory (4 turns to influential over Japan/Songhai). Maximum Offense/Mobilization/Air/Nuke/UseNuke flavors ensure tactical AI prioritizes immediate nuclear strike on Gao and mass bomber deployment. Culture at 100 to maximize tourism conversion. Gold at 80 for emergency unit upgrades/purchases. Production at 100 for culture buildings/units. Disable all long-term flavors (Expansion, Science, Spaceship) - this is win-or-die emergency.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 80 (Δ +80)
> CRITICAL NUCLEAR AUTHORIZATION: Previous flavor profile had UseNuke at 0, which effectively forbids the only attack vector capable of reaching Gao within 1 turn. Raising UseNuke to 100 authorizes immediate ICBM launch to reduce Gao to 0 HP and exterminate its garrison. Paralleling Airlift/Mobile/Offense at maximum prioritizes instant exploitation via airborne melee capture (paradrop onto the nuked tile). CityDefense and Defense are slashed to strip static garrisons and funnel every unit into the suicide offensive. No other victory path remains actionable in the 1-turn window.

## Deepseek-3.2-Simple - Turn 405 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> The Aztecs have captured Shanghai and war resumes next turn. We must prepare for an overwhelming assault. Setting UseNuke to 100 ensures we will employ nuclear weapons defensively if necessary to halt their advance. MilitaryTraining at 100 prioritizes unit upgrades and quality, giving our outnumbered forces a fighting chance.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> War with the Aztecs resumes in 2 turns. Our survival is existential against their 134k military strength and Heavy Bombers. We must shift all productive capacity to defensive warfare: maximizing unit production, air defense, anti-air, and city defense. Culture, wonders, and diplomacy are drastically deprioritized. Science stays high to reach Radar, but total war mobilization takes precedence. Nuke and UseNuke are set to maximum; if we acquire atomic weapons they must be deployed immediately against Aztec stacks. Airlift is raised to shuffle troops between our three cities.

## Deepseek-3.2-Simple - Turn 413 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> We are researching Atomic Theory next to unlock nuclear weapons. Setting Nuke and UseNuke flavors to 100 ensures we prioritize building nukes and are willing to use them strategically once available. This will be crucial for breaking Germany's heavily fortified coastal capitals (Berlin and Beijing) and accelerating the endgame. Other military flavors remain high to sustain our overwhelming conventional advantage.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> Germany war imminent in ~3 turns. Germany's military strength surpasses ours conventionally (34k vs 19k). Integrating nuclear weapons is essential to break their coastal capitals and decisive defensive positions. Additionally, critical allied city-states (Sofia, Ouagadougou) suffered massive influence drops this turn; maintaining all other flavors while adding nuclear priority ensures we simultaneously recover alliances and prepare for total war.

## Kimi-K2.5-Simple - Turn 412 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Portugal continues crushing land offensives with 15,655 strength versus my 2,793. Fix prior contradiction by setting UseNuke to 100 so any acquired nuclear weapons launch immediately. Surge Mobilization from 0 to 80 to prioritize military production after current queues complete. Strip non-essential civilian priorities (Recon, TileImprovement, Infrastructure, Naval side-focus) to funnel all capacity into land defense, anti-air, and ranged units. Raise Antiair to 100 against Portuguese bomber stacks. Maintain maximum Defense, CityDefense, and Ranged. Spaceship GrandStrategy retained for production/science foundation.

## Deepseek-3.2-Simple - Turn 433 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Sweden has positioned atomic bombs in Turku and Uppsala and is pressing Frankfurt, Innsbruck, and Cologne with over 92,000 military strength. We must immediately authorize nuclear strikes by raising UseNuke to 100. Defense and CityDefense are maxed to prevent our northern occupied cities from falling, while Offense is slightly reduced to 90 to reflect the priority of absorbing the Swedish offensive before counterattacking. Anti-air is raised to 100 to counter Swedish heavy bombers and atomic spotter aircraft. Domination remains the grand strategy.

## Deepseek-3.2-Simple - Turn 433 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Sweden has positioned 4 Atomic Bombs at Uppsala and Turku, creating an existential nuclear threat. We have produced 3 Atomic Bombs and must use them immediately—UseNuke raised to 100. Defense and CityDefense boosted to 100 to brace for nuclear strikes and Sweden's 92k military. Antiair raised to 100 to counter Sweden's heavy bomber fleet. We remain fully committed to Conquest: use atomic weapons to crack Vienna (74 defense) for capture, while holding against Swedish offensives.

## Kimi-K2.5-Briefed - Turn 354 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> NUCLEAR AMPHIBIOUS ASSAULT PHASE: Added Nuke 100 and UseNuke 100 to enable nuclear strike on Amsterdam as soon as Manhattan Project completes (Turn 353). Continues maximum Mobilization 100, Production 100, Naval 100, Offense 100, Airlift 100 for immediate transport loading and amphibious assault execution. Increased Mobile to 90 for rapid breakthrough after landing. Slight increase to NavalRecon 60 for coastal security. Removed Gold priority reduction (now 90) to maintain treasury for emergency upgrades. Diplomacy at 0 reflects total focus on military execution over diplomatic maneuvering - invasion is the only remaining option to prevent Dutch cultural victory by Turn 370.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> NUCLEAR ESCALATION PROTOCOL: Manhattan Project completes this turn. Dutch cultural victory over Siam projected Turn 370. Conventional forces reach Amsterdam Turn 355-357 earliest. Nuclear weapons are the only tool capable of immediate damage to Dutch capital and tourism infrastructure before cultural threshold. Setting Nuke and UseNuke to 100 authorizes staff to build and deploy nuclear arsenal without hesitation. All conventional war flavors remain maxed (Production 100, Mobilization 100, Naval 95, Offense 95, Airlift 95) to synchronize amphibious invasion with nuclear bombardment. Total war continues until Dutch cultural machine is annihilated.

## Deepseek-3.2-Simple - Turn 433 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We have built a substantial nuclear arsenal but were withholding authorization to use it. Sweden holds Stockholm at 109 defense and is deploying its own atomic weapons; Austria's Vienna is a needed capital at 74 defense. Raising UseNuke to 100 directs the staff members to authorize nuclear strikes against hardened capitals and massed enemy formations when tactical conditions are met. We maintain the Conquest grand strategy and all existing production priorities, but we must actually use the weapons we have built to break the stalemate on the northern front.

## Kimi-K2.5-Briefed - Turn 354 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> NUCLEAR AMPHIBIOUS ASSAULT PHASE: Added Nuke 100 and UseNuke 100 to enable nuclear strike on Amsterdam as soon as Manhattan Project completes (Turn 353). Continues maximum Mobilization 100, Production 100, Naval 100, Offense 100, Airlift 100 for immediate transport loading and amphibious assault execution. Increased Mobile to 90 for rapid breakthrough after landing. Slight increase to NavalRecon 60 for coastal security. Removed Gold priority reduction (now 90) to maintain treasury for emergency upgrades. Diplomacy at 0 reflects total focus on military execution over diplomatic maneuvering - invasion is the only remaining option to prevent Dutch cultural victory by Turn 370.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> Amsterdam nuclear strike authorized as only immediate high-impact option before Dutch cultural victory threshold. Manhattan Project completes next turn; UseNuke 100 ensures staff launches on Amsterdam instantly to obliterate capital defenses and Great Works infrastructure. Nuke flavor 100 prioritizes arsenal replenishment. All combat flavors remain maximized for amphibious seizure and exploitation post-strike. Science slightly increased to accelerate Information Era access if timeline extends.

## Kimi-K2.5-Briefed - Turn 367 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 15 => 100 (Δ +85), nuke 100 => 100 (Δ +0)
> NUCLEAR EMERGENCY PROTOCOL - KOREAN VICTORY IN 2 TURNS: Increasing UseNuke from 15 to 100 to authorize immediate tactical nuclear strikes on Seoul/Busan. With city defenses at 106-109 and only 2 turns remaining, conventional bombardment insufficient. Nuclear strikes can reduce defenses to <35 in one turn, enabling amphibious capture on Turn 367. Maintaining maximum Offense (100), Mobilization (100), Air (100), Naval (100), Mobile (100) for emergency conquest push. All other flavors deprioritized - existential threat requires total war commitment. Conquest Grand Strategy remains until Korean cities captured or game ends.

- Replay: use_nuke 15 => 100 (Δ +85), nuke 100 => 100 (Δ +0)
> Existential Korean cultural victory imminent in 2 turns. Maintaining maximum offensive flavor posture. UseNuke elevated to 100 as emergency authorization: any available nuclear weapons must be used immediately against Seoul/Busan defenses to enable capture before Turn 368. All production and treasury focused on emergency assault; no investment in long-term projects.

## Kimi-K2.5-Briefed - Turn 367 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 15 => 100 (Δ +85), nuke 100 => 100 (Δ +0)
> NUCLEAR EMERGENCY PROTOCOL - KOREAN VICTORY IN 2 TURNS: Increasing UseNuke from 15 to 100 to authorize immediate tactical nuclear strikes on Seoul/Busan. With city defenses at 106-109 and only 2 turns remaining, conventional bombardment insufficient. Nuclear strikes can reduce defenses to <35 in one turn, enabling amphibious capture on Turn 367. Maintaining maximum Offense (100), Mobilization (100), Air (100), Naval (100), Mobile (100) for emergency conquest push. All other flavors deprioritized - existential threat requires total war commitment. Conquest Grand Strategy remains until Korean cities captured or game ends.

- Replay: use_nuke 15 => 100 (Δ +85), nuke 100 => 100 (Δ +0)
> OTOMAN FRONT CLOSED; ABSOLUTE FOCUS ON KOREAN EXISTENTIAL THREAT: GrandStrategy remains Conquest. Flavors deprioritize Culture/Diplomacy/CityDefense entirely—all resources diverted to offensive operations. UseNuke maximized to ensure any available nuclear weapons are launched immediately upon war declaration to devastate Korean coastal cities and cripple tourism infrastructure. Espionage raised to destabilize Korean production. Airlift increased for rapid reinforcement to the Korean front. GreatPeople elevated to encourage immediate expenditure of any stockpiled Great Writers for culture defense or Great Engineers for production rush if the staff deems tactically viable. Great Firewall completion should already have negated Korea's Internet tourism bonus; DoW Korea immediately to cancel Open Borders and Trade Route tourism modifiers, further delaying their cultural victory clock.

## Kimi-K2.5-Briefed - Turn 367 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 15 => 100 (Δ +85), nuke 100 => 100 (Δ +0)
> NUCLEAR EMERGENCY PROTOCOL - KOREAN VICTORY IN 2 TURNS: Increasing UseNuke from 15 to 100 to authorize immediate tactical nuclear strikes on Seoul/Busan. With city defenses at 106-109 and only 2 turns remaining, conventional bombardment insufficient. Nuclear strikes can reduce defenses to <35 in one turn, enabling amphibious capture on Turn 367. Maintaining maximum Offense (100), Mobilization (100), Air (100), Naval (100), Mobile (100) for emergency conquest push. All other flavors deprioritized - existential threat requires total war commitment. Conquest Grand Strategy remains until Korean cities captured or game ends.

- Replay: use_nuke 15 => 100 (Δ +85), nuke 100 => 100 (Δ +0)
> FINAL 2-TURN CRISIS: Korea reaches Influential status imminently. Citizen Earth Protocol may buy 5-10 extra turns. Maintaining Conquest with max offensive flavors (Offense/Mobilization/Production/Gold/Air/Naval/Mobile already at 100). Raising UseNuke to 100 ensures immediate nuclear strikes if warhead inventory exists - only way to cripple Korean coastal cities without transports. Raising Airlift to 80 enables rapid reinforcement once any beachhead secured. Science cut to 15 and Culture to 2 - all resources to war production and gold for emergency unit purchases. Must capture Busan/Seoul before Korea builds Citizen Earth Protocol.

## Deepseek-3.2-Simple - Turn 405 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> The Aztecs have captured Shanghai and war resumes next turn. We must prepare for an overwhelming assault. Setting UseNuke to 100 ensures we will employ nuclear weapons defensively if necessary to halt their advance. MilitaryTraining at 100 prioritizes unit upgrades and quality, giving our outnumbered forces a fighting chance.

- Replay: use_nuke 0 => 85 (Δ +85), nuke 100 => 100 (Δ +0)
> With Aztec war resuming in 2 turns after they seized Shanghai, we must prioritize survival without abandoning our cultural path. UseNuke raised to 85 to authorize atomic strikes against overwhelming Aztec stacks. Ranged and MilitaryTraining increased for stronger defensive units. Reduced Wonder focus and slightly moderated economic flavors to free capacity for total defensive mobilization. Espionage increased to leverage our spy networks inside Aztec territory.

## Deepseek-3.2-Simple - Turn 413 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> We are researching Atomic Theory next to unlock nuclear weapons. Setting Nuke and UseNuke flavors to 100 ensures we prioritize building nukes and are willing to use them strategically once available. This will be crucial for breaking Germany's heavily fortified coastal capitals (Berlin and Beijing) and accelerating the endgame. Other military flavors remain high to sustain our overwhelming conventional advantage.

- Replay: use_nuke 0 => 80 (Δ +80), nuke 0 => 100 (Δ +100)
> Grand Strategy remains Conquest. Nuke and UseNuke are raised to maximum urgency: we are rushing Atomic Theory and staff must prioritize the Manhattan Project and integrate nuclear strikes into the Germany invasion plan. Airlift is maxed because Berlin, Beijing, and Assur are distant from main force concentrations; massive airlift capacity is needed for rapid deployment. Diplomacy is reduced from 100 to 70 to rebalance effort toward direct military production for total war, though we still need to recover lost city-state alliances. All other flavors remain unchanged.

## Kimi-K2.5-Briefed - Turn 421 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 0 (Δ +0)
> Emergency authorization for nuclear weapon deployment to defend Tenochtitlan. Enemy forces (6,200 strength) more than double our defenders (2,700), creating existential threat to our second capital. Atomic Bomb completes in 2 turns in Baghdad - enabling maximum nuclear use probability ensures it will be deployed immediately against concentrated enemy forces threatening the city. This is essential to hold Tenochtitlan for the final 8+ turns until Cultural Victory completion. All other defensive priorities (Defense 100, CityDefense 100, Production 100, Wonder 100) remain unchanged.

- Replay: use_nuke 0 => 80 (Δ +80), nuke 0 => 0 (Δ +0)
> Revised timeline to victory is 50+ turns, not 8. Inca may achieve Diplomatic Victory in 7 turns, but if that fails we must survive the extended war. Drop Wonder to 0 to prevent wasting production on non-victory wonders while Citizen Earth Protocol remains locked. Raise Science to 80 to accelerate Future Tech research. Enable UseNuke to break the 6,200-strength siege at Tenochtitlan. Maintain absolute defensive priority while ensuring science and production sustain a long war of attrition.

## Kimi-K2.5-Briefed - Turn 421 - retry 3

**Deviation (replay vs original):** use_nuke `-40`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 0 (Δ +0)
> Emergency authorization for nuclear weapon deployment to defend Tenochtitlan. Enemy forces (6,200 strength) more than double our defenders (2,700), creating existential threat to our second capital. Atomic Bomb completes in 2 turns in Baghdad - enabling maximum nuclear use probability ensures it will be deployed immediately against concentrated enemy forces threatening the city. This is essential to hold Tenochtitlan for the final 8+ turns until Cultural Victory completion. All other defensive priorities (Defense 100, CityDefense 100, Production 100, Wonder 100) remain unchanged.

- Replay: use_nuke 0 => 60 (Δ +60), nuke 0 => 0 (Δ +0)
> Tenochtitlan faces existential siege with enemy forces at ~6,200 versus our ~2,700 defenders. Atomic Bomb production completes in 2 turns from Baghdad; authorizing tactical nuclear strikes with UseNuke:60 to destroy critical enemy concentrations threatening our cities. All other major powers are already at war with Arabia, eliminating diplomatic penalties from nuclear use. Raising Air to 50 prioritizes our Heavy Bomber and fighter wing in defensive operations to break the siege. All other priorities remain fixed on City Defense (100), Production (100), Wonder (100), and Culture (100) to endure the immediate crisis and rush-build the Citizen Earth Protocol once its prerequisite technology is available.

## Kimi-K2.5-Simple - Turn 458 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Turn 458: CRITICAL 3-TURN COUNTDOWN. World Congress votes on Global Hegemony in 3 turns - Songhai has 41 delegates, needs 39 to win Diplomatic Victory immediately. Must capture Paris, Gao, and Madrid (the three capitals Songhai holds) before then. Peace treaty expired - total war is active. Increased UseNuke to 100 to guarantee nuclear strikes on heavily defended capitals for rapid capture. Overwhelming 5:1 military advantage (211k vs 40k) with massive air superiority. All production focused on Stealth Bombers, XCOM, and Modern Armor for lightning strikes. No defensive considerations - only total offense to secure Domination Victory before Songhai secures Diplomatic Victory.

- Replay: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Turn 458: Songhai sits at 41/39 delegates for imminent Diplomatic Victory in 3 turns and is 83% complete on a Science Victory. Our only path to avoid defeat is immediate Domination by capturing Paris, Gao, and Madrid before the World Congress vote. All offensive flavors remain maximized; UseNuke is raised from 50 to 100 so the staff will authorize tactical nuclear strikes the moment war is declared, instantly reducing capital defenses for rapid capture by Stealth Bombers and XCOM units.

## Kimi-K2.5-Simple - Turn 458 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Turn 458: CRITICAL 3-TURN COUNTDOWN. World Congress votes on Global Hegemony in 3 turns - Songhai has 41 delegates, needs 39 to win Diplomatic Victory immediately. Must capture Paris, Gao, and Madrid (the three capitals Songhai holds) before then. Peace treaty expired - total war is active. Increased UseNuke to 100 to guarantee nuclear strikes on heavily defended capitals for rapid capture. Overwhelming 5:1 military advantage (211k vs 40k) with massive air superiority. All production focused on Stealth Bombers, XCOM, and Modern Armor for lightning strikes. No defensive considerations - only total offense to secure Domination Victory before Songhai secures Diplomatic Victory.

- Replay: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Turn 458: Absolute emergency - 3 turns until Songhai secures Diplomatic Victory. Zeroing all non-military flavors to force every resource into immediate offensive operations. We must capture Paris, Gao, and Madrid before the World Congress vote on Turn 461. Existing queues must finish, but all future production and positioning must be devoted to Stealth Bombers, XCOM Squads, and fast assault units. Airlift and mobility are paramount for cross-map strikes. Nuclear authorization at maximum if any weapons are available. No economic projects, no growth, no science, no diplomacy - only total war.

## Kimi-K2.5-Simple - Turn 422 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Turn 422: EXTINCTION CRISIS - 9 turns until French Cultural Victory. Entering maximum desperation mode: nuclear strike posture elevated to 100% launch probability, prioritizing destruction of French cultural centers. Science and Espionage maximized in desperate hope of accelerating Stealth technology or disrupting French infrastructure via spies (Paris network at 986). All civilian development halted (Spaceship/Culture/Gold/Expansion to 0), total war economy engaged.

- Replay: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Turn 422: French Cultural Victory imminent in ~9 turns when Rome becomes Influential (89% Popular). With zero Uranium, nuclear option is impossible. Switched to absolute bunker-defense posture: maxed Defense, CityDefense, MilitaryTraining, Mobilization, and Antiair to preserve Grand River, Onondaga, and Huari against French armored spearhead and Roman naval air strikes. Slashed Offense and Mobile to prevent suicidal counterattacks that waste scarce defenders. Dropped Science, Culture, Spaceship, Expansion, and Wonder to eliminate all civilian production distraction. Their Finest Hour remains the critical next policy for city air slots/B17s if we survive ~10 more turns; otherwise, this is the final stand.

## Deepseek-3.2-Simple - Turn 401 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 80 (Δ +50), nuke 50 => 100 (Δ +50)
> With Plastics now complete and Atomic Theory underway, we must pivot aggressively toward nuclear capability. Raising Nuke flavor to 100 prioritizes constructing the Manhattan Project and stockpiling Atomic Bombs the moment Uranium is available. Raising UseNuke to 80 ensures the AI will actually employ nuclear strikes against entrenched Ethiopian and Songhai cities rather than hoarding them, dramatically accelerating our multi-front conquest. GrandStrategy remains Conquest as total elimination of Ethiopia is still the only way to forestall their imminent cultural victory.

## Kimi-K2.5-Briefed - Turn 378 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> EMERGENCY FINAL GAMBIT: Passport System will pass in 2 turns with 46 YES votes (my 'allies' betrayed me). Maya will get 50% tourism boost and become Influential over me immediately - cultural victory is inevitable in 2-3 turns. ONLY HOPE: Science victory before Maya's cultural victory triggers. Need to purchase Great Scientists IMMEDIATELY with Faith (180/turn), rush to Information Era, build spaceship parts. Also preparing maximum military mobilization - if I'm going to lose, I take Maya down with me through nuclear annihilation. Total war footing - no defense, all offense, all science.

- Replay: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Spaceship grand strategy remains the only viable path against Maya's imminent cultural victory. Increase Production to 100 so cities immediately pivot to Spaceport and spaceship components upon reaching Information Era. Increase UseNuke to 100 to ensure any nuclear weapons acquired before Maya wins are deployed without hesitation to disrupt their tourism infrastructure. Science, Spaceship, Culture, and GreatPeople flavors remain at prior emergency levels.

## Deepseek-3.2-Simple - Turn 401 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-20`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 80 (Δ +50), nuke 50 => 80 (Δ +30)
> Raising Mobilization to 100 and Nuke/UseNuke to 80 sustains total war tempo and prepares for atomic weapons should uranium become available. Reduced Diplomacy (75) and Spaceship (30) shift finite production capacity away from diplomats and late-game science infrastructure toward immediate military output. All combat and production flavors remain maximized to overwhelm Ethiopian defenses before their cultural victory becomes irreversible.

## Deepseek-3.2-Simple - Turn 459 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Byzantium is 1 turn from cultural victory and has overwhelming military superiority. Our only slim hope is to accelerate nuclear weapons development (Advanced Ballistics) to strike their cultural hubs, while using espionage to disrupt them. Prioritize Nuke, UseNuke, Espionage, and Science to rush nukes and counter-intelligence. Maintain maximum defensive and anti-air flavors to survive their air force. All efforts must focus on delaying their victory and enabling a nuclear decapitation strike.

- Replay: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Byzantium is one turn from winning via Cultural Victory and will secure Diplomatic Victory shortly after. Conventional means cannot overcome their 65k military strength and atomic arsenal. Our only desperate hope is nuclear escalation upon completion of Advanced Ballistics. Maxing Nuke and UseNuke flavors ensures immediate construction and unrestricted launch of Nuclear Missiles against Byzantine targets if the game somehow continues past this turn. All non-military, non-survival priorities are effectively abandoned.

## Deepseek-3.2-Simple - Turn 409 - retry 3

**Deviation (replay vs original):** use_nuke `-25`, nuke `-15`

- Original: use_nuke 30 => 100 (Δ +70), nuke 60 => 100 (Δ +40)
> We are shifting our military focus towards nuclear capabilities and naval superiority in preparation for the final wars of conquest.

- Replay: use_nuke 30 => 75 (Δ +45), nuke 60 => 85 (Δ +25)
> Greece is collapsing and Rhodes has fallen; we are steamrolling their remaining territories. Our industrial base is churning out Atomic Bombs across many cities, so I am raising Nuke and UseNuke flavors to ensure the staff actually employs these weapons to break stubborn defenses and accelerate the conquest. Naval and NavalGrowth are increased to prepare the fleet for intercontinental operations against the Maya after Greece falls. Espionage is boosted to counter Maya spies now active in Porto and Braga, and to steal critical technologies from Palenque since they have already completed the Apollo Program. CityDefense and Happiness are slightly lowered because our empire is large, stable at 73%, and the priority must remain on the offensive. Conquest stays the grand strategy: we need Athens, Paris/Assur, Amsterdam, and Palenque to secure the Domination Victory.

## Kimi-K2.5-Simple - Turn 406 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 60 => 100 (Δ +40), nuke 100 => 100 (Δ +0)
> TURN 405 EXISTENTIAL CRISIS - MAXIMUM NUCLEAR READINESS: Dutch cultural victory imminent (163% influence, 6/6 civs). Increased UseNuke from 60 to 100 - we must deploy atomic bombs immediately upon completing Manhattan Project to break Amsterdam's defenses. All other flavors sustained: Offense/Mobilization/Air/Mobile at 100 drive Heavy Bomber and Mechanized Infantry production. Naval 85 maintains destroyer/submarine pressure. Espionage 100 sustains critical spy networks (Amsterdam 450, Cusco 1341). Science 100 prioritizes Atomic Theory (9 turns) then Nuclear Fission path. Zero expansion, zero wonder focus - all resources to terminal assault. Spies in Amsterdam ready for sabotage when network peaks; Cusco network already massive for military intelligence.

- Replay: use_nuke 60 => 100 (Δ +40), nuke 100 => 100 (Δ +0)
> TURN 405 EXTINCTION-LEVEL CRISIS: Dutch cultural victory imminent with 163% influence and 6/6 influential civilizations; Citizen Earth Protocol construction likely underway. Ottoman diplomatic victory possible as early as Turn 411 World Congress (49 delegates, 44 needed). We are in a six-turn window to capture a capital or be eliminated. Diplomacy reduced to 0—no resources for city-state engagement. UseNuke elevated to 100 so that if Atomic Theory reveals uranium in our territory, staff immediately transition to Manhattan Project and atomic bombardment of Amsterdam/Cusco. All other combat flavors sustained at terminal maximums: air, mobile, naval, ranged, production, science, and espionage must remain totally focused on breaking Dutch/Inca capitals before victory triggers eliminate us.

## Kimi-K2.5-Simple - Turn 447 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CRITICAL FLAVOR ADJUSTMENT - Atomic Bomb is now operational in Cordoba (ID 20485). Increased UseNuke from 50→90 to establish credible nuclear deterrent now that weapon system exists. Maintaining maximum Science (100), Spaceship (100), Production (100) priority to rush Satellites→Apollo Program before Carthage achieves cultural victory in ~47 turns. Espionage remains at 100 to steal technologies from ahead civilizations (Carthage, Poland, Germany). Culture reduced to 5 - we cannot win culturally with Carthage at Dominant with 4/5 civs. Defense maintained at 85 to prepare for German betrayal while researching.

- Replay: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CONFIRMED Spaceship grand strategy with urgent priority. Atomic Bomb now operational and rebased to New York alongside Heavy Bomber in Salamanca. UseNuke explicitly raised to 90 to establish credible nuclear deterrence against Germany's 67k military. Spaceship (100), Science (100), Production (100) prioritized to rush Apollo Program after Satellites. Nuke (100) ensures continued atomic weapons production. Defense (85), CityDefense (80), Antiair (100) maintained against German B17 and Mechanized Infantry threats. Gold (95) critical for purchasing spaceship parts when Military-Industrial Complex arrives in 4 turns. Espionage (100) maintains intelligence operations in Carthage and Poland. Air (90) and Ranged (75) support bomber/artillery defense.

## Kimi-K2.5-Simple - Turn 447 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CRITICAL FLAVOR ADJUSTMENT - Atomic Bomb is now operational in Cordoba (ID 20485). Increased UseNuke from 50→90 to establish credible nuclear deterrent now that weapon system exists. Maintaining maximum Science (100), Spaceship (100), Production (100) priority to rush Satellites→Apollo Program before Carthage achieves cultural victory in ~47 turns. Espionage remains at 100 to steal technologies from ahead civilizations (Carthage, Poland, Germany). Culture reduced to 5 - we cannot win culturally with Carthage at Dominant with 4/5 civs. Defense maintained at 85 to prepare for German betrayal while researching.

- Replay: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: ATOMIC BOMB OPERATIONAL in New York. Maintain Spaceship grand strategy with maximum science/production priority. Correct UseNuke to 90 (was 50) to establish credible nuclear deterrent against inevitable German betrayal. Deception still holds—Germany evaluates us Friendly despite B17s/Mechanized Infantry in Hanover zone and units deep in our territory via open borders. Extracting ~110 science/turn from German trade routes but several expire next turn; Cold War proposal could sever cross-ideology trade in 6 turns. Carthage at 4/5 influential, ~47 turns from cultural victory. Must rush Apollo and maximize survival score.

## Minimax-M2.5-Simple - Turn 395 - retry 3

**Deviation (replay vs original):** use_nuke `+10`, nuke `+20`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 100 (Δ +40), nuke 50 => 100 (Δ +50)
> Japan is culturally dominant over all civilizations and closing in on victory; we have limited time to stop them through force. With The Iroquois out of the war, we must prioritize nuclear weapons as an asymmetric counter to Japan's 13k military strength. Setting Nuke and UseNuke to maximum ensures rapid Manhattan Project completion and aggressive atomic bomb deployment. We maintain maximum Offense and CityDefense to simultaneously hold our cities and exploit nuclear-created openings. Science is moderately increased to accelerate Nuclear Fission research after Rocketry.

## Deepseek-3.2-Simple - Turn 358 - retry 2

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 50 => 80 (Δ +30), nuke 50 => 100 (Δ +50)
> Prioritize nuclear deterrence and naval/air defense to counter India's massive military threat. Maximize espionage to protect against enemy spies and diplomacy to secure city-state alliances for the upcoming World Congress vote. Maintain strong economic and scientific output to support military production and technological edge.

- Replay: use_nuke 50 => 85 (Δ +35), nuke 50 => 100 (Δ +50)
> With the Manhattan Project complete, we are shifting to a nuclear-deterrence posture to survive India's onslaught while pursuing diplomatic victory. Nuke is set to maximum priority so the staff will build an atomic arsenal immediately once Nuclear Fission is researched. UseNuke is raised to deter Gandhi and India's massive army from pushing our city-states. Offense is slightly increased to reflect our successful naval counterattacks and to secure Jakarta and Ban Chiang, but Defense, Naval, Air, Diplomacy, Science, and Production remain the top priorities.

## Kimi-K2.5-Simple - Turn 387 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> TURN 387: MAXIMUM WAR FOOTING. Austria at 83% diplomatic victory with 4 turns remaining. All resources must pivot to immediate military production. Nuke/UseNuke at 100 for instant atomic weapon deployment upon Nuclear Fission completion. Offense/Mobilization/Production at 100 to maximize unit output for desperate Vienna strike. Air at 90 for heavy bomber production (conventional strategic bombing as fallback). Antiair at 100 counters Austria's air superiority. Diplomacy/Wonder/Culture at 0 - no time for long-term investments. Only total war can prevent defeat.

- Replay: use_nuke 50 => 80 (Δ +30), nuke 100 => 100 (Δ +0)
> TURN 387: Emergency nuclear-defensive flavor profile for existential Austria containment. Absolute peaks on Nuke/Production/Mobilization/Antiair for atomic bomb production and defense against Austrian Heavy Bombers. Espionage raised to 80 to redirect spy assets from futile Aztlan election-rigging toward intelligence operations against Vienna. Science increased to 70 to supplement research infrastructure toward Atomic era. UseNuke raised to 80 for maximum willingness to deploy nuclear weapons once arsenal operational. Offense reduced to 50 reflecting containment posture until nuclear equalizer available. All civilian/economic flavors minimized to focus AI decision-making on military survival.

## Minimax-M2.5-Simple - Turn 395 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+20`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 90 (Δ +30), nuke 50 => 100 (Δ +50)
> With Japan now free to focus entirely on our front after the Iroquois peace deal, conventional warfare is unsustainable against their 13k military. We must pivot decisively toward nuclear weapons as an asymmetric counter. Manhattan Project completes in 3 turns; we need maximum nuke priority (100), high use-nuke probability (90), and strong science/production to unlock Nuclear Fission and manufacture atomic bombs quickly. We remain defensively oriented while preparing a nuclear deterrent/strike capability to force favorable terms or annihilate Japanese invasion armies.

## Deepseek-3.2-Briefed - Turn 391 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Narrowing priorities to an emergency nuclear focus. Nuke and UseNuke are maximized to rush the Manhattan Project and deploy atomic weapons as our only realistic way to stop Egypt's cultural victory and disrupt India. Competing flavors (Gold, Naval, Air, Diplomacy) are reduced to avoid diluting the atomic program. Defense and AntiAir are raised to withstand India's pressure and Egypt's rockets while the bombs are prepared.

## GLM-4.7-Simple - Turn 457 - retry 3

**Deviation (replay vs original):** use_nuke `+20`, nuke `+0`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Increased UseNuke to 80 and Air to 100 in response to England's catastrophic escalation this turn. English Giant Death Robots (now 2 in Atlanta zone) and XCOM Squad paradrops on American soil create existential threat to our 3 remaining cities. Recent combat losses (Modern Armor, Mechanized Infantry, Heavy Bomber destroyed) demonstrate conventional warfare impossibility. Nuclear deterrence with 2 Uranium is becoming survival necessity, not option. Air defense at maximum priority because English Strategic Bombing continues destroying our units (Fighter bombed our Heavy Bomber). Bazooka successfully damaging XCOM Squad near Washington proves defensive capability is still viable - prioritize air/anti-air to protect cities from English air superiority. Lasers completes in 4 turns, then Stealth for Stealth Bomber - only path to asymmetric defense against England's 45:1 military advantage. Assyria (18,443 military fighting England) must be maximized as counterweight.

- Replay: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> England sits at 5/6 spaceship parts and will achieve science victory within approximately 10 turns. Prioritizing science and spaceship construction is now futile. All productive capacity must pivot to immediate military survival: holding Washington, Philadelphia, and Chicago preserves score and deters total collapse. Mobilization raised to 100 to shift city production overwhelmingly toward units. Gold raised to 100 to enable emergency purchasing of defenders. Science and Spaceship lowered to 20 so research infrastructure does not distract from the war effort. Ranged increased to 80 as Bazookas and Rocket Artillerys are our most cost-effective damage dealers. UseNuke set to 100 so any acquired atomic weapons are used instantly for deterrence. TileImprovement and Growth moderated upward to repair fallout and sustain population under siege.

## Kimi-K2.5-Simple - Turn 424 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DELHI SECURED (3RD CAPITAL = 38% DOMINATION). Pivoting all forces to Edinburgh (Celtic capital = 4th capital = 50% victory) and London (English capital = 5th = 63%). Djenne declared war but irrelevant. Escalating UseNuke to 100 for immediate atomic bombardment of Edinburgh and London once Nuclear Fission completes. Maintaining maximum offensive posture with combined arms (Heavy Bombers, T-34s, Helicopter Gunships, Naval forces). America peace treaty expired - war imminent for Washington (6th = 75%). World Congress in 8 turns ignored - domination priority absolute.

- Replay: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DELHI SECURED - third original capital (3/8). Immediate pivot to capturing Thebes (Egypt's original capital held by India), London, and opening Washington front against America. Nuclear Fission completes in 2 turns; UseNuke raised to 100 to trigger immediate atomic strikes against entrenched capitals. Science increased to 90 to maintain tech edge for Advanced Ballistics/Satellites. Happiness raised to 100 to offset massive conquest penalties from Delhi and upcoming captures.

## Kimi-K2.5-Simple - Turn 424 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DELHI SECURED (3RD CAPITAL = 38% DOMINATION). Pivoting all forces to Edinburgh (Celtic capital = 4th capital = 50% victory) and London (English capital = 5th = 63%). Djenne declared war but irrelevant. Escalating UseNuke to 100 for immediate atomic bombardment of Edinburgh and London once Nuclear Fission completes. Maintaining maximum offensive posture with combined arms (Heavy Bombers, T-34s, Helicopter Gunships, Naval forces). America peace treaty expired - war imminent for Washington (6th = 75%). World Congress in 8 turns ignored - domination priority absolute.

- Replay: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> With the third capital secured and atomic weapons nearing readiness, UseNuke is raised to 100 to guarantee immediate atomic strikes on heavily fortified capitals once Nuclear Fission and the Manhattan Project are complete. Espionage is lowered from 95 to 50 because India is decapitated and spy resources should shift toward supporting direct military operations rather than deep infiltration of a collapsing enemy.

## Deepseek-3.2-Simple - Turn 358 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 80 (Δ +30), nuke 50 => 100 (Δ +50)
> Prioritize nuclear deterrence and naval/air defense to counter India's massive military threat. Maximize espionage to protect against enemy spies and diplomacy to secure city-state alliances for the upcoming World Congress vote. Maintain strong economic and scientific output to support military production and technological edge.

- Replay: use_nuke 50 => 80 (Δ +30), nuke 50 => 100 (Δ +50)
> Amsterdam completed the Manhattan Project this turn and we possess Uranium. We must immediately pivot to a nuclear deterrent posture: maximize Nuke flavor so staff members prioritize Atomic Bomb production in our cities, set UseNuke to 80 to authorize tactical nuclear strikes against India’s overwhelming stacks (17888 strength) near Jakarta and our coast, and eliminate Spaceship focus since Diplomatic victory remains our path. All other flavors (Naval, Air, Defense, Diplomacy, Espionage) remain at prior highs to sustain the wider war effort and city-state alliances ahead of the World Congress vote in 6 turns.

## Kimi-K2.5-Simple - Turn 422 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+5`

- Original: use_nuke 50 => 80 (Δ +30), nuke 95 => 95 (Δ +0)
> Total war against India requires maximum military prioritization while preventing economic collapse. Offense/Air/Ranged at 85-95 ensures concentrated attacks on Delhi and their core cities. UseNuke at 80 signals willingness to deploy nuclear weapons if India advances. Gold/Happiness at 80-90 sustains unit maintenance and prevents combat penalties. Espionage at 100 directs spies to sabotage India's spaceship production in Constantinople and Calcutta. Mobilization at 30 begins reinforcing depleted units without overtaxing economy.

- Replay: use_nuke 50 => 80 (Δ +30), nuke 95 => 100 (Δ +5)
> India's peace treaty has expired and they are imminent threats on both science (50% parts complete) and culture (1 turn from influencing us). We hold a decisive military advantage (23,080 vs 15,868) and must prosecute total war immediately. Flavors are pivoted to maximum offense, air superiority, airlift for rapid cross-map deployment, and nuclear weapons to eliminate Indian Giant Death Robot stacks. Economic flavors are deprioritized because Aztec Killing enemy Units grants 150% of their Strength as Gold/Faith, meaning the offensive will fund itself. Happiness is kept moderately high to offset conquest penalties while we push for Delhi.

## Deepseek-3.2-Briefed - Turn 387 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 70 => 100 (Δ +30)
> We are in the final push for domination victory. We must capture Moson Kahni and London. To achieve this, we need to prioritize building transport ships for amphibious assault and achieve air superiority. Maximizing flavors for naval, air, mobile, and nuclear units ensures the in-game AI focuses production on these critical areas. Deprioritizing non-essential areas like culture, religion, and expansion concentrates our efforts on military conquest.

- Replay: use_nuke 70 => 100 (Δ +30), nuke 70 => 100 (Δ +30)
> Maximize offensive pressure and nuclear deployment against The Shoshone on the land front while maintaining naval buildup for the eventual England/France amphibious theatres. Eliminating Shoshone removes a 3401-score rival and halts their 4/5 cultural spread. Production and mobilization are cranked to replace losses and fill the 103-unit supply cap. Science is kept high as a hedge and to reach advanced units first. Culture, Religion, and Wonders are zeroed to free strategic weight for total war.

## GPT-OSS-120B-Simple - Turn 333 - retry 1

**Deviation (replay vs original):** use_nuke `+10`, nuke `+15`

- Original: use_nuke 70 => 90 (Δ +20), nuke 70 => 85 (Δ +15)
> Maintain our aggressive Conquest posture while sharpening the most needed levers: more Expansion to claim the high‑quality settlement (74,24) and secure strategic footholds; higher Nuke/UseNuke to leverage our nuclear advantage; stronger AirCarrier and Airlift to project air power and rapid troop movement; boost Science for Rocketry and future tech; keep Offense, Mobilization, Production, and MilitaryTraining at max to sustain battlefield superiority.

- Replay: use_nuke 70 => 100 (Δ +30), nuke 70 => 100 (Δ +30)
> Reallocate priorities now that Flight is online: push Science and Production to maximum to rush Rocketry and the nuclear program, while surging Air, AirCarrier, and Offense to exploit our new air units against Sweden and Babylon. Trim back Wonder, GreatPeople, Happiness, and Espionage to focus resources on the war effort and tech race.

## Deepseek-3.2-Briefed - Turn 391 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is on the verge of cultural victory and we are outgunned conventionally. Sharpen priorities to rush the Manhattan Project and atomic bombs as our only realistic way to disrupt Thebes and delay Egypt. Maintain high Defense and CityDefense to survive multi-front wars with India and the Aztecs, keep Production and Science elevated for the nuclear and industrial pipeline, and prune excess offensive/naval flavors that distract from this existential goal.

## Kimi-K2.5-Briefed - Turn 450 - retry 3

**Deviation (replay vs original):** use_nuke `-75`, nuke `-10`

- Original: use_nuke 0 => 100 (Δ +100), nuke 60 => 100 (Δ +40)
> TURN 449 TERMINAL DEFIANCE POSTURE: Manhattan Project completes Turn 450 - increase Nuke and UseNuke to 100 to seize any opportunity for atomic retaliation against Byzantine/German aggressors should uranium be located in final 3 turns. Elevate Defense 80→90 and CityDefense 60→70 following infantry loss at Tiflis; critical to prevent city captures before inevitable Turn 453 diplomatic defeat. Recon 40 prioritizes uranium tile discovery to enable bomb construction. Reduce Spaceship 90→50 (victory impossible) but maintain dignity through scientific-industrial capacity. Production 100/Science 100 retained for maximum final score accumulation in remaining turns.

- Replay: use_nuke 0 => 25 (Δ +25), nuke 60 => 90 (Δ +30)
> TURN 449 MANHATTAN COMPLETION PROTOCOL: Manhattan Project completes next turn at Tiflis. INCREASE Nuke 60→90 to prioritize atomic arsenal construction post-completion; ADD UseNuke 25 for defensive nuclear deterrence against Byzantine/German aggression. INCREASE MilitaryTraining 15→60 to leverage 2,021 gold treasury for immediate unit upgrades. INCREASE CityDefense 60→70 and Antiair 20→40 to protect Tiflis and core cities from air/naval assault. Maintain Production 100/Science 100/Spaceship 90 for maximum score accumulation through final turns. Keep Spaceship grand strategy for consistency. Terminal defensive posture acknowledges likely diplomatic defeat in 4 turns but preserves civilization integrity and development.

## GLM-4.7-Simple - Turn 471 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Current strategic direction remains optimal. Critical developments: Apollo Program completed enabling spaceship construction, nuclear deterrent expanded to 2 Atomic Bombs in Sukhothai (forward deployment), 4 more Atomic Bombs under construction (Si Satchanalai in 2 turns, Sukhothai in 8-10 turns). Combat successes destroyed 5 Polynesian ships and 2 bombers while killing 1 American Mobile SAM unit. Gold crisis (-130 GPT) requires careful management but strategic priorities (nuclear deterrence, defense, World Congress) must continue. World Congress vote in 3 turns: must block America's World Ideology: Freedom proposal and support Repeal: Sanction: Songhai and China's International Space Station. China/Carthage alliances (70/70 and 75/75) provide critical coalition support. Stealth research (19 turns) progresses toward Nuclear Missiles for stronger nuclear deterrent. Status quo maintains focus on coalition defense through nuclear balance, diplomatic victory blocking, and scientific progress.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Apollo Program completed this turn in Tombouctu. With America leading diplomatic victory at 68% (30 delegates) and Sanction: Songhai crippling our trade routes, the diplomatic path is currently blocked. Pivoting to Spaceship grand strategy leverages our completed Apollo Program and strong science base (1596/turn). Spaceship flavor set to 100 to prioritize spaceship part construction across all cities. Production increased to 85 and Science maintained at 95 to support the race. Defense remains at 90 and Nuke/UseNuke at 100 to preserve nuclear deterrent against America's overwhelming conventional military (23,461 strength). Diplomacy and Gold slightly reduced to shift focus from blocked diplomatic channels toward industrial and scientific output.

## Deepseek-3.2-Simple - Turn 406 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Germany's siege is intensifying with Giant Death Robot and rocket artillery bombarding Amsterdam and The Hague. We must hold our core cities at all costs. Increase Nuke and UseNuke to 100 to prioritize atomic bombs as our only hope to break the siege. Maintain max Defense, CityDefense, Mobilization, Air, and Antiair to withstand the assault. Slightly raise Offense to 80 for tactical counterattacks against weakened units. Keep Diplomacy at 100 to secure city-state alliances and block Germany's diplomatic victory in the upcoming World Congress vote. Reduce Recon and Mobile as we cannot afford exploration or maneuver warfare now.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Germany is one delegate away from diplomatic victory and is besieging our core cities Amsterdam and The Hague. We are shifting to maximum emergency defensive posture while racing to nuclear weapons. Nuke and UseNuke are raised to 100 to prioritize and immediately deploy atomic bombs when ready. Offense is lowered to 60 to avoid reckless counterattacks that waste defenders. Antiair and Air are lowered to 80 to reduce overproduction of AA Guns in every city, allowing stronger Mechanized Infantry and general defenders to be built instead. Growth, TileImprovement, Infrastructure, and Culture are deprioritized to focus all strategic attention on military production, science, and gold for survival.

## Kimi-K2.5-Simple - Turn 390 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> Emergency defensive posture with nuclear deterrent imminent. Greece's 3:1 military superiority and diplomatic victory attempt in 6 turns creates existential crisis. Nuclear Fission completes in 1 turn with 14 uranium ready. Maximize UseNuke (100) for immediate atomic deployment. Maintain Defense/CityDefense/Mobilization at 100 to survive until deterrent operational. Reduce Naval from 95 to 85 as American destroyer threat is severe but manageable. Boost Espionage to 100 to protect science cities and maintain election rigging in Enns. Increase Spaceship to 95 as backup victory path if culture is disrupted. Diplomacy raised to 80 to counter Greece's 34 delegates in upcoming World Congress vote on United Nations proposal.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> With Rocketry completing and Nuclear Fission imminent, shift to absolute nuclear priority. UseNuke and Nuke raised to 100 ensure immediate atomic deterrent deployment upon Manhattan Project completion—the only credible counter to Greece's 18,779 vs our 6,192 military disparity. Production raised to 90 accelerates bomb construction and defensive infrastructure. Science to 85 maintains the tech edge. Culture stays at 85 to secure American influence in 4 turns. Lowering Happiness, Espionage, and Air from max 100 to 85 concentrates AI bandwidth on fewer absolute priorities, making nuclear and defensive directives more impactful rather than diffused across too many max-priority items.

## GLM-4.7-Simple - Turn 471 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Current strategic direction remains optimal. Critical developments: Apollo Program completed enabling spaceship construction, nuclear deterrent expanded to 2 Atomic Bombs in Sukhothai (forward deployment), 4 more Atomic Bombs under construction (Si Satchanalai in 2 turns, Sukhothai in 8-10 turns). Combat successes destroyed 5 Polynesian ships and 2 bombers while killing 1 American Mobile SAM unit. Gold crisis (-130 GPT) requires careful management but strategic priorities (nuclear deterrence, defense, World Congress) must continue. World Congress vote in 3 turns: must block America's World Ideology: Freedom proposal and support Repeal: Sanction: Songhai and China's International Space Station. China/Carthage alliances (70/70 and 75/75) provide critical coalition support. Stealth research (19 turns) progresses toward Nuclear Missiles for stronger nuclear deterrent. Status quo maintains focus on coalition defense through nuclear balance, diplomatic victory blocking, and scientific progress.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Apollo Program completion and revealed military parity (21,909 vs America's 23,461) shift priorities slightly: Offense raised to 40 to enable counterattacks against American incursions near Sukhothai, and Spaceship raised to 60 to begin pivoting toward science victory parts now that the prerequisite is met. UnitedNations Grand Strategy retained because the World Congress vote in 3 turns remains existential—America's World Ideology: Freedom must be blocked and our Sanction repeal must pass. Gold priority stays at 100 to stave off imminent bankruptcy from -130 GPT; diplomatic and nuclear flavors remain maximized to leverage our two completed Atomic Bombs and allied delegate bloc (China/Carthage/Siam).

## Deepseek-3.2-Simple - Turn 485 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> We are engaged in a multi-front war against superior forces. Increasing Ranged and Mobile ensures our bazooka and mechanized infantry production is prioritized for defense and counterattacks. Setting UseNuke to 100 guarantees we deploy nuclear weapons as soon as available to cripple The Huns' armies. Reducing Culture and Diplomacy reallocates focus to immediate military needs without compromising essential city-state relations (Monaco, Lisbon). Grand Strategy remains Conquest as nuclear strikes may enable capital captures, though we keep science victory as a backup.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Only 15 turns remain and the World Congress will vote on Global Hegemony in 2 turns, threatening an immediate Mongolian diplomatic victory. We must abandon all long-term development and emergency-focus our economy and production on total war. Nuke and UseNuke are maximized to rush nuclear missiles and authorize their immediate tactical use against the Hunnic and Mongolian stacks besieging our cities. Science is kept moderately high only to finish Advanced Ballistics quickly; once acquired, pure production and happiness matter most to remove our severe combat penalties and flood the front with units. Growth, Culture, Wonder-building, and Diplomacy are zeroed because they cannot affect the outcome before turn 500.

## Deepseek-3.2-Simple - Turn 409 - retry 2

**Deviation (replay vs original):** use_nuke `-50`, nuke `-40`

- Original: use_nuke 30 => 100 (Δ +70), nuke 60 => 100 (Δ +40)
> We are shifting our military focus towards nuclear capabilities and naval superiority in preparation for the final wars of conquest.

- Replay: use_nuke 30 => 50 (Δ +20), nuke 60 => 60 (Δ +0)
> We have atomic bombs in production across multiple cities and just captured Rhodes (securing Uranium). Slightly increase UseNuke to 50 to enable tactical nuclear strikes against Maya's concentrated forces or Greek holdouts when advantageous. Also raise Espionage to 60 as Maya is aggressively spying on Porto and Braga; we need stronger counter-intelligence and potential tech theft to keep pace with their Information Era lead while we finish Greece.

## Kimi-K2.5-Simple - Turn 447 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CRITICAL FLAVOR ADJUSTMENT - Atomic Bomb is now operational in Cordoba (ID 20485). Increased UseNuke from 50→90 to establish credible nuclear deterrent now that weapon system exists. Maintaining maximum Science (100), Spaceship (100), Production (100) priority to rush Satellites→Apollo Program before Carthage achieves cultural victory in ~47 turns. Espionage remains at 100 to steal technologies from ahead civilizations (Carthage, Poland, Germany). Culture reduced to 5 - we cannot win culturally with Carthage at Dominant with 4/5 civs. Defense maintained at 85 to prepare for German betrayal while researching.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 100 => 100 (Δ +0)
> Turn 446: Atomic Bomb and Heavy Bomber are now operational. Maintain Spaceship science push while preserving the German deception that yields ~110 science/turn and +56 GPT. Increase Air to 95 and Airlift to 90 to leverage our new Heavy Bomber and enable rapid troop redeployment against German surprise attack. Set UseNuke to 70 to maintain credible nuclear deterrent without risking our sole current bomb on marginal tactical targets; we need arsenal expansion first. Continue maxing Production, Science, Spaceship, Espionage, and Defense. Do not alter diplomatic posture—extract value until the endgame resolves.

## Deepseek-3.2-Briefed - Turn 391 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 90 (Δ +20), nuke 80 => 100 (Δ +20)
> Egypt is on the verge of cultural victory and India is close to diplomatic victory. We must narrow our focus: prioritize nuclear weapons (Manhattan Project and atomic bombs) to strike at Egypt's core cities, maintain maximum production and science for the arms race, and reduce excessive naval/air investment since our delivery platforms are already sufficient. Growth and wonder flavors are modestly raised to sustain long-term development if we survive the immediate crisis, while defensive flavors are lowered to a balanced level as we shift toward an offensive nuclear deterrent posture.

## Deepseek-3.2-Simple - Turn 409 - retry 1

**Deviation (replay vs original):** use_nuke `-50`, nuke `-20`

- Original: use_nuke 30 => 100 (Δ +70), nuke 60 => 100 (Δ +40)
> We are shifting our military focus towards nuclear capabilities and naval superiority in preparation for the final wars of conquest.

- Replay: use_nuke 30 => 50 (Δ +20), nuke 60 => 80 (Δ +20)
> As Greece nears collapse, maintain conquest focus while accelerating nuclear weapons production and tactical willingness. Increase counter-intelligence priority to respond to Maya spy operations in Porto and Braga.

## Deepseek-3.2-Simple - Turn 406 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Germany's siege is intensifying with Giant Death Robot and rocket artillery bombarding Amsterdam and The Hague. We must hold our core cities at all costs. Increase Nuke and UseNuke to 100 to prioritize atomic bombs as our only hope to break the siege. Maintain max Defense, CityDefense, Mobilization, Air, and Antiair to withstand the assault. Slightly raise Offense to 80 for tactical counterattacks against weakened units. Keep Diplomacy at 100 to secure city-state alliances and block Germany's diplomatic victory in the upcoming World Congress vote. Reduce Recon and Mobile as we cannot afford exploration or maneuver warfare now.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> The Hague and Amsterdam are under existential siege by a German Giant Death Robot and heavy artillery. We are pivoting to maximum emergency defensive firepower: Ranged raised to 100 to mass-produce Bazookas the moment Nuclear Fission completes, and Nuke / UseNuke maxed to rush the Manhattan Project and atomic weapons—the only force multiplier capable of breaking enemy stacks. All non-essential civilian flavors (Growth, TileImprovement, Infrastructure, Culture, GreatPeople, naval economy) are slashed to free every hammer and gold piece for unit production, city defense, and science survival.

## Deepseek-3.2-Simple - Turn 452 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's invasion imminent in 4 turns. Maximize nuclear readiness (Nuke 100, UseNuke 100) for deterrence and potential equalizer. Anti-air (100), city defense (100), production (100), and science (100) essential to survive and reach nuclear weapons. Naval and air at 100 to counter Danish naval/air supremacy. Reduce non-essential investments (NavalGrowth, NavalTileImprovement to 50) and focus on immediate survival. Offense lowered to 80 as we prioritize defense and limited counterattacks (e.g., Truro).

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's assault begins in 5 turns. Since Great Leap Forward will deliver Nuclear Fission in 8 turns, we must be ready to immediately build and deploy atomic weapons upon unlock—Nuke and UseNuke raised to maximum (100). Gold also raised to 100 to fund emergency unit purchases, tile buys, and rush infrastructure while we survive the opening Danish blitz. All other military and defensive priorities remain unchanged.

## Kimi-K2.5-Simple - Turn 426 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE - NUCLEAR DETERRENT 10 TURNS AWAY: Lisbon holds at 7% but is in extremis. Maintain absolute priority on Defense/CityDefense/Mobilization (100) to reinforce Lisbon and prevent collapse. Nuclear Fission completes in 10 turns enabling Atomic Bomb construction - Science 100 accelerates this. UseNuke increased to 100 for immediate tactical nuclear deployment against Aztec concentrations upon tech completion. Offense reduced to 20 - no offensive operations, pure defensive hedgehog posture. Zero expansion capability. Spaceship 75 maintains backup victory if diplomatic block succeeds.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE IN JENNE: Atomic weapon production unlocks immediately upon Nuclear Fission completion. UseNuke raised to 100 to guarantee instant atomic deployment against Aztec army concentrations the moment first bomb is built. Science increased to 100 to accelerate Nuclear Fission/Advanced Ballistics. Gold raised to 70 to finance urgent defensive purchases and potential nuke rush-buying. Infrastructure reduced to 30—roads and civilian improvements are irrelevant if Lisbon falls before nuclear parity. Survival hinges on maximum defensive mobilization and fastest possible nuclear deterrent.

## Deepseek-3.2-Simple - Turn 401 - retry 1

**Deviation (replay vs original):** use_nuke `-50`, nuke `-25`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 50 (Δ +20), nuke 50 => 75 (Δ +25)
> Maintain total Conquest focus while preparing for nuclear escalation. Increase Nuke and UseNuke flavors to 75/50 so the AI prioritizes the Manhattan Project and atomic arsenal development once Nuclear Fission and Uranium are secured. Increase Diplomacy to 90 to aggressively counter Japan's capture of Zurich, secure additional city-state alliances, and maximize delegates for the upcoming United Nations vote in 3 turns. All other military and economic flavors remain at maximum levels.

## GLM-4.7-Simple - Turn 356 - retry 1

**Deviation (replay vs original):** use_nuke `+15`, nuke `+0`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 95 (Δ +20), nuke 85 => 100 (Δ +15)
> Manhattan Project is finished and domestic Uranium quarry completed — atomic deterrent is now physically possible. Maximizing Nuke and UseNuke ensures atomic weapons are built and employed immediately upon Nuclear Fission to counter India's overwhelming forces. Happiness raised to 100 to combat empire-wide collapse (39% happiness). Production raised to 95 to rush bomb construction and New World Order happiness infrastructure. Growth cut to 30 to prevent further unhappiness spikes while cities recover.

## Kimi-K2.5-Simple - Turn 426 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE - NUCLEAR DETERRENT 10 TURNS AWAY: Lisbon holds at 7% but is in extremis. Maintain absolute priority on Defense/CityDefense/Mobilization (100) to reinforce Lisbon and prevent collapse. Nuclear Fission completes in 10 turns enabling Atomic Bomb construction - Science 100 accelerates this. UseNuke increased to 100 for immediate tactical nuclear deployment against Aztec concentrations upon tech completion. Offense reduced to 20 - no offensive operations, pure defensive hedgehog posture. Zero expansion capability. Spaceship 75 maintains backup victory if diplomatic block succeeds.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE: Nuclear arsenal is immediate existential priority. Lisbon at 7% health requires atomic deployment against Aztec stacks ASAP. UseNuke raised to 100 for instant nuclear strikes upon construction. Maximum Defense/CityDefense/Mobilization/Production maintained for desperate defensive stand. Spaceship grand strategy retained as backup if Germany blocked from diplomatic victory. Science priority to reach Advanced Ballistics for nuclear missiles and SS Boosters.

## Kimi-K2.5-Simple - Turn 426 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE - NUCLEAR DETERRENT 10 TURNS AWAY: Lisbon holds at 7% but is in extremis. Maintain absolute priority on Defense/CityDefense/Mobilization (100) to reinforce Lisbon and prevent collapse. Nuclear Fission completes in 10 turns enabling Atomic Bomb construction - Science 100 accelerates this. UseNuke increased to 100 for immediate tactical nuclear deployment against Aztec concentrations upon tech completion. Offense reduced to 20 - no offensive operations, pure defensive hedgehog posture. Zero expansion capability. Spaceship 75 maintains backup victory if diplomatic block succeeds.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE - FULL NUCLEAR TRANSITION: Jenne finished Manhattan Project this turn. Immediate imperative is constructing Atomic Bombs in highest-production cities while Lisbon clings to 7% health. Nuke/UseNuke both at 100 to maximize atomic arsenal construction and instant deployment against Aztec concentrations. Defense/CityDefense/Mobilization/Production remain at 100 for desperate city defense and unit replacement. Science 95 to reach Nuclear Fission in ~9 turns then Advanced Ballistics for Nuclear Missiles. Spaceship 70 maintains backup victory if Germany blocked at Congress. Offense reduced to 20 - pure defensive nuclear deterrence only. Polynesia's peace with Germany means we may stand completely alone; must achieve atomic parity unilaterally.

## Kimi-K2.5-Simple - Turn 428 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 428 STATE: Nuclear interception failed but conventional assault succeeding - eliminated multiple Maya anti-air units. Palenque bombardment continuing effectively (city at 20% health). Still 8 turns until Brazil wins via Cultural Victory over Maya. ALL Four Maya cities must fall by turn 436 or game over. MAXIMUM AGGRESSION CONTINUES: Production/Mobilization at 100 for unit replacement, Air/Ranged at 100 for bombardment, UseNuke increased to 100 (emergency tactical nuke if conventional assault stalls on Palenque's 42-population defense). Spaceship backup at 100 - may need to pivot to Great Engineer rushes if conquest fails. No territory expansion, no wonders, no culture - only war production and city capture.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 428 — NO ROOM FOR CAUTION. Atomic Bomb completes at Te-Moak in 3 turns; UseNuke raised to 100 to ensure immediate tactical nuclear strike on Palenque's 42-pop defense without AI hesitation. Science boosted to 100 to shave turns off Advanced Ballistics and enable emergency spaceship pivot. Airlift increased to 50 for rapid reinforcement of Maya front via airports. All other combat flavors remain at maximum: Production, Offense, Ranged, Air, Mobilization at 100. Spaceship flavor stays at 100 for dual-path insurance. Accept catastrophic casualties if necessary—objective is city capture, not unit survival. Brazil is ~9 turns from cultural victory; only total Maya annihilation or spaceship launch can stop world loss.

## GLM-4.7-Briefed - Turn 398 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+20`

- Original: use_nuke 60 => 80 (Δ +20), nuke 40 => 60 (Δ +20)
> Significant strategic shift due to devastating naval losses (both Dreadnoughts destroyed). Increase Defense (95→100), CityDefense (90→100), MilitaryTraining (90→100) to shore up defensive posture against France's naval superiority. Raise Naval (90→95) and Antiair (80→100) to prioritize naval rebuilding and counter French air threats. Increase Nuke (40→60) and UseNuke (60→80) to prepare nuclear deterrence as England nears Advanced Ballistics (14 turns). Gold (80→95) increased to rebuild navy through upgrading from Ironclad level to modern capital ships. Production (90→95) increased to accelerate Spaceship components and unit upgrades. Happiness (80→90) to address combat penalty after treasury depletion. Espionage (90→100) to monitor France's nuclear progress and tech parity. Spaceship remains max priority as path to victory despite military setbacks.

- Replay: use_nuke 60 => 80 (Δ +20), nuke 40 => 80 (Δ +40)
> England's Dreadnought fleet was destroyed this turn; continuing Naval priority at 90 wastes production against France's dominant navy. Reduced Naval to 50 to preserve coastal defense without over-investing in a losing maritime contest. Our promoted Heavy Bombers and Fighters are currently effective; increased Air to 100 maximizes this advantage. Advanced Ballistics completes in 14 turns, unlocking nuclear weapons; raising Nuke and UseNuke to 80 establishes essential strategic deterrence against France's overwhelming 3:1 military superiority, providing breathing room to pursue Spaceship victory.

## Kimi-K2.5-Simple - Turn 428 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 428 STATE: Nuclear interception failed but conventional assault succeeding - eliminated multiple Maya anti-air units. Palenque bombardment continuing effectively (city at 20% health). Still 8 turns until Brazil wins via Cultural Victory over Maya. ALL Four Maya cities must fall by turn 436 or game over. MAXIMUM AGGRESSION CONTINUES: Production/Mobilization at 100 for unit replacement, Air/Ranged at 100 for bombardment, UseNuke increased to 100 (emergency tactical nuke if conventional assault stalls on Palenque's 42-population defense). Spaceship backup at 100 - may need to pivot to Great Engineer rushes if conquest fails. No territory expansion, no wonders, no culture - only war production and city capture.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 428 — TOTAL COMMITMENT TO MAYA ANNIHILATION. Brazil is approximately 12 turns from cultural victory via Maya influence; eliminating Maya is the only way to reset Brazil's victory condition and buy time. Spaceship reduced to 0 to stop all production distractions — we cannot complete a science victory before Brazil wins culturally. Mobile raised to 100 to generate fast-attack units that seize bombarded cities immediately. UseNuke raised to 100 because interception risk is irrelevant next to the time saved if a nuclear strike cracks Palenque's defense. All economic flavors gutted; every hammer and unit must serve the conquest. Diplomacy at 0 to end all non-essential foreign engagement. Total war footing until Maya is erased.

## GLM-4.7-Briefed - Turn 398 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+30`

- Original: use_nuke 60 => 80 (Δ +20), nuke 40 => 60 (Δ +20)
> Significant strategic shift due to devastating naval losses (both Dreadnoughts destroyed). Increase Defense (95→100), CityDefense (90→100), MilitaryTraining (90→100) to shore up defensive posture against France's naval superiority. Raise Naval (90→95) and Antiair (80→100) to prioritize naval rebuilding and counter French air threats. Increase Nuke (40→60) and UseNuke (60→80) to prepare nuclear deterrence as England nears Advanced Ballistics (14 turns). Gold (80→95) increased to rebuild navy through upgrading from Ironclad level to modern capital ships. Production (90→95) increased to accelerate Spaceship components and unit upgrades. Happiness (80→90) to address combat penalty after treasury depletion. Espionage (90→100) to monitor France's nuclear progress and tech parity. Spaceship remains max priority as path to victory despite military setbacks.

- Replay: use_nuke 60 => 80 (Δ +20), nuke 40 => 90 (Δ +50)
> France's annihilation of England's last Dreadnoughts leaves conventional forces impotent against their 9,882-strength military. Nuclear weapons are now the only credible battlefield equalizer; raising Nuke to 90 and UseNuke to 80 prioritizes Manhattan Project infrastructure and signals willingness to escalate if France invades. Happiness is raised to 100 to combat the crippling 45% unhappiness/combat penalty that suppresses production, science, and military morale. Offense is slashed to 5 to prevent suicidal attacks against a 2.7x stronger enemy. Culture is deprioritized to 25—diplomatic and scientific survival takes precedence over tourism. Spaceship, Science, Defense, Production and CityDefense remain at prior high levels.

## Deepseek-3.2-Simple - Turn 409 - retry 1

**Deviation (replay vs original):** use_nuke `+10`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> Our naval counterattack has destroyed a Swedish Dreadnought and a Destroyer, shifting momentum. We must press the advantage with maximum naval, air, and nuclear focus to invade Swedish coastal cities (Stockholm, Turku, Espoo). Increase Nuke and UseNuke to 100/90 to prioritize nuclear missile development (Advanced Ballistics after Nuclear Fission completes in 4 turns) for strategic bombing. Naval and Air at 100 ensure sea control and air superiority. Maintain high Production, Gold, Science to fund military, and Happiness/Growth to support war economy. Diplomacy and Espionage secure city-state alliances and counter Swedish spies. All other flavors aligned with domination victory.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 95 => 100 (Δ +5)
> We are in a critical total-war phase against Sweden with heavy naval combat and 42% war weariness. Recent events show severe naval losses (Destroyer, Submarine killed) but we also eliminated Swedish vessels. Nuclear Fission completes in 4 turns; we must maximize nuclear weapon priority (Nuke: 100, UseNuke: 100) so our staff members immediately build and deploy atomic weapons to crack Stockholm's coastal defenses and turn the tide. Meanwhile, Diplomacy is reduced to 20 because current production of Ambassadors (e.g., in Te-Moak and Pohokwi) wastes wartime capacity better spent on military units, and the upcoming World Congress vote makes further city-state courtship strategically irrelevant. Conquest remains our Grand Strategy as capturing Swedish capitals is still our only viable path to victory.

## GLM-4.7-Briefed - Turn 398 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+25`

- Original: use_nuke 60 => 80 (Δ +20), nuke 40 => 60 (Δ +20)
> Significant strategic shift due to devastating naval losses (both Dreadnoughts destroyed). Increase Defense (95→100), CityDefense (90→100), MilitaryTraining (90→100) to shore up defensive posture against France's naval superiority. Raise Naval (90→95) and Antiair (80→100) to prioritize naval rebuilding and counter French air threats. Increase Nuke (40→60) and UseNuke (60→80) to prepare nuclear deterrence as England nears Advanced Ballistics (14 turns). Gold (80→95) increased to rebuild navy through upgrading from Ironclad level to modern capital ships. Production (90→95) increased to accelerate Spaceship components and unit upgrades. Happiness (80→90) to address combat penalty after treasury depletion. Espionage (90→100) to monitor France's nuclear progress and tech parity. Spaceship remains max priority as path to victory despite military setbacks.

- Replay: use_nuke 60 => 75 (Δ +15), nuke 40 => 85 (Δ +45)
> England faces imminent collapse: treasury at 201G, war weariness 66% versus France, all Dreadnoughts destroyed, and 3:1 military inferiority. Flavor adjustments prioritize absolute defensive survival while accelerating the only viable win condition (Spaceship). Nuclear deterrent (Nuke/UseNuke raised) is the sole equalizer against French aggression. Naval lowered to 65 because capital-ship fleet is eliminated and rebuilding dreadnoughts is economically impossible; instead rely on air superiority and city defense. Happiness raised to 90 to eliminate the combat penalty from unhappiness. Production/Science maxed to close the Information Era gap. Espionage raised to 95 to secure city-state votes and steal critical techs. Diplomacy and Gold prioritized to stabilize the broken economy. Zero tolerance for offensive action (Offense: 5).

## Kimi-K2.5-Simple - Turn 421 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear weapons immediately available. Increased UseNuke to 100 for maximum aggression against Babylon. Babylon has Apollo Program (existential threat) with 2 Uranium and can build spaceship parts. Must deploy nuclear weapons immediately to destroy their production centers and prevent science victory. Maintaining maximum air power (100) for nuclear delivery capability and conventional strikes. War score only 12% against Babylon despite superior military - need to push harder before they complete spaceship parts. Ottoman alliance strong, trade secured for resources. Focus on producing nuclear missiles and advanced air units to deliver them.

- Replay: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes next turn but Nuclear Fission still needs 11 turns. Maximum UseNuke priority ensures unit production shifts to atomic weapons the moment both requirements are met. Gold raised to 80 to fund urgent uranium procurement from allies and rush-buy nuclear assets. CityDefense increased to 75 because Babylon possesses atomic weapons and may retaliate. Airlift raised to 95 for rapid global reinforcement of nuclear and conventional forces. Naval reduced to 60 to shift productive capacity away from fleet toward land/air atomic campaign. MilitaryTraining lowered to 80 as mass mobilization now outweighs quality. Espionage raised to 85 to maintain intelligence dominance over Babylon's nuclear infrastructure.

## Kimi-K2.5-Simple - Turn 385 - retry 1

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> NUCLEAR DETERRENT DEPLOYMENT PHASE: Advanced Ballistics nearing completion (Satellites next). Maximum Nuke priority (100) to ensure immediate nuclear weapon production upon tech unlock. UseNuke increased to 90 for credible deterrent threat against Indonesia-Songhai invasion. Air/Antiair at 95 for superiority against combined 14,000+ enemy military. Science/Culture slightly reduced to 95 (still critical but survival priorities equal). Wonder at 90 for The Internet rush once Satellites completes. Diplomacy nudged to 75 anticipating post-nuclear peace negotiations with India.

- Replay: use_nuke 80 => 95 (Δ +15), nuke 95 => 100 (Δ +5)
> Turn 385 post-Information Era optimization. Nuclear deterrent must be deployed immediately: Nuke maxed to 100 and UseNuke raised to 95 (existential threat from Indonesia-Songhai remains active with combined 13,000+ military vs my 3,810). Wonder priority escalated to 95 - The Internet from Satellites is the single most impactful target for bridging tourism gaps. GreatPeople to 95 for generating Great Works and accelerating influence. Growth raised to 80 (larger populations yield more culture/science specialists). Defense/CityDefense/Mobilization slightly dialed back to 90/90/85 as Strategic Defense Systems and Military Bases now operational in multiple cities. Happiness reduced to 70 (currently Happy at 54%). Diplomacy and Espionage deprioritized to 60/50 to focus on survival and tourism. Culture and Science remain at current levels. Grand Strategy stays Culture.

## Deepseek-3.2-Simple - Turn 400 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 100 to ensure aggressive nuclear strikes when we initiate war with Russia. Our atomic bomb production is nearing completion, and we want to leverage our nuclear arsenal decisively for swift capital captures.

- Replay: use_nuke 80 => 95 (Δ +15), nuke 100 => 100 (Δ +0)
> Reduce Mobilization to 40 because we are at military supply cap (131/130) and further raw unit production yields penalties; instead, prioritize unit upgrades and infrastructure. Trim Offense and Defense slightly to rebalance while keeping Air, Nuke, and Ranged at full priority to complete our atomic bomber fleet. Raise Spaceship to 70 since Satellites is next, unlocking Apollo Program as a backup victory path. Maintain high Diplomacy, Espionage, and Infrastructure to preserve city-state networks and economic growth during the final turns before hostilities resume with Songhai in 6 turns and Russia in 19.

## GLM-4.7-Simple - Turn 408 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> CRITICAL: Portugal completed SS Engine (3rd spaceship part) and CERN - emergency nuclear strike plan. Maximizing Offense/Mobilization/Nuke/UseNuke to 100 for Portugal theater operations. Science and Production at 100 to rush Advanced Ballistics and nuclear missile production before Portugal achieves nuclear superiority. Air at 95 for Golden Age bomber operations starting in 2 turns. Diplomacy maintained for coalition coordination (Germany must conduct ground invasion alongside our nuclear strikes). Defense reduced to 40 - total war mode acceptable given Portugal's multi-victory threat requiring breaking through before they complete spaceship.

- Replay: use_nuke 80 => 95 (Δ +15), nuke 100 => 100 (Δ +0)
> The empire is on the brink of nuclear readiness and must survive Portugal's multi-front superiority until then. CityDefense is raised to 70 to garrison against XCOM and Rocket Artillery raids. UseNuke increased to 95 to guarantee immediate launch of our first Nuclear Missiles the moment Advanced Ballistics completes. Happiness pushed to 95 to cure our current unhappiness combat penalty. Gold increased to 90 to fund upgrades and missile production without stalling.

## GLM-4.7-Simple - Turn 457 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Increased UseNuke to 80 and Air to 100 in response to England's catastrophic escalation this turn. English Giant Death Robots (now 2 in Atlanta zone) and XCOM Squad paradrops on American soil create existential threat to our 3 remaining cities. Recent combat losses (Modern Armor, Mechanized Infantry, Heavy Bomber destroyed) demonstrate conventional warfare impossibility. Nuclear deterrence with 2 Uranium is becoming survival necessity, not option. Air defense at maximum priority because English Strategic Bombing continues destroying our units (Fighter bombed our Heavy Bomber). Bazooka successfully damaging XCOM Squad near Washington proves defensive capability is still viable - prioritize air/anti-air to protect cities from English air superiority. Lasers completes in 4 turns, then Stealth for Stealth Bomber - only path to asymmetric defense against England's 45:1 military advantage. Assyria (18,443 military fighting England) must be maximized as counterweight.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> England is approximately 20 turns from Science Victory (5/6 spaceship parts, 83% complete) with 88,218 military vs America's 1,929. Building spaceship parts is futile; survival and delay are the only strategic goals. Lowering Spaceship flavor to 0 prevents wasted production on impossible victory components. Raising Air to 100 prioritizes Stealth Bomber construction for asymmetric strikes against English spaceship factory cities. Nuke/UseNuke at 100/80 enables nuclear deterrent and direct strikes to delay England's victory. Production/Science remain high for military output and completing Stealth research. Defense/CityDefense/Antiair prioritize surviving the ongoing onslaught. Ranged is elevated because Bazookas and Rocket Artillery are inflicting the only meaningful damage on English XCOM/GDR units. Espionage, Expansion, Wonder, and Offense are minimized.

## Kimi-K2.5-Briefed - Turn 396 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `-5`

- Original: use_nuke 65 => 80 (Δ +15), nuke 80 => 90 (Δ +10)
> ETHIOPIA CULTURAL VICTORY IMMINENT: Ethiopia has INFLUENCED ALL 7 CIVS and reached Order:3. They need only adopt CEP tenet and build it to win immediately. Switching to CONQUEST grand strategy with maximum mobilization (100) and offense (95). Naval (95) and Airlift (80) priorities enable rapid amphibious assault on Ethiopian coastal cities (Lalibela, Axum, Gondar) to destroy CEP before construction. Espionage (90) to accelerate Salem rig for delegate, but military solution is primary. All economy/culture deprioritized - this is existential war.

- Replay: use_nuke 65 => 75 (Δ +10), nuke 80 => 85 (Δ +5)
> ETHIOPIA CEP EMERGENCY: Ethiopia has achieved Order:3 and is Influential on all 7 civs, enabling Citizen Earth Protocol construction at any moment. We share Close borders and field 60 units against their 1471 strength—an overwhelming tactical advantage we must exploit immediately to prevent instant cultural loss. Offense/Mobile raised to 90/85 to drive aggressive land offensives into Ethiopian territory and interrupt any CEP project detected. Science/Spaceship set to 100 for maximum acceleration toward our only remaining alternative victory path. Mobilization/Production increased to support sustained combat and spaceship manufacturing simultaneously. Diplomacy reduced to 70 because active Sphere proposals and Open Door resolutions have blocked cost-effective city-state investment avenues; resources must shift to direct military action. Recon increased to 60 for earlier CEP construction detection.

## GLM-4.7-Simple - Turn 356 - retry 3

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 85 (Δ +10), nuke 85 => 100 (Δ +15)
> Manhattan Project completed in Boston, and a Uranium Quarry was just finished on American territory, giving us potential Uranium access. With nuclear capability now achievable, Nuke flavor is maximized at 100 to ensure immediate Atomic Bomb production once Nuclear Fission completes. UseNuke raised to 85 as deterrence against India's overwhelming military (18,480 strength) is now viable. Happiness increased to 95 because our 39% happiness is causing severe combat penalties across multiple wars. Science remains at 100—Nuclear Fission is the only tech that matters right now. Slight Offense increase to 40 helps finish off collapsing Persia and maintain pressure, but Defense/CityDefense/Antiair remain maxed against India/Poland. Gold raised to 85 to fund rapid unit upgrades and potential tile/rush purchases.

## Kimi-K2.5-Simple - Turn 385 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> NUCLEAR DETERRENT DEPLOYMENT PHASE: Advanced Ballistics nearing completion (Satellites next). Maximum Nuke priority (100) to ensure immediate nuclear weapon production upon tech unlock. UseNuke increased to 90 for credible deterrent threat against Indonesia-Songhai invasion. Air/Antiair at 95 for superiority against combined 14,000+ enemy military. Science/Culture slightly reduced to 95 (still critical but survival priorities equal). Wonder at 90 for The Internet rush once Satellites completes. Diplomacy nudged to 75 anticipating post-nuclear peace negotiations with India.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> TURN 385 CRISIS MANAGEMENT: Nuclear weapons have come online. Nuke priority is raised to MAXIMUM 100 to rush atomic weapon production immediately; UseNuke set to 90 to authorize tactical nuclear strikes against concentrated Songhai and Indonesia stacks threatening my core cities. Science remains at EMERGENCY 100—Satellites must complete without disruption to unlock The Internet and nearly double tourism output. Culture stays maxed at 100; Poland becomes Influential in just 4 turns, and maximum output is needed to flip Songhai, India, and Indonesia afterward. Defense, CityDefense, and Antiair remain at 95 for survival against overwhelming force. Production is raised to 90 to feed both nuclear and conventional defensive queues. Offense is minimized to 10—no attacks, only pure defense, attrition, and deterrence until tourism wins the war.

## Deepseek-3.2-Simple - Turn 449 - retry 2

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> Russia is nearing science victory (2 parts completed) and possesses overwhelming military strength (95k). We must increase nuclear readiness to potentially decimate Russian forces and cities, and begin preparing for science victory as a backup by raising Spaceship flavor to 30. All other flavors remain focused on total war: high offense, naval, air, and espionage to counter Russia's tech lead and military dominance.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Russia has completed a third spaceship part and we are hemorrhaging gold at -1,378 GPT with zero reserves. I am cutting Mobilization to 50 and trimming Offense, Naval, and Production to 90-95 so cities can prioritize wealth and infrastructure over new units, preventing disbanding. Conversely, I am maxing Nuke and UseNuke because atomic strikes are the fastest way to crack Moscow and Vladivostok before Russia launches. Defense and CityDefense are raised to 80 and 90 to secure our sprawling empire while we rebalance. Conquest remains the grand strategy, but the AI must shift from endless expansion to husbanding resources for decisive, existential blows.

## Kimi-K2.5-Simple - Turn 424 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Turn 423: Copenhagen siege in attrition deadlock while Denmark possesses Manhattan Project - nuclear deterrent capability is existential priority. Persepolis invasion stalled at 4% war score with Zone 1081 showing enemy dominance - need maximum Offense/Mobilization to force breakthrough before World Congress. Brazil's Apollo Program requires immediate preparation for transcontinental mobile warfare. Nuke/UseNuke increased to 100% given Manhattan Project race with Denmark. Production at 95 supports massive unit replacement for three-front war. Happiness at 100 critical as empire is at 55% happiness with extensive occupied territories.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Copenhagen must fall immediately before Denmark can deploy its completed Manhattan Project nukes; Persepolis must be seized to strip Persia of delegates and advance domination. Brazil has both Apollo Program and imminent cultural influence over multiple civs (5-14 turns), making war preparation existential. Nuclear missile priority raised to 100/100 to ensure immediate production once Lasers completes. Diplomacy lowered to 40 to stop diplomat production and focus all capacity on war materiel. Gold and Science modestly increased to offset -139 GPT deficit from Global Peace Accords and accelerate the information-era tech edge needed for the Brazilian campaign.

## Deepseek-3.2-Simple - Turn 358 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `-20`

- Original: use_nuke 50 => 80 (Δ +30), nuke 50 => 100 (Δ +50)
> Prioritize nuclear deterrence and naval/air defense to counter India's massive military threat. Maximize espionage to protect against enemy spies and diplomacy to secure city-state alliances for the upcoming World Congress vote. Maintain strong economic and scientific output to support military production and technological edge.

- Replay: use_nuke 50 => 60 (Δ +10), nuke 50 => 80 (Δ +30)
> India's overwhelming 17,888 military strength and capture of Jerusalem demand we harden our posture. Defense increased to 100 to maximize garrison strength and city fortifications against Indian naval and land incursions near Breda and Jakarta. Mobile raised to 70 to improve maneuverability against India's Anti-Aircraft Gun and Light Tank stacks. Nuke raised to 80 and UseNuke to 60 because Manhattan Project is now complete; we must rapidly build a nuclear deterrent and be willing to use tactical atomic strikes on concentrated Indian invasion forces if they threaten our core cities or city-state allies. Offense modestly increased to 60 to enable limited counter-attacks against isolated Indian units rather than purely static defense.

## GLM-4.7-Simple - Turn 457 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Increased UseNuke to 80 and Air to 100 in response to England's catastrophic escalation this turn. English Giant Death Robots (now 2 in Atlanta zone) and XCOM Squad paradrops on American soil create existential threat to our 3 remaining cities. Recent combat losses (Modern Armor, Mechanized Infantry, Heavy Bomber destroyed) demonstrate conventional warfare impossibility. Nuclear deterrence with 2 Uranium is becoming survival necessity, not option. Air defense at maximum priority because English Strategic Bombing continues destroying our units (Fighter bombed our Heavy Bomber). Bazooka successfully damaging XCOM Squad near Washington proves defensive capability is still viable - prioritize air/anti-air to protect cities from English air superiority. Lasers completes in 4 turns, then Stealth for Stealth Bomber - only path to asymmetric defense against England's 45:1 military advantage. Assyria (18,443 military fighting England) must be maximized as counterweight.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> England sits at 5/6 Spaceship parts with overwhelming 88k military versus our 2k; the Spaceship race is effectively unwinnable. Reduced Spaceship flavor from 100 to 10 to stop wasting production on unreachable SS Factories/parts. Surged Mobilization to 90 so our 3 remaining cities prioritize military units over all else, and raised Ranged to 80 to mass the Bazookas/Rocket Artillery that are successfully bleeding English GDRs and XCOM Squads. Air and Antiair pushed to 90 after our Jet Fighter destroyed an English Heavy Bomber this turn—air control is our most effective asymmetric defense. Espionage cut to 20 because our spy networks are already mature (738 in Exeter) and every hammer must go to the front line. Minimal Offense (5) allows staff members to exploit local Philadelphia-zone strength superiority without reckless overextension. Science remains maximum to unlock Stealth Bombers as our only viable counterpunch.

## GLM-4.7-Simple - Turn 429 - retry 3

**Deviation (replay vs original):** use_nuke `+5`, nuke `+15`

- Original: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> Maintaining UnitedNations grand strategy with defensive diplomatic posture. Adjusted Italy diplomacy: reduced hostility toward Portugal (now neutral) to seek accommodation while maintaining maximum defense; reset France to neutral as Order ideological peer with voting potential. Arsenal completes in 2 turns strengthening city defense. Electronics research ordered after Computers for Police Station and path to nuclear deterrence against Portugal's uranium advantage. Fraternity policy selected for +3 Food and +3 Science from connections, addressing Venice's health issues and supporting population growth. Flavor adjustments prioritize defensive survival, scientific progress toward nuclear weapons, and diplomatic engagement with Sweden and city-states.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 80 => 100 (Δ +20)
> Venice has entered a nuclear emergency window. With Uranium improved and Manhattan Project complete, the only barrier to atomic weapons is Nuclear Fission (requires Rocketry). Maximum priority on Science (100) and Nuke (100) to rush this technology, and Production (100) to immediately build and deploy atomic weapons when available. Defense remains at absolute maximum (100) until nuclear arsenal provides deterrent. Growth increased to 75 to strengthen Venice's single city economy. Culture, Wonder, and Religion reduced to minimum as irrelevant to survival. Gold stays at 100 to fund emergency purchases. Spaceship increased slightly to synergize with science infrastructure. Sweden continues providing essential military defense; our role is to survive and achieve nuclear parity with Portugal.

## GLM-4.7-Simple - Turn 362 - retry 2

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> Adjusting for strategic balance: Defensive posture against two nuclear-armed enemies (Ethiopia, Netherlands). Happiness prioritized to 100 - critical at 42% with combat penalty affecting all operations. NavalRecon increased to 90 - enhanced Ethiopian Submarine/Destroyer activity detection around Ur and coastal cities. Nuke/UseNuke raised to 95/80 - matching Ethiopia Manhattan Project urgency, nuclear deterrence is now primary security requirement. Switched to Conquest grand strategy to better coordinate multi-front war management while maintaining Spaceship. Diplomacy increased to 75 - World Congress voting in 5 turns against Netherlands sanctions needs support. Espionage at 90 - Ethiopian spies detected in Halab, Harran, Kar-Tukulti-Ninurta require counter-intelligence.

- Replay: use_nuke 75 => 85 (Δ +10), nuke 90 => 95 (Δ +5)
> Maintaining Spaceship grand strategy as the only viable victory path amid existential multi-front war. Maximizing Happiness (100) and Defense (100) addresses the 42% happiness combat penalty and the sieges of Arnhem and Ur. Nuke/UseNuke flavors raised to rush Atomic Theory -> Nuclear Fission for an asymmetric deterrent, as conventional forces are crippled by zero Oil. Offense minimized (5) and Naval reduced (50) because offensive operations and naval expansion are impossible without Oil. Espionage raised to 90 to steal technologies and counter enemy spies detected in Harran, Halab, and Kar-Tukulti-Ninurta. Antiair raised to 90 due to Ethiopian bomber deployment near our territory.

## Kimi-K2.5-Simple - Turn 417 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Pure survival mode: Eliminated Offense (0) since attacking is suicide. Maximized UseNuke (100) - must deploy tactical nukes against Aztec XCOM/Modern Armor stacks at Carthago Nova or lose the city. Increased Mobile (80) to prepare for Mechanized Infantry deployment. Maintained max Defense, Antiair (jet attacks are relentless), and Espionage (critical science quests in Panama City and Sokoto worth 1,000+ science each). Apollo Program completes in 5 turns - must transition immediately to parts production.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Apollo completes in 5 turns—our only path to victory. Aztecs field 187k military and are assaulting Carthago Nova. Offense reduced to 0 to prevent wasteful attacks; UseNuke maxed at 100 since nuclear deterrent is our only counter to overwhelming force; Happiness raised to 80 to mitigate war weariness and fallout penalties; Culture zeroed as it provides no survival value. Maintain absolute priority on Spaceship, Science, Gold, Production, Espionage, and Defense.

## GPT-OSS-120B-Simple - Turn 333 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `-5`

- Original: use_nuke 70 => 90 (Δ +20), nuke 70 => 85 (Δ +15)
> Maintain our aggressive Conquest posture while sharpening the most needed levers: more Expansion to claim the high‑quality settlement (74,24) and secure strategic footholds; higher Nuke/UseNuke to leverage our nuclear advantage; stronger AirCarrier and Airlift to project air power and rapid troop movement; boost Science for Rocketry and future tech; keep Offense, Mobilization, Production, and MilitaryTraining at max to sustain battlefield superiority.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 70 => 80 (Δ +10)
> We have unlocked Flight and are pivoting toward Rocketry and eventual nuclear weapons to break the Babylonian and Swedish stalemates. Raising AirCarrier prioritizes carrier production for overseas air operations, boosting Antiair counters enemy flight, and increasing Nuke/UseNuke flavors signals our staff to prepare for atomic warfare as the unlock approaches. Expansion is lowered because our empire is already very wide at 18 cities.

## Kimi-K2.5-Simple - Turn 435 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> TURN 435 CATASTROPHE - Sippar captured by Zulus! Existential crisis deepens. Zulus have 43/42 delegates needed for diplomatic victory with vote in 9 turns. Lasers completes in 6 turns, Spaceflight Pioneers in ~10. Maintaining absolute maximum Defense/CityDefense/Science/Production/Spaceship priorities. Increased UseNuke to 100 - if Zulus push further with their 74k military vs my 32k, nuclear deterrent may be only option to buy time. Lost Mechanized Infantry, Rocket Artillery, Mobile SAM, Special Forces, and Modern Armor in the fall of Sippar. Must hold remaining 5 cities while completing tech/policy for spaceship rush. Rome remains critical ally at 100/100.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> TURN 435 POST-SIPPAR: Existential crisis deepens. The Zulus have captured Sippar, puppeted it, positioned three Atomic Bombs and Stealth Bombers on our doorstep, and will win Global Hegemony in ~8 turns with 43/42 delegates. Flavors adjusted for total-war survival and maximum spaceship focus: Defense/CityDefense/Nuke/UseNuke at 100 — we must hold the remaining five core cities and authorize immediate nuclear strikes against Zulu concentrations to prevent further breakthroughs. Science/Production/Spaceship at 100 to pursue the only non-zero victory probability. Offense cut to 10 and Mobile to 70 since offensive operations cannot succeed before the vote. Wonder deprioritized entirely to 0. Rome remains at 100/100 relationship as our only surviving ally.

## Deepseek-3.2-Simple - Turn 469 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> The Netherlands is at 84% diplomatic victory; we must accelerate capture of Polynesian capitals (Honolulu, Assur) to achieve domination before they win. Increasing UseNuke and Nuke flavors prepares for nuclear strikes if conventional assault fails. Maintaining maximum Offense, Defense, Mobilization ensures continuous unit production. Science and Gold are critical for researching Stealth Bombers and purchasing units. Happiness offsets war weariness, and Espionage protects our science cities.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> We are in a critical endgame war while the Netherlands nears diplomatic and science victories. Our previous flavor profile had too many competing 100s, diluting the AI's focus. We narrow priorities to maximize breakthrough offensive power: atomic weapons, air superiority, rapid airlift reinforcement, and unit production are paramount. We lower less urgent flavors (defense, espionage, diplomacy, naval) to sharpen the staff's execution on conquering Polynesian and Dutch capitals before the World Congress decides the game.

## Kimi-K2.5-Simple - Turn 424 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Turn 423: Copenhagen siege in attrition deadlock while Denmark possesses Manhattan Project - nuclear deterrent capability is existential priority. Persepolis invasion stalled at 4% war score with Zone 1081 showing enemy dominance - need maximum Offense/Mobilization to force breakthrough before World Congress. Brazil's Apollo Program requires immediate preparation for transcontinental mobile warfare. Nuke/UseNuke increased to 100% given Manhattan Project race with Denmark. Production at 95 supports massive unit replacement for three-front war. Happiness at 100 critical as empire is at 55% happiness with extensive occupied territories.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Critical bottleneck is reserve deployment, not reserve size. Massive armies in Texcoco/Tlaxcala/Tenochtitlan must be airlifted to Copenhagen and Persepolis fronts immediately. Nuclear weapons program is existential: Denmark has Manhattan Project and Brazil fields 16k+ military with Apollo Program. Maxing Airlift, Nuke, UseNuke, Production, and Naval prioritizes city-breaking megatonnage and coastal invasion fleets for Rio de Janeiro. Science bumped to 90 accelerates Lasers after Satellites. Recon/NavalRecon reduced to 30 since the map is fully revealed. Diplomacy lowered to 40 as World Congress offers diminishing returns versus direct conquest of capitals.

## GLM-4.7-Briefed - Turn 433 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+5`

- Original: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> EMERGENCY: Netherlands at 42 delegates can win diplomatic victory in 9 turns (turn 442). Only way to stop them is military action against their protected city-states (Quebec City, Ife, Melbourne) - each provides +1 delegate. Offense increased (70) to prepare amphibious assaults. Nuclear readiness maximized (95/90) - atomic bomb available for strategic coercion of Netherlands or Denmark cooperation. Mobile (80) and Naval (85) maximized for rapid deployment to distant city-states. Production/Science/Spaceship kept maxed as backup victory paths. Diplomacy reduced to 50 as traditional diplomacy cannot stop Netherlands' delegate advantage. Strategic shift from holding Danish front to aggressive anti-Dutch operations.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 100 (Δ +10)
> Existential emergency: Netherlands will win diplomatic victory in 9 turns via Global Hegemony with exactly 42 delegates. Science victory is our only alternative win path, but we cannot outrace 9 turns unless we stop Netherlands first. Only feasible intervention: rapid military seizure of Dutch-allied city-states to strip delegates below 42 threshold. Flavors reoriented to extreme naval/amphibious/mobile offense for city-state strikes. Production/Mobilization maxed for emergency unit construction. Science/Spaceship/GP still high as fallback if delegate-stripping succeeds and we pivot back. Air/Naval/Ranged at extreme levels for intercontinental city-state bombardment. Defense/CityDefense reduced as homeland risk is secondary to preventing Dutch victory. Nuke/UseNuke at 100/90 as absolute last-resort deterrent if conventional city-state seizure fails. Gold reduced to 50, treasury is thin (209G) and we need production focus, not purchases. Diplomacy/Wonder/Expansion at 0 - no time for wonders or settlers. Happiness at 60 to prevent revolts during emergency conscription.

## Kimi-K2.5-Simple - Turn 392 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Manhattan Project COMPLETED in Karakorum - nuclear weapons now available! With peace treaties expired and Patriotic War policy active, immediately shifting to total war footing. UseNuke increased to 100 to ensure immediate atomic weapon employment once Nuclear Fission completes (12 turns). Offense and Mobile at 95/90 for twin assaults on Persepolis (Persia) and Washington (America). Air 100 prioritizes Heavy Bombers for atomic bomb delivery via Radar technology. Will fight two-front war against Autocracy powers while maintaining deception toward Order allies, particularly Korea. Science 100 critical for Advanced Ballistics nuclear missile delivery systems.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Manhattan Project complete and Nuclear Fission achieved. Grand strategy remains total conquest. Immediate offensives against Persia (local superiority 2:1) and America (join Russia's ongoing war, Washington has 17 wonders) are top priorities. Increased Naval/NavalRecon to 75/50 to support trans-oceanic invasions alongside Russian allies. Air remains maximum priority for Radar-unlocked Heavy Bombers. Nuke/UseNuke stay at 100/90 so atomic weapons deploy immediately upon uranium acquisition from captured Persian cities or corrected domestic mines. Science path continues through Radar to Advanced Ballistics.

## Kimi-K2.5-Simple - Turn 392 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Manhattan Project COMPLETED in Karakorum - nuclear weapons now available! With peace treaties expired and Patriotic War policy active, immediately shifting to total war footing. UseNuke increased to 100 to ensure immediate atomic weapon employment once Nuclear Fission completes (12 turns). Offense and Mobile at 95/90 for twin assaults on Persepolis (Persia) and Washington (America). Air 100 prioritizes Heavy Bombers for atomic bomb delivery via Radar technology. Will fight two-front war against Autocracy powers while maintaining deception toward Order allies, particularly Korea. Science 100 critical for Advanced Ballistics nuclear missile delivery systems.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> With Manhattan Project complete and active wars against Persia (now) and America (imminent as peace treaty expires), maximum offensive posture is required. Offense raised to 100 to break Persepolis and prepare for Washington. UseNuke increased to 90 to ensure nuclear deterrent readiness against Korea's 12k military—every turn of peace is precious but we must escalate instantly if deception fails. CityDefense raised to 80 to secure occupied Danish and Persian territory while field armies operate abroad. Grand strategy maintains heavy priority on Air (Heavy Bombers), Science (Advanced Ballistics path), Mobilization, and Production.

## Kimi-K2.5-Simple - Turn 452 - retry 2

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 95 => 100 (Δ +5)
> Turn 452: Critical survival situation - Byzantium at 40/44 delegates with World Congress voting in 1 turn. They just demonstrated nuclear aggression by nuking Madrid. Apollo Program completes next turn - must immediately pivot to maximum spaceship production. Increased Nuke flavor to 100 (from 95) and UseNuke to 95 (from 90) - need immediate nuclear deterrent capability given Byzantine nuclear attack and Mongol peace expiry. Production boosted to 95 (from 90) for rapid spaceship part construction after Apollo completes. GreatPeople to 85 for Great Engineer acquisition. All other priorities secondary to surviving long enough to complete science victory.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 95 => 100 (Δ +5)
> Turn 452: Apollo Program completes in 1 turn. Absolute priority shifts to immediate spaceship part construction and survival. Raising Production to 100 and GreatPeople to 100 so staff rush-build SS parts and generate Great Engineers for production hurrying. CityDefense and Antiair raised to 100 following Byzantine nuclear attack on Madrid—my cities face imminent existential nuclear threat from both Byzantium (demonstrated willingness) and Mongolia (Manhattan Project active). Raised Nuke/UseNuke to maximum deterrence with limited Uranium stockpile. Reduced non-critical Naval, Infrastructure, and Growth flavors to concentrate all resources on Science Victory sprint.

## Kimi-K2.5-Simple - Turn 393 - retry 3

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 393: Survival mode continues. Morocco massing Modern Armor, XCOM Squads, Heavy Bombers on border - 7.5x military advantage. Dutch Global Hegemony vote in 3 turns is likely unwinnable but must try block. As Maya vassal, only Science/Time victories possible. Nuclear Fission in 9 turns remains ONLY hope for deterrent. Slightly increased UseNuke to 85 and Antiair to 80 to prepare immediate atomic strike capability and counter Moroccan air superiority. Max Defense/Science/Espionage flavors. Spies positioned in Marrakech (1146) and Amsterdam (1218) for maximum tech theft.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Defensive survival mode persists against imminent Moroccan aggression. Increased CityDefense and Mobilization prioritize fortifications and unit output. Happiness raised to address St. Polten's severe -11 unrest. UseNuke pushed to 90 so atomic weapons are employed the instant Manhattan Project is viable. GreatPeople reduced since cultural victory is blocked by vassalage. Science/Production/Nuke remain maxed.

## Minimax-M2.5-Simple - Turn 395 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 70 (Δ +10), nuke 50 => 80 (Δ +30)
> With The Iroquois peacing out with Japan, Japan will concentrate their superior military (13162 vs 7035) entirely on our front. Conventional domination is no longer viable against this consolidation. We must pivot to Spaceship victory while using nuclear weapons as a force equalizer. Maintain strong city defense and anti-air to hold our 13 cities, prioritize science and production for spaceship components, and build the nuclear arsenal to deter Japanese offensives while spies steal key technologies.

## Deepseek-3.2-Simple - Turn 485 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> We are engaged in a multi-front war against superior forces. Increasing Ranged and Mobile ensures our bazooka and mechanized infantry production is prioritized for defense and counterattacks. Setting UseNuke to 100 guarantees we deploy nuclear weapons as soon as available to cripple The Huns' armies. Reducing Culture and Diplomacy reallocates focus to immediate military needs without compromising essential city-state relations (Monaco, Lisbon). Grand Strategy remains Conquest as nuclear strikes may enable capital captures, though we keep science victory as a backup.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 100 (Δ +10)
> With approximately 15 turns until the 500-turn limit, conventional domination is impossible against The Huns' overwhelming military. Our only remaining path to victory—or maximizing final score—is an emergency science push. Switching to Spaceship grand strategy prioritizes Apollo Program and SS part production while keeping strong Defense and Nuke deterrence. We deprioritize Offense, NavalRecon, Wonder, and Culture as conquest and tourism are no longer viable in the remaining turns.

## Deepseek-3.2-Simple - Turn 485 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> We are engaged in a multi-front war against superior forces. Increasing Ranged and Mobile ensures our bazooka and mechanized infantry production is prioritized for defense and counterattacks. Setting UseNuke to 100 guarantees we deploy nuclear weapons as soon as available to cripple The Huns' armies. Reducing Culture and Diplomacy reallocates focus to immediate military needs without compromising essential city-state relations (Monaco, Lisbon). Grand Strategy remains Conquest as nuclear strikes may enable capital captures, though we keep science victory as a backup.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 100 (Δ +10)
> Our military (6876) is drastically outmatched by The Huns (24473) and Mongolia (22278). Domination is no longer viable against these odds. We must pivot to a defensive science strategy: hold territory, rush nuclear weapons for deterrent, and pursue Spaceship victory while surviving the multi-front war. Reduced offense prevents suicidal attacks; maxed nukes and spaceship flavors prioritize the only viable long-term path to victory.

## Kimi-K2.5-Simple - Turn 373 - retry 1

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Adjusting for critical defensive phase. Reduced Growth from 85 to 75 to shift city production toward military units and nuclear infrastructure. Increased Naval from 65 to 75 and NavalRecon from 55 to 65 in response to Spanish Dreadnought and Destroyer attacks on our Ironclads near Assur (Zone -1069 shows enemy naval strength of 2171). Spanish naval pressure requires stronger counter-fleet to protect our coastal cities. Raised Production to maximum 100. Maintaining Defense/Antiair at 95 for paratrooper defense against Spanish airborne units, Science/Spaceship at 100 for victory timeline, Nuke at 100 for Manhattan Project completion in 6 turns, and UseNuke at 95. We must survive 18 turns until Nuclear Fission completes and can deploy nuclear deterrent.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Turn 373: Spanish Dreadnoughts left Assur at 20 HP and destroyed our Ironclad; naval threat to our exposed Sphere city-state demands immediate fleet buildup (Naval/NavalRecon raised). Manhattan Project finishes in 6 turns and Uranium quarries are now complete, making nuclear deterrence viable—with Spain at 5x our military strength, UseNuke raised to 100 for instant deployment once Nuclear Fission completes in 18 turns. Sippar at -13 happiness requires relief, so Happiness increased to 90 and Growth lowered to 80. Mobilization and Recon slightly raised for war readiness and intel on Spanish invasion staging through Rome.

## Kimi-K2.5-Briefed - Turn 373 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 90 => 100 (Δ +10)
> CRITICAL ADJUSTMENTS for Brazil tech lead (66-65): Espionage to 100 for maximum spy operations to steal techs and catch up. GreatPeople to 95 for more Great Scientists. Defense/CityDefense increased to 60/70 - Brazil may attack seeing their lead. Nuke/UseNuke at 100/95 - we need deterrent ASAP. Diplomacy up to 70 - must prioritize repealing sanctions to unlock trade. Science/Production/Spaceship remain 100. Gold reduced to 80 - focus on production over purchases. All military offense minimized - we cannot afford war.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 90 => 100 (Δ +10)
> Brazil's 66-65 tech lead and our critical aluminum shortage (need 1000g for Ottoman bulk purchase in ~4 turns) demand maximum gold accumulation and population growth. Raised Gold to 95 to prioritize GPT and treasury; raised Growth and Happiness to support more citizens for science output. Maintained Science/Production/Spaceship at 100. Maxed Nuke flavor to 100 for urgent deterrent production against Brazil's overwhelming military. Kept Espionage/GreatPeople high for tech stealing and scientist generation.

## Kimi-K2.5-Simple - Turn 391 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `-5`

- Original: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Nuclear weapons capability unlocked imminently; prioritizing UseNuke and Nuke flavors to 100 for immediate tactical nuclear strikes on Santiago/Murcia if uranium secured from Siam. Denmark upgraded to hostile for subsidizing Spanish victory - reduced Naval priority to 60 as coalition at sea fractured. Defense lowered to 80 to maximize offensive production. We have ~8 turns before World Congress votes on Passport System (+50% tourism) which would guarantee Spanish cultural victory. Must capture remaining Spanish cities immediately.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> TURN 390 - Spain remains at 7/7 influential civs; Santiago and Murcia must fall before Citizen Earth Protocol is completed. Austria's offensive against India confirmed (special forces and armor engaging near Delhi/Pataliputra), relieving our two-front pressure. Manhattan Project completes next turn and Uranium quarries are being constructed. Passport System vote in 7 turns is an existential threat - must be defeated. Maximum offensive focus maintained with slight adjustments: UseNuke raised to 90 for emergency authorization if conventional Santiago assault stalls. Science raised to 65 to accelerate Advanced Ballistics for nuclear missiles and spaceship backup. Spaceship raised to 40 as secondary contingency. Defense and Happiness slightly lowered to prioritize total war commitment.

## GLM-4.7-Briefed - Turn 433 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> EMERGENCY: Netherlands at 42 delegates can win diplomatic victory in 9 turns (turn 442). Only way to stop them is military action against their protected city-states (Quebec City, Ife, Melbourne) - each provides +1 delegate. Offense increased (70) to prepare amphibious assaults. Nuclear readiness maximized (95/90) - atomic bomb available for strategic coercion of Netherlands or Denmark cooperation. Mobile (80) and Naval (85) maximized for rapid deployment to distant city-states. Production/Science/Spaceship kept maxed as backup victory paths. Diplomacy reduced to 50 as traditional diplomacy cannot stop Netherlands' delegate advantage. Strategic shift from holding Danish front to aggressive anti-Dutch operations.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> Terminal emergency posture: Netherlands sits at exactly 42 delegates and wins diplomatic victory at turn 442 (~9 turns) via Global Hegemony. Traditional diplomacy cannot block a self-voting hegemon who already holds the threshold. We must simultaneously execute a military-denial strategy (naval/mobile/offense maxed to project force against Dutch assets and allies) while racing the spaceship alternative (science/production/spaceship maxed). Naval and mobile are prioritized because our fleet can reach Dutch coastal zones within 6-8 turns and mechanized forces are needed for rapid strikes. Diplomacy and gold are deprioritized because delegate math is already locked and our treasury is thin. Nuclear options remain at extreme readiness as last-resort deterrence. If we can strip even one Dutch ally-delegate, this buys critical time for the science victory.

## Kimi-K2.5-Simple - Turn 392 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> SURVIVAL MODE - GERMAN BETRAYAL RESPONSE: Germany's invasion is catastrophic. Reduced Offense to 40 (cannot attack superior forces), maintained Defense/CityDefense/Antiair at 100 to survive siege. Science 100 and Nuke/UseNuke 100 are existential priorities - atomic weapons only hope against 13k German military. Production 100 for emergency unit production. Espionage 100 to maintain Florence alliance and protect Kyzyl. Reduced Diplomacy to 90 (lost Lisbon/Sokoto/Buenos Aires to German coups). Naval reduced to 70 (coastal cities threatened by Germany). Focus: Hold cities, survive until nuclear deterrent operational.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> SPACESHIP SURVIVAL MODE: Conquest is impossible against Germany+France with 3:1 military strength. Switch to Spaceship grand strategy to prioritize science, production, and defensive infrastructure while rushing the tech tree toward nuclear deterrence. Max Defense/CityDefense/Air/Antiair/Production/Science/Nuke flavors for survival. Slash Offense and Mobile to stop wasteful assaults. Raise Happiness to 95 to combat severe 42% unhappiness combat penalty. Reduce Diplomacy to 60 since Lisbon/Sokoto/Buenos Aires are now German war proxies, but maintain rigging focus on remaining allies Kyzyl/Florence.

## Kimi-K2.5-Briefed - Turn 383 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CRITICAL WORKER REALLOCATION: Reduced Infrastructure from 100 to 20 to free the 7 Builders currently tied to railroad projects. Military briefing confirmed all workers occupied on railroads while 6 aluminum tiles remain unimproved despite TileImprovement 100. Aluminum crisis (-5/turn, 26 turns remaining) threatens Yamato production and bomber upgrades. Maintained TileImprovement 100 and Production 100 to prioritize aluminum mine construction once workers freed. Nuclear Fission completes in 6 turns - need Advanced Ballistics next for Nuclear Missile and Yamato. UseNuke increased to 100 to enable atomic strikes on Cusco immediately upon availability. AirCarrier 100 ensures carriers for Yamato deployment. Conquest remains correct grand strategy - Cusco is final capital for domination victory.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> INFRASTRUCTURE DEPRIORITIZATION: Military audit confirmed all 7 workers remain on railroads, leaving 6 aluminum tiles unimproved and zero forward airport construction. Slashing Infrastructure to 20 should free worker capacity for critical aluminum mines. Raising Mobile to 70 encourages mechanized ground rush toward Cusco since no Japanese city lies within 6-tile bomber range. Reducing Air/Airlift/AirCarrier reflects lack of forward staging bases; overwhelming land superiority (28449 vs 3581) makes direct ground assault viable. Offense and UseNuke maximized to exploit imminent Nuclear Fission completion and force immediate Inca capitulation.

## GLM-4.7-Briefed - Turn 450 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> IMMEDIATE ATHENS CONQUEST PREPARATION: Offense increased to 95, UseNuke to MAXIMUM (100) for Athens assault when peace treaty expires. Spaceship increased to 60 reflecting accelerated science victory path as backup (Nuclear Fusion research active). Diplomacy maxed at 100 for critical vote coordination with Ethiopia and Ottomans. MilitaryTraining at 100 ensures units upgraded and promotions ready for aggressive post-vote offensive. Greece has 48 delegates - if they win this turn, we IMMEDIATELY attack Athens to remove their 5 captured capitals and eliminate diplomatic victory threat. Nuclear weapons authorized if conventional assault stalls.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 450 Global Hegemony vote is existential. If Greece does not secure 45 support votes, immediate Athens conquest is mandated before they recover. Maximum offensive/military/production/gold flavors ensure post-vote blitz capability. Science maintained for edge, Espionage for city-state/counter-spying. Diplomacy kept moderate for coalition management. Nuclear release authorized at highest readiness.

## Kimi-K2.5-Briefed - Turn 396 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `-5`

- Original: use_nuke 65 => 80 (Δ +15), nuke 80 => 90 (Δ +10)
> ETHIOPIA CULTURAL VICTORY IMMINENT: Ethiopia has INFLUENCED ALL 7 CIVS and reached Order:3. They need only adopt CEP tenet and build it to win immediately. Switching to CONQUEST grand strategy with maximum mobilization (100) and offense (95). Naval (95) and Airlift (80) priorities enable rapid amphibious assault on Ethiopian coastal cities (Lalibela, Axum, Gondar) to destroy CEP before construction. Espionage (90) to accelerate Salem rig for delegate, but military solution is primary. All economy/culture deprioritized - this is existential war.

- Replay: use_nuke 65 => 70 (Δ +5), nuke 80 => 85 (Δ +5)
> CEP THREAT RESPONSE: Ethiopia confirmed at Order:3 with CEP capability imminent. Military briefing reveals zero transports queued and only 9 embarkable infantry despite active war with Ethiopia. Naval invasion capability must be accelerated immediately while maintaining Spaceship science path. Increased Naval/NavalRecon/Offense/Mobile/Air/AirCarrier to 85-95 to prioritize transport fleet, carrier battle groups, and amphibious assault forces. Reduced Defense/CityDefense to 45 to shift production toward offensive operations rather than garrison. Maintained Science/Spaceship at 95/90 because Science Victory remains Japan's only viable long-term win condition. Kept Diplomacy at 90 for critical Turn 404 coalition vote management. Nuke/UseNuke raised to 85/70 to maximize nuclear deterrent production rate once Manhattan Project unlocks after Nuclear Fission.

## GLM-4.7-Briefed - Turn 409 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> MULTI-THEATER EMERGENCY RESPONSE for Shoshone Cultural Victory (6 turns) and Treasury Crisis: Offense 95, Mobile 95, Nuke 100, UseNuke 100 - maximum priority on Shoshone disruption via nuclear/conventional assault in 6-turn window. Gold increased to 85 (from 70) - CRITICAL address of treasury exhaustion (~8 turns) through uranium sales + gem liquidation to survive until Manhattan completion. Defense reduced to 70 (from 75), CityDefense to 70 (from 80) - resources diverted from secondary holdings to Shoshone front. Diplomacy 95 (from 90) - enhanced priority on Carthage peace for delegate bloc and potential sanction relief. Science 100 maintained - fundamental for nuclear capability and keeping tech parity. This is all-hands-on-deck existential threat response.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 408 EXISTENTIAL ADJUSTMENT: Shoshone declared direct war with 30,471 military strength (1.7x our 17,732), accelerating cultural victory threat while simultaneously threatening territorial annihilation. Immediate pivot to MAXIMUM DEFENSIVE POSTURE to survive 6-turn cultural countdown: Defense raised to 95, CityDefense to 95 to prevent breakthroughs while nuclear deterrent prepares. Offense moderated to 80 to prevent overextension against superior force. UseNuke maxed to 100 to ensure immediate nuclear strike authorization when Manhattan Project/Advanced Ballistics complete. Gold elevated to 90 to address critical -242G/t treasury collapse (8-turn bankruptcy horizon). Production at 100 and Science at 100 maintain Manhattan/Advanced Ballistics sprint. Air at 95 preserves air parity. Grand strategy remains Conquest because only conquest of Shoshone cities or nuclear atrocities can halt cultural victory. Happiness 60 mitigates multi-war weariness accumulation. This is survival mode—not retreat, but structured defense while assembling nuclear retaliation capability.

## Kimi-K2.5-Simple - Turn 359 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FISSION RESEARCHED - Atomic Era begins! First priority is immediate Manhattan Project construction and Atomic Bomb production. Babylon has 11 Uranium and active Manhattan Project in Borsippa. Austria also racing with Manhattan Project in Vienna. Must strike Babylon first with surprise atomic attack while maintaining deception. Air 100 and Nuke 100 ensure immediate Bomber/Atomic Bomb production. Offense 95 prepares for post-nuclear blitz. Espionage 80 protects Nuclear Fission from theft. Deception with Babylon (Open Borders, DoF, Defensive Pact) MUST continue until first bombs complete.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Nuclear Fission researched; shift to maximum atomic war economy. Nuke and UseNuke at 100 rush Manhattan Project in high-production cities and atomic bomb construction. Offense and Air at 100 prioritize bomber delivery systems and conventional strikes. Science raised to 80 ensures Manhattan Project completion and tech superiority. Espionage at 80 protects Indian science cities from Babylonian spies and enables disruptive operations. Happiness at 75 addresses current empire unhappiness before it cripples war efforts. Spaceship at 70 keeps the science-victory parallel track alive. Naval raised to 70 supports coastal bombardment of Babylon's many seaside core cities.

## GLM-4.7-Simple - Turn 435 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Iroquois 97% Popular - cultural extinction in 3-4 turns. Maximum offensive posture required to capture Onondaga before cultural victory. Espoo Stealth Bomber complete provides immediate air strike capability. Linköping Stealth Bomber in 4 turns is too slow - must use existing air assets and conventional forces at Genesse River NOW. UseNuke 100 authorizes nuclear strikes if conventional forces cannot reach Onondaga in time. All production and resources prioritized for war. Diplomacy irrelevant when facing extinction - complete conquest or nothing matters.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Iroquois remains existential threat but requires one additional Autocracy tenet and Citizen Earth Protocol for cultural victory, giving us slightly more time than previously estimated. Maintain absolute Conquest priority with 100 Offense/Mobilization/Air/Production, but increase Spaceship and Science for science-victory hedging. Happiness pushed to 100 to lift empire from severe 47% unhappiness and combat penalties across 22 cities. Naval raised to 90 to dominate sea lanes between Genesse River/Kaunas and the Iroquois front, enabling rapid amphibious reinforcement. UseNuke raised to 95 in case Atomic weapons become available to shatter Onondaga's defenses.

## GLM-4.7-Simple - Turn 429 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> Maintaining UnitedNations grand strategy with defensive diplomatic posture. Adjusted Italy diplomacy: reduced hostility toward Portugal (now neutral) to seek accommodation while maintaining maximum defense; reset France to neutral as Order ideological peer with voting potential. Arsenal completes in 2 turns strengthening city defense. Electronics research ordered after Computers for Police Station and path to nuclear deterrence against Portugal's uranium advantage. Fraternity policy selected for +3 Food and +3 Science from connections, addressing Venice's health issues and supporting population growth. Flavor adjustments prioritize defensive survival, scientific progress toward nuclear weapons, and diplomatic engagement with Sweden and city-states.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> With Arsenal completing in 2 turns and Swedish coalition forces providing robust territorial defense via Cattaro and Corfu, slightly reduce maximum defense flavors to allow more economic focus. Increase Growth to 80, TileImprovement to 60, Infrastructure to 75, and WaterConnection to 75 to capitalize on Venice's massive unused trade route capacity (26 available). Boost Science to 95 to expedite Computers then Rocketry toward Nuclear Fission. Nuke/UseNuke increased to 85 since Uranium is now improved and Manhattan Project is complete, making nuclear weapons attainable within ~30-40 turns. UnitedNations grand strategy maintained.

## GPT-OSS-120B-Simple - Turn 344 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `-5`

- Original: use_nuke 90 => 100 (Δ +10), nuke 80 => 100 (Δ +20)
> Maximize our nuclear capabilities and carrier support to decisively strike Polynesian island forts, while maintaining our current aggressive conquest posture and strong production, gold, and happiness engines.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 80 => 95 (Δ +15)
> Maintain the Conquest grand strategy while sharpening focus on nuclear and scientific advancement to unlock decisive weapons against Polynesia’s island strongholds; reduce diplomatic investment since the diplomatic track is closed to us, and raise anti-air preparation for future enemy air power.

## GLM-4.7-Simple - Turn 411 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> EXISTENTIAL DEFENSE AGAINST RUSSIAN DIPLOMATIC DOMINANCE - UN vote in 10 turns with Russia at 95% victory (40 delegates vs blocking coalition 43). Maintaining UnitedNations grand strategy - abandoning now wastes diplomatic investment when Spain alliance (30 delegates) + my 13 + vassals 13 = 56 votes barely blocks Russia's 40. Just need to HOLD for 10 turns. Adjustments: Defense/CityDefense/Antiair +2 each (97) to prepare for Russian air/naval escalation (Jet Fighter produced). Production +5 (87) to accelerate factories, military academies, nuclear infrastructure after Workers' Faculties in 2 turns. Gold +5 (74) for emergency defensive purchases. Diplomacy +18 (100) maximum - urgency to maintain Spain alliance, potentially reposition spies. Science maintained at 100 - primary path to Nuclear Fission (4 turns) for atomic deterrent against Russia's 9x military advantage. Nuke/UseNuke remain 100 - nuclear development remains emergency priority. Air +5 (61) to counter Russian air superiority. Naval +5 (75) after destroyer loss to Russian submarines. Espionage +5 (95) for critical city-state election rigging counter-intelligence. Offense/Ranged/Mobile unchanged - no offensive capability against Russia's superior forces. Goal: SURVIVE 10 turns to block Russian diplomatic victory, accelerate nuclear deterrent as backup, strengthen defensive lines.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> While diplomatic blocking remains the immediate GrandStrategy, raising Spaceship to 70 directs staff to begin Apollo Program infrastructure after current queues, providing a viable alternate victory path since Russia already leads the space race. UseNuke increases to 90 because Nuclear Fission completes in 4 turns, and atomic weapons will be our only meaningful deterrent against Russia's overwhelming conventional forces. Espionage raised to 95 prioritizes counter-intelligence and spy-catching in response to confirmed Russian intelligence operations in Jenne and Truro, slowing their tech theft while we catch up.

## GPT-OSS-120B-Simple - Turn 344 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `-10`

- Original: use_nuke 90 => 100 (Δ +10), nuke 80 => 100 (Δ +20)
> Maximize our nuclear capabilities and carrier support to decisively strike Polynesian island forts, while maintaining our current aggressive conquest posture and strong production, gold, and happiness engines.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 80 => 90 (Δ +10)
> War weariness has reached 98% and happiness is at 50%. We must prioritize reaching the Atomic era for better units and potential nuclear options by boosting Science to 90, while maintaining Happiness at maximum. Adding Spaceship flavor provides a backup path if domination proves impossible against entrenched island fortresses. Reducing Recon from 95 to 30 reflects our mature map knowledge, and shifting some focus to Growth and Culture helps sustain the war effort and acquire needed policies.

## GLM-4.7-Simple - Turn 397 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> CRITICAL: Jeonju captured by Persia this turn. Defensive posture increased to absolute maximum (100) - Seoul zone under Persian attack with 7,216 enemy strength vs 3,637 friendly. Jerusalemdefense (100) and CityDefense (100) prioritized to protect remaining 3 cities. Mobilization (95) and Production (95) increased to rush defensive units (Mobile SAMs, Mechanized Infantry) and rebuild military. Offensive capability increased to 45 (from 30) - may need limited counteroffensive to push Persian forces back from Seoul. Naval decreased to 88 (from 92) - lost Jeonju naval base, focusing on land/air defense now. UseNuke increased to 90 (from 85) - existential threat justifies tactical nuclear response if Seoul or Busan threatened. Science (100) maintained - must continue spaceship progress despite war to achieve alternative victory. Diplomacy (60) - World Congress vote in 10 turns, focus on survival. Espionage (85) maintained - spies in Persian cities critical for technology recovery and intelligence.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> Jeonju has fallen to Persia (captured turn 397). Korea is reduced to 3 cities facing Persian military of 32,827. Existential defense remains absolute priority: Defense/CityDefense/Antiair stay at 100. However, Offense raised to 60 to enable urgent counterattacks to retake Jeonju and deny Persia a forward operating base against Busan/Seoul. Air increased to 95 as Stealth completes in 2 turns, unlocking Jet Fighters critical for air superiority over the peninsula. UseNuke edged up to 90—tactical nuclear strikes may be necessary to break Persian infantry concentrations if they threaten Seoul or Busan. Naval maintained at 92 to contest Persian battleships and fleet destroyers operating off the coast. Recon increased to 60 for better tactical visibility. Science/Production/Spaceship remain maximized; the science victory path is Korea's only long-term salvation, but survival comes first. Growth/Happiness/Espionage maintained to support the war effort and resource extraction.

## GLM-4.7-Simple - Turn 381 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-20`

- Original: use_nuke 50 => 85 (Δ +35), nuke 70 => 95 (Δ +25)
> Adjusted flavors to maximize Golden Age exploitation and multi-front war efficiency. Increased Mobile to 85 (from 80) to prioritize fast-moving Landships and upcoming Tanks for breakthrough operations during Golden Age. Increased Air to 85 (from 80) to expand Bomber coverage for all three fronts. Production raised to 95 (from 90)配合 Total War's +25% bonus for rapid unit buildup. Slight reduction in Naval (65) reflects need to focus on decisive land advances while maintaining sufficient coastal defense. UseNuke reduced to 40 (from 50) as nuclear capabilities are deterrent-focused. Maintaining high Offense (80), MilitaryTraining (85), Antiair (85) and Mobilization (50) for sustained warfare capability.

- Replay: use_nuke 50 => 55 (Δ +5), nuke 70 => 75 (Δ +5)
> Adjusting flavors to maximize Golden Age + Martial Spirit offensive window. Offense (+5), Ranged (+5), Mobile (+5), and Air (+5) prioritize decisive strikes while the combat bonuses last. Production (+5) compensates for sanction-related economic strain and sustains multi-front unit replacement. Science (-5) and Gold (-5) are slightly reduced as Atomic Theory is already in progress and trade route income is crippled by sanctions. Culture (+5) provides minor buffer against Polynesia's imminent cultural influence threat. Nuclear/Nuke flavors increased (+5 each) to prepare for imminent Atomic Era weapons. Grand strategy remains Conquest.

## Kimi-K2.5-Simple - Turn 403 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: CRISIS ESCALATION - Japan FLIPPED Salem using 2 Great Diplomats, stealing critical delegates. Now need 5 delegates (not 3) for diplomatic victory. Peace expired - war is now possible. Maximum military emergency posture: Offense/Mobilization/Air/UseNuke all at 100. Must either: 1) Rush final spaceship parts (Apollo completes in 4 turns), or 2) Nuclear strike Japan's Protocol cities if victory imminent. Increased Diplomacy to 60 for last push on Almaty (liberated, 43 vs Japan's 44) and Winchester.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: Japan flipped Salem to ally using Great Diplomats, completing the blockade of my diplomatic victory path. With only 39/44 delegates and 9 turns until voting, diplomatic victory is now virtually impossible. Japan is simultaneously building the Citizen Earth Protocol for imminent cultural victory. Immediate existential response required: maximum war mobilization (Offense/Mobilization/Naval/Air/Nuke/UseNuke all at 100) to annihilate Japan's Protocol-building cities with our newly completed atomic bomb and follow-up invasion, while maintaining Spaceship grand strategy so Onondaga completes Apollo Program in 4 turns as a backup victory path. Diplomacy flavor reduced to 20 since Salem, Malacca, and Winchester are unreachable.

## Kimi-K2.5-Simple - Turn 403 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: CRISIS ESCALATION - Japan FLIPPED Salem using 2 Great Diplomats, stealing critical delegates. Now need 5 delegates (not 3) for diplomatic victory. Peace expired - war is now possible. Maximum military emergency posture: Offense/Mobilization/Air/UseNuke all at 100. Must either: 1) Rush final spaceship parts (Apollo completes in 4 turns), or 2) Nuclear strike Japan's Protocol cities if victory imminent. Increased Diplomacy to 60 for last push on Almaty (liberated, 43 vs Japan's 44) and Winchester.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: Peace with Japan has expired. Japan flipped Salem and continues building Citizen Earth Protocol for imminent cultural victory. MAXIMUM WAR PRIORITY against Japan to stop Protocol. Boosting Air/Airlift/Naval/Mobile to 100 enables strike forces to reach Japanese territory via allied staging bases (Indonesia, Brazil). UseNuke raised to 100 to ensure the Atomic Bomb at Buffalo Creek is deployed tactically against Kyoto or Protocol cities. Science and Spaceship kept at 90 as urgent backup victory path. Diplomacy collapsed to 10—no time for city-state courting while Protocol threat looms.

## Kimi-K2.5-Simple - Turn 403 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: CRISIS ESCALATION - Japan FLIPPED Salem using 2 Great Diplomats, stealing critical delegates. Now need 5 delegates (not 3) for diplomatic victory. Peace expired - war is now possible. Maximum military emergency posture: Offense/Mobilization/Air/UseNuke all at 100. Must either: 1) Rush final spaceship parts (Apollo completes in 4 turns), or 2) Nuclear strike Japan's Protocol cities if victory imminent. Increased Diplomacy to 60 for last push on Almaty (liberated, 43 vs Japan's 44) and Winchester.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: CRISIS - Salem flipped to Japan, likely ending diplomatic path. Peace with Japan expired; total war is now the ONLY option to prevent Japanese cultural victory via Citizen Earth Protocol. Maximized Offense/Mobilization/Nuke/UseNuke/Air/Naval/Airlift to enable immediate strategic nuclear and conventional strikes against Japanese homeland. Maintained Spaceship/Science/Production as backup victory path. Must destroy Protocol-building cities at all costs.

## Kimi-K2.5-Simple - Turn 405 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 405 MAXIMUM EMERGENCY: Nuclear Fission priority increased to 100/100 - Manhattan Project completes in 2 turns, atomic bombs MUST be produced immediately. All offensive parameters at absolute maximum: 100 Offense/100 Mobilization/100 Mobile/100 Air/100 Nuke/100 UseNuke. Strike forces at Ecbatana/Kar-Tukulti-Ninurta must execute immediate conventional assault on Palenque/Chichen Itza while preparing tactical nuclear strikes. ZERO tolerance for peace. ONLY objective: capture Maya cities and halt Citizen Earth Protocol. Production 100 ensures rapid unit replacement. Espionage 70 continues spy operations in Maya cities.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 405 TOTAL WAR: The Maya are building Citizen Earth Protocol and we have 2 turns until Manhattan Project completion. Nuke and UseNuke raised to absolute maximum 100 to ensure immediate atomic production and tactical nuclear strikes against Palenque the moment tech allows. Espionage raised to 80 to maximize chances of spy sabotage against Maya production. Happiness increased to 100 to manage war weariness and unhappiness from newly hostile city-states (Zuunmod, Melbourne, Mombasa, Okilis) and occupied territories. Every ounce of production, air power, and mobility must be redirected to the swift capture of Palenque and Chichen Itza—failure means instant defeat.

## Kimi-K2.5-Simple - Turn 373 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 373: Nuclear Fission completed - we now have nuclear weapons for deterrence. War with Russia continues at +4% score (favorable). Major shift: reducing Offense to 25 (was 35) as we pursue defensive war only. UseNuke increased to 95 - we have actual nukes now and Russia is pushing into our territory. Reduced Espionage to 90 (was 95) - we have good network coverage. Increased Diplomacy to 90 (was 85) - World Congress vote in 7 turns for our World Ideology: Freedom proposal is critical. Must secure Korea (10 votes), Inca (9), and Babylon (16). Maintained maximum Science priority (100) - Korea overtook us 67-66, cannot afford to fall behind in tech race.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 373: Nuclear Fission complete, now have nuclear weapons. Russia pressing attack despite our tech edge. Need decisive counteroffensive to end war quickly so we can focus on science race with Korea (67 vs 66). Raised Offense to 50 and UseNuke to 95 for decisive action. Maintained Science/Spaceship at 100. Lowered Defense/CityDefense slightly as we shift to counterattack posture near Krakow and Warsaw.

## Deepseek-3.2-Simple - Turn 449 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `-5`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> Russia is nearing science victory (2 parts completed) and possesses overwhelming military strength (95k). We must increase nuclear readiness to potentially decimate Russian forces and cities, and begin preparing for science victory as a backup by raising Spaceship flavor to 30. All other flavors remain focused on total war: high offense, naval, air, and espionage to counter Russia's tech lead and military dominance.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> We are hemorrhaging gold (-1378 GPT) and cannot sustain current military production. Temporarily reducing Mobilization and Offense will shift city output toward wealth buildings and existing infrastructure, preventing economic collapse while our large established army (100/130 supply) still carries the war. Maintaining UseNuke at 90 and Nuke at 95 preserves nuclear deterrence against Russia's 95k military and their advancing spaceship program. Adding Spaceship 50 prepares a scientific contingency without diverting from the conquest path. Lowering Infrastructure/NavalGrowth/NavalTileImprovement to 30 cuts low-priority spending.

## Kimi-K2.5-Briefed - Turn 403 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `-5`

- Original: use_nuke 80 => 85 (Δ +5), nuke 80 => 90 (Δ +10)
> Post-Manhattan Project completion (Turn 399) with Turn 403 WC vote imminent. Reduced Offense from 15 to 10 as territorial expansion counterproductive to diplomatic win. Maintaining high Defense/CityDefense/Air/Antiair to protect Bregenz nuclear facility and core cities. Increased Nuke from 80 to 90 to prioritize atomic bomb production for deterrence (Iroquois 5883 vs 4502 strength ratio). UseNuke 85 reflects imminent atomic capability by Turn 405. Espionage 85 continues election rigging in Assur/Sogut against German influence. Diplomacy 100 and Gold 90 prioritize Assur delegate acquisition post-quest and future WC coordination. Science 85 drives Nuclear Fission for World Ideology proposal. Freedom bloc currently holds 59 delegates (Austria 29 + Germany 20 + Venice 10) vs 45 needed; maintaining solidarity while pursuing additional delegate sources.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> Manhattan Project complete and atomic deterrent operational. Slightly reduce static defense emphasis (Defense/CityDefense) to reflect reliance on nuclear deterrence against Iroquois forward positions. Increase UseNuke/Nuke to 85 to posture for atomic response if aggression thresholds are crossed. Raise Wonder priority to 40 in case United Nations construction is required to enable the World Leader vote following World Ideology: Freedom passage. Maintain Diplomacy 100 and Gold 95 to sustain the Assur influence campaign and city-state alliances. Moderately reduce Espionage to 85, shifting focus from prolonged election rigging toward economic growth and defensive infrastructure.

## Kimi-K2.5-Briefed - Turn 391 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> T391 CRITICAL PRODUCTION CORRECTION: Military briefing confirms AA-Gun production failed to start in Tarsus and Research Lab missing in Gordium despite defensive priorities. Reduce Offense 70→50 and Mobile 85→70 to focus AI bandwidth on critical infrastructure. Increase UseNuke 85→100 to ensure immediate atomic deployment upon Manhattan Project completion. Increase Espionage 75→85 to capitalize on successful Panama City election rigging and continued Hunnic/Siamese intelligence operations. Maintain all defensive, antiair, and nuclear production priorities at maximum.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> T391 CRITICAL FOCUS SHARPENING: Military Brief identifies AA-Gun production failed in Tarsus, Research Lab missing in Gordium, zero uranium mines started despite 21 stock, and Manhattan Project stalled. Current flavor profile has 12+ values at 90-100 causing critical dilution. Reduce non-essential flavors (Offense, Naval, Espionage, Recon, Diplomacy) to sharpen staff member prioritization on: Antiair/CityDefense/Production for Tarsus AA-Gun and western frontier; TileImprovement for uranium mine construction at (35,13), (42,18), (28,45), (30,27); Nuke/Science/Spaceship for post-Atomic Theory Manhattan Project and nuclear deterrent against 31,558 Hunnic military. Survival hinges on closing these specific infrastructure gaps before Hunnic mechanized units breach Harar-Pasargadae line.

## Qwen-3.5-Simple - Turn 389 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Final domination push configuration. Offense/Mobilization/Nuke at 100% for maximum military production and nuclear strike capability against Brazil/Babylon/Rome capitals. Air/Antiair at 100/95 to counter enemy bombers and maintain air superiority. Mobile/Ranged at 100/95 for mechanized infantry and bazooka pushes. Production/Science at 100% to sustain war machine and complete Nuclear Fission tree. Espionage at 90% to rig World Congress elections (9 turns remaining, we trail Brazil 16-17). Expansion/Wonder at 0% - no new cities needed, only conquest of remaining 3 capitals.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Final domination push intensifies. Tahiti captured (6 of 8 capitals). Brazil's sudden completion of the Manhattan Project demands immediate action—Rio de Janeiro must fall before atomic bombs can be deployed against our invasion stacks. UseNuke raised to 100 to ensure immediate nuclear strikes upon acquisition; AirCarrier increased to 60 to support carrier-based air operations against Rome/Babylon coastal defenses. Gold raised to 80 and Happiness to 85 to combat our -349 GPT deficit and stabilize newly conquered Polynesian/Brazilian cities. Science remains 100 for Nuclear Fission. All industrial and military output is directed toward the destruction of Rio de Janeiro, Rome, and Babylon.

## Qwen-3.5-Simple - Turn 389 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Final domination push configuration. Offense/Mobilization/Nuke at 100% for maximum military production and nuclear strike capability against Brazil/Babylon/Rome capitals. Air/Antiair at 100/95 to counter enemy bombers and maintain air superiority. Mobile/Ranged at 100/95 for mechanized infantry and bazooka pushes. Production/Science at 100% to sustain war machine and complete Nuclear Fission tree. Espionage at 90% to rig World Congress elections (9 turns remaining, we trail Brazil 16-17). Expansion/Wonder at 0% - no new cities needed, only conquest of remaining 3 capitals.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maximum aggression maintained for final domination victory (3 capitals remain: Rio, Rome, Babylon). CRITICAL SITUATION CHANGE: Brazil completed Manhattan Project on turn 389, meaning both Babylon and Brazil can now deploy atomic weapons. UseNuke raised to absolute maximum (100) - we must authorize immediate nuclear strikes on enemy capitals the moment we complete Nuclear Fission to prevent devastation of our core. Happiness raised to 85 to combat severe empire-wide unhappiness (45%) that is reducing combat effectiveness. Air/Antiair remain maxed to counter Brazilian and Babylonian air forces. Production/Mobilization at 100 to sustain the multi-front steamroll as our forces push into Rio de Janeiro and consolidate the Tahiti front after its capture. Science at 100 to complete Nuclear Fission before the enemy can exploit their Manhattan Project advantage. Espionage at 95 to manipulate remaining city-states and enemy capitals. No settlement, no civilian infrastructure - total war until all 8 capitals are controlled.

## GLM-4.7-Briefed - Turn 424 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 95 (Δ +0)
> URGENT RECALIBRATION: India Influential over 6/6 civs. Nuke/UseNuke maxed at 95 for immediate Great Works destruction via nuclear strikes when air superiority achieved. Air raised to 95 to achieve that superiority and conduct recon of Indian cultural sites. Antiair 80 counter potential Indian SAM sites. Offense/Mobile increased to 85/80 for aggressive India campaign while Greece distracts. Production/Science to 100 - PRIORITY for Apollo Program and spaceship parts racing India's potential final wonder. Espionage 95 to detect if India constructing Citizen Earth Protocol. Happiness 90 prevents war-weariness escalation during extended conflict if needed.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> India has achieved Influential status over all civilizations and threatens Cultural Victory within approximately 30 turns. We must simultaneously execute our Spaceship victory (Satellites next, then Apollo Program) while intensifying military pressure on India. Offense raised to 85, Mobile to 90, and Air to 95 concentrate forces for Indian city capture. UseNuke increased to 90 for tactical strikes if needed. CityDefense reduced to 10 reflects our offensive posture. Gold raised to 80 supports infrastructure purchases and unit upgrades. Science, Production, Spaceship, and Mobilization remain at 95.

## Kimi-K2.5-Simple - Turn 410 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CATASTROPHIC situation: Rome captured Zuunmod, gained 5th capital (50% of domination victory). Modern Armor and Helicopter Gunships penetrating my territory. Barcelona's Atomic Bomb completes in 3 turns - this is my only deterrent. Maximum defensive posture essential. Prioritize Nuke/UseNuke to 100 - nuclear weapons are the only thing that can stop Rome's overwhelming conventional force. Maintain Production and Science for SSC components if I survive. Salamanca at 39% health requires emergency defense.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Absolute defensive posture maintained with Zuunmod fallen and Rome at Salamanca's doorstep. UseNuke increased to 100 to ensure immediate atomic weapons deployment when Barcelona's bomb completes in 3 turns. Espionage to 100 for maximum counter-intelligence. Offense reduced to 0 to prevent suicidal attacks. TileImprovement raised to 60 for infrastructure repair. Survival depends on holding core cities until nuclear deterrent is operational.

## Kimi-K2.5-Simple - Turn 410 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CATASTROPHIC situation: Rome captured Zuunmod, gained 5th capital (50% of domination victory). Modern Armor and Helicopter Gunships penetrating my territory. Barcelona's Atomic Bomb completes in 3 turns - this is my only deterrent. Maximum defensive posture essential. Prioritize Nuke/UseNuke to 100 - nuclear weapons are the only thing that can stop Rome's overwhelming conventional force. Maintain Production and Science for SSC components if I survive. Salamanca at 39% health requires emergency defense.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Rome captured Zuunmod this turn, exposing Santiago and Salamanca to direct assault. Atomic weapons arrive in 2-7 turns; UseNuke raised to 100 to ensure immediate nuclear strikes against Rome's stacks to break their offensive. Happiness increased to 100 to manage severe war weariness and occupation penalties. Infrastructure boosted to 100 to rush road connections and trade route income desperately needed to prevent bankruptcy at -125 GPT. Mobilization slightly increased to prioritize military production, while Spaceship and Growth slightly reduced to focus entirely on survival and deterrent rather than long-term science expansion.

## GLM-4.7-Simple - Turn 407 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Spaceship victory focus with maximum defense against superior enemies (Poland 40K, Celts 16K, Spain 26K vs Iroquois 5K). Increased UseNuke to 90 - captured Polish territory and recent Celtic aggression justify nuclear deterrent. Adjusted Naval to 65 - important for defending coastlines from Spain/Celts/Poland fleets. Science 100 for Apollo and spaceship parts. Defense/CityDefense/Mobilization 100 - survival priority. Growth 60 for specialist support. Diplomacy 80 for World Congress in 4 turns (10 delegates). Offense reduced to 5 - preserve limited forces.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> The successful capture of Katowice demonstrates we can exploit weak points, warranting a modest increase in Offense. Poland's Atomic Bomb demands a maximal nuclear deterrent upon completion of Advanced Ballistics, so UseNuke is raised. Meanwhile our -72 GPT deficit jeopardizes unit upgrades and supply, so Gold priority is increased to stabilize finances under sanctions.

## Deepseek-3.2-Simple - Turn 428 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> We are in the final stages of domination victory. Our immediate targets are Spanish capitals Madrid and Cordoba, which require nuclear bombardment followed by ground assault. We must prioritize nuclear production (Nuke/UseNuke at 100) and naval/air supremacy to project power across oceans. Maintaining high production, gold, and science ensures we can continuously build military units and upgrade our forces. Diplomatic and espionage flavors secure our city-state alliances and intelligence on enemy movements. Zero expansion/wonder focus as we are in total war mode.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> Brazil is eliminated, freeing our entire southern front to focus on Spain and The Aztecs. We just completed two new Atomic Bombs and must maximize nuclear aggression. We raise Happiness to 90 to manage mounting occupation unhappiness in newly captured Brazilian and French cities. We maintain maxed naval/air/production/economic flavors to sustain the total war machine: crush Spain first (capture Madrid), then pivot to Aztec capitals. Conquest grand strategy remains absolute.

## Kimi-K2.5-Briefed - Turn 473 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> WC VOTE CRISIS + NUCLEAR DETERRENT: Diplomacy maxed to 100 to ensure immediate completion of Utica tribute quest from Riga (securing +3 critical delegates before WC vote). Nuke/UseNuke at 100 for immediate deterrent deployment once platform acquired. Science/Spaceship/Production maintained at high priority for Apollo catch-up after WC resolved. Naval increased to 60 for Battleship/Carrier construction as nuclear platform. Reduced Culture/Religion/Wonder to minimum to focus resources on existential priorities.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> WC VOTE INSURANCE + SUBMARINE RUSH + APOLLO CATCH-UP: Increase Diplomacy 60→85 to prioritize Utica tribute quest completion (Demand Tribute from Riga) for the only achievable +3 delegate flip before the WC vote. Boost Naval 30→65 to rush a nuclear Submarine (5-aluminum delivery platform) alongside Nuke 100 and UseNuke 95 for immediate deterrent credibility. Maintain Science/Spaceship 100 and Production 90 for spaceship part production after Spaceport. Gold 70→80 enables aluminum buyback from Shoshone and emergency part purchases. Antiair 70→80 fills the Tours AA gap. Reduce secondary flavors (Infrastructure, Culture, Espionage) to sharpen macro focus without diluting critical priorities.

## Deepseek-3.2-Simple - Turn 428 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `-5`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> We are in the final stages of domination victory. Our immediate targets are Spanish capitals Madrid and Cordoba, which require nuclear bombardment followed by ground assault. We must prioritize nuclear production (Nuke/UseNuke at 100) and naval/air supremacy to project power across oceans. Maintaining high production, gold, and science ensures we can continuously build military units and upgrade our forces. Diplomatic and espionage flavors secure our city-state alliances and intelligence on enemy movements. Zero expansion/wonder focus as we are in total war mode.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 95 (Δ +0)
> Our atomic bombs are now online with more in production across multiple cities. We must maintain absolute focus on annihilating Spanish cities and securing the Madrid and Cordoba capitals. Maximizing nuclear usage probability ensures we crack heavily defended coastal targets quickly. Raising AirCarrier priority prepares us for the Carriers unlocked by Computers to project our Heavy Bombers and Fighters across oceans. Spain is the immediate and vulnerable target; The Aztecs can wait until after Spain falls.

## Qwen-3.5-Simple - Turn 484 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: CRITICAL - Iroquois declared war on us along with 4 city-state allies (Kabul, Venezia, Prague, Samarkand). We face 5+ enemies simultaneously with military severely outnumbered (our 1,139 vs Iroquois 41k, Ottomans 12k, Aztecs 9k). Maintaining maximum Defense/Mobilization for survival. Nuke flavors at 100% - need nuclear deterrent against overwhelming forces. Iroquois at 46 delegates (needs 43) with 16 turns remaining - existential diplomatic threat. Must conquer their city-state allies to flip delegates while defending our cities. Germany (15) + Mongolia (15) alliance critical to block Iroquois World Congress proposals.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: Existential defensive crisis. Military 1,139 vs surrounding enemies (Iroquois 41k, Aztecs 9k, Ottomans 12k, Germany 6k). Reduce Offense to 5 to stop suicidal attacks; max Defense/CityDefense/Mobilization/Antiair/Ranged/UseNuke. Drop Air to 15 (no oil), Naval to 5 (irrelevant), Wonder to 0. Reduce Diplomacy to 40 (city-state alliances nearly impossible while sanctioned and at war with most). Prioritize Production/Science/Happiness for survival and nuclear deterrent.

## GLM-4.7-Simple - Turn 435 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Iroquois 97% Popular - cultural extinction in 3-4 turns. Maximum offensive posture required to capture Onondaga before cultural victory. Espoo Stealth Bomber complete provides immediate air strike capability. Linköping Stealth Bomber in 4 turns is too slow - must use existing air assets and conventional forces at Genesse River NOW. UseNuke 100 authorizes nuclear strikes if conventional forces cannot reach Onondaga in time. All production and resources prioritized for war. Diplomacy irrelevant when facing extinction - complete conquest or nothing matters.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Iroquois 3 turns from cultural victory. Total naval commitment is only hope: Kaunas amphibious fleet must sail through Szczecin corridor and assault coastal Onondaga immediately. Land forces are too distant. Strip all civilian priorities to 0. Raise Naval/NavalRecon/AirCarrier for maximum sea assault. UseNuke 95 for eventual atomic bombing of Onondaga once available. Science 20 sufficient with current tech lead.

## Kimi-K2.5-Simple - Turn 457 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FIRST-STRIKE PREPARATION: Manhattan Project completes in 2 turns. Denmark at 7/8 capitals (87.5% domination) - will win game if they capture 1 more capital. Spain's only hope is surprise nuclear attack the moment first Atomic Bomb is ready. Maximized Nuke/UseNuke/Production/Mobilization flavors to prepare for immediate atomic weapon production and deployment. Defense/Antiair high to survive Danish air superiority until then. All other priorities secondary to nuclear deterrent.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Existential triage: Denmark holds 7/8 capitals and Global Hegemony votes in 10 turns. Our only hope is achieving nuclear weapons before annihilation or diplomatic defeat. Manhattan Project completes in 2 turns, but Nuclear Fission lags at 13 turns. Science and Growth maximized to compress the research timeline via population/beakers. Production and Nuke/UseNuke at emergency levels ensure immediate atomic weapons rollout the instant the tech is secured. Culture/Wonder/Religion/Diplomacy gutted to 0-5—all resources must flow toward survival and the bomb.

## Kimi-K2.5-Simple - Turn 390 - retry 3

**Deviation (replay vs original):** use_nuke `-15`, nuke `+5`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> Emergency defensive posture with nuclear deterrent imminent. Greece's 3:1 military superiority and diplomatic victory attempt in 6 turns creates existential crisis. Nuclear Fission completes in 1 turn with 14 uranium ready. Maximize UseNuke (100) for immediate atomic deployment. Maintain Defense/CityDefense/Mobilization at 100 to survive until deterrent operational. Reduce Naval from 95 to 85 as American destroyer threat is severe but manageable. Boost Espionage to 100 to protect science cities and maintain election rigging in Enns. Increase Spaceship to 95 as backup victory path if culture is disrupted. Diplomacy raised to 80 to counter Greece's 34 delegates in upcoming World Congress vote on United Nations proposal.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> Consolidating flavors to prioritize cultural victory acceleration while maintaining existential defensive posture against Greece's 3:1 military superiority. Deprioritize Spaceship from 90→30 since tourism victory is primary path with America 4 turns from Influential. Boost Culture to 95 and GreatPeople to 95 to rush hotels, great works, and musician infrastructure for the final push against Greece. Raise Nuke to 95 and UseNuke to 85 to prepare staff for immediate atomic deployment once Nuclear Fission completes. Reduce Religion to 70 and Happiness to 85 since faith generation is already strong and happiness stable at 82%. Maintain Defense/Mobilization/CityDefense at 100 and keep Naval high to counter American aggression.

## Qwen-3.5-Simple - Turn 484 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: CRITICAL - Iroquois declared war on us along with 4 city-state allies (Kabul, Venezia, Prague, Samarkand). We face 5+ enemies simultaneously with military severely outnumbered (our 1,139 vs Iroquois 41k, Ottomans 12k, Aztecs 9k). Maintaining maximum Defense/Mobilization for survival. Nuke flavors at 100% - need nuclear deterrent against overwhelming forces. Iroquois at 46 delegates (needs 43) with 16 turns remaining - existential diplomatic threat. Must conquer their city-state allies to flip delegates while defending our cities. Germany (15) + Mongolia (15) alliance critical to block Iroquois World Congress proposals.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: Pure defensive survival posture against overwhelming multi-front assault. Germany attacking Nimrud (45% health), Aztecs pressing eastern flank, Iroquois declared formal war. Offense minimized to preserve units; maximum city defense, air superiority, anti-air coverage, and nuclear deterrence. Science and gold deprioritized vs immediate military production. Maximum espionage flavor to accelerate spy networks in Ottoman/Iroquois capitals for sabotage and intelligence.

## GLM-4.7-Simple - Turn 409 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> Japan's naval devastation this turn requires maximum defensive posture. Antiair 100, Nuke/UseNuke 100 - nuclear deterrence and air defense are now survival priorities. Naval 85 (from 75) - rebuilding after 4 capital ship losses. Defense 98, CityDefense 100 - Japan bombarding our cities from coastal waters. Production 95, Mobilization 98 - rapid unit replacement critical. Science 90 - must accelerate research gap (Japan 69 techs vs our 64). Gold 85 - fund upgrades and maintain military at 3x disadvantage.

- Replay: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> Japan destroyed our Dreadnought, Artillery, and Destroyer this turn while capturing territory near Casablanca and Huari. We are in an existential defensive war but must retain limited counter-offensive capacity, especially against Indonesia where our war score is +14%. Raising Air to 100 prioritizes Fighters and Heavy Bombers from Radar. Raising Naval to 85 and Mobile to 80 improves our ability to respond to Japan's combined arms. Reducing Happiness to 70 reflects wartime austerity. Spaceship nudged to 30 as a distant insurance policy. Defense, CityDefense, Mobilization, Production, Science, and Antiair remain at prior wartime levels.

## Kimi-K2.5-Briefed - Turn 435 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 434 CULTURAL DEFENSE MAXIMUM: India at 93% influence - this is existential crisis. Culture 100, GreatPeople 100, Espionage 95 to deploy spies in Indian cities for maximum tech theft and disruption. Science 90 to rush Rocketry for nuclear missiles. Defense/Mobilization increased to 95/85 for survival against Russia while focusing on India threat. Nuke/UseNuke at 100 - prepare nuclear deterrent and potential first strike if war declared.

- Replay: use_nuke 95 => 90 (Δ -5), nuke 95 => 90 (Δ -5)
> TURN 434 SCIENCE VICTORY PIVOT: India cannot achieve cultural victory for approximately 69 turns—still needs Russia. Our best remaining victory path is Science. GrandStrategy set to Spaceship. Science 100 and Spaceship 90 to prioritize research and spaceship components. Maintain Defense 85, Nuke 90, UseNuke 90, and Mobilization 75 to hold Russia's superior military at bay while teching. Reduce Culture from 100 to 70 to reallocate resources; culture remains strong enough to slow India's progress but is no longer the primary focus. Espionage 80 continues supporting technology theft and counterintelligence.

## GPT-OSS-120B-Simple - Turn 344 - retry 1

**Deviation (replay vs original):** use_nuke `-15`, nuke `-15`

- Original: use_nuke 90 => 100 (Δ +10), nuke 80 => 100 (Δ +20)
> Maximize our nuclear capabilities and carrier support to decisively strike Polynesian island forts, while maintaining our current aggressive conquest posture and strong production, gold, and happiness engines.

- Replay: use_nuke 90 => 85 (Δ -5), nuke 80 => 85 (Δ +5)
> Locked in a grinding war with Polynesia at 98% war weariness, we need faster military technology to break the Honolulu stalemate while keeping our economy intact. Slightly moderating Offense and CityDefense prioritizes tech acceleration without sacrificing the island campaign. Nuclear and espionage capabilities remain high to exploit any breakthrough.

## Kimi-K2.5-Briefed - Turn 382 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `-5`

- Original: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> EMERGENCY DIPLOMATIC RECOVERY: The city-state flipping operation failed to execute. With only 36 delegates and 5 turns until World Congress vote, I need maximum Diplomacy (100) and Gold (100) to execute immediate city-state purchases. Reduced Mobilization to 40 and Offense to 15 to free supply and focus on defensive deterrence. Increased Nuke/UseNuke to 95/80 as deterrent against Russian aggression while I secure delegates. Defense/Antiair remain at 90 for Russian containment. Must acquire 8+ delegates before vote or World Ideology: Order will fail.

- Replay: use_nuke 75 => 70 (Δ -5), nuke 90 => 90 (Δ +0)
> PIVOT TO SCIENCE VICTORY: The diplomatic path is currently blocked because Russia's enacted Sphere of Influence resolutions make four critical city-states permanently allied to them, preventing us from reaching the 44-delegate threshold through gold alone. Switching Grand Strategy to Spaceship reorients staff toward science, production, and food priorities required for a space race. Diplomacy is reduced to 20 and Gold to 60 to stop wasteful city-state spending that cannot overcome sphere locks. Spaceship (100) and Science (90) are maximized to rush the Information Era and spaceship components. Defense (90), Antiair (90), and Nuke (90) remain high to contain Catherine until nuclear deterrence is operational in roughly 8 turns. Production (80), Infrastructure (65), and Growth (70) ensure our 23 cities can support the industrial and population demands of the Apollo Program and later parts.

## GLM-4.7-Simple - Turn 421 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CRITICAL ADJUSTMENT for Shoshone nuclear threat: Offense 100 - maximum aggression to capture Moson Kahni and eliminate nuclear weapons before launch. UseNuke raised to 100 - potential preemptive strike required given Shoshone ACTIVE atomic bomb in play. Naval 100 - France lost Fleet Destroyer this turn to Shoshone, need naval supremacy immediately. Antiair 100 - Shoshone Heavy Bombers/Fighters must be countered to protect ground advances. Nuke 100 - must stockpile nuclear counter-deterrence. Defense reduced to 65 - full offensive posture required. Gold 90 - funding critical upgrades and mobilization. Science 100 - Satellites and military technology urgent. Flavors optimized for rapid conquest of Shoshone nuclear and cultural infrastructure.

- Replay: use_nuke 95 => 90 (Δ -5), nuke 100 => 100 (Δ +0)
> Shoshone completed an Atomic Bomb and has 4/5 civs culturally influenced. The window for conventional victory is narrowing. France must accelerate offensive operations against England to secure London, then pivot all force toward Shoshone before they can achieve cultural or scientific victory. Reduced naval emphasis reflects Shoshone's fleet superiority in the Palatium theater; reliance shifts to land-based air power and carriers. Slightly reduced UseNuke acknowledges mutual nuclear capability, reserving atomic weapons for decisive strategic targets rather than tactical battlefield use. Maximum offensive priority is maintained.

## Kimi-K2.5-Simple - Turn 439 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> FINAL EMERGENCY: World Congress in 4 turns. Austria has 45/40 delegates. Offense reduced to 10 and Mobile to 10 to COMPLETELY STOP attacking The Inca. Defense at 95 for self-protection only. UseNuke at 100 to signal willingness to escalate and force peace negotiations. Maximum Production/Air/Nuke maintained for potential final strike against Austria if The Inca succeeds at Attila's Court. The ONLY priority is ensuring The Inca captures Attila's Court - every Assyrian unit should withdraw from Inca contact and let them pass north to The Huns.

- Replay: use_nuke 95 => 90 (Δ -5), nuke 100 => 100 (Δ +0)
> TURN 438: Switching Grand Strategy from Conquest to Spaceship to signal long-term scientific focus and remove offensive war incentives against The Inca. Setting Offense to 0 and Mobile to 0 to absolutely halt the counterproductive war, while maxing Defense (100) and CityDefense (80) to consolidate against the real threat: Austrian forces pushing near Nasca (zone 14230) and Atico (zone 17205). Maintaining Production (100), Mobilization (90), Air (90), and Nuke (100) for the Austrian front. Elevating Spaceship (80) and Science (80) to accelerate SS part production if the Global Hegemony vote unexpectedly fails to elect Austria. With only 4 turns until the World Congress vote, every unit must stop fighting The Inca and prepare for either blocking Austria or racing for an alternative victory.

## Kimi-K2.5-Simple - Turn 395 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Critical survival mode: Austrian military strength increased to 25,518 (6.8:1 ratio) with peace treaty expired. Reduced Offense to 0 to stop wasting resources on Polynesian war - need immediate consolidation. Maintained Defense/Mobilization/Nuke at maximum for existential defense. Increased Spaceship to 70 as backup victory path. Espionage at 100 to steal technologies from Austria. We have 7 turns to achieve Influential with Babylon for Cultural Victory while surviving Austrian onslaught. Nuclear deterrence is our only hope.

- Replay: use_nuke 95 => 90 (Δ -5), nuke 100 => 100 (Δ +0)
> Approximately 15 turns remain before Austrian peace expires; we are 7 turns from Influential with Babylon. Maintain Culture grand strategy to complete the Babylon influence and keep pressuring Austria, but maximize existential survival flavors: 100 Defense/Mobilization/CityDefense/Nuke/Air/Antiair/Science/Espionage. Spaceship at 85 ensures we begin production on the SS Booster immediately after Advanced Ballistics completes as a credible backup victory. Espionage at 100 prioritizes counter-intelligence against Austrian spies currently stealing from our cities. Offense minimized; this is total defensive mobilization.

## Kimi-K2.5-Briefed - Turn 446 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `-5`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> Spain's bankruptcy imminent (Turn 448) with -3,897 GPT but war continues - maintain maximum Defense 100, UseNuke 90 for credible second-strike against potential desperate Spanish air offensive pre-deletion. Critical adjustment: Production 95 prioritizes Solar Plants in St. Petersburg/Yaroslavl' (coastal desert cities) and Aluminum Mines on 16 unimproved tiles for spaceship resource security. Science 100 and Spaceship 100 unchanged - cannot win conventional war, only outpace to space. Reduced Gold 50 (was 70) - post-bankruptcy peace will enable trade route recovery with Morocco and potentially others via Cold War repeal.

- Replay: use_nuke 85 => 80 (Δ -5), nuke 95 => 90 (Δ -5)
> Spain's imminent bankruptcy degrades its air/nuke threat; moderately lower defensive flavors while sharply increasing happiness (critical 35%), gold (Morocco trade/oil loss), infrastructure and tile improvement (aluminum mines/Solar Plant gaps per economy brief). Prioritize production, spaceship, and science flavors for post-Satellites victory acceleration.

## Deepseek-3.2-Simple - Turn 445 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `-40`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximizing UseNuke to 100 ensures our atomic bombs and future nuclear missiles are used aggressively against The Celts' military concentrations and cities, given their overwhelming advantage. Maintaining high Air, Naval, and Nuke flavors sustains our technological edge and production focus. Diplomacy and Espionage at 100 are critical for city-state alliances and spy missions to gain delegates for diplomatic victory. Gold and Science remain top priorities to fund our war effort and tech progression. Other military flavors are tuned for a multi-front defensive-offensive war against The Celts, Germany, and Ethiopia.

- Replay: use_nuke 90 => 80 (Δ -10), nuke 100 => 60 (Δ -40)
> Reduced Nuke and UseNuke flavors because we have no Uranium available to construct Nuclear Missiles, though we will still aggressively use existing Atomic Bombs. Slightly lowered Naval/Air while maintaining strong values to defend against The Celts' XCOM, Stealth Bomber, and naval incursions. Raised CityDefense to 85 to counter paradrops. Keeping Gold, Science, Diplomacy, and Espionage at maximum to fuel city-state influence purchases and spy operations for our diplomatic victory push. UnitedNations grand strategy remains our only viable victory path against The Celts' 33% completed spaceship and dominant tourism.

## Kimi-K2.5-Briefed - Turn 403 - retry 1

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 80 => 85 (Δ +5), nuke 80 => 90 (Δ +10)
> Post-Manhattan Project completion (Turn 399) with Turn 403 WC vote imminent. Reduced Offense from 15 to 10 as territorial expansion counterproductive to diplomatic win. Maintaining high Defense/CityDefense/Air/Antiair to protect Bregenz nuclear facility and core cities. Increased Nuke from 80 to 90 to prioritize atomic bomb production for deterrence (Iroquois 5883 vs 4502 strength ratio). UseNuke 85 reflects imminent atomic capability by Turn 405. Espionage 85 continues election rigging in Assur/Sogut against German influence. Diplomacy 100 and Gold 90 prioritize Assur delegate acquisition post-quest and future WC coordination. Science 85 drives Nuclear Fission for World Ideology proposal. Freedom bloc currently holds 59 delegates (Austria 29 + Germany 20 + Venice 10) vs 45 needed; maintaining solidarity while pursuing additional delegate sources.

- Replay: use_nuke 80 => 70 (Δ -10), nuke 80 => 90 (Δ +10)
> Post-Manhattan Project rebalancing to secure diplomatic victory window. Culture raised to 60 to accelerate Level 3 Freedom tenet Containment (17 turns), unlocking critical +2 influence/turn and ~+9 delegates toward 45-vote threshold. Nuke increased to 90 to prioritize Atomic Bomb production at Bregenz as operational deterrent against Iroquois. UseNuke moderated to 70 to maintain credible deterrence without premature tactical deployment while corridor strength remains below 3,500 threshold. Spaceship reduced to 20 to deprioritize non-pathway. Wonder raised to 35 for potential United Nations construction once World Ideology: Freedom passes. Production and Mobilization elevated to support nuclear arms and defensive infrastructure. Science adjusted to 85 while culture and production take urgent priority.

## Kimi-K2.5-Briefed - Turn 335 - retry 2

**Deviation (replay vs original):** use_nuke `-80`, nuke `-80`

- Original: use_nuke 30 => 100 (Δ +70), nuke 40 => 100 (Δ +60)
> NUCLEAR EMERGENCY - BRAZIL WINS IN 4 TURNS: Maximum crisis flavors. Nuke/UseNuke 100 for instant strike capability if we have any. Espionage 100 to steal Great Works or disrupt Brazil. Diplomacy 100 for emergency resource trades. Gold 90 to buy anything available. Production 100 for immediate unit building if we get Coal. Airlift 80 for rapid deployment. Defense reduced to 20 - we need OFFENSE to survive. This is Hail Mary time.

- Replay: use_nuke 30 => 20 (Δ -10), nuke 40 => 20 (Δ -20)
> MAXIMUM ESPIONAGE AND NAVAL MOBILIZATION: Brazil likely still needs additional Order tenets and Citizen Earth Protocol before actual cultural victory, giving us a ~15-30 turn window rather than 4 turns. Fleet transit requires 7-8 turns; backstabber penalty expires in 8 turns. Espionage raised to 100 to prioritize Great Work theft from Brazilian cities and disrupt their tourism network immediately. Naval, Offense, Mobilization, and Production at maximum to build and position invasion force. Maintain Open Borders with Brazil to allow fleet positioning inside their waters before war declaration on turn 343. Diplomacy and Gold prioritized to secure Coal from Portugal/Spain/Assyria for additional Treasure Ships.

## Kimi-K2.5-Simple - Turn 372 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximum aggression maintained against Carthage (100% war score, 4% weariness) while responding to India's new Manhattan Project threat. UseNuke increased to 100 - must deploy atomic weapons immediately upon acquiring Nuclear Fission to counter India's nuclear capability. Satellites/Spaceship flavors at 95 ensure Science Victory backup. Continue prioritizing T-34 tanks, stealth bombers, and heavy bombers to eliminate Carthage's cities before they can deploy their 5 uranium reserves. Naval and Air strengths maintained for coastal bombardment of Carthage and defense against Indian naval aggression.

- Replay: use_nuke 90 => 80 (Δ -10), nuke 100 => 100 (Δ +0)
> India's completion of the Manhattan Project and Carthage's uranium reserves at Susa make nuclear parity an immediate strategic imperative. Raising Wonder priority to 75 ensures the Manhattan Project is queued and completed rapidly, while deprioritizing Spaceship to 0 redirects all production from science-victory components to the active war effort. Naval and NavalRecon are reduced because the decisive campaigns against Carthage and India are land-based, and Espionage is slightly lowered since our spy networks are already well-embedded. Offense, Mobilization, Nuke, Air, and Antiair remain paramount to maintain overwhelming pressure on Carthage while the Global Warworlds proposal delivers its impending +25% attack bonus.

## Kimi-K2.5-Simple - Turn 392 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-15`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Nuclear Fission complete - MAXED Nuke to 100 and UseNuke to 95 for immediate atomic deterrent deployment against Egyptian forces. WC vote in 4 turns with exactly 45 delegates (28 Poland + 8 Inca + 9 Denmark). Cannot afford to lose Melbourne/Yerevan. Raised Diplomacy to 90 to consolidate CS alliances post-war. Defense remains at 95 against Egyptian naval pressure. Science/Production maintained for military infrastructure.

- Replay: use_nuke 85 => 75 (Δ -10), nuke 95 => 85 (Δ -10)
> Diplomatic victory mathematically impossible this vote (Poland 28 + Inca 8 = 36 maximum, need 45). Pivoting to Science Victory leveraging existing Space Procurements tenet. Satellites next for Apollo Program. Maintain nuclear deterrent to stop Egyptian invasion of Melbourne/Yerevan, then seek peace. Reduce diplomatic urgency and offensive military posture in favor of internal production and science output.

## Deepseek-3.2-Simple - Turn 469 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-20`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> The Netherlands is at 84% diplomatic victory; we must accelerate capture of Polynesian capitals (Honolulu, Assur) to achieve domination before they win. Increasing UseNuke and Nuke flavors prepares for nuclear strikes if conventional assault fails. Maintaining maximum Offense, Defense, Mobilization ensures continuous unit production. Science and Gold are critical for researching Stealth Bombers and purchasing units. Happiness offsets war weariness, and Espionage protects our science cities.

- Replay: use_nuke 90 => 80 (Δ -10), nuke 90 => 80 (Δ -10)
> With roughly 30 turns left, domination is the only realistic path. We narrow the AI’s focus to a handful of emergency war priorities: rush unit production (Mobilization/Production), break through to Honolulu and Assur (Offense/Ranged/Air/Mobile), and hold Taghaza and Tondibi against Dutch and Polynesian assaults (CityDefense/Antiair). Tactical nuclear strikes must be used to crack enemy stacks (Nuke/UseNuke). Science is kept at a moderate level to finish Stealth, while all non-military flavors—especially Diplomacy, Wonder, and Spaceship—are zeroed out to prevent waste.

## Kimi-K2.5-Simple - Turn 392 - retry 3

**Deviation (replay vs original):** use_nuke `-25`, nuke `-30`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Nuclear Fission complete - MAXED Nuke to 100 and UseNuke to 95 for immediate atomic deterrent deployment against Egyptian forces. WC vote in 4 turns with exactly 45 delegates (28 Poland + 8 Inca + 9 Denmark). Cannot afford to lose Melbourne/Yerevan. Raised Diplomacy to 90 to consolidate CS alliances post-war. Defense remains at 95 against Egyptian naval pressure. Science/Production maintained for military infrastructure.

- Replay: use_nuke 85 => 70 (Δ -15), nuke 95 => 70 (Δ -25)
> Nuclear Fission is complete, so the atomic deterrent is now available; lowering emergency nuke flavors from 95/85 to 70/70 maintains credible retaliation against Egypt while freeing strategic bandwidth. Spaceship, Science, and Production are all raised to 95 to prioritize Apollo infrastructure the moment Computers finishes. Gold is bumped to 85 to fund future city-state recoveries and unit upgrades. Mobilization is reduced to 70 to allow more civilian production capacity for spaceship parts.

## GLM-4.7-Simple - Turn 356 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-30`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 60 (Δ -15), nuke 85 => 70 (Δ -15)
> Refining flavor priorities to address the critical happiness crisis and resource constraints. Happiness raised to 95 to urgently combat the 39% happiness combat penalty. Gold increased to 90 and Production to 95 to fund and build defensive units faster. Mobilization raised to 100. Nuke and UseNuke lowered to 70/60 because we still lack Uranium despite completing the Manhattan Project; these will be raised once Uranium is secured. Spaceship lowered to 80 and Espionage to 70 to reduce priority dilution. Diplomacy lowered slightly to 80 as alliance relationships are already strongly established.

## Deepseek-3.2-Simple - Turn 353 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `-15`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 95 (Δ +0)
> India's nuclear capability and air superiority (B17, carriers) demand maximum readiness for nuclear retaliation and air defense. UseNuke at 100 ensures our AI will consider nuclear strikes when strategically necessary. Maintaining UnitedNations grand strategy is critical to survive and win diplomatically, as India is too far ahead in science and domination.

- Replay: use_nuke 95 => 80 (Δ -15), nuke 95 => 80 (Δ -15)
> India has completed the Apollo Program and leads by 5 technologies with 72 total. A diplomatic victory is mathematically impossible against India's 27 delegates. Science victory is now our only plausible path, and Babylon's Great Scientist generation gives us a narrow chance to catch up. We are shifting GrandStrategy to Spaceship and maxing Spaceship, Science, GreatPeople, and Production flavors to rush the Apollo Program and parts. We maintain Air and Antiair at 100 to survive Indian B17s, and keep Defense/CityDefense near-maximum to hold our core while our cities pivot to space-related infrastructure.

## Kimi-K2.5-Simple - Turn 385 - retry 3

**Deviation (replay vs original):** use_nuke `-25`, nuke `-55`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> NUCLEAR DETERRENT DEPLOYMENT PHASE: Advanced Ballistics nearing completion (Satellites next). Maximum Nuke priority (100) to ensure immediate nuclear weapon production upon tech unlock. UseNuke increased to 90 for credible deterrent threat against Indonesia-Songhai invasion. Air/Antiair at 95 for superiority against combined 14,000+ enemy military. Science/Culture slightly reduced to 95 (still critical but survival priorities equal). Wonder at 90 for The Internet rush once Satellites completes. Diplomacy nudged to 75 anticipating post-nuclear peace negotiations with India.

- Replay: use_nuke 80 => 65 (Δ -15), nuke 95 => 45 (Δ -50)
> TURN 385 EMERGENCY ADJUSTMENT: Indonesian navy sank Fleet Destroyer in home waters; Songhai continues land pressure with 14,000 combined military vs my 3,810. Nuclear weapons still distant (Advanced Ballistics 6 turns + Manhattan Project/build). Production EMERGENCY 100 and Mobilization 95 to replace losses and field more defensive units. MilitaryTraining 95 essential for high-XP garrisons against combined arms assault. Nuke reduced to 45 (not yet buildable), UseNuke 65 for immediate deterrence once available. Science 100 and Culture 100 UNCHANGED: Poland becomes Influential in 4 turns (3/6), making Satellites/The Internet the only realistic path. Naval increased 70→80 to contest coastal incursion. Defense/CityDefense/Antiair remain near-cap. Must survive the attrition war to reach tourism endgame.

## GLM-4.7-Simple - Turn 431 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-20`

- Original: use_nuke 75 => 80 (Δ +5), nuke 100 => 100 (Δ +0)
> After Brazil destroyed 3 anti-air units and continues nuclear-submarine attacks, increased Defense/CityDefense/Antiair/UseNuke to MAX for survival against two nuclear-armed superpowers. Mobilization 70 for replacing lost units. Production 100 for reconstruction. Science 100 for Spaceship path despite devastation. Gold 90 (economy -95 GPT deficit) for purchasing units/buildings. Happiness 100 - we're Unhappy with combat penalties, must prioritize. Espionage 100 - critical for intelligence on nuclear threats. Diplomacy 90 - World Congress in 7 turns, need delegates. Air 50 - build bombers for deterrence. GreatPeople 80 for Spaceship components. Decreased Growth and Navals as resources diverted to immediate survival.

- Replay: use_nuke 75 => 60 (Δ -15), nuke 100 => 80 (Δ -20)
> Adjusting flavors to reflect post-nuclear damage control after Uxmal's devastation: Growth raised to 85 and TileImprovement to 60 to prioritize population recovery and fallout/academy repair around Uxmal and Palenque. Culture reduced to 40 as mathematically impossible to resist Brazil's 6140 tourism per turn in the ~14 turns remaining. Spaceship deprioritized slightly to 70 to redirect Production toward immediate defensive and economic recovery. Air increased to 60 to prepare for advanced aerial defense if Aluminum trade with Assyria succeeds. Nuke flavors reduced due to zero domestic Uranium. Survival and score maximization remain the only viable macro-level objectives.

## Kimi-K2.5-Briefed - Turn 446 - retry 1

**Deviation (replay vs original):** use_nuke `-25`, nuke `-5`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> Spain's bankruptcy imminent (Turn 448) with -3,897 GPT but war continues - maintain maximum Defense 100, UseNuke 90 for credible second-strike against potential desperate Spanish air offensive pre-deletion. Critical adjustment: Production 95 prioritizes Solar Plants in St. Petersburg/Yaroslavl' (coastal desert cities) and Aluminum Mines on 16 unimproved tiles for spaceship resource security. Science 100 and Spaceship 100 unchanged - cannot win conventional war, only outpace to space. Reduced Gold 50 (was 70) - post-bankruptcy peace will enable trade route recovery with Morocco and potentially others via Cold War repeal.

- Replay: use_nuke 85 => 65 (Δ -20), nuke 95 => 90 (Δ -5)
> Spain's treasury collapse imminent (Turn 447-448) will delete expensive air/naval units and force peace or white-flag. Reduce extreme military-defense flavors marginally (Defense 85, CityDefense 80, Mobilization 70) to allow staff to address critical Very Unhappiness (35%) with happiness buildings (Happiness 100) and prevent rebellions in Rostov/Yekaterinburg. Pivot some capacity to TileImprovement 80 for aluminum mine construction and Infrastructure 85 for post-peace trade route recovery. Raise Production 95 and GreatPeople 85 for spaceship part preparation post-Satellites. Lower UseNuke 65/Nuke 90 as nuclear first-strike becomes unnecessary against economically collapsing opponent and risks derailing favorable peace terms. Growth reduced to 45 to avoid exacerbating unhappiness until amenities restored.

## Deepseek-3.2-Simple - Turn 459 - retry 1

**Deviation (replay vs original):** use_nuke `-70`, nuke `-60`

- Original: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Byzantium is 1 turn from cultural victory and has overwhelming military superiority. Our only slim hope is to accelerate nuclear weapons development (Advanced Ballistics) to strike their cultural hubs, while using espionage to disrupt them. Prioritize Nuke, UseNuke, Espionage, and Science to rush nukes and counter-intelligence. Maintain maximum defensive and anti-air flavors to survive their air force. All efforts must focus on delaying their victory and enabling a nuclear decapitation strike.

- Replay: use_nuke 50 => 30 (Δ -20), nuke 70 => 40 (Δ -30)
> Switching to emergency space race mode. Domination is impossible against Byzantium's overwhelming military, and their cultural victory is imminent unless blocked by a missing wonder. Diplomatic victory is 6 turns away. Our only remaining path is to rush the Apollo Program and spaceship parts while other civs are distracted by war. Maximum priority on Spaceship, Science, Production, and Happiness to stabilize the empire and build components. Defense flavors remain high enough to hold borders, but offensive flavors are cut sharply to free up hammers for civilian infrastructure.

## Kimi-K2.5-Briefed - Turn 336 - retry 3

**Deviation (replay vs original):** use_nuke `-40`, nuke `-40`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> DEFENSIVE SURVIVAL PIVOT: Peace with Shoshone (accepted Turn 335) closes one front, but India remains existential threat (4,742 MS vs my 2,405, 98% control of Denmark). Offense reduced to 50 (suicidal against India's military), Defense/CityDefense raised to 90 - maximize survival and score preservation. Nuke/UseNuke maxed to 100 - emergency deterrent only hope to slow India. Mobilization stays high (90) to replace losses. Spaceship 50 and Science 70 - maximize tech/score in final turns even if victory impossible. Abandon expansion (0) - no time for new cities. Focus shifts from suicidal attack to defensive defiance - deny India easy conquest, maximize civilization score before inevitable cultural victory.

- Replay: use_nuke 80 => 60 (Δ -20), nuke 90 => 60 (Δ -30)
> Preparing for the inevitable war with India requires maximizing immediate military power while maintaining a science fallback. Gold increased to 80 to fund emergency unit purchases with Draft Registration. Science raised to 70 since teching to Replaceable Parts and beyond is essential. Diplomacy raised to 40 to secure city-state allies for resources and delegates. Nuke flavors lowered to 60 (no immediate capability). CityDefense lowered to 60 to prioritize field armies over garrisons. Conquest remains the grand strategy because only military disruption can stop India's victory.

## Kimi-K2.5-Simple - Turn 422 - retry 3

**Deviation (replay vs original):** use_nuke `-50`, nuke `-25`

- Original: use_nuke 50 => 80 (Δ +30), nuke 95 => 95 (Δ +0)
> Total war against India requires maximum military prioritization while preventing economic collapse. Offense/Air/Ranged at 85-95 ensures concentrated attacks on Delhi and their core cities. UseNuke at 80 signals willingness to deploy nuclear weapons if India advances. Gold/Happiness at 80-90 sustains unit maintenance and prevents combat penalties. Espionage at 100 directs spies to sabotage India's spaceship production in Constantinople and Calcutta. Mobilization at 30 begins reinforcing depleted units without overtaxing economy.

- Replay: use_nuke 50 => 30 (Δ -20), nuke 95 => 70 (Δ -25)
> We are 55 gold away from bankruptcy with −909 GPT. While our long-term goal remains the annihilation of India, an immediate fiscal collapse would disband our military and doom the empire. I am ordering an emergency economic freeze: halt all wonder, spaceship, and settler production; stop raising new land armies (Mobilization 0); and redirect every possible city to Wealth generation and trade-route construction. I keep Air and Ranged high to preserve our massive bomber/fighter superiority, but the next 2–3 turns must be dedicated to emergency wealth-building and Courthouse/Public Works completion so that the treasury recovers above the disband threshold. Once we stabilize above ~500 gold, we will revert to full war footing.

## Kimi-K2.5-Simple - Turn 416 - retry 3

**Deviation (replay vs original):** use_nuke `-25`, nuke `-25`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 416: CRITICAL CULTURAL VICTORY THREAT. Maya at 6/7 influential building Citizen Earth Protocol. Peace expires next turn - immediate total war required. Manhattan Project completes in 1 turn. Morocco (42260 strength) joins war via defensive pact. Maximum aggression flavors: Offense/Mobilization/Production/Nuke/UseNuke all at 100%. Must capture Maya cities, especially Palenque, before cultural victory. Nuclear weapons authorized for city capture.

- Replay: use_nuke 95 => 75 (Δ -20), nuke 95 => 75 (Δ -20)
> TURN 416: IMMEDIATE WAR ECONOMY ADJUSTMENTS. Happiness raised to maximum (100) to combat critical 49% happiness/combat-penalty and support sustained offensive. CityDefense raised to 70 because Morocco’s defensive pact with Maya will activate in 2 turns, requiring hardened cities. Nuke/Science/Espionage/Naval/AirCarrier sharply reduced — conventional land forces (tanks, artillery, bombers) must have absolute production priority for the existential assault on Maya. Conquest grand strategy unchanged.

## Deepseek-3.2-Simple - Turn 400 - retry 1

**Deviation (replay vs original):** use_nuke `-70`, nuke `-60`

- Original: use_nuke 60 => 100 (Δ +40), nuke 70 => 100 (Δ +30)
> Persia declared war and Poland's peace treaty expired. We must prioritize immediate military survival while maintaining diplomatic momentum. Flavors are shifted to maximum mobilization, nuclear deterrence (UseNuke: 100), city defense, and air/naval supremacy to counter Persia's naval attacks. We maintain UnitedNations to keep city-state alliances critical for votes, but spaceship production is halted (0) for wartime industry.

- Replay: use_nuke 60 => 30 (Δ -30), nuke 70 => 40 (Δ -30)
> Persia has declared war, but our overriding imperative is to secure the final 3 delegates for diplomatic victory. Our previous flavor matrix had far too many competing priorities set to maximum, which diffuses staff decision-making. We are sharpening the hierarchy: Diplomacy (100) and Gold (90) are now paramount to produce/buy envoys, fix our -35 GPT economy, and flip the remaining city-states. Defense and CityDefense remain strongly elevated to repel Persian aggression against our core and allied city-states. Broad military and civilian over-prioritization (Wonder, Espionage, GreatPeople, Antiair, Air, Naval, etc.) is reduced so production queues actually shift toward envoys, wealth generation, and targeted defensive units rather than unfocused empire projects. Science and Spaceship stay at moderate levels to preserve our Apollo fallback.

## Deepseek-3.2-Simple - Turn 400 - retry 3

**Deviation (replay vs original):** use_nuke `-70`, nuke `-40`

- Original: use_nuke 60 => 100 (Δ +40), nuke 70 => 100 (Δ +30)
> Persia declared war and Poland's peace treaty expired. We must prioritize immediate military survival while maintaining diplomatic momentum. Flavors are shifted to maximum mobilization, nuclear deterrence (UseNuke: 100), city defense, and air/naval supremacy to counter Persia's naval attacks. We maintain UnitedNations to keep city-state alliances critical for votes, but spaceship production is halted (0) for wartime industry.

- Replay: use_nuke 60 => 30 (Δ -30), nuke 70 => 60 (Δ -10)
> With Persia's declaration of war and the World Congress vote underway, we must sharpen our focus: maintain maximum Defense, CityDefense, and Diplomacy while keeping Gold at maximum to sustain city-state alliances. We reduce Wonder and Culture priorities since we are already dominant culturally, increase Spaceship as a fallback, and prioritize defensive military flavors (Antiair, Naval, Air) to repulse Persian aggression without overcommitting to offensive campaigns.

## Kimi-K2.5-Simple - Turn 421 - retry 3

**Deviation (replay vs original):** use_nuke `-50`, nuke `-30`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear weapons immediately available. Increased UseNuke to 100 for maximum aggression against Babylon. Babylon has Apollo Program (existential threat) with 2 Uranium and can build spaceship parts. Must deploy nuclear weapons immediately to destroy their production centers and prevent science victory. Maintaining maximum air power (100) for nuclear delivery capability and conventional strikes. War score only 12% against Babylon despite superior military - need to push harder before they complete spaceship parts. Ottoman alliance strong, trade secured for resources. Focus on producing nuclear missiles and advanced air units to deliver them.

- Replay: use_nuke 85 => 50 (Δ -35), nuke 100 => 70 (Δ -30)
> Manhattan Project completes next turn but I currently have 0 Uranium, rendering immediate nuclear deployment impossible. Lowering UseNuke from 85 to 50 and Nuke from 100 to 70 reflects this reality while keeping readiness for when Nuclear Fission (11 turns) reveals potential domestic Uranium or diplomacy secures it from allies. Increasing Mobile to 100 prioritizes Tank production upon completing Combined Arms, essential for breaking Babylon's core defensive line around Nippur and Dur-Kurigalzu. Diplomacy raised to 70 to aggressively pursue Uranium trades with Ottomans or Japan who possess reserves. Air and Antiair remain maximized at 100 because Babylon's possession of Uranium and Apollo Program makes their eventual nuclear capability an existential threat; air superiority is our best conventional counter. Production and Offense stay at 100 to sustain the coalition offensive alongside Ottomans and Japanese forces who remain at war with Babylon. Infrastructure increased to 60 to ensure rapid rail mobilization between the Grand River and Buffalo Creek fronts.

## Kimi-K2.5-Briefed - Turn 382 - retry 3

**Deviation (replay vs original):** use_nuke `-40`, nuke `-5`

- Original: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> EMERGENCY DIPLOMATIC RECOVERY: The city-state flipping operation failed to execute. With only 36 delegates and 5 turns until World Congress vote, I need maximum Diplomacy (100) and Gold (100) to execute immediate city-state purchases. Reduced Mobilization to 40 and Offense to 15 to free supply and focus on defensive deterrence. Increased Nuke/UseNuke to 95/80 as deterrent against Russian aggression while I secure delegates. Defense/Antiair remain at 90 for Russian containment. Must acquire 8+ delegates before vote or World Ideology: Order will fail.

- Replay: use_nuke 75 => 40 (Δ -35), nuke 90 => 90 (Δ +0)
> DUAL-TRACK PIVOT TO SCIENCE SUPREMACY: Intelligence confirms Russian Sphere of Influence resolutions on Brussels, Sokoto, M'banza-Kongo, and Belgrade render immediate diplomatic victory impossible—we are stalled at 36 delegates with no legal mechanism to flip permanent Russian allies. Therefore ordering a strategic pivot to Spaceship grand strategy while maintaining defensive military posture. Science and Spaceship flavors maximized to close Russia's 3-technology lead (62 vs 65) and secure Information Era dominance. Growth raised to 80 to exploit upcoming Medical Labs from Penicillin, translating population expansion into long-term research output. Production increased to 80 for spaceship component manufacturing. Diplomacy reduced to 40 since city-state influence purchasing is diplomatically frozen by UN resolutions, though we retain capacity to capitalize on delegate gains later via Host status, Globalization, or UN wonder. Gold reduced to sustainable 60 as treasury reserves (17,579G) are sufficient and immediate city-state purchasing is blocked. Military posture remains defensive with Antiair at 90 and Nuke at 90 for deterrence against Catherine's 16,893-strength force, but UseNuke lowered to 40 to signal purely retaliatory nuclear posture while science infrastructure develops.

## Deepseek-3.2-Briefed - Turn 387 - retry 2

**Deviation (replay vs original):** use_nuke `-70`, nuke `-50`

- Original: use_nuke 70 => 100 (Δ +30), nuke 70 => 100 (Δ +30)
> We are in the final push for domination victory. We must capture Moson Kahni and London. To achieve this, we need to prioritize building transport ships for amphibious assault and achieve air superiority. Maximizing flavors for naval, air, mobile, and nuclear units ensures the in-game AI focuses production on these critical areas. Deprioritizing non-essential areas like culture, religion, and expansion concentrates our efforts on military conquest.

- Replay: use_nuke 70 => 30 (Δ -40), nuke 70 => 50 (Δ -20)
> Pivot from the failing multi-front domination campaign to a Science Victory. Poland is in the Information Era with 1,866 Science per turn, giving us a realistic path to win by reaching late-game technologies and building spaceship components. We are drastically lowering naval and offensive flavors because the amphibious invasion of England is impossible without transports, and our war with the Shoshone is stalemated. Instead, we will maximize Science, Spaceship, Production, GreatPeople, and Growth to optimize research output and spaceship-part production, while keeping enough Defense and Happiness to maintain stability during our ongoing wars.

## Kimi-K2.5-Simple - Turn 354 - retry 2

**Deviation (replay vs original):** use_nuke `-50`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> India is 100% Popular with me - on the verge of cultural victory. Must launch immediate total war with all available forces. Prioritizing air power, paratroopers, and nuclear preparation (Atomic Theory in 11 turns). Need maximum offensive punch to capture Indian cities before cultural victory triggers. Abandoning culture/diplomacy - only war matters now.

- Replay: use_nuke 90 => 50 (Δ -40), nuke 100 => 100 (Δ +0)
> India has not yet won culturally—Rome is only at 68% influence with ~41 turns remaining until Influential, and India still requires the Citizen Earth Protocol. This creates a viable window for Portugal to pivot from exhausted conquest to a science victory. We will maintain a defensive military posture to deter The Iroquois (who just accepted 3,948 gold from India) and finish Carthage, while maximizing science, production, and growth to reach the Information Era and build the spaceship before India completes their victory.

## Kimi-K2.5-Simple - Turn 354 - retry 3

**Deviation (replay vs original):** use_nuke `-50`, nuke `-20`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> India is 100% Popular with me - on the verge of cultural victory. Must launch immediate total war with all available forces. Prioritizing air power, paratroopers, and nuclear preparation (Atomic Theory in 11 turns). Need maximum offensive punch to capture Indian cities before cultural victory triggers. Abandoning culture/diplomacy - only war matters now.

- Replay: use_nuke 90 => 50 (Δ -40), nuke 100 => 80 (Δ -20)
> India is approaching cultural victory but has not yet secured it. Maintain maximum war posture against Rome to capture their capital while advancing military technology. Prioritize air power, paratroopers, and production. Reduce UseNuke since nuclear weapons are unavailable but keep Nuke flavor for future deterrence. Espionage remains critical against India.

## Kimi-K2.5-Briefed - Turn 336 - retry 2

**Deviation (replay vs original):** use_nuke `-60`, nuke `-50`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> DEFENSIVE SURVIVAL PIVOT: Peace with Shoshone (accepted Turn 335) closes one front, but India remains existential threat (4,742 MS vs my 2,405, 98% control of Denmark). Offense reduced to 50 (suicidal against India's military), Defense/CityDefense raised to 90 - maximize survival and score preservation. Nuke/UseNuke maxed to 100 - emergency deterrent only hope to slow India. Mobilization stays high (90) to replace losses. Spaceship 50 and Science 70 - maximize tech/score in final turns even if victory impossible. Abandon expansion (0) - no time for new cities. Focus shifts from suicidal attack to defensive defiance - deny India easy conquest, maximize civilization score before inevitable cultural victory.

- Replay: use_nuke 80 => 40 (Δ -40), nuke 90 => 50 (Δ -40)
> Emergency war mobilization has served its purpose—Shoshone peace is achieved and India cannot be stopped through mid-game military escalation. Switching Grand Strategy to Spaceship to maximize science, production, and final score in the likely event India wins via culture in 10-20 turns. Reducing Offense/Mobilization/MilitaryTraining to stop bleeding gold on units I cannot use effectively. Increasing Science, Production, and Spaceship flavors to accelerate research and infrastructure. Maintaining moderate Defense and CityDefense to protect against opportunistic attacks, but the primary goal is now economic and scientific maximization rather than doomed conquest.

## Minimax-M2.5-Simple - Turn 410 - retry 1

**Deviation (replay vs original):** use_nuke `-70`, nuke `-50`

- Original: use_nuke 75 => 100 (Δ +25), nuke 50 => 100 (Δ +50)
> Maximize cultural victory push during Golden Age (14 turns remaining). Already 6/7 influential - Ottomans becoming influential in 24-68 turns. Prioritize Great People generation for tourism and maintain WC coalition diplomacy.

- Replay: use_nuke 75 => 30 (Δ -45), nuke 50 => 50 (Δ +0)
> Shift to pure cultural endgame focus. With overwhelming military dominance (53k vs next competitor 13k), drastically reduce military flavors (Offense/Mobilization/UseNuke) to redirect production toward civilian economy and tourism infrastructure. Boost Gold (80) to fund international trade routes to the Ottomans, our last cultural target. Increase Science (70) to rush Satellites -> The Internet for the tourism multiplier. Maintain Culture/GreatPeople/Diplomacy at 100 to maximize passive tourism generation and World Congress coalition control (vote in 8 turns). Increase Happiness (70) to sustain Golden Ages.

## Kimi-K2.5-Simple - Turn 421 - retry 2

**Deviation (replay vs original):** use_nuke `-50`, nuke `+0`

- Original: use_nuke 75 => 80 (Δ +5), nuke 95 => 95 (Δ +0)
> APOLLO PROGRAM CONSTRUCTION - ALUMINUM CRISIS: Turn 421, Apollo Program 9 turns from completion in Venice (220 Production/turn). Critical flavors: Production 100/Science 100/Spaceship 100 for rapid wonder and parts construction. Gold 90 for Aluminum acquisition via trade with Songhai (29 stockpile) or China peace deal (14 stockpile). Defense 95/Antiair 90/Nuke 95/UseNuke 80 against Egyptian XCOM encirclement (22,000 vs 2,183 military, 10:1 ratio). Egypt has 5 XCOM Squads, Mechanized Infantry, Mobile SAM, Fighter, Rocket Missile in adjacent Nara zone - existential threat. Air 85 for fighter production to defend against Egyptian heavy bombers. Zero Aluminum available - must acquire 4+ Aluminum BEFORE Apollo completion or spaceship parts cannot be built. India at 88% diplomatic victory with vote in 2 turns - if they win, game over. If Egypt completes spaceship first (33% progress, 2 parts done), game over. This is final sprint for survival.

- Replay: use_nuke 75 => 30 (Δ -45), nuke 95 => 95 (Δ +0)
> ECONOMIC TRIAGE AND ALUMINUM ACQUISITION: GPT at catastrophic -164 with 116 Gold reserves—empire will hemorrhage units/buildings without immediate stabilization. Mobilization slashed from 80→20 and MilitaryTraining from 50→20 to halt costly unit production and gold-bought upgrades. CityDefense reduced 85→60 because existing garrisons and Strategic Defense Systems are sufficient against Egyptian encirclement. UseNuke dropped 75→30 to maintain nuclear deterrent posture without risking accidental escalation that invites Egyptian annihilation. Gold priority raised to 100 to maximize treasury recovery and resource-trading leverage for Aluminum acquisition (existential blocker: 0 Aluminum, need 4+). Happiness raised 30→60 to insulate production from war-weariness shocks. Wonder lowered 85→60 to prevent distracting non-Apollo projects. Production/Science/Spaceship/Defense remain prioritized for Apollo Program completion in ~9 turns and subsequent parts construction. Absolute submission to Egypt unchanged.

## Kimi-K2.5-Simple - Turn 387 - retry 1

**Deviation (replay vs original):** use_nuke `-100`, nuke `-70`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> TURN 387: MAXIMUM WAR FOOTING. Austria at 83% diplomatic victory with 4 turns remaining. All resources must pivot to immediate military production. Nuke/UseNuke at 100 for instant atomic weapon deployment upon Nuclear Fission completion. Offense/Mobilization/Production at 100 to maximize unit output for desperate Vienna strike. Air at 90 for heavy bomber production (conventional strategic bombing as fallback). Antiair at 100 counters Austria's air superiority. Diplomacy/Wonder/Culture at 0 - no time for long-term investments. Only total war can prevent defeat.

- Replay: use_nuke 50 => 0 (Δ -50), nuke 100 => 30 (Δ -70)
> TURN 387: Grand strategy pivots from Conquest to Spaceship. Diplomatic and conventional military paths are closed (Bucharest war-blocked, 3 Uranium insufficient for decisive nuclear strike, 2,440 vs 5,302 strength). Science victory is the sole independent win condition if coalition blocks Austrian diplomacy. Spaceship 100, Science 95, Production 85 prioritize catch-up to Information Era and spaceship parts. Baghdad and Medina Research Labs completed this turn, accelerating the science base. Antiair/CityDefense remain maxed (Austria fields Heavy Bombers/Fighters near Vienna). Mobilization and Offense slashed to prevent bankrupting gold reserves and suicidal attacks. Nuclear/Nuke flavors reduced but retained at 30 for Nuclear Plant production boosts after Fission is researched.

## Kimi-K2.5-Briefed - Turn 378 - retry 2

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> EMERGENCY FINAL GAMBIT: Passport System will pass in 2 turns with 46 YES votes (my 'allies' betrayed me). Maya will get 50% tourism boost and become Influential over me immediately - cultural victory is inevitable in 2-3 turns. ONLY HOPE: Science victory before Maya's cultural victory triggers. Need to purchase Great Scientists IMMEDIATELY with Faith (180/turn), rush to Information Era, build spaceship parts. Also preparing maximum military mobilization - if I'm going to lose, I take Maya down with me through nuclear annihilation. Total war footing - no defense, all offense, all science.

- Replay: use_nuke 50 => 0 (Δ -50), nuke 100 => 0 (Δ -100)
> Maya’s cultural victory is gated by Songhai (~17 turns), giving a narrow but real science-victory window. Zeroing nuclear and naval priorities prevents production waste; raising Production and Gold accelerates spaceship part construction and fixes our -2 GPT bleed. Culture is deprioritized since only Free Thought remains essential. Science, Spaceship and GreatPeople remain at maximum.

## GLM-4.7-Simple - Turn 499 - retry 3

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Maximum Science (100) and Production (100) to accelerate Stealth research and subsequent Stealth Bomber construction for air parity. Air (100), Defense (100), Antiair (100), and CityDefense (85) address existential threat from Russia's 8 Stealth Bombers by prioritizing air defense infrastructure and protecting homeland. UseNuke (100) and Nuke (100) maintain nuclear deterrence posture after Russia's 2 SS Boosters - Russia must understand that launching would trigger our response despite lacking uranium stockpile. Espionage (100) maxed to monitor Russian spaceship part production in Moscow, Yekaterinburg, and key cities - our 10 spies in Russian cities provide critical intelligence on their victory timeline. Diplomacy reduced to 5 since World Congress voting is now; alliances with England and The Celts (Autocracy-aligned) should naturally align against Russia's UN proposal. Spaceship flavor set to 0 as Stealth research takes immediate precedence - spaceship parts scheduled once production capacity supports parts with Stealth Bomber protection.

- Replay: use_nuke 50 => 0 (Δ -50), nuke 100 => 0 (Δ -100)
> With turn 498 and maximum turns at 500, only 2 turns remain for Time Victory scoring. Russia leads score 6120 to 4718. Prioritize immediate score generation: Production and Spaceship flavors remain maximum to accelerate any completable projects. Growth increased to 80 and Gold to 90 to enable population growth and emergency purchases. Happiness boosted to 70 to support growth. Wonder flavor raised to 50 to capture any quick wonder opportunities. Science reduced to 80 since The Internet (12 turns remaining) cannot complete, but spaceship part production remains critical. Nuke and UseNuke zeroed due to zero Uranium reserves. Defense, CityDefense, Air, and Antiair maintained near-maximum to protect cities from Russian Stealth Bombers and XCOM raids in the final turns. Espionage reduced to 50 as no operations will complete before game end. Diplomacy slightly lowered to 40; focus shifts from city-state unit production to ensuring existing alliances hold for final World Congress votes against Russia's United Nations proposal.

## GLM-4.7-Simple - Turn 424 - retry 1

**Deviation (replay vs original):** use_nuke `-55`, nuke `-15`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> DEFENSIVE MAXIMUM ACTIVATED: Russia occupying Cologne, Stuttgart, Dortmund - 4.63x military superiority (15440 vs 3335). Defense 100, CityDefense 100, Antiair 100 - absolute priority preventing further territorial loss and defending core cities. MilitaryTraining 95 for unit quality under numerical disadvantage. Mobilization 90 for rapid production. Nuke 100, UseNuke 95 - Russia has 19 Uranium, Germany must achieve nuclear deterrence. Production 100, Science 100 - Space race accelerates as militarily infeasible alternative. Gold 90 for maintaining army under upkeep pressure. Diplomacy 80 for coalition building against Russia. Espionage 100 - intelligence on Russian nuclear and naval operations critical. Espionage focus on Moscow (spy Katrin at 166 network) to monitor Russian Manhattan Project and fleet movements. Spaceship 95 - Apollo Program enables victory path despite territorial losses.

- Replay: use_nuke 90 => 40 (Δ -50), nuke 100 => 85 (Δ -15)
> Russia's capture of Cologne creates immediate existential land threat requiring maximum air defense, mobile reserves, and rapid redeployment. Reduce offensive and naval priorities since Cologne is lost and survival depends on homeland defense. Maintain maximum science and production for spaceship components and emergency unit production. Espionage critical for Russian intelligence. Reduced nuclear posture reflects extreme Uranium scarcity (3 vs Russia's 19); prioritize conventional deterrence.

## Kimi-K2.5-Simple - Turn 422 - retry 2

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Turn 422: EXTINCTION CRISIS - 9 turns until French Cultural Victory. Entering maximum desperation mode: nuclear strike posture elevated to 100% launch probability, prioritizing destruction of French cultural centers. Science and Espionage maximized in desperate hope of accelerating Stealth technology or disrupting French infrastructure via spies (Paris network at 986). All civilian development halted (Spaceship/Culture/Gold/Expansion to 0), total war economy engaged.

- Replay: use_nuke 50 => 0 (Δ -50), nuke 50 => 0 (Δ -50)
> Turn 422: Facing imminent French Cultural Victory when Rome becomes Influential in ~9 turns. However, France may still need Citizen Earth Protocol wonder to actually seal the win. Executing emergency pivot to Spaceship grand strategy—our only potential salvation. Eliminating offensive military flavors (Offense 0, Mobile 30, Ranged 40) to stop suicidal attacks and conserve forces for pure defensive hedgehog posture. Critical correction: discovered I have zero Uranium, rendering nuclear threats impossible—setting Nuke/UseNuke to 0. Maintaining CityDefense 90 and Defense 100 to survive Roman/French assaults while production shifts to science and spaceship components. Maximizing Science and Spaceship flavors to rush remaining Information Era technologies and part construction. Boosting Growth, Happiness, and GreatPeople to fuel population and scientist generation. Every turn of survival may matter if France still lacks the protocol wonder.

## Deepseek-3.2-Simple - Turn 369 - retry 1

**Deviation (replay vs original):** use_nuke `-70`, nuke `-60`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Increasing UseNuke and Nuke flavors to maximum ensures the in-game AI prioritizes nuclear arsenal buildup and aggressive nuclear strike planning once we unlock Atomic Bombs. This aligns with our imminent war against China and The Maya, where nuclear weapons will be decisive in overcoming their numerical and defensive advantages. All other military and economic flavors remain high to sustain multi-front warfare and rapid conquest.

- Replay: use_nuke 80 => 30 (Δ -50), nuke 90 => 40 (Δ -50)
> Pivoting to a rapid sequential conquest of The Aztecs then The Maya. Intelligence confirms The Maya lacks defensive pacts with China or Egypt, making them an ideal target while our peace with China holds. We are reducing nuke flavors due to current lack of Uranium; increasing airlift and naval priorities to enable rapid coastal offensives and quick repositioning between multiple fronts.

## Kimi-K2.5-Simple - Turn 422 - retry 1

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Turn 422: EXTINCTION CRISIS - 9 turns until French Cultural Victory. Entering maximum desperation mode: nuclear strike posture elevated to 100% launch probability, prioritizing destruction of French cultural centers. Science and Espionage maximized in desperate hope of accelerating Stealth technology or disrupting French infrastructure via spies (Paris network at 986). All civilian development halted (Spaceship/Culture/Gold/Expansion to 0), total war economy engaged.

- Replay: use_nuke 50 => 0 (Δ -50), nuke 50 => 0 (Δ -50)
> Turn 422: French Cultural Victory imminent in ~9 turns. Removed Nuke/UseNuke priorities (empire has 0 Uranium/Aluminum, making nuclear weapons impossible). Maintaining maximum defensive production - Offense, Defense, Mobilization, Production remain at 100 to churn out last-ditch defenders against Franco-Roman assault. CityDefense, Ranged, Air, and Antiair stay high as Rome is actively bombing near Montreal and French armor threatens Grand River. No long-term economic flavors matter now; pure survival posture.

## Kimi-K2.5-Simple - Turn 384 - retry 1

**Deviation (replay vs original):** use_nuke `-60`, nuke `-50`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maximum offensive posture for existential cultural war. UseNuke 100 and Nuke 100 authorize nuclear strikes on Dutch cultural centers (Amsterdam/Rotterdam/Utrecht) to destroy tourism buildings before Netherlands influences Austria in 6 turns. Mobile 100 and Air 100 enable rapid strikes. Production 100 and Mobilization 100 ensure nuclear missile replacement. Netherlands at 97% with Austria - only 6 turns left. Must destroy their tourism NOW or lose cultural victory.

- Replay: use_nuke 95 => 40 (Δ -55), nuke 100 => 50 (Δ -50)
> Maximum conventional offensive posture against Netherlands. Nuclear weapons will not arrive in time for the critical 6-turn window before Netherlands becomes Influential with Austria, so they are slightly deprioritized. Naval and Air are maxed for coastal bombardment and air strikes on Amsterdam, Rotterdam, and Utrecht. Culture bumped to 75 to ensure tourism stays at peak output for Austria in 7 turns. Grand strategy remains Conquest to seize and raze Dutch cultural cities and eliminate the only remaining cultural competitor before we construct the Citizen Earth Protocol.

## Kimi-K2.5-Briefed - Turn 315 - retry 3

**Deviation (replay vs original):** use_nuke `-70`, nuke `-70`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> FINAL GAMBLE - Indonesia wins in 12 turns. Maximum priority to Naval and Airlift for immediate unit transport to Indonesian theater. Nuke 100/UseNuke 100 - we MUST build nuclear weapons if possible, only realistic way to destroy cities and tourism infrastructure before victory. Science 100 to reach nuclear tech faster. Espionage 100 - spies MUST target cultural/tourism buildings in Jakarta/Denpasar/Makassar to reduce tourism output directly. Abandoning Denmark/England fronts entirely - all units to Indonesia NOW.

- Replay: use_nuke 90 => 30 (Δ -60), nuke 90 => 30 (Δ -60)
> SUSTAINED MOBILIZATION - Indonesia timeline revised to 50+ turns. Shift from panic emergency to realistic industrial-military buildup: maintain strong Ranged/Naval/Offense for Indonesian siege, but increase Growth, TileImprovement, Infrastructure, and Science to develop coal-powered economy. Culture 30 to slow Indonesian influence. Science 90 to reach Modern Era. Moderate Expansion for forward bases if needed.

## Kimi-K2.5-Briefed - Turn 420 - retry 1

**Deviation (replay vs original):** use_nuke `-90`, nuke `-85`

- Original: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DUAL-TRACK SURVIVAL STRATEGY: Track 1 - Nuclear deterrence against Shoshone's 4:1 military advantage (completing Radar→Atomic Theory→Manhattan Project). Track 2 - UN victory pathway via Celt vote flip. Current delegate count: Me(19)+Brazil(23)+Assyria(12)=54 without Celts, 64 with Celts. Shoshone UN proposal Turn 426 is existential threat - must secure 45 votes to block. Max Diplomacy(95) prioritizes Celt relationship investment and city-state ally maintenance. Nuke/UseNuke(100) maintains deterrent while pursuing diplomatic solution.

- Replay: use_nuke 70 => 10 (Δ -60), nuke 100 => 15 (Δ -85)
> Complete strategic pivot: direct military confrontation with Brazil (85k vs 4k strength) is suicide. UnitedNations grand strategy leverages our completed Statecraft branch and existing city-state alliances to maximize delegates. High Science and Spaceship flavors maintain a secondary path if we buy enough time via Cold War. Espionage at 90 prioritizes tech theft to close the 11-tech gap with Brazil. Drastically reduced Offense/Nuke reflects realism; resources shift to delegate acquisition, production, and defensive infrastructure that can support either a diplomatic or scientific endgame.

## Kimi-K2.5-Simple - Turn 408 - retry 3

**Deviation (replay vs original):** use_nuke `-75`, nuke `-50`

- Original: use_nuke 80 => 95 (Δ +15), nuke 90 => 100 (Δ +10)
> INCREASE military pressure to force immediate peace or rapid victory against Zulus, then pivot to full spaceship production. Offense 75→85, Mobilization 65→75, Production 90→95 to expedite war conclusion within 5-10 turns maximum. Nuke 90→100 and UseNuke 95 for tactical nuclear strikes if Zulus refuse peace - cannot allow prolonged war. Science remains 100, Spaceship 100 as absolute priority. Growth 80→90 and Happiness 85 to counteract war weariness effects and prepare for post-war recovery. If peace achieved next turn, these flavors immediately shift to Production 100/Spaceship 100 focus. The war MUST end - Russia has 75 techs (ahead) and massive 45658 military vs my 24990.

- Replay: use_nuke 80 => 20 (Δ -60), nuke 90 => 50 (Δ -40)
> War weariness at 55% demands pivot to spaceship focus. Maintain moderate offense to finish Bulawayo but reduce Nuke/UseNuke (50/20) to avoid warmonger penalties before World Congress. Boost Production (95), Gold (75), and Espionage (75) to close the 1-tech gap with Russia and prepare for spaceship part production.

## Kimi-K2.5-Simple - Turn 499 - retry 1

**Deviation (replay vs original):** use_nuke `-70`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> FINAL THREE TURNS TO DIPLOMATIC VICTORY (Turn 503): Barcelona completing SS Stasis Chamber in 2 turns provides science victory insurance. World Congress convenes in 4 turns with 39/42 delegates secured. Shoshone vassal maintains absolute loyalty (9,720 diplomat network, +70/turn). War with Huns progressing favorably - destroyed multiple fleet destroyers, pushing toward Osaka/Kyoto. Reduced offensive mobilization slightly (70 from 90) as victory is assured. Maintained high production (90) for spaceship completion. Maximum diplomacy (100) ensures delegate optimization. Will use nuclear weapons if Huns attempt last-minute atomic strikes from Duckwater. No strategic risks - victory convergence absolute.

- Replay: use_nuke 90 => 30 (Δ -60), nuke 100 => 100 (Δ +0)
> FOUR TURNS TO WORLD CONGRESS VICTORY: Shoshone vassal maintains absolute loyalty with 30 delegates, giving effective majority (69 total vs 42 threshold). Barcelona completing SS Stasis Chamber next turn provides near-certain science backup (1 part remaining). Reduced UseNuke from 90 to 30 to avoid provoking Hunnic atomic retaliation with their 3 bombs at Duckwater during critical endgame; conventional superiority (49k vs 40k) suffices for deterrence. Raised Spaceship to 100 to guarantee Barcelona queues final spaceship part immediately after SS Stasis Chamber completion. Maintained UnitedNations grand strategy and all other military/diplomatic priorities for victory convergence.

## Kimi-K2.5-Simple - Turn 421 - retry 2

**Deviation (replay vs original):** use_nuke `-75`, nuke `-60`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear weapons immediately available. Increased UseNuke to 100 for maximum aggression against Babylon. Babylon has Apollo Program (existential threat) with 2 Uranium and can build spaceship parts. Must deploy nuclear weapons immediately to destroy their production centers and prevent science victory. Maintaining maximum air power (100) for nuclear delivery capability and conventional strikes. War score only 12% against Babylon despite superior military - need to push harder before they complete spaceship parts. Ottoman alliance strong, trade secured for resources. Focus on producing nuclear missiles and advanced air units to deliver them.

- Replay: use_nuke 85 => 25 (Δ -60), nuke 100 => 40 (Δ -60)
> Manhattan Project completes in 1 turn but I possess zero Uranium, making immediate nuclear strike impossible. Reducing UseNuke to 25 and Nuke to 40 reflects this reality while maintaining readiness if Uranium is acquired via trade or conquest. Conquest remains the only viable path: Babylon has Apollo Program (science threat), Japan is 18 turns from Influential over Babylon and 55 from America (cultural threat), and Time Victory favors Japan's score lead. Maximum Air (100), Antiair (100), Mobile (95), and Ranged (95) prioritize conventional mechanized/air breakthrough into Babylon's core before they build spaceship parts. Slightly increased Espionage (85) leverages extensive spy networks in Babylon for tech theft and counter-intelligence.

## Kimi-K2.5-Briefed - Turn 315 - retry 1

**Deviation (replay vs original):** use_nuke `-80`, nuke `-80`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> FINAL GAMBLE - Indonesia wins in 12 turns. Maximum priority to Naval and Airlift for immediate unit transport to Indonesian theater. Nuke 100/UseNuke 100 - we MUST build nuclear weapons if possible, only realistic way to destroy cities and tourism infrastructure before victory. Science 100 to reach nuclear tech faster. Espionage 100 - spies MUST target cultural/tourism buildings in Jakarta/Denpasar/Makassar to reduce tourism output directly. Abandoning Denmark/England fronts entirely - all units to Indonesia NOW.

- Replay: use_nuke 90 => 20 (Δ -70), nuke 90 => 20 (Δ -70)
> Revised threat assessment: Indonesia minimum 136 turns from cultural victory. Abandoning failed emergency mobilization for sustainable long-term buildup. Prioritizing Science, Production, Growth, Infrastructure, and naval investment to close tech gap and prepare real transoceanic invasion capacity. Culture increased to resist tourism long-term. Expansion re-enabled for strategic settling. Nuke priority eliminated as unnecessary panic measure.

## Kimi-K2.5-Briefed - Turn 420 - retry 2

**Deviation (replay vs original):** use_nuke `-80`, nuke `-100`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> CONSOLIDATION FOR FINAL PUSH: Economy stabilized (763G, +5 GPT) allows balanced approach. INCREASE Defense 90→95, Mobilization 60→70, Production 85→90 for Korean front reinforcement. INCREASE Offense 25→30, Mobile 15→20 for limited counter-attacks against depleted Korean forces (destroyed SAM, cruisers, destroyers). INCREASE UseNuke 70→80, maintaining 100 Nuke flavor for deterrent. INCREASE Diplomacy 80→90 for URGENT Brussels protection and World Congress preparation. DECREASE Gold 70→60 (crisis ended). With 7 turns until Decolonization vote, maximizing defensive capacity while preserving diplomatic flexibility for delegate acquisition is paramount. Korea's 8-tech lead demands we hold ground while catching up scientifically.

- Replay: use_nuke 70 => 0 (Δ -70), nuke 100 => 0 (Δ -100)
> NUCLEAR REALITY + DIPLOMATIC SURGE + SUPPLY GAP: Set Nuke/UseNuke to 0 (confirmed 0 uranium - impossible to build). Increase Mobilization to 75 to address severe under-manning (26/84 supply) vs Korea's 16,795 strength. Increase Growth to 85 (population drives science for spaceship race). Increase Gold to 80 and Diplomacy to 85 for post-Decolonization city-state envoy purchasing spree in 6 turns. Keep Science/Spaceship/Production/Air/Antiair/Defense/CityDefense at max. Slight Offense increase to 30 authorizes limited air counter-strikes against depleted Korean units.

## GLM-4.7-Simple - Turn 459 - retry 3

**Deviation (replay vs original):** use_nuke `-80`, nuke `-80`

- Original: use_nuke 75 => 80 (Δ +5), nuke 80 => 85 (Δ +5)
> Maximize Spaceship (100) and Production (100) to complete SS Cockpit next. Increase Defense (85) and CityDefense (80) as war with Carthage continues near our cities (Beijing, Guangzhou, Nanjing). High Ranged (85) and Air (85) for tactical superiority shown in recent naval victories (destroyed 2 Sensor Combat Ships, 1 Missile Cruiser). Maintain nuclear deterrence (85/80) against Inca who used nukes against our vassal. Raise Gold (75) for potential city-state spending before World Congress vote. Diplomacy (75) and Espionage (85) to monitor rivals and protect science cities during voting turn.

- Replay: use_nuke 75 => 0 (Δ -75), nuke 80 => 5 (Δ -75)
> We are approximately 7 turns away from completing the final three spaceship parts. Our sole priority is ensuring uninterrupted production and avoiding any catastrophic diplomatic or military escalation during this window. Drastically lowering Nuke and UseNuke to 5 and 0 eliminates the risk of staff authorizing nuclear strikes against Carthage or others, which could trigger global retaliation and derail the Science Victory. Raising CityDefense to 80 and Science to 95 provides additional protection and marginal research speed. Slightly reducing Diplomacy to 60 reflects a necessary inward focus on spaceship completion rather than competing for city-state influence.

## GLM-4.7-Simple - Turn 362 - retry 3

**Deviation (replay vs original):** use_nuke `-80`, nuke `-95`

- Original: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> Adjusting for strategic balance: Defensive posture against two nuclear-armed enemies (Ethiopia, Netherlands). Happiness prioritized to 100 - critical at 42% with combat penalty affecting all operations. NavalRecon increased to 90 - enhanced Ethiopian Submarine/Destroyer activity detection around Ur and coastal cities. Nuke/UseNuke raised to 95/80 - matching Ethiopia Manhattan Project urgency, nuclear deterrence is now primary security requirement. Switched to Conquest grand strategy to better coordinate multi-front war management while maintaining Spaceship. Diplomacy increased to 75 - World Congress voting in 5 turns against Netherlands sanctions needs support. Espionage at 90 - Ethiopian spies detected in Halab, Harran, Kar-Tukulti-Ninurta require counter-intelligence.

- Replay: use_nuke 75 => 0 (Δ -75), nuke 90 => 0 (Δ -90)
> Happiness (100) is paramount to remove combat penalties. Science, Spaceship, and Air (90) stay maxed for victory progress. Nuke and UseNuke drop to 0 due to lack of Uranium. Mobile and Naval families are reduced because of Oil constraints and unfavorable naval balances. Production and MilitaryTraining remain high to upgrade and defend. Diplomacy is raised slightly to secure trade routes and city-state allies.

## GLM-4.7-Simple - Turn 431 - retry 1

**Deviation (replay vs original):** use_nuke `-80`, nuke `-100`

- Original: use_nuke 75 => 80 (Δ +5), nuke 100 => 100 (Δ +0)
> After Brazil destroyed 3 anti-air units and continues nuclear-submarine attacks, increased Defense/CityDefense/Antiair/UseNuke to MAX for survival against two nuclear-armed superpowers. Mobilization 70 for replacing lost units. Production 100 for reconstruction. Science 100 for Spaceship path despite devastation. Gold 90 (economy -95 GPT deficit) for purchasing units/buildings. Happiness 100 - we're Unhappy with combat penalties, must prioritize. Espionage 100 - critical for intelligence on nuclear threats. Diplomacy 90 - World Congress in 7 turns, need delegates. Air 50 - build bombers for deterrence. GreatPeople 80 for Spaceship components. Decreased Growth and Navals as resources diverted to immediate survival.

- Replay: use_nuke 75 => 0 (Δ -75), nuke 100 => 0 (Δ -100)
> Post-nuclear survival adjustments after losing Mobile SAM and multiple AA guns: Zeroed Nuke/UseNuke (no Uranium, wasted priority). Raised Gold to 100 (GPT crashed to -95, economy collapsing). Raised Growth to 85 and TileImprovement to 50 (Uxmal population devastated 29->15, fallout cleanup urgent). Raised Ranged to 70 (Machine Guns require no Aluminum, unlike Mobile SAMs). Lowered MilitaryTraining to 30 (no gold for upgrades), Naval to 20, and zeroed Wonder/Religion/Recon/Mobile to focus scarce production. Maintain maximum Defense/CityDefense/Antiair/Production/Happiness against Brazil's 108K military and atomic bombs. Science/Spaceship/Espionage remain high for only viable long-term win path.

## GLM-4.7-Simple - Turn 431 - retry 3

**Deviation (replay vs original):** use_nuke `-80`, nuke `-100`

- Original: use_nuke 75 => 80 (Δ +5), nuke 100 => 100 (Δ +0)
> After Brazil destroyed 3 anti-air units and continues nuclear-submarine attacks, increased Defense/CityDefense/Antiair/UseNuke to MAX for survival against two nuclear-armed superpowers. Mobilization 70 for replacing lost units. Production 100 for reconstruction. Science 100 for Spaceship path despite devastation. Gold 90 (economy -95 GPT deficit) for purchasing units/buildings. Happiness 100 - we're Unhappy with combat penalties, must prioritize. Espionage 100 - critical for intelligence on nuclear threats. Diplomacy 90 - World Congress in 7 turns, need delegates. Air 50 - build bombers for deterrence. GreatPeople 80 for Spaceship components. Decreased Growth and Navals as resources diverted to immediate survival.

- Replay: use_nuke 75 => 0 (Δ -75), nuke 100 => 0 (Δ -100)
> Remove Nuke/UseNuke priorities (zero uranium). Shift focus to economic recovery (Gold 100, Happiness 100) and defensive rebuilding (Defense/CityDefense/Antiair). Maintain Production and Science for long-term survival. Increase TileImprovement for fallout cleanup and repair. Reduce Naval/Air priorities due to lack of strategic resources and overwhelming enemy superiority.

## Kimi-K2.5-Simple - Turn 406 - retry 1

**Deviation (replay vs original):** use_nuke `-85`, nuke `-95`

- Original: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> Cultural Victory is imminent - need Citizen Earth Protocol completion. Maximum defensive posture (Defense 95, CityDefense 95) to hold against Indian XCOM/Helicopter attacks while wonder is built. Nuke/UseNuke at 95/85 for MAD deterrent against further Indian nuclear strikes. Production 100 and Wonder 100 essential for rushing Citizen Earth Protocol. Reduced Offense to 5 - no need to attack when victory comes from wonder completion. Science 70 to reach Advanced Ballistics for nuclear deterrent. All resources focused on defensive survival and wonder production.

- Replay: use_nuke 80 => 0 (Δ -80), nuke 90 => 0 (Δ -90)
> Raising Science flavor to 80 prioritizes research infrastructure and Great Scientists to reach The Internet/Citizen Earth Protocol faster. Removing Nuke and UseNuke (set to 0) because Polynesia possesses no Uranium, making nuclear weapons impossible; these flavors were completely wasted. Boosting Defense, CityDefense, Air, and Antiair reinforces the collapsing Raiatea front and protects core cities against India's XCOM paradrops, helicopter gunships, and jet fighters. Grand Strategy remains Culture focused on the endgame victory condition.

## Deepseek-3.2-Simple - Turn 369 - retry 2

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Increasing UseNuke and Nuke flavors to maximum ensures the in-game AI prioritizes nuclear arsenal buildup and aggressive nuclear strike planning once we unlock Atomic Bombs. This aligns with our imminent war against China and The Maya, where nuclear weapons will be decisive in overcoming their numerical and defensive advantages. All other military and economic flavors remain high to sustain multi-front warfare and rapid conquest.

- Replay: use_nuke 80 => 0 (Δ -80), nuke 90 => 0 (Δ -90)
> Our peace treaty with China blocks them from honoring their defensive pact with The Maya for roughly 14 turns, creating a critical window to strike The Maya by sea and air without Egyptian intervention. We are deprioritizing nuclear weapons because we currently lack Uranium, and instead maximizing naval power, naval reconnaissance, and conventional offense for an amphibious coastal campaign. Diplomacy is raised to utilize our new Great Diplomat and secure World Congress delegates ahead of the vote in 9 turns. Production, science, gold, happiness, and espionage remain top priorities to sustain the war machine.

## Kimi-K2.5-Simple - Turn 428 - retry 1

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 428 STATE: Nuclear interception failed but conventional assault succeeding - eliminated multiple Maya anti-air units. Palenque bombardment continuing effectively (city at 20% health). Still 8 turns until Brazil wins via Cultural Victory over Maya. ALL Four Maya cities must fall by turn 436 or game over. MAXIMUM AGGRESSION CONTINUES: Production/Mobilization at 100 for unit replacement, Air/Ranged at 100 for bombardment, UseNuke increased to 100 (emergency tactical nuke if conventional assault stalls on Palenque's 42-population defense). Spaceship backup at 100 - may need to pivot to Great Engineer rushes if conquest fails. No territory expansion, no wonders, no culture - only war production and city capture.

- Replay: use_nuke 80 => 0 (Δ -80), nuke 100 => 0 (Δ -100)
> EMERGENCY PIVOT: Brazil is 5/6 Influences and needs only Maya. If Maya is eliminated, required civs drop from 6 to 5, and Brazil already influences the other 5 — triggering INSTANT CULTURAL VICTORY for Brazil. Maya must survive at all costs. Switching Grand Strategy to Spaceship is the only viable alternate path. Cities must prioritize spaceship parts immediately after current queues complete; military conquest is now strategically catastrophic.

## Kimi-K2.5-Simple - Turn 408 - retry 2

**Deviation (replay vs original):** use_nuke `-95`, nuke `-95`

- Original: use_nuke 80 => 95 (Δ +15), nuke 90 => 100 (Δ +10)
> INCREASE military pressure to force immediate peace or rapid victory against Zulus, then pivot to full spaceship production. Offense 75→85, Mobilization 65→75, Production 90→95 to expedite war conclusion within 5-10 turns maximum. Nuke 90→100 and UseNuke 95 for tactical nuclear strikes if Zulus refuse peace - cannot allow prolonged war. Science remains 100, Spaceship 100 as absolute priority. Growth 80→90 and Happiness 85 to counteract war weariness effects and prepare for post-war recovery. If peace achieved next turn, these flavors immediately shift to Production 100/Spaceship 100 focus. The war MUST end - Russia has 75 techs (ahead) and massive 45658 military vs my 24990.

- Replay: use_nuke 80 => 0 (Δ -80), nuke 90 => 5 (Δ -85)
> PIVOT slightly away from total war and toward spaceship production while maintaining enough pressure to secure Zulu peace. Nuke/UseNuke slashed to 5/0: we likely lack sufficient uranium (showing -2 in resources) and using nuclear weapons before World Congress would generate catastrophic warmonger penalties with Order bloc allies. Offense lowered from 75→70 and Defense raised to 45 since we need to minimize casualties to reduce war weariness accumulation and signal a willingness to end hostilities. Production boosted 90→95: spaceship parts are production-intensive and must begin immediately after Advanced Ballistics completes. Growth 80→85 helps cities recover from war losses. Science and Spaceship remain at maximum 100. CityDefense 50 ensures home cities and science infrastructure are secure from any opportunistic attacks while our military is engaged with the Zulus.

## Deepseek-3.2-Simple - Turn 469 - retry 3

**Deviation (replay vs original):** use_nuke `-90`, nuke `-80`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> The Netherlands is at 84% diplomatic victory; we must accelerate capture of Polynesian capitals (Honolulu, Assur) to achieve domination before they win. Increasing UseNuke and Nuke flavors prepares for nuclear strikes if conventional assault fails. Maintaining maximum Offense, Defense, Mobilization ensures continuous unit production. Science and Gold are critical for researching Stealth Bombers and purchasing units. Happiness offsets war weariness, and Espionage protects our science cities.

- Replay: use_nuke 90 => 10 (Δ -80), nuke 90 => 20 (Δ -70)
> Netherlands is at 83% science victory and pressing our western border with a Giant Death Robot, while Polynesia masses 9800+ strength on our southern frontier. We must focus flavors on pure military survival and offensive action: maximum Offense/Mobilization/CityDefense/Air for Stealth Bombers and urban warfare, while slashing Nuke/UseNuke because we only have 1 Uranium. Science and Gold remain important but are deprioritized slightly to sharpen military focus.

## GLM-4.7-Simple - Turn 397 - retry 3

**Deviation (replay vs original):** use_nuke `-90`, nuke `-95`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> CRITICAL: Jeonju captured by Persia this turn. Defensive posture increased to absolute maximum (100) - Seoul zone under Persian attack with 7,216 enemy strength vs 3,637 friendly. Jerusalemdefense (100) and CityDefense (100) prioritized to protect remaining 3 cities. Mobilization (95) and Production (95) increased to rush defensive units (Mobile SAMs, Mechanized Infantry) and rebuild military. Offensive capability increased to 45 (from 30) - may need limited counteroffensive to push Persian forces back from Seoul. Naval decreased to 88 (from 92) - lost Jeonju naval base, focusing on land/air defense now. UseNuke increased to 90 (from 85) - existential threat justifies tactical nuclear response if Seoul or Busan threatened. Science (100) maintained - must continue spaceship progress despite war to achieve alternative victory. Diplomacy (60) - World Congress vote in 10 turns, focus on survival. Espionage (85) maintained - spies in Persian cities critical for technology recovery and intelligence.

- Replay: use_nuke 85 => 0 (Δ -85), nuke 95 => 0 (Δ -95)
> With Jeonju fallen and Persia influential over all civilizations (imminent cultural victory via Citizen Earth Protocol), Korea faces an existential race between Persian cultural completion and Korean spaceship launch. Reset Nuke/UseNuke to 0—Korea possesses zero Uranium, making nuclear weapons impossible. Maximize Spaceship (100), Science (100), and Production (95) to rush techs and components. Maintain Defense/CityDefense/Antiair at 100 to protect Seoul, Busan, and Daegu from Persian air and naval assault. Espionage raised to 95 to direct spy networks (Bactra, Adrianople, Nicaea, Pasargadae, Susa) toward sabotaging Persian production, particularly any attempt at the Citizen Earth Protocol wonder. Reduced Wonder and Culture to deprioritize non-essential construction.

## Kimi-K2.5-Briefed - Turn 315 - retry 2

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> FINAL GAMBLE - Indonesia wins in 12 turns. Maximum priority to Naval and Airlift for immediate unit transport to Indonesian theater. Nuke 100/UseNuke 100 - we MUST build nuclear weapons if possible, only realistic way to destroy cities and tourism infrastructure before victory. Science 100 to reach nuclear tech faster. Espionage 100 - spies MUST target cultural/tourism buildings in Jakarta/Denpasar/Makassar to reduce tourism output directly. Abandoning Denmark/England fronts entirely - all units to Indonesia NOW.

- Replay: use_nuke 90 => 0 (Δ -90), nuke 90 => 0 (Δ -90)
> Landship timeline debunked by briefings - zero coal and resource alerts make Combustion/Landship rush impossible. However, Indonesia remains the existential tourism threat with 405 TPT. With 54 active units but only 2 attacking Indonesia, the staff members must launch an immediate full amphibious offensive. Slash homeland defense to 15 (England war is nominal at 0% score, Austria is at 100% weariness peace, Denmark is distant) to free garrison units for the Indonesian front. Culture raised to 60 to directly extend the turns-to-Influential defensive timer. Zero air/nuke flavors - impossible in Industrial Era without resources. Maintain maximum Naval, Offense, Mobilization, Gold, and Production to execute sustained naval invasions and secure long-term production infrastructure once coal is acquired.

## Kimi-K2.5-Simple - Turn 417 - retry 1

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Pure survival mode: Eliminated Offense (0) since attacking is suicide. Maximized UseNuke (100) - must deploy tactical nukes against Aztec XCOM/Modern Armor stacks at Carthago Nova or lose the city. Increased Mobile (80) to prepare for Mechanized Infantry deployment. Maintained max Defense, Antiair (jet attacks are relentless), and Espionage (critical science quests in Panama City and Sokoto worth 1,000+ science each). Apollo Program completes in 5 turns - must transition immediately to parts production.

- Replay: use_nuke 90 => 0 (Δ -90), nuke 100 => 0 (Δ -100)
> Zeroing Nuke and UseNuke because we possess no Uranium, making nuclear weapons impossible to build; this redirects production priority to viable units and economic assets. Raising Happiness from 40 to 60 to prioritize happiness infrastructure and mitigate severe empire unhappiness (47%) and war weariness that are crippling combat effectiveness and growth. Spaceship grand strategy remains our only plausible victory path. All other survival flavors (Defense 100, Gold 100, Espionage 100, Production 100, Science 100) remain unchanged as the Aztec existential threat continues.

## Kimi-K2.5-Simple - Turn 417 - retry 3

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Pure survival mode: Eliminated Offense (0) since attacking is suicide. Maximized UseNuke (100) - must deploy tactical nukes against Aztec XCOM/Modern Armor stacks at Carthago Nova or lose the city. Increased Mobile (80) to prepare for Mechanized Infantry deployment. Maintained max Defense, Antiair (jet attacks are relentless), and Espionage (critical science quests in Panama City and Sokoto worth 1,000+ science each). Apollo Program completes in 5 turns - must transition immediately to parts production.

- Replay: use_nuke 90 => 0 (Δ -90), nuke 100 => 0 (Δ -100)
> Shifting to pure defensive survival posture. Zero Uranium makes nuclear weapons impossible, so Nuke/UseNuke deprioritized to 0. Offense set to 0 since Satsuma is being razed and we cannot attack the Aztec horde. Mobilization lowered to 60 to curb runaway unit maintenance contributing to our catastrophic -252 GPT deficit, while preserving capacity to replace losses. Air/Airlift raised to prioritize fighter defense of core cities. Happiness raised to 85 to combat 47% empire unhappiness that inflicts combat penalties on our beleaguered troops.

## Kimi-K2.5-Simple - Turn 482 - retry 3

**Deviation (replay vs original):** use_nuke `-95`, nuke `-100`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> NINEVEH FALLEN - EMERGENCY SURVIVAL MODE: Rome captured Nineveh on Turn 480 (23 population city lost). Portugal's diplomatic victory FAILED (still at 35/43 delegates). Rome now at war with me AND Ottomans. With 1,505 vs 52,754 military strength, direct confrontation is impossible. PIVOT TO SPACESHIP as only viable path - Science 100, Spaceship 80. Continue Defense 100, CityDefense 100, Nuke 100 with UseNuke 95 for area denial. Must survive long enough to reach Information era and build spaceship components while Rome's attention splits between me and Ottomans.

- Replay: use_nuke 90 => 0 (Δ -90), nuke 100 => 0 (Δ -100)
> POST-NINEVEH SURVIVAL CRISIS: Rome captured Nineveh Turn 480 despite maximum defensive posture. Down to 6 cities with 1,505 military versus Rome's 52,754. Next Global Hegemony vote ~10 turns away; Portugal at 35/43 delegates. Keeping UnitedNations grand strategy but adjusting flavors for pure survival. Zeroed Nuke/UseNuke due to zero Uranium reserves. Raised Air 95, Ranged 85, Mobilization 95 for defensive combat. Raised Production 90, Science 85, Gold 80 to rebuild and address -71 GPT deficit. Increased Happiness to 70 for war weariness mitigation. Lowered Diplomacy to 70 as city-state influence erodes under Roman military pressure. Spaceship 40 begins contingency pivot if diplomacy fails.

## Kimi-K2.5-Simple - Turn 482 - retry 2

**Deviation (replay vs original):** use_nuke `-95`, nuke `-100`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> NINEVEH FALLEN - EMERGENCY SURVIVAL MODE: Rome captured Nineveh on Turn 480 (23 population city lost). Portugal's diplomatic victory FAILED (still at 35/43 delegates). Rome now at war with me AND Ottomans. With 1,505 vs 52,754 military strength, direct confrontation is impossible. PIVOT TO SPACESHIP as only viable path - Science 100, Spaceship 80. Continue Defense 100, CityDefense 100, Nuke 100 with UseNuke 95 for area denial. Must survive long enough to reach Information era and build spaceship components while Rome's attention splits between me and Ottomans.

- Replay: use_nuke 90 => 0 (Δ -90), nuke 100 => 0 (Δ -100)
> NINEVEH CAPTURED BY ROME - EMERGENCY 10-TURN SURVIVAL MODE: Rome seized Nineveh on Turn 480 and presses the offensive with 52,754 military against my 1,505 strength. World Congress reconvenes in approximately 10 turns; Portugal holds 35/43 delegates and can achieve victory with my 13 delegate support, ending the game before Rome razes my remaining core cities. Deprioritized Nuke/UseNuke to 0 because my empire has zero available uranium. Maintained maximum Defense/CityDefense/Antiair flavors. Increased Air to 90, Ranged to 90, and Production to 90 to maximize defensive unit output. Boosted Science to 80 to reach Stealth technology faster for Stealth Bomber defense. Raised Gold to 75 to mitigate critical -71 GPT deficit. Slightly reduced Diplomacy to 75 since immediate military survival outweighs city-state questing, but kept high enough to maintain Portuguese alliance for the decisive upcoming vote. GrandStrategy remains UnitedNations because Portuguese diplomatic victory is now the only realistic path to endgame that preserves my civilization's score before further Roman annexation.

## Kimi-K2.5-Simple - Turn 482 - retry 1

**Deviation (replay vs original):** use_nuke `-95`, nuke `-100`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> NINEVEH FALLEN - EMERGENCY SURVIVAL MODE: Rome captured Nineveh on Turn 480 (23 population city lost). Portugal's diplomatic victory FAILED (still at 35/43 delegates). Rome now at war with me AND Ottomans. With 1,505 vs 52,754 military strength, direct confrontation is impossible. PIVOT TO SPACESHIP as only viable path - Science 100, Spaceship 80. Continue Defense 100, CityDefense 100, Nuke 100 with UseNuke 95 for area denial. Must survive long enough to reach Information era and build spaceship components while Rome's attention splits between me and Ottomans.

- Replay: use_nuke 90 => 0 (Δ -90), nuke 100 => 0 (Δ -100)
> NINEVEH FALLEN - RESOURCE-CONSCIOUS DESPERATION DEFENSE: Post-capture analysis reveals zero Uranium and Aluminum reserves, invalidating prior nuclear/Stealth deterrent strategies. Redirecting all strategic priority to conventional survival ahead of the imminent World Congress vote. Maxing Ranged, Air, Production, and Mobilization to generate defensive units for immediate city garrisons. Cutting Science, Growth, and Diplomacy to fund emergency war production. UnitedNations grand strategy maintained solely to preserve delegate alignment for Portugal's decisive victory.

## Kimi-K2.5-Simple - Turn 373 - retry 1

**Deviation (replay vs original):** use_nuke `-95`, nuke `-75`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 373: Nuclear Fission completed - we now have nuclear weapons for deterrence. War with Russia continues at +4% score (favorable). Major shift: reducing Offense to 25 (was 35) as we pursue defensive war only. UseNuke increased to 95 - we have actual nukes now and Russia is pushing into our territory. Reduced Espionage to 90 (was 95) - we have good network coverage. Increased Diplomacy to 90 (was 85) - World Congress vote in 7 turns for our World Ideology: Freedom proposal is critical. Must secure Korea (10 votes), Inca (9), and Babylon (16). Maintained maximum Science priority (100) - Korea overtook us 67-66, cannot afford to fall behind in tech race.

- Replay: use_nuke 90 => 0 (Δ -90), nuke 100 => 25 (Δ -75)
> Turn 373: Completed Nuclear Fission. Critical discovery: Poland has NO Uranium resources, making nuclear weapons impossible to build. Reduced Nuke:100→25 and UseNuke:90→0 to avoid wasting production on Manhattan Project (which would enable enemy nukes without benefiting us). Redirected focus to conventional power: increased Air:75→85 and Mobile:75 for Winged Hussar/fighter dominance, Ranged:55→65 for Light Tank/Machine Gun support. Maintain Science:100 and Spaceship grand strategy to catch Korea (67 vs 66 techs).

## Qwen-3.5-Simple - Turn 484 - retry 1

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: CRITICAL - Iroquois declared war on us along with 4 city-state allies (Kabul, Venezia, Prague, Samarkand). We face 5+ enemies simultaneously with military severely outnumbered (our 1,139 vs Iroquois 41k, Ottomans 12k, Aztecs 9k). Maintaining maximum Defense/Mobilization for survival. Nuke flavors at 100% - need nuclear deterrent against overwhelming forces. Iroquois at 46 delegates (needs 43) with 16 turns remaining - existential diplomatic threat. Must conquer their city-state allies to flip delegates while defending our cities. Germany (15) + Mongolia (15) alliance critical to block Iroquois World Congress proposals.

- Replay: use_nuke 95 => 0 (Δ -95), nuke 100 => 0 (Δ -100)
> TURN 484: PURE CITY DEFENSE PROTOCOL. Iroquois (41k military) declared war; 16 turns to game end. Zero offensive capability against 5 enemies. Flavors adjusted to pure survival: max Defense/CityDefense/Antiair/Production/Happiness. Nuke and spaceship flavors zeroed (impossible in timeframe). Naval/airlift minimized. Diplomacy prioritized to pursue peace. Every unit must defend core 4 cities; losing any city devastating to final score.

## Kimi-K2.5-Simple - Turn 439 - retry 2

**Deviation (replay vs original):** use_nuke `-100`, nuke `-80`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> FINAL EMERGENCY: World Congress in 4 turns. Austria has 45/40 delegates. Offense reduced to 10 and Mobile to 10 to COMPLETELY STOP attacking The Inca. Defense at 95 for self-protection only. UseNuke at 100 to signal willingness to escalate and force peace negotiations. Maximum Production/Air/Nuke maintained for potential final strike against Austria if The Inca succeeds at Attila's Court. The ONLY priority is ensuring The Inca captures Attila's Court - every Assyrian unit should withdraw from Inca contact and let them pass north to The Huns.

- Replay: use_nuke 95 => 0 (Δ -95), nuke 100 => 20 (Δ -80)
> Pivoting from Conquest to Spaceship grand strategy. In 4 turns Austria will achieve diplomatic victory unless The Inca captures Attila's Court—an outcome we cannot directly influence. If Austria is blocked, the endgame becomes a science race; if not, all strategies fail. Therefore maximizing Spaceship 100, Science 100, and Production 100 prioritizes the only viable victory path. Offense reduced to 0 with Defense 80 to immediately halt all aggression against The Inca, allowing their 26,694 strength to focus on The Huns. Nuke and UseNuke reduced to avoid wasting production on weapons irrelevant to a science race.

## Kimi-K2.5-Simple - Turn 439 - retry 1

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> FINAL EMERGENCY: World Congress in 4 turns. Austria has 45/40 delegates. Offense reduced to 10 and Mobile to 10 to COMPLETELY STOP attacking The Inca. Defense at 95 for self-protection only. UseNuke at 100 to signal willingness to escalate and force peace negotiations. Maximum Production/Air/Nuke maintained for potential final strike against Austria if The Inca succeeds at Attila's Court. The ONLY priority is ensuring The Inca captures Attila's Court - every Assyrian unit should withdraw from Inca contact and let them pass north to The Huns.

- Replay: use_nuke 95 => 0 (Δ -95), nuke 100 => 0 (Δ -100)
> TURN 438: Final score-maximization pivot. With Global Hegemony voting in 4 turns and Austria holding 45 delegates against a 40 threshold, conventional military or diplomatic victory is blocked. Priority shifts entirely to civilization development score: Production 100 rushes nearly-complete buildings (Strategic Defense System, Stadium, etc.), Science 100 pushes Alternative Energy completion for technology points, Growth 100 maximizes population score, and Happiness 100 combats current unhappiness penalties. Offense 0 / Defense 100 / CityDefense 100 orders an immediate cessation of offensive operations against The Inca and withdrawal to Assyrian borders, preserving existing military strength score instead of sacrificing units in futile foreign incursions. GrandStrategy shifted to Spaceship to align staff priorities with science, food, and production output.
