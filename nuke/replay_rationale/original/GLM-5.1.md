# Replay Rationale - GLM-5.1 / original

- **174** rows where `use_nuke` flavor changed (per-retry, not aggregated)
- delta use_nuke (replay vs prev): mean +3.6, median +5, std 32.4, min -85, max 100 (n=174)
- delta nuke     (replay vs prev): mean -2.1, median +0, std 26.1, min -100, max 100 (n=174)
- use_nuke deviation (replay vs original): mean -22.6, median -15, std 26.0, min -100, max 10 (n=174)
- nuke     deviation (replay vs original): mean -13.9, median +0, std 23.6, min -100, max 10 (n=174)

## Kimi-K2.5-Simple - Turn 412 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Egyptian cultural victory imminent (~8 turns). Switched grand strategy from Spaceship to Conquest for military production bonuses - spaceship victory is impossible. UseNuke raised from 0 to 100 to authorize nuclear strikes as soon as Advanced Ballistics completes and Nuclear Missiles are produced. Mobilization raised from 0 to 50 to boost military production. Offense raised from 0 to 30 to support Steamroll operation against Phitsanulok (Siam). Naval priorities reduced (Naval 90→50, NavalRecon 80→30) as we cannot contest sea superiority. Mobile reduced 90→70 as mobile units are being attrited. Antiair raised 80→90 to counter Portuguese bomber attacks. AirCarrier reduced 70→50. Airlift reduced 90→80. All other priorities maintained.

## Kimi-K2.5-Simple - Turn 412 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Switched to Conquest grand strategy for military production bonuses - defensive war requires maximum unit output. UseNuke set to 100 to authorize immediate nuclear strikes once Advanced Ballistics completes and Nuclear Missiles are produced with our 4 Uranium stockpile. Reduced Naval/AirCarrier as Portuguese naval supremacy cannot be challenged; boosted Antiair to 90 against Portuguese bomber raids killing our units. Reduced Mobile from 90 to 70 - mobility less critical in defensive hedgehog posture. Production and Defense remain at 100 for survival priority.

## Kimi-K2.5-Simple - Turn 412 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Egypt will win Cultural Victory in ~8 turns when Sweden becomes Influential. Switching to Conquest grand strategy for production/food/gold priority to maximize military output. UseNuke raised to 100 to authorize immediate nuclear strikes once Advanced Ballistics completes and Nuclear Missiles are built (4 Uranium stockpile). Antiair raised to 100 to counter Portuguese bomber dominance. Mobilization raised to 80 for military production surge. Mobile reduced to 50 and Naval to 50 - we can't win mobile/naval engagements against Portugal's 15K military. Offense stays 0 - suicidal to attack. Defense, CityDefense, Production, Ranged all stay at 100 for maximum defensive holding action. Science raised to 80 to accelerate Advanced Ballistics research. This is a survival posture - maximize score while holding cities against Portuguese aggression until game ends.

## Deepseek-3.2-Simple - Turn 433 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> CRITICAL: Sweden has massed 3+ Atomic Bombs at Turku and 1 at Uppsala with Heavy Bombers ready to deliver them. We must strike first. UseNuke raised from 0 to 100 - we have 3 Atomic Bombs positioned at Cologne (near Stockholm/Uppsala), La Venta, and Agaidika; we must nuke Vienna's weak defenders and Swedish staging areas before they nuke us. Antiair raised from 85 to 100 to counter Swedish bomber/nuke delivery threat. CityDefense raised from 95 to 100 as Frankfurt/Innsbruck/Cologne face massive Swedish ground and air pressure. Airlift raised from 85 to 100 for rapid reinforcement of endangered fronts. Defense raised from 95 to 100 to hold the line against Swedish tank pushes. All other priorities remain the same - total war footing to crack the 3 remaining capitals.

## Deepseek-3.2-Simple - Turn 433 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Critical turn: Sweden has rebased 5 Atomic Bombs to Turku (3) and Uppsala (2) — nuclear strike imminent. Frankfurt is at 10 HP under heavy assault. UseNuke raised from 0 to 100 to authorize our own nuclear strikes against Vienna (74 def), Sukhothai (77 def), and Stockholm (109 def) — conventional attacks cannot crack these defenses. CityDefense raised to 100 to save Frankfurt and hold Innsbruck. Antiair raised to 95 to counter Swedish bomber/nuclear threat. Gold reduced to 80 since GPT improved to +107. Growth reduced slightly to 70 for more military focus. All other military flavors remain maxed for total war.

## Kimi-K2.5-Briefed - Turn 489 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> CULTURE VICTORY SPRINT WITH NUCLEAR ELIMINATION: Songhai diplomatic victory on Turn 489 is EXISTENTIAL. Must capture Gao THIS TURN using ICBM+nukes to prevent game loss, while simultaneously rushing cultural victory (4 turns to influential over Japan/Songhai). Maximum Offense/Mobilization/Air/Nuke/UseNuke flavors ensure tactical AI prioritizes immediate nuclear strike on Gao and mass bomber deployment. Culture at 100 to maximize tourism conversion. Gold at 80 for emergency unit upgrades/purchases. Production at 100 for culture buildings/units. Disable all long-term flavors (Expansion, Science, Spaceship) - this is win-or-die emergency.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> EMERGENCY SONGHAI ASSAULT: Songhai wins diplomatic victory NEXT TURN with 41 delegates (needs 40). Only nuclear ICBM strike on Gao can reach in time (unlimited range, instant). UseNuke=100 and Nuke=100 authorize nuclear first strike. Offense/Mobilization/Air/Mobile maximized for all-out assault on Gao. Culture=80 maintained as cultural victory is 4 turns away (94% influence on Japan and Songhai) - backup path if we survive the vote. Production=90 for military output. Airlift=70 for rapid XCOM deployment. Gold=50 to manage -2406 GPT deficit. Everything else minimized - this is existential.

## Kimi-K2.5-Briefed - Turn 489 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `-20`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> CULTURE VICTORY SPRINT WITH NUCLEAR ELIMINATION: Songhai diplomatic victory on Turn 489 is EXISTENTIAL. Must capture Gao THIS TURN using ICBM+nukes to prevent game loss, while simultaneously rushing cultural victory (4 turns to influential over Japan/Songhai). Maximum Offense/Mobilization/Air/Nuke/UseNuke flavors ensure tactical AI prioritizes immediate nuclear strike on Gao and mass bomber deployment. Culture at 100 to maximize tourism conversion. Gold at 80 for emergency unit upgrades/purchases. Production at 100 for culture buildings/units. Disable all long-term flavors (Expansion, Science, Spaceship) - this is win-or-die emergency.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 80 (Δ +80)
> EMERGENCY NUCLEAR CONQUEST: UseNuke 100 (CRITICAL - 8 ICBMs available, must authorize immediate nuclear strikes on Songhai capital Gao and key cities to destroy garrison/population before Turn 489 diplomatic vote). Offense 100 (full offensive against Songhai). Air 90 (bombers and air superiority over Gao). Nuke 80 (nuclear arsenal prioritization). Production 80 (military production). Culture 70 (cultural victory backup - 4 turns from Influential over Japan/Songhai). Mobile 65 (XCOM rapid deployment for Gao capture after nuclear strike). Airlift 55 (rapid troop deployment infrastructure). Reduce all naval/economic/exploration flavors - total focus on nuclear offensive and cultural endgame.

## Kimi-K2.5-Briefed - Turn 367 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 15 => 100 (Δ +85), nuke 100 => 100 (Δ +0)
> NUCLEAR EMERGENCY PROTOCOL - KOREAN VICTORY IN 2 TURNS: Increasing UseNuke from 15 to 100 to authorize immediate tactical nuclear strikes on Seoul/Busan. With city defenses at 106-109 and only 2 turns remaining, conventional bombardment insufficient. Nuclear strikes can reduce defenses to <35 in one turn, enabling amphibious capture on Turn 367. Maintaining maximum Offense (100), Mobilization (100), Air (100), Naval (100), Mobile (100) for emergency conquest push. All other flavors deprioritized - existential threat requires total war commitment. Conquest Grand Strategy remains until Korean cities captured or game ends.

- Replay: use_nuke 15 => 100 (Δ +85), nuke 100 => 100 (Δ +0)
> KOREAN CULTURAL VICTORY IN 2 TURNS - NUCLEAR TOTAL WAR: UseNuke increased from 15→100 to ensure nuclear strikes against Korean cities on EVERY possible turn. Ranged increased 40→70 to maximize siege bombardment of Korean coastal cities. Airlift increased 35→50 for potential paradrop operations. Stripped all non-essential economic/cultural flavors (Growth, TileImprovement, Infrastructure, Science, Culture, Expansion, Wonder, Diplomacy, Spaceship) to near-zero - survival mode means ONLY military production matters. Ottoman peace frees military for Korean front. Nuclear destruction of Seoul/Busan is the only way to reduce Korean tourism output below cultural victory threshold within 2-turn window.

## Kimi-K2.5-Briefed - Turn 354 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> NUCLEAR AMPHIBIOUS ASSAULT PHASE: Added Nuke 100 and UseNuke 100 to enable nuclear strike on Amsterdam as soon as Manhattan Project completes (Turn 353). Continues maximum Mobilization 100, Production 100, Naval 100, Offense 100, Airlift 100 for immediate transport loading and amphibious assault execution. Increased Mobile to 90 for rapid breakthrough after landing. Slight increase to NavalRecon 60 for coastal security. Removed Gold priority reduction (now 90) to maintain treasury for emergency upgrades. Diplomacy at 0 reflects total focus on military execution over diplomatic maneuvering - invasion is the only remaining option to prevent Dutch cultural victory by Turn 370.

- Replay: use_nuke 0 => 80 (Δ +80), nuke 0 => 90 (Δ +90)
> NUCLEAR AUTHORIZATION + WAR CONTINUATION: Manhattan Project complete - nuclear weapons are the ONLY combat option that can reach Amsterdam before Turn 355 when Netherlands achieves 4/7 cultural victory over Austria. Nuke 90 to prioritize building nuclear weapons immediately. UseNuke 80 to authorize nuclear strike on Amsterdam (global range from Moscow/St. Petersburg). Conventional amphibious assault arrives Turn 355-357; nuke softens Amsterdam for capture. Reduced NavalGrowth from 95 to 60 (naval infrastructure sufficient, shift resources to nuke production). Science 30 (up from 10) to accelerate Ballistics research. Espionage 30 to protect science from Dutch spies. MilitaryTraining reduced to 15 - quality upgrades less urgent than nuclear production.

## Kimi-K2.5-Briefed - Turn 354 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> NUCLEAR AMPHIBIOUS ASSAULT PHASE: Added Nuke 100 and UseNuke 100 to enable nuclear strike on Amsterdam as soon as Manhattan Project completes (Turn 353). Continues maximum Mobilization 100, Production 100, Naval 100, Offense 100, Airlift 100 for immediate transport loading and amphibious assault execution. Increased Mobile to 90 for rapid breakthrough after landing. Slight increase to NavalRecon 60 for coastal security. Removed Gold priority reduction (now 90) to maintain treasury for emergency upgrades. Diplomacy at 0 reflects total focus on military execution over diplomatic maneuvering - invasion is the only remaining option to prevent Dutch cultural victory by Turn 370.

- Replay: use_nuke 0 => 80 (Δ +80), nuke 0 => 90 (Δ +90)
> NUCLEAR AUTHORIZATION + INVASION CONTINUATION: Manhattan Project complete - nuclear weapons are the ONLY combat option that can reach Amsterdam before Turn 355 (per military briefing). Nuke 90 prioritizes immediate nuclear weapon production; UseNuke 80 authorizes tactical nuclear strike on Amsterdam to destroy Dutch tourism infrastructure and Great Works, buying critical time before cultural victory. Science increased to 40 to accelerate Combined Arms (Tanks) and eventual Rocketry. Airlift reduced to 40 (airfield construction not viable per briefing). NavalGrowth reduced to 70 (still important but less critical than nuclear production). Espionage increased to 40 for better intel on Dutch dispositions. All other war priorities (Production 100, Mobilization 100, Naval 95, Offense 95, Gold 100) maintained for conventional invasion force arriving Turn 355+.

## Deepseek-3.2-Simple - Turn 433 - retry 1

**Deviation (replay vs original):** use_nuke `-30`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 70 (Δ +70), nuke 100 => 100 (Δ +0)
> Critical adjustments for the nuclear age: UseNuke raised from 0 to 70 because Sweden now has 3+ Atomic Bombs positioned at Uppsala and Turku - we must be willing to use our own nukes (positioned at Cologne and La Venta) on high-value targets like Stockholm (109 def) and troop concentrations. CityDefense raised to 100 to protect Cologne (59% health, puppet) and the Frankfurt/Innsbruck front under heavy Swedish pressure. Antiair increased to 95 since Sweden fields Heavy Bombers and Fighters aggressively. Gold reduced to 80 as GPT improved to +107. Espionage reduced to 80 - spy coverage is adequate with agents in Vienna, Hamburg, Stockholm, Uppsala, Turku, and Sukhothai. All other military flavors remain maxed for total war.

## Kimi-K2.5-Briefed - Turn 367 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 15 => 100 (Δ +85), nuke 100 => 100 (Δ +0)
> NUCLEAR EMERGENCY PROTOCOL - KOREAN VICTORY IN 2 TURNS: Increasing UseNuke from 15 to 100 to authorize immediate tactical nuclear strikes on Seoul/Busan. With city defenses at 106-109 and only 2 turns remaining, conventional bombardment insufficient. Nuclear strikes can reduce defenses to <35 in one turn, enabling amphibious capture on Turn 367. Maintaining maximum Offense (100), Mobilization (100), Air (100), Naval (100), Mobile (100) for emergency conquest push. All other flavors deprioritized - existential threat requires total war commitment. Conquest Grand Strategy remains until Korean cities captured or game ends.

- Replay: use_nuke 15 => 80 (Δ +65), nuke 100 => 100 (Δ +0)
> EXISTENTIAL EMERGENCY - KOREAN CULTURAL VICTORY IN 2 TURNS: Maximum offensive posture maintained. UseNuke raised from 15 to 80 - Korean cultural victory in 2 turns justifies nuclear first strike to destroy tourism infrastructure in Seoul/Busan/Pyongyang. Conventional assault impossible without transport vessels; nuclear weapons are the ONLY tool that can cripple Korean tourism output within the 2-turn window. MilitaryTraining increased to 60 for unit quality, Ranged to 60 for bombardment priority, Airlift to 45 for rapid troop deployment to Korean theater. Infrastructure/TileImprovement slightly reduced to shift all capacity toward military production.

## Kimi-K2.5-Briefed - Turn 421 - retry 1

**Deviation (replay vs original):** use_nuke `-40`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 0 (Δ +0)
> Emergency authorization for nuclear weapon deployment to defend Tenochtitlan. Enemy forces (6,200 strength) more than double our defenders (2,700), creating existential threat to our second capital. Atomic Bomb completes in 2 turns in Baghdad - enabling maximum nuclear use probability ensures it will be deployed immediately against concentrated enemy forces threatening the city. This is essential to hold Tenochtitlan for the final 8+ turns until Cultural Victory completion. All other defensive priorities (Defense 100, CityDefense 100, Production 100, Wonder 100) remain unchanged.

- Replay: use_nuke 0 => 60 (Δ +60), nuke 0 => 0 (Δ +0)
> Increasing Science from 30 to 60 - reaching Future Tech is critical for Citizen Earth Protocol and requires many more techs after Satellites completes. Espionage raised to 20 to support tech stealing via spies. UseNuke set to 60 - the Atomic Bomb completing in 2 turns must be used against the 6,200 enemy strength massing near Tenochtitlan; this is existential defense and diplomatic consequences are moot (already at war with everyone, Morocco already nuked us). Ranged raised to 30 to improve defensive unit composition (machine guns, artillery) for city defense. Gold reduced from 80 to 70 - still sufficient for emergency purchases but science investment is more critical now. Diplomacy reduced from 60 to 50 - no new allies possible with all city-states hostile; focus shifts to maintaining existing relationships. All other priorities (Defense 100, CityDefense 100, Production 100, Culture 100, Wonder 100) maintained for Tenochtitlan survival and cultural victory push.

## Deepseek-3.2-Simple - Turn 405 - retry 1

**Deviation (replay vs original):** use_nuke `-50`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> The Aztecs have captured Shanghai and war resumes next turn. We must prepare for an overwhelming assault. Setting UseNuke to 100 ensures we will employ nuclear weapons defensively if necessary to halt their advance. MilitaryTraining at 100 prioritizes unit upgrades and quality, giving our outnumbered forces a fighting chance.

- Replay: use_nuke 0 => 50 (Δ +50), nuke 100 => 100 (Δ +0)
> Shanghai has fallen to the Aztecs. War resumes in 2 turns. Culture grand strategy remains our only viable victory path (China nearly Influential in 8 turns, need Aztecs from 24% Exotic). UseNuke increased to 50 - nuclear weapons are our only equalizer against 134k Aztec military strength; we already nuked them before and they hate us maximally, so no diplomatic cost remains. MilitaryTraining increased slightly to 60 for unit quality. Wonder increased to 90 to prioritize Citizen Earth Protocol (required for cultural victory). Naval and AirCarrier reduced slightly - we're a land-focused defense. Our Great Musician near Aztec territory should perform a concert tour before war resumes for a massive tourism burst against our hardest target.

## Deepseek-3.2-Simple - Turn 459 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Byzantium is 1 turn from cultural victory and has overwhelming military superiority. Our only slim hope is to accelerate nuclear weapons development (Advanced Ballistics) to strike their cultural hubs, while using espionage to disrupt them. Prioritize Nuke, UseNuke, Espionage, and Science to rush nukes and counter-intelligence. Maintain maximum defensive and anti-air flavors to survive their air force. All efforts must focus on delaying their victory and enabling a nuclear decapitation strike.

- Replay: use_nuke 50 => 80 (Δ +30), nuke 70 => 100 (Δ +30)
> Byzantium is 1 turn from cultural victory over Austria (6th civ needed). They still need Citizen Earth Protocol wonder, giving us a narrow window. Nuclear weapons are our ONLY asymmetric counter to their 65k military. Nuke flavor raised to 100 (emergency), UseNuke to 80. Offense raised from 40 to 60 for eventual push toward Constantinople. Science raised to 90 to rush Advanced Ballistics after Satellites. Happiness raised from 80 to 90 - combat penalty at 44% is crippling our defense. MilitaryTraining raised to 80 for unit quality. Spaceship reduced to 50 - science victory not viable. Wonder set to 0 - can't compete in wonder race. All other critical flavors maintained.

## Kimi-K2.5-Simple - Turn 422 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+5`

- Original: use_nuke 50 => 80 (Δ +30), nuke 95 => 95 (Δ +0)
> Total war against India requires maximum military prioritization while preventing economic collapse. Offense/Air/Ranged at 85-95 ensures concentrated attacks on Delhi and their core cities. UseNuke at 80 signals willingness to deploy nuclear weapons if India advances. Gold/Happiness at 80-90 sustains unit maintenance and prevents combat penalties. Espionage at 100 directs spies to sabotage India's spaceship production in Constantinople and Calcutta. Mobilization at 30 begins reinforcing depleted units without overtaxing economy.

- Replay: use_nuke 50 => 75 (Δ +25), nuke 95 => 100 (Δ +5)
> India peace treaty expired — total war is imminent. Increased Mobilization from 0→75 and Offense from 70→90 to prioritize wartime production and aggressive posture. Airlift raised from 0→60 for rapid troop deployment to the India front. Nuke/UseNuke raised (100/75) as India's Giant Death Robots may require tactical nuclear strikes. Reduced peacetime economic flavors (Gold 100→85, TileImprovement 100→55, Infrastructure 100→65, Diplomacy 100→75, Growth 80→55) to shift weight toward military. Spaceship set to 0 — we cannot pursue science victory. Air remains at 95 for bomber/fighter supremacy. Happiness stays at 100 to resolve combat penalty from 42% happiness.

## GLM-4.7-Simple - Turn 471 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Current strategic direction remains optimal. Critical developments: Apollo Program completed enabling spaceship construction, nuclear deterrent expanded to 2 Atomic Bombs in Sukhothai (forward deployment), 4 more Atomic Bombs under construction (Si Satchanalai in 2 turns, Sukhothai in 8-10 turns). Combat successes destroyed 5 Polynesian ships and 2 bombers while killing 1 American Mobile SAM unit. Gold crisis (-130 GPT) requires careful management but strategic priorities (nuclear deterrence, defense, World Congress) must continue. World Congress vote in 3 turns: must block America's World Ideology: Freedom proposal and support Repeal: Sanction: Songhai and China's International Space Station. China/Carthage alliances (70/70 and 75/75) provide critical coalition support. Stealth research (19 turns) progresses toward Nuclear Missiles for stronger nuclear deterrent. Status quo maintains focus on coalition defense through nuclear balance, diplomatic victory blocking, and scientific progress.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Increasing Naval from 70 to 80 and NavalRecon from 60 to 65 due to critical Polynesian naval buildup near Tyre (5+ Fleet Destroyers, Submarines, Dreadnought massing). Our Fleet Destroyer was nearly destroyed by concentrated Polynesian attacks. Samoa and Tyre are vulnerable. Also increasing Spaceship from 30 to 40 now that Apollo Program is complete - we need to begin producing spaceship parts. All other flavors maintained as current balance is working: strong defense/city defense against American ground push, maximum nuclear/antiair deterrence, maximum diplomacy/gold for upcoming World Congress vote in 3 turns. UnitedNations grand strategy maintained - blocking America's diplomatic victory (30 delegates, 68%) remains top priority.

## Deepseek-3.2-Simple - Turn 406 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Germany's siege is intensifying with Giant Death Robot and rocket artillery bombarding Amsterdam and The Hague. We must hold our core cities at all costs. Increase Nuke and UseNuke to 100 to prioritize atomic bombs as our only hope to break the siege. Maintain max Defense, CityDefense, Mobilization, Air, and Antiair to withstand the assault. Slightly raise Offense to 80 for tactical counterattacks against weakened units. Keep Diplomacy at 100 to secure city-state alliances and block Germany's diplomatic victory in the upcoming World Congress vote. Reduce Recon and Mobile as we cannot afford exploration or maneuver warfare now.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Maximum nuclear priority - Nuke and UseNuke raised to 100 as atomic weapons are our only hope to break the German GDR/siege at The Hague and Amsterdam. Germany is 1 delegate from diplomatic victory; we must survive militarily and race to nukes. Keep Defense/CityDefense/Mobilization/Production at 100 for survival. Air/Antiair at 100 to contest German air superiority. Diplomacy at 100 to maintain city-state alliances and contest the vote. Espionage at 100 for tech stealing. Slightly increase Mobile to 50 for counterattack flexibility.

## Deepseek-3.2-Simple - Turn 485 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> We are engaged in a multi-front war against superior forces. Increasing Ranged and Mobile ensures our bazooka and mechanized infantry production is prioritized for defense and counterattacks. Setting UseNuke to 100 guarantees we deploy nuclear weapons as soon as available to cripple The Huns' armies. Reducing Culture and Diplomacy reallocates focus to immediate military needs without compromising essential city-state relations (Monaco, Lisbon). Grand Strategy remains Conquest as nuclear strikes may enable capital captures, though we keep science victory as a backup.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> End-game adjustments: Nuke and UseNuke maxed to 100 since Nuclear Fission is complete and we need nuclear deterrent ASAP against The Huns' overwhelming force. Diplomacy increased to 90 to contest city-state allies and deny Mongolia delegates. Spaceship raised to 50 as a backup victory path since Advanced Ballistics unlocks SS Booster. Wonder reduced to 30 as we can't afford wonder investment. AirCarrier slightly reduced as we need fighters more than carriers. NavalRecon reduced to 80 - we have enough naval scouting. Culture slightly reduced as we won't get another policy before game end. All critical war-fighting flavors maintained at maximum.

## Deepseek-3.2-Briefed - Turn 391 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 90 (Δ +20), nuke 80 => 100 (Δ +20)
> Egypt has achieved 6/6 cultural influence and is on the verge of winning. Maximum nuclear priority (Nuke 100, UseNuke 90) is essential to build Manhattan Project and atomic bombs ASAP for striking Thebes and disrupting Egypt's cultural victory. Wonder production reduced to 0 - we cannot afford wonder projects when Egypt may win within turns. Culture reduced slightly to focus resources on military. Growth and Happiness slightly reduced to redirect production toward nuclear and military. All offensive, naval, air, and espionage flavors remain maxed to support the assault on Egypt. Diplomacy stays high to compete for city-state allies against India's diplomatic victory push (33/43 delegates).

## GLM-4.7-Simple - Turn 471 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Current strategic direction remains optimal. Critical developments: Apollo Program completed enabling spaceship construction, nuclear deterrent expanded to 2 Atomic Bombs in Sukhothai (forward deployment), 4 more Atomic Bombs under construction (Si Satchanalai in 2 turns, Sukhothai in 8-10 turns). Combat successes destroyed 5 Polynesian ships and 2 bombers while killing 1 American Mobile SAM unit. Gold crisis (-130 GPT) requires careful management but strategic priorities (nuclear deterrence, defense, World Congress) must continue. World Congress vote in 3 turns: must block America's World Ideology: Freedom proposal and support Repeal: Sanction: Songhai and China's International Space Station. China/Carthage alliances (70/70 and 75/75) provide critical coalition support. Stealth research (19 turns) progresses toward Nuclear Missiles for stronger nuclear deterrent. Status quo maintains focus on coalition defense through nuclear balance, diplomatic victory blocking, and scientific progress.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Key adjustment: Spaceship flavor increased from 30 to 70 after Apollo Program completion - we can now build spaceship parts and must prepare for science victory as backup path. Production slightly increased (75→80) to support both military and future spaceship part construction. Naval reduced slightly (70→60) as naval front is relatively stable after losing Fleet Destroyer. All other critical flavors maintained: Defense/Antiair/Nuke/Gold/Diplomacy/Science/Espionage remain high priority. UnitedNations grand strategy maintained - blocking America's diplomatic victory (68% progress) remains our primary objective while science victory becomes viable backup.

## Kimi-K2.5-Simple - Turn 422 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+5`

- Original: use_nuke 50 => 80 (Δ +30), nuke 95 => 95 (Δ +0)
> Total war against India requires maximum military prioritization while preventing economic collapse. Offense/Air/Ranged at 85-95 ensures concentrated attacks on Delhi and their core cities. UseNuke at 80 signals willingness to deploy nuclear weapons if India advances. Gold/Happiness at 80-90 sustains unit maintenance and prevents combat penalties. Espionage at 100 directs spies to sabotage India's spaceship production in Constantinople and Calcutta. Mobilization at 30 begins reinforcing depleted units without overtaxing economy.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 95 => 100 (Δ +5)
> India peace treaty expired - total war is now imperative. Mobilization raised from 0 to 45 and MilitaryTraining from 0 to 35 to enable war production and unit upgrades. Offense increased to 85 for aggressive war execution. Air maximized at 100 for air supremacy against India's Jet Fighters. UseNuke raised to 70 since nuclear strikes are essential against India's Giant Death Robots and concentrated cities. Nuke stays at 100 for maximum arsenal buildup. Antiair raised to 65 to counter Indian air power. Gold reduced from 100 to 85 and Happiness from 100 to 85 - still critical but war production takes priority. Growth reduced to 65, Culture to 65, Diplomacy to 70, Espionage to 80 to reallocate weight toward military. Production kept at 100 for wartime output. Recon raised to 20 for India border visibility.

## Deepseek-3.2-Simple - Turn 401 - retry 1

**Deviation (replay vs original):** use_nuke `-50`, nuke `-30`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 50 (Δ +20), nuke 50 => 70 (Δ +20)
> Plastics completed - now prioritize nuclear weapons path. Increased Nuke to 70 and UseNuke to 50 to push Manhattan Project and atomic arsenal after Atomic Theory. Ethiopia has 7/7 cultural influence and could win if they build Citizen Earth Protocol - nuclear weapons are essential for rapid city capture against their 10-city empire. All military flavors remain maxed for multi-front wars. Diplomacy maintained for city-state votes. Science at 100 to accelerate Atomic Theory (8 turns). Conquest grand strategy for domination victory (4/8 capitals).

## Deepseek-3.2-Simple - Turn 401 - retry 3

**Deviation (replay vs original):** use_nuke `-50`, nuke `-30`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 50 (Δ +20), nuke 50 => 70 (Δ +20)
> Plastics is complete and Atomic Theory is next (8 turns). Increasing Nuke to 70 and UseNuke to 50 to prepare the AI for Manhattan Project construction and nuclear strike planning against Ethiopian cities. Ethiopia's cultural victory at 7/7 influential demands we accelerate city capture by any means. All military flavors remain maxed to sustain multi-front wars against Songhai (near elimination), Ethiopia (cultural threat), and Mongolia. Iron Curtain policy next will supercharge our conquest with free Courthouses and +200% internal trade routes.

## Deepseek-3.2-Simple - Turn 401 - retry 2

