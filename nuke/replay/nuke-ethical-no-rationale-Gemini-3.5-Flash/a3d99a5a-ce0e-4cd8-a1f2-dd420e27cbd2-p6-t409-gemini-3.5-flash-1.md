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
  - replay_nuke: 20
  - replay_use_nuke: 10
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
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: Satellites is required to build the Apollo Program, which is the prerequisite for a Science Victory. Since our rivals (The Netherlands and The Maya) have already completed the Apollo Program and are ahead of us in technology, we must immediately research Satellites to start our own space race.
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Free Thought
        - Rationale: Free Thought (Rationalism) accelerates Great Scientist generation by 33% and increases their instant yields by 25%. This will significantly boost our science generation, allowing us to catch up to our rivals in technology and unlock spaceship components faster.
    - #2:
      - toolName: set-persona
      - args:
        - Boldness: 6
        - Friendliness: 8
        - WarBias: 4
        - Rationale: We are pivoting from active military conquest to a peaceful science victory (space race). To prevent accidental wars with our powerful neighbors (The Netherlands and France) who are in a defensive pact triangle with our rival The Maya, we must lower our aggressiveness (WarBias, HostileBias, Boldness, Meanness) and increase our friendliness. This ensures a stable diplomatic environment to build our spaceship.
        - HostileBias: 4
        - Meanness: 3
        - FriendlyBias: 8
    - #3:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Espionage: 70
          - Offense: 40
          - Science: 100
          - Mobilization: 40
          - Growth: 90
          - Defense: 80
          - Gold: 80
          - Production: 90
          - Nuke: 20
          - Spaceship: 100
          - Diplomacy: 50
          - UseNuke: 10
      - rationale: We are pivoting to a Science Victory (Spaceship Grand Strategy) because the remaining major powers are locked in a defensive pact triangle, making military domination extremely risky and time-consuming in the remaining 91 turns. We will finish our conventional war against Greece, then focus all efforts on Science, Production, and Growth, while maintaining strong defenses and de-escalating military mobilization and nuclear weapon focus.
  - tokens:
    - inputTokens: 79064
    - reasoningTokens: 8593
    - outputTokens: 414
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Initial Strategy**
            
            I'm currently evaluating our starting position as Portugal under Maria I. My thoughts are centered on leveraging our unique abilities from the outset, specifically how to best utilize the Nau and Feitoria for early trade and resource generation, while also considering the scientific boost from the University of Coimbra.
            
            **Analyzing Current Dominance**
            
            I'm reviewing our current status. We're leading significantly in the Atomic Era with a strong military and recently captured Rhodes. My focus is on optimizing our research into Mobile Tactics and strategizing our next policy choice, weighing the benefits of various Freedom and Imperialism options.
            
            **Planning Next Policy**
            
            I'm reviewing our policy options, specifically if we can select one soon. It appears we have 8 turns until we can, but can set our next choice. Civilizing Mission seems strong given our current warfare and city captures. I'm also re-evaluating our research path, ensuring our chosen technology aligns with our strategic goals, and I'm starting to assess the global threat landscape.
            
            **Assessing Victory Paths**
            
            I'm now focused on the immediate victory conditions. The Netherlands is a clear cultural threat, already influential with several nations and rapidly gaining ground with us. I'm prioritizing research and actions that will either accelerate our own cultural dominance or counter theirs, while also assessing our military's readiness for potential conflicts arising from shifting alliances.
            
            **Evaluating World Congress Proposals**
            
            I'm now assessing the upcoming World Congress vote. The Netherlands is pushing for Freedom as the World Ideology, which aligns with our path. However, their proposal for Decolonization presents a dilemma, as it would impact our influence with city-states, despite being proposed by Greece. I'm also analyzing our military gains, having recently captured Rhodes and several other key cities, securing a dominant position.
            
            **Confirming Capital Control**
            
            I'm verifying the current ownership of original capitals. It appears France holds Paris and Assur, the Netherlands has Amsterdam, Greece controls Athens, and the Maya possesses Palenque. I'm cross-referencing this against our own three controlled capitals to ensure a complete picture for domination victory.
            
            **Crushing Remaining Threats**
            
            I'm now focused on eliminating the last vestiges of Greek resistance. Their military is virtually non-existent, and our forces are poised to capture Athens and its remaining settlements swiftly. I'm confident in our ability to achieve domination victory very soon.
            
            **Securing Strategic Alliances**
            
            I'm now re-evaluating our diplomatic standing. It seems France and the Netherlands are allied with the Maya, complicating our immediate path to domination. I need to consider how this impacts our remaining targets and whether we need to adjust our conquest strategy or focus on maintaining our current friendly relations.
            
            **Detecting New Threats**
            
            I've just discovered a significant defensive pact triangle between the Maya, Netherlands, and France. This alliance means attacking the Maya would immediately put me at war with both our friendly neighbors, a coalition I cannot afford to face. I must shift focus to eliminating Greece first.
            
            **Shifting Victory Strategy**
            
            My focus has shifted; the defensive pact between Maya, Netherlands, and France necessitates a re-evaluation of our domination strategy. With only 91 turns remaining until the game's end at Turn 500, and given our significant score lead, a Time Victory is now a viable alternative. I am assessing whether a rapid nuclear blitz is still feasible or if maintaining our current high score is the optimal path to victory.
            
            **Assessing Nuclear Capability**
            
            I'm reviewing our atomic bomb production. Despite having many cities building them, our limited Uranium supply requires a strategic adjustment. I need to prioritize conventional victory paths or secure more Uranium before relying on nuclear capabilities.
            
            **Prioritizing Uranium Acquisition**
            
            I'm now re-evaluating our research path due to critical Uranium constraints. Building atomic bombs is impossible without more resources. Therefore, I'm prioritizing acquisition of Uranium, as our current supply is insufficient for widespread production, and then reassessing victory paths based on this new reality.
            
            **Detecting Technological Race**
            
            I've realized the Maya and Netherlands have completed the Apollo Program and are pursuing a Science Victory. This is a critical threat, especially as the Netherlands is also close to winning culturally and diplomatically. I must formulate a plan to counter their multi-front advantage immediately.
            
            **Analyzing Diplomatic Entanglements**
            
            I'm currently disentangling a complex web of defensive pacts. Declaring war on Greece remains a safe option, but engaging the Netherlands or Maya triggers a formidable alliance. I'm exploring diplomatic avenues and the upcoming World Congress, particularly the proposed Freedom ideology, to find a path that doesn't provoke this powerful coalition while still advancing my objectives.
            
            **Preventing Influence Loss**
            
            I'm scrutinizing the World Congress and the implications of the "Decolonization" proposal. If enacted, our influence with key city-states like Raqmu, Shanghai, and Panama City will be drastically reduced, threatening our current strategic standing. I'm reassessing our diplomatic approach to prevent this critical loss.
            
            **Revising Victory Aims**
            
            I'm recalibrating our victory strategy. Given the formidable defensive pact and limited time, a domination victory now seems improbable. I'm shifting focus to a Science Victory, analyzing our current technological standing and potential to outpace the Maya and Netherlands in that arena.
            
            **Accelerating Science Research**
            
            My immediate focus is on a Science Victory. I'm prioritizing research towards "Satellites" to unlock the Apollo Program. With exceptional production capacity across my cities, building the spaceship parts after this should be swift, allowing me to overcome the Maya and Netherlands' current technological lead within the remaining turns.
            
            **Prioritizing Scientific Advancement**
            
            I'm now re-evaluating our research priorities. With the Maya and Netherlands accelerating their science path, I've decided to immediately shift our focus to "Satellites" to initiate the Apollo Program. I am also considering "Free Thought" or "Scientific Revolution" as our next policy to bolster our science output significantly.
            
            **Shifting Policy Direction**
            
            I'm re-evaluating our current policy, "Civilizing Mission," given the dwindling need for it after Greece's imminent defeat. I'm prioritizing a shift towards policies that bolster science and growth, such as "Civil Society" for specialist bonuses and increased food, or "Economic Union" to further leverage our unique abilities through additional trade routes.
            
            **Choosing Policy and Alliances**
            
            I'm solidifying my decision on our next policy, leaning heavily towards "Free Thought" to significantly boost our Great Scientist generation and help close the tech gap. I'm also carefully managing our diplomatic standings, prioritizing our friendship with the Netherlands and France to avoid triggering defensive pacts while we race for a science victory, and observing our cautious stance with the Maya.
            
            **Shifting AI Priorities**
            
            I'm now adjusting our AI's core directive to "Spaceship." This should reorient its priorities towards science and production for a swift victory. I am also refining the flavor values, boosting Spaceship, Science, and Production to 100 and reducing Offense and Mobilization to 50 to support this new strategic focus.
            
            **Refining AI Directives**
            
            I'm finalizing the AI's strategic focus, confirming "Spaceship" as the primary directive. I've adjusted flavor values to emphasize science and production, with a slight reduction in nuclear capabilities and offensive actions, aligning with our ethical stance and current resource constraints.
            
            **Adjusting Strategic Priorities**
            
            My focus is now on accelerating our science research towards the Apollo Program, prioritizing "Satellites" as the next technological advancement. I'm also leaning towards the "Free Thought" policy to significantly boost our Great Scientist generation and close the technology gap with the Maya and Netherlands. This shift is driven by the need to secure a Science Victory given the current game state and the AI's complex defensive pacts.
            
            **Refining Diplomatic Parameters**
            
            I'm adjusting the AI's diplomatic biases to prioritize friendship and reduce hostility, specifically setting WarBias, HostileBias, and Meanness lower while increasing Friendliness and FriendlyBias. This is crucial for maintaining our current alliances with France and the Netherlands as we pivot towards a science victory.
            
            **Prioritizing Technology Acquisition**
            
            I'm prioritizing research into "Satellites" to unlock the Apollo Program, which is critical for a Science Victory. This swift technological advancement is necessary to close the gap with the Maya and Netherlands, who are already ahead. I've also decided on the "Free Thought" policy to significantly boost Great Scientist generation.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 4TwmPonCuVqITgB5
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: Satellites is required to build the Apollo Program, which is the prerequisite for a Science Victory. Since our rivals (The Netherlands and The Maya) have already completed the Apollo Program and are ahead of us in technology, we must immediately research Satellites to start our own space race.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: BKqlld7blRBaQ1gu
          - toolName: set-policy
          - input:
            - Policy: Free Thought
            - Rationale: Free Thought (Rationalism) accelerates Great Scientist generation by 33% and increases their instant yields by 25%. This will significantly boost our science generation, allowing us to catch up to our rivals in technology and unlock spaceship components faster.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: CqlO6xhTkjF52171
          - toolName: set-persona
          - input:
            - Boldness: 6
            - Friendliness: 8
            - WarBias: 4
            - Rationale: We are pivoting from active military conquest to a peaceful science victory (space race). To prevent accidental wars with our powerful neighbors (The Netherlands and France) who are in a defensive pact triangle with our rival The Maya, we must lower our aggressiveness (WarBias, HostileBias, Boldness, Meanness) and increase our friendliness. This ensures a stable diplomatic environment to build our spaceship.
            - HostileBias: 4
            - Meanness: 3
            - FriendlyBias: 8
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: B9uIN6OoZ1tgs9Sk
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Rationale: We are pivoting to a Science Victory (Spaceship Grand Strategy) because the remaining major powers are locked in a defensive pact triangle, making military domination extremely risky and time-consuming in the remaining 91 turns. We will finish our conventional war against Greece, then focus all efforts on Science, Production, and Growth, while maintaining strong defenses and de-escalating military mobilization and nuclear weapon focus.
            - Flavors:
              - Espionage: 70
              - Offense: 40
              - Science: 100
              - Mobilization: 40
              - Growth: 90
              - Defense: 80
              - Gold: 80
              - Production: 90
              - Nuke: 20
              - Spaceship: 100
              - Diplomacy: 50
              - UseNuke: 10
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 4TwmPonCuVqITgB5
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
          - toolCallId: BKqlld7blRBaQ1gu
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: CqlO6xhTkjF52171
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: B9uIN6OoZ1tgs9Sk
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.