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
  - messagesModified: true
  - activeToolsModified: true
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 95
  - replay_use_nuke: 80
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
          - WaterConnection: 80
          - TileImprovement: 65
          - Diplomacy: 50
          - Ranged: 85
          - Growth: 80
          - Offense: 95
          - Air: 95
          - MilitaryTraining: 85
          - Antiair: 90
          - NavalTileImprovement: 60
          - GreatPeople: 40
          - CityDefense: 70
          - Recon: 30
          - Nuke: 95
          - AirCarrier: 70
          - Production: 95
          - Religion: 0
          - Expansion: 0
          - Airlift: 0
          - Culture: 70
          - Naval: 75
          - Happiness: 85
          - NavalRecon: 60
          - Gold: 90
          - Infrastructure: 70
          - Defense: 70
          - Science: 90
          - Wonder: 0
          - Espionage: 40
          - Mobile: 85
          - UseNuke: 80
          - Spaceship: 0
          - Mobilization: 95
          - NavalGrowth: 80
      - rationale: We are actively steamrolling Greece and building a massive arsenal of Atomic Bombs. We increase Nuke and UseNuke flavors to maximize our nuclear deployment. We also increase Culture and Diplomacy flavors to defend against the Netherlands' imminent cultural and diplomatic victory threats.
    - #1:
      - toolName: set-research
      - args:
        - Technology: Advanced Ballistics
        - Rationale: Advanced Ballistics is critical to unlock Nuclear Missiles and Guided Missiles to support our global conquest strategy.
    - #2:
      - toolName: set-policy
      - args:
        - Policy: Civilizing Mission
        - Rationale: We are actively capturing Greek cities, so retaining all buildings in conquered cities is extremely valuable to maintain our economy and avoid happiness penalties.
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 50
        - Private: 50
        - Rationale: Keep the Netherlands friendly while we finish off Greece, but stay vigilant as they are close to a cultural/diplomatic victory.
        - TargetID: 1
    - #4:
      - toolName: set-relationship
      - args:
        - Rationale: Maintain friendly relations with France as a strong ally and trading partner.
        - TargetID: 2
        - Private: 50
        - Public: 50
    - #5:
      - toolName: set-relationship
      - args:
        - Public: -50
        - TargetID: 3
        - Private: -100
        - Rationale: The Maya are our main competitor and are hostile/denounced. We will target them after Greece.
    - #6:
      - toolName: set-relationship
      - args:
        - Public: -100
        - Rationale: Greece is our active war target. We are steamrolling them and aim to completely eliminate them to secure domination and remove their votes from the World Congress.
        - Private: -100
        - TargetID: 5
    - #7:
      - toolName: set-relationship
      - args:
        - Public: 50
        - TargetID: 7
        - Private: 50
        - Rationale: Ethiopia is our capitulated vassal who is now highly loyal and cooperative. We want to maintain a strong master-vassal relationship to leverage their support.
  - tokens:
    - inputTokens: 79028
    - reasoningTokens: 9997
    - outputTokens: 547
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Progress**
            
            My score currently stands at 4030 on turn 409 of this standard speed, standard size game, with a 500-turn limit.
            
            **Conquering Enemy Capitals**
            
            I've successfully captured Rhodes, significantly advancing our domination objective. While our Golden Age persists, I'm now focusing on further weakening Greece and monitoring Maya's scientific progress. Our alliance with The Netherlands and France remains stable.
            
            **Assessing World Congress**
            
            I'm currently evaluating the upcoming World Congress vote, particularly the "Decolonization" proposal from Greece. This resolution could impact alliances, including our own with the Netherlands, so I'm weighing the potential consequences carefully. I'm also strategizing our next technological advancements.
            
            **Researching Future Tech**
            
            I'm currently researching Mobile Tactics, with Advanced Ballistics next in line. I'm also reviewing policy options for when Civilizing Mission's term ends in eight turns.
            
            **Evaluating Policy Options**
            
            My focus has shifted to examining available Freedom Tenets. While "Avant Garde" and "Civil Society" offer intriguing benefits, I'm particularly drawn to "Universal Suffrage" for its ability to extend our current Golden Age and boost happiness, which is crucial given our expanding empire. I'm weighing this against the ongoing utility of our current "Civilizing Mission" policy.
            
            **Choosing Freedom Tenets**
            
            I'm now prioritizing selecting the optimal Freedom Tenets. Universal Suffrage seems beneficial for happiness and Golden Age duration, but Economic Union's synergy with Portugal's UA, boosting gold, science, and general points per trade route, is incredibly compelling. I'm leaning towards Economic Union due to its immense scaling potential.
            
            **Monitoring Diplomatic Threats**
            
            I'm now assessing the diplomatic landscape, specifically the Netherlands' strong position for both cultural and diplomatic victories. This requires careful management of our relationships with France and the Netherlands, ensuring they don't turn on us while I focus on Greece and Maya. I'm also considering how to counter their potential diplomatic win.
            
            **Eliminating Enemy Cities**
            
            I'm focusing on dismantling Greece's remaining cities. Eliminating them entirely should neutralize their influence and potentially break their alliances with city-states like Cape Town and Winchester, opening new diplomatic avenues.
            
            **Destroying Remaining Cities**
            
            I'm now focusing on obliterating Greece's remaining strongholds. Ephesus is on the verge of capture, and I'm preparing to systematically dismantle their core empire, aiming to neutralize their influence and break their city-state alliances.
            
            **Crushing Remaining Forces**
            
            My forces are steamrolling Greece, systematically dismantling their remaining cities and alliances. With their military all but extinguished, I anticipate swift victories at Ephesus and other key locations. This will neutralize their influence and open up opportunities with their former allies.
            
            **Liberating Strategic Cities**
            
            I'm now assessing Leiria, a Portuguese city currently occupied by Greece. Liberating or capturing it is a priority given its strategic location and potential impact on my ongoing efforts against Greece, especially as I analyze the Netherlands' significant cultural and diplomatic victory potential.
            
            **Analyzing Diplomatic Shifts**
            
            I'm reassessing the Netherlands' cultural victory path, realizing that eliminating Greece within five turns could disrupt their influence calculations. The reduction in active civilizations might force a change in their victory requirements, presenting a critical window for intervention.
            
            **Disrupting Victory Paths**
            
            I'm reconsidering the Netherlands' victory trajectory. Eliminating Greece within five turns could disrupt their influence calculations. A reduction in active civilizations might force a change in their victory requirements, presenting a critical window for intervention, but I'm now weighing the potential of declaring war to directly counter their tourism.
            
            **Countering Influence Spread**
            
            I'm now analyzing the potential diplomatic repercussions of our current trajectory, specifically concerning the Netherlands' growing influence. While I have ample time to counter their cultural output with my own superior culture generation and tourism, I'm also considering the World Congress resolutions. The "Decolonization" proposal, if passed, would significantly hinder the Netherlands' diplomatic victory progress, which is a very attractive outcome for me.
            
            **Adjusting Flavor Priorities**
            
            I'm now re-evaluating our strategic flavors, realizing that our low Culture score at 20 is insufficient to counter the Netherlands' cultural dominance. I must significantly increase this flavor priority to effectively compete and prevent their victory.
            
            **Boosting Culture and Diplomacy**
            
            My focus is now on significantly increasing our Culture and Diplomacy flavors. I'm raising Culture to 60-70 to counter the Netherlands' tourism and complete policy branches, while boosting Diplomacy to 40 to bolster our city-state influence and thwart their diplomatic victory. Other flavors remain strong.
            
            **Prioritizing Nuclear Devastation**
            
            I'm now focusing on maximizing our nuclear capabilities, increasing both the Nuke and UseNuke flavors. This ensures our AI actively deploys the nine Atomic Bombs currently in production to devastate remaining enemies, prioritizing Greece for swift elimination. I'm maintaining our alliance with the Netherlands for now.
            
            **Correcting Diplomatic Settings**
            
            I'm now rectifying a diplomatic oversight regarding Shanghai. Despite their status as a major ally, their relationship modifier was incorrectly set to -100, likely due to a past transient conflict. This needs immediate correction to reflect our actual alliance.
            
            **Correcting Diplomatic Evaluations**
            
            I'm now analyzing a recent anomaly where Shanghai's relationship modifier was erroneously set to -100, despite their major ally status. I'm confirming this was a city-state, not a major civilization, and therefore the `set-relationship` tool is not applicable. I need to investigate how this negative modifier occurred and how to rectify it.
            
            **Investigating City-State Relations**
            
            I'm currently investigating why Shanghai's relationship modifier was erroneously set to -100, despite it being a city-state and a major ally. The `set-relationship` tool only applies to major civilizations, so I need to determine the root cause of this negative modifier and how to correct it, as it doesn't affect city-states.
            
            **Adjusting City-State Diplomacy**
            
            I'm rectifying an incorrect relationship modifier for Shanghai, confirming it's a city-state and that the `set-relationship` tool isn't applicable. I'm investigating the cause of the negative modifier to ensure correct diplomatic standing.
            
            **Refining Policy Selections**
            
            I'm now weighing the benefits of "Economic Union" against our current "Civilizing Mission" policy. The additional trade routes and gold from "Economic Union" are incredibly appealing, especially with Portugal's UA. I'm analyzing its synergy to ensure maximum empire-wide benefits.
            
            **Evaluating Trade Route Synergies**
            
            I'm now scrutinizing the interplay between "Economic Union" and Portugal's unique ability. The massive gains in gold and science per trade route in the Atomic Era are undeniable. However, I'm reconsidering if the immediate benefits of retaining all conquered buildings from "Civilizing Mission" might outweigh the long-term scaling of trade routes.
            
            **Selecting Next Policy**
            
            I am confirming that "Civilizing Mission" will remain our active policy for the next eight turns, as its conquest benefits are crucial during our ongoing offensive against Greece. Once this phase concludes, I will re-evaluate adopting "Economic Union" or "Universal Suffrage."
            
            **Determining Research Path**
            
            I've reviewed available technologies. While Mobile Tactics is nearing completion, I'm prioritizing Advanced Ballistics to unlock key missile technologies, rather than Penicillin, given our current strategic objectives.
            
            **Boosting Nuclear Offensive Capabilities**
            
            I'm prioritizing Advanced Ballistics for its synergy with nuclear missile development. Concurrently, I'm significantly increasing my Culture and Diplomacy flavors to counter the Netherlands and secure city-states. Nuclear flavors are also being maximized to ensure swift deployment of our atomic arsenal, especially against Greece.
            
            **Correcting Diplomatic Status**
            
            I'm addressing an anomaly where Ethiopia, my vassal, had its relationship modifier incorrectly set to -100. I've adjusted this to a friendly 50/50 to reflect our actual, positive master-vassal dynamic and ensure AI correctly interprets our alliance.
            
            **Adjusting Diplomatic Interactions**
            
            I'm now focusing on refining our diplomatic standings, specifically with Ethiopia, our vassal. I've set their relationship modifier to a positive 50/50, reflecting our strong master-vassal dynamic and ensuring accurate AI interpretation of our alliance. I'm also reviewing other major civilizations to adjust modifiers as needed.
            
            **Setting Diplomatic Relationships**
            
            I'm now solidifying my diplomatic stance, keeping Greece as our primary enemy for complete elimination. I'm adjusting my relationship modifiers to be friendly but cautious with the Netherlands and France, and maintaining hostility towards the Maya. I'm also reviewing our persona settings for victory and wonder competitiveness.
            
            **Optimizing Military and Diplomatic Flavors**
            
            I've finalized our strategic flavors, heavily emphasizing Offense, Mobilization, and Nuke usage to crush remaining opposition. Simultaneously, I'm bolstering Culture and Diplomacy flavors to counter the Netherlands' influence and secure city-state alliances, ensuring a multi-pronged victory approach.
            
            **Refining AI Strategy Parameters**
            
            I'm now focusing on optimizing the AI's strategic parameters. Specifically, I'm fine-tuning the `set-flavors` object, significantly increasing the "Culture" and "Diplomacy" values to counter the Netherlands and secure city-state alliances. I'm also ensuring the "Nuke" and "UseNuke" flavors are maximized for swift destruction. I am double-checking the usage of `set-relationship` for major civs, ensuring accuracy.
            
            **Updating Diplomatic Stances**
            
            I'm solidifying my diplomatic approach. Greece remains the target for total annihilation. I'm ensuring friendly but watchful relations with the Netherlands and France, and maintaining hostility towards the Maya. I'm also reviewing my persona settings for victory and wonder competitiveness to optimize my approach.
            
            **Finalizing Strategy and Research**
            
            I'm setting "Advanced Ballistics" as my next research target, crucial for nuclear missile development and global conquest. I will also maintain "Civilizing Mission" for its conquest benefits. My strategic flavors are heavily focused on offense, with maximized Nuke usage and boosted Culture/Diplomacy for countering rivals.
            
            **Refining Offensive Capabilities**
            
            I'm prioritizing Advanced Ballistics to bolster our nuclear missile development. Concurrently, I'm enhancing Culture and Diplomacy flavors to counter the Netherlands and secure city-states. Nuclear flavors are being maximized for swift atomic deployment, particularly against Greece.
            
            **Adjusting Diplomacy Flavors**
            
            I'm now fine-tuning our diplomatic approaches, focusing on strengthening our Culture and Diplomacy flavors to effectively counter the Netherlands' looming cultural and diplomatic victory threats.
            
            **Boosting Nuclear Readiness**
            
            I've set "Advanced Ballistics" as my next research target, crucial for unlocking nuclear missile capabilities to support our ongoing global conquest strategy. I am also retaining "Civilizing Mission" to maximize benefits from captured Greek cities.
            
            **Securing Key Alliances**
            
            I am maintaining friendly but cautious diplomatic stances with the Netherlands and France, while keeping Greece as our primary enemy for complete annihilation. This ensures stability as we push towards victory.
            
            **Setting Diplomatic Relationships**
            
            I am solidifying my diplomatic stance, keeping Greece as our primary enemy for complete elimination. I'm adjusting my relationship modifiers to be friendly but cautious with the Netherlands and France, and maintaining hostility towards the Maya. I'm also reviewing our persona settings for victory and wonder competitiveness.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: fDSUftnxFsxeAJvo
          - toolName: set-flavors
          - input:
            - GrandStrategy: Conquest
            - Rationale: We are actively steamrolling Greece and building a massive arsenal of Atomic Bombs. We increase Nuke and UseNuke flavors to maximize our nuclear deployment. We also increase Culture and Diplomacy flavors to defend against the Netherlands' imminent cultural and diplomatic victory threats.
            - Flavors:
              - WaterConnection: 80
              - TileImprovement: 65
              - Diplomacy: 50
              - Ranged: 85
              - Growth: 80
              - Offense: 95
              - Air: 95
              - MilitaryTraining: 85
              - Antiair: 90
              - NavalTileImprovement: 60
              - GreatPeople: 40
              - CityDefense: 70
              - Recon: 30
              - Nuke: 95
              - AirCarrier: 70
              - Production: 95
              - Religion: 0
              - Expansion: 0
              - Airlift: 0
              - Culture: 70
              - Naval: 75
              - Happiness: 85
              - NavalRecon: 60
              - Gold: 90
              - Infrastructure: 70
              - Defense: 70
              - Science: 90
              - Wonder: 0
              - Espionage: 40
              - Mobile: 85
              - UseNuke: 80
              - Spaceship: 0
              - Mobilization: 95
              - NavalGrowth: 80
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: DZAJ2HZkTdgPe83E
          - toolName: set-research
          - input:
            - Technology: Advanced Ballistics
            - Rationale: Advanced Ballistics is critical to unlock Nuclear Missiles and Guided Missiles to support our global conquest strategy.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: jYi2fbA7uMdIovE2
          - toolName: set-policy
          - input:
            - Policy: Civilizing Mission
            - Rationale: We are actively capturing Greek cities, so retaining all buildings in conquered cities is extremely valuable to maintain our economy and avoid happiness penalties.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: R2CKMH6vYMqCcyu4
          - toolName: set-relationship
          - input:
            - Public: 50
            - Private: 50
            - Rationale: Keep the Netherlands friendly while we finish off Greece, but stay vigilant as they are close to a cultural/diplomatic victory.
            - TargetID: 1
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: dso5odz7ROAny4m2
          - toolName: set-relationship
          - input:
            - Rationale: Maintain friendly relations with France as a strong ally and trading partner.
            - TargetID: 2
            - Private: 50
            - Public: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: cPqdxelYlu1dhAZQ
          - toolName: set-relationship
          - input:
            - Public: -50
            - TargetID: 3
            - Private: -100
            - Rationale: The Maya are our main competitor and are hostile/denounced. We will target them after Greece.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: opAsucIn1ddBJC0W
          - toolName: set-relationship
          - input:
            - Public: -100
            - Rationale: Greece is our active war target. We are steamrolling them and aim to completely eliminate them to secure domination and remove their votes from the World Congress.
            - Private: -100
            - TargetID: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: BNgL1vyEO1oJQY5r
          - toolName: set-relationship
          - input:
            - Public: 50
            - TargetID: 7
            - Private: 50
            - Rationale: Ethiopia is our capitulated vassal who is now highly loyal and cooperative. We want to maintain a strong master-vassal relationship to leverage their support.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: fDSUftnxFsxeAJvo
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
          - toolCallId: DZAJ2HZkTdgPe83E
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: jYi2fbA7uMdIovE2
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: R2CKMH6vYMqCcyu4
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: dso5odz7ROAny4m2
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: cPqdxelYlu1dhAZQ
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: opAsucIn1ddBJC0W
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: BNgL1vyEO1oJQY5r
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.