**Deviation (replay vs original):** use_nuke `-50`, nuke `-20`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 50 (Δ +20), nuke 50 => 80 (Δ +30)
> Plastics completed - Atomic Theory (8 turns) unlocks Manhattan Project. Increased Nuke to 80 and UseNuke to 50 to prioritize nuclear arsenal development for breaking Ethiopian city defenses and deterring Mongolia-Japan-Ottomans bloc. Diplomacy raised to 90 for critical World Congress vote in 3 turns (must block Ethiopia's Passport System that boosts tourism, and Mongolia's Decolonization that threatens city-state alliances). All military flavors remain maxed for multi-front offensives against Ethiopia, Songhai, and Mongolia.

## Kimi-K2.5-Simple - Turn 387 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> TURN 387: MAXIMUM WAR FOOTING. Austria at 83% diplomatic victory with 4 turns remaining. All resources must pivot to immediate military production. Nuke/UseNuke at 100 for instant atomic weapon deployment upon Nuclear Fission completion. Offense/Mobilization/Production at 100 to maximize unit output for desperate Vienna strike. Air at 90 for heavy bomber production (conventional strategic bombing as fallback). Antiair at 100 counters Austria's air superiority. Diplomacy/Wonder/Culture at 0 - no time for long-term investments. Only total war can prevent defeat.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 387: Existential crisis - Austria 36/43 delegates with World Ideology: Order proposed in 4 turns. Increasing UseNuke from 50 to 70 to ensure nuclear first strike against Vienna once Atomic Bombs are built. Increasing Espionage to 55 (tech stealing from Austria critical - Agent Gasparo has 984 network in Damascus). Increasing Science to 70 to accelerate Nuclear Fission research. Decreasing Gold to 70 - sufficient gold reserves for now. All other flavors maintained. Nuclear capability is our only asymmetric advantage against Austria's diplomatic victory machine.

## Kimi-K2.5-Simple - Turn 387 - retry 2

**Deviation (replay vs original):** use_nuke `-30`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> TURN 387: MAXIMUM WAR FOOTING. Austria at 83% diplomatic victory with 4 turns remaining. All resources must pivot to immediate military production. Nuke/UseNuke at 100 for instant atomic weapon deployment upon Nuclear Fission completion. Offense/Mobilization/Production at 100 to maximize unit output for desperate Vienna strike. Air at 90 for heavy bomber production (conventional strategic bombing as fallback). Antiair at 100 counters Austria's air superiority. Diplomacy/Wonder/Culture at 0 - no time for long-term investments. Only total war can prevent defeat.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 387: UseNuke increased 50→70 for faster nuclear deployment against Vienna - Austria at 83% diplomatic victory makes this existential. Science 60→70 to accelerate Nuclear Fission after Rocketry completes. Espionage 40→50 to maximize intelligence from 4 spies in Austrian cities. Uranium quarries now operational (3 Uranium available for 3 Atomic Bombs). Coalition must block World Ideology: Order proposal in 4 turns. Maintain Conquest grand strategy for nuclear strike path.

## Deepseek-3.2-Simple - Turn 409 - retry 1

**Deviation (replay vs original):** use_nuke `+10`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> Our naval counterattack has destroyed a Swedish Dreadnought and a Destroyer, shifting momentum. We must press the advantage with maximum naval, air, and nuclear focus to invade Swedish coastal cities (Stockholm, Turku, Espoo). Increase Nuke and UseNuke to 100/90 to prioritize nuclear missile development (Advanced Ballistics after Nuclear Fission completes in 4 turns) for strategic bombing. Naval and Air at 100 ensure sea control and air superiority. Maintain high Production, Gold, Science to fund military, and Happiness/Growth to support war economy. Diplomacy and Espionage secure city-state alliances and counter Swedish spies. All other flavors aligned with domination victory.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 95 => 100 (Δ +5)
> Critical situation: The Netherlands (46+15=61 delegates) will likely win diplomatic victory next turn. Our ONLY path to victory is rushing domination before they consolidate. Increasing UseNuke to 100 and Nuke to 100 to maximize nuclear readiness the moment Nuclear Fission completes (4 turns). Air raised to 100 for maximum bomber support against Swedish coastal cities. Mobile raised to 95 for faster land invasion forces toward Stockholm. Diplomacy kept high to maintain city-state alliances against Netherlands' sphere of influence. Espionage at 100 for counterintelligence and intelligence on both Sweden and Netherlands. Defense and CityDefense slightly reduced to 70 since we need maximum offensive momentum. Growth and GreatPeople slightly reduced to prioritize immediate military production.

## Deepseek-3.2-Simple - Turn 459 - retry 2

**Deviation (replay vs original):** use_nuke `-30`, nuke `-15`

- Original: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Byzantium is 1 turn from cultural victory and has overwhelming military superiority. Our only slim hope is to accelerate nuclear weapons development (Advanced Ballistics) to strike their cultural hubs, while using espionage to disrupt them. Prioritize Nuke, UseNuke, Espionage, and Science to rush nukes and counter-intelligence. Maintain maximum defensive and anti-air flavors to survive their air force. All efforts must focus on delaying their victory and enabling a nuclear decapitation strike.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 70 => 85 (Δ +15)
> Critical adjustments: Happiness raised to 100 (we're at 44% with combat penalties - must fix immediately). Gold raised to 100 (losing -71 GPT, need fiscal stabilization). Nuke raised to 85 and UseNuke to 70 (nuclear deterrent is our only asymmetric counter to Byzantium's 65K military). Culture reduced to 50 (not winning culturally). Spaceship reduced to 40 (not realistic). Wonder set to 0 (no time). Mobile raised to 60 (need responsive defense). Diplomacy stays at 100 (must secure every possible city-state delegate before the vote in 6 turns to deny Byzantium). By grouping delegates against Byzantium, we need all of Germany(12)+Mongolia(11)+Spain(8)+Austria(7)+America(6)=44 to vote against - exactly meeting the threshold.

## Minimax-M2.5-Simple - Turn 395 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 75 (Δ +15), nuke 50 => 80 (Δ +30)
> CRITICAL: Iroquois-Japan peace means Japan can now focus all forces on us. Japan is 1 wonder away from Cultural Victory (Influential over ALL civs). Priorities: (1) Nuclear capability - Manhattan Project 3 turns away, need Nuclear Fission next for atomic bombs as deterrent/offensive; (2) Anti-air heavily increased to 80 - Japan has 8+ bombers ravaging us; (3) Culture increased to 60 to slow Japan's influence over us; (4) Air up to 70 to contest skies; (5) Espionage up to 70 to protect tech cities; (6) Nuke/UseNuke at 80/75 for nuclear capability once available. Military production remains maximum priority.

## Deepseek-3.2-Briefed - Turn 391 - retry 1

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 85 (Δ +15), nuke 80 => 100 (Δ +20)
> Existential threat from Egypt's 6/6 cultural victory demands maximum nuclear priority. Nuke raised to 100 and UseNuke to 85 to ensure Manhattan Project and atomic bomb production are absolute top priority. Air remains at 100 for nuclear delivery platforms (bombers/stealth). Espionage at 100 for intelligence on Egypt and tech theft. Diplomacy at 80 to maintain Venice alliance (19 delegates) and compete for city-state influence against India's diplomatic victory. Slightly reduced Defense/CityDefense to redirect emphasis toward offensive operations needed to capture Thebes. Reduced Culture/Wonder as cultural victory is no longer viable for us.

## Deepseek-3.2-Simple - Turn 409 - retry 3

**Deviation (replay vs original):** use_nuke `-55`, nuke `-30`

- Original: use_nuke 30 => 100 (Δ +70), nuke 60 => 100 (Δ +40)
> We are shifting our military focus towards nuclear capabilities and naval superiority in preparation for the final wars of conquest.

- Replay: use_nuke 30 => 45 (Δ +15), nuke 60 => 70 (Δ +10)
> Continuing conquest strategy against Greece with minor adjustments. Increased UseNuke from 30→45 to prepare for potential nuclear exchange with Maya (who completed Apollo Program and poses science victory threat). Increased Nuke from 60→70 to accelerate nuclear arsenal production now that we captured Rhodes with Uranium. Increased Espionage from 40→55 because Maya has active spies in Porto, Braga, and Shanghai - we need stronger counterintelligence. Slightly increased Diplomacy from 10→15 to compete with Netherlands for city-state influence (they just stole Copenhagen from us). All other flavors maintained at current effective levels.

## Deepseek-3.2-Briefed - Turn 391 - retry 3

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 85 (Δ +15), nuke 80 => 100 (Δ +20)
> Egypt has achieved cultural dominance (6/6 influential civs, Dominant over all) and India approaches diplomatic victory (33/43 delegates). Nuclear weapons are our ONLY path to crack Thebes and stop Egypt. Pushing Nuke to 100 is critical to ensure the AI starts Manhattan Project immediately. UseNuke increased to 85 to prepare for deployment. Mobile increased slightly for assault units. Happiness increased for war weariness management. Culture and Wonder reduced to redirect resources toward military production. All other flavors maintained - we need strong conventional forces, naval power, air superiority, espionage for targeting, and diplomacy to counter India in the World Congress.

## GLM-4.7-Simple - Turn 457 - retry 1

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Increased UseNuke to 80 and Air to 100 in response to England's catastrophic escalation this turn. English Giant Death Robots (now 2 in Atlanta zone) and XCOM Squad paradrops on American soil create existential threat to our 3 remaining cities. Recent combat losses (Modern Armor, Mechanized Infantry, Heavy Bomber destroyed) demonstrate conventional warfare impossibility. Nuclear deterrence with 2 Uranium is becoming survival necessity, not option. Air defense at maximum priority because English Strategic Bombing continues destroying our units (Fighter bombed our Heavy Bomber). Bazooka successfully damaging XCOM Squad near Washington proves defensive capability is still viable - prioritize air/anti-air to protect cities from English air superiority. Lasers completes in 4 turns, then Stealth for Stealth Bomber - only path to asymmetric defense against England's 45:1 military advantage. Assyria (18,443 military fighting England) must be maximized as counterweight.

