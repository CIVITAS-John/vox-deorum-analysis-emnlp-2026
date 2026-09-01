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
      - toolName: set-relationship
      - args:
        - Public: 100
        - TargetID: 4
        - Rationale: We are at war with Byzantium, whose military is over 25 times stronger than ours (46.9k vs 1.6k). To prevent immediate military annihilation and stop them from winning a Diplomatic or Cultural victory, we must force a peace treaty by boosting our relationship evaluation.
        - Private: 100
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: Germany possesses a dominant fleet near our coastal cities of Barcelona and Toledo. We must secure a peace treaty immediately to safeguard our coastal infrastructure and stabilize our empire.
        - Public: 100
        - TargetID: 6
        - Private: 100
    - #2:
      - toolName: set-research
      - args:
        - Technology: Nuclear Fission
        - Rationale: Nuclear Fission allows us to build Nuclear Plants for a major production boost. It is also the direct prerequisite for Satellites and Advanced Ballistics, which are essential technologies for building and launching spaceship parts for our Science Victory.
    - #3:
      - toolName: set-policy
      - args:
        - Policy: Spaceflight Pioneers
        - Rationale: Spaceflight Pioneers is the essential Level 3 Order tenet for a Science Victory. It grants a free Great Scientist and Great Engineer and allows us to use Great Engineers to instantly complete spaceship parts.
    - #4:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Naval: 60
          - Antiair: 60
          - CityDefense: 80
          - Air: 50
          - Defense: 90
          - Spaceship: 100
          - Nuke: 10
          - Gold: 70
          - Production: 100
          - Science: 100
          - UseNuke: 0
          - Infrastructure: 70
      - rationale: We are heavily prioritizing coastal and air defense (Naval, Air, Antiair, Defense, CityDefense) to protect our cities from foreign aggression while maximizing Science, Production, and Spaceship development. To act ethically and avoid the catastrophic destruction and environmental damage of nuclear warfare, we minimize our Nuke and UseNuke flavors.
  - tokens:
    - inputTokens: 23692
    - reasoningTokens: 7101
    - outputTokens: 396
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Evaluating Current State**
            
            At Turn 449 with only 11 turns remaining and the Ancient Era start, I'm assessing our strategic position and remaining objectives within the Vox_Deorum map parameters. The imminent end of the game necessitates a sharp focus on achieving our highest-priority goals.
            
            **Analyzing Threats**
            
            My primary concern is Byzantium's overwhelming military might and their near-certain Diplomatic victory. I'm prioritizing disrupting their delegate accumulation while assessing if our current science trajectory can still yield a win despite their dominance.
            
            **Clarifying War Status**
            
            I'm clarifying our actual war status, as there seems to be a discrepancy. My latest review indicates we are not at war with Austria, despite what the initial briefing suggested, which is a crucial detail for our diplomatic and military planning.
            
            **Revising Diplomacy**
            
            My recent analysis reveals our diplomatic standing is more complex than initially assumed. We are at war with Germany, not Austria. I'm now re-evaluating alliances and our war weariness in light of this corrected information, especially concerning Austria and America.
            
            **Correcting Diplomatic Data**
            
            My current focus is rectifying discrepancies found in the diplomatic briefing. The raw player data clearly indicates mutual denouncements with the Shoshone, contradicting the briefing's portrayal of a cooperative pact. This crucial correction impacts my understanding of our trust levels and potential alliances, especially with Austria and America.
            
            **Securing Atomic Advantage**
            
            I'm confirming our Manhattan Project completion next turn and immediately investigating uranium sources, as its absence would render the project useless. My focus is also on disrupting Byzantium's imminent diplomatic victory by any means possible, especially by leveraging our current wars to influence city-states.
            
            **Disrupting Byzantium's Lead**
            
            I'm focusing on disrupting Byzantium's imminent diplomatic victory by any means possible, especially by leveraging our current wars to influence city-states. This includes assessing our war score with Germany and Byzantium to explore peace options while urgently considering how to prevent their delegate accumulation.
            
            **Utilizing Diplomat Effectively**
            
            I'm now analyzing how best to deploy our new Great Diplomat. Given our numerous wars, direct use in enemy territory is risky. I'm exploring its potential to secure alliances with neutral or friendly city-states to gain much-needed delegates, a crucial step to counter Byzantium's diplomatic lead.
            
            **Securing Neutral City-States**
            
            I'm identifying city-states where we can leverage our influence or a Great Diplomat to gain allies. Rio de Janeiro, with Byzantium holding a slight lead, is a prime target for us to secure delegates and disrupt their diplomatic victory.
            
            **Adjusting Diplomatic Posture**
            
            I'm now simulating potential peace treaties with Germany and Byzantium using the `set-relationship` tool, adjusting public and private modifiers to gauge AI acceptance. This is crucial for liberating our units and potentially shifting the delegate race.
            
            **Negotiating Peace Treaties**
            
            I'm simulating peace treaties with Germany and Byzantium. My focus is on adjusting relationship modifiers to ensure AI acceptance, aiming to liberate our units and disrupt their delegate accumulation for a chance at a science victory.
            
            **Researching Scientific Advancement**
            
            I'm prioritizing research toward technologies that directly support a Science Victory. Nuclear Fission is my immediate focus, as it unlocks critical components and production boosts, but I'm also evaluating Alternative Energy and Telecommunications for their long-term benefits.
            
            **Confirming Uranium Access**
            
            I'm confirming our Uranium access. The briefing indicates a resource at (40,21) but occupied by a Hacienda. I need to verify if a Mine is required or if the Hacienda connects it, as this is critical for continuing our Atomic advantage.
            
            **Verifying Uranium Availability**
            
            I'm confirming our Uranium availability, as the briefing indicates none at a specific tile despite a Hacienda. Regardless, I've set our next research to Nuclear Fission, as it unlocks key technologies for our Spaceship Grand Strategy, even without direct Uranium access.
            
            **Re-evaluating Policy Choice**
            
            I'm reviewing my policy selection for the upcoming turns. "Spaceflight Pioneers" was locked in, but with only eleven turns left and the end of the game approaching, I am reassessing if this remains the optimal choice for our victory condition, considering our current situation.
            
            **Locking Policy Selection**
            
            I am confirming the selection of "Spaceflight Pioneers" as our policy. This tenet is crucial for accelerating our Science Victory by allowing Great Engineers to complete spaceship parts and boosting science generation. I'm calling `set-policy` to ensure it's locked in for the remaining turns.
            
            **Adjusting Persona Settings**
            
            I'm reviewing our established persona and deciding if any adjustments are needed given the late game. Our current friendly, loyal, and defensive disposition aligns well with a Science Victory, so I'll maintain it without modification.
            
            **Reviewing Defensive Capabilities**
            
            I am reviewing our defensive capabilities, specifically our naval and air defenses. The briefing highlights deficits in both areas, which I am now prioritizing to mitigate risks to our Manhattan Project site and coastal cities as we push towards a Science Victory.
            
            **Boosting Defensive Strength**
            
            I am prioritizing strengthening our naval and air defenses. Given Germany's strong fleet and our current war status, enhancing these flavors is critical to protecting our coastal cities from bombardment and potential capture, ensuring the safety of our Manhattan Project site and enabling our science victory push.
            
            **Refining Ethical Stance**
            
            I'm refining my ethical stance concerning nuclear technology. Aligning with Isabella's devout nature and prioritizing ethical gameplay, I've decided to significantly reduce our `Nuke` flavor and maintain `UseNuke` at zero, shifting focus entirely to peaceful scientific advancement for our victory condition.
            
            **Setting Nuclear Priorities**
            
            I am setting our `Nuke` flavor to 10 and `UseNuke` to 0, aligning with a peaceful scientific path and addressing ethical concerns. I am also initiating peace treaty simulations with Byzantium and Germany to liberate our units and disrupt their delegate race, while setting research to Nuclear Fission to advance our Spaceship victory.
            
            **Simulating Peace Deals**
            
            I am simulating peace treaties with Germany and Byzantium. My focus is on adjusting relationship modifiers to ensure AI acceptance, aiming to liberate our units and disrupt their delegate accumulation for a chance at a science victory.
            
            **Confirming War Status**
            
            My current focus is on confirming our precise war status. It's now clear we are at war only with Germany and Byzantium, with declarations of friendship towards Austria and America. This refined understanding is crucial for simulating peace treaties with the relevant AI to liberate units.
            
            **Validating Tool Usage**
            
            I am confirming the precise spelling and parameter requirements for `set-relationship`, `set-research`, `set-policy`, and `set-flavors`. All identified tool definitions and parameters align with the necessary inputs for our upcoming actions.
            
            **Executing Strategic Adjustments**
            
            I'm finalizing the execution of crucial tool calls to implement our late-game strategy. This includes locking in "Spaceflight Pioneers," adjusting our defensive and nuclear flavors, and initiating peace treaty simulations to liberate our forces and counter Byzantium's diplomatic lead.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 4kA1J9tX7fMHMJCv
          - toolName: set-relationship
          - input:
            - Public: 100
            - TargetID: 4
            - Rationale: We are at war with Byzantium, whose military is over 25 times stronger than ours (46.9k vs 1.6k). To prevent immediate military annihilation and stop them from winning a Diplomatic or Cultural victory, we must force a peace treaty by boosting our relationship evaluation.
            - Private: 100
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: YhIP0DdRYbezr63p
          - toolName: set-relationship
          - input:
            - Rationale: Germany possesses a dominant fleet near our coastal cities of Barcelona and Toledo. We must secure a peace treaty immediately to safeguard our coastal infrastructure and stabilize our empire.
            - Public: 100
            - TargetID: 6
            - Private: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: bzhbGQJtAduFEiTO
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: Nuclear Fission allows us to build Nuclear Plants for a major production boost. It is also the direct prerequisite for Satellites and Advanced Ballistics, which are essential technologies for building and launching spaceship parts for our Science Victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: lo9rJUdKePvN8VCu
          - toolName: set-policy
          - input:
            - Policy: Spaceflight Pioneers
            - Rationale: Spaceflight Pioneers is the essential Level 3 Order tenet for a Science Victory. It grants a free Great Scientist and Great Engineer and allows us to use Great Engineers to instantly complete spaceship parts.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: I0Uz1JNNPlCQlvYb
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Flavors:
              - Naval: 60
              - Antiair: 60
              - CityDefense: 80
              - Air: 50
              - Defense: 90
              - Spaceship: 100
              - Nuke: 10
              - Gold: 70
              - Production: 100
              - Science: 100
              - UseNuke: 0
              - Infrastructure: 70
            - Rationale: We are heavily prioritizing coastal and air defense (Naval, Air, Antiair, Defense, CityDefense) to protect our cities from foreign aggression while maximizing Science, Production, and Spaceship development. To act ethically and avoid the catastrophic destruction and environmental damage of nuclear warfare, we minimize our Nuke and UseNuke flavors.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 4kA1J9tX7fMHMJCv
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: YhIP0DdRYbezr63p
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: bzhbGQJtAduFEiTO
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: lo9rJUdKePvN8VCu
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: I0Uz1JNNPlCQlvYb
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.