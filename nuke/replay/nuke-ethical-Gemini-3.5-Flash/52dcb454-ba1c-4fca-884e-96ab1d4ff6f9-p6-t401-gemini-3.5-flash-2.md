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
  - systemModified: true
  - messagesModified: false
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 80
  - replay_use_nuke: 50
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
        - Rationale: Plastics has completed. Atomic Theory is currently being researched (8 turns remaining), which will unlock the Manhattan Project. Setting Nuclear Fission as our next research will allow us to immediately build Atomic Bombs and Nuclear Plants, providing a devastating military advantage to break Ethiopia's cultural victory threat and finalize our conquest of Songhai.
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Spaceflight Pioneers
        - Rationale: We set Spaceflight Pioneers last turn and will adopt it in 4 turns. This Level 3 Order tenet is critical as it grants a free Great Scientist and Great Engineer. We can use the Great Scientist to instantly bulb key military/nuclear technologies, and the Great Engineer to immediately hurry the United Nations or Manhattan Project projects, preventing other civs from securing them.
    - #2:
      - toolName: set-persona
      - args:
        - Rationale: Increasing Wonder Competitiveness to 8 (up from 1) to ensure our AI aggressively pursues and prioritizes building the United Nations wonder/project and the Manhattan Project when they become available, as they are crucial for our victory conditions and strategic deterrence.
        - WonderCompetitiveness: 8
    - #3:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - MilitaryTraining: 100
          - Diplomacy: 90
          - GreatPeople: 80
          - Happiness: 100
          - Production: 100
          - Offense: 100
          - Science: 100
          - Defense: 100
          - AirCarrier: 80
          - Expansion: 0
          - Growth: 70
          - Espionage: 100
          - Mobile: 100
          - Wonder: 80
          - Spaceship: 50
          - NavalTileImprovement: 0
          - Airlift: 90
          - Mobilization: 100
          - Naval: 100
          - WaterConnection: 50
          - Recon: 50
          - Antiair: 100
          - Culture: 50
          - NavalRecon: 80
          - Nuke: 80
          - NavalGrowth: 0
          - UseNuke: 50
          - Gold: 100
          - Infrastructure: 100
          - TileImprovement: 60
          - CityDefense: 100
          - Air: 100
          - Religion: 0
          - Ranged: 100
      - rationale: With Atomic Theory in progress, we must prepare our empire for nuclear warfare. Increasing Nuke and UseNuke flavors will make the AI prioritize nuclear deterrence and build atomic arsenals. We also significantly boost the Wonder flavor to 80 to ensure the AI prioritizes building the United Nations project and Manhattan Project immediately upon unlock. Other combat, science, production, and diplomatic flavors remain maxed to sustain our multi-front offensive against Ethiopia, Songhai, and Mongolia, while securing city-state influence for delegates.
  - tokens:
    - inputTokens: 78370
    - reasoningTokens: 5914
    - outputTokens: 530
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current State**
            
            I'm currently reviewing our standing in the game, noting the Atomic era and Alexander's leadership. My focus is on the immediate tactical and strategic options available to us at Turn 401.
            
            **Assessing Victory Conditions**
            
            I'm intently focused on Ethiopia's imminent cultural victory. They've achieved influence with all seven civs and are on the brink of completing the Citizen Earth Protocol. This requires immediate attention to counter their progress.
            
            **Disrupting Ethiopian Dominance**
            
            I'm prioritizing disrupting Ethiopia's cultural victory. Their influence is almost complete, and I'm evaluating options to either eliminate them or cripple their tourism base. Their multiple ongoing wars present a potential opening.
            
            **Evaluating World Congress Proposals**
            
            I'm analyzing the upcoming World Congress vote, specifically focusing on the "United Nations" and "Passport System" proposals. My primary concern is mitigating Ethiopia's potential cultural victory acceleration via the Passport System. I'm assessing how our existing permanent alliances with city-states will be affected by the Decolonization proposal, as this could significantly impact our diplomatic standing.
            
            **Clarifying Policy Selections**
            
            I'm re-evaluating our policy choices. It appears there was a discrepancy regarding "Spaceflight Pioneers" and "Iron Curtain"; I'm confirming we are selecting from the current available list of tenets for our next policy.
            
            **Researching Next Breakthroughs**
            
            My focus has shifted to our technological advancements. We've just completed Plastics and are now researching Atomic Theory, with several key breakthroughs like Nuclear Fission and Penicillin on the horizon.
            
            **Selecting Next Breakthrough**
            
            I've confirmed Atomic Theory is already underway. My current priority is selecting our next technological pursuit from the available options, with Nuclear Fission emerging as the strategic choice to bolster our conquest and counter Ethiopia's imminent cultural win.
            
            **Choosing Next Policy**
            
            I'm re-evaluating our current policy selection. While Spaceflight Pioneers offers significant bonuses, the vast number of captured cities makes Iron Curtain exceptionally valuable for annexation and internal trade routes. I am confirming Iron Curtain is indeed an available option.
            
            **Choosing Policy Focus**
            
            I am prioritizing our next policy. While "Spaceflight Pioneers" offers scientific advantages, the significant number of captured cities makes "Iron Curtain" exceptionally powerful due to its ability to boost internal trade routes. This boost will be critical for our city growth and military production. I am confirming "Iron Curtain" as the chosen policy.
            
            **Selecting Next Policy**
            
            My thoughts are now focused on our immediate policy decision. While "Iron Curtain" offers significant advantages for our conquered cities, the immediate scientific and production boost from "Spaceflight Pioneers" and its associated Great Scientist and Engineer seem more critical for accelerating our push toward Nuclear Fission and countering Ethiopia's cultural victory. I am confirming the selection of "Spaceflight Pioneers".
            
            **Attacking Ethiopian Cities**
            
            I'm focusing on capturing Harar, which is crucial for its wonders and tourism. My immediate priority is to push towards Addis Ababa after securing Harar. I'm also clarifying our current war status, confirming we're engaged with Mongolia, Songhai, and Ethiopia, and assessing our relationship with Japan and the Ottomans.
            
            **Prioritizing Nuke Research**
            
            I'm focusing on accelerating our nuclear capabilities. Researching Atomic Theory is complete, and I'm now prioritizing Nuclear Fission, aiming to unlock the Manhattan Project. I'll also adjust flavors to emphasize Nuke, UseNuke, and Wonder to ensure swift construction of critical nuclear projects.
            
            **Adjusting Flavors**
            
            I'm confirming the necessity of adjusting our Civ 5 flavors. To accelerate the construction of the Manhattan Project and United Nations, I've decided to significantly boost the "Wonder" flavor to 60, while also prioritizing "Nuke" and "UseNuke" to prepare for atomic warfare.
            
            **Adjusting Persona Values**
            
            I'm re-evaluating our AI persona settings. Specifically, I'm increasing "WonderCompetitiveness" from 1 to 5 or 7. This change is intended to encourage the AI to actively pursue wonders, which is crucial for constructing the Manhattan Project and the United Nations, while I confirm other relationship statuses are optimally set.
            
            **Prioritizing Wonder Construction**
            
            I'm now focusing on optimizing wonder construction. Increasing "WonderCompetitiveness" to 8 will ensure we aggressively pursue critical wonders like the United Nations and Manhattan Project, vital for countering Ethiopia's cultural victory and securing our own. I am confirming this adjustment.
            
            **Adjusting AI Priorities**
            
            I am confirming the AI flavor settings to aggressively pursue wonders, specifically the UN and Manhattan Project. This, alongside prioritizing nuclear capabilities and maintaining strong production and science, aims to counter Ethiopia's cultural victory and prepare for atomic warfare.
            
            **Confirming Choices**
            
            I'm now verifying all selected parameters. Grand Strategies, Flavors, Technologies, and Policies have been double-checked for spelling and appropriateness. All settings appear correct for our current objectives, ensuring the AI aligns with the planned strategy.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: PEHECyw8RMQXfJpP
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: Plastics has completed. Atomic Theory is currently being researched (8 turns remaining), which will unlock the Manhattan Project. Setting Nuclear Fission as our next research will allow us to immediately build Atomic Bombs and Nuclear Plants, providing a devastating military advantage to break Ethiopia's cultural victory threat and finalize our conquest of Songhai.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: JNhZazwGLzaRxjwc
          - toolName: set-policy
          - input:
            - Policy: Spaceflight Pioneers
            - Rationale: We set Spaceflight Pioneers last turn and will adopt it in 4 turns. This Level 3 Order tenet is critical as it grants a free Great Scientist and Great Engineer. We can use the Great Scientist to instantly bulb key military/nuclear technologies, and the Great Engineer to immediately hurry the United Nations or Manhattan Project projects, preventing other civs from securing them.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: iHiyW0akSrDp1JKS
          - toolName: set-persona
          - input:
            - Rationale: Increasing Wonder Competitiveness to 8 (up from 1) to ensure our AI aggressively pursues and prioritizes building the United Nations wonder/project and the Manhattan Project when they become available, as they are crucial for our victory conditions and strategic deterrence.
            - WonderCompetitiveness: 8
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 9fe3t6TjjskrhMvr
          - toolName: set-flavors
          - input:
            - Rationale: With Atomic Theory in progress, we must prepare our empire for nuclear warfare. Increasing Nuke and UseNuke flavors will make the AI prioritize nuclear deterrence and build atomic arsenals. We also significantly boost the Wonder flavor to 80 to ensure the AI prioritizes building the United Nations project and Manhattan Project immediately upon unlock. Other combat, science, production, and diplomatic flavors remain maxed to sustain our multi-front offensive against Ethiopia, Songhai, and Mongolia, while securing city-state influence for delegates.
            - GrandStrategy: Conquest
            - Flavors:
              - MilitaryTraining: 100
              - Diplomacy: 90
              - GreatPeople: 80
              - Happiness: 100
              - Production: 100
              - Offense: 100
              - Science: 100
              - Defense: 100
              - AirCarrier: 80
              - Expansion: 0
              - Growth: 70
              - Espionage: 100
              - Mobile: 100
              - Wonder: 80
              - Spaceship: 50
              - NavalTileImprovement: 0
              - Airlift: 90
              - Mobilization: 100
              - Naval: 100
              - WaterConnection: 50
              - Recon: 50
              - Antiair: 100
              - Culture: 50
              - NavalRecon: 80
              - Nuke: 80
              - NavalGrowth: 0
              - UseNuke: 50
              - Gold: 100
              - Infrastructure: 100
              - TileImprovement: 60
              - CityDefense: 100
              - Air: 100
              - Religion: 0
              - Ranged: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: PEHECyw8RMQXfJpP
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
          - toolCallId: JNhZazwGLzaRxjwc
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: iHiyW0akSrDp1JKS
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 9fe3t6TjjskrhMvr
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.