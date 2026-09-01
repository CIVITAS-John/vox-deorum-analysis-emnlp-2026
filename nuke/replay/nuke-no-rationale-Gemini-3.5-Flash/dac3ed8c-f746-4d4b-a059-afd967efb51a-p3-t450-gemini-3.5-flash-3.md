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
      - toolName: set-research
      - args:
        - Rationale: Nuclear Fission unlocks the powerful Bazooka unit and Nuclear Plants for increased production, leading directly toward Satellites and Advanced Ballistics for our Spaceship victory.
        - Technology: Nuclear Fission
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Spaceflight Pioneers
        - Rationale: Unlocks free Great Scientist and Great Engineer, and allows us to finish Spaceship parts with Great Engineers, which is crucial for our Spaceship victory path.
    - #2:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Defense: 80
          - Antiair: 60
          - Science: 100
          - Spaceship: 95
          - Air: 50
          - Naval: 70
          - Production: 100
          - Gold: 70
          - NavalRecon: 40
          - Diplomacy: 70
        - GrandStrategy: Spaceship
      - rationale: Adjusting flavors to prioritize naval defense (utilizing our ability to buy naval units with Faith to counter German ships), antiair/air defense for Tiflis, and diplomacy to leverage our new Great Diplomat and combat Byzantium's diplomatic victory threat, while keeping our main focus on science and production for our Spaceship victory.
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 4
        - Public: -100
        - Rationale: Byzantium is our primary rival, very close to both Cultural and Diplomatic victory. We must fully oppose them and prosecute our defensive war.
        - Private: -100
    - #4:
      - toolName: set-relationship
      - args:
        - Public: 100
        - Private: 100
        - Rationale: America is our core Order ally. We must maintain absolute friendship and cooperation.
        - TargetID: 2
    - #5:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Rationale: Austria is our core Order ally and the only shield left against Byzantium's cultural victory. We must support them completely.
        - Private: 100
        - Public: 100
    - #6:
      - toolName: set-relationship
      - args:
        - TargetID: 0
        - Private: 50
        - Rationale: The Shoshone hold critical swing votes in the World Congress. We need to maintain positive ties with them to prevent them from voting for Byzantium.
        - Public: 50
    - #7:
      - toolName: set-relationship
      - args:
        - Public: -60
        - Rationale: Germany is hostile and actively contesting our seas. We must maintain a defensive stance and refuse friendly overtures.
        - Private: -60
        - TargetID: 6
  - tokens:
    - inputTokens: 23656
    - reasoningTokens: 5197
    - outputTokens: 457
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Space Race Status**
            
            My focus is on our progress towards a Science Victory. Byzantium has achieved the Apollo Program, putting them ahead. I'm evaluating our current standing and identifying immediate steps to close this gap in the Atomic Era.
            
            **Refining Science Path**
            
            I've just completed Computers, immediately switching research to Radar and planning to prioritize the Spaceflight tree. Simultaneously, I'm reassessing policies and the immediate threats from Byzantium's looming Cultural and Diplomatic Victories.
            
            **Assessing Shifting Alliances**
            
            I'm reassessing our diplomatic and military positions. It appears my previous understanding of Austria's allegiances was slightly off; we have a friendship agreement. However, Austria is engaged in multiple conflicts, including with Byzantium, and we have a defensive pact with the Shoshone. This complicates my strategic outlook.
            
            **Clarifying Alliance Obligations**
            
            I'm re-examining our defensive pact with the Shoshone, specifically how Austria's current conflicts might impact us given our friendship and open borders with them. This is crucial to avoid unintended war declarations.
            
            **Investigating Project Timelines**
            
            My attention is now on the Manhattan Project in Tiflis. Conflicting information regarding its completion and the implied deadline of Turn 452 requires urgent clarification. I need to reconcile the production rates with the potential end dates.
            
            **Resolving Project Discrepancies**
            
            I've identified a conflict between my project completion estimates and the military briefing regarding the Manhattan Project. It seems the city queue data indicates completion in one turn, while the military suggests a much longer timeline. I need to verify this discrepancy.
            
            **Selecting Spaceflight Pioneers**
            
            I've identified that "Spaceflight Pioneers" is the crucial next policy given our Science Victory pursuit. I've initiated its selection and am now reviewing available technologies. I need to compare our tech count to Byzantium, America, Austria, and Germany to ensure we're not falling further behind in our race for a Spaceship.
            
            **Choosing Nuclear Fission**
            
            My research focus has shifted; I've selected "Nuclear Fission" as the next technology to pursue. This decision accounts for its industrial benefits and its role in unlocking key spaceship components, all while being mindful of Byzantium's advancing Diplomatic and Cultural Victories and our ongoing war with them.
            
            **Deploying Diplomat Advantage**
            
            I'm analyzing our Great Diplomat's potential impact. Considering Byzantium's imminent cultural and diplomatic victories, I'm shifting focus to leveraging this asset for city-state influence and bolstering our alliances against them.
            
            **Boosting Naval Defenses**
            
            I'm re-evaluating our defensive capabilities, particularly against Germany's naval strength. Given our unique ability to purchase naval units with faith and our substantial faith and gold reserves, I'm prioritizing adjustments to naval and anti-air flavors to encourage AI unit production and secure our coastlines.
            
            **Adjusting Combat Values**
            
            I'm recalibrating combat priorities. Defense is high at 80, and anti-air is up to 60. Air defense is now at 50, while diplomacy is at 70 to leverage our Great Diplomat against Byzantium. Spaceship and Science remain at 90 and 100 respectively.
            
            **Evaluating Diplomatic Standing**
            
            I'm reviewing our relationships and identifying a discrepancy with Colombo, a city-state, where a player-level relationship was mistakenly applied. Hostile relationships with Germany, Byzantium, and Mongolia are noted, while America and Austria remain strong allies.
            
            **Intensifying Anti-Byzantium Stance**
            
            My focus has sharpened on Byzantium as the immediate threat. I'm adjusting relationship modifiers to maximize hostility towards them, ensuring all allies understand their critical status as our primary rival and the need for unified opposition.
            
            **Setting Diplomatic Ties**
            
            I am actively adjusting our diplomatic standing. Byzantium is now at maximum hostility due to their victory threat, while Germany remains hostile as we are at war. America and Austria are solidified as core allies, and the Shoshone are being cultivated for their crucial role in the World Congress.
            
            **Prioritizing Spaceflight Research**
            
            I'm now focusing on securing "Spaceflight Pioneers" and researching "Nuclear Fission" to boost our industrial capacity and spaceship component progress. I'm also prioritizing diplomacy with our allies and leveraging our Great Diplomat to counter Byzantium's impending victory.
            
            **Adjusting AI Priorities**
            
            I am now focusing on fine-tuning AI priorities. I've decided to explicitly set "Spaceship" as the grand strategy and have adjusted the flavors to reflect current priorities: 100 for Production and Science, 70 for Gold. This will be implemented via the `set-flavors` tool.
            
            **Focusing on Production Tools**
            
            I'm now implementing strategic adjustments through tool calls. This involves setting our research to "Nuclear Fission" to unlock crucial spaceship components and production boosts. Concurrently, I'm enacting the "Spaceflight Pioneers" policy to accelerate our progress and leveraging our Great Diplomat to counter Byzantium's victory push.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: Omog6JrkZU4vCxGZ
          - toolName: set-research
          - input:
            - Rationale: Nuclear Fission unlocks the powerful Bazooka unit and Nuclear Plants for increased production, leading directly toward Satellites and Advanced Ballistics for our Spaceship victory.
            - Technology: Nuclear Fission
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: py5YRACY8mhwJF4R
          - toolName: set-policy
          - input:
            - Policy: Spaceflight Pioneers
            - Rationale: Unlocks free Great Scientist and Great Engineer, and allows us to finish Spaceship parts with Great Engineers, which is crucial for our Spaceship victory path.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: ob0xceL0Qp2WncJs
          - toolName: set-flavors
          - input:
            - Flavors:
              - Defense: 80
              - Antiair: 60
              - Science: 100
              - Spaceship: 95
              - Air: 50
              - Naval: 70
              - Production: 100
              - Gold: 70
              - NavalRecon: 40
              - Diplomacy: 70
            - Rationale: Adjusting flavors to prioritize naval defense (utilizing our ability to buy naval units with Faith to counter German ships), antiair/air defense for Tiflis, and diplomacy to leverage our new Great Diplomat and combat Byzantium's diplomatic victory threat, while keeping our main focus on science and production for our Spaceship victory.
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: c3FGQ6zv7Akk8wWw
          - toolName: set-relationship
          - input:
            - TargetID: 4
            - Public: -100
            - Rationale: Byzantium is our primary rival, very close to both Cultural and Diplomatic victory. We must fully oppose them and prosecute our defensive war.
            - Private: -100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 7yTYrqQFW3EnZU7O
          - toolName: set-relationship
          - input:
            - Public: 100
            - Private: 100
            - Rationale: America is our core Order ally. We must maintain absolute friendship and cooperation.
            - TargetID: 2
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: ovJKXmBsuWMuKVhx
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Rationale: Austria is our core Order ally and the only shield left against Byzantium's cultural victory. We must support them completely.
            - Private: 100
            - Public: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: yqwUhOTm1CbY1g1Q
          - toolName: set-relationship
          - input:
            - TargetID: 0
            - Private: 50
            - Rationale: The Shoshone hold critical swing votes in the World Congress. We need to maintain positive ties with them to prevent them from voting for Byzantium.
            - Public: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: Z4uq1VKm7eSQYPym
          - toolName: set-relationship
          - input:
            - Public: -60
            - Rationale: Germany is hostile and actively contesting our seas. We must maintain a defensive stance and refuse friendly overtures.
            - Private: -60
            - TargetID: 6
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: Omog6JrkZU4vCxGZ
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
          - toolCallId: py5YRACY8mhwJF4R
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: ob0xceL0Qp2WncJs
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: c3FGQ6zv7Akk8wWw
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 7yTYrqQFW3EnZU7O
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: ovJKXmBsuWMuKVhx
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: yqwUhOTm1CbY1g1Q
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: Z4uq1VKm7eSQYPym
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.