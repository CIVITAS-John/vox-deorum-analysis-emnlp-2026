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
      - toolName: set-relationship
      - args:
        - Private: -100
        - TargetID: 4
        - Rationale: India has achieved Influential status with all 6 civilizations and is extremely close to a Cultural Victory. We are at war and must absolutely crush them and capture Delhi to prevent their victory.
        - Public: -100
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 50
        - Rationale: The Inca are our strongest ally, sharing a defensive pact and friendship. We want to secure this alliance to protect our borders and cooperate against mutual enemies like India and Russia.
        - Private: 50
        - TargetID: 3
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Private: 40
        - Rationale: Venice is a close neighbor, trade partner, and friend. We want to maintain strong relations to secure trade routes and diplomatic support.
        - Public: 40
    - #3:
      - toolName: set-policy
      - args:
        - Policy: Free Thought
        - Rationale: We are pursuing a Spaceship (Science) victory. Free Thought will increase our Great Scientist generation by 33% and boost their instant yields by 25%, helping us race through the late-game tech tree.
    - #4:
      - toolName: set-research
      - args:
        - Rationale: While we are pursuing a Spaceship victory, India's imminent cultural victory requires us to prosecute our war aggressively. Combined Arms unlocks Tanks and leads to Radar (for advanced aircraft), which are essential for conquering Indian cities and securing our borders.
        - Technology: Combined Arms
    - #5:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Mobilization: 90
          - Offense: 80
          - Defense: 50
          - Production: 95
          - Gold: 80
          - Science: 95
          - Spaceship: 90
      - rationale: We maintain our Spaceship grand strategy for the long term, but significantly boost our Offense and Mobilization flavors to ensure we produce the military forces necessary to defeat India and capture Delhi before they can win.
  - tokens:
    - inputTokens: 25646
    - reasoningTokens: 5105
    - outputTokens: 372
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Science Momentum**
            
            I'm currently focused on our science trajectory, reviewing the reports to understand our momentum towards a science victory. Our current output appears robust.
            
            **Assessing Cultural Threat**
            
            My immediate concern is India's cultural dominance; they've influenced everyone and are nearing victory. This situation demands we re-evaluate our strategy, potentially shifting from a spaceship race to a more aggressive conquest.
            
            **Crushing Indian Influence**
            
            My immediate priority is to cripple India’s cultural victory by taking their cities, or at least prolonging the war to disrupt their progress. I'm reviewing our next tech and policy choices, ensuring our research path supports this aggressive stance rather than a race to the stars.
            
            **Choosing Autocratic Policies**
            
            I'm evaluating our next policy choices, weighing the benefits of Rationalism's "Free Thought" for science against the advantages of Autocracy. Given our current situation, an Autocracy path seems more aligned with our immediate goals, particularly if we pivot from a science victory.
            
            **Evaluating Policy Synergies**
            
            I'm weighing Autocracy tenets like "Martial Spirit" against Rationalism's "Free Thought" and "Rights of Man." Given our rising war weariness and potential Golden Age, balancing science needs with military advantages is crucial; "Rights of Man" offers appealing production and science bonuses during this critical phase.
            
            **Adjusting Diplomacy**
            
            I am reviewing our diplomatic standing, especially with Freedom-aligned civs like Greece and the Inca. Despite ideological differences, our relationships remain surprisingly strong. I'm considering minor adjustments to ensure these crucial alliances hold as we navigate current conflicts.
            
            **Securing Alliances**
            
            I'm focusing on solidifying relationships, particularly with Venice and the Inca, to ensure their continued support through trade and loyalty, vital for our current strategic maneuvering.
            
            **Stopping Cultural Victory**
            
            I'm analyzing India's imminent cultural victory. They've already achieved global influence and are poised to win once they secure specific ideology tenets and the Citizen Earth Protocol wonder. My focus is entirely on disrupting this; we must prevent them from reaching the Information Era unimpeded.
            
            **Shifting Military Focus**
            
            I'm reassessing our Grand Strategy. While I was leaning towards Conquest, I've realized we can maintain our Spaceship focus by significantly boosting Offense and Mobilization. This dual-track approach allows me to build our spaceship parts while simultaneously launching a decisive offensive against India, aiming to capture Delhi and cripple their cultural victory without sacrificing crucial scientific advancement.
            
            **Adjusting Strategic Priorities**
            
            I am now fine-tuning our strategic flavors, prioritizing Offense and Mobilization at 80 and 90 respectively, while keeping Science and Production high. My next step is to confirm our research path after "Satellites" to best support this balanced approach.
            
            **Researching Defensive Technologies**
            
            I'm prioritizing research towards Combined Arms to unlock Radar and gain air superiority with Bombers and Fighters. This will significantly bolster our military capabilities alongside our ongoing spaceship race and strategic offensive against India.
            
            **Prioritizing Research Boost**
            
            I'm now convinced that "Free Thought" is our optimal next policy, maximizing our science output for the spaceship race. I've decided against "Rights of Man" for now, as the raw science boost from "Free Thought" is more critical for our immediate goals.
            
            **Reviewing Alliances**
            
            I'm currently reviewing our diplomatic stances, ensuring our key allies like the Inca and Venice remain supportive. Given the war with India, maintaining these strong relationships is paramount for our strategic maneuvering and defense.
            
            **Researching Critical Techs**
            
            I'm weighing the immediate need for military advancements like Radar (via Combined Arms) against the long-term necessity of Satellites for the Apollo Program. I've decided to prioritize Combined Arms, as air superiority is crucial for crippling India and defending against Russia, even if it delays our spaceship victory slightly.
            
            **Researching Advanced Military Techs**
            
            I'm focusing on Combined Arms to unlock Radar, which will grant us much-needed air superiority with Bombers and Fighters. This is crucial for a decisive strike against India and for securing our borders, even if it means a slight delay in our spaceship race.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: lnOYEnvWl2oF6Rj8
          - toolName: set-relationship
          - input:
            - Private: -100
            - TargetID: 4
            - Rationale: India has achieved Influential status with all 6 civilizations and is extremely close to a Cultural Victory. We are at war and must absolutely crush them and capture Delhi to prevent their victory.
            - Public: -100
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a19ehwRPDEZcOZUo/9YiXzQK9UrOKpH94JHmzgzcvhaK8NL43dh99uxk+iT6hiS15QCpYKhrrt2tTLLyooKg44forZyoApHcdfoORIxPylI0l30sKK7P0+D3Jw1CJkX5ZCAWBp0nOXtALGg97nQbfOsDHkX+6yJ6VSydWDai6HPwk96g4t/Vg1VLck4OEvGmkjpF4mG8V2b7CLqcvah7xDxdcgzEw4enhkdPT0IYtESQ2t2sIY56IWihtPLcYzY2LNMcfldY0H9HDLiYTlTNaWB90Stu1nQTxg2mtRdhOn90lJKRK+9ayHfL1HUMGvOYGJZuYqXMw67Ri6QcIB2YYmypcWQgLF3x27m596OarNTf1GM4LVCn4SvwJm75WcbpQjQpRPrD+fTonL46h/IJEDd9hcMwOBRF0mZrtFxZdwrVfBayOnxvT1nY0r81Wyu1FScys5NWDVgpL68+3JHkuoXnu6ctal+TLLe+USPBuHwVtK7WjkU+slUoIlen1GNMlcGGqblogWRk0fqrPFZhBcVvnHvBbTbiDFGW6Q3+1wozm/iIU8fuSb8RUqpjFdf5q/xIWcC8HImwW8s4gN8WkZkqC18Hna0YVvH7lBwOy1RMPHtT4S2424lMSSUp3vvPiv8hE9jYLiRhBSa0Id8WhbNJ/bxBTKqxKT0tubRcuVmsHGf74uhMhAuPlVB5fIICqG0hW2GIgShnOO8hKniwBdPZPMzsotDiiHANgvTteUF2ew7A2FHWbC20rt67rrp5balVCjZYJmy7xlVDIT+TNmtWCUDkVrmvbOdZBqls/1j7owcwtlY54up3B0mtfQ1/WnEgHmQzljCF17Y95OGnlLa2otc/heMR0W7i24B2g780WJZhdkvF+Wt3PIW/YrxD3FiLmARNYET2Jz9J/bsyQpmZXrY29FIQpWqTPUrHG53HKRdIUx/wP2GCgUQeY2RtSM8xM+8fYUS90gXOry0BHBFMPoXObNAVHx6oMAK3ATzCfRPCIgHfrcRr9hv6Ex0myLobUQZ3+sdQ2u7jfVhvFfvTfXUTjCVOAdyrDRFvAm2WPdg1WEx7EIsmV2aa3xAhlpzym/1g2hsv1kw+6nE79F6/4EednpH+y5S3G+MECfNhYgTBV2kNAwd9FlF7Y36P5fMwor7wKEdpZb3C0HSekkLJemt3vMibEM6rFckJFCAV2+G8YMfPLLiL3Yjghl60TqzIPui1a5p5QfE8DdNtDSvWAbtSPxOE1g0TsawbkwCmUI/p9Odu+qQ0bI0MH7+BOEL4StW4GXfRggLZRBe/6a3GqXSi6YDq2pTBL3kUEV/zBO5AgBhuMM4rq9t6BP4sOlI8sgrhhFqCEAmpkJXWR2PnoMRxoMA5lEba6KZZFLJaHzEGX9gzkJREEpAUgGTAqkVQZaLiFp74CywMe4EKUMRRVAtebZ1SNvRxHzNgagMbtlHBlM4O7Yx392sGz6Q5RefDzptiR85e9F/ZBBf9YMApgYZ+QdjlzHHvyqoJQ/7OFssbdhSgVfM/A71sm/4gEhZypwD3yNO/U7P8j+Dyym/jX5qOFReWwwmjS17B6UHQzviqHToutGE2608eJXA/KzlLWI+yQW05LN2vSJuzKRMYPr3IjEbns27KZeo40sfkMfWKHcrvf76XgHZdIJEgUB5pIwNiAvSFkq/A0FpufY4e4s0I2n8W8mTziL1FJxFgwfEwkeD/VbwEoBrkebdihQYhuRnF0WyE/b1AX+M62XDWQ1k6zNFsWNL5nmJXOiOOiUNcxzIv6qJLR4pK2KyyIqL4QpyfTA0M2pA0LDv6IRd7EhJZn5GzByDarTRfqXEoC06r+RT1oUIJVn3Zh4EE9fo0P5TrAPm6bREJ2cl6Xlt2tj2wTCNuCt3FpuNBnq1cZZMt+cDdBqvZRV6HDNeFNnQ2ODidG+BNf/kBo9lAj7O1G2gmcUeQoxZQCA+WTGqaeLDTzUxU4Xwsj/cARK739uMeh7310e/OECZoD7KUH0hFVSGhgcE3dBDgJ+6if1oejpq9fus8CMchOrzgR4lupS4nb4ZjGBnXx4W9YFKJDKzuOeHIXDAswiait+tZ63hhDps67je3BykrViJITElpcu5AalsevP4+1qP6tZWIM6a5xWQVHdYuntyLoK2PTNidja4MUxQApcSroHpGPRgou1u6dxDd4bkvdIWxkYZNhDLeaTdpEmGTBKcJ/9Dv9+82NEOIZD84Fwtfn0AkvPkUCC2yk+85GKEFJoDpeBbJEKymtycGQhnYGzFSpNdbYl3oZ5agdyhKyblFMAFSmNk7Lhmp891gF0DzNfYIkG45MhKcBexWNkXR6B7h17v5M/qOxPxeGg12zYPPIhlK7IYgb2wNfFznn+rSBbkvwJcPaOlBoM+O9ElE/7aLTZY8sS/AQRAqfucM3S8UbMJYakdGVS9dar5hAPkitii8phsrm6ADO/I/SJntbKGcYBJmARM9kVadtp9sP1bkNxjFAhKUYPBFbTSTjywdSAOd6+KgtvWfJCSbGXWW3ZQ5bUd3qYIiLFfQAESKQR9l4iRpqzKkPpUKeizKn0oZ7Rlc6QOmEE/uvdnemr6d/8gazVugsoqxHHGNJaClstjDbRYT5H/lrWaFzoi35tipWBTxY/ftHi4iZ4CMK3B+NME130Cqe/MPmObgyy43fOi9S3Uww9dBpLr9hojt35jTnAAPLIktArtoAoWtivHTnltsj3zpuBn4fgobbp9O4gLAWhoPPyPuS2qEzwuSJEPsN9dz8yOQOXuD6ad0o6OcLAlsrgTASnAZlI9yN31CXSlMeMRUHbHdPawTEgi2BPHVJazYVVG7gpE19sp6RhlXaMDQNMeKK3eiPr31sgfyWu+6vO/nmfTipMkDfuKzz1Tgqm8ebsnTii9crfVc9OzU4u3+ogLXVArQt3Y3sSkBYzsnebK7CEfXxDIc12JZvsIX7YfJYf1kT51w7um2GhR6nopdK0VBthB/YdTgwUjUmcFCo2DH0jE0IrOHWCyv9F51rPBV7wgn2P7KpgyFQqPyuIYzwgj1nvrIFkYHGoEXie06QXPNdqIYEY2G1/tpkJlggW8pDTEhh3GDM+dGf5Ht1WVuYvQrmXGZEv95d/rNSqvCeedPVOQ/MMg2fZCyL67m+D86Oc6+V/osU8OW+KNagjNXGgCYfr8IqfI7mBkVGiBc+J7JmMfgtbYi7C7Z7VQL8TRee4ZXmmmnUkxlrZlO9B6CvHMs/xMXXNPwvESU5DkHZp9Ms/lgi0P3UGOPPY6eeoz7r7zF7vk+iMoGp5UaL+XuksrmNS+Vk1FfNJn7ngGYwypqKbBdHw490PWL7lsG8zonENd+Lif7MgzWGOiEp3wvlCDFaKA91LY87zy9GY0fyCd73VkaVcjJXv7dS1WUnOdg5BjGQOsk7P7P3jsZZT/ntqSn9T3z/8J/ENfZ+953eclzG3HhAoJ2l8cQsC09DM9bhGE7FGkpFeRfmw0qVqA1wnOabBHdBGn7417Yi/u76RF0nU2D4W5a4PQkcDRSkxHuY7Fsk3RzTD5VLoBRQgoFPIb+RfSwDNL+r2n9ceH0aNxhLZLwyiWoGCgmCvpnAmb7OoSo6ZQC6oBQRj6tr1u8DY0zUNJLyAWESRy5vv97O6OUf+vVQQuvSuxXS9QDktX/vMYtpY+7Wva3UQgsQIFSbADNJS9ymzPpF2xa+yzOHaG1sm1YHSUzWHJ+u0TlbmMl0uSeDmCAXl7xQgC0PS5BkcaVVNTtzY7ZrXq7pD06A78qQXtI//VAZz0tZelaKDhZO/ympF1qVon+8vHZ1Whz4/q0ebN2FOwS2Tyy2rWSPBL6ULjI6oXHKSyHJLR+aijD1v1Zix5KjbIAASN84wrk4PjMp6lFDHN8/QS5gbS012trRIGUX1z2iqFuMyZCZJhFPDNUxwd1Jy5oseAqUZDpH48AKdZjcFjPawddzo0Z0Hrkn6wbSj4HPcJNuxUHljZZb6ET5aG3IVpzGl3/Iuzw+IkR5Wm7lCga/L5xXreP26xim7c2CECSVAY0adeFFBotgyXMUtsir7fzXtQU0YJR9QTdjIvPTqRDjARZrJ7FHju/bPbZC/x1LjVGnZQAfQkiwR0ZNCIWyHuY1m5SUqwZjpCrpDuQXp9Subjo7QCD0YlK9qVn8Fgr8mZORII7AL8uBXqHSi+Bm9H2awJDXzCrnMTpYKoAQeirbAo0chobFKo+iTqTy1NtQbM5DwOhgkwPMHZCxcUHkLCgSUzD33F+Ld8Mpg0Z/33+68kQCQQ8khsFsTJdZKadI3CF18JVQO4f6tvlBTDC72atV9zKVZTsHgWzDj2N7AYix46HCKUb6kEG7fFJN7AX6nEeWNtW33Pt52f3yM5qvEB+zm+yjY/40b9z9OMM4DMNDUHbpiGjaUSaxj3UBSjh01vm/TN9FeujoUoKC4JSgY53Hevpg86+GRC7XPt01RYEtYiPNFtmGQPZkScbnAA0WGGZeNQmvGDLfc0slYwWiVuXCRWLRf2jLJqViRyID2c6tqnKLaY2NJl//qrdj3b0PaP4Cf+KZNPApVwGPJNBibfYbcV5AFSIMPMhvl+cyTVbW5p/JLGcQtLdVcyXqLAwjElKCVB6wZN5cTX6WpL1/+sQ0JSaJGslnJGe6ovNcX9Dj53RhHlbGQ+SU8b9SXx5ubdmr9zghRWVvycSKGD8yXNxuNFF9cTOD+UaQDOpBHn/hwjxbctdQNAWKHmfi9HO4mRW/PTDyciR/p6zRErcoIkkOIyThAC5/BGX/cjzGIVJs7JVRL/apbJ0P87lYrdbhw6jTWBcMomXrqlj0K9tRLJDETcjXdnjXmAkmYetFgd10ekbiC3Oljq4usiP5wojJP/4U1ZII49TTn+0qOB/EarKVdhCZsDb9RVXmFnt7kCHIfMG+oPsZj6SCflzdCGOSVO55pbKOTD+Q6XxofsXHtiMq1IxDn5vy+84fMyRw2pRTuNZQLpc6ANhWE7MIlx7mvaVonPmFSh9sibw93JEPBnO0mXQWiouwFHswGdHI1WBbDzcOS7ff6z287oxQDSwihVTCqLSjp8iflPWvPedp7tEfenjxrOBDWY7hqLq/BCYWvrLLIOIAPDmsggw2DmzMztMKpLlI2vMI6t3iqw0sZ9cy6YtBRa311qbnIshq41UyJmPiU0eERuComLjWTHuQKm4Eiq3/1C8vOAd/qDFaZYyxOkADlMo0Y6/4qO0bwUCc2QxLHdJKk78WWmeyULHJW88euRyn7BVyK0HceR/CDvM7AnAX0N3okuaLME1ParEeKj3JPJ7XUKDI9x5S8nVmRIu9uTi3y+gKbvJ/KCtCsiGlDt6va3Z2n9zcHcm2pHz3OoTtmm82C2KcgT/pCEHPHbawVJM9gQOszzf3NOCSoiK8INQNOOtaxK58MF4pTi+vaHZXwVyz6ppZBdSvSyBTJ4IYSBWXkJotiN0qKg9AYTLgkKk0+2b49dy4kGABorNp92gDj/AGbz+9WC3sHNf8vm25twVTXyNCeVUA2iFabeNjbVgr0KhEMvTNKEOuNJMaMizypkr33uDqj9DRzLxd68BqtYqtAjgbi8RV004po/SjFAVB9eYlK1LLNhy/nyqbot+buKT2nYWuLz2ny7osPRFFi4GCuldbHclR4G5XpntA7VebjHUp6xkKvCr+AjCjtCbsQCjM57cwvhXNCOsVA77a41m3u9qgU8nQltOc07V/OQGZwhwBcONXdjhjvichLfmuBVwrEUN8oL7bOB4Hn3O4CJc8qvOnyPXCVWf7RivaVFBW6hqQpWAuKdbNZWTzBv4fuN2Hiv98kO/yTyYKq2HCTtvUxWoiJmZSxxKvXx7Z2ntkwxiGZMuqfadnMo/OX63Cw4g1sZihVbDh+g0CYWAMDIFQn+58NIxVVLuPG7DW+4y57Hycuq8cUB2nYTfzIo1DO1mSnlmRrWGhdBRAb+rMG9D1k6Bl4UfNkoqenFpR8Mn3XWqRmcmK++uxx6l7kVqA4CWALHkF5wxIPkDGptcPIz/GLg0hnQGpklvNqWjvW0/tCl3BBF7liZJomb+6ULz72jkaDrNnx5R34iXL9Add1VJBpbVPwtEpV4LqNNSQbS9UkVEOpc0F7Hxe8sR3f2wdOKu22F27gwAg103qVermnbJpH5+XxB4zjlQ+HHaurkCSjMk7pwHMKruKksM1IhcaoGi5kY4/6rnIG8P2gF41ROhqrPJs+6PCkL5vCzWytmlogG66/xdEc6N51zpwGwp9UrOkJPF0Hx6dLcKvb59cmagdxbEkIs5bU4Ia04+ebmmhACX+VfZiAcZLqJt0E4p90UrNKStBqoeZIKKpfapfw+K0WXs7ZGUDgQgdzD/VPll+dWgFpaVaCt/IGS47T6pTv/ERIefRHMxggYNpbhvUyoK7trk08RqKJu4bKuOAmKMjMIyRV00WmqCvfKuNHjg0zqk7uMKzb3r+zAxgY2Oh9eeBUzVcr0LKJ/aZm3WRDIVI/Y81kSFkj+MozMX5RiRBiKbb4jnchiORYxnwdl0nRjZMsOBHeaDhjaDKPxV05sYYSPLfUXyzZ4yLSiBCSYx3zd8HWyeFK4E7SGbd05jfWN+1oke6fkmOe73V1hJ/dyExBogru1Z4j5pknrlCZhfAAR1ELbeTjmCNlMLSGkxRCS0KRn2zgfwjYrL5wkjaQaGhYaPhOKzzWiQpb+EnrviKPnhv/722o5lr+Liiwsi2aApbiguTlHooN2kSypa3LTN8NnsPGZkBbRwEFOwbzB5E91p5UyeAHwUX4nQpXsjgJcDp7/uVGExiB/qGpAP1P1+UsO+kiozfChwpMiWt05yENA1qI4u0vhr+WqdPoUyCBD1QvzRHnnM/N7zf54+wtAt9t9PJYyVMS81EmQt8AIDcGGOQoEXfBZgJYMBi3ZyA22VYGnmGXhHwkgbQAcxZZXC0VvH6eVHtOI4vfXKyBR9OD2SFQY71hKCiBp2KARWOPbxFhDLYN+GDXuq4jFaPdIX9BCoD0okbdyz1EXcicC8x8aIAqqG67bez+KV/YicJQopTNbLBMMH2+nBp3bBecXRgkCAIMO71qOZfTvoRKMbe7tiQEjdeE40RwGeaqWLannY+uGP8B4/PvCTHf0fh4QOJD14ltaD9Jt1E8mv4xnsnt7hwfTANXp1I9g4jMSIEMF+MBjsHwrNg5PeAe1CRAwNDa8IHZoVwmioOz8mKedBu4CT9LSxMWZ6sVldBarrC0tiVp15NCesQeo9na7EYeuD2gyuh3EtL3vGU2MmwOi+dC/9azd/NWy8ng/3NnHrvewrOeNhenXuHUJJU9GrwMjF3fHsLeN4otAWSnIbHETsRgE6uxcxF+swZdXHWFbSi/vS0q+UPneu1KMXvyWmcLOHDUg27vTzPdTOyLX49iVz6MYf/Z1gjWsdO6aACTBvXxFBjmHw+Rwks/m5CJshzhfOELqE/vxRoTe3HuRVZJ8iUUiw5LFKYIGF7ABGYrNWURgGmcXc4VCMJdsk1+VMB8gfwR95TsAtnoclWY1ilMqWGLOCQhEGDPxVs851vNNbg7PfKRnDmm3KLl31p1djzvSxTYgepaN9Jp5FVgKyxdp91KNuyZa4/lRbZSuYGObJp6cDBGUzP+Z8IYhgBy8C17+gHg8bvGVLZOAFfPy819vzgjIPcVVpG7HbtvoaLr7VV2vEQAnpjJPIUtkOPyNvzcTJuzM20QW5Zg7Lue8NLbrdN91dde5XN/dw78mxLwCFdgKOT4Yg3Jnkb+FwNJCQBcvpdylPM9TbSVnz/2pNraEtUai7OcoZE5/dUQNvuaS5sICI1CVBwHzTO03fuhgaH6Awc4LvKAeyr00pGdosaFAaGlzOWXk8j1FpPXk3VKqeulFWa2YImeWkibNpeuO6lOL2fpJg5Wb56pOLQQPSYKN6+rR09fQ9ivRwGgR31th0NmVdGlfQcnr+Y6LObIc4XQe57SCABQCYpAMzKDK/RHfTWe/3AWKsBLFc/+sOnRGuke1C54aKKoEjP9xoztz7INe1yzox5zRqOjQiW42Ae1vXHJgzz8kZPCwxD6FWfuLGLdEpSl90uJ3BgZ5Tv38AsMxQhiPs+/fJqMC4ldIm6/DWzlZMtM+oTMqhgoUm81pAclCM5f+Vds5fR3n3CK7cKK2wu0N5yCLin2XBGNui002pO5a6it6U5I4HTbWB7x1SEgfeW84+NzJ3V7UXn9nVmgkzZeXF6vnDwBVxMJGl8Gbeid/2L5tCd+JWDFvpBBqVJoxJ0Num3nkKAVP0B3v+ALVcI9VyXWyuxpO7WXVxiRjkPBGh1RZ62S+1zVMBQdi8KbTxa2EiHrUZ4wNmpNnuHku5O1NjMCwdJHtdmLgBWev5yNnydVRd67AGDvrcApu1U/Z2Z6wkCc3Pegx2Gn8MhI0l1SfvvT7CdAhA2IcBNcSIsnMgprje+P+G1vUko56PC5U8WGZZWga7q0TMRl3L69oW5RLbHu78ewSZfhVnuY5yQbI+NiOiplr5yrww0KmNJMvI31W1AppgFewrVMHpLb26ZVXArXpRDMoqecJ4N42RgpGAs4XpC3CTykWROZMPUguharvBYXIOzyXi3+XdhynqSI8mowlKxD9HI1OMCeHeKWlV8x861Ve3C8nMRe+P9uyioyiAOvX8f4G46QJtER7HqT10QTuue7EQH9DgliPSUlLh6pq98aIjboqhjhJMejnhSHL+w7dvFsbbPP2zdobQ7zwqiN2DVlVe+NH+EV8Ec5O+XPFbWhajbPIk/YQdAID94Cex5y21fM1P2ZwvXprx3PCleY/0JfQrqWFqXG7bSobH0pP1BAJr/FSW05+sE11EohOOh+mwAAUexfD85kIRHJVHau85J4aL8dCd9NU/Mrb5tAD7hjUGLXPpM4OjPI/mGMCxgwxo/6ulgnaMW+9U1i/rnW5rBgu4IlCzMXruSQvQS/kDznHGjCuAbOybWpkAHfz0aqgFuuxDUn0ZFbvgROvPSy8VS5HGe0pqT0gANpA4GM2UEO25MHWtrZaajO1wqq8PxIDwXb3TXWZR/97+EiH/pO93Bv0UExCWRppvcuViURr/4PGRt7gQ7sqc5oBvVr6rxppzCqu2oi2AzKVanl3Uq75rFUN24IO8cl2PTi13ehuPgO3eGrys1BaHEVIZwmB5tyC/qzAAvjkyA0dPGeeZyYw8FqN2Vy8zrDKYGZQaUDckDkilhp2zc3DvPirZt8FdznKseePir3H659B7pRf8mfrl29YYBxqT2C5Di9Eu6CiXE7uDNKmGO9aOGdYIGR8YSJBWQINeK6Jiz3Yvfon6yhTzVGui1kCZl1jemxWs4oggRuAhHY1xQpkbjbTXi7iDhokp3hJtVJISEn62KSuJz8SUGMuxLSaMpGAlZYEntV+Pa578gzzWBDrQiHddnoi5uzeoyOrYAXT0Htmx3ULSif7i+GpjBv6D7tuY2LiBD95LUHkTqSYYPTqAf47yG6YgIfeL62FPFmiErkVok/HKZFbCHoueRzqnr4+M4Ms8CbD6P2zHzxLVd7A9RiLZDPo8An72ZzFR2enaGrfAAKjJwmqKQ3csYvpua+Eu1MivxaCWsoTcPEgQoktYfN22kPYFh+2iDoWDypJLPB4/j/6JgIKhGHOt/X8CBNRfz+L4P3Yr2noQ13wp4hYg1+y8vVO5+UEADeOHh4bE1Ii+08X8CfR+DIVIlW3bw8yxHUBlCIv2ROMS7EAeF51TGdOxofb6bouo0EXkfVCIe9YIxxSLh0DetU5xl2lRL8YRwRg7jz2yJXPm+m4IYbPCEJW8kIeSTnQjgUehw5GxdMPs3laSZbzkuwOOUGKI915G3ydRBM2+kE7efExateuRLMk4oL5zwy7ei8BcLN6c9emaluaxrhFoSzVkcWK1Wh6A2/PdMxMVoomQWCpqmYFjPUuXHyC0k15oBuqhGVvCCmWmXKTsGlUPndYBPj/0SLTQIKjF5a0s5Ejbg1ZTy97FtNIRTPeEmEIm6EL98SIBXea+OaIbcXsj/gJkuzIRpFM5JtVlPOcKPiFJ8T/jF/bSLeW7muv+ZHdV0fy6F640g4l66gNJj0izfcv+Q0EvvE5/GAXZOGBtxssy27Baj0ja8S5ll+5bs5zcj5ZX9ztCZ9G0jYRPXX9iyMUOflHLWRuFJ7T0yReMVtGRdKyuYzxcR5xmPvZRwMlCnrdGyOmDVWwPGixy4gIHMwg8ex7FdzPEW1ur/n3y9v/hERrY/j99keC3OYrBrwYA8E8zcZ37SAP+ESDpj9UWm8zmns1XtAUPdlfavnyq4BKAqxkq7a4kGKmVVPt+eHBYbZd/02UI5WtCNLtk8V5o0Ma/gPiNMPLOdtJulblCc4h84axNhiJ4ZarNHh+7lkc9PBWGqRZo+apz9JfLvpB5uo87NhKBQmDyDy+cfmDzyhmNkRgmIXLIDsw4Md3ki5vXteWY7rMMoNvP58FBmvOiyvlB6o9WF9bUCEyt/MRvI54+zFCtPYKfkX+ZD2CRNQdM5fCZCPR37pv8BURtBcsMCbsQP6r5XoDU3QlLimSaJ7H7eUbDzppN91brnlU2G6zT2+lzgNnB9XJ6SUnayA5Ydbbwp/zfMCv9wkpJRJfgWrhhRKbzUdVcSVkJ6wxCbmjxyqET8kGdJLh5KGzGpvGlvKpglXUOLPg67yTloNBbtORutR1twOurqPzzX0h0/CNkhy2rg2ZguOBM84srK+3FnnrQDqpSHJETHR0nfgDyI1gPrg872TLg+8Wr0GynB+TJXEvG7EtflDac+IfH8Pjtsd5DUJ76M38ktuCtRXnYFPUosQEHQULAXFe181QLVl9A0ag53Bw/vb3OkVRanRYJCDgXx0QiYboP6Wd4SZ4PrLv3AuzZWTRBZ4kc2t+5EuOOwn8JKKlxTUWkPQWBT+4ZSxcFKPUpfPTGUugUQdzkquWDDwZd4O0XkU/HKO60MAezVfr4p3kWKSViTBjRpPjrtyTeCMxXx0FCoA2mjrT6o6MJMcOJm1VwVv9MtsyF2MUNnuVOFmbkJDx+c0aEfbNLL0tgq4+AT1fW83OQdLAO0Zc2DmJ4jVJAF7fR2oveU1LRAxo7fWTnPr9iny1lArggRcreNO8p+mE+vU13CvrSnuxJDYyZbu690v5/lgpH5YKGcrjZ4R09Q7iD4CH4mIOzpjVgA4mmSLUJErXcuGx+UFM+mn0jv4bXJV/4OyEyo26UzocXM2ReKnc1u/DuoNMhmYD5toHK40IHrIM0uTZenrhT/t6aoyFn3aKVsJzy/mNKCUv8H3dSMyuufWkU7Ovt43jtllYxZHWGcaD+oporDyuXpDNG2vodPrvRLiYHi/+r5+8OCA7x65xKsKq1JS5r8MN/962XOeuo83ZU3sicJRyQv1oq9C+Bw8MCrniICeEcLjnM0BmrYImrw838OrPXTO24yOoTrof6E8ulonzWfvErOYx2rHaDVAMDzGMJtTOqQjSQAtJtw75zK0E0eZ2Tp+zqjGs19J+ajmw94icU5LhdfFYSo6i2T4AJHGordLTyJpY6XoIJGERm/evtGgtpcni024414MGoYcwYrGmOCeBJ4ucvzRc/qKHC2CqjVMPUT5n3IjSFGDfnQNIbhkF5hf4cE6//dVFNM8LKS/POdBlISY0yjvvroac/KlhfcC9GfYLx8a8BltQlGAXJg2lqGPRdcpIbHshWByFsxd33rvAS9FSb8aErvz55fKZxPxRgRteNpI2ZZqtGpoYxJ8bBdqWLhNkCVBFs8Wj1MtSraPGTub+QC7Crz5Cppcvjmce537yuPEZopDhRD31HCg8uhVDqRuSo4Mm0h0nqHPoKih56o5kXUWSt3DWNmOc4ECZVS0d4KHVRZO1oFqvzVy1P3avEv+pGW2xcigtyEFKAO8OM7fUNWm5eA+vdIs5JZhoFAfAnzIXkmC6kPghtBzfG+5WukMjgPSmNM25ao4zIf5vV30+9ZEb5pgYdtQDFTfhi6okIMXt4zsbRFz4y0/KuvZVFyNO7LO5IwTY5/gRWPEqQiuPdzV6mbUqfZmJK+avjlJZc6is3Z73vz17RZT0v61ZM8EH7xudm0QXqJ5V6M1jJL/U8//s4bcDL4kdirx16VefpShcn84jaCplbE/0Rvp07Q00uNesTpyS6iSmPw2Bb1lAqW+6x3HDjE4EpaCGvS4UKOvAdq6nox6Tu8BGTo2wa1AI9rzlBn6H126HjccEGhMIJecqUcJ5oFkeRT+/Dlzx59w9pHEWKydLkeSVVz5cxCKy3ZJlPtuDs0gJyZ3bLKBT69eAUhln1KI3rPEox+/j5H43gNJI8/vbzqmBjk4Ki99PB82X2+YsecYYQkgxcCxo2ckyYF7/WHmxEM3YlodEppU5gYXIqJxegOnZ3CpHFmnDpyzc6s8EJARupw18DFNOe5UFFxztjBE3SQJDI3RBie0wogQWD8vYJG3g5F9pMwaVaLIqh2L2hhZQB3jOW6gKA+EHGhJqIftTlFV1RMubEI3Kvm2Tts+cMgGl4WevtCK5dln2sJW6hzarquY4a2GKYaSEW50zE9OfoQLCWKsMFO9QkWy+jw3WC6VZI6dl3xG/U0GBMMN3h8o2TjvC9wcx+CSniZYXYRMz1LiG+/APJRsdiJhL0ivKBt9Kn9h+aE6YwGr9+uPHQ+auVNNAdlOLKFa0SXn22/HSP9ofYxqEd0DH0SRSKuuHCg+tqw/jdc6/HCvLbJp+nk1hNE+hY/2J7aCCgpEAAXqjIwOCXHUGxikcPtYsMkXQMKNgkxGRAmn6FAxnZfnmdg4L17qdt48R+bArMNzoqMMl/Dxi1CFVROycpPn+Gx1wFZYo4VikY73NZB3UJ5N0mIvKg9XpTxiFkLv1mHCMWbLpJUuFggnujKDhwM7YcDwQcRGF1zbsdT85iJ0hyjCB+jnw9IUnesQHy9n7zCjDnRJLWt2Ut7NSpjhLEXRaDBn7YzHYLIR7YFH1KY9HtK5c3OK/fflbbfOcMEO7tw/i7hOnfXmJ7KGe057J6TPHGr9Fi6FUQacsf2xJrqOwPMER1WJx0fVU0cS2wvB+3cempfbrEf/C0jATFBqeqNFiWNHkTtFYGO7vwGwqRKngWF4m+9J0tLpLhz5vZDdLtaePqea6qku5jNtoenQnkV5JN4NebGasPNSVFBW9FEsMjJu+hjqKZ/LAWoE/l8RWBO7LEr6UBlmrdnvAnP+Dyl+KeNLqq2Z9exaNk7SlxxetSpwD7oSFnKEKSW+cpJO8b4yjMActsb19xlkfkFAyPG69eeJv6gKXnSbtP+Ceqip++lydOTMKVjF9t8AUTOZnsjOzb8OdP3SGKDkUlx19EYFXP8MXIqKH5vAvCLnGR6XyB7gOkvF9U/5yhrZYJSuClZh2AW4cRqz/mm9HyNd76X9skvvtf2m7qENmkzC4O4d+Svp3caGYj/oFLKIEn4VaK+nTFf8NNLYcRb77Do6u1Rh6Ul3PiEnIEcGXU5il/vJ2rZO4EcvRvLtYDc6t/xyNpOmAq6nWWT1gvIIGitrjhP5XgDATFbnHXcFdJEwC5+Pp54o2xk+KpCsUUi3ekvUR2s1C5R8clrh7Xzp1qvQVs2+zO64AXvTi5fEYQF+k46ja4LCBOIZSB2dVWkoLQ6t5pAGkWmdDqYR4Jm1MD9E0FvYeRGva30PUeyLnSz2C6fCWxDETFTuDvyuM3WFok2SmBs2IBWWAeA5zZhJQATMzT69cjk64znExXpU3kS2YyAyj5516j8FudRqMxVtacUEeMZSR+K3ZRmhjD/WsGeKRinCFOjTo9WwMs092qz3P/+4vk7xCEIJeSyNSFXEAvR1s0m1SB8zvrgx8W8U6UBK7fgRGzhH93W8A6DiiKIA+VID+k1zN3690LWGGiY6ycbLVr5HVCItx73s5+fLjW+d7phGrn/56/W4l3hq6sje1X969b5Xs9wtGmqykxOvAYTzxSK2tAmYutSkH8AVyzwMEpJaE1uzAGJppOtlJuOSslnC7+pOtpV+JQPJi07enUFr/ypBcrMRvQVw/HeWqSDm6ax1tbRz7TEJ11B1EfSCQlf+TjKgl4f2Y0SRlQ65OrzQ3Uzw5r6O3KbsXK4BLCREuLkp1PIqy0WEiHyjfcnojfuGXFBYxSu/XmTuTco+BvsJxDC2MS4aBokcuJup8djJ9OuEoz5qWk4uXFdDzEcXEBDpPyVE8+7Nj4fC+m+a77aUSglULig+cuJNqmwhsc/cSE33esAbE/my10EM5fBIid+6TIgeadQK4d9VNMTVax4S6TFA3e21YEydQtQnuT04+5i0DU6rBPaCpFXNWXWC+ABFCREK0ZWWRhvab7GLd8oZXA9R8Y0P8UCF22pYm0JhRVfVO0pBZhMoL6Fh4/bNZPECfrvYmmK3DAQBEdfW31iC8TH2NAwh+VAMkqNUodPSvXsjigIeJR91GyH2aIU7/Wn9WoRDRI9oAMEGm3ye6d+OC24ysgwf84Y5Ti2NvFQJEAGMLyRspZQ8VQZ1FZMvKr2jGwNQflCxYDzTf1KB+5nL6gBPeENfRXV+diqqOU/QvOXxjty85uXw2E4x9o1lsgEGVGgHCl6C+d84B16RdQqAYPEIhUFvJrCQwuTnoYl7KaZtUC5vKNqGtVQS6PbcY+nhyi+95lAIrW3w2aPk6ookM798h9xQHRrdzwGJ0PY3iWMSgDB55shMeNHA2aTVZxLSIqwWmV3/XsApAnDd6uCceEGvGNjUSWhYU2u/63Sb/MK3i8Zzpae0448BXCqhatm6Gm8jLGGhSbzhrW1LzTLgRyYSkG5Hhqr2/sPo+t/ZRjUTqJJZDNEy8uglBCx4ZnepyZ4RMhDOG7OwvtiqdGPEYC9ZBG0exSnSUrKJRsGsf+4tlLAj5+vranvLmUGalFB+EGD8olfFZ3XA9NCvPurYk6MxWPIZnDBLQl9nGl74q07F51TDcRCvIQ81+D9xrmtNSTnl6bPErlSQvVNDv3ja7UoahMlsxr8YYVYKnjh/+kqv9LmchOoGUOoe3m7+d3HJGbVbEFTljvN6ZPKnrIpRwaFKW5j5h6Wvl7uoY/VGMhgijs2Ky1TkebqAoUEQD+0/m8Mw7PSSxR26Y8V0GPJmEjYS34wHi1SQwkKALni2GLhPxLPrhPIExqvTxs4Am+WAIM1A3X0ByL1Kj7qieeNmwOea5vzbI8VlkPqyL58yIIdY6pCKEO5gTegfAqjpHxBl0WV7RSHoMt4fRnbA7vfcPGxPqWJJ6Jluu7t2V+8qc2aaT59gGGto5pfeeCCG6nORSEdesLI1ki0z28sIOKX/Rim7uIHjm+nCzSq+Dk2BeTEvptkc9+xoH42xlABFFCJM2wh4VHlrIyz6F4/7KE9YOPZFHUnAZbPW/5WEgcGdiFgFLriap68CyEyrFmw53V9X5aN6PmhBQyaBGgN7ywwoWq+UWvxDvDFZ4M828KMkrPCG/CWBwTiAfbv485+fVcO5tl39yK4Z4DCbOPofF4OzWPusbohz8AWf7w/tBGmBdnjx1A+9FLMLHzW85wxZIrsQIo3nakXjQiSXF4bpFP4e6YOZhuLQImvZ6rNirdVxu4NuIsBJxC9wOh8I+KI9D8A6mXiIR4p63QjOWby4ApJuDI4L8CL12J7ALI+jZwRJgvcGajxuBaXGVRBAgzW8DASeE/+c6IclWT8RDvWzJ7dy7CcgtoCG5TK0dQaKJa5RZRm6+Kq3C9/NtWRzbvyhWSKZBCRPWV+p8gAeNdSHXWqirYtvNUu2EqzsJGv+iyVx9yd9dw6VjNALuh//NuFaO+/M+vql81MEF+Sf1YY5WuDXoFpZf3mQPdbz2ZDN0Fcfum4aWbkA9C4uRcnCaLc/sk0VBdjUM0R0AtpKpuNdvvcqnaZ0DR0t3azEqy6q0Eq6Fn81maSH78aiUHMOHza2R2HOD8Pd4Pa9UgG46t2UWO2YHKmWWbxqDGe87oXkVC3ndveJ0ko0R1f/FL5XPZ7V9cQq7NtJpjN9t56cWXlkMQ/EwlopVPytlBdgOm3EknkFiAgnXhcp42Grd8GFg2uRgjnaMqpjOaQj8oSOcytY69M4LRAWJxXyeJgvxgBSEsqnVLJWmHD5wgN9vTv6a8gEWlO4+ZP/CCF79/mVnmdL4zo/2tEpX5Ww3MCm3pEdlaQg3ki7M2iaFRyPmlheZ1kiWBGu4n6xF55sMqfwfV0LmchJsbxse0D4++FsLNGIEojvkxJcsgwnTF2z+BeZfLA2fOxGTenLZnCS/t4Zrtbw8uwJdNNAtL6PpctVK4TBBIJTCzzGjF7fJSIbcIiCmxZw68jDhkd3oWx7bW94+u/gamZYnArXFKmj0UHMBsvFloS56ev64i4IdsZo0rPzl3giMiM0zxhdkH4Dmozma3qK90RwMz/HMxr68co30A4VC4Y0W8GdKHciPechOqbyVvYKA9zbhCApfGBtRrdtwcR4BYXHM6TlFakoqv3VE6LKiJODI5m8UTzTi9h3HDeSYcl+F4ZUz7MU889A+KLS/hZB9kqXV4dUZ7ZhR+p97yWpU1X9oYO9C8vnNLGdg9jIkywoSMTSKgeTIxBKTPMxCPHpM2RUL+tGNJ7Lczu6K6iD3wIGrKaY2spokA1Q662FJkkO6gwJohGyoB3MnOGdb0uikspAUwIH7NJjhRt4pxaK08luqW/58KOwuaTGA802ukz5+TvzRWa9hyAO/exRT9O3a/XbJEF7W1zFFoHlUrRsnbINA4AaU8/G6bOYt7tuIhZBTCfPAJuJKMLCLsgI3uKEhWVXwtuGNHEb5MPNssof0qdeiPQ29/qq4b1gDLrZeX5HBUy/Ahe99lf44Llr0dQZsi4r9YkKtqC148KeVkE68pzHH7q9OugJ8ckhcku9RMY3QmyekoNFm/HyZ0G71YPI17DqggVzN+L5dR+m8mddiPvfRDj9FHj2OnrkvL/NtpW3eGWaxOKmkM95mN8QwYqw1yDpVRFX50Uswmfviw3jVskQGemgZDLksG9078lTfSjHR0/qrkQN1NbOtnOnxwBxizE1FgSGDVrShGEg7lk93PZUXNlt7b1l6S/mTkoXBrVe+k3KV/oico95fp8ry1UGkyj5LjL+JmN/I1WC5N0DRqffZw+w3oDqMKMUwu+JVGEzf7zw5JUxcybNG4OP2H627vzRu96Ag+D9IO4Z4NXfbcH+eCghbb2ghfN6Z6sZQ2GutPLbw8GuAzKtelWi/xZmVKDVEPGLLSwrD2csu51l5pPU13OYOn3n6BLf3MA7e8hBtX+X4dBHTJHKFRgcl91FuHwEjrDhRtEjTQeatva9/YuJUlB0DzCCpSFINFdcMalhQsrG9SrvUQd9EnnlGb4OjCWlI1EzEwu5gGO/a3fMTMc8N+uDS3xQIpFOmseoc/6yVS4qFDaYgDcBNkw8IBA/l9kL825A7agzIfJRJbPGaCdbJY3UFJ2mGGWkJRSHhxV/gCIaanx/YKEtDzuNbVJzSES02+sLy9B4idsmeSM03/ZDGXHI20bOjz6cPMXkrhdDHpBeVAdZOz5jTuQ9sCV5DsTrlgqnEVAf7469BnnlKkIHUQ+/uaBqkeiVxcN6+fZpSdCZ9i3PO5ocViz73uO+k59dbu9LrlbSsBS9SbFfvWhzmrWrKUNdoU5+wn5d0WX4BeUeQWUNHvnOyqvpmsqOol0QENjdH01V6eGodyzBoS+3i0m/FYa6nOs74neFUe1opqxzHRoXSIWWDTf5cGuZXc1wT9eLD4lSIu9+J3tLf3S5tFg73k58A34STpTEvusMMSb+MMCjg2kPOaCPiuIXPJDGGQFjKftGrwq+YincIaHW7OaOdAQE0CcRXff+U3HgtOrXqci19IdrBPWo6ADcXP12BNxMS/lUnBe1a4w8ganK+OKm5ltdeFZELltu9fqBW0mG4Ookc4oH2H+lqQ3Ihr1lrA/CFiQYmX2b+BAxVJq9CtXKDVgsqCd/shDl9EgcRs7A8b4lzLbenBl+d3GP9yYntJvifAXzuAx91EHJk+0VgRn/wkmRrtDx19w51Bfa2M+jj0gtHe46cTStabuAy+gIhaL4SFd2NPZBz4NJ0ESU2oDV3vrRaZWiY5KwdQVA5RoKZcmpUxOF0C0hd0TE+4TCi4tFMYlgdTh2SsZXZvKfiKukTJEen3dCh2mVysunjIb+5c1lvewmh41ygyfKWPKPXiMgKrT3gQh4SdoL4qPPNR0c6R9VXYxqYUfOH001cU+aqeFMRANayKRonVZD92CTV/MiAhdZYznWTGn1XtL0Yu4IMlk6+WK05AqjWUkz1rLROj3NDsmGQytSOCiDsp2WrJ0wbDneR5u1k1ON1Ud2JgMVe7nwUYVpeyVmtxfvI+SB/ytf0ANBx7EsD52joSDI2Vmy2lsqqWtJ1/2U3JctNjD3s3dTrr4Uv574tQnMKfYEeQsVKjSCUEK7bVOML+bYhNZJE3T9+zosz6vyaDKhPPwxivI0KcDAvfjCqVPayHbzP+EzCxzIJyVdWvwR/Z3g9M8SpRaU6rZAKY4Nuls9SImQi5N+OBsKI+66y+/O7uk88XrCBJJW+3qTPdia7pFvx8RORlkEva30L7amQng8ArFXk0Yjd/b8rIEGJ+JvUERSF9hD5Tv094MQvRWVvgSaCOjxJHHJqZiRrFKw0X7mlglDeGApUrac7SAMpM/IhsHU/AVDSUWm6O86JUVbY2iNP4khy5xZ5f9Si3YKuRhpv10UTZiWw59nCaP2SkK9UhsCUoFZmWlAr/gKYZMUmngIiOGcuPFWnRLoyPAu1OxwN3+VH5cJuyHwmBpNQAjDdL2IJjRMVcL+soN2rh/P6OrLENwNXVgiFGVg8vM6o+b3eMnx1g2WQZIsAeCw9IfHaz39+zry5AO0Xj11mFP9MOEJW1DPtm5FL7YA9XkjMjzak/I0CrW1Hu75Mnm8RtUwWOq80k/vrTrPgRjzptcolk14a1BiT5MyNLlZK5N0Rind/gbDJP4YzGAC9DaMTJ11FiRDXnPpecPcEvDTFUlNLq/yRprl5ovcMcpmNs+xYti1VMe8snIIte2yGNHP4WDRHgNTcy9yB1trqJ/5iLQAUmzu4bUn9gh9YLyORd7NgbedTmEacVZ0MZb5neDegA7um4qJC0lC5dYqsK+x+9xAX9/peb5tW7n4yi44AbDGfND889kfhnvH9Ef8fiGHNt4t1gsXpiAepe2dwtMGwzAwT+eYQZ8jUJokk/s5KEA6mZbtYBCNbjK0YTIauF8gyEL+59DDawcYr0QvYytWwPWUp4yT7/8qVzaZTFJrlZzartsQMReleoA2RyPhagvTeeNXbVcYAbPjLBcNNPLBhxSG7qt13mrzsVKsWM9rYzc3ZVeegqfsvHyzhv+D9yDh9jkfMcbxUSOn9seQrRzfNF5tw0p7iblnw4eLydPGJQPiXQm3bh2oPhZ6d2a1CPHVmB2vjrY1gaL2orBjpgnWGxEClOtfmdqG0SCpvijU7ytzCrUrAt9/YKkaW/phtYmcsO7nWRsWf6h0aGW5MByQm+x/Z6AEziTGQqNAtNF0nrUgEd7px30r2LGL76pbtXV3ComhNLqhO3digp/43LuVT+M+lOD5znx//OQqzHzIgUZOURWZJfpm37V5EOceE7l8QodOOzT7cmnf5vonbZ43peqo2gVsuWxB0t263n+caF0A7bvON9lMlUCvjzV8AzQA0eymCzTFeGpF24K/uL5+LZ55dYvfzrN1Ve6TpTK2i+dAWIIxAFTmrrSbgH63gIr8SQ21kFquCS8tuVQ3HMt/KXu4AmXGviy0y+qu6KgaoqvGDe4NKAE/p6DtSZJZwY22m3Jja20AncwCdMgv5qLMY3GTocVu1wwb5lzqgK2JfLHgu/6pNum9tOwjYDFmNo1Il4I536vPwTKyq0iCQF7885XddK9slyd9h3HmPDsfrKOYGxbKlJ5SrZm4dwamNy5grFVhtBePMUQ2J9ErBkAsnQbZYa4gFSABO5VYE52y8qyHsOChljAmloG6urPaGymCYZvOtWhK9QWyeAbL65FDnZ0IL5hwXEhkwZ+vSHOYk6LBxpFFCyk57ZJvs54FkigThr3SI6P3zPF0j6K+s1rL7N1vEpAIUjrIu44uv9sFcDjGQ8OAqIDbXDwFawmlDWad24vGWOdRBZK7whgSkmTJYHm0R1eiPFOivNgmqFNKY3HvVTWe26OGTAKdfzu2reQaFnHVvsuWajN7UsbGt+8mTCQl1d53XxP33uNjliAUTpvZRJn839/2UO/MshnaF2xEMN/fiDmGfQjc7xbOT9EOrGiIcFJT11sZKVSR/bWsaPcUZdJehcGx/lIV7QYuhOdLMFD+SLikzKEugbdBXJdY6O9XcdoPVM2JzYC/4/77HjHkZiqhLK8TOXUfu6tx3JrRS82N3S3cc36gYt1E+oU2kANI31eaByvkgFyEBoE0PN+aOrMueQl7WUmtEW+S8kRUuKjIsuSJMmXpCCK9NYdFFg76wCimwsr/h2Tnr2Px8SxOuLGTBxqa35CY9QFyfqkEA+6ZZP0QwzPIQ/oW9RXl5vuzLRk/GVk6Npk2JliF7cDGMf7pKwNhf5mDrg2C323SkpUT/0yseO8irMixy1/I4wpL6vy92SlRzZ229CKCmY6C2q5BdA41hfAimDAwyOOKnRbo3C/vrlT18WsMfMZ2DWAUwBCHLKuja6/zgfQtcAHoGoeEZqRyNdstnsHOGQh2erH6JjjOmj15ZKSZObKCn1ONxshoim2iao/aK+KipvQK1v/oompckp7/0U6PrWgGvxyMXTHexrLB+WaVIDY4MLigHjCfaYx6n5xL/5VCMAnV9Ugaom9YpT5Vnv21kweIRPOwJDBnlZ+iOZrpAitKqp7Um8RB+99cHIViymx/n+CpDzKdAkTSP7R72xMJWykqTE6L5bZUCtmSvlAkPfGQwxcU3Ya4RvZqyD8tsMhZ0HUPrEKEBbU8/WNk7Mg79fxazS/hEtuBn/kJn6KtkAS/wAjrTQxbBl2JnSx4pWx+ZfEnVe9+qvEKgG7ZxnlalYtytwR1xhivvJUyODh3Kiia0y0hhVA4QrHXEVn5mZBRATonPx2ywtHoy1fhXQB6AcsHus7Slt5dquvBB0ruCulCKGXltBHmCncHs9P21z8KfLGxnQVsRmP9oycD7nbI091ej1EbpE1ERW+jXRQL1seYniGuLWziu/ey7f4gTUEjfcYnsGmwVXyl03KzGTjMwQv8DF39LtKSY8HGBfS7IyTe60XyeLgLDKcBp+USnb/rO8PYU5iGs9hHIvku0uvec+I5scbgbEUYYIOkcswWl6nqYzQipuZFpiuQ9H287AFIcNl8jXCtYo+HzfY/JHyUbOluWjN+7LuLs3szojD7QjC9vEk6Jw4iHJOcabjqbZgZ5wgahwkt3DY/DjFT6bl2KC0e9XXDemL4ruPYNDzO+fZpnvV3Zm7LBDXH20V6OLf4ht/NFxMQPkppt+LOScml1xphzhPpw1lFdusKkkFf465yj8ezMe7iSt9/lznQ8vtV8fwNanQT4fS2XdMYuWBrLeNFyBB8Z4EKcAhQPJGESYdIUXfOFP/2BMA5PInGn5/8bTtNEjHPUFIpf8z37REbYqUyZeoOYTskHmYm4BIfxGDdGlN14pzfuaHeMtHghOM217vBkAfhCRJ78lYLvlvE63ERdOE126YpxklfRsAEA/IZxmxza8gA2GQMPjWydHx9QYj0zm92RwPUTBdKPqrKiQRgag+Tgvankd/tiAjh03bT1kCzQZCidFhUOSsORHDKkWTj3vxrym8hJwTB1/GGg/V/XoWj/gq8bI881eE6Po6bHlZ1v+LWEEedPMZdG99HJlY19RuMTcYW/teDse76nlxC1JUXsFqQplE3s31raNvl9nC7DndONSy5gsytzH2UdX4J3NR9UF2TyNl3yMBIYO9dzY9k6i2gXiPGp2AhSMq6FvoSM299BQmMIWbtPAR5KXgWiXwQ3RSBf+hMx591eVVxlSwu15nWO6r3DJkmkAYUpEJ/uTc+w4ZFiLRcY/QXgfNvXD9Iyr/fP1oC0GR6pKlrIUOyT0BTEgtOD2jAON/+du01fNolTVX4Su09x+zUzGojpQGrjCrt8v8cENSF64VJvoDlVJm/4kZN+E9Te1LPqkJJ6ulIstb5P5SDI7hp215MS9T35Xf29ifaKvvdenYkxrf1syJz/b0Uym/1iPAV3+0uLw4PFkPDZdPh+DMeUZJBju7WihUgztY4XNljk+o76bmNSA4C67fXx2OdjXTbMr9tDaEU2auSAhB/nLUnd9le+L7isEO5t+bAqpc2VMgwgSeLXG2a0ffC9ZZDV9YeTvWrfpE5xxTb9qhnoR0QujyS2cOq2EZlbkWTcBd6xG51lCHLyjTvLnXfwBskdLEabaHYI8HrY0P7kM1Ob4g7nb3A2A091I/SvMaVPM+LRf45DL6Dzxf3CwH+TY4Agwpwb9sp4lfuzXRMlDU1DsgU6oeLmLYa0V8v9Lhk0Zfo8xoL0FGCZqK09i8ODa8p6BNwKrJ+2yTZb5m/ywk1+pkwIpqF8UaiALpEJT/Rxf5j2sshODtR+k1mJupj16UIaOkw1RUNhlqBKwRI9iP8TAT4IcEdekcMeuH6e5Upb/35DYtu5kJx4Wuy4rpDQC1A4+wqU1sWnUkfSzk3MQwOG/Zou0tyckkIBrE59wgrfxtRX4+OIfcKC79YiQ/gvPTDuP2ftECb2gr8UjGFnWyJZ22EGZ8ADtDMo1GNzgjJY6JWCh/SAldwxRc4b2sHD86uHU8ZKxNcfNSR4aGbX0LFf6q37pQV6guntn5eBbN/exDegM2tWrrclGTRLgIT7tkEoQbaflREXGIacUl4QL5XPAltGWKGcO8sFuV3+pl+wBSRNAC17fxLXyZVrpQ2X2gBVN2rSSsuys8XA5qn1lj+pmFSanjbcgxJ1iI47rzgCJN5mi7so9HI72lScRi+z7cgywmk/UE9uBIhhWPqglzqbU8w1UOHIA/ZiUNdHUnMThqJ8zVA48LIThlSdoEAJLHZA4gd11FDvYkeR7ouoAGsQTdKvete11H2xDFuWFs00zXarh5v5zk1n8g15jxKYe9rj8bWlE40XenDwtJMD0nbUT1mWjch67tDlX08MuusUh3Q0wVfoWmgLtC8vtF1VdFj4qV2fo130lgVUoInqg+whHrp0siUaug7eINXQEWccRf9L3dWvBBXPVGth30MQed+v70hPkDg1WEemWvk5js4ffOhk4H0sMPFI16but6hhoZSPM0tGbeGgldLlwdakUN0SqJSUrEp0i6zb/cph9qx05EhV/T/IVo4urYMZJwAIW0FTaS/JonaXrgDM/9mTpKZGbTN9Xma7B5tzZnELSQOi95/D8f35xbhdy83vtKxvnTbreqzfMXxbeeAq2JmVyL76aI8fcLfuoAxTj18lH7rYbGDUMP087IthLS7VaoLL/0PT+IMW3SSjF93vsx1PFfYHQz5nIRgfJWIF29ueN6VXuQa3xNKmP5OPWcn+QZVt64oWT30cLOJfzrO8cKqEKOVpgXFcRA82fzMD8uWCr+II3n2f/urn2gqswQv4UiD2OunmY2cJEtgBtwnPM+jxHniLgNEKm3VGOozpCuLd6P6hautNDcvGd/xvwJoowUlq8d+fd1Je71nRaQ1LX0yHxjFo2NFJV4mXW9tzhSq8FlfaiHqcRQENYn4eYFKIP3ETD2xTc0dQtjF0Xy+aORzU3UiYHVNMegeD/ydQtTfgLO7YegWyiqLyGPvU/Ik0S7mpMXAnfyzZ9yEvWdg0+6UH1k9N0dDD/z2BqkN2pK4iE5hU/K6G8+S4RIc3OfovYDhmoKp8gQNbrzOHtsYJPENsADBWViab/2wAnIzsPM9Afl+ma4Vj5rfpa8Ns/csjdmiWu6TfJVD8qV1dbigSG9qT002WgiR07LfBVFGo+mqw+Jg7tjMnIKrzz7g7khutt4uNBY9FmOhfwj6yot9uq2ic5ypMktw14SfBJC5h7ET7SEzCQrBn1zurBsybZQ7RnCHvvWs4mbpmjwTLC9fmxXULOg5q626TPJ/pZtuschbAVlAb1R0MFiolTkjz3IGcFgPlaPEsc8IeScA0mhSXwNzZX9Lqw1DZY66+rRQcHkBrnca/3DgpXsqtnR2KrPCPPKQ2RpqNGgtVSWrXl4OYjVmWi5pA+GfwEpIeCRNwKkEh6SxmD/M4w6CPuzYOpwnon3g2WFtB/I4csMNTEz+/u7clag5schzUiOBRLCnoVQ1NN8wwEN1W4WOKMBCXFgiy7XC8OpY5wizFgxkd3o9p4EAOe9nRbc7qm0OjycPLU0EXWmXwl7MR4A3woXvb2B7xJCafdsl3tOjs0PLJjcyAcJMvVP64M3/EPXQeDe4oho4/YG4O/JKtLVY9Lo7I0uDilf3WoqK9HL4dJHLKJswrhnqwT78jPUeu9cytaKtP3qos4wirwnQrxtMOdUPBVW9lvMbTmcKKkl2hHViH7Fe4HE+s25MSkyRLt3zsXGATwnu/sxfMjFU2+vi+MLlJKnwPDluZImf2RYkxGzzGnv9bu+vDmpZ8HUKg9Nh4IMrPPdi1C0dBoqFazj/pzvzvnW9j1ZqBOCpptNL7pkrOKQ3G26zQ3vAyZwWXFcP7drfaj2u+kJs5GVNOIAcxvZLafjTGNGiNUTCgdtdLWaBqjIMQIz48KzmURD77a3tsMDrsdk0D09I6z9Frnb/vXb1N0VR3egrddjqC/Gaeh1lbPLWv3Z9qOqNsZ1Bf6MaQ+w1ED2KftZXaPLj6FMLpphXuSgea0PVwC1ToE8+HbD6ptxLEcIP5fiCtbMeOj/Dp2LwsdgwdLUemMhPNfeGyS3/POi/9uVfHuh2gNktxkM1T2HQwjdF3UDHVliCF3VgwtShlEGIutxunHJ3hSdl8j9Y8BIN90DrJ+64KQsbbEY4bxYXvGIrlduQ9DiCj2xO/ZCoTuUoYFtJAfj19Tf3cI66FrzJ6rnEbtSez76IOr5Y8W5Ch1pBUnRZcsjQiAZlg0e3qpKRsTmDACgVRcfWWPXDeNa4NR2L2wQKzUziJ6mYt1ixJAMlSM92w57BzD4cpwOZc8LNdmWiJetErIsDQEratyCtzy+DrcDsTEBuJ3kgqbx/iuoluU2zftO0hpNh0CFqQaQBWBXtAOvq5yY65TS4Ut+9HMo1jJ7ejbxqeDd4OyaQ26eQmbcR518luF6Nt2Zj76GYCjUPaVqxsiTxipnLlAefst3PU8vFwIAV8OlZAbMbv+rmN0zPtEsAKMDTGOS+C1ZyBEorwmD24iYUsFRFdPzp6waQSQy4GnLmNM4nrF2a0RHCaihvKGbNQTD0s0eSU7FxHvkVWtdDN206GY47KjKmU6JHKbFMJSKIqMSg7D1irl6InXQPEgjJyvw1dxZHM2zVd9y3DsPbrvFNyC6ywjTmoUiUQ6RcZBUYw0o6dleTf0AgoM63jOM758zqKqkVxzolMy7QyJXAuGKbDTHhGzYW6ORpQslemkXuogGXKkiYTmIRFvNYuBg3SJS8A8TSQmI/xsTIoTLX244EPswHDXSwbhY+Fan5VyU/mICrqjMAsObtsaRRM6MCvy3Imw0KyuGHqzPtqz/G70CIkyvGgLLsH2jtg+EsTo65ZxbIZ70X1IaXMnI7RrYxc2WXjAxS2NyJJ+XasY79sZjbZYkYBvky+3ztBmSXiJDMsr7Gg9VqNZMc8OzpK3Dx3OOPK8AnvLMBLvDMH8AqSmc07zz0RO5li6BA+TTOIrR+gsz5HC8OUqqa7hMy1rpytXCrWZgQoWvbOZVDFbLBRo8PmI7dxq6xfqxFlzfAes8q87DwdgFtp3BMFqEYTZci9UfxylAw1AnjuhWDTnuAnN1xBuA57gf0YpOo6LWl4F4DZqGG308UY7Zf04TulUhRI0ojanzvuD4sP6HNgSLF0tIRJarTbYWCPMTDlH4oBr/RQXLZHczaVti5P1/rUy0QQJR3yNUmzQ3P9WX3Dv88mg+uAag7Ni4MNunwE/UwMpKBmHQ7AvAbfZIRJpM9Av25/V45klYGY2Z2vyM/GXpb3p7gmaSyuKuSppHrabE4qVj9VmoUUQMTE3UXvF50eNGrUMqwvZAV9XTlXtkReGqFfocgD+h2oDG8o+F/zG7fkIv5ChgWt8SGlWB+B0ya49aGIj1dxl7wm9DRQP9BJFzlZeCBGHrQpH8L2XVBvo1jfzAye3YEu/azd76jow9+5vZ/Ed/MZBBkTk8ywJ1jOOBZqpMtB+NNhWpU5DVoz5/jH2WD3aUtVGwepiuBNNTCKG2KXZ5/2c6XFrbB0tqnRmtWyev3vJfPhzmvmcSF7nqjUiBJ7Ns405QNL69fylBi4LYwYtQXsv73lgjZBsQkRUVHrH1t7qlANFAXtqnLY6wizqPIxbW4yxtJSFsJ0RHMesSrUaQgaN8XCjZh6WUt2SEfOaSGQ3CIIlO2mH5HUNFsmT822oCCkav9xOhZzrY7ejKsl+pJ2gHKf6XkEwTtpTL7+dp9OfCMriB76AWnWYUptHPUz2eXngb6VUlXKXtz8W7ftA/dP0OXdiv31ngaSH4BtciiqCpNXuji7ljmHTCoGYrmn+Wy/tjj4hMVj+UWIQZDunJmZ4ZeY5xvA+4kFid7+leoRI6++vCAInWDkqMJiHNRxvTxop5TY8YWbljyLojyJEg/14JjiaNaZi3MwYeHF8JuPugwi5WpHPSbh1DVevHo3zJN0g5zLLTWBBIMb2Qyd4Sn/9NTLdw9bhVxjXxrd9oElO08C/ujIAjycA6U7GN/aalgDw0A9Qs9Kt2J+fopU44v4493luF1q9lUsA+1kw+Uh2s3onrKrOdR/CKKNCAA44BQNIGvBV9bupVhBVbyl60T7yuzWiwvWUixsBcckOLhcy6/sHLKaz1i+Bg1TwbD9IGMK+XDGgAyJKaZhxru5Gac6Mpwls39PtTyofQD5dJI/Af7Y325jQngkETR3YcpRZzR54IIVi5YfPacwsGPuBsPCgbOZCUvp8peZ+qNLeyzpaCpyChLfSiGzKypjellEqdY+2fkr5/Qvshsm39tbG7yGwC/jfzEhcq+/hIm4zL3DdX8NXJIG/fAZ5IT2XmIq4fYle9NuEfWc7p5BC5n9syfe6WmH0npH24zx6IDyAJ2aw7tFo7TV7WnlCbzulPmneH+a9jIenHRLh8GAJCieNlz4tqPcdujwbX+w8AB2z1K9MllaQHeN8b7ChjL4WKMZ+vp6cKWfFjG2eua9dyg/8K5YTkr+B22RB+P0bg50c7w+Hxz5IJIiL9FxDFG+pYt+IRLhL1jMcjLyjAj9cD51I6rULrbXiQkIpZeW2+JgkDcXR0JfUIrDSSdygSMvwOc3qejtqmey5yREuglHM9IdTVRAXGnhhbK9xf4lrRuvVmhjM+z7AWQ8D5Axm89g/nSkFJwmQQvblyBmQg5huoAjyRd5MPgmK2mRDPe6opx0Tor1LqtZ3rPUsDmrmdb/sXUab9qeKCThcQMEEJx9PpTYFCCEo2oIRsXiIAsSRyI7idCNHJwFnKeCEpw1B4NNnsI0ih9JrHZGwie/SMVkfrwZl276vc5z4xczd3ir/B8xW2QcH8nT5fFYPQhQNE03tIBYCXd3iPqAisxENHGfVMVibHvJliUQ6La43rZjMVZEg7FilFyY4rDpeayJBrkrp3cGB4n/gwm/rUfewtDRVUcnOINVHv0o3E1xmOtXdfDla8uOmzHS4MG5tpdNVmUx00x4R+IrM7FTi3FGD8ukaKpOC+57KXtsJvmIpY0VFWmP/hc4BTBMrqJIH4xXpZo0HgSypongNBKBMRKA7Q1MgoGaKZG2nMi4aoW0IcJdZcwQgXUsob3NW9UiQwFh4LxzW84kfjf33XqsqtHRC0S3hEBoY4q7b2UZhP5XHNgk4QtKXa5ug3xXBd6ILvnDav6YPbSV1813MhrvAasIdAP7YUIwbA5rm4qcxii7cCAUP29U4E5LLPQ4OE9N1lkzVeJ/Zt3BJPkJm/OXLywXVUUbUGKydupYqx2scNsZ/+t55V4vFgyLIpawCZ6pbDyQeIdaLcHSIjv9kXl9ze5MznvKTl0ggViyV2+FzKPv/9bTmA5v6ln8u+dd2ReEASSOyO+/hRNnlT1zIA9MYVPrfsEAJY2o3P58IwMNM36+XFJ+b9EWRyDi3wOXhugWt2RiJQL8lQVHzn/hd/7+r0zHYyk3EV1KCY59AqSWjnP3NLQKipE/8El+4nqc4XIACXBs/pWUWwxEJpC7AeRMSSmRIjZmAcdOzqsFASzhgj0tDTKL6ANrBZxVJ4fpK1ONbRvnOpyifmMtDNTpNM/mf+yS3mATLLUYAIXi0Ek6CV8amtduPXdYcMidLWGRparECN2wsADz1Rp+KotHcs8UazFNufrCfRiNBFdlN1D947xM0pLMMXCA8zNmEFGOxKiCEjoFhnVLlZGFoOIH4mrIYo0Kq1r9P6tmSrsKZtYW++ljc/tOTyGIW6EdJcAupo4/SNbVCJfIc7rSC4wfmqCmspcCWLRW3bR35WlMdR3jbWxUhYGe4w+Xj29S5o4JFJ3ugrC4FpO3mmgfezRbonvMv5POFpgfhPiNqHApvjlUsbns538yWw69XRrleR1bvZLmAoRNKT82P5L2Oi5hRF3ktr4AbiOq4qsnkd0ilgHhPN+KTNr/41e0KBX1PiRspABaX8EmLqiFSgWuE5hPFd0jw4fmLMK1Wng4+9hLgvx/8i4ptCXYoC5tPx4fxTxDrg2grUW9Jyc2o6hXQX4eY1XnzTRGT6wqg5vcDjANXPq6WkQNmtRI5f5MNTEUSAdLsjZYnjmwFRKjGX3RnKiFD0lTd2t9HgdImivupqfxibx5M2/cbUStznqhSnfa815jzwQLZ8wFZgIep672CD30Hx6xKJ+ToTU55OagYHs9uGIns26fG8sowgZU9OD0VjvOnuzV9YpvqJTuRLJ6ia/ojkeSN5RfEprQMMtmKrGDh7V/8DbuYbkcfxETHLa8d8Owp9YYud61oZK4UGDupjZg9uIDYYgS+VmjQtIxJiFdfnNJX2JstHoVGhl2hzOm10L8n2ivG3ImJX1B8dYGeZWXJbTW7UzeyH8c5BapS++59N27mC95nt8FEWJ7yvbY4/WRFWG9Dm7Go4IHxg36noBB/olkf/2k24f9o0WdjoflOOiPLS/5HEc0+NBNBZqWPZHc7yG5TjAd0k6dEKl+IOP9O72gEyGF3y193aA8xvF6wQrmp3dfvMtAYg7tVq7Y2Zcm1OC4s3OXW7bJNZ+U4ScPyAI4bgqSFaTALUKqO7mYzjEQpmr44FSt6B8Rf01r1IdCtjraFGoqbNrIu2D0vI4UIFZVSMPww6+Wbt17s4uJI71W+LxLRt24wDt4+0K6U0X5vHq9KwBKOSi24mbmHhAWKOdHhr5TK2HaO3KNmpdZ7eYJCRibF3GafyGqgvN6Qg0MhlBokFm4YgdafStf53TbFRHQnhHtWu72TSHcSgoKtbrOWra43bUuYfG4NWFe1uWpW6XHZLXA80utLZDLH/yGRjAU0mdT3VDA7RgTYW4PjxoihT5433GE3uzjfAhiPMZj1h2LvDymsGZjyRxXYYCG0jaPLgZsgMe0hyY+5lbMtv4YcFQjq33QWTTqRUBAV5IXDaQTNzax8hNdPUrLSy9wtUjkSqCFxZZP9uXFhZpMPZciNTqTZjSlvF/S/KkisDf1TySJi63/Rkyas8H67oZ1sEuvnKStLrN84aLzwOtqinE3Ez3fye6hYytKG59Pybm5B90RP5d4PvUm1OInkEo3QuRJyT8NP/fs/WbA4diC6pW7Tk18zamJdyYMRE3M2c/vjaij4P/mO1/qWBtcXhkPYPWi8QXGmNAZn7JBUR87mkDK1aFZB6G61e6+0rrQJHNMWYBWJ7nSIGHpoTqTDABNqC0p5O1/p3LXLxfhWk0OusMHnR/R8xlS1TzoyPebjqQVMeq5C4ZINFzoqUaxkP7TKzPMEFDtlcXzpHVti/tBjxJoGpnqqiVdEuwnT22c26a9nYHsNc5q/L+eYskr8xKzFTpjMQ16eBoG6LjMn/QVFmuScQszyRWcvqqG7Id52PpAR7TvZxI/I668AAzCOxZtmdwwtP458X161oo6CCiL6W+yaDrulzqtgQdM6W5XnGXle5+JPYNNGnAPbD5Lw/MdJGuCTbGKkaVyzztKl7X4uCQvVLju/mvtRc6ts/7IkO+khiQxzmdA9rFUYv77SjrJoP95D1+tUgQWabEVtxJZ0jc2a0geHlP2KytcGMuZMqgt4C24lbP7lm2UOP02B9i/1deAFdQIasQBDisCcxJ9mXdIE6jtSVOb521ZsDrteGi+T85I+Q2c/k3WXQLlnyU2sXUrRnpnvsMWLVccYxbup6nmlzuaV1LWWsfdpHdGNiFiFLvY/bkoudvT3X/hDicEOK8+OSvMO3lCY1exORXeQLSObxTUud5jgTnEyvZXlzJTqnhJaRRLGVehzwgmRfKwlLYxHWa4otKYaiw9LqTHxQruzhYC9V+Ffm6Y+IG6ljUKuVTbOs+PNyOIAVCHmexVzmf1OnZ/s7qfuZyajOTfeh0Qt8ZZRUNQD+fhWq0tgjK30VZwU1qQTdlNvd6k+rYb/3q82FA1YhD9ggkkxSdQMP9UwwIyMCWWIb3wNcxHzZY1jcaY+9o2xHiEU0nwFeFhFLlBF2f2IBka9LTgvTsvNhg3gRqvQCFewbxEtqnuEdo9Zj9L9pUcC01j3kWKYd2R05uMF8fgleXjlcf+trwAaX7yLTvSAyrdl95H3YE/UVrZVGvY3kwBsOvJ1RKJuQhAz+6YyKJfXr7VFjwvocK0X8gyQRx9zakWP2BrPBCJPm4/rNKLTzukmUVrtLNGpMmvOvJKamS8M7R6YOQltY3ZKja1+nE5Q3Cet2aqjYjJNIIPrc5bknHZQXKFnvwQw6dOO8OjkmtJJrlmnCukDkCZMxNZ7kq/vpxWKHjSKW6T2PrPElAKos0yyUPn/stDsObeLasVMr/d3sd2urrcNqcEUG3iEW54T/Nzzk+tTfPBR8UB1ter1YzIAAa1gP/dWZlWFGpl3UyMUQA+JBiA07DxZcL86CMleIT7Z9TwUPGjPFRrGbb3vYrY10GIhoV3AFAHtJ9UAicxoE6XNPZQ=
        - #2:
          - type: tool-call
          - toolCallId: WlwJvXsh3Bjd09RI
          - toolName: set-relationship
          - input:
            - Public: 50
            - Rationale: The Inca are our strongest ally, sharing a defensive pact and friendship. We want to secure this alliance to protect our borders and cooperate against mutual enemies like India and Russia.
            - Private: 50
            - TargetID: 3
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: OgfByt5FoRikuCnS
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Private: 40
            - Rationale: Venice is a close neighbor, trade partner, and friend. We want to maintain strong relations to secure trade routes and diplomatic support.
            - Public: 40
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 0extd8ZgpTyr7khz
          - toolName: set-policy
          - input:
            - Policy: Free Thought
            - Rationale: We are pursuing a Spaceship (Science) victory. Free Thought will increase our Great Scientist generation by 33% and boost their instant yields by 25%, helping us race through the late-game tech tree.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: TSFGqFjOgDdPG9V2
          - toolName: set-research
          - input:
            - Rationale: While we are pursuing a Spaceship victory, India's imminent cultural victory requires us to prosecute our war aggressively. Combined Arms unlocks Tanks and leads to Radar (for advanced aircraft), which are essential for conquering Indian cities and securing our borders.
            - Technology: Combined Arms
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: Wkj1mCfmOC6nUJI4
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Flavors:
              - Mobilization: 90
              - Offense: 80
              - Defense: 50
              - Production: 95
              - Gold: 80
              - Science: 95
              - Spaceship: 90
            - Rationale: We maintain our Spaceship grand strategy for the long term, but significantly boost our Offense and Mobilization flavors to ensure we produce the military forces necessary to defeat India and capture Delhi before they can win.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: lnOYEnvWl2oF6Rj8
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
          - toolCallId: WlwJvXsh3Bjd09RI
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: OgfByt5FoRikuCnS
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 0extd8ZgpTyr7khz
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: TSFGqFjOgDdPG9V2
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: Wkj1mCfmOC6nUJI4
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.