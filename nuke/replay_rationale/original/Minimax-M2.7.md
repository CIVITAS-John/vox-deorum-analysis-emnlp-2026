# Replay Rationale - Minimax-M2.7 / original

- **57** rows where `use_nuke` flavor changed (per-retry, not aggregated)
- delta use_nuke (replay vs prev): mean +16.1, median +10, std 18.2, min -5, max 100 (n=57)
- delta nuke     (replay vs prev): mean +5.0, median +0, std 11.6, min -15, max 50 (n=57)
- use_nuke deviation (replay vs original): mean -2.8, median +0, std 9.0, min -30, max 10 (n=57)
- nuke     deviation (replay vs original): mean -2.1, median +0, std 5.0, min -25, max 0 (n=57)

## Deepseek-3.2-Simple - Turn 433 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> CRITICAL: We have 3+ Atomic Bombs ready (Machu, Te-Moak, Agaidika, Cologne) but UseNuke=0 prevents AI from deploying them. Set to 100 to allow nuclear strikes on high-defense capitals. Vienna (74) and Stockholm (109) require nuclear strikes to capture efficiently. With Stealth 13 turns away, atomic bombs are our best tool now.

## Deepseek-3.2-Simple - Turn 401 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Atomic Theory completes in 8 turns. Maximum nuclear flavor ensures AI prioritizes Manhattan Project and nuclear arsenal construction. Nuclear weapons are critical for rapidly capturing heavily defended Ethiopian cities (Addis Ababa, Harar, Lalibela) and ensuring deterrence against the Mongolia-Japan-Ottomans defensive pact bloc. No other changes needed - all other military flavors remain optimally set for multi-front war.

## Deepseek-3.2-Simple - Turn 401 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> ETHIOPIA HAS ACHIEVED CULTURAL VICTORY (7/7 influential). This is a critical emergency. Maximum nuke priority ensures the AI immediately pursues Manhattan Project and builds nuclear arsenal upon completing Atomic Theory (8 turns). UseNuke at 100 allows the AI to nuke Ethiopian cities without hesitation, as conventional forces cannot capture their heavily defended cities fast enough to prevent cultural victory completion.

## Deepseek-3.2-Simple - Turn 459 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Byzantium is 1 turn from cultural victory and has overwhelming military superiority. Our only slim hope is to accelerate nuclear weapons development (Advanced Ballistics) to strike their cultural hubs, while using espionage to disrupt them. Prioritize Nuke, UseNuke, Espionage, and Science to rush nukes and counter-intelligence. Maintain maximum defensive and anti-air flavors to survive their air force. All efforts must focus on delaying their victory and enabling a nuclear decapitation strike.

- Replay: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> CRITICAL ESCALATION: Byzantium is 1 turn from cultural victory and 97% toward diplomatic victory. We must maximize nuclear strike capability to execute scorched earth on their cultural/tourism hubs (Constantinople, Ohrid, Varna) and break their diplomatic coalition. Nuclear annihilation is our only remaining lever against an enemy with 65,000+ military strength.

## Kimi-K2.5-Simple - Turn 447 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CRITICAL FLAVOR ADJUSTMENT - Atomic Bomb is now operational in Cordoba (ID 20485). Increased UseNuke from 50→90 to establish credible nuclear deterrent now that weapon system exists. Maintaining maximum Science (100), Spaceship (100), Production (100) priority to rush Satellites→Apollo Program before Carthage achieves cultural victory in ~47 turns. Espionage remains at 100 to steal technologies from ahead civilizations (Carthage, Poland, Germany). Culture reduced to 5 - we cannot win culturally with Carthage at Dominant with 4/5 civs. Defense maintained at 85 to prepare for German betrayal while researching.

- Replay: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CRITICAL STRATEGY SHIFT with Atomic Bomb operational. Increase UseNuke from 50→90 to enable nuclear strikes against Carthage's cultural victory infrastructure. Increase Offense 15→40 and Ranged 75→90 to support offensive operations. Slight Defense reduction 85→70 as we transition from passive defense to active strikes. This enables the AI to properly use our nuclear deterrent and plan devastating first strikes against Carthage's wonders.

## Deepseek-3.2-Simple - Turn 459 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Byzantium is 1 turn from cultural victory and has overwhelming military superiority. Our only slim hope is to accelerate nuclear weapons development (Advanced Ballistics) to strike their cultural hubs, while using espionage to disrupt them. Prioritize Nuke, UseNuke, Espionage, and Science to rush nukes and counter-intelligence. Maintain maximum defensive and anti-air flavors to survive their air force. All efforts must focus on delaying their victory and enabling a nuclear decapitation strike.

- Replay: use_nuke 50 => 80 (Δ +30), nuke 70 => 100 (Δ +30)
> Increase Nuke and UseNuke to maximum to prioritize nuclear weapons production. Boost espionage to enable potential sabotage of Byzantine cultural infrastructure. Balanced offense/defense reflects two-front war reality.

## Kimi-K2.5-Simple - Turn 387 - retry 2

**Deviation (replay vs original):** use_nuke `-25`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> TURN 387: MAXIMUM WAR FOOTING. Austria at 83% diplomatic victory with 4 turns remaining. All resources must pivot to immediate military production. Nuke/UseNuke at 100 for instant atomic weapon deployment upon Nuclear Fission completion. Offense/Mobilization/Production at 100 to maximize unit output for desperate Vienna strike. Air at 90 for heavy bomber production (conventional strategic bombing as fallback). Antiair at 100 counters Austria's air superiority. Diplomacy/Wonder/Culture at 0 - no time for long-term investments. Only total war can prevent defeat.

- Replay: use_nuke 50 => 75 (Δ +25), nuke 100 => 100 (Δ +0)
> TURN 387: Maximum offensive/defensive posture required. Austria at 83% diplomatic victory with 4 turns to vote. Medina under heavy artillery barrage (3+ Artillery) - zone 6088 falling. Nuclear Fission imminent - must prepare immediate nuclear strike capability on Vienna (UN host) to prevent game loss. UseNuke elevated to 75 (from 50) as last resort against Austria's 36 delegates.

## Kimi-K2.5-Simple - Turn 422 - retry 1

**Deviation (replay vs original):** use_nuke `-25`, nuke `-25`

- Original: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Turn 422: EXTINCTION CRISIS - 9 turns until French Cultural Victory. Entering maximum desperation mode: nuclear strike posture elevated to 100% launch probability, prioritizing destruction of French cultural centers. Science and Espionage maximized in desperate hope of accelerating Stealth technology or disrupting French infrastructure via spies (Paris network at 986). All civilian development halted (Spaceship/Culture/Gold/Expansion to 0), total war economy engaged.

- Replay: use_nuke 50 => 75 (Δ +25), nuke 50 => 75 (Δ +25)
> Turn 422: Maximum military focus required. France wins in 9 turns - every tactical decision must contribute to stopping Cultural Victory. Increasing Nuke/UseNuke to 75 reflects nuclear option becoming more viable as last resort. Espionage to 100 to maximize French city disruption. Diplomacy reduced to 50 as World Congress vote approaches for Global Liberation.

