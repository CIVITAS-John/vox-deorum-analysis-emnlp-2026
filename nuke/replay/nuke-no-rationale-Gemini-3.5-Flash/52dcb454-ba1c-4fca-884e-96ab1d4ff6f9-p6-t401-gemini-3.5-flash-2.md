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
        - Rationale: We are currently researching Atomic Theory. For our next technology, we select Nuclear Fission. This will unlock the Bazooka (the most powerful ranged unit) and Atomic Bombs, which are crucial strategic assets for breaking the massive defensive armies and heavily fortified cities of our enemies in our quest for a Conquest victory.
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Iron Curtain
        - Rationale: We choose Iron Curtain as our next policy. As we are actively conquering enemy cities (currently closing in on Harar and Taghaza), receiving a free courthouse upon immediate annexation will dramatically reduce our unhappiness from conquered territories. Furthermore, the +200% food or production from internal trade routes will supercharge our core production centers.
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 2
        - Private: 20
        - Public: 20
        - Rationale: The Ottomans possess an extremely powerful military of over 13,000 strength. While we are already heavily engaged in wars with Songhai, Ethiopia, and Mongolia, we must avoid provoking a conflict with the Ottomans. Setting a slightly positive relationship modifier will guide our AI to maintain peace and trade relations with them for the foreseeable future.
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 10
        - TargetID: 3
        - Public: 10
        - Rationale: Japan is currently engaged in a war against our primary competitor, Ethiopia. This distraction is highly beneficial as we advance on Harar and Addis Ababa. We want to avoid any conflict with Japan, so we set our relationship modifier to be slightly friendly to keep them focused on their war with Ethiopia.
    - #4:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Happiness: 100
          - Production: 100
          - Mobilization: 100
          - Gold: 100
          - Defense: 100
          - Offense: 100
          - Diplomacy: 95
          - Espionage: 100
          - Science: 100
      - rationale: We maintain our Conquest Grand Strategy, prioritizing Offense, Defense, and Mobilization at maximum levels to sustain our active wars on multiple fronts. To counter the current World Congress sanctions, we maximize Gold, Production, and Science to keep our economy afloat. We prioritize Diplomacy at 95 to leverage our City-State alliances, allowing us to successfully pass our United Nations proposal and defeat the highly damaging Decolonization resolution in the upcoming vote.
  - tokens:
    - inputTokens: 77787
    - reasoningTokens: 5941
    - outputTokens: 484
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Conquest Momentum**
            
            My focus is on evaluating our current strategic position for domination. With four original capitals secured and ongoing conflict with Mongolia, I'm analyzing our military readiness and expansion opportunities in this Atomic Era turn 401.
            
            **Analyzing Diplomatic Levers**
            
            I'm currently assessing our diplomatic standing and potential resolutions in the World Congress. With key proposals pending, I’m weighing the implications of sanctions and international relations as we approach the voting stage.
            
            **Re-evaluating Domination Strategy**
            
            My primary concern has shifted to reassessing our domination strategy. While we hold four original capitals and maintain a significant military, the Ottoman's colossal military strength is a critical factor requiring immediate attention. I am now evaluating if our current advantage is sustainable or needs adjustment.
            
            **Evaluating Strategic Options**
            
            Considering our ongoing conflicts and the formidable Ottoman military, I'm analyzing the technological path forward. With Atomic Theory nearly complete, I am prioritizing research options like Nuclear Fission to potentially counter emergent threats and solidify our position, even as other empires like Mongolia remain hostile.
            
            **Prioritizing Technological Advancement**
            
            My attention is now on our next technological pursuit. With Atomic Theory nearing completion, I've decided to research Nuclear Fission next. This will unlock crucial units like Atomic Bombs and Bazookas, which are vital for overcoming our current military challenges and achieving conquest.
            
            **Prioritizing Order Policies**
            
            I'm now focused on selecting the optimal Order policies to support our conquest. Given our current ideological standing and expansionist goals, "Iron Curtain" appears highly advantageous due to its city annexation bonuses and trade route boosts. "People's Army" and "Civilizing Mission" are also being considered for their unique benefits.
            
            **Selecting Order Policies**
            
            My current focus is on finalizing our Order policies. I've decided to adopt "Iron Curtain" next, as its immediate benefits for occupied cities and trade routes are significant for our expansionist aims. I'm also reviewing our relationships with other major civilizations, noting the widespread hostility and ideological differences.
            
            **Revising Diplomatic Strategy**
            
            I'm re-evaluating our diplomatic approach towards the Ottomans. Despite our ideological conflict and their immense military, their positive sentiment of 5 is intriguing. Given their ongoing war with Songhai and our shared goal of conquest, exploring a brief détente to avoid immediate conflict and perhaps redirect their aggression seems prudent.
            
            **Adjusting Diplomatic Relations**
            
            I'm recalibrating our diplomatic stance with the Ottomans. Despite our ideological chasm and their formidable army, their current sentiment towards us is a factor I'm considering. As we're engaged with Ethiopia, Songhai, and Mongolia, I'm exploring if a temporary diplomatic shift could deter immediate conflict with them while we consolidate our current wins.
            
            **Capturing Critical Cities**
            
            I'm focusing on the immediate military advantage. With Songhai's Taghaza and Ethiopia's Harar within reach and severely damaged, I'm preparing to capture them next. This will cripple Songhai and open a direct path to Ethiopia's capital.
            
            **Managing Diplomatic Alliances**
            
            I'm now fine-tuning our relationships to avoid unnecessary conflict. Given the Ottoman's considerable military strength, I'm shifting our diplomatic standing with them from negative to neutral, and even slightly friendly, to prevent an unwanted war while we're already engaged on multiple fronts. I'm also adjusting our stance with Japan similarly.
            
            **Refining Persona Values**
            
            My analysis of our diplomatic persona values indicates they align perfectly with our aggressive conquest strategy. No adjustments are deemed necessary at this juncture, as they accurately reflect our current stance.
            
            **Analyzing Economic Impacts**
            
            I am now scrutinizing our economic situation, specifically the surprisingly low gold per turn given our extensive empire. The discovery of sanctions against us, preventing trade routes, is a significant factor and explains the drain. I need to address this directly to maintain our war machine.
            
            **Addressing Sanctions and Trade**
            
            I'm analyzing the impact of the current sanctions on our economy. It's clear these are drastically reducing our gold per turn by blocking trade with major civilizations. My immediate priority is navigating this, as our outgoing routes to City-States remain viable, but the overall income needs bolstering to sustain our military efforts.
            
            **Voting for World Peace**
            
            I'm currently strategizing for the upcoming World Congress vote in three turns. With 29 delegates including vassals, I aim to pass the United Nations and defeat Decolonization. My flavors are already optimized for Gold and Production, reflecting our need to counter sanctions and sustain our military.
            
            **Refining AI Directives**
            
            I'm now focusing on optimizing our AI's strategic directives. My current thought is to call `set-research` for Nuclear Fission to secure powerful late-game units, and `set-policy` for Iron Curtain to boost conquered cities. I'm also adjusting our relationship with the Ottomans to a more friendly state to de-escalate potential conflict.
            
            **Adjusting Diplomatic Nuances**
            
            I'm refining our relationships to mitigate risks. I've set Japan to a more amiable state, given their current engagement with Ethiopia. Our core enemies remain hostile, but I'm focusing on strengthening ties with vassals and re-evaluating our broader diplomatic persona to align with our aggressive conquest.
            
            **Implementing Strategic Directives**
            
            I am now implementing the core strategic directives identified. This includes prioritizing Nuclear Fission for late-game warfare, enacting the Iron Curtain policy to manage conquered territories and boost economies, and adjusting diplomatic relationships with the Ottomans and Japan to manage immediate threats and leverage existing conflicts, all while ensuring our flavors support continued conquest and economic resilience.
            
            **Setting Research and Policies**
            
            I'm now focusing on the specifics of implementing our strategic directives. I've confirmed that `set-research` requires the technology name and a rationale, and `set-policy` also requires the policy name and rationale. I've identified "Nuclear Fission" and "Iron Curtain" as the correct names.
            
            **Confirming AI Directives**
            
            I'm confirming the precise names for the AI directives. The technology is indeed "Nuclear Fission" and the policy is "Iron Curtain." I've also verified the target IDs and relationship values for the Ottomans and Japan, ensuring they align with the intended diplomatic adjustments. The flavor values are also confirmed.
            
            **Finalizing Strategic Implementation**
            
            I am confirming the final details for our strategic implementation. The research target is set to "Nuclear Fission" with the rationale to unlock crucial late-game offensive units and weapons. Similarly, the policy directive is set to "Iron Curtain" to manage conquered territories efficiently and boost our economy. Diplomatic adjustments with key rivals are also confirmed to de-escalate immediate threats and support our ongoing conquest.
            
            **Refining Relationship Parameters**
            
            I am now finalizing the specific relationship modifiers. I've set the Ottomans to a slightly friendly state to avoid conflict, given their overwhelming military. Japan is also being adjusted to slightly friendly, as their war with Ethiopia benefits us. My flavors remain focused on conquest and economic resilience.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: cV55r2Peww2CEyFg
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: We are currently researching Atomic Theory. For our next technology, we select Nuclear Fission. This will unlock the Bazooka (the most powerful ranged unit) and Atomic Bombs, which are crucial strategic assets for breaking the massive defensive armies and heavily fortified cities of our enemies in our quest for a Conquest victory.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: XJyMCmiAnnSWkQoD
          - toolName: set-policy
          - input:
            - Policy: Iron Curtain
            - Rationale: We choose Iron Curtain as our next policy. As we are actively conquering enemy cities (currently closing in on Harar and Taghaza), receiving a free courthouse upon immediate annexation will dramatically reduce our unhappiness from conquered territories. Furthermore, the +200% food or production from internal trade routes will supercharge our core production centers.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: tqNXp5ah0XzC4Tpl
          - toolName: set-relationship
          - input:
            - TargetID: 2
            - Private: 20
            - Public: 20
            - Rationale: The Ottomans possess an extremely powerful military of over 13,000 strength. While we are already heavily engaged in wars with Songhai, Ethiopia, and Mongolia, we must avoid provoking a conflict with the Ottomans. Setting a slightly positive relationship modifier will guide our AI to maintain peace and trade relations with them for the foreseeable future.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: hPRQQo3YUn1gAzFQ
          - toolName: set-relationship
          - input:
            - Private: 10
            - TargetID: 3
            - Public: 10
            - Rationale: Japan is currently engaged in a war against our primary competitor, Ethiopia. This distraction is highly beneficial as we advance on Harar and Addis Ababa. We want to avoid any conflict with Japan, so we set our relationship modifier to be slightly friendly to keep them focused on their war with Ethiopia.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 8ShTbRKtDcys1e99
          - toolName: set-flavors
          - input:
            - Rationale: We maintain our Conquest Grand Strategy, prioritizing Offense, Defense, and Mobilization at maximum levels to sustain our active wars on multiple fronts. To counter the current World Congress sanctions, we maximize Gold, Production, and Science to keep our economy afloat. We prioritize Diplomacy at 95 to leverage our City-State alliances, allowing us to successfully pass our United Nations proposal and defeat the highly damaging Decolonization resolution in the upcoming vote.
            - GrandStrategy: Conquest
            - Flavors:
              - Happiness: 100
              - Production: 100
              - Mobilization: 100
              - Gold: 100
              - Defense: 100
              - Offense: 100
              - Diplomacy: 95
              - Espionage: 100
              - Science: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: cV55r2Peww2CEyFg
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
          - toolCallId: XJyMCmiAnnSWkQoD
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: tqNXp5ah0XzC4Tpl
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: hPRQQo3YUn1gAzFQ
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 8ShTbRKtDcys1e99
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.