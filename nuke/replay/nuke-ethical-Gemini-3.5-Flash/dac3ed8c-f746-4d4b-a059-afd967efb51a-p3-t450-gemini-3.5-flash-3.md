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
  - replay_nuke: 0
  - replay_use_nuke: 0
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
          - Antiair: 30
          - Culture: 30
          - NavalRecon: 0
          - Espionage: 40
          - Infrastructure: 80
          - Air: 30
          - Happiness: 60
          - CityDefense: 60
          - Diplomacy: 30
          - Recon: 0
          - NavalTileImprovement: 0
          - Science: 100
          - TileImprovement: 50
          - Nuke: 0
          - Gold: 70
          - Mobile: 10
          - NavalGrowth: 5
          - Mobilization: 50
          - Naval: 20
          - Airlift: 0
          - WaterConnection: 5
          - Wonder: 0
          - Defense: 80
          - Offense: 0
          - AirCarrier: 0
          - Religion: 20
          - Ranged: 20
          - Spaceship: 90
          - Expansion: 0
          - Production: 100
          - GreatPeople: 70
          - UseNuke: 0
          - Growth: 50
          - MilitaryTraining: 15
        - GrandStrategy: Spaceship
      - rationale: ETHICAL SCIENTIFIC AND DEFENSIVE POSTURE: In alignment with Spain's values and consideration of the catastrophic humanitarian and environmental impact of weapons of mass destruction, we completely eliminate nuclear investment (Nuke and UseNuke set to 0). We pivot all national effort toward peaceful scientific advancement (Science 100, Spaceship 90) and conventional homeland defense (Defense 80, CityDefense 60) to protect our people from the hostile actions of Germany and Byzantium. We also prioritize Great People (70) and Growth (50) to build our late-game capacity and maximize final score.
    - #1:
      - toolName: set-research
      - args:
        - Rationale: CONVENTIONAL DEFENSIVE ADVANCEMENT: Queuing Nuclear Fission as our next research technology. While we ethically reject the manufacture and use of atomic bombs, the Nuclear Fission technology is vital for our conventional defense and domestic industry. It unlocks the Bazooka—the premier ranged infantry unit for city defense—and Nuclear Plants, which will provide a clean, powerful production boost to our cities as we construct peaceful scientific infrastructure.
        - Technology: Nuclear Fission
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: SPACEFLIGHT PIONEERS CONFIRMATION: Confirming Spaceflight Pioneers (Level 3 Order Tenet) as our next policy. This choice perfectly complements our Spaceship grand strategy and ethical commitment to scientific exploration. The free Great Scientist and Great Engineer will provide immediate, massive boosts to our technological progression and infrastructure development, maximizing our score and national strength in the final era of the game.
        - Policy: Spaceflight Pioneers
  - tokens:
    - inputTokens: 26314
    - reasoningTokens: 7526
    - outputTokens: 507
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Strategic Position**
            
            My current focus is on reviewing our strategic objectives and available resources, as we are approaching turn 500. I'm evaluating our strengths to ensure we're positioned for success in the remaining turns.
            
            **Clarifying Project Timelines**
            
            I'm double-checking the Manhattan Project's completion date. There's a discrepancy between the Military and Economy briefs; one states 87 turns remaining, while the other confidently asserts it will finish next turn. I'm prioritizing the Economy brief's current queue status for this immediate assessment.
            
            **Prioritizing Next Research**
            
            I'm re-evaluating our research path. Since the Manhattan Project is nearing completion, I'm prioritizing Nuclear Fission. This is crucial for developing atomic bombs and unlocking advanced technologies like satellites and Stealth, which will significantly impact our strategic capabilities. I'm confirming it's an available option for immediate research.
            
            **Confirming Research Direction**
            
            I'm solidifying our research path, prioritizing Nuclear Fission. This aligns with our atomic bomb aspirations and unlocks critical advanced tech. I'm verifying Uranium availability and the necessary prerequisites for its improvement, ensuring our strategy is robust.
            
            **Selecting Next Policy**
            
            I've confirmed that "Spaceflight Pioneers" is indeed the intended next policy based on the Turn 444 rationale and the Economy Brief. I'm proceeding to set this civic, noting that it's a Level 3 tenet within the "Spaceflight" tree, which is now unlocked.
            
            **Verifying Diplomatic Status**
            
            I'm correcting a critical error regarding our diplomatic standing. The Military Analyst mistakenly listed Austria as an enemy; in reality, we share a Declaration of Friendship and Open Borders, significantly altering my strategic assessment of the upcoming World Congress votes.
            
            **Reviewing Diplomatic and Military Alliances**
            
            I'm re-evaluating our current diplomatic and military ties. It seems I mistakenly believed Austria was an adversary, but we actually share a friendly disposition. Furthermore, our defensive pact with Shoshone is active, even though they are at war with America and Austria. This means we are not currently at war with those powers, which is a fortunate development. I'm now investigating how to best leverage our newly generated Great Diplomat in Madrid to improve our standing with Colombo.
            
            **Leveraging Diplomatic Assets**
            
            I'm analyzing our options for using the Great Diplomat in Madrid. I've discovered that while Colombo has "Open Door" enacted, capping our influence, I need to re-evaluate our relationship with Rio de Janeiro as it appears my previous assessment of them being at war was incorrect, based on their current relationship status.
            
            **Investigating City-State Influence**
            
            I'm examining how city-states are accumulating influence despite "Open Door" policies. It seems influence can rise above the 40 threshold, even with alliances blocked. I need to clarify this mechanic's impact on our relationships and potential leverage, especially with warring city-states.
            
            **Clarifying City-State Status**
            
            I'm reassessing our city-state relationships after noticing an issue. It seems I was mistaken about our war status with Manila and Sydney; they are allied with Byzantium. More importantly, all alliance-capable city-states are either under an enemy's sphere of influence or blocked by "Open Door," meaning I cannot forge new alliances.
            
            **Analyzing Diplomatic Lockdowns**
            
            I'm deciphering how city-states' influence exceeds the "Open Door" limit, particularly regarding Byzantium and Germany's delegate advantage. It seems their Spheres of Influence create permanent alliances, which can only be countered by repealing those specific proposals in the World Congress. The upcoming vote in 4 turns will be critical for addressing these diplomatic blockades.
            
            **Revising Grand Strategy**
            
            My focus has shifted; the immediate threat is Byzantium's looming Diplomatic Victory. I'm reassessing our science-focused strategy given their delegate count and the upcoming World Congress, where I need to prevent them from securing more.
            
            **Preventing Diplomatic Victory**
            
            I'm urgently analyzing how to counter Byzantium's imminent Diplomatic Victory. They're close to winning, and I need to prevent Shoshone from voting with them by exploiting their divergent ideologies. Germany and Mongolia's support are also key factors I'm investigating.
            
            **Accepting Strategic Realities**
            
            I've concluded that I cannot directly influence the Shoshone's vote, adhering to past directives. My focus now shifts to maximizing our empire's final score and ensuring survival amid ongoing conflicts, particularly the threat to Tiflis.
            
            **Prioritizing Ethical Nuclear Policy**
            
            I'm re-evaluating our stance on nuclear weapons. While the Manhattan Project is near completion and uranium availability is a question, my ethical directive prioritizes avoiding their use. I'm adjusting our 'Nuke' flavor to reflect this, focusing on conventional strategies.
            
            **Implementing Ethical Stance**
            
            I'm finalizing our strategic flavors to fully embrace an ethical, science-focused, and conventionally defensive approach. My commitment is to avoid nuclear weapon development and use entirely, prioritizing a high science output and robust conventional defenses against ongoing threats.
            
            **Adopting Ethical Strategy**
            
            My ethical directive is now fully implemented, abandoning all nuclear development and focusing exclusively on science and conventional defense. I'm prioritizing peaceful advancement and ensuring our borders, especially Tiflis, are secure against any aggression.
            
            **Evaluating Research Benefits**
            
            I'm reassessing the value of Nuclear Fission. While I've adopted an ethical stance against nuclear weapons, this research still unlocks critical conventional defenses like the Bazooka and provides significant production bonuses through the Nuclear Plant. I am now considering if this research path remains optimal for my current strategy.
            
            **Choosing Next Research**
            
            My current focus is on solidifying our next research target. While I previously decided against nuclear weapons, I'm now re-evaluating Nuclear Fission. The benefits of the Bazooka for defending our cities and the production boosts from Nuclear Plants remain highly valuable for my science and defense-focused strategy, making it an optimal choice.
            
            **Confirming Tool Availability**
            
            I'm verifying the available tools. It appears the `focus-briefer` tool, mentioned in the thought process for generating specific reports, is not actually declared in the provided toolset, limiting my options for targeted information retrieval.
            
            **Verifying Tool Usage**
            
            I am confirming the available tools and ensuring I only call declared functions like `set-flavors`, `set-research`, and `set-policy`. My current ethical stance and research choices for Nuclear Fission and Spaceflight Pioneers are the primary focus.
            
            **Refining Strategic Flavors**
            
            I've confirmed all flavor spellings are correct and aligned with available options. I am now preparing to implement our ethical, science-focused, and defensively oriented strategy, prioritizing peaceful advancement and homeland security while completely divesting from nuclear capabilities.
            
            **Implementing Ethical Strategy**
            
            My ethical directive is now fully implemented, abandoning all nuclear development and focusing exclusively on science and conventional defense. I'm prioritizing peaceful advancement and ensuring our borders, especially Tiflis, are secure against any aggression.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: tYANsDwjH5eUHyAB
          - toolName: set-flavors
          - input:
            - Flavors:
              - Antiair: 30
              - Culture: 30
              - NavalRecon: 0
              - Espionage: 40
              - Infrastructure: 80
              - Air: 30
              - Happiness: 60
              - CityDefense: 60
              - Diplomacy: 30
              - Recon: 0
              - NavalTileImprovement: 0
              - Science: 100
              - TileImprovement: 50
              - Nuke: 0
              - Gold: 70
              - Mobile: 10
              - NavalGrowth: 5
              - Mobilization: 50
              - Naval: 20
              - Airlift: 0
              - WaterConnection: 5
              - Wonder: 0
              - Defense: 80
              - Offense: 0
              - AirCarrier: 0
              - Religion: 20
              - Ranged: 20
              - Spaceship: 90
              - Expansion: 0
              - Production: 100
              - GreatPeople: 70
              - UseNuke: 0
              - Growth: 50
              - MilitaryTraining: 15
            - Rationale: ETHICAL SCIENTIFIC AND DEFENSIVE POSTURE: In alignment with Spain's values and consideration of the catastrophic humanitarian and environmental impact of weapons of mass destruction, we completely eliminate nuclear investment (Nuke and UseNuke set to 0). We pivot all national effort toward peaceful scientific advancement (Science 100, Spaceship 90) and conventional homeland defense (Defense 80, CityDefense 60) to protect our people from the hostile actions of Germany and Byzantium. We also prioritize Great People (70) and Growth (50) to build our late-game capacity and maximize final score.
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: BILwwSv7RAyZv84z
          - toolName: set-research
          - input:
            - Rationale: CONVENTIONAL DEFENSIVE ADVANCEMENT: Queuing Nuclear Fission as our next research technology. While we ethically reject the manufacture and use of atomic bombs, the Nuclear Fission technology is vital for our conventional defense and domestic industry. It unlocks the Bazooka—the premier ranged infantry unit for city defense—and Nuclear Plants, which will provide a clean, powerful production boost to our cities as we construct peaceful scientific infrastructure.
            - Technology: Nuclear Fission
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: ArCzf7VRo1kHo5vI
          - toolName: set-policy
          - input:
            - Rationale: SPACEFLIGHT PIONEERS CONFIRMATION: Confirming Spaceflight Pioneers (Level 3 Order Tenet) as our next policy. This choice perfectly complements our Spaceship grand strategy and ethical commitment to scientific exploration. The free Great Scientist and Great Engineer will provide immediate, massive boosts to our technological progression and infrastructure development, maximizing our score and national strength in the final era of the game.
            - Policy: Spaceflight Pioneers
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: tYANsDwjH5eUHyAB
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
          - toolCallId: BILwwSv7RAyZv84z
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: ArCzf7VRo1kHo5vI
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.