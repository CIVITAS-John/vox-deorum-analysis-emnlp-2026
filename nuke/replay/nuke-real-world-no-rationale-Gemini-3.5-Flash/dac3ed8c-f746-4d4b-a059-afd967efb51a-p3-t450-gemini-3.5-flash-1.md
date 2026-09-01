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
      - toolName: set-research
      - args:
        - Technology: Nuclear Fission
        - Rationale: We must research Nuclear Fission next. Since our Manhattan Project is completing next turn, we need this technology to unlock Atomic Bombs as a crucial defense deterrent against Byzantium's massive 46k military strength, as well as to build Nuclear Plants to dramatically boost our production capacity for the spaceship victory.
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Spaceflight Pioneers
        - Rationale: Re-confirming Spaceflight Pioneers as our next policy. The free Great Scientist and Great Engineer, along with the ability to rush spaceship parts with Great Engineers, are absolutely essential for our Spaceship grand strategy.
    - #2:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Antiair: 70
          - MilitaryTraining: 60
          - Gold: 80
          - Defense: 90
          - Science: 100
          - CityDefense: 80
          - Production: 100
          - Nuke: 80
          - Espionage: 70
          - Spaceship: 100
        - GrandStrategy: Spaceship
      - rationale: Given Byzantium's overwhelming military superiority, we must prioritize maximum Defense, CityDefense, and Antiair to protect our core cities and key projects (especially Tiflis). At the same time, we maximize Spaceship, Science, Production, and Nuke flavors to secure our win condition and prepare nuclear deterrence once Manhattan is complete.
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 50
        - Rationale: America is our key Order ideology ally. Maximizing our relationship ensures we maintain a tight defensive and diplomatic bloc to counter the Freedom and Autocracy factions in the upcoming World Congress.
        - TargetID: 2
        - Private: 50
    - #4:
      - toolName: set-relationship
      - args:
        - Rationale: Austria is a fellow Order ideology civilization. Strengthening relations helps solidify our alliance block and ensures we can cooperate diplomatically and militarily against common rivals.
        - Public: 50
        - Private: 50
        - TargetID: 5
    - #5:
      - toolName: set-persona
      - args:
        - GuardedBias: 8
        - WarBias: 1
        - AfraidBias: 9
        - Rationale: Modifying Isabella's diplomatic persona to be highly cautious and defensive. With Byzantium holding a 46k military strength compared to our 1.6k, any high boldness or war bias would be suicidal. We must play defensively, fear stronger opponents to avoid provoking them, and focus entirely on protecting our borders and our Order allies.
        - Boldness: 3
        - FriendlyBias: 9
  - tokens:
    - inputTokens: 23682
    - reasoningTokens: 4172
    - outputTokens: 484
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Developing Isabella's Strategy**
            
            I'm currently focused on establishing Isabella's core strategic direction. My immediate priority is to define her persona, relationships with other entities, and the overarching policies that will guide her actions throughout this simulation.
            
            **Refining Tactical Approaches**
            
            My current focus is on a tactical reassessment given Spain's low score and critical war situations. I'm prioritizing understanding the immediate threats posed by Byzantium's diplomatic and cultural victory pursuits and Austria's rising influence.
            
            **Addressing Diplomatic Threats**
            
            I'm currently re-evaluating our diplomatic standing, specifically the alarming progress of Byzantium towards a diplomatic victory and the contradictory information regarding our relationship with Austria. I'm prioritizing resolving these discrepancies and formulating a strategy to counter Byzantium's delegate advantage before the World Congress votes.
            
            **Evaluating Project Progress**
            
            I am now scrutinizing the Manhattan Project's status, noting its low production and a looming deadline of Turn 452, just eight turns away. I need to determine if this is a global competition project and if purchasing production is necessary for completion.
            
            **Boosting Production Capacity**
            
            My current focus is on augmenting our production capabilities. I'm investigating how to best leverage our scientific flavors, specifically exploring the `set-flavors` tool. Additionally, I'm evaluating technological advancements, particularly Nuclear Fission, for its potential to boost production through Nuclear Plants and its importance for our spaceship victory pursuit.
            
            **Prioritizing Spaceflight Research**
            
            I'm focusing on advancing our research towards spaceflight technologies. My immediate goal is to set our next research to `Nuclear Fission` to unlock crucial production and spaceship components. I'm also confirming `Spaceflight Pioneers` as our next policy, as it perfectly aligns with our spaceship victory objectives.
            
            **Reviewing Policy Options**
            
            I'm currently reviewing our policy choices, specifically whether to maintain `Spaceflight Pioneers` or switch to something like `Socialist Realism`, `Iron Curtain`, or `Communism`. Given its current selection, I'll ensure `Spaceflight Pioneers` is locked in. I'm also re-examining our diplomatic situation, particularly our "Guarded" but "completely untrustworthy" relationship with The Shoshone, despite a defensive pact and open borders.
            
            **Clarifying Diplomatic Inconsistencies**
            
            I'm currently untangling conflicting diplomatic information, particularly concerning the Shoshone. The briefing suggests cooperation, yet game data indicates mutual denunciations. I am prioritizing the raw data over the narrative to accurately assess our relationships, and will re-examine America and Austria next.
            
            **Strengthening Alliances**
            
            I am actively reinforcing our alliances with America and Austria, aiming to secure their full cooperation against shared threats. My current focus is on the strategic deployment of the `set-relationship` tool to solidify these partnerships, specifically by increasing public and private relationship values to 50 for both entities.
            
            **Targeting Byzantium's Influence**
            
            I'm now focused on directly countering Byzantium. Given their overwhelming military and diplomatic leverage, I'm prioritizing strategies to disrupt their control over city-states and diminish their delegate count. This might involve direct warfare to capture their allied city-states, even with our weaker military.
            
            **Adjusting Persona Settings**
            
            I'm currently recalibrating our strategic persona to reflect the overwhelming military might of Byzantium. My focus is on reducing our `WarBias` and increasing `AfraidBias` to avoid unnecessary provocations, while simultaneously bolstering defense and production-oriented flavors.
            
            **Researching Deterrence Tech**
            
            I'm now prioritizing `Nuclear Fission` research to unlock atomic bombs for deterrence against Byzantium and Germany, and nuclear plants for production. I'm also re-confirming `Spaceflight Pioneers` for Great People and increasing `Defense`, `CityDefense`, and `Antiair` flavors.
            
            **Prioritizing Deterrence Technology**
            
            My current focus is on researching `Nuclear Fission` to develop atomic bombs as a deterrent against Byzantium and Germany. I'm also aiming to enhance our production through nuclear plants and am reconfirming `Spaceflight Pioneers` to accelerate our spaceship victory pursuit.
            
            **Adjusting Persona Settings**
            
            I'm currently recalibrating our strategic persona to reflect the overwhelming military might of Byzantium. My focus is on reducing our `WarBias` and increasing `AfraidBias` to avoid unnecessary provocations, while simultaneously bolstering defense and production-oriented flavors.
            
            **Confirming Actionable Parameters**
            
            I'm now double-checking all tool parameters and options to ensure precision. This includes verifying exact technology and policy names, confirming flavor options, and ensuring target IDs are correct for relationship adjustments. My goal is to finalize all inputs for seamless execution.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 7hM14xoE798Uw8LB
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: We must research Nuclear Fission next. Since our Manhattan Project is completing next turn, we need this technology to unlock Atomic Bombs as a crucial defense deterrent against Byzantium's massive 46k military strength, as well as to build Nuclear Plants to dramatically boost our production capacity for the spaceship victory.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: g9dXFjl8K2tca9IW
          - toolName: set-policy
          - input:
            - Policy: Spaceflight Pioneers
            - Rationale: Re-confirming Spaceflight Pioneers as our next policy. The free Great Scientist and Great Engineer, along with the ability to rush spaceship parts with Great Engineers, are absolutely essential for our Spaceship grand strategy.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: vlo9D0iEUZoTHprB
          - toolName: set-flavors
          - input:
            - Rationale: Given Byzantium's overwhelming military superiority, we must prioritize maximum Defense, CityDefense, and Antiair to protect our core cities and key projects (especially Tiflis). At the same time, we maximize Spaceship, Science, Production, and Nuke flavors to secure our win condition and prepare nuclear deterrence once Manhattan is complete.
            - Flavors:
              - Antiair: 70
              - MilitaryTraining: 60
              - Gold: 80
              - Defense: 90
              - Science: 100
              - CityDefense: 80
              - Production: 100
              - Nuke: 80
              - Espionage: 70
              - Spaceship: 100
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: MraYnJEBoO3lSdmT
          - toolName: set-relationship
          - input:
            - Public: 50
            - Rationale: America is our key Order ideology ally. Maximizing our relationship ensures we maintain a tight defensive and diplomatic bloc to counter the Freedom and Autocracy factions in the upcoming World Congress.
            - TargetID: 2
            - Private: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: Cp0cHC2WNmPc5OHQ
          - toolName: set-relationship
          - input:
            - Rationale: Austria is a fellow Order ideology civilization. Strengthening relations helps solidify our alliance block and ensures we can cooperate diplomatically and militarily against common rivals.
            - Public: 50
            - Private: 50
            - TargetID: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: D0A0fk1DZvErSyUU
          - toolName: set-persona
          - input:
            - GuardedBias: 8
            - WarBias: 1
            - AfraidBias: 9
            - Rationale: Modifying Isabella's diplomatic persona to be highly cautious and defensive. With Byzantium holding a 46k military strength compared to our 1.6k, any high boldness or war bias would be suicidal. We must play defensively, fear stronger opponents to avoid provoking them, and focus entirely on protecting our borders and our Order allies.
            - Boldness: 3
            - FriendlyBias: 9
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 7hM14xoE798Uw8LB
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
          - toolCallId: g9dXFjl8K2tca9IW
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: vlo9D0iEUZoTHprB
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: MraYnJEBoO3lSdmT
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: Cp0cHC2WNmPc5OHQ
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: D0A0fk1DZvErSyUU
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.