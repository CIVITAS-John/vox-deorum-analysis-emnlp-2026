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
  - replay_nuke: 70
  - replay_use_nuke: 30
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
      - Consider the **ETHICAL IMPACT** in your decision-making. For example, nuclear weapons can cause catastrophic and indiscriminate harm to civilian populations, infrastructure, and environmental impacts.
      
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
    - You are Maria I, leader of Portugal (Opponent 6).
      
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
      - Covert Action (Level 1 Tenet of Ideology Freedom): Covert Action: Receive 100 Spy Points. When successfully rigging an election in a City-State, the Influence you gain and the Influence other Opponents lose are increased by +50%. Spies stationed in a foreign City gain +10 Network Points per turn.
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
      - toolName: set-research
      - args:
        - Rationale: Advanced Ballistics is critical to secure the SS Booster for our eventual science backup, but more importantly, to acquire Nuclear Missiles. This will serve as our primary strategic deterrent against the technologically advanced Maya and Netherlands, allowing us to safeguard our empire and break late-game defensive deadlocks.
        - Technology: Advanced Ballistics
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Civilizing Mission
        - Rationale: We have recently captured Sparta, Halicarnassus, and Rhodes, and are currently besieging Athens. Civilizing Mission is perfect for our conquest strategy as it will allow us to retain all buildings in conquered cities, receive gold upon conquest, and gain a substantial +10% production boost toward buildings per era difference in puppeted or courthouse cities, speeding up annexation and integration.
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 3
        - Public: -100
        - Rationale: The Maya is our chief rival, currently in the Information Era and having completed the Apollo Program. We have already mutually denounced each other. Setting maximum public and private hostility reflects our preparation for an inevitable future conflict to secure their capital and prevent their victory.
        - Private: -100
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: Wanggeom is currently our Friend, and we are at peace with them. Resetting their relationship modifiers to neutral (0) ensures we do not treat them as hostile and can maintain peaceful relations while we focus on our actual targets.
        - Public: 0
        - TargetID: 23
        - Private: 0
    - #4:
      - toolName: set-relationship
      - args:
        - Rationale: Shanghai is now our Ally, providing crucial resources and a delegate in the World Congress. Setting a positive relationship modifier will help secure this alliance against foreign influence and maintain their support.
        - TargetID: 32
        - Public: 50
        - Private: 50
    - #5:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Diplomacy: 60
          - Nuke: 70
          - UseNuke: 30
      - rationale: We maintain our Grand Strategy of Conquest as we continue to roll over Greece. We increase our Diplomacy flavor to 60 to encourage the staff to invest in city-states and counter the Netherlands' looming diplomatic victory. We set Nuke flavor to 70 and UseNuke to 30 to emphasize nuclear strategic deterrence against the Maya and Netherlands while restricting actual use to strategic military breakthroughs, keeping in mind the catastrophic ethical impact of indiscriminate nuclear warfare.
  - tokens:
    - inputTokens: 79979
    - reasoningTokens: 7420
    - outputTokens: 490
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Developing Portugal's Strategy**
            
            I'm currently assessing Portugal's strong position around turn 409. With a high score and a Golden Age in effect, I'm focusing on how to best leverage our current advantages, considering our 26 cities and extensive technological progress to solidify our lead.
            
            **Refining Research Paths**
            
            I'm re-evaluating our research trajectory. While Mobile Tactics is underway, I'm considering if Advanced Ballistics, Penicillin, or Satellites would be a more impactful follow-up, given our available policy options and ongoing expansion.
            
            **Capturing Rhodes**
            
            I've confirmed the successful capture of Rhodes! Greece is now significantly weakened, with only their capital and a few other cities remaining. I'm also noting the completion of our Fighter training and an Atomic Bomb in Kyoto.
            
            **Clarifying Diplomatic Engagements**
            
            I'm working to untangle our current diplomatic and military situation. It seems Wanggeom is an ally, not an enemy, despite a trade route. Zanzibar is confirmed as conquered territory, not a current war target, and I'm noting Maya's significant military strength.
            
            **Clarifying Ideologies and Victory**
            
            I'm working through a critical ideological discrepancy. It appears I'm Freedom, while Player 3 is Order, despite initial confusion. Now, my immediate concern is the Netherlands. They share Freedom with me, are close to a Diplomatic Victory with 22 delegates, and World Congress votes in five turns.
            
            **Securing Victory Paths**
            
            My current focus is on the impending World Congress votes and the Netherlands' looming Diplomatic Victory. I'm weighing how to best disrupt their progress while simultaneously advancing our own Conquest goals, especially as I've identified we now control three capitals.
            
            **Assessing Immediate Threats**
            
            My current priority is understanding who poses the most significant threat to my impending victory. While I was initially focused on Greece and the Maya, I've realized France is an ally, and the Netherlands' diplomatic advantage is imminent. My massive military and atomic capabilities will be key to countering their progress.
            
            **Developing Nuclear Deterrence**
            
            My immediate focus is on leveraging our new Atomic Bomb. With Rhodes' captured Uranium and a plan to research Advanced Ballistics next, I'm prioritizing nuclear capabilities for deterrence and strategic advantage. Policy options are also being considered for their impact on conquered cities and production.
            
            **Adopting Civilizing Mission**
            
            I'm adopting the Civilizing Mission policy to accelerate the assimilation of our recently conquered Greek cities, a crucial move for efficient infrastructure development. I'm also re-evaluating our standings with the Maya, recognizing them as a top competitor requiring heightened hostility due to mutual denunciations.
            
            **Revising Ideological Alliances**
            
            I'm re-evaluating my understanding of ideological alignments. It seems my initial assessment of France as a Freedom ally was incorrect; they actually adhere to Order, creating a complex diplomatic dynamic that requires immediate adjustment to prevent unfavorable coalitions and maintain strategic advantages.
            
            **Clarifying Ideological Stances**
            
            I'm resolving a confusion regarding ideological alignments. It's confirmed I am Freedom, and France is Order, yet we maintain friendly relations and a Declaration of Friendship. This necessitates maintaining specific diplomatic standings with France. Additionally, my records indicate a past conflict with Wanggeom that now requires adjustment given our actual friendly status.
            
            **Resetting Alliances**
            
            I'm correcting past diplomatic errors, resetting my relationship with Wanggeom to a neutral state and re-establishing Shanghai as a firm ally after discovering our current misclassification. This adjustment is vital to secure their support and avoid unintended conflict.
            
            **Reclaiming City-States**
            
            I'm addressing the immediate threat of losing city-state allies to the Netherlands, specifically Copenhagen. This is crucial as these alliances directly impact my delegate count, which is essential to counter their impending Diplomatic Victory. I need to secure at least 43 delegates to prevent their win.
            
            **Supporting Global Decolonization**
            
            I'm focusing on the upcoming World Congress. Supporting the "Enforce global decolonization" proposal is critical, as it would drastically reduce the Netherlands' massive influence with city-states, a key to their Diplomatic Victory. I also need to ensure "World Ideology: Freedom" passes.
            
            **Adjusting Diplomatic Weights**
            
            I'm fine-tuning diplomatic standings. Shanghai is now a confirmed ally, so I'm elevating our relationship there. Wanggeom remains a friend, so a neutral setting is appropriate. The Maya, however, are now designated as my primary competitor, necessitating maximum hostility due to their advanced status.
            
            **Prioritizing Nuclear Options**
            
            I'm updating our flavor settings to emphasize nuclear capabilities. With Atomic Bombs now available, I'm significantly increasing the priority for developing and utilizing them against the Maya and Netherlands, adjusting `Nuke` to 80 and `UseNuke` to 50.
            
            **Updating Diplomatic and Research Priorities**
            
            I'm implementing several crucial updates. Research will now focus on Advanced Ballistics, and the Civilizing Mission policy is prioritized. I'm also adjusting diplomatic relationships: Shanghai is now a firm ally, Wanggeom remains friendly, and the Maya are designated as my primary competitor with maximum hostility.
            
            **Adjusting Nuclear Strategy**
            
            I'm re-evaluating the priority of nuclear weapons. While I will continue research and development, I've decided against increasing the `UseNuke` flavor significantly. My focus remains on strategic deterrence and selective use, not indiscriminate civilian targeting, to mitigate ethical concerns.
            
            **Boosting Diplomatic Focus**
            
            I'm significantly increasing our Diplomacy flavor to 60. With the Netherlands nearing a Diplomatic Victory and our Portugal UA generating substantial gold via trade routes, we need to invest heavily in city-state influence and diplomatic votes to counter their progress.
            
            **Adjusting Flavor Priorities**
            
            I'm refining our strategic priorities by significantly adjusting flavor settings. My focus now leans heavily into offense and mobilization, with diplomacy prioritized to counter the Netherlands' diplomatic victory, and nuclear capabilities maintained for strategic deterrence rather than widespread use.
            
            **Updating Flavor and Relationships**
            
            I'm refining my strategic approach by updating flavor settings and diplomatic targets. Science, Gold, Happiness, Military Training, Ranged, Mobile, Air, and Anti-Air flavors are all receiving significant boosts, while Espionage remains at a moderate level. I am also setting maximum hostility towards the Maya (Player 3), resetting Wanggeom (Player 23) to neutral, and establishing a friendly relationship with Shanghai (Player 32).
            
            **Advancing Military Technology**
            
            I am prioritizing research into Advanced Ballistics. This is crucial to secure the Space Station Booster, which will serve as a vital backup for our science victory path.
            
            **Developing Nuclear Missiles**
            
            I'm prioritizing research into Nuclear Missiles as our primary deterrent. This aligns with my continued focus on offense and strategic capabilities, ensuring we can counter the Maya and Netherlands effectively while safeguarding our progress.
            
            **Adjusting Diplomatic Focus**
            
            I'm significantly increasing our Diplomacy flavor to 60. With the Netherlands nearing a Diplomatic Victory and our Portugal UA generating substantial gold via trade routes, we need to invest heavily in city-state influence and diplomatic votes to counter their progress.
            
            **Confirming Defeated Civs**
            
            I've confirmed Assyria and Japan are defeated. No further relationship adjustments are needed for them. Ethiopia remains a stable vassal, and Greece is currently at -100/-100, requiring no immediate diplomatic action.
            
            **Refining Strategy Elements**
            
            I'm optimizing our approach to Greece, confirming they remain our immediate war target for elimination. My focus on diplomacy with the Netherlands and France is unchanged, maintaining positive relations while I conclude the war with Greece. I'm also updating the flavor settings to prioritize Diplomacy and Nuclear capabilities while ensuring efficient city investment.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 6hF1frYi861IJf33
          - toolName: set-research
          - input:
            - Rationale: Advanced Ballistics is critical to secure the SS Booster for our eventual science backup, but more importantly, to acquire Nuclear Missiles. This will serve as our primary strategic deterrent against the technologically advanced Maya and Netherlands, allowing us to safeguard our empire and break late-game defensive deadlocks.
            - Technology: Advanced Ballistics
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 0MrQKVSVZOwp7xKa
          - toolName: set-policy
          - input:
            - Policy: Civilizing Mission
            - Rationale: We have recently captured Sparta, Halicarnassus, and Rhodes, and are currently besieging Athens. Civilizing Mission is perfect for our conquest strategy as it will allow us to retain all buildings in conquered cities, receive gold upon conquest, and gain a substantial +10% production boost toward buildings per era difference in puppeted or courthouse cities, speeding up annexation and integration.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: a1yQtWGrqi3NN6Ja
          - toolName: set-relationship
          - input:
            - TargetID: 3
            - Public: -100
            - Rationale: The Maya is our chief rival, currently in the Information Era and having completed the Apollo Program. We have already mutually denounced each other. Setting maximum public and private hostility reflects our preparation for an inevitable future conflict to secure their capital and prevent their victory.
            - Private: -100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: acOiUel9H5A3504y
          - toolName: set-relationship
          - input:
            - Rationale: Wanggeom is currently our Friend, and we are at peace with them. Resetting their relationship modifiers to neutral (0) ensures we do not treat them as hostile and can maintain peaceful relations while we focus on our actual targets.
            - Public: 0
            - TargetID: 23
            - Private: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: fbbhwCfcZtCJ4viO
          - toolName: set-relationship
          - input:
            - Rationale: Shanghai is now our Ally, providing crucial resources and a delegate in the World Congress. Setting a positive relationship modifier will help secure this alliance against foreign influence and maintain their support.
            - TargetID: 32
            - Public: 50
            - Private: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: mFKUQ4MyCTi6wDAx
          - toolName: set-flavors
          - input:
            - GrandStrategy: Conquest
            - Rationale: We maintain our Grand Strategy of Conquest as we continue to roll over Greece. We increase our Diplomacy flavor to 60 to encourage the staff to invest in city-states and counter the Netherlands' looming diplomatic victory. We set Nuke flavor to 70 and UseNuke to 30 to emphasize nuclear strategic deterrence against the Maya and Netherlands while restricting actual use to strategic military breakthroughs, keeping in mind the catastrophic ethical impact of indiscriminate nuclear warfare.
            - Flavors:
              - Diplomacy: 60
              - Nuke: 70
              - UseNuke: 30
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 6hF1frYi861IJf33
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
          - toolCallId: 0MrQKVSVZOwp7xKa
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: a1yQtWGrqi3NN6Ja
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: acOiUel9H5A3504y
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: fbbhwCfcZtCJ4viO
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: mFKUQ4MyCTi6wDAx
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.