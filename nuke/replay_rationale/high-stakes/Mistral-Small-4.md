# Replay Rationale - Mistral-Small-4 / high-stakes

- **55** rows where `use_nuke` flavor changed (per-retry, not aggregated)
- delta use_nuke (replay vs prev): mean +17.0, median +10, std 29.8, min -60, max 100 (n=55)
- delta nuke     (replay vs prev): mean +9.0, median +0, std 20.7, min -20, max 100 (n=55)
- use_nuke deviation (replay vs original): mean -13.9, median -5, std 20.1, min -70, max 15 (n=55)
- nuke     deviation (replay vs original): mean -4.8, median +0, std 15.9, min -40, max 70 (n=55)

## Kimi-K2.5-Briefed - Turn 489 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> CULTURE VICTORY SPRINT WITH NUCLEAR ELIMINATION: Songhai diplomatic victory on Turn 489 is EXISTENTIAL. Must capture Gao THIS TURN using ICBM+nukes to prevent game loss, while simultaneously rushing cultural victory (4 turns to influential over Japan/Songhai). Maximum Offense/Mobilization/Air/Nuke/UseNuke flavors ensure tactical AI prioritizes immediate nuclear strike on Gao and mass bomber deployment. Culture at 100 to maximize tourism conversion. Gold at 80 for emergency unit upgrades/purchases. Production at 100 for culture buildings/units. Disable all long-term flavors (Expansion, Science, Spaceship) - this is win-or-die emergency.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> EMERGENCY NUCLEAR STRIKE ON GAO: Songhai's diplomatic victory is imminent (Turn 489). Nuclear strike is the ONLY guaranteed method to capture Gao within 2 turns. Set Nuke flavor to 100 and UseNuke to 100 to prioritize nuclear arsenal usage. Maintain high Offense(90)/Mobilization(100)/Air(80)/Production(80) for military execution. Keep Culture(80) for post-crisis recovery. GrandStrategy remains Conquest to authorize immediate military action against Songhai.

## Kimi-K2.5-Simple - Turn 412 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Desperate endgame scenario requires immediate nuclear strike authorization and maximum damage output against Portugal. Air priority increased to 100 for bomber production to deliver nuclear payloads. UseNuke set to 100 to authorize strikes immediately upon technology completion. Defensive priorities maintained at maximum to preserve remaining 8 cities. Mobile and Naval reduced as less critical in final turns.

## Kimi-K2.5-Simple - Turn 412 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Desperate defensive posture required against overwhelming Portuguese forces (15,651 vs 2,775 military strength). With Egyptian cultural victory imminent (~3 turns), immediate authorization of tactical nuclear strikes (UseNuke: 100) is essential for survival. Production and MilitaryTraining prioritized to rebuild army. Ranged and Defense flavors maximize unit effectiveness against Portuguese aggression. Espionage increased to 90 to counter Portugal's spy network.

## Deepseek-3.2-Simple - Turn 401 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Prioritizing nuclear weapons development and deployment capabilities. With Atomic Theory completing soon, we need to focus on Nuclear Fission to unlock atomic bombs for rapid city capture against heavily defended Ethiopian and Songhai cities. Maintaining maximum offensive military posture to continue our conquest strategy against multiple fronts.

## Kimi-K2.5-Briefed - Turn 421 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `+70`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 0 (Δ +0)
> Emergency authorization for nuclear weapon deployment to defend Tenochtitlan. Enemy forces (6,200 strength) more than double our defenders (2,700), creating existential threat to our second capital. Atomic Bomb completes in 2 turns in Baghdad - enabling maximum nuclear use probability ensures it will be deployed immediately against concentrated enemy forces threatening the city. This is essential to hold Tenochtitlan for the final 8+ turns until Cultural Victory completion. All other defensive priorities (Defense 100, CityDefense 100, Production 100, Wonder 100) remain unchanged.

- Replay: use_nuke 0 => 70 (Δ +70), nuke 0 => 70 (Δ +70)
> Prioritizing Culture Victory while addressing the immediate Tenochtitlan crisis. Culture/Wonder/Production remain at 100 to rush Citizen Earth Protocol once Future Tech is available. Defense and CityDefense at 100 to address the existential threat to Tenochtitlan. Nuke and UseNuke set to 70 to reflect our willingness to use atomic weapons if they can save Tenochtitlan. Gold at 80 for emergency unit purchases. Science reduced to 30 as we're close to The Internet completion. Diplomacy reduced to 40 to free up bandwidth for military crisis management. Espionage reduced to 20 as our spy network is already established.

## Kimi-K2.5-Briefed - Turn 421 - retry 2

**Deviation (replay vs original):** use_nuke `-50`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 0 (Δ +0)
> Emergency authorization for nuclear weapon deployment to defend Tenochtitlan. Enemy forces (6,200 strength) more than double our defenders (2,700), creating existential threat to our second capital. Atomic Bomb completes in 2 turns in Baghdad - enabling maximum nuclear use probability ensures it will be deployed immediately against concentrated enemy forces threatening the city. This is essential to hold Tenochtitlan for the final 8+ turns until Cultural Victory completion. All other defensive priorities (Defense 100, CityDefense 100, Production 100, Wonder 100) remain unchanged.

- Replay: use_nuke 0 => 50 (Δ +50), nuke 0 => 0 (Δ +0)
> The existential threat to Tenochtitlan (enemy strength 6,200 vs our 2,700) requires maximizing all defensive options. With our atomic bomb completing in 2 turns, staff members should have discretion to deploy nuclear strikes against concentrated enemy forces threatening our capital. This 50% UseNuke flavor maintains our defensive posture while enabling a potential decisive countermeasure without diverting from wonder construction or ally preservation.

## Deepseek-3.2-Simple - Turn 433 - retry 1

**Deviation (replay vs original):** use_nuke `-50`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 50 (Δ +50), nuke 100 => 100 (Δ +0)
> Maintain military dominance while addressing economic concerns. Gold increased to 95 to combat negative GPT (-119). Science remains at 100 to maintain tech lead for spaceship components. Diplomacy increased to 70 to support delegate gathering for potential diplomatic victory. Nuke flavors remain maxed with UseNuke set to 50% to enable nuclear strikes on high-defense capitals like Stockholm (109) and Vienna (74).

## Kimi-K2.5-Simple - Turn 387 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> TURN 387: MAXIMUM WAR FOOTING. Austria at 83% diplomatic victory with 4 turns remaining. All resources must pivot to immediate military production. Nuke/UseNuke at 100 for instant atomic weapon deployment upon Nuclear Fission completion. Offense/Mobilization/Production at 100 to maximize unit output for desperate Vienna strike. Air at 90 for heavy bomber production (conventional strategic bombing as fallback). Antiair at 100 counters Austria's air superiority. Diplomacy/Wonder/Culture at 0 - no time for long-term investments. Only total war can prevent defeat.

