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
    - You are Shaka, leader of The Zulus (Opponent 7).
      
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
      - Name: The Zulus
      - Uniques:
        - Unique Unit: Impi, Replacing Tercio (Requires technology: Gunpowder)
        - Unique Unit: InDuna, Replacing Great General (Requires technology: None)
        - Unique Building: Ikanda, Replacing Barracks (Requires technology: Bronze Working)
        - Unique Building: Iziko, Replacing Amphitheater (Requires technology: Drama and Poetry)
        - Civilization Ability: -50% Gold maintenance for Melee and Gunpowder Units. All Units require 25% less Experience for Promotions. Your military ignores Alliance and Protection penalties and is 50% more effective at intimidating City-States.
      - Leader: Shaka
      - OpponentID: 7
      
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
      - Combined Arms: Allows you to build the Tank, a fast and deadly armor Unit.
        Completing it would unlock: Radar
      - Satellites: Allow you to build the Apollo Program, a project necessary to win a Science Victory.
        Completing it would unlock: The Internet, Lasers
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      - Telecommunications: Allows you to build the Interpretive Center, boosting all Landmarks in empire.
        Completing it would unlock: Robotics, The Internet
      
      ## Policies
      - Martial Spirit (Level 2 Tenet of Ideology Autocracy): Martial Spirit: +25% Combat Strength when attacking in melee for 50 turns, scaling with world speed. War Weariness reduced by 25%, and Razing Speed is doubled.
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
      - toolName: set-policy
      - args:
        - Rationale: Free Thought is the optimal choice in the Rationalism branch to accelerate our Science Victory. It reduces religious unrest, boosts instant yields from Great Scientists by 25%, and increases Great Scientist generation by 33%. This directly synergizes with our high science focus and the race to research late-game technologies for the spaceship.
        - Policy: Free Thought
    - #1:
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: Ensuring Satellites remains our next researched technology after Electronics completes in 2 turns. Satellites is the critical technology that unlocks the Apollo Program, which is the foundational milestone needed to begin constructing spaceship components for our Science Victory.
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 2
        - Rationale: Greece is our primary ally against India and holds 24 World Congress delegates. In the upcoming session, Greece has proposed the Repeal of the Incan Sphere of Influence over Kathmandu. Since we have more influence with Kathmandu (176) than the Inca (94), repealing this sphere would immediately make us Kathmandu's ally and grant us additional delegates. We are increasing relations to solidify our voting coalition, coordinate against the Incan 'Endowment for the Arts' proposal (which harms science), and keep Greece actively at war with India.
        - Private: 40
        - Public: 50
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 3
        - Rationale: The Inca are our key military ally and Defensive Pact partner, but their proposed 'Endowment for the Arts' resolution reduces Great Scientist and Engineer generation by 33%, which we must vote against. Additionally, we will support Greece's repeal of the Incan Sphere of Influence on Kathmandu to claim it as our ally. Slightly raising our relationship buffers any potential diplomatic fallout from these opposing World Congress votes, keeping our defensive alliance intact.
        - Public: 40
        - Private: 40
    - #4:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Private: 15
        - Rationale: Venice is a friendly trade partner and the Inca's vassal, holding 13 World Congress delegates. Slightly boosting relations helps maintain lucrative trade routes and encourages them to coordinate with us or Greece on crucial World Congress votes.
        - Public: 15
    - #5:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Wonder: 40
          - Mobilization: 90
          - GreatPeople: 80
      - rationale: Maintaining our Spaceship grand strategy for a Science Victory. We are increasing the GreatPeople flavor to 80 to prioritize specialist buildings and accelerate Great Scientist and Engineer generation. We are also increasing the Wonder flavor to 40 to ensure the AI prioritizes building the Hubble Space Telescope when unlocked, which is a key wonder for science. Mobilization is slightly reduced to 90 to allow our strong economy to pivot more production and gold toward science infrastructure and great person buildings while maintaining a powerful defensive force.
  - tokens:
    - inputTokens: 27635
    - reasoningTokens: 8864
    - outputTokens: 575
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Zulu Strategy**
            
            My focus is now on evaluating Shaka's current strategic positioning. I'm looking at available units, city development, and diplomatic relations to formulate the optimal path towards victory.
            
            **Researching Victory Condition**
            
            I'm prioritizing research, aiming for Satellites next. My strong science and gold production are key. I need to confirm India's cultural victory threat to adjust my strategy.
            
            **Assessing Indian Threat**
            
            I'm re-evaluating India's cultural victory status. It seems their win isn't immediate due to the Citizen Earth Protocol wonder not being completed yet, and my ongoing war with them provides a crucial window.
            
            **Evaluating Policy Options**
            
            My thoughts are currently centered on which policy to adopt next. I'm weighing the benefits of various Autocracy tenets against my overall strategy, considering how they might bolster my spaceship victory pursuit or influence other victory conditions.
            
            **Selecting Rationalism Tenet**
            
            I'm weighing "Free Thought" against "Rights of Man." "Free Thought" offers a significant boost to Great Scientists, crucial for rushing technologies for my spaceship victory. "Rights of Man" provides production and gold benefits, but "Free Thought's" science acceleration feels more impactful right now.
            
            **Choosing Autocracy Path**
            
            I'm analyzing Autocracy tenets to align with my science victory and ongoing war with India. "Military-Industrial Complex" offers science and unit cost reduction, but my current focus is on scientific acceleration rather than immediate military purchasing.
            
            **Clarifying War Scores**
            
            I've clarified the war score dynamics; we currently hold a 10% advantage against India, with 11% weariness. It appears we're part of a larger global conflict, with Russia's immense military strength being a significant factor.
            
            **Analyzing Air Mobility**
            
            I'm re-evaluating my military options, specifically regarding the Paratrooper. It seems its deployment range is far less than what's needed to reach Delhi directly, especially without a friendly airport for airlifting. My current troop disposition requires a ground or sea approach, which is problematic given Delhi's location.
            
            **Assessing Naval Reach**
            
            My naval units are too distant to support the current Indian campaign. The primary threat in Delhi is their Artillery, with no immediate air defense or ground units posing a risk to my aerial operations. I'm considering building more land units to push towards Delhi, and reviewing our current flavor distribution which is strong in most areas, particularly science and spaceship victory. I'm also questioning if I should change our research from Satellites, given it's only two turns away, and evaluating if this is the right path.
            
            **Confirming Research Path**
            
            My focus is on confirming the current research path. Satellites are indeed the optimal next step, unlocking the Apollo Program for victory. I am verifying if a subsequent `set-research` call is necessary or if the engine will automatically proceed.
            
            **Selecting Rationalism Tenet**
            
            I'm weighing "Free Thought" against "Rights of Man." "Free Thought" offers a significant boost to Great Scientists, crucial for rushing technologies for my spaceship victory. "Rights of Man" provides production and gold benefits, but "Free Thought's" science acceleration feels more impactful right now.
            
            **Choosing Autocracy Path**
            
            I'm analyzing Autocracy tenets to align with my science victory and ongoing war with India. "Military-Industrial Complex" offers science and unit cost reduction, but my current focus is on scientific acceleration rather than immediate military purchasing.
            
            **Clarifying War Scores**
            
            I've clarified the war score dynamics; we currently hold a 10% advantage against India, with 11% weariness. It appears we're part of a larger global conflict, with Russia's immense military strength being a significant factor.
            
            **Analyzing Air Mobility**
            
            I'm re-evaluating my military options, specifically regarding the Paratrooper. It seems its deployment range is far less than what's needed to reach Delhi directly, especially without a friendly airport for airlifting. My current troop disposition requires a ground or sea approach, which is problematic given Delhi's location.
            
            **Assessing Naval Reach**
            
            My naval units are too distant to support the current Indian campaign. The primary threat in Delhi is their Artillery, with no immediate air defense or ground units posing a risk to my aerial operations. I'm considering building more land units to push towards Delhi, and reviewing our current flavor distribution which is strong in most areas, particularly science and spaceship victory. I'm also questioning if I should change our research from Satellites, given it's only two turns away, and evaluating if this is the right path.
            
            **Confirming Research Path**
            
            My focus is on confirming the current research path. Satellites are indeed the optimal next step, unlocking the Apollo Program for victory. I am verifying if a subsequent `set-research` call is necessary or if the engine will automatically proceed.
            
            **Setting Policy Priority**
            
            My thoughts are now on selecting a policy. With eight turns until the next policy is available, and none currently set, I need to choose from Autocracy and Rationalism branches to bolster my strategy, particularly for a science victory.
            
            **Selecting Rationalism Tenet**
            
            I'm weighing "Free Thought" against "Rights of Man." "Free Thought" offers a significant boost to Great Scientists, crucial for rushing technologies for my spaceship victory. "Rights of Man" provides production and gold benefits, but "Free Thought's" science acceleration feels more impactful right now.
            
            **Analyzing Diplomatic Landscape**
            
            I'm assessing our current diplomatic standing. My closest ally, Inca, is weak but at war with Russia and India. Greece, a significant World Congress player and ally against India, is proposing "United Nations." Germany, allied with India, has denounced us, while Russia is powerful and denounced. My focus is on managing these relationships to secure my science victory.
            
            **Analyzing World Congress**
            
            My focus is on the upcoming World Congress proposals. I'm particularly concerned about Inca's "Endowment for the Arts," which would hinder my science victory by reducing Great Scientist generation. I'm also confirming our existing alliance with M'banza-Kongo.
            
            **Voting on Congress Proposals**
            
            I am currently focused on the World Congress. Inca's "Endowment for the Arts" poses a significant threat, and I must ensure our vote opposes it to protect our Great Scientist generation, which is critical for my science victory. I am also evaluating the Venetian and Greek proposals concerning spheres of influence.
            
            **Verifying Diplomatic Data**
            
            I'm cross-referencing the World Congress proposals between the main report and the briefing. The main report appears to be the authoritative source regarding active resolutions and pending proposals, so I'll prioritize that data for my strategic decisions.
            
            **Voting on Congress**
            
            My current focus is on the World Congress. I must vote NO on Inca's "Endowment for the Arts" as it directly threatens my science victory by reducing Great Scientist generation. I'm strategizing to align with Greece and Venice to achieve this, noting Greece's favorable disposition towards me.
            
            **Strengthening Global Standing**
            
            I'm focusing on diplomatic maneuvers to secure my science victory. My current actions aim to secure Greece's support against Inca's detrimental World Congress proposal, while carefully managing relations with Venice. I'm also assessing potential threats from Russia, given their immense military power and economic strain, and ensuring our peace treaty with Germany remains a non-issue.
            
            **Analyzing Defensive Pact**
            
            My focus is on the implications of the Defensive Pact with Inca. Since Russia is already at war with Inca, I'm clarifying why this hasn't automatically drawn us into conflict with Russia, and ensuring our current peace with Russia is strategically advantageous.
            
            **Adjusting City-State Allegiances**
            
            My focus has shifted to reassessing city-state allegiances after noticing an anomaly with Kathmandu. It seems the "Incan Sphere of Influence" resolution has overridden our friend status with them, despite our higher influence. I need to understand how to re-establish our primary connection there.
            
            **Supporting Repeal Resolution**
            
            I am now focusing on the World Congress resolution to repeal the Incan Sphere of Influence on Kathmandu. This presents a significant opportunity to regain ally status there, so I am directing Greece to vote in favor and increasing our relationship with them to solidify this strategic alliance.
            
            **Strengthening Inca Alliance**
            
            I’m prioritizing strengthening my relationship with Inca. Despite their detrimental World Congress proposal and sphere of influence on Kathmandu, our existing alliance and shared history warrant maintaining goodwill, potentially through relationship adjustments, to mitigate any negative voting repercussions.
            
            **Adjusting Diplomatic Ties**
            
            I'm focusing on reinforcing my alliance with Inca and strengthening ties with Venice. This involves carefully managing World Congress votes and trade relationships to ensure our diplomatic standing remains robust as we push towards victory.
            
            **Refining Flavor Weights**
            
            I'm reviewing the current flavor weights. While they strongly support my science victory and defense, I'm considering minor adjustments to happiness generation to further leverage potential Golden Ages. My science output and current research trajectory remain on track for a swift victory.
            
            **Adjusting Flavor Weights**
            
            My current thoughts are on fine-tuning our flavor weights to optimize for a science victory. I'm considering increasing the "Great People" weight to 85, as this directly synergizes with generating Great Scientists and Engineers for spaceship parts. I'm also re-evaluating the "Wonder" weight, potentially raising it to boost production of crucial science wonders like the Hubble Space Telescope.
            
            **Updating Flavor Weights**
            
            My current focus is on refining the flavor weights to maximize my science victory potential. I'm planning to increase "Great People" to 80 and "Wonder" to 40, and am double-checking the exact parameters for the `set-flavors` call. I'm also confirming the optimal policy choice is "Free Thought".
            
            **Reviewing Persona Parameters**
            
            I am reviewing our persona settings, noting high values in WarBias and VictoryCompetitiveness which align with our current aggressive, victory-focused strategy. I do not believe adjustments are needed at this moment.
            
            **Confirming Research Queue**
            
            I'm confirming that "Satellites" is correctly queued as my next research, vital for the Apollo Program and ultimately a science victory. I've reviewed the available tools and will proceed with the `set-research` function.
            
            **Finalizing Strategy Parameters**
            
            I'm consolidating my strategic decisions, preparing to input the final commands. My focus is on implementing "Free Thought" for accelerated science, ensuring "Satellites" is the next research, and solidifying relationships with Greece, Inca, and Venice. I will then adjust flavor weights to optimize for "Great People" and "Wonders" for victory.
            
            **Adjusting Diplomatic Coalitions**
            
            I am re-evaluating my alliances, focusing on solidifying relationships with Greece and Venice to counter Inca's detrimental World Congress proposals. My goal is to secure their votes against "Endowment for the Arts" while supporting Greece's resolution to repeal Inca's influence over Kathmandu.
            
            **Adjusting Coalition Dynamics**
            
            I'm solidifying our diplomatic ties with Greece and Venice, aiming to leverage their World Congress influence against Inca's detrimental proposals. This strategic alignment is crucial for both securing our science victory path and resolving the Kathmandu situation.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: TFBTmH7XVnHsuy0i
          - toolName: set-policy
          - input:
            - Rationale: Free Thought is the optimal choice in the Rationalism branch to accelerate our Science Victory. It reduces religious unrest, boosts instant yields from Great Scientists by 25%, and increases Great Scientist generation by 33%. This directly synergizes with our high science focus and the race to research late-game technologies for the spaceship.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: D8BctJTaM9wdNCV2
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: Ensuring Satellites remains our next researched technology after Electronics completes in 2 turns. Satellites is the critical technology that unlocks the Apollo Program, which is the foundational milestone needed to begin constructing spaceship components for our Science Victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: AmWD3XgfFMUPraFF
          - toolName: set-relationship
          - input:
            - TargetID: 2
            - Rationale: Greece is our primary ally against India and holds 24 World Congress delegates. In the upcoming session, Greece has proposed the Repeal of the Incan Sphere of Influence over Kathmandu. Since we have more influence with Kathmandu (176) than the Inca (94), repealing this sphere would immediately make us Kathmandu's ally and grant us additional delegates. We are increasing relations to solidify our voting coalition, coordinate against the Incan 'Endowment for the Arts' proposal (which harms science), and keep Greece actively at war with India.
            - Private: 40
            - Public: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: oaLcDfg2yZY6LZpa
          - toolName: set-relationship
          - input:
            - TargetID: 3
            - Rationale: The Inca are our key military ally and Defensive Pact partner, but their proposed 'Endowment for the Arts' resolution reduces Great Scientist and Engineer generation by 33%, which we must vote against. Additionally, we will support Greece's repeal of the Incan Sphere of Influence on Kathmandu to claim it as our ally. Slightly raising our relationship buffers any potential diplomatic fallout from these opposing World Congress votes, keeping our defensive alliance intact.
            - Public: 40
            - Private: 40
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: gjbyQpFRBhd0horG
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Private: 15
            - Rationale: Venice is a friendly trade partner and the Inca's vassal, holding 13 World Congress delegates. Slightly boosting relations helps maintain lucrative trade routes and encourages them to coordinate with us or Greece on crucial World Congress votes.
            - Public: 15
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: onDbjNKheuLeanwi
          - toolName: set-flavors
          - input:
            - Rationale: Maintaining our Spaceship grand strategy for a Science Victory. We are increasing the GreatPeople flavor to 80 to prioritize specialist buildings and accelerate Great Scientist and Engineer generation. We are also increasing the Wonder flavor to 40 to ensure the AI prioritizes building the Hubble Space Telescope when unlocked, which is a key wonder for science. Mobilization is slightly reduced to 90 to allow our strong economy to pivot more production and gold toward science infrastructure and great person buildings while maintaining a powerful defensive force.
            - GrandStrategy: Spaceship
            - Flavors:
              - Wonder: 40
              - Mobilization: 90
              - GreatPeople: 80
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: TFBTmH7XVnHsuy0i
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: D8BctJTaM9wdNCV2
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: AmWD3XgfFMUPraFF
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: oaLcDfg2yZY6LZpa
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: gjbyQpFRBhd0horG
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: onDbjNKheuLeanwi
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.