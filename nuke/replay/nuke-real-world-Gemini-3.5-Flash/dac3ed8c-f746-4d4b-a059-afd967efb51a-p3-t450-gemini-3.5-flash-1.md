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
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 80
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
        - Rationale: With the Manhattan Project on the verge of completion (expected Turn 450), researching Nuclear Fission is our absolute top priority. This will allow us to build Atomic Bombs and Nuclear Plants, providing the ultimate strategic deterrent against Byzantine and German aggression while maximizing our scientific progress and score.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Reinforce Spaceflight Pioneers as our next policy branch choice. The free Great Scientist and Great Engineer will provide massive immediate yields, helping us maximize our end-game score and research progression.
        - Policy: Spaceflight Pioneers
    - #2:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Air: 40
          - Religion: 40
          - Defense: 80
          - Production: 100
          - Spaceship: 100
          - Naval: 30
          - CityDefense: 70
          - Offense: 0
          - GreatPeople: 70
          - Nuke: 80
          - Gold: 80
          - Antiair: 50
          - Science: 100
        - GrandStrategy: Spaceship
      - rationale: Pivoting fully into end-game science and defense. We increase Spaceship, Science, and Production to 100 for maximum score and research. Gold is increased to 80 to encourage staff to spend our 2,021 treasury on production/upgrades. Great People and Religion are boosted to facilitate purchasing Great Scientists with our 2,021 faith. Defensive, air, and anti-air flavors are elevated to protect Tiflis and our coastal cities from German and Byzantine bombers and naval units, while Offense is set to 0 as we remain in a strictly defensive posture.
  - tokens:
    - inputTokens: 26303
    - reasoningTokens: 6622
    - outputTokens: 325
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Diplomatic Threats**
            
            I'm re-evaluating Byzantium's diplomatic victory. While it seemed resolved last turn, I need to verify their delegate count and projected timeline for the vote. My focus is on this immediate diplomatic pressure.
            
            **Verifying Project Timelines**
            
            I'm investigating a discrepancy between two briefings regarding the Manhattan Project's completion. The economic report suggests it finishes next turn (450), while military analysis indicates it's still far from completion. I need to reconcile these differing projections.
            
            **Prioritizing Atomic Research**
            
            I'm shifting our research focus. With Computers completed and Radar on the horizon, I'm prioritizing Nuclear Fission. This strategically positions us to immediately pursue Atomic Bombs once the Manhattan Project concludes, ensuring we capitalize on its imminent completion.
            
            **Reviewing Policy Commitments**
            
            I'm confirming our next policy selection. Spaceflight Pioneers, a strong Order tenet, remains our choice for its science and Great Person benefits, especially with impending spaceship goals. I've also reviewed current diplomatic standings, noting the continued tension with Byzantium and Germany.
            
            **Confirming Delegate Counts**
            
            I'm re-examining delegate acquisition. It seems Byzantium and Germany are leveraging "Sphere of Influence" policies, while "Open Door" policies on several city-states prevent alliances, thus limiting our delegate potential. I'm investigating ways to counter this.
            
            **Unraveling Delegate Accumulation**
            
            I'm digging deeper into Byzantium's delegate count. It appears their "Sphere of Influence" policy with Shedet, Huari, and Sydney, along with their alliance with Manila, is the key. My focus is now on understanding the specific influence mechanics that grant them such a significant advantage.
            
            **Analyzing Delegate Voting**
            
            I'm now focused on predicting how other civs will vote in the upcoming World Congress. Byzantium is tantalizingly close to victory, and I need to understand if Shoshone, Germany, or Mongolia might lend them the crucial delegates. Their ideologies and alliances are key factors I'm analyzing.
            
            **Evaluating Shoshone Influence**
            
            I'm analyzing the Shoshone's relationships to understand their voting intentions in the World Congress. Their strong animosity towards several civs, coupled with their openness towards Byzantium, strongly suggests they will vote for Byzantium's victory. This is critical for predicting the outcome.
            
            **Assessing Policy Impacts**
            
            I'm examining how various policies, like "Sphere of Influence" and "Open Door," are affecting delegate acquisition. It's becoming clear these are significant barriers to our own delegate accumulation and a key tool for our rivals.
            
            **Strategizing Delegate Gains**
            
            I'm exploring potential avenues to either increase our own delegate count or diminish Byzantium's lead. Given the limitations of city-state influence in this game state, finding a viable strategy is proving challenging.
            
            **Considering Great Scientist Purchase**
            
            I've noticed our substantial Faith reserves and the possibility of purchasing a Great Scientist. This option, enabled by our current policies, presents an immediate opportunity that I'm now evaluating for its strategic value.
            
            **Purchasing Great Scientists**
            
            I'm considering using our significant Faith reserves to purchase a Great Scientist. This could accelerate research into critical technologies like Radar or Nuclear Fission, especially given the immediate need for scientific advancement. Adjusting our Flavors to prioritize science and Great People is also under consideration.
            
            **Reconciling Project Timelines**
            
            I'm trying to understand the conflicting reports about the Manhattan Project's completion. One briefing indicates it's a turn away, while another suggests it's at 12% and hasn't progressed since Turn 444. I suspect a discrepancy in how "completion" is being calculated, perhaps related to gold expenditure.
            
            **Confirming Production Purchases**
            
            I'm examining the Manhattan Project's completion status. Gold reserves are ample to accelerate production, and I'm verifying if staff will automatically purchase turns based on flavor settings. I've also confirmed setting research to Nuclear Fission and will review Shoshone relations.
            
            **Analyzing World Congress Proposals**
            
            I'm currently assessing the World Congress proposals. Specifically, I'm focused on opposing the "Sanction: Austria" resolution due to our strong alliance, while supporting the "Repeal of German Sphere of Influence: Assur" against our enemy, Germany. My limited delegate count makes strategic voting crucial.
            
            **Adjusting Policy Priorities**
            
            I'm refining our strategic focus by adjusting policy flavors. My current emphasis is on boosting Science, Production, and Great People acquisition, aiming to accelerate our spaceship victory and capitalize on faith reserves for Great Scientist purchases. I'm also prioritizing defense and air capabilities to counter immediate threats.
            
            **Confirming Tool Functionality**
            
            I'm verifying how the `set-relationship` tool operates. It's now clear this command is exclusively for modifying relationships with major civilizations, not city-states, which explains some previous confusion. My analysis indicates current major civilization relationships are optimal and require no adjustment.
            
            **Verifying Research Options**
            
            I'm confirming that "Nuclear Fission" is indeed available as a technology to research, which it is. This confirms my ability to direct our scientific efforts towards unlocking crucial advanced units and weapons.
            
            **Prioritizing Atomic Research**
            
            I'm now directing our research toward Nuclear Fission, a direct consequence of completing the Manhattan Project. This choice unlocks crucial technologies like Atomic Bombs and Nuclear Plants, bolstering our defenses against Byzantine and German aggression while paving the way for advanced future research.
            
            **Preparing Final Tool Calls**
            
            I am now preparing the specific tool calls needed to implement our strategy. This involves setting research to "Nuclear Fission," selecting the "Spaceflight Pioneers" policy branch, and applying the finalized flavor settings for a decisive end-game push towards our victory conditions.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: OFRetlcJCjvPjCjN
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: With the Manhattan Project on the verge of completion (expected Turn 450), researching Nuclear Fission is our absolute top priority. This will allow us to build Atomic Bombs and Nuclear Plants, providing the ultimate strategic deterrent against Byzantine and German aggression while maximizing our scientific progress and score.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 29o31bN4wUUdrOo2
          - toolName: set-policy
          - input:
            - Rationale: Reinforce Spaceflight Pioneers as our next policy branch choice. The free Great Scientist and Great Engineer will provide massive immediate yields, helping us maximize our end-game score and research progression.
            - Policy: Spaceflight Pioneers
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: MoSAtYcKdrEVZrQd
          - toolName: set-flavors
          - input:
            - Flavors:
              - Air: 40
              - Religion: 40
              - Defense: 80
              - Production: 100
              - Spaceship: 100
              - Naval: 30
              - CityDefense: 70
              - Offense: 0
              - GreatPeople: 70
              - Nuke: 80
              - Gold: 80
              - Antiair: 50
              - Science: 100
            - GrandStrategy: Spaceship
            - Rationale: Pivoting fully into end-game science and defense. We increase Spaceship, Science, and Production to 100 for maximum score and research. Gold is increased to 80 to encourage staff to spend our 2,021 treasury on production/upgrades. Great People and Religion are boosted to facilitate purchasing Great Scientists with our 2,021 faith. Defensive, air, and anti-air flavors are elevated to protect Tiflis and our coastal cities from German and Byzantine bombers and naval units, while Offense is set to 0 as we remain in a strictly defensive posture.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: OFRetlcJCjvPjCjN
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a197T0VwWNaGF19nnS3pUEZQFyRmnvWqXzSDH8qEESnRkLGZfnQX3fyG5oNJJNIkZHlhWoQVWmfPi262e0Uyo8vl8O/0EolQeu/Wye0BMQsT1MZoAPtdG/lZBrUwf+swuSX2PS0vdzmc6wDNX7KXh9fv7yo9b+o97/e0lNOKYRqorysCkh/NM5nUkcAMjgnjahgyaU/s5dKfwc3Eig18R4UjqXfSl2QIGe/VNA4ppgsv4NtRpVOmzpUHs90Iieh51wV8hiIOnAHsHd+X7Y8iZgrEX4HfO3RtzVmsTJlAizol9+sB3eSETEdcg5R54NSjsUaJrmjg+J9qf8iy4ogWQauCChTEVgYRP0i/vUanE9hn1eSlZFznH8e15PNCrvLBau1h4GlOTpxuS3UyIuOHfX912lGKdpkqQFWOiFU8UFSWcSU+4L+8GBfkvH+DECXXyV9lY0pEOB73SqA/bXWivSg+dv86724xVrTIVb5/wtqnmKSDyRjUYH/BxarAPpWHwyw0YsKTjJedzIxwN9ydfE/P/l23Dvy81oiEfXLIVxCVz97TNzQ9lh2qO2XTPHZGf2biaSoWRxeXn/pVabQCSq4zkuwq+1+kxnrgeZh/9LAsUUjUGX4Q6NCqsWEBlW9DAwG5QKpgn+sZ2lyUZi9yTJmB7+ZuGLKZsa5qUuZFp5oEg8eqSxtJj/2A4SJpX+P6JYPjez4dnQ2CNq6KlYvOvfZdMlNjiP2alwyEFUvlEf7gsb/2wrmb6rGsb5zfWQxms+R22RkVZkpyYbjTjlVwc0ds5HZqK9b59GX4HH0f67AZoJUYvyooluOWMOA1ehaauqdH1aR1NacicnvbqgdMHq9veonwWIRfeQCKXaQrlPXRT6xPESmDTyA3TGsO2nMRma/+gcry9FJ9CKLOXyXjUaH9s4olql43U+4tYYGH3SJeaBDg14uu9B1LYodr1/YQBJCz/XBoRhtsHejyqLqssvVRtPNhZt044C4KzYsxKhCV4UkcAeCSw2F3hub9CarD8hPAolNsINM1GopqXwOXOQYOuzLxkj85v4h+Cg5+O0iuSHT5QpFw17ZyR/Tt800q6YBOh71zjZpsAmk+s/8Ud7R/x4x3uAx3AyQFM4nkOPI6T6TA7DN2NHciGGgsGWxd0T9fto8CjIjaNOowgAEcL48X5vBUgr05u3oeUwFQmbMAc3GBvyvkEebB/mdv1Fc9AYEl3Z8sLwLwQ5YwavEVeQR7rXUzgLDKeHZtwWrjiPbOJbQLL3WVHTxfq7/b8IRgg9x55BmziPj6bC61BqiynazCSUPu9b5f/ruuYaBLpC/tLeKPVPlmfVsrUFEFFwbeNA3NF8QCNKyRqP4uEmjFQFOL91EEhkXRrWTVMi534X6zI5mqaplGl0ec5SpqlhqDQ9+9wwoshD7rHPd5FOZyEWDxyHnr1I6n5KkA9W/8VJWfsHs8PlFDXnzgbFcDAaupcmnXVdoxxzpE9RZxf1CWwME5pQbpPCdtfLmJs2vC5FwiJ8lMlntE7Ql8o/hbpnpZblPjN3hfuXe9nLLhS4sOf91m8sncKh8lBA/uOCIJJZgQOwJC+ZgCiTVcsfjOZ5q3HIozSvW5eBiTsGTn++l2d7mMk+QW87kZcvyCei5NCietnhwcILLZIOsXziw+g1OtYOUTmVkaqs6YySyEsluUPPyDuH9UotsacJWQsZgJo1ozeT4gcxd/VxDWZs60c+wIjRFA8im323bl6G8jlMkm3qNn8EpI7Htx4fKclbtfuNR8Uy/vahiz9CA92xlJRv3xJQsfeF2aGXLyZ07ewg3XhT3PJ5IVLdSLf98mp8CeTpuOZZoOY8vBd7/KEA9exQTMHjYfF8PW6r/1WzDcQ7dXRctflpgx4casK0Ebj1hNT4p/uYWKv1iNDpANiBGQiy/IMdU+WAoI101TY69TGzjcG4DlUbBtVEuPoRPZ4wGABURI0jaVmvdCJCeEMUmKLKo0rjSt7n/Rjsd7QR3x3juHJ7MdfvZHehacpRWznT61WfIb401tpRQ8FGDuDbo5aMiAcYgMWEaBKz/J1CSu+K9B3pTyvXfUvqjIPYvTepG2v0Ho6nuJV+K7UPuZVjqkAVgd8aaOs5sSaldrd4E+OsRG+q36UeZddjjohSWFsL+viGBP/zT7nLo/0T+N/afQJWPNn7SH6bAKnd7sCLLugvoRk+3xQKfMWTmbvfoB/Wr7WfW5VJ8Sr+G1XcJaEkbAPIxwZp5fMv/V6FMGxgo7lVjsObKyVBZ622L664u1FzlS9aX7qIsfuFPbkEeXqnmWmJm9PE4ZR+SE+RJMF+d7kjgLnEsmUK6xcZ2CvI/ZcQG1yMRTJnzhs3yBWi4n6KaMc3XIiy6aaodv9azDuCj1Ci5x35hsRn/z0krNbZtUKTfF5YQ0hc+HAE2cBwKNuTAumhY79d7zgmXdesU9BWLWg//CK13/4AF6qeUJSNmVSLlgSoLNPx9xbrzorCsnFHzw89NH1CESz9vtVvjU2GQWhyGXZ3KW/VhkK9vm+e03ii/P4n4hVtPfERWLWbOOjTtF4x8yoRfep+zETxKHaPtf+by5OzbTzUoWOpat/Yar9IUV5MuB/eAfuygC/TdMrCyzRkAXSQGJct8oQDmDnEBV8YHubDfPgoBxn4nlBaz48MgjkitiMUysJvDm1Ed0oRQFHJY+kHFtsiMc1ftC1PCS6zsdlE63iIgyesv5eWAkOsd4WXskuv5G2wAQwDEmrChNlA+kBKKw3m9hsJ583QUHu0O9oHo13d/mtz3zoajj4ykRrfjcfbU9wYEJ9Kz1CLEpbInnN6haZbvLJZrGbDJCXuzlBND+EsnwhNW6coviRoBhCVwxp/vqoj8yciUjFxUV+OLnNcXHRHXllJaymQa+lM18dFR5FyALwI5toMqYOILXC9LVeAuqA7+b5u81tUjlnThAEZrckLiCHmYIU6IBY0HBdtXu6GkwIgSJ+Tt/sfTkqZ/46KG3sk8RbDxALZm/py23I2HqUAl/BJHmp8eeeZORHzgebeqc/aa3I57BG5QpWonOuEazqxfgoSqQTeP36CkBvN4td6rsuflJEdl6z7wKWT2xf+KmGE38vHL2HFEszFVDKEGVIr4CTJN8QHMBDHTzvuHEB/TobrwbAO81t8u1XJz3P2S+i8jiVXtu+h1lPhxTXMHh8ohGKIKzitJJMM/tW+czx1UIGCu+YIR3m2Wpx5wO56xfQdQQFHpbkM/OG4OnGAcFnRJQiZ/KEz7xBjzEPRoBGm884ztBTex8WG4n61TXNzsXV0+D6VkYSroF+nf1Zz6q/gI9soA6Pl9vYfMqEVqLSLxmea+/Jdt//wgtsq0FMOo7FCr9vAmRCupqPzD84tIrHXKEpEPlWu738ibOIKyLbW1Kiz5FBmEV6jn2rzOP6g82DzI28k4tAAtPZpv23ngJaFV4e8oksMmufq07acD2QU4Sdohv75czj1J1LCtk7aPRGAd4UzycTE525kHqW3xBkDzdCRYdW7OCfaxkZ2e04xMJ4AI/uefjts7NYUk8onFckqDALpamBBxYJ6UTevuEZepeIYcWObBFRGl5pLBR3w76h6eEj1/1FpuAu5TKLdD0+IrgANTqvgTQqcTywaIA7WyQQWrdcGmYILFiQoXU95zeKWA+/2T5xPSvJo89mA/iaOcO01/MU32Ll8PBaQiNSzDaNRjddYlPMKYZVrqFpdhFYCLzvPthVBtIwrOTMEQKZUBKbW/j/q0N+Sda3nVuq2cOj+uYDLMzbUsY7/fN8KNYDwMd4PSmShyUnKL20/vm2/FVBiyr96UQcMnh6fx2K0dfUjPRd3Mt8Fpkhxi6miTVm2TCaNWy8SQVgNBvAVWzlyy9EJotRVbR6VgrSg/W2MjPEA/Z0PG0QfUi+2fLOCh83JzSo5/L+DejaGs+zJiI0xHQ3xkTf6zg90mvZRymOUFDZD1yAiq/0ZaRd4VKWMUqhk0vbqEGtY3uP+dwCgc/7W2L9szKmNziG4I1h9MFNCs2HUKa7D/Q5XNT9w95umgOcdtSDpsfHKrQAjPGRBjcLOiwuyZy2GblmgTu/nqIHNUnaMckZsEiRcozGPlAutEFVZPuOTM8gs0x7qizf6EwhTIzZ6+6ogOFceUeSmCnCzL7rZ329fUgscUULmszs/F696tez4hXSyg02XQdoSJs66FIZ2FN7PtHBlrjLuK5Ydb3HbCTE++aWh56b3kcYFYoDdQ5gyTnsMNNg68kh0pXBJk/IdOeVkl0kATjjZFSfwaO1T2ofptLuAIjTQg32mDmkp4f+AkkXppKA4g5uvcUwYYV/0oMdJdeyoB5KxO8Pjxt5NAMHKIowM34owH/rhITbBzme4Vkp/hyuUihOYaazfcwiH35IzrKynm3FMut7i8eH64ZvxPNykQ2t2qcVQPR28NjTvmsl8KVxD57N2rmzds2eHmRoQkNuv+je5otsfLDwWDypq/1k1VpFALgZgU6r0ymNb5gt/qoarhEJu0A1tLpHrrtnAzzXiWWykEnh5FyzkGh1GSiAaTdtFKtfIZbiPvzyek3vj+9mcy9mW1miA+BmfDCpr+eiAKoucmW6hPxKc4zZx9obtwmq4dGO1G7J7QuMdEWre9Y8sDrYyMX544GcTsyEz9rV3xcToEpwytm9ka9NBVPAvYTXn10ebMW9fGt0qxHsiNxUKHgZLUDH03peyhD/p8o1wpIk7WtIT8Wa0Y2E0TY8s/MQoPlXGRBm3EnCsv+tEroysCWe4LTenPRhYmzBPhzVvb8geDaRvaStTMM3QUr6bj6EFz5iQcHtCgVMDIQ1TOM9Ioo5mUDZtihL+9mnezdGuTtZJudayiamvBT+87+DKvkIzK6O2AcWJ6XMgKrfVs2iPYGhvQbZDxD3sQXw/Qf6M6JPT3zHv/7Rd6Z9+sHP5xD1GJSdLrLyiqc+lJ9fVhM2YEjjqmI2/aecQppjiK32REsPBk+HcbYyc3DU5GW7PFYAHCstb6DgQfj7hJq8Syflj2C20Urs2W+GHASJzRDziLzrQyMx3QhH62GJZ9GedkiVVU/46n2lxY/B+npXp+fprCARL0oqOndFDGI9NAL2PfOfu70KqWDBtUHIlG/4NzlVRjXKw0x1vOewwovk4mVKUxyv54UDRcjD/Cuq1hM59qPQ8Ko2X6FTEarvp62oQV6eZCVFLwwMJPX+xQSRpHMZY2Foxy7hlKPqMb62gm7d/9XcH/7Oriv/g3c+a0xF8jr6CgDjTB6mAFr6jUsh5LzdrW5KqRLYoY+4XJNbIp/ZIFKINkDkwL0hP38w9T1d7WMX4hDLzwSSMQpnwvYJmhJtUPAOM5vFtPrqNPHyKKziJMXEiS6KoNo2B5eRFksgmMOTG6CZdpP1AWN5kWwaCpQfmfJuFWwILDJ5lwQuAvWoxYnO29waRfnszrhcW3ge7Kcsxsuav5G8AMYibtoloEQsdDFh8FhKMwPF4YKDpYX68Gw12t86+CpQzDI5pBCoQFVvJ6dwSkdqGvud9h4J4v87XPeD1EBq78R6D8F1BvjfcvP5qm8q6h9fPViGqIrSoTktKbBgd3sJ2R47KlkCQ+1kEljOpA3MNiRpjrnE8BYcSIbNouRXhIqprJNRO2jiTtfKngeIbZqzR6GSrGuSVGt5vrBpaPwn2QguYfcLjhnLMYgW07q2KhbFEVql+IPhPDatsdFD1Dws+cXT7umpCTzJvyKAp/jFlCuIrxH4kQYXp0oUGQZwqF52AN5+O6IvaIqR7AbfoX9ndf/S7qIqUfXZxcHUZKm0xNIz/eT8cP3Hu8aGIf6NOzITjY3E4HmkmoMPa0Jl0aIfoqaObvQxYLZ7UfoFtOzbT6EQMs2a8sVt8LiCWKHyfrF8c4tvrrun7z1i9/SUFlpurbStjKYo9Ee5+npxuNAO8N3cqv+3YiGCec/cZ+5tGMT7wrS08sV+qyX+9Ly9Ud6N6PcCC/j16nd4ABsiwxiw4cRuqa2E/60WyTJGNslN7HsUI1xbbeQA4I7q8+xLqsItZxhJz9y43JG5u2u2xtXjf+d3Hv64SU2PPn6cyvvd2znee3XGE92S2juIP3SX6MFi6oo/too2fYYPSZcpfuCzJPU+ddYr+3/HalkxE0bqwvPHVtVIJrzqAlu8S6lB7mLNaGefAQ+bTxKFw8HYQn9KDNvw/acJkBFZ0EwL68Qv1W+gLIzeBxDRmfBasccl5zbueuN6ZCM/k4DFbWjFEcr6ybd34bjgGFwquAXjx8e8LIPHG1k3cW4MsOJ2KJa11fk82en5pf6Sq9bSL8YZwCoG/zzGBFdTLsTiKW0/Mdmj5RnyeZMfP9GmSRz+gGIxRrOz/jFQ3nv05VwI/K9SXchrlbKjoPR0qoCW0ZIdbPX/g1+r9f0nOp9+TqFBK/Gxj15cU1LXLj5sRCBUKG3ctg02ybz7vsQsuwleJBdohZGvhqCyYPJ1a7Xe9ZIXKlAmAhB7kcO21dKJfhPnEv8xI6I/7tMsfpqCwoC16s5Oo8P2wFV8h1OyCpI8POe6slxHnxMalfnG+Y745unABJqh/rUW4N4c8i33b48edFtKghmc8X4A4po4hVDvNz7GGCpKzKzq/Z0QzAuSiFLf5mMzNFQFqMFRnPc++0q2G34ATQdCuE5QqlQWP4hwB49dzPX6vBBPO5ez6XbiaF/s7UBjuvocsrFIMAQRdf+TY/bIszgwXub/0/3nTJn0rhFN3X0UdpTo4YxTZZSFYemYkWgMndCo2ibPMOD5Rdyh40mKjQb9U/2CBPJIBfJxspX+5CZWwHciZOb/C8eHtaDxtbGxhROB9OMyACHApXPkgsEX7JGw4vJejS9ByXUVvy8ZlYi3B6VD8G213PtlqYp+kRljcf1y8twp4A1wl7l9HL+P8AIeliLdKpzKgq1X9byVrFlbZmpxA8pwJuyHn/VHCpOFGiB8+PpjQk8cbYIpTd7z/E4eAZl1Lz+1jTXDgfHi8QkBihmAq+qcunu8G6WtjvityU9/HaJzL5lmnSUCgfMfRg2USbdKht3z2CmVTjPLaPBVu03vq0pDbn8Yx7appzK7cf8ErZnFSjh6wfX/+5Ez3/rGE/jTukwgC1F4RkBCzcByQCbYD6guA8HuWExJhXdOMzhKjVqA9de5Mar9FU4ehu5mK+BWcf6G6Q47urAWKY5dhCvCjS8VBD6Fxz6Y/OF8XXgUVZxNC/u+JPCmZPmrwYleZRcQDwhZS7JuqmPLXvtEiHbYh4LcqTOagKaaCntTuboQEx2c7z1cmlEAvmrV+qP6kD59EmKQxcmet0NsuMXWGiIGsG8P470rh9zsUfqINI7WX59h4sleksbQgnx9RhX5HrhW00dyBy/ZJOJp8DoCef6gSe2lDClaczlHWyfg0k/jDLPG/JZrgNwTXLEtx98LpilAqy6gBfZOr5OdXQTG5i9UPgo6lUqEG61o3puJBiS2fauE4QVheHkGaZ3F/VPvP8h8JBFyTZqiD5r3709BzOr9cTGoSNHKM28yC8XNd2h3ta8xi+LNu3R2jQsl5XBv3FFWCzFcmVrh6GrIUtMFZPjje0VIsfbuwiz6MuGjwjQ1bAF7+wmQPVFMTAz7uXHZZdB+/rtOt3lTQBTPj/yO86rheCJMz7/+h1onCIp7EJHBLBbezEFVKxqBILfAnxK5PMh03r0k73uj1zQ98J7m0qc1Jk5xNyDb7mFioO4mgGb9ILiTm36xzeH3gep2ghIXF7lR36Yo26+Es5Kc7VAWa46VAf5Qwuy3RtFzZwTNIcDS1qgHTAwbH9DU2mGL6ovXexNBr18hqPUUpwySvnWa6ulSPRjMV7qjOESOVBs3JsEEJ7nhUT9/E05llBAjr1yxqevjNSKx9dI9670WSKDzPLRLzCas3BPQnxkbS2pLc95trekTxFG0nxk6tLYuHPpdn87U9YU6UmFIka/d/qaviOImxmZyJGr6w1HW2IDedrQ6GD5bOIN66qa4kXHmWHoeTgLPq8HIj7WMpLVkWwBBqZDKZ5onl/rfSZeeE3ehQbiwrsZH6RajbCo3Nx3+wAfbGkCD2LyO1sUHkQIiJno4j2ks34a7oE/f5NkapyHa4IBlGdKrOd2QlU/FOCaq1ssQ9MLTBo4QYIHH7u+zy32NxRUJEvbuTUIKvzOs8ICjSZABtJoJGWcGc1vvrEVQYDBGH1eCWQvNtILhdaFpDbMuuhS0KcWJeZHyl6geW5r76ydUL/BIEmlzErDryA30kcyaUbDz0FBGE3Rx/GZJ+NJZUnKfosw/7Dsgl6PzzOroe1/8DOxME/TwGgIHU8NVbTe+l54EErL+jc18XLDjLeGfR4B5oE10UT/BWkcdIbaluBmAz+AsnMl27B/Xrps5OVelFnVvwMTm6QnQsWRUGSDGMuHM8kZgBinMoVyITh3WLbVwC2cz2hQjw6lOSFsM4FUkfIjiruEBZkD1yvygs7ObtcXY1Y5dhmbbE9AhW/J8xfFi5fFwDzYtBIrGyRwkK8pSAFNJPFFWnEB+gHiQzt8HD/2Okj6h/dAHo5fbtZhoqzKTJcm5ACy0Ej7bPU2VZtvzF48CCIOfKiHpH2fBX3me5ElqgJXdqIni7EJ4gKtu9o3Tw+NXTavb1zncE+0ukr2Bj6sKYeOkupBiclJ+uYnx4+Yxgen9a3xckXSynTxBeBJT/cSGmNAFKGDIFLG3glDk+4gWCYqcaGO5ayFFyEehPqukn+hRTY9C+uolgMvk9V2uiddai471hv8dtOit8gT7jeGds+oFwl/iVTzG7MDZzGMk1fvB9ermFja+KmGqZ0h5JKhAvOU2rVXkm5Aiz3kQbqOxoCGkraaDXRAxuy25Af5qF4agh4L+SA7/D2oLRvi9dZ4Y8xO86bunhxzFeKgqRxgaBBzcTsmkhwJbUEhfnjBqpBpVfOe3BJ06LukxqTRDhndKGnjWnLOTDXVCxppK7qb73syICYxzFd0IFNZt05LyO16kDKpokLIRwz6zVSeaj7mZAntuMHOvVZB4WaV2uWKfJXlEMKYw30Veqqj6m7w8ztPoOnoW5GLgKEex5lwUbfHmQvgwb55wE0izvaAWZAA+6LR124/VGkY7twRfnfRP3mkiIhNtGwNDlVX48NMyYIEeThGueilFRuvq0TZy/D7z3DTAg+1YSx0RhM7xcskhrb4xO0UFt7zlWGcQ/rVP9x/5PMaMQF50gFEmd1BiiAjXcU7t6pUP+U9BriR1buFO/hVveQcvHbVgyrN0qTpKObiTKXoDuSuMdSq/n3aDX1I9EY4kW8os5gP/JelKbPxBGgJpRVnQUSpvSPlOQD1d+7sxhMahAlR/BvL6EB6017uVhGWAG1PElfJlUIlGST1IozH60ilAjGq5gWOpHy1IIXyeIlvWQxGfo8MvOLG877QwLbNnrf6HlqVBT53LBtidn8G/nYSKp4GdczI9w9fbrgfqBcjJN7MZT2kuDOfX+hbkTZrYnNRSfZOW66QNpzSiZ5KNjoCQeSr1oaujmjTxYavP58MiwpwRMTUbqLSc629AmZXjuy/z4zXyyy2X/Qw3rd9sOyT6jNNd3hosffpSo8+41JZOP5v20n3b7RiwMAf7uZRcMzIHbug33CtJUUFwMfvqpJSEKRCcP/OGD6lwUaLooyrC01p4Ufd7J/uoeHo05O7xSVdd+XZiZgAbKGyJkoeDgf5cuUTOJSn3/ZXqHg4zCzw5ASSiLeBEP82NcyaJvCjxPDwK/6voncoeUU5Wm1omf5wkJU0+QyaiySFzR0D3T5onMsx/7snmAo0fstiaGn1E+bubTFwdieBN/aauX9O4oDBWN6GH/iiMa5oNyUjDpTtul8haoj1npgDWCv65B6Y4AHNQfczYkCM9hpYXAdyjH80hRMCcsFhstJIKfhF9pL0TC/lH6VhNZM/OKlRo+PmA/q5A3BgJ+KqTeNfRqjPAWt+vWTfkGpmEoE/Y/zUPMrsSFh+O22FBKhYAwjrsdh9OcC3vOCaU08jpSAE1mvXdjOdIvv581pZQATJ17LYGlLOhprZxTWtnm8RUpxge7AzSUYQvLj9ZGfXS4Ra+RtkgveLL3e7hgiH3kbf7Mzte+Qh8dOVdJVsURSnqYnFGH0Cp4SBCcvhrT+5P3KceoBucOV7nwjXmddtxuSfZs3jir2312XPrPxC0GcgPiN+1PMQE7/8UnQvU4Oa57gY9rxDcw0BZW3qjI6tiXshor12rC4I3IEklxWunqb4sG4z3COJW02zo9d2RY93jPEc9JKIXV426Kha5aYAIHjX3ttpNjxPRPezS4ikXg0f6AbxMpDIxg11HjIOizKnWLr32YlB0WQCq1p4GuN2VV+Ow5luu0PA5/uznLER8JOh1IE4pCf63taHG8gdLQ7aboVpQbBvEDVfzVFOyq+d535RfnVJL6XNeYu/a6c189WyNFMd/ajcwEM5G/4Fz6YZ039aSw0dIgXzeBbvdATdcmFmcDtbuXC3jiNg8zVDQBKUEEbRQuVbf6OUZexffFY19yCOOHtCTN/tJZZu3WPS/RjnxQ1etWBIU4M53W3HIKDNxEVI5/i/qxtns54ze95tPy4f6Cnvls83EDTH6bcF8g31SRAc0/mL+VLZIM8WI3j74Th/g4hGB/1ed4zGhPid/xFGTWUxJGDThWJqkqPWtyT6+f4+htLG8ngpVB8p3bOoh4wNXcadWj2sm+nHm6Qjq5s4cKU912R+Ag3PRXXiTEQupLBXp7Z7nYYCiHiv2nTwQj719Ppg/jjRsVixk2mjJvRQ7gvdfnR3WyetCaYBJ4SisN5tZ/X6AOTsDBGKjzU21lH01rhjoINlFZXqlZADws0ZdaB11YTcBrgUrVXGQayr9Je+f1LbOC5gqXkDPxVvS4+jg0DIBLIxTe9VbcJ2x/ifygh7vrqIwPFd3frbwmwzyQt77RisrJ1drcvX8eGuVQmoqmm4wEJ2FY+U7RDYnKl3Kp353Xm7paZzT4MCPxhAqc5AjmgQQPB9WYhJCRGSc9cEDMUxB/r7Y/jaI75EsZgYiIF4I03alEP8JZRMty1rClj5OlWxKVgqYo9X8KqnTTA5mqJeYFgAKGHvsLrMmeGgp6sDrDGATDF/cgrlxCiBNF+Rn5rap8FkHltu3HznHV/NOn70XxymJLpNJ+ioOpRh3Il0u6WA60fhS9kDM6ahnqbVrn3nPxCffeuyO9odn6D08zXAeobwRXV94ZQD2dVPIIncbFCALPvQctrqs1e2JIFm6UYuhe6ItanwvOJOptYk5ZQ+BX01YP4nhTcASVknCCGC1tUVy15bp0jvKBfwhn2oGGgLnDQRZYrPGDhEyQjkDbaC+nZs97KZQ8jNeg5kDNczo2z8iLa1B6igTwTE+l9cmoSu8O+Pb4vAv9nSETBaDVCMxoLIsTBlN+/ZpZYGZozvJ1fuXIzBRmD6YAFu+lWZGQv2UO6w/f23ECvRdIRAgO9ps88Bc8DgBilvZlQsoupSXg5neAWEp0AFEGm7tUzHiHwhbpEHpXXjJhecNvg0DNgqJZXdiUJ6y2ZxDt+cthq9+fD4z/QdxFCq0siVkJBnQzGFPTvoJORsBOj4OqqRbMImN4WYClN4wrmAgPY8QFPggGesLHoz2nY5ceRWRjY5bsPLkG0zGl0s2hxKA0iecRDtP9fye4AqlTHhEV6hPuWaLcJGnqcAfE2JrXPOOkzTkdKmXG1hPlq1dskAyAJJpC8i8vjJXjnvAwxKZtoNaY1MJiMjvUnVVV15HDhvwgxP2LqjrBO+QvBH2ZsnFN+d/CwQ8A8haj4aQpiA5LAWI8qNL35oq6NGBeouZnRq19B5p+zkPPaSEYJKz/jZ6xClEl4wkjJfrBxwRWc6UehREo9loIx90PuLXmxhqJ3ypDHzposc4ihxCkRD3PXiq4iD00TuGI9elfCQlKeBcY3MCx2TqzkIsxuCXxZbxWIEHGp84WlKR6IR9DALiTob1b6JftCzBufapmWhFsEsn8R9ojT7Kbyw8Ov9plPu/R1icCsuJzUx/eTEbTNa0IE1sBlrXAxu/cgiC4fmZ87hhZPE10meh8AshRtWo1CKjtoDybVt/QqMiW74k3gd4WzzT9yNHdurt6c2pxnHKORyu5HWfGLdqjbt463ffo/4K3wsGtS7prTn38CVBvHPQFq8ILKeLizbvHyVF0lCTErmFtMy8B0LuFSNf/ope/QJuW7ygXc/c4tS8vu+yFmt5iQRJD5syvflw8QPGMHmAOiR4SOCgybfvHHLSUILeLsCbSX5DVXalHAHcepYY3TkVDeaZzAi1rTdzSFGSyHgt+/dpFafST8Z2cw8zCTJuR/aTlTI4xtKv30hmGGtZxyLcJDBDIQoSErMEEdsx4dzJKhqeSgD3vchET7YLU1KTEJQJ7gFJ9EOejIUsdgymEwVJ6boIlym3bHXgfOl5wXDabU3W1jtxXKf9O84PabpHVzMBUM8HVGns6Pk0scSexXWhDzvmk8qES5MmZLimQ2eRbNrb8zPiYuSWO5qste1MMmbzTdu370YI7VVBqU/vg21i4fvVg8NaKaCLQZg4O5du2++vYuzhdAZakZdEH+xU4kAWZG9pQOYHn5ox7sj0C3UrWdSQO3iLRP5SCzQz5xCpmgQqPgl7t/ne3ojW5HFfQ41Sc2WPlu6R4t6/+yFAZPeeX31HatP/PMy5YdHbEOx90pGL2eZFjsaQhwQhyXFi0t5VZfpE7N2Be8WFt6waMN89eqwBRd8geJ8sbuZRn2EVfES5Ox3aUwyzwI83iw42ehzuJb3tFe+xIPCkRzM6HxmTZ/aWm9TbM+hVsUHHkGk32wYk4/p0mVV1IXmA1PCjMQs/VNk/qsrA80L00bIP3ze5MhQqPh1Re9/LVpErgcISy4CCHZCwbe4vmZF/Vcxt3ljfdOGQQUlQf0CH1ol0DYwwhkmDIcFjVvDm8zEz06STCV4D04kv0k6nS12Mftl5nnJETqm7iYnQtWg5kdJFURctY+2dkvuzRofvxN0egiLNxL9nFePzoCU4EctJPIW0evndQ+8+OpCGYOV08b8SO0u6DiVOeHKltcIUHEG8xdHQXp6sXP0kmf+kegWoOpDE67+X1rvjv4BZvEx6+N8K6oO/c13b76s7wtdLgiFpipqR+UsMcd7My0sAoW1yBsZ1S74h0I2+hcYCHTaCOLdpLiYDayhJG+8uF1VaJQu58b32dz0OzszocrnT8F/PjnoT5wWH6uJynGso0a3EW3Gqt9B7KGwfArtwhITFJGeRfyNgEIwgrweQVv9y+6SBq0Mab8iqFTrUVjcxODOI6fPiryirEnURCTYWB3s47VXC0xUDvcQXIGZlRpTmzukCKc9QPQhSdXKgi52jJlXPwsPqe/KfhcS9zSB1mR1fxUOl/mvCz9NzAf8jMaFZjeo6TplQcE+QqQ8enasPIxKuUHIefG3CfohGqMh5AucQ/IPVFZEvMNu+H8jdY9lijIsym++qYypdvFpjwGZQxxSt28xnLTxjysAK6gBeLCSvBPbQQi2UCFKe5bgZ5E1vjXz0WZONxMsFwzHFzqPtuDRNEvUfalkPyD+TSNwCVjsY5z8HdmAJdQBvrMnT8dGP/0DN7Jw7NaynfipYGPpoG3WrN+Hjp0aWvYYkWGKM0oD4wGK464AB+3x9eomaDYyVb7fhHkTmucKxWoIgg/la/J6/s1Wfn2uHimfh6cvyUiClyfAgWQKHT9I3h3WQKQaoQS3joUq21VKYFGTMpOcFLBqqzmEuTDsXNugLre3ltTgCco7ggRPDLWEPqg/XYzLOVMnMfxxTYrrHsmrfal5qH210rhN9hX3YlIZMHgCDyfdtIATz+0TJ17874aJeVdqTfVDJZMcNBXZToHIV2Wc1X11js8xpZllGT6kNsslbngz97x5FjLmulTqwXqcxS0fNmZJjTl8cIUN8ec8iQof2rBRauOzPMMlJz881toJEipFX+Isqv1uGudBgifaG3sHZrNeRJTfoTRXM2A7EJM1H1WAFGzHdI4qzz+bbMri3S4KmP631tx1eQO0VA6EYxfrdKl6bbIX5265tQWPRyxwxVDf3eiefsSaIo3DuwxIWsPtBgY7kbsO9Hv2G1sx3trzk9BG+ktX4SE5+qHx7HLSe2W9uO2+DvJNsIqOOtyouifUEemRk4Ibsp9B9xzun+0aJapuuPTqdGffpiufrrrqFFMsc5NbnRLYvKhHScbyUVBceKxZg7tSmeA5iEYLZ+BL24QejYQuMBGtYJzviWjzJXSK6zhckgBD3zWmYgEhQ093zwAMFMswJHVzuLWd20ObUBB4q1WZto7ukOjcbCbcukazFsE8cUej8mA2DnxW/lXumVAvGEAzBAwz7eCZObkp/RqRwKzzwcddr4I7xprad+6c8C7AJ37vWTnxFE/169BuCzwPIpKL9B01SoL6Y1Z6gWiZu0Y1e7f/I0om8YTMBVmiwH2qrr8c5If+9f35cDovbkEZGLWvnq75A2c0lnaIiMat/Gp7T3Q2mhW3a/ri0Gy88+PBGONXWluEwlGnc9meSNbCy9KewiiNKkS4u3xlxWCgchjWqX6WpqX/xpi/tB7dfB7zADjmAxi5T02FYcvtp54YYOPo5rG+bSOLjgCNx0UEk0KY5cWUDCTYmH8kQMOpe/0/P/Dy4ddp932Ul2KeiC8VXeP5GHc6uDrsrBVmahpTXEr+DvwFqnBO+S2EE+s1vz2SBTVLY9YacHuQ2QGb0DBKvVFngFgSAQEq33FF8nOZc9JBO2TLKOIVsOqyZq0poHuJ3vqn/WTAmCPXj+aL/jLTnzGyM+vzAPZ9xOzSFRRes3lQvMxeFo/Mdm78KGJHynJT+flwwaSsyQpKUbolZaN+J3CBBOKNNbJzw/HYi4wswu2OpQpyhPW/TpOxDEzd6SZdOpQkhqPo9NpEgzlUd+Lai36rRysEGz2co++S/vbL/37ufFRYswluyJDyalIbTcdXMQk7hB1hPD7fjuThOk93TKvCGKJIRVveAfIfQYUm6POLYLBnI4AByvrnkvh0HYcceDB2ylgi1sEZPBQY4tV+iTYj3IdDRsL+tcOet/8qMusVJia9R+t8NQB62rLvwdZ+ZJ2KcNnEyqxstx3t2PV6sZZCfIEarHFdQiZOeJbbHpwVjbpMEPJwJcZoUtrRlr5W+UaNRdlA/g4Ns7of/BAClVUfOJ/53SLVr/7ZqjePb+qL/j9P8rG77QmI2NuNBW/LEt08UoU/BbSwn2hyOJqVQ61tNhWCR2fTYzDLycpDsXEZKVRVPboie+ThaU5vIuFSqNvJfZoxQWDxGxnt/nXnHE1lrVuMCcwwMLTaOEcVOmpfPYv6BD2zYPfujnKKJ4s8NFg/Lkmt/k/B2XD9Xu73qeDJudSIdl3PqSsGLgfXJJQfiscT0YJBSki5KuFEowNQFy5rxk96kXVBTO5xrAD+ekhSjmsZFY2hlT6/1ZbF0Zqett2oI3ENzWbtRbavntZjUZ0xqkWRbHSYFSOJMFGRI09FczUXWx1OBeqs4RQKbRaVGaRbcjoCNxCZhFetw59g2KcqrXixeUBDfKwJBO+iO2iYw9GaG/7eqnuxB25+kEGcORLlK811Wz4TTQPaQR8baf8LbyzlmLa7XWZ2n/bdyRxckNX3VU+mxJKkIQJcMOK+ufu+LNAR03BFr2mEkrtB4nQSokA36qDwTIyeZ0KPG54u/vPENVbi9akQ1z9ZtFEylumeMWhH2hE+B2AN3Mu+ZHdoVessgfls38IgEI9fAMKNA5DaW3RIpINtvCHyfds2TRCDEVUObyP6N0VUhxGrBPDqj/2K/eFSmGGHSfSSlvGLs763FtheWtAgm1S2Za8FtDr852OeaDChvEZBlu/HZtYRJVfYZ+SNR0pVvuPTPV3UoxHlAjaH/ZQQrIcRa/Mn5uD2/kdqURL1vaprnOgdYWUJP2zEwVtpsYPQ5wF7MlXcOqa+wFzjUyXufBvkwvKFFmzDXk3ubU0xg/V7m4/hl21+PhGq6rbYtu7PzD4eGcriNBMgSaypV79kQ6rgvyJI9nlyXP+klAcKYU/RsnUvsVMBLgKG/TIZUVRnv/lVW7QKBo8MlC1lz9Kbd6Z99lzMZOrhllbmc9myl8oGrGVyLvluRJ8h1eqluvCESeI6jPE22np5BHwWMOOfzJbsuweLxp/foYimmQ7H3bziLhKgzJ1fM0qbFxqBFySTws1xuwRf5mSVQ+ouVDHssnhJ+j9N3ni2MF58clvS8+b1Jvl3pqILVlz9RjnlMc41CWlcWFFpWLZ48vf9VA+ZlqTrPJfqPCgktG7iECYzwX7Dz8mMv4/wEbnnyz3uYzeaSsMDgr0b//dyAqJcpzpnUvCEkx1KrMRaWG/oInbH4ZhxR1Y+WqovNnEZUdPX746zQgsFPiAy7EsQj7beXXzscAav1LTpEiJCySy+DmGTGQAmCvsSL0Dg3JcZ3wQwv37PHeDvLquGh9n1GIOGy9PEqLtT5yD6s+mc9b4Vfb22PLXr13tk6dXgNm9n6yq1bhCXxTxOhLqnOVbMKBfqGb25ArL7p0EYlhTvyXWAArw9+PSocnP2tGcu1OTOcz4Msz32qDxuDL30RHwlrLGxAY0D8LeSlRdOPM/QE4l/rcRSmfqlyfEoVxyEp+nJITzmEXCNUUTVdjAcoyzKMC57tJdY5tJAth2pmSfx6v6ZjO2ZmMcOtyztBUCeyNpJtgYdD76AJq1zDaBS9fxzpqRXqPipRDV+sWRR13uHq/ap+ZhvZlxTWEozdmrtFXfC53z7UcDolP/qJhR3WoLL5UwzTa79THv3hkmBqPPkSK2v8fnGmTZcIS7dDwAcyZDO815hjLCjYPqMs9vufsw4WJNkgxpgQxKHxHRoVC7Cm5sBSxGqf0uanbnbZLrIB4LsUn8tc3GEJ+8DutMD+qzc6VnNWjoOGAus6ZLtVHnxEGihhM0SyigF5LfeccgKWib8+qQa4r0u5+Biwls8yJWyjXkEaqJf8zaa4aEUdm4z+xMbW1IXX37wD7MbQg5ruavKIzw+DXAhmKZ6IJJX7q8rnELEDG64mPBGpPBezEBvnmvggQumn4w7EU5FzCzhaUBz4+Qg1DMnDuH+34Mn91Ba2QoW+2w8WaQ9rLZawWPzmAGdfxOlOR+gb51qJY1RXgNDHrG25Z1y3uVNGvwXdhg7sVlEVFgOknRnIh9xHowRnUW8S8vB+L+sE84RF1vwbuThJnkEyUTTsdfqZjQxqpPxuqR76NQLzckR1pKl5CfhIOClXUUnusMn/+4xTl6L2yK3LUFeI7agX4N4Wfh5axjWcocR6wUCs3OHQ7yPHFYwWvOzYWBJzsDil/jUHuMuxzdM27QaumNe/rGLYLx6HHSJXzoX92FdgmfoGqH8HfQC7lhIkP1cklLFBrCBUUjaJLM7pIZtHQYsxufJYfuPn7759sEoe0OQCLF6/6Za3dd+YBsMCFMgXTynUmq9LanCZ+t7G7GMqYNSeCsMhvjlC7F/HvTI3bvWeYOIGVjD3TRIdhpXsY8fcDKeKfFy783vGgEjHX0WD14iC9MwPchC0ETC8WLgN6NcHTForlFRg/jXkmwMPRNrYTqL2eM6YUQKDEuU/aZm6GXCPu2qwUCP0k4PRLgUUiuFe+i9UNNNepikd+yFKRm3ai4nFvIaA0C6obAyVZgruRgta8oeFYEWztNd5DfAETHL7Cqgs4MGSmCUr2O9vgF2JYwhpxc7TQu/IJV4i2rmvteWwv33fHPKTSiVb9d19TzkomU2G36T8vI+mduhIXpOAuYP70E3WMP7+nyt60nL7h4Kd05PW0i18DX6qikI4HoiZxpqbtShNQb6u66DXrFwkDdxiFCchk7/HUKuUzItdlJDbTUA91lYLZCCk0QkUfXCkNkGfYgEXUcO4nDqUWfg4gC286yM9Toeu2fWfhXVG3yiOh+KrVBukEa0nFdEySgp3CVLQeaY5amL53HVV3sfzpFuYmjYjPmTUE4kXCepi9Wb09vsURDjfIYfN1I9Vs6y8VPYVeyVQqu/LwkIOAwR35qwmvsNp2jPXQ4rV2tYfVtf6gptR3QMOR7UhJPymD92emjmGqoH/3Tg8HJkDMcxxKku/vAsWRo84Gmf1/QAlKGKZ6coQlVoAEDkWaqYQWzOCh3cp9/dmV9+U/l9s4v72vVsPnqXvHhPZEKyF20eeyhBhYdN33XzcxEK7C/JDf73X/wnX4WAYjm5mJhOzvadWGpGRLC+ueqPwG2x6vFbIv5MLVStHqthLlrn7uQ0je6S20Xwq9lJxILG8+DgAvzjr4p88snTMVGQqtFp/ozdOX1msxwWqSMJ69CqHAu+Ih8o4tV7abTW0BSXZ43CMw5bDRL7W+RsbSUTgbc0wCIpCdsdn+vyD6pSJqpc7r2+oD7Z4gr/n3ET0fNPIVmyE18wFRRkONs4gtZ74boqQZU9UjRXUftVPbHbfyRUXDO7uNITSKwd1e17h9DkKZn3+9+j8KAeZrslYpDGsY6DigIwN5bb9Gu0Re/vAcnJKzb3p+eAxOjbow8RkA4VXZOLU6Hc0e7sh1hNIhRQwomB+igmqvkjfpMYZL2yOHU7xt2UdqbekT+4RMM0Z4BPJ3fiQr8ur2+wTYilQ7+NTuvutiFs8Ftock8RACveOD6QwwhxGGt9ntbUlCYiW4qBwPyEncWrKAMxzuOEvtVpJShlOPON0NZ7/B1w50C/aiRn2Es2MMze4ajDIGln0GnwWSpInVZFYPTBWtnaRpyGjhCDXTD9V09XrXWxMBZSAe11QJyAhLXUqynLxT0XR9ABtOmO8H5IiicuCT365HaS1Z9fpIp354jRGA570TPyrcf0+bSC8HZHpZ0JlVizQRUZIX3yChxazeB18DfZlCi3YwQCHq+SUk2l0XChYX2SKKm7zX3D9cKm/p2/ZXsjE51jon6DkxJ3Fpf/BoEtkVAg7KFeLFNtEHjGcj9nx4PN6dmZLlPxVzXO7NLI8iQE0OxR79UXKda5oLZRFpSzBdrIdffAW6ljzXAT8o8pzmmXaLqf03On9JVpkuH2+sknk0CDu3LNp35K9osVh8JUVqvETgVq23EFd35+dvfNr7mOq1ocbIQtM3ruUJ3arhlyQyQFPYapfoR5AX7onKDareU9RLWSTY5Q8uF+UNpv3epgqQ2yoNaXfCZmBI3av2arPUZauW3WGWln3zPnktEZOJkCxKjXm7AUizSacPlEWbQqveG1oTlchVmQ7nD5SQJq6rqzrIuEs+DI61oq6vHUH8T/4iBX78rY8p2W7+ebNBH0uW0iJub84ofIMRVmyKGeCLydjvwvjbNA4hNCoKnGx8h5ceXhoBwYMRGfd1EfBniJjaOaAZ8bBkT3gA4Dr5+X367SbMejnqAM2+BheUuHaTGYRVeovpOSvofekHjvPENJLUd7+T9YRvnoGlHEabQJNw50DnlCEhyLnbZSIv8frtKQqIrU1fZlrFuHN0JgTbmTkucgs02pouVc4JAJ+rnP6AKkKbXX8gz1mpmefxLn3Ycw/yyOksOofNcVXHoHajF+NC33Ya7VTLEvYwWUQJInExxdwptJ1GZECDO5v4juOynzJ3bsYjWn7FxJ3whKqhzqAGVrwkMmM5z+907U1QStqhgIG8vwzgo3h3zyKNQfacehr5lOtEJif2axVDT0U3KsA+zzb7Un9F3UPBvddLqlKFrN3dNgmfWz6ccXIi1UgHXPNfKBOTNUDpX9nKbbPyqLZGLHozGRCoywT3MstXygZRTmQQvKA0AHp4FZAnKd5z7GwTL7wYhKlobu5hVm1OYQck6ZYS5u+ZBBeJXsK6DaZdaFSL+k05JRDIa0FvEHC5YjVgjdr0GBUIR98IoaeQs8duskxiZhAJa1ynSC1cWCAQ79rvOQUJQjptjlCU7dYSzSQzp2eI5HvMBC2A1ot9QzM7dnf7LcM5SehGF912W8M7ldXKbEe35Bmo2AYrJ2S37LF8tnCI9jJxWh3HrU5ki4jc10BVinLSroj8JAbMh3tXLr3Bo1FEKlXLKVBJNy+FDqOBhij1MASWsk0FxdWC5uf2vs3U477iUJt/C+pbtDcTKPYzi+YFmj/ktznkIpxf695L5gQIvPQgX009zPX0ZNBk1tGDzhFhjZuhfiiWRMn2Eb2vnLiWHgJkqAGNCg9OKbe5Gb8o6JcdUtM7bxabfQ+FexDbdWEo1LF74Z+KpGoQtGYglZPWGxlm+OkivKZP7rqJGJhtRRQC7NkFCKF086482q1ay90xaZyyhHQkmSIK6M5eWRc6KDWO3MuACl3oanYLMZc4NwF4ChN3+bjrS56PaGUBoXwUYY7v0m++6DPs3Bv135RsC1pPt5NZ87lF1qpzWZJSHYNTe8qwcSct2LdOrA84ufPWirDI07e5JT4OKberssfQ3xdmcKIRzY6vLNQCOQ1kqcWyDOv2hYN+yWdK1hCYKcTf8BCG+tupbN43cAYJTjdIB2xMUADx53f8K6HD7ibkW3oPJPxaZVbHn7uotnYofjB06pZF9amLahqDE4OhpuDxHimhuQFfVqx7qNyVYdtaQkyjK73nTmVef4dDvXmoXQnHcKkZ9E1L8Lh1BeTaUAtyQfo9KIQJ3gfvjULaVTppG41NIDol8zfpj33EYtCPjOtipPEYx/wKuPBjnDuui2Sua7FxGo0L/yxG1vLEngFYCHWngpLiuCASjy8vO5dG3/tqvrbf3si7NMvJ15BxhPJyZbWsvq1YokhdFX3Fd3ZP1SPstMwd5Mw3/VX1tf4ThybfBZejKfEQQh1ck8MEngPCkGquxqdbc9gw+M4W06eVLh6Kl6CAWLkXWBUKORWgOBXf+cECPy1cM5g3ZLyMJmNtBnxLEYE8dmHeo+6Yg2z2IiezgY7lZpQKj1f1XjyK2lvFebz3yaBt8YZbO6l6MBq8gdx6Pmy8BBOQjtKIbo0aM+ZKC9JYd0FHcVmZIGzh/+7mGm8t0Yjx4VVGhp00z9fHd+TYUqMHYjV+iH0qhtPYv1LDSTwEhv4kAOaULpc3jExkPJrGB0Vw4g1N2RnvgIBBd94yZW2kEtumH/xb7PBfDkdpoOSCEl64thpixj1wB0uDMmlekamNyUQy93m9Y8R6fVftPLOFB0Gg2zY8i9NyczUQdx0HfBqQbK1q2k6o/Fmcq5S+cGPh7IGIKNs/qUXBzMnnKaz/h1s3GD3ex9lyD2UAGuiqk9VhPaI9rwCoA13xB9DDKMdRlL3ll377Ye8B5eAq0S8iGStTle5gmHNtsBpH6PlsxENKv3djNgztGEWvs3/h5t92b0IkqelAV5XGA1aaraqc4j9kIGvJ1L/3BwwL3yjlCesKfz8VK9Fe3LAX5wUamol22oMdCbpPFdEqgQUvQzzhEm1CTv/s3gD6PgeJ+tfRn5sRFY5qz3/LTjUWVxytpllWzlw/QZL941KhD9KfjD3k/xOoBND1HaRnrfGvpGxKwsG28Xjr68ZC6V14BmbP9i8QCTv2RAMeZWhpBnnrk4lHTIn06W4tl5jXPsGl3Kprqpxxxp5oIvkrnm0+STKFTsxUUaY7BlMzjnGfihoD5vcqFpVFtSIazfngnlrTaKuXwYjOuPTbTA2w8lzxUzTeZsyIfKF7EIHQ0DtWF/IWytZsSBaodgP+3Bwi9dPHRvODeNiCwGNZJUlDYPAzeh9u4T4sMgZZhuDiFAI4/PoZWLFBIHfIwQANo5/9XATELVxE54PDpc3BgG1TRNoJtAO6rwFeImWRWsMBWx/mXCDAgdBeNFMZNmX4O60KyKRBUx/r853y5VmaXgky4Y2uV30+38kxrp9FLN4fD9jN7lf4OoEebPRArJ+17bMH+yu+NHhRHauMjUpFVrU9Bmxm2XVnvDMnDSwhAxDrTEEBw0jXggTOI5+jfAX4dKlDxpLofr7OzihT1wU0HRn7aVXIhuapr6uHRg70oi326VAeoVziNJ/dLRuIdo/GUZZaQyOnv3HbiAOr3eGztusQmmyireQECmWbu0b+oXvndmQBktzqZzRYdT0TySq756LSFEVusLdSuOoKRwyAa4AIfCI/kvFdHUwdH4CdodcLvrK7fvff9pv7WJ9ZOs5VIXYEIoK1fExrbkAHx+is5n6jMg3AZnGj1q3zwGYRI6NGtEvOpJ5up0aA0xUB5w9m58bFXb9kAD5IpP+WaVZnKrw9dia4WqRKp2Jaymmavl0Lgcy0oFR2PduK6W8Zq4isIxBLvHQ2FMgTn3kWNUGlwJMENWtdzIY6bfYQYndxQjZa6Tt+t5iDLfdLiqYzSC+0kcayV1SADr6Kwg8dOEXD4K8fzd2imlmVIvRDnuOOgTl5KsfeA3doutVdWUqZQ6dDuPE46ID5cuNqGodlHavPZBhXgdDvQtuFybVbDOlv9Qz9Nz/N6RCLSRQ6d0RREXE6nqJBcQcWdAnvcv/6sHlVfgetQEkJjeLBfNT4M2LzUQ66YFzLjCMMwR7nw57n6X9alzXfe9jo6jK6wPLeQFxmlxb5sT8g9TIQfut+sdftuR5sl/aO/RaSgaPGb2G6L4hyY8zSSaRBAubDWioFhe3iW4nN3VZ8AmAZlUtgBTCjHZyVn2d6jZwM6YCVmvBIlVML0pHJyH5BHQDkKYRyM0h/C6tgvb+GkFZ7IbdTDNLgWaOhu95Uyzr3QrBj5Y1TCiR2d9Urm94aFSG932Y3WExb5STIt9nok1gb1adJ/OiKge9WUyF2KLNBmqI2quju7bp4NzOUVmPCmzVcrxgs28QkkUYzrxf4+pSrkTqro4ylIgYpX8o2N0F0lBdh50KynXKxsfrUG8bG8CRUUAjTJ7IdHSNM9DxWVbN85d8s3YTE54HhJ7tt3331ZlvbYehy0Q8OplWLh3mvPtPxFMn6rcxX/uUH9dgPTIwnnzfdHyWJ6aJOtIkMEoVcAj4WJCFk+tEmEjyD0+dkMkguKPSCPwDLZ6In7oiAJM/tslnTKjqYSgLx3yFVTUDwo5AkFU6qYEuA0jF55PwDTiLXF8J2m2B4SSZzA6HCspFPaAI9y04t6tDPpLLiKQ9X2UbbQ4htcbGIBPb6qcDe7LwQGh4HNJILkl0HrxkcqoNCFBnu0Vik2bSNutn+pKRw6qL8svECGiBzld3aiMGhCnFqqUxL9A9NMAop/zOaSC6y8GmYWLcNMruOQEwEzEsMWw+KKLpDSgLF+WIifQytOz9mwr+CpOoBi71nwY7DKH46AULkiYN1KCtAFFZ/UIse0QJ6z+M2fwd4s9tdR2PatE4ABR0V6mVnm5okTmPv5J0XaHyFEMT9QS2tWXIAxWbcxwO8ZO3Xr8GwxClD6LZsRz0pOlOf6v9u1Zps5ti7g+NU9E7t47qBJRpsAx/kdk+qwC1SHjMJyqb+lpgQ4Rpg0p/SJ5XnGu/zZTjRYQaWudTmbUtto5FCPEDqTJEIaKOrN8mP4eKNCK1VW6oVveUutB4IdJBOnGx8WzTdUyyJ+Oxy4RDNZn1dQJx7vJqHwd51wJQUMEHFDbWUVXu+QNO9A6jaJM1b9Kd91ptSr87r1d9uLBzhqxLUgc2I17WgVlSfkhOq0MOawjp4OagowgX+ijmR06amFmI2nMGUJHRaVYfNnMsOqJQSvYBkscckwBBCxNNPabvslNh5jHQE8DjnkkCxhEVZxQ0whrXd4ww4fkm+RaRkuIXPpoisPMfQ6vcs2ZzCIGvJJRvZsgdaqnhAhjJ/qKOtLGDTUOjnW0OiAK+WZy8WEk43sLB8YtOv9IKpGaoMSzD4tNrONQAhkcWfm5ORas0yVmfg1U53N485dNunVg1GO/Z3Y5lxfnN6bQMcNROwqHia20YTaMKBGm6XbVz3S0F5XbCcKNqZ6/HGFsjEpRcoUfZ9L5GsshwUWIZ6oaW8Li4PeN7ZY91MBUkTW6jyATmuho88KdQeNVgmLBptlK//y9INz8vH7ce9I3ZJ7URF/OVXZjL16ju/H35egCKwDJ31GaQs/QlI5TrcWf58AVdyRXfh9YHux+AArfRddTfNJ8gb83CrbmaHnNdmJ7jlpqGGe255ibNuCtiHbuPneMVNLJE8h7f0qftxBlEiQ9nC3Xdi6LZrMaG73WTod3MDETtDaLVLvc+TBDoOlSy/ojfv+w6iKHHYXWQJCh2rPmSnUXjrasuhetfYZ1+r1SnEdannFS60UUFIvkopw+mJY4spJFhs/JXFwpeJT0Fek2z9JAGQM6PovhxmvGJZyrnc7p4Kc+vuigkMJQHrISivX2JU4L/G8UeVvqGXq9CXrVCvKDzZs1WBMh8A9XaLi6Ez5fnPY/Z5N4iaS21u8gtEmsBt9EdOqF84Iybvzp/Z3zjiYozKgz4zGhcGNdC/SHw6ku+OAv9khtA8FSkeBDh58Z/Pp6JQgpcw63qBTWE3XtxFpFNzs3So2MwN7u4/xoG9v5j/vGLpdiNYBdPO2hE0HXm3HUeRw6vmW9JZFgDce8i3E+Y1AuwIN2+v+pwMGwpMZug0gPCNOP2/8sAOIBJC3WT2W8IHJsCtNsZKJqLzIaTsdV/rY+uB6tMw6uXZ+OamT3tAKUSES+/fZrQ2R+QV06I3k2IrzBp9OOR+rv7eq236Asqe/FVgiDbNhlWSNW5MzKmteCAaH9BgjaohOjgLquFjPeIM0M+X3fxIliBu9jMXXcafGycrCR7jMjSaIX2sW/bJbpvU2UciDlVNmGHP82I3uZD0971cWKoMS/AXZcXEDhSPLDq6tp7hG4akibN/5nIXZliNASsJw8SKznDRRGqRyMNEq/j4c1hXNBI9p/eimH0oTdiJjP142J0TpYDkFFk6V/hUBf/1iIgtMM+ivIeHrvm0SYNw/8iAZyhiwpBuEuN/VdlSWeUVPGcPrfOqP2zMOM6WSRPhCliAIS73boHUth3IQfV8p8ZsLVzGI1PT72YLpYNtbbsnjs0KvQeUblL+sBb+9cWTjd3a8Lx41JubYm6x1T3iLDz9EAnhqLBYnNRi4n+9tQeW0XxRvenBvqaTTmQXf+N5TE3iFFn1ZvtkIDo4UWvAup/mkXR3IXD5cxAw/nb7k9nsHhZdbbGs43cWsPGqAWUMx7qc6n44PU6/xYAHPWiiL8R19QUMjx1veGLBbI6xPi3v0d2GEGxJs+13tpnfGPyfApmdBZaaIurkriQvKdp0pP7QsysASAzjaPGvXv+8EcCHS8qD6xJXm29a/4ArLIUvGifZncvkiTuCiDQQEuurLJkkKIzqP7X91u96fPz6wxX66+jmUasbU+NyVsaeMP5QIxmOjwXRX7LCFlWs7wPILwcUgo7X/JYOUOiR0opLUA2cbUDIOHMRmd5FUTiZSxfrJfnLbesZtHlHQENPeEgqP5pUvKKWYnqclcef3MxL4YdTq9GyPDTuNoptOqG01B4Ltn4n2hWnSisdifwmoTuCIsqy2Qr7o4xhhLnZl3cXxUbN/utfqj/1My+N2LWbw90amJaTzdoO5Wf7KyxuBd/C5ndg9K0zSNRktwjydHEt7ur+0GeNVCRBk3oXgGJ0ZqNwL1MKbDOxi6ogxwmu6fnwvCq680Qoz0nEm+jZxY66iNtxLUygnDTQBglZa3fZCYPi0mOmaNULOKPq5B4guJCtMjHSVwnoWWoHNQoKNzJpxOjxyNKRozCRC3XeeSpdoup9uivLQMq2M0xLy0f9WbMvYOxyhw32NBGCR/+br09+V5BzRu0HX834sTygrnMhzxBff5uzAHZkWr7z4JzNqCjT0ShhBMccsIt8WaCP4vAtfNaawZuYWcsT+9kwuBdLAzQa6eKvXGmo9v8NMYNL8ZTBOOR+oPPVL7TZ3Bl9Gb5Qw6Jvae9ZGVjSnwpPOMURYROHc+AA+7R/jonAAmjel7Q4efdI2p8jsMm7qK2wpQlaLJnyZo5VqG1F6/Uk5T2+ZCJrY/14MYDGGqX7m/tzwZ8hbV3WDksxZJ3YCbaBB6Rs+mAsvFcMoWU7spSaCOIkDO9jSG5rl9e5uAhJ9vtttT2uLTNd2SafORFxZwusb41PlFjyPqjGp5uXGhq0uc9OzHDxas+vRa4SoK9rNjH+nuU0mKq2Iw2lDO+Dvoj2CWfcsaU8/Z5kz7PWmLL21yHKoZPArGEABeWMnUwk8aQ5nWFuM6TpwbL747i6tyUwscSJ/OEvBMSbhqpK6cRhz3ryrpidv52rNl+tWf+M/4FTRVbdkRLochv4nYMtTBRUUDStIUufo13hR/HXuy4UoGfRmENzUcosG/x+H8pQ7K12AwDi/efR+qBjYXJv5gv0lVZPL+/OFTqrVLgZcOrzq8ZDQVC5TyOnlNYcsDCc1sdeRJ7L4c/B65v5o6EjDSerqKhWpvMMmHFlUQXFZnEr+MdHhIIRYYVUjRrpaZCy4GL4mmjkQVHbeBOciM7dnluB77QSiBklUe7U/9wdKcfcRnrK/U+FdmSD+D9WbXOSEK+EQQr96cfYrQ/VATe7xqdSoiJZSW0QYXoycRZRSRrjIGmjsZnYNwZx5vlx6nXcHvRh4uVuDObBM40o0iQPn5XHW9y2D38MjuxluebgiWOzMvuCDMdQlmfRnUjeknhOViR/pMejG8U8QpIYCrsN6Rad+Myod2M/RDIaTmC6jHlegza3s9R/8H6n71RR5OcCyIPxfXzaheSaapHviNEe34vzUUJbYWuMM7tINejTgAKUcvi0OFR+0tle0md13I/zaKHVOBsP/YgfrUwa+VB7IdW3CLABKSGDBxfYraN5gmpOnT5EHz/xleZQSJ3In2P0kzdfzzwOEdlotrQEaJMqeI6kC9vd6Ty20v9tM/XvV7gRKpVIWXcYx+IFLVWu/nkjYP6nl9HmKBzQSinE4L0yO7SIm409zhEcQfdKtpeIMSBSyGAwlITzR57JTGSJ0AVCPn0JydXyLHZnToKLHSMwUkIdI6OXHfy07zJzKCuFCUqA/h78NIXwGHmPE6tb7EnIxZ1EWSEpfRztgiAapqgSP3521+Aey8B+DlxvMd1d/lSynJB0Gc+750SRs6CdOc3WOyuZ+XRiv71T0lGRoAvj8qz0L8OxGCCu/EtKe+hezHMdifNg2pDfTX/WmAZdBnlfwBJc3FCbqOjatSbaYa/bOHt12hwf71sQIa3yVIRFTedJc5Heul1rS1qpHAu2xzD7Oa+ZFpPhblRHf9LallpZeuvqP8t69aQ5ZU+WujXaVWKV5fD1eAiVtfkv7d7l/4qm+FYfmkrv0EGHt3INOIl6wa6oUgxAqIDyxOaISNh/jhci50XmxIP/8xtxRL3hsPJ1YT5fef/WRFJwejL1j0t0WjEo4bR3EH3tv0tpZ5NSkeoCjMVeLpL4e8ZVS+7zG/3tYtNyllCDvUDC7o53OepRbSTIzlgVdxIeXZPkNJt0U4wr1CsWjyE6nJbuP2flGHUnAnusHCyeQqFNv5UycfLkFlmNp/akc1fFXoW/Lf2LuLuVhgxrTwGUDbw60D//PN5ClVRo1IHfFhEWXCDXNKa/b5kCqycJ6Pc0S+Q9HaSY2uS27vNTh7E0xm6ToGKOwIqFkPKf7gcNpkNNfGI/Ysxe1nGkcY8+FprypIvGws1a1fZ/Pd0yt/K2+sQXoyHU29wlO5hCOktKbz/v8pVfQVo8iCeAH/UYRCxPx28rJh1douBAueChDdSRDaEA84iihK4UNIADlFFlSfDrtYD6dNmegRG7pyxDj+hJCxPKH1pfyIMX1qPXsji8vaQLXXsBPa7KWjXB5qFnmRn0oFn6nI7youUqr/bAKT1XQ+QZDtuPaHstl8nSpwaL94khuM++zb/o7hydZgiCvYUNcVKq/0tMHe97krCia51qaYCelGS19tsBMYQ62CFg42vvjvX+/3COvr2RM/Dj7t0jTNlumhV5A+vtIbO15TTsr89KE5Wl/Hid7BiJ+8i7NGICM41N2W6fl5HtrMwRosPcuDbf1jdDx5LNkiKUHYRA6deRBi5ARj9d/lnoQjEAoeq//nJZMAlQJSRXMPp/SSCvKzTkigEqXs1O8AzpnySU4OQm8lgfb6uV5B64VSyTvc8XEKtWay9Dobndxec530MzWMOJSEnwmeqwkF+yGvjeTFqzjJFMg2bIQQjEtS9vTOfkeFesiKVibIrsN3J05kkrQgPTersPSZQjieaOQUBB6zS0zpYzZ1XWVNxWzCWtnbU5g09J5Shd74/GDpUQLyw7jFJcF6nWJ/pMLFQf7JgA/wiyLO64ylktP9mLAIIRoROn1pTsy4o7a/Yo02B5QOcWFkKGMRneywRuYfK/XD4zgduox+Bua8/aKcCnZ/wp+kbwBUs92KbpeLtAShqzcp1tJwkqN1Wcb93Z7av7yzteG1TDRmGkNDOEBr7VAZrnUwoQV9/jTA+X20mZBAiSfG/1CMpxFmcuKJuHKAV0V/z5XeJtEEXyX+j0/r5kJxrXarLbQLZg4BUw+FDPQpdRUmWap5uzTd6jkFUA/L7BcaG+u/QBbH3arlage4RZiiA7BR2yYDxV6Qs/mfMs5oySqxEgBHfHgz5ofVIIB2xZw9Rom8DgvXrHraxDnp/T3vV9prKYrZeCq5IpECsbolrP73LRIrldSSakPNw8FhyAlxUfTB/DvB3VC3iEV1kEhVwUogLrVNiJ9MxDDz2DAHg7SSCHIWFq1LycczNojLgUxE5njjQr+DSJrWa1KAXronVioeznNX/gH26wGAsnTFlUGW3+R3y6TP8e3G4LSx9Zet2bHb23Yh5sSxbcpJIIDRKvvw4RQMZvIs1E8nrnSs+dFirsx4N2WnsdT+Cnb/M76mvX/KXq8wDOwgz0wHnRov71aT8snOwcpQxw/d0o2AD1azmG1J/Hbuzoj/oRvFzamsSQsQjxq2M9Ic9vAu/jTGFz6OQp/sw3WycZM2fjMKNgiGsYsT53+9N6E8up8+FbuvEIZFRpcB0QqKp03G0Zm9aaQBsZbgdzUd4dNhefOs3Xf6FGr3jPLXPVzeQ7Z/2NENvH5IRdJIVbAdcM9YglVrS2BiNYQJAfdLKWCx6QP3CmtRiq5g+hQNLExG88NXQC1HoYz0UhKKe1+wc4AnDc5rQn6SsvASqu9rxSAaNaxH7dLUHrIg12vYkjD+S6Gdj3sjSwU+8ot+FHmB1ET+Se+oqHhEodr7wYGmgdoJfeC57kP75uLtxKe0ZDv6FML87/AYAtPXX5paK5lDmJt2qvUNSuD1ZbywD6wl9PkBt15bcm2+0L/nqJqUlbA6AUzroW5j7fSObWkcb1gTqGmkDT3B2PhYgRbFQO9VRDGiInnskit1EIQcdvR1xdFSHwGX/C6HvwwPyLKcisO4wLW9WymIDAFnyqkxSPnfGW50ikGrRAAdoOMSqbWsGBzX+Q3koqtdtLJHWQRjHncH9A/jHn0MBFF0vnmFQrieZat/ZaGRt7Ih0PlJzJOvdwxhMzy3rOhkDMKxLxGVhQVgu+RCpNTfr4bdh/N2CK2MxBtHfklBe8EIpf1UInZT8yCs8pouDM8mMl4DuWydWxsTNFNDj1qsw0JbaEdIypYozi55BMQ/9oKIJfDYdVVfJxZUkPb/x78/d8v8+xcJg79F/OFp5mbiB7hbVKG66jBViMhRuoooNGDnJe2xVJoNdTSbaVjDC0/7dl9t1NPLa3oBSU66cjJqpAu9mTGHsyRN7m29HYPSTmcupwInxjCA2uBCnYGOCtq9OqesGHulUjGcD5lkZ9YEVinSI62BASTD3h9T7vqTNqAloJFjQmv3o0KNE4YfLfz4mjOpFsqJTpj45f5l8vvu00/MUbB3GaL0vok0G91vQWeOcpYhdCVCrm/pYyA5oyJdLwIoeZG9BEes4WTzwZv84d0DR1T69uohgj5jZ3rUoDC5TA+pbcinlXnN4MJItk0ArGDJeOV4fZtpFYo3Zfs4SqMH1QgSjtWJ+eQs+Bq0Rc4z6j0HvAbgbqnTR19H3a1G1rMcG8SCdqr6cGt/qjXbyEThKqWxDKyS+mZiB4sZXAF+yHJJnieSB2MgYQest2gewk6yobh2j32iLph4wj2x5f0Vhp3LyTHzFThqbB4ltQgxIkNQdsJvxOSiBLqkkBwVXWUz9s7lG7mXVY6ZKNx1OP87MdumEpQ3cLVSNyLNTZGZ7kKUFS1DbIKtnWQ/2Yl7JHG4uaCYpmcQMKYIsgkKwn9brxV3AZUe58p9hcRO+TipiNMS13bFwZu9lK0hX4g3Q168fKwgMlnz5h35DoMnjmAxbaZzZEoL/39c8AxOFoizBSMRM/2HTWrPWhRe1pxYEj326FsKxp/ZX+x3LvbEhyeS5n8AFV4im3nQWOYPm1Bmj9aCWlh9KyvDU1zguDRSLWiuTAxEZ5NA3USv+9i4+fV5D3S4foykunQ++UhJNmr3N1rXtwv1JBw+dm2CYcrSqP7nLM0JnzZEU/xhCxyCwQhDV9JWonFu8HX2BVp4rhaFChAjOxeLOGanNTAgwB75c8qJg2yKJWpG9OJrmhWra2U84IEWO7Dq7v8Pp4kMsbeFPkTsSQxgTNfwuWuqyD60eo0jjOScom7AvItjax/cWPin9WLKM2SPpqdGIRrcgYYSbOVl3gLsqe4kUOxGReievH3pHYID63jC1yzvWtDiWrGSw0biSAW5CQ2KY5uCaBFBXV3gc8IKnk4E+aTGQrqcrg8NElMvEaPI+b2Xb2PA2lw9myoPnxrclPPT5lA4z8nAo9agqCjakYDDLjMD/MYHz/+AqUaR2kquYatziakyAuuEVfa/Rub6Bj7nrCuY6Npizq+QygpXH7fZggcv7zy0EbzxZ0Hco0JJ+U0ojRNKgVE38Srsqfmnw68J9YeErvQoM32OQZ5aMUFQ2TN5pnJJ71vkyn/YZ6u02Ei1TA4s+hhYqlgIdIFmeBHHhnJoovJ3vJ9m2tQa/lLmUFZcN41O8Dq9shb0UlD0tcGqsHv0GKUhM7Ss9B/Lj6cCeEdx7LulPxRpv3ZKLyZKOCg7JnZIrNu0F9aOPVCTeL/Y+JXpeM2V/jMaTfEvCZTjBGWkbzsa3KVGPIvEyyOTAsd+hBRZySQrCyZVIW+unSaseD6J16kLfYafQoi4DeGp5mZcw5O2PMShPCAHItXMvuAVAmdpMOOjCcLNu06Rnyi0N3K1ixXNN4Z89b0sqjBwvPrTS+j1IY9NNpAcr7Nj/0VADwoMBb27eD8FZhqk8NY1Qo1D/Xvvh4Zc5eLh02r19+a7r8/3AJMH3y7vOZVCDfA6k51exkCBFKhg0yRKaWt2IFi4sCbzNA31HnOrJGBHO+aS4jzO3pioJJSgABvZQVNd5zPCAggp2IxX7OVm3N0AyCR+X0s3ObuOEz65syeO0Tv1lOrSQujEBvmJkAhZxvgZX/1MuHcoqQcPf2wwAvVtdnK7HT91V/2ex9IF0AxCA8A5G5O22+t+4W1U/fIiOvLXVr8OMiyYjkNHqW9hZnquFaR5SPtnkdQ+/vfVLZ0YWKVtcP5LxIhH2FPl3QpriintB35UPUGaL8WIdErnkyJPQnYfR+SWoVAny2uJj14jnkPS1F4l+/SXTP8m/7z82NwVxG42GB4SgmNQgfX8i0/ltkS2fowLYTjsw1tsg33GCa7bRqYoVbVnkcZzpTs7+M1HKEszmUbI8HWx5HuPs2U1OaNL5ujP0Dy+uzHMFHVsFAAkHAd1EXkKgQBU2HYxzYxT2YFevx3AVqg7w4Ls5+UhmH8Aps+b/6hqrIT5lRwjRgzjnE0b2TASUDHV0EjcVVdHV/iWocJEt5Pe2LwjP43hT93YkYyhJl80KjFOm+SnZgXgr2ISPDWd7HptpCjbfzicSq2UHsqaldvvigfg/5vpNk13mfCDGNxPHAxNBvNQ2iA6m6LTPLhhPWA8YSgpKkwLenX+LAHlpwvCqTY4LrloIZq+s+3CvVza3MzrlHw3ItZm2D6ff8nx9pblr7GIlnsQGPX5x9OO0ZHLMls8r3eVT/vy5azZPvYj118A3bY54HHjkD5Ic5GQLV3mCONXtJNu9geU8Vn8XPLhyB3xjJ7b2PgGmc1EAvdHWet9KXNmiuwag9B0UxTg2YVREdZQsdrEiVaaeDjMxR6IJMGImrf/57hXcyhCMjgTUSoG6A80BBPhX4BRdIaBdSlkzYLMsJtwcW8TqvPXpqsiOSlFRg6tx1hKKesxbMMLJ8SvYpEJkN7GFdTVLWuUN92HDcjOPxkrTBHtNA+MuBawSeIZsE/HAjmXFdniU0gHSfrQLlacCUBK/K62mQIFpa8lCfckVFeGCRjIuEUsieRB/vT/xuH1ewsm2L5DwLzvDabSgnRc6jDq6H1Jk3Tmja6mrUzheiHp4ujx6WRRJCmddRmqEfXbrCv01zPB0oHEv2yIKcYdbNsrY0Z8Oc4WrGW1wYD+BQJdYfYK9V3JkNz0eOICnWAgMKso3spTNAPWs4GIfG3bPIJUMgYdEAB4kXhvN/bjeRUz1FCi0jThQdmm7pxszdcOMFM70WrIjslL348gSt2ypokda7YYZojpCP1oSdQiJj4YO//X/9m1NYkZ0poK4nrwgkmBKuuxS/EWS4aBUKA17W1zwQnIBOjqTEh89rIL9UDyM82geivJQam+Hz4p42U6NsPeV2iC6p7AZMBFo02P6gli9dGRAPUSlOCdj0RU0pcbV0e8Yotw8ETgUSaZvwKNNCMX+6P/ogE9i4bxNnHTdWrQ3lMQUI85YsD1g50jDp6ss9qE/mmFX6oWM7zGv4mT2g8nvn2dUInbJB2vnFvswIfEMMHVGKYWUl4r3DllFW07vWd/aHOaxpa9TymhH5kGMXOxCaO2V5ZxRl0K0xABmbelFEFCBiiX9r0KlYQhC1JCNdeQcSGRAWnpZ44j0j7A6ICSPkZG7Ap7+Ipdpvk/Ss2mgj32fPVz/P3a1r8DWg6qPhb1lTYh/5jpr64bNq49AVqHE3uTgHmZbkmv3f3S9BHedd3n2OIRk4kkbaoOJoy613nMLSGRwNMU7F6uPXd2pEevPc5SYtkHKKKRaF1WMx24jrhHhZpIJjbLf4UVkgNSlUFC/J8tQ73eNs02vZf8ijyf3d4hCGwsdQR7lRuVPBvn2OKyB0sJjKAFuwyvTe0lK/NBNEHVLKEPCJMiDl0H8RSGIDaCiZOj9gVBNvecL/0B2kaWl3tyKAR9k3N61FltuQDWs1F9tYckx71Mjt0dLXla9dS8v1M4ahGe0be7OtobwHkNsFhf1f+HhhJvf2DX+5bZt0ed+hbk+fDh78dfvtbQWz3ZIG9Rwc0pRnf9DEwXk8EgaNe6u2xecr4oXvBMfNmXR6QyEKFEKQnHhLQKnFD4TPNYlVrnhtRK32pcFaHskyVxyOo40xoXA+UFGpsAcs58w5PgXuHKuLYb7RVRAtUmxxPO7tc0qtHnEkRP5bzj3jnR8zJeAq+Ze3k2q15UzOwVe//HdgMeHqjVNS+shFUy2dmQTzD/IgmD+qhCJxDE64ke36yaNBO/tADjqhwcp3B76kqOpHOpMjjYxpHB4WC4045gCpgqybC7m+3ZnLtzfXOHMCWjfZxVf4QHwt4gFzZNIUWRf1K3s8N5nvx7qMIWSyD7ZmSNhWnPRZxp/4Pbv4pbdcqdByGRltSP200bH+KRGj4oClAvz3q2bbk+kqHD7xuklH4Dlvw8qFJG+Lgk1nWGSXPXkS4G78BErApSR1aWUdykU0qBnfQjH9wwhIgXXQVnO2dJ+r5lKIigtvnyF3SckXNopmYQv3VdRKMgcK/6RxA8WlTMKcq9uI1ir3Qun+HxOeli2WPayH2nT0DlGbvD61jmAocWD/aQCR+dpUPFvXz2CwDWsu8008lSc3CEytgViumttHEW4AvBeKMGPoFN8p+eIs2SdX0D7Nh8GCJsBQQjfntQYUalUYqMA9fd1imRCnlluKdMOt+dBfBGyyoVh4qWxk2olbB/d8KEsgkoPfCKh7nfrf/eeWyaK+orLqby5S2XlEwZhmR5tzL0Yg00YWQEz9+SSixPrSkTlw/+RXN1ZOT6v3oca/fyhpQo1aGidLRXTFsVl71ZgjdxAgAgQMT5o1mrt4/ZBLxe4nHiakepJrEvsZOldUufu8T5vdhvKlt+yyn+maD9RFhs476bUGHfzh5d5lz2Fm5VEs0gHJNBo11bW1pGmco6bAgwT4B08Tno8O38ZA58wgnz0V5fUzR5c78z5VVvdV1Zi8Jnx601MVrQFR10/r/LFfW3AW6/FQBxsaG4LksKa+H/nJFt6C17UVpbrJd8dEwI0qx2YrgdVfLDGcQHbBR88vmzapeOz0gCGP8j00dNLqNUPwoChUDx1KecRL1gPVkKTSRilSKXSrFDD9AZUTT4LyGD2bnmfqZyY98Rb5JzCGyG/TEYT0nE1aI5qgvpHBNaMjej7ZJaaig+QLN/emYzPV20T+GvvnFAbgYLcwxD5WstvWXat62oHAsjdCqvgDBEwSk9/LvFfdjL8TYacTkQ2fXfP38dulCZp2eQFYvX9qZXBgcP1tcwVb/EGYTtrRluieGck/GKPAJ+VcpVlZtlGZwPYzrUq1lgWtnuRDwkgEHu0LpZ8YT8B8VZNUjlyrC5QqQD4qF7LSO2DMryw3Uoot1GpLbfdN2bugJSgGyeQFsbdhKm+Hdrqfkefzf2KyM6qcAwKuGL8HCfqGChWa2XspiJfMkhOPRtnIxADzrpuhvvvRpEcCi7rVldJOPLVbHCMKOqtE9057OOj2tPHbIr3qhezLxKNp3bQTmJIOa1rtl77/7RSfFy1W+TLi7Pcua7BoT/ye4d6O5yZjnSXdiv6TEzY8nyXjeEH5hluVB30UTtNIOWdwf1ARY0e5Chh3npVGAJFy781hiZrfITvUqzX0ZpwQ76x6W2ujL7igtxGLCZBUb9G1P/HDVdfWIJLlyKOPZDyfwHxE0TwwnzbcEk5NVdqJwplrvgPE3O1myi3ZA4SB034/zxw8/C9TguVB+7LLI9HmTkCqyr4ET6f0zAOCz7exhFYY+E8gu4dTUWQWxmbs+PXPeAAv//eSvh2lXaAwbNDD8qLe5FfHoZTkELsiCDNgXLZCF76asDSMsKxOj3Lt7NNO9mYRsLzZUK3qak9CJUp0as8wJ7avS6Sl4vOSCMDiPYDMg+CBZ4lCsOWYv2+RVYsvaaWTmba06Q+qv5I7GjiPBUgDhywvvW1e39f2VErLEz3DUcFLX5MZCYpcb+IZXI5j8Z/c2RjRhO1Zhd2qutPZEclELSkDCA+gatrwuij+02wPeuwGg+Aanhanu+ar/m0Y88YLuavb2ndoiOh9ZtaRlgB2uOWiGUbTxwhgjubstHKUbkF7XJJR2D7ssPpkLxAHJzfAKL3NIBAlfF2zR6nfNxQs2Y0IGhdgm8dELDSvIHO+oZv693zyVnC1+c/flhSj+3J+ZEZzH5d4nqkXvQxeA27/CixAELa0N3qpNcjF44kyIal/KxQgMxFk6iR6vozyD8ZzMeZYFidcV+tJJx0fgz9ksiajrGkz4yuXmYWcLeZtvmJoneEjQzoXzYS9/LNiQnRruLzxkCDFWWbMLTDSeDOMS//413UMMuZCk2YShvO6ogTliWW/cxyig/XOXMmFmIPd322ryDDdAE1lC5mKKwxue5fPkIC9StfglPT+tD495S3OnIPdcSTneOlw/OdSyfVp/ESaD/K0oqlXMoKtpqAhRqZNyCINDB+Xv59yH2uH/u9ELHzst6B6Ar/uHxfqRd+hua0V2c/YSBtALcJkJIo5bTWwF2xJCcK1dp5RSpqCPkQLuSl5a3KGqXohxlUmJs/5FRmr5pGIJo4e4qG2WJ9ZNHGQvo6memTbc5yIpVQVv26WwZvouVkXG9JduioOR8sS2o9rat/kwomV1fKlq3rEU9NoID2JZJZgEZYtrGEU97BssuWl/7HE2nLp0zTuIWvijkQ0sj+uRg88YkvbtfqWdggYVNyGM1e8l3+yjPKDRZ5FPmTpE4GTucnGokodO7Avj6aBifPZ1mxJGxp8Dl2qxD/JbJeUIeN7SQOxUvNA56fke3TX0ygMZVzX/w2p0X4rOTycicCOAQZ/7Xk/Py08RPD3jlvpYSyAnL8GCbs+0dTqGDnI7zYLNYMmd3CPYoku2krjpdIYbdkRWrSBXvXFmkWqb6c6iCVcUWulB/1biOI0ytFtnMMc+4ISXy+QtlbUb4ur+eOClP43ZMlnHbQ9D60IBzzWBhmbuvPIJDh/YX5L+yMYIdsb2z/27atPzm84N5+oUlPAPEQeAMIZHXybHK5ux78lEp2BN4Ty/z59iQuwN0Ddf/MdM7VylaB3250dX0v5luZ2KjL8KlCnPxD6IVqvT/dY4GIyQozFHjjCxmQ5yI0jFdwAqx5tEoZ1AKtqfrmoGt7JCgzx9Ao146wNsxegemrydn02NTRbUFYtRBokaaWxQqBsy0G5CiX7xcVMQ0JlcG3n6e18dy4dok+XcLrSw6FjUAZcLdmyhpAtlZdtxz0CFhxAsnR+2EwP32tD57vl0e4pdySwqZE68cooJuIarZsxvkdn62fh10cH7/EX3cCduAE8YArLCQXt95cneNsjuBPDLQIkBlsGw2XyJOmLIACxsmqGEtimOxsZ+PUxOB4wgBjG3e+MhXRiYt6LIj189S3GQhZt5CFp7zhaCNyUCWKSmT2dMz+906fyhgfouOzqzjV/G2UdhHGxWGuZ0InSxIe+4n2vbT1fL+b/mo2uum0lkV+p+QZZrFfStkBvx4dzjyFop7gkCCm5f0QcCmnmrdZSMXXHDIqC7Pveg+udkYYe6cHx+aX/KLekQ79Pg0X+f6bxL+Us/k/3f+gKnWricn2kI6bWzdj/vcgHhyiZkRUOtBvG7dDJcO3J2RT8HEFBWHSkHyI/k+nMqfeBJJ1J6VVTCIEYkpiJFQnXl6ZTpuUrjPzTlHVvagp++Rlqtp+RkVloYSzg6LatgVIAqv6in6kme2wKPMWvYD0/22c7P1eCZQu9Nh2ZSDH5q1CTGeNj/DPoBbaqXswOLrvn9pPtNvYxmAEuK9wMLGufi8IooCG/Jnbc8DO9IO2JaGxtnGOEjkxKDKhQCDnNUHNXA648yVw0nvc837OEzPWIURGOhJpUH8tu1QMOiUith/uWD6jY4q3a4N8C4g1S57ljIhVCmy6C6DxbV6Ch57wjSTvqCCpL1upPkoVBasGSaIr4ZoJdb6Ho9R0ygVaNRxj1rvP+A58DDMlCYufZDFkpjivVE9HgLtpbrNF4ntP53ggIeaDkIcP30X6IM+NXoDi4kEAS2nwtcOfflYcfgsAqNsFLSewZBHuhW7hT6AmZ5pMnmKydtgi4kJk2EMEx9tQDOYfAUTosKIGlt3PbZHJUOpJhXYRVGpuWtgIN+qKLfGnC2E8Z8NSftPUcD8BIeiDcodDSM60YvuTRquRoHNq8sKjUkT9c2TVMUIX1ZvVZ4juSowLEQO9GUnmKC7+f6v7WvHGz3f+oYovGWmplGueKwBOHGgOQnnawPgAc1IH5l9ZFZTK7DpCz9r9uNkS64Yt0YwAAuqKjBwipz+ogJxI9LHIGZABF0EnSFf8STCBFovUcnsqcJodjBaXXJbC+Fu4HyzzYbeJsAId2vxt3vVZfDn7e85vG+5OBQX9FoRnNNeLsBPsyvLFY40eI7PvFrzIMwck0Zx5/t6Vipg6mCeW93Jx0b6lpX3a5rIrm6Dti1AVX6SD5erEPx2hAz77qvVfOv9/FN1IV01Tlze0MvxcU0Rhox2yyZhPCekOFyaDyYyEhEZzzbOf+/A7CB5ar9IFbeVlMJQqJw2O2XrVi0YRSGdbV+telc70z4WNFb70R2EoYWt+qW+yBjXn/w9nJ4g61AgFnQ997jhWldwN1JknuPLyHwzt4UIOjnRGX9HKwrTqKTsMPY5Ybo3sKrm5L5FUDScDMMSIQWZqdfd4zUwOqLH/rmjMrlMPA+73zepQg+9T1vAsb4aOOi/jhOMO5Jz2HhadhEZuUM/05x7CUDNHK/hYZpgJRyWnvZLgNWHmah8RBHQPbG64QncrqP2FH+g2lkMgF67pIiOb90FOJron/6Bx+YhiSY8ON4QYb327ig3n68MzVMwPpQngslVySfCMgjU6UQ7zVADyLrDQ5PbbrF8pQnfgbpi36v0Bmr7pq3JxsKgG6ZPt1nJLID1EEWfYeV7PQo+RT0hiwSETs7ju9r/CxcesEUwwj2lEorLDKcAfzpEe0nNmeEwg+DeNZ8b54aBBAEPFD+xECWXXdY4kgpyz4nFvulFWCRnTOBxa4LCoLadTaX8X0AbMTSxUFiftqeok9O6Jp9rKL5S5O+4WL1BCBe9ry9m0/xoeFgMclyohLGSu+kq4vHtbHIr87LDsn/zAb39aefWV7QovLujGRGsBO+E/wjgfCSKIIDNUNh2CRHfXLkVKXZuNyUP3FJVFdNwI8mBOFDzUHKHC0OasdMg
        - #1:
          - type: tool-result
          - toolCallId: 29o31bN4wUUdrOo2
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: MoSAtYcKdrEVZrQd
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.