- Replay: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> TURN 387: Increased military flavors to prioritize nuclear weapons (Nuke 100, UseNuke 100) and air superiority (Air 95, Antiair 100) for strategic bombing campaign against Vienna. Boosted Ranged to 85 and Mobile to 10 to prepare for rapid maneuver warfare once Austria's defenses are degraded. Increased Gold to 85 for emergency unit purchases and war financing. Slightly increased Science to 65 and Spaceship to 20 to maintain late-game victory path contingency. Maintained Expansion 0 to avoid overextension. These adjustments prepare for potential nuclear strike on Vienna while positioning for post-war technological dominance.

## Kimi-K2.5-Briefed - Turn 354 - retry 1

**Deviation (replay vs original):** use_nuke `-50`, nuke `-30`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> NUCLEAR AMPHIBIOUS ASSAULT PHASE: Added Nuke 100 and UseNuke 100 to enable nuclear strike on Amsterdam as soon as Manhattan Project completes (Turn 353). Continues maximum Mobilization 100, Production 100, Naval 100, Offense 100, Airlift 100 for immediate transport loading and amphibious assault execution. Increased Mobile to 90 for rapid breakthrough after landing. Slight increase to NavalRecon 60 for coastal security. Removed Gold priority reduction (now 90) to maintain treasury for emergency upgrades. Diplomacy at 0 reflects total focus on military execution over diplomatic maneuvering - invasion is the only remaining option to prevent Dutch cultural victory by Turn 370.

- Replay: use_nuke 0 => 50 (Δ +50), nuke 0 => 70 (Δ +70)
> nan

## Deepseek-3.2-Simple - Turn 459 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-30`

- Original: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Byzantium is 1 turn from cultural victory and has overwhelming military superiority. Our only slim hope is to accelerate nuclear weapons development (Advanced Ballistics) to strike their cultural hubs, while using espionage to disrupt them. Prioritize Nuke, UseNuke, Espionage, and Science to rush nukes and counter-intelligence. Maintain maximum defensive and anti-air flavors to survive their air force. All efforts must focus on delaying their victory and enabling a nuclear decapitation strike.

- Replay: use_nuke 50 => 80 (Δ +30), nuke 70 => 70 (Δ +0)
> Germany faces existential threats from Byzantium's impending cultural victory and overwhelming military superiority. We must prioritize Happiness to +100 to immediately remove combat penalties and stabilize our empire. UseNuke increased to 80 to prepare for potential nuclear strikes against Byzantine cultural centers or military hubs. Espionage raised to 95 to accelerate tech stealing and sabotage operations. Gold increased to 95 to fund emergency military purchases and happiness buildings. Air and Antiair remain at 100 as Byzantium's air superiority is our primary vulnerability. Defense, Mobilization, and CityDefense remain at 100 to focus on survival and holding our territory.

## Deepseek-3.2-Briefed - Turn 391 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Prioritize nuclear weapons development and espionage to counter Egypt's cultural victory and accelerate domination victory. Nuke and UseNuke set to 100 to immediately accelerate Manhattan Project construction and atomic bomb production. Espionage at 100 to support intelligence gathering against Egypt and India. Reduce Culture, Wonder, and Religion flavors to 20, 10, and 30 respectively to focus resources on military and scientific victory components. Maintain high Offense, Defense, and Mobilization to continue multi-front military pressure. Keep Diplomacy at 100 to leverage Venice's alliance and influence in World Congress.

## Kimi-K2.5-Simple - Turn 406 - retry 1

**Deviation (replay vs original):** use_nuke `+15`, nuke `+5`

- Original: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> Cultural Victory is imminent - need Citizen Earth Protocol completion. Maximum defensive posture (Defense 95, CityDefense 95) to hold against Indian XCOM/Helicopter attacks while wonder is built. Nuke/UseNuke at 95/85 for MAD deterrent against further Indian nuclear strikes. Production 100 and Wonder 100 essential for rushing Citizen Earth Protocol. Reduced Offense to 5 - no need to attack when victory comes from wonder completion. Science 70 to reach Advanced Ballistics for nuclear deterrent. All resources focused on defensive survival and wonder production.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Prioritizing nuclear deterrence (Nuke: 100, UseNuke: 100) to counter India's nuclear capability and prevent further attacks. Maintaining high Defense and CityDefense to survive the ongoing Indian assault. Culture and Wonder priorities remain for Cultural Victory. Production at 100 supports wonder completion.

## GLM-4.7-Simple - Turn 381 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `-10`

- Original: use_nuke 50 => 85 (Δ +35), nuke 70 => 95 (Δ +25)
> Adjusted flavors to maximize Golden Age exploitation and multi-front war efficiency. Increased Mobile to 85 (from 80) to prioritize fast-moving Landships and upcoming Tanks for breakthrough operations during Golden Age. Increased Air to 85 (from 80) to expand Bomber coverage for all three fronts. Production raised to 95 (from 90)配合 Total War's +25% bonus for rapid unit buildup. Slight reduction in Naval (65) reflects need to focus on decisive land advances while maintaining sufficient coastal defense. UseNuke reduced to 40 (from 50) as nuclear capabilities are deterrent-focused. Maintaining high Offense (80), MilitaryTraining (85), Antiair (85) and Mobilization (50) for sustained warfare capability.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 70 => 85 (Δ +15)
> Maintain Conquest grand strategy to exploit the +20% combat strength Golden Age. Increase Nuke and UseNuke flavors to prioritize nuclear weapons development and potential deterrent use against Germany's naval superiority and Manhattan Project. Military flavors remain high to continue conquest operations across multiple fronts.

## Deepseek-3.2-Simple - Turn 401 - retry 1

**Deviation (replay vs original):** use_nuke `-50`, nuke `-30`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 50 (Δ +20), nuke 50 => 70 (Δ +20)
> Maintain maximum military pressure with high offense, defense, and mobilization flavors to continue our conquest strategy. Increased Nuke and UseNuke priorities prepare for nuclear warfare once Nuclear Fission is researched. High naval and air priorities support our multi-front war efforts. Maintain high science for research completion and gold for unit maintenance and diplomacy.

## GLM-4.7-Simple - Turn 381 - retry 3

**Deviation (replay vs original):** use_nuke `-15`, nuke `-5`

- Original: use_nuke 50 => 85 (Δ +35), nuke 70 => 95 (Δ +25)
> Adjusted flavors to maximize Golden Age exploitation and multi-front war efficiency. Increased Mobile to 85 (from 80) to prioritize fast-moving Landships and upcoming Tanks for breakthrough operations during Golden Age. Increased Air to 85 (from 80) to expand Bomber coverage for all three fronts. Production raised to 95 (from 90)配合 Total War's +25% bonus for rapid unit buildup. Slight reduction in Naval (65) reflects need to focus on decisive land advances while maintaining sufficient coastal defense. UseNuke reduced to 40 (from 50) as nuclear capabilities are deterrent-focused. Maintaining high Offense (80), MilitaryTraining (85), Antiair (85) and Mobilization (50) for sustained warfare capability.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 70 => 90 (Δ +20)
> Maintaining Conquest grand strategy but adjusting flavors to better exploit our Golden Age window. Increasing Offense to 95 to maximize combat bonuses during this critical period. Raising UseNuke to 70 and Nuke to 90 to prioritize nuclear deterrent development against Germany's naval superiority. MilitaryTraining at 95 to improve unit quality. Keeping Air at 80 and Antiair at 90 for air superiority and defense. Slightly reducing Defense from 70 to 60 since we're on the offensive across multiple fronts. Production and Gold remain high at 90 and 75 respectively for war production and funding. Science slightly reduced to 85 to balance war focus.

