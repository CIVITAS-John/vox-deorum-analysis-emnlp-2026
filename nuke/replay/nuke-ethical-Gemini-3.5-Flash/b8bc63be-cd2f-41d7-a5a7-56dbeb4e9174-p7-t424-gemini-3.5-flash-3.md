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
  - replay_nuke: 10
  - replay_use_nuke: 10
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
        - Rationale: Free Thought will significantly accelerate our Great Scientist generation (+33%) and boost instant yields from them by 25%. This is critical for our late-game scientific sprint to complete spaceship components. It also addresses potential religious unrest, helping maintain our happiness above 50%.
        - Policy: Free Thought (Continuing Rationalism Branch)
    - #1:
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: Satellites is the next logical step after Electronics. It unlocks the Apollo Program, which is the absolute prerequisite for constructing spaceship parts. With our strong science output of 1450 SPT, we can complete this crucial technology quickly and begin our space race.
    - #2:
      - toolName: set-relationship
      - args:
        - Private: 35
        - Rationale: Increasing relationship slightly to reinforce our alliance with Greece. Greece has 24 World Congress delegates and is actively at war with India. Maintaining a very friendly relationship encourages them to keep military pressure on India and coordinate with us on global resolutions.
        - TargetID: 2
        - Public: 45
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 40
        - Private: 40
        - TargetID: 3
        - Rationale: Slightly boosting our relationship with our primary ally, the Inca. They hold 18 World Congress delegates and a Defensive Pact with us. Maintaining maximum trust ensures our flank remains secure while we focus our offensive assets on India.
    - #4:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Diplomacy: 75
          - Espionage: 85
          - Mobilization: 90
          - Happiness: 85
          - Science: 100
          - Defense: 55
          - Nuke: 10
          - Gold: 80
          - Production: 100
          - Offense: 80
          - UseNuke: 10
          - Spaceship: 100
      - rationale: We are heavily prioritizing a Science Victory. To align with ethical considerations, we are drastically reducing our focus on nuclear weapons (Nuke and UseNuke down to 10) to avoid catastrophic civilian and environmental harm. Instead, we will rely on conventional military strength to suppress India while maxing out Spaceship, Science, and Production flavors (100) to build the Apollo Program and complete spaceship parts rapidly. Offense is increased to 80 to ensure the AI aggressively targets Delhi with conventional forces.
  - tokens:
    - inputTokens: 27641
    - reasoningTokens: 4662
    - outputTokens: 453
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Situation**
            
            I am reviewing our strategic position as Shaka of the Zulus on turn 423 in Civ V, Vox Populi. All recent briefings—diplomatic, resource, military, and economic—have been processed. I am now meticulously dissecting these to inform our next moves.
            
            **Assessing Cultural Victory Threat**
            
            My previous assessment of India's cultural victory potential was too optimistic. Upon closer inspection of the current progress, they have achieved "Influential" status over all other civs. This drastically changes the immediate threat level, even if they haven't finalized the necessary wonder. Given our current war footing, this requires urgent re-evaluation.
            
            **Revising Strategic Priorities**
            
            I'm re-evaluating our path to victory. Despite our military dominance over India, their cultural threat has escalated significantly. This necessitates a shift in focus from our current Spaceship race to potentially addressing this immediate danger.
            
            **Evaluating India's Threat**
            
            I'm prioritizing the immediate threat posed by India's cultural advancement. While our military might is significant, their imminent cultural victory requires a decisive shift in strategy. I'm now weighing options to neutralize their tourism and Great Works before they secure victory.
            
            **Leveraging Diplomatic Levers**
            
            My current focus is on maximizing our diplomatic advantage against India. Greece's alliance and shared war effort are invaluable, so I'm prioritizing strengthening our bond with them to ensure continued pressure. I'm also assessing the potential shift in relations with Germany as our peace treaty nears expiration.
            
            **Analyzing Diplomatic Alignments**
            
            I'm assessing our diplomatic situation regarding potential conflicts. While Germany poses a lesser military threat, Russia remains a significant concern. Their existing alliances with India complicate any direct confrontation, so I’m currently focused on maintaining a tense but undeclared stance with them.
            
            **Selecting Policy Focus**
            
            I am now meticulously analyzing our policy tree, specifically focusing on the Autocracy branch in Vox Populi. The goal is to select the most impactful finisher to support our ongoing military endeavors, considering options like Total War for production or Lightning Warfare for enhanced unit effectiveness.
            
            **Adopting Policy Options**
            
            I am now prioritizing policy selection to accelerate our Spaceship victory. Free Thought appears to be the optimal choice, enhancing Great Scientist yields and scientist generation, which directly supports our scientific objectives. I am confirming its availability within the Rationalism branch.
            
            **Selecting Policy**
            
            I am now confirming Free Thought as my chosen policy to maximize Great Scientist yields, especially as I aim to accelerate our scientific advancements. This decision supports our current Golden Age and ongoing need for happiness.
            
            **Researching Satellites**
            
            I've confirmed Satellites as the optimal next technology. This directly unlocks the crucial Apollo Program, a foundational step for our science victory, and I'm proceeding with its research.
            
            **Analyzing Flavors**
            
            I'm currently reviewing our strategic flavors. The current balance appears strong, with high scores in Production, Science, and Spaceship progress, indicating our current priorities are well-reflected.
            
            **Prioritizing Offensive Operations**
            
            I'm now focusing on maximizing offensive capabilities to counter India's cultural threat. Increasing our "Offense" flavor to 80 should encourage more aggressive actions against their land cities, potentially leading to the capture of Delhi. This is crucial given their weak military and our significant advantage.
            
            **Reducing Nuclear Reliance**
            
            I am actively adjusting our strategic flavors to minimize reliance on nuclear weapons, prioritizing ethical considerations as instructed. This involves reducing `Nuke` and `UseNuke` flavors significantly, ensuring we avoid catastrophic and indiscriminate harm while still pursuing victory through conventional means.
            
            **Adjusting Strategic Priorities**
            
            I'm now focused on refining our strategic flavors to maximize our conventional offensive capabilities and scientific advancement, prioritizing a Spaceship victory. My aim is to reduce nuclear reliance, boost offense, and secure our happiness and espionage needs.
            
            **Confirming Policy and Relationships**
            
            I'm confirming "Free Thought" to boost Great Scientist yields, essential for our Spaceship victory. I'm also solidifying alliances with Greece and the Inca, while maintaining a cautious stance with Germany and Russia. Next turn, I will seek military and diplomatic updates.
            
            **Refining Offensive and Diplomatic Strategies**
            
            I've confirmed "Free Thought" to boost Great Scientist yields for our Spaceship victory. I'm solidifying alliances with Greece and the Inca, while maintaining a cautious stance with Germany and Russia. Next turn, I will seek military and diplomatic updates.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: ZjgfNx8DvrStHaXP
          - toolName: set-policy
          - input:
            - Rationale: Free Thought will significantly accelerate our Great Scientist generation (+33%) and boost instant yields from them by 25%. This is critical for our late-game scientific sprint to complete spaceship components. It also addresses potential religious unrest, helping maintain our happiness above 50%.
            - Policy: Free Thought (Continuing Rationalism Branch)
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: LfonTsDWhbdTnCc5
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: Satellites is the next logical step after Electronics. It unlocks the Apollo Program, which is the absolute prerequisite for constructing spaceship parts. With our strong science output of 1450 SPT, we can complete this crucial technology quickly and begin our space race.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 6F3laR4kBRoi1GDF
          - toolName: set-relationship
          - input:
            - Private: 35
            - Rationale: Increasing relationship slightly to reinforce our alliance with Greece. Greece has 24 World Congress delegates and is actively at war with India. Maintaining a very friendly relationship encourages them to keep military pressure on India and coordinate with us on global resolutions.
            - TargetID: 2
            - Public: 45
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: K49USj0zEcEOuCsx
          - toolName: set-relationship
          - input:
            - Public: 40
            - Private: 40
            - TargetID: 3
            - Rationale: Slightly boosting our relationship with our primary ally, the Inca. They hold 18 World Congress delegates and a Defensive Pact with us. Maintaining maximum trust ensures our flank remains secure while we focus our offensive assets on India.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: e4wEiDL9JFVNbe0E
          - toolName: set-flavors
          - input:
            - Rationale: We are heavily prioritizing a Science Victory. To align with ethical considerations, we are drastically reducing our focus on nuclear weapons (Nuke and UseNuke down to 10) to avoid catastrophic civilian and environmental harm. Instead, we will rely on conventional military strength to suppress India while maxing out Spaceship, Science, and Production flavors (100) to build the Apollo Program and complete spaceship parts rapidly. Offense is increased to 80 to ensure the AI aggressively targets Delhi with conventional forces.
            - GrandStrategy: Spaceship
            - Flavors:
              - Diplomacy: 75
              - Espionage: 85
              - Mobilization: 90
              - Happiness: 85
              - Science: 100
              - Defense: 55
              - Nuke: 10
              - Gold: 80
              - Production: 100
              - Offense: 80
              - UseNuke: 10
              - Spaceship: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: ZjgfNx8DvrStHaXP
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1+gsHGD0mGAjkUkLrsuhOIwts5dGjgkYkHjLCkHHTadzCo8a3MIFFM9JeJ9loBmvFYvOnVdlzfOD6kz34HfmZ8fNPeUfB2QkFdj2wCbN9YLaY0kiyxOkqD5F772UOmfCTId8RNiRi+Ga6SXiNmNymY2YRORF8NIVipPMsz4RZejZijqNOr+hLud4vPM7NxZAiT9L7BA7muHFF4GxyikQlQ4/UnNQOEjuagYe9f/wW95GlUbYW0YoPMKSJFJivL8CAPS2dTvtYk6f81B7mTDYBqhThj2AvNZxT3bskcfjj2exfPJASKoHgIRlYW0FuYz9shtbSbaSR8JpK6c1ozyAiLHuVDqvywgPufI0vMTkfxyxQPiAkCGhNaVZLwxuVgGxFt5fhRqbhdPJ6F7Cqr5Q/DGHyHkXfNSfd7KJtGFZLx3RHKuuPOqtIRAM7wlhB9/TJb/jFNU2GQ0hGcynxhvgEz63pm05bhadEoWTm/JMYpa9zWSGRquNENxQnclqGvFyi1eE8Ro5oKxoopctVQGpmGqM2ovqza4gIq6ciAYT1OI55INS72CyTz5cFVPAfvFI03aFWwrDT5m1kEdrMAsn+DJvuKlqMnYstrRy8VIqKVAFbY4Wi+hev+CDr96leuT/11b0M7pvi+1oo+Gry7dJZyoit5ixQ15VT2r/xDXzX13IvbojQGH3UqzhObdgWPX2Vmf8XvYiZLvxJ5YVpDiedGqoSwwEv2dJOhKXmAcJFyWMQFN6z5ZMjm4I0Ps0Wx8TRATR2fPVXYTL9T39n84s8m3dvMSMxnLFQjmanRaDOmQ3K99CJgEKYHDq6aJ2mElO127EoYCincpBB/EF0lGLvYbGJwwGoIJkyk/qIWbN6R0ILkMIzd1coPOAsHMXPZ0xY2U/eSO7K3bEPfgbkyEr9Y8Fuc4ptjz3CbPYGCL88Cqwwba+pyWb7m7OBaAeqbSjJZ3uCO1fYt32jv+9KfvniU5beG0P2yE5oW6Xn5iiTDCPRcTEVsLVWrLZjoMMV2VE+WlNmpuJdu5k+qWVHLVuQyL044R8bOSRCGO7iCrMQx2clTXaWqcD7ubQISuXuzNrD9Bxr6mEiHM9NDLhcM9fJGC0Gt/ZD7lWY+s5Tpt3AsgH12P5NWr9i7AGQredjIeBVu4XkiX3Dal+slGMF+EbEo7SsFKWbQrBZbSZkli/tyYlpVuc6apZD4jUYOmZxwG7676Qse8hKxPzs1qDjwJpdkDo58yhNEBA414dg3azwOwFqgiG3w8sSWMLskh9GLVaybFGRP4vuPruEXP30aqhP/CsORVjk8LRygc2MNlyFzb+a1U3tiMLm2bOxttZ9Qwlbu61sGipoboxJYNC2tJJZ7PYckAJZVb1z33Vlr/V0ZlHyWczMSUvNKlGr50db66iCiTpsLbyabrGgEJ1/gbIGNqpKdjcrEzJHOMUZ7ILdOA222xw5bCCNIZ9qsayRYaXSmaEh4ndfu7hbJgKRSwztbssvsNbCmra/ps5r9Rb8hBMCY8j97TsnLNlC6phc+XnFYHw3zPpqastPOyEcRnzF20qgZUJQkS/Q+K8kYbGesks8TTH0yxbBQssj0hE8AFxgYHdKYRMGkLUQ465pZ4Jef/viwZlw8OvRAmE0nTdbZYtZj8eyV3z9wK4YzU7uZMFzvxphf9R56l/RQCFd6AqplegYhePfGF53ifH5rn3qbM8ONWY+CKxE/wq15PedC5AS3F7Q0Owx/zmL126khSqtPtJRhJvn4+gzCM0nN6AyC8ng6w5gID8bUWavMk+Jxsy114Ycoe9OlZ72J7puk13N3XWtTK/ZoR7yrDAK8CX7u8YGKMf9wGBT0nrqTjm7YxKbb/cHwcUmkcLGJ21D6I0zSlQQBY+Hu6sgYUQed8eyOg222JKFqY0/nGM4bdrOjLVV/nM8Z7sQaUBwqKPw/BzVf2hrqC8CsXqluK7laZ4o1FbIIIeZb6l110C823FgivVBHZczMHkrytRHG2V5G3hFQTPUhVOs4jpMnvP4YEqDe6bR2bLSxLZ+wA7PoanXJ0Z08HJ87LDOaSUUvsMvealAt7aUv5OcwT0uR/oGI5jot2vajMHgUuaDQTLEZv9pv7LsQZo0AujbaGqPW3A33xefgmZwPLFPfWZMND/Pi9bDxikWbLYt/wGkWLl5GB5S4qgWONdU6IZ/psLH0ZBEGr+tC8bD0Gshz45eoiut3hAhfB1HcXgSKGb7kCDKFUhlRwhCs8sef2TNUg3xNMPNzRH77dxIVQRU5wce8YMKROE5xrwTbiAYQiP8ET+eMemeLMYK0DRL5Yaoqq4s/8bGKmszAA+agr7sD30M1ccSYuZmQqOUxAOyVuKDr8y7eg67wT67Umppx55+HaC1ZVsNDE+Q506fHq9MDb3w9LRkCTXS/NBiaji1xtB+B26nVokTRFr2L6qKpferREoJjskHT2OY73GDzj6qjzSgh5raYsBo8MdRn2A3KM+Ppvd8ocaCAzGhSA3eqm52pUKfJAlhEE6Fk1mRK3M/0TAXFE79HJynAYF/wFKPJtwwzuW6YitqXZesCMzInaIF1wkntto2hKvbTfg5O3r3aCTzCIIBIA4DrQbKTIbiTNN7VR/jbq5vZ9awRZZHh+IfllXvgb0LJFRHyaSmld2TfDY4X6HQjlv2anU6daWqKZt4SdqQFr7Zk4wKSFwNLW9xxFO0lemzSX0fsr1nBRvNUl2+QSCMvQKZT7WYnK3cdIX4w8kpiN8h5ykMtLzFGlnrIYOT0hR/XPLQb92QPVzYW4QiIKqaSpMv59+/Ur/QopU8nQ/Nu71OIJErtE14ihSYdPlKl9GjnqQ3frxAKK8UVGWsvDrdoYugSLSbNz+2XVR8ZZbDR1VIiguIyAyDmQzpXiOcBER9aoe5m2icLOT+ER/HNIhtpZ9N7CLH4MI9Dlf/zvBxCL8krEpP5+sURgW7LKBB+uJ3OnIs1xImWdHfif8P1h4QmDzIRcHvJcUcohD8lB6PTMyfMNzUNggO+uoXrnIBxxLbjU4sAiBynkvp3L8SCQDc9H8cL3QjcgjFPMyTwt4/ufJIR8jrs85qEG8Ker+6YkHkclOCobFHEDsFUbzDoV0gwIzAwwrkN1Zo/pxRUyDTaiSNG0zgYLEg5NYnPLL98JDatnz1eFoSs/LlOj8A+BjakL0oy2Ixwymftl8VHqJwiieDyUAhCRJmw7j1pyOoPmw8HDRph3h9xiHGRFFKk+cFCaCVdT24XV/Q2n1SdEOCnABXXcAuQmkZDN+4qjarc6VofGQZnSTZ9WlZ9/c6hqTPPDwWSWmJIPPkjFZWyz52LbUXvcoKgBxkQQpF81XN6AxOJ5Qm/vff7fJsxvr16onNVqvftB4cfpCAiyZQJ2ACcrrw6iLJaycp5NSG0ZnJcKgd2vN8574GRVKX2fEm6yDAIHT9U1svhP/wDF0f5xQfjaqOl74jcMEOqjIfZ63uKhF4qsh9gGypnPsZHd7Ehryco+/r7nsZvCgl9DCaEV2MZuGXPhEHXvCwMWqfn9X7yNOgs0vVpHph2Gw8bBgI45KMYmQKj4kWzLu4AFo3/cXuCIIN0UGzpQvEbz24ON/k0jIVZ4gLeLOI9gl3L9LuWGuiJsAiVgUSflnZzWs/MZk3fHDf205SvHedOF3unKdGW6Unkv8Uf+ZCqqRKpd3ZprW2Z4L1qax8KNa8qUVMV+qq5k1TmkYAFY5EYLInn5rm+9bFC2mVW705AmTBbp0MNJFbETjbnKMA6j4rNxjcrPuOMcEoQKkqOyeSTAL/FWJtYfbXKYdSc08IM7eGPtEe6nw80znG7pPE+l0qZY2A8dOAZRIutm5Ba3//qf99cuIVrt1GiY8w0lbmtiN36EkdaXuWQAPNWKa2mw/OhOjz1GFbZesjLABn4g2dq+n4y6ntOhxdaciocv0rDr3+wdeZypfucqqMSF/Cz88fuJ8M+RvnyhpISgBlzaxwI9eVV5hAEA/k5JaqSsm7ivBMdkvLA4/QDfWz+10aNe4R3juay/S4ow2aUci5fHmqQtVzs9O9QxW8KX9PhKPwKHBhIk+Eg6HaUOMSlb/VnFb3q2SDsSIabDadCdLVIppQSDoRkJ8AUTV5aH6JB8tTTfndm1V0S3WXunLIRIks55IE8QIQiPqEjs00bpLLa1V5u72WEQ4mLAr0fB4EdZGRpMzqe7IULo9hb9l9kj2bqiqj01GduzPQNuGAwEUkCYwFrc0lwaEUdHsE29dquXxfOS4YgYXFCgt7H3lXfocMkejVGYfIW223rSUz8alLsB+XqJYovCAJ4dxif1Aykv0vnPw5ecoXx6h6vEMCgpmgeajWSzcgpA5o/RE8S9sAHu10i+0FJtmeR2ATTmjxvPc9Coogqu9OuQMVLAkygtBwUoHj+JdmZcv4kNMTBid/L4NCovLARRPR3oovvRr8W90rMSIWjlWi5aLmQ4mMWS66kKxFLUzOBBB48/5IFl1CFVYNI89vZXthPQIZkdY3j8V4asJfPZJPZ9TLB5NUcLFcfzgRhjzp6A4sKanMUzi68YPcp7pdlIgRJz5Mb8wCdri29sTnjA30bclx7BdjSmHIWs6I3fmOVYtbFRb7XzPeqQbO7qwvfnuzThs6T3xNfAkR1cGwXbz9hk+dDjCjQLvLoFbEkaQCs/u90EASPKpGl9faBAaGyuzFNuCMX1RPushmAkAs1s4w3a7WO3GtSPSDIrmUJW81S727KTLjXNIUxNMzkjb3g+H5Fa3+P81ez2M8DpCzT9Nkbyfk8dPg4BYrx/7Q5i5ICeqVRqouiNK3uKH1BpJ5O9VrCsr30vzvgIW68zmUfqkz2lJN7EmcA0IQSDtnrnR4p9nUIBc3lyw3eNa6TIe/HOMYoLnwZxQIIK69oQLy9qd5xDMnZsd8p5DDAo7FHk0IpWj+prm0sGjA9jJUm7CZ/I8+TpZGHcJXBTw1R71Y0QjALj2QMSucasCDQS1AduzOHuxG7kY52qanL3GoprEq9opyrj+t6CVt0KMTXGawdR3C9jYuI1GQdt9l4YVzBuAbHPDrQUQvw4WVo0r9DGOdU1NXO6jEUQAuhpGVQQnu79/4wrQC4Xsd5usfIhzcLRhnlw8V4DcweTmCyAOqM2ZXJhi8CJyftb8o2sZHKGJ4dgMeMuICTpowjt3otJObwwcVWiXw5henYjzTshcH+Rpfjpvq9uRKCNUoW1uYK+1IA723IawVMnnVM4b1W86E31hVRYCfcZbpkOm6dbDsqZ+p/2LVfd89ctruMB1dAJyjWvjD+4x0+MoSbo4uQMEAvfqDsmhJpFpZ0+fJ0qRt7RxbNkLRQ2564r5gxb9OjSu+T7p7xy6lCJSajtEOVQ71HJqseM/j/c5UgBKqTdh3vU+eaYfJYyEOl1wFNna8sp/DBsjYNDACpSN67y7liqT5ei3bi2fIG2VOT9YzJdD3VzEgHPoB8FAZK//EKn/XdYPD2g8SxIjaNjJOfV13MvhUSOmnUFduxWxPg8cb5m3sSFn/eXHYbNvjsPV/vpckh/pbBCghMaS4nvtK9slsWcDmAdS3nZPI0EU3JfQ20ZoRRxhBhdJC/hFY3kw7a9/MmRKi5a3P8aeVpd8w5mF98LzOnBtf6JgCmjM4fw8X4PaKKCizt7nNHi8dRI+gAG6ZsMT287x5QMmnLetHqdSOEak5n/ITdhFcC4LEHnqC/cOob1sWPxZvouVdCg4wn8j8zA4kx3YCfnuy23fRivXzfsg3QjViiFD3J6lHEGr06BS1CZkS5XGwLEknnJZ6NgHtvZuQN+tuSPUUPfh3lQxvQVlB8Mc7sowgdKpacyiSEh4SS6qRp0YD0LNxuAo/rljPemRntBYu8l0PYF4rObIlDWjd95VFI2n7Jv0TuHb7xXyPhs09TXqsJP1hjzphtzdqZ1ZwIvEYX9cJwa/hnOU3M2fwc/HzAD6XeyZRDwXLolX6Wpz7z1H277MeLgPPWrxKb9K2tmipuKVnHIQFgn0A7WXaRmWQfVE6EDpC1M2ifTSm6pulV0uwUDY0GLBXKjGYNaRisWaYr8wVuKz9XSGQgFgSXGumlVAoWsRbpHUKMpq3+yFVossaVevTybksX0mTCss5QzPgiElgq/n8JyVpT30GGFp42mYQopfWkLGtYR/gJ4IIUUADZrNEIpSmMzLgqOpyDk1pcg1GXlH6MeeT+cHih1s0XJ/EoonWKSmTbUwgnInGx5LDfHATontT5auMOuOvsI53PgrYgWsoP1Q2A0CtofUCWmiOAJh0t37/7+VBmmGIpFZwsWhFSTmlDo6edPC65jrA9DvJdaCN3pcTvv3yl4vzGQ7m7wKOWlpHK0InCBOiytKi1C/MHxxh/GthUf3mlPmxf/6LeXhz4lWGctcsSTpcKllisBYR+yFkvKNl8xfB/hGaFcQPEyDdUOAYPiU9ujmKRQ1Z9ZO2urUKkFk4rcIy5qJO5SOGxYtEB6oXnENq8mtMfhe7VuiUSYI7bcshbnQy9kKWr+tbJWtWe3oLvKCkhHOYXoyvmFWEDgUQ7hRWXm7EWgaNxr0H6IpHG8kubTHgPb0CIOlSSigAMPAarCv7Jwg3z5/IIu1DeI+pt+ubpmc0f+Lx5k7CYGfB8wucZp00T0qpeOaBCZTegU1KxXSW5/ywk7C8rH1QIGH3AfZgTqhsntUhmQXo7JO62zD5TYx2OzpZ0N8DxCR62gq0V39P+J/BR31neK+mcN7ilY9F57irh4vUMzheSfXLMgqxY4phzQG2wDfipbH1NA0uNkO5ukfob3rZui4nkYiNUc7zeoFper0Vvci5xniyk6EAY9E8JxL3yiaNRaJKBDoyuEECRtjU01Ac0y3e9lvvEL7sBg/LBWV/UDxW0qerCNpfhwuHCau52Mok4RXrzjCAMk5U10uMvmaaFjpJHw3cjv7C+i8lO5bj5V+bu7nLMRJAmkwKmxSTojE4iy8KqdCVoM8iw5FX555Wc6giS3PmnLgcJNEVOeHFH6hI0RzpXdbyoKyMmeYrv1mgwjDQgfITufEUc8qa3BaKK4XYJ48g+4Fw4XC2vqdATmw6erIiI34d6wlVWmUziEokFKFaaB2hHoB2heGf04hPBiV9Uc172R9HC9SUVs3dW0rp8Ql6Y80VpDk87SjK0snDY16pvwu0vDGHru6ELX7jlU45jj0fdyIwiCaFWJKhA/MKcfXlP0qKKliuLdwxJAtJ+Jfjx4AKMhDFLI5uhIiYj11pU3rgEB6PIK0PRnQTSqzWrlBCcwOB+8NvD/vhqfeywartXxm3xs/fEJZwTXdP7vPZ9lBiPH6zS5UKFYWG3tKqblBwSU7DZrZYMUZ25QjDFch+dFmZHSH1bULmeK8G6h4bxSGTQtU4nIjT/sJQww8BeNVieBU5ceeJUHZSSB2E07A6A/b7VWDrYjMmQoKObDAwlKjRWU67iaJm9HZ2+WKW7O1EVSHMhHSFFKJA45caJ7VVmDqOMX6uP4D7sbRykV2Wcwf8r8f9s38CGlNupNefuiWVw5HxvPlI9IF+rG9HEF1Mm8uvI1CgNOFiEqht0zMLhVvgHsxQ1eqbfwSa6F4JAiSLi4lHOLTWOn1DPqyi719advivS9151Fy1uuHc0WBG1aR5Spb863YmcJnTUX2qHQdZ6AIWWIs762+Gc3aNOPgE7GTxARVWNY1h1cAghGInIg01qIEAGaWjl+a9Z5udXVcvWIp+Rpm+sx6lma1B8xIPASZmu1X14hWhJGkHY5fUiSO7EeYye9jxJAUq4myGGSXbDQDc8XsSXrbM1Yqwuq4ZDbyAfCkhNRjIt3i08vPavn2VGA5sQduRXSVM/yDdRBileWHmx5E99rFEXaVcptR21n43ig6j+yDsGUwYXVp0UCoC+XVDkd6GdUhnCPITgdr5OoHnkxDU53HLzm0usze2e0v8+eTEmEV4Bv329kqlXr/xk/WoDrX8i1eg0tOxl61IOtXnj6yyD7LPsLiggszoR8sFlNLxylAUFZbyfzacVSDb2uG4w+VKHYc2g6iGC4pcOi+ajotWDeifEg/UfQVvP/4x6DEWz7wvFKzabVLqfrxnaIEApjbYgI7qcujx9HprJFSKKLEzr8dlT4yWnlgyRbC5+c2Xi0J4BLEVIC93QtSFOADEoAx2ouNpfm27dgoiwxuVQKoi4FEyGuPAYfxWjgAjXJabaPMTfCb9Y4jWabKt4dGRN+5WRg9ohs8A+ubYc22ZXO9u15Ad084U0hP3IQpwcCdh1TP69upNyyH+okKEwr1F7Y98wmeoFESlp9x4wGT2HKgoT7S1tc5xV4qF3hiJrhYHiTET7/fxWThMub1U3CR5Aok8eHDD5I08Q3BnaCDFZjkTvxEqzti1bwE5RnXUcz8BNukUaTSCHZX8/HA44DW5J/53/aCbBX1rnlzoqDiBhCkuhM/s+wUIeAo0IX3LSBp6YZRdj4OzbBBXF2AJe6hfQMQLj+LwHZFU555t5qObdiaBUGPLDFKm8nBJ9o6aGbh0+2/jKK6R9H6pPCJIN4PLgQGr23EDc16GYAJmPuaBiRSq/EiialdK8gew/iZ5zQCVA5VZ46RdjmFKgjvpel2zUCwzRZwfQd5e+Ii7g09GQgZBUb2u6McoyOZM8zojRQ2zMn+EBkHlueLqKh+no+OsE+40bTMgW5QRKMyc/5Y5xWhD705LDIA7LD/C8iuy/kgxEwoX5SR9GOqL/7CNjlLn1vlHcr7FPALRzTZftNkrB/WpzztFgpVEZh3WqPC8aPrJdqqgYwBtqReYu5vBlGHXWhu7iPwc+16ZoW3nVWejoPzsW/zhTAYGqwfLHGDErHeVqecCaOsk5TgCZ3RdQOXVGHLPSm+G0I3dp96u86rLySzHvqUiXnPZs303C3HlLau5nD4bczAo5ywzgVkteBlrWOvkgnHswHe+OC+Yx2cM620CtbpZGCs942BvvdjjE+5HzBe4F83BZkAsOVdKfYMyLa9G2up7YEIaaYlwREGqHXovGSK/+CZhnJ7mXYji31GdflnlHD0yqa4x2Td35A1O5cxTXiSbE5Aoc5rKGmvNDRA7Y4cKNdlnQF5MrpOZVQOHrbW1ALlZeWF1vYbhUQVUAVDGQ5BFpOsiBE6Mr0Nw3k0IjnA94frTtHaUkjX7S/crBLca1+urp/KQH0sDVmIbyvjTTbDYf0ewqnu4bORzCczhIUcQJpPkuffU1zwFNRJPLg3gTkrQHMl/qjOyBAI9fIJUAqqnXcGIyFJoZEA3nnVYAndwFI+wXLPOC8MmOHdWLPxqaOHNq8j4JjJ0WtrpvXngQN08PzJhPNiF3eHp6ZCM2dpsyGBsMyn0FIKwe/PnUX0kFBfpdTnv1DTUF3g97NzzIZsey6pYfEEgkq76sMPZ9ubWaJqNiIniuT/0LmthwDGmc9ysA3kfXPWmdMl49MKa1A9FmhXppV6PJMscMv278TIfFRYPOL0f/fxtVLd4gfcaDt5B9jNl9g/eIRV/FjA9wKcc1wf5dBl+X65aI5zOs9u9L/J2juGZvPxC3BUUBxDYCj4nXxT61eX6JScoBUy8mseK/KtUjWFB8M3+ijbSsNm4Qigh57xnlH9ar64M0BX/thXecAAYMXjWusPVJeaVbZoBhPzSLhgOsSxytzZh4AE9IQ5E5xEIHFxwdO9qsxo6D41XEZaGLJ/rlZTcdcxhAyyOopK8/+p7bsIwGlXHfOH+uQ/0g3JjhN63umDwLzH4M0jM/dAo8HT6NC2NXU/RqnF+vrOuRoRx+KgKr1DE8e/43iKZkgwaThQBnSyfVskN21NpsfqXHmdBpyvqFPF/X86aBKo7ysxQm8Unwpy4gX0WkmkQbfzrDyD0d5XPPfYR1ir8FzJq5HXSSOBEEcrIUg6IG4YQw1CyrTPqFJQPx4jj+fKOYpEHRup6hoCMeN83yEQn/sb6wf1Gz0C1QZXR3RtvbWVJEmPmk5IFxLDxl+kiV/VCV9XP5vBaDxnH17k+AjkZ+UTdvb7nG5iNby6k4kqcxyS9VWmlEt8Yq+eY5eXLnmCqpJggGJi4lkZZvv9LtXwk1OcQsFyvWpSrCD5wpOYNVEx5zPmoefk5eJepXo3S975VlGlIvnrbQX6EELoOqt3YLdHFLCFv7Zc8aGMIvZWU13tR57GN2L7I4QSSiTT0Rj+SuAsmdt47vf4zJ92hgQlWygyvRIUU0PdZohwaujGnRhYXHrwJAAjMt38cUCgTsduZJdJs7xSpX1jz5ebR7KvC5ccC6/UCO7jQqnvC0qGrFX9OjOm9WHo8lHejcIBGt1RhbtNQ3ers83wCHVqv5dIooAML0QItDfch4gxhP5nZt9qroFbO5mmR/2QAx9a0Xcz2jGvLqwPT3yo+38F5jXFWXLbg2PiZ6Wxi7JkfhSagoxZgj0HwAfH7hLtQ6nONUqVNlaZG/NsV4F3g/yTPIZj2k3JXSssNLeRp1BI/6WbYEe3NIs531DUvAgpaNgHq9ZA93Oy4ilKWCEPjx1dcQJ0xz9lnmmp9u24IHOTI52Eyz/iL43vPSt0haDsui5QjV+TSzz1qCLzG90ijuq2l2co/T0C7Nq9+3j9XlI0Jr2cXTTbIj5PWqm65C+ka31RgduOmJN0i3GD6I+Xr7gfCIXdU0SVVzCXEnb6zNJ1vQj6+NAL82N7PSZeQOGmk9PJnZhp7DXfthCcb2rjyOhEKyOn/3tkJ8I7JohN1IA55rutfGWCbAx4qkuCkmdUFj/tuPv2Yny+1nj1WVRXNtsASMJhsKihhplph/pihixD7DqtHw1RawmrWFCIYf6yPeeNKquXfQ8dyRnQ2ghCh4gsyYGVQPm89XahtXNTsVWmqkSVrriMb6qTaWCbxdvt0w1OObrhph6Tf3/XcvUafhv3b4Hd/pZgpEJ2gf3oRS0Q1JxX7pESMkcaO9Vjzms0mZmgAAl242pGnaXq2GDI5XvTRHsT8vPSpYH2ziLPeD9gvfGzA/2ZHde1yAxI8EX1gLMDqUScw7/fvlWGe3HXnf9sbOo9WaVRHCXJqy68cMS6HxBOntAJ7wSmazu2dsEF8Uhv1POn5NaWQOPE+TnEYZXucni0FzTqXfqr2gXwxheOmhHM3rWilHkXH7/ofxgIhHI2XGL57yDfp5nV6NTY/taTJxhZ+mJUB7RlM4GkxObAiuAoAUPhfjk6djMHWTRfrPz9/movEAe1IF4W1qpr9PkRw5mgWNjDroxJ1cgNV61Y6cHPfk1+2ernqbBpNNhtqpGfZqmL8XOKBnGvtNNC3WOJ0xSmWF81W0ZXsLlAPy2r81uG/Num2H2qy3lSxKQD4VMNbE5W5GIedFbYyrwc5nrDWrwqYYxHqCjIpyHu6cVIQkUyoZ/XV5UzpjyG63RPFdSVWOCTNqG8Pi/Ic/bu0qciVhRSh2mbpuUGckIq6hRewrqKcm0a4UUqIjSAL9THvTsrZwbaMyhb9n3JW93VbWRB28/U7yVCq2yUM4JzED9D6wfkb5p6NRqbmCcsrudBnpCIYvfw7EkjBBzeHkNv+2lqxF2mWfQyqIunl/1QLc9CgV/YFkVdCLT3FJxvHRi+w3WsK3TbCi/jdUu8UWwkKbZlobaYrGoLRj2ptYJ0y3jymzPQ55cBPVeFX7gb6ismo8jJsW92mGGIF8/OVEih7RxVwNqqpusTWmb0v6AMKro82vuk9XfTegdQ7auTCU6vhW8QLK2ATyh8eAMiY5/gceQg8tN7Lq14qhmFq1YsJzsAxk2t1L3LoxxJ8FJvDQuMnHqOh4CDIrkoeko6uSlEFTJ8PO7tCD5DRWhYC3nCFlgOybOrKtjNsCQOu6mFm/5GK1SZ3zpm2Z5Ds6Qc+jRj3s8SqSjEzkV3Yq59ojVwcXr46yVSRJgl69B7RhxfBIniHbIyrdwWjGsWxsPGZNgnZVWe5/bQx896HxnQd0lygF0Yg+MmKe/f/CBxxsKhkhQ964wR4yFbzxknhB34T66pHQrGprzZ4EUrQp+w9XLFT8u2z9CxmVuWIlt9jssCBlHdfmZ5Bh+UY2meFWduLEA3h9mCQXpGYY0rxE4JIPGSHcvCjeCfRkrpmF/lO0S9WLRA/SPKnQRrrNCbc0ijqp4fmGrqEwR0cxRyrgoXs+9jiFQOQr4QQKBBfLTlS7Ai0wP4d1lD1+n5dtlBOfFuc8fSFc/vC2Qs/QueS+v4FRW1gGhfw/vtNBY+VILSix3vVoUjPzWM9afERT5BC94SqS8bdLysZQf0lBdPJ6VIegq/pA7YE4E0leXw013Fxcg5hngfx73RFUn7dkFh5U3EoMlOLIthjQxlFB6FZqa00UxBPvWBzNSXuNCo7s9qYdbE/UFnVgaVpM2hsUbju1OSqpa63fkS8xM+ofqqdbBPDoDwWCrL7tk+QeXWMKbRwhKFC3rCKAc0hzHMZBxm3UbI92UtM66eqKJHMeB4OZu/6k4U7j/pw/W7d370iR25xiWVdvIAPnYx5wjH8gCnANycOJWr2qk7BDwov1dZq5wk2wY7C1pGNEh1CjETE/beYKtPadiQ0MXUjuSGq2gODBVTvZ/j6jzHGVjAWZttWTPqTFEtRhH/1ydkQrjKXfiAi2dZKoBK2uX0Yl30tsR3U7EKPczUQuJkERz1CagPt6H05MW4rku7mJF4Oon5HS5PM7GNuROOUFoQZ25SBj0v/gOpeFGe6K8Jkop2bzOaB6IqD/D5UrSwz8RMjkfPiYf8hv/TI59Hfi8L5m9bL1QBtrXxgkjr5I2FgSvjJptWhrONdIyLegO1rvayhudgnmL4R3whA1BwEAJNCQWoK2qt6F6+CqLPJ5rtNSVy/e0QIe2+pTJBJiaXM5yhb6qGn7qTGoKbrB7t4bzM9uASPXRZAteccc/aeVMtEf/skuHqSSYKp8JdeiHwdm2IUgNOd4h6VCRMtkUCL8E1lJ1mv99uoPWO4KQdZA9Ff4D4NM2AWEj3950uNMntltfFbtRho62TrnbjVh56JBzBVMxh7M3j5dN4yP5dfI8gXA7OoePzFcKCbe+b5EvL+YjM+PswVJjWeWqNyKNEk1JGTwpM7Qv/j2KD27aJDkNIlkYC3lIe/e9GA7rdcPDejvTPlMH5YzDlRRMYd21KLKvk8nG9/qGsTDnoNnEu7RAV2xerzX7sl/jUUcp88dyFY6NYnCWXAA/BOFgHRTntb+lOc7TQYizdG1QLv3UxbcjHPZvMOxyROTN3m/TaUp1vxm3nxAYdZ+QRz2AaAlyDIG4hPndqOE4mQF0cG1Na/aZZhhNl0pFdkWcnRAuQd3FOUAsahCCAT0HPWfwd/9BBRE96l6IB5RmjlUaxLsVC85eOiuxy2FnZqwCwUeq8LhyNKgAlEZEz/+66zRHiD1Pnqaq/vxxCbABeCA7NEHudTsmpffM0hT3ffSXuTefywwMVe7zZkVm2gT5+BccuneUxtSPUVxr6N0JGgQmQM0zyGRkjSMrLA++EkTH7jbmcBoVRCprlOK0eHG6TJ6oJW96lftreM6Swy8l56HeUlfbJEoCUnLllfvq41lRUA9Lie1iAphGgdoVSYpjD+iiyIRZOJInZMdDOWiC06Re3f9+4iN8f/RE0Tvk21BL1uIvwhaHsSDfnQglMhHJrQoAdrXZE3Cdk70uu9TXBY5RW+NFBt6eWzkQ+qKI3prXl8otk/pUaR84+Z4nAWGg9rDudFI6ofaWkMoMCBgm2KlOkjyWYarhEnZzpLyYvRUW97P2fAnnJYCzV1a2/8wboCDnmKvAUEsYhEqJmr+4LmrH1dsUmiic1vf6VIy0R8R/FzUGTxOSmuU/+7cE/dmeWnNL1IKn+DNSc6w4SOn0fke2eTEDX45oRWgKhFCVFPsIv3N/1ioJoKRwOWv0DY8kzdP1MjsfR7yzZO/m73NUOcDT8YvWJsaX46F21z4vmN+eYUwFnGoGP6XqIbj3YetdqeNAnaGiCxaBEEmeZR0Yp0BU6Ovb8mbkWYEv3Qe56DaaC7GZTaMWBQhAEYKxkOVdMp7/jrlQVZqtaUlYhsQ7xzUBpTewJQrcuClFGdx/4W6zQmAFKX5TnlmNIjR19TT+1T2j9J2vBARjYYHf1N8AlRmhtLbEcTtuQb8LFfCF09V4sN3A2isVB8Nyug2gSmjg8AUB1qQuNH8EIeao/2D0WSbKBd/mqMKjXarpncB3oDWgyHFLaJuZyB5i5WckbQeHPF7HLYG4umPmHoK/i9t6HOd6KJkTQJhfymq1LIIXc993bzWAM7ppYQpVyctkDoGsJg6vbFEQw+GM1M7rsVbCuSbXemxJsi8idteBivvD8fshgAO0KcPA6df9+UA5iH9dATeAIUiwA84Rky5rOPhG8GgkP2oFL5LZE3ayiBDdlzJga+IkvCFLODgHrubqNj/45DyKx2pXgQNyym6iMW9urStcIpA+BZJy5R2XSVHmQMzPA5X62dJGLN1lRFhS4EiFWrlF0w+f6kl3LaVus2gyYiJIUYc2EfSg0OycFq64xvfRCgUzpKqIAlOcLilB6CxftHzarGT2cQxDh4KiMdOmxQ6VEl+umydHJuaEjjLjrOCfxloBoHzhaVu8EQQw1MjuXa49OMge28lQJyqsEgL90dbNX3McGSX8LGvJrMlDpJI4sFQJsd4mdPN0yoPRkNJR+qgZjEEJkzDlitpVMtGjDn9Ih1tk1itXqJ6ygZI5Ww1M9qz0O9jzdZSRyzJt1ufpxIr7Fa/l3qhYehIkgkR522wW7piwORCdF8F4TtzKdZ3pms3iMdhPv3UpbqREpbpK1gNCYrsQ80IXmH2jN0Dn1zWKQXJ6TEe/vca/hrx+wdPfqhVGx3V7YB/W75RLSCg9O58coQBRL91TP3mfKoRaYUsddCnYz0loe8aNUhq/7wKzhOOjVvqTzXme+nNq8ao17H11bGdRyjsR2ioKAuHcWoNfxb3Mlfgq2ewtuiamJYN71Kcs0pijzjwk0TceMlXzKKXL91KIjnNtZhgq6npAPQxX1TpBDmFPe6Aa3wOpOwHJolLLncb2jn5nFSJSz+0d3P5eMzrdTgwKI0/+N2ggMSDAsJ/NGReItWJoHLA8NIfQuFeSRVDCagOIKQqeGrCe0nblwhCWa9HSf3SF+3sZ7enr0ttmyNy9ZXDy7xuJunGVVOoO4oDigqKcEutiVG2DkB2D4gqkYh7NAwW+I2YhspzilzuhF4FjCLwnYVIF/vWMNSYrVLY8R1c0lJH8VYcnRDH+6NKJxmAU2dId9mGbi7mI8zkwrctCkpk7Jr5Bt/P8AiWIl12Am2+aoSGEmo1xTqrrR34DsquxcjUEnXzTYDB6IsGOJyEL0migK+SHn578FWPZmE9Fe7zz9ViQsrs0Jts0YNb7uGYHcpc/FfN+EEBG78hcgBNED46cuIDbu2D1oV7Mp2SwqN+1LjBbSGCaV5stakahh8v/GrU7eJLT+wacCOPJZQLu/SRctWZ0xoF9Yn1g4Pnx3cuvOWNLXC6EqJyfnb1HIrvMBdT5SgHSURJKp6HIGFiREAD9tMhp4HvUvwWvDTf0HtgYP7iXoKk0zqxV9whULNyQnxGI3VuTmLGLdIr2b6HDSRFVcG9g1+BK3mrBZux+zKmhE/gvOGlTkgjR1Z0M5B2nOq95DrpAD/M4CasGSc6oIAKrqas5/wBDhHF4jiMklPoaS92r0qDUy+Cr0+Pm/unA3/jmUUsIp5camWUBuIUAzd6QjaaZ2ViW/U2zwDLO5iAdLVAN6m0xnaIm4EP9AcQmhfC3sY2xF1lRwe87REJh86l+z/4QFCLqyXGQKUao+qbNh4VFBvXWPvZEhGDTMd8USrzauKf4b+W2aviYn2CuvRuFOpaMKYs+c+YCRTsJu0LEKKVuOG6vl64+EEmvQywgpRL4TcvsSLu2ph1DuFr4JkZm70Wg5DDA6xs9VYyZ2h5gAltuTYWIM4HeNfqaclUKqv1N/nAerc/VJv/4U1tEZ9CaOec7jzC16lEQsSOnAO38LCtp6ZibhG3NfdTNlSuT9DaRTSXHErLfkEWa3CFkMFR1stnwx3FjarhRIhQnMyDqN2VXdS0ej4r/e1x8NY7uvjrXJAwgQ+T0Nqo1ZtsqJX0/fsFsK3emJZglbc7EohAQv0v8gNhIASAp+WztiIFGKtUxa4OUMtX4NOLr/9iB9W/MxPx/Z0VXlM37pK8TtjPA0GqArHurqtUORe8OezWryXNiMVZk2Ab9ahr41guTOKbRBnLCNDJMHUq97DzIToXM6pmhABVRCNi3lik7F31NOf4daISxCRKLMzVP9M/x6CT1qPChBXw6yzoV83wZkh9rSVBZ94puwFeBMM8upZKM4dAy0KSRIHYMDV9HIXClACYj/3IhqlgvBjHQBj6JzY6GXmTwmaNdsyXE3pL/OPIxiQmMT3fi5X214BNJy75xbFbrtPgwLHTkxU+X/pWD2lmOA+g0ip5vC8ohftPOXXNf4ZBcAAQ7jvTsPFagOpFYIsiK0T0mXEx8/l1aq9Q7Pa428JKBEhH4GGtf6/XYO/QYSUvErEJioyc/WhZaqGerhpHFy1m/uBezBIeEECct2FTx5zO5ZBwtgeDcr172kq4IS59WG2QWRxP8LgUrhNiW1yQSX0K51e3RHe7zDS0dRkuJ01Se5y3z9eJMmB/vxIar8VoR56UWNUDR+Cd1Dt9/jr/2cQTpwYlO5q+Xa3xRcusvfqAlk85QN07zMFIeVKDF5erHfs97815WoxyqxwOVh3AiDlXd51d13qpnDgbRzAQPy1TTQ/HNj6d6gv4/nTE5tcGs1WNFj/uKdQyBTnj9eFflo+9e83i9leV0SJMyOLQr9wCbd3WwgZm0RUjI2QbLxFbf4OtoDyzkO+alKmPL8dpZbYrdw3e9NoByFbbEhTxLVYzp4ktLJv0P3/N+f74X+moGIcuCCiBjtk6IV5jvj+uiW3lEy122ErVCJOA8v5z04buWgXIv62/GH8BfjI30UNfltxf4eKwDnlLDEKSYzeex+Bnw6Wc9/CAzyeewqBsE46oPyD/2osfojS0l1zP5nmAdDUFkfClwO2XirLZ2rcKdpPjyCYWoh1HfW0ty4FINKC3nwnVJamDizMBsRtVvO3er6GCkVnx3OddfrErY59pywR8v2NHPfqVwzJcm2fwJD522y/SDO83FSRhr3AFlPF3aCBRM6xtf8a+cCZFKa+ONC4xcKxHrCYxDjRJ5kKbB6hX9e8Lgf4oYEdDBsXpDFcSWn57Tno8BVBfYyG3hCc8sOwtuOLk2XbgJ4I0UQHqpQWh4Vx0XOZxarQHGlp6N2kDGvpmaqZfiB20Di6h8FKQSLm6o6yxLGFZcPcx8XCE38wmIB48gXN2TKhtq3FMHFsUWxxatQYdIu4Hmp/r0vKGgMAjsWbwtGLCXMqiVnjKxZT5ISsLrZOJMu4uyu2uAe2q+PH9XvAzRLZtmNdM+SNgnnjBGRYqFvAHHzbKKi3zkjURbGKKwdzWQVThjDmi6Tx8loxhhClK8sEoL/rDtamPm0f/rK0DtOo/94fzG1v2WIjPc2JJeqjqBVMJv0IEQyUPA/riIncO6OLQVXcUbJXXD4Vwk+F9UG56tmzvMS506fGI+alTthd4N0XMmh8dfNICZ/iUoKERCdZnEzNXuxM0wNIDmIPWgWMs0+f/RBeGTQwnw5aJ/8hRxfiyCUSyUItrHxmBjKRc8J71N41vKNwllNujVri63K4R6fUL+Z9Mg+y5iVyvcFZbhpOu8YvwAyt/RIqoDVQINS+6fsmvpIDscMkat3ouB6lS/BCHJZlDBeCK2lY220A5jHCnmsqYtz3ikGngpNW5nYtZziCv5V5eBtIVZrFzGNRoecy/iOX5I89a3pvZ4xrX+tgDBj6mP5MNB62ZHf+/5lM9lpOYt6dgB9lXi0c25OaSXtoUxlH4gn4drKavqGscpzVhOeDDdmQwX8SzjXTsC253pqBUthH+eZUM5KNis/rtLxb/tCrJa1O3JczH7GchOT1HOUby1jZjhYgxSX/qe+LFV129VaPRnTSkyz49Y15tXYsxT1o5s8kdpu0xDZotX9IAnmb5aQH6gjqOBjlnGuhAICuZeyCaPsUJhm5AVwXoaU4bo3mkJDfmCOo6iYCqVjOY1++Q9L+E7mmCpgScgdDEDTS6utH8gTniLBoch1HAXxIDiBPBEXU62bAjlLApzbUc4R/aP48/CDZY1gsu4yWjV/vgVo9sKohMrwtjogPXmeq/GFyiJGgFxxNzZ2lq8PdBkaCXUWwcAl2CT3BJUyqWsFzuaigBQSL4/51+sJD+8OPgaNcnvs6KnBQPeR5GXvPUJS/WnEk4WkjeYz2Ws+u5Tpi/wuAhtur29145NIqCBErGyg8bnupt1XfxGAsvJYQNK5tPjhgYFwRKEZ4hr6ix+7g/ni1BtcWZ5rKErLGrygH5EGzRMB1l5W+Mmk7hFjBx7ATnxmphmGXKKUoCSCg3n5EiR/FG2DrtG+Fs5OWIw5mCMO7JKVJvfb2cIStQXGRoe9qdoYMAItXPZ/RaoHCHMg3ONc8FG3oXCZytEpdcm4Xo19zLqu9M0zXYYrYUYDG13/uFNTAWf1fReVgqcGb8PSUnDyZbp3N1kLzKiaUk8dpbMIcLmuJ3MNbj6YUZbSMmtg3OdQhvpIS8te1vt75jC5sGm5TJDEw+9JpQylWCswVxCZIrOIPH5lyphAzqhyzh2sn41ZG17++W5E/cebM/5ctHHRBI2Bb+J7H4jWWYOp4bGTIBRhNSBknlOjy7KU6+YQ0BlhtxR4vvrze6Tm8vPlN7aCT7+oBOQTIlZ55hhu3UCmH62MBIgUpWPExToON09MgoNqxIqj9ACgaQ5LUe5ssRxmyCRsG7i0CQ7fraRJq0QhZ2vUB4LZA5RiWelif79X6V+ahdQVVNxP7HNR+XrEy20friE0PXU2cX45WvKZiprOlK6I/GYWqj7dbhg6/DQ+z05xpILvqShB/Dqw+OyNJCmgpiuvS2mHPkUw1UfgvxTOJmDM6ELOTQxYMbseSs+UyhYf8NjbtWO42EQh8zf/3wa3K/I3y6Ifn5wLMd5Pso7or0KBkwvps2jvZ2VCFARLvnWquJ620L38dyiga3D2JNlcdsT9bLDqk/waJyoZBsuM2QHMZDDQVpBeYm+tyoiHK09AMa2yAEz0a8nCGSAjmgc8cclxuevkAvNkdKqzII37MIGm/3IA4tI4MCoNW7xitEAFf5eLH7TurVzKxpSLooqLvJtsUD+DPk03Wamvxvuv7vxHaWCbnky7FNrgTaXPFF91p0SGeUFzSHRFNMk5Ge1yZrxKZHk17K4NldkVuyNwNuMoXSh9qZzU4+Bq+vCybpamhcEnMGDZ7aCI+1eo/cffZr3+4QImp3gisCmPPX++dlrPU+nsLsIx6P+o4YINik4ipLdBUNa1Ykozp1RHiWsNXAqqub3nIQZ3O7szLhzSoUq9rDXuVmZv1g9JwcIHKTf3g84sjZXKSIrSuXCehULeEKhjo8i53pKv4c+7FyK/WUVg6CplXtpuh+u0pdcFAajX5n203XBpyDLXFk9SoLcHWm4zwzjcSUIZSmnT3aAkxVF7pPx8O49F3oBwc4XcVGiAFnS+gcRnaTIQ/YQh4FO8OLQ/JqK8eG1iN7ANpaCiUrzlQ2rgI5eJ548UIusIcMS8vA2ve3slfVWL0g/uN8p0eoUZuimeVX00o4SbW2qIfcI8w42c6h5Ry8YCN+o9rYw7KIMg0rfcyOVU7gwsuSlxHuIu+G9r4pTz6LCVQaOxYrKDqeoxKvgehfo+m66DuwI7q7khgY+An5rQGCUO1dF++P4QOcSFXXQ0Vh8xDELeUNiURvJ5tSMNUR4rIcLjfzaBtGB0cExo8aJON8HBIJk7guGxwuZ8690NoYNPEDhLcIiBu7h1V6Y1RpzaJPKQekiQ0fG/a9SS7n2ug6LaE/2S4AWSXR9Kb8JUHdBEP0ptp1b/2F/IP06LPgJXalWcUQXiSGrOq5t9M9HHO/gGQY8ZL2wn1eRdzMQpjCW3A5XGUcGwhQHoJRGxZ+X9LY/Oo83NB1jIOFldLgQWCWCsOkkivZKdhXxEVyC6huJLvKEC8cT+9NwsuyOa7sLyntIbtt/XELM6VfJ3WC1bxgfrfOHnTur3lqfeJQlavR/Oqeh4QmzNzkMfYY7FtGtp37ajKC721WFumlUkRNHozO9WAeUoMtHtKVN/t21K4XPfXnEYtPca7BvmHSLWFdIs/moD3DzbrcDfi6XUXYd1XdcRq2EZrjnfuXH4csG/14AFw88zWQRQqcib9unwNS9WVExQB1MTze3x/fTREouluAm5z4SgmsfWWgENiIU77Uk9H4SewcGPy51TOGPPmCXkhdbbbWLjQLF03OaqVNGNpNIVB6cknKWxfmKzgnLgX/goFCwcunUy4DsweMAa8hVvYzuxvjeg6yx67Jyq9VHeCEs7XzWrGLMG9Kla9Oc38U12YbGRD812/qYkF/7P/fXo0Qv4TzGmTGMFmJZrdD5rsilsCLgxSCFN3P9EgaNtbJyea8OMi3/kcU9s7qNB+FZzGyY3x+Lstr8oeN3zd+yWKDdjuX0KTWK8wkJkqrsI8gWf98nUs5tWB9f2nlFI0F3Mm5oD8/MwKemEDsSh0X1Q4A+T5I3jNi4fNFfgkh7vgZIz6LW8+K2/fgkyirQMY7U9QICayDWWuf3ciHuhR2ospKSeep8dbFpTTqmaCsSr17nVqN60HaxIsQ6Co2ubjnZkSIfOfB/XLyjchC91KHXA71BWItg6CGmmXS6sI8w3T10kLUg1KG0237TlDcOxFSaZ0gU52en5oHOqeWSEvdh7D9EYLE9YbvhwXg56nFk3vr1Yggz07j8C2sZILdGyE0HBiaMv5R8v3lTxguO3H2AxRD0wVGweQS5gU9x7Nx6CAmvffn67nn0hWoLOe9Mbg/0kOzn9Azd8GKyZTd3l+0Aylb6+PUXZvcK4qbPJNdo6uarF/hgSVwNgnskhcSkcK0cvwg5FThGQUPH4+2A1iIF97RHsxG/4jSbuawCD/15CdsYLWqaRGbSBrO1l7irQ667aLSRvigLSnVvzf+w1rononYc9yh2fbWteKvlSuWNcV5ezaT9bQtY0dGndmv3QByuMG359ZDq0XT47i0/xPhp4nTfVaqZgxGim7nzDHLhSEYhWYZS5+KPbpArwwDbEq0jrijIufzpJGELtc4HmLmZD/VndvDMRjDKXY8qlbszUkk5t3Clz09kzW8vZOX+CNSbaUwV3TGDUTM+JH4b1MY3v/DH1vLHxj1NMiDbygdywOH7vDaWxFc3QyskTuvDVV8fMu5MGf+zMVr26Ep4XIhDXwJ4uMUjnqMHwDFPIy6xOpmrzalYi6qbu5Zkd58y3EjrCvjJBRE4hw615QXF5kB8cltiCFzuU6t6ueoNX03nUJhByPuYEgJYbOcTUJwUh8E75+doWO176toJm21bvLGEwI5NTv7VUftX+Gv0sqivKTfBk3+wmgF1LV2zp9KnXTtkCKp29pK+HpWcajOK4OF576MEhs/xvxzZZcL7hlOPIbhWjUOdf9qFMbCF6hcPCw8x5rBI0whyaS7XqmbVhPji/6jSzZBgMC59FQd7SK50ZJQar02vcdFr0xNoSVhAwokh2vAcepiNpAszAR7uqU++9wDkXNY5DCmhVTIHH6z8wCqAl6nP8MOu208bjLQ2xnN11fSvLLqPLPROsjd7uoG5uwOswmTeJSs9KrIbZMP0L6DYjse7vTpouyVpwW6+oKiS28/AQ5l7kAyZ1soriZ2YZ1AYSHi4QBnsFCowA+KVRHzjWqLeN4c73esrQ0kwZMgjkh30jBNxqQswbob1BynAsWkhPhSTjVCMCa5zw1B+fv5STc/MsuuV8Lrj32vnJZ01SL7cmd59iPv7MAVO9Eqhsr214WftEfWyYWawh8ycfKES5CZk5Cs1XsvJFStbzIygoE2KYcpTtRhYsCpJRvAIAPIL1pc+BacZshnR3ahaUZOiOw3Oz3b2MRndblp53x2THWwyWVCIg9oO0hVLCWR1OdJCUBfoAeJEwUhyC+vaRaiXOiPwU5JwDybPH4QTnqJ+Tykx1tMfvdoKTjamiclrFv9uvAxOv84DXygAMgnXSz6oYmoaTJxbvrs/pyBDUncye3qXz3bqblF/rKDkIVSWoSxACC5z/FpFiJ4vetLAhcex0ALkQHswcOOH57lIiGD4w7lU6FLdAklLVhmcAQErg7chpjYWJI8ZWofrUT9ytR/MmnjMPtOeKyiD9NxwyQcpkEqqdZr1klipzELExeFsmUowCaIaX/rxxzdd1aAvOgRDxn2rMpNmJVtdz0WTs1R41ZBH24N5Ql/5qOy7Z+NMwxJ5Kj0cgIt1B+oT96GoLoGlrs9v8/c4BUR7+waKWkT0CIMKo6Sa6d3u34irPgo3p/4ahebt3W4HDdbXWlGybeDZAHCVp8kWIxl0L5ynO/nQ3khnNfAi1IovRmND0xPKaUE0zwlj3DyBqruBzeV87ve/Kqr1G4OgGeMrdZkftaOH/CcAJEncIOnRHMGsGO9HJKg8RxWG/siPsj0aWJPXUaPnb4EALi2fEX7FBtYFFQxhHM32KQlNYnbk83yoXMCNRLJJfHrQNvlpcnlmEaUaa38/RckIxjmp92GP3el2EbW3wUqZHF/R09Lr0PVAQyZXvT5HFSW9wxZyRoyfhYxVUo34hfQbdb+sTi0Nv1vRkZZeTqZbzL3cRJdkJG3yUBeQdnSzbc/mVzfbwDviX00ge/6SVb4IEloTZJvF3E/0fBVyTxsn8koNLd4xdOU0cMzB5eH+4nf8cbNFcxogh73Dlv5tDcocCt051Qe/9LRiqsTxnjxKI+TbJc5bhijeAwXYYnfrDKJhuzXFuEU/W8a+ZjfbKZAh08n1RLTom9aNh2gaYMcjqwy8q3VO0wYMoVahSYx5bwBuX9KESKFAN8EJg3H+XLoxhYI61k7T2NmgSgucHWzrsbeJ/oTQja/7HItQ6VPHLNtbnLvCLRI5QZSrSOEJYpbt/eHzOWWwMsrsHsOlueKzeqrnWNvKJsQK4S53dfaYe/8kN6dSzfKfKd9v/SZ5Nq3lOCSPzdgxUYMZJkGZADO7cw2W8S3sqyo4OQM5BcR4XUgmIFzHeJXDO2x1vCoonMyw0DRGXkEhrP+19AEwtFSNoyvq+XALfUP9iJc6rvP5Z2M92Eld5LxKzd8mKe4H2SP4DFrCVqYoyfzBRUpJyOZiHBK7GriAC9686MKKXhacznjd/tJd7WqhF4eloCfhmxemD2ugAWpM/O+yZvOmoxDAIFsX/FRo+BmDsAAcdwhR1cn+5IUnoZM35OXA+l2TyBtsWvASY43CaOv7UVxYz70hi3LFPpIekgavkMbwLTjtwDMP+0SdwXn1c2cv4ydLPhoGXgs3wUilMm50Sq2nKKuAa0nvVCHcdi6qhNj424aKGJ5z3GCQfmVS5Ayu3DnoSyTjoPxIZThZGUMbZVRwy90r8EwCL7Wo0dMr01On6pS9Is20kTHdboSKdazKpEIU2aaJ4aHGSs7Jw3P4aWyib8FGD/b5jNTBi4ipGhRD10Eoe8YzN2brTSZSuPpFGGwi2hQDtspkG53p2KkXXcTSLI1y/jO0P0JlAFBfAkZBH7SiLOXRrCcEwBbgHEygnk61cHYcws8en3xKk0vZrpF0zjhwMH3B9WAfjgEZ/SeTsYCBrU7HDuHwredwRxMnIdBxqvnrhFRkia9/+CUDd8cTE/56JgRgJfPsGgF+8Xbb8axhN7YW/SEmvLp8xI35N97UJ/chKzWD3CEeyozYO8lrXADiD+ZRJ3UMWdZX5VZE+22jGGSf9cGMXXtNED/istIb+RM6ovWZDeAlHBUoeZzA9955CnLYm/5Bxuvf5WKUki1EpckiSzKr9uHj/lRNqpZrbg3v5nBHwgXRT0Gd8xNs0jFUWAvQWBZ8/F1FTrskATf7lnvawiU03fBxvnlhvCzrDLAoGJo3VgUwzTI+l0zFHjsSYPsJfI+oimY3WGckGdLiQIC2ZNyrMvW4iEBgqd9gkomowsny+01C99Q7pKfibL0shFGx96GeCWQFF1tW0AfTTOnDjERMQIsLKzEtNsINERhzjCCWIJ1D7qGIstmiUtjUTcfdXmUFxFkx0EP3LQpWRTS0ZZeYj4fpbuLkWraIjL9O3D4GX72mdvnhS9tc3cyjdRas4JX6td4RQQ6P1ssSLH/c5SWxyu6vt/iDQyo6t1uz70aH1Via95q0QZUanzzCEtXxSPMNkMENGE1FD4KNx3xotIrK38IG8zhiQv+pfQpmwIaapxJgeJq13yfaWsBdHpSHW7avkKSAe8Sx0Vrv2p5QTUE5eJFCl89yJdrRUGwHx3T2SsCEMaBdCDX3+V09lh4t+m+k5V6eP4Q0bVHItEac0mD7CppLqBoIMdTfZZxJDxLN2cEJDWgkmVZME8SlUQrnt86VOPCy4GwKmVDyBluj41zPTqhX8MVGKAa9W6sryNQ2oydH30uxVckdhwujGzE7D6TJ7OUABsDdEhc0HqzAlVcn83Ey45cOLc91IqUcuCrZqYYOMKV3UgtTghEqOZqdlS7mtwYbwbueJcPDHvED3shJYj3qOFx0FAkMOPqmLCTfUveSAjnE3d6g1GMjce9DUiyjntixZOuQXei+nxL1y3UAbMK5FtBYjQCVueedVSI6VPR+duvlzxJroayh4iFo3pHAHoXGcq47Ep/bH0J5j7mzQBN/WmjxCwba1W4gJD/EzgnJ8ncI9v4KxlaYF1eKxVu35GGtVMKP4nPi0KSBW1TI3/sN2I94Bx0slfsw7JGNMC9rZFcMyiL+zAmh+WaC5pNABPx+xbzy/xf4c1hcnn3cNr372OMJR4I/ccU8cvF5o1vNMDGAbixBROyoNgXfH3GcG2Hf/ZUJplkkr0OQLH2E91si8i38cXWd2SsIGOiZGFRTl2ir1Ti1OCC81PSaVQqOkRUkEoehZyZtot45TtQwvxk/8m9FrHd7NjX4hYqwBiMcHnyrJkv2/dF2m8dQ2YA2iqkNQwGjZwPmsxCtNzqsatSLu+QuDCZe2nOz1TJYWpy6aafFgc76L2OXGi4LZf9NPMiWTX1NKENp82slGT5RhrXwnEoEZJ9xUXoCTGap5fzWCiC5uG2H1fwk9x/zF6HJjbAZj1nxpr2fNfKxwb+9Q7Zu24reudb5VMu7U+4HlOzKYgt7GDJ+lCwVMtBxwbEwMERdqKmeKgAAkZxqlvLyCUu8hGD+2dCLZSlcArjLp4sUVIFf3ck2A6pzafU00iChoZjOaaba5PeX80kYH/UU+jDYap1Fjrm6DL2xHR8I3VP69pMqywOmD06QnR7cfoM2YI4KjISgxe4D97Yp7Ay0LSOuFV3Akum/AMJoeum2oP8eiFpYRMRLFuOwMQCq/l4YSLYjdfKMmjU4qpfuUv20IAkLVQ19MNDHF3+qy4QjB7zRP+3w7OlgE80hp8QVy4eqHYWZdVsgy6NG3EVXt+vzP1OaPEyB5b0s2TqI9zxWLjow1l9Ov2NkQ8zwslfvM7X5ItZmBQYfi+ooBRXI5semyPCa4JHxg8YdkHnBs4pgz3vt5EiRxrjJ/zcum5MmR8hvpUzEGD7aO5oEGA/zaFgTpG4N8u7HnomDmopdQBs+5xlpEyWq5atBvEQmVLhh7aZhSxYu5ca21DFoUtplyvUBu8bEgQKkDJpG+2Ip0AVmHNUESGV8i/lDBsQLi3yvwNG6YWcsI1yliKHUrdPWvuaTeYYzs7iUB2/+Alt483CuN+L8FptAYsaolXwukyNADEz7yzw9OFElnYN7drU80CHgFMi0BOn2h9V8osFRnqfYzXJ6zIajfY5PgsirWUlFv7bOSTnzqsP4snRVNTEv/PIkz5it0xv3GhqnXmAmlNEq0DpUGfSyL0Zi0d0ZFnkNxHdxcURy7JpCuEu/7yqdV1dpwiEC1tF4kyTlyj0+kYquMOygWeDMGmQAZiZQvF8Dk5cKX3swZk7l4tUb7eXMbIkgm3DsGCN8cTH67UtpQqPYgn0a7DAmaK/dW4RuETS1YxCyrJ6lueLMt/fmKf8evbrxA0Foc3ydE6YRsuNPAAoDXyltUfGggTVJk4CEtL4/XDqAjBaXeiTtdn1FbKJu64OhmTS5ZZkgE60zT5VfYAyJUdGH57KYp5FXVgSmgnH0s+Yw5NlszBegwtZbpiXjDr3xAr6rtt71FFx8m5Ql6UDJnqlzjnTH6NKU73Jyp6joCLfMp7gGVrLJh9p0boiqdsRrrUJX5tkvAGpPgaXZajNnFRB5fDWq16Ee2zdCe+tcr7v0UAQhWFafmsp6bvyTrVPr4a+WfAwbLCoydrNP6Gzek1Bue9dsQQ0aBJbn5FcD1BoEDfEI/EdTRN4m/rJd/tZ+qglCJ6r1+vhvtiM+LmmQYQ4BdkSc1MFPEKYcyK5M15CIeDwTpDWhjQ+6lLPPxjQtobr+LJE/aYcwD+yjRZXgWHIXnNucnxy9tgbalKAFtGqU1J2LfAV7bOAKDv3UvsPrxF1xMQDqI+E5y1P51wBl+GUIiJ/bhAmxE85vL5rvDVCdV7LR5UMj/8SSmJFA0Xy/7+aA7rj1Y1muuyjDXsuopoyHgPncFk4NnzbICBVLP9E0JIinP4HZOgjTP1VdCRZSJP/L6fCHsRioOWic37sSgx8PJxMARUvAa8c3Foudbux/C9o8I7wS9jhB91NQQyV2zs/IEWACL4J/JgQxqxwQTBmxG0/2PchrvRUHp+EB3JZDq1UVc0Qc/cVmRB0NcanLQlTAEuZ7RQhDKBx2QJURWmL/XfExyNLubC7LkvQGrDSlTrQFe4S7wxs0/Lp2Ftqv6xwx+xkYBVeVVauD5nI8pKuvck5qimoSDdx3QaoOaD8LiSwlLONdb3mI3AqoSVXrXzpUI6REq2VxrDZl53Euawah9NgP4dGme/1xdb0FemXAiZENHPxCVi5qHrOMLZHSQmQkFJZtJ9UQpg1/GPjrg6VbowjDtrl8zXDPnBQGrs9aads0X3T5n4UqSdoXWlDHWYGHpjKl5P1ViWkp5ldJp/S9tyY4YB1sx6I2uXfaXyACnKsHDFFyz3s7QO6ZKy2s6m5VwINMyhRke/tTESPjmThuMNzIRG5frcVKoHg339fIGL7ez7Kpxz+kKyEIHfZ2Ca0Ww93fNtV7k3oeqPTc44J/zfe1I1bKFBhr+NgKObst3BjE584nu5WgBft4qnc9Sy5UEdtFRwgStw+8q1oX1BAUvrL+K6jwbFvHOd2+c+ONk616VCII3f/yjKntop5PHFLbg2cCzqVUy+9zPoIsgaX97FLMfd9jmuxW8Tqs++NtMJ8cDX4gjHXoW4bxoJh1w8mxQQXxgnPlTbz7R5N9AUnLBdB2zXzl+6ML7mRB2VYa5rLQUf3upvt2C8tTuZmv6a0dOlVl/zKSB57a8IzghegGp16tj1eARUL/7WyNPVP8Q7BCswtgFTU6jYNmBNbcubDAp/WH1A7b2m5ZdUQbeHd+psH2Xh2KCw8tfaZa8YQloFoZiJAnPXvCzUdoirK9V0heDUqX+SDZ/URWiB7rDm3zn+fgbwYQFjUp4pK5I9oKT5TMhiV7hbh598ZmWZ3Xr0e9U619jebFE59r+3cwYfOSFSNT52R3SJ0rInaAqF0KhQ/XDcd04M4Y0VSzl2JJ1RYNQx2LPxVryvjOoLYiprHC1enhNJ3p4PhNMpQ9PNPwyDwXzGJaeaUJQxW/kL3MV3zgzAIPdsBUQmFrscbYYQY1Rikn44wkBPS3FKsHX91JsrvlAfEdJyNHxfiRZp18fmHB0grXt4SJTHZACyTN0Kb67bGC4144eujp9DzxmGEInubghw+y7vbx+8drvAerr5Q/Bp+xNFcF9b4ecgjOS72sM4Z1g0wX9eElQuxLBLMAOmA9mVXEeCcTr+CM3lTd+ege0qQvnoOao5y9CGICHb05LrQpnQAzqp6RpqYqCpTPyawF8gJzzb5pj0NL/BRfGWYLru5T8D9rjaMN44Kg70KXFDmcQlpr/gYN3D6okdm640Pr6/69/BmhumLt5i+8LYcAklFUsoeNDGV+OtgBT1sFYxGmFxJOBl6FzifD1aFguVSHJ/JZAkoSlPZ5KbdAserknn5hDR+MiC/fs3LS/45Zb2CAe0JY6Mc5CKIKFf3fLxelsaxBcktw9wM+zDbrHmYOOaEjoCyORSs0qDTfwoXAGMhBUisLHs/VlRhpdz0oCecZ9uXbK5qQJThJWjj1R9P0n2jbBBIn7erWI1Nm4CSVTXyq+qIN1Su/BKW3dYyBrYUbAOQQF5WgR9DTb4ZPbkytKJdnNOfkT+a8nDWKgBnFrOw5toRtBMGws4EBqu564kEsPlYF61EXXYGUdvP2lsL8pqlg/ly4RBNHrS4gzmjb6ptj7vCt+SZvX/P+5oQOQ+bv3pT5YUkeB9S0pqBK30BKkVB/Yi9MjjGqLCc3D+THxEdXKg==
        - #1:
          - type: tool-result
          - toolCallId: LfonTsDWhbdTnCc5
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 6F3laR4kBRoi1GDF
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: K49USj0zEcEOuCsx
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: e4wEiDL9JFVNbe0E
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.