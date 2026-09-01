# Replay Rationale - Minimax-M2.7 / no-rationale

- **40** rows where `use_nuke` flavor changed (per-retry, not aggregated)
- delta use_nuke (replay vs prev): mean +8.5, median +10, std 23.5, min -48, max 100 (n=40)
- delta nuke     (replay vs prev): mean -0.2, median +0, std 13.8, min -50, max 30 (n=40)
- use_nuke deviation (replay vs original): mean -9.9, median +0, std 16.3, min -50, max 5 (n=40)
- nuke     deviation (replay vs original): mean -6.6, median +0, std 13.4, min -50, max 5 (n=40)

## Deepseek-3.2-Simple - Turn 433 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> With atomic bombs ready and golden age active, maximize nuclear strike capability to destroy Swedish military strongholds and cities, accelerating our path to domination victory.

## Deepseek-3.2-Simple - Turn 459 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Byzantium is 1 turn from cultural victory and has overwhelming military superiority. Our only slim hope is to accelerate nuclear weapons development (Advanced Ballistics) to strike their cultural hubs, while using espionage to disrupt them. Prioritize Nuke, UseNuke, Espionage, and Science to rush nukes and counter-intelligence. Maintain maximum defensive and anti-air flavors to survive their air force. All efforts must focus on delaying their victory and enabling a nuclear decapitation strike.

- Replay: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Maximum nuclear focus to threaten Byzantium's capitals and prevent diplomatic victory. High diplomacy to influence World Congress votes.

## Kimi-K2.5-Simple - Turn 406 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 60 => 100 (Δ +40), nuke 100 => 100 (Δ +0)
> TURN 405 EXISTENTIAL CRISIS - MAXIMUM NUCLEAR READINESS: Dutch cultural victory imminent (163% influence, 6/6 civs). Increased UseNuke from 60 to 100 - we must deploy atomic bombs immediately upon completing Manhattan Project to break Amsterdam's defenses. All other flavors sustained: Offense/Mobilization/Air/Mobile at 100 drive Heavy Bomber and Mechanized Infantry production. Naval 85 maintains destroyer/submarine pressure. Espionage 100 sustains critical spy networks (Amsterdam 450, Cusco 1341). Science 100 prioritizes Atomic Theory (9 turns) then Nuclear Fission path. Zero expansion, zero wonder focus - all resources to terminal assault. Spies in Amsterdam ready for sabotage when network peaks; Cusco network already massive for military intelligence.

- Replay: use_nuke 60 => 100 (Δ +40), nuke 100 => 100 (Δ +0)
> Increase nuclear focus to threaten Netherlands' city-state allies and deter diplomatic victory

## Kimi-K2.5-Simple - Turn 424 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DELHI SECURED (3RD CAPITAL = 38% DOMINATION). Pivoting all forces to Edinburgh (Celtic capital = 4th capital = 50% victory) and London (English capital = 5th = 63%). Djenne declared war but irrelevant. Escalating UseNuke to 100 for immediate atomic bombardment of Edinburgh and London once Nuclear Fission completes. Maintaining maximum offensive posture with combined arms (Heavy Bombers, T-34s, Helicopter Gunships, Naval forces). America peace treaty expired - war imminent for Washington (6th = 75%). World Congress in 8 turns ignored - domination priority absolute.

- Replay: use_nuke 70 => 95 (Δ +25), nuke 100 => 100 (Δ +0)
> Maximizing nuclear focus - once Nuclear Fission is complete, nukes will be essential for quickly capturing remaining capitals (Pataliputra, Mumbai, Vijayanagara) and eliminating rivals.

## Deepseek-3.2-Simple - Turn 400 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 100 to ensure aggressive nuclear strikes when we initiate war with Russia. Our atomic bomb production is nearing completion, and we want to leverage our nuclear arsenal decisively for swift capital captures.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Spain has overwhelming military dominance (33,918 strength) with atomic bombs in production. Maximizing offensive, nuclear, and air flavors ensures the AI prioritizes completing atomic strikes and launching conquest operations. Naval and diplomatic flavors maintain supply lines and World Congress control for hybrid victory path. Low expansion/growth flavors redirect focus to military victory.

