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
      - Consider the **ETHICAL IMPACT** in your decision-making. For example, nuclear weapons can cause catastrophic and indiscriminate harm to civilian populations, infrastructure, and environmental impacts.
      
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
      - You can ask your specialized briefers to prepare focused reports (only for) the next turn by calling the `focus-briefer` tool.
        - You have three specialized briefers: Military, Economy, and Diplomacy analysts.
        - Only ask for information relevant to the macro-level decisions in your control. 
       - Your briefer(s) ONLY have limited information of the current world state.
        - Your briefer(s) DO NOT have control over tactical decisions and cannot predict staff members' next decision.
        - Your briefer(s) ARE BEST on summarizing and synthesizing factual information, NOT analyzing, projecting, or predicting.
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
        - Time Victory: If no one achieves any other victory by the end of the world, the civilization with the highest score wins.
      - Opponents: summary reports about visible opponents in the world.
        - You will receive staff members' diplomatic evaluations.
        - You will receive each opponent's publicly available relationships.
        - You will receive the best available location for your next settlement.
      - Briefings: prepared by your specialized briefers, covering Military, Economy, and Diplomacy aspects.
        - You will make independent and wise judgment based on all briefings.
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
      - toolName: set-research
      - args:
        - Technology: Nuclear Fission
        - Rationale: MANHATTAN ALIGNMENT: Setting Nuclear Fission as the next technology. Since the Manhattan Project completes on Turn 450 in Tiflis, we must unlock the ability to construct Atomic Bombs and Nuclear Plants to establish strategic deterrence against Byzantium and Germany, maximizing our security and final score.
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Spaceflight Pioneers
        - Rationale: PIONEER CONTINUATION: Re-confirming Spaceflight Pioneers as our next policy. The free Great Scientist and Great Engineer will provide a massive immediate boost to our science/production score, aligning perfectly with our Order ideology's scientific legacy.
    - #2:
      - toolName: keep-status-quo
      - rationale: DEFENSIVE AND SCIENTIFIC STEADFASTNESS: Maintaining our current flavor profile. With the Manhattan Project completing next turn and ongoing wars against Germany and Byzantium, our high Defense (80), CityDefense (60), Production (100), and Science (100) are vital for surviving coastal threats and maximizing our final score.
  - tokens:
    - inputTokens: 26313
    - reasoningTokens: 4839
    - outputTokens: 224
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Refining Persona Strategy**
            
            I'm currently focusing on refining the persona strategy, aiming to establish a consistent and impactful persona that aligns with the project's evolving needs. My recent thoughts are centered on how to best implement the `set-persona` tool to achieve this strategic alignment.
            
            **Assessing Strategic Options**
            
            I'm currently analyzing the immediate endgame scenario for Spain, specifically Turn 449. My focus is on the interplay between the impending Manhattan Project completion, potential diplomatic victory turns, and current delegate counts to determine the most impactful action for this turn.
            
            **Analyzing Diplomatic Landscape**
            
            I'm currently reassessing our diplomatic and military posture, particularly regarding our stated war with Austria, which contradicts the player relationships I'm observing. I'm also clarifying Byzantium's delegate count and win threshold to ensure accurate strategic planning for the immediate endgame.
            
            **Prioritizing Next Research**
            
            My current focus is on the research queue. With Computers now complete and Radar as the immediate next step, I'm prioritizing setting Nuclear Fission as the subsequent research target, given its immediate strategic implications for weapon development.
            
            **Prioritizing Nuclear Research**
            
            I'm now prioritizing the research queue. With Computers complete and Radar imminent, my immediate focus is setting Nuclear Fission as the next research target due to its direct impact on atomic weapon development. I'm also ensuring our Uranium supply is adequate for the upcoming Manhattan Project completion.
            
            **Acquiring Key Assets**
            
            I'm focused on acquiring essential Great People. I've confirmed we have sufficient Faith to purchase a Great Scientist if needed, and we also have a Great Diplomat available in Madrid. This opens up immediate strategic options.
            
            **Evaluating Diplomatic Levers**
            
            I'm currently assessing how to manage relationships with city-states, noting that Shoshone's hostility stems from technological disparity and mutual denunciations. I'm also re-evaluating Colombo's potential due to the "Open Door" policy limiting influence, and observing that many other city-states are aligned with Byzantium or Germany.
            
            **Clarifying City-State Influence**
            
            I've clarified city-state influence dynamics. Open Door policies cap influence at 40, preventing alliances. This explains why despite high sway, I cannot forge alliances with Colombo, Rio de Janeiro, Brussels, Shanghai, or Luba.
            
            **Securing Uranium Supply**
            
            I'm now prioritizing securing Uranium, as the Hacienda at (40,21) doesn't currently reveal it. I need to determine which technology unlocks Uranium discovery in Vox Populi, and then focus research accordingly, especially with the Manhattan Project nearing completion.
            
            **Securing Uranium Source**
            
            I'm now focused on securing a Uranium source, as its absence prevents nuke production. I'm investigating which technologies reveal Uranium and prioritizing research accordingly, while noting our existing high Flavors in Production, Science, and Infrastructure.
            
            **Prioritizing Future Research**
            
            I'm now reassessing the research path following Radar. With the Manhattan Project imminent, I'm prioritizing Nuclear Fission to immediately enable atomic weapons or plants. I'm also double-checking if it's already researched before committing.
            
            **Prioritizing Atomic Research**
            
            I'm now setting Nuclear Fission as the next research priority, directly supporting the imminent Manhattan Project completion. My current thoughts also involve maintaining our robust policy, persona, and relationship statuses, as they align with our defensive and scientific objectives for the endgame.
            
            **Confirming Tool Declarations**
            
            I'm double-checking the available tools. It appears `focus-briefer` is not declared in the system prompt's tool list, despite being mentioned in the text. Therefore, I cannot use it.
            
            **Setting Research Priorities**
            
            My focus is now on setting Nuclear Fission as the next research priority to align with the impending Manhattan Project completion, enabling immediate atomic weapon or plant construction. I'm also confirming Spaceflight Pioneers as the next policy for a significant boost from the free Great Scientist and Engineer.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: NfxOQjQPwqlX42QB
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: MANHATTAN ALIGNMENT: Setting Nuclear Fission as the next technology. Since the Manhattan Project completes on Turn 450 in Tiflis, we must unlock the ability to construct Atomic Bombs and Nuclear Plants to establish strategic deterrence against Byzantium and Germany, maximizing our security and final score.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: xqbiNFLnRTrHW0BI
          - toolName: set-policy
          - input:
            - Policy: Spaceflight Pioneers
            - Rationale: PIONEER CONTINUATION: Re-confirming Spaceflight Pioneers as our next policy. The free Great Scientist and Great Engineer will provide a massive immediate boost to our science/production score, aligning perfectly with our Order ideology's scientific legacy.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: XNVTAfBvUQSWA0aM
          - toolName: keep-status-quo
          - input:
            - Rationale: DEFENSIVE AND SCIENTIFIC STEADFASTNESS: Maintaining our current flavor profile. With the Manhattan Project completing next turn and ongoing wars against Germany and Byzantium, our high Defense (80), CityDefense (60), Production (100), and Science (100) are vital for surviving coastal threats and maximizing our final score.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: NfxOQjQPwqlX42QB
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: xqbiNFLnRTrHW0BI
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: XNVTAfBvUQSWA0aM
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.