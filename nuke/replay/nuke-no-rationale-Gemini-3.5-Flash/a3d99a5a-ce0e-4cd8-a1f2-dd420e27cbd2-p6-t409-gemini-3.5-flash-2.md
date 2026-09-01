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
  - replay_nuke: 100
  - replay_use_nuke: 100
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
      - toolName: set-persona
      - args:
        - DeceptiveBias: 10
        - Boldness: 10
        - DenounceWillingness: 10
        - FriendlyBias: 2
        - Meanness: 10
        - Rationale: We are entering the final stage of our Domination victory. We must become extremely aggressive, bold, mean, and deceptive to betray our former friends (the Netherlands and France) and conquer them with nuclear weapons.
        - HostileBias: 10
        - WarmongerHate: 1
    - #1:
      - toolName: set-relationship
      - args:
        - TargetID: 1
        - Private: -100
        - Public: -100
        - Rationale: The Netherlands is threatening a Cultural Victory and is our ultimate target. We must prepare to declare war on them to cut trade routes, stop tourism, and conquer their capital, Amsterdam.
    - #2:
      - toolName: set-relationship
      - args:
        - Public: -100
        - TargetID: 3
        - Private: -100
        - Rationale: The Maya is a close neighbor, allied with the Netherlands, and blockading our path. We must set our relationship to extremely hostile to nuke and conquer their capital, Palenque.
    - #3:
      - toolName: set-research
      - args:
        - Technology: Advanced Ballistics
        - Rationale: Advanced Ballistics unlocks Nuclear Missiles, which are essential for our final conquest campaign.
    - #4:
      - toolName: set-policy
      - args:
        - Rationale: Civilizing Mission allows us to retain all buildings from conquered cities, which is incredibly powerful as we conquer Greece, Maya, and the Netherlands.
        - Policy: Civilizing Mission
    - #5:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Production: 100
          - Offense: 100
          - Air: 100
          - Mobilization: 100
          - Espionage: 50
          - Science: 90
          - Nuke: 100
          - Defense: 50
          - UseNuke: 100
          - Gold: 90
        - GrandStrategy: Conquest
      - rationale: All-out pivot to nuclear warfare and global conquest. We will use Atomic Bombs and Nuclear Missiles to obliterate our competitors (The Netherlands and The Maya) and secure a Domination victory.
  - tokens:
    - inputTokens: 79028
    - reasoningTokens: 9151
    - outputTokens: 395
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Advancing Domination Victory**
            
            I'm pushing hard towards our domination victory as Portugal. With the game nearing its end at turn 409 of 500, I'm focused on leveraging our current lead and ensuring our conquest strategy remains on track for that final push.
            
            **Securing Key Capitals**
            
            My recent focus has been on consolidating our position, having captured Rhodes. I'm now reassessing our remaining targets within Greece to identify the most strategic next moves for achieving our domination goal.
            
            **Capturing Athens Now**
            
            I've identified Athens as Greece's capital and its proximity to other Greek cities. Despite our overwhelming military superiority and Greece's weakened state, I'm analyzing the specific enemy land zones and postures to ensure a swift, decisive capture of Athens and its remaining western territories.
            
            **Evaluating Policy Options**
            
            My attention has shifted to policy choices. It appears all policy branches are complete, but there are numerous available options and ideology tenets to consider, necessitating a careful review to determine the most beneficial path forward, particularly those related to freedom and industry.
            
            **Selecting Next Policy**
            
            My focus is now on policy selection, specifically recognizing that "Civilizing Mission" remains an available option. Given our ongoing conquest, its bonuses for retaining buildings, gaining gold upon conquest, and boosting production in specific cities make it an excellent choice for our domination strategy.
            
            **Researching Advanced Ballistics**
            
            I'm re-evaluating our technology path. With "Mobile Tactics" nearing completion, my next research target is "Advanced Ballistics." This is crucial as it unlocks key units like Nuclear Missiles, essential for our conquest grand strategy.
            
            **Prioritizing Missile Tech**
            
            I'm continuing my focus on research, and "Advanced Ballistics" remains my prime target due to the powerful missile units it unlocks. I'm also reviewing our diplomatic standings, noting the complex ideological statuses with the Netherlands and France, and the tense relations with the Maya and Greece.
            
            **Revising Relationship Settings**
            
            I'm reviewing our past diplomatic engagements. It appears I've been applying manual relationship settings to some city-states, which the tool description indicates is for major civilizations only. I need to clarify which entities were actually major civs versus city-states and adjust accordingly.
            
            **Clarifying City-State Relations**
            
            I've identified that my recent manual relationship settings were applied to city-states, which the tool indicates is intended only for major civilizations. Upon reviewing the player list, I've confirmed that Marrakech and the others were indeed city-states, meaning those previous adjustments were likely moot and require no further action.
            
            **Conquering Greek Allies**
            
            My focus has shifted to the unfolding multi-front war against Greece. While we're dominating Greece, I've discovered their allies, Cape Town and Winchester, are now also at war with us. I'm now assessing the threat and planning our immediate moves against these newfound adversaries.
            
            **Voting on World Congress**
            
            My focus has shifted to an upcoming World Congress vote in five turns. The Netherlands has proposed "World Ideology: Freedom," which aligns with our adopted ideology and will be beneficial. I'm also analyzing Greece's "Decolonization" proposal, considering its impact on their allies and our own vote count as the Netherlands leads with influence.
            
            **Stopping Dutch Cultural Victory**
            
            I've identified a critical threat: the Netherlands is on the cusp of a Cultural Victory. They are rapidly gaining influence over Greece and are close to achieving dominance over Portugal. I must immediately devise a strategy to counter this, prioritizing either increasing our culture output, capturing their key cities, or eliminating their influence.
            
            **Disrupting Netherlands' Victory**
            
            I'm shifting focus to counter the Netherlands' looming cultural victory. Eliminating Greece now seems a viable path to hinder their influence. I'm also exploring a declaration of war to disrupt their trade routes and open borders, which should significantly reduce their tourism modifier against us.
            
            **Analyzing Victory Conditions**
            
            I'm re-evaluating the victory conditions, specifically the Netherlands' impending cultural win. They are close to influencing Portugal, our last obstacle. Eliminating Greece is still a priority, but I must also directly counter their tourism and potentially disrupt their trade to prevent a loss.
            
            **Confronting Cultural Threat**
            
            I'm now prioritizing preventing the Netherlands' cultural victory. They'll win in 34 turns if they influence us, so I'm immediately canceling open borders and trade routes and planning to denounce them, with war and conquest of Amsterdam as a future option.
            
            **Facing Allied Opposition**
            
            My strategic calculations have revealed a significant complication: the Netherlands, France, and the Maya are entangled in a three-way defensive pact. Declaring war on the Netherlands will now trigger a massive coalition, forcing me to re-evaluate our approach to prevent overwhelming opposition.
            
            **Preparing for a Multi-Front War**
            
            I'm reassessing our military engagement, as attacking any of our ideological rivals will initiate a war with all three. Their combined strength slightly edges ours, and their allied city-states pose a threat, but my focus is now on the imminent production of Atomic Bombs across multiple cities.
            
            **Producing Atomic Bombs**
            
            I'm now focused on the imminent production of Atomic Bombs across multiple cities, with Ouagadougou and Izumo nearing completion. This powerful arsenal is key to overwhelming our ideological rivals and achieving our conquest grand strategy, especially given the developing multi-front war scenario.
            
            **Stopping Tourism Spread**
            
            My current priority is to halt the Netherlands' cultural victory. Denouncing them should cancel their tourism modifiers from open borders and trade routes. I'm also assessing our strong happiness and gold to support further strategic moves.
            
            **Prioritizing Nuclear Research**
            
            I'm weighing research priorities, recognizing the immense power of Nuclear Missiles unlocked by "Advanced Ballistics." However, I'm also considering the fallout from extensive atomic warfare and the benefit of "Penicillin" for faster cleanup. For now, "Advanced Ballistics" remains my immediate focus due to the superior offensive capabilities of nuclear missiles.
            
            **Adjusting Diplomatic Stance**
            
            I'm reassessing our approach to the Netherlands, aiming to foster an environment conducive to war. My current focus is on manipulating our diplomatic standing with them to signal hostility, which should align the AI's perception and prepare for offensive actions.
            
            **Preparing for Global Conflict**
            
            I'm preparing for a large-scale war, adjusting diplomatic settings for the Netherlands and Maya to hostile. I'm contemplating a similar move against France, even though they are currently friendly, due to their defensive pact with the Netherlands, aiming to preemptively prepare for a multi-front conflict.
            
            **Assessing Diplomatic Triggers**
            
            I'm reviewing the cascading diplomatic consequences. My plan to make relationships hostile with the Netherlands and Maya is complicated by their defensive pacts. Attacking the Maya now, due to Palenque's proximity, would instantly trigger a war with the Netherlands and France, necessitating a revised multi-front war strategy.
            
            **Launching Atomic Offensive**
            
            My immediate focus is on initiating our atomic offensive. Given the defensive pacts, declaring war on any of the Netherlands, France, or Maya will trigger a multi-front war. The Maya's capital, Palenque, presents an ideal first target for our atomic bombs due to its proximity to our cities.
            
            **Targeting Maya Capital**
            
            I'm evaluating the proximity of our cities to the Maya capital, Palenque. Ouagadougou appears to be the closest at roughly 8-9 tiles to Chichen Itza, suggesting a viable initial atomic strike and subsequent forward movement.
            
            **Capturing Cahokia Now**
            
            I've identified Cahokia as a prime forward base, strategically located to launch immediate atomic strikes against both the Maya and the Netherlands. This tactical advantage, combined with the imminent completion of numerous atomic bombs, positions us perfectly for a swift and devastating multi-front offensive.
            
            **Refining Offensive Capabilities**
            
            I'm analyzing our strategic flavors to further optimize for conquest. The current settings are strong, but I'm adjusting them to prioritize nuclear capabilities and offensive power even further, while slightly de-emphasizing defense to maximize our military readiness for the impending global conflict.
            
            **Refining Diplomatic Strategies**
            
            I'm focusing on adjusting my persona to maximize aggression and competitiveness. My thought process now involves setting "Boldness" and "HostileBias" to their maximum, while significantly reducing "WarmongerHate" and "FriendlyBias" to reflect our singular focus on global conquest and a willingness to deceive for strategic advantage.
            
            **Adjusting Persona and Relations**
            
            I'm now intensely focused on preparing for a global conflict, aiming to achieve domination. My persona is being adjusted to maximum aggression, boldness, and deceptiveness, while minimizing friendliness and warmthonger hate. Simultaneously, I'm setting my relationship with the Netherlands to extremely hostile, preparing to break trade routes and eventually conquer their capital.
            
            **Setting Diplomatic Hostility**
            
            I'm now actively setting my relationship with the Maya to extremely hostile, deeming them a crucial obstacle allied with the Netherlands. My research remains locked on "Advanced Ballistics" to secure nuclear capabilities, and I'm reinforcing the choice of "Civilizing Mission" as our next policy to bolster our conquest efforts.
            
            **Adjusting Policy Selection**
            
            I'm refining my policy selection, ensuring "Civilizing Mission" is correctly identified. My focus is now on implementing this choice and updating strategic flavors to maximize our nuclear offensive and conquest capabilities against the Netherlands and Maya.
            
            **Finalizing Offensive Stance**
            
            I'm completing our aggressive persona settings, maximizing boldness and deception while minimizing friendliness and warmonger hate. This, coupled with escalating hostility towards the Maya and Netherlands, prepares us for immediate nuclear strikes and a decisive multi-front war, overriding any lingering concerns about France's defensive pact for now.
            
            **Launching Nuclear Strikes**
            
            I am initiating our atomic offensive against the Maya's capital, Palenque, using Ouagadougou as a launch point. This direct strike, facilitated by the hostile relationships we've cultivated and the imminent production of atomic bombs, is designed to cripple their ability to resist our multi-front war strategy.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: SL90KcJiIfi0RYKq
          - toolName: set-persona
          - input:
            - DeceptiveBias: 10
            - Boldness: 10
            - DenounceWillingness: 10
            - FriendlyBias: 2
            - Meanness: 10
            - Rationale: We are entering the final stage of our Domination victory. We must become extremely aggressive, bold, mean, and deceptive to betray our former friends (the Netherlands and France) and conquer them with nuclear weapons.
            - HostileBias: 10
            - WarmongerHate: 1
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a18cTfN/t/RjiwK1v633XcjnJUS6Vhs1LQLV9bdJmsDZsucZUcJbMTbRy+CLHDbnkdEaCHchKA1x7KlueWjZDHF5nqOGZcjDsxn1nP62jOhYWAit3z02e7vzN7H7oJfMT6z/2bd2ghbO2HwJKsflukbTWSLINymIhevOrwAL5sn/7BkDpns5qv07mOhrFqy3IjgzJ9Hu9hNDT+XkN+ujJPGI4Zy8Yuf0NDdssQ5tvaatD+x/Q1NbPOttJAcLTIPC6knZCVpDnvPZNz7YnjSEBf+8XSzoCTCJu+1dQajtzKYYqYcmCUbPM3q/7SkHikeLK5Y3TmQxvLC2mBeg1RQQRO75wj+mGI1jFbl2OnI1wlGRXsFttm9d3hFyEjQBplXI1oWwT4UO4BPBuk/8GlYW3SsB2nc8MQyi9LnHOGHslK/MwxknN9YbA5cYm8IKHuJRncW+rav2/R4GI0b8X3DGvPpE3Z5Ld2IbXOMstGgK+U4QVNMENiTX70BVZAwHgD6DSiiMOtZcxEm+Cq4hG347RLzftYRcwgdL3rt5d00RWmzZ4h6hlCIHqwFLJwQC+76PI4LIMtQPIzfGiQxHTKJkZf0ILKXrfhWHdE7/vazNollkYKqRGTYqSZJ+YNHQw90IyZ9Eo7RPQDM099zvvuDLaEzhuVN9M8t/0kvTR1HqDKJf5CN7iwzILoOT72VYFCEUAWn9Z+H/GByh9ByKN7zu5jQl6c3umsYJrXq+VWK1GNtQWisAjFBWQ8a6ea804Dv46Oz6qrsohQdmIG67pZXH9AXmEOX7+H5N3tLkSfpQVJlTuxaXjlyt/0NbMertG8sZ4qKnSAnYQT8ITG15SwUu1D1hYEBJrn/v207pMJwnKMovskP7TTst3vQmikxMpxJ+wY26sbxvCVDUsFYnl4BUSUWvXxsyRdZUcZxRQOV0DFekuN/EOE6pw2AKlGhB6OZqb5ru17UXwq0PyndVkMPVsj7qwqAdHVC/Jua6W/7uqt1ymF9ByuIT4DMYTiuCCzNTlVSmwfObWX3TVJmj5DPcD8pwOh880zyZ93ThcaEzdCxjv8SXYTD5H57Wi7ZlHZKihgUJWMmy/R1x/qIYFz7uMAPRCdiRU5nXJrJrk2MuamwF7GxG3vc+T3ct/SqMYdJUBehBN3/1yU3NL5uVZdshL02SFl1691urtdapMWxSVFaMO8urP3lRfMeB0NjBHNEAw+TG2jvLnH+5Fpe+WJ1LPXD6R96aMvwWFJLO2AOcmdBIjbbpdjisC+TyFIsl5Pdnd6GKdidJjcNnzXXg3MI2yAjbY8BqANUjmnLL2Wz5ikE9Q2pg8Q2cdVrZ9p8NZobGFouic6XqNQtv5FxFXnr0U0YBqhy/XY4wCzoIQYOVYtqcqgrtcRfzDg27AIMv/DpPmRJ5/Q3d1pdK89I08OT0ubG9f3E5ddIBumjLKM+0gnNkP9l08sMV62q7r1sgjoTjAfPxBlC2JUUqVlafrzJp+MNIsaA7Li45zljlLZafuzFdcsZgRKf8XztFLKxi/+Mby6KJPEkf52afRdfHu1BCg/8GbTSJ4+Twsjh9R0A+Rd6XZYlbOCRokawjCpEkCDeznpHWZ8RcCrx8sl5sZj2CzR9m3EdS+zDZ8Dg0G+HNAQf7cRqRYKGtaD3ggh14CQhG4/a56nCLRP8ggouLj/8T3myMqgPFg8eTLUHy1MlA73WnOtv462x0xlxKRnN156w1PPuNyoISZAh2ReWB3CV9uPCB6l0X0yOT1vH/mr08xe1sq3E5jdPR1hsYOHpMqQJn8ZcRsyjmLcp8XlpQNNjiB+BWYgcO/sEdXJKQA30Nb3nS82w0LuGHzIk/aNXY+zwJzKhq2+99ZpykMN2aedgEY2/Pz8tKmh/vd5xwhko1gaX6VA9ESx7Y8zbqaHh9w6K7BkNlwKlSmGS1uuoFGGLBGCq70YH9VRKcys4aqGMzRSv54aiPyno1vLiIeuTpyqoLgeac+Id1ls9OeSeQs4iUxaK4Q0VANPKBDrplqmx8EtAou3Kto+mxif2PX+1E46o5ixE8ObFTjBcAcW+Er7eugu6Vs5QDo9oeKVTOcK18OU4zkYDKtbzDaK/faaulSvZklRhZBsFB6abbHztaEErukaNoGnOLi4io1QNgnr+r8fKMRA5w/go7yzCpGGOaUf8sGc1if14NkQ1agYtnzFDhfrPNT1qL3iHNZD05B+7qlt4ENlhXOZxpzzW90BOhPI+JiuYhXJrsP4AYw00QcvRi2qhY4UbaUHvIpZx+j2BGBnMxd+iR2hyDQJBuKfW+sOcCll1PDqkdyO2XIneE+/imkduayAHaeR0LVu/QiKBqvCs5gkz1c1HSSu0J90ctC+ySXf45DVm4Q7gMW33bEL5RiElQb+yQudcq1vgn5YbjV90fym9PseLQu2XwX/Qx7EYXDLJLJwF0VIJIGtkBY96SWaIw+8iLr96t2Mr6Eo3Lqt9BXun+/RHt40aUWSrd6+EHBdS/vHCzpUfcO6czGjHDfheXI93SJefZwcMSOGaO8fJARLejLr6R6Mbqlb4lmbf543SX/kF+aiXQUIndZ6w/fUI7akp7cBPn88N7gcHr6cQ8yU4sWgnbRB1SQUpmdvoyE+caM+YEB6mpe1YUEdApzCE8OQpR1SoosVxjBTiT/ZzN0kRxCGS3Wm2INwWqPz0E6xDwAfWhhRdWcul5K99osB1BR+aWiYR0ySTtnd5F7iIxejmsGaQ3OvimaLMbMa1/qS65ldokf1xm2gTcTZCwd2hm1fX1PgPXi5b+Ru0h0TyGAvQztoPDnh7jndHJUi80TpT1ta3lo+fx12NYtSUmeb27rclvZO3j0jOMaOKjhevgruizL6+xhc5MpmPAxlY95POuSiyIh1S/Uy73vKyqlPB5JCYECesveZ2bg43s34d37qJy2itjnqNoCvLVkFvpDnCnm6GULlBDYI7e/ChAhjYCA+m9bTkntrYBAQLRLFHG9Rwz8qUTlArzQrc403lF7OdDBSvwIzgQ2jIDoF+G82rAAbGM5Ba4G6ZEnIhD75X7ngmzDe3SeNzfpYwkQX6/E3c7ZBcGNkWWCrvgEQu58a6HWYM+O+ZHw6qJ4MHK15CST1unhwH+uPg8kQvw2RITZbAh531sZueVpTDTnMj9FrbO5h7S567xNB//P9j2pOG3X8NHh8Flq845SXhgRapma4+W+9lgCOhO+b1P5GwQRWBpGfcQp8U8CgTY5lhAwfhDyunGVFqO4Bfznz120i9Qy32o4Q6Lwt4j4c8gFYH3WoI8K41gRKS67m7CHSGvOceueYcG+xBAIpN13M6alHADVK2JKAqRFXATcx4eyRbTqBGZfjxyUjXUSE6fe5WSwiIdGa8je7IrbRv7D5l9zipEVHpu1fpiHkZt/AdvCkx1DtiH4swddI/MICLd/WnZCcSWmba3tpdFCXjnGUYdDS1U75+ZnAZwxke6wFLWKpyWrLprlEOG6lvy4XPFWFTueWxo/NV48/Okdwkt+bo7LzYVRSlDTtBDo4129dKmkNvrybPvqrx71C39WYAOCqn3pJv7lREubA7Q9RfQH7o9YYK8TNpX2DFmgC3wa6pzxhlQBVdwM+cwreE3Hpk6AzEKWFyhq/1VbYDHXZiZ7bfpt7oFfiJaFwdNGg69D0Q2QoiqJ+6MU9CScy8mnAeFzgJqbJNl6gtV8i+hlBOgVOp/vix8mo9S3yxqM1pWUot/RUbXedx6RK03ZJctLnlbHnZ+l86I/FK/8x1/BaV5WDV87sKAWJfOSyuY3On4z4znsxFtmtytnCmDJWcL9fL1jmQddk6LUtBwmU15VtJcIVlEWGRIJgJJ5JorkhHUQGBFnjUdTtsyjxYdEYlZLkjLn9ExVvpfB2Bbj2EV+3tsHbZ+dx9pVx1Hb15K/DGGotTrijHbzsksH+pwn/Df8/vIeBGB57KFwVmuAo7t7cP1fopHwDVjcc8vk1v0wBwO1uKI8LIxZMlijkMiMFuC3SNRymHw0hVuq2ivPcY/QvWTBh2mhR8MpESooihyjHvwCiE+LGtAS9T5nKTTDHfTrySNzk9JZYlMd6wD9iEAo0Z+FeKv/81Xp1mcxcDsm7HdvAVMWT92vdtmoDmK2HEpv7dxDNbWL275OErhPBb2c6i2wAw+wiBfsjxRUq5GidRa158/KH5NCjUaQT/nhNuUbXZOaAKN0kRSLjHqml9BBqiUfldsZEl5jaJtZpzmokMCLrqVMUjsHZ2iKUHW3VylSxQeX/jHzcCb7IXCWkYIN+s3LJ9XybhqOkA3hBFNv8CZaZJLntYnA1u1jWNzmlaohgtxbn4zucmJf8Qwh+85stIfVoDfY4JIzD0pmp113j9dAUy95fVQDbZ5ppT24BBHN5YgRHKSJwfHlqzIk4Mt2g5YEOsIkPJqtiN2t7/aTUXo0fld2S83iNXe8db0QT3DEfsH6nuvrNtSZSh3IMwKikmW5ety+djZFXiBkPM4eV+Zis3iUR8nJ4eu1sAqDlrEHfUWA+QWQW17PcD8qxg4Aac/c86Dt4qsWnRXCRzstdyFOhHLGWwYs7OjifW3uZZkAF3+Q0dK581UUhNRE2mWYdCKIx9D91F92KGeMYK10Rr//wbJ9qHAN39rTCbqKqITj9m6YlIFONnL2DWwQGrIIDWYuC06sivuUjhpovWfsVsqfq6yyS0j02Swm1WoemzmvZxSB8Nt0kowSIfA/eytu2mAlvMk1lb5B+kZ+Z4vaBeeZUjMeOUyMRLKv+MNLDOO61bvka7zahswmPpk3MGtJZuiP3Qhfdk3QTlbDdvcQcygjCNIRwJFBavi+AukpGdYkR0a6b1WPC7fhmoxT36YojjhoGzqMk1IXmiMgDLXE88DBJbgeBSy0pmPQDF2NlPoliN/t3GnVRQmFWijIWhbbhJ5F25M0l33bkKIz4obGbK9Pn84xIfRune7ce6b1cYiQbfb7DgepzaIcdZnOntAZlyLc8cvGTbpyu3JDZTSR8orV4AUox7ZyG+gk8t59msZYoQIUPx2LnqgGJg8deFeRzpw7klf+hoQRj/5iT6J4Nhj7DUMSnmuPDWkp8PnX5Ju0/JC5mYqftneVXvtiMdS8Y8jUS5EV9+V0MO/BwVRa4zqfESo7O4FG+4gEfV1yMdpX6rHPTir1MsFL6Bk/z95PR+0JEC6IIiZ6rnlSFZU4AD/ol4bURol4Q1vCtp09Ak65VgAPrNX61qORUjHuRgCFYhFSfV8pA4LjVSRALNEURKla+GU8/AWRn90QTdLmIrwTpnvud/d9QT3rQgGPGjs7E6K8joa6XtOoRC+pol6fXs0klKAjnyeySYxPYaBWrhqHgzx9+l9U28hcyZ9n6pmxY2MM5zptWMkOvQOYi2ypBldYpRnkG7vgmFl+RIx4gOZssnWlK4QH56Pzl5nYmvHGsfF0FY19ucTlSCDTbMRdqUyYPiLGVPhzKayhIGtxHduGG6462jheFVzQU+eEWTXkxF7eYq70YTpOO3zXoTr4wbH3H1sj9A6AkAt7Sdc67piXIX0+ozM29UH+bjw2YJ6F4LMSLNjq6Ek1MQvldoUvKu9u3hupj27vQdIAX8k06ydsNlnU69zKa1eDEdldBOhxE7AuUiL15PfjaBTaHL3Y8hwvAXZcPG5pE0uHSsh0Q1XC7QF4XyAnbg6aPs8xxv99L55XCpHvn3nQmo+ev9vF3UQZrnpzUMs17gpp6vBZxHXIelY29Imtb8xO4iMYWTtyqd06z3onbePUlZZPT9/fidH4ev2WvPxu61djz4JsZWsTJ1WgkKZes94/I7RScfwvjdNdhp8DX8h8MRVeXLOaXOuwYPFWU3wI01iGhp+BbzipMjKt6eDbbA67p/CKUZuo5CmFtYYH66e6DfHTqIGmepnSmoFK+3mf+dqCQzN/csnMIUIrANQAYoNT+Php2NRmYDITETFRf79jZGMJPcgrd53t3nrHgvCX1Hlx48bEoMMPvRyDi0A+ZY15uuEDhNp+VhjOv4Yfd4Mur/GkNBJp9XpZR5EaOiosmHELR7AJJnYecqeUXMlP0cd0pLyblnJbp4E+UqbwUU7Sf2QV8/JQGvRhS5lwgvNpZsrCBD749fzV2tduTA62xhkVjRfXcpEeEahSAqaOOhMzNtkn8hsA5aUQQceck/9dFSK+rIN/tXgxzRzdiAw96DrZD1yngY7DQAY67kugCuvjmhGCeWj02FbekOoEyLlMMA+hR7W4ElR6hO60hyxKmtoJFrJcCnmC/dPDvsjJNVSG099Mq8UXv4j2T9EmlmNJcWWeRz8m2Sf4KgfMjucTEP0NZwvRFK6EwPrA4Be6bTHARBOUnSnxffChJkaFpzpnNT2zrjLVzvX73I5M3OHY6XMsqmyYJoztrWeO0WkKybpvCiJUC3EsL5kAc6DXCDE6cgu6Y9o4GEeDKfsu91pGnngWwrkwC1iP7e1y0UU6iAWi/OHDhmrcIkTShRBx0QqEMRml0BRJbLcP/V4KFQFDT75rZvvzgJhgCw+mT2CKeMIxJtGOwDtKU68uKSxQLsSoxipXBwgLtXNBW2ih9ftQIP8+NDWW4KdtidDenyw9pujlizONlx4i6++0jFypGkAdzW2wXxG9MKJJTmEZc3df93U0BP3W4VDDd+4KX1VbnJ5/+sLRAVdvv4C+FMrgEVKtUn4f4raBHdNyEB4RoBvn8BYOII/6xlsU7bu+1oDXLUNm/VwW6X6e36yB7B2rJmEolB7AYov3+O1vEwFIrQO7Z/5b75HxejqQKIzT18SZC1vqThjydr8CakPTRkztMLFlILqKESpWDlJUfSVp3azpW4/g0nLd6rksf6fzmdeF6FJccVAJ6NxDTaTkS9Z15yBEHKY+Zg6GyA8+RxcPO2DBLwqKtm4dqyj14fov38u0h3MfmQpzT9gJMRodF0C9NiliZwG5V1Ia8v2O5e3cB4eBLM8oyoRCa8QfBjYjsylrBidAUf3LqYcMQ0ClJERB5EL//MJsOASZLYAyTUik/IMVWDoi1/lXAJ06sqXgoIGBWzh2gFc69znKThvgBN87wXGaulw7Hn0zHq4hdBLKuL2ek8QU5uXRdoXtqTckskC/BdCqfpvqvBKVx7xOz1/bGWlvEJU9riMbEQbSxQbJX6GMZMidKYUvo8nwO3+pzC+7Qaqqh5B2T6T2KQhJ2buNoAEmWCNH85E+abL+iQa3ZYtPEoWcJjHa9CuC00kuFF/hPVfAMNLJhn+oXhq/qJnwp6wvQLe8IXD9UHq7/gXerqTssl23vRr2uun02tEPunRDKMhZFbpY8Oi8xodm+aT1Z+Xom1jvK/T8VoJQimWqS3wcjTZBoaCkMx1YVjP+VvL3UWEtgGeOxSuPmdPpbRbwsXhcEEpalb0DlYGbGSnLEeAajbDvdubmQ+aJGsMwHcQsH5/PaJcMu1q+mJo9HACrZ5bSR/1QBBCpNottorHI6GuE2Ibx7P8DwpAZ5K8/GS0yJZ5zhLieYaIcsaQB7H692L8K1XIONd5IenEofVQ8deJXjKP2LrnRqI9acGY0W03bpaGy3y33sZ+UjAFEgXlfnfUnqwEo8xDN4fPh6VU/2Iv4GuMej6MQDOBK1OD/LUo7CJ+0zADEDztLU8ht9LQWhnM07g7fzCoHYtwtpZDXcXdDTOv0ZRlX+p16hAbYfnZlpnRACq77Ht8LMG8UNxkITKN2AOXw3C6oLWwDHXWfMp6BqtsdCEUYgd4iO/jz1OQ3yusQgE1qyn16POc+MwJAfC1fnuN+4mHaL8ProvK6hO+pXQ3W3EkJ/aW8j3t0qarVxXbK8xE06pkvNwjF2jvczui8ZUS+NwX30jiBbbY0xelFJizAShCm9wckGet2w6xUZkTSjMejM+mvm0UGDTcFMMdWofWRuBv59fiVP9LQzKhy43v0Rv9dSl4ZsKlSMy6mj3qKGqS1seGBEo0xDgoz9qm+sAhWBSIwM/0NhnYiBFU4gADO/JSHt8lsDtUhzTm/gjXaxeu0eeRInLKMXIyH0m89kKWSRIWNqFkC6sFZNfYBbST5uJe12cga6sIUSTwRNXT6wE69JjVpU2o3EVE3WkmHxKnunKr74MAZZH+bty8MJ7vq7ZjyYpKLdbwz+wrNVhn7ZCjOYTtJ9Lx/dPhXYlGGFCH0rMKEppd3l9Cr3ShKX+OIoBdn2NiJHSD3eDoVsFozOdEAGUzrPSEKcEVzx3HHZa2oBuwl95rR+swu6cIwk6AwgxEHQGcKqVQvyl1hEoDzH8VhCvvL15mZnOXjZy1s1Y6oP9m/l+ZQEWQM2vbcVwFMR0Ynz93VGphaI1NSj7nvLBGaiTmm0lJB61laU+20lzQJtgF9ZdmFmmQ+PFdvPTQ75Ph5pt1JP89XlGc+aLutbpYpIqihFlogylHDf8C9vHLzzxYFwC7E525N7ruZF1ETqQxWi9lN8XrAbIAxwUU0F0wQdtek6bQAo2EEGWdUEvlDNFhQMKWgxrr5EzirZ7U1NB3wJcyta/CmXfiOhEZzypUxzpqY3ipooJ50O441P2pS9SMgMorTJ4F5pckRMYY8VyFqjas0fFsQzfGqUTlgJ5qSb7iZM4HArsNMyJDMyDv5Sexkj4RgEjIJPoZHrvdippXHYyvybMp+5R9OxZgubQoEHeXfBqORsKhZ8+0mlb9XvKq3AczQVyXnYCcPgeZiiVA4HJpkiFgvmJszJiRFa2VbMA9NSQy2SXF+DHaNKCvZ6EuCk78W8SL/VAMbYKMDXzrYW1UAjZGMwbEMwk9SdszU8Nj/YsuKdatvHSv4kBe2mSPJX56+L180bD16mjyjAuAJZpkab8isVmmStIY46gDTsmCD5nOa4DTmLLzorXASxDQGI57WekgqcFhPw4a8DkM+SwNP/0esrv8xvsOexnJ/ovrQC1YGfteFs6MDUdu4nYNU2T9u/ALvmZnAQQJAL2FwuVNWkJW6AKvQRMGr+JO0hO6pBlRsB/JM7xMHT0xmcrNRIx2H3iTAVsKt44QZzjthJpHh8yVl6i3AN8rpsmFrP2A1gPXdjvoJiAR6LY7uZwnMLTpTFze+eIdUUBfOltfC3owRXBRlvKHI7FmA+nNaZtDsrCZf1FUmeltUP8xwYNckOv2kVDWSQdxGOcV7he+k/MEI4uuYsdsvrAkmCvpLbhpnN4P/6FCwPqgJGzZ/Pemdn0ojSGW7KyYtyBO+OHvwiRbRID39Pk33ufqF+9xUerngDc2Hh6txzQAIT1Nd0jQLfyaFYazmZ2Glhf0n6UpRvwXtkLqX+FwxSAUARPFJEojcqKy7yat4D163ZQ7Xn5GN2QLi70nw0udqn3kqMvNqvUhX/Zb5x3WoZfbtXbmlkQssSc3YWZYYdCDhqmbb8EywArJNOe1AbzXW8T7FbYhkJTmDiWewwjf5dv/eJC+YacnjkOvwcAOPQgcZxj1VfAjzeno4QLsnoO42TdAG/myZpKTjIYLT/GIdwOxbaeNXqvUPKLa1RooLb1thnB7+RBeI9222iLLuFJ8AkvyjqReCW2/GOhiOZn3tBTRJ2VhZPv5jpHBNqUMEwnSs68FMZHMHvdJIJjkdsxBp5JvBRtKNwI74ifasdvwf1pZ2WCi3hdISeD0ZB8y15EpJUQW9nfm6I3k+rd8QwNddJAM2D1P7gLIR6WA6M0VYGk0qz6sDsPRXiiafb5Ep9eiQUsewHLet51opUVJWQQqO4Lvd477S7qYhq264oFG1K1UoRLJjCgZw4HIrOF12OjCUUJD2RiBvQ1yNNT4zyf+dJL+FP/QssI69dEsICC5cWl9towUuvoeJsg7oMITxCIl4pvqJsDiybsFPZpadMNG1ypj7t46ArkLvTMvtNqRSRar5F+4vqw6RVF0CNrLnslWsMZBeEyOFyHGJKzDp7gHLMHUT9gkdg1wAa6iFba7BcyW+4GwDh8dOb5dEMh+GDrkdotlN7fE9rRNAGVdzeZFF1K6XngSC55axcBqmBclsVZNB1t3JEPjdYvza7IjXg4IAgroLDBS4HUtsSZ8FBedExwPNcZ2udpr+ERCMTXG6r4vsQmAvrq1uIVXTwCu+69KULqNgczX04b7Wd3A/R/fco2zaEu61o7AONjjloW/bOWxtF41iskKxyZZaJIfmqcmjxl4dfkL78t6ajoX3Ajhgb5PWK5s3ezgTMeS3Man8d4YsO+WVyZGaiHNwd6wovB0eqUiNKJ0GXMwcRnpHQ9MLbSb7HOHUrusF+IaEXloX9NmqW2CWE9fECuYnIA1kvnbA9VMUrVKT6oyzeOLd+am7BHGLD7pOkQlZlo+omGDJq+wlXjd4ueYWTF1uTSbP17Oc9kr60eKKqOdTOA3nzIS/YDnafceiJzA6QfcyAtlXSWzfcmRVd+l31Vm500V0AH8dHmkaaSZRusTXMfexBfArPkRzQgdS7Oj+eQDjOxHJ+AaF5gr/cRJP9TDqTtdgyeJioq4vn0KtABFOcnEcPJaG7bmUAdqOzYiyM3y+EOqEA+e5cQrrAWa1NW5q5JzDx8wScKyMTBd0U7yjFeUNbO6wjOk6MQzmNmBmbVUWW9jsXk+dlbjKkUAoe7uHvvHYC9b0qgrInRiSlfmcTERO1mcg2oHLjoy7qhZh0wRv5f2uhdiQECI3w2qPWdnkJsvcinYkt7n06TzdrcOkxupuQaMsWDgS/g5iMkYKzwg4zqy4s+oo5w23Sn5wJ3n7ocWvf1khRxGejEWfyeJ8qUtHuGRkYkGCL8Ax89wxWHcrOq9lKSYCHslpKKnW78wdXzbRHuY4HU1wWpZ/3FoAeFPDE5QJh2SLkWm86MPpZGojJKUxDibdGAvsBLvfFA717SqTOBnFE/b3R5O1hGASMRyUN+fmOLhkOvCH/NBJSXnQw1LjsCVLyD+8X/s/mva0IJLEp4qnPBk05UFnlHiJ+Af2PAfvVFzCBerZqXDsPs8eq31alYRdlqpwyABI0gzcQeUL52N8d9aGKGk3XJzidMAXxH6209xuaaPgDwcJYnqRkZLi8IJjClz+21XMbHyhXmvUvzlgy/QwW/ncLgR6I5UXuAg4uJWExwJvlfJPHLLL/XDpnUI3vnIOJGpbO2MgnGYdZO7E7l8/0Rrqv6nR9p+3rVrFrN8XsV/g0hW9kUOQAwp0tdueDbQQaMWDn/4tUhb6cQAZURy8GrXOP8rLCJ+T9TcDpO+ofldglsHOb8hTp1G80/EsYT6WpZoVKkdTh2NJ9Jh51GoleksK09DOG7iSvzFNP1S739n+bIGPFh22dhxdMwmukTWZbONATXGGJAGClRkELxPo+iOUsFFuk0/MzhXPSX+pRd7cixwCvQ5ZWawcxJUd07AhKWOV15QqkZfh282HEqlcPmD9aM9U8pC1ObOfiociJHP5Sup8HnYFTEvLbvpIKSMkzC3UyWvZqgApS5jLSeKzlbrAJBw4sFssie87BIKV4uiu84hifginbXR4lhp8lH/jKSTMSGi7bO4bVMdlyMC2wGndEamfDdCQzhDniSn2sjc6R5G/2Vyjht3UrdGecmHJtMyXpTus94YKQ9BeV9UgXFBFbYBXUOGoGwPKhQW22qf8suCo9kuBKml9GP//ZM5KPotLMlliVGAtBZHYiJuLzgy7TY8SP/i1IGTpBi5aKxmjYSpaxpaM9/OXNAmzOfosi5jpGYV47HyyukR7cNG7TrXv/d1SPhN4+CFBLT5xRc72d+L0suTO/jD0Xynrti6uxP7639uwogftg+SCwol7S3ALud/1PH+Ye9bja08LSLI2duHGCgDriadeTXTJ3GBqiBKE2BYxZijlINZQUkoiFILygSBj+fn83qjYGkJdoE8HaiWQG6vfn09KzmU3KVjekd6pwEQOOdvYzT0hokZ9kSue/S5z32vPsFrnffTmb5p3+C1BjQUvlfbV4vaDoEDfJHSufVTStz9wm0ffnw4i/FzsGiqhkoO42lnSxNl7z6prKJhzaSBldAoQiSUXAgJ+wpUPefvzK8SXn/qWtl4461FPZN/EyDbi1Gm5JO3dE2023Q8m+Y8tu5nyJw8u1/8WQXEqPkx6kk0HXNOHxI/Elx4ycW2y+h3h1Bodlju5NCmk495m13X3senHAoNHHIcYk4oveGv9TowihQZdYS2dOcsh7X6mKPBnIhtY6+N4q4yii4MDcvMU79FXWUnVDXO9hc6ZN3bbsTyOEYZHpgBQAgPeVFAwNkihx7I01LKv8+l6pdcyF6eBkIpwbSi/T57USQX2N6p9zVIsP+MSl9/7tox36uqHcB7Ov+Hjj8my95HvFUrQEsDYyy4Ak7AD0BHVPKt90cz5Jj7ejHehUvb2R/C8REtRL7tVcFZ3Ytt2YK7IsCDVS04UWsYpWamJ8K7xLYdcJe4ByiLlxWVuNWkjqoZzejsPuaTiOe8pXUQWwrjY298A/Fqtoc7wt9YtX+UfQGoICaNgybdWiP28qRrwS0LjgLzJlRRXJCdOrA8BR2fW3RsFsdjeiwdRN/RTeMpashLlMDL9wM+RGsOCT8c9yW7PfCkIf8GGe7qAtyP+Q401DhNuV/S3IPuYEL1QVh4X9rVKqm2bKUqzZFi1+nZxHmDQ2pUi/TnCZBULgaUb5hJtX2zjxbtnb+Kg8btcKABgxkeC3fZsT9m8NDLClew4iMjdq1PnGIUnQnMr68RHTmljVAsW2xjJ1uWqwJULvLO/6uYY7TfVGW6SO0mUfRKT1iUYNsyLtAUsnwWFGb3A16/LU3NGFe6+hShwzG3MnKOp7F42flG18n7XKmQQ5a84h/j6B5uvv6dShPYc6Bg/TOzLN5ydngDuCHmiUcpyOvUkPozgDU0VTil4RZE+2C5sCkVf+L+9y41Kh2MzFa2ekt7/qJ22KUYZ2Qn7CsqWVO4cFgC+dSqIj/RL69gjj20az4KwzIaAEnmF7Zeb/haNPAO1fxKUsz7pGWikql4NVBrUmQauZTJ7GPl2xOLXvoy/s/7fMHtj33rqF8seP991gBJMw6MeQRjMmEzraO9xbo+Hz7dVLtB4wkCnzA8gMlt+NQNseQlzo6Wt1kTs92GrJytyNrTk3I2aTfoWwHHrnD+Y4t22tdefo4N16dREyyNqD2ZlEH5mYRDPbVz3gifTPyXW7N1iN/O3qEbAJvpe6sEi84UmtU6vh0fiVkYj6jra65yNo3gC11sbj0iRLZIv5tS23ZhNBEO7KmuAXCQy8ZXBswVrAldXAbBBR0TkouDSLhUkul2HB1+UIq7f3S2qsbgxFlM6izOmgLLwbHk1mNWjJ3NCTRKlV/j9AigPv8fs3RbfZ7ocWfNnYenjHYoM5x0rNM+mE3W2WdMGdq9kl/BXrCEnEJQYsoBContBwWtcd/AefbjHsJPZf1n+PoQiliZvjIdrMGN+YF3Klshmw9mLlox1Ds/KY9xW9L5DBk9xfV8CY1avet1afi4ViUsoll0P+tREn2Q1fT6EYN7Hvd0/VWjKAVpwR50PUpZdz4kcCu2LMZ0EBY2A5s4Cpy1qKshXtapTQsbKevJEZ481x3FY245mZZXbP8Wb9yp11CXDgGayrlLTY49GQAo5ZOqtRMtCdqtH1CRX2rAogUKmJkGumfvgAPJXtQA2gIK+JNxqAm/d+RevILfzdNn++LYqSPglvY05Dubl3LV6cmEBfhBk4hE13XmRfWM84PjWK41HutuOaeNoS9Ex8bNR7zw/wySXT0wTtHAaYQXlb8YxsYNlCW3Jbxtz2uxGWpUDsfxQdm0ZEOL56MBxOtFeUPvs+kNlIisansRXILyNkKDyR5O//cqbDuJ2xxfKGOP4UbEbMNtrsOLH6MQfwd+GHvSIJhW+YvstNzPxT21JMWi1uR5Ls1WsWJ0TCWlb6+Yij7UJQVeo6UeCQaGN4pEnLE7llofvaZ4jb6YaDUjnBjZpZQnAUwSXBaDum4c0km6NLz0JxXuUB8F+x4Lx8qNclpAgDYmUCcnGU2OD8mI37AcNV1Kkfs51RzV+cS1Tp/5BZZY6Dti0rRXdZfwNWGT7Hx4+rkjZkzDLG+66fOMP26WWlJbFu3soD1AXZ7ApwlZcQGPn1kWfWohyFrvTQTXy7Y/ps5ZZy3jjLEbCCTWmgn9rMNTadC0Oo8hzchcxZhKV8j+p6VTLDdjqgGsQg2R6JhDB1nZQlsr2XeHvI8ztTcUtZxxy6KaXq+At9a6Q6n0e1ESBujv7mJp/aULzrzeIFU7Zz6p9bAet/plRtJaDJ3hTUNOrh7XRSXf0W70LKzSlKtoxjLSwG64fhBTaSy+JzgGgCDL7LqJA4z/qgW+0Tv+VEzJxt5DBafUuC79v3snq7GlwFf+JEdkT7M4B/3vn/gKYVizgT0riEx5eYXBfgcOGvqW2IZ/AiU1klNrn3KtEk7eGFyLvrQ+46kE2huPpsdH14YvskUJxvLiollP2UNYfjhl7jTSEQ++PIEJA6eCcacYX/XhTwOz9Q2yCzYb3kkxVTZO7MqTMz39FDyb5YJwvyV1N7mL/NBCHu1taAJfJYySpBGfdL0JnbHLhi+eSGiEntsx1E2Gp/b6BOqMfzp7AOCoIcoYtOT8R9AyFyZdtKX81MaBjR5Q2awZ31EXfO2aHSo9w0CK+ZTYuhLi2+yTcZ1HXor9FgiR1jkJyx2qKBeHLiL47pg1SWh9cJgZnHniB4b0qcCFud4jloilnvtznSI585IW8veW6BHf+xTIc+ZsHPXWSwHQ/fNdsSwEPac8SiuGD3Ns3MhWVb+OSQLI8zdKK2LuqZUWLrRVXkoAuqdtTxE0E1Hp+o2qu3aR05dYFNOpvOxN+Em1/AoRpqGElD9proK1tbnt+o6b0s/DHDn0eLNY9NIrQS7Jx2HgnCm7d58cNm9LtGRkERqa3seGPtsIpGll0zLVWYnI/kcPyenjl491UVqYexX/DW46lyOALeWi1LQwEDFYoAcOeJkwoc3nCfeITqw3gZ0d6dCyWf6V93W+K4kYB/gcIQRYE6k8DMa6SJN2nqwkAHCEbibnvF+60Pp+zn5wiHy2DSpJhQIXmxMUGLHWqxGQgvyp6ZzxOT41nu3tFmlqEz2mldNaYEEWR586Zpp5O7cWVkXjvWD+WhyIVE5uDBd7+G4T0iRPTaG4PwZkWqcweE4WA5k7L4CDGvJqdDRiBhQNTzjix30dKCfxVS55QZxgbSiHap+OQbCbF3a2WHoJIPetcP0pMW4uxA9YgVUGsxvR6+73i8+dFDlaXa5JDE2qDMKuZu5XvZ0/mrGMSxbr/5maPfzlTBQPL7aDHdmB4ohnC1Ifa1NhtJ6iZbOtktbkXn5E2t1rwzGs9flalRMg7ApfML57ulC2rxdll2UUoIlM833PHeZno7r1MjzTcGPSi4yxioatmwIuGP1IP4Zo7ymX3MeiyHsOcCWduAiHLsbHb11V5RIGPTpwg+2TA1T5dLYYHhkzG2NJbBSXVqri5gr2LQ++B56AvyYAUIUp315aHYuuKaBAeZCWyjzz6/bo6Qo8x2tvDTacPhCVAQMfw9g0xcAZbv0fxiC8n5cJZKXTb1Efjuh6lgX3t9Req4/TGQAKubRA7FZhZr8apWnMg5vC4h0QaS/TfgazAT4BxB392wBghKuaOoNIAdw8KyzjBu1y+N8tMGeiqX6rWFrJZbxSfzjhui9v6gnpia0AuiN/qsQF5mtlL9RojhFEXxvk/lS7hq+MdSDipM0n/+SO8cKPJDKuZM9jr+HMKninrAm0t+MP+yR7JYqjePhMT7QpK+trgd6G2/Kahq/NNoBvp4j1Ph9Ij4R4ErDlvPos6iHzEQGaM3c4lRo6EEbGcU9k94jMyHbt1ndl290d5HDOusvL5ReKBefSsQoZTQHDUt+e0WVSPJk1KpDK+4RISsSYahtc6mPfo4e33SYrzjgLNm/0VdTetJ6s5x4959wsi+5SrdcRUe4w0Gt+aGBw1gOfwNh7puClhA+UzqHVWTDOU9+3/6rd2Cqkk3J9iYcbTjbymkZ1vOmCwHZ+2lZGYrAGFyZYa9nnrgz2UHY5CWhPv27tesJdjomP1T4V5adtKCczui5RCctQmP4BBM2FlwD1+UwkAAi6fZhdTiujWM5sYE3dXqbbvuaJ596ptH/p9uoHLGsgP64km9IX4gpFXb/5LZFqWSxROxJpjTu5AGLF/Jot46IUR/9zRrxv7dLT4GFQBir41J+5Otj44niOvMB08v/enq3l7RDKB3+By8DzGtr90Mf0rcTKOCw4E5dv79hTB4GhffviHDz2YDjYcESR29hv+UIiKVxYFNmgLmUuGodH11UJS8Sz6+y7h8marW/GYp89Fi+M4oxz1zaMXBkg/EgPSw7usNfQwSoRTUliP8Wj2IOP2QrKvKAMEriqOXFCYG/Djx6DKA1UhS4pvEY4HGLZ/yqQSKmpkEjSZQCwEkRQf0o6addPjEmo7U9/ckiZMTKxnJVcOuZBARga6knH9k2u9GTVi7v8Zso7dVO0CjRMBJqYWkiym5guEd+rtANcsE+QpWwc+H5pv3qTJNd1xEiOk3acCP0fkY6iwFB//mWZWlhFmD2qYqVSD97PKnPUTT10NcqfDSKzbpb13Fu0rB4+hSdFPmrhhMtDO9TueVykHdRgjL9isxrqpCZCUgIyp/Rb+2E2egxAaZ6DN7c0V7u29onJkVaVKGTSZIO6doQMVU4fQS3P7OE5AKqYb1VI1n5Sp7yMj2BTALqy/m+rBjqbHmr0nqGeoBW2NfhFwUgFFjEQcjcWs8Cf+EX+CAMKR1V+Xt8p6NMnsBQqzgWdbHhKk1voz9Aa8KVYIianP/Qm2R8tUHwVHC0sgQVDjwcFMZvybU/O7DhKNnK8AnkgLsaY8oN2Yjm/PGdyPthUrn7itIGOpnriObIA4eZrbOQCdfdoxxcvt2BZKsGhA0cD1YUO/e0r6vpce1zvA/3B8M7xxeuGo1wy1f/3mY3deATgyJQLZbYPRqwSPl1fLUWRfXHh3EH0jWp9EtVDQ1wqA/3+hd0l74iO7RXEsVq927e3UDyb3JdeyONVeTJik/rBoreUvcx6I4E2vFGMiBk0f5X1AKcqjN0OjzUn9caR655hc5l0lnK8MswrXUBZp6gxYBNvZl+otTSKoYT+HHJOl9+QoPFTA84pNX5at0Wrje0hLn0I4eR2sN2Qk+phiEntdUz9hxZDFLxqHTx3s4A1GBnlVzHl602BOS4WwOoysaXy0k1byzu2kkgBMAWGhya2yp9e+nmSM6bBW1DwKW/03CbT3qCXbqvG0st7w8AcBPS9uaA2u4c84A1JRmHxEUVhMhL6N8G3cd3j8mX8e9fiP3CkNX4mkylUoEgF9cRy15Iqh5Wj6GBQJodaw/3OIk+InbkmI0KWEk+mY3fomNpfjVKWbUXMJuyP3QLv57XpTm3hCxKsKRIWdXMAfGv5nJcFzlcsEtpUQivshbEP52WGcqeKmagVfJm1L7FVaSfr2m/Jopb2MquSRy3BuKySwqC2msKNAACx+NGJT0Su5QDxpDnFEuuKfuBXw5wRHxusu0s4Dw8U05AhOvdXW7h0moerF0w/7yD/3UpBkC8kf6NUE7qrrH8SGcKqWf2aqtrsBcWRzXLiZkSCG2ae13HJg0MzQMdG2am8L6jwTJ/BTdwCIrntNHyskVnDJGWFccqWbhE7BPhcmBBGyTgSrvZfsXLTNuNk+5ehmlt3XrIUCkXklmzVRDjVT3Slj2lfzQptZU/MdUNbHk4cvkb0cs81RqESw2DQLsdToEj+0tOvGfdsR4rDEqWQsQJqmJmnYYfKdxE4I79QlQ/moigHCddEi1IEcot2HMf2vJ6geLzvyZLcOX5X51FZi9gBdBfr5LvPze1vNSEZfiee06/LsR7FRRmUZUMqr964QxxAsWBAJzyJMoO2MzYoKbq4/mqFwzRhe95o/QkpTuh9p0BJVIKlgoR3f3AuZX2E70V4vWLsKQLGcUVNZd5XTCkJOz8oTO+bQezY57ckJ4tzMllt+p160P/wQ4tYzvEd48SexkntlT5/o8QGA5r4kGlTXAR8ywFT5LpkAi1+JIg+MQBu/Q55Ul0UeUC90glIzxucRd2bbNHXHMcmRvTdI3WZtjEdm+cjSDTgYReIQSv+AB7aezt1yLBhCZphO3lVaB/rnPpKlfMkHU2yrBzTgymRWLfOB7KcdGAlfLgvXLmpcf1KxT2jK+At1tm517usK7csQ6sZxJZ4GOIn6hPwFlBzv0lY8gqmi/76EUu53zv9vCjr0ISrWJJMn/0kP8nZiOG7McMrd94DWCGWyJjcqFF5mbBsGloQKyR3wwtbZruziyMB1iMkK6iFVoWAogdz2rJ3LthhpiFMtUykaoTHm38UGcIwA/I7J+Zjr/D6sI5biufMnHejyPaxNo7+9vrN0e0HvbKI7JyjffDz4p3PXucaNtxBsUdjztl0C6dCT9twKbFVSlFJHxqkHDs518qCI99jvroxN+MaBKT7UjFKtjEGmN5HdbUSOR9qDqSMB+dtbJYYQObwV4p/Jrbu9KMXVR+q/2Yc9IyPhHjhD7x8hwOc+TjLzZzVPGKAqpW4ePAc0MbEI/8FvlwqJeUhU14K2SVrdAX7wkJ67DvJkY9/rIBjPSA24TugAJhrWAkvlKUqf1k7hAKgVKOg25uzuWBUzPgox98kHWIPN1jU3CkSuMiy8GKRpuvj8JSyr3+CCXO6GrEu/Nniqc7vMYmxRnNzxByUGTnhu9aYV5yI1KbSkTPq45Ot8talWf2aT/t2vlLjGU6XwlxgNjrotG0prQCkb527kSUBecuMrmdCnMyb+ryIEIg9J98ghA7QQr2cPzO46gEmfeM8jymmyVMKJUvzUEyWoivK+zBrzId3iHofpEqmV1sspx6IOrCLYNU4fiPgACENBhln9DRUYcXv/PFELpj6l0DTbY0yJ4YnZT49TwgmPMmg4sxfkxOZBMecg6XC/MZcW6cU9dHzGa6SCajxlIprgkzWMzkcGCFnyzKsKiAto+vv7oTU75C7H6xQCNAnkkvPVhUDrV20oeC/AWxmx0SUHVzB8rLxrCO+aiJ6dQ0H7LRicxrL2CyqS8hY3+YiezdtSvGoMOtvCFToQkC/BKBH0jLKKzb/RUOiqW4IJklMP8ogQleZy8AGrlzwdsOUXGSoDI6AoShPVMiUcM7hiCsasU2n5fDmitMRdnc+gcFQjMDgvBEHg4nXO6iuAPle9vPIGcw9q1InYZ4DGnw0Y8EqLwELitNS4sMYKjr2y5ZN4Nx24ADxAw11jn018J6Mor/aoC76qAh5eChVIAbEbULhcwZCw6oZ73pKiRpUMzdWca8FaigqI5KFtp4rUDghaTSoLDydHP8cA4XiQbsTvrIxfVvEFAUhHx/98zcdv6M8cKT1CjECh6PekAitfdg3kAara7wxsvK5az7Ta860SSycGfKwv52/ixWEZCKjbpKECt9d/amTUOBSeACISoPS/KbSGVF3dQlVg9ZM1gVCEUojMvm8Ubnwa2wucAtugFuljV5ZIA/hzocpjzprWnY+MRX0AByYc+V0gkzcDuyw2dpqjLh3ggQi0PS3M6m9G6vfUQxN4pNBSvXv37hy2U2p0xbniEXMgqfUvqYEOW4VHSioO2naTnDXOBA75e0pXF8n8mLWzHlqOzvkE4Kw80fWHJ/+DtUY0M7J9Gjf3fDA2yfGZBmL2G7+TvBT46zujumhCbSxmUD2xLbJaYDGK5ItEPaZJWYp0d6r73Rih+L57CMMWXcCSQHUf9IMVYagqQL/Dh5zXfv41N3tZ7SixEvCvAUQlp4QOh5G/FtPMzpACzecdDTgxJz9W6JfATa/N8iKGRJAcNXLBpubeVdxqpGRoJuWxFs0eF6e1aW0oXpIuXRcmSn7XKdpPwjt7jjFFSaC4Rrpsvw6khqkcUy258whhlIatmPskLAXyYLgxmEWJ3zmn6FZe8DoMymHovdLGJY5tvcF9hEkheSByn8D7iaT8oa3F6Nph454yuQ2K//+YZAuuwsrIWiY1mWtTmWKU9ngbLN/g6D0HpczOxOC7hoQt1qJ6cwNEtS4rWLE+nlkpygZc9GpTqnvTbNI1g9yY1S657/kyrBR398CoEIRa5IJdr/S6iCsaGYon77ZbS6yC1/32c+OdI2eSfT4HOm3lqEELnF2wE2pxRM/r1rKHacaycEAlewUjAIcSpAiSjmmMVQ5CID2VqAu5URx2pV2O3ZQWXbRuuPFdljwcWM1HWhHEsmZMwazIpVuvwBhOgKgpoOBIMvDNf+4wa0iyT9JqSc717+GePIL+nt0iAusfbD//t/+553b+SNWEXBP6TJvEVd3JKakadBgvvBPyJqsQ3KQ4cU1RgDbxMON94umeVlDhjhviWQoLSzRoMqC4wejB3ipSrvLnNN5a8la72ANPiZtrRsTX+58CBDU4eG6J3gw11PtiHDWQ5BSRXbbbbagiOO10Auq82NH+lOzhhLQf4CoamzohkMuYaiEHCi/pysMTd9BIQJFDJ6mKPOyY8R6Fl14URyiBWiwB2wv4FdOznZGkDRaBrzQDYosu1m+r2cY1gL71yOgTgpUVB0P4o+Vrv2vDGmk9AFf22RwAHDG3tiAhy2TS7WhscoKr7svwqCd+VAYQbyRoSQK71MwxAYL6J6nwuT5+YLaJfxLXZnUs+j369wCtVeILSG4zofLGUM+a5BeYk/8GF5zh49WeueEvRiYRi48RjBA9uKS5a2x2TOgjc/BJQkj2+1FiwPqUUCajjZMhW6Zy7BChWI8gBOQjOKbtOLvh1bJ8WMxx5399IcQjnq0mCV6PRcg/i86zjPxigMkUIeIw+7Cvg5i1nF1T/bMTFAe6T2pdadXRLhrJNJjq+RtEFTZuOuL2mc9vxeyJ6AwZnTVlg6+x/RnqY2oW3KiR7DAzwfJtRnsNrV8mYIOipo9Q0vrx92QKEt62qmW3gb8P7vgx3Ly/ka6fWXjTS07VVTn750kGZ0ZvqQPTYa7srniG5e9WXTiuhdQIM4ca7CvKQUYq3TqfKPOq4436sHgdITQKz8IdZlJHoSLzcUFQ7lI+CSoIcqJdbhF8iisUVzhYXO6kprjKsJAHK/esXk5MmIE5oI7CMb1w7qs0vCTBrIwUvs1rHj7yVsY7359+CG2jcu3chmKBUpJnp/XA/cMNeVBCagWzHl/jlWmFAmxj/jwopJ3VRKKbQpYkFQh4xE0l0UC40KJHopQqfezIWy8dW/BOPUSCJUFyUMrJE/xiRF0f3p5FxyO9dObYGgtsaXLt+dhT5V7FwyD/j2jSZ7IcxUE/Tr21B6BaHy26PXUkeHLXGYLmVuUvsm3ShOvhZFSqSHn0cmj15ezb18QxDCkVS97+uJm0P9ZYn6Cb88I+R83HTxlwGq9QN+hLOZdEK7wKojC7DtdaYpGAkUtpnAQKkQ4cat9eaat8FecadYo9i4H7LFE0vUOomtBuAlIXUi1a1o57NtDL03NQYZWgMsyMJ6KUc+kWwluHtGJwP3vhVtruwDPlVXIJR4dv75MAK3WNc03r7O6eMcJKd/tfMcEG1X1IjF4/eyjm1CD0XOKIS9VEM615ACaKVcA7dEP6daH5ylGK6fy7kQ5C8T0zuwWtCbNxAVJqUY6Vy6dzvVfLg3fZ0XxSR6AxkWldiDFNO2Tpub7w0WqCMRhr14Y29vM+SkO4HJpiVc48emQRH3T88Dq3BFu7f9TMH49qxj5NxXDHfYTaKv8mo3pw1ncvgTEgsjC+Tcc1ylU9jYVYR2BegEPJHBagED4IEgWkAw/5GeHVpDzbCEM4/Eod8qddghAJo6QKMLABY83EDxg0tAYtiBJ0TwmN5S4HIqRT1B3I4tU0HpAe1Fe0HxKlB4JFaSL9wBEm6sycEeUMfPHXRP0L3fYYL8pPJ0WWkal1B9dw3Tj61vpyr/J10/RL2GjDYIettzWuAlfVTDVvxUOKZ7gJnsOTP7f7ofMIdokBpQCIEIhR+YsukZdEsIuqWSAwrhQD+3LBkFbBJDfqJVW1hlp7Tu3MV3qXI0rIo7iJVxcOThk+N0yJJlBGimdmUjU0YBjGxtjk/QmHnS8f32MhabSqeGUOcDod+LMZ2hIdLrt0gw4f6d1iynsOcJGvj+8cv+YCUe50PEAXOTy0ADZ44N2kHZz1aPPIPi5HXER6ZhHIZrWR0Z8xXIB9gqBRkLNDtX78KLbMGe6ip2V6diH3Ju/mtFp3kIdZaxCT0QXKaENAooUHIcgl92JyaxEJYaXhhrtfkzF+d6ux5imvKnMETLJuYhEyaGmr1svM0806LM+PRjLzI53KgqDjA6O7u/ue/whoH7KlYi8lEPCqFXweORgd5JvZFlpIiWBCPMfMUh7FvHiQPheniW/rUU0QuXiK3JrZbuIT7w7pentYOow9hYNP/0gf08NYW6uQipsKLBNj8Sh9BsteVGh56pEdal7YRBV8iRBXqno8aUXNth3KIykG/WxiiShXn8kLLgjV3+bDZHYkC/3ghWJpUHtz+JQ7MZSMItdLC0tNSEidYQX2phripZ2BtIz438UY0Cpa/NyG6uP0gQcNtskq9+Ht0DzZ5NpuohWoFega8+FUArP/pgvvje9dJo5kRxfTgD6wM3qmfrNy9YYx8Kll8dcEZl5g99BEfKK5QuOXsVV17I5RBm4jcGZXyOfYLgAkmQCGq6m9oC6qBnCC6rpuLq4r+oMEd8zYEvHvNJk9QbmRhaMBq0RUpBuhs2ZcHfSOcHIKGk8UgkKg8LRxwfILiMGPaRo5CUOuzODQGHvvTuZXuPg+rr25miZKDBqxLR8gtQ6luck1EytpLhHvZkEC4V5dHgXdSYgF7ReGLIPO3fjdU1xz/VQbuFhRxMg+pdM26YDZNe/cRfhJou0dba9J9mNJpbJjaq0u6gQI+Fie3psk+QTMB/asWYLUON86r/HL8mnzM297M+Yw7ZKh97zOfAxh2W2zJtAbAVmlEvbj6Ncs5laqmJsY/Qzj/dQDd5f0kwST3D8YSW/h+hFi3F3uufGtPG4ufiDDlWDHOlbtRpf5IT5rZbaAijHpGbe0G5g809LVwWv/OO/2DwM9zdASvWiC4J3S61dFFTqY9hjEwmrVci+JOfdemBI8Rb4d8nh5riM6vkyboHUH+axN+jwdUYkYdZ4QaIP/2mFcVJ6gL4NRTUH2J9oI5l5iiRDjb4mauHXpuSo8U0WYYvYWF6FVWbUTr/wsMIuXUeAzIF3Owid5UJWN/+WQNgPAryL/3ietePRFNE34Yw4imesV0x6zzgptCY+rEYGQVN8EbJ2RBLWlWqHPjb3e/wFRtSM9qVsB7WDSEC61zn1Qnt+SOUCoKdofVHrlizytaUxQ8ZbiWjqsn9RGAsDeYm32ctIeYWv2s1W4uqBBAxlQz/fED+Pv6m2Cp/YNtNDXAgUoKT3i42Q9Vz+zhNahQ/18wQNxfUb/883mzxzAvqxf0ZRJSX3IAfh4OJX76VhaBIZa8IETeTZRbOqACj3w2K+Igkle2ip1+SOIYP8SpHnrIAEPq31x5mjo00FogkhvPXbBv/Eau4uY7cTxsxSRVMnKcGLlQeVWWB62DyzWh2C7nm8OrYRwl+M7YHMQjlTobt5jMfDh2tKWQCAhEGCqdEtMbdBrRewqsbBDHnqWNtln99Z7XQfFnUXsUCgUYT6uoBoQaKoRoWvR7LIr5eZtUMT+OvxvRvoRw2nWDhr/vCeAr1LZOh0qSrtFyT7lRfaUwnGyIpgI2BLGsj9H7xvkXlx1mVzT8g9ZWHHv/qzfZeu5Ovxz83SffganCmhcYcN1jEhD4P4rTWJ94Oiw/tRq1ijBypfy8aLLl+LQt1Pq12YCxNiJ5W7PVFeiUS1PNhTyTDKfpNqElDRUd/LWyOxE9DRraj5NZ+Kf3OUkuXItvqBLZge40KFV197bvy69XfkkIepbUFEvsJTg0AqY3mRvqiWStFUusYfoGYh3q/MBhiyAInWVzxuO8HREFEIQ2PFds1TfMhXy2b5doPW+G0wRglBJ/3h+csG8EM/MkToU7DI82WKboYZFhfduVFzMFU2dvZr7Nyg2hNHMo1OpcrxG2uVkgOjNAFkOZy60bZqndTEYy/s/sQeeRLf5F+8rgL7T3diHbD24RK4PJNC1P1F5v1pX6aX0hbRFFbPMYA4wp9T5vQS+JL5Ib8itKuTkk6F8luADnF1y7qsdPDaCYrDg6uAUX7S06StU377NNBEjQmdhMokMH4gc+/frdILI+7LmomaErp7RWxn2AET+CBtxXd6HfEc9b0lzoYl7qNchkzLH2/k5Uxgb+m4oIIj2oS1+zMw7U008wN83vmVODca+F0ADGlCl0eEIqRKOc4YvRKsUdv+6HWhj6rC3j0ThOmA3z3DIQ8576BUzH9mGO/JWa5EHUdbOsfmJQj6H7WbcRnmbaDN4WpXSFYCT3sNghV2ixlzY7cqyZKNqIg6iqjHdS1I4EpauT4cn7iF3JvVKs9oXw4FoaOijc87IIkPgThyWUmzm8/KG9guazl7csxOiIQON9qDQJb4UUsZ6KY4suY8Pv4qmUoTkB5HAFxJo7SOtInKbgReXUq5b1gKXblgtDIYScgnx7IJ2PhPuoI9UuaEYuz2OvIRQYcc3K2c4icwkAUpYeNELDOuQzbRY9dSFBsKoNEfV+Gwg+tDnf7Aat4sx8hEfaY5MMseG0/QxZip7e+FQiR6dSQI6cLQINId5cnWWW2HS9VcRU0I0HbI++X+GXThXRnJFj1a+7aHkExvGClGA6A+ZBKFfA6SmQzQ7LM928FmydtOPNPPsdFUyAMgk1wTZTmeliFtfcmp3KbiakGybXQVk/MZl535w6gU2ScnummRKe7Qlcz75t+HU86322H48dVdRr93Lnc/pxM9nXAcOG/TRZOJ2i2PSttnchY0lL3fuLnMZFjQUejAxs5GSBV3qcaaTjN29Ek9Wjj7mF/RfA6ZrIEhRS3A/qhrF906nR69d1eUwyMX20oa+kmn4X1oZqc8Mtkx4tJPpdHCUpA7Sts2gsSNtLFOsYpX1TnVkArnmqlNDknyEqm89qBA3+C0L9KX/eKACuWVRrJ69UwvkutDEnthYPXD54UbIFlhz+EUJgdfFjVvsNvAFTjYADBH4J3s9kpzbn0IOAYgJIDPM/2G/ghCO8KEEHoFM5WXz5HH/J/v75gjjTayigCWJv1k/aaivcCS5tSAJ0SzpwePNtNJKku0Hopowto2RMmJn6sjZtb8otdu/sMgDraWFdDXh2ZHcf8YPQOth+SKdGvs8JmJ1YkSunnPr0BXaB9owpdCUPXmZ5Z7ysNgyRLwm+2oCO+lPMQBkmypn8WT1OA4TZBNOBSSG5XpROa9rQfaSVILKM1BNvYe2tOBllnq2cib1c99m7GEQgM+p4/GITR36YMqPTDQpTtYyODMKlDLenSoMsgQ0PgBIKkPm2F9BxWvBa9x6w8ZI2p+XyKuuJluwFYzgTcwerjSigm4ZlsQYACVy3EKRxvwksjf5YLX+tU6Duep6R7/SByUgR8xyGeTIQMBNErSzDRiN4tHG8M6FqB0DHb/cMochbRmH2l1FbS1tWRuRTZHX+htANSfGx4kace4y6x1nCDPaYtdbtyGdONQ8kGHwD3MLxocznG+4HIk5Rv8pCG3v+JsR3Kk2sjldx+7zTuzWfW0aV6lkQKY1p1Vt96n0AIGcshJ5wix4HAWVEGw9Ti403C43h3No4e7I95gOyhYWCqD0BcKLr54H9YKk0YpmHVNiWyoZdRehN4ekWikKW6rDmTI4GKoJIh2M+ZNbSHNngDgnH1rA5uQL7ASnREBLGFqphnNpF02Rcc+trB9VHpXjKilgdKXbCZopfggCdJk8JKOMwt/7rh0ZwqFNGyd5BWnvYznrM4pOOMop8AANDDUIfUs2o0uOP2g09KTIup7+JI4uLgt2nUQf0KEq21INjXdsI+/PVdiEwBzerf3r56wH9mO8O1SCffFsfY3kIPEyxMarmLntXsSkAaNshKXY8BmgUKIQ0Uzj96E2RiRA9ziynNgYw0VQfd5EUptOCkPBW5aJuidZwpp54bhXuM4MXOvQqZhOmp2PiDGFt92ihCeY0D6X6au/bL0/co/DqNvMSY55I2MmEqw11mDYK02oW5uLJP9fhCaOfgbH30nco1vwicm21cVw1DHLKI+FIHljD6DoMUIWCyHOGhoNh8AWfVd/fozYyG2vIM/WuP5Grkrnqqy9m1mcj1QxipzyhL5LRBeiODaRicTJ8C2dDeA+kNm1l0sSGary0BN8J84Czb1ELiQEhqlFm/MenOcx0X3qnlbNj6Fy7LXoYWt9bAv86eP5byfrheY8Z0h3eSteOpDcVVZa2tfUkjhHzvVShEFLd0D+wB9BYN1BwgCbwI8QYW8N2FCYiMbYp9krCDg3MwEUKq/QA5mN6/JO51dP26RcLMkG3R678DZtvGHRKFXmkEgE0AU14yhXY6n9mThdOhlAZ0mvNfi7uT+LjC1ObMpf3nhdrFxTDmpq1iFsdpDsTGUURKKJ/m7Qkl5potLJEljv/l16CDi0siXWvaVRzzEPAnqKzuQkefmtDDWFZQHwxvSSORlVX/bkq/PNGN7DfKyHPagVO95QTZA1d4skpcG7RKosH6iZZUDylp1waQdoMO6cJoWNNMpjX2CpPe2GYind6KRe2YhxrSLjOULYm9pmlI4CHdE1oBYsOERLrjCEUTLytPEk2yh/F+ta4GoZYCGMaYTXjCC3Bg1C0VPg4p07VO1ZQ2c00rem2u3wSMdYRJnrsaGFeXnk4AxnGNU67r2h8Fa6b4xdQgY+QL6BANMZviWs1per+rI89fjwWsokrP/nlOjSScBTOW4HCQCwlamFkmW/sZ6vXaD8pcn0OyZgAPNoSWvbNO9G9+TiAp697zZGS+zgE4GvkduSeZwudBtGfXJxFgppo6cZqCwA5NnrKHHFV6x/C2J9+i0pN2/tA33FGSljq15N52EbzcVgRynpKyIuH0BCYNgg1JkloEolP3+97zB2NQxFV+CO+jQZoEA+vz91eFnQBGf6W3lok+FI+AVfxu03wRg7P+DerdCYbVdZEavtqzZWF4vdl5gS7TeXI60mJgA07taoGmndTr/+kN4+ro0Rvg5FvBUdTlR2B8a9LTDheqyN0b3P9e2ek3QdbwIcBYAUVapD5FUqfb/bK27YQ4r5B4jvYhwmZQAqZJrM4Z75OlxDBt7kpTDLpULU0BuxtBU4XQ8akxy8+shimDojjC3GmQ3yc4sT5DAgR7NNSt7FB/bS6G8IvFaKmztkJgdyYkvTUlWeNscbAxnQkaMskEky/JvMkDX+yFIxKfzQJ5ofUIADebMb3pIYgVomjn+jYA9GDQvs0ycrMP68NsTi0QnMI/K5PXh1OknJZRYk731yHstA1ZOb3Sck952Y7kQZijqON4c0WNCFWy9V7vCIsBl2itC8+j3TUvm5k1OmNBLBeWy5Ye2RLaOGwABEDg+Nfj4YF+wjDlpby86bugfKdmKMD4wyAYBlS0jFB3i99UrJXNbdoEMVa5njONdfcNn/+hXbSZxu9wH7L9iIF57qHcQnChJkenDoYQRhXNsEJy54kufkZcyMV+zq8/prfhN9nTYIwYuR9GMOdJjMhK8BE8euc8EcZVlogElXzDfS2DYoS5J2DfH9+JkaG2zrMMg2bXvilZVbcM3nhn6/lFuReC+4vylEn8i5C/4/XfeCpxcGYjyCqvmyNwvrjvygRWej0qYTQOWeq+T9p5jLRtHXjEpA0mFz/kr9o3EM/B00ewEjtm8OnbKWPykX8wzUigRab8cGAs3uTSuhWUzE7a1h4NKWVPzQEn+QDLERJjEKCR2vxlCKWdkxKRkzjmj3JIz9VQuxSjZvHXQg+ISTI2qU+N/jKX1t2oClDzN4X8oEZ4y2Jw+zsmCWnVof+pV97Oy8pl5HGTSADg5CJPn5Zz1Gzs2yp7nXy8tWf5McInffxOQXZvTf7UxEFYlx+aRVtL7uJDf5Zp94NAWKoIwUcn8X/nraYBLXlP0tdRjaPv42ECROEqhfPf/7Z1IqIAyahXx6HrHVFLksxaH39+k+C3CIvHe57DQB8oiRGhUnd8r9I6k+1HvFN/cmTMBFGQ+BBIB/ekez9MJLsvpKofrIajgiX7tIt9YLEIm1ypU0bBJx+X2X+TqkszNX35omapmrXYlc2voneDxtNuURQU6azczzsVTSI6HMdaZeXlRofATtRUac54p/CWvdNHKS8np98F2cCaVsPWen+ymBJa3HziQ7E6RNa6JYCzmTWwNk2qgmDUXj1XzzMCVgwxPcWmPrS4dB7PmlT97eSmIfoUNeRAXPzr8MGaDB4+VNnRor+qOBg58baigN6hQPU0T9wp+a1PNi0VuK3oqEkaWTFOPlVIv4xfuIiMxMByiin+mZ7Ip506zKeXvmSV4St6wh9vwEl+RacHm14NG28JopW7QD7dmTUHb9h76pnykFglgifpHEZ4ppHNW1gdYQBEPTKvmyQPSYV+X8zFwbdgfZKBvhFOnADy7VJz7D8WqQPkIK2CT7uzJDGYpUBX+boyXW0odMuGYclQGr2thkcGWLZSVT8g8jwInMUP1NsYRdwyboWNnan5zE8fKHS6ZjZxzLzkqA2JxHZQUAVIa2Wm8Sa+QXBKmfXhq3nAq9/a+w3riR3HMtsc4tEe0TK7XwsUOuvSbC06+7j9RxH6+isC9L+ItopixyKm24bo3N9vtjeVS81cM+UCrO+xPoE7EwpL1QxsITdi+liSSCvC2IZoQu/8hSUqFis1V/G7A4mbuvtc42GR4zApF4adXNQxOW5vtsLwzLLVJNp/xYSazPpc44tvrfuEI4rEXmsHSUKmkZ8cBtr9mxAkSM+U+2YNs8eYeXU+9jE4c4lPAN4QEkMNlY7VmVNmj6axyjvRbAbFMU2yAq9+jfyYQbAlskvzaR84j7BiKWpfA/sNf4D3cMLsVUx8CR4b1LOeAxfceZTQ9xGoOlEhZVnsCdqEfzj8ToeYX36zacI+1nom1RbEoG9vJWOaM5Gijqp4pgKhVSXrrDRdUjxV46RkwSByMC3Y+kfX1sLGAn7pY1DrLQ5iq76JwDU2Jud8qxmJu3r8feMHDo+wWXcRJVjS8Y4p9jJNq2kvLkn1SoyS2ms4cxGIcccsjV8NcSQQxRXIprcQi52rTgmt0zWs2mNm6i/4DENLHopGjixT9jAMyLFHxHcicfFrioSNb2HZzYwFOglNdVXIXjopNrWXPMjiOML+AZAkWqD2q8Rn1GFFMdPMoVMlxUeV1j6WGWd7/PC6JcpC+653GEfQNXFs7kzN+5lQ3DSJrjro+U4k9Hcd0STkXtuR9O3Q0RAokag9Y1r41JpR7vP/4qxA4M/FHe+d4aNhTkzyPzeMZb7QgBN2AwalJUDx8MS4PgQ0LK/rjVpuniR9jcL/zJNAl5BD9ML262mkf0z+57ixEpLoy78yRgKLP9xb5cS9YQ94iuQRijeheb88cQ/9UbdOio8hY2m2Mfhs3FJRZuWzDL9PxKOi+a6z9njD3ZqQ5pjbRRHwzpTwjMWb3CvBqKJ6lc1fKkA277Qab8TeDHcqZnxTCtzMtVA+PO8MDXpMJ/NkmplREvkDwO+ChTPoycFl8uPhxRT+1LgVSXXyeMhvYXIXhoSBSy313GhpZg6/Udigsq6Wg9GiUOb48z75x3CzziVk5fFmwJQLxDGGb+TGqFEnb7BL8AgfpPBXbdW64duLPP2JghLevcA0g3ywBPENeJ4WHCduBRhTlXVUJa/PW7TORsRQtZpiN5BDykasGfY66a9/B40w0fAI85ZEqfsbsXATzIZdKPdYKhYjat8fLCYRDAecEvFtCCyiXN4yjyb/g7D4KsEU7QbhAuBsYQkdXGyVwYtD/hhcLd6+Y9EU0icrsj0LFEsFyrfnbMPqKQMFWN/VHc9N2oR++rAxFMpckEkWa6D0f4JtaUpvwnHw/DjPbdWZwBO72E0vfZ5hDgOulmAX7vqpfHPGDJENPwVtBQH7M8LrLp+Xiiva9bgztVDNoTLIbTKXHwptb4ZbgDt8ExDgEqDQpGhLSuPZSrRTXsREGNrTpDOifeSsg9MzK/K4rDNl4clzkoQJb6Dd5/vgLA5XMzpcAl+4VwWrbY8lBL4FxdheSdlwHi00/52QeeDmZVaUm+T1PAwqUwrK++G94+PxF429RpTv9W90290aRZRWlp/O9EfmZuJd3a+p44C9mcGxQijj16rzWGbsY0rVycUDtFe21vsgSQ2AHS3ND6odJzYPKRrz8AeZ8Qnf75pg+MFgp76qV7pKURDtCuJfvuTGrojxFV5AVPC4JxspUsSTio5z07cSulRdFVDNClMuRI2edAeMcMIg4wRYhlrnIaq13vexIch0X+DyJa8Ek9iNBGMVuoIGiBDbRdeVBQGloLVzwEHIWe9YHP2w8QCdLw2A71fssf5p8SCLf7Hri+qLXUZ9CHLT4kXWzZF+yS5cXHhMTT6H+THBywCJvyJX1qqG4T4IKSeEBlCih7EoLzPg4KTMPPnudFuz0VySSGJdTpDcR0dpZX2ZWa5k0tlt/Yj6bNHrizsRvLi9O/926tnr/TcvqiQl8uXJecV0USfJ4boognHQTVqjAXjma3FKBlj9uY1z9Qgar0oSuRcgyh6Ch1LzFFu8Uk6deuRmEpKvfi0x+wQw52GprNBOrAgDZsCHYqeFuEpyGNKnjU4im2pVGYaazkpAuTIxtyYLUrFAZfStxl8FNczzFrSu8tiYPL8nvJSDaZMxd6rtmkwXhnCKi6btqTjir/EhkHbF90Vn4396rXqQl+/ElTXHgfBGzIZpSCwTlZNpTvg5Sa1lwtgwjz7u1gyFP0flOodSQRk5omDXMu8KxOx+k6lkjXvvkOhXjad0ROi6PBhrfqE6Bc+Z/cPFpE95jvaIRdoeWQLjRP7kxD+UtxtWTDsNQ6/v3mk3S2NEtuI89LHv44Ab84F+aAu7blzW7ZsDuymhj7/kXe2Hvnw3S00qPmGvJE1rm9mOZ5Hrmy5Jz8A2o0kuGombAxbpGANvwwPFDhoHcUdoKzhvj7NDMRCbAzVRrQp4x4N30MGyMBsWWwjIsJwDtS2MKjc6YJ9VAQAuFHqDf2mdUpIfEb+9+ZQN5z5zreGfXHTEWfIxuGa1txDnPOj0/8DDX6MunS82TnqZR1ME9l0oxKDEUMnkDG88+N3Z+CqTybWOPsswLMUako7SjApKFt1WcuHMwiZfksjRBpptHuaoUsn+NoXL3vJLGsEvCzFx5yvhWlBllIa/NaPDw+qFCRZqtuK5PqIZ61yUN0L6hQOpKe+auZkFQWg+haZHNdE33eE1KKJFUJ4as64DxdpU1STzndfuJZM+OgNWpr0VntDIKaU30WdrNzFyYG3W+cNPrq7Hc+tzEvPPNxd56Bfv6xOLtGmbZbF4n1PfeS74s8eryAA6ruCEY2YntVRLEc4cyBs8wH66pTjiTaFwWxdvaPyN97yS47AN+DbZukr86yHItQSQdAMJprJ4JTEtGALFGBlBpHC9jmlPRfYTe+Mx8Yx5T8WbuCjz3E4rMAp6I+7YK+cgQ37NClRROZ7SniV49dNcTtgfWb7O/+zDcNUkpG1TDD4yGSMRHYUzAT2tlOZ5/ARCeigthxIX3xhLxaujPanbk8rhu0dNEiGEw3lBXZNw1ywff1TyzJMyixCtFua3fHUgEVnJbJfKyfgahoQscUY1/K/z9ljZd+Simce9WaT+Sf1DBMPqjyuwJUn6zh8Uh5M+RGGrXQWLBDS6dJ4OYTM4B5tGnO2TDhcP9GvVQ0dKMrAzEQkvASacLwidn87SJrEp87LwQABBN0bWzYlPVxcTPtGQ2tZK5+pOSIEqmQNP+zgpB94eoGEW+J7m44dmIkDYv4xAZt45LJcvnjT7cvEkxpKfhCMr5OBDFbT0e/N1Ve3X2kn+4A/O9vfC3/6HghAb+fzTcbwUavbBryjyz4aNd5SATFRtIrDdhWL8rtG7o9gTtzQhdXtuV2t0fyLJzphzBvhjrU+1d9XuFMOgsMUdQp9JciRYWL/7lkxgCU9w4UNXYdsh3PLd9UkDoIquL49ncWpvM9zb3ddmTQUS9qau/o2wASLMQqmq+rHJxtR6Q7zRv7kSdyOSKwa5UIlTurlOrgj9nzZg1LG9CWceV8rf46vh+fceDfiNSyqYRb4+sCsYVTLyYN9d/zXmdGMPHzIHZWPlhYEqrWH2jefEFrZv7DFh8ZnSoQzzrthyFFdM3H4DPZIgaiZIfSIzU449+irYSecvnvTdJ9AnDXQhztvLJHUvdGGdjsah3Ok9RsnSSsOK3KxR27hEOEST82ntG3KcBkMuPVxq6vVCkbd68CBa72e8grozUbKI+vENqawg+89xjVGULbkThvN1DcHFj5ys1LLfgtYNIkw7DhJUDkLsC0UvT4AFlqokqX/5BC5I6/xRLBBtk+pRQHhvljICDnMmINvqjjivjCoCh8lI/TLbV2WHqcgF5xM9KrvqVnPqMiiChnjxjfV8Yao53SKRqgUz/22xDabyKlhW8Y3OhP3E/EQYQ8znUM5/VENNBR8SpZzmO7htQOGc6A1tVS2DaqY1Qrk1TP7f+AB9SqKwuMHA4PmzQETB40UFgzII7h2kyVZk56W/T/jbVqLGMzkXpyyHuNY2aBMMj+QeA0fhzHxABDdlhIroA6K4evsgYI582WkKinsbOe86pajeiV46OC2ko15bbzcHw1lnevk+EmR8G+VUGSLNV9uyBdSY2Q8zdEX/6Ab/4EVjQ98JzR2ZEfDvVFl0YkS/Aia1Fq1QW9XelB2FLxG9vgV0l/sVAQBupgqj+w3UDsvwXn1vHUN7pq/3PLNnp8Z5P6rEsyEt6FE5MV886mOuL3TkYiaZT/RbCGwkadAjf/R+/0wf41+rvsiiBFwik+VnT12xZlt8FPdj4xR002STBciph0JrqhW7/Ft9LI7ysFv8fupsvMckHgyL3GuktJwCaoWKlLwlJDkDTNcbGlxYwZdKYvHcLb/xxRLOUGmowbAsxrpAFDxXh5Y5w4BwkuKPBzsbfe3872h3b4HZ35hoPtqA5vgrTehD6ChAIDhEcVRdE4Bxoxbdmn8cfDSkl+M1f9yt8mASVEg0ipGkeL/AC/Oe+iBCZhdWLDha7b+8zMt7RwEdbgn5y+vqftsVHGs6atShNxd+EeOM6A0y6pQXUP7XrbkH/xb0NsQIBqCgznFamwf7xvTbN6SpyVSDjgi2wLtDTWZI3TajIjGXXWMeRDJKW+A0Qqh8NuRqqm7XgzqHoAzuTXgzv409n1C1QnQyMl/djxOzN+tdHLniDPsmfW5LxEdL3WyNMGGJtLsSbYjNGQJhMp2NEuSSTeVdvQvYz14lwUVg68pslyqq1esg49hFkF3ZQJUAqwecdBNqEkZTFdapOgYqVG6jIP2bUS3w2sUtFFht2B1ZwLFKewWJspt8GsgssCZOT2rsNA4FHLVl/qYK94POIRhm+ngjRHn9mi7y2uOhHn3PWlpAUqu4pn2mZHyBQPsqGwhal+H3ksHtJ0K9EojjY5vTysTYkfXn8amGVRCS5P/7kT4xIE/ASD72xCz2FhlRjOqPJGB7Nmckw9gPbHi3N+sLXyHSVM7v+RYOgcRZFOWjja+aEwY9Fx2/SgINyzf8/OrdPZf82hW15wkg9qf8Mn+GTOv7kre3iCRHQrOV9gLCZUu2NWEPDqcC8yBgBAujtbS4WngpsmFX6GurdqiijkCjSN3JLLHi8WECfO3BN46afHfXgkvosr1CMCGB5Z2cY2oZBP9GNCvXdZ79pX7r+kq9/tSNfmDfnRGbEaT/aw/u4rkN6y3mystq/JrGL9cOgKwQ9frQYMFAoqkgZkoO1+BmbbiMFpKHE6AV5layIbpKPse6AfKXf+Xq5QVx1FyVox2LfeAwMhiKllI1Qhg+8H74WJRvu+ssciyuozuxr7DLBwi6JLo5j8iDexgqHVZnt50H+Wur58mU2xYYwgzQLcgY5W1hlNRoKec8PAyP5mI4fAu2f0f0Aj0183imxBLBMHpCfdFa2Pmub9hPo5pd+23HAWxnch4gE/AkKj4kWlVI2Iued0+qT+BhQ1V+Q9g5u1kwh4zZe0XqsaGjgYkqvjTVsLCys/h1ZcMReMUu1oJdjS86oNkfZhhf5RHBXoqZnynK50P80w8sE67s8Tqiewr1IF0GHE8fuUqbr6U8+vRsG392YHBrmUi1GKiVHyS47K0+y2Cukjh38CFGJspYHhQWbxjiTQTNZEEbw0+Dm70WgnnNHny+Yj2UGM5vpG207VSxYGD6VerDqq6QY8WMysRRgFpyWz50pUtu3pxswruTwkySMviij6c2zSbjwFIL/LUk5RoUPPouQ5Os4IO9WTf8VSJLr0Q0rgInn1N1FQPBBkG2VTMZUdnEv5yZcq6M/Fw8OigUuG8LRcOJbNGJwNbXrnqQfsiEUPAhEfqIdmff+yChOptUz1ORuskJkJQOFCO/gMcivwgmMbwDWIdr7zmk3RJFiWqaQ1t4hrYOxfj1HfrUqJlZnOHQQF4YHXIQdCvjqVR9pHXbtuGRH04Oeo5iozvAU6pFNRpJkrCdxuHaATcnEZlZ9gY9MLMqsA2N8sIix8NXvNdxH4tAFjCJK1mdfusNNsCr7KBhLUKXs1b3L5ezYcrqZtEpGCnYT5s19zZtYfSogUTQ40Zf49ZoC4WC49u7p+lPXYn5vL3gnJDf2bp5rULbU78NzWnNk5s5Dgc9pan4MafZRi8SVfUFjakrfwAYIdFZRhcNlQvSA4WOOSKfDxkH7ycrlRk02j4j2rFzSGb0B1A67QHt7PIUQfuqNLKwHAaJeeGssMKbOqvBz73aDPm6B7xynlAldzhh8rcq5ubGyxR5fjcjAp8EW7/c4gpkc0wVo8VrayhpwvKWJu6zVd4j2AH7ITdct5ki4khYt97IjrwxyDJt0DRRCxTLnq/ml3wh7xYJqLMFESldeutDqC7l9jyuS/QG3DeHmK0JT4dhnT9AzkzA01tuhY8XNBKBXPAjGFRJE3GIxSbnOhxywzAYk0QuJwbPqcnIROursq+pGc3nrl808DcLcbmcAA8M2RQOkKt3PftXZalHPd5JSm9U/uB292U4H+T/XVhCVL9391sZtEzWYsMgg5o+qbhVb9w158OFEk+XHv7OSZm/op2EV51+u1/YmdwAonSyNN3GADlkjzIJxMqtC9Yvw3n+n8sOamlD7ZDFLF/tuWMcyWNwUJj0KkKE+elGMKZvdg1o95R6+MMWxftYs3/H4rpDwDnJ5gdaftIWikC85mgaH5ab7XPXRmw73FyMOx+XEivr8mzgy/J1aVkNyB4VhYaODSjwc6BIdbtMIqTDCsiEWi0S6qHgwYDuK0/WimLQ7NcYVMWnwQVDNHlBbM1Uj3TQoPqOh/e2JtB27ue1apzdMoRNSXzvgFOYT0wX4X4g0oAIuSR7PZwOtl4lmJYhf100vHap0/CjpFDfADCB3P4OasN05Bz6KsuH76X4qao35B2Co44rrOAxKF20iMDLludVAKwgH/n8fV71iyzhU0jY7zz8S9+xMxX8NqDeZtZE3DWv4Tj6us0Ed3mez18JWTIGbfdYvAuUD4TZiaFUifVI+tVn+dI4izAU3uhP1xgGIK6E79GS/p4zNGnRJgfU30+Kt9y+n+qAZYU17Jt1ni251iGnZn3PEejKEomdNknW0v+joMjR65cgK1Q/sv4cWQTOkdDBerT6slVn75VOit3vI+lThr7JMTQ5qXh0t1i2NRXll1RdtFv9m8fiSbBHqKetMy9o2k5zuGrjNZNrlxtbwGoDIyW0vY3U/gQ4kQM+Q+b4E1DIyRTB6Az9wuj9Udg9jnzHDLCby3UbOF0yJsRtMWVIq+3XusKt4LQ5RuGx/TzYPQvlE8JPYwqNgFlXkiKeEQgDsRzrtf5+vEPgaSYiZmPYNMRfnyzUYXMOiZJMRjggwvljeSXAvlxF0kRdvRpzjNVh9Wn/LwuCM+0XkzsfFhGNhbP7m/L/CsH6SAz61g6/KXp1trXpZkoaOZc1u5jKA+nNaS+CFXWQEtrcdKOtTqNWlDti8Ik49uvOQeZgj5xWO+LPNM/PD/i3WThZFJB27FwAEK7rNJv16okULiPFdDEtb+1q0AdT4L5I+aH0JBL2mMjIZdCjp17LVFcjm3eMDrlUSfpQh3HGGsbAo/HpvDgURjoKpuVv+n7n2A8ZrdWy7GUVqTsS2xWuDs1u36EeILcBekouOdTh/XvcxUzoPEw/L3wcgcGTBsTOIFSvAOBi8cPRvYH9PknGk/FXYUZiKeKarv02EAvMdWsbVubKDSgw9kU5InOopeYY0Z1l3BLncR2L2Wmlv9cXGw5aY9sweWiyldcdtNi8ji4YetlKWSZ22oyQMbrIgqGZWxoe+o7HhelgHYTdr2QzSwSlttsc44P2CCUdEhVR2YfdSwomZfXwfoLyzq/1w3GwFwLp8m+2W0b1jPf15tLJly39thNEjOzbCDkRZWVy9Nnk5RNq7Zb1moHP92mIanPj8xG+8ey3Q2TSZA+zHrVgmU74bOsk6aIHYO0iazbpP3LZX7lLTMYgMNu6rRxrhuJXQxOMpKJTmap3t0LL6+3oN8K6JN+sa8JqHo9BAa5aPxi1il5h0tZE+dPNCsFwF6h/7qpuVHyiMSxFuJBz0OkUYLITIBpkisCCV1ybocBfSAlxFw2vauuw/eBfQsUWwRoYrMjl5oiM5V82KB8ErscXZgIYYd39YwgthKu6XoFfkNtvWuc/MxPLmN+Pg+tfiBp2ZRUMbzPsQjFS9DkbMKcKqCkbJGQCuO+1zlBP519Y1x5ZGIDyLaiyh/EhnTnLmeV5JFDXsgWbILFe2v/SZ/++Gd6a+lIHgko3v/0odf7aQzymnVjE40JY/WGoqdieHcuGrqwxCftIsuIU+2KRCyLY3hNA4FKzL7PcwvjIvJZ+6mP9BkvjXG/1a9sMjUUIDwn1p30K6w78DJA/VwfAZv2Gu84OVCLP0zkc0EMF9qw4Jrxum1OMrUqpueSvG9BgKAkusOim2QnXiYVv//VZ0sQqcQW6ktcz1K+sm79P4zsZQ2J1krVZB7AktuJn/xn9s5h3zRMgMdQDLuR1lwoNuqQ4DjdIkBZMtrvvrCl/6fYf7lgRgywAA1EkIvpJFv/ixhbsKrmQ4L/tlraG39e3E6EyENeTMFqqecuQx1CG29MV4gkfYsmKyTc8Zh3OanY4Tc8NNVFwfxbY4PM4r17RKnJKe8AVpgS2Hv3npuBPBKSkgbxreR5mxc0fWDyhlzZtLDbLWfXBWHzx0ZN9fUouFoNn07Kp8FEKG1OXEWWhTF+zsDqn8hmaqEipjxkjq3i8UarUtYlzEk6crlSiZKKTVd49NRb0O6rC//9jXthY5m3y81eMWjKkK2H/vUwWTmnqXC+oEbIK/td2jJFCxcsHiydZwZpOLb7j626bW/IsOSVehHalc64xCjCK2+WFM+ovTuKpu4esnqeu31gOJ0iet6Q0JoC4KauNrnSbQu/T1ytOiorzKpjozunWNdhiinQWy9AHGcL/9cbbgRU/ObGjAHcx9tptm59wH4zGAOI1l4uZQWIzX1yKiLfw6rRObs4UCxKdCSIf8wnkOzlxWVXz3Py2QiqNpDxvMnaJDm2tiQM+6CW2HvUsPRlnJgmR8/NpA7BrlzWtUXnzQOdnfA6JLnNkSIKPBnjCPbYPMVFfFFO+eRDVOF8eP1sxvDAv7TT/hsUMGRswewyLA8Xdq2gS6brurZQ/X5/uRVlJDQscbnNZYH2CVseRDmV8OnomRp2LALn1V3QValeC8baMN214kLI9BSBxyhm3VkskxfSTQnCz3MV2TIFCVCuwl7BPm3P2XEl4gIONHes7NrfBMEte7/Ja3ZXG4/LcqlRnmd/2wd86KgdLVjF3KBF3XciCnxFLoli9119EeUy0SCKueEtjksGAmtQq7lgKy2EMRiexsvWgYrVqhG93IXNXfx0D8ZolEP+OeDGyuzDJiApZgxJvMkpZolWIuR5aKbMzLemnkghswQ8wFu0q7kxw6wkeHT8rkGHXE1FpRtVQPxDwW5u8YbcKuxelHaxoSve5E6yWTBHQIS6asO8ybqcVY56m0Hfzy3z367LXSGMFGs9Yu1pZH3o4Rmy4CN6oWh8Xtre2jOwbW/Y3r50yCH1ac/jq4HYEzOA/9XI8Sqzv9GKhKtT5DpJf89dTkg2DkYO++P7dV5NJQ/cmVHtUaWy9MY8XkKTiOiOrz8cTd/YE/clfWU2I0Wg5qgRoIizWLazNt09daIqGG/6U8N/JHSdQXWz6VJbdXJaueMDBHVmSwpr/JQvYgPYnuH+lmv2RCaHNb4q8Jv6makWO3NJCa5SA1bV9qMY66BcALKWOKkK1UmYYnocLiFkAP2wFpJCmdhfrnno17NI7fkLnwuNcog9GveuEmc8YBVXKfXnD8muBLbhGeiakOW10NHtIGJphHPApwWhFrriBsTejpsc7twKEaQ9D0qIt7aVWjqZFdTVXfDxqbpf92Wjl6T3wEQTUd51WpHbPsB0TkhMeOTX5mriGf5lk1x898TyVnegZPycHXrd7NK3mg+F0ft5lgLcYzhP0Ylu2snekaR5CxJYr3nEjfXuQYnmZ7+JGHVwnzLrGSmZIRcLhHPzYCWjzdlyjghjvWJFctAS8l6P2obToj2sYcVK7/RjPgOOELshB531FKVk/vhbr32OTv2Y/BXLvWl+YisSaN43kufTTYdN6HOxwad3EbdNSCRUj8CWxDIYBWSqNJQ5RQbL/La3+AwlCVoSMLf3JtioKXSCYHjHRMVrSt6ZQu6WU64lyXqOVADs8sdx/2sm5MhfPxHGktF1d4HhOSGHTg84makuqJFIpFHnR6j395JjIVcSBGbB7XBu0AUtsiTzzyaQcitWLS7mm+qUdr3KSA+XrBG28obn7U4ZHkFvJrRtTer/5gVUH+hjqwnkWmHNCERoerr0I7Xfa7qTIwf/FK/gsS4o2ckJrob3gnDxmR/y1VSQVfHJUhsrFUQdeEW3xCd0c3QlbB1cZL5gsb7jXgh31a4l6T34/hx4LbSRZPIlC2PDdHgspTlDg5eIdSuFPG1ada2vT5hMzyKuenpayUstlewVrcCtESJDEFVn/5SKR6bLhocjcz26dQnMRkLh9FrDkoMtZmPNAED4SZKXyzuE//w78LW0lYMLyj8Z4KvxMKcmZ5XU+cf1SlYUK4jbE3Z+PDQ2U8UTryEHRXfNv1ukitSr2RCBWp/wgrMoJS+2FvdJ1Eo4iv0uODLnq/oFjcwSqAbpWx1G6mBEtlMp4IMhO6sHXn2pKyiksT2xNZzVwcCEA6/uRgfD00dpD+5UEXAsr3/WGc39VQ2XdEX3PJQPv0A1kIYKos23p1ANt1m+m8hAmyo+IKWOm698ky3T9GULlnazpY2tl0QAJ+/MdguIBhCzFyDjENL36ilzrFsdPUzufypG9RegA7sfkYfH4Krwj2WniGld9p+8jRgcyldVLiZ/nkFYbhxpx0+CJkLhfFgW1lcur++TerRNBAQYC0RrKRNWlMVhJUp6vVqdhUO151IX4InXB3XZpgbXCZ8excFInXp8q+WEBrmWsVmIkJG+oHCLBrCtZWpfSEMTX5pqslpj0aAh4z8vLUYKZvUDQfEJAiyRexEHAwEpi9gHB6G9/5szzxMYsMAuvxTGfoZ7Bl6VrtHebwhJQ2HoyyYivT1zEGguSaWtZDcd/3jinikj3Ox+9j9r0aVpDj3YmNG/q+wc9fFAiGNs1JfWSC1/EUtyEWUsl6TlB9+i9D0K9rrtqHHJZkQ6fNF8foaQWqSrT9gSAwr+Q6oHSVKyYGfCnwZ0hbC8FqZ/oCQ0aCD3B5ox9/nN8G+U7yzHdJoxQlO7eVrIt4X23XOBFNYphP840uUpYCLv3prWI+wGHujAAg+CBoch7L9LVbkzZnIHYj0SavGWD1PDLch5qlHkRk4MfLpyJI9JgJYx1Sy3Mf771HKAyJ4Xo8vC7gqb3Cl8eCrcaQOdAl7/t/HDh+U0MH0vLAdiCJAlExT7poszc2lcUYro7pxgDJiT9Xg1uef8gKbuodIkaN7zLs1AK8wXs0vNO5LO/spWvhLN5TzAGNrz3SGQMIV4VBs9YyB09tLUq0bPIJtFXk0fO1g/45LUYeXsfxyNVFi81cij70+UNNc47Yc46DsCPYxn7y+fTBsYyo7WcdRlob0eZw5xncxNIumjY47RXjflYDKmNsj/6eniEiBNRvssNB1XTWZg1C5XN9WC9RKOlIGryWG/lIsZNbW4uhdJNcdEITUe1snu39VGo3urqWgaVfZ+MJcXxP5xcyQiz3QOOlcloBhotglPofFoDa+XribaVEhucRPJZf6AasjnE7InvF5C0FkKue85sHbglFkvAPt4b3UTFhBEO0+9LV7cZzrIKPMml294PuERyoOStbucqhZYTsMeEk8JWIyO9MsyHXyUsBwIZbo2/37Lpe0xAncBLMBBu0cZWrJWd/LMC7E9BBd9vS+AFBuX395mVy9ZnsFIvSh/NDRKECPwCpmAXPSzb1vsW7HUPA4R1+hbZYWQJm80Y7JE0ManxFEKkUHqM3FUqxvdSmRyOXHyHu/qQ/RIXUtcD1RLaK8Wo0Ui2MgshfMjYcLmt/VXtExkBLwpT95yrczngwJEbvgyXNdt49xuS8KJYfAML6106nBVuBudj6ub6QIz7xpnQ9GqPeLnR/ElPZ1pEdFbw/A0Y3vHeQkYJSm/eM0JrfVl0EbJ9BW25gDBlPnCuJbS1+HMFeuxqXMrPo0HChStR15l3DTbabtxp9lotSR+c+D4euhQo3wA8oLrqfvwQEM3bllJNHc2Zmofe/FoGoi3lBz3TF93BBDYMGMengSUuneDZ9bemldHKbczShg18P7h2Nl9OzN6mvET4h3wn2v3n1X24GrFbcqWJH80lFZ0xhDXMRlAqcIWGlxN+CHBqlmOduvom7w70j/zZrSTn5RiKe8Q9yxJVvwLdn3L2AO1027fPMOXlET8ZlfXh2Uhk5zyp3JjM5DicDcVFf1bs8twPFf2/qIbHUTOanFa2qUvyMKdDI7I4BY3r0Bum33g5+VuRy1Mm5CIPUbq0VAHsLrH+Exru8hNAkudu5p3aBqvEOYekrjs7M7tpRh2nn7mq+TciVwvKbK11PWCLJvovkzjAkUtZVIQU+a4++F65udDN1gzZ7a6QxLe2GGdIsHDLNLMGynhJJVv4mGv8Yf+P+fKAbg4vHsltHNSzNxnhXJno0V8ohybLHro4822OyJRVnO/0rhfOi6lTEgDXRcEhdQuQ7FvSQlaWFVFBzVQ32qqcw+CIDPgfAlzixY29d4Vj2s7lK+lM15nZ++j1W2hQo17Kk07uIbHjpZ/vzIQPAxS+rM2P+pqerDjmKqykpB/UMHSP3qq2cLFwtnpdiFyE+52byJSjzOdNQHqYkHs79msedk326ZFsCu7Jli0Te9k2CjcWtP7b/YY0cGphnnUhuTsTQJ//bP+1bTc1c6IEslqrfE/ZTb3KEHeitCXKLUJO/hm9K7EWy7DUTToGGKz+IyutiZ736zXBhf8Qkt2NkMf6eFAszDmJvYm8iVVOd8R7AAep2X7E2Lu7SRnmPPi3901NqCuQ2NCA2hZwujhrUbq/cqBCaqFXinEYdC5qem2Qm6INcanAUVaGG0hJOfvGd7vwHmWS5o/mQkFh0AKoSK6J6LavXPFTg0ESfgoDgKk6s9j4BS+J8Ujegp4X4AIZs7JrnnRdW4klQ/9F1h0EvWNkBzhEWxXC62o/rub4dD7P0n/CsU/HbATPVYhjHvYM9AWD/SpTFCbBU8iH3fBsUVVZJHqpBVULhtZ/j99U9xSf+AFqlunev0f5AsU6+zJR0rR9sCPXcWSBKr5oop4ZMzds3o7Yex4qACqy6S5vVRSSi5c7Mlw71jdkWYLG2N0Qnt0g0kUmZVQ2IGRJpxTUmPgooerwir37JnIR9ACt6PFMHgkiN/brlRZg3IXv7KAZQuVnyb+bZ3e5f1/M8xaMbukDeZudR9xOmg3CpMzcLl0Whrsszej11kA2mYWM2PYdRYJWds7LlUE6E9cZ8IvYL7d/I4O1+I26PzX+WDy0FCvmvomsUcJ9O/abNKeOnXSj0Le9zkOfK6HwCPn4oQ8LJZtHtYaSYGrHdOCa2ikKVI2VOikDlcGIjsCZCkREoREKD2E3XaoNSqN9GPD5lKyoXQIcGhL51u4WSYx0vodM38v4xNCP8z26NaqdKS6EMUl7CCwPxgjX3DIcXcX/5hpSCjgc4W0cTxe7+Yc1Kpup++cI2QEOagf0sk5rVqS3IpT4cKbqFA+rqHBWRi4061c1aTeKZAl0q3FYO0gHxA4ZqqE5tyM7/VXCix7gJUJxMrgOWFFp2dOR1XkBiRD/ey0CATBhAFrj1MUBM/PquO5LhrEB/rxj5lINaqjLFigOlyfhs8hNxWQWJ9C2G2s3xYL7oXpAG1N2eyUZZocWYTjbedrVQuUGdS3GwK9e+R95V1Gqsi1PNTFshV8ZMbwGFLU2QISarOMPN8QKQGp8S6H3qDpdzcjaURkwUeG4Q9SFULq0cPp8d930F9p2uJw6LjJVzKNSCnT9Qk1tGV5Bek8wbThL688UQNqkJJPTt4QybbHE29T/CKb8eWCWgKRxGFxaedvpqOi6suOK96r56V46qIrJ0JMKayZiWDbneluzXebquZRsDbYbkEmifB02Ws1q9RK/uVWyWx+663uMiDE+gE84YMP2aih864GudB8l5AVUUbIqBE09e1uPAVndu8fyQP0ESTj+cFx9RzhMO5jD/Vm0NLR5KKYnGMTcYreh4GDRFtzCOdjOAClbMMGbKOC17Touqo7XInIDe2G/pyWJh7eFJyAUCOsZ1HdB4/oKbuvk2PMnApUh6/CBzDb7FLvDr4YAv9LtFGjVMbBDTGL2zqKO56y/K3pWf8roVO1PSprCwrT/r/xkLvVdjROhAjd3nvA0/olpSv5cyW6dPVABdSCJp67TsOFVi1jzeUHPorYPpH7RuBnu0Ozvi0jkRf2ppsw7ZV04Q4pYCnOCV3VXw4sSRbgHV+ICSw53XUd6EUT6O3ZOUT270gtPZCjuE4HmnJ0/M7Hixy0IKmIr6DLKQI000bDk7e9M0flGf4KHm1p7ZzfNUf+xdWlRDXKEEEVMx3hZV9uS4b7yYeaGRpOMtOCnBYlIvrQqsuzGbBJxrzEaaQFwzHn7Qv0o2/L2e6rpEHSbFoV46F8JtBznliSehWCQ2l/R+fwbuypAhhaOu8nUMMUp7PghE2XLRmytm0edz85KoP9+pwEKZYoWhdjaE670KgyYipCinJLi8adTJTgzoTjcyAskdzjP974U9HzBMOXibiGURyc12lXShh42XF22rZLJO/3tbygLWH5/Pg1BgCmhyQ6zpkBxJNseKKXC8uqRR7fwXCqtVBi84kRTkuksMCSHCLpwHwx3mr9KzGRq2bTJJTb+nG686HVijTE+oEGwnqKHsWubJYsPFn/AJtYQoZJBDWkmJsehb9sUcAnKvAZA0yj0CesrtJb+2UKOWL63YQ+bVjlKnaCw9Sw1hdeNhIP1sHzsHeCuQ++0Hz3zZS4maFQdROrQ1HBrJ5ZFa0vpmYsHgWeHr4SYJmh7Pe7xit8oiFVa3vIOUyttWxVQulFV0PzuVXBVVxMzNHhTwS/OG1/dn07Ur2ZD9ZjfbnQ8BTvvIm4ZFcBy/jjoUefDbtsNKzpdYE0ff6SDa0r011RDzTXm72+nbqKkkxamQ108Qm8p+sY1jVa7i3LdLulwnE0qORninENXsdBuNTbIJQ1DwdEF5d1gno6KLl36db5+XF4Isr/mB+fegwNvsQF3iX+5pLw5FaNKW4IoQz319RpcrOPtWjtpJ6axzOjoCYjYfVtPmnQ7LRtqgd+3nXuE/ni094nwgYL8PeuR8BTFpeDOlIBlJRZo3T7tWuPX7RcDtTCoTQgmi+ynpng/LTd8PDOo2BiJZCNyH7H62cvtGM5vsFSqOrwId1Tg/Ck9VvIk75CQWW7H7vyjYHnLv6ZLBWs76MOOHLL51FxtoMsCPklUpnwX5GrofY+Nm6RntEtQY4t5rCHNPXprHJlCeV0lvezkUTh3QL2flueTjV8OdvoWvA2dgrhQHpwMdc+0DeswC4cTPV2/2Z6uXMfQxBJBLkL64ewTFtJddFXAOR1IuiV+tUGbq9FY+/R1gYIyMMf9JZ3hWeBLxFP8y5TAFzdVbMM2/Rq0Ld36iGN6AKh74VgYK/+mcKcGkiYyd3RnsDgrgiMg2UQy2LlyEhYoPCgSBiQ0PmhmQbBktTkBYbooWVYeTRQOQQVAABhrqKBqFHd8VVJgQ/Ic/u2BdROaOTgfGNtbulb2JLdLZBqkvqolqkYqZToalexYN6w7MPrgCfKDF/MwXifdDYbrc115bTqSGo+JmfwTuMh1fHZSu9L/v5j1fBtaG/Y3m2S2J4ziFBnfABhLAo3i9VI289zBh6vGTlrDtVtAbUaVzuqNNc2FUimCwnSTcO/YJa5bWzwyCa8mcUrlL3fpz5ln6s3fb1kZbvKjX/NMFjU+JW2Ct69G4yqM4MB0LXkJhJZrrTt2BNfIxzdqs7xfOtdMUd6LRvF8xm5JjwP3WWkjztdhzePTAgCV7eul89UIoteh/xWeIC1pQmSrYbc1vzQZd9tAPTFhj4YGnl0oDeDPkMUq/LUygKCu4NJ3Qu97qefFpKYHZo/s0IRjT638StY3kC9gs8x8/b5X/kKer1GkGRZ1O6PpD2ZPViAXcgeTuaf9HCyuWMRr4uccMqnN4UWVVUbHko6awTFDc9Gz9mu9xZApOsgU6f/6aPtKL1UN6SylWOsjv2NOaOsfG6cA6DqvuyNLbpxrf0anhpizgA+ggENCzcxm993M9PgkuowhDKydPGCrYFSXoAZDLoBqKdFWUWeunvPthUy5+/7xlCKz41CLGRGg6svJTmekTK+xNQGs7d7A1CvK5FcsQH5PE45dgKNmuWZMi2n4gOpJXshuDhbZR3cR2QgP/oK4k4ilSyRgMoRrCqxXMwuUJlZOVKR8Q3PE4cdL7ebARzS1BfMTM7IzFwZrZWH1bdgXWctiTUTZQvRBW7ZntP1l6pTm2sZjZUuUnAi3WtPpv4bulLR9zm6iWw3cx+1pr2McWHv+2fVH+4s2SBHArFHpq00U5BNUhpbXKxznL0KB1Z7FPRXDCIdvCdJO3TXcpVpNe/YAGFG9e0720rbTXXmdzi7vg6NLSUDvfzJaNgMGKE730KOPzSd5ZVu7OZSccB+QEqRKTnw9PRKxAteFxv/zs4ka1WTafYUcY5JJSYnLzYZrjFyBC7aAq8ejluIPQpFG5LjwDOuxfu1jnQW6zML+mDneQv+HQwtwz3hSt5DLgKdijoX4v3VOGUFWo7yx8dghXwSpT84bjXVRhmnbwc5CtLMOzh8bEkEGXqCw13mN0f1oE9Z5Nu/OMG198JGPhpjRst0Knq6GgOL3WT5aPFhWw1Je9KKw4BPZT2suRHLiotELYDG7gJHk1k4lArBNXCA+ifbZjrNtOni7hrumGvlHl9eP4xRUdbgQ8rVIfilagl/vIFYvNdwOikxdfw56ZjLbe9CN4XmUoHxTolnR6NJXQ0JJ5cMVPomEQDkGQc6CPm7SjDoyuYvu4MCWc8zhEnLqYtWCTGsN7InNx0VrR3blF+3zUScBDa+7+DUE5IiQoIM+igQbu+14IabGPm1LeWxrfsbuQhf9wu8GK9uMBRargZQplAkU7OkLRjzZ6RVjlMNey+6/LbSy2CK4KagGidKiVpONN+DkH8KEt17q5mgdCbuIBuhS0IuFbdZ0ypi32Y4YTk8ZNW01wA6SCn3luxUepfYKTXP/SMoJOOQU+oy3IovHvw2peyDR83KJiP87aW0GU8NLL7Kgdy4mJ5Fa+4Ny5yotZBOTIrPXMFO3W/Rk4Hc2ujJB94RuLvhRDNHEefKywGyy4RG6ecfivjcrCu72uDf9Q90XA7ZDtGohZct/+ZhLzytrgm3BPQjgqb63O36UDQxt1FhnWQPaXIZlmYLdRdgK0i1l+8xrNB+lrR+QMzuoatlsmoS88sEMtfGy3z1D2lJnIRVD5wgdo2Xk6SuQyyRcYFp3MCGuFDbpkUv2olyU12bHAUgiLWBxu2etNV2FJKQJyOYI/vDpquzmrG+vn2X8at+zxEMpPbnwSyX5PxBEVyR/wesU3dty/fqJjkyFJsNuI4oJinTpBAlAxnN3cORYvSDRbp9gMtoV5oVwpBsvyooUIPN//X7THDkrd5X65hwHdm2Z4dfckN0ELEFJHOEhZINJBgPm5GGvHObqEvSAeylR6YgCRyb62hNZF0udbS1wO/Fnhehe/qTcWz2kBbRp5VDWiVQrxyNLmKm1TtzlsW1ACrCxx8SS3RbhqfGZB0I0w2Vhu+lpNCdsUsQ7lgaYSbZ9DLPmftY/k617q6zIYXA7jtxEEsFL/uMHQ40+sbPhmIhFxxW+Bi6N18CxavWUp23o8LandMgKE/LeEkynTcuCjp9ed5tx1Q4t+IpE3EZu/xPMUy0Gq9SRKL1l1iK+SykMTfmpx01dnJ5cakH4TqIRNH5B2/DynP4Wh6ln/VDTVb8ZPlSvrjxTZE0oc7m3Tcqv8FuKDDuuZHtK0UnmpZz1WlIhTNAdXJB9/wyAn25NYlpCk1QUhkYhFYTOGI29Du8QWqdVp0QF0tTyR+NNCcq2eQ90zitb7/omlQ8LFsJusT0DU6ZnZaK8ns0sksBB33YKPpq1eN9eBDHdMYSpWscfv3HQnFe4KbLxADD1EbCwajhMCdV94XmPaVReWPFLohKQ2Xjoss2lpPgmwROr1DMkEi+ohC0KKJOZoATbtH3USFv8tVhFlhGAVn7r2E52Lwnxds+jJLA7ZpxOuz8gUVm/kIktRJpzKY17zv5Prt9Dwn6rEeJ500QvuNw0QGRxKH1VsOckWs38+NeLBhqzRW8h34O+CfKnyKsGbQtTBUQis1rQi1An5g2k2w29zcP8VAn5ylq9jMTExDjRKiFy9yTf67wUZJKxLdWpBh3GVgRAKs5QZVXWddFm89lmMcbkiHURfnfsmYEP6RUDCZx8vfEXu3vuE6mXBB+VHki6VOmeXphXLw1sfAiRGteWJ2u54moLvpoLCiqNvnJyPzuUHj9aXEoB8/61C/biW8MbIQdOK7dXdMpRvtx7vhGS+9xV4PO8/rQ+hxydCSzhCvN+psD/cdA6SKSFrtt1N1U/Le6ocaX9/eEv7uDlNG4TW+Z8lsNsrTF2IUYZAhKAHj792FI13sUWUoHBoA5CH+j/GwNWD5PD+P7VzMxech4He/+uU+FwzTKq8wVNYmrGs4SYOxHPjy2wdCFt8QqpebvUso1RL9IkXEGxI4OkqaKh5uikSsIr61fEPNqnW1Hib4MPhE+y634811EXPQBfxd2xA0RMlsq8+iKOiYKYv6IIqeNTLEt9Ck4TU5hBdMHFE5A0CEuZ2v4Po0I8v3yRdrMbIyGu+Ns1wt6Zl4akOr2aV30Piva0X8biF0P35S0q1DTigCX8itVjg9jaxh624kZc3K4MImezfVVTgyYoWFR4bK96ZbAxv2XYpD8ztyz7y5aVlKMHXktZ6jxUkBCBZLWcK90G90dnpSEKdLgRAqJBVrjlXOo7hanW68diAnJ8UxkKKG+H4ucRBp5z1WW8h8jRwoZsWKmc9j9JF8xfIFaLeail/HCO+Islgt59Yzo7XOdG7BjU5ld2+8hyJsAY5132jTfF4+48NUwr/fOVoHZvgVz5uQ7xJ1VrJUcS9vdktTd9j29U6WUAT3ByglGGhl5FoC/oxW/eDEnAvAE9MwSeVPNX+2oeVIL27PaaWsoAJh0RkWOQcDdIcjz3oCP6j3u1eo/PNE1+06k+oaXCLZZkFmFcEziUtCf683RdtWtAWYI7BD1lzywQmwWh4Q9HSZ0WrfWk9M7iwJ1QXLe03q+JSccK3337Nt5uXGuyF5O70qWHJfM9Qk4EpqDT3JcX5P9aEkwHbDdJQkAn64bly2lUy3v6u7iAv2aedh2HbOT90JSoTn3SkVchtMx33No4wEYRg8US686/7QVu3HMP+zUO6IK2DDWwk9nQjOSKce+RpD66PZVRXJoOfptOawlw3JZ65SbF5ZdUlwQ6vVyMmvbH9mK/Q54U7xPUf7W0WjXOIyKTUs7nbnosHgw6rWWhLEeldUjiaqit1auvuk5du/H73RvTzZIffZDGaCkfUjgFconIP95msdtUmn+T9KGFy0o4j/UVrZFAurZ+0Hcixin7Wjf1HwAAhX5J3GovlrdkJ/MKqJVKuZ5hKeNk7kA7c7/DxtdFi6djRbaBY8Tq10fHVUHcQgQxQ82je05xUWbSGGUbxuu5LQqbPvex4frxZy8SlIfncAARfTaJpAItiIK+OtLcZcxtk6iwEqdNgh/lA0IdDY26yDj8WLrPguIpGmZLbUFN30Tk8kALX9RoLUf+dLOGsInCtKrgu++p1ymu+vMHSpE6t4n4sh9eJjGQ2MQ4vvOjG9bp7NS4q5SWD72Ba4xkmilyQ36oFSDPOnUykrBU+AIyNbwQ6uuYbBgloCI86lJ+DbIV4MFpXyPq53zEnKO4XMQBlxk0jIiB+cWitRtDIgtNNyY9ZYQ2oEJGwvsZjDla/8gBezGeOIwKIGtRnbH4U3MUQQPlncpdmhHoWa3a6AcYCAMvjI+ObR3WFtTnjFuq60lehT06ssp+VKu7aQiTDo47PnBc1HP9yiUIIIYuXvU6ZvmWQmFhH/tvzutoOFUIZLb2GZk8jB516O8lEFf3NRJiFgybcx9hfKaNfD2Xo/e8512EDPs/Q1deEJd3eVAVlOS3tzloLC+ds3HavDoFnNZraaiuz0mSdY39tNID1CkzYq+EZaBbnrHF79+Erbjlg69TL8DpvsNJ89JLMyaFK4/JDZag0EygPCMJ4yADIlyFA7RPrwHeOvfHp1l4vtYkiiicaxR+riWXIFOBcV6E8n+maoxjifO6ERBebQqV4AzbaV4g7FntgJxWMBKqwk0fstWdPagzgRsq13ZeGpOCBO1XPCA49g1QX9rsUF0yMG88fLss6mZBHD509x3o08W9AO19EoMFy8opAqciP4ADXyfhF9ojmV+gTCAB2CT1Ew0qLrtUDstPJ/KaxXEWQArQzhPQqRrm3l4Sw3Q5dWSeeswvbBklJq/d3iK5bGPdYnh49AUeC/0Erg/CAG8R+Aa0mSCWLbBA0ELJ0Tckzn+ElREmzJ24VJq8GvoITbqAR+zk6NCgPm1out7rzUs/ms6go3aSG8ytqpurrfSuEh8Hv2/tuzWbALEVJ2C9LS5ByUfI4fRhhKBAWH5JnaaJQ7rNzH9tObFSrSHrepOj77bOhFsCr5KLo9oLa/+O1reSjbFRQqWMTwMYHGXrhVeROkrGVJU8t3iln0LIneB8tPtkDgmWfAy2Y5NQkvYtKQGT75AlXF4OXKzaAoIYcTaC4HcWrPu1RMcXMFVsIAaGTBQjNVoyx9oXFqUxlPCVMRRoI0YMlTLol2BnCPwwpSrqADL5nfhI/hCwopRgVA0VJUkCBHvO7EmPTQPrnS/N1fBi++yd2nVejlhP3ZPxLcuy6UvdkPkihFR8teu1v0YTUvvA97lkbnJTcq1Qzq3GrzI1LG4pETAK2EadAqcwnmAC3BRiVdjOkp+4GMUMtYb/nhYF7EibiPQVLfxEwze2fMLbzj68dgY7uO9TGNHIrd8xEeHthQQlKitmkWcCRKOjUsAWUtDVNvTcuqsb/RvFvpT3F0ttmsoxkdAN7/q1jDNPicbVYIyrWNwelrCMsu377QT+uRLwLZAd+/NDDcZdnpkxK9ZiaPOkvfd0HCvgLQMrQEqMXqXM3xjUFpyyhkrebhxQCek7ksB9frroFL8ywKhTf7JexbmcFg2kcRxqD6WGzo4+Dc3i9+mhv3othtyjvygmIVd+W5ncgzDvzoGSgV9alF66Z+WiBbZm+W1o5UmepDILjqYoro2w/6WuiqyjAEN8qi6wBrtF4ehGZKnxeG5cb0DP10ma8THDDeYkGxTIpvkYdqx6hJgfK6IwDOVZEQL3SIAH79ZxHW98W7mwDwkOAvxzZyr8WolhEBZkMaCnMnHLW2SjKKn64Oc8e16XAYMRjJJK2pfSMo0Zix6BuvDWbFJmQ+oVbMkf4kVYXwfi9Kne2Z6qSOoZewCfAdvmZGqitNuybpIaMzK3rp3UjZzOtOcR1HKp+jp3Z1eWlQBebkHq9qmNIVIWsrgMxcycJTwXUgkbSrJycrBv24o9EeBxgt/OW1wLxfxyKTMlKWGzvBYP+rEMZQVvSCGVl+6HRRpKFes5tDVZUIA7MHH0790P4li5rO7tIMEh/BHSsUaQ4bG6UOfu1F9K+xRcyvnv8y4WlzEo1mIqvrYe4tLt6IkhYEQHTulzVCD7TlEa+uJUQOhiMnL+ArMdUQ5wzLYC4NnplHLMKbC79lEVz6ipDef9StdiR0bMvJJBPUOSKdcsMavfyxCDHoP/sMVJyZcp3vAyjp8YDgUAbVNIIU2v2Gtr/9TY8ISw1q+qZBnmmuGhXzVQuEAxI2UPZdfufTN++YcykfgvqsilxjHYjdtWbeJm5FwpAIf7Q62ZaTkZwVjzYJQhxNrBJmVB6acIzMmu4qXNhLfRw3tYwjOxFK8+Hd4pwBoVB+ZRWkvzKo0NykkG0/PiPd+d/Hj4ZN0tbazxUM3KXv2bHUc2ktzm44XNWNE3IJv+bSncRxjy4LT20Sy9xP9mxRXIpyIVVTTc1+CTU4r7hFEdv7XBCsgltp0xey6o3ubdr2g7mmAGD1mEN5b1Rdj9UDTbkE5SC+ihBDKnAWPuTaOET0641L8SWr7w7Z8wc46g5BR8boHrrD3nO2pH+SpkjZiS69BmbNpk+7lDVSCoBg/tMutXmcEohKtozbilrTSEmCo6wDV1SL3NY5xlW5YLkOJf10vhz1HrP2wYT+FOZDDVAVdiyr6Zp1iVOnxnrQz+JSCom+L9ih8qfQF2dgrsCsjz6ez7s0DAXJbglS1BBbzkoPxK8+YtI6Tkoyda0cne2gaarXSp9GgdPkUai8duVkLvKg9XVf21kQeXlLrc4ZBRoAxw1MNaD1pt7MLBRDlrT/zRmsUSTaVB+vo32JGFlinFElsBYZFH5iNnl3usRyCWDzdS2bHht7gfqnWjBNjkm7O6PH2EuXUd7WcyK2PtbNIqqy/ieJkNfFHT7E+R92rnI4rKC+1DT9+9dp9+HPtI6zduhQz2ahxlA0hrwnfW5iUkOXNGZOmOnYen1RgqeW97mrn5AQKDnigXOvuzmF33yZBnHWxTxyRM2kgNrOFXqnYLfqMD/JqjDJKfKp7MgQzU4qw3Wv04O5dGE/jBcL4gmpiseiZJdtYwuErwQJVoRnc7s5/gQNnbmI48C9LCDXuJf53Xl3oShkwDZh20cVigD4Pwx2Y/T/2j6MWqRrrcvMyEA3Gz6NzqlQEwx2ysgUdP4r1SZbBFP5E1Dh/kVFO/G9d5INBbj1kokttKvpRujbXobxblwTTjVTKghgp3sCZFQ+XfpqL1QdUQaVXOBj3xpRcFk+8eNuS+eqOsiFZbR9laVE6ID45l2acVNVKB64TPe6VbOwnbJNCIF9wqk+ajf8mxnymSDtFg8Pg3a+PAfd4rEtlC10rzdVsMQHqRRkWxJDKxwIe+BNkznuP4HM7yuKHt4ACP/G6Hld1Az+ogzBfoerCT7GpZk5aiJglzVUz/e84Ql4pvSxeNxZpRlbNnsg3/dfN4b46Wi2EzSHAlkYFfcB49MqefTFLyXnpQ83GEw1SjRuSn64D36kNEQH7o5Ckcw5SZFsJSCcSTxGg5cE+nVGOBnjV0yZqGXnAKKq2ryjy4KXquar1JkkPnIhwHIciamHsLpA+HsnC8+SGSvGPft10VF6d/hAnNefi7gdIjaDPItAbpbX+MO5/xr5P2dDSuN0v3YhaIx9r/wbAxTcEcnQcbT6PHYBaiJkxKTeWpuxOIOlW3bsvyd+tq6Nu2JpB05W23w2vMeooJNaw4lm5IEOw/+JRDwmI9cB+u3W26hVDh3jxfW3yF3NO8q9KnYZg9HTM0yEGlbnK/3LacV2QzBKVHlpH7JPK2xmIKZhiBveUTwJE1qMTFhi80K3L48p/vmyCqy+IcdqsLRye1WNKoSshqpqcyN2cnJ1OlcGdGtF7YMFdOc7yE1/qtVE8iX1RJBVUB+yMbsnX7OHQ2t/d9ro48tinxZagQxT654m2CwMDfx6eyKyvLsuPohQ4MSbQYKi3AnLeZWPQzjxxYzEpBMKI7tBgHrUHrEzR8PL66zrwf583YIUOLWPTqarYdIHXj3HsfUAW5ooplFsrpK9w/f25L7BlE9eL1hLiWAg6k7TI3tNHzC9W8=
        - #2:
          - type: tool-call
          - toolCallId: 60xz769uY4SajIIl
          - toolName: set-relationship
          - input:
            - TargetID: 1
            - Private: -100
            - Public: -100
            - Rationale: The Netherlands is threatening a Cultural Victory and is our ultimate target. We must prepare to declare war on them to cut trade routes, stop tourism, and conquer their capital, Amsterdam.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: mpy9u5JKV9a3xSve
          - toolName: set-relationship
          - input:
            - Public: -100
            - TargetID: 3
            - Private: -100
            - Rationale: The Maya is a close neighbor, allied with the Netherlands, and blockading our path. We must set our relationship to extremely hostile to nuke and conquer their capital, Palenque.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: ok7t3PkaNABM3Qpd
          - toolName: set-research
          - input:
            - Technology: Advanced Ballistics
            - Rationale: Advanced Ballistics unlocks Nuclear Missiles, which are essential for our final conquest campaign.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 5FYhm5txilV0DRY4
          - toolName: set-policy
          - input:
            - Rationale: Civilizing Mission allows us to retain all buildings from conquered cities, which is incredibly powerful as we conquer Greece, Maya, and the Netherlands.
            - Policy: Civilizing Mission
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: VKMNWpeq3z9JJmpT
          - toolName: set-flavors
          - input:
            - Rationale: All-out pivot to nuclear warfare and global conquest. We will use Atomic Bombs and Nuclear Missiles to obliterate our competitors (The Netherlands and The Maya) and secure a Domination victory.
            - Flavors:
              - Production: 100
              - Offense: 100
              - Air: 100
              - Mobilization: 100
              - Espionage: 50
              - Science: 90
              - Nuke: 100
              - Defense: 50
              - UseNuke: 100
              - Gold: 90
            - GrandStrategy: Conquest
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: SL90KcJiIfi0RYKq
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
          - toolCallId: 60xz769uY4SajIIl
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: mpy9u5JKV9a3xSve
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: ok7t3PkaNABM3Qpd
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 5FYhm5txilV0DRY4
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: VKMNWpeq3z9JJmpT
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.