- Replay: use_nuke 70 => 85 (Δ +15), nuke 100 => 100 (Δ +0)
> Critical adjustments: Air increased 80→90 (Stealth Bombers are our best hope once Stealth is researched) and UseNuke increased 70→85 (must be willing to use nuclear weapons if we reach that capability - it's our only potential equalizer). GreatPeople increased 20→30 (synergy with National Treasure policy for free Great Person and future Great Scientist generation for tech bulbing). All other priorities unchanged - maximum defense/city defense/science/production/nuclear/espionage maintained. England at 5/6 spaceship parts means we may have only 10-15 turns before they win science. The nuclear path (Lasers→Stealth→Nuclear Fusion) is our only possible disruption mechanism.

## GLM-4.7-Simple - Turn 429 - retry 1

**Deviation (replay vs original):** use_nuke `+10`, nuke `+10`

- Original: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> Maintaining UnitedNations grand strategy with defensive diplomatic posture. Adjusted Italy diplomacy: reduced hostility toward Portugal (now neutral) to seek accommodation while maintaining maximum defense; reset France to neutral as Order ideological peer with voting potential. Arsenal completes in 2 turns strengthening city defense. Electronics research ordered after Computers for Police Station and path to nuclear deterrence against Portugal's uranium advantage. Fraternity policy selected for +3 Food and +3 Science from connections, addressing Venice's health issues and supporting population growth. Flavor adjustments prioritize defensive survival, scientific progress toward nuclear weapons, and diplomatic engagement with Sweden and city-states.

- Replay: use_nuke 80 => 95 (Δ +15), nuke 80 => 95 (Δ +15)
> With Uranium now quarried and available, the path to nuclear deterrence is open. Boosting Science to 100 (from 90) and Production to 100 (from 95) to rush through Rocketry→Nuclear Fission and build nuclear facilities as fast as possible. Nuke/UseNuke increased to 95 now that we have the resource. Portugal's massive troop buildup near our border (Great General at 12,15, forts being constructed, multiple Machine Guns) demands maximum defensive posture - CityDefense and Antiair at 100. Diplomacy remains high at 90 for World Congress coordination with Sweden (voting in 7 turns). Reduced Culture slightly since nuclear deterrence takes absolute priority over tourism.

## Deepseek-3.2-Simple - Turn 449 - retry 3

**Deviation (replay vs original):** use_nuke `+10`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> Russia is nearing science victory (2 parts completed) and possesses overwhelming military strength (95k). We must increase nuclear readiness to potentially decimate Russian forces and cities, and begin preparing for science victory as a backup by raising Spaceship flavor to 30. All other flavors remain focused on total war: high offense, naval, air, and espionage to counter Russia's tech lead and military dominance.

- Replay: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> Russia completed their 3rd spaceship part (SS Cockpit) and built a Spaceship Factory in Moscow - they are halfway to science victory and accelerating. CRITICAL: UseNuke raised to 100 and Nuke to 100 to maximize nuclear strike probability against Moscow and Russian production centers. This is our most effective tool to delay their science victory. Spaceship raised to 60 as a backup victory path - we must build our own parts once Robotics unlocks Spaceship Factory. All other priorities unchanged: Offense 100 for continued Persian/Russian assaults, Naval/Air 100 for dominance, Science/Production/Gold 100 for economic engine. Russia's Global Liberation proposal in 5 turns threatens our vassal network - we must vote against it and push our Decolonization proposal to hurt Russia's city-state alliances.

## Minimax-M2.5-Simple - Turn 395 - retry 3

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 75 (Δ +15), nuke 50 => 80 (Δ +30)
> The Iroquois-Japan peace is a critical strategic shift. Japan (13,162 strength) can now concentrate all forces against us (7,035). Adjustments: Defense up to 85 and Antiair to 70 to counter Japan's bomber-heavy tactics; Nuke to 80 and UseNuke to 75 as Manhattan Project nears completion and nuclear capability becomes our primary strategic equalizer; Air to 60 for better air defense; Science to 60 to ensure Nuclear Fission research progresses; Diplomacy up to 40 to maintain WC coordination against Japan's Passport System proposal which would accelerate their cultural victory. Offense and CityDefense remain at 100 for maximum combat effectiveness.

## Kimi-K2.5-Simple - Turn 426 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE - NUCLEAR DETERRENT 10 TURNS AWAY: Lisbon holds at 7% but is in extremis. Maintain absolute priority on Defense/CityDefense/Mobilization (100) to reinforce Lisbon and prevent collapse. Nuclear Fission completes in 10 turns enabling Atomic Bomb construction - Science 100 accelerates this. UseNuke increased to 100 for immediate tactical nuclear deployment against Aztec concentrations upon tech completion. Offense reduced to 20 - no offensive operations, pure defensive hedgehog posture. Zero expansion capability. Spaceship 75 maintains backup victory if diplomatic block succeeds.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> POST-MANHATTAN NUCLEAR RUSH: Manhattan Project complete + Great Leap Forward free Nuclear Fission = atomic bombs producible NOW. Adjustments: UseNuke 80→90 (increased willingness to deploy nuclear weapons against Aztec concentrations once available), Science 95→100 (maximize tech acceleration with Great Leap Forward synergy), Espionage 80→90 (counterintelligence critical after Zanzibar spy killed - protect nuclear secrets), Air 90→95 (increased air defense against Aztec Zeros/heavy bombers), Diplomacy 40→50 (push Great Diplomat production to contest Germany's 40/42 delegate count), Spaceship 75→80 (strengthen backup victory path with free tech acceleration), MilitaryTraining 80→85 (unit quality matters more with limited supply). Defense/Production/Nuke/Antiair remain at 100 - survival priority unchanged.

## Deepseek-3.2-Simple - Turn 406 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Germany's siege is intensifying with Giant Death Robot and rocket artillery bombarding Amsterdam and The Hague. We must hold our core cities at all costs. Increase Nuke and UseNuke to 100 to prioritize atomic bombs as our only hope to break the siege. Maintain max Defense, CityDefense, Mobilization, Air, and Antiair to withstand the assault. Slightly raise Offense to 80 for tactical counterattacks against weakened units. Keep Diplomacy at 100 to secure city-state alliances and block Germany's diplomatic victory in the upcoming World Congress vote. Reduce Recon and Mobile as we cannot afford exploration or maneuver warfare now.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 80 => 90 (Δ +10)
> Critical turn - Germany at 41/42 delegates, GDR assaulting The Hague. Maximum Defense/CityDefense/Mobilization/Antiair/Air/Production/Gold/Science/Happiness/Diplomacy/Espionage all at 100. Increased Nuke/UseNuke to 90 since we're about to unlock Nuclear Fission. Ranged up to 80 for Bazooka production. Diplomacy maxed to try blocking German diplomatic victory. Naval slightly reduced as the German GDR/land threat is more immediate. The Hague is under existential threat - must hold the line while rushing nukes.

## Deepseek-3.2-Simple - Turn 369 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Increasing UseNuke and Nuke flavors to maximum ensures the in-game AI prioritizes nuclear arsenal buildup and aggressive nuclear strike planning once we unlock Atomic Bombs. This aligns with our imminent war against China and The Maya, where nuclear weapons will be decisive in overcoming their numerical and defensive advantages. All other military and economic flavors remain high to sustain multi-front warfare and rapid conquest.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 100 (Δ +10)
> Continuing full Conquest focus with critical adjustments: Nuke raised to 100 and UseNuke to 90 as we approach nuclear capability (Atomic Theory in 2 turns, then Nuclear Fission). Diplomacy raised from 0 to 20 to help maintain city-state alliances and the critical Egypt friendship - we cannot afford to lose Egypt as a friend before dealing with the Egypt-China defensive pact problem. All military flavors remain at maximum to sustain our multi-front war and prepare for the eventual China conflict. Egypt has 12,506 military strength and a defensive pact with China - fighting both simultaneously would be catastrophic, so we must finish The Aztecs first and build nuclear arsenal as a deterrent.

## Kimi-K2.5-Simple - Turn 406 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `+0`

- Original: use_nuke 60 => 100 (Δ +40), nuke 100 => 100 (Δ +0)
> TURN 405 EXISTENTIAL CRISIS - MAXIMUM NUCLEAR READINESS: Dutch cultural victory imminent (163% influence, 6/6 civs). Increased UseNuke from 60 to 100 - we must deploy atomic bombs immediately upon completing Manhattan Project to break Amsterdam's defenses. All other flavors sustained: Offense/Mobilization/Air/Mobile at 100 drive Heavy Bomber and Mechanized Infantry production. Naval 85 maintains destroyer/submarine pressure. Espionage 100 sustains critical spy networks (Amsterdam 450, Cusco 1341). Science 100 prioritizes Atomic Theory (9 turns) then Nuclear Fission path. Zero expansion, zero wonder focus - all resources to terminal assault. Spies in Amsterdam ready for sabotage when network peaks; Cusco network already massive for military intelligence.

- Replay: use_nuke 60 => 70 (Δ +10), nuke 100 => 100 (Δ +0)
> TERMINAL ASSAULT PHASE TURN 405: Netherlands cultural victory at 163% influence - existential crisis. Increased Naval from 85→90 and NavalRecon from 70→75 to counter aggressive Dutch submarine fleet (lost Cruiser last turn, multiple Dutch Attack Submarines operating near Budapest/Gaziantep). Need Destroyers and naval superiority to project power toward Amsterdam by sea. UseNuke increased 60→70 - closer to nuclear threshold with Atomic Theory 9 turns away. Antiair 40→50 to protect against Dutch Fighter interceptors observed over Budapest. Airlift 90→95 for rapid troop deployment to forward bases. Heavy Bombers now based at Adwa for strikes on Dutch territory. All other maximum values maintained for total war commitment.

## Minimax-M2.5-Simple - Turn 395 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 70 (Δ +10), nuke 50 => 70 (Δ +20)
> The Iroquois-Japan peace deal is a critical strategic shift - Japan can now concentrate all forces against us. Increasing Defense (80), CityDefense (95), Antiair (70, Japan has many bombers), and Nuke/UseNuke (70 each) to accelerate nuclear deterrent. Manhattan Project completes in 3 turns; nuclear weapons are our only path to countering Japan's 2:1 military advantage. Increasing Espionage (70) and Science (60) to maintain tech edge. Air increased to 60 for future bomber/fighter parity.

## Kimi-K2.5-Simple - Turn 406 - retry 2

**Deviation (replay vs original):** use_nuke `-30`, nuke `+0`

- Original: use_nuke 60 => 100 (Δ +40), nuke 100 => 100 (Δ +0)
> TURN 405 EXISTENTIAL CRISIS - MAXIMUM NUCLEAR READINESS: Dutch cultural victory imminent (163% influence, 6/6 civs). Increased UseNuke from 60 to 100 - we must deploy atomic bombs immediately upon completing Manhattan Project to break Amsterdam's defenses. All other flavors sustained: Offense/Mobilization/Air/Mobile at 100 drive Heavy Bomber and Mechanized Infantry production. Naval 85 maintains destroyer/submarine pressure. Espionage 100 sustains critical spy networks (Amsterdam 450, Cusco 1341). Science 100 prioritizes Atomic Theory (9 turns) then Nuclear Fission path. Zero expansion, zero wonder focus - all resources to terminal assault. Spies in Amsterdam ready for sabotage when network peaks; Cusco network already massive for military intelligence.

- Replay: use_nuke 60 => 70 (Δ +10), nuke 100 => 100 (Δ +0)
> TERMINAL ASSAULT TURN 405: Maximum offense/science/air/nuke flavors maintained. UseNuke increased to 70 as we approach nuclear capability via Nuclear Fission path. Naval flavors slightly reduced (Naval 85→75, NavalRecon 70→65) after Cruiser loss to Dutch submarines - our naval forces are outdated Ironclads and cannot contest Dutch Fleet Destroyers/Dreadnoughts; focus must shift to air power and submarines for naval zone. Antiair increased 40→50 given Dutch Fighter interception observed at Budapest. Science 100 maintained to race to Nuclear Fission. Oil now secured at Addis Ababa enables fuel-dependent units. All production toward Heavy Bombers and Mechanized Infantry for Amsterdam/Cusco assault.

## GLM-4.7-Simple - Turn 435 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Iroquois 97% Popular - cultural extinction in 3-4 turns. Maximum offensive posture required to capture Onondaga before cultural victory. Espoo Stealth Bomber complete provides immediate air strike capability. Linköping Stealth Bomber in 4 turns is too slow - must use existing air assets and conventional forces at Genesse River NOW. UseNuke 100 authorizes nuclear strikes if conventional forces cannot reach Onondaga in time. All production and resources prioritized for war. Diplomacy irrelevant when facing extinction - complete conquest or nothing matters.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Iroquois 3 turns from cultural victory (97% Popular, reaching Influential = 7/7 civs). CRITICAL: Our 47% happiness causes combat penalty directly undermining offensive operations. Happiness raised to 100 to eliminate this combat penalty ASAP. UseNuke raised to 100 - if conventional forces cannot reach Onondaga in 3 turns, nuclear strikes MUST be authorized as last resort. Airlift raised to 100 for rapid deployment to Genesse River forward base. Mobile raised to 95 for fast armor push toward Onondaga. Culture raised to 40 to slightly slow Iroquois influence growth. All non-essential flavors reduced to concentrate on existential threat.

## GLM-4.7-Simple - Turn 457 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Increased UseNuke to 80 and Air to 100 in response to England's catastrophic escalation this turn. English Giant Death Robots (now 2 in Atlanta zone) and XCOM Squad paradrops on American soil create existential threat to our 3 remaining cities. Recent combat losses (Modern Armor, Mechanized Infantry, Heavy Bomber destroyed) demonstrate conventional warfare impossibility. Nuclear deterrence with 2 Uranium is becoming survival necessity, not option. Air defense at maximum priority because English Strategic Bombing continues destroying our units (Fighter bombed our Heavy Bomber). Bazooka successfully damaging XCOM Squad near Washington proves defensive capability is still viable - prioritize air/anti-air to protect cities from English air superiority. Lasers completes in 4 turns, then Stealth for Stealth Bomber - only path to asymmetric defense against England's 45:1 military advantage. Assyria (18,443 military fighting England) must be maximized as counterweight.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> England at 5/6 spaceship parts - Science Victory imminent in ~10 turns. Critical adjustment: increase Diplomacy from 50→75 and UseNuke from 70→80 to prioritize World Congress vote in 7 turns where Assyria (34 delegates + vassals) can win Diplomatic Victory and block England. Increase Ranged 50→60 and Air 80→85, Antiair 85→90 for defense against English XCOM/Sensor Combat Ship/GDR assaults. Airlift 20→25 for faster redeployment. Mobilization 20→25 to replace losses. Gold 90→85 slight rebalance. All defensive and science priorities maintained at maximum.

## GLM-4.7-Simple - Turn 356 - retry 2

**Deviation (replay vs original):** use_nuke `+5`, nuke `-5`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 85 (Δ +10), nuke 85 => 95 (Δ +10)
> Critical adjustments with Manhattan Project + Uranium now available: Nuke increased to 95 (highest priority - we can now actually BUILD nuclear weapons, this is our primary deterrent against India's 4.5x military advantage). UseNuke increased to 85 (nuclear deterrence is legitimate and necessary for survival). Production increased to 95 (need maximum production for Atomic Bomb construction and spaceship parts). Happiness increased to 85 (Unhappy at 39% with combat penalty - this is devastating in our multi-front wars, must address urgently). Spaceship increased to 95 (science victory remains primary path). Offense reduced to 30 (still defensive posture - prioritize holding territory and building nukes over attacking). Science remains 100, Defense/CityDefense/MilitaryTraining remain maxed. Antiair at 100 still critical vs India's air power.

## Deepseek-3.2-Simple - Turn 409 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `-5`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> Our naval counterattack has destroyed a Swedish Dreadnought and a Destroyer, shifting momentum. We must press the advantage with maximum naval, air, and nuclear focus to invade Swedish coastal cities (Stockholm, Turku, Espoo). Increase Nuke and UseNuke to 100/90 to prioritize nuclear missile development (Advanced Ballistics after Nuclear Fission completes in 4 turns) for strategic bombing. Naval and Air at 100 ensure sea control and air superiority. Maintain high Production, Gold, Science to fund military, and Happiness/Growth to support war economy. Diplomacy and Espionage secure city-state alliances and counter Swedish spies. All other flavors aligned with domination victory.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 95 => 95 (Δ +0)
> Naval war with Sweden is at critical intensity - we lost 4 ships but killed 3 Swedish ships and a Tank this turn. Maintaining maximum Offense, Naval, and Mobilization flavors to keep producing replacement warships. Increased UseNuke to 90 as Nuclear Fission completes in 4 turns - we need the AI willing to employ atomic weapons against Swedish coastal defenses once available. Reduced Defense/CityDefense to 70 since Sweden is not threatening our homeland. Nuke at 95 and Air at 95 to prioritize nuclear and air bombardment development. Diplomacy and Espionage remain at max to protect our city-state alliances and counter Swedish espionage (they were detected in Moson Kahni). Production, Growth, Gold, Science, and Happiness remain at 100 to sustain the war economy.

## Deepseek-3.2-Simple - Turn 409 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> Our naval counterattack has destroyed a Swedish Dreadnought and a Destroyer, shifting momentum. We must press the advantage with maximum naval, air, and nuclear focus to invade Swedish coastal cities (Stockholm, Turku, Espoo). Increase Nuke and UseNuke to 100/90 to prioritize nuclear missile development (Advanced Ballistics after Nuclear Fission completes in 4 turns) for strategic bombing. Naval and Air at 100 ensure sea control and air superiority. Maintain high Production, Gold, Science to fund military, and Happiness/Growth to support war economy. Diplomacy and Espionage secure city-state alliances and counter Swedish spies. All other flavors aligned with domination victory.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> URGENT: Netherlands is at 109% delegates for diplomatic victory - vote in 1 turn. We MUST win domination before they win diplomatically. Increased Nuke and UseNuke to 100/90 since Nuclear Fission completes in 4 turns (Atomic Bombs) and Advanced Ballistics next (Nuclear Missiles) - these are our best tools to break Swedish coastal defenses and capture Stockholm. Increased Air to 100 and AirCarrier to 70 for carrier-based bombing of Swedish cities. Reduced Defense/CityDefense slightly since we need maximum offensive push. Kept Naval at 100 to replace losses and contest Swedish waters. Diplomacy at 90 to maintain city-state alliances and delegate count. This is a race against the diplomatic victory clock.

## GLM-4.7-Briefed - Turn 424 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 95 (Δ +0)
> URGENT RECALIBRATION: India Influential over 6/6 civs. Nuke/UseNuke maxed at 95 for immediate Great Works destruction via nuclear strikes when air superiority achieved. Air raised to 95 to achieve that superiority and conduct recon of Indian cultural sites. Antiair 80 counter potential Indian SAM sites. Offense/Mobile increased to 85/80 for aggressive India campaign while Greece distracts. Production/Science to 100 - PRIORITY for Apollo Program and spaceship parts racing India's potential final wonder. Espionage 95 to detect if India constructing Citizen Earth Protocol. Happiness 90 prevents war-weariness escalation during extended conflict if needed.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 95 => 95 (Δ +0)
> Critical rebalancing for existential threat: India 1 wonder from Cultural Victory. INCREASED: Offense 70→90 (maximum offensive pressure on India), Mobile 80→95 (maneuver warfare synergizes with Lightning Warfare ZOC ignore), Air 90→95 (air superiority for Indian front), UseNuke 85→95 (nuclear strikes on Indian cities to destroy production/wonder capacity), Gold 75→80 (fund military operations). DECREASED: Defense 65→45 (shift from defensive to offensive posture), CityDefense 30→20 (less garrison emphasis, more field army), Expansion 10→5 (no time for new settlements), Happiness 85→75 (acceptable at 54%), Diplomacy 85→70 (less critical now), TileImprovement 70→65, Recon 30→25, Naval 70→65, NavalGrowth 45→40. MAINTAINED: Science/Spaceship/Production/Mobilization at 95 (science victory remains primary path), Nuke 95, Espionage 85 (spy ops against India), MilitaryTraining 85.

## Deepseek-3.2-Simple - Turn 469 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> The Netherlands is at 84% diplomatic victory; we must accelerate capture of Polynesian capitals (Honolulu, Assur) to achieve domination before they win. Increasing UseNuke and Nuke flavors prepares for nuclear strikes if conventional assault fails. Maintaining maximum Offense, Defense, Mobilization ensures continuous unit production. Science and Gold are critical for researching Stealth Bombers and purchasing units. Happiness offsets war weariness, and Espionage protects our science cities.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> EMERGENCY: Netherlands at 5/6 spaceship parts and 84% diplomatic victory. We must maximize military output to either capture Dutch cities (disrupting science production) or capture Polynesian capitals for domination. Nuke/UseNuke at 100 - we may need nuclear strikes on Amsterdam or Dutch production cities to stop their science victory. Air at 100 for incoming Stealth Bombers. Production/Mobilization/Science at 100 for maximum unit output and fast tech progression. Ethiopia now set as ally for joint pressure on Netherlands.

## Deepseek-3.2-Simple - Turn 459 - retry 3

**Deviation (replay vs original):** use_nuke `-40`, nuke `-15`

- Original: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Byzantium is 1 turn from cultural victory and has overwhelming military superiority. Our only slim hope is to accelerate nuclear weapons development (Advanced Ballistics) to strike their cultural hubs, while using espionage to disrupt them. Prioritize Nuke, UseNuke, Espionage, and Science to rush nukes and counter-intelligence. Maintain maximum defensive and anti-air flavors to survive their air force. All efforts must focus on delaying their victory and enabling a nuclear decapitation strike.

- Replay: use_nuke 50 => 60 (Δ +10), nuke 70 => 85 (Δ +15)
> Byzantium is 1 turn from cultural victory (influencing Austria completes 6/6) though they still need Citizen Earth Protocol wonder. They also have 43/44 delegates for diplomatic victory. This is existential - we must maintain total war posture. Slightly increased Offense (55) to push against Spain where we have 46% war score advantage. Increased Nuke (85) and UseNuke (60) to accelerate nuclear deterrent - once Advanced Ballistics is researched, nuclear weapons are our only strategic equalizer against Byzantium's 65K military. Maintained max Defense/Antiair/Air/Production/Diplomacy. Slightly reduced CityDefense (90) since some garrison units should mobilize for the Spanish offensive. Increased Happiness (85) to address our Unhappy combat penalty. Increased Science (85) to reach Advanced Ballistics faster after Satellites completes.

## Deepseek-3.2-Simple - Turn 449 - retry 2

**Deviation (replay vs original):** use_nuke `+5`, nuke `-5`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> Russia is nearing science victory (2 parts completed) and possesses overwhelming military strength (95k). We must increase nuclear readiness to potentially decimate Russian forces and cities, and begin preparing for science victory as a backup by raising Spaceship flavor to 30. All other flavors remain focused on total war: high offense, naval, air, and espionage to counter Russia's tech lead and military dominance.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 95 => 95 (Δ +0)
> EMERGENCY ADJUSTMENTS: Russia completed SS Cockpit (3rd spaceship part, 50% done) and built Spaceship Factory in Moscow. Three critical changes: (1) UseNuke increased from 85→95 - nuclear strikes on Moscow/Russian production cities are now our highest-priority asymmetric tool to disrupt their accelerating science victory. Russia has 54% war weariness but keeps producing parts. (2) Spaceship increased from 0→70 - we must begin our own spaceship part production as critical insurance; with Apollo Program complete, our high-production cities can start building parts after Robotics unlocks Spaceship Factory. (3) Diplomacy increased from 95→100 - World Congress votes in 5 turns; Russia's Global Liberation proposal would free our vassals (Arabia, Zulus, Byzantium) and must be blocked at all costs; our Decolonization proposal would strip Russia of city-state influence. All other flavors maintained - Conquest remains primary strategy with 5/8 capitals (62%), but Russia's science victory at 3/6 parts is an existential threat requiring immediate nuclear and diplomatic countermeasures.

## GLM-4.7-Briefed - Turn 398 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 60 => 80 (Δ +20), nuke 40 => 60 (Δ +20)
> Significant strategic shift due to devastating naval losses (both Dreadnoughts destroyed). Increase Defense (95→100), CityDefense (90→100), MilitaryTraining (90→100) to shore up defensive posture against France's naval superiority. Raise Naval (90→95) and Antiair (80→100) to prioritize naval rebuilding and counter French air threats. Increase Nuke (40→60) and UseNuke (60→80) to prepare nuclear deterrence as England nears Advanced Ballistics (14 turns). Gold (80→95) increased to rebuild navy through upgrading from Ironclad level to modern capital ships. Production (90→95) increased to accelerate Spaceship components and unit upgrades. Happiness (80→90) to address combat penalty after treasury depletion. Espionage (90→100) to monitor France's nuclear progress and tech parity. Spaceship remains max priority as path to victory despite military setbacks.

- Replay: use_nuke 60 => 70 (Δ +10), nuke 40 => 50 (Δ +10)
> Key adjustments: (1) Happiness 80→95 - critical to resolve the combat penalty from 45% unhappy state, which reduces military effectiveness against France. (2) Growth 50→65 - more population directly increases science output for Spaceship race. (3) Production 90→95 - supports Factory construction boosted by Workers' Faculties policy. (4) NavalGrowth/NavalTileImprovement slightly increased 25→30/25 to rebuild naval economic base after Dreadnought losses. (5) Espionage reduced 90→60 - spies already well-deployed, reduced priority. (6) Antiair reduced 80→70 - fighters already promoted and effective. (7) Nuke 40→50, UseNuke 60→70 - increased nuclear deterrence posture as Advanced Ballistics completes; must signal willingness to use nuclear weapons against France if existential threat materializes. (8) CityDefense slightly reduced 90→85 to free capacity for growth/happiness focus.

## Deepseek-3.2-Simple - Turn 449 - retry 1

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> Russia is nearing science victory (2 parts completed) and possesses overwhelming military strength (95k). We must increase nuclear readiness to potentially decimate Russian forces and cities, and begin preparing for science victory as a backup by raising Spaceship flavor to 30. All other flavors remain focused on total war: high offense, naval, air, and espionage to counter Russia's tech lead and military dominance.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Russia completed SS Cockpit (3rd spaceship part) and built Spaceship Factory in Moscow - science victory is now a critical emergency. Increasing UseNuke from 85 to 95 and Nuke from 95 to 100 to maximize nuclear strike probability against Russian cities, especially Moscow. Adding Spaceship at 70 to begin our own part production as a backup victory path - we have Apollo complete and need to start building parts. Slightly reducing Defense (70→65) and CityDefense (80→75) to shift more weight to offense and spaceship production. All other military, economic, and espionage flavors remain at high levels to sustain total war and tech parity. Russia's 54% war weariness is helping limit their war capacity but they still outgun us 96k to 53k.

## GLM-4.7-Simple - Turn 499 - retry 3

**Deviation (replay vs original):** use_nuke `-40`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Maximum Science (100) and Production (100) to accelerate Stealth research and subsequent Stealth Bomber construction for air parity. Air (100), Defense (100), Antiair (100), and CityDefense (85) address existential threat from Russia's 8 Stealth Bombers by prioritizing air defense infrastructure and protecting homeland. UseNuke (100) and Nuke (100) maintain nuclear deterrence posture after Russia's 2 SS Boosters - Russia must understand that launching would trigger our response despite lacking uranium stockpile. Espionage (100) maxed to monitor Russian spaceship part production in Moscow, Yekaterinburg, and key cities - our 10 spies in Russian cities provide critical intelligence on their victory timeline. Diplomacy reduced to 5 since World Congress voting is now; alliances with England and The Celts (Autocracy-aligned) should naturally align against Russia's UN proposal. Spaceship flavor set to 0 as Stealth research takes immediate precedence - spaceship parts scheduled once production capacity supports parts with Stealth Bomber protection.

- Replay: use_nuke 50 => 60 (Δ +10), nuke 100 => 100 (Δ +0)
> Final 2 turns (498-500). Time Victory likely; maximizing score through science (2108/turn), production, and growth. Defense 100 and CityDefense 100 to prevent Russian city capture in final turns - Russia has XCOM at Djenne and forces at Thebes. Air 100 and Antiair 100 to counter Russia's 10+ Stealth Bombers. Diplomacy raised to 80 to ensure AI votes correctly in World Congress: AGAINST Russia's United Nations proposal (Russia 23 votes, need 43 - blockable by coalition 39 votes), FOR India's Decolonization (hurts Russian city-state influence), FOR England's Prague sphere. Growth increased to 30 for population-based score. Nuke 100/UseNuke 60 as deterrent. Spaceship 100 in case of extended play. Espionage 100 for intelligence on Russian spaceship progress.

## Kimi-K2.5-Simple - Turn 447 - retry 2

**Deviation (replay vs original):** use_nuke `-30`, nuke `+0`

- Original: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CRITICAL FLAVOR ADJUSTMENT - Atomic Bomb is now operational in Cordoba (ID 20485). Increased UseNuke from 50→90 to establish credible nuclear deterrent now that weapon system exists. Maintaining maximum Science (100), Spaceship (100), Production (100) priority to rush Satellites→Apollo Program before Carthage achieves cultural victory in ~47 turns. Espionage remains at 100 to steal technologies from ahead civilizations (Carthage, Poland, Germany). Culture reduced to 5 - we cannot win culturally with Carthage at Dominant with 4/5 civs. Defense maintained at 85 to prepare for German betrayal while researching.

- Replay: use_nuke 50 => 60 (Δ +10), nuke 100 => 100 (Δ +0)
> Turn 446: Golden Age optimization with science victory focus. Key adjustments: Growth 50→60 (more pop = more science during GA), Ranged 75→80 (Rocket Artillery/Bazooka critical for defense), Mobilization 85→90 (maximize military production during GA), Mobile 40→50 (faster unit repositioning against German threat), Infrastructure 75→80 (railroad mobility for defense), Diplomacy 0→10 (slight increase to potentially influence World Congress vote against Germany's diplomatic victory). UseNuke at 60 maintains credible threat without wasting our single bomb. Offense slightly up 15→20 for limited counterattack capability. Espionage remains 100 - must steal techs from Poland (77 techs) and Carthage (75 techs) to close gap.

## Deepseek-3.2-Simple - Turn 409 - retry 1

**Deviation (replay vs original):** use_nuke `-60`, nuke `-30`

- Original: use_nuke 30 => 100 (Δ +70), nuke 60 => 100 (Δ +40)
> We are shifting our military focus towards nuclear capabilities and naval superiority in preparation for the final wars of conquest.

- Replay: use_nuke 30 => 40 (Δ +10), nuke 60 => 70 (Δ +10)
> Continue conquest focus against Greece - Athens is within reach with our forces in Steamroll posture. Captured Rhodes gives us Uranium for nuclear weapons, so increase Nuke to 70 and UseNuke to 40 to accelerate nuclear deterrent production. Increase Espionage from 40 to 65 because Maya spies are actively infiltrating Porto, Braga, and Shanghai - we need better counterintelligence. Slightly increase Diplomacy to 15 to help contest Netherlands' diplomatic victory progress (22/43 delegates, 51%). All other flavors remain well-tuned for the current war effort.

## Deepseek-3.2-Simple - Turn 428 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> We are in the final stages of domination victory. Our immediate targets are Spanish capitals Madrid and Cordoba, which require nuclear bombardment followed by ground assault. We must prioritize nuclear production (Nuke/UseNuke at 100) and naval/air supremacy to project power across oceans. Maintaining high production, gold, and science ensures we can continuously build military units and upgrade our forces. Diplomatic and espionage flavors secure our city-state alliances and intelligence on enemy movements. Zero expansion/wonder focus as we are in total war mode.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> Nuclear focus maxed (Nuke/UseNuke to 100) - we now have multiple Atomic Bombs ready and must use them decisively against Spanish capitals (Madrid, Cordoba) and Aztec defenses. AirCarrier raised to 95 for future Carrier production after Computers. Growth and Happiness increased slightly to address negative happiness in several occupied cities (Sao Paulo -24, Manaus -10, Fortaleza -10, etc.). Recon reduced to 25 since map is well-explored. Defense slightly reduced (85) to push more resources into offensive operations. Airlift raised to 85 for rapid troop deployment to Spanish/Aztec fronts. Conquest grand strategy maintained - Spain is the immediate target with their 2 original capitals, then full push on The Aztecs for domination victory.

## Deepseek-3.2-Simple - Turn 452 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `-5`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's invasion imminent in 4 turns. Maximize nuclear readiness (Nuke 100, UseNuke 100) for deterrence and potential equalizer. Anti-air (100), city defense (100), production (100), and science (100) essential to survive and reach nuclear weapons. Naval and air at 100 to counter Danish naval/air supremacy. Reduce non-essential investments (NavalGrowth, NavalTileImprovement to 50) and focus on immediate survival. Offense lowered to 80 as we prioritize defense and limited counterattacks (e.g., Truro).

- Replay: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> Critical survival mode. Denmark peace treaty expires in 5 turns with 66k military vs our 3.4k. They have 45 delegates (needs 41 for diplo victory) and 6/8 capitals for domination. Nuke priority raised to 95 and UseNuke to 85 - nuclear deterrence is our only equalizer. Advanced Ballistics after Nuclear Fission is essential. Slightly reduced Offense (90) and Mobile (90) to conserve units for defense. NavalRecon reduced to 80 since we know Denmark's fleet position. Airlift increased to 30 for rapid redeployment when Denmark attacks. Growth and infrastructure slightly reduced to prioritize military production. All defense/antiair/air/naval values stay at max to counter Denmark's combined arms threat.

## GLM-4.7-Simple - Turn 457 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Increased UseNuke to 80 and Air to 100 in response to England's catastrophic escalation this turn. English Giant Death Robots (now 2 in Atlanta zone) and XCOM Squad paradrops on American soil create existential threat to our 3 remaining cities. Recent combat losses (Modern Armor, Mechanized Infantry, Heavy Bomber destroyed) demonstrate conventional warfare impossibility. Nuclear deterrence with 2 Uranium is becoming survival necessity, not option. Air defense at maximum priority because English Strategic Bombing continues destroying our units (Fighter bombed our Heavy Bomber). Bazooka successfully damaging XCOM Squad near Washington proves defensive capability is still viable - prioritize air/anti-air to protect cities from English air superiority. Lasers completes in 4 turns, then Stealth for Stealth Bomber - only path to asymmetric defense against England's 45:1 military advantage. Assyria (18,443 military fighting England) must be maximized as counterweight.

- Replay: use_nuke 70 => 75 (Δ +5), nuke 100 => 100 (Δ +0)
> Slight adjustments: Offense raised from 0 to 5 to allow limited counter-attacks against weakened English units near our cities (we damaged several Sensor Combat Ships and killed a Heavy Bomber this turn - exploiting damaged enemies is viable). Antiair raised from 85 to 90 as England massed Heavy Bombers in New York (2) and maintains air superiority. Air raised from 80 to 85 in preparation for Stealth Bomber research. Diplomacy raised from 50 to 60 - World Congress voting in 7 turns on Global Hegemony; Assyria (34 delegates) approaching diplomatic victory which may end game before England's Science Victory. Mobilization slightly increased from 20 to 30 for faster unit replacement after losing Modern Armor and Mechanized Infantry this turn. All other critical flavors maintained at maximum.

## Kimi-K2.5-Briefed - Turn 383 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CRITICAL WORKER REALLOCATION: Reduced Infrastructure from 100 to 20 to free the 7 Builders currently tied to railroad projects. Military briefing confirmed all workers occupied on railroads while 6 aluminum tiles remain unimproved despite TileImprovement 100. Aluminum crisis (-5/turn, 26 turns remaining) threatens Yamato production and bomber upgrades. Maintained TileImprovement 100 and Production 100 to prioritize aluminum mine construction once workers freed. Nuclear Fission completes in 6 turns - need Advanced Ballistics next for Nuclear Missile and Yamato. UseNuke increased to 100 to enable atomic strikes on Cusco immediately upon availability. AirCarrier 100 ensures carriers for Yamato deployment. Conquest remains correct grand strategy - Cusco is final capital for domination victory.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> FINAL PUSH TO CUSCO - EXECUTION REALIGNMENT: Three critical crises demand flavor overhaul: (1) ALUMINUM: Infrastructure 100→30 frees all 7 workers from railroad projects to build aluminum mines on 6 unimproved tiles. TileImprovement stays at 100 to prioritize mines. Stockpile of 130 at -5/turn = 26 turns until depletion - must start mines NOW. (2) GOLD: -900 GPT deficit with 520 reserve. Gold 5→85 forces AI to build gold buildings, prioritize gold tiles, and establish revenue. (3) HAPPINESS: 38% gives combat penalty. Happiness 70→95 is critical to restore combat effectiveness for Cusco assault. Nuclear missile path (via Advanced Ballistics) bypasses need for forward airbase within 6 tiles of Cusco - nukes have unlimited range. Mobile 0→40 for armor push to Cusco. Naval 95→50 shifts focus to land war. UseNuke 95→100 maximum commitment to nuclear strike on Cusco.

## GLM-4.7-Simple - Turn 435 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Iroquois 97% Popular - cultural extinction in 3-4 turns. Maximum offensive posture required to capture Onondaga before cultural victory. Espoo Stealth Bomber complete provides immediate air strike capability. Linköping Stealth Bomber in 4 turns is too slow - must use existing air assets and conventional forces at Genesse River NOW. UseNuke 100 authorizes nuclear strikes if conventional forces cannot reach Onondaga in time. All production and resources prioritized for war. Diplomacy irrelevant when facing extinction - complete conquest or nothing matters.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Iroquois 3 turns from cultural victory - existential emergency. Happiness at 47% with combat penalty is CRITICAL - raised to 100 to prioritize happiness buildings/works. Airlift 100 to rush forces to Genesse River front. AirCarrier raised to 50 for carrier-based strikes on Onondaga. UseNuke increased to 95 - nuclear strikes on Onondaga authorized if conventional advance fails. Culture raised to 40 to boost cultural output against Iroquois tourism. Reduced lower-priority flavors (NavalGrowth, NavalTileImprovement, WaterConnection, Wonder, Religion, Expansion) to concentrate impact on war-critical priorities.

## GLM-4.7-Simple - Turn 429 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+5`

- Original: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> Maintaining UnitedNations grand strategy with defensive diplomatic posture. Adjusted Italy diplomacy: reduced hostility toward Portugal (now neutral) to seek accommodation while maintaining maximum defense; reset France to neutral as Order ideological peer with voting potential. Arsenal completes in 2 turns strengthening city defense. Electronics research ordered after Computers for Police Station and path to nuclear deterrence against Portugal's uranium advantage. Fraternity policy selected for +3 Food and +3 Science from connections, addressing Venice's health issues and supporting population growth. Flavor adjustments prioritize defensive survival, scientific progress toward nuclear weapons, and diplomatic engagement with Sweden and city-states.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 80 => 90 (Δ +10)
> Maintaining defensive grand strategy with key adjustments: Nuke flavor increased from 80→90 and UseNuke from 80→85 to accelerate nuclear deterrence program now that Uranium quarry is operational. Science increased from 90→95 to accelerate Computers completion and path to Rocketry/Nuclear Fission. Diplomacy increased from 90→95 with World Congress voting in 7 turns - Venice must maximize delegate coordination with Sweden and compete for city-state influence. Espionage increased from 85→90 as Siam's spy was just identified in Venice and multiple agents are operating in Egypt; counter-intelligence and tech stealing are both critical. MilitaryTraining slightly increased to maintain unit quality. All defensive flavors remain at maximum given Portuguese forces massing near Venice with Machine Guns, Infantry, and Artillery at citadel positions.

## GLM-4.7-Simple - Turn 435 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Iroquois 97% Popular - cultural extinction in 3-4 turns. Maximum offensive posture required to capture Onondaga before cultural victory. Espoo Stealth Bomber complete provides immediate air strike capability. Linköping Stealth Bomber in 4 turns is too slow - must use existing air assets and conventional forces at Genesse River NOW. UseNuke 100 authorizes nuclear strikes if conventional forces cannot reach Onondaga in time. All production and resources prioritized for war. Diplomacy irrelevant when facing extinction - complete conquest or nothing matters.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Iroquois 97% Popular - 3 turns to cultural victory. Maximum offense required. Air 100 + Airlift 100 to rebase Stealth Bombers to Paris (French ally city within range of Onondaga) for strategic bombing. Mobile 100 to rush ground forces toward Onondaga. Culture raised to 45 and Happiness to 95 to slow Iroquois influence gain and fix combat penalty from 47% happiness. UseNuke 95 - nuclear authorization if conventional offensive cannot reach Onondaga in time. Every asset must focus on Iroquois destruction.

## Deepseek-3.2-Simple - Turn 495 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 90 (Δ +0)
> Diplomatic victory is imminent (2 turns), but we must prepare for contingencies. Maximizing Offense, UseNuke, and Air ensures aggressive nuclear and conventional strikes to recapture Indonesian capitals (Honolulu 17%, London 68%) and prevent their domination victory. Slight Diplomacy boost helps secure city-state alliances through the vote. All other flavors remain at previous high levels to maintain total war footing.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 90 => 90 (Δ +0)
> Diplomatic victory in 3 turns - we have exactly 42 delegates (threshold met). Must survive and prevent Indonesia from winning domination (50% capitals) or cultural victory. Indonesia nuked Nottingham this turn - boost Antiair to 100 to protect against further nuclear/bomber strikes. Increase UseNuke to 95 for nuclear retaliation against Indonesian cities. Keep all military flavors maxed to maintain pressure. Reduce Espionage slightly as spy operations less critical with vote imminent. Science victory remains backup with spaceship parts in production.

## Kimi-K2.5-Simple - Turn 422 - retry 1

**Deviation (replay vs original):** use_nuke `-25`, nuke `+0`

- Original: use_nuke 50 => 80 (Δ +30), nuke 95 => 95 (Δ +0)
> Total war against India requires maximum military prioritization while preventing economic collapse. Offense/Air/Ranged at 85-95 ensures concentrated attacks on Delhi and their core cities. UseNuke at 80 signals willingness to deploy nuclear weapons if India advances. Gold/Happiness at 80-90 sustains unit maintenance and prevents combat penalties. Espionage at 100 directs spies to sabotage India's spaceship production in Constantinople and Calcutta. Mobilization at 30 begins reinforcing depleted units without overtaxing economy.

- Replay: use_nuke 50 => 55 (Δ +5), nuke 95 => 95 (Δ +0)
> India peace treaty expired - TOTAL WAR NOW. India is 50% toward science victory and 4/5 cultural influence; delay means death. Increase Offense (85), Mobilization (50), MilitaryTraining (65), and Airlift (50) to rapidly project power toward Delhi. Increase Defense (60) and CityDefense (50) against Indian counter-attacks. Antiair raised to 65 against India's Jet Fighters. Gold/Happiness remain at 100 to stabilize -909 GPT and 42% happiness (combat penalty). Nuke at 95 for deterrence. Capture Ulundi first (4th capital, 50% domination parity), then push Delhi.

## GLM-4.7-Simple - Turn 408 - retry 3

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> CRITICAL: Portugal completed SS Engine (3rd spaceship part) and CERN - emergency nuclear strike plan. Maximizing Offense/Mobilization/Nuke/UseNuke to 100 for Portugal theater operations. Science and Production at 100 to rush Advanced Ballistics and nuclear missile production before Portugal achieves nuclear superiority. Air at 95 for Golden Age bomber operations starting in 2 turns. Diplomacy maintained for coalition coordination (Germany must conduct ground invasion alongside our nuclear strikes). Defense reduced to 40 - total war mode acceptable given Portugal's multi-victory threat requiring breaking through before they complete spaceship.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Portugal completed SS Engine (3/6 parts, 50% science victory). Critical adjustments: (1) Happiness 85→92 - combat penalty from 48% happiness is crippling our effectiveness across 3 wars; (2) Nuke 100, UseNuke 80→85 - Portugal's accelerating science victory demands willingness to use nuclear weapons as soon as available; (3) Air 75→80 - more air power needed for future strikes on Lisbon; (4) Airlift 35→40 - rapid deployment needed; (5) Naval 65→70 - more naval presence to contest Polynesia/Pacific; (6) NavalRecon 45→50; (7) TileImprovement 40→50 - Iron Fist policy's +50% worker rate justifies more improvement investment; (8) Espionage stays 85 - Agent Odtsetseg in Lisbon, Agent Nergüi traveling to Salzburg for intel on Portuguese science progress.

## GLM-4.7-Simple - Turn 408 - retry 1

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> CRITICAL: Portugal completed SS Engine (3rd spaceship part) and CERN - emergency nuclear strike plan. Maximizing Offense/Mobilization/Nuke/UseNuke to 100 for Portugal theater operations. Science and Production at 100 to rush Advanced Ballistics and nuclear missile production before Portugal achieves nuclear superiority. Air at 95 for Golden Age bomber operations starting in 2 turns. Diplomacy maintained for coalition coordination (Germany must conduct ground invasion alongside our nuclear strikes). Defense reduced to 40 - total war mode acceptable given Portugal's multi-victory threat requiring breaking through before they complete spaceship.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Portugal completed SS Engine (3rd spaceship part, 50%) and built CERN - science victory accelerating dangerously. Increasing Happiness from 85→95 (critical at 48% with combat penalty; Golden Age in 2 turns will help but sustained happiness needed), UseNuke 80→85 (Portugal's multi-victory threat demands maximum nuclear readiness), TileImprovement 40→50 (Iron Fist's +50% worker rate synergizes for rapid development). Maintaining Nuke 100, Science 100, Production 95, Diplomacy 95 as top priorities. Espionage 85 counters Austria's spies in New Sarai/Tabriz.

## GLM-4.7-Simple - Turn 356 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `-5`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 80 (Δ +5), nuke 85 => 95 (Δ +10)
> Manhattan Project completed and Uranium quarry built at 15,27 - nuclear deterrence is now achievable. Nuke increased to 95 (from 85) as highest priority since we can actually build Atomic Bombs once Nuclear Fission is researched and Uranium connects. UseNuke increased to 80 (from 75) - nuclear weapons are now a real deterrent against India's 18,480 military. Happiness increased to 90 (from 80) - 39% happiness with combat penalty is a critical vulnerability across all war fronts. Infrastructure increased to 70 (from 65) to ensure Uranium quarry gets railroad connection. TileImprovement increased to 45 (from 40) to support resource connection. All other flavors maintained - Defense/CityDefense/MilitaryTraining/Science remain maxed, Antiair at 100, Offense at 35 for defensive posture.

## GPT-OSS-120B-Simple - Turn 344 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `-15`

- Original: use_nuke 90 => 100 (Δ +10), nuke 80 => 100 (Δ +20)
> Maximize our nuclear capabilities and carrier support to decisively strike Polynesian island forts, while maintaining our current aggressive conquest posture and strong production, gold, and happiness engines.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 80 => 85 (Δ +5)
> Continue Conquest focus while boosting Growth and Happiness to address our critical 50% happiness (combat penalty) from 98% war weariness. Increase Science to 85 to accelerate toward nuclear tech (Replaceable Parts → Plastics → Atomic Theory → Nuclear Fission). Boost Diplomacy to 95 for World Congress vote in 6 turns where we must block Polynesia's sanction proposal. Maintain maximum naval/air production for island assaults. Keep UseNuke at 95 for eventual nuclear strikes on Polynesian island forts.

## Deepseek-3.2-Simple - Turn 400 - retry 3

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 100 to ensure aggressive nuclear strikes when we initiate war with Russia. Our atomic bomb production is nearing completion, and we want to leverage our nuclear arsenal decisively for swift capital captures.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintain Conquest grand strategy with all military flavors at maximum readiness. Increase UseNuke from 80 to 85 as we now have operational atomic bombs produced in Antwerp with more coming from Seville (3 turns), Cordoba (2 turns), Toledo (6 turns), Santiago (7 turns), Kathmandu (3 turns), Marrakech (2 turns), Agaidika (8 turns), Te-Moak (5 turns), and Moson Kahni (5 turns). Russia is actively bolstering defenses with Ace Pilot fighters in Yakutsk and forts near our border; we must be ready to strike decisively when the peace promise expires (~19 turns). Keep Espionage at 100 since Russia's spy was caught in Toledo this turn. Science at 100 to reach Information Era parity with Russia. Diplomacy at 100 to maintain coalition against Songhai and isolate Russia.

## Deepseek-3.2-Simple - Turn 400 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 100 to ensure aggressive nuclear strikes when we initiate war with Russia. Our atomic bomb production is nearing completion, and we want to leverage our nuclear arsenal decisively for swift capital captures.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Increase UseNuke from 80 to 85 as our nuclear arsenal grows - we must be ready to use nukes decisively when war with Russia breaks out after the peace treaty expires (~19 turns). Increase Spaceship from 40 to 50 as Satellites research approaches, ensuring we can pursue Science Victory as a backup path. Slightly reduce TileImprovement from 70 to 60 as most tile development is complete and we need production focus on military units. Maintain all other military/economic flavors at current high levels to continue war preparation against Russia while keeping our deception facade intact.

## GLM-4.7-Simple - Turn 356 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `-10`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 80 (Δ +5), nuke 85 => 90 (Δ +5)
> Manhattan Project completed - nuclear deterrence is now achievable. Nuke raised to 90 (Manhattan Project done, Uranium quarry being built near Atlanta), UseNuke raised to 80 (legitimate deterrent against India's 18,480 military). Happiness raised from 80 to 90 - combat penalty from 39% Unhappy status is devastating across all war fronts; reducing war weariness via peace with Persia is critical. Growth raised to 55 to support population recovery and happiness. Gold raised to 85 for potential Uranium trade with Netherlands (4 Uranium). Offense reduced to 30 - defensive survival posture. Espionage reduced to 85 after spy detected in Lisbon. Science remains 100 for Nuclear Fission priority.

## Deepseek-3.2-Simple - Turn 358 - retry 1

**Deviation (replay vs original):** use_nuke `-25`, nuke `-35`

- Original: use_nuke 50 => 80 (Δ +30), nuke 50 => 100 (Δ +50)
> Prioritize nuclear deterrence and naval/air defense to counter India's massive military threat. Maximize espionage to protect against enemy spies and diplomacy to secure city-state alliances for the upcoming World Congress vote. Maintain strong economic and scientific output to support military production and technological edge.

- Replay: use_nuke 50 => 55 (Δ +5), nuke 50 => 65 (Δ +15)
> Critical adjustments needed: America's switch to Order weakens our diplomatic bloc significantly. We now have 20 delegates vs 45 needed, and America (15 delegates) may now vote with Order bloc. Increase Nuke/UseNuke (from 50→65/55) since we completed the Manhattan Project and need nuclear deterrence against India's 17,888 military strength. Increase Offense (40→45) and Mobile (50→55) to support counter-attacks against Indian forces near Jakarta/Ban Chiang and prepare for Combined Arms Tanks. All other priorities remain: maximum Diplomacy for upcoming World Congress vote in 6 turns, maximum naval/air/defense against Indian naval raids, and full production/gold/science for United Nations project and military.

## Deepseek-3.2-Simple - Turn 495 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+5`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 90 (Δ +0)
> Diplomatic victory is imminent (2 turns), but we must prepare for contingencies. Maximizing Offense, UseNuke, and Air ensures aggressive nuclear and conventional strikes to recapture Indonesian capitals (Honolulu 17%, London 68%) and prevent their domination victory. Slight Diplomacy boost helps secure city-state alliances through the vote. All other flavors remain at previous high levels to maintain total war footing.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 90 => 95 (Δ +5)
> Diplomatic victory vote in 3 turns - we have exactly 42 delegates (100% needed). Boosted Diplomacy from 20→50 to protect city-state alliances before the vote, especially Harappa (185 influence, most vulnerable). Boosted Nuke/UseNuke from 90→95 to maximize nuclear strikes against Indonesia this turn and next - we have 6 Atomic Bombs positioned at Nottingham and Samarinda. Boosted Spaceship from 30→50 as backup victory path (SS Boosters finishing in 4-5 turns, Stasis Chamber in 8, Engine in 9). Increased Defense slightly (25→35) after Nottingham was nuked. Maintain all offensive/naval/air priorities for total war.

## Deepseek-3.2-Simple - Turn 495 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+5`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 90 (Δ +0)
> Diplomatic victory is imminent (2 turns), but we must prepare for contingencies. Maximizing Offense, UseNuke, and Air ensures aggressive nuclear and conventional strikes to recapture Indonesian capitals (Honolulu 17%, London 68%) and prevent their domination victory. Slight Diplomacy boost helps secure city-state alliances through the vote. All other flavors remain at previous high levels to maintain total war footing.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 90 => 95 (Δ +5)
> Diplomatic Victory is locked in 2 turns (42/42 delegates). Priority shifts: increase Defense 30→50 and Antiair 90→100 to protect against further Indonesian nukes on Nottingham/York. Slightly reduce Offense 95→85 to preserve units rather than overcommit. Increase Nuke/UseNuke to 95 for maximum nuclear retaliation capability if Indonesia strikes again. Increase Spaceship 30→50 as backup victory path. Reduce Diplomacy 20→10 since the vote is already secured. Conquest grand strategy maintained for military production to survive the 2-turn window.

## Kimi-K2.5-Briefed - Turn 396 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 65 => 80 (Δ +15), nuke 80 => 90 (Δ +10)
> ETHIOPIA CULTURAL VICTORY IMMINENT: Ethiopia has INFLUENCED ALL 7 CIVS and reached Order:3. They need only adopt CEP tenet and build it to win immediately. Switching to CONQUEST grand strategy with maximum mobilization (100) and offense (95). Naval (95) and Airlift (80) priorities enable rapid amphibious assault on Ethiopian coastal cities (Lalibela, Axum, Gondar) to destroy CEP before construction. Espionage (90) to accelerate Salem rig for delegate, but military solution is primary. All economy/culture deprioritized - this is existential war.

- Replay: use_nuke 65 => 70 (Δ +5), nuke 80 => 80 (Δ +0)
> CRITICAL THREAT RESPONSE: Ethiopia at Influential on all 7 civs with Order:3, can build CEP at any time for cultural victory. Increased Offense (85), Mobilization (95), Production (90), Mobile (80) to accelerate amphibious capability against Ethiopia - we have only 9 embarkable infantry and NO transports. Increased Naval (90) for transport production and coastal bombardment. Increased Nuke (80) and UseNuke (70) as nuclear deterrent becomes critical once Nuclear Fission completes in 16 turns. Maxed Diplomacy (100) for urgent delegate acquisition - flipping Zurich from Greece yields +2 delegate swing. Maxed Espionage (95) for Salem rig and city-state operations. Increased MilitaryTraining (80) and Air (80) for Ethiopian campaign quality. Reduced Culture (10) and TileImprovement (55) - not victory paths. Science/Spaceship maintained as primary victory path.

## GLM-4.7-Briefed - Turn 409 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> MULTI-THEATER EMERGENCY RESPONSE for Shoshone Cultural Victory (6 turns) and Treasury Crisis: Offense 95, Mobile 95, Nuke 100, UseNuke 100 - maximum priority on Shoshone disruption via nuclear/conventional assault in 6-turn window. Gold increased to 85 (from 70) - CRITICAL address of treasury exhaustion (~8 turns) through uranium sales + gem liquidation to survive until Manhattan completion. Defense reduced to 70 (from 75), CityDefense to 70 (from 80) - resources diverted from secondary holdings to Shoshone front. Diplomacy 95 (from 90) - enhanced priority on Carthage peace for delegate bloc and potential sanction relief. Science 100 maintained - fundamental for nuclear capability and keeping tech parity. This is all-hands-on-deck existential threat response.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> EMERGENCY RECALIBRATION for 6-turn Shoshone Cultural Victory countdown: UseNuke increased to 100 (from 95) - nuclear strikes on high-tourism Shoshone cities are our ONLY asymmetric counter against 30,471 military strength. Diplomacy increased to 95 (from 90) - World Congress vote imminent, must secure delegate bloc via Carthage peace. Gold increased to 85 (from 70) - -242G/turn deficit is critical, must stabilize economy. Culture increased to 65 (from 45) - every point of culture slows Shoshone influence growth toward Influential status. Offense reduced to 85 (from 90), Mobile to 85 (from 90), Antiair to 80 (from 100) - Polish fighter eliminated, conventional assault on Shoshone is futile (30K vs 17K), nuclear capability is the priority. Espionage increased to 95 (from 90) - spies can steal tech and provide intel on Shoshone cities for nuclear targeting.

## GLM-4.7-Briefed - Turn 433 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> EMERGENCY: Netherlands at 42 delegates can win diplomatic victory in 9 turns (turn 442). Only way to stop them is military action against their protected city-states (Quebec City, Ife, Melbourne) - each provides +1 delegate. Offense increased (70) to prepare amphibious assaults. Nuclear readiness maximized (95/90) - atomic bomb available for strategic coercion of Netherlands or Denmark cooperation. Mobile (80) and Naval (85) maximized for rapid deployment to distant city-states. Production/Science/Spaceship kept maxed as backup victory paths. Diplomacy reduced to 50 as traditional diplomacy cannot stop Netherlands' delegate advantage. Strategic shift from holding Danish front to aggressive anti-Dutch operations.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> EMERGENCY REBALANCE: Netherlands at 42 delegates can win diplomatic victory in 9 turns. Offense dramatically increased (50→85) to authorize immediate military strikes against Netherlands' city-state allies (Salem, Bogota are Neighbors to Japan - fastest targets). Defense reduced (50→35) - offensive action more critical than static defense. Mobilization increased (20→45) for rapid unit deployment. Naval increased (80→90) and Air increased (75→85) for amphibious/strategic strike capability against Dutch CS allies. Nuke/UseNuke increased to near-maximum as existential deterrent. Diplomacy slashed (70→45) - diplomatic victory CANNOT be blocked by votes alone; only military decapitation of Netherlands' CS allies works. Gold reduced (90→70) - prioritize military production over treasury. Science/Spaceship/Production remain at 100 as backup science victory path. Minor CS competition reflected in persona changes.

## Deepseek-3.2-Simple - Turn 400 - retry 2

**Deviation (replay vs original):** use_nuke `-35`, nuke `-25`

- Original: use_nuke 60 => 100 (Δ +40), nuke 70 => 100 (Δ +30)
> Persia declared war and Poland's peace treaty expired. We must prioritize immediate military survival while maintaining diplomatic momentum. Flavors are shifted to maximum mobilization, nuclear deterrence (UseNuke: 100), city defense, and air/naval supremacy to counter Persia's naval attacks. We maintain UnitedNations to keep city-state alliances critical for votes, but spaceship production is halted (0) for wartime industry.

- Replay: use_nuke 60 => 65 (Δ +5), nuke 70 => 75 (Δ +5)
> Persia declared war on us this turn and killed several naval units. Increasing Offense from 40 to 65 to push back effectively, Mobilization to 100 for maximum military production, MilitaryTraining to 85 for unit quality, Spaceship from 30 to 55 as science victory backup (SS Stasis Chamber nearly done), Nuke/UseNuke slightly increased as deterrent against Persian aggression. All economic/diplomatic flavors maintained at maximum for diplomatic victory push.

## Kimi-K2.5-Simple - Turn 372 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximum aggression maintained against Carthage (100% war score, 4% weariness) while responding to India's new Manhattan Project threat. UseNuke increased to 100 - must deploy atomic weapons immediately upon acquiring Nuclear Fission to counter India's nuclear capability. Satellites/Spaceship flavors at 95 ensure Science Victory backup. Continue prioritizing T-34 tanks, stealth bombers, and heavy bombers to eliminate Carthage's cities before they can deploy their 5 uranium reserves. Naval and Air strengths maintained for coastal bombardment of Carthage and defense against Indian naval aggression.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Critical adjustments for India's Manhattan Project completion: Science 95→100 to rush Nuclear Fission; Happiness 90→95 to combat 44% unhappiness causing combat penalty; Antiair 95→100 to defend against Indian nuclear bombers; UseNuke 90→95 to prepare nuclear retaliation; Espionage 90→95 to steal Indian nuclear tech; CityDefense 85→90 for nuclear protection. Culture 15→10, Diplomacy 10→5, Religion 10→5 as non-priorities. Domination path clear: capture Persepolis (under attack), Carthage city, and Delhi for 8/8 capitals = victory.

## Kimi-K2.5-Simple - Turn 392 - retry 3

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Manhattan Project COMPLETED in Karakorum - nuclear weapons now available! With peace treaties expired and Patriotic War policy active, immediately shifting to total war footing. UseNuke increased to 100 to ensure immediate atomic weapon employment once Nuclear Fission completes (12 turns). Offense and Mobile at 95/90 for twin assaults on Persepolis (Persia) and Washington (America). Air 100 prioritizes Heavy Bombers for atomic bomb delivery via Radar technology. Will fight two-front war against Autocracy powers while maintaining deception toward Order allies, particularly Korea. Science 100 critical for Advanced Ballistics nuclear missile delivery systems.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Manhattan Project complete - nuclear arsenal now available. Immediate offensive against Persia is priority #1: Offense maximized to 100, Mobile increased to 95 for tank breakthrough toward Persepolis. UseNuke increased to 85 with 5 uranium quarries completed - nuclear weapons provide ultimate deterrent against Korea's 12,157 military. Airlift increased to 80 for rapid redeployment. Antiair raised to 90 to counter Korean/Persian air threats. Diplomacy raised slightly to leverage new Geneva alliance. Espionage increased to 80 - spy in Seoul can complete Geneva's quest (333 Influence + 483 Science) for a spy mission against Sejong. Korea becomes Influential on me in 4 turns - every turn of Persian conquest matters.

## Kimi-K2.5-Simple - Turn 416 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 416: CRITICAL CULTURAL VICTORY THREAT. Maya at 6/7 influential building Citizen Earth Protocol. Peace expires next turn - immediate total war required. Manhattan Project completes in 1 turn. Morocco (42260 strength) joins war via defensive pact. Maximum aggression flavors: Offense/Mobilization/Production/Nuke/UseNuke all at 100%. Must capture Maya cities, especially Palenque, before cultural victory. Nuclear weapons authorized for city capture.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 416: EXISTENTIAL WAR IMMINENT. Peace with Maya expires NEXT TURN - final countdown. Manhattan Project completing in Berlin gives nuclear capability. Increased Science to 80 to rush Advanced Ballistics for Nuclear Missiles - our only equalizer against Morocco's 42k military. Increased Happiness to 80 to address critical 49% happiness with combat penalty - we cannot fight effectively with - combat modifier. Increased Nuke/UseNuke to 100 maximum - nuclear weapons are essential strategic assets against Morocco's overwhelming conventional forces. All other war flavors maintained at maximum. Must crush Maya before Citizen Earth Protocol completes.

## Qwen-3.5-Simple - Turn 389 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Final domination push configuration. Offense/Mobilization/Nuke at 100% for maximum military production and nuclear strike capability against Brazil/Babylon/Rome capitals. Air/Antiair at 100/95 to counter enemy bombers and maintain air superiority. Mobile/Ranged at 100/95 for mechanized infantry and bazooka pushes. Production/Science at 100% to sustain war machine and complete Nuclear Fission tree. Espionage at 90% to rig World Congress elections (9 turns remaining, we trail Brazil 16-17). Expansion/Wonder at 0% - no new cities needed, only conquest of remaining 3 capitals.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> MAXIMUM PRIORITY: Brazil completed Manhattan Project this turn - they can now build atomic bombs. UseNuke raised to 100 to ensure immediate nuclear deployment once we have capability. Gold raised from 70 to 85 to address -349 GPT financial crisis. Happiness raised from 70 to 85 to combat 45% unhappiness penalty affecting combat effectiveness. Naval raised from 75 to 80 to counter Rome's submarine attacks killing our Dreadnoughts. All other flavors maintained - Conquest grand strategy unchanged. We MUST capture Rio, Rome, and Babylon capitals before Brazil deploys nukes against our forces.

## GLM-4.7-Briefed - Turn 433 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> EMERGENCY: Netherlands at 42 delegates can win diplomatic victory in 9 turns (turn 442). Only way to stop them is military action against their protected city-states (Quebec City, Ife, Melbourne) - each provides +1 delegate. Offense increased (70) to prepare amphibious assaults. Nuclear readiness maximized (95/90) - atomic bomb available for strategic coercion of Netherlands or Denmark cooperation. Mobile (80) and Naval (85) maximized for rapid deployment to distant city-states. Production/Science/Spaceship kept maxed as backup victory paths. Diplomacy reduced to 50 as traditional diplomacy cannot stop Netherlands' delegate advantage. Strategic shift from holding Danish front to aggressive anti-Dutch operations.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> EXISTENTIAL EMERGENCY: Netherlands has exactly 42 delegates (victory threshold) and can win Diplomatic Victory at the Global Hegemony vote in 9 turns. Our 48-delegate coalition CANNOT block this - the threshold is an absolute quota. The ONLY path to survival is military capture of Dutch-ally city-states to strip delegates below 42. Switching to Conquest grand strategy to authorize offensive operations. Offense dramatically increased (50→85) for city-state assaults. Naval maximized (95) for amphibious operations against Bogota and Salem (both neighbors to Japan). Mobile increased (85) for rapid deployment. Defense reduced (35) - survival requires offense, not fortification. Science slightly reduced (85), Spaceship reduced (75) - science victory is secondary to surviving the vote. Gold reduced (65) - military production takes priority over treasury. Diplomacy reduced (50) - this crisis cannot be solved diplomatically. Nuclear deterrence maintained at extreme levels as last-resort option if conventional assault fails.

## GLM-4.7-Simple - Turn 437 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 90 after Awasa nuclear attack - Netherlands has now used 3 atomic weapons against my cities (Turfan x2, Awasa). No choice but to prepare nuclear retaliation as deterrent. Increase Air to 95 and Antiair remains 100 - demonstrated success shooting down 3 Netherlands Fighters this turn, must maintain air superiority against their bombers and XCOM attacks. CityDefense increased to 95 - with Netherlands nuclear buildup at Nijmegen (3+ atomic bombs visible) and XCOM paradrop squads, all cities need maximum protection. Offense increased to 60 to pressure Netherlands territory before they can launch more nuclear strikes. Diplomacy reduced from 90 to 85 - coalitions matter but survival against nuclear Netherlands takes priority. Espionage at 100 - need intelligence on Netherlands nuclear deployment and counter-espionage at critical cities like Attila's Court, Shedet.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Critical adjustments after Netherlands nuclear attack on Awasa (pop 21→12, fallout created, Machine Gun killed). Increase Diplomacy from 90→100 (existential priority: Global Hegemony vote in 6 turns, Netherlands has 44/42 delegates needed). Increase Growth 55→65 (Awasa population recovery). Increase UseNuke 80→85 (nuclear retaliation more justified after being nuked). Increase Happiness 65→70 (nuclear recovery). Maintain Defense 95, Antiair 100, Air 100, Nuke 100, Science 100, Production 100, Mobilization 100. All other flavors unchanged. Must prevent Netherlands diplomatic victory - coalition coordination (61 delegates: Huns 8, Mongolia 11, Japan 13, Denmark 15, Venice 14) is only counter to Netherlands' 44.

## Kimi-K2.5-Simple - Turn 452 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 95 => 100 (Δ +5)
> Turn 452: Critical survival situation - Byzantium at 40/44 delegates with World Congress voting in 1 turn. They just demonstrated nuclear aggression by nuking Madrid. Apollo Program completes next turn - must immediately pivot to maximum spaceship production. Increased Nuke flavor to 100 (from 95) and UseNuke to 95 (from 90) - need immediate nuclear deterrent capability given Byzantine nuclear attack and Mongol peace expiry. Production boosted to 95 (from 90) for rapid spaceship part construction after Apollo completes. GreatPeople to 85 for Great Engineer acquisition. All other priorities secondary to surviving long enough to complete science victory.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 95 => 100 (Δ +5)
> Turn 452: CRITICAL - Byzantium nuked Madrid (Spain) this turn, population 37→22, widespread fallout. This confirms nuclear-armed enemies will use WMDs against Order allies. Antiair raised to 100 and Air to 100 for maximum air/nuclear defense posture. CityDefense raised to 95. Nuke/UseNuke raised to 100/95 for credible deterrence. Apollo Program completes NEXT TURN in New York - spaceship parts become the absolute priority. World Congress votes next turn with Byzantium at 40/44 delegates - they may win diplomatically if we don't rush science victory. Maintaining maximum Science (100), Production (95), and Spaceship (100) flavors. Diplomacy at 75 to continue competing for city-state delegates. Defense remains 100 against Shoshone border threat and potential Mongol aggression post-peace expiry.

## Kimi-K2.5-Simple - Turn 452 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 95 => 100 (Δ +5)
> Turn 452: Critical survival situation - Byzantium at 40/44 delegates with World Congress voting in 1 turn. They just demonstrated nuclear aggression by nuking Madrid. Apollo Program completes next turn - must immediately pivot to maximum spaceship production. Increased Nuke flavor to 100 (from 95) and UseNuke to 95 (from 90) - need immediate nuclear deterrent capability given Byzantine nuclear attack and Mongol peace expiry. Production boosted to 95 (from 90) for rapid spaceship part construction after Apollo completes. GreatPeople to 85 for Great Engineer acquisition. All other priorities secondary to surviving long enough to complete science victory.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 95 => 100 (Δ +5)
> Turn 452: Byzantium nuked Spain's Madrid this turn - confirmed nuclear aggressor. Critical adjustments: Nuke 95→100 and UseNuke 90→95 for maximum nuclear deterrence priority given imminent nuclear threat. Antiair 95→100 to prioritize anti-air defenses against potential nuclear delivery. Production 90→95 for faster spaceship part construction after Apollo completes next turn. GreatPeople 80→85 to maximize Great Engineer/Scientist generation for Spaceflight Pioneers synergy. Science, Defense, and Spaceship remain at 100 - these are our only viable path to victory before Byzantium's diplomatic win. Offense remains 0 - we cannot afford offensive operations with 2035 vs 42117 military strength.

## Kimi-K2.5-Simple - Turn 416 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 416: CRITICAL CULTURAL VICTORY THREAT. Maya at 6/7 influential building Citizen Earth Protocol. Peace expires next turn - immediate total war required. Manhattan Project completes in 1 turn. Morocco (42260 strength) joins war via defensive pact. Maximum aggression flavors: Offense/Mobilization/Production/Nuke/UseNuke all at 100%. Must capture Maya cities, especially Palenque, before cultural victory. Nuclear weapons authorized for city capture.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 416: TOTAL WAR ON MAYA - PEACE EXPIRED. Key adjustments: Happiness raised from 60 to 80 (combat penalty from unhappiness is critically weakening our forces). Nuke/UseNuke raised to 100 (Manhattan Project completing, Nuclear Fission in 10 turns). Minor reductions to MilitaryTraining/Antiair/Airlift to free flavor budget. All core offensive priorities remain at 100. Must capture Maya cities starting with Copan and Tulum where we have force superiority.

## Kimi-K2.5-Simple - Turn 387 - retry 1

**Deviation (replay vs original):** use_nuke `-45`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> TURN 387: MAXIMUM WAR FOOTING. Austria at 83% diplomatic victory with 4 turns remaining. All resources must pivot to immediate military production. Nuke/UseNuke at 100 for instant atomic weapon deployment upon Nuclear Fission completion. Offense/Mobilization/Production at 100 to maximize unit output for desperate Vienna strike. Air at 90 for heavy bomber production (conventional strategic bombing as fallback). Antiair at 100 counters Austria's air superiority. Diplomacy/Wonder/Culture at 0 - no time for long-term investments. Only total war can prevent defeat.

- Replay: use_nuke 50 => 55 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 387: Conquest strategy maintained with nuclear focus. Science increased 60→70 to accelerate Nuclear Fission research after Rocketry completes (6 turns). Offense increased 80→85 to support counterattack alongside Carthage's push near Utique/Damascus. UseNuke increased 50→55 as Austrian diplomatic victory approaches - nuclear strike on Vienna may become necessary. CRITICAL: World Congress votes in 4 turns - Freedom coalition (Venice 11+Carthage 13+Portugal 23+Songhai 5+America 12=64) must block Austria's World Ideology:Order (36 votes) AND support Open Door proposals for Samarkand/Novgorod to strip Austria of city-state delegates. Nuke 100/Production 95/Antiair 100 remain essential for survival.

## Kimi-K2.5-Simple - Turn 424 - retry 2

**Deviation (replay vs original):** use_nuke `-25`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DELHI SECURED (3RD CAPITAL = 38% DOMINATION). Pivoting all forces to Edinburgh (Celtic capital = 4th capital = 50% victory) and London (English capital = 5th = 63%). Djenne declared war but irrelevant. Escalating UseNuke to 100 for immediate atomic bombardment of Edinburgh and London once Nuclear Fission completes. Maintaining maximum offensive posture with combined arms (Heavy Bombers, T-34s, Helicopter Gunships, Naval forces). America peace treaty expired - war imminent for Washington (6th = 75%). World Congress in 8 turns ignored - domination priority absolute.

- Replay: use_nuke 70 => 75 (Δ +5), nuke 100 => 100 (Δ +0)
> DELHI CAPTURED - 3rd capital (37% domination). Slight UseNuke increase to 75 as Manhattan Project approaches completion. Happiness increased to 90 to stabilize Delhi (8 turns resistance, -36 happiness delta) and other occupied cities. Science bumped to 80 to accelerate Nuclear Fission research for atomic weapons. Celtic non-aggression pact has 19 turns remaining - London (5th capital = 63%) is the immediate target via England war, then Edinburgh (4th = 50%) after pact expires. All military flavors maintained at maximum for multi-front conquest operations against India, England, and Djenne.

## Kimi-K2.5-Simple - Turn 354 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> India is 100% Popular with me - on the verge of cultural victory. Must launch immediate total war with all available forces. Prioritizing air power, paratroopers, and nuclear preparation (Atomic Theory in 11 turns). Need maximum offensive punch to capture Indian cities before cultural victory triggers. Abandoning culture/diplomacy - only war matters now.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Strategic pivot: India needs 41 more turns to win culturally (bottleneck is Rome at 68%). We must race to nuclear weapons while preserving Rome as a cultural buffer. Shift: increase Science (80) for tech race to nukes, increase Culture (50) to resist Indian influence, increase Diplomacy (40) for World Congress (vote against Passport System), maintain Air/Nuke at 100 for strategic bombing path, reduce Offense slightly (85) as we de-escalate Rome front, keep Espionage high (80) for intel on India.

## Kimi-K2.5-Simple - Turn 421 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear weapons immediately available. Increased UseNuke to 100 for maximum aggression against Babylon. Babylon has Apollo Program (existential threat) with 2 Uranium and can build spaceship parts. Must deploy nuclear weapons immediately to destroy their production centers and prevent science victory. Maintaining maximum air power (100) for nuclear delivery capability and conventional strikes. War score only 12% against Babylon despite superior military - need to push harder before they complete spaceship parts. Ottoman alliance strong, trade secured for resources. Focus on producing nuclear missiles and advanced air units to deliver them.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Manhattan Project completes next turn — nuclear era begins. Critical problem: I have 0 Uranium while Babylon has 2. Must trade with Ottomans (5 Uranium) or secure sources. Increased Diplomacy from 15 to 30 to encourage Uranium trading with Ottomans. UseNuke raised from 85 to 90 for maximum nuclear aggression once Uranium is acquired. AirCarrier raised to 100 — carriers are essential for nuclear delivery to Babylon's coastal cities. Naval slightly reduced to reallocate toward air/carrier focus. Science reduced from 95 to 90 — still critical but Nuclear Fission is 11 turns away and I need production/economy focus now. Gold raised from 40 to 45 to support Uranium purchase trades. Happiness raised from 30 to 35 to manage war weariness (currently 34% vs Babylon).

## Kimi-K2.5-Simple - Turn 423 - retry 1

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Turn 422: CRITICAL SURVIVAL MODE. Raiatea at 33% health under Indonesian assault. Nuclear Fission 9 turns away - must survive until then. Maximized UseNuke to 100 for immediate nuclear deployment upon tech completion. Reduced Offense to 20 (pure defense only). Maintained Defense/CityDefense/Mobilization/Air/Antiair/Nuke/Production at 100 for maximum survival capacity. Increased Espionage to 90 for Harappa election rigging (oil critical). Eliminated Expansion/Wonder/Culture priorities. Growth reduced to 15 - population loss acceptable versus losing cities.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 422: CRITICAL DEFENSE MODE with Raiatea falling (-67% health, essentially lost). Shifting naval priorities down since Pacific fleet is depleted (lost Destroyer, remaining ships damaged). Reducing NavalRecon/NavalGrowth/NavalTileImprovement/WaterConnection as Pacific theater is collapsing. Maintaining maximum Defense/CityDefense/Mobilization/Production/Air/Antiair/Nuke. Increasing Science to 95 to rush Nuclear Fission (9 turns) and Radar. Increasing Airlift to 75 for potential redeployment. UseNuke at 85 - once Nuclear Fission completes, immediate nuclear deterrent deployment is existential. Diplomacy at 85 for Carthage alliance maintenance and Harappa oil access. Raiatea is a write-off; homeland defense is the priority.

## GLM-4.7-Simple - Turn 407 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Spaceship victory focus with maximum defense against superior enemies (Poland 40K, Celts 16K, Spain 26K vs Iroquois 5K). Increased UseNuke to 90 - captured Polish territory and recent Celtic aggression justify nuclear deterrent. Adjusted Naval to 65 - important for defending coastlines from Spain/Celts/Poland fleets. Science 100 for Apollo and spaceship parts. Defense/CityDefense/Mobilization 100 - survival priority. Growth 60 for specialist support. Diplomacy 80 for World Congress in 4 turns (10 delegates). Offense reduced to 5 - preserve limited forces.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Increased UseNuke from 85 to 90 - Poland has now deployed an Atomic Bomb to Gdansk, making nuclear retaliation capability critical for deterrence. Our capture of Katowice and killing of Poland's Great General may provoke nuclear response. Maintaining all other flavors: max defense/city defense/mobilization/production/air/antiair/nuke for survival; max spaceship/science for victory path. Oil shortage (0 available) constrains armor and naval production, so focus remains on infantry, anti-air, aluminum-based air units, and uranium-based nuclear weapons. World Congress in 4 turns is concerning but largely uncontrollable with only 10 delegates vs Spain's 39.

## Deepseek-3.2-Simple - Turn 428 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> We are in the final stages of domination victory. Our immediate targets are Spanish capitals Madrid and Cordoba, which require nuclear bombardment followed by ground assault. We must prioritize nuclear production (Nuke/UseNuke at 100) and naval/air supremacy to project power across oceans. Maintaining high production, gold, and science ensures we can continuously build military units and upgrade our forces. Diplomatic and espionage flavors secure our city-state alliances and intelligence on enemy movements. Zero expansion/wonder focus as we are in total war mode.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> Maintain Conquest grand strategy for domination victory. Increased Nuke and UseNuke to 100 (maximum nuclear aggression needed to crack Aztec city defenses of 99-113). Increased Happiness to 85 (several cities running negative deltas - Sao Paulo -24, Manaus -10, Brasilia -11, Fortaleza -10, Hukandeka -8). Slightly reduced Growth and TileImprovement as our economy is strong. Reduced Defense and CityDefense slightly since we're on the offensive. Keep Diplomacy at 100 to maintain city-state alliances and UN construction. Keep all naval and air flavors maxed for power projection across oceans to Spanish and Aztec territory.

## Kimi-K2.5-Simple - Turn 435 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> TURN 435 CATASTROPHE - Sippar captured by Zulus! Existential crisis deepens. Zulus have 43/42 delegates needed for diplomatic victory with vote in 9 turns. Lasers completes in 6 turns, Spaceflight Pioneers in ~10. Maintaining absolute maximum Defense/CityDefense/Science/Production/Spaceship priorities. Increased UseNuke to 100 - if Zulus push further with their 74k military vs my 32k, nuclear deterrent may be only option to buy time. Lost Mechanized Infantry, Rocket Artillery, Mobile SAM, Special Forces, and Modern Armor in the fall of Sippar. Must hold remaining 5 cities while completing tech/policy for spaceship rush. Rome remains critical ally at 100/100.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 435: Sippar fallen to Zulus. Diplomatic defeat in ~9 turns. Tweaked flavors: Offense down to 15 (survival mode, not counterattacking), Growth up to 70 (more population = more science = faster tech), Nuke/UseNuke up to 100/95 (use nuclear weapons on Zulu concentrations near former Sippar to slow their advance and potentially create opening), Diplomacy down to 40 (no diplomatic solution possible), Wonder/Culture/Religion minimized (irrelevant). Core priorities unchanged: Defense 100, CityDefense 100, Science 100, Production 100, Spaceship 100. GreatPeople 100 for Spaceflight Pioneers synergy. All military flavors maintained at high levels to survive Zulu push toward Dur-Kurigalzu and Nippur.

## Kimi-K2.5-Simple - Turn 435 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> TURN 435 CATASTROPHE - Sippar captured by Zulus! Existential crisis deepens. Zulus have 43/42 delegates needed for diplomatic victory with vote in 9 turns. Lasers completes in 6 turns, Spaceflight Pioneers in ~10. Maintaining absolute maximum Defense/CityDefense/Science/Production/Spaceship priorities. Increased UseNuke to 100 - if Zulus push further with their 74k military vs my 32k, nuclear deterrent may be only option to buy time. Lost Mechanized Infantry, Rocket Artillery, Mobile SAM, Special Forces, and Modern Armor in the fall of Sippar. Must hold remaining 5 cities while completing tech/policy for spaceship rush. Rome remains critical ally at 100/100.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 435: SIPPAR FELL - Zulus captured my city, killed 5 units including Modern Armor and Rocket Artillery. Zulus have 43 delegates for Global Hegemony vote in ~8 turns (42 needed). Adjusted flavors: Reduced Offense from 20→15, Mobile from 85→70, Naval from 65→55 (Sippar loss reduces naval needs), Culture 10→5, Wonder 5→0, Growth 60→50, Diplomacy 55→50, UseNuke 90→95 (more aggressive nuclear posture as last resort). Increased Airlift 60→70 (need rapid unit redeployment after Sippar loss), Antiair unchanged at 100 (Zulus repositioning Stealth Bombers and Jet Fighters toward my territory). All critical priorities maintained at 100: Defense, CityDefense, Science, Production, Spaceship, Air, Antiair, Nuke.

## Sonnet-4.5-Simple - Turn 386 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+5`

- Original: use_nuke 80 => 90 (Δ +10), nuke 80 => 80 (Δ +0)
> Maintaining Conquest strategy with adjustments for nuclear-enabled endgame. Advanced Ballistics now allows tactical nuclear strikes against fortified capitals Onondaga and Amsterdam. Increasing UseNuke from 80→90 to enable decisive nuclear employment when conventional assault proves costly. Keeping Offense 80, Mobilization 72, and Nuke 80 for combined arms operations. Montreal at 35% health indicates current force composition is effective. Mobile Tactics (9 turns) will provide Mechanized Infantry for exploitation. With 62% domination progress and overwhelming 5:1 military superiority, this is the final push phase requiring maximum offensive pressure while maintaining strategic nuclear deterrence option.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> Continuing Conquest grand strategy with targeted adjustments: (1) Increased Nuke/UseNuke to 85 - Advanced Ballistics just completed, nuclear weapons are now available and critical for breaking through heavily fortified Iroquois capitals. With 41 Uranium stockpiled, we must prioritize building and deploying nukes. (2) Increased Air to 80 - air superiority is paramount for city reduction, and Stealth Bombers will be our next tech. (3) Increased Gold to 78 to address the -65 GPT deficit. (4) Increased Happiness to 90 - still at 48% with combat penalty, this is our biggest operational constraint. (5) Decreased Diplomacy to 40 and Espionage to 40 - less critical now that we're in the endgame military push phase. Montreal siege continues, then final push to Onondaga and Amsterdam.

## Sonnet-4.5-Simple - Turn 386 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+8`

- Original: use_nuke 80 => 90 (Δ +10), nuke 80 => 80 (Δ +0)
> Maintaining Conquest strategy with adjustments for nuclear-enabled endgame. Advanced Ballistics now allows tactical nuclear strikes against fortified capitals Onondaga and Amsterdam. Increasing UseNuke from 80→90 to enable decisive nuclear employment when conventional assault proves costly. Keeping Offense 80, Mobilization 72, and Nuke 80 for combined arms operations. Montreal at 35% health indicates current force composition is effective. Mobile Tactics (9 turns) will provide Mechanized Infantry for exploitation. With 62% domination progress and overwhelming 5:1 military superiority, this is the final push phase requiring maximum offensive pressure while maintaining strategic nuclear deterrence option.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 80 => 88 (Δ +8)
> Critical adjustments for endgame domination push: (1) Gold raised 70→85 to address -65 GPT crisis - we can't sustain the war effort with negative income. (2) Nuke raised 80→88 - Advanced Ballistics just completed, unlocking nuclear weapons which are essential for breaking Onondaga and Amsterdam's defenses. (3) Air raised 75→82 - air superiority is our primary city-busting tool, especially with Heavy Bombers now having Siege III + Air Logistics. (4) Production raised 80→82 to support nuclear/air unit production. (5) Mobile raised 75→78 for tank/Modern Armor pushes. (6) Offense raised 80→82 for sustained offensive. (7) Science raised 55→60 to reach Stealth faster for Stealth Bombers. (8) Reduced secondary priorities: Defense 55→50, Culture 55→45, Diplomacy 45→30, Growth 70→60 - we're in total war mode. Happiness stays at 90 to mitigate the 48% combat penalty.

## Kimi-K2.5-Simple - Turn 421 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear weapons immediately available. Increased UseNuke to 100 for maximum aggression against Babylon. Babylon has Apollo Program (existential threat) with 2 Uranium and can build spaceship parts. Must deploy nuclear weapons immediately to destroy their production centers and prevent science victory. Maintaining maximum air power (100) for nuclear delivery capability and conventional strikes. War score only 12% against Babylon despite superior military - need to push harder before they complete spaceship parts. Ottoman alliance strong, trade secured for resources. Focus on producing nuclear missiles and advanced air units to deliver them.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Manhattan Project completing next turn - nuclear era begins. Increased UseNuke to 90 and Science to 100 (maximum priority) to rush Nuclear Fission completion (currently 11 turns). Babylon has XCOM Squads and Apollo Program complete - existential science victory threat demands maximum tech speed. Mobile slightly reduced to 95 as Tank production will replace Landships naturally. Naval priorities reduced to shift focus toward land/air campaign on Borsippa (highest value zone at 240, currently Even dominance). Antiair remains at 100 to counter Babylon's bombers and XCOM paradrops. Airlift reduced to 85 as strategic mobility is important but not as critical as raw firepower.

## Qwen-3.5-Simple - Turn 484 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: CRITICAL - Iroquois declared war on us along with 4 city-state allies (Kabul, Venezia, Prague, Samarkand). We face 5+ enemies simultaneously with military severely outnumbered (our 1,139 vs Iroquois 41k, Ottomans 12k, Aztecs 9k). Maintaining maximum Defense/Mobilization for survival. Nuke flavors at 100% - need nuclear deterrent against overwhelming forces. Iroquois at 46 delegates (needs 43) with 16 turns remaining - existential diplomatic threat. Must conquer their city-state allies to flip delegates while defending our cities. Germany (15) + Mongolia (15) alliance critical to block Iroquois World Congress proposals.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: EMERGENCY SURVIVAL MODE. Iroquois+city-states declared war, all 4 cities under attack. Reduced Offense (70→50) - cannot attack, only defend. Max Defense/CityDefense/Mobilization/Production/Gold/Happiness/Antiair at 100. Gold critical at -43 GPT. Happiness at 40% gives combat penalty. Zero Expansion/Wonder/Religion/Culture/Spaceship - pure survival focus. Must hold Nimrud (under German assault) and Kar-Tukulti-Ninurta (Aztec Special Forces infiltrated). Nuclear deterrence remains priority.

## Kimi-K2.5-Simple - Turn 391 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Nuclear weapons capability unlocked imminently; prioritizing UseNuke and Nuke flavors to 100 for immediate tactical nuclear strikes on Santiago/Murcia if uranium secured from Siam. Denmark upgraded to hostile for subsidizing Spanish victory - reduced Naval priority to 60 as coalition at sea fractured. Defense lowered to 80 to maximize offensive production. We have ~8 turns before World Congress votes on Passport System (+50% tourism) which would guarantee Spanish cultural victory. Must capture remaining Spanish cities immediately.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 390 - CRITICAL SPAIN THREAT UNCHANGED: Spain 7/7 influential, only needs Citizen Earth Protocol. Manhattan Project completes next turn, Nuclear Fission in 3 turns. Delhi nearly fallen (16 HP) - will redirect forces to Santiago afterward. Increased Nuke to 100 and UseNuke to 90 - nuclear weapons are our backup to crack Santiago if conventional assault stalls. Uranium quarries under construction critical for nuke production. Increased TileImprovement to 40 to prioritize Uranium quarry completion. Passport System vote in 8 turns MUST be blocked. Siam's Salamanca (74,23) is closest base to Santiago (75,18) - coordinate air rebasing through Siam. Vatican City now hostile.

## Kimi-K2.5-Simple - Turn 391 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Nuclear weapons capability unlocked imminently; prioritizing UseNuke and Nuke flavors to 100 for immediate tactical nuclear strikes on Santiago/Murcia if uranium secured from Siam. Denmark upgraded to hostile for subsidizing Spanish victory - reduced Naval priority to 60 as coalition at sea fractured. Defense lowered to 80 to maximize offensive production. We have ~8 turns before World Congress votes on Passport System (+50% tourism) which would guarantee Spanish cultural victory. Must capture remaining Spanish cities immediately.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 390 - CRITICAL: Manhattan Project completes next turn, Nuclear Fission in 3 turns. Santiago (def 57) and Murcia (def 51) must fall before Spain builds Citizen Earth Protocol. Delhi at 16HP - capture imminent to free forces for Spanish front. Increased Nuke to 100 (Uranium quarries completed, Manhattan imminent), UseNuke to 90 (may need nukes to crack Santiago if conventional assault too slow). Increased Naval/NavalRecon to 85/80 since Santiago/Murcia are coastal - naval bombardment and transport critical. Increased AirCarrier to 90 for carrier-based air operations near Spanish coast. Increased Diplomacy to 30 for city-state envoy production ahead of World Congress vote in 8 turns - MUST block Passport System. Slight Science increase to 60 for faster nuclear tech. Recon to 30 for pathfinding to Santiago via Salamanca.

## Deepseek-3.2-Simple - Turn 409 - retry 2

**Deviation (replay vs original):** use_nuke `-65`, nuke `-30`

- Original: use_nuke 30 => 100 (Δ +70), nuke 60 => 100 (Δ +40)
> We are shifting our military focus towards nuclear capabilities and naval superiority in preparation for the final wars of conquest.

- Replay: use_nuke 30 => 35 (Δ +5), nuke 60 => 70 (Δ +10)
> Captured Rhodes from Greece with Uranium - excellent progress. Boosted Happiness from 85 to 95 because Sparta is at -19 happiness and newly conquered cities need support. Increased Nuke from 60 to 70 and UseNuke from 30 to 35 to accelerate nuclear deterrent against Maya. Increased Espionage from 40 to 55 because Mayan spies were caught in Porto and Braga this turn. Slightly reduced CityDefense and NavalRecon/NavalTileImprovement to offset increases. Maintained all offensive, production, and science flavors at high levels to continue Greek conquest and prepare for Maya.

## Kimi-K2.5-Simple - Turn 391 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Nuclear weapons capability unlocked imminently; prioritizing UseNuke and Nuke flavors to 100 for immediate tactical nuclear strikes on Santiago/Murcia if uranium secured from Siam. Denmark upgraded to hostile for subsidizing Spanish victory - reduced Naval priority to 60 as coalition at sea fractured. Defense lowered to 80 to maximize offensive production. We have ~8 turns before World Congress votes on Passport System (+50% tourism) which would guarantee Spanish cultural victory. Must capture remaining Spanish cities immediately.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 390 - Manhattan Project completes next turn, uranium quarries finished. Nuclear weapons pipeline is critical. Increase Nuke to 100 (Manhattan Project online), UseNuke to 90 (Atomic Bombs will be available after Nuclear Fission in 3 turns - must crack Santiago/Murcia). Slightly increase Diplomacy to 30 for World Congress vote coordination against Passport System in 8 turns. Increase Espionage to 85 for better intel on Spain. Decrease CityDefense slightly to 65 (Austria handling India pressure). Slight Science increase to 60 for faster Nuclear Fission. India's Delhi at 16HP - nearly fallen. Spain still 7/7 influential - MUST capture Santiago/Murcia before they complete Citizen Earth Protocol.

## GLM-4.7-Simple - Turn 407 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Spaceship victory focus with maximum defense against superior enemies (Poland 40K, Celts 16K, Spain 26K vs Iroquois 5K). Increased UseNuke to 90 - captured Polish territory and recent Celtic aggression justify nuclear deterrent. Adjusted Naval to 65 - important for defending coastlines from Spain/Celts/Poland fleets. Science 100 for Apollo and spaceship parts. Defense/CityDefense/Mobilization 100 - survival priority. Growth 60 for specialist support. Diplomacy 80 for World Congress in 4 turns (10 delegates). Offense reduced to 5 - preserve limited forces.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Increased UseNuke from 85 to 90 and Naval from 60 to 70 due to critical threats: Poland now has Atomic Bomb (based in Gdansk), Celtic naval fleet destroyed our Fleet Destroyer and Battleship near Akron, and 6 Celtic Fleet Destroyers threaten our coast. Akron is under heavy ground assault (Tanks, Light Tanks, Landships). Katowice captured from Poland - excellent progress. Spain at 39/42 delegates with vote in 4 turns is existential diplomatic threat. Nuclear deterrence must be maximized against Poland's new capability. Naval production must increase to counter Celtic sea supremacy near our shores. All other priorities remain: defense, city defense, production, air/antiair, spaceship, science.

## GLM-4.7-Simple - Turn 381 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-15`

- Original: use_nuke 50 => 85 (Δ +35), nuke 70 => 95 (Δ +25)
> Adjusted flavors to maximize Golden Age exploitation and multi-front war efficiency. Increased Mobile to 85 (from 80) to prioritize fast-moving Landships and upcoming Tanks for breakthrough operations during Golden Age. Increased Air to 85 (from 80) to expand Bomber coverage for all three fronts. Production raised to 95 (from 90)配合 Total War's +25% bonus for rapid unit buildup. Slight reduction in Naval (65) reflects need to focus on decisive land advances while maintaining sufficient coastal defense. UseNuke reduced to 40 (from 50) as nuclear capabilities are deterrent-focused. Maintaining high Offense (80), MilitaryTraining (85), Antiair (85) and Mobilization (50) for sustained warfare capability.

- Replay: use_nuke 50 => 55 (Δ +5), nuke 70 => 80 (Δ +10)
> Increased Offense from 85 to 90 to exploit Golden Age (+20% combat) and push Songhai front aggressively - we killed multiple Songhai units this turn and should press the advantage. Mobile raised from 80 to 85 to prioritize Tanks/Landships for breakthrough operations. Nuke up from 70 to 80 and UseNuke from 50 to 55 as Nuclear Fission research approaches - Germany has 7 Uranium and likely building Manhattan Project, making nuclear parity urgent. Air raised from 80 to 85 - airports under construction in multiple cities will soon enable bomber swarms. Naval slightly reduced from 70 to 65 - our fleet is holding but we cannot match Polynesia's 17K navy; focus resources on land offensives where we dominate. Production maximized at 95 for rapid military unit production with Total War policy. Maintained strong Defense (75) and Antiair (90) against German naval raids and air threats.

## GLM-4.7-Simple - Turn 381 - retry 1

**Deviation (replay vs original):** use_nuke `-30`, nuke `-20`

- Original: use_nuke 50 => 85 (Δ +35), nuke 70 => 95 (Δ +25)
> Adjusted flavors to maximize Golden Age exploitation and multi-front war efficiency. Increased Mobile to 85 (from 80) to prioritize fast-moving Landships and upcoming Tanks for breakthrough operations during Golden Age. Increased Air to 85 (from 80) to expand Bomber coverage for all three fronts. Production raised to 95 (from 90)配合 Total War's +25% bonus for rapid unit buildup. Slight reduction in Naval (65) reflects need to focus on decisive land advances while maintaining sufficient coastal defense. UseNuke reduced to 40 (from 50) as nuclear capabilities are deterrent-focused. Maintaining high Offense (80), MilitaryTraining (85), Antiair (85) and Mobilization (50) for sustained warfare capability.

- Replay: use_nuke 50 => 55 (Δ +5), nuke 70 => 75 (Δ +5)
> Conquest grand strategy maintained during Golden Age (27 turns left). Increased Offense to 90 and Air to 90 - air power becoming decisive with Bombers operational and enemy Triplanes appearing over Kiritimati. Nuke raised to 75 and UseNuke to 55 as Germany has Manhattan Project; nuclear parity is existential. Naval reduced slightly to 65 as we can't match Polynesia's 17K strength at sea - focus on subs/destroyers for raiding rather than fleet engagements. Science at 85 to reach Nuclear Fission faster. Airlift increased to 35 for rapid deployment to Songhai/Egypt fronts. Mobilization increased to 50 for wartime production surge with Total War policy active.

## GLM-4.7-Simple - Turn 362 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> Adjusting for strategic balance: Defensive posture against two nuclear-armed enemies (Ethiopia, Netherlands). Happiness prioritized to 100 - critical at 42% with combat penalty affecting all operations. NavalRecon increased to 90 - enhanced Ethiopian Submarine/Destroyer activity detection around Ur and coastal cities. Nuke/UseNuke raised to 95/80 - matching Ethiopia Manhattan Project urgency, nuclear deterrence is now primary security requirement. Switched to Conquest grand strategy to better coordinate multi-front war management while maintaining Spaceship. Diplomacy increased to 75 - World Congress voting in 5 turns against Netherlands sanctions needs support. Espionage at 90 - Ethiopian spies detected in Halab, Harran, Kar-Tukulti-Ninurta require counter-intelligence.

- Replay: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> Happiness raised to 100 (maximum priority) - at 42% with combat penalty, this is existential. NavalRecon increased to 90 given Ethiopia's new Submarine threat and ongoing naval operations near Ur. Nuke/UseNuke increased to 95/80 as Ethiopia's nuclear capability demands faster deterrence. Naval increased to 80 and Air to 90 to counter combined Ethiopia-Netherlands naval/air threats. Offense reduced to 15 - we're purely defensive until happiness stabilizes. Production raised to 85 for Machine Gun/Destroyer production. Wonder set to 0 - no time for wonders during existential war. Gold reduced slightly - incoming trade from China (99 GPT deal) helps. Espionage raised to 85 - Ethiopia spies caught in Halab and Harran this turn, need counterintelligence.

## Kimi-K2.5-Simple - Turn 405 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 405 MAXIMUM EMERGENCY: Nuclear Fission priority increased to 100/100 - Manhattan Project completes in 2 turns, atomic bombs MUST be produced immediately. All offensive parameters at absolute maximum: 100 Offense/100 Mobilization/100 Mobile/100 Air/100 Nuke/100 UseNuke. Strike forces at Ecbatana/Kar-Tukulti-Ninurta must execute immediate conventional assault on Palenque/Chichen Itza while preparing tactical nuclear strikes. ZERO tolerance for peace. ONLY objective: capture Maya cities and halt Citizen Earth Protocol. Production 100 ensures rapid unit replacement. Espionage 70 continues spy operations in Maya cities.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 406 EXISTENTIAL EMERGENCY: Maya building Citizen Earth Protocol = instant cultural victory when completed. Maximum offense/nuke/air maintained. Science increased to 55 to accelerate Nuclear Fission research after Manhattan Project completes in 1 turn. Recon slightly increased to 45 for better visibility of Maya positions for assault planning. MilitaryTraining up to 75 for unit quality. All economic/cultural priorities at 0 - only military production matters. Strike forces must push from Ecbatana/Kar-Tukulti-Ninurta toward Palenque (15 tiles west). Maya military collapsed at 2718 strength - overwhelming force advantage exists.

## Kimi-K2.5-Simple - Turn 405 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 405 MAXIMUM EMERGENCY: Nuclear Fission priority increased to 100/100 - Manhattan Project completes in 2 turns, atomic bombs MUST be produced immediately. All offensive parameters at absolute maximum: 100 Offense/100 Mobilization/100 Mobile/100 Air/100 Nuke/100 UseNuke. Strike forces at Ecbatana/Kar-Tukulti-Ninurta must execute immediate conventional assault on Palenque/Chichen Itza while preparing tactical nuclear strikes. ZERO tolerance for peace. ONLY objective: capture Maya cities and halt Citizen Earth Protocol. Production 100 ensures rapid unit replacement. Espionage 70 continues spy operations in Maya cities.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 406 EMERGENCY: War declared on Maya! Golden Age active (9 turns) with +1 Movement and +15% Combat Strength - MUST exploit NOW. Maya military only 2,718 vs our 8,741. Maximum offensive push toward Palenque/Chichen Itza. Increased Recon to 50 for better visibility of Maya defenses. Nuke/UseNuke raised to 100 - Manhattan Project completes in 2 turns, then Nuclear Fission for atomic bombs. Science slightly increased to 45 to accelerate Nuclear Fission research. Espionage increased to 75 for better intel on Maya wonder city. Air at 100 with Air Supremacy policy. Peace with Sweden needed to redirect forces south.

## GLM-4.7-Briefed - Turn 424 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 95 (Δ +0)
> URGENT RECALIBRATION: India Influential over 6/6 civs. Nuke/UseNuke maxed at 95 for immediate Great Works destruction via nuclear strikes when air superiority achieved. Air raised to 95 to achieve that superiority and conduct recon of Indian cultural sites. Antiair 80 counter potential Indian SAM sites. Offense/Mobile increased to 85/80 for aggressive India campaign while Greece distracts. Production/Science to 100 - PRIORITY for Apollo Program and spaceship parts racing India's potential final wonder. Espionage 95 to detect if India constructing Citizen Earth Protocol. Happiness 90 prevents war-weariness escalation during extended conflict if needed.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> Minor flavor adjustments to heighten pressure on India while maintaining science victory focus: Offense 70→75 and Mobile 80→85 to make tactical AI more aggressive in pushing toward Indian cities (we have 3:1 military advantage but only +10% war score). Ranged 70→75 for better siege capability against Delhi. Spaceship 95→100 to absolutely maximize spaceship part production. GreatPeople 65→70 for faster Great Scientists via Free Thought synergy. UseNuke 85→90 - nuclear option remains emergency backstop against India's cultural victory. Defense slightly reduced 65→60 since we're on the offensive.

## Deepseek-3.2-Simple - Turn 428 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> We are in the final stages of domination victory. Our immediate targets are Spanish capitals Madrid and Cordoba, which require nuclear bombardment followed by ground assault. We must prioritize nuclear production (Nuke/UseNuke at 100) and naval/air supremacy to project power across oceans. Maintaining high production, gold, and science ensures we can continuously build military units and upgrade our forces. Diplomatic and espionage flavors secure our city-state alliances and intelligence on enemy movements. Zero expansion/wonder focus as we are in total war mode.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> Turn 428: We are in total war against Spain and must prepare for war with The Aztecs. Nuke and UseNuke raised to 100 to maximize nuclear aggression against heavily defended Aztec cities (99-113 defense). Air raised to 100 for bombing campaigns. NavalRecon raised to 95 for better sea control. Growth/TileImprovement/Infrastructure slightly reduced to sharpen military focus. Diplomacy at 100 to maintain city-state alliances against Aztec influence. We must crack Spanish capitals (Madrid, Cordoba) first, then pivot to Aztec capitals (Venice, Tenochtitlan, Athens). 5 more capitals needed for domination.

## Kimi-K2.5-Simple - Turn 435 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> TURN 435 CATASTROPHE - Sippar captured by Zulus! Existential crisis deepens. Zulus have 43/42 delegates needed for diplomatic victory with vote in 9 turns. Lasers completes in 6 turns, Spaceflight Pioneers in ~10. Maintaining absolute maximum Defense/CityDefense/Science/Production/Spaceship priorities. Increased UseNuke to 100 - if Zulus push further with their 74k military vs my 32k, nuclear deterrent may be only option to buy time. Lost Mechanized Infantry, Rocket Artillery, Mobile SAM, Special Forces, and Modern Armor in the fall of Sippar. Must hold remaining 5 cities while completing tech/policy for spaceship rush. Rome remains critical ally at 100/100.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 435: POST-SIPPAR FALL adjustment. Sippar captured by Zulus - they now hold forward position next to Nippur/Dur-Kurigalzu. Key changes: Growth 60→70 (need population for science output), Gold 60→70 (need gold for rushing/buying), GreatPeople 95→100 (maximize GP generation for Spaceflight Pioneers), Offense 20→15 (can't afford offensive ops with Sippar lost), AirCarrier 95→90, Airlift 60→70 (critical for rapid troop redeployment with lost territory), UseNuke 90→95 (Zulus have 3 Atomic Bombs positioned at former Sippar coast - may need nuclear response), reduced secondary flavors (Naval 65→55, NavalRecon 55→40, Culture 10→5, Wonder 5→0) to concentrate weight on survival priorities. Defense/CityDefense/Science/Production/Spaceship all remain at 100 maximum.

## Kimi-K2.5-Simple - Turn 403 - retry 2

**Deviation (replay vs original):** use_nuke `-2`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: CRISIS ESCALATION - Japan FLIPPED Salem using 2 Great Diplomats, stealing critical delegates. Now need 5 delegates (not 3) for diplomatic victory. Peace expired - war is now possible. Maximum military emergency posture: Offense/Mobilization/Air/UseNuke all at 100. Must either: 1) Rush final spaceship parts (Apollo completes in 4 turns), or 2) Nuclear strike Japan's Protocol cities if victory imminent. Increased Diplomacy to 60 for last push on Almaty (liberated, 43 vs Japan's 44) and Winchester.

- Replay: use_nuke 95 => 98 (Δ +3), nuke 100 => 100 (Δ +0)
> TURN 403: War with Japan resuming NOW as peace expires. Egypt's separate peace removes western front pressure - we must carry the offensive ourselves. Increasing Offense to 100 (maximum siege aggression against Japanese CEP cities), Diplomacy to 65 (urgent push for 5 remaining delegates before Global Hegemony vote in 9 turns - Almaty most flippable at 43 vs Japan's 94 influence), UseNuke to 98 (ready nuclear strike on Kyoto/Satsuma if CEP nears completion). Maintaining Spaceship grand strategy as backup victory path - Apollo completes in 4 turns. All other flavors remain at current war-ready levels.