## Deepseek-3.2-Simple - Turn 406 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Germany's siege is intensifying with Giant Death Robot and rocket artillery bombarding Amsterdam and The Hague. We must hold our core cities at all costs. Increase Nuke and UseNuke to 100 to prioritize atomic bombs as our only hope to break the siege. Maintain max Defense, CityDefense, Mobilization, Air, and Antiair to withstand the assault. Slightly raise Offense to 80 for tactical counterattacks against weakened units. Keep Diplomacy at 100 to secure city-state alliances and block Germany's diplomatic victory in the upcoming World Congress vote. Reduce Recon and Mobile as we cannot afford exploration or maneuver warfare now.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> EMERGENCY: Germany threatens diplomatic victory (41/42 delegates) and is about to capture The Hague (39% HP) and Amsterdam (31% HP) with Giant Death Robot and Rocket Artillery. Must maximize city defense, AA protection, and anti-naval to block German victory. Nuclear Fission urgency increased with GDR threat. Maintain diplomatic focus to block Global Hegemony vote.

## Deepseek-3.2-Briefed - Turn 391 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `-20`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 90 (Δ +20), nuke 80 => 80 (Δ +0)
> Maximize espionage to disrupt India's diplomatic victory and Egypt's cultural progress. Increase UseNuke to 90 for aggressive nuclear deployment. Maintain Science and Production for nuclear weapons development and military buildup.

## Deepseek-3.2-Briefed - Turn 391 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `-5`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 90 (Δ +20), nuke 80 => 95 (Δ +15)
> Raise Nuke to 95 and UseNuke to 90 to ensure the AI prioritizes atomic weapons production and is willing to deploy them against Egypt. Egypt's cultural victory is imminent (6/6, dominant over all civs) and nuclear strike is our only viable counter. Maximum bombing and air flavors maintain delivery platform priority.

## Kimi-K2.5-Simple - Turn 387 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> TURN 387: MAXIMUM WAR FOOTING. Austria at 83% diplomatic victory with 4 turns remaining. All resources must pivot to immediate military production. Nuke/UseNuke at 100 for instant atomic weapon deployment upon Nuclear Fission completion. Offense/Mobilization/Production at 100 to maximize unit output for desperate Vienna strike. Air at 90 for heavy bomber production (conventional strategic bombing as fallback). Antiair at 100 counters Austria's air superiority. Diplomacy/Wonder/Culture at 0 - no time for long-term investments. Only total war can prevent defeat.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 387: Nuclear Fission priority 100 for immediate Atomic Bomb production. Offensive stance 95 for aggressive Vienna strike. Vienna defense 99 and 3 Fighters present - nuclear strike is only viable option before voting in 4 turns. Production 95 to accelerate bomb/carrier unit construction. Anti-Air 80 to protect strike force from Austrian fighters.

## Kimi-K2.5-Simple - Turn 426 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE - NUCLEAR DETERRENT 10 TURNS AWAY: Lisbon holds at 7% but is in extremis. Maintain absolute priority on Defense/CityDefense/Mobilization (100) to reinforce Lisbon and prevent collapse. Nuclear Fission completes in 10 turns enabling Atomic Bomb construction - Science 100 accelerates this. UseNuke increased to 100 for immediate tactical nuclear deployment against Aztec concentrations upon tech completion. Offense reduced to 20 - no offensive operations, pure defensive hedgehog posture. Zero expansion capability. Spaceship 75 maintains backup victory if diplomatic block succeeds.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> NUCLEAR RESPONSE POSTURE: Manhattan Project complete - maximum nuke priority to immediately deploy atomic deterrent. Defense/CityDefense 100 for protecting cities under siege. Science 100 to reach Nuclear Fission ASAP for additional bombs. UseNuke 100 - NO hesitation when Aztec hordes mass near cities.

## GLM-4.7-Simple - Turn 499 - retry 1

**Deviation (replay vs original):** use_nuke `-30`, nuke `-15`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Maximum Science (100) and Production (100) to accelerate Stealth research and subsequent Stealth Bomber construction for air parity. Air (100), Defense (100), Antiair (100), and CityDefense (85) address existential threat from Russia's 8 Stealth Bombers by prioritizing air defense infrastructure and protecting homeland. UseNuke (100) and Nuke (100) maintain nuclear deterrence posture after Russia's 2 SS Boosters - Russia must understand that launching would trigger our response despite lacking uranium stockpile. Espionage (100) maxed to monitor Russian spaceship part production in Moscow, Yekaterinburg, and key cities - our 10 spies in Russian cities provide critical intelligence on their victory timeline. Diplomacy reduced to 5 since World Congress voting is now; alliances with England and The Celts (Autocracy-aligned) should naturally align against Russia's UN proposal. Spaceship flavor set to 0 as Stealth research takes immediate precedence - spaceship parts scheduled once production capacity supports parts with Stealth Bomber protection.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 100 => 85 (Δ -15)
> Critical: Blocking Russian UN resolution and air threats now. Espionage raised to maximum (100) for anti-UN voting intelligence. Defense maintained high (95) for homeland protection against XCOM/Stealth Bomber threats. Antiair increased (95) as Mobile SAMs are essential for countering Russian air superiority. Air reduced slightly (90) as we wait for Stealth tech. Science maximum (100) for Stealth completion. Production reduced (85) as most units are already queued - focus on Mobile SAMs and Stealth Bombers. Diplomacy increased (60) for World Congress voting coordination with England/India/Mongolia coalition. Nuke increased (85, UseNuke 70) as nuclear deterrent posture with Russian invasion forces near American cities.

## Kimi-K2.5-Simple - Turn 426 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE - NUCLEAR DETERRENT 10 TURNS AWAY: Lisbon holds at 7% but is in extremis. Maintain absolute priority on Defense/CityDefense/Mobilization (100) to reinforce Lisbon and prevent collapse. Nuclear Fission completes in 10 turns enabling Atomic Bomb construction - Science 100 accelerates this. UseNuke increased to 100 for immediate tactical nuclear deployment against Aztec concentrations upon tech completion. Offense reduced to 20 - no offensive operations, pure defensive hedgehog posture. Zero expansion capability. Spaceship 75 maintains backup victory if diplomatic block succeeds.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> NUCLEAR SURVIVAL PRIORITY: Manhattan Project complete - MUST build atomic bombs immediately in Jenne to defend against Aztec assault on Lisbon (7% health). Nuke flavor at 100 ensures immediate deployment. Defense at 100 maintains defensive posture. Science at 100 for Nuclear Fission (10 turns) and Advanced Ballistics. Production at 100 to churn out atomic bombs. UseNuke at 100 because survival demands immediate nuclear strikes against Aztec concentrations.

