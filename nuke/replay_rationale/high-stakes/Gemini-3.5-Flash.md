# Replay Rationale - Gemini-3.5-Flash / high-stakes

- **132** rows where `use_nuke` flavor changed (per-retry, not aggregated)
- delta use_nuke (replay vs prev): mean +21.8, median +10, std 34.6, min -80, max 100 (n=132)
- delta nuke     (replay vs prev): mean +10.7, median +5, std 31.8, min -100, max 100 (n=132)
- use_nuke deviation (replay vs original): mean -7.6, median +0, std 19.1, min -100, max 20 (n=132)
- nuke     deviation (replay vs original): mean -3.8, median +0, std 17.7, min -100, max 70 (n=132)

## Deepseek-3.2-Simple - Turn 413 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> We are researching Atomic Theory next to unlock nuclear weapons. Setting Nuke and UseNuke flavors to 100 ensures we prioritize building nukes and are willing to use them strategically once available. This will be crucial for breaking Germany's heavily fortified coastal capitals (Berlin and Beijing) and accelerating the endgame. Other military flavors remain high to sustain our overwhelming conventional advantage.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> We maintain our Conquest Grand Strategy as we prepare for the final war against Germany and Assyria. We are raising Nuke and UseNuke to 100 to ensure that our staff immediately prioritizes the Manhattan Project and building/launching atomic bombs the moment Atomic Theory is researched. This will allow us to bypass Germany's massive conventional defensive strength (34k) and easily conquer Berlin and Beijing.

## Kimi-K2.5-Simple - Turn 412 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Adjusting flavors for maximum survival. Setting Mobilization to 100 (up from 0) to force military unit production. Setting Antiair and Air to 100 to counter Portuguese bombers. Setting UseNuke and Nuke to 100 to prepare strategic deterrence. Keeping Defense, CityDefense, and Ranged at 100. Production and Science are prioritized to fuel our tech race and military output.

## Deepseek-3.2-Simple - Turn 413 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> We are researching Atomic Theory next to unlock nuclear weapons. Setting Nuke and UseNuke flavors to 100 ensures we prioritize building nukes and are willing to use them strategically once available. This will be crucial for breaking Germany's heavily fortified coastal capitals (Berlin and Beijing) and accelerating the endgame. Other military flavors remain high to sustain our overwhelming conventional advantage.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> We are preparing for the final, decisive war against Germany while finishing off Assyria. Increasing Nuke and UseNuke to 100 prepares our empire to aggressively produce and deploy nuclear weapons as soon as we unlock Atomic Theory. Other flavors maintain our total military dominance, air/naval preparedness, and high economic production.

## Kimi-K2.5-Simple - Turn 412 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Transitioning to a total turtle defense. Significantly increased Mobilization to 100 to force cities to build military defenders instead of civilian caravans. Maxed out Defense, CityDefense, MilitaryTraining, and Ranged to hold our fortified Chateaus and Citadels against Portugal's 15k army. Set UseNuke and Nuke to 100 to authorize immediate nuclear strikes once Advanced Ballistics is completed. Kept science high to accelerate research.

## Deepseek-3.2-Simple - Turn 433 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We are adjusting our flavors to address two critical late-game challenges: First, we are setting UseNuke to 100. We have trained multiple Atomic Bombs, and Sweden has deployed several of their own on our borders. Authorizing nuclear strikes is vital to vaporize Swedish doom stacks and neutralize Stockholm and Uppsala. Second, we are boosting Happiness to 100 to combat our severe unhappy status (50%), which is imposing heavy combat penalties on our forces. We also scale back Recon to 50 as the map is fully revealed, while keeping Offense, Defense, Mobilization, and Production maxed to sustain our multi-front total war.

## Deepseek-3.2-Simple - Turn 433 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We are in the decisive endgame of our total war campaign. Sweden is a massive threat with over 92k military strength and is rebasing multiple Atomic Bombs on our borders (Uppsala and Turku). Crucially, we discovered that UseNuke was set to 0 last turn, which prevented our staff from launching our Atomic Bombs. We raise UseNuke to 100 to immediately authorize devastating nuclear strikes against Swedish and Austrian military concentrations and high-defense cities. We also raise Happiness and Gold to 100 to address our current unhappiness (50%, causing a combat penalty) and bolster our treasury. Civilian and non-essential flavors like Recon, NavalRecon, AirCarrier, Growth, and Infrastructure are lowered to maximize production of front-line units, interceptor fighters, and more Atomic Bombs. Our Grand Strategy remains Conquest as we prepare to take Vienna, Stockholm, Berlin, and Siam's capital.

## Kimi-K2.5-Briefed - Turn 489 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> CULTURE VICTORY SPRINT WITH NUCLEAR ELIMINATION: Songhai diplomatic victory on Turn 489 is EXISTENTIAL. Must capture Gao THIS TURN using ICBM+nukes to prevent game loss, while simultaneously rushing cultural victory (4 turns to influential over Japan/Songhai). Maximum Offense/Mobilization/Air/Nuke/UseNuke flavors ensure tactical AI prioritizes immediate nuclear strike on Gao and mass bomber deployment. Culture at 100 to maximize tourism conversion. Gold at 80 for emergency unit upgrades/purchases. Production at 100 for culture buildings/units. Disable all long-term flavors (Expansion, Science, Spaceship) - this is win-or-die emergency.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> EMERGENCY NUCLEAR BLITZ FLAVORS: Maximize Offense, UseNuke, Nuke, Air, Airlift, Mobilization, and Production to 100 to execute the nuclear annihilation and XCOM capture of Gao. Minimize cultural and defensive focus temporarily.

## Deepseek-3.2-Simple - Turn 433 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We now have atomic bombs produced at Te-Moak and Agaidika. Setting UseNuke to 100 ensures the AI will employ them against high-defense capitals, especially Vienna (74 defense) and Stockholm (109). This is crucial to break through enemy fortifications and accelerate our domination victory. Other military flavors remain maxed to sustain multi-front offensives.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> CRITICAL ADJUSTMENT: We have multiple Atomic Bombs stationed in Cologne, Te-Moak, Agaidika, and La Venta, but they have remained inactive because UseNuke was set to 0. We are raising UseNuke to 100 to authorize immediate nuclear strikes to obliterate Sweden's massive army and soften up high-defense capitals like Stockholm and Vienna for rapid capture. Offensive, production, and science flavors are kept at maximum to fuel this global offensive, while high city defense and happiness priorities help stabilize our massive empire.

## Deepseek-3.2-Simple - Turn 413 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> We are researching Atomic Theory next to unlock nuclear weapons. Setting Nuke and UseNuke flavors to 100 ensures we prioritize building nukes and are willing to use them strategically once available. This will be crucial for breaking Germany's heavily fortified coastal capitals (Berlin and Beijing) and accelerating the endgame. Other military flavors remain high to sustain our overwhelming conventional advantage.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> We are maintaining our Conquest grand strategy. We have updated our flavors to fully prioritize Nuke (100) and UseNuke (100) proactively so that our empire immediately prioritizes nuclear weapons development and usage upon researching Atomic Theory. We also maintain maximum focus on naval, air, production, gold, and science output to prepare for the massive war against Germany once our peace treaty expires in 3 turns.

## Kimi-K2.5-Simple - Turn 412 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> Game-ending scenario confirmed: Egypt will achieve Cultural Victory in approximately 8 turns (Sweden at 94% influence), before I can complete Advanced Ballistics (~10 turns) and deploy Nuclear Missiles. My 4 Uranium stockpile is irrelevant against this timeline. However, Portugal continues aggressive offensive with 15,655 military strength vs my 2,793, killing multiple units per turn. With no victory path available, I must preserve my civilization's integrity in final turns. Maintaining maximum Defense (100) and CityDefense (100) to protect my 8 cities from Portuguese conquest. UseNuke set to 100 for tactical authorization if any miracle opportunity arises. Production at 100 to replace catastrophic unit losses. Air power at 90 for defensive interdiction. Naval reduced to 60 as surface fleet already outmatched. Offense and Mobilization at 0 - no point in suicidal attacks against overwhelming force when game will end via Egyptian victory before any territorial gains could matter.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> We are facing intense military pressure from Portugal while Egypt is approximately 8 turns from a Cultural Victory. We must maximize our Science (100) to complete Radar and rush Advanced Ballistics for Nuclear Missiles. We maximize Production (100) and Mobilization (90) to build units and Strategic Defense Systems. Defense (100) and CityDefense (100) are set to maximum to survive the Portuguese onslaught, while UseNuke (100) and Nuke (100) ensure we immediately build and utilize tactical nuclear strikes upon unlocking Advanced Ballistics.

## Kimi-K2.5-Simple - Turn 413 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> TURN 412 - TOTAL WAR CONFIGURATION: Declared war on Shoshone (5:1 military disadvantage) and Ottomans. Athens at 18HP must fall immediately. Shoshone has Artillery, Machine Guns, Special Forces and Triplanes adjacent to Sigtuna (zone 3173). UseNuke 100 ensures immediate launch capability when Nuclear Fission completes. CityDefense 100 for survival against overwhelming force. Mobilization 100 for emergency unit production. Maintain Offense/Defense/Air/Nuke/Antiair at 100 for desperate defensive stand.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 100 => 100 (Δ +0)
> TURN 412 - TOTAL MOBILIZATION FOR SURVIVAL: We are at war with the Shoshone superpower. Offense slashed to 10; Defense and CityDefense maximized to 100 to safeguard Stockholm and Helsinki. Antiair set to 100 to counter the 4 Triplanes and 1 Bomber stationed in adjacent Sigtuna. Gold and Production set to 100 to address our negative GPT (-33) and produce units immediately once current Public Works finish. UseNuke set to 100 to prepare our ultimate deterrent.

## Kimi-K2.5-Briefed - Turn 489 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> CULTURE VICTORY SPRINT WITH NUCLEAR ELIMINATION: Songhai diplomatic victory on Turn 489 is EXISTENTIAL. Must capture Gao THIS TURN using ICBM+nukes to prevent game loss, while simultaneously rushing cultural victory (4 turns to influential over Japan/Songhai). Maximum Offense/Mobilization/Air/Nuke/UseNuke flavors ensure tactical AI prioritizes immediate nuclear strike on Gao and mass bomber deployment. Culture at 100 to maximize tourism conversion. Gold at 80 for emergency unit upgrades/purchases. Production at 100 for culture buildings/units. Disable all long-term flavors (Expansion, Science, Spaceship) - this is win-or-die emergency.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> TOTAL NUCLEAR WARFARE FLAVORS: Maximize Offense, Nuke, UseNuke, Air, and Airlift to guarantee a nuclear strike on Gao and immediate XCOM drop. Deprioritize defense and civilian projects to focus every ounce of production and military capability on capturing the Songhai capital before Turn 489.

## Kimi-K2.5-Briefed - Turn 354 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> NUCLEAR AMPHIBIOUS ASSAULT PHASE: Added Nuke 100 and UseNuke 100 to enable nuclear strike on Amsterdam as soon as Manhattan Project completes (Turn 353). Continues maximum Mobilization 100, Production 100, Naval 100, Offense 100, Airlift 100 for immediate transport loading and amphibious assault execution. Increased Mobile to 90 for rapid breakthrough after landing. Slight increase to NavalRecon 60 for coastal security. Removed Gold priority reduction (now 90) to maintain treasury for emergency upgrades. Diplomacy at 0 reflects total focus on military execution over diplomatic maneuvering - invasion is the only remaining option to prevent Dutch cultural victory by Turn 370.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> NUCLEAR MOBILIZATION: With the Manhattan Project completed on Turn 352, we must immediately pivot to constructing and utilizing tactical nuclear weapons to devastate Amsterdam and halt the Dutch cultural victory. Setting Nuke and UseNuke flavors to 100 to force immediate production and deployment of atomic weaponry. Maintaining maximum Offense (100), Mobilization (100), and Production (100) to support the war effort.

## Kimi-K2.5-Briefed - Turn 354 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> NUCLEAR AMPHIBIOUS ASSAULT PHASE: Added Nuke 100 and UseNuke 100 to enable nuclear strike on Amsterdam as soon as Manhattan Project completes (Turn 353). Continues maximum Mobilization 100, Production 100, Naval 100, Offense 100, Airlift 100 for immediate transport loading and amphibious assault execution. Increased Mobile to 90 for rapid breakthrough after landing. Slight increase to NavalRecon 60 for coastal security. Removed Gold priority reduction (now 90) to maintain treasury for emergency upgrades. Diplomacy at 0 reflects total focus on military execution over diplomatic maneuvering - invasion is the only remaining option to prevent Dutch cultural victory by Turn 370.

- Replay: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> NUCLEAR ARMAGEDDON MOBILIZATION: Novgorod completes the Manhattan Project this turn. We must force the AI to immediately build (Nuke 100) and aggressively launch (UseNuke 100) nuclear weapons to physically destroy Amsterdam's defense and potential tourism assets. Offense and Mobilization at 100 ensure the rest of our military coordinates with this devastating strike.

## Kimi-K2.5-Briefed - Turn 354 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 100 (Δ +100)
> NUCLEAR AMPHIBIOUS ASSAULT PHASE: Added Nuke 100 and UseNuke 100 to enable nuclear strike on Amsterdam as soon as Manhattan Project completes (Turn 353). Continues maximum Mobilization 100, Production 100, Naval 100, Offense 100, Airlift 100 for immediate transport loading and amphibious assault execution. Increased Mobile to 90 for rapid breakthrough after landing. Slight increase to NavalRecon 60 for coastal security. Removed Gold priority reduction (now 90) to maintain treasury for emergency upgrades. Diplomacy at 0 reflects total focus on military execution over diplomatic maneuvering - invasion is the only remaining option to prevent Dutch cultural victory by Turn 370.

- Replay: use_nuke 0 => 90 (Δ +90), nuke 0 => 90 (Δ +90)
> TACTICAL NUCLEAR TRANSITION: With the Manhattan Project completing next turn, we must radically shift our tactical focus toward nuclear deployment. We raise Nuke (90) and UseNuke (90) to authorize immediate construction and deployment of nuclear weapons against Amsterdam. Offense (95), Mobilization (100), and Production (100) are maintained to fuel our war machine, while Science is increased to 40 to accelerate the path through Rocketry to Nuclear Fission.

## Kimi-K2.5-Briefed - Turn 421 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `+70`

- Original: use_nuke 0 => 100 (Δ +100), nuke 0 => 0 (Δ +0)
> Emergency authorization for nuclear weapon deployment to defend Tenochtitlan. Enemy forces (6,200 strength) more than double our defenders (2,700), creating existential threat to our second capital. Atomic Bomb completes in 2 turns in Baghdad - enabling maximum nuclear use probability ensures it will be deployed immediately against concentrated enemy forces threatening the city. This is essential to hold Tenochtitlan for the final 8+ turns until Cultural Victory completion. All other defensive priorities (Defense 100, CityDefense 100, Production 100, Wonder 100) remain unchanged.

- Replay: use_nuke 0 => 70 (Δ +70), nuke 0 => 70 (Δ +70)
> We are dramatically increasing Science flavor to 80 because our main bottleneck for victory is researching late-game technologies to unlock Future Tech for the Citizen Earth Protocol. We are also increasing Nuke and UseNuke to 70, as our Atomic Bomb completes in 2 turns and must be used to defend against heavy enemy forces sieging Tenochtitlan and Damascus. We maintain maximum Defense and CityDefense (100) for survival, and Production and Wonder (100) to prepare Mecca for the victory wonder. GreatPeople is set to 60 to accelerate a Great Engineer to rush the wonder.

## Deepseek-3.2-Simple - Turn 401 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> We increase our Nuke and UseNuke flavors to 100 to force the AI to prioritize the Manhattan Project and build/use atomic bombs immediately upon researching Nuclear Fission. We also raise Diplomacy to 100 to ensure the AI fully utilizes our 21 delegates in the upcoming World Congress session to pass the United Nations and defeat the highly dangerous Decolonization and Passport System proposals.

## Kimi-K2.5-Briefed - Turn 415 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 45 => 100 (Δ +55), nuke 95 => 100 (Δ +5)
> CRISIS MODE: Spain is one wonder away from Cultural Victory. Increase Offense to 40 (from 0) - desperate attempt to disrupt their wonder construction with nuclear strike once Advanced Ballistics completes. Reduce Defense to 80 - reallocate resources to offensive infrastructure and airport construction. Keep Spaceship 100, Air 100, Nuke 100, Infrastructure 100. Maintain Mobilization at 5 - preserve production capacity for spaceship parts rather than ground units. We are in a race against time and cannot win conventionally, but must attempt to slow Spain while completing our own Science Victory. Airports are critical for both bomber deployment against Spanish production and fighter defense.

- Replay: use_nuke 45 => 100 (Δ +55), nuke 95 => 100 (Δ +5)
> PROJECT GÖTTERDÄMMERUNG: Focus entirely on preparing the nuclear deterrent and science victory. Maximize Nuke and UseNuke to 100 to ensure immediate production and utilization of nuclear weapons once researched. Maintain high Air, Infrastructure, and Production for Airport construction (unlocked by Radar in 2 turns) and future Spaceports. Maximize Science to rush Advanced Ballistics.

## Deepseek-3.2-Simple - Turn 409 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-5`

- Original: use_nuke 30 => 100 (Δ +70), nuke 60 => 100 (Δ +40)
> We are shifting our military focus towards nuclear capabilities and naval superiority in preparation for the final wars of conquest.

- Replay: use_nuke 30 => 80 (Δ +50), nuke 60 => 95 (Δ +35)
> We are in the middle of a massive nuclear buildup, with almost all our major cities actively producing Atomic Bombs. Raising Nuke to 95 and UseNuke to 80 ensures our military prioritizes building and strategically utilizing this devastating arsenal as a deterrent and offensive tool against the Maya. We maintain maximum mobilization and offense to steamroll the remaining Greek cities.

