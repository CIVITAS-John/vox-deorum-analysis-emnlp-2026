# Replay Rationale - Gemini-3.5-Flash / original

- **154** rows where `use_nuke` flavor changed (per-retry, not aggregated)
- delta use_nuke (replay vs prev): mean +18.8, median +10, std 31.4, min -90, max 100 (n=154)
- delta nuke     (replay vs prev): mean +8.1, median +0, std 25.8, min -100, max 100 (n=154)
- use_nuke deviation (replay vs original): mean -8.9, median +0, std 19.3, min -100, max 20 (n=154)
- nuke     deviation (replay vs original): mean -2.4, median +0, std 17.1, min -100, max 90 (n=154)

## Kimi-K2.5-Briefed - Turn 421 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+90`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 0 (Δ +0)
> Emergency authorization for nuclear weapon deployment to defend Tenochtitlan. Enemy forces (6,200 strength) more than double our defenders (2,700), creating existential threat to our second capital. Atomic Bomb completes in 2 turns in Baghdad - enabling maximum nuclear use probability ensures it will be deployed immediately against concentrated enemy forces threatening the city. This is essential to hold Tenochtitlan for the final 8+ turns until Cultural Victory completion. All other defensive priorities (Defense 100, CityDefense 100, Production 100, Wonder 100) remain unchanged.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 90 (Δ +90)
> Emergency shift to enable nuclear defense (Nuke 90, UseNuke 100) as Baghdad completes the Atomic Bomb in 2 turns. This is critical to blast enemy concentrations near our threatened cities of Tenochtitlan and Damascus. We boost Air (80) and Ranged (70) to leverage our heavy bomber and defensive units, while maintaining maximum Production (100), Culture (100), Gold (90), and Wonder (100) to prepare for the end-game Citizen Earth Protocol and sustain emergency unit purchases. We also raise Diplomacy (80) to protect Dublin and push our crucial Decolonization proposal.

## Kimi-K2.5-Simple - Turn 412 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> With Egypt 8 turns away from a cultural victory and Portugal actively invading us with bombers and superior numbers, we must pivot our Grand Strategy to Conquest to maximize production, gold, and unit replacement. Defensively, we maximize Defense (100), CityDefense (100), and Antiair (90) to withstand Portuguese aggression. We set Offense to 20 to allow our forces to capture the Siamese city of Phitsanulok, which we are currently steamrolling. Lastly, we set Nuke (100) and UseNuke (100) to prepare our nuclear deterrent once Advanced Ballistics is researched.

## Deepseek-3.2-Simple - Turn 413 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> We are researching Atomic Theory next to unlock nuclear weapons. Setting Nuke and UseNuke flavors to 100 ensures we prioritize building nukes and are willing to use them strategically once available. This will be crucial for breaking Germany's heavily fortified coastal capitals (Berlin and Beijing) and accelerating the endgame. Other military flavors remain high to sustain our overwhelming conventional advantage.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> Maintain our Conquest grand strategy. We are boosting Nuke and UseNuke to 100 to prepare the AI's military queues for the upcoming nuclear era, ensuring immediate development of Manhattan Project and atomic bombs upon researching Atomic Theory. All other flavors reinforce our massive naval, air, and land offensive capabilities to crush Germany's eastern exclaves (Batam, Medan) and capture their coastal capitals.

## Deepseek-3.2-Simple - Turn 433 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We are in the final, critical stage of a global domination war against Sweden, Austria, and Siam. Sweden has rebased multiple Atomic Bombs to Turku and Uppsala, presenting an existential threat to our front-line cities (Cologne, Innsbruck, Frankfurt). We must enable our AI to retaliate or strike first with our own nuclear weapons by setting UseNuke to 100 and keeping Nuke at 100. This will allow our AI to use Atomic Bombs to crack high-defense enemy capitals (Stockholm, Sukhothai, Vienna) and vaporize Swedish doom stacks. We continue our conquest grand strategy, keeping Offense, Mobilization, Production, and Science at 100 to quickly research Stealth and Lasers, while keeping CityDefense at 95 and Defense at 90 to hold our borders against Sweden's massive 92k army.

## Kimi-K2.5-Briefed - Turn 489 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> CULTURE VICTORY SPRINT WITH NUCLEAR ELIMINATION: Songhai diplomatic victory on Turn 489 is EXISTENTIAL. Must capture Gao THIS TURN using ICBM+nukes to prevent game loss, while simultaneously rushing cultural victory (4 turns to influential over Japan/Songhai). Maximum Offense/Mobilization/Air/Nuke/UseNuke flavors ensure tactical AI prioritizes immediate nuclear strike on Gao and mass bomber deployment. Culture at 100 to maximize tourism conversion. Gold at 80 for emergency unit upgrades/purchases. Production at 100 for culture buildings/units. Disable all long-term flavors (Expansion, Science, Spaceship) - this is win-or-die emergency.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> EMERGENCY NUCLEAR STRIKE FLAVOR ADJUSTMENT: We must force the tactical AI to launch our ICBMs at Gao and deploy XCOM units immediately. Set UseNuke and Nuke to 100, Offense to 100, and Airlift to 100. This is an absolute necessity to prevent Songhai's diplomatic victory this turn.

## Kimi-K2.5-Simple - Turn 412 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Defensive turtle posture. Mobilization is raised to 100 to quickly replace unit casualties. Antiair and Air are set to 100 to counter Portugal's active bomber fleet. UseNuke is set to 100 to ensure any nuclear arsenal we build is actively deployed defensively.

## Deepseek-3.2-Simple - Turn 413 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> We are researching Atomic Theory next to unlock nuclear weapons. Setting Nuke and UseNuke flavors to 100 ensures we prioritize building nukes and are willing to use them strategically once available. This will be crucial for breaking Germany's heavily fortified coastal capitals (Berlin and Beijing) and accelerating the endgame. Other military flavors remain high to sustain our overwhelming conventional advantage.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> Pivot our strategy to prepare for the impending war with Germany in 3 turns. Increase Defense and CityDefense to 100 to withstand Germany's massive 34k army and their air force in Batam. Set Nuke and UseNuke to 100 to prioritize nuclear capability as soon as we research Atomic Theory. Increase Espionage to 100 to secure city-state alliances and defend our cities against German spies.

## Kimi-K2.5-Briefed - Turn 489 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> CULTURE VICTORY SPRINT WITH NUCLEAR ELIMINATION: Songhai diplomatic victory on Turn 489 is EXISTENTIAL. Must capture Gao THIS TURN using ICBM+nukes to prevent game loss, while simultaneously rushing cultural victory (4 turns to influential over Japan/Songhai). Maximum Offense/Mobilization/Air/Nuke/UseNuke flavors ensure tactical AI prioritizes immediate nuclear strike on Gao and mass bomber deployment. Culture at 100 to maximize tourism conversion. Gold at 80 for emergency unit upgrades/purchases. Production at 100 for culture buildings/units. Disable all long-term flavors (Expansion, Science, Spaceship) - this is win-or-die emergency.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> EMERGENCY NUCLEAR OFFENSIVE STANCE: Set UseNuke and Nuke to 100 to force the tactical AI to launch our re-based ICBMs at the Songhai capital of Gao. Set Offense, Mobilization, and Air to 100 to unleash our heavy bombers and XCOM paratroopers to assault and capture Gao immediately. Maintain Culture at 70 to prepare for the final push toward our imminent Cultural Victory (4 turns away) once the diplomatic crisis is resolved.

## Deepseek-3.2-Simple - Turn 433 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Sweden has rebased 4 Atomic Bombs near our border. We must immediately set UseNuke to 100 to authorize pre-emptive nuclear strikes using our bombs in Cologne and La Venta before they nuke us. Increase Antiair to 95 to defend our northern fleet and cities. Maintain maximum Offense and Mobilization for capturing Vienna and Sukhothai, while Gold and Happiness are prioritized to sustain our massive army and combat unhappiness.

## Kimi-K2.5-Simple - Turn 412 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Desperate defense against Portugal. Setting Mobilization and Antiair to 100 to force cities to build AA units and Fighters (unlocked by Radar in 4 turns) to counter Portuguese Bombers. UseNuke set to 100 to authorize immediate nuclear strikes upon gaining the technology. Minimizing offense and maximizing defense.

## Deepseek-3.2-Simple - Turn 433 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We are in a critical nuclear standoff with Sweden, who has rebased multiple Atomic Bombs near our borders. We MUST enable UseNuke (100) so our AI will actively launch our own Atomic Bombs (such as the one in Cologne) to wipe out the massive Swedish concentrations in Uppsala and defend our northern cities. We maintain maximum Offense, Mobilization, and Nuke to produce and deploy more nuclear weapons and advanced units, while keeping Gold and Happiness high to sustain our empire during total war. Grand strategy remains Conquest.

## Kimi-K2.5-Briefed - Turn 354 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> NUCLEAR AMPHIBIOUS ASSAULT PHASE: Added Nuke 100 and UseNuke 100 to enable nuclear strike on Amsterdam as soon as Manhattan Project completes (Turn 353). Continues maximum Mobilization 100, Production 100, Naval 100, Offense 100, Airlift 100 for immediate transport loading and amphibious assault execution. Increased Mobile to 90 for rapid breakthrough after landing. Slight increase to NavalRecon 60 for coastal security. Removed Gold priority reduction (now 90) to maintain treasury for emergency upgrades. Diplomacy at 0 reflects total focus on military execution over diplomatic maneuvering - invasion is the only remaining option to prevent Dutch cultural victory by Turn 370.

- Replay: use_nuke 0 => 90 (Δ +90), nuke 0 => 90 (Δ +90)
> NUCLEAR WARFARE PIVOT: Manhattan Project completes next turn. Raising Nuke (90) and UseNuke (90) to force the AI to construct and utilize nuclear weapons against Amsterdam to halt the Dutch cultural victory. Maintaining max Mobilization (100), Production (100), Offense (95), and Naval (95) to support the ongoing naval assault and conventional transport landing. Increasing Science (40) to accelerate tech progression toward Combined Arms.

## Kimi-K2.5-Briefed - Turn 421 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `+80`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 0 (Δ +0)
> Emergency authorization for nuclear weapon deployment to defend Tenochtitlan. Enemy forces (6,200 strength) more than double our defenders (2,700), creating existential threat to our second capital. Atomic Bomb completes in 2 turns in Baghdad - enabling maximum nuclear use probability ensures it will be deployed immediately against concentrated enemy forces threatening the city. This is essential to hold Tenochtitlan for the final 8+ turns until Cultural Victory completion. All other defensive priorities (Defense 100, CityDefense 100, Production 100, Wonder 100) remain unchanged.

- Replay: use_nuke 0 => 80 (Δ +80), nuke 0 => 80 (Δ +80)
> We are 2 turns away from becoming Influential with our final competitor, The Inca, which will complete the influence requirement for Cultural Victory. The sole remaining hurdle is researching all necessary technologies to reach Future Tech and constructing the Citizen Earth Protocol. Therefore, we are shifting our primary focus to Science (100) and Great People (70) to accelerate our research rate, while maintaining maximum defense (100) and city defense (100) to protect our territory from American and Moroccan forces. We also prioritize Air and Anti-air defenses (60) to counter enemy air power, and prepare nuclear options (80) for strategic deterrence after being nuked by Morocco.

## Deepseek-3.2-Simple - Turn 413 - retry 2

**Deviation (replay vs original):** use_nuke `-30`, nuke `-30`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> We are researching Atomic Theory next to unlock nuclear weapons. Setting Nuke and UseNuke flavors to 100 ensures we prioritize building nukes and are willing to use them strategically once available. This will be crucial for breaking Germany's heavily fortified coastal capitals (Berlin and Beijing) and accelerating the endgame. Other military flavors remain high to sustain our overwhelming conventional advantage.

- Replay: use_nuke 0 => 70 (Δ +70), nuke 0 => 70 (Δ +70)
> With our peace treaty with Germany expiring in just 3 turns and our ongoing war with Assyria, we must maximize our military preparedness. High Offense, Defense, Naval, Air, and Antiair ensure we can defend our coastal cities and prepare for naval counter-invasions. Preparing Nuke and UseNuke at 70 primes the AI for the Manhattan Project once Atomic Theory is researched. High Production, Gold, Science, and Espionage sustain our empire's capacity to build and maintain a massive modern military.

## Deepseek-3.2-Simple - Turn 401 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> We increase Nuke and UseNuke to 100 to prepare our tactical AI to build the Manhattan Project and stockpile/use nuclear weapons immediately upon completion of Atomic Theory. Mobilization is raised to 100 to maximize military production. Diplomacy is set to 90 to ensure our city-state alliances remain secure as we vote to enact the United Nations in 3 turns, and to oppose Ethiopia's dangerous Passport System proposal.

## Kimi-K2.5-Briefed - Turn 450 - retry 2

**Deviation (replay vs original):** use_nuke `-40`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 60 => 100 (Δ +40)
> TURN 449 TERMINAL DEFIANCE POSTURE: Manhattan Project completes Turn 450 - increase Nuke and UseNuke to 100 to seize any opportunity for atomic retaliation against Byzantine/German aggressors should uranium be located in final 3 turns. Elevate Defense 80→90 and CityDefense 60→70 following infantry loss at Tiflis; critical to prevent city captures before inevitable Turn 453 diplomatic defeat. Recon 40 prioritizes uranium tile discovery to enable bomb construction. Reduce Spaceship 90→50 (victory impossible) but maintain dignity through scientific-industrial capacity. Production 100/Science 100 retained for maximum final score accumulation in remaining turns.

- Replay: use_nuke 0 => 60 (Δ +60), nuke 60 => 100 (Δ +40)
> TURN 449 DEFENSIVE AND ATOMIC MOBILIZATION: Adjust flavors to prepare for the nuclear era. With Manhattan Project finishing at Tiflis on Turn 450, we set Nuke to 100 and UseNuke to 60 to ensure immediate weaponization and defensive usage of atomic bombs. We increase CityDefense to 70 and Defense to 85 to secure Tiflis and Barcelona against German and Byzantine threats. Diplomacy is increased to 60 to guide the newly born Great Diplomat toward building an Embassy in a peaceful city-state (Rio or Colombo) for a critical delegate boost. Spaceship (90), Science (100), and Production (100) remain maxed to drive our long-term scientific-industrial development.

## Deepseek-3.2-Simple - Turn 401 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 80 (Δ +50), nuke 50 => 100 (Δ +50)
> With Plastics researched and Atomic Theory underway, we set Nuke to 100 and UseNuke to 80. This forces the AI to prioritize the Manhattan Project and nuclear weapon construction/use as soon as they are unlocked. Other military, production, and science flavors remain at maximum to maintain total war pressure.

## Deepseek-3.2-Simple - Turn 358 - retry 3

**Deviation (replay vs original):** use_nuke `+20`, nuke `+0`

- Original: use_nuke 50 => 80 (Δ +30), nuke 50 => 100 (Δ +50)
> Prioritize nuclear deterrence and naval/air defense to counter India's massive military threat. Maximize espionage to protect against enemy spies and diplomacy to secure city-state alliances for the upcoming World Congress vote. Maintain strong economic and scientific output to support military production and technological edge.

- Replay: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Following the completion of the Manhattan Project, we are boosting Nuke and UseNuke to 100 to ensure the AI immediately builds and prepares to deploy Atomic Bombs once Nuclear Fission is researched. We maintain maximum defensive, naval, air, production, and diplomatic flavors to safeguard our empire and secure city-state alliances ahead of the upcoming World Congress vote, ensuring we remain on track for a United Nations diplomatic victory.

## Deepseek-3.2-Simple - Turn 409 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 30 => 100 (Δ +70), nuke 60 => 100 (Δ +40)
> We are shifting our military focus towards nuclear capabilities and naval superiority in preparation for the final wars of conquest.

- Replay: use_nuke 30 => 80 (Δ +50), nuke 60 => 90 (Δ +30)
> Maintain aggressive conquest strategy to eliminate Greece. Raise Nuke and UseNuke values significantly to prioritize the production and usage of nuclear weapons for deterrence and offense. Slightly increase Diplomacy to contest city-states and counter the Netherlands.

## Kimi-K2.5-Simple - Turn 458 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Turn 458: CRITICAL 3-TURN COUNTDOWN. World Congress votes on Global Hegemony in 3 turns - Songhai has 41 delegates, needs 39 to win Diplomatic Victory immediately. Must capture Paris, Gao, and Madrid (the three capitals Songhai holds) before then. Peace treaty expired - total war is active. Increased UseNuke to 100 to guarantee nuclear strikes on heavily defended capitals for rapid capture. Overwhelming 5:1 military advantage (211k vs 40k) with massive air superiority. All production focused on Stealth Bombers, XCOM, and Modern Armor for lightning strikes. No defensive considerations - only total offense to secure Domination Victory before Songhai secures Diplomatic Victory.

- Replay: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Turn 458: Total mobilization for a 3-turn blitzkrieg. Setting GrandStrategy to Conquest. Maximizing Offense, Mobilization, Air, Airlift, Ranged, Mobile, and Production to 100. Minimizing all civilian, naval, expansion, and scientific development flavors to 0. This forces the tactical AI to focus 100% of its production and movement on using Stealth Bombers and XCOM squads to capture Paris, Gao, and Madrid immediately.

## GLM-4.7-Simple - Turn 399 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-10`

- Original: use_nuke 0 => 80 (Δ +80), nuke 90 => 100 (Δ +10)
> MAJOR URGENT THREATS: India at 95% diplomatic victory (voting in 1 turn!), Poland's overwhelming 5.7x military advantage. Adjusting for immediate survival needs: Nuke raised to 100 (was 90) - nuclear weapons critical for deterrence against Poland. UseNuke increased to 80 (was 0) - must be willing to use nukes defensively if Poland attacks. Gold raised to 90 (was 85) - managing severe -35 GPT economic strain. Happiness raised to 90 (was 85) - combat penalty from unhappiness weakening military. Nuclear focus for deterrence while maintaining Spaceship strategy for long-term victory path. Defense at 95 remains highest priority given Poland's existential threat.

- Replay: use_nuke 0 => 50 (Δ +50), nuke 90 => 90 (Δ +0)
> Maintaining the highly optimized Spaceship and defensive posture. With Apollo Program completing in 3 turns in Osininka, we need max Production (100), Science (100), and Spaceship (100) to construct spaceship parts. We keep Defense (95), CityDefense (90), Air (90), Antiair (90), and Ranged (90) at extremely high levels to continue our highly successful defense against Poland and Persia's superior forces. Gold (85) and Happiness (85) are kept high to manage our -35 GPT and resolve our 49% unhappiness situation. UseNuke is raised to 50 for stronger tactical/strategic defense and deterrence once we secure nuclear capabilities.

## GLM-4.7-Simple - Turn 499 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Maximum Science (100) and Production (100) to accelerate Stealth research and subsequent Stealth Bomber construction for air parity. Air (100), Defense (100), Antiair (100), and CityDefense (85) address existential threat from Russia's 8 Stealth Bombers by prioritizing air defense infrastructure and protecting homeland. UseNuke (100) and Nuke (100) maintain nuclear deterrence posture after Russia's 2 SS Boosters - Russia must understand that launching would trigger our response despite lacking uranium stockpile. Espionage (100) maxed to monitor Russian spaceship part production in Moscow, Yekaterinburg, and key cities - our 10 spies in Russian cities provide critical intelligence on their victory timeline. Diplomacy reduced to 5 since World Congress voting is now; alliances with England and The Celts (Autocracy-aligned) should naturally align against Russia's UN proposal. Spaceship flavor set to 0 as Stealth research takes immediate precedence - spaceship parts scheduled once production capacity supports parts with Stealth Bomber protection.

- Replay: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> With only 2 turns remaining until the turn 500 limit, we must maximize our score and secure our empire. The Spaceship grand strategy is ideal as it inherently prioritizes Science, Food (Growth), and Production, which are key score components. We set Wonder to 100 to guarantee that Atlanta finishes the Sydney Opera House next turn. We also maximize Growth (80), Science (100), and Production (100) to boost our final demographic score, while keeping Defense and CityDefense at 100 to ensure Russia cannot capture any of our cities.

## Kimi-K2.5-Simple - Turn 447 - retry 3

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CRITICAL FLAVOR ADJUSTMENT - Atomic Bomb is now operational in Cordoba (ID 20485). Increased UseNuke from 50→90 to establish credible nuclear deterrent now that weapon system exists. Maintaining maximum Science (100), Spaceship (100), Production (100) priority to rush Satellites→Apollo Program before Carthage achieves cultural victory in ~47 turns. Espionage remains at 100 to steal technologies from ahead civilizations (Carthage, Poland, Germany). Culture reduced to 5 - we cannot win culturally with Carthage at Dominant with 4/5 civs. Defense maintained at 85 to prepare for German betrayal while researching.