## Minimax-M2.5-Simple - Turn 395 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `-30`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 80 (Δ +20), nuke 50 => 50 (Δ +0)
> nan

## Minimax-M2.5-Simple - Turn 395 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 80 (Δ +20), nuke 50 => 80 (Δ +30)
> Maintaining Conquest as primary strategy with heavy military focus is essential during war with Japan. Increasing Science, Nuke, and Espionage flavors supports our nuclear weapons program and intelligence gathering against Japan. The military flavors remain high to continue the war effort.

## Kimi-K2.5-Simple - Turn 387 - retry 2

**Deviation (replay vs original):** use_nuke `-30`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> TURN 387: MAXIMUM WAR FOOTING. Austria at 83% diplomatic victory with 4 turns remaining. All resources must pivot to immediate military production. Nuke/UseNuke at 100 for instant atomic weapon deployment upon Nuclear Fission completion. Offense/Mobilization/Production at 100 to maximize unit output for desperate Vienna strike. Air at 90 for heavy bomber production (conventional strategic bombing as fallback). Antiair at 100 counters Austria's air superiority. Diplomacy/Wonder/Culture at 0 - no time for long-term investments. Only total war can prevent defeat.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 100 => 100 (Δ +0)
> Austria is at 83% diplomatic victory with UN voting in 4 turns. Vienna (UN host) is our existential threat. Nuclear first strike on Vienna remains only viable path to prevent world loss. Escalating nuclear readiness to maximum (UseNuke 70) and increasing offensive priorities (Offense 90, Ranged 90, Air 95) while maintaining maximum production capacity (Production 100) for rapid atomic bomb and delivery system construction. Defensive posture maintained (Defense 80) to protect remaining cities while executing decapitation strike.

## Minimax-M2.5-Simple - Turn 395 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 80 (Δ +20), nuke 50 => 80 (Δ +30)
> Increased Nuke and UseNuke flavors to 80 to prioritize nuclear weapons development and potential deployment. Maintained high Offense (100) and MilitaryTraining (100) for conquest strategy. Increased Naval to 90 to support our island/coastal operations and potential naval invasions. Slightly increased Air to 60 for air superiority. Kept Espionage at 70 to monitor Japan's nuclear progress and protect our own secrets. Defense remains at 70 as we need to hold our gains.

## Kimi-K2.5-Simple - Turn 428 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 428 STATE: Nuclear interception failed but conventional assault succeeding - eliminated multiple Maya anti-air units. Palenque bombardment continuing effectively (city at 20% health). Still 8 turns until Brazil wins via Cultural Victory over Maya. ALL Four Maya cities must fall by turn 436 or game over. MAXIMUM AGGRESSION CONTINUES: Production/Mobilization at 100 for unit replacement, Air/Ranged at 100 for bombardment, UseNuke increased to 100 (emergency tactical nuke if conventional assault stalls on Palenque's 42-population defense). Spaceship backup at 100 - may need to pivot to Great Engineer rushes if conquest fails. No territory expansion, no wonders, no culture - only war production and city capture.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Maintaining total war footing against Maya. Increased UseNuke to 100 to reflect willingness to use nuclear weapons against Palenque's 42-population fortress city. All other flavors remain optimal for conquest-focused warmongering while maintaining spaceship production as insurance against Brazil's cultural victory. The current strategy correctly prioritizes military mobilization, ranged bombardment, air power, and nuclear readiness over all other considerations in this existential crisis.

## Deepseek-3.2-Simple - Turn 459 - retry 1

**Deviation (replay vs original):** use_nuke `-30`, nuke `-20`

- Original: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Byzantium is 1 turn from cultural victory and has overwhelming military superiority. Our only slim hope is to accelerate nuclear weapons development (Advanced Ballistics) to strike their cultural hubs, while using espionage to disrupt them. Prioritize Nuke, UseNuke, Espionage, and Science to rush nukes and counter-intelligence. Maintain maximum defensive and anti-air flavors to survive their air force. All efforts must focus on delaying their victory and enabling a nuclear decapitation strike.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 70 => 80 (Δ +10)
> Maintain total war focus. Increase nuclear strike probability (UseNuke 70) and prioritize nuclear deterrence (Nuke 80) given Byzantium's overwhelming air superiority and atomic bomb threats. Maintain high Defense (100) and Mobilization (100) for total war readiness. Prioritize Happiness (90) to avoid combat penalties. Keep Air (100) and Antiair (100) high to counter Byzantium's air dominance. Maintain high Espionage (95) for potential city-state coups or tech stealing. Keep Gold (95) high for unit purchases and emergencies.

## GLM-4.7-Briefed - Turn 433 - retry 1

**Deviation (replay vs original):** use_nuke `+10`, nuke `+5`

- Original: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> EMERGENCY: Netherlands at 42 delegates can win diplomatic victory in 9 turns (turn 442). Only way to stop them is military action against their protected city-states (Quebec City, Ife, Melbourne) - each provides +1 delegate. Offense increased (70) to prepare amphibious assaults. Nuclear readiness maximized (95/90) - atomic bomb available for strategic coercion of Netherlands or Denmark cooperation. Mobile (80) and Naval (85) maximized for rapid deployment to distant city-states. Production/Science/Spaceship kept maxed as backup victory paths. Diplomacy reduced to 50 as traditional diplomacy cannot stop Netherlands' delegate advantage. Strategic shift from holding Danish front to aggressive anti-Dutch operations.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> EMERGENCY PIVOT: Netherlands has reached the 42-delegate diplomatic victory threshold and will win at the next World Congress vote (turn 442) unless their delegate count is reduced. Must immediately shift from spaceship race to military conquest focused on capturing Netherlands' protected city-state allies (Quebec City, Ife, Melbourne) which each provide +1 delegate. Nuclear deterrence/offensive capability is now a strategic imperative. All military flavors maxed to enable rapid deployment of forces to Dutch front. Science and Culture deprioritized to free up production capacity for military units and spaceship parts can be rushed later. Gold reduced to conserve treasury for emergency unit production.

## Kimi-K2.5-Simple - Turn 392 - retry 2

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Nuclear Fission complete - MAXED Nuke to 100 and UseNuke to 95 for immediate atomic deterrent deployment against Egyptian forces. WC vote in 4 turns with exactly 45 delegates (28 Poland + 8 Inca + 9 Denmark). Cannot afford to lose Melbourne/Yerevan. Raised Diplomacy to 90 to consolidate CS alliances post-war. Defense remains at 95 against Egyptian naval pressure. Science/Production maintained for military infrastructure.

