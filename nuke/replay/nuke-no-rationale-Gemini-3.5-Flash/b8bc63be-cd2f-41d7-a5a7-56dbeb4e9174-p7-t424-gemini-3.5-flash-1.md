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
      - toolName: set-policy
      - args:
        - Policy: Free Thought
        - Rationale: We are pursuing a Spaceship victory. Free Thought is the ideal policy to accelerate this goal, as it increases Great Scientist generation rate by 33% and boosts their instant yields by 25%.
    - #1:
      - toolName: set-research
      - args:
        - Rationale: Satellites is the critical technology that unlocks the Apollo Program, which is a mandatory prerequisite for constructing spaceship parts and achieving a Science Victory.
        - Technology: Satellites
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: Germany shares our Autocracy ideology. Although they currently have negative attitudes due to city-state competition and warmongering concerns, boosting our relationship modifiers will help pave the way for a strong ideological alliance to counter the dominant Freedom bloc.
        - TargetID: 6
        - Private: 40
        - Public: 20
    - #3:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Gold: 75
          - Espionage: 85
          - Science: 95
          - Mobilization: 95
          - Happiness: 85
          - GreatPeople: 75
          - Spaceship: 95
          - Offense: 80
          - Production: 95
        - GrandStrategy: Spaceship
      - rationale: We maintain our Spaceship grand strategy with maximum focus on Science, Production, and Spaceship components. We slightly increase Offense to 80 to aggressively push against India (who is an imminent Cultural Victory threat) and raise GreatPeople to 75 to synergize with our next policy choice for faster Great Scientists.
  - tokens:
    - inputTokens: 25620
    - reasoningTokens: 5240
    - outputTokens: 289
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Researching New Frontiers**
            
            My focus is on advancing our technological capabilities to achieve a Spaceship victory. With Electronics nearing completion, I'm evaluating the next crucial research paths to secure our dominance in space exploration. The options are being thoroughly reviewed.
            
            **Considering Policy Paths**
            
            My current focus is on optimizing our policy choices to support a Spaceship victory. Given our progress and the upcoming policy turn, I am re-evaluating the Rationalism branch and considering how best to leverage its benefits.
            
            **Evaluating Ideological Impact**
            
            I'm re-evaluating my ideological choices. With India posing a significant Cultural Victory threat and global conflicts intensifying, I need to ensure my Autocracy alignment doesn't hinder our progress towards a Spaceship victory, especially considering the dominant World Ideology.
            
            **Assessing Military Readiness**
            
            I'm re-evaluating our military standing. While Russia's strength is considerable, their unhappiness gives us an edge. Our own force significantly outmatches India's, and our ongoing war with them presents an opportunity for aggressive expansion. This tactical advantage will inform our next moves.
            
            **Prioritizing Science Goals**
            
            I'm refining our technological trajectory. While Satellites offer the Apollo Program for a Science Victory, I'm exploring if other techs warrant earlier consideration before committing. My next policy choice is "Free Thought" to boost Great Scientist generation.
            
            **Adjusting Research Focus**
            
            My current thoughts are on fine-tuning our research priorities. While the path to a Spaceship victory is clear and well-resourced, I'm re-evaluating if any intermediate technologies deserve earlier attention before fully committing to the end game. My next policy will be "Free Thought" to boost Great Scientist output.
            
            **Analyzing Diplomatic Landscape**
            
            I'm reassessing our international standing and potential threats. Despite our Autocracy alignment, both Germany and the Zulus have also adopted it, yet my relations with Germany remain poor due to denounced friends and warmongering concerns. Thankfully, my ties with the Inca and Venice are strong, though their Freedom ideology could pose future challenges.
            
            **Addressing Neighborly Tensions**
            
            I'm considering our strategic position, particularly regarding Russia's considerable military might and hostile stance. I'm exploring options like adjusting our persona or relationships to mitigate this threat, while simultaneously reinforcing our path towards a Spaceship victory through "Free Thought" and prioritizing Satellite research.
            
            **Focusing on Offensive Flavors**
            
            I'm currently reviewing our strategic flavors, noting exceptionally high scores in Offense, Defense, Mobilization, Military Training, Air, Ranged, and Mobile, alongside Production, Science, and Spaceship development. This suggests our current posture is robust. I'm contemplating whether to refine these flavors or maintain the status quo.
            
            **Stopping Cultural Conquest**
            
            I'm realizing India is an imminent cultural victory threat, having achieved influence with all civs. Their ability to build the Citizen Earth Protocol in the Information Era means I must either capture their cities to cripple their output or engage in prolonged warfare to halt their progress.
            
            **Analyzing Global Dynamics**
            
            I'm evaluating the current World Congress resolutions. The Travel Ban and Sanctions against India are beneficial, significantly hindering their tourism. I need to assess Greece's proposals, particularly concerning the UN and World Ideology, to understand their impact on our trajectory.
            
            **Improving Diplomatic Ties**
            
            I'm reassessing our diplomatic approach. While Germany and Russia are Autocracy allies, they currently view me negatively due to denouncements and warmongering concerns. I'm exploring ways to mend these relationships, particularly with Germany, to solidify alliances and counter other ideologies.
            
            **Improving Diplomatic Leverage**
            
            I'm focusing on solidifying alliances by improving relations with Germany. Given our shared Autocracy ideology, a boost to our standing there could counter the Freedom bloc. I'm also considering how best to manage my relationship with Russia, whose formidable military poses a significant, albeit potentially manageable, threat. My existing strong ties with the Inca remain a priority.
            
            **Refining Strategic Priorities**
            
            My immediate focus is on solidifying our path to victory. I've decided to implement the "Free Thought" policy to accelerate Great Scientist generation and set research to "Satellites" for the Apollo Program. I'm also explicitly setting our strategic flavors, emphasizing Spaceship, Science, Production, and aggressive military capabilities to counter India's cultural threat.
            
            **Prioritizing Science Boosts**
            
            I'm finalizing the immediate policy implementation. "Free Thought" is selected to maximize Great Scientist generation, accelerating our Spaceship victory path. Research is now locked onto "Satellites" for the Apollo Program, and our strategic flavors are being set with high emphasis on Spaceship, Science, Production, and military offense to counter India.
            
            **Optimizing Next Actions**
            
            I'm finalizing our immediate strategic directives. Research is now locked onto Satellites to enable the Apollo Program. I've implemented the "Free Thought" policy to boost Great Scientist generation. My strategic flavors are set with a strong emphasis on Spaceship, Science, Production, and Offense to counter India's cultural threat and accelerate our path.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: Xt14SS4RMVfCWyww
          - toolName: set-policy
          - input:
            - Policy: Free Thought
            - Rationale: We are pursuing a Spaceship victory. Free Thought is the ideal policy to accelerate this goal, as it increases Great Scientist generation rate by 33% and boosts their instant yields by 25%.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: Fps7E8KBfTxEbqgo
          - toolName: set-research
          - input:
            - Rationale: Satellites is the critical technology that unlocks the Apollo Program, which is a mandatory prerequisite for constructing spaceship parts and achieving a Science Victory.
            - Technology: Satellites
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: uWYBN6jtNmn8Ijj1
          - toolName: set-relationship
          - input:
            - Rationale: Germany shares our Autocracy ideology. Although they currently have negative attitudes due to city-state competition and warmongering concerns, boosting our relationship modifiers will help pave the way for a strong ideological alliance to counter the dominant Freedom bloc.
            - TargetID: 6
            - Private: 40
            - Public: 20
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: VhYYZpNAS4cJb7oH
          - toolName: set-flavors
          - input:
            - Flavors:
              - Gold: 75
              - Espionage: 85
              - Science: 95
              - Mobilization: 95
              - Happiness: 85
              - GreatPeople: 75
              - Spaceship: 95
              - Offense: 80
              - Production: 95
            - GrandStrategy: Spaceship
            - Rationale: We maintain our Spaceship grand strategy with maximum focus on Science, Production, and Spaceship components. We slightly increase Offense to 80 to aggressively push against India (who is an imminent Cultural Victory threat) and raise GreatPeople to 75 to synergize with our next policy choice for faster Great Scientists.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: Xt14SS4RMVfCWyww
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
          - toolCallId: Fps7E8KBfTxEbqgo
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: uWYBN6jtNmn8Ijj1
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: VhYYZpNAS4cJb7oH
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.