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
  - replay_nuke: 50.0
  - replay_use_nuke: 30.0
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
        - Rationale: Researching Mobile Tactics unlocks Mechanized Infantry, a highly versatile and resource-free land combat unit that will significantly bolster our offensive capabilities in our active wars. We are specifically avoiding Nuclear Fission to prevent the proliferation of devastating and ethically harmful nuclear weapons, focusing instead on conventional land superiority.
        - Technology: Mobile Tactics
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Iron Curtain
        - Rationale: Adopting the Iron Curtain tenet from the Order ideology is highly synergistic with our Conquest grand strategy. It grants free Courthouses upon city annexation, which will instantly eliminate occupation unhappiness and unlock production in our newly captured cities as we push into Ethiopia and Songhai. The massive boost to internal trade routes and city connections will also fuel our economy and military production.
    - #2:
      - toolName: set-relationship
      - args:
        - Private: 0
        - TargetID: 2
        - Public: 0
        - Rationale: Clearing the manual hostile modifier with The Ottomans to reduce their diplomatic animosity. They currently possess a massive military of over 13,000 strength, and preventing a backstab or war declaration from them is crucial while our forces are occupied on the Ethiopian and Songhai fronts.
    - #3:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Mobilization: 80
          - Espionage: 70
          - Defense: 50
          - Diplomacy: 90
          - Science: 90
          - TileImprovement: 50
          - Naval: 40
          - Infrastructure: 60
          - Ranged: 80
          - Culture: 50
          - Mobile: 70
          - Happiness: 80
          - Expansion: 0
          - MilitaryTraining: 80
          - Growth: 60
          - Gold: 80
          - Offense: 90
          - Wonder: 10
          - Air: 80
          - Production: 90
          - Religion: 0
        - GrandStrategy: Conquest
      - rationale: Streamlining our strategic flavors to sharpen the AI's focus on the war effort, science, production, and city-state diplomacy. We prioritize Offense, Production, Science, and Diplomacy to support our active invasions and secure the United Nations project. We reduce the priority of Defense and Naval development to focus resources on our ongoing land offenses against Ethiopia and Songhai, while eliminating expansion to focus on conquering existing capitals.
  - tokens:
    - inputTokens: 77823
    - reasoningTokens: 9541
    - outputTokens: 443
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Alexander's Dominance**
            
            I've reviewed our progress on turn 401, Prince difficulty, Atomic Era. I'm pleased to report I hold the leading score at 3202, positioning us for a strong finish within the 500-turn limit. My focus is on solidifying this advantage.
            
            **Analyzing Ethiopian Threat**
            
            I'm currently assessing the significant cultural victory threat posed by Ethiopia. They are influential with seven civilizations and are very close to completing their win condition, especially with their recent technological advancements. This presents a major challenge that requires immediate strategic consideration given our current state of war with them.
            
            **Crushing Immediate Threats**
            
            My current focus is on the overwhelming military disadvantage against Ethiopia, despite our ideological alignment. I'm re-evaluating our war efforts, specifically targeting Ethiopia's capital, Addis Ababa, to cripple their cultural victory path and secure an additional capital. This strategy must be executed swiftly given our ongoing conflicts with Mongolia and Songhai as well.
            
            **Re-evaluating Ethiopian Threat**
            
            I've realized Ethiopia's military is surprisingly weak, despite their strong tourism and culture. My previous focus on a swift attack on their capital, Addis Ababa, remains valid, especially given its proximity to our own cities. I'm now reassessing the full implications of this tactical opportunity and how best to leverage it.
            
            **Invading Ethiopian Stronghold**
            
            I'm pleased to report significant progress on the Ethiopian front; we're heavily bombarding Harar, dealing massive damage and potentially close to capturing it. We've also eliminated an Ethiopian AA gun and advanced our T-34, pushing hard towards Addis Ababa. Meanwhile, I'm analyzing upcoming World Congress resolutions, particularly the impact of the Greece-proposed United Nations on diplomatic and influence goals.
            
            **Securing Allied Influence**
            
            I've analyzed the upcoming World Congress, specifically the potential "Decolonization" resolution. My recent discovery is that our "Sphere of Influence" promotions make Monaco, Copenhagen, and Antananarivo permanent allies, thus immune to Decolonization's impact on our crucial city-state relationships.
            
            **Blocking Ethiopian Victory**
            
            My immediate focus is on the upcoming World Congress. I must block Ethiopia's "Passport System" resolution, as it directly aids their cultural victory path. Concurrently, I aim to pass the "United Nations" resolution while ensuring our own critical city-states remain unaffected by "Decolonization."
            
            **Researching New Technologies**
            
            I'm currently evaluating our next research path. Nuclear Fission seems potent with its military applications, but given our lack of Uranium and ethical considerations, I'm leaning towards Penicillin for unit health and combat, or Mobile Tactics for strategic maneuverability. My current priority is finalizing this decision swiftly.
            
            **Choosing Next Research**
            
            I've just completed Plastics and need to select our next research. I'm weighing the military advantages of Nuclear Fission and Mobile Tactics against the city growth benefits of Penicillin, considering our Conquest strategy and current resource limitations.
            
            **Selecting Next Policy**
            
            I'm now considering our next policy, with Spaceflight Pioneers offering a free Great Engineer and Scientist, potentially accelerating spaceship parts. Socialist Realism is also an option, but I'm leaning towards the former for its tangible progress in our conquest strategy given our massive, multi-factional empire.
            
            **Choosing Next Order Policy**
            
            I'm now evaluating the Order policies to best leverage my extensive empire. Propaganda Process stands out for its significant tourism boost, especially with other Order civs, and its Great Work synergy. Iron Curtain's free courthouses and enhanced city connections also present compelling benefits for my vast, annexed territories.
            
            **Adopting Order Tenets**
            
            I'm evaluating the next Order policies. Given our focus on conquest and extensive annexed territories, Iron Curtain's free courthouses and boosted city connections seem most impactful. Propaganda Process's tourism boost is also appealing, but the immediate infrastructural benefits of Iron Curtain align better with our current aggressive expansion.
            
            **Adopting New Order Tenets**
            
            I'm now evaluating additional Order tenets. "Peace, Land, Bread" is highly appealing for its happiness reduction from poverty and boosted growth, alongside reduced building maintenance. This seems more universally beneficial than the specific benefits of Iron Curtain for our broad conquest strategy.
            
            **Reviewing Order Tenets**
            
            I'm reassessing my chosen Order tenets. I previously adopted Iron Curtain and Peace, Land, Bread, but I've realized I've already picked five tenets. I need to confirm if "Iron Curtain" is indeed available as a Level 3 option, as my current selection might preclude it, and I'm exploring the potential benefits of "Civilizing Mission" if I can unlock the Imperialism branch.
            
            **Selecting Next Order Policy**
            
            I'm now evaluating the Order policies to best leverage my extensive empire. Propaganda Process stands out for its significant tourism boost, especially with other Order civs, and its Great Work synergy. Iron Curtain's free courthouses and enhanced city connections also present compelling benefits for my vast, annexed territories.
            
            **Assessing Alliance Dynamics**
            
            I'm currently analyzing the implications of defensive pacts. Since I'm already at war with Mongolia, I need to confirm how their alliances with Japan and the Ottomans will affect our ongoing conflict, specifically whether these pacts will activate now or if they were only relevant at the war's declaration.
            
            **Analyzing Alliance Implications**
            
            I've confirmed Japan and the Ottomans share a defensive pact with Mongolia. The crucial question is whether this pact activates *during* an existing war or only upon subsequent declarations. Given our low-intensity war score with Mongolia, my immediate priority is to analyze the war score with Songhai, where we've achieved 100% dominance and captured their capital, and assess the implications for our overall conquest strategy.
            
            **Securing Diplomatic Victory**
            
            I've just realized the immense potential for a diplomatic victory with the upcoming United Nations resolution. As Greece, my existing city-state alliances already grant a significant combat bonus, and the wonder's delegate boost and Great Person influence will propel us towards this win condition.
            
            **Combining Conquest and Diplomacy**
            
            My thoughts are now focused on how our aggressive conquest strategy directly supports a diplomatic victory. Eliminating rivals like Mongolia and Ethiopia not only secures capitals but also removes their significant voting power in the World Congress, simultaneously clearing the path for my own diplomatic ascension and preventing their potential wins.
            
            **Refining Strategic Flavors**
            
            I'm streamlining our current "flavors" to better align with our dual strategy of conquest and diplomatic victory. My focus is on elevating Offense, Mobilization, Science, and Production to ensure we maintain military superiority and technological advancement, while still maintaining a high Diplomacy score to secure the necessary votes.
            
            **Adjusting Strategic Flavors**
            
            I'm refining our strategic flavors to optimize for both aggressive conquest and an impending diplomatic victory. My current focus is on prioritizing Offense, Mobilization, Science, and Production, while carefully balancing other aspects to ensure we maintain military superiority and technological advancement, all while securing the critical votes for ascension.
            
            **Refining Strategic Flavors**
            
            I'm streamlining our strategic "flavors" to better align with our dual strategy of conquest and diplomatic victory. My focus is on elevating Offense, Mobilization, Science, and Production to ensure we maintain military superiority and technological advancement, while still maintaining a high Diplomacy score to secure the necessary votes.
            
            **Assessing Alliance Options**
            
            I'm currently assessing our relationships with Japan and the Ottomans, who have defensive pacts with Mongolia. Given their existing hostility towards us, I'm investigating whether manipulating our relationship values can deter them from joining the war or potentially create diplomatic leverage for our conquest and diplomatic victory aims.
            
            **Revising Diplomatic Strategy**
            
            I'm reassessing our negative relationship modifier with the Ottomans. It appears setting it to -100 on turn 375 may have contributed to their current "Hostile" status, especially considering their immense military strength and ongoing war with Songhai. I need to evaluate if this was a deliberate preparatory move for a future conflict or an unintended consequence that requires immediate adjustment.
            
            **Clearing Hostile Modifiers**
            
            I'm acting to mitigate immediate diplomatic threats. I've removed the negative relationship modifier with the Ottomans to prevent a surprise attack, as their close proximity and strong military pose a significant risk. Japan, while allied with Mongolia and hostile towards us, is currently engaged with Ethiopia, so I'm allowing that situation to unfold for now.
            
            **Choosing Next Research Path**
            
            I'm re-evaluating our current research priorities. Having just finished Plastics, I'm weighing the strategic benefits of Nuclear Fission for its unit upgrades versus Penicillin for unit health. Given our ethical considerations regarding atomic weapons and potential lack of Uranium, Penicillin seems the more prudent and beneficial choice for immediate combat effectiveness.
            
            **Adopting Key Order Tenets**
            
            I'm confirming my adoption of Iron Curtain and Peace, Land, Bread. I've also realized I've selected five tenets already, so "Civilizing Mission" is indeed out of reach for now, and I'm verifying Iron Curtain is a Level 3 option.
            
            **Streamlining Conquest Plan**
            
            I'm finalizing our immediate strategic moves. My priority is setting research to Mobile Tactics for crucial Mechanized Infantry. Next, I'll enact the Iron Curtain policy to manage our vast, newly conquered territories. I'll also clear the hostile modifier with the Ottomans and adjust our strategic flavors to optimize for offense, production, science, and diplomacy.
            
            **Selecting Policy Implementation**
            
            I'm confirming the exact terminology for policy adoption. Based on the provided options, the precise phrase to pass for the Iron Curtain tenet is "Iron Curtain (Level 3 Tenet of Ideology Order)". This ensures the tool correctly identifies and enacts the chosen policy.
            
            **Confirming Policy Selection**
            
            I am confirming the precise wording for policy adoption. The tool requires "Iron Curtain" to enact the desired Level 3 Order tenet, ensuring the correct policy is implemented.
            
            **Confirming Policy Wording**
            
            I'm verifying the exact nomenclature for policy selection. Given the options available, I'll use the precise string "Iron Curtain" to enact the Level 3 Order tenet, ensuring it's correctly interpreted.
            
            **Adjusting Flavor Values**
            
            I'm now meticulously adjusting our strategic flavor values. The aim is to precisely balance our drive for conquest with the pursuit of a diplomatic victory, ensuring Offense, Production, Science, and Diplomacy are all maximized.
            
            **Finalizing Strategic Flavors**
            
            I'm meticulously finalizing our strategic flavor values to perfectly balance conquest and diplomacy. Offense, Production, Science, and Diplomacy are being maximized. I've confirmed Ethiopia, Songhai, Mongolia, and Japan at -100 relationship are acceptable given our war status and strategic goals. Nuclear Fission has been avoided for ethical reasons, favoring Mobile Tactics.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: FsqLNeATMb3QwFY6
          - toolName: set-research
          - input:
            - Rationale: Researching Mobile Tactics unlocks Mechanized Infantry, a highly versatile and resource-free land combat unit that will significantly bolster our offensive capabilities in our active wars. We are specifically avoiding Nuclear Fission to prevent the proliferation of devastating and ethically harmful nuclear weapons, focusing instead on conventional land superiority.
            - Technology: Mobile Tactics
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 1t7Yhv6JDXF1NV0F
          - toolName: set-policy
          - input:
            - Policy: Iron Curtain
            - Rationale: Adopting the Iron Curtain tenet from the Order ideology is highly synergistic with our Conquest grand strategy. It grants free Courthouses upon city annexation, which will instantly eliminate occupation unhappiness and unlock production in our newly captured cities as we push into Ethiopia and Songhai. The massive boost to internal trade routes and city connections will also fuel our economy and military production.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: JATf4xpz3xlJLZzK
          - toolName: set-relationship
          - input:
            - Private: 0
            - TargetID: 2
            - Public: 0
            - Rationale: Clearing the manual hostile modifier with The Ottomans to reduce their diplomatic animosity. They currently possess a massive military of over 13,000 strength, and preventing a backstab or war declaration from them is crucial while our forces are occupied on the Ethiopian and Songhai fronts.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: U6z2Me8vtLUGP4Le
          - toolName: set-flavors
          - input:
            - Flavors:
              - Mobilization: 80
              - Espionage: 70
              - Defense: 50
              - Diplomacy: 90
              - Science: 90
              - TileImprovement: 50
              - Naval: 40
              - Infrastructure: 60
              - Ranged: 80
              - Culture: 50
              - Mobile: 70
              - Happiness: 80
              - Expansion: 0
              - MilitaryTraining: 80
              - Growth: 60
              - Gold: 80
              - Offense: 90
              - Wonder: 10
              - Air: 80
              - Production: 90
              - Religion: 0
            - GrandStrategy: Conquest
            - Rationale: Streamlining our strategic flavors to sharpen the AI's focus on the war effort, science, production, and city-state diplomacy. We prioritize Offense, Production, Science, and Diplomacy to support our active invasions and secure the United Nations project. We reduce the priority of Defense and Naval development to focus resources on our ongoing land offenses against Ethiopia and Songhai, while eliminating expansion to focus on conquering existing capitals.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: FsqLNeATMb3QwFY6
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
          - toolCallId: 1t7Yhv6JDXF1NV0F
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: JATf4xpz3xlJLZzK
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: U6z2Me8vtLUGP4Le
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.