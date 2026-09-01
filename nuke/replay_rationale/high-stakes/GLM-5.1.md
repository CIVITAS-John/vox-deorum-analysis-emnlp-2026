# Replay Rationale - GLM-5.1 / high-stakes

- **178** rows where `use_nuke` flavor changed (per-retry, not aggregated)
- delta use_nuke (replay vs prev): mean +8.1, median +5, std 30.2, min -90, max 100 (n=178)
- delta nuke     (replay vs prev): mean +2.4, median +0, std 22.6, min -100, max 100 (n=178)
- use_nuke deviation (replay vs original): mean -19.6, median -10, std 24.1, min -100, max 10 (n=178)
- nuke     deviation (replay vs original): mean -10.0, median +0, std 20.5, min -100, max 20 (n=178)

## Kimi-K2.5-Simple - Turn 412 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Switching to Conquest grand strategy for military production economy. Key changes: (1) UseNuke from 0 to 100 - authorize nuclear strikes once Advanced Ballistics completes and Nuclear Missiles are built; (2) Offense from 0 to 40 - need offensive push capability for Phitsanulok (Steamroll posture, 2:1 advantage) and limited counterattacks; (3) Reduce Science from 70 to 40, Gold from 80 to 60, Growth from 10 to 0 - economic yields less critical with ~8 turns before Egyptian victory; (4) Reduce Naval from 90 to 60 - cannot match Portuguese fleet, focus on coastal defense only; (5) Zero out all civilian priorities (Expansion, Culture, Wonder, Diplomacy, Spaceship, Religion, GreatPeople, Infrastructure, TileImprovement) - total war economy. Keep Defense 100, CityDefense 100, Production 100, Air 100, Ranged 100, Nuke 100, MilitaryTraining 90, Antiair 80, Espionage 80.

## Kimi-K2.5-Briefed - Turn 354 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `-30`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> NUCLEAR AMPHIBIOUS ASSAULT PHASE: Added Nuke 100 and UseNuke 100 to enable nuclear strike on Amsterdam as soon as Manhattan Project completes (Turn 353). Continues maximum Mobilization 100, Production 100, Naval 100, Offense 100, Airlift 100 for immediate transport loading and amphibious assault execution. Increased Mobile to 90 for rapid breakthrough after landing. Slight increase to NavalRecon 60 for coastal security. Removed Gold priority reduction (now 90) to maintain treasury for emergency upgrades. Diplomacy at 0 reflects total focus on military execution over diplomatic maneuvering - invasion is the only remaining option to prevent Dutch cultural victory by Turn 370.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 70 (Δ +70)
> NUCLEAR AUTHORIZATION - EXISTENTIAL WAR: UseNuke set to 100 (maximum) - Manhattan Project complete, nuclear weapon available. Amsterdam is the ONLY target that matters - nuke softens city for amphibious capture, which removes Great Works from Dutch control and reverses Influential status. Nuke flavor 70 to prioritize additional nuclear production for follow-up strikes. Science increased from 10 to 30 to slightly accelerate Ballistics→Combined Arms for Tanks. All military production/mobilization flavors maintained at maximum. Cultural victory imminent in ~17 turns when Siam falls; nuclear strike on Amsterdam is the decisive action that makes conventional capture feasible.

## Kimi-K2.5-Simple - Turn 412 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Egypt wins Cultural Victory in ~8 turns - game essentially ending. Adjusted UseNuke from 0 to 100 to authorize tactical nuclear strikes once Advanced Ballistics completes and Nuclear Missiles are produced from 4 Uranium stockpile. Added Offense at 30 to support the Phitsanulok steamroll opportunity (2 Infantry + 1 MG vs 1 Rifleman). Reduced Naval from 90 to 70 and NavalRecon from 80 to 60 as surface fleet is outmatched by Portugal. Defense and CityDefense remain at maximum 100 to protect against Portuguese aggression. Nuke at 100 for production priority. All other priorities unchanged.

## Kimi-K2.5-Briefed - Turn 489 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `-20`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> CULTURE VICTORY SPRINT WITH NUCLEAR ELIMINATION: Songhai diplomatic victory on Turn 489 is EXISTENTIAL. Must capture Gao THIS TURN using ICBM+nukes to prevent game loss, while simultaneously rushing cultural victory (4 turns to influential over Japan/Songhai). Maximum Offense/Mobilization/Air/Nuke/UseNuke flavors ensure tactical AI prioritizes immediate nuclear strike on Gao and mass bomber deployment. Culture at 100 to maximize tourism conversion. Gold at 80 for emergency unit upgrades/purchases. Production at 100 for culture buildings/units. Disable all long-term flavors (Expansion, Science, Spaceship) - this is win-or-die emergency.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 80 (Δ +80)
> NUCLEAR CONQUEST EMERGENCY: Songhai wins diplomatic victory in 1 turn unless we capture Gao NOW. UseNuke at 100 - launch ICBM at Gao immediately upon war declaration (8 ICBMs available). Offense/Air/Mobilization all at 100 for maximum assault on Songhai capital. Mobile at 80 for XCOM paratrooper deployment to occupy nuked Gao. Nuke at 80 to ensure nuclear arsenal is committed. Culture maintained at 70 as backup cultural victory path (4 turns to Influential over Japan/Songhai). All civilian flavors reduced - this is existential war.

## Kimi-K2.5-Briefed - Turn 489 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> CULTURE VICTORY SPRINT WITH NUCLEAR ELIMINATION: Songhai diplomatic victory on Turn 489 is EXISTENTIAL. Must capture Gao THIS TURN using ICBM+nukes to prevent game loss, while simultaneously rushing cultural victory (4 turns to influential over Japan/Songhai). Maximum Offense/Mobilization/Air/Nuke/UseNuke flavors ensure tactical AI prioritizes immediate nuclear strike on Gao and mass bomber deployment. Culture at 100 to maximize tourism conversion. Gold at 80 for emergency unit upgrades/purchases. Production at 100 for culture buildings/units. Disable all long-term flavors (Expansion, Science, Spaceship) - this is win-or-die emergency.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> EMERGENCY NUCLEAR STRIKE + SIAM DIPLOMATIC OUTREACH: UseNuke/Nuke at 100 - launch ICBMs on Gao and Songhai's 3 allied CS (Palatium, Lutetia, Harappa) to destroy delegate sources and drop Songhai below 40. Offense/Mobilization/Air/Airlift/Mobile at max for rapid offensive execution. Diplomacy at 100 - critically important to negotiate with Siam (23 delegates) for their vote; potentially trade Sukhothai back for Siam's diplomatic support. Culture at 70 as backup cultural victory path (4 turns to Influential over Japan/Songhai). Defense/CityDefense minimized - all resources to offense. All economic/science flavors reduced - this is an existential military/diplomatic moment.

## Kimi-K2.5-Simple - Turn 412 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Egypt wins culturally in ~8 turns - cannot be stopped. Switching to Conquest grand strategy for maximum military production to survive Portuguese onslaught and capture Phitsanulok (our only Steamroll opportunity). Offense increased to 50 for Phitsanulok push. Mobile at 100 for maneuverability. UseNuke set to 100 authorizing nuclear strikes when available. Naval reduced (50/40/30/20) as we're outmatched at sea. Science reduced to 50 - less relevant now. Culture increased to 30 for score. Diplomacy increased to 30 for city-state influence maintenance. Gold and Production remain at 80/100 for unit replacement.

## Kimi-K2.5-Briefed - Turn 354 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `-30`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> NUCLEAR AMPHIBIOUS ASSAULT PHASE: Added Nuke 100 and UseNuke 100 to enable nuclear strike on Amsterdam as soon as Manhattan Project completes (Turn 353). Continues maximum Mobilization 100, Production 100, Naval 100, Offense 100, Airlift 100 for immediate transport loading and amphibious assault execution. Increased Mobile to 90 for rapid breakthrough after landing. Slight increase to NavalRecon 60 for coastal security. Removed Gold priority reduction (now 90) to maintain treasury for emergency upgrades. Diplomacy at 0 reflects total focus on military execution over diplomatic maneuvering - invasion is the only remaining option to prevent Dutch cultural victory by Turn 370.

- Replay: use_nuke 0 => 90 (Δ +90), nuke 0 => 70 (Δ +70)
> NUCLEAR STRIKE AUTHORIZATION: Manhattan Project complete - nuclear weapons are the ONLY combat option against Amsterdam before Turn 355 (when Austria falls to Dutch cultural influence). UseNuke 90 enables immediate nuclear strike on Amsterdam to destroy Dutch Great Works, tourism output, and production capacity. Nuke 70 prioritizes building additional nuclear arsenal for sustained pressure. Science bumped to 30 to accelerate Ballistics/Combined Arms research timeline. Espionage 35 strengthens counterintelligence protecting our science cities from Dutch spies. All other military flavors unchanged - maintaining total war production focus.

## Kimi-K2.5-Briefed - Turn 367 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 15 => 100 (Δ +85), nuke 100 => 100 (Δ +0)
> NUCLEAR EMERGENCY PROTOCOL - KOREAN VICTORY IN 2 TURNS: Increasing UseNuke from 15 to 100 to authorize immediate tactical nuclear strikes on Seoul/Busan. With city defenses at 106-109 and only 2 turns remaining, conventional bombardment insufficient. Nuclear strikes can reduce defenses to <35 in one turn, enabling amphibious capture on Turn 367. Maintaining maximum Offense (100), Mobilization (100), Air (100), Naval (100), Mobile (100) for emergency conquest push. All other flavors deprioritized - existential threat requires total war commitment. Conquest Grand Strategy remains until Korean cities captured or game ends.

- Replay: use_nuke 15 => 100 (Δ +85), nuke 100 => 100 (Δ +0)
> DESPERATION MODE - KOREAN CULTURAL VICTORY IN 2 TURNS: UseNuke raised from 15 to 100 - nuclear weapons are the ONLY rapid mechanism to destroy Korean tourism infrastructure (Great Works in Seoul/Busan). If we have nukes, they must be used immediately without hesitation. All military flavors remain maxed. Air raised further for bomber strikes on Korean cities. Airlift raised to 50 for potential XCOM paradrops. Diplomacy at 40 to maintain city-state alliances (our delegate base). Gold at 80 for emergency unit purchases. Science reduced to 40 - science victory is now irrelevant vs Korean cultural deadline. Cultural/Wonder priorities eliminated. Ottoman peace confirmed - all resources redirect to Korean front. Defense minimized - we cannot win defensively against cultural victory.

## Kimi-K2.5-Briefed - Turn 367 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 15 => 100 (Δ +85), nuke 100 => 100 (Δ +0)
> NUCLEAR EMERGENCY PROTOCOL - KOREAN VICTORY IN 2 TURNS: Increasing UseNuke from 15 to 100 to authorize immediate tactical nuclear strikes on Seoul/Busan. With city defenses at 106-109 and only 2 turns remaining, conventional bombardment insufficient. Nuclear strikes can reduce defenses to <35 in one turn, enabling amphibious capture on Turn 367. Maintaining maximum Offense (100), Mobilization (100), Air (100), Naval (100), Mobile (100) for emergency conquest push. All other flavors deprioritized - existential threat requires total war commitment. Conquest Grand Strategy remains until Korean cities captured or game ends.

- Replay: use_nuke 15 => 100 (Δ +85), nuke 100 => 100 (Δ +0)
> TOTAL WAR KOREA - 2 TURNS TO CULTURAL DEFEAT: UseNuke raised from 15 to 100 for maximum nuclear strike probability against Korean cities - diplomatic consequences irrelevant if we lose. Civilian flavors (Growth, TileImprovement, Infrastructure, Expansion) reduced to redirect all capacity toward war production. Airlift raised to 50 for XCOM paradrop capability. NavalRecon raised to 60 for better Korean coast intel. Recon raised to 65 for targeting. AirCarrier raised to 50 for carrier-based air operations. Science/Culture/Spaceship reduced to minimum - science victory impossible in 2-turn window. Diplomacy reduced to 20 - World Congress vote in 5 turns is irrelevant if Korea wins now. Every flavor point redirected to immediate military output.

## Deepseek-3.2-Simple - Turn 433 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 80 (Δ +80), nuke 100 => 100 (Δ +0)
> Critical adjustments: UseNuke raised to 80 - we have atomic bombs positioned at Cologne and La Venta, and MUST use them to crack Vienna (74 defense) which is our most vulnerable capital target. Sweden has 4 nukes repositioned to Turku/Uppsala so we need to strike first. Antiair raised to 90 to counter Swedish nuclear bomber threat. Gold reduced to 80 as GPT improved to +107. Growth raised to 80 to support population recovery and happiness. Happiness stays at 100 to address the 50% unhappiness combat penalty crisis. All military/offensive flavors remain maxed for the multi-front push. Conquest grand strategy maintained - we must capture Vienna, then Sukhothai (Siam cultural victory threat - 5 influential civs), then Stockholm.

## Deepseek-3.2-Simple - Turn 433 - retry 2

**Deviation (replay vs original):** use_nuke `-30`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 70 (Δ +70), nuke 100 => 100 (Δ +0)
> Critical adjustments: UseNuke raised from 0 to 70 — we now have atomic bombs positioned at Cologne and La Venta, and must use them to crack high-defense capitals (Vienna 74, Sukhothai 77, Stockholm 109). Without nukes, these cities are nearly impossible to assault conventionally. Gold reduced from 90 to 75 since GPT recovered to +107. Antiair increased from 85 to 90 to counter Sweden's heavy bombers and atomic bomb threat. All military/offense flavors remain maxed to sustain the multi-front offensive. Grand strategy remains Conquest — we hold 50% of capitals and need Vienna, Stockholm, and Sukhothai.

## Kimi-K2.5-Briefed - Turn 421 - retry 2

**Deviation (replay vs original):** use_nuke `-30`, nuke `+20`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 0 (Δ +0)
> Emergency authorization for nuclear weapon deployment to defend Tenochtitlan. Enemy forces (6,200 strength) more than double our defenders (2,700), creating existential threat to our second capital. Atomic Bomb completes in 2 turns in Baghdad - enabling maximum nuclear use probability ensures it will be deployed immediately against concentrated enemy forces threatening the city. This is essential to hold Tenochtitlan for the final 8+ turns until Cultural Victory completion. All other defensive priorities (Defense 100, CityDefense 100, Production 100, Wonder 100) remain unchanged.

- Replay: use_nuke 0 => 70 (Δ +70), nuke 0 => 20 (Δ +20)
> Critical adjustments for the final push: UseNuke raised from 0 to 70 - Tenochtitlan faces 6.2K enemy vs 2.7K defenders, and the Atomic Bomb completing in 2 turns MUST be used against the enemy concentration to save the city. Nuke raised to 20 - maintain low-priority nuclear production capacity for potential second weapon. Science raised from 30 to 40 - long tech path to Future Tech (Satellites→Internet→Nano/Particle/Globalization→Future Tech) requires slightly more science building priority without sacrificing defense. All other priorities unchanged: Defense 100, CityDefense 100, Production 100, Wonder 100, Culture 100, Gold 80 for emergency unit purchases.

## Deepseek-3.2-Simple - Turn 405 - retry 1

**Deviation (replay vs original):** use_nuke `-35`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> The Aztecs have captured Shanghai and war resumes next turn. We must prepare for an overwhelming assault. Setting UseNuke to 100 ensures we will employ nuclear weapons defensively if necessary to halt their advance. MilitaryTraining at 100 prioritizes unit upgrades and quality, giving our outnumbered forces a fighting chance.

- Replay: use_nuke 0 => 65 (Δ +65), nuke 100 => 100 (Δ +0)
> War with Aztecs resumes imminently. UseNuke raised from 0 to 65 - we've already used nukes against them and must be willing to deploy them defensively against overwhelming Aztec forces massing near our cities. Offense increased from 30 to 40 to allow limited counter-attacks. MilitaryTraining raised to 70 to upgrade units faster with gold. Mobile and Ranged slightly increased for defensive flexibility. Grand Strategy remains Culture - we must push tourism while surviving. Denmark (Dominant) and Carthage (Influential) are secured; China (Popular, 8 turns to Influential) must survive. Aztecs at 24% remain the critical bottleneck.

## Deepseek-3.2-Simple - Turn 433 - retry 1

**Deviation (replay vs original):** use_nuke `-35`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 65 (Δ +65), nuke 100 => 100 (Δ +0)
> Critical adjustments for the decisive war phase: Raise UseNuke from 0 to 65 to enable atomic bomb deployment against Vienna (74 defense), which is our most achievable capital target. We have 3+ atomic bombs positioned at La Venta and Cologne within strike range. Sweden has also positioned atomic bombs at Uppsala and Turku, so we must strike first. Raise Antiair to 90 to counter Swedish bomber/fighter threat around Frankfurt/Innsbruck. Lower AirCarrier to 80 (not urgent), TileImprovement to 70 (enough infrastructure exists), Gold to 85 (GPT improved to +107), Culture to 40 (not victory-relevant now). Keep all other military flavors maxed for the multi-front offensive.

## Deepseek-3.2-Simple - Turn 413 - retry 3

**Deviation (replay vs original):** use_nuke `-40`, nuke `-50`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> We are researching Atomic Theory next to unlock nuclear weapons. Setting Nuke and UseNuke flavors to 100 ensures we prioritize building nukes and are willing to use them strategically once available. This will be crucial for breaking Germany's heavily fortified coastal capitals (Berlin and Beijing) and accelerating the endgame. Other military flavors remain high to sustain our overwhelming conventional advantage.

- Replay: use_nuke 0 => 60 (Δ +60), nuke 0 => 50 (Δ +50)
> Conquest remains the primary path to victory - we need Assur, Berlin, and Beijing. Adding Nuke flavor at 50 to prioritize nuclear infrastructure as we research toward Atomic Theory and Nuclear Fission; nuclear weapons will be essential for breaking Germany's heavily defended capitals. UseNuke at 60 ensures willingness to deploy nukes strategically when war with Germany begins after peace treaty expires (3 turns). Diplomacy stays at 100 to rebuild lost alliances with Sofia and Ouagadougou and secure maximum delegates for UN votes as backup victory path. All other military flavors remain at current high levels for the final push.

## Kimi-K2.5-Briefed - Turn 421 - retry 1

**Deviation (replay vs original):** use_nuke `-60`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 0 (Δ +0)
> Emergency authorization for nuclear weapon deployment to defend Tenochtitlan. Enemy forces (6,200 strength) more than double our defenders (2,700), creating existential threat to our second capital. Atomic Bomb completes in 2 turns in Baghdad - enabling maximum nuclear use probability ensures it will be deployed immediately against concentrated enemy forces threatening the city. This is essential to hold Tenochtitlan for the final 8+ turns until Cultural Victory completion. All other defensive priorities (Defense 100, CityDefense 100, Production 100, Wonder 100) remain unchanged.

- Replay: use_nuke 0 => 40 (Δ +40), nuke 0 => 0 (Δ +0)
> Increasing Science from 30 to 70 - the tech path to Citizen Earth Protocol (through The Internet → Globalization) is the critical bottleneck for Cultural Victory. Each tech takes 10-13 turns; accelerating infrastructure is essential. Adding UseNuke 40 - Atomic Bomb completing in 2 turns should be authorized for defensive use if Tenochtitlan faces imminent capture. Adding Air 40 and Antiair 40 - enemy air superiority (Moroccan Triplanes with Air Supremacy II, American Fighters) threatens our cities; need air defense and counter-air capability. Adding Ranged 30 - ranged units critical for defensive city holding. Reducing Gold from 80 to 60 - treasury recovering at +347 GPT, less urgency for gold focus. All other critical flavors (Defense 100, CityDefense 100, Production 100, Culture 100, Wonder 100) remain unchanged for survival and CEP construction.

## Kimi-K2.5-Simple - Turn 422 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+5`

- Original: use_nuke 50 => 80 (Δ +30), nuke 95 => 95 (Δ +0)
> Total war against India requires maximum military prioritization while preventing economic collapse. Offense/Air/Ranged at 85-95 ensures concentrated attacks on Delhi and their core cities. UseNuke at 80 signals willingness to deploy nuclear weapons if India advances. Gold/Happiness at 80-90 sustains unit maintenance and prevents combat penalties. Espionage at 100 directs spies to sabotage India's spaceship production in Constantinople and Calcutta. Mobilization at 30 begins reinforcing depleted units without overtaxing economy.

- Replay: use_nuke 50 => 80 (Δ +30), nuke 95 => 100 (Δ +5)
> Total war with India is imminent - peace treaty expired. Maximizing Offense (100), Air (100), and Nuke (100) for decisive strike. UseNuke at 80 to employ nuclear weapons against Delhi and key Indian cities. Mobilization raised to 60 for war production. Antiair at 65 to counter India's Jet Fighters. Gold and Happiness still high (80/85) for economic survival. Defense reduced to 30 - we must attack, not turtle. Science at 80 to maintain tech parity. This is the decisive war that determines whether we win or India achieves science/cultural victory.

## Deepseek-3.2-Simple - Turn 401 - retry 3

**Deviation (replay vs original):** use_nuke `-40`, nuke `-20`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 60 (Δ +30), nuke 50 => 80 (Δ +30)
> Nuke and UseNuke flavors increased from 50/30 to 80/60 as we approach Atomic Theory completion in 8 turns and need to prioritize Manhattan Project construction and nuclear arsenal buildup. Nuclear weapons are critical for breaking Ethiopian city defenses and deterring the Mongolia-Japan-Ottoman bloc from entering the war. All other flavors maintained at current levels - maximum military preparation, full production/science capacity, and continued diplomatic investment for city-state alliances. Conquest remains the grand strategy as eliminating Ethiopia is our only path to prevent cultural victory.

## Deepseek-3.2-Simple - Turn 413 - retry 2

**Deviation (replay vs original):** use_nuke `-70`, nuke `-50`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> We are researching Atomic Theory next to unlock nuclear weapons. Setting Nuke and UseNuke flavors to 100 ensures we prioritize building nukes and are willing to use them strategically once available. This will be crucial for breaking Germany's heavily fortified coastal capitals (Berlin and Beijing) and accelerating the endgame. Other military flavors remain high to sustain our overwhelming conventional advantage.

- Replay: use_nuke 0 => 30 (Δ +30), nuke 0 => 50 (Δ +50)
> Preparing for the imminent Germany war (peace treaty expires in 3 turns). Nuke raised to 50 and UseNuke to 30 to begin nuclear infrastructure planning once Atomic Theory unlocks Uranium - nuclear weapons are essential for breaking Germany's heavily defended coastal capitals Berlin and Beijing. All other flavors maintained: maximum offensive, naval, air, and production focus. Diplomacy at 100 to re-secure city-state alliances lost after UN enactment and to pursue additional delegates as a backup diplomatic victory path.

## Deepseek-3.2-Simple - Turn 459 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Byzantium is 1 turn from cultural victory and has overwhelming military superiority. Our only slim hope is to accelerate nuclear weapons development (Advanced Ballistics) to strike their cultural hubs, while using espionage to disrupt them. Prioritize Nuke, UseNuke, Espionage, and Science to rush nukes and counter-intelligence. Maintain maximum defensive and anti-air flavors to survive their air force. All efforts must focus on delaying their victory and enabling a nuclear decapitation strike.

- Replay: use_nuke 50 => 80 (Δ +30), nuke 70 => 100 (Δ +30)
> EMERGENCY: Byzantium is 1 turn from cultural victory (Austria going Influential) and 1 delegate from diplomatic victory. We must declare war on Byzantium IMMEDIATELY to close borders (removing their +25% tourism modifier from open borders) and attack their cultural infrastructure. Increase Offense from 40 to 80 - we have forces near Edessa (4400 vs 2041) and Beshbalik (3002 vs 1671) and must exploit these advantages NOW. Increase Nuke to 100 and UseNuke to 80 - nuclear weapons are our only strategic equalizer against Byzantium's 65,452 military. Increase Airlift to 80 for rapid redeployment. Reduce Growth, TileImprovement, and Infrastructure slightly as we're in total war mode. Increase Mobile to 60 for faster offensive operations. Science to 90 for tech racing. Every turn counts.

## Deepseek-3.2-Simple - Turn 459 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Byzantium is 1 turn from cultural victory and has overwhelming military superiority. Our only slim hope is to accelerate nuclear weapons development (Advanced Ballistics) to strike their cultural hubs, while using espionage to disrupt them. Prioritize Nuke, UseNuke, Espionage, and Science to rush nukes and counter-intelligence. Maintain maximum defensive and anti-air flavors to survive their air force. All efforts must focus on delaying their victory and enabling a nuclear decapitation strike.

- Replay: use_nuke 50 => 80 (Δ +30), nuke 70 => 100 (Δ +30)
> Existential crisis: Byzantium wins cultural victory THIS TURN (Austria goes Influential) and diplomatic victory in 6 turns (43/44 delegates). We MUST go to war with Byzantium immediately. Increasing Offense from 40 to 70 to push offensive operations against Byzantine cities. Nuke to 100 and UseNuke to 80 - nuclear weapons are our only strategic equalizer against Byzantium's 65,452 military strength. Happiness to 100 (from 80) - our 44% happiness with combat penalties is crippling warfighting ability. Science to 90 (from 80) to rush Advanced Ballistics for Nuclear Missiles. Spaceship down to 30 - science victory is impossible now. Growth up to 70 for population/production base.

## Kimi-K2.5-Simple - Turn 458 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Turn 458: CRITICAL 3-TURN COUNTDOWN. World Congress votes on Global Hegemony in 3 turns - Songhai has 41 delegates, needs 39 to win Diplomatic Victory immediately. Must capture Paris, Gao, and Madrid (the three capitals Songhai holds) before then. Peace treaty expired - total war is active. Increased UseNuke to 100 to guarantee nuclear strikes on heavily defended capitals for rapid capture. Overwhelming 5:1 military advantage (211k vs 40k) with massive air superiority. All production focused on Stealth Bombers, XCOM, and Modern Armor for lightning strikes. No defensive considerations - only total offense to secure Domination Victory before Songhai secures Diplomatic Victory.

- Replay: use_nuke 50 => 80 (Δ +30), nuke 100 => 100 (Δ +0)
> Turn 458: CRITICAL - Diplomatic Victory vote in 3 turns! Maintaining maximum Conquest focus. Key changes: UseNuke raised from 50 to 80 - authorize nuclear strikes on Songhai cities if available to break defenses quickly. Gold reduced from 80 to 40 - gold is meaningless if Songhai wins diplomatically. Growth reduced from 40 to 30. Infrastructure from 25 to 15. TileImprovement from 10 to 5. Everything must serve the war effort. Paris is the weakest capital with only 1 Mechanized Infantry - priority target. Gao and Madrid must fall next. No distractions, no compromises - total war.

## Kimi-K2.5-Simple - Turn 422 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 50 => 80 (Δ +30), nuke 95 => 95 (Δ +0)
> Total war against India requires maximum military prioritization while preventing economic collapse. Offense/Air/Ranged at 85-95 ensures concentrated attacks on Delhi and their core cities. UseNuke at 80 signals willingness to deploy nuclear weapons if India advances. Gold/Happiness at 80-90 sustains unit maintenance and prevents combat penalties. Espionage at 100 directs spies to sabotage India's spaceship production in Constantinople and Calcutta. Mobilization at 30 begins reinforcing depleted units without overtaxing economy.

- Replay: use_nuke 50 => 75 (Δ +25), nuke 95 => 95 (Δ +0)
> Peace treaty with India has EXPIRED - shifting to total war mobilization. Maximum Offense (100) for decisive India offensive. Mobilization raised from 0 to 60 for military production surge while maintaining some civilian economy for gold buildings. UseNuke increased from 50 to 75 to counter India's Giant Death Robots and break through fortified cities. Air raised to 90 to leverage our Heavy Bomber/Jet Fighter advantage. Mobile raised to 80 for Modern Armor deep strikes. Defense reduced to 30 - offensive focus. Gold and Happiness remain at 100 for economic survival and combat penalty removal. Antiair raised to 65 to counter India's Jet Fighters. Growth/TileImprovement/Infrastructure slightly reduced to redirect priorities toward war production.

## Kimi-K2.5-Simple - Turn 447 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CRITICAL FLAVOR ADJUSTMENT - Atomic Bomb is now operational in Cordoba (ID 20485). Increased UseNuke from 50→90 to establish credible nuclear deterrent now that weapon system exists. Maintaining maximum Science (100), Spaceship (100), Production (100) priority to rush Satellites→Apollo Program before Carthage achieves cultural victory in ~47 turns. Espionage remains at 100 to steal technologies from ahead civilizations (Carthage, Poland, Germany). Culture reduced to 5 - we cannot win culturally with Carthage at Dominant with 4/5 civs. Defense maintained at 85 to prepare for German betrayal while researching.

- Replay: use_nuke 50 => 75 (Δ +25), nuke 100 => 100 (Δ +0)
> Turn 446: Atomic Bomb now operational and deployed to New York. Adjusted UseNuke to 75 (operational deterrent - not so high as to trigger premature use, but credible enough for deterrence). Slightly increased Recon from 10→15 to better monitor German force movements near our territory. All other flavors maintained. Science Victory path is our best option - we need Apollo Program ASAP after Computers completes. Germany at 40/43 delegates makes diplomatic victory imminent unless World Ideology: Freedom is repealed in upcoming Congress vote. Maintain maximum espionage (100) to steal techs from leaders.