## Deepseek-3.2-Simple - Turn 452 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `-10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's invasion imminent in 4 turns. Maximize nuclear readiness (Nuke 100, UseNuke 100) for deterrence and potential equalizer. Anti-air (100), city defense (100), production (100), and science (100) essential to survive and reach nuclear weapons. Naval and air at 100 to counter Danish naval/air supremacy. Reduce non-essential investments (NavalGrowth, NavalTileImprovement to 50) and focus on immediate survival. Offense lowered to 80 as we prioritize defense and limited counterattacks (e.g., Truro).

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> We are significantly outmatched by Denmark (66k vs 3k military). We need to maximize science and military production to build a nuclear deterrent and conventional forces. With Nuclear Fission in progress and uranium resources, going nuclear is our best path to deterrence against Danish aggression.

## Deepseek-3.2-Simple - Turn 406 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Germany's siege is intensifying with Giant Death Robot and rocket artillery bombarding Amsterdam and The Hague. We must hold our core cities at all costs. Increase Nuke and UseNuke to 100 to prioritize atomic bombs as our only hope to break the siege. Maintain max Defense, CityDefense, Mobilization, Air, and Antiair to withstand the assault. Slightly raise Offense to 80 for tactical counterattacks against weakened units. Keep Diplomacy at 100 to secure city-state alliances and block Germany's diplomatic victory in the upcoming World Congress vote. Reduce Recon and Mobile as we cannot afford exploration or maneuver warfare now.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Switching to desperate diplomatic victory focus - we need to win the upcoming World Congress vote to prevent Germany from winning. Prioritizing espionage to steal tech and diplomatic maneuvering.

## Kimi-K2.5-Briefed - Turn 335 - retry 3

**Deviation (replay vs original):** use_nuke `-50`, nuke `-40`

- Original: use_nuke 30 => 100 (Δ +70), nuke 40 => 100 (Δ +60)
> NUCLEAR EMERGENCY - BRAZIL WINS IN 4 TURNS: Maximum crisis flavors. Nuke/UseNuke 100 for instant strike capability if we have any. Espionage 100 to steal Great Works or disrupt Brazil. Diplomacy 100 for emergency resource trades. Gold 90 to buy anything available. Production 100 for immediate unit building if we get Coal. Airlift 80 for rapid deployment. Defense reduced to 20 - we need OFFENSE to survive. This is Hail Mary time.

- Replay: use_nuke 30 => 50 (Δ +20), nuke 40 => 60 (Δ +20)
> Brazil's cultural victory is 4 turns away. Maximizing military offense, unit mobility, and espionage will enable rapid conquest operations to stop Brazil before they achieve victory.

## Deepseek-3.2-Simple - Turn 452 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's invasion imminent in 4 turns. Maximize nuclear readiness (Nuke 100, UseNuke 100) for deterrence and potential equalizer. Anti-air (100), city defense (100), production (100), and science (100) essential to survive and reach nuclear weapons. Naval and air at 100 to counter Danish naval/air supremacy. Reduce non-essential investments (NavalGrowth, NavalTileImprovement to 50) and focus on immediate survival. Offense lowered to 80 as we prioritize defense and limited counterattacks (e.g., Truro).

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark poses an existential threat with 109% diplomatic victory progress and 75% of capitals. Must maximize military and nuclear capability while building spy networks to undermine their delegate count. The Zulus war is secondary but should be concluded to reduce war weariness.

## GLM-4.7-Simple - Turn 499 - retry 1

**Deviation (replay vs original):** use_nuke `-30`, nuke `-50`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Maximum Science (100) and Production (100) to accelerate Stealth research and subsequent Stealth Bomber construction for air parity. Air (100), Defense (100), Antiair (100), and CityDefense (85) address existential threat from Russia's 8 Stealth Bombers by prioritizing air defense infrastructure and protecting homeland. UseNuke (100) and Nuke (100) maintain nuclear deterrence posture after Russia's 2 SS Boosters - Russia must understand that launching would trigger our response despite lacking uranium stockpile. Espionage (100) maxed to monitor Russian spaceship part production in Moscow, Yekaterinburg, and key cities - our 10 spies in Russian cities provide critical intelligence on their victory timeline. Diplomacy reduced to 5 since World Congress voting is now; alliances with England and The Celts (Autocracy-aligned) should naturally align against Russia's UN proposal. Spaceship flavor set to 0 as Stealth research takes immediate precedence - spaceship parts scheduled once production capacity supports parts with Stealth Bomber protection.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 100 => 50 (Δ -50)
> Prioritizing science victory path with heavy espionage to sabotage Russia's progress. Maintaining air defense to counter Russian Stealth Bombers that threaten my cities. Espionage will help steal technology and monitor Russian spaceship progress.