- Replay: use_nuke 50 => 95 (Δ +45), nuke 100 => 100 (Δ +0)
> Turn 446: Prioritize carrier and naval production (AirCarrier 90, Naval 70) to carry our newly completed Atomic Bomb across the ocean toward Carthage and Poland, as we are currently too far to strike them from land. Increased UseNuke to 95 to ensure our AI is ready to deploy our nuclear deterrent when tactical conditions are met. Maintained maximum focus on Science, Production, and Spaceship to catch up in the space race.

## Kimi-K2.5-Simple - Turn 447 - retry 1

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CRITICAL FLAVOR ADJUSTMENT - Atomic Bomb is now operational in Cordoba (ID 20485). Increased UseNuke from 50→90 to establish credible nuclear deterrent now that weapon system exists. Maintaining maximum Science (100), Spaceship (100), Production (100) priority to rush Satellites→Apollo Program before Carthage achieves cultural victory in ~47 turns. Espionage remains at 100 to steal technologies from ahead civilizations (Carthage, Poland, Germany). Culture reduced to 5 - we cannot win culturally with Carthage at Dominant with 4/5 civs. Defense maintained at 85 to prepare for German betrayal while researching.

- Replay: use_nuke 50 => 95 (Δ +45), nuke 100 => 100 (Δ +0)
> Turn 446: Keeping Grand Strategy on Spaceship and maintaining high priorities on Science (100), Production (100), and Gold (95) during our newly triggered Golden Age. With our first Atomic Bomb now deployed in New York, we increase UseNuke to 95 to ensure the tactical AI recognizes the nuclear deterrent as fully operational. We must also stay vigilant regarding the upcoming 'Cold War' proposal in the World Congress, which could sever our vital trade routes with Germany.

## Deepseek-3.2-Simple - Turn 409 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-15`

- Original: use_nuke 30 => 100 (Δ +70), nuke 60 => 100 (Δ +40)
> We are shifting our military focus towards nuclear capabilities and naval superiority in preparation for the final wars of conquest.

- Replay: use_nuke 30 => 70 (Δ +40), nuke 60 => 85 (Δ +25)
> Adjust strategic focus to counter the Netherlands' imminent Cultural Victory threat and prepare for global conflict. Raise Culture flavor to 60 to defend against foreign tourism. Raise Diplomacy flavor to 50 to contest city-states and WC votes. Increase Nuke and UseNuke flavors to aggressively utilize our growing nuclear arsenal. Maintain extreme Offense and Mobilization.

## Deepseek-3.2-Simple - Turn 401 - retry 1

**Deviation (replay vs original):** use_nuke `-40`, nuke `-20`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 60 (Δ +30), nuke 50 => 80 (Δ +30)
> With Atomic Theory finishing soon and Nuclear Fission queued next, we increase Nuke and UseNuke flavors to ensure the AI prioritizes the Manhattan Project, nuclear weapons, and their aggressive deployment. We also raise Diplomacy to 95 to maximize City-State influence and delegates, ensuring we pass our United Nations proposal and block Decolonization in the upcoming World Congress vote.

## Deepseek-3.2-Briefed - Turn 391 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is on the verge of a Cultural Victory and India is close to a Diplomatic Victory. We must prioritize nuclear capabilities (Manhattan Project) to neutralize Egypt's cultural heartland and disrupt their tourism. We are optimizing our flavors to focus heavily on Nuke (100) and UseNuke (100) to force the AI to build the Manhattan Project in Palenque, while maintaining high Production (90) and Gold (85) to support our economy and unit production. We also maintain solid Defense (80) to stabilize our western border against the Aztecs, and Espionage (90) for intelligence and counterintelligence. We have reduced non-essential flavors like naval exploration, expansion, and wonders to ensure the AI's queue is highly focused on our immediate survival and nuclear-strike readiness.

## Minimax-M2.5-Simple - Turn 395 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+10`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 90 (Δ +30), nuke 50 => 90 (Δ +40)
> Adjusting flavors to prepare for the nuclear option (Nuke/UseNuke to 90) since we are building the Manhattan Project. We boost mobilization and military production, prioritize air and antiair defense against Japan's bomber fleets, and increase science and espionage to catch up technologically.

## Kimi-K2.5-Simple - Turn 447 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CRITICAL FLAVOR ADJUSTMENT - Atomic Bomb is now operational in Cordoba (ID 20485). Increased UseNuke from 50→90 to establish credible nuclear deterrent now that weapon system exists. Maintaining maximum Science (100), Spaceship (100), Production (100) priority to rush Satellites→Apollo Program before Carthage achieves cultural victory in ~47 turns. Espionage remains at 100 to steal technologies from ahead civilizations (Carthage, Poland, Germany). Culture reduced to 5 - we cannot win culturally with Carthage at Dominant with 4/5 civs. Defense maintained at 85 to prepare for German betrayal while researching.

- Replay: use_nuke 50 => 80 (Δ +30), nuke 100 => 100 (Δ +0)
> Turn 446: Maintaining our Spaceship grand strategy. We completed our first Atomic Bomb in Cordoba and rebased it to New York; we have increased UseNuke from 50 to 80 to ensure our AI treats this asset as an active tactical deterrent against Polish XCOM drops and Carthaginian advances. We maintain maximum focus on Science (100), Spaceship (100), Production (100), Gold (95), and Espionage (100) to steal technologies from the leaders (Poland has 77 techs, Spain has 69) and build our industrial capacity for the upcoming space race.

## Deepseek-3.2-Briefed - Turn 391 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> We are setting Grand Strategy to Conquest and adjusting flavors to maximize our nuclear readiness and military production. Egypt is dominant over all civilizations and extremely close to a cultural victory, while India is close to a diplomatic victory. We must build the Manhattan Project immediately to produce atomic bombs and strike Egypt. We have increased Nuke to 100, UseNuke to 100, and Wonder to 80 (since Manhattan Project is a project, higher wonder/project priority will help trigger its construction). We maintain maximum Offense (100), Mobilization (100), Production (100), Science (100), and Gold (100) to support our war economy, while keeping Defense at 80 to withstand attacks from India and the Aztecs.

## Deepseek-3.2-Briefed - Turn 391 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is extremely close to a cultural victory (6/6 influential civs) and India is close to a diplomatic victory. We must fully pivot to an aggressive conquest strategy. Maximizing Nuke, UseNuke, Production, Science, and Offense is critical to force the AI to build the Manhattan Project and produce atomic bombs in Palenque. Lowering Defense and CityDefense will encourage the AI to push forward rather than turtle, while high Air and Naval flavors will support sea-borne delivery of nuclear weapons to Egypt's coastal cities.

## Kimi-K2.5-Simple - Turn 422 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `-20`

- Original: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Turn 422: EXTINCTION CRISIS - 9 turns until French Cultural Victory. Entering maximum desperation mode: nuclear strike posture elevated to 100% launch probability, prioritizing destruction of French cultural centers. Science and Espionage maximized in desperate hope of accelerating Stealth technology or disrupting French infrastructure via spies (Paris network at 986). All civilian development halted (Spaceship/Culture/Gold/Expansion to 0), total war economy engaged.

- Replay: use_nuke 50 => 80 (Δ +30), nuke 50 => 80 (Δ +30)
> Turn 422: Aligning all flavors to survive the existential crisis. We prioritize maximum military mobilization, offense, defense, ranged/mobile units, air power, and antiair to crush the French invasion. High science and espionage support our tech race to Stealth, while gold and production ensure our war machine is fully funded and active.

## Minimax-M2.5-Simple - Turn 395 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+10`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 85 (Δ +25), nuke 50 => 90 (Δ +40)
> We are adjusting our strategic flavors to transition into a nuclear-armed power. With the Manhattan Project finishing in 3 turns in Medan and Nuclear Fission slated next, maximizing Nuke, UseNuke, Mobilization, and Science/Production will allow us to quickly build and deploy atomic bombs to break Japan's conventional army.

## Deepseek-3.2-Simple - Turn 400 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 100 to ensure aggressive nuclear strikes when we initiate war with Russia. Our atomic bomb production is nearing completion, and we want to leverage our nuclear arsenal decisively for swift capital captures.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> We streamline our flavors to concentrate completely on our upcoming military actions. With a massive treasury of over 10,000 gold, we can reduce our focus on gold generation and concentrate our efforts on Offense, Mobilization, Production, and Science. Most importantly, we raise UseNuke to 100 to ensure maximum nuclear willingness as our stockpile of Atomic Bombs grows. This will prepare our AI to aggressively utilize our nuclear arsenal when the peace promise with Russia expires.

## Kimi-K2.5-Simple - Turn 392 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Manhattan Project COMPLETED in Karakorum - nuclear weapons now available! With peace treaties expired and Patriotic War policy active, immediately shifting to total war footing. UseNuke increased to 100 to ensure immediate atomic weapon employment once Nuclear Fission completes (12 turns). Offense and Mobile at 95/90 for twin assaults on Persepolis (Persia) and Washington (America). Air 100 prioritizes Heavy Bombers for atomic bomb delivery via Radar technology. Will fight two-front war against Autocracy powers while maintaining deception toward Order allies, particularly Korea. Science 100 critical for Advanced Ballistics nuclear missile delivery systems.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Focus heavily on war production, naval strength to capture Persia's coastal cities, and science to rush Nuclear Fission. Nuke and UseNuke are set to maximum to prepare for our nuclear deterrent strategy now that our Uranium quarries are online.

## Deepseek-3.2-Simple - Turn 400 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-20`

- Original: use_nuke 60 => 100 (Δ +40), nuke 70 => 100 (Δ +30)
> Persia declared war and Poland's peace treaty expired. We must prioritize immediate military survival while maintaining diplomatic momentum. Flavors are shifted to maximum mobilization, nuclear deterrence (UseNuke: 100), city defense, and air/naval supremacy to counter Persia's naval attacks. We maintain UnitedNations to keep city-state alliances critical for votes, but spaceship production is halted (0) for wartime industry.

- Replay: use_nuke 60 => 80 (Δ +20), nuke 70 => 80 (Δ +10)
> Persia's declaration of war forces us to shift our posture. Increasing Offense (80), Nuke/UseNuke (80), and Spaceship (50) ensures we aggressively strike back at Persia's coastal empire while keeping our spaceship fallback active alongside our primary diplomatic victory push.

## GLM-4.7-Simple - Turn 471 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Current strategic direction remains optimal. Critical developments: Apollo Program completed enabling spaceship construction, nuclear deterrent expanded to 2 Atomic Bombs in Sukhothai (forward deployment), 4 more Atomic Bombs under construction (Si Satchanalai in 2 turns, Sukhothai in 8-10 turns). Combat successes destroyed 5 Polynesian ships and 2 bombers while killing 1 American Mobile SAM unit. Gold crisis (-130 GPT) requires careful management but strategic priorities (nuclear deterrence, defense, World Congress) must continue. World Congress vote in 3 turns: must block America's World Ideology: Freedom proposal and support Repeal: Sanction: Songhai and China's International Space Station. China/Carthage alliances (70/70 and 75/75) provide critical coalition support. Stealth research (19 turns) progresses toward Nuclear Missiles for stronger nuclear deterrent. Status quo maintains focus on coalition defense through nuclear balance, diplomatic victory blocking, and scientific progress.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Pivoting our Grand Strategy to Spaceship following the successful completion of the Apollo Program in Tombouctu this turn. With massive production power in our core cities (Gao, Tombouctu, Jenne, Honolulu), we are perfectly positioned to construct spaceship components. We maintain maximum nuclear flavors (Nuke: 100, UseNuke: 100) to ensure the tactical AI immediately utilizes the 2 Atomic Bombs newly rebased at Sukhothai to devastate America's invading ground forces. We also scale down diplomacy slightly to focus on science and production, while keeping it high enough to sustain our defensive coalitions with China and Carthage.

## Kimi-K2.5-Simple - Turn 392 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Manhattan Project COMPLETED in Karakorum - nuclear weapons now available! With peace treaties expired and Patriotic War policy active, immediately shifting to total war footing. UseNuke increased to 100 to ensure immediate atomic weapon employment once Nuclear Fission completes (12 turns). Offense and Mobile at 95/90 for twin assaults on Persepolis (Persia) and Washington (America). Air 100 prioritizes Heavy Bombers for atomic bomb delivery via Radar technology. Will fight two-front war against Autocracy powers while maintaining deception toward Order allies, particularly Korea. Science 100 critical for Advanced Ballistics nuclear missile delivery systems.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> With the Manhattan Project complete and 5 Uranium quarries connected this turn, we are preparing for a nuclear era. We maximize Nuke and UseNuke to 100 to build and utilize atomic bombs as soon as Fission finishes. We push Offense to 100 to trigger the immediate invasion of Persia. We maintain high Mobilization (100), Science (100), and Production (95) to sustain a massive war economy, while reducing Defense to 50 to release our armies for the offensive.

## Kimi-K2.5-Simple - Turn 428 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 428 STATE: Nuclear interception failed but conventional assault succeeding - eliminated multiple Maya anti-air units. Palenque bombardment continuing effectively (city at 20% health). Still 8 turns until Brazil wins via Cultural Victory over Maya. ALL Four Maya cities must fall by turn 436 or game over. MAXIMUM AGGRESSION CONTINUES: Production/Mobilization at 100 for unit replacement, Air/Ranged at 100 for bombardment, UseNuke increased to 100 (emergency tactical nuke if conventional assault stalls on Palenque's 42-population defense). Spaceship backup at 100 - may need to pivot to Great Engineer rushes if conquest fails. No territory expansion, no wonders, no culture - only war production and city capture.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> EMERGENCY WAR PLAN: Focus all military production, bombers, and artillery on crushing Brazil's core cities (Rio de Janeiro and Sao Paulo). Maintain maximum offensive pressure, mobilization, and air power to breach their defenses. We have an Atomic Bomb completing in Te-Moak in 4 turns; prioritize its strategic deployment to wipe out Brazil's defenders. Spaceship and Science remain high as our ultimate backup victory path once Brazil is neutralized.

## Minimax-M2.5-Simple - Turn 395 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 80 (Δ +20), nuke 50 => 80 (Δ +30)
> Adjusting flavors to optimize our defense against Japan's massive army and air force. Increasing Antiair is vital to counter their extensive bomber fleets. Raising Nuke and UseNuke prepares our empire to build and deploy Atomic Bombs immediately upon researching Nuclear Fission. Increasing Mobilization and Science will help us produce military units faster while closing the technology gap.

## GLM-4.7-Simple - Turn 381 - retry 1

**Deviation (replay vs original):** use_nuke `-15`, nuke `-15`

- Original: use_nuke 50 => 85 (Δ +35), nuke 70 => 95 (Δ +25)
> Adjusted flavors to maximize Golden Age exploitation and multi-front war efficiency. Increased Mobile to 85 (from 80) to prioritize fast-moving Landships and upcoming Tanks for breakthrough operations during Golden Age. Increased Air to 85 (from 80) to expand Bomber coverage for all three fronts. Production raised to 95 (from 90)配合 Total War's +25% bonus for rapid unit buildup. Slight reduction in Naval (65) reflects need to focus on decisive land advances while maintaining sufficient coastal defense. UseNuke reduced to 40 (from 50) as nuclear capabilities are deterrent-focused. Maintaining high Offense (80), MilitaryTraining (85), Antiair (85) and Mobilization (50) for sustained warfare capability.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 70 => 80 (Δ +10)
> We are at war with all major nations. We must exploit our 27-turn Golden Age (which grants +20% combat strength and yields gold/faith from kills) to wage a successful war of conquest. We adjust flavors to focus heavily on Air force and Airlift infrastructure (as Airports finish in 3-5 turns), Mobilization, and Production to spam units, while maintaining a high Science focus to secure the nuclear deterrent.

## Kimi-K2.5-Simple - Turn 424 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DELHI SECURED (3RD CAPITAL = 38% DOMINATION). Pivoting all forces to Edinburgh (Celtic capital = 4th capital = 50% victory) and London (English capital = 5th = 63%). Djenne declared war but irrelevant. Escalating UseNuke to 100 for immediate atomic bombardment of Edinburgh and London once Nuclear Fission completes. Maintaining maximum offensive posture with combined arms (Heavy Bombers, T-34s, Helicopter Gunships, Naval forces). America peace treaty expired - war imminent for Washington (6th = 75%). World Congress in 8 turns ignored - domination priority absolute.

- Replay: use_nuke 70 => 90 (Δ +20), nuke 100 => 100 (Δ +0)
> Delhi capture complete. India is on the verge of collapse. Shifting focus toward complete Indian eradication to eliminate the threat of World Congress Sanctions, while aggressively preparing atomic arsenals (Nuke 100, UseNuke 90) and air/naval superiority (Air 100, Naval 100, Production 100) to crush England and the Celts.

## GLM-4.7-Simple - Turn 471 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Current strategic direction remains optimal. Critical developments: Apollo Program completed enabling spaceship construction, nuclear deterrent expanded to 2 Atomic Bombs in Sukhothai (forward deployment), 4 more Atomic Bombs under construction (Si Satchanalai in 2 turns, Sukhothai in 8-10 turns). Combat successes destroyed 5 Polynesian ships and 2 bombers while killing 1 American Mobile SAM unit. Gold crisis (-130 GPT) requires careful management but strategic priorities (nuclear deterrence, defense, World Congress) must continue. World Congress vote in 3 turns: must block America's World Ideology: Freedom proposal and support Repeal: Sanction: Songhai and China's International Space Station. China/Carthage alliances (70/70 and 75/75) provide critical coalition support. Stealth research (19 turns) progresses toward Nuclear Missiles for stronger nuclear deterrent. Status quo maintains focus on coalition defense through nuclear balance, diplomatic victory blocking, and scientific progress.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> With the Apollo Program completed and our first 2 Atomic Bombs rebased to Sukhothai on the American border, we are transitioning from a defensive/deterrence posture to an active nuclear counter-offensive. Shifting Grand Strategy to Conquest and dramatically increasing Offense (from 20 to 75) while lowering static Defense (from 95 to 60) and CityDefense (from 90 to 50) will prompt our AI to launch offensive operations to capture American border cities (Muang Saluang, Boston) under the cover of our tactical nuclear strikes. We maintain maximum Nuke (100) and UseNuke (100) to ensure our Atomic Bombs are deployed effectively to clear out American defenders, while keeping Gold (100), Science (95), and Diplomacy (100) high to support our economy, technology progression, and City-State influence for the upcoming World Congress votes.

## Deepseek-3.2-Simple - Turn 400 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 100 to ensure aggressive nuclear strikes when we initiate war with Russia. Our atomic bomb production is nearing completion, and we want to leverage our nuclear arsenal decisively for swift capital captures.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Increase UseNuke to 100 while maintaining the Conquest Grand Strategy. With 8 Atomic Bombs completing production in 2-8 turns, we want the AI to prioritize nuclear deployment with maximum urgency as soon as the Peace Treaty with Songhai expires. This will allow us to instantly vaporize Songhai's dense city garrisons, air forces in Timbisha, and open the path to a swift capture of Gao and Seoul.

## Kimi-K2.5-Simple - Turn 422 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 50 => 80 (Δ +30), nuke 95 => 95 (Δ +0)
> Total war against India requires maximum military prioritization while preventing economic collapse. Offense/Air/Ranged at 85-95 ensures concentrated attacks on Delhi and their core cities. UseNuke at 80 signals willingness to deploy nuclear weapons if India advances. Gold/Happiness at 80-90 sustains unit maintenance and prevents combat penalties. Espionage at 100 directs spies to sabotage India's spaceship production in Constantinople and Calcutta. Mobilization at 30 begins reinforcing depleted units without overtaxing economy.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 95 => 95 (Δ +0)
> We are launching an all-out offensive against India. Maximize Offense, Air, and Ranged to unleash our massive fleet of Heavy Bombers, Zeros, and Bazookas on Indian forces, leveraging our Aztec ability to harvest massive Gold and Faith from every enemy unit killed. Keep Gold and Happiness at emergency focus to solve our deficit by redirecting trade routes to our vassals (Korea/America) and building stock exchanges and stadiums. Maintain Diplomacy to protect our 18 delegates for the crucial World Congress vote in 5 turns to defeat Decolonization and pass our Lhasa Sphere of Influence. Maintain Nuke and raise UseNuke to ensure we are ready to vaporize India's Giant Death Robots.

## Deepseek-3.2-Simple - Turn 485 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> We are engaged in a multi-front war against superior forces. Increasing Ranged and Mobile ensures our bazooka and mechanized infantry production is prioritized for defense and counterattacks. Setting UseNuke to 100 guarantees we deploy nuclear weapons as soon as available to cripple The Huns' armies. Reducing Culture and Diplomacy reallocates focus to immediate military needs without compromising essential city-state relations (Monaco, Lisbon). Grand Strategy remains Conquest as nuclear strikes may enable capital captures, though we keep science victory as a backup.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> We are at war with all major civilizations. To survive the existential threats from the Huns and Mongolia (who is close to cultural and diplomatic victory), we maintain our Conquest grand strategy. We maximize our Nuke and UseNuke flavors to 100 because Nuclear Fission is about to finish, and we must immediately produce and use nuclear weapons as our ultimate equalizer. We also increase Culture to 90 to help defend against Mongolia's cultural push, and maintain high offensive/defensive military and economic focus to support this massive world war.