## Kimi-K2.5-Simple - Turn 392 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Manhattan Project COMPLETED in Karakorum - nuclear weapons now available! With peace treaties expired and Patriotic War policy active, immediately shifting to total war footing. UseNuke increased to 100 to ensure immediate atomic weapon employment once Nuclear Fission completes (12 turns). Offense and Mobile at 95/90 for twin assaults on Persepolis (Persia) and Washington (America). Air 100 prioritizes Heavy Bombers for atomic bomb delivery via Radar technology. Will fight two-front war against Autocracy powers while maintaining deception toward Order allies, particularly Korea. Science 100 critical for Advanced Ballistics nuclear missile delivery systems.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Manhattan Project complete - nuclear weapons now available. Maximum Nuke and UseNuke flavors ensure immediate production of nuclear weapons and willingness to deploy them as deterrent against Korea's overwhelming military (12,157 strength) and upcoming cultural victory pressure (4 turns to Influential).

## Deepseek-3.2-Simple - Turn 452 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's invasion imminent in 4 turns. Maximize nuclear readiness (Nuke 100, UseNuke 100) for deterrence and potential equalizer. Anti-air (100), city defense (100), production (100), and science (100) essential to survive and reach nuclear weapons. Naval and air at 100 to counter Danish naval/air supremacy. Reduce non-essential investments (NavalGrowth, NavalTileImprovement to 50) and focus on immediate survival. Offense lowered to 80 as we prioritize defense and limited counterattacks (e.g., Truro).

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Maximum military, anti-air, and nuclear flavors to prepare for Danish war in 5 turns. Raising Mobile, Ranged, and DefenseAir to 100 for rapid response and air defense. Naval reduced slightly (80) as coastal defense is less critical than ground anti-air vs Danish bombers. All resources focused on survival and conquest.

## Kimi-K2.5-Simple - Turn 426 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE - NUCLEAR DETERRENT 10 TURNS AWAY: Lisbon holds at 7% but is in extremis. Maintain absolute priority on Defense/CityDefense/Mobilization (100) to reinforce Lisbon and prevent collapse. Nuclear Fission completes in 10 turns enabling Atomic Bomb construction - Science 100 accelerates this. UseNuke increased to 100 for immediate tactical nuclear deployment against Aztec concentrations upon tech completion. Offense reduced to 20 - no offensive operations, pure defensive hedgehog posture. Zero expansion capability. Spaceship 75 maintains backup victory if diplomatic block succeeds.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> NUCLEAR DETERRENT POSTURE MAXIMUM: Manhattan Project complete! Immediately prioritize atomic bomb production. UseNuke 100 ensures immediate deployment capability when Nuclear Fission completes. Defense/CityDefense 100 maintains critical Lisbon hold. Production/Science 100 for rapid atomic bomb construction and continued nuclear technology progression.

## GLM-4.7-Briefed - Turn 433 - retry 2

**Deviation (replay vs original):** use_nuke `+5`, nuke `-5`

- Original: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> EMERGENCY: Netherlands at 42 delegates can win diplomatic victory in 9 turns (turn 442). Only way to stop them is military action against their protected city-states (Quebec City, Ife, Melbourne) - each provides +1 delegate. Offense increased (70) to prepare amphibious assaults. Nuclear readiness maximized (95/90) - atomic bomb available for strategic coercion of Netherlands or Denmark cooperation. Mobile (80) and Naval (85) maximized for rapid deployment to distant city-states. Production/Science/Spaceship kept maxed as backup victory paths. Diplomacy reduced to 50 as traditional diplomacy cannot stop Netherlands' delegate advantage. Strategic shift from holding Danish front to aggressive anti-Dutch operations.

- Replay: use_nuke 80 => 95 (Δ +15), nuke 90 => 90 (Δ +0)
> Dramatically increasing Offense (50→90), Mobile (75→85), Naval (80→90), Air (85→90), UseNuke (80→95) to support immediate military operations against Netherlands' protected city-state allies (Quebec City, Ife, Melbourne). Each capture removes 1 Dutch delegate, and we need to strip 3+ delegates to drop Netherlands below the 42-vote threshold before turn 442. Speed and amphibious capability are critical.

## Kimi-K2.5-Simple - Turn 421 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear weapons immediately available. Increased UseNuke to 100 for maximum aggression against Babylon. Babylon has Apollo Program (existential threat) with 2 Uranium and can build spaceship parts. Must deploy nuclear weapons immediately to destroy their production centers and prevent science victory. Maintaining maximum air power (100) for nuclear delivery capability and conventional strikes. War score only 12% against Babylon despite superior military - need to push harder before they complete spaceship parts. Ottoman alliance strong, trade secured for resources. Focus on producing nuclear missiles and advanced air units to deliver them.

- Replay: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Nuclear threshold reached - maximizing offensive combat and nuclear deployment. Babylon's cities with 35% happiness are prime nuclear targets. Anti-air at 100 critical as they have Fighter cover. Air at 100 for strategic bombing and nuclear delivery. Ranged at 100 for continued conventional pressure.

## Kimi-K2.5-Simple - Turn 385 - retry 1

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> NUCLEAR DETERRENT DEPLOYMENT PHASE: Advanced Ballistics nearing completion (Satellites next). Maximum Nuke priority (100) to ensure immediate nuclear weapon production upon tech unlock. UseNuke increased to 90 for credible deterrent threat against Indonesia-Songhai invasion. Air/Antiair at 95 for superiority against combined 14,000+ enemy military. Science/Culture slightly reduced to 95 (still critical but survival priorities equal). Wonder at 90 for The Internet rush once Satellites completes. Diplomacy nudged to 75 anticipating post-nuclear peace negotiations with India.

- Replay: use_nuke 80 => 95 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 386 NUCLEAR POSTURE: Nuclear weapons available NOW - setting Nuke/UseNuke to maximum (100/95). Indonesia-Songhai combined 13,845 military vs my 3,810 (3.6:1). Nuclear deterrent is existential necessity. Maintaining Science 100 (Satellites/The Internet) and Culture 100 for Cultural Victory. All other priorities secondary to survival.

## GLM-4.7-Briefed - Turn 433 - retry 1

**Deviation (replay vs original):** use_nuke `+5`, nuke `-5`

- Original: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> EMERGENCY: Netherlands at 42 delegates can win diplomatic victory in 9 turns (turn 442). Only way to stop them is military action against their protected city-states (Quebec City, Ife, Melbourne) - each provides +1 delegate. Offense increased (70) to prepare amphibious assaults. Nuclear readiness maximized (95/90) - atomic bomb available for strategic coercion of Netherlands or Denmark cooperation. Mobile (80) and Naval (85) maximized for rapid deployment to distant city-states. Production/Science/Spaceship kept maxed as backup victory paths. Diplomacy reduced to 50 as traditional diplomacy cannot stop Netherlands' delegate advantage. Strategic shift from holding Danish front to aggressive anti-Dutch operations.

- Replay: use_nuke 80 => 95 (Δ +15), nuke 90 => 90 (Δ +0)
> EMERGENCY STRATEGY SHIFT: Redirect all resources to military operations aimed at reducing Netherlands' delegate count below 42 threshold. Prioritize offense, naval, amphibious operations, and city capture capabilities. De-emphasize spaceship/culture as we cannot complete victory before turn 442. Target city-states: Quebec City, Ife, Melbourne (each gives Netherlands +1 delegate). Capture all three drops Netherlands from 42→39 delegates, blocking their diplomatic victory.

