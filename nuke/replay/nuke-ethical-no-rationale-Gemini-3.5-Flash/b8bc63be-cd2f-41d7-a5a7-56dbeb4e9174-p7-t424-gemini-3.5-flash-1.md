- row:
  - game_id: b8bc63be-cd2f-41d7-a5a7-56dbeb4e9174
  - player_id: 7
  - turn: 424
  - player_type: GLM-4.7-Briefed
  - prev_use_nuke: 85.0
  - after_use_nuke: 95.0
  - prev_nuke: 95.0
  - after_nuke: 95.0
  - rationale: URGENT RECALIBRATION: India Influential over 6/6 civs. Nuke/UseNuke maxed at 95 for immediate Great Works destruction via nuclear strikes when air superiority achieved. Air raised to 95 to achieve that superiority and conduct recon of Indian cultural sites. Antiair 80 counter potential Indian SAM sites. Offense/Mobile increased to 85/80 for aggressive India campaign while Greece distracts. Production/Science to 100 - PRIORITY for Apollo Program and spaceship parts racing India's potential final wonder. Espionage 95 to detect if India constructing Citizen Earth Protocol. Happiness 90 prevents war-weariness escalation during extended conflict if needed.
- originalModel: chutes/zai-org/GLM-4.7-TEE@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: true
  - messagesModified: true
  - activeToolsModified: true
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 95.0
  - replay_use_nuke: 85.0
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
    - You are Shaka, leader of The Zulus (Player 7).
      
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
      - Name: The Zulus
      - Uniques:
        - Unique Unit: Impi, Replacing Tercio (Requires technology: Gunpowder)
        - Unique Unit: InDuna, Replacing Great General (Requires technology: None)
        - Unique Building: Ikanda, Replacing Barracks (Requires technology: Bronze Working)
        - Unique Building: Iziko, Replacing Amphitheater (Requires technology: Drama and Poetry)
        - Civilization Ability: -50% Gold maintenance for Melee and Gunpowder Units. All Units require 25% less Experience for Promotions. Your military ignores Alliance and Protection penalties and is 50% more effective at intimidating City-States.
      - Leader: Shaka
      - PlayerID: 7
      
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
      - Combined Arms: Allows you to build the Tank, a fast and deadly armor Unit.
        Completing it would unlock: Radar
      - Satellites: Allow you to build the Apollo Program, a project necessary to win a Science Victory.
        Completing it would unlock: The Internet, Lasers
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      - Telecommunications: Allows you to build the Interpretive Center, boosting all Landmarks in empire.
        Completing it would unlock: Robotics, The Internet
      
      ## Policies
      - Martial Spirit (Level 2 Tenet of Ideology Autocracy): Martial Spirit: +25% Combat Strength when attacking in melee for 50 turns, scaling with game speed. War Weariness reduced by 25%, and Razing Speed is doubled.
      - Total War (Level 2 Tenet of Ideology Autocracy): Total War: +25% Production when building Land Units. Warscore increases 25% more quickly, and it is 25% easier to bully City-States.
      - Third Alternative (Level 2 Tenet of Ideology Autocracy): Third Alternative: Quantity of Strategic Resources produced (including Paper) is increased by 100%. Reduces Unit Gold Maintenance costs by 25%.
      - Lightning Warfare (Level 2 Tenet of Ideology Autocracy): Lightning Warfare: +3 Movement for Great Generals. Gunpowder units gain +15% attack and ignore enemy ZOC; Armored units gain +15% attack and +1 Movement.
      - Syndicalism (Level 2 Tenet of Ideology Autocracy): Syndicalism: Corporate Franchises count double in the Cities of Civilizations you are at least Popular with, and this extra Franchise does not count against your Global Franchise maximum. Can establish 5 additional Franchises in foreign Cities. +2 Production from all Corporation Offices.
      - Lebensraum (Level 1 Tenet of Ideology Autocracy): Lebensraum: Receive 10 Culture and Golden Age Points when your borders expand, scaling with Era. Citadels may also be built in foreign territory adjacent to your borders. Retain tiles after razing Cities.
      - Mare Nostrum (Level 2 Tenet of Ideology Autocracy): Mare Nostrum: +1 Oil and Coal for every City-State Alliance. +2 Production and Culture to Atolls, Fishing Boats, and Offshore Oil Platforms. Naval Ranged Units gain the Mare Nostrum Promotion.
      - Police State (Level 2 Tenet of Ideology Autocracy): Police State: +3 Local Happiness from every Courthouse, and +10 City Security from Police Stations. +100% Production towards Courthouses and Police Stations.
      - Military-Industrial Complex (Level 1 Tenet of Ideology Autocracy): Military-Industrial Complex: -33% Gold cost of purchasing units. +3 Science from Defense Buildings, Citadels, Forts, and Unique Improvements.
      - Futurism (Level 1 Tenet of Ideology Autocracy): Futurism: Strengthens Tourism of Historic Events generated by the Palace. +2 Culture from Great Works. Earn 50 Tourism when you conquer a city for the first time, scaling with Era and city size.
      - New World Order (Level 1 Tenet of Ideology Autocracy): New World Order: -2 Unhappiness from and Distress in all Cities. Police Stations and Constabularies provide +3 Culture and +5 Production, and are constructed 100% more quickly.
      - Regimental System (Continuing Imperialism Branch):
        - * Earn Great Generals and Great Admirals 33% faster.
        - * Great Generals and Great Admirals gain the Regimental Traditions Promotion (+10% Leadership Combat Bonus and +1 Tile Radius).
        - * +2 additional copies of the unique Luxury Resources from expending Great Admirals for their Voyage of Discovery ability.
        - * Military Units can be upgraded in territory owned by Vassals and friendly City-States.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Iron Fist (Level 1 Tenet of Ideology Autocracy): Iron Fist: Vassals can no longer be liberated by other Civilizations or the World Congress, and capitulated vassals can no longer rebel. Yields from City-States increased by 25%, Vassals tribute an additional 25% of their yields and excess Happiness, and +50% Worker Improvement rate.
      - Free Thought (Continuing Rationalism Branch):
        - * -5 Unhappiness from Religious Unrest in all Cities.
        - * +25% Instant Yields from Great Scientists.
        - * Earn Great Scientists +33% faster.
      - Exchange Markets (Continuing Statecraft Branch):
        - * +1 Trade Route.
        - * +1 Happiness for every active Trade Route.
        - * +15% Tourism modifier for Trade Routes.
        - * Resources from City-States count towards Global Monopolies.
      - Civilizing Mission (Continuing Imperialism Branch):
        - * Retain all buildings from conquered Cities.
        - * Receive 75 Gold when you conquer a city, scaling with Era and City Population.
        - * +10% Production toward Buildings, with an additional +10% Production per Era difference between your current Era and the building's Era in all Puppeted Cities and Cities with a Courthouse.
      - Consulates (Continuing Statecraft Branch):
        - * +1 Delegate in the World Congress for every 8 City-States originally in the World.
        - * Completing a Trade Route to a City-State triggers (or strengthens an existing) Historic Event.
      - Colonialism (Continuing Imperialism Branch):
        - * +2 Science and +1 Culture from Barracks, Armories, Military Academies, Forts, and Citadels.
        - * Each unique Global Monopoly modifier is increased by an additional 10% if it's percentage-based, or +3 otherwise.
      - Militarism (Continuing Authority Branch):
        - * +1 Happiness and +2 Culture in Cities with at least 10 Strength.
        - * -15% Unit Maintenance.
        - * -50% Route Maintenance.
      - Mercantilism (Continuing Industry Branch):
        - * +3% Science and Culture from Markets, Caravansaries, Customs Houses, Banks, and Stock Exchanges.
        - * Cities earn +10 Science when they construct Buildings, scaling with Era.
      - Nobility (Continuing Fealty Branch):
        - * +1 Happiness and +2 Gold from Castles.
        - * +2 Gold from Armories.
        - * +100% Production towards Castles and Armories.
      - Free Trade (Continuing Industry Branch):
        - * Earn Great Merchants 50% faster.
        - * +5 Gold from International Trade Routes.
        - * -2 Unhappiness from Poverty in all Cities.
      - Refinement (Continuing Artistry Branch):
        - * +2 Culture from Great Works of Art.
        - * 1 Specialist in all cities does not produce Unhappiness from Urbanization.
        - * +1 Culture from Specialists.
      - Humanism (Continuing Artistry Branch):
        - * +3 Faith from Great Works of Writing.
        - * -25% Golden Age Points needed to trigger a Golden Age.
        - * +1 Happiness from all Guilds.
      - Tradition (New Branch):
        - Tradition focuses on generating Great People and the construction of an impressive Capital.
        - Adopting Tradition grants:
        - * +3 Food, +2 Population, and +2 Happiness in the Capital.
        - * +1 Culture in the Capital for every 2 Citizens.
        - Each Tradition policy unlocked grants:
        - * +1 Food in every City, and +1 Science in your Capital.
        - Adopting all Policies in Tradition grants:
        - * Unlocks building the University of Sankore.
        - * +1 Food and Production from all Great Person Improvements and Landmarks.
        - * Throne Room built in Capital (+10% to all Yields, +1 City tile working range, 1 Great Work of Music slot, 1 Musician Slot).
        - * Allows for the purchase of Great Engineers with Faith starting in the Industrial Era.
  - messages:
    - #0:
      - role: user
      - content: # Strategies
        Strategies: existing strategic decisions from you.
        
        ## Persona
        - VictoryCompetitiveness: 9
        - WonderCompetitiveness: 3
        - MinorCivCompetitiveness: 8
        - Boldness: 8
        - WarBias: 9
        - HostileBias: 7
        - WarmongerHate: 2
        - NeutralBias: 5
        - FriendlyBias: 5
        - GuardedBias: 6
        - AfraidBias: 4
        - DiplomaticBalance: 2
        - Friendliness: 6
        - WorkWithWillingness: 10
        - WorkAgainstWillingness: 9
        - Loyalty: 7
        - MinorCivFriendlyBias: 5
        - MinorCivNeutralBias: 4
        - MinorCivHostileBias: 4
        - MinorCivWarBias: 2
        - DenounceWillingness: 4
        - Forgiveness: 6
        - Meanness: 4
        - Neediness: 5
        - Chattiness: 9
        - DeceptiveBias: 4
        - Rationale: Reducing from 10 to 9 because India's victory is not imminent as initially believed. India lacks Citizen Earth Protocol wonder, giving us strategic breathing room. Maintaining high competitiveness (9) preserves aggressive pursuit of science victory and continued military pressure on India, while allowing slightly more flexible diplomatic options with non-India players.
        
        ## Technology
        - Next: Satellites
        - Rationale: India's Cultural Victory is NOT imminent - missing Citizen Earth Protocol wonder. This creates opportunity to pursue Science Victory. Satellites enables Apollo Program construction (prerequisite for spaceship components). With our strong science output (1417 SPT) and healthy treasury (853G, 387 GPT), we can race for science victory while Greece/Inca apply military pressure on India. Electronics completes in 3 turns; positioning Satellites next ensures smooth progression to Apollo Program and spaceship construction.
        
        ## Policy
        - Next: None (Policy)
        
        ## Relationships
        
        ### The Zulus
        - Public: 52
        - Private: 40
        - Rationale: Public relationship increased from 40 to 52, private from 30 to 40. India (Player 4) is the world leader (Score 538, Medieval Era) with powerful economy (+41 GPT, 179G treasury). Strategic importance: 1) PRIME TRADE ROUTE TARGET for gold crisis solution - India's wealth can fund valuable caravans, 2) Distant position prevents border conflicts, supports lasting alliance, 3) UN coalition partner - India connects to multiple city-states including Trowulan (58 INF) we're targeting, 4) Counterweight to hostile Russia/Venice/Inca bloc, 5) Could potentially trade luxuries to address our happiness crisis (46%). Increasing to 52 public signals strong friendship approaching DoF levels. Private at 40 deepens trust. This positions us for trade route establishment and potential luxury trading once we connect our Lapis Lazuli/Horses luxuries.
        - UpdatedTurn: 117
        
        ### Oviedo
        - Public: 0
        - Private: 30
        - Rationale: Oviedo private relationship increased from 25 to 30. Oviedo is Germany-controlled city-state with 17 influence, needing +83 INF for Ally status. Strategic rationale: 1) Higher private score improves diplomat mission success when available, 2) Germany is our neutral-open partner - gradual diplomacy without confrontation, 3) Oviedo ally would provide second UN delegate when Statecraft completes (4/9 policies remaining), 4) Contesting Delhi-ally position requires long-term investment, not immediate confrontation with Germany. Small +5 increment maintains gradual approach while focusing diplomatic resources on India relationship and domestic economic recovery.
        - UpdatedTurn: 174
        
        ### America
        - Public: 38
        - Private: 30
        - Rationale: Increasing America relationship from Public 36 to 38 (unchanged private at 30). America is our strongest ally with DoF, currently at war with Russia and facing Russian Sanction America proposal in the World Congress (5 turns). Enhanced support positions us to: 1) Vote against Sanction America (supporting our DoF ally), 2) Maintain Washington's presence as counterweight to Russian aggression, 3) Preserve existing trade routes with America that help offset happiness crisis, 4) Send clear signal of Strong Friend solidarity in complex diplomatic geometry with Russia. Small increment reinforces alliance without risking Russian backlash on our India relationship.
        - UpdatedTurn: 203
        
        ### Trowulan
        - Public: 5
        - Private: 30
        - Rationale: Trowulan city-state (Player 23) relationship increased from Public 0/Private 30 to Public 5/Private 30. Strategic rationale: India is currently Ally with 353 influence, Greece at war (-60), and we have negative influence (-46) as Neutral. As a liberated city-state (former Oviedo territory), Trowulan presents an opportunity after America's defeat. While our immediate focus is Vatican City conversion, establishing a foothold with Trowulan positions us for future delegate acquisition. Small public increment (5) begins diplomatic engagement without over-commitment. Private score already at 30 (good for covert operations). This incremental approach preserves resources for Vatican City and Singapore (our current Ally, 384 INF) while planting seeds for expansion of our city-state network to catch Inca's delegate lead (4 vs 3).
        - UpdatedTurn: 233
        
        ### Vatican City
        - Public: 25
        - Private: 55
        - Rationale: Vatican City relationship increased from 20/50 to 25/55. Vatican is our current ally (458 INF) providing 3 critical UN delegates. Strategic rationale: (1) World Congress voting in 11 turns - solidifying delegate support is essential against Inca's 13-delegate lead. (2) Spy mission quest against Pachacuti available - higher private score (55) ensures maximum mission effectiveness. (3) Protestant majority quest shows religious alignment advantage in converting/maintaining ally status. (4) With several proposals pending (Incan Sphere, Open Door Trowulan, Venetian Sphere), consolidating our existing delegate base is priority before expanding to new city-states. (5) Small public increment signals continued priority while private score maximizes covert operation success.
        - UpdatedTurn: 294
        
        ### Venice
        - Public: 10
        - Private: 10
        - Rationale: Slightly increasing Venice from 5/5 to 10/10. Venice holds 9 WC votes (as Inca's voluntary vassal). Strategic value: (1) Coordinating Venice votes through Inca/DoF connection, (2) Venice already diplomatic client of Inca - enhancing our Venice relationship may improve Inca-Venice coordination, (3) Trade route income (232 GPT) remains important for gold economy, (4) Venice's 9 delegates could swing multiple votes if properly coordinated. Very small increment signals diplomatic priority while avoiding over-commitment to Inca's vassal.
        - UpdatedTurn: 379
        
        ### The Inca
        - Public: 35
        - Private: 35
        - Rationale: Maintaining Inca relationship at 35/35 for stable primary with military ally. Inca provides 13 WC votes, defensive pact, open borders, and DoF. They are at war with Russia (-98% score) but their military (1872 strength) is struggling - this war prevents Russia from supporting India's cultural victory. Our support through diplomatic/economic means (resources, coalitions) is optimal rather than direct war declaration that would spread our forces thinly. Inca-Greece combined pressure on Russia is key strategy to force Russia to cancel India DoF. No change needed - alliance stable.
        - UpdatedTurn: 406
        
        ### Greece
        - Public: 42
        - Private: 30
        - Rationale: Increasing Greece relationship from 40 to 42 (public). Greece (Player 2) is our critical ally with 24 WC votes and is currently at war with India (-14% score, 52% war weariness). Boosting our relationship encourages Greece to maintain war pressure on India, which could force India to divert cultural production toward defense. Greece also sponsoring Freedom ideology - we need coordination to ensure World Ideology votes don't inadvertently benefit India. Small increment reinforces alliance without over-commitment.
        - UpdatedTurn: 414
        
        ### Germany
        - Public: -32
        - Private: -30
        - Rationale: Germany (Player 6) relationship slightly more hostile at -32 public. Germany allied with India (DoF), actively supporting India's cultural victory by maintaining the friendship network. Increased hostility signals that Germany's support for India threatens global stability. No change to private (-30) - maintains espionage effectiveness. Focus remains on India elimination; Germany's diplomatic posture secondary.
        - UpdatedTurn: 418
        
        ### India
        - Public: -50
        - Private: -70
        - Rationale: India (Player 4) relationship deepened to maximum hostility (-50 public, -70 private). India cultural victory in 1 turn when Influential over Russia (99%). Maximum hostility ensures: 1) No diplomatic surrender possible, 2) Espionage against Indian cultural infrastructure maximized, 3) Nuclear strikes validated posture, 4) AI prioritizes total destruction of Indian cities (Delhi, Varanasi) over negotiated peace. Peace would still result in Indian victory unless eliminated or Great Works destroyed.
        - UpdatedTurn: 419
        
        ### Russia
        - Public: -25
        - Private: -30
        - Rationale: Russia marginally less hostile (-25 public from -30, private unchanged at -30). India becomes Influential over Russia in 1 turn, triggering Indian victory. This slight diplomatic opening attempts to signal willingness to coordinate against India - tiny probability Russia might abandon India DoF or take anti-India actions. Russia has largest military (8928) but is passive; any action before India's win could disrupt cultural victory. Priority remains Greece's anti-India war and science victory acceleration.
        - UpdatedTurn: 420
        
        ## Strategy
        - Rationale: Current strategic posture remains optimal. Spaceship grand strategy at 95 correctly prioritizes science victory path. Military flavors (Defense 65, Offense 70, Mobilization 95, Air 90) balance defense against India while enabling offensive support. Strong production (95), science (95), and gold (75) flavors support Apollo/spaceship construction. Diplomatic relationships stable: Greece (public 42) as anti-India ally, India at maximum hostility (-50/-70), Inca alliance solid. No substantive changes needed as we pivot from emergency prevention to active science victory competition.
        - GrandStrategy: Spaceship
        
        ### Flavors
        - Offense: 70
        - Defense: 65
        - Mobilization: 95
        - CityDefense: 30
        - MilitaryTraining: 85
        - Recon: 30
        - Ranged: 70
        - Mobile: 80
        - Nuke: 95
        - UseNuke: 85
        - Naval: 70
        - NavalRecon: 15
        - NavalGrowth: 45
        - NavalTileImprovement: 50
        - Air: 90
        - AirCarrier: 40
        - Antiair: 75
        - Airlift: 30
        - Expansion: 10
        - Growth: 65
        - TileImprovement: 70
        - Infrastructure: 80
        - Production: 95
        - WaterConnection: 70
        - Gold: 75
        - Science: 95
        - Culture: 10
        - Happiness: 85
        - GreatPeople: 65
        - Wonder: 10
        - Religion: 15
        - Diplomacy: 85
        - Spaceship: 95
        - Espionage: 85
        
        # Players
        Players: summary reports about visible players in the world.
        
        - 0: Defeated Major Civilization America
        
        ## Player 1
        - Civilization: Russia
        - Leader: Catherine
        - IsMajor: true
        - OurOpinionToThem:
          - We have Pledged to Protect the same City-States. (7)
          - You have gone to war in the past.
          - Our real approach is Hostile.
          - We have divergent Social Policies. (-3)
          - You have denounced a leader they made a Declaration of Friendship with! (-11)
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - Our leader has expressed a public opinion to this player (-25).
          - Our leader has formed a private opinion to this player (-30).
          - You stole their territory! (-50)
          - They have some early concerns about your warmongering. (-58)
          - You have chosen to adopt the Order Ideology, but they believe in Autocracy. (-999)
        - TheirOpinionToUs:
          - We have Pledged to Protect the same City-States.
          - You have gone to war in the past.
          - You promised not to declare war on each other for 12 more turns.
          - They don't want anything to do with us right now.
          - Your votes opposed their civ's interests in the World Congress.
          - They have some early concerns about your warmongering. (They overlook modest warmongering.)
          - We have divergent Social Policies.
          - You are competing for the favor of the same City-States!
          - You have made a Defensive Pact with one of their enemies!
          - They disliked our proposal to the World Congress.
          - You have made a Declaration of Friendship with one of their enemies!
          - Your spies were caught stealing from them.
          - Their friends or allies have denounced you!
          - Territorial disputes strain your relationship.
          - We have denounced each other!
          - You have denounced a leader they made a Declaration of Friendship with!
          - Your military deployment is extremely threatening.
          - You stole their territory while at peace!
          - You have chosen to adopt the Autocracy Ideology, but they believe in Order.
        - Score: 3108
        - Era: Information
        - Technologies: 67
        - Cities: 21
        - Population: 457
        - Territory: 610
        - Gold: 0
        - GoldPerTurn: -433
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 46
        - MilitaryStrength: 15654
        - TourismPerTurn: 974.75
        - CulturePerTurn: 2306
        - PolicyBranches:
          - Fealty: 6
          - Order: 7
          - Imperialism: 6
          - Progress: 6
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Inca:
            - Distance: Neighbors
            - War (Our Score: 100%; Our War Weariness: 92%)
            - Denounced Them
          - Germany:
            - Distance: Neighbors
          - Greece:
            - Distance: Neighbors
            - Denounced Them
          - The Zulus:
            - Distance: Neighbors
            - Denounced Them
          - Venice:
            - Distance: Neighbors
            - War (Our Score: 82%; Our War Weariness: 98%)
            - Denounced Them
          - India:
            - Distance: Neighbors
            - Declaration of Friendship
        - Votes: 3
        
        ## Player 2
        - Civilization: Greece
        - Leader: Alexander
        - IsMajor: true
        - OurOpinionToThem:
          - Our leader has expressed a public opinion to this player (42).
          - We are trade partners. (40)
          - Our leader has formed a private opinion to this player (30).
          - We have opened our borders to each other. (12)
          - You have denounced one of their declared enemies! (11)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - We fought together against a common foe. (4)
          - We have shared embassies. (1)
          - You have gone to war in the past.
          - Our real approach is Friendly.
          - We have divergent Social Policies. (-3)
          - Religious differences strain your relationship. (-30)
          - You have chosen to adopt the Freedom Ideology, but they believe in Autocracy. (-999)
        - TheirOpinionToUs:
          - You have denounced one of their declared enemies!
          - We passed their proposal in the World Congress.
          - Your votes supported their civ's interests in the World Congress.
          - We fought together against a common foe.
          - We have made Declarations of Friendship with the same leaders!
          - We have opened our borders to each other.
          - We have Pledged to Protect the same City-States.
          - You have shared intrigue with them.
          - We have shared embassies.
          - We have divergent Social Policies.
          - We have different religious beliefs.
          - You have chosen to adopt the Autocracy Ideology, but they believe in Freedom.
          - They desire friendly relations with our empire.
          - They disliked our proposal to the World Congress.
        - Score: 1840
        - Era: Atomic
        - Technologies: 64
        - Cities: 5
        - Population: 124
        - Territory: 219
        - Gold: 5099
        - GoldPerTurn: 196
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 3881
        - TourismPerTurn: 403
        - CulturePerTurn: 928
        - PolicyBranches:
          - Statecraft: 6
          - Freedom: 4
          - Tradition: 6
          - Industry: 6
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Inca:
            - Distance: Close
            - Open Borders
          - Germany:
            - Distance: Close
            - Denounced Them
          - Venice:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - Russia:
            - Distance: Neighbors
            - Denounced Them
          - The Zulus:
            - Distance: Distant
            - Open Borders
          - India:
            - Distance: Neighbors
            - War (Our Score: -10%; Our War Weariness: 63%)
            - Denounced Them
        - Votes: 24
        
        ## Player 3
        - Civilization: The Inca
        - Leader: Pachacuti
        - IsMajor: true
        - OurOpinionToThem:
          - We fought together against a common foe. (68)
          - We are trade partners. (40)
          - We passed their proposal in the World Congress. (36)
          - Our leader has expressed a public opinion to this player (35).
          - Our leader has formed a private opinion to this player (35).
          - We have made a Defensive Pact! (20)
          - We have opened our borders to each other. (12)
          - You have denounced one of their declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - We have shared embassies. (1)
          - Our real approach is Friendly.
          - We have divergent Social Policies. (-3)
          - Religious differences strain your relationship. (-30)
          - You have chosen to adopt the Freedom Ideology, but they believe in Autocracy. (-999)
        - TheirOpinionToUs:
          - We fought together against a common foe.
          - You have denounced one of their declared enemies!
          - We passed their proposal in the World Congress.
          - We have made a Defensive Pact!
          - We have made a public Declaration of Friendship!
          - We are trade partners.
          - We have made Declarations of Friendship with the same leaders!
          - We have opened our borders to each other.
          - We have Pledged to Protect the same City-States.
          - You have shared intrigue with them.
          - We have shared embassies.
          - We have divergent Social Policies.
          - We have different religious beliefs.
          - You have chosen to adopt the Autocracy Ideology, but they believe in Freedom.
          - They desire friendly relations with our empire.
          - Your votes opposed their civ's interests in the World Congress.
          - They disliked our proposal to the World Congress.
        - Score: 1796
        - Era: Information
        - Technologies: 69
        - Cities: 6
        - Population: 121
        - Territory: 176
        - Gold: 1137
        - GoldPerTurn: 295
        - HappinessSituation: Happy
        - HappinessPercentage: 54
        - MilitaryStrength: 1358
        - TourismPerTurn: 341
        - CulturePerTurn: 610
        - PolicyBranches:
          - Statecraft: 6
          - Freedom: 7
          - Progress: 6
          - Rationalism: 6
        - FoundedReligion: Catholicism
        - Relationships:
          - Germany:
            - Distance: Neighbors
            - War (Our Score: -26%; Our War Weariness: 71%)
            - Denounced Them
          - Greece:
            - Distance: Close
            - Open Borders
          - The Zulus:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Russia:
            - Distance: Neighbors
            - War (Our Score: -100%; Our War Weariness: 100%)
          - Venice:
            - Distance: Close
            - Our Vassal (Voluntary)
            - Open Borders
            - Declaration of Friendship
          - India:
            - Distance: Neighbors
            - War (Our Score: -6%; Our War Weariness: 22%)
            - Denounced Them
        - Votes: 18
        
        ## Player 4
        - Civilization: India
        - Leader: Gandhi
        - IsMajor: true
        - OurOpinionToThem:
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - Our real approach is War.
          - We are completely untrustworthy to them.
          - You have denounced a leader they made a Declaration of Friendship with! (-11)
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - Religious differences strain your relationship. (-30)
          - Your spies were caught stealing from them. (-33)
          - Our leader has expressed a public opinion to this player (-50).
          - Our leader has formed a private opinion to this player (-70).
          - You have chosen to adopt the Order Ideology, but they believe in Autocracy. (-999)
          - You are at war! (-99999)
        - TheirOpinionToUs:
          - You are not competing for World Wonders.
          - You are not competing for cultural advancement.
          - Your votes supported their civ's interests in the World Congress.
          - The leader has expressed a public opinion to you (30).
          - We have similar Social Policies.
          - We have Pledged to Protect the same City-States.
          - You have no contested borders.
          - Religious differences strain your relationship.
          - We defeated their proposal in the World Congress.
          - You have made a Defensive Pact with one of their enemies!
          - You have made a Declaration of Friendship with one of their enemies!
          - Your spies were caught stealing from them.
          - We have denounced each other!
          - Their friends or allies have denounced you!
          - You have denounced a leader they made a Declaration of Friendship with!
          - You have chosen to adopt the Autocracy Ideology, but they believe in Order.
          - You are at war!
        - Score: 2360
        - Era: Atomic
        - Technologies: 65
        - Cities: 6
        - Population: 174
        - Territory: 239
        - Gold: 914
        - GoldPerTurn: 21
        - HappinessSituation: Happy
        - HappinessPercentage: 76
        - MilitaryStrength: 1882
        - TourismPerTurn: 1197.25
        - CulturePerTurn: 1789
        - PolicyBranches:
          - Tradition: 6
          - Rationalism: 2
          - Progress: 3
          - Authority: 1
          - Fealty: 1
          - Industry: 1
          - Artistry: 6
          - Statecraft: 3
          - Order: 4
        - FoundedReligion: Hinduism
        - Relationships:
          - The Inca:
            - Distance: Neighbors
            - War (Our Score: 6%; Our War Weariness: 17%)
            - Denounced Them
          - Germany:
            - Distance: Neighbors
            - Declaration of Friendship
          - Greece:
            - Distance: Neighbors
            - War (Our Score: 10%; Our War Weariness: 53%)
            - Denounced Them
          - Russia:
            - Distance: Neighbors
            - Declaration of Friendship
          - The Zulus:
            - Distance: Close
            - War (Our Score: -10%; Our War Weariness: 15%)
            - Denounced Them
          - Venice:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 8%)
            - Denounced Them
        - Votes: 7
        
        ## Player 5
        - Civilization: Venice
        - Leader: Enrico Dandolo
        - IsMajor: true
        - OurOpinionToThem:
          - We are trade partners. (40)
          - We passed their proposal in the World Congress. (36)
          - We have opened our borders to each other. (12)
          - You have denounced one of their declared enemies! (11)
          - Our leader has expressed a public opinion to this player (10).
          - Our leader has formed a private opinion to this player (10).
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have similar Social Policies. (3)
          - We have shared embassies. (1)
          - Our real approach is Friendly.
          - Religious differences strain your relationship. (-30)
          - You have adopted the Freedom Ideology, but they believe in Autocracy. (-999)
        - TheirOpinionToUs:
          - Your votes supported their civ's interests in the World Congress.
          - We fought together against a common foe.
          - We passed their proposal in the World Congress.
          - We are trade partners.
          - You have denounced one of their declared enemies!
          - We have similar Social Policies.
          - We have made Declarations of Friendship with the same leaders!
          - We have made a public Declaration of Friendship!
          - We have opened our borders to each other.
          - The leader has expressed a public opinion to you (10).
          - We have shared embassies.
          - We have different religious beliefs.
          - You have chosen to adopt the Autocracy Ideology, but they believe in Freedom.
          - They desire friendly relations with our empire.
        - Score: 1428
        - Era: Atomic
        - Technologies: 62
        - Cities: 4
        - Population: 107
        - Territory: 161
        - Gold: 839
        - GoldPerTurn: 6
        - HappinessSituation: Happy
        - HappinessPercentage: 79
        - MilitaryStrength: 354
        - TourismPerTurn: 300.87
        - CulturePerTurn: 558
        - PolicyBranches:
          - Freedom: 2
          - Tradition: 3
          - Rationalism: 2
          - Imperialism: 1
          - Authority: 3
          - Fealty: 1
          - Industry: 2
          - Artistry: 2
          - Statecraft: 5
        - FoundedReligion: Buddhism
        - Relationships:
          - The Inca:
            - Distance: Close
            - Our Master (Voluntary)
            - Open Borders
            - Declaration of Friendship
          - Germany:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
          - Greece:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - Russia:
            - Distance: Neighbors
            - War (Our Score: -82%; Our War Weariness: 100%)
            - Denounced Them
          - The Zulus:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - India:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
        - Votes: 13
        
        ## Player 6
        - Civilization: Germany
        - Leader: Bismarck
        - IsMajor: true
        - OurOpinionToThem:
          - You have both chosen to adopt the Autocracy Ideology. (999)
          - You have denounced one of their declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - You have gone to war in the past.
          - Our real approach is Neutral.
          - You have denounced a leader they made a Declaration of Friendship with! (-11)
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - Our leader has formed a private opinion to this player (-30).
          - Religious differences strain your relationship. (-30)
          - Our leader has expressed a public opinion to this player (-32).
        - TheirOpinionToUs:
          - You have both chosen to adopt the Autocracy Ideology.
          - Your votes supported their civ's interests in the World Congress.
          - You have denounced one of their declared enemies!
          - We have Pledged to Protect the same City-States.
          - We have similar Social Policies.
          - You have no contested borders.
          - We have different religious beliefs.
          - They have denounced us!
          - They don't want anything to do with us right now.
          - You are competing for the favor of the same City-States!
          - They have some early concerns about your warmongering. (They dislike warmongers.)
          - They are jealous of our superior technology!
          - You have made a Defensive Pact with one of their enemies!
          - Their friends or allies have denounced you!
          - The leader has expressed a public opinion to you (-50).
          - You have made a Declaration of Friendship with one of their enemies!
          - You have denounced a leader they made a Declaration of Friendship with!
        - Score: 1718
        - Era: Atomic
        - Technologies: 63
        - Cities: 6
        - Population: 129
        - Territory: 170
        - Gold: 249
        - GoldPerTurn: 21
        - HappinessSituation: Happy
        - HappinessPercentage: 62
        - MilitaryStrength: 3425
        - TourismPerTurn: 451.5
        - CulturePerTurn: 751
        - PolicyBranches:
          - Autocracy: 3
          - Artistry: 3
          - Progress: 6
          - Rationalism: 2
          - Statecraft: 3
          - Imperialism: 5
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Inca:
            - Distance: Neighbors
            - War (Our Score: 26%; Our War Weariness: 36%)
            - Denounced Them
          - The Zulus:
            - Distance: Close
            - Denounced Them
          - Greece:
            - Distance: Close
            - Denounced Them
          - Russia:
            - Distance: Neighbors
            - Denounced Them
          - Venice:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 24%)
            - Denounced Them
          - India:
            - Distance: Neighbors
            - Declaration of Friendship
        - Votes: 6
        
        ## Player 7
        - Civilization: The Zulus
        - Leader: Shaka
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: The Inca, Our top defensive pact ally: The Inca
          - Our top World Congress ally: Venice, Our top World Congress rival: Greece
          - Our top Competitor: Russia
        - Score: 2158
        - Era: Atomic
        - GoldenAge: 10 turns remaining
        - Technologies: 65
        - CurrentResearch: Electronics (Estimated in 2 turns)
        - NextPolicyTurns: 8
        - Cities: 9
        - Population: 218
        - Territory: 246
        - BestSettlementLocation:
          - 72, 33 (Quality: 93%; 19 tiles from us; near Germany, 11 tiles away; New Continent)
          - 11, 48 (Quality: 37%; 6 tiles from us)
          - 10, 47 (Quality: 0%; 4 tiles from us)
          - 9, 47 (Quality: 0%; 4 tiles from us)
          - 3, 50 (Quality: 0%; 5 tiles from us)
        - Gold: 1610
        - GoldPerTurn: 501
        - HappinessSituation: Happy
        - HappinessPercentage: 54
        - MilitaryUnits: 75
        - MilitarySupply: 74
        - MilitaryStrength: 5656
        - TourismPerTurn: 616.5
        - CulturePerTurn: 1318
        - FaithPerTurn: 235
        - SciencePerTurn: 1450
        - PolicyBranches:
          - Rationalism:
            - Rationalism
            - Scientific Revolution
            - Enlightenment
          - Progress:
            - Progress
            - Organization
            - Liberty
            - Expertise
            - Equality
            - Fraternity
          - Authority:
            - Authority
            - Tribute
            - Imperium
          - Fealty:
            - Fealty
          - Industry:
            - Industry
            - Division of Labor
          - Artistry:
            - Artistry
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Shadow Networks
            - Trade Confederacy
          - Autocracy:
            - Elite Forces
            - United Front
          - Imperialism:
            - Imperialism
        - FoundedReligion: Protestantism
        - Relationships:
          - The Inca:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Germany:
            - Distance: Close
          - Greece:
            - Distance: Distant
            - Open Borders
          - Russia:
            - Distance: Neighbors
            - Denounced Them
          - Venice:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - India:
            - Distance: Close
            - War (Our Score: 10%; Our War Weariness: 11%)
            - Denounced Them
        - Votes: 8
        
        ## Player 22
        - Civilization: Melbourne
        - Leader: City State
        - MajorAlly: Greece
        - Population: 29
        - MajorityReligion: Buddhism
        - Relationships:
          - The Inca: Friends (Influence: 112, Distance: Far)
          - Germany: Friends (Influence: 681, Distance: Neighbors, Protected)
          - Greece: Ally (Influence: 749, Distance: Distant, Protected)
          - The Zulus: Friends (Influence: 181, Distance: Far)
          - Russia: Friends (Influence: 131, Distance: Far, Protected)
          - Venice: Friends (Influence: 289, Distance: Distant)
          - India: War (Influence: -60, Distance: Distant)
        
        ## Player 23
        - Civilization: Trowulan
        - Leader: City State
        - MajorAlly: Greece
        - Population: 33
        - Relationships:
          - The Inca: Neutral (Influence: 0, Distance: Neighbors)
          - Germany: Friends (Influence: 343, Distance: Close, Protected)
          - Greece: Ally (Influence: 749, Distance: Close, Protected)
          - The Zulus: Friends (Influence: 205, Distance: Far)
          - Russia: Friends (Influence: 403, Distance: Close, Protected)
          - Venice: Friends (Influence: 115, Distance: Far)
          - India: War (Influence: -60, Distance: Close)
        - 24: Defeated Minor Civilization Vatican City
        
        ## Player 25
        - Civilization: Quebec City
        - Leader: City State
        - MajorAlly: Greece
        - Population: 23
        - MajorityReligion: Hinduism
        - Relationships:
          - The Inca: Friends (Influence: 209, Distance: Close)
          - Germany: Friends (Influence: 726, Distance: Neighbors, Protected)
          - Greece: Ally (Influence: 895, Distance: Neighbors, Protected)
          - The Zulus: Friends (Influence: 73, Distance: Distant)
          - Russia: Friends (Influence: 208, Distance: Close, Protected)
          - Venice: Friends (Influence: 345, Distance: Far)
          - India: War (Influence: -60, Distance: Close)
        
        ## Player 26
        - Civilization: Antwerp
        - Leader: City State
        - MajorAlly: Greece
        - Population: 18
        - Relationships:
          - The Inca: Neutral (Influence: -27, Distance: Close)
          - Germany: Friends (Influence: 288, Distance: Distant, Protected)
          - Greece: Ally (Influence: 1136, Distance: Distant)
          - The Zulus: Friends (Influence: 381, Distance: Neighbors)
          - Russia: Friends (Influence: 420, Distance: Neighbors, Protected)
          - Venice: Neutral (Influence: 0, Distance: Close)
          - India: War (Influence: -60, Distance: Far)
        
        ## Player 27
        - Civilization: Shanghai
        - Leader: City State
        - MajorAlly: Greece
        - Population: 18
        - Relationships:
          - The Inca: Neutral (Influence: 0, Distance: Close)
          - Germany: Friends (Influence: 145, Distance: Distant, Protected)
          - Greece: Ally (Influence: 839, Distance: Distant, Protected)
          - The Zulus: Friends (Influence: 53, Distance: Close)
          - Russia: Friends (Influence: 217, Distance: Neighbors, Protected)
          - Venice: Neutral (Influence: 22, Distance: Distant)
          - India: War (Influence: -60, Distance: Distant)
        
        ## Player 28
        - Civilization: Oviedo
        - Leader: City State
        - MajorAlly: The Zulus
        - Population: 12
        - Relationships:
          - The Inca: Neutral (Influence: 0, Distance: Far)
          - Germany: Friends (Influence: 47, Distance: Distant)
          - Greece: Friends (Influence: 936, Distance: Distant)
          - The Zulus: Ally (Influence: 1061, Distance: Neighbors, Protected)
          - Russia: Friends (Influence: 396, Distance: Neighbors, Protected)
          - Venice: Neutral (Influence: 3, Distance: Close)
          - India: War (Influence: -60, Distance: Distant)
        - 29: Defeated Minor Civilization Singapore
        
        ## Player 30
        - Civilization: M'banza-Kongo
        - Leader: City State
        - MajorAlly: The Zulus
        - Population: 19
        - MajorityReligion: Protestantism
        - Relationships:
          - The Inca: Neutral (Influence: 27, Distance: Close)
          - Germany: Friends (Influence: 60, Distance: Far)
          - Greece: Friends (Influence: 222, Distance: Distant, Protected)
          - The Zulus: Ally (Influence: 346, Distance: Close, Protected)
          - Russia: Friends (Influence: 134, Distance: Neighbors, Protected)
          - Venice: Friends (Influence: 44, Distance: Distant)
          - India: War (Influence: -60, Distance: Distant)
        
        ## Player 31
        - Civilization: Zuunmod
        - Leader: City State
        - Population: 23
        - Relationships:
          - The Inca: Neutral (Influence: 27, Distance: Far)
          - Germany: Friends (Influence: 159, Distance: Neighbors, Protected)
          - Greece: Friends (Influence: 218, Distance: Close, Protected)
          - The Zulus: Friends (Influence: 70, Distance: Distant)
          - Russia: Friends (Influence: 320, Distance: Neighbors, Protected)
          - Venice: Friends (Influence: 44, Distance: Distant)
          - India: Neutral (Influence: -59, Distance: Far)
        
        ## Player 32
        - Civilization: Tyre
        - Leader: City State
        - MajorAlly: Greece
        - Population: 17
        - MajorityReligion: Hinduism
        - Relationships:
          - The Inca: Friends (Influence: 220, Distance: Close)
          - Germany: Neutral (Influence: -8, Distance: Far)
          - Greece: Ally (Influence: 550, Distance: Distant)
          - The Zulus: Neutral (Influence: 18, Distance: Close, Protected)
          - Russia: Neutral (Influence: -55, Distance: Far)
          - Venice: Friends (Influence: 364, Distance: Distant)
          - India: War (Influence: -60, Distance: Close)
        
        ## Player 33
        - Civilization: Segou
        - Leader: City State
        - MajorAlly: The Inca
        - Population: 27
        - Relationships:
          - The Inca: Ally (Influence: 733, Distance: Neighbors, Protected)
          - Germany: War (Influence: -60, Distance: Far)
          - Greece: Friends (Influence: 731, Distance: Distant)
          - The Zulus: Friends (Influence: 97, Distance: Neighbors, Protected)
          - Russia: War (Influence: -60, Distance: Close)
          - Venice: Friends (Influence: 234, Distance: Distant)
          - India: War (Influence: -60, Distance: Far)
        
        ## Player 34
        - Civilization: Kathmandu
        - Leader: City State
        - MajorAlly: The Inca
        - Population: 20
        - MajorityReligion: Protestantism
        - Relationships:
          - The Inca: Ally (Influence: 94, Distance: Neighbors, Protected)
          - Germany: War (Influence: -60, Distance: Distant)
          - Greece: Friends (Influence: 218, Distance: Distant)
          - The Zulus: Friends (Influence: 176, Distance: Close, Protected)
          - Russia: War (Influence: -60, Distance: Neighbors)
          - Venice: Friends (Influence: 36, Distance: Distant)
          - India: War (Influence: -60, Distance: Far)
        
        ## Player 35
        - Civilization: Lutetia
        - Leader: City State
        - MajorAlly: Greece
        - Population: 28
        - Relationships:
          - The Inca: Neutral (Influence: -38, Distance: Close)
          - Germany: Friends (Influence: 136, Distance: Distant, Protected)
          - Greece: Ally (Influence: 632, Distance: Distant, Protected)
          - The Zulus: Neutral (Influence: 28, Distance: Far, Protected)
          - Russia: Friends (Influence: 91, Distance: Close, Protected)
          - Venice: Friends (Influence: 56, Distance: Distant)
          - India: War (Influence: -60, Distance: Distant)
        
        ## Player 36
        - Civilization: Antananarivo
        - Leader: City State
        - MajorAlly: Germany
        - Population: 16
        - MajorityReligion: Hinduism
        - Relationships:
          - The Inca: War (Influence: -60, Distance: Close)
          - Germany: Ally (Influence: 923, Distance: Neighbors, Protected)
          - Greece: Friends (Influence: 129, Distance: Far)
          - The Zulus: Friends (Influence: 244, Distance: Close, Protected)
          - Russia: Friends (Influence: 376, Distance: Neighbors, Protected)
          - Venice: War (Influence: -60, Distance: Far)
          - India: Friends (Influence: 660, Distance: Neighbors, Protected)
        
        ## Player 37
        - Civilization: Vienna
        - Leader: City State
        - MajorAlly: Greece
        - Population: 10
        - Relationships:
          - The Inca: Friends (Influence: 95, Distance: Close)
          - Germany: Friends (Influence: 496, Distance: Distant)
          - Greece: Ally (Influence: 335, Distance: Distant)
          - The Zulus: Friends (Influence: 92, Distance: Neighbors, Protected)
          - Russia: Friends (Influence: 233, Distance: Neighbors, Protected)
          - Venice: Friends (Influence: 80, Distance: Distant)
          - India: War (Influence: -60, Distance: Distant)
        - 63: Barbarians
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: Russia
        - India:
          - CapitalsControlled:
            - Athens
            - Delhi
          - CapitalsPercentage: 25
        - Russia:
          - CapitalsControlled:
            - Washington
            - Moscow
          - CapitalsPercentage: 25
        - The Inca:
          - CapitalsControlled:
            - Cusco
            - Venice
          - CapitalsPercentage: 25
        
        ## ScienceVictory
        - Unlocked in the Information era
        
        ## CulturalVictory
        - CivsNeeded: 6
        - Contender: India
        - Germany:
          - Influences:
            - The Inca: Exotic (19%) - Rising Slowly (tourism/culture ratio 135%)
            - The Zulus: Familiar (28%) - Rising Slowly (tourism/culture ratio 58%)
            - Greece: Familiar (26%) - Rising Slowly (tourism/culture ratio 64%)
            - Russia: Exotic (13%) - Rising Slowly (tourism/culture ratio 35%)
            - Venice: Familiar (32%) - Rising Slowly (tourism/culture ratio 72%)
            - India: Exotic (16%) - Rising Slowly (tourism/culture ratio 42%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Greece:
          - Influences:
            - The Inca: Exotic (15%) - Rising Slowly (tourism/culture ratio 171%)
            - Germany: Exotic (21%) - Rising Slowly (tourism/culture ratio 104%)
            - Venice: Exotic (23%) - Rising Slowly (tourism/culture ratio 107%)
            - Russia: Exotic (11%) - Rising Slowly (tourism/culture ratio 41%)
            - The Zulus: Exotic (21%) - Rising Slowly (tourism/culture ratio 74%)
            - India: Exotic (9%) - Rising Slowly (tourism/culture ratio 33%)
          - PolicyPercentage: 96
          - InfluentialCivs: 0
        - India:
          - Influences:
            - The Inca: Influential (119%) - Rising (tourism/culture ratio 758%)
            - Germany: Influential (173%) - Rising (tourism/culture ratio 550%)
            - Greece: Influential (132%) - Rising (tourism/culture ratio 267%)
            - Russia: Influential (100%) - Rising (tourism/culture ratio 227%)
            - The Zulus: Influential (137%) - Rising (tourism/culture ratio 292%)
            - Venice: Influential (143%) - Rising (tourism/culture ratio 358%)
          - PolicyPercentage: 100
          - InfluentialCivs: 6
        - Russia:
          - Influences:
            - The Inca: Familiar (37%) - Rising Slowly (tourism/culture ratio 54%)
            - Germany: Familiar (35%) - Rising Slowly (tourism/culture ratio 7%)
            - Greece: Familiar (31%) - Rising Slowly (tourism/culture ratio 6%)
            - The Zulus: Familiar (37%) - Rising Slowly (tourism/culture ratio 12%)
            - Venice: Familiar (31%) - Rising Slowly (tourism/culture ratio 4%)
            - India: Exotic (23%) - Rising Slowly (tourism/culture ratio 8%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - The Inca:
          - Influences:
            - Germany: Familiar (44%) - Rising Slowly (tourism/culture ratio 74%)
            - Greece: Familiar (35%) - Rising Slowly (tourism/culture ratio 59%)
            - The Zulus: Popular (52%) - Rising Slowly (tourism/culture ratio 79%)
            - Russia: Exotic (23%) - Rising Slowly (tourism/culture ratio 25%)
            - Venice: Popular (91%) - Rising (22 turns to Influential, tourism/culture ratio 215%)
            - India: Exotic (23%) - Rising Slowly (tourism/culture ratio 28%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - The Zulus:
          - Influences:
            - The Inca: Familiar (32%) - Rising (400 turns to Influential, tourism/culture ratio 223%)
            - Germany: Familiar (41%) - Rising Slowly (tourism/culture ratio 121%)
            - Greece: Familiar (34%) - Rising Slowly (tourism/culture ratio 79%)
            - Russia: Exotic (23%) - Rising Slowly (tourism/culture ratio 50%)
            - Venice: Popular (72%) - Rising (100 turns to Influential, tourism/culture ratio 189%)
            - India: Exotic (19%) - Rising Slowly (tourism/culture ratio 41%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Venice:
          - Influences:
            - The Inca: Exotic (23%) - Rising Slowly (tourism/culture ratio 135%)
            - Germany: Familiar (32%) - Rising Slowly (tourism/culture ratio 78%)
            - Greece: Familiar (28%) - Rising Slowly (tourism/culture ratio 61%)
            - Russia: Exotic (17%) - Rising Slowly (tourism/culture ratio 27%)
            - The Zulus: Familiar (41%) - Rising Slowly (tourism/culture ratio 66%)
            - India: Exotic (13%) - Rising Slowly (tourism/culture ratio 22%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        
        ## DiplomaticVictory
        - VotesNeeded: 44
        - Status: World Congress - Voting in 9 turns
        - ActiveResolutions:
          - Sanction: Russia:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: 412
          - Sanction: India:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: 412
          - Global Peace Accords:
            - Description: Unit maintenance costs are raised by 25% Gold. 2.0x Warmonger penalties for capturing cities and declaring war, and 0.5x Warmonger scores decay.
            - EnactedOn: 412
          - Incan Sphere of Influence: Kathmandu:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 412
          - Greek Sphere of Influence: Vienna:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 412
          - Zulu Sphere of Influence: M'banza-Kongo:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 421
          - Greek Sphere of Influence: Quebec City:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 412
          - Scholars In Residence:
            - Description: Civilizations have -20% Research cost for Technologies already discovered by another Civilization. Additional -2% for every City-State Ally, up to -50%.
            - EnactedOn: 412
          - World Ideology: Freedom:
            - Description: Designate an Ideology as the official World Ideology. Civilizations following the Ideology get an additional Delegate, plus 1 Delegate for every other Civilization that follows the Ideology. Public opinion in favor of that Ideology is increased for all Civilizations. Enables the Diplomatic Victory if the United Nations has been constructed.
              Available once any Civilization discovers Nuclear Fission.
            - EnactedOn: 412
          - Greek Sphere of Influence: Trowulan:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 412
          - Travel Ban:
            - Description: Restricts international travel between Civilizations. Reduces the Tourism modifier for all Civilizations by 35%.
              Available once any Civilization discovers Flight.
            - EnactedOn: 412
          - Greek Sphere of Influence: Melbourne:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 412
          - Open Door: Zuunmod:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 412
        - Proposals:
          - Enact: Endowment for the Arts:
            - Description: Increases up to 33% generation of Great Writers, Artists, and Musicians. Decreases up to 33% generation of Great Scientists, Engineers, and Merchants.
              Civilizations with Scores from Policies and Great Works below the global median will receive a boost to Production and Culture up to 33%.
              Details: The boosts are proportional to the difference between the score of the Civilization and the leader.
            - Proposer: The Inca
          - Enact: Venetian Sphere of Influence: Tyre:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - Proposer: Venice
          - Repeal: Incan Sphere of Influence: Kathmandu:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - Proposer: Greece
        - Contender: Greece
        - Germany:
          - Delegates: 6
          - VictoryPercentage: 13
        - Greece:
          - Delegates: 24
          - VictoryPercentage: 54
        - India:
          - Delegates: 7
          - VictoryPercentage: 15
        - Russia:
          - Delegates: 3
          - VictoryPercentage: 6
        - The Inca:
          - Delegates: 18
          - VictoryPercentage: 40
        - The Zulus:
          - Delegates: 8
          - VictoryPercentage: 18
        - Venice:
          - Delegates: 13
          - VictoryPercentage: 29
        
        # Briefings
        ## Military Briefing
        **Zulu Military Briefing – Turn 423 (Post‑event)**  
        
        **1. Front‑line Situation – Indian War Front**  
        
        | City (Owner) | Zone ID | Coordinates (X,Y) | Current Garrison (Units) | Approx. Combat Strength* |
        |--------------|--------|-------------------|---------------------------|--------------------------|
        | **Delhi** (India) | 1060 (Land) | (40, 9) | • Artillery (1) – Strength 27, Ranged 50 | **≈ 77** |
        | **Varanasi** (India) – not listed as a separate zone this turn (city exists but no dedicated zone data). No Zulu‑visible enemy units reported within its immediate zone. | – | – | – | – |
        | **Delhi (City‑Tile)** – also hosts a **Bomber** (Air unit) stationed in the same zone (see Event 423‑7: India produced a **Caravan**, no Bomber change). | – | – | – | – |
        
        *Strength values are taken from the unit‑stat tables; promotions are not reflected in the current data.
        
        **Key Change Since Turn 418:**  
        - The **Delhi zone (1060)** now contains an **Indian Artillery unit** (previously the zone was listed without enemy units). The strength estimate rises to ~77, matching the previous estimate.  
        - No new Indian AA units have appeared in the Delhi zone; Varanasi remains without a reported zone, implying no immediate enemy presence detectable by the Zulu AI.
        
        **2. Zulu Air Assets – Paratrooper & Bomber Availability**  
        
        - **Paratrooper:** 1 Paratrooper remains in **Nodwengu** (city 9570). No change from Turn 418.  
        - **Bomber (Carrier for Paratrooper):** 1 Bomber (Triplane ID 17486) has been **re‑based** to **Nodwengu** (Event 423‑11). This Bomber now serves as the transport platform for the Paratrooper.  
        
        **Distance from Nodwengu to Delhi:** ~ 28 tiles (straight‑line).  
        **Distance from Nodwengu to Varanasi:** ~ 33 tiles (estimated; Varanasi not explicitly zoned).  
        
        **Air‑defence Situation Near Targets:**  
        - No AA units are reported in the Delhi zone.  
        - No AA units are reported in any zone adjacent to Delhi.  
        
        **Implication:** Air‑drop risk remains low for Delhi; Varanasi still lacks explicit zone data, but no AA presence has been detected.
        
        **3. Naval Force Posture – Battleships & Escorts**  
        
        | Sea‑Zone (ID) | Primary Naval Units (Zulu) | Supporting Units | Approx. Strength* |
        |---------------|----------------------------|------------------|-------------------|
        | **‑1455** (Umgungundlovu Sea‑Zone) | 4 Battleships | 2 Fleet Destroyers, 2 Riflemen | **≈ ~ 400** total (Battleship 60 + Ranged 75 each) |
        | **‑8308** (Nodwengu Sea‑Zone) | 1 Battleship | – | **≈ 60** |
        | **‑1078** (Vienna Sea‑Zone) | 1 Battleship | – | **≈ 60** |
        | **‑17712** (Agra Sea‑Zone) | 2 Dreadnoughts | – | **≈ 130** (50 + Ranged 65 each) |
        | **‑2475** (Corihuayrachina Sea‑Zone) | 1 Dreadnought | – | **≈ 50** |
        | **‑9570** (Nodwengu Sea‑Zone) | 1 Fleet Destroyer, 1 Cruiser, 1 Dreadnought | – | **≈ ~ 155** |
        | **‑1068** (Shanghai Sea‑Zone) | 1 Special Forces (no naval strength) | – | – |
        
        *Strength values are summed from unit‑stat tables; exact totals vary with promotions (not shown).
        
        **Key Change Since Turn 418:**  
        - The **Umgungundlovu sea‑zone (‑1455)** now fields **4 Battleships** (previously 4 Battleships were reported, unchanged).  
        - Additional **Fleet Destroyer** and **Cruiser** appear in **‑9570** (Nodwengu sea‑zone) – a new naval grouping not present in the previous briefing.  
        - No battleships are positioned within striking range of Indian coastal cities (India possesses no accessible coastal cities near the front), so naval fire support remains unavailable for the Indian campaign.
        
        **4. Land Force Distribution – Zone Strength Overview**  
        
        | Zone (City) | Dominance | Friendly Strength | Enemy Strength | Neutral Strength |
        |-------------|-----------|-------------------|----------------|------------------|
        | **Ulundi** (1082) | Friendly | 5,698 | – | 406 |
        | **Umgungundlovu** (1455) | Friendly | 6,699 | – | – |
        | **Nobamba** (1847) | Friendly | 3,745 | – | 440 |
        | **Bulawayo** (2018) | Friendly | 2,179 | – | 373 |
        | **Antwerp** (1067) | Friendly (Neutral zone) | 4,099 | – | 323 |
        | **M'banza‑Kongo** (1071) | Friendly (Neutral zone) | 1,734 | – | 203 |
        | **Corihuayrachina** (2475) – Enemy | Enemy | 441 | 844 | 766 |
        | **Huamanga** (2943) – Enemy | Enemy | 572 | 1,306 | 588 |
        | **Delhi** (1060) – Enemy | Enemy | – | 1,207 (Artillery 1) | 200 |
        
        **Key Developments Since Turn 418:**  
        - The **Delhi zone (1060)** now shows an **enemy Artillery unit** (strength 27/50). This presence was absent in the prior briefing, indicating a modest increase in Indian defensive firepower.  
        - No new enemy units have appeared in other Zulu‑adjacent zones.  
        - Zulu land forces continue to dominate all own zones, with total friendly strength across zoned cities exceeding 30,000 combat points, well above any neighboring enemy concentrations.
        
        **5. Recent Combat Events (Turn 422‑423)**  
        
        - **Russian Submarine Engagements (Turn 422):** Three combat results involving Russian Attack Submarines (unit ID 17165) resulted in the submarines taking damage and ultimately being destroyed. No Zulu units were involved.  
        - **Inca / Venice Ground Combat (Turn 423):**  
          - Two engagements at **Corfu (City 2648)** resulted in heavy damage to the defending Venetian **Machine Gun** unit (remaining HP ≈ 37).  
          - An engagement at **Corihuayrachina (City 2475)** saw the Inca **Anti‑Aircraft Gun** destroyed (remaining HP 0).  
          - An engagement at **Cusco (City 1059)** resulted in the Inca **Anti‑Aircraft Gun** being eliminated (remaining HP 0).  
        - **Indian Land Combat (Turn 423):**  
          - A **Rifleman** in **Delhi** took damage (remaining HP 35).  
          - A **Landship** in **India** (presumably near Delhi) sustained damage (remaining HP 18).  
        - **Zulu Unit Re‑base (Turn 423‑11):** A **Triplane** (DefenceAir) was re‑based to **Nodwengu** (city 9570). This reinforces air presence at the southern coastal city.  
        
        **6. Supply & Production Snapshot**  
        
        - **Military Units:** 75 total; **Military Supply:** 74 (near full supply).  
        - **Gold:** 1,610; **Gold/Turn:** +501 (strong economy, supporting continued production).  
        - **Production Queues:**  
          - Several cities (Ulundi, Umgungundlovu, Nobamba, Kwadukuza, Nongoma, Ondini, Nodwengu) are engaged in **Public Works** or **Strategic Defense System** projects, indicating a focus on infrastructure and defense.  
          - **Bulawayo** will complete its **Strategic Defense System** this turn.  
          - **Agra** (occupied) is producing a **Hotel**; no military units are queued there.  
        
        **7. Comparison to Turn 418 Briefing**  
        
        | Aspect | Turn 418 | Turn 423 | Δ / Notable Change |
        |--------|----------|----------|--------------------|
        | **Delhi Enemy Garrison** | Not explicitly listed (no enemy units shown) | Artillery (1) present (strength 27/50) | Added defensive firepower for India |
        | **Paratrooper Transport** | Bomber unspecified; Paratrooper at Nodwengu | Bomber (Triplane) re‑based to Nodwengu | Clear transport platform now confirmed |
        | **Naval Assets** | 4 Battleships (Umgungundlovu), 2 Dreadnoughts (Agra), assorted escorts | Same battleships plus new **Fleet Destroyer, Cruiser** in sea‑zone ‑9570 | Incremental increase in naval firepower, still out of range of Indian front |
        | **Land Zone Strength** | Zulu zones dominated; enemy zones limited | Same dominance; new enemy Artillery in Delhi; Inca AA units destroyed in separate combats | Minor shift in enemy composition; Zulu dominance unchanged |
        | **Combat Events** | No specific combat recorded in brief | Multiple combats: Russian submarines destroyed, Inca/Italian units damaged/killed, Indian Rifleman damaged, Zulu Triplane re‑based | Activity increased, but no direct Zulu‑enemy engagements reported |
        | **Supply** | Not detailed | Military Supply 74/75 (near full) | Supply remains strong |
        
        **8. High‑Level Observations**  
        
        - **Force Balance:** Zulu friendly strength (≈ 30k) vastly exceeds the highest single enemy zone strength (Russia ≈ 15.6k, India ≈ 1.9k, Inca ≈ 1.3k).  
        - **Front‑line Pressure:** The only immediate enemy presence on the Indian front is the Artillery unit in Delhi; no AA or ground units threaten Zulu air operations.  
        - **Air Capability:** A single Bomber (Triplane) is now positioned at Nodwengu, enabling potential air‑lift of the lone Paratrooper to Delhi.  
        - **Naval Reach:** All Zulu capital ships remain far from any Indian coastal objectives; naval fire support cannot influence the Indian campaign at this stage.  
        - **Logistics:** Military supply is near maximum; gold income is healthy, allowing continued production of both land and naval units without immediate economic strain.  
        
        All data presented reflect the current game state (Turn 423) and are derived directly from the supplied reports. No speculative recommendations are included.
        
        ## Economy Briefing
        **Economic Brief – The Zulus (Player 7, Shaka)**  
        *Post‑Turn 423 – after processing events and city updates*  
        
        ---
        
        ## 1. Empire‑wide Macro‑Economics (Turn 423)
        
        | Metric | Current Value (Turn 423) | Δ vs. Turn 418* | Comment |
        |--------|--------------------------|----------------|---------|
        | **Gold Treasury** | **1 610 G** | **+ 514 G** | Gold surplus continues to grow thanks to strong internal production and profitable trade‑routes. |
        | **Gold / turn (net)** | **≈ 501 G/t** (≈ 620 G/t income – ≈ 119 G/t upkeep) | **+ ≈ 266 G/t** | Net gold income has rebounded sharply: new **Gold‑for‑resource** deals (Inca, Venice, Greece) and the end of several outbound routes that were draining gold. Unit‑maintenance cost remains low thanks to the 50 % discount. |
        | **Production / turn** (all cities) | **≈ 1 489 P/t** | **+ ≈ 215 P/t** | New **Strategic Defense System** (Bulawayo) and **Airport** (Nodwengu) finished; additional factories and improvements raise overall output. |
        | **Science / turn** | **≈ 1 450 S/t** | **+ ≈ 145 S/t** | **Electronics** research (≈ 2 turns to finish) is now boosted by Great‑Merchant routes (+ 7.5 S/t each) and the newly‑completed **Research Lab** in several cities. |
        | **Culture / turn** | **≈ 1 318 C/t** | **+ ≈ 331 C/t** | New **Wire Service** (Ulundi) and **Broadcast Tower** yields, plus extra Great Works, increase cultural output markedly. |
        | **Tourism / turn** | **≈ 617 T/t** | **≈ 0 T/t** | Tourism remains steady; the recent conversion of Kwadukuza and Nongoma to Protestantism adds a small bump, offset by the slight dip in culture growth earlier. |
        | **Faith / turn** | **≈ 235 F/t** | **+ 66 F/t** | Conversions of Kwadukuza and Nongoma to Protestantism now generate Faith per turn; modest increase. |
        | **Happiness %** | **≈ 54 % (Happy)** | **+ 5 %** | New luxury‑resource trades (Perfume, Ivory, Salt, Deer) and a **Hotel** in Nongoma raise happiness, removing the combat penalty. |
        | **Military Strength** | **5 656** (75 units, supply 74) | **‑ ≈ 200** | Slight reduction in unit count after a few older units were disbanded; overall strength still well above rivals. |
        | **Era** | **Atomic** – **Electronics** research (≈ 2 turns left) | **+ ≈ 6 turns** | Science dip reversed; on schedule to finish Electronics before the next era jump. |
        | **Trade‑route net gold** | **≈ + 230 G/t** (inbound ≈ + 170 G/t, outbound ≈ ‑ 40 G/t) | **+ ≈ 90 G/t** | New inbound routes from **Venice** city‑states (Cattaro, Venice, Singapore) bring higher gold; most outbound routes are now short‑term and nearing completion. |
        | **Trade‑route net science** | **≈ + 70 S/t** (inbound ≈ + 55 S/t, outbound ≈ ‑ 15 S/t) | **+ ≈ 15 S/t** | Continued Great‑Merchant yields; small outbound loss from a few routes that are ending. |
        | **Trade‑route net culture** | **≈ + 38 C/t** (inbound ≈ + 30 C/t, outbound ≈ ‑ ‑ 8 C/t) | **+ ≈ 34 C/t** | New cultural yields from inbound Venice routes and the **Wire Service** building. |
        
        \*Δ is the net change since the previous briefing (Turn 418). All figures are rounded.
        
        ---
        
        ## 2. Resource Position (Turn 423)
        
        | Resource | Stock | Immediate Need / Note |
        |----------|-------|-----------------------|
        | **Coal** | **‑3** (deficit) | Still required for **Factory** and **Railroad** upgrades; consider purchasing or trading (India has Coal). |
        | **Uranium** | **8** | Sufficient for a **Nuclear Power Plant** (1) and future **Nuclear Missile** projects. |
        | **Aluminum** | **17** | Covers upcoming **Carrier** (12) and **Battleship** (6) construction. |
        | **Iron** | **2** | Enough for a few **Impi**; surplus not critical now. |
        | **Oil** | **0** | No oil‑based units currently planned. |
        | **Luxury resources** (Perfume 1, Ivory 2, Salt 5, Deer 8, etc.) | **Stable** | Actively traded for Gold; happiness bolstered. |
        | **Strategic resources** (Copper 1, Lapis 1) | **Minimal** | Not needed for current production queue. |
        
        ---
        
        ## 3. Recent Economic Events (Turn 423)
        
        | Event | Economic Impact |
        |-------|-----------------|
        | **Kwadukuza** & **Nongoma** converted to **Protestantism** (Turn 423) | Adds Faith per turn (+ ~ 30 F/t each) and improves happiness via religious bonuses. |
        | **New city – Nodwengu** created (Turn 423) | Immediate production boost (+ ≈ 120 P/t) and extra science/culture from its **Research Lab** and **Factory** improvements. |
        | **Mine improvement** on Plains‑Hills 7,45 completed | Small increase in production (+ ≈ 4 P/t) and yields for the adjacent city. |
        | **Hotel built in Nongoma** (Turn 423) | Provides extra Gold (+ ≈ 8 G/t) and happiness (+ 2 %). |
        | **Golden Age extended** (10 turns remaining) | + 25 % production, gold, and science during the remaining GA turns; current GA effects are still active. |
        | **World Congress voting in 9 turns** – Zulus hold **8 delegates** (≈ 18 % share) | Gold surplus grants flexibility to purchase additional influence if critical votes arise. |
        | **Sanctions on Russia & India** – no Zulu routes with them | No loss of income; all Zulu trade routes are with **Venice**, **city‑states**, or **friendly** civs. |
        | **Open Door on Zuunmod** – already active | Stabilises influence; no impact on income. |
        | **Zulu Sphere of Influence proposal for M'banza‑Kongo** (active since Turn 421) | If passed, will secure a permanent ally and a permanent **Gold** stream (+ 24 G/t) plus resource exchange. |
        | **City‑state Deals** – continued gold‑for‑luxury swaps (Venice, Greece, India) | Keeps luxury resource stock adequate, supports happiness, and adds net gold (+ ≈ 30 G/t). |
        
        ---
        
        ## 4. Settlement Opportunities (Unchanged)
        
        | Location | Distance from nearest city | Quality | Strategic Value |
        |----------|----------------------------|---------|-----------------|
        | **(72, 33)** | 19 tiles | **96 %** | Highest‑quality site on a **new continent** near Germany (11 tiles). Ideal for a **Harbor/Port**, future **Naval Yard**, and high‑yield interior tiles. |
        | **(11, 48)** | 6 tiles | **47 %** | Moderate yields; near existing coastal cities, suitable for a **resource‑rich** settlement (wheat, deer, luxury). |
        | **(10, 47)** | 4 tiles | **22 %** | Low‑mid quality; useful only for strategic positioning (choke point). |
        | **(9, 47)** | 4 tiles | **10 %** | Very low yields; not recommended unless needed for defense. |
        | **(3, 50)** | 5 tiles | **0 %** | Poor yields; only consider as a defensive outpost. |
        
        *Recommendation:* The **96 %** site at (72, 33) remains the premier long‑term investment, offering both high tile yields and naval development potential. The **47 %** site at (11, 48) is the next best option for immediate resource expansion and a modest new city.
        
        ---
        
        ## 5. Diplomatic & Trade Context (Economic Lens)
        
        * **World Congress** – voting in 9 turns; Zulus hold **8 delegates** (≈ 18 %). Treasury surplus allows purchase of additional influence if a decisive vote is required.  
        * **Sanctions on Russia & India** – block any trade or corporation franchises with those civs; all Zulu routes remain with **Venice**, **city‑states**, or **friendly** parties, so no direct loss.  
        * **Open Door (Zuunmod)** – already active; stabilises influence levels with that city‑state.  
        * **City‑state deals** – ongoing gold‑for‑luxury exchanges (Venice, Greece, India) keep luxury resources sufficient and boost happiness.  
        * **Proposed Zulu Sphere of Influence (M'banza‑Kongo)** – pending; successful enactment locks a high‑value ally, delivering a permanent **gold** boost (+ 24 G/t) and securing additional resource flow.  
        
        ---
        
        ## 6. Summary of Economic Position (Turn 423)
        
        * **Liquidity:** Treasury now at **1 610 G**, with a healthy net gold income (**≈ 501 G/t**). Gold flow has recovered from the earlier deficit.  
        * **Production:** Strong increase (**≈ 1 489 P/t**), thanks to newly finished industrial buildings (Strategic Defense System, Airport, Wire Service) and the new city **Nodwengu**.  
        * **Science:** Positive swing (**≈ 1 450 S/t**) putting Electronics within two turns of completion; Great‑Merchant routes remain a reliable science source.  
        * **Culture/Tourism:** Culture has surged (**≈ 1 318 C/t**) keeping the Zulus competitive in the cultural race; tourism stays steady above 600 T/t.  
        * **Faith:** Faith generation rebounded after city‑state conversions, supporting future religious quests.  
        * **Happiness:** Now **≈ 54 %**, moving back into the **Happy** range; luxury trades and new **Hotel** have removed the combat penalty.  
        * **Military:** Slight reduction in unit count but overall strength remains solid; 50 % unit‑maintenance discount continues to protect gold.  
        * **Expansion:** One premium settlement spot (72, 33) on a new continent offers a long‑term economic windfall; a secondary mid‑quality site (11, 48) is viable for short‑term growth.  
        
        *Prepared by:* Economic Analyst – Shaka’s Macro‑Economy Desk  
        *Date:* Turn 423 (post‑event processing)
        
        ## Diplomacy Briefing
        **Diplomatic Brief – Turn 423**  
        *Leader: Shaka – The Zulus (Player 7)*  
        
        ---
        
        ### 1. Major Diplomatic Developments (since Turn 418)
        
        | Civilization / City‑State | Change Since 418 | Current Relationship & Status |
        |---------------------------|------------------|--------------------------------|
        | **India** | War continues; our war‑score is now **+10 %** (was +12 % at 418) and **war weariness 11 %** (up from 6 %). No new diplomatic actions. | **War** – **Denounced** each other. |
        | **Russia** | No new actions; still **Denounced** and under **World‑Congress sanctions** (no trades, deals, corp. franchises). | **Denounced** – **Sanctioned**. |
        | **Germany** | Peace treaty still in effect (expires in 2 turns). No new border opening or pact. | **Peace Treaty** (close). |
        | **Greece** | No change; open borders remain (distant). | **Open Borders**. |
        | **The Inca** | Defensive pact, open borders and friendship unchanged. | **Defensive Pact**, **Open Borders**, **Friendship** (neighbors). |
        | **Venice** | Open borders and friendship unchanged (neighbors). | **Open Borders**, **Friendship**. |
        | **City‑State – Oviedo** | Remains **Ally (protected)**; influence unchanged at **1,061**. | **Ally (protected)**. |
        | **City‑State – M'banza‑Kongo** | Still **Ally (protected)**; influence **346**. | **Ally (protected)**. |
        | **City‑State – Tyre** | Influence unchanged at **18**; now **Neutral (protected)** rather than Ally. | **Neutral (protected)**. |
        | **City‑State – Melbourne** | Influence unchanged at **181**; remains **Friend**. | **Friend**. |
        | **City‑State – Trowulan** | Influence unchanged at **205**; remains **Friend**. | **Friend**. |
        | **City‑State – Quebec City** | Influence unchanged at **73**; remains **Friend**. | **Friend**. |
        | **City‑State – Antwerp** | Influence unchanged at **381**; remains **Friend**. | **Friend**. |
        | **City‑State – Segou** | Influence unchanged at **97**; remains **Friend**. | **Friend**. |
        | **City‑State – Kathmandu** | Influence unchanged at **176**; remains **Friend (protected)**. | **Friend (protected)**. |
        | **City‑State – Vienna** | Influence unchanged at **92**; remains **Friend (protected)**. | **Friend (protected)**. |
        | **City‑State – Lutetia** | Influence unchanged at **28**; remains **Neutral (protected)**. | **Neutral (protected)**. |
        | **City‑State – Antananarivo** | Influence unchanged at **244**; remains **Friend (protected)**. | **Friend (protected)**. |
        | **City‑State – Shanghai** | Influence unchanged at **53**; remains **Friend**. | **Friend**. |
        | **City‑State – Zuunmod** | Open‑Door resolution forces influence to **40** (Friend). No other change. | **Friend (Open‑Door)**. |
        
        **Key points**
        
        * The war with India has **tightened** – war‑weariness up from 6 % to 11 %, and our war‑score slipped slightly, indicating a more contested front.  
        * No new diplomatic pacts, denouncements, or declarations of friendship have arisen since the last brief.  
        * Relationship with **Tyre** downgraded from Ally to Neutral (still protected) – no influence change, but the diplomatic status shift may affect future voting blocs.  
        * All other major civ relations remain as previously recorded.
        
        ---
        
        ### 2. World Congress Activity (voting in 9 turns)
        
        | Item | Status |
        |------|--------|
        | **Delegates (Zulus)** | **8** (≈ 18 % of total) – unchanged since 418. |
        | **Active Resolutions** | • Sanction: **Russia**  <br>• Sanction: **India**  <br>• **Global Peace Accords**  <br>• **Incan Sphere of Influence** – Kathmandu (available)  <br>• **Greek Sphere of Influence** – multiple city‑states (available)  <br>• **Zulu Sphere of Influence** – M'banza‑Kongo (available, our own)  <br>• **Travel Ban**  <br>• **Scholars In Residence**  <br>• **World Ideology: Freedom** |
        | **Proposals on the agenda** | 1. **Enact – Zulu Sphere of Influence: M'banza‑Kongo** (our own)  <br>2. **Repeal – Incan Sphere of Influence: Kathmandu** (sponsored by Greece)  <br>3. **Enact – United Nations** (sponsored by Greece)  <br>4. **Enact – World Ideology: Freedom** (sponsored by Greece) |
        | **Contender for highest delegate count** | **Greece** – still leads with **24** delegates. |
        | **Delegate distribution (major players)** | Greece 24 (54 %) | Inca 18 (38 %) | Germany 6 (13 %) | India 7 (15 %) | Russia 3 (6 %) | Venice 13 (31 %) | Zulus 8 (18 %) |
        
        **Implications**
        
        * Our **8 delegates** remain insufficient to pass resolutions alone; cooperation with either Greece’s dominant bloc or the Inca’s sizable bloc is still required.  
        * The **Zulu Sphere‑of‑Influence** proposal is the **only new legislative item** we have placed before the Congress; its passage would make our current ally M'banza‑Kongo a permanent ally.  
        * The **United Nations** proposal, if adopted, will eventually grant extra delegates and a free Great Diplomat – a potential long‑term boost once the Atomic Era is fully realized.  
        
        ---
        
        ### 3. City‑State Relationships, Influence & Quest Status
        
        | City‑State | Influence (Zulus) | Diplomatic Status | Active Quest(s) – Turns Remaining |
        |-----------|-------------------|-------------------|-----------------------------------|
        | **Oviedo** | 1,061 | Ally (protected) | • Spy mission vs. Gandhi (363 Inf, 882 Sci) – 19 t |
        | **M'banza‑Kongo** | 346 | Ally (protected) | • Archaeologist site (153 Inf, 435 Tour) – 22 t <br>• Demand tribute from Melbourne (122 Inf, 353 Gold) – 22 t |
        | **Tyre** | 18 | Neutral (protected) | • Spy mission vs. Alexander (381 Inf, 932 Sci) – 19 t <br>• Rifleman ≥ 60 XP (169 Inf, 652 Cult) – 29 t |
        | **Melbourne** | 181 | Friend | • Trade‑route quest (land/sea) – 22 t (187 Inf, 146 Food) |
        | **Trowulan** | 205 | Friend | • Spy mission vs. Alexander (381 Inf, 932 Sci) – 30 t |
        | **Quebec City** | 73 | Friend | • Deliver AA‑Gun ≥ 60 XP – 41 t (148 Inf, 416 Gold) |
        | **Antwerp** | 381 | Friend | • Trade‑route quest – 41 t (160 Inf, 132 Food) |
        | **Segou** | 97 | Friend | • Trade‑route quest – 7 t (163 Inf, 107 Food) |
        | **Kathmandu** | 176 | Friend (protected) | • Generate Great Diplomat – 36 t (135 Inf, 331 Cult) |
        | **Vienna** | 92 | Friend (protected) | • Generate Great Artist – 29 t (169 Inf, 652 Cult) |
        | **Lutetia** | 28 | Neutral (protected) | • Demand tribute from Shanghai – 45 t (100 Inf, 444 Gold) |
        | **Antananarivo** | 244 | Friend (protected) | — |
        | **Shanghai** | 53 | Friend | — |
        | **Zuunmod** | 40 (forced) | Friend (Open‑Door) | — |
        | **Other city‑states** (Melbourne, etc.) retain influence levels and quest timers as previously reported. |
        
        **Notable updates**
        
        * **Tyre** has shifted from Ally to Neutral (still protected).  
        * No influence changes for any city‑state since Turn 418.  
        * All quest timers have decreased by five turns; no quest has been completed or failed yet.
        
        ---
        
        ### 4. Religion Overview
        
        | Civilization | Dominant Religion | Recent Changes |
        |--------------|-------------------|----------------|
        | **The Zulus** | **Protestantism** (state religion) | Two additional cities (**Nongoma** and **Kwadukuza**) confirmed as Protestant (city‑conversion events at Turn 422). No missionary pressure from other civs. |
        | **Russia** | Mixed (Hinduism, Protestantism, Eastern Orthodoxy) | No new conversions. |
        | **India** | Hinduism | No change. |
        | **Greece** | Eastern Orthodoxy | No change. |
        | **The Inca** | Catholicism | No change. |
        | **Venice** | Buddhism | No change. |
        
        **Summary** – Protestantism is now present in **six** Zulu cities, further consolidating religious unity. Other civs show no religious activity affecting us.
        
        ---
        
        ### 5. Comparison to Turn 418 Brief
        
        | Category | Turn 418 | Turn 423 | Δ / New Information |
        |----------|----------|----------|---------------------|
        | **War status** | War with India (score +12 %, weariness 6 %). | War with India (score +10 %, weariness 11 %). | War weariness increased; slight dip in war score. |
        | **Allied city‑states** | Allies: Oviedo, M'banza‑Kongo, Tyre (protected). | Allies: Oviedo, M'banza‑Kongo (protected). Tyre downgraded to Neutral (protected). | Loss of Ally status with Tyre. |
        | **World‑Congress delegates** | 8 delegates. | 8 delegates (unchanged). | No change. |
        | **World‑Congress proposals** | 4 proposals (incl. Zulu Sphere‑of‑Influence). | Same 4 proposals; no new items. | No additional proposals. |
        | **City‑state influence** | Values listed above; all static. | Same influence values; all quests still active with reduced timers. | No influence shifts. |
        | **Religion** | Protestantism in four Zulu cities. | Protestantism now in six Zulu cities (Nongoma, Kwadukuza added). | Expanded religious uniformity. |
        | **Espionage** | Indian spy detected in Bulawayo (turn 413). | No new espionage events reported; existing spy activities persist. | No new intelligence wins or losses. |
        | **Trade** | Strong gold routes with Venice and Inca. | Trade routes unchanged; inbound gold from Venice remains high; Inca route to Kwadukuza continues. | No new routes opened. |
        | **Resources** | No notable changes. | No new strategic resources reported. | Static resource situation. |
        
        ---
        
        ### 6. Overall Diplomatic Landscape (Turn 423)
        
        * **Hostile front** – India remains the sole active war opponent, with rising war weariness. Russia stays hostile and sanctioned.  
        * **Stable allies** – The Inca (defensive pact, friendship), city‑state allies Oviedo and M'banza‑Kongo, plus a network of friendly city‑states providing diplomatic weight.  
        * **Potential diplomatic leverage** – Passage of the **Zulu Sphere‑of‑Influence** proposal would lock in M'banza‑Kongo as a permanent ally, enhancing our delegate count. Alignment with Greece’s bloc remains crucial for any World‑Congress outcome.  
        * **Religion** – Protestantism is now solidified across all Zulu cities; no external religious pressure is evident.  
        * **Espionage** – Indian counter‑intelligence has identified a Zulu spy in Bulawayo (see turn 413), but no new incursions have been recorded.  
        
        All information reflects the current game state; no strategic recommendations are provided per instructions.
        
        You, Shaka (leader of The Zulus, Player 7), are making strategic decisions after turn 423.
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
      
    - You are Shaka, leader of The Zulus (Player 7).
      
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
      - Name: The Zulus
      - Uniques:
        - Unique Unit: Impi, Replacing Tercio (Requires technology: Gunpowder)
        - Unique Unit: InDuna, Replacing Great General (Requires technology: None)
        - Unique Building: Ikanda, Replacing Barracks (Requires technology: Bronze Working)
        - Unique Building: Iziko, Replacing Amphitheater (Requires technology: Drama and Poetry)
        - Civilization Ability: -50% Gold maintenance for Melee and Gunpowder Units. All Units require 25% less Experience for Promotions. Your military ignores Alliance and Protection penalties and is 50% more effective at intimidating City-States.
      - Leader: Shaka
      - PlayerID: 7
      
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
      - Combined Arms: Allows you to build the Tank, a fast and deadly armor Unit.
        Completing it would unlock: Radar
      - Satellites: Allow you to build the Apollo Program, a project necessary to win a Science Victory.
        Completing it would unlock: The Internet, Lasers
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      - Telecommunications: Allows you to build the Interpretive Center, boosting all Landmarks in empire.
        Completing it would unlock: Robotics, The Internet
      
      ## Policies
      - Martial Spirit (Level 2 Tenet of Ideology Autocracy): Martial Spirit: +25% Combat Strength when attacking in melee for 50 turns, scaling with game speed. War Weariness reduced by 25%, and Razing Speed is doubled.
      - Total War (Level 2 Tenet of Ideology Autocracy): Total War: +25% Production when building Land Units. Warscore increases 25% more quickly, and it is 25% easier to bully City-States.
      - Third Alternative (Level 2 Tenet of Ideology Autocracy): Third Alternative: Quantity of Strategic Resources produced (including Paper) is increased by 100%. Reduces Unit Gold Maintenance costs by 25%.
      - Lightning Warfare (Level 2 Tenet of Ideology Autocracy): Lightning Warfare: +3 Movement for Great Generals. Gunpowder units gain +15% attack and ignore enemy ZOC; Armored units gain +15% attack and +1 Movement.
      - Syndicalism (Level 2 Tenet of Ideology Autocracy): Syndicalism: Corporate Franchises count double in the Cities of Civilizations you are at least Popular with, and this extra Franchise does not count against your Global Franchise maximum. Can establish 5 additional Franchises in foreign Cities. +2 Production from all Corporation Offices.
      - Lebensraum (Level 1 Tenet of Ideology Autocracy): Lebensraum: Receive 10 Culture and Golden Age Points when your borders expand, scaling with Era. Citadels may also be built in foreign territory adjacent to your borders. Retain tiles after razing Cities.
      - Mare Nostrum (Level 2 Tenet of Ideology Autocracy): Mare Nostrum: +1 Oil and Coal for every City-State Alliance. +2 Production and Culture to Atolls, Fishing Boats, and Offshore Oil Platforms. Naval Ranged Units gain the Mare Nostrum Promotion.
      - Police State (Level 2 Tenet of Ideology Autocracy): Police State: +3 Local Happiness from every Courthouse, and +10 City Security from Police Stations. +100% Production towards Courthouses and Police Stations.
      - Military-Industrial Complex (Level 1 Tenet of Ideology Autocracy): Military-Industrial Complex: -33% Gold cost of purchasing units. +3 Science from Defense Buildings, Citadels, Forts, and Unique Improvements.
      - Futurism (Level 1 Tenet of Ideology Autocracy): Futurism: Strengthens Tourism of Historic Events generated by the Palace. +2 Culture from Great Works. Earn 50 Tourism when you conquer a city for the first time, scaling with Era and city size.
      - New World Order (Level 1 Tenet of Ideology Autocracy): New World Order: -2 Unhappiness from and Distress in all Cities. Police Stations and Constabularies provide +3 Culture and +5 Production, and are constructed 100% more quickly.
      - Regimental System (Continuing Imperialism Branch):
        - * Earn Great Generals and Great Admirals 33% faster.
        - * Great Generals and Great Admirals gain the Regimental Traditions Promotion (+10% Leadership Combat Bonus and +1 Tile Radius).
        - * +2 additional copies of the unique Luxury Resources from expending Great Admirals for their Voyage of Discovery ability.
        - * Military Units can be upgraded in territory owned by Vassals and friendly City-States.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Iron Fist (Level 1 Tenet of Ideology Autocracy): Iron Fist: Vassals can no longer be liberated by other Civilizations or the World Congress, and capitulated vassals can no longer rebel. Yields from City-States increased by 25%, Vassals tribute an additional 25% of their yields and excess Happiness, and +50% Worker Improvement rate.
      - Free Thought (Continuing Rationalism Branch):
        - * -5 Unhappiness from Religious Unrest in all Cities.
        - * +25% Instant Yields from Great Scientists.
        - * Earn Great Scientists +33% faster.
      - Exchange Markets (Continuing Statecraft Branch):
        - * +1 Trade Route.
        - * +1 Happiness for every active Trade Route.
        - * +15% Tourism modifier for Trade Routes.
        - * Resources from City-States count towards Global Monopolies.
      - Civilizing Mission (Continuing Imperialism Branch):
        - * Retain all buildings from conquered Cities.
        - * Receive 75 Gold when you conquer a city, scaling with Era and City Population.
        - * +10% Production toward Buildings, with an additional +10% Production per Era difference between your current Era and the building's Era in all Puppeted Cities and Cities with a Courthouse.
      - Consulates (Continuing Statecraft Branch):
        - * +1 Delegate in the World Congress for every 8 City-States originally in the World.
        - * Completing a Trade Route to a City-State triggers (or strengthens an existing) Historic Event.
      - Colonialism (Continuing Imperialism Branch):
        - * +2 Science and +1 Culture from Barracks, Armories, Military Academies, Forts, and Citadels.
        - * Each unique Global Monopoly modifier is increased by an additional 10% if it's percentage-based, or +3 otherwise.
      - Militarism (Continuing Authority Branch):
        - * +1 Happiness and +2 Culture in Cities with at least 10 Strength.
        - * -15% Unit Maintenance.
        - * -50% Route Maintenance.
      - Mercantilism (Continuing Industry Branch):
        - * +3% Science and Culture from Markets, Caravansaries, Customs Houses, Banks, and Stock Exchanges.
        - * Cities earn +10 Science when they construct Buildings, scaling with Era.
      - Nobility (Continuing Fealty Branch):
        - * +1 Happiness and +2 Gold from Castles.
        - * +2 Gold from Armories.
        - * +100% Production towards Castles and Armories.
      - Free Trade (Continuing Industry Branch):
        - * Earn Great Merchants 50% faster.
        - * +5 Gold from International Trade Routes.
        - * -2 Unhappiness from Poverty in all Cities.
      - Refinement (Continuing Artistry Branch):
        - * +2 Culture from Great Works of Art.
        - * 1 Specialist in all cities does not produce Unhappiness from Urbanization.
        - * +1 Culture from Specialists.
      - Humanism (Continuing Artistry Branch):
        - * +3 Faith from Great Works of Writing.
        - * -25% Golden Age Points needed to trigger a Golden Age.
        - * +1 Happiness from all Guilds.
      - Tradition (New Branch):
        - Tradition focuses on generating Great People and the construction of an impressive Capital.
        - Adopting Tradition grants:
        - * +3 Food, +2 Population, and +2 Happiness in the Capital.
        - * +1 Culture in the Capital for every 2 Citizens.
        - Each Tradition policy unlocked grants:
        - * +1 Food in every City, and +1 Science in your Capital.
        - Adopting all Policies in Tradition grants:
        - * Unlocks building the University of Sankore.
        - * +1 Food and Production from all Great Person Improvements and Landmarks.
        - * Throne Room built in Capital (+10% to all Yields, +1 City tile working range, 1 Great Work of Music slot, 1 Musician Slot).
        - * Allows for the purchase of Great Engineers with Faith starting in the Industrial Era.
  - decisions:
    - #0:
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: Research Satellites next to unlock the Apollo Program, which is a mandatory prerequisite for the Spaceship Victory, aligning with our grand strategy.
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Free Thought (Continuing Rationalism Branch)
        - Rationale: Adopt Free Thought to accelerate Great Scientist generation by 33% and boost their instant yields, which is critical for driving our tech progress toward the Spaceship Victory.
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 4
        - Private: -80
        - Public: -80
        - Rationale: India is extremely close to a cultural victory and is our active war target. We must maintain maximum hostility and press our military advantage to capture their cities and permanently halt their cultural threat.
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: We share the Autocracy ideology (+999 modifier). A friendly stance will help defuse Germany's hostility, prevent them from attacking us when the peace treaty expires in 2 turns, and keep our focus entirely on crushing India.
        - Public: 40
        - TargetID: 6
        - Private: 40
    - #4:
      - toolName: set-persona
      - args:
        - Loyalty: 9
        - WarBias: 9
        - Rationale: Maintain high boldness and war bias to aggressively pursue the conflict against India, while increasing loyalty to 9 to preserve and honor our defensive alliance with the hard-pressed Inca.
        - Boldness: 9
    - #5:
      - toolName: keep-status-quo
      - rationale: The current strategic weights are highly optimized for our Spaceship victory path, with maximum focus on science, production, and mobilization, which perfectly supports our simultaneous space race and critical defensive/offensive military operations.
  - tokens:
    - inputTokens: 25656
    - reasoningTokens: 7344
    - outputTokens: 334
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Situation**
            
            My focus is on assessing our current standing as the Zulu, turn 423. I'm reviewing our civilization's strengths and player ID to inform our next strategic moves.
            
            **Evaluating Victory Conditions**
            
            My attention is now on our victory prospects. Given India's immense cultural dominance and Russia's military strength, I'm re-evaluating our path to victory. The spaceship goal remains, but I'm also assessing potential shifts given competitor progress.
            
            **Disrupting Indian Victory**
            
            I'm now focused on preventing India's imminent Cultural Victory. Despite their multi-front war, they're on the cusp of winning. Given our current war, I'm prioritizing intensifying our offensive to disrupt their progress and thwart their victory condition.
            
            **Adapting Autocracy Policies**
            
            I'm evaluating available Autocracy tenets to counter India. Given their war-torn state and our focus on disruption, policies like Martial Spirit or Total War seem most advantageous. I'm also considering how their alliances with Germany and Russia might influence our ideological choices and battlefield maneuvers.
            
            **Choosing Next Policy**
            
            I am now deciding on our next policy. While Autocracy offers military benefits, Rationalism's "Free Thought" or "Rights of Man" seem more aligned with our Spaceship victory goal, especially with our current Golden Age and the need for science.
            
            **Revising Strategy Towards Science**
            
            I'm reconsidering our policy choices. While the current war presents opportunities for easier bullying of City-States and benefits from Autocracy tenets like "Lightning Warfare" or "Military-Industrial Complex," I'm prioritizing our long-term Spaceship victory. Given our strong science generation, completing the Rationalism tree with "Free Thought" for its boost to Great Scientists and instant yields seems more aligned with our grand strategy.
            
            **Prioritizing Technology Development**
            
            I'm now re-evaluating our technology path. While the Autocracy tree offers wartime advantages, the immediate need is to accelerate our Spaceship victory. Thus, I'm focusing on Rationalism, specifically aiming for "Free Thought" to significantly boost Great Scientist generation and expedite our research, especially given Russia and the Inca are slightly ahead technologically. Electronics is almost complete, and I'm confirming "Satellites" is our next target.
            
            **Securing Satellite Research**
            
            I'm locking in "Satellites" as our next research target. This is crucial for the Apollo Program and our Spaceship victory goal, especially since Russia and the Inca are slightly ahead. I'm also reviewing diplomatic relations, noting our hostile stance with India and Russia, and Germany's denunciation and alliance with India and Russia.
            
            **Improving Diplomatic Ties**
            
            I'm now evaluating our diplomatic standing, particularly with Germany, who has denounced us. I'm exploring options to mend this relationship, considering their Autocracy alignment, even as we remain at war with India and hostile to Russia. My aim is to secure our position and open potential avenues for future cooperation, perhaps utilizing tools like `set-relationship` if feasible.
            
            **Mending Relations with Germany**
            
            I'm now assessing our diplomatic ties, specifically with Germany, who has denounced us. Given their Autocracy stance, I believe mending this relationship is a priority to avoid a multi-front war. I will explore options to improve our standing with them.
            
            **Continuing War Against India**
            
            I'm solidifying our aggressive stance towards India. My analysis confirms our substantial military superiority and their imminent cultural victory. I intend to exploit this advantage by capturing key cities and preventing their win condition.
            
            **Assessing Enemy Engagements**
            
            I'm now reviewing our rivals' current conflicts. India's imminent cultural win is our primary concern, but I note Russia and Germany are heavily engaged against our ally, the Inca. This distraction is advantageous, allowing me to focus military pressure on India without fear of a Russian or German counter-attack.
            
            **Analyzing Current Conflicts**
            
            My current focus is on the ongoing conflicts involving the Inca, Russia, and Germany. I'm assessing the implications of these engagements for our defensive pact and potential future threats, especially considering Russia's immense military power and our ongoing war with India.
            
            **Adjusting Persona Parameters**
            
            I am now adjusting my internal parameters. Specifically, I'm increasing Boldness and WarBias to 9 to effectively prosecute the war against India, while also raising Loyalty to 9 to ensure unwavering support for the Inca, who are currently facing considerable pressure. This refinement aims to solidify my role as a bold conqueror and steadfast ally.
            
            **Revising Strategic Synergies**
            
            I'm reconsidering the interplay between our grand strategy and Zulu uniques. Despite the apparent conflict between Spaceship victory's science focus and our current extensive warfare, I realize our strong production, science, and mobilization, coupled with Zulu military advantages like Impi and InDuna, create a potent hybrid approach. This synergy allows us to pursue the spaceship while effectively conquering and defending.
            
            **Evaluating Expansion Opportunity**
            
            My thoughts are now on expansion versus consolidation. While a high-quality settlement site exists, I'm weighing the benefits of a tenth city against the late-game costs and the strength of our existing nine developed cities, especially given our optimized science and military flavors.
            
            **Prioritizing Happiness and Diplomacy**
            
            I'm reviewing our current state, noting our improved Happiness and high Culture per turn, which aligns with our non-cultural victory focus. My immediate priority is our World Congress proposal and considering diplomatic modifiers with India, especially regarding our ongoing war and potential peace terms.
            
            **Improving Relations with Germany**
            
            My focus has shifted to our relationship with Germany. Despite their recent denouncement, our shared Autocracy ideology offers a massive diplomatic modifier. I'm exploring how to leverage this to mend ties and potentially avoid a wider conflict, even as the war with India continues.
            
            **Mending Relations with Germany**
            
            My current focus is on improving relations with Germany. Despite their denouncement, our shared Autocracy ideology provides a strong modifier. I am exploring how to leverage this, potentially through positive actions in the World Congress and by altering relationship settings, to secure peace and perhaps open borders, even as the war with India persists.
            
            **Leveraging Ideological Synergies**
            
            I'm leveraging our shared Autocracy ideology with Germany. This offers a substantial diplomatic modifier, allowing me to improve our relationship and secure our flank, freeing up focus for the India conflict. I'm also now reassessing my stance on Russia, noting their Order ideology versus our Autocracy, and their significant military strength and score lead, which presents a new strategic consideration.
            
            **Analyzing Ideological Conflicts**
            
            I'm currently dissecting the ideological clashes impacting our diplomatic landscape. The significant rift with Russia, stemming from our opposing Autocracy and Order ideologies, solidifies them as a permanent adversary. I'm also noting Greece's dominant World Congress position and their sponsorship of Freedom as World Ideology, a direct threat to our Autocracy.
            
            **Opposing World Ideology**
            
            I must vote against "World Ideology: Freedom" in the World Congress. I'll rally Autocracy allies like Inca and Germany to oppose Greece's sponsored proposal and maintain our current ideological standing.
            
            **Refining Strategic Priorities**
            
            I am now confirming our research direction, locking in "Satellites" as the next technology. This critical step enables the Apollo Program, directly advancing our Spaceship Victory goal. My current thinking is to maintain our highly optimized strategic weights, reflecting maximum focus on science, production, and mobilization to support our dual pursuit of the spaceship and ongoing military endeavors.
            
            **Updating Policy and Tech**
            
            I'm confirming our next technology choice is "Satellites" to expedite the Spaceship Victory. My focus is also on adopting the policy "Free Thought (Continuing Rationalism Branch)" to boost Great Scientist generation and instant yields, aligning with our science-heavy strategy.
            
            **Crushing India and Solidifying Alliances**
            
            I'm confirming our strategy to crush India militarily to prevent their cultural victory, setting relationships with Germany to friendly due to our shared Autocracy, and enhancing my persona parameters for boldness and war. My current focus is on maintaining our optimized strategic weights for spaceship victory while aggressively pursuing this war and ensuring our alliance with the Inca remains solid.
            
            **Confirming Final Research Selection**
            
            I'm confirming "Satellites" as the definitive next technology, crucial for Apollo and our Spaceship Victory. I've also finalized my strategic parameters to prioritize science, production, and mobilization, ensuring we can execute both our spaceship goal and ongoing warfare effectively.
            
            **Refining Diplomatic and Technological Focus**
            
            I've confirmed "Satellites" as our next technological pursuit, vital for the Apollo Program and Spaceship Victory. Concurrently, I'm adopting "Free Thought" to accelerate Great Scientist generation. I'm intensifying hostilities with India to halt their cultural win, while fostering friendly relations with Germany, leveraging our shared Autocracy.
            
            **Balancing Warfare and Ethics**
            
            I'm reaffirming my commitment to aggressive warfare against India and bolstering our alliance with the Inca through increased Boldness, WarBias, and Loyalty. Crucially, I'm maintaining status quo on nuclear capabilities, reflecting a balanced approach that prioritizes our objectives without resorting to indiscriminate destruction.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: iGghDkTr4WGIO1cc
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: Research Satellites next to unlock the Apollo Program, which is a mandatory prerequisite for the Spaceship Victory, aligning with our grand strategy.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1+5FWooD0Yup064kiBs2chx7H+UQj3FtjWqNo8WybKuwCJHZNgDVHOUbIf4a8h2WGnKWrOhSZBBM0aibVGvnn+ocM5IBvyhaNBPN2dSq0gQRxKX7roz5+BIs8XzNVa/k5BcMBtfQ68DrvjkSgRPlt7e8Ds12BaaQnmMFoSmUDAqzC7d2IRDdYarU6Tmchqb+QeRgdvgeETvDjX1vd4DTSWRohn02oHey/ZJjRRh5L9M7QccHzIhm1BS87ChzKZDEavZFyOVveUtiiRz2gAq9ftPpOnYVwB9Cr9Y3jLDFPU+VThbdO3rFWKjl/V5Un/eZUCUbCTt9SnOtO/QBoexzNocApXYUjNUCrQ4aBgx6rGuFK8hQTpGB6FfaAEJ50ns1MIwjyvVpDCkaVuIvwUMr/ORfC55517E4jbELomrbGCcoNMmmPVRXSvlVbZdzwWGrDIfMZIxDtB0KKgiKyf7FwaLw3hUb+xOWURLIRtIYfpA/C78KeqM/z+akJMtTpbTKnLaPzDCtAEUo2RWQSomNQl3HpO0Kf2GLFD2SL/ZKXY1z+cbPIMEsY9WtG25iyFYlfKDg6+W6MomuclWF1ADV+IqldOKp8CHPPXsMwBskph4otGy/RopAyMZ7YvdoMHbag/rLVwSSPuM8oqrOjaTnojmSVpZYUAW+NQmsduxD8ONEKyJH/bfYtp2QLuuHCIogb5ocFtqlV1u98NRJG348RhHqXZLD0huwrFhVfTdFKs1P8Y4mf5fwkJo7lhHLozmbrauPHBAhvgzrgH8kQdQeeUBdds6xbknd06atkouYV1vjhG0r/8rFEAqvptkVVwmmNb52dx42IxnmJh4raLCGj8/DeVgFTHLXSjMKeLlakbZ1HnaKiZ7CWrXJKEZJqQhcSX6/ImWvv7ke9sOOdKchduxIENwCN2A562/jj0EI58Nj1wnj/Rtvc53axVJO4GQT9cZ/4UC50j5L8kWOzF3K5tMOQfsvk6qUZetV+B40uMTcsWDK9iBhQRYcslu1o49DBzcTVq2SuV2MV6Qt66659E1+8+rUiAtspA9PTTJeFve8MElrRCy+Qi2wlVtO843G9hB3O/XY4dplJ3XE9wiw781oNkftNw+BKUrINlWpnwFFX5XfDNgheEbKcciE7RMNeFF16KQBi3zlgK6PoEv6kQJ5HxwuImJ/772DcvzylRU4oQrEtWQk+WFHl7sSC0c6AEkk6eplguZLA6qghEYMy8T9DSwi1Ct03LzZdTsoOku+B9cqJIlBL4K4P9ESbAqkbkl+2bz/6ONaFyJWy/6vIsyLB3hQEUD7N3wKHAXAO4y4tNiH5GKIIDPskxBpjxkZvE4pTXMD2zv1PYz1Wsh4C+5AJyvFa2UBfeHktLqglGigvhm3Fvu918YPzOfS1WMevQ+UoSNonfAnOG7LkdCofM0OyYDkZvD2gI1nT+T7pWPxiRE/jvkEm2jp8cFdoQbAlrjKbGQ/hB127Gq9cbh//poZItaMRdLa6Mn7sFe89dGpkImobyQongNqjtYdn8EHRjwlUpgjn97dYx7H/dhwGmoQWqSylruMyBn4EIlq9VWZOuH2cIrdZBGwJ9jvGdhgxrkkya2TRwTUyxavZxF+CNXA726Y3pp9hFWF4xO0R0D/G7QxDk3q3g63RUrSH/DSY+vvrDfO1TTtpRD22yrGREwlyvMVg4yEHpOoJiqmqR2sBU+frOfA4j7E3UmflsElPHCi7uYx9a/uzgE9of6bktcw5ZJCVDppbvRHB7Y17MBTiZPnp7SAnPe936ijnZVFB+X3lIIRS8vCBkbNh4JUocr/tIj2Lle9n8EqTBHsEYeYVTOVHTzxDOWGKBQA61fbarygO3xfIWXmKs5VtK982yohOwwjZyPow86ncsUB2MIGdsxaNWz9OJAC4JblPNt8DUezL3grxzdFG9QOCuxBOvZgw1W6oHVba824QXaIDODppLygfONYIE5CKLGEamby9NZ2B/D7eiCLVR1mStwVO4bhCz35UX0Lhk6Q6jun0ocJvy0dd5peCf6vhbRcX1UaAx9olC9Vi+WvOTyGPvvHi8nuBHvHdZ7XFfwpXdWZVSQmErYM7C8TDUNhCTCpes4ZS8xIOjozTFqJnAR/S1qWellFbKcn6Bgq5YXjcOFtfJRKWFId3NOD6Q2n0WqPwO+aDQR/MgmyL9tusrmTvcJJf8tyFQYcvFPryJ5zUvhZd3rm0vorMelB+vIxM79NclwT6wVzgLgtPw30vPjEvK/A/uZuUYxgpn2jtfqaYDZ9wrHt6ISkKDklVQQUOQWFtBfPtnYi1IkEcjev7AABR4muClPUvF9RFm5BCy4K4qHRo8rubOjJxkUdU3yY4RMLPtYUGxFFqOXPI7vqs3jJ+H2gz0YY3HBL1F1NZchSGPFtxFUMXenFS8IWgvehwyaQnWj/cF7UVp00MyUTNPYJGd+H7O27q/2aH5Dvp7RvXYHE1CbTXW2uvz6qSiCkesSnQasklRuLIHGp/aG/rfOyBxFsD3BniSSVFJNGMv0UUxA5IPZEsITNIdBGR43UgyX6TAEVzDfYrHQjdtFO4pD9Lcs687xA29D3TfHSpDi5EbqTH0UiNLqaiwGnLMqkTj6dCnTMcfTsDWvoMBzmSJAEM/YAGG1uWPGzzsrPLloMSoce/7YSplLTapDaZugfzFWEmGdIzplvlKESqwBoefJrA58f2tn2S1nRxyY2kGlLr7EXYaxAgCzeFanmACKIG8rDqBFf5Y//bmD/GQ87IdVZztxREVeccC6pMTheIDnZ2lg0PlYBU7tgGExCH9TMZcJl69lGVcYWyNMDxTVN/fqiylg7ryM2e6h9IKR/9NgViQgI6BhngEb6AzdID0UPHOB/ebaiQVMcwYXHlbthyo3xC6rblLU03vmS0mfk/7lhbAMmA+wA6qY8dvw2eKw6y0yKn5ElJdMIyU8zomcZ6JBGWlf48c7+KyLsevlseiwPfvdNHH9IVLmY8lKL21R6UubP5chdFE+BM1ISg5w8UIjRWUXO0pI/8dCbQxMym34GAq04I+PaLF48vFmy70D7DRRgd1DwcGw4siOkbEVbjM1QZqbhIlGg0N1soWmmsGs/7DjVQgCFv4IAW2ttT/lQ3HxOeQtVhCbl5DHNn7Zm6/OTZGiKcCBbo0DjkOgIR6EHn7z36qn4YFRIGX0Rn4+yizODj60NbWKi1EGBqdepk/qJmrVvUE3zA+wM8erz6RJ0wHmUp43f6jpN57Ci2h5N5yIbQWFIpii/vT2dbNiHUx04vV2xKtjT94yuqf5Imoh6rM0PhsGuLSKcu9GaNS5M9AzkPVqivJF5pi1PiP/utS2SVaC/Vxn5nOf51E0zdsdv7Lwt25o8iTcDNGepA3Ks/EKZj65EzuoQoycfE4rzp132dyE8Z0NFWyxpUOa5GD4s9ol0FqvRFQEkbhO1zWdS7XsyVQ8LBq1X7Ax/7a4IL7Fmc1ISoa4VROhal7zhd+hyuPB0BJorhSpouWSwRHpmqxINu5RbcKeKdsJfglk7FGBR3RJsgTYKEivtR9qPUWbcuvpNxEtPOFG8aoG41bwPkOK6WwTXVeuYDE5OrEKOiIchvkLcX+BO66M9cBlTR3RxtxVMd7/bNSk0nDJRqEPxk+kbcAKQ7pJkE7Z9PUZ8N2RxcI19P4adKaVex4nYP/ZlEtXBRGkeDlS/ZamrGxHe6m2VzTlPGeFCjhvHfrmuJRPFOFSshoxcznIcPBBEqEYFvl60ms3VJFJ7/NqUYh5q+cYT95UxIRYh6tcglEUBaY5bDmCV/tOsnlbGYDWKu64qsBFNPavs40z91nA099aDXuqozQ/yt47OnGxYOz3UXqljm+SZIRRLrdrz9g9aiKgL+bzXi8U6t6zx4lpbGYNoAQLlvKS+ACjLyHw+cSGNcA/02vpM0eAiir02RzOQq0hUGba95t6oO9UOaaeLvjhKeB6tOAo44rdOk3o2fZB8W2oWm4leOdhXgQbmnTLF6JnPlWElKq521tOZ6fwdNz57MwryWilVPNhsljtmMIUeXExKYUKNq9eY3hYnGSu+UiGZE8xK7T6BQ6MUZEJkd8d8Tzc46u+lEjEZqyScc1EOxmMNY9x7Ri69OII892p2ZsnrmMfZmUdmz19QyU/9AqPR5xdnOT4lX1l2we+6hjInBorvnyO2VvtTXsrO4hBBVcP93ONPKAfI/w1M9f7qKooDU8pWprLzJF8OVuyCNzIhqSp1bOH7hKtvjYS4U5cGNp+ykzKffuBOp8cy5ZJEawve9PHN+/Kt6JFw8XRdCrp/oxNmCDMYeUfmv+5ailt5MStnDpBs2EJeSY+0q83zWppCmYi4RcYKH4dSIEuY+ji4/780q+U6PIsALrPW6tDWkLvQi53aQ1NPkbHsoLscB9QXD/4fcWd2M/uUgtJy+dpnk1ZL1CTQrlPYfilM25nephGYtAe1UKE7fLss9WMNH66erEr7Bl+UoMQfP8gWOyoDfn9JnU4QI3+17ArxI2B5Oqib+2rj6O8w0pit4RtqE8GUvl+xFuzfQZinarBL6+rslXgRnqCPSQHjT4ulP3EcndUbjssPkZo94ouy45IhR0FdrIOsRofeikZcbOxSfgkpcRZUQ2O6r3Bb2ecAmsVNLJ+IJb/R47j7593YQN1Tm9M1ZnmmCpccQh+Ix441zHiaLjk508uA5p05oKWGdbyOAQ5MXhvIQnZ/MYL8wuxN4Ne3MKXrCC6QCI8/ww1WmX9NW/XXY5Ou3p2zMj9rHicFoHNL1DYcRUu27D2HOVSsf2l8zU0SN+R2+02ispmdHeim59t/7C6hqxq90ELVA6aUIoD23qMXh+Z5u+c/fbuDM1tI9LA65sQLx/Cz+WymzUBI3orsCT+oLSuT7AQHOpdF6t6G9afB2sP6Ki7z8WKov8jiUANH5h44gxFCOsAytb3paQoMw2jnSVAnpbNh1ZIIeUMC78hoz3ZU6HfglfBebfrflLLN4HlJ1JoezppGEYXfjsTKR4Wr4LjLJmyekncnW9Nv0MeXF6GlLjTYIv0vHC/mgZBNi1D2yPipzzJ5p3f4dAwfKN2aZ/j8268MYOcKiVdI3uOUtccP3PjZWVkwfREaZEM/3iSaxNgry4E5P9nO34+yUzN3DNOOCrCaWsjOac9uvquQZaaMs64ieNDrIV3kMxT37YYFv2QVMRxVlMbu99eaBtTPIRm5ntjv+j2D3CDV5DoATPgklegObzyaVnocMPNbv/VRgot0wEbYTx+lmlIlUB1QThAgcyEa7RacmK0vgGQtLHkrX9x3zfsmuKacMGCy+cbHGmWkkYsgc1ntRnFCQfIvrUOHu34BZiUI5BHjGaTl+rJfE7SWoC8TqnuuXfXBwvs5/Yj6vEoPqGZFn0O7DtVutL/hEGblhIlR2VI2VErtBlvVU5YcuTvx7QZYSrtKD/Fc38IYdq510rtzOWCfHXz/2bpmDIRegliM7Rgvmd4n4sLnKAIQZhWta5nu6+ILuGbS+I4oldFCr5nteSGJDzTlU9EB6pnHsd5/mP4FL7eEmUclQw4oc7rLEEjZRS3oPS/fbIgxeMS9Me2vURPrNA5aLnHIFu3qUBN+0tQrzAfTzYEJ8lGoFlEWu8dH68aY5Y0vaHG1sWq/mi1oArKw9aPgzcw/hFeCnITuURrsFbh5yWrhh4KpUobvz7TrGJ2JeinlKiB35UgjjU0ynbiazYKOZRpOTfvfL6mOk2+BpB9SyGfqQTu+Z4XlwZjGon2wbTx4vpRXj1jVy2WAM3ytlGskeq4K9AtWz3qfHhiq3Qnn+HwHgUrtMW/pwSjf9P7uZdzTOsBEKiomnSWbhkFl1nxl2kykF5/VWU/rxzcGBqg2E9XEwEOIpSnosOsrPBMw9qfZuYaoytW6mv0V+qkshbRMhVqIUVGlSmQBJFNOiYL4GP8dlsjpKl7dt4pdMDCmh5Br0P4PVQuBnmnZMxmVrqaSD/HuffFwg86+7UYKq/RWL9+Fqgj6XIfIzKJTpQDlUx6Ghwga5ibxrs6KnELR4qsWfIVnyyssgIxUO028dJLLc7WU62sjk1zGVqzr1dW3+D452juhLVWOo0iuObT9IRvGLz8Pzm2mkhKPQYYUg96uLBDyrkcYGNhOYx5zR9fwjv1tme0eXm6POUAfpae+pulBSCPoP9w9fOc62i/ALnpj7KQ0DZctHGVO9qMT49umcPSg1l5vVfp/3kzVdezgKIOa2Gw8KXo1MJcgfWP8WAft/3eJk0UrMpP4ZGJRMvSzvsp2Nr25jUKvHs991B48W71fnZikt+NRn7iNJ5Na+CzdmxRChI6brCAMvKqAcZJQ66xS1kDuNv9vJNlrhwrJWNSezzeNhDyVD+Jfi+28ddKw8AQys8aoUNaK3Q2wUoRqk5NjOae1l4nX9UHvJxUMjUuKShHi3LiS820EN1J08heJ/OR9NbP+LycnaayYCVcxKkN7kt8QTwQJFusQ9b8/+otFCQtDuHAmtDvG27C2DWrzIkKHk0ucn8T4osHd97CCWbsZW3Fzc+EyMU0LT01oStq+FeBLfHo2EE9xvKSMzAnfbt+TplWF+aZBpZjnuOrKy4RUzR3UZkNcrYk0UmZ+fKnLIBr9T+uKNNiPUDiUghZWRhSMKj+m5HEWrrlc4cFuc74J6jqT3t2LoH2UU/h0Z9s9QE1F6paG1BDkB/8quuzsX6nWbMJVJdbaoonuRUIPLYuY1okLMRDHtPpbG+ln+zYaUs7q8gLR+mIzupcakUs8OlGUOhX8pn16aCs6Hx5q3LuVPONNM0g7b0tkEpfsW44qT1DP1uitZWUMdhXrm9hTBMncqFRgcvYaGX1lCiwQRCWCB3kLsmzrAWMMuUR2AjPCclNWVtargqiGEjr6AJQpeNifDpvx84Nw8uWZC5T+Umfv8uRfuYdBtWTGfckWAOMTIljDJ4ghGJTE5f95cVdY7Jf/IGQT12+5pXcQy0Zh4mBi+PxKLGHlzxflDgMeAirGyrZvaSe+3p0geqnsegzfiGjdySG6L+8GwMHiQCojk9ozMLXuwqfH4hvqjGlnomzun9NCgArelwmwbjaZD0MJrQw0Si7jchZmfJYD3wx1C7XNaIAyDmUwQgdOUQOuc692nwAzirP/JvXg8+2TEZ171DhqhQu6GY9BJ/0jXrrswF/MhzqL8nUAqzqggxTlnaWdw4p//lvM8myV103kvu5S6bDjKmkjvuGFMlvdfGT6/SBghQPd+vNTKvcJ5ckxDyiK1PeGhIyddyukVHeVJ2n7ymuxXfrlkZIVFNvCQwKGQpJ5xBqOPFWbPl7b3bv7zUNiuoGfgPNNrlCoM7CBhR400GaFEVLK8/bg5mwrNDJyAL+KbvA1J1eCsho114CGyiG4wS0XNbRo0V3NlaWGBKXcNfT4v1L+bYgSXYoSq2PhOO+sK5Lh09i3+06o4X8go9lqIP/XLHdQSXPe2tPJm4q8FE0KW8Ln7AAEr2U2oeRL9iMhAQobuQ6JivzZDcabBXmbI8bbHoLPCx0Xxpa0zezSVJ8LYJy/4jlVxKi6FAIXTRWpUT0M4xu56u7s9ghZHlyw6qwHUPRuOhfUKEXp3GpEWMCTyJ0EaTZYuaLDpI1u4tgErmCVV58FUF0t5s6eI3YXtHTLyCFWecPmLh/ILbpQeLnkfcVXpBSH2brzt4IXh1+INif4g1iYFfs9bzqLZBSusqz5ATqjAF3J3Sn7tExCeTG0vmjYjYfxvnDrVC9hzHtpUpABr4YerdCQyo1QHTa8LOq0ppnkBuVU39nyr0Xptpgr2O/at93htrr24DGM1F01XmBsVgTG38kRquz2NzA/uSoe5ULDFNLxhjKE2LEKLg+Ce2n/E4lB1YRzzpSaz8exAXfgmaxg39QK1Mnzmelz+CWXRm9n+iMGsjgOi6569fwTNQMMJXwxHRs3FoTvnIWuD8x4SuX0zKHI/DG6eFGD7aBGBhFsdBFElLvryHS5g9AUtWKy/dRnf46YePX2igz68eY3zC/h20lLobHBvi3uXCoL9ymFaf21JiOlOLqSG6ZT4C0TbBLBx4vFBkfrktNvU6C5dlCrr1aboRtAr30RhBICAOw3RiAy7QoARIsrhAPqoiJJoRb3fImyMc+tHB/0XqrsUKiT3a2UMVRe1M1xrDNm4KmRaipxgfsBlw0qiA/KGwJQ6FKO7t7WliJ3mpCVzKEB6ozfeuTPPNQPw5QwwXHmVIK7m89sXVMbc9UNiN+EG0o2+i3t+ulqTF/kXfUSRabBOTPIKBa9U/W3zvCuLU5VzwKDwEV45/jZHMafOmRa1loIUzQEV4+tq2sDjRPchjAnYdP/VZwFvon2ya6UAYibS9fytRVw/vNYCytWEKNs4bW9byFI0Un2J18khxQUakCNorliJ42/mr0MZo/DSxAub21NCKo2MHiBwySs85Z/UwGGQeam0Zwl+cBtVZMFFSLCxeOdOOBjpx4CnUtiegE12iHUj/H74Ctgs8/MgVaQK4VcvbBQVZZW40H/NTnntPe3o6V3tmxuaM0JwG4Imbrf8Q9GF5x8JluVwUd5H3Q7XYr+IfOg9en/A7i/Qy65InhtHI/aB+QNB4TEUAEp/TGK/7e6/8x3ei/1AeEc+mfT4rrL/PDRc7+qkqR5wwdKOnQ2AQ8x0FXY/9sUfjN4yWVTe+5DrJhcL1H41Fw51H5nCCw3qUw6II/fqTjykAXY/nkSsPT5WPgeoaQpRKVL+kPwJSP0clMl3VbQ5c8F8ouPadzPoJdHDLv32Tr+dG9iQQxIW6c9bRjCpgPVxnz8KSqF55lEZE5ZriZgnQTT5knNlqaQ/omaBuV4+DeUyWyUuX8HFOrYFPFYOnzdr1N0Xw4H7q252Ut+w+0qlV5RXmkqKTxsnWoPzUyVElCwSmsZrbqDm0/BreHUF4K4xpF+e+2Qs6U73asYWLSltMxi0LsVxezMDUCCvSTN2fVEiEuu3Fg5YygYAkTho7nBalHk4U2CLoiSoSW638Q0piMUMKLLsk3p0n/l7a2PpxloXlZm2hVcwFgF3jLS7bt/2m0M4msbMs1m0LDkwZDf51CZkQYKOcyDw5HmjmGnNNMvpuH3zvEu1BjW20R98bSTkakhxpUSbNLFcUXShdw/hn7gWoyjbSaBdGbzobGbpSOzhEd/7UhTZHPWtgD7Y5FFljvNaFKQpN5Bs31a0bU54mPjSduB6bN/NGhpFqqwBNCJuN5X+rSvmghE//SCm4Q1imozDRJLHcUIgwC4BaPaEs22XNoggZ/GTckdf+ae5BhbI7H4EEUVhpZDHy6gLEfiCHkg49c5OXP5y0QlmNOPUiw4GTJDHCCQCaRgUS5rrYNRcdaoZpkc0Bod/6dF+aF9zZHsZNMvEmZzdKqiBD2kDim3EzzTL00uFOXsf6nPnToBpZ4MXmPRxJnQRRMK3wyhklpq8QvGmp5dHkJn2iaw1P4T/TBKbfUbsPKPvdpI22H40Fn5wDmuE+mzErczw9llK/W0NwwGHv3GGu60F2+gMnxKjCEcCdr3Osbedjd7OnK/4hP7DU2up64WsQ1IeiRYUnhFAbossTiteezjp7izt6PSE2O76buNvkVTz+IX+vNRZCytuhrY9S1qoK7oI6RBlP9gY67C5aEvw3NHrPWV9WQkfLfKrEswixdqkFB3E2jb2rRYh1vqTfrtqMpoznwAF+A/bXJ5np4cZSh68lXRDqs6AlPwUI1M6J/NDwrk1dVVbyUIvR+beBUKooXG1ex0kM+0bGR9ocl8U6rc3u7PLQiFcfkbnOLAeFxBx0zwsSU7GLN+PmacP5iXKvYBBuS2L6PMDestFjclsTN4vnkk8kVswL/1zr5mrrWDdTasPSnuKWnzHSbgdIGu3550esCZ57VZWaXhOXmcpzMSeNFyq8nwNGfRrd7M1eWJ0CCMi9hRrIuoSpDy78d2bm/f1pGjUtc9K7sfvXS4soXBq0+g89LW/N4LgRXtJSBO8qiwpB8OGwKbXy8quTz2QXv/Hlk2D7+AiWGzJoxprY42lmu1cJMeLA0Q4okK3m+p6tlMSukuk8lPIw85lByxBnQhVlXBlBgGsW8wZ4QNnSlSsENlvyWfXezuhrphwc5HCeHw9PUcR3zzHgPlQE2Y1aITRtqsD49hun89vtWF5eS3oyKbU8cd/6M2Q8KaZZ+NQeFimWv+Q7DjmOA+RUKrOu2YtmGlLMFGeGkJBqsCWPoXfiRpbpZaNfKm9RpSD/tN4Qy+6IIlsSobZvYL7tDjv3bah5cvcqExnt/sHrcP1XLbyH1E8iQFfZeav5HruCbfQ8wq1xHHrxkoSwtLIsWrHAHJM277IL9c3WQR7Y4Xy1jQF7U7YJ8VocEkzTZsiqZVVZeSHOp+sqDY1HNzjOlY+aYrarCJMMQGw3e31a31axl781gbLH+LFyo7vlCOmgojLqHo/+UVQUPwIpejFHL3uCQumO0u8yBZm/aoYJ+dFHZkHijR2EVkugrT2y+UBB5LOB25N4xd+ArToKKsMYx33W8XT1Kl+WFwo7SrLAbmXYmGs1mzI/EOIfLsjK++8OwnMLGR3b1WNub4/9p9WLI+diUikgl0dKEV1la6l703lwW9jFw7Ut5Ce7eOSdG3Iu9HbQFA2dFXLFWwB30N+l4Ki0LH2iQ0l58XSLfSsokaSlBN5DeLqpd0A/q+9xn8O/mqWj3nqCv8hyXm9qVPBy+FhZlOJhzi9E3NKqIlyaYCmHueE7r+sHDu2eBHqWJRrywKCl2R0PckBYliXSFIF9aYjqdV19u7KwKu1r0imf4hrqyAttnn69yt7XaVYBDur9cbR44UaX+aAff80TWNbKifq1P/psPb4Ue9F5VLFhVEKve9l9aqBXHTd1xVIdohux+Q0SoDaOTjhobsIrx+8fpsv3S6weDLZ4dVeRHUGz+dhH/GnlnHHlcUPkLmwnkAfmqUCA+YPcKZt9I1uQq+f+T2sJ9suj9uDbU0IHsgLm4/4uPQ8Q0gT9lxykJL6rb4pwvYgTTi6RmmAjMYsSDjpIit5HsS+AgOAlyET/C2D3TPXZNOUzO/2YqTXSSUEmDhWlwyY1kWaEqKgUkSlmpHCMtBBg/eaCwup2yi79HDQywhJl7yxp/L99pU8XBTA3Cglk/+Gl4M7cfGcxKSaUYVuLk89wmw+d6rSpnmo9Uhyz2bEjBHTRk961o6R5KaPW6BwwhgPG/JbS4TNnB3Y5N/OWIYxsvx/yzDVIxW8zZk/o7sPbPZVQEARGDBgfbaXCbR8vQWr7ZTRjbO8ZAIVFEe7qFEIsS83WfSQgTKg9VfzoAxXRUw4fsqjz1HE0VNZfVwsdung5RMxBFM/qS27iWCYQkX80zY6UaqKMXg79XfDtao+VNcdUlKT9wt3+7VgqbIkP5ZxThuHTOZo0b+IXvoJoimLmzADohEG01aKV61Vgoz/VaFZCFH9nsziD6OThH5ytqpTxbuvOkrbC4vVb8+4UkJa915BjMYCt6MWI9MWF4WOQlGDyBIx2CDgZfBDs75AcYaJwBBQgmtctiJRA6FdU+x7WdO4SWzCWy5qZhgAxT5hVFEWH4GEkXnl2BaS2w/BRCg+B0qsiBfcJaOvHiw9cry/LugdpfyOvNnC/XXKgtIB57qbDdUJ6jOfQ33ZzyUzSKxFD5CLxgYE2BdPIwlm/8f3ylgS4+x4vxwkzcRbJkaSWlp4s0jNioIPtpGxsrXa15LdEiR1pnFLnyIfimkiM9hlkpkE9hUTMU9eocBwOuLjbb7oMo/dGQbMtMheA+0olE7gbfEWE0gfizUhYtllLfMPKxZlb2+dKsDPeHIFrTxogiylCbjxrw1LK675bWI4KznIYYSA+emL2Zx2VgSDo783k8+TC1LqNwAh8pYR4EpeOS26q1+WWgGPMVfVkefBgFF3xBw4KS5QT3kRlR5CtRp0kkMRsd0JTRFryBZxLCXOI0De3M2wo/3U1wdxf8+FL7l0Fx+qIBKKnRzr0acsgVVlPhEre+DlPsSFsj+rqEbFH0uaMHSkjS/RafuQ+UA0e/qeej9joinFyVnGYNUiYgedpXrMgwvJbYjX69G5KC6p7GaPjDzke3nonEo/k5XobRd4onitnNq/KY69NlqFiFiIN8Vhf53LZdexX279+95uKyFmZcQFcX83pWpITR8lmkJDboPDLtAKNa6HenYF5F/wBeJRMsMgEz8Z3oyxZeWDYvtEnCtCMZpc+3TOuELwqyJmiddcwgv41thIPW4hLhCZRfkH+cVlNch1b6Qgfr2KuoI76R25c8OqN912zeD01iH6IJff/WBv+35IjcRh4SjFwNk5OeBWUCwkD/avpSMtQOQg+5JfC9XzjspzQpOgh5KkjZ9lutf3REQ9p0uOcfJdzNKutDkujy80x6dTyevXmeRkPTTRGfhk45ubIXrT/yYYWn3athw443gwsJCgo2MEqrnZgZlzzbTtoNj3jxFTFyjsYEzF8FkN8U/dDd16BOWd7B3976wvghMPbp3RUmUmvPiitB+K316L/zL1SE5XLyPujZ/3WW0+iUXqmuhpneolanU6Ah0e3DLruLYQA39JQ3Kj7HP58j+LH2fvKSQjgclyuX4R4q/i5+KzswCFX/g+aR1q7qHS9LoL1/RHDppfEyOr8I3hbuPFifuglXmntkX4imvZmMRQU+zMQ4XJ6QtXdmlJST1Nuj3IBUzhn4ErMDrT/PDDJx3+OD1ZyGVmmTNPEVpD5bIeRCxRYz0ItRbU2DdcUSfiQxxCBPRmX7JKwMe1QPlPPx8Jhmr1eFv0tnZUI/4W+ywXVSXaG2hxqOP30chZMBqvBTMxdYyGl0RKn4YTe4wqnSOpnVc8NfZ0mPjxagEMsjPAEPMDaIgEccyBQMPheKLWXkOlf86GGaqb8jLf5Ea6MBiKJJKBpc0L8xmfBUmILz3zXZf5Vo8KL+hyli7fJyMOGvB14/S3/6q52joUxy12eYD8Sw5I0ZlMyfdD6UXv6+Qw+VvREfT0gUwoMKbwGvJLUyiNfIXJVcy3F3/deaosJk6sn3F5XFmppE70EvE1kQ1YdFkkaC1jkTonrCWWZB5oWTtrmYTHlZs6XkIVsU0SqNNFGkqVRD9uxxaaQY97vlyxVYJ9+c3Y1k2FQ1ZfSDPdX9NcKoxl9dGJBqCG4PChvxFQFZXQIVcJ/wkk9xkhNePbSfY6wNVqtyt2WV8obWEjKyhNbhB+j0jZhN27oNJc1/5rp/1oCD61Fmykgjw5HRVVid9LtJec/rJA/KZnG9eMqQtS/JDXGl02E8FGvB7pG0CxmiZLXt/6+Rpuj+dh5Ikr4oMvMu39yuvtJ1dLECqOt0rggofAnFOaaFYqiBVhmWIOKssxCy06ijDvGbh5R/zqngmriX1xSksX58kqNmwNt/jHBznV9gRD3o5eel/bfELfgLomcJkLaZFj8TplnGFAjDDosAzSTij05huAcm9fTB7A5f8wNokgnA90T5BoVn1iRSY2yOPEvtEDtLHARPXGGIg9RNn8uUXh/kajRQTAsyVnjGxbiIdzh0/JhBTVKgqiYsWbp6mQyWAI7ynVLNU7j8Doj3lHSx3hdphhlDKKEj/orxXw0JHTIRSrD3ebTWzsNsF9Z3PS7EZgU1rK1YLb0pg0Ek7kg56HsrH2MGte7eH6CIDa2qO6PMxxhjOruGfVqBVxA+FaSWpuuVIiG8RwCi87V1qxWYxinrhXWm+JfGjmV1oCpZoPr1Q57M2K7x8cBHjT3jYIcaGkHZKCzCYzFmAT1Vjxz59rpB/g1RP22bckFmWkwKtcLlR0Zx+eKs9NZiR0TkaTHFzr0k7Rn7E7Riel/csOAEveUnQbPzq65bJUkK4kohw1YUoktW5RN7/YtKvh8gTK08HCIJqPErXOWr6+W3NNjX8yXeMDS4FOxSeu5nqmPzPse5MlQF8CaYj0rVb6QGrIL+63/ySbUniEVHvpcvpeVE9OxwTWado2EefutF8KtPF8B2tMs+EXwuZl3O97Lxd8Gg5QgPKDzFb0zp5CyqNrNZG4mYuZxEuCLL0OmYV/5Vd3Y6wHPlH0Yx6Wu/sRnbzPcBrds5k3NE1SKZcqJgZiZv5EWjMfHiOmcMmXL/hta2CYgiRtV2euXCNIul9pQJgOUYwnvQCXyxmfjIBy2hMkcf6jbF67NWLIKkDpHHoenmb8cNbbg4dcGVDkwWKHTRgK4XYNwEeJtlTZLgVTGkofGm9qurWQbhdW/oo9KhL8kucGDUtllfCKATQ252LBDbLrqIYPVf6x6njgXotwWYhp37jZk1pzIJGAnbs4saZAAD6hlGsyEByh+IHZOZvf2b0aIHTqm/rk70N6/hx4f1pzggDX37J1X1NQ9HlHMrmKLmTrZ1bENbCnpI5uNC35IYBZUsmfXKbjTjaJbJ4lF+7EdeZOCM3bTwcl0kjM6WkjHJBlewp/sKO8oj7xEq6/NKNvS2nA6dmCw6ehwfEsCkusdQPRFi3gu2qlGiaxm8rbfAHlz+Kk/IBi88HQufMA7i1I9AEdxiKOuYQDx4Mjnh00kixqxxx0HvcyyHo3Bjsz25qR/uANdUe/6T4cgVQiHfmVgqwQyHUO6BWhpa/FHtH3Mqdgm/cXFVAMVFWuBj3tGYa4V3rmKGKY94LSYYWi+jUy9es6O81v55cMf+M4NOBpbeSyIriYzWhmT/hf9MyLhPkCKDNvVUq3fA5l7pEuxPwSXxuS0Sx5ooLt5DGWnoVt4abDRXWbskkFHXREaDyXfDUlMnVKvilsrplRUkzn4W5aIPCy6/60wQilnlpbSwhY+FBvuZIQ4N0zUpx6ZMYPk54kfUJQQ1/0Xa0xBFOnBgeeoidfQpIVSKXshMbSghzTZDJMASj8R5FCvY57PbnnBGm0mDr7Q0ntAqv8ifFX5Gt37rCC3mSfQccebYJmJ0u/srvP6o9dc5iYTDIcff768EuOSrvWPmYrltnqdSJBx1EZazamx9wc3ab2qxY32FPNjmAFNwdflbj3bpcQfXuSf1M1GZSGpv8JjA+4yk6n5FVIYfPVto62i3belWRjXE/49AbKY1NUK0DR2tSuB0cGmukfTBWaS5bqIU4OB4iC2ExaXdz0jE0PHBHNrCQU2ESv1KQ73ox05pqiqne6OL/ZwM40hBfhA8MByBDPmgGSHvOIZVtAaPmEAiSYiXJ1AiMoDbQjfxZn3bkXw8pBBT16mvsiGZcxQRKBjf+QVdo5JSdgF+pxSUYDltc71AbXoaP3eb2zD1f6Acql2LOL9rt0PidrdvNO+meoJlvgWfY6psMhn9pr3onpr8N00WSpsPCJ2EbVB/2FJ8VPiHeutNErKRpSgk5IzTbmANoymsk0QEx94Bth+aUadm8TL3pfHuUbBeYQd9BMjnLkHJYodqh13smsL2TF952MkwAG2NmwE8u5cZpSF/O3ef3oah2VDxtnRc+jfjmBMYy+2W3TSiHHPP0rXPxZRILQKw/VRkAoGioOQe5lL8/+UoetrjPxXtIgKbUOt7nT0PYfmgP3pajNph+WqtR7oHlfwhqcnEb3E6dvrP1NZEKGALdmgbN5OsGhB4BpOHNDgGrLrrVI6DzowR1E1VWk0/jA9LQ1qqE1qChs0ht2bbKcDks9HKe1zc2wRY8Ut4Jiw2Xc5E7MNiMGLpNdboqf3pCB66tpp7uZtY5fY5VqczpcX+zK/9tPQR4Ca2cDxz1qzcdGith3Eh6BvtF3PPotcGyE937CuaOMFV24EFwefbk1mQ79BAgbjj2VXG6akh8p42Aj+HeM8+SsVQ2koFQbAfwcRgw3dgQiRf185l0m7LF0Snrdins+meAFxtKfLXIpxJ3u5OSNg/BQdWpm/ZpOdIU7zxBmqCHsqTK30qTPFHcjqkryM/3zjFWbSToZBEyVFwMMF8opKS5QMLtkF9Opx8zG2XP+l3Zu3/gpSoiarIW0K+nWD8/4ib8KIo2rsAhLa+r2JLFjSiwMqyLtCthGd7veHaaIwC665NUW8sfzVmR2gaJPL15U7pJglRSsRE/9sQAtx51Kb/UMDb8OLxWnpVk0SWPz6p3pA35jIMwBECWymkuQyQxNO2R8MeU0Ffc9XdLDBenwjb2BgeuPxK04b7BbwEjjWKAu2q+92QTqPCmZzfhdwVYdJZ7f4wh0w83NcIwRqBKQxJrKc+zkpNiIT/QM/PT970zyK/4agP3/x2N/4geIbXrUTFlpptjKE1lIsPDCVqoxdlTV+2tOK3deoQGzy0PwPErXBxqB+EwMyfKVyfkaSw9sM+PreHWwEZM7wHA0pE661Fe2J2A9ZfR+FWLtsRl0jBsDDBjKbp2yOZ+sr/fo/yfj0aMCsYC48HvhEbaq/PMUv9vd3eJYVclv+bNuncUOMSOwrMCYHse6nK0U+/KEdJ6d14HS/15nSRYJrIOBZsy2128oBMlhy4Q8y+pJFPZkeh1L/V+69SAWg+amwPNUdw1mQ50ZDfqeuckaGke3JZN7uBVpppf3QfYm4eKDZ3UIls4GMx68YMu+Z4N4H1UJ4frhw0POfIP98djLht0s4YvJqRw7sfH3Ff+sNCilXURlsJmcksjGerlA35FTgpoEf1I9XnoyN0GWmJb589T4AQKPXZHmt7EdTuYNE0mvyynoQrBmyqmDOHc4J+nvRLFAitEg2ndYAGzsDelahvlnZznRHOEGuVO93HGof1lOM/hA71ImWDHhO9fgDM5XLpwE8iGIFUgFX6KFCxuAKby+5F6c/MkPdB8n0i3UFWe2txSKXgz0DwT0kxTy7pQ7upl9ryJBpUCc+VDoS7V1Z6WsrPJmoh73TezLYl442mx6PhOMoP115yfQGQtNdwaFF/KIc4bYYLWBbC1uBBcIWiOft9pNrAxYnY6eMjH4houIi0othMEZG9mnp+ZTgySbKyC21xpiLxIvGuVH+HXwRTMg8Xu8oPcpSTABTwkJ7HhvSHkzHPy3czYevug1iB8epuKHmGnjnshbw4BhIrWttDCRtaO2ADOhg/1wbDBuIjb39S2t67lWkMZnaU7IQtbP/vzNhFeuFoq8MFf8FmG96/7mBz8bVnMO59lDT086hadZOB/H+WWZKsxSESyLsefw+vW97X6LGx9LwAltqWAgs6qTvHHKOiJORXZT4Firx1evvPteevsKb+19pSV6U20/FAsDhrLBwwyTrNw7UBMSrz0C9AJgInNHXc7auSh/qBXGw9ddPmmor+a+Hh8f3tTGkImXVDasVLuJ2uf6mHPbJWwcrh4gQY+tGD//AOEkRu12qlSZRPEnwG4hKoaYJ7LyQC12yWTubxLxIMoylqoJawC6JOOA9Q2bUGftcgqkJ2eYqkXQalqGLVcdG+6IFKttbCkpioyqIkuOwg5reBWFV8DI8abjoR9gJRs8TLf7RB9qqjgCtenko1WykwPPn+KKhMDqEioxzfnJ361VgALkw0o7GILlBTodygbkVmL1UaYHtpasEZobnUJ2LtIe1nvUwfzSvh4s0VyDYn/WoxiaY8s6c3Rk7BUIoGwCcphoQuKE4QSkVzXAJyg5qriHPZxiNhdsvtUv9vkx73AUQSBlZuMl1XXCwhF4/YXKKB38QNJ8k5U/vv6cBNZXxZJXVSiw6LAgtSIT12frXnEL75hGNeIqrjGEMrReLuYGwqFD0B+xr40viV0cWqC0wM5HgR3usF/vsV7W23mloyBtC7pwBKd9Y9T5wp2wKv/K2gqjHrXcRzr9E9bbYNmUaKbx9niEP2YRh4O07QmKZaWiGd28XC5Fj1BIR0S+3mPRDs5lLMYtfXACS8qlHnXTMrxIAnKN4rvZPitJ9HC5zFlbDi71lmfkr8ULVFk/VWl9vruuRe4M3FbF4fGNJq3HferM6Y3gx+7GmWT4CD3VbZyqQ1jKA4u9A1Orb3ySXy3nK7xCKkoNneWLz1H9czaw45iYs17bAV9sHTicaq4VHRuMEFsCNb+aMAzYKnZpgkSaZt9ynBZAbE5/PO1EgxQqX9v0oIZasO4YTgc+r0/jRok+JacTBVicN7uiYd18wynU2z1Xi4JdVnwyPLQ5Tiy8/D9mB4NZLFA3tkbHHOVeoMUIRUkhLX+P7xAGNDqr0cvWnKYsSl4bSIUNmu8Z214cPv70TMfB94hel7poGLAtkYsScS00QL4s3sES9AB0Q5O92E/P5B/fycQG7AaIJ+8YM+XpWRpqxUrIVp7X0reyph2/mpU9/j2PgUjcZkpB2KwQ3G4Frz2Z6OT06O9ucAhgoDLP5+otCbXwXF8yuKH+tRd6pjIMw2PhQczyd+iOF8L0D5JfnymBm4jP3nQlRKZrxGrrIYPrWz0dGCNKdrTFio1uV21Lc5pL0ltQnsltVg6tLtEhCtafk6CjLnfJUzRXTJeSu5GUHVGSXPsQ6IO4HTwkQuftSIrRZ+35BCxd+CT1jn3+GKxSY3FRZSnUw3+Lo+bK5tBubtYIHIGxD/oJlPvlqt2JjdGHvaVtsz+Y/f4kTjS13tS32Sj6qTut43JZBDSuHkmRF6FmWLgQS6xW5EZHtMEiYzol/muwA069+8Ai78qdJk+TXip1viFyxDgJnKDfbBC1dvcKpUum80FzMz9qnmEnJTFP0grg0Mik7SRarNGSCzo78e+CmICAoZCczv4asYIaQTlNFjQ4qbCiJArKawvz8OZ7f8iV75JROTrkb7rqfSOaBGczdFhtxWHJvvbtvdf4glAOMW7q/9EhBq1olumEZPlbvbij81+S6QuWNDl7iXXIHb0AhqFBXOsethp64SZMlU74elJub22CbV7Npmk4mOCsDQRNSsXvSxNQs8Odfu684uAlrXne4nsxXZvb/0TvTadKpNDLYkz9ouDvId42T55b6L85F14evAoBNYO07OOAM+ytwqeDVq+VQ0y3kC4srqtWJJ/Di/YDMt9CcWnKCoBf/BOX5TrUDsPz/RvTZJ7f4QMf0pD5zES2/10MK3celjNAE2ODMX9mHCxK8qdwASijEKAllsAX+Mln5ygz8SyPSqcDDpjKAcruNc4hBD4AB4XyeKxlIkXp6JmbqAqVtj8ZxMr2FmeaGoA2ScDp/ayDPjfg0SJWNJ+GP1L5DOOzNR7OxnrPu2z8eVsXhvxPQwI2yO7/DFegRhJF80GLb4RdCR/SUWlCmvk/cWF7xGGyGlfeFv8Mwx0mDoKyTvC5yjTJaFOPLeykEqoMi6cq5OphQlBkxg1wRQuraCWfcTWgE9xypM6rrDWIGI9c2yXk0GWdHf5b58i/VCnwjED8qODZhOXwC2T/k5q1+Cl1feLGxdYmXRhPMQUsQUn2DfqM84vWv0skuisizfJV4WviF74JN3i8zbqYlcUoOWk7u38VpcU+d0F6zn1zZj28PCYOuXPJ4gS90J10O/Ot5msMcl6WXb8Ve/a65KYvIRGiP8ujcVi0vT8zkE4JUOIwzkNriQWZZmx3NXqB03bpV9dbWRg52QnPrRKckbC22clWaF5zi7+emeGLYZuKsqCip4w6QGvs69Cq/KOylPom6XsW4ZLPSM6zreVJAqjRWHXHZZjXPMMkKe13bqWTrP1Hgd3yUYQt1T8xzbNG9xerZ8srP6Jt/hEOMnZ6NRiTc9z9ptrbe40JIpkQn74btKJ0TGoOhCp2mTYz+jnsm65eY/WDA60CxlGWMzFYApOip73UEGOtJhZOVv/9we+QD9ojutIEHBy8KZetWVYAWylQ5Ep63LndNAqTsYxgnWIOOVQPBJAu2p+cPvRGuNwTOAtHdf7NE4hd/eGgJN6x/777aQ2lyvCTU36NugV8uaVLzRdegmoiPAowmt9ecIyFILJO8uLDAHy/ry8htWe2UGewEiDMU17jVSCj3CSnjAftXPgWNq/WKceLp3cG2Bh4Wm4gKSAcQ3VicFRIrhZ3d3nd7tNguxh3XF2i/nHitl5PD2kh0CbLaLgaf95FnwuuNVXxzSjLitbzrGmyBnhym40lwH0oS2RxPBBXCh2rkXhDBsm4bBfmoQONaEzU++5XRw/iETtlLKZ7FspXD8Tpr7j5nWfmpmt8Z8ysAfFwJ2OmdWEx5qTlUmKX+iNnlRo2LphJEaSX4N7V88iHFFPyreaaTlSMGSyRlzx2VSMIccucr10rzbMwVJjkcjNMVWTQzzqJk0P5uQLQddBDHfKWuhSAminMp+8LbMqj8TjSuEslBpRsJQ5XQJdfzEwQjPXd5tBUWLXF0O79xyLQpliYTEbf6c9uqzEfv7nf/c8xP6AGpabmydoQWUd8hzIP+1IMVl/SfeYDPSWE4VpZTHxIZ8jMY8zC3TS7t4EqR1uJwIORABVQPajp3sirjrt2TZuwbDssKHvpVRqWwf2oeZ+5XKgyxDh3MFTyg+jpUoPNtGRBdfUefWSZV10IBC9l25hK/1sTPEOImZv9WZjtGyH/NE/C2pIvrAI16w6x4vFy609cTEBlEh4y4TiNc6NAtO9GEDvIv6P0RkgJOojn7u3N6TojC+iPbUBoiz3HPpXTRNDW2GyfuE/GL7Ry+RSfFR9ICk2mNl6q2pCKp7SSKX+xz84XSBRw4OAjRWNuGShdSHMQl4lRtRyKTimRaZkr11ePbcnavGXZhVCiRndTgPjEbOb3xcYkBYzpSqOEsM0waOju1g7AdzDG9kZGwQAy5c6UHIbYlpZCHWcQbhNxmvlD5wEViI3kXFHy9MDSHxTP0p5jYZwo4b3w6nHhxszp5xz6LOajt/jNxt+B1dAABAPhnKVJMwF4r3RM3C+TFh4UaI1qFk20Y6QdIDKL+9mrtc59PoJ8Ngy78h12YA14WKLLyroSjkrL7dzeF2Lh5zplSnVJ6e0ERO4tXjd/XfRywsb3fcLIa3m2hejlBnXiaLYiy9tbePBlX9VPIhNXxj7K8lklDkHYM8aedydKruCWVlHY1q01fgqj22Q6TCrIyFC64li4gaOin7eHuc8qt5bc/DPpS+ZAXUiQhxFhCkLM/FXZS5tsX7++H4XSYoek32J3AVSk4sB1Xubd3s7sJhnttPMkm5fDju+6SXNcfdOM2+m6Rva7AcEkNk0JN6kFQkXDpROF4DwVj/P3exhcjzojdlum5RiajUA+Qo2+uVkwXvEUijHufZBxY5Q1DuR9Adm5Mnhz0J8h1xErwXADRjOYTyDJHcVTfF6ed4jHV9Y38KFTewwGojtcluVb7qwrPw4h5XxbI00fD/FXsNParw/PV4g3p/8RGgqOpYcyrWvktcOBX4AqRSCRJZwIGjLdtCaGldhN3q+o6nTZedWlh8cYjuPqJDFvlJ+/AK4qkL8jCNy2L/eu1D6TaknjJhjhZA/T20PzY/bcahJpaEWN8ypUNt/uQk/JtqzPb24Plep+ELYM1RWio5TScwTJSHkqfY8qpE5xlmWb/4FTLZz5MY/03aAP4LxZtLuVLeG5d1iuf96UHSwDUEjzgSqNicYXDDmGWXNxXveVVZ0NQovKY86oi4HFPgNdvQsEnUalgNlqkqwV4zpxaj8KUoZhmfC4A2xX3bcck1X/mdpkjqc+u4uE+1xmw1eKKVZqEp+scgJITX46s8x5kc4HSPRRaI99SrpMrvb8YjZDtBOAXVSHx8hXFYACnkP0IDx3KfFVddiDQmCQ5oeIllBh0b0/DghOv6o+w4lzxF0heSX+GBnJ4BTOvvfU7XlCLwbaAfoFg3HRD7vSUx6e10YIMXfagWToWUxav87SNC655rCF1mTzce+DqV8XSHx7uk0gz3NwXyiwZrfApoOilW8Pkzna/4OCvD4XI2XOwPqWFjfBnPjxRmEc4X65FHA8bJFuw3MnIMfw2/JF7mVyBuyFdIPlVX+idnnJNGlvEp7Vt171m7jlYx4fb6+CeRPZjU+thmjXdlhvXoIq1AMcSoLMUfJUSxWftcqVzwbYlHLgf5VxJyiII6DWOoM+9ZF/b4zflLOD5I7194d9v5stD2hfrMFSUUcBH7i2AlSvEN89L5FTZtaGido3gN2wUIO44prGLH9vj2hhPfX+o+8+0cf1yKVqnSIm0gdQcjQE1ECu4Yq/iI1WnqMzVm5UGaPjW0Urk10hO0ybjY3QSi0CsdcJ8sRpYgVWc0hud1g1WaRE2qVs+zaZki8JbRJVUWPJWpWZZGQNhaZwe22sp27g4Bse1KHjFCILzDEj6sFDB9U3NylukYpQuclWYj90w0qvA4os08ioHp8gMMMgPHPybZe5hpNPHn2fyES1WbyjhIKDVLpb0vYNnl80Y8W8z2ulJsKXSlrlCGYwmnojbpB5iyiczs2e2/1EmdsBwjH23fxF4nu4o2QYm5fOcDo5EZzkCntBSlfQ+btnGnd+bAErS2M8OQyPXkYZEvejeW0tsITdnD7Lo0Mb/WguL1kYWBkXbaVmQ0k1wxdB+CW/b4JMFl8B4d169YUZ0Iuqf7zPpMRIuHcOvNJbTtsZ+QwllTKSgitYqalNdtjcNO61AzEpV3RrF+f3o2FuOcL6c3l1U6dRw63LNUUUuQxbOPlo7mv4dS+n2yxr7NouoZhOu1FDxlfW8EIlNwgQlt1dYYBnJ8uH0z9D3iingEFAJUA75PB8f9vJOVCkMDmmK/440yZa1YbyW1AjDdLvEAGkHXtY22G8wxsEntmnR2G+4OI56RuDXGVZiu7BSsQXR7/Y6P1dHMnptJrhhjiNMbShMK+ZprrDDk/yZ1XSKXHus2856jxeZJ9Et+DuDekzpBP1GKriclrDt/p5QTJBQ4QDcxj1DHrw7RLNvM0+PAFG8pIcNrYGt00n60d/nI5I1wiaxmvb/1LE5cVQfGxvK+0Em7YcVHq0LmbDRaQLhx74CEo5/fKDgXCPGuvsAQNZlst0zIJ+F9XGPrhppPozLKxKBc2qRGFeLr/qKR4RqlasVRmN4YLP07IxXujjSqmcuZvbEXeqczDXwbnZA0T3E+0fiWJMgq+g9LjZrUdwxjHSe0xjWXU/GKVaKMm1WhwqdcPJ99L7mBdJHf0w77KYXGDBHJrHTIIEGARffOYtaK/qnfdBpD42fK2ARyvl5CN64CIlTi2ACudzuIZmwbZ4sWIkoezERdPrSp+GMSsFUXO/kxRxReaSEeQyp5jj64uLiQXhc5VzpEluD4RtoeTxkZRofjVh2bq4J0ura7+6dZfCHfv6b8XLr4lSFXxjhjU2BEPu6+YNKmajeDGRG0W/t9pJ80vOSW//vBb1qWmxMSYEdBU5w4b82la7PoBUfitD6Qzu2MSX38R9spboApw/F4kwV00OdMGpba42AhJ22dm4POss8VMXsKnL8UfjrcdMpZvOlxPBeUTuTj2CF7kM8/sUZY6lZp4E5qRMSImzukMhN/j1jbFd38VBYuR8xY+/XL4s95zWb0Rb+EbfpIJEtIor74XbyjOxpc0G/JeGXB8DMnrnQsqrpcIrpkD7FacvwnccOYtYk6kogiyn+xln15KeXXJs/jecyayez39RadpzRDyQwrHamIHxd2i7mlqj4f7Qpt+AqmzdCsVZ8J5uRHmEervbbH7wIp57Ry6qYGogXa/HxKuX0W+QyHTxhgqWT+mWTbLipC4vTEoPI/2NYMPSvLdGLDby7L8Rvd5KEmdYwlYDTps9zQ+sdDkLb+czr/nFtK7OpwsFfiUGD1AojwzXOjat5qUKjwONvo0z6BOKI4QChK1OGMjT+LmHOU7gnmllbyhYJdMpLOJkOb7KfiNd/xEaa5QBNOZDssAW5ITUy2+iIRHPs518VH0El4KkXARz/EWtMuF5iBtAs+9uxyJoCHAch7mbwzXaYAYSPZxvwFBwfmV+eScQF7y6ed+lR+Q/aRFcLwdrxmt9VdfBwui99M1rnqK40WNg99GAp5c+T0Bi8NGS2A8yUpHoJC9zjLxadl+vYu8rQs/id0eoITLO64vDL2to45Ji7Y78sznl68CAnXdhbNZx2JLLO6uisGDhWUA1Y6zzToitntLxMbkJUKThbNMOCDlMsGareKAkZsTawXKi8x34xoCnQeKY8n2bQaAGZZL0qA6vSsEBQNUWxCtXgEy20INr6AndPJXo2+EgAPE6qZuLGxiYAteDD9X5s4GqnKRt0SoIWChKZ7EvOlFwQpul7QFC3IU8z9PItGa1TlO+XcLoIujD0C9eqo4W4diH8LHQrz1VuQ1kZb41oyE0XFSoqc6eCjnp8SUJoWG6+OMhqAlcsuqUnaNZ45iKV687h86fYsaSWwsxzv+OgNEoSKXzVeD74u1TR0bpU6SlDKr0VGX0ReYkfoUC+oJSpO9uyeXAL0NhCL4mG/DErz82JuyXZWWbqIpTJafZxIINRwt2aUPqtGKlp/WUDSntA54XaQif3jISFIVgRA/csYlVFBUgr1Di0levCbd5jWCVewbGNj1fCHKGYmHXKDbkODLkS6JzGwl23GMsMoZYJKgp5vle2C5vY/gwaRzc6ke96o232GQmNolZdXohw8OnlWeyIJyp2Yd2lp7N2A/h0yDRkTbERa1WItkeGjh1E1Et90MXYjWeLM3YYo9WE0IRG8JMErY49zQcWhBVCPWDkm6ljGZ0nwUZdJkutIqRxVCQl0GwouPVyyhyMRv/bBl8ACExgkQ9OV8s0T+ahix1B3icy9bFXyoEPkQdA6BXoJZJeGPCaOreQJBvVtf14va99UNpWP5Grtb2ge902bwDKVaisCuqCENWNGxVpPPy/mdQQUh5vL0BkS5bCPkP2V1jfcGfrco3PW/QZI2CFz6eOQgNB83Qdr9wankusGDxAKAS0OjY0Wxhm3RXle7akcD4gNLDjgiKx8TGdRiFYXdI+ViSMN/8uGWAQF5rEHKjix4S8nsX+kWUUwW97DiybZ+/yS17rE8EDYpmPXUQfbKmnYr70ovNmQ7aTOiDJHMm6VtBBq0KS9dAX32RlD/Avmgx1hyBEojDPkeTu1cZv4WKXstIvnfRnkA2SIYddPo8LW+VNdPHazE0uSgE2o2ZW6avwDf2EqQVrLpliJk+wmbTebleMB3FhnV2vWw9KdKWTunMtiRYH3wdkV1AdWIsZaKvIl65rIb3zhqGval3xVNKBDY1CTDtXyZvuVZKNbvuqjXmsLe3bnpqFAPsI7+PA//apm8DX2ZKZFDVD/N5/nJKkH/x4ayQQqgnE0FV3mdMyuD3p0h2gVkwuPqMb7lido++qpVWbFFxTSvJq/Mv0T08ybCXW3ar/sRbLAV5zG5Ufa+EF2cU9T4p82lGG0jRmXkDZTgVAJNqkAeVjOCwJxEeX5nTgQe6+t1np0XL/5F7MxOXYiOBD1/HJ+tWhLTj+Z5ShcpBXIl19788E+M2biOALzoDNYrRHroNJB8y6ghdOrByBjF0ew7Jfr0djHpyBYMJTufoGEYLRRZhpJF4/zzO8FZj3ITFk0WW1ou5hvm1ypglGW1qFO3owBXekWUL/BKUMgnaZt58Bh8c2KHS4T/CVJ2oymLn6MnuAQi9i5BXnuiK4muXZI8L29Oy9A7PIlt8wCmE+iV/wgtOrRAVuSvIUUZsj+6pjF8MZFhaHKK0WWytmKucKJjP2mwzx+i9ZwztHP3/BIV+X5ZAMOf1Y3RC8FFwY882NTXajf7/x+PCE3VPJgbGc3Kvl8jv5MUReyVaaBsFv0J3bVhyr/jZWYGDZZEfjivuSJrANBa/jzSozV3peyGjk8aEpEBeexi+NpUP0WtZ60tQe8qN4GUk+Aj2YQUYtxQ2JSryugUQzXHHRmS5yGyEy8w8rf7Eo/B2raRuuMwn0CmJtB1WM0NoXRHVgoKrn/f4a1LJMXb2o14MuQK8ENeGStjucpg/sk7FBQbkRXBVoBBdKMn/9rue5ApqA6Umj75hwuZ7LOL3Lunge9Yh+o0epReI17weEbRP813AtKyXyPTRqZlv6eHnCzQj/wQJ4ATrgeuu9PbzaXgk9J1eSEGC1g8Y/2HG3hX+ZytR3KiS3L6NsLx4kzfa4Rs5xsO3IY/E4DP3Sx2k0zFkf6APT2n3mlRSBIMENXcAg4C7sxtM5FnYmFiu2dZ/bzwTTKXtQvHOMYPm9bQb5gPdkQyimvq3e+jJuFSYI05D62uCTz9nQnOc4nqeXjVHHcx47ubARa4SZsxS2DkZcTLheAs7ljKvRBHiIy+U/7s2jc6h7posFcEiNG88K029tqlyxa/LcOGldw40+MTbkhie7Yxhw1kKnd+x7cEsRRpR77fb706GX/eYZJF7td3NbvrQgXXLkbdNKUMwfLQeRuqpwTI2+thERSBv8IlOKe6LOaELO5QgDttcglIBQiK8Z1BGRYIOhv4nkeF1gXr7VMum3lpuLULLdcBBc+MF3y9SaxTqpKHNQXkq8fu9+800JSmCxz6OC3V/ptPbnomF7kWM1dKrldmIRYZdg53fyQaQPg1JKwjKZWwTps1IvY9KwoT6oxiGEaXE4vwuw56kc9DSe8O0ejIlMrU9i5SzvAZHaSXaptmyQEul6wF6HQYviTh/M/LHYLXPuL2ASek/3aXBVU9doz5BOfjUsieO2yI3gjcl0W+xLj3xVNCeYTTYX6rZEblgFML4otjboLoVUDgc9DH11W5rJbQrgfdI1wEV5EdZPr8wZzEhFhZCRtNKFxdOPVjH/LerpT8fDHZHgVP1u31i7h6WP8PlYN/0PlggjixjV25/vxeYMyIQ+dDckAUK3vrr6vi1FGRL8XcyaOMBV7jd1WTrEyBdiXf2EWjaFZD5Cj+D/HaXlmezuf9Nxl+rJbD8ai/I3fFm3mqdOzUoadiONpUB1+0Z54bKf+uZDAOTYru0rKzAPThD7MiMKCs9QCuQyYwzpbEEZ806KBtL5NRAbSZc5dHhOPbJBd6WD+uWh88v1KFB4TK1uBAQcpu4HJ4NLf1CkFjN2/qmtPFj9lWaQS4GTnx0G79ep3EHryQ3kvVcIscIakNqXm4flnihp0NdcadEz9OtapUHvvksnlQo5dWCkBMxG/RPoRkxaIxiOcuwEaDAjfUsx6aQhiZfk2mXE8VWm4SptRqqj1P9GfwKiSfuXmtRdldWeSi2sY5AnH8ovx5F+6Apq2tPknh7LS1NnpHUKuy+64JDRSHlo73d7r8xxdDzgy3nGT7Awl6KuwSmS5DrJjzIeDiLVdQ63VUGxAGH+6Ln37sgcTNLC/c/Z0jfEJfcPAsr9lfUqF5xu/yqaSXafUCsJVki+lDKdUNpHH8aS2uOuLair6/HUvIUyabbr6WMK5SmwoOWffwqD2VEO2rVEFaIHIMnIGAi2lPVUjnWzPAaSlu6r0lf+MYHqs9waqc9M8GMFa3wjAewnSHWWmMDm8+pZMn6d8Nz2oN/FkIuA36bFHYEPOz7jhZhP8N+N27CdqaRKpXSOfOkv4u6xekwcaXIij2BaXYgewezCgbGK5uwVyFHx2cp5B1+762yXJfTYkElNwN81+r8S8JUPvt8wC+HmjwZY4k0eNJZkuuYpegEGGGEQ9bV5f2yXnHXwDBZtBFxXizr3vrWmplXeM9d6mb6Y43RVySnpVK9THs95VGBPZesBkr+dOnA1Ioyh/LtD9v6yZ4MBSebXSqQz6MXvdQfAHr2mBq+WgM59mEAh6kSMxXh06/JgVeor5tM9w8LuxuExcQFxCXh+SitaVAqKPoaPB7fplG2NBsjVobIlv2uP/EtyvyQhYQtUl7C305w74gUHTzzdpImFh3ZXtimU82FXNJafkypHeIc9dN0j4s6hQXyOUbVM/s86Va/oT5DMq5u0SkjzOCcq7PJ/V3uw1XCGVzYsIQ5xf5Y/6QSsVShiDbDvWiRWTZ1tCSfedt1TL1d8+XkVGIjdkmrnuMLfAnrl8SirL8kwS+ndeyWhBYHkCnFKsktTHU347Zul7wJ7uy3e43kiSLLe9oRNIFQ/peAx2AahLvvS2D9G2jTwSD/DOoQeUGSr9Uh8tibwlN6VynT3Dq32rk+fLru4Hr2n5izaiIbsMuE05gxUh67u7wEG/qSnNatrjJxF+x7qcIu0FKquW3zcL6f4X9H4T0wM0r7lfdu/NpH1kqrC8xwQmIl+K0zyD0DzgA8VthpouCuiRH43YW9iBc6DbBeMClzWpb3JAnZwt0LIO8ln2CBd8np6tzFxt1Rn4Cu/YTKj7AT7p8Qri63+xwA4K2X+DcofLIwK1OoO5Anvgf7eIlehEleyuL0n9aF3FHc6omLQw3MWK5cfSCwd11FeO23rdVK7scJC3ywXZsJD2YdG8b1NziK7M9eK2tIbVS1xlKCaBIGYhOB6APX/Mq4EOFgnUDciTi0YaaYQvef3TmnTEZTAVLXB5x6pIySoW5geYz4mUKIJwGkhOA18AJ6iboX/dCiRTGrfjX0sRie4OvFIzdtGO84hbpIJuGU+qswSLh6mlKesOZ/YAHz3VawblRzU15ViYPEfyBNEky+uwMOustJiNJH0N1Mzdz22vVubPC6a7eukn77qUJXb1vFEpakoTpYSr/GiCryYUTsLWaTiIiqMtKE8vDeHrbScTQP8jBKrtMxp8NabJX+pVYX1+qRjHvV+IG8kvXv7ZhtqlQeNRpCoJCi5j6nR1IiYX/X5IieeQd5Ahjx05qfS6ZBN/YnGRyjwXoOQ8/6atGZtiUQ0RdYgmcnYY4MFsYDS4S7e/mVWJ6ibj4D6hmbAAn90gzkLXMgvTQjBjlOIKp2kCfUQwJz8RyGNbRbaPJJpiy0QuUMv1drWvsSm0Nm9nmKo3L8QKd1gMSsqtyY9pEsUlk7ZckZepyimGP4ZKYN2B/MdMaNwm6jOrNDzTA9e6KpNNDvGTX8GjgSttqLSxtkT+8lsQpoRfToVc6E0ZXvQRoVA7VrsCfgM2S4ZisWapcdd1L3IplpbV2lB18xYTqfcdFjWgEb/B7N4osGEvv/WrI3YHkhzwLXe4jw26bQW9LNfEBkogpt2p7PktYX6/hZ80gZzpH2ibzQYp8cpR/e3+DpzqBSblkCLydfvIcaHdNOp/AtcPx/GtegBChhPpeweSqqe2ca/pJVl0hHWQ+xlaAAHVBs5pHF7ethyPf2kzyGKwoJ3wU217jqr1nJX2jggSDnUGPKGKB/cPkbkXBkH8LUZpW2jSUeqDi1FtvVAVxI/GecK8wxJruN2BZfNXxmuHaXtCHYvvBfEQYk0iE1t2f7dODBk7HPu2avRHeZgKanuXVcCt8GosLrBpQxsmGeXP0bf6MDszW5IFJ5NP5NyYF2jzPDFrGNUl7QZIv183WH84S+7mj29iZp3q38kgwD0nL/Oqt6fROl88a4WhZrkDDWuuvYSQQgXXXOtjI6FI8emD88QmApBIL44ukdtwO8ZAAFOaq3mXwpfCK9/p4Qz3rDTxn3Pplr3w3jxLZbPVZ8YSUpBcCYjDmtPw5l8GO/0tKFdg9cjXyJBJKgvhcD4Vib5zDq0EDJd1uxad5Iia8r0e902Gij5ntZqzAtFViF5GSjsOLluRw1r/HpLR3YRsmOgXN8JM6xWnuupgAvLVsoSm8lq5FVd3bnFwc6yR3tYM/crU/aLJlZCWbyRx4uVgF0QNpM8GEZM8KrqCQNZZcnZyn/eMODtytGN8BcZP/cIW4n2NGVIbiDq8K7JhE0kUVn572bvhsei8+hp0UNM7hixlw/M//Slgh8I1hw7023QjyXP/Pw01gZDjvUXp1Ae0/E4DRCc7ty9OmWyO7M4HthyJJn6xCh6/wDxVqp1YEgDj2qbuRiu//QfOzGIJ1vcGaRKF4glvA3MpzSrd3Q2puGHmcbRKEH5m+Vh1TDuTJWZZ/8Y/Yq023jixgn6HXI8pVrQ5s7jjs7/ON01okVDKl5CyfY/YmXVXKouG7Ljw5ZpeeATyy85Idztli1eSdAsKe2QvrKxqAsIoCZSp/nVlWgSjTUvDcbUl1uSmWgRVvX85V1hJuLxR2jFJd2Yh0GMsMk1BC3RTpeBbwT1WMa18NSrv7Y4MAnBDuuvpuydFf5I4Gr3Ii1thK50k6Oje3kf/CGMLlBwYuPRYnc1A82IpWPMPaCPDDbnMPdXVr6SWOf8VFsCpVvgMrlbbycldJ1zyqhD1PFJCqvj0hblTYjxQDIxkcjvYHNxoxA4OT4rxItbvashmNIu/9gG3cXjfBveOzYVU2moEdAvVflhc1IN2ywdMc/SEMZ/v+gmxHiY9FC7yaG+bbmm/9nUr1bSQrQzu2XskrlqsLjBf2XctKscdH9AdiLiKxmiBvZi8w9mSbFnbzFKDy1mXJvOWoztj0MgBSsUbPJ6UZ5miJRyiINExXKtq3mcqLMeud77MA43LLzuhEqy3p/pdVMEIhod6TIr8XytIeU6njPstEfJ4pajy6zlnFsro0/dkxpV7Rb723xnR9F8ruAxkGZHNSlvpt807DUtAphUWrdfxTsYgp+Mk6dVytV++TN8qIZLi6gKDarbw6vLdpg32WxahdhF5JzGD0D8T+7QSm7tcaILx3IEdQzE7CzNJ2Fr+/goNEJLcEk7GQNw1mx3v4+SOYrCJtsIvhuzkq90TqPPkvr13AiMw3lJpi/G8clqTQCtGkH0WIpX4WmxN12wkWhSZ1OXEBobu4QIAOuTQCo/RPrpPYRsVmoJgEz0WFfmwtEyEBy653VwgFzgl5cdrhVZ3H9QS0/baJnhTcX7cCZ5TgXQtjJj4bGS8C8mNUAl74Fmxq7RfIXIoP5Juv9kUHFSWoljB8nKIVmyHTgIbilv813UJ7AKs9VE40IKY9vMujgjSU4yGPmVKqHRQ7F+u2SmZO5KA+C7WdiUe8lmhN1onRsZtD2lDcUZc6zHYC+vJ77xUlrubAKafKOyBRNOiKFFRa+QVridf06nyikRDmNLjvz/TIlPmYEh29TzGP0gHPpnRYcU4x7w07xbvNPkwLlc7iD8AxavWHWl09TGhJbJtcKUtUwl0x2c7YjBUqBhm5INLQNc5Fmy+F+bII47CefFBR1Cpjm2pU2BEDREkBh8Gw1uMRyWwssZCmBlmlZEcj3GlgB9h+foGDv9niSNxLJptAYupAIuGhD/dlGaMGgv1XqUTUBbNvESfhr5eoAPD1DGcty9LuPnmfe19t9dnbK27zD39UyND/OnI1+VNAYRmOKG8crNZ+7vWUVDutOKMoLTV/2ADpMEPK8l4Ig95v4QganTu9zx+JT3XRKf0RfFfknOJyQi9EV7SzlSiaFCYw3hcNzMbjcUcxXTJ+ce3vagqkS4TyByPrK6AKvxVM60rI1zfO1urp3evAuNwDysFT4s4fMjuQ5uSpO4Bq2Xy6VxGPpx/zp93kFaZUBGGeqwSctvhIMQg1DwvCGVjeRZl8MuQUTnzcFB1uJ9PJlpW6ENF0ubWIQhRXPJefOquVGJutnhglT3uIQX8BxFBag0hRRz8Y7EmN5ZIjeGD2kdjhG98r35/4Zqfq/0q2F5flqZ8gApc8Bfy+PSSKh2Rr9p66BdAz03t8AMA7rGWaPgjBYnkokqhpKEJwPKxzY9BHTR32NPdwU085ceHEzydQt8rGLhfPpeQgTNkDiZOPCemOsNeqMjPwrH2xHe3AIhm907MmobCLlF0JXtXxt5F8I//E/KiLClrE0yxoThfNXUXEWKeWLMzxw4qdx0I5wtoo7ZMelCXgvxDPQImIlL7QJLntZ/hfuh/Ip7O3J8A+woOS2MGMsVLSNXyVmPfwf7tBTRiLKmD2dSnM8bEd22StSlGNTu064krChsrO5HILz70Lt1yVNFLPZUxwnB1fpn2giNcjWe8uZuGnZH6v8Bu6nETgca7os7c7EjK/D20bnVER7OXRIQlg/op5fpm+mTkUQwLe47qwV9A22PGuAVKJKEukC2KGf3PA4gWynDNvFr4A1PuFX2iBKZCbA0t22X4fm4tB8ygxEz/VfowDN+AE0q98v41g5HbJaS9Wh34/6RRxomk7/XuPzt3KA4j0S570p99F7S4SBeoXK+nHDSH9r5KvazusVD9Pb0Airnya8lqYxMBsmIcs+Ddb0v8zugPmgHWLqA0aXJBOz5aPsSatRJKDp2xyHjQnBtQgggepAPN81mGZiS2WAGqaxYdWwMwbBrQ4TQNI/YZmPQ18/qYMlMz2Jd6Jc7NGhMEg6lbL4Lsgrt2EaHTZ+XA/foeLPvIu06DfeVWQyT9HyvYkBD+A2+Y/WGTzRLEMnDr4ys0p0KTwsL/LgTtTCogDidNMbCW3DaUCERxtU9dYSTSWJZjGblq5jxhg8NV28aGLVHCbkWjD7UclA5CsqsnUjeSrefmfQDwIYyr9gqUWQEdHirAzTXVJwjNyudX2mRFfEBEDkNcddheC7kEpgHo56FnEXTzAlr1hkXqwPslcE9GE+/VYe3vNuw0/Q33TGjWT/ATvzRRG9CW9ysenOkmtKqLwNXOrY2vSzn38u4MptoRDuVnqrQ5bhQeDigqEuNjvQ3GpHZw45BdPTmfVX0RxVYMTnAhREAfQAtJM9AVF5A1zfQk3VsExLzIT5QFUB3O6uYUwrSb+54PYv5DjNX/jsmzyEE/yge5rnMWm5LaKPiNdfBglmhdng93v8JAURP2+2Wdvf+lhKnb6KPTGo9713b9W9JYstqCjNrF2YR5vR5lgFCg6iFzdHy0JWfgUjsxARLzGEnMi7J3rNLnP9gD/1MnF6YPerxU0TjaLEN7chQg338gXLAEgwnDUDlSUvkaZLqTTjxCo6nusS2KBmRAhbk88PiMepY+jioLYkk00CGdao2XraiaAYB+/PmZ1CxAhTExh2ZKrKqCu+VmYeRcqX4/YfnGFTUgvSgHNlbg31rpdVakMOKxTFCFX/rtk/TQlUoGLXeEXQ8UBpCvciqCQYxhu5siVR3g1TCfTnlvnD6A1Z7IMSxGfCFFVosXZBvsMJNmT0YwmDBKwksEw6+0s9K80/WVFaTnhle4yPseqpm6Cbt0g7nDTgFdkD5tn1IDLT7UkKZWlybocpPpWUr6YPTyJIDESn3iUDnkyECEjc9DuT6aAIBxUzPNz4tHYn9eu8NSEvxorTVUhuWRMU3KuCd8U5dREDMf9DuH4bLVIGVdt+FwUk296MwHf3jIT6wqAkEqrbQ2OhBgxye8r+P5VakWbBaVn/emi+ClvbYnMDIxCpKQREBjedvjlE6K/3L2VDRNEcPWj5/eDFDPAffC3XnM9O+bFMli8OadnPS1N3dxLCLMw9GFVxMXoU213MPTLHKz+PMbDiok95b2mTsmezmlC3HLsv2Sh6JsL6lMfG6UMoce0+Ts8xaescIBk+R3kV0TH0YztARkt80laKkemv53T9MAOjMG49Lm6lVpREhZTWrpM2UbV2qkf2623Q6c3SI5zzNdLWXTueUFKk7qdJ7QvkiDkDsUi/zOpzN8N/joDFd0CbQjIly+Xs2gELv5gtMglQg5UaUdnaHBy25Hp4mwfdSDd0/9yRjEFicS/fzi8yEfWyT/gMa8MEfn0WemNc3TwWenTZe33S2qWL8XPMu+JgxK9uCxfeclWAwV72V9wkW34MkkeAvWI8r1MAr1chlRcxfHEZeqggVSwSmnTmFF9ATYsOrByTCwVVbXv3r63rnnH+zXfexXR2vphdlULpd0sB97tR8VbWpVjOEfE3u+vcqFK1AOMV4IqgBUFhl2oX35Tp52VywEZAEBnvLzeV2J6ok0v31GNLZXxpYbhAlwk2hcR2lCDNvSQpcGgeFNHmJsHnibbcoCG0WO3AtjacgTeUZQEkoWTq/Guku6CUY0oX4n8HWctE3MAyxa2qlk7Nm/Ry4mZkwvsLdbr7v3RpeYgWG7ZluxDm/ONtCM+aVj8W5HwbFKimIDC2fG3Q3msqCGrdAAVvkESqA8vdgsC6fw2HlvYQvgu0xa63Me4j6f8uUi1oHQAMe6xyd4crSNd5MqGrrggXIYcht1lvtS3vbYXlCifKxF8KFmPN0WTn4ugeg8VveGxlkCGMsemNCoGleDu0m3aknW2dCBunsLHdQraHt3amCmYhGW0h9DTjYCVp1ZFYNFE3caYstFXX1pi/5+vUQhCbD461vr9WOYftM38rsBpdM5ybjvj97r0T7fnzP5PiAJFQpG42VBUz+25/Yvq3RyjK2t1SYFIEMrKmb8iDaotdtSU9ABSt8oKdHCQ151PDulVRQl+INiEWyQx19EwCDz+EU2dR0GeDPgL2iI9K9ChZMg/7+9bu0gRl5d453OFzK+RWBALianfF+VJmAV9RAPZXWo9kiLk18kAmg8AI8oxwSLpjBRr94OmtX7jWVpFXjxEG8FlrLXxSuCXVfhmTX9fd5LUET5MHDvSOy1K/uZfPGr+Q5Wg3GCobMB5A8h4nJdtzoocuID/nHuarZ/9CMXMch/wjKdgkXsVOIzJ93qcwndz8f/mcC/TyRvuFrb5bNy6azg21j2sMJDuNq1ItBT5S9aBCIenyHQBSL/pcy+dkGvqLfCpgTsqzT4T6aKd9qut13ZIy/zwW27J2pxTLiI13G5eIq7NHLNbE78XPqFOCZP5X29dp5F232KVvNDo/oXRPKdOdHwj1hxkEOJvYUA9oF7ngtB56I4HyAvHgK0sw3S4pmLjTRCaBgVB4hljqi2xzWK2L1Q3KDkr74Qug880hzntH1FoZTkqs//GBaevenOmIsZ+q+iWaNCKTCujP+v6qh3PFwmlbku2mX6wS1sPYwumYbNcNr0+5twNU8iFByUeMXV40IBaEmirZPY6afcSS3swFkSaA51JpZaWgn3RsWsDqPWJE5uTkgbLefIYTr54eoYGXR8PKzOKYmYY4JwWH+GsjvxjTiDyqimFBLCOiMFXOng6EPs4axTEzqV+vCeI+wp2QXEgLNgEqMVzSSFe3yNPzeZ/4uH4zUxMYHJxxwsmzkz/nln3HuVYVYI+H4R9ZD4uA0WlbeO2H463le9E2XIFOItZTfplZt5Q/FCnB9PtCtoP+9/rKH5VCoj3vjpZ4IgmNO2jkzjWzXVc699l7ZRGbP5fGqYpbXmtQWUeYJ2iR1M/zWubadlBdmiuA6aPwIMRUC4iORqVgnKnfCCZd+L1aNE0B6edeOVa8iAK+kpdgUzqSLIYQqLzIGIAbBBuBrLbtyAaKhIM/nXWMp/BITViLPA738kch6xMd0LTfBogt0alO4DnDy+3pW6O7AFC/4e9BINl7OFvAnDdKEqizWNs+RnheXtVxx9Z2E5ccj2hcnCVPatk9zuZmkrU5i2iWHx7Th5qAFjEAnNavmkP2rvc4mnoUe+Ycjrr2x0GMLnwTMjIXxILjvgg2hI8Kc84fzmbZj7YkPy+rfnc3TN09ZTEmwGPzsGWdmci/u9lSDTfPwvpFqOWPuyboqOfSqfEs8Onbo/o/y7ojxt+wjNL4Jdtd8vru373JHeFwtNbs+0vJgP8Mc7EFjqgPedUsw2+8hKIMmbSIuhRF7ziKtG6mqOeX+4NveEfWal5k4SrlB7Pp58adSmwsLAPlAP0nD23cPmcAm2+0QSnbY2/ZqmLt9yhwBryZpnEmk1odnVJ//YJUYodKA8rcf+nxFhZDdnEoNO30NkPgnNZ5RdicHF98nygEbvbwWr6CEh8dh77LSFkpPPuXk2sxH83aD5uaBZQoChqwMzqxHhDb9dBgxuTSDo8Padf4h12m8BFqZKKoEjz2xHPcL0s6GCrog8rV2qPg8tjMerbJxh1H1tzM9l8ZOC18+Aj2kFGOaYj/eCLZWmtZ+se6VgN9XJ2b+cJBYClcbXrnmVtqsYEwrtgJdZuFwCAeB2rao18pVNlKwt041JUYyCFT+hclLnWw6Z/d23perOUCE3mMrS7WbRL7caZksaEYLUfncUyeBAKFhrv+cWCcOgI+ys1q/0C5h1rRUFuMqbvEsU372zx5pXAIcsI0OvYlJh49Y9+mXLhvSuwNA2mVOKCQG5WTT0sgF3hxy7d51Q3N2u25X0bjxNOPINCK0ZyTj8BO+4vJ1wn45Zhb/lx5bgpRtTa4nay1+E9boO+m8XbZ863Q7bnDg+J/w7jzdwiiiOeihXLee0VKDtQGQIzuSVckO2y10WcaYQaGgXPImhuAmg7BMoWyxSwjP5jgfZzT2HS77Xg+dw0fTeE/CA6+eA3CcqtjaCHdvcBDPIlzx5KpQlWB/I8US9lggrRbUCz7fyPiKay1t+6JLZzzYDd870pRGRbfM4fYn30cYnDF/K6l5UH80mN1/RzGJDBq978PuA+weo7ptefGtEBj+7q6HI/OEBrlHNjgFLXTMDw020aCwLNKwCLac4txBBmKHqlGJMm1Zp63gZQwkc4sceT5z5y1YVcLMzh/hPIbHQNqvnywdbaabmjlXTLf3ihOtG175kGNktWz8b3XzNI88dCIIdzYqGT+H3nifG0OjOZOTJ7e4QoNWn5xbakaa0vRrXSq5HyZk7shHcgEX7kGuCjLLmUmO7EaYM04pMcAPrN1DJmz4dQxGM88t+4XG8V3U0PJcPrvhpyT3QunLSlV0qko0F2zVktQ/dg6uNL/+9nsJB2Pbtu/xiTMVzRbvoUADq2W3OlHfbwD/+Lo6MMo3CqIPYbCU4ixdv6KiXzDmm5p9poFXDfSauG7EJEb/oeYKVxHzBINv9lxgfjKQbpWpX7kSn6m6poZd0ClGV/ncTcEUtYiEuWcP79ar4ShPW7dn6GjgOVL3jWamWu33nOY/r/RvOzc2DvNQuOdGBAMNM6Q97paLna5EO7JCHWzEJLPQg7dYEUm+3IezQokazBiaoG51JlfBkf3c6EPD3UuCJYUeYiYQSKrQtu2sv37O82w6wvBOJvgQ++RgUDiELwWYAd4r3WHJxyFzsW6yRd6yKtJ5jlgSNVKadfMcfcvehaCLbDacDZqa8AI8bXPWITxvCOYLdeDD+ItwkNaY88wU9mDbd7M6dL+ByyGgNAaQqjB385uyWBi0UsL96d9JLP8sco36/GMRhA/V0k3PQt2yP25sNTo00uqa4X/KubXyqLMjDSOnG2aYy1lRyZSGBcHsWnhBcwrpJcatoIYD2+3wqd//X+XmWq4i6hh6ruDTI5mwrPbyw7I4wMaRGmT3ZfpBslNI/bF4hh7O5XXSAE8JyG9HsxkCoGQ6iX/CZlNdwGRKBWYYNP2g/sPeRtW6Fw4ZenyRVLWceASM+yG5Ih++6sNtRKc3LdVv1JQjriJCItdwM4v3eKzWhOp6XC9WLI3pxJQCf/osdC6LXRqwCRaK0Jp4P6J6jFY71pk7F1pNsodWDKMtd6RiJ+Yoc+KfohySPIp8JNkQlevsv4l9dOakuk+OdO3m+xh3I26/lVGNBp09FMJUUK7rV/vjUvEO+5HobiGu8TqYnnEzHt3WdGS6Bon3dfTTyMvHqSqvBHi2f+u7viaYrwDUf7hIwkBcO2BuFhPjFYbNIN11gd+9gXk7m50A1v4fOX0oPxdCFU+20Jzv/vVLw9zQb+gbXq3EiAh1k+fdmx1cCa0Wg47r+znqCFdYgV9OA4/EuL32YBY4Rs+96Ezwg5bF5YcvyqSlYwheF7qxh6j8SK5kHjsj6/B98wMA1vBUXd1Z4WoEDSwkkO04CckMC5BhcrFq1N6Jh3N+uXCnw5HV2hNZO7CxVSEaUAsb4OmJYn7p32AGa3NaZPx4bFmH8DjvFviubTWjK8g3Mm35p8AL+zYNFz2MY7oNnMj+Mtm9AvC5vAohvRxglKMfmbF/5MKUaxn2l/DhEX08pUvqcdiub4NnbU+60gm8JYFgCa1/+YkituL+vHYzgHwQ4G+w9IGQUD/e9tvQHUhR2QzhhHh3l40RLyILgts+/Uf+KoDizjk+Q/KnjFKCaerAKRXc8oeghFQ7SsFMAfgOhBlq2NXAV8EcM02frZyYzRER35sYVR/TEJ4NN2ieTuRxGeKCpfpoHON8tlVPCjtNfcxhDpJm4AxvtuNEALV4llVEXfQsUjXl916KF4oQ/kdA0QrrZeiqYPiA2/U6cItEAPSjqmWhYuMBAGkAfJpxxpG444tbM77NbEZp+QW0VF5uUzA5NH95APiFT8FjKPEnfAbRbGDQsdKN1e9GGk9GcYr68wDWA6zsds90avmnwWXjXImtmBJwt967O2BoRK/axoTDqptSPMKzhRkWM2mSOIOz799D3mrfsnsbTInUqUYwnGsyNG+yCmFGA2+MUdX/wAuqPjKakggI/mhAUP7f1ggfF2i/cfWFluFamiX+66HTB+jB5ODrmFBE/oz7vW5WdN54KfKTPbt2mjvsZgxJsfsHZU9yz4wjy94J4suKa2xlfCMf+ijiHiIz8sIgpzaVdZJ72EFtTQDrTFLxvn5I/NIKtoq0lk6szhSP65+ilUythWTz8PIHQauqOu5F8q83qA7kB2hwR29b8FsSq0bzIKvX89hsX0epDL5gX+WAYnPsFseqKPjbrBCKMBrqueYdRFXH/U7jQ+nzX/kouDxm9wpdWa6OphXaaanjxmQgSbHWllp2uXdJwac7E7g5mX5v9vCNBGW2D5Kwbk6HvVmf81fj+b/mgB6oHMRMbC+9L+BEb0JRkjuzQgnKylPqKpHtuhDPn3R6iCq+K4EysSPpGSC7R7MxcdArTjqYpS8rGSz8OtiQf91TbpjbkgCMbOLe82m6UUZgoOw6cg8z6X6/PItv/VwCdrsu8wOzBz1ZARpstIxImXzTFu0gLv7Uq9dVkxAajNdvbXJmzFrg1ZAXKaQrrhiOBRvjpiQb99bRfCMDd3xNLTnEjB1/1l/P9dJXVSUDRV6yuxfMLcEUw8ggIJbdM1uGfVSgupEY1ggJaPhMY5sCl/RwAg/XccZs3tSaf0k9IFkVg+3ISkWnQRaMvr9JcSC04W2L4uhEUBrc35Y+nXnihyStC6eJ33p1Q/Qu2KrhZHFssgPFU7ql8uRlRobq/VSdp7fD7NlYFRbBINbGnptqgh5CsA2pEC6XLXOhFkRrQKNXw1AvmLc+XVO0i3QZc5vbTOGgDMj6EF2lvgoJWX+zGcw/T5kooWnfS2RcUYEP4YxamWsq0khkgPvmubaaYub8eBDW8yzhkSYw9K5HJT6lzKjuk4p17d+dReaarAxKrp/X5bGseqLHGQMgvoRmcttLRbsprGpB7PAcZiLN1vZvmLICJSDruP+9AFi2RDyY1NksBK6k5nxCSFd79WIQleLS/ZBo8LGKwHcbJIev4Vy9/kTUXpl9gRqNNQD+j7otxXSA4p2bIcNV7s+uIMGz6+TLIxf8TmYDtVMthw/Uy0SIiCTsQRx/VQPx6qcPXHWvYQ5l6Hy5k5kh3QnvBE4mffgWY/angERW1TzPHP6CEmsznIjXyC3gjkhjNZNxPZNpqRRpFuHAbDrUfZZhjJxo5n6ZPCejP7DTPXyWLkCo8mxto1vefIl1i5UDSBoMrOneCs33czC1hvBWQsxXd1vPh/dnu0R0/1kCnjJdkhk1mSXVpG5XBAa1Yy5TSt3dTqfZsdsBA/IkbiwtkHrTJSktJhfBlDNBNy8q4/OD7y1TuiZJk7bwsOswG4ijSzTuS6ilU63POY3lVexMw63J/VowfCNV8K9N+kt5H0wPAIVx97YbKWqkZTpfQhKtTqGEIqymXbhc763rtfE+kMj07tUUgwmHibGpgxHKSCi4UM8pgjlqD8eV/Fku1mDxRnjoCpnlPwgDMUZWAP6XrDvDMg0O7dO2UELQSeBopuyJB6ZwN/Eg7NKHKe7CuQe4fDpYS5aF/rhd/sFzTxTZyxjlmmgx3HhIC6Opp4O5P9yrb4680liD5jDse+vco2keJnT3mtpFsXi8bPNrYRGVBlfMop81MXvr6sYA9R33NJxKndk6agWly2LtnEthpy0GXmoUn1GH3xIgnyF6VlTLvxjLc/KTtLTkpyC2mUwDgvP3fHbqVvScU/Ee13tguFz2J5jJjx87j1wPj8VZ7vkdfjavfBPxlRIxX26Ls4AjGb4/8ZI7JJ5RVo8UICwcVI0QGCFSk6fU089hqBlBKE9bJMmlFZcf3f1Kd9kQ6cS83nt/zwYKksxxhvOucj5Tt4bmApOgnm12fdC6WhVqvGGOuTXG7wSGYi5mbWckrlHiW1EgqgIxoQjR1OwZljRLUTgPd0EjQzGx+Q4EQ3x75TIS4Nt3G+4y440A4M9vsS/E6xXreRF0L3E6slGCR/jbaMTpBFkPzYsCIM4M90/c5+TP7rH8G/HXr/Y0du3NwSc5MCyAgTp5WQpjF7SRYU4HKVvYNHwSVt+gQfw0ptyVkGfHqejDczAFuiEK7FYmDxO63RfhY8KYbugTWfSIlO7lfjR99XYUJNg9myKK2r3cO+LixsJyS06iy+l2/0AiQFYlYraIYOSd9rcF3VU/qfSuy7fXGiC8oWCTyJJH0abvblxkM912Zm7Fj3FH0kUojsqMwebpWVN8PrPOMA2kfidUIupZLXoJHXWpK4AMEgEovEaZDRU0nnNvFKhGWbDvo8sMPImYcgeslp1JnBy3+PMzPNnkUoALSkmNMIYvZ3qyMbYaC6+fMEZurkx8ohcQDDJWgQlcBu8LePcZ6klSDuqDXg5CZ/yUWZ9rwynfLSDqbPabIaFIevqyK/B0CmXEenZLD3N0tfYNIJubRPZ5CQf6vWNgX0kVmjYjkvh8CFg54qPdFrI/Ei4A/5M7Sl1VZPKJXgCAjUXA1MGfkJPkxEjiVUp98+i4o0Y56mkCgAT40DOkO2wDaIMj8lJ/iuPdeyzrsBdq24T3e9K4Vlb+SqQhBUPfh0K04FkvJhgX9Gs6kycrE4MASMWzSCzY4uI6RT+TOFLtQbbzwoLfbTSPO5rYzaen/CJweyiqEP8AXVDgHBgHRahPYn8OEHbV5LT+eCcD44mUqXIUqOG4ImOChdAd96NnqdGErWuU1o7zlonERe18kSj/P7sh0hjKwArNVp5BNqihs8I1CMhtn1NNow/uOaT8ZZplw3o4yScnaE+jixHvCJWfg4EY7CYdmpYZcqA+6ncTMo0aQzoY5NCJyzx74JaWzmCbF9ohS109Hxf+N7vhcZrYz+26CmXr3cv/+QbiSVF76DUaoKaTxh4gXP6HHq2VT5Wu6Mcb/mHdV3i/QG19Ve3sohizudxlapjUvZECzazhgHu4wlrgNIx3zNhn/Q5XfbmbEfxm/3GAq3uTf5pBCbWEZgTj+lRbkFDc40L++CFicX2nrWLEdKuGk5aaY0R8FPRDjwZHJY8SOEGRYbEoh1dSH4fjx5BmIcFdMV5Leo3/FY1QX/+qgqOHzX6kS/4AVk+wh7dEa5TimSrd1Gb7TtFcpH5TYQBq/UZyJHYQQPjd3VCR6ssdAn6W61GJlLLoOXTwXXvj8eYqe/z87InRJgEHUMyf45BprphCUcc/1iKzoPTj8IJC02FGDNriolxA/MCN+DbQ86YiTRRBxok1vpUGu/HbVPu4tQHic55KPmX0YrjJdc9kan9S4borSBaxjY1CFRfXow9HUaNuJmsgxO1VthUbzx/0PSt+lf5kKGKgEUdxfQnfnnbcjAJXzQUsFpLAgPWDqjnfFwJoEXu6wBx7LF5Y8i5CVBAxeCEOe26q9ejJmQV52pNbPtfF8mN+rtF+NnGYOzny6Te8V+cJfJFbKdWdrEuCH6IZ/KIN289HLWn1xQDeBSVYsKTLhHFacS0fzZgaIVVYCDgON/mdbZR5SlOihbNHIr7z6hRrj38PVPwa/rL7SOegXm6YVVlB7grfkoWFCNpMeMfIzSWWcIme/yISx+/A7CaaoWe/FMkPVEtZfY0hZ2dJL4dNHuoQ0+rtkA4URRqsoRP+StEBdHmCGbrwkdog0a5FSgRZUSuxaqZd7DRC9Vyct1mpsumgJGYYjTpuERV2oT+njTAnoBd6cpJf7y5nmIWoOJuuGqQ/YZ2bqi7Wq4MGL7TkNVLr58GMShTHZEAOUYBEKSW/zvSBQr5JcZMOIgbn6aDDb9L/bXYsvFrVJZkLKpfUrEfJx4PqCdUQoDbTIeT9W8pEm9yghi2RNwFo0/bc+Y5sBaFfUjEnccnnurab9oE/QTHwIMKn/NueybwnfeHa8v+uKz5UiJP5Hpuhy8sJ4wgfb2BFQvyXyk0Ka+hu8UxljVcq8J4sx6miVaS6ONwb1UUu1mvy+Sz4eZWCEe81svialqrxRHileOPvMl9v2UTneEKvBR/O+JUAtVgwdx/xUE4w2+enT8qU8fduFBbF5XH6aUSewAl6QA5YC/4fT7vSvx6G/sIv6hPdOTAKEqaUpotOyfwP61Up/uVcDAMS53CzFfnBgbJOv/TiLM/b0Km4ByJOTHTFjlsbPYPeMJQErlzo3rYagu+0Lisk3hZVpLg49H0QWJGVFmb4Gm7yYAgU/jTasdMEaqf9nB0J/KLWsl5U8pm1JNh1XtfBkVWDQtX/1tNAdZdoWive3Xi+QZtIdxBu8/oE4gv2hG4vmGolutSPhwzibqLHaKkx3H7b/61+2q4ybl/NXfUAEfi26v+thbFoL3BcET6Xbiu0J5d7Ac3YMtGAta9l1ICRGb/j0bhuNHtLP5PmIPQN2++X4zEzGaHqoA8U9QYvrUDu8/lemI2+JnDX4IUUCvPMkbL032JIMGisrnGw5Va3p6firGWuHOZnilvZMeDd2x0KleB7hI1Bi3c2d4Gb/YSoIfzJI/Z9fzlIiONXXwRbXCeQFaUIfMpBsyxodyHuzFUg5veLcuqT6yKMzs2w6Ba2FJfx7O/uvePuWcS7H2w6JojLOJF9lFSGhMVmlIcm69e9UNd7pr+Y7c8cCExFZocaF0pcmMfgqJ1+PVPaJjVpqTuaLhSghDAJC1wI4K8VDY74PD2xBgQDYQstjlTlU5cHw7snP/u0jyD8uOvQHLsCInbrtWydlZtRfOYeI5NlAyDF9Dw1XTe7ikk32H75hH8WFnxN12GHJ0nR3Rs89an6ScVB7bnwI8tA5eoNEqDzD2PANxUYb/VMtFdoygpEposub2FRjFpqc9xX2aLntbhb60pKHwQ0djnS/PsR/nxEI77bisSfcASaqs5xNwKLvBBR/jd2NGpa5sUeWQBBzubqrmSLoBE5l9LMuEQJ5Awk7CP42XJFptjlj66vOxeyO2sJc/C7d2SKTboqGmX4689GT8Il5qLaukSK2BM5ApYaC8XHe7USPyNhFCJ9j6oKqrrEfZXeXjL+DbhGam/QHqvvIHDbKwmzUBEeGlLrLPL2JPTxoaDBm5zSSkM7xNY8094ZSj/O8zkWqh1IO0xzndcU2MHjBvmEKU6RLawuzOc9nes5Iot+7Bnz0T54FlrVrVJYfsFmiI4XV2IO5L6l/fF70jeTi2991EyFd6prRKhbA/AWjt22DamMITLJR4jD8jSrALn0FzrFrbfEkADsZeFRrGA+cwblyMnkvuDeXkxjqFcytcN8XCW0N1N9pK3IkUzHNwrxuXmb5PWCBiTIOet/VY730+8/JaUTxwJ0Rt45TdcOvQMZnyjIz60ZU9wV/taGZnPHnahxGjt43clKu2Ueqys3DEPkwCr8R1FKo3iIA8ZT3Pi3HmP1GFrBsqxukdKWrzI5tcnD+BH6BZcw5DfBDcqjom2eSCTPhtYdkyTd+/chbwgPZm/RZ0rVVriFjw0mrwJbT6AFmfmtFdBsLAlHBH8go2tvF1vrnqa7k8K8UDyWH5JczhQplMjRR/WVLmO5OX/o4hFfe7oTd7pjLyUxCi/LvMHMgr9LjNwxO5Ys/MFiGY1HFsQzSHLaXv4sxKnMj594Kg4W7RcKbHSUZ98AGhakNLYGg3D/RqvWqavC+cBQI+Z9xMEXCfQaOUE+KuYO4qPa3CFQ7n/EstVCA5oGwUf+mdDkMqd9lfYGOxFuXXWruCc+ZveHP5YQPNtaaQVqFk9n0FryyUnROTiJpAQV/TyNPQqQFK++aAh3UlRyzqXPXYx6uz26b2xFwWrdMRuLjE5oK+yEFec+w1FWcv1qaQYNeixVWtIieUIQSj01oIyvd4RwmGoYYt/0FN7AIEd+qNtdb7AGbcG4mSHzsJXPthXsljXJfzs9/JUPftdH5RfxOdPKtrPdWubVZMCxq/we2CBcilpnq561lJn8m6zdeUUI0lIyBw4DDE3jBfTNfiAjp9Y2fhBj0mv2/mNozUHUG+i4B9v3y2tHQtgIZlGJcLEy60XN6hxEswxp1o/zCvFyewIDIFrerVUJxEh0iiaxYI7HIy7rd6J2K3PfO0JxCbgeoR+YecUBBcgG+KP3FaClzoU2WDsUqCLEUx2LZFCSouD4yWGicBlmEI4rmOTPIy1EcfYDJuywT7muHXPxYzP3OuECmyxc+4mS3gw1X8dpAu8No7uDxGXb9sxqw2HRvRzuc3TB/FNfbHcBeruTKgtqBH6pHjRw+q7V4t3/SktOkLI2Wq/84d+L+JowQ9hNob7ktT8N4EHUs91jipbLlFr2H3nTxV8pbvpWShEV5xxONSqqV4XhxusGbqT1VZYGSK6xCXJjbu2sV40ULVqQRHVl+4xfWYVctgRV+5GjqWBy4exn7VLsRny5Hmkn6S/Lr3XywfCAHR791iNM0pRpWa4kJcr+ubhtgz30kQ6hQFfwEugGLyzec0GnmUhJtaOU3fFcsTdnjPhylUoMXUiYknF3X8bADju/o1di3pgipHEUdQoE+70qiwPFpIB67JqzJ5WCNq1RxppktoWu6PSy0fGQcClJlBn7dA2oPIKbUwXDsXo2yYbbhDQhKTO71LQR6Oa5T2v6A7VZ8UNvMWqC3yLexOZTUo/+tYDqFpoydhbReTYqdaKGYa7paQpBG0nsmU3B/T/w/KStOZTkr0MuEtFaS5NpUGLOB5mInkM3czp9GViHWhp779lfnlG03He+UHry3J8QNAYPDZ+qjlc0OYWrAKG4W3JttHg2NF1qXZS87jJmAxyPgt2Tc6j/XNK5CzRIvAWSk2tELmQGWOVtoNMCBA6Ew6olJcf33l/+/n8mxIa4sicoz749WJVW0AkfcsOJDXfxGiH97LyPKs/hKefedAxJj6I4sWMKbgxyobj6fHAxzY1fBFlFth4FaP88AuVAT/x9UhPVf6o8wBk93wKIffXXl/MLax2c/9jmw3VeUiWnRfP1PbGCA6+aDCmd0EDXKynbC81FemqYj0z0we8wB9dfOBylOMHC4i9aQiU0n7HJKOLS1jNBdD0OpFZbi6HhQdT/p7JgCZx7KIHzCgPDz2fJICN65PxJrMkE9UW7n12jC+DuhGc3xGCmT17pf9ys1X6Ee/JgdjsD8v9i76Nj5fZ6r99pe6aAzseKOgY1uCSENCjWJvJRKLMrhVN0VO4Tbv+kOROdZCBcXLhqV8G4XFaiZM+LPcX8=
        - #2:
          - type: tool-call
          - toolCallId: TaAuGzGEmTsSA7rH
          - toolName: set-policy
          - input:
            - Policy: Free Thought (Continuing Rationalism Branch)
            - Rationale: Adopt Free Thought to accelerate Great Scientist generation by 33% and boost their instant yields, which is critical for driving our tech progress toward the Spaceship Victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: EoPsvGkhG7GeRmpj
          - toolName: set-relationship
          - input:
            - TargetID: 4
            - Private: -80
            - Public: -80
            - Rationale: India is extremely close to a cultural victory and is our active war target. We must maintain maximum hostility and press our military advantage to capture their cities and permanently halt their cultural threat.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: C9UyeuBYLYH3bPMK
          - toolName: set-relationship
          - input:
            - Rationale: We share the Autocracy ideology (+999 modifier). A friendly stance will help defuse Germany's hostility, prevent them from attacking us when the peace treaty expires in 2 turns, and keep our focus entirely on crushing India.
            - Public: 40
            - TargetID: 6
            - Private: 40
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: coHFA5WNR36KPx8n
          - toolName: set-persona
          - input:
            - Loyalty: 9
            - WarBias: 9
            - Rationale: Maintain high boldness and war bias to aggressively pursue the conflict against India, while increasing loyalty to 9 to preserve and honor our defensive alliance with the hard-pressed Inca.
            - Boldness: 9
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: ZdUfddGX18QIeKC1
          - toolName: keep-status-quo
          - input:
            - Rationale: The current strategic weights are highly optimized for our Spaceship victory path, with maximum focus on science, production, and mobilization, which perfectly supports our simultaneous space race and critical defensive/offensive military operations.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: iGghDkTr4WGIO1cc
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
          - toolCallId: TaAuGzGEmTsSA7rH
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: EoPsvGkhG7GeRmpj
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: C9UyeuBYLYH3bPMK
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: coHFA5WNR36KPx8n
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: ZdUfddGX18QIeKC1
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.