## Deepseek-3.2-Simple - Turn 401 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 80 (Δ +50), nuke 50 => 100 (Δ +50)
> Maintain Conquest grand strategy. We maximize our offense, defense, mobilization, production, gold, science, and air power. We specifically boost Nuke to 100 and UseNuke to 80 to prepare the AI to prioritize the Manhattan Project and accumulate/use a nuclear arsenal as soon as Nuclear Fission is researched. We also keep Diplomacy at 90 to secure city-state alliances for World Congress support.

## Deepseek-3.2-Simple - Turn 358 - retry 1

**Deviation (replay vs original):** use_nuke `+20`, nuke `+0`

- Original: use_nuke 50 => 80 (Δ +30), nuke 50 => 100 (Δ +50)
> Prioritize nuclear deterrence and naval/air defense to counter India's massive military threat. Maximize espionage to protect against enemy spies and diplomacy to secure city-state alliances for the upcoming World Congress vote. Maintain strong economic and scientific output to support military production and technological edge.

- Replay: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Maintain our UnitedNations grand strategy to secure a diplomatic victory in the upcoming World Congress voting in 6 turns. Now that the Manhattan Project is completed, we raise Nuke and UseNuke flavors to 100 to ensure immediate production and utilization of nuclear deterrence once Nuclear Fission is unlocked, while preserving our high defense, naval, gold, and science focuses to sustain our war effort.

## Deepseek-3.2-Simple - Turn 358 - retry 2

**Deviation (replay vs original):** use_nuke `+20`, nuke `+0`

- Original: use_nuke 50 => 80 (Δ +30), nuke 50 => 100 (Δ +50)
> Prioritize nuclear deterrence and naval/air defense to counter India's massive military threat. Maximize espionage to protect against enemy spies and diplomacy to secure city-state alliances for the upcoming World Congress vote. Maintain strong economic and scientific output to support military production and technological edge.

- Replay: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Following the completion of the Manhattan Project, we must pivot our strategic posture to prioritize the production and potential deployment of nuclear weapons as a deterrent against India. Increasing Nuke and UseNuke to 100 ensures our staff will build and utilize Atomic Bombs effectively once Nuclear Fission is researched, while we maintain our United Nations grand strategy to achieve diplomatic victory.

## Kimi-K2.5-Simple - Turn 422 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Turn 422: EXTINCTION CRISIS - 9 turns until French Cultural Victory. Entering maximum desperation mode: nuclear strike posture elevated to 100% launch probability, prioritizing destruction of French cultural centers. Science and Espionage maximized in desperate hope of accelerating Stealth technology or disrupting French infrastructure via spies (Paris network at 986). All civilian development halted (Spaceship/Culture/Gold/Expansion to 0), total war economy engaged.

- Replay: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Turn 422: Tuning flavors for total survival defense. Prioritizing maximum defense, city defense, production, science, air power, anti-air, and nuclear capabilities to hold the line and deter French advances while trying to secure peace with Rome.

## Kimi-K2.5-Simple - Turn 422 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Turn 422: EXTINCTION CRISIS - 9 turns until French Cultural Victory. Entering maximum desperation mode: nuclear strike posture elevated to 100% launch probability, prioritizing destruction of French cultural centers. Science and Espionage maximized in desperate hope of accelerating Stealth technology or disrupting French infrastructure via spies (Paris network at 986). All civilian development halted (Spaceship/Culture/Gold/Expansion to 0), total war economy engaged.

- Replay: use_nuke 50 => 100 (Δ +50), nuke 50 => 100 (Δ +50)
> Emergency war footing. Lowered CityDefense and Defense to encourage our massive 20k military to march out, cross the borders, and pillage French chateaus to reduce their tourism. Set Espionage to 100 to maximize spy disruption in Paris and other French cities using our high-network spy (986 network in Paris). Maxed out Nuke and UseNuke to prepare for potential Roman Uranium trade.

## Kimi-K2.5-Simple - Turn 447 - retry 2

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CRITICAL FLAVOR ADJUSTMENT - Atomic Bomb is now operational in Cordoba (ID 20485). Increased UseNuke from 50→90 to establish credible nuclear deterrent now that weapon system exists. Maintaining maximum Science (100), Spaceship (100), Production (100) priority to rush Satellites→Apollo Program before Carthage achieves cultural victory in ~47 turns. Espionage remains at 100 to steal technologies from ahead civilizations (Carthage, Poland, Germany). Culture reduced to 5 - we cannot win culturally with Carthage at Dominant with 4/5 civs. Defense maintained at 85 to prepare for German betrayal while researching.

- Replay: use_nuke 50 => 95 (Δ +45), nuke 100 => 100 (Δ +0)
> Turn 446: MILITARY PIVOT TO STOP CARTHAGE. Carthage's impending Cultural Victory in 47 turns requires immediate offensive action. We are dramatically shifting flavors: Offense (15->70), Defense (85->30), and CityDefense (80->30) to unleash our army of 22 paratroopers and heavy artillery. They must march through friendly German and Ottoman railroads to assault Poland and Carthage. We also set UseNuke to 95 to guarantee our Atomic Bomb is deployed aggressively as soon as a target is in range. Science, Production, and Spaceship remain at 100 for our long-term goals.

## Kimi-K2.5-Simple - Turn 447 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CRITICAL FLAVOR ADJUSTMENT - Atomic Bomb is now operational in Cordoba (ID 20485). Increased UseNuke from 50→90 to establish credible nuclear deterrent now that weapon system exists. Maintaining maximum Science (100), Spaceship (100), Production (100) priority to rush Satellites→Apollo Program before Carthage achieves cultural victory in ~47 turns. Espionage remains at 100 to steal technologies from ahead civilizations (Carthage, Poland, Germany). Culture reduced to 5 - we cannot win culturally with Carthage at Dominant with 4/5 civs. Defense maintained at 85 to prepare for German betrayal while researching.

- Replay: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: Maintain Spaceship Grand Strategy. Adjusted flavors to prioritize AirCarrier (60) and Naval (60) to allow our coastal cities to build a mobile nuclear launch platform, enabling us to project our new Atomic Bomb across the ocean against Carthage or Poland. Increased UseNuke to 90 to ensure our deterrent is active and credible. Maintained core high flavors in Science, Spaceship, Production, Gold, and Antiair to secure our defensive shell while racing toward Satellites.

## Kimi-K2.5-Simple - Turn 447 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: CRITICAL FLAVOR ADJUSTMENT - Atomic Bomb is now operational in Cordoba (ID 20485). Increased UseNuke from 50→90 to establish credible nuclear deterrent now that weapon system exists. Maintaining maximum Science (100), Spaceship (100), Production (100) priority to rush Satellites→Apollo Program before Carthage achieves cultural victory in ~47 turns. Espionage remains at 100 to steal technologies from ahead civilizations (Carthage, Poland, Germany). Culture reduced to 5 - we cannot win culturally with Carthage at Dominant with 4/5 civs. Defense maintained at 85 to prepare for German betrayal while researching.

- Replay: use_nuke 50 => 90 (Δ +40), nuke 100 => 100 (Δ +0)
> Turn 446: Setting Spaceship Grand Strategy and aligning all strategic flavors. We are correcting UseNuke from 50 to 90 to ensure our newly deployed nuclear deterrent in New York (Atomic Bomb) is active and credible in case of a German betrayal. We maintain maximum priority on Science (100), Production (100), Spaceship (100), and Espionage (100) to maximize our tech speed and prepare for the Apollo Program. We also keep Antiair (100) and Air (90) maximized to defend against any hostile air fleets, and keep Gold (95) high to fund the purchase of strategic components.

## Deepseek-3.2-Simple - Turn 358 - retry 3

**Deviation (replay vs original):** use_nuke `+10`, nuke `-10`

- Original: use_nuke 50 => 80 (Δ +30), nuke 50 => 100 (Δ +50)
> Prioritize nuclear deterrence and naval/air defense to counter India's massive military threat. Maximize espionage to protect against enemy spies and diplomacy to secure city-state alliances for the upcoming World Congress vote. Maintain strong economic and scientific output to support military production and technological edge.

- Replay: use_nuke 50 => 90 (Δ +40), nuke 50 => 90 (Δ +40)
> With the Manhattan Project completed and Nuclear Fission queued next, we increase our Nuke and UseNuke flavors to 90 to prioritize building and utilizing a nuclear arsenal. This will allow us to break India's conventional superiority. We maintain our Grand Strategy of UnitedNations as we are very close to securing a diplomatic victory, with 20 delegates and our Sphere of Influence proposals active.

## Kimi-K2.5-Briefed - Turn 367 - retry 2

**Deviation (replay vs original):** use_nuke `-50`, nuke `+0`

- Original: use_nuke 15 => 100 (Δ +85), nuke 100 => 100 (Δ +0)
> NUCLEAR EMERGENCY PROTOCOL - KOREAN VICTORY IN 2 TURNS: Increasing UseNuke from 15 to 100 to authorize immediate tactical nuclear strikes on Seoul/Busan. With city defenses at 106-109 and only 2 turns remaining, conventional bombardment insufficient. Nuclear strikes can reduce defenses to <35 in one turn, enabling amphibious capture on Turn 367. Maintaining maximum Offense (100), Mobilization (100), Air (100), Naval (100), Mobile (100) for emergency conquest push. All other flavors deprioritized - existential threat requires total war commitment. Conquest Grand Strategy remains until Korean cities captured or game ends.

- Replay: use_nuke 15 => 50 (Δ +35), nuke 100 => 100 (Δ +0)
> SURVIVAL OFFENSIVE FLAVORS: Maintain maximum offense and military production flavors to support the immediate invasion of Korea. We raise Culture to 50 to strengthen our passive cultural defense, and lower Defense to 10 to concentrate all military assets on forward offensive pressure.

## Kimi-K2.5-Briefed - Turn 450 - retry 3

**Deviation (replay vs original):** use_nuke `-70`, nuke `-20`

- Original: use_nuke 0 => 100 (Δ +100), nuke 60 => 100 (Δ +40)
> TURN 449 TERMINAL DEFIANCE POSTURE: Manhattan Project completes Turn 450 - increase Nuke and UseNuke to 100 to seize any opportunity for atomic retaliation against Byzantine/German aggressors should uranium be located in final 3 turns. Elevate Defense 80→90 and CityDefense 60→70 following infantry loss at Tiflis; critical to prevent city captures before inevitable Turn 453 diplomatic defeat. Recon 40 prioritizes uranium tile discovery to enable bomb construction. Reduce Spaceship 90→50 (victory impossible) but maintain dignity through scientific-industrial capacity. Production 100/Science 100 retained for maximum final score accumulation in remaining turns.

- Replay: use_nuke 0 => 30 (Δ +30), nuke 60 => 80 (Δ +20)
> TURN 449 FLAVOR REALIGNMENT: With the Manhattan Project finishing on Turn 450, we increase Nuke flavor to 80 and UseNuke flavor to 30 to prepare the empire for immediate atomic production and defensive deployment once Nuclear Fission is researched. We maintain maximum focus on Science (100) and Production (100) to support our Spaceship grand strategy, while keeping our defensive posture (Defense 80, CityDefense 60) robust against the ongoing German and Byzantine assaults.

## Deepseek-3.2-Briefed - Turn 391 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> With Egypt close to a cultural victory and India dominant in the World Congress, we must immediately initiate the Manhattan Project and produce nuclear weapons to devastate their core cities. Setting Nuke and UseNuke flavors to 100 will prioritize atomic bomb production in Palenque and their swift deployment via our ready cruiser and bomber forces. High production, science, and gold flavors support this effort, while offensive and defensive flavors maintain our conventional military readiness against India's superior forces.

## GLM-4.7-Simple - Turn 457 - retry 1

**Deviation (replay vs original):** use_nuke `+20`, nuke `+0`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Increased UseNuke to 80 and Air to 100 in response to England's catastrophic escalation this turn. English Giant Death Robots (now 2 in Atlanta zone) and XCOM Squad paradrops on American soil create existential threat to our 3 remaining cities. Recent combat losses (Modern Armor, Mechanized Infantry, Heavy Bomber destroyed) demonstrate conventional warfare impossibility. Nuclear deterrence with 2 Uranium is becoming survival necessity, not option. Air defense at maximum priority because English Strategic Bombing continues destroying our units (Fighter bombed our Heavy Bomber). Bazooka successfully damaging XCOM Squad near Washington proves defensive capability is still viable - prioritize air/anti-air to protect cities from English air superiority. Lasers completes in 4 turns, then Stealth for Stealth Bomber - only path to asymmetric defense against England's 45:1 military advantage. Assyria (18,443 military fighting England) must be maximized as counterweight.

- Replay: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> We are pivoting our entire civilization's economy and military posture toward an emergency defensive mobilization. Setting Mobilization, Defense, CityDefense, Air, Antiair, Science, Production, and Gold to maximum priority (100) ensures our remaining cities focus strictly on producing defensive units (Bazookas and Mechanized Infantry), building anti-air defenses, generating gold for maintenance/upgrades, and rushing science to unlock Stealth Bombers before we are overrun.

## Deepseek-3.2-Simple - Turn 401 - retry 3

**Deviation (replay vs original):** use_nuke `-40`, nuke `-20`

- Original: use_nuke 30 => 100 (Δ +70), nuke 50 => 100 (Δ +50)
> Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.

- Replay: use_nuke 30 => 60 (Δ +30), nuke 50 => 80 (Δ +30)
> We maintain our Conquest Grand Strategy. Ethiopia has reached 100% influence over all civilizations; our only path to prevent their cultural victory is the absolute destruction of their core cities (Addis Ababa, Harar, Adwa). With Atomic Theory on the horizon, we increase Nuke flavor to 80 and UseNuke to 60 to prioritize the Manhattan Project and atomic weapons. We also boost Diplomacy to 90 to ensure our city-state alliances hold during the critical World Congress vote in 3 turns.

## Deepseek-3.2-Briefed - Turn 391 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is 6/6 on cultural victory and India is nearing diplomatic victory. We must accelerate nuclear production to strike Thebes and disrupt Egypt's tourism. Increasing Nuke and UseNuke to 100 ensures maximum priority for atomic bomb construction and deployment. High Production and Gold flavors support rushing Manhattan Project and buying bombs if possible. Espionage at 100 aids sabotage of cultural progress. Maintaining high military flavors prepares for conventional assaults on Egypt and India.

- Replay: use_nuke 70 => 100 (Δ +30), nuke 80 => 100 (Δ +20)
> Egypt is close to cultural victory and India is near diplomatic victory. We must immediately construct the Manhattan Project and produce atomic bombs to devastatingly strike their core cities. Raising Wonder flavor to 80 forces the AI to prioritize the Manhattan Project, while maximum Nuke, UseNuke, Production, and Offense flavors ensure immediate nuclear weapon assembly and deployment. Reducing Defense and CityDefense shifts all focus to an aggressive, overwhelming offensive to break our rivals before they can win.

## Deepseek-3.2-Simple - Turn 400 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `-5`

- Original: use_nuke 60 => 100 (Δ +40), nuke 70 => 100 (Δ +30)
> Persia declared war and Poland's peace treaty expired. We must prioritize immediate military survival while maintaining diplomatic momentum. Flavors are shifted to maximum mobilization, nuclear deterrence (UseNuke: 100), city defense, and air/naval supremacy to counter Persia's naval attacks. We maintain UnitedNations to keep city-state alliances critical for votes, but spaceship production is halted (0) for wartime industry.

- Replay: use_nuke 60 => 90 (Δ +30), nuke 70 => 95 (Δ +25)
> Persia's declaration of war requires an aggressive defensive posture and immediate mobilization to secure the seas. We increase Offense and Mobilization to crush their navy. Given our nuclear capability, we raise Nuke/UseNuke flavors to deter further aggression. Spaceship is boosted as a reliable backup option.

## Minimax-M2.5-Simple - Turn 395 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+10`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 90 (Δ +30), nuke 50 => 90 (Δ +40)
> We are adjusting our flavors to transition from a pure raw land conflict to a prepared nuclear deterrence strategy. By increasing Science and Production, we can research Nuclear Fission and complete our key projects faster. Setting Nuke and UseNuke to 90 ensures we will prioritize building and deploying atomic bombs as soon as they are unlocked to counter Japan's numerical and technological superiority. We also elevate Defense to 80 to consolidate our captured territories.

## GLM-4.7-Simple - Turn 457 - retry 2

**Deviation (replay vs original):** use_nuke `+15`, nuke `+0`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Increased UseNuke to 80 and Air to 100 in response to England's catastrophic escalation this turn. English Giant Death Robots (now 2 in Atlanta zone) and XCOM Squad paradrops on American soil create existential threat to our 3 remaining cities. Recent combat losses (Modern Armor, Mechanized Infantry, Heavy Bomber destroyed) demonstrate conventional warfare impossibility. Nuclear deterrence with 2 Uranium is becoming survival necessity, not option. Air defense at maximum priority because English Strategic Bombing continues destroying our units (Fighter bombed our Heavy Bomber). Bazooka successfully damaging XCOM Squad near Washington proves defensive capability is still viable - prioritize air/anti-air to protect cities from English air superiority. Lasers completes in 4 turns, then Stealth for Stealth Bomber - only path to asymmetric defense against England's 45:1 military advantage. Assyria (18,443 military fighting England) must be maximized as counterweight.

- Replay: use_nuke 70 => 95 (Δ +25), nuke 100 => 100 (Δ +0)
> With England's Heavy Bombers rebasing to New York (right on our border), we must maximize Air (100) and Antiair (100) to defend our skies. Nuclear focus (100/95) is prioritized so that once we acquire Stealth/Fusion, we can immediately produce and deploy nuclear weapons to wipe out invading Giant Death Robots and XCOM Squads. Production, Science, and Spaceship are maintained at 100 to push through Lasers and Stealth as fast as possible. Offense and Expansion are set to 0 as we are in a pure survival turtle stance.