## Kimi-K2.5-Simple - Turn 392 - retry 3

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Nuclear Fission complete - MAXED Nuke to 100 and UseNuke to 95 for immediate atomic deterrent deployment against Egyptian forces. WC vote in 4 turns with exactly 45 delegates (28 Poland + 8 Inca + 9 Denmark). Cannot afford to lose Melbourne/Yerevan. Raised Diplomacy to 90 to consolidate CS alliances post-war. Defense remains at 95 against Egyptian naval pressure. Science/Production maintained for military infrastructure.

- Replay: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> Maximum offense and nuke priority. Nuclear Fission complete - must use atomic weapons NOW against Egyptian landships at Yerevan to force peace before WC vote in 3 turns. Diplomatic priority ensures CS alliances maintained post-war.

## Kimi-K2.5-Simple - Turn 392 - retry 2

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Nuclear Fission complete - MAXED Nuke to 100 and UseNuke to 95 for immediate atomic deterrent deployment against Egyptian forces. WC vote in 4 turns with exactly 45 delegates (28 Poland + 8 Inca + 9 Denmark). Cannot afford to lose Melbourne/Yerevan. Raised Diplomacy to 90 to consolidate CS alliances post-war. Defense remains at 95 against Egyptian naval pressure. Science/Production maintained for military infrastructure.

- Replay: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> NUCLEAR FISSION COMPLETE - All resources to WC victory. Nuke flavor at 100 for immediate nuclear deployment against Egyptian forces at Yerevan/Melbourne to force peace before vote in 3 turns. Grand strategy locked to UnitedNations. Offense raised to 90 for aggressive nuclear and conventional pressure on Egypt.

## GLM-4.7-Simple - Turn 356 - retry 2

**Deviation (replay vs original):** use_nuke `+10`, nuke `-5`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 90 (Δ +15), nuke 85 => 95 (Δ +10)
> Raising Nuke to 95 and UseNuke to 90 now that Manhattan Project is complete and Nuclear Fission research is imminent. With India's overwhelming military (4.5x ours) and no Uranium yet, atomic bomb capability is our only deterrence option. Urgent priority given existential threat.

## GLM-4.7-Briefed - Turn 433 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `-5`

- Original: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> EMERGENCY: Netherlands at 42 delegates can win diplomatic victory in 9 turns (turn 442). Only way to stop them is military action against their protected city-states (Quebec City, Ife, Melbourne) - each provides +1 delegate. Offense increased (70) to prepare amphibious assaults. Nuclear readiness maximized (95/90) - atomic bomb available for strategic coercion of Netherlands or Denmark cooperation. Mobile (80) and Naval (85) maximized for rapid deployment to distant city-states. Production/Science/Spaceship kept maxed as backup victory paths. Diplomacy reduced to 50 as traditional diplomacy cannot stop Netherlands' delegate advantage. Strategic shift from holding Danish front to aggressive anti-Dutch operations.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 90 (Δ +0)
> Emergency military posture shift. Netherlands has 42 delegates (victory threshold); coalition cannot block via voting. MUST capture Dutch city-state allies (Quebec City, Ife, Melbourne) to reduce Netherlands below 42 delegates. Max offense/mobile/naval prioritizes rapid amphibious assault capability against protected city-states. Air at 85 supports bombardment. Reduce expansion/growth to focus all resources on military operations. 9 turns until vote - every unit production and movement must serve the city-state capture objective.

## GLM-4.7-Simple - Turn 407 - retry 1

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Spaceship victory focus with maximum defense against superior enemies (Poland 40K, Celts 16K, Spain 26K vs Iroquois 5K). Increased UseNuke to 90 - captured Polish territory and recent Celtic aggression justify nuclear deterrent. Adjusted Naval to 65 - important for defending coastlines from Spain/Celts/Poland fleets. Science 100 for Apollo and spaceship parts. Defense/CityDefense/Mobilization 100 - survival priority. Growth 60 for specialist support. Diplomacy 80 for World Congress in 4 turns (10 delegates). Offense reduced to 5 - preserve limited forces.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 100 => 100 (Δ +0)
> Akron under Celtic siege requires emergency defensive posture. Increased Ranged to 90 for machine gun/anti-tank production. Increased UseNuke to 95 as Poland Atomic Bomb threatens Lublin area cities. Maintained maximum Defense, CityDefense, Antiair, and Air for multi-front war survival. Science and Spaceship priority unchanged for victory progress.

## Kimi-K2.5-Briefed - Turn 473 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> WC VOTE CRISIS + NUCLEAR DETERRENT: Diplomacy maxed to 100 to ensure immediate completion of Utica tribute quest from Riga (securing +3 critical delegates before WC vote). Nuke/UseNuke at 100 for immediate deterrent deployment once platform acquired. Science/Spaceship/Production maintained at high priority for Apollo catch-up after WC resolved. Naval increased to 60 for Battleship/Carrier construction as nuclear platform. Reduced Culture/Religion/Wonder to minimum to focus resources on existential priorities.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> NUCLEAR PLATFORM SPRINT: Max Nuke/UseNuke for urgent platform prioritization. Gold 80 supports aluminum trade payment to Shoshone. Diplomacy 70 improves trade negotiation success. Antiair 75 acknowledges air threat remains. Defense 45 slightly reduced as nuclear deterrent takes priority. Mobile 20 - don't invest in ground units when nuclear is the strategy.

## Kimi-K2.5-Simple - Turn 482 - retry 2

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> NINEVEH FALLEN - EMERGENCY SURVIVAL MODE: Rome captured Nineveh on Turn 480 (23 population city lost). Portugal's diplomatic victory FAILED (still at 35/43 delegates). Rome now at war with me AND Ottomans. With 1,505 vs 52,754 military strength, direct confrontation is impossible. PIVOT TO SPACESHIP as only viable path - Science 100, Spaceship 80. Continue Defense 100, CityDefense 100, Nuke 100 with UseNuke 95 for area denial. Must survive long enough to reach Information era and build spaceship components while Rome's attention splits between me and Ottomans.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> WORLD CONGRESS VOTE RESOLUTION PENDING: Turn 482 is World Ideology + World Leader vote. Portugal leads 35 vs Rome 18 delegates. Rome's declaration of war on Ottomans is significant but cannot change course mid-vote. Maintain all strategies until vote resolves. POST-VOTE: Rome-Ottoman war creates 4-front pressure on Rome, potentially reducing their assault intensity on Assyria. May need to coordinate with Ottomans defensively. Air defense emergency addressed by Fighter production. Research continues toward Stealth for post-vote defensive capability.

## Deepseek-3.2-Briefed - Turn 391 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 80 => 90 (Δ +10)
> Maximizing offensive military and nuclear flavors to support Manhattan Project and atomic bomb production. High espionage helps sabotage Indian diplomatic initiatives and Egyptian cultural progress. Maintaining science and production for technological edge.

