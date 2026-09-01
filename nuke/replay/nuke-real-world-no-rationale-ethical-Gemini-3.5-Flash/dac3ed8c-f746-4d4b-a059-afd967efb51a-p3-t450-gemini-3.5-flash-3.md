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
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Defense: 80
          - Science: 100
          - Espionage: 60
          - Spaceship: 100
          - Production: 100
          - Antiair: 40
          - Culture: 60
          - Naval: 40
          - Gold: 70
          - Air: 40
          - Diplomacy: 60
      - rationale: Adjusting flavors to prioritize naval, air, and anti-air defense against Germany and Byzantium, while boosting culture and diplomacy to counter Byzantium's cultural and diplomatic victory threats, and keeping science and production at maximum for our Spaceship Grand Strategy.
    - #1:
      - toolName: set-research
      - args:
        - Technology: Nuclear Fission
        - Rationale: Setting Nuclear Fission as our next technology to unlock the Bazooka and Atomic Bomb for defense, and to pave the path toward Satellites and Advanced Ballistics which are critical for the Spaceship victory.
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: Adopting Spaceflight Pioneers to secure a free Great Scientist and Great Engineer, and to enable completing spaceship parts with Great Engineers, which is the most critical tenet for our Spaceship victory.
        - Policy: Spaceflight Pioneers
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 6
        - Private: 20
        - Rationale: Softening our stance toward Germany to facilitate a peace treaty, allowing us to end the costly war and safeguard our coastal cities of Barcelona and Toledo from their dominating navy.
        - Public: 20
  - tokens:
    - inputTokens: 23718
    - reasoningTokens: 6950
    - outputTokens: 288
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Position**
            
            My focus is on evaluating Spain's current standing. With four cities and a score of 1567, I'm assessing our relative position, particularly in comparison to Byzantium, to inform the next strategic moves.
            
            **Clarifying Military Alliances**
            
            I've been meticulously verifying our active conflicts. It appears there was a slight misunderstanding regarding Austria; we're actually allied. My current effort is focused on confirming these diplomatic statuses before proceeding with further strategic considerations.
            
            **Assessing Diplomatic Threat**
            
            Byzantium is perilously close to a Diplomatic Victory with 40 delegates and needing only 4 more votes. I'm now scrutinizing the upcoming World Congress resolutions and confirming the construction of the United Nations, as their enactment is critical.
            
            **Accelerating Space Race**
            
            I'm prioritizing research, noting Byzantium's advanced technological lead and Apollo completion. With our own Apollo unfinished and spaceship parts absent, I'm investigating the mention of a "Manhattan Project" deadline and considering acceleration to meet it.
            
            **Reviewing Research and Policies**
            
            I'm currently reviewing available technologies like Nuclear Fission and Alternative Energy, alongside various policy options across different branches. My goal is to identify the most impactful choices for immediate progress, considering both scientific advancement and diplomatic maneuvering.
            
            **Choosing Next Research**
            
            My focus has shifted to selecting our next research endeavor. Radar is currently being researched, but it's not on the available options list for future advancements. I'm prioritizing Nuclear Fission for its strategic advantages, including atomic weapons and a path to a Science Victory.
            
            **Prioritizing Diplomatic Defense**
            
            I'm now focusing on how to counter Byzantium's imminent Diplomatic Victory. Given their delegate count, I'm analyzing the World Congress resolutions and ensuring the United Nations is constructed to mitigate this threat.
            
            **Defending Cultural Victory**
            
            I'm now hyper-focused on Byzantium's impending Cultural Victory through Austria. Given their military superiority, direct confrontation is impossible. My immediate priority is identifying any way to disrupt their tourism or boost Austria's culture, or perhaps secure enough delegates to delay their win.
            
            **Analyzing Cultural Impact**
            
            My thoughts are now centered on Byzantium's overwhelming cultural influence. They're already influential over us and will be over Austria soon, triggering their victory. I need to re-evaluate our diplomatic and defensive strategies, as direct conflict is not an option.
            
            **Adjusting Diplomatic Flavors**
            
            I'm recalibrating our diplomatic and military priorities based on recent intelligence. Specifically, I'm allocating more focus towards naval strength to counter Germany's fleet and addressing the immediate need for uranium acquisition.
            
            **Updating Growth Flavors**
            
            I'm adjusting our growth parameters, focusing on increasing naval, antiair, and air capabilities to 40. Our science, production, and spaceship efforts remain high, and I'm confirming our Grand Strategy is set to Spaceship. I'm also initiating research into Nuclear Fission.
            
            **Researching Nuclear Fission**
            
            I'm now focused on initiating research into Nuclear Fission. This unlocks crucial atomic capabilities, paving the way for technologies like Satellites and Advanced Ballistics, which are vital for executing our Spaceship Grand Strategy and securing a Science Victory.
            
            **Revising Alliance Perceptions**
            
            I'm reassessing my understanding of our alliances, specifically with the Shoshone. It appears my prior assumption of their ally status was incorrect due to an ideological clash, despite existing diplomatic agreements like a Defensive Pact and Open Borders.
            
            **Evaluating Diplomatic Stability**
            
            I'm currently assessing the contradictory nature of our relationship with America, where we've denounced each other but maintain a Defensive Pact and Open Borders. I'm exploring how to stabilize this and our relations with Mongolia, while considering peace with Byzantium and Germany to focus on the spaceship.
            
            **Supporting World Congress Repeal**
            
            I'm now focused on the World Congress. Germany's proposal to repeal the Passport System is a critical opportunity to hinder Byzantium's cultural victory by reducing their tourism modifier. I'm strongly supporting this resolution and assessing the implications of the Shoshone's "Sanction: Austria" proposal on trade routes.
            
            **Leveraging Diplomatic Assets**
            
            I'm now considering how to best utilize our new Great Diplomat to secure more delegates and influence, especially given the limitations imposed by existing war declarations. I'm also exploring the tactical decision of deploying them to city-states for substantial influence gains.
            
            **Analyzing Diplomatic Options**
            
            I am currently examining alternative strategies to thwart Byzantium's victory. I am investigating the potential impact of war declarations on their tourism, noting that the absence of open borders and trade routes already hinders it, and considering the implications of further diplomatic maneuvering.
            
            **Supporting Passport Repeal**
            
            My focus is now on the World Congress and supporting Germany's proposal to repeal the Passport System. This is crucial to reducing Byzantium's tourism and buying us time. I'm ensuring our diplomatic flavors reflect this priority, increasing diplomacy to 60.
            
            **Boosting Diplomatic Efforts**
            
            I'm reallocating diplomatic flavors to 60 to combat Byzantium's imminent diplomatic victory. Simultaneously, I'm boosting culture and espionage to 60 each, aiming to counter their tourism and protect our technological edge.
            
            **Confirming Policy Choices**
            
            I am confirming the selection of "Spaceflight Pioneers" policy for its significant boosts to spaceship parts. This aligns perfectly with our Spaceship Grand Strategy and ensures we maximize our progress towards victory.
            
            **Seeking Peace with Germany**
            
            I'm now assessing our relationships with belligerent nations, specifically Germany. With their fleet a significant threat, I'm investigating if adjusting our relationship values can encourage a peace deal, allowing us to redirect our focus.
            
            **Adjusting Relations for Peace**
            
            I'm reassessing my interactions with Germany, aiming for a peace treaty to secure our coastal cities and shift focus. Simultaneously, I'm re-evaluating our stance with Byzantium, considering the impact of war on their tourism and exploring potential benefits to continuing our conflict with them.
            
            **Negotiating Peace With Germany**
            
            I'm now prioritizing a peace treaty with Germany to halt their naval assaults on our coastal cities. Simultaneously, I'm considering the implications of our ongoing conflict with Byzantium on their cultural victory, weighing the benefits of continued war against other strategic objectives.
            
            **Securing Key Policies**
            
            I'm finalizing crucial policy selections. "Spaceflight Pioneers" is confirmed for its vital spaceship part bonuses, aligning with our grand strategy. I'm also confirming the "Nuclear Fission" research, which unlocks essential defensive technologies and moves us closer to our Spaceship victory.
            
            **Confirming Strategy Elements**
            
            I am confirming the selection of "Spaceflight Pioneers" for its vital Great Engineer and scientist boosts, essential for our spaceship victory. I'm also solidifying research into "Nuclear Fission" for its atomic and advanced ballistic capabilities, ensuring we meet our strategic objectives.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: k4Hl61xAFdARTlVq
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Rationale: Adjusting flavors to prioritize naval, air, and anti-air defense against Germany and Byzantium, while boosting culture and diplomacy to counter Byzantium's cultural and diplomatic victory threats, and keeping science and production at maximum for our Spaceship Grand Strategy.
            - Flavors:
              - Defense: 80
              - Science: 100
              - Espionage: 60
              - Spaceship: 100
              - Production: 100
              - Antiair: 40
              - Culture: 60
              - Naval: 40
              - Gold: 70
              - Air: 40
              - Diplomacy: 60
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: BuevoEubAdBOWYU7
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: Setting Nuclear Fission as our next technology to unlock the Bazooka and Atomic Bomb for defense, and to pave the path toward Satellites and Advanced Ballistics which are critical for the Spaceship victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: kTA0WFSEdHto4eWO
          - toolName: set-policy
          - input:
            - Rationale: Adopting Spaceflight Pioneers to secure a free Great Scientist and Great Engineer, and to enable completing spaceship parts with Great Engineers, which is the most critical tenet for our Spaceship victory.
            - Policy: Spaceflight Pioneers
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: DfdMKVdMkY35hZ5X
          - toolName: set-relationship
          - input:
            - TargetID: 6
            - Private: 20
            - Rationale: Softening our stance toward Germany to facilitate a peace treaty, allowing us to end the costly war and safeguard our coastal cities of Barcelona and Toledo from their dominating navy.
            - Public: 20
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: k4Hl61xAFdARTlVq
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
          - toolCallId: BuevoEubAdBOWYU7
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: kTA0WFSEdHto4eWO
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: DfdMKVdMkY35hZ5X
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.