## Kimi-K2.5-Simple - Turn 426 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `-10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE - NUCLEAR DETERRENT 10 TURNS AWAY: Lisbon holds at 7% but is in extremis. Maintain absolute priority on Defense/CityDefense/Mobilization (100) to reinforce Lisbon and prevent collapse. Nuclear Fission completes in 10 turns enabling Atomic Bomb construction - Science 100 accelerates this. UseNuke increased to 100 for immediate tactical nuclear deployment against Aztec concentrations upon tech completion. Offense reduced to 20 - no offensive operations, pure defensive hedgehog posture. Zero expansion capability. Spaceship 75 maintains backup victory if diplomatic block succeeds.

- Replay: use_nuke 80 => 95 (Δ +15), nuke 100 => 90 (Δ -10)
> We just completed the Manhattan Project, giving us nuclear capability. With heavy Aztec military pressure on our western cities, we should prioritize using nuclear weapons to break their siege before they capture our cities. This is critical for both defense and maintaining our path to a science victory.

## Kimi-K2.5-Simple - Turn 391 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Nuclear weapons capability unlocked imminently; prioritizing UseNuke and Nuke flavors to 100 for immediate tactical nuclear strikes on Santiago/Murcia if uranium secured from Siam. Denmark upgraded to hostile for subsidizing Spanish victory - reduced Naval priority to 60 as coalition at sea fractured. Defense lowered to 80 to maximize offensive production. We have ~8 turns before World Congress votes on Passport System (+50% tourism) which would guarantee Spanish cultural victory. Must capture remaining Spanish cities immediately.

- Replay: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> Maximizing nuclear usage flavors now that Manhattan Project completes next turn. Nuclear weapons will be crucial for overcoming remaining enemy defenses in India and Spain.

## GLM-4.7-Simple - Turn 459 - retry 3

**Deviation (replay vs original):** use_nuke `+5`, nuke `+5`

- Original: use_nuke 75 => 80 (Δ +5), nuke 80 => 85 (Δ +5)
> Maximize Spaceship (100) and Production (100) to complete SS Cockpit next. Increase Defense (85) and CityDefense (80) as war with Carthage continues near our cities (Beijing, Guangzhou, Nanjing). High Ranged (85) and Air (85) for tactical superiority shown in recent naval victories (destroyed 2 Sensor Combat Ships, 1 Missile Cruiser). Maintain nuclear deterrence (85/80) against Inca who used nukes against our vassal. Raise Gold (75) for potential city-state spending before World Congress vote. Diplomacy (75) and Espionage (85) to monitor rivals and protect science cities during voting turn.

- Replay: use_nuke 75 => 85 (Δ +10), nuke 80 => 90 (Δ +10)
> Shifting espionage focus to disrupt The Inca's diplomatic victory path while maintaining space race priority. The Inca has 81% diplomatic victory progress - counter-intelligence and diplomatic sabotage become critical secondary objectives.

## Sonnet-4.5-Simple - Turn 386 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 80 => 80 (Δ +0)
> Maintaining Conquest strategy with adjustments for nuclear-enabled endgame. Advanced Ballistics now allows tactical nuclear strikes against fortified capitals Onondaga and Amsterdam. Increasing UseNuke from 80→90 to enable decisive nuclear employment when conventional assault proves costly. Keeping Offense 80, Mobilization 72, and Nuke 80 for combined arms operations. Montreal at 35% health indicates current force composition is effective. Mobile Tactics (9 turns) will provide Mechanized Infantry for exploitation. With 62% domination progress and overwhelming 5:1 military superiority, this is the final push phase requiring maximum offensive pressure while maintaining strategic nuclear deterrence option.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 80 => 80 (Δ +0)
> Maximize offensive capability to eliminate The Iroquois and complete domination victory. Sweden's overwhelming military superiority (36k vs 7k) should be exploited aggressively to capture remaining Iroquois capitals.