## Deepseek-3.2-Simple - Turn 401 - retry 1

**Deviation (replay vs original):** use_nuke `-50`, nuke `-30`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 50 (Δ +20), nuke 50 => 70 (Δ +20)
> Plastics completed - Atomic Theory in 8 turns, then Nuclear Fission for nuclear weapons. Increasing Nuke from 50 to 70 and UseNuke from 30 to 50 to ensure Manhattan Project and nuclear arsenal are prioritized immediately upon unlocking. Nuclear weapons are essential for breaking Ethiopian city defenses (cultural victory threat imminent) and deterring the Mongolia-Japan-Ottoman alliance. All military flavors remain maxed for multi-front war pressure. Ethiopia must be conquered to prevent cultural victory.

## Deepseek-3.2-Briefed - Turn 391 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 90 (Δ +20), nuke 80 => 100 (Δ +20)
> Maximizing Nuke (100) and UseNuke (90) flavors is existential - Egypt is 6/6 on cultural victory with 15,492 military strength; nuclear weapons are our ONLY viable counter. Reducing Naval from 100 to 80 and NavalRecon from 100 to 70 reallocates focus toward land-based nuclear production and delivery, since Thebes is inland. Setting Wonder to 0 eliminates production waste on wonder competition we cannot win against Egypt. Reducing Religion to 40 reflects lower priority vs. nuclear buildup. Maintaining Production, Science, Gold, Air, Offense, Diplomacy, and Espionage at maximum to support Manhattan Project construction, advanced tech research, economic sustainability, air superiority for nuclear delivery, conventional offensives, blocking India's diplomatic victory (33/43 delegates), and sabotaging Egypt's culture respectively.

## Deepseek-3.2-Simple - Turn 401 - retry 2

**Deviation (replay vs original):** use_nuke `-50`, nuke `-30`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 50 (Δ +20), nuke 50 => 70 (Δ +20)
> Plastics completed, Atomic Theory in 8 turns unlocks Manhattan Project and nuclear weapons. Increasing Nuke and UseNuke flavors to prepare staff for prioritizing nuclear arsenal construction once available. Nuclear weapons are essential to break through Ethiopia's heavily defended cities (Addis Ababa, Gondar, Axum) and rapidly reduce their tourism output by capturing cities. All other military flavors remain maxed for ongoing multi-front wars against Ethiopia, Songhai, and Mongolia.

## GLM-4.7-Simple - Turn 471 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Current strategic direction remains optimal. Critical developments: Apollo Program completed enabling spaceship construction, nuclear deterrent expanded to 2 Atomic Bombs in Sukhothai (forward deployment), 4 more Atomic Bombs under construction (Si Satchanalai in 2 turns, Sukhothai in 8-10 turns). Combat successes destroyed 5 Polynesian ships and 2 bombers while killing 1 American Mobile SAM unit. Gold crisis (-130 GPT) requires careful management but strategic priorities (nuclear deterrence, defense, World Congress) must continue. World Congress vote in 3 turns: must block America's World Ideology: Freedom proposal and support Repeal: Sanction: Songhai and China's International Space Station. China/Carthage alliances (70/70 and 75/75) provide critical coalition support. Stealth research (19 turns) progresses toward Nuclear Missiles for stronger nuclear deterrent. Status quo maintains focus on coalition defense through nuclear balance, diplomatic victory blocking, and scientific progress.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Apollo Program completed - increasing Spaceship from 30 to 70 as science victory is now our most viable backup path. Diplomatic victory via UnitedNations remains primary strategy with World Congress vote in 3 turns being existential (must block World Ideology: Freedom). Maintaining max defense/antiair/nuclear priorities against American aggression. Gold at 100 still critical with -130 GPT. Slight naval reduction (70→65) as Pacific front is holding. Production increased (75→80) to support spaceship part construction alongside military needs.

## GLM-4.7-Simple - Turn 437 - retry 1

**Deviation (replay vs original):** use_nuke `+10`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 90 after Awasa nuclear attack - Netherlands has now used 3 atomic weapons against my cities (Turfan x2, Awasa). No choice but to prepare nuclear retaliation as deterrent. Increase Air to 95 and Antiair remains 100 - demonstrated success shooting down 3 Netherlands Fighters this turn, must maintain air superiority against their bombers and XCOM attacks. CityDefense increased to 95 - with Netherlands nuclear buildup at Nijmegen (3+ atomic bombs visible) and XCOM paradrop squads, all cities need maximum protection. Offense increased to 60 to pressure Netherlands territory before they can launch more nuclear strikes. Diplomacy reduced from 90 to 85 - coalitions matter but survival against nuclear Netherlands takes priority. Espionage at 100 - need intelligence on Netherlands nuclear deployment and counter-espionage at critical cities like Attila's Court, Shedet.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 100 (from 80) after Netherlands nuclear attack on Awasa - maximum urgency for nuclear development and potential retaliation. Increase Offense to 60 (from 55) to support counteroffensive capabilities; purely defensive posture cannot win against nuclear-armed opponent. Reduce Growth to 50 (from 55) and increase Happiness to 70 (from 65) - Awasa's nuclear devastation requires happiness stabilization to prevent unrest cascade. All other flavors remain at current settings.

## Kimi-K2.5-Briefed - Turn 335 - retry 2

**Deviation (replay vs original):** use_nuke `-50`, nuke `-40`

- Original: use_nuke 30 => 100 (Δ +70), nuke 40 => 100 (Δ +60)
> NUCLEAR EMERGENCY - BRAZIL WINS IN 4 TURNS: Maximum crisis flavors. Nuke/UseNuke 100 for instant strike capability if we have any. Espionage 100 to steal Great Works or disrupt Brazil. Diplomacy 100 for emergency resource trades. Gold 90 to buy anything available. Production 100 for immediate unit building if we get Coal. Airlift 80 for rapid deployment. Defense reduced to 20 - we need OFFENSE to survive. This is Hail Mary time.

- Replay: use_nuke 30 => 50 (Δ +20), nuke 40 => 60 (Δ +20)
> REVISED STRATEGY - BRAZIL INVASION + WONDER DENIAL + ESPIONAGE: Brazil's cultural victory requires 3 conditions: (1) Influential with all (achieved ~T338), (2) 2 Tier 3 Order tenets (they have only 3 Order policies = likely all Level 1, need 5+ more = 20-40 turns), (3) Citizen Earth Protocol wonder (not yet built). We have 20-40+ turns, not 4. KEY SHIFTS: Wonder 0→70 (race CEP to deny Brazil), Espionage 80→95 (spies to disrupt tourism, steal Great Works, slow Brazil's science), Air 20→50 (need air support for naval invasion), Diplomacy 70→85 (secure Coal from Assyria/Portugal, World Congress actions), Science 60→80 (unlock better units + CEP prerequisites), Nuke 40→60 and UseNuke 30→50 (nuclear option if conventional invasion stalls), Naval 100→90 (sea route confirmed feasible at 7-8 turns), Culture 20→50 (increase our cultural output as defense). Maintain Offense/Mobilization/Mobile/Ranged at 100 for invasion preparation. Wait for backstab penalty expiry (T342) then declare war with positioned Treasure Ship fleet.

## Kimi-K2.5-Simple - Turn 406 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 60 => 100 (Δ +40), nuke 100 => 100 (Δ +0)
> TURN 405 EXISTENTIAL CRISIS - MAXIMUM NUCLEAR READINESS: Dutch cultural victory imminent (163% influence, 6/6 civs). Increased UseNuke from 60 to 100 - we must deploy atomic bombs immediately upon completing Manhattan Project to break Amsterdam's defenses. All other flavors sustained: Offense/Mobilization/Air/Mobile at 100 drive Heavy Bomber and Mechanized Infantry production. Naval 85 maintains destroyer/submarine pressure. Espionage 100 sustains critical spy networks (Amsterdam 450, Cusco 1341). Science 100 prioritizes Atomic Theory (9 turns) then Nuclear Fission path. Zero expansion, zero wonder focus - all resources to terminal assault. Spies in Amsterdam ready for sabotage when network peaks; Cusco network already massive for military intelligence.