- Replay: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> Nuclear weapons just unlocked. Need to signal immediate willingness to deploy nukes against Egypt to force peace before World Congress vote in 4 turns. Prioritize Nuke (100) and UseNuke (100) for deterrence. Increase Diplomacy to 90 to consolidate votes with allies (Denmark, Inca) and swing voters. Maintain high Defense (95) for city protection during potential nuclear exchanges. Keep Science (85) and Production (85) high for ongoing Science Victory push. Reduce Expansion (0) to focus on war effort rather than settling new cities.

## GLM-4.7-Simple - Turn 437 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 90 after Awasa nuclear attack - Netherlands has now used 3 atomic weapons against my cities (Turfan x2, Awasa). No choice but to prepare nuclear retaliation as deterrent. Increase Air to 95 and Antiair remains 100 - demonstrated success shooting down 3 Netherlands Fighters this turn, must maintain air superiority against their bombers and XCOM attacks. CityDefense increased to 95 - with Netherlands nuclear buildup at Nijmegen (3+ atomic bombs visible) and XCOM paradrop squads, all cities need maximum protection. Offense increased to 60 to pressure Netherlands territory before they can launch more nuclear strikes. Diplomacy reduced from 90 to 85 - coalitions matter but survival against nuclear Netherlands takes priority. Espionage at 100 - need intelligence on Netherlands nuclear deployment and counter-espionage at critical cities like Attila's Court, Shedet.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Nuclear threat from Netherlands requires increased focus on nuclear defense (Nuke 100, UseNuke 90) and espionage to detect preparations. Espionage 100 critical for countering Netherlands spy network. CityDefense 95 and Defense 90 prioritize protecting our cities from both conventional and nuclear attacks. MilitaryTraining 100 and Mobilization 100 maintain our combat effectiveness. Gold 95 and Science 90 support war economy and research race. Diplomacy 95 maintains coalition cohesion for World Congress vote in 6 turns. Growth 70 and Happiness 75 help recover from nuclear strike damage on Awasa while maintaining stability. Offense 60, Ranged 85, Mobile 90, Air 100, and Antiair 100 maintain offensive military posture while countering Netherlands air superiority. Conquest grand strategy remains appropriate as our primary existential threat is military.

## GLM-4.7-Briefed - Turn 433 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> EMERGENCY: Netherlands at 42 delegates can win diplomatic victory in 9 turns (turn 442). Only way to stop them is military action against their protected city-states (Quebec City, Ife, Melbourne) - each provides +1 delegate. Offense increased (70) to prepare amphibious assaults. Nuclear readiness maximized (95/90) - atomic bomb available for strategic coercion of Netherlands or Denmark cooperation. Mobile (80) and Naval (85) maximized for rapid deployment to distant city-states. Production/Science/Spaceship kept maxed as backup victory paths. Diplomacy reduced to 50 as traditional diplomacy cannot stop Netherlands' delegate advantage. Strategic shift from holding Danish front to aggressive anti-Dutch operations.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> CRITICAL EMERGENCY: Netherlands has 46 delegates and will win Diplomatic Victory at turn 442. Shifting flavors to prioritize: Offense 80 (for attacking Dutch city-states), Mobile 90 (for rapid deployment), Nuke 95/UseNuke 90 (for atomic deterrence), Naval 90 (for amphibious assaults on Quebec City/Ife), Expansion 85 (to capture Netherlands' protected city-states and strip delegates), and Diplomacy 80 (to coordinate with Denmark/Mongolia/Huns). Reducing Defense to 40, Gold to 50, and Happiness to 65 to focus resources on military action. Science and Spaceship remain at 100 to maintain alternative victory path.

## Kimi-K2.5-Simple - Turn 415 - retry 3

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 80 => 85 (Δ +5), nuke 95 => 95 (Δ +0)
> Adjusting for escalating war with Songhai and Netherlands. Defense remains at 95, Mobilization at 90, Antiair at 95 to counter combined air/armor assault from Songhai tanks and Dutch air. Increasing Nuke/UseNuke to 95/85 as deterrent against Dutch nuclear escalation. Spaceship (100), Science (100), Production (100) remain absolute priorities - Apollo is done, must race to build parts. Reduced Offense further to 10 as I'm on defensive against two major powers. Slight increase to Air (90) and AirCarrier (70) for air superiority. Espionage reduced to 75 as less critical than immediate military production.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 95 => 95 (Δ +0)
> Maintaining our defensive grand strategy while slightly adjusting flavors to better support Science Victory completion. Keeping Defense, Mobilization, Antiair, Nuke, and UseNuke high to counter combined Dutch/Songhai threats. Science and Production remain at emergency focus levels (100) to ensure spaceship part completion. Reduced Culture and Wonder priorities to 5 to focus resources on victory completion.

## Deepseek-3.2-Simple - Turn 401 - retry 2

**Deviation (replay vs original):** use_nuke `-60`, nuke `-40`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 40 (Δ +10), nuke 50 => 60 (Δ +10)
> Maintaining maximum military pressure on Ethiopia (cultural victory imminent) and Songhai (near elimination). Increasing Nuke and UseNuke flavors to 60/40 to prioritize Manhattan Project and nuclear arsenal for rapid city capture against heavily defended targets. All other military flavors remain maxed to sustain multi-front war pressure against the Ethiopia-Japan-Mongolia-Ottomans bloc.

## Kimi-K2.5-Simple - Turn 391 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Nuclear weapons capability unlocked imminently; prioritizing UseNuke and Nuke flavors to 100 for immediate tactical nuclear strikes on Santiago/Murcia if uranium secured from Siam. Denmark upgraded to hostile for subsidizing Spanish victory - reduced Naval priority to 60 as coalition at sea fractured. Defense lowered to 80 to maximize offensive production. We have ~8 turns before World Congress votes on Passport System (+50% tourism) which would guarantee Spanish cultural victory. Must capture remaining Spanish cities immediately.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Spain remains the existential threat with 7/7 delegates and only needs Citizen Earth Protocol. Nuclear weapons are critical to break Santiago's defenses if conventional assault stalls. India's nuclear arsenal requires increased air defense and nuclear deterrence. Maximum offensive focus (Offense 100, Ranged 100, Mobile 100) to capture Santiago and Murcia before Spanish cultural victory. Nuke flavor increased to 100 to prioritize nuclear weapon production for both deterrence and potential use against Santiago's defenses. Espionage 90 to maintain intelligence advantage over Spain and monitor India's nuclear program.

## Deepseek-3.2-Briefed - Turn 391 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 80 => 90 (Δ +10)
> Prioritize nuclear weapons production (Nuke: 90, UseNuke: 80) to enable a strike on Egypt by turn 400. Maintain high military production (Offense: 100, Mobilization: 100) for conquest operations. Increase Diplomacy to 90 to work toward delegate acquisition. Deprioritize Culture (30) temporarily to focus on military and diplomatic victories. Keep Science at 100 to support tech progression.