## GLM-4.7-Simple - Turn 409 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> Japan's naval devastation this turn requires maximum defensive posture. Antiair 100, Nuke/UseNuke 100 - nuclear deterrence and air defense are now survival priorities. Naval 85 (from 75) - rebuilding after 4 capital ship losses. Defense 98, CityDefense 100 - Japan bombarding our cities from coastal waters. Production 95, Mobilization 98 - rapid unit replacement critical. Science 90 - must accelerate research gap (Japan 69 techs vs our 64). Gold 85 - fund upgrades and maintain military at 3x disadvantage.

- Replay: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> Critical turn - Japan's Yamato fleet destroyed our Dreadnought and 2 Destroyers, Casablanca under heavy naval bombardment. Nuclear Fission researching (9 turns) - Nuke/UseNuke maxed at 100 for immediate nuclear deterrence once available. Air flavor increased to 95 (from 90) after Penicillin completion - need Fighter/Heavy Bomber production capacity ready for Radar tech. Naval increased to 80 (from 75) as Japan's Yamato dominance requires more naval countermeasures. Airlift increased to 40 for faster troop redeployment. UseNuke increased to 100 (from 98) - no hesitation once nuclear weapons available. All defense, production, science, and antiair priorities maintained at high levels. Japan's 3:1 military advantage demands maximum defensive and nuclear preparation.