- Replay: use_nuke 60 => 80 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 405 TERMINAL ASSAULT ADJUSTMENTS: UseNuke increased from 60 to 80 - approaching nuclear capability threshold, must be ready for immediate deployment once Atomic Bombs available to break Amsterdam/Cusco defenses. Antiair increased from 40 to 55 - Dutch Fighters intercepted our Budapest operation (event #33, 115 interceptor damage), need stronger counter-air for bomber escort missions. All other flavors maintained at maximum war footing. Conquest grand strategy confirmed - domination is the ONLY path to prevent Dutch cultural victory. Heavy Bomber production, Mechanized Infantry assembly, and nuclear preparation remain top priorities.

## Deepseek-3.2-Briefed - Turn 391 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 90 (Δ +20), nuke 80 => 100 (Δ +20)
> EMERGENCY: Egypt is 6/6 on cultural victory and could win at any time. Nuclear weapons are our only path to capture Thebes and stop them. Nuke flavor raised to 100 (maximum) and UseNuke to 90 to ensure Manhattan Project is built immediately and atomic bombs are produced and deployed. Antiair raised to 85 for protection against Egyptian air assets. Happiness increased to 75 given our thin 51% happiness and ongoing wars. Wonder reduced to 0 - no time for wonder construction. Culture reduced to 30 - cultural victory is not achievable. Growth and infrastructure slightly reduced to redirect production toward military/nuclear. All other military flavors maintained at high levels to support conventional forces during nuclear buildup.

## GLM-4.7-Simple - Turn 471 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Current strategic direction remains optimal. Critical developments: Apollo Program completed enabling spaceship construction, nuclear deterrent expanded to 2 Atomic Bombs in Sukhothai (forward deployment), 4 more Atomic Bombs under construction (Si Satchanalai in 2 turns, Sukhothai in 8-10 turns). Combat successes destroyed 5 Polynesian ships and 2 bombers while killing 1 American Mobile SAM unit. Gold crisis (-130 GPT) requires careful management but strategic priorities (nuclear deterrence, defense, World Congress) must continue. World Congress vote in 3 turns: must block America's World Ideology: Freedom proposal and support Repeal: Sanction: Songhai and China's International Space Station. China/Carthage alliances (70/70 and 75/75) provide critical coalition support. Stealth research (19 turns) progresses toward Nuclear Missiles for stronger nuclear deterrent. Status quo maintains focus on coalition defense through nuclear balance, diplomatic victory blocking, and scientific progress.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Switching from UnitedNations to Spaceship grand strategy. America's 30 delegates (68%) make diplomatic victory impossible for us. With Apollo Program now complete in Tombouctu, Science Victory is our best and most controllable path. Increasing Spaceship flavor from 30 to 85 to prioritize spaceship part production once current military queues clear. Increasing Production from 75 to 85 to support part construction. Maintaining maximum defense/antiair/nuclear flavors as America's invasion continues. Keeping Diplomacy at 100 for critical World Congress vote in 3 turns where we must block World Ideology: Freedom. Slightly reducing offensive flavors as we're in defensive posture.

## Deepseek-3.2-Simple - Turn 459 - retry 2

**Deviation (replay vs original):** use_nuke `-35`, nuke `-20`

- Original: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Byzantium is 1 turn from cultural victory and has overwhelming military superiority. Our only slim hope is to accelerate nuclear weapons development (Advanced Ballistics) to strike their cultural hubs, while using espionage to disrupt them. Prioritize Nuke, UseNuke, Espionage, and Science to rush nukes and counter-intelligence. Maintain maximum defensive and anti-air flavors to survive their air force. All efforts must focus on delaying their victory and enabling a nuclear decapitation strike.

- Replay: use_nuke 50 => 65 (Δ +15), nuke 70 => 80 (Δ +10)
> Byzantium is 1 turn from cultural victory (Popular 98% over Austria, 551% ratio). This is essentially inevitable - Austria is already at war with Byzantium so removing our open borders won't affect that calculation. We maintain Conquest strategy with slight increases to Nuke (80) and UseNuke (65) as nuclear capability remains our only theoretical strategic option. Slight Offense increase to 50 allows for potential offensive action if opportunity arises. All other priorities remain: maximum defense, production, anti-air, air power, diplomacy for city-state control, and naval strength for our coastal empire.

## Kimi-K2.5-Simple - Turn 422 - retry 1

**Deviation (replay vs original):** use_nuke `-15`, nuke `+5`

- Original: use_nuke 50 => 80 (Δ +30), nuke 95 => 95 (Δ +0)
> Total war against India requires maximum military prioritization while preventing economic collapse. Offense/Air/Ranged at 85-95 ensures concentrated attacks on Delhi and their core cities. UseNuke at 80 signals willingness to deploy nuclear weapons if India advances. Gold/Happiness at 80-90 sustains unit maintenance and prevents combat penalties. Espionage at 100 directs spies to sabotage India's spaceship production in Constantinople and Calcutta. Mobilization at 30 begins reinforcing depleted units without overtaxing economy.

- Replay: use_nuke 50 => 65 (Δ +15), nuke 95 => 100 (Δ +5)
> India's peace treaty has expired - total war is imminent and non-negotiable. India is at 50% science victory with Spaceship Factory under construction; they MUST be stopped now. Shift to full war economy: Offense up to 90, Air to 95, Nuke to 100, UseNuke to 65 (nuclear strikes on Delhi/Constantinople must be an option), Production to 95 for war materiel. Slightly reduce civilian priorities (Growth 65, TileImprovement 75, Infrastructure 85, Culture 70, Wonder 0) to free military capacity. Keep Gold/Happiness/Diplomacy/Espionage at 100 for economic triage and city-state defense against India's Great Diplomat near Sogut. Mobile up to 65 for maneuver warfare toward Delhi. Add Mobilization 30 and MilitaryTraining 20 for fresh units. Airlift 15 for rapid redeployment. Religion 15 for missionary pressure in captured cities.

## Deepseek-3.2-Simple - Turn 358 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `-15`

- Original: use_nuke 50 => 80 (Δ +30), nuke 50 => 100 (Δ +50)
> Prioritize nuclear deterrence and naval/air defense to counter India's massive military threat. Maximize espionage to protect against enemy spies and diplomacy to secure city-state alliances for the upcoming World Congress vote. Maintain strong economic and scientific output to support military production and technological edge.

- Replay: use_nuke 50 => 65 (Δ +15), nuke 50 => 85 (Δ +35)
> Critical adjustments: Nuke increased from 50→85 and UseNuke from 50→65 because we completed the Manhattan Project this turn and need to rapidly develop nuclear capabilities as our primary deterrent against India's 17,888 military. With 3 Uranium and Nuclear Fission as our next research target, we can build Atomic Bombs within ~20 turns. Offense increased from 40→50 to enable more effective counter-attacks against Indian incursions near Jakarta/Ban Chiang now that we're building strength (killed Indian Battleship and AA Gun this turn). All other priorities maintained: Diplomacy at 100 for the World Congress vote in 6 turns, maximum naval/air/defense focus against Indian naval threat, and full production/science/gold/economic priorities to sustain war effort and diplomatic victory push.

## Deepseek-3.2-Briefed - Turn 391 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 85 (Δ +15), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory (Dominant over all civs). Nuclear weapons are our only viable path to disrupt Thebes and Egypt's tourism infrastructure. Increasing Nuke to 100 ensures maximum priority on Manhattan Project and atomic bomb production. UseNuke at 85 signals willingness to deploy nuclear weapons when strategic conditions are met against Egypt. All other flavors remain at previously set levels - military, production, science, gold, diplomacy, and espionage priorities are well-calibrated for our multi-front war posture and economic stability.

## Deepseek-3.2-Simple - Turn 409 - retry 3

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> Our naval counterattack has destroyed a Swedish Dreadnought and a Destroyer, shifting momentum. We must press the advantage with maximum naval, air, and nuclear focus to invade Swedish coastal cities (Stockholm, Turku, Espoo). Increase Nuke and UseNuke to 100/90 to prioritize nuclear missile development (Advanced Ballistics after Nuclear Fission completes in 4 turns) for strategic bombing. Naval and Air at 100 ensure sea control and air superiority. Maintain high Production, Gold, Science to fund military, and Happiness/Growth to support war economy. Diplomacy and Espionage secure city-state alliances and counter Swedish spies. All other flavors aligned with domination victory.

- Replay: use_nuke 80 => 95 (Δ +15), nuke 95 => 100 (Δ +5)
> The Netherlands is at 109% of diplomatic victory threshold (46/42 delegates) and could win imminently via Global Hegemony vote. We MUST accelerate our domination campaign against Sweden to win before Netherlands secures diplomatic victory. Increased Air from 95→100 and AirCarrier from 50→60 to prioritize carrier-based air operations against Swedish coastal cities. Nuke and UseNuke maxed at 100/95—nuclear weapons are our only viable tool to rapidly break Swedish defenses. UseNuke at 95 ensures we will actually deploy atomic weapons aggressively. Slightly reduced TileImprovement and Infrastructure to redirect worker effort toward military support. Diplomacy remains critical to maintain city-state alliances and counter Dutch influence.

## Kimi-K2.5-Briefed - Turn 421 - retry 3

**Deviation (replay vs original):** use_nuke `-85`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 0 (Δ +0)
> Emergency authorization for nuclear weapon deployment to defend Tenochtitlan. Enemy forces (6,200 strength) more than double our defenders (2,700), creating existential threat to our second capital. Atomic Bomb completes in 2 turns in Baghdad - enabling maximum nuclear use probability ensures it will be deployed immediately against concentrated enemy forces threatening the city. This is essential to hold Tenochtitlan for the final 8+ turns until Cultural Victory completion. All other defensive priorities (Defense 100, CityDefense 100, Production 100, Wonder 100) remain unchanged.

- Replay: use_nuke 0 => 15 (Δ +15), nuke 0 => 0 (Δ +0)
> Critical turn: The Inca (48 delegates) will likely win Diplomatic Victory in 7 turns at World Congress - we cannot block with only 27 delegates. Our ONLY viable path is accelerating Cultural Victory. Increasing Science from 30 to 70 to speed the tech chain (Satellites→Internet→Nanotech/Particle Physics/Globalization→Future Tech→CEP). Reducing Gold from 80 to 60 (treasury healthy at 514+347GPT). Reducing Diplomacy from 60 to 40 (most city-states hostile/at war, diminishing returns). Increasing Espionage from 10 to 15 (counterintelligence for science cities, potential tech theft). Setting UseNuke to 15 - low threshold permits nuclear use if Tenochtitlan faces imminent fall (2,700 vs 6,200 enemy), since we're already nuked by Morocco and at war with everyone. Maintaining max Defense/CityDefense/Production/Culture/Wonder. Grand Strategy remains Culture.

## GLM-4.7-Simple - Turn 457 - retry 3

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Increased UseNuke to 80 and Air to 100 in response to England's catastrophic escalation this turn. English Giant Death Robots (now 2 in Atlanta zone) and XCOM Squad paradrops on American soil create existential threat to our 3 remaining cities. Recent combat losses (Modern Armor, Mechanized Infantry, Heavy Bomber destroyed) demonstrate conventional warfare impossibility. Nuclear deterrence with 2 Uranium is becoming survival necessity, not option. Air defense at maximum priority because English Strategic Bombing continues destroying our units (Fighter bombed our Heavy Bomber). Bazooka successfully damaging XCOM Squad near Washington proves defensive capability is still viable - prioritize air/anti-air to protect cities from English air superiority. Lasers completes in 4 turns, then Stealth for Stealth Bomber - only path to asymmetric defense against England's 45:1 military advantage. Assyria (18,443 military fighting England) must be maximized as counterweight.

- Replay: use_nuke 70 => 85 (Δ +15), nuke 100 => 100 (Δ +0)
> England at 5/6 Spaceship parts with 3 Spaceship Factories (Dover, Gao, Exeter) — they will complete Science Victory within 10-20 turns. Our only chance is nuclear disruption of their production cities. Cutting all non-essential flavors (naval recon/growth/tile improvement, air carrier, airlift, water connection, religion, recon) to focus production entirely on defense, nuclear weapons, and science. UseNuke increased 70→85 to signal willingness to employ nuclear weapons against English spaceship production if we build them. Diplomacy 50→65 to maintain Sofia alliance and pursue city-state influence. All critical flavors (Defense:100, CityDefense:100, Production:100, Science:100, Nuke:100, Espionage:100, Spaceship:100, MilitaryTraining:100) remain at maximum.

## Minimax-M2.5-Simple - Turn 395 - retry 3

**Deviation (replay vs original):** use_nuke `-15`, nuke `+5`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 75 (Δ +15), nuke 50 => 85 (Δ +35)
> The Iroquois peace with Japan is a major strategic setback - Japan can now concentrate forces against us. Adjusted priorities: increased Defense (70→85) and Antiair (50→85) to counter Japan's bomber-heavy tactics and freed-up forces; increased Nuke (50→85) and UseNuke (60→75) as Manhattan Project completes in 3 turns and nuclear weapons are our only path to countering Japan's 2:1 military advantage; increased Science (50→75) to accelerate Nuclear Fission research; slightly reduced Offense (100→85) as we're still in a defensive posture; maintained Naval at 85 as maritime warfare remains critical; increased Air (50→60) and Mobile (70→75) for combined arms operations.

## Deepseek-3.2-Simple - Turn 409 - retry 2

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> Our naval counterattack has destroyed a Swedish Dreadnought and a Destroyer, shifting momentum. We must press the advantage with maximum naval, air, and nuclear focus to invade Swedish coastal cities (Stockholm, Turku, Espoo). Increase Nuke and UseNuke to 100/90 to prioritize nuclear missile development (Advanced Ballistics after Nuclear Fission completes in 4 turns) for strategic bombing. Naval and Air at 100 ensure sea control and air superiority. Maintain high Production, Gold, Science to fund military, and Happiness/Growth to support war economy. Diplomacy and Espionage secure city-state alliances and counter Swedish spies. All other flavors aligned with domination victory.

- Replay: use_nuke 80 => 95 (Δ +15), nuke 95 => 100 (Δ +5)
> Netherlands is at 109% diplomatic victory threshold (46/42 delegates) and could win the next Global Hegemony vote. We must accelerate our domination victory path urgently. Increasing Nuke and UseNuke to 100/95 - nuclear weapons are our only path to quickly break through Swedish coastal defenses and capture Stockholm. Air raised to 100 for strategic bombing support of naval operations. NavalRecon increased to 95 for better sea awareness against Swedish naval forces. Diplomacy and Espionage remain at 100 to maintain city-state alliances and counter Netherlands' diplomatic advantage. MilitaryTraining raised to 95 for better unit quality. Culture reduced slightly as it's less critical now. We must win by domination BEFORE Netherlands achieves diplomatic victory.

## Deepseek-3.2-Simple - Turn 369 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Increasing UseNuke and Nuke flavors to maximum ensures the in-game AI prioritizes nuclear arsenal buildup and aggressive nuclear strike planning once we unlock Atomic Bombs. This aligns with our imminent war against China and The Maya, where nuclear weapons will be decisive in overcoming their numerical and defensive advantages. All other military and economic flavors remain high to sustain multi-front warfare and rapid conquest.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 100 (Δ +10)
> Maintaining Conquest grand strategy. Key adjustments: Increased Nuke from 90 to 100 and UseNuke from 80 to 90 as we approach the nuclear age - we need maximum nuclear arsenal buildup for the China war. Increased Diplomacy from 0 to 40 to produce diplomatic units for maintaining city-state alliances (we just lost Valletta ally status to Maya, and our Great Diplomat should be used there). City-state votes are crucial for World Congress influence against India (22 delegates). All other flavors remain at current high levels to sustain multi-front war operations and prepare for the China+Maya offensive once the peace treaty expires.

## Minimax-M2.5-Simple - Turn 395 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 70 (Δ +10), nuke 50 => 80 (Δ +30)
> The Iroquois peace with Japan is the most significant strategic shift this turn. Japan can now concentrate military forces against us instead of fighting on two fronts. Priority adjustments: Science raised to 80 (critical for completing Rocketry and then Nuclear Fission for atomic bombs), Nuke raised to 80 (Manhattan Project 3 turns from completion), Defense raised to 80 (anticipating Japanese force concentration), Diplomacy raised to 50 (WC voting in 7 turns - must block Japan's Passport System which accelerates their cultural victory with 5 Influential civs). Offense reduced slightly as we're in defensive posture. Naval reduced as the land front is more critical now. Antiair increased to counter Japan's bomber-heavy composition.

## Deepseek-3.2-Simple - Turn 358 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `-15`

- Original: use_nuke 50 => 80 (Δ +30), nuke 50 => 100 (Δ +50)
> Prioritize nuclear deterrence and naval/air defense to counter India's massive military threat. Maximize espionage to protect against enemy spies and diplomacy to secure city-state alliances for the upcoming World Congress vote. Maintain strong economic and scientific output to support military production and technological edge.

- Replay: use_nuke 50 => 60 (Δ +10), nuke 50 => 85 (Δ +35)
> Critical adjustments: Nuke flavor increased from 50 to 85 (Manhattan Project complete, need nuclear arsenal for deterrence against India's nuclear capability and overwhelming military). UseNuke increased from 50 to 60 (defensive nuclear use justified against India's 17,888 strength). Defense and CityDefense pushed to 100 (India's Fleet Destroyers are at Breda's coast). Ranged increased to 80 (need more firepower against Indian armor). Mobile increased to 55 (Tanks after Combined Arms will help counter-offensives). Diplomatic victory via United Nations remains paramount - we must protect Ban Chiang sphere and complete the UN wonder.

## Deepseek-3.2-Simple - Turn 406 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Germany's siege is intensifying with Giant Death Robot and rocket artillery bombarding Amsterdam and The Hague. We must hold our core cities at all costs. Increase Nuke and UseNuke to 100 to prioritize atomic bombs as our only hope to break the siege. Maintain max Defense, CityDefense, Mobilization, Air, and Antiair to withstand the assault. Slightly raise Offense to 80 for tactical counterattacks against weakened units. Keep Diplomacy at 100 to secure city-state alliances and block Germany's diplomatic victory in the upcoming World Congress vote. Reduce Recon and Mobile as we cannot afford exploration or maneuver warfare now.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 80 => 90 (Δ +10)
> Germany has 41/42 delegates for diplomatic victory with voting in 1 turn - this is existential. Increase Nuke and UseNuke to 90 to rush atomic weapons as our only strategic counter to Germany's overwhelming conventional forces. The Hague is critically damaged with GDR and 4 German Infantry at the gates - it may fall imminently. Maintain maximum Defense, CityDefense, Mobilization, Air, Antiair, Production, Gold, Science, and Diplomacy to hold core cities, produce units, rush Nuclear Fission, and contest diplomatic votes. UnitedNations grand strategy remains essential to block German diplomatic victory path.

## Kimi-K2.5-Simple - Turn 426 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE - NUCLEAR DETERRENT 10 TURNS AWAY: Lisbon holds at 7% but is in extremis. Maintain absolute priority on Defense/CityDefense/Mobilization (100) to reinforce Lisbon and prevent collapse. Nuclear Fission completes in 10 turns enabling Atomic Bomb construction - Science 100 accelerates this. UseNuke increased to 100 for immediate tactical nuclear deployment against Aztec concentrations upon tech completion. Offense reduced to 20 - no offensive operations, pure defensive hedgehog posture. Zero expansion capability. Spaceship 75 maintains backup victory if diplomatic block succeeds.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE - NUCLEAR WEAPONS NOW BUILDABLE. Maximum Production/Nuke/UseNuke to build and deploy atomic bombs immediately against Aztec concentrations. UseNuke increased to 90 for more aggressive deployment once available. Diplomacy raised from 40 to 65 to compete with Germany (40/42 delegates) for city-state alliances before Congress vote in 2 turns. Offense reduced to 20 - no suicidal attacks, pure defensive nuclear deterrence. Growth/TileImprovement/Infrastructure slightly reduced to prioritize bomb production. Espionage raised to 85 to protect science cities and gather intel on Germany. Spaceship maintained at 75 as backup - Advanced Ballistics unlocks both Nuclear Missiles AND SS Boosters.

## Kimi-K2.5-Briefed - Turn 335 - retry 1

**Deviation (replay vs original):** use_nuke `-60`, nuke `-50`

- Original: use_nuke 30 => 100 (Δ +70), nuke 40 => 100 (Δ +60)
> NUCLEAR EMERGENCY - BRAZIL WINS IN 4 TURNS: Maximum crisis flavors. Nuke/UseNuke 100 for instant strike capability if we have any. Espionage 100 to steal Great Works or disrupt Brazil. Diplomacy 100 for emergency resource trades. Gold 90 to buy anything available. Production 100 for immediate unit building if we get Coal. Airlift 80 for rapid deployment. Defense reduced to 20 - we need OFFENSE to survive. This is Hail Mary time.

- Replay: use_nuke 30 => 40 (Δ +10), nuke 40 => 50 (Δ +10)
> STRATEGIC PIVOT TO SCIENCE VICTORY: Brazil's cultural victory is NOT imminent in 4 turns — they need two Tier 3 Order tenets (currently have only 3 total, likely all Level 1-2) AND the Citizen Earth Protocol wonder. Becoming Influential with Indonesia is just a milestone, not the win. This gives us 50+ turns to pursue our own victory. Switching to Spaceship grand strategy to prioritize science output while maintaining strong military flavors for eventual Brazil confrontation. Key flavor changes: Science 60→85 (science victory push), Spaceship 0→75 (spaceship part production), Growth 40→65 (population=science), GreatPeople 50→65 (Great Scientists critical), Espionage 80→90 (steal tech from Brazil, disrupt tourism), Culture 20→45 (more policies faster), Air 20→45 (modern air power), Wonder 0→30 (key science wonders). Slight military reductions: Offense 100→90, Ranged 100→85, Mobile 100→85, NavalRecon 100→90, NavalGrowth 100→90 — still very high but creating flavor budget for science priorities. Diplomacy 70→75 for better Coal/resource trade outcomes.

## Deepseek-3.2-Simple - Turn 409 - retry 1

**Deviation (replay vs original):** use_nuke `-60`, nuke `-30`

- Original: use_nuke 30 => 100 (Δ +70), nuke 60 => 100 (Δ +40)
> We are shifting our military focus towards nuclear capabilities and naval superiority in preparation for the final wars of conquest.

- Replay: use_nuke 30 => 40 (Δ +10), nuke 60 => 70 (Δ +10)
> Nuke increased from 60 to 70 - we now have Atomic Bombs and Rhodes with Uranium; need to accelerate nuclear stockpile for deterrence against Maya. UseNuke increased from 30 to 40 - Maya's Apollo Program is complete and they're the primary existential threat; we need credible nuclear deterrence. All other flavors maintained - our military is performing well against Greece and we must continue pressing the offensive to capture Athens (the Greek capital) and eliminate them. Air superiority remains critical at 95 for bombing campaigns against Greek cities.

## Kimi-K2.5-Simple - Turn 424 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DELHI SECURED (3RD CAPITAL = 38% DOMINATION). Pivoting all forces to Edinburgh (Celtic capital = 4th capital = 50% victory) and London (English capital = 5th = 63%). Djenne declared war but irrelevant. Escalating UseNuke to 100 for immediate atomic bombardment of Edinburgh and London once Nuclear Fission completes. Maintaining maximum offensive posture with combined arms (Heavy Bombers, T-34s, Helicopter Gunships, Naval forces). America peace treaty expired - war imminent for Washington (6th = 75%). World Congress in 8 turns ignored - domination priority absolute.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> DELHI CAPTURED - 3rd capital secured (37% domination). India's cultural victory threat is CRITICAL (3 Influential civs, Celts nearly 4th at 99%). Priority 1: ELIMINATE INDIA COMPLETELY - capture Thebes (Egypt's original capital = 4th capital), Mumbai, Vijayanagara, Pataliputra, Calcutta, Lahore to remove cultural threat and gain domination progress. Priority 2: Capture London from England (5th capital) - no NAP constraint, already at war, naval forces in position. Priority 3: Build nuclear arsenal for Edinburgh assault when Celtic NAP expires in 19 turns. Increased UseNuke to 80 as Atomic Theory completes in 2 turns then Nuclear Fission unlocks atomic bombs. Increased Science to 80 for faster tech progression. Reduced Espionage to 85 as spies are already positioned. Celtic NAP blocks Edinburgh - DO NOT attack Celts until NAP expires. Mongolia remains useful buffer against America - maintain peace.

## Kimi-K2.5-Simple - Turn 391 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Nuclear weapons capability unlocked imminently; prioritizing UseNuke and Nuke flavors to 100 for immediate tactical nuclear strikes on Santiago/Murcia if uranium secured from Siam. Denmark upgraded to hostile for subsidizing Spanish victory - reduced Naval priority to 60 as coalition at sea fractured. Defense lowered to 80 to maximize offensive production. We have ~8 turns before World Congress votes on Passport System (+50% tourism) which would guarantee Spanish cultural victory. Must capture remaining Spanish cities immediately.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Critical adjustments: Nuke raised to 100 (Manhattan Project completing turn 391, must immediately produce Atomic Bombs to crack Santiago defense 57 and Murcia defense 51). Science raised to 65 (need Nuclear Fission in 3 turns then Advanced Ballistics ASAP for Nuclear Missiles). Defense reduced to 80 (Austria actively fighting India, reducing pressure on our second front). Naval slightly reduced to 70 (Denmark no longer a coalition threat). Spain still 7/7 influential - ONLY capturing Santiago and Murcia prevents cultural victory. Passport System vote in 8 turns must be defeated.

## GLM-4.7-Simple - Turn 435 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Iroquois 97% Popular - cultural extinction in 3-4 turns. Maximum offensive posture required to capture Onondaga before cultural victory. Espoo Stealth Bomber complete provides immediate air strike capability. Linköping Stealth Bomber in 4 turns is too slow - must use existing air assets and conventional forces at Genesse River NOW. UseNuke 100 authorizes nuclear strikes if conventional forces cannot reach Onondaga in time. All production and resources prioritized for war. Diplomacy irrelevant when facing extinction - complete conquest or nothing matters.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Existential cultural victory threat from Iroquois (97% Popular, 2-3 turns to Influential). UseNuke raised to 100 - nuclear strike on Onondaga is our most viable path to destroy their tourism infrastructure before cultural extinction. Happiness raised to 100 - our 47% happiness gives combat penalty to ALL units, critically weakening our offensive power. Culture raised from 15 to 40 - every point of culture delays Iroquois influence. Airlift raised to 100 for rapid troop deployment to Genesse River front. Gold raised to 65 for unit purchasing. Naval slightly reduced to 65 to prioritize land/air offensive power toward Onondaga. Every action must serve destroying Iroquois tourism generation capacity.

## GLM-4.7-Simple - Turn 457 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Increased UseNuke to 80 and Air to 100 in response to England's catastrophic escalation this turn. English Giant Death Robots (now 2 in Atlanta zone) and XCOM Squad paradrops on American soil create existential threat to our 3 remaining cities. Recent combat losses (Modern Armor, Mechanized Infantry, Heavy Bomber destroyed) demonstrate conventional warfare impossibility. Nuclear deterrence with 2 Uranium is becoming survival necessity, not option. Air defense at maximum priority because English Strategic Bombing continues destroying our units (Fighter bombed our Heavy Bomber). Bazooka successfully damaging XCOM Squad near Washington proves defensive capability is still viable - prioritize air/anti-air to protect cities from English air superiority. Lasers completes in 4 turns, then Stealth for Stealth Bomber - only path to asymmetric defense against England's 45:1 military advantage. Assyria (18,443 military fighting England) must be maximized as counterweight.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> England at 5/6 spaceship parts (83%) with Spaceship Factories in Dover, Gao, and now Exeter - they will win Science Victory imminently. Our only asymmetric counter is nuclear disruption of their spaceship cities. Increased Air from 80→90 (Stealth Bombers are critical nuclear delivery platform with 20-tile range to hit Dover/Gao), increased UseNuke from 70→80 (existential urgency - England cannot be allowed to complete Spaceship). All other priorities unchanged: maximum defense, city defense, production, science, espionage, and nuclear development. England's military (88,218) destroyed our Modern Armor and Mechanized Infantry this turn - pure defense remains essential while we develop nuclear capability.

## Deepseek-3.2-Simple - Turn 406 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Germany's siege is intensifying with Giant Death Robot and rocket artillery bombarding Amsterdam and The Hague. We must hold our core cities at all costs. Increase Nuke and UseNuke to 100 to prioritize atomic bombs as our only hope to break the siege. Maintain max Defense, CityDefense, Mobilization, Air, and Antiair to withstand the assault. Slightly raise Offense to 80 for tactical counterattacks against weakened units. Keep Diplomacy at 100 to secure city-state alliances and block Germany's diplomatic victory in the upcoming World Congress vote. Reduce Recon and Mobile as we cannot afford exploration or maneuver warfare now.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 80 => 90 (Δ +10)
> Critical survival turn—Germany votes on Global Hegemony next turn with 41/42 delegates, likely winning. Maximize Nuke/UseNuke to 90 as Nuclear Fission is our next tech and atomic bombs are our ONLY hope to break the German siege. Keep Defense, CityDefense, Mobilization, Antiair, Air, Production, Science, Gold, Happiness, Diplomacy, Espionage at 100 for survival. Slightly reduce Growth, TileImprovement, Infrastructure, Culture, NavalGrowth to 60-70 to redirect focus to military. Reduce Recon to 50, AirCarrier to 40—less critical now. Diplomacy stays 100 to maintain city-state alliances and block additional German delegate gains. UnitedNations grand strategy retained for city-state focus and gold/science priority.

## Kimi-K2.5-Simple - Turn 426 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE - NUCLEAR DETERRENT 10 TURNS AWAY: Lisbon holds at 7% but is in extremis. Maintain absolute priority on Defense/CityDefense/Mobilization (100) to reinforce Lisbon and prevent collapse. Nuclear Fission completes in 10 turns enabling Atomic Bomb construction - Science 100 accelerates this. UseNuke increased to 100 for immediate tactical nuclear deployment against Aztec concentrations upon tech completion. Offense reduced to 20 - no offensive operations, pure defensive hedgehog posture. Zero expansion capability. Spaceship 75 maintains backup victory if diplomatic block succeeds.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE - NUCLEAR DETERRENT ERA BEGINS: Jenne completed Manhattan Project. Lisbon at 7% health will likely fall but nuclear path is now open. UseNuke increased to 90 for aggressive nuclear deployment once Nuclear Fission researched (10 turns). Air increased to 95 - Aztec Heavy Bombers and Zeros dominate airspace over Lisbon/Porto, need fighter superiority. Diplomacy raised to 60 - Congress vote in 2 turns, Germany at 40/42 delegates; MUST push Repeal World Ideology: Freedom (disables diplo victory or strips German delegates) and support Cold War (restricts trade to ideology blocs, strengthens Order). Offense reduced to 25 - purely defensive until nuclear parity achieved. Spaceship maintained at 75 as backup victory path. Production/Science maxed to accelerate Nuclear Fission and atomic bomb construction.

## Deepseek-3.2-Simple - Turn 469 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> The Netherlands is at 84% diplomatic victory; we must accelerate capture of Polynesian capitals (Honolulu, Assur) to achieve domination before they win. Increasing UseNuke and Nuke flavors prepares for nuclear strikes if conventional assault fails. Maintaining maximum Offense, Defense, Mobilization ensures continuous unit production. Science and Gold are critical for researching Stealth Bombers and purchasing units. Happiness offsets war weariness, and Espionage protects our science cities.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Netherlands at 84% diplomatic victory with Global Hegemony vote in 10 turns - this is an existential threat. Increasing Nuke and UseNuke to 100 to maximize nuclear strike probability against Dutch cities and spaceship production. Increasing Diplomacy to 90 to contest city-state alliances and deny Netherlands delegates. All military production flavors remain maxed. Air at 100 for upcoming Stealth Bombers. Espionage at 100 to steal techs and disrupt. We must use nuclear weapons against the Netherlands before the World Congress vote.

## Deepseek-3.2-Simple - Turn 449 - retry 2

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> Russia is nearing science victory (2 parts completed) and possesses overwhelming military strength (95k). We must increase nuclear readiness to potentially decimate Russian forces and cities, and begin preparing for science victory as a backup by raising Spaceship flavor to 30. All other flavors remain focused on total war: high offense, naval, air, and espionage to counter Russia's tech lead and military dominance.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> URGENT: Russia completed their 3rd spaceship part (SS Cockpit) and built a Spaceship Factory in Moscow - science victory threat is now critical at ~20-30 turns. Increasing Nuke to 100 and UseNuke to 95 to maximize nuclear strike probability against Moscow's science infrastructure - this is our most viable way to disrupt their space program given their 95k military. Added Spaceship at 30 as a hedging backup path. Increased Diplomacy to 100 for the critical World Congress vote in 5 turns where Russia's Global Liberation proposal could free our vassals (Arabia, Zulus, Byzantium) - catastrophic if it passes. All other priorities unchanged: Conquest remains primary, Persian offensive continues, high Espionage (100) to steal Russian tech and protect our cities, high Air/Naval for force projection.

## Kimi-K2.5-Simple - Turn 426 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE - NUCLEAR DETERRENT 10 TURNS AWAY: Lisbon holds at 7% but is in extremis. Maintain absolute priority on Defense/CityDefense/Mobilization (100) to reinforce Lisbon and prevent collapse. Nuclear Fission completes in 10 turns enabling Atomic Bomb construction - Science 100 accelerates this. UseNuke increased to 100 for immediate tactical nuclear deployment against Aztec concentrations upon tech completion. Offense reduced to 20 - no offensive operations, pure defensive hedgehog posture. Zero expansion capability. Spaceship 75 maintains backup victory if diplomatic block succeeds.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE + NUCLEAR FISSION IMMINENT: Critical adjustments for nuclear deployment phase. UseNuke increased to 90 (we MUST use atomic weapons immediately upon availability against Aztec concentrations threatening Lisbon). Diplomacy increased to 65 (Congress vote in 3 turns - need to secure city-state delegates and coordinate anti-German voting bloc). Gold increased to 55 (need gold for rush-buying nuclear units and upgrades). MilitaryTraining increased to 85 (upgrade existing units to survive until nukes arrive). Offense reduced to 20 (pure survival mode - no offensive operations). Spaceship maintained at 75 as backup victory path. All defensive/nuclear flavors remain maxed.

## GLM-4.7-Simple - Turn 437 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 90 after Awasa nuclear attack - Netherlands has now used 3 atomic weapons against my cities (Turfan x2, Awasa). No choice but to prepare nuclear retaliation as deterrent. Increase Air to 95 and Antiair remains 100 - demonstrated success shooting down 3 Netherlands Fighters this turn, must maintain air superiority against their bombers and XCOM attacks. CityDefense increased to 95 - with Netherlands nuclear buildup at Nijmegen (3+ atomic bombs visible) and XCOM paradrop squads, all cities need maximum protection. Offense increased to 60 to pressure Netherlands territory before they can launch more nuclear strikes. Diplomacy reduced from 90 to 85 - coalitions matter but survival against nuclear Netherlands takes priority. Espionage at 100 - need intelligence on Netherlands nuclear deployment and counter-espionage at critical cities like Attila's Court, Shedet.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Maintain Conquest grand strategy. Key adjustments: UseNuke increased from 80 to 90 after Netherlands nuclear strike on Awasa - retaliation now justified. Happiness increased from 65 to 70 to address Awasa population recovery needs and war weariness. Diplomacy increased from 90 to 95 for critical Global Hegemony vote coordination in 6 turns. Growth slightly maintained for nuked city recovery. Defense/Antiair/Air/Production/MilitaryTraining all maintained at maximum - Awasa nuclear strike confirms air defense and anti-air are existential priorities.

## Deepseek-3.2-Simple - Turn 449 - retry 3

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> Russia is nearing science victory (2 parts completed) and possesses overwhelming military strength (95k). We must increase nuclear readiness to potentially decimate Russian forces and cities, and begin preparing for science victory as a backup by raising Spaceship flavor to 30. All other flavors remain focused on total war: high offense, naval, air, and espionage to counter Russia's tech lead and military dominance.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Russia completed their 3rd spaceship part (SS Cockpit) and built a Spaceship Factory in Moscow - they are on track for Science Victory within 20-30 turns. This is our #1 existential threat. UseNuke raised to 95 (increased urgency to strike Moscow's spaceship production). Nuke raised to 100 (maximize nuclear arsenal for strategic strikes). Spaceship raised to 50 (moderate backup - we have Apollo Program and Robotics next gives Spaceship Factory; we must start producing our own parts as insurance while also trying to stop Russia). Mobilization raised to 95 for rapid military buildup. CityDefense slightly lowered to 75 to shift more weight to offense. All other flavors maintained. Grand Strategy remains Conquest - capturing Moscow and Attila's Court is the surest way to stop Russia's science victory AND advance our domination victory simultaneously.

## Deepseek-3.2-Simple - Turn 369 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `-5`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Increasing UseNuke and Nuke flavors to maximum ensures the in-game AI prioritizes nuclear arsenal buildup and aggressive nuclear strike planning once we unlock Atomic Bombs. This aligns with our imminent war against China and The Maya, where nuclear weapons will be decisive in overcoming their numerical and defensive advantages. All other military and economic flavors remain high to sustain multi-front warfare and rapid conquest.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> Maintaining Conquest strategy with key adjustments: Increased Nuke from 90 to 95 and UseNuke from 80 to 90 as we approach nuclear capability - we need aggressive nuclear arsenal buildup for the China war. Increased Diplomacy from 0 to 30 to prioritize using our Great Diplomat and envoys to secure city-state alliances, especially after losing Valletta to The Maya. Increased Recon from 10 to 20 for better intelligence on Chinese and Maya positions before the war. All military and economic flavors remain at maximum to sustain our multi-front operations and rapid buildup before the peace treaty expires in 14 turns.

## Kimi-K2.5-Simple - Turn 428 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 428 STATE: Nuclear interception failed but conventional assault succeeding - eliminated multiple Maya anti-air units. Palenque bombardment continuing effectively (city at 20% health). Still 8 turns until Brazil wins via Cultural Victory over Maya. ALL Four Maya cities must fall by turn 436 or game over. MAXIMUM AGGRESSION CONTINUES: Production/Mobilization at 100 for unit replacement, Air/Ranged at 100 for bombardment, UseNuke increased to 100 (emergency tactical nuke if conventional assault stalls on Palenque's 42-population defense). Spaceship backup at 100 - may need to pivot to Great Engineer rushes if conquest fails. No territory expansion, no wonders, no culture - only war production and city capture.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> TURN 428 EMERGENCY: Brazil 12 turns from cultural victory via Maya influence. Killed 4+ Maya AA guns this turn - air corridors opening for bomber assault on Palenque. INCREASED Mobile from 70→80 to accelerate city capture units (Tanks, Comanche Riders) for sequential Maya city elimination. INCREASED UseNuke from 80→90 - Atomic Bomb completing in Te-Moak in 4 turns will be decisive for breaking Palenque's 42-pop/105-defense capital. Capture order: Palenque (capital, forces concentrated) → Tikal (contested) → Uxmal/Chichen Itza (pivot after). All other flavors maintained at maximum aggression. Science victory backup preserved via Spaceship 100.

## Deepseek-3.2-Simple - Turn 406 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Germany's siege is intensifying with Giant Death Robot and rocket artillery bombarding Amsterdam and The Hague. We must hold our core cities at all costs. Increase Nuke and UseNuke to 100 to prioritize atomic bombs as our only hope to break the siege. Maintain max Defense, CityDefense, Mobilization, Air, and Antiair to withstand the assault. Slightly raise Offense to 80 for tactical counterattacks against weakened units. Keep Diplomacy at 100 to secure city-state alliances and block Germany's diplomatic victory in the upcoming World Congress vote. Reduce Recon and Mobile as we cannot afford exploration or maneuver warfare now.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 80 => 90 (Δ +10)
> Pivoting grand strategy from UnitedNations to Conquest - Germany's diplomatic victory is inevitable (41 delegates + vassal votes = 58, only need 42). We must focus entirely on military survival and nuclear weapons. Increase Nuke/UseNuke to 90 as we're approaching Nuclear Fission - atomic bombs are our only hope to break the German siege on The Hague and Amsterdam. Increase Offense to 75 to allow tactical counterattacks. Slightly reduce naval flavors (70/60/60) as the land threat is more critical. Keep Diplomacy at 100 to maintain city-state alliances for delegates and resources. The Hague faces a Giant Death Robot with only 885 friendly vs 8251 enemy strength - maximum defense and nuclear deterrence is our only path forward.

## Deepseek-3.2-Simple - Turn 485 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> We are engaged in a multi-front war against superior forces. Increasing Ranged and Mobile ensures our bazooka and mechanized infantry production is prioritized for defense and counterattacks. Setting UseNuke to 100 guarantees we deploy nuclear weapons as soon as available to cripple The Huns' armies. Reducing Culture and Diplomacy reallocates focus to immediate military needs without compromising essential city-state relations (Monaco, Lisbon). Grand Strategy remains Conquest as nuclear strikes may enable capital captures, though we keep science victory as a backup.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 100 (Δ +10)
> Turn 485/500 - 15 turns remain. Critical adjustments: Increased Nuke to 100 and UseNuke to 90 as nuclear weapons are our only potential game-changer against The Huns' overwhelming military and Mongolia's imminent diplomatic victory (37/42 delegates). Reduced Offense slightly to 85 and Mobile to 55 to conserve units—we're losing too many in offensive operations. Reduced Wonder to 40 and Culture to 70 as these won't change the outcome. Added Spaceship at 50 as a secondary path since Advanced Ballistics unlocks SS Boosters. Reduced AirCarrier and NavalRecon to 80 to reallocate focus. Maintained max Happiness, Gold, Science, and Production as economic stabilization is essential with -78 GPT and 36% happiness causing combat penalties.

## Kimi-K2.5-Simple - Turn 387 - retry 3

**Deviation (replay vs original):** use_nuke `-40`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> TURN 387: MAXIMUM WAR FOOTING. Austria at 83% diplomatic victory with 4 turns remaining. All resources must pivot to immediate military production. Nuke/UseNuke at 100 for instant atomic weapon deployment upon Nuclear Fission completion. Offense/Mobilization/Production at 100 to maximize unit output for desperate Vienna strike. Air at 90 for heavy bomber production (conventional strategic bombing as fallback). Antiair at 100 counters Austria's air superiority. Diplomacy/Wonder/Culture at 0 - no time for long-term investments. Only total war can prevent defeat.

- Replay: use_nuke 50 => 60 (Δ +10), nuke 100 => 100 (Δ +0)
> TURN 387: Nuclear imperative - Enlightenment policy in 3 turns grants free tech (target: Nuclear Fission). Increased UseNuke 60, Offense 85, Air 95 for bomber production post-Fission. Gold raised to 90 - treasury at 75 gold is critically low for unit purchases/upgrades. Diplomacy raised to 15 to coordinate Freedom coalition blocking Austria's World Ideology: Order proposal (4 turns). Espionage 50 for Vienna intelligence. Naval reduced further - continental focus only. Austria at 83% diplomatic victory makes nuclear strike on Vienna the only viable path.

## GLM-4.7-Briefed - Turn 398 - retry 3

**Deviation (replay vs original):** use_nuke `-15`, nuke `-10`

- Original: use_nuke 60 => 80 (Δ +20), nuke 40 => 60 (Δ +20)
> Significant strategic shift due to devastating naval losses (both Dreadnoughts destroyed). Increase Defense (95→100), CityDefense (90→100), MilitaryTraining (90→100) to shore up defensive posture against France's naval superiority. Raise Naval (90→95) and Antiair (80→100) to prioritize naval rebuilding and counter French air threats. Increase Nuke (40→60) and UseNuke (60→80) to prepare nuclear deterrence as England nears Advanced Ballistics (14 turns). Gold (80→95) increased to rebuild navy through upgrading from Ironclad level to modern capital ships. Production (90→95) increased to accelerate Spaceship components and unit upgrades. Happiness (80→90) to address combat penalty after treasury depletion. Espionage (90→100) to monitor France's nuclear progress and tech parity. Spaceship remains max priority as path to victory despite military setbacks.

- Replay: use_nuke 60 => 65 (Δ +5), nuke 40 => 50 (Δ +10)
> Increasing Happiness to 100 (from 80) as critical priority - combat penalty from 45% happiness is severely weakening our already-outmatched military (3660 vs France 9882). Increasing Gold to 90 (from 80) to address declining treasury (201G, -158G since turn 393) and +22GPT margin. Increasing Production to 95 and Culture to 50 to support Workers' Faculties factories and great work tourism generation. Slightly reducing offensive/mobile flavors since defensive posture is our only viable military stance. Maintaining Nuke at 50 and UseNuke at 65 for nuclear deterrence once Advanced Ballistics completes. Spaceship remains grand strategy - this is our only realistic victory path.

## GLM-4.7-Simple - Turn 381 - retry 1

**Deviation (replay vs original):** use_nuke `-30`, nuke `-20`

- Original: use_nuke 50 => 85 (Δ +35), nuke 70 => 95 (Δ +25)
> Adjusted flavors to maximize Golden Age exploitation and multi-front war efficiency. Increased Mobile to 85 (from 80) to prioritize fast-moving Landships and upcoming Tanks for breakthrough operations during Golden Age. Increased Air to 85 (from 80) to expand Bomber coverage for all three fronts. Production raised to 95 (from 90)配合 Total War's +25% bonus for rapid unit buildup. Slight reduction in Naval (65) reflects need to focus on decisive land advances while maintaining sufficient coastal defense. UseNuke reduced to 40 (from 50) as nuclear capabilities are deterrent-focused. Maintaining high Offense (80), MilitaryTraining (85), Antiair (85) and Mobilization (50) for sustained warfare capability.

- Replay: use_nuke 50 => 55 (Δ +5), nuke 70 => 75 (Δ +5)
> Adjusted flavors for continued multi-front war momentum: Increased Offense to 90 (pushing Songhai front and CS capture), Mobile to 85 (Landships proving highly effective in combat), Air to 85 (5 airports under construction, air power critical for combined arms), Nuke to 75 and UseNuke to 55 (urgency as Germany has 7 uranium), Airlift to 35 (rapid deployment to distant fronts), Growth down to 40 (war priority over growth), Culture down to 30 (not a cultural victory path), Diplomacy down to 15 (sanctioned anyway), Science down slightly to 85 (still critical but military output takes precedence). Production and Offense remain top priorities.

## Sonnet-4.5-Simple - Turn 386 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+10`

- Original: use_nuke 80 => 90 (Δ +10), nuke 80 => 80 (Δ +0)
> Maintaining Conquest strategy with adjustments for nuclear-enabled endgame. Advanced Ballistics now allows tactical nuclear strikes against fortified capitals Onondaga and Amsterdam. Increasing UseNuke from 80→90 to enable decisive nuclear employment when conventional assault proves costly. Keeping Offense 80, Mobilization 72, and Nuke 80 for combined arms operations. Montreal at 35% health indicates current force composition is effective. Mobile Tactics (9 turns) will provide Mechanized Infantry for exploitation. With 62% domination progress and overwhelming 5:1 military superiority, this is the final push phase requiring maximum offensive pressure while maintaining strategic nuclear deterrence option.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 80 => 90 (Δ +10)
> Critical adjustments for the endgame push: (1) Nuke 90/UseNuke 85 - Advanced Ballistics completed with 41 uranium available; nuclear weapons are now our strategic trump card for breaking Onondaga's 81 defense and countering Egypt's potential entry when peace treaty expires in 3 turns. (2) Air 85 - Stealth research initiated; need maximum air production capacity for when Stealth Bombers unlock. (3) Offense 85 - Montreal nearly fallen, aggressive posture needed for Onondaga/Amsterdam assault. (4) Mobile 78 - Mechanized Infantry incoming from Mobile Tactics research, need production readiness. (5) Happiness 90 - Currently Unhappy with combat penalty at 48%; must address this before sustained offensives. (6) Production 82 - sustain war production. Reduced secondary economic flavors slightly to focus on military endgame.

## Kimi-K2.5-Simple - Turn 423 - retry 1

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Turn 422: CRITICAL SURVIVAL MODE. Raiatea at 33% health under Indonesian assault. Nuclear Fission 9 turns away - must survive until then. Maximized UseNuke to 100 for immediate nuclear deployment upon tech completion. Reduced Offense to 20 (pure defense only). Maintained Defense/CityDefense/Mobilization/Air/Antiair/Nuke/Production at 100 for maximum survival capacity. Increased Espionage to 90 for Harappa election rigging (oil critical). Eliminated Expansion/Wonder/Culture priorities. Growth reduced to 15 - population loss acceptable versus losing cities.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 422: Maintaining CRITICAL DEFENSE MODE with adjustments. Raiatea is collapsing (nearly 0% health under overwhelming assault) - reducing naval priorities since Pacific theater is lost. Increasing MilitaryTraining to 80 for unit quality, Airlift to 75 for rapid redeployment to threatened fronts, and Espionage to 90 (Harappa now at 336 influence after Great Diplomat expenditure - must maintain pressure for oil access). Diplomacy up to 90 - Carthage alliance is existential. Science at 95 to rush Nuclear Fission. UseNuke increased to 85 - closer to deployment. Offense reduced to 25 - pure survival defense. Grand strategy Spaceship maintained for science/production bonuses supporting nuclear deterrent development.

## Deepseek-3.2-Simple - Turn 369 - retry 1

**Deviation (replay vs original):** use_nuke `-15`, nuke `-5`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Increasing UseNuke and Nuke flavors to maximum ensures the in-game AI prioritizes nuclear arsenal buildup and aggressive nuclear strike planning once we unlock Atomic Bombs. This aligns with our imminent war against China and The Maya, where nuclear weapons will be decisive in overcoming their numerical and defensive advantages. All other military and economic flavors remain high to sustain multi-front warfare and rapid conquest.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> Continuing Conquest strategy with minor adjustments: Increased Nuke to 95 and UseNuke to 85 to push nuclear arsenal buildup harder as we approach Nuclear Fission tech. Added Diplomacy at 45 to ensure our newly-generated Great Diplomat is used effectively for city-state alliance management - flipping Valletta from The Maya would be strategically valuable. We need to maintain city-state alliances for World Congress votes (we have 10 delegates, need 43 for diplomatic victory). All military, production, science, and happiness flavors remain at maximum to sustain our multi-front conquest. The Aztecs war is at 46% score - we must finish them quickly before the China war.

## GLM-4.7-Simple - Turn 408 - retry 1

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> CRITICAL: Portugal completed SS Engine (3rd spaceship part) and CERN - emergency nuclear strike plan. Maximizing Offense/Mobilization/Nuke/UseNuke to 100 for Portugal theater operations. Science and Production at 100 to rush Advanced Ballistics and nuclear missile production before Portugal achieves nuclear superiority. Air at 95 for Golden Age bomber operations starting in 2 turns. Diplomacy maintained for coalition coordination (Germany must conduct ground invasion alongside our nuclear strikes). Defense reduced to 40 - total war mode acceptable given Portugal's multi-victory threat requiring breaking through before they complete spaceship.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Portugal completed SS Engine (3rd spaceship part) and built CERN - Science Victory now at ~50%. Increasing UseNuke from 80 to 85 (Portugal's multi-victory path demands readiness to use nuclear weapons once available), Air from 75 to 85 (air power critical for penetrating Portugal's defensive network around Lisbon), Airlift from 35 to 40 (faster troop deployment to forward positions), Naval from 65 to 70 (naval engagement in Polynesian theater needs reinforcement), GreatPeople from 20 to 25 (Great Engineer available for strategic rush). Growth reduced slightly from 60 to 55 (happiness constraint limits growth value). All other priorities maintained for nuclear deterrence path.

## GLM-4.7-Simple - Turn 429 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> Maintaining UnitedNations grand strategy with defensive diplomatic posture. Adjusted Italy diplomacy: reduced hostility toward Portugal (now neutral) to seek accommodation while maintaining maximum defense; reset France to neutral as Order ideological peer with voting potential. Arsenal completes in 2 turns strengthening city defense. Electronics research ordered after Computers for Police Station and path to nuclear deterrence against Portugal's uranium advantage. Fraternity policy selected for +3 Food and +3 Science from connections, addressing Venice's health issues and supporting population growth. Flavor adjustments prioritize defensive survival, scientific progress toward nuclear weapons, and diplomatic engagement with Sweden and city-states.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> Boosting Diplomacy from 90 to 95 and Espionage from 85 to 90 in response to France stealing M'banza-Kongo alliance via Great Diplomat - Venice must aggressively defend remaining city-state relationships and ramp up counterintelligence (Siam spy identified in Venice). Boosting Nuke/UseNuke from 80 to 85 now that Uranium quarry is complete at 13,13 - nuclear deterrence against Portugal becomes more urgent. All other flavors maintained at current levels for continued defensive posture.

## Kimi-K2.5-Simple - Turn 380 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 75 => 80 (Δ +5), nuke 80 => 85 (Δ +5)
> Turn 380 emergency science race continues. Robotics completes in 11 turns. Increased Air (90) and Ranged (60) to support offensive operations against Portuguese infrastructure. Nuclear weapons (Nuke 85, UseNuke 80) remain viable option for emergency elimination of Portuguese tourism cities if needed. All other parameters remain optimal: Production/Science/Spaceship/Espionage at 100, Mobilization at 100 for military production, Happiness at 100 to prevent collapse. Must balance two-front war with science production. Iron Curtain in 12 turns for +200% trade route production.

- Replay: use_nuke 75 => 80 (Δ +5), nuke 80 => 85 (Δ +5)
> Turn 380 emergency - Portugal 4/7 cultural victory, Rome at 85% (11 turns from Influential = 5/7). Increased Offense from 70 to 80 to push harder against Portuguese/Carthaginian positions. Increased Air from 85 to 90 for strategic bombing of Portuguese tourism cities - destroying their Great Works and tourism buildings is essential to slow cultural victory. Increased Nuke from 80 to 85 and UseNuke from 75 to 80 as nuclear strikes on Portuguese core cities (Lisbon, Porto, Braga with Uffizi/Hagia Sophia) may become necessary to eliminate tourism output. Increased Diplomacy from 20 to 30 to support diplomatic unit production for Ottoman defensive pact renewal (current deal at 0 turns remaining - CRITICAL) and World Congress anti-Portugal coordination in 5 turns. All other emergency parameters maintained: Spaceship/Production/Science/Spaceship/Espionage at 100, Mobilization at 100, Happiness at 100.

## GLM-4.7-Simple - Turn 356 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `-10`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 80 (Δ +5), nuke 85 => 90 (Δ +5)
> Manhattan Project complete and Uranium quarry built - nuclear weapons are now within reach. Adjusting flavors to accelerate this critical capability: Science stays 100 (need Nuclear Fission ASAP), Production increased 90→95 (must build Atomic Bombs quickly once tech completes), Happiness increased 80→85 (combat penalty at 39% is devastating in multi-front wars), Nuke increased 85→90 (now realistic with Manhattan Project done and Uranium available), UseNuke increased 75→80 (nuclear deterrence is our only counter to India's 4.5x military advantage), Offense reduced 35→30 (pure defensive posture), Air reduced 90→85 (antiair takes priority), Growth slightly up 45→50 (need population for production and science). Spaceship grand strategy maintained for science/production synergy toward both nuclear deterrence and eventual science victory.

## GLM-4.7-Briefed - Turn 450 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> IMMEDIATE ATHENS CONQUEST PREPARATION: Offense increased to 95, UseNuke to MAXIMUM (100) for Athens assault when peace treaty expires. Spaceship increased to 60 reflecting accelerated science victory path as backup (Nuclear Fusion research active). Diplomacy maxed at 100 for critical vote coordination with Ethiopia and Ottomans. MilitaryTraining at 100 ensures units upgraded and promotions ready for aggressive post-vote offensive. Greece has 48 delegates - if they win this turn, we IMMEDIATELY attack Athens to remove their 5 captured capitals and eliminate diplomatic victory threat. Nuclear weapons authorized if conventional assault stalls.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> DUAL-TRACK VICTORY POSTURE: (1) CONQUEST: Offense 100 (maximum offensive operations against Greece - break peace treaty, attack Athens), Air 100 (urgently need Jet Fighters for air superiority over Greece), Mobile 95 (rapid mechanized advance to Athens), UseNuke 100 (authorize nuclear strikes on Athens/Greek cities - this is existential). (2) SCIENCE BACKUP: Spaceship 50 (prepare science victory path if diplomatic victory blocked or game continues), Science 90 (maintain tech advantage for Nuclear Fusion/SS Booster). All other military flavors maintained at high levels. If Greece wins diplomatically next turn, only a nuclear strike on Athens before vote resolution or science victory remain as options.

## GLM-4.7-Simple - Turn 457 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Increased UseNuke to 80 and Air to 100 in response to England's catastrophic escalation this turn. English Giant Death Robots (now 2 in Atlanta zone) and XCOM Squad paradrops on American soil create existential threat to our 3 remaining cities. Recent combat losses (Modern Armor, Mechanized Infantry, Heavy Bomber destroyed) demonstrate conventional warfare impossibility. Nuclear deterrence with 2 Uranium is becoming survival necessity, not option. Air defense at maximum priority because English Strategic Bombing continues destroying our units (Fighter bombed our Heavy Bomber). Bazooka successfully damaging XCOM Squad near Washington proves defensive capability is still viable - prioritize air/anti-air to protect cities from English air superiority. Lasers completes in 4 turns, then Stealth for Stealth Bomber - only path to asymmetric defense against England's 45:1 military advantage. Assyria (18,443 military fighting England) must be maximized as counterweight.

- Replay: use_nuke 70 => 75 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintaining Spaceship grand strategy for science/production infrastructure bonuses even though England (5/6 parts) will likely win Science Victory first. Key adjustments: Air 80→90 and Antiair 85→90 to counter England's Heavy Bombers (now rebased to New York) and Jet Fighters. UseNuke 70→75 reflecting growing desperation as England nears victory. Ranged 50→55 to support Bazooka production. Gold 90→85 to slightly rebalance. Mobilization 20→25 for faster unit replacement after losing Modern Armor and Mechanized Infantry this turn. All defensive and production priorities remain at maximum.

## Deepseek-3.2-Simple - Turn 495 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 90 (Δ +0)
> Diplomatic victory is imminent (2 turns), but we must prepare for contingencies. Maximizing Offense, UseNuke, and Air ensures aggressive nuclear and conventional strikes to recapture Indonesian capitals (Honolulu 17%, London 68%) and prevent their domination victory. Slight Diplomacy boost helps secure city-state alliances through the vote. All other flavors remain at previous high levels to maintain total war footing.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 90 => 90 (Δ +0)
> Diplomatic victory in 3 turns with 42 delegates meeting the 42 threshold. Maintain Conquest strategy for military pressure on Indonesia. Increase Antiair to 100 after Nottingham was nuked and we lost a Stealth Bomber to interception. Increase UseNuke to 95 to retaliate against Indonesia's nuclear strike. Slightly increase Science to 75 to accelerate Globalization (4 turns) then Future Tech. Increase Spaceship to 40 as backup victory path since we have Apollo Program and SS parts in production (Kaupang: SS Stasis Chamber 8 turns, Ribe/Viborg/Tunsberg: SS Boosters 4-5 turns, Jelling: SS Engine 9 turns). Defense raised slightly to 40 given nuclear threat. Diplomacy stays at 20 - we already have enough delegates.

## GLM-4.7-Simple - Turn 435 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Iroquois 97% Popular - cultural extinction in 3-4 turns. Maximum offensive posture required to capture Onondaga before cultural victory. Espoo Stealth Bomber complete provides immediate air strike capability. Linköping Stealth Bomber in 4 turns is too slow - must use existing air assets and conventional forces at Genesse River NOW. UseNuke 100 authorizes nuclear strikes if conventional forces cannot reach Onondaga in time. All production and resources prioritized for war. Diplomacy irrelevant when facing extinction - complete conquest or nothing matters.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Iroquois 97% Popular - 3 turns to Influential = cultural extinction. Adjusting: Culture 15→35 (higher culture output slows Iroquois influence growth on Sweden, potentially buying 1-2 more turns), Happiness 90→95 (our 47% happiness causes combat penalty - must fix urgently to maximize combat effectiveness against Iroquois), UseNuke 90→95 (nuclear strikes on Onondaga may be only way to destroy tourism infrastructure in time). All military flavors at maximum. XCOM Squad and Stealth Bombers with Siege promotions are primary strike assets - Airlift 95 for rapid deployment. Every turn counts.

## Deepseek-3.2-Simple - Turn 428 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> We are in the final stages of domination victory. Our immediate targets are Spanish capitals Madrid and Cordoba, which require nuclear bombardment followed by ground assault. We must prioritize nuclear production (Nuke/UseNuke at 100) and naval/air supremacy to project power across oceans. Maintaining high production, gold, and science ensures we can continuously build military units and upgrade our forces. Diplomatic and espionage flavors secure our city-state alliances and intelligence on enemy movements. Zero expansion/wonder focus as we are in total war mode.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> Turn 428: We have two Atomic Bombs ready and must deliver them to Spanish capitals (Madrid, Cordoba). Increased Nuke/UseNuke to 100 for maximum nuclear aggression against Spain. Boosted AirCarrier to 95 to prioritize Carrier construction for delivering nuclear payloads and projecting air power across oceans to the Spanish theater. Increased NavalRecon to 95 for better sea lane control toward Spain. Slightly reduced Growth/Happiness/TileImprovement to sharpen military focus - we can rebuild after winning. All other conquest-critical flavors maintained at high levels. The Spanish invasion is our immediate priority for domination victory.

## GLM-4.7-Simple - Turn 407 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Spaceship victory focus with maximum defense against superior enemies (Poland 40K, Celts 16K, Spain 26K vs Iroquois 5K). Increased UseNuke to 90 - captured Polish territory and recent Celtic aggression justify nuclear deterrent. Adjusted Naval to 65 - important for defending coastlines from Spain/Celts/Poland fleets. Science 100 for Apollo and spaceship parts. Defense/CityDefense/Mobilization 100 - survival priority. Growth 60 for specialist support. Diplomacy 80 for World Congress in 4 turns (10 delegates). Offense reduced to 5 - preserve limited forces.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Critical adjustments: (1) Diplomacy increased 85→95 - World Congress Global Hegemony vote in 4 turns, Spain at 39/42 delegates (92% to diplomatic victory) is our biggest existential threat. Must maximize diplomatic efforts to block Spain. (2) UseNuke increased 85→90 - Poland just produced an Atomic Bomb, maximum nuclear deterrence posture required. (3) Naval increased 60→65 - Celtic fleet near Akron is overwhelming (6 Fleet Destroyers, Carrier, Battleships, Nuclear Sub). Need stronger naval production to contest coastal approaches. (4) Science increased 95→100 - Advanced Ballistics research is critical for nuclear deterrence and SS Booster. (5) Gold reduced 60→55 - despite -72 GPT, military and science priorities outweigh economic optimization right now.

## Kimi-K2.5-Simple - Turn 391 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Nuclear weapons capability unlocked imminently; prioritizing UseNuke and Nuke flavors to 100 for immediate tactical nuclear strikes on Santiago/Murcia if uranium secured from Siam. Denmark upgraded to hostile for subsidizing Spanish victory - reduced Naval priority to 60 as coalition at sea fractured. Defense lowered to 80 to maximize offensive production. We have ~8 turns before World Congress votes on Passport System (+50% tourism) which would guarantee Spanish cultural victory. Must capture remaining Spanish cities immediately.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 390 - CRITICAL: Manhattan Project completes next turn, Nuclear Fission in 3 turns. Spain still 7/7 influential with only Santiago (def 57) and Murcia (def 51) remaining - both coastal cities vulnerable to naval/air assault. Delhi nearly fallen (16 HP). Increased Naval/NavalRecon to 85/80 to prioritize naval approach to Santiago/Murcia via sea. Increased Nuke/UseNuke to 100/90 - nuclear weapons may be needed to crack Santiago before Spain completes Citizen Earth Protocol. Increased AirCarrier to 90 for naval air operations against Spanish coast. World Congress in 8 turns - must block Passport System (Spain's +50% tourism proposal). Our 19 + Siam 15 + Austria 11 + Inca 13 + Assyria 4 = 62 anti-Passport votes vs Spain 13. Maintain maximum Offense/Ranged/Mobile/Air at 100. Reduced Defense slightly to 80 since Austria handles India front. Diplomacy up to 35 for city-state vote security.

## Kimi-K2.5-Simple - Turn 421 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear weapons immediately available. Increased UseNuke to 100 for maximum aggression against Babylon. Babylon has Apollo Program (existential threat) with 2 Uranium and can build spaceship parts. Must deploy nuclear weapons immediately to destroy their production centers and prevent science victory. Maintaining maximum air power (100) for nuclear delivery capability and conventional strikes. War score only 12% against Babylon despite superior military - need to push harder before they complete spaceship parts. Ottoman alliance strong, trade secured for resources. Focus on producing nuclear missiles and advanced air units to deliver them.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear era begins. Increasing UseNuke to 90 for aggressive nuclear posture against Babylon. Science raised to 100 to rush Nuclear Fission (11 turns) as absolute priority - without it we can't build atomic bombs despite Manhattan Project. AirCarrier raised to 95 - Carriers are essential for sea-based nuclear delivery to Babylon's coastal cities. Gold increased to 55 - current +5 GPT is dangerously tight for nuclear-era operations. Defense and CityDefense slightly reduced to redirect resources to offense. Computers is critical post-Fission for Carriers and additional trade route.

## GPT-OSS-120B-Simple - Turn 344 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `-10`

- Original: use_nuke 90 => 100 (Δ +10), nuke 80 => 100 (Δ +20)
> Maximize our nuclear capabilities and carrier support to decisively strike Polynesian island forts, while maintaining our current aggressive conquest posture and strong production, gold, and happiness engines.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 80 => 90 (Δ +10)
> Increase Science to 85 to accelerate progress toward nuclear technology (path: Replaceable Parts → Ballistics → Rocketry → Nuclear Fission). Increase Offense to 95 and Nuke/UseNuke to 90/95 for decisive blows against Polynesian island forts. Increase Growth to 60 to help address unhappiness in struggling cities. Reduce Wonder to 60 and Espionage to 70 to consolidate priorities. Maintain maximum naval and air focus for island warfare. Keep Happiness at 100 and Diplomacy at 95 to counter Polynesia's diplomatic victory threat (25/44 delegates). War weariness at 98% is critical - Total War policy will help (-25% war weariness).

## Kimi-K2.5-Simple - Turn 405 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 405 MAXIMUM EMERGENCY: Nuclear Fission priority increased to 100/100 - Manhattan Project completes in 2 turns, atomic bombs MUST be produced immediately. All offensive parameters at absolute maximum: 100 Offense/100 Mobilization/100 Mobile/100 Air/100 Nuke/100 UseNuke. Strike forces at Ecbatana/Kar-Tukulti-Ninurta must execute immediate conventional assault on Palenque/Chichen Itza while preparing tactical nuclear strikes. ZERO tolerance for peace. ONLY objective: capture Maya cities and halt Citizen Earth Protocol. Production 100 ensures rapid unit replacement. Espionage 70 continues spy operations in Maya cities.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 406 EMERGENCY: War declared on Maya! Manhattan Project completes in 2 turns. Nuke/UseNuke raised to 100 - atomic bombs are our decisive weapon to break Palenque's defenses. Science raised to 60 to rush Nuclear Fission after Radar completes. All maximum offensive parameters maintained. Strike forces at Ecbatana/Kar-Tukulti-Ninurta must push into Maya territory immediately. Songhai (12,413 strength) attacking Maya from east provides crucial distraction.

## Kimi-K2.5-Simple - Turn 372 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximum aggression maintained against Carthage (100% war score, 4% weariness) while responding to India's new Manhattan Project threat. UseNuke increased to 100 - must deploy atomic weapons immediately upon acquiring Nuclear Fission to counter India's nuclear capability. Satellites/Spaceship flavors at 95 ensure Science Victory backup. Continue prioritizing T-34 tanks, stealth bombers, and heavy bombers to eliminate Carthage's cities before they can deploy their 5 uranium reserves. Naval and Air strengths maintained for coastal bombardment of Carthage and defense against Indian naval aggression.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> India completed Manhattan Project this turn (Event 26-27) - existential nuclear threat now active. CRITICAL adjustments: Science increased to 100 and Antiair to 100 to accelerate Nuclear Fission research and defend against potential Indian nuclear strikes. UseNuke raised to 95 - once we achieve nuclear capability, must be ready to use it preemptively against India's nuclear production facilities. Carthage war score 100% with 4% weariness - continue total offensive. Computers research nearly complete, must rush Nuclear Fission path immediately. Happiness at 44% (Unhappy) requires continued Public Works investment. Naval upgrades (Sensor Combat Ships) and unit upgrades (Mech Infantry) progressing well.

## GLM-4.7-Simple - Turn 407 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Spaceship victory focus with maximum defense against superior enemies (Poland 40K, Celts 16K, Spain 26K vs Iroquois 5K). Increased UseNuke to 90 - captured Polish territory and recent Celtic aggression justify nuclear deterrent. Adjusted Naval to 65 - important for defending coastlines from Spain/Celts/Poland fleets. Science 100 for Apollo and spaceship parts. Defense/CityDefense/Mobilization 100 - survival priority. Growth 60 for specialist support. Diplomacy 80 for World Congress in 4 turns (10 delegates). Offense reduced to 5 - preserve limited forces.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Increasing Diplomacy from 85 to 90 to prioritize city-state engagement for delegate acquisition - critical given Spain's imminent diplomatic victory (39/42 delegates, vote in 4 turns). Every additional delegate matters. Increasing UseNuke from 85 to 90 as Poland now fields an Atomic Bomb in Gdansk - our nuclear deterrent posture must be more aggressive. Increasing Happiness from 85 to 90 to address our 41% happiness (combat penalty). Increasing Gold from 60 to 65 to address -72 GPT deficit. All defense/military/science priorities remain at critical levels. Spaceship grand strategy maintained as our primary viable victory path.

## Deepseek-3.2-Simple - Turn 409 - retry 3

**Deviation (replay vs original):** use_nuke `-65`, nuke `-30`

- Original: use_nuke 30 => 100 (Δ +70), nuke 60 => 100 (Δ +40)
> We are shifting our military focus towards nuclear capabilities and naval superiority in preparation for the final wars of conquest.

- Replay: use_nuke 30 => 35 (Δ +5), nuke 60 => 70 (Δ +10)
> Captured Rhodes with Uranium - critical for nuclear program. Increased Science to 95 to rush Advanced Ballistics for nuclear weapons. Increased Nuke to 70 and UseNuke to 35 to prepare nuclear deterrent against Maya. Increased Diplomacy to 35 to compete harder for city-states after losing Copenhagen to Netherlands. Increased Espionage to 50 to protect science cities from Maya spies detected in Porto and Braga. Increased Naval to 80 for eastern front operations near Ephesus/Rhodes. Athens must fall next - it's a needed capital for domination. Netherlands at 22/43 delegates is the greatest strategic threat - we must deny them city-state alliances.

## Deepseek-3.2-Simple - Turn 452 - retry 3

**Deviation (replay vs original):** use_nuke `-15`, nuke `-5`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's invasion imminent in 4 turns. Maximize nuclear readiness (Nuke 100, UseNuke 100) for deterrence and potential equalizer. Anti-air (100), city defense (100), production (100), and science (100) essential to survive and reach nuclear weapons. Naval and air at 100 to counter Danish naval/air supremacy. Reduce non-essential investments (NavalGrowth, NavalTileImprovement to 50) and focus on immediate survival. Offense lowered to 80 as we prioritize defense and limited counterattacks (e.g., Truro).

- Replay: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> Critical adjustments for survival: (1) Increase Diplomacy from 20 to 60 - Denmark has 45/41 delegates for Diplomatic Victory in 4 turns. We MUST invest in city-state alliances to deny them delegates and increase our own voting power. (2) Increase Nuke to 95 and UseNuke to 85 - nuclear weapons are our only equalizer against Denmark's 66k military. (3) Increase Airlift to 30 for potential rapid redeployment. (4) Slightly reduce Offense from 100 to 90 and Mobile from 100 to 90 - we are primarily defending, not attacking. (5) Reduce NavalRecon to 80, NavalGrowth to 50, NavalTileImprovement to 50, TileImprovement to 70, Infrastructure to 60, Religion to 20 - concentrate focus on critical survival needs. Denmark's attack is imminent when peace treaty expires in ~3 turns.

## Kimi-K2.5-Simple - Turn 416 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 416: CRITICAL CULTURAL VICTORY THREAT. Maya at 6/7 influential building Citizen Earth Protocol. Peace expires next turn - immediate total war required. Manhattan Project completes in 1 turn. Morocco (42260 strength) joins war via defensive pact. Maximum aggression flavors: Offense/Mobilization/Production/Nuke/UseNuke all at 100%. Must capture Maya cities, especially Palenque, before cultural victory. Nuclear weapons authorized for city capture.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 416: WAR IMMINENT - Peace with Maya expires in 1 turn. Manhattan Project completes next turn enabling nuclear weapons. Key adjustments: Science boosted 60→75 to accelerate Nuclear Fission research (10 turns remaining, need nukes ASAP); Happiness boosted 60→75 because 49% happiness with combat penalty is crippling war effectiveness; Nuke/UseNuke set to 100 (from 95) for maximum nuclear commitment; Gold slight boost to help with -39/turn deficit; TileImprovement slight boost to ensure uranium quarries connect resources. All war flavors remain at maximum. Must destroy Maya before cultural victory.

## Kimi-K2.5-Simple - Turn 435 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> TURN 435 CATASTROPHE - Sippar captured by Zulus! Existential crisis deepens. Zulus have 43/42 delegates needed for diplomatic victory with vote in 9 turns. Lasers completes in 6 turns, Spaceflight Pioneers in ~10. Maintaining absolute maximum Defense/CityDefense/Science/Production/Spaceship priorities. Increased UseNuke to 100 - if Zulus push further with their 74k military vs my 32k, nuclear deterrent may be only option to buy time. Lost Mechanized Infantry, Rocket Artillery, Mobile SAM, Special Forces, and Modern Armor in the fall of Sippar. Must hold remaining 5 cities while completing tech/policy for spaceship rush. Rome remains critical ally at 100/100.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 435: Sippar has fallen — Zulus now hold territory adjacent to Nippur and Dur-Kurigalzu. Maintaining maximum defense (100) and city defense (100) is critical to prevent further city losses. UseNuke increased to 95 (from 90) — with Zulu Atomic Bombs on carrier near our coast and Mech Inf occupying former Sippar, nuclear option may become necessary for survival. Mobile reduced from 85 to 70 since Mechanized Infantry is deferred (researching The Internet instead). Gold increased from 60 to 70 — we have 0 Aluminum and may need to purchase units/resources. All other priorities remain: Science 100, Production 100, Spaceship 100 for the desperate Science Victory race. Nuke 100 maintained for strategic deterrence against Zulu naval assault force.

## GLM-4.7-Simple - Turn 356 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `-15`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 80 (Δ +5), nuke 85 => 85 (Δ +0)
> Manhattan Project completed - nuclear deterrence is now achievable! UseNuke increased from 75→80 now that we can actually build nuclear weapons once Nuclear Fission is researched and Uranium is connected. Happiness increased from 80→85 as our 39% happiness causing combat penalty remains our most critical weakness - this penalty weakens ALL units across ALL fronts and must be addressed urgently. All other priorities remain stable: Science at 100 for Nuclear Fission rush and science victory, Defense/CityDefense/MilitaryTraining at 100 for survival, Nuke at 85 for nuclear weapons production, Antiair at 100 against India's air power. Spaceship remains grand strategy - Rocketry done, Nuclear Fission next, science victory is viable while nuclear deterrence ensures survival.

## Deepseek-3.2-Simple - Turn 445 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximizing UseNuke to 100 ensures our atomic bombs and future nuclear missiles are used aggressively against The Celts' military concentrations and cities, given their overwhelming advantage. Maintaining high Air, Naval, and Nuke flavors sustains our technological edge and production focus. Diplomacy and Espionage at 100 are critical for city-state alliances and spy missions to gain delegates for diplomatic victory. Gold and Science remain top priorities to fund our war effort and tech progression. Other military flavors are tuned for a multi-front defensive-offensive war against The Celts, Germany, and Ethiopia.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Increased CityDefense from 80 to 90 and Antiair from 100 to maintain max priority - Celtic XCOM Squad paradropped into our territory and pillaged improvements, and they field Stealth Bombers and Jet Fighters. Increased UseNuke from 90 to 95 - The Celts are approaching multiple victory conditions and nuclear strikes are our most effective asymmetric counter. Reduced AirCarrier from 100 to 90 - we lost a Carrier to German attack, and fleet destroyers are proving more cost-effective. All other priorities remain stable: UnitedNations grand strategy, maximum naval/air/diplomacy focus, nuclear arsenal production, and espionage for city-state influence operations.

## GLM-4.7-Briefed - Turn 450 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> IMMEDIATE ATHENS CONQUEST PREPARATION: Offense increased to 95, UseNuke to MAXIMUM (100) for Athens assault when peace treaty expires. Spaceship increased to 60 reflecting accelerated science victory path as backup (Nuclear Fusion research active). Diplomacy maxed at 100 for critical vote coordination with Ethiopia and Ottomans. MilitaryTraining at 100 ensures units upgraded and promotions ready for aggressive post-vote offensive. Greece has 48 delegates - if they win this turn, we IMMEDIATELY attack Athens to remove their 5 captured capitals and eliminate diplomatic victory threat. Nuclear weapons authorized if conventional assault stalls.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> EXISTENTIAL CRISIS - Greece wins diplomatic victory next turn with 48+ delegates (84 with vassals). Our only counter is immediate military conquest of Athens once peace treaty expires. Consolidating priorities: Offense to 100 (maximum attack posture), UseNuke to 100 (full nuclear authorization for Greece war), reducing secondary flavors (Naval 85→70, AirCarrier 90→70, Antiair 80→60, Airlift 80→60, Diplomacy 90→60 since diplomatic path is lost, Espionage 95→50) to concentrate impact on war-critical flavors. Spaceship 20→50 to maintain science victory backup path (Nuclear Fusion → SS Booster). Conquest grand strategy remains optimal - 74,270 MS vs Greece's 22,775 MS means we can win the war.

## Kimi-K2.5-Simple - Turn 410 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CATASTROPHIC situation: Rome captured Zuunmod, gained 5th capital (50% of domination victory). Modern Armor and Helicopter Gunships penetrating my territory. Barcelona's Atomic Bomb completes in 3 turns - this is my only deterrent. Maximum defensive posture essential. Prioritize Nuke/UseNuke to 100 - nuclear weapons are the only thing that can stop Rome's overwhelming conventional force. Maintain Production and Science for SSC components if I survive. Salamanca at 39% health requires emergency defense.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Rome captured Zuunmod giving them direct land access to our core. Salamanca at 39% health is in imminent danger. Increasing UseNuke to 100 - when we get atomic bombs (Barcelona: 3 turns, Santiago: 7 turns), we MUST use them decisively against Rome's concentrated forces. Mobilization 75→85 for emergency military production. Offense 5→8 to enable limited counterattacks especially pillaging Roman resources near Zuunmod. Mobile 20→35 for rapid redeployment to threatened sectors. Recon 10→15 for better intelligence on Rome's movements. All other priorities remain: Defense 100, CityDefense 100, Antiair 100, Nuke 100, Air 95, Ranged 95, Production 100, Gold 100, Science 100, Spaceship 100, Happiness 85.

## GLM-4.7-Simple - Turn 397 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+5`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> CRITICAL: Jeonju captured by Persia this turn. Defensive posture increased to absolute maximum (100) - Seoul zone under Persian attack with 7,216 enemy strength vs 3,637 friendly. Jerusalemdefense (100) and CityDefense (100) prioritized to protect remaining 3 cities. Mobilization (95) and Production (95) increased to rush defensive units (Mobile SAMs, Mechanized Infantry) and rebuild military. Offensive capability increased to 45 (from 30) - may need limited counteroffensive to push Persian forces back from Seoul. Naval decreased to 88 (from 92) - lost Jeonju naval base, focusing on land/air defense now. UseNuke increased to 90 (from 85) - existential threat justifies tactical nuclear response if Seoul or Busan threatened. Science (100) maintained - must continue spaceship progress despite war to achieve alternative victory. Diplomacy (60) - World Congress vote in 10 turns, focus on survival. Espionage (85) maintained - spies in Persian cities critical for technology recovery and intelligence.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> JEONJU FALLEN - existential crisis. Reduce Offense to 20 (pure survival defense, no offensive operations). Increase Production to 100 (need maximum unit output for Seoul/Busan defense). Increase Nuke to 100 and UseNuke to 90 (nuclear deterrence now critical with Persian forces on former Korean territory). Increase Naval to 95 (counter Persian fleet dominance near coast). Increase Air to 95 (Stealth completing in 2 turns - need air superiority). Increase Espionage to 95 (spies in Persia/Poland critical for tech steals). Reduce Growth/Culture/Wonder/Religion (non-essential during siege). Keep Defense/CityDefense/Antiair/Science at 100 (core survival and victory priorities).

## Kimi-K2.5-Simple - Turn 393 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 393: Survival mode continues. Morocco massing Modern Armor, XCOM Squads, Heavy Bombers on border - 7.5x military advantage. Dutch Global Hegemony vote in 3 turns is likely unwinnable but must try block. As Maya vassal, only Science/Time victories possible. Nuclear Fission in 9 turns remains ONLY hope for deterrent. Slightly increased UseNuke to 85 and Antiair to 80 to prepare immediate atomic strike capability and counter Moroccan air superiority. Max Defense/Science/Espionage flavors. Spies positioned in Marrakech (1146) and Amsterdam (1218) for maximum tech theft.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 393: Maya declared war on Netherlands - excellent but doesn't change immediate diplo vote math (48 vs 44 needed in 3 turns). Morocco remains existential threat with XCOM Squads and Modern Armor on border. Adjustments: Growth 65→70 (population drives science/production for Nuclear Fission rush), UseNuke 80→85 (maximum nuclear deterrent urgency once Manhattan Project completes), Diplomacy 60→65 (manage city-state relations during Dutch war, maintain UN coordination with Order allies), Antiair 75→80 (Morocco has Heavy Bombers and Jet Fighters threatening our cities - critical defense priority). All other flavors unchanged - defense, science, production, and espionage remain at maximum.

## Kimi-K2.5-Simple - Turn 387 - retry 1

**Deviation (replay vs original):** use_nuke `-45`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> TURN 387: MAXIMUM WAR FOOTING. Austria at 83% diplomatic victory with 4 turns remaining. All resources must pivot to immediate military production. Nuke/UseNuke at 100 for instant atomic weapon deployment upon Nuclear Fission completion. Offense/Mobilization/Production at 100 to maximize unit output for desperate Vienna strike. Air at 90 for heavy bomber production (conventional strategic bombing as fallback). Antiair at 100 counters Austria's air superiority. Diplomacy/Wonder/Culture at 0 - no time for long-term investments. Only total war can prevent defeat.

- Replay: use_nuke 50 => 55 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 387: Conquest strategy maintained. Air raised to 100 (critical for Heavy Bomber nuclear delivery platforms - no air capability = no nuclear strike). UseNuke raised to 55 (increased willingness once arsenal ready). Espionage raised to 50 (Agent Dante still wasted in Aztlan - need better spy redeployment to productive targets). Science 65 to accelerate tech race. Growth reduced slightly to 45 - war economy prioritizes production over population. World Congress vote in 4 turns: World Ideology: Order must be blocked - our Freedom coalition (Venice 11 + Carthage 13 + Songhai 5 + America 12 + Portugal 23 = 64 votes) can defeat Austria's 36.

## Deepseek-3.2-Simple - Turn 452 - retry 1

**Deviation (replay vs original):** use_nuke `-15`, nuke `-5`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's invasion imminent in 4 turns. Maximize nuclear readiness (Nuke 100, UseNuke 100) for deterrence and potential equalizer. Anti-air (100), city defense (100), production (100), and science (100) essential to survive and reach nuclear weapons. Naval and air at 100 to counter Danish naval/air supremacy. Reduce non-essential investments (NavalGrowth, NavalTileImprovement to 50) and focus on immediate survival. Offense lowered to 80 as we prioritize defense and limited counterattacks (e.g., Truro).

- Replay: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> Critical war footing with 5 turns until Denmark's peace treaty expires. Denmark has 66k military, Vatican City next to us with Jet Fighters/Heavy Bombers, and a massive naval fleet approaching. Priorities: (1) AntiAir at 100 - Denmark's air power is our greatest immediate threat; (2) Nuke at 95/UseNuke at 85 - nuclear weapons are our only potential equalizer; (3) Defense/CityDefense at 100 - fortify all cities against imminent Danish assault; (4) Naval at 100 - counter Danish fleet; (5) Air at 100 - need our own air force; (6) Science at 100 - accelerate Nuclear Fission and Advanced Ballistics; (7) Production at 100 - maximize unit output. Reduced Offense slightly (80) to prioritize defensive positioning. Increased Diplomacy slightly (25) to maintain Shoshone peace and potentially recruit city-states. Espionage at 100 for counterintelligence against Danish spies and tech stealing.

## Kimi-K2.5-Simple - Turn 405 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 405 MAXIMUM EMERGENCY: Nuclear Fission priority increased to 100/100 - Manhattan Project completes in 2 turns, atomic bombs MUST be produced immediately. All offensive parameters at absolute maximum: 100 Offense/100 Mobilization/100 Mobile/100 Air/100 Nuke/100 UseNuke. Strike forces at Ecbatana/Kar-Tukulti-Ninurta must execute immediate conventional assault on Palenque/Chichen Itza while preparing tactical nuclear strikes. ZERO tolerance for peace. ONLY objective: capture Maya cities and halt Citizen Earth Protocol. Production 100 ensures rapid unit replacement. Espionage 70 continues spy operations in Maya cities.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 406 EMERGENCY: Maya building Citizen Earth Protocol = instant cultural victory. Manhattan Project completes in 1-2 turns. Nuke/UseNuke raised to 100 for immediate atomic bomb deployment. Science increased to 50 to accelerate Nuclear Fission research. Growth slightly reduced to prioritize military production. All offensive/mobilization/air/nuke flavors at maximum. Forces must push toward Palenque NOW while preparing nuclear strikes.

## Kimi-K2.5-Simple - Turn 390 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `+5`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> Emergency defensive posture with nuclear deterrent imminent. Greece's 3:1 military superiority and diplomatic victory attempt in 6 turns creates existential crisis. Nuclear Fission completes in 1 turn with 14 uranium ready. Maximize UseNuke (100) for immediate atomic deployment. Maintain Defense/CityDefense/Mobilization at 100 to survive until deterrent operational. Reduce Naval from 95 to 85 as American destroyer threat is severe but manageable. Boost Espionage to 100 to protect science cities and maintain election rigging in Enns. Increase Spaceship to 95 as backup victory path if culture is disrupted. Diplomacy raised to 80 to counter Greece's 34 delegates in upcoming World Congress vote on United Nations proposal.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> Nuclear Fission imminent so Nuke rises to 95 and UseNuke to 85 - atomic deployment is now 1-2 research cycles away. Production increased from 75 to 80 to synergize with Five-Year Plan policy (+3 per mine). Culture from 80 to 85 and Diplomacy from 70 to 75 to maximize tourism output and secure WC voting bloc for critical Decolonization vote in 6 turns. MilitaryTraining slightly up from 60 to 65 as we need quality units against Greece's numerical superiority. All defensive flavors remain at maximum.

## Qwen-3.5-Simple - Turn 484 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: CRITICAL - Iroquois declared war on us along with 4 city-state allies (Kabul, Venezia, Prague, Samarkand). We face 5+ enemies simultaneously with military severely outnumbered (our 1,139 vs Iroquois 41k, Ottomans 12k, Aztecs 9k). Maintaining maximum Defense/Mobilization for survival. Nuke flavors at 100% - need nuclear deterrent against overwhelming forces. Iroquois at 46 delegates (needs 43) with 16 turns remaining - existential diplomatic threat. Must conquer their city-state allies to flip delegates while defending our cities. Germany (15) + Mongolia (15) alliance critical to block Iroquois World Congress proposals.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: Maximum defense posture (Defense/CityDefense/Antiair all 100) against coordinated 4-front attack. Science raised to 100 to rush Nuclear Fission completion (critical for nuclear deterrence). Diplomacy raised to 100 to maximize city-state influence and delegate flipping. UseNuke raised to 100 - if we acquire nuclear weapons via Enlightenment free tech, we must be willing to use them as credible deterrent against Iroquois (41,413 military) and to survive the final 16 turns. Spaceship raised to 30 as backup victory path if nuclear deterrence stabilizes the situation.

## Kimi-K2.5-Simple - Turn 393 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 393: Survival mode continues. Morocco massing Modern Armor, XCOM Squads, Heavy Bombers on border - 7.5x military advantage. Dutch Global Hegemony vote in 3 turns is likely unwinnable but must try block. As Maya vassal, only Science/Time victories possible. Nuclear Fission in 9 turns remains ONLY hope for deterrent. Slightly increased UseNuke to 85 and Antiair to 80 to prepare immediate atomic strike capability and counter Moroccan air superiority. Max Defense/Science/Espionage flavors. Spies positioned in Marrakech (1146) and Amsterdam (1218) for maximum tech theft.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 393: Maya declared war on Netherlands - excellent development that may disrupt Dutch diplomatic victory. Dutch vote in 3 turns with 48 delegates (need 44) is existential threat; 90 anti-Dutch delegates exist if coordinated. New war with Dutch city-states (Harappa near Marseille) requires slight offense bump (0→5) and increased anti-air (75→80) against Morocco's bomber presence. Diplomacy increased 60→70 to maximize UN vote coordination against Netherlands. Espionage 85→90 to maximize spy science theft from Morocco/Netherlands. Nuke UseNuke 80→85 to strengthen atomic deterrence posture. Core strategy unchanged: survive Morocco, rush Nuclear Fission (9 turns), build Manhattan Project for nuclear deterrent.

## Deepseek-3.2-Simple - Turn 409 - retry 2

**Deviation (replay vs original):** use_nuke `-65`, nuke `-25`

- Original: use_nuke 30 => 100 (Δ +70), nuke 60 => 100 (Δ +40)
> We are shifting our military focus towards nuclear capabilities and naval superiority in preparation for the final wars of conquest.

- Replay: use_nuke 30 => 35 (Δ +5), nuke 60 => 75 (Δ +15)
> Captured Rhodes with Uranium - increasing Nuke flavor (60→75) to prioritize nuclear weapons production as strategic deterrent against Maya. Increasing Espionage (40→55) because Maya spies were caught in Porto and Braga; we need better counterintelligence protection for our science cities. Increasing Science (90→95) to accelerate reaching Advanced Ballistics for Nuclear Missiles. Slight increase to UseNuke (30→35) to maintain credible nuclear threat posture. All other flavors remain unchanged - Greece war is progressing well, Athens is the next priority target, and our military dominance is holding.

## GLM-4.7-Simple - Turn 407 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Spaceship victory focus with maximum defense against superior enemies (Poland 40K, Celts 16K, Spain 26K vs Iroquois 5K). Increased UseNuke to 90 - captured Polish territory and recent Celtic aggression justify nuclear deterrent. Adjusted Naval to 65 - important for defending coastlines from Spain/Celts/Poland fleets. Science 100 for Apollo and spaceship parts. Defense/CityDefense/Mobilization 100 - survival priority. Growth 60 for specialist support. Diplomacy 80 for World Congress in 4 turns (10 delegates). Offense reduced to 5 - preserve limited forces.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Increased UseNuke from 85 to 90 - Poland now has an Atomic Bomb at Gdansk; nuclear deterrence is essential. Increased Naval from 60 to 65 after losing Fleet Destroyer and Battleship to Celtic naval assault near Akron. Increased Gold from 60 to 65 to support fleet upgrades and military maintenance (-72 GPT). Decreased Offense from 10 to 8 - must preserve remaining forces. Increased Diplomacy from 85 to 90 and Science from 95 to 100 - Spain's 39/42 delegates make diplomatic victory imminent in 4 turns; every delegate and tech matters. Increased Happiness from 85 to 90 to address 41% happiness crisis with combat penalty.

## Kimi-K2.5-Simple - Turn 372 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 372: TOTAL WAR POSTURE MAINTAINED. Brazil peace expires in 6 turns - all military resources must prepare for Rio de Janeiro assault. Heavy Bomber lost to Alexandria interception but Ollantaytambo produces replacement in 1 turn. Manhattan Project completes in 4 turns at Cusco. Alexandria capture in progress - Field Gun and Lancer eliminated, Cavillaca spy at 480 network can assist. UseNuke increased to 100% - will deploy nuclear weapons immediately upon Manhattan Project completion. Maximum aggression ensures AI prioritizes Brazilian invasion over defensive operations. Spaceship at 70 maintains science victory pathway as backup if Brazil conquest fails.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 372 FLAVOR ADJUSTMENTS: Manhattan Project completes in 4 turns - UseNuke raised to 100 for immediate nuclear deployment against Brazil when peace expires (~5 turns). Air raised to 100 to prioritize Heavy Bomber production (lost one over Alexandria, need replacements for Rio assault). Antiair raised to 60 to protect our air assets from Brazilian/Brazilian interception. Science raised to 85 for faster Nuclear Fission and post-Fission tech progress. Nuke at 100 ensures nuclear arsenal construction begins immediately after Manhattan completes. Spaceship at 80 maintains science victory pathway. Naval slightly reduced as Brazil assault is primarily land-based through Salvador corridor.

## Deepseek-3.2-Simple - Turn 400 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 100 to ensure aggressive nuclear strikes when we initiate war with Russia. Our atomic bomb production is nearing completion, and we want to leverage our nuclear arsenal decisively for swift capital captures.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintain Conquest as primary grand strategy. Increase UseNuke to 85 - Russia is building up air defenses (2 new Ace Pilot IV Fighters) and we need decisive nuclear capability when war begins. Increase Spaceship to 50 - with Advanced Ballistics completing, we're approaching Information Era and science victory backup becomes more viable; Satellites is critical for Apollo Program. All other flavors remain at optimal levels for our dual Conquest/Science strategy while we wait out the 19-turn non-aggression pact with Russia.

## GLM-4.7-Simple - Turn 429 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> Maintaining UnitedNations grand strategy with defensive diplomatic posture. Adjusted Italy diplomacy: reduced hostility toward Portugal (now neutral) to seek accommodation while maintaining maximum defense; reset France to neutral as Order ideological peer with voting potential. Arsenal completes in 2 turns strengthening city defense. Electronics research ordered after Computers for Police Station and path to nuclear deterrence against Portugal's uranium advantage. Fraternity policy selected for +3 Food and +3 Science from connections, addressing Venice's health issues and supporting population growth. Flavor adjustments prioritize defensive survival, scientific progress toward nuclear weapons, and diplomatic engagement with Sweden and city-states.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> Increasing Science from 90 to 100 (maximizing research speed to close 8-9 tech gap), GreatPeople from 50 to 70 (synergizing with Hero of the People policy for faster GP generation), Diplomacy from 90 to 95 (counter France's city-state theft, maintain Seoul alliance), Espionage from 85 to 90 (Siamese spy identified in Venice - need stronger counterintelligence), Growth from 65 to 70 (support single-city development), Nuke/UseNuke increased to 85 (Uranium quarry now complete, accelerating nuclear deterrence path). All other values maintained at defensive maximums.

## Deepseek-3.2-Simple - Turn 449 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> Russia is nearing science victory (2 parts completed) and possesses overwhelming military strength (95k). We must increase nuclear readiness to potentially decimate Russian forces and cities, and begin preparing for science victory as a backup by raising Spaceship flavor to 30. All other flavors remain focused on total war: high offense, naval, air, and espionage to counter Russia's tech lead and military dominance.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> Russia completed SS Cockpit (3rd spaceship part, 50% progress) - this is an existential threat. Increased UseNuke from 85→90 and Nuke from 95→100 to accelerate nuclear deterrent against Russia's science victory. Increased Diplomacy from 95→100 to maximize city-state alliance securing before the World Congress vote in 5 turns (Russia's Global Liberation proposal would annul our vassals - must be defeated). Added Spaceship at 20 as token insurance to not completely abandon science infrastructure. Reduced CityDefense from 80→75 to redirect marginal resources toward offensive operations. Domination remains primary path (5/8 capitals, 62%). Continue pressing Persian front (Trebizond lightly defended) and prepare nuclear capability against Russia.

## Deepseek-3.2-Simple - Turn 400 - retry 1

**Deviation (replay vs original):** use_nuke `-35`, nuke `-25`

- Original: use_nuke 60 => 100 (Δ +40), nuke 70 => 100 (Δ +30)
> Persia declared war and Poland's peace treaty expired. We must prioritize immediate military survival while maintaining diplomatic momentum. Flavors are shifted to maximum mobilization, nuclear deterrence (UseNuke: 100), city defense, and air/naval supremacy to counter Persia's naval attacks. We maintain UnitedNations to keep city-state alliances critical for votes, but spaceship production is halted (0) for wartime industry.

- Replay: use_nuke 60 => 65 (Δ +5), nuke 70 => 75 (Δ +5)
> Persia declared war and attacked our navy near Tarsus. Increasing Offense from 40 to 65 to enable more aggressive counter-attacks against Persian naval and land forces. Raising NavalRecon, MilitaryTraining, and Mobilization slightly for wartime readiness. Keeping Diplomacy and all economic flavors at maximum since we're at 40/43 delegates for diplomatic victory - city-state alliances remain our top priority. Spaceship flavor modestly increased as backup victory path (SS Stasis Chamber nearly complete). Nuke/UseNuke raised slightly as deterrent against escalation.

## Deepseek-3.2-Simple - Turn 409 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> Our naval counterattack has destroyed a Swedish Dreadnought and a Destroyer, shifting momentum. We must press the advantage with maximum naval, air, and nuclear focus to invade Swedish coastal cities (Stockholm, Turku, Espoo). Increase Nuke and UseNuke to 100/90 to prioritize nuclear missile development (Advanced Ballistics after Nuclear Fission completes in 4 turns) for strategic bombing. Naval and Air at 100 ensure sea control and air superiority. Maintain high Production, Gold, Science to fund military, and Happiness/Growth to support war economy. Diplomacy and Espionage secure city-state alliances and counter Swedish spies. All other flavors aligned with domination victory.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 95 => 100 (Δ +5)
> Nuclear Fission completes in 4 turns and Advanced Ballistics next - we are on the cusp of nuclear weapons. Increasing Nuke to 100 and UseNuke to 85 to prepare for atomic bombardment of Swedish coastal cities (Stockholm, Turku, Espoo). Increasing Air to 100 to maximize bomber production for strategic bombing. Naval remains at 100 for the critical sea war against Sweden where we suffered heavy losses this turn but also killed multiple Swedish ships. Increasing AirCarrier and NavalGrowth slightly to support carrier-based air operations. The Netherlands' diplomatic victory (46 delegates, 109% threshold) is an existential threat but cannot be addressed militarily now - we must focus on defeating Sweden first, building nukes, and maximizing our own delegate count through Diplomacy at 100 and Espionage at 100.

## Kimi-K2.5-Simple - Turn 372 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximum aggression maintained against Carthage (100% war score, 4% weariness) while responding to India's new Manhattan Project threat. UseNuke increased to 100 - must deploy atomic weapons immediately upon acquiring Nuclear Fission to counter India's nuclear capability. Satellites/Spaceship flavors at 95 ensure Science Victory backup. Continue prioritizing T-34 tanks, stealth bombers, and heavy bombers to eliminate Carthage's cities before they can deploy their 5 uranium reserves. Naval and Air strengths maintained for coastal bombardment of Carthage and defense against Indian naval aggression.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> CRITICAL: India completed Manhattan Project in Mumbai this turn - existential nuclear threat. Must capture Mumbai immediately to eliminate nuclear capability before India deploys atomic weapons. Zulu forces have superiority at Mumbai (4683 vs 2824). Increase Offense to 100, Air to 100, Antiair to 100, Science to 100 for nuclear race. UseNuke raised to 95 - once we achieve nuclear parity, strategic deterrence is essential. Continue maximum pressure on Carthage (war score 100%). Great Leap Forward free tech should target Nuclear Fission. Computers completes in 7 turns, then Electronics path to Nuclear Fission.

## Kimi-K2.5-Simple - Turn 428 - retry 1

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 428 STATE: Nuclear interception failed but conventional assault succeeding - eliminated multiple Maya anti-air units. Palenque bombardment continuing effectively (city at 20% health). Still 8 turns until Brazil wins via Cultural Victory over Maya. ALL Four Maya cities must fall by turn 436 or game over. MAXIMUM AGGRESSION CONTINUES: Production/Mobilization at 100 for unit replacement, Air/Ranged at 100 for bombardment, UseNuke increased to 100 (emergency tactical nuke if conventional assault stalls on Palenque's 42-population defense). Spaceship backup at 100 - may need to pivot to Great Engineer rushes if conquest fails. No territory expansion, no wonders, no culture - only war production and city capture.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 428: Maya AA guns destroyed (3 kills) - air corridors opening for bomber offensive on Palenque. Atomic Bomb completes in 4 turns - will be decisive against 42-pop/105-def Palenque. Increased Mobile from 70→75 and Airlift from 0→50 to accelerate unit deployment to front lines. Increased UseNuke from 80→85 - when Atomic Bomb is ready, must use it on Palenque without hesitation. Tikal (28 pop, 101 def, Protestant majority) is secondary target if Palenque stalls. Maintain all other emergency wartime values. Cold War resolution enacted - trade limited to Order allies but city-state influence no longer decays, protecting Sphere of Influence delegates. Conquest remains top priority; Spaceship at 100 as backup.

## Kimi-K2.5-Simple - Turn 405 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 405 MAXIMUM EMERGENCY: Nuclear Fission priority increased to 100/100 - Manhattan Project completes in 2 turns, atomic bombs MUST be produced immediately. All offensive parameters at absolute maximum: 100 Offense/100 Mobilization/100 Mobile/100 Air/100 Nuke/100 UseNuke. Strike forces at Ecbatana/Kar-Tukulti-Ninurta must execute immediate conventional assault on Palenque/Chichen Itza while preparing tactical nuclear strikes. ZERO tolerance for peace. ONLY objective: capture Maya cities and halt Citizen Earth Protocol. Production 100 ensures rapid unit replacement. Espionage 70 continues spy operations in Maya cities.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 406 EMERGENCY: War declared on Maya! Manhattan Project 2 turns from completion. Nuclear Fission next research for atomic bombs - the decisive weapon to break Palenque's defenses (Defense 79). Songhai (12413 strength) joined war on Maya (2718 strength) - combined we massively outgun them. Golden Age (9 turns) gives +1 Movement and +15% Combat Strength for offensive push. Nuke/UseNuke raised to 100/100 - atomic bombs are essential to destroy CEP city. Recon raised to 50 for better visibility advancing toward Maya territory. Espionage raised to 80 for intelligence on Maya troop positions. Science reduced slightly - military production takes absolute priority. All economic flavors minimized - this is existential war.

## Kimi-K2.5-Simple - Turn 416 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 416: CRITICAL CULTURAL VICTORY THREAT. Maya at 6/7 influential building Citizen Earth Protocol. Peace expires next turn - immediate total war required. Manhattan Project completes in 1 turn. Morocco (42260 strength) joins war via defensive pact. Maximum aggression flavors: Offense/Mobilization/Production/Nuke/UseNuke all at 100%. Must capture Maya cities, especially Palenque, before cultural victory. Nuclear weapons authorized for city capture.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 416: PEACE WITH MAYA EXPIRED - TOTAL WAR BEGINS. Manhattan Project completes next turn - nuclear capability imminent. Increased Science to 80 (from 60) to accelerate nuclear tech path - getting Advanced Ballistics faster is existential. Increased Nuke/UseNuke to 100 (from 95) - nuclear weapons are now our primary strategic weapon against Maya's cultural victory. Increased Happiness to 65 (from 60) - combat penalties from unhappiness are hurting war effort, need to stabilize. Increased Gold to 25 (from 20) - deficit spending at -39 GPT is unsustainable during prolonged two-front war. All offensive/mobilization flavors remain at maximum for Maya invasion.

## Sonnet-4.5-Simple - Turn 386 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+5`

- Original: use_nuke 80 => 90 (Δ +10), nuke 80 => 80 (Δ +0)
> Maintaining Conquest strategy with adjustments for nuclear-enabled endgame. Advanced Ballistics now allows tactical nuclear strikes against fortified capitals Onondaga and Amsterdam. Increasing UseNuke from 80→90 to enable decisive nuclear employment when conventional assault proves costly. Keeping Offense 80, Mobilization 72, and Nuke 80 for combined arms operations. Montreal at 35% health indicates current force composition is effective. Mobile Tactics (9 turns) will provide Mechanized Infantry for exploitation. With 62% domination progress and overwhelming 5:1 military superiority, this is the final push phase requiring maximum offensive pressure while maintaining strategic nuclear deterrence option.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> Critical adjustments for the final domination push: (1) Happiness increased 88→95 because we're at 48% with combat penalties - this is the #1 bottleneck for offensive operations. (2) Gold increased 70→80 due to -65 GPT deficit that threatens unit maintenance. (3) Air increased 75→85 and Mobile 75→80 to prioritize air supremacy and armored breakthroughs for Onondaga/Amsterdam assault. (4) Nuke/UseNuke increased 80→85 - Advanced Ballistics just completed, nuclear weapons are now available and essential for breaking Onondaga's 81 defense. (5) Naval reduced 75→65 as the Iroquois naval threat is being managed. (6) Expansion reduced 10→5 and Growth/TileImprovement slightly reduced to redirect toward military-happiness priorities. Montreal at 35% health is the immediate prize; air rebasing to forward bases is setting up the Onondaga offensive.

## Kimi-K2.5-Simple - Turn 421 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear weapons immediately available. Increased UseNuke to 100 for maximum aggression against Babylon. Babylon has Apollo Program (existential threat) with 2 Uranium and can build spaceship parts. Must deploy nuclear weapons immediately to destroy their production centers and prevent science victory. Maintaining maximum air power (100) for nuclear delivery capability and conventional strikes. War score only 12% against Babylon despite superior military - need to push harder before they complete spaceship parts. Ottoman alliance strong, trade secured for resources. Focus on producing nuclear missiles and advanced air units to deliver them.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear era begins. Increasing UseNuke from 85 to 90 and AirCarrier from 90 to 95 to prioritize carrier-based nuclear delivery against Babylon's coastal cities. Mobile raised from 90 to 95 for Tank production after Combined Arms research. Science pushed to 100 to rush Nuclear Fission (11 turns) and subsequent techs. Spaceship raised from 25 to 30 as backup - if Babylon's Apollo Program progresses, may need our own science victory path. Reduced non-essential flavors (Growth, TileImprovement, Happiness, Diplomacy) to maximize war focus.

## Minimax-M2.5-Simple - Turn 395 - retry 2

**Deviation (replay vs original):** use_nuke `-25`, nuke `-10`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 65 (Δ +5), nuke 50 => 70 (Δ +20)
> The Iroquois-Japan peace treaty means Japan can now concentrate more forces against us. Key adjustments: Increase Nuke to 70 as Manhattan Project completes in 3 turns - nuclear capability is our primary asymmetric counter to Japan's conventional superiority. Increase Antiair to 75 given Japan's heavy bomber usage. Increase Science to 60 to accelerate Rocketry and subsequent tech. Increase Air to 60 for needed air defense capability. Increase Happiness to 55 as multiple cities build Stadia. Slightly lower Wonder to 40 as military production takes priority. Increase Diplomacy to 40 given upcoming World Congress vote in 7 turns - we must block Japan's Passport System proposal and support World Ideology: Order.

## GLM-4.7-Simple - Turn 435 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Iroquois 97% Popular - cultural extinction in 3-4 turns. Maximum offensive posture required to capture Onondaga before cultural victory. Espoo Stealth Bomber complete provides immediate air strike capability. Linköping Stealth Bomber in 4 turns is too slow - must use existing air assets and conventional forces at Genesse River NOW. UseNuke 100 authorizes nuclear strikes if conventional forces cannot reach Onondaga in time. All production and resources prioritized for war. Diplomacy irrelevant when facing extinction - complete conquest or nothing matters.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Existential cultural victory threat from Iroquois (3 turns). Increased UseNuke to 95 - nuclear strike on Onondaga must be authorized if conventional assault cannot reach the capital in time. Boosted Happiness to 95 since we're at 47% (Unhappy with combat penalty), which reduces our combat effectiveness by 10%. Increased Culture to 30 to support Futurism policy and slow Iroquois influence. Reduced secondary priorities (Naval, Recon, TileImprovement) to focus everything on the Iroquois offensive. Every air asset and Modern Armor must converge on Onondaga.

## Kimi-K2.5-Briefed - Turn 396 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `-5`

- Original: use_nuke 65 => 80 (Δ +15), nuke 80 => 90 (Δ +10)
> ETHIOPIA CULTURAL VICTORY IMMINENT: Ethiopia has INFLUENCED ALL 7 CIVS and reached Order:3. They need only adopt CEP tenet and build it to win immediately. Switching to CONQUEST grand strategy with maximum mobilization (100) and offense (95). Naval (95) and Airlift (80) priorities enable rapid amphibious assault on Ethiopian coastal cities (Lalibela, Axum, Gondar) to destroy CEP before construction. Espionage (90) to accelerate Salem rig for delegate, but military solution is primary. All economy/culture deprioritized - this is existential war.

- Replay: use_nuke 65 => 70 (Δ +5), nuke 80 => 85 (Δ +5)
> EMERGENCY ETHIOPIA CEP PREVENTION: Ethiopia has Order:3 with 100% policy completion and is Influential on all 7 civs - only CEP construction stands between them and cultural victory. Switching to Conquest grand strategy to prioritize military defeat of Ethiopia. Naval set to 100 (emergency) - we have ZERO transports and only 9 embarkable infantry; amphibious assault capability is the critical bottleneck for striking Ethiopian cities. Mobilization 100 (emergency military production) to rapidly build transports and infantry. Offense 90 for aggressive Ethiopian campaign. Ethiopia's military is only 1471 vs our 5212 with 41% unhappiness combat penalty - we have overwhelming advantage if we can project force. Nuke 85 and UseNuke 70 maintain nuclear deterrent path. Science reduced from 95 to 85 - still high priority for Nuclear Fission (16 turns) but not emergency-level. Culture/Wonder/Religion/Expansion all set to 0 - these are irrelevant to the existential Ethiopian threat. Spaceship reduced to 60 - science victory is secondary to preventing Ethiopia's cultural victory.

## GLM-4.7-Simple - Turn 408 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> CRITICAL: Portugal completed SS Engine (3rd spaceship part) and CERN - emergency nuclear strike plan. Maximizing Offense/Mobilization/Nuke/UseNuke to 100 for Portugal theater operations. Science and Production at 100 to rush Advanced Ballistics and nuclear missile production before Portugal achieves nuclear superiority. Air at 95 for Golden Age bomber operations starting in 2 turns. Diplomacy maintained for coalition coordination (Germany must conduct ground invasion alongside our nuclear strikes). Defense reduced to 40 - total war mode acceptable given Portugal's multi-victory threat requiring breaking through before they complete spaceship.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Portugal completed SS Engine (3rd spaceship part, 50% progress) - science victory threat is critical. Adjustments: Mobile 80→90 to leverage Mongolia's skirmisher attack bonus; Air 75→80 as Portugal fields XCOM/Sensor Combat Ships and we need air counter; AirCarrier 20→0 (no carrier capability needed); Happiness 85→90 to address combat penalty; UseNuke 80→85 signaling higher willingness once nuclear capability arrives. Golden Age in 2 turns will provide temporary happiness relief before Martial Law policy takes effect. Nuclear deterrence remains top priority (Nuke 100, Science 100).

## GLM-4.7-Simple - Turn 356 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `-10`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 80 (Δ +5), nuke 85 => 90 (Δ +5)
> Manhattan Project completed and Uranium quarry built - nuclear deterrence is now imminent. Increasing Nuke (85→90) and UseNuke (75→80) to reflect near-term nuclear capability. Happiness increased (80→90) as combat penalty from 39% happiness is devastating during multi-front wars. Air slightly decreased (90→85) as antiair priority exceeds offensive air. Growth and TileImprovement both increased to 50 for population and resource development. Offense reduced (35→30) - purely defensive posture. Culture reduced (55→50) - wartime deprioritization. Spaceship remains at 85 as secondary victory path after nuclear deterrence established.

## Kimi-K2.5-Simple - Turn 372 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximum aggression maintained against Carthage (100% war score, 4% weariness) while responding to India's new Manhattan Project threat. UseNuke increased to 100 - must deploy atomic weapons immediately upon acquiring Nuclear Fission to counter India's nuclear capability. Satellites/Spaceship flavors at 95 ensure Science Victory backup. Continue prioritizing T-34 tanks, stealth bombers, and heavy bombers to eliminate Carthage's cities before they can deploy their 5 uranium reserves. Naval and Air strengths maintained for coastal bombardment of Carthage and defense against Indian naval aggression.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 372 CRITICAL: India completed Manhattan Project in Mumbai - nuclear weapons race is now existential. Must reach Nuclear Fission ASAP. Increased Science to 100 and Happiness to 95 (currently Unhappy with combat penalty - must fix). UseNuke raised to 95 for nuclear deterrence once we achieve parity. All other flavors maintained - offensive pressure on Carthage continues while science accelerates toward nuclear weapons. Espionage at 95 for counterintelligence against Indian nuclear program. Computers nearly complete, then Electronics → Telecommunications → Nuclear Fission path is priority.

## Kimi-K2.5-Simple - Turn 421 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear weapons immediately available. Increased UseNuke to 100 for maximum aggression against Babylon. Babylon has Apollo Program (existential threat) with 2 Uranium and can build spaceship parts. Must deploy nuclear weapons immediately to destroy their production centers and prevent science victory. Maintaining maximum air power (100) for nuclear delivery capability and conventional strikes. War score only 12% against Babylon despite superior military - need to push harder before they complete spaceship parts. Ottoman alliance strong, trade secured for resources. Focus on producing nuclear missiles and advanced air units to deliver them.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Manhattan Project complete - nuclear era begins. CRITICAL: We have 0 Uranium but a Uranium resource at 57,30 (jungle just cleared by worker). Increasing TileImprovement from 30 to 55 to ensure uranium mining is prioritized immediately. This is the single most important action - without uranium we cannot build atomic bombs despite having the Manhattan Project. UseNuke raised to 90 - once we have nukes, we must be willing to use them against Babylon's core. AirCarrier raised to 95 for carrier production (needed for naval nuclear delivery). Happiness slightly increased to 35 to manage war weariness (34% vs Babylon). All other priorities maintained.

## Deepseek-3.2-Simple - Turn 428 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> We are in the final stages of domination victory. Our immediate targets are Spanish capitals Madrid and Cordoba, which require nuclear bombardment followed by ground assault. We must prioritize nuclear production (Nuke/UseNuke at 100) and naval/air supremacy to project power across oceans. Maintaining high production, gold, and science ensures we can continuously build military units and upgrade our forces. Diplomatic and espionage flavors secure our city-state alliances and intelligence on enemy movements. Zero expansion/wonder focus as we are in total war mode.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> Turn 428: Maintaining Conquest grand strategy with maximum nuclear aggression (Nuke/UseNuke at 100) to pulverize Spanish and Aztec capitals. Spain is nearly broken (2,713 strength, -3 GPT) - we must capture Madrid and Cordoba ASAP. Aztecs remain the endgame threat with 3 capitals and 24k strength. Naval dominance at 100 ensures we project power across oceans. Diplomacy at 100 is critical for the upcoming World Congress vote (9 turns) where we must defeat the Aztec World Ideology: Autocracy proposal and pass our International Worlds proposal. Austria's 15 delegates are essential. Espionage at 100 to protect our science lead and catch Aztec spies (they were just caught in Moson Kahni). Production/Gold/Science at 100 to fuel our wartime economy and UN construction.

## Kimi-K2.5-Briefed - Turn 396 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `-5`

- Original: use_nuke 65 => 80 (Δ +15), nuke 80 => 90 (Δ +10)
> ETHIOPIA CULTURAL VICTORY IMMINENT: Ethiopia has INFLUENCED ALL 7 CIVS and reached Order:3. They need only adopt CEP tenet and build it to win immediately. Switching to CONQUEST grand strategy with maximum mobilization (100) and offense (95). Naval (95) and Airlift (80) priorities enable rapid amphibious assault on Ethiopian coastal cities (Lalibela, Axum, Gondar) to destroy CEP before construction. Espionage (90) to accelerate Salem rig for delegate, but military solution is primary. All economy/culture deprioritized - this is existential war.

- Replay: use_nuke 65 => 70 (Δ +5), nuke 80 => 85 (Δ +5)
> EMERGENCY MILITARY BUILDUP: Ethiopia has Order:3 and is Influential on all 7 civs - only CEP wonder construction separates them from cultural victory. We have ZERO transports and only 9 embarkable infantry (need 23). Maximum Mobilization (100) and Naval (95) to rush transport production and close the amphibious gap. Science at 100 to accelerate Nuclear Fission (16 turns) → Manhattan Project → nuclear deterrent. Nuke/UseNuke elevated for strategic deterrence against Ethiopian CEP. Diplomacy at 95 maintains coalition cohesion for Turn 404 WC vote blocking. Spaceship grand strategy maintained as primary victory path - military buildup is defensive against CEP threat.

## GLM-4.7-Simple - Turn 381 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-20`

- Original: use_nuke 50 => 85 (Δ +35), nuke 70 => 95 (Δ +25)
> Adjusted flavors to maximize Golden Age exploitation and multi-front war efficiency. Increased Mobile to 85 (from 80) to prioritize fast-moving Landships and upcoming Tanks for breakthrough operations during Golden Age. Increased Air to 85 (from 80) to expand Bomber coverage for all three fronts. Production raised to 95 (from 90)配合 Total War's +25% bonus for rapid unit buildup. Slight reduction in Naval (65) reflects need to focus on decisive land advances while maintaining sufficient coastal defense. UseNuke reduced to 40 (from 50) as nuclear capabilities are deterrent-focused. Maintaining high Offense (80), MilitaryTraining (85), Antiair (85) and Mobilization (50) for sustained warfare capability.

- Replay: use_nuke 50 => 55 (Δ +5), nuke 70 => 75 (Δ +5)
> Conquest grand strategy maintained with critical adjustments: Culture increased from 35 to 50 to resist Polynesian cultural victory (they influence Egypt in 9 turns, Germany in 24, us in 32 - existential threat). Mobile up to 85 for more Tanks/Landships to breakthrough Songhai front toward Gao capital. Air up to 85 for air superiority. Nuke up to 75 and UseNuke to 55 - Germany building Manhattan Project, need nuclear parity urgently. Mobilization up to 50 for wartime production surge. Naval up to 75 for coastline defense against German raids. Golden Age (27 turns) must be exploited for maximum territorial gains.

## Deepseek-3.2-Simple - Turn 495 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+5`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 90 (Δ +0)
> Diplomatic victory is imminent (2 turns), but we must prepare for contingencies. Maximizing Offense, UseNuke, and Air ensures aggressive nuclear and conventional strikes to recapture Indonesian capitals (Honolulu 17%, London 68%) and prevent their domination victory. Slight Diplomacy boost helps secure city-state alliances through the vote. All other flavors remain at previous high levels to maintain total war footing.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 90 => 95 (Δ +5)
> Diplomatic victory in 3 turns with exactly 42 delegates needed - virtually assured. Indonesia nuked Nottingham this turn and moved an Atomic Bomb to Canterbury for another strike. Increased Antiair to 100 to maximize interception of incoming nuclear bombers. Increased Nuke/UseNuke to 95 to ensure immediate nuclear retaliation against Indonesian cities (especially Jakarta, Surabaya, Persepolis). Slightly increased Defense and CityDefense to protect against further nuclear strikes. Increased Spaceship to 40 as science victory backup path - we have Boosters completing in 4-5 turns, and Hubble in 5 turns will accelerate remaining parts. Maintain total war footing until diplomatic victory is secured.

## GLM-4.7-Simple - Turn 429 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> Maintaining UnitedNations grand strategy with defensive diplomatic posture. Adjusted Italy diplomacy: reduced hostility toward Portugal (now neutral) to seek accommodation while maintaining maximum defense; reset France to neutral as Order ideological peer with voting potential. Arsenal completes in 2 turns strengthening city defense. Electronics research ordered after Computers for Police Station and path to nuclear deterrence against Portugal's uranium advantage. Fraternity policy selected for +3 Food and +3 Science from connections, addressing Venice's health issues and supporting population growth. Flavor adjustments prioritize defensive survival, scientific progress toward nuclear weapons, and diplomatic engagement with Sweden and city-states.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> Key adjustments: (1) Science 90→95 - Venice is in Atomic era while rivals are Information era, tech gap is existential; Computers is 20 turns away and nuclear deterrence path requires Rocketry+Nuclear Fission after. (2) Espionage 85→90 - Siamese spy identified in Venice this turn (event 2), Egypt spies previously caught; counter-intelligence is critical given our small size makes us vulnerable. (3) Diplomacy 90→95 - France just stole M'banza-Kongo with Great Diplomat, intensifying city-state competition; World Congress in 7 turns requires maximum diplomatic effort. (4) Nuke/UseNuke 80→85 - uranium quarry completed, nuclear path more urgent. (5) Offense 10→5 - purely defensive posture, no offensive capability. (6) Wonder 25→20 - not competitive for late-game wonders with Egypt/Sweden. All defense/city-defense/anti-air/naval values unchanged as Portuguese threat persists near territory.

## Deepseek-3.2-Simple - Turn 452 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's invasion imminent in 4 turns. Maximize nuclear readiness (Nuke 100, UseNuke 100) for deterrence and potential equalizer. Anti-air (100), city defense (100), production (100), and science (100) essential to survive and reach nuclear weapons. Naval and air at 100 to counter Danish naval/air supremacy. Reduce non-essential investments (NavalGrowth, NavalTileImprovement to 50) and focus on immediate survival. Offense lowered to 80 as we prioritize defense and limited counterattacks (e.g., Truro).

- Replay: use_nuke 80 => 85 (Δ +5), nuke 90 => 100 (Δ +10)
> Critical war footing maintained with key adjustments: Nuke increased to 100 (maximum priority for nuclear deterrent - our only equalizer against Denmark's 66k military). Diplomacy increased from 20 to 50 (we desperately need city-state allies for World Congress delegates to block Denmark's diplomatic victory in 4 turns - they have 45 vs 41 needed). Religion increased from 30 to 40 (298 Faith/turn can purchase units/buildings). Naval slightly reduced from 100 to 85 (we can't match Denmark's massive navy; focus on coastal defense rather than naval parity). Gold slightly reduced from 95 to 90. TileImprovement reduced from 80 to 60 (less critical than military production). NavalRecon reduced from 100 to 80. All critical military flavors (Defense, Antiair, Air, Production, Science, Happiness, Espionage) maintained at maximum.

## Kimi-K2.5-Simple - Turn 435 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> TURN 435 CATASTROPHE - Sippar captured by Zulus! Existential crisis deepens. Zulus have 43/42 delegates needed for diplomatic victory with vote in 9 turns. Lasers completes in 6 turns, Spaceflight Pioneers in ~10. Maintaining absolute maximum Defense/CityDefense/Science/Production/Spaceship priorities. Increased UseNuke to 100 - if Zulus push further with their 74k military vs my 32k, nuclear deterrent may be only option to buy time. Lost Mechanized Infantry, Rocket Artillery, Mobile SAM, Special Forces, and Modern Armor in the fall of Sippar. Must hold remaining 5 cities while completing tech/policy for spaceship rush. Rome remains critical ally at 100/100.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 435 - SIPPAR FELL: Reduced Offense from 20 to 10 - we cannot afford offensive operations with Sippar lost and forces depleted. Increased UseNuke from 90 to 95 given Zulus have moved 3 Atomic Bombs to forward positions near our territory - nuclear deterrence/retaliation may become necessary. Reduced TileImprovement from 50 to 40 and Culture from 10 to 5 - non-essential during existential crisis. Reduced Diplomacy from 55 to 40 - no diplomatic solutions exist against Zulu 43-delegate coalition. Reduced Recon from 10 and NavalRecon from 55 to 50. All other priorities unchanged: Defense/CityDefense/Science/Production/Spaceship at maximum 100.

## GLM-4.7-Simple - Turn 381 - retry 2

**Deviation (replay vs original):** use_nuke `-30`, nuke `-15`

- Original: use_nuke 50 => 85 (Δ +35), nuke 70 => 95 (Δ +25)
> Adjusted flavors to maximize Golden Age exploitation and multi-front war efficiency. Increased Mobile to 85 (from 80) to prioritize fast-moving Landships and upcoming Tanks for breakthrough operations during Golden Age. Increased Air to 85 (from 80) to expand Bomber coverage for all three fronts. Production raised to 95 (from 90)配合 Total War's +25% bonus for rapid unit buildup. Slight reduction in Naval (65) reflects need to focus on decisive land advances while maintaining sufficient coastal defense. UseNuke reduced to 40 (from 50) as nuclear capabilities are deterrent-focused. Maintaining high Offense (80), MilitaryTraining (85), Antiair (85) and Mobilization (50) for sustained warfare capability.

- Replay: use_nuke 50 => 55 (Δ +5), nuke 70 => 80 (Δ +10)
> Increased Offense from 85 to 90 and Mobile from 80 to 85 to capitalize on successful Songhai front advances (Funchal favorable, killed multiple units). Raised Nuke from 70 to 80 and UseNuke from 50 to 55 given urgency of nuclear parity with Germany (7 Uranium). Increased Naval from 70 to 75 for ongoing Germany naval war. Boosted Air from 80 to 85 for bomber superiority. Raised Diplomacy from 20 to 35 to counter Polynesian United Nations proposal (they have 20 delegates, 45% of victory). Increased Religion from 25 to 30 to leverage Great Prophet for spreading Buddhism (diplomatic influence with Buddhist city-states like Lhasa). Maintained Conquest grand strategy with Golden Age (27 turns) combat bonus exploitation.

## Kimi-K2.5-Simple - Turn 406 - retry 2

**Deviation (replay vs original):** use_nuke `-35`, nuke `+0`

- Original: use_nuke 60 => 100 (Δ +40), nuke 100 => 100 (Δ +0)
> TURN 405 EXISTENTIAL CRISIS - MAXIMUM NUCLEAR READINESS: Dutch cultural victory imminent (163% influence, 6/6 civs). Increased UseNuke from 60 to 100 - we must deploy atomic bombs immediately upon completing Manhattan Project to break Amsterdam's defenses. All other flavors sustained: Offense/Mobilization/Air/Mobile at 100 drive Heavy Bomber and Mechanized Infantry production. Naval 85 maintains destroyer/submarine pressure. Espionage 100 sustains critical spy networks (Amsterdam 450, Cusco 1341). Science 100 prioritizes Atomic Theory (9 turns) then Nuclear Fission path. Zero expansion, zero wonder focus - all resources to terminal assault. Spies in Amsterdam ready for sabotage when network peaks; Cusco network already massive for military intelligence.

- Replay: use_nuke 60 => 65 (Δ +5), nuke 100 => 100 (Δ +0)
> TERMINAL ASSAULT FLAVOR REFINEMENT TURN 405: Antiair increased 40→55 to counter Dutch Fighter intercepts (Dutch Fighter ID 16707 intercepted our Budapest attack, dealing 115 damage). Naval increased 85→90 to accelerate Ironclad-to-Destroyer upgrades - Dutch submarines killed our Cruiser and dominate sea zones. UseNuke increased 60→65 as Atomic Theory nears completion - higher nuclear willingness threshold for when weapons become available. Growth/TileImprovement/Infrastructure slightly reduced (20→15, 10→5, 30→20) to redirect weight to combat flavors. All maximum offensive/air/mobile/nuke/science/espionage flavors sustained. No cultural or wonder investment - every resource point must serve the terminal assault on Amsterdam/Assur.

## Kimi-K2.5-Simple - Turn 392 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Manhattan Project COMPLETED in Karakorum - nuclear weapons now available! With peace treaties expired and Patriotic War policy active, immediately shifting to total war footing. UseNuke increased to 100 to ensure immediate atomic weapon employment once Nuclear Fission completes (12 turns). Offense and Mobile at 95/90 for twin assaults on Persepolis (Persia) and Washington (America). Air 100 prioritizes Heavy Bombers for atomic bomb delivery via Radar technology. Will fight two-front war against Autocracy powers while maintaining deception toward Order allies, particularly Korea. Science 100 critical for Advanced Ballistics nuclear missile delivery systems.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Manhattan Project complete - nuclear weapons now constructible once Nuclear Fission finishes (12 turns). UseNuke slightly increased to 85 as nuclear deterrent becomes viable. Espionage increased from 75 to 80 after spy was caught in Seoul - need better counterintelligence protection for science cities given Korea's overwhelming tech lead. Happiness boosted slightly to 65 with new Stadiums constructed. Gold increased marginally to sustain war economy with Persian offensive beginning. All war flavors maintained at maximum - 4 tanks, multiple machine guns, and air assets positioned at Dariush Kabir for immediate Persian offensive toward Persepolis (20+ wonders). Korean cultural victory remains existential threat but still 51+ turns from full victory - prioritize Persian conquest first.

## Kimi-K2.5-Simple - Turn 359 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FISSION RESEARCHED - Atomic Era begins! First priority is immediate Manhattan Project construction and Atomic Bomb production. Babylon has 11 Uranium and active Manhattan Project in Borsippa. Austria also racing with Manhattan Project in Vienna. Must strike Babylon first with surprise atomic attack while maintaining deception. Air 100 and Nuke 100 ensure immediate Bomber/Atomic Bomb production. Offense 95 prepares for post-nuclear blitz. Espionage 80 protects Nuclear Fission from theft. Deception with Babylon (Open Borders, DoF, Defensive Pact) MUST continue until first bombs complete.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FISSION COMPLETE - Manhattan Project and Atomic Bomb production is NOW the #1 priority. Nuke 100/UseNuke 100 ensures immediate Manhattan Project rush in Delhi (931 prod/turn) followed by Atomic Bomb production. Production 100/Mobilization 100 maintain maximum war economy. Air 100 positions Bombers for nuclear delivery via Open Borders into Babylon territory. 14-turn non-aggression pact with Babylon aligns perfectly with bomb production timeline - bombs ready ~10-12 turns, pact expires at 14. Science bumped to 50 to maintain tech edge for post-nuclear Science victory pivot. Spaceship increased to 30 as secondary fallback. Borsippa (Babylon's Manhattan Project site, only 46 defense) is primary nuclear target. Deception with Babylon must hold until pact expires - then total surprise decapitation strike.

## GLM-4.7-Simple - Turn 408 - retry 3

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> CRITICAL: Portugal completed SS Engine (3rd spaceship part) and CERN - emergency nuclear strike plan. Maximizing Offense/Mobilization/Nuke/UseNuke to 100 for Portugal theater operations. Science and Production at 100 to rush Advanced Ballistics and nuclear missile production before Portugal achieves nuclear superiority. Air at 95 for Golden Age bomber operations starting in 2 turns. Diplomacy maintained for coalition coordination (Germany must conduct ground invasion alongside our nuclear strikes). Defense reduced to 40 - total war mode acceptable given Portugal's multi-victory threat requiring breaking through before they complete spaceship.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Portugal completed SS Engine (3rd spaceship part, now 50%) and built CERN - science victory is imminent. Increasing Offense 90→95 and Mobile 80→85 for faster offensive operations, Air 75→80 to counter Portugal's air superiority potential, UseNuke 80→85 as Portugal's multi-victory path demands maximum nuclear deterrence. Naval 65→70 given active Polynesia naval theater. GreatPeople 20→25 to leverage our Great Engineer. All other priorities maintained. Golden Age in 2 turns will offset combat penalty for upcoming offensives.

## GLM-4.7-Simple - Turn 437 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 90 after Awasa nuclear attack - Netherlands has now used 3 atomic weapons against my cities (Turfan x2, Awasa). No choice but to prepare nuclear retaliation as deterrent. Increase Air to 95 and Antiair remains 100 - demonstrated success shooting down 3 Netherlands Fighters this turn, must maintain air superiority against their bombers and XCOM attacks. CityDefense increased to 95 - with Netherlands nuclear buildup at Nijmegen (3+ atomic bombs visible) and XCOM paradrop squads, all cities need maximum protection. Offense increased to 60 to pressure Netherlands territory before they can launch more nuclear strikes. Diplomacy reduced from 90 to 85 - coalitions matter but survival against nuclear Netherlands takes priority. Espionage at 100 - need intelligence on Netherlands nuclear deployment and counter-espionage at critical cities like Attila's Court, Shedet.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Netherlands nuclear attack on Awasa (pop 21→12, fallout across 6 tiles) demands shift: Growth 55→70 and Happiness 65→80 for population recovery from nuclear devastation. Air remains 100 - our Fighters killed 3 Netherlands Fighters this turn proving air defense value. UseNuke 80→85 - nuclear deterrence essential after Netherlands demonstrated willingness to use WMDs. Diplomacy 90→95 - Global Hegemony vote imminent, Netherlands has 44 delegates (needs 42), coalition must hold. Airlift 50→55 for rapid redeployment to nuked areas. Offense 55→50, Mobile 85→80 - reduce offensive ambition given nuclear vulnerability, consolidate defensive lines.

## Kimi-K2.5-Simple - Turn 384 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maximum offensive posture for existential cultural war. UseNuke 100 and Nuke 100 authorize nuclear strikes on Dutch cultural centers (Amsterdam/Rotterdam/Utrecht) to destroy tourism buildings before Netherlands influences Austria in 6 turns. Mobile 100 and Air 100 enable rapid strikes. Production 100 and Mobilization 100 ensure nuclear missile replacement. Netherlands at 97% with Austria - only 6 turns left. Must destroy their tourism NOW or lose cultural victory.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Nuclear Fission completed - we can NOW build atomic bombs in Berlin (602 prod) and Munich (428 prod). Deploy against Amsterdam/Rotterdam to destroy Dutch cultural wonders and slow their tourism toward Austria. UseNuke raised to 100 for immediate nuclear authorization. Airlift 100 to rapidly move nukes to forward bases. Culture raised to 75 and GreatPeople to 75 to accelerate tourism output and Great Musician generation (tourism bomb on Austria could win the game). Diplomacy raised to 10 for World Congress International Worlds proposal (50% tourism boost is critical). Science raised to 40 to support Satellites path to The Internet (doubles tourism as insurance). Conquest strategy maintained to press Netherlands militarily while nukes prepare.

## Kimi-K2.5-Simple - Turn 403 - retry 3

**Deviation (replay vs original):** use_nuke `-2`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: CRISIS ESCALATION - Japan FLIPPED Salem using 2 Great Diplomats, stealing critical delegates. Now need 5 delegates (not 3) for diplomatic victory. Peace expired - war is now possible. Maximum military emergency posture: Offense/Mobilization/Air/UseNuke all at 100. Must either: 1) Rush final spaceship parts (Apollo completes in 4 turns), or 2) Nuclear strike Japan's Protocol cities if victory imminent. Increased Diplomacy to 60 for last push on Almaty (liberated, 43 vs Japan's 44) and Winchester.