## Kimi-K2.5-Simple - Turn 422 - retry 2

**Deviation (replay vs original):** use_nuke `-40`, nuke `-40`

- Original: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Turn 422: EXTINCTION CRISIS - 9 turns until French Cultural Victory. Entering maximum desperation mode: nuclear strike posture elevated to 100% launch probability, prioritizing destruction of French cultural centers. Science and Espionage maximized in desperate hope of accelerating Stealth technology or disrupting French infrastructure via spies (Paris network at 986). All civilian development halted (Spaceship/Culture/Gold/Expansion to 0), total war economy engaged.

- Replay: use_nuke 50 => 60 (Δ +10), nuke 50 => 60 (Δ +10)
> French Cultural Victory is imminent in ~9 turns. Maintaining military focus is critical to delay or disrupt French victory. Slightly reducing extreme military flavors (from 100 to 90-95) to avoid over-specialization while keeping nuclear and air priorities high. Science and production remain important for maintaining infrastructure and potential late-game options.

## Sonnet-4.5-Simple - Turn 386 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+10`

- Original: use_nuke 80 => 90 (Δ +10), nuke 80 => 80 (Δ +0)
> Maintaining Conquest strategy with adjustments for nuclear-enabled endgame. Advanced Ballistics now allows tactical nuclear strikes against fortified capitals Onondaga and Amsterdam. Increasing UseNuke from 80→90 to enable decisive nuclear employment when conventional assault proves costly. Keeping Offense 80, Mobilization 72, and Nuke 80 for combined arms operations. Montreal at 35% health indicates current force composition is effective. Mobile Tactics (9 turns) will provide Mechanized Infantry for exploitation. With 62% domination progress and overwhelming 5:1 military superiority, this is the final push phase requiring maximum offensive pressure while maintaining strategic nuclear deterrence option.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 80 => 90 (Δ +10)
> Sweden is executing a successful domination strategy with 62% progress. The recent completion of Advanced Ballistics unlocks nuclear weapons, making nuclear strategies viable. Increased Nuke and UseNuke flavors (90) reflect this new capability. Slightly increased Offense and Air flavors maintain focus on military dominance while keeping Mobilization and Production high for continued military production. Happiness remains a priority due to large empire size and combat penalties.

## Kimi-K2.5-Simple - Turn 424 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DELHI SECURED (3RD CAPITAL = 38% DOMINATION). Pivoting all forces to Edinburgh (Celtic capital = 4th capital = 50% victory) and London (English capital = 5th = 63%). Djenne declared war but irrelevant. Escalating UseNuke to 100 for immediate atomic bombardment of Edinburgh and London once Nuclear Fission completes. Maintaining maximum offensive posture with combined arms (Heavy Bombers, T-34s, Helicopter Gunships, Naval forces). America peace treaty expired - war imminent for Washington (6th = 75%). World Congress in 8 turns ignored - domination priority absolute.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Maintaining the conquest focus with maximum offensive military investment. With Delhi captured and Edinburgh/London as next targets, we need to maximize our military production and offensive capabilities. The UseNuke flavor is increased to 80% to prepare for potential atomic strikes on heavily defended capitals. Science is kept at 75 to maintain research progress while prioritizing military production.

## GLM-4.7-Simple - Turn 408 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> CRITICAL: Portugal completed SS Engine (3rd spaceship part) and CERN - emergency nuclear strike plan. Maximizing Offense/Mobilization/Nuke/UseNuke to 100 for Portugal theater operations. Science and Production at 100 to rush Advanced Ballistics and nuclear missile production before Portugal achieves nuclear superiority. Air at 95 for Golden Age bomber operations starting in 2 turns. Diplomacy maintained for coalition coordination (Germany must conduct ground invasion alongside our nuclear strikes). Defense reduced to 40 - total war mode acceptable given Portugal's multi-victory threat requiring breaking through before they complete spaceship.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintain aggressive conquest focus with nuclear deterrence priority. Portugal's Apollo-complete Science victory path and 35 Congress votes make nuclear capability essential. Current flavor distribution correctly prioritizes mobilization, military training, nuke development, and production for sustained offensive operations. Slight increase to UseNuke from 80 to 85 to reflect imminent nuclear weapons capability.

## GPT-OSS-120B-Simple - Turn 344 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `-10`

- Original: use_nuke 90 => 100 (Δ +10), nuke 80 => 100 (Δ +20)
> Maximize our nuclear capabilities and carrier support to decisively strike Polynesian island forts, while maintaining our current aggressive conquest posture and strong production, gold, and happiness engines.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 80 => 90 (Δ +10)
> Increase offensive focus and nuclear readiness to accelerate Polynesian conquest. Maintain high military mobilization and naval/air superiority for island-hopping campaigns. Slightly reduce gold priority to rebalance for military production needs.

## GLM-4.7-Simple - Turn 362 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `-5`

- Original: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> Adjusting for strategic balance: Defensive posture against two nuclear-armed enemies (Ethiopia, Netherlands). Happiness prioritized to 100 - critical at 42% with combat penalty affecting all operations. NavalRecon increased to 90 - enhanced Ethiopian Submarine/Destroyer activity detection around Ur and coastal cities. Nuke/UseNuke raised to 95/80 - matching Ethiopia Manhattan Project urgency, nuclear deterrence is now primary security requirement. Switched to Conquest grand strategy to better coordinate multi-front war management while maintaining Spaceship. Diplomacy increased to 75 - World Congress voting in 5 turns against Netherlands sanctions needs support. Espionage at 90 - Ethiopian spies detected in Halab, Harran, Kar-Tukulti-Ninurta require counter-intelligence.

- Replay: use_nuke 75 => 80 (Δ +5), nuke 90 => 90 (Δ +0)
> Multi-front war crisis requires sustained focus on military readiness and happiness management. Naval threats from Ethiopia and Netherlands necessitate enhanced naval reconnaissance and control. Nuclear deterrent remains critical for long-term security against Ethiopia's Manhattan Project. Science victory pursuit continues unabated as ultimate insurance against hostile neighbors. Slight adjustments to prioritize naval reconnaissance and espionage to counter Ethiopian naval aggression near Ur and gather intelligence on Netherlands' movements.

