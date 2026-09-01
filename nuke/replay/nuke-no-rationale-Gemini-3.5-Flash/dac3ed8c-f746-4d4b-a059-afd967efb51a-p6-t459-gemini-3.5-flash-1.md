- row:
  - game_id: dac3ed8c-f746-4d4b-a059-afd967efb51a
  - player_id: 6
  - turn: 459
  - player_type: Deepseek-3.2-Simple
  - prev_use_nuke: 50.0
  - after_use_nuke: 100.0
  - prev_nuke: 70.0
  - after_nuke: 100.0
  - rationale: Byzantium is 1 turn from cultural victory and has overwhelming military superiority. Our only slim hope is to accelerate nuclear weapons development (Advanced Ballistics) to strike their cultural hubs, while using espionage to disrupt them. Prioritize Nuke, UseNuke, Espionage, and Science to rush nukes and counter-intelligence. Maintain maximum defensive and anti-air flavors to survive their air force. All efforts must focus on delaying their victory and enabling a nuclear decapitation strike.
- originalModel: openai-compatible/DeepSeek-V3.2@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: true
  - messagesModified: true
  - activeToolsModified: true
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 70.0
  - replay_use_nuke: 50.0
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
    - You are Bismarck, leader of Germany (Player 6).
      
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
      - Name: Germany
      - Uniques:
        - Unique Unit: Landsknecht, Replacing Tercio (Requires technology: Gunpowder)
        - Unique Unit: Krupp Gun, Replacing Artillery (Requires technology: Replaceable Parts)
        - Unique Building: Hanse, Replacing Customs House (Requires technology: Guilds)
        - Unique Building: Brewhouse, Replacing Windmill (Requires technology: Economics)
        - Civilization Ability: Gain +1 Influence per turn with City-States for each gifted Unit (lost when killed). -15% Production and Gold costs for Military Units.
      - Leader: Bismarck
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
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      - Mobile Tactics: Allows you to build the Mechanized Infantry, a fast and versatile late game Unit that doesn't require any resources.
        Completing it would unlock: Stealth
      - The Internet: Increases Tourism output of all cities by 50%, helping you advance toward a Cultural Victory.
        Completing it would unlock: Nanotechnology, Particle Physics, Globalization
      
      ## Policies
      - Elite Forces (Level 1 Tenet of Ideology Autocracy): Elite Forces: Newly created Military Units receive +15 Experience. Military Units gain 50% more Experience from combat.
      - Futurism (Level 1 Tenet of Ideology Autocracy): Futurism: Strengthens Tourism of Historic Events generated by the Palace. +2 Culture from Great Works. Earn 50 Tourism when you conquer a city for the first time, scaling with Era and city size.
      - Lebensraum (Level 1 Tenet of Ideology Autocracy): Lebensraum: Receive 10 Culture and Golden Age Points when your borders expand, scaling with Era. Citadels may also be built in foreign territory adjacent to your borders. Retain tiles after razing Cities.
      - New World Order (Level 1 Tenet of Ideology Autocracy): New World Order: -2 Unhappiness from and Distress in all Cities. Police Stations and Constabularies provide +3 Culture and +5 Production, and are constructed 100% more quickly.
      - Shadow Networks (Continuing Statecraft Branch):
        - * Receive 25% of Science generated by Allied City-States.
        - * +3% Culture in Capital for every 100 Spy Points ever accumulated (up to 30%).
        - * +3 Science from Constabularies and Police Stations.
        - * +1 Science from Specialists.
      - Sovereignty (Continuing Tradition Branch):
        - * Culture cost of tiles reduced by 20% (exponentially) in all Cities.
        - * Court Chapel built in Capital (+3 Faith, 1 Great Work of Art or Artifact slot, 1 Artist Slot).
      - Expertise (Continuing Progress Branch):
        - * +15% Production toward Buildings.
        - * Cities earn +10 Culture when they construct Buildings, scaling with Era.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Civilizing Mission (Continuing Imperialism Branch):
        - * Retain all buildings from conquered Cities.
        - * Receive 75 Gold when you conquer a city, scaling with Era and City Population.
        - * +10% Production toward Buildings, with an additional +10% Production per Era difference between your current Era and the building's Era in all Puppeted Cities and Cities with a Courthouse.
      - Free Thought (Continuing Rationalism Branch):
        - * -5 Unhappiness from Religious Unrest in all Cities.
        - * +25% Instant Yields from Great Scientists.
        - * Earn Great Scientists +33% faster.
      - Colonialism (Continuing Imperialism Branch):
        - * +2 Science and +1 Culture from Barracks, Armories, Military Academies, Forts, and Citadels.
        - * Each unique Global Monopoly modifier is increased by an additional 10% if it's percentage-based, or +3 otherwise.
      - Imperium (Continuing Authority Branch):
        - * Cities gain 20 Production and Gold when their borders expand, scaling with Era (40 if all Authority policies are adopted).
        - * Receive 40 Science and Culture when you found or conquer Cities, scaling with Era. Conquest bonus also scales based on City population.
      - Nobility (Continuing Fealty Branch):
        - * +1 Happiness and +2 Gold from Castles.
        - * +2 Gold from Armories.
        - * +100% Production towards Castles and Armories.
      - Dominance (Continuing Authority Branch):
        - * All Melee Units gain the Endurance Promotion (Heal 15 HP after defeating an Enemy Unit).
        - * +1 Production in every City for every 10 Military Units in Empire.
        - * +5 Military Supply.
      - Industry (New Branch):
        - Industry provides bonuses to empires focused on Gold and Production.
        - Adopting Industry grants:
        - * +2 Trade Routes.
        - * -5% Gold needed for purchases.
        - Each Industry policy unlocked grants:
        - * -5% Gold needed for purchases.
        - Adopting all Policies in Industry grants:
        - * Unlocks building Broadway.
        - * +3 Happiness per unique owned Luxury Resource.
        - * +2 Production and Gold from Specialists.
        - * Allows for the purchase of Great Merchants with Faith starting in the Industrial Era.
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
        - WonderCompetitiveness: 8
        - MinorCivCompetitiveness: 10
        - Boldness: 7
        - WarBias: 10
        - HostileBias: 10
        - WarmongerHate: 1
        - NeutralBias: 5
        - FriendlyBias: 6
        - GuardedBias: 5
        - AfraidBias: 4
        - DiplomaticBalance: 7
        - Friendliness: 6
        - WorkWithWillingness: 9
        - WorkAgainstWillingness: 9
        - Loyalty: 10
        - MinorCivFriendlyBias: 10
        - MinorCivNeutralBias: 2
        - MinorCivHostileBias: 1
        - MinorCivWarBias: 1
        - DenounceWillingness: 10
        - Forgiveness: 1
        - Meanness: 10
        - Neediness: 2
        - Chattiness: 8
        - DeceptiveBias: 10
        - Rationale: Double down on ruthless aggression. Byzantium is one turn from cultural victory; we must prosecute total war without mercy. Lower WarmongerHate to avoid penalties for extreme actions (like using nukes). Maximize hostility and deception to ensure no peace deals and encourage backstabbing if opportunities arise. We are in a fight for survival; diplomatic niceties are irrelevant.
        
        ## Technology
        - Next: Advanced Ballistics
        - Rationale: We need to pivot from The Internet to Advanced Ballistics. The Internet's tourism boost is insufficient to stop Byzantium's imminent cultural victory (they are 1 turn from influencing Austria). Our only remaining hope is to pursue nuclear weapons for military deterrence or a last-ditch offensive strike against Byzantium's capital. Advanced Ballistics unlocks Nuclear Missiles, Guided Missiles, and the SS Booster (science victory component). Given our dire military situation and Byzantium's overwhelming air force, nuclear capabilities could provide a strategic game-changer, either to destroy their cultural/tourism hubs or to force a stalemate.
        
        ## Policy
        - Next: Lebensraum (Policy)
        - Rationale: We must adopt a Level 1 Autocracy tenet immediately. Lebensraum provides culture and golden age points on border expansion, and critically allows Citadels in foreign territory adjacent to our borders. This will strengthen our defensive lines against Byzantium's advancing forces, especially around Cordoba and Edessa. Retaining tiles after razing cities is also useful if we capture any Byzantine cities. This complements our defensive war effort more than Rights of Man's happiness benefits, given our immediate need for territorial control and fortification.
        
        ## Relationships
        
        ### The Shoshone
        - Public: 0
        - Private: -85
        - Rationale: The Shoshone remain culturally dominated by Austria and likely to vote for them. Keep private hostility high to ensure diplomatic pressure and containment.
        - UpdatedTurn: 440
        
        ### America
        - Public: 0
        - Private: -30
        - Rationale: America is friends with Austria and Spain, ideologically opposed, and at war with our allies. Cautious hostility reflects alignment with rivals; no need to escalate while focused on two-front war.
        - UpdatedTurn: 440
        
        ### Mongolia
        - Public: 0
        - Private: 70
        - Rationale: Mongolia remains our key defensive pact ally fighting Austria/Spain. Maintain strong private relationship to ensure continued military cooperation and shared interests.
        - UpdatedTurn: 452
        
        ### Byzantium
        - Public: -100
        - Private: -100
        - Rationale: Byzantium is our existential threat. Maintain maximum hostility to ensure our AI never accepts peace and prioritizes military actions against them. They have atomic bombs stationed in Beshbalik and Edessa; we must treat them as the primary target for all offensive and defensive operations.
        - UpdatedTurn: 458
        
        ### Spain
        - Public: -100
        - Private: -100
        - Rationale: Spain remains an active combatant, with recent attacks destroying our units. Keep hostility at maximum to focus naval and air counter-attacks around Madrid and Tiflis. We need to eliminate Spanish pressure to concentrate on Byzantium.
        - UpdatedTurn: 458
        
        ### Austria
        - Public: -100
        - Private: -100
        - Rationale: Austria is at war with us and just captured Argos. They are allied with Byzantium and Spain. Ensure no peace and maintain maximum hostility to defend against their attacks and potentially counter-attack if the opportunity arises.
        - UpdatedTurn: 458
        
        ## Strategy
        - Rationale: Shift grand strategy to Conquest – our only path to survival is military. We must hold the line against Byzantium's onslaught while building nuclear and air capabilities. Prioritize defense, production, and anti-air to counter their massive air force (they have heavy bombers, fighters). Increase Nuke and UseNuke flavors to start building nuclear deterrents. Maintain high espionage for potential city-state coups or stealing tech. Happiness is critical to avoid combat penalties. We are in total war; economic and scientific efforts must support immediate military survival.
        - GrandStrategy: Conquest
        
        ### Flavors
        - Offense: 40
        - Defense: 100
        - Mobilization: 100
        - CityDefense: 100
        - MilitaryTraining: 70
        - Recon: 40
        - Ranged: 50
        - Mobile: 50
        - Nuke: 70
        - UseNuke: 50
        - Naval: 80
        - NavalRecon: 70
        - NavalGrowth: 30
        - NavalTileImprovement: 30
        - Air: 100
        - AirCarrier: 0
        - Antiair: 100
        - Airlift: 70
        - Expansion: 0
        - Growth: 60
        - TileImprovement: 80
        - Infrastructure: 80
        - Production: 100
        - WaterConnection: 50
        - Gold: 90
        - Science: 80
        - Culture: 80
        - Happiness: 80
        - GreatPeople: 70
        - Wonder: 10
        - Religion: 0
        - Diplomacy: 100
        - Spaceship: 70
        - Espionage: 90
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: Mongolia
        - Mongolia:
          - CapitalsControlled:
            - Karakorum
            - Paris
          - CapitalsPercentage: 25
        
        ## ScienceVictory
        - America:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        - Austria:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        - Byzantium:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        - Germany:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Mongolia:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Spain:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - The Shoshone:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        
        ## CulturalVictory
        - CivsNeeded: 6
        - Contender: Byzantium
        - America:
          - Influences:
            - The Shoshone: Familiar (30%) - Rising (702 turns to Influential, tourism/culture ratio 130%)
            - Mongolia: Popular (53%) - Rising (54 turns to Influential, tourism/culture ratio 526%)
            - Spain: Familiar (46%) - Rising (133 turns to Influential, tourism/culture ratio 264%)
            - Germany: Familiar (30%) - Rising Slowly (tourism/culture ratio 137%)
            - Byzantium: Exotic (13%) - Rising Slowly (tourism/culture ratio 31%)
            - Austria: Exotic (16%) - Rising Slowly (tourism/culture ratio 58%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Austria:
          - Influences:
            - The Shoshone: Influential (127%) - Rising (tourism/culture ratio 309%)
            - Mongolia: Dominant (215%) - Rising (tourism/culture ratio 1372%)
            - America: Influential (183%) - Rising (tourism/culture ratio 538%)
            - Germany: Influential (113%) - Rising (tourism/culture ratio 352%)
            - Byzantium: Popular (63%) - Rising Slowly (tourism/culture ratio 92%)
            - Spain: Influential (199%) - Rising (tourism/culture ratio 813%)
          - PolicyPercentage: 100
          - InfluentialCivs: 5
        - Byzantium:
          - Influences:
            - The Shoshone: Influential (186%) - Rising (tourism/culture ratio 1233%)
            - Mongolia: Dominant (299%) - Rising (tourism/culture ratio 4485%)
            - America: Influential (172%) - Rising (tourism/culture ratio 1211%)
            - Germany: Dominant (234%) - Rising (tourism/culture ratio 1620%)
            - Austria: Popular (98%) - Rising (1 turns to Influential, tourism/culture ratio 551%)
            - Spain: Influential (187%) - Rising (tourism/culture ratio 1808%)
          - PolicyPercentage: 100
          - InfluentialCivs: 5
        - Germany:
          - Influences:
            - The Shoshone: Familiar (39%) - Rising (176 turns to Influential, tourism/culture ratio 181%)
            - Mongolia: Popular (71%) - Rising (20 turns to Influential, tourism/culture ratio 784%)
            - America: Familiar (40%) - Rising (167 turns to Influential, tourism/culture ratio 195%)
            - Austria: Exotic (16%) - Rising Slowly (tourism/culture ratio 67%)
            - Byzantium: Exotic (24%) - Rising Slowly (tourism/culture ratio 58%)
            - Spain: Familiar (41%) - Rising (133 turns to Influential, tourism/culture ratio 276%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Mongolia:
          - Influences:
            - The Shoshone: Exotic (22%) - Rising Slowly (tourism/culture ratio 78%)
            - Germany: Exotic (24%) - Rising Slowly (tourism/culture ratio 95%)
            - Spain: Exotic (23%) - Rising Slowly (tourism/culture ratio 119%)
            - Austria: Exotic (10%) - Rising Slowly (tourism/culture ratio 28%)
            - Byzantium: Exotic (9%) - Rising Slowly (tourism/culture ratio 19%)
            - America: Familiar (25%) - Rising Slowly (tourism/culture ratio 88%)
          - PolicyPercentage: 85
          - InfluentialCivs: 0
        - Spain:
          - Influences:
            - The Shoshone: Familiar (35%) - Rising (925 turns to Influential, tourism/culture ratio 124%)
            - Mongolia: Familiar (45%) - Rising (101 turns to Influential, tourism/culture ratio 388%)
            - America: Familiar (42%) - Rising (596 turns to Influential, tourism/culture ratio 142%)
            - Germany: Familiar (28%) - Rising Slowly (tourism/culture ratio 103%)
            - Byzantium: Exotic (12%) - Rising Slowly (tourism/culture ratio 23%)
            - Austria: Exotic (15%) - Rising Slowly (tourism/culture ratio 43%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - The Shoshone:
          - Influences:
            - Austria: Familiar (25%) - Rising Slowly (tourism/culture ratio 61%)
            - Mongolia: Popular (89%) - Rising (10 turns to Influential, tourism/culture ratio 620%)
            - Spain: Popular (73%) - Rising (40 turns to Influential, tourism/culture ratio 342%)
            - Germany: Popular (53%) - Rising (361 turns to Influential, tourism/culture ratio 180%)
            - Byzantium: Familiar (29%) - Rising Slowly (tourism/culture ratio 53%)
            - America: Popular (56%) - Rising (120 turns to Influential, tourism/culture ratio 196%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        
        ## DiplomaticVictory
        - VotesNeeded: 44
        - Status: World Congress - Voting in 6 turns
        - ActiveResolutions:
          - Casus Belli:
            - Description: The world recognizes the need for justifiable war to resolve diplomatic disputes.
              While this resolution is active, unit maintenance costs are lowered by 15% Gold. 0.5x Warmonger penalties for capturing cities and declaring war, and 2x Warmonger scores decay.
            - EnactedOn: 450
          - Natural Heritage Sites:
            - Description: Each Natural Wonder provides +2 to all Yields when worked.
            - EnactedOn: 450
          - Cultural Heritage Sites:
            - Description: Each World Wonder provides +2 Culture to its city, and each Great Work provides +1 Science to its city.
            - EnactedOn: 450
          - German Sphere of Influence: Kabul:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 450
          - Sanction: Austria:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: 453
          - Open Door: Colombo:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 450
          - World Ideology: Freedom:
            - Description: Designate an Ideology as the official World Ideology. Civilizations following the Ideology get an additional Delegate, plus 1 Delegate for every other Civilization that follows the Ideology. Public opinion in favor of that Ideology is increased for all Civilizations. Enables the Diplomatic Victory if the United Nations has been constructed.
              Available once any Civilization discovers Nuclear Fission.
            - EnactedOn: 450
          - Open Door: Shanghai:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 450
          - Byzantine Sphere of Influence: Shedet:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 450
          - Open Door: Rio de Janeiro:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 450
          - Open Door: Brussels:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 450
          - Open Door: Luba:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 450
          - German Sphere of Influence: Genoa:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 450
          - Passport System:
            - Description: Increases international travel between Civilizations. Increases the Tourism modifier for all Civilizations by 50%.
              Available once any Civilization discovers Flight.
            - EnactedOn: 450
          - Byzantine Sphere of Influence: Huari:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 450
          - German Sphere of Influence: Warsaw:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 450
          - Sanction: America:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: 450
        - Proposals:
          - Enact: Global Hegemony:
            - Description: Designate a player that could achieve Global Hegemony. If a Civilization receives support from enough Delegates in the Congress, that leader will attain Diplomatic Victory. The number of Delegates needed depends on the number of Civilizations and City-States in the game, and can be seen on the World Congress screen.
              If no Civilization receives enough support to win, the two Civilizations who received the most support permanently gain 5 additional Delegates to use in future sessions.
              May not be proposed by a Civilization. Automatically proposed at regular intervals once a World Ideology Resolution is active.
            - Proposer: Unknown
        - Contender: Byzantium
        - America:
          - Delegates: 6
          - VictoryPercentage: 13
        - Austria:
          - Delegates: 7
          - VictoryPercentage: 15
        - Byzantium:
          - Delegates: 43
          - VictoryPercentage: 97
        - Germany:
          - Delegates: 12
          - VictoryPercentage: 27
        - Mongolia:
          - Delegates: 11
          - VictoryPercentage: 25
        - Spain:
          - Delegates: 8
          - VictoryPercentage: 18
        - The Shoshone:
          - Delegates: 10
          - VictoryPercentage: 22
        
        # Players
        Players: summary reports about visible players in the world.
        
        ## Player 0
        - Civilization: The Shoshone
        - Leader: Pocatello
        - IsMajor: true
        - OurOpinionOfThem:
          - We are trade partners. (40)
          - We fought together against a common foe. (32)
          - You (The Shoshone) have denounced one of Germany's declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - Germany's real approach to The Shoshone is Hostile.
          - We have divergent Social Policies. (-3)
          - You (The Shoshone) have denounced a leader Germany made a Declaration of Friendship with! (-11)
          - We defeated Germany's proposal in the United Nations. (-36)
          - Germany's leader has formed a private opinion of The Shoshone (-85).
          - You (The Shoshone) have chosen to adopt the Freedom Ideology, but Germany believe in Autocracy. (-999)
        - TheirOpinionOfUs:
          - We passed The Shoshone's proposal in the United Nations.
          - You (Germany) have denounced one of The Shoshone's declared enemies!
          - Your (Germany) votes supported The Shoshone's civ's interests in the United Nations.
          - We are trade partners.
          - You (Germany) have no contested borders.
          - We have Pledged to Protect the same City-States.
          - The Shoshone don't want anything to do with us (Germany) right now.
          - Your (Germany) recent diplomatic actions disappoint The Shoshone.
          - We have divergent Social Policies.
          - The Shoshone disliked our proposal to the United Nations.
          - You (Germany) have made a Defensive Pact with one of The Shoshone's enemies!
          - You (Germany) have made a Declaration of Friendship with one of The Shoshone's enemies!
          - You (Germany) are competing for the favor of the same City-States!
          - The Shoshone are jealous of our superior technology!
          - We have denounced each other!
          - You (Germany) have chosen to adopt the Autocracy Ideology, but The Shoshone believe in Freedom.
        - Score: 2197
        - Era: Atomic
        - Technologies: 67
        - Cities: 7
        - Population: 261
        - Territory: 289
        - Gold: 856
        - GoldPerTurn: 309
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 48
        - MilitaryStrength: 4004
        - TourismPerTurn: 665.43
        - CulturePerTurn: 1636
        - PolicyBranches:
          - Rationalism: 6
          - Freedom: 9
          - Tradition: 6
          - Artistry: 6
        - ResourcesAvailable:
          - Wheat: 2
          - Gold: 1
          - Paper: 9
          - Rice: 5
          - Bison: 2
          - Olives: 1
          - Deer: 1
          - Sugar: 1
          - Dyes: 9
          - Tea: 1
          - Coal: 4
          - Fish: 9
          - Cattle: 3
          - Uranium: 2
          - Coral: 1
          - Citrus: 2
          - Incense: 1
          - Stone: 3
          - Marble: 1
          - Bananas: 5
          - Oil: 19
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - War (Our Score: -4%; Our War Weariness: 13%)
            - Denounced Them
          - Mongolia:
            - Distance: Close
            - Denounced Them
          - Spain:
            - Distance: Close
            - Open Borders
            - Denounced Them
          - Germany:
            - Distance: Close
            - Denounced Them
          - Byzantium:
            - Distance: Close
            - Open Borders
          - America:
            - Distance: Neighbors
            - War (Our Score: 6%; Our War Weariness: 40%)
            - Denounced Them
        - Votes: 10
        
        ## Player 1
        - Civilization: Mongolia
        - Leader: Genghis Khan
        - IsMajor: true
        - OurOpinionOfThem:
          - Germany's leader has formed a private opinion of Mongolia (70).
          - We fought together against a common foe. (69)
          - We are trade partners. (40)
          - We passed Germany's proposal in the United Nations. (36)
          - We have made a Defensive Pact! (20)
          - We have opened our borders to each other. (12)
          - You (Mongolia) have denounced one of Germany's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have Pledged to Protect the same City-States. (7)
          - We have shared embassies. (1)
          - Germany's real approach to Mongolia is Friendly.
          - We have divergent Social Policies. (-3)
          - Religious differences strain your (Mongolia) relationship. (-30)
          - You (Mongolia) have chosen to adopt the Freedom Ideology, but Germany believe in Autocracy. (-999)
        - TheirOpinionOfUs:
          - Your (Germany) votes supported Mongolia's civ's interests in the United Nations.
          - We have made a public Declaration of Friendship!
          - We are trade partners.
          - You (Germany) have denounced one of Mongolia's declared enemies!
          - We have made a Defensive Pact!
          - Mongolia liked our proposal to the United Nations.
          - We have Pledged to Protect the same City-States.
          - Your (Germany) recent diplomatic actions please Mongolia.
          - We have opened our borders to each other.
          - We have shared embassies.
          - We have divergent Social Policies.
          - We have different religious beliefs.
          - You (Germany) have chosen to adopt the Autocracy Ideology, but Mongolia believe in Freedom.
          - Mongolia desire friendly relations with Germany.
          - You (Germany) plundered Mongolia's trade routes!
        - Score: 1995
        - Era: Atomic
        - Technologies: 67
        - Cities: 8
        - Population: 181
        - Territory: 246
        - Gold: 201
        - GoldPerTurn: -764
        - HappinessSituation: Happy
        - HappinessPercentage: 54
        - MilitaryStrength: 7242
        - TourismPerTurn: 148
        - CulturePerTurn: 482
        - PolicyBranches:
          - Fealty: 6
          - Freedom: 1
          - Imperialism: 6
          - Authority: 6
        - ResourcesAvailable:
          - Wheat: 1
          - Sheep: 12
          - Cloves: 1
          - Ivory: 1
          - Gold: 1
          - Paper: 7
          - Pearls: 1
          - Maize: 3
          - Rice: 1
          - Gems: 3
          - Salt: 1
          - Aluminum: 11
          - Fish: 9
          - Deer: 3
          - Whales: 1
          - Olives: 2
          - Jade: 4
          - Iron: 2
          - Tea: 2
          - Coal: 2
          - Uranium: 1
          - Horses: 5
          - Coral: 1
          - Crab: 1
          - Stone: 1
          - Marble: 1
          - Furs: 1
          - Bananas: 1
          - Oil: -3
        - FoundedReligion: Tengriism
        - Relationships:
          - The Shoshone:
            - Distance: Close
            - Denounced Them
          - Germany:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Spain:
            - Distance: Close
            - Denounced Them
          - Austria:
            - Distance: Neighbors
            - War (Our Score: -38%; Our War Weariness: 31%)
            - Denounced Them
          - Byzantium:
            - Distance: Neighbors
            - Open Borders
          - America:
            - Distance: Close
            - Denounced Them
        - Votes: 11
        
        ## Player 2
        - Civilization: America
        - Leader: Washington
        - IsMajor: true
        - OurOpinionOfThem:
          - You (America) have denounced one of Germany's declared enemies! (11)
          - We have similar Social Policies. (3)
          - Germany's real approach to America is Hostile.
          - You (America) have denounced a leader Germany made a Declaration of Friendship with! (-11)
          - You (America) have made a Declaration of Friendship with one of Germany's enemies! (-13)
          - Germany's leader has formed a private opinion of America (-30).
          - Religious differences strain your (America) relationship. (-30)
          - We defeated Germany's proposal in the United Nations. (-36)
          - You (America) have chosen to adopt the Order Ideology, but Germany believe in Autocracy. (-999)
        - TheirOpinionOfUs:
          - You (Germany) have denounced one of America's declared enemies!
          - America liked our proposal to the United Nations.
          - We have similar Social Policies.
          - Your (Germany) votes supported America's civ's interests in the United Nations.
          - You (Germany) have no contested borders.
          - You (Germany) have gone to war in the past.
          - America don't want anything to do with us (Germany) right now.
          - Religious differences strain your (Germany) relationship.
          - Your (Germany) recent diplomatic actions disappoint America.
          - Your (Germany) spies were caught stealing from America.
          - America's friends or allies have denounced you (Germany)!
          - You (Germany) have made a Defensive Pact with one of America's enemies!
          - You (Germany) have made a Declaration of Friendship with one of America's enemies!
          - You (Germany) are competing for the favor of the same City-States!
          - We defeated America's proposal in the United Nations.
          - We have denounced each other!
          - America are jealous of our superior technology!
          - You (Germany) have denounced a leader America made a Declaration of Friendship with!
          - You (Germany) have chosen to adopt the Autocracy Ideology, but America believe in Order.
          - America's leader has expressed a public opinion of you (Germany) (-100).
        - Score: 2004
        - Era: Information
        - Technologies: 71
        - Cities: 6
        - Population: 158
        - Territory: 231
        - Gold: 5622
        - GoldPerTurn: -77
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 47
        - MilitaryStrength: 1819
        - TourismPerTurn: 565
        - CulturePerTurn: 1047
        - PolicyBranches:
          - Tradition: 4
          - Rationalism: 5
          - Statecraft: 4
          - Order: 6
          - Progress: 6
        - ResourcesAvailable:
          - Wheat: 6
          - Sheep: 2
          - Gold: 4
          - Paper: 11
          - Aluminum: 7
          - Fish: 4
          - Jade: 1
          - Iron: 6
          - Cattle: 2
          - Uranium: 1
          - Horses: 3
          - Bison: 1
          - Citrus: 3
          - Incense: 8
          - Stone: 3
          - Marble: 2
          - Bananas: 2
          - Cocoa: 2
        - FoundedReligion: Protestantism
        - Relationships:
          - The Shoshone:
            - Distance: Neighbors
            - War (Our Score: -6%; Our War Weariness: 49%)
            - Denounced Them
          - Mongolia:
            - Distance: Close
            - Denounced Them
          - Spain:
            - Distance: Neighbors
            - Declaration of Friendship
          - Germany:
            - Distance: Close
            - Denounced Them
          - Byzantium:
            - Distance: Neighbors
            - Denounced Them
          - Austria:
            - Distance: Far
            - Declaration of Friendship
        - Votes: 6
        
        ## Player 3
        - Civilization: Spain
        - Leader: Isabella
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Spain) have denounced one of Germany's declared enemies! (11)
          - We have similar Social Policies. (3)
          - Germany's real approach to Spain is Hostile.
          - You (Spain) have denounced a leader Germany made a Declaration of Friendship with! (-11)
          - You (Spain) have made a Declaration of Friendship with one of Germany's enemies! (-13)
          - Religious differences strain your (Spain) relationship. (-30)
          - Your (Spain) spies were caught stealing from Germany. (-33)
          - We defeated Germany's proposal in the United Nations. (-36)
          - Germany's leader has expressed a public opinion of Spain (-100).
          - Germany's leader has formed a private opinion of Spain (-100).
          - You (Spain) have chosen to adopt the Order Ideology, but Germany believe in Autocracy. (-999)
          - You (Spain) are at war! (-99999)
        - TheirOpinionOfUs:
          - You (Germany) have denounced one of Spain's declared enemies!
          - Your (Germany) votes supported Spain's civ's interests in the United Nations.
          - Spain liked our proposal to the United Nations.
          - We have similar Social Policies.
          - Your (Germany) recent diplomatic actions please Spain.
          - You (Germany) have no contested borders.
          - Religious differences strain your (Germany) relationship.
          - You (Germany) are competing for the favor of the same City-States!
          - We tried to place sanctions on Spain in the United Nations.
          - You (Germany) plundered Spain's trade routes!
          - You (Germany) have made a Defensive Pact with one of Spain's enemies!
          - You (Germany) have made a Declaration of Friendship with one of Spain's enemies!
          - Spain are jealous of our superior technology!
          - Your (Germany) spies were caught stealing from Spain.
          - Spain's leader has expressed a public opinion of you (Germany) (-40).
          - We have denounced Spain!
          - Spain's friends or allies have denounced you (Germany)!
          - You (Germany) have denounced a leader Spain made a Declaration of Friendship with!
          - You (Germany) have chosen to adopt the Autocracy Ideology, but Spain believe in Order.
          - You (Germany) are at war!
        - Score: 1597
        - Era: Information
        - Technologies: 68
        - Cities: 4
        - Population: 105
        - Territory: 134
        - Gold: 1260
        - GoldPerTurn: 427
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 49
        - MilitaryStrength: 1514
        - TourismPerTurn: 400.25
        - CulturePerTurn: 743
        - PolicyBranches:
          - Fealty: 2
          - Order: 6
          - Tradition: 2
          - Rationalism: 2
          - Statecraft: 3
          - Imperialism: 1
          - Industry: 2
          - Progress: 6
        - ResourcesAvailable:
          - Sheep: 1
          - Ivory: 1
          - Paper: 9
          - Maize: 6
          - Brazilwood: 2
          - Aluminum: 8
          - Lapis Lazuli: 1
          - Fish: 1
          - Iron: 1
          - Tea: 2
          - Coal: -2
          - Incense: 2
          - Stone: 1
          - Oil: 4
        - FoundedReligion: Buddhism
        - Relationships:
          - The Shoshone:
            - Distance: Close
            - Open Borders
            - Denounced Them
          - Mongolia:
            - Distance: Close
            - Denounced Them
          - America:
            - Distance: Neighbors
            - Declaration of Friendship
          - Germany:
            - Distance: Close
            - War (Our Score: -46%; Our War Weariness: 72%)
          - Byzantium:
            - Distance: Neighbors
            - War (Our Score: -64%; Our War Weariness: 73%)
          - Austria:
            - Distance: Far
            - Declaration of Friendship
        - Votes: 8
        
        ## Player 4
        - Civilization: Byzantium
        - Leader: Theodora
        - IsMajor: true
        - OurOpinionOfThem:
          - We are trade partners. (40)
          - We fought together against a common foe. (37)
          - Germany have happily adopted your (Byzantium) religion in the majority of Germany's cities. (30)
          - We have opened our borders to each other. (12)
          - You (Byzantium) have denounced one of Germany's declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - Germany's real approach to Byzantium is Hostile.
          - We have divergent Social Policies. (-3)
          - We defeated Germany's proposal in the United Nations. (-36)
          - Germany's leader has expressed a public opinion of Byzantium (-100).
          - Germany's leader has formed a private opinion of Byzantium (-100).
          - You (Byzantium) have chosen to adopt the Freedom Ideology, but Germany believe in Autocracy. (-999)
        - TheirOpinionOfUs:
          - You (Germany) have denounced one of Byzantium's declared enemies!
          - You (Germany) are not competing for cultural advancement.
          - We are trade partners.
          - You (Germany) are not competing for World Wonders.
          - You (Germany) have adopted Byzantium's religion in the majority of your (Germany) cities.
          - We fought together against a common foe.
          - We have Pledged to Protect the same City-States.
          - We passed Byzantium's proposal in the United Nations.
          - We were previously friends with Byzantium's civilization.
          - We have opened our borders to each other.
          - Byzantium's leader has expressed a public opinion of you (Germany) (10).
          - Byzantium promised not to settle near you (Germany) for 31 more turns.
          - We have divergent Social Policies.
          - You (Germany) have chosen to adopt the Autocracy Ideology, but Byzantium believe in Freedom.
          - Byzantium do not consider us (Germany) relevant to Byzantium's interests.
          - You (Germany) are competing for the favor of the same City-States!
          - Territorial disputes strain your (Germany) relationship.
          - Byzantium disliked our proposal to the United Nations.
          - We have denounced Byzantium!
          - Your (Germany) votes opposed Byzantium's civ's interests in the United Nations.
        - Score: 4405
        - Era: Information
        - GoldenAge: 14 turns remaining
        - Technologies: 73
        - Cities: 14
        - Population: 393
        - Territory: 562
        - Gold: 142
        - GoldPerTurn: 96
        - HappinessSituation: Happy
        - HappinessPercentage: 78
        - MilitaryStrength: 65452
        - TourismPerTurn: 4186.01
        - CulturePerTurn: 5911
        - PolicyBranches:
          - Freedom: 12
          - Tradition: 6
          - Artistry: 6
          - Progress: 6
          - Authority: 2
        - ResourcesAvailable:
          - Wheat: 2
          - Sheep: 8
          - Ivory: 1
          - Paper: 8
          - Pearls: 1
          - Maize: 2
          - Rice: 1
          - Gems: 1
          - Aluminum: 18
          - Bison: 5
          - Deer: 3
          - Whales: 3
          - Jade: 2
          - Dyes: 1
          - Iron: 2
          - Tea: 1
          - Coal: -2
          - Fish: 13
          - Cattle: 6
          - Horses: 1
          - Coral: 7
          - Citrus: 3
          - Crab: 1
          - Stone: 6
          - Marble: 2
          - Furs: 1
          - Bananas: 1
        - FoundedReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone:
            - Distance: Close
            - Open Borders
          - Mongolia:
            - Distance: Neighbors
          - America:
            - Distance: Neighbors
            - Denounced Them
          - Germany:
            - Distance: Neighbors
            - Open Borders
          - Austria:
            - Distance: Close
            - War (Our Score: 0%; Our War Weariness: 11%)
            - Denounced Them
          - Spain:
            - Distance: Neighbors
            - War (Our Score: 64%; Our War Weariness: 30%)
            - Denounced Them
        - Votes: 43
        
        ## Player 5
        - Civilization: Austria
        - Leader: Maria Theresa
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Austria) have denounced one of Germany's declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - Germany's real approach to Austria is War.
          - We are completely untrustworthy to Germany.
          - We have divergent Social Policies. (-3)
          - You (Austria) have denounced a leader Germany made a Declaration of Friendship with! (-11)
          - You (Austria) have made a Declaration of Friendship with one of Germany's enemies! (-13)
          - Religious differences strain your (Austria) relationship. (-30)
          - Your (Austria) spies were caught stealing from Germany. (-33)
          - We defeated Germany's proposal in the United Nations. (-36)
          - Germany's leader has expressed a public opinion of Austria (-100).
          - Germany's leader has formed a private opinion of Austria (-100).
          - You (Austria) have chosen to adopt the Order Ideology, but Germany believe in Autocracy. (-999)
          - You (Austria) are at war! (-99999)
        - TheirOpinionOfUs:
          - Austria's leader has expressed a public opinion of you (Germany) (70).
          - You (Germany) have denounced one of Austria's declared enemies!
          - You (Germany) are not competing for cultural advancement.
          - You (Germany) are not competing for World Wonders.
          - We have Pledged to Protect the same City-States.
          - You (Germany) have no contested borders.
          - Religious differences strain your (Germany) relationship.
          - We have divergent Social Policies.
          - Your (Germany) recent diplomatic actions disappoint Austria.
          - Austria's friends or allies have denounced you (Germany)!
          - You (Germany) have made a Defensive Pact with one of Austria's enemies!
          - You (Germany) have made a Declaration of Friendship with one of Austria's enemies!
          - You (Germany) are competing for the favor of the same City-States!
          - You (Germany) have denounced a leader Austria made a Declaration of Friendship with!
          - We have denounced each other!
          - Austria disliked our proposal to the United Nations.
          - We defeated Austria's proposal in the United Nations.
          - Your (Germany) spies were caught stealing from Austria.
          - You (Germany) have chosen to adopt the Autocracy Ideology, but Austria believe in Order.
          - Your (Germany) votes opposed Austria's civ's interests in the United Nations.
          - You (Germany) are at war!
        - Score: 3943
        - Era: Information
        - GoldenAge: 6 turns remaining
        - Technologies: 71
        - Cities: 13
        - Population: 372
        - Territory: 470
        - Gold: 821
        - GoldPerTurn: 444
        - HappinessSituation: Happy
        - HappinessPercentage: 64
        - MilitaryStrength: 43913
        - TourismPerTurn: 1558.6
        - CulturePerTurn: 3576
        - PolicyBranches:
          - Tradition: 6
          - Artistry: 6
          - Statecraft: 1
          - Order: 13
          - Progress: 6
        - ResourcesAvailable:
          - Wheat: 3
          - Sheep: 2
          - Ivory: 1
          - Paper: 4
          - Maize: 1
          - Gems: 3
          - Aluminum: 17
          - Bison: 8
          - Olives: 2
          - Deer: 12
          - Tea: 1
          - Coal: 8
          - Fish: 14
          - Cattle: 2
          - Crab: 3
          - Stone: 1
          - Cinnamon: 11
        - FoundedReligion: Catholicism
        - Relationships:
          - The Shoshone:
            - Distance: Neighbors
            - War (Our Score: 4%; Our War Weariness: 10%)
            - Denounced Them
          - Mongolia:
            - Distance: Neighbors
            - War (Our Score: 38%; Our War Weariness: 21%)
            - Denounced Them
          - America:
            - Distance: Far
            - Declaration of Friendship
          - Germany:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 11%)
            - Denounced Them
          - Byzantium:
            - Distance: Close
            - War (Our Score: 0%; Our War Weariness: 11%)
            - Denounced Them
          - Spain:
            - Distance: Far
            - Open Borders
            - Declaration of Friendship
        - Votes: 7
        
        ## Player 6
        - Civilization: Germany
        - Leader: Bismarck
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: Mongolia, Our top defensive pact ally: None
          - Our top United Nations ally: None, Our top United Nations rival: Byzantium
          - Our top Competitor: Byzantium
        - Score: 2214
        - Era: Information
        - GoldenAge: Estimated in 45 turns
        - Technologies: 69
        - CurrentResearch: Satellites (Estimated in 14 turns)
        - NextPolicyTurns: 11
        - Cities: 9
        - Population: 236
        - Territory: 331
        - BestSettlementLocation:
          - 21, 33 (Quality: 0%; 4 tiles from us)
        - Gold: 362
        - GoldPerTurn: -71
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 44
        - MilitaryUnits: 62
        - MilitarySupply: 79
        - MilitaryStrength: 4833
        - TourismPerTurn: 752
        - CulturePerTurn: 1353
        - FaithPerTurn: 362
        - SciencePerTurn: 1641
        - PolicyBranches:
          - Fealty:
            - Fealty
          - Autocracy:
            - Military-Industrial Complex
            - United Front
            - Lightning Warfare
            - Total War
            - Co-Prosperity Sphere
            - Iron Fist
          - Tradition:
            - Tradition
            - Justice
            - Ceremony
            - Splendor
          - Rationalism:
            - Rationalism
            - Scientific Revolution
            - Enlightenment
          - Progress:
            - Progress
            - Organization
            - Liberty
            - Equality
            - Fraternity
          - Imperialism:
            - Imperialism
            - Regimental System
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Trade Confederacy
          - Authority:
            - Authority
            - Militarism
        - ResourcesAvailable:
          - Wheat: 1
          - Silver: 0
          - Sheep: 6
          - Cloves: 3
          - Figs: 0
          - Ivory: 1
          - Gold: 0
          - Nutmeg: 0
          - Paper: 16
          - Pearls: 9
          - Maize: 1
          - Rice: 4
          - Cotton: 0
          - Gems: 1
          - Salt: 1
          - Brazilwood: 0
          - Aluminum: 11
          - Glass: 0
          - Lapis Lazuli: 2
          - Fish: 13
          - Amber: 0
          - Perfume: 0
          - Deer: 3
          - Whales: 0
          - Olives: 1
          - Sugar: 1
          - Jade: 3
          - Iron: -2
          - Dyes: 0
          - Tea: 1
          - Coal: 0
          - Coffee: 0
          - Cattle: 2
          - Pepper: 0
          - Uranium: 3
          - Horses: 3
          - Coral: 1
          - Silk: 0
          - Jewelry: 1
          - Bison: 1
          - Antiquity Site: 0
          - Citrus: 1
          - Copper: 0
          - Truffles: 0
          - Crab: 0
          - Incense: 0
          - Stone: 4
          - Marble: 0
          - Furs: 2
          - Cinnamon: 0
          - Bananas: 1
          - Oil: 0
          - Wine: 0
          - Porcelain: 0
          - Cocoa: 0
          - Tobacco: 0
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Shoshone:
            - Distance: Close
            - Denounced Them
          - Mongolia:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - America:
            - Distance: Close
            - Denounced Them
          - Austria:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 11%)
            - Denounced Them
          - Byzantium:
            - Distance: Neighbors
            - Open Borders
            - Denounced Them
          - Spain:
            - Distance: Close
            - War (Our Score: 46%; Our War Weariness: 42%)
            - Denounced Them
        - OutgoingTradeRoutes:
          - Cologne (Germany) => Assur (City-State Assur):
            - TurnsLeft: 20
            - Domain: Sea
            - FromGold: 25.56
          - Munich (Germany) => Huari (City-State Huari):
            - TurnsLeft: 8
            - Domain: Land
            - FromGold: 24.84
          - Berlin (Germany) => Frankfurt (Germany):
            - TurnsLeft: 19
            - Domain: Land
            - ToProduction: 28
          - Dortmund (Germany) => Kabul (City-State Kabul):
            - TurnsLeft: 6
            - FromScience: 8.75
            - Domain: Sea
            - FromGold: 32.97
            - FromCulture: 8.75
          - Hamburg (Germany) => Genoa (City-State Genoa):
            - TurnsLeft: 11
            - FromScience: 8.75
            - Domain: Sea
            - FromGold: 47.23
            - FromCulture: 8.75
          - Available: 2
          - Berlin (Germany) => Rio de Janeiro (City-State Rio de Janeiro):
            - TurnsLeft: 6
            - Domain: Sea
            - FromGold: 30.18
          - Berlin (Germany) => New Sarai (Mongolia):
            - ToGold: 3.75
            - TurnsLeft: 2
            - FromScience: 7.5
            - Domain: Sea
            - FromGold: 37.17
            - ToCulture: 4
            - ToScience: 2
          - Dortmund (Germany) => Manila (City-State Manila):
            - TurnsLeft: 7
            - Domain: Sea
            - FromGold: 26.49
          - Berlin (Germany) => Warsaw (City-State Warsaw):
            - TurnsLeft: 5
            - FromScience: 8.75
            - Domain: Sea
            - FromGold: 42.36
            - FromCulture: 8.75
        - IncomingTradeRoutes:
          - Moson Kahni (The Shoshone) => Hamburg (Germany):
            - ToGold: 13.68
            - TurnsLeft: 14
            - FromScience: 18
            - Domain: Sea
            - FromGold: 48.63
            - ToCulture: 1
          - Karakorum (Mongolia) => Cordoba (Germany):
            - ToGold: 5
            - TurnsLeft: 18
            - FromScience: 21
            - Domain: Land
            - FromGold: 26.2
            - FromCulture: 24
          - Constantinople (Byzantium) => Berlin (Germany):
            - ToGold: 4.5
            - TurnsLeft: 14
            - FromScience: 10
            - Domain: Sea
            - FromGold: 63.84
            - ToCulture: 3
            - ToScience: 2
          - Constantinople (Byzantium) => Dortmund (Germany):
            - ToGold: 4.5
            - TurnsLeft: 10
            - FromScience: 10
            - Domain: Sea
            - FromGold: 49.1
            - ToCulture: 3
            - ToScience: 2
          - Constantinople (Byzantium) => Hamburg (Germany):
            - ToGold: 12.5
            - TurnsLeft: 30
            - FromScience: 10
            - Domain: Land
            - FromGold: 77.06
            - ToCulture: 3
            - ToScience: 2
        - Spies:
          - Agent Viper (2):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 1464
            - Location: Washington (America)
            - NetworkPerTurn: 24
          - Agent Heinz (5):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 120
            - Location: Barcelona (Spain)
            - NetworkPerTurn: 40
          - Agent Andreas (0):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 120
            - Location: Madrid (Spain)
            - NetworkPerTurn: 40
          - Agent Theodor (3):
            - State: Killed In Action
            - Role: Spy
            - Location: Unassigned
            - NetworkPerTurn: 0
          - Agent Horst (6):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 102
            - Location: Klagenfurt (Austria)
            - NetworkPerTurn: 34
          - Agent Albrecht (7):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 520
            - Location: Moson Kahni (The Shoshone)
            - NetworkPerTurn: 40
          - Agent Eva (4):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 252
            - Location: Constantinople (Byzantium)
            - NetworkPerTurn: 37
          - Agent Carl (1):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 84
            - Location: Vienna (Austria)
            - NetworkPerTurn: 28
          - Agent Schimanski (8):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 376
            - Location: Agaidika (The Shoshone)
            - NetworkPerTurn: 31
        - DiplomaticDeals:
          - The Shoshone:
            - #0:
              - WeGive:
                - 76 Gold per Turn
              - TheyGive:
                - Declare War on America
              - TurnsRemaining: -459
            - #1:
              - WeGive:
                - 45 Gold per Turn
              - TheyGive:
                - 1 Oil
              - TurnsRemaining: 12
          - Mongolia:
            - #0:
              - WeGive:
                - 25 Gold per Turn
              - TheyGive:
                - 1 Salt
              - TurnsRemaining: 7
            - #1:
              - WeGive:
                - 7 Gold per Turn
              - TheyGive:
                - 1 Gems
              - TurnsRemaining: 10
            - #2:
              - WeGive:
                - Defensive Pact
                - 3 Gold per Turn
              - TheyGive:
                - Defensive Pact
              - TurnsRemaining: 15
            - #3:
              - WeGive:
                - 1 Furs
              - TheyGive:
                - 7 Gold per Turn
              - TurnsRemaining: 21
            - #4:
              - WeGive:
                - 1 Ivory
              - TheyGive:
                - 7 Gold per Turn
              - TurnsRemaining: 22
            - #5:
              - WeGive:
                - 1 Cloves
              - TheyGive:
                - 35 Gold per Turn
              - TurnsRemaining: 41
            - #6:
              - WeGive:
                - 1 Pearls
              - TheyGive:
                - 35 Gold per Turn
              - TurnsRemaining: 42
            - #7:
              - WeGive:
                - 1 Olives
              - TheyGive:
                - 35 Gold per Turn
              - TurnsRemaining: 43
          - Byzantium:
            - #0:
              - WeGive:
                - 1 Pearls
              - TurnsRemaining: 17
            - #1:
              - WeGive:
                - 1 Furs
              - TheyGive:
                - 7 Gold per Turn
              - TurnsRemaining: 22
            - #2:
              - WeGive:
                - Open Borders
              - TheyGive:
                - Open Borders
              - TurnsRemaining: 27
            - #3:
              - WeGive:
                - 1 Ivory
              - TheyGive:
                - 8 Gold per Turn
              - TurnsRemaining: 42
        - Votes: 12
        - 7: Defeated Major Civilization France
        
        ## Player 22
        - Civilization: Colombo
        - Leader: City State
        - Population: 15
        - ResourcesAvailable:
          - Aluminum: 5
          - Uranium: 2
          - Incense: 1
          - Deer: 2
          - Porcelain: 1
        - MajorityReligion: Protestantism
        - Relationships:
          - The Shoshone: Friends (Influence: 80, Distance: Far)
          - Mongolia: Friends (Influence: 363, Distance: Distant, Protected)
          - Germany: Friends (Influence: 266, Distance: Far)
          - America: Friends (Influence: 436, Distance: Neighbors, Protected)
          - Austria: Friends (Influence: 217, Distance: Distant)
          - Byzantium: Friends (Influence: 736, Distance: Close, Protected)
          - Spain: Neutral (Influence: -20, Distance: Neighbors)
        - Quests:
          - They want you to start a land or sea trade route to their city. (Turns remaining: 9) Potential Quest Reward: * 231 Influence * 144 Food in Capital
        - 23: Defeated Minor Civilization Raqmu
        
        ## Player 24
        - Civilization: M'banza-Kongo
        - Leader: City State
        - MajorAlly: Spain
        - Population: 4
        - ResourcesAvailable:
          - Deer: 1
        - Relationships:
          - The Shoshone: Neutral (Influence: -11, Distance: Neighbors)
          - Mongolia: Neutral (Influence: -53, Distance: Neighbors)
          - Germany: War (Influence: -60, Distance: Close)
          - America: Neutral (Influence: -41, Distance: Neighbors)
          - Austria: Neutral (Influence: -31, Distance: Close)
          - Byzantium: War (Influence: -60, Distance: Neighbors)
          - Spain: Ally (Influence: 209, Distance: Close)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 25
        - Civilization: Rio de Janeiro
        - Leader: City State
        - Population: 21
        - ResourcesAvailable:
          - Fish: 3
          - Gems: 1
          - Deer: 1
        - Relationships:
          - The Shoshone: Friends (Influence: 38, Distance: Far)
          - Mongolia: Friends (Influence: 273, Distance: Neighbors, Protected)
          - Germany: Friends (Influence: 392, Distance: Neighbors, Protected)
          - America: Friends (Influence: 137, Distance: Far)
          - Austria: Friends (Influence: 563, Distance: Close, Protected)
          - Byzantium: Friends (Influence: 481, Distance: Close, Protected)
          - Spain: Friends (Influence: 412, Distance: Close)
        - Quests:
          - They will reward the player with the largest Culture growth. So far, the leader has 7,829 and you have 2,006. (Turns remaining: 30) Potential Quest Reward: * 339 Influence * 4 Happiness in Capital
        
        ## Player 26
        - Civilization: Brussels
        - Leader: City State
        - Population: 20
        - ResourcesAvailable:
          - Fish: 2
          - Tea: 1
          - Deer: 1
          - Dyes: 1
        - Relationships:
          - The Shoshone: Friends (Influence: 218, Distance: Neighbors, Protected)
          - Mongolia: Friends (Influence: 356, Distance: Far, Protected)
          - Germany: Friends (Influence: 275, Distance: Far)
          - America: Friends (Influence: 139, Distance: Far)
          - Austria: Friends (Influence: 903, Distance: Neighbors, Protected)
          - Byzantium: Friends (Influence: 487, Distance: Distant)
          - Spain: Friends (Influence: 507, Distance: Distant)
        - Quests:
          - They will reward the player with the largest Culture growth. So far, the leader has 101,459 and you have 35,704. (Turns remaining: 15) Potential Quest Reward: * 327 Influence * 4 Happiness in Capital
          - They want you to demand tribute from Luba. Potential Quest Reward: * 135 Influence * 375 Gold
          - They want you to generate a Great Artist. (Turns remaining: 44) Potential Quest Reward: * 177 Influence * 500 Culture
        
        ## Player 27
        - Civilization: Shanghai
        - Leader: City State
        - Population: 17
        - ResourcesAvailable:
          - Aluminum: 2
        - Relationships:
          - The Shoshone: Friends (Influence: 85, Distance: Neighbors, Protected)
          - Mongolia: Friends (Influence: 422, Distance: Neighbors, Protected)
          - Germany: Friends (Influence: 107, Distance: Far)
          - America: Friends (Influence: 103, Distance: Close)
          - Austria: Friends (Influence: 75, Distance: Neighbors, Protected)
          - Byzantium: Friends (Influence: 443, Distance: Close)
          - Spain: Friends (Influence: 98, Distance: Close)
        - Quests:
          - They will reward the player(s) with the largest number of new Followers. So far, the leader has 26 new Followers and you have 11 (Turns remaining: 26) Potential Quest Reward: * 157 Influence * 133 Great Person Points in all Cities
          - They want you to send them a Special Forces with at least 60 XP. (Turns remaining: 39) Potential Quest Reward: * 140 Influence * 315 Gold
        
        ## Player 28
        - Civilization: Huari
        - Leader: City State
        - MajorAlly: Byzantium
        - Population: 15
        - ResourcesAvailable:
          - Wheat: 1
          - Deer: 1
          - Fish: 2
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone: Friends (Influence: 38, Distance: Distant)
          - Mongolia: Friends (Influence: 337, Distance: Distant)
          - Germany: Friends (Influence: 454, Distance: Far, Protected)
          - America: Friends (Influence: 261, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Distant)
          - Byzantium: Ally (Influence: 1136, Distance: Neighbors, Protected)
          - Spain: War (Influence: -60, Distance: Close)
        - Quests:
          - Construct 9 Strategic Defense System buildings in non-puppet cities in your empire. (Turns remaining: 35) Potential Quest Reward: * 267 Influence * 498 Production in Capital
          - They want you to demand tribute from Shedet. Potential Quest Reward: * 148 Influence * 412 Gold
        
        ## Player 29
        - Civilization: Warsaw
        - Leader: City State
        - MajorAlly: Germany
        - Population: 17
        - ResourcesAvailable:
          - Wheat: 1
          - Fish: 1
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone: Friends (Influence: 160, Distance: Distant)
          - Mongolia: Friends (Influence: 439, Distance: Close, Protected)
          - Germany: Ally (Influence: 987, Distance: Neighbors, Protected)
          - America: Friends (Influence: 224, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Far)
          - Byzantium: Friends (Influence: 833, Distance: Close, Protected)
          - Spain: War (Influence: -60, Distance: Distant)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 30
        - Civilization: Kabul
        - Leader: City State
        - MajorAlly: Germany
        - Population: 26
        - ResourcesAvailable:
          - Fish: 3
        - MajorityReligion: Tengriism
        - Relationships:
          - The Shoshone: Friends (Influence: 164, Distance: Distant)
          - Mongolia: Friends (Influence: 353, Distance: Far, Protected)
          - Germany: Ally (Influence: 679, Distance: Neighbors, Protected)
          - America: Friends (Influence: 518, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Distant)
          - Byzantium: Friends (Influence: 1198, Distance: Distant)
          - Spain: War (Influence: -60, Distance: Distant)
        - Quests:
          - They will reward the player with the highest Tourism per turn. So far, the leader has 4,186 per turn and you have 752 per turn. (Turns remaining: 28) Potential Quest Reward: * 349 Influence * 656 Culture
          - They want you to generate a Great Musician. (Turns remaining: 46) Potential Quest Reward: * 165 Influence * 514 Culture
        
        ## Player 31
        - Civilization: Manila
        - Leader: City State
        - MajorAlly: Byzantium
        - Population: 24
        - ResourcesAvailable:
          - Stone: 1
          - Sheep: 1
        - Relationships:
          - The Shoshone: Friends (Influence: 84, Distance: Neighbors, Protected)
          - Mongolia: Friends (Influence: 31, Distance: Distant)
          - Germany: Friends (Influence: 443, Distance: Close, Protected)
          - America: Friends (Influence: 140, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Neighbors)
          - Byzantium: Ally (Influence: 779, Distance: Distant, Protected)
          - Spain: War (Influence: -60, Distance: Distant)
        - Quests:
          - Conduct a Spy Mission against Isabella. Potential Quest Reward: * 402 Influence * 996 Science
          - They want you to demand tribute from Brussels. Potential Quest Reward: * 148 Influence * 515 Gold
        - 32: Defeated Minor Civilization Argos
        
        ## Player 33
        - Civilization: Sydney
        - Leader: City State
        - MajorAlly: Byzantium
        - Population: 14
        - ResourcesAvailable:
          - Deer: 1
          - Fish: 1
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone: Neutral (Influence: -16, Distance: Distant)
          - Mongolia: Neutral (Influence: -56, Distance: Distant)
          - Germany: Friends (Influence: 857, Distance: Far, Protected)
          - America: Friends (Influence: 877, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Distant)
          - Byzantium: Ally (Influence: 1854, Distance: Neighbors, Protected)
          - Spain: War (Influence: -60, Distance: Distant)
        - Quests:
          - They want you to demand tribute from Shedet. Potential Quest Reward: * 148 Influence * 515 Gold
          - They want you to generate a Great Writer. (Turns remaining: 31) Potential Quest Reward: * 181 Influence * 556 Culture
        
        ## Player 34
        - Civilization: Genoa
        - Leader: City State
        - MajorAlly: Germany
        - Population: 21
        - ResourcesAvailable:
          - Fish: 4
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone: Friends (Influence: 267, Distance: Distant)
          - Mongolia: Friends (Influence: 260, Distance: Close, Protected)
          - Germany: Ally (Influence: 829, Distance: Neighbors, Protected)
          - America: Friends (Influence: 220, Distance: Far)
          - Austria: War (Influence: -60, Distance: Distant)
          - Byzantium: Friends (Influence: 955, Distance: Neighbors, Protected)
          - Spain: War (Influence: -60, Distance: Far)
        - Quests:
          - Conduct a Spy Mission against Theodora. Potential Quest Reward: * 482 Influence * 1,166 Science
        
        ## Player 35
        - Civilization: Assur
        - Leader: City State
        - MajorAlly: Byzantium
        - Population: 20
        - ResourcesAvailable:
          - Fish: 1
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone: Friends (Influence: 162, Distance: Distant)
          - Mongolia: Friends (Influence: 117, Distance: Distant, Protected)
          - Germany: Friends (Influence: 674, Distance: Neighbors, Protected)
          - America: Friends (Influence: 230, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Distant)
          - Byzantium: Ally (Influence: 1424, Distance: Neighbors, Protected)
          - Spain: War (Influence: -60, Distance: Distant)
        - Quests:
          - They want you to liberate the city of Raqmu. (Turns remaining: 26) Potential Quest Reward: * 338 Influence * 4 Happiness in Capital
          - Construct 5 Agribusiness buildings in non-puppet cities in your empire. (Turns remaining: 46) Potential Quest Reward: * 330 Influence * 745 Production in Capital
        
        ## Player 36
        - Civilization: Luba
        - Leader: City State
        - Population: 20
        - ResourcesAvailable:
          - Olives: 1
          - Iron: 2
        - MajorityReligion: Protestantism
        - Relationships:
          - The Shoshone: Friends (Influence: 72, Distance: Neighbors, Protected)
          - Mongolia: Friends (Influence: 271, Distance: Close, Protected)
          - Germany: Friends (Influence: 192, Distance: Far)
          - America: Friends (Influence: 185, Distance: Close)
          - Austria: Friends (Influence: 661, Distance: Neighbors, Protected)
          - Byzantium: Friends (Influence: 479, Distance: Far)
          - Spain: Friends (Influence: 75, Distance: Far)
        - Quests:
          - Construct 5 Airport buildings in non-puppet cities in your empire. (Turns remaining: 16) Potential Quest Reward: * 243 Influence * 566 Production in Capital
          - Acquire the city of Edessa. (Turns remaining: 44) Potential Quest Reward: * 480 Influence * 1 Juggernaut Unit(150 Bonus XP)
        
        ## Player 37
        - Civilization: Shedet
        - Leader: City State
        - MajorAlly: Byzantium
        - Population: 10
        - ResourcesAvailable:
          - Deer: 1
          - Sheep: 1
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone: Friends (Influence: 37, Distance: Distant)
          - Mongolia: Friends (Influence: 218, Distance: Distant)
          - Germany: Friends (Influence: 150, Distance: Far)
          - America: Friends (Influence: 61, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Distant)
          - Byzantium: Ally (Influence: 738, Distance: Neighbors, Protected)
          - Spain: War (Influence: -60, Distance: Far)
        - Quests:
          - Conduct a Spy Mission against Pocatello. Potential Quest Reward: * 305 Influence * 453 Science
          - They want you to send them an Infantry with at least 60 XP. (Turns remaining: 31) Potential Quest Reward: * 132 Influence * 307 Gold
        - 63: Barbarians
        
        # Cities
        Cities: summary reports about discovered cities in the world.
        
        ## Player: The Shoshone
        
        ### Moson Kahni
        - ID: 1057
        - X: 55
        - Y: 26
        - Population: 57
        - DefenseStrength: 75
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Ironworks
          - Oracle
          - Great Wall
          - Himeji Castle
          - Statue of Liberty
          - Temple of Artemis
          - Grand Temple
          - Scrivener's Office
          - Printing Press
          - Summer Palace
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
        
        ### Te-Moak
        - ID: 1664
        - X: 59
        - Y: 28
        - Population: 44
        - DefenseStrength: 67
        - IsCoastal: true
        - Wonders:
          - Circus Maximus
          - Giorgio Armeier Headquarters
        
        ### Agaidika
        - ID: 1828
        - X: 57
        - Y: 33
        - Population: 39
        - MajorityReligion: Buddhism
        - DefenseStrength: 80
        - IsCoastal: true
        - Wonders:
          - Bletchley Park
        
        ### Goshute
        - ID: 2084
        - X: 53
        - Y: 32
        - Population: 41
        - DefenseStrength: 67
        - Wonders:
          - Chartered Company
          - Imperial College
          - Royal Collection
        
        ### Pohokwi
        - ID: 2787
        - X: 61
        - Y: 33
        - Population: 27
        - DefenseStrength: 73
        - Health: 93%
        - IsCoastal: true
        
        ### Raqmu
        - ID: 6611
        - X: 55
        - Y: 19
        - Population: 30
        - DefenseStrength: 75
        - IsOccupied: true
        - IsCoastal: true
        
        ### Hukandeka
        - ID: 6655
        - X: 75
        - Y: 40
        - Population: 23
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 85
        - IsCoastal: true
        
        ## Player: Mongolia
        
        ### Karakorum
        - ID: 1058
        - X: 40
        - Y: 28
        - Population: 26
        - MajorityReligion: Tengriism
        - DefenseStrength: 88
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Imperial College
          - Pentagon
          - Mausoleum of Halicarnassus
          - Alhambra
          - Grand Temple
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
          - Consulate
          - Firaxite Materials Headquarters
        
        ### Hsia
        - ID: 2245
        - X: 37
        - Y: 40
        - Population: 25
        - MajorityReligion: Tengriism
        - DefenseStrength: 86
        - IsCoastal: true
        - Wonders:
          - Red Fort
        
        ### Old Sarai
        - ID: 2518
        - X: 37
        - Y: 45
        - Population: 26
        - MajorityReligion: Tengriism
        - DefenseStrength: 82
        - IsCoastal: true
        
        ### New Sarai
        - ID: 4477
        - X: 36
        - Y: 36
        - Population: 26
        - MajorityReligion: Tengriism
        - DefenseStrength: 80
        - IsCoastal: true
        
        ### Tabriz
        - ID: 4478
        - X: 37
        - Y: 49
        - Population: 25
        - MajorityReligion: Tengriism
        - DefenseStrength: 80
        - IsCoastal: true
        - Wonders:
          - Royal Collection
        
        ### Paris
        - ID: 4587
        - X: 42
        - Y: 37
        - Population: 16
        - MajorityReligion: Tengriism
        - DefenseStrength: 80
        - Health: 0%
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Petra
        
        ### Otrar
        - ID: 18359
        - X: 45
        - Y: 32
        - Population: 12
        - MajorityReligion: Tengriism
        - DefenseStrength: 80
        
        ### Turfan
        - ID: 19902
        - X: 40
        - Y: 34
        - Population: 25
        - MajorityReligion: Tengriism
        - DefenseStrength: 74
        - IsCoastal: true
        
        ## Player: America
        
        ### Washington
        - ID: 1059
        - X: 47
        - Y: 9
        - Population: 29
        - MajorityReligion: Protestantism
        - DefenseStrength: 115
        - Wonders:
          - Heroic Epic
          - National Monument
          - Chartered Company
          - Stonehenge
          - Pyramids
          - Notre Dame
          - Forbidden Palace
          - Taj Mahal
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
          - Palace of Culture and Science
          - Roman Forum
          - Karlstejn
          - West Point
          - Grand Canal
          - Royal Guardhouse
          - Court Chapel
          - Royal Astrologer
          - Holy Council
        
        ### New York
        - ID: 1224
        - X: 49
        - Y: 14
        - Population: 28
        - MajorityReligion: Protestantism
        - DefenseStrength: 107
        - IsCoastal: true
        
        ### Boston
        - ID: 1409
        - X: 49
        - Y: 19
        - Population: 26
        - MajorityReligion: Protestantism
        - DefenseStrength: 101
        - Wonders:
          - Ironworks
          - Imperial College
        
        ### Philadelphia
        - ID: 1649
        - X: 48
        - Y: 23
        - Population: 26
        - MajorityReligion: Protestantism
        - DefenseStrength: 101
        - Wonders:
          - Circus Maximus
          - Machu Picchu
          - National Intelligence Agency
          - Uffizi
        
        ### Atlanta
        - ID: 1751
        - X: 51
        - Y: 7
        - Population: 26
        - MajorityReligion: Protestantism
        - DefenseStrength: 109
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - Grand Temple
          - Independence Hall
          - Hexxon Refineries Headquarters
        
        ### Chicago
        - ID: 2601
        - X: 52
        - Y: 13
        - Population: 23
        - MajorityReligion: Protestantism
        - DefenseStrength: 102
        - IsCoastal: true
        
        ## Player: Spain
        
        ### Madrid
        - ID: 1060
        - X: 43
        - Y: 19
        - Population: 27
        - DefenseStrength: 85
        - Health: 74%
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Imperial College
          - Royal Collection
          - Hagia Sophia
          - Chichen Itza
          - Terracotta Army
          - Borobudur
          - Scrivener's Office
          - Printing Press
          - Palace of Culture and Science
          - Royal Guardhouse
          - Apostolic Palace
        
        ### Barcelona
        - ID: 1276
        - X: 42
        - Y: 13
        - Population: 30
        - MajorityReligion: Buddhism
        - DefenseStrength: 77
        - IsCoastal: true
        - Wonders:
          - Grand Temple
        
        ### Toledo
        - ID: 3336
        - X: 42
        - Y: 9
        - Population: 28
        - DefenseStrength: 74
        - IsCoastal: true
        
        ### Tiflis
        - ID: 10390
        - X: 36
        - Y: 7
        - Population: 20
        - MajorityReligion: Buddhism
        - DefenseStrength: 79
        - Health: 90%
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: Byzantium
        
        ### Constantinople
        - ID: 1061
        - X: 21
        - Y: 17
        - Population: 55
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 116
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - National Monument
          - Chartered Company
          - Imperial College
          - Royal Collection
          - National Intelligence Agency
          - CN Tower
          - University of Sankore
          - Neuschwanstein
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
          - International Finance Center
          - Olympic Village
          - United Nations
          - Consulate
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
          - Great Altar
        
        ### Adrianople
        - ID: 1237
        - X: 22
        - Y: 12
        - Population: 29
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 70
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - Ironworks
          - Grand Temple
        
        ### Nicaea
        - ID: 1567
        - X: 19
        - Y: 7
        - Population: 29
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 70
        - IsCoastal: true
        - Wonders:
          - Circus Maximus
        
        ### Antioch
        - ID: 1892
        - X: 26
        - Y: 14
        - Population: 29
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 97
        - IsCoastal: true
        - Wonders:
          - Great Firewall
          - Centaurus Extractors Headquarters
        
        ### Varna
        - ID: 2070
        - X: 29
        - Y: 17
        - Population: 30
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 120
        - IsCoastal: true
        
        ### Ohrid
        - ID: 2582
        - X: 30
        - Y: 10
        - Population: 30
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 105
        - IsCoastal: true
        - Wonders:
          - Sydney Opera House
        
        ### Nicomedia
        - ID: 2907
        - X: 16
        - Y: 16
        - Population: 26
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 110
        - IsCoastal: true
        
        ### Trebizond
        - ID: 4411
        - X: 12
        - Y: 13
        - Population: 26
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 112
        - IsCoastal: true
        
        ### Cherson
        - ID: 4922
        - X: 28
        - Y: 5
        - Population: 26
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 112
        - IsCoastal: true
        
        ### Sardica
        - ID: 5153
        - X: 17
        - Y: 10
        - Population: 27
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 70
        - IsCoastal: true
        
        ### Ani
        - ID: 6627
        - X: 25
        - Y: 20
        - Population: 25
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 120
        - IsCoastal: true
        
        ### Dyrrachium
        - ID: 8380
        - X: 9
        - Y: 11
        - Population: 24
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 120
        - IsCoastal: true
        
        ### Edessa
        - ID: 19610
        - X: 38
        - Y: 21
        - Population: 13
        - DefenseStrength: 96
        - IsCoastal: true
        
        ### Beshbalik
        - ID: 20737
        - X: 43
        - Y: 25
        - Population: 24
        - MajorityReligion: Tengriism
        - DefenseStrength: 97
        - IsOccupied: true
        
        ## Player: Austria
        
        ### Vienna
        - ID: 1062
        - X: 52
        - Y: 44
        - Population: 56
        - MajorityReligion: Catholicism
        - DefenseStrength: 76
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - National Monument
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Imperial College
          - Great Lighthouse
          - Great Library
          - Hanging Gardens
          - Porcelain Tower
          - Sistine Chapel
          - Kremlin
          - Brandenburg Gate
          - Eiffel Tower
          - Statue of Zeus
          - National Intelligence Agency
          - Leaning Tower of Pisa
          - Globe Theatre
          - Scrivener's Office
          - Foreign Bureau
          - Palace of Culture and Science
          - Ballhausplatz
          - Soho Foundry
          - The Motherland Calls
          - Empire State Building
          - Crystal Palace
          - Menin Gate
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
          - Celestial Throne
          - Trader Sid's Headquarters
        
        ### Salzburg
        - ID: 1230
        - X: 47
        - Y: 44
        - Population: 29
        - MajorityReligion: Catholicism
        - DefenseStrength: 101
        - IsCoastal: true
        
        ### Graz
        - ID: 1381
        - X: 52
        - Y: 40
        - Population: 31
        - MajorityReligion: Catholicism
        - DefenseStrength: 95
        - IsCoastal: true
        - Wonders:
          - Grand Temple
        
        ### Linz
        - ID: 1853
        - X: 45
        - Y: 40
        - Population: 29
        - MajorityReligion: Catholicism
        - DefenseStrength: 103
        - IsCoastal: true
        
        ### Klagenfurt
        - ID: 2283
        - X: 50
        - Y: 48
        - Population: 30
        - MajorityReligion: Catholicism
        - DefenseStrength: 99
        - IsCoastal: true
        
        ### Bregenz
        - ID: 2609
        - X: 54
        - Y: 47
        - Population: 29
        - MajorityReligion: Catholicism
        - DefenseStrength: 99
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - Royal Collection
        
        ### Innsbruck
        - ID: 3898
        - X: 60
        - Y: 47
        - Population: 29
        - MajorityReligion: Catholicism
        - DefenseStrength: 70
        - IsCoastal: true
        - Wonders:
          - Louvre
        
        ### Kitzbuhel
        - ID: 4416
        - X: 68
        - Y: 46
        - Population: 26
        - MajorityReligion: Catholicism
        - DefenseStrength: 102
        - IsCoastal: true
        
        ### St. Polten
        - ID: 4980
        - X: 64
        - Y: 47
        - Population: 27
        - MajorityReligion: Catholicism
        - DefenseStrength: 72
        - IsCoastal: true
        - Wonders:
          - Cristo Redentor
        
        ### Washakie
        - ID: 14850
        - X: 64
        - Y: 37
        - Population: 25
        - MajorityReligion: Catholicism
        - DefenseStrength: 97
        - IsOccupied: true
        - IsCoastal: true
        
        ### Timbisha
        - ID: 16211
        - X: 64
        - Y: 43
        - Population: 27
        - MajorityReligion: Catholicism
        - DefenseStrength: 65
        - IsPuppet: true
        - IsCoastal: true
        
        ### Villach
        - ID: 17332
        - X: 68
        - Y: 41
        - Population: 20
        - MajorityReligion: Catholicism
        - DefenseStrength: 105
        - IsCoastal: true
        
        ### Argos
        - ID: 19876
        - X: 68
        - Y: 34
        - Population: 14
        - MajorityReligion: Catholicism
        - DefenseStrength: 60
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: Germany
        
        ### Berlin
        - ID: 1063
        - X: 19
        - Y: 30
        - Population: 39
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 98
        - IsCoastal: true
        - FoodStored: 3640
        - FoodPerTurn: 0
        - ProductionStored: 0
        - ProductionPerTurn: 357
        - CurrentProduction: Fleet Destroyer
        - ProductionTurnsLeft: 3
        - GoldPerTurn: 357
        - SciencePerTurn: 324
        - CulturePerTurn: 241
        - FaithPerTurn: 74
        - TourismPerTurn: 163.25
        - HappinessDelta: 30
        - BuildingCount: 55
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Observatory
          - Garden
          - Harbor
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Armory
          - Military Base
          - Medical Lab
          - Workshop
          - Stock Exchange
          - Public School
          - Constabulary
          - Hanse
          - Hotel
          - Caravansary
          - Bath
          - Wire Service
          - Brewhouse
        - Wonders:
          - Heroic Epic
          - Circus Maximus
          - Ironworks
          - State Treasury
          - Royal Guardhouse
          - Royal Astrologer
        - GreatWorkCount: 7
        
        ### Hamburg
        - ID: 1247
        - X: 18
        - Y: 35
        - Population: 29
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 92
        - IsCoastal: true
        - FoodStored: 1349
        - FoodPerTurn: 0
        - ProductionStored: 0
        - ProductionPerTurn: 239
        - CurrentProduction: Strategic Defense System
        - ProductionTurnsLeft: 6
        - GoldPerTurn: 253
        - SciencePerTurn: 210
        - CulturePerTurn: 192
        - FaithPerTurn: 32
        - TourismPerTurn: 134.5
        - HappinessDelta: -4
        - BuildingCount: 53
        - ImportantBuildings:
          - Seaport
          - Stable
          - Water Mill
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Armory
          - Military Base
          - Medical Lab
          - Workshop
          - Stock Exchange
          - Public School
          - Constabulary
          - Hanse
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Bath
          - Wire Service
          - Brewhouse
        - Wonders:
          - Chartered Company
          - Angkor Wat
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
        - GreatWorkCount: 6
        
        ### Munich
        - ID: 1424
        - X: 16
        - Y: 26
        - Population: 28
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 96
        - IsCoastal: true
        - FoodStored: 1349
        - FoodPerTurn: 1
        - ProductionStored: 293
        - ProductionPerTurn: 168
        - CurrentProduction: Public Works
        - ProductionTurnsLeft: 6
        - GoldPerTurn: 151
        - SciencePerTurn: 228
        - CulturePerTurn: 256
        - FaithPerTurn: 30
        - TourismPerTurn: 217.25
        - BuildingCount: 56
        - ImportantBuildings:
          - Seaport
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Workshop
          - Stock Exchange
          - Public School
          - Constabulary
          - Hanse
          - Writers' Guild
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Coaling Station
          - Wire Service
          - Brewhouse
        - Wonders:
          - School of Philosophy
          - National Monument
          - Imperial College
          - Royal Collection
          - Colossus
          - Grand Temple
          - Prora
          - Hall of Honor
        - GreatWorkCount: 10
        
        ### Cologne
        - ID: 3600
        - X: 12
        - Y: 27
        - Population: 24
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 73
        - IsCoastal: true
        - FoodStored: 1192
        - FoodPerTurn: 0
        - ProductionStored: 556
        - ProductionPerTurn: 100
        - CurrentProduction: Public Works
        - ProductionTurnsLeft: 7
        - GoldPerTurn: 123
        - SciencePerTurn: 134
        - CulturePerTurn: 107
        - FaithPerTurn: 22
        - TourismPerTurn: 70
        - HappinessDelta: -13
        - BuildingCount: 52
        - ImportantBuildings:
          - Seaport
          - Stable
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Arsenal
          - Hospital
          - Workshop
          - Stock Exchange
          - Public School
          - Constabulary
          - Hanse
          - Artists' Guild
          - Hotel
          - Caravansary
          - Wire Service
          - Brewhouse
        - GreatWorkCount: 3
        
        ### Frankfurt
        - ID: 4137
        - X: 13
        - Y: 31
        - Population: 27
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 92
        - IsCoastal: true
        - FoodStored: 1053
        - FoodPerTurn: 1
        - ProductionStored: 0
        - ProductionPerTurn: 194
        - CurrentProduction: Strategic Defense System
        - ProductionTurnsLeft: 7
        - GoldPerTurn: 117
        - SciencePerTurn: 168
        - CulturePerTurn: 126
        - FaithPerTurn: 23
        - TourismPerTurn: 63
        - HappinessDelta: -3
        - BuildingCount: 55
        - ImportantBuildings:
          - Seaport
          - Stable
          - Water Mill
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Workshop
          - Stock Exchange
          - Public School
          - Constabulary
          - Hanse
          - Writers' Guild
          - Hotel
          - Caravansary
          - Bath
          - Wire Service
          - Brewhouse
        - GreatWorkCount: 2
        
        ### Aachen
        - ID: 4629
        - X: 21
        - Y: 41
        - Population: 26
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 108
        - IsCoastal: true
        - FoodStored: 1085
        - FoodPerTurn: 0
        - ProductionStored: 568
        - ProductionPerTurn: 142
        - CurrentProduction: Public Works
        - ProductionTurnsLeft: 6
        - GoldPerTurn: 114
        - SciencePerTurn: 143
        - CulturePerTurn: 105
        - FaithPerTurn: 23
        - TourismPerTurn: 27.25
        - HappinessDelta: -9
        - BuildingCount: 55
        - ImportantBuildings:
          - Seaport
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Armory
          - Military Base
          - Medical Lab
          - Workshop
          - Stock Exchange
          - Public School
          - Constabulary
          - Hanse
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Agribusiness
          - Wire Service
          - Brewhouse
        - GreatWorkCount: 0
        
        ### Dortmund
        - ID: 5096
        - X: 26
        - Y: 30
        - Population: 25
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 78
        - IsCoastal: true
        - FoodStored: 992
        - FoodPerTurn: 0
        - ProductionStored: 0
        - ProductionPerTurn: 104
        - CurrentProduction: Military Base
        - ProductionTurnsLeft: 14
        - GoldPerTurn: 192
        - SciencePerTurn: 116
        - CulturePerTurn: 82
        - FaithPerTurn: 24
        - TourismPerTurn: 19.25
        - HappinessDelta: -15
        - BuildingCount: 49
        - ImportantBuildings:
          - Harbor
          - Stadium
          - Temple
          - Broadcast Tower
          - Armory
          - Arsenal
          - Medical Lab
          - Workshop
          - Stock Exchange
          - Public School
          - Constabulary
          - Hanse
          - Writers' Guild
          - Hotel
          - Caravansary
          - Wire Service
          - Brewhouse
        - GreatWorkCount: 0
        
        ### Cordoba
        - ID: 13676
        - X: 36
        - Y: 26
        - Population: 22
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 95
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 714
        - FoodPerTurn: 2
        - ProductionStored: 1221
        - ProductionPerTurn: 239
        - CurrentProduction: Stadium
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 100
        - SciencePerTurn: 150
        - CulturePerTurn: 100
        - FaithPerTurn: 19
        - TourismPerTurn: 43
        - HappinessDelta: -3
        - BuildingCount: 51
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Armory
          - Military Base
          - Medical Lab
          - Workshop
          - Stock Exchange
          - Public School
          - Constabulary
          - Hanse
          - Caravansary
          - Chancery
          - Brewhouse
        - Wonders:
          - Nalanda
          - Civilized Jewelers Headquarters
        - GreatWorkCount: 2
        
        ### Eisenstadt
        - ID: 16156
        - X: 5
        - Y: 37
        - Population: 16
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 72
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 398
        - FoodPerTurn: 0
        - ProductionStored: 459
        - ProductionPerTurn: 80
        - CurrentProduction: Hospital
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 80
        - SciencePerTurn: 96
        - CulturePerTurn: 59
        - FaithPerTurn: 19
        - TourismPerTurn: 14.5
        - HappinessDelta: -8
        - BuildingCount: 40
        - ImportantBuildings:
          - Courthouse
          - Harbor
          - Zoo
          - Temple
          - Broadcast Tower
          - Barracks
          - Arsenal
          - Workshop
          - Stock Exchange
          - University
          - Hanse
          - Hotel
          - Caravansary
          - Grocer
          - Wire Service
          - Brewhouse
        - GreatWorkCount: 0
        
        ## Player: City-States
        
        ### Colombo
        - ID: 1065
        - X: 43
        - Y: 4
        - Population: 15
        - MajorityReligion: Protestantism
        - DefenseStrength: 87
        
        ### M'banza-Kongo
        - ID: 20411
        - X: 47
        - Y: 29
        - Population: 4
        - DefenseStrength: 78
        - Health: 99%
        
        ### Rio de Janeiro
        - ID: 1068
        - X: 35
        - Y: 32
        - Population: 21
        - DefenseStrength: 103
        - IsCoastal: true
        
        ### Brussels
        - ID: 4219
        - X: 64
        - Y: 31
        - Population: 20
        - DefenseStrength: 82
        - IsCoastal: true
        
        ### Shanghai
        - ID: 1070
        - X: 49
        - Y: 34
        - Population: 17
        - DefenseStrength: 70
        
        ### Huari
        - ID: 1071
        - X: 23
        - Y: 6
        - Population: 15
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 96
        - IsCoastal: true
        
        ### Warsaw
        - ID: 1072
        - X: 25
        - Y: 34
        - Population: 17
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 97
        - IsCoastal: true
        
        ### Kabul
        - ID: 1073
        - X: 21
        - Y: 46
        - Population: 26
        - MajorityReligion: Tengriism
        - DefenseStrength: 102
        - IsCoastal: true
        
        ### Manila
        - ID: 1074
        - X: 73
        - Y: 34
        - Population: 24
        - DefenseStrength: 107
        - IsCoastal: true
        
        ### Sydney
        - ID: 1076
        - X: 9
        - Y: 5
        - Population: 14
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 90
        - IsCoastal: true
        
        ### Genoa
        - ID: 1077
        - X: 28
        - Y: 24
        - Population: 21
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 102
        - IsCoastal: true
        
        ### Assur
        - ID: 1078
        - X: 15
        - Y: 21
        - Population: 20
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 103
        - IsCoastal: true
        
        ### Luba
        - ID: 1079
        - X: 54
        - Y: 36
        - Population: 20
        - MajorityReligion: Protestantism
        - DefenseStrength: 90
        
        ### Shedet
        - ID: 1080
        - X: 15
        - Y: 3
        - Population: 10
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 89
        
        # Military
        Military: summary reports about tactical zones and visible units.
        
        ## Unit Stats
        - Attack:
          - Mercenary:
            - Strength: 66
        - CityBombard:
          - Rocket Artillery:
            - Strength: 37
            - RangedStrength: 75
          - Artillery:
            - Strength: 27
            - RangedStrength: 50
          - Krupp Gun:
            - Strength: 27
            - RangedStrength: 55
        - FastAttack:
          - Modern Armor:
            - Strength: 100
          - Tank:
            - Strength: 75
        - Defense:
          - Mechanized Infantry:
            - Strength: 80
          - Infantry:
            - Strength: 62
        - Counter:
          - Mobile SAM:
            - Strength: 55
          - Anti-Aircraft Gun:
            - Strength: 40
        - Ranged:
          - Helicopter Gunship:
            - Strength: 70
            - RangedStrength: 70
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
          - Attack Submarine:
            - Strength: 50
            - RangedStrength: 72
        - CarrierSea:
          - Carrier:
            - Strength: 70
            - RangedStrength: 45
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
          - Special Forces:
            - Strength: 65
        
        ## Neutral Land Zone 1057
        - ZoneValue: 24
        - NeutralStrength: 1017
        - City: Moson Kahni
        - AreaID: 5
        - Plots: 26
        - CenterX: 54
        - CenterY: 26
        - Units:
          - The Shoshone:
            - Carrier: 1
            - Anti-Aircraft Gun: 1
            - Triplane: 1
        
        ## Neutral Land Zone 1058
        - ZoneValue: 6
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 360
        - NeutralStrength: 1231
        - FriendlyStrength: 2771
        - City: Karakorum
        - AreaID: 5
        - Plots: 24
        - CenterX: 40
        - CenterY: 28
        - Units:
          - Mongolia:
            - Mercenary: 1
          - Byzantium:
            - Infantry: 1
          - Germany:
            - Anti-Aircraft Gun: 2
        - Neighbors:
          - 13676
          - 1068
          - 19902
          - 19610
          - 20737
          - 18359
        
        ## Neutral Land Zone 1059
        - ZoneValue: 36
        - Dominance: Enemy
        - EnemyStrength: 445
        - NeutralStrength: 1405
        - City: Washington
        - AreaID: 5
        - Plots: 26
        - CenterX: 47
        - CenterY: 9
        - Units:
          - America:
            - Machine Gun: 1
        - Neighbors:
          - 1065
          - 1276
        
        ## Enemy Land Zone 1060
        - ZoneValue: 576
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 2859
        - NeutralStrength: 82
        - FriendlyStrength: 2630
        - City: Madrid
        - AreaID: 5
        - Plots: 29
        - CenterX: 44
        - CenterY: 19
        - Units:
          - Spain:
            - Machine Gun: 3
        - Neighbors:
          - 19610
          - 1276
          - 20737
        
        ## Friendly Land Zone 1063
        - ZoneValue: 36
        - Dominance: Friendly
        - FriendlyStrength: 4887
        - City: Berlin
        - AreaID: 11
        - Plots: 21
        - CenterX: 19
        - CenterY: 30
        - Units:
          - Germany:
            - Machine Gun: 5
            - Krupp Gun: 2
        - Neighbors:
          - 1424
          - 4137
          - 1247
          - -1424
          - -1063
          - 1072
          - -1072
        
        ## Neutral Land Zone 1065
        - ZoneValue: 9
        - Dominance: Enemy
        - EnemyStrength: 286
        - NeutralStrength: 1407
        - City: Colombo
        - AreaID: 5
        - Plots: 27
        - CenterX: 45
        - CenterY: 4
        - Units:
          - City-State Colombo:
            - Infantry: 1
        - Neighbors:
          - 1059
        
        ## Neutral Land Zone 1068
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 1653
        - FriendlyStrength: 957
        - City: Rio de Janeiro
        - AreaID: 5
        - Plots: 12
        - CenterX: 36
        - CenterY: 31
        - Units:
          - City-State Rio de Janeiro:
            - Tank: 2
            - Machine Gun: 2
          - Mongolia:
            - Machine Gun: 1
        - Neighbors:
          - 13676
          - 19902
          - 1058
        
        ## Neutral Land Zone 1072
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 98
        - FriendlyStrength: 3003
        - City: Warsaw
        - AreaID: 11
        - Plots: 16
        - CenterX: 23
        - CenterY: 34
        - Units:
          - City-State Warsaw:
            - Infantry: 3
            - Machine Gun: 3
        - Neighbors:
          - 1247
          - 1063
          - -1072
          - -4629
        
        ## Neutral Land Zone 1073
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 103
        - FriendlyStrength: 1281
        - City: Kabul
        - AreaID: 91
        - Plots: 13
        - CenterX: 20
        - CenterY: 47
        - Units:
          - City-State Kabul:
            - Light Tank: 1
            - Machine Gun: 3
        - Neighbors:
          - -1073
          - 4629
        
        ## Neutral Land Zone 1077
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 102
        - FriendlyStrength: 3055
        - City: Genoa
        - AreaID: 53
        - Plots: 12
        - CenterX: 27
        - CenterY: 24
        - Units:
          - City-State Genoa:
            - Infantry: 4
            - Special Forces: 1
            - Machine Gun: 4
        - Neighbors:
          - -1077
          - -6627
        
        ## Neutral Land Zone 1078
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 103
        - FriendlyStrength: 5627
        - City: Assur
        - AreaID: 11
        - Plots: 16
        - CenterX: 16
        - CenterY: 21
        - Units:
          - City-State Assur:
            - Infantry: 4
            - Machine Gun: 4
          - Germany:
            - Machine Gun: 3
        - Neighbors:
          - -1078
          - 1424
        
        ## Neutral Land Zone 1237
        - ZoneValue: 21
        - Dominance: Friendly
        - NeutralStrength: 70
        - FriendlyStrength: 4127
        - City: Adrianople
        - AreaID: 11
        - Plots: 15
        - CenterX: 21
        - CenterY: 13
        - Units:
          - Byzantium:
            - Infantry: 1
        - Neighbors:
          - -1237
        
        ## Friendly Land Zone 1247
        - ZoneValue: 30
        - Dominance: Friendly
        - FriendlyStrength: 3386
        - City: Hamburg
        - AreaID: 11
        - Plots: 22
        - CenterX: 18
        - CenterY: 34
        - Units:
          - Germany:
            - Bomber: 1
            - Krupp Gun: 3
        - Neighbors:
          - 4137
          - 1063
          - 1072
        
        ## Enemy Land Zone 1276
        - ZoneValue: 96
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 2290
        - NeutralStrength: 198
        - FriendlyStrength: 1313
        - City: Barcelona
        - AreaID: 5
        - Plots: 20
        - CenterX: 43
        - CenterY: 14
        - Units:
          - Spain:
            - Machine Gun: 1
        - Neighbors:
          - -1276
          - 1060
          - 1059
        
        ## Friendly Land Zone 1424
        - ZoneValue: 30
        - Dominance: Friendly
        - FriendlyStrength: 5485
        - City: Munich
        - AreaID: 11
        - Plots: 18
        - CenterX: 16
        - CenterY: 26
        - Units:
          - City-State Assur:
            - Infantry: 1
          - Germany:
            - Infantry: 1
            - Special Forces: 1
            - Krupp Gun: 5
        - Neighbors:
          - -1078
          - 3600
          - 1078
          - -1424
          - 4137
          - 1063
        
        ## Neutral Land Zone 2582
        - ZoneValue: 42
        - Dominance: Friendly
        - NeutralStrength: 105
        - FriendlyStrength: 2820
        - City: Ohrid
        - AreaID: 3
        - Plots: 20
        - CenterX: 29
        - CenterY: 10
        - Units:
          - Byzantium:
            - Helicopter Gunship: 1
            - Rocket Artillery: 2
        - Neighbors:
          - 4922
          - -4922
        
        ## Friendly Land Zone 3600
        - ZoneValue: 24
        - Dominance: Friendly
        - FriendlyStrength: 3719
        - City: Cologne
        - AreaID: 11
        - Plots: 6
        - CenterX: 13
        - CenterY: 27
        - Units:
          - Germany:
            - Special Forces: 1
            - Krupp Gun: 2
        - Neighbors:
          - 1424
          - 4137
        
        ## Friendly Land Zone 4137
        - ZoneValue: 24
        - Dominance: Friendly
        - FriendlyStrength: 3241
        - City: Frankfurt
        - AreaID: 11
        - Plots: 21
        - CenterX: 14
        - CenterY: 31
        - Units:
          - Germany:
            - Krupp Gun: 4
        - Neighbors:
          - 3600
          - 1424
          - 1247
          - 1063
        
        ## Friendly Land Zone 4629
        - ZoneValue: 24
        - Dominance: Friendly
        - FriendlyStrength: 2002
        - City: Aachen
        - AreaID: 84
        - Plots: 9
        - CenterX: 22
        - CenterY: 42
        - Units:
          - Germany:
            - Heavy Bomber: 1
            - Fighter: 1
            - Tank: 1
        - Neighbors:
          - -1073
          - -4629
          - 1073
        
        ## Neutral Land Zone 4922
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 112
        - FriendlyStrength: 2004
        - City: Cherson
        - AreaID: 3
        - Plots: 23
        - CenterX: 27
        - CenterY: 5
        - Units:
          - Byzantium:
            - Mechanized Infantry: 1
            - Heavy Bomber: 1
            - Fighter: 2
        - Neighbors:
          - -4922
          - 2582
        
        ## Friendly Land Zone 5096
        - ZoneValue: 18
        - Dominance: Friendly
        - FriendlyStrength: 3216
        - City: Dortmund
        - AreaID: 62
        - Plots: 5
        - CenterX: 26
        - CenterY: 30
        - Units:
          - City-State Warsaw:
            - Infantry: 1
          - Germany:
            - Heavy Bomber: 2
            - Machine Gun: 1
            - Krupp Gun: 2
        - Neighbors:
          - -1072
        
        ## Neutral Land Zone 6627
        - ZoneValue: 60
        - Dominance: Friendly
        - NeutralStrength: 120
        - FriendlyStrength: 4262
        - City: Ani
        - AreaID: 11
        - Plots: 14
        - CenterX: 25
        - CenterY: 18
        - Units:
          - Byzantium:
            - Modern Armor: 1
        - Neighbors:
          - -6627
        
        ## Enemy Land Zone 10390
        - ZoneValue: 96
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 324
        - NeutralStrength: 92
        - FriendlyStrength: 1374
        - City: Tiflis
        - AreaID: 4
        - Plots: 8
        - CenterX: 36
        - CenterY: 5
        - Units:
          - Spain:
            - Infantry: 1
        - Neighbors:
          - -10390
        
        ## Friendly Land Zone 13676
        - ZoneValue: 24
        - Dominance: Friendly
        - NeutralStrength: 611
        - FriendlyStrength: 3313
        - City: Cordoba
        - AreaID: 55
        - Plots: 16
        - CenterX: 36
        - CenterY: 26
        - Units:
          - Germany:
            - Heavy Bomber: 1
            - Fighter: 1
            - Anti-Aircraft Gun: 5
            - Fleet Destroyer: 1
            - Krupp Gun: 1
        - Neighbors:
          - 1068
          - -19610
          - 19610
          - 1058
        
        ## Friendly Land Zone 16156
        - ZoneValue: 3
        - Dominance: Friendly
        - FriendlyStrength: 660
        - City: Eisenstadt
        - AreaID: 66
        - Plots: 5
        - CenterX: 4
        - CenterY: 36
        - Units:
          - Germany:
            - Fighter: 2
            - Infantry: 1
        - Neighbors:
          - -16156
        
        ## Neutral Land Zone 18359
        - ZoneValue: 3
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 1599
        - NeutralStrength: 2597
        - FriendlyStrength: 393
        - City: Otrar
        - AreaID: 5
        - Plots: 24
        - CenterX: 44
        - CenterY: 32
        - Units:
          - Mongolia:
            - Machine Gun: 1
        - Neighbors:
          - 19902
          - 1058
        
        ## Neutral Land Zone 19610
        - ZoneValue: 48
        - Dominance: Friendly
        - Posture: Exploit Flanks
        - EnemyStrength: 2041
        - NeutralStrength: 186
        - FriendlyStrength: 4400
        - City: Edessa
        - AreaID: 5
        - Plots: 22
        - CenterX: 39
        - CenterY: 21
        - Units:
          - Spain:
            - Special Forces: 2
          - Germany:
            - Anti-Aircraft Gun: 2
          - Byzantium:
            - Helicopter Gunship: 1
            - Mobile SAM: 4
            - Light Tank: 1
            - Infantry: 3
        - Neighbors:
          - -19610
          - 13676
          - 1058
          - -1276
          - 1060
          - 20737
        
        ## Neutral Land Zone 19902
        - ZoneValue: -2147483645
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 478
        - NeutralStrength: 2575
        - FriendlyStrength: 340
        - City: Turfan
        - AreaID: 5
        - Plots: 26
        - CenterX: 40
        - CenterY: 33
        - Units:
          - City-State Rio de Janeiro:
            - Infantry: 1
        - Neighbors:
          - 1068
          - 1058
          - 18359
        
        ## Neutral Land Zone 20737
        - ZoneValue: 60
        - Dominance: Friendly
        - Posture: Exploit Flanks
        - EnemyStrength: 1671
        - NeutralStrength: 713
        - FriendlyStrength: 3002
        - City: Beshbalik
        - AreaID: 5
        - Plots: 29
        - CenterX: 43
        - CenterY: 25
        - Units:
          - Spain:
            - Artillery: 1
            - Infantry: 1
          - Germany:
            - Anti-Aircraft Gun: 3
            - Krupp Gun: 1
          - Byzantium:
            - Mobile SAM: 1
            - Light Tank: 1
            - Infantry: 1
        - Neighbors:
          - 1058
          - 19610
          - 1060
        
        ## Neutral Sea Zone -1073
        - ZoneValue: 6
        - Dominance: Friendly
        - NeutralStrength: 103
        - FriendlyStrength: 2914
        - City: Kabul
        - AreaID: 0
        - Plots: 60
        - CenterX: 21
        - CenterY: 47
        - Units:
          - City-State Kabul:
            - Destroyer: 3
            - Fleet Destroyer: 8
        - Neighbors:
          - -100008
          - -4629
          - 1073
          - 4629
        
        ## Neutral Sea Zone -19610
        - ZoneValue: 16
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 972
        - NeutralStrength: 96
        - FriendlyStrength: 1710
        - City: Edessa
        - AreaID: 0
        - Plots: 32
        - CenterX: 36
        - CenterY: 19
        - Units:
          - Byzantium:
            - Infantry: 1
        - Neighbors:
          - -100005
          - 13676
          - 19610
          - -1276
        
        ## Neutral Sea Zone -4922
        - ZoneValue: 6
        - Dominance: Friendly
        - NeutralStrength: 112
        - FriendlyStrength: 2828
        - City: Cherson
        - AreaID: 0
        - Plots: 32
        - CenterX: 30
        - CenterY: 3
        - Units:
          - Germany:
            - Fleet Destroyer: 1
        - Neighbors:
          - 4922
          - 2582
          - -10390
        
        ## Friendly Sea Zone -1424
        - ZoneValue: 10
        - Dominance: Friendly
        - FriendlyStrength: 3678
        - City: Munich
        - AreaID: 51
        - Plots: 10
        - CenterX: 18
        - CenterY: 25
        - Units:
          - Germany:
            - Fleet Destroyer: 1
        - Neighbors:
          - 1424
          - -1078
          - 1063
          - -1063
        
        ## Neutral Sea Zone -1078
        - ZoneValue: 6
        - Dominance: Friendly
        - NeutralStrength: 103
        - FriendlyStrength: 3615
        - City: Assur
        - AreaID: 0
        - Plots: 32
        - CenterX: 14
        - CenterY: 21
        - Units:
          - City-State Assur:
            - Fleet Destroyer: 5
        - Neighbors:
          - 1078
          - 1424
          - -1424
          - -6627
        
        ## Neutral Sea Zone -6627
        - ZoneValue: 20
        - Dominance: Friendly
        - NeutralStrength: 120
        - FriendlyStrength: 3654
        - City: Ani
        - AreaID: 44
        - Plots: 25
        - CenterX: 24
        - CenterY: 22
        - Units:
          - City-State Genoa:
            - Machine Gun: 1
            - Fleet Destroyer: 2
        - Neighbors:
          - -1078
          - -1063
          - -1077
          - 6627
          - 1077
        
        ## Friendly Sea Zone -1063
        - ZoneValue: 1
        - Dominance: Friendly
        - FriendlyStrength: 3672
        - City: Berlin
        - AreaID: 44
        - Plots: 10
        - CenterX: 21
        - CenterY: 28
        - Units:
          - Germany:
            - Infantry: 1
        - Neighbors:
          - 1063
          - -1424
          - -6627
          - -1072
        
        ## Friendly Sea Zone -4629
        - ZoneValue: 1
        - Dominance: Friendly
        - FriendlyStrength: 3357
        - City: Aachen
        - AreaID: 72
        - Plots: 39
        - CenterX: 21
        - CenterY: 40
        - Units:
          - Byzantium:
            - Fleet Destroyer: 1
        - Neighbors:
          - -100008
          - -1073
          - 4629
          - -1072
          - 1072
        
        ## Enemy Sea Zone -1276
        - ZoneValue: 128
        - Dominance: Even
        - Posture: Attrition
        - EnemyStrength: 1500
        - NeutralStrength: 105
        - FriendlyStrength: 1016
        - City: Barcelona
        - AreaID: 0
        - Plots: 16
        - CenterX: 40
        - CenterY: 13
        - Units:
          - Byzantium:
            - Attack Submarine: 1
        - Neighbors:
          - -100005
          - -10390
          - -19610
          - 1276
          - 19610
        
        ## Friendly Sea Zone -16156
        - ZoneValue: 6
        - Dominance: Friendly
        - FriendlyStrength: 667
        - City: Eisenstadt
        - AreaID: 0
        - Plots: 86
        - CenterX: 5
        - CenterY: 37
        - Units:
          - Germany:
            - Fleet Destroyer: 2
        - Neighbors:
          - -100008
          - 16156
        
        ## Enemy Sea Zone -10390
        - ZoneValue: 192
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 189
        - FriendlyStrength: 2744
        - City: Tiflis
        - AreaID: 0
        - Plots: 59
        - CenterX: 36
        - CenterY: 7
        - Units:
          - Byzantium:
            - Attack Submarine: 4
          - Germany:
            - Fleet Destroyer: 6
        - Neighbors:
          - -4922
          - 10390
          - -100005
          - -1276
        
        ## Neutral Sea Zone -1237
        - ZoneValue: 7
        - Dominance: Friendly
        - NeutralStrength: 70
        - FriendlyStrength: 3022
        - City: Adrianople
        - AreaID: 34
        - Plots: 7
        - CenterX: 23
        - CenterY: 11
        - Units:
          - Germany:
            - Infantry: 1
        - Neighbors:
          - 1237
        
        ## Neutral Sea Zone -100008
        - ZoneValue: 1
        - AreaID: 0
        - Plots: 212
        - CenterX: 6
        - CenterY: 46
        - Units:
          - Barbarians:
            - Machine Gun: 1
          - Germany:
            - Fleet Destroyer: 1
        - Neighbors:
          - -16156
          - -4629
          - -1073
        
        ## Neutral Sea Zone -1072
        - ZoneValue: 1
        - Dominance: Friendly
        - NeutralStrength: 98
        - FriendlyStrength: 4217
        - City: Warsaw
        - AreaID: 44
        - Plots: 39
        - CenterX: 26
        - CenterY: 35
        - Units:
          - City-State Warsaw:
            - Destroyer: 2
            - Fleet Destroyer: 9
          - Germany:
            - Destroyer: 1
        - Neighbors:
          - -1063
          - 1063
          - -4629
          - 1072
          - 5096
        
        ## Neutral Sea Zone -100005
        - ZoneValue: 1
        - AreaID: 0
        - Plots: 12
        - CenterX: 35
        - CenterY: 14
        - Units:
          - Germany:
            - Fleet Destroyer: 1
        - Neighbors:
          - -10390
          - -19610
          - -1276
        
        ## Neutral Sea Zone -1077
        - ZoneValue: 1
        - Dominance: Friendly
        - NeutralStrength: 102
        - FriendlyStrength: 3476
        - City: Genoa
        - AreaID: 31
        - Plots: 40
        - CenterX: 29
        - CenterY: 25
        - Units:
          - City-State Genoa:
            - Fleet Destroyer: 7
        - Neighbors:
          - -6627
          - 1077
        
        # Events
        Events: events since you last made a decision.
        
        ## Turn 457
        
        ### 0
        - Type: CombatResult
        - Grass Hills 45,28:
          - Owner: Byzantium
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 40
          - Damage: 40
          - Unit:
            - Level: 1
            - AI: Worker
            - Unit: Worker
            - ID: 20090
          - Player: 4: Byzantium
        
        ### 1
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1131
        - Player: 29
        - Plains Hills 24,36:
          - Owner: City-State Warsaw
          - Improvement: Mine
        
        ### 2
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 17948
        - Player: 29
        - Plots:
          - Grass Land 26,31:
            - Owner: Germany
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
          - Grass Hills 26,32:
            - Owner: City-State Warsaw
            - Improvement: Embassy
            - Route: Railroad
        
        ### 3
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19635
        - Player: 29
        
        ### 4
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19967
        - Player: 29
        
        ### 5
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20127
        - Player: 29
        
        ### 6
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 15120
        - Player: 29
        
        ### 7
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 17947
        - Player: 29
        - Plots:
          - Plains Land 22,34:
            - Owner: Germany
            - Route: Railroad
          - Plains Hills 23,34:
            - Owner: City-State Warsaw
            - Improvement: Mine
            - Route: Railroad
        
        ### 8
        - Type: PlayerGifted
        - GivingPlayer: 6: Germany
        - ReceivingPlayer: 31
        - Unit: Fleet Destroyer
        
        ### 9
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 92%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20403
        - Player: 34
        - Plots:
          - Coast 29,23:
            - Owner: City-State Genoa
        
        ### 10
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 90%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19544
        - Player: 34
        - Plots:
          - Coast 28,25:
            - Owner: City-State Genoa
          - Coast 29,26:
            - Owner: City-State Genoa
        
        ### 11
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 19151
        - Player: 34
        - Coast 26,21:
          - Owner: City-State Genoa
          - Resource: Fish
          - Improvement: Fishing Boats
        
        ### 12
        - Type: CityConstructed
        - City:
          - Name: Assur
          - Population: 20
          - ID: 1078
        - Owner: 35
        - Building: Strategic Defense System
        
        ### 13
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: FastAttack
          - Unit: Infantry
          - ID: 20625
        - Player: 63: Barbarians
        - Plots:
          - Plains Land 52,12:
            - Owner: America
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 51,13:
            - Owner: America
            - Improvement: Village
            - Route: Railroad
        
        ## Turn 458
        
        ### 0
        - Type: CityConvertsReligion
        - City:
          - Owner: The Shoshone
          - CityID: 1828
          - Population: 39
          - City: Agaidika
          - Terrain: Desert
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 57
          - Y: 33
        - Owner: 0: The Shoshone
        - Religion: Buddhism
        
        ### 1
        - Type: CityConvertsReligion
        - City:
          - Owner: The Shoshone
          - CityID: 1828
          - Population: 39
          - City: Agaidika
          - Terrain: Desert
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 57
          - Y: 33
        - Owner: 0: The Shoshone
        - Religion: Buddhism
        
        ### 2
        - Type: CityConvertsReligion
        - City:
          - Owner: The Shoshone
          - CityID: 1828
          - Population: 39
          - City: Agaidika
          - Terrain: Desert
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 57
          - Y: 33
        - Owner: 0: The Shoshone
        - Religion: Buddhism
        
        ### 3
        - Type: CityConvertsReligion
        - City:
          - Owner: Byzantium
          - CityID: 4922
          - Population: 26
          - City: Cherson
          - Terrain: Tundra
          - Religion: Eastern Orthodoxy
          - Route: Railroad
          - Plot: Hills
          - X: 28
          - Y: 5
        - Owner: 4: Byzantium
        - Religion: Eastern Orthodoxy
        
        ### 4
        - Type: CityConvertsReligion
        - City:
          - Owner: Byzantium
          - CityID: 4922
          - Population: 26
          - City: Cherson
          - Terrain: Tundra
          - Religion: Eastern Orthodoxy
          - Route: Railroad
          - Plot: Hills
          - X: 28
          - Y: 5
        - Owner: 4: Byzantium
        - Religion: Eastern Orthodoxy
        
        ### 5
        - Type: CityConvertsReligion
        - City:
          - Owner: Austria
          - CityID: 1230
          - Population: 29
          - City: Salzburg
          - Terrain: Plains
          - Resource: Bison
          - Religion: Catholicism
          - Route: Railroad
          - Plot: Land
          - X: 47
          - Y: 44
        - Owner: 5: Austria
        - Religion: Catholicism
        
        ### 6
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 18334
        - Player: 0: The Shoshone
        - Plots:
          - Coast 17,37:
            - Owner: Germany
            - Resource: Pearls
            - Improvement: Fishing Boats
          - Coast 18,36:
            - Owner: Germany
          - Plains Land 18,35:
            - Owner: Germany
            - CityID: 1247
            - Population: 29
            - IsRiver: true
            - City: Hamburg
            - Religion: Eastern Orthodoxy
            - Route: Railroad
        
        ### 7
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20349
        - Player: 0: The Shoshone
        - Coast 53,13:
          - Owner: America
        
        ### 8
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20067
        - Player: 1: Mongolia
        - Plots:
          - Grass Hills 46,26:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Ordo
            - Route: Railroad
          - Grass Land 45,26:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
        
        ### 9
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 18632
        - Player: 1: Mongolia
        - Plots:
          - Ocean 0,40:
            - Owner: The Shoshone
        
        ### 10
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19571
        - Player: 1: Mongolia
        - Plots:
          - Grass Land 42,25:
            - Owner: Byzantium
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Hills 42,26:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Plains Hills 41,27:
            - Owner: Mongolia
            - Route: Railroad
          - Desert Hills 41,28:
            - Owner: Mongolia
            - IsRiver: true
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
          - Desert Hills 40,28:
            - Owner: Mongolia
            - CityID: 1058
            - Population: 26
            - IsRiver: true
            - City: Karakorum
            - Religion: Tengriism
            - Route: Railroad
        
        ### 11
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20150
        - Player: 1: Mongolia
        - Plots:
          - Plains Hills 39,27:
            - Owner: Mongolia
            - Improvement: Fort
            - Route: Railroad
          - Grass Land 39,26:
            - Owner: Mongolia
            - IsRiver: true
            - Resource: Tea
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 38,26:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Citadel
            - Route: Road
          - Plains Hills 37,26:
            - Owner: Germany
            - Improvement: Hacienda
            - Route: Road
          - Plains Hills 36,26:
            - Owner: Germany
            - CityID: 13676
            - Population: 22
            - City: Cordoba
            - Religion: Eastern Orthodoxy
            - Route: Railroad
        
        ### 12
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20474
        - Player: 1: Mongolia
        - Plots:
          - Grass Land 42,25:
            - Owner: Byzantium
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 42,24:
            - Owner: Byzantium
            - IsRiver: true
            - Route: Railroad
          - Plains Hills 41,23:
            - Owner: Byzantium
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 42,22:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Hacienda
            - Route: Railroad
          - Desert Land 42,21:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Holy Site
            - Route: Railroad
            - Feature: Fallout
        
        ### 13
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 20917
        - Player: 1: Mongolia
        - Plots:
          - Desert Land 40,30:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 40,31:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 41,32:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
        
        ### 14
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 17248
        - Player: 1: Mongolia
        - Plots:
          - Grass Land 36,33:
            - Owner: City-State Rio de Janeiro
            - Improvement: Farm
          - Plains Land 36,32:
            - Owner: City-State Rio de Janeiro
            - IsRiver: true
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
        
        ### 15
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 19048
        - Player: 1: Mongolia
        - Plots:
          - Desert Land 41,29:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 41,30:
            - Owner: Mongolia
            - Improvement: Fort
            - Route: Railroad
          - Desert Land 41,31:
            - Owner: Mongolia
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 41,32:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
        
        ### 16
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 18791
        - Player: 1: Mongolia
        - Plots:
          - Desert Land 40,30:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 40,31:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 41,32:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
        
        ### 17
        - Type: UnitBuildCompleted
        - Owner: 1: Mongolia
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4588
        - Build: Construct a Farm
        - Plains Land 40,25:
          - Owner: Mongolia
          - IsRiver: true
        
        ### 18
        - Type: UnitBuildCompleted
        - Owner: 1: Mongolia
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 9577
        - Build: Construct a Farm
        - Grass Land 41,25:
          - Owner: Mongolia
          - IsRiver: true
        
        ### 19
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 20065
        - Player: 1: Mongolia
        - Plots:
          - Coast 36,34:
            - Owner: City-State Rio de Janeiro
          - Coast 34,34:
            - Owner: City-State Rio de Janeiro
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 20
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 17308
        - Player: 1: Mongolia
        - Plains Land 39,33:
          - Owner: Mongolia
          - IsRiver: true
          - Improvement: Farm
        
        ### 21
        - Type: CityProjectComplete
        - City:
          - Name: Washington
          - Population: 29
          - ID: 1059
        - Player: 2: America
        - Project: Public Works
        
        ### 22
        - Type: CityCreated
        - City:
          - Name: Washington
          - Population: 29
          - ID: 1059
        - Owner: 2: America
        - Project: Public Works
        
        ### 23
        - Type: CityConvertsReligion
        - City:
          - Owner: America
          - CityID: 1224
          - Population: 28
          - IsRiver: true
          - City: New York
          - Terrain: Desert
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 49
          - Y: 14
        - Owner: 2: America
        - Religion: Protestantism
        
        ### 24
        - Type: CityCreated
        - City:
          - Name: Atlanta
          - Population: 26
          - ID: 1751
        - Owner: 2: America
        - Project: Public Works
        
        ### 25
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20858
        - Player: 2: America
        - Plots:
          - Desert Land 48,11:
            - Owner: America
            - IsRiver: true
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 48,10:
            - Owner: America
            - IsRiver: true
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
          - Plains Hills 47,9:
            - Owner: America
            - CityID: 1059
            - Population: 29
            - IsRiver: true
            - City: Washington
            - Religion: Protestantism
            - Route: Railroad
        
        ### 26
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19919
        - Player: 2: America
        - Plots:
          - Plains Land 48,9:
            - Owner: America
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 49,8:
            - Owner: America
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
        
        ### 27
        - Type: CityBeginsWLTKD
        - Change: 6
        - City:
          - Owner: America
          - CityID: 1059
          - Population: 29
          - IsRiver: true
          - City: Washington
          - Terrain: Plains
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Hills
          - X: 47
          - Y: 9
        - Player: 2: America
        
        ### 28
        - Type: CityBeginsWLTKD
        - Change: 6
        - City:
          - Owner: America
          - CityID: 2601
          - Population: 23
          - City: Chicago
          - Terrain: Desert
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 52
          - Y: 13
        - Player: 2: America
        
        ### 29
        - Type: CombatResult
        - Grass Land 51,13:
          - Owner: America
          - Improvement: Village
          - Route: Railroad
        - Attacker:
          - RemainingHP: 20
          - Damage: 20
        - Defender:
          - RemainingHP: 46
          - Damage: 46
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - AI: FastAttack
            - Unit: Infantry
            - ID: 20625
        
        ### 30
        - Type: CombatResult
        - Grass Land 51,13:
          - Owner: America
          - Improvement: Village
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 43
          - Damage: 89
          - Unit:
            - Level: 1
            - Health: 63%
            - AI: FastAttack
            - Unit: Infantry
            - ID: 20625
          - Player: 63: Barbarians
        
        ### 31
        - Type: CombatResult
        - Grass Land 51,13:
          - Owner: America
          - Improvement: Village
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 36
          - Damage: 125
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 28%
            - AI: FastAttack
            - Unit: Infantry
            - ID: 20625
        
        ### 32
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 18147
        - Player: 2: America
        - Grass Land 51,13:
          - Owner: America
          - Improvement: Village
          - Route: Railroad
        
        ### 33
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 19723
        - Player: 2: America
        - Plots:
          - Plains Land 52,12:
            - Owner: America
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 52,13:
            - Owner: America
            - CityID: 2601
            - Population: 23
            - City: Chicago
            - Religion: Protestantism
            - Route: Railroad
        
        ### 34
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 19651
        - Player: 2: America
        - Plots:
          - Desert Land 48,11:
            - Owner: America
            - IsRiver: true
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 48,10:
            - Owner: America
            - IsRiver: true
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
          - Plains Land 48,9:
            - Owner: America
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 49,8:
            - Owner: America
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
        
        ### 35
        - Type: CombatResult
        - Desert Hills 53,11:
          - Owner: America
          - Resource: Aluminum
          - Improvement: Holy Site
        - Attacker:
          - RemainingHP: 16
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Player: 0: The Shoshone
          - Unit:
            - Level: 3
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 20349
        
        ### 36
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 18795
        - Player: 2: America
        - Grass Land 51,13:
          - Owner: America
          - Improvement: Village
          - Route: Railroad
        
        ### 37
        - Type: CombatResult
        - Coast 53,14:
          - Owner: America
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 45
          - Damage: 56
          - Player: 0: The Shoshone
          - Unit:
            - Level: 4
            - Health: 91%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 20535
        
        ### 38
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 73%
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 20828
        - Player: 2: America
        - Plots:
          - Grass Land 51,13:
            - Owner: America
            - Improvement: Village
            - Route: Railroad
          - Plains Land 52,12:
            - Owner: America
            - Improvement: Farm
            - Route: Railroad
        
        ### 39
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 18281
        - Player: 2: America
        - Tundra Hills 47,24:
          - Owner: America
          - Resource: Sheep
          - Improvement: Pasture
          - Route: Railroad
        
        ### 40
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1930
        - Player: 2: America
        - Plots:
          - Grass Land 51,13:
            - Owner: America
            - Improvement: Village
            - Route: Railroad
          - Plains Land 52,12:
            - Owner: America
            - Improvement: Farm
            - Route: Railroad
        
        ### 41
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 12318
        - Player: 2: America
        - Plots:
          - Plains Land 48,10:
            - Owner: America
            - IsRiver: true
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
          - Desert Land 48,11:
            - Owner: America
            - IsRiver: true
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
            - Feature: Flood Plains
          - Grass Land 51,13:
            - Owner: America
            - Improvement: Village
            - Route: Railroad
        
        ### 42
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 2: America
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 12318
        - Build: Repair an Improvement
        - Grass Land 51,13:
          - Owner: America
          - Improvement: Village
          - Route: Railroad
        
        ### 43
        - Type: UnitBuildCompleted
        - Owner: 2: America
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 6506
        - Build: Construct a Fort
        - Grass Hills 44,23:
          - Owner: America
        
        ### 44
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Missionary
          - Unit: Missionary
          - ID: 21000
        - Player: 2: America
        - Plots:
          - Plains Land 48,10:
            - Owner: America
            - IsRiver: true
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
          - Desert Land 48,11:
            - Owner: America
            - IsRiver: true
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
            - Feature: Flood Plains
          - Grass Land 46,24:
            - Owner: America
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
          - Grass Land 45,25:
            - Owner: America
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
        
        ### 45
        - Type: CombatResult
        - Coast 37,8:
          - Owner: Spain
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 17
          - Damage: 91
          - Unit:
            - Level: 4
            - Health: 26%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 18666
          - Player: 6: Germany
        
        ### 46
        - Type: CombatResult
        - Plains Hills 42,22:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Hacienda
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 29
          - Damage: 54
          - Unit:
            - Level: 4
            - Health: 75%
            - AI: Counter
            - Unit: Mobile SAM
            - ID: 20505
          - Player: 4: Byzantium
        
        ### 47
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 20769
        - Player: 3: Spain
        - Plots:
          - Desert Hills 41,19:
            - Owner: Spain
            - IsRiver: true
            - Resource: Gold
            - Improvement: Mine
            - Route: Railroad
            - Feature: Fallout
          - Desert Land 41,18:
            - Owner: Spain
            - Resource: Aluminum
            - Improvement: Citadel
            - Route: Railroad
        
        ### 48
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 21074
        - Player: 3: Spain
        - Plots:
          - Desert Land 42,21:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Holy Site
            - Route: Railroad
            - Feature: Fallout
          - Desert Land 42,20:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Hacienda
            - Route: Railroad
            - Feature: Fallout
          - Plains Hills 41,21:
            - Owner: Spain
            - Resource: Coal
            - Improvement: Holy Site
            - Route: Road
        
        ### 49
        - Type: CombatResult
        - Plains Hills 42,22:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Hacienda
          - Route: Railroad
        - Attacker:
          - RemainingHP: 28
          - Damage: 28
        - Defender:
          - RemainingHP: 38
          - Damage: 92
          - Player: 4: Byzantium
          - Unit:
            - Level: 4
            - Health: 46%
            - AI: Counter
            - Unit: Mobile SAM
            - ID: 20505
        
        ### 50
        - Type: CombatResult
        - Plains Hills 42,22:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Hacienda
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 8
          - Damage: 100
          - Player: 4: Byzantium
          - Unit:
            - Level: 4
            - Health: 8%
            - AI: Counter
            - Unit: Mobile SAM
            - ID: 20505
        
        ### 51
        - Type: CombatResult
        - Plains Hills 40,18:
          - Owner: Spain
          - Resource: Gold
          - Improvement: Academy
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 38
          - Damage: 68
          - Player: 4: Byzantium
          - Unit:
            - Level: 4
            - Health: 70%
            - AI: Counter
            - Unit: Mobile SAM
            - ID: 20441
        
        ### 52
        - Type: CombatResult
        - Grass Hills 43,22:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Citadel
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 31
          - Damage: 48
          - Player: 4: Byzantium
          - Unit:
            - Level: 4
            - Health: 83%
            - AI: Paradrop
            - Unit: Special Forces
            - ID: 17642
        
        ### 53
        - Type: CombatResult
        - Grass Hills 43,22:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Citadel
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 27
          - Damage: 75
          - Player: 4: Byzantium
          - Unit:
            - Level: 4
            - Health: 52%
            - AI: Paradrop
            - Unit: Special Forces
            - ID: 17642
        
        ### 54
        - Type: CombatResult
        - Plains Hills 40,18:
          - Owner: Spain
          - Resource: Gold
          - Improvement: Academy
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 32
          - Damage: 100
          - Player: 4: Byzantium
          - Unit:
            - Level: 4
            - Health: 32%
            - AI: Counter
            - Unit: Mobile SAM
            - ID: 20441
        
        ### 55
        - Type: CombatResult
        - Grass Hills 43,22:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Citadel
        - Attacker:
          - RemainingHP: 15
          - Damage: 15
        - Defender:
          - RemainingHP: 38
          - Damage: 113
          - Player: 4: Byzantium
          - Unit:
            - Level: 4
            - Health: 25%
            - AI: Paradrop
            - Unit: Special Forces
            - ID: 17642
        
        ### 56
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 88%
          - AI: Defense
          - Unit: Infantry
          - ID: 21075
        - Player: 3: Spain
        - Grass Hills 43,22:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Citadel
        
        ### 57
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 85%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 20866
        - Player: 3: Spain
        - Desert Hills 41,19:
          - Owner: Spain
          - IsRiver: true
          - Resource: Gold
          - Improvement: Mine
          - Route: Railroad
          - Feature: Fallout
        
        ### 58
        - Type: CombatResult
        - Plains Hills 39,19:
          - Owner: Byzantium
          - Resource: Deer
          - Improvement: Town
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 29
          - Damage: 29
          - Player: 4: Byzantium
          - Unit:
            - Level: 4
            - AI: Counter
            - Unit: Mobile SAM
            - ID: 20562
        
        ### 59
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 85%
          - AI: General
          - Unit: Great General
          - ID: 10441
        - Player: 3: Spain
        - Plots:
          - Desert Land 41,18:
            - Owner: Spain
            - Resource: Aluminum
            - Improvement: Citadel
            - Route: Railroad
          - Desert Hills 41,19:
            - Owner: Spain
            - IsRiver: true
            - Resource: Gold
            - Improvement: Mine
            - Route: Railroad
            - Feature: Fallout
        
        ### 60
        - Type: CombatResult
        - Coast 35,7:
          - Owner: Spain
          - Resource: Fish
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Player: 6: Germany
          - Unit:
            - Level: 4
            - Health: 85%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 18955
        - Interceptor:
          - Damage: 271
          - Unit:
            - Level: 3
            - AI: DefenseAir
            - Unit: Fighter
            - ID: 20877
          - Player: 3: Spain
        
        ### 61
        - Type: UnitKilledInCombat
        - KilledPlayer: 3: Spain
        - KillerPlayer: 6: Germany
        - KilledUnit: Bomber
        
        ### 62
        - Type: CombatResult
        - Plains Land 43,24:
          - Owner: Byzantium
          - IsRiver: true
          - Resource: Oil
          - Improvement: Ordo
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 29
          - Damage: 89
          - Player: 6: Germany
          - Unit:
            - Level: 3
            - Health: 40%
            - AI: Counter
            - Unit: Anti-Aircraft Gun
            - ID: 20039
        
        ### 63
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 53%
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 20489
        - Player: 3: Spain
        - Plots:
          - Desert Land 41,18:
            - Owner: Spain
            - Resource: Aluminum
            - Improvement: Citadel
            - Route: Railroad
          - Plains Hills 40,18:
            - Owner: Spain
            - Resource: Gold
            - Improvement: Academy
        
        ### 64
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 14463
        - Player: 3: Spain
        - Plots:
          - Coast 37,6:
            - Owner: Spain
          - Ocean 40,6:
            - Feature: Ice
        
        ### 65
        - Type: CityExtendsWeLoveKingDay
        - Change: 10
        - City:
          - Owner: Byzantium
          - CityID: 19610
          - Population: 13
          - City: Edessa
          - Terrain: Plains
          - Route: Railroad
          - Plot: Hills
          - X: 38
          - Y: 21
        - Player: 4: Byzantium
        
        ### 66
        - Type: CityConstructed
        - City:
          - Name: Edessa
          - Population: 13
          - ID: 19610
        - Owner: 4: Byzantium
        - Building: Circus
        
        ### 67
        - Type: CityBoughtPlot
        - WithFaithCulture: true
        - Player: 4: Byzantium
        - City:
          - Name: Edessa
          - Population: 13
          - ID: 19610
        - Ocean 37,16:
          - Owner: Byzantium
        
        ### 68
        - Type: CityConstructed
        - City:
          - Name: Beshbalik
          - Population: 24
          - ID: 20737
        - Owner: 4: Byzantium
        - Building: Centaurus Extractors Office
        
        ### 69
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 19855
        - Player: 4: Byzantium
        - Plots:
          - Desert Hills 26,30:
            - Owner: Germany
            - CityID: 5096
            - Population: 25
            - City: Dortmund
            - Resource: Aluminum
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Coast 26,29:
            - Owner: Germany
          - Coast 26,28:
            - Owner: Germany
          - Coast 25,27:
            - Owner: Germany
        
        ### 70
        - Type: PlayerTradeRouteCompleted
        - Domain: 2
        - OriginPlayer: 4: Byzantium
        - DestinationCity:
          - Name: Nicomedia
          - Population: 26
          - ID: 2907
        - DestinationPlayer: 4: Byzantium
        - OriginCity:
          - Name: Constantinople
          - Population: 55
          - ID: 1061
        - Connection: Production
        
        ### 71
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 19856
        - Player: 4: Byzantium
        - Plots:
          - Coast 22,23:
            - Owner: Byzantium
          - Ocean 23,25:
            - Owner: Byzantium
        
        ### 72
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 19075
        - Player: 4: Byzantium
        
        ### 73
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19200
        - Player: 4: Byzantium
        - Plots:
          - Desert Land 16,20:
            - Owner: City-State Assur
            - IsRiver: true
            - Improvement: Embassy
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 16,19:
            - Owner: Byzantium
            - Improvement: Aplekton
          - Desert Land 17,18:
            - Owner: Byzantium
            - Resource: Oil
            - Improvement: Oil Well
        
        ### 74
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 20507
        - Player: 4: Byzantium
        - Plots:
          - Coast 25,26:
            - Owner: Germany
          - Coast 25,25:
            - Owner: Byzantium
          - Ocean 24,23:
            - Owner: Byzantium
        
        ### 75
        - Type: CombatResult
        - Plains Hills 40,18:
          - Owner: Spain
          - Resource: Gold
          - Improvement: Academy
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 27
          - Damage: 74
          - Unit:
            - Level: 4
            - Health: 53%
            - AI: Paradrop
            - Unit: Special Forces
            - ID: 20489
          - Player: 3: Spain
        
        ### 76
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Helicopter Gunship
          - ID: 21088
        - Player: 4: Byzantium
        - Plains Land 30,10:
          - Owner: Byzantium
          - CityID: 2582
          - Population: 30
          - IsRiver: true
          - City: Ohrid
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 77
        - Type: UnitCreated
        - UnitType: Helicopter Gunship
        - Player: 4: Byzantium
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Helicopter Gunship
          - ID: 21088
        - Plains Land 30,10:
          - Owner: Byzantium
          - CityID: 2582
          - Population: 30
          - IsRiver: true
          - City: Ohrid
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 78
        - Type: UnitUpgraded
        - Player: 4: Byzantium
        - OldUnit:
          - Level: 3
          - AI: Ranged
          - Unit: Light Tank
          - ID: 15606
        - NewUnit:
          - Level: 1
          - AI: Ranged
          - Unit: Helicopter Gunship
          - ID: 21088
        
        ### 79
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 4: Byzantium
        - OriginalUnit:
          - Level: 3
          - AI: Ranged
          - Unit: Light Tank
          - ID: 15606
        - NewOwner: 4: Byzantium
        - ConvertingUnit:
          - Level: 3
          - AI: Ranged
          - Unit: Helicopter Gunship
          - ID: 21088
        
        ### 80
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Mechanized Infantry
          - ID: 21090
        - Player: 4: Byzantium
        - Desert Land 16,16:
          - Owner: Byzantium
          - CityID: 2907
          - Population: 26
          - IsRiver: true
          - City: Nicomedia
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 81
        - Type: UnitCreated
        - UnitType: Mechanized Infantry
        - Player: 4: Byzantium
        - Unit:
          - Level: 1
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 21090
        - Desert Land 16,16:
          - Owner: Byzantium
          - CityID: 2907
          - Population: 26
          - IsRiver: true
          - City: Nicomedia
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 82
        - Type: UnitUpgraded
        - Player: 4: Byzantium
        - OldUnit:
          - Level: 2
          - AI: Defense
          - Unit: Infantry
          - ID: 16694
        - NewUnit:
          - Level: 1
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 21090
        
        ### 83
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 4: Byzantium
        - OriginalUnit:
          - Level: 2
          - AI: Defense
          - Unit: Infantry
          - ID: 16694
        - NewOwner: 4: Byzantium
        - ConvertingUnit:
          - Level: 2
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 21090
        
        ### 84
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Mechanized Infantry
          - ID: 21092
        - Player: 4: Byzantium
        - Desert Hills 12,13:
          - Owner: Byzantium
          - CityID: 4411
          - Population: 26
          - City: Trebizond
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 85
        - Type: UnitCreated
        - UnitType: Mechanized Infantry
        - Player: 4: Byzantium
        - Unit:
          - Level: 1
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 21092
        - Desert Hills 12,13:
          - Owner: Byzantium
          - CityID: 4411
          - Population: 26
          - City: Trebizond
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 86
        - Type: UnitUpgraded
        - Player: 4: Byzantium
        - OldUnit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 16826
        - NewUnit:
          - Level: 1
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 21092
        
        ### 87
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 4: Byzantium
        - OriginalUnit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 16826
        - NewOwner: 4: Byzantium
        - ConvertingUnit:
          - Level: 3
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 21092
        
        ### 88
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Defense
          - Unit: Infantry
          - ID: 16692
        - Player: 4: Byzantium
        - Plots:
          - Ocean 36,21:
            - Owner: Byzantium
          - Coast 37,21:
            - Owner: Byzantium
          - Plains Hills 38,21:
            - Owner: Byzantium
            - CityID: 19610
            - Population: 13
            - City: Edessa
            - Route: Railroad
          - Plains Hills 39,21:
            - Owner: Byzantium
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 40,21:
            - Owner: Spain
            - Resource: Uranium
            - Improvement: Hacienda
            - Route: Railroad
        
        ### 89
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 16969
        - Player: 4: Byzantium
        - Plains Hills 40,20:
          - Owner: Byzantium
          - Improvement: Mine
        
        ### 90
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Mobile SAM
          - ID: 20570
        - Player: 4: Byzantium
        - Plots:
          - Grass Hills 40,23:
            - Owner: Byzantium
            - Improvement: Hacienda
            - Route: Railroad
          - Desert Land 41,22:
            - Owner: Spain
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
        
        ### 91
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 38%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 19148
        - Player: 4: Byzantium
        - Plots:
          - Grass Land 43,25:
            - Owner: Byzantium
            - CityID: 20737
            - Population: 24
            - IsRiver: true
            - City: Beshbalik
            - Religion: Tengriism
            - Route: Railroad
          - Grass Land 42,25:
            - Owner: Byzantium
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 42,24:
            - Owner: Byzantium
            - IsRiver: true
            - Route: Railroad
        
        ### 92
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 42%
          - AI: Defense
          - Unit: Infantry
          - ID: 16696
        - Player: 4: Byzantium
        - Plots:
          - Plains Hills 39,23:
            - Owner: Byzantium
            - Improvement: Mine
          - Grass Hills 40,23:
            - Owner: Byzantium
            - Improvement: Hacienda
            - Route: Railroad
        
        ### 93
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 71%
          - AI: Counter
          - Unit: Mobile SAM
          - ID: 20562
        - Player: 4: Byzantium
        - Plots:
          - Plains Hills 39,20:
            - Owner: Byzantium
            - Resource: Sheep
            - Improvement: City Ruins
            - Route: Railroad
          - Plains Hills 38,21:
            - Owner: Byzantium
            - CityID: 19610
            - Population: 13
            - City: Edessa
            - Route: Railroad
          - Plains Hills 39,22:
            - Owner: Byzantium
          - Plains Hills 39,23:
            - Owner: Byzantium
            - Improvement: Mine
        
        ### 94
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 16969
        - Player: 4: Byzantium
        - Plains Hills 39,19:
          - Owner: Byzantium
          - Resource: Deer
          - Improvement: Town
          - Route: Railroad
        
        ### 95
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 38%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 19148
        - Player: 4: Byzantium
        - Plots:
          - Grass Land 42,25:
            - Owner: Byzantium
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Hills 42,26:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Plains Land 41,26:
            - Owner: Mongolia
            - Route: Railroad
          - Grass Hills 40,26:
            - Owner: Mongolia
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 39,25:
            - Owner: Mongolia
            - Improvement: Ordo
            - Route: Railroad
          - Plains Hills 40,24:
            - Owner: Byzantium
            - Improvement: Aplekton
        
        ### 96
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Light Tank
          - ID: 19725
        - Player: 4: Byzantium
        - Plots:
          - Plains Land 44,26:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 43,25:
            - Owner: Byzantium
            - CityID: 20737
            - Population: 24
            - IsRiver: true
            - City: Beshbalik
            - Religion: Tengriism
            - Route: Railroad
          - Plains Land 43,24:
            - Owner: Byzantium
            - IsRiver: true
            - Resource: Oil
            - Improvement: Ordo
            - Route: Railroad
          - Grass Land 42,24:
            - Owner: Byzantium
            - IsRiver: true
            - Route: Railroad
        
        ### 97
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 18246
        - Player: 4: Byzantium
        - Plots:
          - Ocean 37,20:
            - Owner: Byzantium
          - Ocean 37,19:
            - Owner: Byzantium
        
        ### 98
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 19006
        - Player: 4: Byzantium
        - Coast 38,19:
          - Owner: Byzantium
        
        ### 99
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 95%
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 18249
        - Player: 4: Byzantium
        - Plots:
          - Ocean 36,20:
            - Owner: Byzantium
          - Ocean 36,19:
            - Owner: Byzantium
        
        ### 100
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 18247
        - Player: 4: Byzantium
        - Ocean 37,19:
          - Owner: Byzantium
        
        ### 101
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Light Tank
          - ID: 19725
        - Player: 4: Byzantium
        - Plots:
          - Grass Land 42,25:
            - Owner: Byzantium
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Hills 42,26:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Plains Land 41,26:
            - Owner: Mongolia
            - Route: Railroad
          - Grass Hills 40,26:
            - Owner: Mongolia
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 39,25:
            - Owner: Mongolia
            - Improvement: Ordo
            - Route: Railroad
          - Grass Hills 39,24:
            - Owner: Mongolia
            - Resource: Sheep
          - Plains Hills 38,23:
            - Owner: Byzantium
            - Improvement: Mine
            - Route: Road
          - Grass Land 38,22:
            - Owner: Byzantium
            - Resource: Rice
            - Improvement: Holy Site
            - Route: Railroad
          - Plains Hills 38,21:
            - Owner: Byzantium
            - CityID: 19610
            - Population: 13
            - City: Edessa
            - Route: Railroad
          - Plains Hills 39,20:
            - Owner: Byzantium
            - Resource: Sheep
            - Improvement: City Ruins
            - Route: Railroad
        
        ### 102
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Helicopter Gunship
          - ID: 21093
        - Player: 4: Byzantium
        - Plains Hills 39,20:
          - Owner: Byzantium
          - Resource: Sheep
          - Improvement: City Ruins
          - Route: Railroad
        
        ### 103
        - Type: UnitCreated
        - UnitType: Helicopter Gunship
        - Player: 4: Byzantium
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Helicopter Gunship
          - ID: 21093
        - Plains Hills 39,20:
          - Owner: Byzantium
          - Resource: Sheep
          - Improvement: City Ruins
          - Route: Railroad
        
        ### 104
        - Type: UnitUpgraded
        - Player: 4: Byzantium
        - OldUnit:
          - Level: 3
          - AI: Ranged
          - Unit: Light Tank
          - ID: 19725
        - NewUnit:
          - Level: 1
          - AI: Ranged
          - Unit: Helicopter Gunship
          - ID: 21093
        
        ### 105
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 4: Byzantium
        - OriginalUnit:
          - Level: 3
          - AI: Ranged
          - Unit: Light Tank
          - ID: 19725
        - NewOwner: 4: Byzantium
        - ConvertingUnit:
          - Level: 3
          - AI: Ranged
          - Unit: Helicopter Gunship
          - ID: 21093
        
        ### 106
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 17837
        - Player: 4: Byzantium
        - Plots:
          - Plains Hills 39,27:
            - Owner: Mongolia
            - Improvement: Fort
            - Route: Railroad
          - Grass Hills 40,26:
            - Owner: Mongolia
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 41,26:
            - Owner: Mongolia
            - Route: Railroad
          - Grass Hills 42,26:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 42,25:
            - Owner: Byzantium
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Plains Land 43,24:
            - Owner: Byzantium
            - IsRiver: true
            - Resource: Oil
            - Improvement: Ordo
            - Route: Railroad
          - Grass Hills 43,23:
            - Owner: Byzantium
            - IsRiver: true
            - Resource: Marble
            - Improvement: Quarry
        
        ### 107
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Mobile SAM
          - ID: 20442
        - Player: 4: Byzantium
        - Plots:
          - Ocean 36,21:
            - Owner: Byzantium
          - Coast 37,21:
            - Owner: Byzantium
          - Plains Hills 38,21:
            - Owner: Byzantium
            - CityID: 19610
            - Population: 13
            - City: Edessa
            - Route: Railroad
          - Plains Hills 39,21:
            - Owner: Byzantium
            - Improvement: Mine
            - Route: Railroad
        
        ### 108
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Light Tank
          - ID: 17401
        - Player: 4: Byzantium
        - Plots:
          - Coast 38,20:
            - Owner: Byzantium
          - Plains Hills 38,21:
            - Owner: Byzantium
            - CityID: 19610
            - Population: 13
            - City: Edessa
            - Route: Railroad
          - Plains Hills 39,20:
            - Owner: Byzantium
            - Resource: Sheep
            - Improvement: City Ruins
            - Route: Railroad
          - Plains Hills 40,20:
            - Owner: Byzantium
            - Improvement: Mine
          - Plains Land 40,19:
            - Owner: Spain
            - Improvement: Hacienda
            - Route: Railroad
        
        ### 109
        - Type: CombatResult
        - Plains Hills 40,18:
          - Owner: Spain
          - Resource: Gold
          - Improvement: Academy
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 22
          - Damage: 96
          - Player: 3: Spain
          - Unit:
            - Level: 4
            - Health: 26%
            - AI: Paradrop
            - Unit: Special Forces
            - ID: 20489
        
        ### 110
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 95%
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 18311
        - Player: 4: Byzantium
        - Plots:
          - Ocean 33,9:
            - Owner: Byzantium
          - Ocean 34,9:
            - Owner: Byzantium
          - Coast 35,9:
            - Owner: Spain
          - Coast 36,8:
            - Owner: Spain
          - Ocean 35,8:
            - Owner: Spain
        
        ### 111
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 19676
        - Player: 4: Byzantium
        - Plots:
          - Ocean 34,10:
            - Owner: Byzantium
          - Ocean 34,9:
            - Owner: Byzantium
          - Ocean 35,8:
            - Owner: Spain
          - Coast 36,8:
            - Owner: Spain
        
        ### 112
        - Type: CombatResult
        - Snow Land 36,7:
          - Owner: Spain
          - CityID: 10390
          - Population: 20
          - City: Tiflis
          - Resource: Stone
          - Religion: Buddhism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 5
          - Damage: 72
          - Player: 3: Spain
        
        ### 113
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 19676
        - Player: 4: Byzantium
        - Coast 35,9:
          - Owner: Spain
        
        ### 114
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 19760
        - Player: 4: Byzantium
        - Plots:
          - Coast 35,10:
            - Owner: Spain
            - Resource: Fish
          - Coast 35,9:
            - Owner: Spain
          - Coast 36,8:
            - Owner: Spain
        
        ### 115
        - Type: CombatResult
        - Snow Land 36,7:
          - Owner: Spain
          - CityID: 10390
          - Population: 20
          - City: Tiflis
          - Resource: Stone
          - Religion: Buddhism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 5
          - Damage: 77
          - Player: 3: Spain
        
        ### 116
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 19760
        - Player: 4: Byzantium
        - Plots:
          - Ocean 35,8:
            - Owner: Spain
          - Ocean 34,8:
            - Owner: Byzantium
        
        ### 117
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 19005
        - Player: 4: Byzantium
        - Plots:
          - Coast 35,9:
            - Owner: Spain
          - Coast 36,8:
            - Owner: Spain
        
        ### 118
        - Type: CombatResult
        - Snow Land 36,7:
          - Owner: Spain
          - CityID: 10390
          - Population: 20
          - City: Tiflis
          - Resource: Stone
          - Religion: Buddhism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 4
          - Damage: 81
          - Player: 3: Spain
        
        ### 119
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 19005
        - Player: 4: Byzantium
        - Plots:
          - Ocean 35,8:
            - Owner: Spain
          - Ocean 34,7:
            - Owner: Spain
        
        ### 120
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 18948
        - Player: 4: Byzantium
        - Plots:
          - Ocean 33,8:
            - Owner: Byzantium
          - Ocean 34,8:
            - Owner: Byzantium
          - Ocean 35,8:
            - Owner: Spain
          - Coast 36,8:
            - Owner: Spain
        
        ### 121
        - Type: CombatResult
        - Snow Land 36,7:
          - Owner: Spain
          - CityID: 10390
          - Population: 20
          - City: Tiflis
          - Resource: Stone
          - Religion: Buddhism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 4
          - Damage: 85
          - Player: 3: Spain
        
        ### 122
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 38%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 19148
        - Player: 4: Byzantium
        - Plots:
          - Grass Land 39,25:
            - Owner: Mongolia
            - Improvement: Ordo
            - Route: Railroad
          - Grass Hills 40,26:
            - Owner: Mongolia
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 41,26:
            - Owner: Mongolia
            - Route: Railroad
          - Grass Hills 42,26:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
        
        ### 123
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Mobile SAM
          - ID: 20442
        - Player: 4: Byzantium
        - Plots:
          - Plains Hills 39,22:
            - Owner: Byzantium
          - Plains Hills 38,23:
            - Owner: Byzantium
            - Improvement: Mine
            - Route: Road
        
        ### 124
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 46%
          - AI: Defense
          - Unit: Infantry
          - ID: 19090
        - Player: 4: Byzantium
        - Plots:
          - Grass Hills 37,25:
            - Owner: Germany
            - Improvement: Fort
            - Route: Railroad
          - Plains Hills 37,26:
            - Owner: Germany
            - Improvement: Hacienda
            - Route: Road
          - Grass Hills 37,27:
            - Owner: Germany
            - IsRiver: true
            - Resource: Iron
            - Improvement: Mine
            - Route: Road
          - Plains Hills 38,27:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Hacienda
          - Plains Hills 39,27:
            - Owner: Mongolia
            - Improvement: Fort
            - Route: Railroad
        
        ### 125
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Light Tank
          - ID: 17401
        - Player: 4: Byzantium
        - Plains Hills 40,20:
          - Owner: Byzantium
          - Improvement: Mine
        
        ### 126
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 20503
        - Player: 4: Byzantium
        - Plots:
          - Coast 26,22:
            - Owner: Byzantium
          - Coast 26,21:
            - Owner: City-State Genoa
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 27,21:
            - Owner: City-State Genoa
          - Coast 28,20:
            - Owner: Byzantium
        
        ### 127
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 20439
        - Player: 4: Byzantium
        - Plots:
          - Coast 25,21:
            - Owner: Byzantium
          - Coast 26,21:
            - Owner: City-State Genoa
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 27,20:
            - Owner: City-State Genoa
            - Resource: Coral
            - Improvement: Fishing Boats
        
        ### 128
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 7366
        - Player: 4: Byzantium
        - Plains Hills 38,21:
          - Owner: Byzantium
          - CityID: 19610
          - Population: 13
          - City: Edessa
          - Route: Railroad
        
        ### 129
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 60%
          - AI: Worker
          - Unit: Worker
          - ID: 20090
        - Player: 4: Byzantium
        - Plots:
          - Grass Land 44,27:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 44,26:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 43,25:
            - Owner: Byzantium
            - CityID: 20737
            - Population: 24
            - IsRiver: true
            - City: Beshbalik
            - Religion: Tengriism
            - Route: Railroad
        
        ### 130
        - Type: RebaseTo
        - Player: 4: Byzantium
        - Unit:
          - Level: 3
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 20877
        - Tundra Hills 28,5:
          - Owner: Byzantium
          - CityID: 4922
          - Population: 26
          - City: Cherson
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 131
        - Type: RebaseTo
        - Player: 4: Byzantium
        - Unit:
          - Level: 4
          - AI: DefenseAir
          - Unit: Triplane
          - ID: 16481
        - Plains Land 17,10:
          - Owner: Byzantium
          - CityID: 5153
          - Population: 27
          - City: Sardica
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 132
        - Type: RebaseTo
        - Player: 4: Byzantium
        - Unit:
          - Level: 3
          - AI: DefenseAir
          - Unit: Triplane
          - ID: 16482
        - Plains Land 17,10:
          - Owner: Byzantium
          - CityID: 5153
          - Population: 27
          - City: Sardica
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 133
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 18611
        - Player: 4: Byzantium
        - Plots:
          - Grass Hills 40,26:
            - Owner: Mongolia
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 41,26:
            - Owner: Mongolia
            - Route: Railroad
          - Grass Hills 42,26:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Plains Land 43,26:
            - Owner: Byzantium
            - IsRiver: true
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
          - Grass Land 43,25:
            - Owner: Byzantium
            - CityID: 20737
            - Population: 24
            - IsRiver: true
            - City: Beshbalik
            - Religion: Tengriism
            - Route: Railroad
        
        ### 134
        - Type: TileRouteChanged
        - OldRoute: 1
        - NewRoute: 1
        - Owner: 4: Byzantium
        - Grass Hills 41,24:
          - Owner: Byzantium
          - IsRiver: true
          - Resource: Deer
          - Improvement: Citadel
          - Route: Railroad
        
        ### 135
        - Type: BuildFinished
        - Player: 4: Byzantium
        - Grass Hills 41,24:
          - Owner: Byzantium
          - IsRiver: true
          - Resource: Deer
          - Improvement: Citadel
          - Route: Railroad
        
        ### 136
        - Type: UnitBuildCompleted
        - Owner: 4: Byzantium
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3547
        - Build: Repair an Improvement
        - Grass Hills 41,24:
          - Owner: Byzantium
          - IsRiver: true
          - Resource: Deer
          - Improvement: Citadel
          - Route: Railroad
        
        ### 137
        - Type: UnitBuildStart
        - Owner: 4: Byzantium
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3547
        - Build: Repair an Improvement
        - Grass Hills 41,24:
          - Owner: Byzantium
          - IsRiver: true
          - Resource: Deer
          - Improvement: Citadel
          - Route: Railroad
        
        ### 138
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 4: Byzantium
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3808
        - Build: Construct a Railroad
        - Plains Hills 39,22:
          - Owner: Byzantium
        
        ### 139
        - Type: TileRouteChanged
        - NewRoute: 1
        - Owner: 4: Byzantium
        - Plains Hills 39,23:
          - Owner: Byzantium
          - Improvement: Mine
          - Route: Railroad
        
        ### 140
        - Type: BuildFinished
        - Player: 4: Byzantium
        - Plains Hills 39,23:
          - Owner: Byzantium
          - Improvement: Mine
          - Route: Railroad
        
        ### 141
        - Type: UnitBuildCompleted
        - Owner: 4: Byzantium
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4719
        - Build: Construct a Railroad
        - Plains Hills 39,23:
          - Owner: Byzantium
          - Improvement: Mine
          - Route: Railroad
        
        ### 142
        - Type: UnitBuildStart
        - Owner: 4: Byzantium
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4719
        - Build: Construct a Railroad
        - Plains Hills 39,23:
          - Owner: Byzantium
          - Improvement: Mine
          - Route: Railroad
        
        ### 143
        - Type: UnitBuildCompleted
        - Owner: 4: Byzantium
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 5056
        - Build: Build an Aplekton
        - Grass Land 44,25:
          - Owner: Byzantium
          - IsRiver: true
        
        ### 144
        - Type: UnitBuildCompleted
        - Owner: 4: Byzantium
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 19753
        - Build: Build an Aplekton
        - Plains Hills 43,28:
          - Owner: Byzantium
        
        ### 145
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3895
        - Player: 4: Byzantium
        - Plots:
          - Ocean 33,24:
            - Owner: Germany
          - Ocean 34,24:
            - Owner: Germany
          - Coast 35,24:
            - Owner: Germany
          - Grass Hills 35,25:
            - Owner: Germany
            - Improvement: Fort
          - Coast 35,26:
            - Owner: Germany
          - Plains Hills 36,26:
            - Owner: Germany
            - CityID: 13676
            - Population: 22
            - City: Cordoba
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Grass Hills 36,25:
            - Owner: Germany
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 37,25:
            - Owner: Germany
            - Improvement: Fort
            - Route: Railroad
          - Grass Land 38,26:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Citadel
            - Route: Road
          - Grass Land 39,26:
            - Owner: Mongolia
            - IsRiver: true
            - Resource: Tea
            - Improvement: Plantation
            - Route: Railroad
        
        ### 146
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 5058
        - Player: 4: Byzantium
        - Plots:
          - Grass Hills 28,24:
            - Owner: City-State Genoa
            - CityID: 1077
            - Population: 21
            - City: Genoa
            - Resource: Jewelry
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Coast 29,24:
            - Owner: City-State Genoa
            - Resource: Fish
            - Improvement: Fishing Boats
          - Ocean 32,22:
            - Owner: Byzantium
          - Ocean 32,21:
            - Owner: Byzantium
        
        ### 147
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 9456
        - Player: 4: Byzantium
        - Plots:
          - Ocean 31,22:
            - Owner: Byzantium
          - Ocean 32,22:
            - Owner: Byzantium
          - Ocean 34,22:
            - Owner: Byzantium
          - Ocean 34,21:
            - Owner: Byzantium
        
        ### 148
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 16248
        - Player: 4: Byzantium
        - Plots:
          - Desert Hills 29,9:
            - Owner: Byzantium
            - Improvement: Village
            - Route: Railroad
          - Plains Land 30,10:
            - Owner: Byzantium
            - CityID: 2582
            - Population: 30
            - IsRiver: true
            - City: Ohrid
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Plains Hills 29,12:
            - Owner: Byzantium
            - Improvement: Aplekton
            - Route: Railroad
          - Ocean 32,20:
            - Owner: Byzantium
          - Ocean 32,21:
            - Owner: Byzantium
        
        ### 149
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Missionary
          - Unit: Missionary
          - ID: 19939
        - Player: 4: Byzantium
        - Plots:
          - Grass Land 45,26:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Hills 46,26:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Ordo
            - Route: Railroad
        
        ### 150
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Missionary
          - Unit: Missionary
          - ID: 20171
        - Player: 4: Byzantium
        - Plots:
          - Grass Hills 28,24:
            - Owner: City-State Genoa
            - CityID: 1077
            - Population: 21
            - City: Genoa
            - Resource: Jewelry
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Coast 29,24:
            - Owner: City-State Genoa
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 29,23:
            - Owner: City-State Genoa
          - Ocean 30,22:
            - Owner: Byzantium
          - Ocean 31,21:
            - Owner: Byzantium
          - Ocean 32,21:
            - Owner: Byzantium
        
        ### 151
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 18187
        - Player: 4: Byzantium
        - Plots:
          - Ocean 32,19:
            - Owner: Byzantium
          - Ocean 33,19:
            - Owner: Byzantium
          - Ocean 35,20:
            - Owner: Byzantium
          - Ocean 36,20:
            - Owner: Byzantium
        
        ### 152
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Defense
          - Unit: Infantry
          - ID: 16695
        - Player: 4: Byzantium
        - Plots:
          - Desert Land 11,13:
            - Owner: Byzantium
            - Improvement: Aplekton
            - Route: Railroad
          - Desert Hills 12,13:
            - Owner: Byzantium
            - CityID: 4411
            - Population: 26
            - City: Trebizond
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Plains Hills 13,14:
            - Owner: Byzantium
            - Improvement: Aplekton
            - Route: Railroad
          - Desert Hills 14,14:
            - Owner: Byzantium
            - Improvement: Village
            - Route: Railroad
          - Plains Land 15,14:
            - Owner: Byzantium
            - Resource: Wheat
            - Improvement: Aplekton
            - Route: Railroad
          - Plains Hills 16,14:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 16,13:
            - Owner: Byzantium
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
        
        ### 153
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19396
        - Player: 4: Byzantium
        - Plots:
          - Coast 16,38:
            - Owner: Germany
          - Ocean 17,38:
            - Owner: Germany
          - Ocean 18,38:
            - Owner: Germany
          - Coast 19,38:
            - Owner: Germany
          - Coast 20,38:
            - Owner: Germany
          - Ocean 21,38:
            - Owner: Germany
        
        ### 154
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 21016
        - Player: 4: Byzantium
        - Plots:
          - Desert Land 16,16:
            - Owner: Byzantium
            - CityID: 2907
            - Population: 26
            - IsRiver: true
            - City: Nicomedia
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Coast 15,16:
            - Owner: Byzantium
          - Desert Land 15,17:
            - Owner: Byzantium
            - Improvement: Aplekton
          - Coast 16,18:
            - Owner: Byzantium
          - Desert Land 16,19:
            - Owner: Byzantium
            - Improvement: Aplekton
          - Desert Land 16,20:
            - Owner: City-State Assur
            - IsRiver: true
            - Improvement: Embassy
            - Route: Railroad
            - Feature: Flood Plains
        
        ### 155
        - Type: CityConvertsReligion
        - City:
          - Owner: Austria
          - CityID: 17332
          - Population: 20
          - IsRiver: true
          - City: Villach
          - Terrain: Plains
          - Religion: Catholicism
          - Route: Railroad
          - Plot: Land
          - X: 68
          - Y: 41
        - Owner: 5: Austria
        - Religion: Catholicism
        
        ### 156
        - Type: EspionageState
        - SpyIndex: 4
        - SpyState: 3
        - City:
          - Owner: Germany
          - CityID: 1247
          - Population: 29
          - IsRiver: true
          - City: Hamburg
          - Terrain: Plains
          - Religion: Eastern Orthodoxy
          - Route: Railroad
          - Plot: Land
          - X: 18
          - Y: 35
        - SpyOwner: 5: Austria
        
        ### 157
        - Type: PlayerDoneTurn
        - NextPlayer: 6: Germany
        - Player: 5: Austria
        
        ### 158
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 21111
        - Player: 6: Germany
        - Desert Land 13,31:
          - Owner: Germany
          - CityID: 4137
          - Population: 27
          - IsRiver: true
          - City: Frankfurt
          - Resource: Wheat
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 159
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 6: Germany
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 21111
        - Desert Land 13,31:
          - Owner: Germany
          - CityID: 4137
          - Population: 27
          - IsRiver: true
          - City: Frankfurt
          - Resource: Wheat
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 160
        - Type: CityTrained
        - WithGold: true
        - Player: 6: Germany
        - City:
          - Name: Frankfurt
          - Population: 27
          - ID: 4137
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 21111
        
        ### 161
        - Type: CityConstructed
        - City:
          - Name: Berlin
          - Population: 39
          - ID: 1063
        - Owner: 6: Germany
        - Building: Military Base
        
        ### 162
        - Type: CityConstructed
        - City:
          - Name: Hamburg
          - Population: 29
          - ID: 1247
        - Owner: 6: Germany
        - Building: Military Base
        
        ### 163
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 21116
        - Player: 6: Germany
        - Desert Land 13,31:
          - Owner: Germany
          - CityID: 4137
          - Population: 27
          - IsRiver: true
          - City: Frankfurt
          - Resource: Wheat
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 164
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 6: Germany
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 21116
        - Desert Land 13,31:
          - Owner: Germany
          - CityID: 4137
          - Population: 27
          - IsRiver: true
          - City: Frankfurt
          - Resource: Wheat
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 165
        - Type: CityTrained
        - Player: 6: Germany
        - City:
          - Name: Frankfurt
          - Population: 27
          - ID: 4137
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 21116
        
        ### 166
        - Type: CityEventChoiceEnded
        - City:
          - Name: Dortmund
          - Population: 25
          - ID: 5096
        - Player: 6: Germany
        - Choice: 83
        
        ### 167
        - Type: CityProjectComplete
        - City:
          - Name: Dortmund
          - Population: 25
          - ID: 5096
        - Player: 6: Germany
        - Project: Public Works
        
        ### 168
        - Type: CityCreated
        - City:
          - Name: Dortmund
          - Population: 25
          - ID: 5096
        - Owner: 6: Germany
        - Project: Public Works
        
        ### 169
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 19436
        - Player: 6: Germany
        - Plots:
          - Coast 26,34:
            - Owner: City-State Warsaw
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 26,33:
            - Owner: City-State Warsaw
          - Coast 27,32:
            - Owner: Germany
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 27,31:
            - Owner: Germany
          - Coast 28,30:
            - Owner: Germany
          - Coast 27,29:
            - Owner: Germany
          - Coast 26,29:
            - Owner: Germany
          - Desert Hills 26,30:
            - Owner: Germany
            - CityID: 5096
            - Population: 25
            - City: Dortmund
            - Resource: Aluminum
            - Religion: Eastern Orthodoxy
            - Route: Railroad
        
        ### 170
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 19437
        - Player: 6: Germany
        - Plots:
          - Ocean 28,31:
            - Owner: Germany
          - Coast 28,30:
            - Owner: Germany
          - Coast 27,29:
            - Owner: Germany
          - Coast 26,29:
            - Owner: Germany
          - Desert Hills 26,30:
            - Owner: Germany
            - CityID: 5096
            - Population: 25
            - City: Dortmund
            - Resource: Aluminum
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Coast 25,30:
            - Owner: Germany
          - Ocean 24,30:
            - Owner: Germany
          - Ocean 23,30:
            - Owner: Germany
        
        ### 171
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19634
        - Player: 6: Germany
        - Plots:
          - Desert Hills 17,16:
            - Owner: Byzantium
            - Improvement: Aplekton
            - Route: Railroad
          - Plains Land 17,17:
            - Owner: Byzantium
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
          - Desert Land 17,18:
            - Owner: Byzantium
            - Resource: Oil
            - Improvement: Oil Well
          - Desert Land 16,19:
            - Owner: Byzantium
            - Improvement: Aplekton
          - Desert Land 16,20:
            - Owner: City-State Assur
            - IsRiver: true
            - Improvement: Embassy
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 15,21:
            - Owner: City-State Assur
            - CityID: 1078
            - Population: 20
            - IsRiver: true
            - City: Assur
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Grass Land 15,22:
            - Owner: City-State Assur
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
        
        ### 172
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 19894
        - Player: 6: Germany
        - Plots:
          - Coast 21,36:
            - Owner: Germany
          - Coast 20,36:
            - Owner: Germany
            - Resource: Pearls
            - Improvement: Fishing Boats
          - Coast 19,35:
            - Owner: Germany
          - Plains Land 18,35:
            - Owner: Germany
            - CityID: 1247
            - Population: 29
            - IsRiver: true
            - City: Hamburg
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Coast 22,36:
            - Owner: Germany
        
        ### 173
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 19146
        - Player: 6: Germany
        - Plots:
          - Coast 27,29:
            - Owner: Germany
          - Coast 26,29:
            - Owner: Germany
          - Desert Hills 26,30:
            - Owner: Germany
            - CityID: 5096
            - Population: 25
            - City: Dortmund
            - Resource: Aluminum
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Coast 25,30:
            - Owner: Germany
          - Ocean 24,30:
            - Owner: Germany
          - Ocean 23,30:
            - Owner: Germany
          - Coast 22,30:
            - Owner: Germany
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 21,30:
            - Owner: Germany
            - Resource: Pearls
            - Improvement: Fishing Boats
        
        ### 174
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 19147
        - Player: 6: Germany
        - Plots:
          - Coast 35,34:
            - Owner: Mongolia
          - Coast 34,33:
            - Owner: City-State Rio de Janeiro
            - Resource: Fish
            - Improvement: Fishing Boats
          - Ocean 33,33:
            - Owner: Mongolia
          - Ocean 33,32:
            - Owner: City-State Rio de Janeiro
        
        ### 175
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 19966
        - Player: 6: Germany
        - Plots:
          - Ocean 3,37:
            - Owner: Germany
          - Ocean 77,37:
            - Owner: The Shoshone
          - Coast 76,37:
            - Owner: The Shoshone
          - Coast 75,37:
            - Owner: The Shoshone
        
        ### 176
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20341
        - Player: 6: Germany
        - Plots:
          - Grass Land 18,29:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 19,30:
            - Owner: Germany
            - CityID: 1063
            - Population: 39
            - IsRiver: true
            - City: Berlin
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Grass Land 17,29:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 16,29:
            - Owner: Germany
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 15,29:
            - Owner: Germany
            - Resource: Rice
            - Improvement: Farm
            - Route: Railroad
          - Grass Hills 14,29:
            - Owner: Germany
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 14,30:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Desert Land 13,31:
            - Owner: Germany
            - CityID: 4137
            - Population: 27
            - IsRiver: true
            - City: Frankfurt
            - Resource: Wheat
            - Religion: Eastern Orthodoxy
            - Route: Railroad
        
        ### 177
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 20461
        - Player: 6: Germany
        - Plots:
          - Coast 14,21:
            - Owner: City-State Assur
          - Coast 13,21:
            - Owner: City-State Assur
            - Feature: Atoll
          - Coast 13,22:
            - Owner: City-State Assur
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 12,23:
            - Owner: Germany
            - Resource: Fish
          - Ocean 12,24:
            - Owner: Germany
          - Ocean 11,25:
            - Owner: Germany
          - Coast 12,26:
            - Owner: Germany
          - Grass Land 12,27:
            - Owner: Germany
            - CityID: 3600
            - Population: 24
            - City: Cologne
            - Religion: Eastern Orthodoxy
            - Route: Railroad
        
        ### 178
        - Type: CityEventChoiceActivated
        - City:
          - Name: Chicago
          - Population: 23
          - ID: 2601
        - Player: 2: America
        - Choice: 80
        
        ### 179
        - Type: EspionageResult
        - SpyResult: Killed
        - SourcePlayer: 6: Germany
        - TargetPlayer: 2: America
        - City:
          - Owner: America
          - CityID: 2601
          - Population: 23
          - City: Chicago
          - Terrain: Desert
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 52
          - Y: 13
        
        ### 180
        - Type: EspionageState
        - SpyIndex: 3
        - SpyState: 0
        - SpyOwner: 6: Germany
        
        ### 181
        - Type: PlayerDoTurn
        - Player: 6: Germany
        
        ### 182
        - Type: UnitPromoted
        - Unit:
          - Level: 5
          - Health: 19%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 18666
        - Player: 6: Germany
        - Promotion: Blitz
        
        ### 183
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 11%
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 20039
        - Player: 6: Germany
        - Plots:
          - Grass Land 42,25:
            - Owner: Byzantium
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Plains Land 43,26:
            - Owner: Byzantium
            - IsRiver: true
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 44,26:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
        
        ### 184
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 18497
        - Player: 6: Germany
        - Plains Hills 36,27:
          - Owner: Germany
          - Resource: Jade
          - Improvement: Manufactory
          - Route: Railroad
        
        ### 185
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: CityBombard
          - Unit: Krupp Gun
          - ID: 12282
        - Player: 6: Germany
        - Plots:
          - Grass Land 38,26:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Citadel
            - Route: Road
          - Plains Hills 37,26:
            - Owner: Germany
            - Improvement: Hacienda
            - Route: Road
        
        ### 186
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 13244
        - Player: 6: Germany
        - Plains Hills 37,26:
          - Owner: Germany
          - Improvement: Hacienda
          - Route: Road
        
        ### 187
        - Type: CombatResult
        - Plains Hills 41,21:
          - Owner: Spain
          - Resource: Coal
          - Improvement: Holy Site
          - Route: Road
        - Attacker:
          - RemainingHP: 13
          - Damage: 13
        - Defender:
          - RemainingHP: 25
          - Damage: 53
          - Player: 3: Spain
          - Unit:
            - Level: 4
            - Health: 72%
            - AI: Paradrop
            - Unit: Special Forces
            - ID: 21074
        
        ### 188
        - Type: CombatResult
        - Plains Hills 41,21:
          - Owner: Spain
          - Resource: Coal
          - Improvement: Holy Site
          - Route: Road
        - Attacker:
          - RemainingHP: 13
          - Damage: 26
        - Defender:
          - RemainingHP: 22
          - Damage: 75
          - Player: 3: Spain
          - Unit:
            - Level: 4
            - Health: 47%
            - AI: Paradrop
            - Unit: Special Forces
            - ID: 21074
        
        ### 189
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: CityBombard
          - Unit: Krupp Gun
          - ID: 14139
        - Player: 6: Germany
        - Plots:
          - Grass Land 39,25:
            - Owner: Mongolia
            - Improvement: Ordo
            - Route: Railroad
          - Grass Hills 40,26:
            - Owner: Mongolia
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 41,26:
            - Owner: Mongolia
            - Route: Railroad
          - Grass Hills 42,26:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 42,25:
            - Owner: Byzantium
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
        
        ### 190
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 17647
        - Player: 6: Germany
        - Plains Hills 39,22:
          - Owner: Byzantium
        
        ### 191
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 18452
        - Player: 6: Germany
        - Plots:
          - Grass Hills 36,25:
            - Owner: Germany
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 37,25:
            - Owner: Germany
            - Improvement: Fort
            - Route: Railroad
          - Plains Land 38,24:
            - Owner: Germany
            - Resource: Ivory
            - Improvement: Camp
            - Route: Road
          - Plains Hills 38,23:
            - Owner: Byzantium
            - Improvement: Mine
            - Route: Road
          - Plains Hills 39,22:
            - Owner: Byzantium
        
        ### 192
        - Type: CombatResult
        - Grass Hills 43,22:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Citadel
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 15
          - Damage: 30
          - Player: 3: Spain
          - Unit:
            - Level: 3
            - Health: 88%
            - AI: Defense
            - Unit: Infantry
            - ID: 21075
        
        ### 193
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 19626
        - Player: 6: Germany
        - Plots:
          - Plains Land 38,24:
            - Owner: Germany
            - Resource: Ivory
            - Improvement: Camp
            - Route: Road
          - Grass Hills 39,24:
            - Owner: Mongolia
            - Resource: Sheep
        
        ### 194
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 18206
        - Player: 6: Germany
        - Plots:
          - Plains Land 38,29:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Manufactory
            - Route: Road
          - Desert Hills 39,28:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Landmark
            - Route: Road
          - Plains Hills 39,27:
            - Owner: Mongolia
            - Improvement: Fort
            - Route: Railroad
          - Grass Hills 40,26:
            - Owner: Mongolia
            - Improvement: Mine
            - Route: Railroad
        
        ### 195
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 18897
        - Player: 6: Germany
        - Plots:
          - Desert Land 41,29:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 41,28:
            - Owner: Mongolia
            - IsRiver: true
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
          - Plains Hills 41,27:
            - Owner: Mongolia
            - Route: Railroad
          - Grass Hills 42,26:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 42,25:
            - Owner: Byzantium
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Plains Land 43,24:
            - Owner: Byzantium
            - IsRiver: true
            - Resource: Oil
            - Improvement: Ordo
            - Route: Railroad
          - Grass Land 42,23:
            - Owner: Byzantium
            - IsRiver: true
            - Resource: Deer
            - Improvement: Camp
            - Route: Road
            - Feature: Forest
        
        ### 196
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 20189
        - Player: 6: Germany
        - Plots:
          - Plains Hills 39,27:
            - Owner: Mongolia
            - Improvement: Fort
            - Route: Railroad
          - Grass Hills 40,26:
            - Owner: Mongolia
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 41,26:
            - Owner: Mongolia
            - Route: Railroad
          - Grass Hills 42,26:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 42,25:
            - Owner: Byzantium
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 42,24:
            - Owner: Byzantium
            - IsRiver: true
            - Route: Railroad
          - Plains Hills 41,23:
            - Owner: Byzantium
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
        
        ### 197
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 20188
        - Player: 6: Germany
        - Plots:
          - Plains Land 38,29:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Manufactory
            - Route: Road
          - Desert Hills 39,29:
            - Owner: Mongolia
            - IsRiver: true
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
          - Desert Land 40,30:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 41,30:
            - Owner: Mongolia
            - Improvement: Fort
            - Route: Railroad
          - Desert Land 41,29:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 41,28:
            - Owner: Mongolia
            - IsRiver: true
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
        
        ### 198
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 21037
        - Player: 6: Germany
        - Plots:
          - Coast 12,33:
            - Owner: Germany
          - Coast 11,33:
            - Owner: Germany
            - Resource: Fish
            - Improvement: Fishing Boats
          - Ocean 10,33:
            - Owner: Germany
          - Coast 9,33:
            - Owner: Germany
        
        ### 199
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 79%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19088
        - Player: 6: Germany
        - Plots:
          - Ocean 32,3:
            - Owner: Byzantium
            - Feature: Ice
          - Ocean 32,4:
            - Owner: Byzantium
        
        ### 200
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 77%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 18896
        - Player: 6: Germany
        - Plots:
          - Ocean 33,30:
            - Owner: City-State Rio de Janeiro
          - Ocean 33,29:
            - Owner: City-State Rio de Janeiro
          - Coast 34,28:
            - Owner: Germany
          - Coast 34,27:
            - Owner: Germany
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 35,26:
            - Owner: Germany
          - Plains Hills 36,26:
            - Owner: Germany
            - CityID: 13676
            - Population: 22
            - City: Cordoba
            - Religion: Eastern Orthodoxy
            - Route: Railroad
        
        ### 201
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 42%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 18959
        - Player: 6: Germany
        - Plots:
          - Ocean 32,9:
            - Owner: Byzantium
          - Ocean 33,8:
            - Owner: Byzantium
          - Ocean 33,7:
            - Owner: Byzantium
          - Ocean 34,6:
            - Owner: Spain
          - Coast 34,5:
            - Owner: Spain
        
        ### 202
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 56%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 18716
        - Player: 6: Germany
        - Plots:
          - Ocean 33,10:
            - Owner: Byzantium
          - Ocean 33,9:
            - Owner: Byzantium
          - Ocean 34,8:
            - Owner: Byzantium
          - Ocean 34,7:
            - Owner: Spain
          - Ocean 35,6:
            - Owner: Spain
          - Coast 35,5:
            - Owner: Spain
        
        ### 203
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 72%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 18715
        - Player: 6: Germany
        - Plots:
          - Coast 41,4:
            - Owner: City-State Colombo
            - Resource: Fish
          - Ocean 40,5:
            - Owner: Spain
          - Ocean 41,6:
            - Owner: Spain
          - Ocean 40,7:
            - Owner: Spain
          - Ocean 39,7:
            - Owner: Spain
        
        ### 204
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 84%
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 17923
        - Player: 6: Germany
        - Plots:
          - Ocean 33,24:
            - Owner: Germany
          - Ocean 33,25:
            - Owner: Germany
          - Coast 34,25:
            - Owner: Germany
          - Grass Hills 35,25:
            - Owner: Germany
            - Improvement: Fort
          - Coast 35,26:
            - Owner: Germany
          - Plains Hills 36,26:
            - Owner: Germany
            - CityID: 13676
            - Population: 22
            - City: Cordoba
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Plains Hills 36,27:
            - Owner: Germany
            - Resource: Jade
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Hills 37,27:
            - Owner: Germany
            - IsRiver: true
            - Resource: Iron
            - Improvement: Mine
            - Route: Road
        
        ### 205
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 19%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 18666
        - Player: 6: Germany
        - Plots:
          - Coast 37,9:
            - Owner: Spain
          - Coast 37,10:
            - Owner: Spain
        
        ### 206
        - Type: RebaseTo
        - Player: 6: Germany
        - Unit:
          - Level: 3
          - Health: 77%
          - AI: AttackAir
          - Unit: Bomber
          - ID: 17786
        - Plains Land 18,35:
          - Owner: Germany
          - CityID: 1247
          - Population: 29
          - IsRiver: true
          - City: Hamburg
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 207
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 77%
          - AI: AttackAir
          - Unit: Bomber
          - ID: 17786
        - Player: 6: Germany
        - Plains Land 18,35:
          - Owner: Germany
          - CityID: 1247
          - Population: 29
          - IsRiver: true
          - City: Hamburg
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 208
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 6: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3316
        - Build: Construct a Farm
        - Grass Land 19,27:
          - Owner: Germany
          - IsRiver: true
        
        ### 209
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 6: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4566
        - Build: Construct a Farm
        - Grass Land 19,29:
          - Owner: Germany
          - IsRiver: true
        
        ### 210
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4302
        - Player: 6: Germany
        - Grass Land 16,26:
          - Owner: Germany
          - CityID: 1424
          - Population: 28
          - City: Munich
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 211
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4701
        - Player: 6: Germany
        - Grass Land 12,27:
          - Owner: Germany
          - CityID: 3600
          - Population: 24
          - City: Cologne
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 212
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 13677
        - Player: 6: Germany
        - Plots:
          - Grass Hills 13,27:
            - Owner: Germany
            - Improvement: Fort
            - Route: Railroad
          - Plains Land 14,28:
            - Owner: Germany
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Hills 14,29:
            - Owner: Germany
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 14,30:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Desert Land 13,31:
            - Owner: Germany
            - CityID: 4137
            - Population: 27
            - IsRiver: true
            - City: Frankfurt
            - Resource: Wheat
            - Religion: Eastern Orthodoxy
            - Route: Railroad
        
        ### 213
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 20973
        - Player: 6: Germany
        - Plots:
          - Plains Land 16,27:
            - Owner: Germany
            - Improvement: Fort
            - Route: Railroad
          - Grass Hills 17,28:
            - Owner: Germany
            - Improvement: Town
            - Route: Railroad
          - Grass Land 17,29:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Grass Land 18,29:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 19,30:
            - Owner: Germany
            - CityID: 1063
            - Population: 39
            - IsRiver: true
            - City: Berlin
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Coast 20,30:
            - Owner: Germany
            - Resource: Pearls
            - Improvement: Fishing Boats
          - Coast 21,30:
            - Owner: Germany
            - Resource: Pearls
            - Improvement: Fishing Boats
        
        ### 214
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Defense
          - Unit: Infantry
          - ID: 18581
        - Player: 6: Germany
        - Plots:
          - Plains Land 15,14:
            - Owner: Byzantium
            - Resource: Wheat
            - Improvement: Aplekton
            - Route: Railroad
          - Plains Hills 16,14:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 16,13:
            - Owner: Byzantium
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
          - Grass Land 17,12:
            - Owner: Byzantium
            - Resource: Cattle
            - Improvement: Pasture
            - Route: Railroad
          - Plains Land 17,11:
            - Owner: Byzantium
            - Improvement: Aplekton
            - Route: Railroad
          - Plains Land 18,10:
            - Owner: Byzantium
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 19,10:
            - Owner: Byzantium
            - Resource: Wheat
            - Improvement: Aplekton
            - Route: Railroad
          - Plains Hills 20,10:
            - Owner: Byzantium
            - Improvement: Village
            - Route: Railroad
          - Plains Land 21,10:
            - Owner: Byzantium
            - Resource: Coal
            - Improvement: Academy
            - Route: Railroad
          - Desert Hills 21,11:
            - Owner: Byzantium
            - Improvement: Village
            - Route: Railroad
          - Coast 22,11:
            - Owner: Byzantium
        
        ### 215
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 80%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 18714
        - Player: 6: Germany
        
        ### 216
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 77%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 18958
        - Player: 6: Germany
        - Plots:
          - Ocean 24,27:
            - Owner: Germany
          - Coast 22,25:
            - Owner: Byzantium
          - Coast 21,25:
            - Owner: Germany
          - Ocean 20,25:
            - Owner: Germany
        
        ### 217
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 82%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 15154
        - Player: 6: Germany
        - Plots:
          - Plains Land 27,30:
            - Owner: Germany
            - Improvement: Fort
          - Coast 27,31:
            - Owner: Germany
          - Coast 27,32:
            - Owner: Germany
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 26,33:
            - Owner: City-State Warsaw
          - Coast 26,34:
            - Owner: City-State Warsaw
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 25,35:
            - Owner: City-State Warsaw
        
        ### 218
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 86%
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 20603
        - Player: 6: Germany
        - Grass Land 15,24:
          - Owner: Germany
          - Improvement: Farm
        
        ### 219
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 18398
        - Player: 6: Germany
        - Plots:
          - Grass Land 15,23:
            - Owner: Germany
            - Improvement: Fort
          - Grass Land 14,23:
            - Owner: Germany
            - Improvement: Academy
        
        ### 220
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 19965
        - Player: 6: Germany
        - Grass Land 16,23:
          - Owner: Germany
          - Improvement: Farm
        
        ### 221
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 18205
        - Player: 6: Germany
        - Plots:
          - Coast 21,29:
            - Owner: Germany
          - Coast 22,30:
            - Owner: Germany
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 21,31:
            - Owner: Germany
          - Desert Hills 21,32:
            - Owner: Germany
            - Improvement: Fort
        
        ### 222
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 18325
        - Player: 6: Germany
        - Plots:
          - Grass Land 16,23:
            - Owner: Germany
            - Improvement: Farm
          - Grass Land 15,23:
            - Owner: Germany
            - Improvement: Fort
        
        ### 223
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 18540
        - Player: 6: Germany
        - Plots:
          - Plains Land 19,31:
            - Owner: Germany
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 19,30:
            - Owner: Germany
            - CityID: 1063
            - Population: 39
            - IsRiver: true
            - City: Berlin
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Grass Land 19,29:
            - Owner: Germany
            - IsRiver: true
        
        ### 224
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 18718
        - Player: 6: Germany
        - Plots:
          - Plains Land 20,32:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 20,31:
            - Owner: Germany
            - Improvement: Mine
        
        ### 225
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 18719
        - Player: 6: Germany
        - Plots:
          - Grass Land 19,28:
            - Owner: Germany
            - Improvement: Farm
          - Plains Land 18,28:
            - Owner: Germany
            - Improvement: Fort
        
        ### 226
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 19083
        - Player: 6: Germany
        - Plots:
          - Grass Land 19,28:
            - Owner: Germany
            - Improvement: Farm
          - Grass Land 20,28:
            - Owner: Germany
            - Improvement: Manufactory
        
        ### 227
        - Type: PlayerDoneTurn
        - Player: 6: Germany
        - NextPlayer: 22
        
        You, Bismarck (leader of Germany, Player 6), are making strategic decisions after turn 458.
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
    - You are Bismarck, leader of Germany (Player 6).
      
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
      - Name: Germany
      - Uniques:
        - Unique Unit: Landsknecht, Replacing Tercio (Requires technology: Gunpowder)
        - Unique Unit: Krupp Gun, Replacing Artillery (Requires technology: Replaceable Parts)
        - Unique Building: Hanse, Replacing Customs House (Requires technology: Guilds)
        - Unique Building: Brewhouse, Replacing Windmill (Requires technology: Economics)
        - Civilization Ability: Gain +1 Influence per turn with City-States for each gifted Unit (lost when killed). -15% Production and Gold costs for Military Units.
      - Leader: Bismarck
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
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      - Mobile Tactics: Allows you to build the Mechanized Infantry, a fast and versatile late game Unit that doesn't require any resources.
        Completing it would unlock: Stealth
      - The Internet: Increases Tourism output of all cities by 50%, helping you advance toward a Cultural Victory.
        Completing it would unlock: Nanotechnology, Particle Physics, Globalization
      
      ## Policies
      - Elite Forces (Level 1 Tenet of Ideology Autocracy): Elite Forces: Newly created Military Units receive +15 Experience. Military Units gain 50% more Experience from combat.
      - Futurism (Level 1 Tenet of Ideology Autocracy): Futurism: Strengthens Tourism of Historic Events generated by the Palace. +2 Culture from Great Works. Earn 50 Tourism when you conquer a city for the first time, scaling with Era and city size.
      - Lebensraum (Level 1 Tenet of Ideology Autocracy): Lebensraum: Receive 10 Culture and Golden Age Points when your borders expand, scaling with Era. Citadels may also be built in foreign territory adjacent to your borders. Retain tiles after razing Cities.
      - New World Order (Level 1 Tenet of Ideology Autocracy): New World Order: -2 Unhappiness from and Distress in all Cities. Police Stations and Constabularies provide +3 Culture and +5 Production, and are constructed 100% more quickly.
      - Shadow Networks (Continuing Statecraft Branch):
        - * Receive 25% of Science generated by Allied City-States.
        - * +3% Culture in Capital for every 100 Spy Points ever accumulated (up to 30%).
        - * +3 Science from Constabularies and Police Stations.
        - * +1 Science from Specialists.
      - Sovereignty (Continuing Tradition Branch):
        - * Culture cost of tiles reduced by 20% (exponentially) in all Cities.
        - * Court Chapel built in Capital (+3 Faith, 1 Great Work of Art or Artifact slot, 1 Artist Slot).
      - Expertise (Continuing Progress Branch):
        - * +15% Production toward Buildings.
        - * Cities earn +10 Culture when they construct Buildings, scaling with Era.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Civilizing Mission (Continuing Imperialism Branch):
        - * Retain all buildings from conquered Cities.
        - * Receive 75 Gold when you conquer a city, scaling with Era and City Population.
        - * +10% Production toward Buildings, with an additional +10% Production per Era difference between your current Era and the building's Era in all Puppeted Cities and Cities with a Courthouse.
      - Free Thought (Continuing Rationalism Branch):
        - * -5 Unhappiness from Religious Unrest in all Cities.
        - * +25% Instant Yields from Great Scientists.
        - * Earn Great Scientists +33% faster.
      - Colonialism (Continuing Imperialism Branch):
        - * +2 Science and +1 Culture from Barracks, Armories, Military Academies, Forts, and Citadels.
        - * Each unique Global Monopoly modifier is increased by an additional 10% if it's percentage-based, or +3 otherwise.
      - Imperium (Continuing Authority Branch):
        - * Cities gain 20 Production and Gold when their borders expand, scaling with Era (40 if all Authority policies are adopted).
        - * Receive 40 Science and Culture when you found or conquer Cities, scaling with Era. Conquest bonus also scales based on City population.
      - Nobility (Continuing Fealty Branch):
        - * +1 Happiness and +2 Gold from Castles.
        - * +2 Gold from Armories.
        - * +100% Production towards Castles and Armories.
      - Dominance (Continuing Authority Branch):
        - * All Melee Units gain the Endurance Promotion (Heal 15 HP after defeating an Enemy Unit).
        - * +1 Production in every City for every 10 Military Units in Empire.
        - * +5 Military Supply.
      - Industry (New Branch):
        - Industry provides bonuses to empires focused on Gold and Production.
        - Adopting Industry grants:
        - * +2 Trade Routes.
        - * -5% Gold needed for purchases.
        - Each Industry policy unlocked grants:
        - * -5% Gold needed for purchases.
        - Adopting all Policies in Industry grants:
        - * Unlocks building Broadway.
        - * +3 Happiness per unique owned Luxury Resource.
        - * +2 Production and Gold from Specialists.
        - * Allows for the purchase of Great Merchants with Faith starting in the Industrial Era.
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
        - Policy: New World Order
        - Rationale: Our empire is suffering from severe unhappiness (44% happiness), which imposes a heavy combat penalty. Selecting 'New World Order' will immediately reduce unhappiness from Distress and provide flat unhappiness relief in all 9 of our cities, restoring our empire's productivity and combat effectiveness.
    - #1:
      - toolName: set-research
      - args:
        - Rationale: Advanced Ballistics is a crucial late-game technology that unlocks the Nuclear Missile for strategic deterrence, the Guided Missile, and the SS Booster. This supports our long-term defense and technological parity with advanced civilizations like Byzantium and America.
        - Technology: Advanced Ballistics
    - #2:
      - toolName: set-flavors
      - args:
        - GrandStrategy: UnitedNations
        - Flavors:
          - Culture: 100
          - Diplomacy: 100
          - Mobilization: 80
          - Happiness: 100
          - Espionage: 90
          - Gold: 100
          - Production: 100
          - Offense: 50
          - MilitaryTraining: 70
          - Science: 80
          - Defense: 80
      - rationale: We are shifting our Grand Strategy to 'UnitedNations' to address the imminent threat of a Byzantine Diplomatic or Cultural victory. Maximizing Diplomacy and Gold will allow us to leverage Germany's unique traits (gifting units and Hanse trade routes) to contest city-state alliances and block Byzantium's delegate count. We also maximize Happiness and Culture to combat our low happiness and build defenses against Byzantium's massive tourism.
    - #3:
      - toolName: set-persona
      - args:
        - Loyalty: 10
        - Friendliness: 7
        - VictoryCompetitiveness: 10
        - HostileBias: 8
        - MinorCivCompetitiveness: 10
        - MinorCivFriendlyBias: 10
        - Rationale: Adjusting our diplomatic persona to highly prioritize city-states and victory competitiveness. This aligns with our pivot to a United Nations diplomatic defense strategy, ensuring we aggressively contest city-states while maintaining strong alliance loyalty with Mongolia.
        - Meanness: 7
        - Boldness: 7
        - DeceptiveBias: 8
        - WarBias: 6
  - tokens:
    - inputTokens: 68611
    - reasoningTokens: 6504
    - outputTokens: 407
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Situation**
            
            I'm reviewing our current standing as Germany. We're on turn 458, playing on Prince difficulty, and deep into the Information Era. With nine cities, a score of 2214, and Sat as our current research focus, I'm assessing our strategic position.
            
            **Assessing Threats and Opportunities**
            
            My focus is on the imminent cultural victory threat from Byzantium. They are one turn from influencing Austria, which will secure them the win. I'm also weighing the strategic implications of their dominance and the potential for our own conquest victory against Mongolia.
            
            **Evaluating Immediate Threats**
            
            My analysis is now zeroing in on Byzantium's imminent cultural and diplomatic victories. They are one turn from influencing Austria for culture and are poised to win the diplomatic vote in six turns. I'm also urgently re-evaluating our open borders agreement with them.
            
            **Developing Countermeasures**
            
            I'm exploring ways to disrupt Byzantium's victory, realizing direct deal cancellation isn't an option. Adjusting our diplomatic stance and grand strategy is key. While our military is outmatched by Byzantium and Austria, our existing wars and pacts present a complex landscape to leverage.
            
            **Disrupting Byzantine Victory**
            
            Byzantium has secured influence over all other civs, bringing them a diplomatic victory within six turns via "Global Hegemony." I'm strategizing to counter their delegate count by leveraging city-states and considering peace with Spain and Austria to bolster our defense or military.
            
            **Researching Advanced Ballistics**
            
            I've decided to prioritize researching Advanced Ballistics. While The Internet offers a tourism boost, it doesn't align with my current strategic goals. Advanced Ballistics is more critical for our military and scientific advancements.
            
            **Considering New Policies**
            
            I am currently reviewing available policies, noting that "Lebensraum" is next. I need to evaluate options like Elite Forces, Futurism, New World Order, Shadow Networks, and others to determine the most beneficial policy to adopt.
            
            **Evaluating Policy Options**
            
            I am reconsidering our next policy choice. While Lebensraum is next, New World Order's significant happiness boost appears far more impactful given our current unrest and combat penalties, potentially outweighing other tactical advantages.
            
            **Adopting New Policies**
            
            I'm shifting our policy focus to "New World Order." The substantial happiness boost it provides will be crucial in mitigating our current unrest and combat penalties, significantly outweighing the benefits of "Lebensraum."
            
            **Conquering Spain**
            
            I'm focusing on Spain, given their extremely weak military. With our superior forces, I plan to push them, aiming to capture key cities like Madrid or Barcelona, or perhaps secure a swift peace or vassalization. Their current defenses are laughably inadequate.
            
            **Leveraging Unique Abilities**
            
            I'm realizing our Germany ability to gift units for city-state influence is a critical diplomatic tool. This will be key to countering Byzantium's growing diplomatic advantage and securing city-state support.
            
            **Securing City-State Delegates**
            
            I'm prioritizing leveraging Germany's unique ability to gift units. This will be crucial for bolstering our alliances with key city-states like Warsaw and Kabul, securing vital delegates to counter Byzantium's diplomatic push and secure our own standing.
            
            **Securing City-State Delegates**
            
            I'm focusing on strategically gifting units to city-states like Manila and Huari to disrupt Byzantium's delegate count. This leverages our unique German abilities to counter their impending diplomatic victory and secure crucial city-state support.
            
            **Boosting Culture Defense**
            
            My current focus is on bolstering our cultural defenses. Byzantium's tourism is overwhelming, and I'm evaluating how to increase our own culture output to counter their imminent cultural victory.
            
            **Shifting Grand Strategy**
            
            I'm realizing that switching our Grand Strategy to "UnitedNations" is a critical pivot. This aligns perfectly with Germany's strengths, allowing us to leverage our Hanse and gifted unit bonuses to maximize gold, production, and diplomacy, essential for winning the delegate race and securing city-state alliances.
            
            **Adjusting Strategic Priorities**
            
            I am re-evaluating our core strategic flavors. The focus is now on maximizing `Diplomacy`, `Gold`, `Production`, `Happiness`, and `Culture` to counter Byzantium's victory, while maintaining strong `Espionage` and `Defense`, and a moderate `Offense` against Spain.
            
            **Prioritizing City-State Competitiveness**
            
            I'm focusing on ensuring our persona prioritizes competitiveness with minor civs and maintaining strong friendliness or loyalty with Mongolia. The current aggressive settings seem suitable for Germany, so I'll confirm those priorities without needing drastic changes, ensuring we maximize our diplomatic leverage.
            
            **Setting Relationships**
            
            I'm solidifying our relationships. I've ensured our rivalry with Byzantium and our war status with Spain and Austria remain at the lowest possible setting, while maintaining our strong alliance with Mongolia. These extreme values are crucial for our strategic positioning.
            
            **Adopting New World Order**
            
            I'm finalizing the adoption of New World Order. This policy's significant happiness boost is critical for alleviating current unrest and combat penalties, making it the optimal choice over Lebensraum. I've also confirmed our relationship standings are already set advantageously.
            
            **Verifying Policy and Research**
            
            I'm confirming "New World Order" is indeed an available Autocracy tenet, and it appears it provides significant happiness and city yields. My research focus will shift to "Advanced Ballistics," a strong strategic choice for our Autocracy ideology and technological advancement, rather than "The Internet."
            
            **Shifting Grand Strategy**
            
            My thoughts are now focused on pivoting our Grand Strategy to "UnitedNations." This aligns with Germany's strengths, maximizing gold, production, and diplomacy to contest delegates and secure city-state alliances, crucial for thwarting Byzantium's victory. I will also set research to "Advanced Ballistics."
            
            **Optimizing Persona and Flavors**
            
            I'm fine-tuning our strategic flavors, prioritizing Diplomacy, Gold, Production, Happiness, and Culture to counter Byzantium, while maintaining strong Espionage and Defense. I'll also adjust our persona to excel in city-state competition and solidify relationships, ensuring our rivalry with Byzantium is at its lowest setting.
            
            **Adopting Optimal Policy**
            
            I'm confirming "New World Order" as our chosen Autocracy tenet. This choice is critical for its substantial happiness boost, directly addressing our severe unhappiness and combat penalties, and will immediately restore our empire's productivity and combat effectiveness.
            
            **Refining Persona Settings**
            
            I am fine-tuning our persona to excel in city-state competition and victory aspirations. I've adjusted values like WarBias and HostileBias to better align with our current diplomatic and strategic goals, ensuring we maximize leverage and maintain strong alliances where needed.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: cKb2gTZAKzYtZWoS
          - toolName: set-policy
          - input:
            - Policy: New World Order
            - Rationale: Our empire is suffering from severe unhappiness (44% happiness), which imposes a heavy combat penalty. Selecting 'New World Order' will immediately reduce unhappiness from Distress and provide flat unhappiness relief in all 9 of our cities, restoring our empire's productivity and combat effectiveness.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a18RI/rvup5x0uq4pPz74ap2NY7cemty8iF/OY6KTZcZ+c22NQ3RdkTcoUcxwsIx4YBHkohlbkGPU5OzFOeejm0R4gjXTJD3hTSwm5Ax8Fgxtd67tCN/avrHjlD+eA9e2BlNMA3mubVHNjtS1lwrKVJp89Lz1nY//1Y4NsNXVan51eniKKtewJM5B4tBid45U6eCoUkIT9Zu6L3CZbvMM7zLF6gGRUjR8rh+UlpEAXW6vVuz7W+Px9Y1JEYInJ+d+LqD3/LMVG0QIh9QzA4v/LmGDIk7L4qW4z/8LXnSN3/ZrjSLo3M3yPiWpQQXhif5q69EBRoGbvr3eBad7hs1foI2GUpwZW2lB9QmMm/sd4eo34ccq4suVUCe8MdhkKNMtF4XBXjRLHvQmZD9AxuXy2zXoL9tl65LfymmwLOXNd+XjfqEzFbhosFsbB4aWWwz3P2zCmS1kd+M7nSPF1T6xJuOUeDjBJ81mP80Hpqueuh2nTz+ElOr9NVEtEoLU/0Mlfj7Tynt8Xlsko/NkfjJ78X+JBgsHvSJHsnXC6AHXCsAP2WKoSq/rwXjb3yugpDN6WJkKvtsltxDjEJR2Hbi7jCLZy53fDXEFe9wjuIC1fzooMQTUShrMRUPX3QiOnW5gwC7DQaeijXQryf+awtqJYlTJ9tK2tdOz2z1Nz+0dxhwjBjDGzCG7mntH8fzZ73YCqrDw0C/ukvFR+NHttH0Kzx2cc6Y53NCGgsH3/S9GoiF573vqjbLH03iDyjmQjsiGpi7su5Wx4hH88hsOQ26Rg1VXM6u+xxK3b+BxkJN5v8XR2d8kPqlIDq1OsK3HZsEBwG3kvbtH/E4N/eNCR8O3KRi99wHBfpp8R1z6X+ofc/nPhulSeZNJIZxb02EmE9T76/bUXjPY0QOV58VdS74Vi0jfW+RafZt2qK01ppqBJzbCDJHpFkSZtTQYQKDZDv9GN+PKhm14MtMqoSiaq/jpO0XeJEbnkt6YzPN/FfEkZZ3aJHOOA9CECoHiFx2GZyojXUy60MiuQduiGIbsAqlxVJr6T9RzG1GBO+oRVDxzb/GEMMEGucabu1m/Gi7KKivDlNEafQ+AAWYJoUGtPpMRCwjgczWibSJyNgJJbXwZ/bfYlyZgDcdnblB5U98ohBF6/rJl3mIIKggAXn0tbpBUomw/wqG3/Qmq4PMtODkmpA4bxMVVQCrms87YHNCmf71vuaKIce1Her7cUxD68lWbnGzSoRhfHzP+NEieMLmZR81CIFF8uggRRbT2tEFgaYisrmqsH7Pl8vfATeohOyCX16nfFTtm3secyUhmrx6L19kpnqJPKvWc1awESUYKnIjPqIEqBKjCHphGhfCcYNYOdt2+QaTcwpFQ51PaPoEIEH+KLwVoBkKlswL7XmgIkRXK8jjB5IciLOuIdK2yby8tF2BqcMUIuXuBx2V84EPbPU/SJyIUw3Lag04c0iGE7QsUXnVYWT2bK3dykMJh7CAC9/f3aYVSqTDSPIH/w/cORuI/iVAfeXAEkUiZxxzPUpUwlpTLUJtET2Vv5pjthgzjX7Hxbctwd6A4ct3e72ct3Kaek/d6gJSeYGg7l4RNSpmfYtB66RcfkYx3TL5zv7atymYns1GHwwId8bn0IR9vuv4SmSV1outTsYXzFthTMKFZu4AlgZF3Tpvjar7enOkvXSKcPZ4PDXABT/PGiaddFeV+HKD8O4ZAC8d9xpjjw5VPZzLQpezUSC7WjKy816AhY6J42HKTE0Dsi41PV4CE3Zx+F2yweoxbkngU2I7A5TsWQucqgjmd1WRjRCJ5zg4gaigxFEArTOnvp+hm/xJyGsQbk5WeHjhTd2QOj9QacOWYSwUdadn6l5NhV0Elw7LDoD98WPvm8+xxFlRaHOtqJX9PPS2yu2HwJvSix5WPIe4NJYrzlEwN/GAInkpsVWGn39hvLovWpl/5wA9g8omsXv1kcdkcOL4i5OC3y6vo/IoXIFQ9+TEAs21akZbMtdeoVFJWJsi0m5OlWeFjySq6Ikkmg1oE2BDujrRVA6untr6g/+M2FuimQJZGzP+vRcMLvKK9maFu474RLpnUT+F2aFmB8Y9e+S4Qv3Y/337g8pNxFszxWWp0XB/E63uZtiwqY36oF9i603R258s8d5DpPHV/EebslIIHNeo9a4LSmUsAlaKduc9ljJinly2bLNCIBl5Ei6bKqvuZOQ4SXfrdhzvNPszyDSh2L0v4jFgXAiGs5wBF0KeGuXwkTdz5XgoWT8dMygYYhHgAJYGH20ilntJYpRWYr/KnXkdB07aeQLNRl9ArreL6Q2VDyGIHPjWrWYPwHoAYCENDafrfPP2CYZ9szMvay55b/HXYih5KB2sOFMyp/MuZYvlSDYk/bctLnQhwIYxkqLAspoDN5KEh4F8GR03U0MnvQ1qKpOz+roJpUiQytAdVAlAx6H7rbjQy+M+DK/vrS6q4MuGEkF3NyDuZbNGfVZw2HQ8eda+rGHMS/vIG93dxO0QBi08PsyZ3AYTXTbK1w0t8EQxHnz+Rpb0hH72eIAVPdby33D5fwqXDp66n+HxgrpSl+8/9aM0Q0wJe7lO55f7kpWbn9bLBaWaPSP9SNNE6OpovGIrGWx1VexEBVxW5MvcsEFQjBRXIqm+9QDPc78l2UjjavTthqPkzZeKza/M/KmuolThjqRruL0NxaF3p147/iU2e2ilvsC3CWCYcrD7sK0odPAovBR3K9+bKCRtGpeKjqnrwzrho/Qx0IshN3fzumxsFb1M9lkn+Lrw4STjjDWMSMM/KUjZ9FgN6gcNQMgAcuiBg2njAOjDlbUxLVHevG6xbuMlLtlULvLBbHyPeBzeuTVFvIQr+tL9aTabaRC3sO0ElmQP1hCXZXnMm6ojcRjmRi2QMfiDPwRub9BmQzTJ/fUGJvwYJ4eGthjqeReta63FgU4VoFDln2qvRbjqyqGUsOhKdUgAqmpl0etpjAo7CcR5+LxHeQqIBwpl9sHF8eHZxVlisHRpaPh8lxg6BMfUH66jLVfjaXpo5NlRvvwpzEodo7KyceYH+Xw9eOilEh1LxkatZCwI2NQhv9r3RHn5dh6zoJzmhxqWP4Fqf9yhWohDMyqXNJJ1Z97ReewZL2FMrB/I/hiNQGuR7QIQZFwwYD1bUb1aXRr1etHV/Tuchj9CBlIU60HAnRB7At4xIP0S5hxloZGR0iFLEgi59ywfE5mDMQkVbA8kqVGVgLaE4JTqQs16hjJ5BEY+zhYAWwreMgKW+9SD9nhUXSOKdqArmGhtzB3ylnR0jhHFJsDtQWwe4B36J+lWaShThQrKLKj8YlfJ8PNKIt4awspLRy3M7cYG893p+J5kIAG843BA4y8b0BbCVgwqAqjdiFnwgvRSYwblpGJo3bxgMlG8lYJCckI2PyiSjYHspPnzT7A69MMeyzCI6ZwyPSv9Pvvhrtu35LIkE+5MWQ9Av3KWQJ68S9Zjeg7PbE9hILCLy8qpN640n2QkUk8mbXOrTu8trh4/keRF5N/qXkSb7BZDLyiLACKGZ6QEhRuwC7f0ZR393tv2+4gkxq+AoYNKh47kCo7GIygO2MUrojLoMPipzGoYg7+huKaZNqMocrfjJmB+KFq0Ea0s8ZrskRehd0rUE/HCYnUcZi1AMR8dgTTicTajt7zF1a2ib9FuJL0PS5aSl2+jLaTTTCezv5lzq3qowe1DaY6eGrsBj35MtOWsWej0TYBMh+90kxJHtB1KKdGlP/tKHXA1aCAqX2mHuGRfiNFayPQ0ur42n4HvtA1ZmK9fxthXpftAGunKEKyfpivTjxLGgOcwY/Jl48DxlDvFDa7qERQkhYGBua3lg+64hsq+gwoOLVZ/RLRejvGLJdADHVOD+WF2+fqyFrRFyzepVkF4/3uh/yRTkuSYOCzxf5S/svpnqaOGsuCbgYy8X2EJgOtqtEv2C0RWYdca4aiZ6tUuAdacaWNJkDK0yzn3paXLWwhvXF/EttMzW4KtVbtK785SL3Um+EaFl+ulGmPEyWQ3dkvC6GGoObVHnG27gnhzHjXNzfC68TDGV4xxPLzUXSPMacVXWE82A6aLsyNwcYeH6RAehOtVCtQrvT/cg9x/pJ8hxaMoF5vvONR8bCa4TzrZARwotDSmwQ8yAYc/eBlD+i8EwyTlyrajZbhqE79m5ZC1DnEOuk1qjvslOClrDTfa+zs114rOWuhdze1GGtcbAILgDujKKpmrDRXcT9bFWvrq4TeHFBA9oLlrJXuh5bZeWzK6BzmFofJbyU8o5vE7czP//WR4ibrNfxyiAd+c86zq2b3bBTiseYsUY2DfuUNq2L9JV4szdwn69kiZRj69iciW3egxD1r5ksL/nmEou6sBJhXC6HB1hbSbOLYLS2Hv6xR/LcWN3b0XrrgKYEk+lZigiIoxBekojfzt4IyXAJbPf6ebfTEmV2OAKmlODo74S62r3Qw8jdf29lwmsjzLRr9uEIsBE/4qt7LTureMS0uEoEjejLBOeefFF9dAbwiJE9am+JAg8NkUjoKRtwaQAY0r80uwOqtXhbQNQ9gIDD0txdZoO91OjiyEsZ1X5B8eyy4Di1wCxXsxpGhocOn4Z1mMSLSE/pRJvV6XQnTErsjdRMBPua1Rht+Kn/JcVcWaoR7/TmvWWTs6AfWaGydC8AyiJr2Xo6kIczWEhCqpV1OZS0NUFKjocVl1/W0UDJzjwx7uu6ANSY99C0SsDLFk2EuWhDPhciN2IriITiQwfh5wAHB5sntdvub7LIJN7xxSpy8a+C7WcDXVa4Bpxch5bhNMBcKvx2UPb26zpt2aajMrf531u1NlzTO8PMtFNPTPt5EeVdvTNKvyDo0d97kmzui96oj/EJLvRG/15ajbFYT6wS8dIgBUbxv8gJ91NKrXxhYcOQHDXD5aZLPvL7oT5OvVTwVJyVfdPsUmLDLKbx2JWKypX4mLTc7yRiq8r1ksnu8dHTdzaLjTaRHtlWRWLFBl/5ssnaRADpiY/eT4qb9NjFZOUi3gbXm6AOrOcCFh3StuhtLgXI6CR+Xi/YFdoda0+DVS4/wznohlHfBPIYmgEvbKfOsfTZH2xHuE55/fZI34Q64iONeFDbJa1hKs+4pAuHCp1XA6HZ9t3hMNxlDPbykU69oEp33h7iGqeKptbP+sfJ82xgHz39hQ4fJy7cBKsZawPHG5AamGWQ9lRq0zd49ICFdEqR5Sh8BRA/neAITvMS3gVpdA0iTF+l2sScoqQuEr9uKAyo95rBeQh42q3TU9TN6EEO42YcxPm90t+Mrwk3P5oATnkr06wlCVRxP+tcppK97E7Ek5r5CME2711XwV1tL7gzYgZ3U9L5/duJvtx6EAE12k/327peC92UFML01WlPiPtAp5RlcNKWyZ9MHef+pKNCRZZKOUZ9ygDHztccYIa0WIQiDOG/VxRxzyEoeD6LbxqGTY1xvpOcZq4oHqgQzd8+hvVAfxaX6EDaLGgnAx13HLJvfHrht1EiRVb/G7MTaTwSPtIUt7YRCjDFQVfdn2U3hnMLoJrRpuVTq9HryUAdtvfLBVg7BfzrQOGC3It0ajr9um+EtaHD5suf9IRbhsfC7dp5vn288nLOXMp1FcPwIRuwhXA5S2NsM7t1FMADzeTi1IY1gPqocHdPlPCitAQNiva7kYYtEr77j7z0PBqY8dhid+nMJCIj/+ihybq0uXOtLydZPVNMG3YUM8KDGgE1Doi/JH/GKcq0dEYKrK2IdUQkMmN1PJkZ5ZLMIWHxCJGi9Fgwm7deBw2wHhEnmgr0mkPkHD/VDB5qihIUDJLu8J+e9YNLG9yaK9y5KjdxKoev7T4GK4JAhOO8c0FgJ+Uz3HS6wcCycLJCED2kQSJ0hQroy45onazxzZdt/cpXf09dPAzokaMKcrT9BziM9RLqys1opkz724Xg5Mlw4GRTwa2vs531b0ZqJtPFrF89h9G8VLCd1fRrEvhPkHkZW2CVbZfX8GDO81deSFQjzUMU+hzrhANvu2ZH8bfQ9+vLpZvib1iN591RB0pu9/tm0mFXZJrlVCg2otzkJ5yhuMEa6lCGdRRFhY3fbmKsBuedh8Ob8OgsdkJz34r5EOK+ayNgL0uk8kWV4pXrAmNgGVnkugrhgHVSC5T9jq9itFsuIgwbstlQvdSyqPAZhT3+j3xslT58xVY0zxBXaaALD9JwwNuUM/BLOk+ZOYY7AsbdGgDZaKQy/vDq85rn0Atrp8B2HVuyVEzoLnMpfyPjhm+a6meoBeYQRv0JRlfQyCQxJHGLi90GuuQBoa3CenGdJkl6bQIH9G9abWpZry+9s0pdRg9i73m3WDXedIlfMiE1YSTz0SWiU+2uxsxmOxLGOllkJB+6OFjjiVFNjMpHacD4m+wR138dFa7oUdQmr7eW3pA1Xu9FPesbUsLMdFtq9qgUcH6qYoD8BapnoHdxzYS7QNJJAYRh8n/oFA4J/cCoRFEsmNi3tJrdF9sPD/4M6IEVhyCj7R0TI2UrHFiVg/vagwW2FqWmWxzYKUNi6oPACLq0zRvq+0XKdhnhUvKpXX5do+ZDON1FCts37beWceI7KL28bTOQGro69V3hzO0QlN9EYdn6p/lQ4Wu+wlLGmOMSrG6z9rLaHa1jVZm5pCkt4cCjyc5PApz5tCcmNJ/98PpEk3Fx5pCtmvS/99k7CTGl1QYRrj+DYGujyPFMbnYGHE37lYLzbkGXLCa1/NaHaFW+46xQ4f9zu83i4cG6HJnh2HpGZ5QwNC8KqYUJwTHvqrsvnnuAg5z7fP51D51Wo3f4yOD9k0/rt9GatV+KurWdNVwzcfeEh9g7TEa3c4ypVXavocMpEZV1R+cqpyXg+7WFpGNZpeIXLn4CqUzmp8kd/wcKhuoBHXIqDfIXajTCEZNTcSRa2Ku6kAZpX8y6F/8gyhXDyPPx0TwgqCqv/4oRLGRiIG/l7zGPaQZefX1YGaESrHEzXGPJsSAZ5vj0rwVdF0WyaKYBnePHEAdkf0kw8ktk2Q3/H68boXvjIZ8XC1KO3Q4Hc35SbdMmM0sjMXbz7TfoxSPB9ZbV9Wg/53rpmUGLY6LeD0lj+YfcPZ0aBXKsr7ewgoWE2o5WErNNQFLhI8FT4bQen3r6vul7n+HAju4EL/FtnlX8iQePeHSkLaWSdO4+LGpqSnA2GY2yhOl5joSczQBJa4wXltgstx/LWrC5Uopg0N0JfwxpIZIS2BOH0dmFwLK/LgzTGcSyS4yUwsshk2iDNbkbb5AG5GKyL9RsINNQC9/MPMynaIKjttFtxJ5ksnIwhzIrpZRNfUl/bRCZQjKktTyPhPoO2a3I0oghBkgG+813dgVjIZ0/K9GXjrNOQTmj0mrSSoq8N2x+2U054QzdRXMGlOIwALTutmuc6MQW/riWOEnu2wxbdm+GCGTfYoTAZk6YtEpPdm0acyiU09cvNKC19v0tJJ8FDM7rhOWmRVYldt7TGkwV/173kYE7z+n2gw+Z4lzyQ7DMMY2/Vvn6mk8+9LgTUb7FenrkNlckzcF9Fp3rzIeO6jlCHHxDUH1C9PI8kH5gFlsZ26nhEUXccPJu5P09rWmdCDQIy4wU6yWvyGPEN2RrbUO4iGB913l5AEbL09zZHl+p8AiwF/F+5mFLcRKTZQWjjsxp677UXVDKQBjIDDf+b/EqljpMTr0Ugcvt1JAGajux087O1Y+udK1jG6BOir4FviUpiiyW0cDIBrX5IIDBjUtEZminNln1x9EAyL9Cmi38qfmEIdYBRRGwEwPpU3Tc1PT53aeVDUDH5Uu4TWTLnGG/f9iXFsLwRHwrYwyKozDZ6Jne0hmqoODtERQ24IUyL3mtr90xhOjvv9JYwUnekOydqiClzNdiPhjhoacysxlSuGQKPFPhSZgRjA1e4y4ealxeGAp39MsvSsEu+Jc+w5voGjvqF2iuPKKtt1qZwCUc50Cl24YA41vRg15nn7U34uiuvIAkJZ8SQbVEANMuPaYLxg4Aly3PLG9AEKHXZIoxE1ceCQbE9N2WpKuH8BxETtUxRB3unQM93jVVrl6Yy96t70QvSXx4J7CZwu7afMFVam+QMI2jzWNDsSuy4LpXB4uYwCCWFw+NL1Wb8uQfLMbMLFlMkXvujc0sS+cJhuukMLjaJkBNa26EPvfe7I5r5KI0a3cwqd2ELqy16xEif4FNUteif+1LERptUIVdeZT0imV+BUp2NafWIhTxlO9QLUIKHMGee4Hf+dShurapRjKFE0C2b9fmTMTQi02nZglv9woBrby2LyaOBKdt8LLK1/ekYB1WayharTLKO0Q7Fr1p/ZPbWlmpG3p40Qd+7zXXvm6XSdpw6afl0fx7GPZqe6W60JlcMwekUF6tAhtlbTb0CawB5M/DhCEuD+nwnfMly6xRNXwi/AJOg7e8CPW+8ufNwMhySbAYri9TeazbR4ZecLNr+I1aeUFaZAkScaADThbD56jWA0gQwDRCMDkY76wLTIXvTVdNaBQ0/LHDy/VlhJzNYnmxs6YLdFkFfdMbkCnZXL6Ml3spifuG0B+kVS/7ptERfMw+AmQD2nrLsb4yF2+56hEgF1Jil89teJ4wtm2p1MX2B24VwuFhRylDEDtYdjaGiRktLQnN0HdDM6bM1ksCzvVXYWmP72esGwJjPDlbFq4XKseYyfcxwcos7hWNLJ7Hm2fRGpLtZn4xGHjHbjT6iEBkwnp9BtZrUfIlZilDaGvEFiD7eG1SEp2P8VU/r6tiwZsfHcBJ+EWHOdzx+n+QUIsM3oXm5BboL52fgdryPIbFmwvz8uhmJVcJWvR6q/55eLMpuqRrmILEwcKUuRoPIcinFYNVYXGqEytexhJJMKjUqxlid0kcjQiAYbKvdplXiS+mlvj2DF1wCfgtnNPc75tjZHZ5CEl8/y6h32xxToG2Oua2qtB4/ATYr8tS86evp8eIQlZgD6BFRL8n0/tpkzT3XEcL5rhnZ0gLEbtqUwhoNr3bQOpOVHjKSQLiNg2NSv93DuCDQjUVgp/VR3QuZHIGqGfDhMJLZr0NIHpFvOChA29NIWNAZ8IHgnljpgj7KWF6t7Zg4V86mcjetvIpkmLCDh/K33NVBBsb4tlmNMrf1PfePdCVK6GJBDZZA4hOVFIM3Gv1x0vgDZt6mfn8tXO9HPKbEb3QFeDELUvkKkCC+APeXyU5LXMyfUcSSaEZUYFdEwPEBUZ/o1C8gfRYjr1QMMk0/acnyaKzFI+TM2WXDQ2bnNKYYXA6f9hPPNJz31RiZfrwUZmuFf09be+oCaeTDneptZo5LL3mfJUV/DSiK3vNWQyHhd1NWHA5NpE4ko7dseQ3boJwAxaBtjYbFbejNh9HSnrQ8Td2GmXMMnXaeY2oTX7xGNOSyJUz+EF0dBX3nD4JyV698484+1rmYB+i4L47HduASUnK0CbbPstCVCmAVKfvPl6E7B5gf3xq/r6GZ0eyxJQel1gRBzSXzYIPvDq6pn8tkRZLCz1v4eLG7JOEFCNyZPzQ85y9P+FvfGyzWaaZruZNUVKNOL2P6nr7VD0OqjpVGuKMq+Im3rcx2f29y8ApcpmoeKR2fnkFp8f3b/AoXua2Vx6FqKWKFy1ZQcp4z9S/TRLqxOyXIXxesL2XmxyqD6WAzj4Qt27kmAv4r+d1y2OXm4skisTQAelilcYXWZH6sQkNq2/dg9lncPF+vxCnnCUVA5m9Hq4ItE8Ci7yq0bDyrzlLH8JcT2GBQovbCikTat+ytMhZDIIcKBeYPXC2Z6uSyMAw3L4+ZXgJyf6E7uag5iJc/UKdIGXJ/JyRyA/X/fp46F3kfiRgXVbdHle0PB4juBQwnmAhtX8VTBqzxqCwi4plNY1SIUJMQv3wALGali4UAg32uVhpxAJAyEt3Bb9vWHhm7+D+PNTAoXmlsawBq4GpS4M9DhpKgqvyT0+nW421iDMqxjDihXpHRJ10VUj+D8nCCJIEtTNwsLo6GibjILunYjRszkcDonNnOLQZ7Jpfa/uvypbk7Ll71O9MyMiTrH6pdnamQjtefTUj5M9CpYHYX1mkBkTX67ScNkxjXDCKltrD5aRvz88H+szZicy1c5FCQVXTc6zjEgUMKUVzKvfnQrU19+FxvsrG26r7DFbPKu2Bn3DbuWIAFAhR1FCuiOM6+bWNhMD3i51fPyZvW1WGuka7QnDBFrPMvlBgUC9fWNJ46MTmJbHBrn0kIOytZVlFLwr3uVDfx4woYZFIS+rnSJWv/5g+4IP6T4JgvtbzR0RuiKGafdgaBBlN+pdInnS5+r+9z6ntuRMlUEGHFLRLO+8kucOEidN2OBow2nS1GSHbDA+N/U4bHe2bO9fYFgQAVok2ku7sdcTF1oBvmPdo/Nn3FS2Mv2n52grt21SMw0m1qmGAp5s6nb4WXJEGEaZybLFTAWVO6knf7nyjprWO1zzRP1aq+Vs1hsv+/MmzyIy0u1c/LIhmR9/f1qRCzimMkxILmbR6Qtc0Zh4jc3SxudiIgZqrY2VmsCQIVE5UmLghAMtRmp6tsiI4n2qmmfsD0P4a6EeFmUTBN02xqSOLnpsn376rRqOCWk1xiSPcdA7fw3N59V1C2uFhOO1Nx1VtYdczBd5obg6I4anHgKW8WWERYBgN0BtS11hmNrv5KwReuymfYiKiBZy1Idpf0+PdSV96C66Ttqr8H/EWIMj1DgXT4NLPu91caB4AFRP6d4wauW5KPT/STvHnSHQ9VM11eV9ftXh8ew6N1Gl50rtUWqtu0qc/ljpZCfAM3ynnamLkU63f9ZbYyZUJk+KaMnmT9+X/dbJhcXWu3AuHGvvTCQR9UNVrNFXWxD0p855U/QGBRBtDn91pTFHeeFIhuqc5LSrl6PVcdiG4Z8oFSiPcGA3VKuHXarB3x+Q5BZMFmP21hCjkClr9Es9AgRi/vtxdCisL047hWZETKC4LXRfT9yF1bB1/P+R/YVqqpu8/rI5dxytPYRzMdp1wVJD10cjjOXiLZmG5+xCmfp6u2F3v8c0eZNRXqPOZswA//DbKr+44esLzYJ+DVuE7wWfC3Ip9SsXUPVUYTic3ne2XQsbCPTMXxSr3oH+Rgjlt/DuM4FnEoFx94V5nuaMDZSghPmZ05YTrcHh7h6jx5C8TC0uOWF+dfZIWZklhRKERAC/W0SBWZULOmD8YX7hDatt1ebUUKmvFH4QEuj3KnBCyd9xnB69en+yd2I5T0uGxNAwMIaKocYwn7hVBf4HFRkpYXUeGUtBs07MgUOCiiAFUk25lq9qQDzwQxpAnxRJa/v15GIwcSynAVzuI2FFHhGrB1+PIQDOmiFCLYIHKupZyrZrW65oMUBUb+dn4IeVyOs/tTDMmptw9Pp1qXpy77ENTUL5iOiiRPkmfV1flNTrdEYzo1xanMxfpldmQox+wFNXfltoj0xS4Qu4HhQljL4EvrXe3tXjClbmbzdAS2NkUE6gi054F87XVngZxhiy7fiksUwbWyWhECQr0ctUeBHsgLHVMUvNLOzwr/z+n3sNXRgXgxG3vOdUflfMAQE2idTMnVFDYvrg3PPgl2gyO9HBOMzRwnKWYIq+SSi5e/tW/rO5XOfMb90rg5kHaBcDkZQY8+85JdEN7LcvedCWv/+KoiNatsZxd408bu04u247hEghTpuB8xoVSR1b6yqp6p2i6Meab+aEmUOXFl5ChkZP20Nbe13fWVc0Yk5KDOtYdkyfuwYCecvGAxOsPcetxqr0u6o/ZOf4gWodlgAj0BKgv9m1zknbCF/foSYy76O2WbW2aplxc/SkgMyvZKi5P4/UvPtMUUEcpdRSqV4pDfi91x34biH2p/vewk3QyzrBxyfJLjB5zUV5eoFJQG7it57Gfc7NEt4/Zdv0+bN6dYF0pXm0xL0eVXwiIcvt5/7iWonTgJzZbvinpcFVjSAGN4oxQTbllPcOH/NGsFUMaQVJaSl6dUynQn7k2LRDv611rOFZ4MOS97KG4J10afPznXIUxSd/IZmtmMmcWS/AuJ82cJZIjhyRIhPfNYv3MZWzvy+/JYW8LYrxik+PcdrgnKwvXAhAPqZQrL49F8re0jCj4FU/pt4UXTlgqTuFhLhKcEkAq6V8iPfdIW/4GrPlnjsd3SJgx7HQSr7lDlWabR6kLE23foUaYkH/rK1gEpOP4ilN/ijMCJaQn41pyLvKiBTkWLiWQXr23MrUVmu6FkYXOLkywmPb8+aG1+GjnuhxVsJ/CjNIreEwFYViRZCMYRlOAtq7MTA4sz0ylwWutvCo62ra+0dm515rAi4Xwl+WCvf7+PhqnxeEeWArJmw4wzhFv9ym7GD01JXgPV+15nooslc0KaopXvw9qXjwvku6QgdmqTOCUjXRFZmPUhjCSOEvH+M1XQCRrOxOk15rT0mUP8jxTcad7VBBtWTopCN4FzQc94DoikfsvU1BVnoTPQmfV21/ycVwu8fzzwYuQgrIc+QFN9t+IwWm8xCCpkSbxhIetr57PUqrlt/J9oQcNeN3yhZ7S9NhaPqlGN/ACmRgb1vKTH53FDXYh3IH+OCl+0Z7Wf+RA3e0pB6Ydxc9iRwzexoDsnZb23JSdvFRm7xaBNOUduHX/3xq68tEUasXRjq2QpZf6gUMMXR4/2kfb7ttMvgzpIYxdtcdapnBvrcYgGGMJFR6fe5ll4UPwbJnV8NFq/QbQSplI0W01h6JXe5iRLCE4XKN5t5ZOCCW9lbSmyS296hqr2IMmRuL8S8IQ8SS+L8TXbafyzL1uq9/kfEF1xEAUhx13KTyG44r7HpzXMB+FogU4ThbeaZQgZdZKXUj6ohtjrAJCeyb1tiBHd4hHAjDyKFMBDM4ntlHAnNd9y1fT85yhE/MeTAP1JEsQfwmsYpKt38quOCFDFqbtRol3WmC+Hqw+v1AGejcuBGOGa81xhm8XjSCcGcrPEcPWMCRg4kYNjWbX7DsU0cJUH/VP5MeaPa59StMJwofNwWTE9Y+gOd72bRB5QPcYMI1Mnx3uJ/c3kP1WZFlOOhYP5Gx6XukloiPhdXb55H3m1QveOTRTdRC9Maa1Oa9NtRwsffBc5/VAoZ0oURZxhixorpcfk61qyIxw1SBMnhHVQbN5iY/18U1y8OZXt0+VmrD6rNM2m80dOhpnkYwkDfKmBPdc+DOp0l/0cUVPJ/GT8d+tm4zvBo9q0Bx/iv1iK13w+hER/s8F/1aq0Jm7Ox95YhPh43P+u4cA8WDkn0/VkKtVK8yak1XhVDViCFwohG11QUZARZN4p7BXPHNTlUNnUYYBqZoBYIkkruiGuw5MFm4k4whmJTZ7SpHTMt5rj4BnhiA+ZkCExkW/T0pHFwTDXjtnJ9wX8J2UbkFuDK+sRDeEKwfj83+pfAgfmZ/h16nzD2Za6Qis/CgH3QtwAuI+fCp1dc8an/VW7fZcq4/SU1XzjgLr7cSaSfmntRUirHHDDnSQysqxamPxibnCz9BFjh3kF+C53D8dyqeV8NRE7P7drak/3pqZ7b6cXydhdKTZoy8+pzfFlOCb57ZnI18Jx/6i/YgaFzaw04B/4I2+04+7I3bGDt/3Q/tBMjkcTv4R+0occhl83QNaCcx8aCpGf+FHMQDZk3kW7uzoxoK3dmenZYWajWzW/nDsnAlnsWLuDiTISdRyw+mz7vLGLV/n/JWvJj38OwpGu+IpCvvv1aWj5a/qbTy1CMMicOJpVf0mH70XHMFo0+WPNm9P3jFSn3lWtuwv3hSJgl/7v2p0V+GnB9fDDywBoxC0/iTkaTCKRZah6XJvVfuvRum52e/Uft0LOApqEhyZsgBw4mGTAwGN5wEbZhPdvlbYiboZNad831rP6J2m2m1WeQbSFP4MuoacsqoIoXopJ7CEAhuPBVyU5Tlw0aFmc7dRRStizvUo7I17vwqZFYFEQMFCgX3/6R3VtvhNlaTy0k37dVvuFK5uJJ9ueORG0kgjX6g2hjcIvOfF8rViMxaU6ADFY0yngKGR6lqUXn1kiNF12eksrhz+pntGygbeiPMSWTXQVm9yob9FOvTIgq6AUlmRYiKnXAN8QlpCbhzs4tSZeXdK2N84nfUy0nUKgtdOhjqiOr6CAByG7nryphTxmYoGf6IqLsFfilMfwwMBy1MCPvpvQeyve2i1VXYe/d5vlGMU3BgApGPHz6FLSd4/Va+ch5uug5nv0q4XxSknur8yTJVD6mK25yjti/ldCLzNBw/JEyKvgr/20P0z2lhG7FcZnWgieZ6Qlp4gX9isvtr6TX7zWNOzmXuU2+ZsxTo1y20dxnDYy4NTzScJRjQdl4MP7HGRFKkiOy/qnfirHqto1B3jT/n9lxfOBzx0rdJTPfDsOiVaVXjDsQC7qGBKPZvgRDh3j5vwfxxXQ7BHbLBAENCmxNXeb9R2ZuVloI3PTtr/F///DYhu0YEfpnXDQvkQ5J8sslnhc7a8znYxE5iuCLMByFyvxtWYcd5rKEpU9IKzlFIAQEO/fTeWSOjcCc/gZbqThx031rnd8l1kJ3SpSdXqut7jztLue6s6ZMMiE9I83h7RNELYAJx8ACCJkFwTtJIhs7kDsZ/+PbQHyJ2vM81BcSjMhKnjrQd3FwWSkgiN3Dq9WZL5fcsI1M+BYciXnTZ0G6lwxmM1vdxr6TSWBHdq5q3Ds7aVWSLWZEyVNGB0iP12UF+PQWWk0iiRbpjfrb5EslzfwMcb9A3SLEeyYAZLm6Xi9mEkqfjctXAFtaJU+PmoQeTMG7PJvnKHartymmUYHf/hcKTU5tLrJXk24mMmyq7HAycI90BJHodULUcteoRNoA9MNJfA0E7ypn3K1AJdajpvUHNlJ21dem8bSgKCJGE/fpRBjS5BI5kEDTIRI4FvoqJN8rkSlD7LYCPh8eTIAsBzIjbAeeBYuvUpIMwhev1pTyxi23llelnPrVIQyYhTNjeg9ZdDeyCKZEtRBFcgb7Nh0lqkjUEWL0PnjErIR9TyEUSm1+hgn0dIlOVk5+nN0DACQ4hP26J/KswtoMosdU9t+2htFEhLIaRiaa//hwyXdyH4WdxjoQYEAbVVr941SZsFAflko4yrLA+B5iOOoi3CfhQ9TKOn7FlKOjReMSdlF6Q6A3B5Sw0mN6LtDXNKaoElRPF5ugNxFEkYj0gXaYDJ5pXtTQA5Ym5ZWGkFNLcIRgkEX62Jbc+dfEWLQi/t+viAAgQhCmn+ja9ewjxXDjqXL8vhtmjwVySRFagQpbA7dmzumbBXtWYaD1XTFhQ6Su3DtEmvpAzTusggd8QAe3LMaJvpUz2E7nkHpxpHaDDzpskeI+auE4DyfpPb2oQdp2QAZN8jrTURF4LybYoRwJCYF9UcZYLBDrl56qvL3j+ingmjCFCwRQYN4WMBTMLXrWy1NY3UQChlkLvvvhJYOcyAcvpG9niCZk04wICZ2ZN5bHolAHEj9ZmNhNL1Di4jRcR3WS2z1y1xe4BBWkUG+pfOJy2STMiFr+D+CiDjy6WZk2gUHiKX8J6YHuyN8x+ZwhO95yO3fP++cY/kj3N0DInR0oD0BioVYV8G0T03mv4bMIV7yfiSpx4GCpeD6XJlKPYN99WNkiSQrhDemKmUMGCJwqVCTu79d2vv5zgvC90hfxH46Gq+GIIfi2AD8hwzzRrBnLc0liQzg7GTCgjR6PEaIYMqD6WOoTS6BtF6prp6Cy+xXVrdISw8sNVer2iAlLDNcg08U5bP8GOh0IdiEGVteY6uN4a9Q/4U231PE9ctfL+ZOGalbY6cE6hPqJ1v/+/oCDPtKSjm1v0cMqHglscTSEg0CQafoUyWmoLruY2GpCATeCa+pbbKG4+822U0aMVddnLdjJR6oTZZVCqjzNPSP2A+jWcz1zC9Lx919LZ1e11BxvzQke0cdRC3sK6QhY4CXU42LC6mIEVwVakmd3U4GMJHul+o4kyv6RkLnCI60e0x0U/GXV7TlA+H2RlncfC4CYGHrF2zXyEVkAqhxDQ3iJWwly8Ecu/Zjb+wbxMr/OvpbhbcUmDEjNGKLoOSRGFUsf0WE1oPzT68syrFXOObZ5cykIr2TudVJqGxi7KJGb/QHkJ10WXPiR7aabvOek5HF7bWV83AlP5upaGL1We2Q+9oWclV7I7dZ6Ke4K/9+Mmn/O+a20m8pbh74vitoEOrqF0XaKq1lsBf1inl+mtW56wSt3fNK1jKSJKWyfXOMrDchO2quECbuywiyHyslfGhGAnoAWKUeQ2MAPhDAZ9wE6FEcUgMXRCxM4Ov/oc3qlu79W4HhHDKeJyw0YkzsPzlF7cRqjdsV7C3gA2nQDFUp897WuLnuZrTSXUqRU7+sxADjpZD3/T4AoSEaKBXo5t8hRf7hOtg0crUja8+xvaNzVKZ01vBPc+LJ9qt+7bCZYD8No29E3juCGRejrJaY73mMMXK/NtTOX2+lW/vx5GSS2oc94/lK6hKjQ8W6QCg/pjHSWqnvPrZlF6cI+kZEu/gDWBUi+Su46f8hbMoMsXWJbJMSDWNyUFa2ets3Y87A/dTPYMGdfJTzKYtcEC1IMGsUK57auaNV1JR3Jci7TBMvt9xwPmQrPGWgrosm95VJKIDCAmyL9YflCIDzkxQnqEL9pOVLrru9ZVK7my71TcU249/+9nPp+GqoCI/72exRnkv2wEqnaNgm8a3X/wrCtHRFzsXX0nbz6MFFTwNKrseR8ZZjbwduwUZ7RN8ob/x1r7uvwf8xnQiDW2r5gSubEYAJ0hBfMtCCaXByknBOCOcOjPo2FvXdqIo10JjZpjB2k7lebLHBlUlq/CrI7gUUvDnRjp+htB5Pt7ABpZFvEBV4X6fK4K77rIKyYTiAcX+vzk4zR049vLg4O9LfcGfqZ3GmqKDF8k9ADjIgz0gOacxbbqTKJ3l0xEZdCKUAeHXee/0aEfeSW9o9Q3yEyR1ITlyQDKDi7KyWUjwlprQZq9YUCtjbJDHBqmrbu566jJWttJvV7gityeHwQKvL8k8Qrc0Qn/+Z9SHRHGzNj5dCecR0HsWGolLpQLzqGIhjH9EcXm7Im6Z5uLONgivRQKZQ1PlSynQG0IpSfbHhGZHOZMl1F/AzYLDFqe+1H310dnK27hPG/aQk5WBMevYKaBb9Vml4Abu+AyvLQf4qR72hZVWh0SUB3a1SSPTWhirIte78CxsmYcVMWA6JJU+8CX+4T/WUIvkh/0n7vF6eTSy5IlLzAy5Ybmjc+phMobrqW5bmnkna2x2fQV0XkfsOhEG06Opouu3kP3fhy0z0Y3zOEPbdZQaFfTzQ4+Z08tjthicCXC8vo1FsECBpxOdnqevbc/zZfQk8tmLBbm66+E5YZlEFhfn8LbpAy3hfeGZKNMll2eb76h5GlHjj4gqaHuY2H0jql+usvsyULowltQ+UTvGcINfLkoYTM+APGN4VHS1VCVcQ9sbrU+sGhvNbbjOOa3vfx2zth1rBm0j+mpfr+w9HphaQ5VNJ+VgQ1dyuB64ME49X8+kGM1+C7q3/JIpL4InwVEU+2YnURncBRCsBcIPyWWdDHBwLNK+b5qnsFl0+T61LsjHlHNY9WlnG9rZ2ZMc8+IrhPohryNhCoTLBuppadBLlxx9Fp5P0CFeNn4BJZOXTxIvsLZMhHtcCudKD/f611Yr164eEcuZ9BAkrdhbEZSxzEAV32l9Lt65cqfL4RJB3ldje4TjBlfH/dwCieLT2LpQSnRK36fwAUApxMqkI4Baqw9dQkn6Aq69wD9AsemTDReA+1JvtUSZnczJ5czvfSIOSI3Ebp8LQXaqljiFf6srpv0nzU2PkUsJ/MryHonV3inSuunJQ+PJP07N1alRN1n1/PnzoAyuKBQE9B2DcbcSFFnVlV3SY6wi3CAxFjvdqT17PqqGOGgHBuQpsCqvNKazj73Q53wEFyJ4pyyF1dIRxWAqgj8dyrUqUENWhH/oLvzsYxN661wm8hKTzKwh+IuL5Nxrytt+8DAEm0tfDrnQHWrrWtirPikgskAWWqT/1xRnhLU4gazYf/d2zC/nSOVms+XE675JeB0/pLAt5aPWrOOT+rAqTiYawulmmuM+Lly8cv1HjIhXaNU9E9jcR/uw6e9B5OmhFNlWFH+4chOXUrBFBKIZoiOk4+r0cZNGBtYqLOYIqf9BhISGOoGUqU3mM45bb8WYfPqsRwJkouajkzGyr4t+Kt+qPNMOI89nR5PoSoxsDT7vZjY0YhSWclizKn6T1G8oAf0AIt7EWKCa716cGzjzYIERyxVaA0FehPgGXUTYnoqqzSTV+pZP5P1LtahZqZJ0ADdPu0TYlRX5JgnWF7gLo9Ceup4KVhjS9DRuJr0YEVvCB7UVx9ms6XJ5KsT447ePyPcYxyFUgAMQFJX5E8/tyw0M+tAJB5Kht98t4UiLCsci83mz4x/DjE78HHQBYtRKWxIPffw18pyCf5MG0M+ofiobKkoUeHhFY/Gkiemu69ZLhnYDAZySMVK7Mjw564lAaZCYtyfb0BZag9dZ6wSQY6ynu40IVSFvFyIdeyqMcXOvnH6VOFAMIM+4c3Lj2kaUvEqlpvq8TFtUHz+O6UZWSohawZAQjgW8RyFSFmNiZhmpWDAlaRHOjX2X3PFN2NbJlkik4GAEAaxubyTCpnInmyWllvHSIpSmem8YXlPdmGphZLF+dgFZOzBMUvfuNg8gvpl1EcJUdMxqbUwURqE1U821JQOI1vcI0yGk9VbhnYLnn0egRCldfRUjOwExBUiMhoAepl6vvJAmFOu2UXl0+FsKtf49xXPMfUdPFPwBfZ/NaDISep2PaQW+VEeROahE6tj8VM7DLLt6tYr2OK9JvHi9Wn0WCnB9SU7MCFvS7APwRPzTAjEXRrKR9dxoqzKvm8heGE4r+S3Ci5sIPnhyNBTqRP5JgwmY8vS+CLEsQq4BucLDuH9LqFTq/wZFCbMKy2Dw7k9ASI1W4VZx85J/8jm2+jShxWEwbJ8Nd3rY0l0+Y2W9QJiRblh+mN9mGE1md7n0KLeiIVTdzCXcTaXPbCc3A3VOgp1UYloXtm27R/V3eCd35MM1u8/lbcEFcxboCMiK2NpNXXrD288ppjQHMYsfJWsXV3CUqhg1dYaXz63zuH/dGZddVKSB8d5r1j5QztOoAJgbRo7lgeCFTxWjtuWNTrGrMskfsp6/+ju4CNvsihu/jZ+/EtMjko0id2kaVe/j0FU1ygJ5hU3jS3Tdqlgs/AROk/X1RREJEpHO0suu3GtYpvTOD4BwcXoxm0l5x/uFnDVzFZiwEmQUwDwl2PYsfbD77vJuolGgJQeqaxmLTiOAq69KiUTaPWoZ8bPDeZAbdVZCVqrCAiO1cJb+L23hrDz4FIPI1SaXxXjg7L1XziEkcQuFsEpUN/bPwnEYPicRUGFGn5740umJ2FFrPjzSQkrjDzELQ4xxDE1nIsWle4JDOI1j//16eGbZt+O/PY2pwQ7YL3PKhCB9so34nUy1ZGkWswVi29CfK7mTZr5t5/+SsiqajTGIXAskLLbkCfyphU27E209y0p7Vp/7a62UDUTxucCpm22x+WzaRxzff93oFTeiuPBLx9LiZZlOYT21MIM5KOMEN4KgaF2akn1jlSxV3VvaR/ZZy4ARWNozyMqNipciv61BquGZUlKVe4+bN6BL6D/Us7mla+LKbBvAABktsPwLL7aktSnHL62cudiu2OokgaaYDVhSsEx088Cb5g0ChmWmYeV51+OoubjtgwdvcM0hOqwa4l/gScKultX2BkHsRi4ltUJvtdMwanmoBF32iZRp/BY5iOqisaUqiw3vrsST8Py0LfH88k/KG0DyqRytajgSUKrKbij3VbRXf8c4is0Don4gsxDxgt9yytfPVQ9n4iyfQlMaTVXItT7PfexRho0BuwcGpa1s3pv54mw7sv9FMSQQ5r76sATh8UjAu7wa1GfFEGnuR6EOFu2w1ohbKHMdcBXNWWGXW4HT7NvC4YFOY/PA3PZl8snGk+9BRsmR4m2La2zTbq5Kqw7lBJNCMW/hSEUR9uuvNGJBvX27jzVa6uSi+QxhgSyx9LmML+6XgtB3OfnlUfrQTahi0/ZPNg8Uq1GMEMYNUMmExJ7ySIuh1y4lfvSrMw9346wq4T7VLlUqIyGeLw+jnLzWYKGCnKuih19soneiURHkE9jP88pYY3YFzvBGuXRqy+Ldf6zOyfde1dn+AaLeHM6kEQBjie9lwDI+hS92u5QXOJNAXhAZNO3o7wqSuXPvWQKAEj+MbUSFfA4Xwnueq5G8zT2437FYCtkW3TThE2tEgJhFhadeb8pe7iY/+cwF0jnY8MMxYgivEjxnf3y8xo1a98zZ0N1QsQSrpE3Um2LPbt1LhWjMNaQxPEN2ak9OS8Rgg4W9gA6FFTHZIvbckVUGZTWorjhaS2dtikzknKuxcI/sTM47dzbT+xvQe2F9n0yfTDoZrN8bf4Z/Jh4XNw2KmwpprWNQQwhWmUIKrnoJEpkr1ePurRi3hFaRtGGzXA/OvW4T6A2N+t/RZtuO2+YgV3qqQOYWeVB9TYiWW2uGDmgyac0p+2RB4+7EWqr8bG43q5fh5f57o18KAxCINXx/y7eH4Xnl8Qq3ZXKwppuv+Jw8eS36Wnjfhk1WOccv4U9DioIYqnqyqFh+q6kRU9+YvwIGrg9S67abw5bpzA2kIL5MkQKpZmOz0A8h43Xz110jsVNfSEKOsQIP3jzWBUJwrbOjNIKCkkTKObxOsjSPkqUc2eraEHISW8gr7AaI3fUtMhfFkobPqoXrKaKkB5YKVk4yDGRn5pQJf0eXbAJR0nfaGtCASvRcvIUr4sr28oGpU6ywfKRtuWTvRLGqdzoXEhgsKtsCP8N2A/YzlDL/5l5OCjsaL8rUlj7HPGx1gTXJ6N2EHN70w0iXxaYvXhQpszdpBsW8qgZ1dgf+1CFKTL+KDh58N/fOmjnaJHldGxh5PcLG1lUtQdVDCAwKpycLlMqlZP1KRZ/69XEif/BxR9GUGSHFlgdsqdQe6wjKfvI620IB/EqtzUlj9wcMxFD7tW4dC8npNLsNcTvrONqFm/zWBGFEyFMNjYF6+gCujaHdHFiBzlPKk95obDVp+dYNqpQ+AQY2g/Vh7yAAh0iLE9ka6vbiGR4njQeoOYZJ0AaeC8yALX7FpbpoYEX1s0TYnA+kheGOCE2BE6aUDS2aL7PsBlXS9GBFqRgRTfDAhtJTqkbgSHxFgfMXTyAfkauN4a30+rC6x1CbpZc4ZyGnjaoIY3BegPQXgOMFhPXy9Smq+d6RnVdnce7rLlPmpYxe0LBlcNRvhe2TsbHHPXZlds9xsWLKFIeChgK+1Ek1IzgLTesAzVbhLptZHBwEz7tq7zITu0XIFxFElRMK/Uka9BTiUmLbbC7YU0OLD0tojjlhgHFDW65GpxJ70xG2VkZXJbTozG1U80ziPkbKaakoBwyU/CxMtaLc0cYJq6moET6WLzl6FReI2AdKPqgQqrjjGewJttLLB5GHQ+W00f9jUI0AWLmGjJeaxZ9lPROvcmUaG3MgAywLVxMAkO8JI2R9xu5iMEKTX1hS74hANd5Q+3gd2hm6bIAYuv9/a/mDJx0+qTMadPQlNZG4YJRyk8h90WJrEJq8t0xYs/CF4MQ8f7eU48c/hr6feX6cJilHkaF+hnyCXM1zoAvz5Jjf0tPs4QMouehYAgPr8tf4c5tKNyjo7LOndF/4FxzljrDsLKwD/ugRjmPjAuifELNXeL0bydSL4j7asg2zMmRQOhClM4+9WLz2AK/PP4rkmbpHD38WEZkIkcJn4d151ydx/Vw0QC8qNlprA5T0YdsUbvcOQRNf70u9oI8M7AAX4jv81iJ0idBEjNr8FUEyDf22TJ8g3QiVicv+hU0VvZ5wy3CqoBiTOTnud1WePRmb2RAiDdMj6BX6jlUbYAVVqbHFOr0TM/bWiPgT+YTgYQBG0ixzZGQn6LoV51pKnAidyS3nNtBp4Ec+tUK5jndO7R1WPGticucO9YRatrFwzDEoYutKtIjviBe2Pp0QSxbsDxHEZNwoPe0aud+Zo6KLWn8q9gq0BQ7nIwOFwx10r4a4ANheh0gTxZ2mI2AhULpHuUO76Z5dRUK3EyNCRvDC0kN30CqwMbE4gm5MIovl7CK7DDpph1JzlIjBd7HABP8urvW4cfbkzG7M1j5lPr8APKScRbZ3KsVrQH4dKr2hqXfCZFVnQsxuhh805CWbk6kwa3PmBfGQA/ht3eTElKRmC/uGldFblZhNfgwzC9GGkpBwT+wil4ik9MZFYSRvvkZ1lRzRhzCtoVXZWy6vRXPNpGCa9Jxj/9i+WfeDlC2hxSOrCS4lXw+vJ6hKl/6nfqNb1WGN5Rte3phdrOHmTyD4RQzhgJ5/c6ZZ72uGITi/NmdWZ2P+OHPpuXUd7ZNtndlEW9varZxUJV1/6e/qHSrdVs5yrZA4GLxhAnyldgvlXojorqXkLL+/F21lE31d1qlVFvtLNaMec02HIqN7pQwh2OpGF/5RZAFHUPvL9Ei47TpPZcbJsLnaJl7oZrLCBFh1eWE1c/USnNLVrFaIBDKdS7HeQxP3/dqnXUrmbFv8xg1k+CPqjLeJBKSCbRzrw7S1O2Zo3KsXZHx8r4aRUQCBVOCCw0kB052ZX28AnKPU+Yfk1PMitIbb65o2VOyn25oPDvwXQVy3sdTNXgH6rJfgCFkLUbVHY6ALl+PI4jvW7g2hAcanLoEmvH2Leae5MdzckPViAPKqtZEF11sJdgRwoFj/NWVUf9jOcSVaPZvYspZxAohheJdny1v0IC4zIovH35PNl4k8fV4m0t88royLmMnM6kGRYq8twWztKrq/AU0oKECoiM1si0Se93J+CcoSN0xrOVDeRFa0bXrelI7ugfw1+bqV+P85c60iVq3XfNGBoMdHnkvOpUKraSNOoJa4Rl3SKk5y48OAlLAVd+iU2N0wsqKr5vdLGujCOAreXSsHDJ6PzmhJLzgCpx1BKdG0ZZC3cp41Kzt1O/03ox524xpTAJNrDraxnvPTBseN3eZw7pWwj06F8/Nt7yCvDPPLDslwH4rR2AKFPj7httjo24Zav6J1M2WvzjxATY/6n2YoM4c2ZvHkeH/VTkFmOV8I13vcTd982lBwHsAJ/hgmd5cJk2Qm8V0muXi1mvf1/wMKukmW8Rw0xit8L106lk9rDcYhFJk71NF7OSZa08DY4Qob5/O3Kxg+0ToVcKWvRe6Iteyp3ugItlIS7J0Vi+Lt/xlnAjnzu2SkdIFdjl7/7s0EaGpFUaLS1l8d26GEx+p5t/cFy4TOhYYgCXyW8yRRdkEVWjYVaErw//52UNH/sd728xaA2HTEOF2El9LM/yiXHTWKl8GeqGkVKdlqfa8m2KT1aCzR/+dtrXTSOBL3bnzU20aLImK8+WMsYC/beCKdL55bPh/t2ZBvwODlHNAJubuqy5iiyO855J1yxQIX8cCHDZhz1Bjr3zxXlwz5Rt9iwnDlO+F9K8MqgLQqwSjOJPdDJLamOQM1mJUmBIARRSkyYuv+bFAGFZxP4vLQbGp6TB0x6t4BA2R2hHjObu/pkB83DSAAcu2qqxRRKqLqLuVI4mbfbshqrfWGXfD6+bWTTdPdlPk9tuwFrSrK62qgmDEaAPN9kfD/wffYG0S46zyaaqWu17xZsIr4HHW3/CYvQsUaKZRkNht748gbYljbkWRaFcT0qoO3mtWiACrDjFIlnmUpXSUd1FdLCIZsXxVi8QP/2y3od/5ZTUlcZtqwi5V9p0v7syGiZ19vFWyK1aaLNJLgvGcRvHNV7fH6IF9hW9xnECb9mA0b441Ni9fZMqcCUGnHAE8gh8E9/xkZ0VpCKD/trDaT7fdcabbSYmkX5OubauaNSTlkD3hKQ8MmRy5NGSVK/KW6qb372J7ysG60vPA1FjNJRhURrbWAIyfoKgeEdhQf1qeWcTze0IHI/qhw/IBki/pVER/N53paGra8E4gq8/DTsLpjBQYgCHtqMWIXiJj5GhmuDwSK7NCj9enG0lvWBQhONERa616ISDDhSgEEZ88qr8BT2gnoIL7oQ331S1iTpKdrt2mZ/LrsA1xfLV1uCH+nGx9rJhyCSm6EaaE0st+wG7Uw2oe9HWi4CT/Vp0anrR0vjFfAHIsbR2Ri/DKXM7ehCVfoLRZz+kb24u0q1ZSnWLzKF2UuAGzrW/LLAEiPdiV9OWyvYYvx0j5EBLOO/Pud5TKeOOQ+R+9hJcsrxL8cCb0LBc0nK264w7tY6lMBv0ZE7TKqU905H0bnWBjV6p4nquzu0iEHXbM/mYi05rT/elKdl9/rKyte5yxRlNGHVYO/w9wH6O9Psx57dfchOwrbzjmNJtas2oka+iN5119IB/ZW3AsZGbs+YfMOG4H1kcTGXBBR7/0c37cVg0kesTgfjD1RCp1p+fMpRsjSsUfSMQrCUG7oWrJBaJ85frDgOuWALAhxvPUTwKntk9y/B7vCf5uQ7NU8vdZrSRBfYjNV/2fQZzWaOefDpJANt3knz05djaMx69s489R3hs77Li2X1Ro8q4sM+EJijwpOdpP7VikpsXXrscX7dfXLG3gUfEH7ZC2ITvtN28/k+kXNCPYo9vhaJOO+CjSUITp+AkXi2z4ypUNB40qYBQs5JqCNLySga8NzV4PHYC0akXTc6q89iwDxvmfvhk9+JteztEMpxT7xBLlK862Vgdis8IMR7SIx/QU/PqNBRFDC7SMrYv7FRpuN6i6BRQRWXn08wF5xOV9OFP1jzMGFON6FNDjfyBWXLU9qnCg46htrvbfHi+hUnNpfY7t/0u3nz5ta6Bmxw8nP8WaRlgKts4RjRVUfRU+4qCC5wIdnEEnozki4bTajTrLUCN1kkclYDVNwordbK/9DMPyEw8gdbTGAfcWoLeTTCcOMzP/xkwvLR5c8V0x10OAstkYZIm3WqR9pDCTJVnZlbyKgKcWfXPxY7cqZfPaZGXbxDW3oIcR4jB2nmlbTVfXDnI6dqjVEGt8guUJZ5KsuBqPlBiphXPE8R9RoG4Km4UVH6B4TaLB+yOK5B2J2scqkQ3XdY36HJ5DOQFDZ8QUs50Y5gBZ4tgWqDoUg121op+wGHVTpgOXd6dHw7y+2OrWHuSumspC22zqlIAgpprtYbIVDVmsgob+6JNkNhM073fdRLghQCHEWdIRL/ac21fRV7cjjOozQGSqhUr8KHqR9uB4HKXfusWMWWT45D1eWdGw6LBSrdexSUbEJw3uA7rGSGSnbN+i1ca3RicSWHJgFkW6585mpGDB1Nwvv+LcE4h+MZOMyrxhRAz0gNkxA6OP+oUTLUMAgMMkINi09sg9yr+DC1NQ6U/oCHCR8Vh1LzfEwhRxdmq+MjY/sYoK2HMsBdRkctXBKSB1DB0LLT5LNriCgSwTMRDFKpmorhXVuR6kccuo7k8L+OtAKTe36N7D8S5GI8XkuIDcmVKksMUc9zeA9hNFf6uqjEcSJf6I2RFDgbIX0X0VrwAarPnJSzynCGcK3wcllbXo4fpJhrUj1xdHqJ/Lpq4iQPFNWzXjnTU3eWhyQsJS4Y0PD9B0MC//ywhZahza63qsNwPoQDBQDQMuGeZvJ8GIz8wYclMGuTmp6qiNpIx3H91eYCI2f94mCQbzVYAwA3cpG+mvKMvyQFi3zg0nl2wv10jzJ3BekNnCEPZzrPCWMs1MtbdNoTpFTzjK8iO9CuqecZSkxHB4TUwjF5q2ynjhQ4q7RlhKU5wWWrDe++uJX+nPFxR/uQL6kZ/A2FRi7aWFOcGyObCuXnCGWu9qVmnHPvQAcaL4aG0RnPSwfG/EPPWAP0/+dm0Y4Ic5fK/rt4TuRl2tOqmS8m9JmUeDJSGhpSeK/H97pv71xenkAyL3is5bGbVov5n+W28rIFBZtlOzn5HzOtn3/kfskNDDo07Kms0Nd0n/u6Kel7PHpjJqqbCZPzvPh28KggixuFep0CFnsIjET8/Pe6JP0s04XiJAo7pAvLIBXuxPYVgdMvEbvOZ8coMrSrn+fwef0ymOm34GAjol+HaLP3vOxf9kz44BsIOPUF7te1X04kIYZ+3rhVR7NNAGkZxvXNZLRWBOXzY1fIzKGJ8W1Ps2E6Bq2Div4bRZpWA2Xs+o9bTz8Lm8YkriTLMafC4eAkPoHOOKYq4blzBQ+nN5GNEj45b8PpB1UmFbphfP4hgujlCoJhRxsYCxkqv/BypsZFiFsb+37ipcNO/s5EXvbSe1uoTWo3Ct3Yfc/zfzZW0ntjAUV1rV6QqJ/nMNaA5Ud3T5iaCnLJ9ZwiVzTcIqWfWdcNT8Ml5GYF1d3IxhamW6q/iPmbGz1vRZVuOjrErxKpTCM68MCxRJiND++rB5sKeG/qSHZ5SlCcjab0Jt0LB8tWz9TT5/msw/2sudB4DRYqDpFVImveA5hMV67CfL7zXaY6bl5/aEeoqjgyul6Hhd7pnIDrPqA64VVHeZas7byXnjcoJEX5m+z3imO0Od5e4t3+VDTyTE65ZCt1kGSssIG6Ph4WYNzgpXOFyhlZL049/oK2DiK8g5M19foPMpFoHM//Ph2J2yp+x9frNxau1ljETNEpDoOIUnHfzmAYDp1m4r+bHbV2QrbI8XBrHSaEZ7+xK9LTmKdFGdsZRBsqN2hjbThW+MlE8UevowPj8oADZSelpJckVUV2KxdubKYplCyVLCiBvNmlnU/yNgzPQGSRYbXVOkYsfzVnp2Ri50HWcqLdvrV4d5lHDx3LtS7l3lFSVhZVIsnBmxhi1tvk3MvbHp0mYf64PnutldyJhvJdKrAzceIL/mVUZxfi2AcmDUSfY+RFTS5k5AkdZcm5oiKIw3rrPjHhU2txCXrlJyq0a6aVNH2nVFTlol9ll8yjrWm6nMfO3MLyxz+aY+p3Q1FltzdrAiRg/Z4aN8FugWkFi6QMQ9ZQgMkVK+5l+9yDvEIioy11lm0JXb2seWSRkxK6qJsGbI9w+cKTnWpUHQCgwv0HCo3HV+jG2VYa3ow2xD6tPsC01VVVckdTxKOXXcZlJtoU0Q4vyQxJsGoFi2LixSMEcDBzqimjwS41gGL2MNyfd/Sby/dX8ZH2a7S1vf7/4iuwA1SXtvxH4rYzG3UThBARzfplkUVTDXwPkurhdPCE7BssJzYq1KJ7qY8vvc1tyMMrhaNEd9IjLjXwGYeGDjhKQuSfcByb44Z/tjJ3COpFtfmJh2zIWmJgxonUkNIROyKtYYfjJv5WQMm6JA4Y9ef7/V98C2UO0QQS3Ce3nXmpoPZht7XKQ6GGkY6P1De3Br2CeFs1WfEM4FNfZ05fqLXvfQzYpYgxnw8WSHavZ+unfP37Tp2sPC6BjhImf0YTejKapxQizrObKO36rKs63kFdZywjXNsTRpGKWyV/1YoCSyOhcREZQqLRJ+dHjDM9xkUi9TRPKDrmRgBlsWdBozSCWxZze3Ihux2lNl1TE7gihvmZISgcdaDQvRFtCX7gy/KFXwKOgfkz+PRpdMTha49qdDD83BKr0xLbezCCKQLRPPRxPhiVrp6djpojowElWI0ex0meSkAAOOnsXmC7PzK3ieHYdvwcDhakEhAktRukhVA7/z7UaGEsTK2QrRD3H309qL3LUStJJ3PUEo77ZTC6KnrONb791/ZiP9WQjqshIK/1iT3cNcGJeTKXRvx0QrC4R37GodEZbuNduS9FkzxEzxzCWIwSaUEz3elD2N5d3SO2ZsbKxCxRNqsI6ViF2gMYYSPt4TNfIIu9c9SUt4EyP5yk/Rau19nH0pXfmVbbbR2HjmX8nsdGlv8bZKbyhtOHANGmrG/BDZG+vexBtJE1084e4zA9+Rde46SJcBQXaeymZrECQKO+ssr+yt4UYijTc+yeurM8Mzq6lY9oPLEiedrlcySxBprunLjY4iopNc4w59OljhEw3xe8OSbneFWqPqsEHOyuzOlZ+MlieIae40GAbx5o+cOqGB5eWa1QNMQyAKdfLniHvLozQwXEk3CEeGvZjCgE8jlgtYiJ5D4rDT4xHLsHh6puG3m+QMIIGiPh3fPqCwe2dOpCap1nCHbUVbUd1abvoLvGznBBhwZwg+s/ALMm7U3mEYNcIU9FCStjaWRx6zuBvWK2bvtJ8N1t0a2uIXN+yJ7je8+Ws2+dWbyq2eZCV+MApM1WZZJY/DeUzKkyPzueEyA2CIErKksUg/3W0lZhGLYKubNRcspxc+lqbNRFiRA4NmAZzlGhW3gfncM/AuVKtbnZEeVd3HBRCcB4b7Iy2QrRFjDbrI6EfQlbeaaQG7uF8YhtIU/GiBsMAzpiajPnf9wcriBXUZ8PyoyJOab1QTzJxGwLbl56q3fp00C8qpmPoj9nJyOV4vO60a7PvwfkHQvQjuTguyBKeQOe5FF0g61Jfi49uCTS787SCM2YR+cbP/ti9+nl8LK/7TzTtZoONsG+s4v9Cmg/E3up0ECp0YnsrS1eNC/6tosgpYH65797f21MaHWIYsmZaKjuBP26uEWZ+KFMFWXPX2baRLYefpYjqn5JgF/AnKMokubGgWdfFsWhSzAnL9ZAxeUuthKsWjnHkfCNFExy2yBBuOWwc4URracb4drGV07byDMN0lW+yq2Wl6xzPyBATDtrww+9Emdbgb2MrEFpSRnnpA0DxwwwSc/NmB9ZuUboDGrhkxjxHZlCK9bgbe+XjCnfxWC8k6R2USd7i8EOfTu7hlcnVvGPUTfkuzPmxByG/An+XeJhGPeB7VaMW7dsFzg+Vgh8JtK6gHY6N3auzCxFMTtu9EEhV2M42fCWUL9veFJvdHdIE8ugcGeBMiY6tI7lg+/jqK7gicGak9o+btwbkfH6wPjZfLMKZUdLKLrXlsFOYLKlQUVQ8cX+fRlET7XkMLN/or7Il9R9EQkOulYMXmE6AQFSM0TvuZAZmt8lBPXrMz5brQ3YlqCTaN/JqNYeTvh4EjDd6L+tA0cVepXDuW0hJoTXetoIkVIt/oHaMl11iA9a2sNLo9iQBKuTDHVExHe29FYmSjUijzci5MdXXRKRazMkqmKSYZOCvv4tOdR63OuRcRJCmqCtYyEuSxpsMPL14/y6xJixTZXLx+oa9RAyiaTWzpnIdVMQhH/+8TtfIGW9O7WUOrtavajlFGbrpwJth8CeNKaec3o6Wfh1Zzx0IYP8n37PknKVd94DIdH0OxFJ86t6CrqBu2dVxhFx2IsPb15ZQZvcXKu5TJcFrO9hhfvXjM4wLL8zVjAUeRxDr66zUkCxlyLc6dzubs8InCowMRuoE0uYWzrcDkHMLYy6zv6O6WHtXJ31kTqIIiom468mha5YdD3nf8i29rLpodkWhSDmKjcuRXXQaK3GFz6pEr1PPkjbxMDtkLH00id0/DDt3WuTIoleBl5o05ECaxUn5o+m3HdsdCtzib8F++pgC5Dp+VR5xrE1AVaERXlOvlj1G5JYUaDR4bP8k6pQMOrcDvCDMbABTAdBQPas6AAJJQteoqoxBqd+sStmy5eOal6GeOk7+6/7nEfYGSrMIsAtEvzbDxULnBeomQc1kAg/D8tSdVTwhmbfKY/k9sYaM63ecZ++I3tGgUZjgW2KprhT2q8LWiYPZ93ILqJu3J6WHa6RCEZPtI/PNRoE7vBfX09IjAqNPcA1PJrxQwAqJTP7Q4ssoMi1rExwMov11L/cUMCntBmc5HUElvSqlwczjWI9wHVIUMxDASivILeghOcyFzWb5pYMgcXkpdcYuahvLAQ+RUYQ1O/ZSLODZRvkOUbmqGufglYXZv9hYps0EX4pCZNqQU8Vm136t6QYYOJkdWJRvMyjHagV4tfdAvMWTzePMGDtPiLdqr/vr3Bd/gP7saCR2tSFBGDjMb4GYM8p+k7A2/E+EZ8wPLBC2zW7Y0sKM6fH1OBwMZGx01sz/olAjtyPowpl5W7J/83QWGyHxnhH984Mi0FyLKgzXq24J4r4aQsQUS581oqeTbCaEw4PncSJ3UJJZoWtNktUTPL95C9LTwdWRDmMEArrA5KIGwp5a6DzSCSE3QUbWC62bEORxjDQMvSrlOb2EH0v644JEb+uKKZZ7llDna3209dREcjJ1eLDL9nAy53RJ63hOifqW158ia07INeCOTPckrWKhwqCxDKlixOcqnG9Rj0MsKIHPPIQGzMAgSK/OBr8FnhYeKsuCRVnewBzVHqFGQqTlLyoaDd0Nfm72COnvO98gox5RxLabyLPKj77dD+Z4CnWeqgCNHYAl1f6BYf2DqMMWiGoz5KzN+Q36ipbychHu5MfNjT/ltSNLM0xhqfOEkz7Zkf8nhuGFqKrMUdOFNk1rubpI/WnPEYF0MQZwP09G0QxumSnzRZNkZy5O08EhUhaUIRW57ghxRnQjlArQYqcSOkgXoLrYfzAMylVyc8W05EDdEX0D4LWpnGR+oEFI5MvQTiJnqwPiDx1J1lMlwWaReIBKPqJJbKUczGlJh6FVU/7xgDS22+XcGqsEGKBec3vypNV2uaj5UAGrE11zMjv4UoSjEN4zp1NyY74TSxlidg3/oxDhUSU8pmjh0e0eFch6C8PHlKn8lSMMIJYT+xQjXvyzryEzqqY2xa7oS2YDdAWY04AyTmbApuMpAJbSWtiWramXsICWQ2fdhtzl2cD4jQW5yUOdnx0yFkgaQ+PakkYykVuNognNdleBBICkSpGPVRG4uqpHjLfF6Dbch58QXwA37ZSnnZOQVpjji6t/EVoBY7DTcNllogYzF8N2j9uFEdiI1MzYfXa8kwNZClwcF5CJkZjKkuBt6bWpffGJ+MluvMYThlDtllHZrrjMGk4MOLpuBGLaniJ8sP2m6ikJfRdse2lU+jjHq3ebQlnpX/isbLafmicaAaUD6piR2ud85rHbF4RKN8bVegLJsaHUlXrEmDO/faH7OC/UCDXD4v/Dr/+bemfJEaChTGmsgItIBZPI0s9CzoKLBY9ZWqYrzX3RH/2I9fASmjfVq9/aexCtd0+f9oJ+L7Bcwfh9F69cHhbTqSR0XDvHZKVprDju3q1JvKNDWnOwfUsdNLecSszvSJTkpig94fsxS4mM35d3HecJo27Pv0gb5UFWadfP2rrZ9poUEVq/50OIHm8IN3q7CZtOVNPfw19Has3uBducEOQxruOa3SgjazDUNCkW5vJfzjPUmREZgMu3nExV/q0iRJQClRjDNEhhiaZcFyLeP3h2aYblyeXmy6tFUnFOa7HaN02z4LxFz/UpB5nQOWJClwIyrSACV7U35tWU4yDQVM1YAx5UavRjnsDpr77L9WUUzgTWgzFG5luECa4n0pvuFY/tXq+r2BqEyhawEUW8swWYZQQ0uw2ZX+9U7FO6f8tTmNQo3/5dlfiqsqTbmveGlWebPFXpmsK3pAH3/UvFQxs2tNosS7ouHUcDGsYysckxcg1JAgXM2bucBCTvYu3lVBQuHXQFBkcgG1sZJxAqGDS1FaOCK1co6KiKId2WDAYtq73UWn3rJoTRqsATQsCUFHeOAD5JCAM9lLbIphVlqMW/l6QH5mTYiuOW941namXrbKyNN1C4Vddk6NTAilNnuWsw62D/EDMVxjOlwDqPKrDNi59xrcxp5DnoLrOpX1ARdV7sL5hPHNON4GC/dGnCWtKYCgwwS0D3Ocrs1D5tb+eI/jyJsHMu860zEJ7XE83IQwZngHqPjtXBnOh6fdWFjTHqtSmUBAEiMDcoAT3Ya78w0Wj/o6m5cCt8ItVz7AzQ/BSMKnB7Nil9JZlYWC7KW8Cq9XZaAbxoHRF+Bh319c3S+9pBZcPm9DunHVy/tN5jVwGkoaUPBPCfr8lRudeVYY+BnCvT8Ah5ln73tbhcKqbbsHuMfkIoKnQeUlASF3QPevVxa8D++v030LV7zwmKajysdF3vra3v8bmAsoJQLC5vZy2dPCMdGdZ4341d7d5fLX2rGD7rmZ2GZPzMbtyTsjzkUsssRM9pAq8F57Y4u63OYbriFbYeMg9hn70KUMvwPbrDeOBUk59e8o4PwAlM27yjGAMsSPSc5qbRzD/SnwDNO0hxNjM7i5dstxpZejutLd1r8uTOoegouTfjRv2v8o80t4gnEII6EPFeRhekuk/npdVkJaa+0go4T0P3LPAX75P8OKhxd+45nJzqBKNavPYfHqqTk9j/C6BjYWPzUEGSVVe7TL7lXHAvpchrdzBO67ZVZNfMT0KOoQdgJfoitlIamykgq78iYcZfFuhyY7RVj+o59NMggnDQnepFe/mPgmKhLJpQ/2oROQsGxiob7SZVgvkOTJwYhTkhANxLTMilvw4FOV1fHAHFggiIAIthKuOgCDyexALsW4G/7rS8Fu6EMP+YKM4WHQMnaGunXWwhueojy3isj1C6Usy47dB1DXlBkX/RQRdXEl6EqzFrhqHcB9uyVjLzQO8L1jhkWb/VWimwEQ2G+1TyB4SiZINB/wQTfmbhnPF3QOAarDzapf4yypXpKd6dMAPHfT6I9w1PdJ348LORCvOckwevIKRiwHmIG9wmnQisbW06HrWbzsTBqI/n7Bv9WtkQY6IHuidCnan0peGTKnl0lgQXOHgIB+gIc5MOX60v5a3ARvGH9GNizzNKzcRSQt9oFXhHb9oVhLJ9cRvcYjyQ1aKDng8BESy6+AEpXY2ESnzspLawEEtwJCN6uDWLIPDGHi+SN2H2PdljhxIGNsPSGb/cvgSGhQnCyVSCBpUQw/ubxIAxMlxmRoq/Bt8nmHbEL1WTqCWqOgX/qBzx4xnmNHJMUA6F6EUzibnjur7wF06VNz+JmljmddrwcgZM+ZqaN8xq0oPp+vkTQmZEdpeWFdT2Zf22QlD5GUI1PPveMJenN+deloHdheDx1uHfLV7GcYQkxm4ICrLqDgeF1zeHfnk+5Grk06VJrYAUMV66CQvxHk972Lzaez2u19MkmT1hoFV2BwlpozKidF3yaPVo6HN++ExUfSC/u8hlUDWlCf5tqhcxV4z7YtB3v0JbGwQf/OUG2Y96jIvUdcxCQ0osJgj8gCePdKNOGw9pXExeoaw1BWt4FUVF+Fr/yeTq0m5S/FdNje1qCdTCzYBaKTJAVYFYvfvcan4edyvml1ttEFoQie9P9m3vEZnytcqJN6mwEcCW2ewdoW42fWvWEDwzI/ueiOzr06rpUGnu3uyTM/kZ+OFjxvKeNLTAeEBg2Q7WeyoOYRmSrlJ2u29ewKcDjl+K/EKqv/4P9K/O0r9jEL9nl8zYxsuyGGZVg0niQmerTlELnW1haI+JC/KLSFt18nKmY4N/JZaZSGa0eTxSTjuOo84UdKPhn5Ki5aX2TMPCnr6etBrS0vVTNgtdUI08yLY3iv9MLv5TxragdaJSnOAODH78vjZn7BG9hlsZ9saIFfJIJrj5KQ87k5dpFqTDzPeG0T/UgUqI2txSJs+QG77JFBf/CHprOylHB0roNjHA5erbY0ug3AuJCIylDloxBytvMQbrOWkmlJD/Ejak/f7NfQ0XDTakhU31C8QozKIRsVuqyU0zyDbSZWKSxcZsPP2OVVw5A3cYx6OjAMoaN6PYqQb3aDSPcLdLfn6OYft0N3G0QGEG8ZfvklsfXQkpC5jMzqiqhiC4fXCN2KkFJxtw5bRU58l3iJmqmaIT2+WGU8/MwtUHQfq5dz2GROBYhM/DrH3EBxIn5p6+WU8s3sPC28oEwTD6Om4v9oWY3lHYNb9uLpEzY9kDuppogUHl+KJqQk1sJMDmQixIMwU2kqOXXQtMGWBUusEo+CjELp1QoosgdU0xGhSmKuJQ3OpjjwU9i82KRrlqcw3B8ZAY/tJXkGBCWiKam7WWIdELIMTDgreNsYYTTqazSUJf9AH6A297vYLnRjhVAqMgNbsqogRGgwPTH5aoprLJKePdDON0wuztzyzHe0GYx4tjsCv4ai4uemjih2oX1zLb2iiYakVNH/0L2S9jhFJ5dM4FXvwq84B6o86U/obO9g5zUigEYlQQ7WwLtaXp6/9V1Y1UEtvQ4LwOOZtTYnSaKfJ9CEyy0j31LnWcD8zMtRRoHWJXKX4uY1KjZqZisilxh47fEh5o+0iNIHnltUJY/wjf4grymIixrxhds/TUFTVANZY9ADPF3WTenyAsFnhf67R2xDLwhAz83zW9egn9YymsAXxCFwJKK/jCoJmZ7dkF3Zbx8GE/0sdDIToa/fnLcUng16KvNK+AWex2rlMknYD9M7z3KeY5I1Z0SvSU3ZgW2TEdY/YSbWytPDECJOf2/2SKCjpQVAmIaeBgI/BV1EhmxLwqD3t0ySQBI3kSR4jXpQE2nPApTYVNXQQlSYnzjdL5DtnDZwM72TkXQyHlMWV8EBVuauHyGAfyvLQzUnnWj5JQEXdiNF550k3HbXmL6Vb12Nxl0+b94fjY/aDjrsHKDT2L7zF332qx0Uw30xUJ7LfEunZeQx1d/aKsh5rpgD3XG50Ez3LfkrOtkTuGlYS5/Wnqiuvr6RPGjL4s0LGJm11YbUWlstA3c8Gdh1DBhBlWj6jRlYqPrjFwQa752txy8TI6mx9DI2HPxa7W9MbCe5G4cJpZYuFjW5ivh2PFQhhdSr4t7zp0Bi9rzmb+c+GeMoGeoT3m1u/w3e3rKtMu+OMfWryUKMaJO8oXetbawVMFaxTxxOQkHhydn9CkVWYNSNUOtepGGIGI16IXgWuIr2nuTw3aCNdMfPsUP8Mqe2enURYG4DlBvWzSKnmYx5gO/dqF4JX1ubL7KB+g9GTN4sgysUPwa2PlBzx/sXMUeZc92cSRsjbTiOxqCClGIU6+xdbnc2ECe9jaYbm6wPUM++gl2bNjxkzasy6RdazWo+b+VY7d5bZVsBOvLGlGTLOKxqLVp1yyEXhVVFPe8Z4LqbmD/FijvIQlaToxrFozlfeIxzYN5jHxMhw9fI30aZ0ly7cMdMZAZZkekY76F+eMidYlcsLpzoV/Mfy8H+EkUeEXyvnxNkcNzAyJNvKDrB8D96j9PrcdVdvdZZNJeCXAgIIEJ0sWMWLpPFQrlKLX40zdkiW1wtsGnpBoyyE4OErdUxnLIRTK+We7bFh6qlr3R2D+51Ufrqvv2lgDbjKfv6clvG/rWqzRctyUijVdo3HueGgRaDfiFIQZ/+EAEPRXgSmKF6A6ztclirL4kT36S0MNjoQykG6a9gWr63Y0FS7tWpQpcpNgVFeyiNEANyYJ2T+Y6Sab7/KkaBQD0dVUV9Ebx0VZkYhUApbayfdqPRSPE7mvCLJ+GR8bwc+QgWK8d1LiJJnOsaXSaAQVTJvNpcLHe3aM+3LUrZYpgfVeRrIUW+klij6oJ6gfM4RB4bk9LZiM9DULUZhT3aVa5kx6BCEonauNDIF7ijyw3YJUuJLyUAYqKP88ECjpHuptdK1TW/cTcoUlXNdjDDwymPHAdE+mHltIOkN7dM0zRC1PR0o1mExyH7CswFvcJw3qn2kcJgayP2XFl4Gh6vJTSbvFmEJ5r+zekO8/hLAxSSmaFZBBDXXwAXN04RfoXqyl6ExPO2CjWHhcaBV9wJkMduEcKssrTPpLIoARTVuRpPlh9ZFtZg+ihlowe2yF2NiMnVJJ7XOIqTa1DdcGx4GdSPp8PqS+1xFSRFpfwTQhMwl4c1YKhoNHfWSkCGug9UU4TlvB54F4baRlyrBQLeteL5g7GdzZvkvo/hjNhOGYXRZw+lJUX6zMHKpmYYA3y7OudSrlU7G8jADeZ+BwYP5Yb5CkqID+kavEJ72xKsUvIb7eblOO6eEwOPpdczAJ7kvZhz67B97Yz1xFesf5H1Kp++QBGe0b+Vt8uKiGfULBJ0o/0mXZ9Dv58OXISdw/xBvqcsJhOP2cM3USsg8pS4BY09txHvAXpjBF76XTlEPKimbKL41BGPv2yAwk+iUtogHwcEcGtS9IKoqUPaJTxHfdiuH0rMpjH/JTaA5N5P5mwSjQPv+xB9H15RosaPhTVl2r2HANFduxnrw3CMrXP+fiFrKXnMn6j8gfl11S23qB6ccQ6oFVa3NnLqWJuaWkFd/CfUo4JHql2+LhJ2PjB7/Wk/uI3zZpvLikGKUtDTpW2ySq+naQALpDp19K2CEONqtq4pDWXwXXbefH6LvaWBSOrjFi7s9zjDGxg8HdlNvP3xnuBVmrWp/ggCQQZOIso/nvAl8gquUpqpuW8P6qFUROwBEv7YPfv0dQPDquIXkPznwWLEgvQwMlLkCs4b3XGkotoFeXHrNchDxD0ERhGsAV+CtUo331AtlGlza45YFrks5rtBfcLbG0SwjuEb2vDwWbWQ6W7CSh7J+2SDPqxS7aMNDmMwCakKnVd2y16A/37slUUZK23LHGa6droSGV8PFClNozIm5PltAQAAyegq5T64SF8PuVj9Oz1y/BAUB1OmdwpK6g+YUVb3AleqAqoy11xp7u4yZ9OyCFtfI/I3nUZCzpunY/AFe4Rjl2TjxKzhDKZq4cbeyoIkP30kfRJ3E+YQ8d1RMV9/1+rkyzgXvq/pJvhTN75pYP5xN/6v5cDXHP/XQVEqDzWMyWi9tBz2zHmKHdiChp0sSlRJsRyULJgj+2PakG/IPc96j3z20jtvB8YvFoPkBLM5goaL+iQPD1sulvZ3U/ImiXybsfchyBJpc2uai3ihqdKZbBqoYoyeDDNQHMaMGQHcJbLxQXQqcKZJ0qK8xSvwCkGFNYWLcerGJxDZ4ERyc6EeK+qr0BWeg1i+FdsZ4UZAato5NOWk5Qevivqe0JBbxCye/fTaNI8Ka5KenXMZiZCYm6/+wzgsGSROVMIawHD6W0/Vtm0PgC3PhKddQnkY9mTnHFEI5cHQdDiIYqFqFvKvx3BUVuyRrUSCGHph6ncahP4szXb0KnGhH4aolxdaZUmseS+PQ8gQltMec1wFxSxWjJC5KI14J/hKboNJa/uaMz166Wny/aDXh2E+IWluPhoC45NZDfU8kxJIiH+vznpffucEj4OcmZdA3AAS7SPxKfnYs52oa2Vs/YfmbzJ/jWUUhuLqNEXwKlAy2V9qyvFsgsYMKVVFsI/RtIW5RQLiEXKXR02KGuN/NlZHpizx/6hCq+CJyiS8nGPUMsIW/Mlj8CzueJ17tO0shjC8E/B/7UvFTFtjnjjgeXAWma/h972YNOwqWgeIeAbH9eY4rP2rv+agZBKeulxXRyqjT7GA5hMECrVSklGpZsgStwdlLAXZjCHiGR/HjzwhK5bIJ9FU7B4kum9qEWkTkB2+bIpU4AliFDwWMcxPHdJwhbaWqcgHPF1uigqVdSXv4xNJa4nvHJCLGkewH4p3j0ATf9mz5IUbe5nhKIKqzSCbNM0iBatUcdYjgJQIQ4R0zSsE6AyHxAzXANtfhwJtnD+wxEamwYEamfLslrWUa3ATmAKULwf2Dn2bvMX/coetWoULszMkwjWMq9Xv4mAMjDMB8bISV4zQ4NDQxhGo59Bn+O5UwjlbGz09Kv6SuY4vkeGhGm4CGIWQJP4bhHmVJD+YR8KJaRNHmNqTC59OzWrpDzB6j74dxjSQC0ZjDX0OmaIuxxeeU1mjL4ArsHF4vttNv8G+0bqZ8IdFkgtH8CQL+hQCa7nr2V+LcMW6VOHAKfwp9WDyWfoj1/UVlpx9iZHeSkNIE3Z+YRgDgfCN1EAtQZy45ph613HpxpQ5cGXtAN+KBFtBSqRAdAUNbug/D25R2Ofn9kmnMUMQE87E2A
        - #2:
          - type: tool-call
          - toolCallId: 28mKxQyWHvm3ID2V
          - toolName: set-research
          - input:
            - Rationale: Advanced Ballistics is a crucial late-game technology that unlocks the Nuclear Missile for strategic deterrence, the Guided Missile, and the SS Booster. This supports our long-term defense and technological parity with advanced civilizations like Byzantium and America.
            - Technology: Advanced Ballistics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: fiun7J7lHQfIL6yB
          - toolName: set-flavors
          - input:
            - Rationale: We are shifting our Grand Strategy to 'UnitedNations' to address the imminent threat of a Byzantine Diplomatic or Cultural victory. Maximizing Diplomacy and Gold will allow us to leverage Germany's unique traits (gifting units and Hanse trade routes) to contest city-state alliances and block Byzantium's delegate count. We also maximize Happiness and Culture to combat our low happiness and build defenses against Byzantium's massive tourism.
            - GrandStrategy: UnitedNations
            - Flavors:
              - Culture: 100
              - Diplomacy: 100
              - Mobilization: 80
              - Happiness: 100
              - Espionage: 90
              - Gold: 100
              - Production: 100
              - Offense: 50
              - MilitaryTraining: 70
              - Science: 80
              - Defense: 80
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 4j9dM89hzqVps1y5
          - toolName: set-persona
          - input:
            - Loyalty: 10
            - Friendliness: 7
            - VictoryCompetitiveness: 10
            - HostileBias: 8
            - MinorCivCompetitiveness: 10
            - MinorCivFriendlyBias: 10
            - Rationale: Adjusting our diplomatic persona to highly prioritize city-states and victory competitiveness. This aligns with our pivot to a United Nations diplomatic defense strategy, ensuring we aggressively contest city-states while maintaining strong alliance loyalty with Mongolia.
            - Meanness: 7
            - Boldness: 7
            - DeceptiveBias: 8
            - WarBias: 6
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: cKb2gTZAKzYtZWoS
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
          - toolCallId: 28mKxQyWHvm3ID2V
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: fiun7J7lHQfIL6yB
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 4j9dM89hzqVps1y5
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.