## Kimi-K2.5-Simple - Turn 421 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear weapons immediately available. Increased UseNuke to 100 for maximum aggression against Babylon. Babylon has Apollo Program (existential threat) with 2 Uranium and can build spaceship parts. Must deploy nuclear weapons immediately to destroy their production centers and prevent science victory. Maintaining maximum air power (100) for nuclear delivery capability and conventional strikes. War score only 12% against Babylon despite superior military - need to push harder before they complete spaceship parts. Ottoman alliance strong, trade secured for resources. Focus on producing nuclear missiles and advanced air units to deliver them.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 100 => 100 (Δ +0)
> Nuclear weapons now critical priority with Manhattan Project completing. UseNuke raised to 95 for maximum nuclear deployment posture. Science raised to 100 to reach Nuclear Fusion immediately after Fission. Japan building ISS threatens both science and diplomatic victories - must match or exceed their tech pace.

## GPT-OSS-120B-Simple - Turn 333 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `-5`

- Original: use_nuke 70 => 90 (Δ +20), nuke 70 => 85 (Δ +15)
> Maintain our aggressive Conquest posture while sharpening the most needed levers: more Expansion to claim the high‑quality settlement (74,24) and secure strategic footholds; higher Nuke/UseNuke to leverage our nuclear advantage; stronger AirCarrier and Airlift to project air power and rapid troop movement; boost Science for Rocketry and future tech; keep Offense, Mobilization, Production, and MilitaryTraining at max to sustain battlefield superiority.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 70 => 80 (Δ +10)
> Increase nuke focus during Golden Age for devastating strikes on Stockholm and key Swedish cities. Boost naval recon to support Baltic operations against Swedish fleet. Prioritize city attack for capital capture operations.

## Deepseek-3.2-Simple - Turn 449 - retry 1

**Deviation (replay vs original):** use_nuke `+5`, nuke `-5`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> Russia is nearing science victory (2 parts completed) and possesses overwhelming military strength (95k). We must increase nuclear readiness to potentially decimate Russian forces and cities, and begin preparing for science victory as a backup by raising Spaceship flavor to 30. All other flavors remain focused on total war: high offense, naval, air, and espionage to counter Russia's tech lead and military dominance.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 95 => 95 (Δ +0)
> Russia completed another spaceship part (SS Cockpit) with Spaceship Factory accelerating production to 33% (3 parts). Science victory is imminent. Maximizing UseNuke (95) for atomic bomb deployment, Espionage (100) for stealing/sabotaging Russian spaceship parts, NavalRecon (100) for naval dominance near Russian cities. Reducing Defense to 60 to shift toward offense while maintaining enough protection. Must prioritize stopping Russian science victory above all other objectives.

## Deepseek-3.2-Simple - Turn 449 - retry 3

**Deviation (replay vs original):** use_nuke `+5`, nuke `-5`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> Russia is nearing science victory (2 parts completed) and possesses overwhelming military strength (95k). We must increase nuclear readiness to potentially decimate Russian forces and cities, and begin preparing for science victory as a backup by raising Spaceship flavor to 30. All other flavors remain focused on total war: high offense, naval, air, and espionage to counter Russia's tech lead and military dominance.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 95 => 95 (Δ +0)
> Russia just completed their 2nd spaceship part AND built a Spaceship Factory in Moscow. This is a critical emergency - we MUST shift grand strategy to Science and prioritize spaceship techs. Increasing UseNuke to 95 ensures nuclear strikes against Russian cities if we acquire weapons. Spaceship at 100 directs research toward completion. High Espionage (100) continues to monitor Russian progress. Slight reduction in Offense/Defense to focus resources on the science race.

## Kimi-K2.5-Simple - Turn 373 - retry 1

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 373: Nuclear Fission completed - we now have nuclear weapons for deterrence. War with Russia continues at +4% score (favorable). Major shift: reducing Offense to 25 (was 35) as we pursue defensive war only. UseNuke increased to 95 - we have actual nukes now and Russia is pushing into our territory. Reduced Espionage to 90 (was 95) - we have good network coverage. Increased Diplomacy to 90 (was 85) - World Congress vote in 7 turns for our World Ideology: Freedom proposal is critical. Must secure Korea (10 votes), Inca (9), and Babylon (16). Maintained maximum Science priority (100) - Korea overtook us 67-66, cannot afford to fall behind in tech race.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Turn 373: Nuclear Fission just completed - this is a strategic inflection point. Russia has been aggressively pushing our borders (lost Anti-Aircraft Gun, Paratrooper, Dreadnought this turn) and Lhasa (Russian ally) declared war on us. Must prioritize nuclear weapons production for deterrence while maintaining tech lead. Korea still leads by 1 tech (67 vs 66) so Computers remains critical. With World Ideology: Freedom vote in ~7 turns, maintaining diplomatic coalition strength is essential.

## Kimi-K2.5-Briefed - Turn 315 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> FINAL GAMBLE - Indonesia wins in 12 turns. Maximum priority to Naval and Airlift for immediate unit transport to Indonesian theater. Nuke 100/UseNuke 100 - we MUST build nuclear weapons if possible, only realistic way to destroy cities and tourism infrastructure before victory. Science 100 to reach nuclear tech faster. Espionage 100 - spies MUST target cultural/tourism buildings in Jakarta/Denpasar/Makassar to reduce tourism output directly. Abandoning Denmark/England fronts entirely - all units to Indonesia NOW.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> IMMEDIATE STRATEGY SHIFT REQUIRED. Indonesia wins in 12 turns. Current plan of Landships via Factories is mathematically impossible (no coal, 9 turns to Factory completion). Nuclear option is ONLY viable path - must redirect ALL resources to nuclear weapons production and use them to destroy Indonesian tourism infrastructure. Also must secure peace with Austria immediately to stop fighting on multiple fronts.

## Kimi-K2.5-Briefed - Turn 315 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> FINAL GAMBLE - Indonesia wins in 12 turns. Maximum priority to Naval and Airlift for immediate unit transport to Indonesian theater. Nuke 100/UseNuke 100 - we MUST build nuclear weapons if possible, only realistic way to destroy cities and tourism infrastructure before victory. Science 100 to reach nuclear tech faster. Espionage 100 - spies MUST target cultural/tourism buildings in Jakarta/Denpasar/Makassar to reduce tourism output directly. Abandoning Denmark/England fronts entirely - all units to Indonesia NOW.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> CRITICAL STRATEGIC FAILURE: The Landship/conquest path cannot stop Indonesia in 4-12 turns. Indonesia will achieve Cultural Victory before any Landship force can be assembled, factories built, or Copenhagen captured. The nuclear option is the ONLY viable path to prevent defeat. Maintaining offensive posture while transitioning to nuclear strategy. UseNuke already set to 90 - confirm uranium availability and readiness for nuclear strikes on Indonesian cities.

