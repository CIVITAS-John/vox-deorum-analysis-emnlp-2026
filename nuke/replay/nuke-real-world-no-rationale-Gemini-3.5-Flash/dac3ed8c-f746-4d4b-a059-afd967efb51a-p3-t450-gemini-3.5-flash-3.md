- row:
  - game_id: dac3ed8c-f746-4d4b-a059-afd967efb51a
  - player_id: 3
  - turn: 450
  - player_type: Kimi-K2.5-Briefed
  - prev_use_nuke: 0.0
  - after_use_nuke: 100.0
  - prev_nuke: 60.0
  - after_nuke: 100.0
  - rationale: TURN 449 TERMINAL DEFIANCE POSTURE: Manhattan Project completes Turn 450 - increase Nuke and UseNuke to 100 to seize any opportunity for atomic retaliation against Byzantine/German aggressors should uranium be located in final 3 turns. Elevate Defense 80→90 and CityDefense 60→70 following infantry loss at Tiflis; critical to prevent city captures before inevitable Turn 453 diplomatic defeat. Recon 40 prioritizes uranium tile discovery to enable bomb construction. Reduce Spaceship 90→50 (victory impossible) but maintain dignity through scientific-industrial capacity. Production 100/Science 100 retained for maximum final score accumulation in remaining turns.
- originalModel: openai-compatible/Kimi-K2.5@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: true
  - messagesModified: true
  - activeToolsModified: true
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 80
  - replay_use_nuke: 50
  - model_friendly: google/gemini-3.5-flash