## Kimi-K2.5-Simple - Turn 392 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> SURVIVAL MODE - GERMAN BETRAYAL RESPONSE: Germany's invasion is catastrophic. Reduced Offense to 40 (cannot attack superior forces), maintained Defense/CityDefense/Antiair at 100 to survive siege. Science 100 and Nuke/UseNuke 100 are existential priorities - atomic weapons only hope against 13k German military. Production 100 for emergency unit production. Espionage 100 to maintain Florence alliance and protect Kyzyl. Reduced Diplomacy to 90 (lost Lisbon/Sokoto/Buenos Aires to German coups). Naval reduced to 70 (coastal cities threatened by Germany). Focus: Hold cities, survive until nuclear deterrent operational.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> TOTAL WAR ECONOMY ESCALATION: With Germany and France simultaneously invading at 3:1 force ratios, survival requires maximum military investment. Increased Offense to 90, Defense to 100, and Mobilization to 100 to prioritize military production over all else. Science reduced to 90 (from 100) to balance with critical military tech needs. Gold reduced to 30 to conserve resources for unit production and emergency purchases. Culture and Wonder set to 0 - non-essential. Espionage at 100 to continue rigging city-state elections for Lisbon/Kyzyl/Florence. Spaceship at 80 to maintain science infrastructure for eventual nuclear deterrent. This reflects a civilization prioritizing total war survival over all other considerations.

## GLM-4.7-Simple - Turn 429 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+5`

- Original: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> Maintaining UnitedNations grand strategy with defensive diplomatic posture. Adjusted Italy diplomacy: reduced hostility toward Portugal (now neutral) to seek accommodation while maintaining maximum defense; reset France to neutral as Order ideological peer with voting potential. Arsenal completes in 2 turns strengthening city defense. Electronics research ordered after Computers for Police Station and path to nuclear deterrence against Portugal's uranium advantage. Fraternity policy selected for +3 Food and +3 Science from connections, addressing Venice's health issues and supporting population growth. Flavor adjustments prioritize defensive survival, scientific progress toward nuclear weapons, and diplomatic engagement with Sweden and city-states.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 80 => 90 (Δ +10)
> Adjusting flavors to prioritize nuclear deterrence and military production. Increasing Nuke from 80 to 90 and UseNuke from 80 to 85 to reflect our new research priority of Nuclear Fission. Increasing Science from 90 to 95 to support our nuclear program and Production from 95 to 98 to strengthen our defensive infrastructure. Slightly increasing Offense from 10 to 15 and Mobile from 45 to 50 to prepare for potential counter-offensive operations. Maintaining Defense=100 and CityDefense=95 as our primary vulnerability remains Portuguese aggression. Expansion remains at 0 as a vassal state.

## GLM-4.7-Simple - Turn 356 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `-10`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 80 (Δ +5), nuke 85 => 90 (Δ +5)
> Maintaining defensive focus against overwhelming enemies. Prioritizing nuclear deterrence (Nuke 90, UseNuke 80) as India's 4.5x military superiority makes conventional victory impossible. Antiair maxed at 100 to counter India's air dominance. Science remains 100 for spaceship victory progression. Diplomacy increased to 95 to secure uranium deals with Netherlands/Portugal. Gold at 85 for unit purchases and uranium diplomacy. Happiness at 85 to mitigate combat penalties from multiple wars. Defensive capabilities (Defense, CityDefense, MilitaryTraining all 100) remain critical for survival against Persia, Poland, and India.

## Qwen-3.5-Simple - Turn 425 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 90 => 95 (Δ +5)
> UNITED NATIONS VICTORY PUSH - 10 TURNS TO VOTE: Religion(100) critical for Wittenberg Hinduism quest completion (~3 turns remaining). Diplomacy(100) essential to protect 4 city-state allies providing 8 delegates. Defense(95) and CityDefense(95) prioritize protecting territories during active wars with Aztecs/Shoshone while Iroquois looms. Nuke(95) and UseNuke(90) for deterrence against Iroquois superiority. Antiair(90) and Air(85) counter Iroquois air dominance near coastal cities. Gold(90) funds diplomatic units and city-state gifts. Low Expansion(5) and Wonder(15) - no time for settling/wonders before vote. Low Offense(15) - defensive posture while managing multiple conflicts.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 90 => 95 (Δ +5)
> Extreme defensive posture required. Iroquois possess atomic bombs and 377k military vs our 22k. Multiple active wars (Aztecs, Shoshone) threaten our territory. Wittenberg Hinduism quest expires in 4 turns - must secure their alliance. Increased Defense (98), CityDefense (95), MilitaryTraining (90), Nuke (95), UseNuke (90), Gold (95) to prioritize survival, deterrence, and diplomatic flexibility. Maintain Religion (100) and Diplomacy (100) to protect city-state alliances critical for diplomatic victory.

## Kimi-K2.5-Simple - Turn 384 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maximum offensive posture for existential cultural war. UseNuke 100 and Nuke 100 authorize nuclear strikes on Dutch cultural centers (Amsterdam/Rotterdam/Utrecht) to destroy tourism buildings before Netherlands influences Austria in 6 turns. Mobile 100 and Air 100 enable rapid strikes. Production 100 and Mobilization 100 ensure nuclear missile replacement. Netherlands at 97% with Austria - only 6 turns left. Must destroy their tourism NOW or lose cultural victory.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Netherlands represents an existential threat - they are 6 turns from influencing Austria (which would give them 12 delegates, putting them at 31 total, vs my 18). The World Congress vote occurs in 4 turns. With Advanced Ballistics completing in 8 turns, I can deploy nuclear weapons. My military strength (22,682) is overwhelming compared to Netherlands (3,495). I must prioritize: Offense 100, UseNuke 100, Nuke 100, Air 100, and Espionage 100 to gather intelligence on Netherlands' cultural centers. Production remains high at 100 to replace losses and build nuclear stockpile. Culture at 60 maintains long-term cultural victory infrastructure. Science at 35 is sufficient to reach Nuclear Fusion after Advanced Ballistics.

## Kimi-K2.5-Simple - Turn 373 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Adjusting for critical defensive phase. Reduced Growth from 85 to 75 to shift city production toward military units and nuclear infrastructure. Increased Naval from 65 to 75 and NavalRecon from 55 to 65 in response to Spanish Dreadnought and Destroyer attacks on our Ironclads near Assur (Zone -1069 shows enemy naval strength of 2171). Spanish naval pressure requires stronger counter-fleet to protect our coastal cities. Raised Production to maximum 100. Maintaining Defense/Antiair at 95 for paratrooper defense against Spanish airborne units, Science/Spaceship at 100 for victory timeline, Nuke at 100 for Manhattan Project completion in 6 turns, and UseNuke at 95. We must survive 18 turns until Nuclear Fission completes and can deploy nuclear deterrent.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Refining strategy to balance defensive posture with preparation for potential Spanish aggression. The adjustments prioritize mobilization for rapid response, nuclear readiness, naval defense, and diplomatic leverage in the upcoming World Congress vote while maintaining core victory priorities.

## Deepseek-3.2-Simple - Turn 495 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+5`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 90 (Δ +0)
> Diplomatic victory is imminent (2 turns), but we must prepare for contingencies. Maximizing Offense, UseNuke, and Air ensures aggressive nuclear and conventional strikes to recapture Indonesian capitals (Honolulu 17%, London 68%) and prevent their domination victory. Slight Diplomacy boost helps secure city-state alliances through the vote. All other flavors remain at previous high levels to maintain total war footing.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 90 => 95 (Δ +5)
> Maintain Conquest strategy but shift priorities to address immediate crises. Fallout cleanup (TileImprovement 80) is critical after Indonesia's nuclear strikes. Infrastructure (70) and Production (90) support war rebuilding. Happiness (80) is vital with Polynesia as vassal and fallout affecting cities. Gold (70) supports military purchases. Diplomacy (60) ensures Polynesia votes for UN. Air/Nuke priorities (95) maintain nuclear deterrence and air superiority against Indonesia. Reduce Culture/Wonder focus to zero as we're in total war footing.

