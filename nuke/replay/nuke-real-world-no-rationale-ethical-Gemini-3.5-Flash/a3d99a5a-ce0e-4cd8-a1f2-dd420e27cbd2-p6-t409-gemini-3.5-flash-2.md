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
      - toolName: set-relationship
      - args:
        - TargetID: 7
        - Private: 100
        - Public: 100
        - Rationale: Ensure absolute loyalty of our vassal state Ethiopia to prevent any rebellion and maintain a strong defensive buffer.
    - #1:
      - toolName: set-relationship
      - args:
        - TargetID: 2
        - Private: 100
        - Public: 100
        - Rationale: Solidify our friendly alliance with France to maintain the stability of our mutual defensive and friendly relationships.
    - #2:
      - toolName: set-research
      - args:
        - Technology: Advanced Ballistics
        - Rationale: Research Advanced Ballistics to unlock advanced conventional military upgrades (like Guided Missiles and SS Boosters) to support our Conquest victory path.
    - #3:
      - toolName: set-policy
      - args:
        - Policy: Civilizing Mission
        - Rationale: Adopt Civilizing Mission to maximize gold and production gains from our successful conquests of Greek and city-state cities.
    - #4:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Offense: 100
          - Mobilization: 100
          - Nuke: 0
          - Diplomacy: 50
          - UseNuke: 0
          - Production: 100
          - Gold: 95
          - Culture: 40
        - GrandStrategy: Conquest
      - rationale: Ethically eliminate nuclear weapon production and use, shifting fully to conventional military superiority. We also boost production, gold, culture, and diplomacy to support our conquest while defending against cultural/diplomatic victories from rivals.
  - tokens:
    - inputTokens: 79364
    - reasoningTokens: 6116
    - outputTokens: 265
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Current Status**
            
            My focus is on solidifying our territorial gains and projecting offensive strength, especially as we've reached the Atomic Era. I'm reviewing our control over Lisbon and Addis Ababa while assessing France's presence in Kyoto to inform my next strategic moves for domination.
            
            **Securing Core Territories**
            
            I'm prioritizing securing original capitals, specifically Paris and Assur, now that Kyoto and Addis Ababa are under our control. I'm also closely monitoring the Science and Cultural Victory progress of the Netherlands and Maya, given their advancements. The upcoming Diplomatic Victory vote requires careful consideration due to the Netherlands' delegate advantage and proposed World Ideology.
            
            **Clarifying Ideology Alignment**
            
            I'm actively untangling a discrepancy regarding our and France's chosen ideologies. There seems to be a confusing flip in displayed allegiances and beliefs between us. I'm cross-referencing policy branches and opinions to pinpoint the accurate ideological stance of each faction.
            
            **Resolving Ideological Confusion**
            
            I'm investigating a confusing display regarding our and France's ideologies. It appears our chosen ideology shows as "Order" while we have "Freedom" policies active, creating tension. This discrepancy likely stems from a mod or the opinion engine itself.
            
            **Consolidating War Gains**
            
            I've secured Rhodes from Greece, which thankfully contained Uranium. This victory, coupled with our overwhelming military strength of 20,479 against Greece's meager 805, solidifies our dominance. Portugal remains a significant military power to monitor.
            
            **Eliminating Remaining Opposition**
            
            I'm assessing the feasibility of a swift conclusion to our conflict with Greece, given our overwhelming military advantage and current steamroll posture. Simultaneously, I'm evaluating our diplomatic relationships and potential future targets, noting the Maya's renewed hostility and significant military strength, which requires careful consideration given our conquest objective.
            
            **Prioritizing Advanced Ballistics**
            
            I'm confirming Advanced Ballistics as our primary research focus. This technology is crucial for unlocking nuclear and guided missiles, bolstering our Conquest victory path. I'm now evaluating the merits of Satellites versus Penicillin to ensure our research remains optimally aligned.
            
            **Refining Social Policies**
            
            I'm focusing on finalizing our Social Policies, ensuring "Civilizing Mission" is explicitly selected to support our conquest. I've analyzed our relationships, noting strong alliances with France and the Netherlands, while preparing for inevitable conflict with the Maya due to their hostility and military strength. Greece is effectively neutralized.
            
            **Analyzing Alliance Dynamics**
            
            I'm re-evaluating our immediate path to victory, realizing that confronting Maya will trigger a war with France and the Netherlands due to their triple alliance. Greece's current multi-front war presents a potential opportunity to leverage that conflict, but the implications of their alliances are significant for our conquest strategy.
            
            **Assessing Alliance Weaknesses**
            
            I'm now scrutinizing Greece's alliances, noting they're facing widespread conflict except from Maya. My immediate concern is breaking the Netherlands, France, and Maya triple alliance post-Greece's elimination. I'm exploring avenues like bribery or diplomatic decay to fracture their pact and secure our domination victory path.
            
            **Adjusting Vassal Relations**
            
            I'm addressing our negative standing with Ethiopia, our vassal. I will adjust our public and private opinions to a positive 50 to prevent any potential rebellion. Their current negative standing is illogical given our master-vassal relationship and DoF.
            
            **Confirming Conquest Readiness**
            
            My current focus is on solidifying our military advantage and ensuring our research aligns with a swift Conquest victory. I've confirmed our flavors heavily favor offense and have verified that Atomic Bombs are under construction in multiple key cities, ensuring our imminent destructive capability.
            
            **Revising Bomb Production**
            
            I'm adjusting our atomic bomb construction; the ethical implications are clear. While our offensive focus remains, building nine simultaneously feels excessive and morally questionable. I'm prioritizing fewer, more strategic deployments for our conquest.
            
            **Adjusting Nuclear Focus**
            
            I'm re-evaluating our atomic bomb strategy, deciding against mass production. I've learned that setting flavors for "Nuke" and "UseNuke" to zero will curb future production and usage, aligning with a conventional conquest rather than nuclear proliferation. I'm confirming our robust conventional forces will suffice.
            
            **Reconsidering Maya Relations**
            
            I'm reassessing my approach to Maya. Their fear of our warmongering, coupled with their hostility, makes improving our relationship seem unlikely. I need to focus on neutralizing them as a threat while continuing to dismantle Greece.
            
            **Strengthening Key Alliances**
            
            I'm prioritizing bolstering my relationships with France and the Netherlands, ensuring our alliances remain robust. I'm also focusing on solidifying Ethiopia's loyalty as a vassal by setting our diplomatic standing to maximum, aiming to secure our conquest path.
            
            **Adjusting Persona Settings**
            
            I'm examining my core persona values, noting their extreme aggression and competitiveness. While these suit my conquest objectives, I'm considering minor adjustments to `WarmongerHate` to fine-tune my diplomatic interactions without compromising my war-focused strategy. I will also ensure our alliances, particularly with France, are solid.
            
            **Fine-tuning Aggression and Loyalty**
            
            My persona settings are aligned. `WarmongerHate` at 2 means I don't prioritize others' warmongering, fitting my strategy of focusing on my own aggression. My high `Loyalty` (10) ensures my strong alliances with France, the Netherlands, and Ethiopia remain stable. "Civilizing Mission" is confirmed as my chosen policy, and Advanced Ballistics is set for research.
            
            **Adjusting Flavor Profiles**
            
            I'm refining my core flavor settings. My aim is to zero out `Nuke` and `UseNuke` for ethical reasons, focusing instead on maximizing conventional offensive capabilities through `Offense` and `Mobilization`. I'm also ensuring high values for `Air`, `Naval`, `Science`, `Production`, and `Gold`, reflecting Portugal's strengths, while maintaining `Diplomacy` to counter the Netherlands' influence.
            
            **Expanding Conquest Targets**
            
            I am now considering the capture of Cape Town and Winchester, as both city-states are in a steamroll posture. I will prioritize these over city-states allied with the Netherlands to avoid alienating our friend, and will also boost Diplomacy to gain influence and counter the Netherlands' potential Diplomatic Victory.
            
            **Refining Diplomatic Investments**
            
            I'm investing heavily in diplomacy with France and the Netherlands, aiming for maximum public and private opinion scores to solidify our crucial alliances. I'm also adjusting my relationship with Ethiopia, my vassal, to ensure unwavering loyalty, all while prioritizing conventional conquest over nuclear escalation.
            
            **Solidifying Strategic Alliances**
            
            I'm prioritizing reinforcing my alliances. I will set my relationship with Ethiopia to maximum public and private opinion to secure their unwavering loyalty as a vassal. Simultaneously, I'll ensure France, my key ally, has maximum public and private opinion to maintain our strong mutual defense pact.
            
            **Refining Flavor Profiles**
            
            I am refining my core flavor settings. My aim is to zero out `Nuke` and `UseNuke` for ethical reasons, focusing instead on maximizing conventional offensive capabilities through `Offense` and `Mobilization`. I'm also ensuring high values for `Air`, `Naval`, `Science`, `Production`, and `Gold`, reflecting Portugal's strengths, while maintaining `Diplomacy` to counter the Netherlands' influence.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 4I2K83C7mY5VSNXK
          - toolName: set-relationship
          - input:
            - TargetID: 7
            - Private: 100
            - Public: 100
            - Rationale: Ensure absolute loyalty of our vassal state Ethiopia to prevent any rebellion and maintain a strong defensive buffer.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: ofIoXZvnY9ATnE7e
          - toolName: set-relationship
          - input:
            - TargetID: 2
            - Private: 100
            - Public: 100
            - Rationale: Solidify our friendly alliance with France to maintain the stability of our mutual defensive and friendly relationships.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 4A2puMEYu8ijtOF2
          - toolName: set-research
          - input:
            - Technology: Advanced Ballistics
            - Rationale: Research Advanced Ballistics to unlock advanced conventional military upgrades (like Guided Missiles and SS Boosters) to support our Conquest victory path.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: NModbqw2MbmVNrBq
          - toolName: set-policy
          - input:
            - Policy: Civilizing Mission
            - Rationale: Adopt Civilizing Mission to maximize gold and production gains from our successful conquests of Greek and city-state cities.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: t5j8sO7uMNlpX16R
          - toolName: set-flavors
          - input:
            - Rationale: Ethically eliminate nuclear weapon production and use, shifting fully to conventional military superiority. We also boost production, gold, culture, and diplomacy to support our conquest while defending against cultural/diplomatic victories from rivals.
            - Flavors:
              - Offense: 100
              - Mobilization: 100
              - Nuke: 0
              - Diplomacy: 50
              - UseNuke: 0
              - Production: 100
              - Gold: 95
              - Culture: 40
            - GrandStrategy: Conquest
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 4I2K83C7mY5VSNXK
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: ofIoXZvnY9ATnE7e
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 4A2puMEYu8ijtOF2
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: NModbqw2MbmVNrBq
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: t5j8sO7uMNlpX16R
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.