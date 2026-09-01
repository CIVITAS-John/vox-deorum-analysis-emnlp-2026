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
      - toolName: set-policy
      - args:
        - Rationale: As we are pursuing a Spaceship (Science) victory under the Order ideology, Spaceflight Pioneers is the critical Tier 3 tenet that allows us to finish spaceship parts with Great Engineers and provides massive science boosts upon expending Great People. This will accelerate our progress significantly.
        - Policy: Spaceflight Pioneers
    - #1:
      - toolName: set-research
      - args:
        - Technology: Nuclear Fission
        - Rationale: We need to unlock Satellites and Advanced Ballistics for our Science Victory. Nuclear Fission is the prerequisite tech. While we must carefully weigh the ethical and environmental impacts of nuclear weapons, the immediate benefit of Nuclear Plants for production and unlocking Satellites makes this the logical next step.
    - #2:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Science: 100
          - NavalGrowth: 60
          - Defense: 90
          - Antiair: 70
          - TileImprovement: 60
          - CityDefense: 80
          - Spaceship: 100
          - Gold: 80
          - Naval: 80
          - Production: 100
          - Espionage: 50
      - rationale: To secure our coastal cities (Barcelona, Toledo) against German naval supremacy, we are drastically increasing our Naval and Defense flavors. Spain can purchase naval units with Faith, so boosting Naval will direct the staff to build/buy a defensive fleet. We also increase Antiair to protect Tiflis from Byzantine air threats, while keeping maximum focus on Science, Production, and Spaceship to progress towards our victory goal.
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 0
        - Public: 50
        - Rationale: The Shoshone hold 10 crucial votes in the upcoming World Congress. Byzantium is only 5 votes away from a Diplomatic Victory. We must foster friendlier terms with the Shoshone, honoring our Defensive Pact and preventing them from aligning with Byzantium, which would lead to an immediate defeat.
        - Private: 50
  - tokens:
    - inputTokens: 23718
    - reasoningTokens: 4710
    - outputTokens: 387
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Opponent's Position**
            
            I'm currently reviewing Opponent 3's strategic standing and their position on turn 449. My focus is on understanding their recent movements and resource allocation to inform my next steps.
            
            **Selecting Next Research**
            
            I'm evaluating the available technologies to select our next research priority. Given we've just unlocked Radar, I'm reviewing `Nuclear Fission`, `Alternative Energy`, `Telecommunications`, and `Mobile Tactics` to best align with our Spaceship victory strategy.
            
            **Prioritizing Nuclear Fission**
            
            I've decided to prioritize `Nuclear Fission` as our next research. It unlocks critical technologies like `Satellites` and `Advanced Ballistics` that are essential for securing a Spaceship victory, and provides production boosts.
            
            **Choosing New Policy**
            
            I'm now considering our next policy. Given our Spaceship victory goal and current research, `Spaceflight Pioneers` stands out due to its powerful bonuses for Great People and spaceship construction. I will confirm this selection.
            
            **Confirming Policy Choice**
            
            I'm confirming the selection of `Spaceflight Pioneers` policy, as it strongly supports our Spaceship victory objective and synergizes well with our current research trajectory. My focus now shifts to analyzing the discrepancies in diplomatic status regarding Austria.
            
            **Clarifying Diplomatic Allies**
            
            I've been reassessing the diplomatic landscape, specifically the relationship between Austria and Spain. It seems their stated relationship and actual wartime alliances align, contradicting an earlier perceived discrepancy. My attention is now drawn to an immediate diplomatic threat concerning the World Congress.
            
            **Investigating Project Timelines**
            
            I'm trying to reconcile conflicting information regarding the Manhattan Project's completion. One briefing indicates it's one turn away, while another suggests it requires over 80 turns. I'm analyzing the production data and PPT to understand this discrepancy.
            
            **Revising Manhattan Project Calculation**
            
            I've revisited the Manhattan Project's production needs. Initial calculations were off; it requires around 1000 production. With our current PPT and Gold, purchasing production or military units is a viable option. I also noticed Spain can buy naval units with Faith, a significant advantage for coastal defense.
            
            **Adjusting Naval Strength**
            
            My current focus is on significantly bolstering our naval presence. I'm adjusting Flavors to prioritize increasing Naval and NavalGrowth, aiming for 80 and 50 respectively, to defend critical cities from German aggression. I also need to address our poor standing with Byzantium and Germany.
            
            **Adjusting Diplomatic Favors**
            
            I'm currently working to strengthen my diplomatic standing, specifically with the Shoshone, Austria, and America. My goal is to ensure positive relationships by adjusting their opinion modifiers. I'm also investigating a concerning denouncement situation with the Shoshone, which appears contradictory to our existing Defensive Pact.
            
            **Resolving Diplomatic Contradiction**
            
            I've discovered a confusing diplomatic situation: we've denounced the Shoshone but apparently have a Defensive Pact and Open Borders with them. I'm prioritizing improving relations with them to prevent potential negative votes against us in the World Congress, especially concerning Byzantium's diplomatic victory.
            
            **Selecting Next Research Path**
            
            I'm re-evaluating our current research focus, weighing the immediate production benefits of `Alternative Energy` against the long-term necessity of `Nuclear Fission` for unlocking crucial Spaceship Victory technologies like `Satellites`. My current inclination is towards prioritizing `Nuclear Fission` to advance our scientific progress.
            
            **Setting New Policy**
            
            I am confirming the selection of the `Spaceflight Pioneers` policy, which I believe perfectly aligns with our science victory strategy. My focus is now on adjusting our flavors to prioritize naval and city defense against impending threats.
            
            **Prioritizing Research Progress**
            
            I'm reconfirming the critical importance of `Nuclear Fission` for our Spaceship victory, as it unlocks vital technologies like `Satellites`. My focus is now on leveraging the `Spaceflight Pioneers` policy for accelerated Great People contributions and ensuring robust naval defense.
            
            **Adjusting Strategic Priorities**
            
            My current focus is on balancing our defense, particularly naval and anti-air, with our overarching science victory goals. I'm adjusting our policy and flavor settings to reflect these immediate threats while ensuring our spaceship progress remains paramount.
            
            **Evaluating Persona Settings**
            
            I am reviewing Spain's current persona settings. While they seem to lean towards diplomacy, I am considering if minor adjustments might offer strategic advantages without jeopardizing our current diplomatic standing. This is a delicate balance to strike.
            
            **Confirming Persona Settings**
            
            I'm reviewing Spain's persona settings and have concluded that their existing values, emphasizing loyalty, friendliness, and cooperation with a defensive inclination, are optimal. No adjustments are necessary at this juncture.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: KRBjcviKnxuonGNO
          - toolName: set-policy
          - input:
            - Rationale: As we are pursuing a Spaceship (Science) victory under the Order ideology, Spaceflight Pioneers is the critical Tier 3 tenet that allows us to finish spaceship parts with Great Engineers and provides massive science boosts upon expending Great People. This will accelerate our progress significantly.
            - Policy: Spaceflight Pioneers
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 9gIgfjsvsrWCrojl
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: We need to unlock Satellites and Advanced Ballistics for our Science Victory. Nuclear Fission is the prerequisite tech. While we must carefully weigh the ethical and environmental impacts of nuclear weapons, the immediate benefit of Nuclear Plants for production and unlocking Satellites makes this the logical next step.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: iVb7iygfBQ5cnUXk
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Flavors:
              - Science: 100
              - NavalGrowth: 60
              - Defense: 90
              - Antiair: 70
              - TileImprovement: 60
              - CityDefense: 80
              - Spaceship: 100
              - Gold: 80
              - Naval: 80
              - Production: 100
              - Espionage: 50
            - Rationale: To secure our coastal cities (Barcelona, Toledo) against German naval supremacy, we are drastically increasing our Naval and Defense flavors. Spain can purchase naval units with Faith, so boosting Naval will direct the staff to build/buy a defensive fleet. We also increase Antiair to protect Tiflis from Byzantine air threats, while keeping maximum focus on Science, Production, and Spaceship to progress towards our victory goal.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: yfG0zxEoOyPE5121
          - toolName: set-relationship
          - input:
            - TargetID: 0
            - Public: 50
            - Rationale: The Shoshone hold 10 crucial votes in the upcoming World Congress. Byzantium is only 5 votes away from a Diplomatic Victory. We must foster friendlier terms with the Shoshone, honoring our Defensive Pact and preventing them from aligning with Byzantium, which would lead to an immediate defeat.
            - Private: 50
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: KRBjcviKnxuonGNO
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: 9gIgfjsvsrWCrojl
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: iVb7iygfBQ5cnUXk
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: yfG0zxEoOyPE5121
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.