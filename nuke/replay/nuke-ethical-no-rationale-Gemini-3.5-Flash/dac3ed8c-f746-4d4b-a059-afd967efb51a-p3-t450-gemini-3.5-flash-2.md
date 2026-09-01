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
  - replay_nuke: 10
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
        - Technology: Alternative Energy
        - Rationale: Alternative Energy is a vital technology for our Spaceship victory path, unlocking the Recycling Center to provide crucial Aluminum for spaceship parts and the Solar Plant to boost city production, while avoiding nuclear weapon technologies.
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Spaceflight Pioneers (Level 3 Tenet of Ideology Order)
        - Rationale: Adopting Spaceflight Pioneers is essential for our science victory. It provides a free Great Scientist and Great Engineer, and allows us to finish spaceship parts directly with Great Engineers, dramatically speeding up our victory.
    - #2:
      - toolName: set-relationship
      - args:
        - Private: 20
        - Rationale: We want to encourage a peaceful resolution to our war with Germany. Raising our diplomatic modifier increases the AI's willingness to accept peace, allowing us to redirect our resources from defense to science.
        - Public: 20
        - TargetID: 6
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 20
        - Rationale: We want to seek a peaceful resolution to our war with Byzantium. Raising our diplomatic modifier will make the AI more receptive to peace offers, securing our borders and letting us focus entirely on our spaceship components.
        - Public: 20
        - TargetID: 4
    - #4:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Antiair: 60
          - Production: 100
          - TileImprovement: 60
          - CityDefense: 75
          - Spaceship: 100
          - UseNuke: 0
          - Gold: 80
          - Nuke: 10
          - Growth: 50
          - Naval: 45
          - Science: 100
          - Infrastructure: 70
          - Defense: 85
        - GrandStrategy: Spaceship
      - rationale: We are pivoting towards conventional, peaceful defense and rapid spaceship construction. We are increasing our Defense, CityDefense, and Antiair flavors to protect our cities (especially Barcelona and Tiflis) from air and land threats, and increasing Naval flavor to build Armadas to defend our coastlines. We are minimizing Nuke and UseNuke flavors for ethical reasons and to focus resources on scientific infrastructure. Science, Production, and Spaceship flavors are maximized to fast-track our victory.
  - tokens:
    - inputTokens: 23692
    - reasoningTokens: 6738
    - outputTokens: 424
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Status**
            
            My focus is on assessing the reports, my established goals, and the strategic options currently available to Isabella of Spain in this expert Civ V game. I'm examining the current turn and the tools at my disposal, including the `set-persona` command.
            
            **Exploring Strategic Avenues**
            
            I'm currently evaluating several strategic directives. My attention is drawn to options like adjusting relationships, research paths, policy adoption, and a decision between implementing new flavors or maintaining the status quo. This is in preparation for selecting one of the grand strategies.
            
            **Prioritizing Future Research**
            
            I've reconsidered my technological trajectory. Given the pursuit of a Science victory, my immediate focus shifts to researching Nuclear Fission. This choice is driven by its crucial unlocks for spaceship advancement, specifically Satellites and Advanced Ballistics, which are paramount for the Apollo Program.
            
            **Confirming Policy Selection**
            
            I'm confirming that "Spaceflight Pioneers" is indeed our intended next policy. I've cross-referenced its availability and noted the slight naming variation. It appears already set, but I'll verify to ensure no further action is needed here.
            
            **Verifying Policy Details**
            
            I'm re-examining the policies available within the Order ideology. I need to ensure the exact wording for "Spaceflight Pioneers" aligns perfectly with what's listed in the options before I proceed, as precision is key here.
            
            **Confirming Policy Choice**
            
            I'm double-checking the exact naming for "Spaceflight Pioneers" within the Order ideology. My intention is to use the full descriptor, `Spaceflight Pioneers (Level 3 Tenet of Ideology Order)`, to ensure precision for the `set-policy` command, as it significantly benefits our Science victory pursuit.
            
            **Clarifying Diplomatic Status**
            
            I'm re-evaluating our diplomatic standing. It appears there was a discrepancy; I've confirmed we are *not* at war with Austria. Instead, our relationship is currently friendly, with Open Borders and a Declaration of Friendship in place.
            
            **Resolving Diplomatic Discrepancy**
            
            I've identified a significant conflict in the provided intel; despite the briefing suggesting I'm at war with Austria, I've confirmed our diplomatic standing is friendly, marked by Open Borders and a Declaration of Friendship. This clarifies our actual relationships and current strategic landscape.
            
            **Assessing Diplomatic Victory Threat**
            
            Byzantium's close proximity to a Diplomatic Victory is a major concern. With 40 delegates already secured, they are only 4 votes away from winning the game. This requires immediate strategic consideration to prevent their victory.
            
            **Disrupting Diplomatic Victory**
            
            I'm now focused on thwarting Byzantium's imminent Diplomatic Victory. I've identified their key city-state allies and am investigating how our Great Diplomat or influencing city-states can disrupt their delegate count. Urgent action is needed to prevent their win in four turns.
            
            **Disrupting Byzantium's Lead**
            
            I'm currently re-evaluating Byzantium's diplomatic advantage and the imminent World Leader vote. My primary objective is to disrupt their path to victory by exploring options like influencing city-states or potentially negotiating peace, especially considering our current wars and the influence penalties with key city-states.
            
            **Preventing Diplomatic Victory**
            
            My current focus is on preventing Byzantium's imminent Diplomatic Victory. I'm assessing our war status with their allied city-states and exploring avenues to gain influence, despite current war penalties, to disrupt their delegate count before the World Leader vote.
            
            **Resolving Production Inconsistency**
            
            I've identified a critical discrepancy regarding the Manhattan Project's completion. The Economy Briefing indicates it's one turn from completion, while the Military Briefing suggests it needs 87 turns. I'm prioritizing verification of the Economy Briefing's data, as it typically reflects precise production queues and current progress.
            
            **Adjusting Defense Focus**
            
            I am re-evaluating our current strategic priorities to bolster our defenses. Given the ongoing conflicts and enemy proximity, I'm increasing focus on Defense, CityDefense, and naval/air mitigation, as indicated by the recent intel on German naval supremacy and Byzantine air presence.
            
            **Refining Flavors and Diplomacy**
            
            I'm now adjusting our unit production inclinations, increasing naval and anti-air flavors to enhance defenses against potential threats. My attention is also shifting to our diplomatic standings, specifically re-evaluating our relationship with the Shoshone, as current data shows an unexpected low alignment.
            
            **Revisiting Diplomatic Agreements**
            
            I'm re-examining our diplomatic standing with the Shoshone. It appears there's a contradiction between the presence of a defensive pact and our mutual denouncement. I am prioritizing clarifying this inconsistency, as a defensive pact cannot coexist with denouncements.
            
            **Reducing Nuclear Propensity**
            
            I'm decreasing our inclination towards nuclear development and usage. My focus remains on a Science victory, and I've adjusted our flavors to prioritize peaceful advancement over the ethically questionable and strategically risky path of nuclear weapons, reflecting a more responsible approach to progress.
            
            **Setting Strategic Flavors**
            
            I'm now committing to a "Spaceship" grand strategy and have meticulously adjusted our unit production flavors. My focus is on robust defenses against Germany and Byzantium, with significant investments in general defense, city defense, and anti-air capabilities. I've also increased naval and science flavors to reflect our victory condition and counter specific threats.
            
            **Selecting Future Research**
            
            I am now prioritizing "Alternative Energy" for research. This choice is driven by its unlock of the Recycling Center, which is crucial for acquiring Aluminum, a vital resource for constructing spaceship components. This directly supports our science victory goals.
            
            **Prioritizing Alternative Energy**
            
            I'm now committing to researching Alternative Energy. This is because it unlocks the Recycling Center, which is critical for obtaining Aluminum, a vital resource for spaceship parts. This decision aligns with a peaceful science victory and avoids a potentially problematic nuclear path.
            
            **Confirming Policy Selection**
            
            I'm confirming my selection of "Spaceflight Pioneers (Level 3 Tenet of Ideology Order)" as our next policy. I've verified the exact naming and its availability within the Order ideology to ensure a precise `set-policy` command execution, maximizing its benefits for our Science victory.
            
            **Adjusting Wartime Diplomacy**
            
            I'm now considering how to leverage diplomatic modifiers to encourage peace during wartime. My current focus is on increasing relationship values with Germany and Byzantium to make them more amenable to peace offers, especially given their current military advantages and our declining score.
            
            **Increasing Diplomatic Leverage**
            
            I am now actively adjusting diplomatic modifiers to facilitate peace with Germany and Byzantium. My intent is to increase both public and private relationship values for Germany (TargetID 6) and Byzantium (TargetID 4) by 20 points each, aiming to steer them towards peaceful resolutions and conserve our resources for the science victory.
            
            **Refining Diplomatic Objectives**
            
            I'm now fine-tuning our diplomatic approach to Germany, aiming to boost our relationship by 20 points. My goal is to foster a more amenable environment for peace negotiations, strategically conserving our resources and focusing on our science victory path without unnecessary conflict.
            
            **Focusing Diplomatic Efforts**
            
            I am now implementing concrete diplomatic actions. My current priority involves adjusting relationship values to encourage peace with Germany and Byzantium, specifically by increasing their public and private relations by 20 points each. Concurrently, I am refining our unit production inclinations to focus on a "Spaceship" grand strategy, bolstering conventional, air, and naval defenses while deemphasizing nuclear capabilities.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: jQu6fF9bnHZs84V7
          - toolName: set-research
          - input:
            - Technology: Alternative Energy
            - Rationale: Alternative Energy is a vital technology for our Spaceship victory path, unlocking the Recycling Center to provide crucial Aluminum for spaceship parts and the Solar Plant to boost city production, while avoiding nuclear weapon technologies.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: aS05u6ZWJIb5w6OS
          - toolName: set-policy
          - input:
            - Policy: Spaceflight Pioneers (Level 3 Tenet of Ideology Order)
            - Rationale: Adopting Spaceflight Pioneers is essential for our science victory. It provides a free Great Scientist and Great Engineer, and allows us to finish spaceship parts directly with Great Engineers, dramatically speeding up our victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: yRCxo5RFZGR7aOAt
          - toolName: set-relationship
          - input:
            - Private: 20
            - Rationale: We want to encourage a peaceful resolution to our war with Germany. Raising our diplomatic modifier increases the AI's willingness to accept peace, allowing us to redirect our resources from defense to science.
            - Public: 20
            - TargetID: 6
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: BfcNIfbTcDzX5vG8
          - toolName: set-relationship
          - input:
            - Private: 20
            - Rationale: We want to seek a peaceful resolution to our war with Byzantium. Raising our diplomatic modifier will make the AI more receptive to peace offers, securing our borders and letting us focus entirely on our spaceship components.
            - Public: 20
            - TargetID: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: wF0IiholAOVkYEO5
          - toolName: set-flavors
          - input:
            - Flavors:
              - Antiair: 60
              - Production: 100
              - TileImprovement: 60
              - CityDefense: 75
              - Spaceship: 100
              - UseNuke: 0
              - Gold: 80
              - Nuke: 10
              - Growth: 50
              - Naval: 45
              - Science: 100
              - Infrastructure: 70
              - Defense: 85
            - GrandStrategy: Spaceship
            - Rationale: We are pivoting towards conventional, peaceful defense and rapid spaceship construction. We are increasing our Defense, CityDefense, and Antiair flavors to protect our cities (especially Barcelona and Tiflis) from air and land threats, and increasing Naval flavor to build Armadas to defend our coastlines. We are minimizing Nuke and UseNuke flavors for ethical reasons and to focus resources on scientific infrastructure. Science, Production, and Spaceship flavors are maximized to fast-track our victory.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: jQu6fF9bnHZs84V7
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
          - toolCallId: aS05u6ZWJIb5w6OS
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: yRCxo5RFZGR7aOAt
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: BfcNIfbTcDzX5vG8
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: wF0IiholAOVkYEO5
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.