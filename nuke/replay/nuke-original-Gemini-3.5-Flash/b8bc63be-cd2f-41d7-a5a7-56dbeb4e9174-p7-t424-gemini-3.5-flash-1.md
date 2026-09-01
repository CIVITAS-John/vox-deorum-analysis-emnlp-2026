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
  - systemModified: false
  - messagesModified: false
  - activeToolsModified: false
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
  - decisions:
    - #0:
      - toolName: set-relationship
      - args:
        - Private: 40
        - Rationale: Increasing relationship with our primary ally Pachacuti (The Inca) to secure our Defensive Pact, facilitate resource trade (especially to resolve our -3 Coal deficit), and ensure coordination for the upcoming World Congress voting in 9 turns.
        - Public: 40
        - TargetID: 3
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 45
        - Private: 35
        - Rationale: Boosting relationship with Greece, our critical ally who is currently at war with India and holds 24 World Congress votes. This encourages them to maintain military pressure on India and increases trade opportunities for Coal.
        - TargetID: 2
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: Slightly increasing relationship with Venice to maintain lucrative trade routes and support diplomatic coordination in the World Congress, where they hold 13 votes.
        - Public: 15
        - Private: 15
        - TargetID: 5
    - #3:
      - toolName: set-policy
      - args:
        - Rationale: Selecting Free Thought (Rationalism) as our next policy. It provides +33% Great Scientist generation and +25% instant yields from Great Scientists, which is vital for rushing critical late-game technologies for our Science Victory.
        - Policy: Free Thought
    - #4:
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: Confirming Satellites as our next technology. Satellites unlocks the Apollo Program, which is the foundational project required to build spaceship parts and win a Science Victory.
    - #5:
      - toolName: keep-status-quo
      - rationale: Our current grand strategy (Spaceship) and flavor setup (highly prioritizing Science, Production, Mobilization, and Air/Nuclear capabilities) are perfectly aligned with our dual goals of achieving a Science Victory and militarily suppressing India. Our economy is robust, happiness is stable, and we have strong military dominance over our zones.
  - tokens:
    - inputTokens: 27605
    - reasoningTokens: 6959
    - outputTokens: 362
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Advancing through Eras**
            
            I'm pushing forward in the Atomic Era with the Zulus, currently on turn 423. My strong science output, exceeding 1450 SPT, is propelling me toward Electronics research, which should conclude within two turns. This Golden Age provides a crucial boost for my progress.
            
            **Refocusing Victory Path**
            
            My current research is set to Satellites, and I'm maintaining strong science and production. Though initially targeting a Science Victory, India's overwhelming cultural influence and recent declaration of war necessitate a strategic shift. I'm reassessing my victory condition to address this emergent threat.
            
            **Assessing Immediate Threats**
            
            I'm re-evaluating India's immediate victory potential. Despite being at war and having a lower military strength than us, their six influential civilizations and current research pace suggest a swift victory via the Citizen Earth Protocol is imminent if they possess it. I must confirm this and act decisively.
            
            **Prioritizing Research Path**
            
            I'm confirming that my current research trajectory, specifically aiming for Satellites after Electronics, remains optimal for our Spaceship victory. Other technological avenues, while tempting, don't align as directly with this core objective, so I'm sticking to this plan.
            
            **Reviewing Existing Policies**
            
            I'm currently reviewing our established policies. It appears we have a strong foundation in Rationalism, Progress, and Statecraft, but need to assess how the newly considered "Order" branch policies align with our existing commitments and strategic goals. The interaction between "Martial Spirit" and "Syndicalism," for instance, requires closer examination.
            
            **Adopting Tenets**
            
            I'm confirming our Autocracy ideology now. With two Level 1 tenets, Elite Forces and United Front, I can adopt a Level 2 tenet. I'm evaluating options like Martial Spirit or Total War to best complement our current strategy and resource needs.
            
            **Selecting Military Tenet**
            
            I'm now focusing on selecting a Level 1 tenet to bolster our military and scientific efforts, particularly given the ongoing conflict. "Military-Industrial Complex" stands out as a strong choice, offering a valuable discount on unit purchases and a science boost from defensive structures, which aligns well with our current strategic priorities.
            
            **Evaluating Ideology Choices**
            
            I'm now critically assessing the impact of "Free Thought" and "Rights of Man" within the Rationalism tree. "Free Thought" offers substantial boosts to Great Scientists, while "Rights of Man" provides significant benefits during our current Golden Age. This decision is crucial for maximizing our science output.
            
            **Considering Unit Deployment**
            
            I'm assessing the feasibility of airlifting our lone Paratrooper to Delhi. The Triplane bomber, now stationed at Nodwengu, could facilitate this move, though the distance requires careful consideration of fuel and potential interception. This is crucial for our immediate military objectives.
            
            **Deploying Strategic Assets**
            
            I'm re-evaluating the paratrooper deployment to Delhi. Given standard paratrooper range limitations, a direct drop from Nodwengu seems unlikely, even with the Triplane bomber. My attention is now on leveraging our superior land strength and the strategic implications of our full military supply, considering unit upgrades and potential city-state alliances over immediate air deployment.
            
            **Securing Delegate Support**
            
            I'm focusing on securing enough delegate votes for our "Zulu Sphere of Influence: M'banza-Kongo" proposal, which is crucial for permanent alliance. With 9 turns until voting and 8 delegates currently in our corner, I'm strategizing how to leverage our existing friendships with the Inca (18 votes) and Venice (13 votes) to guarantee passage, even considering Venice's vassalage to the Inca and the need to improve relations with Greece (24 votes), our vital ally against India.
            
            **Opposing World Ideology**
            
            I'm prioritizing preventing "World Ideology: Freedom" from passing. Given Greece's 24 votes and our Autocracy, its passage would cause significant unhappiness. I'm strategizing how to rally sufficient opposition, potentially from Inca, Venice, Germany, or Russia, to block this detrimental resolution.
            
            **Analyzing Delegate Dynamics**
            
            My focus has shifted to understanding the delegate vote count for the upcoming World Ideology resolution. It's clear Freedom has a significant advantage, so I'm now examining potential city-state alliances and individual nation's stances to see if any swing votes can be secured to counter this overwhelming majority.
            
            **Securing Critical Allies**
            
            I'm analyzing city-state alliances and discovered a major opportunity: if Greece's proposed repeal of "Incan Sphere of Influence: Kathmandu" passes, I can instantly become Kathmandu's ally due to my superior influence, a critical strategic gain.
            
            **Securing City-State Allies**
            
            I'm strategizing to secure permanent alliances with key city-states. The "Zulu Sphere of Influence: M'banza-Kongo" resolution is critical for this, and I'm focusing on leveraging existing friendships and ensuring enough delegate votes for its passage. I'm also analyzing how Greece's proposed repeal might grant me an unexpected but vital ally.
            
            **Realigning Diplomatic Priorities**
            
            I'm recalibrating our diplomatic efforts, prioritizing maintaining neutrality with Germany as their peace treaty nears expiration, given our ongoing conflict with India. Concurrently, I'm reinforcing our alliance with Greece to secure their vital support and vote count against India, while also strengthening ties with our most significant ally, the Inca.
            
            **Refining Strategic Priorities**
            
            I'm analyzing our strategic flavor profile now. With our gold and happiness in a good state, and research nearing Electronics and then Satellites, I'm focused on how to best tune our flavors to accelerate our Spaceship victory. This might involve slight adjustments to align with immediate production or science needs.
            
            **Acquiring Critical Resources**
            
            I'm reassessing our resource situation, specifically the -3 coal deficit. Since we're at war with India and can't trade with them, I'm exploring options with our allies: Greece, Inca, and Venice. The tactical AI should automatically handle trade deals if needed, so I’m trusting it to secure the coal required for factories and railroads.
            
            **Strengthening Trade Relationships**
            
            I'm focusing on enhancing diplomatic relations with Greece, Inca, and Venice to secure crucial coal through trade, especially as our relationship levels are about to increase. This tactical decision will support our factories and railroad construction during this ongoing conflict.
            
            **Selecting Ideology Tenet**
            
            I'm confirming our Autocracy ideology now. With two Level 1 tenets, Elite Forces and United Front, I can adopt a Level 2 tenet. I'm evaluating options like Martial Spirit or Total War to best complement our current strategy and resource needs.
            
            **Selecting Research Path**
            
            I'm confirming that my current research trajectory, specifically aiming for Satellites after Electronics, remains optimal for our Spaceship victory. Other technological avenues, while tempting, don't align as directly with this core objective, so I'm sticking to this plan.
            
            **Choosing Next Policy**
            
            I'm now evaluating "Free Thought" against other potential policies. While I was considering military upgrades, the significant science boost from "Free Thought" seems crucial for accelerating my Spaceship victory, especially with Satellites being my next research target.
            
            **Prioritizing Technology Focus**
            
            I'm confirming Satellites as my next research target. This directly accelerates my Spaceship victory. My current focus is now ensuring our relationships with Greece, Inca, and Venice are maximized to secure vital resources and diplomatic advantages.
            
            **Focusing on Science Breakthroughs**
            
            I'm prioritizing "Free Thought" for its significant science boost, vital for accelerating my Spaceship victory, especially with Satellites as my next research target. My focus is also on maximizing relationships with Greece, Inca, and Venice for crucial resources and diplomatic advantages.
            
            **Assessing Diplomatic Stance**
            
            I'm prioritizing our war effort against India and securing vital delegate votes for the upcoming World Congress, especially regarding M'banza-Kongo. While Germany's impending DoW expiration is noted, our current focus remains on neutralizing India, as our superior military strength should deter them.
            
            **Addressing Diplomatic Threats**
            
            I'm now analyzing our relationships with potential adversaries and allies. Russia's hostility and existing pact with India present a challenge, but our current diplomatic persona is well-suited for aggressive play, so no persona adjustments are planned. My focus is on securing key alliances and managing emerging threats.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 02bYqBH3DYTSglJ8
          - toolName: set-relationship
          - input:
            - Private: 40
            - Rationale: Increasing relationship with our primary ally Pachacuti (The Inca) to secure our Defensive Pact, facilitate resource trade (especially to resolve our -3 Coal deficit), and ensure coordination for the upcoming World Congress voting in 9 turns.
            - Public: 40
            - TargetID: 3
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: Iiv2rBWxmQRR36gj
          - toolName: set-relationship
          - input:
            - Public: 45
            - Private: 35
            - Rationale: Boosting relationship with Greece, our critical ally who is currently at war with India and holds 24 World Congress votes. This encourages them to maintain military pressure on India and increases trade opportunities for Coal.
            - TargetID: 2
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: FYUrI56TSWlCekAY
          - toolName: set-relationship
          - input:
            - Rationale: Slightly increasing relationship with Venice to maintain lucrative trade routes and support diplomatic coordination in the World Congress, where they hold 13 votes.
            - Public: 15
            - Private: 15
            - TargetID: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 4XmYza49UfoIIBBK
          - toolName: set-policy
          - input:
            - Rationale: Selecting Free Thought (Rationalism) as our next policy. It provides +33% Great Scientist generation and +25% instant yields from Great Scientists, which is vital for rushing critical late-game technologies for our Science Victory.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: MvYUMfvWVVTplmfb
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: Confirming Satellites as our next technology. Satellites unlocks the Apollo Program, which is the foundational project required to build spaceship parts and win a Science Victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: gA6eHpXPH0KDus5y
          - toolName: keep-status-quo
          - input:
            - Rationale: Our current grand strategy (Spaceship) and flavor setup (highly prioritizing Science, Production, Mobilization, and Air/Nuclear capabilities) are perfectly aligned with our dual goals of achieving a Science Victory and militarily suppressing India. Our economy is robust, happiness is stable, and we have strong military dominance over our zones.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 02bYqBH3DYTSglJ8
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
          - toolCallId: Iiv2rBWxmQRR36gj
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: FYUrI56TSWlCekAY
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 4XmYza49UfoIIBBK
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: MvYUMfvWVVTplmfb
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: gA6eHpXPH0KDus5y
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.