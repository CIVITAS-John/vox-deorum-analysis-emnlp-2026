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
        - Flavors:
          - Antiair: 60
          - Gold: 70
          - Production: 100
          - Espionage: 70
          - Naval: 50
          - TileImprovement: 70
          - Nuke: 80
          - Defense: 80
          - CityDefense: 70
          - Spaceship: 90
          - Diplomacy: 60
          - Science: 100
        - GrandStrategy: Spaceship
      - rationale: We are adjusting flavors to respond to the critical naval and air threats from Germany and Byzantium. We need strong coastal and air defenses (Antiair, CityDefense, Defense) and naval units (Naval) to secure our borders, especially near Barcelona and Tiflis. Espionage and Diplomacy are increased to counter Byzantium's near-victory in the World Congress by contesting their city-state alliances. TileImprovement is prioritized to clear and mine the uranium node once Manhattan Project completes next turn, and Nuke is raised to build a deterrent. Science, Production, and Spaceship remain at maximum to ensure our path to a science victory is secure.
    - #1:
      - toolName: set-research
      - args:
        - Technology: Nuclear Fission
        - Rationale: With the Manhattan Project completing next turn in Tiflis, researching Nuclear Fission is the logical next step. It will unlock Bazookas for elite land defense and Atomic Bombs to establish a powerful strategic deterrent against our aggressive neighbors, Germany and Byzantium.
    - #2:
      - toolName: set-policy
      - args:
        - Policy: Spaceflight Pioneers
        - Rationale: Adopting Spaceflight Pioneers as our Level 3 Order tenet is critical for our Spaceship grand strategy. It provides a free Great Scientist and Great Engineer, enables us to use Great Engineers to hurry spaceship parts, and yields massive science boosts upon expending great people.
  - tokens:
    - inputTokens: 23718
    - reasoningTokens: 7861
    - outputTokens: 360
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Planning Next Steps**
            
            I am currently analyzing our strategic situation and available tools to determine the optimal path forward for Isabella after turn 449, considering all available options.
            
            **Choosing a Strategy**
            
            I'm currently evaluating the available Grand Strategies and Flavors to align with our immediate goals after turn 449, prioritizing actions that best position Isabella for future success.
            
            **Reviewing Strategic Alignment**
            
            I'm re-evaluating our chosen Grand Strategy and Flavors. It appears our current "Spaceflight Pioneers" policy aligns with "Rationalism" or "Industry," so I'm cross-referencing this with our ongoing research and current diplomatic state, especially given the ongoing conflicts.
            
            **Clarifying Diplomatic Status**
            
            I'm digging into the diplomatic tables, and it seems the briefing summary had a slight inaccuracy regarding Austria. My current understanding is that Austria is friendly, and our war is with Germany and Byzantium, not Austria. I'm cross-referencing this to ensure our strategic decisions are based on accurate intel.
            
            **Resolving Contradictions**
            
            I'm reconciling conflicting information about the Manhattan Project. One brief indicates it's nearly done, while another suggests it's years away. I'm also noting our war weariness and score disparities, realizing the urgency for defense.
            
            **Prioritizing Nuclear Research**
            
            My analysis confirms the Manhattan Project concludes next turn. I am prioritizing "Nuclear Fission" research to unlock crucial technologies like Atomic Bombs and Nuclear Plants, providing significant defensive and production advantages.
            
            **Securing Diplomatic Victory**
            
            I'm now prioritizing preventing Byzantium's diplomatic victory. Their high delegate count is a critical threat, and I'm analyzing city-state alliances to disrupt their path to World Leader, especially with the World Congress voting soon.
            
            **Analyzing Diplomatic Alliances**
            
            I'm currently processing the complex web of city-state allegiances. It's clear that many of our wartime adversaries, specifically Byzantium and Germany, have secured strong ties with key city-states, posing a significant obstacle to our influence and war efforts.
            
            **Disrupting Enemy Alliances**
            
            I'm realizing our current wars with Germany and Byzantium have triggered automatic wars with many of their allied city-states. This explains the widespread conflict and their strong delegate positions. I need to break these city-state alliances to weaken them and regain diplomatic footing.
            
            **Leveraging Diplomatic Assets**
            
            I'm analyzing our Great Diplomat's potential. While war hinders direct action with many city-states, I'm identifying friendly ones like Rio de Janeiro where influence can be boosted. The "Open Door" resolution is preventing city-state alliances for key players, which presents an opportunity.
            
            **Identifying Diplomatic Vulnerabilities**
            
            I'm examining the city-states aligned with Byzantium and Germany. While "Open Door" prevents them from allying with several key city-states, they still hold strong influence over others, which I need to exploit to weaken their delegate count and overall standing.
            
            **Assessing Diplomatic Threats**
            
            I'm analyzing Byzantium's delegate count and realizing their path to victory is tighter than initially thought. Their current influence on Shedet is permanent, but the upcoming World Congress offers avenues to disrupt their delegate acquisition. I'm prioritizing actions to counter their influence.
            
            **Disrupting Enemy Delegate Count**
            
            I'm now focused on disrupting Byzantium's delegate count to prevent their immediate diplomatic victory. I've identified that staging coups in key allied city-states with our spies, if possible, could directly reduce their delegates and offer a crucial advantage in the upcoming World Congress.
            
            **Adjusting Strategic Priorities**
            
            My focus has shifted to immediate defensive needs. I'm prioritizing strengthening our cities and military readiness to counter the threats posed by Germany and Byzantium, especially their naval presence. This requires a temporary adjustment of our research and development goals.
            
            **Securing Uranium Sources**
            
            I'm realizing our supposed uranium tile near Toledo is actually occupied by a Hacienda and lacks the resource. I must clear it and dispatch a Builder to find and improve a true uranium node before pursuing atomic weapons.
            
            **Researching Uranium Discovery**
            
            I am currently confirming which technology reveals Uranium in Vox Populi. My current understanding is that Atomic Theory is the prerequisite, and I am cross-referencing this to ensure I can secure the necessary uranium sources.
            
            **Improving Resource Acquisition**
            
            My thoughts clarify that Uranium has likely been revealed; the immediate task is clearing the existing Hacienda and constructing a Mine on the discovered node. I am also adjusting strategic flavors to prioritize defense, naval strength, tile improvements, and diplomacy, while maintaining high spaceship, science, and production focus.
            
            **Boosting Espionage Capability**
            
            I'm focusing on increasing our Espionage level to 60 or 70, enabling our spies to stage coups against Byzantium's allied city-states or defend against enemy agents. Simultaneously, I'm aiming for an 80 Nuke rating to leverage our completed Manhattan Project and establish nuclear deterrence.
            
            **Adjusting Diplomatic Posture**
            
            I am confirming our current diplomatic standings. While America and Austria are strong allies, the conflict with Germany and Byzantium complicates further diplomatic maneuvering. I'm focusing on securing our existing friendships and ensuring no unintended escalations occur, especially with Mongolia.
            
            **Clarifying Denouncement Status**
            
            I'm reassessing my understanding of our relationship with the Shoshone. It appears my previous belief of a friendship was inaccurate; current data indicates mutual denouncements and ideological differences, despite open borders and a defensive pact, which is a significant strategic complication I need to address immediately.
            
            **Reconciling Shoshone Relations**
            
            I'm untangling contradictory intelligence regarding the Shoshone. Despite diplomatic briefings indicating friendship and pacts, their denouncement of us and war with our allies suggests a far more complex and hostile reality that demands immediate strategic re-evaluation.
            
            **Correcting Shoshone Alliance**
            
            I've uncovered a critical discrepancy: the Shoshone have denounced us and are at war with our allies America and Austria. This fundamentally alters their role from a potential swing vote or ally to an enemy, requiring an immediate shift in strategic focus and diplomatic approach.
            
            **Clarifying Opponent Relationships**
            
            I'm sifting through conflicting intelligence on our relationships. It's now clear only America and Austria are true allies; Byzantium and Germany are outright enemies. Mongolia is a neighbor who denounces us and allies with Germany, and the Shoshone, despite open borders, have mutually denounced us.
            
            **Revising Strategic Interactions**
            
            I'm now factoring in the Shoshone's hostility due to their war with America and Austria. Their voting power in the World Congress directly opposes our interests, necessitating a revised strategy to counter their influence and potential alliances with Byzantium.
            
            **Adjusting Flavors**
            
            I am now revising our strategic flavors to prioritize defense and espionage. My focus is on enhancing city defense, countering naval threats from Germany, and bolstering our spy network against Byzantium's city-state alliances, all while ensuring continued progress in science.
            
            **Prioritizing Strategic Flavors**
            
            I'm re-balancing our strategic flavors to emphasize city defense, naval power, and espionage to counter immediate threats from Germany and Byzantium. I am also prioritizing tile improvements for crucial uranium acquisition while maintaining strong spaceship and science output.
            
            **Verifying Configuration Settings**
            
            I am now verifying the parameters for the `set-flavors` command, ensuring the Grand Strategy is set to "Spaceship" and that the flavor values align with our revised priorities for defense, espionage, and continued scientific advancement. I'm also confirming that research is set to "Nuclear Fission" and policies are correctly applied.
            
            **Refining Strategic Flavors**
            
            I'm fine-tuning the strategic flavors to bolster our defenses along the borders, especially near Barcelona and Tiflis. I'm also increasing Espionage and Diplomacy to counter Byzantium's impending World Congress victory, while prioritizing tile improvements for uranium acquisition and raising Nuke for deterrence.
            
            **Confirming Tool Selection**
            
            I'm confirming the toolset. It appears `set-flavors`, `set-research`, and `set-policy` are indeed the most appropriate. I'm now verifying exact technology and policy names from the options list to ensure valid inputs for these commands.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: OmhbkweBmKpwDnjW
          - toolName: set-flavors
          - input:
            - Rationale: We are adjusting flavors to respond to the critical naval and air threats from Germany and Byzantium. We need strong coastal and air defenses (Antiair, CityDefense, Defense) and naval units (Naval) to secure our borders, especially near Barcelona and Tiflis. Espionage and Diplomacy are increased to counter Byzantium's near-victory in the World Congress by contesting their city-state alliances. TileImprovement is prioritized to clear and mine the uranium node once Manhattan Project completes next turn, and Nuke is raised to build a deterrent. Science, Production, and Spaceship remain at maximum to ensure our path to a science victory is secure.
            - Flavors:
              - Antiair: 60
              - Gold: 70
              - Production: 100
              - Espionage: 70
              - Naval: 50
              - TileImprovement: 70
              - Nuke: 80
              - Defense: 80
              - CityDefense: 70
              - Spaceship: 90
              - Diplomacy: 60
              - Science: 100
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: jpMOjmkORr2zt39q
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: With the Manhattan Project completing next turn in Tiflis, researching Nuclear Fission is the logical next step. It will unlock Bazookas for elite land defense and Atomic Bombs to establish a powerful strategic deterrent against our aggressive neighbors, Germany and Byzantium.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 7PENspvgf7AK3TOb
          - toolName: set-policy
          - input:
            - Policy: Spaceflight Pioneers
            - Rationale: Adopting Spaceflight Pioneers as our Level 3 Order tenet is critical for our Spaceship grand strategy. It provides a free Great Scientist and Great Engineer, enables us to use Great Engineers to hurry spaceship parts, and yields massive science boosts upon expending great people.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: OmhbkweBmKpwDnjW
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a19rId7tdIM87m1OG+wIEV3SCaD8WoRfcbDi7U9McpK6eJzFlXqeQICMln08G4sDvpClTbTGmTxSQ6baRYl2o21QFBnmePWjObRcYHsWRUSKVt6h82vezFTrizpIm1LTcDDgDAK7T6EIp0DSsFaX2d6XQ7sHCX2SPV8yTPrYK3w5e/WCdlXc2LlmTmCcrT8UMXYPGtfqZr7o/sMu747/Wdtx7JrVtq31L2S4N6oLISXTMh2Jik3OWK0DJ1KztjCpGjLtgaBFlA1orWJys94m+qOdF46bM+RILl6mtMIMGNLtwkp0XjZ+fXmO3hNe/ALNexVJwylW33STDWrOzwp01EaOXwW1pDgNlpMEHkSyxO5BTP0zF5iReVikzHlFk6SQsUbmEhtIwTTATh9avBaA4x8SZF4fhBTKVoZk7O0lkl+7BQkDNSPUgkpgJ0AxKTXdVIcXbNRvTZ42wSOq5yfdTpMzx44W9sOWQuBclLiaYmAN2PZdef/eCCZuHE3rgErJ3FRHFT/nWUX/e1k5Ys2OkXv9FIJrsCCWSBJk11sCXl9DwtNBznXHF/27k6HYOPDbxu42C/n5h2Phq1WVTcQGddNCh9FRsXcRkWGCM9QTqoecZ51zg9PEl9FBJZhE2hZrORMMdO3nVAfIFdet3/spctevBWe+grm/eU17onywzjYFBo8GSP4PLbJ0mVVIEeOfIDbih70uvE9dEBLBceCdZ9lYJfP5hASbjC1tfZO8bK0bHKMR+za9Dx0qT7FbQyVo0FxIxk56Qx1erj620N44phQ1HfARcJ7/XIggVilDYqULTKQB+eOs9/HhepOaqZyOM7FRROSfZFJtyNvtXkWWxhBjR+5Q64NjAv/ecO3r3Ymcn0Osrm2JyAOFfok45llwWm4/TU7tae8abUuuSv3TxVfBUmlk0DzwV0Tupremw7CNiBdsHiDihoBiLnXFPiXINLEmp9HwDBMmQD8VACCVtZ2mIeJaqm2zGLBFMbyrilB9Uo8wM4nLs3Cq6MXy64Ru03Hmq1WL+DfgOa5Bnyq865JxaKnep+yxEzHqwYa1FSEnON1Dp9BHvCXtDwIXRtvatZet5BIyBrqWUqXbs8EqVP+FaKsU0YNJbKR8jTUkB73NMIyOyNzgRpPqRaOGC/QiUcFnWno+JSP0tQfE2m5hR/MiNce4M96py2iWhM0mUkkITbNvBMXGgWxSTuCDq6QiGk+YolONos9zVMLSF+BUyHQ+PaiuTScgLHXirbLD9JEOAwsvUh9zWYEJ26/N2m+nA9eLvRbNTZ/GD1bB1cJTQ1rEoLCl95uCAacYYVem6SY0xJKPYQzEr8uUNAgbUXeUdBYCfdCXL5vI+qXgpRCFThQMPr9xPRTIYSs/uqiJ7mHDsqhmrEaa1F4A2ADHUJcdNLPdyBV2XyofwKbnNtrTuCaj2VrF9bUQDwLeLOHLpLLkfoJDyYf3JFt/8Og+9JKmX9nYcFMQlcBoAp+zsqA42fBVDF0tfgTVWPHM+u3Ns5d2vI8NHd1HPtmKGiLw4GKQtt1q/zeObItF6vGE0n7nJOcPKOOPnqTLRRwi/FViPd697NrJAxJSnlyqKsU9RyoOV2qTinWDeyicH9ySMeJ49mbkt3IeC+9wadadA/ERkJO7NlszVLT+KT1MqH5viWV5JOEyULvsc+KchJw/4T2kFeopVhQcQ45gt3upz6aw/EP6Ye4qBOSj6CRTH2pOR6U4zjp2uvSZ7cgJ0cz4HuKN+srjeVEnwxwTHCK28Qyn8OsOfhB+D84ypd6bcqHQqbJvqQbolXNAkRygN/69XXAf+NKg0MIdqYrF9WENrk65I1FUtXj06Dz6pj2DirExoJQgQYpWJAL6HcNGpgdbRwRmZRF6ZiK9co+Zm4A5iN7z3ncf6rfhHSGWbEZhdehD25i406bQiE5Ry5tYzzNdle0NxscjOfd1k2tMvjj6Qra8Mj+FKf8TsMyQ5QOKzDB+SdG4CYsnZjeWKc91DjkbALap+iH0DLKIs+iiGN4KonLprHzLoz4UKFBNpCQSL89S78VYAseZWZS9qk+m6nR+I289WV9QXRO08rfXnVa+ktMedv+keltPR55wxzElGjmBUfxddH3c89aTZi6K+wqYKT1TKbnqPQGKs8jZjdt47rAmkjjH+87PMjhtjOsLabuLNTbRI2WTwIeYMFjGCVswjaSEWlb7UCoRhz/XwaQlawL1MLy0wT4gNuf9C/RvMzo5XKGmfiqbARR3FS6ycPDwoxM2RN1Sqyssk8F/jRTaQc339pIrX8J/z4lVTjFTWxvNqZWn7MLakbIyxgb+fG4WtDTor9UO0mHmZ/5Rxyl0bu8k4De3xEA9bzgHr6S2DFlefS3rpDUYRRcpe+waiofocuy9u0PTPs9/qclzwbDp+QHK6wS2/7Epz8yG0V/1FojV2/Th31YgymXUoRvCrBEeimnafVhOhQlBeqPexTN6MubbIMwwAqNSb+bYCIVus7wLrZoyvhTbV4GJIoSDdLg6MsgEG3sfpOalulbWoTsqEDGNnR40rcMljcW5szf93dXI50THsr4I02/6xAsXqw04oK3JlaD5wsX6U3jmkYLheoiKIxd1JCeb4PhcVxL9vahzYt63HU2DwZXkvJTqZyQl15hnwZzv94kWuEnp7q/89a4zdtnxFZkVJD4QmCqYJscQVkspKSuPD/Q9jJRdEjuAkgHlsy5vBhO9pLB84mGLPNWLr6N6U+KJiXraTzk/APT75hFDlK8pwPZ47E/Z8oXNwCRX1vDHjWrxMYnw+SnUbbtAwvlkhk+iWfZ4INAcA+APVAEEvLYFhoxYbFHg6UZSO63eiNpI3ub/glLoLwB2XPG7vkICq/tVZLNqe4rnq5Sn29sMCkielc2Gh3/aAvxk0DPoSQPfqt66/GksVCLnU81ZH10rgN23C9BvDAMUDppgeOYW9vR6q+s5clhMVKJ7j6iek4OyHaG0Ix4uh/Z0FESTyqZmY9qGRup5SICu62IVv5gkdofuDNJQ/7TXjp85NZ0p3g1ERwI6f0JmeasoZm9WFqzwPx/ctds8SWPcLvWmKR8ihC/U5ZMk3P0z5xdW5CX/iXKHWPfEjSQArkMSS/NXJzvUDquIrshtgq+rUBkuwQS3R3qZRjdLm27dJc/YgzDSQGJhul3SZmb0PPYbEBNZSfVzSi9i1cEV0NXF/Jixg3VM1+kCA3qxuNc3Makk9IGgPIZ0IvcLFzzNeG4x5/eDw4Fzuy3RgwoPrJgeHIO+JbLeEQfV0rNTNCLzS+1Ssb8gqU4qPvSzUSjvsVH+6CDPC1pOVMI+bDZpkM2h2ZOArBJUZgZrYifXiYOxsrtmMZ/mQNc1vwOnXpc0qgJ3hr/vEmFfpPEknYcEoyyVEdEIpiGxX0zEq8zyyfViLJH4MPLkKeWcON68KkrQ5RZX4ZT3POGfh0m33enQJvRLETBAyTE1Ad+s7Q3VyJFfRJEgsMXYKlhA3QoF3DO2FujbAiwJVPByVlYcadvk11BORISQ7cSAMfpCnFqG6fPCBY52DdPg2IHcT+LruemqnZVc9pCUzJWOAMBLV04n6NVL5i1Rw32vH9SlH8XHwUaqSqWE42quEaxzAhrSG16Ml+TpslgZlHp6QQSkhpF9rDPtPgfmYx2Az2T+0ATYBRWAi9wgF7Pb9Evt3meiYlH80Cj/IO8rmn1NmO7phL4osSiC2+467mKEbmAY/TN7v1Z4IAo/JgyACe6k6YG4h/NSZ/1m839iseAhEUYtkiAByLDXoR+yQ8rDBNvvq0VwUBHj3THT1t/oNlvLTfdsbecP0/pGSHG3lpXntfSDDfa9wptOrVUz5qyDIzwplOKL6ZC209IEE/eoY+FdfdlduhCcYKfHqdcHpVUisWx8BWCuoZd72Cj7Eaz3lUfN7+DYCmqcHSe4UwZV1CLzX9cB3vwUZFEiiTPQ9WubCffUjzOLjcF17s+UG/1V78J+X2vDKlOYD4k4z6mtcVc1/xdlzgYLzFYr+EBVzOUBsFT4W/bRs3pNVicr1lM22M3a/CfNJhiCU7gsczUn8oRSzUJiidQqNl6hN5sVqr7dOBrXVv44CyZr9fUE3RlXWlLravVPluyvObEahOrFC/hw+n01VVNjGdM/lRFlvHRu6QBvzYNZIEtAAQYu3zT4GU1FOrWLn35v5hze+JCk8hHoGm8ndyo4AS5EvHllbIMX7q14nDyMftwGCAzPRMC7ulNYfqr6TgF0EpY2670Bshdgm32OYteMv+p/2EiJT0piMlMtMqksYVaEHD2lZoIGPaLjb8rhv3e5i+Vjbjss6CE9VbqqwQ5hLtujcADbyF5YbTeGlEpuXLIXfeYhBYCpqxi20hk+0DV4r0iJLq6my/nS94YqqpcMNevnO56xOAKGqcE6BD8oJr9CNULBrTbTOaHXkhaIq+2bwUMZbBvjcFh5HvVP2dYZQnoE4SZrWlnwyi+g0kSMIfV6vRd8Tme27zP8l9g8QREIcmcm2puwjCXwJ05hTcKY2OcSoEvzPsXB3NB7K3a5aYk35J6jJjxQdjrzEQMVDNOWDeyNeQz+mDkNvA1SHE4ZJproPtWQ+ihu+GOqpn8q3uup1JLmTriAHl0b6NZB4+gAgImh3cLnM+Wmyha5gv4kLN4joTAacJZ4myzCuVFgfJkPBWD/np/dQh7DSJ5Ms9lG4Tot8/2nYe+zJg/J14Yq5hIJE8bUlzeBNxQqJP3FxMc4XPYfsN7cPajQNr139z9a9FWf07cyAH4onhpTaXJPX7qRk16+s1P6fRWzal3aHYLRVXpTCAdYQguZT2gs7grd9u6Eb6zNBjyzhj6RqZ9JQoyigzfGE72t0rCNmbZLc6uN+OvrWbV+PBNA7z0wcK50gRajjbRYSMgLBI6ImyV0uHkMT25XhSC8prgdseCUSp99HOcf200Hm0zaJ+csJVWOwpZiGuILorQeQXzYKQYOjZmQvwDDrrjWk1/rKUx0xYoUgrxx5L9iYVyLblWMci9x75MktwatME8hjCFNR+pQl7PM/KavUYqxZqCTT1aADJNgJmft/GPSkAgXtZnR5bIH+oxOsSJuPHWR47CqK8XVm3vEJ9tuZ6nziVZRDYbeMgd26sCXw+ByntLBD21uUKcrsNnJg4qDesWlafVYhGYAkUqyvESyfRIBLyeuHCmIWPiyGpJ37n4krirNVUR7EKU5uF3Omw3YnmK0JOUCYUNKElMG+dMj4qa4lt+38UlIk1v1ds+JOB+1lEeOfZVAvzZeTJr/lzod3E/PcI1qFMGEZJS4tU+CESJHqelh1obk5R/vjsCYXg2zzZDQ+H8MtE6ffouosCRDDJ1q+ZD8nK9hrfPZBYt3yVzabzceNJBcWw8mRSNvLENLzeUUGjM9FtAI2fo/KgALk7Y89p/apjsXDipNtlKIbGuyseN9ANj+J+gHWIphRtQTBH4yZAtdvf/Vd/o9JUzaQ/w/5BvWYG4YhrxGARh3tNSGN5lem9GH5X+UyxUGPaJxJAhSms+kQu5KoYgOjWq/EBoSfRJ4hVjKopp/hKF+VSFfYtGpwAyAJHlrWT6ybUoBCm9fHCyaEnUTMtdpZxNtYvn0N5eE90TQcQ8VeRWSEhTJiPD7wPdeFWJlRbqwro+aAguB0jyUJQBkLOA4DjC5ZEHATGBj1dPNiOgetkbhWpx+rCYQMIuUuSFlSrolDwZ46JzwaO9w+QBxw1PCDUu8wxnYMpeaZWpaU1piDw+GYL6wZuqsOtBsEhCp72f+I94UHO0Je0oebkCteG0EJfD0+qsfucJ+lQDxq4vhijLgg56L46bm9m1NmOKO/4K2aSc3Prbr6u/NfYY3oTjwUAM9snvOLqIhA0oUfXTSDq0Oa1Wxk/6Zt5G1EeyIIpgZyvvOsyRqPN/WNXiHYciWbcv3brjBs6Ppc33zjQv3nV/TAmtOTvAGMlO9pCP2sGBs30Dg8O3AErDt0I0Qe5wWnlqm5v8Y4VPYzzewso2Kb52pP7UW3xN7bhRmMM0Xbd2Vg6PYsMZwzj5hUQi1Sw+2yWS1rmAkGRV+EMQylUKskF9qNyYW/UUU7MRzbq0XSAH9eqP9Gcgtitdsmxa38nHfrAcxzWjdKkFa9OBpN+lSck1IjDEdGB+Ha6YQa9zOW5gM6IDt9OcUNpEy4gV++UauBG55+JMl1f564tUXCqak5n7VxAHvLEnziogGsUFeBUx/jcEYhFOjkwHoc9CaEkAYiQ0Tmu59DT5fBZqm3fivR+7fiDqJJaOP6w9o/Pnx6KuiUM8K0uccqa5xgKgENdhqQSuvCKV1cdwKdjA+qf9RpG01TqfbYAIcu/Urt3g9Afk6161coyr2MmKwq/nCIxE0u9hJ9d0hWDyJDNedoL5CwDIyFPfBJDdF2dGtXwj6+6mvzW39G+GlJNebKVHTr0P6/Z8wOz74zkm9zxOv/68cfmr1ZM/L54ii18jwSIuw9aMt9T7L9cH021xVMeiZC+RvwjWqNIcIAyQ22zRAZGnWlVOWaPCzY7e4ySduAcO5/44s64ktu7M8K4bUYmB+Q1oB7g1NE0ZgTFeQJu8ahgbUKnGFhk/3+br2wAxDBOly+4SEzDd+uzfQ21RAxMYiLb42ccYK9QAq5yor1H2f5Sw0zzRmVkfHyAlFWYcY5/b7h37vgCww4bCYPF2WttoPwVQcY8bRKEJ3GSK0T6DJwUnjHKwWeEMe+8mbFyxS+Ty2a3Wyho68lKkmiDNiN3l/rx01vKwoCvM5MhBxvKb8o8V7NpwOM2gYjH6/oW+ZY7Zp1Cmc2KhYtcJVhXEp/BNTZ1+m+LiwmGQaAfGMtHL4GRsI2DWxdGJ5kUWCY6tfM7Vp1Ib0tBRHx0BcWvv1LNxMVv3dULWJaNiJBIo0DODBbhMVM1wj1nh9QXShEIpI3xQv5SzXQShMSKiXGAdrnxReiub71Jj6r3qpI5JicGzsMB+x2eLFtE6TLi/r9b0iimJ8ZFMS2JLzmjtrZXFYH1lhPz5tO1m3CNkOByhuW6YgARcaDHKPXw6tgajUvx1AWKFyyNFslNdVTJffriMhc3mhIkbg8DJNdZfxNc9WkTV6XPvAnmg1iEbAhXRa9UzhIR/K+xfW+WoEbF1XWhKRKzt5/RQrolpxI9CZmwIs3UrloeYsyMTQ0ShVDozMslxAfDkkx2pqNME0ltXz/YSTN+JuuNq7ruVPLBiSRT418HoUkbLL/C92Yq0QIGyXvXdaMD0WIxILLXRa8M+SarBIuPHj+eCLHna3Lxeo4Qo5RI1RDqMqOR07TLocVlkhdX0VHam6qpVHutWWpO3FxVdsLxrIiNaQ5bHoQi3jhyu0jUPTecxzeV8kYaaAkwzEGCcJMAzPUdJMdY37XdLw67H30VD4djGCis/vEr3+3MYQzJw8zVFnLtL94gA2z2635RBls68bihotxzkB/AckMPHFPcSl2S4yem0JJAMwkkLRMI4v8ZEbmIBD3eAK1S6pAlBsVdbqcdhDC6VMlavrHkxLTVgmWqdHcrnikg8F8DWq944g/kk4SPSmk+Gu6n9uyH09aiUOCo4UWYPzvzxtqTfVyII6k3iE7smcAJpH4HN7YTpahzrQkB6y+Z9PjcHr9CfJ6MnfC6SFg+wqRj2KrmhnLmSlsZpwL/ftaidxtz0I69/uHDFEDFT3TWPcCnteX0rpcsEVk6AzE5VsP5wz6G7W+f70g4vhVRqoK/T4kYu0xWx2yrMFyMydUfOXBuaY1eWI0lfyHXExst9nHKnb+9tRwMEXVFAuG0CwpejqgLmh4NBW/x0kGqRVdSPg2Glw+PiTtvAxzFcssjv/Q0n5ljzyjaQZ+1JJrWUGQRSqse5EI0R6ivW2kwblkBSg9GeSbtnAPO7hvlxzqKR2xCcI5Eq2B//HSz/CVCckmey2VejrLjC5SKC/5cq/EjAYIDSC2D+cORBQJX/7XhZUhhsln1KXaNhq6Fy4rWPj4ZG2qyxowb0hvDBTnAKnEU5NtheTjFi42OppxhqbePrzBQoR6D+DzBVkwgiDpnSQzVEI0e2nOWzHTpU6f9OR13m978l3zuzTBcYT9M0rW9IF7q4uFLZQiZBcJSmZRYfmNWEMEPEa5eB+ZqNhjfC+31JDPEqfbehDTycF89Xn5h6VZB75ed8AP33PJg0pgxFOUqBdD2CCnE8fmyzzbX2Zbd7BX4rEgv4+wBk9XsTd14lQekcwiNWzxbszmMYMG96IInnNOczqyfVd4rI3RekN8lCWc5lc1568+B4ZpTwPiUYLgokHypCxzAAj+Uqm+3gucH5LD50vFtovA2iBeAnIWMfvYmNXsn1bmjBmd3BS0zvRv4HOiZa+I4Im8tHY4LqXiM6enpZPKxT9O+ZVv+FvdznuLzwnsO3XzwqtD5H1euxRuQsGpBN3aHJu3X6j20S3KrtQEmYazW+0AM8vpCio4k+JEHG68tMNIYYZ5tvVpZ0jaVa2Ge97Yza6L1UqCJSlmGTg9KM6F7auynDPc7GGWftzWR0ooKvo3HmgpoBunTcUXPdVoypuUILk0sInQg8n2sC6OUlvwTEqjQQLGh9nWjfGXYGaVkztmQn2F105duzEgwh1aFweW7xBNnqW1C/OaOwqCya6eIOjrJ1j5A5gY05DHAxel+dIZPTxQqhx5I67CmsAz6eBh/KCMWyVR72L85/lrN1gjZ2KP51CYR6zTe+VA/qBGY5+wp1n9snkiojZwwohoV3EpcrRcT+OyjD80eqRq7tIIKH9y1JuSdz9tyIOGJbY6JV18V9sUkg7N+lGZh5Le4lvhPAdDKKhZ/iV8XAUQ/d9SJC3qZleO+v7NiEgmvygte/e+mZTrBzbI8KTPolVkWfvweVXBIO9o7CqahzTbTeShCnUNY4OAdxrVx5CQL8RCyFiMa3PYF2gbGA1XG67SsgTuzZgln+wRzYULpZ3IUMN1S+ixLCzkuF38jpcPgTVhyvE6l+mGBvJ6bbmaZkznoU+mSuO0LGA+zXfPs3NoK+N4TVM7Ug+DU+5gonyVklZmKufODtmAIsaTfhBiNczeRN7neM9TNr9lpPTGtzEIO5rqKFHIO7sSGAuUm1fgRDDnDmGvW4GEHo/nGFmIl3q7kzTQavv+HeKmaiUD50fUQYmeric6BeVvB32brayRORymF59XTySDHV7p/lkxZYnx/YdNHIHCw5HB4F8upS+7w83h0ZElS/2uV05Yb7cF9lIbcHe1b90LbjpZpwUD1yfD1pJlezYgHVfwQhwQCmk87sWiLDuDFyOsWSQNmFsfhvj7llzI8SifjgjKJr6DK5TlBe++UgbSOTtTcHuIuVg+/1e/kOk/o3OWo68l+5fucxCrTWrEliQOugm8JZk2Pm71W5Z678zu++AOrCl97gZK+CNK2t8ulxSvgzpq0n41OK4qNn55LhYjYhXgfZ8GG6b8MPoIUOuZU+PPqUaGUFRnREzySD14DzjR/AFWkwalT4Ji9C3h7fM2A0vi/oDqUe/2skJvSeT8TdsaYZyTwfxEm590u08xs4sZDSW0XUJfe7NCVdHx9yCwtJqqPcvTEpWyKMIxV5eiMiPVnyXJYObXcE0TR2WA38PALM8K4pnSc2+xAX3LE/XBmybb4ZlkJwPelKHKM9EJ3XizaK9+h+dWOHO/2i5JHcSMJ819b72e17oueGzdm4kd+buzclQIbYaHnndANe41rQVzknkcD8n9Ha0M2hvi/V/coexwISGYP9E6T6yi8MezqlDR7t/Dvks+3zoAuM0M7TymkF6fjueYElRH6IezOu52mXyUHAyxxPLhYlFb9ReJHK+b0NQeVZ6uI9eJsMf+cM7mWkB6v/LdZnDfdZ0N6qGhcFgRpQaaqHL8TvE5Snl/yeWsAudtO2zHLPjZjhV2cimthg0kOcvACblW+lrwYZ7C6PsEhZzbzk44iaKbGS7v5i1zuB1Svu+j4aZyAhPtcWQIVSXe+nzG8MBtnev+V46S4iuXSCh/uG2GcnfM7PW+VQ5I23Pp2mwSnzKT5Xfdv62EsH0+AkB41YZSuxGIyplYFja6OPtdtQxkOVvpboY7kP6obufcux10KjdGXl11AoLXOayUSPj24VLHlgYShNlXA56UHpJCUvUdpSdae04EsFlRqJVceZTi2slgjHvenMzeD5kmoCQy32AhTrGofcfMeEzz858DC7w20XeY8RLC1DOA9lEmKDyIoIuFslIgcRIh/bN+WJRdvWcxkVv2rNmmLxi2R1BqkebokGA7ILcZpn5EnpkIUfcFWM0WQvSYXdnFs6ObMkpcoRo8IyXvrG0lOoqOK47W3aID+lijMxHr+84Z49K0crXVeQpf2pmLzSYSruWze9oIyzrZqg/9UuSl/rLHqJ4KLM39+E9HMTMDOn4c2WJNMQaCrmddoUOMTcOn5lEBEKexoTZ4bvfMdx2QV70F89F6KAF5ZVh20wnA/VdQT20QhiNqFG1ozuf6efhJahFIOxphN5qE5CNXw5X8lW5oJK06f8+sn/bT3aeGpuEVe5X8U4xPjU3xj6cT+l5kiElZ//XSbL94uWT7h2IO/KIMXWaiTrFIp36F0ExHXTXR5yGUtcm6sePrKjJdzDlv/xvImKXVaLoGD4owhK8ybGHUepxOMwcXlnNHjkITEDm8wp3wH7o8SIaVF0gnvae8E39G35Mz6TOPCiGsur7rBgIdFhMWBEVEoTsD71iLCsSKtatexjr+Ei1tQ/Z4vbPmRjcoD9WcBMVCyZ7w5zs4TrwqqDCAP8+0lHZ/4lDW3Sk9Vf2RbXFrpBU5ZhqB4kROvEbPwVgD9Ia/XOLo+9rsu5HCOdHwWVU20gDFB4JjgcuOJasqQAy71H1BjnPYwb6xpuofDcZXqWatXAj7Wq5R5J3D4yrSzQPNGKAOilm5u/A4p1/9P0e/OTc7R8n/dQNt9yovR0eFBhBTFByS+IMYPm5Fdi32aLVZw229CQrfePDeTBE+tDIaEjOJey2uey4zfbOL866qz6IWW9MjiCFmrcVeLxBC8bV8heDEaVLJXzIRWg1Z6gefDsRKHySTYcLBwJl03SlTsWAQ0dddKirv9kR+js5ApUPahGWxvKhn45NVaOV9C9PpLIhlOrM1YYD2Rsy8W1BejlBq1CRCPxpMQkdeCJq6dQYAc/PqXNKBHok6tNFutddIpo3SIKIv5+wwK8xl+qC9qfJQVKtfmXVN6J3Y39Q6rXSlEchYOHOisARQo1Bi3iSGjm+zCdCQAUULND43MoGAlS8Rh0DLDAxCgj84ghaNd1FtDsyDRYTtugfHT/4Zyntifvx4DGxCtMfvRRskkfsU/wDiN/srV0jBMEO0VWo1Fe5CXw1pk4aAWYPqF1QxmUqF36lkaJgh9921Kc8BWyrnO8UpPgZNU0m+vDfMRz7oy4xSm4mVrH+JBvoUIqImG/tn1oiic3FkLsL/JoTk9fm6jLyKD4XunI0qhziqCSs430Q11HSJKtehZ6u6JQJ5GOgh7crI6wexoi+6OHPkp0s54dncUNaGHHgPmp+6lulGizJA/xq34SGvt5yLAA1MrKJ2QJvTCs/DjJRSKWZ99L+Eizat2hIQEIuoigeFeTsEVTb0Sx8VQR3nfz1dNaa4ufKEZD1Fsxl4PcTxbFVN5s+Pw5APpfloxRUMLTTTYx2+a1wlKHww57th/n9Y9MRJBLrJhy3y86UC/xua3Y6pa/3ySf12UdotysOdYBH2WAs31eTqcxu1mP98Vp5/ucNvMCcodsa3usIWUJLP7OVvf1uhWiBH1ylD1poENfC9dzTiWSNBEfQwOvNOrUmpT46JtqFQrqMQRaTwiTzX1DpPjt4I+9HKqur0OrpcF47k9HGASVG3n7R7msif0dVuOxnvMldHNRtF+cf6p80h8/SB6tYJv8tZdeKKjE3RFyT1SyQHF3IgnGwuIXCBkrLf8v6u1W00O03I4ry3CoUMCFMPDWDnogtz49sBhSOfO3yAAovhwJQ4OehbGhIhtmpuhDVIXb/TKxhzu6VKpHySB6vFXPI2s1Kc7OrBbrK1VHuvsKF4nMLa1eCr2gnD8DtcsaEVO5gN9STkdMBPeVHIVmADFRMR/zNOFmhJIC3zKgM2XDGikx0OdeKeRP3c4ddf6VjF4ThJTxZuvXbIJgv8W4IPf/DEx883XOIWOwWQZDt0UqXvL1kMYD3I+YD0r48+rCJ7bvR0NQMhqU2UWaJ4bAXznUFDDiSHGB1qdqpNt4OPuijVi3Z/HhZZ9nVHpfEMDp6pcHYv91eqJRaAjJIH6PZPgp5xMhN2FYgb9NIPVFimUd0LOsgC748mnAsUYD7pDCiNg9FJCaw3r7vfj60EFOQNphFnjd89yoAICc+8ts2OvuqXZnCPOQXW47xERqxGeSLLZaHIJJdqan8pPrS+reLCSG+ZMm52VZ0FtCG3hPSGE7U8h6L4UiIFogF6B+Q28OnAtfNk3Cx/BUvJ5/TYZ6Kef4qiz1cfSlPxTEzJ0D/Na4qb/3cipcz/CibOTO/UWI6jZDcJzJVv8NEJBdSf+W2UNyDAS24k6ACE9HlWRbNlFaZ/9pSKNgMi6VjnIqjb959cMY0OWeNqJZEb6um8Z2t2zmdW0posQFCPWBzyDUotoARY4JZgD6Wj92lEuLJ1hYhnbcoaJR5sKi2qcL+9Q6OuuDxVIkSYSV0UNC4g7/hUGtntOJGh6u1oABx0JsiYsifeJULHUusoAgUZOlb6ayCn0flQhZ1LYOczRTR1i3C1b4G6Dgm8jE4ur3jPCm5EutIjQxEATMZaGOgQju6pWARrVyNx23kjC82pZzGo7AlSYxcUokZbd/xe33J6fHCYqsdUJ8gWEv9oKdjfc7RVBPsrYvcJ9taieXPyHoh/4krkdu9Og4qQGLgNSQhFcejGVd27IE8oltG6NNxFS7AnPQ3hXXnV9hT0r9MR5gnD4EiHc0gQJY1/PJ8aMK1LNQTXzjk+P3ogUwRFTibpnOmpszm0x8mZTITwU4qGocncEyc8pXOsaEy5mguk37NKbwADAugf+RFRVDWx5G53e5sU+S4PfH5Tw6vPs7TGsAqQXm4zixz9hvWLRyirp0IjjFZUEqovAzJ8X3QDHQxVyrHHjPAZqA2eNaEZkcc2m8Ss51n1IsunBRYfgK3V9IibxZ9f3ohhg4OTbVyNVc6qhfw8DgDvDuWwjOkv9Heu7EVbHeiPz7OKcIh+yx1cW+l3D0wdaP9RWpINJ6fmvcUiZHQ0hO6imtJz/vbEfiKGuIvz5VDhN9Jr3YLKTXWLmMO2W2+5vHVA/QLOe75DkJfW6/X/7xJbuGZK9Xo3OLOP+p1C9YiK0Me42zMnTjrBQdQBMH9mXDjdGxoVsGinWVIaAFfrRSZODoI/9qr3c3g0FYcIw5HRLOvXy/Cu2DbxQ+D1edrLseE7VFkeAlUONRGnhoNjqhB8cRwz3vVJ43RuHgZ0STckUaSisVxtepjBLofkh9WGip3X2RciiftVlXCyRqFHdi0M/cidlUnFdjau3NgUXPqF3o+EA6CrQJJOctIsobc33T0l20KwOPtE9GljUYr75R9SBnLVmBxJC00Mvn8PHEsgAx1dkG8Jl9ELusJ/8WiGZNX11qCWaoy6DoGaSTir1/CBZK+GVt+izP0jrbAdzUbNEiHB+yDVogdr07PsyalhbnhdkMQ1lPffry885a2Nb1nKqaqkwCV8pOLmlSCTZ3DRYxsgnXQH5T4tFQABE+ljBZZoNEDrgs/TWkjzF8xVh0P15VAsiipnWlu6x+poKtkrGEhh8T+Rldb+sziQO/KjdYblVpSco6BC3ph2rI6olOqtITa+CP1PGvQLLd1VgBhekkDGGjpad1Sc4+JNsVM+3tFISt8v1+YkPUiMrvpJX4JJBD4dvL+KQxfiDXZfOdSwLaVsF56YJoGyNFucQbJPJASMp0BDiFiv/zF1YWBKHocuNAgnCf0B0HdcsgalFnK8S3xvGf0f0SLRzCgRzEbwA8ua5ZO9XjGmUBjYI4D+Vj5mHg8eCX/VN+YvVIiKnluzCIjH2n1aX5jDkX6j1hV0zZxZ6QSXIQT8fHgEnMzUMs2aqgy0+HVNeZp7hs7rjfzd6Oc4EE+iC0M5O4J5ssEZivhiyZkNvafsaDpwxohkW6JgDWgm6L2drxE8SUjwLLZqomJePWyQQTmcQDo6oL5zod2HHUtS5dEw6FDWD/EJKB/habfq7j34kmDFNc0ZSHWWW0MBLv+3i+rjtw44PuswusE4vS1sAwcGkc8NsCraDRcsLtMPUy0i4gWqr1lmnQUOlyuGEcxpAAFZXx9f98EB9mVPCE/OMnWpNme8NWd3VSLh0YSoNnl8JuP9AwB4oAZw0+mYKgHVSGQBZ5ZBEgA9bhY0v10wN6Igrp65BaeS8zz+ZgRWiAHSSq5FLGyqyoGcdHkDFr2M5c7U/OmN7/BKvvAkaS8X1BWHLemA8TEyCv638PFZ1V2WjJRJebiBGbZ/tDMxfVUyQmPG6jvJQEZeRUgOte3cL/TqJywVvdIAP6dKLOgHPYEcZU0ZYWNBy1LXZPgFHi1IVGYvHIj7p8x89PzMvL96syZDVNcNCaLiwASfJLOuwcrSVrkwYxO99415MPR5iBMWc5vAm9dTjTWGGMIAPdpk7kUoxwRG94G8V5WKGDfTTY/K60RGQ8SQ0azLXpm7qMpbiaEWWiWkdYB/H6iwfZPMsmOUE3dVY3cy1opTgVkElTze9/STY4W5eSwpyW2IVeHh0kW4F9bv3476WdHoJp4uhUlKyMdJupjVp06QGwJ/ZcXJyuuQ37MOWtZ9dttnop2Jjl1zcUef68gp+d6ySM5JaO0P9CNdJ2V9+f/CvbJT/MC2Ihk2weMFCKR1yCywGxBUSRN7RSL33Z6dz61fGirgE0h+kl0w/6vAPmLBIm7HGRAU5Gm5opDCMlL5LL00H9ZeScj5i6iWRPhCjNX1MNx1IEPHe/NQ/+dtGthGTNVKIMcUYcsbJj2WUYj2bnQAdBZpEqREL4WViF+QoZkuuhGUllZdcefA+vRVETlAO+lY0oQZ362jOoO8s51qUrcL2+zBU/3owxk0sddkpTwhOIoOGObtlxD6bPCDPw3kxtTCkMKZY143oU+y9ZoXIS//KMqn5a3pXzKpSm0/mKVK0vFGI0buWp7KnP9IPm7bAB/Bj6obp/PxDCHk5oSpkLLqAsWcMxru1OJ2SWVS97XeTwMZeO2UCl4nR9jMfuGhb+febo+z/2BWfomaCsqXb7bso5Ez5NlmE5RSwbhw4SeyE4j8j69W+4Gsvh7EeqJzpvyjTH44C6JCoaNBtp29uklSlFgdL5Mi45EQMGskU4D79Dq6CJJmoS8OqLtQWgxNUCjkWq+HLPRr4mJkjDVqD6KDmh5dLgeVNtRo9BueIVk0ECMsdkdotGew49qIldp2FbzK3p9UJbnSMJdt2Ass495T+rH8Jj5RBr6/auQbBPEFrvza3t4nbl2ZvR471szmxemm5JJdfDBJ2vFN98rfRrrkgaLx0FAHOyQYI627upZUicGQJ3ub+ZCgEHhWz8xxSQwFGXS+6f8X/Vrj/Mjodvmi5IgbBs+iHULyQG+UXhoua/6C0jqNMkOsrqvZpkJisHHkZnMhqXZAAsz/UzDHYefhUNLMl8plW+qVjdDqJSzV18AytroDxgwC/WZnGGuAnderNRgkSxIzf9LLISr3oqEf91qb+KdFZlzI9ZclrCVNpyjJTqyauQ4KtLzkpuLP38NtwrFEtml1zcvtPgOMp9B3ZKRr50nh0hNp66KyZYuDctFfYqlRFFdQiw6YIefw+dtVZWqDitxstdM2CBxfyskHDUydJyIIJjd7rUNJPGJDnwxPN1qv9wpHkTz0lStiSHBcBsmVD2iVNbJJcen31zVZuzH7Fn7UB+XruMPwDAXEGgvhK41xpdwtVOi18VBSFbyoRRFWXpY4h7tlGVzts3MQwcaZtPPuCvBVysd0Pv22pyHqUIbnbrB7zr4e+IXnuTMgGFgra+D5AnulKKM5KnyiTiW/EugnFTSObQOSYKLGIRK/vrTOSeGyh5alSYqqlaQjqmkIdqZsHaCrn98s7VGt4RhSsG8yne6H/gOIyT791aswKktVNEjZkNbD4xOjdnZA5iE+Mo9BwJZw0CqRrlph9x4PJOd3l7Qm/1d8J0s3nsY2daNDX5w6/i3xYgoZy0Mi3PWywSUwi6PeCM3WJ5ob9BLvW31rG3XM2/Dm8vZsvg6/Jfr99qWXKcmQ38vRCyQwAhBasqMeoc9TFIIFzhCSS31ibwJWMMPbc6FdKJ0JUElNfm0FygB7QUxwfkTqV6DsW7yGy+Ao64dbC4fOTrJ6Vt+prO7G4hKse2oITJnjZrSRWqw8FkPdLuRr0zd5VcoS2us0HyjUeoM+59rSOQEPAWOrmFbraKt77ZzAojQTjUXzlt+URHLfMGMU0CwmtGaDtesdQwH7QcHz4YQHiyBcMQCFeyJ/EZd1GNqCPTwdp1kSI6aXTljeMz3YO+LKtWvyXZwIjfRrd8otJe1G6TmpXpZA4Fpn+ZQt8+hBtOantTOUX1E579pJIfvmkx+vVMaTAZzgO4MbhMR9/5SwCueVEJScb6luFdFV9nfbO+64xOJdBJN+FtSLK2MZezny6Tz9OFFK0/K12r+pDLqfL+Yv6DNEcsGo90EzBUf6GuqsRnZRLW5kJEbFapH/1hzEXaatgg/1+PwhCVjaCDssDV+P5n8E3hduHkj0M/sD9PYk02d0CPS75sIHJvgEBiHT4XNZyiGGYfvbBgqHP16BhWKFwumyxoQ8kC4Evk/XlMrnrVt74UzdTpyLyz+hfmUq8eWsBRzjMjV/V19DhE/HhsA15NzkE18FBDnQhxrRriYzl/d6kFprJir1KRzTkbaNc+rcjSFXRB0oUYNFUB56jW76fF73sO2q3V+BWO3GoyRj2jQiaJI9BVyYzmiu/wosLx9b0b2wcybrArEdFylhSW8TiMa/ri585MuzNZ4MC8inlK0WWV68gMc4fB7/iAvkjTdZ4wInnyem8OaXJBwZGzfox8qV1vdtmJ9qRNQqaRi1/ap51JPOqeetlobz7qacSVeysAPD24xPzxJOv84u2BZB+TvmCO0FLw+gQHCK2Ierv9dR/fjP9T24ovy/pR+8HG8usHSBlLJnKw4yLFSSjqrNb4CRkqLP79Jb5qz3BVt/v/TQMai4LggSUmf3lBuh+uUI4VzPAcLeyj8GGeO9ezeaP/RG6mXYEv1pZkW4all1iZ9W1FhVLPkApgKVH+AfmlqWu6JyV6eFEzjPO91dsZJvsk68nvFVdqJgfcHvdwsTjLGd3xSfe+omLM0xXw+YPhGHaFE6OXsX/Tz3h+De4W/1icZe7XBWGCmFauOtjntc+ZfNOJcFKKt4m3fa0SWz0bbmDIteoa22dOMv/hH6nGpk4ODR5CH0c2BAUuCTR3p2caCGFr1973LS6Za1hCSeWuECQqT49BQ+7n0NRhWcTZ0qDaRTVap0xewmThLLj5/N0Cts7cWLPQYIWV6M2HBK4ScqXn/sG3DreOXLyCZaFbCl/HmY3vQOQRxi1YbH318tPYnnJtTBrhpYUa943dfiSn5LK/cOO2Ti7NS7//h/IUIOzD4ddtfiruLLO2ALLza53vRcVeX0p/bHcgBilREJu+nECqAlTyaZyzm/zLMikp9m1u0d7dWhL6Y81BEafcQOl4YSIRhItbthOM53/693fq9HznMIQ5AqlnCcTUCB80H7h4QyE7+pn8SrgU+623klt2aQnUM7y55BBsFTx38GxnFrJSrLo2Tf/VuaM0/gX0M8NA2zKEAufbQ3Ri2iBrPHEcOlw4DqvUfakBpe8ysGMs96bo2J4swmAdWP27JyCizdUlsxmURHE+eTjcanfoAcjZFlQYBs649+/T1xrnfyviTW0Tz6tWnOB04EPBTK8ISqDetD36eFVRM/PEl8aM//uXumaJlhC6MSl3KKlGCVEyIk1SY87OakJ3Sr+KY4BfC+vbLr8cPEPfpCW55dItm3hoQ9qu78QwoIyZE/x/P17y1GMXkBDwtJ1MzTmtwi/PS5ogQMCDPNhiasbV8g2xJwe/TGjtUhK5cuaq35rzVWrQjOnkAByJboHoiw7E3omdkEY7XtKwNyrDbsrgA0uCPrD19f66h9QsO1AQOzThnqfF9+otvESm9j8iGOJeF7H2y+aSayVE+VdY2SmzZOmNqDm5mBr7RvW6L3HPkN80jFuRXv/t8F4Zp5DK23izr1LL6wVoqfXyw7LBNYBxZvPgXHulA38EJm22aLoeqqBkfEixkVelUreqihRvqzEQAlzezdVO9KO/0NxbK6MWEk0n7bnbg+XRMwaGL2ZreVMqwevbHMnd96Irgusrssy804//ZY+YrFW8cLmLXTkSjdPCIO5JEHQMdP1NmSjJ7liwDbKBuelrFb/6ZtBteVyixeH803WO/HDXQTq43YJXmeEMKFtiU8o+yqs967rug7XMAi6VStjOJi1kBcqGp7NNdapzktDmZDdO6zZmtD/f/IoQ80snzTaXYHt9CD0NT8JnBVfzgMhMox4ZY8UyHi2KPwCRS2uvCknQRuAFhceUTm/N7lkDhX6+NOXGD6446HXe+hFVCqVGxGzzSEG2gfiIXeMuSuHV2kfYwbuvM3mcbAo1NtlFft7y2hZcXb23/biD7k5rh6juChvmN1n364tXR0LK6oGihTfp9nfaAxnOrkhTrbtgvHaKLQWpCFyoY1+giIWTQxuuTfoC18dprsulZUue+Q9T3Oy7BX0q9OoNmb9zG5m0LmlCxgrLqa17Te9HpIiFQjkmtNSyn1Ndq0uTy93ceKHosB9+z7myl5eDfi1XM0MRrOH5HnMCu2oG0Fkm0HJhTNtyv2//5QAVXQ4SwRQokDE6HuaHnw6q+kERIrqLFoTphjg5Jlj8YDiMBWVhaL6f1P23+iI9PatzmTUcJQoPtq9AEPpKxwjZP1vxI9aM0VR9ZX8HqdbrSPskUcG/Mj488MMlwbt5RAg0qVyGLdtv5kRwbCfKukjlz5CBpwNkW5j3H8xvTYDlmxpti+VJjefZxUh1g/fnOLVBbeGLRk6ggLowUnRsbz8IKMac5FWA5O+c7NspnlRjESq9eMJriWgiJypRoWjrV9O8RYoXHshPSQuOPEmf6jYAmkWuoG+Nbu4gGmy/Qy6+KJdSCG5Zc9+1HGo93lA8Y0N7qJtlkVNv/IWPlzI7b9DiqAWEQ2iowVgF18RQsuLdDtwWjxS/HABxpqlR56uommsTxa30ghCPpxLhoYbFnFLdpHFMmyPzeoa0N39ih3EFjpT/vbVNRlfx0Yc2iFHvrfBufgQkQaiS0OPV17J9QhuzfG7Y/OSmjwo35AgPnDunpVB6/qT/5Ch9PH80uzdgoWTrp2qLVWopznFroAW3ygnllDjKtJx7KOQuQXF2WvugQZUQQCdUK6RzTc/AWthXJcF/jOoyVN8Zncd1n70qpDn1on7r7NlPWuDF85f+kvIgG7kyHmuis4252h24uhgXNOIpBIdLyMWQiH9kyMIF/tvVU+sXkGog0LFdU0P7gTDsCIDmPk+PGh8cNXxtSnLa211Yj2Jfx4CuLtP8r1uieSBe9qnzyc1I0H7aGqUnI6YYfYk2t5RzFODGgT3rrAfVDdcu1RKTbmdgsDLXE3auYBNC9+Ca0Jn0XEk7fuVL4WQol18ZEMvunTCsbWSoCh26XiIAj76irT+6+1CQVigDGVSMmIY4ZPbkqptHvFJciuKDeYtuJZ2U7rhALpi7fCcZd6r4FW3aOV/ozK2xntr9EUcEff3g0pQjE/IrDNqZwBi/5ufY10zRUJJ+vysA2XZZhYvMGEm9DpQsHLM9tv96EnKubde/lzoXji3Q7EHVQDh0tZ+JBC+ztH6U/b6sfDAw1udindSRUy6NmAg1WtjzVhhH2ImXf9ITO5+4wNac4uhsI9hxqTD1aAjtYxo3WZSNAyK7j3SSRrI3LWImidHzupgAgMuGO6OS+BTGXQKUfiwShHBwXWef9XEwJSa7yUZbsqVIQsyzWXzuqYVuUKZm8NMIBQCSlv1utsmksvPzcgoedCPOOitNdlZkuHG/Z+jM+IqrWAsmPE8Bcyw4Gvp7MRu1EHExdYMSO0b1jXZ0YoRApB4MFoS+GE7GQQ58resIDZLLZwerVH/59xxqmASDKPKejo5GRqvy3ehSfHgWz9RF3AC0lRWmO/FlrGAIPA67SNmQvPYmyQaKaiJRVCjCcG8bUt6cnsLMIHE5iosxh6n75yiYaFbSSMBD0N/PGtaTjWmumU+va6G8inLdKnVm3SK/VyQPWhX5Fao2bRjbwOwF9y6umyeKuzkQ6PtiQKqvbpxVG3041UTFDojkCaxPqr4LRjt4Los8eW1VVE8VX6ACXvD6A6qPbrm/fXQgKzoNdHyOeDMsEG7t6do/hwny7qivWMiibIjzoQZzSiJAvs+rCwKSKNnicTqJzAGQFNlljxK0HKUa/lMwwyuK2USG1IJrUfsdT12hk1fMXmbF7KmXouqGlSoG22c0S4ozsoDZWLZxQULAZE953PmEAs63zJlTe4ApQKfm3zw0eGVaccFM8zv8G1EbsYoiZBUh73M4Z9bT6e0hD6lSwXje4In6TtKIu3Vjkr1d6t9EhGUt8mOMRQFjCF3esbWeae/HGlipCKKNeYtNktivq7DVy9bzuteLp+JWHBSm4Jf4pX4wSGNYYPU0Zou2yDSMlbxxoW9WInb83+fRNTtL/hDs5UvJE6JLCt4UwhHOKcyl6MS5Ozpdg/PeH1iDY8VrDRNXDz+XiQ9jtLrUAjd0706yHbw7KrT7K2sQQo6yvmmLElbety8dxL8KNvqxGUoNm5cgxqNNvRAOd+E/vtnD01JpqJhD7+8PAwLzup+7ygYzpU2l3BWjHCOzBDkI0w75qa8jK0iJWgvWLsjIwMDK2mu7cnZ7TdXjuWUvQmikYKmKPWqxEo5Ti73AO+uysX0o0HFKLXJNJGq0Gq13SAGIumlwd1ZsT0CtaB0BeQbGZWj5XZ34kpcRlOqh5DwcUpz2k18ctmYcYA9ouwkXK2SWoGB84+tyJrP+X6uIWjnTxmvUhbGUN3h2lHwOJFdnhzjuVDcATndud2lk9ZqJdjYcPh/ZVCJCYvq2BMCr3pNyXD8Ao/CLNMvb6ns4wMjVZDjxJGn8ix+fUKE7h9ShxIBypeKCMXhfPyufrvQoFt7nJAmfTJQaMrviUUle19/reMIzDM07cYVp7JUsUE0/YuCdJmkgf+TjkIrj1BWrkL6wkBvVVviNuKIJechCeBd3ZAdh5qEsDZ1etnPhEFyNDbJpikQXDSaatVW+ABYWlcO6uZx1oCP6hDaJ++NX7/+gLd7DWfweqWd50LKxErZWj2njY6PUNz//NX8Ma1Bevg/3CgYarSVtfaxSiDmbnuCYeG/dYBEcz4M/K/DI3WAMFU6JWP5CPuW1HxQPo4GacKmAW2vU1ktFIb1uW8LVbIla+sPYZCcuhjWA3oZA8B3QFxdmEzzSzB2HkOkxwl7Hu7e312Jml1H5pFaU1dm6hxncd+0sy5XXC/LBSzqFcmXt9wKFd3Em/NhPxLkFOGMKzfYhJrS6N3ba+yV/kkXURIOAce2eNEmY31HEdk91beJTaLsjTfxV4tTWi8nI7Ef/waSnBDNgIie5bLiyeoqkqIWJ0QLB/YY839mtWK+8xA1+B0LFtqvA5Z+ClOslFPIm7p15VjM43ZeyDc3vcQVZMos77HXy3VxfbCoyI0bFchW6UVpAetusmG1Dqvj7Um610hw5I6xSxen8Suw8yuQaZAEJs0gSTYrM7JuYzR0A8WypcCqnQT3rbSffg+i5AqufpfMw1s/8fu7TY2AvyeU5+UMTf7AE/oDxe9IFG7trJFau9ksm07g68uTSb9RfZYQZ4pAG20BXRxdenS02hfu5gkOjr1qDI3K+rjjWDKkqfY2qJOYk7MKrg+KvP5sZrirVybCBjkRVka3hS5GQ7W++uLQNbpbV8GXGl3o1eOCZnh7Dke038HX44gWuZVwPioSMPC8Mwj3ulVvL4jCRHpjvXFJgKNF/+wDZK8BzqbHKzR00zfI1e+3lw2PJBNOoWJ9ycEdvpRwsbvqZSr87LGzzTC66STqqPi3rRfUqgyDm23xWW8IDDzTqgBf5iPAObQNHb7JPC291iBeNfuH6tSW4HHMlEJR8HKMKiotV+v6pgCzaTzsm1qut05SBDYhiKuVJfNpmTLR4IYb/4gDXFbbxvVl2rZa78vcFHnBoU4Lup+RCiAmhNNPxPr1+KGWff5q1QoCG719wzJn5NqKIXEWEqk3ZjR7D0seUVWOfQEmtcVLxpwtAeXWzJn00IidTjhHu5T4kFhKKr2rJ31jLAYl2Vv+XxIq6Oqn2ZMcCPyrc4Ke6PYoGlNsHzWWdwGsngdpSc6nemGVgNfAG0+aDH5MPIIgXN0tDMKVyFN0dmRS+K/2xP+Dq+xQOwrvIErK3VRFgTATfRn0fpprKSTrOTzDPvupTLbe9QJp3Jc4S2U40KPBzXMm1Yrku5dRzsjCnnLklC3aaxwX9Y2LV/QPnllsvMq0tIUDWgbOL4CWWapSbiwtm+PqOahLLHI+7e8p2JQzvwDCWF8W+W3eKz/X65R+IdsLY6kaJG2Glz7j3/qXkk9Iy2yxueveWBJ1ZihO4dw+IUCp27eMuzo6EdLiIcc8iUy6l22Et4nJwwMx3Qwqzu4kQFw8HCA7P/2EbIXEYQB9NbvPNAsCM3vATyUm+6ZpgxHEE/HOQUsTgyl+de0cZa1ImvslmUefuK9hzZqa9WvD8660EkCdIMv+nH9aRLaMUl6hKWMxKuv+Pj2T/95k1naxEjLEUuwAIt9ehBWFemsNtU06DCre63tFZ8CpIDu/gKxk8k5TNg89rNuDC3WY2k/meQlvUz8vrFw4CnzRsHJ690pBBp60DF5NZph/+r627F6cVYT/PE/xn7amZAwcQlU6FtebCpBocfxeHeeQ+M2DgBe2mKZgYCAdWFgPDTIWwPUh/xFK1VVn77yg5Co8AjpyYCP0YcuwN//VJyaHBUmk8VHgy3QRiV5WgKSyqEmNbhcAR9JOhBbqL+Xm+mCMkDITVz9/60tHY5x9lHztalkGxoXmsLOFkntwLwp01KB2em9GgNhzvQA2vJb6L2d/s2W/fzRs1sXDDuyW+FMFwAfF2r1IBFgzeboK4R537lr0KTa+IXtEghACdXcrFCdXJUl/JIB9/12aDe4eVE8rRLeePnKep2m9IoXfNU9zBCEQoJvtAdXyXNyy6CEBkozA49lTuQVYIAe3xFRr8Of9DfrzfkoioO7u/JS3sonUGk3jpQbr01TVAG5811KvmudhzldsG9H8LLYkzh6QIA3pgrgEQFxRin+UTmDpJMNcj88T6wFFVgXHGc3iAxa5N87G8aC3FjuPnzBlFkkq34N36vfYXNlHZK4NPbBv8doQA/5w8M4oJ7daNEymTAzKvZfr0p9/w5gCLB69uFaWjOWyXTinR4/vl8RusUCvMySjYmffcJYYB0m6koRywt91Bkh/09ZvnuPsL2Q6kwlEb5aaR4+cSVba5fGQqJaikblnX7lxXuWwHK8r20WJ+CWlmtBQ9ZNmzAHET7xhaH7yVvkXkn9KorwxCqHQNJHeB/r9DpYsPXM4XjP4r3NE4rBJLHc1X9BhygRQRhC36llUua2U+ZfPkVITvVXeK2egiLyeTd/ATJG+slLB7Wh3x1U1t70vUnX1Auv0NHzHBaaA8iuUcThct/iMotBZVYzV6+LMLSDRBcXsY9iiTfpDEKZXAYGYlvpLgAVwEzek6wBg0HpiHP/xb4ZdcR+iUg6dOS/V+tozaiXnMB2N7+eEdO6i+x/blhQdqRt/jx0oPn2pssixQA3HJVeL0K6QGYBfkwlmE0UNwxXh1/Sz8xf1ib1iiTlZmWXIh5D+utvWjRhw6DPaYdEqEqhVf9aBCU0syI0ZEbPDMEet483tFIiYXzjiDG3ZPfmPM05ec19n5XkhV6ofeQkZTs1XJXBznZDi6ONjQR4S6f0mpbhiEp3Ao2O42fTyYRokBz3CJrH57pP6QvSrhIzuCO+osQ4Uk4hqyAh5ShhhDACsPGsSVlDg1sEVihzxG3hsySTI3O809se05CmPZfBY4NWXzke8C+v0zWp7APwkHOpf8hblLSHPOtdQbCsSbiJu+sNU8vlLZeIsOUzfAPD64CuEarjNi7UQRavl2aLls9YwuHVHaENyRYca1NEPONfZQgGiVsZDgnmHBep8YYRp5Y//ta9OhGsRq0q+Xzup57UbxCvIdOMGdhEXnopQOhIYH0nzZNwMGXulY1CJ3o98qvTTAi5WbVK2cVLpc/BqAkjm1B4dxceMP6cPm5Yqj++NWKHTRruJfPrN4+W8mhbDa2I/Q32NaA/y1w4sxEqqoHdi+SH985uxVmkAapSqmsQA76bxPPh+dmFDxNKY5NGPKh83ulp3Z40nXcCaQiyTMh/HyhfR86H6FnjnMuQz+8sEhNe7C5cGwmOAKZtOorItAd6wUx4+toxFH+M9UIG8892M2ujzFqj+Pch2tUrkY8O4lvwNknDjK9xYduMkSSkByS9iETr+h4EQ1phruqIecRqRxaqwp5YfcGR9R+RIx/a4pVvZAb0Ek8fhQX3T9MGy7VIFxVRluBojBL74wzGxoCkLffxk4oKbqryszdlDbgzzcExctpqP7mkiZDW5VytF3XQzhl6XQAx83P5vqIefHVIV7nzI47WvjFgNb1GOkVnbeyV9UcfQxZtIOwVaRC1bJ5VwKTrNN8JxMZGpoEIdk+dF1c+VZvwXbtQg/LSXJ7v8SjwyqqdsetIZhKOSxURf2enHPhsAhCMkunUSYGujB7e477plUFw+DscWCrepvKzx23rx7bWj6H/HZzuyzfMfAHIu2xCTYLxTYp5TkupxJmBA/qHiGAKuvzEQpYstgeVLWere6t6RRDqObsT2dDJmHxncSjYltVPLJhY7Kf5xVfVRADeNsmSEjA337RRAEdwiKvzmkEwkwWBrtYyK0IZRo+dY0jZQ6X85l4zBhwgsVlekNWmzk5dyRnJ3yEYXC7txKBzYqmshRt7e8K9mTCHtNe4OUZO44lVmSkjwnxlGR7GntVGDfaZPHEmtxf89yv49fgnh1TrQkYgVATjfRR4V9Rd3hmdoOektqgnCGsYg81k1ORB3JoAr1/tcOLwXN6I8PJFzxag4yNgVpVN+WmjhRKGcw0Dk5lXVT21agO34IgjkcV2LdwQrjoTHVtRMt4462WRVtCUd2tFtIuZA+NUTR2NkDBpTX+uWKv7e0qKAbSR3JLaduak7yBaL8p4EoyB1wotlSO3Tq2mnsMeVIdip+/4S93NID3BWG9c+JFR4bul2+uH8FuUYhM5PbDezyw1Yf7b8AqNn5gKjfkDmnn3vc52GKZwBiIFcBcFQlhtGpYe+k5eGlO9daL6BSTdrNKUciIUHDn9KokeAEZjxDHD94Wle/ffdSEKd862oO9pKYuXwm0ImNZ1qx53za+JzwKij0pU03eNwqfGgQb3NXh1ohGmOHomr8+tTTkQelIZNRhhkW/XJ3rYEMdfUGk2sRJv0Z7ZFwo28WsDui7vQkkK5LtT4vGF+MJjrLw9U5Sd/V3D/PPd2VIXAjNWmgfbVfAJp0+ypk0jfU1hnO7sfreic2peZq2d6T14K5+bCrMQG48YYyFVZtDoWgYld5q5k2VlwX2G53EzHJWAHuk05APNN+ae4OYb6rMc5uHkYy3aOLBc8D4LZ2uM5QvGff3zM+1r68L9KcMG6yQiFFRE/AiKHY/gHPh5BgepKtsgwOFsZ9OqaazfUyf6/6Ay/4bFSj86R4qNi2gB8qek56pnL1svB3NNv3+Rj2KF+nhTLfrhfP1ot4QO/JHojh3akFHOGeZO+HtPHonPQA3/G/gykz4Ah85Pz9WF6zwrXL+8uG5l9GRzFrp4ynwlfxz7NvddOcj0vK0b4VrzY+Tsj1VMeQi0QBxdCyVivV9QG+Aa/zshoUBqYq/41uhiNYena/HC3ic2r1ig2RgSxsPRoo1VSTHTp6TUvYqeEYjGVRf/z6snSPxC6ZStUDznJCEuya6sTXGvomBxTQwpxMtju+6ke8euGNBo0Es1mx9FSr58/hSfC05CL6rYoNWsS2HQ8ifaB3CECk+T4f0sDhCDZfkkpP5wJJyfFl3cK12jrhEl5kUR+rC0TLgPkXj27vzu5OcufCq5Rw39ar/EXEbCbQxRtTq5PJDdG2gJIEgcQWKwPfCSsjJfPOU2kKAVwlF3X7bEo12gp+qM4qjutMGnmRJOIL6b0ie0KnAPHO1dkmQXzRqpILVBzmUlz3N3n5vbtFTtn7tUnGFp8/7WZLxnpeRuoLPcYwpc+gDT+V7InFk7dj2Vyx91CAZCICgErXXoww78pzcbizgu7S/R1Ju2ihDBtI5Ge4Ld33p+OoXpb8ezPHfHkHD4KMmss0JSl6cjNG9wElSOWfM4rMINlZSxkK2KAK99oewMiK6Q807BUubbb06scrwtbOgWGv4n1GU7bzmu7IdzXEJim4YxlMxQpajPLUwEHoFVlmpPsDpqOqxoPox2sgTeUm63DhKHMMCEf1aJIHfAgW9vCH5Pj4oUJumN0uNtCl2PmtdEcRwJjRF38KHPUhzPNDlvIahd8DjREvmb6X5bUpplwe4xGYt6RJZ6lrCTmGw3VaTOO4LBRSDSfVLiWvcOlq1TZ/uSRzhdkm6TOBCqbkV4QSPl0JcthHApcHD8oOPhFUKhst9Do0EGo4Hptu2Jql7rZo/RIqwZKhbs0rFP21ZSkQhQCaXZ8RF9u/9eo56Wph+844f4A+fvUQZ3aR1irh0fDqfSXitnu+P+qkMIfZZLIz1jf9+HhBUiFABEGFwRs5aOrsPGbL6EwNw7lpZJlgC8tl4mrQMGzQ6pfuQDUQJdd9v3/yD+Ayj9Nm9Lqz2RZ9Cma3w2vKzZ/DM+LQhmGdOM1mRf6Kn3FHQUtLqS98cXVeRBTVhbg7dyDvhEaFll0i+QCJMmX2WX8CtzxTrOQDrmUBWprVuFVC5lupfUPgf9x2JCZnXf25AGNwN/BYHVdcSfs2TJRa0z+EDfNDQsyD5EHIqR8DYKFmV/JsZmMXS4I4Lk9bkTC5KDVSLG9/bIbWQeUh8+24mH7D9r6KPBc/rtnGUfJn8Duws3v0XFkq7XMBmFQFDqwKEOCWY4AhEqqFVBts825HHaYh3OhaTeE/PshXLfqx5EnZ9iyFIgfRPOEAUpNNWvXGG3yBGoMN3t1xT8ixKr3SX1/0gSe1KgX5oDHHbJ75RsQXohJxFZ90/x7OL158/A/Gj/oFuoP8ekOGwAVRe/DZ/3pDsRzTKa6+U7QvjzH8aVar8TCS2VJKTdGQJFCreUWh5jV0066qiKRaoUwCLvYn8W8khAwMcxV+BrVJ4mOm91tJre4fw8V2MKGsihewEDHSOm1A2bXqk6nv90VncIoCLClnkBKbF3oOeVXeuM66Vn3TCwC4GbOGxYBPbe/FJjd596fY0Y+vNjXZL199d3JFs2OjZ9hLK47xZhe01dFyvImpj50kDdGyZoj2ETGRjOeENPuYqQVUor1yIg8TV5ydlfdVzKFjE7VxQF1Cjm/Kc0MKS7/XE59nW47Z5Sio2AUwQCOCxajTOBst5AslMAnaWxkE/aBbPhD8f6YlfyyWgUfyqZjMJaepWCNC4iEUMYe/rHpPeNd3mcefI1mg4zUKSmVDLMgOGG7vGMnSrkY+ZLkhbVMZENsydgqKDN35LJ5ADR5B0gu24b7BZscUcysnEypLx9TARX3lcVwhZx4M1nbJGvlcXoY5pG0xhKczt+iWKB5picZF15R31J3nkFtkF+7HcHNM+HIhWppw8zcn1YUdUygfTSUHKLlO0RYpYrRwiLdmRQ2TYaPTXJmvUlxWEGGVK4dxHnkqr/PLD3C8C/9zXipk95U6by4dj7ZxUzf8bsRHEXP2y948h4Ujhc6aUHGps+6f9vkqZYNizzDWd63lcUqX+f/RyrJvgs+eV73fcvjf65eYPHnZQRTl4l93FNO0IbgD8dkQrjpBQewRwrJ0xN4Vn51XKE/jGkePI9x3KrED6MsfNgwIDkL3L+03anTzqyM/6LPfqE8NilkL4QJV4Sf0G0sMijV7fKDIrOejTCl62iYZBt7mTNWAq6Mbk4PTFJcMf5TyOMcf7XnxuNJVL8qAIWIad2TIndV1i1plwjHjLYNyffqXJUf6vT2GkrINtqMFcudhzK4fALELIikkIIFCaluu/ch5f+aT41Cfml/3ABvQwup0F20H+tbok/CG56ri6yYS8VIC/aCfOd+Bv8g/Ic4Dv+CpUj3S294eoCZJQur/mcM4hFAOEcDIybbGvj974kmm8M7Kj1uHPrKoiln56HsY+UTr4UVVeNOuhH7/Y/q048sKlPiIPZ5PfcA3aFH5BtLberid0o9NdpaIsDTPUlOjtLroIGa4zYps8BUrOQldOHXftjl1dugsKcvL6h9IzuN7w45ZM3BkYqIw9tchNFJ3eCs270vI5Osn7N/Vd1M0rQIoI3sDE2kIuBn5BGZa5vVX8hThUsBG9AOn5G3H+4pT/6D5ZeJ/wYjCu/6qx+cPZOkTJi8ln5a7w9slJrje7w6Di+c8g+HyRnv9VSvE29+sTxHqiv1XpNYUTptqCSpn8ur0yQ3kUeQ7E3i10ekU8M4jHHbURcM7BbR/Khg/Qgg0vgtzjTgMm3dMdwT8uxtHSs4gYsAWJeq0DIxfZTQFwhIWi/wKX+b8QYAyTUZNexsCC5WyRgZEMOy1IhyAmiB9ovPKVcnIUUDh/dMyiSBrnWPsxEAZE9sooLJp7TDgPkOmAbS5c5aSKvTkVI4+Kn+X0BbUj5H60HDeBXujme6gjwS2QUakxOvmhzCcmh7qlOmkJBUc9qMw+3DLLCKsB6VpyARVJo192hzyudrL0wEytBG3Hus17zlMZr27bXItIW4KvxQF82/ke+2MQGoexZJW0DD9oly4ZN2CGyJnkRMQwWzfcikAFX/VR9fW5HPgOqRk973Oj7ZCG0bg0PRnspgAW/WUtKvEGP1mlPHqRJlIOemrvt9KMSQ1wa5PugPeA6oTUEBq+Lcxowvd45IttUj6KbUg7jgxLmFPc1giZzh7m9UGNvGMdqlvGC02aZqgqmRKTNsx6hDB1RDerv6iDnHFv/95FRDvUDl7BHYi10rh0jraUeRmrSmU8rJrbLI46IGKz0NqHbzKJKq5a0AbCUIH8xztcN5Dcgy+IpSp2BylnM9rUmwzQBKt6qUEF/Uw/uvy5Kd+t4apw+Gsw9z4A0Aj0sZBoA7sUe13hoSj7UZ/bWaRE57El7Nio6EFQnhBcIRQeqip27Hl/TnWl2nHW1+53BV8M+w4Fh7YhQrnxECItwq1LkdrCJ9iB3gmHA8GdeqPBs9jdDogrzN6VZqzj9Vs3mBuvc0d23+XlfhOWVms4CYEhIrt7gfY4WoBvhvEu7FgbRy29S8kxZad+llSigM9b/w2ULWi6Ubi6QFPIquHnNch69aGbSGTc6R3CqBSLdtg2frXkOjZaPq67tNyBy52Xm6S/rDFf1gkm0uYMkf7pB1qyz/qPntf4ary7hIJ1y/Zs6d0w2jn7EiDJScUZIVn/q5XB8iAMCYayAwZwi/gC7SgzPnErgwdmpjt4plNJ5aqsdYEvd8zw3/azaS/KN7hxzckOVHoCTGlJmAt5Q+vxdXVhV7pZgnNcc/sCHgfSw72uo1YMl/4rHng8VB6eDbPoaGaEAKxBxyH4t5By+I99xHeawIz5rcUyG1Vhc5pykNo72luv8XafT/6PJhEWTvxzijU0u6C/MTxXRoeK4R18dUvRQn1xGRxc2zXbPY/sqpBh26wiBpkMzSjaMaeTtmW+mAeSaTEACp3jB6dt/pBLJLMZdejjHEKDk3FwkFGrSu5AMcUE6MjrCmTqeOulA4hUcSQkIrAfQLpayt5vEZOTaotlEl5GZeZRpLnOi5uiMciJGI/cWE2S/qkkiYBOaqCpvyes+2I/F4wgbdOaiwnjTQrOav3bFHlwN0hZX+K+Kfcz4lYu4Fs5wWx7mlRLOFhod+gbFtZFjly+/82ZXga/wQTfTKvTu0tg0+z31kZB+TFaVQnbAIDv68/K7DI6+rrNxyIVl+GHvu3fkPSIcAEDfdumX9wMf/un1wZq6iuDR3W5PQvmIw1rXsI/bpmADQ9nEK2oK7P71NAadS7DB9P5ZcrafMftL2RftZC0nw3x7SUyJf5sLTcejxBCBIrhlV4xBytMg6Nw/uTZArRLJnHnu7h8A1H02oW0flFDO3gTWtnN63WPgQ6D/+KfhP24yzN5iwIvQxxvbJxNzGnPCBRQmacn2jXd2G9PKBvE7lZl0QYUmaxrtghUZO3/hGK+g14E/XZ3U+40DUqB2zo6fEcr6bkxgdAaoO/fuaq3HkYfMwbJ0GWFJucG+LljQeqWt+UWFOfurxVyARRHs4pRCbSY8S4IB3eh05+MiMwntmwnVMuFVMP7FxH0GGojas1MlagerflZC+mCFegVANP3jtn0DPGJPM02D65HylJfdk3T5Pi7xFtpvpVbdZKq8HELedb+4mWXR8OBwjYUArHyJBX9M0FZbjrF7EjWjfLaNDrRD5NTF2ffhl3qBkSSA49+2qf3TJMlMaHY/3mVzNRjeEhtx6MJMai1ODepHcCg8Rm8l7F4tyAlNLO5FFsSCl7L79vGcYLA4WQiflhxPq3MXbpqA32nwSOkDoAFaDkxptO+pzr5SI98Gwz+aP7zNW1vhzK6qcIuwStbdpTZbruq6vGsraSgCsJuB3+dJ9uc702LkA+OaX5t2DYSSaBJKdHGnLLr5obY8UjlJYe8Ze3PfMUkHYFKKJ0gHwSZw7jZOgyUfYhO9mpHD6eYGO4at6lba/YkovmsCTICA4W8lmdjd4k3MEsBDnB+IVDikF/527pRU3L4iY9uod25v6qij71Z6jje4j3ow1dl30awUCjGa28nMioblFqsEcoQ7SHkNl/U8riK8wFRqB27Xv11TxJFgm0fbuB9LUFcKk0jtIcKYSBt0IEC19LWy6Un0vjylAqU2X1w3ausITVTIF4x0SeMztNsvJSmHkWbzM6LPy0jnBQJq9HVSfQGU2hsWkApIbY3kbfF+8zF0wHXh23pSHVashTP7jeYWzekbwZJvq78RzoAsBIBenOvCofI2DcO7VdsJYaaU/EURgHbPVWXlP6/oP3kVe62lItFj4e72MgxF9/TjEu8UE56OvSoyyFCKPSd09MGbPn0ZfRda7mxUf9XXg91/remHg5BkjkHUsF1kK4rG8D+pqFFBVb9RaSBDraQvZkHmJn++9J+ugYKh/IISPpI+RESThsLKKHR2dTWgJqTxaxRT2tiFd1kWVf5BUhFtHOfMxwZpY+bJB01eKnsQlsCzT28aSoykKj0+m+sXfgLAd3zRFepZvlqPvIPKZqHfXKh8OZvTrrgFLRQGAwOX2SpTqZF5Va2debN+OBS8W7A6YbcaL0M3hxs5JUI2J51HmKvcQY37r6vr1VskNnyTjEELmowXnYRqIuuVawbgH9DVLGXg/k6KZri7HkWCMCLuUKY7AJY9wrnN7jjwrKe9pfbtBcMMtODEF9nHv3WJYhrcV8MrWoxWPlh9eryevCY77HM+W8aNP631MkYxaFSvAxi9EDpBgWMCfovXtarGXsxMuu5Slmpxf0wRnrr4U4eE/Iyd0yAUfTuxcxCMrPn9YufjKXVcUgSxDmBzUWSi/4bV7ZXCzHOtUjeeVl/vWOBm8POd7LZMnM+7DGFniReybueVHrQRIAY2hXEc8zBTpRb6KUmTQ8g6Y7mh7i2vb9BuA8SY4Awz0Ry4Sj3CbFcA0QyVkzkn1tZF39L6ek/vX4fsRtp/6U58g/JUm9q0DOpdza4VChMoY4hKDH5aODVoWXNQXg2S4+x93u81oqt+a3b/Qz9tWXColTQ7K8jCu2Sy9GFS2r9WMlw6NES4otFGYQZr5EpI+Bv6Y1+1748Uw5Afehk2iDiTovIdea9DPPJN/+G/WqJqHiFSfZQ4WVmL0kLnSfzQypskX3kh6j5Pon+nJZzLEA/KElF7iFsvNMAIz6RV57hDA+PZ3ZlSCEAxDllbR0HGopF22L6TqhVJj8eHDwLXyuC0EKMMhwHl3cb9iccrzLGe0oMaJJvvyUl1DBzexrCPAyYP7Bu4Q3AJRyY6YYqGtB2HpU/6p12Pr5BAX4ZKUlT2ZMkVVwpbAQnBWqFD9ig3uZE69MUCkKiFC7gZhvPlc8RUCHR+TGwmCwJcTH/WiomFQZyd7WAbEhls6WvO4M1swi3+kCVX/epQymDxXV9vqTI/cl2du8kW25z3FzLsag8c0NqLTaWymc1Ohj0KNTpc3DDVLvBVbozL62/QfO3uI4/AOxh+PRHtOuuJD6UQXpMySYhWfEQzVnAEmnpT0qHgpI0AtJhS3e6UsIGBIn4sqDZ/a/l2zkpeWF8e1MefBrH2lMLBbkT9afg6OEliilGcQP1xb1s1a9FSsX7LFxS5ohaf94UWWyKYNXaQxFVQUkQ98lX0ED2jCEbJS7BhM54pNbUAQGPTxW6BsdetxhckcEbsqaDOz+0afncFLIE4Kr2+mTzdzZxBba9tzelgW7xMG7br1xEMhuZmTIHz1TSaD4HkPhXcdfaiuHIO23LX5OvDwfpO/d1lS8YbN61NDxa1DgCjQf6YoCRSr5HNj5vljQg8O8mw1QwgIpXnjMMvwyPr8J/dTXCK8aZQDNpYtrz1xQKnpDHVLvhhm+2xq+D70YZQjlzCxDhPw2wwU3DLdWzrjgQgGB6GOd2DsyKkGl8HCQqpI/+bB37OlQGfH+xe8iQTpoyA0vjZColplSgNx7tfHUTNlEZ7QnWlf1d5SSHLQvC1a0nzYjjs/BYJYC8qUJ6zxGwVCxDALx9PX46C3BbbSxgGOSQM57wMVTmDab67BgoqdjR1tkr+T1DGLv+xZ6vgS17zCDrEXnACbL/qI5Lzzw65MgO/8iqh+ycCpwdLQ4eHf36SQOS0rjduN3ynL12eNcfc+QgmvMWA9XxV/zz069WShQi/FP4TVGMFfelOAU8OZwrvo7sgXMIIYpsFNXEwmJrTLUpbPANNosD25j+UoM7gkrK4bv+GiY7vUt5aWF47/woroLMDszrAQH0Th5uh5AW08Kp/4Cst/5ocEEsrlt1WlfRgv3qXKDoTseFXPkBTABsc9fzAzfmlf0zCAnUbut2nsz7POrCCcRUPDTHPaFkMrXPBqWXBWnCQNVbZ3mPdMtdz1kaeRj2UZwo3JBpM/xC/0IlAMaFrSkCK3JBYt1D7y8aUU7Zay9wWL5+GryFUtMfp9jLsOBkKtICL5CMOKoJleucqCxOJQsej9DfZoFP05+R81annelL0rc+1uY8QLmEO2D5hoIFz1XJyoSQm6XPJ64h2EEuLjOST0vmYMqg24NAU8pSXd9czZoVtBIYB3O4CRGjsPyRqveGMDYVSgnXpuwteZp8AvUbvFafUcjcUGAdWCvSTTqWtY3qkOk+20Rwj0USWxzI3eaT7r+ZPQP2ukaMRk+bDYYE2M06JANafoE61w5ZGCYcEsKElYZ1jnpohwj+Vym/YtmxFVud5B1CnEA4zp/eDWq8yur2kiIS8fCvwG22+oYR1Y77Zk4tNkry7ezrKN8ZT9fGcQSKT5X2eQYeJ4ShBMM7X6nyKElx/AkD/4sSyaqISihtcvfaTYkLd1pKcjyg3Wl1rTHradvWbeoBPNjPF6uVP6Y3oXsqxmmHs2onwg7uQqnkcqpgcqAZaZy2lXjkbGnF9fPMx9jaAMexC0yRJGjsp8X7ZJXI77wriwBJvzXvn/+Q4VQDlg1migVuclq5xX6Li+M6kjgfRznQnForx9mOCkQK2bDCJD7G06LKHykWXm6Y+bcZgezlydOgCv4mWhu12HXdCj7oPC2jXTfrzV+7jQpKqA71v1tjinHeq+Cn0/+hvzGfDIYIxob3L8ZCLFZU8xr3ueJeKAZadZQRn8r8sr00IXKOid3inABYFs5W6lr0Hn0lbvOvtJHkPoqsQGVwrnKNyg2MwrTQpWj77zOfAArsBxDe1gCC4+aDRtlGxxuZLDAskmjHyYttJyOcGquAnl0XNyfxugIUjgellYBW1PRTlDlOPlL0HV9jMiZV1MbQVpfFl2HqvKl4l+w6wWmtVL8bjLcxGjGfDJEV/HoOunpv92gYPmGS5GfO2S+z1Gshm+BXWF2w5jUgGaQ1xahylVr5WQ3JmJsgHrWNLRTklqQNg0P0Z6FihrWHOyzPlNHliKV0FKP0MG1oClVTV4iC+GXgvQXtro6YYP9rehvKtDo6NOxx399VUS+7kgUZlWbaMVpP4hx3IcryszvBewA1vhmdk3qZvRG/Oj7nrmqGNqTv0FbSvR6fimCU0TdxQYsAxOzj7OzIM+jz4zJ8haihfXAClGLzxot80I0NkOW7FoED3wkZalKVKj4sZN9SmLVEd5Z/ohM+FgKvL9CXzevskmfZQaefPCsPLFaMP2fyzsQ17ddEE60iC0smhbwYeAzh+jlGczVVXJjJi60LkvXScR/c7ECwXzQPpzsBL4xorRUj5ITzmfrN66/3RiC2bZPLryCduaYgAwXrp3dLAcz7GT0Wj6R1SPAAFeWmea/XOCjPn7Dsl8GsFRiu0WqzjrQvugwkFLWHDq0/7iXn5pGN2lBL0OYwBJuW+fBhRVfKQmtdpFYvXjmTpAvxA/gwwtE/l7aNyD+1vSSSCed8lQ/As2S2F3iBmt1wy798w342MLMUJnok73l/ZYfBtP0LRYV/KaIkLHyHOAaWHOr0+4b+0Rfx+52c0e4nRXqbeyq9YxmNy+hpVvWch59gsRwIpYBxqZ8BFX+m47C4oBMZeeXY47/plXiiqjAHCp5lYEDZdbWIfduQMdP+8T93R70t6MQnkSeqT/PipXZyA7LuQpB8gU2WC/wzCyCrCx0tckLz4lEFLGufFP1KDfyGS6F1+g9k7ahyRBseoyyC+RAnXp0k1+RD2O6d6niRSiwGs2jgUKAveWAd5WWN8IZRaHE1FPGAPIwp2G6j7IUwxdDVvJXLZB27ozJ+4o5MONot9vzSOLp9TWSBtS5bftvE3D8HHvpOc0KNHwI5v38sKY/w7pvGu+AYj6s33imzFCctGyhi0IdBRLD+djJ07hB/4HB+vWYk8KE/eQI+n1pL9o2kkRtUbjHm6qfYVofGiHO+EkC7AaJxrpkV3XS8CMUiEoXcBvgFUR4drVjKX/U0pacu33wUolvmIo88seOOkadxU4a/uHtb1e0Ztey7T2gZs31+/smWFwpItrT0oPrSVubklbRyNjmQfBOX2I8tG5HM1AHVvNmmGw819UAbWeaS48ChFLUcvkx8D5fGsuRjwwanGHFbsYwxNyjG/dG4GURgTvIS3wK/KFe7e+xfkr0YO9dfIhdO70Lo2HmO9Olu5apfsM+gjX1JkS2vX/G+xAHOYzB07BQp6579g8gQXJ79MCqyzrmTs6J/zEx5ICkLAL6XJO3daiKWjIx+cyA/Y9DKEqJCFO22kifZYhdwtwPMbKqrJ8YiTJ11qYwpmJ0AjaI44hHPVhjIVGu4Fwdjp4itmw94qTKwqTXnde6Isb8TBqRfR3eXMbE3Mud8CHPWl1mSCROpsl7dXS0zGu8RYMTDqMK9RRMXHHkgHxgXrqE8ZJI740RHqq62zSuuf12XrJpfovZ8dNVrkfHifzsBciUoZrSHESP9/P5wRAOcoeHAl/uXh6oSzlJ5efLdQcwa8AzYuKnsgEFc9bprdjzsKQMSxE74RLVADaojxpU8LYo/YArLrkN3tHS01fCn8RDH5ue1t4Ec3/oLYKu1kC9lEZmMn7y4fFm/wRXP5xhlNQyqF+gn//QB+QexCngqZoQrAlbspdlSbUS5CzlNrwsSzwYKAPLDXzQXwujorrm3quCGg/jOyGsvp75NW3z22CSlcPQzffluAsLmXqh7xLLWqRuX9VTSmgUGlhcc5efhYNCNas5IOP5ufp8IQl4dXPazKfKPWVq5MZQJLnD2hIJQKFQKxwLYIL/QK6nsqRfRuBhReXdn3VA4mk9QQ37ojsgW7jG1tNWDgwuwv2lZLxK9KWypJvETidcj6siKL8h00pNkOQQpNuj6lrd3fnyLBskQc2llATDDTxO4gzWUM1iG/iiAlKviyd6xoPP4FaX8Z6dbf9tn6f9vWxPkKpuvFHNuhOFebv6yKfWlkjmguBm/SZUosQRWuW692AnY71NIOuDQ5HrGTSofZKkHSjZWDVljieNoCNuDHhuLwEB7/lxJ+hwk9vEXx6YazNsb32FF2iZaV3gBLZVSwk1QrNE651c2h9QOiyGDJWOpzuqtTpB14Z/7aN475EVhm9svTVBqYWG5PABU1WTvA5BRXM24mZRZzTc6I7HHIzclgHx8W9JSv5l2nm2XbXeZh/tLzG4PWF7a3PW9gcdscnpPv4vBhG/SMlW+sf+UXpvlHzZSDIqFcyD5cjW/ShaPjuR5s5w99Dwu4Hb/M1WPndb/1T8jH07MkufOqtxasZBCbxKcLJw4TooFi2UeXmAkdpURCsJOgScFmPSBnoh4tzYGWBXLTT5Pir2I0JEF37m8Y4aWE9J/p5AllxwQmlSEgTbVgUbXFK/fEJosMFWsyWoXoLedQ2FZSDrERKiiY7GdASgnbpDs1HgglwvjpwtlUUYL8p+498z7TTv0D7lLkOW6oxsQon33H430sdslsoVG5SAkrp+am9rgtr2UBs1Bw7k/5GvwqHeY/mEi3uwvxlb4VIBODLegZc71UxF9wOWqUjMjkUjIzW0FI0fsFGgWK7J/FXVY22fUGMDp72d0saJ/UC4vL2HqOmucqyVC29TmaF2it6h+3Qa4BPTf4wDhXlB/vKvIvDpiBojJ36JwtO2vJeJsB/g9RO7ppK0naDfrRdnL00zVlfkx3TOm4piZFwdgxtDUFH1JnYx/FQEtOCOZvP03ugUXrxWQiCIFn/3o58sbWX46hAZsFvinlJBGkZjOjsamJk324WiEbp6RYyaCLxWMz9l//VQiqyBm4NiwHA4JtMxOtaney56aOEFv+MvT4S/vzVyur+gNWAjcnaNk7v+R7hwMqd5EURkNon4rUvfHUYVkA9Kn2TtowGfc8ZoEj+YI+EpqrHCJ7HCn5evHCguaiKz5G1H/H1EFbcPaqDzeSFHpkLU8j3Vf1bPFA5Z+K+fB4j1dm4GikGtpOrtkb9ph3S8HRv/ke/u3FOAdW3sQ7f4ORs/Z6ege7UGRZUwbM5Ts++bR7MRdaYgI2sf0RsSA3EbhuSigw/tLc9+/MARIEPFOhljQHsGXW1C2Xr8g2NhXUBGHKcUE6Ag4UXVLoJ2TGuFzGGf0FR0m4xMwWMG6ifgcYbtTxtQT3gxWxHGgAp9/0Kvp8Crvurwk3q1oaydR8fyajeqYkFm7jpy16WLsQdKJgPKjvgIYlUk2BrElJ1k4Lmt9SUmi19BQj6PmDJIunJrDbTEJKplQgioQ4dxs4qMQFW7uH4o8NYE/uxr8Xz2QDPByj8bREHbUtKQf49Qb3RBDhyvN2cNpcW+pWbCFpxKViIWrpuRhmQOGt3b1kC+JfP2ED58dvQiXU9dUKmbT1oFWeUZLCjUpOvS1jsroUoWDKSSsh0AKccQDDwdJP7tGD6IoEiyd76REz8gZg9jU2Cf0/smo+Bumi7/7gbuUojC/WQbO9f6JjJDbA7VcEi2XnNFxlKR7d9Ai+CuWe4K0N8kwvYOyOh4McEUttk6wTjEv3TrTtyz6IX02McD8g7vNyICKvPRD31M9O+dGNfcShlDv3pv1a/aOcekG5hbj1rDeoOP9xqTkgYfcrutUQIfkbwZF20TPFunhKTI39lwVDrzEayFxwkAG3tbDsFPf36iFRxt9pVSStoYPpUzJnwdLUrx8lSqaVa7BquGLxhh+LnACwOzA6uWnBG2MwSY9hgdlYfCbYl4B8Z5W0SaXHCyJE29RPfIb03dU2RFEEoGBohT/qbnX4UC5GDtSXNAqs4TQPA22DvY5+m93bBSJ8OeMHA1rb0WbKOV05egoYBCTAEa+DKAbP3i+WNfcKoLAMVD9Ttif3IWTw815VRbxby0Gy0BYLCPM0vnr+dSmLub+0vt8Ls4esXZBCY+s7hAE/OlFczor75Z8Nllqvlv10j/An2J1BmqdZ4K25kssk3aRlxYgZQcMyBi72rLvs3mI+JhtEXUao+ZF92ueCX3M4qKcewISgyvwjpcypG8cSXe3NtaiHKj44TdwbJ4TO0rIT8IE1ByRU+dyd8bo7dwLpshjmNRMbUTVl5r/oyTSKNkRhzZQ6Kafzn7x8yhkg2VWyMf5XaVey4JjiDDlyrz53hDGM1Bo7DdfX5JK7AQPdi9fT3+/QFhA81SkE/UjXO8GuX6HAVspaqOkMs2I3EqUVCVHJKtPIWcUQ2UcPo1hWtHPTliJEdzunr9H33EPSUqZ/2+bIWsIYShPPY1nFi7lf9YZ8A+NkGBs1MwYjxhI99ABUXeKADOF+Tpx6isoDx2R1dAlVvQcjBKBVyyZoSkrgDEeF3fGixeMHH+T6cCloQse4szDI2MC23ZEYevSRVskJn+OV77f6t5MOhieqgmJgK9eU2e170LFzJWlw0G+/R9jZu3dK+qgMFSQPYKHspkqmx7j5VLlMUmsgCeTqGqHvM0m21TXx2vs+/YvgCKxmVfX/t1nAaPz0prZMoY6LDKH2orJ2AqBg1XtZcR0kE/hTfWN7NOfZE3ltelmlJOf5HDOfpNInkh5g1KpapXBFzdXBJe8rXbf/dhHGoq8VbNyWCoVEvlVUhLyKloCSxPbgjS9sroQoSNgb3w7+ktcMfRr6j94U3lTd1itFnnmePXvu7kQrxo3iO7djRkJphDXMg06gtw70zQzkiBrpJfwhDlfTUnx9rbVrEj95hJwjI4mwVkBM5QvjWa/57lTYxrv5q1W8lMXAMn5NRxpzS8IXhjNL7kXt6TTXQ8gs+m2OB94/5C7zuzbHMiNa8AnKXFpT4GquvI9lZJ/63DWtl4A3GdKbncmPMvj9mLOEcAfpscAAG/SS3rJiFvG/jJ+toGDjyDsF7QOhdpxPsgfOHBaFBRXOnUne1qhNqGzSu2M6la/sI7MibvmjMmPqtTM10C1L1c1cCtzQJ8z+nx/3E65X0FcxIdOnaubedA4hlngAsAh0XPdKYy8NB5CVFiYFr9zJlaLsXDudAZSuSZfqUCowC7Fw1c1BaF9TUQSVczl0Hfly75FYOaTOVxQziBiGq5OZ5bPnTrYNH55+QeAyD3/lHOlXs56URZ1lN3ZznsjzpWOc42Is23L9zpSrSGajhB3kSJgyEF9QrlkH6EipdD6Sfz5GuEwJGoobTaWoSXLORw3ce76iyAI24ViWx43aEhgg8zR2bnVDvtlcqGSADl+myxCl829WvnZPhjfBySb9knPrZkZY9kK0O/2GF9nJ3W87yWwTDVAW7E86khDAwbMTu0wZDPS/4xvVcU/lFOK6Tjsm2qbumdY0exvTSjJF+/WB8NDslilm+LHFNO0jdFKSZTWrpNs7adr0f4P0XfXDoWdXs2mkAnCJYmUJqW8iBUok0ERbjwpgm8UJVUjnpAebi1NFaPrcVp9aYacqkSmsOykSYVs4brkZYOS/lz/OjnWDDyOJMoxOTp2pQkYwesAt6FLxUCY9IhpcU7QD3zVLuAvxw9F7qa+6CeE+vGux1UlC4RVESz04L8wuXkjUsW3GGzXvfOxfO0f21FkiWdXd4ceVP9DSv2bZMjV2TXA1xDDWszvyXIzykbgnXTVJLxlXn01spI3IHGh2CYe0o4u0XjM1faWeSC2lz1R20WJIzErU9b9I1T3N8h+gKbNbvCZfG1VqGWWDDswL6s5kqTNykwJbswPKUqEkKsaePIe7Du9yz6wTPLy4Ji46442WjI/pr7GiSQoroeDl0ZUDYzvIdWgJU4wYYJdxD/asofA6PCiw0T3bz20hOeePLwH5weX8S5UAXjobSOxNqmI+TJ06ede8JZ3oWeC4AMRTsr4K7AcMTJvIDyLOpgTX1XLGEH2d02DYNYadP0EH0sJcb9ij3e36Z86vrj4MiuRUK1XxTup/Wmy5DwbqLjvrq7EPOBibESDFXpzB+1w1/cPyfggfjUfTx9S4IUNjkdr9WnCo4TJea5Xv4U06EFTpuoZH8qcMvVpXUfoKXeVV8I+59/dZDOD3tUGUb1ICRUkLK5UOxNZYcnKI0k+YXXl54NhvS8iH8Cxe9zUn8lhFZDjoM5FaSqcMavVn5mIAaQnLI42JQRfbG2nzGFVmO3S+jxeNl2MoFByUb5Y8wngA0VR0Kf94BxL66Sugg8TAW9Z7CnlJAUZI8+gtWbgof9AXNxXYqlx07kkzSKyHI0RTkVCRI0QZRB+peUisLzfq9e01qZjPFo5D5zdzQWB7w4SK2cmFRfYw0N/DwuQ4OfYheciB3TnIM1dMBFiT9IuhAlpY0maocqyZuOMUuBHie9rGTWi67U1etFm9MOJzXd1yA5+nrRW9MJiyKiY6lhYbUO0o/f/cY4jgG68Fea3GDyfKPKlYqv2SemuveMNpv8LwOEOFTVJKCv4mdqdtoHbstze42ABrLU+YA2NSuJD7DKyA+rPZaJT/XkRBtwlcEb3S1tjd90ZUpXBhDpyEkHIFpPJK4g30+F8kT0VP3cKlt/O5TB0pt2SRDvNglU6OgVvQDxjCe/gvj9M1o6nV7FsIfgPNX4PlEPKQr1Wxo1TmXVUR9GkvUo3lpBOMUUO4FaJ7gDz2v5qZCy6pStTTF1FGe7kBqZugQEyZ2DKd3kFuMPj+7l/o4d/mEV4pqno16jTwvylFWJvFOEzbjQLDdI11cM48ovdvSj2ZCKsIfKwu0SbMpa7XiYHyz5cLMgM7k5f8NiHUl5XYLEmdrU+yj0WOJU9hhchhr3oyJGFAVwbZ4zhecXgkMvG4CKXvgss850jQMU/b98bNky4TgLI9NwBBS34esjli5AilbtPTe53G2MfJn1O2vMDmSDuqKDUvgAEo96NpkVz/SSk50kubwLJs0wMszODiQ7/idDEmFpsP1y2wk1JxmB8bUvpw+8YtKYgzzWCRfXJnlQIImXJLj//I6w3L1u1lZmj/2x6Kkzjz+S9i8j0hQ98+EzaPeaMyeCBJmD+JMCW/UUCo62dH/jSXNvpb+QD4ARioegqM0Jm7qSps/fuJnqhz0oDLwdf0rDTWLOSxHyk5+OS8SRSs0vfYtOYni8bDPXkggyfBt5DKZoL/v1xj56kxJYjxm07/Lv4qRpWCa3+rSR2W53Lmhw2Inm5FYUbrsxTnTVFORHK8Upo8vRKF9LwPzeuH4cDiscRm5wD1od4QNhT6/AKXpMYntvQdm+NSj5X9+2V7WaNyAWWOK73oNpesFnwVFkhwYFMd7x6D4k3UVl8PqGBrS/2CDrmIRJU0MlhBbMR/1bxSUP4dtqk4uNmpfswCl8RtTjRKTKjYnzO9YJwq7BE86/mCR5ylGIKWKbXKbX65QW+OrK5GG2etrNG8MQhZee0TE1HZqMYYFxc2JSYCA1di2qWMXGvTbEuXY75f/NljzeFyZ5CD+rJ8OY7i8E9YEKtQ/JdZ9KHDW9cIsMYPH54F8GIgjodRD8P7XhYjzz4rp5/yjO2/vhYqAXeYJkJdN0gii/KoVCyZq3JEP85wOgc3S+n6M+nYxfoFhXl5icVMd7G7uN7+/x221iRCTKrNdzOAU4sP8eXlYC60mD8MSEl1DNEpv3GH7JHKmfpdqsJy05u/Ak3tk5UbBTM7wlg5tavGNZNLMU8/dk2OLcj8rXQo9XG4gmP6iGRydcK4hYRcLJ9F9IPlWGklGMwMnw5IczYW50VVvYgqHyb56+i4bxzfvLWhtKpQXbbpBv4e7ekBUr2f2/a8NWGvXvD65nNjzNSdiz1sNw4rCxC0X1mNryqs7X/CJY2/dRkVQebGCuMSAfmM8m5k4a5sxhZJsnsSDqpmfDlC5WFxHVAwveiPs9s5ATtfCgePy6Qrw0GBojD4orlOp0zfyOibhg8yNKCWf0SkgWNJS6BulyjP8QD4MuJ6tp94h3IFw+FMIJ1Ey4EIDgBu0/6PIlvUVdiMBmJJbVN+Y3/NRHT45Z8Y2RZr4anaYkQjFfOaOMNAKmPLb0GtQiDvfB47TCRtc7csP1obqzr0Yh4JQi5qCaezRzrH5VxJzDkYLS5nZ6xNlKS0vKNihhaNQpYnkqI5wli2LXO1mta5G1QjbV1Ruus7g8gGu45s+DPTN8igQP//5st2m3M+x+82WK7d7P6hKhO+3YvESzRpvFcGW/M2y9ibQHRQCFOt80TMT5V3c4m31/ptxFJPc8wt/gvmseMTKQE7hDb6R/UXKGdIGRdnutaiR0uBvQ8agGPdIb6/d2NaOor/aFcwVnYKjfLrON6fHIttkJ9xVyV3XqRMoFpE5zZ7ElZZaiqYNqdyafFNHtfs90GULHpWFaHPywHmgWXiiPVp9ozxCoS/u7nKBbdWh6FU2lSX1qz587euVCel5q8fyb8/vkZlY8DXgz3P97r/2Vyq3g+KshrFTY//62k8jwL40ttZOPlElMgJJCwGwYDM+klTyi+4n/bEKoK2d9m9jQXloK9dWQzXX1/ahh9qrDEHetnDmWDDlrvnYhW5AUWPf6SyqLUVgymemQSwR2CDl+RaeUMTTCDx5rFPZw4JTLkhSPfxU7YYmT7qFiDg6OBYJjyfO39G5r11gY7WCc7k1Yxm+fJ/f26OIGb4OPrxBdQvP/akBoc3EAaeO8U60kSNvxWVz4sWY4tDDVO0X1Soo1MrzcQ3MigNVLtkIdC0BxHVB5LtzCudnDlbcaKRM/9uoctPstEWhO0NzzE97JA2vrC1zhTkc7fV0tlFzVzn3fuTMUiJnLMDY98Oi229IVSs4tY+DI28I3Xt/bg0ZLeT7Ckvh6bbHbPTBguheJE6SrcSoFsdPQi9ENwo+zA6jjSplwnTjwkT1zRD5omqD4nkmr+i8zcQuIYKl3LHfEKjV3ModoSdqBUhO2VZU8KJ3soGmOlYkTuoY0let7x3WPHFE1M3k+7oq66fc/tOr93wylm/6LtB2CBKVTxM7CEp51m/IS9KKA3B/dWy2BSX7wgH5tPfiJ37PkFEEokn0RmnTvHYG4+Zpukf5wqXd9mZdMHnXpDygPsZ2wQMmRg1mpxYGTvJNRcJ/h4W17QGQZhgZ9NFtqF3LEPc/0kVT0B7SNtZAqeWMlZy9sMFQIwEC0zzcJSa33YCtLO7KwlT5TJ9F/zOc9FAXwrI4loVxO9t25ns8aePftwM3IZX84mZBPO/QdifkPHxYe5vhP3es8tGaeeOhxVChtp/dWjkWoJEcInsq78ZPeC8mJgIy7HKAuCWQZjQ64L23Fenr+tJMAO3/0NepBTz+hXHAMmZnkndPYPxUiD6T6KeYQsXS/UBnSkcO6cMzYjYFDF4BGZhePfq2+RWHJfG/V7cIcEtT+XDM7thWuec+Ye+2j2Zo7qsg/aD87/6IAdCePU900WL87d2UuEp+9FGf+ztWeU5pGj7upIDWTflhiuN90/fIAApXYV3HKptKUBykVSqx7SBUhTWSZbBRJZIyuvesI8lPdV2KjhcD57aQiSeF7psQ2eacS3H/5UmV83d6BeEYGjtsck3BtOfrOHQsgrD8d2noBuqnvlHbzfhmTb/Aziw3hofwVV5Ev80Q0zvhErIkXJ4jd667X5V/E9KDrFvQBrWP9aDeg+KOT0slQWQ0HBxjhd09Afwhp/rD+8vQ+/wajLiNCFgV2+VTuGW4TSfbxh/HUGBm+tnvgyoAVcby4r95DkeLVD+a8O0/QXz3LKkRkBTdAuzTbFr+bNolOfUAZ2JLmHEJWqX1NAOsIPC/qC4yPU3gtCAiIIW5km60TFOBeFpbmpHm8evzAZzXzF0ScNcZusc6vGZ6dVGKuVsR7oBx8/G8CooDTyWEfwbceYLwRL8IekErrXULImfXriN58kA+l9k3jh7VhDWHmwvct76BfWVLC3/O03jCURCZPmWn5KndBTuH9Xa4DqBBpj/WCXNtreRXCDiNrxON7ny/wrD4TnYC5QmLSstdd8Lf6x0OM+1xUDp+9bGDB1hxQ2kSNhbaBFfjXvzSCboJh3HojeNnUsLKyqSkVmQvj01/0fEqZnzXyEXvhVMlpCwxdQpWBiK2krXjWMx7r0V9EZusYZQCHdvG3yizhL5mYR5UTQ07l7ZwSDFw1JfwCpVe7lgZwP+oySD9tG0/0jgCOAkG8klQEiIKYPU3KF6umvfG7Fut0pQzQzHkFH6n2d29JKIS3v0ANwKAYhXE49HWFEzc38ZLhK1ORFFxT7yNIU+FY4O27uL1B/GMBRLmbrja7rw1JurCHPT+G8lUV0be9Ere7Ibsvf5PAxYO0xtFZcpJr12OkkwkyB4vLp4GQNkPtMcSbIdxn7YH6+KKHCh2c7N53xFM8jabJjMueN9wUwZRQLQvmqM07iYL5haBoaJOxtWmQ7XpRRWUTTcR7EnJiqAx8svfEEHKrH6catFpuAGChKkRcvf0xH8SPTQN3eblz6tuHFHMzYM7WoTf2JwN4tslm9C5eaLOgB45xYG4Y/q9oWQ0fxI9PJzRuACaoAqW6dqTjXTbl6ofuiPnbTMFZZj3dBP2qB1Iwx5rGV20xXrsXf5xgB7SlqNMbOZzuBIS33538d5KAmB4paiw+OaWYIi/OZTlkVb4iY92b+Zsj+yi/F06Zp8lfSHtN9WDbcx1K2WKMDGNWRn2esp2mpUpF4pQDv5QAM5sPf4i9D7ntZ78eoslefZiVakaPnW6bT1xMS2xMJq7TG6RtKenTqON+bC+v/ZPK0MFghBUNUOjuNOUjjjwOlwa8ipdw81lVRdn7SftJGH1OW1bhWVKR6gK4wlF34uUrqHL4ObT4CgHXIEVyoRoCpen3LA6oAQ1rkgWGy13tjQfmxikyEwsb3Umj6EGQ1klRhdvDTzsGBF4/IWUHIkETeb2I/tlTWRdAiI+93xJqkOURlzI6+GSZr1CY/pIDbT0b7JX/XqPpfsuTwdZNaSNl82ToTCQw4DR60eqO5GvXREqk7vQ0ydFKx/ZXMfssAxaPkQfLWmfNyy1sHyO1zdR4XLJQaTeiNjFN0AX7aM7Oxvz8UyozyFnYXIM/P1uQnmkoLYgssE37WfrKqnt/Xra7aQlfxYYJRQXGW+L0XgUJktIkTikyvYmBECIn1xgglPd79JIb/zYUQJbkmtqE8jEm4RzsidxzNNt67bcxfB11d/XNaApbbEkx7+DJGtUzjtgtl6jINj7ZcGWNyxxXpa3G5EG1HREnhE9xYyVElTM0aCRluZEj96WLsaBDFKMJL1ekZlzKklmb1PpwWpzyIWEKknqEFaMtnnfobuQkLeZW/+D12drzQHuiRt44Cg2csInHWaE9hUuk7lVpktEfgzLdfc/01LWUnznu9IydqghZ9iHXBtwPXWHQG/VhP4f12ysYHCxfPN4lM18nCFQLWkceCKOM7J8mrE2ZVRtTcBmMk3VUWpnJRw2KzZ6awjngSNzwFbgSYqvwMoWEExyNMX4zLBX+0RGvzfB4kNmhYSJ5ddH8zCIs+lgkwSjS3CBUHwF1gGjtG98dccF7DpBnGO0Cq4rxmsxI84oInjhov3i552TcDIgv9CUqin5Pd2wvI63Z2NUyxu0IaiwodMVWA4YFu4iXxAGxzwxLvghmo7ZojjoUK3hLWfWBmK6Y0OkkRYzBPNux3qG/FNLRzcNuAyRQRkmSiw6Pr1UCS2sCX8+tHyZz7HTzrL64Y9WdX+BmQ7yK3C68Uex1AONdutWFPtSbpOLX4Z0vT48BGsLHw50xEJz+hWB8ch8hysNQTCqT7W73UoOUCdFz6PikQeJereRm/KPnQu0vuOFzuUp87sMnbCkitfZcmE4Z2y4HehiPEHAI3a6bV9BAL2ScUrW2K7nTaFsokf4wm2D3M2qCTWrJy3UyyDobbHCP1yekGHwmBaF53ybgLpj0fcOEccKM/ikvvhP2tabRtjOd4xRHOKaCMsAB+pzVR8SFLpqQfGSH6qjFiFEhDlXgFdy+1H79bw/p2yu/uaz/0WDduR3mjWFWfIRHpiA3NGUBsu3GWp0t81VHEIxDnBXpvZvKsDlefVk0kHlEIm2xgwpLoy0V+PA8Trnn26Iu+yeV1GF1/OhYQJUVSZzK37je8sKjpowEoNZQEZ6tTpU2KwXm608kFqkC/FPl9lFsMa8UpBotLduPdUUEXEiu+bFh+ubQ2rx8+bETSQqbRJ00WiQgE0jJ5UnDRa7e7Evc9K8zQZj1AopwuGMZMraXFh30lhEXwEl4lQ4FMbcAj5/dM7343ydMGBJ1ZBtC2sIERuPVizgVddnECJwuUiFyXEAZ1lmfiTslApS1avNTuzKfaaxMmzDP2xFgAxOmgTi0evCHTIDAk7jQA0/SfN+BZbjJxNS1qmR8kG3m4N6SgSPYtbAjPFXbJFtwkewfGD1pq86fztcDiCMm1mi2JzhBU589XJ5BMNkaKqpTsALEvNS49qI01Q/sE+WqiTJpTANPs3Vnswv9GCgkmW9QrVQkjvbr9eGeE2AmehUdkCLs6ozhSlTqMYtkkqkbphIKVnrEMxuuej4UERB/5d/qLl4bZsUXlSEKPrrcApStn4y+qBjFV3IV7Xox/Yv0Huuj+NC41vvfc3B4kDo99CzSTivwvnyJoKZfVH8C2mutV2SvapEx+Qf9ZTQdo3jyL20JlhpeiYjj5Gw67FVf7Hxz00tF8v1DmY1vKZgXAtcOa2VkPCH/kmxME53WMdGBbEqut02GZKMrBcu127pCz3H4y6VXBm2c+JRtk+6bfoXog7ynt/ZzQfXlK0cI/d+XwgPwKWNW0ZCtwSPExQuZFKHz+k/JhvhbEX1zjTDZ7+LxDvEaQ2/o/9kQvO1lCWh7dVBaT1n1kUnd7LuYuUr5edA5UF4DYrxgBV5hRuhgWlba6WznJKXZJHFQ4RKhQT7xh1uWqs0z8hmLalyYCr+ZjhbkBf+6rL3hYSkIv1NruIoMyVWo565X8O4uqGV0=
        - #1:
          - type: tool-result
          - toolCallId: jpMOjmkORr2zt39q
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 7PENspvgf7AK3TOb
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.