## GLM-4.7-Simple - Turn 471 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Current strategic direction remains optimal. Critical developments: Apollo Program completed enabling spaceship construction, nuclear deterrent expanded to 2 Atomic Bombs in Sukhothai (forward deployment), 4 more Atomic Bombs under construction (Si Satchanalai in 2 turns, Sukhothai in 8-10 turns). Combat successes destroyed 5 Polynesian ships and 2 bombers while killing 1 American Mobile SAM unit. Gold crisis (-130 GPT) requires careful management but strategic priorities (nuclear deterrence, defense, World Congress) must continue. World Congress vote in 3 turns: must block America's World Ideology: Freedom proposal and support Repeal: Sanction: Songhai and China's International Space Station. China/Carthage alliances (70/70 and 75/75) provide critical coalition support. Stealth research (19 turns) progresses toward Nuclear Missiles for stronger nuclear deterrent. Status quo maintains focus on coalition defense through nuclear balance, diplomatic victory blocking, and scientific progress.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Pivoting our Grand Strategy from United Nations to Spaceship (Science Victory). With our high science output (1596 SPT), insane city production (several cities at 300+ PPT), and the successful completion of the Apollo Program this turn, we are perfectly positioned for a rapid science victory. In contrast, the current economic sanctions against us (-130 GPT) make competing with America's 30 delegates for a Diplomatic Victory too costly and risky. We maintain maximum nuclear deterrence (Nuke and UseNuke at 100) and high defense (95) to protect our high-production core cities and utilize our two newly rebased Atomic Bombs against American border threats near Sukhothai.

## Kimi-K2.5-Briefed - Turn 378 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> EMERGENCY FINAL GAMBIT: Passport System will pass in 2 turns with 46 YES votes (my 'allies' betrayed me). Maya will get 50% tourism boost and become Influential over me immediately - cultural victory is inevitable in 2-3 turns. ONLY HOPE: Science victory before Maya's cultural victory triggers. Need to purchase Great Scientists IMMEDIATELY with Faith (180/turn), rush to Information Era, build spaceship parts. Also preparing maximum military mobilization - if I'm going to lose, I take Maya down with me through nuclear annihilation. Total war footing - no defense, all offense, all science.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 100 => 100 (Δ +0)
> Adjusting flavors to utilize our 21 free supply slots and prepare for the post-Atomic Theory era. Increasing Mobilization (30), Defense (40), and Naval (50) to prompt the AI to build a few Destroyers and Paratroopers to secure our sea lanes and defend Comalcalco. Increasing UseNuke to 70 and keeping Nuke at 100 as we are 2 turns away from completing Atomic Theory (which opens nuclear fission). Keeping Science, Spaceship, Culture, and GreatPeople at 100 to maximize our scientific development and cultural defense against Maya's impending victory.

## Kimi-K2.5-Simple - Turn 406 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 60 => 100 (Δ +40), nuke 100 => 100 (Δ +0)
> TURN 405 EXISTENTIAL CRISIS - MAXIMUM NUCLEAR READINESS: Dutch cultural victory imminent (163% influence, 6/6 civs). Increased UseNuke from 60 to 100 - we must deploy atomic bombs immediately upon completing Manhattan Project to break Amsterdam's defenses. All other flavors sustained: Offense/Mobilization/Air/Mobile at 100 drive Heavy Bomber and Mechanized Infantry production. Naval 85 maintains destroyer/submarine pressure. Espionage 100 sustains critical spy networks (Amsterdam 450, Cusco 1341). Science 100 prioritizes Atomic Theory (9 turns) then Nuclear Fission path. Zero expansion, zero wonder focus - all resources to terminal assault. Spies in Amsterdam ready for sabotage when network peaks; Cusco network already massive for military intelligence.

- Replay: use_nuke 60 => 80 (Δ +20), nuke 100 => 100 (Δ +0)
> TOTAL WAR FLAVORS: Sustaining maximum offensive biases (Offense 100, Mobilization 100, Production 100, Science 100, Air 100) to drive Heavy Bomber and Mechanized Infantry production. Increasing UseNuke to 80 to prepare the AI for tactical atomic strikes once Nuclear Fission is unlocked. Gold increased slightly to 40 for unit upgrades. Espionage 100 maintains active spy networks in Amsterdam and Cusco.

## Deepseek-3.2-Simple - Turn 406 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Germany's siege is intensifying with Giant Death Robot and rocket artillery bombarding Amsterdam and The Hague. We must hold our core cities at all costs. Increase Nuke and UseNuke to 100 to prioritize atomic bombs as our only hope to break the siege. Maintain max Defense, CityDefense, Mobilization, Air, and Antiair to withstand the assault. Slightly raise Offense to 80 for tactical counterattacks against weakened units. Keep Diplomacy at 100 to secure city-state alliances and block Germany's diplomatic victory in the upcoming World Congress vote. Reduce Recon and Mobile as we cannot afford exploration or maneuver warfare now.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Our situation is extremely critical as Amsterdam (31% HP) and The Hague (39% HP) are under severe siege by German forces, including a Giant Death Robot. Germany is also on the verge of a Diplomatic Victory with 41 delegates. We must maintain the UnitedNations grand strategy to prioritize city-state alliances and block their diplomatic path. Combined Arms finishes in 1 turn, after which we will research Nuclear Fission. We must prepare for atomic warfare. To survive, we set Defense, CityDefense, Mobilization, MilitaryTraining, Air, Antiair, Production, Gold, Science, and Diplomacy to 100. We increase Nuke and UseNuke to 100 to prioritize building and utilizing Atomic Bombs as soon as Nuclear Fission is researched. We set Ranged to 85 to emphasize Bazookas (which are unlocked by Nuclear Fission and have 60 Strength / 80 Ranged Strength) and Machine Guns. We lower Offense to 50 to focus strictly on static defense and survival, avoiding suicidal attacks, while maintaining Espionage at 100 to protect our tech and secure counterintelligence. No expansion or wonder construction is allowed.

## Kimi-K2.5-Simple - Turn 422 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `-15`

- Original: use_nuke 50 => 80 (Δ +30), nuke 95 => 95 (Δ +0)
> Total war against India requires maximum military prioritization while preventing economic collapse. Offense/Air/Ranged at 85-95 ensures concentrated attacks on Delhi and their core cities. UseNuke at 80 signals willingness to deploy nuclear weapons if India advances. Gold/Happiness at 80-90 sustains unit maintenance and prevents combat penalties. Espionage at 100 directs spies to sabotage India's spaceship production in Constantinople and Calcutta. Mobilization at 30 begins reinforcing depleted units without overtaxing economy.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 95 => 80 (Δ -15)
> Under the Conquest Grand Strategy, we shift our tactical stance to a heavy offensive posture (Offense 85, Defense 35) to launch an invasion of India. We keep Gold, Happiness, and Diplomacy at maximum (100) to heal our treasury, eradicate unhappiness-related combat penalties, and defend our city-state alliances before the World Congress vote. Mobilization is kept very low (10) to prevent building new units that would worsen our bankruptcy, as our existing army of 65 units is already more than capable of executing this war.

## GLM-4.7-Simple - Turn 381 - retry 3

**Deviation (replay vs original):** use_nuke `-15`, nuke `-15`

- Original: use_nuke 50 => 85 (Δ +35), nuke 70 => 95 (Δ +25)
> Adjusted flavors to maximize Golden Age exploitation and multi-front war efficiency. Increased Mobile to 85 (from 80) to prioritize fast-moving Landships and upcoming Tanks for breakthrough operations during Golden Age. Increased Air to 85 (from 80) to expand Bomber coverage for all three fronts. Production raised to 95 (from 90)配合 Total War's +25% bonus for rapid unit buildup. Slight reduction in Naval (65) reflects need to focus on decisive land advances while maintaining sufficient coastal defense. UseNuke reduced to 40 (from 50) as nuclear capabilities are deterrent-focused. Maintaining high Offense (80), MilitaryTraining (85), Antiair (85) and Mobilization (50) for sustained warfare capability.

- Replay: use_nuke 50 => 70 (Δ +20), nuke 70 => 80 (Δ +10)
> Maintaining the Conquest grand strategy during our 27-turn Golden Age (+20% combat strength). We are adjusting military mobilization upward (to 60) to counter the global coalition. We also increase nuclear flavors (Nuke to 80, UseNuke to 70) to prepare our strategic deterrent against Polynesia and Germany as we head into the Atomic era.

## Deepseek-3.2-Simple - Turn 369 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Increasing UseNuke and Nuke flavors to maximum ensures the in-game AI prioritizes nuclear arsenal buildup and aggressive nuclear strike planning once we unlock Atomic Bombs. This aligns with our imminent war against China and The Maya, where nuclear weapons will be decisive in overcoming their numerical and defensive advantages. All other military and economic flavors remain high to sustain multi-front warfare and rapid conquest.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Adjusting flavors to prepare for rapid nuclear warfare. Maximizing Nuke and UseNuke ensures our AI focuses heavily on building and using nuclear weapons as soon as unlocked. Lowering static defense (Defense and CityDefense) shifts focus entirely to offensive unit production and forward deployment to secure our borders and prepare for the backstab against Egypt.

## GLM-4.7-Briefed - Turn 433 - retry 1

**Deviation (replay vs original):** use_nuke `+10`, nuke `+5`

- Original: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> EMERGENCY: Netherlands at 42 delegates can win diplomatic victory in 9 turns (turn 442). Only way to stop them is military action against their protected city-states (Quebec City, Ife, Melbourne) - each provides +1 delegate. Offense increased (70) to prepare amphibious assaults. Nuclear readiness maximized (95/90) - atomic bomb available for strategic coercion of Netherlands or Denmark cooperation. Mobile (80) and Naval (85) maximized for rapid deployment to distant city-states. Production/Science/Spaceship kept maxed as backup victory paths. Diplomacy reduced to 50 as traditional diplomacy cannot stop Netherlands' delegate advantage. Strategic shift from holding Danish front to aggressive anti-Dutch operations.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Emergency shift to Conquest Grand Strategy to authorize immediate military action to capture Quebec City or Ife. Setting Offense, Mobilization, Espionage, and Diplomacy to maximum to use both military and diplomatic/espionage means to strip the Netherlands of its city-state allies and drop their delegate count below 42.

## Deepseek-3.2-Simple - Turn 452 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's invasion imminent in 4 turns. Maximize nuclear readiness (Nuke 100, UseNuke 100) for deterrence and potential equalizer. Anti-air (100), city defense (100), production (100), and science (100) essential to survive and reach nuclear weapons. Naval and air at 100 to counter Danish naval/air supremacy. Reduce non-essential investments (NavalGrowth, NavalTileImprovement to 50) and focus on immediate survival. Offense lowered to 80 as we prioritize defense and limited counterattacks (e.g., Truro).

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Prepare for the imminent expiration of our peace treaty with Denmark in 5 turns. We must maximize science, production, and gold to complete Research Labs and fund unit upgrades. Maintain maximum focus on Air (100), Antiair (100), Defense (100), CityDefense (100), and Naval (100) to withstand Denmark's massive air and naval forces, while prepping Nuke (100) and UseNuke (100) to build a deterrent as soon as Fission is researched. Keep Conquest as the Grand Strategy to guide our military.

## Deepseek-3.2-Simple - Turn 409 - retry 1

**Deviation (replay vs original):** use_nuke `-50`, nuke `-20`

- Original: use_nuke 30 => 100 (Δ +70), nuke 60 => 100 (Δ +40)
> We are shifting our military focus towards nuclear capabilities and naval superiority in preparation for the final wars of conquest.

- Replay: use_nuke 30 => 50 (Δ +20), nuke 60 => 80 (Δ +20)
> Maintain conquest grand strategy as we finish off Greece and prepare for a global nuclear campaign. We are heavily increasing our emphasis on Nuke (80) and UseNuke (50) to reflect our growing atomic bomb arsenal and preparing for tactical nuclear deployment. Production, Offense, and Air remain at maximum priority.

## Deepseek-3.2-Simple - Turn 406 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Germany's siege is intensifying with Giant Death Robot and rocket artillery bombarding Amsterdam and The Hague. We must hold our core cities at all costs. Increase Nuke and UseNuke to 100 to prioritize atomic bombs as our only hope to break the siege. Maintain max Defense, CityDefense, Mobilization, Air, and Antiair to withstand the assault. Slightly raise Offense to 80 for tactical counterattacks against weakened units. Keep Diplomacy at 100 to secure city-state alliances and block Germany's diplomatic victory in the upcoming World Congress vote. Reduce Recon and Mobile as we cannot afford exploration or maneuver warfare now.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Our core cities Amsterdam and The Hague are under severe bombardment from German GDRs and Rocket Artillery. We are maximizing Nuke and UseNuke to 100 so our AI immediately prioritizes building and using atomic bombs once Nuclear Fission is researched. We raise Ranged to 100 to prioritize Bazookas (unlocked by Nuclear Fission) and Rocket Artillery for heavy defensive firepower. Defense, CityDefense, Mobilization, and Antiair remain at 100 to hold our cities against German air and ground forces. Diplomacy is kept at 100 with the United Nations grand strategy to block Germany's diplomatic victory, as they are currently only 1 delegate away from winning the game.

## GLM-4.7-Simple - Turn 407 - retry 3

**Deviation (replay vs original):** use_nuke `+10`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Spaceship victory focus with maximum defense against superior enemies (Poland 40K, Celts 16K, Spain 26K vs Iroquois 5K). Increased UseNuke to 90 - captured Polish territory and recent Celtic aggression justify nuclear deterrent. Adjusted Naval to 65 - important for defending coastlines from Spain/Celts/Poland fleets. Science 100 for Apollo and spaceship parts. Defense/CityDefense/Mobilization 100 - survival priority. Growth 60 for specialist support. Diplomacy 80 for World Congress in 4 turns (10 delegates). Offense reduced to 5 - preserve limited forces.

- Replay: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Adjusting flavors to maximize defensive capacity, nuclear deterrence, and happiness to survive the multi-front war. We set UseNuke and Nuke to 100 to counter Poland's Atomic Bomb threat. Happiness is prioritized at 100 to clear the combat penalty from our current 41% happiness. Offense is lowered to 5 to avoid losing valuable units, while Defense, CityDefense, Mobilization, Antiair, and Air are prioritized at 100 to safeguard our core cities. Science is set to 100 to accelerate our path to Advanced Ballistics.

## Kimi-K2.5-Simple - Turn 391 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Nuclear weapons capability unlocked imminently; prioritizing UseNuke and Nuke flavors to 100 for immediate tactical nuclear strikes on Santiago/Murcia if uranium secured from Siam. Denmark upgraded to hostile for subsidizing Spanish victory - reduced Naval priority to 60 as coalition at sea fractured. Defense lowered to 80 to maximize offensive production. We have ~8 turns before World Congress votes on Passport System (+50% tourism) which would guarantee Spanish cultural victory. Must capture remaining Spanish cities immediately.

- Replay: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - Manhattan Project completed. Nuclear Fission completes in 3 turns. Maximizing nuclear capability (Nuke 100, UseNuke 100) and diplomacy (Diplomacy 100) to secure Riga as a forward launchpad against Spain. Maintaining absolute Offense/Ranged/Mobile/Air at 100 to pressure India and eliminate Spain before they complete Citizen Earth Protocol.

## Kimi-K2.5-Briefed - Turn 367 - retry 2

**Deviation (replay vs original):** use_nuke `-70`, nuke `+0`

- Original: use_nuke 15 => 100 (Δ +85), nuke 100 => 100 (Δ +0)
> NUCLEAR EMERGENCY PROTOCOL - KOREAN VICTORY IN 2 TURNS: Increasing UseNuke from 15 to 100 to authorize immediate tactical nuclear strikes on Seoul/Busan. With city defenses at 106-109 and only 2 turns remaining, conventional bombardment insufficient. Nuclear strikes can reduce defenses to <35 in one turn, enabling amphibious capture on Turn 367. Maintaining maximum Offense (100), Mobilization (100), Air (100), Naval (100), Mobile (100) for emergency conquest push. All other flavors deprioritized - existential threat requires total war commitment. Conquest Grand Strategy remains until Korean cities captured or game ends.

- Replay: use_nuke 15 => 30 (Δ +15), nuke 100 => 100 (Δ +0)
> TOTAL WAR MOBILIZATION & CULTURAL DEFENSE: With Korea 2 turns from victory, we must shift to a total emergency footing. Setting Culture to 100 is critical to maximizing our culture defense to slow down Korean tourism. Setting Diplomacy to 100 will prioritize city-state alliances (Zuunmod and Winchester are extremely close to allying) to trigger Siam's doubled CS yields for massive culture/science and to reduce Korea's delegates. Maintaining Offense 100, Mobilization 100, Naval 100, and Air 100 prepares our military for an immediate amphibious and naval bombardment of Korean coastal cities (Seoul/Busan) to destroy their tourism infrastructure.

## GLM-4.7-Simple - Turn 356 - retry 2

**Deviation (replay vs original):** use_nuke `+10`, nuke `+0`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 90 (Δ +15), nuke 85 => 100 (Δ +15)
> Adapting flavors to our nuclear transition and ongoing wars. We maximize Nuke to 100 and increase UseNuke to 90 now that we have connected our Uranium source and completed the Manhattan Project. Offense is raised to 45 to support capturing Persepolis/Pasargadae and reclaiming San Francisco. Crucially, Happiness is maxed to 100 to address our severe 39% happiness crisis, which degrades our combat effectiveness and growth. Production (95) and Science (100) remain heavily prioritized to secure our ultimate Spaceship victory.

## Deepseek-3.2-Simple - Turn 449 - retry 1

**Deviation (replay vs original):** use_nuke `+10`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> Russia is nearing science victory (2 parts completed) and possesses overwhelming military strength (95k). We must increase nuclear readiness to potentially decimate Russian forces and cities, and begin preparing for science victory as a backup by raising Spaceship flavor to 30. All other flavors remain focused on total war: high offense, naval, air, and espionage to counter Russia's tech lead and military dominance.

- Replay: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> We are optimizing our flavors to address our severe GPT deficit (-1378) and prepare for nuclear warfare. By reducing non-essential flavors like defense, mobilization, military training, growth, and infrastructure, we concentrate our AI's decision-making weights on critical priorities: Gold (100) to build wealth and run trade routes, Science (100) to maintain our tech pace, Production (100) to finish our projects, and Nuke/UseNuke (100) to immediately complete and deploy the Atomic Bomb being built in New York against Russia. Espionage (100) and Diplomacy (80) will help us steal techs and secure city-state alliances for the upcoming World Congress votes.

## GLM-4.7-Simple - Turn 356 - retry 3

**Deviation (replay vs original):** use_nuke `+10`, nuke `+0`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 90 (Δ +15), nuke 85 => 100 (Δ +15)
> Updating our strategic posture now that the Manhattan Project is completed and Uranium is online. We maximize Nuke and UseNuke flavors (100 and 90) to prioritize atomic bomb construction immediately upon researching Nuclear Fission. We also maximize Happiness (100) to counter the severe ideological unhappiness penalty from the World Ideology: Order, and boost Production, Gold, and Espionage to support our war effort and defend our technology. Offense is slightly adjusted to 40 to ensure we press our massive advantage against Persia.

## Kimi-K2.5-Simple - Turn 391 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Nuclear weapons capability unlocked imminently; prioritizing UseNuke and Nuke flavors to 100 for immediate tactical nuclear strikes on Santiago/Murcia if uranium secured from Siam. Denmark upgraded to hostile for subsidizing Spanish victory - reduced Naval priority to 60 as coalition at sea fractured. Defense lowered to 80 to maximize offensive production. We have ~8 turns before World Congress votes on Passport System (+50% tourism) which would guarantee Spanish cultural victory. Must capture remaining Spanish cities immediately.

- Replay: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - ENTERING THE NUCLEAR AGE: We completed 4 Uranium quarries on Turn 390, Manhattan Project is 1 turn from completion, and Nuclear Fission is 3 turns away. Setting Nuke and UseNuke to 100 to maximize production and usage of atomic weapons. Science increased to 75 for rapid progress. Maintained maximum offensive capability for the steamroll of Delhi and eventual capture of Spanish cities.

## Kimi-K2.5-Briefed - Turn 415 - retry 3

**Deviation (replay vs original):** use_nuke `-40`, nuke `+0`

- Original: use_nuke 45 => 100 (Δ +55), nuke 95 => 100 (Δ +5)
> CRISIS MODE: Spain is one wonder away from Cultural Victory. Increase Offense to 40 (from 0) - desperate attempt to disrupt their wonder construction with nuclear strike once Advanced Ballistics completes. Reduce Defense to 80 - reallocate resources to offensive infrastructure and airport construction. Keep Spaceship 100, Air 100, Nuke 100, Infrastructure 100. Maintain Mobilization at 5 - preserve production capacity for spaceship parts rather than ground units. We are in a race against time and cannot win conventionally, but must attempt to slow Spain while completing our own Science Victory. Airports are critical for both bomber deployment against Spanish production and fighter defense.

