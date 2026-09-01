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
      - toolName: set-persona
      - args:
        - Boldness: 10
        - Rationale: We need to aggressively prosecute the war against India to prevent them from achieving a Cultural Victory, as they have already influenced all other major civilizations. We must capture or cripple their cities and refuse easy peace.
        - Meanness: 8
        - WarBias: 10
    - #1:
      - toolName: set-relationship
      - args:
        - TargetID: 6
        - Rationale: Germany is a fellow Autocracy nation whose peace treaty with us expires in 2 turns. We want to improve our relations to prevent a conflict on our borders while we deal with India.
        - Private: 30
        - Public: 30
    - #2:
      - toolName: set-relationship
      - args:
        - Private: 40
        - Rationale: The Inca is our key friend and defensive pact ally. We must maintain positive relationships to preserve our mutual defense agreements and trade.
        - TargetID: 3
        - Public: 40
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 30
        - TargetID: 5
        - Rationale: Venice is our friend, trade partner, and a helpful partner in the World Congress. Strengthening relations will secure their diplomatic support.
        - Private: 30
    - #4:
      - toolName: set-research
      - args:
        - Rationale: Researching Satellites unlocks the Apollo Program, which is a mandatory prerequisite for constructing the Spaceship and winning a Science Victory.
        - Technology: Satellites
    - #5:
      - toolName: set-policy
      - args:
        - Policy: Free Thought
        - Rationale: Adopting Free Thought will boost our Great Scientist generation speed and instant yields, significantly accelerating our progress towards the Spaceship Victory.
    - #6:
      - toolName: set-flavors
      - args:
        - Flavors:
          - MilitaryTraining: 85
          - Mobilization: 100
          - Gold: 80
          - Offense: 90
          - Happiness: 85
          - Spaceship: 95
          - Defense: 65
          - Production: 95
          - GreatPeople: 75
          - Science: 95
          - Espionage: 85
      - rationale: We must prioritize military offense and mobilization to crush India before they achieve a cultural victory, while maintaining our high-level focus on Science and production to advance our Spaceship victory path.
  - tokens:
    - inputTokens: 25682
    - reasoningTokens: 5688
    - outputTokens: 397
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Researching Electronics Progress**
            
            My focus is on accelerating our Electronics research. It's currently projected to conclude within two turns, a crucial step towards our ultimate Spaceship victory.
            
            **Selecting Next Research**
            
            I've been reviewing our research options. Electronics is nearing completion in two turns, which is promising. I'm now considering what technology or policy to prioritize next to maintain our momentum towards a Spaceship victory.
            
            **Analyzing Opponent Strategy**
            
            I'm re-evaluating my strategic direction. My previous focus on Electronics is nearing completion, but I've just discovered India is close to a cultural victory. I must now pivot to counter this threat and secure our own Spaceship victory, considering how to disrupt their influence.
            
            **Defending Against Victory**
            
            I'm immediately shifting focus. India is dangerously close to a cultural victory; I must find a way to disrupt them. Thankfully, we are at war and our military strength significantly outweighs theirs, so I can perhaps push them back and secure our own Spaceship win before they achieve theirs.
            
            **Adapting Strategy Now**
            
            I'm reassessing our approach. While Electronics research is almost complete and our military is robust, India's cultural victory threat requires immediate attention. I'm weighing whether to pivot our focus or leverage our offensive strengths to counter them and still secure our Spaceship victory.
            
            **Choosing Future Research**
            
            I am evaluating our next research path. Satellites remain a strong contender due to the Apollo Program unlock, furthering our Science victory. Alternatively, Combined Arms offers military advantages while Alternative Energy boosts production, potentially aiding our defense against India. I'm also considering policy adoption.
            
            **Prioritizing Science Advancement**
            
            I'm weighing immediate science boosts. "Free Thought" offers excellent immediate yields from Great Scientists and faster generation, ideal for our science victory push. "Rights of Man" is also attractive with its golden age science bonus, but the direct science benefits of "Free Thought" seem more impactful now. My next policy choice is "Free Thought".
            
            **Revising Ideology Strategy**
            
            I've just noticed Germany has denounced us despite sharing the Autocracy Ideology. Their jealousy of our technology and competition for city-states are clearly factors. This diplomatic situation requires careful consideration alongside my current science focus.
            
            **Evaluating Diplomatic Impact**
            
            Our shared Autocracy ideology with Germany hasn't prevented them from denouncing us. Their jealousy of our technological advancements and competition for city-states are significant diplomatic hurdles that I need to address. This adds another layer to my strategic planning.
            
            **Addressing Ideological Friction**
            
            Despite sharing the Autocracy ideology, Germany has denounced us. Their envy of our technological progress and competition over city-states are the clear drivers behind this animosity. I need to factor this into my overall strategy.
            
            **Navigating Inter-Civ Relations**
            
            It's surprising that Germany, also an Autocracy, has denounced us. Their apparent jealousy of our technology and competition for city-states are the key issues. I need to reassess our diplomatic stance.
            
            **Analyzing Ideological Conflicts**
            
            My focus has shifted to understanding our strained relationship with Germany. Despite both adhering to Autocracy, their denunciation, fueled by technological envy and city-state rivalry, presents a new challenge to our strategic goals.
            
            **Strengthening Inca Alliance**
            
            I'm focusing on solidifying our alliance with the Inca. They are our strongest friend and defensive pact partner, and I want to further improve our relationship to 60 public and 50 private to ensure their support during any potential conflicts, especially concerning Russia or India.
            
            **Securing Spaceship Victory**
            
            I'm shifting my immediate focus. While our Electronics research is nearly complete and our military is strong, India is dangerously close to a cultural victory. I need to assess how to counter this threat and ensure our Spaceship victory.
            
            **Opposing Cultural Threat**
            
            I must act to prevent the Inca's proposed "Endowment for the Arts" from passing, as it directly harms our Great Scientist generation and thus our Spaceship victory. I will oppose it.
            
            **Revising Ideological Alignment**
            
            I'm analyzing the broader ideological landscape. It appears most civilizations have adopted Freedom or Order, leaving Germany and myself as the sole adherents to Autocracy. This suggests an opportunity to mend our relationship with Germany, potentially fostering an alliance against our more hostile neighbors like Russia and India.
            
            **Improving Diplomatic Ties**
            
            I am focusing on strengthening my relationships with key allies. I've adjusted modifiers for the Inca and Venice to maintain our friendships, ensuring their support. I'm also working to reduce hostility from another civ. My game flavors are highly optimized for a science victory with strong military.
            
            **Pursuing Aggressive War**
            
            I'm now prioritizing an aggressive stance against India. Given their proximity to a cultural victory, I must increase my `WarBias` and `Boldness` to 10, along with `Meanness` to 8, to aggressively pursue their cities and secure our Spaceship victory.
            
            **Aggressing Against India**
            
            My current focus is on a direct military confrontation with India. To ensure our Spaceship victory and prevent their cultural win, I'm significantly increasing my `WarBias`, `Boldness`, and `Meanness` to aggressively target their cities and secure our win.
            
            **Improving Inter-Civ Relations**
            
            I am actively managing our diplomatic standing. I'm enhancing relations with Germany, our fellow Autocracy, to preempt a two-front war as our treaty expires. Concurrently, I'm fortifying our alliance with the Inca, our strongest partner, to guarantee their steadfast support.
            
            **Adjusting Diplomatic Strategy**
            
            I'm refining our diplomatic approach. I'm strengthening ties with Germany, our fellow Autocracy, to prevent a two-front war as our treaty ends. Simultaneously, I'm reinforcing our alliance with the Inca, our strongest partner, to ensure their unwavering support.
            
            **Prioritizing Offensive Mobilization**
            
            I'm enacting immediate measures to counter India's cultural threat. I'll be setting "Free Thought" as my next policy and then calling `set-flavors` to prioritize Offense and Mobilization at 90 and 100 respectively, while keeping Science and Spaceship flavors high.
            
            **Prioritizing Offensive Mobilization**
            
            I'm enacting immediate measures to counter India's cultural threat. I'll be setting "Free Thought" as my next policy and then calling `set-flavors` to prioritize Offense and Mobilization at 90 and 100 respectively, while keeping Science and Spaceship flavors high.
            
            **Increasing Aggression Levels**
            
            I'm adjusting my internal parameters to reflect an aggressive stance. My `Meanness` is now set to 8 to ensure we prosecute the war against India effectively and reject premature peace, aiming to conquer their cities and halt their cultural victory.
            
            **Reviewing Diplomacy and Policies**
            
            I'm currently assessing our diplomatic landscape, particularly with Greece, Russia, and India, to ensure our strategic objectives remain on track. I'm also re-evaluating policy choices like "Free Thought" and technologies like "Satellites" to confirm they align with our path to victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: Pcl5t6cS5C3MvdC0
          - toolName: set-persona
          - input:
            - Boldness: 10
            - Rationale: We need to aggressively prosecute the war against India to prevent them from achieving a Cultural Victory, as they have already influenced all other major civilizations. We must capture or cripple their cities and refuse easy peace.
            - Meanness: 8
            - WarBias: 10
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: PzISuoqyrcCEdOqM
          - toolName: set-relationship
          - input:
            - TargetID: 6
            - Rationale: Germany is a fellow Autocracy nation whose peace treaty with us expires in 2 turns. We want to improve our relations to prevent a conflict on our borders while we deal with India.
            - Private: 30
            - Public: 30
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: NDdsgatgZiZvABb0
          - toolName: set-relationship
          - input:
            - Private: 40
            - Rationale: The Inca is our key friend and defensive pact ally. We must maintain positive relationships to preserve our mutual defense agreements and trade.
            - TargetID: 3
            - Public: 40
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: yFFeCBQoBuuMmzc6
          - toolName: set-relationship
          - input:
            - Public: 30
            - TargetID: 5
            - Rationale: Venice is our friend, trade partner, and a helpful partner in the World Congress. Strengthening relations will secure their diplomatic support.
            - Private: 30
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: kkn6eogNDlvxzanG
          - toolName: set-research
          - input:
            - Rationale: Researching Satellites unlocks the Apollo Program, which is a mandatory prerequisite for constructing the Spaceship and winning a Science Victory.
            - Technology: Satellites
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: Ja1Df87zvnUqFM7i
          - toolName: set-policy
          - input:
            - Policy: Free Thought
            - Rationale: Adopting Free Thought will boost our Great Scientist generation speed and instant yields, significantly accelerating our progress towards the Spaceship Victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: ijNXLZnpkALSarID
          - toolName: set-flavors
          - input:
            - Flavors:
              - MilitaryTraining: 85
              - Mobilization: 100
              - Gold: 80
              - Offense: 90
              - Happiness: 85
              - Spaceship: 95
              - Defense: 65
              - Production: 95
              - GreatPeople: 75
              - Science: 95
              - Espionage: 85
            - Rationale: We must prioritize military offense and mobilization to crush India before they achieve a cultural victory, while maintaining our high-level focus on Science and production to advance our Spaceship victory path.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: Pcl5t6cS5C3MvdC0
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a18cBI5JdS3pNtx5UA3J2jTOu8kLjvpTNX4n+t6cw7DeiXiBdxkcEdYHgjQAJfTcPv7M7ZRzxKru2JEUPCdPjKr1+vFf3vF3EbFrRC3rzb5DBo67IlMxV3PzCQWVpBeOZLUsoH7k5B+Upj0e9D/WbEMw4qkVjnGudO+SbTs6p8eHzCn8lOlW8yQAuAgrJ0YjBh6P3aoAvwyQkTluvrclXV7c8h59Wk/74M+rB+U2mlVE8oaKYFXiAQOoHPdtPz3nuUXDoKXfslcpZqzoO+eiP0m/i5Gvh3RJKhkiDsUGwcFQEc8fWSwht12XHeeYZVChj0gFvaixi4AlCsHdXGuwRjJcCp155W4Zgbe2F9EYzA8cZQjX7A+hZt3v76nCV8a3vHhz6oEFp5TC+pT570W+F60NCiS5EtCbrwii7bD0bCTPFG2DTQ1RVsZAaG69WOm53loXvyyCpmswhLssGAulGUxngEmfmHH2wkiXCAqe1OG1jAg0MOpS84XiIHoDUB5cwOgsm15RynCj0ba377VFOwy8VGvBb4a5+CQaEYCDWuFfi89V7xe0svkefbYee2pMpbUoaV1f057P/lRLv8pkXo9k4aOP4NnpDfDA4GyeETrooPosLNiB1QQr5JlYi6o7OtoSu90t1sKiLaC+ouCxNwrm5bZeN3qwbDRYF77wB31ZdvrkGZ8chNr9p6nbwpjAW+eK8fI/kd0ADl494bLQcDSHVnt+y1Tv9/lXmGL7bW0LSULv78xI6QPdJyVMyRs1yIORPa2RCHf4sWQRmJyiWQ9kU3m47Z7u9LGzgzJA3F7EOwGbBjSKidyV8+rWIyuwG++E9JIZ9Ty4VH3h/97O+ID3AQXnwGqecuQAFEWpuM7hvjoF/Frd1R0jhGLhR5xGWtHb8CkXS0heVVHRWwGtUG8fHHac52l1P5M/t93Ry5j5jfRIk96nheb8QtxVlPsG0zD9XsqCrHvOGKnruoLXbpz65sZHOc8qDK9UeYpBNi1jfdxm+ulUjNruKYS0ctdy53NJ+Ywv1A2cAswXjL2jEtwRqF6v/4zDjFLOPUz4lNhnDVLOytOZiTWceoOp2pU7OKNYzVgvUVlq2q+AB5VHw+adNtUFNhBszi654MryreYOjXLHv7OBFM9oxC+nyMty3ShdYpLH9fnsLQCzxDWMmkDhkpmL8l/v4YcpynODcsJ8Vq9udOdy9rt3aCai9qipC1vGgmRHWWG+YwrQY2gK54QohG8V2zsEfyu2UgCmS99ytpIYRVjctN7VgeJ2xSRUw2Fdx4AObZCVo5YLNKg7p11v7sCxclXqHavTwlHwpM/P05NRzewo5EnuQcKi/ldqki62mU0PzW3DddsKOnKNuicBxxO5zYzuzgTST+tW2DZcyeNvntv+EvoMGXKgqzl9SirR2YnVjCwTjqkXOtMoXR38P7xjUo9CuN1sn6FAsYlnLbChrORdW41SgVhMT/MyyOU7DhtJb61HWkBtphwaU4a8rtqpHq1/0HYq5Kl/K+FyeFbBEH4jAQ/v5NMG4R4aQxeUxpAX429RtPruKnlTExSR4K5Vm6jNy9vIo+RJtrgVEdCQ7nQZOxwSiXX1EMFNNSRCRyjbMMqAqxku1saEA0eKIXjWXxqI9NnbblS6l7dnsaIkgxfmmbuEVYqqLB17Aha+VNPUJC85hEUeoXd82Sx4R9lMuJQoKCc1HGiyVjp6X1FrSBtBMNn4o3cPdx3FkLV2mw5nCklwUx3wQ6taeobvOfJkxoLfSCjC75HN89RUvAdkWM3wJyqZQyzFpe5VZOfXY/z6kPxD60v0EhvyeFWhjcWflh0AfVD0vsAdbj+qzWZatx5LuR2ykYe0/pL7FkSIdsBxGX1+EqgkYAOXvBGRKuDMuyfQEnMWcOH/O5GBno9NuE9lWZegCd3SbHu067wmYPVA8da+xQowaU6srLXYWlV78vNHZqOyhJMPHhLZpvpCcD9anIpft5cO5QXfietY/y4bdO9TJO21gCr4BKTQQEyLof4CuGXFIm2Ur8BprLLMXOd3OAQAqoX5rLzHdpOqFneSkVUTjQQ8TBfyevKuoUL9F3Fe4gxZQVKyoSgDVuwI5raVpmu+rXw00Mo3gIUP6/LMpxwnN3AdSbTBUne0feop1ZUV9OdYHzDEgAC1oQ4k4rYj1J8z1IwVMAR7Tq/fhg6uLHwfCQM5anbyMxEdwfbnVvplcog6e8jaxpqR9DKq8s5Snd1wjuAiXoT4i0gjztgKGqe1WLEi3/abTEOjLbfR9lXMYtcxhe4tYSZSUcgVIHTmaOYBwisIbXTWgdZYwAkDVhe7U0vbqUkxfhcwfdccNYNTmTacAQexfheVRJCNmuatqzHuWulvSnfiARBlQ1R1WDMi+EfWBuWLUB9BjShJekkVM7XTPomVw6yxRmwg/swR5QaVrISIkp7gBUznEiP/eVUZml++tuUx+FMWnRq5aumOm+javqWB3peL2dNoULQA06mrmZcCUyKBPvT6BI7jJNFBeRngz5MrkzsNEPbBtkU77pJ7wgis6yEByhfYPYsReFcXNh9WQWbdxDzlG0fVlEIDsiIxpxGf5/gJk1/7zurYUMYE7WAmjxcm6drXQ7QsHcGL9TWlWYxW//K5HV/NBWyBl5XkJJMyIrzOjiwuwiiwkuOX6rOPKf6QEnUcMiNYKLiyqYkRfXjnoysn4qbbWH2HzB78VeZu2mrDc2XMn2rwyPmv3fCEkD1M7RWJ4AknKCzW92BEdqX2047xAfzxW449JW9213Hl1LeLl+mm9FssdaHXrQmW+gxIZtfW0nR2Prg/hZFwPUXSY53BrkghSj+6tC2VeX4zsBeaFGUmSANC3nPv4c09Vg087GMpLQiLmIN3UgaUDmuxFHKYmtk1SHcOHy7hBQFmGwyuEUFJotUyYPAoBDAngC40pZ1WwBB8YzTePG3GiODDt1wfpOBWFEshG8N6KYOOt6hL6hlKG14BNayRkoM7ejCz8Bmo2z6hM35bXXJ/NaWMnlhyly8bNZcaTNK/g0aNqlt6xXepHOKSmZ55giobP7fjufrHr6HFTwBMd8hmchuAzdHOuxiLfpPMv8Sv2xyEkZlDNO/tXNIl+dUcIJP+50rcuJuxaUAwms9fc4Lgcd4t6uYb4cndhnQ1PznrFinFddYY04hNkeCYIfzalYzuDPohliacnUqH2o2oPGhZLmDCUOmrEpQBj8FAwjiuUyC/nPZpCBKesnvV774YjAFMr7In3qRy1nPc8oVnqmEA5DBC6JWJ1chkwHzLb7lhASjcT2uRXCh1RUL+v4ZNE+yQTDUHjWw+iuZnAUh4crYwahLPEz0at9k3hT2M9M6NOapJ61faXzjVkdz+zO4EMrjpazOd5qDsAz/3kbK93OcGFrWgsAHySJM/3FcmFrJ5TXwB6l3Yoydn6ZqNy7ZPK+KIQ6ZiG5inulbdpnucT+7m76CGk3ekTu61nPeexk352HfUTQlotZKU2vXERYm3r4tDFMG7z7Hx2oRJyA7Qq0TGWwhL8f07PkTcufZVJNgypRYAir4REocgJoy135mJcAb4PCprYr19MA3At42uwco7xJh1AxbS3Q0K77fkWwbSdTmMDql1q4P6qZ++sCu5e7upztuk2g+Pe+rsfp+/zUzR8+GH1d7eL3LJrbRCBowBRyLFcvPXbNXokEqWDhXHPIHET80r20TZjtky6gRjQWgNUxwD1B9TCFsLhfEGPYvrzBev4/wAm7rikMdWibTNhbHzvreva28mgUGhA8u5BgyunL4+ziemRSpm+Y/OZZ23wstLDVqvCDpSZNBIrmaY8BoAmmaw3kUWA6mw2XpzjtV0GhZGfocSjsNaEvxi5dRUQuIdh+G2RWZz0NBl9NyKs5Du5SQJRDEpe1NeXfdd4dTXgcW1Whqo28DbqVR5BTR7hG7w09T9ds1ikSjXObYu18KisgtO+U1Goq5s3vuWtNIlvN2L42vk5F1Gz/AVP6hfxnIKKq1qCuvvUKEsKkA3zWeP8ot3dTJ4DhRY6QvKj+VjZpRRC1io09zKCniYpaQsIyBpptMj2ZmI17KpEEq6rjAu04Vvbj86ZRxFotDwOi9yOwaECO3ZLPZYr0YuAH/2u9xHd9q//2LNFg3nxlAqRzF0v0M10y4zJY/RuT/Jj0culyzmK6btkAE6TfsxSUwqd1ojn9RccdhV9mIsxOp42x/W3aPwY8+9lAlLeVEKxRnZ+gi4CYHxRnvuqCYJB4xhAoG7y14qWFFALQeTIsD2h3tONUZ+aIYWXBo4+QuIeDglbKO5uLsi646txGYJvwU7vD7RBue74CU6IcmrD1TXGCPJK0PZL2zRAe6/Cd9lLIFLpcnZIi/zTQP/ahMEcenQyfFcHYvAQFLG7sd1LsqDzfgQuOFFJEPpXzGQ6jDU95cWbU+mLD0lPO5Mx8EhuqOWv8ZxbbIlmi+wORoIsa/d33YKWw47mna3O5Mrgdlk3dBAp/we8q08X4IfEP7eP3PWusOxpDiDx9R3baOJS/DdYBOmh2dcWhrpWTnaX8KTvDitlzFCC1J7av2aHrZsikkbZAGlrwFMb6frIAAvqMq7DAmFADxe1b10tNMCDgRa8xQVHq2N061fketHhi9OYmLrqjJbND4miYO43vZxKzN/MzzwKXHUtBV0TO55YZTA48enGuSU9QyP+N6Ji25jC4VXflmIiocXyka1XZT5otrYpUMuE1cV6pX1noAwqo09D1jzuFKrP250+uo842JFyOUmIdwo2reA1kQ9ScbextJBdk6FPnc3ozn+XvrsLn1awIozMV5/ik+M8ve3zi+okOm/8Yxs45/ikiMPApSoR9CHL54ruTB3tNfSSpywzboP7sEjlnnyrXBJq15j59ONdZ10IB2BgFaBMpFxxjE/dXKkhHkfi+U528ObTlZSYpkzANJbuoyh3Wkkr0nIF4pZfeo4m4vONF+2f+JP0KolttugdO4ZwmUTB7aIjkoR4iSJBu1r0V2J/g/LSotyz3adCq6fsVt1BXL/Do7zQCDbySZS+1ygB/CnpP/dpfYjRGQcYAaCQ5SILUFJmh3DfaDiZPzPnoA1AK7sRA2/JgabZ//25Jn53ryG6xqnUsGw9eayQIT/XuEpeuwy3VIBEdbJFYmqsmxWf77q1Zw3ZK9+whQRWR6gddgVrejD1qL+a/8YDFdP2jpPJYlXmjf+L1rvaAYeBvUiiDt+MQZM1fM9eLX+in8nGaj2UVa0kDHTGgyz45JrfYVSzZIwZhVYpXmvG/3a0OxpgfoLnP69JwmN3vAeRFwbGZERnSYelB4j17SflM4MHwplyxY6/SHhdPrMN67lrJvtAw3KzKKQcCO0dJCrtb0jHw530DnpqS1b1knvNRLGpfEI87QW38VId2OarZexGMLC4R9U4TmjLA37A96jDrHTqGWVSp5zryJSLnXM2/oOEgkJF+fNUZmKIxHQEFlN2YtzdQuwqlbrmCaTkAS8svHXm3RCB6xkcy/Zx1P2EusKgl5n8CCzfShS7QiCYt8TqvAtlATmMa81/jlg/uywey3XJRAnRUEQdhAvVQ5sTWFISBwjT1+Y435UE0JDyTPQj32x1dM8p3m9D/V9aZzIvh08zPHgljbm0WJRsfgb/lYK4ZjgCuNRdWrTm7yctIblBMrx7amfhcJo4VwTpcHoWppmF+2pBjSfeFxAdjVBVMKGELRkn+YF/OvkvK/TtFV0qnAnQnh9XSVA1FmmOzbMzzjJ9hRLrcmpxnwZDZUHsZNnOMqjMuP249lGiMJCaVnH+OI3f8QCB5ngoZDCSJucOc8XbJN/LNLWDvSmD8BU+F21K8D8FP2JY9+lE1DR11g4i6mvRy6dIj2TZZD3wIKfeXijrq6LBtKjra0lSX2og78HCbI8jECoPXqQ6VNTuuDzxNMZzWwYxluhStPZp+Ww8OZtS19oiNj2izjWkYNcBvMb6yNqZCZIDKsv5WGXXEoTqUIxvaauZvAyBuEfBf9/MRyFUGDnSYzusTejj4JpoX+6wQLJUP82QoQV/X5UO4SWL+QvWBj18dqBxcl0RmP4lg6TD/ocRO6q885dY2xqEBoXlbg12vShIz0be7LrG7Jmqdkgw6Bn/2D5gPK+HkWMGbLeu9AsyuzR1bBWiv2Vh93hmsYeXo8xsbOPmXe4QxevHYLlCE4AVKY8aNCT/+oCMA5WL+1hB67G6MONkf9LJUV2xRokT+EQ22lGbw8hklZLCT/Yl23bPXl7wcv1Fh05ZSoNaOmV0SsW0lFhJztdRTJsECeRqh77J14gX9zZE6K7cEdPwUn4vUxV/PzUcMCx98RtXr5X4DMsQVfvRHUvpKa50z9v0UO9pcnNm3FKBs56JRLvY2tdki7xjuefEky25tvFCb7zL5dj04zoVJnioLtFnXHJcXEw7ybx7MmqPhhNVDgsggcYhYRr3sI/Ef3OV785p3QG+UpHB3J0ehJLPGv3qX3Ht6/NMLkMrtBQmC5Mc85khCzmS4nk12mfHPozAboq7JbLZWtL79fPjm1f26S4Kgho3oqv6beHTVq1Pkvmdj6utEgSg7AyB9lOBbYS18olkltTm3Mr90g+Hopdtarvs/HAHRNS5dhXVmelYxXv0J6m05pU/c9iWbTbJ+/otdgtQqdZEj+ce8/cBrT2Oj/65YLW8Obh3PEqATLqNT//y/5cc6jho8EYKODXFyJtGv6SQtlS2OzxwMZ7I0nWFCCuN5p2BqGixlFwJcEQE7X86WX2wuWYz5C7goXJTQRC0TC8mqYaCyqrG9lSG/XX6nlyoBE4udshQrVsR/fPxN3tO9D/RZsxD+S9GJBCNNgTRccUp0bGJu/P2vRpFWQLFk1s0yIteuZXcWj27AzProXCcpUcTqHOEQ6w3BKQqc+rA3InDWdNKXxdievY9DrmZKbELP+zS5yd4USGp7YbVmnFRetYPn0Qusg/yDcCv/MTTi1MjT7eJSmeO4/LifB3Kl5die2XfpvXyj2gy1+HV5TnpBcer03RSisaCtBmm3oj0iZLVwwAj98qPMsYrtYSkDKe75SoHPtJhnKXrSlwZs5LbH8odhH3niV3Foo0cejQNTp9hK56KeIlbcUjr01yJzCkuDpYv92MR6E/K2CsVGM7IOvjDkH1GKh6XGxhBQ8gc0YMJIxh4PfIFd/mLee/FEgxEFdOysh5P2ZPp7jm3kp3UUgV5bsomm7PPreV3Tqhj2++6GkKAFJny08/gaPGJX2Ocug21UNz2CU6Z0FZf38M8ZgxWFpEFAwcgQPuZ7S/rLgaXjulxJnqvjBQNsHv07vSlGdWLPXwBU6RpS+NfFppNbGbl5WNkySzyYmKNLIgkLsXsSbihlIl+dOK9qWClSjW4JIDnStQXx6kWBjeVYrljqlGBPaAfIipSwScv8/alt8ftuHW2y+fmCYOeIHbXisBVFYyTe13NCFApXhnTkrQyIYtp8QUIuLln/SPv46leLy5L5sWM5R+r+7oO1BR3Wtze/e7W63rXw3D2d9hgpmOKs4vpux3jT2oJWA+TZhgYGfIgeoWF7VCAhHjH4Y0LgAl754CO1M2CYqKv5zpTg7C5k3cfShqhC0OCE5UBqbBC1hKqQdsYH8zHln90paWB/IjRv1fe3QHQ5T8icbZdlJ28w+96SsqPCKN+vDExA/hqm4sKBGN/YWmnNtPoH/sEmuUbWnYXbH4277776H5hRSzKymPLWx9R8oorjp6WMG9L2CypomkZoNIt9AwMhPUwqtxedKPZ597+fp4nPyLDIpbNa/t5UeGHeE2ZvMpX3zGj9+OLi+gbUOMgJkPBJXRBEw8M0fVtnsH2QZcYCzdeQ2FndaqcoJ+JJg+fhDrtg3E5boRauU44lJTCzfcZV6Pwwx9/PMgT9qhws5gC1qZBkqeactjguo1+RzhJu1G7BurcIZvlVZQDfVcLgyGkj7i2sGJ8i09zXJAQ3DHy227ptIHSjS1hFNJnJgZtAgSk3+rPoVioGtMH+cHR9QpPu0GIctN4CHgeEIrpnrOiEK/PWC6CUbKBn3dCdhFW+VavtK9PUWWOeysme9nce6zxcJ871xvBmiOhaqvgAbceYqkkYnuLJcXyniZic43mY61MUUg6QqGWpzdrV20L/eDr5qAXSKnG15F2sy++DE1WqE8bF/THhF+HQ9JFj2WtuVllejMD6JkfA7oqreLdg4unD5edEAdzcHRa6Kq9V6FfN156NzOmNVwnJyS/1i+9JCB+QSGP4VRDpfF/Dg7s1s7LAXWHqeHe3r5T02MWZD7JQwGw314pyljLmGu0RGoCGTfV+7QLtcl1HLCNm4QRMCUcY61g5TILbCTSRkTl+LWj+xbSVgE05DJlPkrzPuosMKpdkZLywGAP/BYZ6aVoaf+EXcM/fF6pkrhWAzkkzMMBmAUyQ5GOCMeVDEJFfGhj9DFWKyWg/RizloRQQLs+yphYRVHbPy6l78jqUfYNtemJuWmjg1juHsJU0Kxx/FQCAyQdbBH+szah43JNCA01sr6+W+2mNQWaD39JBac5ZdHo232O61lKnKQHhyN1kPO9q6w8dM7lKh/DX9Xfk1Nq2/rej/csXibBkl9TrHcMuvBiw9ZhAYLN1UIw6rALXwWfyoKHTbutGZ6YJL9QD/CW6VEQH0QnuAKcsUATWR0XHXOK2+z6kIL+cYu/XW8xyv3QpnbMQz+/wwcsTIlbvE9ytwJn8zJ6YjyRNIQ1YjdCPNzwLM1B2dh4ZzYhmZc6/kEXyEWh4LPtZRlT3ey9Wj6T3HUjEyqqRoxkgxJ0TNMCxPKbKr/aIdfGgbxxobKD3JqcUot/PD73ZUmnN3w8CYRfSu4/Ll9ZNdKW0wHEglFQ0h8a0CTJp9cUVPhgxNf51VCl5+282iO5nEzBNgeBHLIPrkGa1yLI8BiSxS0ss8gbY8w13KXloMtHe97pEzFk2LS3uMCTFTS8RpAhqay2VE+9VH/58cBe3JEp2uFx/g4wItXWOfWDezG4ibzKWysU9rRgdNcXn5AWEWnTzIWUij0okJAlUMBk4B1We+azZDWG78VBH6ei7PMW7Mh3rhUoaBan5ZfuqQsmMKNq1BMMQJzQD0bosboTkTEdTdCzQ3rG+icJaz9aKlrknKhajplw+9R+iIVGSebfjLmHMxB6cjKtCaTAFx5azK5LUa2xxpZi3VVi8na8cGO39wDD4IFmHa96DG9Iy0zkV4E7zCi5Pr1b1Cl224yKgDiT7Z5U5S9N1Tr19OiiZC2q3v1qAT+HIP8t014dSEuWa+r4we0B/tU+P4GaCamxv3Myd+RRDgX30XyF2BWcAlaYIuAB8v54MYt4XHquPo5B/PD7kVfu6vwsUGZdK/LULnf9nHHteafoyyJYn51sI1wlI0DkTwOqSgNWDfh2zhmrGBUpkspHHmKi1K20545RqDkGNWAYaR6x6FbAuw2Ek9F3mFargCkIv0i2+jwtRjP+KnsAWAc9Ryi+umhHBslMW53ztKgk0c8MrZmK069b4VZRehgIek+eWj2XlVEluEw1RMAbFSYrNKUQjtK/mbuBg24HKAe1qyh2N9fk6jR7CxwP6TOwT1ta/2twU+zroZ5TJW7Rg+L2loXacAuYRMeqGUyYZKiY6r8eE6zHg1s/jnJrL1h9ikS+SMWahDxaqhiMRGi/Udg44i8ngngquits+u07NAfpaSniJBfGCLliuzxutxT4uEMM3xs3qydn/XdCPlPqbzyt/+xfoI+XtrDnDTsovnrcsHc88Ui0Qqj+XZrkQslhQvM6bI3HDwsVqLW4X5on9n78hGtVowuPVAwIR5TbqxeXrst6UDe44dYY7UNl/oIEItykUKychdgqlhIWyggvXDkipgxFFs5yqWvWX+oO4jowtOqDT7z1dOUoE5Re8Or35xmfjzXlH5U3Jmv1/cg0IZrKIDMJBvBsqGD0NvBMmzZPSOKZfzM/qQwxUZzrk4RUW5/VEVVo0NY8zqFZwL3q+rNZuFSqzbQKY6nO90QkqqHbYyG7Grpiy1l8cdfA1yu8GB8mt3ire8Peit2VYzTwKJ21sT8b33Iu9jJxbn96cUlrlNDGDLX70+rAYuLypD9J1QpuSn9jia1N50hjnSsAIZzPKxJ3UoMVDNkCDEmo0AdA00ytdej/OnqVXPqZwOBmTdcsindqVSoYwvA4M7w6ZVjUuE4PFOG+6qGjCVcSEjkuqRmd0yUAtMHZ2mi76FlOtLNPzoOpez/kZYQyknlT3sQrZxGApi4jGKBF6pTaL3Hm6mmQCUOTWoTn+WPgRx1E0LV93yI6NE+ht0id2l6RqL6wjP81bfFz95A7p07SIqxmudPJDU4hMu26CGnnSmqKz4Cmc58j/ZNn3mBe7OhflvT0paB3QCTFSXl/ul6fapH+c9rKfTgAHViGwK27Ag6Z7GFT25RBO9qCnJWHK8mIxhH5KW2EwXZ9jxCKwZgiqai/GKPDBYzL/tL+KQMyX5Hsrh8SQF5y82Tr1FSuxLLrUMeN21tn3w6kclgEHqC4qE5KbBA4j1oa917JOW0IVi3RgtG/e1dN4qQqLCOFNvF/LqmNd3ybFf8/PSO6rA+m0CcVnMbs2e8J64xrB/zvIzYclW65Vw44BF78CNFFqYaROvL+NdcfjPk6GQGaop3LVTVs+0ZuGavGQ437xSiDve92eSUxUed2b9GWSL3L9EXjwwan6Pkn5G4OHhFAZ6lu4g1oBlVp7tzmJPp3Nwap4FgIXL2gIDGaeIUMFg1Y89UG0mkMjKdcI7d7ohS8xOIZ3akJWxVOw2dUcirqZ2S+kCcuteEqMATzCsOBfLHbeA+bwrb5pbxpgsf6wyxLnJFbWxBj/FmClHmQ5P3CHmbuPNfxaBrwY7VcAqYDT/TdVg+UJ9kFc0dUpzu/wH1D/AxVtjKX2xobLjqQE62OfLgVk6LlUoIanGsfAiqtcWc9SLRex0BXGCIZ6i1eerJRRpxowbq2TbtGJLKU4+3pYTBEjqDOEu/W22AwN5MTrCo7YnefJE3cuHT9K7ejsRaIyZDKmSckpvfaFc4ZXtcg9YG2e+Q4c1tn4EucJRIebd1z7c73QXAy1ltAzTnPOvdBrke9/IG+Ai7yrNCGJ/Os8E8OjdS1YIAJ7A7kRwv5j4iaFTSRJtQMHNAXFPEbRLVasKPxgfXVwDHM8m7/SWLtolDsiJRrjMw1KUOaijVQxbIqqiClXbI3MNHcGqahkpcCPXlVursh5EftU7slnIOGQoRw7AQ23I9kHtPL8OPicAfJ8SKZLFQEvi6PFWCB8p/ZhWW2zTib6QZcJOjyRmBxJyg0jE9N3SwqiaOdHrOse8rPC0Q5eIDA61MZ6LMxAKkC75FG9WGzD9q3nkjKk5jVBSKejcaq8VYDeiOWPSNGFULHfdhwzu8N8kvdQ5lOBt3Q0oGv9L6tyaBQbGvJSeatKYkhiULGvs4vQAZ4I10uZuUJqlMd6t4nZfmHtoVXZqEjdUHzMhWVqknZ9nRJ7/vU4MERQ/B7paz9JWfT4zEbfFg3+Jw70wPbF5tdgAFk/L4zKgo6Utt8EiSv1MEPQ/vX7uxM+UXaF/Xc9ufzadBB9XaYuoOFBmVO6bJbRzE5sdCYbbi2Pzml/njGg6IUuFsv39Le8ZEAWv8aZnWPUovfTYdBgJObyddBH1Mes3+5R5WMQ0T3xgqc24lbq5Qkv35wqk8PBb0GZpt6bsqVs2PpepJz15yciJY5MnK/y0kJ3Yn4eEexQnNArq2rMQ7wsS79MGUS07O9xms10Y6eyj8K4OItq2Rin7TScclyyOhJf+OQNExl87TLwGbaVsP1uaCJZIICG1YXwK0o8W5BndHkb7TrXXr8XpalfRYxQ//EGsbN5w4RRFb3+J8ZbH/TxUKH7kAxjYtRYm4H1r1PKMjmb0hcMK85Vq0uzoKxkm0RFVhZMH3TKwATgGjkI/p2SOBH8Zx+sEj10ZgDP+VEs51hwD9giYvfV16lIF2WzJvwXEDvkbn31aot2OlT4FvKe5cwV7RPJJagFSCG2BpBfkaBa9U4UAg36iHwl0IOhJnZxTU0YE9tLsOi3so8uV+vhlPKQ8vJaPe1pe6bCOYajq6HR6QFZJJ5i1yFYKkWJiHXEMLI5GQmhYicefxB/B52Jv4jrAA358D5J00xPO9oARdcjt8zw8zNHsw+Yj/AFFTDbGnnFL4kfrr9qRUIl+A2Y5nltRNJAUg8hqXVUDPb47CGY0nfP5XWQUstlWu2x2cdpAbj1KtEqeFCBPn0/5JTmXfTDFiMuh99xHPP8bommfj8VC1+P8bRi43Xmc1WDeZ9kFOyh8fxPQJL93Znn8U285rgOlvTOCnlE0/txXf3yL5iAjo5deOgGrTEalr/5mkIvGLHduAtoVkCMGNBgxI/2YlBKp72J/Z7JORXBsFGsrsFBfxPIzlo00W1V5SWPkjDV3u5z6vggKWFihs7WuWF5MPgLbcekBubdY8FhOuS2OzENNOV3YE6QSfK/fJheQ7C/ETpSRulh1G2oEiNFkjuCSfAsuqKd0c6xZMv93xtk+44kj5jGpg9ScDXil3Uw50R/K53Pcy5lM8k8Ki/va0v055FXpCuDkn4sJUQhmuLc7ARRDszkLVKRVQOjZzoSHk7giUZqm+fp85VQtTfPIqo4t82Y9TaO6f5ee6POchGoVhiHocA9kfGchDYKmJ+m7fkyyAgiE4bicPF1QDF76or5540KohZURNTxNKpPbaYL3Av5nSL2HkQpuNFnsLwqIm3rytYY25X5HeR0ejJrQW0G7g1LpzRaEy8jzQcbHXwHMgTXgN3ZlvfduFaRN3Os9g5Si0Ltb9DLcyTodSx+bQXwq3xkNbNVURkYBW8g3wAmdcSHsnJNZ9cBrFL1UoQUU7x5J+vfRs/soQDP+3QiWJ5fu6jxgEwayBKfSE7C5JE9LLlK+KrYWvCeXfCaD1Ml+TftuCjpbw9+5GPY4IHLbDFQ75brycpUbhj4E/uUB3fm7fafQvoN0NmkEu6bQTuK+fqvRY/C8BCcwI/mvNKk8aX750xeHoF0WTEmkN2rkizWeEyuqY0Bc0cQ2MHswF1st0Qy8ks4lYyUB/MAGBosVe3rJEyiQBqfROCRQIGXp7d7p/Lbeo7HXSUP2QMFoXsJGxV9hp644guRr9RIY0g88Wyu8aW9Oi9MsCfPKGNPSn6AX3Iv+OVSjhycVLEo0qNJit1UzpcofvdJvIChbiVlglX8UZA5DT8m2KEA3hZ7ZDkuQ7JY4Y7uuwlfLN5no0M8HnPrUIgGPzNL2+/WwEnIKI0N+2vFoShVGWjehmJkM/bc4ltVXPxCtjA0PRyEjF0qbJdDYzfEg+iu6PZEE37+9X9Q2Tv6D+ZT6uPuDES10/JFvs+MEWKaRgIkKk5Iwss5SJkKL7fFQThMnOrW0sEOLN76VpCbE5FtszulUBYn7VBcR/IQAr6Osmf9hoGl6dvudTthapfQ1WsKYJRoSlIsPGWBJ2v/FVk9MHkLEUVaa49M0GjhUs49R/lhpk5h+TozXfeLqv718pELBCBAuEMCA5rJsHJsx4/QzQTXKXnoPripTP/syZZ+45WKdyB06yikCDFwbex4bdnNPndNMzoUlYJXTP/ou/GguDLuVl86Qv4PirusnX3UKwN8EGvJcRVsyfi7UMw1cnK27/dBKO6B/4WPd+kvOtZPy960MnyaEHLghk7eknXcraHyJZonMw349ZIpY33PFOjrhUmOrgtK77bEiiBwP5Xp6UTv3q9se0vJc4c8poPJoq5DvaCyMQjNsINvwAZUBx9rz0igmziJxC04//SPgyXwTGVTpmpIIPlwVKk/8gnALT9gHg7lysPluqxayb50OBkze+GADoQApoEg9ZHda+UCvydJ0wnqJqBbMfsXlg656G2gLVcMw4nK2AfszZHGBClL2b8FJ1M2ywMKCanA3TwH481PSWGae89H+A50eJ109IOHkJMykOPdo0YnwfGSA39917Butcw6vNA4zR8IlqYF+uuny+ipqtyGSMtBKdWNfPBLeMaGTDI9Q/xmf+b8J2zSUqjnPfWp9MmnY8XXG/zDDMvkGmHHljodyVMHrxaKzRALY+CO6sL6IkjeWfo8JyLUKw9JMlvgyEpfh+kPzQVMLq/nL1RFo3Sar4daRKSmqFQ+YLxrzZnIlCdExgOls8mLqnQL7PSZ+qubfDhUwkWcANEx/4eaD4nsktO5VuBDp365Hjl6rs729ajnj5m2eBo8WMF5zfcL57QpnMgTqLvM+AOwjsnB56t3mUJciDzyaaHe4d1iy9nHxXQ18A7glo9BEFmbSLSXejRKvlel2MeAIqaJRqB7xI3mH1z9/d3ZOt+pZuA4XqUSH3JCxg3AEVsio0X/FyTWW8hc/BN4evLd0U6AZZ8bgYtHslEJa3Tl3ETFnNr8SKMeZu25cN1+SiuBTK2JcSMDVsOErq2sxTMyAn8q8VwY1l3/Tr3lsljVQdM0kHqIPIQw/K/jafk3WcwqyZI6ARBfsDw0ZDltOBZ05TC3V844sAQgqbct5dsQaK2oqnOaPUBO1H5+StxsbkZRvdEJh91drvZotlBGP3gvPBk1FFwE1UBeqHkNNOeVjrbrolm6QOoWx7wgeeiWM5APTnkEckZpSNCtb6DG8pmngUhZ7aFG7IZ3+9bhf5W+PkMDNfPoR2TlymTfmOn1X1HFwpdEZllw+osg+ECjMnYqL6VOW5Wvzv2KpBE6yNUjlzs9gFtL7ggpTTkeK8j9NnEml/F7v4buPsxXqex75Ga5E4THX45IqQvsfSjImzho7N4EunQ/+trDUICmtFZwEpGmq2tzhP+944z9/Gceu2/dNiSqsLFu6YQd7QbHLnHhYeE+zDjZVSrimezxG/KKeqhPyQx3rx1yI6jTtXgWWKr1AtjiBD5jh0rkpeUUGnMU9IgDnM/eTjAC0to0BkInJhycodRPBjZvH45W1YqFK2eBPSkD3uRJEnCQc+For7mWYdnqyS9/ZrKYNoDVCGuMR3kJRQnNMevFjIWy7wfzBEWT2oyehZ/Wn/hqa/NDw4HklkREoacaz5Bft8JZbzxzpfD8uYetlLfDpKtwN4XDRFnnMmkYTI5k9e/yhTth3GryOPmDcBRtjGojoJp7fnMoQIS4lcmS469n7XJfGX69TvmMrET2H+4fM8wiBvNuubvOYeBb61OL2K6E88hMB5fCB1Ov0n1HK8NW4jf2kn6TICSShfOh0+uO09lsPokA2B9aczofiRjaRHiUKu6sYNuZMFmGCnvv/qIUjZkP+9jfCqdHkO1oYKN9JS194OdC5c+cz/4IcUwbY4U8XQJmL3Xkpcfv/ICKB3n5bREDd0ZAwTPIJNB5TlXxJbynF1+AqSKT8/Kidj6VfQFJwbunngC/idXG3D6IlYWQPRP+PfNswSZLhdNzhKkZwbFxTvRVryse1qHNaieCIVarpEEcn+P4VoO75ZXLZic1COGLpGykh/ulFJ8SAtpaze7eBuQu3wGBlhUnuetIbnw3VuIBkn8Sq+m6pAN6o2yRDd/H+YA/EaNMKEF60DmLDgDOmelruVaPvzuF3SFFmMl0C6+QVcprdPhrmPTccRgOfP/ke0D1QP6uH2cSuGLZGnaiCjOvfGSelWlgjS41pAleWebdupSAsZ8gUQ0qxezriXYiA25vWyJhIEWPGU2QouJn1q67cg02A963NpIuAgvniX/nU836qj+5EBFgdvNsN161jWr0qg5KWHyLiaCMCAjZT1DAEjReOdcq1OKE7yrQ1A0iAah05M1JkcP4fhx1weHwwkWvl4Hk83hNGAulvq97w0zzzgqqB8xxbMavfqGJzICp+QnjEd7kpSVVHW8lmbexBji+O+4xtyn0rThIN+bNFz3r2pUfHq0lBaImN0WM1w/WWuBNjKuW2xXw4xiaa4CPCTA65RwxLZaLLoL+6CSlrptMqhC/hHaqxfIf/3+HtDomXgG34edkb434Ww5BP++Znbjxg6l9z0f1P5EsXFK7ysgGNcLSZaAA8vYiE6LCXlYHquCFgImtzCYzeuNtW6Yw1Wb/SIBrZ0GFm44YtbI/wtjwMK03WNsxDDpHwKigAT16IyC/Cv4sIKZopAyr12PoWjrqeTHM+AuThySQz6KCxeAKUyF2VqOUIzFB1nnD2eHWH+L2NYy5VOCV2cls1I9b8jCBp3z/LCZpBzZ1qlfQ1Do1DFxuw9y522yvlm9Eqo9uyaZc2+79giUxMN42Rc93Rq1F6RMxIZMU18pAZq/q5sCIufcA7esPfr+hsCZKutdVRb0STUyA4rMv8C85RmhsScWbIuVmYR74K8xgYD4AwsZNMUAHWdjm78Oxs95eHf2kNJEzN2vPLz2XaQrAp6r/JHqi8LMguga6EJTEaWm6tg7E7TlaJDHlJCQZ1RH4FMgTBj2McUZgHbBA0cpqQmV5cuETnlso/8/oKJ8LTxWhroH+zbQNjl4bmw8LRq8d/uEabS7VQ6CYLhOs5QizC8WoJ6r5NSePMlVuxkMa4Lmy5hSJv7bQUNaV/aRvgKJaGUTvcUEGH5rDpFzDhL5pYCUxiucwYQLVmSpxqGl5WzSDEvZJVqevwoyvJZ2qQddl3HKJ+DYGU+focZuqG2jOJ+mfJRUVpoFL7Xo73cldDO3GssXEb69Fq8OkxoStlMY21MLNIQ3WAZjDjZDAChJJhkb7Be6j8CbmDBtL4qgpHpZqrPUrTmieYkiHn1k2h/zmYKGhsADejgUplmdwaKLiG2cSMdKt+nKhxFMI9hhJTkEIR9PnRXCzDKKAJSwS5/DvhsIWp2loSwMsdy1S5nEcbjHZSsaGrwlMLRZZLhHAO8G4KnPn9+04a1bSRAr3D+PLMAcu5XVjt8/nvFxDmmUL7fwJ38m/f4c8IeVs+peXg/kIQyi3t7lW/uE8NZE6hq0Ox+XiahBcNJVd68+IzpT1oU/KyR813mf75Z/e7SDogFe6PnP0kZvzk6lUXeLC8kF8VL3uZp88PUBF0CjMS8SgPRk6toLBVfS4sQGGJhyrZEB5sWHegF5Ly4drNS5mDWdFMLl7HhikANTrFtIjv3b0bk3PqhMJ5O2A5+k6NSSIs9MGhoySKzboh/ehWkHicQapePyII/yZcrmIlIh0neC+jh14OSgoB0/p53OnEH2jhic9StVEP7tmicXm7r04h9lFxcbnhxETUJVwuMz4Ae1KdHygy7AwTivEPAV7Kl3TyAQGg5DNw+w0iLSEe/tCOnsiTxDgfnai8zyIbc9CohwhlRZTWfX+ruhXv1P8WnnqcehEkHv+5VPMxeNzETOmdsjSN47mt/6ec4eS0msqK+7xkAp/O+otNp8eC5cAAzgL1plWa8M5KwhIza/DC1xm4Cnxef5a8v45dJ1xreB+uJTW52ttD9InZZTHM5aLkla7kZH+aPh1G18FsnCVEtN/eR78oo14yqcOJPcwkgJSst8J3lC6C9hqexdQwzXP53vA1C5i+NS18bGBRFrIVOoTwD70RoxVwZ1U3N5dv1aCZWdqAqAoNbeYSWYO0a3n+DYVZJkF+/NEPn2Zz8K8DVkZGHoG4hva/WtJlarxUaPAxMVwRqdknp16S62oQGeRvVxpK5oSC0ZzYnqNodMiOwpHlBEQ7ekxRsVdud/7jdRgpzM/RtdMgLo6kUk9vg7OGQQ8ehb/oCRUBDu2jCbM6nJk+WeDWCHBl1BNflP9t2pBGHssqgGFNag5lHXSrKveocX8imLGMl5sY+O+cAUUB9Tsm4fEduj+TkMgycKY7usBgC4dNljBRnDHCXUz5xme0BMcMdBbkupwSFGAenZR+QenH815XNrUSlY0gv1EWc86HpiV0loY0KgCVWsyLfY45Po7CWS+jKPwm7BwjspO7FFAjIH7ONQtsJTqbcQXUcEHXAU/rNqlAXUtagaRek7qzKc/y60uODokQTtEHlJf5N6PJzDRztV6/6iIQElrddaZVSH/sVqMr+VsQtxrb2qx4Eif6r3NBI2Bdelg45ZLqYEgIwlG4eUvn3YwDWqDiIK2d+fxaoVHgEb+7M7NquIwO+/P9d8veGw8f3VsBtU+63D0mqQZePLMtx3FyWYX50csCfa0spKMhtefXjWH0y7W+9Vo9tQPwSagpHQRsqVZl/gjnivY3j835cINUmIjUnHKn6nJNOH/A4H+7dL7l4gtq85umw6xbyRh+8CHo4iWheC+js58njp2nfbxQtRPV4M8xMJ6cv80GDJ0Vz7aST2ZiUz6FyShtaQijzOR3gCUevqoLLF4g4NFnLlpKs7NBdCzro7dyj6FOwLrb6LjtEVUMLHdhAR0Syp91HlU0O9ATpwmNKBTWv6nujWxO0wvAS35Xo55Sg/rIqB6gn9H6YEVi/sUtV9DlsDPBpc/ZEeI/LU7d+pjdSMRK6ZmKXdB4pP5NJniJ+kOpDtqEHcoQAt+PxvhqpKG+EaclNa3lPkwhBycpWOVaCNpVPOhaRU0mCQ1h3zNFKIJ6W0ISk7qWAZwtFJwmdjxwPHYlI7y7zxf1N9ZjFkodWo3RJ57Nv7yOeBrq56zR81PcAMaxIIL1yRWI6tjr0YvmlBtz9tuxjFmi2N/63V3p62ggY6AqdZow1KM6dHxWc34oG5X/0HjKEEHkH4WDFoWOWHDnNnYMZM54f5QshL5aOeV8tcJQmof0I4PtXUM/nnpOP+1CHIoC28sunxz3J3LHJxS628B0K92eXDS9Rjje8ShZqPtxNaCaIUU3VR9+uhhELzmJJzr/QMSsEeyTXbmx3XhLalZPB4mq0eRtIjpb3GrNt8o25P7kpUzHKUOo+A202ozkpVgKQW6fwwaIYaWeUrO3yJACp0tVUFxHxBJ9wETIVbA9InX3t82dpeQJLYBszeQqYOSQJvmUcaY+XEwRv+7K3K/iuJ4MYzEuVbICig5oLQS1KmpUiC6nezGeVu8iQLQ5+vrf/E7GKBBKh0GMbzWbSwFvXQx0WICbDlTQ3jBvfh8OxFdNybMR8WhzdXji17kve0wv9Dv2u4Bs3WEPxjWlZoe8nGvNWGk8JeMGM7xHLarF57Zy8DSrLA80in2hnVQb76sFbjBLhlV+cdcKHNrciBNrN+04I+ArFqSm/xi98ZCwzDrjCh2gP3LIujKEKxkAZrZbigmUz0fDA1zzsHz9FbrnxT6K1fgY+h4mRQQC+htu5jqMmJQcjdru3qVBVCPA13aLKYb1Pz0Qzz2mQ3Z2Zf6XTMKpMS+qdKPm8K2klwoSnSSFANyP9x9G2f244TWJHMgK6bDixrUuLymro0qYRrHsVCqFCNviowetx0rOydDeyXmUGElB+U2aGsdYHPqjF+U94Cbr0uyQNXLMNwlJLq0d4Wj0HqQy84CLWm+PvhJBhLB7yYDrw0UipSDeptsdQZYriRcOdus3YaTcOC8kumLf2BzQGesWdALS2cnJ74l13aLsXZcwoiVrUrfyO1kIMYJsWs0C2mx2kwgI57hBGvYGWhDpHUuZ2P9DzlftGPb+DDBt1MvgNF0qxRcliygd0H5e6YiZvlm+l7zMWtpozu/oAdrQGM0UzTqmiat3rvBfw5f8TfSe6W83nKhvcEamrvDMj5WD58bvrSrPZ0FBpeimV/rWDdquWMR63Jq6g4NyDnS4ZuZUDlS0AdRMkPuzIQeJ5CY3I/SQ8lMJdFuf+kXNpedWURQ7SzqtR/LIqnTq9MRAMmUTRuEj74NlrtPrM0e2KHVZkxLEH+slMDzPWMRpdbSFSKOPjqRQj0VXafwH2eOy2giaDVv4x0xpmMSMNyn+2qPVL3V2w09QkTPD9m8+nD7uI9EQ2/VfhxqOeo6/lIpLPUYTcP1qD5unRTdUKu0z/iKwxKbNluESGL/Lr+dRczvcfxK1kKh8gUjW9eoOVo2SHeXPS9gf/Bk+MlhYagBbZ2+/V4nKCOtrv7Lj5qe7bmK3jLyHW56kNQQXB59F623m5sAFiwIOtBMbWkYkzhsrNY/sYPLq+fqRKOR26VR76pgcsqFJ/qAxlHQDG3o/Gd0/w7gPPDT5Sgse/0z3dF7pwYfwXhMehLbvyAiQSMKxKNhdrvRaaDxRw0mcUPtYSo5p0v4iKDcjNxsm78YkhS6dcCkMgxSG4U9zFd47cJoWjeI5SnIwYwfB6JvbfjtbAWNOD1yIY9Nq60lhlIIJSeTtVN3RdgICxPC7Af40iTLYs/ekD6OWYZO7l1n6630uxLK6tqiMwKXV/kMNH5uNXpm5PGR3H19F8IyVSLcNf8LHbyZZMAWgEkw9/jI1N+RBCx57MCSZwjQcT1CFCtGDTI8p+7va1z2hv6DWwP7u436tMJQtI29ZWt8N4upcI2m6vBq5LxDawM9E6qdf0o1dTCktWkqUhFw2ulBvYPNF2fAahiKM4XaFcdSzYktMaR7DgaHEaSG3qX79rssywJ7Jc61w0g6B6F/j029OqNL7phAIZ6M03J48uBCQD3kxzcqjGtXMlxiVDG/isKoLEUnrOqfleBtX6GcEw9AkCMP+BBhUsk/nAKMhhXSE8+U1uki2d9xbFPZkIS5P9qvpLlLFMWNkVysMdWs6c7+zJaaDy+fOrFwqsKKodOIjwG/OV51bXV+EclIlKlrw65PW7kKW35f5Cv/vXpf1GmrpDi7acn+N5E26ibgfUg2EtNvQGu1eiDrPQdoIwl3RfYdfnkaJ1DKp9hzKbIduy4rNA2td4wcHm2CAHV6+ElqWwa3SmVEGpOpm4nD5Pq+D7xykM3L/4r8P2Y7bAb1PUwUCeu68WMmByV1PrREz/f31q2rRgbkftZNgNc7W/TBqA7WCMYbDZiXZ17DtWyMTueYpiTkxkJtkqHcnHoI3B20/U+esnz8Awa8fOSSqVNYWOeVAXX/mkIca7FLh27wK+tXlQo305AFl91uwquV494JePFP5b/xSxUU42YfNFM6ic/b3LPQOE2mF2B2/wMBQJ6HlXpOchszmKS3EMryrmIxNDMlr5odXSmeL4P7R9kk6hWD9M0+jC/xsonodVtlSEDItv6rB+JRNK4NVG2JvTrcVleWO1GmGH3xDm6a3c+laFfLZKGSqeL2KL02C01CrMEyNXR3lqAbMxTFWv0KX+wDY/SMlpgjJLKu9ma9FWXAfxSx8fMFFZXl/tWc/ZxCABZF8RaCzkwg6Fb8Wcrnq31Z6U5bL0y4r7NaFH74pnwIgzjQPXz3zlMSQHlf7VLUehDgUlOM6GG8FzEK2kj+Uu+nOgOSSIy7GCZSyJy9LhpnV2sS8wtDulREi7Vvr4HCENW1ICRsW2AuAcomQuwg8/pwi4sDQ3cNFHHzQzRgLXQzTpIRbymY6kJm8jA0oCMBhEwpK//lo8joND0oEvM+P1XspxVJTwbT+qo+bLIfA6VQdxUeWGS1gd7oRkYk220H2LhmS/+CwOF5uMgPaJcEazKpt+yQ3s0P4f4RsM+VU9cGkN5jU813yqKFHsNyMvqkDzlcoD+Mfw4now6qNWjg9nWftZ5Jxmuf1ht7/x5sTH53w4GatCcsiKd62bguEDs/kzWnNT7PB69bvaNDSn114PCwuZHj+E0HUGWxetLFrv8Qb/SKsjSHBVBjqkZ65H5XuuupTcFEiTEek35RisGX9yqbak8WdIX1vvbTb1uAYR/IUVc8bcMTsN+36g+HqJpt7TCoYnlkQV8pzA3R7sZ5SDPN4Jgw4p8IsF1YlfgLqFN/rk0BiZ9gA5F4hXj03hAhBriIqcFmsbS/j3AewnFphv1PXNtn+1ZIqWSLT5WsNaxaUKXXklgrH+S3VEgUW82wQkTVBNJLu6rhcVAneI7oxzyaiUIRhiXzem0A3ynHvLxGckKpc/iVvOVTXvd0BQGOW11Cl0WVQ5oYvSxnH2iqTpE2/lq7mZRbUJzkf5whRonNLRCVokmCpmwxnSwyRhDkeElG/JFv+lxlqjtz3EOuvg13Dlj5KCnbmDAvA366MAyJ6PRs6Z8odNxQtGHHVara0vvXfMULBlR4WmSy+0byzuaMqBI722perMzsOJ714g1sP6t1go+dhquxMBsdWBEdAFUaHmCSUnVNk5hy53LJKkCaiPW8pbtQBfiXdGWin0bkbbPYFw69GZAhNCpMRXfz5o0c0dgde0BZtYkOsrcwZb+aMbhn6knRqQbwfLLryigcrbYZ69u/maL3jwP542fuXOlW5OUopcVcV4NXxignDvX1x+XN/aUdz/KV612vX7CcAAGFBYU5fh2EXaCv0ohmqiWDB6+rnwfyzobwZyzSogkAztEgkWBjUfvp4802tbBvJ2JCOy9htI9ikUvlrtXtMlCMDwwxEfgkYeVcOBzzD5uh3PR3arwpzhkBNzCHFWzDoLYVhz/NtC1USWKYUBtFvEjnX6ZQhYqr0+a4OVI++ugWuH4y5isYECupx2d6xcXh0eTbM77XGyqDu9ebvD4AlNE5tES99bmlYep2N00NbflVtwNtNb4Rd1CPofuYwsXmdpTPVsW046CRpEQJ28QbgcRqn5tnW3p2i8umMw0012ZAlRz6Fn/0EMf4dnKWq8yBHyjX4dxDMQuUkwvq15TXiYaf/+8x5iCX7LZVyR9LnhIebizhQ5Zr1KA1KYMnPJl1Gkl+DAyy+AAqW/Fze+WKK2bc2+iDcuwXyoQD+ukJcCiVkoG82YoRWTFHhfNWvAGY/BS6dKhgFStGbe/tLvWg6CKXfEYsFmEsIyeu/T1fguMyJEprOFyBK1sDPpc9avIuKQ7VvcryX58aUixTC0SeV5bjVxNaXdeaDsC3gv/wZqnumQgw0p8YVMFqfgzgTZuF5XWOGvBWxG/nxbHBJgg7QDh6eBIxb3ENZe2mA/qYGiUSSmaelIKUELs7k4xXFjd5LunV2if3yfylgABuoLi2Hoz5XfJlwCV8g9ToiMxpfHC8vrWECJyhn6kSWCUXuyX9XBm0l9nzFLAqak6pInMk+K0W/ryrhhgTIvtLlSPwvKVIfG01YfYHwWtfBKFpeOzmT/0HHvFPF9IQATNHFRPXEX6GFzo8X70rFUyGFQv/WUzEsIc/Tp3SppykoYBLMHaLWWWiIhiqO55jhOaKlXy3KYWPOMbC+rG3BqkJuGFDxnWJX4IEfq4/5sknrxFnHOfNDqcisUWBXlL769hBdV7nx8zyXqIV++QBgQLQUMELJVQFyg/oZrb15m/rl79lwjRt8JsNlFbyWOuQEsYF673VLrkN0SELXIefYNTd6Uq/GbMOUT17fckd1hnYfRmeulBvMl03+QofzIdjdFixCbEdWUCYjfefl+lozcnSQRmX6jHb2pADCiKiEaudz39y8zcawFKa5U+doRzU7uceWMFAl5Bw96LptKeyGmXV7DXDmPnxUhghFiVfx6ZwZ8yXk1HoboH648SqJjHao7eOFICn54LgtA0cl/9Znfs9kchKlIO7mRllc6+4i5S4qzFZzB8EJTuP61cKl1q9z6YyGu8CwjLBjBJLELJkPG8L95Q41ulmSNwPKRZ0rs0lz6v85oGkcDSn6eGjM+8cuqgs370x0vLVLZUmkaaMrESZlYATDYGo4She/8wrIn7v+dvcTafpC7af9kHJKISVwy4RgKj7/uu0L/R5TludFDAyLnY0Mk7+kUjmNCBa8YW+k+WvPJLXzD2oytXMZt0eav/lKqXrC5ne48B9x7ThagXAtELM2mcJt7IOFXzcNNl8Mgqaxx1jo9WlnetHQGNIWqEuXX8UYPx/7x3a1ueH1U719HM2cHzv7ZyBa47zfyJ5SIq7f4s4fHctQqEye+Zpp5Ys4hWPeke4/nL3mKkOkustnIx34JjR2+lI/RorwuzL+DV3leAft5bTI20vEE1B98UTuORRSpALHJeFrn2M8zJnGt62QDWVTPMXH9egBcDy1JBY2bkOpGPDKWaXPKZytCD95gnzCUTdHC0F2dk9n2rvNrj9z3y23keLbeJmGJlVwRC5tnUCWEWNs0gDyMMTskA3tJGpcs3hsD+NfmGzw00b1jxhTWH5N5ipauaeS57OiyY544q1MMOn0Wi/eDAxuijiF8OWOiTa4uhP/I4JyzmW+AgxdBkhSCK/wCX5YXxU+Lq7dWNdVP89zqLVj+Ih482mvsgvXFL1BN480jouQafuPe4HvnTrDie4zgyIgmrFNM4Fjxz2ZVG2ZO90WfH1p1zfn1MV++p7RCFobBszOltPw6H2UDgE0/l2HTj/tXBwKUji4vntW+EPeB1G5Fq+WgDdIhu9vfrmUJVdYJ96rBM2OlMcrQy4O8t2dcw7jGCjSGnHupTLX4xBaxxBJZOqF9F4lEizADrBYvH0C4c2lORGDKRADkVl27E16/tpYj2qf9PajwpUbET7glAn+3ot8Zqp6I1oMPqHlZ2tJzlPcZLloJjE76xLJJJU6K7B15oFzYsc6ni5Q+USB5Bx0vP29EapUzPsa3VecT44AxcvnZjBNTW7C2+FKrdF1PymVnGoRF+PLz4AZnv9Pa5QWETSkvmQG39SY29RZ5saRp/6a4kfZmAbh6h275XK24AhuttFeHbYdSFtjS1UFpYqw09pj6/3wi5QFEMGqh9qyfBGmD0umIq74SKuLkMnImd4uDTV6XzkFkQiKkmnQHKYwK3MWDvBEtH8pf3RyDxALCUSZh9ZTZOOTAVfbwLIJLPOQ5DhfjOqx3cmYAJlFFM7PDP/FPCJywwfmGN0vLXXAfM7i+jz3C10fe0dO3PwltvpKhIDtGpriFoLgtQ2ilXMf3RpwZ/xK/hIhqZvkSCkZfjVcTMl5kM8Scs7adguHaf92VW9Vl5PtckGmZYp44YlUPZzQh7hKbsQyzpFtMVPwCG0A4UmjTzW10UC75+juY82Csq/nnH8g4kTSolLDob9ZNDNfEcXEq4mjfPB57P+C0M8q5qdilQP+dTntBP62YBBkvtVoZDkxzwVHtwBdaUJKyDU59gdYjFRKNbJCLPnfaFKJ8Mo/oQuW7n1e9HZt5XA8zXCEtCt2Mww6jAQwQVQfCGhjDTf8C2eUqTNnVpqYcNSL9A1N5Mg7nT/ik9Hkn2mQyBd/YJLGGayun6ZTZ+nsvw5GduKfZAZPYOkgqXvD2LAqpg0Qac5qmdIRrBaILr1w2oJdtSQ3W08UgkW8BZwy7r7jwzMGt1l6SHxj/t9AKcbPGzuaAwAW2V7Oi5n3WDx4SMd/j7ou0Tp31CPrFvPQZ8Nalveu8Wpb+uSh35oD1BkfEaFmwKWxUAvNg7+//USWdvp7+eMvWxKWmskqGTgavTG8+Clcu12PdE6E4Np0MvW7x/jZLSVsucKfbEZcLmXCu7LdZSNGUjKUXsWFIDIFCEJkE+UAaDArZ6j/riCyaS3Uu3wzzGM9gSKkB31WG6LNNBM8i/1B+5C7tVb3HeLiHfXtcMOemPUYPbHG6LdqgOlAkHeKRKakw8meOHoiGZgU4RH6bXhFUugSzWjjLzH5/Fiza/rbODOgI4dwY9Td6lfXqvm+qC0dCCHhBsfVRLRPno9wlAGzRsR8pn0gixbOwrvAV6snXOpCTJbXCmmIIY8uDS0za+V/Pla29K1/j3/b0oDCH+Z8JCHXW5X1fkC842AQO9wCj/r+Q0EV6T/lf3oMPFX1vlvNFpN++EfFkcRwEy/rI4ob4r+Kvua+R5LykR1FNed8KzWpz6LoDi/kho5H7AR0FL3ExA9auYayejyRlx1IQ27bQB+ZBPGmkey8wX2NtlgTwOs6YhOPfJrrE5GpXi4jAumuUB0eqfg/r81kchOK/0UGvxksrB4ESiivRP/bdlAQ/+2jmbyFZL9JPbgAnA2V0UHuADQnR5e5OWbNedt5RE/pUiJBLkHTfawTXtHShmY9fgNbR8tgOB+AUO0K6j/791Nho+3jX+74ZWyO5HNj5JB6KH4/jTyYx5peGM3LpKaRRk9iZee/TVTOdFTCfY2hhC+dSK/VYDomI+0SgZkG/qpZSjEhSwrdJN0w+kaSQIOCm73L/mM2S5qAd82QX57p5rckT0e72EgfqKuGIZEkwpuphTvdohTCqc9U21e4KvBl3NeIO1mYsN3kjTd7mMTBqMsWtROkfAUbdIqJe2Sklvqu5RGr2H2WPzTqLeYru3jmzEZ0wDHtImi6iKmT6LhqLo+jNH4wgl5zuNqcHwc4609UuZZsne2RofS7ImX9PU9d5nKsPdCVqEWlIxWQgykdsJRSTAtKNX59I8+FdMnNghsEnMWJ3tFTmyv9CICk8/R6lrlImigiBi2OIxuAKTbUQGIlmh51S0A30Ev9Z9m13QUrJqAq3dijB7XntTsmVOckXUOkX4Un2WwVPUAi3JizM3hmd/ALoY33s505G3lvVB6O3NsKsqYOVT2xPMgnZurQu7LuSY7bGbarrwO04b1U8xU6BbivLcvl2syKg/uAZzhTLq+9eOpHmNMO23z0icqRD3GOQvj2eBZ1a3pjSePCUXCcyKzK7GjXoeg8Yd6WUCJkV2gutfgd84SXmomwcFFsSRC4LAtdvT1k8VK9a25PNMjjrH7EUmxffY56YZ8lCdj9XKL+HbBYUSuua1GTWoiGVoSq5A1wqhR3urNNMBdyXunEWmq8bJgP4fkeA1rVvf7bYkN3uM9Km5ngfWHQ4WDY2Ksm5oaJkb7NNVRnXBpuAm2G9ydktkwsZwsK2oZJUydxUrrUiZ3lBkdv47DzuAEHzRjHU1ncCwMB8BoMIzw1h1TztfOavLY4EfsLw5ce9MjZfRJ8/R8sGJQMsnuRbCqUxLiEOEAYLNc5oCCmI4Z2th4g1StVLjdlbjUteEudzcFA8m4LXReQ5BvmctXWo+nWAlU5zz4mDYDqFmOzpicXtVMrPQQTqjsu0yDzAxCVoxGs3zee+GTCH0bcD0zueDEIDwa5Yu4WyvsRRAmXXOs/IRXRNHWM8qcfE+vWt2FeTi1m+q0/cObgloQH99YDu8lVgfbfUZBK3lxmxtrln4BXr732Yj8+xX2cxalJv0NBibRheiEwv68UV5ltAtjcKp2gdJIR1uHPY4l8xyWKpm9NK40zr8pDn00EyTWDLvL+5TSbnIokRRG5gPfkCwvoRKl+XRnfSVeztSCfn6/9Ifxo+4v0vXrHB1Gj4aNcUHX6ctagN72gvPHO62n78iQ7mi03ifUBx9T+hg1bRM6Gn4mBOoTJkvRLobWyqy8Y1ObrjQZW9wjShS8tdDLsfztXGRc6u6PNr9S1v18ksDXkk996Qnv8IUb6ay0FDuBIoOpm5Q0pxVZsGgq+9XmHfWiM4hK9NV8sZFQgO36ugIqX38Toy+vBM7rqSoQX2czAgHgclUYNWYWvyYnPK2DvVjZoADwk7tnKq4bkgv7ArXEI15Qv8RUkOtRQ1Zx89g6wssLnKrkC1rh/J9BARQHWaYOr+NnAGa6LTDxBbBHV1WJN9v+g4DQPFwWoOuevBz856OrNLBN3Hi6Wq8qQ9JG+1MEQx6Z/Bo/fzxPSgENwEu8xf6dt8KR5zkFn3+hNB9z1z4T532GLSmE7MLTeazDdN6oQkkhkY3BWZ4OYB5zRH/GO1NcC0r1Z6idO5ii/8Ba8Gacz4zS6PiNE5D/zGpCeVvSd8rn1rn687ZGHKiXPiSyG80dzJQQRWMeXT+mlPAdCjH9glL6LwBUyzhybtcsbwZN1bjJrjn9qx5i8g7iCgiasyD+5CblMPfGQVR32/D20vGMpp0cduim4E2eQS8kCCGwmo5cfLIbbBWktmKUSHg6sf4Av9GA9mPgZiJNkwKl8BcBihVAoiZ6y1gv2wtgQkIBi04vJGeZif094necgxP9wavwOJFaieoYQBtniX8zSvD0unQHX4umu5maJCELQLywR84V1MtCp+D7XRxwAE/4504k6/x6s4JLZM2suqE79ts+jlo0mNjs04dxFk9y1KfMLfqyxdbgZ2jwVUqSu8tegSa1c/ht/KQ5WvR+880R0+eqoHBXbUKoZUb/hZ8DX4G3U6qlD/+DWVE3ii0FtLhExzvkz24hXTtQi+bEDLApi6XijNEzHWmyNRtQ4QVWMVaxt0VniK5XiOL9KSu9X6E3poPetHdfPLPv0z2qjz68aFDFSfQHRD+1n4MwYWfRdhgceNaE1kjrfFdPSfPmI+OyBU3FnRK55bSmmWAKLu30rpm4BzypQMfNgozNOEOmv55RJ35BLYWgOL3DeIGJbMncysDtx/tZVJ5d1x91q1QTw6khRgar2p1e04+OuEVgOrq5/hQ/420hSrni384APQmtmhNAtyD8JlnVuF8GZii9oTbMwJbjYGLoM98VZjtvFBZLsAS2pZ9guR3dWAdaM4ULlQ2ObZRQZKCfx6/xj1yKNAahqexl4J0AnMM4f6S62UI2zvrX6y3t+suYSsj564Qm1+jpDyi4jc3tZwi93Qo7k+VvxcKsOqeSiu5kh4v1d7Vdi1VoJMEzJP05CG1+7gdXuVqeJaJhBBtq9/KsozCPhRjRELva4V8jaORb+uDFwi80KjKr3Oopd89CUYu2BqjGQA613IRmZIEudPMBVlQReiCwJdXfveyGKnUBGcwIWuBfrBja5BFemHphxj80krq+unKdQJrnlAUsqCuhw0PXq+TTFjhWcvptfUJ4+wVGAq7PkdLO8inDectv/Q9hlQy4Xx2BfacFpBn4snKUdIMuzGXUk3bnWG72wgc+nX+EYka1NNQ8Psf+MmB1NNgUOqpjwMO9m/QNn1JKUt+zXm6fe6FPyqXr4lUkzw/5UdwNwSesRYeTcFxzdkaZuqnNtdJc0pqNiE5Dlu/tjsVMIaC43R6GHvKRMd7B2D9B48MHyrXUJ7eSzalmulsom7Yw/CbkCCGDypWY3eqAcZa8TYsj3TlpUceuyI3mgoWKOEQ+CCmkuBRCaZ4JQNiqiCc+JaL9w51MBPF/ZlalhUP70aweVcROC3WHezt4iZ+zMOUeMqqni8eS+/WSSEplvN02FnwB8+8kwYMWmc8odD3tYdF8qVmm0blkDOD9VVqtwgww90EcQbH1Nqxg0ZK2HKfY7C1drZcUpeUvm8W6cEL9VfF2btHBna8iD+Y8SwEkPfw537FXnb1c2woVakqtOeMxxOXUNdpk65+JCvLpVFNMFEMIzcKO4QjTlNFcr9q/Ia9QAEDT0Zd1L8rxlSC3BTAbGjCH7VIOTXFqpxm+wH39mGWxe76gz0SfN806+xyP7/mUHfWqiTQg+kE4nbx1aNUU8RTGhsk9jKnkbhZcnWSQ5j/QevKoDmEeWMHKvzNDA2I5noEu3cb2RXr3pt2C74gcKXsUhyxuu679LcQWEDQvL8KLF+49Quonridq2rg1rUxe7rlvgCliEIBwIqVw0RhVps157WBC8OMutxO+5gsXzHpOXKv/bB+35TsmoXgAmbLgmH5E70iqoMbSKuv7oVAi2L5jOVakduK7PJh1sPyrjtxi2UyPjo3DId7lOadS+1CfVnEgniiqIvYaJ9Tu4snGNeuXiIM+2S3zDiIsNlD2kQRZ8n6qVyiY0vGpYj102Cel5VZ7MzwWX9JiRbwGawOsCd6mdhqLoUdnpiybztfmQR8YVHWTjI4vgASuud6H3WNO6wRMBCY8fqAgdjeP4x7iqtMBMdEFOeSbjs0pNUK3CfJeYWQ9LRwFZhy0tjESf2uJMyMp4trPe8PRojzTZb/RM3u53QKh1HAF2DJR6yv0W7OzY4JuzbdjS2SQ/MaFDyfZqe23qzpx25v4tKiJUX9Fc3ztINcSKtZPC1CO7LJHks5qSrZ90G/Gk47WuiJppZrdrha4jiFRjXntXI5Po2PIpzRcu8PhF3Rg3fslhBqOhvqVmd7QFw7JI9w2ernC5J6sZTZ3gpYA+nWcr5X8DMZRFTn5rVHoPJdpt7kv33ZJJKkuUYqWwvkdBSBV+erXfSeS6WpIMbyFye7RZAj6e+v+ppz+H66HvcNVakc7cQReG81j3gzi5iCjPnWzczBrj4PSUKG6K82/Y1x6QNac2hFozkax7+8NvT9ZkVjolliKn3MAfF+0VahgJB0/UH4RPCgN9yMOjoKuOi3iDOpHKedkvdM/JbqMVs4+zPqYfi7uMSP3km5d2aPDaNQ4HNnCFs/DK+Nk3lpboeiECbHjUeI42fHm+U727BEM/OnMvWWtSXz4QMxsUb1EjUoCRpME7XqKDFNINi7ZmJKpZqgeKEQzEkmDN8BxXg+NINGkBASZoZ/7Scpwgm2Kv73kGhoBTdQkJbdynZ0WOQpRhpS6E+mapQd/dLTddy/SdgXVvtL8Ez8nIMKOJgxEHIVNszYab7eCSHkxW3YxGxcJMx8qIAuFGSq5my1fQN98vvusWsr2UVhLj1sNpjZiHvqhZLXm2DDBvVg1YRxO2AtrZhlgSEDY/4rJwt0KCkZ2dXgFaAfrDoXfEgOtNvOg2KcbvGQ4j0FZ6TUq2f0+IfPqsTZiIfk9PYRWYVYHz1B/3qYY6wWjRazcSvMLjYU4eGcf5F9tnJsOcdBAuBiEdyfVzENH2yvwsQarLF76oSWHmnqDGggClXlyBMV+YayJEbj+uIVNT4un5RIMhZ8iV6ITy3CO0yTq7Om3+RrWs7Wb/lPF0mdqlwu5sFkZ+kg9tv1MEDildyUgojoFaSkCIShPcxVSpkU2LhZXq5seBwoJkTVzJ7k21r5jVTWbQNif/0K/8kTYn8Hc3+Hli3Y4qQifLU9kB2lo5Cu/wV5bkCsgd0/bMho1/HlGZXDLuPizllHWpjxrQkPj3vU37BcuVYXAoVpFzkiOM4xxA3rpdf+gQrjqj6wRr7f6nOKwb/D/bub0/Hveb1PxuIQiRqeK0LuVjGukSW88Hk6L94m+KeHPqH7UqBY+crmnBldTeqOtFdbbp+bnrmABEKQ9Alwvu6GeROEGgALgPW3KVOWYzVd9b5Ko11sUAg3eI3hGDNyWf7Ug/R8yRpS54ketRmx7rGuNc5hxBr++oqxPxEb8A84YwlinTcAaWX3DwALJrLNEndKHcJDDseqbngFVSy9RvWXLz7XwOgxdCSSkcyZ4rEYt7LgwNl+tL+LEfC9NhxRjZHp1wgvZmZxOAZakmY/OfQaNiu1LRaXQMtiARinMInBhS0lRHDnghFqJ9Gk1a5tmB+D9Lfs2/B1r8gszE6rPAEcvRC0RRKL2MfRLgxmHKIFZlaasgtrwKrFBCOuUdWy0a99NuVrMXYzpiOtJQqDsDMJzwRej1GmCHmOQaxFuFds0boG3OnZrmifQRWvTPJMsEuzm5xSMMnDFVYH5s+8QVEFGiMK2Juc7Cw91hf8QPGIXHi/goYJr/8PjjfzDwTujtn0StGq96liEtir4CM7+YSXoHc+vuSBR5PrJpq3nrYVtZNdCedjblFr6WQrmGoubClguZ/GO4UDfGCiUscBT9Wupa8ZyrtjARZjiLyjF5M2BaqwTOFjFqVgl4NYzutR6c3P1lAP9efqz6swvBpCV+gOhMMNmiTW9qd0BbDIx+gXhouAxsHxBZEYBT76mToi5N51X6+yzlHwqAAv+oMxAdwIhw37iCUJ/dA6kj0NSbeGmCOFr+9rsZnW8krKjJvLNyRmYbel/3joSukyUaTScoNGOV87jpP+1KVUWvUjwSLlxEfdadjNP93gh6DR1wH03QHxztL4C01gn/OO9XAhsjAGEtJUM9Gx9i4HQR0Tc8QSFey2Sox8tI5rlgjv3yQ9H63OlFulBHzpSPinXv+yeMztPesEi/mJw56XRak7k2C0bs+iQvds8FebUmxYsvZMYAoy+bM7KFC3lz421ZY9S9izfV7tu4LTAZgqOX2c+bFwdqGH2oIW8LRVZ4cIsK8gCVA1C7sW3fCd8pm9RyA5h193RGzEsEt948gSw6QTRzuruuMKTAEQl0FbrsuBqiVU+sWSoS8iSA8guvdnttYdwvs3qJ8bRiN7VJZRZ3hOsVA7TdEsltI6LC7Pt27z3DCvtlsPnBzEzgepwrPuy6cX4hXzz1t5KUdpMvSN4z3Go7rqP4zR9hM7DURRVla3e/11WYOZJE2rlgJUx7+y1nC4gARFZCDkEyNusE0RjoOgNUubk2plDTZL1ENpEO/AuwbRPJwS9fEjH8a6ipneBNyyK/cB3ZX2LTWchVYB0vDlMRMlHhC2rSjL2qigsalI2PD3MJY2bH1d2xDODi1RMv2lQ/7BfDG2N83ktEKsIkca7ShaxLhGZyj1u3lwSjer68Whx7hVZHnse/f6ACuMe/ai3wXgjwSlKXfjxaf1Ou1Dsx+YACSLaQO3CFL5T2y4c73wfrT/fAsxPPLPK5nISGrRDsSZK3fvvPxgddclWZNadm2QCQWyBAcdeoVY/bD7GJUkX4hzvlUgWj0+QsfMVaemgmut2r+NZpshY9b9U5efXp3JtK6nHzy0fmojfe8yUdvQRlg0rd90e6PuUWOkZh9JKYDhq/X8pvYRTBZB4b2HxXznk1R1KnZ/NE+Gc3lNqkSl+o6y6diXHmyr9s37VQcd4Gvrr7YdDEM9idXn+Tmo7meo3pwVOwr+h3mGp7p/CbeY66AMJtHrV6KiWh+VM3D99JvoJgnwuzmjHab2DcW4H4VvnwD9IZ/EeAihprwUzbpOmDlP9QqjUvihiZJuukAEHtlJ0VJAlRyBYz6Xdnvjx3iNkfmPUEJS+MouEA7wtUL26+q3tJW4i0GzW94gH8QkEr6e0F2niRb75NOEUo7cDJv5HtJEkxyaqxrH8YQqvdh/vaLzeI+EfA4w64lILs2KlVdn2zP7BaiFH/ju0tDliwex05rvAAZNbd0QofDGoRMbJRB5+rsrbb1c8hg6Z7B9ICOGDZ83vwFPI8UKSIj2mdFf1Y2ZoE19M7l3UG2Qrh4AtACL5qepz64mqIOo31G6/w9QCAUU9FtUyH9lZMEBKmvT0aS6eRDzB4R7FnjzkMdj3b56jQxnnRTQWPHKhn1O4sn+RxTIC0e98vRDHCZIuHi8nB1qAuVe1AGFd9lD6U=
        - #1:
          - type: tool-result
          - toolCallId: PzISuoqyrcCEdOqM
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: NDdsgatgZiZvABb0
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: yFFeCBQoBuuMmzc6
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: kkn6eogNDlvxzanG
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: Ja1Df87zvnUqFM7i
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: ijNXLZnpkALSarID
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.