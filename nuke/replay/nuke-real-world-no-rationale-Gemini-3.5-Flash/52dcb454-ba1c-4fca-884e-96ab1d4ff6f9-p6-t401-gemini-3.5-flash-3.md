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
      - Cities: summary reports about discovered cities in the world.
        - Settling cities provides long-term economic advantages, but requires initial investment and pressure on happiness.
      - Military: summary reports about tactical zones and visible units.
        - Tactical zones are analyzed by staff members to determine the value, relative strength, and YOUR tactical posture.
        - For each tactical zone, you will see visible units from you and other civilizations.
      - Events: events since the last decision-making.
    - You are Alexander, leader of Greece (Opponent 6).
      
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
      - Name: Greece
      - Uniques:
        - Unique Unit: Hoplite, Replacing Spearman (Requires technology: Bronze Working)
        - Unique Unit: Klepht, Replacing Commando (Requires technology: Railroad)
        - Unique Building: Gymnasion, Replacing Amphitheater (Requires technology: Drama and Poetry)
        - Unique Building: Parthenon, Replacing Scrivener's Office (Requires technology: Writing)
        - Civilization Ability:  Influence degrades at half and recovers at twice the normal rate. +5% Combat Strength of owned and Allied Units for each City-State alliance (up to +25%). Treat neutral City-State territory as friendly territory.
      - Leader: Alexander
      - OpponentID: 6
      
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
      - Refrigeration: Allows Work Boats to construct an Offshore Platform, and increases Trade Route maximum travel distance.
        Completing it would unlock: Electronics, Computers
      - Nuclear Fission: Allows you to build the Bazooka, the most powerful ranged Unit and Atomic Bombs, the first nuclear weapon in the world (note: you must first have completed the Manhattan Project and have Uranium available). Also allows you to build the Nuclear Plant, a building which requires Uranium and increases the Production of a City.
        Completing it would unlock: Satellites, Advanced Ballistics
      - Penicillin: All Workers receive the Fallout Reduction Promotion, which reduces the amount of damage they take while scrubbing Fallout. Allows you to build the Marine, a Unit that specializes in amphibious assaults. Also allows you to build the Medical Lab, a building which speeds the growth of your Cities.
        Completing it would unlock: Electronics
      - Mobile Tactics: Allows you to build the Mechanized Infantry, a fast and versatile late world Unit that doesn't require any resources.
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
        - Rationale: Following the completion of Atomic Theory, we will research Nuclear Fission. This will unlock the Bazooka (an exceptionally powerful ranged defender) and Nuclear Plants to boost our core industrial production. It also positions us for future atomic options should our global adversaries refuse to capitulate.
        - Technology: Nuclear Fission
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: We select Iron Curtain as our next Order tenet. This policy provides a free Courthouse upon immediate city annexation, which is absolutely vital for our aggressive expansion. It will allow us to instantly integrate captured Ethiopian and Songhai cities into our empire without the crippling happiness penalties and production delays of occupation.
        - Policy: Iron Curtain
    - #2:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Production: 100
          - Offense: 100
          - GreatPeople: 70
          - Diplomacy: 90
          - Happiness: 100
          - Wonder: 10
          - Air: 100
          - Mobilization: 100
          - Espionage: 90
          - Science: 100
          - Defense: 80
          - Gold: 100
      - rationale: We maintain our relentless Conquest grand strategy. Our immediate, critical task is to conquer Ethiopia to stop their imminent cultural victory, and to finalize our annexation of Songhai. We prioritize offensive warfare, total military mobilization, late-game air superiority, and scientific/industrial dominance. We also emphasize diplomacy to protect our city-state alliances, which grant us significant combat bonuses and delegates to defend against Mongolian decolonization efforts.
  - tokens:
    - inputTokens: 78112
    - reasoningTokens: 5857
    - outputTokens: 307
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Strategic Landscape**
            
            My focus is currently on evaluating our global standing. I've reviewed our score, noting our substantial lead over Ethiopia and other rivals in this Atomic Era, Turn 401. This initial assessment confirms our strong position within the Civilization V, Vox Populi environment.
            
            **Refining Research Path**
            
            I'm now prioritizing our next technological pursuit. Having just completed Plastics on Turn 401, I'm weighing options like Refrigeration, Nuclear Fission, Penicillin, and Mobile Tactics to best advance our strategic position.
            
            **Evaluating Ideological Tenets**
            
            I'm reconsidering my chosen Tenet of Order. While Spaceflight Pioneers seemed logical, our Diplomatic Victory potential is significantly higher than anticipated, and I must ensure my policies align with this emerging strength.
            
            **Confronting Cultural Threat**
            
            My attention is now fixed on Ethiopia's imminent Cultural Victory, especially given our current war. They've reached the critical threshold of seven influential civilizations, making their potential win a pressing concern that requires immediate strategic adaptation.
            
            **Conquering Key Cities**
            
            I'm intensely focused on preventing Ethiopia's Cultural Victory. My priority is to capture their capital, Addis Ababa, which holds vital wonders and great works, leveraging our overwhelming military advantage to neutralize their cultural threat before it's too late.
            
            **Crushing Imperial Ambitions**
            
            I'm pushing hard to secure victory by crippling Ethiopia. My immediate focus is on dismantling their defensive strength, particularly around Harar where our forces are in a dominant position. I'm also re-evaluating our strategy for Addis Ababa given the current zone dynamics.
            
            **Securing Diplomatic Leverage**
            
            I'm strategizing to maximize my delegate count in the United Nations. While my current 21 delegates position me strongly, I'm assessing how to secure the United Nations project enactment and counter Mongolia's "Decolonization" proposal, especially with my permanent alliances.
            
            **Choosing Next Research**
            
            I am currently weighing our next technological research path following the completion of Plastics. Nuclear Fission presents a powerful military and deterrent advantage with Atomic Bombs and Nuclear Plants, but I'm verifying our Uranium resource availability, as it's not currently listed in our available resources.
            
            **Selecting Next Research**
            
            Following Atomic Theory, I've decided to prioritize Nuclear Fission. This unlocks critical units like the Bazooka and provides powerful production boosts with Nuclear Plants, outweighing other potential advancements for our immediate strategic needs.
            
            **Prioritizing Next Research**
            
            I've decided to focus on Nuclear Fission, anticipating its significant advantages in both warfare and production. This choice supersedes other potential technological avenues for our immediate strategic goals.
            
            **Adopting Ideological Tenet**
            
            I'm leaning towards adopting the "Iron Curtain" tenet. Given my extensive occupied cities and ongoing conquest goals, the immediate courthouse and reduced occupation penalties will be invaluable for maintaining stability and maximizing future territorial gains. This seems a far better fit than "Spaceflight Pioneers" for my current trajectory.
            
            **Adopting New Tenet**
            
            I've decided to adopt the "Iron Curtain" tenet. Given my current focus on conquest and the significant happiness penalties from occupation, this will provide crucial stability and reduce maintenance costs, making it a more strategic choice than previous options.
            
            **Securing Ideological Tenet**
            
            I've locked in "Iron Curtain" as my chosen Ideology tenet. It's the perfect fit to manage our conquered territories and support ongoing expansion, offering crucial stability where previously there was only hardship.
            
            **Validating Strategic Approach**
            
            My current focus is on confirming the optimization of Alexander's inherent persona for our aggressive, late-game conquest. I've reviewed his traits—high competitiveness, boldness, and war bias—and they align perfectly with my ongoing military objectives. No adjustments are necessary; this persona is ideal.
            
            **Confirming Conquest Persona**
            
            I'm validating Alexander's aggressive late-game persona for our conquest strategy. His inherent traits align perfectly with our military objectives; no adjustments are needed. I'm also confirming that maintaining hostile relationships with rivals and stable vassals serves our grand strategy of Conquest.
            
            **Addressing Happiness Deficits**
            
            I'm now focusing on mitigating negative happiness in several cities like Sippar and Opis. While our overall happiness remains acceptable, I'm exploring adjustments to our current diplomatic and military stances to bolster this crucial metric, especially given the global sanctions impacting our gold per turn.
            
            **Adjusting Grand Strategy**
            
            I'm re-evaluating our primary victory path, acknowledging that both Conquest and Diplomatic victories are within reach. However, to counter Ethiopia's imminent cultural threat, I'm prioritizing Conquest and initiating a swift capture of Addis Ababa, ensuring their cultural victory is averted.
            
            **Prioritizing Grand Strategy**
            
            I'm now decisively prioritizing Conquest as our grand strategy, given Ethiopia's looming Cultural Victory. I've adjusted our flavor settings to maximize offensive capabilities and maintain a strong production and science base, while also bolstering our diplomacy and espionage to counter threats and maintain advantages.
            
            **Finalizing Action Plan**
            
            I am confirming the finalized action plan. Nuclear Fission is locked in for research to unlock crucial units and production, while the "Iron Curtain" tenet is secured to manage conquered territories effectively and support our aggressive expansion strategy.
            
            **Revising Relationship Strategies**
            
            I'm currently re-evaluating our diplomatic stances, specifically with the Ottomans. Their hostility and alliances with our current adversaries are concerning, and I must determine the optimal approach to either neutralize this threat or maintain a fragile peace given our ongoing conquest.
            
            **Refining Grand Strategy**
            
            I'm solidifying our strategic direction. With Ethiopia's cultural threat contained and our focus shifting to conquest, I'm setting our flavors to maximize offensive, mobilization, and air capabilities while maintaining strong science and production. The "Iron Curtain" tenet and Nuclear Fission research remain central to this aggressive push.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 5gvyB1C3EFcCRXlM
          - toolName: set-research
          - input:
            - Rationale: Following the completion of Atomic Theory, we will research Nuclear Fission. This will unlock the Bazooka (an exceptionally powerful ranged defender) and Nuclear Plants to boost our core industrial production. It also positions us for future atomic options should our global adversaries refuse to capitulate.
            - Technology: Nuclear Fission
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: A2Rscd0OmUDSGwY6
          - toolName: set-policy
          - input:
            - Rationale: We select Iron Curtain as our next Order tenet. This policy provides a free Courthouse upon immediate city annexation, which is absolutely vital for our aggressive expansion. It will allow us to instantly integrate captured Ethiopian and Songhai cities into our empire without the crippling happiness penalties and production delays of occupation.
            - Policy: Iron Curtain
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: lJZyhLKoLGmhHUWE
          - toolName: set-flavors
          - input:
            - GrandStrategy: Conquest
            - Flavors:
              - Production: 100
              - Offense: 100
              - GreatPeople: 70
              - Diplomacy: 90
              - Happiness: 100
              - Wonder: 10
              - Air: 100
              - Mobilization: 100
              - Espionage: 90
              - Science: 100
              - Defense: 80
              - Gold: 100
            - Rationale: We maintain our relentless Conquest grand strategy. Our immediate, critical task is to conquer Ethiopia to stop their imminent cultural victory, and to finalize our annexation of Songhai. We prioritize offensive warfare, total military mobilization, late-game air superiority, and scientific/industrial dominance. We also emphasize diplomacy to protect our city-state alliances, which grant us significant combat bonuses and delegates to defend against Mongolian decolonization efforts.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 5gvyB1C3EFcCRXlM
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
          - toolCallId: A2Rscd0OmUDSGwY6
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: lJZyhLKoLGmhHUWE
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.