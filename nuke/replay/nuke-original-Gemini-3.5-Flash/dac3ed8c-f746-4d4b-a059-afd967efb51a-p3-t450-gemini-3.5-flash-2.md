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
  - systemModified: false
  - messagesModified: false
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 100
  - replay_use_nuke: 60
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
      - toolName: set-research
      - args:
        - Rationale: NUCLEAR DETERRENCE PATHWAY: Set Nuclear Fission as the next technology. With the Manhattan Project scheduled to complete at Tiflis on Turn 450, obtaining Nuclear Fission is the critical next step to unlock Atomic Bombs and Bazookas, providing Spain with ultimate defensive deterrence against the overwhelming military forces of Byzantium and Germany.
        - Technology: Nuclear Fission
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: RIO DE JANEIRO EMBASSY TARGET: Increase priority from 0/0 to 90/85. Rio de Janeiro is our highest influence peaceful city-state (511 influence) and is close to our borders. This extremely strong relationship makes it the prime candidate for our newly born Great Diplomat to establish an Embassy, granting us +1 delegate to help counter the Byzantine diplomatic threat.
        - Private: 85
        - Public: 90
        - TargetID: 25
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: BRUSSELS PEACE ENGAGEMENT: Increase from 0/0 to 60/55. Brussels is at peace and we maintain Friends status with 145 influence. This priority encourages the AI to utilize Brussels for trade, diplomatic units, or Great Diplomat missions to secure our position.
        - Private: 55
        - TargetID: 26
        - Public: 60
    - #3:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Happiness: 60
          - Religion: 30
          - Production: 100
          - Diplomacy: 60
          - Infrastructure: 70
          - CityDefense: 70
          - Nuke: 100
          - Growth: 40
          - Spaceship: 90
          - UseNuke: 60
          - Science: 100
          - Defense: 85
          - GreatPeople: 60
          - Gold: 75
          - Espionage: 50
        - GrandStrategy: Spaceship
      - rationale: TURN 449 DEFENSIVE AND ATOMIC MOBILIZATION: Adjust flavors to prepare for the nuclear era. With Manhattan Project finishing at Tiflis on Turn 450, we set Nuke to 100 and UseNuke to 60 to ensure immediate weaponization and defensive usage of atomic bombs. We increase CityDefense to 70 and Defense to 85 to secure Tiflis and Barcelona against German and Byzantine threats. Diplomacy is increased to 60 to guide the newly born Great Diplomat toward building an Embassy in a peaceful city-state (Rio or Colombo) for a critical delegate boost. Spaceship (90), Science (100), and Production (100) remain maxed to drive our long-term scientific-industrial development.
  - tokens:
    - inputTokens: 26278
    - reasoningTokens: 7677
    - outputTokens: 505
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Standings**
            
            My focus is on understanding our current position. At Turn 449, playing as Isabella on Vox_Deorum (Prince difficulty, Standard speed), my score is 1567. This is currently the lowest among the major civilizations; Byzantium leads significantly at 3828, followed by Austria.
            
            **Re-evaluating Victory Path**
            
            My attention has shifted. With only 51 turns remaining and our score trailing, I'm re-examining victory conditions. Byzantium's diplomatic lead appears less insurmountable now, with their delegate count at 40, requiring 44 for victory. The upcoming World Congress vote in 4 turns is critical.
            
            **Assessing Diplomatic Thresholds**
            
            I'm scrutinizing the delegate count. Byzantium is at 40, needing only 4 more for a diplomatic win. The "Open Door" resolution, active on key city-states like Colombo, Shanghai, Rio, Brussels, and Luba, prevents any major power from gaining an ally. This is a critical constraint I'm currently analyzing.
            
            **Investigating Rio's Status**
            
            I'm digging into Rio de Janeiro's allegiance. Despite what the military briefing suggests, the raw data indicates no major ally. This discrepancy, particularly regarding the "Open Door" resolution and Byzantium's influence, is the current focus of my investigation.
            
            **Calculating Delegate Influence**
            
            My current thought process is focused on deciphering Byzantium's delegate count. Despite the "Open Door" resolution affecting key city-states like Rio, they still hold significant sway with 4 major allies and bonuses from the Freedom World Ideology, bringing their delegate count to 40. I'm investigating ways to counter this.
            
            **Clarifying Victory Conditions**
            
            My immediate concern is the true victory threshold. I had assumed a World Leader election was imminent, but it appears there's no such proposal for Turn 453. I'm verifying the exact delegate requirement for diplomatic victory and the presence of the United Nations, as this significantly alters my strategy.
            
            **Resolving Production Data**
            
            I'm reconciling conflicting reports regarding the Manhattan Project's completion. The discrepancy between the Military and Economy Briefings is crucial; if it's finishing imminently, that significantly alters our endgame options. I'm also reviewing our current research path and available technologies.
            
            **Researching Nuclear Fission**
            
            I'm excited to discover Nuclear Fission is available! I'm now confirming if it's already researched or can be set as our next technology, aiming to initiate research on it immediately.
            
            **Securing Policy Choice**
            
            I've confirmed Spaceflight Pioneers is already selected as our next policy. This is ideal as it grants us a free Great Engineer and Scientist, crucial for accelerating our spaceship parts production and securing a victory.
            
            **Prioritizing Nuclear Arsenal**
            
            I'm recalibrating our grand strategy and flavors. With the Manhattan Project nearing completion, I'm drastically increasing our "Nuke" flavor to 100 and adding a "UseNuke" flavor at 50. This prioritizes building nuclear weapons and their deployment if necessary, assuming we have Uranium.
            
            **Securing Critical Resources**
            
            I'm currently investigating our Uranium supply. A crucial tile needs clearing for a Hacienda to access a node, but I'm simultaneously exploring trade options with America and Austria due to our strong diplomatic standing and ample gold reserves, ensuring we don't lack this vital strategic resource.
            
            **Analyzing Diplomatic Shifts**
            
            I'm currently trying to understand why the Shoshone denounced us, especially with our active pacts. Simultaneously, I'm evaluating if our Great Diplomat can be used in Madrid despite the ongoing war with Spain, as this could be a crucial diplomatic move.
            
            **Investigating City-State Alliances**
            
            I'm focusing on gaining influence in city-states to secure allies. The "Open Door" resolution is a significant obstacle, affecting Colombo, Rio, Brussels, Shanghai, and Luba. I'm now investigating if there are any non-at-war city-states outside of Austria's influence where we can establish a major alliance.
            
            **Analyzing Diplomatic Gridlock**
            
            I'm currently assessing the dire diplomatic situation. Every city-state allied with Byzantium or Germany has declared war on me due to ongoing conflicts. Those I remain at peace with are either under the "Open Door" policy, preventing alliances, or allied with Austria, my own ally. This presents a significant strategic confinement.
            
            **Leveraging Diplomat Capabilities**
            
            I'm realizing my Great Diplomat can build an Embassy in city-states, even under the "Open Door" resolution. This grants a delegate, circumventing the alliance restriction. I'm investigating building one in Colombo, as it's nearby and currently neutral, despite its negative influence.
            
            **Directing Diplomatic Asset**
            
            I'm prioritizing directing our Great Diplomat. Colombo and Rio de Janeiro are the targets for embassy placement to gain delegates, circumventing the "Open Door" resolution. I'm ensuring Rio's relations are boosted for AI consideration, rationalizing this action to secure a delegate.
            
            **Setting Nuclear Research**
            
            I am now focusing on our research path. To unlock critical units like Bazookas and Atomic Bombs, with the Manhattan Project nearing completion, I'm setting Nuclear Fission as our next technology. This strategic shift aims to provide Spain with powerful defensive capabilities against the current threats.
            
            **Adjusting Flavors**
            
            My focus is on fine-tuning our AI's priorities. With Spaceflight Pioneers secured, I'm adjusting Flavors. I'm maximizing "Nuke" to 100 and setting "UseNuke" to 60 for defensive atomic weapon deployment, while maintaining high "Science" and "Production" for our spaceship victory.
            
            **Boosting Diplomatic Focus**
            
            I'm adjusting our priorities. I've increased Diplomacy flavor to 60 to better leverage our Great Diplomat and secure alliances with remaining peaceful city-states. I'm also reconfiguring other flavors, focusing on Defense, CityDefense, Nuke, Production, Science, and Gold to align with our current strategic needs.
            
            **Directing Diplomatic Asset**
            
            I'm prioritizing directing our Great Diplomat. Colombo and Rio de Janeiro are the targets for embassy placement to gain delegates, circumventing the "Open Door" resolution. I'm ensuring Rio's relations are boosted for AI consideration, rationalizing this action to secure a delegate.
            
            **Setting Nuclear Research**
            
            I am now focusing on our research path. To unlock critical units like Bazookas and Atomic Bombs, with the Manhattan Project nearing completion, I'm setting Nuclear Fission as our next technology. This strategic shift aims to provide Spain with powerful defensive capabilities against the current threats.
            
            **Adjusting Flavors**
            
            My focus is on fine-tuning our AI's priorities. With Spaceflight Pioneers secured, I'm adjusting Flavors. I'm maximizing "Nuke" to 100 and setting "UseNuke" to 60 for defensive atomic weapon deployment, while maintaining high "Science" and "Production" for our spaceship victory.
            
            **Boosting Diplomatic Focus**
            
            I'm adjusting our priorities. I've increased Diplomacy flavor to 60 to better leverage our Great Diplomat and secure alliances with remaining peaceful city-states. I'm also reconfiguring other flavors, focusing on Defense, CityDefense, Nuke, Production, Science, and Gold to align with our current strategic needs.
            
            **Mobilizing Nuclear Defense**
            
            I'm fine-tuning AI flavors for immediate nuclear preparedness. With the Manhattan Project concluding soon, I'm prioritizing nuclear weapon development and deployment for defense, alongside strengthening our cities against imminent threats. Diplomacy is also being boosted to leverage our Great Diplomat effectively.
            
            **Optimizing Strategic Flavors**
            
            My focus is on synergizing our diplomatic and technological efforts. I'm setting Flavors to maximize Spaceship, Science, and Production at 100 to drive our victory condition. Simultaneously, I'm using a Great Diplomat to build an Embassy in a peaceful city-state, securing a crucial delegate. I've also verified our persona is well-optimized and requires no adjustments.
            
            **Refining Diplomatic Tones**
            
            I'm adjusting our diplomatic stances. Relations with Shoshone are appropriately hostile at 0/0 due to mutual denunciations. Byzantium and Germany remain hostile, reflecting our current wars. I'm setting Rio de Janeiro's relationship to 80/75 and confirming Colombo's high scores, ensuring our interactions align with our strategic objectives.
            
            **Revising Brussels Strategy**
            
            I'm re-evaluating Brussels. Despite the Open Door policy, we have significant influence and are not at war. I'm questioning why our priority there is 0/0, and realizing a past reset due to a mistaken war status needs correction to secure a delegate.
            
            **Correcting Diplomatic Focus**
            
            I'm rectifying our focus on Brussels. It was incorrectly marked as at war, but is now at peace and friendly. I'm increasing its diplomatic priority to ensure it's considered for AI actions, expanding our peaceful influence. I'm also investigating why Colombo's influence is negative.
            
            **Securing High-Influence City-States**
            
            I'm now prioritizing Rio de Janeiro, Brussels, and Shanghai due to their high influence and peaceful status. I'm setting Rio's relationship to 90/85, acknowledging its significant positive influence and making it a prime target for an Embassy, bypassing the "Open Door" policy.
            
            **Prioritizing Diplomatic Gains**
            
            I'm focusing on maximizing delegate acquisition. I've increased our influence with Brussels to 60/55, recognizing its peaceful status and proximity, and am directing our Great Diplomat there for an Embassy. I've also confirmed Nuclear Fission is set for research.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: mPNz1248CyjGn7G8
          - toolName: set-research
          - input:
            - Rationale: NUCLEAR DETERRENCE PATHWAY: Set Nuclear Fission as the next technology. With the Manhattan Project scheduled to complete at Tiflis on Turn 450, obtaining Nuclear Fission is the critical next step to unlock Atomic Bombs and Bazookas, providing Spain with ultimate defensive deterrence against the overwhelming military forces of Byzantium and Germany.
            - Technology: Nuclear Fission
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: OBLLqR83DSecb7J4
          - toolName: set-relationship
          - input:
            - Rationale: RIO DE JANEIRO EMBASSY TARGET: Increase priority from 0/0 to 90/85. Rio de Janeiro is our highest influence peaceful city-state (511 influence) and is close to our borders. This extremely strong relationship makes it the prime candidate for our newly born Great Diplomat to establish an Embassy, granting us +1 delegate to help counter the Byzantine diplomatic threat.
            - Private: 85
            - Public: 90
            - TargetID: 25
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: zetWOuRHhMJNM9Vf
          - toolName: set-relationship
          - input:
            - Rationale: BRUSSELS PEACE ENGAGEMENT: Increase from 0/0 to 60/55. Brussels is at peace and we maintain Friends status with 145 influence. This priority encourages the AI to utilize Brussels for trade, diplomatic units, or Great Diplomat missions to secure our position.
            - Private: 55
            - TargetID: 26
            - Public: 60
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 6bNYidVaLBZ9RFkK
          - toolName: set-flavors
          - input:
            - Flavors:
              - Happiness: 60
              - Religion: 30
              - Production: 100
              - Diplomacy: 60
              - Infrastructure: 70
              - CityDefense: 70
              - Nuke: 100
              - Growth: 40
              - Spaceship: 90
              - UseNuke: 60
              - Science: 100
              - Defense: 85
              - GreatPeople: 60
              - Gold: 75
              - Espionage: 50
            - Rationale: TURN 449 DEFENSIVE AND ATOMIC MOBILIZATION: Adjust flavors to prepare for the nuclear era. With Manhattan Project finishing at Tiflis on Turn 450, we set Nuke to 100 and UseNuke to 60 to ensure immediate weaponization and defensive usage of atomic bombs. We increase CityDefense to 70 and Defense to 85 to secure Tiflis and Barcelona against German and Byzantine threats. Diplomacy is increased to 60 to guide the newly born Great Diplomat toward building an Embassy in a peaceful city-state (Rio or Colombo) for a critical delegate boost. Spaceship (90), Science (100), and Production (100) remain maxed to drive our long-term scientific-industrial development.
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: mPNz1248CyjGn7G8
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
          - toolCallId: OBLLqR83DSecb7J4
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: zetWOuRHhMJNM9Vf
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 6bNYidVaLBZ9RFkK
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.