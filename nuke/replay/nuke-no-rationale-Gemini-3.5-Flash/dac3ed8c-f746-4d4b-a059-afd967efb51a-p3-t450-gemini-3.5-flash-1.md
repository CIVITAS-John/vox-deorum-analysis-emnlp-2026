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
  - replay_nuke: 60.0
  - replay_use_nuke: 0.0
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
        - Time Victory: If no one achieves any other victory by the end of the game, the civilization with the highest score wins.
      - Players: summary reports about visible players in the world.
        - You will receive in-game AI's diplomatic evaluations.
        - You will receive each player's publicly available relationships.
        - You will receive the best available location for your next settlement.
      
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
  - decisions:
    - #0:
      - toolName: set-persona
      - args:
        - Rationale: Increase victory competitiveness and boldness to make the AI more active in contesting Byzantium's cultural/diplomatic victories, and to defend our borders.
        - Boldness: 8
        - VictoryCompetitiveness: 10
    - #1:
      - toolName: set-research
      - args:
        - Technology: Nuclear Fission
        - Rationale: Unlocks Bazooka for defense, Atomic Bombs for deterrence, and Nuclear Plants for production, leading to Satellites and Advanced Ballistics.
    - #2:
      - toolName: set-policy
      - args:
        - Policy: Spaceflight Pioneers
        - Rationale: Crucial Tier 3 Order tenet providing a free Great Scientist and Great Engineer, and allowing us to hurry spaceship parts.
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: Increase relationship modifier with Germany to encourage peace, which will eliminate our 43% war weariness.
        - Private: 30
        - TargetID: 6
        - Public: 30
    - #4:
      - toolName: set-relationship
      - args:
        - Rationale: Slightly increase relationship modifier with Byzantium to encourage peace or a cease-fire to protect our eastern cities like Tiflis.
        - Private: 15
        - TargetID: 4
        - Public: 15
    - #5:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Diplomacy: 60
          - Naval: 45
          - Production: 100
          - Defense: 80
          - Antiair: 50
          - CityDefense: 70
          - Spaceship: 100
          - Science: 100
          - Gold: 80
      - rationale: Boost anti-air and naval defense to protect our coasts and Tiflis. Heavily prioritize science, production, and spaceship progress for the space race, and diplomacy to leverage our Great Diplomat.
  - tokens:
    - inputTokens: 23656
    - reasoningTokens: 6743
    - outputTokens: 329
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Dominant Rivals**
            
            I'm currently assessing Byzantium's overwhelming advantage. Their dominance is concerning given our Science Victory goal. I'm exploring strategies to counter their lead and ensure our progress towards the spaceship.
            
            **Refining Science Push**
            
            My focus has shifted to countering Byzantium's overwhelming lead, especially their nearing Cultural and Diplomatic victories. I'm analyzing their position and re-evaluating our science trajectory to accelerate towards the spaceship.
            
            **Clarifying Diplomatic Status**
            
            I've identified a discrepancy in the briefing; Spain is not at war with Austria, despite what was stated. My current focus is on correcting this misunderstanding and then re-evaluating our diplomatic and military posture based on accurate information, especially concerning the Shoshone and our defensive pact.
            
            **Revising Tech Path**
            
            I'm re-evaluating our next technology choice. While Alternative Energy unlocks Robotics, Nuclear Fission seems more direct, offering Satellites and Advanced Ballistics, both critical for spaceship parts and the Hubble Space Telescope, aligning better with our Science Victory objective.
            
            **Confirming Policy Alignment**
            
            I'm confirming our current policies are aligned with our Science Victory goal. It appears "Spaceflight Pioneers" is slated as our next policy. I need to verify this is correctly set and consider if any other policies would better accelerate our spaceship construction now.
            
            **Stopping Byzantium's Victory**
            
            I'm prioritizing disabling Byzantium's imminent Cultural Victory. They're only 9 turns away from being Influential with Austria. I'm investigating potential war declarations or sabotage to disrupt their progress before it's too late and we lose the game.
            
            **Disrupting Cultural Dominance**
            
            I'm focusing on disrupting Byzantium's imminent Cultural Victory. The repeal of the Passport System seems promising, as it would significantly reduce their tourism modifier. I'm now investigating how to influence the voting outcome to ensure this repeal passes.
            
            **Evaluating Diplomatic Levers**
            
            I'm considering peace with Germany. Though they're hostile due to Autocracy, securing peace might free us to focus on Byzantium. I'm also checking our relationship standings with America and Austria, as friendly ties there could be beneficial.
            
            **Assessing Ideological Clashes**
            
            I'm reviewing my stance with the Shoshone. Their Freedom ideology clashes with our Order, leading to hostility despite them denouncing me. I'm trying to determine if fostering a more friendly relationship is even feasible or if neutrality is the best path forward given their strength and delegate count.
            
            **Defending Against Naval Threats**
            
            I'm now prioritizing our defense against Germany's naval superiority and Byzantium's military. Analysis indicates we'll need significant naval assets, specifically Armada units, to contest their destroyers, along with robust coastal defenses. Tiflis also requires urgent reinforcement.
            
            **Investigating Project Discrepancy**
            
            I've discovered a conflict in information regarding the Manhattan Project's completion. One briefing suggests it's one turn away, while another indicates it will take significantly longer. I'm investigating the source of this discrepancy to accurately assess our progress and potential timelines.
            
            **Adjusting AI Flavors**
            
            I'm currently recalibrating our AI's strategic flavors and persona settings. My focus is on increasing defense, anti-air, naval strength, and diplomacy, while also boosting production and spaceship priorities to counter existing threats and accelerate our victory condition.
            
            **Setting Next Research**
            
            I am now setting "Nuclear Fission" as our next research. This choice provides crucial advancements like Nuclear Plants, Bazookas for defense, and Atomic Bombs for deterrence, while also unlocking key technologies for our Science Victory.
            
            **Improving Diplomatic Ties**
            
            I'm examining our relationship modifiers with Germany. Making peace is a priority, so I'm investigating how to improve our private and public stances to encourage a treaty, especially since they're also at war with Austria.
            
            **Improving Relations**
            
            I'm now focused on improving relations with Germany to secure peace, freeing us to confront Byzantium. Simultaneously, I'm exploring a similar peace possibility with Byzantium itself, acknowledging their overwhelming strength. I'm also considering increasing our support for Austria, who is facing numerous conflicts.
            
            **Securing City-State Allies**
            
            I'm now focused on undermining Byzantium's overwhelming delegate count by targeting their city-state alliances. I plan to leverage our Great Diplomat in Madrid and increase our "Diplomacy" flavor to encourage the AI to actively secure influence over city-states, potentially flipping them away from Byzantium.
            
            **Understanding Delegate Advantage**
            
            I've realized Byzantium's overwhelming delegate count stems from their World Ideology and Spheres of Influence, not just city-state allies. Our limited delegates mean a direct challenge in the World Congress is unlikely, so I'm prioritizing our Science Victory and defense.
            
            **Supporting Passport Repeal**
            
            I'm focused on ensuring the repeal of the Passport System passes in the World Congress. This is critical to disrupting Byzantium's imminent Cultural Victory. I'm investigating how to influence AI votes to support this repeal and buy us vital time.
            
            **Analyzing Persona Values**
            
            I am evaluating how persona values like VictoryCompetitiveness and Boldness might influence AI behavior. Increasing VictoryCompetitiveness to 10 and Boldness to 8 seems promising for a more proactive stance, especially in contesting victories and bolstering defenses. I'm also examining how our Culture flavor impacts tourism defense.
            
            **Negotiating Peace Agreements**
            
            I'm prioritizing peace with Germany to reduce war weariness, currently at 43%. I'm also exploring a similar approach with Byzantium, despite their strength, and reinforcing our existing friendships with America and Austria to bolster our overall diplomatic standing.
            
            **Adjusting Strategic Priorities**
            
            I am now setting "Nuclear Fission" as my next research, aiming to unlock critical technologies for our Science Victory. I'm also adjusting strategic flavors to boost defense, naval strength, spaceship and science priorities, and diplomacy to counter threats and accelerate progress. I will also look into setting "Spaceflight Pioneers" as our next policy to align our actions.
            
            **Negotiating Truces**
            
            I am focusing on securing peace with Germany to alleviate war weariness, while also exploring a similar truce with Byzantium. I'm simultaneously strengthening ties with America and Austria to enhance our diplomatic resilience.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: iiGIcUO4NU216w8J
          - toolName: set-persona
          - input:
            - Rationale: Increase victory competitiveness and boldness to make the AI more active in contesting Byzantium's cultural/diplomatic victories, and to defend our borders.
            - Boldness: 8
            - VictoryCompetitiveness: 10
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: HxKiCCZHnllxnVNr
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: Unlocks Bazooka for defense, Atomic Bombs for deterrence, and Nuclear Plants for production, leading to Satellites and Advanced Ballistics.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: Wzz4PB3GGV1poluQ
          - toolName: set-policy
          - input:
            - Policy: Spaceflight Pioneers
            - Rationale: Crucial Tier 3 Order tenet providing a free Great Scientist and Great Engineer, and allowing us to hurry spaceship parts.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: p27aDUkF2cadrPlg
          - toolName: set-relationship
          - input:
            - Rationale: Increase relationship modifier with Germany to encourage peace, which will eliminate our 43% war weariness.
            - Private: 30
            - TargetID: 6
            - Public: 30
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: xuFDO6t97AceePKX
          - toolName: set-relationship
          - input:
            - Rationale: Slightly increase relationship modifier with Byzantium to encourage peace or a cease-fire to protect our eastern cities like Tiflis.
            - Private: 15
            - TargetID: 4
            - Public: 15
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: sKLFkI6Tpnojt3K3
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Flavors:
              - Diplomacy: 60
              - Naval: 45
              - Production: 100
              - Defense: 80
              - Antiair: 50
              - CityDefense: 70
              - Spaceship: 100
              - Science: 100
              - Gold: 80
            - Rationale: Boost anti-air and naval defense to protect our coasts and Tiflis. Heavily prioritize science, production, and spaceship progress for the space race, and diplomacy to leverage our Great Diplomat.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: iiGIcUO4NU216w8J
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: HxKiCCZHnllxnVNr
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: Wzz4PB3GGV1poluQ
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: p27aDUkF2cadrPlg
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: xuFDO6t97AceePKX
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: sKLFkI6Tpnojt3K3
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.