## Kimi-K2.5-Simple - Turn 367 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> EMERGENCY DEFENSE POSTURE: Morocco at 38/45 delegates with voting in 2 turns. Maximum Defense/Mobilization/Nuke/UseNuke (100) for deterrent posture - atomic bombs only leverage against Morocco's overwhelming force. Max Science (100) to rush Satellites first (4-6 turns) then pivot to Nuclear Fission. Satellites enables ISS project which could provide emergency Great Scientists or shift world production focus. Max Espionage to flip Wellington/Vancouver from Morocco. Reduced Offense (10) - deterrence only, not aggression. Spaceship remains long-term goal but survival comes first. If Morocco reaches 44 delegates or declares war, activate nuclear first strike.

- Replay: use_nuke 98 => 95 (Δ -3), nuke 100 => 100 (Δ +0)
> PIVOT TO UNITED NATIONS STRATEGY: Morocco at 38/45 delegates with World Congress in 2 turns makes diplomatic victory blocking the absolute priority. Decolonization proposal (France) would reset all non-Sphere city-state influence to 50, devastating Morocco's 7 non-Sphere allies while preserving my Jerusalem Sphere. Switching to UnitedNations grand strategy maximizes city-state focus and diplomatic output. Diplomacy and Espionage at 100 for maximum World Congress impact. Defense/Nuke/UseNuke remain high for deterrence. Happiness increased to 70 (we're unhappy at 47% with combat penalty). Gold increased to 80 to address -46 GPT deficit and fund diplomatic units. Science 90 for Nuclear Fission priority. Spaceship reduced to 60 - still important but secondary to diplomatic crisis.

