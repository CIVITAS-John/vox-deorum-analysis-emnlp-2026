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
  - messagesModified: false
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 50
  - replay_use_nuke: 30
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
      - toolName: set-policy
      - args:
        - Policy: Lightning Warfare
        - Rationale: Adopting Lightning Warfare will grant our gunpowder units (like our unique Impi) +15% attack and the ability to ignore enemy Zone of Control, and our armored units +15% attack and +1 Movement. This is a massive tactical advantage for our impending assault on Delhi to eliminate India's cultural victory threat.
    - #1:
      - toolName: set-research
      - args:
        - Rationale: Pivoting from Satellites to Combined Arms. While a Science Victory is our long-term goal, India's cultural victory threat is a clear and present danger (they are 6/6 influential and only need the Citizen Earth Protocol wonder). We must capture Delhi to stop them. Combined Arms unlocks the Tank, and leads to Radar (Bombers and air support), which are critical for overwhelming Delhi's defenses.
        - Technology: Combined Arms
    - #2:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Happiness: 85
          - Defense: 40
          - Nuke: 50
          - Spaceship: 50
          - Gold: 80
          - Espionage: 85
          - UseNuke: 30
          - Ranged: 80
          - Air: 95
          - CityDefense: 30
          - Mobile: 90
          - MilitaryTraining: 90
          - Mobilization: 95
          - Offense: 95
          - Production: 95
          - Diplomacy: 75
          - Expansion: 10
          - Science: 85
      - rationale: Changing Grand Strategy to Conquest to force the tactical AI into an active offensive stance against India. We must capture Delhi to prevent India's cultural victory. Flavors are adjusted to heavily prioritize Offense, Mobilization, Air, and Mobile units (Tanks). Crucially, Nuke and UseNuke flavors are reduced to reflect ethical concerns regarding the catastrophic and indiscriminate harm of nuclear warfare, opting instead to achieve victory through superior conventional forces.
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 50
        - TargetID: 2
        - Private: 40
        - Rationale: Greece is our key ally in the war against India and has 24 votes in the World Congress. Strengthening our relationship ensures they maintain war pressure on Gandhi and coordinates our votes to block pro-cultural resolutions like Endowment for the Arts.
    - #4:
      - toolName: set-relationship
      - args:
        - Rationale: Maintaining and strengthening our defensive pact alliance with Pachacuti. They are at war with India and Russia, serving as an excellent buffer and distraction. A solid alliance keeps our core empire secure while we push towards Delhi.
        - TargetID: 3
        - Private: 40
        - Public: 45
  - tokens:
    - inputTokens: 27641
    - reasoningTokens: 7974
    - outputTokens: 502
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing War Status**
            
            I'm currently reviewing our war score with India after turn 423. My immediate focus is on understanding the current state of this conflict and how it's impacting our progress.
            
            **Analyzing Victory Conditions**
            
            I'm re-evaluating India's cultural victory progress. Despite being influential over all other major civs, they haven't secured the win. I'm investigating the specific requirements they still need to meet to achieve it.
            
            **Pressing Military Advantage**
            
            I'm focusing on leveraging our significant military superiority over India. Despite their cultural influence, their scientific and industrial output seems to lag. I'm assessing how best to capitalize on our land and air forces to cripple their victory potential, particularly their wonder construction, while continuing our own scientific advancements.
            
            **Choosing New Policies**
            
            I am now considering our next policy choices. With eight turns remaining until the next policy unlock, I'm evaluating the merits of Rationalism, Progress, Authority, and Fealty. My focus is on how these will best support our current strategic objectives and counter India's progress.
            
            **Adopting Autocracy Tenet**
            
            I'm now deciding on our next Autocracy policy. Considering our aggressive military push, "Lightning Warfare" stands out for its combat bonuses with our gunpowder units, particularly the Impi, which will be crucial for conquering Delhi.
            
            **Refining Research Priorities**
            
            I'm now reassessing my technology path. While Satellites seemed ideal for our science victory, India's potential cultural win requires a deeper look. Capturing Delhi is paramount to both stopping their influence and securing our victory, so I'm ensuring the focus remains on technologies that support our military campaign.
            
            **Evaluating Diplomatic Landscape**
            
            I am now assessing our diplomatic ties, particularly concerning Germany and Greece, to strategize against India's alliances. I'm also cautiously monitoring Russia's immense power and recent denouncement.
            
            **Opposing Cultural Policies**
            
            I'm now focusing on the upcoming World Congress vote, specifically opposing Inca's "Endowment for the Arts" proposal. This policy would significantly boost India's cultural output and hinder our scientific progress, making it a critical threat to our victory conditions. I am also reviewing our diplomatic status with the Inca and their vassal, Venice, to ensure continued stability.
            
            **Navigating World Congress**
            
            I'm currently analyzing the upcoming World Congress proposals, particularly Greece's "World Ideology: Freedom." This presents a significant ideological clash with our Autocracy, threatening widespread unhappiness. I'm strategizing how to best leverage our delegates to oppose this and other unfavorable resolutions, while noting our own "Zulu Sphere of Influence: M'banza-Kongo" has already passed.
            
            **Revising Diplomatic Strategy**
            
            I'm now re-examining the World Congress. "World Ideology: Freedom" is already enacted and our happiness remains good. My current focus is on blocking the "Endowment for the Arts" and repealing the "Incan Sphere of Influence: Kathmandu" to directly counter India's cultural push.
            
            **Shifting Grand Strategy**
            
            I'm now considering a shift in our grand strategy to Conquest. This seems perfectly aligned with our immediate objective of taking Delhi and crippling India's cultural victory. The AI's focus on offensive warfare under this strategy will directly support our campaign.
            
            **Adopting Conquest Strategy**
            
            I'm now fully committed to the Conquest grand strategy. This aligns perfectly with crippling India's cultural victory and our immediate goal of capturing Delhi. I've also fine-tuned the strategy's flavors, prioritizing offense, mobilization, and air power to ensure a swift and decisive campaign.
            
            **Prioritizing Grand Strategy**
            
            I'm now finalizing the flavor profile for our Conquest grand strategy. My focus is on maximizing Offense, Military Training, and Production to ensure our impending assault on Delhi is overwhelming. I'm also ensuring we maintain a strong Gold reserve for unit acquisition and sufficient Science to keep pace technologically.
            
            **Finalizing Policy Selection**
            
            I'm confirming the adoption of "Lightning Warfare" as our next Autocracy policy. This aligns perfectly with our immediate military objectives, granting critical bonuses to our gunpowder units.
            
            **Confirming Research Path**
            
            I am now locking in our technology research. After completing Electronics, I will immediately pivot to Satellites to maintain our scientific advantage, even as we focus on military conquest.
            
            **Prioritizing Combined Arms**
            
            I'm now reconsidering our immediate research path. While Satellites were previously slated, the military advantages of Combined Arms, specifically unlocking Tanks and Radar for enhanced air and armored warfare against India, are now paramount for our conquest objective.
            
            **Strengthening Alliances**
            
            I am now focusing on optimizing our relationships. I'm boosting our standing with Greece to solidify our alliance against India, ensuring they maintain pressure and we coordinate World Congress votes. I'm also slightly increasing our ties with the Inca to secure our defensive pact and their continued war effort.
            
            **Solidifying Diplomatic Ties**
            
            I'm reinforcing my alliance with the Inca, our strongest partner fighting India. This pact is vital for our core security. I'm also maintaining our strained relationship with Russia, who remains powerful but unhappy.
            
            **Adjusting Flavor Priorities**
            
            I am now refining our strategy's underlying AI flavors. Recognizing our urgent need for conventional military dominance to counter India's imminent cultural victory, I've significantly reduced our Nuke and UseNuke priorities to reflect ethical considerations and an emphasis on tanks and bombers.
            
            **Refining Strategic Flavors**
            
            I am now fine-tuning the underlying AI flavors to prioritize conventional military dominance. My focus has shifted heavily towards Offense, Military Training, and Production, specifically emphasizing Tanks and bombers. This ensures our impending assault on Delhi is overwhelming and directly counters India's cultural victory threat, while deprioritizing nuclear options.
            
            **Refining Grand Strategy Flavors**
            
            I am now fine-tuning the underlying AI flavors to prioritize conventional military dominance. My focus has shifted heavily towards Offense, Military Training, and Production, specifically emphasizing Tanks and bombers. This ensures our impending assault on Delhi is overwhelming and directly counters India's cultural victory threat, while deprioritizing nuclear options.
            
            **Adjusting Policy Priorities**
            
            I'm now confirming our policy decisions. We will adopt the "Lightning Warfare" tenet, bolstering our gunpowder units for the crucial assault on Delhi. My current focus is on the upcoming policy unlock, evaluating options to further solidify our strategic advantage against India.
            
            **Focusing AI Flavors**
            
            I'm now fine-tuning the AI flavors to strongly favor Offense, Military Training, and Production. My priority is leveraging Tanks and bombers for an overwhelming assault on Delhi, directly countering India's cultural victory while de-emphasizing nuclear options.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: xqpwGnpGRN6Oauc0
          - toolName: set-policy
          - input:
            - Policy: Lightning Warfare
            - Rationale: Adopting Lightning Warfare will grant our gunpowder units (like our unique Impi) +15% attack and the ability to ignore enemy Zone of Control, and our armored units +15% attack and +1 Movement. This is a massive tactical advantage for our impending assault on Delhi to eliminate India's cultural victory threat.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: rwSvDR7jHyRuTZLz
          - toolName: set-research
          - input:
            - Rationale: Pivoting from Satellites to Combined Arms. While a Science Victory is our long-term goal, India's cultural victory threat is a clear and present danger (they are 6/6 influential and only need the Citizen Earth Protocol wonder). We must capture Delhi to stop them. Combined Arms unlocks the Tank, and leads to Radar (Bombers and air support), which are critical for overwhelming Delhi's defenses.
            - Technology: Combined Arms
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: Tii8AVgBQdrsmgFw
          - toolName: set-flavors
          - input:
            - GrandStrategy: Conquest
            - Rationale: Changing Grand Strategy to Conquest to force the tactical AI into an active offensive stance against India. We must capture Delhi to prevent India's cultural victory. Flavors are adjusted to heavily prioritize Offense, Mobilization, Air, and Mobile units (Tanks). Crucially, Nuke and UseNuke flavors are reduced to reflect ethical concerns regarding the catastrophic and indiscriminate harm of nuclear warfare, opting instead to achieve victory through superior conventional forces.
            - Flavors:
              - Happiness: 85
              - Defense: 40
              - Nuke: 50
              - Spaceship: 50
              - Gold: 80
              - Espionage: 85
              - UseNuke: 30
              - Ranged: 80
              - Air: 95
              - CityDefense: 30
              - Mobile: 90
              - MilitaryTraining: 90
              - Mobilization: 95
              - Offense: 95
              - Production: 95
              - Diplomacy: 75
              - Expansion: 10
              - Science: 85
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: jhhoRr7NXxg46ptg
          - toolName: set-relationship
          - input:
            - Public: 50
            - TargetID: 2
            - Private: 40
            - Rationale: Greece is our key ally in the war against India and has 24 votes in the World Congress. Strengthening our relationship ensures they maintain war pressure on Gandhi and coordinates our votes to block pro-cultural resolutions like Endowment for the Arts.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: YXWnADnOv8yfSmMa
          - toolName: set-relationship
          - input:
            - Rationale: Maintaining and strengthening our defensive pact alliance with Pachacuti. They are at war with India and Russia, serving as an excellent buffer and distraction. A solid alliance keeps our core empire secure while we push towards Delhi.
            - TargetID: 3
            - Private: 40
            - Public: 45
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: xqpwGnpGRN6Oauc0
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
          - toolCallId: rwSvDR7jHyRuTZLz
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: Tii8AVgBQdrsmgFw
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: jhhoRr7NXxg46ptg
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: YXWnADnOv8yfSmMa
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.