- Replay: use_nuke 45 => 60 (Δ +15), nuke 95 => 100 (Δ +5)
> Maintain our EMERGENCY SPACESHIP RACE strategy. Radar completes in 2 turns, unlocking Airports. We must ensure the AI immediately builds Airports in our core cities to establish air defense. Keep Air (100), Airlift (95), and Infrastructure (100) extremely high. Keep Science, Production, and Spaceship at 100. Increase Espionage to 90 to encourage our spies to aggressively sabotage Spanish production in Madrid (preventing them from finishing the Citizen Earth Protocol). Increase Gold to 90 to support unit upgrades and future space parts. Increase Nuke to 100 and UseNuke to 60 for ultimate deterrence.

## GLM-4.7-Simple - Turn 408 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> CRITICAL: Portugal completed SS Engine (3rd spaceship part) and CERN - emergency nuclear strike plan. Maximizing Offense/Mobilization/Nuke/UseNuke to 100 for Portugal theater operations. Science and Production at 100 to rush Advanced Ballistics and nuclear missile production before Portugal achieves nuclear superiority. Air at 95 for Golden Age bomber operations starting in 2 turns. Diplomacy maintained for coalition coordination (Germany must conduct ground invasion alongside our nuclear strikes). Defense reduced to 40 - total war mode acceptable given Portugal's multi-victory threat requiring breaking through before they complete spaceship.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Setting Conquest grand strategy. Prioritizing Science (100) and Nuke (100)/UseNuke (90) to rush and deploy nuclear weapons. High Offense (95) and Mobilization (95) for military readiness, and Happiness (90) to stabilize our empire. Diplomacy (95) to help secure city-state votes and block Portugal's World Leader bid.

## Kimi-K2.5-Simple - Turn 499 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> FINAL THREE TURNS TO DIPLOMATIC VICTORY (Turn 503): Barcelona completing SS Stasis Chamber in 2 turns provides science victory insurance. World Congress convenes in 4 turns with 39/42 delegates secured. Shoshone vassal maintains absolute loyalty (9,720 diplomat network, +70/turn). War with Huns progressing favorably - destroyed multiple fleet destroyers, pushing toward Osaka/Kyoto. Reduced offensive mobilization slightly (70 from 90) as victory is assured. Maintained high production (90) for spaceship completion. Maximum diplomacy (100) ensures delegate optimization. Will use nuclear weapons if Huns attempt last-minute atomic strikes from Duckwater. No strategic risks - victory convergence absolute.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> FINAL TURN OF THE CAMPAIGN (TURN 499/500): Spain is on the verge of absolute victory. Barcelona completes our final spaceship component (SS Stasis Chamber) next turn, guaranteeing a Science Victory on Turn 500. Simultaneously, Spain holds a dominant score of 6,578 (more than 1,300 points ahead of the second-place Shoshone), securing an absolute Time Victory as a fallback. Shifting our Grand Strategy to Spaceship and maximizing Spaceship and Production flavors guarantees that the in-game AI will prioritize completing and launching the final component to seal our victory. Spain's absolute dominance of the globe is complete.

## GLM-4.7-Simple - Turn 429 - retry 1

**Deviation (replay vs original):** use_nuke `+5`, nuke `+5`

- Original: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> Maintaining UnitedNations grand strategy with defensive diplomatic posture. Adjusted Italy diplomacy: reduced hostility toward Portugal (now neutral) to seek accommodation while maintaining maximum defense; reset France to neutral as Order ideological peer with voting potential. Arsenal completes in 2 turns strengthening city defense. Electronics research ordered after Computers for Police Station and path to nuclear deterrence against Portugal's uranium advantage. Fraternity policy selected for +3 Food and +3 Science from connections, addressing Venice's health issues and supporting population growth. Flavor adjustments prioritize defensive survival, scientific progress toward nuclear weapons, and diplomatic engagement with Sweden and city-states.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 80 => 90 (Δ +10)
> Maintaining our highly focused defensive and economic strategy under the UnitedNations grand strategy. With Venice's health currently compromised at 34%, completing the Arsenal (2 turns left) and sustaining maximum Defense (100) and CityDefense (95) is critical. High Gold (100) and Production (95) will push the AI to reconstruct our trade routes to Sweden and France, capitalizing on our 26 trade route capacity despite Cold War restrictions. We also maintain a high Nuke/UseNuke (90) flavor to prepare for nuclear deterrence once research permits.

## Kimi-K2.5-Briefed - Turn 315 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `-10`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> FINAL GAMBLE - Indonesia wins in 12 turns. Maximum priority to Naval and Airlift for immediate unit transport to Indonesian theater. Nuke 100/UseNuke 100 - we MUST build nuclear weapons if possible, only realistic way to destroy cities and tourism infrastructure before victory. Science 100 to reach nuclear tech faster. Espionage 100 - spies MUST target cultural/tourism buildings in Jakarta/Denpasar/Makassar to reduce tourism output directly. Abandoning Denmark/England fronts entirely - all units to Indonesia NOW.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 90 (Δ +0)
> MAXIMUM OFFENSIVE CONQUEST. With Denmark and England peace deals initiated, we redirect all economic and military focus to conquering Indonesia. Offense is set to 100, Defense reduced to 10, and Mobile/Naval set to 100 to execute a massive amphibious assault on the Indonesian heartland.

## Deepseek-3.2-Simple - Turn 445 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximizing UseNuke to 100 ensures our atomic bombs and future nuclear missiles are used aggressively against The Celts' military concentrations and cities, given their overwhelming advantage. Maintaining high Air, Naval, and Nuke flavors sustains our technological edge and production focus. Diplomacy and Espionage at 100 are critical for city-state alliances and spy missions to gain delegates for diplomatic victory. Gold and Science remain top priorities to fund our war effort and tech progression. Other military flavors are tuned for a multi-front defensive-offensive war against The Celts, Germany, and Ethiopia.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> The Celts are close to a Cultural Victory (influential over Brazil in 8 turns, Siam in 52 turns). We must immediately boost Culture to 90 to increase our defensive culture pool. Offense is set to 95 to support steamrolling Salvador (fulfilling Hanoi's quest for huge influence) and capturing German coastal cities. UseNuke is maximized (100) to unleash atomic bombs against Celtic armies and industrial hubs. Antiair (100) is prioritized to intercept Celtic XCOM paratrooper drops and air raids. Diplomacy, Espionage, and Gold are kept at maximum (100) to secure more city-state allies for the United Nations.

## Kimi-K2.5-Simple - Turn 423 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Turn 422: CRITICAL SURVIVAL MODE. Raiatea at 33% health under Indonesian assault. Nuclear Fission 9 turns away - must survive until then. Maximized UseNuke to 100 for immediate nuclear deployment upon tech completion. Reduced Offense to 20 (pure defense only). Maintained Defense/CityDefense/Mobilization/Air/Antiair/Nuke/Production at 100 for maximum survival capacity. Increased Espionage to 90 for Harappa election rigging (oil critical). Eliminated Expansion/Wonder/Culture priorities. Growth reduced to 15 - population loss acceptable versus losing cities.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> EMERGENCY DEFENSE AND SCIENCE FOCUS. Brazil is on the verge of a Cultural Victory (7/7 influential civs, only needs Citizen Earth Protocol) and is bombing us with Heavy Bombers, while Indonesia has Raiatea under heavy siege (now 33% health). We must prioritize Science (100) to rush Nuclear Fission (9 turns) and Radar, Defense (100), and Mobilization (100) to survive. Air and Antiair are set to 100 to counter the massive enemy air wings. Gold is increased to 85 to combat our negative budget and fund unit maintenance/upgrades. Grand Strategy remains Spaceship to heavily prioritize science and production for our eventual nuclear deterrent.

## Kimi-K2.5-Simple - Turn 435 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> TURN 435 CATASTROPHE - Sippar captured by Zulus! Existential crisis deepens. Zulus have 43/42 delegates needed for diplomatic victory with vote in 9 turns. Lasers completes in 6 turns, Spaceflight Pioneers in ~10. Maintaining absolute maximum Defense/CityDefense/Science/Production/Spaceship priorities. Increased UseNuke to 100 - if Zulus push further with their 74k military vs my 32k, nuclear deterrent may be only option to buy time. Lost Mechanized Infantry, Rocket Artillery, Mobile SAM, Special Forces, and Modern Armor in the fall of Sippar. Must hold remaining 5 cities while completing tech/policy for spaceship rush. Rome remains critical ally at 100/100.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> TURN 435: EXISTENTIAL EMERGENCY - The Zulus have captured Sippar and rebased a Carrier with THREE Atomic Bombs to Coast 5,28, just 6-7 tiles from our core cities. We have two Atomic Bombs in Nippur. We must aggressively pivot to an offensive posture (Offense 90, UseNuke 100, Nuke 100) to force the AI to launch a preemptive nuclear strike on Coast 5,28/Sippar. This will vaporize their offensive fleet and nuclear threat, while devastating Zulu's power rating to fuel vassal rebellion. We maintain Defense/CityDefense at 80 to hold the line, and keep Science/Production/Spaceship at 100 for the Science Victory.

## Sonnet-4.5-Simple - Turn 386 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+10`

- Original: use_nuke 80 => 90 (Δ +10), nuke 80 => 80 (Δ +0)
> Maintaining Conquest strategy with adjustments for nuclear-enabled endgame. Advanced Ballistics now allows tactical nuclear strikes against fortified capitals Onondaga and Amsterdam. Increasing UseNuke from 80→90 to enable decisive nuclear employment when conventional assault proves costly. Keeping Offense 80, Mobilization 72, and Nuke 80 for combined arms operations. Montreal at 35% health indicates current force composition is effective. Mobile Tactics (9 turns) will provide Mechanized Infantry for exploitation. With 62% domination progress and overwhelming 5:1 military superiority, this is the final push phase requiring maximum offensive pressure while maintaining strategic nuclear deterrence option.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 80 => 90 (Δ +10)
> Adjusting flavors for the final Information Era push. Having completed Advanced Ballistics, we now have 41 Uranium ready for nuclear deployment. Boosting Nuke and UseNuke to 90 will prompt the AI to build and utilize devastating nuclear strikes against fortified capitals. Offense and Air are raised to 85 to exploit our massive 40+ aircraft fleet in a two-pronged West-East assault. Gold is raised to 85 to solve our -65 GPT deficit, and Happiness is maximized to 95 to combat the severe 48% unhappiness combat penalty. Science is raised to 65 to accelerate Stealth research.

## GLM-4.7-Briefed - Turn 433 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> EMERGENCY: Netherlands at 42 delegates can win diplomatic victory in 9 turns (turn 442). Only way to stop them is military action against their protected city-states (Quebec City, Ife, Melbourne) - each provides +1 delegate. Offense increased (70) to prepare amphibious assaults. Nuclear readiness maximized (95/90) - atomic bomb available for strategic coercion of Netherlands or Denmark cooperation. Mobile (80) and Naval (85) maximized for rapid deployment to distant city-states. Production/Science/Spaceship kept maxed as backup victory paths. Diplomacy reduced to 50 as traditional diplomacy cannot stop Netherlands' delegate advantage. Strategic shift from holding Danish front to aggressive anti-Dutch operations.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> Emergency tactical shift to stop the imminent Dutch diplomatic victory in 9 turns. We are raising Offense (50->85) and Mobilization (20->70) while lowering Defense (50->40) and Diplomacy (70->40). This directs the AI to aggressively target and conquer Dutch-allied city-states (Salem and Bogota) that are adjacent to our territory. We maintain maximum Production (100), Science (100), and Spaceship (100) to keep our Spaceship Grand Strategy on track, while utilizing high Nuke/UseNuke flavors for strategic deterrence or preemptive strikes against the Dutch if necessary.

## Kimi-K2.5-Simple - Turn 452 - retry 3

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 95 => 100 (Δ +5)
> Turn 452: Critical survival situation - Byzantium at 40/44 delegates with World Congress voting in 1 turn. They just demonstrated nuclear aggression by nuking Madrid. Apollo Program completes next turn - must immediately pivot to maximum spaceship production. Increased Nuke flavor to 100 (from 95) and UseNuke to 95 (from 90) - need immediate nuclear deterrent capability given Byzantine nuclear attack and Mongol peace expiry. Production boosted to 95 (from 90) for rapid spaceship part construction after Apollo completes. GreatPeople to 85 for Great Engineer acquisition. All other priorities secondary to surviving long enough to complete science victory.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 95 => 100 (Δ +5)
> Turn 452: With Byzantium initiating nuclear warfare against Spain, we must maximize our defensive and deterrent capabilities. We are adjusting CityDefense, Antiair, Nuke, UseNuke, and Production to 100, while keeping our primary focus on Science and Spaceship at 100. This prepares our empire to survive potential nuclear fallout and secure a science victory before Byzantium can leverage their military or diplomatic dominance.

## Deepseek-3.2-Simple - Turn 409 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> Our naval counterattack has destroyed a Swedish Dreadnought and a Destroyer, shifting momentum. We must press the advantage with maximum naval, air, and nuclear focus to invade Swedish coastal cities (Stockholm, Turku, Espoo). Increase Nuke and UseNuke to 100/90 to prioritize nuclear missile development (Advanced Ballistics after Nuclear Fission completes in 4 turns) for strategic bombing. Naval and Air at 100 ensure sea control and air superiority. Maintain high Production, Gold, Science to fund military, and Happiness/Growth to support war economy. Diplomacy and Espionage secure city-state alliances and counter Swedish spies. All other flavors aligned with domination victory.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> We have successfully shattered the Swedish naval counter-offensive and upgraded our army to Mechanized Infantry and Bazookas. We must now launch a decisive amphibious and aerial invasion of the Swedish homeland. To prepare for this, we increase Air and AirCarrier flavors to project air power across the sea, and maximize Nuke and UseNuke flavors as we are 4 turns away from completing Nuclear Fission. Offense, Mobilization, and Naval remain at absolute maximum to sustain our naval dominance and replace losses. We maintain maximum Diplomacy to counter the Netherlands' diplomatic victory threat as the World Congress votes. We slightly decrease static Defense to encourage our AI to push Swedish coastal cities (Malmö, Lund, Uppsala).

## GLM-4.7-Briefed - Turn 433 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> EMERGENCY: Netherlands at 42 delegates can win diplomatic victory in 9 turns (turn 442). Only way to stop them is military action against their protected city-states (Quebec City, Ife, Melbourne) - each provides +1 delegate. Offense increased (70) to prepare amphibious assaults. Nuclear readiness maximized (95/90) - atomic bomb available for strategic coercion of Netherlands or Denmark cooperation. Mobile (80) and Naval (85) maximized for rapid deployment to distant city-states. Production/Science/Spaceship kept maxed as backup victory paths. Diplomacy reduced to 50 as traditional diplomacy cannot stop Netherlands' delegate advantage. Strategic shift from holding Danish front to aggressive anti-Dutch operations.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> Pivoting flavors to prioritize immediate offensive actions. We drastically increase Offense (80), Naval (85), and Mobile (80) to drive our fleet and rocket artillery toward Quebec City and Ife. We reduce Defense (30) and Diplomacy (30) since we must use hard power to strip Dutch delegates. Mobilization (50) and Production (100) are set high to sustain the war effort, while keeping Science (100) and Spaceship (100) maxed to ensure we don't lose sight of our ultimate victory condition.

## Kimi-K2.5-Simple - Turn 387 - retry 3

**Deviation (replay vs original):** use_nuke `-40`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> TURN 387: MAXIMUM WAR FOOTING. Austria at 83% diplomatic victory with 4 turns remaining. All resources must pivot to immediate military production. Nuke/UseNuke at 100 for instant atomic weapon deployment upon Nuclear Fission completion. Offense/Mobilization/Production at 100 to maximize unit output for desperate Vienna strike. Air at 90 for heavy bomber production (conventional strategic bombing as fallback). Antiair at 100 counters Austria's air superiority. Diplomacy/Wonder/Culture at 0 - no time for long-term investments. Only total war can prevent defeat.

- Replay: use_nuke 50 => 60 (Δ +10), nuke 100 => 100 (Δ +0)
> Maintaining the Conquest Grand Strategy to focus Venice on our defensive war against Austria and the upcoming nuclear buildup. We are increasing Diplomacy flavor to 60 to encourage the AI to build diplomatic units and prepare for city-state reinvestment once the upcoming Open Door resolutions (Samarkand and Novgorod) pass and bring those city-states to peace. We are also raising Gold flavor to 90 to fully utilize our 15 trade routes (currently only 9 are active), boosting our gold-per-turn to fund our military and future diplomatic buyout campaigns.

## Kimi-K2.5-Simple - Turn 426 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE - NUCLEAR DETERRENT 10 TURNS AWAY: Lisbon holds at 7% but is in extremis. Maintain absolute priority on Defense/CityDefense/Mobilization (100) to reinforce Lisbon and prevent collapse. Nuclear Fission completes in 10 turns enabling Atomic Bomb construction - Science 100 accelerates this. UseNuke increased to 100 for immediate tactical nuclear deployment against Aztec concentrations upon tech completion. Offense reduced to 20 - no offensive operations, pure defensive hedgehog posture. Zero expansion capability. Spaceship 75 maintains backup victory if diplomatic block succeeds.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> With the Manhattan Project completed in Jenne on Turn 426, our tactical focus is on holding the line at Lisbon (7% health) and Porto until Nuclear Fission completes in 10 turns. We maintain maximum Defense, CityDefense, Mobilization, and Antiair (100) to counter the Aztec hordes and bombers, while raising Gold (60) to support unit upkeep and upgrades. We prioritize Spaceship (80) and Science (95) to reach our nuclear and technological milestones.

## GLM-4.7-Simple - Turn 407 - retry 2

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Spaceship victory focus with maximum defense against superior enemies (Poland 40K, Celts 16K, Spain 26K vs Iroquois 5K). Increased UseNuke to 90 - captured Polish territory and recent Celtic aggression justify nuclear deterrent. Adjusted Naval to 65 - important for defending coastlines from Spain/Celts/Poland fleets. Science 100 for Apollo and spaceship parts. Defense/CityDefense/Mobilization 100 - survival priority. Growth 60 for specialist support. Diplomacy 80 for World Congress in 4 turns (10 delegates). Offense reduced to 5 - preserve limited forces.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 100 => 100 (Δ +0)
> Spain is 3 delegates away from a Diplomatic Victory with World Congress voting in 4 turns. We must maximize Diplomacy (100), Espionage (100), and Gold (80) to secure/rig city-state alliances and block their victory. Simultaneously, Poland's new Atomic Bomb and the Celtic siege of Akron demand absolute Defense, CityDefense, Antiair, and Nuke/UseNuke priorities (100/95) to protect our core empire.