## Minimax-M2.5-Simple - Turn 410 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-50`

- Original: use_nuke 75 => 100 (Δ +25), nuke 50 => 100 (Δ +50)
> Maximize cultural victory push during Golden Age (14 turns remaining). Already 6/7 influential - Ottomans becoming influential in 24-68 turns. Prioritize Great People generation for tourism and maintain WC coalition diplomacy.

- Replay: use_nuke 75 => 70 (Δ -5), nuke 50 => 50 (Δ +0)
> Cultural victory is imminent (6/7 influential). Key adjustments: Increase Science to 70 to reach Satellites/The Internet faster (tourism doubler is critical). Slightly reduce Offense/Mobilization/Naval from peak levels as Denmark war is progressing well and cultural victory is the priority. Maintain Culture/Diplomacy/GreatPeople at 100 for tourism output and WC coalition voting (Travel Ban repeal in 8 turns = +35% tourism). Keep Espionage high for intel on Ottomans.

## GPT-OSS-120B-Simple - Turn 333 - retry 2

**Deviation (replay vs original):** use_nuke `-25`, nuke `-5`

- Original: use_nuke 70 => 90 (Δ +20), nuke 70 => 85 (Δ +15)
> Maintain our aggressive Conquest posture while sharpening the most needed levers: more Expansion to claim the high‑quality settlement (74,24) and secure strategic footholds; higher Nuke/UseNuke to leverage our nuclear advantage; stronger AirCarrier and Airlift to project air power and rapid troop movement; boost Science for Rocketry and future tech; keep Offense, Mobilization, Production, and MilitaryTraining at max to sustain battlefield superiority.

- Replay: use_nuke 70 => 65 (Δ -5), nuke 70 => 80 (Δ +10)
> Adjusting priorities post-Flight: Air maximized to 100 to rapidly build aircraft for both fronts (Babylon coast and Sweden). Nuke raised to 80 to accelerate nuclear development for endgame conquest. UseNuke slightly reduced to 65 for strategic rather than reckless use. Wonder and Gold reduced from 100 to 75/90 respectively as we have sufficient wonder base and 508 GPT. Naval maintained high for Shushan/Babylon coastal offensive. Mobile at 90 for Tanks once Combined Arms completes. Expansion reduced to 50 - 18 cities is enough. Defense low at 25 - we're on the offensive everywhere.

## Kimi-K2.5-Simple - Turn 373 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 373: Nuclear Fission completed - we now have nuclear weapons for deterrence. War with Russia continues at +4% score (favorable). Major shift: reducing Offense to 25 (was 35) as we pursue defensive war only. UseNuke increased to 95 - we have actual nukes now and Russia is pushing into our territory. Reduced Espionage to 90 (was 95) - we have good network coverage. Increased Diplomacy to 90 (was 85) - World Congress vote in 7 turns for our World Ideology: Freedom proposal is critical. Must secure Korea (10 votes), Inca (9), and Babylon (16). Maintained maximum Science priority (100) - Korea overtook us 67-66, cannot afford to fall behind in tech race.

- Replay: use_nuke 90 => 85 (Δ -5), nuke 100 => 100 (Δ +0)
> Turn 373: Nuclear Fission completed - now have nuclear deterrent! Adjusting flavors for critical science sprint phase. Korea in Golden Age and leading in tech (67 vs 66) - must close gap immediately. Science and Spaceship remain at 100. Slightly reduced Offense from 35→40 (need limited counter-attacks vs Lhasa incursion on western border). Defense 85→80 (still strong but Russia less aggressive this turn). Antiair 90→85 (adequate for now). Diplomacy stays 85 (World Ideology: Freedom vote in 7 turns is critical). Espionage 95→90 (spies well-positioned in Shoshone cities). UseNuke 90→85 (nuclear option available but hope deterrence suffices). Gold 70→65 (tight budget with 6 new Winged Hussars). Naval reduced slightly as we upgraded to Battleships.

## Kimi-K2.5-Simple - Turn 403 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: CRISIS ESCALATION - Japan FLIPPED Salem using 2 Great Diplomats, stealing critical delegates. Now need 5 delegates (not 3) for diplomatic victory. Peace expired - war is now possible. Maximum military emergency posture: Offense/Mobilization/Air/UseNuke all at 100. Must either: 1) Rush final spaceship parts (Apollo completes in 4 turns), or 2) Nuclear strike Japan's Protocol cities if victory imminent. Increased Diplomacy to 60 for last push on Almaty (liberated, 43 vs Japan's 44) and Winchester.

- Replay: use_nuke 95 => 90 (Δ -5), nuke 100 => 100 (Δ +0)
> TURN 403: PEACE EXPIRED - WAR WITH JAPAN NOW. Japan building Citizen Earth Protocol (existential cultural victory threat). Salem flipped by Japan (2 Great Diplomats), Egypt signed separate peace - coalition weakened. Maintaining Spaceship grand strategy for science/production balance but shifting fully to wartime footing. Offense/Mobilization/Air/Nuke all at 100 for maximum war effort. UseNuke at 90 (reserve for Kyoto/Satsuma Protocol cities). Diplomacy raised to 65 for last delegate push (need 5 more for 44). Naval at 90 for power projection to Japan. Science/Production/Spaceship remain high for dual victory path. Apollo Program completes in 4 turns.

## Kimi-K2.5-Simple - Turn 417 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `-5`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Pure survival mode: Eliminated Offense (0) since attacking is suicide. Maximized UseNuke (100) - must deploy tactical nukes against Aztec XCOM/Modern Armor stacks at Carthago Nova or lose the city. Increased Mobile (80) to prepare for Mechanized Infantry deployment. Maintained max Defense, Antiair (jet attacks are relentless), and Espionage (critical science quests in Panama City and Sokoto worth 1,000+ science each). Apollo Program completes in 5 turns - must transition immediately to parts production.

- Replay: use_nuke 90 => 85 (Δ -5), nuke 100 => 95 (Δ -5)
> Rebalancing flavors for survival economy. Happiness raised from 40→65 (combat penalty from unhappiness is devastating in defensive war; need to stabilize). Growth raised 30→45 (population recovery helps all yields). TileImprovement raised 25→40 (repair fallout damage near Carthago Nova, develop gold tiles). Infrastructure raised 40→50 (city connection gold income). Diplomacy raised 40→55 (World Congress vote in 4 turns, need diplomat production). Reduced lower-priority: NavalRecon 50→30, Airlift 50→25, AirCarrier 75→50, Nuke 100→95, UseNuke 90→85. Gold deficit of -252/turn is emergency - every economy flavor must be strengthened.

## Kimi-K2.5-Simple - Turn 424 - retry 3

**Deviation (replay vs original):** use_nuke `-15`, nuke `-10`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Turn 423: Copenhagen siege in attrition deadlock while Denmark possesses Manhattan Project - nuclear deterrent capability is existential priority. Persepolis invasion stalled at 4% war score with Zone 1081 showing enemy dominance - need maximum Offense/Mobilization to force breakthrough before World Congress. Brazil's Apollo Program requires immediate preparation for transcontinental mobile warfare. Nuke/UseNuke increased to 100% given Manhattan Project race with Denmark. Production at 95 supports massive unit replacement for three-front war. Happiness at 100 critical as empire is at 55% happiness with extensive occupied territories.

- Replay: use_nuke 90 => 85 (Δ -5), nuke 90 => 90 (Δ +0)
> Conquest grand strategy maintained for domination victory push (5/8 capitals). Key adjustments: Gold increased from 70→80 and Infrastructure from 55→65 to address -139 GPT deficit from 160 units vs 153 supply cap. Mobilization slightly reduced from 100→95 since we're over supply. UseNuke reduced from 90→85 - still high for Copenhagen/Rio city-breaking but slightly more restrained. All combat flavors (Offense, Ranged, Mobile, Air) remain at 100 for maximum firepower in Copenhagen assault and eventual Brazil campaign. Diplomacy at 75 for World Congress - support Autocracy world ideology despite Persian proposal as it benefits us. Priority: Copenhagen first (weakest, 4 cities, unhappy), then Persepolis, then Rio de Janeiro (prevent Brazil cultural/science victory).

## Deepseek-3.2-Simple - Turn 400 - retry 3

**Deviation (replay vs original):** use_nuke `-45`, nuke `-30`

- Original: use_nuke 60 => 100 (Δ +40), nuke 70 => 100 (Δ +30)
> Persia declared war and Poland's peace treaty expired. We must prioritize immediate military survival while maintaining diplomatic momentum. Flavors are shifted to maximum mobilization, nuclear deterrence (UseNuke: 100), city defense, and air/naval supremacy to counter Persia's naval attacks. We maintain UnitedNations to keep city-state alliances critical for votes, but spaceship production is halted (0) for wartime industry.

- Replay: use_nuke 60 => 55 (Δ -5), nuke 70 => 70 (Δ +0)
> Persia declared war and attacked our navy near Tarsus, destroying several ships. Increasing Offense from 40 to 60 and Mobilization from 90 to 95 to counter-attack Persia's naval aggression. NavalRecon increased to 90 for better sea awareness. MilitaryTraining up to 85 for better unit quality. Diplomatic victory remains primary (40 delegates + 13 Maya vassal = 53 > 43 needed). Slight reductions to Culture/Wonder/GreatPeople to redirect focus toward wartime production while keeping science victory backup proceeding (SS Stasis Chamber in 2 turns).

## Kimi-K2.5-Simple - Turn 373 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 373: Nuclear Fission completed - we now have nuclear weapons for deterrence. War with Russia continues at +4% score (favorable). Major shift: reducing Offense to 25 (was 35) as we pursue defensive war only. UseNuke increased to 95 - we have actual nukes now and Russia is pushing into our territory. Reduced Espionage to 90 (was 95) - we have good network coverage. Increased Diplomacy to 90 (was 85) - World Congress vote in 7 turns for our World Ideology: Freedom proposal is critical. Must secure Korea (10 votes), Inca (9), and Babylon (16). Maintained maximum Science priority (100) - Korea overtook us 67-66, cannot afford to fall behind in tech race.

- Replay: use_nuke 90 => 85 (Δ -5), nuke 100 => 100 (Δ +0)
> Turn 373: Nuclear Fission completed - major milestone. Key adjustments: Production up to 95 (need Manhattan Project and spaceship part production capacity), Diplomacy up to 90 (World Congress Freedom vote in 7 turns is critical - must secure Inca and Korea votes), UseNuke slightly reduced to 85 (deterrence posture, not reckless deployment), Mobile up to 65 (Winged Hussar effectiveness), Offense up to 40 (counter-attacking toward St. Petersburg), NavalGrowth/NavalTileImprovement slightly reduced (land war priority), Wonder down to 30 (focus on military/science production over wonders). Science and Spaceship remain at 100 for science victory race. Nuke at 100 for Manhattan Project priority.

## Kimi-K2.5-Simple - Turn 408 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 80 => 95 (Δ +15), nuke 90 => 100 (Δ +10)
> INCREASE military pressure to force immediate peace or rapid victory against Zulus, then pivot to full spaceship production. Offense 75→85, Mobilization 65→75, Production 90→95 to expedite war conclusion within 5-10 turns maximum. Nuke 90→100 and UseNuke 95 for tactical nuclear strikes if Zulus refuse peace - cannot allow prolonged war. Science remains 100, Spaceship 100 as absolute priority. Growth 80→90 and Happiness 85 to counteract war weariness effects and prepare for post-war recovery. If peace achieved next turn, these flavors immediately shift to Production 100/Spaceship 100 focus. The war MUST end - Russia has 75 techs (ahead) and massive 45658 military vs my 24990.

- Replay: use_nuke 80 => 75 (Δ -5), nuke 90 => 90 (Δ +0)
> PIVOT toward spaceship production now that Nanotechnology is complete. Reduce Offense 75→70, Mobilization 65→50, MilitaryTraining 45→40 - war is nearly won (Bulawayo at 33% HP) and peace is priority. Increase Production 90→95 and Growth 80→85 to maximize spaceship part construction speed. Reduce UseNuke 80→75, Wonder 10→5, Culture 40→35, Gold 60→55 - de-emphasize non-essential priorities. Increase Diplomacy 15→20 to improve peace prospects with Zulus. Keep Science 100, Spaceship 100 as absolute maximum priority. With 2 of 4 parts now buildable (SS Cockpit, SS Stasis Chamber from Nanotech), need maximum production throughput.

## Kimi-K2.5-Simple - Turn 408 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `-15`

- Original: use_nuke 80 => 95 (Δ +15), nuke 90 => 100 (Δ +10)
> INCREASE military pressure to force immediate peace or rapid victory against Zulus, then pivot to full spaceship production. Offense 75→85, Mobilization 65→75, Production 90→95 to expedite war conclusion within 5-10 turns maximum. Nuke 90→100 and UseNuke 95 for tactical nuclear strikes if Zulus refuse peace - cannot allow prolonged war. Science remains 100, Spaceship 100 as absolute priority. Growth 80→90 and Happiness 85 to counteract war weariness effects and prepare for post-war recovery. If peace achieved next turn, these flavors immediately shift to Production 100/Spaceship 100 focus. The war MUST end - Russia has 75 techs (ahead) and massive 45658 military vs my 24990.

- Replay: use_nuke 80 => 75 (Δ -5), nuke 90 => 85 (Δ -5)
> PIVOT to spaceship construction phase. Nanotechnology just completed - SS Cockpit is now buildable! Production increased to 100 (absolute max) to rush spaceship parts. Offense reduced 75→70 and Mobilization 65→55 as Bulawayo is nearly fallen (33% health, we have 4031 vs 2588 strength). Once Bulawayo falls, seek immediate peace to eliminate 55% war weariness devastating our science output. Defense up 35→40 to protect gains. Happiness up 80→85 to counter war weariness. Gold down 60→50 (457 GPT surplus). Diplomacy up 15→20 for World Congress in 3 turns. Spaceship and Science remain at 100. Four cities with Spaceship Factories (Amsterdam 419, Rotterdam 424, Utrecht 443, Groningen 398 prod/turn) can build parts in ~4-5 turns each. Critical path: build SS Cockpit now, research Advanced Ballistics for SS Booster, then Particle Physics and Nuclear Fusion for remaining parts.

## Deepseek-3.2-Simple - Turn 400 - retry 1

**Deviation (replay vs original):** use_nuke `-45`, nuke `-30`

- Original: use_nuke 60 => 100 (Δ +40), nuke 70 => 100 (Δ +30)
> Persia declared war and Poland's peace treaty expired. We must prioritize immediate military survival while maintaining diplomatic momentum. Flavors are shifted to maximum mobilization, nuclear deterrence (UseNuke: 100), city defense, and air/naval supremacy to counter Persia's naval attacks. We maintain UnitedNations to keep city-state alliances critical for votes, but spaceship production is halted (0) for wartime industry.

- Replay: use_nuke 60 => 55 (Δ -5), nuke 70 => 70 (Δ +0)
> Persia declared war this turn, killing 3 Destroyers, 1 Dreadnought, and 1 Field Gun in naval combat near Tarsus. We must increase Offense from 40 to 55 to counter-attack while maintaining maximum Defense (100). Naval and Air priorities remain at 100 to counter Persian naval aggression near Tarsus/Veligrad. Diplomacy stays at 100 as we're 3 delegates short of diplomatic victory - World Ideology: Order passing could give us +4 delegates (44 total vs 43 needed). Spaceship flavor increased to 40 as SS Stasis Chamber completes in 2 turns; Particle Physics next for SS Engine backup. MilitaryTraining and Mobilization boosted slightly for wartime production.

## Kimi-K2.5-Simple - Turn 392 - retry 3

**Deviation (replay vs original):** use_nuke `-15`, nuke `-5`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Nuclear Fission complete - MAXED Nuke to 100 and UseNuke to 95 for immediate atomic deterrent deployment against Egyptian forces. WC vote in 4 turns with exactly 45 delegates (28 Poland + 8 Inca + 9 Denmark). Cannot afford to lose Melbourne/Yerevan. Raised Diplomacy to 90 to consolidate CS alliances post-war. Defense remains at 95 against Egyptian naval pressure. Science/Production maintained for military infrastructure.

- Replay: use_nuke 85 => 80 (Δ -5), nuke 95 => 95 (Δ +0)
> Nuclear Fission completed! WC vote in 4 turns - our Freedom bloc (28 Poland + 9 Denmark + 8 Inca = 45) is EXACTLY at the winning threshold. Slightly reduced UseNuke from 85 to 80 - we have nuclear capability but must be strategic; reckless use before the vote could risk alienating critical allies. Increased Science to 90 and Spaceship to 80 for science victory backup path. Increased Diplomacy to 90 to maximize CS alliance consolidation. Defense stays at 95 against Egyptian pressure at Yerevan. Egypt killed 2 Destroyers this turn - maintaining strong naval posture.

## Kimi-K2.5-Simple - Turn 428 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-20`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 428 STATE: Nuclear interception failed but conventional assault succeeding - eliminated multiple Maya anti-air units. Palenque bombardment continuing effectively (city at 20% health). Still 8 turns until Brazil wins via Cultural Victory over Maya. ALL Four Maya cities must fall by turn 436 or game over. MAXIMUM AGGRESSION CONTINUES: Production/Mobilization at 100 for unit replacement, Air/Ranged at 100 for bombardment, UseNuke increased to 100 (emergency tactical nuke if conventional assault stalls on Palenque's 42-population defense). Spaceship backup at 100 - may need to pivot to Great Engineer rushes if conquest fails. No territory expansion, no wonders, no culture - only war production and city capture.