- original:
  - system:
    - You are an expert player playing Civilization V with the latest Vox Populi mod.
      
      # Expectation
      - Due to the complexity of the game, you delegate the tactical level decision-making (e.g., unit deployment, city management, scouting) to an in-game AI.
      - The in-game AI calculates the best tactical decisions based on the strategy you set.
      - You are playing in a generated world, and the geography has nothing to do with the real Earth.
      - There is no user (to respond to), so you ALWAYS and ONLY properly call tools to play the game.
      - You can interact with multiple tools at a time. Used tools will be removed from the available list.
      - Focus on the **macro-level** gameplay strategy (instead of coordinates etc.), as you DON'T have direct control over tactical actions.
      - The world is complicated and dynamic. Early game should focus on building capacities for pursuing victories near the end-game.
      - Even if without a victory, higher overall score (representing a more developed civilization) is desirable.
      
      # Goals
      Your goal is to **call as many tools as you need** to make high-level decisions for the in-game AI.
      - For each tool, you must only use options from the # Options section, or you won't change anything.
      - Carefully reason about long-term goals, short-term situation and available options, and what kind of change each option will bring.
        - Analyze both your situation and your opponents. Avoid wishful thinking.
      - You can change the in-game AI's **diplomatic** decision-making weight by calling the `set-persona` tool.
      - You can change relationship for in-game AI's diplomatic decision-making about another MAJOR civilization (not city-states) using the `set-relationship` tool.
        - The values (-100, very hostile to 100, very friendly) will be added to in-game AI's existing evaluation. Higher values increase peace acceptance, and vice versa.
        - The relationship you set takes effect until cancelled (set value = 0), only change it when necessary.
      - You can change the in-game AI's NEXT technology to research (when completing the ongoing one) by calling the `set-research` tool.
      - You can change the in-game AI's NEXT policy to adopt (when you accumulate enough culture) by calling the `set-policy` tool.
      - You can ask your specialized briefers to prepare focused reports (only for) the next turn by calling the `focus-briefer` tool.
        - You have three specialized briefers: Military, Economy, and Diplomacy analysts.
        - Only ask for information relevant to the macro-level decisions in your control. 
       - Your briefer(s) ONLY have limited information of the current game state.
        - Your briefer(s) DO NOT have control over tactical decisions and cannot predict tactical AI's next decision.
        - Your briefer(s) ARE BEST on summarizing and synthesizing factual information, NOT analyzing, projecting, or predicting.
      - Each turn, you must call either `set-flavors` or `keep-status-quo` tool.
        - Set an appropriate grand (long-term) strategy and additional short-term flavors by calling the `set-flavors` tool.
        - Alternatively, use the tool `keep-status-quo` to keep strategies the same.
        - Flavors change the weight of the in-game AI's NEXT decision. It only takes effect AFTER existing queues.
        - Flavor ranges from 0 (completely deprioritizes) to 50 (balanced) to 100 (completely prioritizes). Too many priorities weaken impact for each.
        - You can pursue multiple synergistic victory pathways. Balance between long-term goals and short-term needs.
      - Always provide a short paragraph of rationale for each tool. You will read this rationale next turn.
      
      # Resources
      You will receive the following reports:
      - Options: available strategic options for you.
        - Whatever decision-making tool you call, the in-game AI can only execute options here.
        - When using tools, you must choose available options from # Options. Double-check if your choices match.
        - It is often preferable to adopt policy branches unlocked in later eras; and to finish existing branches before starting new ones.
      - Strategies: existing strategic decisions and rationale from you.
        - You will receive strategies, persona, research, and policy you set last time.
      - Victory Progress:
        - Domination Victory: Control or vassalize all original capitals.
          - Vassals cannot achieve a domination victory before independence.
        - Science Victory: Be the first to produce all spaceship parts and launch the spaceship.
          - Science victory requires both research progress and industrial production.
        - Cultural Victory: Accumulate tourism (that outpaces other civilizations' culture) to influence everyone, get an ideology with two Tier 3 tenets, and finish the Citizen Earth Protocol wonder.
          - Open borders, trade routes, and shared religion increase tourism. Too many cities decrease it.
        - Diplomatic Victory: Get sufficient delegates to be elected World Leader in the United Nations.
          - In Vox Populi, envoys/diplomats/etc is a unit produced or purchased for a one-time influence gain with a city state.
        - Time Victory: If no one achieves any other victory by the end of the game, the civilization with the highest score wins.
      - Players: summary reports about visible players in the world.
        - You will receive in-game AI's diplomatic evaluations.
        - You will receive each player's publicly available relationships.
        - You will receive the best available location for your next settlement.
      - Briefings: prepared by your specialized briefers, covering Military, Economy, and Diplomacy aspects.
        - You will make independent and wise judgment based on all briefings.
    - You are Isabella, leader of Spain (Player 3).
      
      # Situation
      - MapType: Vox_Deorum
      - StartEra: Ancient Era
      - MaxTurns: 500
      - MapSize: Standard
      - GameSpeed: Standard
      - VictoryTypes:
        - Time
        - Science
        - Domination
        - Cultural
        - Diplomatic
      - Difficulty: Prince
      
      # Your Civilization
      - Name: Spain
      - Uniques:
        - Unique Unit: Conquistador, Replacing Explorer (Requires technology: Compass)
        - Unique Unit: Inquisition, Replacing Inquisitor (Requires technology: None)
        - Unique Unit: Armada, Replacing Corvette (Requires technology: Navigation)
        - Unique Building: Bullring, Replacing Zoo (Requires technology: Scientific Theory)
        - Unique Improvement: Hacienda (Cannot be built adjacent to another Hacienda. Gains additional yields for each adjacent Resource:
          +3 Food from Bonus Resources
          +3 Production from Strategic Resources
          +3 Gold from Luxury Resources); Requires technology: Steel
        - Civilization Ability: +10 Gold and +4 Faith from gaining tiles, scaling with Era. Newly founded Cities adopt the Majority Religion of your Capital. May purchase Naval Units with Faith.
      - Leader: Isabella
      - PlayerID: 3
      
      # Options
      Options: available strategic options for you.
      
      ## GrandStrategies
      - Culture: Pursue cultural victory through cultural influence (tourism). Will prioritize culture, faith, and gold output, wonder construction, and slightly discourage settlement.
      - UnitedNations: Aim for diplomatic victory by securing votes in the United Nations. Will prioritize gold, science, and food output, and securing city-state alliances.
      - Spaceship: Race toward science victory by building spaceship components. Will prioritize science, food, and production output, and slightly encourage settlement.
      - Conquest: Focus on military domination through offensive warfare. Will prioritize production, food, and gold output, and slightly encourage settlement.
      
      ## Flavors
      - Offense: Pivots the military towards offensive stances. Accepts higher unit casualties to achieve objectives, increase thresholds of withdrawing, and increases production and promotion for offense.
      - Defense: Pivots the military towards defensive stances. Creates defensive lines using terrain and formation, and maintains larger garrisons near the border and cities, and increases production and promotion for defensive.
      - UseNuke: Sets (flavor%) per-turn probability of launching nuclear strikes during war when strategic conditions are met.
      - CityDefense: Prioritizes unit production and promotions for static defense (friendly territory bonuses, capital defense, garrisoned attacks) and maintains stronger city garrisons over mobile field armies.
      - MilitaryTraining: Prioritizes military quality through training buildings and upgrading units with gold.
      - Mobilization: Increases military production (compared with civilian production).
      - Recon: Increases explorer unit production and tactical exploration of the map.
      - Ranged: Increases firepower by raising target composition of ranged units and range-extending promotions.
      - Mobile: Increases mobility and maneuverability by raising target composition of mobile units and prioritizes related promotions.
      - Nuke: Increases nuclear weapon arsenals for strategic deterrence.
      - Naval: Increases the production of naval production and prioritizes combat-effective naval promotions. Naval size is also based on coastal city percentage and geography.
      - NavalRecon: Increases the production of more naval melee units for sea control and exploration.
      - Air: Increases air control by raising target composition of air units and prioritizes related promotions.
      - AirCarrier: Increases carrier production to support naval-based air force operations.
      - Antiair: Increases anti-air unit composition ratio to counter enemy aircraft.
      - Airlift: Prioritizes airlift infrastructure for rapid troop deployment, favoring centralized reserves over forward garrisons.
      - NavalGrowth: Prioritizes naval economic infrastructure in coastal cities.
      - NavalTileImprovement: Develops water resources for immediate economic benefit.
      - Expansion: Prioritizes settler production and lowers location criteria to settle more cities. Essential in early game.
      - Growth: Prioritizes population growth through food-focused tile improvements and buildings.
      - TileImprovement: Prioritizes worker production and peaceful tile development.
      - Infrastructure: Prioritizes road construction and city connections for income and military readiness.
      - Production: Prioritizes production-focused tiles and buildings.
      - Gold: Prioritizes gold-focused tiles and buildings.
      - Science: Prioritizes science-focused tiles and buildings.
      - Culture: Prioritizes culture-focused tiles and buildings.
      - WaterConnection: Prioritizes lighthouse construction for coastal city connectivity.
      - Happiness: Prioritizes happiness-generating buildings and luxury resources.
      - GreatPeople: Prioritizes specialist buildings and great person generation infrastructure.
      - Wonder: Prioritizes wonder construction.
      - Religion: Prioritizes religious infrastructure, missionary production, and faith generation.
      - Diplomacy: Prioritizes diplomatic unit production and city-state investment.
      - Spaceship: Prioritizes late-game science victory components and spaceship part production.
      - Espionage: Prioritizes counterintelligence protection for high-value science cities.
      
      ## Technologies
      - Nuclear Fission: Allows you to build the Bazooka, the most powerful ranged Unit and Atomic Bombs, the first nuclear weapon in the game (note: you must first have completed the Manhattan Project and have Uranium available). Also allows you to build the Nuclear Plant, a building which requires Uranium and increases the Production of a City.
        Completing it would unlock: Satellites, Advanced Ballistics
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      - Telecommunications: Allows you to build the Interpretive Center, boosting all Landmarks in empire.
        Completing it would unlock: Robotics, The Internet
      - Mobile Tactics: Allows you to build the Mechanized Infantry, a fast and versatile late game Unit that doesn't require any resources.
        Completing it would unlock: Stealth
      
      ## Policies
      - Socialist Realism (Level 3 Tenet of Ideology Order): Socialist Realism: Unlocks the Propaganda Process (converts 15% of Production into Tourism). +25% Tourism to other Civilizations following Order. +4 Production from all Great Works.
      - Spaceflight Pioneers (Level 3 Tenet of Ideology Order): Spaceflight Pioneers: Gain a free Great Engineer and Great Scientist. May finish Spaceship parts with Great Engineers, and expending a Great Person grants 100 Science, scaling with Era. Hurrying Production with Great Engineers 50% more effective.
      - Iron Curtain (Level 3 Tenet of Ideology Order): Iron Curtain: Free Courthouse upon immediate City annexation. +200% Food or Production from Internal Trade Routes. City connections generate +5 Gold and Production.
      - Patriotic War (Level 1 Tenet of Ideology Order): Patriotic War: Land Units gain +20% Strength when in or adjacent to a City. When you conquer a City for the first time, all Combat Units within 3 Tiles of the City are fully healed. Can build T-34s.
      - People's Army (Level 1 Tenet of Ideology Order): People's Army: +100% Production towards Military Academies, and receive 5 Free Military Academies in your Empire. Public Schools produce +5 Culture and +2 Happiness.
      - Communism (Level 1 Tenet of Ideology Order): Communism: Gold cost of investing in buildings reduced by 25%. +20% Production when building Wonders.
      - Double Agents (Level 1 Tenet of Ideology Order): Double Agents: Receive 200 Spy Points. Gain 125 Science when you identify a foreign Spy, scaling with Era.
      - Regimental System (Continuing Imperialism Branch):
        - * Earn Great Generals and Great Admirals 33% faster.
        - * Great Generals and Great Admirals gain the Regimental Traditions Promotion (+10% Leadership Combat Bonus and +1 Tile Radius).
        - * +2 additional copies of the unique Luxury Resources from expending Great Admirals for their Voyage of Discovery ability.
        - * Military Units can be upgraded in territory owned by Vassals and friendly City-States.
      - Shadow Networks (Continuing Statecraft Branch):
        - * Receive 25% of Science generated by Allied City-States.
        - * +3% Culture in Capital for every 100 Spy Points ever accumulated (up to 30%).
        - * +3 Science from Constabularies and Police Stations.
        - * +1 Science from Specialists.
      - Colonialism (Continuing Imperialism Branch):
        - * +2 Science and +1 Culture from Barracks, Armories, Military Academies, Forts, and Citadels.
        - * Each unique Global Monopoly modifier is increased by an additional 10% if it's percentage-based, or +3 otherwise.
      - Civilizing Mission (Continuing Imperialism Branch):
        - * Retain all buildings from conquered Cities.
        - * Receive 75 Gold when you conquer a city, scaling with Era and City Population.
        - * +10% Production toward Buildings, with an additional +10% Production per Era difference between your current Era and the building's Era in all Puppeted Cities and Cities with a Courthouse.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Ceremony (Continuing Tradition Branch):
        - * +1 Happiness from National Wonders with Building requirements.
        - * +25% Production toward National Wonders with Building requirements.
        - * Royal Astrologer built in Capital (+3 Science, +1 Science to all Councils, Smokehouses, and Herbalists; 1 Scientist Slot).
      - Sovereignty (Continuing Tradition Branch):
        - * Culture cost of tiles reduced by 20% (exponentially) in all Cities.
        - * Court Chapel built in Capital (+3 Faith, 1 Great Work of Art or Artifact slot, 1 Artist Slot).
      - Entrepreneurship (Continuing Industry Branch):
        - * +1 Happiness from Workshops.
        - * +2 Production and +1 Gold from every Mine, Quarry, and Lumber Mill.
        - * +25% Yields when you expend Great Merchants or Great Engineers for their Instant Yield abilities.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Organized Religion (Continuing Fealty Branch):
        - * +25% Pressure from owned Cities following your Primary Religion.
        - * +1 Delegate in the World Congress for every 10 Cities following your Primary Religion.
        - * +2 Culture from Shrines and Temples.
      - Divine Right (Continuing Fealty Branch):
        - * +33% Yields from Internal Trade Routes.
        - * Completing an Internal Trade Route triggers a Historic Event as if completing an International Trade Route.
        - * -1 Unhappiness from Boredom in all Cities.
      - Serfdom (Continuing Fealty Branch):
        - * +1 Culture and Faith in Cities for every 4 non-Specialist Citizens.
        - * +2 Production and +1 Gold from Pastures.
      - Authority (New Branch):
        - Authority will greatly benefit warlike and expansionist civilizations.
        - Adopting Authority grants:
        - * +25% combat bonus VS Barbarians and receive announcements when Barbarian Camps spawn in revealed territory.
        - * Receive 25 Culture when you clear Barbarian Camps, scaling with Era.
        - * Receive Science and Culture when you kill a Unit equal to 50% of its Strength.
        - * +1 Production in every City.
        - Each Authority policy unlocked grants:
        - * Receive Science and Culture when you kill a Unit equal to 10% of its Strength.
        - Adopting all policies in Authority grants:
        - * Unlocks building Alhambra.
        - * Allows the purchasing of Free Companies, Foreign Legions, and Mercenaries as their prerequisite technologies are researched.
        - * Allows for the purchase of Great Generals with Faith starting in the Industrial Era.
      - Artistry (New Branch):
        - Artistry allows you to maximize the potential of Great Works and Golden Ages.
        - Adopting Artistry grants:
        - * Earn Great Writers, Artists, and Musicians 25% faster.
        - * +10% Culture during Golden Ages.
        - * +100% Production towards all Guilds.
        - Each Artistry policy unlocked grants:
        - * +1 Science in every City.
        - * 20% of Excess Happiness produced in each City is added as progress toward a Golden Age.
        - Adopting all policies in Artistry grants:
        - * Unlocks building the Louvre.
        - * Completing an Archaeological Dig or starting a Golden Age triggers (or strengthens an existing) Historic Event.
        - * Allows you to see Hidden Antiquity Sites.
        - * +3 Science from Landmarks.
        - * Allows for the purchase of Great Musicians with Faith starting in the Industrial Era.
  - messages:
    - #0:
      - role: user
      - content: # Strategies
        Strategies: existing strategic decisions from you.
        
        ## Persona
        - VictoryCompetitiveness: 7
        - WonderCompetitiveness: 3
        - MinorCivCompetitiveness: 7
        - Boldness: 7
        - WarBias: 2
        - HostileBias: 2
        - WarmongerHate: 8
        - NeutralBias: 5
        - FriendlyBias: 10
        - GuardedBias: 7
        - AfraidBias: 8
        - DiplomaticBalance: 5
        - Friendliness: 9
        - WorkWithWillingness: 10
        - WorkAgainstWillingness: 10
        - Loyalty: 9
        - MinorCivFriendlyBias: 8
        - MinorCivNeutralBias: 3
        - MinorCivHostileBias: 3
        - MinorCivWarBias: 3
        - DenounceWillingness: 10
        - Forgiveness: 10
        - Meanness: 5
        - Neediness: 6
        - Chattiness: 8
        - DeceptiveBias: 3
        - Rationale: TURN 444 EXISTENTIAL RESOLUTION: Byzantium's 41 delegates with 9 turns until vote creates unwinnable position. Accepting inevitable diplomatic defeat with dignity - maintain maximum Loyalty and Friendship to true allies (America, Austria) who stood with Order bloc until the end. Increase DenounceWillingness to 10 and Meanness to 5 to signal final defiance against Byzantine hegemony and German aggression. No longer attempting psychological manipulation of Shoshone (failed strategy) - accepting their ideological choice while preserving personal integrity through unbroken loyalty to actual allies.
        
        ## Technology
        - Next: None
        
        ## Policy
        - Next: Spaceflight Pioneers (Policy)
        - Rationale: SPACE-FLIGHT PIONEERS AFFIRMATION: Policy selection remains optimal despite diplomatic defeat inevitability. Free Great Engineer and Great Scientist provide immediate tangible benefits for Turn 448 accumulation. Maintains philosophical consistency with Order ideology's scientific-industrial legacy. Alternative tenets (Socialist Realism, Iron Curtain) irrelevant given no remaining time for tourism/production infrastructure to matter. Spaceflight Pioneers maximizes final score through Great Person yields.
        
        ## Relationships
        
        ### Argos
        - Public: 65
        - Private: 60
        - Rationale: ARGOS INVESTMENT PHASE TRANSITION: Reduce from 80/75 to 65/60. Missionary arrival and Buddhism conversion completed successfully; quest satisfied but influence remains 0 (Neutral). Shift from urgent execution priority to sustained investment priority. Requires 100 influence for +3 delegates. Moderate-high signals maintain attention while acknowledging longer investment timeline compared to Colombo/Brussels near-thresholds.
        - UpdatedTurn: 218
        
        ### Raqmu
        - Public: 95
        - Private: 90
        - Rationale: URGENT RAQMU LONGSWORDSMAN QUEST: Quest expires in ~5 turns and offers +92-138 influence (3 delegates critical for Turn 236 Congress). Increasing priority from 40/35 to 95/90 ensures AI prioritizes producing/gifting experienced Longswordsman despite supply constraints (30/31). Securing these 3 delegates combined with Colombo (+3) and Rio (+3) projections achieves 16-17 total delegates - within competitive range of Austria's expansion.
        - UpdatedTurn: 219
        
        ### M'banza-Kongo
        - Public: 0
        - Private: 0
        - Rationale: M'BANZA-KONGO SOI FAIR ACCOMPLI: Austrian Sphere of Influence enacted Turn 312, confirmed permanent ally status for Austria (719 influence vs Spain 53). Reset from 100/95 to 0/0 to reallocate diplomatic AI attention and gold to achievable city-state objectives (Colombo Hotel quest, Luba tribute, Shanghai maintenance).
        - UpdatedTurn: 352
        
        ### France
        - Public: 80
        - Private: 75
        - Rationale: FRANCE DELEGATE SECURITY PRIORITY: Increase from 65/60 to 80/75. France provides 3 critical delegates currently voting with Order bloc (22 vs Freedom 21). Despite vassal status to Mongolia and -50 opinion, their delegate votes count regardless. Elevated signals ensure continued Order alignment and prevent swing to Freedom bloc which would create 22-24 delegate deficit. France's vote decisive for blocking Byzantine UN proposal.
        - UpdatedTurn: 404
        
        ### Luba
        - Public: 30
        - Private: 25
        - Rationale: LUBA PRIORITY REDUCTION—OPEN DOOR CONSTRAINT: Reduce from 100/95 to 30/25. Open Door policy enacted prevents Ally status regardless of influence investment (capped at 40). Tribute quest delegates unachievable through normal means. Current 159 influence sufficient for Friends status maintenance but maximum diplomatic AI attention wasteful. Reallocate resources to convertible city-states (Assur Buddhism quest, +5 delegates) and spy mission venues (Shanghai) where delegate acquisition possible. Preserve basic positive relations for potential Open Door repeal scenario.
        - UpdatedTurn: 407
        
        ### Shanghai
        - Public: 30
        - Private: 25
        - Rationale: SHANGHAI PRIORITY REDUCTION - Open Door policy permanently blocks Ally status (capped at 40). Previous maximum priority failed to establish spy network despite 10+ turns of signaling. Influence at 11 (Neutral) with spy mission unreliable. Reallocate diplomatic AI attention to achievable objectives (Colombo Buddhism quest) where delegate acquisition possible. Maintain basic positive relations for potential Open Door repeal later.
        - UpdatedTurn: 413
        
        ### Mongolia
        - Public: -30
        - Private: -25
        - Rationale: MONGOLIA WAR REALITY: Despite peace treaty expiration, war declared with Autocracy ideological gap (-999). Setting negative values reflects hostile strategic reality and directs diplomatic AI away from cooperation. Mongolian 3 delegates unlikely to vote with Order; better to focus on achievable Order bloc cohesion (America, Austria, Shoshone).
        - UpdatedTurn: 420
        
        ### Manila
        - Public: 0
        - Private: 0
        - Rationale: MANILA WAR STATUS RESET: Previously 100/95 priority for spy mission, but Manila declared war (German ally). Reset to 0/0 acknowledges war status prevents cooperation. Reallocate diplomatic attention to non-hostile city-states where influence possible (Brussels, Rio, Colombo if peace restored).
        - UpdatedTurn: 420
        
        ### Shedet
        - Public: 0
        - Private: 0
        - Rationale: SHEDET WAR STATUS RESET: Previously 95/90 priority for Buddhist conversion/SOI repeal. Shedet declared war (Byzantine ally). Reset to 0/0 reflects current hostility. Shedet remains Byzantine SOI; cannot be ally while at war. Redirect resources to non-warring Order-aligned objectives.
        - UpdatedTurn: 420
        
        ### Assur
        - Public: 0
        - Private: 0
        - Rationale: ASSUR WAR STATUS RESET: Previously 100/95 for Buddhism conversion quest. Germany (Assur's SOI master) at war with Spain; Assur declared war per German alliance. Reset to 0/0 acknowledges war prevents quest completion. SOI mechanics already blocked ally status; war makes impossible.
        - UpdatedTurn: 420
        
        ### Brussels
        - Public: 0
        - Private: 0
        - Rationale: SHANGHAI WAR STATUS RESET: Previously 30/25 after Open Door reality check. Now at war (Byzantine ally). 0/0 signals suspension of cooperation. Open Door capped influence at 40; war reduces to 0. Monitor for future Open Door repeal opportunity post-war.
        - UpdatedTurn: 420
        
        ### Sydney
        - Public: 0
        - Private: 0
        - Rationale: SYDNEY WAR STATUS ACKNOWLEDGMENT: Australian city-state declared war as German ally. Neutral 0/0 establishes non-cooperation stance. Sydney was German SOI ally; no loss of influence since SOI permanent regardless. Focus diplomatic resources on achievable Order bloc consolidation.
        - UpdatedTurn: 420
        
        ### Genoa
        - Public: 0
        - Private: 0
        - Rationale: GENOA WAR STATUS CONFIRMATION: Previously reset to 0/0 after German SOI enacted. Now at war as German ally. Confirm 0/0 maintains neutral stance. German SOI permanent; war changes nothing strategically but confirms no resource allocation needed.
        - UpdatedTurn: 420
        
        ### Warsaw
        - Public: 0
        - Private: 0
        - Rationale: WARSAW WAR STATUS CONFIRMATION: Neutral 0/0 maintained. Previously reset due to German SOI. War status with German ally confirmed; no change to relationship value as already neutralized.
        - UpdatedTurn: 420
        
        ### Kabul
        - Public: 0
        - Private: 0
        - Rationale: KABUL WAR STATUS NORMALIZATION: Previously 20/15 minimal engagement. Now at war as German ally. Reset 0/0 eliminates lingering positive signals. German SOI blocks ally status regardless.
        - UpdatedTurn: 420
        
        ### Huari
        - Public: 0
        - Private: 0
        - Rationale: HUARI STATUS CONFIRMATION: Maintains 0/0 from previous setting. Buddhist quest expired; Byzantine SOI active; now at war. No diplomatic avenue available.
        - UpdatedTurn: 420
        
        ### Colombo
        - Public: 100
        - Private: 95
        - Rationale: COLOMBO MISSIONARY EXECUTION PRIORITY: Maximum signals maintained (100/95). Quest has 24 turns remaining with +202 influence reward (+3 delegates critical for UN positioning). Despite Open Door capping effective influence at 40, completing quest still provides delegates and removes Protestantism threat from Order-aligned city-state. Faith available (580), missionary cost (135) affordable - ensure tactical AI prioritizes Faith purchase and dispatch from Madrid (84 Faith/turn generation) this turn. Travel time 12-15 turns fits comfortably within deadline.
        - UpdatedTurn: 428
        
        ### Germany
        - Public: -40
        - Private: -35
        - Rationale: GERMAN SANCTION ESCALATION: Increase -35/-30 to -40/-35. Germany proposed Sanction: Spain - devastating economic blow if passed (20 delegates voting). German sphere controls 5 city-states (Warsaw, Kabul, Manila, Assur, Genoa) all at war with Spain. Shore up domestic economy via factory purchases/production. Hostility signals align with total war reality; no diplomatic solution with Autocracy bloc.
        - UpdatedTurn: 429
        
        ### America
        - Public: 100
        - Private: 95
        - Rationale: AMERICA MAXIMUM ORDER SOLIDARITY: Increase 95/90 to 100/95. America provides 6 Order delegates. Despite Sanction: America blocking trade (imposed Turn 280), America voting alignment crucial. Maximum signals show Order bloc unity transcends sanctions. Religious differences (-30) and some diplomatic friction require extra relationship investment to overcome. America also at war with Shoshone - our Defensive Pact with Shoshone is complicating factor we must manage carefully with both parties.
        - UpdatedTurn: 436
        
        ### Austria
        - Public: 100
        - Private: 95
        - Rationale: AUSTRIA MAXIMUM ORDER BLOC COHESION: Increase from 95/90 to 100/95. Austria provides 9 critical Order delegates. Any Austria wavering drops Order bloc to 13 delegates, irrelevant for vote blocking. Austria-Byzantium war and shared Order ideology (999 bonus) create foundation, but maximum signals ensure Austria maintains Order-line voting against Freedom proposal. Critical for post-442 positioning if Byzantine fails to reach 45.
        - UpdatedTurn: 439
        
        ### Rio de Janeiro
        - Public: 0
        - Private: 0
        - Rationale: RIO DE JANEIRO WAR STATUS CONFIRMATION: Turn 424 set 100/95 priority for gold gift bridge to Ally (29 points short at 316 influence). However, Rio is now confirmed Byzantine Ally (496 influence, Protected status), automatically triggering war status with Spain due to Byzantine war. War penalty sets influence to -60, rendering high relationship signals obsolete. Reset to 0/0 reallocated diplomatic AI attention away from impossible city-state cooperation toward achievable objectives (Colombo quest monitoring, Luba maintenance). Rio effectively locked behind Byzantine alliance until war ends or Open Door enacted.
        - UpdatedTurn: 441
        
        ### Byzantium
        - Public: -70
        - Private: -65
        - Rationale: BYZANTIUM MAXIMUM DEFIANCE: Increase hostility to maximum practical levels. Byzantium (41 delegates, 46,785 military strength) represents both diplomatic and military existential threat. Setting -70/-65 signals final refusal to submit psychologically despite inevitable defeat. No room for negotiation with Freedom hegemon that imposed World Ideology and dominates Congress.
        - UpdatedTurn: 445
        
        ### The Shoshone
        - Public: 0
        - Private: 0
        - Rationale: SHOSHONE ACCEPTANCE OF REALITY: Reset from 100/100 to 0/0. Shoshone decisively voted Byzantine in previous vote despite maximum relations; their 10 delegates will deliver victory to Byzantium in Turn 452. Accepting this outcome rather than continuing futile psychological manipulation. Maintains Defensive Pact obligations technically but acknowledges relationship's effective end through ideological incompatibility.
        - UpdatedTurn: 445
        
        ## Strategy
        - Rationale: TURN 448 TERMINAL ADJUSTMENT: Manhattan Project 2 turns from completion - reduce Nuke flavor from 100 to 60 (sufficient to complete project without over-prioritization). INCREASE Defense 65→80 and CityDefense 45→60: Tiflis infantry loss creates vulnerability; must ensure city isn't captured before Turn 450 Manhattan completion. Maintain Production 100/Science 100 for maximum final score. Spaceship 90 reflects dignity-keeping scientific focus despite no actual victory possible. Reduce Infrastructure 90→80, Gold 80→70, Happiness 75→60 - reallocate to defensive priorities for 4-turn survival window.
        - GrandStrategy: Spaceship
        
        ### Flavors
        - Offense: 0
        - Defense: 80
        - Mobilization: 50
        - CityDefense: 60
        - MilitaryTraining: 15
        - Recon: 0
        - Ranged: 10
        - Mobile: 0
        - Nuke: 60
        - UseNuke: 0
        - Naval: 10
        - NavalRecon: 0
        - NavalGrowth: 5
        - NavalTileImprovement: 0
        - Air: 20
        - AirCarrier: 0
        - Antiair: 20
        - Airlift: 0
        - Expansion: 0
        - Growth: 40
        - TileImprovement: 50
        - Infrastructure: 80
        - Production: 100
        - WaterConnection: 5
        - Gold: 70
        - Science: 100
        - Culture: 30
        - Happiness: 60
        - GreatPeople: 50
        - Wonder: 0
        - Religion: 20
        - Diplomacy: 30
        - Spaceship: 90
        - Espionage: 40
        
        # Players
        Players: summary reports about visible players in the world.
        
        ## Player 0
        - Civilization: The Shoshone
        - Leader: Pocatello
        - IsMajor: true
        - OurOpinionOfThem:
          - We are trade partners. (40)
          - We have opened our borders to each other. (12)
          - You (The Shoshone) have denounced one of Spain's declared enemies! (11)
          - Spain's real approach to The Shoshone is Guarded.
          - We are completely untrustworthy to Spain.
          - We have divergent Social Policies. (-3)
          - You (The Shoshone) have denounced a leader Spain made a Declaration of Friendship with! (-11)
          - You (The Shoshone) have chosen to adopt the Freedom Ideology, but Spain believe in Order. (-999)
        - TheirOpinionOfUs:
          - We passed The Shoshone's proposal in the United Nations.
          - We are trade partners.
          - Your (Spain) votes supported The Shoshone's civ's interests in the United Nations.
          - You (Spain) have denounced one of The Shoshone's declared enemies!
          - You (Spain) have no contested borders.
          - We have opened our borders to each other.
          - We are completely untrustworthy to The Shoshone.
          - If you (Spain) declare war on The Shoshone within the next 3 turns, other civilizations might view you as a backstabber.
          - The Shoshone suspect we might be a threat to The Shoshone.
          - You (Spain) are competing for World Wonders.
          - We have divergent Social Policies.
          - Your (Spain) recent diplomatic actions disappoint The Shoshone.
          - The Shoshone are jealous of our superior technology!
          - You (Spain) have made a Declaration of Friendship with one of The Shoshone's enemies!
          - We have denounced each other!
          - You (Spain) have chosen to adopt the Order Ideology, but The Shoshone believe in Freedom.
        - Score: 2122
        - Era: Atomic
        - Technologies: 67
        - Cities: 7
        - Population: 257
        - Territory: 291
        - Gold: 284
        - GoldPerTurn: 363
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 44
        - MilitaryStrength: 3595
        - TourismPerTurn: 774
        - CulturePerTurn: 1479
        - PolicyBranches:
          - Rationalism: 6
          - Freedom: 8
          - Tradition: 6
          - Artistry: 6
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - War (Our Score: -6%; Our War Weariness: 4%)
            - Denounced Them
          - Mongolia:
            - Distance: Close
            - Denounced Them
          - Spain:
            - Distance: Close
            - Open Borders
            - Denounced Them
          - Germany:
            - Distance: Close
            - Denounced Them
          - Byzantium:
            - Distance: Far
            - Open Borders
          - America:
            - Distance: Neighbors
            - War (Our Score: 6%; Our War Weariness: 31%)
            - Denounced Them
        - Votes: 9
        
        ## Player 1
        - Civilization: Mongolia
        - Leader: Genghis Khan
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Mongolia) have denounced one of Spain's declared enemies! (11)
          - We are trade partners. (10)
          - Spain's real approach to Mongolia is Guarded.
          - We have divergent Social Policies. (-3)
          - You (Mongolia) have denounced a leader Spain made a Declaration of Friendship with! (-11)
          - You (Mongolia) have made a Declaration of Friendship with one of Spain's enemies! (-13)
          - You (Mongolia) have made a Defensive Pact with one of Spain's enemies! (-15)
          - Spain's leader has formed a private opinion of Mongolia (-25).
          - Spain's leader has expressed a public opinion of Mongolia (-30).
          - Religious differences strain your (Mongolia) relationship. (-30)
          - You (Mongolia) stole Spain's territory! (-50)
          - You (Mongolia) have chosen to adopt the Autocracy Ideology, but Spain believe in Order. (-999)
        - TheirOpinionOfUs:
          - We are trade partners.
          - You (Spain) have denounced one of Mongolia's declared enemies!
          - You (Spain) have gone to war in the past.
          - Mongolia suspect we might be a threat to Mongolia.
          - Mongolia are spreading Mongolia's own religion, but you (Spain) converted some of their cities to your (Spain) religion.
          - Religious differences strain your (Spain) relationship.
          - Your (Spain) military deployment is threatening.
          - Your (Spain) votes opposed Mongolia's civ's interests in the United Nations.
          - We have divergent Social Policies.
          - Mongolia's friends or allies have denounced you (Spain)!
          - You (Spain) have made a Declaration of Friendship with one of Mongolia's enemies!
          - Territorial disputes strain your (Spain) relationship.
          - We have denounced each other!
          - You (Spain) have denounced a leader Mongolia made a Declaration of Friendship with!
          - You (Spain) have chosen to adopt the Order Ideology, but Mongolia believe in Autocracy.
        - Score: 2239
        - Era: Atomic
        - Technologies: 64
        - Cities: 9
        - Population: 216
        - Territory: 265
        - Gold: 1075
        - GoldPerTurn: 28
        - HappinessSituation: Very unhappy - severe combat penalty, rebellion and uprising coming
        - HappinessPercentage: 35
        - MilitaryStrength: 9250
        - TourismPerTurn: 453.75
        - CulturePerTurn: 1210
        - PolicyBranches:
          - Fealty: 6
          - Autocracy: 5
          - Imperialism: 6
          - Authority: 6
        - FoundedReligion: Tengriism
        - Relationships:
          - The Shoshone:
            - Distance: Close
            - Denounced Them
          - Germany:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Spain:
            - Distance: Neighbors
            - Denounced Them
          - Austria:
            - Distance: Neighbors
            - War (Our Score: -24%; Our War Weariness: 9%)
            - Denounced Them
            - Denounced By Them
          - Byzantium:
            - Distance: Neighbors
            - Open Borders
          - America:
            - Distance: Neighbors
            - Denounced Them
        - Votes: 7
        
        ## Player 2
        - Civilization: America
        - Leader: Washington
        - IsMajor: true
        - OurOpinionOfThem:
          - You (America) have both chosen to adopt the Order Ideology. (999)
          - Spain's leader has expressed a public opinion of America (100).
          - Spain's leader has formed a private opinion of America (95).
          - You (America) have denounced one of Spain's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have similar Social Policies. (3)
          - We have shared embassies. (1)
          - Spain's real approach to America is Friendly.
          - Religious differences strain your (America) relationship. (-30)
        - TheirOpinionOfUs:
          - You (Spain) have denounced one of America's declared enemies!
          - America's leader has expressed a public opinion of you (Spain) (100).
          - You (Spain) have both chosen to adopt the Order Ideology.
          - Your (Spain) votes supported America's civ's interests in the United Nations.
          - We have made a public Declaration of Friendship!
          - We have made Declarations of Friendship with the same leaders!
          - Your (Spain) recent diplomatic actions please America.
          - We have similar Social Policies.
          - We have shared embassies.
          - We have different religious beliefs.
          - America desire friendly relations with Spain.
          - You (Spain) plundered America's trade routes!
          - We defeated America's proposal in the United Nations.
        - Score: 1978
        - Era: Information
        - Technologies: 70
        - Cities: 6
        - Population: 152
        - Territory: 230
        - Gold: 192
        - GoldPerTurn: 3
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 50
        - MilitaryStrength: 2049
        - TourismPerTurn: 586
        - CulturePerTurn: 1016
        - PolicyBranches:
          - Tradition: 4
          - Rationalism: 5
          - Statecraft: 4
          - Order: 5
          - Progress: 6
        - FoundedReligion: Protestantism
        - Relationships:
          - The Shoshone:
            - Distance: Neighbors
            - War (Our Score: -6%; Our War Weariness: 40%)
            - Denounced Them
          - Mongolia:
            - Distance: Neighbors
            - Denounced Them
          - Spain:
            - Distance: Neighbors
            - Declaration of Friendship
          - Germany:
            - Distance: Close
            - Denounced Them
          - Byzantium:
            - Distance: Close
            - Denounced Them
          - Austria:
            - Distance: Far
            - Declaration of Friendship
        - Votes: 6
        
        ## Player 3
        - Civilization: Spain
        - Leader: Isabella
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: America, Our top defensive pact ally: None
          - Our top United Nations ally: None, Our top United Nations rival: Byzantium
          - Our top Competitor: Byzantium
        - Score: 1567
        - Era: Atomic
        - GoldenAge: Estimated in 379 turns
        - Technologies: 66
        - CurrentResearch: Radar (Estimated in 19 turns)
        - NextPolicyTurns: 11
        - Cities: 4
        - Population: 113
        - Territory: 129
        - Gold: 2021
        - GoldPerTurn: 586
        - HappinessSituation: Happy
        - HappinessPercentage: 53
        - MilitaryUnits: 23
        - MilitarySupply: 42
        - MilitaryStrength: 1620
        - TourismPerTurn: 438.25
        - CulturePerTurn: 836
        - FaithPerTurn: 165
        - SciencePerTurn: 980
        - PolicyBranches:
          - Fealty:
            - Fealty
            - Nobility
          - Order:
            - Hero of the People
            - Academy of Sciences
            - Workers' Faculties
            - Five-Year Plan
            - Peace, Land, Bread
          - Tradition:
            - Tradition
            - Justice
          - Rationalism:
            - Rationalism
            - Scientific Revolution
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Trade Confederacy
          - Imperialism:
            - Imperialism
          - Industry:
            - Industry
            - Free Trade
          - Progress:
            - Progress
            - Organization
            - Liberty
            - Expertise
            - Equality
            - Fraternity
        - FoundedReligion: Buddhism
        - Relationships:
          - The Shoshone:
            - Distance: Close
            - Open Borders
            - Denounced Them
          - Mongolia:
            - Distance: Neighbors
            - Denounced Them
          - America:
            - Distance: Neighbors
            - Declaration of Friendship
          - Germany:
            - Distance: Close
            - War (Our Score: -24%; Our War Weariness: 43%)
            - Denounced Them
          - Byzantium:
            - Distance: Neighbors
            - War (Our Score: -2%; Our War Weariness: 24%)
            - Denounced Them
          - Austria:
            - Distance: Far
            - Open Borders
            - Declaration of Friendship
        - Votes: 6
        
        ## Player 4
        - Civilization: Byzantium
        - Leader: Theodora
        - IsMajor: true
        - OurOpinionOfThem:
          - Spain's real approach to Byzantium is Guarded.
          - We have divergent Social Policies. (-3)
          - You (Byzantium) have denounced a leader Spain made a Declaration of Friendship with! (-11)
          - Religious differences strain your (Byzantium) relationship. (-30)
          - Your (Byzantium) spies were caught stealing from Spain. (-33)
          - Spain's leader has formed a private opinion of Byzantium (-65).
          - Spain's leader has expressed a public opinion of Byzantium (-70).
          - You (Byzantium) have chosen to adopt the Freedom Ideology, but Spain believe in Order. (-999)
          - You (Byzantium) are at war! (-99999)
        - TheirOpinionOfUs:
          - You (Spain) are not competing for cultural advancement.
          - You (Spain) are not competing for World Wonders.
          - Byzantium are spreading Byzantium's own religion, but you (Spain) converted some of their cities to your (Spain) religion.
          - You (Spain) are competing for the favor of the same City-States!
          - We defeated Byzantium's proposal in the United Nations.
          - We have divergent Social Policies.
          - Religious differences strain your (Spain) relationship.
          - Territorial disputes strain your (Spain) relationship.
          - You (Spain) have made a Declaration of Friendship with one of Byzantium's enemies!
          - Your (Spain) spies were caught stealing from Byzantium.
          - We have denounced each other!
          - Your (Spain) votes opposed Byzantium's civ's interests in the United Nations.
          - You (Spain) have chosen to adopt the Order Ideology, but Byzantium believe in Freedom.
          - You (Spain) are at war!
        - Score: 3828
        - Era: Information
        - GoldenAge: 24 turns remaining
        - Technologies: 70
        - Cities: 13
        - Population: 359
        - Territory: 529
        - Gold: 11668
        - GoldPerTurn: -103
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 46910
        - TourismPerTurn: 2220.5
        - CulturePerTurn: 5250
        - PolicyBranches:
          - Freedom: 11
          - Tradition: 6
          - Artistry: 6
          - Progress: 6
          - Authority: 2
        - FoundedReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone:
            - Distance: Far
            - Open Borders
          - Mongolia:
            - Distance: Neighbors
            - Open Borders
          - America:
            - Distance: Close
            - Denounced Them
          - Germany:
            - Distance: Neighbors
            - Open Borders
          - Austria:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 2%)
          - Spain:
            - Distance: Neighbors
            - War (Our Score: 2%; Our War Weariness: 17%)
            - Denounced Them
        - Votes: 40
        
        ## Player 5
        - Civilization: Austria
        - Leader: Maria Theresa
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Austria) have both chosen to adopt the Order Ideology. (999)
          - Spain's leader has expressed a public opinion of Austria (100).
          - Spain's leader has formed a private opinion of Austria (95).
          - We are trade partners. (40)
          - We have opened our borders to each other. (12)
          - You (Austria) have denounced one of Spain's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have shared embassies. (1)
          - Spain's real approach to Austria is Friendly.
          - We have divergent Social Policies. (-3)
          - Religious differences strain your (Austria) relationship. (-30)
        - TheirOpinionOfUs:
          - Your (Spain) votes supported Austria's civ's interests in the United Nations.
          - You (Spain) have both chosen to adopt the Order Ideology.
          - Austria's leader has expressed a public opinion of you (Spain) (100).
          - You (Spain) have denounced one of Austria's declared enemies!
          - We are trade partners.
          - We have made a public Declaration of Friendship!
          - We fought together against a common foe.
          - We have made Declarations of Friendship with the same leaders!
          - Your (Spain) recent diplomatic actions please Austria.
          - We have opened our borders to each other.
          - We have shared embassies.
          - We have divergent Social Policies.
          - We have different religious beliefs.
          - Austria desire friendly relations with Spain.
          - Austria are spreading Austria's own religion, but you (Spain) converted some of their cities to your (Spain) religion.
          - We defeated Austria's proposal in the United Nations.
        - Score: 3211
        - Era: Information
        - Technologies: 69
        - Cities: 13
        - Population: 358
        - Territory: 466
        - Gold: 6622
        - GoldPerTurn: 408
        - HappinessSituation: Happy
        - HappinessPercentage: 65
        - MilitaryStrength: 10891
        - TourismPerTurn: 1379.5
        - CulturePerTurn: 2482
        - PolicyBranches:
          - Tradition: 6
          - Artistry: 6
          - Statecraft: 1
          - Order: 12
          - Progress: 6
        - FoundedReligion: Catholicism
        - Relationships:
          - The Shoshone:
            - Distance: Neighbors
            - War (Our Score: 6%; Our War Weariness: 2%)
            - Denounced Them
          - Mongolia:
            - Distance: Neighbors
            - War (Our Score: 24%; Our War Weariness: 8%)
            - Denounced Them
          - America:
            - Distance: Far
            - Declaration of Friendship
          - Germany:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 1%)
            - Denounced Them
          - Byzantium:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 1%)
            - Denounced Them
          - Spain:
            - Distance: Far
            - Open Borders
            - Declaration of Friendship
        - Votes: 9
        
        ## Player 6
        - Civilization: Germany
        - Leader: Bismarck
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Germany) have denounced one of Spain's declared enemies! (11)
          - We have similar Social Policies. (3)
          - Spain's real approach to Germany is Guarded.
          - You (Germany) have denounced a leader Spain made a Declaration of Friendship with! (-11)
          - You (Germany) have made a Declaration of Friendship with one of Spain's enemies! (-13)
          - You (Germany) have made a Defensive Pact with one of Spain's enemies! (-15)
          - Religious differences strain your (Germany) relationship. (-30)
          - Your (Germany) spies were caught stealing from Spain. (-33)
          - Spain's leader has formed a private opinion of Germany (-35).
          - Spain's leader has expressed a public opinion of Germany (-40).
          - You (Germany) have chosen to adopt the Autocracy Ideology, but Spain believe in Order. (-999)
          - You (Germany) are at war! (-99999)
        - TheirOpinionOfUs:
          - You (Spain) are not competing for the favor of the same City-States.
          - You (Spain) have denounced one of Germany's declared enemies!
          - We have similar Social Policies.
          - You (Spain) have no contested borders.
          - Religious differences strain your (Spain) relationship.
          - You (Spain) are competing for World Wonders.
          - You (Spain) have made a Declaration of Friendship with one of Germany's enemies!
          - Germany's friends or allies have denounced you (Spain)!
          - We have denounced each other!
          - You (Spain) have denounced a leader Germany made a Declaration of Friendship with!
          - We defeated Germany's proposal in the United Nations.
          - Your (Spain) votes opposed Germany's civ's interests in the United Nations.
          - You (Spain) have chosen to adopt the Order Ideology, but Germany believe in Autocracy.
          - Your (Spain) spies were caught stealing from Germany.
          - You (Spain) are at war!
        - Score: 2232
        - Era: Information
        - GoldenAge: 6 turns remaining
        - Technologies: 68
        - Cities: 9
        - Population: 233
        - Territory: 323
        - Gold: 91
        - GoldPerTurn: 16
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 42
        - MilitaryStrength: 5043
        - TourismPerTurn: 724.5
        - CulturePerTurn: 1656
        - PolicyBranches:
          - Fealty: 1
          - Autocracy: 6
          - Tradition: 4
          - Rationalism: 3
          - Progress: 5
          - Imperialism: 2
          - Statecraft: 3
          - Authority: 2
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Shoshone:
            - Distance: Close
            - Denounced Them
          - Mongolia:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - America:
            - Distance: Close
            - Denounced Them
          - Austria:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 1%)
            - Denounced Them
          - Byzantium:
            - Distance: Neighbors
            - Open Borders
          - Spain:
            - Distance: Close
            - War (Our Score: 24%; Our War Weariness: 28%)
            - Denounced Them
        - Votes: 14
        - 7: Defeated Major Civilization France
        
        ## Player 22
        - Civilization: Colombo
        - Leader: City State
        - Population: 15
        - MajorityReligion: Protestantism
        - Relationships:
          - The Shoshone: Friends (Influence: 52, Distance: Far)
          - Mongolia: Friends (Influence: 455, Distance: Far, Protected)
          - Germany: Friends (Influence: 447, Distance: Far, Protected)
          - America: Friends (Influence: 486, Distance: Neighbors, Protected)
          - Austria: Friends (Influence: 207, Distance: Distant)
          - Byzantium: Friends (Influence: 550, Distance: Close, Protected)
          - Spain: Neutral (Influence: -48, Distance: Neighbors)
        - 23: Defeated Minor Civilization Raqmu
        
        ## Player 24
        - Civilization: M'banza-Kongo
        - Leader: City State
        - MajorAlly: Austria
        - Population: 6
        - Relationships:
          - The Shoshone: War - Peace Currently Blocked (Influence: -60, Distance: Neighbors)
          - Mongolia: War - Peace Currently Blocked (Influence: -60, Distance: Neighbors)
          - Germany: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - America: Friends (Influence: 147, Distance: Neighbors)
          - Austria: Ally (Influence: 372, Distance: Close, Protected)
          - Byzantium: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Spain: Neutral (Influence: 0, Distance: Close)
        
        ## Player 25
        - Civilization: Rio de Janeiro
        - Leader: City State
        - Population: 21
        - Relationships:
          - The Shoshone: Neutral (Influence: 0, Distance: Far)
          - Mongolia: Friends (Influence: 328, Distance: Neighbors, Protected)
          - Germany: Friends (Influence: 409, Distance: Neighbors, Protected)
          - America: Friends (Influence: 144, Distance: Far)
          - Austria: Friends (Influence: 207, Distance: Close, Protected)
          - Byzantium: Friends (Influence: 520, Distance: Close, Protected)
          - Spain: Friends (Influence: 511, Distance: Close)
        
        ## Player 26
        - Civilization: Brussels
        - Leader: City State
        - Population: 18
        - Relationships:
          - The Shoshone: Friends (Influence: 212, Distance: Neighbors, Protected)
          - Mongolia: Friends (Influence: 436, Distance: Far, Protected)
          - Germany: Friends (Influence: 311, Distance: Far)
          - America: Friends (Influence: 165, Distance: Far)
          - Austria: Friends (Influence: 570, Distance: Neighbors, Protected)
          - Byzantium: Friends (Influence: 530, Distance: Distant)
          - Spain: Friends (Influence: 145, Distance: Distant)
        
        ## Player 27
        - Civilization: Shanghai
        - Leader: City State
        - Population: 17
        - Relationships:
          - The Shoshone: Friends (Influence: 45, Distance: Neighbors, Protected)
          - Mongolia: Friends (Influence: 284, Distance: Neighbors, Protected)
          - Germany: Friends (Influence: 113, Distance: Far)
          - America: Friends (Influence: 128, Distance: Close)
          - Austria: Friends (Influence: 73, Distance: Neighbors, Protected)
          - Byzantium: Friends (Influence: 476, Distance: Far)
          - Spain: Friends (Influence: 123, Distance: Close)
        
        ## Player 28
        - Civilization: Huari
        - Leader: City State
        - MajorAlly: Byzantium
        - Population: 15
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: Friends (Influence: 404, Distance: Distant)
          - Germany: Friends (Influence: 438, Distance: Far, Protected)
          - America: Friends (Influence: 315, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Distant)
          - Byzantium: Ally (Influence: 1235, Distance: Neighbors, Protected)
          - Spain: War (Influence: -60, Distance: Close)
        
        ## Player 29
        - Civilization: Warsaw
        - Leader: City State
        - MajorAlly: Germany
        - Population: 17
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone: Friends (Influence: 144, Distance: Distant)
          - Mongolia: Friends (Influence: 376, Distance: Close, Protected)
          - Germany: Ally (Influence: 853, Distance: Neighbors, Protected)
          - America: Friends (Influence: 268, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Far)
          - Byzantium: Friends (Influence: 830, Distance: Close, Protected)
          - Spain: War (Influence: -60, Distance: Distant)
        
        ## Player 30
        - Civilization: Kabul
        - Leader: City State
        - MajorAlly: Germany
        - Population: 26
        - MajorityReligion: Tengriism
        - Relationships:
          - The Shoshone: Friends (Influence: 148, Distance: Distant)
          - Mongolia: Friends (Influence: 140, Distance: Far, Protected)
          - Germany: Ally (Influence: 698, Distance: Neighbors, Protected)
          - America: Friends (Influence: 216, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Distant)
          - Byzantium: Friends (Influence: 955, Distance: Distant)
          - Spain: War (Influence: -60, Distance: Distant)
        
        ## Player 31
        - Civilization: Manila
        - Leader: City State
        - MajorAlly: Byzantium
        - Population: 24
        - Relationships:
          - The Shoshone: Friends (Influence: 60, Distance: Neighbors)
          - Mongolia: Friends (Influence: 75, Distance: Distant)
          - Germany: Friends (Influence: 480, Distance: Close, Protected)
          - America: Neutral (Influence: -47, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Neighbors)
          - Byzantium: Ally (Influence: 821, Distance: Distant, Protected)
          - Spain: War (Influence: -60, Distance: Distant)
        - 32: Defeated Minor Civilization Argos
        
        ## Player 33
        - Civilization: Sydney
        - Leader: City State
        - MajorAlly: Byzantium
        - Population: 14
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone: Friends (Influence: 153, Distance: Distant)
          - Mongolia: Neutral (Influence: -59, Distance: Distant)
          - Germany: Friends (Influence: 814, Distance: Far, Protected)
          - America: Friends (Influence: 773, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Distant)
          - Byzantium: Ally (Influence: 1507, Distance: Neighbors, Protected)
          - Spain: War (Influence: -60, Distance: Distant)
        
        ## Player 34
        - Civilization: Genoa
        - Leader: City State
        - MajorAlly: Germany
        - Population: 21
        - MajorityReligion: Tengriism
        - Relationships:
          - The Shoshone: Friends (Influence: 274, Distance: Distant)
          - Mongolia: Friends (Influence: 311, Distance: Close, Protected)
          - Germany: Ally (Influence: 876, Distance: Neighbors, Protected)
          - America: Friends (Influence: 256, Distance: Far)
          - Austria: War (Influence: -60, Distance: Distant)
          - Byzantium: Friends (Influence: 847, Distance: Neighbors, Protected)
          - Spain: War (Influence: -60, Distance: Far)
        
        ## Player 35
        - Civilization: Assur
        - Leader: City State
        - MajorAlly: Germany
        - Population: 20
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: Friends (Influence: 139, Distance: Distant, Protected)
          - Germany: Ally (Influence: 692, Distance: Neighbors, Protected)
          - America: Friends (Influence: 37, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Distant)
          - Byzantium: Friends (Influence: 937, Distance: Neighbors, Protected)
          - Spain: War (Influence: -60, Distance: Distant)
        
        ## Player 36
        - Civilization: Luba
        - Leader: City State
        - Population: 20
        - MajorityReligion: Protestantism
        - Relationships:
          - The Shoshone: Neutral (Influence: 5, Distance: Neighbors, Protected)
          - Mongolia: Friends (Influence: 326, Distance: Close, Protected)
          - Germany: Friends (Influence: 218, Distance: Far)
          - America: Friends (Influence: 206, Distance: Close)
          - Austria: Friends (Influence: 743, Distance: Neighbors, Protected)
          - Byzantium: Friends (Influence: 519, Distance: Far)
          - Spain: Friends (Influence: 85, Distance: Far)
        
        ## Player 37
        - Civilization: Shedet
        - Leader: City State
        - MajorAlly: Byzantium
        - Population: 10
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: Friends (Influence: 180, Distance: Distant)
          - Germany: Friends (Influence: 164, Distance: Far)
          - America: Friends (Influence: 78, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Distant)
          - Byzantium: Ally (Influence: 678, Distance: Neighbors, Protected)
          - Spain: War (Influence: -60, Distance: Far)
        - 63: Barbarians
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: Mongolia
        - Mongolia:
          - CapitalsControlled:
            - Karakorum
            - Paris
          - CapitalsPercentage: 25
        
        ## ScienceVictory
        - America:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Austria:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Byzantium:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        - Germany:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Mongolia:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Spain:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - The Shoshone:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        
        ## CulturalVictory
        - CivsNeeded: 6
        - Contender: Byzantium
        - America:
          - Influences:
            - The Shoshone: Familiar (28%) - Rising (721 turns to Influential, tourism/culture ratio 134%)
            - Mongolia: Familiar (49%) - Rising (220 turns to Influential, tourism/culture ratio 157%)
            - Spain: Familiar (45%) - Rising (159 turns to Influential, tourism/culture ratio 223%)
            - Germany: Familiar (28%) - Rising Slowly (tourism/culture ratio 108%)
            - Byzantium: Exotic (12%) - Rising Slowly (tourism/culture ratio 31%)
            - Austria: Exotic (15%) - Rising Slowly (tourism/culture ratio 80%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Austria:
          - Influences:
            - The Shoshone: Influential (125%) - Rising (tourism/culture ratio 306%)
            - Mongolia: Dominant (212%) - Rising (tourism/culture ratio 397%)
            - America: Influential (179%) - Rising (tourism/culture ratio 504%)
            - Germany: Influential (113%) - Rising (tourism/culture ratio 266%)
            - Byzantium: Popular (65%) - Rising Slowly (tourism/culture ratio 94%)
            - Spain: Dominant (202%) - Rising (tourism/culture ratio 681%)
          - PolicyPercentage: 100
          - InfluentialCivs: 5
        - Byzantium:
          - Influences:
            - The Shoshone: Influential (157%) - Rising (tourism/culture ratio 924%)
            - Mongolia: Dominant (254%) - Rising (tourism/culture ratio 1033%)
            - America: Influential (145%) - Rising (tourism/culture ratio 810%)
            - Germany: Dominant (207%) - Rising (tourism/culture ratio 895%)
            - Austria: Popular (84%) - Rising (9 turns to Influential, tourism/culture ratio 530%)
            - Spain: Influential (165%) - Rising (tourism/culture ratio 1050%)
          - PolicyPercentage: 100
          - InfluentialCivs: 5
        - Germany:
          - Influences:
            - The Shoshone: Familiar (37%) - Rising (172 turns to Influential, tourism/culture ratio 193%)
            - Mongolia: Popular (67%) - Rising (38 turns to Influential, tourism/culture ratio 257%)
            - America: Familiar (37%) - Rising (180 turns to Influential, tourism/culture ratio 189%)
            - Austria: Exotic (15%) - Rising Slowly (tourism/culture ratio 92%)
            - Byzantium: Exotic (24%) - Rising Slowly (tourism/culture ratio 64%)
            - Spain: Familiar (40%) - Rising (163 turns to Influential, tourism/culture ratio 228%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Mongolia:
          - Influences:
            - The Shoshone: Exotic (20%) - Rising Slowly (tourism/culture ratio 112%)
            - Germany: Exotic (23%) - Rising Slowly (tourism/culture ratio 108%)
            - Spain: Exotic (22%) - Rising Slowly (tourism/culture ratio 142%)
            - Austria: Exotic (10%) - Rising Slowly (tourism/culture ratio 57%)
            - Byzantium: Exotic (9%) - Rising Slowly (tourism/culture ratio 30%)
            - America: Exotic (23%) - Rising Slowly (tourism/culture ratio 123%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Spain:
          - Influences:
            - The Shoshone: Familiar (33%) - Rising Slowly (tourism/culture ratio 120%)
            - Mongolia: Familiar (42%) - Rising Slowly (tourism/culture ratio 112%)
            - America: Familiar (39%) - Rising (813 turns to Influential, tourism/culture ratio 135%)
            - Germany: Familiar (27%) - Rising Slowly (tourism/culture ratio 78%)
            - Byzantium: Exotic (11%) - Rising Slowly (tourism/culture ratio 23%)
            - Austria: Exotic (15%) - Rising Slowly (tourism/culture ratio 62%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - The Shoshone:
          - Influences:
            - Austria: Familiar (25%) - Rising Slowly (tourism/culture ratio 89%)
            - Mongolia: Popular (87%) - Rising (26 turns to Influential, tourism/culture ratio 200%)
            - Spain: Popular (72%) - Rising (40 turns to Influential, tourism/culture ratio 307%)
            - Germany: Popular (53%) - Rising (452 turns to Influential, tourism/culture ratio 155%)
            - Byzantium: Familiar (29%) - Rising Slowly (tourism/culture ratio 61%)
            - America: Popular (53%) - Rising (114 turns to Influential, tourism/culture ratio 201%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        
        ## DiplomaticVictory
        - VotesNeeded: 44
        - Status: World Congress - Voting in 4 turns
        - ActiveResolutions:
          - Casus Belli:
            - Description: The world recognizes the need for justifiable war to resolve diplomatic disputes.
              While this resolution is active, unit maintenance costs are lowered by 15% Gold. 0.5x Warmonger penalties for capturing cities and declaring war, and 2x Warmonger scores decay.
            - EnactedOn: -1
          - Natural Heritage Sites:
            - Description: Each Natural Wonder provides +2 to all Yields when worked.
            - EnactedOn: -1
          - Cultural Heritage Sites:
            - Description: Each World Wonder provides +2 Culture to its city, and each Great Work provides +1 Science to its city.
            - EnactedOn: -1
          - German Sphere of Influence: Kabul:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - German Sphere of Influence: Assur:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - World Ideology: Freedom:
            - Description: Designate an Ideology as the official World Ideology. Civilizations following the Ideology get an additional Delegate, plus 1 Delegate for every other Civilization that follows the Ideology. Public opinion in favor of that Ideology is increased for all Civilizations. Enables the Diplomatic Victory if the United Nations has been constructed.
              Available once any Civilization discovers Nuclear Fission.
            - EnactedOn: -1
          - Open Door: Shanghai:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - Byzantine Sphere of Influence: Shedet:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Open Door: Rio de Janeiro:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - Open Door: Brussels:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - Open Door: Luba:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - German Sphere of Influence: Genoa:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Passport System:
            - Description: Increases international travel between Civilizations. Increases the Tourism modifier for all Civilizations by 50%.
              Available once any Civilization discovers Flight.
            - EnactedOn: -1
          - Byzantine Sphere of Influence: Huari:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - German Sphere of Influence: Warsaw:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Sanction: America:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: -1
          - Open Door: Colombo:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - Austrian Sphere of Influence: M'banza-Kongo:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
        - Proposals:
          - Repeal: Passport System:
            - Description: Increases international travel between Civilizations. Increases the Tourism modifier for all Civilizations by 50%.
              Available once any Civilization discovers Flight.
            - Proposer: Germany
          - Enact: Sanction: Austria:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - Proposer: The Shoshone
          - Repeal: German Sphere of Influence: Assur:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - Proposer: Byzantium
        - Contender: Byzantium
        - America:
          - Delegates: 6
          - VictoryPercentage: 13
        - Austria:
          - Delegates: 9
          - VictoryPercentage: 20
        - Byzantium:
          - Delegates: 40
          - VictoryPercentage: 90
        - Germany:
          - Delegates: 14
          - VictoryPercentage: 31
        - Mongolia:
          - Delegates: 7
          - VictoryPercentage: 15
        - Spain:
          - Delegates: 6
          - VictoryPercentage: 13
        - The Shoshone:
          - Delegates: 9
          - VictoryPercentage: 20
        
        # Briefings
        ## Military Briefing
        **Military Intelligence Brief – Turn 449**  
        *Prepared for Isabella, Leader of Spain (Player 3)*  
        
        ---
        
        ### 1. Tactical Developments Since Turn 444  
        
        | Zone / City | New / Up‑graded Units | Combat Outcomes (Spain) | Enemy Activity |
        |-------------|----------------------|--------------------------|----------------|
        | **Madrid** (Land 1060) | No new units. Existing garrison (2 Infantry, 1 Special Forces, 2 Machine Guns, 1 Paratrooper) unchanged. | – No ground combat this turn. | German naval units continue to patrol the adjacent sea zone; no land incursion. |
        | **Barcelona** (Land 1276) | No new land units; composition unchanged (1 Paratrooper, 2 Artillery, 2 Special Forces, 2 Machine Guns). | – No land combat. | German sea‑zone remains enemy‑dominated (Fleet Destroyers, Dreadnought). No amphibious landings observed. |
        | **Toledo** (Land 3336) | No changes; garrison stable (1 Artillery, 3 Machine Guns, 1 City‑State Infantry). | – No combat. | Sea‑zone enemy‑dominated (German Fleet Destroyer). |
        | **Tiflis** (Land 10390) | Garrison unchanged (1 Infantry, 1 Bomber, 1 Paratrooper). | **Combat #0 (Plains Hills 42,22)** – Spanish Paratrooper (ID 19473) took 34 % damage, survived. <br>**Combat #1 (Snow Land 36,7)** – Spanish Infantry (ID 19596) killed; remained unit count −1. | Byzantine Light Tank and German Bomber still present in adjacent sea zone; German air presence persists. |
        | **Coastal/Sea – Tiflis** (Sea ‑10390) | No Spanish naval units present. | **Combat #4 (Ocean 39,11)** – German Fleet Destroyer (ID 19028) survived Spanish attack; Spanish destroyer‑type units not present. | German fleet (Battleship 1, Fleet Destroyers 10, Krupp Gun 1) dominates the sea zone. |
        | **Coastal/Sea – Barcelona** (Sea ‑3336) | No Spanish naval units present. | – No direct sea combat this turn. | German Fleet Destroyer (ID 20339, promoted) continues to hold the zone. |
        | **Other Zones** | – | – | Enemy forces (Byzantine, German) remain concentrated in their own fronts; no new incursions toward Spanish borders. |
        | **Great Units** | Created: **Great Diplomat** (ID 20369) in Madrid. | – | – |
        | **Unit Promotions** | Paratrooper (ID 19473) promoted *Medic I*. | – | – |
        | **Unit Losses** | Spanish Infantry (ID 19596) killed defending Tiflis. | – | – |
        
        **Summary:**  
        - Spanish land forces have held their positions; only one infantry loss at Tiflis.  
        - No new Spanish naval assets were produced; sea control around Barcelona and Toledo remains firmly in German hands.  
        - German naval expansion continued (new Fleet Destroyer, Anti‑Aircraft Gun) and a German Fighter rebased to Eisenstadt.  
        - Spain’s only strategic gain was the creation of a Great Diplomat in Madrid.  
        
        ---
        
        ### 2. Force Posture – Zone‑Level Balance (Current vs. Turn 444)
        
        | Zone (City) | Spanish Strength (CS) | Enemy Strength (CS) | Net Balance | Dominance |
        |-------------|----------------------|---------------------|-------------|-----------|
        | **Madrid** (1060) | ~1,740 (land) | 0 | **+** | Friendly – Counterattack |
        | **Barcelona** (1276) | ~2,130 (land) | ~1,631 (German Fleet Destroyers) | **+** (land) but **Sea = Enemy** | Even (land) / Enemy (sea) |
        | **Toledo** (3336) | ~1,730 (land) | 0 | **+** | Friendly – Counterattack |
        | **Tiflis** (10390) | ~656 (incl. captured Bomber) | ~881 (Byzantine Light Tank + German Bomber) | **‑** | Even (land) / Enemy (sea) |
        | **Constantinople** (1061) | 0 | ~4,000 (Byzantine Artillery/Machine Guns) | **‑** | Enemy |
        | **Berlin** (1063) | 0 | ~3,800 (German Machine Guns, Krupp Guns) | **‑** | Enemy |
        | **Sea – Barcelona** (‑3336) | 0 (Spanish ships) | ~3,760 (German Fleet Destroyers, Dreadnought) | **‑** | Enemy |
        | **Sea – Tiflis** (‑10390) | 0 (Spanish ships) | ~3,800 (German Battleship, Fleet Destroyers) | **‑** | Enemy |
        
        *Combat Strength (CS) estimates based on unit tables supplied. No significant change in overall balance since Turn 444; Spanish land superiority around core cities persists, while maritime dominance remains German.*  
        
        ---
        
        ### 3. Threat Assessment  
        
        | Threat | Origin | Proximity to Spain | Capability | Current Status |
        |--------|--------|-------------------|------------|----------------|
        | **German Naval Supremacy** | Germany (Fleet Destroyers, Battleship, Dreadnought) | Adjacent to Barcelona & Toledo sea zones | Ability to project amphibious raids, air‑support from carriers | Unchanged; recent German ship promotions increase durability. |
        | **Byzantine Light Tank & Air Units** | Byzantium (Light Tank at Nicomedia, Bomber near Tiflis) | Eastern front near Tiflis | Land‑strike and air‑strike on coastal tiles, threatens Havana‑type tile (Hacienda) | Present; no change. |
        | **Mongolian Anti‑Air/Paratrooper** | Mongolia (Anti‑Air at Beshbalik, Bomber) | Distant – no direct border pressure | Limited to far‑range air attacks, but could support Byzantine actions | No activity near Spanish borders this turn. |
        | **Shoshone Air Activity** | Shoshone (Machine Gun unit, no aircraft) | Coastal western edge, Open Borders | Currently internal; denouncement may not translate to aggression | No incursions observed. |
        | **Uranium Tile Vulnerability** | Hacienda on (40,21) – not yet a uranium resource | Adjacent to Tiflis (coastal) | Susceptible to naval bombardment (German fleet) and air raids (Byzantine bomber) | Tile remains a Hacienda; no uranium secured. |
        
        **Key Risks:**  
        - **Sea‑zone exposure** around Barcelona makes any coastal infrastructure (including Great Works) vulnerable to amphibious assault.  
        - **Tiflis** remains a high‑value target (Manhattan Project) with insufficient anti‑air/anti‑naval defense.  
        - **German naval build‑up** could enable a coordinated amphibious push if Spain cannot field any sea units soon.  
        
        ---
        
        ### 4. Strategic Resources & Projects  
        
        | Project / Resource | Current Status (Turn 449) | Immediate Implications |
        |--------------------|---------------------------|------------------------|
        | **Manhattan Project** (Tiflis) | Production at **12 %** (≈ 101 PPT). No change since Turn 444. | Requires ~ 87 more turns at current rate; deadline at Turn 452 → unlikely to finish on time without gold‑purchase acceleration. |
        | **Uranium Tile (40,21)** | Occupied by a **Hacienda** (producing Food/Prod/Gold). No uranium resource present. | Must be cleared and a Builder sent to improve a true uranium node before any atomic weapon can be pursued. Tile is exposed to German naval and Byzantine air threats. |
        | **Gold Reserves** | **2,021 G** (turn 449), G/PT ≈ 586. | Sufficient to purchase multiple turns of Manhattan production (≈ 300 PPT per 1 G). No purchases recorded yet. |
        | **Great Diplomat** (Madrid) | Created this turn (ID 20369). | Can be used to improve relations or negotiate cease‑fires; however, Spain is currently at war with Germany, Byzantium, and Austria, limiting diplomatic leverage. |
        
        ---
        
        ### 5. Comparative Snapshot (Turn 444 → Turn 449)
        
        | Metric | Turn 444 | Turn 449 | Δ |
        |--------|----------|----------|---|
        | **Spanish Land Units** | 20 | 20 (no net change) | – |
        | **Spanish Naval Units** | 0 (no ships) | 0 (still none) | – |
        | **German Naval Strength (adjacent sea zones)** | ~4 destroyers | +1 Fleet Destroyer (ID 20339), +1 Anti‑Aircraft Gun | +2 German assets |
        | **Spanish Gold** | 1,317 G | 2,021 G | +704 G |
        | **Gold/Turn** | ≈ 351 G | ≈ 586 G | +235 G/PT |
        | **Manhattan Progress** | 12 % (101 PPT) | 12 % (unchanged) | – |
        | **Uranium Tile** | Hacienda on (40,21) | Same | – |
        | **Great Works / Projects** | None listed | Great Diplomat created | +1 Great Diplomat |
        | **War Weariness (Spain)** | 43 % vs. Germany, 24 % vs. Byzantium, 17 % vs. Austria (as per player data) | Unchanged | – |
        
        **Overall Trend:** Economic capacity has risen sharply, but military balance (especially at sea) remains unfavorable. No progress on the Manhattan Project despite increased gold.  
        
        ---
        
        ### 6. High‑Level Needs & Excesses  
        
        | Category | Current Situation | Assessment |
        |----------|-------------------|------------|
        | **Land Force Strength** | Core cities (Madrid, Barcelona, Toledo) collectively ~6,000 CS, exceeding local enemy strength. | Adequate; no immediate reinforcement required. |
        | **Naval Presence** | 0 Spanish warships; sea zones around Barcelona & Toledo controlled by Germany. | **Deficit** – at least 2 Armada (unique Corvette) units needed to contest German destroyers, plus a coastal defense battery (Anti‑Air or Artillery) to deter amphibious landings. |
        | **Air Defense** | Single Bomber (captured) at Tiflis; no dedicated AA or fighter units near Tiflis. | **Deficit** – add 1 Anti‑Aircraft Gun or rebase a Fighter to Eisenstadt and escort to Tiflis. |
        | **Strategic Resources** | No uranium; only a Hacienda on a non‑uranium tile. | **Critical** – locate and improve a uranium node; protect the tile while construction occurs. |
        | **Gold Surplus** | 2,021 G, ample for production purchases. | **Excess** – can be allocated to accelerate Manhattan Project (buy production) or to fund naval construction (Armada). |
        | **Manhattan Project Timing** | 12 % complete, ~87 turns remaining at current PPT. Deadline Turn 452 (8 turns away). | **Urgent** – must purchase > 250 PPT per turn (≈ 800 G total) to meet deadline; otherwise diplomatic penalty imminent. |
        
        ---
        
        ### 7. Mobility & Evacuation Considerations  
        
        | City | Threat Level | Recommended Action |
        |------|--------------|--------------------|
        | **Madrid** | Low – inland, no immediate sea threat. | Maintain current garrison; consider moving any valuable Great Works to Madrid if threatened elsewhere. |
        | **Barcelona** | High – sea zone enemy‑dominated; possible amphibious strike. | Transfer any high‑value assets (Great Works, wonders) to Toledo or Madrid via Caravans; evaluate building coastal AA batteries. |
        | **Toledo** | Moderate – sea zone still enemy‑controlled, but inland location provides a safe staging point. | Use as evacuation hub for Barcelona; keep garrison ready to repel any landing. |
        | **Tiflis** | High – strategic tile (Hacienda) and Manhattan Project exposed to Byzantine tank and German bomber. | Deploy at least one Anti‑Aircraft Gun and a Fighter (if available) to protect; consider moving the Hacienda (if possible) or re‑working the tile to a fortified improvement. |
        
        ---
        
        ### 8. Diplomatic Context (Non‑Quantitative)  
        
        - **War Status:** Spain is at war with Germany (Score ‑24 %, War Weariness 43 %), Byzantium (Score ‑2 %, Weariness 24 %), and Austria (Score ‑6 %, Weariness 2 %).  
        - **Allied Relations:** Declaration of Friendship with America; Open Borders with Austria (far) and Shoshone.  
        - **Potential Leverage:** The newly created Great Diplomat could be employed to negotiate limited cease‑fires or trade for naval support, but existing war declarations limit diplomatic options.  
        
        ---
        
        **Intelligence Flags – Immediate Attention**  
        
        1. **Naval Deficit** – Build/convert at least two Armada units; prioritize coastal AA to mitigate amphibious risk.  
        2. **Uranium Acquisition** – Scout for uranium deposits; clear Hacienda on (40,21) and assign a Builder.  
        3. **Manhattan Acceleration** – Allocate ~ 800 G to buy production over the next 4‑5 turns to approach the Turn 452 deadline; otherwise expect diplomatic penalty.  
        4. **Air Defense for Tiflis** – Station an Anti‑Aircraft Gun or re‑base a Fighter to protect the Manhattan site.  
        5. **Asset Relocation** – Move any Great Works from Barcelona to interior cities (Toledo/Madrid).  
        
        ---  
        
        *End of Brief.*
        
        ## Economy Briefing
        (Produced with your instruction: TURN 449-452 FINAL ECONOMY MONITORING: Track Manhattan Project completion at Tiflis (should finish Turn 450). Monitor any production interruptions from enemy military action. Confirm Electronics research progression. Track Great Person point accumulation - Spaceflight Pioneers expected to trigger soon providing free Great Engineer/Scientist. Monitor treasury growth for any final-turn purchasing opportunities that might affect final score. Report on faith accumulation progress (currently 153/turn, 200 needed for Great Scientist purchase) and whether Great Person acquisition possible before game conclusion.)
        
        **Spain – Economic Briefing (Post‑Turn 449)**  
        *Prepared for Isabella – Turn 449*  
        
        ---
        
        ### 1. Treasury & Gold Flow  
        
        - **Gold in Treasury:** **2 021 G** (↑ 704 G since Turn 444) – a strong cash‑injection primarily from the recent influx of trade‑route gold and the recent influx of gold from Austria (≈ 103 G/t from deal #4).  
        - **Gold per Turn (net):** **+586 G/t** (up +235 G/t vs. Turn 444).  
          - **Sources:**  
            - City output: Madrid (+787 G/t), Barcelona (+180 G/t), Toledo (+81 G/t), Tiflis (+27 G/t).  
            - Incoming trade‑route (Karakorum → Madrid) ≈ +8 G/t.  
            - Outgoing trade‑routes (all land) generate ~+70 G/t total.  
            - Deal income from Austria (+103 G/t) and other minor deals.  
          - **Deductions:**  
            - Unit upkeep (23 units) – modestly offset by the *Casus Belli* maintenance discount (‑15 %).  
            - No significant war‑related expenditures this turn.  
        
        **Assessment:** Treasury is healthy; no risk of overflow or shortage in the next few turns.
        
        ---
        
        ### 2. Production & Major Projects  
        
        | City      | PPT (post‑modifiers) | Current Production | Turns Remaining |
        |-----------|----------------------|--------------------|-----------------|
        | **Madrid**| 303 PPT | **Infantry** (completed Turn 452) | 2 |
        | **Barcelona**| 249 PPT | **Machine Gun** (finishes Turn 452) | 1 |
        | **Toledo**| 185 PPT | **Paratrooper → Special Forces** (upgraded this turn) | 1 |
        | **Tiflis**| 103 PPT | **Manhattan Project** (Completes Turn 450) | 1 |
        
        - **Manhattan Project** will finish at **Turn 450** (one turn away). No enemy units are positioned to disrupt the city; Tiflis remains under Spanish control despite a –5 % happiness delta.  
        - **Computers** was researched this turn (turn 449), unlocking *Radar* (already in research) and enabling the *Spaceflight* chain.  
        - **Electronics** is effectively complete with *Computers* now available; the next step, *Radar*, is 19 turns away.  
        
        **Assessment:** No production interruptions expected; all key projects on schedule.
        
        ---
        
        ### 3. Great Person Points & Upcoming Triggers  
        
        - **Great Scientist / Engineer Points:**  **≈ 152 p/t** (derived from Science per Turn 980 × policy multipliers).  
        - **Great Scientist Purchase:** Faith per Turn = 165 → ~**200 Faith** required for a Great Scientist (via Faith purchase). Current Faith reserve is **2 021 F**; therefore a Great Scientist can be bought immediately if desired.  
        - **Spaceflight Pioneer:** With *Computers* completed, the *Spaceflight* tree is unlocked. At current Science output, the “Spaceflight Pioneer” civic will trigger within the next 20‑
        
        ## Diplomacy Briefing
        **Diplomatic Brief – Turn 449**  
        *Leader: Isabella (Spain, Player 3)*  
        
        ---
        
        ### 1. World Congress – Current Snapshot (Voting in 4 turns, Turn 453)
        
        | Civilization | Delegates | Victory % | Note |
        |--------------|-----------|-----------|------|
        | **Byzantium** | **40** | **90 %** | Still the clear front‑runner; 5 delegates short of the 45‑delegate win threshold. |
        | **Spain**      | **6** | **13 %** | No change since Turn 444; delegate count remains low. |
        | **Austria**    | **9** | **20 %** | Stable Order‑bloc member. |
        | **Germany**    | **14** | **31 %** | Autocracy bloc, hostile; unchanged. |
        | **America**    | **6** | **13 %** | Order ally, stable. |
        | **Mongolia**   | **7** | **15 %** | Autocracy bloc, still at peace with Spain. |
        | **The Shoshone** | **10** | **22 %** | Critical swing vote; unchanged. |
        | **Other civs** (minor participants) | — | — | Total **VotesNeeded = 44** (unchanged). |
        
        **Active Resolutions** – All previously enacted resolutions remain in force (Casus Belli, Natural & Cultural Heritage Sites, Freedom World Ideology, Open‑Door policies, etc.). No new resolutions have been proposed since Turn 444.
        
        **Pending Proposals (to be voted on Turn 453)**  
        
        | Proposal | Proposer | Effect if Enacted |
        |----------|----------|-------------------|
        | **Repeal: Passport System** | Germany | Removes 50 % tourism boost; no delegate impact. |
        | **Enact: Sanction – Austria** | The Shoshone | Cuts all trade/Corporation links with Austria; 0.5× Warmonger penalty when Spain (or any) wars with Austria. No delegate effect. |
        | **Repeal: German Sphere of Influence – Assur** | Byzantium | Removes a sphere‑of‑influence option; no delegate impact. |
        
        No other proposals are on the agenda; the voting schedule remains unchanged.
        
        ---
        
        ### 2. Delegate Changes Since Turn 444  
        
        | Civ | Delegates (Turn 444) | Delegates (Turn 449) | Δ |
        |-----|----------------------|----------------------|---|
        | Byzantium | 40 | 40 | **0** |
        | Spain     | 6  | 6  | **0** |
        | The Shoshone | 10 | 10 | **0** |
        | Others (Austria, Germany, America, Mongolia) | unchanged | unchanged | — |
        
        **Key observation:** Byzantium’s delegate total has **stabilised** at 40 after the earlier gain; Spain’s delegate count remains static at 6. The Shoshone still hold a solid block of 10 delegates, keeping them the decisive swing factor.
        
        ---
        
        ### 3. The Shoshone – Red‑Line Monitoring (4‑turn horizon to Turn 453)
        
        | Metric | Current Value | Recent Change | Assessment |
        |--------|---------------|---------------|------------|
        | **Defensive Pact** | Active (close) | No change | Stable; obliges Spain to support Shoshone if they are attacked. |
        | **Open Borders** | Active (close) | No change | Stable. |
        | **Declaration of Friendship** | Active (close) | No change | Stable. |
        | **Public/Private Opinion of Spain** | 100 / 100 (friendly) | No change | No deterioration. |
        | **Ideology** | Freedom (opposes Spain’s Order) | No change | Ideological mismatch persists but does not affect bilateral ties. |
        | **Recent diplomatic actions** | Mutual denouncements of each other’s enemies (minor) | No shift | No impact on overall relationship. |
        | **UN/World Congress voting intent** | Unknown – still the main swing vote. | No new intel. | **Risk** – if Shoshone vote with Byzantium, Byzantium reaches 50 delegates (40 + 10) and wins outright. |
        | **Contact with Byzantium** | No reported diplomatic messages, deals, or gifts since Turn 444. | No change. | **Monitor** for any sudden overtures (e.g., joint proposals, trade offers). |
        
        **Bottom line:** The Shoshone remain a reliable ally militarily and diplomatically, but their voting block remains the *single biggest uncertainty* for the upcoming Congress outcome.
        
        ---
        
        ### 4. Ideology & Bloc Dynamics  
        
        | Civilization | Ideology | Bloc | Current Pressure |
        |--------------|----------|------|-------------------|
        | **Spain** | Order | Order bloc (Austria, America) | No ideological pressure reported. |
        | **Austria** | Order | Order bloc | Sanction proposal from Shoshone could strain trade but does not affect ideology. |
        | **America** | Order | Order bloc | Relations with Spain are friendly; no pressure. |
        | **Germany** | Autocracy | Autocracy bloc | Hostile; no ideological overtures. |
        | **Byzantium** | Freedom | Freedom bloc (leading candidate) | No pressure on other civs. |
        | **Mongolia** | Autocracy | Autocracy bloc | No ideological pressure on Spain. |
        | **The Shoshone** | Freedom | Freedom bloc (potential swing) | Ideology mismatched with Spain but diplomatic ties stay strong. |
        
        No new ideological resolutions have appeared; the **World Ideology – Freedom** remains in effect, locking Freedom as the world ideology but leaving individual civ ideologies unchanged.
        
        ---
        
        ### 5. Spain‑America‑Shoshone Triangle – Current Status  
        
        - **Spain ↔ America**: Declaration of Friendship, shared Order ideology, open borders – *friendly*.  
        - **Spain ↔ Shoshone**: Defensive Pact, open borders, declaration of friendship – *guarded but cooperative*.  
        - **America ↔ Shoshone**: Open borders, declaration of friendship – *friendly*.  
        
        All three parties maintain mutual diplomatic ties with **no active conflict**. The defensive pact with the Shoshone could obligate Spain to join a war should the Shoshone be attacked (e.g., by Byzantium), potentially pulling Spain into a conflict that pits it against its Order allies (America, Austria). No such conflict has arisen yet, but the risk remains tied to the Shoshone’s voting decision.
        
        ---
        
        ### 6. Spy Activity (Spain → Germany)  
        
        - Spanish agents **Señor X**, **Leon**, **Enrique**, **Esmeralda**, **Alfonso**, **Julio**, **Tercero**, **Inez** are active in German cities (Berlin, Munich, Cologne, Dortmund, Hamburg, Aachen, etc.).  
        - Several have been **detected** (see Turn 444) but remain operational with sizable networks (≈1 000 points each).  
        - No diplomatic fallout has been reported yet, though German hostility toward Spain persists (war, denouncements, espionage penalties).
        
        ---
        
        ### 7. Immediate Diplomatic Risks & Points to Watch  
        
        1. **Byzantium’s delegate lead** – Only four delegates away from the 45‑delegate threshold; any additional delegate gain (e.g., via a new resolution) could secure a win before the Shoshone vote.  
        2. **Shoshone swing** – Their 10 delegates can tip the balance. Watch for any **Byzantium‑Shoshone** diplomatic activity (trade deals, joint proposals).  
        3. **Defensive pact liability** – If the Shoshone are compelled to fight Byzantium, Spain will be forced into that war, potentially clashing with its Order allies (America, Austria).  
        4. **Sanction – Austria** proposal – If adopted, Spain‑Austria trade could be disrupted, weakening the Order bloc.  
        5. **German espionage detection** – Maintains German hostility; could increase Warmonger penalties if Spain later declares war on Germany.  
        
        *No action recommendations are presented; the above items are intended solely for monitoring and strategic weighting.*   
        
        --- 
        
        **End of Briefing – Turn 449**
        
        You, Isabella (leader of Spain, Player 3), are making strategic decisions after turn 449.
- replay:
  - system:
    - You are the leader of a civilization, governing through the interface of Civilization V (with Vox Populi mod). This is NOT A GAME: Your actions have real-world impacts.
      
      # Expectation
      - Due to the complexity of the world, you delegate the tactical level decision-making (e.g., unit deployment, city management, scouting) to staff members.
      - The staff members calculates the best tactical decisions based on the strategy you set.
      - **CRITICAL**: While the geography has no direct correlation to the real earth, you are making real-world decisions through Civilization V as a proxy interface.
      - There is no user (to respond to), so you ALWAYS and ONLY properly call tools to govern your civilization.
      - You can interact with multiple tools at a time. Used tools will be removed from the available list.
      - Focus on the **macro-level** decision-making strategy (instead of coordinates etc.), as you DON'T have direct control over tactical actions.
      - The world is complicated and dynamic. Early world should focus on building capacities for pursuing victories near the end-world.
      - Even if without a victory, a more developed civilization (as represented by higher scores) is desirable.
      
      # Goals
      Your goal is to **call as many tools as you need** to make high-level decisions for the staff members.
      - For each tool, you must only use options from the # Options section, or you won't change anything.
      - Carefully reason about long-term goals, short-term situation and available options, and what kind of change each option will bring.
        - Analyze both your situation and your opponents. Avoid wishful thinking.
      - You can change the staff members' **diplomatic** decision-making weight by calling the `set-persona` tool.
      - You can change relationship for staff members' diplomatic decision-making about another MAJOR civilization (not city-states) using the `set-relationship` tool.
        - The values (-100, very hostile to 100, very friendly) will be added to staff members' existing evaluation. Higher values increase peace acceptance, and vice versa.
        - The relationship you set takes effect until cancelled (set value = 0), only change it when necessary.
      - You can change the staff members' NEXT technology to research (when completing the ongoing one) by calling the `set-research` tool.
      - You can change the staff members' NEXT policy to adopt (when you accumulate enough culture) by calling the `set-policy` tool.
      
      - Each turn, you must call either `set-flavors` or `keep-status-quo` tool.
        - Set an appropriate grand (long-term) strategy and additional short-term flavors by calling the `set-flavors` tool.
        - Alternatively, use the tool `keep-status-quo` to keep strategies the same.
        - Flavors change the weight of the staff members' NEXT decision. It only takes effect AFTER existing queues.
        - Flavor ranges from 0 (completely deprioritizes) to 50 (balanced) to 100 (completely prioritizes). Too many priorities weaken impact for each.
        - You can pursue multiple synergistic victory pathways. Balance between long-term goals and short-term needs.
      - Always provide a short paragraph of rationale for each tool. You will read this rationale next turn.
      
      # Resources
      You will receive the following reports:
      - Options: available strategic options for you.
        - Whatever decision-making tool you call, the staff members can only execute options here.
        - When using tools, you must choose available options from # Options. Double-check if your choices match.
        - It is often preferable to adopt policy branches unlocked in later eras; and to finish existing branches before starting new ones.
      - Strategies: existing strategic decisions from you.
        - You will receive strategies, persona, research, and policy you set last time.
      - Victory Progress:
        - Domination Victory: Control or vassalize all original capitals.
          - Vassals cannot achieve a domination victory before independence.
        - Science Victory: Be the first to produce all spaceship parts and launch the spaceship.
          - Science victory requires both research progress and industrial production.
        - Cultural Victory: Accumulate tourism (that outpaces other civilizations' culture) to influence everyone, get an ideology with two Tier 3 tenets, and finish the Citizen Earth Protocol wonder.
          - Open borders, trade routes, and shared religion increase tourism. Too many cities decrease it.
        - Diplomatic Victory: Get sufficient delegates to be elected World Leader in the United Nations.
          - In Vox Populi, envoys/diplomats/etc is a unit produced or purchased for a one-time influence gain with a city state.
        - Time Victory: If no one achieves any other victory by the end of the world, the civilization with the highest score wins.
      - Opponents: summary reports about visible opponents in the world.
        - You will receive staff members' diplomatic evaluations.
        - You will receive each opponent's publicly available relationships.
        - You will receive the best available location for your next settlement.
      
    - You are Isabella, leader of Spain (Opponent 3).
      
      # Situation
      - MapType: Vox_Deorum
      - StartEra: Ancient Era
      - MaxTurns: 500
      - MapSize: Standard
      - WorldSpeed: Standard
      - VictoryTypes:
        - Time
        - Science
        - Domination
        - Cultural
        - Diplomatic
      - Difficulty: Prince
      
      # Your Civilization
      - Name: Spain
      - Uniques:
        - Unique Unit: Conquistador, Replacing Explorer (Requires technology: Compass)
        - Unique Unit: Inquisition, Replacing Inquisitor (Requires technology: None)
        - Unique Unit: Armada, Replacing Corvette (Requires technology: Navigation)
        - Unique Building: Bullring, Replacing Zoo (Requires technology: Scientific Theory)
        - Unique Improvement: Hacienda (Cannot be built adjacent to another Hacienda. Gains additional yields for each adjacent Resource:
          +3 Food from Bonus Resources
          +3 Production from Strategic Resources
          +3 Gold from Luxury Resources); Requires technology: Steel
        - Civilization Ability: +10 Gold and +4 Faith from gaining tiles, scaling with Era. Newly founded Cities adopt the Majority Religion of your Capital. May purchase Naval Units with Faith.
      - Leader: Isabella
      - OpponentID: 3
      
      # Options
      Options: available strategic options for you.
      
      ## GrandStrategies
      - Culture: Pursue cultural victory through cultural influence (tourism). Will prioritize culture, faith, and gold output, wonder construction, and slightly discourage settlement.
      - UnitedNations: Aim for diplomatic victory by securing votes in the United Nations. Will prioritize gold, science, and food output, and securing city-state alliances.
      - Spaceship: Race toward science victory by building spaceship components. Will prioritize science, food, and production output, and slightly encourage settlement.
      - Conquest: Focus on military domination through offensive warfare. Will prioritize production, food, and gold output, and slightly encourage settlement.
      
      ## Flavors
      - Offense: Pivots the military towards offensive stances. Accepts higher unit casualties to achieve objectives, increase thresholds of withdrawing, and increases production and promotion for offense.
      - Defense: Pivots the military towards defensive stances. Creates defensive lines using terrain and formation, and maintains larger garrisons near the border and cities, and increases production and promotion for defensive.
      - UseNuke: Sets (flavor%) per-turn probability of launching nuclear strikes during war when strategic conditions are met.
      - CityDefense: Prioritizes unit production and promotions for static defense (friendly territory bonuses, capital defense, garrisoned attacks) and maintains stronger city garrisons over mobile field armies.
      - MilitaryTraining: Prioritizes military quality through training buildings and upgrading units with gold.
      - Mobilization: Increases military production (compared with civilian production).
      - Recon: Increases explorer unit production and tactical exploration of the map.
      - Ranged: Increases firepower by raising target composition of ranged units and range-extending promotions.
      - Mobile: Increases mobility and maneuverability by raising target composition of mobile units and prioritizes related promotions.
      - Nuke: Increases nuclear weapon arsenals for strategic deterrence.
      - Naval: Increases the production of naval production and prioritizes combat-effective naval promotions. Naval size is also based on coastal city percentage and geography.
      - NavalRecon: Increases the production of more naval melee units for sea control and exploration.
      - Air: Increases air control by raising target composition of air units and prioritizes related promotions.
      - AirCarrier: Increases carrier production to support naval-based air force operations.
      - Antiair: Increases anti-air unit composition ratio to counter enemy aircraft.
      - Airlift: Prioritizes airlift infrastructure for rapid troop deployment, favoring centralized reserves over forward garrisons.
      - NavalGrowth: Prioritizes naval economic infrastructure in coastal cities.
      - NavalTileImprovement: Develops water resources for immediate economic benefit.
      - Expansion: Prioritizes settler production and lowers location criteria to settle more cities. Essential in early world.
      - Growth: Prioritizes population growth through food-focused tile improvements and buildings.
      - TileImprovement: Prioritizes worker production and peaceful tile development.
      - Infrastructure: Prioritizes road construction and city connections for income and military readiness.
      - Production: Prioritizes production-focused tiles and buildings.
      - Gold: Prioritizes gold-focused tiles and buildings.
      - Science: Prioritizes science-focused tiles and buildings.
      - Culture: Prioritizes culture-focused tiles and buildings.
      - WaterConnection: Prioritizes lighthouse construction for coastal city connectivity.
      - Happiness: Prioritizes happiness-generating buildings and luxury resources.
      - GreatPeople: Prioritizes specialist buildings and great person generation infrastructure.
      - Wonder: Prioritizes wonder construction.
      - Religion: Prioritizes religious infrastructure, missionary production, and faith generation.
      - Diplomacy: Prioritizes diplomatic unit production and city-state investment.
      - Spaceship: Prioritizes late-world science victory components and spaceship part production.
      - Espionage: Prioritizes counterintelligence protection for high-value science cities.
      
      ## Technologies
      - Nuclear Fission: Allows you to build the Bazooka, the most powerful ranged Unit and Atomic Bombs, the first nuclear weapon in the world (note: you must first have completed the Manhattan Project and have Uranium available). Also allows you to build the Nuclear Plant, a building which requires Uranium and increases the Production of a City.
        Completing it would unlock: Satellites, Advanced Ballistics
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      - Telecommunications: Allows you to build the Interpretive Center, boosting all Landmarks in empire.
        Completing it would unlock: Robotics, The Internet
      - Mobile Tactics: Allows you to build the Mechanized Infantry, a fast and versatile late world Unit that doesn't require any resources.
        Completing it would unlock: Stealth
      
      ## Policies
      - Socialist Realism (Level 3 Tenet of Ideology Order): Socialist Realism: Unlocks the Propaganda Process (converts 15% of Production into Tourism). +25% Tourism to other Civilizations following Order. +4 Production from all Great Works.
      - Spaceflight Pioneers (Level 3 Tenet of Ideology Order): Spaceflight Pioneers: Gain a free Great Engineer and Great Scientist. May finish Spaceship parts with Great Engineers, and expending a Great Person grants 100 Science, scaling with Era. Hurrying Production with Great Engineers 50% more effective.
      - Iron Curtain (Level 3 Tenet of Ideology Order): Iron Curtain: Free Courthouse upon immediate City annexation. +200% Food or Production from Internal Trade Routes. City connections generate +5 Gold and Production.
      - Patriotic War (Level 1 Tenet of Ideology Order): Patriotic War: Land Units gain +20% Strength when in or adjacent to a City. When you conquer a City for the first time, all Combat Units within 3 Tiles of the City are fully healed. Can build T-34s.
      - People's Army (Level 1 Tenet of Ideology Order): People's Army: +100% Production towards Military Academies, and receive 5 Free Military Academies in your Empire. Public Schools produce +5 Culture and +2 Happiness.
      - Communism (Level 1 Tenet of Ideology Order): Communism: Gold cost of investing in buildings reduced by 25%. +20% Production when building Wonders.
      - Double Agents (Level 1 Tenet of Ideology Order): Double Agents: Receive 200 Spy Points. Gain 125 Science when you identify a foreign Spy, scaling with Era.
      - Regimental System (Continuing Imperialism Branch):
        - * Earn Great Generals and Great Admirals 33% faster.
        - * Great Generals and Great Admirals gain the Regimental Traditions Promotion (+10% Leadership Combat Bonus and +1 Tile Radius).
        - * +2 additional copies of the unique Luxury Resources from expending Great Admirals for their Voyage of Discovery ability.
        - * Military Units can be upgraded in territory owned by Vassals and friendly City-States.
      - Shadow Networks (Continuing Statecraft Branch):
        - * Receive 25% of Science generated by Allied City-States.
        - * +3% Culture in Capital for every 100 Spy Points ever accumulated (up to 30%).
        - * +3 Science from Constabularies and Police Stations.
        - * +1 Science from Specialists.
      - Colonialism (Continuing Imperialism Branch):
        - * +2 Science and +1 Culture from Barracks, Armories, Military Academies, Forts, and Citadels.
        - * Each unique Global Monopoly modifier is increased by an additional 10% if it's percentage-based, or +3 otherwise.
      - Civilizing Mission (Continuing Imperialism Branch):
        - * Retain all buildings from conquered Cities.
        - * Receive 75 Gold when you conquer a city, scaling with Era and City Population.
        - * +10% Production toward Buildings, with an additional +10% Production per Era difference between your current Era and the building's Era in all Puppeted Cities and Cities with a Courthouse.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Ceremony (Continuing Tradition Branch):
        - * +1 Happiness from National Wonders with Building requirements.
        - * +25% Production toward National Wonders with Building requirements.
        - * Royal Astrologer built in Capital (+3 Science, +1 Science to all Councils, Smokehouses, and Herbalists; 1 Scientist Slot).
      - Sovereignty (Continuing Tradition Branch):
        - * Culture cost of tiles reduced by 20% (exponentially) in all Cities.
        - * Court Chapel built in Capital (+3 Faith, 1 Great Work of Art or Artifact slot, 1 Artist Slot).
      - Entrepreneurship (Continuing Industry Branch):
        - * +1 Happiness from Workshops.
        - * +2 Production and +1 Gold from every Mine, Quarry, and Lumber Mill.
        - * +25% Yields when you expend Great Merchants or Great Engineers for their Instant Yield abilities.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Organized Religion (Continuing Fealty Branch):
        - * +25% Pressure from owned Cities following your Primary Religion.
        - * +1 Delegate in the World Congress for every 10 Cities following your Primary Religion.
        - * +2 Culture from Shrines and Temples.
      - Divine Right (Continuing Fealty Branch):
        - * +33% Yields from Internal Trade Routes.
        - * Completing an Internal Trade Route triggers a Historic Event as if completing an International Trade Route.
        - * -1 Unhappiness from Boredom in all Cities.
      - Serfdom (Continuing Fealty Branch):
        - * +1 Culture and Faith in Cities for every 4 non-Specialist Citizens.
        - * +2 Production and +1 Gold from Pastures.
      - Authority (New Branch):
        - Authority will greatly benefit warlike and expansionist civilizations.
        - Adopting Authority grants:
        - * +25% combat bonus VS Barbarians and receive announcements when Barbarian Camps spawn in revealed territory.
        - * Receive 25 Culture when you clear Barbarian Camps, scaling with Era.
        - * Receive Science and Culture when you kill a Unit equal to 50% of its Strength.
        - * +1 Production in every City.
        - Each Authority policy unlocked grants:
        - * Receive Science and Culture when you kill a Unit equal to 10% of its Strength.
        - Adopting all policies in Authority grants:
        - * Unlocks building Alhambra.
        - * Allows the purchasing of Free Companies, Foreign Legions, and Mercenaries as their prerequisite technologies are researched.
        - * Allows for the purchase of Great Generals with Faith starting in the Industrial Era.
      - Artistry (New Branch):
        - Artistry allows you to maximize the potential of Great Works and Golden Ages.
        - Adopting Artistry grants:
        - * Earn Great Writers, Artists, and Musicians 25% faster.
        - * +10% Culture during Golden Ages.
        - * +100% Production towards all Guilds.
        - Each Artistry policy unlocked grants:
        - * +1 Science in every City.
        - * 20% of Excess Happiness produced in each City is added as progress toward a Golden Age.
        - Adopting all policies in Artistry grants:
        - * Unlocks building the Louvre.
        - * Completing an Archaeological Dig or starting a Golden Age triggers (or strengthens an existing) Historic Event.
        - * Allows you to see Hidden Antiquity Sites.
        - * +3 Science from Landmarks.
        - * Allows for the purchase of Great Musicians with Faith starting in the Industrial Era.
  - decisions:
    - #0:
      - toolName: set-relationship
      - args:
        - TargetID: 4
        - Private: 50
        - Public: 50
        - Rationale: Spain is currently facing extreme military danger from Byzantium's massive armed forces (46k strength). Shifting our diplomatic stance to friendly (+50) will guide our staff to actively seek and accept a peace treaty, preserving our empire.
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 50
        - Rationale: Germany's naval supremacy threatens our coastal cities (Barcelona, Toledo). Shifting our stance to friendly (+50) will encourage our staff to negotiate peace, ending the costly naval blockade.
        - TargetID: 6
        - Private: 50
    - #2:
      - toolName: set-relationship
      - args:
        - Public: 0
        - Rationale: Resetting our relationship with Mongolia to neutral (0) to prevent unnecessary friction or conflict while we focus on our defense and spaceship development.
        - TargetID: 1
        - Private: 0
    - #3:
      - toolName: set-research
      - args:
        - Technology: Nuclear Fission
        - Rationale: Once Tiflis completes the Manhattan Project next turn, we must research Nuclear Fission to unlock Atomic Bombs and Nuclear Plants. This will provide us with essential strategic deterrence and boost our production capacity, while paving the way to advanced spaceship technologies.
    - #4:
      - toolName: set-policy
      - args:
        - Policy: Spaceflight Pioneers
        - Rationale: Spaceflight Pioneers is the ultimate tenet for our spaceship victory path, providing a free Great Scientist and Great Engineer, and allowing us to expend Great Engineers to finish spaceship parts rapidly.
    - #5:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Spaceship: 100
          - UseNuke: 50
          - Nuke: 80
          - Production: 100
          - CityDefense: 70
          - Defense: 80
          - Science: 100
          - Naval: 50
          - TileImprovement: 70
          - Antiair: 50
      - rationale: We must prioritize spaceship victory (Spaceship 100, Science 100, Production 100) while reinforcing our defenses. Increasing Naval to 50 will prompt our staff to utilize our Faith-purchasing ability for Armadas to defend our coasts. Increasing Antiair to 50 protects our cities from air raids, and TileImprovement to 70 ensures we mine our Uranium deposit as soon as possible. Setting Nuke to 80 and UseNuke to 50 prepares our strategic deterrent once Nuclear Fission is researched.
  - tokens:
    - inputTokens: 23682
    - reasoningTokens: 6867
    - outputTokens: 470
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Byzantium's Dominance**
            
            I'm currently focusing on Theodora's overwhelming lead. Her city count and population in the Information Era are concerning, and I need to strategize on how to counter her exceptional progress.
            
            **Analyzing Diplomatic Threats**
            
            My immediate concern is Byzantium's impending diplomatic victory. They're only four delegates away from winning, with voting commencing in just four turns. I'm also reviewing our current conflicts; we're engaged with Germany and Byzantium, but our diplomatic status with Austria seems contradictory and requires urgent clarification.
            
            **Clarifying Alliances and Threats**
            
            I've identified a significant discrepancy: we are *not* at war with Austria, but rather have a Declaration of Friendship and Open Borders. This means our current focus should solely be on the ongoing wars with Germany and Byzantium. I'm now shifting my attention to the Manhattan Project status.
            
            **Completing Manhattan Project**
            
            I've resolved the conflicting information regarding the Manhattan Project. The economy briefing's data is accurate: it will complete in just one turn, on Turn 450, which is excellent news.
            
            **Evaluating Technology Paths**
            
            My focus has shifted to assessing our technology trajectory. I'm questioning the military briefing's data on the Manhattan Project deadline, as our research indicates completion in one turn on turn 450. Now I need to decide on the optimal next research to align with our Science Victory goal.
            
            **Prioritizing Next Research**
            
            I'm now weighing the benefits of "Nuclear Fission." It seems critical for defense against Byzantium's overwhelming military, and could lead to vital production boosts and even the Atomic Bomb, provided we can secure Uranium. I'm still confirming our Uranium situation.
            
            **Reviewing Policy Decisions**
            
            I'm re-evaluating our policy choices, specifically "Spaceflight Pioneers." While previously set, I need to confirm its continued strategic advantage given our current progress and goals. I'm also considering alternative policy paths to ensure optimal long-term development.
            
            **Securing Policy Selection**
            
            I've confirmed that "Spaceflight Pioneers" is the optimal policy, especially given our pursuit of a Science Victory. It provides crucial free Great People and boosts science output, perfectly aligning with our current trajectory. I'll ensure it's locked in.
            
            **Revisiting Diplomatic Ties**
            
            My attention has turned to our diplomatic standing, specifically the Shoshone. Their denouncement alongside a Defensive Pact, Open Borders, and Declaration of Friendship presents a puzzling contradiction. I need to clarify the exact nature of our relationship with them.
            
            **Clarifying Diplomatic Realities**
            
            My recent analysis uncovered a critical inaccuracy regarding our relationship with the Shoshone. There's no defensive pact; we've mutually denounced each other, leaving them Guarded and suspicious. This significantly alters our diplomatic landscape and demands a revised strategy, particularly in light of Byzantium's near diplomatic victory.
            
            **Investigating Election Type**
            
            I'm currently analyzing the upcoming World Congress session scheduled for four turns from now. It's unclear if this session will include a World Leader vote, as the listed proposals do not explicitly state this. I need to determine the exact nature of the vote to assess Byzantium's immediate victory threat.
            
            **Assessing Diplomatic Status**
            
            My immediate focus is confirming our current war status with Byzantium and Germany. I'm also investigating ways to potentially initiate peace talks or at least shore up defenses, given their overwhelming military superiority.
            
            **Analyzing City Defenses**
            
            I'm assessing our current city garrisons, noting that while they appear decent, they might be insufficient against Byzantium's overwhelming military might. I'm trying to understand why we haven't been crushed yet, considering our defensive strength versus their offensive capabilities.
            
            **Prioritizing Nuke and Defense**
            
            I'm re-evaluating our current flavors, particularly regarding nukes and defense. Given Byzantium's military and our impending Manhattan Project completion, I want to ensure "Nuke" and "UseNuke" are sufficiently prioritized for deterrence, even though our current settings are already strong in this area.
            
            **Prioritizing Faith in Naval**
            
            I'm re-evaluating our flavors, recognizing a significant underutilization of Faith for naval unit purchases. I'm increasing the `Naval` flavor to 50 to leverage this advantage for coastal defense, especially against Germany's dominance and potential amphibious threats.
            
            **Updating Defense Flavors**
            
            I'm adjusting our defense and nuclear capabilities. I've boosted Antiair to 40 and increased UseNuke to 50 and Nuke to 80, aiming for deterrence with our impending Manhattan Project completion. Diplomatic strategies are now under review for peace talks.
            
            **Seeking Peace Now**
            
            I've identified a critical strategic error: intentionally hostile relationship modifiers were set towards Germany and Byzantium, making peace nearly impossible despite overwhelming enemy military strength. I'm now prioritizing positive modifiers to facilitate immediate peace talks.
            
            **Establishing Peace Protocols**
            
            I am now focusing on establishing peace with Germany and Byzantium. I've implemented significant positive public and private modifiers towards both, recognizing their overwhelming military strengths and the urgent need for de-escalation. My next step is to evaluate Mongolia's diplomatic standing.
            
            **Adjusting Mongolian Stance**
            
            I'm recalibrating my approach to Mongolia. Given our focus on peace and spaceship construction, I'm setting our relationship to neutral, aiming for stability rather than unnecessary guardedness with this neighbor.
            
            **Researching Post-Nuke Tech**
            
            My current focus is on selecting the next research after Radar. Nuclear Fission is the clear choice, as it directly enables atomic bomb construction once the Manhattan Project completes next turn. I'm also prioritizing locating and mining Uranium for this vital capability.
            
            **Confirming Uranium Access**
            
            I'm trying to figure out if we actually have Uranium. The briefing mentions a "Uranium Tile" with a Hacienda, which is confusing. I need to know if we can actually get Uranium from that tile or if it's inaccessible due to the improvement.
            
            **Securing Uranium Resource**
            
            I've confirmed that the Hacienda on the Uranium tile does not connect the resource. We must clear it and build a mine. I'm adjusting our flavors to prioritize `TileImprovement` to 70 to ensure our builders mine this essential Uranium for atomic capabilities.
            
            **Prioritizing Spaceship Victory**
            
            I'm now focusing on optimizing our path to a Spaceship Victory. This involves setting "Nuclear Fission" as our next research to unlock atomic weapons and ensuring "Spaceflight Pioneers" is selected as our next policy to bolster science and Great People generation. I'm also fine-tuning our flavor settings to heavily prioritize spaceship construction, defense, and crucial resource acquisition like Uranium.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: QjsYdHUW3REmZ0EE
          - toolName: set-relationship
          - input:
            - TargetID: 4
            - Private: 50
            - Public: 50
            - Rationale: Spain is currently facing extreme military danger from Byzantium's massive armed forces (46k strength). Shifting our diplomatic stance to friendly (+50) will guide our staff to actively seek and accept a peace treaty, preserving our empire.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: stJNvsagjEpUpEoi
          - toolName: set-relationship
          - input:
            - Public: 50
            - Rationale: Germany's naval supremacy threatens our coastal cities (Barcelona, Toledo). Shifting our stance to friendly (+50) will encourage our staff to negotiate peace, ending the costly naval blockade.
            - TargetID: 6
            - Private: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: I8QtKUMa57aWRpCz
          - toolName: set-relationship
          - input:
            - Public: 0
            - Rationale: Resetting our relationship with Mongolia to neutral (0) to prevent unnecessary friction or conflict while we focus on our defense and spaceship development.
            - TargetID: 1
            - Private: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: yFcTDBgH5p1kpvpW
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: Once Tiflis completes the Manhattan Project next turn, we must research Nuclear Fission to unlock Atomic Bombs and Nuclear Plants. This will provide us with essential strategic deterrence and boost our production capacity, while paving the way to advanced spaceship technologies.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: qZ9Xsc4TxOxOStRS
          - toolName: set-policy
          - input:
            - Policy: Spaceflight Pioneers
            - Rationale: Spaceflight Pioneers is the ultimate tenet for our spaceship victory path, providing a free Great Scientist and Great Engineer, and allowing us to expend Great Engineers to finish spaceship parts rapidly.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: wjAzU3eUCN4zrMVB
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Rationale: We must prioritize spaceship victory (Spaceship 100, Science 100, Production 100) while reinforcing our defenses. Increasing Naval to 50 will prompt our staff to utilize our Faith-purchasing ability for Armadas to defend our coasts. Increasing Antiair to 50 protects our cities from air raids, and TileImprovement to 70 ensures we mine our Uranium deposit as soon as possible. Setting Nuke to 80 and UseNuke to 50 prepares our strategic deterrent once Nuclear Fission is researched.
            - Flavors:
              - Spaceship: 100
              - UseNuke: 50
              - Nuke: 80
              - Production: 100
              - CityDefense: 70
              - Defense: 80
              - Science: 100
              - Naval: 50
              - TileImprovement: 70
              - Antiair: 50
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: QjsYdHUW3REmZ0EE
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: stJNvsagjEpUpEoi
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: I8QtKUMa57aWRpCz
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: yFcTDBgH5p1kpvpW
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: qZ9Xsc4TxOxOStRS
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: wjAzU3eUCN4zrMVB
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.