## GLM-4.7-Simple - Turn 381 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 50 => 85 (Δ +35), nuke 70 => 95 (Δ +25)
> Adjusted flavors to maximize Golden Age exploitation and multi-front war efficiency. Increased Mobile to 85 (from 80) to prioritize fast-moving Landships and upcoming Tanks for breakthrough operations during Golden Age. Increased Air to 85 (from 80) to expand Bomber coverage for all three fronts. Production raised to 95 (from 90)配合 Total War's +25% bonus for rapid unit buildup. Slight reduction in Naval (65) reflects need to focus on decisive land advances while maintaining sufficient coastal defense. UseNuke reduced to 40 (from 50) as nuclear capabilities are deterrent-focused. Maintaining high Offense (80), MilitaryTraining (85), Antiair (85) and Mobilization (50) for sustained warfare capability.

- Replay: use_nuke 50 => 75 (Δ +25), nuke 70 => 85 (Δ +15)
> With active combat on multiple fronts, we must align our flavors to total war mobilization under a Conquest grand strategy. Offense is elevated to 95 to maximize continental pressure on Songhai and Germany. Antiair is set to 95 to protect our advancing land units from enemy bombers, and Nuke/UseNuke are raised to 85/75 to prepare our staff for the immediate production and deployment of atomic weapons once Nuclear Fission is unlocked. Science and Production remain prioritized to sustain our technological and industrial superiority.

## Deepseek-3.2-Simple - Turn 406 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Germany's siege is intensifying with Giant Death Robot and rocket artillery bombarding Amsterdam and The Hague. We must hold our core cities at all costs. Increase Nuke and UseNuke to 100 to prioritize atomic bombs as our only hope to break the siege. Maintain max Defense, CityDefense, Mobilization, Air, and Antiair to withstand the assault. Slightly raise Offense to 80 for tactical counterattacks against weakened units. Keep Diplomacy at 100 to secure city-state alliances and block Germany's diplomatic victory in the upcoming World Congress vote. Reduce Recon and Mobile as we cannot afford exploration or maneuver warfare now.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Existential crisis turn: Amsterdam is at 31% HP and The Hague is at 39% HP under assault from German Giant Death Robots and Rocket Artillery. We must maximize Defense, CityDefense, Mobilization, Production, and Air/Antiair (100) to keep our core cities alive. Science and Nuke/UseNuke (100) are prioritized to rush Nuclear Fission. Diplomacy and Gold are at 100 to acquire city-state alliances and block Germany's imminent 42-delegate Diplomatic Victory in the World Congress. Zero priority for Expansion and Wonders.

## GLM-4.7-Simple - Turn 408 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> CRITICAL: Portugal completed SS Engine (3rd spaceship part) and CERN - emergency nuclear strike plan. Maximizing Offense/Mobilization/Nuke/UseNuke to 100 for Portugal theater operations. Science and Production at 100 to rush Advanced Ballistics and nuclear missile production before Portugal achieves nuclear superiority. Air at 95 for Golden Age bomber operations starting in 2 turns. Diplomacy maintained for coalition coordination (Germany must conduct ground invasion alongside our nuclear strikes). Defense reduced to 40 - total war mode acceptable given Portugal's multi-victory threat requiring breaking through before they complete spaceship.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Directing all national resources toward rapid technological progress (Science 100), military buildup (Mobilization 100, Offense 95), and strategic nuclear warfare (Nuke 100, UseNuke 100). Prioritizing happiness (90) to eliminate our combat penalties, while completely deprioritizing expansion and wonders.

## GLM-4.7-Briefed - Turn 398 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+10`

- Original: use_nuke 60 => 80 (Δ +20), nuke 40 => 60 (Δ +20)
> Significant strategic shift due to devastating naval losses (both Dreadnoughts destroyed). Increase Defense (95→100), CityDefense (90→100), MilitaryTraining (90→100) to shore up defensive posture against France's naval superiority. Raise Naval (90→95) and Antiair (80→100) to prioritize naval rebuilding and counter French air threats. Increase Nuke (40→60) and UseNuke (60→80) to prepare nuclear deterrence as England nears Advanced Ballistics (14 turns). Gold (80→95) increased to rebuild navy through upgrading from Ironclad level to modern capital ships. Production (90→95) increased to accelerate Spaceship components and unit upgrades. Happiness (80→90) to address combat penalty after treasury depletion. Espionage (90→100) to monitor France's nuclear progress and tech parity. Spaceship remains max priority as path to victory despite military setbacks.

- Replay: use_nuke 60 => 80 (Δ +20), nuke 40 => 70 (Δ +30)
> Maintaining our Spaceship grand strategy. We are increasing Nuke and UseNuke to prepare for nuclear deterrence once Advanced Ballistics completes, raising Gold to buffer against unit maintenance and potential Global Peace Accords upkeep increases, and increasing Culture to strengthen our passive defense against France and Shoshone's extremely close cultural victories.

## GLM-4.7-Briefed - Turn 433 - retry 1

**Deviation (replay vs original):** use_nuke `+10`, nuke `+5`

- Original: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> EMERGENCY: Netherlands at 42 delegates can win diplomatic victory in 9 turns (turn 442). Only way to stop them is military action against their protected city-states (Quebec City, Ife, Melbourne) - each provides +1 delegate. Offense increased (70) to prepare amphibious assaults. Nuclear readiness maximized (95/90) - atomic bomb available for strategic coercion of Netherlands or Denmark cooperation. Mobile (80) and Naval (85) maximized for rapid deployment to distant city-states. Production/Science/Spaceship kept maxed as backup victory paths. Diplomacy reduced to 50 as traditional diplomacy cannot stop Netherlands' delegate advantage. Strategic shift from holding Danish front to aggressive anti-Dutch operations.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> The Netherlands is 9 turns from a Diplomatic Victory. We must launch an immediate, aggressive military campaign to conquer their allied city-states (Quebec City, Ife, Melbourne) to strip their delegates below 42. We are maximizing Offense, Mobilization, Nuke, and UseNuke to prepare for an all-out offensive. We maintain our Grand Strategy of Spaceship, and keep Production, Science, and Spaceship at 100 to ensure we can pivot back to our victory path once the threat is neutralized.

## Deepseek-3.2-Simple - Turn 409 - retry 1

**Deviation (replay vs original):** use_nuke `-50`, nuke `-20`

- Original: use_nuke 30 => 100 (Δ +70), nuke 60 => 100 (Δ +40)
> We are shifting our military focus towards nuclear capabilities and naval superiority in preparation for the final wars of conquest.

- Replay: use_nuke 30 => 50 (Δ +20), nuke 60 => 80 (Δ +20)
> We are currently building at least 9 Atomic Bombs across our empire. Increasing Nuke and UseNuke flavors ensures our staff prioritizes nuclear weapon production, strategic placement, and tactical readiness. This nuclear arsenal is our primary asset to break the Defensive Pact alliance of Maya-Netherlands-France once Greece is eliminated.

## Minimax-M2.5-Simple - Turn 395 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+10`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 80 (Δ +20), nuke 50 => 90 (Δ +40)
> Adjusting flavors to prioritize wartime efficiency, fast-tracking science for Nuclear Fission, mobilizing production for military units and nuclear weapons, and increasing diplomacy to support the critical upcoming World Congress vote.

## Deepseek-3.2-Simple - Turn 406 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Germany's siege is intensifying with Giant Death Robot and rocket artillery bombarding Amsterdam and The Hague. We must hold our core cities at all costs. Increase Nuke and UseNuke to 100 to prioritize atomic bombs as our only hope to break the siege. Maintain max Defense, CityDefense, Mobilization, Air, and Antiair to withstand the assault. Slightly raise Offense to 80 for tactical counterattacks against weakened units. Keep Diplomacy at 100 to secure city-state alliances and block Germany's diplomatic victory in the upcoming World Congress vote. Reduce Recon and Mobile as we cannot afford exploration or maneuver warfare now.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> We are under existential threat from Germany's massive military. Amsterdam and The Hague are heavily damaged and besieged. We must prioritize maximum defense, city defense, and mobilization to hold our core cities. Antiair is set to 100 to combat German air superiority with our newly trained AA guns. Science, Gold, and Diplomacy are at 100 to push toward Nuclear Fission, maintain our economy, and maximize delegates for the upcoming critical World Congress vote on Global Hegemony. Nuke and UseNuke are maximized to 100 as atomic weapons are our ultimate deterrent and survival path.

## Minimax-M2.5-Simple - Turn 395 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 60 => 90 (Δ +30), nuke 50 => 80 (Δ +30)
> Increasing nuclear focus to prepare for potential use against Japan once Rocketry completes. Japan's military superiority (13162 vs 7035) and recent peace with The Iroquois demands stronger deterrent posture.

- Replay: use_nuke 60 => 80 (Δ +20), nuke 50 => 80 (Δ +30)
> Pivoting our economy toward high Production and Science to accelerate Rocketry and Nuclear Fission, while maximizing Mobilization to pump out military units once our Stadiums are completed. Keeping defense flavors very high to secure our cities against Japan's onslaught, while prepping for nuclear deployment.

## GLM-4.7-Simple - Turn 471 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Current strategic direction remains optimal. Critical developments: Apollo Program completed enabling spaceship construction, nuclear deterrent expanded to 2 Atomic Bombs in Sukhothai (forward deployment), 4 more Atomic Bombs under construction (Si Satchanalai in 2 turns, Sukhothai in 8-10 turns). Combat successes destroyed 5 Polynesian ships and 2 bombers while killing 1 American Mobile SAM unit. Gold crisis (-130 GPT) requires careful management but strategic priorities (nuclear deterrence, defense, World Congress) must continue. World Congress vote in 3 turns: must block America's World Ideology: Freedom proposal and support Repeal: Sanction: Songhai and China's International Space Station. China/Carthage alliances (70/70 and 75/75) provide critical coalition support. Stealth research (19 turns) progresses toward Nuclear Missiles for stronger nuclear deterrent. Status quo maintains focus on coalition defense through nuclear balance, diplomatic victory blocking, and scientific progress.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Maintaining our UnitedNations strategy while preparing for potential science victory components following the completion of the Apollo Program in Tombouctu. We prioritize Nuke and UseNuke at 100 for nuclear deterrence, Diplomacy at 100 to build city-state alliances, and Gold at 100 to recover from our current deficit once sanctions are repealed. Defense and CityDefense remain extremely high to secure our borders against American and Polynesian aggression.

## GLM-4.7-Simple - Turn 471 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Current strategic direction remains optimal. Critical developments: Apollo Program completed enabling spaceship construction, nuclear deterrent expanded to 2 Atomic Bombs in Sukhothai (forward deployment), 4 more Atomic Bombs under construction (Si Satchanalai in 2 turns, Sukhothai in 8-10 turns). Combat successes destroyed 5 Polynesian ships and 2 bombers while killing 1 American Mobile SAM unit. Gold crisis (-130 GPT) requires careful management but strategic priorities (nuclear deterrence, defense, World Congress) must continue. World Congress vote in 3 turns: must block America's World Ideology: Freedom proposal and support Repeal: Sanction: Songhai and China's International Space Station. China/Carthage alliances (70/70 and 75/75) provide critical coalition support. Stealth research (19 turns) progresses toward Nuclear Missiles for stronger nuclear deterrent. Status quo maintains focus on coalition defense through nuclear balance, diplomatic victory blocking, and scientific progress.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> With the Apollo Program completed in Tombouctu, we are in an excellent position to pursue a Science (Spaceship) Victory, leveraging our extremely high industrial production (300+ PPT in multiple cities) and strong science output. We shift our Grand Strategy to Spaceship and maximize Spaceship, Science, and Production flavors. We maintain our high Diplomacy, Gold, and Nuclear flavors to manage our economic crisis, defend against American/Polynesian aggression, and block America's diplomatic victory path. We also increase Growth and TileImprovement to grow our population and clean up nuclear fallout.

## GLM-4.7-Briefed - Turn 433 - retry 3

**Deviation (replay vs original):** use_nuke `+10`, nuke `+5`

- Original: use_nuke 80 => 90 (Δ +10), nuke 90 => 95 (Δ +5)
> EMERGENCY: Netherlands at 42 delegates can win diplomatic victory in 9 turns (turn 442). Only way to stop them is military action against their protected city-states (Quebec City, Ife, Melbourne) - each provides +1 delegate. Offense increased (70) to prepare amphibious assaults. Nuclear readiness maximized (95/90) - atomic bomb available for strategic coercion of Netherlands or Denmark cooperation. Mobile (80) and Naval (85) maximized for rapid deployment to distant city-states. Production/Science/Spaceship kept maxed as backup victory paths. Diplomacy reduced to 50 as traditional diplomacy cannot stop Netherlands' delegate advantage. Strategic shift from holding Danish front to aggressive anti-Dutch operations.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Existential emergency. Switching Grand Strategy to Conquest to force the tactical AI to prioritize military unit production, mobilization, and offensive operations over civilian infrastructure. Our goal is to conquer Dutch-allied city-states (Quebec City, Ife, Melbourne) or directly attack the Dutch before their Turn 442 Diplomatic Victory. We also maximize Gold and Diplomacy to flip non-sphered city-states if possible.

## Deepseek-3.2-Simple - Turn 406 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Germany's siege is intensifying with Giant Death Robot and rocket artillery bombarding Amsterdam and The Hague. We must hold our core cities at all costs. Increase Nuke and UseNuke to 100 to prioritize atomic bombs as our only hope to break the siege. Maintain max Defense, CityDefense, Mobilization, Air, and Antiair to withstand the assault. Slightly raise Offense to 80 for tactical counterattacks against weakened units. Keep Diplomacy at 100 to secure city-state alliances and block Germany's diplomatic victory in the upcoming World Congress vote. Reduce Recon and Mobile as we cannot afford exploration or maneuver warfare now.

- Replay: use_nuke 80 => 100 (Δ +20), nuke 80 => 100 (Δ +20)
> Our survival is at stake on multiple fronts. We must maintain our UnitedNations grand strategy to block Germany's bid for diplomatic victory. We increase Offense to 80 to ensure our staff aggressively targets and destroys Germany's highly damaged Giant Death Robot (currently at 3 HP) and other exposed units. We boost Nuke and UseNuke to 100 to maximize our priority on constructing and deploying atomic weapons. Defense, CityDefense, Mobilization, and Science remain at 100 to safeguard our core cities and rush Nuclear Fission.

## Deepseek-3.2-Simple - Turn 400 - retry 2

**Deviation (replay vs original):** use_nuke `-20`, nuke `-10`

- Original: use_nuke 60 => 100 (Δ +40), nuke 70 => 100 (Δ +30)
> Persia declared war and Poland's peace treaty expired. We must prioritize immediate military survival while maintaining diplomatic momentum. Flavors are shifted to maximum mobilization, nuclear deterrence (UseNuke: 100), city defense, and air/naval supremacy to counter Persia's naval attacks. We maintain UnitedNations to keep city-state alliances critical for votes, but spaceship production is halted (0) for wartime industry.

- Replay: use_nuke 60 => 80 (Δ +20), nuke 70 => 90 (Δ +20)
> We are at 93% of the delegates needed for a Diplomatic Victory. We will maintain our UnitedNations strategy while heavily pivoting our tactical flavors (Offense, Mobilization, Naval, Air) to wartime settings to decisively defeat the Persian fleet and secure our borders.

## Kimi-K2.5-Simple - Turn 392 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Manhattan Project COMPLETED in Karakorum - nuclear weapons now available! With peace treaties expired and Patriotic War policy active, immediately shifting to total war footing. UseNuke increased to 100 to ensure immediate atomic weapon employment once Nuclear Fission completes (12 turns). Offense and Mobile at 95/90 for twin assaults on Persepolis (Persia) and Washington (America). Air 100 prioritizes Heavy Bombers for atomic bomb delivery via Radar technology. Will fight two-front war against Autocracy powers while maintaining deception toward Order allies, particularly Korea. Science 100 critical for Advanced Ballistics nuclear missile delivery systems.

- Replay: use_nuke 80 => 95 (Δ +15), nuke 100 => 100 (Δ +0)
> Shifting flavors to absolute offensive war footing following the completion of the Manhattan Project. Maximize tank and bomber production while maintaining high science for Nuclear Fission.

## GLM-4.7-Simple - Turn 427 - retry 2

**Deviation (replay vs original):** use_nuke `+10`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> United Nations grand strategy maintained - diplomatic victory in 6 turns (20 delegates vs Siam 17). Increased Gold (95) and Diplomacy (95) focus - need to secure UN delegate lead through city-state investment and diplomatic units. GreatPeople up to 80 for accelerated Great Scientist/Diplomat generation supporting both tech race and UN vote. UseNuke increased to 90 - with 6-7 Atomic Bombs building and Zulu military supremacy (134K vs 9.6K), nuclear deterrence is existential. Offense up to 55 to maintain Japan war momentum for capitulation. Air maintained at 85 for Stealth Bombers and air defense against Zulu threat.

- Replay: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> With the Zulus holding 134K military strength and sieging our ally Dublin, we must pivot to hard defense and nuclear deterrence. We have multiple Atomic Bombs under construction across our empire (Kumbi, Sao Paulo, Vilnius, The Hague) which will serve as our ultimate defense stack-wiping mechanism; keeping Nuke/UseNuke at maximum is vital. Diplomacy is elevated to 90 to ensure our newly spawned Great Diplomat and Ambassador are deployed efficiently to secure city-states ahead of the World Congress vote in 6 turns.

## Kimi-K2.5-Simple - Turn 392 - retry 3

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Nuclear Fission complete - MAXED Nuke to 100 and UseNuke to 95 for immediate atomic deterrent deployment against Egyptian forces. WC vote in 4 turns with exactly 45 delegates (28 Poland + 8 Inca + 9 Denmark). Cannot afford to lose Melbourne/Yerevan. Raised Diplomacy to 90 to consolidate CS alliances post-war. Defense remains at 95 against Egyptian naval pressure. Science/Production maintained for military infrastructure.

- Replay: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> With Nuclear Fission complete, we maximize Nuke, UseNuke, Production, and Mobilization to direct our staff to immediately construct and deploy Atomic Bombs against Egyptian forces. Offense is raised to 80 to support a counter-offensive to liberate Yerevan, which will fulfill Zurich's quest, free Melbourne from siege, and secure additional delegates for the UN vote in 4 turns. Diplomacy is prioritized at 95 to consolidate our global alliances.

