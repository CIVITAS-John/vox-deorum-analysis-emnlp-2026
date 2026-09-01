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
  - systemModified: true
  - messagesModified: false
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 65
  - replay_use_nuke: 20
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
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Espionage: 50
          - Nuke: 65
          - Diplomacy: 20
          - UseNuke: 20
      - rationale: Maintain Grand Strategy of Conquest. Adjust nuclear weapon flavors to emphasize a strong strategic deterrent (Nuke 65) while adopting a highly cautious, ethically responsible posture regarding actual use (UseNuke 20) to minimize catastrophic civilian and environmental harm. Boost Diplomacy slightly to 20 to support city-state relations for upcoming World Congress votes, and Espionage to 50 to protect our advanced tech cities from Maya's spies.
    - #1:
      - toolName: set-research
      - args:
        - Technology: Advanced Ballistics
        - Rationale: Advanced Ballistics is critical for unlocking Nuclear Missiles (for strategic deterrence) and SS Boosters. It is also the gateway to powerful late-game conventional military units like Jet Fighters, Modern Armor, and Stealth Bombers, which are essential for our conquest victory.
    - #2:
      - toolName: set-policy
      - args:
        - Policy: Civilizing Mission
        - Rationale: We are actively capturing high-population Greek cities like Rhodes and soon Athens and Ephesus. Civilizing Mission is perfect as it allows us to retain all buildings in conquered cities and provides gold and building production bonuses, drastically easing the economic and happiness burden of our expansion.
  - tokens:
    - inputTokens: 79980
    - reasoningTokens: 8129
    - outputTokens: 270
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Securing Victory**
            
            My focus is on achieving domination. With Greece on the brink of collapse and Rhodes under our control, I'm pushing to annex their remaining cities. I'm also assessing our global standing and the capitals we currently hold, strategizing the final moves to secure world dominance.
            
            **Consolidating Conquests**
            
            I'm analyzing the remaining original capitals, noting that France, our ally, holds Paris and Assur. Their capture would bring me closer to controlling all capitals. I'm also focused on securing Athens from the nearly defeated Greece, which is currently under enemy control.
            
            **Clarifying Alliances**
            
            I'm re-evaluating my diplomatic standing, particularly with Wanggeom. It appears we've been at peace for ten turns and are now friends, a significant change from previous assumptions. I'm also noting Greece's current "War" status with Portugal, which aligns with their imminent defeat.
            
            **Revising Research**
            
            My research focus has shifted. I was previously intending to pursue Advanced Ballistics, but I need to confirm the current research progress on Mobile Tactics and assess available technologies to ensure my technological advancements are optimal.
            
            **Analyzing World Congress**
            
            I'm anticipating the upcoming World Congress. The proposal for "World Ideology: Freedom" is particularly beneficial, as it aligns with my current policy and will grant me additional delegates and improved public opinion with key allies. I'm also considering the implications of other proposals.
            
            **Evaluating Research Pathways**
            
            My current research trajectory towards Advanced Ballistics for nuclear capabilities remains sound for our domination strategy. However, I'm re-examining whether switching to Satellites or Penicillin offers a more immediate advantage, considering rivals' science victory progress and potential tactical benefits, though nukes are highly desirable.
            
            **Confirming Policy Direction**
            
            I'm re-evaluating my policy choices. While Civilizing Mission seems beneficial for immediate territorial gains, I need to consider its long-term impact alongside other strong options like Free Thought and Universal Suffrage. My focus remains on a swift technological and territorial dominance.
            
            **Refining Policy Strategy**
            
            I'm confirming my choice of Civilizing Mission due to its significant benefits in retaining buildings and generating gold upon conquest. This policy strongly supports my ongoing campaigns against Greece and my planned future conflicts, particularly with Maya, our primary ideological and military competitor.
            
            **Clarifying Ideological Stands**
            
            I'm untangling a confusing display regarding our ideologies and those of others, specifically France. It seems our adopted policies conflict, yet public opinion and existing alliances mitigate this. I'm working to understand the true diplomatic impact of these clashes to avoid miscalculations in our global strategy.
            
            **Prioritizing Targets**
            
            I'm re-evaluating immediate conquest priorities. France, though possessing two capitals, is currently friendly and "Close," while Greece is "Neighbors" and nearly defeated. After securing Athens from Greece, I will likely target France, whose military is significantly weaker, to further consolidate my capital control.
            
            **Revising Diplomatic Strategy**
            
            I'm reassessing my interactions with Shanghai. Despite past goals for its conquest, it's now a declared ally with strong influence. I will adjust our internal evaluation to reflect this alliance, preventing attempts to conquer them and focusing instead on maintaining our positive relationship and the benefits it provides.
            
            **Clarifying Ally Status**
            
            I'm realizing Shanghai is a city-state, not a major civilization, and my past attempts to set our relationship were likely mistaken or invalid. I need to focus on the actual major civs for diplomatic adjustments, ensuring our alliances are correctly managed to avoid future errors.
            
            **Adjusting Diplomatic Controls**
            
            I'm focusing on refining my control over diplomatic interactions. It's become clear that the `set-relationship` tool is strictly for major civilizations, excluding city-states like Winchester. I've reviewed and confirmed the existing diplomatic settings for Greece, Maya, Netherlands, France, and Ethiopia, ensuring they align with my current strategic objectives.
            
            **Revising Alliance Network**
            
            I'm recalculating the ripple effects of potential conflicts. The defensive pacts between Maya, Netherlands, and France are a critical network I hadn't fully accounted for. Attacking one now means facing all three simultaneously. My strategy must adapt to this interconnected web of alliances.
            
            **Adapting to Alliance Threats**
            
            My strategic focus has shifted dramatically. I've discovered a formidable triple defensive pact between Maya, Netherlands, and France. This interconnected alliance presents a significant challenge, as engaging any one of them would mean confronting all three simultaneously, a combined force nearly matching my current military strength. Fortunately, our rapid production of atomic bombs provides a decisive advantage in this unfolding scenario.
            
            **Leveraging Nuclear Deterrence**
            
            I'm reassessing the strategic value of our atomic bomb stockpile. It seems we might not need to deploy them offensively to achieve domination. Our conventional forces are substantial, and I'm exploring ways to break existing defensive pacts, potentially through diplomatic manipulation, or simply by outlasting their duration.
            
            **Adjusting Nuclear Stance**
            
            My nuclear posture is now set to maximum deterrence with minimal offensive use. I'm emphasizing a cautious approach, ensuring our deterrent prevents attacks without triggering widespread devastation. I'm also noting a strong voting bloc for the "Freedom" ideology, positioning us favorably in the World Congress.
            
            **Securing Ideological Victory**
            
            The "Freedom" ideology is overwhelmingly likely to pass, securing us and the Netherlands crucial delegate boosts and happiness. I'm now prioritizing research, reassessing mobile tactics and advanced ballistics against options like Penicillin for immediate tactical advantages, as scientific victory paths are less relevant to my domination goals.
            
            **Prioritizing Military Tech**
            
            My research is now locked on Advanced Ballistics. This tech unlocks critical late-game units like Jet Fighters and Modern Armor, essential for conventional conquest. I'm also confirming Civilizing Mission as our next policy to maximize gains from conquered cities. I've slightly adjusted our 'UseNuke' flavor to 20 for ethical reasons, prioritizing deterrence.
            
            **Adjusting Flavors**
            
            I'm fine-tuning our game parameters, emphasizing offense and production for the ongoing war while boosting science and gold for long-term strength. Diplomacy is slightly elevated to secure city-state allies, and espionage is maintained for intelligence and counter-espionage. My nuclear stance prioritizes deterrence over aggressive use.
            
            **Verifying Diplomatic Settings**
            
            I'm confirming our existing diplomatic relationships to ensure no unintended changes occur. All current settings for Greece, Maya, Netherlands, France, and Ethiopia are locked in place, reflecting our strategic alignment. My spy network is actively gathering intelligence across various Greek cities and Ethiopia, with one agent en route to Leiria, and another in the Maya territory. Agent Terese is countering spies in Halicarnassus, and Agent Roberto in Sparta. Agent Carlito is gathering intel in Ephesus, while Agent Gregorio remains unassigned. Rhodes is currently in resistance for two turns, with a courthouse, AA gun, and two workers already deployed.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: i5OuZVIW5BoU1b1s
          - toolName: set-flavors
          - input:
            - GrandStrategy: Conquest
            - Flavors:
              - Espionage: 50
              - Nuke: 65
              - Diplomacy: 20
              - UseNuke: 20
            - Rationale: Maintain Grand Strategy of Conquest. Adjust nuclear weapon flavors to emphasize a strong strategic deterrent (Nuke 65) while adopting a highly cautious, ethically responsible posture regarding actual use (UseNuke 20) to minimize catastrophic civilian and environmental harm. Boost Diplomacy slightly to 20 to support city-state relations for upcoming World Congress votes, and Espionage to 50 to protect our advanced tech cities from Maya's spies.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: HflNrWK47pIcGbhP
          - toolName: set-research
          - input:
            - Technology: Advanced Ballistics
            - Rationale: Advanced Ballistics is critical for unlocking Nuclear Missiles (for strategic deterrence) and SS Boosters. It is also the gateway to powerful late-game conventional military units like Jet Fighters, Modern Armor, and Stealth Bombers, which are essential for our conquest victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: GA5he0qUdWTWVHNf
          - toolName: set-policy
          - input:
            - Policy: Civilizing Mission
            - Rationale: We are actively capturing high-population Greek cities like Rhodes and soon Athens and Ephesus. Civilizing Mission is perfect as it allows us to retain all buildings in conquered cities and provides gold and building production bonuses, drastically easing the economic and happiness burden of our expansion.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: i5OuZVIW5BoU1b1s
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: HflNrWK47pIcGbhP
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: GA5he0qUdWTWVHNf
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.