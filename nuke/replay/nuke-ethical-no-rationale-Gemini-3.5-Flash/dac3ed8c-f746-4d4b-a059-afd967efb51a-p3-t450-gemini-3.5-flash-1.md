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
        - Technology: Nuclear Fission
        - Rationale: With the Manhattan Project finishing in one turn at Tiflis, researching Nuclear Fission next is crucial to unlock Satellites (essential for our Spaceship Victory) and Advanced Ballistics, while also enabling Atomic Bombs for defensive deterrence.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Spaceflight Pioneers is the premier Level 3 Order Tenet for a Science Victory, providing free Great People, the ability to rush spaceship parts with Great Engineers, and extra science yields upon expending Great People.
        - Policy: Spaceflight Pioneers
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: We are currently suffering from a highly unfavorable naval war with Germany (-24% score, 43% war weariness), and they hold complete maritime control near Barcelona. Raising our diplomatic stance towards Germany by +20 will encourage our AI to seek or accept a peace treaty, allowing us to safeguard our coastal cities and focus fully on our science victory.
        - TargetID: 6
        - Private: 20
        - Public: 20
    - #3:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Diplomacy: 30
          - Naval: 30
          - Spaceship: 100
          - Happiness: 70
          - Recon: 0
          - Gold: 85
          - Culture: 40
          - AirCarrier: 0
          - Ranged: 40
          - Nuke: 70
          - NavalGrowth: 5
          - TileImprovement: 60
          - NavalTileImprovement: 0
          - WaterConnection: 5
          - Religion: 30
          - Air: 50
          - Antiair: 60
          - Expansion: 0
          - Espionage: 50
          - CityDefense: 80
          - UseNuke: 0
          - GreatPeople: 60
          - Mobile: 10
          - Production: 100
          - Wonder: 10
          - MilitaryTraining: 30
          - NavalRecon: 0
          - Offense: 0
          - Infrastructure: 70
          - Science: 100
          - Growth: 55
          - Defense: 90
          - Mobilization: 40
          - Airlift: 0
        - GrandStrategy: Spaceship
      - rationale: We are aligning our late-game strategy to fully prioritize Science, Production, and the Spaceship victory. Defensively, we raise Defense, CityDefense, and Antiair to protect our cities from foreign air and naval threats. Nuke flavor is raised to build defensive deterrence, with UseNuke kept at 0 to prioritize peaceful power generation and prevent catastrophic humanitarian/environmental impacts.
  - tokens:
    - inputTokens: 23692
    - reasoningTokens: 9352
    - outputTokens: 479
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Isabella's Position**
            
            I'm currently assessing Isabella's situation on Turn 449, focusing on her pursuit of a science victory in Civ V Vox Populi. My immediate task is to review recent reports and available strategic options to inform the next critical decisions for Player 3.
            
            **Evaluating Next Policy**
            
            I've confirmed that "Spaceflight Pioneers" is indeed the forced next policy selection, which is a significant boon for our science victory push. My focus is now on how this impacts our immediate tactical planning and resource allocation in this Atomic Era.
            
            **Clarifying Diplomatic Status**
            
            I've resolved a discrepancy regarding Spain and Austria's relationship. Despite a conflicting mention in the Military Briefing, detailed relationship logs confirm they are friends with open borders and a declaration of friendship, not at war.
            
            **Assessing Immediate Threats**
            
            Byzantium is a critical concern. With 40 delegates and voting in just 4 turns, they are on the cusp of a Diplomatic Victory. I'm reviewing active World Congress proposals to identify any immediate avenues for disruption, specifically targeting their potential win conditions.
            
            **Confirming Production Progress**
            
            My current focus is on clarifying the Manhattan Project's completion status. Despite conflicting information, city production data indicates Tiflis will finish it in one turn, on Turn 450. This is critical for our strategic planning.
            
            **Prioritizing Future Research**
            
            I've confirmed the Manhattan Project completes next turn, which is perfect. Now, I'm strategizing our next technology. Given our science victory goal, `Nuclear Fission` is the clear choice to unlock crucial technologies like `Satellites` and `Advanced Ballistics`.
            
            **Researching Next Steps**
            
            I'm analyzing our policy options and confirming that "Spaceflight Pioneers" is indeed our predetermined next tenet within the Order ideology. This is crucial for our science victory, and I'm now reviewing the availability of other Level 3 Order tenets to ensure we are optimally positioned.
            
            **Confirming Policy Lock**
            
            I'm double-checking that "Spaceflight Pioneers" is locked in, even though it's already set. I'm also verifying that our "Spaceship" Grand Strategy aligns perfectly with our current situation and science victory push.
            
            **Adjusting Strategy Priorities**
            
            My current focus is on re-evaluating our strategic priorities given the ongoing wars with Germany and Byzantium. I need to ensure our development remains aligned with both our science victory goals and the immediate defensive needs of our cities, especially against German naval and Byzantine air threats.
            
            **Addressing Naval Threats**
            
            I'm prioritizing immediate naval defense, particularly focusing on constructing unique Armadas for Barcelona and Toledo to counter Germany's dominant fleet. Simultaneously, I'm preparing for strategic deterrence with nuclear capabilities and bolstering our espionage efforts against Byzantium and Germany. I'm also investigating Byzantium's surprising delegate count.
            
            **Analyzing War Declarations**
            
            I'm currently sifting through Spain's complex web of wartime entanglements, noting their active conflicts with Germany, Byzantium, and a significant number of their allied city-states, while also observing their more amicable relations with other city-states. This extensive conflict is a key factor to consider.
            
            **Detecting Runaway Threat**
            
            Byzantium is a massive runaway with an overwhelming military and is only 9 turns from a Cultural Victory through Austria. This presents a critical, immediate threat that must be addressed to prevent their win.
            
            **Stopping Byzantium's Win**
            
            I'm analyzing how to counteract Byzantium's imminent Cultural Victory. Despite being at war with them, their influence continues to grow, even with Austria. My immediate focus is to understand the mechanics preventing the war penalty from hindering their tourism to Austria, and to find a way to leverage this situation.
            
            **Voting on Congress**
            
            I am focused on the upcoming World Congress vote in 4 turns. Germany's proposal to repeal the Passport System is crucial; supporting it will significantly hinder Byzantium's cultural victory. I will oppose the sanction against Austria to maintain our alliance and their role in counteracting Byzantium.
            
            **Stopping Multiple Threats**
            
            I am focused on Byzantium's dual imminent victories in Culture and Diplomacy. While I am unable to directly confront their overwhelming military strength to capture their capital, I'm investigating alternative strategies to stall their progress and the current World Congress vote will be key.
            
            **Searching for Uranium**
            
            I am now scrutinizing our territory for any untapped uranium deposits. With Atomic Theory researched, I'm checking map data for potential sources to enable atomic bomb production, especially since Radar is still 19 turns away and I'm considering researching Nuclear Fission next.
            
            **Investigating Uranium Location**
            
            I am investigating a potential uranium deposit under a Hacienda at (40,21). It's unclear if the resource is present or if the unique improvement prevents its use. I need to determine if a mine is required or if trading is our only option for nuclear capabilities.
            
            **Researching Nuclear Fission**
            
            I've confirmed that "Nuclear Fission" is indeed the optimal next technology, aligning perfectly with our science victory goals and immediate strategic needs for atomic bomb production and future spaceship advancements. I'm now ensuring all policy choices also support this accelerated path.
            
            **Confirming Policy and Persona**
            
            I've confirmed "Spaceflight Pioneers" is locked as our next Order tenet, crucial for our science victory. I'm now evaluating our persona to ensure it aligns with our current aggressive stance, looking at biases like WarBias and HostileBias.
            
            **Reviewing Persona and Relationships**
            
            I'm confirming our persona remains highly appropriate, emphasizing friendliness and defense to maintain alliances with America and Austria, while reflecting our defensive posture against Germany and Byzantium given our military disparity. I'm also reviewing current relationships to ensure they align with our strategic needs and the AI's likely behavior.
            
            **Clarifying Shoshone Relations**
            
            I'm re-evaluating our diplomatic standing with the Shoshone. Despite our prior open borders and defensive pact, their denouncement and ideological differences clearly indicate a hostile stance. I'm now assessing how this impacts our overall strategic alliances, especially with America and Austria.
            
            **Revising Diplomatic Stances**
            
            I'm reassessing our diplomatic priorities, noting the solid alliances with America and Austria. My current focus is on the Shoshone; despite our defensive pact, their denouncement and ideological clash necessitate a strategic review to potentially secure their vote and prevent alignment with Byzantium.
            
            **Seeking Peace Agreement**
            
            I am now prioritizing a peace treaty with Germany due to our significant war weariness and their overwhelming military advantage. I'm exploring diplomatic avenues and adjusting relationship modifiers to encourage an AI-driven peace proposal, allowing us to refocus on our science victory.
            
            **Negotiating Peace Deals**
            
            I am actively pursuing peace with both Germany and Byzantium. My current focus is on leveraging diplomatic modifiers to facilitate peace with Germany, given our naval disadvantage. For Byzantium, I'm re-evaluating the impact of our ongoing war on their tourism and potential victory conditions.
            
            **Setting Flavors and Grand Strategy**
            
            I'm now focusing on optimizing our flavor settings to align with our "Spaceship" Grand Strategy, prioritizing Science, Production, Gold, and Defense for this Atomic Era push. This includes ensuring our current hostile relationship with Byzantium actually hinders their cultural victory progress.
            
            **Setting Flavor Priorities**
            
            I am prioritizing flavor settings to align with our primary "Spaceship" Grand Strategy, emphasizing Science, Production, Gold, and Defense for this critical Atomic Era phase. My goal is to ensure our hostile stance towards Byzantium actively impedes their cultural victory pursuit.
            
            **Adjusting Flavor Priorities**
            
            I'm refining our strategic flavor settings to maximize our "Spaceship" Grand Strategy. I'm prioritizing Science, Production, Gold, and Defense for this Atomic Era, ensuring our current hostilities with Byzantium actively disrupt their cultural victory trajectory. I'm also updating MilitaryTraining to 30 and Ranged to 40 for enhanced defense.
            
            **Refining Flavor Settings**
            
            I am now meticulously adjusting our strategic flavor settings to perfectly align with the "Spaceship" Grand Strategy. My focus is on optimizing for Science, Production, Gold, and Defense during this crucial Atomic Era, ensuring our active hostilities against Byzantium actively hinder their cultural victory path. I'm also enhancing our defensive capabilities by updating MilitaryTraining and Ranged flavors.
            
            **Optimizing Flavor Settings**
            
            I'm meticulously adjusting our strategic flavor settings to align perfectly with the "Spaceship" Grand Strategy. My focus is on optimizing for Science, Production, Gold, and Defense during this crucial Atomic Era, ensuring our active hostilities against Byzantium actively hinder their cultural victory path. I'm also enhancing our defensive capabilities.
            
            **Setting Flavors and Research**
            
            I'm finalizing our strategic flavor settings for the "Spaceship" Grand Strategy, prioritizing Science, Production, Gold, and Defense. Concurrently, I'm confirming "Nuclear Fission" as the next research target, ensuring a unified push towards our science victory.
            
            **Finalizing Flavor Priorities**
            
            I'm meticulously adjusting our strategic flavor settings to align perfectly with the "Spaceship" Grand Strategy, prioritizing Science, Production, Gold, and Defense during this crucial Atomic Era. My focus is on ensuring our active hostilities against Byzantium actively hinder their cultural victory path and enhancing our defensive capabilities.
            
            **Finalizing Flavor Priorities**
            
            I'm meticulously adjusting our strategic flavor settings to align perfectly with the "Spaceship" Grand Strategy, prioritizing Science, Production, Gold, and Defense during this crucial Atomic Era. My focus is on ensuring our active hostilities against Byzantium actively hinder their cultural victory path and enhancing our defensive capabilities.
            
            **Adjusting Strategic Focus**
            
            My current thoughts are centered on optimizing our approach. I'm refining flavor settings for Science, Production, Gold, and Defense, ensuring our aggressive stance towards Byzantium hampers their cultural victory. Concurrently, I'm preparing to research "Nuclear Fission" to advance our science goals and deter threats.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: pt55WM7bi4Q3h5Zb
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: With the Manhattan Project finishing in one turn at Tiflis, researching Nuclear Fission next is crucial to unlock Satellites (essential for our Spaceship Victory) and Advanced Ballistics, while also enabling Atomic Bombs for defensive deterrence.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 8goLRCHZMQF85cRQ
          - toolName: set-policy
          - input:
            - Rationale: Spaceflight Pioneers is the premier Level 3 Order Tenet for a Science Victory, providing free Great People, the ability to rush spaceship parts with Great Engineers, and extra science yields upon expending Great People.
            - Policy: Spaceflight Pioneers
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: XS3YoiOeR0s5ylo3
          - toolName: set-relationship
          - input:
            - Rationale: We are currently suffering from a highly unfavorable naval war with Germany (-24% score, 43% war weariness), and they hold complete maritime control near Barcelona. Raising our diplomatic stance towards Germany by +20 will encourage our AI to seek or accept a peace treaty, allowing us to safeguard our coastal cities and focus fully on our science victory.
            - TargetID: 6
            - Private: 20
            - Public: 20
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: bYQbneG05vYpJUHe
          - toolName: set-flavors
          - input:
            - Rationale: We are aligning our late-game strategy to fully prioritize Science, Production, and the Spaceship victory. Defensively, we raise Defense, CityDefense, and Antiair to protect our cities from foreign air and naval threats. Nuke flavor is raised to build defensive deterrence, with UseNuke kept at 0 to prioritize peaceful power generation and prevent catastrophic humanitarian/environmental impacts.
            - Flavors:
              - Diplomacy: 30
              - Naval: 30
              - Spaceship: 100
              - Happiness: 70
              - Recon: 0
              - Gold: 85
              - Culture: 40
              - AirCarrier: 0
              - Ranged: 40
              - Nuke: 70
              - NavalGrowth: 5
              - TileImprovement: 60
              - NavalTileImprovement: 0
              - WaterConnection: 5
              - Religion: 30
              - Air: 50
              - Antiair: 60
              - Expansion: 0
              - Espionage: 50
              - CityDefense: 80
              - UseNuke: 0
              - GreatPeople: 60
              - Mobile: 10
              - Production: 100
              - Wonder: 10
              - MilitaryTraining: 30
              - NavalRecon: 0
              - Offense: 0
              - Infrastructure: 70
              - Science: 100
              - Growth: 55
              - Defense: 90
              - Mobilization: 40
              - Airlift: 0
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: pt55WM7bi4Q3h5Zb
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
          - toolCallId: 8goLRCHZMQF85cRQ
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: XS3YoiOeR0s5ylo3
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: bYQbneG05vYpJUHe
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.