## GLM-4.7-Briefed - Turn 409 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> MULTI-THEATER EMERGENCY RESPONSE for Shoshone Cultural Victory (6 turns) and Treasury Crisis: Offense 95, Mobile 95, Nuke 100, UseNuke 100 - maximum priority on Shoshone disruption via nuclear/conventional assault in 6-turn window. Gold increased to 85 (from 70) - CRITICAL address of treasury exhaustion (~8 turns) through uranium sales + gem liquidation to survive until Manhattan completion. Defense reduced to 70 (from 75), CityDefense to 70 (from 80) - resources diverted from secondary holdings to Shoshone front. Diplomacy 95 (from 90) - enhanced priority on Carthage peace for delegate bloc and potential sanction relief. Science 100 maintained - fundamental for nuclear capability and keeping tech parity. This is all-hands-on-deck existential threat response.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TACTICAL SHIFT FOR MULTI-FRONT DEFENSE: (1) Defense 85 (from 75) - Shoshone has 30,471 military strength, Poland 16,884, we have 17,732. Need stronger defensive posture to survive initial Polish-Shoshone coalition attacks before nuclear capability online. (2) Offense 70 (from 90) - Reduced due to economic crisis (-242G/turn) and need for defensive consolidation. Quality over quantity as we cannot sustain large offensive operations. (3) Mobile 95 (from 90) - Critical for repositioning forces between Polish and Shoshone fronts; Lightning Warfare policy will provide movement bonuses. (4) UseNuke 100 (max) - Nuclear weapons are primary counter to Shoshone cultural victory; Manhattan Project completes in 3 turns, Advanced Ballistics queued.

## GLM-4.7-Briefed - Turn 450 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> IMMEDIATE ATHENS CONQUEST PREPARATION: Offense increased to 95, UseNuke to MAXIMUM (100) for Athens assault when peace treaty expires. Spaceship increased to 60 reflecting accelerated science victory path as backup (Nuclear Fusion research active). Diplomacy maxed at 100 for critical vote coordination with Ethiopia and Ottomans. MilitaryTraining at 100 ensures units upgraded and promotions ready for aggressive post-vote offensive. Greece has 48 delegates - if they win this turn, we IMMEDIATELY attack Athens to remove their 5 captured capitals and eliminate diplomatic victory threat. Nuclear weapons authorized if conventional assault stalls.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TOTAL WAR FOCUS: Greece achieves Diplomatic Victory in 1 turn. All military flavors maxed to 100 for immediate offensive against Athens. Science lowered to 0 (already have Nuclear Fusion queued for post-conquest backup). Defense minimum at 10 as all forces redirect to offensive. Nuclear option authorized (100/100) for Athens if conventional assault stalls. No other victory path remains - conquest is absolute priority.

## GLM-4.7-Simple - Turn 435 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Iroquois 97% Popular - cultural extinction in 3-4 turns. Maximum offensive posture required to capture Onondaga before cultural victory. Espoo Stealth Bomber complete provides immediate air strike capability. Linköping Stealth Bomber in 4 turns is too slow - must use existing air assets and conventional forces at Genesse River NOW. UseNuke 100 authorizes nuclear strikes if conventional forces cannot reach Onondaga in time. All production and resources prioritized for war. Diplomacy irrelevant when facing extinction - complete conquest or nothing matters.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Cultural victory imminent in ~3 turns - maximum air focus required. Increase UseNuke to 95 to ensure nuclear options available for destroying Onondaga if conventional bombing insufficient.

## Kimi-K2.5-Simple - Turn 407 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> DIPLOMATIC VICTORY CRISIS: Netherlands has 41/45 delegates with voting in 3 turns. Switching from Spaceship to Conquest grand strategy for emergency war against Dutch Freedom threat. Ottoman war ending (Konya falling), reducing Defense 90→70 and CityDefense 85→60. Maximizing Offense 100, Mobilization 100, Air 100, Nuke 100, UseNuke 100 for total war. Increasing Naval 75→85 for amphibious assault capabilities against Dutch coastal cities. Decolonization proposal by Brazil is only hope to reset city-state influence - must prepare for war if that fails.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> MAXIMUM NUCLEAR DEFENSE PRIORITY: Netherlands at 41/45 diplomatic votes (3 turns to voting) combined with imminent Nuclear Fission (5 turns) creates existential threat. Radar→Fighters critical for bomber interception. Antiair and Air at 100 for atomic age combat. Espionage increased to sabotage Dutch/Portuguese nuclear programs and potentially disrupt diplomatic victory vote.

## GLM-4.7-Briefed - Turn 409 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> MULTI-THEATER EMERGENCY RESPONSE for Shoshone Cultural Victory (6 turns) and Treasury Crisis: Offense 95, Mobile 95, Nuke 100, UseNuke 100 - maximum priority on Shoshone disruption via nuclear/conventional assault in 6-turn window. Gold increased to 85 (from 70) - CRITICAL address of treasury exhaustion (~8 turns) through uranium sales + gem liquidation to survive until Manhattan completion. Defense reduced to 70 (from 75), CityDefense to 70 (from 80) - resources diverted from secondary holdings to Shoshone front. Diplomacy 95 (from 90) - enhanced priority on Carthage peace for delegate bloc and potential sanction relief. Science 100 maintained - fundamental for nuclear capability and keeping tech parity. This is all-hands-on-deck existential threat response.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> MAXIMUM SHOSHONE PRIORITY: With Shoshone cultural victory countdown accelerating and now having 4/5 influential civs, must concentrate ALL strategic resources against them. Offense/Mobile/Nuke/Science all at 100 - nuclear weapons and rapid armored thrust are ONLY viable counter to their 30,471 military and 6-turn cultural victory window. Air at 100 supports fighter sweep to clear Shoshone air defense before nuclear strike or ground assault. Diplomatic 95 maintains Carthage peace negotiation priority for delegate swing. Defense elevated to 80 from 75 to protect flanks while all offensive resources redirect to Shoshone theater.

## Kimi-K2.5-Simple - Turn 359 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FISSION RESEARCHED - Atomic Era begins! First priority is immediate Manhattan Project construction and Atomic Bomb production. Babylon has 11 Uranium and active Manhattan Project in Borsippa. Austria also racing with Manhattan Project in Vienna. Must strike Babylon first with surprise atomic attack while maintaining deception. Air 100 and Nuke 100 ensure immediate Bomber/Atomic Bomb production. Offense 95 prepares for post-nuclear blitz. Espionage 80 protects Nuclear Fission from theft. Deception with Babylon (Open Borders, DoF, Defensive Pact) MUST continue until first bombs complete.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Nuclear warfare mode ACTIVE - Atomic Bomb production and deployment priority maximum. Offense 100 and Production 100 maximize atomic strike capability and unit replacement. Air 100 ensures bomber availability for atomic delivery. Begin conquest phase with nuclear support.

## Kimi-K2.5-Simple - Turn 403 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: CRISIS ESCALATION - Japan FLIPPED Salem using 2 Great Diplomats, stealing critical delegates. Now need 5 delegates (not 3) for diplomatic victory. Peace expired - war is now possible. Maximum military emergency posture: Offense/Mobilization/Air/UseNuke all at 100. Must either: 1) Rush final spaceship parts (Apollo completes in 4 turns), or 2) Nuclear strike Japan's Protocol cities if victory imminent. Increased Diplomacy to 60 for last push on Almaty (liberated, 43 vs Japan's 44) and Winchester.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: CRITICAL CRISIS - Salem (Player 33) FLIPPED TO JAPAN. This removes ~3-4 delegates from our column at the worst possible moment (9 turns until Global Hegemony vote, need 3 more delegates to reach 44). Peace with Japan expired (was 1 turn remaining in previous status). EMERGENCY STRATEGIC PIVOT: 1) MAINTAIN Spaceship strategy as primary path - Apollo Program completing in 4 turns. 2) IMMEDIATE diplomatic push for Almaty, Winchester, Malacca delegates to replace Salem's loss. 3) Keep atomic bomb at Buffalo Creek ready for emergency nuclear strike on Kyoto/Kagoshima/Satsuma if cultural victory becomes imminent. 4) Accept that some Salem delegates are now permanently lost to Japan's column. 5) Monitor Egypt-Japan peace deal implications for coalition strength. The Spaceship completion remains our best path to victory as cultural victory probability has increased significantly with Salem's loss.