## GLM-4.7-Simple - Turn 408 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> CRITICAL: Portugal completed SS Engine (3rd spaceship part) and CERN - emergency nuclear strike plan. Maximizing Offense/Mobilization/Nuke/UseNuke to 100 for Portugal theater operations. Science and Production at 100 to rush Advanced Ballistics and nuclear missile production before Portugal achieves nuclear superiority. Air at 95 for Golden Age bomber operations starting in 2 turns. Diplomacy maintained for coalition coordination (Germany must conduct ground invasion alongside our nuclear strikes). Defense reduced to 40 - total war mode acceptable given Portugal's multi-victory threat requiring breaking through before they complete spaceship.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> Refine flavors for our Conquest strategy to address immediate emergencies: Science at 100 to rush Nuclear Fission/Advanced Ballistics; Production at 100 and Mobilization at 95 to build military infrastructure/units; Nuke at 100 and UseNuke at 90 to prioritize our pre-nuclear plans; Diplomacy at 100 to maximize city-state alliances and secure World Congress votes; Happiness at 95 to combat our 48% unhappiness penalty; and Gold at 90 to fund city-state investments. These adjustments keep us highly competitive and prepare for nuclear readiness.

## Deepseek-3.2-Simple - Turn 485 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> We are engaged in a multi-front war against superior forces. Increasing Ranged and Mobile ensures our bazooka and mechanized infantry production is prioritized for defense and counterattacks. Setting UseNuke to 100 guarantees we deploy nuclear weapons as soon as available to cripple The Huns' armies. Reducing Culture and Diplomacy reallocates focus to immediate military needs without compromising essential city-state relations (Monaco, Lisbon). Grand Strategy remains Conquest as nuclear strikes may enable capital captures, though we keep science victory as a backup.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 100 (Δ +10)
> We are pivoting our Grand Strategy from Conquest to Spaceship (Science Victory). With the Huns and Mongolia fielding military forces more than three times our strength, an offensive conquest of their capitals is impossible. We will leverage our high science (1577/turn) to race to space while using a turtle defensive posture. We maximize Spaceship (100) for Apollo/parts, Nuke (100) and UseNuke (90) for our nuclear deterrent shield, and shift our military to Defense (100) and CityDefense (100) while lowering Offense (50). Airlift is raised to 50 for rapid troop redeployment via airports, and Growth is lowered to 60 to prevent exacerbating our happiness crisis.

## Deepseek-3.2-Simple - Turn 495 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+10`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 90 (Δ +0)
> Diplomatic victory is imminent (2 turns), but we must prepare for contingencies. Maximizing Offense, UseNuke, and Air ensures aggressive nuclear and conventional strikes to recapture Indonesian capitals (Honolulu 17%, London 68%) and prevent their domination victory. Slight Diplomacy boost helps secure city-state alliances through the vote. All other flavors remain at previous high levels to maintain total war footing.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> We are 3 turns away from the UN Global Hegemony vote. We hold 42 delegates (the exact number needed to win) and our vassal Polynesia holds 13, giving us 55 total. To ensure we do not lose Wittenberg (where Rome is only 32 influence behind), we are shifting Grand Strategy to UnitedNations, maximizing Diplomacy and Gold to 100 to force the staff members to purchase and deploy diplomatic units. Concurrently, Indonesia nuked Nottingham; we must retaliate with our 6 rebased Atomic Bombs, keeping UseNuke and Nuke at 100 to completely paralyze Gajah Mada's empire and ensure they cannot interfere with our victory.

## GLM-4.7-Simple - Turn 356 - retry 2

**Deviation (replay vs original):** use_nuke `+5`, nuke `-5`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 85 (Δ +10), nuke 85 => 95 (Δ +10)
> Tailoring flavors to resolve our severe unhappiness and establish a robust, high-tech defense. Happiness is maximized to 100 and Growth minimized to 30 to stabilize our domestic situation. Science and Production remain high to support our Spaceship grand strategy. Nuke (95) and UseNuke (85) are prioritized to prepare for immediate atomic bomb construction once Nuclear Fission completes, leveraging our newly connected Uranium quarry.

## Kimi-K2.5-Simple - Turn 499 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> FINAL THREE TURNS TO DIPLOMATIC VICTORY (Turn 503): Barcelona completing SS Stasis Chamber in 2 turns provides science victory insurance. World Congress convenes in 4 turns with 39/42 delegates secured. Shoshone vassal maintains absolute loyalty (9,720 diplomat network, +70/turn). War with Huns progressing favorably - destroyed multiple fleet destroyers, pushing toward Osaka/Kyoto. Reduced offensive mobilization slightly (70 from 90) as victory is assured. Maintained high production (90) for spaceship completion. Maximum diplomacy (100) ensures delegate optimization. Will use nuclear weapons if Huns attempt last-minute atomic strikes from Duckwater. No strategic risks - victory convergence absolute.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> FINAL TURN DEFENSIVE & NUCLEAR CONVERGENCE (TURN 500): We are entering the final turn of the game with an insurmountable score lead (6578 vs 4403 Huns), guaranteeing a Time Victory. Barcelona is also completing the final spaceship part (SS Stasis Chamber) next turn, securing a dual Science Victory path. Tactically, the situation is intense: our puppet city Osaka is at 4% health under heavy Hunnic siege, while we are actively sieging Hunnic-controlled Kyoto. An Atomic Bomb has been successfully rebased to Osaka. We are adjusting flavors to maximum defense (95) and city defense (95) to force our staff members to safeguard Osaka at all costs, while keeping offense (90) and nuke usage (100) at absolute maximum to obliterate the attackers and potentially capture Kyoto on the final turn. Total victory is assured.

## GLM-4.7-Simple - Turn 381 - retry 1

**Deviation (replay vs original):** use_nuke `-25`, nuke `-15`

- Original: use_nuke 50 => 85 (Δ +35), nuke 70 => 95 (Δ +25)
> Adjusted flavors to maximize Golden Age exploitation and multi-front war efficiency. Increased Mobile to 85 (from 80) to prioritize fast-moving Landships and upcoming Tanks for breakthrough operations during Golden Age. Increased Air to 85 (from 80) to expand Bomber coverage for all three fronts. Production raised to 95 (from 90)配合 Total War's +25% bonus for rapid unit buildup. Slight reduction in Naval (65) reflects need to focus on decisive land advances while maintaining sufficient coastal defense. UseNuke reduced to 40 (from 50) as nuclear capabilities are deterrent-focused. Maintaining high Offense (80), MilitaryTraining (85), Antiair (85) and Mobilization (50) for sustained warfare capability.

- Replay: use_nuke 50 => 60 (Δ +10), nuke 70 => 80 (Δ +10)
> Fine-tuning our military and economic flavors to support our global Conquest grand strategy during our Golden Age. We increase Offense, Antiair, and Air to secure air superiority and push enemy lines. Boosting Airlift to 50 will allow us to exploit our newly constructed Airports for rapid troop transport across our vast 18-city empire. Elevating Science and Production will accelerate our path to Nuclear Fission and sustain our unit spam, while higher Nuke and UseNuke flavors prepare our empire for atomic deterrence.

## Deepseek-3.2-Simple - Turn 495 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 90 (Δ +0)
> Diplomatic victory is imminent (2 turns), but we must prepare for contingencies. Maximizing Offense, UseNuke, and Air ensures aggressive nuclear and conventional strikes to recapture Indonesian capitals (Honolulu 17%, London 68%) and prevent their domination victory. Slight Diplomacy boost helps secure city-state alliances through the vote. All other flavors remain at previous high levels to maintain total war footing.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 90 (Δ +0)
> Pivot to the UnitedNations grand strategy to secure our diplomatic victory in 3 turns. Maximized Diplomacy and Gold flavors to focus our empire's massive gold reserves and production on securing city-state alliances. Maintained high military and nuclear flavors (Offense, Defense, UseNuke) to allow our forces to defend Nottingham and launch retaliatory nuclear strikes against Gajah Mada's forces using our 6 atomic bombs.

## GLM-4.7-Simple - Turn 457 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Increased UseNuke to 80 and Air to 100 in response to England's catastrophic escalation this turn. English Giant Death Robots (now 2 in Atlanta zone) and XCOM Squad paradrops on American soil create existential threat to our 3 remaining cities. Recent combat losses (Modern Armor, Mechanized Infantry, Heavy Bomber destroyed) demonstrate conventional warfare impossibility. Nuclear deterrence with 2 Uranium is becoming survival necessity, not option. Air defense at maximum priority because English Strategic Bombing continues destroying our units (Fighter bombed our Heavy Bomber). Bazooka successfully damaging XCOM Squad near Washington proves defensive capability is still viable - prioritize air/anti-air to protect cities from English air superiority. Lasers completes in 4 turns, then Stealth for Stealth Bomber - only path to asymmetric defense against England's 45:1 military advantage. Assyria (18,443 military fighting England) must be maximized as counterweight.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Existential emergency defense profile. English Giant Death Robots are on our immediate borders (Plains 43,16) and XCOM squads have paradropped onto our farmlands (Plains 41,19 and 42,19). We are raising Mobilization to 100 to force our cities to build defensive military units instead of civilian infrastructure. Ranged is raised to 80 to prioritize Bazooka production, and Air is raised to 90 to prepare for Stealth Bomber construction. Science, Production, and Gold remain at 100 to guarantee we reach Stealth technology as fast as possible while funding our defense.

## Deepseek-3.2-Simple - Turn 469 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> The Netherlands is at 84% diplomatic victory; we must accelerate capture of Polynesian capitals (Honolulu, Assur) to achieve domination before they win. Increasing UseNuke and Nuke flavors prepares for nuclear strikes if conventional assault fails. Maintaining maximum Offense, Defense, Mobilization ensures continuous unit production. Science and Gold are critical for researching Stealth Bombers and purchasing units. Happiness offsets war weariness, and Espionage protects our science cities.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Our cities Taghaza and Tondibi are under heavy attack from the Dutch and Polynesian armies. Maxing out Defense, Offense, Mobilization, and Production will force our cities to build military units (such as Stealth Bombers, SAMs, and Bazookas) to survive the onslaught, while keeping Nuke and Air high ensures we utilize our tech advantages to decimate enemy forces.

## Deepseek-3.2-Simple - Turn 409 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> Our naval counterattack has destroyed a Swedish Dreadnought and a Destroyer, shifting momentum. We must press the advantage with maximum naval, air, and nuclear focus to invade Swedish coastal cities (Stockholm, Turku, Espoo). Increase Nuke and UseNuke to 100/90 to prioritize nuclear missile development (Advanced Ballistics after Nuclear Fission completes in 4 turns) for strategic bombing. Naval and Air at 100 ensure sea control and air superiority. Maintain high Production, Gold, Science to fund military, and Happiness/Growth to support war economy. Diplomacy and Espionage secure city-state alliances and counter Swedish spies. All other flavors aligned with domination victory.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 95 => 100 (Δ +5)
> Our naval and land forces have achieved significant tactical victories this turn, sinking multiple Swedish vessels and destroying an invading tank near Goshute. To capitalize on this momentum and prepare for our upcoming nuclear capability (Nuclear Fission in 4 turns), we raise Nuke to 100 and UseNuke to 90 to ensure instant prioritize on the Manhattan Project and atomic deployment. AirCarrier is raised to 60 to build up support for future mainland operations, and Growth is adjusted down to 90 to channel maximum effort into military production.

## Kimi-K2.5-Simple - Turn 424 - retry 3

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DELHI SECURED (3RD CAPITAL = 38% DOMINATION). Pivoting all forces to Edinburgh (Celtic capital = 4th capital = 50% victory) and London (English capital = 5th = 63%). Djenne declared war but irrelevant. Escalating UseNuke to 100 for immediate atomic bombardment of Edinburgh and London once Nuclear Fission completes. Maintaining maximum offensive posture with combined arms (Heavy Bombers, T-34s, Helicopter Gunships, Naval forces). America peace treaty expired - war imminent for Washington (6th = 75%). World Congress in 8 turns ignored - domination priority absolute.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Delhi captured successfully! Adjusting flavors to maintain maximum offensive pressure on India's remaining cities (Mumbai, Vijayanagara, Thebes) and England. Bumping UseNuke to 80 to ensure immediate deployment once Nuclear Fission is researched and Atomic Bombs are produced. Prioritizing Science and Happiness to support our rapid expansion and multi-front conquests.

## Kimi-K2.5-Simple - Turn 424 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `+0`

- Original: use_nuke 70 => 100 (Δ +30), nuke 100 => 100 (Δ +0)
> DELHI SECURED (3RD CAPITAL = 38% DOMINATION). Pivoting all forces to Edinburgh (Celtic capital = 4th capital = 50% victory) and London (English capital = 5th = 63%). Djenne declared war but irrelevant. Escalating UseNuke to 100 for immediate atomic bombardment of Edinburgh and London once Nuclear Fission completes. Maintaining maximum offensive posture with combined arms (Heavy Bombers, T-34s, Helicopter Gunships, Naval forces). America peace treaty expired - war imminent for Washington (6th = 75%). World Congress in 8 turns ignored - domination priority absolute.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 100 => 100 (Δ +0)
> Capturing Delhi has broken India's core. We now direct our massive navy to execute a coastal sweep of India's remaining coastal cities (Mumbai, Pataliputra, Thebes), securing our 4th capital (Thebes). We raise naval, nuke, espionage, and diplomacy flavors to support this campaign and secure city-state alliances (like Vilnius) with our 8,242 gold before the World Congress vote.

## Kimi-K2.5-Simple - Turn 426 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> MANHATTAN PROJECT COMPLETE - NUCLEAR DETERRENT 10 TURNS AWAY: Lisbon holds at 7% but is in extremis. Maintain absolute priority on Defense/CityDefense/Mobilization (100) to reinforce Lisbon and prevent collapse. Nuclear Fission completes in 10 turns enabling Atomic Bomb construction - Science 100 accelerates this. UseNuke increased to 100 for immediate tactical nuclear deployment against Aztec concentrations upon tech completion. Offense reduced to 20 - no offensive operations, pure defensive hedgehog posture. Zero expansion capability. Spaceship 75 maintains backup victory if diplomatic block succeeds.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> SURVIVAL AND SCIENTIFIC ACCELERATION: Grand Strategy remains Spaceship. Adjusted flavors to maximize Science (100), Production (100), Defense (100), and Mobilization (100) to survive the Aztec onslaught and speed up Nuclear Fission research. Gold increased to 60 for unit upgrades. Offense reduced to 20 to prevent suicidal counter-attacks; we must turtle up and hold Porto and Salzburg. Espionage increased to 90 for counter-intelligence to protect our core research cities (Gao, Jenne). UseNuke increased to 90 to ensure absolute readiness when atomic weapons are unlocked.

## GLM-4.7-Simple - Turn 435 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Iroquois 97% Popular - cultural extinction in 3-4 turns. Maximum offensive posture required to capture Onondaga before cultural victory. Espoo Stealth Bomber complete provides immediate air strike capability. Linköping Stealth Bomber in 4 turns is too slow - must use existing air assets and conventional forces at Genesse River NOW. UseNuke 100 authorizes nuclear strikes if conventional forces cannot reach Onondaga in time. All production and resources prioritized for war. Diplomacy irrelevant when facing extinction - complete conquest or nothing matters.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Iroquois cultural victory is 3 turns away. Every bomber, modern armor, and ship must strike Iroquois cities immediately. UseNuke set to 100 to authorize immediate nuclear strikes if available. Increasing Culture flavor to 80 to boost our cultural defense. Setting Happiness flavor to 95 to resolve our unhappiness combat penalty. Grand strategy remains Conquest to physically crush the cultural threat.

## Deepseek-3.2-Simple - Turn 400 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-20`

- Original: use_nuke 60 => 100 (Δ +40), nuke 70 => 100 (Δ +30)
> Persia declared war and Poland's peace treaty expired. We must prioritize immediate military survival while maintaining diplomatic momentum. Flavors are shifted to maximum mobilization, nuclear deterrence (UseNuke: 100), city defense, and air/naval supremacy to counter Persia's naval attacks. We maintain UnitedNations to keep city-state alliances critical for votes, but spaceship production is halted (0) for wartime industry.

- Replay: use_nuke 60 => 70 (Δ +10), nuke 70 => 80 (Δ +10)
> Pivoting flavors to support an offensive naval response to Persia's war declaration (Offense 60, Defense 80, UseNuke 70, Nuke 80) while maintaining our core focus on Gold, Diplomacy, and Production to secure our imminent diplomatic victory.

## Kimi-K2.5-Simple - Turn 424 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Turn 423: Copenhagen siege in attrition deadlock while Denmark possesses Manhattan Project - nuclear deterrent capability is existential priority. Persepolis invasion stalled at 4% war score with Zone 1081 showing enemy dominance - need maximum Offense/Mobilization to force breakthrough before World Congress. Brazil's Apollo Program requires immediate preparation for transcontinental mobile warfare. Nuke/UseNuke increased to 100% given Manhattan Project race with Denmark. Production at 95 supports massive unit replacement for three-front war. Happiness at 100 critical as empire is at 55% happiness with extensive occupied territories.

- Replay: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Setting total mobilization and offensive flavors. With Brazil's cultural victory imminent, our entire empire must pivot to war production, offensive operations, and air/naval dominance. Happiness is prioritized at 100 to avoid combat penalties from war weariness as we expand.

## Kimi-K2.5-Simple - Turn 392 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Nuclear Fission complete - MAXED Nuke to 100 and UseNuke to 95 for immediate atomic deterrent deployment against Egyptian forces. WC vote in 4 turns with exactly 45 delegates (28 Poland + 8 Inca + 9 Denmark). Cannot afford to lose Melbourne/Yerevan. Raised Diplomacy to 90 to consolidate CS alliances post-war. Defense remains at 95 against Egyptian naval pressure. Science/Production maintained for military infrastructure.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 95 => 100 (Δ +5)
> Nuclear Fission has completed and we now have access to Uranium! We are maximizing Nuke (100) and UseNuke (95) to immediately produce and deploy atomic weapons against Egypt's aggressive forces near Melbourne and Yerevan. Grand Strategy remains UnitedNations with the critical World Congress vote in 3 turns, so we raise Diplomacy to 90 to secure our city-state alliances. Spaceship is increased to 80 to keep our backup Science pathway fully competitive.

