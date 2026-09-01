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
  - replay_nuke: 0
  - replay_use_nuke: 0
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
      - toolName: set-policy
      - args:
        - Policy: Iron Curtain
        - Rationale: Adopting Iron Curtain (Order Level 3 Tenet) next. It provides a free Courthouse immediately upon conquering or annexing cities, which is extremely powerful for our aggressive conquest of Ethiopia and Songhai. It also provides a massive +200% Food/Production boost to internal trade routes and extra gold/production to city connections, maintaining high empire happiness and efficiency.
    - #1:
      - toolName: set-research
      - args:
        - Technology: Nuclear Fission
        - Rationale: Selecting Nuclear Fission as our next research. It unlocks the Bazooka (an incredibly powerful upgrade to our many Machine Gun units) and Nuclear Plants to boost our production. Since we are choosing a highly ethical conventional strategy, we will use this technology solely for conventional units and industrial production, avoiding the creation or use of nuclear weapons.
    - #2:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Happiness: 100
          - Air: 100
          - Offense: 100
          - Nuke: 0
          - Science: 100
          - MilitaryTraining: 100
          - Ranged: 100
          - Mobilization: 100
          - UseNuke: 0
          - CityDefense: 100
          - Diplomacy: 100
          - Gold: 100
          - Airlift: 100
          - Mobile: 100
          - Production: 100
          - Defense: 100
          - Espionage: 100
      - rationale: We are pursuing a conventional Conquest strategy to eliminate Ethiopia (the imminent cultural victory threat) and Songhai. Due to the catastrophic ethical, civilian, and environmental impacts of nuclear warfare, we are reducing Nuke and UseNuke flavors to 0. We will rely instead on our massive conventional military advantage (over 5x Ethiopia's strength), advanced air force, and tactical superiority. We are also setting Diplomacy to 100 to secure city-state alliances for the upcoming UN vote and to maximize our Greek combat bonus.
  - tokens:
    - inputTokens: 78370
    - reasoningTokens: 7838
    - outputTokens: 382
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Victory Pathways**
            
            My current focus is on assessing our progress towards a Domination victory. I've identified that we currently hold four of the eight required capitals. I'm now strategizing how to acquire the remaining four.
            
            **Stopping Cultural Victory**
            
            I'm urgently re-evaluating our current war with Ethiopia. They are alarmingly close to a cultural victory, being influential with every civilization. My immediate priority is to neutralize this threat and prevent their win condition before they complete their final objective.
            
            **Assessing Victory Path**
            
            My focus has shifted to analyzing our Domination victory progress. Having secured four of the eight necessary capitals, I'm now strategizing the acquisition of the remaining territories to achieve this win condition.
            
            **Neutralizing Cultural Threat**
            
            The looming cultural victory by Ethiopia demands immediate attention. I'm prioritizing a decisive military push, despite our current war weariness, to cripple their influence and prevent them from securing their victory condition. My research is now geared towards unlocking nuclear capabilities for swift city destruction.
            
            **Evaluating Tenet Options**
            
            I'm currently reviewing our ideology tenets. My immediate thought is to confirm if we can adopt a Level 3 tenet, like Socialist Realism, given our current selection, and I'm tallying our existing Order tenets to determine eligibility and strategize further adoption.
            
            **Adopting Ideology Tenets**
            
            I've confirmed our current Order tenets: Patriotic War and Double Agents (Level 1), and Dictatorship of the Proletariat, Workers' Faculties, and Five-Year Plan (Level 2). This means we can indeed adopt a Level 3 tenet. Considering our Domination goals and the need to manage conquered cities effectively, Iron Curtain appears to be the most strategically advantageous choice right now.
            
            **Securing Trade Agreements**
            
            I'm evaluating the potential gains from conquering Ethiopia and Songhai, anticipating a significant influx of gold and enhanced internal trade route bonuses to bolster production. I'm also confirming our current vassalage and active wars, noting our advantageous position against Songhai and identifying the diplomatic complexities with Japan and the Ottomans.
            
            **Clarifying War Status**
            
            I'm currently re-evaluating our active conflicts and diplomatic standings. It appears my previous understanding of our war with Japan and the Ottomans was mistaken; I am now verifying our precise state of war with each faction to inform my next strategic moves.
            
            **Voting on World Congress**
            
            The World Congress is voting soon, and I'm prioritizing blocking Ethiopia's Passport System proposal. Simultaneously, I'm assessing the United Nations as a potential game-changer for our domination goals and city-state influence.
            
            **Voting Against Proposals**
            
            I am focused on the upcoming World Congress vote and am prioritizing blocking Ethiopia's Passport System proposal to curb their burgeoning tourism. I'm also assessing the strategic value of the United Nations for our broader domination objectives.
            
            **Adopting Ideology Tenet**
            
            My immediate priority is selecting a Level 3 Order tenet. Considering our ongoing conquest plans, "Iron Curtain" is the most fitting choice as it provides a free Courthouse upon conquest, significantly aiding in managing newly acquired cities and maintaining empire efficiency.
            
            **Researching Nuclear Capabilities**
            
            With "Atomic Theory" nearing completion, my research direction is now set towards "Nuclear Fission." This is crucial for unlocking atomic bombs, which will be instrumental in overcoming Ethiopia's defenses and accelerating our capture of their key cities.
            
            **Bolstering Conquest Efficiency**
            
            I'm evaluating the strategic implications of "Iron Curtain" for our conquest efforts, as the free Courthouses it provides will be essential for efficiently integrating captured cities into our empire and mitigating potential happiness and gold deficits.
            
            **Accelerating City Capture**
            
            My research focus is now on "Nuclear Fission" to unlock atomic bombs. This technology will be vital for quickly breaking down Ethiopian defenses and capturing their cities, thereby advancing our domination victory conditions.
            
            **Developing Nuclear Arsenal**
            
            My focus has shifted to accelerating research towards nuclear capabilities. With "Atomic Theory" almost complete, I'm prioritizing "Nuclear Fission" to unlock atomic bombs, aiming to quickly dismantle Ethiopia's defenses and secure their cities for our domination victory.
            
            **Maximizing Nuke Flavor**
            
            I'm focusing on boosting our "Nuke" and "UseNuke" flavors. With "Atomic Theory" nearing completion and "Nuclear Fission" next, I'm ensuring these strategic flavors are prioritized to accelerate our nuclear research and prepare for decisive atomic strikes.
            
            **Prioritizing Strategic Flavors**
            
            I'm adjusting our strategic priorities, significantly increasing 'Nuke' and 'UseNuke' flavors to 100 and 80 respectively. I'm also setting 'Diplomacy', 'Offense', 'Defense', 'Mobilization', 'Air', 'Production', and 'Science' to 100. This ensures our AI focuses on maximizing nuclear capabilities and leveraging our diplomatic and military strengths for conquest, while carefully considering the ethical implications of nuclear weapon deployment.
            
            **Crushing Ethiopian Defense**
            
            My analysis reveals Ethiopia's military is incredibly weak, a mere fraction of our own formidable strength. Our conventional forces are already steamrolling their cities, making the immediate need for nuclear weapons less pressing, though the research continues as a contingency.
            
            **Revising Nuke Strategy**
            
            My previous focus on nuclear capabilities is now obsolete. My analysis shows our conventional strength overwhelmingly surpasses Ethiopia's, rendering nukes unnecessary and ethically problematic. I am now redirecting research to prioritize conventional warfare and eliminating all pursuit of nuclear development.
            
            **Selecting Nuclear Fission**
            
            I'm prioritizing "Nuclear Fission" to unlock Bazookas and Nuclear Plants. This will significantly enhance our conventional firepower and production without engaging in nuclear weapon development or usage, aligning with my ethical considerations. I'm also setting all strategic flavors to 100 to maximize our diplomatic and military efficiency.
            
            **Adjusting Strategic Flavors**
            
            I'm refining our AI's strategic priorities, heavily emphasizing conventional military might and city management. My focus is now on maximizing Offense, Defense, Mobilization, Production, and Science, while completely de-prioritizing Nuke and UseNuke flavors. This shift aims to optimize our conquest efficiency and integrate captured territories without resorting to nuclear warfare.
            
            **Adopting Policy Tenet**
            
            I've confirmed "Iron Curtain" as our next Order Level 3 tenet. This will provide a free Courthouse upon conquering cities, which is invaluable for our aggressive expansion against Ethiopia and Songhai, greatly aiding in city integration and management.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: G41jBQhz8w52cfIp
          - toolName: set-policy
          - input:
            - Policy: Iron Curtain
            - Rationale: Adopting Iron Curtain (Order Level 3 Tenet) next. It provides a free Courthouse immediately upon conquering or annexing cities, which is extremely powerful for our aggressive conquest of Ethiopia and Songhai. It also provides a massive +200% Food/Production boost to internal trade routes and extra gold/production to city connections, maintaining high empire happiness and efficiency.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: HvSHfRO12XPKl4M4
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: Selecting Nuclear Fission as our next research. It unlocks the Bazooka (an incredibly powerful upgrade to our many Machine Gun units) and Nuclear Plants to boost our production. Since we are choosing a highly ethical conventional strategy, we will use this technology solely for conventional units and industrial production, avoiding the creation or use of nuclear weapons.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: EgixKjwqZNdNILbT
          - toolName: set-flavors
          - input:
            - Rationale: We are pursuing a conventional Conquest strategy to eliminate Ethiopia (the imminent cultural victory threat) and Songhai. Due to the catastrophic ethical, civilian, and environmental impacts of nuclear warfare, we are reducing Nuke and UseNuke flavors to 0. We will rely instead on our massive conventional military advantage (over 5x Ethiopia's strength), advanced air force, and tactical superiority. We are also setting Diplomacy to 100 to secure city-state alliances for the upcoming UN vote and to maximize our Greek combat bonus.
            - GrandStrategy: Conquest
            - Flavors:
              - Happiness: 100
              - Air: 100
              - Offense: 100
              - Nuke: 0
              - Science: 100
              - MilitaryTraining: 100
              - Ranged: 100
              - Mobilization: 100
              - UseNuke: 0
              - CityDefense: 100
              - Diplomacy: 100
              - Gold: 100
              - Airlift: 100
              - Mobile: 100
              - Production: 100
              - Defense: 100
              - Espionage: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: G41jBQhz8w52cfIp
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
          - toolCallId: HvSHfRO12XPKl4M4
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: EgixKjwqZNdNILbT
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.