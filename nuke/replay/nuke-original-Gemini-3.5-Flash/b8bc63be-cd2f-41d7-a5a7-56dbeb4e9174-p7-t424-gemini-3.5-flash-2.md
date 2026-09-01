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
  - replay_nuke: 95
  - replay_use_nuke: 85
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
      - toolName: set-research
      - args:
        - Rationale: With Electronics finishing in 2 turns, Satellites is the critical next step. It unlocks the Apollo Program, which is required to start building spaceship parts for our Science Victory.
        - Technology: Satellites
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Free Thought
        - Rationale: Free Thought provides +33% Great Scientist generation and +25% instant yields from Great Scientists. This is the most powerful policy available to accelerate our late-game science generation as we push towards a Spaceship victory.
    - #2:
      - toolName: set-flavors
      - args:
        - Flavors:
          - TileImprovement: 70
          - Diplomacy: 85
          - Mobilization: 95
          - Espionage: 90
          - UseNuke: 85
          - Production: 95
          - MilitaryTraining: 85
          - Antiair: 75
          - Offense: 70
          - Infrastructure: 80
          - Science: 95
          - Air: 90
          - Nuke: 95
          - Spaceship: 95
          - Defense: 65
          - GreatPeople: 70
          - Gold: 80
          - Growth: 65
        - GrandStrategy: Spaceship
      - rationale: Our economic rebound is solid with 1610 Gold and +501 GPT, and our science output is at 1450 SPT. We maintain our extreme focus on the Spaceship grand strategy, prioritizing Science, Production, and Mobilization. We boost Gold to 80 to leverage our high GPT for unit upgrades and city-state influence, and increase Espionage to 90 to protect our research cities and counter Indian influence.
  - tokens:
    - inputTokens: 27605
    - reasoningTokens: 6526
    - outputTokens: 301
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Evaluating Research Path**
            
            My focus is on optimizing our technological trajectory. I'm currently reassessing our next research choice after Electronics, specifically whether Satellites remains the most advantageous option given our current progress and strategic goals.
            
            **Analyzing Victory Conditions**
            
            My thoughts are now centered on reassessing India's cultural victory progress and our own strategic position amidst ongoing conflicts. I'm specifically examining their influence over other civs and our current war status.
            
            **Assessing Research Priorities**
            
            I'm currently evaluating our research path post-Electronics. While Satellites is an option, I'm weighing it against other possibilities like Combined Arms, Alternative Energy, and Telecommunications, considering their potential unlocks and impact on our overall scientific progression towards a Space Race victory.
            
            **Choosing Autocracy Path**
            
            I'm now deliberating which Autocracy tier 2 Ideological path to pursue next. My current consideration set includes options like Total War, Syndicalism, and Mare Nostrum, analyzing their immediate and long-term strategic implications for our empire.
            
            **Selecting Autocracy Tenet**
            
            I'm now focused on choosing our next Autocracy tenet, due in 8 turns. Considering our Science Victory aim and current war with India, Military-Industrial Complex seems highly beneficial, offering science boosts and gold savings on units.
            
            **Prioritizing Scientific Advancement**
            
            I'm now reassessing our immediate ideological choices, specifically comparing the long-term science benefits of Free Thought from Rationalism against other tenets. The boost to Great Scientist generation and instant yields from Free Thought appears incredibly potent for our Science Victory pursuit, especially with our current Golden Age.
            
            **Setting Next Policy**
            
            My current thought process is focused on finalizing our next ideological policy. Given its significant synergy with our Science Victory objective, I am prioritizing the selection of "Free Thought" from the Rationalism branch, particularly considering the substantial instant yield bonus it provides from Great Scientists.
            
            **Reviewing Diplomatic Status**
            
            My current focus is on refining our diplomatic standings. I've confirmed our active war with India and have reviewed our positive relationships with the Inca, Germany, Greece, Russia, and Venice, noting no immediate need for adjustments to these existing accords or city-state alliances.
            
            **Evaluating Alliance Network**
            
            My focus is on our current alliance structure given the ongoing conflicts. I've noted our defensive pact with the Inca and friendship with Venice align against Russia, Germany, and India, but Russia's immense military strength warrants immediate concern for our border.
            
            **Analyzing Military Power**
            
            My focus has shifted to reassessing our current strategic alliances and potential threats. Russia's immense military power is a significant concern, especially given their Declaration of Friendship with India and our recent denouncements. I'm also noting the impending expiration of our peace treaty with Germany.
            
            **Refining Grand Strategy**
            
            I'm currently evaluating our overarching strategy. Given our strong emphasis on science and production, I believe maintaining our "Spaceship" grand strategy is optimal. Re-setting flavors seems unnecessary as our current allocation strongly supports our Science Victory goals.
            
            **Confirming Research Goal**
            
            I'm confirming that Satellites remains our next research target. It's already set, so no action is needed there. The current flavors also still strongly support our Science Victory path.
            
            **Setting Next Research**
            
            I am confirming our next research target is Satellites, as it is already set. This technology is crucial for initiating the Apollo Program and advancing our Science Victory. I will also ensure the rationale is clearly documented for clarity.
            
            **Implementing Policy Upgrade**
            
            I have decided to implement the "Free Thought" policy from Rationalism. This choice is driven by its significant synergy with our Science Victory objective, offering substantial boosts to Great Scientist yields and generation rates, particularly beneficial during our current Golden Age.
            
            **Adjusting Flavors**
            
            I am now focused on fine-tuning our strategic flavors. I will be executing the `set-flavors` command to align them precisely with our "Spaceship" grand strategy and Science Victory objective, making minor adjustments to ensure optimal support.
            
            **Updating Strategic Flavors**
            
            I'm now executing the `set-flavors` command to precisely align our strategic priorities with the "Spaceship" grand strategy. This adjustment will reinforce our Science Victory focus, boost production and mobilization, and leverage our strong GPT by increasing Gold and Espionage.
            
            **Analyzing Defensive Pact**
            
            I am currently reassessing the implications of my defensive pact with the Inca, given Germany's existing war with them. It appears I was not pulled into that conflict, which is unexpected and requires immediate investigation into the mechanics of that pact.
            
            **Investigating Pact Trigger**
            
            I'm analyzing why my defensive pact with the Inca didn't pull me into their war with Germany. It appears pacts only trigger if war is declared *after* the pact is active, not if war already exists. Russia is also at war with the Inca, and our relationships with them are already hostile.
            
            **Investigating Pact Triggers**
            
            I'm analyzing why my defensive pact with the Inca didn't pull me into their war with Germany. It seems pacts only trigger if war is declared *after* the pact is active, not if war already exists. Russia is also at war with the Inca, and our relationships with them are already hostile.
            
            **Blocking World Congress**
            
            I'm now focused on the upcoming World Congress. The Inca's "Endowment for the Arts" proposal is highly detrimental to our Science Victory, so I will use my delegates to vote against it and potentially propose something beneficial to our science efforts instead.
            
            **Blocking Detrimental Proposals**
            
            I'm now focused on the upcoming World Congress. The Inca's "Endowment for the Arts" proposal is highly detrimental to our Science Victory, so I will use my delegates to vote against it and potentially propose something beneficial to our science efforts instead. I've also noted our own Sphere of Influence proposal has already passed.
            
            **Confirming Ideology and Actions**
            
            My current focus is on finalizing our ideological stance and planned actions. Given the global shift to Freedom, my Autocracy path remains strategic, and I've confirmed our research and policy are aligned for a Science Victory, including setting Flavors to support the "Spaceship" grand strategy.
            
            **Refining Strategic Flavors**
            
            I am now executing the `set-flavors` command to precisely align our strategic priorities with the "Spaceship" grand strategy. This adjustment will reinforce our Science Victory focus, boost production and mobilization, and leverage our strong GPT by increasing Gold and Espionage.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: wkyUGzanYSBP3ZUQ
          - toolName: set-research
          - input:
            - Rationale: With Electronics finishing in 2 turns, Satellites is the critical next step. It unlocks the Apollo Program, which is required to start building spaceship parts for our Science Victory.
            - Technology: Satellites
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: eS4E1VKOECzRYL9J
          - toolName: set-policy
          - input:
            - Policy: Free Thought
            - Rationale: Free Thought provides +33% Great Scientist generation and +25% instant yields from Great Scientists. This is the most powerful policy available to accelerate our late-game science generation as we push towards a Spaceship victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: rmWkv5tWbUT3LTv2
          - toolName: set-flavors
          - input:
            - Flavors:
              - TileImprovement: 70
              - Diplomacy: 85
              - Mobilization: 95
              - Espionage: 90
              - UseNuke: 85
              - Production: 95
              - MilitaryTraining: 85
              - Antiair: 75
              - Offense: 70
              - Infrastructure: 80
              - Science: 95
              - Air: 90
              - Nuke: 95
              - Spaceship: 95
              - Defense: 65
              - GreatPeople: 70
              - Gold: 80
              - Growth: 65
            - Rationale: Our economic rebound is solid with 1610 Gold and +501 GPT, and our science output is at 1450 SPT. We maintain our extreme focus on the Spaceship grand strategy, prioritizing Science, Production, and Mobilization. We boost Gold to 80 to leverage our high GPT for unit upgrades and city-state influence, and increase Espionage to 90 to protect our research cities and counter Indian influence.
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: wkyUGzanYSBP3ZUQ
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
          - toolCallId: eS4E1VKOECzRYL9J
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: rmWkv5tWbUT3LTv2
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.