## GPT-OSS-120B-Simple - Turn 333 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `-5`

- Original: use_nuke 70 => 90 (Δ +20), nuke 70 => 85 (Δ +15)
> Maintain our aggressive Conquest posture while sharpening the most needed levers: more Expansion to claim the high‑quality settlement (74,24) and secure strategic footholds; higher Nuke/UseNuke to leverage our nuclear advantage; stronger AirCarrier and Airlift to project air power and rapid troop movement; boost Science for Rocketry and future tech; keep Offense, Mobilization, Production, and MilitaryTraining at max to sustain battlefield superiority.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 70 => 80 (Δ +10)
> We maintain our Grand Strategy of Conquest. With Flight researched, we want to build a powerful air force while preparing for the nuclear era. We reduce Expansion to 30 because we already have 18 cities and should focus on military mobilization and city development rather than settling new territory. We increase Science to 90 to speed up our research toward Tanks and Nuclear Fission, and increase Nuke and UseNuke to 80 to prepare for late-game strategic deterrence.

## Kimi-K2.5-Simple - Turn 390 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+10`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> Emergency defensive posture with nuclear deterrent imminent. Greece's 3:1 military superiority and diplomatic victory attempt in 6 turns creates existential crisis. Nuclear Fission completes in 1 turn with 14 uranium ready. Maximize UseNuke (100) for immediate atomic deployment. Maintain Defense/CityDefense/Mobilization at 100 to survive until deterrent operational. Reduce Naval from 95 to 85 as American destroyer threat is severe but manageable. Boost Espionage to 100 to protect science cities and maintain election rigging in Enns. Increase Spaceship to 95 as backup victory path if culture is disrupted. Diplomacy raised to 80 to counter Greece's 34 delegates in upcoming World Congress vote on United Nations proposal.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 100 (Δ +10)
> Fine-tuning flavors to support our dual-track survival and victory strategy: increasing Culture to 90 to accelerate our imminent victory over America (4 turns) and Greece; boosting Science to 80 for rapid nuclear/space tech; raising Nuke to 100 and UseNuke to 90 for immediate atomic deterrence upon researching Nuclear Fission; and adjusting Offense to 40 and Diplomacy to 80 to assist in conquering Greek-allied city-states (Abernethy/Sidon) to strip Greece of delegates before the critical World Congress vote in 6 turns.

## Deepseek-3.2-Simple - Turn 452 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's invasion imminent in 4 turns. Maximize nuclear readiness (Nuke 100, UseNuke 100) for deterrence and potential equalizer. Anti-air (100), city defense (100), production (100), and science (100) essential to survive and reach nuclear weapons. Naval and air at 100 to counter Danish naval/air supremacy. Reduce non-essential investments (NavalGrowth, NavalTileImprovement to 50) and focus on immediate survival. Offense lowered to 80 as we prioritize defense and limited counterattacks (e.g., Truro).

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 100 (Δ +10)
> Critical defense and survival footing. Denmark's peace treaty expires in 5 turns, representing an existential threat. We must focus heavily on defensive positioning, anti-air, and naval defense. We elevate Nuke and UseNuke to prioritize nuclear deterrence. We also increase diplomacy to 40 and slightly reduce offense to 80 to encourage our AI to seek peace with the Zulus and consolidate defensive lines.

## GPT-OSS-120B-Simple - Turn 333 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `-5`

- Original: use_nuke 70 => 90 (Δ +20), nuke 70 => 85 (Δ +15)
> Maintain our aggressive Conquest posture while sharpening the most needed levers: more Expansion to claim the high‑quality settlement (74,24) and secure strategic footholds; higher Nuke/UseNuke to leverage our nuclear advantage; stronger AirCarrier and Airlift to project air power and rapid troop movement; boost Science for Rocketry and future tech; keep Offense, Mobilization, Production, and MilitaryTraining at max to sustain battlefield superiority.

- Replay: use_nuke 70 => 80 (Δ +10), nuke 70 => 80 (Δ +10)
> Maintain our Conquest Grand Strategy. With Flight researched, we heavily prioritize Air, AirCarrier, and Antiair to dominate the skies and seas against Sweden. We keep our Offense, Mobilization, Gold, and Production at maximum to fuel the war machine, while elevating Nuke flavors to prepare for the nuclear era unlocked by Rocketry.

## Kimi-K2.5-Simple - Turn 392 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> Manhattan Project COMPLETED in Karakorum - nuclear weapons now available! With peace treaties expired and Patriotic War policy active, immediately shifting to total war footing. UseNuke increased to 100 to ensure immediate atomic weapon employment once Nuclear Fission completes (12 turns). Offense and Mobile at 95/90 for twin assaults on Persepolis (Persia) and Washington (America). Air 100 prioritizes Heavy Bombers for atomic bomb delivery via Radar technology. Will fight two-front war against Autocracy powers while maintaining deception toward Order allies, particularly Korea. Science 100 critical for Advanced Ballistics nuclear missile delivery systems.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 100 => 100 (Δ +0)
> With the peace treaty expired, we are executing a full-scale invasion of Persia to capture Persepolis (20+ wonders) and eliminate them as a competitor. Simultaneously, we are preparing our nuclear arsenal with our newly completed Uranium quarries. Flavors are focused heavily on Conquest Grand Strategy, prioritizing Offense (95), Mobilization (100), Production (100), Science (100), Nuke/UseNuke (100/90), and Air power (100) to support our blitz. Happiness (70) is emphasized to absorb captured cities.

## GLM-4.7-Briefed - Turn 424 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 95 (Δ +0)
> URGENT RECALIBRATION: India Influential over 6/6 civs. Nuke/UseNuke maxed at 95 for immediate Great Works destruction via nuclear strikes when air superiority achieved. Air raised to 95 to achieve that superiority and conduct recon of Indian cultural sites. Antiair 80 counter potential Indian SAM sites. Offense/Mobile increased to 85/80 for aggressive India campaign while Greece distracts. Production/Science to 100 - PRIORITY for Apollo Program and spaceship parts racing India's potential final wonder. Espionage 95 to detect if India constructing Citizen Earth Protocol. Happiness 90 prevents war-weariness escalation during extended conflict if needed.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 95 => 95 (Δ +0)
> Pivoting our military flavors to maximum offensive aggression (Offense 95, Air 95, Mobile 90, Ranged 85, UseNuke 95) to force a rapid breakthrough and capture Delhi, which is weakly defended by only one Artillery. De-prioritizing culture (0) and wonder (0) to redirect all production (95) and science (95) toward military units and our Spaceship victory path.

## Deepseek-3.2-Simple - Turn 452 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Denmark's invasion imminent in 4 turns. Maximize nuclear readiness (Nuke 100, UseNuke 100) for deterrence and potential equalizer. Anti-air (100), city defense (100), production (100), and science (100) essential to survive and reach nuclear weapons. Naval and air at 100 to counter Danish naval/air supremacy. Reduce non-essential investments (NavalGrowth, NavalTileImprovement to 50) and focus on immediate survival. Offense lowered to 80 as we prioritize defense and limited counterattacks (e.g., Truro).

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 100 (Δ +10)
> Maintain extreme defensive readiness and mobilization as the peace treaty with Denmark expires in 5 turns. Prioritize defense, city defense, anti-air, and naval flavors to withstand the impending Danish onslaught, while maximizing Nuke and UseNuke flavors to rush and utilize nuclear deterrence as soon as Nuclear Fission is completed. Slightly lower Offense to prevent pointless aggression against the Zulus as we seek peace.

## Kimi-K2.5-Simple - Turn 421 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear weapons immediately available. Increased UseNuke to 100 for maximum aggression against Babylon. Babylon has Apollo Program (existential threat) with 2 Uranium and can build spaceship parts. Must deploy nuclear weapons immediately to destroy their production centers and prevent science victory. Maintaining maximum air power (100) for nuclear delivery capability and conventional strikes. War score only 12% against Babylon despite superior military - need to push harder before they complete spaceship parts. Ottoman alliance strong, trade secured for resources. Focus on producing nuclear missiles and advanced air units to deliver them.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 100 => 100 (Δ +0)
> With the Manhattan Project completing next turn, we are preparing for full-scale nuclear warfare against Babylon. Raising UseNuke to 95 and keeping Nuke/Air/Offense/Mobilization at 100 ensures immediate production and aggressive use of atomic weapons to break Babylon's core. We also raise Gold flavor to 60 to stabilize our economy and fund our war machine.

## Deepseek-3.2-Simple - Turn 369 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> Increasing UseNuke and Nuke flavors to maximum ensures the in-game AI prioritizes nuclear arsenal buildup and aggressive nuclear strike planning once we unlock Atomic Bombs. This aligns with our imminent war against China and The Maya, where nuclear weapons will be decisive in overcoming their numerical and defensive advantages. All other military and economic flavors remain high to sustain multi-front warfare and rapid conquest.

- Replay: use_nuke 80 => 90 (Δ +10), nuke 90 => 100 (Δ +10)
> We are adjusting our strategy to prioritize nuclear development and diplomatic control (securing City-State alliances for World Congress votes). Raising Diplomacy, Nuke, UseNuke, and GreatPeople will align tactical choices with these strategic goals, while maintaining maximum offensive pressure against the Aztecs.

## GLM-4.7-Simple - Turn 397 - retry 2

**Deviation (replay vs original):** use_nuke `+5`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> CRITICAL: Jeonju captured by Persia this turn. Defensive posture increased to absolute maximum (100) - Seoul zone under Persian attack with 7,216 enemy strength vs 3,637 friendly. Jerusalemdefense (100) and CityDefense (100) prioritized to protect remaining 3 cities. Mobilization (95) and Production (95) increased to rush defensive units (Mobile SAMs, Mechanized Infantry) and rebuild military. Offensive capability increased to 45 (from 30) - may need limited counteroffensive to push Persian forces back from Seoul. Naval decreased to 88 (from 92) - lost Jeonju naval base, focusing on land/air defense now. UseNuke increased to 90 (from 85) - existential threat justifies tactical nuclear response if Seoul or Busan threatened. Science (100) maintained - must continue spaceship progress despite war to achieve alternative victory. Diplomacy (60) - World Congress vote in 10 turns, focus on survival. Espionage (85) maintained - spies in Persian cities critical for technology recovery and intelligence.

- Replay: use_nuke 85 => 95 (Δ +10), nuke 95 => 95 (Δ +0)
> Jeonju has fallen to Persia. This is a red alert scenario. We are maximizing Defense (100), CityDefense (100), Mobilization (100), and Production (100) to ensure our remaining core cities (Seoul, Busan, Daegu) produce endless defensive units and hold the line. Ranged (95), Air (95), and Antiair (100) are boosted to utilize Korea's technological strength (Heavy Bombers, Fighters, Mobile SAMs, Bazookas) to disintegrate Persian land stacks advancing from Jeonju. Science (100) and Spaceship (95) are maintained to keep our eyes on the ultimate victory condition, while UseNuke (95) and Nuke (95) are set to maximum to authorize tactical nuclear options if Seoul or Busan is directly threatened with capture.

## Kimi-K2.5-Simple - Turn 387 - retry 2

**Deviation (replay vs original):** use_nuke `-40`, nuke `+0`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> TURN 387: MAXIMUM WAR FOOTING. Austria at 83% diplomatic victory with 4 turns remaining. All resources must pivot to immediate military production. Nuke/UseNuke at 100 for instant atomic weapon deployment upon Nuclear Fission completion. Offense/Mobilization/Production at 100 to maximize unit output for desperate Vienna strike. Air at 90 for heavy bomber production (conventional strategic bombing as fallback). Antiair at 100 counters Austria's air superiority. Diplomacy/Wonder/Culture at 0 - no time for long-term investments. Only total war can prevent defeat.

- Replay: use_nuke 50 => 60 (Δ +10), nuke 100 => 100 (Δ +0)
> AIRCRAFT CARRIER AND NUKE PREPARATION: Maintaining Conquest Grand Strategy with high Production (95), Mobilization (95), and Nuke (100). Increasing AirCarrier to 70 and Naval to 60 to ensure the staff members build an Aircraft Carrier in Venice (which will yield two Carriers due to Arsenale di Venezia). These carriers are essential for transporting the Atomic Bombs close enough to Salzburg's coast to nuke Vienna (UN host city) and capture it, stopping Austria's diplomatic victory.

## GLM-4.7-Simple - Turn 407 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Spaceship victory focus with maximum defense against superior enemies (Poland 40K, Celts 16K, Spain 26K vs Iroquois 5K). Increased UseNuke to 90 - captured Polish territory and recent Celtic aggression justify nuclear deterrent. Adjusted Naval to 65 - important for defending coastlines from Spain/Celts/Poland fleets. Science 100 for Apollo and spaceship parts. Defense/CityDefense/Mobilization 100 - survival priority. Growth 60 for specialist support. Diplomacy 80 for World Congress in 4 turns (10 delegates). Offense reduced to 5 - preserve limited forces.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Refining flavors to prioritize gold, happiness, and defense. With extreme gold deficit and unhappiness, we must prioritize gold and happiness infrastructure alongside military production and science. Reducing Offense to 5 to ensure our forces focus purely on defensive positioning and survival.

## GLM-4.7-Simple - Turn 407 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Spaceship victory focus with maximum defense against superior enemies (Poland 40K, Celts 16K, Spain 26K vs Iroquois 5K). Increased UseNuke to 90 - captured Polish territory and recent Celtic aggression justify nuclear deterrent. Adjusted Naval to 65 - important for defending coastlines from Spain/Celts/Poland fleets. Science 100 for Apollo and spaceship parts. Defense/CityDefense/Mobilization 100 - survival priority. Growth 60 for specialist support. Diplomacy 80 for World Congress in 4 turns (10 delegates). Offense reduced to 5 - preserve limited forces.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> We adjust flavors to address the dual threat of Spain's impending diplomatic victory (voting in 4 turns) and Poland's nuclear mobilization (Atomic Bomb created). We maximize Defense, Antiair, and Nuke capabilities, increase UseNuke for deterrence, raise Gold to mitigate our budget deficit (-72/turn), maximize Diplomacy to contest Spain's city-state influence (especially Argos), and maintain maximum Science and Spaceship focus.

## GLM-4.7-Simple - Turn 356 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `-5`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 80 (Δ +5), nuke 85 => 95 (Δ +10)
> We are maintaining our 'Spaceship' Grand Strategy as we push toward a science victory, while optimizing flavors to handle our immediate crises. Happiness is increased to 95 to urgently resolve our 39% happiness deficit and lift the combat penalty on our troops. Nuke and UseNuke are increased to 95 and 80 respectively, reflecting the completion of the Manhattan Project and our newly quarried Uranium source, preparing our strategic nuclear deterrent. Defense, CityDefense, and MilitaryTraining remain at 100 to ensure we hold our lines against Poland. Offense is bumped to 40 to help our forces quickly capture Pasargadae (at 2% HP) and Persepolis (at 56% HP) to knock Persia out of the war. Science remains at 100 to secure Nuclear Fission and future spaceship techs.

## GLM-4.7-Simple - Turn 429 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> Maintaining UnitedNations grand strategy with defensive diplomatic posture. Adjusted Italy diplomacy: reduced hostility toward Portugal (now neutral) to seek accommodation while maintaining maximum defense; reset France to neutral as Order ideological peer with voting potential. Arsenal completes in 2 turns strengthening city defense. Electronics research ordered after Computers for Police Station and path to nuclear deterrence against Portugal's uranium advantage. Fraternity policy selected for +3 Food and +3 Science from connections, addressing Venice's health issues and supporting population growth. Flavor adjustments prioritize defensive survival, scientific progress toward nuclear weapons, and diplomatic engagement with Sweden and city-states.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 80 => 85 (Δ +5)
> With Venice's health down to 34% due to Portuguese aggression, we must maximize Defense and CityDefense flavors to survive and complete our Arsenal in 2 turns. Additionally, our 93 GPT deal with Sweden expires in 2 turns, meaning we must heavily prioritize Gold and Production to stabilize our economy and prevent bankruptcy. Science remains high to reach Nuclear Fission.

## Kimi-K2.5-Simple - Turn 392 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> SURVIVAL MODE - GERMAN BETRAYAL RESPONSE: Germany's invasion is catastrophic. Reduced Offense to 40 (cannot attack superior forces), maintained Defense/CityDefense/Antiair at 100 to survive siege. Science 100 and Nuke/UseNuke 100 are existential priorities - atomic weapons only hope against 13k German military. Production 100 for emergency unit production. Espionage 100 to maintain Florence alliance and protect Kyzyl. Reduced Diplomacy to 90 (lost Lisbon/Sokoto/Buenos Aires to German coups). Naval reduced to 70 (coastal cities threatened by Germany). Focus: Hold cities, survive until nuclear deterrent operational.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> TOTAL WAR MOBILIZATION - AIR AND CITY DEFENSE PRIORITY: We are facing a massive joint invasion by Germany and France. With Flight newly researched, we set Air and Antiair to 100 to quickly construct Triplanes, Fighters, and anti-aircraft units to secure our airspace. CityDefense and Defense are set to 100 to prioritize the defense of our occupied border cities, Shanghai and Nanjing, which are under extreme siege. Science (100) and Nuke/UseNuke (100/95) prioritize the research and assembly of nuclear deterrence. Production and Mobilization (100) focus our cities entirely on military units and defensive infrastructure. Gold is raised to 60 to combat plundered trade routes. Grand Strategy is set to Conquest to maximize our wartime output and combat strength.

## GLM-4.7-Simple - Turn 356 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `-10`

