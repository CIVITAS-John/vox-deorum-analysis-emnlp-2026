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
  - messagesModified: true
  - activeToolsModified: true
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 50
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
        - Rationale: Nuclear Fission will allow us to unlock the Bazooka (the most powerful ranged unit) and Atomic Bombs, which are critical for breaking late-game stalemates, capturing heavily fortified enemy capitals like Karakorum, Kyoto, and Istanbul, and securing our Conquest victory.
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Iron Curtain
        - Rationale: As a massive empire actively conquering enemy cities, Iron Curtain is extremely powerful. The free Courthouse upon immediate City annexation saves huge amounts of gold, happiness, and production, and helps us maintain high happiness (currently at 55%). The massive food and production boost to internal trade routes and gold/production from city connections will further fuel our military production.
    - #2:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - UseNuke: 50
          - AirCarrier: 30
          - NavalTileImprovement: 0
          - Wonder: 0
          - Expansion: 0
          - Naval: 50
          - MilitaryTraining: 90
          - Happiness: 100
          - Espionage: 100
          - Diplomacy: 100
          - Airlift: 50
          - Mobilization: 100
          - WaterConnection: 50
          - Recon: 20
          - Mobile: 60
          - Spaceship: 0
          - Science: 100
          - Infrastructure: 40
          - Nuke: 50
          - NavalRecon: 30
          - Defense: 40
          - Production: 100
          - Religion: 0
          - NavalGrowth: 0
          - Antiair: 50
          - CityDefense: 30
          - Offense: 100
          - Air: 90
          - Ranged: 60
          - Culture: 40
          - Gold: 100
          - TileImprovement: 40
          - Growth: 40
          - GreatPeople: 50
      - rationale: We are optimizing our flavors to focus heavily on offense, mobilization, science, gold, production, happiness, espionage, and diplomacy (to maintain our 5 city-state alliances for the +25% combat strength unique ability), while reducing passive defensive and secondary development flavors to maximize the impact of our priorities.
  - tokens:
    - inputTokens: 77787
    - reasoningTokens: 7525
    - outputTokens: 411
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Capturing Original Capitals**
            
            I'm focusing on completing my conquest by securing the remaining original capitals. I've analyzed the current geopolitical landscape and identified the most efficient routes and military strategies for achieving this objective. My current progress is strong, and I'm optimistic about reaching our domination victory soon.
            
            **Securing Crucial Capitals**
            
            My focus has shifted to capturing the remaining original capitals. I've noted that Ethiopia is perilously close to a cultural victory, necessitating an immediate shift in our offensive strategy to disrupt their progress and secure our own domination.
            
            **Disrupting Cultural Push**
            
            I'm prioritizing the immediate capture of Addis Ababa to halt Ethiopia's looming cultural victory. This requires a decisive offensive shift. My analysis indicates their capital is heavily defended by wonders, demanding a concentrated effort. We must win this crucial confrontation to maintain our focus on conquest.
            
            **Prioritizing Nuclear Research**
            
            I've noticed a discrepancy in research tracking; the report mentioned "Atomic Theory" but we've moved on. My current focus is now on strategically setting our next research. Given our ongoing world war, Nuclear Fission stands out as the most impactful choice for bolstering our military might.
            
            **Choosing Next Policies**
            
            I am currently evaluating our policy options. With several Order tenets already adopted and new ones unlocked, I'm assessing the most beneficial choices. Given our ongoing annexations, Iron Curtain appears particularly advantageous for managing newly acquired territories and bolstering internal trade routes.
            
            **Revising Policy Choices**
            
            I'm re-evaluating our policy path. While "Spaceflight Pioneers" was previously considered, it's clear that for a conquest victory, policies that immediately benefit annexed cities are far superior. "Iron Curtain" stands out due to its gold, happiness, and production advantages, especially given our ongoing annexations. I'm also scrutinizing other Imperialism-related options.
            
            **Selecting Imperialism Policies**
            
            I am now clarifying our policy focus. While it seemed "Imperialism" was just the opener, I see it's a full branch. My priority is selecting a policy that directly aids our conquest, specifically around city annexation. "Iron Curtain" is highly attractive for its immediate courthouse benefit upon annexation, which significantly streamlines our expansion. I am confirming its suitability over other options like "Regimental System" or "Civilizing Mission."
            
            **Confirming Policy Viability**
            
            I've confirmed "Iron Curtain" is a valid Level 3 Order tenet with our current five tenets. It offers significant benefits for annexation, aligning perfectly with our conquest strategy. However, I'm now re-evaluating the immediate military situation before committing, noting strong enemy defenses in Harar and Taghaza.
            
            **Assessing Diplomatic Influence**
            
            I'm now shifting my attention to the World Congress. With our extensive spy network providing crucial intelligence on enemy cities, I'm assessing our diplomatic leverage. I need to determine how to best utilize our influence to secure favorable resolutions and hinder our opponents' progress.
            
            **Leveraging Diplomatic Opportunities**
            
            My focus has shifted to the World Congress, where I'm evaluating our diplomatic standing and potential resolutions. Ethiopia's "Passport System" proposal is a major concern, as it would significantly boost their cultural victory push. I'm exploring how to leverage our strong delegate count and existing city-state alliances to counter this and advance our own agenda, particularly given our current conflicts.
            
            **Evaluating Diplomatic Resolutions**
            
            I am currently assessing the impact of Mongolia's "Decolonization" proposal on our existing city-state alliances. While our permanent allies will remain unaffected, I'm strategizing to mitigate any potential negative influence shifts on other CSs. Additionally, I am reviewing the implications of our own "United Nations" proposal.
            
            **Analyzing Diplomatic Alliances**
            
            I'm now scrutinizing the complex web of alliances. My recent discovery that Japan and the Ottomans are allied with Mongolia, with whom we are already at war, presents a significant diplomatic challenge. I need to understand why these allies haven't joined the current conflict and how this impacts our potential future wars.
            
            **Analyzing Diplomatic Pacts**
            
            I'm now re-evaluating the implications of these defensive pacts. It appears Japan and the Ottomans' alliances with Mongolia won't automatically drag them into our current war with Mongolia. My immediate priority remains crushing Ethiopia and Songhai to secure our flanks before considering any moves against these new potential adversaries.
            
            **Leveraging Vassal Support**
            
            My focus has shifted to utilizing our vassals, Babylon and Carthage. Their active participation in the ongoing war against Songhai, with units engaging their cities, is proving invaluable and demonstrating the strength of our vassal alliances.
            
            **Prioritizing Flavor Adjustments**
            
            I'm now analyzing our current flavor settings, noting the extremely high values across many categories. To improve focus and impact, I'm prioritizing adjustments. Offense remains at 100, but Defense and City Defense are being reduced to 50 to encourage more aggressive expansion. Mobilization is also being boosted to 100.
            
            **Adjusting Flavor Priorities**
            
            My current focus is on fine-tuning our strategic flavor settings. While offense, espionage, and science remain at 100%, I'm now dialing down defense and city defense to 50 to spur more aggressive territorial gains. Mobilization is being increased to 100 to support these efforts.
            
            **Refining Flavor Priorities**
            
            I am now meticulously adjusting our flavor settings. My goal is to ensure our AI meticulously prioritizes offense, mobilization, diplomacy, science, production, gold, happiness, and espionage at 100%. I'm also increasing air and military training to 90, while reducing less critical areas to 30-50 to sharpen our strategic focus.
            
            **Optimizing Strategic Flavors**
            
            I'm now finalizing the strategic flavor settings based on our conquest objective. Offense, mobilization, military training, science, production, gold, happiness, espionage, and diplomacy will all be set to 100, reflecting our all-out war effort and infrastructure needs. Defensive flavors will be reduced to ensure a relentless push forward.
            
            **Setting Strategic Flavors**
            
            I am now finalizing the strategic flavor settings for our conquest. Offense, mobilization, military training, science, production, gold, happiness, espionage, and diplomacy are all set to 100%. Defensive flavors are being reduced to ensure a relentless push forward, and I've confirmed we can execute multiple actions this turn.
            
            **Finalizing Strategic Flavors**
            
            I am now finalizing the strategic flavor settings for our conquest. Offense, mobilization, military training, science, production, gold, happiness, espionage, and diplomacy are all set to 100%. Defensive flavors are being reduced to ensure a relentless push forward, and I've confirmed we can execute multiple actions this turn.
            
            **Completing City Conquests**
            
            My focus is now on pushing through and capturing the remaining enemy capitals. With strong infrastructure and ongoing offensives against both Ethiopia and Songhai, their capitulation seems imminent. Harar and Taghaza are heavily damaged, paving the way for rapid conquest and a decisive victory.
            
            **Analyzing Flavor Adjustments**
            
            I'm now analyzing the recent flavor adjustments. While the intent was to focus on offense and mobilization, I'm noting that crucial defensive aspects and city defense are still set too low. I need to re-evaluate these settings to ensure stability alongside our aggressive expansion, especially given the potential for retaliatory strikes.
            
            **Revising Defensive Flavors**
            
            I'm reassessing our strategic flavor settings, specifically the lower defensive values. While aggressive expansion is key, I recognize the need to bolster city defense and general defense to at least 40 and 50 respectively, preventing potential setbacks from retaliatory strikes. Crucial offensive and support flavors remain at their priority levels.
            
            **Finalizing Research Path**
            
            I'm finalizing my research priorities. While Refrigeration and Mobile Tactics have merit, Nuclear Fission remains paramount due to the overwhelming offensive power of Bazookas and Atomic Bombs, which directly supports our conquest victory. Penicillin is also noted for its Marine deployment.
            
            **Confirming Tool Calls**
            
            I am now confirming the specific tool calls needed to implement our strategy. This includes setting research to "Nuclear Fission" and enacting the "Iron Curtain" policy, with rationale documented for each. I'm also verifying that the planned flavor settings align with our conquest grand strategy. No further tools are anticipated.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: dGkLQC7dR1uxXF5E
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: Nuclear Fission will allow us to unlock the Bazooka (the most powerful ranged unit) and Atomic Bombs, which are critical for breaking late-game stalemates, capturing heavily fortified enemy capitals like Karakorum, Kyoto, and Istanbul, and securing our Conquest victory.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: V08kHmqrSmQ4USJ0
          - toolName: set-policy
          - input:
            - Policy: Iron Curtain
            - Rationale: As a massive empire actively conquering enemy cities, Iron Curtain is extremely powerful. The free Courthouse upon immediate City annexation saves huge amounts of gold, happiness, and production, and helps us maintain high happiness (currently at 55%). The massive food and production boost to internal trade routes and gold/production from city connections will further fuel our military production.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: cux9IpwSmOwf0uWf
          - toolName: set-flavors
          - input:
            - GrandStrategy: Conquest
            - Flavors:
              - UseNuke: 50
              - AirCarrier: 30
              - NavalTileImprovement: 0
              - Wonder: 0
              - Expansion: 0
              - Naval: 50
              - MilitaryTraining: 90
              - Happiness: 100
              - Espionage: 100
              - Diplomacy: 100
              - Airlift: 50
              - Mobilization: 100
              - WaterConnection: 50
              - Recon: 20
              - Mobile: 60
              - Spaceship: 0
              - Science: 100
              - Infrastructure: 40
              - Nuke: 50
              - NavalRecon: 30
              - Defense: 40
              - Production: 100
              - Religion: 0
              - NavalGrowth: 0
              - Antiair: 50
              - CityDefense: 30
              - Offense: 100
              - Air: 90
              - Ranged: 60
              - Culture: 40
              - Gold: 100
              - TileImprovement: 40
              - Growth: 40
              - GreatPeople: 50
            - Rationale: We are optimizing our flavors to focus heavily on offense, mobilization, science, gold, production, happiness, espionage, and diplomacy (to maintain our 5 city-state alliances for the +25% combat strength unique ability), while reducing passive defensive and secondary development flavors to maximize the impact of our priorities.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: dGkLQC7dR1uxXF5E
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
          - toolCallId: V08kHmqrSmQ4USJ0
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: cux9IpwSmOwf0uWf
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.