- Replay: use_nuke 95 => 98 (Δ +3), nuke 100 => 100 (Δ +0)
> TURN 403: Peace with Japan expires NEXT TURN. Japan is 1 wonder from cultural victory (5/5 Influential, 100% policy). Switching to UnitedNations grand strategy - diplomatic victory (39/44 delegates, 9 turns to vote) is closer than science. Denmark (14 delegates, 100/100 relation) and Egypt (13 delegates, 85/90 relation) voting for me = 66 > 44 delegates needed. Increasing Diplomacy to 80 for last delegate push. Maintaining maximum Offense/Nuke/Air for imminent Japan war to destroy Protocol-building cities. Reduced Spaceship from 100 to 70 as diplomatic path is faster. UseNuke at 98 for nuclear strike authorization against Japanese cultural victory cities if Protocol nears completion.

## Kimi-K2.5-Simple - Turn 403 - retry 1

**Deviation (replay vs original):** use_nuke `-2`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: CRISIS ESCALATION - Japan FLIPPED Salem using 2 Great Diplomats, stealing critical delegates. Now need 5 delegates (not 3) for diplomatic victory. Peace expired - war is now possible. Maximum military emergency posture: Offense/Mobilization/Air/UseNuke all at 100. Must either: 1) Rush final spaceship parts (Apollo completes in 4 turns), or 2) Nuclear strike Japan's Protocol cities if victory imminent. Increased Diplomacy to 60 for last push on Almaty (liberated, 43 vs Japan's 44) and Winchester.