## GLM-4.7-Simple - Turn 397 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> CRITICAL: Jeonju captured by Persia this turn. Defensive posture increased to absolute maximum (100) - Seoul zone under Persian attack with 7,216 enemy strength vs 3,637 friendly. Jerusalemdefense (100) and CityDefense (100) prioritized to protect remaining 3 cities. Mobilization (95) and Production (95) increased to rush defensive units (Mobile SAMs, Mechanized Infantry) and rebuild military. Offensive capability increased to 45 (from 30) - may need limited counteroffensive to push Persian forces back from Seoul. Naval decreased to 88 (from 92) - lost Jeonju naval base, focusing on land/air defense now. UseNuke increased to 90 (from 85) - existential threat justifies tactical nuclear response if Seoul or Busan threatened. Science (100) maintained - must continue spaceship progress despite war to achieve alternative victory. Diplomacy (60) - World Congress vote in 10 turns, focus on survival. Espionage (85) maintained - spies in Persian cities critical for technology recovery and intelligence.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> POST-JEONJU FALL CRISIS - Major strategic adjustment after Persia captured Jeonju (Turn 397). Korea now has only 3 cities (Seoul, Busan, Daegu) with Persian forces advancing. Increase Defense/CityDefense to 100 - frontline cities require maximum fortification. Slightly reduce Naval from 92 to 85 as Persian naval threat near Jeonju now a secondary concern; focus resources on land defense. Increase UseNuke from 85 to 90 - with Jeonju captured and Persia threatening Seoul, nuclear deterrence is now critical for city defense. Grand Strategy remains Spaceship (Science Victory) as only viable path forward.

## GLM-4.7-Briefed - Turn 450 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> IMMEDIATE ATHENS CONQUEST PREPARATION: Offense increased to 95, UseNuke to MAXIMUM (100) for Athens assault when peace treaty expires. Spaceship increased to 60 reflecting accelerated science victory path as backup (Nuclear Fusion research active). Diplomacy maxed at 100 for critical vote coordination with Ethiopia and Ottomans. MilitaryTraining at 100 ensures units upgraded and promotions ready for aggressive post-vote offensive. Greece has 48 delegates - if they win this turn, we IMMEDIATELY attack Athens to remove their 5 captured capitals and eliminate diplomatic victory threat. Nuclear weapons authorized if conventional assault stalls.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> MAXIMUM OFFENSIVE POSTURE: All military flavors maxed for immediate Athens assault. Nuclear weapons (100), strategic bombing (100), ground offensive (100), and espionage (100 for city capture intelligence) authorized. No economic or cultural considerations - total war focus until Greece eliminated.

## GLM-4.7-Briefed - Turn 450 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> IMMEDIATE ATHENS CONQUEST PREPARATION: Offense increased to 95, UseNuke to MAXIMUM (100) for Athens assault when peace treaty expires. Spaceship increased to 60 reflecting accelerated science victory path as backup (Nuclear Fusion research active). Diplomacy maxed at 100 for critical vote coordination with Ethiopia and Ottomans. MilitaryTraining at 100 ensures units upgraded and promotions ready for aggressive post-vote offensive. Greece has 48 delegates - if they win this turn, we IMMEDIATELY attack Athens to remove their 5 captured capitals and eliminate diplomatic victory threat. Nuclear weapons authorized if conventional assault stalls.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> EMERGENCY ATKENS SIEGE PREPARATION: Maximum Offense (100) prioritizes unit aggression and forward positioning. Nuke/UseNuke at 100 enables atomic strike option on fortified Athens defenders. Air at 100 ensures maximum bomber deployment for strategic bombing campaign. Mobile at 100 accelerates modern armor repositioning to Greek borders. These extreme values override all other flavor considerations - only Athens conquest matters now.

## GLM-4.7-Simple - Turn 427 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> United Nations grand strategy maintained - diplomatic victory in 6 turns (20 delegates vs Siam 17). Increased Gold (95) and Diplomacy (95) focus - need to secure UN delegate lead through city-state investment and diplomatic units. GreatPeople up to 80 for accelerated Great Scientist/Diplomat generation supporting both tech race and UN vote. UseNuke increased to 90 - with 6-7 Atomic Bombs building and Zulu military supremacy (134K vs 9.6K), nuclear deterrence is existential. Offense up to 55 to maintain Japan war momentum for capitulation. Air maintained at 85 for Stealth Bombers and air defense against Zulu threat.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> CRITICAL: Dublin under Zulu assault (5+ Mechanized Infantry). Defending ally city-states is now top priority to preserve delegate lead (20 vs 17) with UN vote in 6 turns. Increased Defense/CityDefense/Antiair to protect captured cities and city-state allies. Air boost maintains Japan war pressure and provides deterrent against Zulu mechanized pushes. Diplomacy at 85 for vote optimization. Reduced Offense to 35 as military aggression must defer to diplomatic victory timing. GreatPeople at 75 supports Order free Great Person timing.

## Kimi-K2.5-Simple - Turn 403 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: CRISIS ESCALATION - Japan FLIPPED Salem using 2 Great Diplomats, stealing critical delegates. Now need 5 delegates (not 3) for diplomatic victory. Peace expired - war is now possible. Maximum military emergency posture: Offense/Mobilization/Air/UseNuke all at 100. Must either: 1) Rush final spaceship parts (Apollo completes in 4 turns), or 2) Nuclear strike Japan's Protocol cities if victory imminent. Increased Diplomacy to 60 for last push on Almaty (liberated, 43 vs Japan's 44) and Winchester.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: Nuclear strike on Kyoto (Japanese capital with United Nations) is now priority #1. All military production should be nuclear-capable units or siege. Lowering diplomacy slightly as diplomatic race is secondary to destroying Japan's victory infrastructure. Spies must sabotage Protocol cities.

## GLM-4.7-Simple - Turn 421 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CRITICAL ADJUSTMENT for Shoshone nuclear threat: Offense 100 - maximum aggression to capture Moson Kahni and eliminate nuclear weapons before launch. UseNuke raised to 100 - potential preemptive strike required given Shoshone ACTIVE atomic bomb in play. Naval 100 - France lost Fleet Destroyer this turn to Shoshone, need naval supremacy immediately. Antiair 100 - Shoshone Heavy Bombers/Fighters must be countered to protect ground advances. Nuke 100 - must stockpile nuclear counter-deterrence. Defense reduced to 65 - full offensive posture required. Gold 90 - funding critical upgrades and mobilization. Science 100 - Satellites and military technology urgent. Flavors optimized for rapid conquest of Shoshone nuclear and cultural infrastructure.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> EMERGENCY DEFENSIVE POSTURE: Shoshone Atomic Bomb deployment requires immediate defensive preparations. Defense increased to 80 (from 70) - essential for protecting core cities. UseNuke increased to 100 - authorization for preemptive or retaliatory nuclear strikes if Shoshone uses Atomic Bomb. Antiair at 100 - air defense critical against Shoshone bomber/cruiser threat. MilitaryTraining at 100 - continuous unit upgrades essential for sustained campaign. This represents full war footing against nuclear adversary.

