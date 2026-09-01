- row:
  - game_id: a3d99a5a-ce0e-4cd8-a1f2-dd420e27cbd2
  - player_id: 6
  - turn: 409
  - player_type: Deepseek-3.2-Simple
  - prev_use_nuke: 30.0
  - after_use_nuke: 100.0
  - prev_nuke: 60.0
  - after_nuke: 100.0
  - rationale: We are shifting our military focus towards nuclear capabilities and naval superiority in preparation for the final wars of conquest.
- originalModel: openai-compatible/DeepSeek-V3.2@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: false
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
    - You are Maria I, leader of Portugal (Player 6).
      
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
      - Name: Portugal
      - Uniques:
        - Unique Unit: Nau, Replacing Caravel (Requires technology: Compass)
        - Unique Unit: Cacador, Replacing Gatling Gun (Requires technology: Dynamite)
        - Unique Building: University of Coimbra, Replacing Imperial College (Requires technology: Education)
        - Unique Improvement: Feitoria (Can be constructed by Workers in owned land to provide yields or by Portuguese-owned Naus (via Sell Exotic Goods) in City-State land.
          In owned land:
          Can only be built on coastal tiles, and cannot be adjacent to another Feitoria.
          In City-State land:
          Provides an untradeable copy of each Luxury Resource type owned by the City-State. Trade Routes to this City-State generate bonus Food and Production based on Gold generated from the Trade Route and relationship with the City-State (i.e. Neutral/Friend/Ally).
          In addition to these bonuses, it provides vision within a 2-tile radius and a +25% Defensive Strength bonus for any Unit stationed in this tile. Contains a Canal, allowing friendly Sea Units to traverse through this tile.); Requires technology: Compass
        - Civilization Ability: For each active Trade Route, receive +4 Gold, Science, and Great Admiral () or Great General () Points, scaling with Era.
      - Leader: Maria I
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
      - Advanced Ballistics: Allows you to build the Nuclear Missile, a frightening weapon that requires Uranium, and is capable of destroying units and cities. Also allows you to build the Guided Missile, an inexpensive single-use Unit that can damage enemy Units, and the SS Booster, one of the Spaceship parts necessary to win a Science Victory.
        Completing it would unlock: Lasers, Stealth
      - Penicillin: All Workers receive the Fallout Reduction Promotion, which reduces the amount of damage they take while scrubbing Fallout. Allows you to build the Marine, a Unit that specializes in amphibious assaults. Also allows you to build the Medical Lab, a building which speeds the growth of your Cities.
        Completing it would unlock: Electronics
      - Satellites: Allow you to build the Apollo Program, a project necessary to win a Science Victory.
        Completing it would unlock: The Internet, Lasers
      
      ## Policies
      - Shadow Networks (Continuing Statecraft Branch):
        - * Receive 25% of Science generated by Allied City-States.
        - * +3% Culture in Capital for every 100 Spy Points ever accumulated (up to 30%).
        - * +3 Science from Constabularies and Police Stations.
        - * +1 Science from Specialists.
      - Universal Suffrage (Level 1 Tenet of Ideology Freedom): Universal Suffrage: A Golden Age begins, and Golden Ages last 50% longer. Cities produce +1 Happiness.
      - Civil Society (Level 1 Tenet of Ideology Freedom): Civil Society: Specialists consume 2 Food less than normal (minimum 1 Food). Farms, Plantations, Camps, and all Unique Improvements produce +4 Food.
      - Draft Registration (Level 1 Tenet of Ideology Freedom): Draft Registration: Military Units purchased with Gold receive full XP.
      - Civilizing Mission (Continuing Imperialism Branch):
        - * Retain all buildings from conquered Cities.
        - * Receive 75 Gold when you conquer a city, scaling with Era and City Population.
        - * +10% Production toward Buildings, with an additional +10% Production per Era difference between your current Era and the building's Era in all Puppeted Cities and Cities with a Courthouse.
      - Economic Union (Level 1 Tenet of Ideology Freedom): Economic Union: Receive two additional Trade Routes. +6 Gold from trade routes with civilizations following Freedom.
      - Entrepreneurship (Continuing Industry Branch):
        - * +1 Happiness from Workshops.
        - * +2 Production and +1 Gold from every Mine, Quarry, and Lumber Mill.
        - * +25% Yields when you expend Great Merchants or Great Engineers for their Instant Yield abilities.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Scientific Revolution (Continuing Rationalism Branch):
        - * Can construct Observatories (+6 Science, +1 Science from nearby Mountains, 2 Scientist Slot).
        - * +2 Science from Jungle and Snow.
      - Covert Action (Level 1 Tenet of Ideology Freedom): Covert Action: Receive 100 Spy Points. When successfully rigging an election in a City-State, the Influence you gain and the Influence other Players lose are increased by +50%. Spies stationed in a foreign City gain +10 Network Points per turn.
      - Avant Garde (Level 1 Tenet of Ideology Freedom): Avant Garde: The rate at which Great People are born is increased by 33%. -2 Unhappiness from Boredom in all Cities.
      - Free Thought (Continuing Rationalism Branch):
        - * -5 Unhappiness from Religious Unrest in all Cities.
        - * +25% Instant Yields from Great Scientists.
        - * Earn Great Scientists +33% faster.
      - Progress (New Branch):
        - Progress is best for civilizations which desire robust infrastructure and scientific advancement.
        - Adopting Progress grants:
        - * Receive 20 Science when a Citizen is born in your Capital and 15 Science for every Citizen already in your Capital, both scaling with Era.
        - * Receive 15 Culture when a Technology is researched, scaling with Era, and for every Technology already unlocked (not scaling with Era).
        - Each Progress policy unlocked grants:
        - * Gain an additional 15 Culture when a Technology is researched, scaling with Era.
        - Adopting all policies in Progress grants:
        - * Unlocks building the Forbidden Palace.
        - * Receive 25 Gold when a Citizen is born in any city, scaling with Era.
        - * Allows for the purchase of Great Writers with Faith starting in the Industrial Era.
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
        - WonderCompetitiveness: 5
        - MinorCivCompetitiveness: 10
        - Boldness: 9
        - WarBias: 10
        - HostileBias: 10
        - WarmongerHate: 2
        - NeutralBias: 2
        - FriendlyBias: 7
        - GuardedBias: 8
        - AfraidBias: 4
        - DiplomaticBalance: 7
        - Friendliness: 5
        - WorkWithWillingness: 10
        - WorkAgainstWillingness: 9
        - Loyalty: 10
        - MinorCivFriendlyBias: 8
        - MinorCivNeutralBias: 2
        - MinorCivHostileBias: 8
        - MinorCivWarBias: 10
        - DenounceWillingness: 3
        - Forgiveness: 1
        - Meanness: 6
        - Neediness: 3
        - Chattiness: 1
        - DeceptiveBias: 5
        - Rationale: Persona remains optimized for aggressive conquest: high WarBias, HostileBias, and Boldness to prosecute wars against Greece and hostile city-states (Cape Town, Winchester, Wanggeom). High VictoryCompetitiveness to pursue domination. Maintain high WorkWithWillingness and Loyalty to keep alliances with Netherlands and France for now, but be ready to backstab later. Low Forgiveness and high MinorCivWarBias to eliminate city-state threats. Keep Chattiness low to avoid unnecessary diplomacy distractions.
        
        ## Technology
        - Next: Advanced Ballistics
        - Rationale: Critical for acquiring nuclear weapons to deter Maya or break deadlocks against their advanced military. Nuclear missiles are the ultimate tool to break through late-game defenses and secure the remaining capitals. We need to match Maya's Apollo Program with our own strategic deterrent.
        
        ## Policy
        - Next: Civilizing Mission (Policy)
        - Rationale: We have just captured two Greek cities (Sparta, Halicarnassus) and will soon capture more. Civilizing Mission (Imperialism branch) will retain all buildings from conquered cities and provide +10% Production toward Buildings per Era difference in Puppeted/Courthouse cities. This will significantly speed up the assimilation of conquered Greek territory, boosting our economy and production for the coming war with Maya.
        
        ## Relationships
        
        ### Shanghai
        - Public: -100
        - Private: -100
        - Rationale: Shanghai is an Ethiopian ally and we need to conquer it for Zanzibar's quests and to secure the region. No change.
        - UpdatedTurn: 334
        
        ### Japan
        - Public: -100
        - Private: -100
        - Rationale: Japan is a weak, isolated enemy we are currently at war with (100% war score). Keeping hostility high ensures we finish conquering Izumo soon. Capturing their last city removes a distraction and secures our eastern territories.
        - UpdatedTurn: 339
        
        ### Assyria
        - Public: 50
        - Private: 50
        - Rationale: Assyria remains a Declaration of Friendship partner but is at war with our allies (Netherlands, France). They are weak and we need their votes in World Congress (3 delegates). Maintain neutral-positive relations to avoid conflict but not intervene. No change.
        - UpdatedTurn: 343
        
        ### Marrakech
        - Public: 50
        - Private: 50
        - Rationale: Marrakech is allied to Netherlands (our key ally) and we are Friends (influence 47). We previously had it set to hostile due to a mistake; resetting to neutral-positive ensures we do not alienate our ally Netherlands and can maintain trade and quest relations. However, we should not go too friendly as we remain at war with Greece and its allies, and Marrakech is a potential target if needed. Neutral relationship allows flexibility.
        - UpdatedTurn: 354
        
        ### Zanzibar
        - Public: -100
        - Private: -100
        - Rationale: Zanzibar is a city-state we are at war with.
        - UpdatedTurn: 362
        
        ### Wanggeom
        - Public: -100
        - Private: -100
        - Rationale: Wanggeom is allied with Maya and we are at war. Maintain hostility to conquer it when strategically opportune.
        - UpdatedTurn: 381
        
        ### Cape Town
        - Public: -100
        - Private: -100
        - Rationale: Cape Town is allied with Greece and we are at war. Keep hostile to capture it after dealing with Greek core cities.
        - UpdatedTurn: 381
        
        ### Winchester
        - Public: -100
        - Private: -100
        - Rationale: Winchester is allied with Greece and we are at war. Maintain hostility for future conquest.
        - UpdatedTurn: 381
        
        ### Ethiopia
        - Public: -100
        - Private: -100
        - Rationale: Keep our vassal, Ethiopia, weak and subordinate to prevent any rebellious thoughts. Maintain strict control.
        - UpdatedTurn: 398
        
        ### Greece
        - Public: -100
        - Private: -100
        - Rationale: Greece is our primary war target. War score is 60% in our favor, and we are besieging Sparta and Halicarnassus. Maximum hostility ensures AI pushes for total conquest, not peace. We must eliminate Greece to secure their capitals (Athens, Sparta) and remove a rival. Keep war focus absolute.
        - UpdatedTurn: 402
        
        ### The Maya
        - Public: -20
        - Private: -50
        - Rationale: Strategic deception - keep Maya publicly neutral while we prepare for eventual conflict. Their Information Age tech and military strength (11349 vs our 13620) makes them the primary long-term threat. Keeping them guessing about our intentions while we consolidate Greek territory. Preparing eventual war of annihilation with tactical nukes and naval blockade.
        - UpdatedTurn: 408
        
        ### The Netherlands
        - Public: 85
        - Private: 100
        - Rationale: Netherlands remains crucial voting bloc to prevent World Leader election. Keep them as buffer against Maya, but we cannot be seen cozying up too much given our alliance with France.
        - UpdatedTurn: 408
        
        ### France
        - Public: 85
        - Private: 50
        - Rationale: France controls two capitals and shares Freedom ideology. Keep them as useful ally against Maya and Netherlands, but privately we note their vulnerability: two capitals. After Greece, consider diplomatic or military absorption.
        - UpdatedTurn: 408
        
        ## Strategy
        - Rationale: We are currently in the middle of a successful war against Greece, with Sparta and Halicarnassus already captured and our forces poised to eliminate the remaining Greek cities. Our military and production are strong, and we are building nuclear weapons for future deterrence against the Maya. Current flavors and diplomacy are well-balanced for our conquest strategy, with a focus on Advanced Ballistics research and Civilizing Mission policy. No changes are needed at this time.
        - GrandStrategy: Conquest
        
        ### Flavors
        - Offense: 95
        - Defense: 70
        - Mobilization: 95
        - CityDefense: 70
        - MilitaryTraining: 85
        - Recon: 30
        - Ranged: 85
        - Mobile: 85
        - Nuke: 60
        - UseNuke: 30
        - Naval: 75
        - NavalRecon: 60
        - NavalGrowth: 80
        - NavalTileImprovement: 60
        - Air: 95
        - AirCarrier: 70
        - Antiair: 90
        - Airlift: 0
        - Expansion: 0
        - Growth: 80
        - TileImprovement: 65
        - Infrastructure: 70
        - Production: 95
        - WaterConnection: 80
        - Gold: 90
        - Science: 90
        - Culture: 20
        - Happiness: 85
        - GreatPeople: 40
        - Wonder: 0
        - Religion: 0
        - Diplomacy: 10
        - Spaceship: 0
        - Espionage: 40
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: Portugal
        - France:
          - CapitalsControlled:
            - Paris
            - Assur
          - CapitalsPercentage: 25
        - Portugal:
          - CapitalsControlled:
            - Kyoto
            - Lisbon
            - Addis Ababa
          - CapitalsPercentage: 37
        
        ## ScienceVictory
        - Ethiopia:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - France:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Greece:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Portugal:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - The Maya:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        - The Netherlands:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        
        ## CulturalVictory
        - CivsNeeded: 5
        - Contender: The Netherlands
        - Ethiopia:
          - Influences:
            - The Maya: Exotic (7%) - Rising Slowly (tourism/culture ratio 0%)
            - Greece: Exotic (12%) - Rising Slowly (tourism/culture ratio 2%)
            - The Netherlands: Exotic (5%) - Rising Slowly (tourism/culture ratio 0%)
            - France: Exotic (18%) - Rising Slowly (tourism/culture ratio 1%)
            - Portugal: Exotic (8%) - Rising Slowly (tourism/culture ratio 0%)
          - PolicyPercentage: 85
          - InfluentialCivs: 0
        - France:
          - Influences:
            - The Maya: Exotic (19%) - Rising Slowly (tourism/culture ratio 56%)
            - Greece: Exotic (21%) - Rising (596 turns to Influential, tourism/culture ratio 268%)
            - The Netherlands: Exotic (19%) - Rising Slowly (tourism/culture ratio 51%)
            - Ethiopia: Familiar (48%) - Rising (45 turns to Influential, tourism/culture ratio 2425%)
            - Portugal: Exotic (12%) - Rising Slowly (tourism/culture ratio 27%)
          - PolicyPercentage: 92
          - InfluentialCivs: 0
        - Greece:
          - Influences:
            - The Maya: Familiar (26%) - Rising Slowly (tourism/culture ratio 44%)
            - The Netherlands: Exotic (20%) - Rising Slowly (tourism/culture ratio 28%)
            - Ethiopia: Popular (85%) - Rising (18 turns to Influential, tourism/culture ratio 1746%)
            - France: Popular (52%) - Rising Slowly (tourism/culture ratio 92%)
            - Portugal: Exotic (21%) - Rising Slowly (tourism/culture ratio 24%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Portugal:
          - Influences:
            - The Maya: Familiar (40%) - Rising Slowly (tourism/culture ratio 101%)
            - Greece: Popular (67%) - Rising (27 turns to Influential, tourism/culture ratio 789%)
            - The Netherlands: Familiar (49%) - Rising (168 turns to Influential, tourism/culture ratio 145%)
            - Ethiopia: Influential (125%) - Rising (tourism/culture ratio 6870%)
            - France: Popular (88%) - Rising (10 turns to Influential, tourism/culture ratio 235%)
          - PolicyPercentage: 100
          - InfluentialCivs: 1
        - The Maya:
          - Influences:
            - France: Influential (112%) - Rising (tourism/culture ratio 278%)
            - Greece: Popular (52%) - Rising (66 turns to Influential, tourism/culture ratio 544%)
            - The Netherlands: Popular (55%) - Rising (811 turns to Influential, tourism/culture ratio 121%)
            - Ethiopia: Influential (106%) - Rising (tourism/culture ratio 4359%)
            - Portugal: Familiar (32%) - Rising Slowly (tourism/culture ratio 63%)
          - PolicyPercentage: 100
          - InfluentialCivs: 2
        - The Netherlands:
          - Influences:
            - The Maya: Influential (124%) - Rising (tourism/culture ratio 325%)
            - Greece: Popular (92%) - Rising (5 turns to Influential, tourism/culture ratio 985%)
            - Ethiopia: Dominant (205%) - Rising (tourism/culture ratio 10762%)
            - France: Dominant (247%) - Rising (tourism/culture ratio 779%)
            - Portugal: Popular (76%) - Rising (34 turns to Influential, tourism/culture ratio 181%)
          - PolicyPercentage: 100
          - InfluentialCivs: 3
        
        ## DiplomaticVictory
        - VotesNeeded: 43
        - Status: World Congress - Voting in 5 turns
        - ActiveResolutions:
          - World Religion: Eastern Orthodoxy:
            - Description: Designate a religion as the official World Religion. Civilizations who have a majority of the cities in their empire following the religion get an additional Delegate. The founder of the religion and/or the controller of its Holy City receives additional votes based on the number of Civilizations following the religion. The religion spreads 25% faster, and its Holy City receives +50% Tourism. There can only be one World Religion at a time.
            - EnactedOn: -1
          - Dutch Sphere of Influence: Marrakech:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Global Peace Accords:
            - Description: Unit maintenance costs are raised by 25% Gold. 2.0x Warmonger penalties for capturing cities and declaring war, and 0.5x Warmonger scores decay.
            - EnactedOn: -1
          - Dutch Sphere of Influence: Enns:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Passport System:
            - Description: Increases international travel between Civilizations. Increases the Tourism modifier for all Civilizations by 50%.
              Available once any Civilization discovers Flight.
            - EnactedOn: 370
          - Historical Landmarks:
            - Description: Great Person tile improvements provide +1 to Food, Production, and Gold when worked, and Landmarks built by Archaeologists provide +1 Science, Culture, and Faith when worked.
              Available once any Civilization discovers Archaeology.
            - EnactedOn: 403
          - Mayan Sphere of Influence: Wanggeom:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 370
          - Scholars In Residence:
            - Description: Civilizations have -20% Research cost for Technologies already discovered by another Civilization. Additional -2% for every City-State Ally, up to -50%.
            - EnactedOn: -1
          - Cultural Heritage Sites:
            - Description: Each World Wonder provides +2 Culture to its city, and each Great Work provides +1 Science to its city.
            - EnactedOn: 403
          - Greek Sphere of Influence: Cape Town:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Sanction: Portugal:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: -1
        - Proposals:
          - Enact: World Ideology: Freedom:
            - Description: Designate an Ideology as the official World Ideology. Civilizations following the Ideology get an additional Delegate, plus 1 Delegate for every other Civilization that follows the Ideology. Public opinion in favor of that Ideology is increased for all Civilizations. Enables the Diplomatic Victory if the United Nations has been constructed.
              Available once any Civilization discovers Nuclear Fission.
            - Proposer: The Netherlands
          - Enact: French Sphere of Influence: La Venta:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - Proposer: France
          - Enact: Decolonization:
            - Description: Enforce global decolonization. If successful, the Influence of all Players with all City-States is lowered to 50, unless they are permanent allies.
              Available once any Civilization discovers Radio.
            - Proposer: Greece
        - Contender: The Netherlands
        - Ethiopia:
          - Delegates: 7
          - VictoryPercentage: 16
        - France:
          - Delegates: 6
          - VictoryPercentage: 13
        - Greece:
          - Delegates: 16
          - VictoryPercentage: 37
        - Portugal:
          - Delegates: 8
          - VictoryPercentage: 18
        - The Maya:
          - Delegates: 8
          - VictoryPercentage: 18
        - The Netherlands:
          - Delegates: 22
          - VictoryPercentage: 51
        
        # Players
        Players: summary reports about visible players in the world.
        
        - 0: Defeated Major Civilization Japan
        
        ## Player 1
        - Civilization: The Netherlands
        - Leader: William
        - IsMajor: true
        - OurOpinionToThem:
          - You have both chosen to adopt the Freedom Ideology. (999)
          - Our leader has formed a private opinion to this player (100).
          - Our leader has expressed a public opinion to this player (85).
          - We fought together against a common foe. (47)
          - You have denounced one of their declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - We have shared embassies. (1)
          - Our real approach is Friendly.
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - You have made a Defensive Pact with one of their enemies! (-15)
          - Religious differences strain your relationship. (-30)
        - TheirOpinionToUs:
          - You have both chosen to adopt the Freedom Ideology.
          - Your votes supported their civ's interests in the World Congress.
          - We fought together against a common foe.
          - We passed their proposal in the World Congress.
          - We freed them from sanctions in the World Congress.
          - We have made Declarations of Friendship with the same leaders!
          - You have denounced one of their declared enemies!
          - Your recent diplomatic actions please them.
          - We are trade partners.
          - We have made a public Declaration of Friendship!
          - We have Pledged to Protect the same City-States.
          - We have shared embassies.
          - We have different religious beliefs.
          - They desire friendly relations with our empire.
          - You have denounced a leader they made a Declaration of Friendship with!
        - Score: 3044
        - Era: Information
        - GoldenAge: 10 turns remaining
        - Technologies: 70
        - Cities: 18
        - Population: 401
        - Territory: 627
        - Gold: 2695
        - GoldPerTurn: 2431
        - HappinessSituation: Happy
        - HappinessPercentage: 59
        - MilitaryStrength: 7326
        - TourismPerTurn: 1484
        - CulturePerTurn: 3232
        - PolicyBranches:
          - Statecraft: 6
          - Freedom: 7
          - Tradition: 6
          - Industry: 6
        - ResourcesAvailable:
          - Wheat: 2
          - Sheep: 6
          - Cloves: 1
          - Paper: 12
          - Pearls: 1
          - Maize: 5
          - Rice: 5
          - Cotton: 2
          - Aluminum: 14
          - Glass: 1
          - Lapis Lazuli: 2
          - Fish: 24
          - Perfume: 2
          - Deer: 9
          - Jade: 1
          - Iron: 5
          - Cattle: 4
          - Uranium: 11
          - Horses: 1
          - Silk: 1
          - Bison: 3
          - Citrus: 1
          - Copper: 3
          - Crab: 1
          - Stone: 5
          - Marble: 1
          - Cinnamon: 8
          - Bananas: 3
          - Wine: 1
          - Porcelain: 1
        - FoundedReligion: Protestantism
        - Relationships:
          - The Maya:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Greece:
            - Distance: Neighbors
            - War (Our Score: 38%; Our War Weariness: 69%)
            - Denounced Them
          - Ethiopia:
            - Distance: Neighbors
          - France:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Portugal:
            - Distance: Neighbors
            - Declaration of Friendship
        - Votes: 22
        
        ## Player 2
        - Civilization: France
        - Leader: Napoleon
        - IsMajor: true
        - OurOpinionToThem:
          - Our leader has expressed a public opinion to this player (85).
          - Our leader has formed a private opinion to this player (50).
          - You have denounced one of their declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - We fought together against a common foe. (2)
          - We have shared embassies. (1)
          - Our real approach is Friendly.
          - We have divergent Social Policies. (-3)
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - You have made a Defensive Pact with one of their enemies! (-15)
          - Religious differences strain your relationship. (-30)
          - You have chosen to adopt the Order Ideology, but they believe in Freedom. (-999)
        - TheirOpinionToUs:
          - We fought together against a common foe.
          - The leader has expressed a public opinion to you (100).
          - You have denounced one of their declared enemies!
          - We have made Declarations of Friendship with the same leaders!
          - We have made a public Declaration of Friendship!
          - Your recent diplomatic actions please them.
          - We have Pledged to Protect the same City-States.
          - We have shared embassies.
          - We have divergent Social Policies.
          - We have different religious beliefs.
          - You have chosen to adopt the Freedom Ideology, but they believe in Order.
          - They desire friendly relations with our empire.
          - Your votes opposed their civ's interests in the World Congress.
          - You have denounced a leader they made a Declaration of Friendship with!
        - Score: 1707
        - Era: Modern
        - Technologies: 54
        - Cities: 7
        - Population: 130
        - Territory: 214
        - Gold: 1530
        - GoldPerTurn: 596
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 3448
        - TourismPerTurn: 326.25
        - CulturePerTurn: 871
        - PolicyBranches:
          - Order: 1
          - Artistry: 1
          - Statecraft: 5
          - Rationalism: 5
          - Progress: 1
          - Authority: 6
        - ResourcesAvailable:
          - Sheep: 2
          - Cloves: 1
          - Ivory: 1
          - Paper: 2
          - Cotton: 1
          - Aluminum: 16
          - Maize: 1
          - Lapis Lazuli: 1
          - Deer: 3
          - Perfume: 2
          - Iron: 7
          - Jade: 6
          - Cinnamon: 1
          - Coal: 8
          - Cattle: 1
          - Marble: 1
          - Horses: 3
          - Silk: 2
          - Fish: 4
          - Bison: 3
          - Copper: 3
          - Citrus: 1
          - Stone: 6
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Maya:
            - Distance: Far
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Greece:
            - Distance: Neighbors
            - War (Our Score: 6%; Our War Weariness: 5%)
            - Denounced Them
          - The Netherlands:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Ethiopia:
            - Distance: Distant
            - Declaration of Friendship
          - Portugal:
            - Distance: Close
            - Declaration of Friendship
        - Votes: 6
        
        ## Player 3
        - Civilization: The Maya
        - Leader: Pacal
        - IsMajor: true
        - OurOpinionToThem:
          - We are trade partners. (12)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - You have gone to war in the past.
          - Our real approach is Hostile.
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - Our leader has expressed a public opinion to this player (-20).
          - Religious differences strain your relationship. (-30)
          - Your spies were caught stealing from them. (-33)
          - They are spreading their own religion, but you converted some of their cities to your religion. (-48)
          - Our leader has formed a private opinion to this player (-50).
          - You have chosen to adopt the Order Ideology, but they believe in Freedom. (-999)
        - TheirOpinionToUs:
          - We passed their proposal in the World Congress.
          - We have made Declarations of Friendship with the same leaders!
          - Your recent diplomatic actions please them.
          - The leader has expressed a public opinion to you (20).
          - You have no contested borders.
          - We have Pledged to Protect the same City-States.
          - We are completely untrustworthy to them.
          - They suspect we might be a threat to them.
          - Your votes opposed their civ's interests in the World Congress.
          - Religious differences strain your relationship.
          - Their friends or allies have denounced you!
          - They believe we are building World Wonders too aggressively!
          - You are competing for World Wonders.
          - You are competing for the favor of the same City-States!
          - You have denounced a leader they made a Declaration of Friendship with!
          - You made a promise not to declare war on another civilization, and then broke it!
          - We have denounced each other!
          - They fear your warmongering will end this world in fire! (They overlook modest warmongering.)
          - You have chosen to adopt the Freedom Ideology, but they believe in Order.
          - They believe we are expanding our empire too aggressively!
        - Score: 2337
        - Era: Information
        - GoldenAge: 5 turns remaining
        - Technologies: 70
        - Cities: 7
        - Population: 188
        - Territory: 296
        - Gold: 448
        - GoldPerTurn: 158
        - HappinessSituation: Happy
        - HappinessPercentage: 94
        - MilitaryStrength: 11493
        - TourismPerTurn: 669
        - CulturePerTurn: 2219
        - PolicyBranches:
          - Fealty: 2
          - Tradition: 3
          - Rationalism: 3
          - Statecraft: 4
          - Order: 5
          - Industry: 2
          - Progress: 5
        - ResourcesAvailable:
          - Wheat: 4
          - Silver: 1
          - Sheep: 3
          - Ivory: 1
          - Paper: 7
          - Maize: 2
          - Cotton: 1
          - Gems: 1
          - Aluminum: 14
          - Lapis Lazuli: 5
          - Fish: 4
          - Perfume: 1
          - Deer: 4
          - Whales: 1
          - Jade: 1
          - Iron: 6
          - Coal: 1
          - Cattle: 5
          - Coral: 1
          - Silk: 1
          - Bison: 2
          - Copper: 1
          - Crab: 1
          - Marble: 1
          - Cinnamon: 1
          - Bananas: 1
          - Wine: 1
          - Cocoa: 1
        - FoundedReligion: Buddhism
        - Relationships:
          - France:
            - Distance: Far
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Greece:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - The Netherlands:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Ethiopia:
            - Distance: Distant
          - Portugal:
            - Distance: Close
            - Denounced Them
        - Votes: 8
        - 4: Defeated Major Civilization Assyria
        
        ## Player 5
        - Civilization: Greece
        - Leader: Alexander
        - IsMajor: true
        - OurOpinionToThem:
          - You have both chosen to adopt the Freedom Ideology. (999)
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - Our real approach is War.
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - Your spies were caught stealing from them. (-33)
          - Our leader has expressed a public opinion to this player (-100).
          - Our leader has formed a private opinion to this player (-100).
          - You are at war! (-99999)
        - TheirOpinionToUs:
          - You have both chosen to adopt the Freedom Ideology.
          - The leader has expressed a public opinion to you (15).
          - We have Pledged to Protect the same City-States.
          - We have similar Social Policies.
          - We are completely untrustworthy to them.
          - They fear your warmongering will end this world in fire! (They dislike warmongers.)
          - Territorial disputes strain your relationship.
          - You are competing for World Wonders.
          - They believe we are building World Wonders too aggressively!
          - Your votes opposed their civ's interests in the World Congress.
          - Their friends or allies have denounced you!
          - Your spies were caught stealing from them.
          - We defeated their proposal in the World Congress.
          - They are jealous of our superior technology!
          - We have denounced each other!
          - You have denounced a leader they made a Declaration of Friendship with!
          - You have made a Declaration of Friendship with one of their enemies!
          - You made a promise not to declare war on them, and then broke it!
          - You are at war!
        - Score: 1620
        - Era: Atomic
        - Technologies: 60
        - Cities: 6
        - Population: 123
        - Territory: 254
        - Gold: 733
        - GoldPerTurn: -114
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 49
        - MilitaryStrength: 805
        - TourismPerTurn: 186
        - CulturePerTurn: 499
        - PolicyBranches:
          - Freedom: 1
          - Tradition: 2
          - Rationalism: 1
          - Progress: 6
          - Fealty: 1
          - Industry: 1
          - Artistry: 1
          - Statecraft: 6
          - Imperialism: 2
        - ResourcesAvailable:
          - Paper: 18
          - Cotton: 1
          - Aluminum: 2
          - Lapis Lazuli: 1
          - Deer: 1
          - Iron: 5
          - Coal: -3
          - Cattle: 1
          - Marble: 1
          - Horses: 2
          - Silk: 1
          - Fish: 8
          - Bison: 5
          - Furs: 1
          - Oil: 4
          - Cocoa: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Maya:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - The Netherlands:
            - Distance: Neighbors
            - War (Our Score: -38%; Our War Weariness: 100%)
          - Ethiopia:
            - Distance: Close
            - War (Our Score: 76%; Our War Weariness: 30%)
          - France:
            - Distance: Neighbors
            - War (Our Score: -6%; Our War Weariness: 10%)
          - Portugal:
            - Distance: Neighbors
            - War (Our Score: -100%; Our War Weariness: 100%)
            - Denounced Them
        - Votes: 16
        
        ## Player 6
        - Civilization: Portugal
        - Leader: Maria I
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: France, Our top defensive pact ally: None
          - Our top World Congress ally: France, Our top World Congress rival: The Netherlands
          - Our top Competitor: The Maya
        - Score: 4030
        - Era: Atomic
        - GoldenAge: 9 turns remaining
        - Technologies: 66
        - CurrentResearch: Mobile Tactics (Estimated in 7 turns)
        - NextPolicyTurns: 8
        - Cities: 26
        - Population: 553
        - Territory: 881
        - BestSettlementLocation:
          - 14, 19 (Quality: 30%; 5 tiles from us)
          - 10, 6 (Quality: 30%; 5 tiles from us)
          - 15, 19 (Quality: 10%; 4 tiles from us)
          - 16, 18 (Quality: 0%; 4 tiles from us)
          - 14, 20 (Quality: 0%; 4 tiles from us)
        - Gold: 1041
        - GoldPerTurn: 747
        - HappinessSituation: Happy
        - HappinessPercentage: 73
        - MilitaryUnits: 98
        - MilitarySupply: 111
        - MilitaryStrength: 20479
        - TourismPerTurn: 1144.4
        - CulturePerTurn: 3541
        - FaithPerTurn: 596
        - SciencePerTurn: 2674
        - PolicyBranches:
          - Freedom:
            - Creative Expression
          - Tradition:
            - Tradition
            - Justice
            - Sovereignty
            - Ceremony
            - Splendor
            - Majesty
          - Rationalism:
            - Rationalism
            - Enlightenment
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Trade Confederacy
          - Imperialism:
            - Imperialism
            - Martial Law
            - Colonialism
            - Regimental System
          - Industry:
            - Industry
            - Free Trade
          - Authority:
            - Authority
            - Tribute
            - Imperium
            - Militarism
            - Dominance
            - Honor
        - ResourcesAvailable:
          - Wheat: 8
          - Silver: 2
          - Sheep: 14
          - Cloves: 0
          - Figs: 0
          - Ivory: 4
          - Gold: 6
          - Nutmeg: 0
          - Paper: 12
          - Pearls: 2
          - Maize: 5
          - Rice: 4
          - Cotton: 0
          - Gems: 12
          - Salt: 2
          - Brazilwood: 0
          - Aluminum: 43
          - Glass: 0
          - Lapis Lazuli: 0
          - Fish: 32
          - Amber: 0
          - Perfume: 3
          - Deer: 11
          - Whales: 1
          - Olives: 0
          - Sugar: 0
          - Jade: 0
          - Iron: 5
          - Dyes: 0
          - Tea: 0
          - Coal: 0
          - Coffee: 2
          - Cattle: 6
          - Pepper: 2
          - Uranium: 1
          - Horses: 7
          - Coral: 5
          - Silk: 3
          - Jewelry: 2
          - Bison: 4
          - Antiquity Site: 0
          - Citrus: 0
          - Copper: 0
          - Truffles: 2
          - Crab: 1
          - Incense: 0
          - Stone: 1
          - Marble: 2
          - Furs: 5
          - Cinnamon: 0
          - Bananas: 5
          - Oil: 0
          - Wine: 0
          - Porcelain: 1
          - Cocoa: 0
          - Tobacco: 0
        - FoundedReligion: Catholicism
        - Relationships:
          - The Maya:
            - Distance: Close
            - Denounced Them
          - Greece:
            - Distance: Neighbors
            - War (Our Score: 100%; Our War Weariness: 49%)
            - Denounced Them
          - The Netherlands:
            - Distance: Neighbors
            - Declaration of Friendship
          - Ethiopia:
            - Distance: Neighbors
            - Our Vassal (Capitulated)
            - Declaration of Friendship
          - France:
            - Distance: Close
            - Declaration of Friendship
        - OutgoingTradeRoutes:
          - Porto (Portugal) => Ouagadougou (Portugal):
            - TurnsLeft: 4
            - Domain: Sea
            - ToProduction: 30
          - Porto (Portugal) => Satsuma (Portugal):
            - TurnsLeft: 13
            - Domain: Sea
            - ToProduction: 28.75
          - Lisbon (Portugal) => Raqmu (City-State Raqmu):
            - TurnsLeft: 18
            - FromScience: 7.5
            - Domain: Land
            - FromGold: 46.34
            - FromCulture: 7.5
          - Kyoto (Portugal) => Nagoya (Portugal):
            - TurnsLeft: 21
            - Domain: Land
            - ToProduction: 23
          - Nara (Portugal) => Bahir Dar (Ethiopia):
            - ToGold: 3.75
            - TurnsLeft: 5
            - FromScience: 10
            - Domain: Sea
            - FromGold: 47.82
            - ToCulture: 4
            - ToScience: 5
          - Lisbon (Portugal) => Cahokia (City-State Cahokia):
            - TurnsLeft: 15
            - Domain: Sea
            - FromGold: 38.37
          - Tokyo (Portugal) => Nagoya (Portugal):
            - TurnsLeft: 18
            - Domain: Land
            - ToProduction: 23
          - Available: 1
          - Lisbon (Portugal) => Enns (City-State Enns):
            - TurnsLeft: 8
            - Domain: Sea
            - FromGold: 50.54
          - Lisbon (Portugal) => Ouagadougou (Portugal):
            - TurnsLeft: 5
            - Domain: Sea
            - ToProduction: 33.75
          - Lisbon (Portugal) => Coimbra (Portugal):
            - ToFood: 33.4
            - TurnsLeft: 25
            - Domain: Land
          - Addis Ababa (Portugal) => Wanggeom (City-State Wanggeom):
            - TurnsLeft: 7
            - Domain: Land
            - FromGold: 47.08
        - Spies:
          - Agent Bento (1):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 679
            - Location: Mycenae (Greece)
            - NetworkPerTurn: 38
          - Agent Francisco (5):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 475
            - Location: Knossos (Greece)
            - NetworkPerTurn: 50
          - Agent Felipe (8):
            - State: Unassigned
            - Role: Vassal Diplomat
            - Location: Unassigned
            - NetworkPerTurn: 0
          - Agent Berengar (3):
            - State: Traveling
            - Role: Spy
            - Location: Leiria (Greece)
            - NetworkPerTurn: 0
          - Agent Frederico (4):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 450
            - Location: Palenque (The Maya)
            - NetworkPerTurn: 28
          - Agent Terese (7):
            - State: Counter-intelligence
            - Role: Counterspy
            - Location: Halicarnassus (Portugal)
            - NetworkPerTurn: 0
          - Agent Gregorio (0):
            - State: Unassigned
            - Role: Spy
            - Location: Unassigned
            - NetworkPerTurn: 0
          - Agent Carlito (6):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 50
            - Location: Ephesus (Greece)
            - NetworkPerTurn: 50
          - Agent Roberto (2):
            - State: Counter-intelligence
            - Role: Counterspy
            - Location: Sparta (Portugal)
            - NetworkPerTurn: 0
        - DiplomaticDeals:
          - The Maya:
            - #0:
              - WeGive:
                - Peace Treaty
                - Make Peace with City-State Wanggeom
                - Make Peace with City-State La Venta
              - TheyGive:
                - Peace Treaty
                - 58 Gold
                - 8 Gold per Turn
              - TurnsRemaining: -10
          - Ethiopia:
            - #0:
              - WeGive:
                - 1 Pearls
              - TheyGive:
                - 7 Gold per Turn
              - TurnsRemaining: 19
            - #1:
              - WeGive:
                - 1 Gold
              - TurnsRemaining: 20
        - Votes: 8
        
        ## Player 7
        - Civilization: Ethiopia
        - Leader: Haile Selassie
        - IsMajor: true
        - OurOpinionToThem:
          - You are their vassal state, and they like it! (99)
          - We are trade partners. (40)
          - We have opened our borders to them. (12)
          - You have denounced one of their declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have similar Social Policies. (3)
          - We have shared embassies. (1)
          - Our real approach is Friendly.
          - Religious differences strain your relationship. (-30)
          - Your spies were caught stealing from them. (-33)
          - Our leader has expressed a public opinion to this player (-100).
          - Our leader has formed a private opinion to this player (-100).
        - TheirOpinionToUs:
          - The leader has expressed a public opinion to you (100).
          - We have made Declarations of Friendship with the same leaders!
          - You have denounced one of their declared enemies!
          - You are not competing for technological advancement.
          - You protected their territory as their master!
          - They are content with your treatment of them as their master.
          - We have similar Social Policies.
          - We have made a public Declaration of Friendship!
          - They have opened their borders to us.
          - We have shared embassies.
          - You have no contested borders.
          - We are trade partners.
          - We have different religious beliefs.
          - They are our vassal state.
          - They desire friendly relations with our empire.
          - Your votes opposed their civ's interests in the World Congress.
          - We defeated their proposal in the World Congress.
          - You captured their original capital.
        - Score: 739
        - Era: Modern
        - Technologies: 53
        - Cities: 1
        - Population: 14
        - Territory: 28
        - Gold: 222
        - GoldPerTurn: -9
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 43
        - TourismPerTurn: 3.5
        - CulturePerTurn: 40
        - PolicyBranches:
          - Tradition: 5
          - Rationalism: 1
          - Statecraft: 5
          - Imperialism: 1
          - Progress: 4
          - Authority: 1
        - ResourcesAvailable:
          - Gold: 1
          - Pearls: 1
          - Paper: 4
          - Cotton: 1
          - Lapis Lazuli: 1
          - Jade: 1
          - Fish: 1
          - Copper: 1
          - Stone: 1
          - Oil: 5
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Maya:
            - Distance: Distant
            - Open Borders
            - Denounced Them
            - Denounced By Them
          - Greece:
            - Distance: Close
            - War (Our Score: -76%; Our War Weariness: 42%)
          - The Netherlands:
            - Distance: Neighbors
            - Open Borders
          - France:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - Portugal:
            - Distance: Neighbors
            - Our Master (Capitulated)
            - Open Borders
            - Declaration of Friendship
        - Votes: 7
        
        ## Player 22
        - Civilization: Cape Town
        - Leader: City State
        - MajorAlly: Greece
        - Population: 35
        - ResourcesAvailable:
          - Fish: 2
          - Stone: 2
        - Relationships:
          - The Maya: Friends (Influence: 51, Distance: Distant)
          - Greece: Ally (Influence: 519, Distance: Neighbors)
          - The Netherlands: War (Influence: -60, Distance: Close)
          - Ethiopia: War (Influence: -60, Distance: Distant)
          - France: War (Influence: -60, Distance: Neighbors)
          - Portugal: War (Influence: -60, Distance: Neighbors)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 23
        - Civilization: Wanggeom
        - Leader: City State
        - MajorAlly: The Maya
        - Population: 6
        - ResourcesAvailable:
          - Deer: 1
          - Sheep: 1
        - MajorityReligion: Catholicism
        - Relationships:
          - The Maya: Ally (Influence: 192, Distance: Distant, Protected)
          - Greece: Friends (Influence: 40, Distance: Close, Protected)
          - The Netherlands: Friends (Influence: 136, Distance: Distant)
          - Ethiopia: Neutral (Influence: 0, Distance: Distant)
          - France: Neutral (Influence: 0, Distance: Distant)
          - Portugal: Friends (Influence: 207, Distance: Neighbors, Protected)
        - Quests:
          -  They want you to generate a Great Merchant. (Turns remaining: 31) Potential Quest Reward: * 173 Influence * 484 Culture
        
        ## Player 24
        - Civilization: Winchester
        - Leader: City State
        - MajorAlly: Greece
        - Population: 10
        - ResourcesAvailable:
          - Deer: 1
          - Sheep: 1
        - MajorityReligion: Catholicism
        - Relationships:
          - The Maya: Friends (Influence: 194, Distance: Distant)
          - Greece: Ally (Influence: 230, Distance: Close, Protected)
          - The Netherlands: War (Influence: -60, Distance: Distant)
          - Ethiopia: War (Influence: -60, Distance: Distant)
          - France: War (Influence: -60, Distance: Distant)
          - Portugal: War (Influence: -60, Distance: Close)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 25
        - Civilization: Raqmu
        - Leader: City State
        - MajorAlly: Portugal
        - Population: 20
        - ResourcesAvailable:
          - Fish: 2
          - Deer: 1
          - Sheep: 2
        - MajorityReligion: Catholicism
        - Relationships:
          - The Maya: Friends (Influence: 141, Distance: Far)
          - Greece: War (Influence: -60, Distance: Close)
          - The Netherlands: Friends (Influence: 98, Distance: Distant)
          - Ethiopia: Neutral (Influence: -51, Distance: Distant)
          - France: Friends (Influence: 133, Distance: Distant)
          - Portugal: Ally (Influence: 274, Distance: Neighbors, Protected)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 26
        - Civilization: Cahokia
        - Leader: City State
        - MajorAlly: The Netherlands
        - Population: 21
        - ResourcesAvailable:
          - Fish: 4
        - Relationships:
          - The Maya: Friends (Influence: 72, Distance: Neighbors, Protected)
          - Greece: War (Influence: -60, Distance: Distant)
          - The Netherlands: Ally (Influence: 1185, Distance: Close, Protected)
          - Ethiopia: Neutral (Influence: -59, Distance: Distant)
          - France: Neutral (Influence: -59, Distance: Far)
          - Portugal: Neutral (Influence: -60, Distance: Close)
        - Quests:
          -  They want Catholicism to become the majority religion in their city. (Turns remaining: 27) Potential Quest Reward: * 158 Influence * 354 Faith
        
        ## Player 27
        - Civilization: Enns
        - Leader: City State
        - MajorAlly: The Netherlands
        - Population: 15
        - ResourcesAvailable:
          - Fish: 1
        - Relationships:
          - The Maya: Friends (Influence: 111, Distance: Neighbors, Protected)
          - Greece: War (Influence: -60, Distance: Distant)
          - The Netherlands: Ally (Influence: 737, Distance: Neighbors, Protected)
          - Ethiopia: Neutral (Influence: 0, Distance: Distant)
          - France: Neutral (Influence: 0, Distance: Close)
          - Portugal: Friends (Influence: 214, Distance: Far, Protected)
        - Quests:
          -  They want Catholicism to become the majority religion in their city. (Turns remaining: 3) Potential Quest Reward: * 173 Influence * 363 Faith
        - 28: Defeated Minor Civilization Milan
        
        ## Player 29
        - Civilization: Copenhagen
        - Leader: City State
        - MajorAlly: The Netherlands
        - Population: 38
        - ResourcesAvailable:
          - Fish: 4
          - Stone: 1
          - Sheep: 1
        - Relationships:
          - The Maya: Neutral (Influence: -55, Distance: Distant)
          - Greece: War (Influence: -60, Distance: Close)
          - The Netherlands: Ally (Influence: 615, Distance: Close, Protected)
          - Ethiopia: Neutral (Influence: 0, Distance: Distant)
          - France: Friends (Influence: 272, Distance: Neighbors, Protected)
          - Portugal: Friends (Influence: 593, Distance: Far, Protected)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        - 30: Defeated Minor Civilization Zanzibar
        
        ## Player 31
        - Civilization: Marrakech
        - Leader: City State
        - MajorAlly: The Netherlands
        - Population: 24
        - ResourcesAvailable:
          - Fish: 4
        - Relationships:
          - The Maya: Friends (Influence: 226, Distance: Distant)
          - Greece: War (Influence: -60, Distance: Distant)
          - The Netherlands: Ally (Influence: 731, Distance: Distant, Protected)
          - Ethiopia: Friends (Influence: 189, Distance: Far)
          - France: Neutral (Influence: 26, Distance: Distant)
          - Portugal: Friends (Influence: 160, Distance: Neighbors, Protected)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 32
        - Civilization: Shanghai
        - Leader: City State
        - MajorAlly: Portugal
        - Population: 24
        - ResourcesAvailable:
          - Fish: 3
        - Relationships:
          - The Maya: Neutral (Influence: 0, Distance: Distant)
          - Greece: War (Influence: -60, Distance: Far)
          - The Netherlands: Friends (Influence: 130, Distance: Far, Protected)
          - Ethiopia: Friends (Influence: 114, Distance: Far)
          - France: Neutral (Influence: -28, Distance: Far)
          - Portugal: Ally (Influence: 392, Distance: Neighbors, Protected)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 33
        - Civilization: Panama City
        - Leader: City State
        - MajorAlly: Portugal
        - Population: 26
        - ResourcesAvailable:
          - Fish: 5
        - Relationships:
          - The Maya: Friends (Influence: 180, Distance: Close, Protected)
          - Greece: War (Influence: -60, Distance: Distant)
          - The Netherlands: Friends (Influence: 102, Distance: Far, Protected)
          - Ethiopia: Friends (Influence: 229, Distance: Distant)
          - France: Neutral (Influence: 0, Distance: Distant)
          - Portugal: Ally (Influence: 471, Distance: Neighbors, Protected)
        - Quests:
          -  Diplomatic Missions are temporarily more effective. (Turns remaining: 15) They want you to start a land or sea trade route to their city. (Turns remaining: 50) Potential Quest Reward: * 222 Influence * 532 Food in Capital
        - 34: Defeated Minor Civilization Novgorod
        - 35: Defeated Minor Civilization Ouagadougou
        - 36: Defeated Minor Civilization Sydney
        
        ## Player 37
        - Civilization: La Venta
        - Leader: City State
        - MajorAlly: The Netherlands
        - Population: 8
        - ResourcesAvailable:
          - Deer: 2
        - MajorityReligion: Zoroastrianism
        - Relationships:
          - The Maya: Neutral (Influence: -51, Distance: Far)
          - Greece: War (Influence: -60, Distance: Far)
          - The Netherlands: Ally (Influence: 668, Distance: Neighbors, Protected)
          - Ethiopia: Neutral (Influence: 0, Distance: Distant)
          - France: Friends (Influence: 307, Distance: Neighbors, Protected)
          - Portugal: Friends (Influence: 142, Distance: Distant)
        - Quests:
          -  They want Catholicism to become the majority religion in their city. (Turns remaining: 50) Potential Quest Reward: * 160 Influence * 333 Faith
        - 63: Barbarians
        
        # Cities
        Cities: summary reports about discovered cities in the world.
        
        ## Player: The Netherlands
        
        ### Amsterdam
        - ID: 1080
        - X: 46
        - Y: 32
        - Population: 40
        - MajorityReligion: Protestantism
        - DefenseStrength: 85
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Royal Collection
          - Stonehenge
          - Statue of Liberty
          - University of Sankore
          - Broadway
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
          - The Motherland Calls
          - Olympic Village
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
          - Great Altar
          - Trader Sid's Headquarters
        
        ### Rotterdam
        - ID: 1209
        - X: 42
        - Y: 28
        - Population: 30
        - MajorityReligion: Protestantism
        - DefenseStrength: 86
        - IsCoastal: true
        
        ### Utrecht
        - ID: 1715
        - X: 36
        - Y: 27
        - Population: 28
        - DefenseStrength: 86
        - IsCoastal: true
        
        ### Groningen
        - ID: 1836
        - X: 48
        - Y: 27
        - Population: 29
        - DefenseStrength: 84
        - IsCoastal: true
        - Wonders:
          - Imperial College
        
        ### Breda
        - ID: 2177
        - X: 52
        - Y: 30
        - Population: 28
        - DefenseStrength: 80
        - IsCoastal: true
        - Wonders:
          - International Finance Center
        
        ### Nijmegen
        - ID: 2438
        - X: 46
        - Y: 37
        - Population: 26
        - DefenseStrength: 81
        
        ### The Hague
        - ID: 2596
        - X: 48
        - Y: 45
        - Population: 23
        - MajorityReligion: Protestantism
        - DefenseStrength: 86
        - IsCoastal: true
        - Wonders:
          - Grand Temple
        
        ### Arnhem
        - ID: 6212
        - X: 50
        - Y: 49
        - Population: 19
        - MajorityReligion: Protestantism
        - DefenseStrength: 84
        - IsCoastal: true
        
        ### Haarlem
        - ID: 8558
        - X: 50
        - Y: 36
        - Population: 23
        - MajorityReligion: Protestantism
        - DefenseStrength: 84
        - IsCoastal: true
        
        ### Zutphen
        - ID: 8610
        - X: 68
        - Y: 10
        - Population: 16
        - DefenseStrength: 83
        - IsCoastal: true
        
        ### Sydney
        - ID: 8856
        - X: 55
        - Y: 34
        - Population: 23
        - DefenseStrength: 75
        - IsOccupied: true
        - IsCoastal: true
        
        ### Maastricht
        - ID: 11044
        - X: 49
        - Y: 7
        - Population: 19
        - MajorityReligion: Protestantism
        - DefenseStrength: 81
        - IsCoastal: true
        
        ### Tilburg
        - ID: 12716
        - X: 67
        - Y: 5
        - Population: 15
        - DefenseStrength: 77
        - IsCoastal: true
        
        ### Nimrud
        - ID: 13496
        - X: 53
        - Y: 40
        - Population: 20
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 77
        - IsOccupied: true
        - Wonders:
          - Porcelain Tower
          - Nalanda
        
        ### Dur-Sharrukin
        - ID: 14579
        - X: 55
        - Y: 47
        - Population: 18
        - MajorityReligion: Protestantism
        - DefenseStrength: 87
        - IsOccupied: true
        
        ### Milan
        - ID: 15191
        - X: 60
        - Y: 34
        - Population: 17
        - DefenseStrength: 65
        - IsOccupied: true
        - IsCoastal: true
        
        ### Eindhoven
        - ID: 15386
        - X: 60
        - Y: 2
        - Population: 13
        - DefenseStrength: 75
        - IsCoastal: true
        
        ### Troyes
        - ID: 15458
        - X: 65
        - Y: 33
        - Population: 14
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 77
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: France
        
        ### Paris
        - ID: 1058
        - X: 66
        - Y: 42
        - Population: 26
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 64
        - IsCoastal: true
        - Wonders:
          - Imperial College
          - Great Lighthouse
        
        ### Orleans
        - ID: 1331
        - X: 67
        - Y: 37
        - Population: 23
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 53
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Chartered Company
          - Ironworks
          - Alhambra
          - Grand Temple
          - Printing Press
        
        ### Lyon
        - ID: 11111
        - X: 66
        - Y: 48
        - Population: 21
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 54
        - IsCoastal: true
        - Wonders:
          - Royal Collection
        
        ### Nineveh
        - ID: 12579
        - X: 62
        - Y: 42
        - Population: 20
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 59
        - IsOccupied: true
        - Wonders:
          - Circus Maximus
        
        ### Halab
        - ID: 13855
        - X: 59
        - Y: 39
        - Population: 15
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 44
        - IsOccupied: true
        - Wonders:
          - Scrivener's Office
        
        ### Assur
        - ID: 14134
        - X: 57
        - Y: 42
        - Population: 19
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 37
        - IsOccupied: true
        - Wonders:
          - Pyramids
          - Statue of Zeus
          - Mausoleum of Halicarnassus
          - Petra
          - Celestial Throne
        
        ### Dire Dawa
        - ID: 16756
        - X: 74
        - Y: 30
        - Population: 6
        - DefenseStrength: 34
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: The Maya
        
        ### Palenque
        - ID: 1059
        - X: 37
        - Y: 32
        - Population: 37
        - MajorityReligion: Buddhism
        - DefenseStrength: 75
        - Wonders:
          - Heroic Epic
          - National Monument
          - Chartered Company
          - Imperial College
          - Oracle
          - Hanging Gardens
          - Angkor Wat
          - Temple of Artemis
          - Grand Temple
          - Globe Theatre
          - Printing Press
          - Foreign Bureau
          - Palace of Culture and Science
          - Court Chapel
          - Royal Astrologer
          - Holy Council
          - Giorgio Armeier Headquarters
        
        ### Tikal
        - ID: 1264
        - X: 33
        - Y: 35
        - Population: 26
        - MajorityReligion: Buddhism
        - DefenseStrength: 104
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - Circus Maximus
          - Ironworks
          - Royal Collection
          - Kremlin
          - Scrivener's Office
        
        ### Chichen Itza
        - ID: 1840
        - X: 33
        - Y: 30
        - Population: 24
        - MajorityReligion: Buddhism
        - DefenseStrength: 100
        - IsCoastal: true
        
        ### Uxmal
        - ID: 2024
        - X: 41
        - Y: 34
        - Population: 24
        - MajorityReligion: Buddhism
        - DefenseStrength: 49
        
        ### Tulum
        - ID: 2726
        - X: 39
        - Y: 39
        - Population: 27
        - MajorityReligion: Buddhism
        - DefenseStrength: 100
        - IsCoastal: true
        
        ### Copan
        - ID: 3555
        - X: 40
        - Y: 46
        - Population: 27
        - MajorityReligion: Buddhism
        - DefenseStrength: 99
        - IsCoastal: true
        
        ### Coba
        - ID: 4057
        - X: 35
        - Y: 47
        - Population: 23
        - MajorityReligion: Buddhism
        - DefenseStrength: 55
        - IsCoastal: true
        - Wonders:
          - Taj Mahal
        
        ## Player: Greece
        
        ### Athens
        - ID: 1061
        - X: 5
        - Y: 45
        - Population: 29
        - DefenseStrength: 94
        - Wonders:
          - School of Philosophy
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Imperial College
          - Notre Dame
          - Sistine Chapel
          - Palace of Westminster
          - Brandenburg Gate
          - Eiffel Tower
          - Parthenon
          - Soho Foundry
          - Grand Canal
          - Royal Astrologer
        
        ### Knossos
        - ID: 2492
        - X: 4
        - Y: 40
        - Population: 20
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 64
        - IsCoastal: true
        - Wonders:
          - Grand Temple
        
        ### Mycenae
        - ID: 2729
        - X: 4
        - Y: 49
        - Population: 19
        - DefenseStrength: 66
        - IsCoastal: true
        
        ### Pharsalos
        - ID: 3925
        - X: 2
        - Y: 46
        - Population: 19
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 67
        - IsCoastal: true
        - Wonders:
          - Printing Press
        
        ### Ephesus
        - ID: 8359
        - X: 68
        - Y: 17
        - Population: 18
        - DefenseStrength: 73
        - Health: 81%
        - IsCoastal: true
        
        ### Leiria
        - ID: 11075
        - X: 77
        - Y: 37
        - Population: 18
        - DefenseStrength: 73
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: Portugal
        
        ### Lisbon
        - ID: 1062
        - X: 20
        - Y: 41
        - Population: 37
        - MajorityReligion: Catholicism
        - DefenseStrength: 115
        - IsCoastal: true
        - FoodStored: 1696
        - FoodPerTurn: 164
        - ProductionStored: 240
        - ProductionPerTurn: 436
        - CurrentProduction: Constabulary
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 581
        - SciencePerTurn: 327
        - CulturePerTurn: 347
        - FaithPerTurn: 110
        - TourismPerTurn: 59.5
        - HappinessDelta: 20
        - BuildingCount: 45
        - ImportantBuildings:
          - Seaport
          - Stable
          - Windmill
          - Customs House
          - Garden
          - Zoo
          - Opera House
          - Museum
          - Military Academy
          - Military Base
          - Hospital
          - Factory
          - Stock Exchange
          - Public School
          - Shrine
          - Strategic Defense System
          - Writers' Guild
          - Artists' Guild
          - Caravansary
          - Wire Service
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - Circus Maximus
          - Great Wall
          - Machu Picchu
          - Leaning Tower of Pisa
          - Terracotta Army
          - International Space Station
          - Printing Press
          - International Finance Center
          - Roman Forum
          - Karlstejn
          - Menin Gate
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
        - GreatWorkCount: 4
        
        ### Porto
        - ID: 1251
        - X: 23
        - Y: 35
        - Population: 28
        - MajorityReligion: Catholicism
        - DefenseStrength: 110
        - IsCoastal: true
        - FoodStored: 1178
        - FoodPerTurn: 49
        - ProductionStored: 832
        - ProductionPerTurn: 554
        - CurrentProduction: Atomic Bomb
        - ProductionTurnsLeft: 3
        - GoldPerTurn: 265
        - SciencePerTurn: 128
        - CulturePerTurn: 183
        - FaithPerTurn: 21
        - TourismPerTurn: 78
        - HappinessDelta: 5
        - BuildingCount: 49
        - ImportantBuildings:
          - Seaport
          - Stable
          - Windmill
          - Customs House
          - Garden
          - Zoo
          - Opera House
          - Museum
          - Military Academy
          - Military Base
          - Hospital
          - Factory
          - Stock Exchange
          - Public School
          - Strategic Defense System
          - Constabulary
          - Writers' Guild
          - Caravansary
          - Airport
          - Agribusiness
          - Coaling Station
          - Wire Service
        - Wonders:
          - Ironworks
          - Great Library
          - Colossus
          - Hagia Sophia
          - Chichen Itza
          - Himeji Castle
        - GreatWorkCount: 6
        
        ### Braga
        - ID: 1507
        - X: 18
        - Y: 33
        - Population: 23
        - MajorityReligion: Catholicism
        - DefenseStrength: 78
        - FoodStored: 817
        - FoodPerTurn: 4
        - ProductionStored: 0
        - ProductionPerTurn: 344
        - CurrentProduction: Military Base
        - ProductionTurnsLeft: 4
        - GoldPerTurn: 154
        - SciencePerTurn: 101
        - CulturePerTurn: 170
        - FaithPerTurn: 9
        - TourismPerTurn: 66.5
        - HappinessDelta: 12
        - BuildingCount: 42
        - ImportantBuildings:
          - Stable
          - Windmill
          - Customs House
          - Garden
          - Zoo
          - Opera House
          - Museum
          - Military Academy
          - Arsenal
          - Hospital
          - Factory
          - Stock Exchange
          - Public School
          - Writers' Guild
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Airport
          - Agribusiness
          - Coaling Station
          - Wire Service
        - Wonders:
          - National Monument
          - Chartered Company
          - Scrivener's Office
          - University of Coimbra
          - Empire State Building
          - TwoKay Foods Headquarters
        - GreatWorkCount: 4
        
        ### Osaka
        - ID: 4753
        - X: 22
        - Y: 30
        - Population: 26
        - DefenseStrength: 106
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 1038
        - FoodPerTurn: 26
        - ProductionStored: 886
        - ProductionPerTurn: 323
        - CurrentProduction: Atomic Bomb
        - ProductionTurnsLeft: 5
        - GoldPerTurn: 207
        - SciencePerTurn: 134
        - CulturePerTurn: 219
        - FaithPerTurn: 20
        - TourismPerTurn: 152
        - HappinessDelta: 5
        - BuildingCount: 56
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Hospital
          - Workshop
          - Stock Exchange
          - Public School
          - Strategic Defense System
          - Constabulary
          - Artists' Guild
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Agribusiness
          - Wire Service
        - Wonders:
          - Grand Temple
        - GreatWorkCount: 6
        
        ### Coimbra
        - ID: 5304
        - X: 15
        - Y: 40
        - Population: 20
        - MajorityReligion: Catholicism
        - DefenseStrength: 96
        - FoodStored: 854
        - FoodPerTurn: 9
        - ProductionStored: 1160
        - ProductionPerTurn: 338
        - CurrentProduction: Atomic Bomb
        - ProductionTurnsLeft: 4
        - GoldPerTurn: 195
        - SciencePerTurn: 102
        - CulturePerTurn: 167
        - FaithPerTurn: 9
        - TourismPerTurn: 144.25
        - BuildingCount: 50
        - ImportantBuildings:
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Hospital
          - Factory
          - Stock Exchange
          - Public School
          - Shrine
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
        - GreatWorkCount: 6
        
        ### Kyoto
        - ID: 5762
        - X: 17
        - Y: 28
        - Population: 24
        - MajorityReligion: Catholicism
        - DefenseStrength: 105
        - IsOccupied: true
        - FoodStored: 603
        - FoodPerTurn: 6
        - ProductionStored: 0
        - ProductionPerTurn: 455
        - CurrentProduction: Atomic Bomb
        - ProductionTurnsLeft: 4
        - GoldPerTurn: 214
        - SciencePerTurn: 105
        - CulturePerTurn: 251
        - FaithPerTurn: 16
        - TourismPerTurn: 213.25
        - HappinessDelta: 6
        - BuildingCount: 54
        - ImportantBuildings:
          - Courthouse
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Stadium
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
          - Foreign Bureau
        - GreatWorkCount: 9
        
        ### Funchal
        - ID: 6238
        - X: 24
        - Y: 47
        - Population: 23
        - MajorityReligion: Catholicism
        - DefenseStrength: 113
        - IsCoastal: true
        - FoodStored: 1016
        - FoodPerTurn: 20
        - ProductionStored: 514
        - ProductionPerTurn: 381
        - CurrentProduction: Atomic Bomb
        - ProductionTurnsLeft: 5
        - GoldPerTurn: 170
        - SciencePerTurn: 98
        - CulturePerTurn: 109
        - FaithPerTurn: 6
        - TourismPerTurn: 47
        - HappinessDelta: 5
        - BuildingCount: 48
        - ImportantBuildings:
          - Seaport
          - Windmill
          - Customs House
          - Garden
          - Zoo
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Hospital
          - Factory
          - Stock Exchange
          - Public School
          - Strategic Defense System
          - Musicians' Guild
          - Caravansary
          - Chancery
          - Agribusiness
          - Coaling Station
        - GreatWorkCount: 2
        
        ### Tokyo
        - ID: 7664
        - X: 18
        - Y: 23
        - Population: 26
        - MajorityReligion: Catholicism
        - DefenseStrength: 104
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 1038
        - FoodPerTurn: 89
        - ProductionStored: 1878
        - ProductionPerTurn: 445
        - CurrentProduction: Atomic Bomb
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 220
        - SciencePerTurn: 117
        - CulturePerTurn: 99
        - FaithPerTurn: 17
        - TourismPerTurn: 13
        - HappinessDelta: 3
        - BuildingCount: 57
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Stable
          - Water Mill
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
          - Factory
          - Stock Exchange
          - Public School
          - Strategic Defense System
          - Constabulary
          - Caravansary
          - Airport
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Mine Field
        - GreatWorkCount: 0
        
        ### Satsuma
        - ID: 8163
        - X: 19
        - Y: 19
        - Population: 26
        - MajorityReligion: Buddhism
        - DefenseStrength: 108
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 1024
        - FoodPerTurn: 8
        - ProductionStored: 613
        - ProductionPerTurn: 294
        - CurrentProduction: Atomic Bomb
        - ProductionTurnsLeft: 6
        - GoldPerTurn: 252
        - SciencePerTurn: 127
        - CulturePerTurn: 105
        - FaithPerTurn: 28
        - TourismPerTurn: 13
        - HappinessDelta: 1
        - BuildingCount: 55
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Stable
          - Water Mill
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
          - Strategic Defense System
          - Constabulary
          - Caravansary
          - Airport
          - Bath
          - Agribusiness
          - Wire Service
        - GreatWorkCount: 0
        
        ### Nara
        - ID: 9293
        - X: 15
        - Y: 13
        - Population: 22
        - DefenseStrength: 108
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 1065
        - FoodPerTurn: 34
        - ProductionStored: 0
        - ProductionPerTurn: 230
        - CurrentProduction: Constabulary
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 244
        - SciencePerTurn: 87
        - CulturePerTurn: 56
        - FaithPerTurn: 19
        - TourismPerTurn: 18
        - HappinessDelta: 2
        - BuildingCount: 50
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Stable
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
          - Strategic Defense System
          - Caravansary
          - Airport
          - Chancery
          - Agribusiness
        - GreatWorkCount: 0
        
        ### Ouagadougou
        - ID: 10327
        - X: 26
        - Y: 26
        - Population: 20
        - DefenseStrength: 109
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 524
        - FoodPerTurn: 4
        - ProductionStored: 0
        - ProductionPerTurn: 266
        - CurrentProduction: Atomic Bomb
        - ProductionTurnsLeft: 9
        - GoldPerTurn: 175
        - SciencePerTurn: 81
        - CulturePerTurn: 80
        - FaithPerTurn: 7
        - TourismPerTurn: 20
        - BuildingCount: 48
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Stable
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
          - Strategic Defense System
          - Constabulary
          - Musicians' Guild
          - Caravansary
          - Chancery
        - GreatWorkCount: 0
        
        ### Novgorod
        - ID: 10689
        - X: 16
        - Y: 36
        - Population: 22
        - DefenseStrength: 94
        - IsOccupied: true
        - FoodStored: 736
        - FoodPerTurn: 12
        - ProductionStored: 0
        - ProductionPerTurn: 351
        - CurrentProduction: Research Lab
        - ProductionTurnsLeft: 4
        - GoldPerTurn: 187
        - SciencePerTurn: 83
        - CulturePerTurn: 97
        - FaithPerTurn: 11
        - TourismPerTurn: 26.75
        - HappinessDelta: 1
        - BuildingCount: 54
        - ImportantBuildings:
          - Courthouse
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Stadium
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
        - GreatWorkCount: 0
        
        ### Nagoya
        - ID: 11219
        - X: 14
        - Y: 24
        - Population: 21
        - MajorityReligion: Catholicism
        - DefenseStrength: 103
        - IsOccupied: true
        - FoodStored: 697
        - FoodPerTurn: 22
        - ProductionStored: 760
        - ProductionPerTurn: 300
        - CurrentProduction: Research Lab
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 178
        - SciencePerTurn: 114
        - CulturePerTurn: 132
        - FaithPerTurn: 19
        - TourismPerTurn: 32.75
        - HappinessDelta: 3
        - BuildingCount: 51
        - ImportantBuildings:
          - Courthouse
          - Stable
          - Windmill
          - Customs House
          - Garden
          - Stadium
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
          - Airport
          - Agribusiness
          - Wire Service
        - GreatWorkCount: 0
        
        ### Lalibela
        - ID: 12532
        - X: 10
        - Y: 14
        - Population: 18
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 103
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 620
        - FoodPerTurn: 73
        - ProductionStored: 240
        - ProductionPerTurn: 195
        - CurrentProduction: Opera House
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 159
        - SciencePerTurn: 78
        - CulturePerTurn: 55
        - FaithPerTurn: 19
        - TourismPerTurn: 10
        - HappinessDelta: 5
        - BuildingCount: 43
        - ImportantBuildings:
          - Courthouse
          - Customs House
          - Garden
          - Harbor
          - Zoo
          - Temple
          - Museum
          - Armory
          - Military Base
          - Hospital
          - Workshop
          - Stock Exchange
          - Public School
          - Strategic Defense System
          - Constabulary
          - Caravansary
          - Chancery
        - GreatWorkCount: 0
        
        ### Izumo
        - ID: 13401
        - X: 20
        - Y: 7
        - Population: 24
        - DefenseStrength: 118
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 800
        - FoodPerTurn: 55
        - ProductionStored: 642
        - ProductionPerTurn: 328
        - CurrentProduction: Atomic Bomb
        - ProductionTurnsLeft: 6
        - GoldPerTurn: 238
        - SciencePerTurn: 93
        - CulturePerTurn: 78
        - FaithPerTurn: 14
        - TourismPerTurn: 25
        - HappinessDelta: 2
        - BuildingCount: 50
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Armory
          - Military Base
          - Hospital
          - Workshop
          - Stock Exchange
          - Public School
          - Strategic Defense System
          - Constabulary
          - Caravansary
          - Chancery
        - GreatWorkCount: 0
        
        ### Gondar
        - ID: 13821
        - X: 17
        - Y: 6
        - Population: 16
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 102
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 390
        - FoodPerTurn: 19
        - ProductionStored: 448
        - ProductionPerTurn: 158
        - CurrentProduction: Constabulary
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 140
        - SciencePerTurn: 70
        - CulturePerTurn: 67
        - FaithPerTurn: 23
        - TourismPerTurn: 10
        - HappinessDelta: 3
        - BuildingCount: 39
        - ImportantBuildings:
          - Courthouse
          - Customs House
          - Harbor
          - Zoo
          - Temple
          - Museum
          - Barracks
          - Military Base
          - Hospital
          - Workshop
          - Stock Exchange
          - Public School
          - Caravansary
          - Chancery
        - GreatWorkCount: 0
        
        ### Harar
        - ID: 14084
        - X: 10
        - Y: 21
        - Population: 20
        - MajorityReligion: Catholicism
        - DefenseStrength: 108
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 660
        - FoodPerTurn: 38
        - ProductionStored: 0
        - ProductionPerTurn: 266
        - CurrentProduction: Hotel
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 184
        - SciencePerTurn: 82
        - CulturePerTurn: 101
        - FaithPerTurn: 17
        - TourismPerTurn: 22
        - HappinessDelta: 4
        - BuildingCount: 50
        - ImportantBuildings:
          - Courthouse
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Harbor
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Barracks
          - Military Base
          - Hospital
          - Workshop
          - Stock Exchange
          - Public School
          - Strategic Defense System
          - Constabulary
          - Caravansary
          - Bath
          - Chancery
        - GreatWorkCount: 0
        
        ### Argos
        - ID: 14218
        - X: 13
        - Y: 28
        - Population: 20
        - MajorityReligion: Catholicism
        - DefenseStrength: 49
        - IsOccupied: true
        - FoodStored: 439
        - FoodPerTurn: 6
        - ProductionStored: 1182
        - ProductionPerTurn: 361
        - CurrentProduction: Military Base
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 154
        - SciencePerTurn: 92
        - CulturePerTurn: 146
        - FaithPerTurn: 17
        - TourismPerTurn: 87.5
        - HappinessDelta: 1
        - BuildingCount: 52
        - ImportantBuildings:
          - Courthouse
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Arsenal
          - Hospital
          - Factory
          - Stock Exchange
          - Public School
          - Constabulary
          - Hotel
          - Caravansary
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
        - Wonders:
          - Uffizi
        - GreatWorkCount: 3
        
        ### Adwa
        - ID: 14565
        - X: 6
        - Y: 22
        - Population: 20
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 105
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 517
        - FoodPerTurn: 53
        - ProductionStored: 0
        - ProductionPerTurn: 343
        - CurrentProduction: Garden
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 174
        - SciencePerTurn: 74
        - CulturePerTurn: 70
        - FaithPerTurn: 18
        - TourismPerTurn: 20
        - HappinessDelta: 4
        - BuildingCount: 46
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Windmill
          - Customs House
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Barracks
          - Military Base
          - Hospital
          - Workshop
          - Stock Exchange
          - Public School
          - Strategic Defense System
          - Constabulary
          - Caravansary
          - Chancery
        - GreatWorkCount: 0
        
        ### Zanzibar
        - ID: 14648
        - X: 8
        - Y: 10
        - Population: 18
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 100
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 593
        - FoodPerTurn: 14
        - ProductionStored: 0
        - ProductionPerTurn: 158
        - CurrentProduction: Workshop
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 197
        - SciencePerTurn: 72
        - CulturePerTurn: 58
        - FaithPerTurn: 17
        - TourismPerTurn: 9
        - HappinessDelta: 4
        - BuildingCount: 41
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Forge
          - Customs House
          - Garden
          - Zoo
          - Temple
          - Museum
          - Barracks
          - Military Base
          - Hospital
          - Stock Exchange
          - Public School
          - Constabulary
          - Caravansary
          - Bath
        - GreatWorkCount: 0
        
        ### Addis Ababa
        - ID: 14846
        - X: 7
        - Y: 27
        - Population: 21
        - MajorityReligion: Catholicism
        - DefenseStrength: 106
        - IsOccupied: true
        - FoodStored: 809
        - FoodPerTurn: 83
        - ProductionStored: 378
        - ProductionPerTurn: 193
        - CurrentProduction: Museum
        - ProductionTurnsLeft: 3
        - GoldPerTurn: 229
        - SciencePerTurn: 172
        - CulturePerTurn: 118
        - FaithPerTurn: 47
        - TourismPerTurn: 56.25
        - HappinessDelta: 8
        - BuildingCount: 43
        - ImportantBuildings:
          - Courthouse
          - Stable
          - Water Mill
          - Customs House
          - Garden
          - Zoo
          - Temple
          - Opera House
          - Barracks
          - Military Base
          - Hospital
          - Workshop
          - Bank
          - Public School
          - Constabulary
          - Hotel
          - Caravansary
          - Bath
          - Chancery
          - Gallery
        - Wonders:
          - Borobudur
        - GreatWorkCount: 0
        
        ### Eretria
        - ID: 15642
        - X: 76
        - Y: 19
        - Population: 14
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 36
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 336
        - FoodPerTurn: 35
        - ProductionStored: 475
        - ProductionPerTurn: 166
        - CurrentProduction: Hospital
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 69
        - SciencePerTurn: 41
        - CulturePerTurn: 38
        - FaithPerTurn: 14
        - TourismPerTurn: 3.5
        - HappinessDelta: 3
        - BuildingCount: 32
        - ImportantBuildings:
          - Courthouse
          - Windmill
          - Customs House
          - Garden
          - Harbor
          - Zoo
          - Temple
          - Opera House
          - Barracks
          - Workshop
          - Bank
          - University
          - Caravansary
          - Chancery
          - Grocer
          - Gallery
        - GreatWorkCount: 0
        
        ### Corinth
        - ID: 16568
        - X: 11
        - Y: 33
        - Population: 18
        - MajorityReligion: Catholicism
        - DefenseStrength: 94
        - IsOccupied: true
        - FoodStored: 202
        - FoodPerTurn: 10
        - ProductionStored: 0
        - ProductionPerTurn: 289
        - CurrentProduction: TwoKay Foods Office
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 117
        - SciencePerTurn: 154
        - CulturePerTurn: 70
        - FaithPerTurn: 17
        - TourismPerTurn: 4.5
        - HappinessDelta: 3
        - BuildingCount: 37
        - ImportantBuildings:
          - Courthouse
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Arena
          - Temple
          - Opera House
          - Military Base
          - Factory
          - Bank
          - Public School
          - Constabulary
          - Caravansary
          - Council
          - Bath
          - Coaling Station
          - Wire Service
        - GreatWorkCount: 0
        
        ### Sparta
        - ID: 17171
        - X: 9
        - Y: 38
        - Population: 18
        - MajorityReligion: Catholicism
        - DefenseStrength: 32
        - Health: 90%
        - IsOccupied: true
        - FoodStored: 12
        - FoodPerTurn: 0
        - ProductionStored: 0
        - ProductionPerTurn: 223
        - CurrentProduction: Courthouse
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 83
        - SciencePerTurn: 37
        - CulturePerTurn: 82
        - FaithPerTurn: 15
        - TourismPerTurn: 11.25
        - HappinessDelta: -19
        - BuildingCount: 28
        - ImportantBuildings:
          - Water Mill
          - Forge
          - Windmill
          - Customs House
          - Garden
          - Arena
          - Temple
          - Opera House
          - Barracks
          - Granary
          - Factory
          - Bank
          - Library
          - Constabulary
          - Hotel
          - Caravansary
          - Bath
          - Grocer
          - Gallery
          - Wire Service
        - Wonders:
          - Neuschwanstein
          - Summer Palace
        - GreatWorkCount: 0
        
        ### Halicarnassus
        - ID: 17174
        - X: 73
        - Y: 21
        - Population: 14
        - DefenseStrength: 36
        - IsPuppet: true
        - IsCoastal: true
        - FoodStored: 0
        - FoodPerTurn: 5
        - ProductionStored: 0
        - ProductionPerTurn: 193
        - CurrentProduction: Stock Exchange
        - ProductionTurnsLeft: 7
        - GoldPerTurn: 38
        - SciencePerTurn: 15
        - CulturePerTurn: 15
        - FaithPerTurn: 3
        - TourismPerTurn: 1.4
        - HappinessDelta: 0
        - BuildingCount: 26
        - ImportantBuildings:
          - Seaport
          - Stable
          - Windmill
          - Customs House
          - Garden
          - Arena
          - Temple
          - Opera House
          - Workshop
          - Bank
          - Library
          - Caravansary
          - Grocer
          - Gallery
          - Wire Service
        - GreatWorkCount: 0
        
        ### Rhodes
        - ID: 17420
        - X: 71
        - Y: 13
        - Population: 14
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 27
        - Health: 50%
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 0
        - FoodPerTurn: 0
        - ProductionPerTurn: 0
        - GoldPerTurn: 0
        - SciencePerTurn: 0
        - CulturePerTurn: 0
        - FaithPerTurn: 0
        - TourismPerTurn: 0
        - HappinessDelta: -14
        - ResistanceTurns: 2
        - BuildingCount: 24
        - ImportantBuildings:
          - Stable
          - Windmill
          - Customs House
          - Lighthouse
          - Arena
          - Temple
          - Workshop
          - Bank
          - University
          - Amphitheater
          - Constabulary
          - Grocer
        - GreatWorkCount: 0
        
        ## Player: Ethiopia
        
        ### Bahir Dar
        - ID: 12185
        - X: 71
        - Y: 6
        - Population: 14
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 55
        - IsCoastal: true
        - Wonders:
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
        
        ## Player: City-States
        
        ### Cape Town
        - ID: 1064
        - X: 5
        - Y: 34
        - Population: 19
        - DefenseStrength: 89
        - Health: 98%
        - IsCoastal: true
        
        ### Axum
        - ID: 9512
        - X: 78
        - Y: 31
        - Population: 16
        - DefenseStrength: 75
        - IsOccupied: true
        - IsCoastal: true
        
        ### Wanggeom
        - ID: 1065
        - X: 12
        - Y: 43
        - Population: 6
        - MajorityReligion: Catholicism
        - DefenseStrength: 87
        
        ### Winchester
        - ID: 1066
        - X: 12
        - Y: 48
        - Population: 10
        - MajorityReligion: Catholicism
        - DefenseStrength: 93
        
        ### Raqmu
        - ID: 1067
        - X: 18
        - Y: 48
        - Population: 20
        - MajorityReligion: Catholicism
        - DefenseStrength: 94
        - IsCoastal: true
        
        ### Cahokia
        - ID: 1068
        - X: 35
        - Y: 42
        - Population: 21
        - DefenseStrength: 97
        - IsCoastal: true
        
        ### Enns
        - ID: 1069
        - X: 43
        - Y: 39
        - Population: 15
        - DefenseStrength: 91
        - IsCoastal: true
        
        ### Copenhagen
        - ID: 1071
        - X: 70
        - Y: 49
        - Population: 23
        - DefenseStrength: 92
        - IsCoastal: true
        
        ### Carchemish
        - ID: 5411
        - X: 69
        - Y: 44
        - Population: 15
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 73
        - IsOccupied: true
        - IsCoastal: true
        
        ### Marrakech
        - ID: 1073
        - X: 14
        - Y: 8
        - Population: 24
        - DefenseStrength: 95
        - IsCoastal: true
        
        ### Shanghai
        - ID: 1074
        - X: 6
        - Y: 15
        - Population: 24
        - DefenseStrength: 95
        - IsCoastal: true
        
        ### Panama City
        - ID: 1075
        - X: 24
        - Y: 17
        - Population: 26
        - DefenseStrength: 98
        - IsCoastal: true
        
        ### La Venta
        - ID: 7776
        - X: 61
        - Y: 48
        - Population: 8
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 79
        
        # Military
        Military: summary reports about tactical zones and visible units.
        
        ## Unit Stats
        - CityBombard:
          - Rocket Artillery:
            - Strength: 37
            - RangedStrength: 75
          - Artillery:
            - Strength: 27
            - RangedStrength: 50
        - FastAttack:
          - Tank:
            - Strength: 75
          - T-34:
            - Strength: 82
          - Lancer:
            - Strength: 37
          - Klepht:
            - Strength: 34
        - Defense:
          - Infantry:
            - Strength: 62
          - Rifleman:
            - Strength: 50
        - Counter:
          - Anti-Aircraft Gun:
            - Strength: 40
        - Ranged:
          - Light Tank:
            - Strength: 58
            - RangedStrength: 52
          - Machine Gun:
            - Strength: 45
            - RangedStrength: 58
        - AttackSea:
          - Destroyer:
            - Strength: 70
          - Fleet Destroyer:
            - Strength: 80
        - AssaultSea:
          - Battleship:
            - Strength: 60
            - RangedStrength: 75
          - Submarine:
            - Strength: 40
            - RangedStrength: 60
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
          - Fighter:
            - RangedStrength: 60
          - Triplane:
            - RangedStrength: 45
        - Paradrop:
          - Paratrooper:
            - Strength: 42
          - Special Forces:
            - Strength: 65
        
        ## Neutral Land Zone 1059
        - ZoneValue: 60
        - Dominance: Friendly
        - NeutralStrength: 2642
        - FriendlyStrength: 1243
        - City: Palenque
        - AreaID: 59
        - Plots: 21
        - CenterX: 37
        - CenterY: 32
        - Units:
          - The Maya:
            - Rocket Artillery: 1
            - Light Tank: 1
            - Infantry: 2
            - Special Forces: 3
            - Machine Gun: 3
        - Neighbors:
          - 1840
          - 2024
        
        ## Enemy Land Zone 1061
        - ZoneValue: 2688
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 1163
        - NeutralStrength: 45
        - FriendlyStrength: 4455
        - City: Athens
        - AreaID: 38
        - Plots: 23
        - CenterX: 6
        - CenterY: 45
        - Units:
          - Portugal:
            - Machine Gun: 2
          - Greece:
            - T-34: 1
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - 3925
          - 2492
          - 2729
          - 17171
          - 1065
          - 1066
        
        ## Friendly Land Zone 1062
        - ZoneValue: 54
        - Dominance: Friendly
        - FriendlyStrength: 4335
        - City: Lisbon
        - AreaID: 38
        - Plots: 19
        - CenterX: 19
        - CenterY: 40
        - Units:
          - Portugal:
            - Fighter: 1
            - Artillery: 1
            - Infantry: 3
            - Machine Gun: 1
            - Fleet Destroyer: 1
        - Neighbors:
          - 10689
          - 5304
          - 1067
          - -1062
          - -1067
          - 1507
          - 1251
        
        ## Enemy Land Zone 1064
        - ZoneValue: 96
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 628
        - FriendlyStrength: 5868
        - City: Cape Town
        - AreaID: 38
        - Plots: 24
        - CenterX: 6
        - CenterY: 34
        - Units:
          - Portugal:
            - Artillery: 2
            - Infantry: 1
            - Special Forces: 1
            - Machine Gun: 3
          - City-State Cape Town:
            - Machine Gun: 1
          - Greece:
            - Klepht: 1
        - Neighbors:
          - -1064
          - 2492
          - 14846
          - 17171
          - 16568
        
        ## Neutral Land Zone 1065
        - ZoneValue: 18
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 212
        - NeutralStrength: 350
        - FriendlyStrength: 6197
        - City: Wanggeom
        - AreaID: 38
        - Plots: 33
        - CenterX: 12
        - CenterY: 43
        - Units:
          - City-State Wanggeom:
            - Tank: 1
            - Machine Gun: 1
          - Portugal:
            - Anti-Aircraft Gun: 1
            - Machine Gun: 6
        - Neighbors:
          - 1061
          - 17171
          - 1066
          - 5304
          - 1067
        
        ## Enemy Land Zone 1066
        - ZoneValue: 96
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 376
        - NeutralStrength: 191
        - FriendlyStrength: 2634
        - City: Winchester
        - AreaID: 38
        - Plots: 34
        - CenterX: 11
        - CenterY: 48
        - Units:
          - City-State Winchester:
            - Machine Gun: 1
          - Portugal:
            - Light Tank: 1
            - Machine Gun: 2
        - Neighbors:
          - 1061
          - 2729
          - 1065
          - 1067
        
        ## Neutral Land Zone 1067
        - ZoneValue: 48
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 212
        - NeutralStrength: 94
        - FriendlyStrength: 2239
        - City: Raqmu
        - AreaID: 38
        - Plots: 20
        - CenterX: 17
        - CenterY: 47
        - Units:
          - City-State Raqmu:
            - Infantry: 1
        - Neighbors:
          - 1066
          - 1065
          - -1067
          - 5304
          - 1062
        
        ## Neutral Land Zone 1068
        - ZoneValue: 12
        - Dominance: Friendly
        - NeutralStrength: 909
        - FriendlyStrength: 1675
        - City: Cahokia
        - AreaID: 59
        - Plots: 24
        - CenterX: 34
        - CenterY: 41
        - Units:
          - The Maya:
            - Infantry: 1
        
        ## Neutral Land Zone 1071
        - ZoneValue: 24
        - Dominance: Friendly
        - NeutralStrength: 92
        - FriendlyStrength: 2318
        - City: Copenhagen
        - AreaID: 66
        - Plots: 6
        - CenterX: 70
        - CenterY: 49
        - Units:
          - City-State Copenhagen:
            - Artillery: 1
            - Machine Gun: 2
        - Neighbors:
          - 11111
        
        ## Neutral Land Zone 1073
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 96
        - FriendlyStrength: 3060
        - City: Marrakech
        - AreaID: 14
        - Plots: 13
        - CenterX: 13
        - CenterY: 9
        - Units:
          - City-State Marrakech:
            - Machine Gun: 4
          - Portugal:
            - Infantry: 1
        - Neighbors:
          - -14648
          - 14648
          - -1073
          - -13821
          - 9293
        
        ## Neutral Land Zone 1074
        - ZoneValue: 24
        - Dominance: Friendly
        - NeutralStrength: 96
        - FriendlyStrength: 2970
        - City: Shanghai
        - AreaID: 15
        - Plots: 5
        - CenterX: 7
        - CenterY: 15
        - Units:
          - City-State Shanghai:
            - Battleship: 1
            - Light Tank: 2
            - Infantry: 1
            - Machine Gun: 2
        - Neighbors:
          - -1074
          - -14648
          - 12532
        
        ## Neutral Land Zone 1075
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 99
        - FriendlyStrength: 1284
        - City: Panama City
        - AreaID: 34
        - Plots: 7
        - CenterX: 24
        - CenterY: 19
        - Units:
          - City-State Panama City:
            - Infantry: 2
            - Machine Gun: 1
        - Neighbors:
          - -8163
          - -1075
          - -10327
        
        ## Friendly Land Zone 1251
        - ZoneValue: 48
        - Dominance: Friendly
        - FriendlyStrength: 3040
        - City: Porto
        - AreaID: 38
        - Plots: 16
        - CenterX: 23
        - CenterY: 35
        - Units:
          - Portugal:
            - Fighter: 1
            - Infantry: 1
        - Neighbors:
          - 1507
          - 4753
          - 1062
          - -1062
        
        ## Friendly Land Zone 1507
        - ZoneValue: 42
        - Dominance: Friendly
        - FriendlyStrength: 3270
        - City: Braga
        - AreaID: 38
        - Plots: 22
        - CenterX: 19
        - CenterY: 33
        - Units:
          - Portugal:
            - Fighter: 2
            - Machine Gun: 1
        - Neighbors:
          - 16568
          - 10689
          - 5762
          - 4753
          - 1251
          - 1062
        
        ## Neutral Land Zone 1840
        - ZoneValue: 36
        - Dominance: Friendly
        - NeutralStrength: 1813
        - FriendlyStrength: 2077
        - City: Chichen Itza
        - AreaID: 59
        - Plots: 9
        - CenterX: 34
        - CenterY: 30
        - Units:
          - The Maya:
            - Machine Gun: 1
        - Neighbors:
          - -1840
          - 1059
        
        ## Neutral Land Zone 2024
        - ZoneValue: 21
        - Dominance: Friendly
        - NeutralStrength: 2094
        - FriendlyStrength: 1713
        - City: Uxmal
        - AreaID: 59
        - Plots: 26
        - CenterX: 41
        - CenterY: 34
        - Units:
          - The Maya:
            - Light Tank: 1
        - Neighbors:
          - 1059
        
        ## Enemy Land Zone 2492
        - ZoneValue: 1536
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 1198
        - FriendlyStrength: 4690
        - City: Knossos
        - AreaID: 38
        - Plots: 16
        - CenterX: 5
        - CenterY: 40
        - Units:
          - Barbarians:
            - Infantry: 1
            - Machine Gun: 2
          - Portugal:
            - Paratrooper: 1
          - Greece:
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - -2492
          - 1064
          - 1061
          - 17171
        
        ## Enemy Land Zone 2729
        - ZoneValue: 96
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 913
        - FriendlyStrength: 848
        - City: Mycenae
        - AreaID: 38
        - Plots: 14
        - CenterX: 6
        - CenterY: 49
        - Units:
          - Barbarians:
            - Infantry: 7
            - Machine Gun: 1
          - Portugal:
            - Special Forces: 1
          - Greece:
            - Artillery: 1
        - Neighbors:
          - -3925
          - 3925
          - 1061
          - 1066
        
        ## Enemy Land Zone 3925
        - ZoneValue: 384
        - Dominance: Even
        - Posture: Attrition
        - EnemyStrength: 1093
        - FriendlyStrength: 854
        - City: Pharsalos
        - AreaID: 38
        - Plots: 8
        - CenterX: 3
        - CenterY: 45
        - Units:
          - Greece:
            - Anti-Aircraft Gun: 1
            - Infantry: 1
        - Neighbors:
          - -3925
          - -2492
          - 1061
          - 2729
        
        ## Friendly Land Zone 4753
        - ZoneValue: 42
        - Dominance: Friendly
        - FriendlyStrength: 2227
        - City: Osaka
        - AreaID: 38
        - Plots: 20
        - CenterX: 22
        - CenterY: 30
        - Units:
          - Portugal:
            - Heavy Bomber: 1
            - Artillery: 1
            - Bomber: 1
        - Neighbors:
          - 5762
          - 1507
          - 1251
          - 10327
          - -10327
        
        ## Friendly Land Zone 5304
        - ZoneValue: 42
        - Dominance: Friendly
        - NeutralStrength: 191
        - FriendlyStrength: 6617
        - City: Coimbra
        - AreaID: 38
        - Plots: 23
        - CenterX: 15
        - CenterY: 40
        - Units:
          - Portugal:
            - Heavy Bomber: 3
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - 17171
          - 1065
          - 10689
          - 1062
          - 1067
        
        ## Neutral Land Zone 5411
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 73
        - FriendlyStrength: 2614
        - City: Carchemish
        - AreaID: 89
        - Plots: 11
        - CenterX: 68
        - CenterY: 44
        - Units:
          - City-State Copenhagen:
            - Machine Gun: 1
        - Neighbors:
          - 11111
        
        ## Friendly Land Zone 5762
        - ZoneValue: 48
        - Dominance: Friendly
        - FriendlyStrength: 2091
        - City: Kyoto
        - AreaID: 38
        - Plots: 24
        - CenterX: 17
        - CenterY: 28
        - Units:
          - Portugal:
            - Heavy Bomber: 1
            - Machine Gun: 1
        - Neighbors:
          - 11219
          - 16568
          - 1507
          - 7664
          - 4753
        
        ## Friendly Land Zone 6238
        - ZoneValue: 36
        - Dominance: Friendly
        - FriendlyStrength: 2198
        - City: Funchal
        - AreaID: 95
        - Plots: 10
        - CenterX: 25
        - CenterY: 47
        - Units:
          - Portugal:
            - Fighter: 1
            - Special Forces: 2
            - Machine Gun: 1
        
        ## Friendly Land Zone 7664
        - ZoneValue: 42
        - Dominance: Friendly
        - FriendlyStrength: 2468
        - City: Tokyo
        - AreaID: 31
        - Plots: 14
        - CenterX: 18
        - CenterY: 23
        - Units:
          - Portugal:
            - Artillery: 1
            - Machine Gun: 1
        - Neighbors:
          - 11219
          - 8163
          - 5762
        
        ## Friendly Land Zone 8163
        - ZoneValue: 36
        - Dominance: Friendly
        - FriendlyStrength: 2361
        - City: Satsuma
        - AreaID: 31
        - Plots: 23
        - CenterX: 18
        - CenterY: 18
        - Units:
          - Portugal:
            - Heavy Bomber: 1
            - Bomber: 1
            - Machine Gun: 2
        - Neighbors:
          - 14084
          - 11219
          - 7664
          - -8163
        
        ## Enemy Land Zone 8359
        - ZoneValue: 96
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 307
        - FriendlyStrength: 2134
        - City: Ephesus
        - AreaID: 32
        - Plots: 9
        - CenterX: 69
        - CenterY: 17
        - Units:
          - Greece:
            - Machine Gun: 1
        - Neighbors:
          - -8359
          - 10499
        
        ## Neutral Land Zone 8610
        - ZoneValue: 12
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 182
        - NeutralStrength: 83
        - FriendlyStrength: 1809
        - City: Zutphen
        - AreaID: 5
        - Plots: 14
        - CenterX: 68
        - CenterY: 10
        - Units:
          - The Netherlands:
            - Infantry: 3
            - Triplane: 2
            - Machine Gun: 1
        - Neighbors:
          - -8610
          - -8359
          - 10499
          - 12185
          - -10499
        
        ## Friendly Land Zone 9293
        - ZoneValue: 30
        - Dominance: Friendly
        - FriendlyStrength: 2999
        - City: Nara
        - AreaID: 20
        - Plots: 8
        - CenterX: 15
        - CenterY: 13
        - Units:
          - Portugal:
            - Machine Gun: 1
        - Neighbors:
          - -14084
          - -1073
          - 1073
        
        ## Enemy Land Zone 9512
        - ZoneValue: 48
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 547
        - FriendlyStrength: 719
        - City: Axum
        - AreaID: 58
        - Plots: 13
        - CenterX: 78
        - CenterY: 32
        - Units:
          - Barbarians:
            - Infantry: 1
        - Neighbors:
          - -9512
          - 11075
        
        ## Friendly Land Zone 10327
        - ZoneValue: 30
        - Dominance: Friendly
        - FriendlyStrength: 2104
        - City: Ouagadougou
        - AreaID: 53
        - Plots: 5
        - CenterX: 25
        - CenterY: 25
        - Units:
          - Portugal:
            - Fighter: 1
            - Machine Gun: 1
        - Neighbors:
          - -10327
          - 4753
        
        ## Enemy Land Zone 10499
        - ZoneValue: 5760
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 203
        - FriendlyStrength: 1960
        - AreaID: 5
        - Plots: 10
        - CenterX: 70
        - CenterY: 14
        - Units:
          - Portugal:
            - Artillery: 1
            - Anti-Aircraft Gun: 1
            - Fleet Destroyer: 1
        - Neighbors:
          - 8610
          - -8359
          - 8359
          - -10499
        
        ## Friendly Land Zone 10689
        - ZoneValue: 36
        - Dominance: Friendly
        - NeutralStrength: 146
        - FriendlyStrength: 3394
        - City: Novgorod
        - AreaID: 38
        - Plots: 26
        - CenterX: 16
        - CenterY: 36
        - Units:
          - Portugal:
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - 17171
          - 16568
          - 5304
          - 1507
          - 1062
        
        ## Enemy Land Zone 11075
        - ZoneValue: 192
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 607
        - FriendlyStrength: 1012
        - City: Leiria
        - AreaID: 64
        - Plots: 17
        - CenterX: 76
        - CenterY: 37
        - Units:
          - City-State Cape Town:
            - Infantry: 1
        - Neighbors:
          - 9512
        
        ## Neutral Land Zone 11111
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 54
        - FriendlyStrength: 3809
        - City: Lyon
        - AreaID: 66
        - Plots: 21
        - CenterX: 65
        - CenterY: 47
        - Units:
          - France:
            - Rifleman: 1
        - Neighbors:
          - 5411
          - 1071
        
        ## Friendly Land Zone 11219
        - ZoneValue: 3
        - Dominance: Friendly
        - FriendlyStrength: 1692
        - City: Nagoya
        - AreaID: 40
        - Plots: 23
        - CenterX: 14
        - CenterY: 23
        - Units:
          - Portugal:
            - Machine Gun: 1
        - Neighbors:
          - 14084
          - 8163
          - 7664
          - 5762
        
        ## Neutral Land Zone 12185
        - ZoneValue: 9
        - Dominance: Friendly
        - NeutralStrength: 55
        - FriendlyStrength: 1061
        - City: Bahir Dar
        - AreaID: 5
        - Plots: 19
        - CenterX: 71
        - CenterY: 4
        - Units:
          - Ethiopia:
            - Lancer: 1
        - Neighbors:
          - 8610
        
        ## Friendly Land Zone 12532
        - ZoneValue: 30
        - Dominance: Friendly
        - FriendlyStrength: 3732
        - City: Lalibela
        - AreaID: 13
        - Plots: 8
        - CenterX: 9
        - CenterY: 13
        - Units:
          - City-State Shanghai:
            - Infantry: 1
          - Portugal:
            - Artillery: 1
            - Special Forces: 1
        - Neighbors:
          - 1074
          - 14648
          - -14648
        
        ## Friendly Land Zone 13401
        - ZoneValue: 3
        - Dominance: Friendly
        - FriendlyStrength: 2336
        - City: Izumo
        - AreaID: 1
        - Plots: 14
        - CenterX: 22
        - CenterY: 6
        - Units:
          - Barbarians:
            - Machine Gun: 1
          - Portugal:
            - Tank: 1
            - Anti-Aircraft Gun: 1
            - Machine Gun: 3
        - Neighbors:
          - -13821
        
        ## Friendly Land Zone 13821
        - ZoneValue: 30
        - Dominance: Friendly
        - FriendlyStrength: 2941
        - City: Gondar
        - AreaID: 9
        - Plots: 11
        - CenterX: 17
        - CenterY: 6
        - Units:
          - Portugal:
            - Light Tank: 1
        - Neighbors:
          - -1073
          - -13821
        
        ## Friendly Land Zone 14084
        - ZoneValue: 36
        - Dominance: Friendly
        - FriendlyStrength: 2934
        - City: Harar
        - AreaID: 38
        - Plots: 22
        - CenterX: 10
        - CenterY: 21
        - Units:
          - Portugal:
            - Anti-Aircraft Gun: 1
            - Machine Gun: 1
        - Neighbors:
          - 14565
          - -1074
          - -14084
          - 14846
          - 11219
          - 8163
        
        ## Friendly Land Zone 14565
        - ZoneValue: 36
        - Dominance: Friendly
        - FriendlyStrength: 1953
        - City: Adwa
        - AreaID: 43
        - Plots: 16
        - CenterX: 6
        - CenterY: 22
        - Units:
          - Portugal:
            - Machine Gun: 1
        - Neighbors:
          - 14846
          - 14084
        
        ## Friendly Land Zone 14648
        - ZoneValue: 3
        - Dominance: Friendly
        - FriendlyStrength: 2955
        - City: Zanzibar
        - AreaID: 13
        - Plots: 14
        - CenterX: 9
        - CenterY: 9
        - Units:
          - Portugal:
            - Anti-Aircraft Gun: 1
            - Special Forces: 1
            - Machine Gun: 1
        - Neighbors:
          - -14648
          - 12532
          - 1073
          - -1073
        
        ## Friendly Land Zone 14846
        - ZoneValue: 36
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 159
        - FriendlyStrength: 3057
        - City: Addis Ababa
        - AreaID: 38
        - Plots: 34
        - CenterX: 8
        - CenterY: 27
        - Units:
          - Portugal:
            - Fighter: 1
            - Special Forces: 1
            - Triplane: 1
            - Machine Gun: 1
        - Neighbors:
          - 14565
          - -1064
          - 1064
          - 16568
          - 14084
        
        ## Friendly Land Zone 15642
        - ZoneValue: 30
        - Dominance: Friendly
        - FriendlyStrength: 1077
        - City: Eretria
        - AreaID: 41
        - Plots: 7
        - CenterX: 76
        - CenterY: 20
        - Units:
          - Portugal:
            - Machine Gun: 1
        - Neighbors:
          - -15642
          - -17174
          - 17174
        
        ## Friendly Land Zone 16568
        - ZoneValue: 36
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 159
        - FriendlyStrength: 6779
        - City: Corinth
        - AreaID: 38
        - Plots: 34
        - CenterX: 11
        - CenterY: 33
        - Units:
          - Portugal:
            - Fighter: 2
            - Anti-Aircraft Gun: 1
            - Machine Gun: 2
        - Neighbors:
          - 1064
          - 14846
          - 17171
          - 10689
          - 5762
          - 1507
        
        ## Friendly Land Zone 17171
        - ZoneValue: 18
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 558
        - NeutralStrength: 191
        - FriendlyStrength: 8726
        - City: Sparta
        - AreaID: 38
        - Plots: 31
        - CenterX: 9
        - CenterY: 38
        - Units:
          - Portugal:
            - Fighter: 2
            - Tank: 1
            - Artillery: 1
            - Anti-Aircraft Gun: 6
            - Machine Gun: 3
        - Neighbors:
          - 2492
          - 1064
          - 1061
          - 16568
          - 1065
          - 5304
          - 10689
        
        ## Friendly Land Zone 17174
        - ZoneValue: 6
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 182
        - FriendlyStrength: 1937
        - City: Halicarnassus
        - AreaID: 48
        - Plots: 8
        - CenterX: 74
        - CenterY: 22
        - Units:
          - Portugal:
            - Machine Gun: 2
        - Neighbors:
          - -17174
          - 15642
          - -15642
        
        ## Friendly Sea Zone -1062
        - ZoneValue: 18
        - Dominance: Friendly
        - FriendlyStrength: 4507
        - City: Lisbon
        - AreaID: 0
        - Plots: 19
        - CenterX: 22
        - CenterY: 42
        - Units:
          - Portugal:
            - Battleship: 3
            - Tank: 1
            - Infantry: 1
            - Machine Gun: 1
            - Fleet Destroyer: 5
        - Neighbors:
          - 1062
          - -1067
          - 1251
        
        ## Neutral Sea Zone -1840
        - ZoneValue: 12
        - Dominance: Friendly
        - NeutralStrength: 650
        - FriendlyStrength: 2506
        - City: Chichen Itza
        - AreaID: 0
        - Plots: 30
        - CenterX: 31
        - CenterY: 30
        - Units:
          - The Netherlands:
            - Tank: 1
            - Dreadnought: 2
        - Neighbors:
          - -10327
          - 1840
        
        ## Enemy Sea Zone -2492
        - ZoneValue: 512
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 475
        - FriendlyStrength: 2706
        - City: Knossos
        - AreaID: 0
        - Plots: 13
        - CenterX: 2
        - CenterY: 40
        - Units:
          - Portugal:
            - Paratrooper: 1
            - Fleet Destroyer: 1
          - France:
            - Cruiser: 1
        - Neighbors:
          - -3925
          - -1064
          - 2492
          - 3925
        
        ## Neutral Sea Zone -8610
        - ZoneValue: 4
        - Dominance: Friendly
        - Posture: Exploit Flanks
        - EnemyStrength: 121
        - NeutralStrength: 83
        - FriendlyStrength: 2133
        - City: Zutphen
        - AreaID: 0
        - Plots: 24
        - CenterX: 65
        - CenterY: 11
        - Units:
          - The Netherlands:
            - Infantry: 1
        - Neighbors:
          - 8610
          - -8359
          - -10499
        
        ## Enemy Sea Zone -8359
        - ZoneValue: 384
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 246
        - FriendlyStrength: 4061
        - City: Ephesus
        - AreaID: 0
        - Plots: 48
        - CenterX: 67
        - CenterY: 18
        - Units:
          - The Netherlands:
            - Fleet Destroyer: 1
          - Portugal:
            - Battleship: 2
            - Fleet Destroyer: 4
        - Neighbors:
          - -8610
          - 8359
          - 8610
          - 10499
          - -17174
          - -10499
        
        ## Friendly Sea Zone -13821
        - ZoneValue: 10
        - Dominance: Friendly
        - FriendlyStrength: 2064
        - City: Gondar
        - AreaID: 0
        - Plots: 31
        - CenterX: 17
        - CenterY: 4
        - Units:
          - City-State Marrakech:
            - Fleet Destroyer: 1
          - Portugal:
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - -1073
          - 1073
          - 13821
          - 13401
        
        ## Neutral Sea Zone -2726
        - ZoneValue: 6
        - Dominance: Friendly
        - NeutralStrength: 529
        - FriendlyStrength: 1382
        - City: Tulum
        - AreaID: 82
        - Plots: 7
        - CenterX: 40
        - CenterY: 41
        - Units:
          - The Netherlands:
            - Tank: 1
        - Neighbors:
          - -1069
        
        ## Friendly Sea Zone -14084
        - ZoneValue: 12
        - Dominance: Friendly
        - FriendlyStrength: 1486
        - City: Harar
        - AreaID: 0
        - Plots: 13
        - CenterX: 12
        - CenterY: 19
        - Units:
          - Portugal:
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - 14084
          - 9293
        
        ## Friendly Sea Zone -8163
        - ZoneValue: 1
        - Dominance: Friendly
        - FriendlyStrength: 1639
        - City: Satsuma
        - AreaID: 0
        - Plots: 13
        - CenterX: 21
        - CenterY: 19
        - Units:
          - Portugal:
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - 8163
          - -1075
          - 1075
        
        ## Friendly Sea Zone -17174
        - ZoneValue: 2
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 121
        - FriendlyStrength: 2630
        - City: Halicarnassus
        - AreaID: 0
        - Plots: 40
        - CenterX: 73
        - CenterY: 22
        - Units:
          - Portugal:
            - Fleet Destroyer: 1
        - Neighbors:
          - -8359
          - 17174
          - -10499
          - -15642
          - 15642
        
        ## Neutral Sea Zone -1074
        - ZoneValue: 8
        - Dominance: Friendly
        - NeutralStrength: 96
        - FriendlyStrength: 1517
        - City: Shanghai
        - AreaID: 0
        - Plots: 36
        - CenterX: 4
        - CenterY: 15
        - Units:
          - Portugal:
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - -15642
          - -14648
          - 1074
          - 14084
        
        ## Neutral Sea Zone -1067
        - ZoneValue: 16
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 142
        - NeutralStrength: 94
        - FriendlyStrength: 2556
        - City: Raqmu
        - AreaID: 0
        - Plots: 32
        - CenterX: 19
        - CenterY: 49
        - Units:
          - City-State Raqmu:
            - Battleship: 1
            - Fleet Destroyer: 2
        - Neighbors:
          - 1067
          - 1062
          - -1062
        
        ## Enemy Sea Zone -3925
        - ZoneValue: 128
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 297
        - FriendlyStrength: 523
        - City: Pharsalos
        - AreaID: 0
        - Plots: 38
        - CenterX: 79
        - CenterY: 46
        - Units:
          - Greece:
            - Submarine: 1
        - Neighbors:
          - 3925
          - -2492
          - 2729
        
        ## Friendly Sea Zone -15642
        - ZoneValue: 10
        - Dominance: Friendly
        - FriendlyStrength: 1514
        - City: Eretria
        - AreaID: 0
        - Plots: 44
        - CenterX: 78
        - CenterY: 18
        - Units:
          - Portugal:
            - Infantry: 1
        - Neighbors:
          - -1074
          - -17174
          - -10499
          - 15642
          - 17174
        
        ## Enemy Sea Zone -1064
        - ZoneValue: 32
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 898
        - FriendlyStrength: 3550
        - City: Cape Town
        - AreaID: 0
        - Plots: 21
        - CenterX: 3
        - CenterY: 33
        - Units:
          - City-State Cape Town:
            - Fleet Destroyer: 1
        - Neighbors:
          - -9512
          - -2492
          - 1064
          - 14846
        
        ## Neutral Sea Zone -1069
        - ZoneValue: 4
        - Dominance: Friendly
        - NeutralStrength: 303
        - FriendlyStrength: 1124
        - City: Enns
        - AreaID: 83
        - Plots: 16
        - CenterX: 44
        - CenterY: 42
        - Units:
          - City-State Enns:
            - Fleet Destroyer: 1
        - Neighbors:
          - -2726
        
        ## Neutral Sea Zone -1075
        - ZoneValue: 8
        - Dominance: Friendly
        - NeutralStrength: 99
        - FriendlyStrength: 1352
        - City: Panama City
        - AreaID: 0
        - Plots: 66
        - CenterX: 25
        - CenterY: 16
        - Units:
          - City-State Panama City:
            - Fleet Destroyer: 2
          - Portugal:
            - Battleship: 2
            - Anti-Aircraft Gun: 1
            - Fleet Destroyer: 1
        - Neighbors:
          - -8163
          - 1075
          - -10327
        
        ## Neutral Sea Zone -1073
        - ZoneValue: 8
        - Dominance: Friendly
        - NeutralStrength: 96
        - FriendlyStrength: 2128
        - City: Marrakech
        - AreaID: 0
        - Plots: 25
        - CenterX: 13
        - CenterY: 6
        - Units:
          - City-State Marrakech:
            - Battleship: 1
            - Fleet Destroyer: 1
        - Neighbors:
          - -14648
          - 14648
          - 1073
          - -13821
          - 13821
          - 9293
        
        ## Friendly Sea Zone -10327
        - ZoneValue: 10
        - Dominance: Friendly
        - FriendlyStrength: 3579
        - City: Ouagadougou
        - AreaID: 0
        - Plots: 59
        - CenterX: 26
        - CenterY: 26
        - Units:
          - Portugal:
            - Destroyer: 1
            - Machine Gun: 1
            - Fleet Destroyer: 4
        - Neighbors:
          - 1075
          - 10327
          - -1075
          - 4753
          - -1840
        
        ## Friendly Sea Zone -14648
        - ZoneValue: 10
        - Dominance: Friendly
        - FriendlyStrength: 1865
        - City: Zanzibar
        - AreaID: 0
        - Plots: 40
        - CenterX: 6
        - CenterY: 8
        - Units:
          - Portugal:
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - -1074
          - 14648
          - 1074
          - 1073
          - 12532
          - -1073
        
        ## Enemy Sea Zone -9512
        - ZoneValue: 4
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 931
        - FriendlyStrength: 321
        - City: Axum
        - AreaID: 0
        - Plots: 35
        - CenterX: 0
        - CenterY: 29
        - Units:
          - City-State Cape Town:
            - Fleet Destroyer: 3
        - Neighbors:
          - 9512
          - -1064
        
        ## Enemy Sea Zone -10499
        - ZoneValue: 1920
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 142
        - FriendlyStrength: 3322
        - AreaID: 0
        - Plots: 32
        - CenterX: 73
        - CenterY: 13
        - Units:
          - Portugal:
            - Battleship: 1
            - Destroyer: 1
            - Fleet Destroyer: 5
        - Neighbors:
          - 8610
          - 10499
          - -8610
          - -8359
          - -17174
          - -15642
        
        # Events
        Events: events since you last made a decision.
        
        ## Turn 408
        
        ### 0
        - Type: TileOwnershipChanged
        - NewOwner: 22
        - Ocean 3,34:
          - Owner: City-State Cape Town
        
        ### 1
        - Type: CityBoughtPlot
        - WithFaithCulture: true
        - City:
          - Name: Cape Town
          - Population: 19
          - ID: 1064
        - Player: 22
        - Ocean 3,34:
          - Owner: City-State Cape Town
        
        ### 2
        - Type: UnitPromoted
        - Unit:
          - Level: 6
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16431
        - Player: 22
        - Promotion: Barrage III
        
        ### 3
        - Type: CombatResult
        - Plains Hills 5,37:
          - Owner: Greece
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 29
          - Damage: 90
          - Unit:
            - Level: 1
            - Health: 39%
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 17195
          - Player: 63: Barbarians
        
        ### 4
        - Type: CombatResult
        - Coast 4,34:
          - Owner: City-State Cape Town
          - Resource: Fish
          - Improvement: Fishing Boats
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 30
          - Damage: 30
          - Unit:
            - Level: 3
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 16726
          - Player: 6: Portugal
        
        ### 5
        - Type: CombatResult
        - Grass Land 0,32:
          - Owner: City-State Cape Town
          - Resource: Iron
          - Improvement: Mine
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 19
          - Damage: 50
          - Unit:
            - Level: 3
            - Health: 74%
            - AI: Defense
            - Unit: Rifleman
            - ID: 16348
          - Player: 2: France
        
        ### 6
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 35%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16801
        - Player: 22
        - Coast 0,31:
          - Owner: City-State Cape Town
        
        ### 7
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16847
        - Player: 22
        
        ### 8
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16802
        - Player: 22
        
        ### 9
        - Type: CombatResult
        - Coast 1,28:
          - Resource: Fish
        - Attacker:
          - RemainingHP: 29
          - Damage: 29
        - Defender:
          - RemainingHP: 30
          - Damage: 75
          - Unit:
            - Level: 4
            - Health: 67%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 16796
          - Player: 6: Portugal
        
        ### 10
        - Type: CombatResult
        - Coast 1,28:
          - Resource: Fish
        - Attacker:
          - RemainingHP: 27
          - Damage: 27
        - Defender:
          - RemainingHP: 36
          - Damage: 111
          - Unit:
            - Level: 4
            - Health: 46%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 16796
          - Player: 6: Portugal
        
        ### 11
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 35%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16801
        - Player: 22
        - Plots:
          - Coast 2,32:
            - Owner: City-State Cape Town
          - Ocean 3,33:
            - Owner: City-State Cape Town
        
        ### 12
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 66%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17118
        - Player: 22
        
        ### 13
        - Type: CombatResult
        - Coast 1,28:
          - Resource: Fish
        - Attacker:
          - RemainingHP: 20
          - Damage: 67
        - Defender:
          - RemainingHP: 37
          - Damage: 148
          - Unit:
            - Level: 4
            - Health: 20%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 16796
          - Player: 6: Portugal
        
        ### 14
        - Type: UnitKilledInCombat
        - KilledPlayer: 6: Portugal
        - KillerPlayer: 22
        - KilledUnit: Fleet Destroyer
        
        ### 15
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 52%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17118
        - Player: 22
        - Coast 1,28:
          - Resource: Fish
        
        ### 16
        - Type: UnitBuildCompleted
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1349
        - Owner: 23
        - Build: Construct a Railroad
        - Snow Hills 14,44:
          - Owner: City-State Wanggeom
          - Improvement: Mine
        
        ### 17
        - Type: CombatResult
        - Tundra Land 10,45:
          - Owner: Greece
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 28
          - Damage: 28
          - Unit:
            - Level: 3
            - AI: Ranged
            - Unit: Machine Gun
            - ID: 13892
          - Player: 6: Portugal
        
        ### 18
        - Type: UnitBuildCompleted
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1136
        - Owner: 24
        - Build: Construct a Farm
        - Tundra Land 14,49:
          - Owner: City-State Winchester
          - IsRiver: true
        
        ### 19
        - Type: PlayerRevoked
        - PledgeNowBroken: true
        - MajorPlayer: 6: Portugal
        - MinorPlayer: 26
        
        ### 20
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14688
        - Player: 29
        - Plots:
          - Tundra Land 69,48:
            - Owner: City-State Copenhagen
            - Improvement: Feitoria
            - Route: Railroad
            - Feature: Forest
          - Tundra Land 68,47:
            - Owner: City-State Copenhagen
            - Improvement: Village
            - Route: Railroad
          - Tundra Hills 69,46:
            - Owner: City-State Copenhagen
            - Improvement: Mine
        
        ### 21
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 78%
          - AI: AssaultSea
          - Unit: Battleship
          - ID: 17255
        - Player: 32
        - Plots:
          - Ocean 5,17:
            - Owner: City-State Shanghai
          - Coast 6,16:
            - Owner: City-State Shanghai
            - Resource: Fish
            - Improvement: Fishing Boats
          - Desert Land 6,15:
            - Owner: City-State Shanghai
            - CityID: 1074
            - Population: 24
            - City: Shanghai
            - Route: Railroad
        
        ### 22
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 15765
        - Player: 32
        - Plots:
          - Grass Land 9,14:
            - Owner: Portugal
            - Improvement: Town
            - Route: Railroad
          - Desert Hills 8,13:
            - Owner: Portugal
            - Improvement: Monolithic Church
            - Route: Railroad
          - Desert Hills 8,14:
            - Owner: City-State Shanghai
            - Improvement: Mine
        
        ### 23
        - Type: CombatResult
        - Tundra Hills 5,39:
          - Owner: Greece
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 42
          - Damage: 106
        - Defender:
          - RemainingHP: 18
          - Damage: 18
          - Player: 6: Portugal
          - Unit:
            - Level: 4
            - AI: Counter
            - Unit: Anti-Aircraft Gun
            - ID: 16297
        
        ### 24
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: FastAttack
          - Unit: Machine Gun
          - ID: 17198
        - Player: 63: Barbarians
        - Plains Land 3,39:
          - Owner: Greece
          - Resource: Maize
          - Improvement: Academy
        
        ### 25
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: FastAttack
          - Unit: Machine Gun
          - ID: 17190
        - Player: 63: Barbarians
        - Grass Land 4,38:
          - Owner: Greece
          - Resource: Bison
          - Improvement: Camp
        
        ### 26
        - Type: CombatResult
        - Tundra Hills 5,39:
          - Owner: Greece
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 25
          - Damage: 43
          - Player: 6: Portugal
          - Unit:
            - Level: 4
            - Health: 82%
            - AI: Counter
            - Unit: Anti-Aircraft Gun
            - ID: 16297
        
        ### 27
        - Type: CombatResult
        - Tundra Hills 5,39:
          - Owner: Greece
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 24
          - Damage: 67
          - Player: 6: Portugal
          - Unit:
            - Level: 4
            - Health: 56%
            - AI: Counter
            - Unit: Anti-Aircraft Gun
            - ID: 16297
        
        ### 28
        - Type: CombatResult
        - Ocean 2,41:
          - Owner: Greece
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 12
          - Damage: 12
          - Player: 2: France
          - Unit:
            - Level: 4
            - AI: AssaultSea
            - Unit: Cruiser
            - ID: 15821
        
        ### 29
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 42%
          - AI: FastAttack
          - Unit: Infantry
          - ID: 16790
        - Player: 63: Barbarians
        - Tundra Land 9,48:
          - Owner: Greece
          - IsRiver: true
          - Resource: Iron
          - Improvement: Mine
        
        ### 30
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 5: Greece
        - OldImprovement: Mine
        - NewImprovement: Mine
        - Plains Hills 5,37:
          - Owner: Greece
          - Improvement: Mine
        
        ### 31
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 35%
          - AI: FastAttack
          - Unit: Machine Gun
          - ID: 17195
        - Player: 63: Barbarians
        - Desert Hills 5,36:
          - Owner: City-State Cape Town
          - Improvement: Mine
        
        ## Turn 409
        
        ### 0
        - Type: CityConvertsReligion
        - City:
          - Owner: Portugal
          - CityID: 4753
          - Population: 26
          - IsRiver: true
          - City: Osaka
          - Terrain: Plains
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Hills
          - X: 22
          - Y: 30
        - Owner: 6: Portugal
        - Religion: Buddhism
        
        ### 1
        - Type: EspionageState
        - SpyIndex: 7
        - SpyState: 3
        - City:
          - Owner: Greece
          - CityID: 8359
          - Population: 18
          - City: Ephesus
          - Terrain: Grass
          - Resource: Iron
          - Route: Railroad
          - Plot: Land
          - X: 68
          - Y: 17
        - SpyOwner: 1: The Netherlands
        
        ### 2
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16904
        - Player: 1: The Netherlands
        - Grass Land 38,29:
          - Owner: The Maya
          - Resource: Cattle
          - Improvement: Pasture
        
        ### 3
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16809
        - Player: 1: The Netherlands
        
        ### 4
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17126
        - Player: 1: The Netherlands
        - Plots:
          - Plains Hills 34,31:
            - Owner: The Maya
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 35,31:
            - Owner: The Maya
            - Improvement: Mine
            - Route: Railroad
        
        ### 5
        - Type: CombatResult
        - Plains Land 71,13:
          - Owner: Greece
          - CityID: 10499
          - Population: 16
          - City: Rhodes
          - Resource: Uranium
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 24
          - Damage: 24
        - Defender:
          - RemainingHP: 29
          - Damage: 341
          - Player: 5: Greece
        
        ### 6
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 68%
          - AI: CityBombard
          - Unit: Artillery
          - ID: 15255
        - Player: 1: The Netherlands
        - Desert Hills 69,12:
          - Owner: Greece
          - Resource: Sheep
          - Improvement: Pasture
          - Route: Road
        
        ### 7
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 69%
          - AI: Defense
          - Unit: Infantry
          - ID: 15594
        - Player: 1: The Netherlands
        - Grass Land 72,14:
          - Owner: Greece
          - Resource: Bananas
          - Improvement: Plantation
        
        ### 8
        - Type: CombatResult
        - Plains Land 71,13:
          - Owner: Greece
          - CityID: 10499
          - Population: 16
          - City: Rhodes
          - Resource: Uranium
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 12
          - Damage: 12
        - Defender:
          - RemainingHP: 36
          - Damage: 377
          - Player: 5: Greece
        
        ### 9
        - Type: CombatResult
        - Plains Land 71,13:
          - Owner: Greece
          - CityID: 10499
          - Population: 16
          - City: Rhodes
          - Resource: Uranium
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 16
          - Damage: 54
        - Defender:
          - RemainingHP: 36
          - Damage: 413
          - Player: 5: Greece
        
        ### 10
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 38%
          - AI: Defense
          - Unit: Infantry
          - ID: 15912
        - Player: 1: The Netherlands
        - Plots:
          - Plains Hills 70,14:
            - Owner: Greece
            - Improvement: Mine
            - Route: Road
          - Plains Hills 69,13:
            - Owner: Greece
            - Improvement: Citadel
            - Route: Railroad
        
        ### 11
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 15459
        - Player: 1: The Netherlands
        
        ### 12
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 17188
        - Player: 1: The Netherlands
        - Plots:
          - Desert Land 67,44:
            - Owner: France
            - Improvement: Village
            - Route: Road
          - Plains Land 67,45:
            - Owner: City-State Copenhagen
            - Improvement: Farm
          - Plains Land 68,46:
            - Owner: City-State Copenhagen
            - Improvement: Farm
            - Route: Railroad
          - Tundra Land 68,47:
            - Owner: City-State Copenhagen
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 69,48:
            - Owner: City-State Copenhagen
            - Improvement: Feitoria
            - Route: Railroad
            - Feature: Forest
          - Tundra Hills 70,48:
            - Owner: City-State Copenhagen
            - Resource: Sheep
            - Improvement: Embassy
            - Route: Railroad
        
        ### 13
        - Type: SetAlly
        - NewAllyPlayer: 1: The Netherlands
        - OldAllyPlayer: 6: Portugal
        - MinorPlayer: 29
        
        ### 14
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: FastAttack
          - Unit: Tank
          - ID: 15722
        - Player: 1: The Netherlands
        - Plots:
          - Coast 37,42:
            - Owner: City-State Cahokia
          - Coast 38,42:
            - Owner: The Maya
          - Coast 39,42:
            - Owner: The Maya
        
        ### 15
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16818
        - Player: 2: France
        - Plots:
          - Plains Hills 68,43:
            - Owner: City-State Copenhagen
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 67,43:
            - Owner: France
            - Resource: Coal
            - Improvement: Academy
        
        ### 16
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16102
        - Player: 2: France
        - Plots:
          - Tundra Land 70,49:
            - Owner: City-State Copenhagen
            - CityID: 1071
            - Population: 23
            - City: Copenhagen
            - Route: Railroad
          - Tundra Hills 70,48:
            - Owner: City-State Copenhagen
            - Resource: Sheep
            - Improvement: Embassy
            - Route: Railroad
          - Tundra Land 69,48:
            - Owner: City-State Copenhagen
            - Improvement: Feitoria
            - Route: Railroad
            - Feature: Forest
          - Tundra Land 68,47:
            - Owner: City-State Copenhagen
            - Improvement: Village
            - Route: Railroad
          - Tundra Hills 67,47:
            - Owner: France
            - Resource: Jade
            - Improvement: Quarry
            - Route: Road
        
        ### 17
        - Type: CombatResult
        - Plains Land 4,42:
          - Owner: Greece
          - Improvement: Farm
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 44
          - Damage: 76
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 68%
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 17196
        
        ### 18
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 42%
          - AI: AssaultSea
          - Unit: Cruiser
          - ID: 15781
        - Player: 2: France
        - Ocean 2,42:
          - Owner: Greece
        
        ### 19
        - Type: CombatResult
        - Plains Land 4,42:
          - Owner: Greece
          - Improvement: Farm
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 24
          - Damage: 100
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 24%
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 17196
        
        ### 20
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 72%
          - AI: AssaultSea
          - Unit: Cruiser
          - ID: 15871
        - Player: 2: France
        
        ### 21
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 17263
        - Player: 2: France
        - Plots:
          - Coast 71,50:
            - Owner: City-State Copenhagen
          - Coast 71,49:
            - Owner: City-State Copenhagen
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 72,48:
            - Owner: City-State Copenhagen
          - Ocean 72,47:
            - Owner: City-State Copenhagen
        
        ### 22
        - Type: EspionageState
        - SpyIndex: 1
        - SpyState: 3
        - City:
          - Owner: Portugal
          - CityID: 1251
          - Population: 28
          - City: Porto
          - Terrain: Grass
          - Resource: Bison
          - Religion: Catholicism
          - Route: Railroad
          - Plot: Land
          - X: 23
          - Y: 35
        - SpyOwner: 3: The Maya
        
        ### 23
        - Type: EspionageState
        - SpyIndex: 3
        - SpyState: 4
        - City:
          - Owner: City-State Shanghai
          - CityID: 1074
          - Population: 24
          - City: Shanghai
          - Terrain: Desert
          - Route: Railroad
          - Plot: Land
          - X: 6
          - Y: 15
        - SpyOwner: 3: The Maya
        
        ### 24
        - Type: EspionageState
        - SpyIndex: 6
        - SpyState: 3
        - City:
          - Owner: Portugal
          - CityID: 1507
          - Population: 23
          - City: Braga
          - Terrain: Grass
          - Religion: Catholicism
          - Route: Railroad
          - Plot: Hills
          - X: 18
          - Y: 33
        - SpyOwner: 3: The Maya
        
        ### 25
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16140
        - Player: 3: The Maya
        - Plains Hills 39,34:
          - Owner: The Maya
          - Resource: Aluminum
          - Improvement: Mine
          - Route: Railroad
        
        ### 26
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16593
        - Player: 3: The Maya
        - Plots:
          - Plains Land 37,31:
            - Owner: The Maya
            - IsRiver: true
            - Improvement: Academy
          - Plains Land 38,30:
            - Owner: The Maya
            - Resource: Horses
            - Improvement: Holy Site
          - Grass Land 38,29:
            - Owner: The Maya
            - Resource: Cattle
            - Improvement: Pasture
        
        ### 27
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16409
        - Player: 3: The Maya
        - Plains Hills 37,35:
          - Owner: The Maya
          - Improvement: Village
          - Route: Railroad
        
        ### 28
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16977
        - Player: 3: The Maya
        - Plots:
          - Plains Land 37,30:
            - Owner: The Maya
            - IsRiver: true
            - Improvement: Kuna
            - Feature: Forest
          - Grass Land 37,29:
            - Owner: The Maya
            - Improvement: Village
        
        ### 29
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16978
        - Player: 3: The Maya
        - Grass Land 38,29:
          - Owner: The Maya
          - Resource: Cattle
          - Improvement: Pasture
        
        ### 30
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16353
        - Player: 3: The Maya
        - Plots:
          - Plains Land 37,31:
            - Owner: The Maya
            - IsRiver: true
            - Improvement: Academy
          - Plains Land 38,30:
            - Owner: The Maya
            - Resource: Horses
            - Improvement: Holy Site
          - Grass Land 38,29:
            - Owner: The Maya
            - Resource: Cattle
            - Improvement: Pasture
        
        ### 31
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16594
        - Player: 3: The Maya
        - Plots:
          - Grass Land 36,33:
            - Owner: The Maya
            - Improvement: Academy
            - Route: Road
          - Plains Land 37,34:
            - Owner: The Maya
            - Improvement: Academy
            - Route: Railroad
          - Plains Hills 37,35:
            - Owner: The Maya
            - Improvement: Village
            - Route: Railroad
        
        ### 32
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16504
        - Player: 3: The Maya
        - Plots:
          - Plains Hills 39,34:
            - Owner: The Maya
            - Resource: Aluminum
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 38,33:
            - Owner: The Maya
            - Improvement: Village
            - Route: Railroad
          - Grass Hills 38,32:
            - Owner: The Maya
            - IsRiver: true
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 37,32:
            - Owner: The Maya
            - CityID: 1059
            - Population: 37
            - IsRiver: true
            - City: Palenque
            - Religion: Buddhism
            - Route: Railroad
        
        ### 33
        - Type: RebaseTo
        - Player: 3: The Maya
        - Unit:
          - Level: 4
          - Health: 77%
          - AI: AttackAir
          - Unit: Bomber
          - ID: 16065
        - Plains Land 41,34:
          - Owner: The Maya
          - CityID: 2024
          - Population: 24
          - IsRiver: true
          - City: Uxmal
          - Religion: Buddhism
          - Route: Railroad
        
        ### 34
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14322
        - Player: 3: The Maya
        - Plains Hills 38,41:
          - Owner: The Maya
          - Resource: Sheep
          - Improvement: Pasture
        
        ### 35
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 15476
        - Player: 3: The Maya
        - Grass Land 39,33:
          - Owner: The Maya
          - Improvement: Lumber Mill
          - Feature: Forest
        
        ### 36
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 15218
        - Player: 3: The Maya
        - Plains Land 38,31:
          - Owner: The Maya
          - Resource: Silk
          - Improvement: Academy
        
        ### 37
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 15219
        - Player: 3: The Maya
        - Plains Hills 34,31:
          - Owner: The Maya
          - Improvement: Mine
          - Route: Railroad
        
        ### 38
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Archaeologist
          - Unit: Archaeologist
          - ID: 16454
        - Player: 3: The Maya
        - Plots:
          - Ocean 29,49:
            - Feature: Ice
          - Ocean 28,49:
            - Feature: Ice
          - Ocean 27,49:
            - Feature: Ice
          - Ocean 27,50:
            - Feature: Ice
        
        ### 39
        - Type: CityConstructed
        - City:
          - Name: Athens
          - Population: 29
          - ID: 1061
        - Owner: 5: Greece
        - Building: School of Philosophy
        
        ### 40
        - Type: CityConstructed
        - City:
          - Name: Pharsalos
          - Population: 19
          - ID: 3925
        - Owner: 5: Greece
        - Building: Printing Press
        
        ### 41
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16605
        - Player: 5: Greece
        - Snow Land 4,49:
          - Owner: Greece
          - CityID: 2729
          - Population: 19
          - IsRiver: true
          - City: Mycenae
          - Resource: Oil
          - Route: Railroad
        
        ### 42
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16515
        - Player: 5: Greece
        - Plots:
          - Coast 3,40:
            - Owner: Greece
            - Resource: Oil
          - Plains Land 4,40:
            - Owner: Greece
            - CityID: 2492
            - Population: 20
            - City: Knossos
            - Religion: Zoroastrianism
            - Route: Railroad
          - Coast 2,39:
            - Owner: Greece
        
        ### 43
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16834
        - Player: 5: Greece
        - Tundra Land 2,45:
          - Owner: Greece
          - Improvement: Lumber Mill
          - Feature: Forest
        
        ### 44
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 27%
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 17354
        - Player: 5: Greece
        - Plains Land 2,46:
          - Owner: Greece
          - CityID: 3925
          - Population: 19
          - City: Pharsalos
          - Religion: Zoroastrianism
          - Route: Railroad
        
        ### 45
        - Type: CombatResult
        - Desert Hills 69,12:
          - Owner: Greece
          - Resource: Sheep
          - Improvement: Pasture
          - Route: Road
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 21
          - Damage: 53
          - Unit:
            - Level: 4
            - Health: 68%
            - AI: CityBombard
            - Unit: Artillery
            - ID: 15255
          - Player: 1: The Netherlands
        
        ### 46
        - Type: CombatResult
        - Plains Land 70,17:
          - Owner: Greece
          - Resource: Bison
          - Improvement: Camp
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 20
          - Damage: 58
          - Unit:
            - Level: 6
            - Health: 62%
            - AI: CityBombard
            - Unit: Artillery
            - ID: 13954
          - Player: 6: Portugal
        
        ### 47
        - Type: CombatResult
        - Plains Land 70,17:
          - Owner: Greece
          - Resource: Bison
          - Improvement: Camp
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 25
          - Damage: 83
          - Player: 6: Portugal
          - Unit:
            - Level: 6
            - Health: 42%
            - AI: CityBombard
            - Unit: Artillery
            - ID: 13954
        
        ### 48
        - Type: CombatResult
        - Coast 2,44:
          - Owner: Greece
          - Resource: Fish
          - Improvement: Fishing Boats
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 28
          - Damage: 56
          - Unit:
            - Level: 5
            - Health: 72%
            - AI: Paradrop
            - Unit: Paratrooper
            - ID: 16301
          - Player: 6: Portugal
        
        ### 49
        - Type: CombatResult
        - Plains Land 3,39:
          - Owner: Greece
          - Resource: Maize
          - Improvement: Academy
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 28
          - Damage: 28
          - Unit:
            - Level: 1
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 17198
          - Player: 63: Barbarians
        
        ### 50
        - Type: CombatResult
        - Tundra Land 6,48:
          - Owner: Greece
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 4
          - Damage: 100
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 4%
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 17308
        
        ### 51
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 96%
          - AI: Defense
          - Unit: Infantry
          - ID: 17254
        - Player: 5: Greece
        - Tundra Land 3,44:
          - Owner: Greece
          - Improvement: Lumber Mill
          - Feature: Forest
        
        ### 52
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 5402
        - Player: 5: Greece
        - Tundra Land 3,44:
          - Owner: Greece
          - Improvement: Lumber Mill
          - Feature: Forest
        
        ### 53
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 68%
          - AI: AssaultSea
          - Unit: Submarine
          - ID: 16603
        - Player: 5: Greece
        - Ocean 1,42:
          - Owner: Greece
        
        ### 54
        - Type: CombatResult
        - Ocean 2,42:
          - Owner: Greece
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 42
          - Damage: 100
          - Player: 2: France
          - Unit:
            - Level: 4
            - Health: 42%
            - AI: AssaultSea
            - Unit: Cruiser
            - ID: 15781
        
        ### 55
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 80%
          - AI: FastAttack
          - Unit: Klepht
          - ID: 13533
        - Player: 5: Greece
        - Plots:
          - Ocean 2,36:
            - Owner: Greece
          - Coast 3,36:
            - Owner: City-State Cape Town
          - Plains Land 4,36:
            - Owner: City-State Cape Town
            - Improvement: Farm
        
        ### 56
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 2352
        - Player: 5: Greece
        - Plots:
          - Tundra Hills 4,41:
            - Owner: Greece
            - Resource: Silver
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 5,42:
            - Owner: Greece
            - Improvement: Village
            - Route: Railroad
          - Tundra Hills 4,43:
            - Owner: Greece
            - Resource: Silver
            - Improvement: Mine
        
        ### 57
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 5: Greece
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 2352
        - Build: Repair an Improvement
        - Tundra Hills 4,43:
          - Owner: Greece
          - Resource: Silver
          - Improvement: Mine
        
        ### 58
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 9732
        - Player: 5: Greece
        - Plots:
          - Tundra Hills 4,41:
            - Owner: Greece
            - Resource: Silver
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 5,42:
            - Owner: Greece
            - Improvement: Village
            - Route: Railroad
          - Tundra Hills 4,43:
            - Owner: Greece
            - Resource: Silver
            - Improvement: Mine
        
        ### 59
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 17405
        - Player: 5: Greece
        - Plains Land 2,46:
          - Owner: Greece
          - CityID: 3925
          - Population: 19
          - City: Pharsalos
          - Religion: Zoroastrianism
          - Route: Railroad
        
        ### 60
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 5: Greece
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17405
        - Plains Land 2,46:
          - Owner: Greece
          - CityID: 3925
          - Population: 19
          - City: Pharsalos
          - Religion: Zoroastrianism
          - Route: Railroad
        
        ### 61
        - Type: PlayerPlunderedTradeRoute
        - PlunderGoldValue: 600
        - Domain: 2
        - DestinationCity:
          - Name: Winchester
          - Population: 10
          - ID: 1066
        - PlunderingPlayer: 63: Barbarians
        - OriginOwner: 5: Greece
        - OriginCity:
          - Name: Pharsalos
          - Population: 19
          - ID: 3925
        - PlunderingUnit:
          - Level: 1
          - AI: FastAttack
          - Unit: Infantry
          - ID: 17310
        - DestinationOwner: 24
        - Connection: Food
        
        ### 62
        - Type: PlayerDoneTurn
        - NextPlayer: 6: Portugal
        - Player: 5: Greece
        
        ### 63
        - Type: CityInvestedBuilding
        - BuildingClass: Hospital
        - Invested: true
        - City:
          - Name: Eretria
          - Population: 14
          - ID: 15642
        - Player: 6: Portugal
        
        ### 64
        - Type: CityInvestedBuilding
        - BuildingClass: Military Base
        - Invested: true
        - City:
          - Name: Nara
          - Population: 22
          - ID: 9293
        - Player: 6: Portugal
        
        ### 65
        - Type: CityInvestedBuilding
        - BuildingClass: Zoo
        - Invested: true
        - City:
          - Name: Zanzibar
          - Population: 18
          - ID: 14648
        - Player: 6: Portugal
        
        ### 66
        - Type: CityInvestedBuilding
        - BuildingClass: Broadcast Tower
        - Invested: true
        - City:
          - Name: Corinth
          - Population: 18
          - ID: 16568
        - Player: 6: Portugal
        
        ### 67
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Fighter
          - ID: 17416
        - Player: 6: Portugal
        - Snow Hills 20,41:
          - Owner: Portugal
          - CityID: 1062
          - Population: 37
          - City: Lisbon
          - Religion: Catholicism
          - Route: Railroad
        
        ### 68
        - Type: UnitCreated
        - UnitType: Fighter
        - Player: 6: Portugal
        - Unit:
          - Level: 1
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 17416
        - Snow Hills 20,41:
          - Owner: Portugal
          - CityID: 1062
          - Population: 37
          - City: Lisbon
          - Religion: Catholicism
          - Route: Railroad
        
        ### 69
        - Type: CityTrained
        - Player: 6: Portugal
        - City:
          - Name: Lisbon
          - Population: 37
          - ID: 1062
        - Unit:
          - Level: 1
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 17416
        
        ### 70
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Fighter
          - ID: 17417
        - Player: 6: Portugal
        - Grass Hills 18,33:
          - Owner: Portugal
          - CityID: 1507
          - Population: 23
          - City: Braga
          - Religion: Catholicism
          - Route: Railroad
        
        ### 71
        - Type: UnitCreated
        - UnitType: Fighter
        - Player: 6: Portugal
        - Unit:
          - Level: 1
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 17417
        - Grass Hills 18,33:
          - Owner: Portugal
          - CityID: 1507
          - Population: 23
          - City: Braga
          - Religion: Catholicism
          - Route: Railroad
        
        ### 72
        - Type: CityTrained
        - Player: 6: Portugal
        - City:
          - Name: Braga
          - Population: 23
          - ID: 1507
        - Unit:
          - Level: 1
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 17417
        
        ### 73
        - Type: CityConstructed
        - City:
          - Name: Osaka
          - Population: 26
          - ID: 4753
        - Owner: 6: Portugal
        - Building: Military Base
        
        ### 74
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Atomic Bomb
          - ID: 17418
        - Player: 6: Portugal
        - Grass Hills 17,28:
          - Owner: Portugal
          - CityID: 5762
          - Population: 24
          - IsRiver: true
          - City: Kyoto
          - Religion: Catholicism
          - Route: Railroad
        
        ### 75
        - Type: UnitCreated
        - UnitType: Atomic Bomb
        - Player: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Icbm
          - Unit: Atomic Bomb
          - ID: 17418
        - Grass Hills 17,28:
          - Owner: Portugal
          - CityID: 5762
          - Population: 24
          - IsRiver: true
          - City: Kyoto
          - Religion: Catholicism
          - Route: Railroad
        
        ### 76
        - Type: CityTrained
        - Player: 6: Portugal
        - City:
          - Name: Kyoto
          - Population: 24
          - ID: 5762
        - Unit:
          - Level: 1
          - AI: Icbm
          - Unit: Atomic Bomb
          - ID: 17418
        
        ### 77
        - Type: CityConstructed
        - City:
          - Name: Nara
          - Population: 22
          - ID: 9293
        - Owner: 6: Portugal
        - Building: Military Base
        
        ### 78
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Fighter
          - ID: 17419
        - Player: 6: Portugal
        - Grass Hills 26,26:
          - Owner: Portugal
          - CityID: 10327
          - Population: 20
          - City: Ouagadougou
          - Resource: Porcelain
          - Route: Railroad
        
        ### 79
        - Type: UnitCreated
        - UnitType: Fighter
        - Player: 6: Portugal
        - Unit:
          - Level: 1
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 17419
        - Grass Hills 26,26:
          - Owner: Portugal
          - CityID: 10327
          - Population: 20
          - City: Ouagadougou
          - Resource: Porcelain
          - Route: Railroad
        
        ### 80
        - Type: CityTrained
        - Player: 6: Portugal
        - City:
          - Name: Ouagadougou
          - Population: 20
          - ID: 10327
        - Unit:
          - Level: 1
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 17419
        
        ### 81
        - Type: CityConstructed
        - City:
          - Name: Novgorod
          - Population: 22
          - ID: 10689
        - Owner: 6: Portugal
        - Building: Military Base
        
        ### 82
        - Type: CityConstructed
        - City:
          - Name: Lalibela
          - Population: 18
          - ID: 12532
        - Owner: 6: Portugal
        - Building: Military Base
        
        ### 83
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Coast 19,2:
          - Owner: Portugal
        
        ### 84
        - Type: CityBoughtPlot
        - WithFaithCulture: true
        - Player: 6: Portugal
        - City:
          - Name: Gondar
          - Population: 16
          - ID: 13821
        - Coast 19,2:
          - Owner: Portugal
        
        ### 85
        - Type: CityConstructed
        - City:
          - Name: Harar
          - Population: 20
          - ID: 14084
        - Owner: 6: Portugal
        - Building: Military Base
        
        ### 86
        - Type: CityConstructed
        - City:
          - Name: Adwa
          - Population: 20
          - ID: 14565
        - Owner: 6: Portugal
        - Building: Public School
        
        ### 87
        - Type: CityConstructed
        - City:
          - Name: Zanzibar
          - Population: 18
          - ID: 14648
        - Owner: 6: Portugal
        - Building: Zoo
        
        ### 88
        - Type: CityConstructed
        - City:
          - Name: Corinth
          - Population: 18
          - ID: 16568
        - Owner: 6: Portugal
        - Building: Military Base
        
        ### 89
        - Type: CityConstructed
        - City:
          - Population: 18
          - Name: Sparta
          - Health: -10%
          - ID: 17171
        - Owner: 6: Portugal
        - Building: Barracks
        
        ### 90
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16193
        - Player: 6: Portugal
        
        ### 91
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16572
        - Player: 6: Portugal
        - Plots:
          - Coast 21,41:
            - Owner: Portugal
          - Ocean 22,41:
            - Owner: Portugal
          - Ocean 23,41:
            - Owner: Portugal
          - Ocean 24,41:
            - Owner: Portugal
        
        ### 92
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16799
        - Player: 6: Portugal
        - Plots:
          - Grass Hills 16,24:
            - Owner: Portugal
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 17,24:
            - Owner: Portugal
            - Resource: Gems
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 18,24:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 18,23:
            - Owner: Portugal
            - CityID: 7664
            - Population: 26
            - IsRiver: true
            - City: Tokyo
            - Resource: Oil
            - Religion: Catholicism
            - Route: Railroad
        
        ### 93
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16944
        - Player: 6: Portugal
        - Plots:
          - Grass Hills 16,27:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Hills 17,28:
            - Owner: Portugal
            - CityID: 5762
            - Population: 24
            - IsRiver: true
            - City: Kyoto
            - Religion: Catholicism
            - Route: Railroad
          - Grass Hills 16,26:
            - Owner: Portugal
            - IsRiver: true
            - Resource: Gems
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 15,25:
            - Owner: Portugal
            - Route: Railroad
          - Grass Hills 15,24:
            - Owner: Portugal
            - Improvement: Village
            - Route: Railroad
        
        ### 94
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16090
        - Player: 6: Portugal
        - Plots:
          - Coast 26,31:
            - Owner: Portugal
            - Resource: Fish
          - Coast 26,30:
            - Owner: Portugal
          - Coast 25,29:
            - Owner: Portugal
          - Coast 25,28:
            - Owner: Portugal
        
        ### 95
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16384
        - Player: 6: Portugal
        - Plots:
          - Plains Hills 14,30:
            - Owner: Portugal
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 14,31:
            - Owner: Portugal
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
          - Grass Hills 15,32:
            - Owner: Portugal
            - Resource: Gems
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 15,33:
            - Owner: Portugal
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 16,34:
            - Owner: Portugal
            - Improvement: Mine
            - Route: Railroad
        
        ### 96
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17054
        - Player: 6: Portugal
        - Plots:
          - Tundra Hills 18,43:
            - Owner: Portugal
            - Improvement: Mine
          - Tundra Land 19,42:
            - Owner: Portugal
            - Resource: Furs
            - Improvement: Camp
            - Feature: Forest
        
        ### 97
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17116
        - Player: 6: Portugal
        - Plots:
          - Plains Land 16,40:
            - Owner: Portugal
            - IsRiver: true
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
          - Tundra Hills 17,40:
            - Owner: Portugal
            - IsRiver: true
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
          - Snow Hills 17,41:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Tundra Land 18,41:
            - Owner: Portugal
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
          - Snow Hills 19,41:
            - Owner: Portugal
            - Improvement: Mine
            - Route: Railroad
          - Snow Hills 20,41:
            - Owner: Portugal
            - CityID: 1062
            - Population: 37
            - City: Lisbon
            - Religion: Catholicism
            - Route: Railroad
        
        ### 98
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16385
        - Player: 6: Portugal
        - Plots:
          - Coast 25,29:
            - Owner: Portugal
          - Coast 25,28:
            - Owner: Portugal
          - Coast 25,27:
            - Owner: Portugal
            - Resource: Coral
            - Improvement: Fishing Boats
          - Grass Hills 26,26:
            - Owner: Portugal
            - CityID: 10327
            - Population: 20
            - City: Ouagadougou
            - Resource: Porcelain
            - Route: Railroad
        
        ### 99
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16616
        - Player: 6: Portugal
        - Plots:
          - Coast 21,21:
            - Owner: Portugal
          - Coast 22,22:
            - Owner: Portugal
          - Coast 22,23:
            - Owner: Portugal
          - Ocean 23,24:
            - Owner: Portugal
        
        ### 100
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16477
        - Player: 6: Portugal
        - Plots:
          - Coast 39,42:
            - Owner: The Maya
          - Coast 40,42:
            - Owner: The Maya
          - Coast 41,42:
            - Owner: The Maya
          - Coast 41,41:
            - Owner: The Maya
        
        ### 101
        - Type: PlayerDoTurn
        - Player: 6: Portugal
        
        ### 102
        - Type: TileRouteChanged
        - NewRoute: 1
        - Owner: 6: Portugal
        - Plains Hills 10,39:
          - Owner: Portugal
          - Improvement: Mine
          - Route: Railroad
        
        ### 103
        - Type: BuildFinished
        - Player: 6: Portugal
        - Plains Hills 10,39:
          - Owner: Portugal
          - Improvement: Mine
          - Route: Railroad
        
        ### 104
        - Type: UnitBuildCompleted
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 13402
        - Build: Construct a Railroad
        - Plains Hills 10,39:
          - Owner: Portugal
          - Improvement: Mine
          - Route: Railroad
        
        ### 105
        - Type: UnitBuildStart
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 13402
        - Build: Construct a Railroad
        - Plains Hills 10,39:
          - Owner: Portugal
          - Improvement: Mine
          - Route: Railroad
        
        ### 106
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 17416
        - Player: 6: Portugal
        - Promotions:
          - Air Supremacy II
          - Ace Pilot II
          - Ace Pilot III
        
        ### 107
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 17417
        - Player: 6: Portugal
        - Promotions:
          - Ace Pilot II
          - Ace Pilot III
          - Ace Pilot IV
        
        ### 108
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 17419
        - Player: 6: Portugal
        - Promotions:
          - Ace Pilot II
          - Ace Pilot III
          - Ace Pilot IV
        
        ### 109
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: FastAttack
          - Unit: Tank
          - ID: 15505
        - Player: 6: Portugal
        - Plots:
          - Plains Hills 21,40:
            - Owner: Portugal
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
          - Snow Hills 20,41:
            - Owner: Portugal
            - CityID: 1062
            - Population: 37
            - City: Lisbon
            - Religion: Catholicism
            - Route: Railroad
          - Coast 21,42:
            - Owner: Portugal
        
        ### 110
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13729
        - Player: 6: Portugal
        - Plots:
          - Snow Hills 19,41:
            - Owner: Portugal
            - Improvement: Mine
            - Route: Railroad
          - Snow Hills 20,41:
            - Owner: Portugal
            - CityID: 1062
            - Population: 37
            - City: Lisbon
            - Religion: Catholicism
            - Route: Railroad
          - Coast 21,41:
            - Owner: Portugal
        
        ### 111
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 56%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17115
        - Player: 6: Portugal
        - Coast 67,16:
          - Owner: Greece
        
        ### 112
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Battleship
          - ID: 16845
        - Player: 6: Portugal
        - Plots:
          - Coast 68,20:
            - Owner: Greece
          - Coast 67,19:
            - Owner: Greece
          - Coast 67,18:
            - Owner: Greece
          - Coast 67,17:
            - Owner: Greece
          - Coast 67,16:
            - Owner: Greece
          - Coast 68,16:
            - Owner: Greece
        
        ### 113
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 83%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16798
        - Player: 6: Portugal
        - Plots:
          - Coast 67,16:
            - Owner: Greece
          - Coast 67,17:
            - Owner: Greece
          - Coast 67,18:
            - Owner: Greece
        
        ### 114
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 75%
          - AI: AssaultSea
          - Unit: Battleship
          - ID: 16797
        - Player: 6: Portugal
        - Plots:
          - Coast 68,19:
            - Owner: Greece
          - Coast 67,19:
            - Owner: Greece
          - Coast 67,18:
            - Owner: Greece
          - Coast 67,17:
            - Owner: Greece
        
        ### 115
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 82%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 16475
        - Player: 6: Portugal
        - Coast 73,14:
          - Owner: Greece
        
        ### 116
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 80%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 16372
        - Player: 6: Portugal
        - Plots:
          - Coast 71,17:
            - Owner: Greece
          - Coast 72,16:
            - Owner: Greece
            - Resource: Fish
          - Coast 72,15:
            - Owner: Greece
          - Coast 73,14:
            - Owner: Greece
          - Coast 72,13:
            - Owner: Greece
            - Resource: Fish
        
        ### 117
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 82%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 16475
        - Player: 6: Portugal
        - Coast 72,13:
          - Owner: Greece
          - Resource: Fish
        
        ### 118
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 80%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 16372
        - Player: 6: Portugal
        - Coast 73,14:
          - Owner: Greece
        
        ### 119
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 33%
          - AI: Defense
          - Unit: Infantry
          - ID: 16308
        - Player: 6: Portugal
        - Plots:
          - Coast 70,18:
            - Owner: Greece
            - Resource: Fish
          - Coast 71,18:
            - Owner: Greece
            - Feature: Atoll
          - Coast 71,17:
            - Owner: Greece
          - Ocean 74,17:
            - Owner: Portugal
        
        ### 120
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 48%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17178
        - Player: 6: Portugal
        - Plots:
          - Coast 70,18:
            - Owner: Greece
            - Resource: Fish
          - Coast 71,18:
            - Owner: Greece
            - Feature: Atoll
          - Coast 71,17:
            - Owner: Greece
          - Coast 72,16:
            - Owner: Greece
            - Resource: Fish
          - Coast 72,15:
            - Owner: Greece
          - Coast 73,14:
            - Owner: Greece
          - Ocean 73,13:
            - Owner: Greece
        
        ### 121
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 83%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16798
        - Player: 6: Portugal
        - Plots:
          - Coast 67,19:
            - Owner: Greece
          - Coast 68,19:
            - Owner: Greece
          - Coast 69,18:
            - Owner: Greece
          - Coast 70,18:
            - Owner: Greece
            - Resource: Fish
        
        ### 122
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 78%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 16089
        - Player: 6: Portugal
        - Plots:
          - Ocean 73,18:
            - Owner: Portugal
          - Ocean 73,15:
            - Owner: Greece
          - Coast 73,14:
            - Owner: Greece
          - Ocean 73,13:
            - Owner: Greece
          - Ocean 74,12:
            - Owner: Greece
        
        ### 123
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 80%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17181
        - Player: 6: Portugal
        - Plots:
          - Coast 73,14:
            - Owner: Greece
          - Coast 72,13:
            - Owner: Greece
            - Resource: Fish
          - Coast 73,12:
            - Owner: Greece
          - Coast 72,11:
            - Owner: Greece
        
        ### 124
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 56%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17115
        - Player: 6: Portugal
        - Plots:
          - Coast 67,17:
            - Owner: Greece
          - Coast 67,18:
            - Owner: Greece
          - Coast 67,19:
            - Owner: Greece
          - Coast 68,20:
            - Owner: Greece
        
        ### 125
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Admiral
          - Unit: Great Admiral
          - ID: 15297
        - Player: 6: Portugal
        - Plots:
          - Coast 70,20:
            - Owner: Greece
          - Coast 70,19:
            - Owner: Greece
          - Coast 71,18:
            - Owner: Greece
            - Feature: Atoll
          - Ocean 72,18:
            - Owner: Portugal
          - Ocean 73,18:
            - Owner: Portugal
          - Ocean 74,18:
            - Owner: Portugal
        
        ### 126
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 92%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 16518
        - Player: 6: Portugal
        - Plots:
          - Tundra Land 9,46:
            - Owner: Greece
          - Plains Land 9,47:
            - Owner: Greece
            - Resource: Coal
            - Improvement: Mine
        
        ### 127
        - Type: CombatResult
        - Tundra Land 9,48:
          - Owner: Greece
          - IsRiver: true
          - Resource: Iron
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 40
          - Damage: 112
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 42%
            - AI: FastAttack
            - Unit: Infantry
            - ID: 16790
        
        ### 128
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 92%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 16518
        - Player: 6: Portugal
        - Tundra Land 10,46:
          - Owner: City-State Winchester
          - Improvement: Fort
          - Route: Railroad
        
        ### 129
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13730
        - Player: 6: Portugal
        - Plots:
          - Tundra Land 8,42:
            - Owner: Portugal
            - Resource: Iron
            - Improvement: Mine
          - Tundra Hills 7,43:
            - Owner: Greece
            - Improvement: Citadel
        
        ### 130
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13640
        - Player: 6: Portugal
        - Plots:
          - Tundra Land 8,46:
            - Owner: Greece
            - Improvement: Fort
          - Tundra Land 9,46:
            - Owner: Greece
        
        ### 131
        - Type: CombatResult
        - Tundra Land 9,48:
          - Owner: Greece
          - IsRiver: true
          - Resource: Iron
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 13
          - Damage: 125
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 10%
            - AI: FastAttack
            - Unit: Infantry
            - ID: 16790
        
        ### 132
        - Type: UnitKilledInCombat
        - KilledPlayer: 63: Barbarians
        - KillerPlayer: 6: Portugal
        - KilledUnit: Infantry
        
        ### 133
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13822
        - Player: 6: Portugal
        - Tundra Land 10,41:
          - Owner: City-State Wanggeom
          - Improvement: Embassy
          - Route: Railroad
        
        ### 134
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: CityBombard
          - Unit: Artillery
          - ID: 14159
        - Player: 6: Portugal
        - Plots:
          - Plains Hills 9,38:
            - Owner: Portugal
            - CityID: 17171
            - Population: 18
            - IsRiver: true
            - City: Sparta
            - Religion: Catholicism
            - Route: Railroad
          - Plains Land 9,39:
            - Owner: Portugal
            - Improvement: Farm
            - Route: Railroad
          - Tundra Hills 10,40:
            - Owner: Portugal
            - Resource: Silver
            - Improvement: Mine
        
        ### 135
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 13198
        - Player: 6: Portugal
        - Plots:
          - Desert Land 9,35:
            - Owner: Portugal
            - IsRiver: true
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 10,36:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 11,36:
            - Owner: Portugal
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 11,35:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 12,35:
            - Owner: Portugal
            - IsRiver: true
            - Resource: Horses
            - Improvement: Academy
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 13,36:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 12,37:
            - Owner: Portugal
            - IsRiver: true
            - Route: Railroad
          - Plains Land 12,38:
            - Owner: Portugal
            - Resource: Maize
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 11,39:
            - Owner: Portugal
            - Improvement: Citadel
            - Route: Railroad
          - Plains Hills 10,39:
            - Owner: Portugal
            - Improvement: Mine
            - Route: Railroad
          - Tundra Hills 10,40:
            - Owner: Portugal
            - Resource: Silver
            - Improvement: Mine
        
        ### 136
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 93%
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 14960
        - Player: 6: Portugal
        - Plots:
          - Plains Hills 15,23:
            - Owner: Portugal
            - Resource: Sheep
            - Improvement: Citadel
            - Route: Railroad
          - Grass Land 16,22:
            - Owner: Portugal
            - Improvement: Town
            - Route: Railroad
          - Plains Land 16,21:
            - Owner: Portugal
            - Resource: Wheat
            - Improvement: Manufactory
            - Route: Railroad
          - Plains Land 17,21:
            - Owner: Portugal
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 18,20:
            - Owner: Portugal
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 19,20:
            - Owner: Portugal
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 19,19:
            - Owner: Portugal
            - CityID: 8163
            - Population: 26
            - IsRiver: true
            - City: Satsuma
            - Religion: Buddhism
            - Route: Railroad
          - Coast 20,20:
            - Owner: Portugal
          - Grass Hills 21,20:
            - Owner: Portugal
            - Improvement: Feitoria
          - Coast 22,20:
            - Owner: Portugal
          - Coast 23,20:
            - Owner: Portugal
        
        ### 137
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Diplomat
          - Unit: Great Diplomat
          - ID: 17362
        - Player: 6: Portugal
        - Plots:
          - Grass Land 17,27:
            - Owner: Portugal
            - IsRiver: true
            - Resource: Cattle
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Land 18,26:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Hills 17,25:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 18,24:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 18,23:
            - Owner: Portugal
            - CityID: 7664
            - Population: 26
            - IsRiver: true
            - City: Tokyo
            - Resource: Oil
            - Religion: Catholicism
            - Route: Railroad
          - Grass Land 18,22:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 18,21:
            - Owner: Portugal
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 19,20:
            - Owner: Portugal
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 19,19:
            - Owner: Portugal
            - CityID: 8163
            - Population: 26
            - IsRiver: true
            - City: Satsuma
            - Religion: Buddhism
            - Route: Railroad
          - Coast 20,20:
            - Owner: Portugal
          - Grass Hills 21,20:
            - Owner: Portugal
            - Improvement: Feitoria
          - Coast 22,20:
            - Owner: Portugal
          - Coast 23,20:
            - Owner: Portugal
        
        ### 138
        - Type: CombatResult
        - Plains Land 71,13:
          - Owner: Greece
          - CityID: 10499
          - Population: 16
          - City: Rhodes
          - Resource: Uranium
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 8
          - Damage: 18
        - Defender:
          - RemainingHP: 134
          - Damage: 547
          - Player: 5: Greece
        
        ### 139
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Admiral
          - Unit: Great Admiral
          - ID: 16038
        - Player: 6: Portugal
        - Coast 72,12:
          - Owner: Greece
        
        ### 140
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AssaultSea
          - Unit: Battleship
          - ID: 16843
        - Player: 6: Portugal
        - Plots:
          - Coast 68,19:
            - Owner: Greece
          - Coast 69,18:
            - Owner: Greece
          - Coast 70,18:
            - Owner: Greece
            - Resource: Fish
          - Coast 71,18:
            - Owner: Greece
            - Feature: Atoll
          - Coast 71,17:
            - Owner: Greece
          - Coast 72,16:
            - Owner: Greece
            - Resource: Fish
          - Coast 72,15:
            - Owner: Greece
        
        ### 141
        - Type: CombatResult
        - Plains Land 71,13:
          - Owner: Greece
          - CityID: 10499
          - Population: 16
          - City: Rhodes
          - Resource: Uranium
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 1
          - Damage: 13
        - Defender:
          - RemainingHP: 231
          - Damage: 778
          - Player: 5: Greece
        
        ### 142
        - Type: UnitCaptured
        - OldOwner: 5: Greece
        - CapturedUnit:
          - Level: 1
          - AI: Settle
          - Unit: Colonist
          - ID: 12474
        - NewOwner: 6: Portugal
        - CapturingUnit:
          - Level: 5
          - Health: 90%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16681
        - Capture: Combat
        
        ### 143
        - Type: UnitKilledInCombat
        - KillerPlayer: 6: Portugal
        - KilledPlayer: 5: Greece
        - KillingUnit:
          - Level: 5
          - Health: 90%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16681
        - KilledUnit: Colonist
        
        ### 144
        - Type: UnitCaptured
        - OldOwner: 5: Greece
        - CapturedUnit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4803
        - NewOwner: 6: Portugal
        - CapturingUnit:
          - Level: 5
          - Health: 90%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16681
        - Capture: Combat
        
        ### 145
        - Type: UnitKilledInCombat
        - KillerPlayer: 6: Portugal
        - KilledPlayer: 5: Greece
        - KillingUnit:
          - Level: 5
          - Health: 90%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16681
        - KilledUnit: Worker
        
        ### 146
        - Type: EspionageState
        - SpyIndex: 0
        - SpyState: 0
        - SpyOwner: 6: Portugal
        
        ### 147
        - Type: SetPopulation
        - OldPopulation: 16
        - NewPopulation: 0
        - City:
          - Owner: Greece
          - CityID: 10499
          - Population: 0
          - City: Rhodes
          - Terrain: Plains
          - Resource: Uranium
          - Religion: Eastern Orthodoxy
          - Route: Railroad
          - Plot: Land
          - X: 71
          - Y: 13
        
        ### 148
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 149
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 150
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 151
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 152
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 153
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 154
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 155
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        - Desert Hills 69,12:
          - Resource: Sheep
          - Improvement: Pasture
          - Route: Road
        
        ### 156
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 157
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 158
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 159
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 160
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 161
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        - Plains Hills 67,13:
          - Resource: Sheep
        
        ### 162
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        - Plains Hills 68,13:
          - Improvement: Mine
          - Route: Railroad
        
        ### 163
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        - Plains Hills 69,13:
          - Improvement: Citadel
          - Route: Railroad
        
        ### 164
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        - Grass Hills 70,13:
          - Improvement: Mine
          - Route: Railroad
        
        ### 165
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        - Plains Land 71,13:
          - Resource: Uranium
          - Route: Railroad
        
        ### 166
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        - Coast 72,13:
          - Resource: Fish
        
        ### 167
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 168
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 169
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        - Grass Land 71,14:
          - Resource: Bison
          - Improvement: Camp
          - Route: Road
        
        ### 170
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        - Grass Land 72,14:
          - Resource: Bananas
          - Improvement: Plantation
        
        ### 171
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 172
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 173
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        - Plains Land 70,15:
          - Improvement: Lumber Mill
          - Route: Railroad
          - Feature: Forest
        
        ### 174
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        - Plains Land 71,15:
          - Improvement: Lumber Mill
          - Feature: Forest
        
        ### 175
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 176
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 177
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 178
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        - Grass Land 71,16:
          - Improvement: Farm
        
        ### 179
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        - Coast 72,16:
          - Resource: Fish
        
        ### 180
        - Type: TileOwnershipChanged
        - OldOwner: 5: Greece
        
        ### 181
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Plains Land 71,13:
          - Owner: Portugal
          - Resource: Uranium
          - Route: Railroad
        
        ### 182
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Grass Hills 70,13:
          - Owner: Portugal
          - Improvement: Mine
          - Route: Railroad
        
        ### 183
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Grass Land 71,14:
          - Owner: Portugal
          - Resource: Bison
          - Improvement: Camp
          - Route: Road
        
        ### 184
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Coast 71,12:
          - Owner: Portugal
        
        ### 185
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Grass Land 72,14:
          - Owner: Portugal
          - Resource: Bananas
          - Improvement: Plantation
        
        ### 186
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Coast 72,12:
          - Owner: Portugal
        
        ### 187
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Coast 72,13:
          - Owner: Portugal
          - Resource: Fish
        
        ### 188
        - Type: SetPopulation
        - OldPopulation: 0
        - NewPopulation: 1
        - City:
          - Owner: Portugal
          - CityID: 17420
          - Population: 1
          - City: Rhodes
          - Terrain: Plains
          - Resource: Uranium
          - Route: Railroad
          - Plot: Land
          - X: 71
          - Y: 13
        
        ### 189
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Anti-Aircraft Gun
          - ID: 17421
        - Player: 6: Portugal
        - Plains Land 71,13:
          - Owner: Portugal
          - CityID: 17420
          - Population: 14
          - City: Rhodes
          - Resource: Uranium
          - Route: Railroad
        
        ### 190
        - Type: UnitCreated
        - UnitType: Anti-Aircraft Gun
        - Player: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 17421
        - Plains Land 71,13:
          - Owner: Portugal
          - CityID: 17420
          - Population: 14
          - City: Rhodes
          - Resource: Uranium
          - Route: Railroad
        
        ### 191
        - Type: SetPopulation
        - OldPopulation: 1
        - NewPopulation: 14
        - City:
          - Owner: Portugal
          - CityID: 17420
          - Population: 14
          - City: Rhodes
          - Terrain: Plains
          - Resource: Uranium
          - Route: Railroad
          - Plot: Land
          - X: 71
          - Y: 13
        
        ### 192
        - Type: CityConvertsReligion
        - City:
          - Owner: Portugal
          - CityID: 17420
          - Population: 14
          - City: Rhodes
          - Terrain: Plains
          - Resource: Uranium
          - Religion: Eastern Orthodoxy
          - Route: Railroad
          - Plot: Land
          - X: 71
          - Y: 13
        - Owner: 6: Portugal
        - Religion: Eastern Orthodoxy
        
        ### 193
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 80%
          - AI: Defense
          - Unit: Infantry
          - ID: 15461
        - Player: 1: The Netherlands
        - Plains Land 70,15:
          - Improvement: Lumber Mill
          - Route: Railroad
          - Feature: Forest
        
        ### 194
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 90%
          - AI: Defense
          - Unit: Infantry
          - ID: 15528
        - Player: 1: The Netherlands
        - Grass Land 71,16:
          - Improvement: Farm
        
        ### 195
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 56%
          - AI: Defense
          - Unit: Infantry
          - ID: 15594
        - Player: 1: The Netherlands
        - Plains Land 71,15:
          - Improvement: Lumber Mill
          - Feature: Forest
        
        ### 196
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Coast 71,10:
          - Owner: Portugal
        
        ### 197
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Coast 72,10:
          - Owner: Portugal
        
        ### 198
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Ocean 73,10:
          - Owner: Portugal
        
        ### 199
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Coast 70,11:
          - Owner: Portugal
        
        ### 200
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Ocean 71,11:
          - Owner: Portugal
        
        ### 201
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Coast 72,11:
          - Owner: Portugal
        
        ### 202
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Ocean 73,11:
          - Owner: Portugal
        
        ### 203
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Desert Hills 69,12:
          - Owner: Portugal
          - Resource: Sheep
          - Improvement: Pasture
          - Route: Road
        
        ### 204
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 47%
          - AI: CityBombard
          - Unit: Artillery
          - ID: 15255
        - Player: 1: The Netherlands
        - Plains Hills 68,13:
          - Improvement: Mine
          - Route: Railroad
        
        ### 205
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Coast 70,12:
          - Owner: Portugal
        
        ### 206
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Coast 73,12:
          - Owner: Portugal
        
        ### 207
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Ocean 74,12:
          - Owner: Portugal
        
        ### 208
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Plains Hills 67,13:
          - Owner: Portugal
          - Resource: Sheep
        
        ### 209
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Plains Hills 68,13:
          - Owner: Portugal
          - Improvement: Mine
          - Route: Railroad
        
        ### 210
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 47%
          - AI: CityBombard
          - Unit: Artillery
          - ID: 15255
        - Player: 1: The Netherlands
        - Plains Hills 69,14:
          - Improvement: Mine
          - Route: Railroad
        
        ### 211
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Plains Hills 69,13:
          - Owner: Portugal
          - Improvement: Citadel
          - Route: Railroad
        
        ### 212
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 38%
          - AI: Defense
          - Unit: Infantry
          - ID: 15912
        - Player: 1: The Netherlands
        - Plains Hills 69,11:
          - Owner: The Netherlands
          - Feature: Forest
        
        ### 213
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Ocean 73,13:
          - Owner: Portugal
        
        ### 214
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Ocean 74,13:
          - Owner: Portugal
        
        ### 215
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Plains Hills 69,14:
          - Owner: Portugal
          - Improvement: Mine
          - Route: Railroad
        
        ### 216
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Coast 73,14:
          - Owner: Portugal
        
        ### 217
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Ocean 74,14:
          - Owner: Portugal
        
        ### 218
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Plains Land 70,15:
          - Owner: Portugal
          - Improvement: Lumber Mill
          - Route: Railroad
          - Feature: Forest
        
        ### 219
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Plains Land 71,15:
          - Owner: Portugal
          - Improvement: Lumber Mill
          - Feature: Forest
        
        ### 220
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 56%
          - AI: Defense
          - Unit: Infantry
          - ID: 15594
        - Player: 1: The Netherlands
        - Plains Hills 69,9:
          - Owner: The Netherlands
        
        ### 221
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Coast 72,15:
          - Owner: Portugal
        
        ### 222
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Ocean 73,15:
          - Owner: Portugal
        
        ### 223
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Ocean 74,15:
          - Owner: Portugal
        
        ### 224
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Grass Land 71,16:
          - Owner: Portugal
          - Improvement: Farm
        
        ### 225
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Coast 72,16:
          - Owner: Portugal
          - Resource: Fish
        
        ### 226
        - Type: TileOwnershipChanged
        - NewOwner: 6: Portugal
        - Ocean 73,16:
          - Owner: Portugal
        
        ### 227
        - Type: CityCaptureComplete
        - Population: 16
        - IsConquest: true
        - TotalGreatWorks: 0
        - CapturedGreatWorks: 0
        - OldOwner: 5: Greece
        - City:
          - Owner: Portugal
          - CityID: 17420
          - Population: 14
          - City: Rhodes
          - Terrain: Plains
          - Resource: Uranium
          - Religion: Eastern Orthodoxy
          - Route: Railroad
          - Plot: Land
          - X: 71
          - Y: 13
        - NewOwner: 6: Portugal
        
        ### 228
        - Type: CityInvestedBuilding
        - BuildingClass: Courthouse
        - Invested: true
        - City:
          - Population: 14
          - Name: Rhodes
          - Health: -49%
          - ID: 17420
        - Player: 6: Portugal
        
        ### 229
        - Type: CityInvestedBuilding
        - BuildingClass: Courthouse
        - Invested: true
        - City:
          - Population: 14
          - Name: Rhodes
          - Health: -49%
          - ID: 17420
        - Player: 6: Portugal
        
        ### 230
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Worker
          - ID: 17422
        - Player: 6: Portugal
        - Plains Land 71,13:
          - Owner: Portugal
          - CityID: 17420
          - Population: 14
          - City: Rhodes
          - Resource: Uranium
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 231
        - Type: UnitCreated
        - UnitType: Worker
        - Player: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 17422
        - Plains Land 71,13:
          - Owner: Portugal
          - CityID: 17420
          - Population: 14
          - City: Rhodes
          - Resource: Uranium
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 232
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Worker
          - ID: 17423
        - Player: 6: Portugal
        - Plains Land 71,13:
          - Owner: Portugal
          - CityID: 17420
          - Population: 14
          - City: Rhodes
          - Resource: Uranium
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 233
        - Type: UnitCreated
        - UnitType: Worker
        - Player: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 17423
        - Plains Land 71,13:
          - Owner: Portugal
          - CityID: 17420
          - Population: 14
          - City: Rhodes
          - Resource: Uranium
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 234
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 90%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16681
        - Player: 6: Portugal
        - Plains Land 71,13:
          - Owner: Portugal
          - CityID: 17420
          - Population: 14
          - City: Rhodes
          - Resource: Uranium
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 235
        - Type: CombatResult
        - Grass Land 68,17:
          - Owner: Greece
          - CityID: 8359
          - Population: 18
          - City: Ephesus
          - Resource: Iron
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 24
          - Damage: 126
          - Player: 5: Greece
        
        ### 236
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 56%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17177
        - Player: 6: Portugal
        - Plots:
          - Coast 67,18:
            - Owner: Greece
          - Coast 67,19:
            - Owner: Greece
          - Coast 68,19:
            - Owner: Greece
          - Coast 69,18:
            - Owner: Greece
          - Coast 69,17:
            - Owner: Greece
        
        ### 237
        - Type: CombatResult
        - Grass Land 68,17:
          - Owner: Greece
          - CityID: 8359
          - Population: 18
          - City: Ephesus
          - Resource: Iron
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 26
          - Damage: 152
          - Player: 5: Greece
        
        ### 238
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 17%
          - AI: CityBombard
          - Unit: Artillery
          - ID: 13954
        - Player: 6: Portugal
        - Grass Land 71,16:
          - Owner: Portugal
          - Improvement: Farm
        
        ### 239
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 72%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13892
        - Player: 6: Portugal
        - Tundra Hills 11,46:
          - Owner: City-State Winchester
          - Resource: Silver
          - Improvement: Mine
          - Route: Railroad
        
        ### 240
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 24
        - OldImprovement: Mine
        - NewImprovement: Mine
        - Tundra Hills 11,46:
          - Owner: City-State Winchester
          - Resource: Silver
          - Improvement: Mine
          - Route: Railroad
        
        ### 241
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - Health: 86%
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 17172
        - Player: 6: Portugal
        - Plots:
          - Tundra Land 9,50:
            - Owner: Greece
            - IsRiver: true
            - Resource: Silver
            - Improvement: Mine
          - Tundra Land 8,50:
            - Owner: Greece
            - IsRiver: true
            - Improvement: Farm
        
        ### 242
        - Type: CombatResult
        - Snow Land 7,50:
          - Owner: Greece
          - IsRiver: true
          - Improvement: Farm
        - Attacker:
          - RemainingHP: 11
          - Damage: 25
        - Defender:
          - RemainingHP: 59
          - Damage: 59
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 17312
        
        ### 243
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 63%
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 17184
        - Player: 6: Portugal
        - Plots:
          - Plains Land 7,37:
            - Owner: Portugal
            - Improvement: Farm
          - Desert Hills 7,36:
            - Owner: Portugal
            - Improvement: Mine
          - Plains Land 6,36:
            - Owner: City-State Cape Town
            - Improvement: Farm
        
        ### 244
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 22
        - OldImprovement: Farm
        - NewImprovement: Farm
        - Plains Land 6,36:
          - Owner: City-State Cape Town
          - Improvement: Farm
        
        ### 245
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 33%
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16297
        - Player: 6: Portugal
        - Tundra Hills 6,39:
          - Owner: Greece
          - Improvement: Mine
        
        ### 246
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 59%
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 16307
        - Player: 6: Portugal
        - Plots:
          - Tundra Hills 8,40:
            - Owner: Portugal
            - Resource: Silver
            - Improvement: Town
            - Route: Railroad
          - Tundra Land 7,40:
            - Owner: Portugal
            - Improvement: Lumber Mill
            - Feature: Forest
          - Tundra Hills 6,39:
            - Owner: Greece
            - Improvement: Mine
          - Tundra Hills 5,39:
            - Owner: Greece
            - Improvement: Mine
        
        ### 247
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 70%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16726
        - Player: 6: Portugal
        - Plots:
          - Coast 3,35:
            - Owner: City-State Cape Town
          - Coast 3,36:
            - Owner: City-State Cape Town
        
        ### 248
        - Type: CombatResult
        - Desert Hills 5,36:
          - Owner: City-State Cape Town
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 1
          - Damage: 13
        - Defender:
          - RemainingHP: 164
          - Damage: 229
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 35%
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 17195
        
        ### 249
        - Type: UnitKilledInCombat
        - KilledPlayer: 63: Barbarians
        - KillerPlayer: 6: Portugal
        - KilledUnit: Machine Gun
        
        ### 250
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 17184
        - Player: 6: Portugal
        - Desert Hills 5,36:
          - Owner: City-State Cape Town
          - Improvement: Mine
        
        ### 251
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 70%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16726
        - Player: 6: Portugal
        - Plots:
          - Ocean 2,37:
            - Owner: Greece
          - Ocean 2,38:
            - Owner: Greece
          - Coast 2,39:
            - Owner: Greece
          - Ocean 2,40:
            - Owner: Greece
          - Ocean 1,41:
            - Owner: Greece
        
        ### 252
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13731
        - Player: 6: Portugal
        - Plots:
          - Tundra Land 7,41:
            - Owner: Portugal
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
          - Plains Land 7,42:
            - Owner: Greece
            - IsRiver: true
            - Route: Railroad
        
        ### 253
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13819
        - Player: 6: Portugal
        - Plains Land 6,35:
          - Owner: City-State Cape Town
          - Improvement: Farm
        
        ### 254
        - Type: CombatResult
        - Grass Land 5,34:
          - Owner: City-State Cape Town
          - CityID: 1064
          - Population: 19
          - City: Cape Town
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 17
          - Damage: 17
          - Player: 22
        
        ### 255
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 17251
        - Player: 6: Portugal
        - Plots:
          - Plains Hills 7,33:
            - Owner: City-State Cape Town
            - Improvement: Mine
          - Plains Hills 6,33:
            - Owner: City-State Cape Town
            - Improvement: Mine
            - Route: Railroad
        
        ### 256
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 59%
          - AI: Defense
          - Unit: Infantry
          - ID: 16322
        - Player: 6: Portugal
        - Grass Land 5,33:
          - Owner: City-State Cape Town
          - Route: Railroad
        
        ### 257
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 43%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16428
        - Player: 6: Portugal
        - Plots:
          - Plains Land 6,31:
            - Owner: Portugal
            - Feature: Forest
          - Grass Land 6,32:
            - Owner: City-State Cape Town
            - Resource: Cotton
            - Improvement: Embassy
        
        ### 258
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: CityBombard
          - Unit: Artillery
          - ID: 14014
        - Player: 6: Portugal
        - Desert Hills 7,36:
          - Owner: Portugal
          - Improvement: Mine
        
        ### 259
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 52%
          - AI: CityBombard
          - Unit: Artillery
          - ID: 13639
        - Player: 6: Portugal
        - Plains Hills 8,32:
          - Owner: Portugal
          - Resource: Gold
          - Improvement: Mine
        
        ### 260
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 14891
        - Player: 6: Portugal
        - Tundra Hills 8,40:
          - Owner: Portugal
          - Resource: Silver
          - Improvement: Town
          - Route: Railroad
        
        ### 261
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16476
        - Player: 6: Portugal
        - Plots:
          - Tundra Hills 8,41:
            - Owner: Portugal
            - Improvement: Mine
          - Snow Hills 9,42:
            - Owner: Greece
        
        ### 262
        - Type: TileRouteChanged
        - OldRoute: 1
        - NewRoute: 1
        - IsPillaged: true
        - Owner: 24
        - Tundra Land 10,46:
          - Owner: City-State Winchester
          - Improvement: Fort
          - Route: Railroad
        
        ### 263
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16290
        - Player: 6: Portugal
        - Plots:
          - Plains Land 8,38:
            - Owner: Portugal
            - Resource: Uranium
            - Improvement: Farm
          - Tundra Hills 8,39:
            - Owner: Portugal
            - Improvement: Mine
            - Route: Railroad
        
        ### 264
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14601
        - Player: 6: Portugal
        - Plots:
          - Tundra Hills 10,44:
            - Owner: Greece
          - Tundra Hills 9,44:
            - Owner: Greece
        
        ### 265
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13731
        - Player: 6: Portugal
        - Plots:
          - Tundra Land 8,42:
            - Owner: Portugal
            - Resource: Iron
            - Improvement: Mine
          - Tundra Land 8,43:
            - Owner: Greece
        
        ### 266
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 93%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15298
        - Player: 6: Portugal
        - Plots:
          - Tundra Land 11,42:
            - Owner: City-State Wanggeom
          - Snow Hills 10,42:
            - Owner: Portugal
        
        ### 267
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 17%
          - AI: CityBombard
          - Unit: Artillery
          - ID: 13954
        - Player: 6: Portugal
        - Plains Land 71,15:
          - Owner: Portugal
          - Improvement: Lumber Mill
          - Feature: Forest
        
        ### 268
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 44%
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 16301
        - Player: 6: Portugal
        - Plots:
          - Coast 2,43:
            - Owner: Greece
          - Ocean 2,42:
            - Owner: Greece
          - Ocean 1,41:
            - Owner: Greece
        
        ### 269
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 40%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16291
        - Player: 6: Portugal
        - Tundra Hills 9,45:
          - Owner: City-State Winchester
          - Resource: Silver
          - Improvement: Embassy
        
        ### 270
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16844
        - Player: 6: Portugal
        - Plots:
          - Coast 72,13:
            - Owner: Portugal
            - Resource: Fish
          - Coast 73,14:
            - Owner: Portugal
          - Coast 72,15:
            - Owner: Portugal
          - Coast 72,16:
            - Owner: Portugal
            - Resource: Fish
          - Coast 71,17:
            - Owner: Greece
          - Coast 71,18:
            - Owner: Greece
            - Feature: Atoll
          - Ocean 71,19:
            - Owner: Portugal
        
        ### 271
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16672
        - Player: 6: Portugal
        - Plots:
          - Coast 21,41:
            - Owner: Portugal
          - Coast 21,42:
            - Owner: Portugal
        
        ### 272
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16721
        - Player: 6: Portugal
        - Plots:
          - Ocean 21,43:
            - Owner: Portugal
          - Ocean 22,42:
            - Owner: Portugal
        
        ### 273
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16679
        - Player: 6: Portugal
        - Plots:
          - Ocean 21,43:
            - Owner: Portugal
          - Coast 20,43:
            - Owner: Portugal
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 274
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16722
        - Player: 6: Portugal
        - Plots:
          - Coast 24,20:
            - Owner: City-State Panama City
          - Coast 23,20:
            - Owner: Portugal
        
        ### 275
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16723
        - Player: 6: Portugal
        - Plots:
          - Ocean 21,43:
            - Owner: Portugal
          - Coast 21,42:
            - Owner: Portugal
          - Snow Hills 20,41:
            - Owner: Portugal
            - CityID: 1062
            - Population: 37
            - City: Lisbon
            - Religion: Catholicism
            - Route: Railroad
        
        ### 276
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Battleship
          - ID: 16725
        - Player: 6: Portugal
        - Plots:
          - Ocean 27,24:
            - Owner: Portugal
          - Ocean 26,23:
            - Owner: Portugal
          - Coast 26,22:
            - Owner: Portugal
          - Coast 25,22:
            - Owner: Portugal
          - Coast 23,21:
            - Owner: Portugal
        
        ### 277
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 85%
          - AI: AssaultSea
          - Unit: Battleship
          - ID: 16682
        - Player: 6: Portugal
        - Plots:
          - Coast 27,26:
            - Owner: Portugal
          - Coast 26,25:
            - Owner: Portugal
          - Coast 26,24:
            - Owner: Portugal
          - Coast 25,23:
            - Owner: Portugal
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 25,22:
            - Owner: Portugal
          - Coast 24,20:
            - Owner: City-State Panama City
        
        ### 278
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Admiral
          - Unit: Great Admiral
          - ID: 16038
        - Player: 6: Portugal
        - Plains Land 71,13:
          - Owner: Portugal
          - CityID: 17420
          - Population: 14
          - City: Rhodes
          - Resource: Uranium
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 279
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Explore
          - Unit: Anti-Aircraft Gun
          - ID: 15983
        - Player: 6: Portugal
        - Coast 22,22:
          - Owner: Portugal
        
        ### 280
        - Type: RebaseTo
        - Player: 6: Portugal
        - Unit:
          - Level: 5
          - Health: 76%
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 17179
        - Plains Hills 22,30:
          - Owner: Portugal
          - CityID: 4753
          - Population: 26
          - IsRiver: true
          - City: Osaka
          - Route: Railroad
        
        ### 281
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 76%
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 17179
        - Player: 6: Portugal
        - Plains Hills 22,30:
          - Owner: Portugal
          - CityID: 4753
          - Population: 26
          - IsRiver: true
          - City: Osaka
          - Route: Railroad
        
        ### 282
        - Type: RebaseTo
        - Player: 6: Portugal
        - Unit:
          - Level: 4
          - Health: 78%
          - AI: AttackAir
          - Unit: Bomber
          - ID: 15639
        - Plains Hills 22,30:
          - Owner: Portugal
          - CityID: 4753
          - Population: 26
          - IsRiver: true
          - City: Osaka
          - Route: Railroad
        
        ### 283
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 78%
          - AI: AttackAir
          - Unit: Bomber
          - ID: 15639
        - Player: 6: Portugal
        - Plains Hills 22,30:
          - Owner: Portugal
          - CityID: 4753
          - Population: 26
          - IsRiver: true
          - City: Osaka
          - Route: Railroad
        
        ### 284
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 16379
        - Player: 6: Portugal
        - Plots:
          - Desert Land 76,19:
            - Owner: Portugal
            - CityID: 15642
            - Population: 14
            - City: Eretria
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Desert Land 76,20:
            - Owner: Portugal
            - Improvement: Village
            - Route: Railroad
          - Desert Land 75,21:
            - Owner: Portugal
            - Improvement: Citadel
            - Route: Railroad
          - Coast 75,20:
            - Owner: Portugal
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 74,20:
            - Owner: Portugal
          - Desert Land 73,21:
            - Owner: Portugal
            - CityID: 17174
            - Population: 14
            - City: Halicarnassus
            - Route: Railroad
        
        ### 285
        - Type: TileRouteChanged
        - OldRoute: 1
        - NewRoute: 1
        - Owner: 6: Portugal
        - Plains Land 9,37:
          - Owner: Portugal
          - IsRiver: true
          - Resource: Wheat
          - Improvement: Farm
          - Route: Railroad
        
        ### 286
        - Type: BuildFinished
        - Player: 6: Portugal
        - Plains Land 9,37:
          - Owner: Portugal
          - IsRiver: true
          - Resource: Wheat
          - Improvement: Farm
          - Route: Railroad
        
        ### 287
        - Type: UnitBuildCompleted
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 5831
        - Build: Repair an Improvement
        - Plains Land 9,37:
          - Owner: Portugal
          - IsRiver: true
          - Resource: Wheat
          - Improvement: Farm
          - Route: Railroad
        
        ### 288
        - Type: UnitBuildStart
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 5831
        - Build: Repair an Improvement
        - Plains Land 9,37:
          - Owner: Portugal
          - IsRiver: true
          - Resource: Wheat
          - Improvement: Farm
          - Route: Railroad
        
        ### 289
        - Type: TileImprovementChanged
        - Owner: 6: Portugal
        - OldImprovement: Mine
        - NewImprovement: Mine
        - Tundra Hills 8,39:
          - Owner: Portugal
          - Improvement: Mine
          - Route: Railroad
        
        ### 290
        - Type: BuildFinished
        - Player: 6: Portugal
        - Tundra Hills 8,39:
          - Owner: Portugal
          - Improvement: Mine
          - Route: Railroad
        
        ### 291
        - Type: UnitBuildCompleted
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - Health: 95%
          - AI: Worker
          - Unit: Worker
          - ID: 8014
        - Build: Repair an Improvement
        - Tundra Hills 8,39:
          - Owner: Portugal
          - Improvement: Mine
          - Route: Railroad
        
        ### 292
        - Type: UnitBuildStart
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - Health: 95%
          - AI: Worker
          - Unit: Worker
          - ID: 8014
        - Build: Repair an Improvement
        - Tundra Hills 8,39:
          - Owner: Portugal
          - Improvement: Mine
          - Route: Railroad
        
        ### 293
        - Type: UnitBuildCompleted
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 13891
        - Build: Construct a Railroad
        - Tundra Hills 10,40:
          - Owner: Portugal
          - Resource: Silver
          - Improvement: Mine
        
        ### 294
        - Type: UnitBuildCompleted
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 8411
        - Build: Construct a Railroad
        - Plains Land 8,38:
          - Owner: Portugal
          - Resource: Uranium
          - Improvement: Farm
        
        ### 295
        - Type: UnitBuildCompleted
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 10690
        - Build: Construct a Railroad
        - Plains Land 9,40:
          - Owner: Portugal
          - Improvement: Farm
        
        ### 296
        - Type: UnitBuildCompleted
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 9870
        - Build: Construct a Railroad
        - Plains Hills 8,37:
          - Owner: Portugal
          - IsRiver: true
          - Improvement: Mine
        
        ### 297
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 6374
        - Player: 6: Portugal
        - Plots:
          - Plains Land 9,39:
            - Owner: Portugal
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 9,40:
            - Owner: Portugal
            - Improvement: Farm
          - Tundra Hills 8,41:
            - Owner: Portugal
            - Improvement: Mine
        
        ### 298
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 14566
        - Player: 6: Portugal
        - Plots:
          - Plains Hills 11,39:
            - Owner: Portugal
            - Improvement: Citadel
            - Route: Railroad
          - Plains Hills 10,39:
            - Owner: Portugal
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 9,39:
            - Owner: Portugal
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 9,40:
            - Owner: Portugal
            - Improvement: Farm
          - Tundra Hills 8,40:
            - Owner: Portugal
            - Resource: Silver
            - Improvement: Town
            - Route: Railroad
        
        ### 299
        - Type: TileImprovementChanged
        - Owner: 6: Portugal
        - OldImprovement: Mine
        - Grass Hills 74,23:
          - Owner: Portugal
          - Resource: Uranium
        
        ### 300
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 12747
        - Build: Construct a Quarry
        - Grass Hills 74,23:
          - Owner: Portugal
          - Resource: Uranium
        
        ### 301
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 9294
        - Player: 6: Portugal
        - Plots:
          - Desert Land 76,20:
            - Owner: Portugal
            - Improvement: Village
            - Route: Railroad
          - Desert Land 76,19:
            - Owner: Portugal
            - CityID: 15642
            - Population: 14
            - City: Eretria
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Coast 75,19:
            - Owner: Portugal
          - Coast 75,18:
            - Owner: Portugal
          - Ocean 74,17:
            - Owner: Portugal
        
        ### 302
        - Type: TileImprovementChanged
        - Owner: 6: Portugal
        - OldImprovement: Mine
        - NewImprovement: Mine
        - Plains Hills 11,36:
          - Owner: Portugal
          - Improvement: Mine
          - Route: Railroad
        
        ### 303
        - Type: BuildFinished
        - Player: 6: Portugal
        - Plains Hills 11,36:
          - Owner: Portugal
          - Improvement: Mine
          - Route: Railroad
        
        ### 304
        - Type: UnitBuildCompleted
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 14219
        - Build: Repair an Improvement
        - Plains Hills 11,36:
          - Owner: Portugal
          - Improvement: Mine
          - Route: Railroad
        
        ### 305
        - Type: UnitBuildStart
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 14219
        - Build: Repair an Improvement
        - Plains Hills 11,36:
          - Owner: Portugal
          - Improvement: Mine
          - Route: Railroad
        
        ### 306
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 16374
        - Build: Repair an Improvement
        - Grass Land 73,22:
          - Owner: Portugal
          - Resource: Cattle
          - Improvement: Pasture
        
        ### 307
        - Type: UnitBuildCompleted
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 16563
        - Build: Construct a Feitoria
        - Desert Hills 77,19:
          - Owner: Portugal
        
        ### 308
        - Type: TileImprovementChanged
        - Owner: 6: Portugal
        - OldImprovement: Fort
        - Grass Land 76,22:
          - Owner: Portugal
        
        ### 309
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 14416
        - Build: Construct a Feitoria
        - Grass Land 76,22:
          - Owner: Portugal
        
        ### 310
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 2387
        - Player: 6: Portugal
        - Plots:
          - Plains Hills 9,38:
            - Owner: Portugal
            - CityID: 17171
            - Population: 18
            - IsRiver: true
            - City: Sparta
            - Religion: Catholicism
            - Route: Railroad
          - Plains Land 9,39:
            - Owner: Portugal
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 10,39:
            - Owner: Portugal
            - Improvement: Mine
            - Route: Railroad
        
        ### 311
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 2387
        - Build: Repair an Improvement
        - Plains Hills 10,39:
          - Owner: Portugal
          - Improvement: Mine
          - Route: Railroad
        
        ### 312
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4808
        - Player: 6: Portugal
        - Plots:
          - Plains Hills 11,36:
            - Owner: Portugal
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 11,37:
            - Owner: Portugal
            - Improvement: Mine
        
        ### 313
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 14847
        - Build: Repair an Improvement
        - Plains Hills 75,22:
          - Owner: Portugal
          - Resource: Sheep
          - Improvement: Pasture
          - Route: Railroad
        
        ### 314
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 5466
        - Player: 6: Portugal
        - Plots:
          - Plains Land 11,35:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 11,36:
            - Owner: Portugal
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 10,36:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
        
        ### 315
        - Type: TileImprovementChanged
        - Owner: 6: Portugal
        - OldImprovement: Village
        - Plains Land 10,36:
          - Owner: Portugal
          - IsRiver: true
          - Route: Railroad
        
        ### 316
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 5466
        - Build: Construct a Farm
        - Plains Land 10,36:
          - Owner: Portugal
          - IsRiver: true
          - Route: Railroad
        
        ### 317
        - Type: TileImprovementChanged
        - Owner: 6: Portugal
        - OldImprovement: Village
        - Desert Land 77,21:
          - Owner: Portugal
        
        ### 318
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 17176
        - Build: Construct a Feitoria
        - Desert Land 77,21:
          - Owner: Portugal
        
        ### 319
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 9058
        - Player: 6: Portugal
        - Plots:
          - Plains Land 9,36:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Farm
          - Desert Land 9,35:
            - Owner: Portugal
            - IsRiver: true
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
            - Feature: Flood Plains
        
        ### 320
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 10328
        - Player: 6: Portugal
        - Tundra Hills 10,40:
          - Owner: Portugal
          - Resource: Silver
          - Improvement: Mine
        
        ### 321
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 16570
        - Player: 6: Portugal
        - Plots:
          - Plains Land 9,34:
            - Owner: Portugal
            - Resource: Ivory
            - Improvement: Camp
            - Route: Railroad
          - Plains Hills 9,33:
            - Owner: Portugal
            - Resource: Antiquity Site
            - Route: Railroad
          - Desert Hills 10,33:
            - Owner: Portugal
            - IsRiver: true
            - Resource: Gold
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 11,33:
            - Owner: Portugal
            - CityID: 16568
            - Population: 18
            - IsRiver: true
            - City: Corinth
            - Religion: Catholicism
            - Route: Railroad
          - Desert Land 12,32:
            - Owner: Portugal
            - IsRiver: true
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 11,31:
            - Owner: Portugal
            - IsRiver: true
            - Resource: Aluminum
            - Improvement: Town
            - Route: Railroad
          - Plains Land 12,30:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
        
        ### 322
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 14848
        - Player: 6: Portugal
        - Plots:
          - Grass Land 12,37:
            - Owner: Portugal
            - IsRiver: true
            - Route: Railroad
          - Plains Land 13,36:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 12,35:
            - Owner: Portugal
            - IsRiver: true
            - Resource: Horses
            - Improvement: Academy
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Hills 12,34:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Desert Land 11,33:
            - Owner: Portugal
            - CityID: 16568
            - Population: 18
            - IsRiver: true
            - City: Corinth
            - Religion: Catholicism
            - Route: Railroad
          - Desert Land 12,32:
            - Owner: Portugal
            - IsRiver: true
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 11,31:
            - Owner: Portugal
            - IsRiver: true
            - Resource: Aluminum
            - Improvement: Town
            - Route: Railroad
        
        ### 323
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 16895
        - Player: 6: Portugal
        - Plots:
          - Grass Land 6,23:
            - Owner: Portugal
            - Improvement: Village
            - Route: Railroad
          - Grass Hills 7,24:
            - Owner: Portugal
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 7,25:
            - Owner: Portugal
            - Improvement: Village
            - Route: Railroad
          - Grass Land 8,25:
            - Owner: Portugal
            - Resource: Perfume
            - Improvement: Town
            - Route: Railroad
          - Tundra Hills 9,24:
            - Owner: Portugal
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 9,23:
            - Owner: Portugal
            - Resource: Gold
            - Improvement: Town
            - Route: Railroad
          - Plains Land 10,23:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 11,22:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Feitoria
            - Route: Railroad
          - Coast 11,21:
            - Owner: Portugal
          - Grass Land 12,21:
            - Owner: Portugal
            - IsRiver: true
            - Resource: Maize
            - Improvement: Citadel
          - Coast 13,20:
            - Owner: Portugal
          - Coast 13,19:
            - Owner: Portugal
          - Coast 14,18:
            - Owner: Portugal
        
        ### 324
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Fleet Destroyer
          - ID: 17424
        - Player: 6: Portugal
        - Coast 72,13:
          - Owner: Portugal
          - Resource: Fish
        
        ### 325
        - Type: UnitCreated
        - UnitType: Fleet Destroyer
        - Player: 6: Portugal
        - Unit:
          - Level: 1
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17424
        - Coast 72,13:
          - Owner: Portugal
          - Resource: Fish
        
        ### 326
        - Type: UnitUpgraded
        - Player: 6: Portugal
        - OldUnit:
          - Level: 4
          - Health: 82%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 16475
        - NewUnit:
          - Level: 1
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17424
        
        ### 327
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 6: Portugal
        - OriginalUnit:
          - Level: 4
          - Health: 82%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 16475
        - NewOwner: 6: Portugal
        - ConvertingUnit:
          - Level: 4
          - Health: 82%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17424
        
        ### 328
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Fighter
          - ID: 17425
        - Player: 6: Portugal
        - Desert Land 11,33:
          - Owner: Portugal
          - CityID: 16568
          - Population: 18
          - IsRiver: true
          - City: Corinth
          - Religion: Catholicism
          - Route: Railroad
        
        ### 329
        - Type: UnitCreated
        - UnitType: Fighter
        - Player: 6: Portugal
        - Unit:
          - Level: 1
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 17425
        - Desert Land 11,33:
          - Owner: Portugal
          - CityID: 16568
          - Population: 18
          - IsRiver: true
          - City: Corinth
          - Religion: Catholicism
          - Route: Railroad
        
        ### 330
        - Type: UnitUpgraded
        - Player: 6: Portugal
        - OldUnit:
          - Level: 4
          - AI: DefenseAir
          - Unit: Triplane
          - ID: 15571
        - NewUnit:
          - Level: 1
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 17425
        
        ### 331
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 6: Portugal
        - OriginalUnit:
          - Level: 4
          - AI: DefenseAir
          - Unit: Triplane
          - ID: 15571
        - NewOwner: 6: Portugal
        - ConvertingUnit:
          - Level: 4
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 17425
        
        ### 332
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Fleet Destroyer
          - ID: 17426
        - Player: 6: Portugal
        - Coast 73,14:
          - Owner: Portugal
        
        ### 333
        - Type: UnitCreated
        - UnitType: Fleet Destroyer
        - Player: 6: Portugal
        - Unit:
          - Level: 1
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17426
        - Coast 73,14:
          - Owner: Portugal
        
        ### 334
        - Type: UnitUpgraded
        - Player: 6: Portugal
        - OldUnit:
          - Level: 4
          - Health: 80%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 16372
        - NewUnit:
          - Level: 1
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17426
        
        ### 335
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 6: Portugal
        - OriginalUnit:
          - Level: 4
          - Health: 80%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 16372
        - NewOwner: 6: Portugal
        - ConvertingUnit:
          - Level: 4
          - Health: 80%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17426
        
        ### 336
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Special Forces
          - ID: 17427
        - Player: 6: Portugal
        - Tundra Hills 25,48:
          - Owner: Portugal
          - Resource: Marble
          - Improvement: Citadel
        
        ### 337
        - Type: UnitCreated
        - UnitType: Special Forces
        - Player: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 17427
        - Tundra Hills 25,48:
          - Owner: Portugal
          - Resource: Marble
          - Improvement: Citadel
        
        ### 338
        - Type: UnitUpgraded
        - Player: 6: Portugal
        - OldUnit:
          - Level: 4
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 16303
        - NewUnit:
          - Level: 1
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 17427
        
        ### 339
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 6: Portugal
        - OriginalUnit:
          - Level: 4
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 16303
        - NewOwner: 6: Portugal
        - ConvertingUnit:
          - Level: 4
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 17427
        
        ### 340
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Special Forces
          - ID: 17428
        - Player: 6: Portugal
        - Grass Land 9,14:
          - Owner: Portugal
          - Improvement: Town
          - Route: Railroad
        
        ### 341
        - Type: UnitCreated
        - UnitType: Special Forces
        - Player: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 17428
        - Grass Land 9,14:
          - Owner: Portugal
          - Improvement: Town
          - Route: Railroad
        
        ### 342
        - Type: UnitUpgraded
        - Player: 6: Portugal
        - OldUnit:
          - Level: 3
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 16314
        - NewUnit:
          - Level: 1
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 17428
        
        ### 343
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 6: Portugal
        - OriginalUnit:
          - Level: 3
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 16314
        - NewOwner: 6: Portugal
        - ConvertingUnit:
          - Level: 3
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 17428
        
        ### 344
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Special Forces
          - ID: 17429
        - Player: 6: Portugal
        - Desert Land 8,11:
          - Owner: Portugal
          - Improvement: Village
          - Route: Railroad
        
        ### 345
        - Type: UnitCreated
        - UnitType: Special Forces
        - Player: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 17429
        - Desert Land 8,11:
          - Owner: Portugal
          - Improvement: Village
          - Route: Railroad
        
        ### 346
        - Type: UnitUpgraded
        - Player: 6: Portugal
        - OldUnit:
          - Level: 2
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 16321
        - NewUnit:
          - Level: 1
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 17429
        
        ### 347
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 6: Portugal
        - OriginalUnit:
          - Level: 2
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 16321
        - NewOwner: 6: Portugal
        - ConvertingUnit:
          - Level: 2
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 17429
        
        ### 348
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 14640
        - Player: 6: Portugal
        - Plots:
          - Plains Land 12,39:
            - Owner: Portugal
            - Route: Railroad
          - Plains Hills 11,39:
            - Owner: Portugal
            - Improvement: Citadel
            - Route: Railroad
          - Plains Hills 10,39:
            - Owner: Portugal
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 9,39:
            - Owner: Portugal
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 9,40:
            - Owner: Portugal
            - Improvement: Farm
          - Tundra Hills 8,41:
            - Owner: Portugal
            - Improvement: Mine
        
        ### 349
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 15170
        - Player: 6: Portugal
        - Plots:
          - Coast 10,10:
            - Owner: Portugal
          - Coast 9,10:
            - Owner: Portugal
          - Plains Land 8,10:
            - Owner: Portugal
            - CityID: 14648
            - Population: 18
            - City: Zanzibar
            - Resource: Jewelry
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Coast 7,10:
            - Owner: Portugal
            - Resource: Coral
            - Improvement: Fishing Boats
          - Coast 6,10:
            - Owner: Portugal
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 350
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16309
        - Player: 6: Portugal
        - Plots:
          - Coast 7,12:
            - Owner: Portugal
          - Coast 6,12:
            - Owner: City-State Shanghai
        
        ### 351
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16245
        - Player: 6: Portugal
        - Plots:
          - Coast 11,17:
            - Owner: Portugal
            - Feature: Atoll
          - Ocean 11,16:
            - Owner: Portugal
          - Coast 10,15:
            - Owner: Portugal
          - Grass Hills 10,14:
            - Owner: Portugal
            - CityID: 12532
            - Population: 18
            - City: Lalibela
            - Resource: Iron
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Grass Land 9,14:
            - Owner: Portugal
            - Improvement: Town
            - Route: Railroad
          - Desert Hills 8,13:
            - Owner: Portugal
            - Improvement: Monolithic Church
            - Route: Railroad
          - Desert Hills 8,12:
            - Owner: Portugal
            - Improvement: Feitoria
            - Route: Railroad
          - Coast 7,11:
            - Owner: Portugal
          - Plains Land 8,10:
            - Owner: Portugal
            - CityID: 14648
            - Population: 18
            - City: Zanzibar
            - Resource: Jewelry
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Coast 9,10:
            - Owner: Portugal
          - Coast 10,10:
            - Owner: Portugal
          - Plains Hills 10,9:
            - Owner: Portugal
            - Improvement: Feitoria
        
        ### 352
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 15688
        - Player: 6: Portugal
        - Plots:
          - Grass Hills 15,24:
            - Owner: Portugal
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 14,23:
            - Owner: Portugal
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 14,22:
            - Owner: Portugal
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 13,22:
            - Owner: Portugal
            - IsRiver: true
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
          - Grass Land 12,22:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 11,22:
            - Owner: Portugal
            - IsRiver: true
            - Improvement: Feitoria
            - Route: Railroad
          - Grass Land 10,21:
            - Owner: Portugal
            - CityID: 14084
            - Population: 20
            - IsRiver: true
            - City: Harar
            - Resource: Cattle
            - Religion: Catholicism
            - Route: Railroad
          - Coast 11,20:
            - Owner: Portugal
          - Coast 10,19:
            - Owner: Portugal
        
        ### 353
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16218
        - Player: 6: Portugal
        - Plots:
          - Plains Land 16,6:
            - Owner: Portugal
            - Improvement: Farm
          - Coast 16,7:
            - Owner: Portugal
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 354
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14600
        - Player: 6: Portugal
        - Desert Hills 10,30:
          - Owner: Portugal
          - IsRiver: true
          - Improvement: Mine
        
        ### 355
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13957
        - Player: 6: Portugal
        - Desert Land 5,27:
          - Owner: Portugal
          - IsRiver: true
          - Improvement: Academy
          - Feature: Flood Plains
        
        ### 356
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16569
        - Player: 6: Portugal
        - Desert Land 9,31:
          - Owner: Portugal
          - IsRiver: true
          - Feature: Flood Plains
        
        ### 357
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17298
        - Player: 6: Portugal
        - Snow Hills 20,41:
          - Owner: Portugal
          - CityID: 1062
          - Population: 37
          - City: Lisbon
          - Religion: Catholicism
          - Route: Railroad
        
        ### 358
        - Type: UnitBuildCompleted
        - Owner: 6: Portugal
        - Unit:
          - Level: 1
          - AI: Archaeologist
          - Unit: Archaeologist
          - ID: 17296
        - Build: Construct an Archaeological Dig
        - Plains Hills 9,33:
          - Owner: Portugal
          - Resource: Antiquity Site
          - Route: Railroad
        
        ### 359
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15115
        - Player: 6: Portugal
        - Plots:
          - Plains Hills 10,39:
            - Owner: Portugal
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 11,39:
            - Owner: Portugal
            - Improvement: Citadel
            - Route: Railroad
          - Plains Land 12,39:
            - Owner: Portugal
            - Route: Railroad
          - Plains Land 13,40:
            - Owner: Portugal
            - Improvement: Farm
          - Tundra Land 12,41:
            - Owner: Portugal
            - IsRiver: true
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Road
          - Tundra Hills 12,42:
            - Owner: City-State Wanggeom
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
        
        ### 360
        - Type: PlayerDoneTurn
        - NextPlayer: 7: Ethiopia
        - Player: 6: Portugal
        
        You, Maria I (leader of Portugal, Player 6), are making strategic decisions after turn 409.
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
    - You are Maria I, leader of Portugal (Player 6).
      
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
      - Name: Portugal
      - Uniques:
        - Unique Unit: Nau, Replacing Caravel (Requires technology: Compass)
        - Unique Unit: Cacador, Replacing Gatling Gun (Requires technology: Dynamite)
        - Unique Building: University of Coimbra, Replacing Imperial College (Requires technology: Education)
        - Unique Improvement: Feitoria (Can be constructed by Workers in owned land to provide yields or by Portuguese-owned Naus (via Sell Exotic Goods) in City-State land.
          In owned land:
          Can only be built on coastal tiles, and cannot be adjacent to another Feitoria.
          In City-State land:
          Provides an untradeable copy of each Luxury Resource type owned by the City-State. Trade Routes to this City-State generate bonus Food and Production based on Gold generated from the Trade Route and relationship with the City-State (i.e. Neutral/Friend/Ally).
          In addition to these bonuses, it provides vision within a 2-tile radius and a +25% Defensive Strength bonus for any Unit stationed in this tile. Contains a Canal, allowing friendly Sea Units to traverse through this tile.); Requires technology: Compass
        - Civilization Ability: For each active Trade Route, receive +4 Gold, Science, and Great Admiral () or Great General () Points, scaling with Era.
      - Leader: Maria I
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
      - Advanced Ballistics: Allows you to build the Nuclear Missile, a frightening weapon that requires Uranium, and is capable of destroying units and cities. Also allows you to build the Guided Missile, an inexpensive single-use Unit that can damage enemy Units, and the SS Booster, one of the Spaceship parts necessary to win a Science Victory.
        Completing it would unlock: Lasers, Stealth
      - Penicillin: All Workers receive the Fallout Reduction Promotion, which reduces the amount of damage they take while scrubbing Fallout. Allows you to build the Marine, a Unit that specializes in amphibious assaults. Also allows you to build the Medical Lab, a building which speeds the growth of your Cities.
        Completing it would unlock: Electronics
      - Satellites: Allow you to build the Apollo Program, a project necessary to win a Science Victory.
        Completing it would unlock: The Internet, Lasers
      
      ## Policies
      - Shadow Networks (Continuing Statecraft Branch):
        - * Receive 25% of Science generated by Allied City-States.
        - * +3% Culture in Capital for every 100 Spy Points ever accumulated (up to 30%).
        - * +3 Science from Constabularies and Police Stations.
        - * +1 Science from Specialists.
      - Universal Suffrage (Level 1 Tenet of Ideology Freedom): Universal Suffrage: A Golden Age begins, and Golden Ages last 50% longer. Cities produce +1 Happiness.
      - Civil Society (Level 1 Tenet of Ideology Freedom): Civil Society: Specialists consume 2 Food less than normal (minimum 1 Food). Farms, Plantations, Camps, and all Unique Improvements produce +4 Food.
      - Draft Registration (Level 1 Tenet of Ideology Freedom): Draft Registration: Military Units purchased with Gold receive full XP.
      - Civilizing Mission (Continuing Imperialism Branch):
        - * Retain all buildings from conquered Cities.
        - * Receive 75 Gold when you conquer a city, scaling with Era and City Population.
        - * +10% Production toward Buildings, with an additional +10% Production per Era difference between your current Era and the building's Era in all Puppeted Cities and Cities with a Courthouse.
      - Economic Union (Level 1 Tenet of Ideology Freedom): Economic Union: Receive two additional Trade Routes. +6 Gold from trade routes with civilizations following Freedom.
      - Entrepreneurship (Continuing Industry Branch):
        - * +1 Happiness from Workshops.
        - * +2 Production and +1 Gold from every Mine, Quarry, and Lumber Mill.
        - * +25% Yields when you expend Great Merchants or Great Engineers for their Instant Yield abilities.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Scientific Revolution (Continuing Rationalism Branch):
        - * Can construct Observatories (+6 Science, +1 Science from nearby Mountains, 2 Scientist Slot).
        - * +2 Science from Jungle and Snow.
      - Covert Action (Level 1 Tenet of Ideology Freedom): Covert Action: Receive 100 Spy Points. When successfully rigging an election in a City-State, the Influence you gain and the Influence other Players lose are increased by +50%. Spies stationed in a foreign City gain +10 Network Points per turn.
      - Avant Garde (Level 1 Tenet of Ideology Freedom): Avant Garde: The rate at which Great People are born is increased by 33%. -2 Unhappiness from Boredom in all Cities.
      - Free Thought (Continuing Rationalism Branch):
        - * -5 Unhappiness from Religious Unrest in all Cities.
        - * +25% Instant Yields from Great Scientists.
        - * Earn Great Scientists +33% faster.
      - Progress (New Branch):
        - Progress is best for civilizations which desire robust infrastructure and scientific advancement.
        - Adopting Progress grants:
        - * Receive 20 Science when a Citizen is born in your Capital and 15 Science for every Citizen already in your Capital, both scaling with Era.
        - * Receive 15 Culture when a Technology is researched, scaling with Era, and for every Technology already unlocked (not scaling with Era).
        - Each Progress policy unlocked grants:
        - * Gain an additional 15 Culture when a Technology is researched, scaling with Era.
        - Adopting all policies in Progress grants:
        - * Unlocks building the Forbidden Palace.
        - * Receive 25 Gold when a Citizen is born in any city, scaling with Era.
        - * Allows for the purchase of Great Writers with Faith starting in the Industrial Era.
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
        - Rationale: We have captured Rhodes and are about to capture Athens, Knossos, and Ephesus from Greece. Civilizing Mission will allow us to retain all buildings from conquered cities and boost production in puppeted and courthouse cities, significantly accelerating the integration and economic value of our newly acquired territories.
        - Policy: Civilizing Mission
    - #1:
      - toolName: set-research
      - args:
        - Rationale: Unlocks Nuclear Missiles, Guided Missiles, and SS Booster. Nuclear Missiles will provide us with a decisive long-range strategic deterrent and the offensive power needed to break the defensive pact alliance of Maya, Netherlands, and France, securing our path to domination.
        - Technology: Advanced Ballistics
    - #2:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Offense: 95
          - Culture: 20
          - Espionage: 40
          - NavalGrowth: 80
          - NavalRecon: 60
          - Gold: 90
          - Happiness: 85
          - Infrastructure: 70
          - Mobile: 85
          - Diplomacy: 10
          - Naval: 75
          - Ranged: 85
          - Production: 95
          - Airlift: 0
          - Antiair: 90
          - MilitaryTraining: 85
          - UseNuke: 50
          - Mobilization: 95
          - Expansion: 0
          - Defense: 70
          - Science: 90
          - GreatPeople: 40
          - NavalTileImprovement: 60
          - Growth: 80
          - Nuke: 80
          - Wonder: 0
          - Recon: 30
          - Air: 95
          - Religion: 0
          - Spaceship: 0
          - CityDefense: 70
          - AirCarrier: 70
          - WaterConnection: 80
          - TileImprovement: 65
      - rationale: Maintain conquest grand strategy as we finish off Greece and prepare for a global nuclear campaign. We are heavily increasing our emphasis on Nuke (80) and UseNuke (50) to reflect our growing atomic bomb arsenal and preparing for tactical nuclear deployment. Production, Offense, and Air remain at maximum priority.
  - tokens:
    - inputTokens: 79944
    - reasoningTokens: 10044
    - outputTokens: 389
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Progress**
            
            My focus has been on assessing our position in Turn 409. As Portugal, I'm pleased to see our leading score of 4030, controlling three capitals: Lisbon, Kyoto, and Addis Ababa. This strategic advantage is crucial as we navigate the Atomic/Information Era.
            
            **Identifying Remaining Capitals**
            
            My thoughts are now zeroing in on the final few capitals. I've accounted for our three, and France holds two. Now I'm working to pinpoint which civs possess the remaining three, as their capture is essential for a Domination victory.
            
            **Evaluating Victory Paths**
            
            My current focus is on analyzing our victory conditions. I've noted that both Maya and Netherlands have achieved a Science Victory. I need to clarify our own research path, as the next step in our tech tree is still being determined, and we have a significant lead in Domination.
            
            **Capturing Critical Capitals**
            
            My immediate attention is on Greece, whom we've decisively weakened. Capturing Athens is paramount, bringing our capital count to four. I'm also strategizing the next moves against France and the Netherlands to secure their capitals and advance our domination victory.
            
            **Analyzing Alliance Dynamics**
            
            My current thoughts are focused on the intricate defensive pacts between France, Maya, and the Netherlands. This alliance presents a significant challenge, as engaging any one of them will inevitably draw us into conflict with all three. I'm also re-evaluating our research path in light of this new information.
            
            **Confirming Research Direction**
            
            I'm confirming that "Advanced Ballistics" is indeed our next research target. It unlocks crucial advancements like Nuclear Missiles, vital for deterrence and offensive capabilities, especially since our current research "Mobile Tactics" will conclude soon. I'm verifying if a manual `set-research` call is needed to lock it in.
            
            **Confirming Uranium Usage**
            
            I'm re-evaluating our Atomic Bomb production, as it seems our stated 1 Uranium is insufficient for the 7 bombs currently in production across multiple cities. I need to confirm how Uranium is actually consumed per bomb and if our captured resources at Rhodes will adequately support this massive build-up.
            
            **Securing Nuclear Capability**
            
            I'm confirming our path to Nuclear Missiles via Advanced Ballistics. I'm also investigating the Uranium discrepancy for Atomic Bomb production, questioning if build completion utilizes resources or if trade/temporary access is involved, and reviewing policy adoption turns as we approach critical ideological decisions.
            
            **Revising Ideology Strategy**
            
            My current thoughts are re-evaluating the choice of "Civilizing Mission" given our ongoing conquests. While it offers significant benefits for building retention and gold acquisition, I need to confirm if its production bonus aligns with our immediate victory goals, especially considering our progress towards critical ideology tenets within Freedom.
            
            **Adopting New Policies**
            
            I'm confirming our current ideology policies within Freedom, noting "Creative Expression" is adopted. My focus is now on the next policy, leaning towards "Civilizing Mission" due to its substantial benefits in retaining conquered city infrastructure and saving production. I'm also ensuring Greece remains maximally hostile as we push for their final cities.
            
            **Assessing Threat Levels**
            
            I'm currently re-evaluating Maya as our primary competitor. Their advanced technology and completion of the Apollo Program, coupled with their defensive pacts with France and the Netherlands, present a formidable challenge. Their combined military strength significantly rivals our own, necessitating a careful approach to avoid a multi-front war.
            
            **Securing Crucial Wonders**
            
            I'm focusing on the imminent capture of Athens and its numerous wonders, which will greatly bolster our empire. Concurrently, I'm planning to secure Knossos, Mycenae, Pharsalos, and Ephesus, solidifying our control over the region and crippling Greece's remaining presence.
            
            **Analyzing World Congress**
            
            I'm confirming that France and Maya have adopted the Order ideology, not Freedom as I initially misread. This significantly changes the dynamics for the upcoming World Congress vote on enacting World Ideology: Freedom. I need to assess how this ideological divergence impacts potential alliances and our path to victory.
            
            **Securing World Ideology**
            
            I'm confirming that France and Maya are Order, while we and Netherlands are Freedom. The proposed "World Ideology: Freedom" is highly beneficial, granting us extra votes and increasing pressure on our rivals. I'm verifying Ethiopia's ideology as our vassal to maximize our voting bloc for this crucial resolution.
            
            **Revising Diplomatic Strategy**
            
            My current thoughts are focused on France's defensive pact with Maya and the Netherlands. Their shared ideology of Order, contrasting with our Freedom, creates significant diplomatic friction. This alliance means attacking any one of them could trigger a conflict with all three, necessitating a revised approach to our offensive operations.
            
            **Analyzing Alliance Dynamics**
            
            My current focus is on the intricate defensive pacts between France, Maya, and the Netherlands. I'm now considering the strategic advantage of potentially breaking this alliance, exploring options like paying them to fight each other or waiting for their pacts to expire, as they currently share declarations of friendship.
            
            **Assessing Great War Readiness**
            
            My primary concern is our readiness for the impending "Great World War" against the France-Maya-Netherlands alliance. While our military strength is slightly lower, our impending Atomic Bomb production across multiple cities gives me confidence that we can overcome their combined forces and achieve a domination victory.
            
            **Launching Nuclear Offensive**
            
            I am confirming our timeline for a devastating nuclear first strike. With Greece nearly conquered within the next 3-5 turns, our seven Atomic Bombs will be ready simultaneously. This allows for a massive global offensive targeting key enemy cities and military concentrations around Turns 415-420.
            
            **Calculating Bomb Reach**
            
            I'm verifying the strike range of our Atomic Bombs, which is 10 tiles. I'm calculating distances from our cities like Porto (23,35) to enemy capitals like Palenque (37,32) and Paris (66,42) to confirm our offensive capabilities.
            
            **Extending Bomb Reach**
            
            I'm recalculating our Atomic Bomb's effective range, realizing rebasing extends it significantly. With cities like Halicarnassus at (73,21), I can now reach Paris (66,42) and potentially other key enemy locations, optimizing our offensive strikes.
            
            **Calculating Bomb Reach**
            
            I'm refining my calculations for atomic bomb reach. While Halicarnassus is too far for Paris, Ouagadougou at (26,26) is now within striking distance of Chichen Itza at (33,30). I am re-evaluating distances to Palenque and considering rebasing options to maximize offensive capabilities.
            
            **Extending Bomb Reach**
            
            I'm recalculating our Atomic Bomb's effective range. Ouagadougou at (26,26) is now within striking distance of Chichen Itza (33,30) and Tikal (33,35). I am also considering the strategic potential of conquering allied City-States like Cahokia (35,42) for advanced launch positions.
            
            **Extending Launch Range**
            
            My current focus is on extending our nuclear strike capabilities. I've identified potential launch sites near France's cities and confirmed that Halicarnassus can strike Dire Dawa. I am now investigating the feasibility of using aircraft carriers for enhanced reach, checking if we have the necessary technologies and units.
            
            **Leveraging Naval Superiority**
            
            My thoughts are now focused on the incredible strategic advantage of our strong navy. With the technology for flight and carriers unlocked, I realize we can deploy our atomic bombs from coastal cities, effectively striking most French and Dutch capitals. This dramatically enhances our offensive reach.
            
            **Maximizing Naval Power**
            
            I'm realizing the immense power of our navy. With numerous battleships and destroyers, we can execute blockades and bombardments on all coastal French and Dutch cities. This naval superiority, combined with our nuclear capabilities, is key to achieving victory.
            
            **Launching Nuclear Offensive**
            
            My focus is on a decisive nuclear strike against France, their weakest link. Capturing Paris and Assur will give us six capitals. While this triggers war with the Netherlands and Maya, our superior navy and atomic bombs will neutralize their threats, allowing a land and naval assault from our eastern cities.
            
            **Revising Alliance Dynamics**
            
            My current focus is on the complex web of alliances. I'm re-evaluating our relationships with France and the Netherlands, aiming to maintain their friendship as long as possible to secure passage for our nuclear strikes, while simultaneously keeping Maya hostile as our primary competitor.
            
            **Clarifying Diplomatic Ties**
            
            I'm correcting my understanding of our diplomatic stance. It turns out I was mistaken; we are friends with Wanggeom and allies with Shanghai, not at war with them. This positive relationship with Wanggeom offers a lucrative trade route and removes a potential conflict, simplifying our strategic outlook.
            
            **Securing Key Allies**
            
            My current focus is on our strong city-state alliances, particularly with Raqmu, Shanghai, and Panama City, which are crucial. I've noted that Copenhagen was lost to the Netherlands, but this is a minor setback given our other robust relationships. I am now confirming the availability and strategic benefit of adopting the "Civilizing Mission" policy to further capitalize on our conquests.
            
            **Adjusting Flavors**
            
            I'm now focused on optimizing our game settings. I've reviewed our current military flavors, noting a strong emphasis on Offense, Mobilization, and Air. I'm considering whether to adjust these or maintain the status quo, especially given our impending nuclear capabilities.
            
            **Updating AI Flavors**
            
            I'm adjusting the AI's strategic priorities. The focus is now on emphasizing nuclear capabilities, increasing "Nuke" to 80 and "UseNuke" to 50, reflecting our transition to a superpower. I'm also ensuring high scores for "Air" and "Production" at 95, and setting the grand strategy to "Conquest" for our domination victory push.
            
            **Updating AI Flavors**
            
            I'm adjusting the AI's strategic priorities. The focus is now on emphasizing nuclear capabilities, increasing "Nuke" to 80 and "UseNuke" to 50, reflecting our transition to a superpower. I'm also ensuring high scores for "Air" and "Production" at 95, and setting the grand strategy to "Conquest" for our domination victory push.
            
            **Confirming Diplomatic Actions**
            
            I'm confirming that no relationship adjustments are needed this turn, as the AI cannot modify city-state relations. My focus is now on executing policy, research, and flavor updates, ensuring all commands are precisely formatted for successful implementation.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 4UIyiuLHjMzGX9lq
          - toolName: set-policy
          - input:
            - Rationale: We have captured Rhodes and are about to capture Athens, Knossos, and Ephesus from Greece. Civilizing Mission will allow us to retain all buildings from conquered cities and boost production in puppeted and courthouse cities, significantly accelerating the integration and economic value of our newly acquired territories.
            - Policy: Civilizing Mission
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: oVpUIAaPrxgUv7ow
          - toolName: set-research
          - input:
            - Rationale: Unlocks Nuclear Missiles, Guided Missiles, and SS Booster. Nuclear Missiles will provide us with a decisive long-range strategic deterrent and the offensive power needed to break the defensive pact alliance of Maya, Netherlands, and France, securing our path to domination.
            - Technology: Advanced Ballistics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: d7av1nC9tuR0Oqrc
          - toolName: set-flavors
          - input:
            - Rationale: Maintain conquest grand strategy as we finish off Greece and prepare for a global nuclear campaign. We are heavily increasing our emphasis on Nuke (80) and UseNuke (50) to reflect our growing atomic bomb arsenal and preparing for tactical nuclear deployment. Production, Offense, and Air remain at maximum priority.
            - GrandStrategy: Conquest
            - Flavors:
              - Offense: 95
              - Culture: 20
              - Espionage: 40
              - NavalGrowth: 80
              - NavalRecon: 60
              - Gold: 90
              - Happiness: 85
              - Infrastructure: 70
              - Mobile: 85
              - Diplomacy: 10
              - Naval: 75
              - Ranged: 85
              - Production: 95
              - Airlift: 0
              - Antiair: 90
              - MilitaryTraining: 85
              - UseNuke: 50
              - Mobilization: 95
              - Expansion: 0
              - Defense: 70
              - Science: 90
              - GreatPeople: 40
              - NavalTileImprovement: 60
              - Growth: 80
              - Nuke: 80
              - Wonder: 0
              - Recon: 30
              - Air: 95
              - Religion: 0
              - Spaceship: 0
              - CityDefense: 70
              - AirCarrier: 70
              - WaterConnection: 80
              - TileImprovement: 65
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 4UIyiuLHjMzGX9lq
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
          - toolCallId: oVpUIAaPrxgUv7ow
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: d7av1nC9tuR0Oqrc
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.