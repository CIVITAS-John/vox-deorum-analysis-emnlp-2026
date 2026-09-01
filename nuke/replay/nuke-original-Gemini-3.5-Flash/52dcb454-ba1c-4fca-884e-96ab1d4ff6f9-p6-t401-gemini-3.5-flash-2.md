- row:
  - game_id: 52dcb454-ba1c-4fca-884e-96ab1d4ff6f9
  - player_id: 6
  - turn: 401
  - player_type: Deepseek-3.2-Simple
  - prev_use_nuke: 30.0
  - after_use_nuke: 100.0
  - prev_nuke: 50.0
  - after_nuke: 100.0
  - rationale: Maximize nuclear weapon production and willingness to use them to break enemy defenses and accelerate domination victory. All other military flavors remain high to sustain multi-front warfare.
- originalModel: openai-compatible/DeepSeek-V3.2@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: false
  - messagesModified: false
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 100
  - replay_use_nuke: 100
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
      - Cities: summary reports about discovered cities in the world.
        - Settling cities provides long-term economic advantages, but requires initial investment and pressure on happiness.
      - Military: summary reports about tactical zones and visible units.
        - Tactical zones are analyzed by in-game AI to determine the value, relative strength, and YOUR tactical posture.
        - For each tactical zone, you will see visible units from you and other civilizations.
      - Events: events since the last decision-making.
    - You are Alexander, leader of Greece (Player 6).
      
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
      - Name: Greece
      - Uniques:
        - Unique Unit: Hoplite, Replacing Spearman (Requires technology: Bronze Working)
        - Unique Unit: Klepht, Replacing Commando (Requires technology: Railroad)
        - Unique Building: Gymnasion, Replacing Amphitheater (Requires technology: Drama and Poetry)
        - Unique Building: Parthenon, Replacing Scrivener's Office (Requires technology: Writing)
        - Civilization Ability:  Influence degrades at half and recovers at twice the normal rate. +5% Combat Strength of owned and Allied Units for each City-State alliance (up to +25%). Treat neutral City-State territory as friendly territory.
      - Leader: Alexander
      - PlayerID: 6
      
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
      - Refrigeration: Allows Work Boats to construct an Offshore Platform, and increases Trade Route maximum travel distance.
        Completing it would unlock: Electronics, Computers
      - Nuclear Fission: Allows you to build the Bazooka, the most powerful ranged Unit and Atomic Bombs, the first nuclear weapon in the game (note: you must first have completed the Manhattan Project and have Uranium available). Also allows you to build the Nuclear Plant, a building which requires Uranium and increases the Production of a City.
        Completing it would unlock: Satellites, Advanced Ballistics
      - Penicillin: All Workers receive the Fallout Reduction Promotion, which reduces the amount of damage they take while scrubbing Fallout. Allows you to build the Marine, a Unit that specializes in amphibious assaults. Also allows you to build the Medical Lab, a building which speeds the growth of your Cities.
        Completing it would unlock: Electronics
      - Mobile Tactics: Allows you to build the Mechanized Infantry, a fast and versatile late game Unit that doesn't require any resources.
        Completing it would unlock: Stealth
      
      ## Policies
      - Spaceflight Pioneers (Level 3 Tenet of Ideology Order): Spaceflight Pioneers: Gain a free Great Engineer and Great Scientist. May finish Spaceship parts with Great Engineers, and expending a Great Person grants 100 Science, scaling with Era. Hurrying Production with Great Engineers 50% more effective.
      - Socialist Realism (Level 3 Tenet of Ideology Order): Socialist Realism: Unlocks the Propaganda Process (converts 15% of Production into Tourism). +25% Tourism to other Civilizations following Order. +4 Production from all Great Works.
      - Iron Curtain (Level 3 Tenet of Ideology Order): Iron Curtain: Free Courthouse upon immediate City annexation. +200% Food or Production from Internal Trade Routes. City connections generate +5 Gold and Production.
      - Peace, Land, Bread (Level 1 Tenet of Ideology Order): Peace, Land, Bread: -2 Unhappiness from Poverty and Growth increased by 20% in all Cities. Building maintenance reduced by 20%.
      - Communism (Level 1 Tenet of Ideology Order): Communism: Gold cost of investing in buildings reduced by 25%. +20% Production when building Wonders.
      - People's Army (Level 1 Tenet of Ideology Order): People's Army: +100% Production towards Military Academies, and receive 5 Free Military Academies in your Empire. Public Schools produce +5 Culture and +2 Happiness.
      - Hero of the People (Level 1 Tenet of Ideology Order): Hero of the People: Great Person rate increases by 25%. A Great Person of your choice appears near your Capital.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Equality (Continuing Progress Branch):
        - * +1 Happiness in every City and +1 Happiness for every 15 Citizens in a City.
        - * -1 Unhappiness from and Distress, Poverty, Illiteracy, and Boredom in all Cities.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Organization (Continuing Progress Branch):
        - * +2 Production in every City.
        - * +25% Production toward Workers and Trade Units.
        - * +1 Movement for Workers.
      - Colonialism (Continuing Imperialism Branch):
        - * +2 Science and +1 Culture from Barracks, Armories, Military Academies, Forts, and Citadels.
        - * Each unique Global Monopoly modifier is increased by an additional 10% if it's percentage-based, or +3 otherwise.
      - Regimental System (Continuing Imperialism Branch):
        - * Earn Great Generals and Great Admirals 33% faster.
        - * Great Generals and Great Admirals gain the Regimental Traditions Promotion (+10% Leadership Combat Bonus and +1 Tile Radius).
        - * +2 additional copies of the unique Luxury Resources from expending Great Admirals for their Voyage of Discovery ability.
        - * Military Units can be upgraded in territory owned by Vassals and friendly City-States.
      - Civilizing Mission (Continuing Imperialism Branch):
        - * Retain all buildings from conquered Cities.
        - * Receive 75 Gold when you conquer a city, scaling with Era and City Population.
        - * +10% Production toward Buildings, with an additional +10% Production per Era difference between your current Era and the building's Era in all Puppeted Cities and Cities with a Courthouse.
      - Fraternity (Continuing Progress Branch):
        - * +3 Food in every City.
        - * +3 Science from City Connections.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Fealty (New Branch):
        - Fealty enhances your ability to defend and leverage your Majority Religion.
        - Adopting Fealty grants:
        - * Can purchase Monasteries with Faith (+3 Food, +3 Science, +2 Faith).
        - * -25% Faith costs for purchasing Buildings, Missionaries, and Inquisitors.
        - Each Fealty policy unlocked grants:
        - * +1 Faith and Strength in every City.
        - Adopting all Policies in Fealty grants:
        - * Unlocks building the Red Fort.
        - * Your Tourism modifier for Shared Religion is 50% stronger.
        - * Cities that follow your Majority Religion generate +3 Production, Gold, Science, and Culture.
        - * Allows for the purchase of Great Artists with Faith starting in the Industrial Era.
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
        - VictoryCompetitiveness: 10
        - WonderCompetitiveness: 1
        - MinorCivCompetitiveness: 10
        - Boldness: 10
        - WarBias: 10
        - HostileBias: 10
        - WarmongerHate: 1
        - NeutralBias: 1
        - FriendlyBias: 1
        - GuardedBias: 5
        - AfraidBias: 1
        - DiplomaticBalance: 9
        - Friendliness: 1
        - WorkWithWillingness: 10
        - WorkAgainstWillingness: 10
        - Loyalty: 10
        - MinorCivFriendlyBias: 10
        - MinorCivNeutralBias: 1
        - MinorCivHostileBias: 5
        - MinorCivWarBias: 1
        - DenounceWillingness: 10
        - Forgiveness: 1
        - Meanness: 10
        - Neediness: 1
        - Chattiness: 3
        - DeceptiveBias: 5
        - Rationale: Maintain maximum aggression towards Ethiopia (cultural victory imminent) and Songhai (near elimination). High city-state competitiveness secures diplomatic backup. High loyalty ensures vassal stability. No changes needed.
        
        ## Technology
        - Next: None
        
        ## Policy
        - Next: Spaceflight Pioneers (Policy)
        - Rationale: Iron Curtain will be adopted next turn. After that, Spaceflight Pioneers (Order Level 3) provides a free Great Engineer and Great Scientist, boosts science, and allows Great Engineers to finish spaceship parts. This synergizes with our high science output, preparing for either science victory backup or using Engineers to hurry critical military projects.
        
        ## Relationships
        
        ### Carthage
        - Public: 0
        - Private: 0
        - Rationale: Carthage is our vassal and effectively neutralized. Reset to neutral baseline since war is won (Gades remains but poses no threat). This prevents unnecessary diplomatic penalties and allows peaceful relations with our subjugated opponent.
        - UpdatedTurn: 267
        
        ### Babylon
        - Public: 0
        - Private: 0
        - Rationale: Babylon is our vassal and no longer a military threat. Resetting relationship modifiers to neutral ensures our AI treats them appropriately as a subjugated ally, preventing unnecessary diplomatic friction and allowing peaceful management of the vassal relationship.
        - UpdatedTurn: 329
        
        ### Songhai
        - Public: -100
        - Private: -100
        - Rationale: Songhai is at 100% war score; we must continue capturing their remaining cities (Gao, Taghaza, etc.) to eliminate them for domination victory. Lock in maximum hostility to prevent any peace and ensure total conquest.
        - UpdatedTurn: 375
        
        ### Japan
        - Public: -100
        - Private: -100
        - Rationale: Japan is allied with Ethiopia and has defensive pacts with Mongolia and Ottomans. They may join the war against us. Maximum hostility prepares our AI for potential conflict and ensures no friendly diplomatic actions.
        - UpdatedTurn: 375
        
        ### Mongolia
        - Public: -100
        - Private: -100
        - Rationale: Mongolia is allied with Ethiopia and has defensive pacts with Japan and Ottomans. They remain a military threat. Maximum hostility ensures our AI treats them as an enemy and prepares for possible war.
        - UpdatedTurn: 375
        
        ### The Ottomans
        - Public: -100
        - Private: -100
        - Rationale: The Ottomans have defensive pacts with Japan and Mongolia and are allied with Ethiopia. They are likely to join any conflict. Maximum hostility ensures our AI is ready for naval and land defenses and treats them as an immediate threat.
        - UpdatedTurn: 375
        
        ### Ethiopia
        - Public: -100
        - Private: -100
        - Rationale: Ethiopia has achieved a cultural victory condition (7/7 influential). Our only path to prevent their ultimate victory is total conquest. Maximum hostility ensures no peace deals are considered and our AI relentlessly attacks Ethiopian cities until they are eliminated. We must capture Harar, Gondar, Axum, and their capital Addis Ababa to destroy their tourism base.
        - UpdatedTurn: 390
        
        ## Strategy
        - Rationale: Plastics completes in 1 turn, then Atomic Theory unlocks nuclear weapons. Increasing Nuke and UseNuke flavors prepares the AI to prioritize Manhattan Project and nuclear arsenal for rapid city capture against heavily defended Ethiopian and Songhai cities, and for deterrence against the Mongolia-Japan-Ottomans bloc. All other military flavors remain maxed to sustain multi-front war pressure.
        - GrandStrategy: Conquest
        
        ### Flavors
        - Offense: 100
        - Defense: 100
        - Mobilization: 90
        - CityDefense: 100
        - MilitaryTraining: 100
        - Recon: 50
        - Ranged: 100
        - Mobile: 100
        - Nuke: 50
        - UseNuke: 30
        - Naval: 100
        - NavalRecon: 80
        - NavalGrowth: 0
        - NavalTileImprovement: 0
        - Air: 100
        - AirCarrier: 80
        - Antiair: 100
        - Airlift: 90
        - Expansion: 0
        - Growth: 70
        - TileImprovement: 60
        - Infrastructure: 100
        - Production: 100
        - WaterConnection: 50
        - Gold: 100
        - Science: 100
        - Culture: 50
        - Happiness: 100
        - GreatPeople: 75
        - Wonder: 0
        - Religion: 0
        - Diplomacy: 85
        - Spaceship: 50
        - Espionage: 100
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: Greece
        - Greece:
          - CapitalsControlled:
            - Gao
            - Babylon
            - Carthage
            - Athens
          - CapitalsPercentage: 50
        
        ## ScienceVictory
        - Unlocked in the Information era
        
        ## CulturalVictory
        - CivsNeeded: 7
        - Contender: Ethiopia
        - Babylon:
          - Influences:
            - Mongolia: Exotic (21%) - Rising Slowly (tourism/culture ratio 31%)
            - Greece: Exotic (13%) - Rising Slowly (tourism/culture ratio 33%)
            - Songhai: Exotic (19%) - Rising Slowly (tourism/culture ratio 55%)
            - Carthage: Familiar (34%) - Rising Slowly (tourism/culture ratio 61%)
            - Ethiopia: Exotic (10%) - Rising Slowly (tourism/culture ratio 21%)
            - Japan: Familiar (25%) - Rising Slowly (tourism/culture ratio 46%)
            - The Ottomans: Familiar (33%) - Rising Slowly (tourism/culture ratio 99%)
          - PolicyPercentage: 88
          - InfluentialCivs: 0
        - Carthage:
          - Influences:
            - Mongolia: Exotic (6%) - Rising Slowly (tourism/culture ratio 14%)
            - Songhai: Exotic (5%) - Rising Slowly (tourism/culture ratio 20%)
            - Greece: Exotic (6%) - Rising Slowly (tourism/culture ratio 14%)
            - Babylon: Exotic (9%) - Rising Slowly (tourism/culture ratio 30%)
            - Japan: Exotic (6%) - Rising Slowly (tourism/culture ratio 18%)
            - The Ottomans: Exotic (9%) - Rising Slowly (tourism/culture ratio 35%)
          - PolicyPercentage: 77
          - InfluentialCivs: 0
        - Ethiopia:
          - Influences:
            - Mongolia: Influential (103%) - Rising (tourism/culture ratio 120%)
            - Greece: Influential (102%) - Rising (tourism/culture ratio 132%)
            - Songhai: Influential (102%) - Rising (tourism/culture ratio 185%)
            - Carthage: Dominant (256%) - Rising (tourism/culture ratio 285%)
            - Babylon: Influential (113%) - Rising (tourism/culture ratio 207%)
            - Japan: Influential (117%) - Rising (tourism/culture ratio 155%)
            - The Ottomans: Influential (132%) - Rising (tourism/culture ratio 336%)
          - PolicyPercentage: 100
          - InfluentialCivs: 7
        - Greece:
          - Influences:
            - Mongolia: Familiar (39%) - Rising Slowly (tourism/culture ratio 52%)
            - Babylon: Popular (93%) - Rising (6 turns to Influential, tourism/culture ratio 368%)
            - Songhai: Familiar (35%) - Rising Slowly (tourism/culture ratio 78%)
            - Carthage: Influential (196%) - Rising (tourism/culture ratio 370%)
            - Ethiopia: Familiar (38%) - Rising Slowly (tourism/culture ratio 62%)
            - Japan: Familiar (42%) - Rising Slowly (tourism/culture ratio 74%)
            - The Ottomans: Familiar (47%) - Rising Slowly (tourism/culture ratio 145%)
          - PolicyPercentage: 100
          - InfluentialCivs: 1
        - Japan:
          - Influences:
            - Mongolia: Popular (62%) - Rising (138 turns to Influential, tourism/culture ratio 152%)
            - Greece: Exotic (20%) - Rising Slowly (tourism/culture ratio 55%)
            - Songhai: Familiar (30%) - Rising Slowly (tourism/culture ratio 122%)
            - Carthage: Popular (76%) - Rising (59 turns to Influential, tourism/culture ratio 168%)
            - Ethiopia: Exotic (19%) - Rising Slowly (tourism/culture ratio 46%)
            - The Ottomans: Popular (56%) - Rising (108 turns to Influential, tourism/culture ratio 264%)
            - Babylon: Familiar (41%) - Rising (952 turns to Influential, tourism/culture ratio 139%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Mongolia:
          - Influences:
            - Babylon: Popular (55%) - Rising (70 turns to Influential, tourism/culture ratio 271%)
            - Greece: Familiar (29%) - Rising Slowly (tourism/culture ratio 104%)
            - Songhai: Familiar (39%) - Rising (144 turns to Influential, tourism/culture ratio 223%)
            - Carthage: Influential (109%) - Rising (tourism/culture ratio 314%)
            - Ethiopia: Familiar (27%) - Rising Slowly (tourism/culture ratio 99%)
            - Japan: Popular (95%) - Rising (4 turns to Influential, tourism/culture ratio 382%)
            - The Ottomans: Popular (78%) - Rising (16 turns to Influential, tourism/culture ratio 513%)
          - PolicyPercentage: 100
          - InfluentialCivs: 1
        - Songhai:
          - Influences:
            - Mongolia: Familiar (32%) - Rising Slowly (tourism/culture ratio 63%)
            - Greece: Exotic (21%) - Rising Slowly (tourism/culture ratio 48%)
            - Babylon: Popular (55%) - Rising (312 turns to Influential, tourism/culture ratio 158%)
            - Carthage: Familiar (45%) - Rising Slowly (tourism/culture ratio 96%)
            - Ethiopia: Exotic (19%) - Rising Slowly (tourism/culture ratio 35%)
            - Japan: Familiar (36%) - Rising Slowly (tourism/culture ratio 89%)
            - The Ottomans: Popular (54%) - Rising (291 turns to Influential, tourism/culture ratio 201%)
          - PolicyPercentage: 96
          - InfluentialCivs: 0
        - The Ottomans:
          - Influences:
            - Mongolia: Exotic (23%) - Rising Slowly (tourism/culture ratio 54%)
            - Greece: Exotic (10%) - Rising Slowly (tourism/culture ratio 27%)
            - Songhai: Exotic (17%) - Rising Slowly (tourism/culture ratio 65%)
            - Carthage: Familiar (34%) - Rising Slowly (tourism/culture ratio 72%)
            - Ethiopia: Exotic (11%) - Rising Slowly (tourism/culture ratio 32%)
            - Japan: Familiar (30%) - Rising Slowly (tourism/culture ratio 82%)
            - Babylon: Familiar (27%) - Rising Slowly (tourism/culture ratio 72%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        
        ## DiplomaticVictory
        - VotesNeeded: 45
        - Status: World Congress - Voting in 3 turns
        - ActiveResolutions:
          - Casus Belli:
            - Description: The world recognizes the need for justifiable war to resolve diplomatic disputes.
              While this resolution is active, unit maintenance costs are lowered by 15% Gold. 0.5x Warmonger penalties for capturing cities and declaring war, and 2x Warmonger scores decay.
            - EnactedOn: 330
          - Sanction: Greece:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: 393
          - Greek Sphere of Influence: Copenhagen:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 393
          - Cultural Heritage Sites:
            - Description: Each World Wonder provides +2 Culture to its city, and each Great Work provides +1 Science to its city.
            - EnactedOn: 330
          - Greek Sphere of Influence: Monaco:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 360
          - Open Door: Budapest:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 330
          - Mongolian Sphere of Influence: Buenos Aires:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 382
          - Greek Sphere of Influence: Antananarivo:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 382
          - Ottoman Sphere of Influence: Salem:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 393
          - Open Door: Abernethy:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 330
          - Mongolian Sphere of Influence: Hanoi:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 349
          - Ethiopian Sphere of Influence: Vatican City:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 349
          - Open Door: Almaty:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 330
          - World Religion: Eastern Orthodoxy:
            - Description: Designate a religion as the official World Religion. Civilizations who have a majority of the cities in their empire following the religion get an additional Delegate. The founder of the religion and/or the controller of its Holy City receives additional votes based on the number of Civilizations following the religion. The religion spreads 25% faster, and its Holy City receives +50% Tourism. There can only be one World Religion at a time.
            - EnactedOn: 330
          - Mongolian Sphere of Influence: Antwerp:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 360
          - Sanction: Babylon:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: 330
        - Proposals:
          - Enact: United Nations:
            - Description: Begins the United Nations project. Once underway, Civilizations can contribute Production towards its completion by selecting it in the city production list. When complete, Civilizations receive bonuses based on how much they contributed.
              : United Nations wonder appears in Capital. (Receive 1 Additional Delegate in the World Congress for every 8 City-States originally in the World. Also, when you expend a Great Person, earn 25 Influence with all City-States you have met. Triggers a Golden Age, as well as the United Nations Special Session of the World Congress if the world has reached the Atomic Era.)
              : Receive an immediate boost of 25 Influence with all City-States. The Consulate National Wonder appears in Capital. (Receive 1 Additional Delegate in the World Congress for every 8 City-States originally in the World.)
              : Receive a free Great Diplomat.
              Available once any Civilization discovers Atomic Theory.
            - Proposer: Greece
          - Enact: Decolonization:
            - Description: Enforce global decolonization. If successful, the Influence of all Players with all City-States is lowered to 50, unless they are permanent allies.
              Available once any Civilization discovers Radio.
            - Proposer: Mongolia
          - Enact: Passport System:
            - Description: Increases international travel between Civilizations. Increases the Tourism modifier for all Civilizations by 50%.
              Available once any Civilization discovers Flight.
            - Proposer: Ethiopia
        - Contender: Greece
        - Babylon:
          - Delegates: 5
          - VictoryPercentage: 11
        - Carthage:
          - Delegates: 3
          - VictoryPercentage: 6
        - Ethiopia:
          - Delegates: 9
          - VictoryPercentage: 20
        - Greece:
          - Delegates: 21
          - VictoryPercentage: 46
        - Japan:
          - Delegates: 6
          - VictoryPercentage: 13
        - Mongolia:
          - Delegates: 12
          - VictoryPercentage: 26
        - Songhai:
          - Delegates: 5
          - VictoryPercentage: 11
        - The Ottomans:
          - Delegates: 7
          - VictoryPercentage: 15
        
        # Players
        Players: summary reports about visible players in the world.
        
        ## Player 0
        - Civilization: Songhai
        - Leader: Askia
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Songhai) have denounced one of Greece's declared enemies! (11)
          - Greece's real approach to Songhai is War.
          - We have divergent Social Policies. (-3)
          - You (Songhai) have denounced a leader Greece made a Declaration of Friendship with! (-11)
          - You (Songhai) have made a Declaration of Friendship with one of Greece's enemies! (-13)
          - Religious differences strain your (Songhai) relationship. (-30)
          - Your (Songhai) spies were caught stealing from Greece. (-33)
          - You (Songhai) stole Greece's territory! (-50)
          - Greece's leader has expressed a public opinion of Songhai (-100).
          - Greece's leader has formed a private opinion of Songhai (-100).
          - You (Songhai) have chosen to adopt the Freedom Ideology, but Greece believe in Order. (-999)
          - You (Songhai) are at war! (-99999)
        - TheirOpinionOfUs:
          - You (Greece) have denounced one of Songhai's declared enemies!
          - We are completely untrustworthy to Songhai.
          - Songhai fear your (Greece) warmongering will end this world in fire! (They strongly dislike warmongers.)
          - Religious differences strain your (Greece) relationship.
          - We have divergent Social Policies.
          - Your (Greece) spies were caught stealing from Songhai.
          - You (Greece) killed or captured Songhai's civilians!
          - You (Greece) have made a Declaration of Friendship with one of Songhai's enemies!
          - You (Greece) have denounced a leader Songhai made a Declaration of Friendship with!
          - Songhai's friends or allies have denounced you (Greece)!
          - Songhai disliked our proposal to the World Congress.
          - Songhai fear your (Greece) acquisition of multiple vassals!
          - Territorial disputes strain your (Greece) relationship.
          - We have denounced Songhai!
          - Your (Greece) votes opposed Songhai's civ's interests in the World Congress.
          - You (Greece) have chosen to adopt the Order Ideology, but Songhai believe in Freedom.
          - You (Greece) captured Songhai's original capital.
          - You (Greece) are at war!
        - Score: 1470
        - Era: Atomic
        - Technologies: 59
        - Cities: 6
        - Population: 130
        - Territory: 154
        - Gold: 306
        - GoldPerTurn: 43
        - HappinessSituation: Happy
        - HappinessPercentage: 61
        - MilitaryStrength: 1298
        - TourismPerTurn: 310.5
        - CulturePerTurn: 690
        - PolicyBranches:
          - Fealty: 6
          - Freedom: 4
          - Imperialism: 6
          - Authority: 6
        - ResourcesAvailable:
          - Wheat: 3
          - Sheep: 1
          - Cloves: 3
          - Gold: 1
          - Pearls: 2
          - Paper: 4
          - Cotton: 2
          - Brazilwood: 2
          - Aluminum: 4
          - Lapis Lazuli: -2
          - Deer: 1
          - Perfume: 3
          - Olives: 1
          - Iron: 4
          - Cattle: 1
          - Marble: 1
          - Horses: -6
          - Fish: 2
          - Bison: 3
          - Copper: 2
          - Truffles: 1
          - Stone: 3
          - Cocoa: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Mongolia:
            - Distance: Far
            - Open Borders
          - Greece:
            - Distance: Neighbors
            - War (Our Score: -100%; Our War Weariness: 100%)
          - Babylon:
            - Distance: Neighbors
            - War (Our Score: 16%; Our War Weariness: 100%)
            - Denounced Them
          - Carthage:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 84%)
            - Denounced Them
          - Ethiopia:
            - Distance: Far
            - Denounced Them
          - Japan:
            - Distance: Close
            - Open Borders
            - Declaration of Friendship
          - The Ottomans:
            - Distance: Neighbors
            - War (Our Score: -48%; Our War Weariness: 89%)
        - Votes: 5
        
        ## Player 1
        - Civilization: Babylon
        - Leader: Nebuchadnezzar II
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Babylon) have both adopted the Order Ideology. (999)
          - You (Babylon) are Greece's vassal state, and Greece like it! (99)
          - We are trade partners. (40)
          - We passed Greece's proposal in the World Congress. (36)
          - We have opened our borders to each other. (12)
          - You (Babylon) have denounced one of Greece's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - We have shared embassies. (1)
          - Greece's real approach to Babylon is Friendly.
          - We have divergent Social Policies. (-3)
          - Religious differences strain your (Babylon) relationship. (-30)
          - Your (Babylon) spies were caught stealing from Greece. (-33)
        - TheirOpinionOfUs:
          - Babylon are content with your (Greece) treatment of Babylon as Babylon's master.
          - We are trade partners.
          - You (Greece) have denounced one of Babylon's declared enemies!
          - You (Greece) have both adopted the Order Ideology.
          - We have made a public Declaration of Friendship!
          - You (Greece) protected Babylon's territory as their master!
          - We have a Diplomat in Babylon's capital.
          - You (Greece) are not competing for technological advancement.
          - We have made Declarations of Friendship with the same leaders!
          - Your (Greece) recent diplomatic actions please Babylon.
          - We have opened our borders to each other.
          - We have Pledged to Protect the same City-States.
          - You (Greece) have no contested borders.
          - We have shared embassies.
          - Your (Greece) military deployment is extremely threatening.
          - We have divergent Social Policies.
          - We have different religious beliefs.
          - Babylon are our vassal state.
          - Babylon desire friendly relations with Greece.
          - Babylon disliked our proposal to the World Congress.
        - Score: 1255
        - Era: Atomic
        - Technologies: 58
        - Cities: 4
        - Population: 84
        - Territory: 130
        - Gold: 330
        - GoldPerTurn: 115
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 1475
        - TourismPerTurn: 158.25
        - CulturePerTurn: 489
        - PolicyBranches:
          - Order: 2
          - Rationalism: 6
          - Tradition: 6
          - Artistry: 6
        - ResourcesAvailable:
          - Ivory: 1
          - Paper: 6
          - Maize: 1
          - Aluminum: 11
          - Lapis Lazuli: 2
          - Fish: 10
          - Deer: 3
          - Sugar: 1
          - Iron: 3
          - Coal: 2
          - Coffee: 2
          - Cattle: 1
          - Marble: 1
          - Horses: 2
          - Bison: 2
          - Truffles: 2
          - Stone: 3
          - Furs: 1
          - Cocoa: 2
        - FoundedReligion: Catholicism
        - Relationships:
          - Mongolia:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
          - Greece:
            - Distance: Neighbors
            - Our Master (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Songhai:
            - Distance: Neighbors
            - War (Our Score: -16%; Our War Weariness: 85%)
            - Denounced Them
          - Carthage:
            - Distance: Far
            - Declaration of Friendship
          - Ethiopia:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
          - Japan:
            - Distance: Far
          - The Ottomans:
            - Distance: Neighbors
            - Denounced Them
        - Votes: 5
        
        ## Player 2
        - Civilization: The Ottomans
        - Leader: Suleiman
        - IsMajor: true
        - OurOpinionOfThem:
          - We fought together against a common foe. (28)
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - You (The Ottomans) have gone to war in the past.
          - Greece's real approach to The Ottomans is Hostile.
          - You (The Ottomans) have denounced a leader Greece made a Declaration of Friendship with! (-11)
          - You (The Ottomans) have made a Declaration of Friendship with one of Greece's enemies! (-13)
          - You (The Ottomans) have made a Defensive Pact with one of Greece's enemies! (-15)
          - We defeated Greece's proposal in the World Congress. (-36)
          - Greece's leader has expressed a public opinion of The Ottomans (-100).
          - Greece's leader has formed a private opinion of The Ottomans (-100).
          - You (The Ottomans) have chosen to adopt the Freedom Ideology, but Greece believe in Order. (-999)
        - TheirOpinionOfUs:
          - We fought together against a common foe.
          - You (Greece) are not competing for technological advancement.
          - We have similar Social Policies.
          - We are trade partners.
          - You (Greece) have denounced one of The Ottomans's declared enemies!
          - We have Pledged to Protect the same City-States.
          - The Ottomans's leader has expressed a public opinion of you (Greece) (5).
          - You (Greece) have no contested borders.
          - You (Greece) have gone to war in the past.
          - The Ottomans fear your (Greece) warmongering will end this world in fire! (They dislike warmongers.)
          - The Ottomans don't want anything to do with us (Greece) right now.
          - You (Greece) are competing for World Wonders.
          - Your (Greece) recent diplomatic actions disappoint The Ottomans.
          - The Ottomans believe we are building World Wonders too aggressively!
          - Your (Greece) spies were caught stealing from The Ottomans.
          - You (Greece) are competing for the favor of the same City-States!
          - The Ottomans disliked our proposal to the World Congress.
          - The Ottomans's friends or allies have denounced you (Greece)!
          - You (Greece) have made a Declaration of Friendship with one of The Ottomans's enemies!
          - The Ottomans believe we are expanding Greece too aggressively!
          - The Ottomans fear your (Greece) acquisition of multiple vassals!
          - Your (Greece) votes opposed The Ottomans's civ's interests in the World Congress.
          - We defeated The Ottomans's proposal in the World Congress.
          - You (Greece) have denounced a leader The Ottomans made a Declaration of Friendship with!
          - You (Greece) have chosen to adopt the Order Ideology, but The Ottomans believe in Freedom.
        - Score: 2131
        - Era: Atomic
        - Technologies: 66
        - Cities: 8
        - Population: 202
        - Territory: 277
        - Gold: 350
        - GoldPerTurn: 10
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 48
        - MilitaryStrength: 13286
        - TourismPerTurn: 231.25
        - CulturePerTurn: 535
        - PolicyBranches:
          - Freedom: 4
          - Tradition: 3
          - Rationalism: 2
          - Statecraft: 3
          - Imperialism: 2
          - Progress: 6
          - Industry: 1
        - ResourcesAvailable:
          - Sheep: 2
          - Ivory: 1
          - Gold: 1
          - Paper: 6
          - Pearls: 1
          - Rice: 3
          - Salt: 1
          - Aluminum: 5
          - Lapis Lazuli: 1
          - Fish: 9
          - Deer: 2
          - Whales: 7
          - Olives: 1
          - Coal: 6
          - Cattle: 4
          - Uranium: 3
          - Horses: 8
          - Bison: 1
          - Truffles: 2
          - Stone: 1
          - Marble: 1
          - Cinnamon: 1
          - Bananas: 1
          - Wine: 1
          - Cocoa: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Mongolia:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Greece:
            - Distance: Close
          - Songhai:
            - Distance: Neighbors
            - War (Our Score: 48%; Our War Weariness: 69%)
          - Carthage:
            - Distance: Distant
            - Denounced Them
          - Ethiopia:
            - Distance: Far
            - Open Borders
            - Declaration of Friendship
          - Japan:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - Babylon:
            - Distance: Neighbors
            - Denounced Them
        - Votes: 7
        
        ## Player 3
        - Civilization: Japan
        - Leader: Oda Nobunaga
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Japan) have denounced one of Greece's declared enemies! (11)
          - We fought together against a common foe. (9)
          - We have Pledged to Protect the same City-States. (7)
          - You (Japan) have gone to war in the past.
          - Greece's real approach to Japan is Hostile.
          - We have divergent Social Policies. (-3)
          - You (Japan) have denounced a leader Greece made a Declaration of Friendship with! (-11)
          - You (Japan) have made a Declaration of Friendship with one of Greece's enemies! (-13)
          - You (Japan) have made a Defensive Pact with one of Greece's enemies! (-15)
          - Religious differences strain your (Japan) relationship. (-30)
          - Your (Japan) spies were caught stealing from Greece. (-33)
          - Greece's leader has expressed a public opinion of Japan (-100).
          - Greece's leader has formed a private opinion of Japan (-100).
          - You (Japan) have chosen to adopt the Autocracy Ideology, but Greece believe in Order. (-999)
        - TheirOpinionOfUs:
          - You (Greece) have no contested borders.
          - You (Greece) have denounced one of Japan's declared enemies!
          - We have Pledged to Protect the same City-States.
          - We fought together against a common foe.
          - Japan fear your (Greece) warmongering will end this world in fire! (They strongly dislike warmongers.)
          - Japan suspect we might be a threat to Japan.
          - Religious differences strain your (Greece) relationship.
          - You (Greece) are competing for World Wonders.
          - We have divergent Social Policies.
          - You (Greece) are competing for the favor of the same City-States!
          - You (Greece) killed or captured civilians from other civilizations!
          - Japan disliked our proposal to the World Congress.
          - Japan believe we are building World Wonders too aggressively!
          - You (Greece) have made a Declaration of Friendship with one of Japan's enemies!
          - Japan fear your (Greece) acquisition of multiple vassals!
          - Japan's friends or allies have denounced you (Greece)!
          - We have denounced each other!
          - Your (Greece) votes opposed Japan's civ's interests in the World Congress.
          - You (Greece) have denounced a leader Japan made a Declaration of Friendship with!
          - You (Greece) have chosen to adopt the Order Ideology, but Japan believe in Autocracy.
          - Japan's leader has expressed a public opinion of you (Greece) (-90).
        - Score: 1880
        - Era: Atomic
        - Technologies: 63
        - Cities: 7
        - Population: 165
        - Territory: 211
        - Gold: 1328
        - GoldPerTurn: 594
        - HappinessSituation: Happy
        - HappinessPercentage: 56
        - MilitaryStrength: 6050
        - TourismPerTurn: 376.5
        - CulturePerTurn: 813
        - PolicyBranches:
          - Fealty: 1
          - Rationalism: 3
          - Statecraft: 4
          - Autocracy: 3
          - Progress: 4
          - Authority: 6
        - ResourcesAvailable:
          - Wheat: 1
          - Sheep: 2
          - Cloves: 1
          - Ivory: 1
          - Gold: 7
          - Paper: 14
          - Pearls: 1
          - Maize: 3
          - Rice: 1
          - Cotton: 1
          - Brazilwood: 1
          - Aluminum: 19
          - Glass: 1
          - Fish: 7
          - Perfume: 1
          - Deer: 2
          - Whales: 1
          - Olives: 1
          - Iron: 7
          - Coal: 9
          - Cattle: 2
          - Uranium: 4
          - Horses: 14
          - Bison: 1
          - Copper: 1
          - Truffles: 1
          - Stone: 1
          - Cinnamon: 1
          - Oil: 7
          - Cocoa: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Mongolia:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Greece:
            - Distance: Far
            - Denounced Them
          - Songhai:
            - Distance: Close
            - Open Borders
            - Declaration of Friendship
          - Carthage:
            - Distance: Distant
            - Denounced Them
          - Ethiopia:
            - Distance: Close
            - War (Our Score: 12%; Our War Weariness: 21%)
            - Denounced Them
          - The Ottomans:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - Babylon:
            - Distance: Far
            - Denounced Them
        - Votes: 6
        
        ## Player 4
        - Civilization: Carthage
        - Leader: Dido
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Carthage) are Greece's vassal state, and Greece like it! (99)
          - We are trade partners. (40)
          - We passed Greece's proposal in the World Congress. (36)
          - We have opened our borders to each other. (12)
          - You (Carthage) have denounced one of Greece's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - We have shared embassies. (1)
          - Greece's real approach to Carthage is Friendly.
        - TheirOpinionOfUs:
          - You (Greece) have denounced one of Carthage's declared enemies!
          - Your (Greece) votes supported Carthage's civ's interests in the World Congress.
          - We are trade partners.
          - You (Greece) are not competing for technological advancement.
          - We have a Diplomat in Carthage's capital.
          - We have made a public Declaration of Friendship!
          - We have made Declarations of Friendship with the same leaders!
          - Carthage are content with your (Greece) treatment of Carthage as Carthage's master.
          - You (Greece) protected Carthage's territory as their master!
          - Your (Greece) recent diplomatic actions please Carthage.
          - We have opened our borders to each other.
          - We have Pledged to Protect the same City-States.
          - We have similar Social Policies.
          - You (Greece) have no contested borders.
          - We have shared embassies.
          - Your (Greece) military deployment is threatening.
          - Carthage are our vassal state.
          - Carthage desire friendly relations with Greece.
          - Carthage's leader has expressed a public opinion of you (Greece) (-20).
          - Carthage disliked our proposal to the World Congress.
          - You (Greece) captured Carthage's original capital.
        - Score: 873
        - Era: Modern
        - GoldenAge: 10 turns remaining
        - Technologies: 50
        - Cities: 1
        - Population: 32
        - Territory: 60
        - Gold: 1228
        - GoldPerTurn: 190
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 1341
        - TourismPerTurn: 65.25
        - CulturePerTurn: 487
        - PolicyBranches:
          - Tradition: 6
          - Artistry: 3
          - Statecraft: 3
          - Rationalism: 2
          - Progress: 2
        - ResourcesAvailable:
          - Cotton: 1
          - Paper: 1
          - Maize: 1
          - Amber: 1
          - Lapis Lazuli: 1
          - Cinnamon: 1
          - Marble: 1
          - Horses: 1
          - Coffee: 1
          - Fish: 3
          - Furs: 1
          - Oil: 2
          - Bananas: 2
          - Cocoa: 2
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Mongolia:
            - Distance: Far
            - War (Our Score: -18%; Our War Weariness: 11%)
            - Denounced Them
          - Babylon:
            - Distance: Far
            - Declaration of Friendship
          - Songhai:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 10%)
            - Denounced Them
          - Greece:
            - Distance: Neighbors
            - Our Master (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Ethiopia:
            - Distance: Far
            - War (Our Score: -10%; Our War Weariness: 15%)
            - Denounced Them
          - Japan:
            - Distance: Distant
          - The Ottomans:
            - Distance: Distant
            - Denounced Them
        - Votes: 3
        
        ## Player 5
        - Civilization: Mongolia
        - Leader: Genghis Khan
        - IsMajor: true
        - OurOpinionOfThem:
          - We have similar Social Policies. (3)
          - Greece's real approach to Mongolia is War.
          - You (Mongolia) have denounced a leader Greece made a Declaration of Friendship with! (-11)
          - You (Mongolia) have made a Declaration of Friendship with one of Greece's enemies! (-13)
          - You (Mongolia) have made a Defensive Pact with one of Greece's enemies! (-15)
          - Religious differences strain your (Mongolia) relationship. (-30)
          - Your (Mongolia) spies were caught stealing from Greece. (-33)
          - We defeated Greece's proposal in the World Congress. (-36)
          - Greece's leader has expressed a public opinion of Mongolia (-100).
          - Greece's leader has formed a private opinion of Mongolia (-100).
          - You (Mongolia) have chosen to adopt the Autocracy Ideology, but Greece believe in Order. (-999)
          - You (Mongolia) are at war! (-99999)
        - TheirOpinionOfUs:
          - You (Greece) have no contested borders.
          - We have similar Social Policies.
          - Mongolia liked our proposal to the World Congress.
          - Mongolia fear your (Greece) warmongering will end this world in fire! (They overlook modest warmongering.)
          - Religious differences strain your (Greece) relationship.
          - Your (Greece) recent diplomatic actions disappoint Mongolia.
          - Mongolia believe we are building World Wonders too aggressively!
          - You (Greece) are competing for the favor of the same City-States!
          - You (Greece) killed or captured civilians from other civilizations!
          - We defeated Mongolia's proposal in the World Congress.
          - You (Greece) have made a Declaration of Friendship with one of Mongolia's enemies!
          - Mongolia fear your (Greece) acquisition of multiple vassals!
          - You (Greece) have denounced a leader Mongolia made a Declaration of Friendship with!
          - Mongolia's friends or allies have denounced you (Greece)!
          - We have denounced each other!
          - Your (Greece) votes opposed Mongolia's civ's interests in the World Congress.
          - You (Greece) have chosen to adopt the Order Ideology, but Mongolia believe in Autocracy.
          - Mongolia's leader has expressed a public opinion of you (Greece) (-100).
          - Mongolia believe we are expanding Greece too aggressively!
          - You (Greece) are at war!
        - Score: 2222
        - Era: Atomic
        - Technologies: 65
        - Cities: 6
        - Population: 165
        - Territory: 195
        - Gold: 892
        - GoldPerTurn: 365
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 5506
        - TourismPerTurn: 586.5
        - CulturePerTurn: 1018
        - PolicyBranches:
          - Tradition: 2
          - Rationalism: 2
          - Progress: 2
          - Authority: 4
          - Fealty: 1
          - Industry: 1
          - Artistry: 1
          - Statecraft: 6
          - Autocracy: 2
          - Imperialism: 1
        - ResourcesAvailable:
          - Wheat: 3
          - Ivory: 1
          - Gold: 1
          - Pearls: 2
          - Paper: 11
          - Cotton: 1
          - Gems: 1
          - Salt: 1
          - Brazilwood: 1
          - Aluminum: 20
          - Glass: 2
          - Lapis Lazuli: 1
          - Coffee: 1
          - Deer: 4
          - Whales: 1
          - Olives: 7
          - Iron: 3
          - Cinnamon: 1
          - Coal: 6
          - Cattle: 2
          - Marble: 1
          - Horses: 4
          - Bison: 1
          - Copper: 1
          - Stone: 1
          - Crab: 1
          - Oil: 5
          - Cocoa: 1
        - FoundedReligion: Tengriism
        - Relationships:
          - Babylon:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
          - Greece:
            - Distance: Close
            - War (Our Score: -6%; Our War Weariness: 7%)
            - Denounced Them
          - Songhai:
            - Distance: Far
            - Open Borders
          - Carthage:
            - Distance: Far
            - War (Our Score: 18%; Our War Weariness: 1%)
            - Denounced Them
          - Ethiopia:
            - Distance: Distant
            - Open Borders
          - Japan:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - The Ottomans:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
        - Votes: 12
        
        ## Player 6
        - Civilization: Greece
        - Leader: Alexander
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: None, Our top defensive pact ally: None
          - Our top World Congress ally: Carthage, Our top World Congress rival: Mongolia
          - Our top Competitor: Ethiopia
        - Score: 3202
        - Era: Atomic
        - GoldenAge: Estimated in 20 turns
        - Technologies: 62
        - CurrentResearch: Atomic Theory (Estimated in 8 turns)
        - NextPolicyTurns: 4
        - Cities: 16
        - Population: 338
        - Territory: 652
        - BestSettlementLocation:
          - 29, 12 (Quality: 100%; 10 tiles from us; near Songhai, 6 tiles away)
          - 30, 12 (Quality: 100%; 11 tiles from us; near Babylon, 6 tiles away)
          - 30, 13 (Quality: 100%; 10 tiles from us; near Babylon, 6 tiles away)
          - 28, 12 (Quality: 67%; 10 tiles from us; near Songhai, 6 tiles away)
          - 35, 19 (Quality: 53%; 6 tiles from us)
        - Gold: 1168
        - GoldPerTurn: 58
        - HappinessSituation: Happy
        - HappinessPercentage: 55
        - MilitaryUnits: 61
        - MilitarySupply: 61
        - MilitaryStrength: 7352
        - TourismPerTurn: 681.75
        - CulturePerTurn: 1941
        - FaithPerTurn: 394
        - SciencePerTurn: 2735
        - PolicyBranches:
          - Order:
            - Patriotic War
            - Double Agents
            - Dictatorship of the Proletariat
            - Workers' Faculties
            - Five-Year Plan
          - Tradition:
            - Tradition
            - Justice
            - Sovereignty
            - Ceremony
            - Splendor
            - Majesty
          - Rationalism:
            - Rationalism
            - Scientific Revolution
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Consulates
            - Shadow Networks
            - Exchange Markets
            - Trade Confederacy
          - Imperialism:
            - Imperialism
          - Progress:
            - Progress
            - Liberty
          - Industry:
            - Industry
            - Entrepreneurship
            - Free Trade
        - ResourcesAvailable:
          - Wheat: 4
          - Silver: 0
          - Sheep: 11
          - Cloves: 0
          - Figs: 0
          - Ivory: 1
          - Gold: 0
          - Nutmeg: 0
          - Pearls: 1
          - Paper: 14
          - Rice: 1
          - Cotton: 1
          - Gems: 2
          - Salt: 1
          - Brazilwood: 0
          - Aluminum: 33
          - Maize: 2
          - Glass: 0
          - Lapis Lazuli: 5
          - Amber: 6
          - Coffee: 1
          - Deer: 6
          - Whales: 0
          - Perfume: 0
          - Sugar: 1
          - Olives: 0
          - Iron: 9
          - Jade: 0
          - Cinnamon: 1
          - Coal: -2
          - Tea: 0
          - Cattle: 5
          - Pepper: 0
          - Marble: 1
          - Horses: -2
          - Coral: 0
          - Silk: 0
          - Jewelry: 1
          - Fish: 14
          - Bison: 6
          - Antiquity Site: 0
          - Copper: 0
          - Truffles: 1
          - Citrus: 0
          - Incense: 0
          - Stone: 3
          - Crab: 1
          - Furs: 7
          - Dyes: 0
          - Bananas: 2
          - Wine: 3
          - Porcelain: 0
          - Cocoa: 3
          - Tobacco: 0
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Mongolia:
            - Distance: Close
            - War (Our Score: 6%; Our War Weariness: 3%)
            - Denounced Them
          - Babylon:
            - Distance: Neighbors
            - Our Vassal (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Songhai:
            - Distance: Neighbors
            - War (Our Score: 100%; Our War Weariness: 97%)
            - Denounced Them
          - Carthage:
            - Distance: Neighbors
            - Our Vassal (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Ethiopia:
            - Distance: Neighbors
            - War (Our Score: 16%; Our War Weariness: 44%)
            - Denounced Them
          - Japan:
            - Distance: Far
            - Denounced Them
          - The Ottomans:
            - Distance: Close
        - OutgoingTradeRoutes:
          - Carthage (Greece) => Zurich (City-State Zurich):
            - TurnsLeft: 20
            - Domain: Sea
            - FromGold: 34.84
          - Sparta (Greece) => Copenhagen (City-State Copenhagen):
            - TurnsLeft: 19
            - FromScience: 7.5
            - Domain: Land
            - FromGold: 57.05
            - FromCulture: 7.5
          - Jenne (Greece) => Monaco (City-State Monaco):
            - TurnsLeft: 28
            - FromScience: 7.5
            - Domain: Sea
            - FromGold: 39.49
            - FromCulture: 7.5
          - Athens (Greece) => Manila (City-State Manila):
            - TurnsLeft: 12
            - FromScience: 7.5
            - Domain: Land
            - FromGold: 51.91
            - FromCulture: 7.5
          - Tombouctu (Greece) => Dur-Kurigalzu (Babylon):
            - ToGold: 4.75
            - TurnsLeft: 14
            - FromScience: 22.5
            - Domain: Land
            - FromGold: 50.19
            - ToCulture: 3
            - ToScience: 3
          - Sparta (Greece) => Antananarivo (City-State Antananarivo):
            - TurnsLeft: 7
            - FromScience: 7.5
            - Domain: Land
            - FromGold: 65.36
            - FromCulture: 7.5
          - Argos (Greece) => Sparta (Greece):
            - TurnsLeft: 16
            - Domain: Land
            - ToProduction: 22
          - Athens (Greece) => Utique (Greece):
            - ToFood: 32.03
            - TurnsLeft: 21
            - Domain: Land
          - Shushan (Greece) => Budapest (City-State Budapest):
            - TurnsLeft: 7
            - Domain: Land
            - FromGold: 32.99
          - Shushan (Greece) => Knossos (Greece):
            - TurnsLeft: 22
            - Domain: Land
            - ToProduction: 23
          - Athens (Greece) => Argos (Greece):
            - ToFood: 33.4
            - TurnsLeft: 21
            - Domain: Land
        - IncomingTradeRoutes:
          - Gades (Carthage) => Borsippa (Greece):
            - ToGold: 13.75
            - TurnsLeft: 19
            - FromScience: 33.75
            - Domain: Sea
            - FromGold: 40.97
            - FromCulture: 25
          - Gades (Carthage) => Awasa (Greece):
            - ToGold: 10.78
            - TurnsLeft: 16
            - FromScience: 33.75
            - Domain: Sea
            - FromGold: 33.56
            - FromCulture: 25
          - Babylon (Babylon) => Gao (Greece):
            - ToGold: 7.2
            - TurnsLeft: 21
            - FromScience: 20
            - Domain: Land
            - FromGold: 23.36
            - FromCulture: 18
            - ToScience: 2
          - Gades (Carthage) => Carthage (Greece):
            - ToGold: 10.23
            - TurnsLeft: 4
            - FromScience: 33.75
            - Domain: Sea
            - FromGold: 44.67
            - FromCulture: 25
          - Dur-Kurigalzu (Babylon) => Tombouctu (Greece):
            - ToGold: 10.17
            - TurnsLeft: 8
            - FromScience: 20
            - Domain: Land
            - FromGold: 31.87
            - FromCulture: 18
            - ToScience: 2
          - Gades (Carthage) => Knossos (Greece):
            - ToGold: 8.25
            - TurnsLeft: 3
            - FromScience: 33.75
            - Domain: Sea
            - FromGold: 34.34
            - FromCulture: 25
          - Dur-Kurigalzu (Babylon) => Jenne (Greece):
            - ToGold: 9
            - TurnsLeft: 26
            - FromScience: 20
            - Domain: Land
            - FromGold: 30.22
            - FromCulture: 18
            - ToScience: 2
          - Gades (Carthage) => Hippo Regius (Greece):
            - ToGold: 8.25
            - TurnsLeft: 27
            - FromScience: 33.75
            - Domain: Sea
            - FromGold: 37.51
            - FromCulture: 25
          - Gades (Carthage) => Shushan (Greece):
            - ToGold: 8.25
            - TurnsLeft: 27
            - FromScience: 33.75
            - Domain: Sea
            - FromGold: 31.48
            - FromCulture: 25
          - Gades (Carthage) => Sparta (Greece):
            - ToGold: 15.45
            - TurnsLeft: 22
            - FromScience: 33.75
            - Domain: Sea
            - FromGold: 52.59
            - FromCulture: 25
          - Gades (Carthage) => Opis (Greece):
            - ToGold: 13.75
            - TurnsLeft: 25
            - FromScience: 33.75
            - Domain: Sea
            - FromGold: 34.48
            - FromCulture: 25
          - Dur-Kurigalzu (Babylon) => Borsippa (Greece):
            - ToGold: 8.55
            - TurnsLeft: 7
            - FromScience: 20
            - Domain: Sea
            - FromGold: 25.92
            - FromCulture: 18
            - ToScience: 2
        - Spies:
          - Agent Iolaus (5):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 1511
            - Location: Harar (Ethiopia)
            - NetworkPerTurn: 46
          - Agent Straton (1):
            - State: Killed In Action
            - Role: Spy
            - Location: Unassigned
            - NetworkPerTurn: 0
          - Agent Andres (12):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 174
            - Location: Kyoto (Japan)
            - NetworkPerTurn: 42
          - Agent Aeneas (8):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 382
            - Location: Adwa (Ethiopia)
            - NetworkPerTurn: 46
          - Agent Gaiane (4):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 382
            - Location: Addis Ababa (Ethiopia)
            - NetworkPerTurn: 46
          - Agent Leander (6):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 252
            - Location: Bahir Dar (Ethiopia)
            - NetworkPerTurn: 46
          - Agent Ligeia (10):
            - State: Schmoozing
            - Role: Vassal Diplomat
            - Network: 4240
            - Location: Babylon (Babylon)
            - NetworkPerTurn: 50
          - Agent Alexa (2):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 252
            - Location: Axum (Ethiopia)
            - NetworkPerTurn: 46
          - Agent Desdemona (7):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 178
            - Location: Istanbul (The Ottomans)
            - NetworkPerTurn: 28
          - Agent Cletus (11):
            - State: Killed In Action
            - Role: Spy
            - Location: Unassigned
            - NetworkPerTurn: 0
          - Agent Phaidros (0):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 752
            - Location: Gondar (Ethiopia)
            - NetworkPerTurn: 46
          - Agent Theophila (3):
            - State: Schmoozing
            - Role: Vassal Diplomat
            - Network: 9450
            - Location: Gades (Carthage)
            - NetworkPerTurn: 60
          - Agent Nikandros (9):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 382
            - Location: Lalibela (Ethiopia)
            - NetworkPerTurn: 46
        - DiplomaticDeals:
          - Carthage:
            - #0:
              - WeGive:
                - 1 Marble
              - TheyGive:
                - 6 Gold per Turn
            - #1:
              - WeGive:
                - 1 Lapis Lazuli
              - TheyGive:
                - 6 Gold per Turn
              - TurnsRemaining: 5
            - #2:
              - WeGive:
                - 1 Coffee
              - TheyGive:
                - 6 Gold per Turn
              - TurnsRemaining: 8
            - #3:
              - WeGive:
                - Open Borders
              - TheyGive:
                - 4 Gold per Turn
              - TurnsRemaining: 12
            - #4:
              - WeGive:
                - 1 Cotton
              - TurnsRemaining: 12
            - #5:
              - WeGive:
                - 1 Furs
              - TheyGive:
                - 6 Gold per Turn
              - TurnsRemaining: 19
            - #6:
              - WeGive:
                - 1 Iron
              - TheyGive:
                - 11 Gold per Turn
              - TurnsRemaining: 24
            - #7:
              - WeGive:
                - 1 Cinnamon
              - TheyGive:
                - 6 Gold per Turn
              - TurnsRemaining: 25
            - #8:
              - WeGive:
                - 1 Amber
              - TheyGive:
                - 6 Gold per Turn
              - TurnsRemaining: 39
            - #9:
              - WeGive:
                - 1 Marble
              - TheyGive:
                - 6 Gold per Turn
              - TurnsRemaining: 50
          - Babylon:
            - #0:
              - WeGive:
                - 1 Ivory
              - TheyGive:
                - 6 Gold per Turn
              - TurnsRemaining: 11
            - #1:
              - WeGive:
                - 19 Gold per Turn
              - TheyGive:
                - 1 Sugar
              - TurnsRemaining: 15
            - #2:
              - WeGive:
                - 19 Gold per Turn
              - TheyGive:
                - 1 Truffles
              - TurnsRemaining: 17
            - #3:
              - WeGive:
                - 1 Marble
              - TurnsRemaining: 28
            - #4:
              - WeGive:
                - Open Borders
              - TheyGive:
                - 3 Gold per Turn
              - TurnsRemaining: 31
            - #5:
              - WeGive:
                - 1 Coffee
              - TheyGive:
                - 7 Gold per Turn
              - TurnsRemaining: 32
            - #6:
              - WeGive:
                - 1 Furs
              - TheyGive:
                - 7 Gold per Turn
              - TurnsRemaining: 42
        - Votes: 21
        
        ## Player 7
        - Civilization: Ethiopia
        - Leader: Haile Selassie
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Ethiopia) have both chosen to adopt the Order Ideology. (999)
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - Greece's real approach to Ethiopia is War.
          - Greece are spreading Greece's own religion, but you (Ethiopia) converted some of their cities to your (Ethiopia) religion. (-2)
          - You (Ethiopia) have denounced a leader Greece made a Declaration of Friendship with! (-11)
          - You (Ethiopia) excavated Greece's cultural artifacts! (-18)
          - Religious differences strain your (Ethiopia) relationship. (-30)
          - Your (Ethiopia) spies were caught stealing from Greece. (-33)
          - We defeated Greece's proposal in the World Congress. (-36)
          - Greece's leader has expressed a public opinion of Ethiopia (-100).
          - Greece's leader has formed a private opinion of Ethiopia (-100).
          - You (Ethiopia) are at war! (-99999)
        - TheirOpinionOfUs:
          - You (Greece) have both chosen to adopt the Order Ideology.
          - We passed Ethiopia's proposal in the World Congress.
          - Ethiopia's leader has expressed a public opinion of you (Greece) (80).
          - You (Greece) are not competing for cultural advancement.
          - You (Greece) have denounced one of Ethiopia's declared enemies!
          - Your (Greece) recent diplomatic actions please Ethiopia.
          - We have Pledged to Protect the same City-States.
          - We have similar Social Policies.
          - Ethiopia fear your (Greece) warmongering will end this world in fire! (They hate warmongers!)
          - Territorial disputes strain your (Greece) relationship.
          - Religious differences strain your (Greece) relationship.
          - You (Greece) have made a Declaration of Friendship with one of Ethiopia's enemies!
          - Ethiopia believe we are building World Wonders too aggressively!
          - You (Greece) are competing for the favor of the same City-States!
          - We tried to place sanctions on Ethiopia in the World Congress.
          - You (Greece) stole Ethiopia's territory while at peace!
          - Ethiopia disliked our proposal to the World Congress.
          - Ethiopia fear your (Greece) acquisition of multiple vassals!
          - Ethiopia believe we are expanding Greece too aggressively!
          - We have denounced Ethiopia!
          - Your (Greece) spies were caught stealing from Ethiopia.
          - Your (Greece) votes opposed Ethiopia's civ's interests in the World Congress.
          - You (Greece) are at war!
        - Score: 2376
        - Era: Atomic
        - Technologies: 65
        - Cities: 10
        - Population: 221
        - Territory: 446
        - Gold: 1286
        - GoldPerTurn: 343
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 37
        - MilitaryStrength: 1321
        - TourismPerTurn: 479.25
        - CulturePerTurn: 1608
        - PolicyBranches:
          - Tradition: 5
          - Rationalism: 2
          - Progress: 2
          - Authority: 1
          - Fealty: 1
          - Industry: 1
          - Artistry: 5
          - Statecraft: 4
          - Order: 3
        - ResourcesAvailable:
          - Wheat: 3
          - Sheep: 7
          - Paper: 7
          - Pearls: 1
          - Maize: 5
          - Salt: 3
          - Aluminum: 10
          - Fish: 5
          - Deer: 4
          - Whales: 1
          - Olives: 1
          - Iron: 12
          - Coal: 3
          - Coffee: 1
          - Cattle: 1
          - Horses: 6
          - Coral: 1
          - Bison: 5
          - Stone: 2
          - Marble: 1
          - Bananas: 1
          - Oil: 12
          - Cocoa: 1
        - FoundedReligion: Eastern Orthodoxy
        - Relationships:
          - Mongolia:
            - Distance: Distant
            - Open Borders
          - Greece:
            - Distance: Neighbors
            - War (Our Score: -16%; Our War Weariness: 61%)
          - Songhai:
            - Distance: Far
          - Carthage:
            - Distance: Far
            - War (Our Score: 10%; Our War Weariness: 39%)
            - Denounced Them
          - Babylon:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 36%)
          - Japan:
            - Distance: Close
            - War (Our Score: -12%; Our War Weariness: 34%)
          - The Ottomans:
            - Distance: Far
            - Open Borders
            - Declaration of Friendship
        - Votes: 9
        
        ## Player 22
        - Civilization: Riga
        - Leader: City State
        - MajorAlly: Greece
        - Population: 21
        - ResourcesAvailable:
          - Fish: 2
          - Stone: 1
          - Sheep: 1
        - MajorityReligion: Buddhism
        - Relationships:
          - Babylon: Friends (Influence: 123, Distance: Far)
          - Mongolia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Greece: Ally (Influence: 525, Distance: Close, Protected)
          - Songhai: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Carthage: Neutral (Influence: -44, Distance: Distant)
          - Ethiopia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Japan: Neutral (Influence: 5, Distance: Distant, Protected)
          - The Ottomans: Friends (Influence: 56, Distance: Close, Protected)
        - Quests:
          - Diplomatic Missions are temporarily more effective. (Turns remaining: 25) They want you to start a land or sea trade route to their city. (Turns remaining: 15) Potential Quest Reward: * 152 Influence * 375 Food in Capital
        
        ## Player 23
        - Civilization: Monaco
        - Leader: City State
        - MajorAlly: Greece
        - Population: 14
        - ResourcesAvailable:
          - Fish: 3
        - MajorityReligion: Buddhism
        - Relationships:
          - Babylon: Neutral (Influence: -60, Distance: Neighbors)
          - Mongolia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Greece: Ally (Influence: 856, Distance: Neighbors, Protected)
          - Songhai: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Carthage: Friends (Influence: 106, Distance: Distant)
          - Ethiopia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Japan: Neutral (Influence: 0, Distance: Far)
          - The Ottomans: Friends (Influence: 160, Distance: Close, Protected)
        - Quests:
          - They want you to generate a Great Musician. (Turns remaining: 40) Potential Quest Reward: * 150 Influence * 713 Culture
        
        ## Player 24
        - Civilization: Salem
        - Leader: City State
        - MajorAlly: The Ottomans
        - Population: 16
        - ResourcesAvailable:
          - Fish: 2
        - MajorityReligion: Buddhism
        - Relationships:
          - Babylon: Neutral (Influence: 0, Distance: Close)
          - Mongolia: Neutral (Influence: 0, Distance: Distant)
          - Greece: Friends (Influence: 138, Distance: Close, Protected)
          - Songhai: War - Peace Currently Blocked (Influence: -60, Distance: Neighbors)
          - Carthage: Friends (Influence: 63, Distance: Distant)
          - Ethiopia: Friends (Influence: 34, Distance: Distant)
          - Japan: Neutral (Influence: 5, Distance: Far, Protected)
          - The Ottomans: Ally (Influence: 215, Distance: Neighbors, Protected)
        - Quests:
          - They will reward the player with the highest Tourism per turn. So far, you have the lead with 681 per turn. (Turns remaining: 29) Potential Quest Reward: * 347 Influence * 547 Culture
          - They want you to start a land or sea trade route to their city. (Turns remaining: 40) Potential Quest Reward: * 199 Influence * 332 Food in Capital
        
        ## Player 25
        - Civilization: Zurich
        - Leader: City State
        - MajorAlly: Japan
        - Population: 20
        - ResourcesAvailable:
          - Fish: 4
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: Neutral (Influence: -6, Distance: Distant)
          - Mongolia: Neutral (Influence: -6, Distance: Distant)
          - Greece: Friends (Influence: 294, Distance: Close, Protected)
          - Songhai: Neutral (Influence: -6, Distance: Distant)
          - Carthage: Neutral (Influence: -21, Distance: Far)
          - Ethiopia: War (Influence: -60, Distance: Neighbors)
          - Japan: Ally (Influence: 375, Distance: Far, Protected)
          - The Ottomans: Neutral (Influence: 0, Distance: Distant)
        - Quests:
          - They will reward the player with the highest Tourism per turn. So far, you have the lead with 681 per turn. (Turns remaining: 8) Potential Quest Reward: * 250 Influence * 397 Culture
          - Conduct a Spy Mission against Genghis Khan. Potential Quest Reward: * 322 Influence * 763 Science
          - They want Islam to become the majority religion in their city. (Turns remaining: 37) Potential Quest Reward: * 175 Influence * 371 Faith
        
        ## Player 26
        - Civilization: Manila
        - Leader: City State
        - MajorAlly: Greece
        - Population: 22
        - ResourcesAvailable:
          - Fish: 2
          - Bison: 1
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: Neutral (Influence: -55, Distance: Distant)
          - Mongolia: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Greece: Ally (Influence: 1342, Distance: Neighbors, Protected)
          - Songhai: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Carthage: Neutral (Influence: 28, Distance: Close, Protected)
          - Ethiopia: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Japan: Neutral (Influence: -55, Distance: Distant)
          - The Ottomans: Neutral (Influence: -55, Distance: Distant)
        - Quests:
          - They will reward the player that destroys a nearby Barbarian Encampment. Potential Quest Reward: * 135 Influence * 161 Great General Points
        
        ## Player 27
        - Civilization: Copenhagen
        - Leader: City State
        - MajorAlly: Greece
        - Population: 9
        - ResourcesAvailable:
          - Deer: 1
          - Sheep: 1
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Greece: Ally (Influence: 605, Distance: Neighbors, Protected)
          - Songhai: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Carthage: Neutral (Influence: 0, Distance: Far)
          - Ethiopia: War - Peace Currently Blocked (Influence: -60, Distance: Neighbors)
          - Japan: Neutral (Influence: 0, Distance: Distant)
          - The Ottomans: Friends (Influence: 108, Distance: Distant)
        - Quests:
          - Conduct a Spy Mission against Askia. Potential Quest Reward: * 359 Influence * 879 Science
          - They want Islam to become the majority religion in their city. (Turns remaining: 11) Potential Quest Reward: * 176 Influence * 407 Faith
        
        ## Player 28
        - Civilization: Veligrad
        - Leader: City State
        - MajorAlly: Mongolia
        - Population: 26
        - ResourcesAvailable:
          - Fish: 2
        - MajorityReligion: Tengriism
        - Relationships:
          - Babylon: War (Influence: -60, Distance: Far)
          - Mongolia: Ally (Influence: 723, Distance: Neighbors, Protected)
          - Greece: War (Influence: -60, Distance: Close)
          - Songhai: Neutral (Influence: -20, Distance: Far)
          - Carthage: War (Influence: -60, Distance: Close)
          - Ethiopia: Friends (Influence: 289, Distance: Distant)
          - Japan: Friends (Influence: 166, Distance: Close, Protected)
          - The Ottomans: Friends (Influence: 421, Distance: Far, Protected)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 29
        - Civilization: Wanggeom
        - Leader: City State
        - MajorAlly: Mongolia
        - Population: 21
        - ResourcesAvailable:
          - Fish: 1
          - Deer: 1
          - Sheep: 1
        - MajorityReligion: Tengriism
        - Relationships:
          - Babylon: War (Influence: -60, Distance: Distant)
          - Mongolia: Ally (Influence: 754, Distance: Close, Protected)
          - Greece: War (Influence: -60, Distance: Distant)
          - Songhai: Neutral (Influence: -55, Distance: Distant)
          - Carthage: War (Influence: -60, Distance: Distant)
          - Ethiopia: Neutral (Influence: -35, Distance: Far)
          - Japan: Friends (Influence: 98, Distance: Neighbors)
          - The Ottomans: Neutral (Influence: -55, Distance: Far)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 30
        - Civilization: Abernethy
        - Leader: City State
        - Population: 22
        - ResourcesAvailable:
          - Fish: 2
          - Cocoa: 1
          - Sheep: 1
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: Neutral (Influence: 0, Distance: Close)
          - Mongolia: Neutral (Influence: 0, Distance: Distant)
          - Greece: Neutral (Influence: 5, Distance: Neighbors, Protected)
          - Songhai: Neutral (Influence: 0, Distance: Close)
          - Carthage: Friends (Influence: 60, Distance: Far)
          - Ethiopia: Friends (Influence: 73, Distance: Close, Protected)
          - Japan: Neutral (Influence: 0, Distance: Distant)
          - The Ottomans: Neutral (Influence: 29, Distance: Distant)
        - Quests:
          - They want Islam to become the majority religion in their city. (Turns remaining: 32) Potential Quest Reward: * 155 Influence * 526 Faith
          - They want you to defeat Barbarian units that are invading their territory. You are allowed to enter their territory until the Barbarians are defeated.
        
        ## Player 31
        - Civilization: Hanoi
        - Leader: City State
        - MajorAlly: Mongolia
        - Population: 26
        - ResourcesAvailable:
          - Fish: 3
        - MajorityReligion: Tengriism
        - Relationships:
          - Babylon: War (Influence: -60, Distance: Distant)
          - Mongolia: Ally (Influence: 564, Distance: Neighbors, Protected)
          - Greece: War (Influence: -60, Distance: Close)
          - Songhai: Neutral (Influence: 0, Distance: Distant)
          - Carthage: War (Influence: -60, Distance: Far)
          - Ethiopia: Friends (Influence: 31, Distance: Distant)
          - Japan: Friends (Influence: 196, Distance: Far)
          - The Ottomans: Friends (Influence: 68, Distance: Distant)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 32
        - Civilization: Vatican City
        - Leader: City State
        - MajorAlly: Ethiopia
        - Population: 25
        - ResourcesAvailable:
          - Fish: 4
          - Sheep: 1
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: War (Influence: -60, Distance: Distant)
          - Mongolia: Friends (Influence: 70, Distance: Distant)
          - Greece: War (Influence: -60, Distance: Far)
          - Songhai: Neutral (Influence: 10, Distance: Far)
          - Carthage: War (Influence: -60, Distance: Distant)
          - Ethiopia: Ally (Influence: 319, Distance: Neighbors, Protected)
          - Japan: War (Influence: -60, Distance: Far)
          - The Ottomans: Neutral (Influence: 29, Distance: Far, Protected)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 33
        - Civilization: Budapest
        - Leader: City State
        - Population: 22
        - ResourcesAvailable:
          - Aluminum: 3
          - Pearls: 1
          - Deer: 1
          - Fish: 4
        - Relationships:
          - Babylon: Neutral (Influence: 5, Distance: Close, Protected)
          - Mongolia: Neutral (Influence: 10, Distance: Distant)
          - Greece: Friends (Influence: 295, Distance: Neighbors, Protected)
          - Songhai: Neutral (Influence: 0, Distance: Close)
          - Carthage: Neutral (Influence: 10, Distance: Close)
          - Ethiopia: Neutral (Influence: -13, Distance: Far)
          - Japan: Friends (Influence: 30, Distance: Distant)
          - The Ottomans: Friends (Influence: 325, Distance: Distant)
        - Quests:
          - Send an archaeologist to a site near this city-state. Potential Quest Reward: * 176 Influence * 670 Tourism with all known Civilizations
          - They want Islam to become the majority religion in their city. (Turns remaining: 38) Potential Quest Reward: * 199 Influence * 465 Faith
        
        ## Player 34
        - Civilization: Buenos Aires
        - Leader: City State
        - MajorAlly: Mongolia
        - Population: 14
        - ResourcesAvailable:
          - Deer: 1
          - Sheep: 1
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: War (Influence: -60, Distance: Distant)
          - Mongolia: Ally (Influence: 234, Distance: Distant)
          - Greece: War (Influence: -60, Distance: Far)
          - Songhai: Neutral (Influence: 0, Distance: Distant)
          - Carthage: War (Influence: -60, Distance: Distant)
          - Ethiopia: Friends (Influence: 33, Distance: Neighbors, Protected)
          - Japan: Friends (Influence: 30, Distance: Distant)
          - The Ottomans: Friends (Influence: 157, Distance: Distant)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 35
        - Civilization: Antananarivo
        - Leader: City State
        - MajorAlly: Greece
        - Population: 8
        - ResourcesAvailable:
          - Stone: 1
          - Deer: 1
          - Sheep: 1
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Greece: Ally (Influence: 886, Distance: Neighbors, Protected)
          - Songhai: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Carthage: Neutral (Influence: 10, Distance: Far)
          - Ethiopia: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Japan: Friends (Influence: 128, Distance: Distant)
          - The Ottomans: Friends (Influence: 46, Distance: Distant)
        - Quests:
          - They will reward the player with the highest Tourism per turn. So far, you have the lead with 681 per turn. (Turns remaining: 18) Potential Quest Reward: * 301 Influence * 380 Culture
        
        ## Player 36
        - Civilization: Almaty
        - Leader: City State
        - Population: 11
        - ResourcesAvailable:
          - Coffee: 1
          - Sheep: 2
        - MajorityReligion: Tengriism
        - Relationships:
          - Babylon: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: Friends (Influence: 371, Distance: Neighbors, Protected)
          - Greece: Friends (Influence: 138, Distance: Distant)
          - Songhai: Neutral (Influence: 14, Distance: Distant)
          - Carthage: Neutral (Influence: 0, Distance: Distant)
          - Ethiopia: Friends (Influence: 242, Distance: Distant)
          - Japan: Friends (Influence: 115, Distance: Close, Protected)
          - The Ottomans: Neutral (Influence: 29, Distance: Far)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 37
        - Civilization: Antwerp
        - Leader: City State
        - MajorAlly: Mongolia
        - Population: 28
        - ResourcesAvailable:
          - Fish: 2
        - MajorityReligion: Tengriism
        - Relationships:
          - Babylon: War (Influence: -60, Distance: Far)
          - Mongolia: Ally (Influence: 659, Distance: Neighbors, Protected)
          - Greece: War (Influence: -60, Distance: Far)
          - Songhai: Neutral (Influence: 0, Distance: Far)
          - Carthage: War (Influence: -60, Distance: Distant)
          - Ethiopia: Friends (Influence: 404, Distance: Distant)
          - Japan: Friends (Influence: 405, Distance: Neighbors, Protected)
          - The Ottomans: Friends (Influence: 295, Distance: Close, Protected)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        - 63: Barbarians
        
        # Cities
        Cities: summary reports about discovered cities in the world.
        
        ## Player: Songhai
        
        ### Taghaza
        - ID: 1776
        - X: 59
        - Y: 9
        - Population: 25
        - MajorityReligion: Buddhism
        - DefenseStrength: 113
        - Health: 82%
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - Ironworks
          - Imperial College
          - Pentagon
          - Soho Foundry
          - Giorgio Armeier Headquarters
        
        ### Tondibi
        - ID: 2265
        - X: 58
        - Y: 14
        - Population: 18
        - MajorityReligion: Buddhism
        - DefenseStrength: 80
        - Health: 84%
        - Wonders:
          - Circus Maximus
          - Royal Collection
        
        ### Kumbi Saleh
        - ID: 2885
        - X: 61
        - Y: 3
        - Population: 23
        - MajorityReligion: Buddhism
        - DefenseStrength: 93
        - Health: 64%
        - Wonders:
          - Neuschwanstein
          - Grand Temple
        
        ### Kukia
        - ID: 3862
        - X: 62
        - Y: 12
        - Population: 23
        - MajorityReligion: Buddhism
        - DefenseStrength: 80
        - IsCoastal: true
        - Wonders:
          - Scrivener's Office
          - Printing Press
        
        ### Ankara
        - ID: 5086
        - X: 62
        - Y: 16
        - Population: 22
        - MajorityReligion: Buddhism
        - DefenseStrength: 89
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Chartered Company
          - Red Fort
        
        ### Tegdaoust
        - ID: 9435
        - X: 27
        - Y: 6
        - Population: 19
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 78
        - IsCoastal: true
        - Wonders:
          - National Monument
        
        ## Player: Babylon
        
        ### Babylon
        - ID: 1058
        - X: 54
        - Y: 13
        - Population: 30
        - MajorityReligion: Catholicism
        - DefenseStrength: 74
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Imperial College
          - Royal Collection
          - Great Wall
          - University of Sankore
          - Scrivener's Office
          - Printing Press
          - Etemenanki
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
          - Grand Ossuary
        
        ### Dur-Kurigalzu
        - ID: 1293
        - X: 51
        - Y: 11
        - Population: 23
        - MajorityReligion: Catholicism
        - DefenseStrength: 51
        - IsCoastal: true
        
        ### Eshnunna
        - ID: 9153
        - X: 41
        - Y: 8
        - Population: 18
        - MajorityReligion: Catholicism
        - DefenseStrength: 53
        - IsCoastal: true
        
        ### Gwandu
        - ID: 13974
        - X: 34
        - Y: 8
        - Population: 13
        - DefenseStrength: 55
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: The Ottomans
        
        ### Istanbul
        - ID: 1059
        - X: 63
        - Y: 21
        - Population: 34
        - DefenseStrength: 80
        - IsCoastal: true
        - Wonders:
          - National Monument
          - Circus Maximus
          - Chartered Company
          - Great Lighthouse
          - Oracle
          - Scrivener's Office
          - Printing Press
          - Royal Guardhouse
          - Court Chapel
        
        ### Edirne
        - ID: 1238
        - X: 66
        - Y: 26
        - Population: 35
        - DefenseStrength: 66
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - Ironworks
          - Imperial College
          - Great Library
          - Himeji Castle
          - Forbidden Palace
          - Grand Temple
          - Centaurus Extractors Headquarters
        
        ### Bursa
        - ID: 1979
        - X: 65
        - Y: 32
        - Population: 27
        - MajorityReligion: Tengriism
        - DefenseStrength: 78
        - IsCoastal: true
        - Wonders:
          - Royal Collection
        
        ### Konya
        - ID: 2328
        - X: 68
        - Y: 21
        - Population: 23
        - DefenseStrength: 85
        - IsCoastal: true
        - Wonders:
          - Statue of Liberty
        
        ### Samsun
        - ID: 4640
        - X: 62
        - Y: 25
        - Population: 27
        - DefenseStrength: 78
        - IsCoastal: true
        
        ### Gaziantep
        - ID: 5051
        - X: 68
        - Y: 15
        - Population: 19
        - DefenseStrength: 73
        - IsCoastal: true
        
        ### Nippur
        - ID: 11509
        - X: 59
        - Y: 22
        - Population: 19
        - DefenseStrength: 25
        - IsOccupied: true
        - IsCoastal: true
        
        ### Akkad
        - ID: 11698
        - X: 57
        - Y: 18
        - Population: 18
        - MajorityReligion: Catholicism
        - DefenseStrength: 27
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: Japan
        
        ### Kyoto
        - ID: 1060
        - X: 60
        - Y: 40
        - Population: 29
        - MajorityReligion: Tengriism
        - DefenseStrength: 77
        - Wonders:
          - Heroic Epic
          - Terracotta Army
          - Grand Temple
          - Scrivener's Office
          - Printing Press
          - Summer Palace
        
        ### Osaka
        - ID: 1350
        - X: 64
        - Y: 39
        - Population: 25
        - MajorityReligion: Tengriism
        - DefenseStrength: 69
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - Circus Maximus
          - Chartered Company
        
        ### Tokyo
        - ID: 2034
        - X: 59
        - Y: 35
        - Population: 26
        - MajorityReligion: Tengriism
        - DefenseStrength: 33
        - IsCoastal: true
        - Wonders:
          - Civilized Jewelers Headquarters
        
        ### Satsuma
        - ID: 2292
        - X: 61
        - Y: 30
        - Population: 22
        - MajorityReligion: Tengriism
        - DefenseStrength: 35
        - IsCoastal: true
        - Wonders:
          - National Monument
        
        ### Kagoshima
        - ID: 2516
        - X: 65
        - Y: 43
        - Population: 25
        - MajorityReligion: Tengriism
        - DefenseStrength: 74
        - IsCoastal: true
        - Wonders:
          - Ironworks
          - Imperial College
          - Royal Collection
        
        ### Nara
        - ID: 8651
        - X: 73
        - Y: 30
        - Population: 20
        - MajorityReligion: Tengriism
        - DefenseStrength: 73
        - IsCoastal: true
        
        ### Nagoya
        - ID: 10129
        - X: 55
        - Y: 50
        - Population: 18
        - MajorityReligion: Tengriism
        - DefenseStrength: 69
        
        ## Player: Carthage
        
        ### Gades
        - ID: 2518
        - X: 32
        - Y: 31
        - Population: 32
        - DefenseStrength: 62
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Circus Maximus
          - Ironworks
          - Imperial College
          - Grand Temple
          - Scrivener's Office
          - Printing Press
          - Great Cothon
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
        
        ## Player: Mongolia
        
        ### Karakorum
        - ID: 1062
        - X: 50
        - Y: 41
        - Population: 40
        - MajorityReligion: Tengriism
        - DefenseStrength: 79
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - Chartered Company
          - Royal Collection
          - Colossus
          - Cristo Redentor
          - Mausoleum of Halicarnassus
          - Prora
          - Printing Press
          - Hall of Honor
          - The Motherland Calls
          - Royal Astrologer
          - Holy Council
        
        ### Beshbalik
        - ID: 1180
        - X: 54
        - Y: 43
        - Population: 26
        - MajorityReligion: Tengriism
        - DefenseStrength: 75
        - Wonders:
          - Circus Maximus
          - Imperial College
        
        ### Turfan
        - ID: 1857
        - X: 50
        - Y: 46
        - Population: 28
        - MajorityReligion: Tengriism
        - DefenseStrength: 75
        - Wonders:
          - School of Philosophy
        
        ### Hsia
        - ID: 2045
        - X: 46
        - Y: 47
        - Population: 23
        - MajorityReligion: Tengriism
        - DefenseStrength: 81
        - Wonders:
          - National Monument
          - Ironworks
          - Foreign Bureau
          - TwoKay Foods Headquarters
        
        ### Old Sarai
        - ID: 2403
        - X: 49
        - Y: 37
        - Population: 24
        - MajorityReligion: Tengriism
        - DefenseStrength: 73
        - IsCoastal: true
        - Wonders:
          - Scrivener's Office
        
        ### New Sarai
        - ID: 3272
        - X: 58
        - Y: 45
        - Population: 24
        - MajorityReligion: Tengriism
        - DefenseStrength: 83
        - Wonders:
          - Grand Temple
        
        ## Player: Greece
        
        ### Athens
        - ID: 1063
        - X: 27
        - Y: 47
        - Population: 35
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 73
        - FoodStored: 2033
        - FoodPerTurn: 125
        - ProductionStored: 1053
        - ProductionPerTurn: 443
        - CurrentProduction: Broadcast Tower
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 310
        - SciencePerTurn: 246
        - CulturePerTurn: 379
        - FaithPerTurn: 58
        - TourismPerTurn: 125.25
        - HappinessDelta: 26
        - BuildingCount: 47
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Military Base
          - Hospital
          - Factory
          - Stock Exchange
          - Public School
          - Constabulary
          - Writers' Guild
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Ironworks
          - Imperial College
          - Chichen Itza
          - Notre Dame
          - Palace of Westminster
          - Brandenburg Gate
          - Eiffel Tower
          - Statue of Zeus
          - Temple of Artemis
          - Leaning Tower of Pisa
          - Printing Press
          - Foreign Bureau
          - Roman Forum
          - Menin Gate
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
        - GreatWorkCount: 8
        
        ### Sparta
        - ID: 1181
        - X: 31
        - Y: 46
        - Population: 26
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 94
        - IsCoastal: true
        - FoodStored: 772
        - FoodPerTurn: 6
        - ProductionStored: 1221
        - ProductionPerTurn: 294
        - CurrentProduction: Broadcast Tower
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 280
        - SciencePerTurn: 194
        - CulturePerTurn: 144
        - FaithPerTurn: 20
        - TourismPerTurn: 54.75
        - HappinessDelta: 6
        - BuildingCount: 54
        - ImportantBuildings:
          - Seaport
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Military Base
          - Hospital
          - Factory
          - Stock Exchange
          - Public School
          - Constabulary
          - Writers' Guild
          - Artists' Guild
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Mine Field
        - Wonders:
          - Circus Maximus
          - Chartered Company
        - GreatWorkCount: 4
        
        ### Corinth
        - ID: 1342
        - X: 28
        - Y: 42
        - Population: 27
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 70
        - FoodStored: 1031
        - FoodPerTurn: 37
        - ProductionPerTurn: 289
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 231
        - SciencePerTurn: 213
        - CulturePerTurn: 192
        - FaithPerTurn: 26
        - TourismPerTurn: 117.75
        - HappinessDelta: 2
        - BuildingCount: 50
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Hospital
          - Factory
          - Stock Exchange
          - Public School
          - Constabulary
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
        - Wonders:
          - Royal Collection
          - Uffizi
          - Parthenon
        - GreatWorkCount: 6
        
        ### Argos
        - ID: 1584
        - X: 24
        - Y: 46
        - Population: 22
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 65
        - FoodStored: 1113
        - FoodPerTurn: 37
        - ProductionPerTurn: 276
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 135
        - SciencePerTurn: 188
        - CulturePerTurn: 148
        - FaithPerTurn: 29
        - TourismPerTurn: 61.5
        - HappinessDelta: 8
        - BuildingCount: 49
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Hospital
          - Factory
          - Stock Exchange
          - Public School
          - Constabulary
          - Writers' Guild
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
        - Wonders:
          - Angkor Wat
          - Machu Picchu
          - Grand Temple
        - GreatWorkCount: 2
        
        ### Utique
        - ID: 3363
        - X: 25
        - Y: 39
        - Population: 25
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 94
        - IsOccupied: true
        - FoodStored: 774
        - FoodPerTurn: 32
        - ProductionPerTurn: 272
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 163
        - SciencePerTurn: 224
        - CulturePerTurn: 117
        - FaithPerTurn: 20
        - TourismPerTurn: 67.75
        - HappinessDelta: 3
        - BuildingCount: 51
        - ImportantBuildings:
          - Courthouse
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Hospital
          - Factory
          - Stock Exchange
          - Public School
          - Constabulary
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
        - GreatWorkCount: 2
        
        ### Hippo Regius
        - ID: 6999
        - X: 29
        - Y: 35
        - Population: 24
        - MajorityReligion: Islam
        - DefenseStrength: 65
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 668
        - FoodPerTurn: 15
        - ProductionPerTurn: 293
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 173
        - SciencePerTurn: 225
        - CulturePerTurn: 114
        - FaithPerTurn: 14
        - TourismPerTurn: 43.75
        - HappinessDelta: 1
        - BuildingCount: 56
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Stable
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Hospital
          - Factory
          - Stock Exchange
          - Public School
          - Constabulary
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Airport
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Mine Field
        - Wonders:
          - Kremlin
        - GreatWorkCount: 0
        
        ### Carthage
        - ID: 7854
        - X: 23
        - Y: 34
        - Population: 23
        - MajorityReligion: Islam
        - DefenseStrength: 92
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 827
        - FoodPerTurn: 8
        - ProductionPerTurn: 296
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 175
        - SciencePerTurn: 204
        - CulturePerTurn: 88
        - FaithPerTurn: 16
        - TourismPerTurn: 35.5
        - HappinessDelta: 8
        - BuildingCount: 55
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Hospital
          - Factory
          - Stock Exchange
          - Public School
          - Constabulary
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Coaling Station
          - Wire Service
          - Mine Field
        - Wonders:
          - Stonehenge
          - Pyramids
        - GreatWorkCount: 0
        
        ### Shushan
        - ID: 8484
        - X: 27
        - Y: 27
        - Population: 21
        - DefenseStrength: 96
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 865
        - FoodPerTurn: 12
        - ProductionPerTurn: 191
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 184
        - SciencePerTurn: 204
        - CulturePerTurn: 75
        - FaithPerTurn: 13
        - TourismPerTurn: 37.75
        - HappinessDelta: 2
        - BuildingCount: 56
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Hospital
          - Factory
          - Stock Exchange
          - Public School
          - Constabulary
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Wire Service
          - Mine Field
        - GreatWorkCount: 0
        
        ### Sippar
        - ID: 10621
        - X: 45
        - Y: 24
        - Population: 18
        - DefenseStrength: 88
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 479
        - FoodPerTurn: 8
        - ProductionStored: 0
        - ProductionPerTurn: 201
        - CurrentProduction: Observatory
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 91
        - SciencePerTurn: 109
        - CulturePerTurn: 59
        - FaithPerTurn: 7
        - TourismPerTurn: 20.25
        - HappinessDelta: -3
        - BuildingCount: 48
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Windmill
          - Customs House
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Hospital
          - Workshop
          - Stock Exchange
          - Public School
          - Constabulary
          - Hotel
          - Caravansary
          - Wire Service
        - GreatWorkCount: 0
        
        ### Opis
        - ID: 10817
        - X: 45
        - Y: 18
        - Population: 15
        - MajorityReligion: Catholicism
        - DefenseStrength: 96
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 489
        - FoodPerTurn: 0
        - ProductionStored: 0
        - ProductionPerTurn: 142
        - CurrentProduction: Gallery
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 106
        - SciencePerTurn: 73
        - CulturePerTurn: 41
        - FaithPerTurn: 8
        - TourismPerTurn: 3.75
        - HappinessDelta: -8
        - BuildingCount: 37
        - ImportantBuildings:
          - Courthouse
          - Windmill
          - Customs House
          - Garden
          - Harbor
          - Zoo
          - Armory
          - Military Base
          - Hospital
          - Workshop
          - Stock Exchange
          - Public School
          - Shrine
          - Caravansary
          - Chancery
          - Gymnasion
        - GreatWorkCount: 0
        
        ### Borsippa
        - ID: 11110
        - X: 48
        - Y: 17
        - Population: 18
        - MajorityReligion: Catholicism
        - DefenseStrength: 106
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 424
        - FoodPerTurn: 5
        - ProductionStored: 298
        - ProductionPerTurn: 188
        - CurrentProduction: Constabulary
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 103
        - SciencePerTurn: 99
        - CulturePerTurn: 51
        - FaithPerTurn: 14
        - TourismPerTurn: 9
        - HappinessDelta: -9
        - BuildingCount: 42
        - ImportantBuildings:
          - Courthouse
          - Water Mill
          - Windmill
          - Customs House
          - Harbor
          - Zoo
          - Temple
          - Opera House
          - Museum
          - Armory
          - Military Base
          - Hospital
          - Workshop
          - Stock Exchange
          - Public School
          - Caravansary
          - Bath
          - Chancery
        - GreatWorkCount: 0
        
        ### Jenne
        - ID: 12645
        - X: 48
        - Y: 6
        - Population: 18
        - MajorityReligion: Buddhism
        - DefenseStrength: 73
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 544
        - FoodPerTurn: 7
        - ProductionStored: 1151
        - ProductionPerTurn: 278
        - CurrentProduction: Broadcast Tower
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 136
        - SciencePerTurn: 102
        - CulturePerTurn: 66
        - FaithPerTurn: 21
        - TourismPerTurn: 12.75
        - HappinessDelta: 1
        - BuildingCount: 51
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Windmill
          - Customs House
          - Garden
          - Zoo
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Military Base
          - Hospital
          - Workshop
          - Stock Exchange
          - Public School
          - Constabulary
          - Hotel
          - Caravansary
          - Airport
          - Coaling Station
          - Wire Service
          - Mine Field
        - GreatWorkCount: 0
        
        ### Knossos
        - ID: 13214
        - X: 31
        - Y: 23
        - Population: 16
        - MajorityReligion: Islam
        - DefenseStrength: 96
        - IsCoastal: true
        - FoodStored: 523
        - FoodPerTurn: 22
        - ProductionStored: 316
        - ProductionPerTurn: 226
        - CurrentProduction: Military Academy
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 122
        - SciencePerTurn: 90
        - CulturePerTurn: 47
        - FaithPerTurn: 12
        - TourismPerTurn: 18
        - HappinessDelta: -4
        - BuildingCount: 39
        - ImportantBuildings:
          - Windmill
          - Customs House
          - Harbor
          - Zoo
          - Temple
          - Armory
          - Military Base
          - Hospital
          - Workshop
          - Stock Exchange
          - Public School
          - Constabulary
          - Caravansary
          - Wire Service
          - Gymnasion
        - GreatWorkCount: 0
        
        ### Tombouctu
        - ID: 13487
        - X: 53
        - Y: 6
        - Population: 18
        - MajorityReligion: Buddhism
        - DefenseStrength: 102
        - IsOccupied: true
        - FoodStored: 713
        - FoodPerTurn: 58
        - ProductionStored: 1177
        - ProductionPerTurn: 291
        - CurrentProduction: Wire Service
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 198
        - SciencePerTurn: 140
        - CulturePerTurn: 68
        - FaithPerTurn: 29
        - TourismPerTurn: 25
        - BuildingCount: 48
        - ImportantBuildings:
          - Courthouse
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Military Base
          - Hospital
          - Factory
          - Stock Exchange
          - Public School
          - Constabulary
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Chancery
        - GreatWorkCount: 0
        
        ### Awasa
        - ID: 14195
        - X: 24
        - Y: 21
        - Population: 14
        - MajorityReligion: Islam
        - DefenseStrength: 98
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 216
        - FoodPerTurn: 4
        - ProductionStored: 0
        - ProductionPerTurn: 232
        - CurrentProduction: Zoo
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 97
        - SciencePerTurn: 75
        - CulturePerTurn: 31
        - FaithPerTurn: 14
        - TourismPerTurn: 5.75
        - HappinessDelta: -4
        - BuildingCount: 41
        - ImportantBuildings:
          - Courthouse
          - Circus
          - Windmill
          - Customs House
          - Garden
          - Harbor
          - Temple
          - Opera House
          - Armory
          - Military Base
          - Hospital
          - Workshop
          - Stock Exchange
          - Public School
          - Hotel
          - Caravansary
          - Chancery
          - Gallery
        - GreatWorkCount: 0
        
        ### Gao
        - ID: 15451
        - X: 57
        - Y: 4
        - Population: 18
        - MajorityReligion: Buddhism
        - DefenseStrength: 95
        - IsOccupied: true
        - FoodStored: 369
        - FoodPerTurn: 7
        - ProductionStored: 0
        - ProductionPerTurn: 378
        - CurrentProduction: Bank
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 62
        - SciencePerTurn: 69
        - CulturePerTurn: 97
        - FaithPerTurn: 52
        - TourismPerTurn: 43.25
        - HappinessDelta: -4
        - BuildingCount: 41
        - ImportantBuildings:
          - Courthouse
          - Stable
          - Water Mill
          - Circus
          - Windmill
          - Customs House
          - Garden
          - Temple
          - Opera House
          - Museum
          - Barracks
          - Military Base
          - Hospital
          - Factory
          - University
          - Constabulary
          - Hotel
          - Chancery
          - Agribusiness
          - Coaling Station
        - Wonders:
          - Alhambra
          - Karlstejn
          - Grand Canal
        - GreatWorkCount: 0
        
        ## Player: Ethiopia
        
        ### Addis Ababa
        - ID: 1064
        - X: 13
        - Y: 39
        - Population: 34
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 67
        - Wonders:
          - Royal Collection
          - Hanging Gardens
          - Hagia Sophia
          - Porcelain Tower
          - Sistine Chapel
          - Petra
          - Borobudur
          - Palace of Culture and Science
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
          - Celestial Throne
          - Trader Sid's Headquarters
        
        ### Harar
        - ID: 1187
        - X: 17
        - Y: 37
        - Population: 20
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 61
        - Health: 46%
        - Wonders:
          - School of Philosophy
          - Imperial College
          - Taj Mahal
          - Scrivener's Office
          - Printing Press
          - Empire State Building
        
        ### Adwa
        - ID: 1328
        - X: 10
        - Y: 43
        - Population: 23
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 72
        - Wonders:
          - Heroic Epic
          - National Monument
          - Circus Maximus
          - Chartered Company
          - Grand Temple
        
        ### Lalibela
        - ID: 1995
        - X: 8
        - Y: 38
        - Population: 23
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 65
        - IsCoastal: true
        - Wonders:
          - Ironworks
          - Nalanda
        
        ### Gondar
        - ID: 2712
        - X: 4
        - Y: 40
        - Population: 23
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 70
        - Health: 99%
        - IsCoastal: true
        
        ### Axum
        - ID: 3454
        - X: 4
        - Y: 45
        - Population: 23
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 66
        - Health: 98%
        - IsCoastal: true
        - Wonders:
          - Globe Theatre
        
        ### Dire Dawa
        - ID: 7474
        - X: 18
        - Y: 26
        - Population: 19
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 68
        - IsCoastal: true
        
        ### Bahir Dar
        - ID: 7902
        - X: 13
        - Y: 25
        - Population: 19
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 72
        - Health: 99%
        - IsCoastal: true
        
        ### Adama
        - ID: 8536
        - X: 11
        - Y: 21
        - Population: 19
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 65
        - Health: 98%
        - IsCoastal: true
        
        ### Mek'ele
        - ID: 8573
        - X: 15
        - Y: 19
        - Population: 18
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 72
        - IsCoastal: true
        - ResistanceTurns: 1
        
        ## Player: City-States
        
        ### Riga
        - ID: 1065
        - X: 69
        - Y: 5
        - Population: 21
        - MajorityReligion: Buddhism
        - DefenseStrength: 100
        - IsCoastal: true
        
        ### Monaco
        - ID: 12340
        - X: 47
        - Y: 11
        - Population: 14
        - MajorityReligion: Buddhism
        - DefenseStrength: 83
        - IsCoastal: true
        
        ### Salem
        - ID: 3811
        - X: 65
        - Y: 9
        - Population: 16
        - MajorityReligion: Buddhism
        - DefenseStrength: 97
        - IsCoastal: true
        
        ### Zurich
        - ID: 1068
        - X: 16
        - Y: 31
        - Population: 20
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 103
        - IsCoastal: true
        
        ### Manila
        - ID: 1069
        - X: 32
        - Y: 40
        - Population: 22
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 91
        - IsCoastal: true
        
        ### Copenhagen
        - ID: 1070
        - X: 21
        - Y: 41
        - Population: 9
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 91
        
        ### Veligrad
        - ID: 1071
        - X: 46
        - Y: 34
        - Population: 26
        - MajorityReligion: Tengriism
        - DefenseStrength: 96
        - IsCoastal: true
        
        ### Wanggeom
        - ID: 1072
        - X: 65
        - Y: 48
        - Population: 21
        - MajorityReligion: Tengriism
        - DefenseStrength: 92
        - IsCoastal: true
        
        ### Abernethy
        - ID: 1073
        - X: 24
        - Y: 15
        - Population: 22
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 82
        - IsCoastal: true
        
        ### Hanoi
        - ID: 1074
        - X: 43
        - Y: 43
        - Population: 26
        - MajorityReligion: Tengriism
        - DefenseStrength: 94
        - IsCoastal: true
        
        ### Vatican City
        - ID: 1075
        - X: 9
        - Y: 15
        - Population: 25
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 101
        - IsCoastal: true
        
        ### Budapest
        - ID: 1076
        - X: 31
        - Y: 17
        - Population: 22
        - DefenseStrength: 80
        - IsCoastal: true
        
        ### Buenos Aires
        - ID: 1077
        - X: 9
        - Y: 49
        - Population: 14
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 91
        
        ### Antananarivo
        - ID: 1078
        - X: 19
        - Y: 47
        - Population: 8
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 90
        
        ### Almaty
        - ID: 1079
        - X: 59
        - Y: 49
        - Population: 11
        - MajorityReligion: Tengriism
        - DefenseStrength: 81
        
        ### Antwerp
        - ID: 1080
        - X: 55
        - Y: 35
        - Population: 28
        - MajorityReligion: Tengriism
        - DefenseStrength: 100
        - IsCoastal: true
        
        # Military
        Military: summary reports about tactical zones and visible units.
        
        ## Unit Stats
        - Attack:
          - Foreign Legion:
            - Strength: 40
        - CityBombard:
          - Artillery:
            - Strength: 27
            - RangedStrength: 50
          - Field Gun:
            - Strength: 17
            - RangedStrength: 40
        - FastAttack:
          - Tank:
            - Strength: 75
          - T-34:
            - Strength: 82
          - Landship:
            - Strength: 60
          - Commando:
            - Strength: 32
        - Defense:
          - Infantry:
            - Strength: 62
          - Fusilier:
            - Strength: 38
          - Rifleman:
            - Strength: 50
        - Counter:
          - Anti-Aircraft Gun:
            - Strength: 40
        - Ranged:
          - Light Tank:
            - Strength: 58
            - RangedStrength: 52
          - Cavalry:
            - Strength: 40
            - RangedStrength: 31
          - Machine Gun:
            - Strength: 45
            - RangedStrength: 58
          - Gatling Gun:
            - Strength: 32
            - RangedStrength: 44
        - AttackSea:
          - Destroyer:
            - Strength: 70
          - Ironclad:
            - Strength: 55
        - AssaultSea:
          - Cruiser:
            - Strength: 40
            - RangedStrength: 55
          - Dreadnought:
            - Strength: 50
            - RangedStrength: 65
        - AttackAir:
          - Heavy Bomber:
            - RangedStrength: 65
          - Bomber:
            - RangedStrength: 50
        - DefenseAir:
          - Jet Fighter:
            - RangedStrength: 70
          - Fighter:
            - RangedStrength: 60
          - Triplane:
            - RangedStrength: 45
        - Paradrop:
          - Paratrooper:
            - Strength: 42
        
        ## Neutral Land Zone 1058
        - ZoneValue: 24
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 674
        - NeutralStrength: 246
        - FriendlyStrength: 2893
        - City: Babylon
        - AreaID: 3
        - Plots: 21
        - CenterX: 54
        - CenterY: 13
        - Units:
          - Greece:
            - Light Tank: 1
          - Babylon:
            - Field Gun: 1
        - Neighbors:
          - 11110
          - 1293
          - 13487
          - 2265
          - 1776
        
        ## Friendly Land Zone 1063
        - ZoneValue: 60
        - Dominance: Friendly
        - FriendlyStrength: 1301
        - City: Athens
        - AreaID: 77
        - Plots: 19
        - CenterX: 27
        - CenterY: 48
        - Units:
          - Greece:
            - Heavy Bomber: 1
        - Neighbors:
          - 1584
          - 1342
          - 1181
        
        ## Enemy Land Zone 1064
        - ZoneValue: 48
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 1231
        - NeutralStrength: 202
        - FriendlyStrength: 1697
        - City: Addis Ababa
        - AreaID: 81
        - Plots: 29
        - CenterX: 13
        - CenterY: 39
        - Units:
          - Ethiopia:
            - Anti-Aircraft Gun: 2
        - Neighbors:
          - 1068
          - 1187
          - 1078
          - 1070
        
        ## Neutral Land Zone 1065
        - ZoneValue: 30
        - Dominance: Friendly
        - NeutralStrength: 220
        - FriendlyStrength: 1103
        - City: Riga
        - AreaID: 3
        - Plots: 19
        - CenterX: 68
        - CenterY: 4
        - Units:
          - City-State Riga:
            - Bomber: 1
            - Machine Gun: 1
        - Neighbors:
          - 2885
          - -1065
        
        ## Neutral Land Zone 1068
        - ZoneValue: 3
        - Dominance: Friendly
        - Posture: Exploit Flanks
        - EnemyStrength: 613
        - NeutralStrength: 596
        - FriendlyStrength: 1364
        - City: Zurich
        - AreaID: 37
        - Plots: 21
        - CenterX: 16
        - CenterY: 33
        - Units:
          - Carthage:
            - Landship: 1
          - City-State Zurich:
            - Destroyer: 1
            - Tank: 1
            - Light Tank: 1
            - Machine Gun: 3
          - Greece:
            - Anti-Aircraft Gun: 2
            - Machine Gun: 1
        - Neighbors:
          - -1068
          - 1064
          - 7902
          - 1187
          - 7854
        
        ## Neutral Land Zone 1069
        - ZoneValue: 24
        - Dominance: Friendly
        - NeutralStrength: 91
        - FriendlyStrength: 2527
        - City: Manila
        - AreaID: 77
        - Plots: 14
        - CenterX: 31
        - CenterY: 40
        - Units:
          - City-State Manila:
            - Artillery: 1
            - Infantry: 3
            - Machine Gun: 1
          - Greece:
            - Artillery: 2
        - Neighbors:
          - 3363
          - 6999
          - 1342
        
        ## Neutral Land Zone 1070
        - ZoneValue: 24
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 354
        - NeutralStrength: 91
        - FriendlyStrength: 4217
        - City: Copenhagen
        - AreaID: 77
        - Plots: 36
        - CenterX: 21
        - CenterY: 41
        - Units:
          - City-State Copenhagen:
            - Artillery: 1
            - Machine Gun: 2
          - City-State Antananarivo:
            - Infantry: 1
        - Neighbors:
          - 1187
          - 1064
          - 1078
          - 7854
          - 3363
          - 1584
        
        ## Enemy Land Zone 1071
        - ZoneValue: 12
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 2200
        - FriendlyStrength: 87
        - City: Veligrad
        - AreaID: 85
        - Plots: 14
        - CenterX: 46
        - CenterY: 35
        - Units:
          - City-State Veligrad:
            - Machine Gun: 1
        - Neighbors:
          - -1071
        
        ## Neutral Land Zone 1073
        - ZoneValue: 15
        - Dominance: Friendly
        - NeutralStrength: 1007
        - FriendlyStrength: 536
        - City: Abernethy
        - AreaID: 6
        - Plots: 25
        - CenterX: 26
        - CenterY: 14
        - Units:
          - Barbarians:
            - Rifleman: 1
          - City-State Abernethy:
            - Infantry: 3
          - Greece:
            - Machine Gun: 1
        - Neighbors:
          - 14195
          - 9435
          - 1076
          - -1076
        
        ## Enemy Land Zone 1075
        - ZoneValue: 12
        - Dominance: Enemy
        - EnemyStrength: 1176
        - City: Vatican City
        - AreaID: 22
        - Plots: 10
        - CenterX: 9
        - CenterY: 16
        - Units:
          - City-State Vatican City:
            - Infantry: 1
        - Neighbors:
          - 8536
          - 8573
        
        ## Neutral Land Zone 1076
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 763
        - FriendlyStrength: 687
        - City: Budapest
        - AreaID: 6
        - Plots: 27
        - CenterX: 31
        - CenterY: 17
        - Units:
          - City-State Budapest:
            - Infantry: 1
            - Machine Gun: 3
          - Greece:
            - Paratrooper: 1
        - Neighbors:
          - 14195
          - 1073
          - -1076
          - 13214
          - -13974
          - -13214
          - -100005
        
        ## Neutral Land Zone 1078
        - ZoneValue: 24
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 143
        - NeutralStrength: 91
        - FriendlyStrength: 3455
        - City: Antananarivo
        - AreaID: 77
        - Plots: 51
        - CenterX: 18
        - CenterY: 47
        - Units:
          - City-State Antananarivo:
            - Light Tank: 2
            - Infantry: 3
            - Machine Gun: 3
          - City-State Copenhagen:
            - Machine Gun: 1
          - Greece:
            - Infantry: 1
            - Machine Gun: 1
        - Neighbors:
          - 1064
          - 100009
          - 1070
          - 1584
        
        ## Enemy Land Zone 1080
        - ZoneValue: 12
        - Dominance: Enemy
        - EnemyStrength: 2402
        - NeutralStrength: 918
        - City: Antwerp
        - AreaID: 86
        - Plots: 26
        - CenterX: 55
        - CenterY: 37
        - Units:
          - City-State Antwerp:
            - Infantry: 1
        - Neighbors:
          - -1080
        
        ## Friendly Land Zone 1181
        - ZoneValue: 42
        - Dominance: Friendly
        - FriendlyStrength: 1474
        - City: Sparta
        - AreaID: 77
        - Plots: 15
        - CenterX: 30
        - CenterY: 47
        - Units:
          - Greece:
            - Machine Gun: 1
        - Neighbors:
          - 1063
          - 1342
        
        ## Enemy Land Zone 1187
        - ZoneValue: 10752
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 790
        - NeutralStrength: 389
        - FriendlyStrength: 3249
        - City: Harar
        - AreaID: 77
        - Plots: 30
        - CenterX: 17
        - CenterY: 37
        - Units:
          - Ethiopia:
            - Paratrooper: 1
            - Anti-Aircraft Gun: 1
            - Triplane: 1
          - Greece:
            - T-34: 1
            - Anti-Aircraft Gun: 1
            - Infantry: 1
            - Machine Gun: 2
        - Neighbors:
          - 1068
          - 1064
          - 1070
          - 7854
        
        ## Neutral Land Zone 1293
        - ZoneValue: 30
        - Dominance: Friendly
        - NeutralStrength: 51
        - FriendlyStrength: 3731
        - City: Dur-Kurigalzu
        - AreaID: 3
        - Plots: 17
        - CenterX: 51
        - CenterY: 11
        - Units:
          - Babylon:
            - Gatling Gun: 3
            - Field Gun: 1
        - Neighbors:
          - 12340
          - -12340
          - 12645
          - 13487
          - 1058
        
        ## Friendly Land Zone 1342
        - ZoneValue: 48
        - Dominance: Friendly
        - FriendlyStrength: 3200
        - City: Corinth
        - AreaID: 77
        - Plots: 17
        - CenterX: 28
        - CenterY: 42
        - Units:
          - Greece:
            - Bomber: 2
        - Neighbors:
          - 3363
          - 1584
          - 1063
          - 1069
          - 1181
        
        ## Friendly Land Zone 1584
        - ZoneValue: 42
        - Dominance: Friendly
        - FriendlyStrength: 2973
        - City: Argos
        - AreaID: 77
        - Plots: 29
        - CenterX: 24
        - CenterY: 47
        - Units:
          - Greece:
            - Fighter: 1
        - Neighbors:
          - 1078
          - 1070
          - 3363
          - 1342
          - 1063
        
        ## Enemy Land Zone 1776
        - ZoneValue: 8064
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 1727
        - NeutralStrength: 236
        - FriendlyStrength: 3639
        - City: Taghaza
        - AreaID: 3
        - Plots: 27
        - CenterX: 59
        - CenterY: 9
        - Units:
          - Greece:
            - T-34: 1
            - Infantry: 1
            - Machine Gun: 1
          - Songhai:
            - Jet Fighter: 2
            - Machine Gun: 1
        - Neighbors:
          - 13487
          - 15451
          - 1058
          - 2265
          - 2885
          - 3862
        
        ## Enemy Land Zone 2265
        - ZoneValue: 288
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 1386
        - NeutralStrength: 314
        - FriendlyStrength: 1595
        - City: Tondibi
        - AreaID: 3
        - Plots: 18
        - CenterX: 58
        - CenterY: 14
        - Units:
          - Babylon:
            - Rifleman: 1
          - Songhai:
            - Artillery: 1
        - Neighbors:
          - 1058
          - 1776
          - 3862
        
        ## Enemy Land Zone 2712
        - ZoneValue: 12
        - Dominance: Enemy
        - EnemyStrength: 439
        - City: Gondar
        - AreaID: 87
        - Plots: 18
        - CenterX: 4
        - CenterY: 40
        - Units:
          - Barbarians:
            - Machine Gun: 2
          - Ethiopia:
            - Machine Gun: 1
        - Neighbors:
          - 3454
        
        ## Enemy Land Zone 2885
        - ZoneValue: 6912
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 777
        - NeutralStrength: 50
        - FriendlyStrength: 3204
        - City: Kumbi Saleh
        - AreaID: 3
        - Plots: 28
        - CenterX: 62
        - CenterY: 4
        - Units:
          - City-State Riga:
            - Tank: 1
            - Infantry: 1
            - Machine Gun: 1
          - Songhai:
            - Machine Gun: 1
        - Neighbors:
          - 15451
          - 1776
          - 1065
        
        ## Friendly Land Zone 3363
        - ZoneValue: 42
        - Dominance: Friendly
        - FriendlyStrength: 3919
        - City: Utique
        - AreaID: 77
        - Plots: 22
        - CenterX: 25
        - CenterY: 39
        - Units:
          - Greece:
            - Triplane: 1
            - Machine Gun: 1
        - Neighbors:
          - 1070
          - 7854
          - 1584
          - 1342
          - 6999
          - 1069
        
        ## Enemy Land Zone 3454
        - ZoneValue: 120
        - Dominance: Enemy
        - EnemyStrength: 730
        - City: Axum
        - AreaID: 94
        - Plots: 31
        - CenterX: 5
        - CenterY: 46
        - Units:
          - Barbarians:
            - Rifleman: 1
            - Machine Gun: 6
          - Ethiopia:
            - Artillery: 1
        - Neighbors:
          - 2712
        
        ## Enemy Land Zone 3862
        - ZoneValue: 288
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 1570
        - NeutralStrength: 256
        - FriendlyStrength: 1314
        - City: Kukia
        - AreaID: 3
        - Plots: 12
        - CenterX: 61
        - CenterY: 11
        - Units:
          - Songhai:
            - Light Tank: 1
            - Foreign Legion: 1
            - Machine Gun: 1
        - Neighbors:
          - 1776
          - 2265
        
        ## Friendly Land Zone 6999
        - ZoneValue: 3
        - Dominance: Friendly
        - FriendlyStrength: 3814
        - City: Hippo Regius
        - AreaID: 78
        - Plots: 29
        - CenterX: 29
        - CenterY: 35
        - Units:
          - City-State Manila:
            - Machine Gun: 1
          - Greece:
            - Artillery: 1
            - Anti-Aircraft Gun: 1
            - Light Tank: 1
        - Neighbors:
          - 7854
          - 3363
          - 8484
          - -2518
          - 1069
        
        ## Friendly Land Zone 7854
        - ZoneValue: 3
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 104
        - NeutralStrength: 37
        - FriendlyStrength: 2880
        - City: Carthage
        - AreaID: 78
        - Plots: 28
        - CenterX: 23
        - CenterY: 35
        - Units:
          - Greece:
            - Heavy Bomber: 1
            - Fighter: 2
            - Artillery: 1
            - Triplane: 3
        - Neighbors:
          - 1068
          - 1187
          - -1068
          - 1070
          - 3363
          - 6999
          - 8484
        
        ## Enemy Land Zone 7902
        - ZoneValue: 120
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 992
        - NeutralStrength: 169
        - FriendlyStrength: 36
        - City: Bahir Dar
        - AreaID: 37
        - Plots: 16
        - CenterX: 14
        - CenterY: 25
        - Units:
          - Ethiopia:
            - Artillery: 1
            - Infantry: 1
            - Machine Gun: 1
          - Barbarians:
            - Machine Gun: 1
          - Greece:
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - 8536
          - 8573
          - 1068
          - -1068
        
        ## Friendly Land Zone 8484
        - ZoneValue: 42
        - Dominance: Friendly
        - FriendlyStrength: 2378
        - City: Shushan
        - AreaID: 6
        - Plots: 14
        - CenterX: 28
        - CenterY: 27
        - Units:
          - Carthage:
            - Gatling Gun: 1
          - Greece:
            - Heavy Bomber: 1
            - Infantry: 1
        - Neighbors:
          - -8484
          - 14195
          - 7854
          - 6999
          - 13214
          - -13214
          - -2518
        
        ## Enemy Land Zone 8536
        - ZoneValue: 48
        - Dominance: Enemy
        - EnemyStrength: 1336
        - City: Adama
        - AreaID: 37
        - Plots: 16
        - CenterX: 11
        - CenterY: 20
        - Units:
          - Barbarians:
            - Machine Gun: 2
        - Neighbors:
          - 1075
          - 8573
          - 7902
        
        ## Enemy Land Zone 8573
        - ZoneValue: 12
        - Dominance: Enemy
        - EnemyStrength: 1039
        - City: Mek'ele
        - AreaID: 45
        - Plots: 23
        - CenterX: 15
        - CenterY: 20
        - Units:
          - Barbarians:
            - Rifleman: 2
            - Machine Gun: 3
          - Ethiopia:
            - Infantry: 1
        - Neighbors:
          - 1075
          - 8536
          - -8573
          - 7902
          - -7474
        
        ## Enemy Land Zone 9435
        - ZoneValue: 96
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 557
        - NeutralStrength: 68
        - FriendlyStrength: 1130
        - City: Tegdaoust
        - AreaID: 4
        - Plots: 28
        - CenterX: 28
        - CenterY: 7
        - Units:
          - Greece:
            - Machine Gun: 1
          - Songhai:
            - Paratrooper: 1
        - Neighbors:
          - 1073
          - -13974
          - 13974
        
        ## Friendly Land Zone 10621
        - ZoneValue: 36
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 92
        - FriendlyStrength: 1755
        - City: Sippar
        - AreaID: 58
        - Plots: 9
        - CenterX: 44
        - CenterY: 25
        - Units:
          - Greece:
            - Paratrooper: 1
            - Machine Gun: 1
        - Neighbors:
          - -10621
          - -1071
        
        ## Friendly Land Zone 10817
        - ZoneValue: 30
        - Dominance: Friendly
        - FriendlyStrength: 1960
        - City: Opis
        - AreaID: 34
        - Plots: 9
        - CenterX: 45
        - CenterY: 17
        - Units:
          - Greece:
            - Paratrooper: 1
            - Infantry: 1
        - Neighbors:
          - -12340
          - 11110
        
        ## Friendly Land Zone 11110
        - ZoneValue: 36
        - Dominance: Friendly
        - FriendlyStrength: 2323
        - City: Borsippa
        - AreaID: 34
        - Plots: 14
        - CenterX: 48
        - CenterY: 16
        - Units:
          - Greece:
            - T-34: 1
            - Artillery: 2
          - Babylon:
            - Commando: 1
        - Neighbors:
          - 10817
          - 12340
          - 1058
        
        ## Neutral Land Zone 12340
        - ZoneValue: 24
        - Dominance: Friendly
        - NeutralStrength: 84
        - FriendlyStrength: 2706
        - City: Monaco
        - AreaID: 3
        - Plots: 11
        - CenterX: 48
        - CenterY: 11
        - Units:
          - City-State Monaco:
            - Tank: 1
        - Neighbors:
          - -12340
          - 11110
          - 12645
          - 1293
        
        ## Friendly Land Zone 12645
        - ZoneValue: 42
        - Dominance: Friendly
        - FriendlyStrength: 1752
        - City: Jenne
        - AreaID: 3
        - Plots: 17
        - CenterX: 49
        - CenterY: 6
        - Units:
          - Babylon:
            - Gatling Gun: 1
        - Neighbors:
          - -12340
          - 12340
          - 13487
          - 1293
        
        ## Friendly Land Zone 13214
        - ZoneValue: 36
        - Dominance: Friendly
        - NeutralStrength: 214
        - FriendlyStrength: 1314
        - City: Knossos
        - AreaID: 6
        - Plots: 27
        - CenterX: 32
        - CenterY: 23
        - Units:
          - Greece:
            - Infantry: 1
        - Neighbors:
          - 14195
          - 8484
          - 1076
          - -13214
          - -1076
          - -2518
          - -100005
        
        ## Friendly Land Zone 13487
        - ZoneValue: 42
        - Dominance: Friendly
        - FriendlyStrength: 3450
        - City: Tombouctu
        - AreaID: 3
        - Plots: 34
        - CenterX: 52
        - CenterY: 6
        - Units:
          - Greece:
            - Light Tank: 1
            - Infantry: 2
          - Babylon:
            - Gatling Gun: 4
        - Neighbors:
          - 12645
          - 1293
          - 15451
          - 1776
          - 1058
        
        ## Neutral Land Zone 13974
        - ZoneValue: 24
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 193
        - NeutralStrength: 100
        - FriendlyStrength: 1588
        - City: Gwandu
        - AreaID: 2
        - Plots: 18
        - CenterX: 33
        - CenterY: 6
        - Units:
          - Barbarians:
            - Rifleman: 1
          - Greece:
            - Infantry: 1
            - Machine Gun: 1
          - Babylon:
            - Cavalry: 1
            - Gatling Gun: 3
            - Field Gun: 1
        - Neighbors:
          - 9435
          - -13974
        
        ## Friendly Land Zone 14195
        - ZoneValue: 36
        - Dominance: Friendly
        - NeutralStrength: 543
        - FriendlyStrength: 1230
        - City: Awasa
        - AreaID: 6
        - Plots: 20
        - CenterX: 26
        - CenterY: 21
        - Units:
          - Greece:
            - Artillery: 1
            - Infantry: 1
        - Neighbors:
          - -14195
          - 1073
          - 8484
          - 1076
          - 13214
        
        ## Friendly Land Zone 15451
        - ZoneValue: 42
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 613
        - FriendlyStrength: 3688
        - City: Gao
        - AreaID: 3
        - Plots: 17
        - CenterX: 56
        - CenterY: 4
        - Units:
          - Greece:
            - Heavy Bomber: 1
            - Fighter: 1
            - Paratrooper: 1
            - Tank: 1
            - Machine Gun: 1
        - Neighbors:
          - 13487
          - 1776
          - 2885
        
        ## Neutral Land Zone 100009
        - ZoneValue: 3
        - AreaID: 77
        - Plots: 1
        - CenterX: 15
        - CenterY: 50
        - Units:
          - Greece:
            - Machine Gun: 1
        - Neighbors:
          - 1078
        
        ## Neutral Sea Zone -100005
        - ZoneValue: 1
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 318
        - FriendlyStrength: 319
        - AreaID: 0
        - Plots: 161
        - CenterX: 38
        - CenterY: 33
        - Units:
          - Carthage:
            - Cavalry: 1
            - Cruiser: 1
          - Mongolia:
            - Machine Gun: 1
          - City-State Veligrad:
            - Destroyer: 1
        - Neighbors:
          - -1076
          - 1076
          - 13214
          - -13214
          - -2518
          - -13974
          - -10621
          - -1071
        
        ## Friendly Sea Zone -8484
        - ZoneValue: 14
        - Dominance: Friendly
        - FriendlyStrength: 2652
        - City: Shushan
        - AreaID: 0
        - Plots: 30
        - CenterX: 26
        - CenterY: 28
        - Units:
          - Carthage:
            - Fusilier: 1
            - Rifleman: 1
            - Field Gun: 1
          - Greece:
            - Destroyer: 1
            - Ironclad: 1
            - Dreadnought: 3
        - Neighbors:
          - -7474
          - -14195
          - 8484
          - -2518
          - -13214
        
        ## Friendly Sea Zone -13214
        - ZoneValue: 1
        - Dominance: Friendly
        - NeutralStrength: 511
        - FriendlyStrength: 1256
        - City: Knossos
        - AreaID: 0
        - Plots: 21
        - CenterX: 33
        - CenterY: 24
        - Units:
          - City-State Budapest:
            - Destroyer: 1
        - Neighbors:
          - 8484
          - 13214
          - -8484
          - -1076
          - -2518
          - 1076
          - -100005
        
        ## Neutral Sea Zone -2518
        - ZoneValue: 8
        - Dominance: Friendly
        - NeutralStrength: 62
        - FriendlyStrength: 2278
        - City: Gades
        - AreaID: 0
        - Plots: 39
        - CenterX: 34
        - CenterY: 31
        - Units:
          - Carthage:
            - Ironclad: 1
            - Gatling Gun: 1
        - Neighbors:
          - 8484
          - -8484
          - 6999
          - -13214
          - 13214
          - -100005
        
        ## Friendly Sea Zone -14195
        - ZoneValue: 12
        - Dominance: Friendly
        - NeutralStrength: 393
        - FriendlyStrength: 1157
        - City: Awasa
        - AreaID: 0
        - Plots: 27
        - CenterX: 23
        - CenterY: 22
        - Units:
          - Carthage:
            - Ironclad: 2
            - Rifleman: 1
            - Field Gun: 1
        - Neighbors:
          - -7474
          - -8573
          - 14195
          - -8484
        
        ## Neutral Sea Zone -1065
        - ZoneValue: 10
        - Dominance: Friendly
        - NeutralStrength: 223
        - FriendlyStrength: 876
        - City: Riga
        - AreaID: 0
        - Plots: 54
        - CenterX: 71
        - CenterY: 5
        - Units:
          - Japan:
            - Rifleman: 1
          - City-State Riga:
            - Destroyer: 1
        - Neighbors:
          - 1065
        
        ## Enemy Sea Zone -1071
        - ZoneValue: 4
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 2123
        - FriendlyStrength: 287
        - City: Veligrad
        - AreaID: 0
        - Plots: 55
        - CenterX: 45
        - CenterY: 33
        - Units:
          - City-State Veligrad:
            - Dreadnought: 1
          - Greece:
            - Dreadnought: 1
        - Neighbors:
          - -100005
          - -10621
          - 1071
          - 10621
          - -100007
        
        ## Neutral Sea Zone -1068
        - ZoneValue: 1
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 284
        - NeutralStrength: 466
        - FriendlyStrength: 332
        - City: Zurich
        - AreaID: 70
        - Plots: 28
        - CenterX: 15
        - CenterY: 30
        - Units:
          - Carthage:
            - Fusilier: 1
        - Neighbors:
          - 1068
          - 7902
          - -7474
          - 7854
        
        ## Neutral Sea Zone -13974
        - ZoneValue: 8
        - Dominance: Friendly
        - NeutralStrength: 169
        - FriendlyStrength: 1547
        - City: Gwandu
        - AreaID: 0
        - Plots: 48
        - CenterX: 34
        - CenterY: 8
        - Units:
          - Babylon:
            - Ironclad: 1
            - Cruiser: 1
            - Dreadnought: 2
        - Neighbors:
          - 9435
          - 1076
          - 13974
          - -1076
          - -100005
        
        ## Neutral Sea Zone -100007
        - ZoneValue: 1
        - Dominance: Friendly
        - FriendlyStrength: 333
        - AreaID: 0
        - Plots: 49
        - CenterX: 52
        - CenterY: 27
        - Units:
          - Greece:
            - Destroyer: 2
            - Dreadnought: 2
        - Neighbors:
          - -10621
          - -1071
          - -1080
        
        ## Enemy Sea Zone -8573
        - ZoneValue: 64
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 379
        - FriendlyStrength: 551
        - City: Mek'ele
        - AreaID: 0
        - Plots: 32
        - CenterX: 17
        - CenterY: 17
        - Units:
          - Greece:
            - Destroyer: 1
            - Ironclad: 2
        - Neighbors:
          - 8573
          - -7474
          - -14195
        
        ## Enemy Sea Zone -7474
        - ZoneValue: 160
        - Dominance: Even
        - Posture: Attrition
        - EnemyStrength: 389
        - NeutralStrength: 190
        - FriendlyStrength: 654
        - City: Dire Dawa
        - AreaID: 0
        - Plots: 32
        - CenterX: 20
        - CenterY: 26
        - Units:
          - Carthage:
            - Ironclad: 1
            - Fusilier: 1
            - Rifleman: 2
            - Cruiser: 1
        - Neighbors:
          - -1068
          - -8573
          - 8573
          - -14195
          - -8484
        
        ## Neutral Sea Zone -1076
        - ZoneValue: 8
        - Dominance: Friendly
        - NeutralStrength: 1049
        - FriendlyStrength: 349
        - City: Budapest
        - AreaID: 18
        - Plots: 36
        - CenterX: 32
        - CenterY: 16
        - Units:
          - City-State Budapest:
            - Destroyer: 3
        - Neighbors:
          - 1073
          - 1076
          - -13974
          - 13214
          - -13214
          - -100005
        
        ## Enemy Sea Zone -1080
        - ZoneValue: 4
        - Dominance: Enemy
        - EnemyStrength: 1870
        - NeutralStrength: 59
        - City: Antwerp
        - AreaID: 0
        - Plots: 26
        - CenterX: 54
        - CenterY: 32
        - Units:
          - City-State Antwerp:
            - Destroyer: 1
        - Neighbors:
          - -100007
          - 1080
        
        ## Neutral Sea Zone -12340
        - ZoneValue: 8
        - Dominance: Friendly
        - NeutralStrength: 84
        - FriendlyStrength: 1247
        - City: Monaco
        - AreaID: 0
        - Plots: 27
        - CenterX: 46
        - CenterY: 11
        - Units:
          - City-State Monaco:
            - Dreadnought: 1
        - Neighbors:
          - 10817
          - 12340
          - 12645
          - 1293
        
        ## Friendly Sea Zone -10621
        - ZoneValue: 12
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 275
        - FriendlyStrength: 1890
        - City: Sippar
        - AreaID: 0
        - Plots: 57
        - CenterX: 45
        - CenterY: 25
        - Units:
          - Greece:
            - Destroyer: 2
        - Neighbors:
          - -100005
          - 10621
          - -1071
          - -100007
        
        # Events
        Events: events since you last made a decision.
        
        ## Turn 400
        
        ### 0
        - Type: CityTrained
        - WithGold: true
        - Player: 7: Ethiopia
        - City:
          - Name: Addis Ababa
          - Population: 34
          - ID: 1064
        - Unit:
          - Level: 1
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16970
        
        ### 1
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Anti-Aircraft Gun
          - ID: 16972
        - Player: 7: Ethiopia
        - Plains Hills 14,38:
          - Owner: Ethiopia
          - Improvement: Academy
        
        ### 2
        - Type: UnitCreated
        - UnitType: Anti-Aircraft Gun
        - Player: 7: Ethiopia
        - Unit:
          - Level: 1
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16972
        - Plains Hills 14,38:
          - Owner: Ethiopia
          - Improvement: Academy
        
        ### 3
        - Type: CityTrained
        - Player: 7: Ethiopia
        - City:
          - Name: Addis Ababa
          - Population: 34
          - ID: 1064
        - Unit:
          - Level: 1
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16972
        
        ### 4
        - Type: CityEndsWLTKD
        - Unused: 0
        - Owner: 7: Ethiopia
        - Grass Land 13,25:
          - Owner: Ethiopia
          - CityID: 7902
          - Population: 19
          - City: Bahir Dar
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 5
        - Type: EspionageState
        - SpyIndex: 0
        - SpyState: 1
        - City:
          - Owner: Ethiopia
          - CityID: 1187
          - Population: 20
          - IsRiver: true
          - City: Harar
          - Terrain: Plains
          - Resource: Wheat
          - Religion: Eastern Orthodoxy
          - Route: Railroad
          - Plot: Land
          - X: 17
          - Y: 37
        - SpyOwner: 7: Ethiopia
        
        ### 6
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16972
        - Player: 7: Ethiopia
        - Promotions:
          - Interceptor III
          - Interceptor IV
          - Shock I
        
        ### 7
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 16%
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 14256
        - Player: 7: Ethiopia
        - Plots:
          - Grass Hills 15,22:
            - Owner: Ethiopia
            - Resource: Iron
            - Improvement: Mine
          - Grass Hills 15,23:
            - Owner: Ethiopia
            - Improvement: Lumber Mill
            - Route: Road
            - Feature: Jungle
        
        ### 8
        - Type: CombatResult
        - Coast 5,39:
          - Owner: Ethiopia
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 31
          - Damage: 120
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 25%
            - AI: FastAttack
            - Unit: Rifleman
            - ID: 16624
        
        ### 9
        - Type: CombatResult
        - Coast 2,43:
          - Owner: Ethiopia
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 31
          - Damage: 31
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - AI: FastAttack
            - Unit: Rifleman
            - ID: 16703
        
        ### 10
        - Type: CombatResult
        - Plains Land 15,26:
          - Owner: Ethiopia
          - IsRiver: true
          - Improvement: Lumber Mill
          - Route: Railroad
          - Feature: Jungle
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 29
          - Damage: 107
          - Unit:
            - Level: 1
            - Health: 35%
            - AI: FastAttack
            - Unit: Rifleman
            - ID: 16768
          - Player: 63: Barbarians
        
        ### 11
        - Type: CombatResult
        - Plains Land 15,26:
          - Owner: Ethiopia
          - IsRiver: true
          - Improvement: Lumber Mill
          - Route: Railroad
          - Feature: Jungle
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 13
          - Damage: 120
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 10%
            - AI: FastAttack
            - Unit: Rifleman
            - ID: 16768
        
        ### 12
        - Type: CombatResult
        - Plains Hills 15,36:
          - Owner: Ethiopia
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 25
          - Damage: 27
          - Unit:
            - Level: 3
            - Health: 98%
            - AI: Ranged
            - Unit: Machine Gun
            - ID: 14025
          - Player: 25
        
        ### 13
        - Type: CombatResult
        - Plains Hills 15,36:
          - Owner: Ethiopia
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 23
          - Damage: 50
          - Unit:
            - Level: 3
            - Health: 73%
            - AI: Ranged
            - Unit: Machine Gun
            - ID: 14025
          - Player: 25
        
        ### 14
        - Type: CombatResult
        - Grass Land 13,24:
          - Owner: Ethiopia
          - Resource: Maize
          - Improvement: Farm
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 29
          - Damage: 29
          - Unit:
            - Level: 1
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 16767
          - Player: 63: Barbarians
        
        ### 15
        - Type: CombatResult
        - Tundra Hills 7,44:
          - Owner: Ethiopia
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 25
          - Damage: 25
        - Defender:
          - RemainingHP: 30
          - Damage: 30
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 16700
        
        ### 16
        - Type: CombatResult
        - Coast 2,43:
          - Owner: Ethiopia
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 39
          - Damage: 70
          - Unit:
            - Level: 1
            - Health: 74%
            - AI: FastAttack
            - Unit: Rifleman
            - ID: 16703
          - Player: 63: Barbarians
        
        ### 17
        - Type: CombatResult
        - Grass Land 13,24:
          - Owner: Ethiopia
          - Resource: Maize
          - Improvement: Farm
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 37
          - Damage: 66
          - Unit:
            - Level: 1
            - Health: 71%
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 16767
          - Player: 63: Barbarians
        
        ### 18
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16836
        - Player: 7: Ethiopia
        - Plots:
          - Plains Land 13,39:
            - Owner: Ethiopia
            - CityID: 1064
            - Population: 34
            - IsRiver: true
            - City: Addis Ababa
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Grass Land 14,39:
            - Owner: Ethiopia
            - IsRiver: true
            - Resource: Bison
            - Improvement: Town
            - Route: Railroad
          - Tundra Hills 15,39:
            - Owner: Ethiopia
            - Improvement: Village
            - Route: Railroad
        
        ### 19
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 82%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 16712
        - Player: 7: Ethiopia
        - Plains Land 15,40:
          - Owner: Ethiopia
          - Resource: Salt
          - Improvement: Holy Site
        
        ### 20
        - Type: CombatResult
        - Tundra Hills 15,41:
          - Owner: Ethiopia
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 15
          - Damage: 82
          - Unit:
            - Level: 3
            - Health: 46%
            - AI: Defense
            - Unit: Infantry
            - ID: 15305
          - Player: 27
        
        ### 21
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 82%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 16712
        - Player: 7: Ethiopia
        - Plains Land 14,40:
          - Owner: Ethiopia
          - IsRiver: true
          - Resource: Coffee
          - Improvement: Academy
        
        ### 22
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16972
        - Player: 7: Ethiopia
        - Plots:
          - Grass Land 14,39:
            - Owner: Ethiopia
            - IsRiver: true
            - Resource: Bison
            - Improvement: Town
            - Route: Railroad
          - Plains Land 15,40:
            - Owner: Ethiopia
            - Resource: Salt
            - Improvement: Holy Site
        
        ### 23
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 61%
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16201
        - Player: 7: Ethiopia
        - Tundra Hills 17,40:
          - Owner: Ethiopia
          - Resource: Sheep
          - Improvement: Pasture
          - Route: Railroad
        
        ### 24
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: CityBombard
          - Unit: Artillery
          - ID: 14822
        - Player: 7: Ethiopia
        - Plots:
          - Grass Hills 15,24:
            - Owner: Ethiopia
            - Improvement: Mine
            - Route: Road
          - Grass Land 14,25:
            - Owner: Ethiopia
            - Resource: Cattle
            - Improvement: Pasture
            - Route: Railroad
          - Plains Land 15,26:
            - Owner: Ethiopia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
        
        ### 25
        - Type: CombatResult
        - Grass Land 13,24:
          - Owner: Ethiopia
          - Resource: Maize
          - Improvement: Farm
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 34
          - Damage: 100
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 34%
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 16767
        
        ### 26
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 65%
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 14388
        - Player: 7: Ethiopia
        - Plots:
          - Grass Hills 15,23:
            - Owner: Ethiopia
            - Improvement: Lumber Mill
            - Route: Road
            - Feature: Jungle
          - Grass Hills 15,24:
            - Owner: Ethiopia
            - Improvement: Mine
            - Route: Road
          - Grass Hills 14,24:
            - Owner: Ethiopia
            - Improvement: Monolithic Church
        
        ### 27
        - Type: CombatResult
        - Grass Land 13,23:
          - Owner: Ethiopia
          - Resource: Maize
          - Improvement: Farm
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 43
          - Damage: 86
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 56%
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 16763
        
        ### 28
        - Type: CombatResult
        - Grass Land 13,23:
          - Owner: Ethiopia
          - Resource: Maize
          - Improvement: Farm
        - Attacker:
          - RemainingHP: 4
          - Damage: 39
        - Defender:
          - RemainingHP: 53
          - Damage: 139
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 14%
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 16763
        
        ### 29
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 61%
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 14388
        - Player: 7: Ethiopia
        - Grass Land 13,23:
          - Owner: Ethiopia
          - Resource: Maize
          - Improvement: Farm
        
        ### 30
        - Type: CombatResult
        - Grass Land 4,42:
          - Owner: Ethiopia
          - Improvement: Village
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 31
          - Damage: 31
          - Unit:
            - Level: 1
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 16628
          - Player: 63: Barbarians
        
        ### 31
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 7810
        - Player: 7: Ethiopia
        - Tundra Hills 7,46:
          - Owner: Ethiopia
          - Resource: Sheep
          - Improvement: Pasture
        
        ### 32
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 21%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 14021
        - Player: 22
        - Tundra Land 62,3:
          - Owner: Songhai
          - IsRiver: true
          - Improvement: Farm
        
        ### 33
        - Type: CombatResult
        - Tundra Land 61,3:
          - Owner: Songhai
          - CityID: 2885
          - Population: 23
          - IsRiver: true
          - City: Kumbi Saleh
          - Resource: Deer
          - Religion: Buddhism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 16
          - Damage: 279
          - Player: 0: Songhai
        
        ### 34
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 31%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14022
        - Player: 22
        - Tundra Land 63,5:
          - Owner: Songhai
          - Improvement: Fort
        
        ### 35
        - Type: CombatResult
        - Tundra Land 61,3:
          - Owner: Songhai
          - CityID: 2885
          - Population: 23
          - IsRiver: true
          - City: Kumbi Saleh
          - Resource: Deer
          - Religion: Buddhism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 22
          - Damage: 301
          - Player: 0: Songhai
        
        ### 36
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 21%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 14021
        - Player: 22
        - Tundra Land 63,3:
          - Owner: Songhai
          - Improvement: Lumber Mill
          - Feature: Forest
        
        ### 37
        - Type: CombatResult
        - Grass Hills 65,10:
          - Owner: Songhai
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Unit:
            - Level: 4
            - Health: 49%
            - AI: Attack
            - Unit: Foreign Legion
            - ID: 16715
          - Player: 0: Songhai
        - Interceptor:
          - Damage: 42
          - Player: 22
          - Unit:
            - Level: 4
            - Health: 67%
            - AI: DefenseAir
            - Unit: Jet Fighter
            - ID: 16665
        
        ### 38
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 15056
        - Player: 22
        
        ### 39
        - Type: CityConstructed
        - City:
          - Name: Monaco
          - Population: 14
          - ID: 12340
        - Owner: 23
        - Building: Windmill
        
        ### 40
        - Type: CombatResult
        - Grass Hills 65,10:
          - Owner: Songhai
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 25
          - Damage: 83
          - Unit:
            - Level: 4
            - Health: 49%
            - AI: Attack
            - Unit: Foreign Legion
            - ID: 16715
          - Player: 0: Songhai
        
        ### 41
        - Type: CombatResult
        - Grass Hills 65,10:
          - Owner: Songhai
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 27
          - Damage: 110
          - Unit:
            - Level: 4
            - Health: 27%
            - AI: Attack
            - Unit: Foreign Legion
            - ID: 16715
          - Player: 0: Songhai
        
        ### 42
        - Type: SetAlly
        - NewAllyPlayer: 3: Japan
        - OldAllyPlayer: 6: Greece
        - MinorPlayer: 25
        
        ### 43
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 83%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14024
        - Player: 25
        - Plots:
          - Desert Land 13,35:
            - Owner: Ethiopia
            - Feature: Oasis
          - Plains Hills 14,35:
            - Owner: Ethiopia
        
        ### 44
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 78%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 14257
        - Player: 25
        - Plots:
          - Desert Land 14,34:
            - Owner: Ethiopia
            - IsRiver: true
            - Feature: Flood Plains
          - Plains Hills 15,34:
            - Owner: Ethiopia
            - Resource: Deer
            - Feature: Forest
          - Desert Hills 15,33:
            - Owner: Ethiopia
            - Route: Railroad
        
        ### 45
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - Health: 72%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14026
        - Player: 25
        - Plains Hills 15,34:
          - Owner: Ethiopia
          - Resource: Deer
          - Feature: Forest
        
        ### 46
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 50%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14025
        - Player: 25
        - Plots:
          - Plains Land 15,35:
            - Owner: Ethiopia
          - Plains Hills 16,34:
            - Owner: Ethiopia
            - Improvement: Monolithic Church
            - Route: Railroad
        
        ### 47
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Defense
          - Unit: Infantry
          - ID: 15302
        - Player: 26
        - Plots:
          - Plains Land 31,40:
            - Owner: City-State Manila
            - Improvement: Village
            - Route: Railroad
          - Grass Land 30,40:
            - Owner: City-State Manila
            - Improvement: Farm
        
        ### 48
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14027
        - Player: 26
        - Plots:
          - Plains Land 30,36:
            - Owner: Greece
            - Resource: Maize
            - Improvement: Farm
          - Plains Land 29,36:
            - Owner: Greece
            - Improvement: Village
            - Route: Railroad
        
        ### 49
        - Type: UnitPromoted
        - Unit:
          - Level: 4
          - Health: 42%
          - AI: Defense
          - Unit: Infantry
          - ID: 15305
        - Player: 27
        - Promotion: Forlorn Hope
        
        ### 50
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14032
        - Player: 27
        
        ### 51
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - Health: 41%
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 14827
        - Player: 28
        
        ### 52
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 14826
        - Player: 28
        
        ### 53
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 16898
        - Player: 28
        
        ### 54
        - Type: CombatResult
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 16
          - Damage: 52
          - Unit:
            - Level: 5
            - Health: 74%
            - AI: AttackSea
            - Unit: Destroyer
            - ID: 16575
          - Player: 6: Greece
        
        ### 55
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 16898
        - Player: 28
        - Coast 43,33:
          - Owner: City-State Veligrad
          - Feature: Atoll
        
        ### 56
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 15312
        - Player: 30
        
        ### 57
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 15311
        - Player: 30
        - Grass Hills 25,17:
          - Owner: City-State Abernethy
          - Improvement: Mine
          - Route: Railroad
        
        ### 58
        - Type: CityConstructed
        - City:
          - Name: Budapest
          - Population: 22
          - ID: 1076
        - Owner: 33
        - Building: Opera House
        
        ### 59
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14259
        - Player: 34
        - Tundra Hills 11,49:
          - Owner: City-State Buenos Aires
          - Improvement: Mine
          - Route: Railroad
        
        ### 60
        - Type: CombatResult
        - Tundra Land 6,48:
          - Owner: Ethiopia
          - IsRiver: true
          - Improvement: Lumber Mill
          - Feature: Forest
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 39
          - Damage: 39
          - Unit:
            - Level: 1
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 16696
          - Player: 63: Barbarians
        
        ### 61
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 15465
        - Player: 35
        - Tundra Hills 21,44:
          - Owner: Greece
          - IsRiver: true
          - Route: Railroad
        
        ### 62
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 15325
        - Player: 35
        - Snow Hills 20,47:
          - Owner: City-State Antananarivo
          - IsRiver: true
          - Improvement: Mine
          - Route: Railroad
        
        ### 63
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 82%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 14530
        - Player: 35
        
        ### 64
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 84%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 14531
        - Player: 35
        - Plots:
          - Tundra Hills 19,48:
            - Owner: City-State Antananarivo
            - Resource: Gems
            - Improvement: Mine
            - Route: Railroad
          - Tundra Land 19,47:
            - Owner: City-State Antananarivo
            - CityID: 1078
            - Population: 8
            - City: Antananarivo
            - Resource: Jewelry
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Mountain Mountain 19,46:
            - Owner: City-State Antananarivo
            - Route: Railroad
          - Snow Land 18,45:
            - Owner: City-State Antananarivo
            - Resource: Iron
            - Improvement: Embassy
        
        ### 65
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14052
        - Player: 35
        - Plots:
          - Tundra Hills 19,48:
            - Owner: City-State Antananarivo
            - Resource: Gems
            - Improvement: Mine
            - Route: Railroad
          - Tundra Hills 18,49:
            - Owner: City-State Antananarivo
            - Improvement: Mine
        
        ### 66
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14323
        - Player: 35
        - Snow Hills 18,47:
          - Owner: City-State Antananarivo
          - Improvement: Mine
          - Route: Railroad
        
        ### 67
        - Type: BarbariansCampFounded
        - Tundra Land 32,3:
          - Improvement: Barbarian Encampment
          - Feature: Forest
        
        ### 68
        - Type: TileImprovementChanged
        - NewImprovement: Barbarian Encampment
        - Tundra Land 32,3:
          - Improvement: Barbarian Encampment
          - Feature: Forest
        
        ### 69
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Rifleman
          - ID: 16975
        - Player: 63: Barbarians
        - Tundra Land 32,3:
          - Improvement: Barbarian Encampment
          - Feature: Forest
        
        ### 70
        - Type: UnitCreated
        - UnitType: Rifleman
        - Player: 63: Barbarians
        - Unit:
          - Level: 1
          - AI: Defense
          - Unit: Rifleman
          - ID: 16975
        - Tundra Land 32,3:
          - Improvement: Barbarian Encampment
          - Feature: Forest
        
        ### 71
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Machine Gun
          - ID: 16976
        - Player: 63: Barbarians
        - Plains Land 32,4:
          - IsRiver: true
          - Resource: Iron
          - Improvement: Mine
        
        ### 72
        - Type: UnitCreated
        - UnitType: Machine Gun
        - Player: 63: Barbarians
        - Unit:
          - Level: 1
          - AI: FastAttack
          - Unit: Machine Gun
          - ID: 16976
        - Plains Land 32,4:
          - IsRiver: true
          - Resource: Iron
          - Improvement: Mine
        
        ### 73
        - Type: CombatResult
        - Grass Land 13,23:
          - Owner: Ethiopia
          - Resource: Maize
          - Improvement: Farm
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 30
          - Damage: 69
          - Player: 7: Ethiopia
          - Unit:
            - Level: 3
            - Health: 61%
            - AI: Paradrop
            - Unit: Paratrooper
            - ID: 14388
        
        ### 74
        - Type: CombatResult
        - Grass Land 13,23:
          - Owner: Ethiopia
          - Resource: Maize
          - Improvement: Farm
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 31
          - Damage: 100
          - Player: 7: Ethiopia
          - Unit:
            - Level: 3
            - Health: 31%
            - AI: Paradrop
            - Unit: Paratrooper
            - ID: 14388
        
        ### 75
        - Type: CombatResult
        - Grass Land 13,25:
          - Owner: Ethiopia
          - CityID: 7902
          - Population: 19
          - City: Bahir Dar
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 9
          - Damage: 9
          - Player: 7: Ethiopia
        
        ### 76
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 70%
          - AI: FastAttack
          - Unit: Machine Gun
          - ID: 16700
        - Player: 63: Barbarians
        - Plains Hills 6,44:
          - Owner: Ethiopia
          - Improvement: Monolithic Church
        
        ### 77
        - Type: CombatResult
        - Grass Land 4,45:
          - Owner: Ethiopia
          - CityID: 3454
          - Population: 23
          - IsRiver: true
          - City: Axum
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 7
          - Damage: 7
          - Player: 7: Ethiopia
        
        ### 78
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: FastAttack
          - Unit: Machine Gun
          - ID: 16701
        - Player: 63: Barbarians
        - Plains Hills 6,46:
          - Owner: Ethiopia
          - Improvement: Monolithic Church
        
        ### 79
        - Type: CombatResult
        - Grass Land 4,45:
          - Owner: Ethiopia
          - CityID: 3454
          - Population: 23
          - IsRiver: true
          - City: Axum
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 7
          - Damage: 14
          - Player: 7: Ethiopia
        
        ### 80
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 61%
          - AI: FastAttack
          - Unit: Machine Gun
          - ID: 16696
        - Player: 63: Barbarians
        - Tundra Hills 6,47:
          - Owner: Ethiopia
          - Resource: Sheep
          - Improvement: Pasture
        
        ### 81
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: FastAttack
          - Unit: Rifleman
          - ID: 16632
        - Player: 63: Barbarians
        - Plains Hills 4,44:
          - Owner: Ethiopia
          - Resource: Sheep
          - Improvement: Pasture
        
        ### 82
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: FastAttack
          - Unit: Machine Gun
          - ID: 16702
        - Player: 63: Barbarians
        - Grass Land 5,46:
          - Owner: Ethiopia
          - IsRiver: true
          - Improvement: Lumber Mill
          - Feature: Forest
        
        ### 83
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 85%
          - AI: FastAttack
          - Unit: Machine Gun
          - ID: 16626
        - Player: 63: Barbarians
        - Plots:
          - Grass Land 4,42:
            - Owner: Ethiopia
            - Improvement: Village
          - Grass Land 3,43:
            - Owner: Ethiopia
            - Improvement: Lumber Mill
            - Feature: Forest
        
        ### 84
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 69%
          - AI: FastAttack
          - Unit: Machine Gun
          - ID: 16628
        - Player: 63: Barbarians
        - Plains Land 3,42:
          - Owner: Ethiopia
        
        ### 85
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 60%
          - AI: FastAttack
          - Unit: Machine Gun
          - ID: 16625
        - Player: 63: Barbarians
        - Plots:
          - Grass Land 4,42:
            - Owner: Ethiopia
            - Improvement: Village
          - Plains Hills 4,43:
            - Owner: Ethiopia
        
        ### 86
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: FastAttack
          - Unit: Rifleman
          - ID: 16632
        - Player: 63: Barbarians
        - Grass Land 5,44:
          - Owner: Ethiopia
          - Improvement: Lumber Mill
          - Route: Railroad
          - Feature: Forest
        
        ### 87
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 48%
          - AI: FastAttack
          - Unit: Rifleman
          - ID: 16627
        - Player: 63: Barbarians
        - Plots:
          - Coast 2,40:
            - Owner: Ethiopia
          - Coast 2,39:
            - Owner: Ethiopia
        
        ### 88
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 41%
          - AI: FastAttack
          - Unit: Rifleman
          - ID: 16703
        - Player: 63: Barbarians
        - Plots:
          - Coast 2,44:
            - Owner: Ethiopia
            - Resource: Fish
            - Improvement: Fishing Boats
          - Ocean 1,45:
            - Owner: Ethiopia
          - Coast 2,46:
            - Owner: Ethiopia
        
        ## Turn 401
        
        ### 0
        - Type: CityConvertsReligion
        - City:
          - Owner: Greece
          - CityID: 8484
          - Population: 21
          - IsRiver: true
          - City: Shushan
          - Terrain: Grass
          - Religion: Islam
          - Route: Railroad
          - Plot: Land
          - X: 27
          - Y: 27
        - Owner: 6: Greece
        - Religion: Islam
        
        ### 1
        - Type: MakePeace
        - PacifierFlag: true
        - OriginatingPlayer: 0: Songhai
        - TargetTeam: 25
        
        ### 2
        - Type: EspionageState
        - SpyIndex: 5
        - SpyState: 3
        - City:
          - Owner: Ethiopia
          - CityID: 7902
          - Population: 19
          - City: Bahir Dar
          - Terrain: Grass
          - Religion: Eastern Orthodoxy
          - Route: Railroad
          - Plot: Land
          - X: 13
          - Y: 25
        - SpyOwner: 0: Songhai
        
        ### 3
        - Type: UnitPromoted
        - Unit:
          - Level: 5
          - Health: 51%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 16024
        - Player: 0: Songhai
        - Promotion: Logistics
        
        ### 4
        - Type: UnitPromoted
        - Unit:
          - Level: 5
          - Health: 77%
          - AI: DefenseAir
          - Unit: Jet Fighter
          - ID: 16665
        - Player: 0: Songhai
        - Promotion: Air Supremacy II
        
        ### 5
        - Type: UnitPromoted
        - Unit:
          - Level: 3
          - Health: 47%
          - AI: Defense
          - Unit: Infantry
          - ID: 15819
        - Player: 0: Songhai
        - Promotion: Shock II
        
        ### 6
        - Type: CombatResult
        - Tundra Hills 64,4:
          - Owner: Songhai
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 17
          - Damage: 17
          - Unit:
            - Level: 5
            - AI: Ranged
            - Unit: Machine Gun
            - ID: 14018
          - Player: 22
        
        ### 7
        - Type: CombatResult
        - Tundra Land 62,2:
          - Owner: Songhai
          - IsRiver: true
          - Resource: Deer
          - Improvement: Camp
          - Feature: Forest
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 18
          - Damage: 29
          - Unit:
            - Level: 4
            - Health: 91%
            - AI: Defense
            - Unit: Infantry
            - ID: 15800
          - Player: 22
        
        ### 8
        - Type: CombatResult
        - Desert Hills 56,9:
          - Owner: Babylon
          - Improvement: Mine
          - Route: Road
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 18
          - Damage: 18
          - Unit:
            - Level: 7
            - AI: Ranged
            - Unit: Machine Gun
            - ID: 12087
          - Player: 6: Greece
        
        ### 9
        - Type: CombatResult
        - Plains Land 57,9:
          - Owner: Songhai
          - Improvement: Farm
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 28
          - Damage: 28
          - Player: 6: Greece
          - Unit:
            - Level: 9
            - AI: Ranged
            - Unit: Light Tank
            - ID: 12093
        
        ### 10
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 74%
          - AI: CityBombard
          - Unit: Artillery
          - ID: 13971
        - Player: 0: Songhai
        - Plots:
          - Plains Hills 60,10:
            - Owner: Songhai
            - Route: Railroad
          - Plains Hills 59,11:
            - Owner: Songhai
            - Resource: Aluminum
            - Improvement: Manufactory
            - Route: Railroad
        
        ### 11
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 51%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 16024
        - Player: 0: Songhai
        - Plains Hills 59,11:
          - Owner: Songhai
          - Resource: Aluminum
          - Improvement: Manufactory
          - Route: Railroad
        
        ### 12
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 42%
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 14445
        - Player: 0: Songhai
        - Plains Hills 29,7:
          - Improvement: Lumber Mill
          - Feature: Forest
        
        ### 13
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 51%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 16024
        - Player: 0: Songhai
        - Plots:
          - Plains Hills 60,10:
            - Owner: Songhai
            - Route: Railroad
          - Plains Land 61,10:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
        
        ### 14
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4339
        - Player: 0: Songhai
        - Plots:
          - Plains Land 61,10:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 60,10:
            - Owner: Songhai
            - Route: Railroad
          - Plains Hills 59,11:
            - Owner: Songhai
            - Resource: Aluminum
            - Improvement: Manufactory
            - Route: Railroad
        
        ### 15
        - Type: UnitBuildCompleted
        - Owner: 0: Songhai
        - Unit:
          - Level: 1
          - Health: 75%
          - AI: Worker
          - Unit: Worker
          - ID: 9966
        - Build: Construct a Village
        - Plains Hills 60,10:
          - Owner: Songhai
          - Route: Railroad
        
        ### 16
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 11238
        - Player: 0: Songhai
        - Plots:
          - Coast 70,2:
            - Feature: Ice
          - Coast 71,3:
            - Feature: Ice
        
        ### 17
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Gatling Gun
          - ID: 16999
        - Player: 1: Babylon
        - Plains Hills 33,7:
          - Owner: Babylon
          - Resource: Iron
          - Improvement: Mine
        
        ### 18
        - Type: UnitCreated
        - UnitType: Gatling Gun
        - Player: 1: Babylon
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 16999
        - Plains Hills 33,7:
          - Owner: Babylon
          - Resource: Iron
          - Improvement: Mine
        
        ### 19
        - Type: CityTrained
        - Player: 1: Babylon
        - City:
          - Name: Gwandu
          - Population: 12
          - ID: 13974
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 16999
        
        ### 20
        - Type: SetPopulation
        - OldPopulation: 12
        - NewPopulation: 13
        - City:
          - Owner: Babylon
          - CityID: 13974
          - Population: 13
          - City: Gwandu
          - Terrain: Plains
          - Religion: Catholicism
          - Route: Railroad
          - Plot: Hills
          - X: 34
          - Y: 8
        
        ### 21
        - Type: EspionageState
        - SpyIndex: 2
        - SpyState: 3
        - City:
          - Owner: Ethiopia
          - CityID: 1187
          - Population: 20
          - IsRiver: true
          - City: Harar
          - Terrain: Plains
          - Resource: Wheat
          - Religion: Eastern Orthodoxy
          - Route: Railroad
          - Plot: Land
          - X: 17
          - Y: 37
        - SpyOwner: 1: Babylon
        
        ### 22
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15563
        - Player: 1: Babylon
        - Plots:
          - Grass Land 52,6:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 53,6:
            - Owner: Greece
            - CityID: 13487
            - Population: 18
            - IsRiver: true
            - City: Tombouctu
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 51,7:
            - Owner: Greece
            - IsRiver: true
            - Resource: Horses
            - Improvement: Pasture
            - Route: Road
        
        ### 23
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 15692
        - Player: 1: Babylon
        - Plots:
          - Coast 50,14:
            - Owner: Babylon
          - Coast 49,15:
            - Owner: Babylon
          - Coast 49,16:
            - Owner: Greece
            - Resource: Fish
            - Improvement: Fishing Boats
          - Desert Land 48,17:
            - Owner: Greece
            - CityID: 11110
            - Population: 18
            - IsRiver: true
            - City: Borsippa
            - Religion: Catholicism
            - Route: Railroad
        
        ### 24
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16740
        - Player: 1: Babylon
        - Plots:
          - Plains Land 49,6:
            - Owner: Greece
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 48,6:
            - Owner: Greece
            - CityID: 12645
            - Population: 18
            - City: Jenne
            - Resource: Aluminum
            - Religion: Buddhism
            - Route: Railroad
          - Grass Hills 49,7:
            - Owner: Greece
            - IsRiver: true
            - Resource: Lapis Lazuli
            - Improvement: Quarry
            - Route: Railroad
        
        ### 25
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16676
        - Player: 1: Babylon
        - Plots:
          - Desert Hills 56,9:
            - Owner: Babylon
            - Improvement: Mine
            - Route: Road
          - Desert Land 57,8:
            - Owner: Babylon
            - Route: Road
          - Plains Land 56,7:
            - Owner: Greece
            - Improvement: Fort
            - Route: Railroad
          - Plains Land 55,7:
            - Owner: Greece
            - Route: Railroad
          - Plains Land 55,6:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
        
        ### 26
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16803
        - Player: 1: Babylon
        - Plots:
          - Grass Land 52,11:
            - Owner: Babylon
            - Improvement: Village
            - Route: Railroad
          - Grass Land 51,11:
            - Owner: Babylon
            - CityID: 1293
            - Population: 23
            - IsRiver: true
            - City: Dur-Kurigalzu
            - Religion: Catholicism
            - Route: Railroad
        
        ### 27
        - Type: UnitPromoted
        - Unit:
          - Level: 3
          - Health: 98%
          - AI: Ranged
          - Unit: Cavalry
          - ID: 16738
        - Player: 1: Babylon
        - Promotion: Barrage II
        
        ### 28
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 16999
        - Player: 1: Babylon
        - Promotion: Barrage I
        
        ### 29
        - Type: CombatResult
        - Plains Hills 30,8:
          - Improvement: City Ruins
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 22
          - Damage: 78
          - Player: 0: Songhai
          - Unit:
            - Level: 3
            - Health: 55%
            - AI: Defense
            - Unit: Infantry
            - ID: 15819
        
        ### 30
        - Type: CombatResult
        - Plains Land 32,4:
          - IsRiver: true
          - Resource: Iron
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 38
          - Damage: 38
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 16976
        
        ### 31
        - Type: CombatResult
        - Plains Hills 29,7:
          - Improvement: Lumber Mill
          - Feature: Forest
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 22
          - Damage: 80
          - Player: 0: Songhai
          - Unit:
            - Level: 4
            - Health: 42%
            - AI: Paradrop
            - Unit: Paratrooper
            - ID: 14445
        
        ### 32
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 15561
        - Player: 1: Babylon
        - Plots:
          - Grass Land 32,7:
            - Improvement: Village
        
        ### 33
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 98%
          - AI: Ranged
          - Unit: Cavalry
          - ID: 16738
        - Player: 1: Babylon
        - Plains Land 32,5:
          - Owner: Babylon
          - Resource: Stone
          - Improvement: Quarry
        
        ### 34
        - Type: CombatResult
        - Plains Land 32,4:
          - IsRiver: true
          - Resource: Iron
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 25
          - Damage: 63
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 62%
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 16976
        
        ### 35
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 98%
          - AI: Ranged
          - Unit: Cavalry
          - ID: 16738
        - Player: 1: Babylon
        - Plains Hills 33,5:
          - Feature: Forest
        
        ### 36
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 16614
        - Player: 1: Babylon
        - Plots:
          - Plains Land 51,9:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
          - Plains Hills 51,10:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Mine
            - Route: Road
        
        ### 37
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - Health: 86%
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 15233
        - Player: 1: Babylon
        - Plots:
          - Plains Land 51,8:
            - Owner: Babylon
            - Improvement: Village
            - Route: Road
          - Plains Land 50,9:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
        
        ### 38
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: FastAttack
          - Unit: Commando
          - ID: 16922
        - Player: 1: Babylon
        - Desert Hills 51,15:
          - Owner: Babylon
          - Improvement: Mine
          - Route: Road
        
        ### 39
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: CityBombard
          - Unit: Field Gun
          - ID: 15482
        - Player: 1: Babylon
        - Plots:
          - Plains Land 51,9:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
          - Plains Hills 52,9:
            - Owner: Babylon
            - Improvement: Mine
            - Route: Road
        
        ### 40
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 15754
        - Player: 1: Babylon
        - Plots:
          - Plains Hills 53,10:
            - Owner: Babylon
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 52,10:
            - Owner: Babylon
            - Resource: Truffles
            - Improvement: Camp
            - Route: Road
            - Feature: Forest
          - Plains Land 51,9:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
          - Plains Land 52,8:
            - Owner: Greece
            - Resource: Ivory
            - Improvement: Camp
        
        ### 41
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 15888
        - Player: 1: Babylon
        - Plots:
          - Plains Land 52,10:
            - Owner: Babylon
            - Resource: Truffles
            - Improvement: Camp
            - Route: Road
            - Feature: Forest
          - Plains Land 51,9:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
          - Plains Land 51,8:
            - Owner: Babylon
            - Improvement: Village
            - Route: Road
        
        ### 42
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 82%
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 13410
        - Player: 1: Babylon
        - Plots:
          - Grass Land 51,11:
            - Owner: Babylon
            - CityID: 1293
            - Population: 23
            - IsRiver: true
            - City: Dur-Kurigalzu
            - Religion: Catholicism
            - Route: Railroad
          - Plains Hills 51,10:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Mine
            - Route: Road
          - Plains Land 50,9:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
          - Grass Land 50,8:
            - Owner: Babylon
            - IsRiver: true
            - Resource: Deer
            - Improvement: Camp
            - Feature: Forest
        
        ### 43
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 11145
        - Player: 1: Babylon
        - Plots:
          - Plains Hills 51,10:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Mine
            - Route: Road
          - Plains Land 50,9:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
          - Plains Land 51,8:
            - Owner: Babylon
            - Improvement: Village
            - Route: Road
          - Plains Land 51,7:
            - Owner: Greece
            - IsRiver: true
            - Resource: Horses
            - Improvement: Pasture
            - Route: Road
        
        ### 44
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 81%
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 14558
        - Player: 1: Babylon
        - Plains Hills 53,9:
          - Owner: Babylon
          - Improvement: Mine
          - Route: Railroad
        
        ### 45
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 93%
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 10016
        - Player: 1: Babylon
        - Plots:
          - Plains Land 53,11:
            - Owner: Babylon
            - Improvement: Manufactory
            - Route: Road
          - Plains Hills 53,10:
            - Owner: Babylon
            - Improvement: Mine
            - Route: Railroad
        
        ### 46
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 15%
          - AI: Defense
          - Unit: Rifleman
          - ID: 16674
        - Player: 1: Babylon
        - Grass Land 56,11:
          - Owner: Babylon
          - Resource: Deer
          - Improvement: Camp
          - Route: Road
          - Feature: Forest
        
        ### 47
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - Health: 73%
          - AI: CityBombard
          - Unit: Field Gun
          - ID: 16923
        - Player: 1: Babylon
        - Grass Land 54,11:
          - Owner: Babylon
          - IsRiver: true
          - Improvement: Farm
          - Route: Railroad
        
        ### 48
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 11038
        - Player: 1: Babylon
        - Plots:
          - Ocean 45,11:
            - Owner: City-State Monaco
        
        ### 49
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 6566
        - Player: 1: Babylon
        - Plains Hills 34,8:
          - Owner: Babylon
          - CityID: 13974
          - Population: 13
          - City: Gwandu
          - Route: Railroad
        
        ### 50
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Missionary
          - Unit: Missionary
          - ID: 16860
        - Player: 1: Babylon
        - Plots:
          - Coast 51,17:
            - Owner: Babylon
          - Coast 51,16:
            - Owner: Babylon
          - Desert Land 50,16:
            - Owner: Greece
            - Improvement: Fort
          - Coast 49,15:
            - Owner: Babylon
        
        ### 51
        - Type: DealMade
        - StartTurn: 401
        - TradedItems:
          - #0:
            - Data1: 0
            - Data2: 1
            - Data3: 0
            - Duration: 50
            - FromPlayer: 3
            - Item: Resources
          - #1:
            - Data1: 23
            - Data2: 0
            - Data3: 0
            - Duration: 50
            - FromPlayer: 2
            - Item: GoldPerTurn
        - ToPlayer: 3: Japan
        - FromPlayer: 2: The Ottomans
        
        ### 52
        - Type: CityConvertsReligion
        - City:
          - Owner: Japan
          - CityID: 1060
          - Population: 29
          - IsRiver: true
          - City: Kyoto
          - Terrain: Grass
          - Religion: Tengriism
          - Route: Railroad
          - Plot: Land
          - X: 60
          - Y: 40
        - Owner: 3: Japan
        - Religion: Tengriism
        
        ### 53
        - Type: EspionageState
        - SpyIndex: 6
        - SpyState: 1
        - City:
          - Owner: Ethiopia
          - CityID: 1064
          - Population: 34
          - IsRiver: true
          - City: Addis Ababa
          - Terrain: Plains
          - Religion: Eastern Orthodoxy
          - Route: Railroad
          - Plot: Land
          - X: 13
          - Y: 39
        - SpyOwner: 3: Japan
        
        ### 54
        - Type: DealMade
        - StartTurn: 401
        - TradedItems:
          - #0:
            - Data1: 18
            - Data2: 1
            - Data3: 0
            - Duration: 50
            - FromPlayer: 6
            - Item: Resources
          - #1:
            - Data1: 6
            - Data2: 0
            - Data3: 0
            - Duration: 50
            - FromPlayer: 4
            - Item: GoldPerTurn
        - ToPlayer: 6: Greece
        - FromPlayer: 4: Carthage
        
        ### 55
        - Type: PlayerGoldenAge
        - TurnChange: 10
        - Player: 4: Carthage
        
        ### 56
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16487
        - Player: 4: Carthage
        - Plots:
          - Coast 33,34:
            - Owner: Greece
          - Coast 33,35:
            - Owner: Greece
            - Resource: Fish
          - Coast 34,36:
            - Owner: Greece
          - Ocean 33,37:
            - Owner: Greece
        
        ### 57
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16940
        - Player: 4: Carthage
        - Plots:
          - Plains Land 29,35:
            - Owner: Greece
            - CityID: 6999
            - Population: 24
            - City: Hippo Regius
            - Religion: Islam
            - Route: Railroad
          - Coast 30,34:
            - Owner: Greece
          - Coast 29,33:
            - Owner: Greece
          - Coast 30,32:
            - Owner: Carthage
          - Coast 31,32:
            - Owner: Carthage
        
        ### 58
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 15575
        - Player: 4: Carthage
        - Plots:
          - Coast 23,32:
            - Owner: Greece
          - Coast 22,33:
            - Owner: Greece
          - Desert Hills 23,34:
            - Owner: Greece
            - CityID: 7854
            - Population: 23
            - IsRiver: true
            - City: Carthage
            - Religion: Islam
            - Route: Railroad
        
        ### 59
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16236
        - Player: 4: Carthage
        - Plots:
          - Grass Land 27,27:
            - Owner: Greece
            - CityID: 8484
            - Population: 21
            - IsRiver: true
            - City: Shushan
            - Route: Railroad
          - Coast 28,28:
            - Owner: Greece
          - Coast 28,29:
            - Owner: Greece
          - Coast 29,30:
            - Owner: Greece
        
        ### 60
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16686
        - Player: 4: Carthage
        - Plots:
          - Coast 44,18:
            - Owner: Greece
          - Ocean 43,19:
            - Owner: Greece
          - Ocean 43,20:
            - Owner: Greece
        
        ### 61
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 15167
        - Player: 4: Carthage
        - Plots:
          - Coast 29,30:
            - Owner: Greece
          - Coast 30,30:
            - Owner: Carthage
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 31,30:
            - Owner: Carthage
          - Coast 32,30:
            - Owner: Carthage
        
        ### 62
        - Type: PlayerTradeRouteCompleted
        - Domain: 0
        - OriginPlayer: 4: Carthage
        - DestinationCity:
          - Name: Shushan
          - Population: 21
          - ID: 8484
        - DestinationPlayer: 6: Greece
        - OriginCity:
          - Name: Gades
          - Population: 32
          - ID: 2518
        - Connection: Food
        
        ### 63
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 15438
        - Player: 4: Carthage
        - Plots:
          - Coast 30,25:
            - Owner: Greece
          - Coast 31,24:
            - Owner: Greece
          - Grass Land 31,23:
            - Owner: Greece
            - CityID: 13214
            - Population: 16
            - City: Knossos
            - Resource: Rice
            - Religion: Islam
            - Route: Railroad
        
        ### 64
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16634
        - Player: 4: Carthage
        - Plots:
          - Desert Land 48,17:
            - Owner: Greece
            - CityID: 11110
            - Population: 18
            - IsRiver: true
            - City: Borsippa
            - Religion: Catholicism
            - Route: Railroad
          - Coast 49,18:
            - Owner: Greece
          - Coast 48,19:
            - Owner: Greece
          - Coast 48,20:
            - Owner: Greece
        
        ### 65
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 8%
          - AI: FastAttack
          - Unit: Landship
          - ID: 14959
        - Player: 4: Carthage
        - Plots:
          - Desert Land 13,35:
            - Owner: Ethiopia
            - Feature: Oasis
          - Desert Land 14,34:
            - Owner: Ethiopia
            - IsRiver: true
            - Feature: Flood Plains
          - Desert Land 13,33:
            - IsRiver: true
            - Feature: Flood Plains
        
        ### 66
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - Health: 43%
          - AI: Defense
          - Unit: Fusilier
          - ID: 10135
        - Player: 4: Carthage
        - Plots:
          - Ocean 24,28:
            - Owner: Greece
          - Ocean 23,27:
            - Owner: Greece
        
        ### 67
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: CityBombard
          - Unit: Field Gun
          - ID: 11226
        - Player: 4: Carthage
        - Plots:
          - Coast 20,31:
            - Owner: Greece
          - Ocean 21,31:
            - Owner: Greece
          - Ocean 22,30:
            - Owner: Greece
          - Ocean 22,29:
            - Owner: Greece
          - Ocean 23,28:
            - Owner: Greece
        
        ### 68
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 15912
        - Player: 4: Carthage
        - Plots:
          - Ocean 25,26:
            - Owner: Greece
          - Ocean 24,26:
            - Owner: Greece
          - Ocean 23,26:
            - Owner: Greece
        
        ### 69
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Defense
          - Unit: Rifleman
          - ID: 16051
        - Player: 4: Carthage
        - Plots:
          - Coast 27,28:
            - Owner: Greece
          - Coast 26,27:
            - Owner: Greece
          - Ocean 25,27:
            - Owner: Greece
          - Ocean 25,26:
            - Owner: Greece
          - Ocean 24,26:
            - Owner: Greece
        
        ### 70
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 16046
        - Player: 4: Carthage
        - Plots:
          - Coast 26,26:
            - Owner: Greece
          - Coast 25,25:
            - Owner: Greece
          - Ocean 24,25:
            - Owner: Greece
          - Ocean 23,25:
            - Owner: Greece
        
        ### 71
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 16336
        - Player: 4: Carthage
        - Plots:
          - Coast 26,28:
            - Owner: Greece
          - Ocean 25,27:
            - Owner: Greece
          - Ocean 24,27:
            - Owner: Greece
          - Ocean 24,26:
            - Owner: Greece
          - Ocean 23,25:
            - Owner: Greece
        
        ### 72
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Defense
          - Unit: Rifleman
          - ID: 16048
        - Player: 4: Carthage
        - Plots:
          - Coast 26,27:
            - Owner: Greece
          - Coast 26,26:
            - Owner: Greece
          - Ocean 25,26:
            - Owner: Greece
          - Ocean 24,26:
            - Owner: Greece
          - Ocean 23,26:
            - Owner: Greece
        
        ### 73
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 15912
        - Player: 4: Carthage
        
        ### 74
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AssaultSea
          - Unit: Cruiser
          - ID: 16751
        - Player: 4: Carthage
        - Plots:
          - Ocean 25,27:
            - Owner: Greece
          - Ocean 25,26:
            - Owner: Greece
          - Ocean 24,26:
            - Owner: Greece
          - Ocean 23,26:
            - Owner: Greece
        
        ### 75
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Defense
          - Unit: Rifleman
          - ID: 16049
        - Player: 4: Carthage
        - Plots:
          - Coast 26,28:
            - Owner: Greece
          - Ocean 25,27:
            - Owner: Greece
          - Ocean 25,26:
            - Owner: Greece
          - Ocean 24,26:
            - Owner: Greece
          - Ocean 23,25:
            - Owner: Greece
        
        ### 76
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Defense
          - Unit: Rifleman
          - ID: 16050
        - Player: 4: Carthage
        - Plots:
          - Ocean 25,27:
            - Owner: Greece
          - Ocean 24,27:
            - Owner: Greece
          - Ocean 23,27:
            - Owner: Greece
          - Ocean 22,27:
            - Owner: Greece
        
        ### 77
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 14046
        - Player: 4: Carthage
        - Grass Land 28,27:
          - Owner: Greece
          - IsRiver: true
          - Improvement: Lumber Mill
          - Route: Road
          - Feature: Jungle
        
        ### 78
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: CityBombard
          - Unit: Field Gun
          - ID: 10463
        - Player: 4: Carthage
        - Plots:
          - Ocean 25,27:
            - Owner: Greece
          - Ocean 25,26:
            - Owner: Greece
          - Ocean 24,25:
            - Owner: Greece
          - Ocean 23,25:
            - Owner: Greece
        
        ### 79
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Ranged
          - Unit: Cavalry
          - ID: 12165
        - Player: 4: Carthage
        
        ### 80
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Diplomat
          - Unit: Great Diplomat
          - ID: 16873
        - Player: 4: Carthage
        
        ### 81
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 76%
          - AI: AssaultSea
          - Unit: Cruiser
          - ID: 16124
        - Player: 4: Carthage
        
        ### 82
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 13366
        - Player: 4: Carthage
        - Plots:
          - Grass Land 29,32:
            - Owner: Greece
            - Improvement: Lumber Mill
            - Route: Road
            - Feature: Forest
          - Coast 29,31:
            - Owner: Carthage
        
        ### 83
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: FastAttack
          - Unit: Commando
          - ID: 13735
        - Player: 4: Carthage
        - Grass Hills 32,29:
          - Owner: Carthage
          - Improvement: Lumber Mill
          - Feature: Jungle
        
        ### 84
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 16553
        - Player: 4: Carthage
        
        ### 85
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 16872
        - Player: 4: Carthage
        - Plots:
          - Coast 19,31:
            - Owner: Greece
          - Coast 20,32:
            - Owner: Greece
          - Coast 21,32:
            - Owner: Greece
          - Desert Land 21,33:
            - Owner: Greece
            - Improvement: Fort
          - Desert Hills 22,34:
            - Owner: Greece
            - Resource: Sheep
            - Improvement: Manufactory
            - Route: Railroad
          - Desert Hills 23,34:
            - Owner: Greece
            - CityID: 7854
            - Population: 23
            - IsRiver: true
            - City: Carthage
            - Religion: Islam
            - Route: Railroad
          - Desert Hills 23,35:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 24,36:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 24,37:
            - Owner: Greece
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 25,38:
            - Owner: Greece
            - Improvement: Village
            - Route: Railroad
          - Grass Land 25,39:
            - Owner: Greece
            - CityID: 3363
            - Population: 25
            - IsRiver: true
            - City: Utique
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Plains Hills 26,39:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 27,39:
            - Owner: Greece
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Road
        
        ### 86
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 17011
        - Player: 4: Carthage
        - Plots:
          - Coast 32,30:
            - Owner: Carthage
          - Coast 31,30:
            - Owner: Carthage
          - Coast 30,30:
            - Owner: Carthage
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 29,30:
            - Owner: Greece
          - Coast 28,29:
            - Owner: Greece
        
        ### 87
        - Type: MakePeace
        - PacifierFlag: true
        - OriginatingPlayer: 5: Mongolia
        - TargetTeam: 25
        
        ### 88
        - Type: MakePeace
        - PacifierFlag: true
        - OriginatingPlayer: 5: Mongolia
        - TargetTeam: 25
        
        ### 89
        - Type: MakePeace
        - PacifierFlag: true
        - OriginatingPlayer: 5: Mongolia
        - TargetTeam: 25
        
        ### 90
        - Type: MakePeace
        - PacifierFlag: true
        - OriginatingPlayer: 5: Mongolia
        - TargetTeam: 25
        
        ### 91
        - Type: MakePeace
        - PacifierFlag: true
        - OriginatingPlayer: 5: Mongolia
        - TargetTeam: 25
        
        ### 92
        - Type: MakePeace
        - PacifierFlag: true
        - OriginatingPlayer: 5: Mongolia
        - TargetTeam: 25
        
        ### 93
        - Type: CityConvertsReligion
        - City:
          - Owner: Mongolia
          - CityID: 1062
          - Population: 40
          - IsRiver: true
          - City: Karakorum
          - Terrain: Desert
          - Religion: Tengriism
          - Route: Railroad
          - Plot: Hills
          - X: 50
          - Y: 41
        - Owner: 5: Mongolia
        - Religion: Tengriism
        
        ### 94
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14795
        - Player: 5: Mongolia
        
        ### 95
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Settle
          - Unit: Colonist
          - ID: 9685
        - Player: 5: Mongolia
        
        ### 96
        - Type: PlayerDoneTurn
        - NextPlayer: 6: Greece
        - Player: 5: Mongolia
        
        ### 97
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Diplomat
          - ID: 17022
        - Player: 6: Greece
        - Tundra Hills 27,47:
          - Owner: Greece
          - CityID: 1063
          - Population: 35
          - IsRiver: true
          - City: Athens
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 98
        - Type: UnitCreated
        - UnitType: Diplomat
        - Player: 6: Greece
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 17022
        - Tundra Hills 27,47:
          - Owner: Greece
          - CityID: 1063
          - Population: 35
          - IsRiver: true
          - City: Athens
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 99
        - Type: CityTrained
        - WithGold: true
        - Player: 6: Greece
        - City:
          - Name: Athens
          - Population: 35
          - ID: 1063
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 17022
        
        ### 100
        - Type: CityEventChoiceEnded
        - City:
          - Name: Corinth
          - Population: 27
          - ID: 1342
        - Player: 6: Greece
        - Choice: 80
        
        ### 101
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Diplomat
          - ID: 17029
        - Player: 6: Greece
        - Desert Hills 28,42:
          - Owner: Greece
          - CityID: 1342
          - Population: 27
          - IsRiver: true
          - City: Corinth
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 102
        - Type: UnitCreated
        - UnitType: Diplomat
        - Player: 6: Greece
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 17029
        - Desert Hills 28,42:
          - Owner: Greece
          - CityID: 1342
          - Population: 27
          - IsRiver: true
          - City: Corinth
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 103
        - Type: CityTrained
        - Player: 6: Greece
        - City:
          - Name: Corinth
          - Population: 27
          - ID: 1342
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 17029
        
        ### 104
        - Type: CityConstructed
        - City:
          - Name: Shushan
          - Population: 21
          - ID: 8484
        - Owner: 6: Greece
        - Building: Broadcast Tower
        
        ### 105
        - Type: CityBeginsWLTKD
        - Change: 10
        - City:
          - Owner: Greece
          - CityID: 8484
          - Population: 21
          - IsRiver: true
          - City: Shushan
          - Terrain: Grass
          - Route: Railroad
          - Plot: Land
          - X: 27
          - Y: 27
        - Player: 6: Greece
        
        ### 106
        - Type: CityConstructed
        - City:
          - Name: Sippar
          - Population: 18
          - ID: 10621
        - Owner: 6: Greece
        - Building: Broadcast Tower
        
        ### 107
        - Type: CityConstructed
        - City:
          - Name: Opis
          - Population: 15
          - ID: 10817
        - Owner: 6: Greece
        - Building: Public School
        
        ### 108
        - Type: TileOwnershipChanged
        - NewOwner: 6: Greece
        - Ocean 41,19:
          - Owner: Greece
        
        ### 109
        - Type: CityBoughtPlot
        - WithFaithCulture: true
        - Player: 6: Greece
        - City:
          - Name: Opis
          - Population: 15
          - ID: 10817
        - Ocean 41,19:
          - Owner: Greece
        
        ### 110
        - Type: CityConstructed
        - City:
          - Name: Awasa
          - Population: 13
          - ID: 14195
        - Owner: 6: Greece
        - Building: Public School
        
        ### 111
        - Type: TileOwnershipChanged
        - NewOwner: 6: Greece
        - Coast 27,17:
          - Owner: Greece
          - Resource: Fish
        
        ### 112
        - Type: CityBoughtPlot
        - WithFaithCulture: true
        - Player: 6: Greece
        - City:
          - Name: Awasa
          - Population: 13
          - ID: 14195
        - Coast 27,17:
          - Owner: Greece
          - Resource: Fish
        
        ### 113
        - Type: SetPopulation
        - OldPopulation: 13
        - NewPopulation: 14
        - City:
          - Owner: Greece
          - CityID: 14195
          - Population: 14
          - City: Awasa
          - Terrain: Plains
          - Resource: Coal
          - Religion: Islam
          - Route: Railroad
          - Plot: Hills
          - X: 24
          - Y: 21
        
        ### 114
        - Type: CityConstructed
        - City:
          - Name: Gao
          - Population: 18
          - ID: 15451
        - Owner: 6: Greece
        - Building: Customs House
        
        ### 115
        - Type: TeamTechResearched
        - ChangeAmount: 1
        - Team:
          - Player_6: Alexander
          - ID: 6
        - Tech: Plastics
        
        ### 116
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15787
        - Player: 6: Greece
        - Plots:
          - Plains Land 30,46:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 31,46:
            - Owner: Greece
            - CityID: 1181
            - Population: 26
            - IsRiver: true
            - City: Sparta
            - Resource: Furs
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Plains Land 29,47:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
        
        ### 117
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15862
        - Player: 6: Greece
        - Plots:
          - Plains Hills 28,47:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 29,47:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 30,46:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 29,45:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
        
        ### 118
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16577
        - Player: 6: Greece
        - Plots:
          - Coast 18,30:
            - Owner: City-State Zurich
          - Coast 18,31:
            - Owner: Greece
          - Coast 19,31:
            - Owner: Greece
          - Coast 20,31:
            - Owner: Greece
        
        ### 119
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15599
        - Player: 6: Greece
        - Plots:
          - Plains Land 28,26:
            - Owner: Greece
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Hills 28,25:
            - Owner: Greece
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 29,24:
            - Owner: Greece
            - Resource: Marble
            - Improvement: Quarry
            - Route: Railroad
        
        ### 120
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 15120
        - Player: 6: Greece
        - Plots:
          - Coast 46,8:
            - Owner: Greece
          - Coast 46,7:
            - Owner: Greece
          - Coast 47,6:
            - Owner: Greece
          - Plains Hills 48,6:
            - Owner: Greece
            - CityID: 12645
            - Population: 18
            - City: Jenne
            - Resource: Aluminum
            - Religion: Buddhism
            - Route: Railroad
        
        ### 121
        - Type: PlayerTradeRouteCompleted
        - Domain: 0
        - OriginPlayer: 6: Greece
        - OriginCity:
          - Name: Jenne
          - Population: 18
          - ID: 12645
        - DestinationCity:
          - Name: Monaco
          - Population: 14
          - ID: 12340
        - DestinationPlayer: 23
        - Connection: Food
        
        ### 122
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Cargo Ship
          - ID: 17030
        - Player: 6: Greece
        - Plains Hills 48,6:
          - Owner: Greece
          - CityID: 12645
          - Population: 18
          - City: Jenne
          - Resource: Aluminum
          - Religion: Buddhism
          - Route: Railroad
        
        ### 123
        - Type: UnitCreated
        - UnitType: Cargo Ship
        - Player: 6: Greece
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 17030
        - Plains Hills 48,6:
          - Owner: Greece
          - CityID: 12645
          - Population: 18
          - City: Jenne
          - Resource: Aluminum
          - Religion: Buddhism
          - Route: Railroad
        
        ### 124
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16188
        - Player: 6: Greece
        - Plots:
          - Snow Hills 25,46:
            - Owner: Greece
            - Improvement: Mine
            - Route: Railroad
          - Tundra Land 24,46:
            - Owner: Greece
            - CityID: 1584
            - Population: 22
            - IsRiver: true
            - City: Argos
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Tundra Hills 26,46:
            - Owner: Greece
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 27,46:
            - Owner: Greece
            - IsRiver: true
            - Resource: Furs
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
          - Tundra Hills 27,47:
            - Owner: Greece
            - CityID: 1063
            - Population: 35
            - IsRiver: true
            - City: Athens
            - Religion: Eastern Orthodoxy
            - Route: Railroad
        
        ### 125
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16426
        - Player: 6: Greece
        - Plots:
          - Snow Hills 23,46:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 22,45:
            - Owner: Greece
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Manufactory
            - Route: Railroad
          - Tundra Land 22,44:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Tundra Hills 21,43:
            - Owner: Greece
            - IsRiver: true
        
        ### 126
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16509
        - Player: 6: Greece
        - Plots:
          - Plains Land 28,26:
            - Owner: Greece
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Hills 28,25:
            - Owner: Greece
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 29,24:
            - Owner: Greece
            - Resource: Marble
            - Improvement: Quarry
            - Route: Railroad
          - Grass Land 29,23:
            - Owner: Greece
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Plains Land 30,23:
            - Owner: Greece
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 31,23:
            - Owner: Greece
            - CityID: 13214
            - Population: 16
            - City: Knossos
            - Resource: Rice
            - Religion: Islam
            - Route: Railroad
        
        ### 127
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16510
        - Player: 6: Greece
        - Plots:
          - Tundra Land 27,46:
            - Owner: Greece
            - IsRiver: true
            - Resource: Furs
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
          - Tundra Hills 26,46:
            - Owner: Greece
            - Improvement: Village
            - Route: Railroad
          - Snow Hills 25,46:
            - Owner: Greece
            - Improvement: Mine
            - Route: Railroad
          - Tundra Land 24,46:
            - Owner: Greece
            - CityID: 1584
            - Population: 22
            - IsRiver: true
            - City: Argos
            - Religion: Eastern Orthodoxy
            - Route: Railroad
        
        ### 128
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16578
        - Player: 6: Greece
        - Plots:
          - Plains Land 26,43:
            - Owner: Greece
            - Resource: Wheat
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 27,42:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 26,41:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 26,40:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 25,39:
            - Owner: Greece
            - CityID: 3363
            - Population: 25
            - IsRiver: true
            - City: Utique
            - Religion: Eastern Orthodoxy
            - Route: Railroad
        
        ### 129
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15991
        - Player: 6: Greece
        - Plots:
          - Plains Hills 51,10:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Mine
            - Route: Road
          - Grass Land 51,11:
            - Owner: Babylon
            - CityID: 1293
            - Population: 23
            - IsRiver: true
            - City: Dur-Kurigalzu
            - Religion: Catholicism
            - Route: Railroad
          - Plains Land 50,9:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
        
        ### 130
        - Type: PlayerDoTurn
        - Player: 6: Greece
        
        ### 131
        - Type: UnitPromoted
        - Unit:
          - Level: 4
          - Health: 92%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 12089
        - Player: 6: Greece
        - Promotion: Accuracy III
        
        ### 132
        - Type: UnitPromoted
        - Unit:
          - Level: 5
          - Health: 92%
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 16708
        - Player: 6: Greece
        - Promotion: Air Logistics
        
        ### 133
        - Type: CombatResult
        - Plains Land 17,37:
          - Owner: Ethiopia
          - CityID: 1187
          - Population: 20
          - IsRiver: true
          - City: Harar
          - Resource: Wheat
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 33
          - Damage: 378
          - Player: 7: Ethiopia
        
        ### 134
        - Type: TileRouteChanged
        - OldRoute: 1
        - NewRoute: 1
        - IsPillaged: true
        - Owner: 7: Ethiopia
        - Plains Hills 16,39:
          - Owner: Ethiopia
          - Resource: Aluminum
          - Improvement: Holy Site
          - Route: Railroad
        
        ### 135
        - Type: CombatResult
        - Tundra Hills 17,40:
          - Owner: Ethiopia
          - Resource: Sheep
          - Improvement: Pasture
          - Route: Railroad
        - Attacker:
          - RemainingHP: 5
          - Damage: 5
        - Defender:
          - RemainingHP: 110
          - Damage: 149
          - Player: 7: Ethiopia
          - Unit:
            - Level: 4
            - Health: 61%
            - AI: Counter
            - Unit: Anti-Aircraft Gun
            - ID: 16201
        
        ### 136
        - Type: UnitKilledInCombat
        - KilledPlayer: 7: Ethiopia
        - KillerPlayer: 6: Greece
        - KilledUnit: Anti-Aircraft Gun
        
        ### 137
        - Type: UnitMoved
        - Unit:
          - Level: 7
          - Health: 95%
          - AI: FastAttack
          - Unit: T-34
          - ID: 13588
        - Player: 6: Greece
        - Tundra Hills 17,40:
          - Owner: Ethiopia
          - Resource: Sheep
          - Improvement: Pasture
          - Route: Railroad
        
        ### 138
        - Type: CombatResult
        - Plains Land 17,37:
          - Owner: Ethiopia
          - CityID: 1187
          - Population: 20
          - IsRiver: true
          - City: Harar
          - Resource: Wheat
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 21
          - Damage: 399
          - Player: 7: Ethiopia
        
        ### 139
        - Type: CombatResult
        - Plains Land 17,37:
          - Owner: Ethiopia
          - CityID: 1187
          - Population: 20
          - IsRiver: true
          - City: Harar
          - Resource: Wheat
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 15
          - Damage: 38
        - Defender:
          - RemainingHP: 36
          - Damage: 435
          - Player: 7: Ethiopia
        
        ### 140
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 65%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 15719
        - Player: 6: Greece
        - Plots:
          - Coast 28,29:
            - Owner: Greece
          - Coast 28,28:
            - Owner: Greece
          - Coast 27,28:
            - Owner: Greece
          - Coast 26,27:
            - Owner: Greece
          - Ocean 25,27:
            - Owner: Greece
          - Ocean 25,26:
            - Owner: Greece
        
        ### 141
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 99%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 15130
        - Player: 6: Greece
        - Plots:
          - Coast 27,28:
            - Owner: Greece
          - Coast 26,28:
            - Owner: Greece
          - Ocean 25,27:
            - Owner: Greece
          - Ocean 25,26:
            - Owner: Greece
          - Ocean 24,26:
            - Owner: Greece
        
        ### 142
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Admiral
          - Unit: Great Admiral
          - ID: 9693
        - Player: 6: Greece
        - Plots:
          - Coast 27,28:
            - Owner: Greece
          - Coast 26,28:
            - Owner: Greece
          - Ocean 25,27:
            - Owner: Greece
          - Ocean 25,26:
            - Owner: Greece
          - Ocean 24,26:
            - Owner: Greece
        
        ### 143
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 16508
        - Player: 6: Greece
        - Plots:
          - Coast 29,30:
            - Owner: Greece
          - Coast 28,30:
            - Owner: Greece
          - Ocean 27,29:
            - Owner: Greece
          - Ocean 26,29:
            - Owner: Greece
          - Ocean 25,29:
            - Owner: Greece
        
        ### 144
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 16571
        - Player: 6: Greece
        - Plots:
          - Coast 30,28:
            - Owner: Carthage
          - Coast 30,29:
            - Owner: Carthage
          - Coast 30,30:
            - Owner: Carthage
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 29,30:
            - Owner: Greece
          - Coast 28,30:
            - Owner: Greece
        
        ### 145
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 16572
        - Player: 6: Greece
        - Plots:
          - Coast 30,29:
            - Owner: Carthage
          - Coast 30,30:
            - Owner: Carthage
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 29,30:
            - Owner: Greece
          - Coast 28,30:
            - Owner: Greece
          - Coast 27,30:
            - Owner: Greece
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 146
        - Type: UnitMoved
        - Unit:
          - Level: 10
          - AI: Ranged
          - Unit: Light Tank
          - ID: 12933
        - Player: 6: Greece
        - Desert Land 58,8:
          - Owner: Songhai
          - Route: Railroad
          - Feature: Oasis
        
        ### 147
        - Type: UnitMoved
        - Unit:
          - Level: 9
          - Health: 77%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 12093
        - Player: 6: Greece
        - Plains Land 58,9:
          - Owner: Songhai
          - Resource: Wheat
          - Improvement: Farm
          - Route: Railroad
        
        ### 148
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 83%
          - AI: FastAttack
          - Unit: Tank
          - ID: 15131
        - Player: 6: Greece
        - Plains Land 57,9:
          - Owner: Songhai
          - Improvement: Farm
        
        ### 149
        - Type: UnitMoved
        - Unit:
          - Level: 8
          - Health: 98%
          - AI: FastAttack
          - Unit: T-34
          - ID: 13488
        - Player: 6: Greece
        - Plots:
          - Tundra Land 61,5:
            - Owner: Songhai
            - Resource: Deer
            - Improvement: Camp
            - Route: Road
            - Feature: Forest
          - Plains Land 62,6:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Maize
            - Improvement: Farm
          - Plains Land 61,7:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Farm
        
        ### 150
        - Type: CombatResult
        - Plains Hills 59,9:
          - Owner: Songhai
          - CityID: 1776
          - Population: 25
          - City: Taghaza
          - Religion: Buddhism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 21
          - Damage: 118
          - Player: 0: Songhai
        
        ### 151
        - Type: UnitMoved
        - Unit:
          - Level: 10
          - AI: Ranged
          - Unit: Light Tank
          - ID: 12933
        - Player: 6: Greece
        - Plains Land 58,9:
          - Owner: Songhai
          - Resource: Wheat
          - Improvement: Farm
          - Route: Railroad
        
        ### 152
        - Type: UnitMoved
        - Unit:
          - Level: 9
          - Health: 77%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 12093
        - Player: 6: Greece
        - Desert Land 58,8:
          - Owner: Songhai
          - Route: Railroad
          - Feature: Oasis
        
        ### 153
        - Type: CombatResult
        - Plains Hills 59,9:
          - Owner: Songhai
          - CityID: 1776
          - Population: 25
          - City: Taghaza
          - Religion: Buddhism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 17
          - Damage: 135
          - Player: 0: Songhai
        
        ### 154
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 83%
          - AI: FastAttack
          - Unit: Tank
          - ID: 15131
        - Player: 6: Greece
        - Plains Land 58,9:
          - Owner: Songhai
          - Resource: Wheat
          - Improvement: Farm
          - Route: Railroad
        
        ### 155
        - Type: UnitMoved
        - Unit:
          - Level: 10
          - AI: Ranged
          - Unit: Light Tank
          - ID: 12933
        - Player: 6: Greece
        - Plains Land 57,9:
          - Owner: Songhai
          - Improvement: Farm
        
        ### 156
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 9371
        - Player: 6: Greece
        - Plots:
          - Desert Land 58,8:
            - Owner: Songhai
            - Route: Railroad
            - Feature: Oasis
          - Plains Land 57,9:
            - Owner: Songhai
            - Improvement: Farm
        
        ### 157
        - Type: CombatResult
        - Plains Hills 59,9:
          - Owner: Songhai
          - CityID: 1776
          - Population: 25
          - City: Taghaza
          - Religion: Buddhism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 14
          - Damage: 149
          - Player: 0: Songhai
        
        ### 158
        - Type: UnitMoved
        - Unit:
          - Level: 8
          - Health: 98%
          - AI: FastAttack
          - Unit: T-34
          - ID: 13488
        - Player: 6: Greece
        - Plots:
          - Plains Land 61,8:
            - Owner: Songhai
            - Improvement: Manufactory
          - Plains Hills 60,9:
            - Owner: Songhai
            - Improvement: Mine
        
        ### 159
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 94%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 12180
        - Player: 6: Greece
        - Plains Land 31,6:
          - Owner: Babylon
          - Resource: Coffee
          - Improvement: Plantation
          - Route: Road
        
        ### 160
        - Type: CombatResult
        - Plains Land 32,4:
          - IsRiver: true
          - Resource: Iron
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 37
          - Damage: 100
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 37%
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 16976
        
        ### 161
        - Type: UnitKilledInCombat
        - KilledPlayer: 63: Barbarians
        - KillerPlayer: 6: Greece
        - KilledUnit: Machine Gun
        
        ### 162
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 71%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 16420
        - Player: 6: Greece
        - Plots:
          - Ocean 15,15:
            - Owner: Ethiopia
          - Coast 15,16:
            - Owner: Ethiopia
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 163
        - Type: TileImprovementChanged
        - Owner: 7: Ethiopia
        - OldImprovement: Fishing Boats
        - Coast 15,16:
          - Owner: Ethiopia
          - Resource: Fish
        
        ### 164
        - Type: CombatResult
        - Grass Land 27,13:
          - Improvement: Barbarian Encampment
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 29
          - Damage: 96
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 44%
            - AI: Defense
            - Unit: Rifleman
            - ID: 16592
        
        ### 165
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 37%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 12260
        - Player: 6: Greece
        - Tundra Land 15,50:
          - IsRiver: true
          - Resource: Deer
          - Feature: Forest
        
        ### 166
        - Type: CombatResult
        - Attacker:
          - RemainingHP: 30
          - Damage: 82
        - Defender:
          - RemainingHP: 38
          - Damage: 38
          - Unit:
            - Level: 3
            - AI: AttackSea
            - Unit: Destroyer
            - ID: 14826
          - Player: 28
        
        ### 167
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 16648
        - Player: 6: Greece
        - Plots:
          - Coast 46,27:
            - Owner: Greece
          - Coast 46,28:
            - Owner: Greece
        
        ### 168
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Defense
          - Unit: Infantry
          - ID: 13755
        - Player: 6: Greece
        - Plains Land 53,7:
          - Owner: Greece
          - Improvement: Lumber Mill
          - Route: Railroad
          - Feature: Forest
        
        ### 169
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 84%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13489
        - Player: 6: Greece
        - Plots:
          - Tundra Land 57,2:
            - Owner: Greece
            - IsRiver: true
            - Resource: Lapis Lazuli
            - Improvement: Quarry
          - Tundra Land 58,2:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
        
        ### 170
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16062
        - Player: 6: Greece
        - Plots:
          - Coast 14,31:
            - Owner: City-State Zurich
          - Coast 15,30:
            - Owner: City-State Zurich
          - Coast 15,29:
            - Owner: City-State Zurich
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 15,28:
            - Owner: Ethiopia
          - Grass Land 14,27:
            - Owner: Ethiopia
            - IsRiver: true
        
        ### 171
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16695
        - Player: 6: Greece
        - Desert Hills 19,32:
          - Owner: Greece
        
        ### 172
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 83%
          - AI: FastAttack
          - Unit: Tank
          - ID: 15131
        - Player: 6: Greece
        - Plots:
          - Desert Land 58,8:
            - Owner: Songhai
            - Route: Railroad
            - Feature: Oasis
          - Plains Land 57,7:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 56,7:
            - Owner: Greece
            - Improvement: Fort
            - Route: Railroad
          - Plains Land 55,7:
            - Owner: Greece
            - Route: Railroad
          - Plains Land 55,6:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
          - Plains Hills 55,5:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
          - Plains Land 56,4:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 56,3:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Holy Site
        
        ### 173
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16818
        - Player: 6: Greece
        - Plots:
          - Desert Land 19,33:
            - Owner: Greece
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Citadel
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 18,33:
            - Owner: Greece
        
        ### 174
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16503
        - Player: 6: Greece
        - Plots:
          - Desert Land 21,35:
            - Owner: Greece
            - Route: Railroad
            - Feature: Oasis
          - Desert Hills 20,35:
            - Owner: Greece
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 20,34:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 19,34:
            - Owner: Greece
            - IsRiver: true
            - Resource: Amber
            - Improvement: Quarry
        
        ### 175
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 12094
        - Player: 6: Greece
        - Desert Land 14,34:
          - Owner: Ethiopia
          - IsRiver: true
          - Feature: Flood Plains
        
        ### 176
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 39%
          - AI: Defense
          - Unit: Infantry
          - ID: 13644
        - Player: 6: Greece
        - Tundra Hills 31,3:
          - Resource: Sheep
        
        ### 177
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 12344
        - Player: 6: Greece
        - Grass Land 32,7:
          - Improvement: Village
        
        ### 178
        - Type: UnitMoved
        - Unit:
          - Level: 10
          - AI: Ranged
          - Unit: Light Tank
          - ID: 12933
        - Player: 6: Greece
        - Plots:
          - Plains Land 57,10:
            - Owner: Babylon
            - Improvement: Village
            - Route: Road
          - Plains Land 56,10:
            - Owner: Babylon
            - IsRiver: true
            - Resource: Aluminum
            - Improvement: Mine
            - Route: Railroad
        
        ### 179
        - Type: UnitMoved
        - Unit:
          - Level: 9
          - Health: 77%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 12093
        - Player: 6: Greece
        - Plots:
          - Plains Land 57,7:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 56,7:
            - Owner: Greece
            - Improvement: Fort
            - Route: Railroad
          - Plains Land 55,7:
            - Owner: Greece
            - Route: Railroad
          - Plains Land 55,6:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
          - Grass Land 54,6:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 53,7:
            - Owner: Greece
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 52,7:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Citadel
            - Route: Road
        
        ### 180
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 66%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 14003
        - Player: 6: Greece
        - Plots:
          - Ocean 16,15:
            - Owner: Ethiopia
        
        ### 181
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 78%
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 16830
        - Player: 6: Greece
        
        ### 182
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 62%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 16707
        - Player: 6: Greece
        - Plots:
          - Coast 49,25:
            - Owner: Greece
            - Resource: Pearls
            - Improvement: Fishing Boats
        
        ### 183
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 82%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 16892
        - Player: 6: Greece
        - Plots:
          - Coast 50,27:
            - Resource: Fish
        
        ### 184
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 88%
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 16891
        - Player: 6: Greece
        - Plots:
          - Ocean 48,25:
            - Owner: Greece
          - Coast 49,26:
            - Owner: Greece
          - Coast 50,27:
            - Resource: Fish
        
        ### 185
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 9371
        - Player: 6: Greece
        - Plains Land 57,10:
          - Owner: Babylon
          - Improvement: Village
          - Route: Road
        
        ### 186
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 84%
          - AI: Explore
          - Unit: Paratrooper
          - ID: 14371
        - Player: 6: Greece
        - Coast 35,16:
          - Resource: Fish
        
        ### 187
        - Type: BarbariansCampCleared
        - Player: 6: Greece
        - Desert Land 35,15:
          - Resource: Stone
          - Improvement: Barbarian Encampment
        
        ### 188
        - Type: TileImprovementChanged
        - OldImprovement: Barbarian Encampment
        - Desert Land 35,15:
          - Resource: Stone
        
        ### 189
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 84%
          - AI: Explore
          - Unit: Paratrooper
          - ID: 14371
        - Player: 6: Greece
        - Desert Land 35,15:
          - Resource: Stone
        
        ### 190
        - Type: RebaseTo
        - Player: 6: Greece
        - Unit:
          - Level: 4
          - Health: 79%
          - AI: AttackAir
          - Unit: Bomber
          - ID: 14902
        - Desert Hills 28,42:
          - Owner: Greece
          - CityID: 1342
          - Population: 27
          - IsRiver: true
          - City: Corinth
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 191
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 79%
          - AI: AttackAir
          - Unit: Bomber
          - ID: 14902
        - Player: 6: Greece
        - Desert Hills 28,42:
          - Owner: Greece
          - CityID: 1342
          - Population: 27
          - IsRiver: true
          - City: Corinth
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 192
        - Type: RebaseTo
        - Player: 6: Greece
        - Unit:
          - Level: 4
          - Health: 76%
          - AI: AttackAir
          - Unit: Bomber
          - ID: 15517
        - Desert Hills 28,42:
          - Owner: Greece
          - CityID: 1342
          - Population: 27
          - IsRiver: true
          - City: Corinth
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 193
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 76%
          - AI: AttackAir
          - Unit: Bomber
          - ID: 15517
        - Player: 6: Greece
        - Desert Hills 28,42:
          - Owner: Greece
          - CityID: 1342
          - Population: 27
          - IsRiver: true
          - City: Corinth
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 194
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 13871
        - Player: 6: Greece
        - Plots:
          - Coast 45,23:
            - Owner: Greece
          - Ocean 46,22:
            - Owner: Greece
          - Coast 46,21:
            - Owner: Greece
          - Coast 47,20:
            - Owner: Greece
          - Desert Hills 47,19:
            - Owner: Greece
            - Resource: Sheep
            - Improvement: Pasture
        
        ### 195
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Destroyer
          - ID: 17031
        - Player: 6: Greece
        - Ocean 24,26:
          - Owner: Greece
        
        ### 196
        - Type: UnitCreated
        - UnitType: Destroyer
        - Player: 6: Greece
        - Unit:
          - Level: 1
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 17031
        - Ocean 24,26:
          - Owner: Greece
        
        ### 197
        - Type: UnitUpgraded
        - Player: 6: Greece
        - OldUnit:
          - Level: 4
          - Health: 99%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 15130
        - NewUnit:
          - Level: 1
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 17031
        
        ### 198
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 6: Greece
        - OriginalUnit:
          - Level: 4
          - Health: 99%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 15130
        - NewOwner: 6: Greece
        - ConvertingUnit:
          - Level: 4
          - Health: 99%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 17031
        
        ### 199
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 87%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 16774
        - Player: 6: Greece
        - Plots:
          - Ocean 43,22:
            - Owner: Greece
          - Coast 44,22:
            - Owner: Greece
          - Coast 45,22:
            - Owner: Greece
          - Ocean 46,22:
            - Owner: Greece
          - Coast 47,22:
            - Owner: Greece
        
        ### 200
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 16957
        - Player: 6: Greece
        - Plots:
          - Coast 12,31:
            - Owner: City-State Zurich
            - Feature: Atoll
        
        ### 201
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 17029
        - Player: 6: Greece
        - Plots:
          - Plains Land 28,41:
            - Owner: Greece
            - IsRiver: true
            - Resource: Bison
            - Improvement: Citadel
            - Route: Road
          - Grass Land 29,40:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
          - Grass Land 30,40:
            - Owner: City-State Manila
            - Improvement: Farm
          - Plains Land 31,40:
            - Owner: City-State Manila
            - Improvement: Village
            - Route: Railroad
        
        ### 202
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Cargo Ship
          - ID: 17032
        - Player: 6: Greece
        - Plains Hills 48,6:
          - Owner: Greece
          - CityID: 12645
          - Population: 18
          - City: Jenne
          - Resource: Aluminum
          - Religion: Buddhism
          - Route: Railroad
        
        ### 203
        - Type: UnitCreated
        - UnitType: Cargo Ship
        - Player: 6: Greece
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 17032
        - Plains Hills 48,6:
          - Owner: Greece
          - CityID: 12645
          - Population: 18
          - City: Jenne
          - Resource: Aluminum
          - Religion: Buddhism
          - Route: Railroad
        
        ### 204
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 17032
        - Player: 6: Greece
        - Plots:
          - Coast 47,6:
            - Owner: Greece
          - Coast 46,7:
            - Owner: Greece
          - Coast 46,8:
            - Owner: Greece
          - Coast 46,9:
            - Owner: Greece
          - Coast 47,10:
            - Owner: City-State Monaco
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 205
        - Type: UnitBuildCompleted
        - Owner: 6: Greece
        - Unit:
          - Level: 1
          - AI: Archaeologist
          - Unit: Archaeologist
          - ID: 16574
        - Build: Construct an Archaeological Dig
        - Tundra Hills 51,3:
          - Owner: Greece
          - Resource: Antiquity Site
        
        ### 206
        - Type: PlayerDoneTurn
        - NextPlayer: 7: Ethiopia
        - Player: 6: Greece
        
        You, Alexander (leader of Greece, Player 6), are making strategic decisions after turn 401.
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
      - Cities: summary reports about discovered cities in the world.
        - Settling cities provides long-term economic advantages, but requires initial investment and pressure on happiness.
      - Military: summary reports about tactical zones and visible units.
        - Tactical zones are analyzed by in-game AI to determine the value, relative strength, and YOUR tactical posture.
        - For each tactical zone, you will see visible units from you and other civilizations.
      - Events: events since the last decision-making.
    - You are Alexander, leader of Greece (Player 6).
      
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
      - Name: Greece
      - Uniques:
        - Unique Unit: Hoplite, Replacing Spearman (Requires technology: Bronze Working)
        - Unique Unit: Klepht, Replacing Commando (Requires technology: Railroad)
        - Unique Building: Gymnasion, Replacing Amphitheater (Requires technology: Drama and Poetry)
        - Unique Building: Parthenon, Replacing Scrivener's Office (Requires technology: Writing)
        - Civilization Ability:  Influence degrades at half and recovers at twice the normal rate. +5% Combat Strength of owned and Allied Units for each City-State alliance (up to +25%). Treat neutral City-State territory as friendly territory.
      - Leader: Alexander
      - PlayerID: 6
      
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
      - Refrigeration: Allows Work Boats to construct an Offshore Platform, and increases Trade Route maximum travel distance.
        Completing it would unlock: Electronics, Computers
      - Nuclear Fission: Allows you to build the Bazooka, the most powerful ranged Unit and Atomic Bombs, the first nuclear weapon in the game (note: you must first have completed the Manhattan Project and have Uranium available). Also allows you to build the Nuclear Plant, a building which requires Uranium and increases the Production of a City.
        Completing it would unlock: Satellites, Advanced Ballistics
      - Penicillin: All Workers receive the Fallout Reduction Promotion, which reduces the amount of damage they take while scrubbing Fallout. Allows you to build the Marine, a Unit that specializes in amphibious assaults. Also allows you to build the Medical Lab, a building which speeds the growth of your Cities.
        Completing it would unlock: Electronics
      - Mobile Tactics: Allows you to build the Mechanized Infantry, a fast and versatile late game Unit that doesn't require any resources.
        Completing it would unlock: Stealth
      
      ## Policies
      - Spaceflight Pioneers (Level 3 Tenet of Ideology Order): Spaceflight Pioneers: Gain a free Great Engineer and Great Scientist. May finish Spaceship parts with Great Engineers, and expending a Great Person grants 100 Science, scaling with Era. Hurrying Production with Great Engineers 50% more effective.
      - Socialist Realism (Level 3 Tenet of Ideology Order): Socialist Realism: Unlocks the Propaganda Process (converts 15% of Production into Tourism). +25% Tourism to other Civilizations following Order. +4 Production from all Great Works.
      - Iron Curtain (Level 3 Tenet of Ideology Order): Iron Curtain: Free Courthouse upon immediate City annexation. +200% Food or Production from Internal Trade Routes. City connections generate +5 Gold and Production.
      - Peace, Land, Bread (Level 1 Tenet of Ideology Order): Peace, Land, Bread: -2 Unhappiness from Poverty and Growth increased by 20% in all Cities. Building maintenance reduced by 20%.
      - Communism (Level 1 Tenet of Ideology Order): Communism: Gold cost of investing in buildings reduced by 25%. +20% Production when building Wonders.
      - People's Army (Level 1 Tenet of Ideology Order): People's Army: +100% Production towards Military Academies, and receive 5 Free Military Academies in your Empire. Public Schools produce +5 Culture and +2 Happiness.
      - Hero of the People (Level 1 Tenet of Ideology Order): Hero of the People: Great Person rate increases by 25%. A Great Person of your choice appears near your Capital.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Equality (Continuing Progress Branch):
        - * +1 Happiness in every City and +1 Happiness for every 15 Citizens in a City.
        - * -1 Unhappiness from and Distress, Poverty, Illiteracy, and Boredom in all Cities.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Organization (Continuing Progress Branch):
        - * +2 Production in every City.
        - * +25% Production toward Workers and Trade Units.
        - * +1 Movement for Workers.
      - Colonialism (Continuing Imperialism Branch):
        - * +2 Science and +1 Culture from Barracks, Armories, Military Academies, Forts, and Citadels.
        - * Each unique Global Monopoly modifier is increased by an additional 10% if it's percentage-based, or +3 otherwise.
      - Regimental System (Continuing Imperialism Branch):
        - * Earn Great Generals and Great Admirals 33% faster.
        - * Great Generals and Great Admirals gain the Regimental Traditions Promotion (+10% Leadership Combat Bonus and +1 Tile Radius).
        - * +2 additional copies of the unique Luxury Resources from expending Great Admirals for their Voyage of Discovery ability.
        - * Military Units can be upgraded in territory owned by Vassals and friendly City-States.
      - Civilizing Mission (Continuing Imperialism Branch):
        - * Retain all buildings from conquered Cities.
        - * Receive 75 Gold when you conquer a city, scaling with Era and City Population.
        - * +10% Production toward Buildings, with an additional +10% Production per Era difference between your current Era and the building's Era in all Puppeted Cities and Cities with a Courthouse.
      - Fraternity (Continuing Progress Branch):
        - * +3 Food in every City.
        - * +3 Science from City Connections.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Fealty (New Branch):
        - Fealty enhances your ability to defend and leverage your Majority Religion.
        - Adopting Fealty grants:
        - * Can purchase Monasteries with Faith (+3 Food, +3 Science, +2 Faith).
        - * -25% Faith costs for purchasing Buildings, Missionaries, and Inquisitors.
        - Each Fealty policy unlocked grants:
        - * +1 Faith and Strength in every City.
        - Adopting all Policies in Fealty grants:
        - * Unlocks building the Red Fort.
        - * Your Tourism modifier for Shared Religion is 50% stronger.
        - * Cities that follow your Majority Religion generate +3 Production, Gold, Science, and Culture.
        - * Allows for the purchase of Great Artists with Faith starting in the Industrial Era.
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
        - Rationale: Following the completion of Atomic Theory, Nuclear Fission is our absolute priority. It unlocks Bazookas, Atomic Bombs, and Nuclear Plants. This is vital to break heavily defended enemy capitals like Addis Ababa and Karakorum, allowing us to conquer Ethiopia (who is close to cultural victory) and achieve our own Domination victory.
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Iron Curtain (Level 3 Tenet of Ideology Order)
        - Rationale: Adopting Iron Curtain next provides a free Courthouse upon city annexation, which is extremely valuable as we conquer enemy lands. Additionally, it gives +200% Food/Production to internal trade routes and +5 Gold/Production to city connections, greatly boosting our empire's economy and industrial capacity to support the war effort.
    - #2:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Defense: 100
          - Growth: 70
          - CityDefense: 100
          - Production: 100
          - Spaceship: 50
          - Mobile: 100
          - Airlift: 90
          - Ranged: 100
          - MilitaryTraining: 100
          - Science: 100
          - GreatPeople: 75
          - Espionage: 100
          - Nuke: 100
          - Religion: 0
          - Happiness: 100
          - Diplomacy: 90
          - Infrastructure: 100
          - Wonder: 0
          - Air: 100
          - Recon: 50
          - NavalRecon: 80
          - WaterConnection: 50
          - Gold: 100
          - Expansion: 0
          - Offense: 100
          - TileImprovement: 60
          - UseNuke: 100
          - Culture: 50
          - Naval: 100
          - Antiair: 100
          - AirCarrier: 80
          - Mobilization: 100
        - GrandStrategy: Conquest
      - rationale: We increase Nuke and UseNuke to 100 to prepare our tactical AI to build the Manhattan Project and stockpile/use nuclear weapons immediately upon completion of Atomic Theory. Mobilization is raised to 100 to maximize military production. Diplomacy is set to 90 to ensure our city-state alliances remain secure as we vote to enact the United Nations in 3 turns, and to oppose Ethiopia's dangerous Passport System proposal.
  - tokens:
    - inputTokens: 78334
    - reasoningTokens: 6408
    - outputTokens: 435
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Multi-Front Conflict**
            
            My current focus is on strategically evaluating our multi-front war situation. I'm analyzing the immediate threats from Ethiopia, Songhai, and Mongolia, while also considering the potential implications of our passive hostility with Japan. This assessment is crucial for determining our next moves.
            
            **Prioritizing Next Research**
            
            I'm now prioritizing our next technology after Plastics. Atomic Theory is still underway, so I'm reviewing Refrigeration, Nuclear Fission, Penicillin, and Mobile Tactics to determine the most impactful choice.
            
            **Researching Nuclear Fission**
            
            My thoughts are now laser-focused on immediately pursuing Nuclear Fission for research. Given Atomic Theory is in progress, this unlocks critical advancements like Atomic Bombs and Bazookas, essential for overcoming fortified Ethiopian and Songhai cities. I'm also reviewing the implications of this choice on other unlocks.
            
            **Choosing Next Policy**
            
            My current thought process is centered on deciding our next Ideology policy. I'm weighing the merits of Iron Curtain against Spaceflight Pioneers, given we don't currently possess either. The choice hinges on immediate strategic advantage versus long-term technological gain, with our next adoption due in four turns.
            
            **Revising Ideology Strategy**
            
            My thinking has shifted significantly. Given our Domination Grand Strategy and controlling four capitals, I'm now prioritizing Socialist Realism. This choice better supports our immediate conquest goals over the longer-term benefits of Spaceflight Pioneers or the defensive nature of Iron Curtain, especially with Ethiopia nearing a cultural victory.
            
            **Conquering Imminent Victory**
            
            My immediate concern is that Ethiopia is on the verge of a Wonder victory. We must conquer them now, especially since we're already at war and besieging their capital. I'm also strategizing our approach against Songhai and Mongolia amidst our ongoing global conflict.
            
            **Prioritizing Ideology Policy**
            
            My thoughts are now focused on the immediate benefits of conquering. The production and happiness demands of our expanding empire are immense. I am re-evaluating whether the instantaneous happiness relief from Iron Curtain's free Courthouse upon annexation outweighs the long-term scientific and engineering boons of Spaceflight Pioneers. Socialist Realism is also in consideration for its immediate conquest support.
            
            **Adopting Ideology Policy**
            
            My current thinking is focused on the policy adoption. I'm reassessing Iron Curtain, recognizing its free Courthouse benefit will primarily aid future annexations rather than existing occupied cities. However, its substantial boost to internal trade routes from +200% Food or Production is now a significant consideration for my empire.
            
            **Choosing Iron Curtain Policy**
            
            I'm solidifying my decision to adopt Iron Curtain. The policy's immense boosts to city connections and internal trade routes will significantly bolster our production and gold generation, which is critical for sustaining our conquest-oriented, wide empire. This feels like the most impactful choice for our current situation.
            
            **Managing Diplomatic Ties**
            
            I'm currently reviewing our relationships with allied and neutral civs, ensuring they remain stable while our enemies are locked into perpetual conflict. This careful management of diplomatic ties allows for a more predictable AI behavior and prevents premature peace treaties that could jeopardize our conquest goals.
            
            **Prioritizing Nuclear Focus**
            
            My current thinking is to significantly boost our "Nuke" and "UseNuke" flavors. With Atomic Theory nearing completion in about seven turns, I want to ensure the AI immediately prioritizes building the Manhattan Project and then stockpiling atomic bombs to swiftly dismantle the high-defense Ethiopian capitals and break our ongoing stalemates.
            
            **Adjusting AI Priorities**
            
            I'm now focusing on adjusting AI priorities, specifically increasing "Nuke" and "UseNuke" flavors. With Atomic Theory nearly finished, I want the AI to rush the Manhattan Project and stockpile bombs to quickly overcome Ethiopia's high-defense cities and end our current stalemates.
            
            **Refining AI Focus**
            
            I'm assessing our AI's victory condition priorities, confirming Spaceship and Wonder competitiveness are appropriately set for our current Domination strategy. This ensures our focus remains squarely on military might and essential projects like the Manhattan Project, avoiding distractions.
            
            **Focusing on Congress**
            
            My current thoughts are centered on the upcoming United Nations vote. I am ensuring our persona's standing within the Congress remains unchanged and undisturbed by any recent developments or potential diplomatic shifts.
            
            **Opposing Unfavorable Proposals**
            
            I'm now focused on the upcoming UN vote. My priority is to oppose Ethiopia's Passport System, as it would accelerate their cultural victory. I am also evaluating Mongolia's Decolonization proposal, which could impact our city-state alliances. I'm confident we have enough votes to sway the outcome.
            
            **Adjusting Voting Leverage**
            
            My thinking is now focused on ensuring our AI's tactical voting aligns perfectly with our strategic goals. I'm confirming that aggressive diplomatic stances, specifically setting Ethiopia to an extremely hostile relationship, will strongly influence the AI to oppose their proposals, particularly the Passport System, thus securing our desired outcomes in the World Congress without direct intervention.
            
            **Setting Research Focus**
            
            My current thinking is about setting our next technology. With Atomic Theory nearing completion, I'm directing the research towards Nuclear Fission. This choice is critical for unlocking atomic bombs and bazookas, which are essential for overwhelming our heavily fortified opponents. I'm also considering the implications of this research path.
            
            **Researching Nuclear Fission**
            
            My current focus is on Atomic Theory's completion, after which Nuclear Fission will be my immediate research priority. This will unlock critical units and infrastructure to support our domination strategy and ensure continued military superiority.
            
            **Choosing Iron Curtain Policy**
            
            I am now focused on adopting the Iron Curtain policy. Its benefits for managing occupied unhappiness, boosting trade routes, and fueling my wide empire's economy and production are highly appealing for our current conquest-driven approach.
            
            **Boosting Offensive AI Capabilities**
            
            My thinking is now directed at bolstering the AI's offensive capabilities. By maximizing Offense, Defense, and Mobilization flavors, I aim to ensure our AI partners are aggressively pursuing victory through military might and efficient war-making, aligning perfectly with our grand strategy.
            
            **Adjusting AI Priorities**
            
            I'm now focusing on adjusting AI priorities, specifically increasing "Nuke" and "UseNuke" flavors. With Atomic Theory nearly finished, I want the AI to rush the Manhattan Project and stockpile bombs to quickly overcome Ethiopia's high-defense cities and end our current stalemates.
            
            **Adopting Iron Curtain Policy**
            
            I'm now fully committed to adopting Iron Curtain. The free Courthouse on annexation, combined with the massive boosts to internal trade routes for production and gold, are precisely what my wide, conquest-focused empire needs to sustain its momentum.
            
            **Adopting Iron Curtain Policy**
            
            I'm now fully committed to adopting Iron Curtain. The free Courthouse on annexation, combined with the massive boosts to internal trade routes for production and gold, are precisely what my wide, conquest-focused empire needs to sustain its momentum.
            
            **Adopting Iron Curtain Policy**
            
            I'm now fully committed to adopting Iron Curtain. The free Courthouse on annexation, combined with the massive boosts to internal trade routes for production and gold, are precisely what my wide, conquest-focused empire needs to sustain its momentum.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 0pKWLVitINIkhHUk
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: Following the completion of Atomic Theory, Nuclear Fission is our absolute priority. It unlocks Bazookas, Atomic Bombs, and Nuclear Plants. This is vital to break heavily defended enemy capitals like Addis Ababa and Karakorum, allowing us to conquer Ethiopia (who is close to cultural victory) and achieve our own Domination victory.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: xeynK7tfGRdQIPYd
          - toolName: set-policy
          - input:
            - Policy: Iron Curtain (Level 3 Tenet of Ideology Order)
            - Rationale: Adopting Iron Curtain next provides a free Courthouse upon city annexation, which is extremely valuable as we conquer enemy lands. Additionally, it gives +200% Food/Production to internal trade routes and +5 Gold/Production to city connections, greatly boosting our empire's economy and industrial capacity to support the war effort.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: h0VlSP9vOffyjesh
          - toolName: set-flavors
          - input:
            - Flavors:
              - Defense: 100
              - Growth: 70
              - CityDefense: 100
              - Production: 100
              - Spaceship: 50
              - Mobile: 100
              - Airlift: 90
              - Ranged: 100
              - MilitaryTraining: 100
              - Science: 100
              - GreatPeople: 75
              - Espionage: 100
              - Nuke: 100
              - Religion: 0
              - Happiness: 100
              - Diplomacy: 90
              - Infrastructure: 100
              - Wonder: 0
              - Air: 100
              - Recon: 50
              - NavalRecon: 80
              - WaterConnection: 50
              - Gold: 100
              - Expansion: 0
              - Offense: 100
              - TileImprovement: 60
              - UseNuke: 100
              - Culture: 50
              - Naval: 100
              - Antiair: 100
              - AirCarrier: 80
              - Mobilization: 100
            - GrandStrategy: Conquest
            - Rationale: We increase Nuke and UseNuke to 100 to prepare our tactical AI to build the Manhattan Project and stockpile/use nuclear weapons immediately upon completion of Atomic Theory. Mobilization is raised to 100 to maximize military production. Diplomacy is set to 90 to ensure our city-state alliances remain secure as we vote to enact the United Nations in 3 turns, and to oppose Ethiopia's dangerous Passport System proposal.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 0pKWLVitINIkhHUk
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
          - toolCallId: xeynK7tfGRdQIPYd
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: h0VlSP9vOffyjesh
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.