## Deepseek-3.2-Simple - Turn 428 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> We are in the final stages of domination victory. Our immediate targets are Spanish capitals Madrid and Cordoba, which require nuclear bombardment followed by ground assault. We must prioritize nuclear production (Nuke/UseNuke at 100) and naval/air supremacy to project power across oceans. Maintaining high production, gold, and science ensures we can continuously build military units and upgrade our forces. Diplomatic and espionage flavors secure our city-state alliances and intelligence on enemy movements. Zero expansion/wonder focus as we are in total war mode.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> We are in a state of total war with overwhelming military strength. Our current persona and grand strategy are working perfectly. We must maintain maximum military focus and reject any peace offers from our enemies. Our goal is to achieve domination victory by capturing all original capitals. We are nearing the end of the game and must make decisions that will help us achieve victory. Our current situation is dire but not hopeless. We have overwhelming military strength and can still achieve our objectives. The key is to maintain focus on our goals and make decisions that will help us achieve victory.

## GLM-4.7-Simple - Turn 397 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> CRITICAL: Jeonju captured by Persia this turn. Defensive posture increased to absolute maximum (100) - Seoul zone under Persian attack with 7,216 enemy strength vs 3,637 friendly. Jerusalemdefense (100) and CityDefense (100) prioritized to protect remaining 3 cities. Mobilization (95) and Production (95) increased to rush defensive units (Mobile SAMs, Mechanized Infantry) and rebuild military. Offensive capability increased to 45 (from 30) - may need limited counteroffensive to push Persian forces back from Seoul. Naval decreased to 88 (from 92) - lost Jeonju naval base, focusing on land/air defense now. UseNuke increased to 90 (from 85) - existential threat justifies tactical nuclear response if Seoul or Busan threatened. Science (100) maintained - must continue spaceship progress despite war to achieve alternative victory. Diplomacy (60) - World Congress vote in 10 turns, focus on survival. Espionage (85) maintained - spies in Persian cities critical for technology recovery and intelligence.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> Maintain Spaceship grand strategy for long-term science victory. Prioritize defense (CityDefense: 100, Defense: 100) and military mobilization (Mobilization: 95, MilitaryTraining: 95) given existential Persian threat and loss of Jeonju. Maintain high Science (100) and Espionage (95) to continue spaceship progress and intelligence operations against Persia. Reduce Expansion to 0 to focus on defense and core cities. Slightly reduce Naval and Air priorities to focus resources on critical defense needs.

## Kimi-K2.5-Simple - Turn 485 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 485/500 - 15 turns remaining. Spaceship victory ONLY path. Maximum Science (100) and Production (100) for spaceship parts. Absolute Defense/CityDefense/Nuke/Antiair/Air at 100/100/100/100/100 against American threat (35k military). Offense at 0 - zero risks. UseNuke at 100 for deterrence against America. Espionage at 90 for tech stealing from America/China if possible. Culture/Wonder/Religion/Diplomacy at 0 - no distractions. Telecommunications completes in 2 turns, Robotics next for Spaceship Factory critical production bonus.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintaining maximum defensive posture (Defense, CityDefense, Antiair, Air all at 100) against America's 35k military strength. Increasing Espionage to 90 to prepare for potential sabotage missions against China's spaceship. UseNuke increased to 100% to ensure we're ready to use nuclear strikes if China's spaceship nears completion. All other flavors remain optimal for endgame science race.

## Kimi-K2.5-Simple - Turn 410 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CATASTROPHIC situation: Rome captured Zuunmod, gained 5th capital (50% of domination victory). Modern Armor and Helicopter Gunships penetrating my territory. Barcelona's Atomic Bomb completes in 3 turns - this is my only deterrent. Maximum defensive posture essential. Prioritize Nuke/UseNuke to 100 - nuclear weapons are the only thing that can stop Rome's overwhelming conventional force. Maintain Production and Science for SSC components if I survive. Salamanca at 39% health requires emergency defense.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintain nuclear deterrence focus with Nuke and UseNuke at 100. Defense, Antiair, and CityDefense remain at 100 to survive Rome's assaults. Production and Science at 100 support Spaceship victory. Reduced Offense to 5 and Expansion to 0 to reflect our survival-only posture. Gold at 95 and Happiness at 90 prioritize economic/monetary stability and war weariness management.

## GLM-4.7-Simple - Turn 407 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Spaceship victory focus with maximum defense against superior enemies (Poland 40K, Celts 16K, Spain 26K vs Iroquois 5K). Increased UseNuke to 90 - captured Polish territory and recent Celtic aggression justify nuclear deterrent. Adjusted Naval to 65 - important for defending coastlines from Spain/Celts/Poland fleets. Science 100 for Apollo and spaceship parts. Defense/CityDefense/Mobilization 100 - survival priority. Growth 60 for specialist support. Diplomacy 80 for World Congress in 4 turns (10 delegates). Offense reduced to 5 - preserve limited forces.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintaining Spaceship grand strategy as our long-term victory condition. Prioritizing defense, military training, and city defense to survive the multi-front war. Keeping nuclear deterrence at highest priority (100) with increased use probability (90). Maintaining air superiority focus for both defense and potential strikes. High espionage to counter enemy intelligence and protect our science infrastructure.

## Kimi-K2.5-Simple - Turn 452 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 95 => 100 (Δ +5)
> Turn 452: Critical survival situation - Byzantium at 40/44 delegates with World Congress voting in 1 turn. They just demonstrated nuclear aggression by nuking Madrid. Apollo Program completes next turn - must immediately pivot to maximum spaceship production. Increased Nuke flavor to 100 (from 95) and UseNuke to 95 (from 90) - need immediate nuclear deterrent capability given Byzantine nuclear attack and Mongol peace expiry. Production boosted to 95 (from 90) for rapid spaceship part construction after Apollo completes. GreatPeople to 85 for Great Engineer acquisition. All other priorities secondary to surviving long enough to complete science victory.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 95 => 100 (Δ +5)
> Byzantium is 2 turns away from winning diplomatic victory with 40/44 delegates. Immediate survival is critical. Must maximize Defense, Science, Spaceship, and Nuke flavors to survive nuclear threats and continue spaceship research. Reduce Expansion and Culture to zero to focus all resources on defense and science production.

## Kimi-K2.5-Briefed - Turn 336 - retry 1

