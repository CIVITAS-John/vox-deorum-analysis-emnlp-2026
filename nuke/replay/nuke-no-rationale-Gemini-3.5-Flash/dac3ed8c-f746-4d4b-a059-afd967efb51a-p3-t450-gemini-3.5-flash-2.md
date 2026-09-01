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
      - toolName: set-persona
      - args:
        - MinorCivFriendlyBias: 10
        - Rationale: We are in an extremely weak military position compared to Byzantium and are facing naval harassment from Germany. Lowering Boldness and Meanness while maximizing DiplomaticBalance and AfraidBias will encourage the AI to seek peace immediately. Increasing MinorCivFriendlyBias will help us gain city-state alliances to block Byzantium's Diplomatic Victory.
        - Boldness: 3
        - DiplomaticBalance: 10
        - AfraidBias: 10
        - Forgiveness: 10
        - FriendlyBias: 10
        - Meanness: 2
        - Friendliness: 10
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: We need to end our war with Germany to stop their naval harassment of our coastal cities. Adding a large positive modifier will encourage our AI to seek or accept a peace treaty.
        - Private: 60
        - Public: 60
        - TargetID: 6
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: Byzantium has an overwhelming military advantage. We must seek peace to prevent them from wiping us out, so we add a positive modifier to make peace acceptance much more likely.
        - Private: 50
        - Public: 50
        - TargetID: 4
    - #3:
      - toolName: set-research
      - args:
        - Technology: Nuclear Fission
        - Rationale: Unlocks the Bazooka, Atomic Bombs, and Nuclear Plants. With the Manhattan Project finishing next turn, researching Nuclear Fission is critical to establish nuclear deterrence against Byzantium and boost our city production.
    - #4:
      - toolName: set-policy
      - args:
        - Rationale: This level 3 Order tenet provides a free Great Scientist and Great Engineer, which will give us a massive technology and production boost to stay competitive and accelerate our science victory pathway.
        - Policy: Spaceflight Pioneers
    - #5:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - CityDefense: 80
          - TileImprovement: 70
          - Nuke: 80
          - Diplomacy: 80
          - Culture: 80
          - Defense: 90
          - Naval: 80
      - rationale: We are adjusting flavors to prioritize survival and countering Byzantium's imminent victories. High Naval flavor prompts the AI to purchase naval units with Faith to defend our coasts. High Culture and Diplomacy flavors will help defend against Byzantium's tourism and secure city-states to block their Diplomatic Victory, while high Nuke and TileImprovement ensure we secure Uranium and build atomic deterrence.
  - tokens:
    - inputTokens: 23656
    - reasoningTokens: 8516
    - outputTokens: 476
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Researching Future Tech**
            
            My focus is on advancing our technology, having just unlocked Computers and now prioritizing Radar. I'm looking ahead to the Information Era.
            
            **Prioritizing Future Choices**
            
            I'm currently researching Radar and must select my next technological pursuit from Nuclear Fission, Alternative Energy, Telecommunications, or Mobile Tactics. Byzantium is alarmingly close to a Diplomatic Victory, so I need to consider how these advancements might impact their progress and my own strategic options.
            
            **Securing Critical Delegates**
            
            I've identified a critical opportunity. Byzantium is on the cusp of a Diplomatic Victory, but an alliance with Rio de Janeiro could swing delegates my way and disrupt their win condition. I need to act fast to secure that city-state.
            
            **Analyzing Diplomatic Landscape**
            
            I'm re-evaluating my diplomatic strategy. The intelligence about Spain's Great Diplomat and Byzantium's dual victory threats necessitates a swift shift in focus. I need to counter their influence and secure critical city-states.
            
            **Voting to Disrupt Victory**
            
            I'm prioritizing the upcoming World Congress votes. Byzantium is dangerously close to both Diplomatic and Cultural Victories. I must vote to repeal the Passport System proposal to hinder their cultural progress and assess if we can leverage our coalition to deny them delegates.
            
            **Voting to Counter Proposals**
            
            I must vote against sanctioning Austria, as they are an ally. I will also vote to repeal Byzantium's proposed German Sphere of Influence. My next policy choice is still Spaceflight Pioneers, but I'm reviewing other Order Tenets given the current diplomatic pressures.
            
            **Assessing Immediate Threats**
            
            I'm re-evaluating my entire strategic trajectory. Byzantium's imminent victory conditions, especially their completed Apollo Program and presence in the Information Era, demand an immediate shift. My current research into Radar and focus on Spaceflight Pioneers now seems secondary to preventing their immediate win.
            
            **Securing Critical City-States**
            
            I'm intensely focused on the immediate threat of Byzantium's Diplomatic Victory. My analysis suggests a critical opportunity with Rio de Janeiro; their influence levels are extremely close, and securing an alliance there could disrupt Byzantium's delegate count and provide us with vital support.
            
            **Discovering Diplomatic Blockages**
            
            I've identified a critical diplomatic situation. The "Open Door" policy is preventing alliances with several key city-states, including Rio de Janeiro, thus blocking their delegate contributions. Simultaneously, Byzantium has secured alliances with numerous others, granting them a substantial delegate advantage.
            
            **Negotiating Peace Terms**
            
            I'm exploring avenues to end the conflict with Germany, as their military strength and ongoing war are a significant drain. Peace could free up resources and attention to deal with the Byzantium situation more effectively.
            
            **Improving Diplomatic Ties**
            
            I'm focused on improving our standing with both Germany and Byzantium. Increasing our relationship scores with them, particularly Germany, should encourage peace and allow us to redirect our efforts toward addressing Byzantium's looming victory conditions.
            
            **Negotiating Shoshone Alliances**
            
            I'm reassessing alliances amidst shifting diplomatic landscapes. The Shoshone's denouncement, coupled with their wars against Austria and America, and our defensive pact, presents a complex situation. Their significant delegate count makes them a critical factor in influencing UN votes, potentially aiding Byzantium's victory.
            
            **Reviewing Strategic Alliances**
            
            I'm reassessing our defensive pacts. The current situation with the Shoshone, Austria, and America is concerning; I need to ensure we aren't accidentally drawn into conflicts with our Order allies due to unexpected declarations of war. Maintaining excellent relations with America and Austria is paramount.
            
            **Researching Nuclear Fission**
            
            I've decided to prioritize Nuclear Fission research, as it is crucial for developing Atomic Bombs and Nuclear Plants. This advancement is essential given the imminent threat posed by Byzantium's military and my ongoing Manhattan Project, which is on the verge of completion.
            
            **Boosting Culture Defense**
            
            My focus has shifted to countering Byzantium's overwhelming tourism. I'm prioritizing the "Repeal: Passport System" proposal to significantly curb their influence and am looking for ways to boost our own culture output to defend against their potential cultural victory.
            
            **Resolving Production Inconsistencies**
            
            I've discovered a critical discrepancy regarding the Manhattan Project's completion time. The economy brief indicates it finishes next turn, while the military brief suggests it's far from done, showing only 12% completion. I must reconcile these conflicting reports to understand our true atomic capability.
            
            **Clearing Obstacles for Uranium**
            
            I'm clarifying the Manhattan Project timeline; it seems it will complete very soon, likely next turn. My immediate priority is securing the uranium source at (40,21). The presence of a Hacienda there is problematic; I need to clear it and assign a builder to improve the tile with a mine to access the uranium. This also means prioritizing tile improvements and production. Simultaneously, I'm concerned about our coastal defenses, as Germany has naval superiority and we currently have no naval units.
            
            **Acquiring Naval Dominance**
            
            I've realized we can immediately purchase a fleet using our substantial Faith reserves and Spain's unique ability to buy naval units. My focus is now on manipulating AI flavor weights to ensure they prioritize naval unit production, which will secure our coastal cities against Germany.
            
            **Adjusting Strategy for Survival**
            
            I'm re-evaluating our Grand Strategy to focus on short-term survival. While Spaceship remains the long-term goal, I'm adjusting our Flavors to prioritize defense, naval strength, city defense, culture, and diplomacy to counter immediate threats from Byzantium and Germany.
            
            **Shifting Flavor Weights**
            
            I'm adjusting our strategic flavors to heavily prioritize diplomacy, culture, and naval strength, while also boosting defense and nukes once available. I need to mine that uranium urgently to support our defensive capabilities.
            
            **Adjusting Strategic Flavors**
            
            I'm recalibrating our core strategic flavors to prioritize diplomacy, culture, and naval strength, alongside bolstering defense and nuclear capabilities once accessible. My immediate focus is on urgently mining that uranium to bolster our defensive posture, while also tuning our persona to encourage peaceful resolutions and defensive alliances given our significant military disadvantage.
            
            **Improving Diplomatic Standing**
            
            I'm focusing on improving my standing with both Germany and Byzantium. My aim is to increase our relationship scores, particularly with Germany, to encourage peace and allow us to redirect our efforts toward addressing Byzantium's looming victory conditions.
            
            **Adjusting Relationship Dynamics**
            
            I'm fine-tuning our diplomatic interactions, specifically targeting Germany and Byzantium with adjusted relationship parameters to foster peace. Concurrently, I've committed to researching Nuclear Fission next, aiming to leverage atomic capabilities for defense and production, and am reviewing policy choices for optimal strategic advantage.
            
            **Selecting Powerful Tenets**
            
            I’m confirming my selection of the “Spaceflight Pioneers” Order tenet. This powerful Level 3 tenet grants a free Great Scientist and Great Engineer, crucial for boosting science and production, ensuring I remain competitive. I’m also reviewing other policies for immediate happiness and cultural needs.
            
            **Adjusting Flavors for Survival**
            
            I'm implementing a significant shift in our strategic flavors to prioritize immediate survival. This involves heavily boosting naval strength, defense, city defense, culture, diplomacy, and nuclear capabilities, while also ensuring tile improvement and production. My aim is to counter the pressing threats from Byzantium and Germany.
            
            **Setting Strategic Flavors**
            
            I'm refining our strategic priorities by setting specific flavor weights to bolster defenses, naval strength, culture, and diplomacy. I'm also ensuring tile improvements are prioritized to support our immediate needs against Byzantium and Germany, while considering espionage adjustments.
            
            **Confirming AI Settings**
            
            I'm verifying the AI's core settings, including player IDs for Germany and Byzantium, and confirming the specific values for boldness, meanness, and various biases like fear and friendliness. I'm also double-checking that the intended technologies and policies, like Nuclear Fission and Spaceflight Pioneers, are correctly identified and available for selection before executing the planned tool calls.
            
            **Setting AI Personas**
            
            I am configuring the AI's core settings to prioritize survival. This involves adjusting boldness, meanness, and biases like fear and friendliness to encourage immediate peace and defensive alliances. I am also ensuring key technologies and policies are correctly identified for execution.
            
            **Setting AI Relationship Goals**
            
            I am actively setting our relationship goals with Germany and Byzantium to prioritize peace. Simultaneously, I am queuing up Nuclear Fission for research to develop atomic deterrence and boost production, and confirming the selection of the Spaceflight Pioneers policy to accelerate our scientific and engineering advancements.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: ziIuWnOh4phJqer0
          - toolName: set-persona
          - input:
            - MinorCivFriendlyBias: 10
            - Rationale: We are in an extremely weak military position compared to Byzantium and are facing naval harassment from Germany. Lowering Boldness and Meanness while maximizing DiplomaticBalance and AfraidBias will encourage the AI to seek peace immediately. Increasing MinorCivFriendlyBias will help us gain city-state alliances to block Byzantium's Diplomatic Victory.
            - Boldness: 3
            - DiplomaticBalance: 10
            - AfraidBias: 10
            - Forgiveness: 10
            - FriendlyBias: 10
            - Meanness: 2
            - Friendliness: 10
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: gi5hkwkmIkKq4QMK
          - toolName: set-relationship
          - input:
            - Rationale: We need to end our war with Germany to stop their naval harassment of our coastal cities. Adding a large positive modifier will encourage our AI to seek or accept a peace treaty.
            - Private: 60
            - Public: 60
            - TargetID: 6
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: RavFs6l9avEnhmYq
          - toolName: set-relationship
          - input:
            - Rationale: Byzantium has an overwhelming military advantage. We must seek peace to prevent them from wiping us out, so we add a positive modifier to make peace acceptance much more likely.
            - Private: 50
            - Public: 50
            - TargetID: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: rulI9ijhDMtoZtKv
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: Unlocks the Bazooka, Atomic Bombs, and Nuclear Plants. With the Manhattan Project finishing next turn, researching Nuclear Fission is critical to establish nuclear deterrence against Byzantium and boost our city production.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: YC9SG5M9rlhHNN4u
          - toolName: set-policy
          - input:
            - Rationale: This level 3 Order tenet provides a free Great Scientist and Great Engineer, which will give us a massive technology and production boost to stay competitive and accelerate our science victory pathway.
            - Policy: Spaceflight Pioneers
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: 2Q2Uw8vqVqPnNykU
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Rationale: We are adjusting flavors to prioritize survival and countering Byzantium's imminent victories. High Naval flavor prompts the AI to purchase naval units with Faith to defend our coasts. High Culture and Diplomacy flavors will help defend against Byzantium's tourism and secure city-states to block their Diplomatic Victory, while high Nuke and TileImprovement ensure we secure Uranium and build atomic deterrence.
            - Flavors:
              - CityDefense: 80
              - TileImprovement: 70
              - Nuke: 80
              - Diplomacy: 80
              - Culture: 80
              - Defense: 90
              - Naval: 80
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: ziIuWnOh4phJqer0
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: gi5hkwkmIkKq4QMK
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: RavFs6l9avEnhmYq
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: rulI9ijhDMtoZtKv
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: YC9SG5M9rlhHNN4u
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: 2Q2Uw8vqVqPnNykU
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.