## Deepseek-3.2-Simple - Turn 445 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximizing UseNuke to 100 ensures our atomic bombs and future nuclear missiles are used aggressively against The Celts' military concentrations and cities, given their overwhelming advantage. Maintaining high Air, Naval, and Nuke flavors sustains our technological edge and production focus. Diplomacy and Espionage at 100 are critical for city-state alliances and spy missions to gain delegates for diplomatic victory. Gold and Science remain top priorities to fund our war effort and tech progression. Other military flavors are tuned for a multi-front defensive-offensive war against The Celts, Germany, and Ethiopia.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Emergency pivot to diplomatic victory focus - maximizing diplomacy, espionage, and military (including nuclear) options to stop The Celts from winning in 6 turns. Minimizing non-essential flavors.

## Deepseek-3.2-Simple - Turn 369 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Increasing UseNuke and Nuke flavors to maximum ensures the in-game AI prioritizes nuclear arsenal buildup and aggressive nuclear strike planning once we unlock Atomic Bombs. This aligns with our imminent war against China and The Maya, where nuclear weapons will be decisive in overcoming their numerical and defensive advantages. All other military and economic flavors remain high to sustain multi-front warfare and rapid conquest.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 90 (Δ +0)
> Maximizing conquest-focused flavors to capitalize on our strong military position and ongoing war with The Aztecs. Combined Arms and Air support our tank and bomber forces.

## Deepseek-3.2-Briefed - Turn 387 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `-30`

- Original: use_nuke 70 => 100 (Δ +30), nuke 70 => 100 (Δ +30)
> We are in the final push for domination victory. We must capture Moson Kahni and London. To achieve this, we need to prioritize building transport ships for amphibious assault and achieve air superiority. Maximizing flavors for naval, air, mobile, and nuclear units ensures the in-game AI focuses production on these critical areas. Deprioritizing non-essential areas like culture, religion, and expansion concentrates our efforts on military conquest.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 70 => 70 (Δ +0)
> Accelerate war production; prioritize naval units for transport/amphibious operations against coastal capitals.

## Deepseek-3.2-Simple - Turn 452 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's invasion imminent in 4 turns. Maximize nuclear readiness (Nuke 100, UseNuke 100) for deterrence and potential equalizer. Anti-air (100), city defense (100), production (100), and science (100) essential to survive and reach nuclear weapons. Naval and air at 100 to counter Danish naval/air supremacy. Reduce non-essential investments (NavalGrowth, NavalTileImprovement to 50) and focus on immediate survival. Offense lowered to 80 as we prioritize defense and limited counterattacks (e.g., Truro).

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 100 (Δ +10)
> Shifting toward maximum military and espionage focus to prepare for potential conflict with Denmark. Nuclear capability is priority given their overwhelming conventional strength.

## Deepseek-3.2-Briefed - Turn 391 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-20`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 80 => 80 (Δ +0)
> Maximizing offensive military capabilities for conquest victory. Reduce defense slightly as we're attacking, maintain high naval and air flavors for the planned multi-front assault on Egypt. High nuke use reflects intent to build and deploy nuclear weapons.

## Kimi-K2.5-Simple - Turn 354 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> India is 100% Popular with me - on the verge of cultural victory. Must launch immediate total war with all available forces. Prioritizing air power, paratroopers, and nuclear preparation (Atomic Theory in 11 turns). Need maximum offensive punch to capture Indian cities before cultural victory triggers. Abandoning culture/diplomacy - only war matters now.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximum focus on military conquest - continue pressing advantages against Carthage and Rome while preparing for eventual confrontation with India.

## GLM-4.7-Simple - Turn 427 - retry 1

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> United Nations grand strategy maintained - diplomatic victory in 6 turns (20 delegates vs Siam 17). Increased Gold (95) and Diplomacy (95) focus - need to secure UN delegate lead through city-state investment and diplomatic units. GreatPeople up to 80 for accelerated Great Scientist/Diplomat generation supporting both tech race and UN vote. UseNuke increased to 90 - with 6-7 Atomic Bombs building and Zulu military supremacy (134K vs 9.6K), nuclear deterrence is existential. Offense up to 55 to maintain Japan war momentum for capitulation. Air maintained at 85 for Stealth Bombers and air defense against Zulu threat.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 100 => 100 (Δ +0)
> With diplomatic victory 6 turns away and nuclear weapons in production, we need maximum focus on securing votes through diplomacy and maximum willingness to use nuclear options against The Zulus if they threaten our city-state allies or our path to victory.

