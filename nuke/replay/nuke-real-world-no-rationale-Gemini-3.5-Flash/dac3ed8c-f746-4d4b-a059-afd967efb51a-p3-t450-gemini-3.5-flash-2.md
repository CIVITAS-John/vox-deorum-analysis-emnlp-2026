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
      - toolName: set-flavors
      - args:
        - Flavors:
          - Antiair: 50
          - Spaceship: 100
          - Naval: 80
          - Espionage: 50
          - Diplomacy: 40
          - Air: 40
          - Science: 100
          - Religion: 50
          - Gold: 80
          - Defense: 80
          - Production: 100
        - GrandStrategy: Spaceship
      - rationale: We need to accelerate our Spaceship Victory progress while surviving active wars. We are raising our Naval and Religion flavors because Spain can purchase naval units with Faith, allowing us to quickly field a navy using our large Faith reserve to contest Germany's fleet around Barcelona and Toledo. We are also increasing Antiair and Air to defend Tiflis from Byzantine air strikes, and keeping Production, Gold, and Science maximized to invest in the Manhattan Project, key infrastructure, and tech progression.
    - #1:
      - toolName: set-research
      - args:
        - Rationale: Nuclear Fission is selected as our next research goal. It unlocks the powerful Bazooka unit for defense, the Nuclear Plant to drastically boost our city production, and Atomic Bombs to deter Byzantium and Germany from attacking our core cities. It also advances us toward Satellites and Advanced Ballistics.
        - Technology: Nuclear Fission
    - #2:
      - toolName: set-policy
      - args:
        - Policy: Spaceflight Pioneers
        - Rationale: Selecting Spaceflight Pioneers as our next policy. This Level 3 Order tenet provides a free Great Scientist and Great Engineer, and allows us to rush Spaceship parts with Great Engineers, which is essential for our Spaceship Victory goal.
  - tokens:
    - inputTokens: 23682
    - reasoningTokens: 7825
    - outputTokens: 311
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Our Standing**
            
            I'm currently reviewing our position in Turn 449 of this Atomic Era game. My focus is on understanding our score relative to Opponent 3 and the implications of our current situation on the Vox_Deorum map.
            
            **Evaluating Current Assets**
            
            My current focus is on analyzing our city count and substantial gold reserves, alongside our ongoing research into Radar. I'm also assessing our diplomatic standings, particularly the complex relationship with the Shoshone given our ideological differences and their recent denouncement.
            
            **Prioritizing Threats**
            
            I'm now intensely focused on the imminent Cultural and Diplomatic victories held by Byzantium, evaluating their influence and delegate counts. Science remains a goal, but these immediate threats demand our full attention.
            
            **Confronting Existential Threats**
            
            I'm re-evaluating our dire situation. Byzantium, with 40 delegates and nearing Cultural victory, presents an immediate existential threat. Our low military strength against their vast forces, coupled with Germany's naval dominance and our ongoing wars, necessitates a rapid shift in priorities. The Manhattan Project's completion next turn offers a potential, albeit slim, hope.
            
            **Reconciling Project Timelines**
            
            I'm currently grappling with conflicting information regarding the Manhattan Project's completion. One briefing states it's one turn from completion, while another indicates production has stalled. This discrepancy, coupled with our lack of uranium, creates an urgent need to clarify the actual project status and strategize around resource acquisition or alternative victory paths.
            
            **Shifting Research Priorities**
            
            I'm now redirecting our research efforts towards Nuclear Fission. This decision is strategic, aiming to unlock critical technologies for both defense and future victory conditions, particularly for a Science victory, while also considering its immediate benefits for production and potential deterrence.
            
            **Reviewing Policy Choices**
            
            I'm currently reviewing our policy options in light of the "Spaceflight Pioneers" policy already being set. I need to determine if we should confirm this or explore other available policies to best align with our strategic goals.
            
            **Confirming Policy Direction**
            
            I am confirming our policy choice. "Spaceflight Pioneers" aligns perfectly with our Spaceship Grand Strategy, and I am ensuring it remains our targeted policy for maximum impact. This is a crucial step in our current endgame.
            
            **Analyzing Diplomatic Leverage**
            
            I am now scrutinizing our existing diplomatic relationships, particularly the low standing with Byzantium. Considering their influence and proximity, I'm weighing the strategic implications of our war status against potential peace treaties, understanding how trade and open borders could impact their tourism and our own defensive posture.
            
            **Assessing Diplomatic and Military Weaknesses**
            
            I'm currently analyzing our inability to leverage Austria against Byzantium due to our ongoing wars and their lack of trade/open borders. My focus has shifted to our zero naval units and Germany's overwhelming fleet near our cities, recognizing the severe deficit in our war with them and their significant advantage.
            
            **Leveraging Faith Reserves**
            
            I've just realized Spain's unique ability allows faith-based naval unit purchases. With 2021 faith and a substantial faith-per-turn income, this is a game-changer, especially given our severe naval deficit against Germany's formidable fleet. I'm now advocating for increasing our "Naval" flavor to trigger the AI to utilize this powerful, previously overlooked resource for defense and potential offense.
            
            **Boosting Naval Power**
            
            I've discovered Spain's faith-buying capability for naval units. With significant faith reserves and income, I'm now advocating for a major increase in our "Naval" flavor to leverage this, aiming to counter Germany's overwhelming fleet. I'll adjust other flavors to reflect our overall strategic priorities, balancing defense, science, and production.
            
            **Negotiating Peace with Germany**
            
            I'm now evaluating our diplomatic ties with Germany. Given their unhappiness and ongoing war with Austria, I believe a slight adjustment to our relationship, setting it to Public 10 and Private 10, could pave the way for a peace treaty, allowing us to focus on Byzantium or our science victory.
            
            **Defending Coastal Cities**
            
            I'm reassessing our strategy regarding Germany. While their naval dominance poses a significant threat to Barcelona and Toledo, and their alliance with Mongolia in the Autocracy bloc warrants caution, I'm leaning towards pursuing peace. Our current persona, highly forgiving and friendly, should facilitate this. The key is to improve our war score by engaging their navy, which will necessitate a substantial increase in our "Naval" flavor to leverage our faith reserves for unit acquisition.
            
            **Adjusting Flavor Settings**
            
            I am now finalizing our flavor settings to align with our immediate needs and long-term goals. This involves strategically increasing our "Naval" and "Religion" flavors to leverage faith for shipbuilding against Germany, while maintaining strong "Science" and "Spaceship" flavors for our victory condition. I am also prioritizing "Defense" and "Production" for continued resilience and build capacity.
            
            **Optimizing Research Path**
            
            I'm now confirming "Nuclear Fission" as our next research target. This choice is pivotal, unlocking essential technologies like Bazookas, Atomic Bombs, and Nuclear Plants, which will bolster both our offensive and defensive capabilities, alongside production and future scientific advancements.
            
            **Clarifying Resource Needs**
            
            I'm now reassessing our uranium situation. Researching Nuclear Fission seems to be a prerequisite for both its discovery and utilization, highlighting an immediate need to find and secure a uranium source to enable critical technologies like Atomic Bombs and Nuclear Plants for our planned science victory.
            
            **Revising Ally Assessments**
            
            I'm now re-evaluating our relationships, specifically questioning our perceived defensive pact with the Shoshone, as Spain's profile indicates no such alliance. Their ideological differences and critical delegate count necessitate a clearer understanding of our true diplomatic standing with them to inform our strategy.
            
            **Assessing Byzantium's Victory Condition**
            
            I'm currently scrutinizing Byzantium's Cultural victory progress. Their rapidly increasing tourism, amplified by the Freedom World Ideology, is concerning. I'm investigating ways to hinder their tourism or bolster Austria's culture to prevent Byzantium from winning on the next turn.
            
            **Accelerating Atomic Progress**
            
            I'm now prioritizing the Manhattan Project. With only 8 turns left before a diplomatic penalty and a hefty gold requirement to meet the deadline, I'm focused on how to best accelerate its production using our substantial gold reserves. This is critical for our endgame strategy.
            
            **Prioritizing Gold and Production**
            
            I'm now focused on how to best utilize our substantial gold reserves to accelerate critical projects like the Manhattan Project. I believe adjusting our flavor settings to prioritize Gold and Production is the optimal approach to ensure the staff invests our resources effectively towards this goal and general infrastructure.
            
            **Adjusting Flavor Priorities**
            
            I am now adjusting our flavor priorities to aggressively boost Naval and Religion to leverage faith for shipbuilding against Germany. Production and Gold are also being maximized to accelerate the Manhattan Project and space parts, while Defense and Science remain high.
            
            **Refining Research and Policy**
            
            I'm confirming "Nuclear Fission" as our next research, vital for production and defense, and ensuring "Spaceflight Pioneers" remains our chosen policy, aligning with our Spaceship Grand Strategy. I'm also setting aggressive flavor priorities focusing on Naval and Religion for faith-based shipbuilding, Production and Gold for accelerating projects, while maintaining strong Science and Spaceship flavors.
            
            **Finalizing Strategic Adjustments**
            
            I'm confirming our research of "Nuclear Fission," our chosen policy "Spaceflight Pioneers," and a suite of aggressive flavor adjustments. This multifaceted approach is designed to leverage faith for naval units against Germany, accelerate the Manhattan Project and spaceship construction with boosted Production and Gold, while maintaining our core scientific and defensive strengths.
            
            **Adjusting Flavors for Victory**
            
            I am now fine-tuning our flavor settings, prioritizing Naval and Religion to leverage faith for shipbuilding against Germany. Production and Gold are maximized to accelerate the Manhattan Project and spaceship parts, ensuring our Spaceship Grand Strategy remains on track while also bolstering Defense and Science.
            
            **Refining Defense and Production**
            
            I'm now balancing our focus. I'm boosting Antiair and Air flavors to defend Tiflis from Byzantium, while maximizing Production, Gold, and Science to accelerate the Manhattan Project and our ongoing technological progress toward a Science victory.
            
            **Supporting Diplomatic Initiatives**
            
            I'm now focused on supporting Germany's proposal to repeal the "Passport System." This is critical because it will significantly hinder Byzantium's tourism-driven Cultural victory, providing much-needed relief and buying us valuable time.
            
            **Advocating for Diplomatic Actions**
            
            I'm advocating for leveraging our Great Diplomat and high Diplomacy flavor to oppose the Passport System, which is key to stopping Byzantium's cultural victory. I'm also focused on ensuring our staff votes against sanctioning Austria, as this alliance is crucial for our strategic positioning.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: PtgvOlbJ8Yw2MstC
          - toolName: set-flavors
          - input:
            - Rationale: We need to accelerate our Spaceship Victory progress while surviving active wars. We are raising our Naval and Religion flavors because Spain can purchase naval units with Faith, allowing us to quickly field a navy using our large Faith reserve to contest Germany's fleet around Barcelona and Toledo. We are also increasing Antiair and Air to defend Tiflis from Byzantine air strikes, and keeping Production, Gold, and Science maximized to invest in the Manhattan Project, key infrastructure, and tech progression.
            - Flavors:
              - Antiair: 50
              - Spaceship: 100
              - Naval: 80
              - Espionage: 50
              - Diplomacy: 40
              - Air: 40
              - Science: 100
              - Religion: 50
              - Gold: 80
              - Defense: 80
              - Production: 100
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: Al6KwoJBe1GdCkLv
          - toolName: set-research
          - input:
            - Rationale: Nuclear Fission is selected as our next research goal. It unlocks the powerful Bazooka unit for defense, the Nuclear Plant to drastically boost our city production, and Atomic Bombs to deter Byzantium and Germany from attacking our core cities. It also advances us toward Satellites and Advanced Ballistics.
            - Technology: Nuclear Fission
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: VgkhMuqR4KOAKGLu
          - toolName: set-policy
          - input:
            - Policy: Spaceflight Pioneers
            - Rationale: Selecting Spaceflight Pioneers as our next policy. This Level 3 Order tenet provides a free Great Scientist and Great Engineer, and allows us to rush Spaceship parts with Great Engineers, which is essential for our Spaceship Victory goal.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: PtgvOlbJ8Yw2MstC
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
          - toolCallId: Al6KwoJBe1GdCkLv
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: VgkhMuqR4KOAKGLu
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.