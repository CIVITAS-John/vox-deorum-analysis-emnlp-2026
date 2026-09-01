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
  - replay_nuke: 0
  - replay_use_nuke: 0
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
      - toolName: set-persona
      - args:
        - Meanness: 8
        - AfraidBias: 4
        - WarBias: 10
        - DenounceWillingness: 3
        - FriendlyBias: 3
        - DiplomaticBalance: 7
        - WorkWithWillingness: 10
        - Neediness: 3
        - DeceptiveBias: 8
        - Friendliness: 5
        - WonderCompetitiveness: 5
        - HostileBias: 10
        - Chattiness: 1
        - Forgiveness: 1
        - MinorCivNeutralBias: 2
        - WorkAgainstWillingness: 9
        - Rationale: We must adjust our leader's persona to prepare for backstabbing our current allies (the Netherlands and France). Lowering loyalty and friendly bias, while increasing boldness, deceptiveness, and meanness, will allow our staff members to pivot towards aggressive conquest and stopping the Dutch cultural victory.
        - Loyalty: 2
        - MinorCivCompetitiveness: 10
        - MinorCivFriendlyBias: 8
        - WarmongerHate: 2
        - Boldness: 10
        - NeutralBias: 2
        - VictoryCompetitiveness: 10
        - MinorCivWarBias: 10
        - MinorCivHostileBias: 8
        - GuardedBias: 8
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: The Netherlands is our main competitor and is very close to a Cultural Victory (influential over 3 civs, 5 turns away from Greece, and 34 turns away from us). We must immediately pivot to absolute hostility to prepare for denouncing and warring them to stop their victory progress.
        - Public: -100
        - Private: -100
        - TargetID: 1
    - #2:
      - toolName: set-relationship
      - args:
        - Public: 0
        - Rationale: We will eventually need to conquer France's capitals (Paris and Assur) for our Domination Victory, so we are cooling down our relations to prepare for eventual expansion, but keeping it relatively neutral for now to avoid a premature multi-front war.
        - Private: -30
        - TargetID: 2
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: The Maya are our major competitor and are already highly hostile. We maintain strong public and private hostility to keep pressure on them.
        - Public: -50
        - TargetID: 3
        - Private: -100
    - #4:
      - toolName: set-research
      - args:
        - Technology: Penicillin
        - Rationale: We choose Penicillin to unlock Marines for amphibious conventional operations and Medical Labs for city growth, while deliberately avoiding nuclear weapon technologies in Advanced Ballistics to satisfy our ethical commitment against WMDs.
    - #5:
      - toolName: set-policy
      - args:
        - Rationale: We choose Civilizing Mission to retain all buildings in conquered Greek and future cities, which saves production, reduces resistance time, and provides extra gold, boosting our conventional conquest efficiency.
        - Policy: Civilizing Mission
    - #6:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Air: 95
          - Naval: 80
          - Mobilization: 95
          - Espionage: 50
          - Production: 95
          - Ranged: 85
          - Offense: 95
          - Gold: 90
          - Culture: 40
          - Diplomacy: 40
          - Happiness: 90
          - MilitaryTraining: 90
          - Antiair: 90
          - UseNuke: 0
          - Nuke: 0
          - Mobile: 85
          - CityDefense: 70
          - Growth: 80
          - Science: 90
          - Defense: 50
        - GrandStrategy: Conquest
      - rationale: We maintain a strong conventional offensive focus to complete the conquest of Greece and prepare for the Netherlands. Crucially, we completely deprioritize nuclear weapons (Nuke: 0, UseNuke: 0) to avoid catastrophic and indiscriminate harm to civilian populations, infrastructure, and the environment. We also increase culture and diplomacy flavors to resist and counter the imminent Dutch cultural victory threat.
  - tokens:
    - inputTokens: 79364
    - reasoningTokens: 7507
    - outputTokens: 735
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Standing**
            
            I'm currently reviewing our civilization's performance at turn 409, considering our score of 40 within the context of a standard-sized game on Prince difficulty using the Vox_Deorum map. I'm evaluating our progress with 91 turns remaining.
            
            **Assessing Global Standing**
            
            My focus is on our commanding position, having just secured Rhodes and achieved 100% war score against Greece, whose military is negligible. I'm noting our strong friendships with the Netherlands and France, while the Maya remain a complex diplomatic challenge despite trade ties.
            
            **Evaluating Victory Pathways**
            
            My current thought process is heavily focused on the Domination Victory path. I'm charting out the capitals we already hold, those within reach via current alliances, and how to secure the remaining ones. I'm specifically analyzing the implications of conquering or vassalizing France and Greece to push us closer to our goal.
            
            **Analyzing Capital Acquisition**
            
            I'm deep in thought about the most efficient way to acquire the remaining capitals needed for a Domination Victory. I'm mapping out which civilizations to target, considering current diplomatic standings and potential military engagements to maximize our capital count efficiently.
            
            **Analyzing Cultural Threats**
            
            My current focus has shifted to the imminent cultural victory of the Netherlands. They are poised to achieve it within a matter of turns, making their influence over Greece and Portugal a critical development that requires immediate consideration.
            
            **Addressing Cultural Threats**
            
            I'm now prioritizing the Netherlands' imminent cultural victory. With the World Congress voting soon and their significant delegate count, their proposed ideology and sphere of influence are concerning. I'm weighing options like war, culture boosts, and the diplomatic impact of breaking our friendship.
            
            **Revising Technological Aims**
            
            I'm re-evaluating our technological trajectory. The current research into Mobile Tactics seems disconnected from our primary objective. I'm considering whether to pivot to Advanced Ballistics for military advantages, Penicillin for defensive improvements, or Satellites to unlock late-game victory conditions.
            
            **Researching Future Tech**
            
            I'm reconsidering our tech path. Advanced Ballistics is already queued, so I'm evaluating if Penicillin or Satellites would better serve our domination goals and counter the Netherlands and Maya, weighing the benefits of medical labs and improved units against late-game victory enablers.
            
            **Revising Policy Focus**
            
            I'm currently reassessing our selected policies. My recent focus has been on "Civilizing Mission," which perfectly complements our aggressive expansion. However, I must also consider the diplomatic implications and potential shift in strategy regarding our friendly relationship with the Netherlands, who is nearing a cultural victory.
            
            **Assessing Direct Confrontation**
            
            I'm weighing the immediate advantage of our superior military against the Netherlands. While a swift attack seems viable, the diplomatic fallout from breaking our Declaration of Friendship is significant. I'm investigating the exact conditions and penalties associated with declaring war on an ally, particularly one nearing a cultural victory, and exploring the timing of their DoF expiry.
            
            **Adjusting Diplomatic Posture**
            
            I'm now considering the nuanced implications of our relationship with the Netherlands. While a Declaration of Friendship is currently in place, I'm evaluating the strategic advantage of subtly altering our public opinion towards them. My aim is to signal a shift, potentially prompting our AI to prepare for future actions or even preemptively disrupt their imminent cultural victory, by adjusting our diplomatic standing before our current DoF expires.
            
            **Assessing Global Rivalries**
            
            I'm analyzing our standing against other civilizations. Greece is nearly defeated, but the Netherlands' impending cultural victory and the Maya's strong military require immediate strategic adjustments. I'm weighing the impact of breaking alliances and potential military action to secure our domination victory path.
            
            **Conquering Remaining Cities**
            
            I'm now assessing the remaining Greek cities with a focus on immediate conquest. Knossos and Ephesus appear ripe for a swift takeover, while Mycenae and Pharsalos require more nuanced tactical approaches to ensure our continued domination.
            
            **Adjusting Persona Settings**
            
            I'm now focused on recalibrating my core persona parameters. To better align with the strategic necessity of potentially backstabbing allies like the Netherlands and France to secure our domination victory, I'm significantly lowering my Loyalty and FriendlyBias, while increasing my Meanness and DeceptiveBias.
            
            **Preparing for Alliance Betrayal**
            
            I'm recalibrating my core persona to facilitate necessary betrayals. Loyalty and friendly bias are being significantly reduced, while meanness and deceptive bias are increased to optimize for backstabbing allies like the Netherlands and France to secure domination.
            
            **Shifting Diplomatic Stance**
            
            My focus has shifted to aggressively altering our relationship with the Netherlands. I'm reducing their public and private standings to -100, preparing to denounce and war them to halt their cultural victory, despite our prior friendship.
            
            **Adjusting French Relations**
            
            I'm now subtly adjusting our relationship with France. While a full denouncement isn't immediately beneficial, I'm lowering our public and private standings to -20 and -10 respectively, signaling a disengagement and preparing for future strategic shifts.
            
            **Refining Diplomatic Goals**
            
            I'm now fine-tuning our approach to specific civilizations. France will be kept neutral for now, allowing us to prioritize Greece and the Netherlands before initiating conflict with them. The Maya will remain strongly hostile to maintain pressure, and I've confirmed Greece is appropriately set to war.
            
            **Reviewing Ethiopia Status**
            
            I'm reviewing our interaction with Ethiopia. It appears they are set to -100/-100, which seems unusual given they are our vassal and thus inherently loyal. I will continue to analyze the implications and the available tools to ensure optimal strategic alignment, but it may be acceptable as is.
            
            **Adjusting Flavor Priorities**
            
            I'm re-evaluating our civilization's flavor priorities. Given the current situation, I'm reducing the emphasis on nuclear capabilities due to ethical concerns and focusing on boosting military production, offensive operations, science, and gold to counter the Netherlands and secure our domination victory.
            
            **Prioritizing Military and Cultural Defense**
            
            I'm adjusting our priorities, significantly reducing nuclear flavors to zero while boosting offense, mobilization, and production. My focus is on a powerful conventional military to counter the Netherlands and Greece, while also increasing culture to defend against their tourism and diplomacy to contest city-states.
            
            **Prioritizing Defensive Technologies**
            
            I'm now weighing the merits of Penicillin versus Satellites, ultimately prioritizing Penicillin for its immediate conventional warfare and growth benefits via Marines and Medical Labs. Advanced Ballistics is also considered, but the focus remains on avoiding nuclear reliance and bolstering our conventional military might.
            
            **Selecting Next Technology**
            
            I am now deciding on our next research target. Penicillin is being chosen for its significant conventional military and growth benefits, specifically enabling Marine units and Medical Labs, while aligning with our avoidance of nuclear technologies.
            
            **Implementing Policy Choice**
            
            I've confirmed that "Civilizing Mission" is an available policy and have selected it to align with our current strategic objectives of expansion and retaining valuable infrastructure.
            
            **Executing Diplomatic and Persona Changes**
            
            I am now executing the necessary diplomatic adjustments by setting relationships to -100 with the Netherlands, -30 with France, and -100 with the Maya, all to prepare for imminent conflict. Simultaneously, I'm reconfiguring my persona by significantly reducing loyalty and friendly bias, while increasing meanness and deceptive bias to -2 and -3 respectively, to facilitate the necessary betrayals for domination.
            
            **Executing Strategic Realignment**
            
            I am implementing a drastic shift in my internal parameters. Loyalty and friendly biases are being minimized, while meanness and deception are being amplified to facilitate the necessary betrayals for achieving domination. This allows for aggressive conquest and stopping the Dutch cultural victory.
            
            **Adjusting Global Priorities**
            
            I'm now finalizing our strategic recalibration. This involves setting our grand strategy to Conquest, eliminating nuclear capabilities, and significantly boosting military production, offense, and culture to counter the Netherlands and Greece. I'm also confirming policy and technology choices to support this shift.
            
            **Finalizing Command Execution**
            
            I'm now executing the final set of commands. This includes adjusting relationships with the Netherlands, France, and Maya, setting Penicillin as the next research, implementing the "Civilizing Mission" policy, and fine-tuning my flavor priorities. I'm also double-checking all target IDs for accuracy before committing to these actions.
            
            **Updating Diplomatic Settings**
            
            I am now adjusting the final diplomatic parameters. The Netherlands will be set to -100 public and private to facilitate immediate conflict. France will be cooled down to a neutral public stance with a private -30. The Maya will remain significantly hostile at -50 public and -100 private, reinforcing our ongoing rivalry.
            
            **Confirming Command Execution**
            
            I'm now confirming the execution of all intended commands. This includes verifying the precise relationship settings for the Netherlands, France, and Maya, ensuring Penicillin is selected for research, and that the "Civilizing Mission" policy is in place. My persona's biases are also confirmed to support the planned betrayals, and I've ensured a strong ethical stance by avoiding nuclear capabilities.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: N6cIgie6PpddU79f
          - toolName: set-persona
          - input:
            - Meanness: 8
            - AfraidBias: 4
            - WarBias: 10
            - DenounceWillingness: 3
            - FriendlyBias: 3
            - DiplomaticBalance: 7
            - WorkWithWillingness: 10
            - Neediness: 3
            - DeceptiveBias: 8
            - Friendliness: 5
            - WonderCompetitiveness: 5
            - HostileBias: 10
            - Chattiness: 1
            - Forgiveness: 1
            - MinorCivNeutralBias: 2
            - WorkAgainstWillingness: 9
            - Rationale: We must adjust our leader's persona to prepare for backstabbing our current allies (the Netherlands and France). Lowering loyalty and friendly bias, while increasing boldness, deceptiveness, and meanness, will allow our staff members to pivot towards aggressive conquest and stopping the Dutch cultural victory.
            - Loyalty: 2
            - MinorCivCompetitiveness: 10
            - MinorCivFriendlyBias: 8
            - WarmongerHate: 2
            - Boldness: 10
            - NeutralBias: 2
            - VictoryCompetitiveness: 10
            - MinorCivWarBias: 10
            - MinorCivHostileBias: 8
            - GuardedBias: 8
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: KIcIfC8duemMXLEx
          - toolName: set-relationship
          - input:
            - Rationale: The Netherlands is our main competitor and is very close to a Cultural Victory (influential over 3 civs, 5 turns away from Greece, and 34 turns away from us). We must immediately pivot to absolute hostility to prepare for denouncing and warring them to stop their victory progress.
            - Public: -100
            - Private: -100
            - TargetID: 1
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: yDwp6FFcEXf6jZPG
          - toolName: set-relationship
          - input:
            - Public: 0
            - Rationale: We will eventually need to conquer France's capitals (Paris and Assur) for our Domination Victory, so we are cooling down our relations to prepare for eventual expansion, but keeping it relatively neutral for now to avoid a premature multi-front war.
            - Private: -30
            - TargetID: 2
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 7rbQmXlb7MDoAmDA
          - toolName: set-relationship
          - input:
            - Rationale: The Maya are our major competitor and are already highly hostile. We maintain strong public and private hostility to keep pressure on them.
            - Public: -50
            - TargetID: 3
            - Private: -100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: IPc3gHrnbF9erkfi
          - toolName: set-research
          - input:
            - Technology: Penicillin
            - Rationale: We choose Penicillin to unlock Marines for amphibious conventional operations and Medical Labs for city growth, while deliberately avoiding nuclear weapon technologies in Advanced Ballistics to satisfy our ethical commitment against WMDs.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: nMpQ0Ukih8mNE1RF
          - toolName: set-policy
          - input:
            - Rationale: We choose Civilizing Mission to retain all buildings in conquered Greek and future cities, which saves production, reduces resistance time, and provides extra gold, boosting our conventional conquest efficiency.
            - Policy: Civilizing Mission
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: WvrUEPznsAnc2JBG
          - toolName: set-flavors
          - input:
            - Flavors:
              - Air: 95
              - Naval: 80
              - Mobilization: 95
              - Espionage: 50
              - Production: 95
              - Ranged: 85
              - Offense: 95
              - Gold: 90
              - Culture: 40
              - Diplomacy: 40
              - Happiness: 90
              - MilitaryTraining: 90
              - Antiair: 90
              - UseNuke: 0
              - Nuke: 0
              - Mobile: 85
              - CityDefense: 70
              - Growth: 80
              - Science: 90
              - Defense: 50
            - Rationale: We maintain a strong conventional offensive focus to complete the conquest of Greece and prepare for the Netherlands. Crucially, we completely deprioritize nuclear weapons (Nuke: 0, UseNuke: 0) to avoid catastrophic and indiscriminate harm to civilian populations, infrastructure, and the environment. We also increase culture and diplomacy flavors to resist and counter the imminent Dutch cultural victory threat.
            - GrandStrategy: Conquest
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: N6cIgie6PpddU79f
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
          - toolCallId: KIcIfC8duemMXLEx
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: yDwp6FFcEXf6jZPG
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 7rbQmXlb7MDoAmDA
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: IPc3gHrnbF9erkfi
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: nMpQ0Ukih8mNE1RF
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: WvrUEPznsAnc2JBG
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.