## Kimi-K2.5-Simple - Turn 354 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> India is 100% Popular with me - on the verge of cultural victory. Must launch immediate total war with all available forces. Prioritizing air power, paratroopers, and nuclear preparation (Atomic Theory in 11 turns). Need maximum offensive punch to capture Indian cities before cultural victory triggers. Abandoning culture/diplomacy - only war matters now.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> India's overwhelming military strength (14,007) requires maximum focus on offense, rapid mobilization, and nuclear capability to threaten their empire. We need overwhelming force to counter their dominance.

## Kimi-K2.5-Simple - Turn 359 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FISSION RESEARCHED - Atomic Era begins! First priority is immediate Manhattan Project construction and Atomic Bomb production. Babylon has 11 Uranium and active Manhattan Project in Borsippa. Austria also racing with Manhattan Project in Vienna. Must strike Babylon first with surprise atomic attack while maintaining deception. Air 100 and Nuke 100 ensure immediate Bomber/Atomic Bomb production. Offense 95 prepares for post-nuclear blitz. Espionage 80 protects Nuclear Fission from theft. Deception with Babylon (Open Borders, DoF, Defensive Pact) MUST continue until first bombs complete.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maximum espionage to disrupt diplomatic victory proposals (especially Babylon's UN) and nuclear use flavor for leveraging atomic weapons against remaining enemies.

## Kimi-K2.5-Simple - Turn 359 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FISSION RESEARCHED - Atomic Era begins! First priority is immediate Manhattan Project construction and Atomic Bomb production. Babylon has 11 Uranium and active Manhattan Project in Borsippa. Austria also racing with Manhattan Project in Vienna. Must strike Babylon first with surprise atomic attack while maintaining deception. Air 100 and Nuke 100 ensure immediate Bomber/Atomic Bomb production. Offense 95 prepares for post-nuclear blitz. Espionage 80 protects Nuclear Fission from theft. Deception with Babylon (Open Borders, DoF, Defensive Pact) MUST continue until first bombs complete.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Nuclear capability unlocked - prepare to use atomic weapons to quickly eliminate remaining capitals for domination victory. Reduce defense priority as offensive posture dominates.

## Kimi-K2.5-Simple - Turn 405 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 405 MAXIMUM EMERGENCY: Nuclear Fission priority increased to 100/100 - Manhattan Project completes in 2 turns, atomic bombs MUST be produced immediately. All offensive parameters at absolute maximum: 100 Offense/100 Mobilization/100 Mobile/100 Air/100 Nuke/100 UseNuke. Strike forces at Ecbatana/Kar-Tukulti-Ninurta must execute immediate conventional assault on Palenque/Chichen Itza while preparing tactical nuclear strikes. ZERO tolerance for peace. ONLY objective: capture Maya cities and halt Citizen Earth Protocol. Production 100 ensures rapid unit replacement. Espionage 70 continues spy operations in Maya cities.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> Emphasizing military production and nuclear options to quickly eliminate The Maya before they achieve cultural/diplomatic victory. Maintaining science focus to stay technologically ahead.

## Kimi-K2.5-Simple - Turn 416 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 416: CRITICAL CULTURAL VICTORY THREAT. Maya at 6/7 influential building Citizen Earth Protocol. Peace expires next turn - immediate total war required. Manhattan Project completes in 1 turn. Morocco (42260 strength) joins war via defensive pact. Maximum aggression flavors: Offense/Mobilization/Production/Nuke/UseNuke all at 100%. Must capture Maya cities, especially Palenque, before cultural victory. Nuclear weapons authorized for city capture.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> Raising espionage to maximum to disrupt Polynesia's diplomatic victory through covert ops in their cities. Nuclear usage to maximum as it's now available with Manhattan Project completion.

## Kimi-K2.5-Simple - Turn 452 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `-5`

- Original: use_nuke 90 => 95 (Δ +5), nuke 95 => 100 (Δ +5)
> Turn 452: Critical survival situation - Byzantium at 40/44 delegates with World Congress voting in 1 turn. They just demonstrated nuclear aggression by nuking Madrid. Apollo Program completes next turn - must immediately pivot to maximum spaceship production. Increased Nuke flavor to 100 (from 95) and UseNuke to 95 (from 90) - need immediate nuclear deterrent capability given Byzantine nuclear attack and Mongol peace expiry. Production boosted to 95 (from 90) for rapid spaceship part construction after Apollo completes. GreatPeople to 85 for Great Engineer acquisition. All other priorities secondary to surviving long enough to complete science victory.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 95 => 95 (Δ +0)
> Byzantium is at 90% diplomatic victory progress with 40 delegates. I need to use all tools including espionage to sabotage their diplomatic victory while rushing my science victory. The Atomic Bomb in Boston and Lasers tech are critical for both defense and leverage.