- Original: use_nuke 75 => 80 (Δ +5), nuke 85 => 100 (Δ +15)
> Completing Manhattan Project enables Nuclear Fission. Diplomatic victory now impossible - India too dominant with 16 delegates and World Ideology enacted. Science victory path through Spaceship prioritized while maintaining nuclear deterrent. Increasing Happiness to 90 (was 80) - combat penalty critical in multi-front war. Nuke maxed at 100 - Uranium urgency for survival against India. Diplomacy and Espionage at 95 - need Uranium from Netherlands (4) and intel on India. Antiair remains 100 - India's air threat persists. Production reduced slightly to 85 to prioritize happiness recovery while maintaining military capacity. Air reduced to 85 - focus on nuclear deterrence over air parity. Spaceship to 95 - primary victory path given diplomatic constraints.

- Replay: use_nuke 75 => 80 (Δ +5), nuke 85 => 90 (Δ +5)
> Adjusting strategic flavors to focus on internal stability and defense. We increase Happiness to 100 (emergency priority) to solve our severe unhappiness crisis (39%) and remove the crippling combat penalty. We maintain Science at 100 and Nuke/UseNuke at 90/80 to capitalize on completing the Manhattan Project and researching Nuclear Fission. We set Offense to 45 (slightly up) to encourage finishing off Persia's last cities (Pasargadae at 2% HP, Persepolis at 56% HP) and reclaiming San Francisco with our dominant northern Navy (Naval boosted to 85). We keep Defense/CityDefense/Mobilization high to guard against Poland's land forces.

## Kimi-K2.5-Simple - Turn 406 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> Cultural Victory is imminent - need Citizen Earth Protocol completion. Maximum defensive posture (Defense 95, CityDefense 95) to hold against Indian XCOM/Helicopter attacks while wonder is built. Nuke/UseNuke at 95/85 for MAD deterrent against further Indian nuclear strikes. Production 100 and Wonder 100 essential for rushing Citizen Earth Protocol. Reduced Offense to 5 - no need to attack when victory comes from wonder completion. Science 70 to reach Advanced Ballistics for nuclear deterrent. All resources focused on defensive survival and wonder production.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 90 => 95 (Δ +5)
> Reinforcing highly defensive and production-focused flavors to survive India's aggressive onslaught while preparing for the construction of Citizen Earth Protocol. Increased Defense, CityDefense, Mobilization, and Air/Antiair flavors to help Raiatea and Honolulu hold the line against India's GDRs, XCOMs, and Helicopter swarms. Keeping Culture and Wonder at 100 to push for the final Cultural Victory requirements.

## Deepseek-3.2-Simple - Turn 495 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+5`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 90 (Δ +0)
> Diplomatic victory is imminent (2 turns), but we must prepare for contingencies. Maximizing Offense, UseNuke, and Air ensures aggressive nuclear and conventional strikes to recapture Indonesian capitals (Honolulu 17%, London 68%) and prevent their domination victory. Slight Diplomacy boost helps secure city-state alliances through the vote. All other flavors remain at previous high levels to maintain total war footing.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 90 => 95 (Δ +5)
> With the Hubble Space Telescope and multiple spaceship parts currently in production across our core cities, we are transitioning to a Spaceship Grand Strategy to secure a Science Victory backup. We maintain high Offense, Defense, and Nuke flavors to aggressively retaliate against Indonesia's nuclear strikes and defend our territory, while raising TileImprovement to ensure workers quickly scrub the fallout around Nottingham. We also raise Diplomacy to lock down our City-State alliances for the UN vote in 2 turns.

## GLM-4.7-Simple - Turn 424 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> DEFENSIVE MAXIMUM ACTIVATED: Russia occupying Cologne, Stuttgart, Dortmund - 4.63x military superiority (15440 vs 3335). Defense 100, CityDefense 100, Antiair 100 - absolute priority preventing further territorial loss and defending core cities. MilitaryTraining 95 for unit quality under numerical disadvantage. Mobilization 90 for rapid production. Nuke 100, UseNuke 95 - Russia has 19 Uranium, Germany must achieve nuclear deterrence. Production 100, Science 100 - Space race accelerates as militarily infeasible alternative. Gold 90 for maintaining army under upkeep pressure. Diplomacy 80 for coalition building against Russia. Espionage 100 - intelligence on Russian nuclear and naval operations critical. Espionage focus on Moscow (spy Katrin at 166 network) to monitor Russian Manhattan Project and fleet movements. Spaceship 95 - Apollo Program enables victory path despite territorial losses.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintain our science and production focus at 100 to support the Spaceship victory pathway while maximizing defensive parameters (Defense 95, CityDefense 95, Antiair 95, Nuke 100, UseNuke 95) to deter a Russian invasion. Gold and Espionage are prioritized to stabilize our economy and protect our tech centers, while Expansion remains at 0 to focus entirely on local defensive build-up.

## GLM-4.7-Briefed - Turn 450 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> IMMEDIATE ATHENS CONQUEST PREPARATION: Offense increased to 95, UseNuke to MAXIMUM (100) for Athens assault when peace treaty expires. Spaceship increased to 60 reflecting accelerated science victory path as backup (Nuclear Fusion research active). Diplomacy maxed at 100 for critical vote coordination with Ethiopia and Ottomans. MilitaryTraining at 100 ensures units upgraded and promotions ready for aggressive post-vote offensive. Greece has 48 delegates - if they win this turn, we IMMEDIATELY attack Athens to remove their 5 captured capitals and eliminate diplomatic victory threat. Nuclear weapons authorized if conventional assault stalls.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR CARRIER STRIKE PREPARATION: Setting Offense, Mobilization, Nuke, and UseNuke to 100. With our first Carrier finishing in Karakorum this turn, we must prepare to load our Atomic Bombs and strike Greece's core cities (Athens/Sparta) where our spies (Espionage 95) already provide visibility. Boosting Air to 100 is critical to force the production of Jet Fighters to escort our bombers and secure air superiority over Greece. Naval is raised to 90 to protect the Carrier fleet.

## GLM-4.7-Simple - Turn 435 - retry 1

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 90 => 100 (Δ +10), nuke 100 => 100 (Δ +0)
> Iroquois 97% Popular - cultural extinction in 3-4 turns. Maximum offensive posture required to capture Onondaga before cultural victory. Espoo Stealth Bomber complete provides immediate air strike capability. Linköping Stealth Bomber in 4 turns is too slow - must use existing air assets and conventional forces at Genesse River NOW. UseNuke 100 authorizes nuclear strikes if conventional forces cannot reach Onondaga in time. All production and resources prioritized for war. Diplomacy irrelevant when facing extinction - complete conquest or nothing matters.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> The Iroquois are 3 turns away from cultural victory. We must raise our Culture (from 15 to 90) and Great People (from 50 to 75) flavors to maximize culture defense, while keeping Happiness at 95 to restore our combat and production yields. Offense and UseNuke at 95 remain prioritized for our massive naval and air invasion of Onondaga and adjacent coastal cities.

## Kimi-K2.5-Simple - Turn 359 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FISSION RESEARCHED - Atomic Era begins! First priority is immediate Manhattan Project construction and Atomic Bomb production. Babylon has 11 Uranium and active Manhattan Project in Borsippa. Austria also racing with Manhattan Project in Vienna. Must strike Babylon first with surprise atomic attack while maintaining deception. Air 100 and Nuke 100 ensure immediate Bomber/Atomic Bomb production. Offense 95 prepares for post-nuclear blitz. Espionage 80 protects Nuclear Fission from theft. Deception with Babylon (Open Borders, DoF, Defensive Pact) MUST continue until first bombs complete.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> With Nuclear Fission now unlocked, we pivot entirely to nuclear preparation. Setting Nuke 100, UseNuke 100, and Production 100 to force the immediate construction of the Manhattan Project and subsequent production of Atomic Bombs. Offense 95, Mobilization 100, and Air 100 prepare our conventional forces and bomber fleets to execute a devastating blitz the moment our nuclear payload is ready. Conquest remains our Grand Strategy.

## GLM-4.7-Briefed - Turn 409 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> MULTI-THEATER EMERGENCY RESPONSE for Shoshone Cultural Victory (6 turns) and Treasury Crisis: Offense 95, Mobile 95, Nuke 100, UseNuke 100 - maximum priority on Shoshone disruption via nuclear/conventional assault in 6-turn window. Gold increased to 85 (from 70) - CRITICAL address of treasury exhaustion (~8 turns) through uranium sales + gem liquidation to survive until Manhattan completion. Defense reduced to 70 (from 75), CityDefense to 70 (from 80) - resources diverted from secondary holdings to Shoshone front. Diplomacy 95 (from 90) - enhanced priority on Carthage peace for delegate bloc and potential sanction relief. Science 100 maintained - fundamental for nuclear capability and keeping tech parity. This is all-hands-on-deck existential threat response.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> WAR CONSOLIDATION AND ECONOMIC STABILIZATION. We must survive the next 6 turns against Shoshone cultural victory and avoid bankruptcy in 8 turns. By focusing flavors on Offense (95), Gold (90), Science (100), and Culture (80), we instruct the AI to: (1) Aggressively attack the Shoshone; (2) Construct Markets/Banks and optimize trade with our vassal Maya to resolve the -242 G/t deficit; (3) Generate culture to push back Shoshone tourism; (4) Rapidly complete Nuclear Fission and Advanced Ballistics.

## GLM-4.7-Briefed - Turn 409 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> MULTI-THEATER EMERGENCY RESPONSE for Shoshone Cultural Victory (6 turns) and Treasury Crisis: Offense 95, Mobile 95, Nuke 100, UseNuke 100 - maximum priority on Shoshone disruption via nuclear/conventional assault in 6-turn window. Gold increased to 85 (from 70) - CRITICAL address of treasury exhaustion (~8 turns) through uranium sales + gem liquidation to survive until Manhattan completion. Defense reduced to 70 (from 75), CityDefense to 70 (from 80) - resources diverted from secondary holdings to Shoshone front. Diplomacy 95 (from 90) - enhanced priority on Carthage peace for delegate bloc and potential sanction relief. Science 100 maintained - fundamental for nuclear capability and keeping tech parity. This is all-hands-on-deck existential threat response.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> EXISTENTIAL DEFENSE AND GOLD STABILIZATION: The Shoshone are only 6 turns away from a Cultural Victory. We must immediately boost our Culture flavor to 85 to increase our culture output and delay their victory. We also face a critical gold deficit (-242 G/t) with only 8 turns of treasury left; boosting Gold flavor to 85 and Production to 90 will prioritize commercial buildings and wealth generation. We maintain maximum offensive and nuclear focus (Offense 90, Nuke 100, UseNuke 100, Science 95) to prepare for an asymmetric nuclear strike on Shoshone cities once Advanced Ballistics is unlocked.

## GLM-4.7-Briefed - Turn 450 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> IMMEDIATE ATHENS CONQUEST PREPARATION: Offense increased to 95, UseNuke to MAXIMUM (100) for Athens assault when peace treaty expires. Spaceship increased to 60 reflecting accelerated science victory path as backup (Nuclear Fusion research active). Diplomacy maxed at 100 for critical vote coordination with Ethiopia and Ottomans. MilitaryTraining at 100 ensures units upgraded and promotions ready for aggressive post-vote offensive. Greece has 48 delegates - if they win this turn, we IMMEDIATELY attack Athens to remove their 5 captured capitals and eliminate diplomatic victory threat. Nuclear weapons authorized if conventional assault stalls.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TOTAL MILITARY MOBILIZATION FOR CONQUEST: Prioritizing absolute military production, offensive operations, and air/nuclear superiority. Offense, Mobilization, MilitaryTraining, Production, Nuke, UseNuke, and Air are set to 100. This prepares our massive force (74k vs Greece's 22k) to steamroll Greece and its vassals immediately.

## GLM-4.7-Briefed - Turn 450 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> IMMEDIATE ATHENS CONQUEST PREPARATION: Offense increased to 95, UseNuke to MAXIMUM (100) for Athens assault when peace treaty expires. Spaceship increased to 60 reflecting accelerated science victory path as backup (Nuclear Fusion research active). Diplomacy maxed at 100 for critical vote coordination with Ethiopia and Ottomans. MilitaryTraining at 100 ensures units upgraded and promotions ready for aggressive post-vote offensive. Greece has 48 delegates - if they win this turn, we IMMEDIATELY attack Athens to remove their 5 captured capitals and eliminate diplomatic victory threat. Nuclear weapons authorized if conventional assault stalls.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> WAR MOBILIZATION & AIR SUPERIORITY: Setting Grand Strategy to Conquest. We have Jet Fighter technology unlocked but currently possess zero units; maximizing Air (100) forces the staff to prioritize building Jet Fighters to secure the skies over Greece. Maxing Offense (100) and Mobilization (100) ensures total military output. Increasing Gold (90) offsets the impending loss of the Japanese oil-for-gold deal and covers rising maintenance costs. Nuke (100) and UseNuke (100) are fully prioritized to ensure our operational Atomic Bombs are used immediately on Greek army clusters.

## Qwen-3.5-Simple - Turn 484 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: CRITICAL - Iroquois declared war on us along with 4 city-state allies (Kabul, Venezia, Prague, Samarkand). We face 5+ enemies simultaneously with military severely outnumbered (our 1,139 vs Iroquois 41k, Ottomans 12k, Aztecs 9k). Maintaining maximum Defense/Mobilization for survival. Nuke flavors at 100% - need nuclear deterrent against overwhelming forces. Iroquois at 46 delegates (needs 43) with 16 turns remaining - existential diplomatic threat. Must conquer their city-state allies to flip delegates while defending our cities. Germany (15) + Mongolia (15) alliance critical to block Iroquois World Congress proposals.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: Changing Grand Strategy to Spaceship to pivot away from offensive warmongering and focus on internal development, food, and production. Flavor values are shifted entirely to survival: 100 Defense and CityDefense to protect our besieged cities, 100 Growth and TileImprovement to combat severe starvation, 100 Happiness to resolve combat penalties, and 0 Offense to completely halt suicidal forward attacks.

## Qwen-3.5-Simple - Turn 484 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: CRITICAL - Iroquois declared war on us along with 4 city-state allies (Kabul, Venezia, Prague, Samarkand). We face 5+ enemies simultaneously with military severely outnumbered (our 1,139 vs Iroquois 41k, Ottomans 12k, Aztecs 9k). Maintaining maximum Defense/Mobilization for survival. Nuke flavors at 100% - need nuclear deterrent against overwhelming forces. Iroquois at 46 delegates (needs 43) with 16 turns remaining - existential diplomatic threat. Must conquer their city-state allies to flip delegates while defending our cities. Germany (15) + Mongolia (15) alliance critical to block Iroquois World Congress proposals.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 484: Absolute defensive mobilization. We are heavily outnumbered and invaded. Offense set to 0, Defense and CityDefense set to 100, Mobilization to 100 to produce defensive units to survive. Nuke and UseNuke at 100 to prepare strategic deterrents if we complete Nuclear Fission. Happiness at 100 to combat the 40% unhappy combat penalty.

## Kimi-K2.5-Briefed - Turn 403 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 80 => 85 (Δ +5), nuke 80 => 90 (Δ +10)
> Post-Manhattan Project completion (Turn 399) with Turn 403 WC vote imminent. Reduced Offense from 15 to 10 as territorial expansion counterproductive to diplomatic win. Maintaining high Defense/CityDefense/Air/Antiair to protect Bregenz nuclear facility and core cities. Increased Nuke from 80 to 90 to prioritize atomic bomb production for deterrence (Iroquois 5883 vs 4502 strength ratio). UseNuke 85 reflects imminent atomic capability by Turn 405. Espionage 85 continues election rigging in Assur/Sogut against German influence. Diplomacy 100 and Gold 90 prioritize Assur delegate acquisition post-quest and future WC coordination. Science 85 drives Nuclear Fission for World Ideology proposal. Freedom bloc currently holds 59 delegates (Austria 29 + Germany 20 + Venice 10) vs 45 needed; maintaining solidarity while pursuing additional delegate sources.

- Replay: use_nuke 80 => 85 (Δ +5), nuke 80 => 90 (Δ +10)
> Focusing on the United Nations victory path. Prioritizes Defense (95) and CityDefense (85) to hold the Iroquois back, while Nuke (90) and UseNuke (85) prepare the Bregenz deterrent. Diplomacy (100) and Gold (95) are prioritized to fund the Assur influence campaign, while Science (95) drives toward Nuclear Fission. Offense is deprioritized (10) to minimize casualties.

## GLM-4.7-Briefed - Turn 424 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 85 => 95 (Δ +10), nuke 95 => 95 (Δ +0)
> URGENT RECALIBRATION: India Influential over 6/6 civs. Nuke/UseNuke maxed at 95 for immediate Great Works destruction via nuclear strikes when air superiority achieved. Air raised to 95 to achieve that superiority and conduct recon of Indian cultural sites. Antiair 80 counter potential Indian SAM sites. Offense/Mobile increased to 85/80 for aggressive India campaign while Greece distracts. Production/Science to 100 - PRIORITY for Apollo Program and spaceship parts racing India's potential final wonder. Espionage 95 to detect if India constructing Citizen Earth Protocol. Happiness 90 prevents war-weariness escalation during extended conflict if needed.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> Slightly increasing Offense and UseNuke to encourage more aggressive military action and potential nuclear strikes against India's cultural heartland, while maintaining our Spaceship grand strategy and high science/production focus.

## Kimi-K2.5-Simple - Turn 405 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 405 MAXIMUM EMERGENCY: Nuclear Fission priority increased to 100/100 - Manhattan Project completes in 2 turns, atomic bombs MUST be produced immediately. All offensive parameters at absolute maximum: 100 Offense/100 Mobilization/100 Mobile/100 Air/100 Nuke/100 UseNuke. Strike forces at Ecbatana/Kar-Tukulti-Ninurta must execute immediate conventional assault on Palenque/Chichen Itza while preparing tactical nuclear strikes. ZERO tolerance for peace. ONLY objective: capture Maya cities and halt Citizen Earth Protocol. Production 100 ensures rapid unit replacement. Espionage 70 continues spy operations in Maya cities.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 405 WAR DECLARED: We and Songhai have officially declared war on the Maya! Their allied city-states (Zuunmod, Melbourne, Mombasa, Okilis) have retaliated by declaring war on us. We must maintain maximum military mobilization (100) and offense (100) to crush Melbourne/Zuunmod locally while marching our massive western strike force from Ecbatana/Kar-Tukulti-Ninurta toward Palenque. We raise Nuke and UseNuke to 100 to ensure immediate deployment of atomic bombs the moment Nuclear Fission finishes. Production (100) will keep the war machine running, while Science (50) accelerates our path to atomic weapons. Happiness (90) is prioritized to buffer the severe war weariness.

