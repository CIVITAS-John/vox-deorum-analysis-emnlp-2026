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
  - replay_nuke: 60
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
          - Diplomacy: 90
          - Offense: 0
          - TileImprovement: 50
          - CityDefense: 60
          - Spaceship: 90
          - Production: 100
          - UseNuke: 0
          - Infrastructure: 80
          - WaterConnection: 5
          - Air: 20
          - MilitaryTraining: 15
          - Culture: 30
          - Espionage: 40
          - Airlift: 0
          - Nuke: 60
          - Gold: 70
          - AirCarrier: 0
          - NavalGrowth: 5
          - Naval: 10
          - Happiness: 60
          - Expansion: 0
          - Growth: 40
          - Defense: 80
          - Religion: 40
          - Mobilization: 50
          - Science: 100
          - NavalTileImprovement: 0
          - Mobile: 0
          - Recon: 0
          - Wonder: 0
          - Ranged: 10
          - GreatPeople: 70
          - NavalRecon: 0
          - Antiair: 20
        - GrandStrategy: Spaceship
      - rationale: TURN 449 DIPLOMATIC AND DEFENSIVE CONSOLIDATION: With the Manhattan Project completing on Turn 450 in Tiflis and a Great Diplomat spawning in Madrid, we pivot our focus. Increase Diplomacy flavor (30->90) and GreatPeople flavor (50->70) to ensure the AI immediately utilizes the Great Diplomat for an Embassy mission in Rio de Janeiro or Shanghai to secure a critical delegate, and utilizes our abundant Faith/Gold for Great Person acquisition. Maintain high Defense (80), CityDefense (60), and Nuke (60) to protect Tiflis and our core cities from German/Byzantine threats. Maintain Production (100) and Science (100) with Spaceship (90) to maximize our final score and scientific progression.
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 100
        - Rationale: RIO DE JANEIRO EMBASSY MISSION: Elevate relationship to maximum priority to guide the newly spawned Great Diplomat in Madrid to Rio de Janeiro. Establishing an Embassy here will grant Spain +1 permanent Delegate in the World Congress, helping block Byzantium's diplomatic victory. Rio is at peace and close, making it the safest and most efficient target.
        - Private: 95
        - TargetID: 25
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 27
        - Private: 75
        - Public: 80
        - Rationale: SHANGHAI SECONDARY EMBASSY TARGET: Increase priority to ensure the AI considers Shanghai as a viable secondary target for diplomatic missions or future emissaries. At peace and close proximity.
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 0
        - TargetID: 7
        - Public: 0
        - Rationale: FRANCE DEFEATED CLEANUP: Reset France to 0/0 as they have been defeated by Germany, making any diplomatic signaling obsolete.
    - #4:
      - toolName: set-research
      - args:
        - Rationale: NUCLEAR FISSION RESEARCH DIRECTION: Set Nuclear Fission as the next technology after Radar. This unlocks Bazookas for premier ranged defense, Atomic Bombs, and Nuclear Plants to boost our production capacity, aligning with our defense and high-score goals.
        - Technology: Nuclear Fission
    - #5:
      - toolName: set-policy
      - args:
        - Rationale: SPACEFLIGHT PIONEERS CONFIRMATION: Confirm Spaceflight Pioneers as the next policy choice. The free Great Scientist and Great Engineer will provide massive immediate yields, boosting our final score and scientific capabilities.
        - Policy: Spaceflight Pioneers
  - tokens:
    - inputTokens: 26278
    - reasoningTokens: 10024
    - outputTokens: 676
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Congress Impact**
            
            My focus is on the upcoming World Congress. With only four turns until voting commences, I'm evaluating potential resolutions and their strategic implications. Understanding the current geopolitical landscape will be crucial for influencing outcomes to my advantage.
            
            **Evaluating Shoshone's Influence**
            
            I'm re-evaluating the Shoshone's delegate count and potential vote. If they support Byzantium, a victory is imminent, drastically altering our strategic approach away from the previously planned Spaceship focus. I need to quickly assess our available policy options in light of this new development.
            
            **Setting Policy Priority**
            
            I'm confirming the `Spaceflight Pioneers` policy will be adopted. It seems we can set it again with `set-policy`, despite the 11-turn delay to the next actual policy adoption. This ensures our chosen path remains intact.
            
            **Prioritizing Technology Advancement**
            
            I'm re-evaluating our research path, aiming for a Spaceship victory. With Computers now researched and Radar 19 turns away, I need to select the optimal next technology. Nuclear Fission, offering significant military and economic benefits, appears to be the most strategic choice from the available options, especially considering the Manhattan Project's imminent completion.
            
            **Clarifying Production Delays**
            
            I'm working to reconcile conflicting turn estimates for the Manhattan Project. Military reports show stalled progress, while economic briefings indicate imminent completion. I need to pinpoint the source of this discrepancy to ensure accurate planning.
            
            **Adjusting Flavor Priorities**
            
            I'm re-evaluating our strategic flavors given the mandatory turnly decision. My current focus is on aligning these flavors with our continued pursuit of a Spaceship victory, analyzing the impact of recent research and economic data to determine the most effective settings.
            
            **Leveraging Diplomatic Assets**
            
            I'm reassessing our diplomatic flavor. With a Great Diplomat ready and Shoshone's potential vote for Byzantium in the World Congress, maximizing this flavor is critical for swaying city-states and preventing a premature defeat. I need to find ways to boost it immediately.
            
            **Resolving Diplomatic Contradiction**
            
            I've identified a critical contradiction. While military reports claim I'm at war with Austria, player status and my positive relationship indicate we're allies. This discrepancy needs immediate resolution to accurately assess diplomatic leverage.
            
            **Correcting Diplomatic Blunders**
            
            I've discovered a significant misinterpretation from my military advisors; I am, in fact, enjoying a Declaration of Friendship with Austria, not engaged in conflict. This error has also masked a crucial detail: our true adversaries are Germany and Byzantium. Many city-states, allied with them, have consequently declared war on us, complicating our current diplomatic and strategic positioning.
            
            **Analyzing City-State Alliances**
            
            I'm re-evaluating city-state alliances. Rio de Janeiro's Open Door policy prevents us from gaining ally status, despite our influence. I'm now checking other city-states for potential alliances and looking for any not allied to Byzantium or Germany.
            
            **Utilizing Diplomatic Missions**
            
            I'm now focusing on the Great Diplomat's potential. I've confirmed that a Diplomatic Mission can establish an Embassy in a city-state, granting an additional delegate for the World Congress. This is crucial for leveraging my influence against Germany and Byzantium.
            
            **Securing Diplomatic Influence**
            
            I'm confirming that establishing an embassy in a peaceful, allied city-state with my Great Diplomat will grant a permanent delegate for the World Congress. Given my current gold reserves and GPT, I can afford the necessary diplomatic actions to secure these crucial delegates, especially from friendly cities like Rio de Janeiro and Shanghai.
            
            **Assessing Shoshone Influence**
            
            I'm re-evaluating our standing with the Shoshone. Given our mutual denunciations and Spain's untrustworthy reputation with them, a swift improvement in relations appears unlikely. My focus has shifted to identifying other avenues for diplomatic leverage, as direct influence with the Shoshone seems unattainable within the remaining turns.
            
            **Voting on World Congress**
            
            I'm analyzing the upcoming World Congress proposals. Repealing the Passport System seems beneficial to hinder Byzantium's cultural victory, while sanctioning Austria is detrimental to our ally. I'm prioritizing diplomatic actions to secure delegates and influence the vote against our adversaries, Germany and Byzantium.
            
            **Establishing Embassies**
            
            My current focus is on leveraging my Great Diplomat to establish embassies. I've identified Shanghai and Rio de Janeiro as prime targets, as their closeness and existing friendships offer significant potential for gaining crucial World Congress delegates, even with Rio's Open Door policy in effect.
            
            **Clarifying Ally Status**
            
            I've discovered that Rio de Janeiro isn't actually allied with Byzantium, despite my previous assumptions. This changes my approach significantly, as I can now focus on securing an embassy there and gaining a delegate without worrying about Byzantium's influence over them, given our mutual "Friends" status.
            
            **Boosting Diplomatic Efforts**
            
            I'm significantly increasing our Diplomacy flavor to ensure the Great Diplomat is utilized effectively for gaining crucial World Congress delegates, especially from friendly city-states like Rio de Janeiro and Shanghai. This adjustment is vital for our strategic goals against Germany and Byzantium.
            
            **Setting Next Research**
            
            I am confirming Nuclear Fission as the next technology after Radar, as it provides essential advancements for both defense and power generation, aligning with my long-term strategic objectives. This will unlock critical units and infrastructure.
            
            **Confirming France's Status**
            
            I've confirmed that France has been defeated and is no longer a factor in delegate calculations. I've reset their relationship to 0/0 and am now re-tallying delegates for the World Congress, focusing on America and Austria as our remaining close friends.
            
            **Assessing Delegate Counts**
            
            My current focus is on Byzantium's overwhelming delegate count. I'm analyzing their city-state alliances, specifically Huari, Manila, Sydney, and Shedet, to understand how they acquired such influence. Given our war status with these states and their strong ties to Byzantium, flipping them is proving to be an insurmountable challenge at this juncture.
            
            **Clarifying Delegate Sources**
            
            I'm re-evaluating delegate calculations. Open Door city-states, it seems, don't grant delegates. Byzantium's high count likely stems from World Ideology, policies, religion, and extensive Great Diplomat embassies, not just allies. I need to verify this to accurately strategize against them.
            
            **Deploying Diplomat Wisely**
            
            I'm optimizing our Great Diplomat's mission, prioritizing Rio de Janeiro or Shanghai for embassy establishment to secure an essential delegate. By significantly boosting our Diplomacy flavor and setting specific target relationships, I'm ensuring the diplomat is directed to these high-value, peaceful city-states, maximizing our delegate count for the World Congress.
            
            **Directing Diplomatic Focus**
            
            I'm prioritizing securing a delegate from Rio de Janeiro with my Great Diplomat, given its peace and proximity. I'm also setting Shanghai as a secondary target for an embassy to further bolster our delegate count and counter Byzantium's influence. My current efforts are focused on confirming France's player ID for accurate relationship settings.
            
            **Updating City-State Relations**
            
            I'm re-evaluating relationships with city-states. France is out, so I've reset their player ID. My focus is now on Colombo; I need to confirm if our missionary has arrived before adjusting our influence there, as it's crucial for a quest and our standing.
            
            **Adjusting Diplomacy Flavor**
            
            I am increasing the Diplomacy flavor significantly to ensure our Great Diplomat is immediately utilized to establish an embassy in Rio de Janeiro or Shanghai. This is crucial for securing vital World Congress delegates and countering Byzantine influence, while maintaining strong defensive and production priorities.
            
            **Boosting Diplomatic Influence**
            
            My current focus is on leveraging the Great Diplomat to establish embassies, aiming for Rio de Janeiro or Shanghai to secure crucial World Congress delegates. I'm significantly increasing our Diplomacy flavor to ensure the diplomat is immediately directed to these high-value, peaceful city-states, maximizing our delegate count and countering Byzantium's influence.
            
            **Correcting Diplomatic Strategy**
            
            I've realized a critical misunderstanding: `set-relationship` is only for major civilizations, not city-states. This invalidates previous plans to directly influence Rio de Janeiro and Shanghai with that command. My focus must now shift to alternative methods of securing delegates from these vital city-states.
            
            **Clarifying Command Usage**
            
            I'm re-examining how I use `set-relationship`. It appears I mistakenly believed it was only for major civilizations, but past successful applications on city-states like Colombo and Rio de Janeiro prove otherwise. This is a critical correction for my diplomatic planning moving forward.
            
            **Directing Diplomatic Efforts**
            
            I'm confirming the `set-relationship` tool works on city-states, like Rio de Janeiro and Shanghai. I will direct our Great Diplomat towards them, as restoring relations with the Shoshone is likely futile with only four turns left. My focus is now on securing our own delegates.
            
            **Refining Diplomatic Actions**
            
            I'm confirming the `set-relationship` command's utility on city-states, specifically Rio de Janeiro and Shanghai. With Shoshone relations unlikely to improve within the remaining turns, my focus is now solely on securing delegates from these key cities.
            
            **Re-evaluating France's Status**
            
            I've reset France's player ID to 0/0, as they've been defeated by Germany. This cleanup action removes them as a diplomatic factor for delegate calculations.
            
            **Confirming Colombo's Status**
            
            I'm checking Colombo's missionary status. With their "Open Door" policy and Protestantism as their religion, I need to ensure our Buddhist missionary's progress before adjusting influence.
            
            **Purchasing Great Scientist**
            
            I'm considering using our substantial Faith reserves to purchase a Great Scientist. This aligns with our long-term strategic objectives and leverages our current financial position.
            
            **Purchasing Great Scientist**
            
            My current thoughts are focused on whether I can actually purchase a Great Scientist with Faith. I thought I needed to complete the Rationalism branch for this in Vox Populi, but the economy briefing states I can buy one immediately. This requires clarification before proceeding.
            
            **Adjusting Flavors Strategically**
            
            I'm re-evaluating our flavor settings to prioritize diplomatic and defensive consolidation. With the Manhattan Project nearing completion and a Great Diplomat poised to spawn, I'm increasing Diplomacy and GreatPeople flavors to leverage these assets effectively for the World Congress and future strategic moves.
            
            **Leveraging Faith and Gold**
            
            I'm considering purchasing a Great Scientist with my abundant Faith. My current thoughts are focused on whether this is actually possible immediately, as I believed the Rationalism branch was required in Vox Populi. This needs clarification before proceeding with our long-term strategic objectives.
            
            **Securing Delegate Advantage**
            
            I'm focusing on leveraging my Great Diplomat to establish embassies, aiming for Rio de Janeiro or Shanghai to secure crucial World Congress delegates. I'm significantly increasing our Diplomacy flavor to ensure the diplomat is immediately directed to these high-value, peaceful city-states, maximizing our delegate count and countering Byzantium's influence.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: dkyyfV1X96gAvX9z
          - toolName: set-flavors
          - input:
            - Rationale: TURN 449 DIPLOMATIC AND DEFENSIVE CONSOLIDATION: With the Manhattan Project completing on Turn 450 in Tiflis and a Great Diplomat spawning in Madrid, we pivot our focus. Increase Diplomacy flavor (30->90) and GreatPeople flavor (50->70) to ensure the AI immediately utilizes the Great Diplomat for an Embassy mission in Rio de Janeiro or Shanghai to secure a critical delegate, and utilizes our abundant Faith/Gold for Great Person acquisition. Maintain high Defense (80), CityDefense (60), and Nuke (60) to protect Tiflis and our core cities from German/Byzantine threats. Maintain Production (100) and Science (100) with Spaceship (90) to maximize our final score and scientific progression.
            - Flavors:
              - Diplomacy: 90
              - Offense: 0
              - TileImprovement: 50
              - CityDefense: 60
              - Spaceship: 90
              - Production: 100
              - UseNuke: 0
              - Infrastructure: 80
              - WaterConnection: 5
              - Air: 20
              - MilitaryTraining: 15
              - Culture: 30
              - Espionage: 40
              - Airlift: 0
              - Nuke: 60
              - Gold: 70
              - AirCarrier: 0
              - NavalGrowth: 5
              - Naval: 10
              - Happiness: 60
              - Expansion: 0
              - Growth: 40
              - Defense: 80
              - Religion: 40
              - Mobilization: 50
              - Science: 100
              - NavalTileImprovement: 0
              - Mobile: 0
              - Recon: 0
              - Wonder: 0
              - Ranged: 10
              - GreatPeople: 70
              - NavalRecon: 0
              - Antiair: 20
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: GeG6Dxi91DeOifTs
          - toolName: set-relationship
          - input:
            - Public: 100
            - Rationale: RIO DE JANEIRO EMBASSY MISSION: Elevate relationship to maximum priority to guide the newly spawned Great Diplomat in Madrid to Rio de Janeiro. Establishing an Embassy here will grant Spain +1 permanent Delegate in the World Congress, helping block Byzantium's diplomatic victory. Rio is at peace and close, making it the safest and most efficient target.
            - Private: 95
            - TargetID: 25
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: gz07aOeGDBlEqpBq
          - toolName: set-relationship
          - input:
            - TargetID: 27
            - Private: 75
            - Public: 80
            - Rationale: SHANGHAI SECONDARY EMBASSY TARGET: Increase priority to ensure the AI considers Shanghai as a viable secondary target for diplomatic missions or future emissaries. At peace and close proximity.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 4o8ue7p8K77Z7MCa
          - toolName: set-relationship
          - input:
            - Private: 0
            - TargetID: 7
            - Public: 0
            - Rationale: FRANCE DEFEATED CLEANUP: Reset France to 0/0 as they have been defeated by Germany, making any diplomatic signaling obsolete.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: MtlQNNy50n7pZeq1
          - toolName: set-research
          - input:
            - Rationale: NUCLEAR FISSION RESEARCH DIRECTION: Set Nuclear Fission as the next technology after Radar. This unlocks Bazookas for premier ranged defense, Atomic Bombs, and Nuclear Plants to boost our production capacity, aligning with our defense and high-score goals.
            - Technology: Nuclear Fission
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: A27ZylPDmJoT3HGY
          - toolName: set-policy
          - input:
            - Rationale: SPACEFLIGHT PIONEERS CONFIRMATION: Confirm Spaceflight Pioneers as the next policy choice. The free Great Scientist and Great Engineer will provide massive immediate yields, boosting our final score and scientific capabilities.
            - Policy: Spaceflight Pioneers
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: dkyyfV1X96gAvX9z
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
          - toolCallId: GeG6Dxi91DeOifTs
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: gz07aOeGDBlEqpBq
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 4o8ue7p8K77Z7MCa
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: MtlQNNy50n7pZeq1
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: A27ZylPDmJoT3HGY
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.