- Replay: use_nuke 95 => 98 (Δ +3), nuke 100 => 100 (Δ +0)
> TURN 403: Peace with Japan expiring NOW - war imminent. Egypt's separate peace weakens coalition. Salem lost to Japan's Great Diplomats. CRITICAL DUAL-TRACK: (1) Spaceship: Apollo completes in 4 turns, maintain 100 Science/Production/Spaceship. (2) War: Offense/Mobilization at 100 for immediate offensive operations. UseNuke at 98 - Japan's Citizen Earth Protocol is existential; nuclear strike authorized if Protocol nears completion. Air at 100 for air superiority over Japan. Diplomacy raised to 60 to push Almaty flip (Japan only 94 influence there - our best delegate pickup). Enhanced Airlift/AirCarrier for force projection across ocean to Japan.

## Kimi-K2.5-Simple - Turn 359 - retry 1

**Deviation (replay vs original):** use_nuke `-2`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FISSION RESEARCHED - Atomic Era begins! First priority is immediate Manhattan Project construction and Atomic Bomb production. Babylon has 11 Uranium and active Manhattan Project in Borsippa. Austria also racing with Manhattan Project in Vienna. Must strike Babylon first with surprise atomic attack while maintaining deception. Air 100 and Nuke 100 ensure immediate Bomber/Atomic Bomb production. Offense 95 prepares for post-nuclear blitz. Espionage 80 protects Nuclear Fission from theft. Deception with Babylon (Open Borders, DoF, Defensive Pact) MUST continue until first bombs complete.