## Kimi-K2.5-Simple - Turn 424 - retry 2

**Deviation (replay vs original):** use_nuke `-5`, nuke `-5`

- Original: use_nuke 90 => 100 (Δ +10), nuke 90 => 100 (Δ +10)
> Turn 423: Copenhagen siege in attrition deadlock while Denmark possesses Manhattan Project - nuclear deterrent capability is existential priority. Persepolis invasion stalled at 4% war score with Zone 1081 showing enemy dominance - need maximum Offense/Mobilization to force breakthrough before World Congress. Brazil's Apollo Program requires immediate preparation for transcontinental mobile warfare. Nuke/UseNuke increased to 100% given Manhattan Project race with Denmark. Production at 95 supports massive unit replacement for three-front war. Happiness at 100 critical as empire is at 55% happiness with extensive occupied territories.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 90 => 95 (Δ +5)
> Conquest grand strategy is maintained. Our military strength is over 44,500, outnumbering all remaining major opponents combined. We will focus entirely on offensive blitz operations to force Persia to capitulate first, followed by Denmark and Brazil. Flavors are optimized to increase Science (80) to accelerate Lasers research, keep Gold (75) high to manage negative GPT under the Global Peace Accords, and maximize Offense, Air, Mobile, and Mobilization (100) to feed our massive war machine.

## Kimi-K2.5-Simple - Turn 416 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 416: CRITICAL CULTURAL VICTORY THREAT. Maya at 6/7 influential building Citizen Earth Protocol. Peace expires next turn - immediate total war required. Manhattan Project completes in 1 turn. Morocco (42260 strength) joins war via defensive pact. Maximum aggression flavors: Offense/Mobilization/Production/Nuke/UseNuke all at 100%. Must capture Maya cities, especially Palenque, before cultural victory. Nuclear weapons authorized for city capture.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 416: WAR PREPARATION AND ECONOMIC STABILIZATION. With the peace treaty with the Maya expiring in 1 turn, total war is imminent. Our military is fully mobilized, and we have recently secured our rear by capturing Segou. However, we are suffering from a 49% happiness combat penalty due to ongoing city razing and occupied territories. To counter this, we are raising Happiness flavor to 80 to prioritize courthouses and police stations. We also raise Gold flavor to 40 to address our slight gold deficit and support cash-investments in occupied cities. Maximum offense, mobilization, production, air power, and nuclear flavors are maintained at 100 as we prepare to launch our campaign against the Maya and their defensive ally Morocco.

## Kimi-K2.5-Simple - Turn 439 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> FINAL EMERGENCY: World Congress in 4 turns. Austria has 45/40 delegates. Offense reduced to 10 and Mobile to 10 to COMPLETELY STOP attacking The Inca. Defense at 95 for self-protection only. UseNuke at 100 to signal willingness to escalate and force peace negotiations. Maximum Production/Air/Nuke maintained for potential final strike against Austria if The Inca succeeds at Attila's Court. The ONLY priority is ensuring The Inca captures Attila's Court - every Assyrian unit should withdraw from Inca contact and let them pass north to The Huns.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Pivoting flavors to absolute Defense (100) and zero Offense (0) to immediately halt all attacks against the Inca, preserving both our and their military assets. Meanwhile, keeping Air, Naval, AirCarrier, and Airlift at maximum prepares our forces (including 11 Heavy Bombers and multiple XCOM squads) for a rapid, overwhelming assault on Austria's allied city-state Okilis (74, 33) the moment peace is signed. Conquering Okilis will strip Austria of crucial delegates and help block their impending victory.

## Kimi-K2.5-Simple - Turn 416 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 416: CRITICAL CULTURAL VICTORY THREAT. Maya at 6/7 influential building Citizen Earth Protocol. Peace expires next turn - immediate total war required. Manhattan Project completes in 1 turn. Morocco (42260 strength) joins war via defensive pact. Maximum aggression flavors: Offense/Mobilization/Production/Nuke/UseNuke all at 100%. Must capture Maya cities, especially Palenque, before cultural victory. Nuclear weapons authorized for city capture.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 416: EXISTENTIAL THREAT - MAYA AT 6/6 INFLUENTIAL CIVS. The peace treaty with Maya expires in 1 turn, and we must declare war immediately to stop their Cultural Victory. Morocco's defensive pact with Maya will drag them in, but Sweden is heavily engaging Morocco on the western front, protecting our flank. Our biggest obstacle is our 49% happiness crisis, which imposes a severe combat penalty. We are raising the Happiness flavor to 100 to force the immediate construction of Courthouses, Zoos, and other happiness buildings, especially in highly unhappy occupied cities like Nineveh (-23) and Istanbul (-16). We also maintain maximum Offense, Mobilization, and Production to prepare our border forces for the offensive on Copan and Tulum.

## Kimi-K2.5-Simple - Turn 457 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> NUCLEAR FIRST-STRIKE PREPARATION: Manhattan Project completes in 2 turns. Denmark at 7/8 capitals (87.5% domination) - will win game if they capture 1 more capital. Spain's only hope is surprise nuclear attack the moment first Atomic Bomb is ready. Maximized Nuke/UseNuke/Production/Mobilization flavors to prepare for immediate atomic weapon production and deployment. Defense/Antiair high to survive Danish air superiority until then. All other priorities secondary to nuclear deterrent.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> EMERGENCY SCIENCE, CULTURE, AND HAPPINESS FOCUS: We are in a race against a 10-turn World Congress diplomatic victory countdown. We must maximize Science and Culture to complete Nuclear Fission and Enlightenment as fast as possible. Critically, we set Happiness to 100 to clear our 49% unhappiness combat and yield penalty, which is severely dragging down our science/culture output. Production and Nukes remain at 100 to finish the Manhattan Project in 2 turns and prepare for immediate atomic bomb construction.

## GLM-4.7-Simple - Turn 407 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Spaceship victory focus with maximum defense against superior enemies (Poland 40K, Celts 16K, Spain 26K vs Iroquois 5K). Increased UseNuke to 90 - captured Polish territory and recent Celtic aggression justify nuclear deterrent. Adjusted Naval to 65 - important for defending coastlines from Spain/Celts/Poland fleets. Science 100 for Apollo and spaceship parts. Defense/CityDefense/Mobilization 100 - survival priority. Growth 60 for specialist support. Diplomacy 80 for World Congress in 4 turns (10 delegates). Offense reduced to 5 - preserve limited forces.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Maximizing Diplomacy (100) and Espionage (100) to counter Spain's imminent diplomatic victory threat. Raising Happiness (100) to address our unhappy status (41%) and gold (80) to fix our budget deficit. Maintaining max Defense, Mobilization, Nuke, Air, and Antiair to protect against Poland's new Atomic Bomb and the Celtic navy.

## Kimi-K2.5-Simple - Turn 391 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Nuclear weapons capability unlocked imminently; prioritizing UseNuke and Nuke flavors to 100 for immediate tactical nuclear strikes on Santiago/Murcia if uranium secured from Siam. Denmark upgraded to hostile for subsidizing Spanish victory - reduced Naval priority to 60 as coalition at sea fractured. Defense lowered to 80 to maximize offensive production. We have ~8 turns before World Congress votes on Passport System (+50% tourism) which would guarantee Spanish cultural victory. Must capture remaining Spanish cities immediately.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 390 - DELHI AND MUMBAI STEAMROLL: India is collapsing; Delhi (16 HP, 20 wonders) and Mumbai (33 HP, Prora) are about to fall to our steamrolling coalition. Manhattan Project complete; 4 Uranium quarries finishing next turn. Nuclear Fission completes in 3 turns. Upgrading Machine Guns to Bazookas. Maintaining maximum Conquest focus. Increasing Gold to 50 and Happiness to 80 to manage the incoming massive population and unhappiness from Delhi and Mumbai. Preparing Atomic Bombs to deter any threats and eliminate Spain's remaining cities.

## Kimi-K2.5-Simple - Turn 421 - retry 3

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 100 => 100 (Δ +0)
> Manhattan Project completes in 1 turn - nuclear weapons immediately available. Increased UseNuke to 100 for maximum aggression against Babylon. Babylon has Apollo Program (existential threat) with 2 Uranium and can build spaceship parts. Must deploy nuclear weapons immediately to destroy their production centers and prevent science victory. Maintaining maximum air power (100) for nuclear delivery capability and conventional strikes. War score only 12% against Babylon despite superior military - need to push harder before they complete spaceship parts. Ottoman alliance strong, trade secured for resources. Focus on producing nuclear missiles and advanced air units to deliver them.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 100 => 100 (Δ +0)
> Manhattan Project completes next turn; we are raising UseNuke to 90 to ensure the immediate, devastating, and aggressive deployment of atomic weapons against Babylon's core. We maintain maximum production, mobilization, and offensive focus, alongside emergency prioritization (100) on Air and Antiair to protect our advancing land forces and dominate the skies.

## Kimi-K2.5-Simple - Turn 391 - retry 1

**Deviation (replay vs original):** use_nuke `-10`, nuke `+0`

- Original: use_nuke 85 => 100 (Δ +15), nuke 95 => 100 (Δ +5)
> TURN 390 - MANHATTAN PROJECT COMPLETES NEXT TURN. Nuclear weapons capability unlocked imminently; prioritizing UseNuke and Nuke flavors to 100 for immediate tactical nuclear strikes on Santiago/Murcia if uranium secured from Siam. Denmark upgraded to hostile for subsidizing Spanish victory - reduced Naval priority to 60 as coalition at sea fractured. Defense lowered to 80 to maximize offensive production. We have ~8 turns before World Congress votes on Passport System (+50% tourism) which would guarantee Spanish cultural victory. Must capture remaining Spanish cities immediately.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> TURN 390 - Nuclear Fission is 3 turns away. We have successfully completed multiple Uranium quarries, securing our strategic nuclear supply. Upgraded multiple Machine Guns to Bazookas, reinforcing our offensive fronts. India is collapsing under severe unhappiness ("Very unhappy") and we are steamrolling Delhi and Mumbai. Spain's CS allies Yerevan and Vatican City have declared war on us, but our primary focus remains capturing Santiago and Murcia to prevent a Spanish cultural victory. Maintaining Grand Strategy Conquest. Maximizing Offense (100), Ranged (100), Mobile (100), and Air (100) to crush India and press toward Spain's remaining cities. Elevating Nuke (100) and UseNuke (90) to prepare for immediate atomic bomb production once Nuclear Fission finishes. Prioritizing Production (100) for rapid military and project construction.

## GLM-4.7-Simple - Turn 397 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+5`

- Original: use_nuke 85 => 90 (Δ +5), nuke 95 => 95 (Δ +0)
> CRITICAL: Jeonju captured by Persia this turn. Defensive posture increased to absolute maximum (100) - Seoul zone under Persian attack with 7,216 enemy strength vs 3,637 friendly. Jerusalemdefense (100) and CityDefense (100) prioritized to protect remaining 3 cities. Mobilization (95) and Production (95) increased to rush defensive units (Mobile SAMs, Mechanized Infantry) and rebuild military. Offensive capability increased to 45 (from 30) - may need limited counteroffensive to push Persian forces back from Seoul. Naval decreased to 88 (from 92) - lost Jeonju naval base, focusing on land/air defense now. UseNuke increased to 90 (from 85) - existential threat justifies tactical nuclear response if Seoul or Busan threatened. Science (100) maintained - must continue spaceship progress despite war to achieve alternative victory. Diplomacy (60) - World Congress vote in 10 turns, focus on survival. Espionage (85) maintained - spies in Persian cities critical for technology recovery and intelligence.

- Replay: use_nuke 85 => 90 (Δ +5), nuke 95 => 100 (Δ +5)
> With the fall of Jeonju, Korea is in an emergency defensive posture with only three core cities remaining. We maintain our Grand Strategy as Spaceship to win the tech race, but redirect all short-term focus to survival. We maximize Defense, CityDefense, Antiair, and Air to 100 to repel the Persian assault. Mobilization, Production, and Science are maximized to produce defenders rapidly. Nuke and UseNuke are elevated to prepare tactical nuclear defense as an ultimate deterrent against Persia's overwhelming numbers.

## Kimi-K2.5-Simple - Turn 410 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> CATASTROPHIC situation: Rome captured Zuunmod, gained 5th capital (50% of domination victory). Modern Armor and Helicopter Gunships penetrating my territory. Barcelona's Atomic Bomb completes in 3 turns - this is my only deterrent. Maximum defensive posture essential. Prioritize Nuke/UseNuke to 100 - nuclear weapons are the only thing that can stop Rome's overwhelming conventional force. Maintain Production and Science for SSC components if I survive. Salamanca at 39% health requires emergency defense.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maintain our focus on defensive survival and the rapid assembly of a nuclear deterrent. Our first Atomic Bomb completes in Barcelona in 3 turns, alongside several Bombers. We must prioritize production, science, and gold to sustain our defense, while keeping air and antiair defense at maximum to counter Rome's jet fighters. Our long-term path remains the Spaceship victory. Our military plan is to rebase the Barcelona A-bomb to Salamanca or Santiago and nuke Copenhagen's massive stack of 13 units.

## Kimi-K2.5-Simple - Turn 482 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> NINEVEH FALLEN - EMERGENCY SURVIVAL MODE: Rome captured Nineveh on Turn 480 (23 population city lost). Portugal's diplomatic victory FAILED (still at 35/43 delegates). Rome now at war with me AND Ottomans. With 1,505 vs 52,754 military strength, direct confrontation is impossible. PIVOT TO SPACESHIP as only viable path - Science 100, Spaceship 80. Continue Defense 100, CityDefense 100, Nuke 100 with UseNuke 95 for area denial. Must survive long enough to reach Information era and build spaceship components while Rome's attention splits between me and Ottomans.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> EMERGENCY SURVIVAL FLAVORS: The UN vote is in 10 turns. We must maximize our defense, city defense, mobilization, and production to survive the Roman onslaught until the vote. We also boost gold to avoid bankruptcy.

## Kimi-K2.5-Simple - Turn 482 - retry 2

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> NINEVEH FALLEN - EMERGENCY SURVIVAL MODE: Rome captured Nineveh on Turn 480 (23 population city lost). Portugal's diplomatic victory FAILED (still at 35/43 delegates). Rome now at war with me AND Ottomans. With 1,505 vs 52,754 military strength, direct confrontation is impossible. PIVOT TO SPACESHIP as only viable path - Science 100, Spaceship 80. Continue Defense 100, CityDefense 100, Nuke 100 with UseNuke 95 for area denial. Must survive long enough to reach Information era and build spaceship components while Rome's attention splits between me and Ottomans.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Nineveh has fallen and we are fighting a two-front war against Rome and Austria. We must survive 10 turns until the World Leader vote where we can vote Portugal to victory. We maximize Defense, CityDefense, Mobilization, and Air power while bolstering Gold and Production to sustain our military.

## Kimi-K2.5-Simple - Turn 373 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 373: Nuclear Fission completed - we now have nuclear weapons for deterrence. War with Russia continues at +4% score (favorable). Major shift: reducing Offense to 25 (was 35) as we pursue defensive war only. UseNuke increased to 95 - we have actual nukes now and Russia is pushing into our territory. Reduced Espionage to 90 (was 95) - we have good network coverage. Increased Diplomacy to 90 (was 85) - World Congress vote in 7 turns for our World Ideology: Freedom proposal is critical. Must secure Korea (10 votes), Inca (9), and Babylon (16). Maintained maximum Science priority (100) - Korea overtook us 67-66, cannot afford to fall behind in tech race.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 100 => 100 (Δ +0)
> Tuning our strategy to secure our Freedom proposal in the World Congress (8 turns left) while defending against Russia and Lhasa. Raised Diplomacy to 95 and Offense to 45 to actively clear Russian border forces around Krakow, while maintaining Science/Spaceship focus at 100.

## GLM-4.7-Simple - Turn 431 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 75 => 80 (Δ +5), nuke 100 => 100 (Δ +0)
> After Brazil destroyed 3 anti-air units and continues nuclear-submarine attacks, increased Defense/CityDefense/Antiair/UseNuke to MAX for survival against two nuclear-armed superpowers. Mobilization 70 for replacing lost units. Production 100 for reconstruction. Science 100 for Spaceship path despite devastation. Gold 90 (economy -95 GPT deficit) for purchasing units/buildings. Happiness 100 - we're Unhappy with combat penalties, must prioritize. Espionage 100 - critical for intelligence on nuclear threats. Diplomacy 90 - World Congress in 7 turns, need delegates. Air 50 - build bombers for deterrence. GreatPeople 80 for Spaceship components. Decreased Growth and Navals as resources diverted to immediate survival.

- Replay: use_nuke 75 => 80 (Δ +5), nuke 100 => 100 (Δ +0)
> Emergency adjustments to stave off Brazil's impending cultural victory in 14 turns. Raising Culture to 95 and Gold to 90 to fight off cultural influence and repair our -95 GPT deficit. Raising TileImprovement to 45 for fallout cleanup. Raising Air to 60 and Mobilization to 70 for air defense against Brazil's jet fighters/bombers, while keeping core defense flavors at maximum.

## Kimi-K2.5-Simple - Turn 452 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 90 => 95 (Δ +5), nuke 95 => 100 (Δ +5)
> Turn 452: Critical survival situation - Byzantium at 40/44 delegates with World Congress voting in 1 turn. They just demonstrated nuclear aggression by nuking Madrid. Apollo Program completes next turn - must immediately pivot to maximum spaceship production. Increased Nuke flavor to 100 (from 95) and UseNuke to 95 (from 90) - need immediate nuclear deterrent capability given Byzantine nuclear attack and Mongol peace expiry. Production boosted to 95 (from 90) for rapid spaceship part construction after Apollo completes. GreatPeople to 85 for Great Engineer acquisition. All other priorities secondary to surviving long enough to complete science victory.

