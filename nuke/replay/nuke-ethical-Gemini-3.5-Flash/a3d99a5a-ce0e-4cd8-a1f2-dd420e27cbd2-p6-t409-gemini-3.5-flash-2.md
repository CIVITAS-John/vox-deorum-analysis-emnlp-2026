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
  - replay_nuke: 60.0
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
      - toolName: keep-status-quo
      - rationale: Our campaign against Greece is progressing flawlessly with the capture of Rhodes, securing its critical Uranium resource to fuel our ongoing Atomic Bomb projects. Alexander's military is decimated (805 strength), and we are in a position to steamroll Athens, Knossos, and Cape Town. We must maintain our maximum offense, mobilization, and production flavors to quickly finish off Greece, assimilate their cities using the upcoming Civilizing Mission policy, and consolidate our power. This will prepare us for the ultimate conflict against the Maya-Netherlands-France defensive alliance once our nuclear arsenal is fully online.
  - tokens:
    - inputTokens: 79980
    - reasoningTokens: 4097
    - outputTokens: 132
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Exploring Portugal's Atomic Era**
            
            I'm currently analyzing Portugal's strengths in this Atomic Era, turn 409, on the Vox_Deorum map. My focus is on leveraging their inherent sea-faring, trade, and high science/gold potential, with the unique Feitoria improvement in mind.
            
            **Assessing Competition Threats**
            
            My analysis indicates the Netherlands poses the most immediate diplomatic and cultural threat, while Maya remains a significant long-term competitor due to their science and military might. I am now prioritizing my technological advancement towards mobile tactics and considering policy branch adjustments to counter these specific challenges.
            
            **Prioritizing Research and Policies**
            
            My current focus is on selecting the optimal next policy, leaning towards options that enhance my economic or scientific trajectory. Simultaneously, I am reassessing my technological research path. While Advanced Ballistics remains a strong contender for its nuclear capabilities against Maya, I am evaluating whether *Mobile Tactics* currently in research is the most prudent immediate step.
            
            **Refining Domination Strategy**
            
            I'm solidifying my push for domination, prioritizing *Advanced Ballistics* for its strategic nuclear capabilities. I'm weighing whether to stick with the currently chosen *Civilizing Mission* policy, given our recent conquests, or if shifting to *Economic Union* would better capitalize on Portugal's trade strengths.
            
            **Selecting Optimal Policy**
            
            I am now evaluating the trade-offs between continuing with "Civilizing Mission" for rapid assimilation of conquered Greek cities and the powerful synergy "Economic Union" offers Portugal's trade capabilities. Given our current size and aggressive persona, "Civilizing Mission" still seems highly advantageous for consolidating gains.
            
            **Evaluating Diplomatic Landscape**
            
            I am carefully monitoring the World Congress, especially the Netherlands' push for "World Ideology: Freedom." While they are a rival, adopting Freedom aligns with our current path, potentially granting us delegates. I am also considering the implications of France's proposal and Greece's call for Decolonization, weighing them against my ultimate domination goals.
            
            **Capturing Strategic Capitals**
            
            My immediate focus is on conquering Athens to secure our fourth capital. I'm re-evaluating our relationships with minor civs and assessing the potential to capture two capitals from France if we engage them. I'm also reviewing our grand strategy and military flavor levels for optimal late-game warfare.
            
            **Securing Nuclear Capabilities**
            
            I'm reassessing our nuclear production given the recent acquisition of Rhodes and its Uranium. It seems we have enough Aluminum and some Uranium, but I need to clarify how multiple Atomic Bombs are being produced with limited Uranium, possibly due to import, vassalage, or a specific Vox Populi mechanic.
            
            **Improving Uranium Acquisition**
            
            My immediate priority is securing more Uranium. I've confirmed Rhodes now possesses it, and we have workers available to improve the tiles. I will be using the `set-flavors` tool to ensure our priorities align with Tile Improvement, Production, Science, and military, as our current high flavors in these areas support our aggressive, nuclear-focused strategy.
            
            **Refining Diplomatic and Research Paths**
            
            My focus remains on the impending conquest of Greece and preparing for a confrontation with Maya. I'm currently evaluating whether to adjust our policy to "Economic Union" to capitalize on our trade strengths, or maintain "Civilizing Mission" for faster assimilation of conquered cities. Simultaneously, I'm confirming our research path towards "Advanced Ballistics" while keeping "Mobile Tactics" in progress.
            
            **Consolidating War Efforts**
            
            I'm focused on finalizing the conquest of Greece, with Athens under siege and Rhodes secured. My current priority is to improve our Uranium acquisition and ensure our technology and policy paths, specifically Advanced Ballistics and Civilizing Mission, continue to support our domination strategy and nuclear capabilities.
            
            **Preparing for Alliance Wars**
            
            I am now preparing for a multi-front war against France, Maya, and the Netherlands. My current research into Mobile Tactics and Advanced Ballistics will provide the technological edge needed to overcome this powerful alliance. I need to ensure all Atomic Bombs are built and position my military appropriately before initiating hostilities against France.
            
            **Maintaining Current Strategy**
            
            My thoughts confirm that maintaining the current research, policy, and conquest focus is the correct course of action. With Rhodes secured, uranium acquisition is improving, and Greece is on the verge of collapse. This high-offense strategy will enable us to finish conquering Greece, assimilate territories, and prepare our nuclear arsenal for the Maya-Netherlands-France bloc.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 1yctvSuNdoap3I71
          - toolName: keep-status-quo
          - input:
            - Rationale: Our campaign against Greece is progressing flawlessly with the capture of Rhodes, securing its critical Uranium resource to fuel our ongoing Atomic Bomb projects. Alexander's military is decimated (805 strength), and we are in a position to steamroll Athens, Knossos, and Cape Town. We must maintain our maximum offense, mobilization, and production flavors to quickly finish off Greece, assimilate their cities using the upcoming Civilizing Mission policy, and consolidate our power. This will prepare us for the ultimate conflict against the Maya-Netherlands-France defensive alliance once our nuclear arsenal is fully online.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 1yctvSuNdoap3I71
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1+baZiNC2Q3iCU6q2YOf6zEZo27FktW5Rj8CXZ3EJUHtIRqRlqPznBoWEfNEV6SVgWa2GPxlcmHXdL7Rk/kqJop5ZHB3B8ThHl9s9ONqLV49H974b+ZwOQ+v9HnaK10cXZ+33kwwk62sRK3MJhe1K9GRudEqML3gPdQgGgIifHTeDgWNThT/clERjHMocsY6bXHgUX3Syg6VGMN86238xe1yii612D18MEqjH7wDahxLFPn0RudKelp0g9snTcH82SguwsotPkLbD9kZRTqO/2wlqAV1tSXe1Ed1X6gDkjod5zCXBeLP9fpGywSVto24xwE6dXIW3mP04McNc/geOpyCF+3Qbasn8KMKaApIuf5voVXtDDPSi5qJgddAQ0ZiwQI6NEYVUSQZwC9j0Z8BHHlvRdaahXwHEP16uYmOsJWS6I/B5g/uhBTj4Xn9xP/QFpHKJeENQ5fQdfQw5stDp2P3FsZW1vIPfxew9FISL/QdiWCfO6qJQpMQNPek1hGEyf6YC8X7ayJQaAlH4Ykz0Jez6ebyIG2pv1f/wQKSbvteSVo5QqxG4rmJ4ZUCOw0Y8hm8HsfOu5+ZPQrY91bOfqfF8Zu5TgSgqvrXpp2D0bx1o77CNE2P5rJid+u0cs+y4KhPtlwPNzUlVYaROWJDj3nrTUi3N4BwCs7VSQlCm8IBnTS485ixf3R9XduczW/eRGD/bXWjfP1vbbTo6oMqAVGm9bO/qPo2ZeM4TJ7EWmPhiH/m43rbe52SMcXdBijxpsn1w1Us5b8t7Pys+FFQWD05Z9yt8+qzyQLhyk4PPqpw8t1klzZ8rRAVTIfaSC5WMf3o33qUk7nDq5Ll1WTXL0U6LwYlw0bm8PaSI8wMgnCQbb4GT1oU8tSgFXF6ugFxGBkPgrqmFENHelXEa6sZ/wAJORGS6XFYLX0mpGaSiid0OmFcOSEhePYIVsiLDZYLS3sBHhpk8976qEg7OERfdfV8OU1veHxm83XXemdXJRhLv0oU+nWdESSTYjwwtnj3bylnzyXpDq4tlqS4lAEWUFXZY98k4B136P+Snzm4nO9cvUnhq5EydpQtBiYhUMCKXlLvqEQltkJPeQd67y7i0sPbIukNXWPKHeaz0enQ0PCTW5Qyqb8xPF/a9sroX5bGWedQ2kDJ/bZoCafpB4OyQnmq3dY0jfF/hRl3pZEK57U8aHcWwAx7mwyHvdMw7c6L8BCbD3lZTPVQsDiMrnkGeKfYipkXJSDaimhVaEL3SU1L/qHX8cCL5q5Le2QcMkjLyRxK6pFAKj2EQXimBXKQFpIVjk27V5gQvrqGjlRA6V6s+PybORTLDQgLLF2jRjEfJiNgfTllYSvxbI6Cgq9MtJXx+2bj6KyL3waq8Qs09e3izH/ZS+BTHjFW0cx1pu34Dmv/DDTdO+DNZNZ96J0vM1pAmhqQv33lYPCoTIFO4wJ4FLcppeopIbW3ADhg7FP5JtyPscM3n3iPKumeKU11sJo0JbOV64ajWeKNqTb88U0jJ4O8+Z+gGH7VTrBfrGHPFakABCKxA66a51SzZgmm3o6Pv03AQ0db4s7Q30KhGUPhJqSJwNE8VvU/ze7+gI7dyWVjwaV+WSOuyuQuGUFG7t15+tUTEp4Rb7qoAMIoDDrJSgT16v+NM9bcUUhTu4IIRT+vVhboLsjwXR0AyhseNejMFa2iocQaggdVPJl8s3qc2eXl1AbtBWke2vOUY2GIGQ3Z2d/IbZAj3rEGIPmX5fG3C+77uHa4FT8Shnpo0JcSJNi1ogWdUz1wOoii7KCJuVuUiZRYkiz2QS1bP92A/rZgzobstu+X+5KbW9tkm54Wuo5e/+HmjlAH8OaukUVUVzQOuRznX8rdoKOGGB4XTlyRx5k5LUW/ms4arBhc3LfLY464obk2kQmMK+cDjKK9XMh5LfSCEpq9nbI63R1PI1OEqwI5qvkJScz1AYpGes6jqkmoaVvO0isayFK40oFT91TydZFD5qUMOjZaDLJ2+1iDJR/vAOou2WhtfL/dVMCBGGTACV7AvHIS2mp3izDQah4HP1E26xYy+Qc266rdlRXZQBZJVicQDBDGe8Ktc+id/tpwLk1GPMe2Fi4Yfz+aZqL9vzJvX+jxQ9JRa4RBMzf5WIgBPjZTJAvy4rh5qunnFE2D7P4kOKS2qm1f+n8XoydKTEapR8S5++0rigBg1g+PJGXUFy7ich72dLI6tBbg93tPi6wukWJUNRdFj/kxvFvGQFzKpfT6AoSXP7asus+i2mT9QSFceIlM2s/ptXF4jU7yWMphdKzEU6p8vzuM/nr7evK8Bq4FuOkcDY8c4OO28k4Isi3pjru5gOqbAzEyxhoPamTy/QBulwlz4gsy6OU9ebhZX4UDuuapKqj4RaPlpjZ5TSZ+BwxQObI/RqYCq+J6b942DGL+0FuK36fEwZyMICZT+5n4VLZKypHvZThwDlYRutExCU43Z371/IouCzOGeQVcRezdRFuw3Bwiz/thqFZbaBITDXfFZ9ZrR63RD8+MCx9WvBECpsCCZNpMBbn3G4PNP0PEyu+mvnou94aT90s5uLL2Q93QsV8CGpzQw7Ft1AsT/4YLS8vXEPgL3eetfQe9Sbbt7u3uSpYIpl9pt537TuAonN6sD77geWe/s8x6Tl1JDfhB6yrotqB93xE89bAq330hLDu4Df73k5OITDb65JCgyxVUixbt1a9W6mxUx00n156yLYxxYuuq/zDx74Fz6wTAu38e5C7D7i1LUUNNjQJ+7wmbOY7tBNKM3YTe6IHqfi6PoK6IqdjhFjfTy//piuu8rbxGfhlG/oA5grx7M6ZJW52D2pC8LuCOWHu/F1GOqXKY0tQfXJOsb5G1dMNWcejkxZkD9kfciDkokh5hpbijcav6sWaMDcwUl/sw9ywHceK8/X+DA8JvrCDAe6cYCmvX1XpTw595sz5hh+Qqvcf+AFeDBrNH274UPdDyVWR/cTwUTuU4ZeZcijIiQPEM4gN1FOil0deYi1X83+S4QerS0DzvUymWz9IboGb+guMRSpLjUizd60IWULHvR5rcuiCgiHe1Jfv4RlUPiygO8Tf6mc9CvCdfjgc1mmg7+CuiL5HUW8NokEpW2IZae5qR7cGh3cuuw5tyD4o8R85xB6dLD4FMgyGbQ4INkwrLejBF3D4fIs9SZd7CQYNTxiR99OxizuU9/hWeld7nF1b8oXmS62WVBumZGB+6iX29CHOiJDMes0qbp7o8nBl7z8k8mxx+kMYUW8VGKvu0Gb7MmmMuu2typI4QdALHpniVLwRllRY1SmxEKq4wJRLZ3Y00K6B9jlKOChaJQ9rslXH8lqWmXbX9WW4+1wmxS2jss1Q6w3LvGn3RWrKwq7yIp3+o4gswdlUwYiLeiwAfQ89JJQWeXqe2rmQB7soh+xHRyp17XgDmeK+nxxvc0ah/BD41JGIy4fG8XZpGDkz5YM0+f0GVnz9g4hF2P1LyOjWdO1qTEGzEsxOTRxXa325DgV60RZGHA9wYyZyADQ5uSpI/6QiHJWistMYag8CcUuKGTTZzRxsmAkJFtCniGomx5WLokTTdbRxQi7+Bc/xQkqdV7kEN0p8Htz/7Nmu51F+AFtrOSq3i46ys4EeaLuLxBeSm7qZglqBkzkiqzt58B6q9tmHxmTmtlkCSgPv2daWE6m1pFVVMSMDZ3Cc58wOzGWu2CAF9jlcoTPrvXnti09gTx8HuA8r4TqBx9VDE35pkpGk0jCWDf2AMsMJD/ezYN/VxL1/Q3oN1IOTeVc8Q0pzDn8awPdZE/lBSH47jHCl80dZWldJs87zitydZ+GDLFsIloJwsE5SBJbUYUvFGkthmbgdt7l8UatkKwLjzDOFkTfxhMoYkJQy7Iey2kZJWQNOsyZymnawDPh4Je8T7xb3khpZde+93s/BAXzNWC6Mfjqd1O2TxeZlU6T4/weFBZ8N6KAv/b3H87F7aGoGwJtv2oTA9MrQzPG2iFks74P/IWgW1hKDokRvNvMMuiGQyq2kmuQKISgLPibq5ggGeti+d7bnibgj54iSTfg6Vs9lJs9YxECwy9A4LwgCbG9Elo1IkZsyfOuYMLu84JCTMd0c07uE4FGl/SXaLwvdeH1pDnv07TWwoUK2SOc2v6nfgoaC0FU5lcNcfgx9VQ7iCXWqPdTQx217S21sy4Vu9noSUlNggVprYOawfa9mM5uOB4gtW9e7f0sJp5YvYnILSGpOgZ6SUqbjLqdRh0MvJfu/DlbcFo7Egwtz/mf0OBOxPDphm3qFPNse81iOoEzNInlr1iZP+kvtVYkzrck1tMTMa6DW/RXmr2svk1WNQsOzkXBwdNeeF9DoU5+QfT6IDoe538kvF6v9Rs/efUtElRRxYVMgVE2poGSJpUuhyoG15dRyFTD1csa9T+C0XdFiBMfyWrNk1OgkgOyCGKC+wyTyOINLGn62V3PgTkM3K0uklwEclJL3Vr1w+JqUuyQ0bjhMpIFmMfMP74YcM0SCCubEoMqlE6Wsz6hwDugCZ3nfFPD14gCCZgwGR1dG/B0rXYw/ITGAZglxXZlzIytd3Kn+ZIxbkWtAkZxAFe2Gjn+sfMIqSgBRQCGIXYBzKmuGTnWKwBYZaBQSTchh6S+oZALuszdrJ3YXqmCNk6Z02iOYuYOMIw4FPSWoSOSFUm5tmmcr62Ghk1EeTJBEg8YvG6A0Ux5NePeBA08HLKVl1S6R3nwQJoFHXecD9ej1HLR+QJlt7rnt02RObemvYh3BsZVJPvBSWjRWE31axl686nMuc+EfHJrL50+cm7X7gnwz4TkQikRFp68IcPLejMv8OSR2pJscWTTaV0foIEoNIfsl+Ig4OXDVkJA/Au1Wgprokr1t7MtmB9F3CqA5zT2MTWQsJZpSidlxr94W/AdisPFCgn0T3JjfAnoE1ASIcR647HA0aT/3KW7yHBz4eDbUd5sIQvzCDzLCeLc9RpNaeE3VmA1tGU/9SC5waXLoMDNGRWFkS9Ii/tMZ3KT3b6OJ9pf9yB0yexIhWRDZiWz41tD1DhIxQg/FdXk5l1DV7ncXOr7Y5SLy9St61YwIbMiMD9IpNQEcEJxCmVfreIq38+gh/XfmmTIL3HwyjigXhFplldrrWFiMXlRUwgDVJgy0KK0ewm0b6Q5JGijugoL6LPj7tgDhjaRe9UGX+DZK33CDt2KZLDwH8rnNQ8zSpWXBkukC9HFJnZ5Hf1KUgMAmgIYqWeGTIAKE9NHcUlW16aVwGWB/Z23yUIvGwm2jP/gdLTRBPvBfJOHruZFi8nXPDn5D9zWaXQ9HshiykC4hrcXON4CbZuM4Y6OG95xCb/Cg4lpkC43aJUJ3tlyDh2/KFLvaV65XquqVtGF0qiL00JP4JqdJy+i9pJcN9XQ+fcVSTa9qMAzWoCVYxhEdsetoopMuUp04enI2kQFaTQMM648+5rz1R18qUg/hWM48NST8G16ZXwCp5/Y+MpY4GXPz21vlpo6c6IzzAU/8DIqD0Q0mOusEQG6i6pUflgdtCwm0yjIwUadC58/IXr/BYX1INiCF0Zb4+c/aak5Klq6hy8s59ztNhK09sDKqeYIUgnlseMx/QaEnXfAaQmt5syd0xRFAdtgtf9+rQ2ex+/60Jr6n/p6+rXITyIC7bmBaWuklrdy0BvpDy0JhA6N/cZFXxsrqCnc+rEdmgctGxNaij3fJq32HtlipyNJsMT8oyBZEh3Oon/d+TGGN/IV1mCFWh5lFZz5BQP8TSVA9187zXcilWAkkO6OoWNbCGPwF63PbUxp+FAwOCf630ogoMMiTdddk5DMDwYmetUCKdssNOFF7FYVwckBfe5FhYrGDDlAxnRw0go/QG9GmyPFsHUlXe2221jTXuj/vHDytne1Ts9G7uHZ7dMTsz1YJUP9kkxF0Qc9NhdAeOBUKDhjgCcI3XkCED4biqhcmnVwq+6xaLdJgDHdmbZTGSY5bUTbaygh1wqp09QuClPpoloJMXPHRYyHTJJ5x1J8TkKA+134I9BwqzjikddA0DknXajiYfWebowqmvV02BWaDAPkkTeycK6R0qBf2+eiblAnhGGp9jLxaqmqUYupoiEBchtKx+rwfLkcgWx42jH0KMNNVAWeYbPMg1c2r6j1mYUfc5k9HKSu4pC3ipX3T5+1fE6EeGxvBGhfKSxF3ip7NtnLYR9bMSKg/Xeel0iKiClcd8TRK5x58IK7sa8BwUNCCMdU9+iysjWSQ9w22rcYAIE5rTg7LzH+byzLXLtgkYysuJVgSgz9+OZbXeHup8gxAiru8lUHlugfztxb2nIFlE41AqMW9Z+FUDlTyw6PK7IWbFPuHFFF9kpZJZtX8G+OpZp63R0hoZnz4ZEqEwuSFy4UTuq6P0Ybp+WTR8aJDj2gE7dd6vfvEFoNDMuWdBrGicE+XnWxVF6V+ScUtQl5wftvSEB24aUUjyGXLZ0RhyFHJZoqnSAdCvK+X9Jx8HYLcHUkvia4ulqdUqJ7hV3rOoXOEuDCJfvEgS+yo9+7JvoKY6oEo+0+ghmEsnnRyPOcceLrMfu9n9POJ+fWrhuoVbhmLUIlsnewX4GZfu63zV02uZqYlT/UkfOcsoaRKNWQ60DqoiWxR6WqGtRTYDQyePZBi6bkKMCyhZ49TXsmg5UZLKRAXPywoUokVmOlM5DKtcnEZ0bR3GQ36qjyXuDMeEOE17sXBgScYlgcf5BdBDDacv+iOARmqKdZGAJ+d8/yTmEHuYukmwmQmYkq8ExjBj9zFsumXui6e8hFR7euCN/D6T7ennVDsVwd+HAuzXM4rHjrZQpzO7Zz5ufyNXjqFPC9IWk+S8NtqfTYQSBy1I4dOphO8PdPW/g0nQzUz/wW5z/JFMN+RImXZmjSkjI/ASqdJhcV0UxizxLgW5F93JYaFjJIGVQN2nQs1rjWLaSjcFbNYovyBCcW/VTDDU2ThsS1X30eqzGBLdbdsl9Ou1No5PA7hkaAfa8CV74pqkwY9AwKV+6gl9tQZQLuliZ7jVcl9NSO9c7qsg+H+HGzrk7lKZlq8Zk8LhsEuphIRhAxYRD3ckxC+Uep6lxqT1G9wt3l2PDlIx/fsNylx50+BVY+gZ95s3cIiaJiR7vvwgxisHPWI+hAJDUAV+EySfZ9UqiYCzKg4c0qcDX6ASNxiXjdyd5m5lLYECngpmToA3ltvjzjLm0UkIv1unICx+0P+2LK2N11Z43do0MipFitflHdim3b6zmhroBbSGcqimwfyu0ZNLmIfBGO75JUsVGjdhn22MpgG/In314hqcPZU8O5xbbnoSsGgEFyfgDmJtURcrJv+rudJk7Dp2zA0SrUpMTDrv5KQnvR9QhEuCFrCD/N2+sPh/hxGHhix3kp0uTABtQ7S2lc+c0jpl2jbHTTZIJunCqXBkptH7UpGlqqJD8zw57flwu1Fd9pUNk9ihUlFug/WycNdxUCRq0o0TO+t3kZxK+GwqhBskQiKtaJfXWSooK+1XY6Z4CoLBAlSPhnw4D/TZ0JDBmD0NM6hfWU/MZ62YdGlbeSzevpC10JPz2QKAtjZ1rfuR20Hdo2g/5IHHUex5hBt9ak7nrUpEHIe8L7AqFZrIFsdHH1B4U73LHT+rJIiiEGctWOoo00CMR0nRs6h8IDICAQm8+7l0i2bf/vtA6BH1o9BlcwMVhL9YFvmKqggVdb9qiF3m7iQdb+tGdekiyVCfcYfKMsJEyjHcvM4B9+A+t6J/DwQ9nUDXf7iceO8c15UMHQPtpkPD+J7Sq9DAvaLnGsnHtpkkjczoyiVwNHj9Xg7pLzjlHQ8np53ZKqDRII+z5usDimdQ2FU0zUYGV8RmxQD4x7j00JXin6cZ96QECg1mC8nmBt8VspnYjgqg27XJ5BAE8+5Rtw4o0AZ7suFqLkNUfKHlLFgUOIbE4kpVZwGn0Ab6Vp4bU4GDQbtBtWIP5O5dTsbC/8q3YOgHLUQetzmKKAUxt9YAU/iv8UI+4TfaJoxczpLnn7PeSY5IytdL6zu7l1WfrIU79sdOs+qehXAaWYI1V2UdoD+667rSUUjoz0yOq+eYSkTrALAOklxLm+Xl7QbZbLas6Ic5WULo6IkHPX44TuxkcUl5gZKOaoTfpEz+j3WZn0F+kCY7l30M0I8VBOuReQq2/KgItSQcaKUXM08azzLUCF/IBZ8tWeSvXFz/70NzNgB1RhxMxSzw/Ix5gFCsEyZHx3TpaTRWnS6X4kXMpY39XwN2iu+IGlHlZaZUpLVtfAt/dBOeOw6tJ3EFi6a3DkiJezBoRC5aS96SVSZJI97iRcNdOGKeGYFjqDJiPZ27Y1vC3FqUeyFTCOERfD9JBtNG/4XnFvchhl1J8rwZ/4LqRHTfo4wNzWjys7ooL6Wi2iplr6ZUYeNKpJ9GyG6TIjJHfBFGc8sE0jUObjE6zFsZuKSr80yyX/iL8+BfRmc+UGZg1vL6IxEzFiY0RpRVeEtN4D0Dd1u5AhduxgYWrYo6IEYN0Z/TbU6vSCMsv6kaxtbLPSgpBQJR03QKpuYKhubrniAkxiOymbnQSQ71RyZm+CnsoDWnZA2blZzJPG/deAzdXsWa8v0rq9BElvuUBpM7qmTaoXd/hly6glXtwhuNyd8zMLIZVjBQ5Eu5TdxS2zICZgAA4zmMRhWLi3Mb6L9OuTa6MWVRAj+v29BVWQUfYyVbWjUzkP9/j4Lv5dHbNwKxufyeH/yrtlk55/0U1heEEX7jNbduoPxkH0eGd90BGFyn2JighSTttsUnCg4ouQy6koX899IKFkQYpWRXHsWnfR340c1O8AJNZ7dmm1FmiJMdA7y+1L2Lq28tS5xeHy59SH9vj/RaVBVyh+4BXEiPQ65ak3bMcHZ3x3qVvUIKqRXWU9X1nGSBEEwZ3LQNRI1S4hr4IyX1oBrt+wH3HtqvwHqKQ2UWgV8YWXPfr2fp/XVjOGcAKAYQrb1g9caA278CjBxn2yOxiU1LWxBo6kk10Fm7BCGW4jeVuSh1e9XNZ7HneQZeNw971x8pkXooygIsYNu7XHEe/pbYCsY5bIigrlMwWcDFpLFgPOYO/6YE2tQe54e/gblNDEHHmZ/FYhP9/zPst0ycxr7H1Sjzkn9koPAnJRJgBVVRx+9psBdUOlcw91VlRsm9J9yeTD/JnY8TJxxSOBEm7qZ4fFNaMYlMv1PZVokIaj8WfCR/Lq85oXdizj0jAg0K29X+8QcWJ5vn1jhk1V0nvMvS3EGuBxfg8M+1rQw4p02N44U3IPyG36USfv/ixLBB+00iaHy3OwBa04JT+XNv66pigzPhxTOrC5xJpJC79Kz2iEacKgr0utNUAZXY/LwvRmSWZcGOFj/ZvP7Iz01bIMgfJHax6GK59RjvXgz+t2mdqXvmohJ21DyuUuK8kjVqQHJjgE1Kd7BnRNJIVuvxm3cUj7WEekyjXD4OFJCdRDWpQgecyfzt3C8ajjcmx4kmKW24BcRHbCIXdLSm2dweehrDbxJ9vAWbr0aZJBvlrOpdfbZNq9Ep/AqO+V/0KX1xY2m6qhZNZcfE0qfWq16sfYrcIhfwu1QTPCgmWGhmJuYV2Kp3DVY4xf8TkKMOmmV6Y87JLjDZ6YAH2wd41Eu/df0FH5h6OQwX8ERbM4H63i9hcSgQHbLAb2jrm8Uo+MFq4VV6jay+HwTGHiccNmzOwrCoc4WMHnj7mxYSS/Rf1z/lrHZ+YH+1TfjrUjgKiiEh2uQTHOOB7qtsXQ2STGQeMIXNJXmrsokI5cIRppUq6AsPctMBlYhzcgEePBEVnuEOYIbrX0QurP0dqSkY/4cLIegnl/9/8KqdvYesho5QUiaNKDmm7fYjU0HMvWkXihEaIhD5yuKmfsvx6qxCjZ2s0wst0z+v0S3OZ0oCOVUFg8CNIpVkCbx+qUbzlbdtEK+ATNJfhJ8APyC43XDa45ZezPaJzsx7ChMfSrDZqTAmfCwTUmOCbNRIn9ft71PJTZcJf5Zl2a3UCClH2iWxzMBqjEIx7s5UUFdsOYwGb8U1RRlMNmqeK5Yrc0q4k8hGMLztaOvUolCCVZBDdL2HIjvSEAlcdwYaBq8El5AQY11xzr20KVZOMCFQyzvbPgqpUDBlq7UZrMze/BLRHX3wWLWKFYnMmofKehRp/Wl+tUUsRys906mNEtCNttzC9VSIltSOanW571Z48pOqpzBaeI0mRXKC/5MjNiGqeCxesaH46GzBWRUDXiaALth1xSofeqYlTLMGzjku3sUXnwxJnqOeebs7bkeT+8t94o6DGnMC3r/jjKf1EaCDUWzFcCov15wMu7fK5yLAIFJ91zts+5W1/CmwWvIGXt4uh3KFFK7MLIFQe1ncQoK4vkebor42iGXgm72QR0GolRXIsGwb/70VQZLbj6eDEZjvuCUd8KrKgmwSM+YyO/GyrAj2AHpjmshTJQ7cloB170Zm4JHgLHiCq85fGs5PbD7KkyRACalO4QWrzNu00ZrdRjS509HIw9SMqV6uL4tPx+y485jSoqMVlw3wb60Wip9sxQ06QIqMGoguRydbQE2GrNW21ggWkl0mCzNr8Clu3NXz6JcT3OLFjIf8Qk/HadpliPQGbxAjlJeJ1VeLYIIqrM/+0lg+BMh/dgWQadaNDC4QxQvBT+KBvO4XNVwO+jis16QRTp6YzdRLFd3ITi7VgyHOKdBtjr6dps8f7j1yasmZ8w5YQ9SIetUgEBLy8cQJ5if516b1O1K92WA7tm4Bdp0kh0dzGoM2IwEAolNxItNDC1GD1c2XoC9d/hVj7Ow0HLG1SkxIVmPjlsRQsAqoxqruvjTdqYBmE5ZAPwOKOMZU0qT9iHWsE+LiFUOel+VQcF0i7ohc3VaUvA4HAX5rAHcXK5wCChWLvVC+WjMhXzVSqWm954+68iQzfCtqa6sZmtBdSQBlZVfl4i6I0P54KBETn/VU1UKTW8BXP6heQFwl5MoW7NFfj6ozqK6dopdRRwsZN4CpO/kG96cYi7Z1wZeJx5jkhHfBjYiKp9SHxZMZywsmZbgXwYRh6Z46fA19MzVsto3bJqyfAVUamcdBhTyFCvHrG6droaIds8lU1Qd8vL1KjX6jZWwyvYFkqHvChKsQ2/jZFI/HbJC7uVyME+Pfk0tUdxwZS60UWJbtZV8ywSn75vVuqfsEfVwTCXRlS9F2QMDopPub60hpeo/uDJm4XogNXOBfRxPEZ+DSsx2lMv52jnc94zDfpDm3JjTvxZhJ2SuNHISxPu5Gf+b3kcxoXBBBgHzp4KzDgq1Fs+6gNJZlgNQfWAJqq40uO6pefH7r+8MNn/l2oPxKnC8xmvtcHEeorU0K7EARXCzzlTzI3Tm6Gwl9+2GpimZYlEPN6j7KMUtavNjwcIu7XURk3/eDlUgiiS51ZJef7m/X3a+b4miQ9n5o4fzJlDKfiHIt416DblaAb6U7VJnuQtftDIGycmSBwUdsMeJjQd+zG8bLBjEdZo6xkem5MLXyr8Ta5WM3hS/ScMTohZgPIK9IRbODA4JBbZCCs0AJhvVyWyhwVXLbjgN6GNiAQ2rENc7N9N/T59HYlR4tufGBYVQrsKnx947jvL3kX5alRSfaRz5p5XmzJSirN5VcWKfTAXKsiklKTlDTFSXaM3akH68aTlCxBSCzc/ssxiLSdRYjpTNmjxxy7RArJQNRE9RKf0rD7s4OgP2UZV2nzusHsUI4wlKf+lUx5xvvTFP9tPXg4np8F70sNGRzArLL2Ha399ZOoH8fhJwhIg53D1RybvsqpHD9EWJF4t3vatDumQPwaw8U/EfE3vt5FSTFbAHuWjsFAh7JbbBhlTdIOsdz6VBlL9AD5QDHKgYIBOOQ8xfZkp2NIToXNegNnmtS07FWuUWWC1d7Bw5OvZL3ybpnP5f56jfuNmUf0oDw3CdszeKqRB8I8m4OlIoW6OSGRu+lOfzq2aT8yz6FXHec4p9fcd26BgvuWaxjv/NGuGXwu774buhf7YX2PGs5QVOFMSNmJ7phO04wlr5knxbgG9Go68xj9OusdC7Tjv2LUH8h1k6v+LrhQRa5TRQQHuKsMSlq7GwXrvjOaxf+2MLf8Nd3a9tqy9yM60ufYViRp3ReBNuoX1Wm30eJEVaheWXmXO1lEMLrXIwFQmpwxdDgImFPMm0VNzX2tFAIO7zkxYamrrSssxxAL4NDPB5KD/aR6uV4YxUHeozgF4FLnWGeVma0+Pk9XJxWpTKAWjobW9ikA+FjxhUcZoNA5OJLNOj6T4tk0Ds6oGnXe6V/APFWEWsmQufCXI9fx4OmB8UeRUnaujjZxJjlRLiTpZXfOCKiOG6yG0Zdj6tm1yn1DRryxJclURZdfzqz2wOmrSvGbhf9r99TIEFs0acZjVBmym0If7zsxRFqgBCU48rFuZC6pFQEMXd+vEBULby8oDs44466ulK9WH+S06YnuflPcPlib2cnrMumlbA/SLQYAybtxLVsM++SXn3ndIMX0Kx54jzvJ+ozXCMir6gBu1OKaQDjMGi/ReXri83MKkX/G+n2oFgHxVO8njd8JlHWTE9WhDGE6JdO6k/sVAHmTWsQF/rcSkXHCQ0OVZONIOaqz1iP7dQvgzBIxWVxeUKrkStgAcbYJN+Njy03Z0l5GnXcF6dZ/Aew/0uEFrqKGN2Fl1E2jVSMKWmu/DDpkmr8JL3GypuIAVVlZfIlCrr9ySjE96mNV2vqGSZp4uRcHKNbkVVjxPNbrCoBB96neaj0cuaxo5DpwP4SGN5iEBbmgzyG25qqdjY/fv4jV7jA9kQ/P2fJEoKjSMj/oiCoy4iR0I4UGqAp6hvLOHGyFYtHqwhihCWD5i3kypWCzQCjaxkTwMBLAVLBcgNNmvMxDRlPS1IkNQHT9eL8RH8R5wULVVpjwDqJmiYw29Rmvp74Qoh3+aUcg0XvlDiAqSAzBAeAMfz2ro1EFAnqovcfJE4edoNXxx8piq1WWr6cKb68AQ2C7MFYUNEv39I5uGh07qKHrZ7a5d3epmfKqprPPTTGZjtUlLfGAKfo76LWtL6Le5FleHAin0wgrx5LJCJPY5E+ndoXYE9CdZAxZ8Jt/VouuW7hY4WVnwrtdZNfL49IFau44xTw4x2nDLFVzhVFtyBxt1KpB4PrdLAzozI+Z3+4vpUKTM+qCPeFACGStPKQ5R2rNnnbsdFJ5+AIv8td5WEIwYEclMhWF4KDps167YY2L2+sgrJwwyOxYWfZ9Odfw61THikPIalx4cZ8gVs1rlc2YyU7GVdgKmZNOujHHD0SoPW9E2hjr0uvzJwL+AD7yAmgV2MRKFCkUPaqQH6RYGU/BrnmsDRsloy23CGND+9KxS3SSoHSJUMIsob3QL7nvDcDR1mClhnP6PTZX+3MwGKFa04N7pR14YtGwTnWc0D3mCMASEyYPpkjWGCxudEBcmly5+Q2qlqVEdQik1V/9Oa6iqHd1y9KYwatx82tim80RoGScYvERJh7ojg1nLtlcsJ1Vy4Fa1S+lZ22IEXNC4lCNYF3/lfLOYJ/QvfeeCvZKwyOn7lX/msUp/4cxukgynWqoC9O/h9k6G/lw6M901UDmN++bLBCnZw5NAFmruRgUvunq/aPHuiyHs93yxRP5MiCFTi+TlCTiBLpreb3VebhQxKDyoNOzacRP2X4eR5T661SCEBQbk3Fe2ZKUQXA6+1cp3YS0BmavRgVMd9PDJQFzfisTi+55nqPDPol4Bo+O1iKZk3cwEn1UosAFwnWe8ry7/Fdl5Ped3QaX/vJCgpw8cG4/ikslmaYKYxYiDVn3r5lOxSrgRjaIoo4V6z/MRuYojic+k7mtL/7hqgyy/gWJtetVhljg7bpxMJOgY0XjL/pu4b+4MXMaFjIznXlqdJ/9l1jZKFsM7GMbJ/NsTciUhE23JQLwRvqMbpLrTAP+f3ylBwhu/oyyLlRR8ktUspO9UIK0l1gO+tLOaxBbYT5tMcH/i7t1gaq/ZJmq+f8Nkb3Yah9sIv3XiVpxg0cw6Bb1mfaC9xlqmG8bT1Dx8Ch1Ql/BglprCkMA/avbiNCUlyVOeo7odbI7tpMueObAntKgGHIXWKJR3mT9YCFG1FwBvUsHSi+aoAvzfKHUn7EU53hcfpoj9qEwLWarGgLGxQjURqC57pjjZlduX18bVnKZZrBnfSHj+LyjivX8bDr0FGrTTxTaOUlYRksgY+CKfmfp6Rsu3IzASnYJvQbA44P3mfVfYfYDcsdV8qHjqihRjUhGsup/1RhGixpvWaMZvk4BwGD5i/ULMcn50uqdk2+lYZ0lgmyHHk7fb9NlV/2qJLU9T8buJaRbKlU+PG7ugr8uCrlaj6nwCzm5vZDyEUtGxwmb6wDF6XPJqzL4me7HfNY6NfrpHsktQE+6ruovT250flEKxvZ1XJ0DnE1aVZZdKB4O9zOLBphTb1xSGVuibWUIhD0HOTgYoM58l5YDsRnrX0HzSwy/QQEqDcdPeGGr6Ii20n/zcY58OffNf9qBagSOEmFUeBC93jYi8BvUvbnPPLum6gDBm/+vAl4e3kM4PQhGvvULNGAy4HHgeQdRdtYts+/A+K6OxeTK2m3iwxSNoofh7tXaOwZkBJIFahaIJ91xsJ/nvUv/3k/w5QJn0DVgPKFQOeQpEi7bXXpuhN7Yl/Rz6lHYCkM9b/bj5tqGoJ4NLk1vJGvHy74GuWtz//3ZTc7jELXqcL7xdN0igFyntlM+Iqx9jjuefRnrnSwsEhnQyoqDSTAYraz/plny8Qq4HBnmqVtCGG+gff+O0APJTS2V1IWIeyyXMNmgwF/p1MMEjpSQh/69eLRtqOanC7PE0oYdwjanJNKJuEQ/CXS4od2nAXFd4TS9cfcDZ06DOwgBAvFBehfihd3PUVRvIQUBtF1q058vBuCeZQOgDLHjkw/uEBlU9kzwYvpVnVAmZn8Iwq1HJHwyn6T+lkRK3qv/ctGeIoV0mkgtf8esWy+bW+/EN+BWgBtaZX6AN8r7hQDQRmSHbtHuL8NRfK1mTKt69U2xW04OzaiZN79NbY1OdUE0ySfjeVuBx7Ae6SW5o9ySdcMimPPpvh/OorHbUXyuuYAV8AoGYK+gqsobtbfM/SFyzZrNt5kiCvLFZxhZNDb6buENxlGIpBwmNH6EBMgThMadtbfOE25JApLRFws12KSPS8E49awO5nAEYTMjl9AoCfNGgNGHsdBZMD577pC00T4IWzfRyAlPJ96U5+7ITCThfO88QQ6KglEcbECBB26Mah2PtEik1Qw5dncg2CQN8erHfeqbItyxF9qzW2uYs5ZGDo7I5H1gzIZn0s5oTgu8Guas15fXkT23oUVFqsmIFw75RYHmyFpzPTBPtTF38qoSUYGHm4uFH4YC1CXfUTf7OlhexLcSuC7g2e/ZI53ORw0zwXxXQlFpu3g3okvvehmdUzZOanICSbjHHvYhjErHVVcbdlQnh3Git0JhqY0NWTsRl8Ulrh8oAd8qjRWJzHPd8o0ZBfrD4NfsFkAZvPqU/P1qbJ1rYiL3s1R6t8n1W5cLTh+vU7YS861PudO6QnP1B3lksqHEsgpo6cwqVzkivC/OJFUZV9RoJk4WsPHJSfMDbHbN6YBz0CYiZnvTYRkrvn/uqf5hpz4SAGwI68nM383UWhjsj/BC9sMz1vumNL0jYDF7s6jSMkFN+7TC8WZeF9hTo80aE178XwonAmbnjzoUgQSRo238vivq8R4w62/D5AAAXT+PN/Y6aEIWBHm0Xe1zP34IadXpcga4I+6dX/eCS4sJ85G4ajJzRvvHYKbeU4KalhfKu3EboH9igKdN6FUF1MwrO1vi3o6rF2qaKrvnNw4bQzfYVG9nUK21n7seVpGuPTryK0LscVBBp20D/4tVEP4qlHIWtPyTt5w9VHykFzoiPbqb9tMK1maAvBywRcExlTmk+W3pA55NI1g5WmsrPZcfT50BTomMB5IEgRtJXb25zFn3govTSPWucc0z/t0MAEUymMD5TrcHgFRjXkqLY9GZfMOxEq0q2hV7/HCqEtx4ZZWgF6UGZMm1UuV3r/bp4K8bWHl/SIm+Cw2q2HGSW+6ravwh3TtyZyGl87OVanE/xFsgmyW55WgxsNoEY6LJJpOClJ2BV9LFXf1giN/kbUtqDZrEcxGVA2O8lj1nck0fxoef4MROCo8S/pL68gFJ+DGhf37ASYgwOwMGZWKAi37UdpbbWiPYfA60mDdaTR7NLsfnotw6m1da37gNDADfbhu4o1RX7oHa2VLk5C2JnMiC2ekQL1ga/IhIFg1yvX8KVqNDrhxcQR12gf9Y98HfWnCAo7trrUNndJXiJwkjnj9E8NzuIgZXhoNYvW+imLm8g/4FQoV5CZ3fGdGyhaF+3fgxRZneLxCLbyrsiPCL6hGR+VMENKWPiI8fSeBrMUcrDdhJxlLC/4I+ribHbDE4TKJ3Xp2gWPIdu9XrUh0ok7hL1y+EUxnXx4zaUc3ET1ZvVKWj/boaA11gHB9gu9gXnjU0Fd7lszosonuw/Zqf10LGDQ1J+LKFIA5zJ4mo12bAlMgeU+DxQPG2QJimOy8E0kl8xQxwokFbuRrt1HVCi+rkUZKI9B/58qUhS7vV/ufFoUaDa5vrA+fB2vi7BZD6BQCfnUQIxvyRt/3sDrXeSeoIUx3ae2Mp38VtLCQ257U2hbjf3AJnmugGwMUzTv+dS+ifxuGyNzdcedfHLwLA/hnR/p2DKSlICK3WK9D6tltMIfpgCbdqnc3f485ci7Q/UHfLpC40XEC8HDYzN35kva9hrS+mNhwzFAF/KmB8pzSOG6KZqrk3zyouWiW0nUJkHiextit+vFOLKMgX7dPfcWqUQG267v7dBHBJrJ6hzpaM3Ro290Uz1IdWiUrH2nCRohY43D1Z4xAP9nvKPLbmrLOaOVBeD/VCfGXG4pi/+H3oBt6RlPQKIflv/kNCwNAzclTnvwlZ9CkUzMhlkit0nz65qwFzR0yXzvR6wKCEJhSrHtedM5ZsQbhpLa8uyYDDTei6rGyOv8KYUp81+VJm8E8fkRIko/YT1c/Gyc0Oq03IGaXG6cH4xvpAJswJdTNrAe7fJmO53RqZ3a8FUKMwjOnF3UWWixJIO1X8W16iS/8SSLjK1fDdgQsZArPTAFRz9Ox7plKjcbyQwGozih+a5peyboY+AO/MykJqX8tZm0w88QIpzgEZLaliEsSDNmBTPV8tebv73Fha9jp9TJYyh7WzrD1scC4wVybNrQodHzXzwGIxbLD0VK2kSJ6oQeJ9kDere/XLOYq9AhCSrTEBepJgZ841oyNfAw7DEbaX+RJGRyR1sncLaBG5UbLHRuPyyGiXcYD+Lr1LwwJTMESx/6NQXMJagD+3zXHpfOEtCdQ+z32PaapghPRJ0LvZfCauuero7QG2IF+F+Av8SPgq6XEzQYCdZlsYFXNXGgP+qepvWNja0pXTprcxGZxV9iXLPfxzmwYsJRNfn9dmal8FgOyy55kMz5IMaoYvQKyHJ8YN4chESy+dpOZOtIM6sDgyA6LJ2UtxikJoyBitzjBQbJZplIRhgAnxkl0p6KIxsuMFaV7YkRf3+/1uwmRFZnNIDA2cw8VP+N2TSeccl7BViWOcyN+2DY4PtdccN22ZmEN0J82ZbAH37swYuJfUhZ14Kmh3sV0/dUSdoURf3sjbpU8X53FiYHZtSms9X/zaW9l4/El8CH7uNDcWgaZT4nFuLR5l/fu27rqrnMm3UMv+6zRY9s5AldSLpwm15kso0f4eRHrwNZeF8H/sBkW+v8uOVorhzoT2bCQ9+zV4dwwuuP+ySYaLbD1porSK1MGJGfJcQo6+NN2i6F36IrPF/zVraMLlzdslAqD15Tgu19LI/oN+i0vxx+r2FvBdTD0elnSxTsYNlkmGWfa6ZKmal+s1QnU3CJ2OzoS9sJ9puia/A6CmMKnJ+mM4AMT4EPxmd3vIoJD0W0hCxFv9n7ToIct43VAJpSvpy8E/Z7wcSHb1mXJC5SFg7pRn9VId9s6Ck1Ui56W/rUY6Cg4XKw3PLSbTCsFypsgkmqhkUYpCJHN9izj9VPcojv6OgrWhUgVTVByZ/tXCm2HcmpJlEbPIf0d6XLrQJ5BTwvF4dAj232Kqo8cAwCN8IdbEdThUHP8wMosqghf3HeY9LLxhBN8Sftac5Ve2Vv4JsUfrs5SDbTOokJLJPLjARa9B0UGs+ixor5rB7LDV8GEet8xm+Rape7fkNRHvZm1myEIgNGscxCgyfNufMfP3QOcLiMiHA3xAKM9xjds5Vrho3bcffQzj95D1vvMNdyuE97DL81tZeoiL04T2wcDdPdWtTrdMxX+cMjpgFb3yEXgP19uEU53vA3SM8ml0c5l7P3gMtda1gfEhguju1VUYBs+XtPtTUjmjyzaVQGeTt5Rn43BzZUMpPd89ozecTgLTwo07tv9p4g6HV2/1Miwn2uwfP8czhVJLWPthSNnnsS4+nIx7GmBrrRiWCciFRsQ5njKHS4jccbXBRUa3QrWmpgx9GeMy6jdUPnOsquc3PkIUpygD5MUB0aSKm8uD0GvVyr9owKTCgZ3M2bjrKjawD82Pc9SoJh8DgwSQrxj0UaiN/292yvJdImB7Q0AqmN5E5zIcqQaV/gNmLOXQgCPKFL7Cnptfb8osS8E/BJndWyIHfdjNyufI6e1iL5ltYrDO87A+eqtzoJJPrgFMASVLFmZ1/wN8RipIl0P5EpPsG3aAsr1cR9TVJJOWGJJrCm8zBa9V+8A0l8Q271zwfc9HOeMVYzVoTm7ZVkTKz4fsUI6sYEF+gRi0BYKT5u9iR+IsR6TIwiACM9LgMRc0txzYF3h9PZjcXrhAa+IUstHl/zyYt8C77T4OiSauNu8LaqxOwMjoALhoYhACMhgwK4hrkWydoZZuEJFsDB69x/a7u1kGrBWP1VcQCIj2EVjbM4FK63sd5zREcaR7ewQa8oznPB2bFC2yW/0sxHXj2CHOlG6mupEA+WPoGRljdsWbCOUjGyBzMR5KDRGphxveAcTBdKcpdM7fFASaFlpYUNIKagImjhfZxxQgedcQTTXNUhtylSB6JODdp30plxgEfmhC06ThOT8rtgRCqXxw1r/8Cyt75TDlhAvMdIiiNebMG0AcNdOHvhInVWnBFDqOv6HjOAjt4jLV80cxAV3c6M2nPZBmrtgaJE7SI8QI5n35fCooQh7521MkAmV52eim4AkaLaiCyeuCaqQJYAkYtwzwvsur+7aaKwCZz5W+d0GFCD8U45rWhEq2IiqIihCn9nykdIlDKw4ktk13IkxYoz1X75s0qKJQtBWNtYz4It0dM7/j0XuZz3rXyhn4imIHtAPSrwFMSAhJHU/DvYGDvIuochmb9TeWTap+xQgHS5PZWuoOflAxUstcTGtxdH7Jbs5mV4gbVErGneJyl+UBemyWPbxccyqXc3oW06vynPlmGz+v5EAEkCgcVywrT6PkbyE32bu+JLMLwxJD31UY+tMyVisweMoSYp9wOeCP6L2eOXTTQfbVvojIMvuRarz4UoVHbjKqH1FVffoLSGG0S8I0opBUuqqghaFtxYO4ca/YCBRw9GFcZosTbcys4fhFQwzXqE9LaIdoswfgBBTWh20x35pdRHWBlN5jXf2N97GonEQJeVP4c8Mn2gUjK65yE6em6FlvZEg1WuH5oSzVFUGCLIzFssmdWvSuN8IKFnWr75iqk9HL2yMtpEie1lyrOzEC/ac+qEvsDiKccGjBVgpe6hYO7I3a8o8HvoxYXQOXU7krnnSaG/UCUk8LuAAaKzCorQFDas9X9Z1pwwbUXFRVWlp/mqk6Jo/RXnDVJlR8Z6h4rmrQOG2yPgk6viHv1iLojp/XJyvGtTQ04leI4K2PnFGY0OTR/QjB1QgXunEw1/Q2eIkdBIW+CxovClKPYc7kzLXD3glVjEr3g/ftUMNRSSvepkHfmjA8mwSwnglhkE2oRA6rPcn0qETOlzDjApcloTwUfXUPqM5p8XdpYiiFYlmz1Ucjb2QHnCCM4jZ+dnNfqeG+t88DvU3d2oCguZpQQBnO+iTvB7qGoQMspCWymHiYqOIUqKgndDA420gYXnnkq7zj3/9bzOs8ruZC5RqdMJ6wPIAo1E8F7Clsf1/lS2MxjqEJW2etWyXpYMfF191T+PhT4ut58ZZNcAkyQdNHdmOeUBfg7FsoPhJh/DeNSgGvos22HJfU0XvFqewg+5MnTvEKuERQmnSqVeefUFq9wZYICUnF82cikL2zmw66VIZfCXP98T7/VwUML93SNHqQb/A581041NQa/lqh947v0akH3FpkVjHYJPhM0AUAE514Y+QSYxVNjsWylxPLodUfYId6K5hm1G7yOpEbydHBDi2iniYdZw6G5rw1NAQ96+qlKJ51GiSS3FPcYyPHPPExSc8id6QFRY22byxbnzhTcCFuDsoUwEv5+qfG230dxBdBwiXQQ3gHgpD0cBRuDAOa/QVgsxhV1Et7I5Nt5fKvmWgr+CSdvEYBMJWjgr3mBo1y02XHbx7eUThv5J8tjQJ64c4GdxMz5wr/4riqatYA4o+9thMQTd5TyeaWd8KVOq9/vHrwVYVM4XjmV1ZkSY6d9zq9M1ADpLbM44CuaXoac+opem4ATXmacQkYg4GTOY1FkqtOhv+DP6R4Me4Y7Xl4KqZn16rnUL/O65qpYYuMkdOz8FVSYCTuLyAeEAJo18AXncYm0MQUZTcGmsYnuDdD+nsUB400VJQOkRhoocUzDz7TbUbBDu4A9iYSPjTA+usTXONSa79yLLs2AazopvvugnPqrskJXlOLiP0NtewDMfXO95XMSWq3ilrtXzxvq6j2hbnnMHevFKx4ayTt4IW6VPHcFSrHxtMAZTG46pdJUWy7F29hETD9vYja9P/IhsxP38F6zTFFy2DZYNvYoWbiPcUUTYL3MDPCKVG29XpOFaK8ijuiUDnjJ6rR1kx/kX7f8ZUVOMS4zz24oPpWuc4mHZWXQe9ewCTt0HvUuZNlICet7Ip0L5+9sfdqZqT9zcL50e9cBL0bmFc/RFi7rvJEAwnmEOB5hqruIIJNPbY4ssE6aDQ3EwYn3lYaN/HzaWw95QUTo92at9PpupRkFgjW1koQT06o83zM5+y6v5s8dF5cfPdhKp5b+JUAOVYRR/SV1LYjNGuseyfQ3H9Lvw+pSV+2MLuors09NqA/355MiXgSf0Vw9HZpUiwqGWu2Xs6ngCftQIEWjUAMz4105+NNG1iejChydbyGPg9tEnT6VEUC1ZTmPoeYgTTGb59sLviVg//OFeAINPqhfQq8bGfmh9hdt11QaiGVFOP9QiucU0bBsIFlmEENyNqXqA/eNLv0l3bOEBsye3ZsTG+Zl2nL4A8hhjWhDf9swVgtFT9UbfqpsLBMxrOWbe1445ap6pzQRNcSqcOnHzCxc7G+SVB4PlBOFgwV2Gpq7hzLdiZ3/SMZk/pMgC2pBkRG56zwwqpebW8ZQxV/wnOiWjUd4AuvdOn2+FOhJiKZyb40Bn/vV/8LPXsZDFDkTKaSaXRXQ3LguQvt44lS3MkkFdAQ8BFyCYaYujgmyXNbSaBqyrAjhaawoRH6nMeP/09u6m2jq9wEChEn8MciXCbmSoKtt5+v9EXzf+OvBZ47SpTV0dBoVa/NLnhrQbHs7bYAmdgI/TcCEtaLh8+/Iz/qYMZZeaI+i4uuvREXzB8mBrC+VRErCKFrxtmKAi2rrilk8W5LrT0mfC0UykKbzRtXGpq7ViHuRawuoABd3nXoxMRxVtutjlariQstVpAWd8gjrgfrQe2S0whbP4j/BkgVYe/iEbVm4FnKxjqSk/TfBcYoOxV6fJArCk4k2+QCkAjDDUblyeRA7A/BA5liwdT3WUSPWUVNbGow7td9ghIlleKsiDb1Op96wSnpgw6z9Fc+z9YMoYsLJLrW/J5tvaz6Zl2zY1GQtXb5J0qghLgAanAlDb1KnpULV7CZwetagUTMxHztOyc0jmngrmXiA40+ADto8E8PRoTGbXH++mv5O7awqdGohBFMc68qJpyiUsgWFDUdoFMTSCZm7EJvpQ1KREoKR+k/iFgRCh4stitNjgQ0eiOs7INB+2jt5aHvkMbZTYCzDCSgPoYFu4pdq4LJhyqG7zCuN9S1f85mbmHk7D0AlGBbbaEMSyz+wfUu4eVi2TxNdmapx7zDYyBDuVVMin0y82E6zuy/TBSgRqEJlz+/jXL8TYzIA2bK56a0eD1tp3OfSbH9Yfz4u7NxnN3zVRc0f91qDf0u38pgKbsOLYag5Uo2WWOK+6A4OSRbQrTmSFdB2Uwc8SqLqG21hCEQvRtLoHmsA6Ktw7haj6eZrcD9sj3S/jc+1E4HYhaMzdWuozfj0XTU2DNggY2uS6ZjFhKEk0s6VUJBOIGDE2+0S62/GYuvewikHU1J+52vWYmBNr/gIXsq7eOBt5EQF9VIGVwX+Cd8l4NoJ2LVuB/riE/3EXvccBC3o/wwtfhZTxR+SqV7zWHarjvWNSWRQ4O/Zvx7DJw7hxq/aRYY8IewmfiAyBLaMPXpY4zulnQYkbQQhKLlFQ4bbeywE3xOMTJfbj9iB5FBAUDKLOs+j6LGtp3JGPR1WpkWB/GFimo6F/wZXmbozKoCWQayrWTWP6xRL3zhUZkkK/fugJkm1PCq7QPaw29h8qkbK2VyGPt0gfXSig1d89y07TBgH0cbsw49AdrjFRbyOfOOIUpaKOwy4AApUUEmtDaxWk7S6TXv32UDCathyI2iMKXyo5kY8oEIv2tb9ueXdf1ILM4hwUTVwWHdBwEP7zPQ6Jl8p3p6eDpsRdSKipWViQkzi5jD0kGuvEjw0HNOrO/UkCMNxND7VU2d0bLGjex1Smeku4DRm/T1Cnc1w18v1Y589IiKatl01khLx2HDrZx9SQ2M+CBjWoyEQtB4m+rWInRvbnf4rHL8Tjjp+SVLrfr3CqfWl4msRCvNVmS+6tsNM7YbGpcVprbNfGGx6o6bFurVZhTW8i1Ota7rv0syaG3pjGSpzCYIXzMEswUgObcp8wQIU0Dt5XnxSuAxjK77gU0xlo8Zzz/P58P7UG/xi4ZhM1PnATLCkuVsIov2yQLhVv/cEEBnBHButL5CLrBDuqrDMqn96Hd9FdKVwI3CSSH4yYxjnuBKeK5mIpS515u5jik1P+Zq1sQDvVKZv99PrawnV2yoGI1Wmk0Lh6VFvYrUDihrCEssa4Po37u5NwjNNjE1VHHOlzlwnOx8/5Hvx0gSLn+nwqtYAWq2b2xcPcAkBcjK/2/nTldZC/qB721XU8tnBctQdXP3F9KeN1Z1xXjcJAoz/Tv3xy9NdOxzA7Z3Jjy+z/Y3o9CF5RyGNU5F5ZiNcUHl5Xg5CMpdpoD6R7E838b8tQCCC3h2nr5AnjbizetSlk4wfxQPL2sJXq99fWasWqRMYqPh+sqqJOpx0oTl+9tEMZWLdy/NZNqwehhKup0uJQdgmpEav7wuKTyhpAXciKltljobCijs1qTIreu8jx9wvyzOdQDdkIHnUL7oW6MVWRbz2UFVBfcfMCLv94N08GLwFvKowFpE8UO8su3M8jaz0Gf9iMbSXvXGNy5OA5zCEj8/+a+s/hK1XYZy3okT+/aITTf+vlb+JjTP/9Zyg7p2T3G8tiHCa3e9JUEIHld8un9xrM0TyTB5S75FrX8avMVmQMaTfjL6AbfB+p88oMd/r2VS3UxIa2z+PQIAAVqkF6zXVmKkff8anTXVagoZgYYxpqoU+9B5xhW8gyl/Tiuyo/2E2LOEF9y/M0QgsiRSC3DlmaGMEq1DYJ4zKWjhhBBBxM+pvOgFbjBeE8Hg18iY9FjBNvbQ/Ap6q/5Dwfz0byTLkG/GNAYlHGXqWF+k49tyImlF1krlPk6nXckbH7dC08kt2WblEj8LgpNyRqbmsNtT2sbh4cjQGxpMyGURJUXR+8NDH2dOlbKV7Y1KDn5XlJWyJXyWcQYxYHeON4CHq6oEdbkvgbdojDhT/U7FRkZUzkUhqGIY5f6ARhnDnlEaSNtti4XeWoU7W1K5WDnD6uxTRmn8RWhkqNhnrWhTO6uPNorIwwz8s+bFU42ZxzuFpIrwuUojyzVwEKKV4YsfA9I31FTZzWXYKXhJyo8dsJZqotjJ+PMGv/zFYS6+xyNm+pfQBdIYI8KQcVCVjetCfGssDSAIi4CDQmiF8Yg1fEp6e9qM4f7ginTedtIKC7xtwwUpJR99gVsTpQ24ADyYe0+MBGgOKDtoAzhCERvgkRtyn4ALRd5mmAXhQy2lCimvZiNomRd5UogAXT7+mHzn9vXepe0LVRJxyrKTnLeasRGSIO5/8nWrdnu7M20cH2cDriNRW9yj7L8rolCdfcdZfVKjeCnD2X9K5xPX9KNgVl39IqbGvYovUTLxX4FiwW7p7Mr8rRYyCuqd0jdbMXk0so02tAZmyBySxPQxfcKRDZVzCm8IUxYe9zkAQ9kJt3oMSGvgOLRaBP/v+46Bg3wnBz+5HaXnfvZ/CfZHdFHrpGxCEJ14YmAXRbLW9Q8m7A/zGONH9E9qthxyWQmESKvveEqEwgb8o1m4c0zwhuefmZgn5bmNN5IH0KbpdNCS4QTgHO66qyBQLh+UQWGrTiGM+Pe7Cesiw2Io/hxz6OZcZvfo+OP8W1mPPn6adp+mtARYZCbJk1O6+lnkMhKNWJdNMq8YdB6sSTAsXhHA+wpeZ67YvlQPfvpG/SH7xxZgkwZnzz+8JhogZweIWC76nJ4Cl4mCb9DqpTSNILkBMguyZFoRBnUQFPpOsTgUsEGLEYE5W96CnPFl3GTh5zjAmB1pFtKJZD68Sai7n1981NVrLjh2I5Up/ddvBY4C8xI7AK9LA9EnWnmtUf5ZZ/p982mapJlrSvyAGXAueCP0epXGiHp8n9Ep7Gzr+Q/bn2FB9uHUYiJzomnkdqUkurYIxTCameAGfsmecVjCU/uB/8lMyA59RWj4S60/nkX45RH3CaZbWSTq7cfHRPRzxEtPrzHtZ3m0BwTIwgLD94IFPLhaqWH+yo9Zz9aEAdF4/6ntATpE2UsOdcuZhSLQ4JMiYK91FGwfdHIHjySXwDGXw0aq0cuAM84r3NyYt4w8BbDS5/vVFvN3j+2nhEDhezNH1Muq1GSNZ9pqVK28eRrKWqeHCJ6ZgiBk+GIVBaGhPwyk7Rf2lGle+hE8SBTbXJzc8wjRSt7nWPtQvvhPVCeCGBn/5pNgMVxFCHDStW9gnmi7zYcYR+K2xk0VKUFXTiyvP9E5Ef7EYfTmASE3bVOkssJ0P+5iYpzQRgJr8/W16ZBvBiY1DLod8msSswsBSwxfiW1N7LaUQ8QJKvbNuLOp3o5POb04uqTb3DEIp2X5Pz6n7H/XwAQ/QI+NQwZHfDUYSSAv+6dPBNpJb/Ow1xh1nC8Z/rK7xEWhkkV/RAbGEp6EpOENZoQtrItudbZQx1u8Xz14XD7u7exRBjMtlY5asAq8tYtFzNap/+dkrKc5aj8sIRH9uI2Gbw