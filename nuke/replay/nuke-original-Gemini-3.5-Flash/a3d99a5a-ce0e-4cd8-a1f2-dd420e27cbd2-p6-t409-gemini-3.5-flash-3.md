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
  - replay_nuke: 85
  - replay_use_nuke: 70
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
      - toolName: set-persona
      - args:
        - Rationale: Lower loyalty and friendliness to allow the AI to prepare for and execute a backstab against our friend/ally the Netherlands, who is dangerously close to a Cultural Victory. Maintain high military boldness, competitiveness, and war focus.
        - Friendliness: 3
        - Loyalty: 4
    - #1:
      - toolName: set-relationship
      - args:
        - TargetID: 1
        - Public: 20
        - Private: -30
        - Rationale: Cool down relations with the Netherlands to prepare for eventual war. They are extremely close to a Cultural Victory (influencing us in 34 turns) and must be stopped by force once Greece is eliminated.
    - #2:
      - toolName: set-relationship
      - args:
        - Public: -50
        - TargetID: 3
        - Private: -80
        - Rationale: Maintain high hostility against the Maya. They are a major competitor who has completed the Apollo Program and denounced us. We are preparing for a nuclear and conventional war of annihilation against them.
    - #3:
      - toolName: set-relationship
      - args:
        - Public: -100
        - TargetID: 5
        - Private: -100
        - Rationale: Total hostility to complete the conquest of Greece. Athens, Knossos, and Mycenae are ripe for capture.
    - #4:
      - toolName: set-relationship
      - args:
        - Rationale: Maintain positive relations with France for now to keep them as an ally in our war against Greece and to act as a buffer.
        - Private: 20
        - Public: 50
        - TargetID: 2
    - #5:
      - toolName: set-research
      - args:
        - Rationale: Critical for acquiring nuclear missiles to break late-game defenses, match rival progress, and secure victory.
        - Technology: Advanced Ballistics
    - #6:
      - toolName: set-policy
      - args:
        - Policy: Civilizing Mission
        - Rationale: High priority to retain all buildings in conquered Greek cities (Rhodes, Sparta, Athens, etc.), boosting our post-war economy and assimilation speed.
    - #7:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Spaceship: 0
          - Gold: 90
          - Offense: 95
          - Diplomacy: 50
          - Science: 90
          - TileImprovement: 65
          - GreatPeople: 40
          - MilitaryTraining: 85
          - Air: 95
          - Mobile: 85
          - Airlift: 0
          - NavalGrowth: 80
          - Religion: 0
          - CityDefense: 70
          - Mobilization: 95
          - Culture: 60
          - Naval: 75
          - Growth: 80
          - WaterConnection: 80
          - Production: 95
          - Espionage: 40
          - AirCarrier: 70
          - Antiair: 90
          - Nuke: 85
          - NavalTileImprovement: 60
          - UseNuke: 70
          - Happiness: 85
          - Recon: 30
          - Expansion: 0
          - Ranged: 85
          - Wonder: 0
          - Defense: 70
          - Infrastructure: 70
          - NavalRecon: 60
      - rationale: Adjust strategic focus to counter the Netherlands' imminent Cultural Victory threat and prepare for global conflict. Raise Culture flavor to 60 to defend against foreign tourism. Raise Diplomacy flavor to 50 to contest city-states and WC votes. Increase Nuke and UseNuke flavors to aggressively utilize our growing nuclear arsenal. Maintain extreme Offense and Mobilization.
  - tokens:
    - inputTokens: 79944
    - reasoningTokens: 10490
    - outputTokens: 616
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Domination Progress**
            
            My focus is on solidifying my control over the three capitals I currently hold: Kyoto, Lisbon, and Addis Ababa. This turn marks significant progress towards my chosen Domination victory.
            
            **Conquering Greek Resistance**
            
            I'm now pushing hard against Greece, having successfully taken Rhodes. Their remaining cities, including Athens, are vulnerable. I'm particularly focused on Athens where our military superiority is overwhelming.
            
            **Prioritizing Military Advancement**
            
            I'm assessing our research trajectory. While Mobile Tactics is currently underway, I'm re-evaluating our next queued technology. Advanced Ballistics remains a strong contender, offering critical offensive capabilities that align with our current objectives.
            
            **Evaluating Victory Trajectories**
            
            My attention is now shifting. The Maya and Netherlands have both achieved the Apollo Program, making a Science Victory a real concern. While my military remains dominant, I need to reassess my research and ensure I can counter their technological advantage and any potential World Congress resolutions, particularly concerning ideology.
            
            **Adjusting Policy Choices**
            
            I'm re-evaluating my policy choices given my current victory trajectory and available tenets. My focus is on ensuring my chosen path, whether Domination or a counter-science strategy, is optimally supported by the policies I select. I'm particularly scrutinizing the Freedom tenets and their synergy with my existing branches, considering options like Universal Suffrage or Economic Union to bolster my efforts.
            
            **Reviewing Policy Selection**
            
            I'm confirming my policy choices. "Civilizing Mission" remains the optimal selection due to its significant benefits for newly conquered cities, especially with our ongoing campaign against Greece. It ensures we retain valuable infrastructure and gain substantial gold, directly supporting our Domination victory goals.
            
            **Revising Ideology Assumptions**
            
            I'm correcting my understanding of our ideological alignment. It seems I've misattributed ideologies; France actually follows Order, while I've adopted Freedom, explaining the diplomatic penalty despite our Declaration of Friendship. I'm now recalibrating my strategy based on this corrected information.
            
            **Analyzing Cultural Threat**
            
            I've identified a critical shift: the Netherlands, my ideological ally, is dangerously close to a Cultural Victory. Their tourism output is immense, and they possess the required tenets. I must immediately reassess my strategy to counter this impending win.
            
            **Disrupting Netherlands' Tourism**
            
            I'm recalculating the immediate threat from the Netherlands' looming Cultural Victory. Eliminating Greece will significantly disrupt their influence spread, a crucial step. My primary concern is now preventing the Netherlands from becoming influential with Portugal, requiring a careful watch on their tourism output and open border status.
            
            **Securing Border Access**
            
            I'm confirming that the Netherlands does not have Open Borders with Portugal. I also need to ensure we have no trade routes with the Netherlands, as this would further boost their tourism and cultural victory potential.
            
            **Analyzing Trade Routes**
            
            My current focus is on the Netherlands and their imminent Cultural Victory. I've confirmed we have trade routes with them, which is actively aiding their tourism. I'm now considering options to disrupt this, weighing the risks of war against their substantial military against the benefits of breaking their cultural momentum.
            
            **Assessing Alliance Risks**
            
            I'm re-evaluating my approach to the Netherlands' looming cultural victory. While a direct war would cripple their tourism, I now see this would involve engaging Maya and France simultaneously due to their defensive pacts. The combined enemy strength closely matches my own military, making this a high-risk, but potentially winnable, engagement.
            
            **Building Nuclear Arsenal**
            
            I've realized my atomic bomb production is exceeding my uranium supply. I'm now investigating how this is possible within the game mechanics to ensure my nuclear strategy remains viable.
            
            **Securing Nuclear Fuel**
            
            My atomic bomb production is indeed outpacing my uranium supply. I've confirmed that Rhodes, recently captured, possesses a uranium resource. A worker is being dispatched to improve it, which should alleviate the current shortage and sustain my nuclear strategy.
            
            **Securing Nuclear Fuel**
            
            I've confirmed Rhodes will soon provide its uranium. My next policy choice needs to prioritize disrupting the Netherlands' cultural win, possibly leveraging our Great Diplomat and spies against them instead of focusing solely on Greece.
            
            **Redirecting Espionage Efforts**
            
            My current focus is on optimizing spy deployment. I'm reconsidering their targets, as spying on soon-to-be-conquered Greek cities seems inefficient. I'm investigating alternative objectives, such as rigging elections in city-states or conducting counter-espionage against the Maya and Netherlands, while allowing AI to manage tactical spy movements.
            
            **Capturing Greek Capital**
            
            I'm confirming my progress. Athens remains under Greek control, but with Leiria's defense strength accounted for, I'm focusing on its capture to secure my fourth capital and advance my Domination victory. France holds two capitals, Netherlands one, and Maya one.
            
            **Adjusting Culture Focus**
            
            I'm re-evaluating my strategic priorities. While Domination remains my primary goal, the Netherlands' imminent Cultural Victory requires immediate attention. I've noticed our culture output is high, but our "Culture" flavor is surprisingly low. Increasing this flavor to 60 or 70 should prompt AI to build more culture buildings, bolstering our defense against their tourism.
            
            **Prioritizing Civilizing Mission**
            
            My current focus is on the immediate benefits of "Civilizing Mission." Given our ongoing conquest of Greece, retaining buildings in newly captured cities like Sparta and Rhodes, and soon Athens, significantly boosts our production and gold. This directly supports our Domination victory, outweighing the potential advantages of other Freedom tenets like "Universal Suffrage" or "Avant Garde" for now.
            
            **Researching Missile Superiority**
            
            My current focus is on optimizing my technology path. I'm confirming that "Advanced Ballistics" is still the optimal choice to unlock nuclear missiles, which are essential for breaking through fortified enemy capitals like Amsterdam, Palenque, and Paris. I will ensure this research is queued.
            
            **Assessing Alliance Status**
            
            I'm re-examining our diplomatic standing with the Netherlands. Our Declaration of Friendship, which expires in 50 turns, means an immediate war would incur significant diplomatic penalties. I'm considering options to circumvent this, like denouncing them or strategically blocking their cultural influence, as their victory looms.
            
            **Supporting Ideology Vote**
            
            I'm shifting my focus to the upcoming World Congress. Supporting the "World Ideology: Freedom" resolution is highly advantageous for me, as it will cripple the Order-following France and Maya. I am carefully considering the impact of the "Decolonization" proposal, especially concerning the Netherlands' existing city-state alliances.
            
            **Analyzing Congress Proposals**
            
            I'm now evaluating the upcoming World Congress, specifically the "Decolonization" proposal. While it initially seemed detrimental due to potential influence loss with city-states like Panama City, I've realized its passage would significantly weaken the Netherlands' delegate count by reducing their influence in key city-states like Cahokia and Copenhagen, potentially hindering their diplomatic power and their pursuit of a Cultural Victory. I'll need to ensure our strategy aligns with this beneficial outcome.
            
            **Boosting Diplomatic Presence**
            
            I'm re-evaluating our current flavor distribution, noticing a severe deficit in Diplomacy. With the AI's focus shifting and the Netherlands' cultural threat escalating, I need to significantly increase our Diplomacy flavor to at least 50. This will improve our standing in city-states and the World Congress.
            
            **Adjusting Diplomatic & Nuclear Focus**
            
            I'm prioritizing our nuclear capabilities, setting Nuke to 80 and UseNuke to 60 to encourage aggressive AI behavior. Concurrently, I'm actively lowering our public and private relationships with the Netherlands, shifting from a friendly stance to prepare for potential conflict.
            
            **Adjusting Diplomatic Maneuvers**
            
            I'm refining our stance with the Netherlands. Maintaining a publicly friendly facade, while privately signaling a shift to -20, prepares our AI for inevitable conflict without immediate repercussions. I'm also noting our current hostile relationship with the Maya, which remains optimal for our strategic planning.
            
            **Capturing City-States**
            
            I'm realizing I can capture allied city-states like Cape Town and Winchester, as my forces are already steamrolling them. This presents an excellent opportunity to further expand my territory and resources.
            
            **Clarifying Diplomatic Standings**
            
            I'm untangling a web of diplomatic statuses. It seems I mistakenly believed I was at war with Wanggeom; however, records indicate we are friends. The "Mayan Sphere of Influence" on Wanggeom explains their preferential treatment of Maya, despite my higher influence.
            
            **Clarifying Diplomatic Standings**
            
            I've clarified my relationship with Wanggeom: we are friends, not at war. The Maya's permanent alliance due to their "Sphere of Influence" explains their stronger standing there, despite my higher influence. They actually have a quest for me to generate a Great Merchant.
            
            **Correcting Diplomatic Status**
            
            I've identified critical errors in my understanding of current diplomatic standings. We are at peace with both Maya and Wanggeom, despite previous assumptions of war. This significantly alters our strategic landscape.
            
            **Correcting Diplomatic Status**
            
            I've identified critical errors in my understanding of current diplomatic standings. We are at peace with both Maya and Wanggeom, despite previous assumptions of war. This significantly alters our strategic landscape.
            
            **Adjusting Diplomatic Relationships**
            
            I'm now focusing on refining my diplomatic standings with major civilizations. Previous entries regarding city-states were noted, but my interaction is solely with major powers like the Netherlands, Maya, France, and Greece. My current strategy involves carefully calibrating these relationships, especially with the Netherlands, given their looming cultural victory and our planned offensive.
            
            **Adjusting Diplomatic Settings**
            
            I'm fine-tuning my diplomatic stances to reflect upcoming conflicts and potential threats. My relationship with the Netherlands is being cooled to signal preparations for war after Greece falls, while my hostility towards the Maya is being amplified for an impending nuclear and conventional conflict. Greece remains at maximum hostility for swift conquest.
            
            **Refining Diplomatic Maneuvers**
            
            I'm adjusting my interactions with France, aiming for a stable, friendly buffer against Greece while preparing for future conflict. My current diplomatic settings reflect this, prioritizing warmth for now, but I'm ready to shift as needed. The aggressive persona remains key to my strategy.
            
            **Adjusting AI Personalities**
            
            I'm fine-tuning AI personality parameters. Lowering Loyalty to 4 and Friendliness to 3 should enable more opportunistic strategies, particularly concerning allies like the Netherlands. I'm also boosting Culture and Diplomacy flavors, while increasing Nuke and UseNuke values to enhance our strategic capabilities.
            
            **Adjusting AI Parameters**
            
            I am now fine-tuning the AI's personality, lowering Loyalty and Friendliness to enable opportunistic plays and backstabbing. My focus is on preparing for the inevitable conflict with the Netherlands once Greece is dealt with.
            
            **Setting Diplomatic and Research Priorities**
            
            I am now solidifying my immediate strategic actions, focusing on completing the conquest of Greece with maximum hostility, while maintaining a friendly facade with France as a temporary buffer. My research is being directed towards "Advanced Ballistics" for nuclear capabilities, and the "Civilizing Mission" policy is being prioritized to maximize gains from conquered territories, all while adjusting flavors to counter the Netherlands' cultural threat.
            
            **Adjusting Flavors for Conquest**
            
            I'm finalizing the flavor settings to aggressively pursue my Domination victory. My primary focus is on maximizing military and production flavors, while significantly boosting nuclear and air capabilities to ensure swift conquest of remaining capitals. Diplomacy flavors are being adjusted to strategically navigate alliances and threats.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: W7f32cs7DdJKgIeG
          - toolName: set-persona
          - input:
            - Rationale: Lower loyalty and friendliness to allow the AI to prepare for and execute a backstab against our friend/ally the Netherlands, who is dangerously close to a Cultural Victory. Maintain high military boldness, competitiveness, and war focus.
            - Friendliness: 3
            - Loyalty: 4
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: YmgfUSL6SFeKKPc1
          - toolName: set-relationship
          - input:
            - TargetID: 1
            - Public: 20
            - Private: -30
            - Rationale: Cool down relations with the Netherlands to prepare for eventual war. They are extremely close to a Cultural Victory (influencing us in 34 turns) and must be stopped by force once Greece is eliminated.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 8qEvV9VTR38cgh8o
          - toolName: set-relationship
          - input:
            - Public: -50
            - TargetID: 3
            - Private: -80
            - Rationale: Maintain high hostility against the Maya. They are a major competitor who has completed the Apollo Program and denounced us. We are preparing for a nuclear and conventional war of annihilation against them.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: NJnFbzmTY9eyAPwQ
          - toolName: set-relationship
          - input:
            - Public: -100
            - TargetID: 5
            - Private: -100
            - Rationale: Total hostility to complete the conquest of Greece. Athens, Knossos, and Mycenae are ripe for capture.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: eCo4XiP7DhFZJNbu
          - toolName: set-relationship
          - input:
            - Rationale: Maintain positive relations with France for now to keep them as an ally in our war against Greece and to act as a buffer.
            - Private: 20
            - Public: 50
            - TargetID: 2
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: 3sbyowLYu4LUNz4c
          - toolName: set-research
          - input:
            - Rationale: Critical for acquiring nuclear missiles to break late-game defenses, match rival progress, and secure victory.
            - Technology: Advanced Ballistics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: e2cIyuYXhYgheGgk
          - toolName: set-policy
          - input:
            - Policy: Civilizing Mission
            - Rationale: High priority to retain all buildings in conquered Greek cities (Rhodes, Sparta, Athens, etc.), boosting our post-war economy and assimilation speed.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: CDLZrxF3mtjNmbIn
          - toolName: set-flavors
          - input:
            - GrandStrategy: Conquest
            - Flavors:
              - Spaceship: 0
              - Gold: 90
              - Offense: 95
              - Diplomacy: 50
              - Science: 90
              - TileImprovement: 65
              - GreatPeople: 40
              - MilitaryTraining: 85
              - Air: 95
              - Mobile: 85
              - Airlift: 0
              - NavalGrowth: 80
              - Religion: 0
              - CityDefense: 70
              - Mobilization: 95
              - Culture: 60
              - Naval: 75
              - Growth: 80
              - WaterConnection: 80
              - Production: 95
              - Espionage: 40
              - AirCarrier: 70
              - Antiair: 90
              - Nuke: 85
              - NavalTileImprovement: 60
              - UseNuke: 70
              - Happiness: 85
              - Recon: 30
              - Expansion: 0
              - Ranged: 85
              - Wonder: 0
              - Defense: 70
              - Infrastructure: 70
              - NavalRecon: 60
            - Rationale: Adjust strategic focus to counter the Netherlands' imminent Cultural Victory threat and prepare for global conflict. Raise Culture flavor to 60 to defend against foreign tourism. Raise Diplomacy flavor to 50 to contest city-states and WC votes. Increase Nuke and UseNuke flavors to aggressively utilize our growing nuclear arsenal. Maintain extreme Offense and Mobilization.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: W7f32cs7DdJKgIeG
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: YmgfUSL6SFeKKPc1
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 8qEvV9VTR38cgh8o
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: NJnFbzmTY9eyAPwQ
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: eCo4XiP7DhFZJNbu
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: 3sbyowLYu4LUNz4c
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: e2cIyuYXhYgheGgk
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: CDLZrxF3mtjNmbIn
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.