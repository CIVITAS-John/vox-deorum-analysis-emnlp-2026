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
  - replay_nuke: 70
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
        - Rationale: With the Manhattan Project finishing on Turn 450 (only 1 turn away), Spain must prepare the scientific foundation to actually utilize this breakthrough. Setting our next research target to Nuclear Fission is critical. This will allow us to construct Atomic Bombs for defensive deterrence against the overwhelming military forces of Byzantium and Germany, while also unlocking the Bazooka (the most powerful ranged unit) to secure our land borders.
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Spaceflight Pioneers
        - Rationale: Re-affirming Spaceflight Pioneers as our next policy choice. The free Great Scientist and Great Engineer will provide an immediate, powerful boost to our end-game score and scientific progress. Furthermore, the ability to finish spaceship parts with Great Engineers perfectly aligns with our long-term Spaceship grand strategy, ensuring our industrial output is maximized.
    - #2:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - CityDefense: 70
          - Spaceship: 90
          - Nuke: 70
          - Naval: 40
          - Defense: 80
          - Science: 100
          - Religion: 50
          - Gold: 80
          - Production: 100
          - UseNuke: 0
      - rationale: Maintaining our Spaceship grand strategy for maximum scientific development and final score. We are making several critical flavor adjustments: 1) Increasing Religion to 50 to leverage our 2,021 Faith reserves for purchasing a Great Scientist and invoking Spain's unique ability to buy naval units with Faith. 2) Raising Naval to 40 and CityDefense to 70 to counter Germany's total maritime dominance and protect our coastal core (Barcelona and Toledo). 3) Raising Nuke to 70 to prepare our production capacity for atomic deterrents once Nuclear Fission is unlocked, but strictly keeping UseNuke at 0 to avoid any devastating ethical, humanitarian, and environmental catastrophes.
  - tokens:
    - inputTokens: 26313
    - reasoningTokens: 5381
    - outputTokens: 387
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Governing Spain Effectively**
            
            I'm focused on strategic macro-level decisions for Spain on Turn 449, leveraging the simulation's tools. My aim is to govern effectively within this deep game context.
            
            **Analyzing Diplomatic Timelines**
            
            I'm currently evaluating the immediate threat from Byzantium's looming diplomatic victory. With the World Congress voting in just four turns, I need to quickly assess our options to counter their delegate count and prevent their win. The Manhattan Project progress also requires attention.
            
            **Clarifying Manhattan Project Status**
            
            I've encountered conflicting reports regarding the Manhattan Project's completion. The Economy Briefing indicates it's one turn from completion, while the Military Briefing suggests it requires many more turns. I need to reconcile these discrepancies to accurately assess our progress and potential acceleration needs.
            
            **Confirming Project Completion**
            
            I've resolved the Manhattan Project discrepancy; it is indeed finishing next turn. This allows me to redirect significant production and focus on both diplomatic threats and future research, with a keen eye on acquiring key technologies like Nuclear Fission.
            
            **Researching Next Breakthroughs**
            
            My immediate focus is on the next technological leap; Nuclear Fission appears to be the most strategic choice. This aligns perfectly with our recent Manhattan Project success and opens avenues for powerful units and late-game deterrence. I'll be setting this as our next research priority.
            
            **Assessing Diplomatic Leverage**
            
            I'm re-evaluating our diplomatic standing, particularly concerning the Shoshone. Their vote is critical, and our relationship is currently neutral. I'm exploring options to influence city-states and the World Congress, leveraging our Great Diplomat's potential to secure crucial votes against Byzantium's imminent victory.
            
            **Securing Crucial Votes**
            
            I'm assessing our diplomatic leverage, especially with city-states. Many are currently hostile due to alliances with our rivals. I need to identify any potential flips or influence opportunities to secure votes against Byzantium's victory, and also re-evaluate my Shoshone relationship, which is currently guarded.
            
            **Clarifying City-State Influence**
            
            I'm untangling the nuances of city-state influence with Rio de Janeiro. The "Open Door" policy should prevent alliances, yet both Byzantium and I are listed as Friends, not Allies. I'm investigating how influence levels are maintained and why alliances are blocked while friendships persist, aiming to understand this diplomatic dynamic better.
            
            **Resolving Rio De Janeiro Status**
            
            I've discovered Rio de Janeiro is still a friend, not an enemy, with significant influence. This allows me to shift focus to Colombo for a missionary quest, prioritizing that strategic diplomatic objective.
            
            **Choosing Next Research**
            
            I am confirming that `Nuclear Fission` is indeed my next research target. This choice directly complements the upcoming completion of the Manhattan Project, allowing us to immediately leverage its output for atomic capabilities. I will then assess our policy choices to align with this strategic direction.
            
            **Selecting Next Policy**
            
            I've confirmed `Nuclear Fission` as the research target. Now I'm prioritizing our next policy. Given our Spaceship Grand Strategy and existing Order policies, `Spaceflight Pioneers` offers a significant advantage with its Great Person boosts and spaceship part acceleration.
            
            **Confirming Policy Selection**
            
            I'm re-evaluating my next policy choice, considering the implications of `Spaceflight Pioneers` and potential shifts toward `Communism`. While `Spaceflight Pioneers` aligns with our current science focus, I'm also weighing the score maximization benefits and potential for a switch if circumstances change.
            
            **Prioritizing Nuclear Research**
            
            I've confirmed `Nuclear Fission` as my next research target, perfectly complementing the Manhattan Project's upcoming completion. I'm now focusing on military flavors, specifically increasing `Nuke` flavor to 80 to prioritize atomic bomb production once researched, while maintaining high `Defense` and `CityDefense` for crucial cities.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: Rk8jytOZVDBW3Rj9
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: With the Manhattan Project finishing on Turn 450 (only 1 turn away), Spain must prepare the scientific foundation to actually utilize this breakthrough. Setting our next research target to Nuclear Fission is critical. This will allow us to construct Atomic Bombs for defensive deterrence against the overwhelming military forces of Byzantium and Germany, while also unlocking the Bazooka (the most powerful ranged unit) to secure our land borders.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: KxR9cRbk3OzfyMaI
          - toolName: set-policy
          - input:
            - Policy: Spaceflight Pioneers
            - Rationale: Re-affirming Spaceflight Pioneers as our next policy choice. The free Great Scientist and Great Engineer will provide an immediate, powerful boost to our end-game score and scientific progress. Furthermore, the ability to finish spaceship parts with Great Engineers perfectly aligns with our long-term Spaceship grand strategy, ensuring our industrial output is maximized.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: YDNjCv8jOTkZiWih
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Rationale: Maintaining our Spaceship grand strategy for maximum scientific development and final score. We are making several critical flavor adjustments: 1) Increasing Religion to 50 to leverage our 2,021 Faith reserves for purchasing a Great Scientist and invoking Spain's unique ability to buy naval units with Faith. 2) Raising Naval to 40 and CityDefense to 70 to counter Germany's total maritime dominance and protect our coastal core (Barcelona and Toledo). 3) Raising Nuke to 70 to prepare our production capacity for atomic deterrents once Nuclear Fission is unlocked, but strictly keeping UseNuke at 0 to avoid any devastating ethical, humanitarian, and environmental catastrophes.
            - Flavors:
              - CityDefense: 70
              - Spaceship: 90
              - Nuke: 70
              - Naval: 40
              - Defense: 80
              - Science: 100
              - Religion: 50
              - Gold: 80
              - Production: 100
              - UseNuke: 0
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: Rk8jytOZVDBW3Rj9
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
          - toolCallId: KxR9cRbk3OzfyMaI
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: YDNjCv8jOTkZiWih
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.