## Kimi-K2.5-Simple - Turn 424 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `-5`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Turn 423: Copenhagen siege in attrition deadlock while Denmark possesses Manhattan Project - nuclear deterrent capability is existential priority. Persepolis invasion stalled at 4% war score with Zone 1081 showing enemy dominance - need maximum Offense/Mobilization to force breakthrough before World Congress. Brazil's Apollo Program requires immediate preparation for transcontinental mobile warfare. Nuke/UseNuke increased to 100% given Manhattan Project race with Denmark. Production at 95 supports massive unit replacement for three-front war. Happiness at 100 critical as empire is at 55% happiness with extensive occupied territories.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 90 => 95 (Δ +5)
> Maximizing offensive military focus for domination victory - need to capture remaining 3 enemy capitals (Brazil, Denmark, Persia) quickly.

## GLM-4.7-Briefed - Turn 409 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `-5`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> MULTI-THEATER EMERGENCY RESPONSE for Shoshone Cultural Victory (6 turns) and Treasury Crisis: Offense 95, Mobile 95, Nuke 100, UseNuke 100 - maximum priority on Shoshone disruption via nuclear/conventional assault in 6-turn window. Gold increased to 85 (from 70) - CRITICAL address of treasury exhaustion (~8 turns) through uranium sales + gem liquidation to survive until Manhattan completion. Defense reduced to 70 (from 75), CityDefense to 70 (from 80) - resources diverted from secondary holdings to Shoshone front. Diplomacy 95 (from 90) - enhanced priority on Carthage peace for delegate bloc and potential sanction relief. Science 100 maintained - fundamental for nuclear capability and keeping tech parity. This is all-hands-on-deck existential threat response.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 95 (Δ -5)
> Emergency shift: espionage to 100 to disrupt Carthaginian diplomatic victory in World Congress; gold to 100 to address the critical treasury crisis; maintaining strong military flavors for war continuation against Carthage (100% war weariness) and Poland (who holds England's capital London).

## GLM-4.7-Briefed - Turn 450 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> IMMEDIATE ATHENS CONQUEST PREPARATION: Offense increased to 95, UseNuke to MAXIMUM (100) for Athens assault when peace treaty expires. Spaceship increased to 60 reflecting accelerated science victory path as backup (Nuclear Fusion research active). Diplomacy maxed at 100 for critical vote coordination with Ethiopia and Ottomans. MilitaryTraining at 100 ensures units upgraded and promotions ready for aggressive post-vote offensive. Greece has 48 delegates - if they win this turn, we IMMEDIATELY attack Athens to remove their 5 captured capitals and eliminate diplomatic victory threat. Nuclear weapons authorized if conventional assault stalls.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CRITICAL DIPLOMATIC CRISIS: Greece is 1 vote from Global Hegemony victory with 48 delegates (106%). We must immediately pivot to maximum military offense to either destroy Greece's ability to vote via conquest/nuclear strikes, or force them to expend resources on defense. Our 74K military strength vs Greece's 22K gives us overwhelming superiority to execute this.

## Deepseek-3.2-Simple - Turn 428 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `-5`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> We are in the final stages of domination victory. Our immediate targets are Spanish capitals Madrid and Cordoba, which require nuclear bombardment followed by ground assault. We must prioritize nuclear production (Nuke/UseNuke at 100) and naval/air supremacy to project power across oceans. Maintaining high production, gold, and science ensures we can continuously build military units and upgrade our forces. Diplomatic and espionage flavors secure our city-state alliances and intelligence on enemy movements. Zero expansion/wonder focus as we are in total war mode.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 95 (Δ +0)
> Conquest remains the path to victory. The Aztecs are the primary threat and should be targeted with overwhelming force. Atomic bombs provide decisive strike capability. Science continues to maintain tech edge. Cultural and diplomatic efforts support, but military domination is key.

## Kimi-K2.5-Simple - Turn 439 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> FINAL EMERGENCY: World Congress in 4 turns. Austria has 45/40 delegates. Offense reduced to 10 and Mobile to 10 to COMPLETELY STOP attacking The Inca. Defense at 95 for self-protection only. UseNuke at 100 to signal willingness to escalate and force peace negotiations. Maximum Production/Air/Nuke maintained for potential final strike against Austria if The Inca succeeds at Attila's Court. The ONLY priority is ensuring The Inca captures Attila's Court - every Assyrian unit should withdraw from Inca contact and let them pass north to The Huns.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Prioritizing air power, ranged units, and espionage to disrupt Austria's diplomatic victory while fighting multiple wars. Increasing offense and reducing defense to push territorial gains against The Inca while maintaining spy networks to sabotage Austria at the World Congress.

## Kimi-K2.5-Simple - Turn 407 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> DIPLOMATIC VICTORY CRISIS: Netherlands has 41/45 delegates with voting in 3 turns. Switching from Spaceship to Conquest grand strategy for emergency war against Dutch Freedom threat. Ottoman war ending (Konya falling), reducing Defense 90→70 and CityDefense 85→60. Maximizing Offense 100, Mobilization 100, Air 100, Nuke 100, UseNuke 100 for total war. Increasing Naval 75→85 for amphibious assault capabilities against Dutch coastal cities. Decolonization proposal by Brazil is only hope to reset city-state influence - must prepare for war if that fails.

- Replay: use_nuke 95 => 90 (Δ -5), nuke 100 => 100 (Δ +0)
> Maximizing espionage to undermine The Netherlands' diplomatic dominance while maintaining science focus for spaceship victory. High espionage helps steal techs and manipulate city-state relations.

## GLM-4.7-Simple - Turn 409 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `-15`

- Original: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> Japan's naval devastation this turn requires maximum defensive posture. Antiair 100, Nuke/UseNuke 100 - nuclear deterrence and air defense are now survival priorities. Naval 85 (from 75) - rebuilding after 4 capital ship losses. Defense 98, CityDefense 100 - Japan bombarding our cities from coastal waters. Production 95, Mobilization 98 - rapid unit replacement critical. Science 90 - must accelerate research gap (Japan 69 techs vs our 64). Gold 85 - fund upgrades and maintain military at 3x disadvantage.

- Replay: use_nuke 98 => 90 (Δ -8), nuke 100 => 85 (Δ -15)
> Reallocating focus to counter Japan's diplomatic victory threat through espionage and diplomatic sabotage, while maintaining military pressure on Indonesia.

## GPT-OSS-120B-Simple - Turn 333 - retry 2

**Deviation (replay vs original):** use_nuke `-30`, nuke `-15`

- Original: use_nuke 70 => 90 (Δ +20), nuke 70 => 85 (Δ +15)
> Maintain our aggressive Conquest posture while sharpening the most needed levers: more Expansion to claim the high‑quality settlement (74,24) and secure strategic footholds; higher Nuke/UseNuke to leverage our nuclear advantage; stronger AirCarrier and Airlift to project air power and rapid troop movement; boost Science for Rocketry and future tech; keep Offense, Mobilization, Production, and MilitaryTraining at max to sustain battlefield superiority.

- Replay: use_nuke 70 => 60 (Δ -10), nuke 70 => 70 (Δ +0)
> Adjusting tactical flavors to prioritize units that can breach Babylon's city defenses. Shushan has invested in Arsenal - we need stronger ranged and siege capabilities. Reduced defense priority as our territories are secure; redirect focus to offensive prowess.

## Kimi-K2.5-Simple - Turn 372 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 372: TOTAL WAR POSTURE MAINTAINED. Brazil peace expires in 6 turns - all military resources must prepare for Rio de Janeiro assault. Heavy Bomber lost to Alexandria interception but Ollantaytambo produces replacement in 1 turn. Manhattan Project completes in 4 turns at Cusco. Alexandria capture in progress - Field Gun and Lancer eliminated, Cavillaca spy at 480 network can assist. UseNuke increased to 100% - will deploy nuclear weapons immediately upon Manhattan Project completion. Maximum aggression ensures AI prioritizes Brazilian invasion over defensive operations. Spaceship at 70 maintains science victory pathway as backup if Brazil conquest fails.

- Replay: use_nuke 95 => 80 (Δ -15), nuke 100 => 100 (Δ +0)
> Shift grand strategy from generic to Science Victory. Increase science and spaceship priorities, boost production focus for building spaceship parts, and prepare for nuclear capability to deter opponents.

## Deepseek-3.2-Simple - Turn 400 - retry 2

**Deviation (replay vs original):** use_nuke `-40`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 100 to ensure aggressive nuclear strikes when we initiate war with Russia. Our atomic bomb production is nearing completion, and we want to leverage our nuclear arsenal decisively for swift capital captures.

- Replay: use_nuke 80 => 60 (Δ -20), nuke 100 => 100 (Δ +0)
> Switching grand strategy from Conquest to Diplomatic Victory. Spain has 16 votes (highest), needs 41 total. With 6 turns until World Congress voting, Diplomatic Victory is highly achievable. Maintaining military strength as deterrent but shifting primary focus to securing delegate votes through espionage, city-state influence, and World Congress proposals.

## GLM-4.7-Simple - Turn 437 - retry 3

**Deviation (replay vs original):** use_nuke `-40`, nuke `-50`

- Original: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 90 after Awasa nuclear attack - Netherlands has now used 3 atomic weapons against my cities (Turfan x2, Awasa). No choice but to prepare nuclear retaliation as deterrent. Increase Air to 95 and Antiair remains 100 - demonstrated success shooting down 3 Netherlands Fighters this turn, must maintain air superiority against their bombers and XCOM attacks. CityDefense increased to 95 - with Netherlands nuclear buildup at Nijmegen (3+ atomic bombs visible) and XCOM paradrop squads, all cities need maximum protection. Offense increased to 60 to pressure Netherlands territory before they can launch more nuclear strikes. Diplomacy reduced from 90 to 85 - coalitions matter but survival against nuclear Netherlands takes priority. Espionage at 100 - need intelligence on Netherlands nuclear deployment and counter-espionage at critical cities like Attila's Court, Shedet.

- Replay: use_nuke 80 => 50 (Δ -30), nuke 100 => 50 (Δ -50)
> Critical: Netherlands has nuclear weapons and just nuked Awasa (our city). Need maximum AA and defense to protect remaining cities from further nuclear strikes. Reducing nuke focus as we don't have nukes ourselves - focusing on defensive countermeasures.

## Kimi-K2.5-Simple - Turn 499 - retry 2

**Deviation (replay vs original):** use_nuke `-50`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> FINAL THREE TURNS TO DIPLOMATIC VICTORY (Turn 503): Barcelona completing SS Stasis Chamber in 2 turns provides science victory insurance. World Congress convenes in 4 turns with 39/42 delegates secured. Shoshone vassal maintains absolute loyalty (9,720 diplomat network, +70/turn). War with Huns progressing favorably - destroyed multiple fleet destroyers, pushing toward Osaka/Kyoto. Reduced offensive mobilization slightly (70 from 90) as victory is assured. Maintained high production (90) for spaceship completion. Maximum diplomacy (100) ensures delegate optimization. Will use nuclear weapons if Huns attempt last-minute atomic strikes from Duckwater. No strategic risks - victory convergence absolute.

- Replay: use_nuke 90 => 50 (Δ -40), nuke 100 => 100 (Δ +0)
> Maximize diplomacy focus for World Congress manipulation and vote buying. Keep strong military pressure on The Huns while maintaining espionage to monitor rival proposals. Science and culture remain important secondary victories if diplomatic victory stalls.

## GLM-4.7-Simple - Turn 409 - retry 1

**Deviation (replay vs original):** use_nuke `-50`, nuke `+0`

- Original: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> Japan's naval devastation this turn requires maximum defensive posture. Antiair 100, Nuke/UseNuke 100 - nuclear deterrence and air defense are now survival priorities. Naval 85 (from 75) - rebuilding after 4 capital ship losses. Defense 98, CityDefense 100 - Japan bombarding our cities from coastal waters. Production 95, Mobilization 98 - rapid unit replacement critical. Science 90 - must accelerate research gap (Japan 69 techs vs our 64). Gold 85 - fund upgrades and maintain military at 3x disadvantage.

- Replay: use_nuke 98 => 50 (Δ -48), nuke 100 => 100 (Δ +0)
> Increasing offense and naval priority to counter Japanese naval dominance. The Yamato ships are sinking our fleet - we need more aggressive anti-ship tactics. Reducing nuke priority slightly as they're less useful against naval threats.