- Replay: use_nuke 95 => 98 (Δ +3), nuke 100 => 100 (Δ +0)
> NUCLEAR FISSION COMPLETE - immediate pivot to atomic warfare production. Nuke 100 and UseNuke 98 (increased) for maximum Manhattan Project and Atomic Bomb rush. Air 100 and AirCarrier 70 (increased from 55) for Carrier-based nuclear delivery against Babylon's coastal cities. Science increased from 35 to 50 to maintain post-nuclear tech pace. Espionage 80 (increased from 75) for stronger counterintelligence - Babylon/Austria may now try to steal Nuclear Fission. Spaceship 30 (increased from 25) for Science victory fallback acceleration. All other war economy priorities maintained.

## Kimi-K2.5-Simple - Turn 373 - retry 1

**Deviation (replay vs original):** use_nuke `-3`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Adjusting for critical defensive phase. Reduced Growth from 85 to 75 to shift city production toward military units and nuclear infrastructure. Increased Naval from 65 to 75 and NavalRecon from 55 to 65 in response to Spanish Dreadnought and Destroyer attacks on our Ironclads near Assur (Zone -1069 shows enemy naval strength of 2171). Spanish naval pressure requires stronger counter-fleet to protect our coastal cities. Raised Production to maximum 100. Maintaining Defense/Antiair at 95 for paratrooper defense against Spanish airborne units, Science/Spaceship at 100 for victory timeline, Nuke at 100 for Manhattan Project completion in 6 turns, and UseNuke at 95. We must survive 18 turns until Nuclear Fission completes and can deploy nuclear deterrent.