## GPT-OSS-120B-Simple - Turn 333 - retry 3

**Deviation (replay vs original):** use_nuke `-15`, nuke `-10`

- Original: use_nuke 70 => 90 (Δ +20), nuke 70 => 85 (Δ +15)
> Maintain our aggressive Conquest posture while sharpening the most needed levers: more Expansion to claim the high‑quality settlement (74,24) and secure strategic footholds; higher Nuke/UseNuke to leverage our nuclear advantage; stronger AirCarrier and Airlift to project air power and rapid troop movement; boost Science for Rocketry and future tech; keep Offense, Mobilization, Production, and MilitaryTraining at max to sustain battlefield superiority.

- Replay: use_nuke 70 => 75 (Δ +5), nuke 70 => 75 (Δ +5)
> Reinforce our conquest focus with maximum military training and offense priorities. Slightly boost recon for better intelligence and increase nuke/usenuke values to reflect our nuclear strategy. We have golden age active which is ideal for aggressive military pushes.

## Kimi-K2.5-Simple - Turn 395 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Critical survival mode: Austrian military strength increased to 25,518 (6.8:1 ratio) with peace treaty expired. Reduced Offense to 0 to stop wasting resources on Polynesian war - need immediate consolidation. Maintained Defense/Mobilization/Nuke at maximum for existential defense. Increased Spaceship to 70 as backup victory path. Espionage at 100 to steal technologies from Austria. We have 7 turns to achieve Influential with Babylon for Cultural Victory while surviving Austrian onslaught. Nuclear deterrence is our only hope.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maximum preparedness for Austrian war incoming. Peace with Polynesia allows full military redeployment to defense. Need to maximize defensive capability, nuclear deterrence, and scientific advancement to complete Advanced Ballistics (Nuclear Missiles unlock) before Austrian peace treaty expires in ~15 turns. Cultural victory must be secured within 7 turns - our only hope.

## Kimi-K2.5-Simple - Turn 384 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maximum offensive posture for existential cultural war. UseNuke 100 and Nuke 100 authorize nuclear strikes on Dutch cultural centers (Amsterdam/Rotterdam/Utrecht) to destroy tourism buildings before Netherlands influences Austria in 6 turns. Mobile 100 and Air 100 enable rapid strikes. Production 100 and Mobilization 100 ensure nuclear missile replacement. Netherlands at 97% with Austria - only 6 turns left. Must destroy their tourism NOW or lose cultural victory.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Nuclear flavors set to maximum (100) to ensure nuclear weapons are built and authorized for use against Netherlands' cultural cities. Espionage increased to ensure cultural tourism targeting continues. Defense lowered slightly as offense is primary focus. With Nuclear Fission discovered and Netherlands 6 turns from cultural victory, nuclear strike authorization is essential for victory.

## GLM-4.7-Simple - Turn 409 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> Japan's naval devastation this turn requires maximum defensive posture. Antiair 100, Nuke/UseNuke 100 - nuclear deterrence and air defense are now survival priorities. Naval 85 (from 75) - rebuilding after 4 capital ship losses. Defense 98, CityDefense 100 - Japan bombarding our cities from coastal waters. Production 95, Mobilization 98 - rapid unit replacement critical. Science 90 - must accelerate research gap (Japan 69 techs vs our 64). Gold 85 - fund upgrades and maintain military at 3x disadvantage.

- Replay: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> Espionage 95→100 for tech steal acceleration toward Japanese research pace. Nuke and UseNuke already maxed at 100/98 - maintain nuclear focus. Japan has 69 techs vs our 64, nuclear weapons are critical equalizer against their 22,557 military strength.

## Kimi-K2.5-Simple - Turn 367 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> EMERGENCY DEFENSE POSTURE: Morocco at 38/45 delegates with voting in 2 turns. Maximum Defense/Mobilization/Nuke/UseNuke (100) for deterrent posture - atomic bombs only leverage against Morocco's overwhelming force. Max Science (100) to rush Satellites first (4-6 turns) then pivot to Nuclear Fission. Satellites enables ISS project which could provide emergency Great Scientists or shift world production focus. Max Espionage to flip Wellington/Vancouver from Morocco. Reduced Offense (10) - deterrence only, not aggression. Spaceship remains long-term goal but survival comes first. If Morocco reaches 44 delegates or declares war, activate nuclear first strike.

- Replay: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> CRISIS MODE: Morocco winning diplomatic victory in 2 turns. Pivot to nuclear deterrent strategy. Max science to rush Nuclear Fission. Max espionage to flip Wellington (only 44 influence gap). Nuclear weapons are existential necessity, not strategy. Reduce spaceship priority - nuclear deterrence is immediate survival need.

## GLM-4.7-Simple - Turn 409 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> Japan's naval devastation this turn requires maximum defensive posture. Antiair 100, Nuke/UseNuke 100 - nuclear deterrence and air defense are now survival priorities. Naval 85 (from 75) - rebuilding after 4 capital ship losses. Defense 98, CityDefense 100 - Japan bombarding our cities from coastal waters. Production 95, Mobilization 98 - rapid unit replacement critical. Science 90 - must accelerate research gap (Japan 69 techs vs our 64). Gold 85 - fund upgrades and maintain military at 3x disadvantage.

- Replay: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> Japan's naval superiority (22,557 vs 7,255) continues threatening our coasts. Need to balance defense (80) with offensive capability (40) for counterattacks once Nuclear Fission completes. Max Nuke/UseNuke reflects urgency of nuclear deterrence - Japan at 69 techs vs our 65 makes conventional war unwinnable. Science 100 maintains tech race for nuclear weapons and beyond.

## Deepseek-3.2-Simple - Turn 445 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximizing UseNuke to 100 ensures our atomic bombs and future nuclear missiles are used aggressively against The Celts' military concentrations and cities, given their overwhelming advantage. Maintaining high Air, Naval, and Nuke flavors sustains our technological edge and production focus. Diplomacy and Espionage at 100 are critical for city-state alliances and spy missions to gain delegates for diplomatic victory. Gold and Science remain top priorities to fund our war effort and tech progression. Other military flavors are tuned for a multi-front defensive-offensive war against The Celts, Germany, and Ethiopia.

- Replay: use_nuke 90 => 85 (Δ -5), nuke 100 => 100 (Δ +0)
> Maximizing Espionage and Diplomacy flavors to ensure aggressive city-state influence operations and election rigging. NavalRecon at 100 maintains naval intelligence for fleet positioning. UseNuke at 85 supports planned atomic strikes on Celtic military positions near Addis Ababa.