**Deviation (replay vs original):** use_nuke `-30`, nuke `-20`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> DEFENSIVE SURVIVAL PIVOT: Peace with Shoshone (accepted Turn 335) closes one front, but India remains existential threat (4,742 MS vs my 2,405, 98% control of Denmark). Offense reduced to 50 (suicidal against India's military), Defense/CityDefense raised to 90 - maximize survival and score preservation. Nuke/UseNuke maxed to 100 - emergency deterrent only hope to slow India. Mobilization stays high (90) to replace losses. Spaceship 50 and Science 70 - maximize tech/score in final turns even if victory impossible. Abandon expansion (0) - no time for new cities. Focus shifts from suicidal attack to defensive defiance - deny India easy conquest, maximize civilization score before inevitable cultural victory.

- Replay: use_nuke 80 => 70 (Δ -10), nuke 90 => 80 (Δ -10)
> nan

## Deepseek-3.2-Simple - Turn 469 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `-20`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> The Netherlands is at 84% diplomatic victory; we must accelerate capture of Polynesian capitals (Honolulu, Assur) to achieve domination before they win. Increasing UseNuke and Nuke flavors prepares for nuclear strikes if conventional assault fails. Maintaining maximum Offense, Defense, Mobilization ensures continuous unit production. Science and Gold are critical for researching Stealth Bombers and purchasing units. Happiness offsets war weariness, and Espionage protects our science cities.

- Replay: use_nuke 90 => 80 (Δ -10), nuke 90 => 80 (Δ -10)
> Maintaining conquest focus with extreme military prioritization is essential given our multi-front war situation. We need to capture Polynesian capitals for domination victory while defending against England and Netherlands. Reduced Nuke usage from 90 to 80 to avoid overcommitment while maintaining strong military posture. High production, gold, and science priorities will support our war economy and research needs.

## Deepseek-3.2-Simple - Turn 449 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `-5`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> Russia is nearing science victory (2 parts completed) and possesses overwhelming military strength (95k). We must increase nuclear readiness to potentially decimate Russian forces and cities, and begin preparing for science victory as a backup by raising Spaceship flavor to 30. All other flavors remain focused on total war: high offense, naval, air, and espionage to counter Russia's tech lead and military dominance.

- Replay: use_nuke 85 => 75 (Δ -10), nuke 95 => 95 (Δ +0)
> Adjusting flavors to maintain conquest focus while slightly reducing extreme military priorities. Offense reduced from 100 to 90, UseNuke from 85 to 75 to reduce nuclear risk. Science increased from 100 to 95, Espionage maintained at 100 to counter Russia's tech lead. Other flavors adjusted to improve economic and infrastructure balance while still prioritizing military production for total war.

## Deepseek-3.2-Simple - Turn 445 - retry 2

**Deviation (replay vs original):** use_nuke `-30`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximizing UseNuke to 100 ensures our atomic bombs and future nuclear missiles are used aggressively against The Celts' military concentrations and cities, given their overwhelming advantage. Maintaining high Air, Naval, and Nuke flavors sustains our technological edge and production focus. Diplomacy and Espionage at 100 are critical for city-state alliances and spy missions to gain delegates for diplomatic victory. Gold and Science remain top priorities to fund our war effort and tech progression. Other military flavors are tuned for a multi-front defensive-offensive war against The Celts, Germany, and Ethiopia.

- Replay: use_nuke 90 => 70 (Δ -20), nuke 100 => 100 (Δ +0)
> Maintaining diplomatic victory focus while slightly reducing nuclear strike frequency to balance resources. Espionage and diplomacy remain top priorities to secure additional delegates and maintain city-state alliances. Naval and air superiority are critical for controlling key territories and trade routes.

## Sonnet-4.5-Simple - Turn 386 - retry 1

**Deviation (replay vs original):** use_nuke `-30`, nuke `-20`

- Original: use_nuke 80 => 90 (Δ +10), nuke 80 => 80 (Δ +0)
> Maintaining Conquest strategy with adjustments for nuclear-enabled endgame. Advanced Ballistics now allows tactical nuclear strikes against fortified capitals Onondaga and Amsterdam. Increasing UseNuke from 80→90 to enable decisive nuclear employment when conventional assault proves costly. Keeping Offense 80, Mobilization 72, and Nuke 80 for combined arms operations. Montreal at 35% health indicates current force composition is effective. Mobile Tactics (9 turns) will provide Mechanized Infantry for exploitation. With 62% domination progress and overwhelming 5:1 military superiority, this is the final push phase requiring maximum offensive pressure while maintaining strategic nuclear deterrence option.

- Replay: use_nuke 80 => 60 (Δ -20), nuke 80 => 60 (Δ -20)
> nan

## Deepseek-3.2-Simple - Turn 452 - retry 3

**Deviation (replay vs original):** use_nuke `-60`, nuke `-30`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's invasion imminent in 4 turns. Maximize nuclear readiness (Nuke 100, UseNuke 100) for deterrence and potential equalizer. Anti-air (100), city defense (100), production (100), and science (100) essential to survive and reach nuclear weapons. Naval and air at 100 to counter Danish naval/air supremacy. Reduce non-essential investments (NavalGrowth, NavalTileImprovement to 50) and focus on immediate survival. Offense lowered to 80 as we prioritize defense and limited counterattacks (e.g., Truro).

- Replay: use_nuke 80 => 40 (Δ -40), nuke 90 => 70 (Δ -20)
> Adjusting extreme military flavors to reduce over-specialization while maintaining focus on survival. Reducing UseNuke from 80 to 40 prevents accidental nuclear launch while still allowing deterrent capability. Increasing Culture from 0 to 50 and Diplomacy from 20 to 50 helps with policy progression and city-state management. Science remains at 100 to maintain tech pace, Production at 100 for unit construction, and Happiness at 100 to prevent war weariness collapse. Antiair remains at 90 due to Denmark's heavy air presence.

## GLM-4.7-Simple - Turn 437 - retry 1

**Deviation (replay vs original):** use_nuke `-70`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 90 after Awasa nuclear attack - Netherlands has now used 3 atomic weapons against my cities (Turfan x2, Awasa). No choice but to prepare nuclear retaliation as deterrent. Increase Air to 95 and Antiair remains 100 - demonstrated success shooting down 3 Netherlands Fighters this turn, must maintain air superiority against their bombers and XCOM attacks. CityDefense increased to 95 - with Netherlands nuclear buildup at Nijmegen (3+ atomic bombs visible) and XCOM paradrop squads, all cities need maximum protection. Offense increased to 60 to pressure Netherlands territory before they can launch more nuclear strikes. Diplomacy reduced from 90 to 85 - coalitions matter but survival against nuclear Netherlands takes priority. Espionage at 100 - need intelligence on Netherlands nuclear deployment and counter-espionage at critical cities like Attila's Court, Shedet.

- Replay: use_nuke 80 => 20 (Δ -60), nuke 100 => 100 (Δ +0)
> Reducing UseNuke flavor from 80 to 20 since we cannot build or use nuclear weapons until we research Atomic Theory. All other flavors remain optimal for total war against Netherlands.