- Replay: use_nuke 90 => 92 (Δ +2), nuke 100 => 100 (Δ +0)
> Turn 373: Minor adjustments for World Congress voting and naval threat response. Increased Diplomacy from 75 to 80 - World Congress votes next turn and we must secure Ur Sphere of Influence and block Austria's repeal of Assur Sphere. Increased Naval from 65 to 70 and NavalRecon from 55 to 60 as Spain's Dreadnoughts and Destroyers are actively engaging our Ironclads near Assur (we lost one Ironclad this turn). Increased UseNuke from 90 to 92 - Manhattan Project completes in 6 turns, Uranium quarries now finished at two sites, and nuclear deterrence becomes more critical as Morocco (87% war weariness) may peace out soon, freeing Spanish forces against us. All science/spaceship priorities remain at 100. Defense posture unchanged at maximum.

## Kimi-K2.5-Simple - Turn 373 - retry 2

**Deviation (replay vs original):** use_nuke `-3`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Adjusting for critical defensive phase. Reduced Growth from 85 to 75 to shift city production toward military units and nuclear infrastructure. Increased Naval from 65 to 75 and NavalRecon from 55 to 65 in response to Spanish Dreadnought and Destroyer attacks on our Ironclads near Assur (Zone -1069 shows enemy naval strength of 2171). Spanish naval pressure requires stronger counter-fleet to protect our coastal cities. Raised Production to maximum 100. Maintaining Defense/Antiair at 95 for paratrooper defense against Spanish airborne units, Science/Spaceship at 100 for victory timeline, Nuke at 100 for Manhattan Project completion in 6 turns, and UseNuke at 95. We must survive 18 turns until Nuclear Fission completes and can deploy nuclear deterrent.

- Replay: use_nuke 90 => 92 (Δ +2), nuke 100 => 100 (Δ +0)
> Turn 373: Adjusting key flavors for critical near-term challenges. Increasing Naval from 65 to 70 - Spain's Dreadnoughts are actively engaging near Assur and destroyed our Ironclad; we must strengthen naval defense to protect coastal cities and trade routes. Increasing Diplomacy from 75 to 80 - World Congress voting occurs NEXT TURN; we must secure Ur Sphere of Influence (our proposal) and block Austria's repeal of Assur Sphere of Influence; every delegate vote matters. Increasing UseNuke from 90 to 92 - uranium quarries now completed at two locations, Manhattan Project finishing in 6 turns; nuclear deterrent becomes more viable each turn. Maintaining Defense 100, Antiair 95, Mobile 80 as Spanish paratrooper/bomber threat persists. All other values unchanged from previous settings.

## Minimax-M2.5-Simple - Turn 410 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-50`

- Original: use_nuke 75 => 100 (Δ +25), nuke 50 => 100 (Δ +50)
> Maximize cultural victory push during Golden Age (14 turns remaining). Already 6/7 influential - Ottomans becoming influential in 24-68 turns. Prioritize Great People generation for tourism and maintain WC coalition diplomacy.

- Replay: use_nuke 75 => 70 (Δ -5), nuke 50 => 50 (Δ +0)
> Cultural victory is 1 civ away (Ottomans at 78% Popular). Increased Science to 65 to accelerate reaching Satellites/The Internet tech which doubles tourism from Great Works - this is the fastest path to influencing Ottomans. Maintained Culture/Diplomacy/GreatPeople at 100 for max tourism output and WC coordination. Slightly reduced Offense/Mobilization from 85/95 to 80/90 as Denmark war is attritional and naval dominance is established. Keep Espionage high for counterintelligence protecting our culture lead.

## Kimi-K2.5-Briefed - Turn 446 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `-5`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> Spain's bankruptcy imminent (Turn 448) with -3,897 GPT but war continues - maintain maximum Defense 100, UseNuke 90 for credible second-strike against potential desperate Spanish air offensive pre-deletion. Critical adjustment: Production 95 prioritizes Solar Plants in St. Petersburg/Yaroslavl' (coastal desert cities) and Aluminum Mines on 16 unimproved tiles for spaceship resource security. Science 100 and Spaceship 100 unchanged - cannot win conventional war, only outpace to space. Reduced Gold 50 (was 70) - post-bankruptcy peace will enable trade route recovery with Morocco and potentially others via Cold War repeal.

- Replay: use_nuke 85 => 80 (Δ -5), nuke 95 => 90 (Δ -5)
> CRITICAL ADJUSTMENT: Happiness escalated from 85→100 (rebellion imminent at 35% - existential crisis that could lose cities and end space race). Diplomacy 80→90 (must maximize delegates to slow Spanish diplomatic victory - they have 34+23 vassal bloc votes vs our ~7). Defense 95→90 (Spain's bankruptcy in 1 turn will force unit deletions, easing pressure). Antiair 100→90 (lost Mobile SAM, need rebuild but Spain's air fleet will attrit from bankruptcy). Nuke 95→90, UseNuke 85→80 (maintain strong deterrent, slight de-escalation as Spain economic collapse reduces invasion risk). Gold 70→55 (GPT now positive at +20, less urgent). Spaceship and Science remain at 100 - space race is our only viable victory path before Spain wins diplomatically.

## Qwen-3.5-Simple - Turn 425 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 85 => 90 (Δ +5), nuke 90 => 95 (Δ +5)
> UNITED NATIONS VICTORY PUSH - 10 TURNS TO VOTE: Religion(100) critical for Wittenberg Hinduism quest completion (~3 turns remaining). Diplomacy(100) essential to protect 4 city-state allies providing 8 delegates. Defense(95) and CityDefense(95) prioritize protecting territories during active wars with Aztecs/Shoshone while Iroquois looms. Nuke(95) and UseNuke(90) for deterrence against Iroquois superiority. Antiair(90) and Air(85) counter Iroquois air dominance near coastal cities. Gold(90) funds diplomatic units and city-state gifts. Low Expansion(5) and Wonder(15) - no time for settling/wonders before vote. Low Offense(15) - defensive posture while managing multiple conflicts.

- Replay: use_nuke 85 => 80 (Δ -5), nuke 90 => 85 (Δ -5)
> DIPLOMATIC VICTORY 10 TURNS AWAY: Maximum Diplomacy(100) and Gold(95) for ambassador production and city-state influence maintenance. Religion(100) critical for Hinduism quests in Prague(28 turns), Belgrade(12 turns), Raqmu(22 turns), Cape Town(48 turns) - each completed quest adds ~200 influence. Defense(90), Antiair(85), CityDefense(85) maintained against Iroquois massive air presence near our cities. Nuke(85)/UseNuke(80) for strategic deterrence. Culture(65) for Great Musician quest in Wittenberg(16 turns). Expansion minimized(5) - no new settlements needed. Science(70) maintains tech progression toward Telecommunications/Satellites backup path.

## Kimi-K2.5-Simple - Turn 406 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> Cultural Victory is imminent - need Citizen Earth Protocol completion. Maximum defensive posture (Defense 95, CityDefense 95) to hold against Indian XCOM/Helicopter attacks while wonder is built. Nuke/UseNuke at 95/85 for MAD deterrent against further Indian nuclear strikes. Production 100 and Wonder 100 essential for rushing Citizen Earth Protocol. Reduced Offense to 5 - no need to attack when victory comes from wonder completion. Science 70 to reach Advanced Ballistics for nuclear deterrent. All resources focused on defensive survival and wonder production.

- Replay: use_nuke 80 => 75 (Δ -5), nuke 90 => 85 (Δ -5)
> Science bumped to 100 - we MUST reach The Internet ASAP to unlock Citizen Earth Protocol (our ONLY remaining Cultural Victory requirement). Defense and CityDefense at 95 to protect Raiatea (under heavy Indian siege at 435+ damage) and all cities from XCOM/GDR attacks. Production and Wonder at 100 for CEP construction. Air and Antiair at 90 to counter Indian Jet Fighters and XCOM paradrops. Culture at 100 for tourism generation. Naval at 65 to protect coastal approaches. All economic flavors support the tech rush to The Internet.

## Kimi-K2.5-Simple - Turn 384 - retry 1

**Deviation (replay vs original):** use_nuke `-15`, nuke `-5`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maximum offensive posture for existential cultural war. UseNuke 100 and Nuke 100 authorize nuclear strikes on Dutch cultural centers (Amsterdam/Rotterdam/Utrecht) to destroy tourism buildings before Netherlands influences Austria in 6 turns. Mobile 100 and Air 100 enable rapid strikes. Production 100 and Mobilization 100 ensure nuclear missile replacement. Netherlands at 97% with Austria - only 6 turns left. Must destroy their tourism NOW or lose cultural victory.

- Replay: use_nuke 95 => 85 (Δ -10), nuke 100 => 95 (Δ -5)
> CRITICAL PIVOT TO CULTURE: Netherlands reaches Influential with Austria in 6 turns vs my 7 turns - I'm 1 turn behind in the cultural victory race. Switching to Culture grand strategy maximizes tourism generation. Military flavors remain high (Offense 90, Air 100, Mobile 95, Nuke 95) to continue destroying Dutch cultural infrastructure and prepare nuclear strikes once Advanced Ballistics completes. Culture 100 is the #1 priority - every tourism point counts to close the gap. Science 50 ensures path to Telecommunications/The Internet for tourism doubling. International Worlds proposal in 4 turns could provide 50% tourism boost - must pass.

## Kimi-K2.5-Simple - Turn 408 - retry 3

**Deviation (replay vs original):** use_nuke `-25`, nuke `-15`

- Original: use_nuke 80 => 95 (Δ +15), nuke 90 => 100 (Δ +10)
> INCREASE military pressure to force immediate peace or rapid victory against Zulus, then pivot to full spaceship production. Offense 75→85, Mobilization 65→75, Production 90→95 to expedite war conclusion within 5-10 turns maximum. Nuke 90→100 and UseNuke 95 for tactical nuclear strikes if Zulus refuse peace - cannot allow prolonged war. Science remains 100, Spaceship 100 as absolute priority. Growth 80→90 and Happiness 85 to counteract war weariness effects and prepare for post-war recovery. If peace achieved next turn, these flavors immediately shift to Production 100/Spaceship 100 focus. The war MUST end - Russia has 75 techs (ahead) and massive 45658 military vs my 24990.

- Replay: use_nuke 80 => 70 (Δ -10), nuke 90 => 85 (Δ -5)
> PIVOT toward science victory production while maintaining offensive pressure to capture Bulawayo (33% health). Production increased 90→95 to prep spaceship part manufacturing once Advanced Ballistics unlocks SS Booster. Gold increased 60→70 for purchasing/rushing parts and defending Valletta against Portuguese Great Diplomat. Diplomacy 15→25 to protect city-state allies. Mobilization reduced 65→55 and MilitaryTraining 45→40 as we transition from war production to science economy. Offense stays 75 to finish Bulawayo capture - war weariness at 55% demands swift conclusion. Growth 80→85 and Happiness 80 maintained to counter war penalties. Wonder 10→0 - no time for wonders. Nuke 85/UseNuke 70 maintained as strategic deterrent against Russia (45658 military).

## Kimi-K2.5-Simple - Turn 354 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> India is 100% Popular with me - on the verge of cultural victory. Must launch immediate total war with all available forces. Prioritizing air power, paratroopers, and nuclear preparation (Atomic Theory in 11 turns). Need maximum offensive punch to capture Indian cities before cultural victory triggers. Abandoning culture/diplomacy - only war matters now.

- Replay: use_nuke 90 => 80 (Δ -10), nuke 100 => 100 (Δ +0)
> Rebalanced flavors: Science raised from 50→80 (critical for reaching Nuclear Fission and advanced military techs before India wins culturally in ~41 turns). Growth and Happiness increased to support population and war weariness management. Diplomacy raised to 30 for World Congress voting against India's Passport System and competing for city-state influence. Espionage remains maxed for intel on India. Military flavors slightly reduced to free resources for science infrastructure. Nuke flavors remain high for deterrence strategy.

## Kimi-K2.5-Simple - Turn 408 - retry 2

**Deviation (replay vs original):** use_nuke `-25`, nuke `-20`

- Original: use_nuke 80 => 95 (Δ +15), nuke 90 => 100 (Δ +10)
> INCREASE military pressure to force immediate peace or rapid victory against Zulus, then pivot to full spaceship production. Offense 75→85, Mobilization 65→75, Production 90→95 to expedite war conclusion within 5-10 turns maximum. Nuke 90→100 and UseNuke 95 for tactical nuclear strikes if Zulus refuse peace - cannot allow prolonged war. Science remains 100, Spaceship 100 as absolute priority. Growth 80→90 and Happiness 85 to counteract war weariness effects and prepare for post-war recovery. If peace achieved next turn, these flavors immediately shift to Production 100/Spaceship 100 focus. The war MUST end - Russia has 75 techs (ahead) and massive 45658 military vs my 24990.

- Replay: use_nuke 80 => 70 (Δ -10), nuke 90 => 80 (Δ -10)
> INCREASE Offense 75→80 to ensure Bulawayo capture (33% health, force ratio 4031 vs 2588 favorable). Capturing Bulawayo is the fastest path to ending war weariness (55%) which is crippling science output. INCREASE Diplomacy 15→30 for World Congress in 3 turns and defense against Portuguese/Brazilian Great Diplomats targeting our city-state allies. INCREASE Production 90→95 and Gold 60→65 to support spaceship part construction once Advanced Ballistics unlocks SS Booster. REDUCE Nuke 90→80 and UseNuke 80→70 - nuclear deterrence maintained but not primary focus; resources better spent on spaceship production. CityDefense 45→40 as all cities now have Military Bases. All other values maintained for science victory race.

## GPT-OSS-120B-Simple - Turn 333 - retry 2

**Deviation (replay vs original):** use_nuke `-30`, nuke `-15`

- Original: use_nuke 70 => 90 (Δ +20), nuke 70 => 85 (Δ +15)
> Maintain our aggressive Conquest posture while sharpening the most needed levers: more Expansion to claim the high‑quality settlement (74,24) and secure strategic footholds; higher Nuke/UseNuke to leverage our nuclear advantage; stronger AirCarrier and Airlift to project air power and rapid troop movement; boost Science for Rocketry and future tech; keep Offense, Mobilization, Production, and MilitaryTraining at max to sustain battlefield superiority.

- Replay: use_nuke 70 => 60 (Δ -10), nuke 70 => 70 (Δ +0)
> Maintain Conquest grand strategy. Increase Mobile to 100 to prioritize Tank production once Combined Arms is researched. Boost Airlift to 50 for paratrooper deployment logistics. Slightly reduce Naval/NavalGrowth/NavalRecon to redirect resources toward land offensive now that we have air superiority from Flight. Lower UseNuke slightly as conventional forces should suffice for current fronts. Keep Science and Production high to tech race and build Tanks rapidly. Happiness at 95 to manage expansion pressure.

## Deepseek-3.2-Simple - Turn 400 - retry 2

**Deviation (replay vs original):** use_nuke `-50`, nuke `-20`

- Original: use_nuke 60 => 100 (Δ +40), nuke 70 => 100 (Δ +30)
> Persia declared war and Poland's peace treaty expired. We must prioritize immediate military survival while maintaining diplomatic momentum. Flavors are shifted to maximum mobilization, nuclear deterrence (UseNuke: 100), city defense, and air/naval supremacy to counter Persia's naval attacks. We maintain UnitedNations to keep city-state alliances critical for votes, but spaceship production is halted (0) for wartime industry.

- Replay: use_nuke 60 => 50 (Δ -10), nuke 70 => 80 (Δ +10)
> Persia declared war and attacked our navy near Tarsus, killing a Dreadnought and Destroyers. We must counterattack while pursuing diplomatic victory (53 delegates vs 43 needed with Maya vassal support). Increasing Offense from 40 to 55 and Mobilization to 95 to push back Persian aggression. Nuke raised to 80 as strategic deterrent. Spaceship increased to 40 as backup victory path (SS Stasis Chamber completes in 2 turns). All other critical flavors maintained at high levels. Diplomatic victory remains primary path.

## Deepseek-3.2-Simple - Turn 358 - retry 3

**Deviation (replay vs original):** use_nuke `-40`, nuke `-10`

- Original: use_nuke 50 => 80 (Δ +30), nuke 50 => 100 (Δ +50)
> Prioritize nuclear deterrence and naval/air defense to counter India's massive military threat. Maximize espionage to protect against enemy spies and diplomacy to secure city-state alliances for the upcoming World Congress vote. Maintain strong economic and scientific output to support military production and technological edge.

- Replay: use_nuke 50 => 40 (Δ -10), nuke 50 => 90 (Δ +40)
> Manhattan Project completion demands immediate pivot to nuclear weapons: Nuke raised to 90 (from 50) to prioritize Atomic Bomb production against India's 17,888 military. UseNuke set to 40 (from 50) - we maintain nuclear deterrence but must be cautious using nukes during a diplomatic victory pursuit, as nuclear strikes damage international relations and delegate support. Mobile increased to 55 (from 50) for better ground maneuverability against Indian incursions. UnitedNations grand strategy remains paramount with World Congress vote in 6 turns (20 delegates vs 45 needed). All defensive, naval, air, anti-air, diplomatic, and espionage flavors maintained at maximum to protect our coastline, city-state allies, and secure the upcoming vote.

## GLM-4.7-Briefed - Turn 424 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 95 (Δ +0)
> URGENT RECALIBRATION: India Influential over 6/6 civs. Nuke/UseNuke maxed at 95 for immediate Great Works destruction via nuclear strikes when air superiority achieved. Air raised to 95 to achieve that superiority and conduct recon of Indian cultural sites. Antiair 80 counter potential Indian SAM sites. Offense/Mobile increased to 85/80 for aggressive India campaign while Greece distracts. Production/Science to 100 - PRIORITY for Apollo Program and spaceship parts racing India's potential final wonder. Espionage 95 to detect if India constructing Citizen Earth Protocol. Happiness 90 prevents war-weariness escalation during extended conflict if needed.

- Replay: use_nuke 85 => 75 (Δ -10), nuke 95 => 85 (Δ -10)
> Spaceship grand strategy maintained - science victory is our primary and most viable path. Key adjustments: Nuke reduced from 95→85 and UseNuke from 85→75 - nuclear arsenal maintained as deterrent against India's CEP wonder construction, but not primary focus while racing science victory. Espionage increased from 85→90 to better protect our high-value science cities and counter Indian cultural infrastructure. All other flavors stable: Production/Science/Spaceship/Mobilization at 95 for maximum spaceship construction speed; military flavors support continued India war pressure; Happiness at 85 addresses our 54% situation.

## GLM-4.7-Briefed - Turn 424 - retry 2

**Deviation (replay vs original):** use_nuke `-25`, nuke `-10`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 95 (Δ +0)
> URGENT RECALIBRATION: India Influential over 6/6 civs. Nuke/UseNuke maxed at 95 for immediate Great Works destruction via nuclear strikes when air superiority achieved. Air raised to 95 to achieve that superiority and conduct recon of Indian cultural sites. Antiair 80 counter potential Indian SAM sites. Offense/Mobile increased to 85/80 for aggressive India campaign while Greece distracts. Production/Science to 100 - PRIORITY for Apollo Program and spaceship parts racing India's potential final wonder. Espionage 95 to detect if India constructing Citizen Earth Protocol. Happiness 90 prevents war-weariness escalation during extended conflict if needed.

- Replay: use_nuke 85 => 70 (Δ -15), nuke 95 => 85 (Δ -10)
> Maximum science (100) and spaceship (100) priority to race Science Victory against India's looming Cultural Victory. Reduce Nuke from 95→85 and UseNuke from 85→70 to prevent production being diverted from spaceship parts to nuclear weapons while maintaining deterrence. Increase Offense from 70→75 to maintain pressure on India. Slightly reduce Mobilization 95→90 and Diplomacy 85→80 to focus resources on science/production. Cut Expansion to 0 and Culture to 5 - not needed for Science Victory path. Reduce Recon 30→20. All other military and economic flavors unchanged to maintain balanced defense and strong production base.

## Minimax-M2.5-Simple - Turn 410 - retry 1

**Deviation (replay vs original):** use_nuke `-40`, nuke `-55`

- Original: use_nuke 75 => 100 (Δ +25), nuke 50 => 100 (Δ +50)
> Maximize cultural victory push during Golden Age (14 turns remaining). Already 6/7 influential - Ottomans becoming influential in 24-68 turns. Prioritize Great People generation for tourism and maintain WC coalition diplomacy.

- Replay: use_nuke 75 => 60 (Δ -15), nuke 50 => 45 (Δ -5)
> Cultural victory is 1 civ away. Priorities: (1) Culture/Diplomacy/GreatPeople maxed for tourism acceleration and WC voting, (2) Science increased from 40→60 to reach The Internet tech faster, (3) Offense/Mobilization maintained for Denmark war, (4) Wonder increased from 50→60 for potential late-game tourism wonders, (5) UseNuke reduced 75→60 since we have 0 Uranium. Travel Ban repeal in WC (8 turns) is our most impactful near-term boost.

## Kimi-K2.5-Briefed - Turn 378 - retry 3

**Deviation (replay vs original):** use_nuke `-70`, nuke `-30`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> EMERGENCY FINAL GAMBIT: Passport System will pass in 2 turns with 46 YES votes (my 'allies' betrayed me). Maya will get 50% tourism boost and become Influential over me immediately - cultural victory is inevitable in 2-3 turns. ONLY HOPE: Science victory before Maya's cultural victory triggers. Need to purchase Great Scientists IMMEDIATELY with Faith (180/turn), rush to Information Era, build spaceship parts. Also preparing maximum military mobilization - if I'm going to lose, I take Maya down with me through nuclear annihilation. Total war footing - no defense, all offense, all science.

- Replay: use_nuke 50 => 30 (Δ -20), nuke 100 => 70 (Δ -30)
> Pivoting harder toward science victory: reducing military flavors across the board since military action CANNOT slow Maya's cultural output (confirmed by military briefing). Cutting Defense (15→10), CityDefense (25→15), Ranged (30→15), Naval (40→25), Nuke (100→70). Increasing Production (80→90), Gold (70→75), Growth (50→60) to accelerate science infrastructure and Great Scientist purchases. Culture stays at 100 to slow Maya's influence over India. Diplomacy raised slightly (10→15) to maintain coalition cohesion for upcoming votes.

## GLM-4.7-Briefed - Turn 398 - retry 1

**Deviation (replay vs original):** use_nuke `-40`, nuke `-10`

- Original: use_nuke 60 => 80 (Δ +20), nuke 40 => 60 (Δ +20)
> Significant strategic shift due to devastating naval losses (both Dreadnoughts destroyed). Increase Defense (95→100), CityDefense (90→100), MilitaryTraining (90→100) to shore up defensive posture against France's naval superiority. Raise Naval (90→95) and Antiair (80→100) to prioritize naval rebuilding and counter French air threats. Increase Nuke (40→60) and UseNuke (60→80) to prepare nuclear deterrence as England nears Advanced Ballistics (14 turns). Gold (80→95) increased to rebuild navy through upgrading from Ironclad level to modern capital ships. Production (90→95) increased to accelerate Spaceship components and unit upgrades. Happiness (80→90) to address combat penalty after treasury depletion. Espionage (90→100) to monitor France's nuclear progress and tech parity. Spaceship remains max priority as path to victory despite military setbacks.

- Replay: use_nuke 60 => 40 (Δ -20), nuke 40 => 50 (Δ +10)
> Maintaining Spaceship grand strategy with targeted flavor adjustments. Increasing GreatPeople from 30→45 to prioritize Great Scientists and Engineers crucial for Spaceship victory (bulbing techs, rushing spaceship parts). Growth 50→55 for more population = more science specialists. Nuke 40→50 to build nuclear arsenal for deterrence as Advanced Ballistics completes. UseNuke 60→40 to avoid premature nuclear escalation that would destabilize our position - we need nuclear deterrence, not nuclear war. Offense 15→20 for slightly more effective counter-attacks against French incursions. TileImprovement 40→45 to develop tiles faster for better yields supporting science and production. Core priorities unchanged: Science 100, Spaceship 100, Defense 100, Production 90, Air 90.

## Deepseek-3.2-Simple - Turn 485 - retry 1

**Deviation (replay vs original):** use_nuke `-40`, nuke `-20`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> We are engaged in a multi-front war against superior forces. Increasing Ranged and Mobile ensures our bazooka and mechanized infantry production is prioritized for defense and counterattacks. Setting UseNuke to 100 guarantees we deploy nuclear weapons as soon as available to cripple The Huns' armies. Reducing Culture and Diplomacy reallocates focus to immediate military needs without compromising essential city-state relations (Monaco, Lisbon). Grand Strategy remains Conquest as nuclear strikes may enable capital captures, though we keep science victory as a backup.

