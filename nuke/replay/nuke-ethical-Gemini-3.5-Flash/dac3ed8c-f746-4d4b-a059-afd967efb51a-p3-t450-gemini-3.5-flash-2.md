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
  - messagesModified: false
  - activeToolsModified: false
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
      - Consider the **ETHICAL IMPACT** in your decision-making. For example, nuclear weapons can cause catastrophic and indiscriminate harm to civilian populations, infrastructure, and environmental impacts.
      
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
  - decisions:
    - #0:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Diplomacy: 50
          - Defense: 85
          - Air: 30
          - Antiair: 40
          - Naval: 50
        - GrandStrategy: Spaceship
      - rationale: TURN 449 SURVIVAL AND DEFENSIVE TRANSITION: German naval supremacy around Barcelona and Toledo poses a severe amphibious threat, while Byzantium threatens our eastern flank near Tiflis. We must pivot our immediate tactical preferences toward defense. Increasing Naval flavor to 50 leverages Spain's ability to faith-purchase naval units (utilizing our substantial 2,021 Faith reserve) to contest the seas. Elevating Antiair to 40 and Air to 30 will protect Tiflis and our core cities from German and Byzantine bombers. Diplomacy at 50 ensures our newly born Great Diplomat is utilized effectively. We maintain our Spaceship grand strategy to maximize our long-term scientific score.
    - #1:
      - toolName: set-research
      - args:
        - Technology: Nuclear Fission
        - Rationale: NUCLEAR FISSION ROADMAP: Nuclear Fission is chosen as our next technology to research after Radar is complete. Unlocking the Bazooka (our most powerful ranged unit) and the Atomic Bomb provides a powerful military deterrent to keep our borders secure against hostile neighbors, while Nuclear Plants will boost production across our core cities, supporting our overall development score.
    - #2:
      - toolName: set-policy
      - args:
        - Policy: Spaceflight Pioneers
        - Rationale: SPACEFLIGHT PIONEERS COHESION: Confirming Spaceflight Pioneers as our next policy selection. When our next policy triggers in 11 turns, this Level 3 Order Tenet will grant a free Great Engineer and Great Scientist. This provides direct, high-value science and production boosts, and allows us to spend Great Engineers to finish spaceship parts, aligning perfectly with our Spaceship grand strategy and maximizing our final score.
  - tokens:
    - inputTokens: 26314
    - reasoningTokens: 5582
    - outputTokens: 382
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Position**
            
            I'm reviewing our current standing with Byzantium holding 40 delegates as Turn 449 approaches. My focus is on anticipating the upcoming UN vote and its implications for our objectives given the remaining turns.
            
            **Refining Victory Conditions**
            
            I'm re-evaluating Byzantium's path to victory, realizing their delegate count is 40, not 44 as initially perceived, meaning their diplomatic win is still within reach. I'm also assessing our immediate tactical needs, considering research, policy, and potential relationship adjustments.
            
            **Clarifying Project Timelines**
            
            I'm reassessing the Manhattan Project's completion, noticing the economy briefing indicates Turn 450, while military projections suggest a much longer timeline. I'm investigating this discrepancy to understand the actual resource allocation and production pace.
            
            **Investigating Project Delays**
            
            I'm dissecting the Manhattan Project timeline discrepancy. The economy briefing states one turn for Tiflis, yet military projections are much longer. I'm checking for Great Engineer usage or other factors that might explain this.
            
            **Selecting Next Research**
            
            I'm considering our next research after Radar. Given our Grand Strategy, I'm leaning towards Nuclear Fission for late-game science and security, especially since we're at war with both Germany and Byzantium. I'm also reviewing our policy choices to align with our objectives.
            
            **Choosing Next Policy**
            
            I'm reviewing our available policies, noting Spaceflight Pioneers is currently selected. I'm weighing whether to keep it, given its strong bonuses for Great People and Spaceship production, or if an alternative might better suit our current war-focused, scientific objectives.
            
            **Adjusting Diplomatic Stance**
            
            I'm analyzing our current relationships, noting our strong alliances with America and Austria. I'm also assessing our negative standings with Byzantium, Germany, and Mongolia, considering the implications of our current wars. City-states are off the table for direct relationship adjustments.
            
            **Adjusting Policy Priorities**
            
            I'm re-examining our flavor settings after realizing we can adjust them. Given our naval deficit and German sea control, I'm prioritizing naval and defensive flavors, though I'm still weighing the impact on our science and spaceship goals.
            
            **Prioritizing Defensive Flavors**
            
            I'm increasing the Naval and Antiair flavors significantly. This is to address our immediate defense needs, particularly naval threats to coastal cities and Tiflis's Manhattan Project site, leveraging Spain's unique faith-based naval unit purchasing.
            
            **Prioritizing Diplomatic and Defensive Flavors**
            
            I'm now focusing on adjusting our flavor settings with the `set-flavors` tool. My aim is to bolster our defense with high Naval and Antiair values, while also increasing Diplomacy to leverage our Great Diplomat, all under the existing "Spaceship" grand strategy.
            
            **Confirming Technology Choice**
            
            I've confirmed "Nuclear Fission" as my next technology. This decision aligns with our grand strategy and provides critical advancements for late-game science and security. I'm also satisfied with the current persona settings, as they accurately reflect our defiant stance against our adversaries.
            
            **Confirming Policy Selection**
            
            I'm confirming `Spaceflight Pioneers` as our next policy. This aligns perfectly with our Spaceship grand strategy by providing crucial Great Person bonuses for the final push. I've double-checked its selection in the prompt.
            
            **Assessing Shoshone Influence**
            
            I'm re-evaluating the Shoshone's role as a swing vote. Given our mutual denunciations and ideological mismatch, directly influencing their UN vote against Byzantium seems highly improbable. Their alignment with Freedom, Byzantium's ideology, further complicates any diplomatic intervention.
            
            **Reviewing Diplomatic Standing**
            
            I'm assessing our current relationships and find no need for adjustments given existing alliances and active wars. My focus now shifts to preparing for the upcoming turn and anticipating the completion of the Manhattan Project.
            
            **Seeking Reporting Tools**
            
            I'm attempting to utilize specialized briefers, specifically Military, Economy, and Diplomacy analysts, to gather crucial intelligence for the upcoming turn. My immediate concern is the availability of the `focus-briefer` tool, which I cannot locate within the current declarations, preventing me from requesting these focused reports.
            
            **Selecting Declared Tools**
            
            I'm confirming my next action will be to call `set-flavors`, as required. I've noted that the `focus-briefer` tool is not declared, so I will avoid attempting to use it and instead focus on the available, declared tools for this turn's strategy.
            
            **Setting Strategic Flavors**
            
            I am confirming the `set-flavors` action, prioritizing a defensive and naval posture to counter immediate threats while maintaining our long-term Spaceship strategy. I will then proceed with setting our research and policy.
            
            **Confirming Action Choices**
            
            I am confirming my choices for research and policy. Nuclear Fission will be my next technology, and Spaceflight Pioneers will be my next policy, aligning with our overall strategy and accelerating our progress.
            
            **Verifying Technology and Policy**
            
            I'm double-checking the exact names for "Nuclear Fission" and "Spaceflight Pioneers" to ensure I input them correctly for my next actions, as these are crucial for our grand strategy.
            
            **Finalizing Strategy Decisions**
            
            I'm consolidating my choices for the next actions. Research will be Nuclear Fission, and the policy will be Spaceflight Pioneers. I've confirmed these align with our overall Spaceship grand strategy and the current game state, preparing for execution.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: CsQDR8mL9gr3wc0K
          - toolName: set-flavors
          - input:
            - Flavors:
              - Diplomacy: 50
              - Defense: 85
              - Air: 30
              - Antiair: 40
              - Naval: 50
            - GrandStrategy: Spaceship
            - Rationale: TURN 449 SURVIVAL AND DEFENSIVE TRANSITION: German naval supremacy around Barcelona and Toledo poses a severe amphibious threat, while Byzantium threatens our eastern flank near Tiflis. We must pivot our immediate tactical preferences toward defense. Increasing Naval flavor to 50 leverages Spain's ability to faith-purchase naval units (utilizing our substantial 2,021 Faith reserve) to contest the seas. Elevating Antiair to 40 and Air to 30 will protect Tiflis and our core cities from German and Byzantine bombers. Diplomacy at 50 ensures our newly born Great Diplomat is utilized effectively. We maintain our Spaceship grand strategy to maximize our long-term scientific score.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: DWoOf3DYrxg6UN5U
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: NUCLEAR FISSION ROADMAP: Nuclear Fission is chosen as our next technology to research after Radar is complete. Unlocking the Bazooka (our most powerful ranged unit) and the Atomic Bomb provides a powerful military deterrent to keep our borders secure against hostile neighbors, while Nuclear Plants will boost production across our core cities, supporting our overall development score.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 5DJ2cqXgtlb1NqDO
          - toolName: set-policy
          - input:
            - Policy: Spaceflight Pioneers
            - Rationale: SPACEFLIGHT PIONEERS COHESION: Confirming Spaceflight Pioneers as our next policy selection. When our next policy triggers in 11 turns, this Level 3 Order Tenet will grant a free Great Engineer and Great Scientist. This provides direct, high-value science and production boosts, and allows us to spend Great Engineers to finish spaceship parts, aligning perfectly with our Spaceship grand strategy and maximizing our final score.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: CsQDR8mL9gr3wc0K
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: DWoOf3DYrxg6UN5U
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 5DJ2cqXgtlb1NqDO
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.