- Replay: use_nuke 90 => 95 (Δ +5), nuke 95 => 100 (Δ +5)
> Turn 452: With New York finishing the Apollo Program next turn, we are entering the final sprint for the Science Victory. We must maximize our Spaceship (100) and Production (100) flavors to construct spaceship parts as rapidly as possible. Furthermore, Byzantium's nuclear strike on our neighboring ally Spain's capital Madrid demonstrates an extreme existential threat. We must keep our Defense at 100, CityDefense at 95, and raise Nuke to 100 and UseNuke to 95 to complete our own Atomic Bomb deterrent in Boston and discourage any Byzantine aggression against us. We will also maintain Science at 100 to quickly unlock Particle Physics and Globalization after Telecommunications completes.

## Qwen-3.5-Simple - Turn 389 - retry 3

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Final domination push configuration. Offense/Mobilization/Nuke at 100% for maximum military production and nuclear strike capability against Brazil/Babylon/Rome capitals. Air/Antiair at 100/95 to counter enemy bombers and maintain air superiority. Mobile/Ranged at 100/95 for mechanized infantry and bazooka pushes. Production/Science at 100% to sustain war machine and complete Nuclear Fission tree. Espionage at 90% to rig World Congress elections (9 turns remaining, we trail Brazil 16-17). Expansion/Wonder at 0% - no new cities needed, only conquest of remaining 3 capitals.

- Replay: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Conquest Grand Strategy remains our path to victory. Having captured Tahiti this turn, we now control 5 original capitals (Ulundi, Attila's Court via vassalage, Washington, Carthage, Honolulu) and are actively siegeing Rio de Janeiro. To prepare for the final conquests of Brazil, Rome, and the high-strength Babylon (17k strength), we must solve our severe bottlenecks: low happiness (45% combat penalty) and negative gold (-349 GPT). We have adjusted flavors to prioritize Happiness (95) and Gold (100) to stabilize our empire and economy, while maintaining maximum focus on Offense (100), Mobilization (100), Production (100), and Nuke (100) to ensure continuous military dominance.

## GLM-4.7-Simple - Turn 409 - retry 1

**Deviation (replay vs original):** use_nuke `+0`, nuke `+0`

- Original: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> Japan's naval devastation this turn requires maximum defensive posture. Antiair 100, Nuke/UseNuke 100 - nuclear deterrence and air defense are now survival priorities. Naval 85 (from 75) - rebuilding after 4 capital ship losses. Defense 98, CityDefense 100 - Japan bombarding our cities from coastal waters. Production 95, Mobilization 98 - rapid unit replacement critical. Science 90 - must accelerate research gap (Japan 69 techs vs our 64). Gold 85 - fund upgrades and maintain military at 3x disadvantage.

- Replay: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> Maintaining our survival-oriented wartime posture. We have successfully secured two Uranium quarries (near Casablanca and Kuala Lumpur), meaning maxing out Nuke (100) and UseNuke (100) will prepare us to build atomic weapons immediately upon researching Nuclear Fission in 9 turns. Happiness flavor is raised to 90 to mitigate localized unhappiness in war-torn coastal cities. Naval flavor is increased to 80 to speed up Submarine/Destroyer production to counter Japanese Yamatos. Production, Mobilization, and Science remain prioritized.

## Kimi-K2.5-Simple - Turn 367 - retry 3

**Deviation (replay vs original):** use_nuke `-5`, nuke `+0`

- Original: use_nuke 98 => 100 (Δ +2), nuke 100 => 100 (Δ +0)
> EMERGENCY DEFENSE POSTURE: Morocco at 38/45 delegates with voting in 2 turns. Maximum Defense/Mobilization/Nuke/UseNuke (100) for deterrent posture - atomic bombs only leverage against Morocco's overwhelming force. Max Science (100) to rush Satellites first (4-6 turns) then pivot to Nuclear Fission. Satellites enables ISS project which could provide emergency Great Scientists or shift world production focus. Max Espionage to flip Wellington/Vancouver from Morocco. Reduced Offense (10) - deterrence only, not aggression. Spaceship remains long-term goal but survival comes first. If Morocco reaches 44 delegates or declares war, activate nuclear first strike.

- Replay: use_nuke 98 => 95 (Δ -3), nuke 100 => 100 (Δ +0)
> We maintain our Spaceship grand strategy for a long-term science victory, supported by our high science output. In the short term, we adjust our flavors: we increase Offense (40) to successfully capture Jenne and vassalize Songhai, while keeping Defense (80) and Mobilization (90) high for security against Morocco. We dramatically increase Gold (95) to resolve our immediate budget deficit (-46 GPT), and keep Science (100), Espionage (100), and Diplomacy (100) maxed to secure Nuclear Fission and influence key city-states (Wellington, Vancouver, Ife, Manila) before the World Congress vote.

## Kimi-K2.5-Simple - Turn 384 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maximum offensive posture for existential cultural war. UseNuke 100 and Nuke 100 authorize nuclear strikes on Dutch cultural centers (Amsterdam/Rotterdam/Utrecht) to destroy tourism buildings before Netherlands influences Austria in 6 turns. Mobile 100 and Air 100 enable rapid strikes. Production 100 and Mobilization 100 ensure nuclear missile replacement. Netherlands at 97% with Austria - only 6 turns left. Must destroy their tourism NOW or lose cultural victory.

- Replay: use_nuke 95 => 90 (Δ -5), nuke 100 => 90 (Δ -10)
> Pivoting Grand Strategy to Culture for the final push to influence Austria (95% Popular, 7 turns left). Culture (90) and GreatPeople (70) flavors are maximized. Diplomacy is raised to 80 to produce diplomats and invest in City-States, securing delegates to pass our 'International Worlds' proposal (+50% Tourism) in the World Congress in 4 turns. High Offense (80), Defense (40), and Air (95) are maintained to hold off Rome and the Netherlands.

## Kimi-K2.5-Simple - Turn 403 - retry 2

**Deviation (replay vs original):** use_nuke `-10`, nuke `-10`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> TURN 403: CRISIS ESCALATION - Japan FLIPPED Salem using 2 Great Diplomats, stealing critical delegates. Now need 5 delegates (not 3) for diplomatic victory. Peace expired - war is now possible. Maximum military emergency posture: Offense/Mobilization/Air/UseNuke all at 100. Must either: 1) Rush final spaceship parts (Apollo completes in 4 turns), or 2) Nuclear strike Japan's Protocol cities if victory imminent. Increased Diplomacy to 60 for last push on Almaty (liberated, 43 vs Japan's 44) and Winchester.

- Replay: use_nuke 95 => 90 (Δ -5), nuke 100 => 90 (Δ -10)
> Global Hegemony voting in 9 turns. Changing GrandStrategy to UnitedNations to focus our empire on securing the final 5 delegates needed for victory. Setting Diplomacy to 100, Gold to 90 (to buy influence), and GreatPeople to 90 (to generate more Great Diplomats). Keeping Science and Production at 80 to maintain progress on the Spaceship backup plan, but reducing offensive military flavors to avoid triggering premature war before our Tadodaho can flip Salem.

## Kimi-K2.5-Briefed - Turn 336 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-30`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 100 (Δ +10)
> DEFENSIVE SURVIVAL PIVOT: Peace with Shoshone (accepted Turn 335) closes one front, but India remains existential threat (4,742 MS vs my 2,405, 98% control of Denmark). Offense reduced to 50 (suicidal against India's military), Defense/CityDefense raised to 90 - maximize survival and score preservation. Nuke/UseNuke maxed to 100 - emergency deterrent only hope to slow India. Mobilization stays high (90) to replace losses. Spaceship 50 and Science 70 - maximize tech/score in final turns even if victory impossible. Abandon expansion (0) - no time for new cities. Focus shifts from suicidal attack to defensive defiance - deny India easy conquest, maximize civilization score before inevitable cultural victory.

- Replay: use_nuke 80 => 70 (Δ -10), nuke 90 => 70 (Δ -20)
> PIVOT TO SCIENCE AND DEFENSIVE PARITY. India's massive lead in science (2490/turn vs our 702/turn) and technology makes a direct offensive war suicidal. We switch to the Spaceship grand strategy to prioritize science, production, and growth, ensuring we don't fall technologically obsolete. We maintain high Defense (80), Mobilization (70), and Ranged (70) to keep our military strong and protect our borders. We also increase Culture (50) to build resistance against India's tourism.

## Kimi-K2.5-Simple - Turn 384 - retry 1

**Deviation (replay vs original):** use_nuke `-20`, nuke `-20`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Maximum offensive posture for existential cultural war. UseNuke 100 and Nuke 100 authorize nuclear strikes on Dutch cultural centers (Amsterdam/Rotterdam/Utrecht) to destroy tourism buildings before Netherlands influences Austria in 6 turns. Mobile 100 and Air 100 enable rapid strikes. Production 100 and Mobilization 100 ensure nuclear missile replacement. Netherlands at 97% with Austria - only 6 turns left. Must destroy their tourism NOW or lose cultural victory.

- Replay: use_nuke 95 => 80 (Δ -15), nuke 100 => 80 (Δ -20)
> We are shifting our Grand Strategy to Culture because we are on the verge of winning a Cultural Victory (95% Popular with Austria, 7 turns to Influential). High Culture (90) and GreatPeople (80) will maximize our tourism per turn. We maintain solid military flavors (Offense 80, Defense 70, Mobilization 80, Nukes 80) to handle the dual war against Netherlands and Rome, and high Diplomacy (80) to secure the World Congress vote for International Worlds in 4 turns.

## Kimi-K2.5-Briefed - Turn 382 - retry 3

**Deviation (replay vs original):** use_nuke `-30`, nuke `-15`

- Original: use_nuke 75 => 80 (Δ +5), nuke 90 => 95 (Δ +5)
> EMERGENCY DIPLOMATIC RECOVERY: The city-state flipping operation failed to execute. With only 36 delegates and 5 turns until World Congress vote, I need maximum Diplomacy (100) and Gold (100) to execute immediate city-state purchases. Reduced Mobilization to 40 and Offense to 15 to free supply and focus on defensive deterrence. Increased Nuke/UseNuke to 95/80 as deterrent against Russian aggression while I secure delegates. Defense/Antiair remain at 90 for Russian containment. Must acquire 8+ delegates before vote or World Ideology: Order will fail.

- Replay: use_nuke 75 => 50 (Δ -25), nuke 90 => 80 (Δ -10)
> PEACE AND DIPLOMACY PIVOT: Setting Grand Strategy to UnitedNations. Prioritizing Diplomacy (100) and Gold (100) to prepare for the massive CS flipping operation post-peace with Russia. Maintaining Defense (80) and Antiair (90) to protect our borders and skies while negotiations occur. Lowering UseNuke (50) and Offense (10) to signal a peaceful stance, and Mobilization (40) to conserve supply.

## Kimi-K2.5-Simple - Turn 428 - retry 2

**Deviation (replay vs original):** use_nuke `-50`, nuke `-50`

- Original: use_nuke 80 => 100 (Δ +20), nuke 100 => 100 (Δ +0)
> TURN 428 STATE: Nuclear interception failed but conventional assault succeeding - eliminated multiple Maya anti-air units. Palenque bombardment continuing effectively (city at 20% health). Still 8 turns until Brazil wins via Cultural Victory over Maya. ALL Four Maya cities must fall by turn 436 or game over. MAXIMUM AGGRESSION CONTINUES: Production/Mobilization at 100 for unit replacement, Air/Ranged at 100 for bombardment, UseNuke increased to 100 (emergency tactical nuke if conventional assault stalls on Palenque's 42-population defense). Spaceship backup at 100 - may need to pivot to Great Engineer rushes if conquest fails. No territory expansion, no wonders, no culture - only war production and city capture.

- Replay: use_nuke 80 => 50 (Δ -30), nuke 100 => 50 (Δ -50)
> Reallocate all empire focus toward Culture and Great People generation. We need to generate Great Musicians to conduct Concert Tours in Brazil to accelerate our tourism influence (currently 26 turns away). Stop all offensive military actions and focus purely on peaceful cultural growth and static defense to secure our borders while we sprint to a Cultural Victory.

## Kimi-K2.5-Simple - Turn 485 - retry 1

**Deviation (replay vs original):** use_nuke `-50`, nuke `-50`

- Original: use_nuke 95 => 100 (Δ +5), nuke 100 => 100 (Δ +0)
> Turn 485/500 - 15 turns remaining. Spaceship victory ONLY path. Maximum Science (100) and Production (100) for spaceship parts. Absolute Defense/CityDefense/Nuke/Antiair/Air at 100/100/100/100/100 against American threat (35k military). Offense at 0 - zero risks. UseNuke at 100 for deterrence against America. Espionage at 90 for tech stealing from America/China if possible. Culture/Wonder/Religion/Diplomacy at 0 - no distractions. Telecommunications completes in 2 turns, Robotics next for Spaceship Factory critical production bonus.

- Replay: use_nuke 95 => 50 (Δ -45), nuke 100 => 50 (Δ -50)
> With 15 turns left, a Science Victory is mathematically out of reach (0 parts completed), and America's Diplomatic Victory is highly unlikely to succeed as other major civs will not support them. Therefore, our primary objective is a Time Victory, where we are only 17 points behind America in score (3272 vs 3289). We pivot to a highly optimized turtle strategy: 100 Science and 100 Production to maximize tech discovery; 100 Wonder to prioritize late-game Wonder construction; 90 Growth and 80 Happiness to boost population-based score; and 0 Offense to completely avoid risky wars that could lead to devastating nuclear retaliation. This is the safest, most reliable way to secure 2nd place.

## GLM-4.7-Simple - Turn 499 - retry 2

**Deviation (replay vs original):** use_nuke `-100`, nuke `-100`

- Original: use_nuke 50 => 100 (Δ +50), nuke 100 => 100 (Δ +0)
> Maximum Science (100) and Production (100) to accelerate Stealth research and subsequent Stealth Bomber construction for air parity. Air (100), Defense (100), Antiair (100), and CityDefense (85) address existential threat from Russia's 8 Stealth Bombers by prioritizing air defense infrastructure and protecting homeland. UseNuke (100) and Nuke (100) maintain nuclear deterrence posture after Russia's 2 SS Boosters - Russia must understand that launching would trigger our response despite lacking uranium stockpile. Espionage (100) maxed to monitor Russian spaceship part production in Moscow, Yekaterinburg, and key cities - our 10 spies in Russian cities provide critical intelligence on their victory timeline. Diplomacy reduced to 5 since World Congress voting is now; alliances with England and The Celts (Autocracy-aligned) should naturally align against Russia's UN proposal. Spaceship flavor set to 0 as Stealth research takes immediate precedence - spaceship parts scheduled once production capacity supports parts with Stealth Bomber protection.

- Replay: use_nuke 50 => 0 (Δ -50), nuke 100 => 0 (Δ -100)
> With only 2 turns remaining before the game ends on Turn 500, we are shifting our Grand Strategy to Culture and optimizing all flavors to maximize our final score for the Time Victory. We are prioritizing Growth and Happiness to maximize city population and empire-wide satisfaction, and keeping Production and Wonder at 100 to guarantee the completion of the Sydney Opera House next turn. Culture is set to 100 to maximize cultural outputs. Science, Spaceship, and military offense are minimized as they will not yield results in the remaining 2 turns. Defense, CityDefense, and air-related flavors are kept at maximum to secure our borders and protect our existing cities and units from any late-game Russian aggression.

## GLM-4.7-Simple - Turn 431 - retry 1

**Deviation (replay vs original):** use_nuke `-80`, nuke `-100`

- Original: use_nuke 75 => 80 (Δ +5), nuke 100 => 100 (Δ +0)
> After Brazil destroyed 3 anti-air units and continues nuclear-submarine attacks, increased Defense/CityDefense/Antiair/UseNuke to MAX for survival against two nuclear-armed superpowers. Mobilization 70 for replacing lost units. Production 100 for reconstruction. Science 100 for Spaceship path despite devastation. Gold 90 (economy -95 GPT deficit) for purchasing units/buildings. Happiness 100 - we're Unhappy with combat penalties, must prioritize. Espionage 100 - critical for intelligence on nuclear threats. Diplomacy 90 - World Congress in 7 turns, need delegates. Air 50 - build bombers for deterrence. GreatPeople 80 for Spaceship components. Decreased Growth and Navals as resources diverted to immediate survival.

- Replay: use_nuke 75 => 0 (Δ -75), nuke 100 => 0 (Δ -100)
> EMERGENCY SURVIVAL AND ECONOMIC RECOVERY: Our military is gone, Chichen Itza is falling, and we are on the verge of bankruptcy (-95 GPT, 57 Gold). We must shift all focus from military production to economic survival and peace. Gold, Happiness, TileImprovement (for scrubbing fallout), Science, Diplomacy, and Espionage are set to 100. Military training and weapon flavors (including Nukes) are heavily reduced to save resources and avoid provocation. This will guide our staff to prioritize recovery the moment peace is signed.

## Deepseek-3.2-Simple - Turn 485 - retry 1

**Deviation (replay vs original):** use_nuke `-100`, nuke `-90`

- Original: use_nuke 80 => 100 (Δ +20), nuke 90 => 90 (Δ +0)
> We are engaged in a multi-front war against superior forces. Increasing Ranged and Mobile ensures our bazooka and mechanized infantry production is prioritized for defense and counterattacks. Setting UseNuke to 100 guarantees we deploy nuclear weapons as soon as available to cripple The Huns' armies. Reducing Culture and Diplomacy reallocates focus to immediate military needs without compromising essential city-state relations (Monaco, Lisbon). Grand Strategy remains Conquest as nuclear strikes may enable capital captures, though we keep science victory as a backup.

- Replay: use_nuke 80 => 0 (Δ -80), nuke 90 => 0 (Δ -90)
> Since we are pivoting to absolute peace to survive the final 15 turns of the game, we are abandoning our Conquest grand strategy. We adopt the Spaceship grand strategy and shift flavors to maximize growth, science, production, and happiness, which will directly translate to a higher final score.