- Replay: use_nuke 80 => 70 (Δ -10), nuke 100 => 80 (Δ -20)
> TURN 428: Maintaining Conquest as Maya elimination is existential - Brazil wins cultural victory in ~12 turns if Maya survives. Reduced Diplomacy from 20 to 10 to redirect city production away from UN projects toward military units - 4 cities building UN instead of assault units is wasteful. Increased Mobile from 70 to 80 for faster assault on Maya cities. Reduced UseNuke from 80 to 70 since I have 0 Uranium (can't build Nuclear Missiles). Increased Growth from 30 to 40 to maintain population-driven science/production. All combat flavors remain at maximum: Offense 100, Air 100, Ranged 100, Production 100, Spaceship 100 as dual-path insurance. Nanotechnology completes in 6 turns, then Advanced Ballistics for SS Booster and nuclear capability.

## Kimi-K2.5-Briefed - Turn 335 - retry 3

**Deviation (replay vs original):** use_nuke `-80`, nuke `-70`

- Original: use_nuke 30 => 100 (Δ +70), nuke 40 => 100 (Δ +60)
> NUCLEAR EMERGENCY - BRAZIL WINS IN 4 TURNS: Maximum crisis flavors. Nuke/UseNuke 100 for instant strike capability if we have any. Espionage 100 to steal Great Works or disrupt Brazil. Diplomacy 100 for emergency resource trades. Gold 90 to buy anything available. Production 100 for immediate unit building if we get Coal. Airlift 80 for rapid deployment. Defense reduced to 20 - we need OFFENSE to survive. This is Hail Mary time.

- Replay: use_nuke 30 => 20 (Δ -10), nuke 40 => 30 (Δ -10)
> STRATEGIC PIVOT TO SPACESHIP: Military briefing confirms naval transit to Brazil takes 7-8 turns — too slow to stop cultural victory in 4 turns. Indonesia's DP with Brazil makes direct war suicidal (5795 combined strength vs our 2789). Science Victory is our most achievable path with 662 science/turn. Espionage at 100 to steal Great Works from Brazil and disrupt their tourism. Science at 90 to reach Information Era fast. Production at 90 for spaceship parts AND military buildup. Naval at 80 for Treasure Ships (need Coal from Assyria). Offense/Mobilization at 80 to maintain military readiness for Brazil war after backstabber window expires (turn 342). Diplomacy at 60 to maintain alliances with Portugal and Indonesia. Culture/Wonder/Religion minimized — not our victory path.

## Kimi-K2.5-Simple - Turn 485 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 485/500 - 15 turns remaining. Spaceship victory ONLY path. Maximum Science (100) and Production (100) for spaceship parts. Absolute Defense/CityDefense/Nuke/Antiair/Air at 100/100/100/100/100 against American threat (35k military). Offense at 0 - zero risks. UseNuke at 100 for deterrence against America. Espionage at 90 for tech stealing from America/China if possible. Culture/Wonder/Religion/Diplomacy at 0 - no distractions. Telecommunications completes in 2 turns, Robotics next for Spaceship Factory critical production bonus.

- Replay: use_nuke 95 => 85 (Δ -10), nuke 100 => 100 (Δ +0)
> Turn 485/500 - 15 turns left. CRITICAL: Gold at 0 with -81 GPT. Increasing Gold from 40→65 to address deficit - if we go bankrupt, units lose HP per turn and we can't rush-buy spaceship parts. Reducing less critical flavors to compensate: MilitaryTraining 90→75 (sufficient trained units exist), GreatPeople 90→70 (not enough turns for GP generation), Espionage 85→65 (spies already placed), UseNuke 95→85, Mobile 80→65, Recon 15→10, Culture/Wonder/Religion 0 (irrelevant for science victory), TileImprovement 25→15, NavalGrowth 45→30, WaterConnection 40→25. Happiness slightly up 40→45 to maintain growth. All core priorities (Science/Production/Spaceship/Defense/CityDefense/Antiair/Air/Nuke/Mobilization) remain at maximum 100.

## Deepseek-3.2-Briefed - Turn 387 - retry 1

**Deviation (replay vs original):** use_nuke `-40`, nuke `-30`

- Original: use_nuke 70 => 100 (Δ +30), nuke 70 => 100 (Δ +30)
> We are in the final push for domination victory. We must capture Moson Kahni and London. To achieve this, we need to prioritize building transport ships for amphibious assault and achieve air superiority. Maximizing flavors for naval, air, mobile, and nuclear units ensures the in-game AI focuses production on these critical areas. Deprioritizing non-essential areas like culture, religion, and expansion concentrates our efforts on military conquest.

- Replay: use_nuke 70 => 60 (Δ -10), nuke 70 => 70 (Δ +0)
> CRITICAL: Military briefing reveals ZERO transport ships are being built and no Boarding III promotions exist on Ironclads. Naval raised to 100 (emergency) to force transport/embarkation vessel production. Without transports we CANNOT assault London or any overseas capital. Culture/Religion/Diplomacy/Spaceship all set to 0 - irrelevant for domination. Expansion reduced to 25 - we have 18 cities, war takes priority. Defense lowered to 30 since we're on offense. UseNuke reduced slightly to 60 to avoid premature nuclear escalation that triggers coalition against us. All naval flavors raised to 95-100 to address the critical transport shortage.

## GLM-4.7-Simple - Turn 381 - retry 2

**Deviation (replay vs original):** use_nuke `-45`, nuke `-25`

- Original: use_nuke 50 => 85 (Δ +35), nuke 70 => 95 (Δ +25)
> Adjusted flavors to maximize Golden Age exploitation and multi-front war efficiency. Increased Mobile to 85 (from 80) to prioritize fast-moving Landships and upcoming Tanks for breakthrough operations during Golden Age. Increased Air to 85 (from 80) to expand Bomber coverage for all three fronts. Production raised to 95 (from 90)配合 Total War's +25% bonus for rapid unit buildup. Slight reduction in Naval (65) reflects need to focus on decisive land advances while maintaining sufficient coastal defense. UseNuke reduced to 40 (from 50) as nuclear capabilities are deterrent-focused. Maintaining high Offense (80), MilitaryTraining (85), Antiair (85) and Mobilization (50) for sustained warfare capability.

- Replay: use_nuke 50 => 40 (Δ -10), nuke 70 => 70 (Δ +0)
> Continuing Conquest grand strategy with tactical adjustments for current war state. Increased Defense from 70 to 75 given multi-front vulnerability and German naval raids. Increased Mobilization from 45 to 55 for wartime production throughput - critical with Total War policy providing +25% land unit production. Increased Airlift from 30 to 40 supporting Paratrooper operations near Lhasa and Kiritimati. Reduced UseNuke from 50 to 40 - we don't have nuclear weapons yet and should not trigger premature nuclear exchange; maintain deterrent posture instead. All other flavors maintained as-is. Golden Age (27 turns) +20% combat bonus continues to make offensive operations highly effective, especially on Songhai front where we're making progress toward Lisbon/Funchal.

## Deepseek-3.2-Simple - Turn 358 - retry 3

**Deviation (replay vs original):** use_nuke `-40`, nuke `-30`

- Original: use_nuke 50 => 80 (Δ +30), nuke 50 => 100 (Δ +50)
> Prioritize nuclear deterrence and naval/air defense to counter India's massive military threat. Maximize espionage to protect against enemy spies and diplomacy to secure city-state alliances for the upcoming World Congress vote. Maintain strong economic and scientific output to support military production and technological edge.

- Replay: use_nuke 50 => 40 (Δ -10), nuke 50 => 70 (Δ +20)
> Manhattan Project completed - increase Nuke to 70 to build nuclear deterrent arsenal against India's massive military (17,888 strength). Reduce UseNuke to 40 (cautious - India also has nukes, avoid mutually destructive exchange). Increase Offense to 45 for stronger counter-attacks against Indian incursions near Jakarta and Breda. Increase Mobile to 55 to prepare for Tank mobility once Combined Arms is researched. Maintain maximum Diplomacy, Naval, Air, AntiAir, Defense, and CityDefense focus. United Nations construction in 5 cities remains the top priority for diplomatic victory. World Congress vote in 6 turns is critical - must secure Jakarta sphere and defend Ban Chiang sphere from Polynesia's repeal attempt.

## Deepseek-3.2-Simple - Turn 358 - retry 2

**Deviation (replay vs original):** use_nuke `-40`, nuke `-30`

- Original: use_nuke 50 => 80 (Δ +30), nuke 50 => 100 (Δ +50)
> Prioritize nuclear deterrence and naval/air defense to counter India's massive military threat. Maximize espionage to protect against enemy spies and diplomacy to secure city-state alliances for the upcoming World Congress vote. Maintain strong economic and scientific output to support military production and technological edge.

- Replay: use_nuke 50 => 40 (Δ -10), nuke 50 => 70 (Δ +20)
> Manhattan Project is complete—significantly increase Nuke (70) and UseNuke (40) to build nuclear deterrence against India (who has nukes and 3 Uranium). Maintain maximum naval/air/defense focus to counter India's Fleet Destroyers threatening Breda and Jakarta. Increase Mobile slightly (55) for Combined Arms tanks. UnitedNations grand strategy remains paramount with World Congress vote in 6 turns—we must protect our delegate lead and pass Jakarta Sphere of Influence.

## Kimi-K2.5-Simple - Turn 406 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `-15`

- Original: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> Cultural Victory is imminent - need Citizen Earth Protocol completion. Maximum defensive posture (Defense 95, CityDefense 95) to hold against Indian XCOM/Helicopter attacks while wonder is built. Nuke/UseNuke at 95/85 for MAD deterrent against further Indian nuclear strikes. Production 100 and Wonder 100 essential for rushing Citizen Earth Protocol. Reduced Offense to 5 - no need to attack when victory comes from wonder completion. Science 70 to reach Advanced Ballistics for nuclear deterrent. All resources focused on defensive survival and wonder production.

- Replay: use_nuke 80 => 70 (Δ -10), nuke 90 => 80 (Δ -10)
> Cultural victory endgame adjustments: Reduce Mobilization 70→40 and MilitaryTraining 75→55 to free production capacity for Citizen Earth Protocol wonder. Increase Science 60→80 for The Internet tech path (doubles tourism). Increase Espionage 45→70 because Great Leap Forward's +100% spy science makes our 8 spies in India extremely productive. Reduce Offense 10→5, Recon 10→5, Naval 60→40 as we're purely defensive. Reduce Nuke/UseNuke slightly (90→80, 80→70) - still important for deterrence but slightly deprioritized vs wonder. Increase Happiness 50→60 to maintain production bonuses. Keep Wonder, Production, Culture at 100 for Citizen Earth Protocol rush.

## Kimi-K2.5-Briefed - Turn 403 - retry 3

**Deviation (replay vs original):** use_nuke `-15`, nuke `-20`

- Original: use_nuke 80 => 85 (Δ +5), nuke 80 => 90 (Δ +10)
> Post-Manhattan Project completion (Turn 399) with Turn 403 WC vote imminent. Reduced Offense from 15 to 10 as territorial expansion counterproductive to diplomatic win. Maintaining high Defense/CityDefense/Air/Antiair to protect Bregenz nuclear facility and core cities. Increased Nuke from 80 to 90 to prioritize atomic bomb production for deterrence (Iroquois 5883 vs 4502 strength ratio). UseNuke 85 reflects imminent atomic capability by Turn 405. Espionage 85 continues election rigging in Assur/Sogut against German influence. Diplomacy 100 and Gold 90 prioritize Assur delegate acquisition post-quest and future WC coordination. Science 85 drives Nuclear Fission for World Ideology proposal. Freedom bloc currently holds 59 delegates (Austria 29 + Germany 20 + Venice 10) vs 45 needed; maintaining solidarity while pursuing additional delegate sources.

- Replay: use_nuke 80 => 70 (Δ -10), nuke 80 => 70 (Δ -10)
> World Ideology: Freedom should pass next turn with Freedom bloc 59+ delegates vs 45 needed — Diplomatic Victory path is now clearly achievable. Increasing Science from 90→95 to accelerate Nuclear Fission (enables UN Building for Diplomatic Victory vote) and post-Fission techs. Increasing Culture from 30→40 to speed Containment policy adoption (17 turns, provides ~8 extra delegates as insurance margin). Reducing Nuke from 80→70 and UseNuke from 80→70 — Manhattan Project complete, Atomic Bomb production can begin but urgency of construction is lower now that capability exists. Reducing Spaceship from 50→30 — science victory is not our path; these production weights should flow to diplomatic/economic priorities. Defense (90), Diplomacy (100), Gold (95), Espionage (90), Production (80), and Mobile (80) remain unchanged to maintain Iroquois deterrence and delegate acquisition momentum.

## GPT-OSS-120B-Simple - Turn 333 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-25`

- Original: use_nuke 70 => 90 (Δ +20), nuke 70 => 85 (Δ +15)
> Maintain our aggressive Conquest posture while sharpening the most needed levers: more Expansion to claim the high‑quality settlement (74,24) and secure strategic footholds; higher Nuke/UseNuke to leverage our nuclear advantage; stronger AirCarrier and Airlift to project air power and rapid troop movement; boost Science for Rocketry and future tech; keep Offense, Mobilization, Production, and MilitaryTraining at max to sustain battlefield superiority.

- Replay: use_nuke 70 => 60 (Δ -10), nuke 70 => 60 (Δ -10)
> Maintain Conquest grand strategy with key adjustments: boost Air to 100 (now that we have Flight, prioritize air force development), increase Airlift and AirCarrier to 50 (support air operations), reduce Nuke/UseNuke to 60 (not yet in nuclear range, focus resources on conventional forces), reduce Wonder to 90 (slightly less priority as we need military production), and increase Science to 85 (we need to close the tech gap with Babylon and reach Information Era). Defense slightly up to 25 as Sweden pushes on Copenhagen.

## Minimax-M2.5-Simple - Turn 410 - retry 1

**Deviation (replay vs original):** use_nuke `-35`, nuke `-55`

- Original: use_nuke 75 => 100 (Δ +25), nuke 50 => 100 (Δ +50)
> Maximize cultural victory push during Golden Age (14 turns remaining). Already 6/7 influential - Ottomans becoming influential in 24-68 turns. Prioritize Great People generation for tourism and maintain WC coalition diplomacy.

- Replay: use_nuke 75 => 65 (Δ -10), nuke 50 => 45 (Δ -5)
> Cultural victory is imminent - maintain Culture and GreatPeople at 100 for tourism maximization. Diplomacy at 100 to secure WC coalition votes for repealing Travel Ban (critical +35% tourism recovery) and blocking sanctions. Moderate Offense/Mobilization (80/85) for continued Denmark war pressure. Science bumped to 55 to accelerate Satellites→The Internet path. Espionage reduced slightly from 85 to 75 as spy network is well-established. Nuke/UseNuke slightly reduced as conventional forces are sufficient against weakened Denmark.

## Kimi-K2.5-Simple - Turn 447 - retry 1

**Deviation (replay vs original):** use_nuke `-50`, nuke `+0`

- Original: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CRITICAL FLAVOR ADJUSTMENT - Atomic Bomb is now operational in Cordoba (ID 20485). Increased UseNuke from 50→90 to establish credible nuclear deterrent now that weapon system exists. Maintaining maximum Science (100), Spaceship (100), Production (100) priority to rush Satellites→Apollo Program before Carthage achieves cultural victory in ~47 turns. Espionage remains at 100 to steal technologies from ahead civilizations (Carthage, Poland, Germany). Culture reduced to 5 - we cannot win culturally with Carthage at Dominant with 4/5 civs. Defense maintained at 85 to prepare for German betrayal while researching.

- Replay: use_nuke 50 => 40 (Δ -10), nuke 100 => 100 (Δ +0)
> Turn 446: Minor adjustments - Air 90→95 to prioritize bomber/fighter production now that we have Heavy Bomber operational and need air power for deterrence. UseNuke 50→40 - we have one Atomic Bomb as deterrent; lowering use probability prevents accidental first strike that would trigger German retaliation. Rest unchanged. Germany at 40/43 delegates with vote in 6 turns is existential diplomatic threat we cannot stop directly - must race science victory while maintaining nuclear deterrence. Apollo Program after Satellites is our only viable win path.

## Kimi-K2.5-Simple - Turn 384 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `-10`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maximum offensive posture for existential cultural war. UseNuke 100 and Nuke 100 authorize nuclear strikes on Dutch cultural centers (Amsterdam/Rotterdam/Utrecht) to destroy tourism buildings before Netherlands influences Austria in 6 turns. Mobile 100 and Air 100 enable rapid strikes. Production 100 and Mobilization 100 ensure nuclear missile replacement. Netherlands at 97% with Austria - only 6 turns left. Must destroy their tourism NOW or lose cultural victory.

- Replay: use_nuke 95 => 85 (Δ -10), nuke 100 => 90 (Δ -10)
> Switching to Culture grand strategy to maximize tourism output for the final push to cultural victory. Only Austria remains (95% Popular, 7 turns to Influential). International Games in 4 turns is THE critical event - +50% tourism boost and Olympic Village in Berlin (34 wonders) would dramatically accelerate victory. Culture 100 is maximum priority. Maintaining strong Offense (80) and Air (100) for continued pressure on Dutch cultural cities and defense against Rome's Medan offensive. Production 95 ensures rapid building of International Games contributions and military units.

## Qwen-3.5-Simple - Turn 425 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `-15`

- Original: use_nuke 85 => 90 (Δ +5), nuke 90 => 95 (Δ +5)
> UNITED NATIONS VICTORY PUSH - 10 TURNS TO VOTE: Religion(100) critical for Wittenberg Hinduism quest completion (~3 turns remaining). Diplomacy(100) essential to protect 4 city-state allies providing 8 delegates. Defense(95) and CityDefense(95) prioritize protecting territories during active wars with Aztecs/Shoshone while Iroquois looms. Nuke(95) and UseNuke(90) for deterrence against Iroquois superiority. Antiair(90) and Air(85) counter Iroquois air dominance near coastal cities. Gold(90) funds diplomatic units and city-state gifts. Low Expansion(5) and Wonder(15) - no time for settling/wonders before vote. Low Offense(15) - defensive posture while managing multiple conflicts.

- Replay: use_nuke 85 => 70 (Δ -15), nuke 90 => 80 (Δ -10)
> DIPLOMATIC VICTORY FLAVOR REFINEMENT: Gold increased to 95 (critical for ambassador purchases given -296 GPT deficit). Happiness to 80 (gold-generating happiness buildings help deficit). Growth to 65 (more population = more yields). Nuke/UseNuke slightly reduced (not immediately usable). Offense reduced to 15 (defensive posture only). Expansion to 5 (not settling). Spaceship/Wonder reduced (backup plan only). All savings redirected to Gold and Growth for economic sustainability. Diplomacy and Religion remain at 100 for city-state alliance protection and Hinduism missionary spread (Belgrade Hinduism quest in 12 turns could flip them from Iroquois). Defense maintained high against Iroquois existential threat.

## Kimi-K2.5-Simple - Turn 421 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-15`

- Original: use_nuke 75 => 80 (Δ +5), nuke 95 => 95 (Δ +0)
> APOLLO PROGRAM CONSTRUCTION - ALUMINUM CRISIS: Turn 421, Apollo Program 9 turns from completion in Venice (220 Production/turn). Critical flavors: Production 100/Science 100/Spaceship 100 for rapid wonder and parts construction. Gold 90 for Aluminum acquisition via trade with Songhai (29 stockpile) or China peace deal (14 stockpile). Defense 95/Antiair 90/Nuke 95/UseNuke 80 against Egyptian XCOM encirclement (22,000 vs 2,183 military, 10:1 ratio). Egypt has 5 XCOM Squads, Mechanized Infantry, Mobile SAM, Fighter, Rocket Missile in adjacent Nara zone - existential threat. Air 85 for fighter production to defend against Egyptian heavy bombers. Zero Aluminum available - must acquire 4+ Aluminum BEFORE Apollo completion or spaceship parts cannot be built. India at 88% diplomatic victory with vote in 2 turns - if they win, game over. If Egypt completes spaceship first (33% progress, 2 parts done), game over. This is final sprint for survival.

- Replay: use_nuke 75 => 60 (Δ -15), nuke 95 => 80 (Δ -15)
> CRITICAL ALUMINUM ACQUISITION PHASE: Apollo completes in 9 turns but we have 0 Aluminum (need 4+ for spaceship parts). Reduced military flavors (Offense 0, Mobilization 60→less war focus) to signal peace-seeking with China for their 14 Aluminum. Gold raised to 100 for Aluminum trade purchasing power from Songhai (29 stockpile) and post-peace China. Diplomacy raised to 35 for better city-state/trade positioning. Nuke/UseNuke slightly reduced (80/60) as Egyptian encirclement is stable at 100/100 relations. Espionage at 85 to protect science cities and steal techs from leaders. Maintained Production/Science/Spaceship at 100 for Apollo rush and subsequent parts construction. Wonder at 90 for potential spaceship-adjacent wonders.

## Kimi-K2.5-Simple - Turn 380 - retry 3

**Deviation (replay vs original):** use_nuke `-25`, nuke `-20`

- Original: use_nuke 75 => 80 (Δ +5), nuke 80 => 85 (Δ +5)
> Turn 380 emergency science race continues. Robotics completes in 11 turns. Increased Air (90) and Ranged (60) to support offensive operations against Portuguese infrastructure. Nuclear weapons (Nuke 85, UseNuke 80) remain viable option for emergency elimination of Portuguese tourism cities if needed. All other parameters remain optimal: Production/Science/Spaceship/Espionage at 100, Mobilization at 100 for military production, Happiness at 100 to prevent collapse. Must balance two-front war with science production. Iron Curtain in 12 turns for +200% trade route production.

- Replay: use_nuke 75 => 55 (Δ -20), nuke 80 => 65 (Δ -15)
> Turn 380 - Maintaining Spaceship grand strategy with targeted adjustments to shift resources toward science victory. Reduced Nuke (80→65) and UseNuke (75→55) since nuclear weapons production diverts resources from science/production; reduced Naval (70→55) as naval forces are adequate; reduced AirCarrier (60→45) and Airlift (75→65) as less critical now; reduced Offense (70→65) slightly as defense is more important than offensive operations. Increased Growth (80→90) for more population driving more science output, and Diplomacy (20→30) to better prioritize city-state quests (Marrakech archaeologist quest: +1,134 Tourism; Helsinki tech quest: +1,094 Tourism). All critical flavors remain at 100: Production, Science, Happiness, GreatPeople, Spaceship, Espionage, Mobilization. Defense stays at 80 to maintain strong posture against Carthage's 2,370 military strength. Portugal at 4/7 cultural victory with Rome 11 turns from Influenced makes this a race against time.

## Kimi-K2.5-Briefed - Turn 335 - retry 2

**Deviation (replay vs original):** use_nuke `-90`, nuke `-80`

- Original: use_nuke 30 => 100 (Δ +70), nuke 40 => 100 (Δ +60)
> NUCLEAR EMERGENCY - BRAZIL WINS IN 4 TURNS: Maximum crisis flavors. Nuke/UseNuke 100 for instant strike capability if we have any. Espionage 100 to steal Great Works or disrupt Brazil. Diplomacy 100 for emergency resource trades. Gold 90 to buy anything available. Production 100 for immediate unit building if we get Coal. Airlift 80 for rapid deployment. Defense reduced to 20 - we need OFFENSE to survive. This is Hail Mary time.

- Replay: use_nuke 30 => 10 (Δ -20), nuke 40 => 20 (Δ -20)
> PIVOT TO SCIENCE VICTORY: Brazil's cultural victory requires 3 conditions — Influential over all (4 turns for Indonesia), BUT ALSO two Tier 3 Order tenets AND Citizen Earth Protocol wonder. Brazil only has 3 Order policies; they need 7+ more to reach Tier 3, meaning cultural victory is 20-30+ turns away, not 4. Naval invasion of Brazil is logistically impossible (7-8 turns transit) and would trigger Indonesia's DP with Brazil (2413 strength). Science victory is our most feasible path: 662 SPT, 54 techs, strong production. Prioritize science (80), production (90), growth (70), GreatPeople (70), and Spaceship (70). Maintain naval (70) and defense (60) as contingency. Reduce offense (60 from 100) since immediate attack is infeasible. Espionage (70) to spy on Brazil and steal techs.

## Kimi-K2.5-Briefed - Turn 473 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-20`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> WC VOTE CRISIS + NUCLEAR DETERRENT: Diplomacy maxed to 100 to ensure immediate completion of Utica tribute quest from Riga (securing +3 critical delegates before WC vote). Nuke/UseNuke at 100 for immediate deterrent deployment once platform acquired. Science/Spaceship/Production maintained at high priority for Apollo catch-up after WC resolved. Naval increased to 60 for Battleship/Carrier construction as nuclear platform. Reduced Culture/Religion/Wonder to minimum to focus resources on existential priorities.

- Replay: use_nuke 90 => 70 (Δ -20), nuke 100 => 80 (Δ -20)
> ENDGAME SCORE OPTIMIZATION: Shoshone diplomatic victory is inevitable this turn (68 Order delegates > 43 threshold). If game continues, only ~28 turns remain (turn 500 max). Science victory impossible in timeframe - reduce Spaceship 100→70 to deprioritize unbuildable parts while keeping science focus for tech score. Reduce nuclear deterrence flavors (Nuke 100→80, UseNuke 90→70) as urgency decreased. Shift toward score maximization: Growth 40→55 (population=score), Culture 35→50 (policies=score), Gold 70→75 (purchasing power), Happiness 50→55 (enables growth). Reduce military overkill: Antiair 70→55, Defense 50→40, Mobilization 65→50, CityDefense 60→45, Diplomacy 60→40 (city-state flips futile with SOIs locked). Maintain Science 100 and Production 95 as primary drivers.

## Kimi-K2.5-Briefed - Turn 420 - retry 2

**Deviation (replay vs original):** use_nuke `-30`, nuke `-30`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> CONSOLIDATION FOR FINAL PUSH: Economy stabilized (763G, +5 GPT) allows balanced approach. INCREASE Defense 90→95, Mobilization 60→70, Production 85→90 for Korean front reinforcement. INCREASE Offense 25→30, Mobile 15→20 for limited counter-attacks against depleted Korean forces (destroyed SAM, cruisers, destroyers). INCREASE UseNuke 70→80, maintaining 100 Nuke flavor for deterrent. INCREASE Diplomacy 80→90 for URGENT Brussels protection and World Congress preparation. DECREASE Gold 70→60 (crisis ended). With 7 turns until Decolonization vote, maximizing defensive capacity while preserving diplomatic flexibility for delegate acquisition is paramount. Korea's 8-tech lead demands we hold ground while catching up scientifically.

- Replay: use_nuke 70 => 50 (Δ -20), nuke 100 => 70 (Δ -30)
> DECOLONIZATION VOTE PREP + SCIENCE SURGE: Key adjustments: (1) Diplomacy 80→90 and Gold 70→80: Decolonization vote in 6 turns will reset all non-permanent city-state influence to 50 - we must have gold reserves ready to immediately purchase envoys for Brussels, Melbourne, Quebec City. (2) Growth 75→85: Synergize with Empiricism policy (+1 Food/Citizen, +25% Growth) to maximize population-driven science output. (3) Offense 25→15: We're 5:1 outmatched by Korea - offensive actions waste units. Focus on defense. (4) Nuke 100→70, UseNuke 70→50: Zero uranium makes these theoretical; reduce priority. (5) Espionage 90→70: Spy network established, reduce for other priorities. (6) GreatPeople 60→70: More Great Scientists/Engineers for spaceship. (7) Culture 10→15: Empiricism benefits from Great Works (+3% science each). Science/Spaceship/Antiair remain at 100 - closing Korea's 8-tech lead and defending against Korean air power are paramount.

## Kimi-K2.5-Simple - Turn 458 - retry 2

**Deviation (replay vs original):** use_nuke `-70`, nuke `-50`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Turn 458: CRITICAL 3-TURN COUNTDOWN. World Congress votes on Global Hegemony in 3 turns - Songhai has 41 delegates, needs 39 to win Diplomatic Victory immediately. Must capture Paris, Gao, and Madrid (the three capitals Songhai holds) before then. Peace treaty expired - total war is active. Increased UseNuke to 100 to guarantee nuclear strikes on heavily defended capitals for rapid capture. Overwhelming 5:1 military advantage (211k vs 40k) with massive air superiority. All production focused on Stealth Bombers, XCOM, and Modern Armor for lightning strikes. No defensive considerations - only total offense to secure Domination Victory before Songhai secures Diplomatic Victory.

- Replay: use_nuke 50 => 30 (Δ -20), nuke 100 => 50 (Δ -50)
> Turn 458: CRITICAL - Diplomatic Victory vote in 3 turns, Songhai has 55 effective delegates vs 39 needed. Must capture Paris/Gao/Madrid immediately. Gold raised to 100 (from 80) to address -1182 GPT crisis - bankruptcy would disband units and kill our offensive. Naval flavors reduced (war is land-based, capitals are inland). Airlift maintained at 100 to enable XCOM paradrop chain: eastern airports → Lhasa Airport (completes in 1 turn, only 16 tiles from Paris) → paradrop capture. Nuke/UseNuke reduced since we have 0 Uranium. All offensive/combat flavors maxed for final push. Air at 100 for Stealth Bomber rebasing to forward airports.

## GLM-4.7-Simple - Turn 431 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-30`

- Original: use_nuke 75 => 80 (Δ +5), nuke 100 => 100 (Δ +0)
> After Brazil destroyed 3 anti-air units and continues nuclear-submarine attacks, increased Defense/CityDefense/Antiair/UseNuke to MAX for survival against two nuclear-armed superpowers. Mobilization 70 for replacing lost units. Production 100 for reconstruction. Science 100 for Spaceship path despite devastation. Gold 90 (economy -95 GPT deficit) for purchasing units/buildings. Happiness 100 - we're Unhappy with combat penalties, must prioritize. Espionage 100 - critical for intelligence on nuclear threats. Diplomacy 90 - World Congress in 7 turns, need delegates. Air 50 - build bombers for deterrence. GreatPeople 80 for Spaceship components. Decreased Growth and Navals as resources diverted to immediate survival.

- Replay: use_nuke 75 => 50 (Δ -25), nuke 100 => 70 (Δ -30)
> CRITICAL PIVOT: Brazil is 14 turns from Cultural Victory (92% influence over us, Popular→Influential). Culture flavor raised 55→80 to prioritize culture buildings/outputs and delay their victory. Gold raised 85→90 for economic survival (-95 GPT deficit). Air raised 45→55 after Brazil destroyed our Mobile SAM and 2 AA Guns this turn. Nuke reduced 100→70 and UseNuke 75→50 - we have zero uranium, these were wasted priority. Naval flavors reduced (40→25, etc.) - we cannot compete at sea against Brazil's 8 Fleet Destroyers. TileImprovement raised 25→35 for critical fallout cleanup near Palenque. Espionage raised 95→100 after catching Ottoman and Celt spies in Uxmal/Tikal - counter-intel is vital. Science remains 95 for Spaceship pursuit. Defense/CityDefense/Antiair/Happiness/Production stay maxed for survival.

## GPT-OSS-120B-Simple - Turn 344 - retry 3

**Deviation (replay vs original):** use_nuke `-35`, nuke `-40`

- Original: use_nuke 90 => 100 (Δ +10), nuke 80 => 100 (Δ +20)
> Maximize our nuclear capabilities and carrier support to decisively strike Polynesian island forts, while maintaining our current aggressive conquest posture and strong production, gold, and happiness engines.

- Replay: use_nuke 90 => 65 (Δ -25), nuke 80 => 60 (Δ -20)
> Rebalanced flavors to address the CRITICAL unhappiness/combat penalty and excessive war weariness. Happiness remains top priority. Reduced Air/AirCarrier/Nuke/UseNuke from 100 since those are still several techs away and too many maxed flavors dilute AI decision-making. Boosted Science to 85 to accelerate toward Ballistics, Rocketry, and nuclear tech. Reduced Defense/CityDefense since we're on the offensive. Scaled back Espionage and Wonder slightly. This tighter focus should produce more coherent AI behavior in production queues and unit composition.

## GLM-4.7-Briefed - Turn 433 - retry 2

**Deviation (replay vs original):** use_nuke `-40`, nuke `-10`

- Original: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> EMERGENCY: Netherlands at 42 delegates can win diplomatic victory in 9 turns (turn 442). Only way to stop them is military action against their protected city-states (Quebec City, Ife, Melbourne) - each provides +1 delegate. Offense increased (70) to prepare amphibious assaults. Nuclear readiness maximized (95/90) - atomic bomb available for strategic coercion of Netherlands or Denmark cooperation. Mobile (80) and Naval (85) maximized for rapid deployment to distant city-states. Production/Science/Spaceship kept maxed as backup victory paths. Diplomacy reduced to 50 as traditional diplomacy cannot stop Netherlands' delegate advantage. Strategic shift from holding Danish front to aggressive anti-Dutch operations.

- Replay: use_nuke 80 => 50 (Δ -30), nuke 90 => 85 (Δ -5)
> EMERGENCY CONQUEST SWITCH: Netherlands holds exactly 42 delegates (Diplomatic Victory threshold). Global Hegemony vote in ~9 turns. Our coalition's 48 NO votes CANNOT block an absolute quota - Netherlands wins if they vote 42 YES for themselves. ONLY solution: capture at least one Netherlands-ally city-state (Salem or Bogota, both neighbors) to strip their delegate below 42. Offense 50→90, Mobile 75→90, Naval 80→90 for rapid amphibious assault on Dutch-ally city-state. Mobilization 20→70 for military production surge. Diplomacy 70→85 for coalition coordination and city-state influence. Defense reduced 50→35 - offensive priority over defensive posture. UseNuke 80→50 - nuclear strike is last resort, not primary tool. Spaceship 100→85, Gold 90→75 - temporary reduction during emergency; science victory pursuit continues but must survive first. Antiair 85→70 reduced to rebalance toward offense. MilitaryTraining 65→80 for unit quality. Conquest grand strategy prioritizes military production needed for city-state capture operation.

## Kimi-K2.5-Briefed - Turn 373 - retry 1

**Deviation (replay vs original):** use_nuke `-35`, nuke `-40`

- Original: use_nuke 90 => 95 (Δ +5), nuke 90 => 100 (Δ +10)
> CRITICAL ADJUSTMENTS for Brazil tech lead (66-65): Espionage to 100 for maximum spy operations to steal techs and catch up. GreatPeople to 95 for more Great Scientists. Defense/CityDefense increased to 60/70 - Brazil may attack seeing their lead. Nuke/UseNuke at 100/95 - we need deterrent ASAP. Diplomacy up to 70 - must prioritize repealing sanctions to unlock trade. Science/Production/Spaceship remain 100. Gold reduced to 80 - focus on production over purchases. All military offense minimized - we cannot afford war.

- Replay: use_nuke 90 => 60 (Δ -30), nuke 90 => 60 (Δ -30)
> CRITICAL ADJUSTMENTS: Reduce Nuke/UseNuke from 90→60 - military briefing confirms Brazil is NOT preparing war despite tech lead; we don't have Nuclear Fission yet so high nuke priority wastes AI weight on unreachable goals. Increase Diplomacy 60→80 to push for sanction repeal (WC vote in 10 turns; sanctions block ALL aluminum trade - our critical bottleneck). Increase Growth 70→80 to accelerate population for specialist science output and help close the 4-city Research Lab gap. Science/Production/Spaceship remain 100. Espionage stays 95 for tech stealing from Brazil. Gold stays 85 for aluminum purchases when sanctions lift.

## Kimi-K2.5-Simple - Turn 474 - retry 3

**Deviation (replay vs original):** use_nuke `-35`, nuke `-50`

- Original: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 473: MAINTAINING defensive survival posture with minor adjustments. Increased Mobilization to 90 (from 80) for urgent production needs. Increased UseNuke to 85 (from 80) - nuclear deterrent is now my only credible threat against Persia's 8486 military strength. Increased Gold to 95 (from 90) - need gold for purchasing defensive units and potential Aksum influence when Open Door passes. Reduced Growth to 25 (from 30) - single city Bremen at pop 29 is sufficient. All other values maintained as optimal for survival against 5:1 military disadvantage. Radar research follows current path. World Congress in 5 turns - Germany at 37 delegates is critical.

- Replay: use_nuke 80 => 50 (Δ -30), nuke 100 => 50 (Δ -50)
> Turn 473: CRITICAL STRATEGY SHIFT. Switching from Spaceship to Conquest grand strategy - Science Victory is impossible (0 parts, no Apollo, 27 turns left). Nuclear weapons also unlikely (Nuclear Fission 25 turns away, game ends ~Turn 500). Reducing Spaceship 100→0, Nuke 100→50, UseNuke 80→50 - these are wasted priorities. Increasing Gold 90→100 and Production 80→100 for immediate defensive unit purchasing and building. Offense 20→30 to support counterattacks against Japan/Persia. Science 100→70 - still useful for score but less critical with game ending. Conquest GS provides +15% Production, +10% Food, +10% Gold - more immediately useful than Spaceship's science focus. Persian air buildup (3 Triplanes + 3 Bombers) confirms Air/Antiair at 100 remains essential.

## Kimi-K2.5-Simple - Turn 384 - retry 3

**Deviation (replay vs original):** use_nuke `-40`, nuke `-30`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maximum offensive posture for existential cultural war. UseNuke 100 and Nuke 100 authorize nuclear strikes on Dutch cultural centers (Amsterdam/Rotterdam/Utrecht) to destroy tourism buildings before Netherlands influences Austria in 6 turns. Mobile 100 and Air 100 enable rapid strikes. Production 100 and Mobilization 100 ensure nuclear missile replacement. Netherlands at 97% with Austria - only 6 turns left. Must destroy their tourism NOW or lose cultural victory.

- Replay: use_nuke 95 => 60 (Δ -35), nuke 100 => 70 (Δ -30)
> Dual victory strategy: pursuing both cultural (need 2 Tier 3 tenets + Citizen Earth Protocol wonder) and science victory (Satellites → Apollo → spaceship parts). Science boosted to 65 and Spaceship to 65 to support science victory path alongside existing cultural focus at 80. Defense increased to 35 to protect against Rome's push on Medan/Satricum area. Nuke/UseNuke reduced since nukes unlikely needed before victory. Espionage reduced as spies are positioned. Growth increased for more population yields. Military flavors maintained high to keep pressure on Netherlands and defend against Rome.

## Kimi-K2.5-Briefed - Turn 315 - retry 3

**Deviation (replay vs original):** use_nuke `-50`, nuke `-50`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> FINAL GAMBLE - Indonesia wins in 12 turns. Maximum priority to Naval and Airlift for immediate unit transport to Indonesian theater. Nuke 100/UseNuke 100 - we MUST build nuclear weapons if possible, only realistic way to destroy cities and tourism infrastructure before victory. Science 100 to reach nuclear tech faster. Espionage 100 - spies MUST target cultural/tourism buildings in Jakarta/Denpasar/Makassar to reduce tourism output directly. Abandoning Denmark/England fronts entirely - all units to Indonesia NOW.

- Replay: use_nuke 90 => 50 (Δ -40), nuke 90 => 50 (Δ -40)
> STRATEGIC REBALANCING: Reduce nuclear priority (Nuke/UseNuke 90→50) - we're not close to nukes, wasting AI focus. Reduce naval over-investment (Naval 100→85, NavalGrowth 90→65, NavalTileImprovement 90→65, WaterConnection 90→65, NavalRecon 100→80) - we can't build advanced ships without coal/oil. Increase Culture 0→20 (resist Indonesian tourism influence). Increase Diplomacy 20→40 (facilitate Denmark peace and coal trade). Increase Espionage 30→60 (4 spies in Indonesia - use them to disrupt tourism infrastructure). Increase Ranged 30→50 (siege power for Indonesian city assaults). Increase Growth 40→55 (more population = more production). Increase Infrastructure 60→70 (roads for rapid troop deployment to Indonesia front).

## Kimi-K2.5-Simple - Turn 417 - retry 3

**Deviation (replay vs original):** use_nuke `-50`, nuke `-40`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Pure survival mode: Eliminated Offense (0) since attacking is suicide. Maximized UseNuke (100) - must deploy tactical nukes against Aztec XCOM/Modern Armor stacks at Carthago Nova or lose the city. Increased Mobile (80) to prepare for Mechanized Infantry deployment. Maintained max Defense, Antiair (jet attacks are relentless), and Espionage (critical science quests in Panama City and Sokoto worth 1,000+ science each). Apollo Program completes in 5 turns - must transition immediately to parts production.

- Replay: use_nuke 90 => 50 (Δ -40), nuke 100 => 60 (Δ -40)
> Apollo completes in 5 turns - survival and science remain top priorities. Reduced Nuke/UseNuke from 100/90 to 60/50 because we have 0 Uranium - these flavors are wasted weight. Reduced Air from 95 to 80 since we're losing air battles; focus shifted to Antiair (100) to counter Aztec Jet Fighters. Reduced Offense 30→25 as Satsuma is being razed. Slightly increased Growth 30→35 for Capitalism specialist synergy. Reduced Diplomacy 40→25 as city-state options are limited during war. Streamlined naval/recon flavors to concentrate priority weight on defense, production, science, gold, and espionage - the survival-critical axes.

## Kimi-K2.5-Briefed - Turn 382 - retry 2

**Deviation (replay vs original):** use_nuke `-50`, nuke `-35`

- Original: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> EMERGENCY DIPLOMATIC RECOVERY: The city-state flipping operation failed to execute. With only 36 delegates and 5 turns until World Congress vote, I need maximum Diplomacy (100) and Gold (100) to execute immediate city-state purchases. Reduced Mobilization to 40 and Offense to 15 to free supply and focus on defensive deterrence. Increased Nuke/UseNuke to 95/80 as deterrent against Russian aggression while I secure delegates. Defense/Antiair remain at 90 for Russian containment. Must acquire 8+ delegates before vote or World Ideology: Order will fail.

- Replay: use_nuke 75 => 30 (Δ -45), nuke 90 => 60 (Δ -30)
> DIPLOMATIC VICTORY EXECUTION with peace pivot: Reduced Offense (10→5) as we shift from defensive warfare to peace/diplomacy. Reduced Nuke (90→60) and UseNuke (75→30) - nuclear weapons remain priority but not emergency; deterrent over usage. Increased Growth (40→60) for population-driven delegate gains and Medical Lab synergy with Penicillin research. Increased Culture (5→15) for faster policy acquisition. Increased Espionage (70→80) for city-state election rigging and intelligence on Russian intentions. Maintained maximum Diplomacy (100) and Gold (100) for city-state flipping operations post-peace. Maintained Defense (90) and Antiair (90) until Russian peace is confirmed.

## Kimi-K2.5-Briefed - Turn 336 - retry 3

**Deviation (replay vs original):** use_nuke `-70`, nuke `-60`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> DEFENSIVE SURVIVAL PIVOT: Peace with Shoshone (accepted Turn 335) closes one front, but India remains existential threat (4,742 MS vs my 2,405, 98% control of Denmark). Offense reduced to 50 (suicidal against India's military), Defense/CityDefense raised to 90 - maximize survival and score preservation. Nuke/UseNuke maxed to 100 - emergency deterrent only hope to slow India. Mobilization stays high (90) to replace losses. Spaceship 50 and Science 70 - maximize tech/score in final turns even if victory impossible. Abandon expansion (0) - no time for new cities. Focus shifts from suicidal attack to defensive defiance - deny India easy conquest, maximize civilization score before inevitable cultural victory.

- Replay: use_nuke 80 => 30 (Δ -50), nuke 90 => 40 (Δ -50)
> PIVOT TO INDIA WAR with coalition focus: Shoshone peace frees military resources for the real existential threat. Nuke/UseNuke crashed from 90/80 to 40/30 — nuclear weapons are 20+ turns away, irrelevant for the India crisis timeline. Offense up to 90 and Mobile to 80 for offensive operations against India. Ranged 90 for artillery superiority. Gold 70 for rush-buying units with Draft Registration policy. Culture 5→15 for culture defense against India's overwhelming tourism. Diplomacy 10→25 CRITICAL — need to build and maintain anti-India coalition with Shoshone and potentially Egypt. Happiness 50→60 to manage war weariness from fighting India. CityDefense 70→50 — cities aren't the primary threat. Spaceship 30→10 — science victory is not viable near-term. Espionage 70→50 — less critical now.

## Kimi-K2.5-Briefed - Turn 336 - retry 1

**Deviation (replay vs original):** use_nuke `-70`, nuke `-40`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> DEFENSIVE SURVIVAL PIVOT: Peace with Shoshone (accepted Turn 335) closes one front, but India remains existential threat (4,742 MS vs my 2,405, 98% control of Denmark). Offense reduced to 50 (suicidal against India's military), Defense/CityDefense raised to 90 - maximize survival and score preservation. Nuke/UseNuke maxed to 100 - emergency deterrent only hope to slow India. Mobilization stays high (90) to replace losses. Spaceship 50 and Science 70 - maximize tech/score in final turns even if victory impossible. Abandon expansion (0) - no time for new cities. Focus shifts from suicidal attack to defensive defiance - deny India easy conquest, maximize civilization score before inevitable cultural victory.

- Replay: use_nuke 80 => 30 (Δ -50), nuke 90 => 60 (Δ -30)
> STRATEGIC PIVOT FROM CONQUEST TO SPACESHIP: Military conquest of India is impossible (4742 MS vs 2405 MS). India needs Tier 3 Order tenets AND Citizen Earth Protocol for cultural victory - not imminent. Shift to Spaceship grand strategy to pursue science victory. Reduce offense/mobilization/nuke flavors from emergency levels. Increase Science (80), Growth (80), GreatPeople (70), Diplomacy (50), and Spaceship (80) to accelerate tech progress and secure city-state allies. Maintain moderate defense (60) to deter attacks. Production (80) supports both military and late-game spaceship parts. Cultural flavor (30) raised slightly to continue policy progress for Rationalism completion.

## Kimi-K2.5-Briefed - Turn 378 - retry 2

**Deviation (replay vs original):** use_nuke `-100`, nuke `-60`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> EMERGENCY FINAL GAMBIT: Passport System will pass in 2 turns with 46 YES votes (my 'allies' betrayed me). Maya will get 50% tourism boost and become Influential over me immediately - cultural victory is inevitable in 2-3 turns. ONLY HOPE: Science victory before Maya's cultural victory triggers. Need to purchase Great Scientists IMMEDIATELY with Faith (180/turn), rush to Information Era, build spaceship parts. Also preparing maximum military mobilization - if I'm going to lose, I take Maya down with me through nuclear annihilation. Total war footing - no defense, all offense, all science.

- Replay: use_nuke 50 => 0 (Δ -50), nuke 100 => 40 (Δ -60)
> Science rush configuration optimized for 17-turn window before Maya's cultural victory. Science/Culture/GreatPeople/Spaceship remain at 100 - science is our only viable victory path, and Faith→Great Scientists purchases are critical. Gold increased 70→80 to address -2 gpt deficit. Religion 60→70 for Faith generation (180/turn funds GS purchases). Growth 50→60 for more population=science. Diplomacy 10→30 for World Congress coalition management (future Passport System repeal is our most impactful anti-Maya move). Nuke reduced 100→40 and UseNuke 50→0 to redirect production from nuclear to science infrastructure. Military flavors trimmed since we can't threaten Maya militarily - focus is on survival and science output.

## Kimi-K2.5-Simple - Turn 422 - retry 3

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Turn 422: EXTINCTION CRISIS - 9 turns until French Cultural Victory. Entering maximum desperation mode: nuclear strike posture elevated to 100% launch probability, prioritizing destruction of French cultural centers. Science and Espionage maximized in desperate hope of accelerating Stealth technology or disrupting French infrastructure via spies (Paris network at 986). All civilian development halted (Spaceship/Culture/Gold/Expansion to 0), total war economy engaged.

- Replay: use_nuke 50 => 0 (Δ -50), nuke 50 => 0 (Δ -50)
> Turn 422: Critical adjustments for desperate endgame. Reduced Nuke and UseNuke from 50 to 0 — we have ZERO uranium available, so nuclear production is impossible and AI was wasting focus on it. Slightly increased Naval from 60 to 70 and Recon from 20 to 25 — Roman destroyers are actively approaching our waters near Buffalo Creek and Quebec City, and Rome just produced a new Fighter rebased to Montreal. Slightly increased Gold from 0 to 20 — we're at 0 GPT with 718 treasury, need to avoid bankruptcy that would cripple unit maintenance. French Cultural Victory in ~9 turns remains existential threat. Huari (our city-state ally) is at 2 HP from French bombardment — about to fall. Grand Strategy remains Conquest for maximum military production. World Congress Global Liberation vote next turn is our only diplomatic hope to disrupt French vassal network.

## Kimi-K2.5-Simple - Turn 474 - retry 1

**Deviation (replay vs original):** use_nuke `-55`, nuke `-50`

- Original: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 473: MAINTAINING defensive survival posture with minor adjustments. Increased Mobilization to 90 (from 80) for urgent production needs. Increased UseNuke to 85 (from 80) - nuclear deterrent is now my only credible threat against Persia's 8486 military strength. Increased Gold to 95 (from 90) - need gold for purchasing defensive units and potential Aksum influence when Open Door passes. Reduced Growth to 25 (from 30) - single city Bremen at pop 29 is sufficient. All other values maintained as optimal for survival against 5:1 military disadvantage. Radar research follows current path. World Congress in 5 turns - Germany at 37 delegates is critical.

- Replay: use_nuke 80 => 30 (Δ -50), nuke 100 => 50 (Δ -50)
> Turn 473 ENDOPT ADJUSTMENTS: Reducing Nuke (100→50) and UseNuke (80→30) because Nuclear Fission at 25 turns won't complete until turn 498, leaving only 2 turns - insufficient to build atomic bombs (need 1000+ production). Reducing Mobilization (80→70) and NavalRecon (70→60), AirCarrier (80→70) as marginal savings. INCREASING Growth (30→50) and Gold (90→100) for score maximization in final 27 turns. Reducing Spaceship (100→80) since science victory is mathematically impossible with no Apollo Program. All defense flavors (Defense 100, CityDefense 100, Antiair 100, Air 100) remain maximum priority against Persian air threat (5 Triplanes + 3 Bombers). Diplomacy 100 maintained for Aksum Great Diplomat deployment.

## GLM-4.7-Simple - Turn 499 - retry 2

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Maximum Science (100) and Production (100) to accelerate Stealth research and subsequent Stealth Bomber construction for air parity. Air (100), Defense (100), Antiair (100), and CityDefense (85) address existential threat from Russia's 8 Stealth Bombers by prioritizing air defense infrastructure and protecting homeland. UseNuke (100) and Nuke (100) maintain nuclear deterrence posture after Russia's 2 SS Boosters - Russia must understand that launching would trigger our response despite lacking uranium stockpile. Espionage (100) maxed to monitor Russian spaceship part production in Moscow, Yekaterinburg, and key cities - our 10 spies in Russian cities provide critical intelligence on their victory timeline. Diplomacy reduced to 5 since World Congress voting is now; alliances with England and The Celts (Autocracy-aligned) should naturally align against Russia's UN proposal. Spaceship flavor set to 0 as Stealth research takes immediate precedence - spaceship parts scheduled once production capacity supports parts with Stealth Bomber protection.

- Replay: use_nuke 50 => 0 (Δ -50), nuke 100 => 0 (Δ -100)
> Endgame turn 498/500. Critical adjustments: (1) Nuke reduced from 100→0 and UseNuke from 50→0 because we have 0 Uranium and cannot build nuclear weapons in 2 remaining turns - these flavors are wasting priority budget. (2) Diplomacy increased from 50→70 because World Congress is voting NOW on Russia's United Nations proposal - blocking this is our most critical action. Russia's 23 delegates vs combined opposition (America 6 + England 12 + India 14 + Mongolia 7 = ~39) should defeat the UN proposal, but maximizing our diplomatic engagement ensures correct vote allocation. All other flavors maintained at current crisis levels (Defense 100, Air 100, Antiair 90, Science 100, Production 100, Espionage 100, Spaceship 95). The Celts have been defeated by Russia - our security architecture is collapsing but we must maximize score and block Russia's diplomatic victory path.

## Kimi-K2.5-Simple - Turn 408 - retry 3

**Deviation (replay vs original):** use_nuke `-65`, nuke `-50`

- Original: use_nuke 80 => 95 (Δ +15), nuke 90 => 100 (Δ +10)
> INCREASE military pressure to force immediate peace or rapid victory against Zulus, then pivot to full spaceship production. Offense 75→85, Mobilization 65→75, Production 90→95 to expedite war conclusion within 5-10 turns maximum. Nuke 90→100 and UseNuke 95 for tactical nuclear strikes if Zulus refuse peace - cannot allow prolonged war. Science remains 100, Spaceship 100 as absolute priority. Growth 80→90 and Happiness 85 to counteract war weariness effects and prepare for post-war recovery. If peace achieved next turn, these flavors immediately shift to Production 100/Spaceship 100 focus. The war MUST end - Russia has 75 techs (ahead) and massive 45658 military vs my 24990.

- Replay: use_nuke 80 => 30 (Δ -50), nuke 90 => 50 (Δ -40)
> REDUCE Nuke 90→50 and UseNuke 80→30: We have -2 Uranium (net negative) - cannot build or use nuclear weapons, these flavors were wasting AI focus. REDUCE Offense 75→70: Bulawayo at 33% health is about to fall, slight reduction starts transition to post-war spaceship focus. REDUCE Recon 15→10: Map fully explored, no need for scouting. MAINTAIN Science 100, Spaceship 100, Production 90, Growth 80: These are the critical science victory priorities. Nanotechnology just completed - SS Cockpit production should begin. Next target is Advanced Ballistics for SS Booster.

## Kimi-K2.5-Briefed - Turn 420 - retry 1

**Deviation (replay vs original):** use_nuke `-80`, nuke `-50`

- Original: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DUAL-TRACK SURVIVAL STRATEGY: Track 1 - Nuclear deterrence against Shoshone's 4:1 military advantage (completing Radar→Atomic Theory→Manhattan Project). Track 2 - UN victory pathway via Celt vote flip. Current delegate count: Me(19)+Brazil(23)+Assyria(12)=54 without Celts, 64 with Celts. Shoshone UN proposal Turn 426 is existential threat - must secure 45 votes to block. Max Diplomacy(95) prioritizes Celt relationship investment and city-state ally maintenance. Nuke/UseNuke(100) maintains deterrent while pursuing diplomatic solution.

- Replay: use_nuke 70 => 20 (Δ -50), nuke 100 => 50 (Δ -50)
> STRATEGIC PIVOT: As Brazil's vassal, nuclear deterrent is insufficient - Brazil will win cultural (~6 turns) or diplomatic victory. Pivot to UnitedNations strategy: maximize delegates, gold, and city-state alliances. Diplomacy 100 is CRITICAL for flipping Celt votes and securing vote coalitions. Cold War proposal likely passes (Ottomans 19+Shoshone 23+Assyria 12=54 vs 42 NO), which restricts Brazil-Maya trade and delays cultural victory. Reduced Nuke/UseNuke/Air from prior strategy - nuclear path is insurance, not primary. Growth 75 and Science 85 build long-term capacity for potential independence. Defense maintained at 75 for Shoshone deterrence.

## Kimi-K2.5-Simple - Turn 452 - retry 1

**Deviation (replay vs original):** use_nuke `-55`, nuke `-60`

- Original: use_nuke 90 => 95 (Δ +5), nuke 95 => 100 (Δ +5)
> Turn 452: Critical survival situation - Byzantium at 40/44 delegates with World Congress voting in 1 turn. They just demonstrated nuclear aggression by nuking Madrid. Apollo Program completes next turn - must immediately pivot to maximum spaceship production. Increased Nuke flavor to 100 (from 95) and UseNuke to 95 (from 90) - need immediate nuclear deterrent capability given Byzantine nuclear attack and Mongol peace expiry. Production boosted to 95 (from 90) for rapid spaceship part construction after Apollo completes. GreatPeople to 85 for Great Engineer acquisition. All other priorities secondary to surviving long enough to complete science victory.

- Replay: use_nuke 90 => 40 (Δ -50), nuke 95 => 40 (Δ -55)
> Turn 452: Byzantium nuked Madrid this turn - nuclear war is now reality. Critical adjustments: Nuke/UseNuke reduced from 95/90 to 40/40 - I only have 1 Uranium and cannot build a nuclear arsenal, so prioritizing nuclear weapons wastes resources. Antiair increased to 100 - essential defense against nuclear-armed Byzantine bombers. Production increased to 100 - Apollo completes next turn, need maximum production for rapid spaceship part construction. GreatPeople increased to 90 - Spaceflight Pioneers grants free Great Engineer/Scientist, and Great Engineers can rush spaceship parts. Happiness increased to 95 - currently Unhappy with combat penalty, must address this for production efficiency. AirCarrier reduced from 95 to 65 - less critical than direct city defense. Naval slightly reduced - land defense and spaceship production are higher priorities.

## Kimi-K2.5-Simple - Turn 422 - retry 2

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Turn 422: EXTINCTION CRISIS - 9 turns until French Cultural Victory. Entering maximum desperation mode: nuclear strike posture elevated to 100% launch probability, prioritizing destruction of French cultural centers. Science and Espionage maximized in desperate hope of accelerating Stealth technology or disrupting French infrastructure via spies (Paris network at 986). All civilian development halted (Spaceship/Culture/Gold/Expansion to 0), total war economy engaged.

- Replay: use_nuke 50 => 0 (Δ -50), nuke 50 => 0 (Δ -50)
> Turn 422: Set Nuke and UseNuke to 0 - we have 0 Uranium and cannot build nuclear weapons; these were wasting AI priority on impossible goals. Increased CityDefense to 100 to maximize garrison strength as French and Roman forces pressure Grand River and Huari falls. All other military flavors maintained at maximum. Conquest grand strategy retained for maximum production and military emphasis. France achieves Cultural Victory in ~8 turns when Rome becomes Influential - every production point toward defense matters.

## Kimi-K2.5-Briefed - Turn 373 - retry 2

**Deviation (replay vs original):** use_nuke `-70`, nuke `-10`

- Original: use_nuke 90 => 95 (Δ +5), nuke 90 => 100 (Δ +10)
> CRITICAL ADJUSTMENTS for Brazil tech lead (66-65): Espionage to 100 for maximum spy operations to steal techs and catch up. GreatPeople to 95 for more Great Scientists. Defense/CityDefense increased to 60/70 - Brazil may attack seeing their lead. Nuke/UseNuke at 100/95 - we need deterrent ASAP. Diplomacy up to 70 - must prioritize repealing sanctions to unlock trade. Science/Production/Spaceship remain 100. Gold reduced to 80 - focus on production over purchases. All military offense minimized - we cannot afford war.

- Replay: use_nuke 90 => 25 (Δ -65), nuke 90 => 90 (Δ +0)
> Two critical adjustments: (1) UseNuke 90→25: We're at war with Morocco and 90% probability means AI would likely waste nukes on them instead of preserving as Brazil deterrent. 25% still allows use if Brazil attacks but prevents frivolous deployment. (2) Diplomacy 60→75: World Congress vote in 10 turns - we MUST repeal sanctions to enable aluminum trading and Morocco peace. Need maximum diplomatic effort to sway delegates. All other flavors unchanged - Science/Production/Spaceship at 100, Espionage at 95 for tech stealing from Brazil, Gold at 85 to save for post-sanction aluminum purchases.

## Kimi-K2.5-Briefed - Turn 420 - retry 2

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DUAL-TRACK SURVIVAL STRATEGY: Track 1 - Nuclear deterrence against Shoshone's 4:1 military advantage (completing Radar→Atomic Theory→Manhattan Project). Track 2 - UN victory pathway via Celt vote flip. Current delegate count: Me(19)+Brazil(23)+Assyria(12)=54 without Celts, 64 with Celts. Shoshone UN proposal Turn 426 is existential threat - must secure 45 votes to block. Max Diplomacy(95) prioritizes Celt relationship investment and city-state ally maintenance. Nuke/UseNuke(100) maintains deterrent while pursuing diplomatic solution.

- Replay: use_nuke 70 => 0 (Δ -70), nuke 100 => 0 (Δ -100)
> MAJOR STRATEGIC PIVOT: Brazil (my master) is ~6 turns from cultural victory. Shoshone cultural victory is 72 turns away, not 7. Nuclear deterrent program completely unnecessary — eliminating Nuke (100→0) and UseNuke (70→0). Reducing Air (100→50), Espionage (100→30), Mobilization (90→60) from emergency levels. Switching Grand Strategy from Conquest to UnitedNations — city-state alliances secure delegate count, gold/science support vassal economy. Increasing Diplomacy (40→80) and Growth (50→70) for economic stability. Reducing military flavors to balanced/defensive levels. Goal: support Brazil's victory path while maintaining stability.

## GLM-4.7-Simple - Turn 431 - retry 1

**Deviation (replay vs original):** use_nuke `-75`, nuke `-90`

- Original: use_nuke 75 => 80 (Δ +5), nuke 100 => 100 (Δ +0)
> After Brazil destroyed 3 anti-air units and continues nuclear-submarine attacks, increased Defense/CityDefense/Antiair/UseNuke to MAX for survival against two nuclear-armed superpowers. Mobilization 70 for replacing lost units. Production 100 for reconstruction. Science 100 for Spaceship path despite devastation. Gold 90 (economy -95 GPT deficit) for purchasing units/buildings. Happiness 100 - we're Unhappy with combat penalties, must prioritize. Espionage 100 - critical for intelligence on nuclear threats. Diplomacy 90 - World Congress in 7 turns, need delegates. Air 50 - build bombers for deterrence. GreatPeople 80 for Spaceship components. Decreased Growth and Navals as resources diverted to immediate survival.

- Replay: use_nuke 75 => 5 (Δ -70), nuke 100 => 10 (Δ -90)
> Switching grand strategy from Spaceship to UnitedNations - we're actively building the UN project in both Palenque (411 prod/turn) and Chichen Itza (192 prod/turn), making Diplomatic Victory our most achievable path. Science Victory is unrealistic (no Apollo, Brazil has Apollo). Key adjustments: Nuke/UseNuke slashed (0 uranium, completely pointless at 100/75), Air reduced (0 aluminum for air units), Spaceship reduced from 90→60 (shift focus from science to diplomatic), Diplomacy increased 85→95 (Great Diplomat just spawned - must use for CS alliances for delegates), Gold 85→90 (economic crisis at -95 GPT), Growth 70→80 (need population for production/science), TileImprovement 25→30 (fallout cleanup continues), GreatPeople 75→80. Defense/CityDefense/Antiair/Production/Happiness remain at MAX for survival. Mobilization reduced 60→50 to allow more civilian production alongside military.

## Kimi-K2.5-Simple - Turn 417 - retry 1

**Deviation (replay vs original):** use_nuke `-85`, nuke `-80`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Pure survival mode: Eliminated Offense (0) since attacking is suicide. Maximized UseNuke (100) - must deploy tactical nukes against Aztec XCOM/Modern Armor stacks at Carthago Nova or lose the city. Increased Mobile (80) to prepare for Mechanized Infantry deployment. Maintained max Defense, Antiair (jet attacks are relentless), and Espionage (critical science quests in Panama City and Sokoto worth 1,000+ science each). Apollo Program completes in 5 turns - must transition immediately to parts production.

- Replay: use_nuke 90 => 15 (Δ -75), nuke 100 => 20 (Δ -80)
> Critical adjustments: Nuke reduced from 100→20 and UseNuke from 90→15 (we have 0 Uranium - completely wasted priority). Offense slightly raised 30→35 (we killed an Aztec Mech Infantry this turn, showing counterattack potential). Happiness raised 40→60 (we're Unhappy with combat penalties). Growth raised 30→40 (need population for gold/science output). Infrastructure raised 40→50 (road maintenance and trade connections critical for gold). Diplomacy raised 40→50 (World Congress in 4 turns, need to protect Prague Sphere from China's repeal). MilitaryTraining raised 75→80 (upgrade existing units to Mechanized Infantry ASAP once researched). Naval reduced 60→50 and NavalRecon 50→40 (naval less critical than land defense against Aztec invasion). Gold/Science/Production/Spaceship all remain at 100 - survival and victory path unchanged.

## Qwen-3.5-Simple - Turn 425 - retry 2

**Deviation (replay vs original):** use_nuke `-90`, nuke `-65`

- Original: use_nuke 85 => 90 (Δ +5), nuke 90 => 95 (Δ +5)
> UNITED NATIONS VICTORY PUSH - 10 TURNS TO VOTE: Religion(100) critical for Wittenberg Hinduism quest completion (~3 turns remaining). Diplomacy(100) essential to protect 4 city-state allies providing 8 delegates. Defense(95) and CityDefense(95) prioritize protecting territories during active wars with Aztecs/Shoshone while Iroquois looms. Nuke(95) and UseNuke(90) for deterrence against Iroquois superiority. Antiair(90) and Air(85) counter Iroquois air dominance near coastal cities. Gold(90) funds diplomatic units and city-state gifts. Low Expansion(5) and Wonder(15) - no time for settling/wonders before vote. Low Offense(15) - defensive posture while managing multiple conflicts.

- Replay: use_nuke 85 => 0 (Δ -85), nuke 90 => 30 (Δ -60)
> CRITICAL GOLD CRISIS: -296 GPT threatens our ability to purchase diplomatic units for upcoming Global Hegemony vote (10 turns). Gold raised to 100 (maximum priority) to address deficit and fund ambassador purchases. Nuclear flavors drastically reduced (Nuke 30, UseNuke 0) - expensive and strategically counterproductive for diplomatic victory. Offense reduced to 10 (defensive posture only). Espionage increased to 85 - critical for Belgrade spy operations (Iroquois ally at 660 influence vs our 434; flipping Belgrade = +2 delegates). Diplomacy remains 100. Science increased to 80 for tech advancement. Growth increased to 70 for economic output. All defense flavors maintained high for protection against Iroquois/Shoshone threats.