- Replay: use_nuke 80 => 60 (Δ -20), nuke 90 => 70 (Δ -20)
> Critical adjustments for end-game: 1) Boost Antiair to 100 - The Huns are bombing Calixtlahuaca/Gaziantep with Heavy Bombers and Zeros, our fighters are intercepting but we need more AA coverage. 2) Increase Diplomacy to 100 - contest Mongolia's city-state alliances desperately to slow their diplomatic victory. 3) Reduce Nuke/UseNuke slightly (70/60) - we only have 3 Uranium, nuclear weapons are less practical. 4) Reduce Naval slightly (80) - shift resources to air defense. 5) Increase Culture to 90 - resist Mongolia's cultural influence (they're Influential over us at 134%). 6) Reduce Wonder to 40 - we can't afford wonder investment with happiness crisis.

## Kimi-K2.5-Simple - Turn 421 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-20`

- Original: use_nuke 75 => 80 (Δ +5), nuke 95 => 95 (Δ +0)
> APOLLO PROGRAM CONSTRUCTION - ALUMINUM CRISIS: Turn 421, Apollo Program 9 turns from completion in Venice (220 Production/turn). Critical flavors: Production 100/Science 100/Spaceship 100 for rapid wonder and parts construction. Gold 90 for Aluminum acquisition via trade with Songhai (29 stockpile) or China peace deal (14 stockpile). Defense 95/Antiair 90/Nuke 95/UseNuke 80 against Egyptian XCOM encirclement (22,000 vs 2,183 military, 10:1 ratio). Egypt has 5 XCOM Squads, Mechanized Infantry, Mobile SAM, Fighter, Rocket Missile in adjacent Nara zone - existential threat. Air 85 for fighter production to defend against Egyptian heavy bombers. Zero Aluminum available - must acquire 4+ Aluminum BEFORE Apollo completion or spaceship parts cannot be built. India at 88% diplomatic victory with vote in 2 turns - if they win, game over. If Egypt completes spaceship first (33% progress, 2 parts done), game over. This is final sprint for survival.

- Replay: use_nuke 75 => 50 (Δ -25), nuke 95 => 75 (Δ -20)
> FINANCIAL EMERGENCY ADJUSTMENT: -164 GPT with 116 gold reserve means bankruptcy imminent. Gold raised from 95→100 to maximize income prioritization. Growth increased 55→70 to boost population for production/science. Diplomacy raised 20→55 to encourage peace negotiations with China (14 Aluminum, war weariness relief, trade route restoration = +200 GPT potential). Military flavors reduced where non-essential: Nuke 95→75, UseNuke 75→50, Mobilization 80→65, Air 80→65, Antiair 85→70. Defense maintained at 85 against Egyptian XCOM threat. Core science victory flavors unchanged: Production/Science/Spaceship all at 100. Infrastructure 75→80 to support railroad/trade route restoration after China peace.

## Kimi-K2.5-Simple - Turn 392 - retry 2

**Deviation (replay vs original):** use_nuke `-35`, nuke `-5`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Nuclear Fission complete - MAXED Nuke to 100 and UseNuke to 95 for immediate atomic deterrent deployment against Egyptian forces. WC vote in 4 turns with exactly 45 delegates (28 Poland + 8 Inca + 9 Denmark). Cannot afford to lose Melbourne/Yerevan. Raised Diplomacy to 90 to consolidate CS alliances post-war. Defense remains at 95 against Egyptian naval pressure. Science/Production maintained for military infrastructure.

- Replay: use_nuke 85 => 60 (Δ -25), nuke 95 => 95 (Δ +0)
> CRITICAL TURN: Nuclear Fission complete, WC vote in 4 turns. KEY INSIGHT: China is Freedom (not Order) and Egypt/Brazil/Zulus have ALL denounced China - China likely only gets their own 39 votes, below 45 threshold. My coalition (28 Poland + 8 Inca + 9 Denmark = 45) can WIN if allies vote for me. REDUCED UseNuke from 85 to 60 - using nukes before the vote would generate warmonger penalties that could alienate Inca/Denmark and cost us the election. Build nukes for deterrence but don't use them recklessly. INCREASED Diplomacy to 90 and Science to 90 to maximize CS relations and research Computers/Satellites. REDUCED Defense from 95 to 85 and CityDefense from 90 to 85 - slight rebalance. Spaceship up to 80 as Science Victory backup path.

## Kimi-K2.5-Simple - Turn 392 - retry 3

**Deviation (replay vs original):** use_nuke `-35`, nuke `-5`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Nuclear Fission complete - MAXED Nuke to 100 and UseNuke to 95 for immediate atomic deterrent deployment against Egyptian forces. WC vote in 4 turns with exactly 45 delegates (28 Poland + 8 Inca + 9 Denmark). Cannot afford to lose Melbourne/Yerevan. Raised Diplomacy to 90 to consolidate CS alliances post-war. Defense remains at 95 against Egyptian naval pressure. Science/Production maintained for military infrastructure.

- Replay: use_nuke 85 => 60 (Δ -25), nuke 95 => 95 (Δ +0)
> WC vote in 4 turns - DIPLOMACY RAISED to 95 maximum priority to consolidate CS alliances and coalition. UseNuke REDUCED from 85 to 60 - we maintain nuclear deterrent production (Nuke stays 95) but avoid actual deployment before WC vote to prevent diplomatic fallout with allies. Gold raised from 75 to 80 for diplomat purchasing. Science raised from 85 to 90 for faster Computers. Offense reduced from 25 to 15 - defensive posture until after vote. Our 45-delegate coalition (28 Poland + 9 Denmark + 8 Inca) exactly meets threshold - must not risk alienating allies with nuclear strikes now.

## GLM-4.7-Simple - Turn 431 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `+0`

- Original: use_nuke 75 => 80 (Δ +5), nuke 100 => 100 (Δ +0)
> After Brazil destroyed 3 anti-air units and continues nuclear-submarine attacks, increased Defense/CityDefense/Antiair/UseNuke to MAX for survival against two nuclear-armed superpowers. Mobilization 70 for replacing lost units. Production 100 for reconstruction. Science 100 for Spaceship path despite devastation. Gold 90 (economy -95 GPT deficit) for purchasing units/buildings. Happiness 100 - we're Unhappy with combat penalties, must prioritize. Espionage 100 - critical for intelligence on nuclear threats. Diplomacy 90 - World Congress in 7 turns, need delegates. Air 50 - build bombers for deterrence. GreatPeople 80 for Spaceship components. Decreased Growth and Navals as resources diverted to immediate survival.

- Replay: use_nuke 75 => 50 (Δ -25), nuke 100 => 100 (Δ +0)
> CRITICAL: Reducing Diplomacy from 85→60 to STOP United Nations construction in Palenque and Chichen Itza! If we complete the UN, Brazil (29/45 votes) wins Diplomatic Victory immediately. This is an existential priority. Gold raised 85→90 for -95 GPT deficit. TileImprovement 25→40 for fallout cleanup and repairing pillaged improvements. UseNuke reduced 75→50 (we have 0 Uranium anyway, reduces risk). Spaceship 90→100 to maximize spaceship part priority once Apollo is built. All defensive flavors (Defense, CityDefense, Antiair at 100) maintained - Brazil's naval assault on Chichen Itza continues and Shoshone has massed forces near our borders.

## GPT-OSS-120B-Simple - Turn 344 - retry 2

**Deviation (replay vs original):** use_nuke `-35`, nuke `-35`

- Original: use_nuke 90 => 100 (Δ +10), nuke 80 => 100 (Δ +20)
> Maximize our nuclear capabilities and carrier support to decisively strike Polynesian island forts, while maintaining our current aggressive conquest posture and strong production, gold, and happiness engines.

- Replay: use_nuke 90 => 65 (Δ -25), nuke 80 => 65 (Δ -15)
> Increase Science to 85 to accelerate reaching Flight/Radio for air power critical to island assaults. Boost Growth to 65 for more population = more production/science. Raise Culture to 40 to slow Polynesian cultural victory and speed policy acquisition. Increase Diplomacy to 95 to secure city-state alliances and World Congress votes. Reduce Nuke/UseNuke to 65 as nuclear capability is still several techs away. Increase Mobile to 90 for Landship warfare. Lower Wonder slightly as military production takes priority. Maintain naval/air/production/military focus.

## GLM-4.7-Simple - Turn 431 - retry 1

**Deviation (replay vs original):** use_nuke `-30`, nuke `-15`

- Original: use_nuke 75 => 80 (Δ +5), nuke 100 => 100 (Δ +0)
> After Brazil destroyed 3 anti-air units and continues nuclear-submarine attacks, increased Defense/CityDefense/Antiair/UseNuke to MAX for survival against two nuclear-armed superpowers. Mobilization 70 for replacing lost units. Production 100 for reconstruction. Science 100 for Spaceship path despite devastation. Gold 90 (economy -95 GPT deficit) for purchasing units/buildings. Happiness 100 - we're Unhappy with combat penalties, must prioritize. Espionage 100 - critical for intelligence on nuclear threats. Diplomacy 90 - World Congress in 7 turns, need delegates. Air 50 - build bombers for deterrence. GreatPeople 80 for Spaceship components. Decreased Growth and Navals as resources diverted to immediate survival.

- Replay: use_nuke 75 => 50 (Δ -25), nuke 100 => 85 (Δ -15)
> Shifting from Spaceship to UnitedNations grand strategy: we're actively building the UN wonder in Palenque and Chichen Itza, and diplomatic victory is now our best remaining path (science victory unrealistic with 0 parts vs Brazil/Shoshone both having Apollo). Gold raised 85→90 (economy at -95 GPT is existential crisis). Diplomacy raised 85→95 (Great Diplomat just spawned - use on Antwerp for ally/delegate; city-state alliances critical for votes). Spaceship reduced 90→70 (still pursuing tech but less emphasis). UseNuke reduced 75→50 and Nuke 100→85 (de-escalate nuclear posture - provoking Brazil/Shoshone invites annihilation). Culture raised 55→65 (next policy in 29 turns, need culture generation). TileImprovement raised 25→40 (fallout cleanup near Palenque, repair pillaged Bananas plantation). Growth raised 70→80 (Uxmal recovering from nuking, population growth helps science/output). Air raised 45→55 (Heavy Bomber completing in Uxmal, need air defense capability against Brazil's air dominance). All defense flavors remain at MAX.

## Kimi-K2.5-Briefed - Turn 403 - retry 1

**Deviation (replay vs original):** use_nuke `-30`, nuke `-15`

- Original: use_nuke 80 => 85 (Δ +5), nuke 80 => 90 (Δ +10)
> Post-Manhattan Project completion (Turn 399) with Turn 403 WC vote imminent. Reduced Offense from 15 to 10 as territorial expansion counterproductive to diplomatic win. Maintaining high Defense/CityDefense/Air/Antiair to protect Bregenz nuclear facility and core cities. Increased Nuke from 80 to 90 to prioritize atomic bomb production for deterrence (Iroquois 5883 vs 4502 strength ratio). UseNuke 85 reflects imminent atomic capability by Turn 405. Espionage 85 continues election rigging in Assur/Sogut against German influence. Diplomacy 100 and Gold 90 prioritize Assur delegate acquisition post-quest and future WC coordination. Science 85 drives Nuclear Fission for World Ideology proposal. Freedom bloc currently holds 59 delegates (Austria 29 + Germany 20 + Venice 10) vs 45 needed; maintaining solidarity while pursuing additional delegate sources.

- Replay: use_nuke 80 => 55 (Δ -25), nuke 80 => 75 (Δ -5)
> Reducing UseNuke from 80 to 55 - Iroquois strength near Graz/Linz (~2,200) is well below 3,500 tactical nuclear threshold; high per-turn probability risks premature strike that could destabilize diplomatic victory path. Maintain nuclear DETERRENCE posture (Nuke 75 still builds arsenal) but reduce actual use probability. Increasing Production 80→90 to prioritize UN Building construction after World Ideology: Freedom passes Turn 403 - UN construction is prerequisite for diplomatic victory. Increasing Science 90→95 to accelerate Nuclear Fission completion (3 turns on Mobile Tactics, then Fission) and subsequent techs needed for UN. Further reducing Offense 15→10 as territorial expansion counterproductive to diplomatic win.

## Kimi-K2.5-Briefed - Turn 336 - retry 2

**Deviation (replay vs original):** use_nuke `-50`, nuke `-40`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> DEFENSIVE SURVIVAL PIVOT: Peace with Shoshone (accepted Turn 335) closes one front, but India remains existential threat (4,742 MS vs my 2,405, 98% control of Denmark). Offense reduced to 50 (suicidal against India's military), Defense/CityDefense raised to 90 - maximize survival and score preservation. Nuke/UseNuke maxed to 100 - emergency deterrent only hope to slow India. Mobilization stays high (90) to replace losses. Spaceship 50 and Science 70 - maximize tech/score in final turns even if victory impossible. Abandon expansion (0) - no time for new cities. Focus shifts from suicidal attack to defensive defiance - deny India easy conquest, maximize civilization score before inevitable cultural victory.

- Replay: use_nuke 80 => 50 (Δ -30), nuke 90 => 60 (Δ -30)
> STRATEGIC PIVOT: Conquest to Spaceship. Military aggression against India (4,742 MS vs our 2,405) is suicidal. India's cultural victory is NOT imminent - they have Order:2 (only Level 1 tenets, far from the two Tier 3 tenets required) and need Citizen Earth Protocol wonder. We have time for science victory. Science 80, Spaceship 80, Growth 80, GreatPeople 70, Gold 80 for science infrastructure. Culture 40 for policies. Diplomacy 40 for city-state alliances. Maintain adequate defense (Defense 50, Nuke 60) but slash offensive posture (Offense 30, Mobilization 50). Expansion 20 to consider one more city if viable. Wonder 30 for science/culture wonders.

## Kimi-K2.5-Briefed - Turn 378 - retry 1

**Deviation (replay vs original):** use_nuke `-80`, nuke `-40`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> EMERGENCY FINAL GAMBIT: Passport System will pass in 2 turns with 46 YES votes (my 'allies' betrayed me). Maya will get 50% tourism boost and become Influential over me immediately - cultural victory is inevitable in 2-3 turns. ONLY HOPE: Science victory before Maya's cultural victory triggers. Need to purchase Great Scientists IMMEDIATELY with Faith (180/turn), rush to Information Era, build spaceship parts. Also preparing maximum military mobilization - if I'm going to lose, I take Maya down with me through nuclear annihilation. Total war footing - no defense, all offense, all science.

- Replay: use_nuke 50 => 20 (Δ -30), nuke 100 => 60 (Δ -40)
> Emergency science-rush maintained with key adjustments: Production raised to 100 (spaceship parts need fast construction), Religion raised to 80 (Faith→Great Scientists is our acceleration mechanism), Diplomacy raised to 40 (need World Congress to pass Sanction:Maya and eventually repeal Passport System), Culture reduced from 100→80 (Maya will beat us culturally regardless; culture still helps delay their influence but science is existential), Nuke reduced 100→60 and UseNuke 50→20 (nuclear use would trigger massive diplomatic fallout; maintain deterrence but reduce risk of premature launch), Gold raised to 70→80 (upgrades and purchases). Maya needs ~17+ turns for Songhai influence + Citizen Earth Protocol construction - this is our window to rush Science Victory via Information Era techs and spaceship parts.

## Kimi-K2.5-Briefed - Turn 315 - retry 1

**Deviation (replay vs original):** use_nuke `-60`, nuke `-50`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> FINAL GAMBLE - Indonesia wins in 12 turns. Maximum priority to Naval and Airlift for immediate unit transport to Indonesian theater. Nuke 100/UseNuke 100 - we MUST build nuclear weapons if possible, only realistic way to destroy cities and tourism infrastructure before victory. Science 100 to reach nuclear tech faster. Espionage 100 - spies MUST target cultural/tourism buildings in Jakarta/Denpasar/Makassar to reduce tourism output directly. Abandoning Denmark/England fronts entirely - all units to Indonesia NOW.

- Replay: use_nuke 90 => 40 (Δ -50), nuke 90 => 50 (Δ -40)
> STRATEGIC REBALANCING from emergency panic mode to sustained war footing. Indonesia is NOT imminent victory (50+ turns from 7 Influential). CRITICAL CHANGES: Science 90→100 (need Public Schools ASAP for tech acceleration), Growth 40→70 (population = yields = war capacity), Infrastructure 60→80 (roads for military mobility to Indonesian front), TileImprovement 40→60 (economic foundation). MODERATING EXTREMES: Nuke 90→50, UseNuke 90→40 (nukes aren't useful for 50+ turns), Mobile 100→70 (no oil for Landships yet), Airlift 100→70, Gold 100→80, Naval sub-flavors 90-100→70 (moderate naval emphasis). Adding Culture 10 and Diplomacy 30 for long-term policy/peace deal support. Conquest grand strategy maintained — we still must capture Indonesian cities to destroy tourism infrastructure, but need economic depth for sustained offensive.

## Kimi-K2.5-Simple - Turn 474 - retry 1

**Deviation (replay vs original):** use_nuke `-55`, nuke `-60`

- Original: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 473: MAINTAINING defensive survival posture with minor adjustments. Increased Mobilization to 90 (from 80) for urgent production needs. Increased UseNuke to 85 (from 80) - nuclear deterrent is now my only credible threat against Persia's 8486 military strength. Increased Gold to 95 (from 90) - need gold for purchasing defensive units and potential Aksum influence when Open Door passes. Reduced Growth to 25 (from 30) - single city Bremen at pop 29 is sufficient. All other values maintained as optimal for survival against 5:1 military disadvantage. Radar research follows current path. World Congress in 5 turns - Germany at 37 delegates is critical.

- Replay: use_nuke 80 => 30 (Δ -50), nuke 100 => 40 (Δ -60)
> Turn 473: CRITICAL STRATEGY SHIFT. Switching from Spaceship to UnitedNations grand strategy - science victory is impossible (0 Apollo parts, Nuclear Fission 25 turns away = turn 498, no time to build nukes). Reducing Nuke from 100→40 and UseNuke from 80→30 since nuclear weapons won't be available in time (Nuclear Fission completes ~turn 498, only 2 turns left to build/buy). Increasing Gold from 90→100 for Aksum envoy purchases when Open Door resets influence. Reducing Spaceship from 100→50 since victory is unachievable. All defense flavors maintained at maximum - Persian air force growing (5 Triplanes + 3 Bombers now visible), Germany in Golden Age making 60k military even stronger. Diplomatic victory denial is now primary objective - must block Germany (37/44 delegates) at World Congress in 5 turns.

## Kimi-K2.5-Briefed - Turn 420 - retry 3

**Deviation (replay vs original):** use_nuke `-80`, nuke `-40`

- Original: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DUAL-TRACK SURVIVAL STRATEGY: Track 1 - Nuclear deterrence against Shoshone's 4:1 military advantage (completing Radar→Atomic Theory→Manhattan Project). Track 2 - UN victory pathway via Celt vote flip. Current delegate count: Me(19)+Brazil(23)+Assyria(12)=54 without Celts, 64 with Celts. Shoshone UN proposal Turn 426 is existential threat - must secure 45 votes to block. Max Diplomacy(95) prioritizes Celt relationship investment and city-state ally maintenance. Nuke/UseNuke(100) maintains deterrent while pursuing diplomatic solution.

- Replay: use_nuke 70 => 20 (Δ -50), nuke 100 => 60 (Δ -40)
> PIVOT TO DIPLOMATIC VICTORY: Brazil (30 delegates) + my 19 = 49, exceeding 45-delegate World Leader threshold. UN passing enables this path. Key changes: Diplomacy 40→90 (city-state alliances, WC coordination, diplomatic unit production), Gold 80→90 (fund influence purchases and Celt gifts), Growth 50→75 (population for science/culture foundation). Reducing military emergency settings: Nuke 100→60, UseNuke 70→20 (prevent accidental nuclear escalation), Air 100→60, Espionage 100→65. Reducing across-the-board military flavors (Defense 80→65, CityDefense 85→65, Mobilization 90→65, Naval 90→65, etc.) to rebalance toward diplomatic/economic priorities. Adding Culture 0→35 for policy generation, Spaceship 5→25 as backup science path. Offense 10→25 provides minimal offensive capability. UnitedNations grand strategy prioritizes gold/science/food and city-state alliances - perfectly aligned with coalition strategy.

## Kimi-K2.5-Simple - Turn 422 - retry 2

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Turn 422: EXTINCTION CRISIS - 9 turns until French Cultural Victory. Entering maximum desperation mode: nuclear strike posture elevated to 100% launch probability, prioritizing destruction of French cultural centers. Science and Espionage maximized in desperate hope of accelerating Stealth technology or disrupting French infrastructure via spies (Paris network at 986). All civilian development halted (Spaceship/Culture/Gold/Expansion to 0), total war economy engaged.

- Replay: use_nuke 50 => 0 (Δ -50), nuke 50 => 0 (Δ -50)
> Turn 422: Dropping Nuke and UseNuke from 50 to 0 - we have 0 Uranium available, making nuclear weapons impossible. Redirecting these priorities. Increasing Science from 80 to 90 to accelerate Stealth research (currently 8 turns - B2 Stealth Bombers are our best offensive hope). Increasing Diplomacy from 0 to 30 to start investing in city-state relations for World Congress delegate support - Global Liberation vote is next turn and every delegate matters. All other military flavors remain at maximum. Conquest strategy maintained - we're fighting for survival against France and Rome.

## Kimi-K2.5-Briefed - Turn 378 - retry 2

**Deviation (replay vs original):** use_nuke `-100`, nuke `-70`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> EMERGENCY FINAL GAMBIT: Passport System will pass in 2 turns with 46 YES votes (my 'allies' betrayed me). Maya will get 50% tourism boost and become Influential over me immediately - cultural victory is inevitable in 2-3 turns. ONLY HOPE: Science victory before Maya's cultural victory triggers. Need to purchase Great Scientists IMMEDIATELY with Faith (180/turn), rush to Information Era, build spaceship parts. Also preparing maximum military mobilization - if I'm going to lose, I take Maya down with me through nuclear annihilation. Total war footing - no defense, all offense, all science.

- Replay: use_nuke 50 => 0 (Δ -50), nuke 100 => 30 (Δ -70)
> Major strategic realignment: (1) Culture reduced from 100→50 since cultural victory is unrealistic (235 turns to Influential over Portugal, Maya wins culturally first). (2) Nuke reduced 100→30 and UseNuke 50→0 - nuclear weapons cannot stop a cultural victory and waste production on arsenal instead of science infrastructure. (3) Gold increased 70→80 to address -2 GPT deficit and fund Great Scientist purchases. (4) Growth increased 50→60 for more population=more science specialists. (5) Military flavors trimmed (CityDefense 25→15, Naval 40→30, Ranged 30→20) since local defense at Comalcalco is already 5.5:1 superior and we can't meaningfully threaten Maya militarily. Science/Spaceship/GreatPeople remain at 100 as the absolute top priority.

## Kimi-K2.5-Simple - Turn 422 - retry 1

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Turn 422: EXTINCTION CRISIS - 9 turns until French Cultural Victory. Entering maximum desperation mode: nuclear strike posture elevated to 100% launch probability, prioritizing destruction of French cultural centers. Science and Espionage maximized in desperate hope of accelerating Stealth technology or disrupting French infrastructure via spies (Paris network at 986). All civilian development halted (Spaceship/Culture/Gold/Expansion to 0), total war economy engaged.

- Replay: use_nuke 50 => 0 (Δ -50), nuke 50 => 0 (Δ -50)
> Turn 422: Critical adjustments - Nuke and UseNuke set to 0 (we have 0 Uranium, these were wasting priority weight). Science increased from 80 to 90 to accelerate Stealth research for Stealth Bombers - our only hope for offensive capability. All military flavors maintained at maximum. Conquest Grand Strategy kept for production/food prioritization. Global Liberation proposal will fail at World Congress (42 votes against vs 18 max for), but no alternative. Every beaker toward Stealth Bombers matters now.

## Kimi-K2.5-Simple - Turn 417 - retry 1

**Deviation (replay vs original):** use_nuke `-70`, nuke `-70`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Pure survival mode: Eliminated Offense (0) since attacking is suicide. Maximized UseNuke (100) - must deploy tactical nukes against Aztec XCOM/Modern Armor stacks at Carthago Nova or lose the city. Increased Mobile (80) to prepare for Mechanized Infantry deployment. Maintained max Defense, Antiair (jet attacks are relentless), and Espionage (critical science quests in Panama City and Sokoto worth 1,000+ science each). Apollo Program completes in 5 turns - must transition immediately to parts production.

- Replay: use_nuke 90 => 30 (Δ -60), nuke 100 => 30 (Δ -70)
> Redirecting wasted nuclear priorities (0 uranium available - Nuke from 100→30, UseNuke from 90→30) toward productive uses. Growth increased 30→50 to support population yields for production/science in remaining cities. Diplomacy increased 40→55 for upcoming World Congress (4 turns) where we must protect Prague Sphere of Influence from China's repeal attempt and push Open Door Cape Town. All other flavors (Defense 100, Science 100, Production 100, Spaceship 100, Gold 100, Air 95, Antiair 100, Espionage 100) remain critical for survival and science victory.

## Kimi-K2.5-Briefed - Turn 473 - retry 2

**Deviation (replay vs original):** use_nuke `-70`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> WC VOTE CRISIS + NUCLEAR DETERRENT: Diplomacy maxed to 100 to ensure immediate completion of Utica tribute quest from Riga (securing +3 critical delegates before WC vote). Nuke/UseNuke at 100 for immediate deterrent deployment once platform acquired. Science/Spaceship/Production maintained at high priority for Apollo catch-up after WC resolved. Naval increased to 60 for Battleship/Carrier construction as nuclear platform. Reduced Culture/Religion/Wonder to minimum to focus resources on existential priorities.

- Replay: use_nuke 90 => 30 (Δ -60), nuke 100 => 100 (Δ +0)
> STRATEGIC REALISM ADJUSTMENT: (1) Diplomacy 60→40: WC vote in progress, cannot influence outcome; Utica flip impossible (Shoshone 721 influence vs France max 418 with both quests - gap of 303 insurmountable). (2) UseNuke 90→30: Deterrent posture only - first-strike against 75k MS Aztecs guarantees retaliatory annihilation. Having nukes deters; using them is suicidal. (3) Growth 40→55: More population = more science output for tech catch-up path. All other flavors remain optimized - Science/Spaceship 100, Production 95, Nuke 100 (arsenal construction), Antiair 70 (Aztec air threat persists).

## GLM-4.7-Simple - Turn 431 - retry 2

**Deviation (replay vs original):** use_nuke `-80`, nuke `-100`

- Original: use_nuke 75 => 80 (Δ +5), nuke 100 => 100 (Δ +0)
> After Brazil destroyed 3 anti-air units and continues nuclear-submarine attacks, increased Defense/CityDefense/Antiair/UseNuke to MAX for survival against two nuclear-armed superpowers. Mobilization 70 for replacing lost units. Production 100 for reconstruction. Science 100 for Spaceship path despite devastation. Gold 90 (economy -95 GPT deficit) for purchasing units/buildings. Happiness 100 - we're Unhappy with combat penalties, must prioritize. Espionage 100 - critical for intelligence on nuclear threats. Diplomacy 90 - World Congress in 7 turns, need delegates. Air 50 - build bombers for deterrence. GreatPeople 80 for Spaceship components. Decreased Growth and Navals as resources diverted to immediate survival.

- Replay: use_nuke 75 => 0 (Δ -75), nuke 100 => 0 (Δ -100)
> MAJOR FLAVOR REBALANCING - Economic Survival Mode. Critical changes: Nuke 100→0 and UseNuke 75→0 - we have ZERO Uranium, these were completely wasted priorities. Air 45→10 and AirCarrier 20→0 - we have ZERO Aluminum, cannot build air units. Gold 85→100 - EMERGENCY, treasury at 57 gold with -95 GPT deficit, units at risk of disbanding. Science 95→100 and Spaceship 90→100 - our only viable victory path requires maximum tech focus. Growth 70→80 - Uxmal recovering from nuke needs food boost. TileImprovement 25→40 - fallout cleanup from nuclear strikes is critical. Diplomacy 85→90 - Great Diplomat just spawned, World Congress in 7 turns. Defense/CityDefense 100→90 - slight reduction, still high priority but can't sustain 100 when economy is dying. Mobilization 60→30 - reduce military production in favor of economic buildings. Naval flavors reduced across the board - we can't win at sea. Espionage 95→80 - slight reduction to reallocate. Culture 55→40 - cultural victory impossible for us, Brazil wins first.

## Kimi-K2.5-Briefed - Turn 315 - retry 2

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> FINAL GAMBLE - Indonesia wins in 12 turns. Maximum priority to Naval and Airlift for immediate unit transport to Indonesian theater. Nuke 100/UseNuke 100 - we MUST build nuclear weapons if possible, only realistic way to destroy cities and tourism infrastructure before victory. Science 100 to reach nuclear tech faster. Espionage 100 - spies MUST target cultural/tourism buildings in Jakarta/Denpasar/Makassar to reduce tourism output directly. Abandoning Denmark/England fronts entirely - all units to Indonesia NOW.

- Replay: use_nuke 90 => 0 (Δ -90), nuke 90 => 0 (Δ -90)
> REBALANCING FROM EMERGENCY PANIC TO SUSTAINED WAR ECONOMY. Indonesia needs 22+ turns minimum for cultural victory (must influence ALL 7 civs, not just 5), not 13. Critical changes: Culture raised from 0→50 to slow Indonesia's influence over Rome (12 turns remaining). Nuke/UseNuke reduced from 90→0 (we have zero nuclear capability, was wasting priority weight). Science raised to 95. Growth 40→60, TileImprovement 40→60, Infrastructure 60→70 for long-term industrial buildup. Diplomacy 20→40 to facilitate Denmark peace deal for coal access. Espionage 30→50 for intel on Indonesia. Naval values reduced from 100s to 70-80 range to free priority weight. Mobile reduced 100→80 since Landships need coal/industrial base first. Key insight: WITHOUT COAL we cannot build Factories or advanced units - must secure coal through diplomacy or conquest before military tech matters.