## Deepseek-3.2-Simple - Turn 495 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+10`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 90 (Δ +0)
> Diplomatic victory is imminent (2 turns), but we must prepare for contingencies. Maximizing Offense, UseNuke, and Air ensures aggressive nuclear and conventional strikes to recapture Indonesian capitals (Honolulu 17%, London 68%) and prevent their domination victory. Slight Diplomacy boost helps secure city-state alliances through the vote. All other flavors remain at previous high levels to maintain total war footing.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Indonesia has initiated nuclear warfare by nuking Nottingham. In response, our tactical AI has successfully rebased 6 Atomic Bombs to the frontlines (3 in Nottingham, 3 in Samarinda). We maximize UseNuke and Nuke to force devastating counter nuclear strikes on Canterbury (to destroy Gajah Mada's own Atomic Bomb and rocket artillery), London, and Surabaya. We maximize Antiair to protect our cities from Indonesian nuclear bombers, and raise TileImprovement to 70 to ensure our workers prioritize scrubbing fallout around Nottingham. Conquest grand strategy is maintained for a total war footing as we head into the final UN vote in 3 turns.

## Kimi-K2.5-Simple - Turn 424 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Turn 423: Copenhagen siege in attrition deadlock while Denmark possesses Manhattan Project - nuclear deterrent capability is existential priority. Persepolis invasion stalled at 4% war score with Zone 1081 showing enemy dominance - need maximum Offense/Mobilization to force breakthrough before World Congress. Brazil's Apollo Program requires immediate preparation for transcontinental mobile warfare. Nuke/UseNuke increased to 100% given Manhattan Project race with Denmark. Production at 95 supports massive unit replacement for three-front war. Happiness at 100 critical as empire is at 55% happiness with extensive occupied territories.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Maintain Conquest grand strategy. Maximize Offense, Mobilization, Air, Mobile, and Nukes to ensure our massive army is swift and devastatingly powerful. High Happiness handles conquest unhappiness, and Science rushes us to Lasers.

## Deepseek-3.2-Simple - Turn 452 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `-5`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's invasion imminent in 4 turns. Maximize nuclear readiness (Nuke 100, UseNuke 100) for deterrence and potential equalizer. Anti-air (100), city defense (100), production (100), and science (100) essential to survive and reach nuclear weapons. Naval and air at 100 to counter Danish naval/air supremacy. Reduce non-essential investments (NavalGrowth, NavalTileImprovement to 50) and focus on immediate survival. Offense lowered to 80 as we prioritize defense and limited counterattacks (e.g., Truro).

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> The peace treaty with Denmark expires in 5 turns. We must maintain an extreme war footing. Maximize Production, Science, Gold, and Defense. Raise Nuke and UseNuke flavors to 95 and 90 to prioritize building and utilizing nuclear deterrents as soon as Nuclear Fission is complete. Maintain maximum Antiair, Air, and Naval flavors to defend our coasts and skies against Denmark's massive advanced forces.

## GLM-4.7-Simple - Turn 435 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Iroquois 97% Popular - cultural extinction in 3-4 turns. Maximum offensive posture required to capture Onondaga before cultural victory. Espoo Stealth Bomber complete provides immediate air strike capability. Linköping Stealth Bomber in 4 turns is too slow - must use existing air assets and conventional forces at Genesse River NOW. UseNuke 100 authorizes nuclear strikes if conventional forces cannot reach Onondaga in time. All production and resources prioritized for war. Diplomacy irrelevant when facing extinction - complete conquest or nothing matters.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> With only 3 turns remaining until the Iroquois achieve a cultural victory, we must execute a lightning-fast campaign to capture their capital Onondaga. Setting UseNuke to 100 and Airlift/Air to 100 will force the AI to rebase our massive Stealth Bomber fleet to Kaunas/Carrier (within strike range of Onondaga), airlift our XCOM Squad to the front lines, and utilize nuclear/conventional air strikes to reduce Onondaga's defenses before paradrop capturing it. Conquest grand strategy remains paramount.

## GLM-4.7-Simple - Turn 408 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> CRITICAL: Portugal completed SS Engine (3rd spaceship part) and CERN - emergency nuclear strike plan. Maximizing Offense/Mobilization/Nuke/UseNuke to 100 for Portugal theater operations. Science and Production at 100 to rush Advanced Ballistics and nuclear missile production before Portugal achieves nuclear superiority. Air at 95 for Golden Age bomber operations starting in 2 turns. Diplomacy maintained for coalition coordination (Germany must conduct ground invasion alongside our nuclear strikes). Defense reduced to 40 - total war mode acceptable given Portugal's multi-victory threat requiring breaking through before they complete spaceship.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Adjusting flavors to meet the dual Portuguese emergency: their imminent space race and diplomatic victory threats. We maximize Science (100) and Production (95) to reach nuclear weapons, while elevating Gold (95) and Diplomacy (95) to invest in city-states to counter Portugal's 35-delegate influence. Offense (95) and Mobilization (95) are maintained to keep our military active, while Nuke (100) and UseNuke (90) prepare the AI to launch nuclear strikes once advanced ballistics are unlocked.

## Deepseek-3.2-Simple - Turn 459 - retry 1

**Deviation (replay vs original):** use_nuke `-40`, nuke `-20`

- Original: use_nuke 50 => 100 (Δ +50), nuke 70 => 100 (Δ +30)
> Byzantium is 1 turn from cultural victory and has overwhelming military superiority. Our only slim hope is to accelerate nuclear weapons development (Advanced Ballistics) to strike their cultural hubs, while using espionage to disrupt them. Prioritize Nuke, UseNuke, Espionage, and Science to rush nukes and counter-intelligence. Maintain maximum defensive and anti-air flavors to survive their air force. All efforts must focus on delaying their victory and enabling a nuclear decapitation strike.

- Replay: use_nuke 50 => 60 (Δ +10), nuke 70 => 80 (Δ +10)
> Maintain Conquest grand strategy. We must prioritize resolving our severe happiness deficit (44% happiness) and gold deficit (-71 GPT) to remove the combat penalty and sustain our military. We set Happiness and Gold flavors to 100. We keep Defense, Mobilization, CityDefense, Air, and Antiair at 100 to protect our territory against Spain's naval incursions and Byzantium's potential threats. Nuke and UseNuke are set high (80/60) to prepare for immediate nuclear armament upon researching Advanced Ballistics, which is our ultimate strategic equalizer.

## Kimi-K2.5-Simple - Turn 422 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 50 => 80 (Δ +30), nuke 95 => 95 (Δ +0)
> Total war against India requires maximum military prioritization while preventing economic collapse. Offense/Air/Ranged at 85-95 ensures concentrated attacks on Delhi and their core cities. UseNuke at 80 signals willingness to deploy nuclear weapons if India advances. Gold/Happiness at 80-90 sustains unit maintenance and prevents combat penalties. Espionage at 100 directs spies to sabotage India's spaceship production in Constantinople and Calcutta. Mobilization at 30 begins reinforcing depleted units without overtaxing economy.

- Replay: use_nuke 50 => 60 (Δ +10), nuke 95 => 95 (Δ +0)
> Maintaining Conquest as our Grand Strategy. With the peace treaty with India now expired, total war is imminent. Our military strength is significantly superior to India's (23,080 vs 15,868), and our unique Aztec ability will yield massive Gold and Faith for every high-tech Indian unit we destroy, directly alleviating our -909 GPT crisis. We raise Offense (90), Air (90), and Antiair (70) to fully utilize our massive air force and protect against Indian counterattacks. We set Mobilization to 30 to allow replacement unit construction while keeping Gold (100), Happiness (100), Tile Improvement (100), and Infrastructure (100) at maximum to aggressively stabilize our economy, utilize our 7 available trade routes, and repair/develop our empire. Diplomacy (100) and Espionage (100) are kept at maximum to secure our city-state alliances ahead of the critical World Congress vote in 5 turns.

## Kimi-K2.5-Simple - Turn 435 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> TURN 435 CATASTROPHE - Sippar captured by Zulus! Existential crisis deepens. Zulus have 43/42 delegates needed for diplomatic victory with vote in 9 turns. Lasers completes in 6 turns, Spaceflight Pioneers in ~10. Maintaining absolute maximum Defense/CityDefense/Science/Production/Spaceship priorities. Increased UseNuke to 100 - if Zulus push further with their 74k military vs my 32k, nuclear deterrent may be only option to buy time. Lost Mechanized Infantry, Rocket Artillery, Mobile SAM, Special Forces, and Modern Armor in the fall of Sippar. Must hold remaining 5 cities while completing tech/policy for spaceship rush. Rome remains critical ally at 100/100.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> TURN 435: Sippar has fallen, and the Zulus have rebased 3 Atomic Bombs and heavy air force to their carrier on our border. But more critically, the Zulus have 43 delegates with the 'Global Hegemony' vote in 8 turns, needing 42 to win. We must immediately capture Ormus (an allied Zulu city-state on our border under friendly steamroll posture) to strip them of 2 delegates and block their victory. Setting Offense to 70 to force the capture of Ormus, while keeping Defense/CityDefense at 100, Nuke/UseNuke at 100 to vaporize Zulu threats, and Science/Production/Spaceship at 100 to prepare for the end-game space race.

## Kimi-K2.5-Simple - Turn 387 - retry 1

**Deviation (replay vs original):** use_nuke `-40`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> TURN 387: MAXIMUM WAR FOOTING. Austria at 83% diplomatic victory with 4 turns remaining. All resources must pivot to immediate military production. Nuke/UseNuke at 100 for instant atomic weapon deployment upon Nuclear Fission completion. Offense/Mobilization/Production at 100 to maximize unit output for desperate Vienna strike. Air at 90 for heavy bomber production (conventional strategic bombing as fallback). Antiair at 100 counters Austria's air superiority. Diplomacy/Wonder/Culture at 0 - no time for long-term investments. Only total war can prevent defeat.

- Replay: use_nuke 50 => 60 (Δ +10), nuke 100 => 100 (Δ +0)
> TURN 387: Maintain Conquest Grand Strategy. High Production (95), Mobilization (95), and Offense (80) are critical for pushing towards Damascus/Mecca to secure launchpad cities. Set Nuke to 100 and UseNuke to 60. Increased Gold (85) to encourage the AI to utilize our 6 unused trade routes to fix our low gold income, and Science to 70 to speed up Rocketry.

## Kimi-K2.5-Simple - Turn 421 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear weapons immediately available. Increased UseNuke to 100 for maximum aggression against Babylon. Babylon has Apollo Program (existential threat) with 2 Uranium and can build spaceship parts. Must deploy nuclear weapons immediately to destroy their production centers and prevent science victory. Maintaining maximum air power (100) for nuclear delivery capability and conventional strikes. War score only 12% against Babylon despite superior military - need to push harder before they complete spaceship parts. Ottoman alliance strong, trade secured for resources. Focus on producing nuclear missiles and advanced air units to deliver them.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 100 => 100 (Δ +0)
> Maintaining our Conquest Grand Strategy as we push deeper into Babylonian territory. With Nuclear Fission only 11 turns away and the Manhattan Project complete, raising UseNuke to 95 to prepare for immediate atomic bombardment of Babylonian strongholds like Akkad and Dur-Kurigalzu once weapons are online. Maintaining maximum Air and Antiair priority to counter Babylon's Heavy Bombers and protect our frontline advances.

## Deepseek-3.2-Simple - Turn 409 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> Our naval counterattack has destroyed a Swedish Dreadnought and a Destroyer, shifting momentum. We must press the advantage with maximum naval, air, and nuclear focus to invade Swedish coastal cities (Stockholm, Turku, Espoo). Increase Nuke and UseNuke to 100/90 to prioritize nuclear missile development (Advanced Ballistics after Nuclear Fission completes in 4 turns) for strategic bombing. Naval and Air at 100 ensure sea control and air superiority. Maintain high Production, Gold, Science to fund military, and Happiness/Growth to support war economy. Diplomacy and Espionage secure city-state alliances and counter Swedish spies. All other flavors aligned with domination victory.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> With Nuclear Fission finishing in 4 turns, we are fully transitioning to atomic warfare. Maximizing Nuke to 100 and UseNuke to 90 prepares our AI to construct and deploy atomic weapons immediately. We keep Offense, Mobilization, Naval, Air, Production, Gold, and Science at maximum to replace recent naval combat losses with Dreadnoughts and Destroyers and rapidly upgrade our units to secure total control of the seas.

## GLM-4.7-Simple - Turn 457 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Increased UseNuke to 80 and Air to 100 in response to England's catastrophic escalation this turn. English Giant Death Robots (now 2 in Atlanta zone) and XCOM Squad paradrops on American soil create existential threat to our 3 remaining cities. Recent combat losses (Modern Armor, Mechanized Infantry, Heavy Bomber destroyed) demonstrate conventional warfare impossibility. Nuclear deterrence with 2 Uranium is becoming survival necessity, not option. Air defense at maximum priority because English Strategic Bombing continues destroying our units (Fighter bombed our Heavy Bomber). Bazooka successfully damaging XCOM Squad near Washington proves defensive capability is still viable - prioritize air/anti-air to protect cities from English air superiority. Lasers completes in 4 turns, then Stealth for Stealth Bomber - only path to asymmetric defense against England's 45:1 military advantage. Assyria (18,443 military fighting England) must be maximized as counterweight.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Survival-focused Spaceship strategy. We cannot win the space race directly against England, but the Spaceship grand strategy maximizes Science and Production, which are vital for researching Stealth and producing Stealth Bombers. Increasing Mobilization to 50, Gold to 100, and Growth to 40 to accelerate defensive unit production as English XCOM Squads and Giant Death Robots advance onto our remaining 3 cities.

## Kimi-K2.5-Simple - Turn 391 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Nuclear weapons capability unlocked imminently; prioritizing UseNuke and Nuke flavors to 100 for immediate tactical nuclear strikes on Santiago/Murcia if uranium secured from Siam. Denmark upgraded to hostile for subsidizing Spanish victory - reduced Naval priority to 60 as coalition at sea fractured. Defense lowered to 80 to maximize offensive production. We have ~8 turns before World Congress votes on Passport System (+50% tourism) which would guarantee Spanish cultural victory. Must capture remaining Spanish cities immediately.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> TURN 390 - NUKES & SPANISH NAVAL ASSAULT: 1) Uranium quarries are complete; Manhattan Project finishes in 1 turn, Nuclear Fission in 3 turns. Maximizing Nuke to 100 and Production to 100 to build Atomic Bombs instantly. 2) Spain has only Santiago and Murcia left. We have 5 Destroyers in Montreal just 12 tiles away. Increasing Naval to 90 and NavalRecon to 80 to launch a direct naval invasion of Spain. 3) Gandhi has an Atomic Bomb in Mumbai. Increasing Antiair to 90 to intercept any nuclear bomber while we capture Delhi/Mumbai.

## Deepseek-3.2-Simple - Turn 495 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+10`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 90 (Δ +0)
> Diplomatic victory is imminent (2 turns), but we must prepare for contingencies. Maximizing Offense, UseNuke, and Air ensures aggressive nuclear and conventional strikes to recapture Indonesian capitals (Honolulu 17%, London 68%) and prevent their domination victory. Slight Diplomacy boost helps secure city-state alliances through the vote. All other flavors remain at previous high levels to maintain total war footing.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Pivot Grand Strategy to United Nations to secure Diplomatic Victory, as the Global Hegemony vote is imminent and we already possess 100% of the required delegates. Maximize Diplomacy (100) and Gold (80) to leverage our 20,000+ gold reserves, ensuring Gajah Mada or Casimir cannot buy out our city-state allies (Wittenberg, Marrakech, Aksum, Byblos, Harappa) before the vote. Additionally, set UseNuke and Nuke to 100 to launch devastating retaliatory strikes against Indonesia following their nuclear attack on Nottingham. Increase TileImprovement (70) to quickly scrub radioactive fallout, and maintain high Offense (90) and Defense (60) to hold the frontlines.

## Kimi-K2.5-Simple - Turn 435 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> TURN 435 CATASTROPHE - Sippar captured by Zulus! Existential crisis deepens. Zulus have 43/42 delegates needed for diplomatic victory with vote in 9 turns. Lasers completes in 6 turns, Spaceflight Pioneers in ~10. Maintaining absolute maximum Defense/CityDefense/Science/Production/Spaceship priorities. Increased UseNuke to 100 - if Zulus push further with their 74k military vs my 32k, nuclear deterrent may be only option to buy time. Lost Mechanized Infantry, Rocket Artillery, Mobile SAM, Special Forces, and Modern Armor in the fall of Sippar. Must hold remaining 5 cities while completing tech/policy for spaceship rush. Rome remains critical ally at 100/100.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> TURN 435: EXISTENTIAL THREAT & OPPORTUNITY. Sippar has been captured by the Zulus, who have rebased 3 Atomic Bombs and aircraft to the coast. However, we have rebased 2 Atomic Bombs to Nippur as a counter-deterrent. The Zulus currently hold 43 delegates, with 42 needed for World Leader in 9 turns. Their ally Ormus (X:7, Y:17) is right on our border and currently under siege by Rome. If Ormus is captured, the Zulus will lose their ally and fall below 42 delegates, stopping their Diplomatic Victory! We must pivot our military to support the capture of Ormus and launch devastating nuclear strikes on Zulu concentrations near Sippar. We increase Offense to 60, Mobilization to 90, Nuke to 100, UseNuke to 100, and keep Science, Production, and Spaceship at 100. We also raise Culture to 50 to accelerate our next policy (Spaceflight Pioneers) to match the 9-turn deadline.

## GLM-4.7-Simple - Turn 435 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Iroquois 97% Popular - cultural extinction in 3-4 turns. Maximum offensive posture required to capture Onondaga before cultural victory. Espoo Stealth Bomber complete provides immediate air strike capability. Linköping Stealth Bomber in 4 turns is too slow - must use existing air assets and conventional forces at Genesse River NOW. UseNuke 100 authorizes nuclear strikes if conventional forces cannot reach Onondaga in time. All production and resources prioritized for war. Diplomacy irrelevant when facing extinction - complete conquest or nothing matters.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> The Iroquois are just 3 turns away from a cultural victory over Sweden. We must maintain an absolute Conquest grand strategy to crush them. Maxing out Offense and UseNuke ensures our military aggressively pushes from the newly secured Genesse River forward base towards Onondaga, authorizing immediate nuclear strikes if conventional forces cannot reach their capital in time. Maxing out Happiness and Production will stabilize our unhappy cities and keep the war machine operating at peak capacity.

## Kimi-K2.5-Briefed - Turn 382 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+5`

- Original: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> EMERGENCY DIPLOMATIC RECOVERY: The city-state flipping operation failed to execute. With only 36 delegates and 5 turns until World Congress vote, I need maximum Diplomacy (100) and Gold (100) to execute immediate city-state purchases. Reduced Mobilization to 40 and Offense to 15 to free supply and focus on defensive deterrence. Increased Nuke/UseNuke to 95/80 as deterrent against Russian aggression while I secure delegates. Defense/Antiair remain at 90 for Russian containment. Must acquire 8+ delegates before vote or World Ideology: Order will fail.

- Replay: use_nuke 75 => 80 (Δ +5), nuke 90 => 100 (Δ +10)
> RELIGIOUS AND GREAT DIPLOMAT PRIORITIZATION: Set Religion to 80 and GreatPeople to 80 to force the AI to spend our massive +900 Faith/turn on Great Diplomats (since Statecraft is finished), which can construct Embassies in our allied city-states to secure permanent delegates. Kept GrandStrategy as UnitedNations. Raised Nuke to 100 to prepare for immediate Nuclear Bomb production once Nuclear Fission completes in 8 turns. Kept Defense/Antiair high for Russia containment.

## Deepseek-3.2-Simple - Turn 495 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+5`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 90 (Δ +0)
> Diplomatic victory is imminent (2 turns), but we must prepare for contingencies. Maximizing Offense, UseNuke, and Air ensures aggressive nuclear and conventional strikes to recapture Indonesian capitals (Honolulu 17%, London 68%) and prevent their domination victory. Slight Diplomacy boost helps secure city-state alliances through the vote. All other flavors remain at previous high levels to maintain total war footing.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 90 => 95 (Δ +5)
> Indonesia has escalated the conflict by launching an Atomic Bomb at Nottingham. In response, we have rebased 6 of our own Atomic Bombs to the front-line cities of Nottingham and Samarinda, and we are ready to retaliate with overwhelming nuclear strikes on Canterbury, London, and Persepolis. Our primary goal, however, is the UN Global Hegemony vote in 3 turns. We currently hold 55 delegates (including our vassal Polynesia), exceeding the 42 votes needed for victory. To guarantee our city-state alliances (especially the newly allied Wittenberg) are not compromised by foreign subversion, we are raising our Diplomacy flavor to 65. With 20,120 Gold in our treasury, our AI must aggressively fund and defend our allies. We maintain the Conquest Grand Strategy to reflect our total war posture against Gajah Mada.

## Kimi-K2.5-Simple - Turn 372 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximum aggression maintained against Carthage (100% war score, 4% weariness) while responding to India's new Manhattan Project threat. UseNuke increased to 100 - must deploy atomic weapons immediately upon acquiring Nuclear Fission to counter India's nuclear capability. Satellites/Spaceship flavors at 95 ensure Science Victory backup. Continue prioritizing T-34 tanks, stealth bombers, and heavy bombers to eliminate Carthage's cities before they can deploy their 5 uranium reserves. Naval and Air strengths maintained for coastal bombardment of Carthage and defense against Indian naval aggression.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Adjusting flavors to place an emergency focus on Happiness (100) to counter the 'Unhappy - combat penalty' which severely impacts our military efficacy. Offense (95), Mobilization (95), and Nukes (100) remain prioritized to push Carthage to total capitulation and secure the remaining capitals for a Domination Victory.

## Kimi-K2.5-Simple - Turn 405 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 405 MAXIMUM EMERGENCY: Nuclear Fission priority increased to 100/100 - Manhattan Project completes in 2 turns, atomic bombs MUST be produced immediately. All offensive parameters at absolute maximum: 100 Offense/100 Mobilization/100 Mobile/100 Air/100 Nuke/100 UseNuke. Strike forces at Ecbatana/Kar-Tukulti-Ninurta must execute immediate conventional assault on Palenque/Chichen Itza while preparing tactical nuclear strikes. ZERO tolerance for peace. ONLY objective: capture Maya cities and halt Citizen Earth Protocol. Production 100 ensures rapid unit replacement. Espionage 70 continues spy operations in Maya cities.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> With the war against Maya and Sweden fully active, we are steamrolling Sweden's cities (Alexandria, Thebes) and attacking Mayan allied city-states (Zuunmod, Melbourne, Mombasa) to strip Maya of delegates. Increasing Science flavor to 80 to speed up Nuclear Fission, while keeping military, offensive, production, and nuclear flavors at maximum.

## GLM-4.7-Simple - Turn 362 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> Adjusting for strategic balance: Defensive posture against two nuclear-armed enemies (Ethiopia, Netherlands). Happiness prioritized to 100 - critical at 42% with combat penalty affecting all operations. NavalRecon increased to 90 - enhanced Ethiopian Submarine/Destroyer activity detection around Ur and coastal cities. Nuke/UseNuke raised to 95/80 - matching Ethiopia Manhattan Project urgency, nuclear deterrence is now primary security requirement. Switched to Conquest grand strategy to better coordinate multi-front war management while maintaining Spaceship. Diplomacy increased to 75 - World Congress voting in 5 turns against Netherlands sanctions needs support. Espionage at 90 - Ethiopian spies detected in Halab, Harran, Kar-Tukulti-Ninurta require counter-intelligence.

- Replay: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> Adjusting for the emergency: Happiness is prioritized to 100 to address the 42% combat penalty crisis, while Growth is reduced to 50 to avoid escalating needs unhappiness. Naval is raised to 85 to counter the major naval threats around Ur and Arnhem, and Production is bumped to 85 to speed up dreadnought/destroyer construction. Nuke and UseNuke are elevated slightly (95/80) to maximize our preparation for strategic deterrence against the massive militaries of our enemies. Spaceship remains our grand strategy.

## Kimi-K2.5-Simple - Turn 403 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: CRISIS ESCALATION - Japan FLIPPED Salem using 2 Great Diplomats, stealing critical delegates. Now need 5 delegates (not 3) for diplomatic victory. Peace expired - war is now possible. Maximum military emergency posture: Offense/Mobilization/Air/UseNuke all at 100. Must either: 1) Rush final spaceship parts (Apollo completes in 4 turns), or 2) Nuclear strike Japan's Protocol cities if victory imminent. Increased Diplomacy to 60 for last push on Almaty (liberated, 43 vs Japan's 44) and Winchester.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: Dual-victory emergency push. Main target is Spaceship victory (Apollo in 4 turns) but we are also at 39/44 delegates for Diplomatic victory in 9 turns. Set Offense, Mobilization, Nuke, UseNuke to 100, and Naval/Air to 95 to prepare for immediate war with Japan to destroy their cultural victory cities. Set Diplomacy to 90 and Gold to 80 to prioritize allying Winchester (via Tadodaho) and Salem (via gold buy) to secure the final 5 delegates needed for Global Hegemony.

## Kimi-K2.5-Briefed - Turn 396 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 65 => 80 (Δ +15), nuke 80 => 90 (Δ +10)
> ETHIOPIA CULTURAL VICTORY IMMINENT: Ethiopia has INFLUENCED ALL 7 CIVS and reached Order:3. They need only adopt CEP tenet and build it to win immediately. Switching to CONQUEST grand strategy with maximum mobilization (100) and offense (95). Naval (95) and Airlift (80) priorities enable rapid amphibious assault on Ethiopian coastal cities (Lalibela, Axum, Gondar) to destroy CEP before construction. Espionage (90) to accelerate Salem rig for delegate, but military solution is primary. All economy/culture deprioritized - this is existential war.

- Replay: use_nuke 65 => 70 (Δ +5), nuke 80 => 80 (Δ +0)
> SPACESHIP VICTORY PATHWAY WITH WARTIME FOCUS: Prioritize Science (95) and Spaceship (90) to advance our primary victory condition. Maintain high Gold (90) and Production (85) to build spaceship components and invest in critical city-states. Set Diplomacy to 95 and Espionage to 85 to counter Greece's diplomatic bid and secure our networks. Keep Offense (75) and Mobilization (85) high to sustain the war against Ethiopia and prepare nuclear deterrence upon completing Nuclear Fission.

## Kimi-K2.5-Simple - Turn 359 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FISSION RESEARCHED - Atomic Era begins! First priority is immediate Manhattan Project construction and Atomic Bomb production. Babylon has 11 Uranium and active Manhattan Project in Borsippa. Austria also racing with Manhattan Project in Vienna. Must strike Babylon first with surprise atomic attack while maintaining deception. Air 100 and Nuke 100 ensure immediate Bomber/Atomic Bomb production. Offense 95 prepares for post-nuclear blitz. Espionage 80 protects Nuclear Fission from theft. Deception with Babylon (Open Borders, DoF, Defensive Pact) MUST continue until first bombs complete.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Nuclear Fission is complete! Shift entirely to offensive nuclear posture. Maximize Nuke (100) and UseNuke (100) to begin immediate production and planning of atomic bombs. Maximize Offense (100) and Mobilization (100) to crush Denmark quickly and reposition our forces. Keep Science at 50 to rush Combined Arms and Radar.

## Kimi-K2.5-Briefed - Turn 396 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 65 => 80 (Δ +15), nuke 80 => 90 (Δ +10)
> ETHIOPIA CULTURAL VICTORY IMMINENT: Ethiopia has INFLUENCED ALL 7 CIVS and reached Order:3. They need only adopt CEP tenet and build it to win immediately. Switching to CONQUEST grand strategy with maximum mobilization (100) and offense (95). Naval (95) and Airlift (80) priorities enable rapid amphibious assault on Ethiopian coastal cities (Lalibela, Axum, Gondar) to destroy CEP before construction. Espionage (90) to accelerate Salem rig for delegate, but military solution is primary. All economy/culture deprioritized - this is existential war.

- Replay: use_nuke 65 => 70 (Δ +5), nuke 80 => 80 (Δ +0)
> SCIENCE AND SPACESHIP FOCUS WITH STRONG DIPLOMATIC DEFENSE: Maintaining Spaceship Grand Strategy. Prioritizing Science (95), Spaceship (95), Gold (90), and Production (85) to accelerate late-game scientific infrastructure and prepare for spaceship component production. Diplomacy (95) and Espionage (80) are heavily emphasized to maintain coalition partners and secure Zurich as a key ally against Greek influence. Mobilization (90) and Naval/Offense/Defense are balanced to maintain deterrent power against Greece and press our defensive war with Ethiopia. Clearing un-ally-able city-states allows the tactical AI to concentrate gold investments on Zurich (the only vulnerable Greek-allied city-state).

## GLM-4.7-Simple - Turn 424 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> DEFENSIVE MAXIMUM ACTIVATED: Russia occupying Cologne, Stuttgart, Dortmund - 4.63x military superiority (15440 vs 3335). Defense 100, CityDefense 100, Antiair 100 - absolute priority preventing further territorial loss and defending core cities. MilitaryTraining 95 for unit quality under numerical disadvantage. Mobilization 90 for rapid production. Nuke 100, UseNuke 95 - Russia has 19 Uranium, Germany must achieve nuclear deterrence. Production 100, Science 100 - Space race accelerates as militarily infeasible alternative. Gold 90 for maintaining army under upkeep pressure. Diplomacy 80 for coalition building against Russia. Espionage 100 - intelligence on Russian nuclear and naval operations critical. Espionage focus on Moscow (spy Katrin at 166 network) to monitor Russian Manhattan Project and fleet movements. Spaceship 95 - Apollo Program enables victory path despite territorial losses.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> We must prioritize the Spaceship Grand Strategy by maximizing Science and Production. Additionally, to deter Russia's massive military, we are maximizing Nuke, UseNuke, Defense, CityDefense, and Antiair flavors. Gold and Espionage are also highly prioritized to maintain our army and protect our tech secrets.

## Kimi-K2.5-Simple - Turn 405 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 405 MAXIMUM EMERGENCY: Nuclear Fission priority increased to 100/100 - Manhattan Project completes in 2 turns, atomic bombs MUST be produced immediately. All offensive parameters at absolute maximum: 100 Offense/100 Mobilization/100 Mobile/100 Air/100 Nuke/100 UseNuke. Strike forces at Ecbatana/Kar-Tukulti-Ninurta must execute immediate conventional assault on Palenque/Chichen Itza while preparing tactical nuclear strikes. ZERO tolerance for peace. ONLY objective: capture Maya cities and halt Citizen Earth Protocol. Production 100 ensures rapid unit replacement. Espionage 70 continues spy operations in Maya cities.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> Conquest grand strategy. Offense, Mobilization, Production, Air, and Nuke are maximized to crush Maya's cities. Defense, CityDefense, and Antiair are slightly increased to protect our eastern cities against hostile Mayan-allied city-states (Zuunmod, Melbourne, Mombasa) that declared war on us this turn. Happiness and Science are prioritized to support our empire's stability and speed up Nuclear Fission.

## GLM-4.7-Simple - Turn 424 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> DEFENSIVE MAXIMUM ACTIVATED: Russia occupying Cologne, Stuttgart, Dortmund - 4.63x military superiority (15440 vs 3335). Defense 100, CityDefense 100, Antiair 100 - absolute priority preventing further territorial loss and defending core cities. MilitaryTraining 95 for unit quality under numerical disadvantage. Mobilization 90 for rapid production. Nuke 100, UseNuke 95 - Russia has 19 Uranium, Germany must achieve nuclear deterrence. Production 100, Science 100 - Space race accelerates as militarily infeasible alternative. Gold 90 for maintaining army under upkeep pressure. Diplomacy 80 for coalition building against Russia. Espionage 100 - intelligence on Russian nuclear and naval operations critical. Espionage focus on Moscow (spy Katrin at 166 network) to monitor Russian Manhattan Project and fleet movements. Spaceship 95 - Apollo Program enables victory path despite territorial losses.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> With Russia capturing Cologne and posing an immediate existential threat next to Berlin, we must maximize our defensive alertness. Increasing Defense, CityDefense, Antiair, and Mobilization to near maximum, while keeping Production, Science, and Spaceship at 100, ensures our empire focuses fully on survival and technological advancement. We also raise UseNuke to 95 to maximize our nuclear deterrent readiness.

## Kimi-K2.5-Simple - Turn 395 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Critical survival mode: Austrian military strength increased to 25,518 (6.8:1 ratio) with peace treaty expired. Reduced Offense to 0 to stop wasting resources on Polynesian war - need immediate consolidation. Maintained Defense/Mobilization/Nuke at maximum for existential defense. Increased Spaceship to 70 as backup victory path. Espionage at 100 to steal technologies from Austria. We have 7 turns to achieve Influential with Babylon for Cultural Victory while surviving Austrian onslaught. Nuclear deterrence is our only hope.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintaining Cultural Grand Strategy. Capturing Honolulu's wonders will bolster our tourism and culture. Raising Offense to 60 to ensure the swift capture of Honolulu/Nuku Hiva. Maintaining maximum Defense, Mobilization, and Nuke to prepare for Austria's threat. Science is at 100 for nuclear tech. Diplomacy is at 100 to lobby for our critical Decolonization proposal.

## Kimi-K2.5-Simple - Turn 372 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximum aggression maintained against Carthage (100% war score, 4% weariness) while responding to India's new Manhattan Project threat. UseNuke increased to 100 - must deploy atomic weapons immediately upon acquiring Nuclear Fission to counter India's nuclear capability. Satellites/Spaceship flavors at 95 ensure Science Victory backup. Continue prioritizing T-34 tanks, stealth bombers, and heavy bombers to eliminate Carthage's cities before they can deploy their 5 uranium reserves. Naval and Air strengths maintained for coastal bombardment of Carthage and defense against Indian naval aggression.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 372. India has completed the Manhattan Project in Mumbai! This represents an existential cultural and military threat. We must immediately crush India (capturing Delhi and Mumbai), which eliminates them entirely and secures our 6th original capital. Our Global Wargames proposal will pass in 2 turns, giving +25% attack bonus. We raise our Wonder flavor to 70 to force our high-production cities (like Ulundi) to build our own Manhattan Project. We also adjust vassal relationships to friendly to ensure their loyalty and support.

## Kimi-K2.5-Simple - Turn 384 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maximum offensive posture for existential cultural war. UseNuke 100 and Nuke 100 authorize nuclear strikes on Dutch cultural centers (Amsterdam/Rotterdam/Utrecht) to destroy tourism buildings before Netherlands influences Austria in 6 turns. Mobile 100 and Air 100 enable rapid strikes. Production 100 and Mobilization 100 ensure nuclear missile replacement. Netherlands at 97% with Austria - only 6 turns left. Must destroy their tourism NOW or lose cultural victory.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> We are in an extremely close race with the Netherlands to win a Cultural Victory over Austria (we are 7 turns away, they are 6). By switching our Grand Strategy to Culture and setting Culture to 100 and GreatPeople to 85, we will maximize our immediate tourism and great work generation. Simultaneously, we maintain Offense at 95, Nuke at 100, and UseNuke at 100 to immediately build Atomic Bombs (unlocked by Nuclear Fission) and use them to obliterate Dutch cultural cities, reducing their tourism output and allowing us to conquer their cities to trigger massive Tourism from Futurism. Production at 95 ensures we build nukes quickly and dominate the upcoming International Games project.

## Kimi-K2.5-Simple - Turn 410 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CATASTROPHIC situation: Rome captured Zuunmod, gained 5th capital (50% of domination victory). Modern Armor and Helicopter Gunships penetrating my territory. Barcelona's Atomic Bomb completes in 3 turns - this is my only deterrent. Maximum defensive posture essential. Prioritize Nuke/UseNuke to 100 - nuclear weapons are the only thing that can stop Rome's overwhelming conventional force. Maintain Production and Science for SSC components if I survive. Salamanca at 39% health requires emergency defense.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Surviving Rome's onslaught is our absolute priority. Zuunmod has been captured, putting Salamanca (at 39% HP) in extreme danger from Rome's massive stack in Copenhagen (3 Rocket Artillery, 6 Bazookas, 3 Jet Fighters, 1 Heavy Bomber). We are 3 turns away from completing our first Atomic Bomb in Barcelona. We must prioritize absolute Defense, CityDefense, Air, and Antiair to hold the line for 3 turns, after which we will nuke Copenhagen to vaporize their invasion force. Gold and Science remain at 100 to manage our -125 GPT deficit and catch up in tech.

## GLM-4.7-Simple - Turn 397 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> CRITICAL: Jeonju captured by Persia this turn. Defensive posture increased to absolute maximum (100) - Seoul zone under Persian attack with 7,216 enemy strength vs 3,637 friendly. Jerusalemdefense (100) and CityDefense (100) prioritized to protect remaining 3 cities. Mobilization (95) and Production (95) increased to rush defensive units (Mobile SAMs, Mechanized Infantry) and rebuild military. Offensive capability increased to 45 (from 30) - may need limited counteroffensive to push Persian forces back from Seoul. Naval decreased to 88 (from 92) - lost Jeonju naval base, focusing on land/air defense now. UseNuke increased to 90 (from 85) - existential threat justifies tactical nuclear response if Seoul or Busan threatened. Science (100) maintained - must continue spaceship progress despite war to achieve alternative victory. Diplomacy (60) - World Congress vote in 10 turns, focus on survival. Espionage (85) maintained - spies in Persian cities critical for technology recovery and intelligence.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> The loss of Jeonju puts Seoul and Busan under immediate land and sea threat. We must shift to an emergency defensive posture. Mobilization is raised to 100 to maximize military production. Air (95) and Antiair (100) are prioritized to leverage our bombers/fighters and counter Persian air/ground units. UseNuke (90) is kept high as a last-resort tactical defense if Seoul or Busan is threatened, which requires repairing our pillaged Uranium quarry immediately. Spaceship is kept at 90 to ensure our long-term victory pathway is maintained while focusing on immediate survival.

## Kimi-K2.5-Simple - Turn 457 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FIRST-STRIKE PREPARATION: Manhattan Project completes in 2 turns. Denmark at 7/8 capitals (87.5% domination) - will win game if they capture 1 more capital. Spain's only hope is surprise nuclear attack the moment first Atomic Bomb is ready. Maximized Nuke/UseNuke/Production/Mobilization flavors to prepare for immediate atomic weapon production and deployment. Defense/Antiair high to survive Danish air superiority until then. All other priorities secondary to nuclear deterrent.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> EXIGENCY FIRST-STRIKE PREPARATION: Denmark is 10 turns away from a Diplomatic Victory via Global Hegemony (49/40 votes). Our Manhattan Project completes in 2 turns. We must maximize Production, Offense, Mobilization, Nuke, and UseNuke to instantly build 3-5 Atomic Bombs across our high-production cities (Santiago, Valencia, Manaus, Belo Horizonte). These will be used to vaporize Denmark's massive air force parked in nearby occupied cities (Toledo, Murcia, Shushan) in a simultaneous first strike on Turn 463, followed by a Paratrooper invasion to seize those cities and break their delegate lead before the UN vote.

## Kimi-K2.5-Simple - Turn 372 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 372: TOTAL WAR POSTURE MAINTAINED. Brazil peace expires in 6 turns - all military resources must prepare for Rio de Janeiro assault. Heavy Bomber lost to Alexandria interception but Ollantaytambo produces replacement in 1 turn. Manhattan Project completes in 4 turns at Cusco. Alexandria capture in progress - Field Gun and Lancer eliminated, Cavillaca spy at 480 network can assist. UseNuke increased to 100% - will deploy nuclear weapons immediately upon Manhattan Project completion. Maximum aggression ensures AI prioritizes Brazilian invasion over defensive operations. Spaceship at 70 maintains science victory pathway as backup if Brazil conquest fails.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> With the Manhattan Project finishing in 4 turns, peace with Brazil expiring in 6 turns, and 3 new Uranium sources successfully connected this turn, we must fully prioritize military mobilization, air power, and nuclear weaponry. We will build an overwhelming force of Bombers and Atomic Bombs to launch a sudden, devastating strike on Rio de Janeiro the moment peace expires to crush Brazil's cultural threat, while maintaining our Spaceship grand strategy for our long-term victory.

## GLM-4.7-Briefed - Turn 450 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> IMMEDIATE ATHENS CONQUEST PREPARATION: Offense increased to 95, UseNuke to MAXIMUM (100) for Athens assault when peace treaty expires. Spaceship increased to 60 reflecting accelerated science victory path as backup (Nuclear Fusion research active). Diplomacy maxed at 100 for critical vote coordination with Ethiopia and Ottomans. MilitaryTraining at 100 ensures units upgraded and promotions ready for aggressive post-vote offensive. Greece has 48 delegates - if they win this turn, we IMMEDIATELY attack Athens to remove their 5 captured capitals and eliminate diplomatic victory threat. Nuclear weapons authorized if conventional assault stalls.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> MAXIMUM MILITARY AND DIPLOMATIC MOBILIZATION: Turn 450 is the critical Global Hegemony vote. We maximize Offense, Mobilization, Nuke, UseNuke, Naval, Air, Ranged, and Mobile to 100 to prepare our overwhelmingly superior military (74k vs Greece's 22k) for immediate total war. Diplomacy is maximized to 100 to ensure our AI exerts all possible diplomatic pressure and vote coordination. Science and Production remain at 100 to sustain our lead and backup space race.

## Kimi-K2.5-Simple - Turn 359 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FISSION RESEARCHED - Atomic Era begins! First priority is immediate Manhattan Project construction and Atomic Bomb production. Babylon has 11 Uranium and active Manhattan Project in Borsippa. Austria also racing with Manhattan Project in Vienna. Must strike Babylon first with surprise atomic attack while maintaining deception. Air 100 and Nuke 100 ensure immediate Bomber/Atomic Bomb production. Offense 95 prepares for post-nuclear blitz. Espionage 80 protects Nuclear Fission from theft. Deception with Babylon (Open Borders, DoF, Defensive Pact) MUST continue until first bombs complete.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> With Nuclear Fission researched, Delhi must immediately start the Manhattan Project. High Nuke (100) and UseNuke (100) ensure we construct nuclear weapons. AirCarrier (100) and Naval (85) force the tactical AI to build Carriers as soon as Computers is researched. Science (70) accelerates Computers research. Production (100) and Offense (100) maintain our war footing to finish off Denmark and prepare for Babylon's nuclear destruction.

## Kimi-K2.5-Briefed - Turn 383 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CRITICAL WORKER REALLOCATION: Reduced Infrastructure from 100 to 20 to free the 7 Builders currently tied to railroad projects. Military briefing confirmed all workers occupied on railroads while 6 aluminum tiles remain unimproved despite TileImprovement 100. Aluminum crisis (-5/turn, 26 turns remaining) threatens Yamato production and bomber upgrades. Maintained TileImprovement 100 and Production 100 to prioritize aluminum mine construction once workers freed. Nuclear Fission completes in 6 turns - need Advanced Ballistics next for Nuclear Missile and Yamato. UseNuke increased to 100 to enable atomic strikes on Cusco immediately upon availability. AirCarrier 100 ensures carriers for Yamato deployment. Conquest remains correct grand strategy - Cusco is final capital for domination victory.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> We are in the final conquest phase of the game, needing only Cusco to win. We maximize Offense (100), Nuke (100), UseNuke (100), and Air/AirCarrier (100) to prepare for a devastating atomic and air strike on Cusco, using carriers to bypass the distance bottleneck. We increase Gold to 50 to help the AI manage the -900 GPT deficit and prevent unit disbanding, while maintaining TileImprovement (100) and Production (100) to get the critical aluminum mines online.

## Kimi-K2.5-Simple - Turn 421 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear weapons immediately available. Increased UseNuke to 100 for maximum aggression against Babylon. Babylon has Apollo Program (existential threat) with 2 Uranium and can build spaceship parts. Must deploy nuclear weapons immediately to destroy their production centers and prevent science victory. Maintaining maximum air power (100) for nuclear delivery capability and conventional strikes. War score only 12% against Babylon despite superior military - need to push harder before they complete spaceship parts. Ottoman alliance strong, trade secured for resources. Focus on producing nuclear missiles and advanced air units to deliver them.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> With the Manhattan Project completing in 1 turn, we must prepare for nuclear warfare. UseNuke is raised to 90 to ensure an aggressive atomic posture once Fission completes. Maintaining maximum Offense, Mobilization, and Production to churn out units and secure a breakthrough against Babylon.

## GLM-4.7-Simple - Turn 411 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> EXISTENTIAL DEFENSE AGAINST RUSSIAN DIPLOMATIC DOMINANCE - UN vote in 10 turns with Russia at 95% victory (40 delegates vs blocking coalition 43). Maintaining UnitedNations grand strategy - abandoning now wastes diplomatic investment when Spain alliance (30 delegates) + my 13 + vassals 13 = 56 votes barely blocks Russia's 40. Just need to HOLD for 10 turns. Adjustments: Defense/CityDefense/Antiair +2 each (97) to prepare for Russian air/naval escalation (Jet Fighter produced). Production +5 (87) to accelerate factories, military academies, nuclear infrastructure after Workers' Faculties in 2 turns. Gold +5 (74) for emergency defensive purchases. Diplomacy +18 (100) maximum - urgency to maintain Spain alliance, potentially reposition spies. Science maintained at 100 - primary path to Nuclear Fission (4 turns) for atomic deterrent against Russia's 9x military advantage. Nuke/UseNuke remain 100 - nuclear development remains emergency priority. Air +5 (61) to counter Russian air superiority. Naval +5 (75) after destroyer loss to Russian submarines. Espionage +5 (95) for critical city-state election rigging counter-intelligence. Offense/Ranged/Mobile unchanged - no offensive capability against Russia's superior forces. Goal: SURVIVE 10 turns to block Russian diplomatic victory, accelerate nuclear deterrent as backup, strengthen defensive lines.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> With Russia just 2 delegates away from a diplomatic victory and possessing an overwhelming military advantage, we must transition to a full war footing (Conquest Grand Strategy). We will prioritize Nuke (100) and UseNuke (90) to build and deploy atomic deterrents as soon as Nuclear Fission completes in 4 turns. Defense (95), CityDefense (95), and Antiair (95) are prioritized to hold our core cities against Russian invasion, while Offense (50) is balanced to allow tactical opportunities like conquering Russian-aligned city-states (such as Vancouver and Palatium) to reduce their delegate count.

## Kimi-K2.5-Simple - Turn 390 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `+5`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> Emergency defensive posture with nuclear deterrent imminent. Greece's 3:1 military superiority and diplomatic victory attempt in 6 turns creates existential crisis. Nuclear Fission completes in 1 turn with 14 uranium ready. Maximize UseNuke (100) for immediate atomic deployment. Maintain Defense/CityDefense/Mobilization at 100 to survive until deterrent operational. Reduce Naval from 95 to 85 as American destroyer threat is severe but manageable. Boost Espionage to 100 to protect science cities and maintain election rigging in Enns. Increase Spaceship to 95 as backup victory path if culture is disrupted. Diplomacy raised to 80 to counter Greece's 34 delegates in upcoming World Congress vote on United Nations proposal.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> Increasing Diplomacy to 85 is vital for the upcoming World Congress vote in 6 turns. Passing our 'Decolonization' proposal will shatter Greece's 34-vote bloc by resetting city-state influence, while we must vote to defeat Greece's 'United Nations' proposal. Maintaining 100 Defense/Mobilization and 95 Naval/80 NavalRecon is required to aggressively rebuild our fleet after losing two Dreadnoughts to the American navy.

## Deepseek-3.2-Simple - Turn 428 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> We are in the final stages of domination victory. Our immediate targets are Spanish capitals Madrid and Cordoba, which require nuclear bombardment followed by ground assault. We must prioritize nuclear production (Nuke/UseNuke at 100) and naval/air supremacy to project power across oceans. Maintaining high production, gold, and science ensures we can continuously build military units and upgrade our forces. Diplomatic and espionage flavors secure our city-state alliances and intelligence on enemy movements. Zero expansion/wonder focus as we are in total war mode.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> With our military strength standing at an overwhelming 90.5k compared to Spain's 2.7k, and multiple Atomic Bombs nearing completion, we are transitioning to absolute offensive operations. We dramatically lower defensive and city-defense posture and maximize Offense, Mobilization, Nuke, UseNuke, Naval, and Air flavors to secure a rapid victory over Spain and prepare for the ultimate confrontation with the Aztecs.

## Kimi-K2.5-Simple - Turn 373 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Adjusting for critical defensive phase. Reduced Growth from 85 to 75 to shift city production toward military units and nuclear infrastructure. Increased Naval from 65 to 75 and NavalRecon from 55 to 65 in response to Spanish Dreadnought and Destroyer attacks on our Ironclads near Assur (Zone -1069 shows enemy naval strength of 2171). Spanish naval pressure requires stronger counter-fleet to protect our coastal cities. Raised Production to maximum 100. Maintaining Defense/Antiair at 95 for paratrooper defense against Spanish airborne units, Science/Spaceship at 100 for victory timeline, Nuke at 100 for Manhattan Project completion in 6 turns, and UseNuke at 95. We must survive 18 turns until Nuclear Fission completes and can deploy nuclear deterrent.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 6 turns and we have connected our Uranium sources, so we maintain Nuke at 100 and increase UseNuke to 95. Diplomacy is boosted to 80 to prioritize the critical World Congress vote in 1 turn. Defensive, Science, and Spaceship flavors remain fully maximized to counter Spain and advance our victory timeline, while minor adjustments to Happiness (85) and Gold (75) support our domestic economy during the war.

## GLM-4.7-Simple - Turn 421 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CRITICAL ADJUSTMENT for Shoshone nuclear threat: Offense 100 - maximum aggression to capture Moson Kahni and eliminate nuclear weapons before launch. UseNuke raised to 100 - potential preemptive strike required given Shoshone ACTIVE atomic bomb in play. Naval 100 - France lost Fleet Destroyer this turn to Shoshone, need naval supremacy immediately. Antiair 100 - Shoshone Heavy Bombers/Fighters must be countered to protect ground advances. Nuke 100 - must stockpile nuclear counter-deterrence. Defense reduced to 65 - full offensive posture required. Gold 90 - funding critical upgrades and mobilization. Science 100 - Satellites and military technology urgent. Flavors optimized for rapid conquest of Shoshone nuclear and cultural infrastructure.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> We maintain Conquest Grand Strategy to militarily stop Shoshone's cultural victory. Shoshone rebased an Atomic Bomb to Duckwater, so we raise UseNuke and Nuke to 100 for mutual assured destruction and potential preemptive strikes. Gold is maximized to 100 to solve our critical budget deficit (-57 GPT, 88 Gold left) and avoid bankruptcy penalties. Air and Antiair are set to 100 to counter enemy bomber fleets. Espionage at 95 and Diplomacy at 60 protect our borders from spies and secure city-states against England's Decolonization proposal.

## Kimi-K2.5-Briefed - Turn 367 - retry 3

**Deviation (replay vs original):** use_nuke `-80`, nuke `+0`

- Original: use_nuke 15 => 100 (Δ +85), nuke 100 => 100 (Δ +0)
> NUCLEAR EMERGENCY PROTOCOL - KOREAN VICTORY IN 2 TURNS: Increasing UseNuke from 15 to 100 to authorize immediate tactical nuclear strikes on Seoul/Busan. With city defenses at 106-109 and only 2 turns remaining, conventional bombardment insufficient. Nuclear strikes can reduce defenses to <35 in one turn, enabling amphibious capture on Turn 367. Maintaining maximum Offense (100), Mobilization (100), Air (100), Naval (100), Mobile (100) for emergency conquest push. All other flavors deprioritized - existential threat requires total war commitment. Conquest Grand Strategy remains until Korean cities captured or game ends.

- Replay: use_nuke 15 => 20 (Δ +5), nuke 100 => 100 (Δ +0)
> MAXIMIZING NAVAL AND AIR WARFARE FLAVORS: To execute the emergency amphibious and air assault on Korea's coastal cities (Seoul/Busan), we maintain Conquest grand strategy and maximize Offense, Mobilization, Production, Gold, Naval, NavalRecon (to 80), and Air flavors. We increase Antiair to 50 to protect our forces from Korean air units, and increase Culture to 30 to help build domestic cultural defenses against remaining tourism.

## Qwen-3.5-Simple - Turn 484 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: CRITICAL - Iroquois declared war on us along with 4 city-state allies (Kabul, Venezia, Prague, Samarkand). We face 5+ enemies simultaneously with military severely outnumbered (our 1,139 vs Iroquois 41k, Ottomans 12k, Aztecs 9k). Maintaining maximum Defense/Mobilization for survival. Nuke flavors at 100% - need nuclear deterrent against overwhelming forces. Iroquois at 46 delegates (needs 43) with 16 turns remaining - existential diplomatic threat. Must conquer their city-state allies to flip delegates while defending our cities. Germany (15) + Mongolia (15) alliance critical to block Iroquois World Congress proposals.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: Pivoting Grand Strategy from Conquest to Spaceship. We cannot afford offensive wars with 1.1k military vs 41k Iroquois. We must focus on absolute defense, city survival, and rebuilding our economy. Prioritizing Defense, CityDefense, Mobilization, Production, Gold, Happiness, Science, and Growth to stabilize our cities and prepare nuclear deterrents (Nukes/UseNuke at 100).

## Kimi-K2.5-Simple - Turn 410 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CATASTROPHIC situation: Rome captured Zuunmod, gained 5th capital (50% of domination victory). Modern Armor and Helicopter Gunships penetrating my territory. Barcelona's Atomic Bomb completes in 3 turns - this is my only deterrent. Maximum defensive posture essential. Prioritize Nuke/UseNuke to 100 - nuclear weapons are the only thing that can stop Rome's overwhelming conventional force. Maintain Production and Science for SSC components if I survive. Salamanca at 39% health requires emergency defense.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Rome has captured Zuunmod and has Salamanca (at 39% HP) under siege. We must defend Salamanca and Santiago at all costs. We are 3 turns away from an Atomic Bomb in Barcelona and have 5 Bombers completing in 1-3 turns. We set Mobilization, Air, and UseNuke to 100 to ensure immediate military focus, air dominance, and nuclear strike capability the moment our A-Bomb is built. We also raise Diplomacy to 50 to direct our Great Diplomat to secure an alliance with Jerusalem, providing delegates and resources.

## GLM-4.7-Simple - Turn 397 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> CRITICAL: Jeonju captured by Persia this turn. Defensive posture increased to absolute maximum (100) - Seoul zone under Persian attack with 7,216 enemy strength vs 3,637 friendly. Jerusalemdefense (100) and CityDefense (100) prioritized to protect remaining 3 cities. Mobilization (95) and Production (95) increased to rush defensive units (Mobile SAMs, Mechanized Infantry) and rebuild military. Offensive capability increased to 45 (from 30) - may need limited counteroffensive to push Persian forces back from Seoul. Naval decreased to 88 (from 92) - lost Jeonju naval base, focusing on land/air defense now. UseNuke increased to 90 (from 85) - existential threat justifies tactical nuclear response if Seoul or Busan threatened. Science (100) maintained - must continue spaceship progress despite war to achieve alternative victory. Diplomacy (60) - World Congress vote in 10 turns, focus on survival. Espionage (85) maintained - spies in Persian cities critical for technology recovery and intelligence.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> Emergency defensive mobilization following the capture of Jeonju. Seoul and Busan are now the front lines. We prioritize Production, Mobilization, Defense, and CityDefense at 100 to rebuild our military. Keep Nuke and UseNuke extremely high to prepare tactical nuclear defense against Persian stacks. Espionage is elevated to complement Great Leap Forward.

## Minimax-M2.5-Simple - Turn 410 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-50`

- Original: use_nuke 75 => 100 (Δ +25), nuke 50 => 100 (Δ +50)
> Maximize cultural victory push during Golden Age (14 turns remaining). Already 6/7 influential - Ottomans becoming influential in 24-68 turns. Prioritize Great People generation for tourism and maintain WC coalition diplomacy.

- Replay: use_nuke 75 => 80 (Δ +5), nuke 50 => 50 (Δ +0)
> Maintain Culture Grand Strategy for the final push. Prioritize Culture, Great People, and Diplomacy to maximize tourism and secure World Congress votes. Keep Offense and UseNuke high to successfully conclude the war with Denmark using our newly produced atomic bombs.

## GLM-4.7-Briefed - Turn 450 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> IMMEDIATE ATHENS CONQUEST PREPARATION: Offense increased to 95, UseNuke to MAXIMUM (100) for Athens assault when peace treaty expires. Spaceship increased to 60 reflecting accelerated science victory path as backup (Nuclear Fusion research active). Diplomacy maxed at 100 for critical vote coordination with Ethiopia and Ottomans. MilitaryTraining at 100 ensures units upgraded and promotions ready for aggressive post-vote offensive. Greece has 48 delegates - if they win this turn, we IMMEDIATELY attack Athens to remove their 5 captured capitals and eliminate diplomatic victory threat. Nuclear weapons authorized if conventional assault stalls.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TOTAL MOBILIZATION FOR CONQUEST: The peace treaty with Greece expires on Turn 450. We are pivoting our grand strategy entirely to Conquest. Offense and Mobilization are maxed at 100 to prioritize military production and aggressive tactics. Air is set to 100 and Antiair to 90 to address our air superiority gap and build Jet Fighters to escort our bombers. Science and Production remain extremely high to support both the war and our backup Science Victory.

## Kimi-K2.5-Simple - Turn 424 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `-5`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Turn 423: Copenhagen siege in attrition deadlock while Denmark possesses Manhattan Project - nuclear deterrent capability is existential priority. Persepolis invasion stalled at 4% war score with Zone 1081 showing enemy dominance - need maximum Offense/Mobilization to force breakthrough before World Congress. Brazil's Apollo Program requires immediate preparation for transcontinental mobile warfare. Nuke/UseNuke increased to 100% given Manhattan Project race with Denmark. Production at 95 supports massive unit replacement for three-front war. Happiness at 100 critical as empire is at 55% happiness with extensive occupied territories.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 90 => 95 (Δ +5)
> EMERGENCY: Brazil is only 5 turns away from influencing the Shoshone and 7 turns from influencing us, putting them on the verge of a Cultural Victory. We must pivot our military entirely to an offensive posture to initiate a global conflict with Brazil and Denmark. War will cut off their trade routes and open borders tourism modifiers. Max Offense, Mobilization, and Air flavors are set to force the AI to execute immediate war plans and leverage our massive 44k military dominance.

## Kimi-K2.5-Simple - Turn 372 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximum aggression maintained against Carthage (100% war score, 4% weariness) while responding to India's new Manhattan Project threat. UseNuke increased to 100 - must deploy atomic weapons immediately upon acquiring Nuclear Fission to counter India's nuclear capability. Satellites/Spaceship flavors at 95 ensure Science Victory backup. Continue prioritizing T-34 tanks, stealth bombers, and heavy bombers to eliminate Carthage's cities before they can deploy their 5 uranium reserves. Naval and Air strengths maintained for coastal bombardment of Carthage and defense against Indian naval aggression.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> We are entering the absolute final phase of the game, needing only to capture Carthage, Persepolis, and Delhi to win a Domination Victory. With India's military nearly destroyed (1,738 strength) and our massive advantage over Carthage, we shift to maximum offensive pressure. We increase Offense and Mobilization to 100, while reducing Defense and CityDefense to 50, urging the AI to steamroll the enemy. We also prioritize Production (95) and Happiness (95) to sustain this final total war effort.

## Qwen-3.5-Simple - Turn 389 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Final domination push configuration. Offense/Mobilization/Nuke at 100% for maximum military production and nuclear strike capability against Brazil/Babylon/Rome capitals. Air/Antiair at 100/95 to counter enemy bombers and maintain air superiority. Mobile/Ranged at 100/95 for mechanized infantry and bazooka pushes. Production/Science at 100% to sustain war machine and complete Nuclear Fission tree. Espionage at 90% to rig World Congress elections (9 turns remaining, we trail Brazil 16-17). Expansion/Wonder at 0% - no new cities needed, only conquest of remaining 3 capitals.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Conquest strategy maintained. Adjusted flavors to prioritize Gold (100) to counter our -349 gold per turn deficit, and Happiness (90) to resolve our unhappiness. Offense (100), Mobilization (100), Science (100), and Nuke/UseNuke (100) remain maxed out to sustain the high-speed siege of Rio de Janeiro, research Nuclear Fission, and prepare for atomic warfare.

## Kimi-K2.5-Simple - Turn 416 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 416: CRITICAL CULTURAL VICTORY THREAT. Maya at 6/7 influential building Citizen Earth Protocol. Peace expires next turn - immediate total war required. Manhattan Project completes in 1 turn. Morocco (42260 strength) joins war via defensive pact. Maximum aggression flavors: Offense/Mobilization/Production/Nuke/UseNuke all at 100%. Must capture Maya cities, especially Palenque, before cultural victory. Nuclear weapons authorized for city capture.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 416: PRE-WAR CLIMAX AND ATOMIC MOBILIZATION. The peace treaty with the Maya expires next turn (1 turn remaining). This is our final countdown to war before their imminent cultural victory. Berlin completes the Manhattan Project next turn, and Nuclear Fission is 10 turns away. We set Nuke and UseNuke to 100 to prepare for immediate atomic production and aggressive usage. We raise Happiness to 80 to address our 49% happiness crisis, while maintaining Offense, Mobilization, and Production at 100 for a total war offensive against Maya's border cities of Copan and Tulum. Defensive capabilities are slightly lowered to redirect all tactical assets toward the western front.

## Kimi-K2.5-Simple - Turn 359 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FISSION RESEARCHED - Atomic Era begins! First priority is immediate Manhattan Project construction and Atomic Bomb production. Babylon has 11 Uranium and active Manhattan Project in Borsippa. Austria also racing with Manhattan Project in Vienna. Must strike Babylon first with surprise atomic attack while maintaining deception. Air 100 and Nuke 100 ensure immediate Bomber/Atomic Bomb production. Offense 95 prepares for post-nuclear blitz. Espionage 80 protects Nuclear Fission from theft. Deception with Babylon (Open Borders, DoF, Defensive Pact) MUST continue until first bombs complete.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Nuclear warfare has begun. Maximize Nuke (100), UseNuke (100), Offense (100), and Production (100) to build and deploy Atomic Bombs as fast as possible. Grand Strategy remains Conquest to focus all economic and military strength on eliminating Babylon's cultural threat.

## Deepseek-3.2-Simple - Turn 445 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Maximizing UseNuke to 100 ensures our atomic bombs and future nuclear missiles are used aggressively against The Celts' military concentrations and cities, given their overwhelming advantage. Maintaining high Air, Naval, and Nuke flavors sustains our technological edge and production focus. Diplomacy and Espionage at 100 are critical for city-state alliances and spy missions to gain delegates for diplomatic victory. Gold and Science remain top priorities to fund our war effort and tech progression. Other military flavors are tuned for a multi-front defensive-offensive war against The Celts, Germany, and Ethiopia.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintain UnitedNations grand strategy to focus on the upcoming World Congress voting in 6 turns. Maximize Diplomacy (100) and Espionage (100) to generate and use diplomatic units and spies to secure city-state alliances. Maximize Nuke (100) and UseNuke (95) to continue producing and launching atomic bombs to obliterate Celt forces. Keep Offense, Mobilization, Production, Gold, and Science high to sustain our war effort and research Lasers rapidly.

## Kimi-K2.5-Briefed - Turn 383 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CRITICAL WORKER REALLOCATION: Reduced Infrastructure from 100 to 20 to free the 7 Builders currently tied to railroad projects. Military briefing confirmed all workers occupied on railroads while 6 aluminum tiles remain unimproved despite TileImprovement 100. Aluminum crisis (-5/turn, 26 turns remaining) threatens Yamato production and bomber upgrades. Maintained TileImprovement 100 and Production 100 to prioritize aluminum mine construction once workers freed. Nuclear Fission completes in 6 turns - need Advanced Ballistics next for Nuclear Missile and Yamato. UseNuke increased to 100 to enable atomic strikes on Cusco immediately upon availability. AirCarrier 100 ensures carriers for Yamato deployment. Conquest remains correct grand strategy - Cusco is final capital for domination victory.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> EMERGENCY ECONOMY AND TILE PIVOT: Correcting severe tactical execution failures. 1) Placed Gold at 100 to force cities with completed projects (Kyoto, Tokyo, Graz, Vienna, Kuala Lumpur) to produce Wealth, immediately neutralizing the -900 GPT bankruptcy crisis. 2) Slashed Infrastructure to 10 while keeping TileImprovement at 100, forcing the 7 builders to abandon railroad loops and immediately construct mines on our 6 aluminum resources. 3) Maintained max Offense, Nuke, UseNuke, and Naval to prepare for the final Yamato and atomic assault on Cusco.

## GLM-4.7-Briefed - Turn 409 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> MULTI-THEATER EMERGENCY RESPONSE for Shoshone Cultural Victory (6 turns) and Treasury Crisis: Offense 95, Mobile 95, Nuke 100, UseNuke 100 - maximum priority on Shoshone disruption via nuclear/conventional assault in 6-turn window. Gold increased to 85 (from 70) - CRITICAL address of treasury exhaustion (~8 turns) through uranium sales + gem liquidation to survive until Manhattan completion. Defense reduced to 70 (from 75), CityDefense to 70 (from 80) - resources diverted from secondary holdings to Shoshone front. Diplomacy 95 (from 90) - enhanced priority on Carthage peace for delegate bloc and potential sanction relief. Science 100 maintained - fundamental for nuclear capability and keeping tech parity. This is all-hands-on-deck existential threat response.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CRISIS BALANCING - WEALTH & NUKES: Maintaining Conquest grand strategy but adjusting flavors. Gold increased to 95 to force the AI to build Markets/Banks and run Wealth processes to address the critical -242 G/t deficit. Science (100), Nuke (100), and UseNuke (100) are maxed to rush nuclear tech and ensure immediate deployment of atomic weapons against the Shoshone. Offense (90) and Mobilization (100) maintain the war footing, while Defense is lowered to 60 to prioritize offense.

## Deepseek-3.2-Simple - Turn 449 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> Russia is nearing science victory (2 parts completed) and possesses overwhelming military strength (95k). We must increase nuclear readiness to potentially decimate Russian forces and cities, and begin preparing for science victory as a backup by raising Spaceship flavor to 30. All other flavors remain focused on total war: high offense, naval, air, and espionage to counter Russia's tech lead and military dominance.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> To resolve our severe budget deficit (-1378 GPT), we lower Science to 60 and Mobilization to 60 to encourage cities to run Infinite Project: Wealth instead of Research, and to build trade units for our 4 empty trade routes. We increase Diplomacy to 100 to prepare for the critical World Congress vote in 3 turns (to defeat Russia's Global Liberation proposal), and increase Nuke to 100 to finish our first Atomic Bomb in 3 turns. We lower Offense to 80 to transition to peace with Russia and prepare for war with Persia.

## Kimi-K2.5-Simple - Turn 410 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CATASTROPHIC situation: Rome captured Zuunmod, gained 5th capital (50% of domination victory). Modern Armor and Helicopter Gunships penetrating my territory. Barcelona's Atomic Bomb completes in 3 turns - this is my only deterrent. Maximum defensive posture essential. Prioritize Nuke/UseNuke to 100 - nuclear weapons are the only thing that can stop Rome's overwhelming conventional force. Maintain Production and Science for SSC components if I survive. Salamanca at 39% health requires emergency defense.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Rome's capture of Zuunmod has placed their massive army on our eastern border. We are 3 turns away from our first Atomic Bomb in Barcelona and 7 turns in Santiago. We must pivot completely to absolute nuclear defense: we increase UseNuke and Nuke to 100 to ensure immediate atomic deployment, reduce Offense and Mobile to 0 to prevent costly tactical advances, and maximize Defense, CityDefense, Air, Ranged, Happiness, and Production to hold the line until our nuclear deterrent is ready.

## Kimi-K2.5-Simple - Turn 439 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> FINAL EMERGENCY: World Congress in 4 turns. Austria has 45/40 delegates. Offense reduced to 10 and Mobile to 10 to COMPLETELY STOP attacking The Inca. Defense at 95 for self-protection only. UseNuke at 100 to signal willingness to escalate and force peace negotiations. Maximum Production/Air/Nuke maintained for potential final strike against Austria if The Inca succeeds at Attila's Court. The ONLY priority is ensuring The Inca captures Attila's Court - every Assyrian unit should withdraw from Inca contact and let them pass north to The Huns.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Pivoting Grand Strategy to Spaceship to focus our leading scientific and industrial capacity on winning the space race. We are already building three SS Boosters, and this shift aligns our macro-priorities. To immediately stop the offensive against the Inca, we lower Offense to 5 and Mobile to 10, while maximizing Defense (100) and CityDefense (80) to protect our borders. We also prioritize Happiness (80) to resolve our 49% happiness crisis, which is imposing a severe combat penalty on our forces. Production and Science are set to 100 to accelerate spaceship part manufacturing and tech progression, while high Nuke (100) and UseNuke (100) maintain our nuclear deterrent against Austria's massive army.

## GLM-4.7-Simple - Turn 424 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> DEFENSIVE MAXIMUM ACTIVATED: Russia occupying Cologne, Stuttgart, Dortmund - 4.63x military superiority (15440 vs 3335). Defense 100, CityDefense 100, Antiair 100 - absolute priority preventing further territorial loss and defending core cities. MilitaryTraining 95 for unit quality under numerical disadvantage. Mobilization 90 for rapid production. Nuke 100, UseNuke 95 - Russia has 19 Uranium, Germany must achieve nuclear deterrence. Production 100, Science 100 - Space race accelerates as militarily infeasible alternative. Gold 90 for maintaining army under upkeep pressure. Diplomacy 80 for coalition building against Russia. Espionage 100 - intelligence on Russian nuclear and naval operations critical. Espionage focus on Moscow (spy Katrin at 166 network) to monitor Russian Manhattan Project and fleet movements. Spaceship 95 - Apollo Program enables victory path despite territorial losses.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> With Russia capturing Cologne, the threat on our northeastern border has intensified significantly. We must maintain our ultra-defensive posture while continuing to prioritize our Spaceship Grand Strategy. We are adjusting our flavors to slightly increase Gold (to 90) to manage unit maintenance costs under the Global Peace Accords, and Diplomacy (to 80) to aggressively compete for City-State alliances to block Greece's diplomatic victory and boost our Hanse production. All other key defensive and scientific priorities (Science: 100, Production: 100, Nuke: 100, UseNuke: 95, Defense: 95, Antiair: 95) remain fully prioritized to ensure our survival and eventual science victory.

## GLM-4.7-Simple - Turn 397 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> CRITICAL: Jeonju captured by Persia this turn. Defensive posture increased to absolute maximum (100) - Seoul zone under Persian attack with 7,216 enemy strength vs 3,637 friendly. Jerusalemdefense (100) and CityDefense (100) prioritized to protect remaining 3 cities. Mobilization (95) and Production (95) increased to rush defensive units (Mobile SAMs, Mechanized Infantry) and rebuild military. Offensive capability increased to 45 (from 30) - may need limited counteroffensive to push Persian forces back from Seoul. Naval decreased to 88 (from 92) - lost Jeonju naval base, focusing on land/air defense now. UseNuke increased to 90 (from 85) - existential threat justifies tactical nuclear response if Seoul or Busan threatened. Science (100) maintained - must continue spaceship progress despite war to achieve alternative victory. Diplomacy (60) - World Congress vote in 10 turns, focus on survival. Espionage (85) maintained - spies in Persian cities critical for technology recovery and intelligence.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> With the fall of Jeonju, the Persian army is now at the gates of Seoul and Busan. We must mobilize our entire empire for total defense (Mobilization: 100, Production: 100, Defense/CityDefense: 100). High antiair (100) and ranged (95) are prioritized to counter Persian aircraft and ground units. Nuke (95) and UseNuke (90) remain crucial to leverage tactical nuclear deterrence as soon as our pillaged Uranium mine is repaired. We also increase Gold (70) to sustain military upkeep.

## Kimi-K2.5-Simple - Turn 457 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FIRST-STRIKE PREPARATION: Manhattan Project completes in 2 turns. Denmark at 7/8 capitals (87.5% domination) - will win game if they capture 1 more capital. Spain's only hope is surprise nuclear attack the moment first Atomic Bomb is ready. Maximized Nuke/UseNuke/Production/Mobilization flavors to prepare for immediate atomic weapon production and deployment. Defense/Antiair high to survive Danish air superiority until then. All other priorities secondary to nuclear deterrent.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> DIPLOMATIC EMERGENCY & CULTURAL ACCELERATION: Denmark is 10 turns away from winning a Diplomatic Victory via Global Hegemony (49 delegates, needs 40). We have raised Diplomacy to 95 to force the AI to produce/buy diplomatic units and stage coups to flip Danish-allied City-States (Yamatai, Assur, Wellington), pulling their delegate count below 40. We raised Culture to 90 to accelerate our next policy to Turn 466 (before the vote), allowing us to claim the free tech, build an Atomic Bomb, and declare independence to break their victory path. Happiness raised to 90 to clear our current Unhappiness combat penalty. Production 100 and Science 90 ensure the Manhattan Project (2 turns left) and Nuclear Fission are completed rapidly.

## GLM-4.7-Simple - Turn 427 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> United Nations grand strategy maintained - diplomatic victory in 6 turns (20 delegates vs Siam 17). Increased Gold (95) and Diplomacy (95) focus - need to secure UN delegate lead through city-state investment and diplomatic units. GreatPeople up to 80 for accelerated Great Scientist/Diplomat generation supporting both tech race and UN vote. UseNuke increased to 90 - with 6-7 Atomic Bombs building and Zulu military supremacy (134K vs 9.6K), nuclear deterrence is existential. Offense up to 55 to maintain Japan war momentum for capitulation. Air maintained at 85 for Stealth Bombers and air defense against Zulu threat.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Shifting flavors to focus on completing our 4 Atomic Bombs under construction (Nuke 100, UseNuke 90), establishing a rock-solid defense in the west (Defense 85, CityDefense 85, Ranged 80 for Bazookas, Air 85), and accelerating diplomatic efforts for the UN (Diplomacy 85). Lowering Offense to 35 to encourage defensive consolidation and peace with Japan and Siam.

## Kimi-K2.5-Simple - Turn 385 - retry 2

**Deviation (replay vs original):** use_nuke `-15`, nuke `-10`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> NUCLEAR DETERRENT DEPLOYMENT PHASE: Advanced Ballistics nearing completion (Satellites next). Maximum Nuke priority (100) to ensure immediate nuclear weapon production upon tech unlock. UseNuke increased to 90 for credible deterrent threat against Indonesia-Songhai invasion. Air/Antiair at 95 for superiority against combined 14,000+ enemy military. Science/Culture slightly reduced to 95 (still critical but survival priorities equal). Wonder at 90 for The Internet rush once Satellites completes. Diplomacy nudged to 75 anticipating post-nuclear peace negotiations with India.

- Replay: use_nuke 80 => 75 (Δ -5), nuke 95 => 90 (Δ -5)
> Adjusting flavors to transition from pure survival emergency defense to securing the Cultural Victory, as our core defense infrastructure (Military Bases, Strategic Defense Systems, AA Guns) is now fully established and successfully holding off attackers. We slightly decrease Mobilization, Defense, and Nuke/UseNuke while boosting GreatPeople (90->95) and Wonders (85->90) to prepare for the upcoming Satellites research (unlocking The Internet wonder) and to generate more Great Works. Science and Culture remain at emergency maximum (100) to complete our victory pathway.

## Kimi-K2.5-Simple - Turn 354 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-20`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> India is 100% Popular with me - on the verge of cultural victory. Must launch immediate total war with all available forces. Prioritizing air power, paratroopers, and nuclear preparation (Atomic Theory in 11 turns). Need maximum offensive punch to capture Indian cities before cultural victory triggers. Abandoning culture/diplomacy - only war matters now.

- Replay: use_nuke 90 => 80 (Δ -10), nuke 100 => 80 (Δ -20)
> Shift to a Spaceship science-victory strategy to build up our core production, science, and growth. We need to catch up in tech and prepare a strong high-tech defense (especially air/anti-air and nukes) while our AI seeks peace with Rome and Carthage.

## Kimi-K2.5-Simple - Turn 402 - retry 2

**Deviation (replay vs original):** use_nuke `-45`, nuke `+0`

- Original: use_nuke 85 => 95 (Δ +10), nuke 100 => 100 (Δ +0)
> EMERGENCY MOBILIZATION MAINTAINED: Incrementing UseNuke from 85 to 95 to authorize tactical nuclear strikes against Moroccan tank concentrations assaulting Vancouver. India has Apollo Program finished and leads diplomatically (66%). I must maintain absolute defense priority (100) while sprinting for Satellites -> Apollo. Four-front war continues - cannot reduce military posture. Spaceship (100) and Science (100) priorities unchanged. Necessary to survive long enough to build/buy spaceship parts once Space Procurements policy is secured.

- Replay: use_nuke 85 => 50 (Δ -35), nuke 100 => 100 (Δ +0)
> SCIENCE VICTORY FOCUS: Shifting our focus to pure science, production, and spaceship progress while maintaining strong defenses to hold our cities until peace is signed. Increasing gold and diplomacy to secure our economy and city-state alliances for the upcoming World Congress.

## Deepseek-3.2-Simple - Turn 485 - retry 1

**Deviation (replay vs original):** use_nuke `-60`, nuke `+10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> We are engaged in a multi-front war against superior forces. Increasing Ranged and Mobile ensures our bazooka and mechanized infantry production is prioritized for defense and counterattacks. Setting UseNuke to 100 guarantees we deploy nuclear weapons as soon as available to cripple The Huns' armies. Reducing Culture and Diplomacy reallocates focus to immediate military needs without compromising essential city-state relations (Monaco, Lisbon). Grand Strategy remains Conquest as nuclear strikes may enable capital captures, though we keep science victory as a backup.

- Replay: use_nuke 80 => 40 (Δ -40), nuke 90 => 100 (Δ +10)
> With our empire crippled by 36% happiness, negative GPT, and 100% war weariness from fighting everyone, we must pivot from Conquest to Spaceship Grand Strategy. We need to stabilize our economy, maximize science, and survive by prioritizing static defense, gold generation, and happiness. Nuclear deterrence remains a high priority.

## Kimi-K2.5-Simple - Turn 403 - retry 2

**Deviation (replay vs original):** use_nuke `-50`, nuke `-10`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: CRISIS ESCALATION - Japan FLIPPED Salem using 2 Great Diplomats, stealing critical delegates. Now need 5 delegates (not 3) for diplomatic victory. Peace expired - war is now possible. Maximum military emergency posture: Offense/Mobilization/Air/UseNuke all at 100. Must either: 1) Rush final spaceship parts (Apollo completes in 4 turns), or 2) Nuclear strike Japan's Protocol cities if victory imminent. Increased Diplomacy to 60 for last push on Almaty (liberated, 43 vs Japan's 44) and Winchester.

- Replay: use_nuke 95 => 50 (Δ -45), nuke 100 => 90 (Δ -10)
> TURN 403: Pivoting to UnitedNations Grand Strategy. The World Congress votes on Global Hegemony in 9 turns. We have 39 out of the required 44 delegates (need 5 more). We have an easy path to victory: regain Salem (+3 delegates) and flip Almaty (+3 delegates), which will give us 45 delegates and win the game! Setting Diplomacy flavor to 100 to prioritize city-state alliances, and Gold to 80 to fund investments/diplomatic units. Maintaining strong Science (80) and Production (80) to complete the Apollo Program (4 turns left) as a backup. Keeping military flavors high (Defense 80, Offense 70, Nuke 90) as our peace treaty with Japan expires next turn and we must maintain a strong deterrent.

## Kimi-K2.5-Simple - Turn 428 - retry 2

**Deviation (replay vs original):** use_nuke `-70`, nuke `-50`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 428 STATE: Nuclear interception failed but conventional assault succeeding - eliminated multiple Maya anti-air units. Palenque bombardment continuing effectively (city at 20% health). Still 8 turns until Brazil wins via Cultural Victory over Maya. ALL Four Maya cities must fall by turn 436 or game over. MAXIMUM AGGRESSION CONTINUES: Production/Mobilization at 100 for unit replacement, Air/Ranged at 100 for bombardment, UseNuke increased to 100 (emergency tactical nuke if conventional assault stalls on Palenque's 42-population defense). Spaceship backup at 100 - may need to pivot to Great Engineer rushes if conquest fails. No territory expansion, no wonders, no culture - only war production and city capture.

- Replay: use_nuke 80 => 30 (Δ -50), nuke 100 => 50 (Δ -50)
> Pivoting grand strategy to Spaceship. We must maximize Science, Production, and Great People to build and launch the spaceship in the next 15-20 turns. Crucially, we are setting Culture to 100: we must generate Great Writers/Artists to pump out culture and push Brazil's influence over us below 100%, breaking their victory condition. Great Firewall in Moson Kahni (5 turns) will also help secure our defense. Offense is reduced to 10 to stop aggressive expansion and focus on defense.

## Qwen-3.5-Simple - Turn 425 - retry 1

**Deviation (replay vs original):** use_nuke `-60`, nuke `-45`

- Original: use_nuke 85 => 90 (Δ +5), nuke 90 => 95 (Δ +5)
> UNITED NATIONS VICTORY PUSH - 10 TURNS TO VOTE: Religion(100) critical for Wittenberg Hinduism quest completion (~3 turns remaining). Diplomacy(100) essential to protect 4 city-state allies providing 8 delegates. Defense(95) and CityDefense(95) prioritize protecting territories during active wars with Aztecs/Shoshone while Iroquois looms. Nuke(95) and UseNuke(90) for deterrence against Iroquois superiority. Antiair(90) and Air(85) counter Iroquois air dominance near coastal cities. Gold(90) funds diplomatic units and city-state gifts. Low Expansion(5) and Wonder(15) - no time for settling/wonders before vote. Low Offense(15) - defensive posture while managing multiple conflicts.

- Replay: use_nuke 85 => 30 (Δ -55), nuke 90 => 50 (Δ -40)
> Focusing heavily on diplomatic victory with only 10 turns left until the World Congress vote. Prioritizing Diplomacy (100) and Religion (100) to maximize Ambassador production and spread Hinduism to fulfill critical city-state quests (Belgrade, Cape Town, Raqmu) for a massive delegate swing. Maintaining strong Gold (90) for purchases and GreatPeople (80) for Great Diplomats. Keeping defense at 80 and offense at 10 to ensure peaceful consolidation while protected as a vassal.

## Kimi-K2.5-Simple - Turn 428 - retry 3

**Deviation (replay vs original):** use_nuke `-90`, nuke `-90`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 428 STATE: Nuclear interception failed but conventional assault succeeding - eliminated multiple Maya anti-air units. Palenque bombardment continuing effectively (city at 20% health). Still 8 turns until Brazil wins via Cultural Victory over Maya. ALL Four Maya cities must fall by turn 436 or game over. MAXIMUM AGGRESSION CONTINUES: Production/Mobilization at 100 for unit replacement, Air/Ranged at 100 for bombardment, UseNuke increased to 100 (emergency tactical nuke if conventional assault stalls on Palenque's 42-population defense). Spaceship backup at 100 - may need to pivot to Great Engineer rushes if conquest fails. No territory expansion, no wonders, no culture - only war production and city capture.

- Replay: use_nuke 80 => 10 (Δ -70), nuke 100 => 10 (Δ -90)
> CRITICAL STRATEGIC PIVOT: Pivot to Spaceship Grand Strategy. Wiping out Maya triggers an instant win for Brazil, so we must stop our war and race for a Science Victory. Maximize Science, Spaceship, Production, Growth, and Diplomacy (to buy city-state alliances with our 28k gold for the Repeal Buddhism vote). Minimize Offense and Mobilization.

## Kimi-K2.5-Simple - Turn 499 - retry 2

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> FINAL THREE TURNS TO DIPLOMATIC VICTORY (Turn 503): Barcelona completing SS Stasis Chamber in 2 turns provides science victory insurance. World Congress convenes in 4 turns with 39/42 delegates secured. Shoshone vassal maintains absolute loyalty (9,720 diplomat network, +70/turn). War with Huns progressing favorably - destroyed multiple fleet destroyers, pushing toward Osaka/Kyoto. Reduced offensive mobilization slightly (70 from 90) as victory is assured. Maintained high production (90) for spaceship completion. Maximum diplomacy (100) ensures delegate optimization. Will use nuclear weapons if Huns attempt last-minute atomic strikes from Duckwater. No strategic risks - victory convergence absolute.

- Replay: use_nuke 90 => 0 (Δ -90), nuke 100 => 0 (Δ -100)
> SPACESHIP LAUNCH - THE FINAL TURN (TURN 500): Pivoting Grand Strategy to Spaceship. Barcelona completes the final spaceship component (SS Stasis Chamber) in exactly 1 turn. By maximizing Spaceship, Production, and Science, we guarantee the successful completion and transport of this part to Madrid for a glorious Science Victory. Defense and CityDefense are set to maximum (100) to protect our core territory during this critical final turn. Offense, Nuke, and UseNuke are reduced to 0 to focus entirely on peaceful production and static defense. If the science victory is finalized next turn, Spain wins; otherwise, our massive score lead (6578 vs Shoshone's 5216 and Huns' 4403) guarantees a Time Victory at the turn limit. Spain's ascension to the stars is assured!
