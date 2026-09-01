- row:
  - game_id: b24d37ee-16aa-4fcf-b43d-72e129c1a1e3
  - player_id: 2
  - turn: 395
  - player_type: Kimi-K2.5-Simple
  - prev_use_nuke: 95.0
  - after_use_nuke: 100.0
  - prev_nuke: 100.0
  - after_nuke: 100.0
  - rationale: Critical survival mode: Austrian military strength increased to 25,518 (6.8:1 ratio) with peace treaty expired. Reduced Offense to 0 to stop wasting resources on Polynesian war - need immediate consolidation. Maintained Defense/Mobilization/Nuke at maximum for existential defense. Increased Spaceship to 70 as backup victory path. Espionage at 100 to steal technologies from Austria. We have 7 turns to achieve Influential with Babylon for Cultural Victory while surviving Austrian onslaught. Nuclear deterrence is our only hope.
- originalModel: openai-compatible/Kimi-K2.5@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: true
  - messagesModified: true
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 100
  - replay_use_nuke: 95
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
    - You are Pedro II, leader of Brazil (Player 2).
      
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
      - Name: Brazil
      - Uniques:
        - Unique Unit: Bandeirante, Replacing Explorer (Requires technology: Compass)
        - Unique Unit: Amazonas, Replacing Ironclad (Requires technology: Industrialization)
        - Unique Building: Embrapa, Replacing Research Lab (Requires technology: Plastics)
        - Unique Improvement: Brazilwood Camp (Can only be built on Jungle or Forest tiles without access to Fresh Water, and cannot be built adjacent to another Brazilwood Camp. It spawns and connects a Brazilwood Resource under the tile.); Requires technology: Calendar
        - Civilization Ability: "We Love the King Day" becomes Carnival, adding -50% Unhappiness from Needs. When a Golden Age begins, 30% of Golden Age Points convert into Gold and Tourism, and Cities gain 10 turns of Carnival.
      - Leader: Pedro II
      - PlayerID: 2
      
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
      - Computers: Grants an additional Trade Route. Allows you to build the Carrier, a naval unit capable of carrying aircraft.
        Completing it would unlock: Telecommunications, Satellites
      - Advanced Ballistics: Allows you to build the Nuclear Missile, a frightening weapon that requires Uranium, and is capable of destroying units and cities. Also allows you to build the Guided Missile, an inexpensive single-use Unit that can damage enemy Units, and the SS Booster, one of the Spaceship parts necessary to win a Science Victory.
        Completing it would unlock: Lasers, Stealth
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      - Mobile Tactics: Allows you to build the Mechanized Infantry, a fast and versatile late game Unit that doesn't require any resources.
        Completing it would unlock: Stealth
      
      ## Policies
      - Dictatorship of the Proletariat (Level 2 Tenet of Ideology Order): Dictatorship of the Proletariat: +7 Food, Science, Gold, and Culture per city.
      - Five-Year Plan (Level 2 Tenet of Ideology Order): Five-Year Plan: +20% Production towards Buildings in all Cities. +3 Production for every Mine, Quarry, Lumber Mill, Oil Well, and Unique Improvement.
      - Nationalization (Level 2 Tenet of Ideology Order): Nationalization: Each Corporate Office counts as a Franchise. Foreign Franchises no longer benefit your Corporation, you can no longer construct Franchises in foreign Cities (except Vassals), and foreign Corporations can no longer set up Franchises in your Cities (except Masters). +2 Science from all Corporation Offices.
      - Great Leap Forward (Level 2 Tenet of Ideology Order): Great Leap Forward: Receive a free Technology. Spies gain +100% Science. +1 Science in Cities for every 3 non-Specialist Citizens.
      - Resettlement (Level 2 Tenet of Ideology Order): Resettlement: New Cities have +3 Population. All Cities gain +2 Citizens immediately. No Partisans from razing enemy Cities.
      - Peace, Land, Bread (Level 1 Tenet of Ideology Order): Peace, Land, Bread: -2 Unhappiness from Poverty and Growth increased by 20% in all Cities. Building maintenance reduced by 20%.
      - Communism (Level 1 Tenet of Ideology Order): Communism: Gold cost of investing in buildings reduced by 25%. +20% Production when building Wonders.
      - Hero of the People (Level 1 Tenet of Ideology Order): Hero of the People: Great Person rate increases by 25%. A Great Person of your choice appears near your Capital.
      - Cultural Revolution (Level 2 Tenet of Ideology Order): Cultural Revolution: +25% Tourism to civilizations with less Happiness. +1 Happiness from Factories.
      - Double Agents (Level 1 Tenet of Ideology Order): Double Agents: Receive 200 Spy Points. Gain 125 Science when you identify a foreign Spy, scaling with Era.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Trade Confederacy (Continuing Statecraft Branch):
        - * +25% Yields for International Trade Routes.
        - * Trade Routes to City-States generate +1 Influence per turn (with the target City-State) per each owned City-State Trade Route (up to +5).
      - Ceremony (Continuing Tradition Branch):
        - * +1 Happiness from National Wonders with Building requirements.
        - * +25% Production toward National Wonders with Building requirements.
        - * Royal Astrologer built in Capital (+3 Science, +1 Science to all Councils, Smokehouses, and Herbalists; 1 Scientist Slot).
      - Justice (Continuing Tradition Branch):
        - * +1 Production in every City.
        - * Cities with a garrison gain +25% Ranged Combat Strength.
        - * Royal Guardhouse built in Capital (+3 Production, +2 Defense, +50 Hit Points, +10% Military Supply from Population in all Cities, 1 Engineer Slot).
      - Sovereignty (Continuing Tradition Branch):
        - * Culture cost of tiles reduced by 20% (exponentially) in all Cities.
        - * Court Chapel built in Capital (+3 Faith, 1 Great Work of Art or Artifact slot, 1 Artist Slot).
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Free Trade (Continuing Industry Branch):
        - * Earn Great Merchants 50% faster.
        - * +5 Gold from International Trade Routes.
        - * -2 Unhappiness from Poverty in all Cities.
      - Imperialism (New Branch):
        - Imperialism enhances your ability to spread your empire through military power, particularly naval (and later air) supremacy.
        - Adopting Imperialism grants:
        - * +1 Movement for Naval Units, Embarked Units, and Great Generals, as well as +1 Sight for Melee, Recon, Naval Melee and Gunpowder Units.
        - * +10% Production toward Military Units, -10% Gold required for upgrades.
        - Each Imperialism policy unlocked grants:
        - * +5% Production for Military Units, -5% Gold required for upgrades.
        - Adopting all policies in Imperialism grants:
        - * Unlocks building the Pentagon.
        - * All Naval and Air units gain the Banzai! Promotion (become stronger as they take damage).
        - * Allows for the purchase of Great Admirals with Faith starting in the Industrial Era.
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
      - Authority (New Branch):
        - Authority will greatly benefit warlike and expansionist civilizations.
        - Adopting Authority grants:
        - * +25% combat bonus VS Barbarians and receive announcements when Barbarian Camps spawn in revealed territory.
        - * Receive 25 Culture when you clear Barbarian Camps, scaling with Era.
        - * Receive Science and Culture when you kill a Unit equal to 50% of its Strength.
        - * +1 Production in every City.
        - Each Authority policy unlocked grants:
        - * Receive Science and Culture when you kill a Unit equal to 10% of its Strength.
        - Adopting all policies in Authority grants:
        - * Unlocks building Alhambra.
        - * Allows the purchasing of Free Companies, Foreign Legions, and Mercenaries as their prerequisite technologies are researched.
        - * Allows for the purchase of Great Generals with Faith starting in the Industrial Era.
  - messages:
    - #0:
      - role: user
      - content: # Strategies
        Strategies: existing strategic decisions from you.
        
        ## Persona
        - VictoryCompetitiveness: 9
        - WonderCompetitiveness: 6
        - MinorCivCompetitiveness: 8
        - Boldness: 2
        - WarBias: 2
        - HostileBias: 2
        - WarmongerHate: 10
        - NeutralBias: 8
        - FriendlyBias: 10
        - GuardedBias: 10
        - AfraidBias: 8
        - DiplomaticBalance: 8
        - Friendliness: 6
        - WorkWithWillingness: 10
        - WorkAgainstWillingness: 7
        - Loyalty: 1
        - MinorCivFriendlyBias: 3
        - MinorCivNeutralBias: 4
        - MinorCivHostileBias: 8
        - MinorCivWarBias: 2
        - DenounceWillingness: 4
        - Forgiveness: 3
        - Meanness: 1
        - Neediness: 6
        - Chattiness: 5
        - DeceptiveBias: 2
        - Rationale: Increasing WorkWithWillingness from 8 to 10 (maximum) to ensure complete military and diplomatic coordination with Babylon, our only defensive pact ally and sole cultural victory path. Austria's 5.5:1 military superiority (19,541 vs 3,547) requires maximum allied cooperation. With Austria now fighting Russia AND being attacked by Polynesia, we have a narrow window to achieve nuclear parity and cultural victory. Maximum willingness to work with allies essential for survival.
        
        ## Technology
        - Next: Advanced Ballistics
        - Rationale: Radar completes in 3 turns. Advanced Ballistics is the clear next priority - unlocks Nuclear Missiles for deterrence against Austria's 5x military advantage AND SS Booster for potential Science Victory pivot. Nuclear capability is our only path to credible defense against Austrian aggression when peace treaty expires in ~15 turns.
        
        ## Policy
        - Next: Dictatorship of the Proletariat (Policy)
        - Rationale: Next policy available in 20 turns. Order Level 2 tenet providing +7 Food, Science, Gold, Culture per city (42 total yields/turn with 6 cities). Essential for catching up to Austria economically and scientifically while maintaining tourism pressure for the final 8 turns to achieve Influential with Babylon. Raw yields take priority over Cultural Revolution's +25% tourism since we're already on track for cultural victory.
        
        ## Relationships
        
        ### Denmark
        - Public: 50
        - Private: 45
        - Rationale: Denmark is our loyal ally in crisis - 35% happiness but holding defensive pact with Korea. They face wars with Russia and Polynesia who captured Copenhagen. Polynesia proposing to sanction Denmark in World Congress - we must oppose this vigorously. Solidarity despite Austrian aggression.
        - UpdatedTurn: 261
        
        ### America
        - Public: 0
        - Private: 0
        - Rationale: Clarifying rationale: America (Player 1 = Denmark in original notation) previously misreferenced. America has not defeated Poland - Denmark is the defeated civilization. Austria now controls America (Washington). This relationship with the American civilization is irrelevant as Austria conquered them earlier. Setting neutral 0/0 since America no longer exists as independent actor.
        - UpdatedTurn: 339
        
        ### Austria
        - Public: 0
        - Private: -80
        - Rationale: Austrian peace treaty expired - total war is CERTAIN. Austria has 17,627 military strength vs Brazil's 3,496 (5:1 ratio), controls 37% of capitals for domination victory, and is Influential with 4 civs. Korea's capitulation gives Austria strategic depth. Public stance 0 maintains minimal diplomatic contact but signals no tolerance. Private opinion worsened to -80 reflecting absolute certainty of existential war. Austria is the primary threat to all Brazilian victory conditions.
        - UpdatedTurn: 384
        
        ### Babylon
        - Public: 100
        - Private: 100
        - Rationale: Babylon is Brazil's sole remaining victory path and only potential military ally. Babylon has nuclear capability (completed Manhattan Project), Order ideology alignment (+999), and defensive pact with us. We are 88% Popular with them, 9 turns from Influential at 290% tourism ratio. If Austria attacks either of us, the other must respond. Maximum relations are essential - any rupture dooms our cultural victory since we cannot influence Austria (42% Familiar, impossible trajectory).
        - UpdatedTurn: 390
        
        ### Korea
        - Public: -70
        - Private: -90
        - Rationale: Korea is Austrian vassal with Open Borders allowing Austrian military passage to our borders. Increasing negative relations to -70/-90 signals AI to distance from Korea immediately and NOT renew Open Borders expiring in 3 turns. Korea's DoF with us while being Austrian vassal creates critical security vulnerability - Austrian units can pass through Korean territory to attack us. This must be severed before Austrian peace treaty expires in 17 turns.
        - UpdatedTurn: 393
        
        ### Polynesia
        - Public: 50
        - Private: 40
        - Rationale: Peace established via Cold War resolution! Polynesia is no longer an enemy and is actively fighting Austria (our existential threat). Setting to +50/+40 signals willingness for normalized relations and potential cooperation. We share common religion (Buddhism) and common enemy. This frees all our military resources for Austrian defense.
        - UpdatedTurn: 394
        
        ### Russia
        - Public: 70
        - Private: 60
        - Rationale: Russia is fighting Austria (-6% war score) and buying us critical time. Increasing to +70/+60 to solidify anti-Austrian coordination. Russia's survival is essential to prevent Austrian domination victory (Austria already has 3/8 capitals). With our peace treaty expiring in 1 turn, we need Russia as an active ally against Austria.
        - UpdatedTurn: 394
        
        ## Strategy
        - Rationale: PEACE WITH POLYNESIA CHANGES EVERYTHING! Can now redirect all military from Polynesian war to Austrian defense. Cultural Victory path: 7 turns to Influential with Babylon (90% Popular). Must survive ~15 turns until Austrian war. Priorities: Defense/Mobilization/Nuke maxed for Austrian war prep, Science to complete Advanced Ballistics, Culture to finish victory with Babylon. Offense reduced to 20 to consolidate gains from Polynesian war, Mobile increased slightly for defensive flexibility.
        - GrandStrategy: Culture
        
        ### Flavors
        - Offense: 20
        - Defense: 100
        - Mobilization: 100
        - CityDefense: 100
        - MilitaryTraining: 95
        - Recon: 10
        - Ranged: 95
        - Mobile: 30
        - Nuke: 100
        - UseNuke: 95
        - Naval: 50
        - NavalRecon: 20
        - NavalGrowth: 40
        - NavalTileImprovement: 40
        - Air: 100
        - AirCarrier: 90
        - Antiair: 100
        - Airlift: 95
        - Expansion: 0
        - Growth: 60
        - TileImprovement: 70
        - Infrastructure: 80
        - Production: 90
        - WaterConnection: 50
        - Gold: 60
        - Science: 100
        - Culture: 95
        - Happiness: 70
        - GreatPeople: 90
        - Wonder: 20
        - Religion: 10
        - Diplomacy: 60
        - Spaceship: 60
        - Espionage: 100
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: Austria
        - Austria:
          - CapitalsControlled:
            - Vienna
            - Washington
            - Seoul
          - CapitalsPercentage: 37
        - Russia:
          - CapitalsControlled:
            - Moscow
            - Copenhagen
          - CapitalsPercentage: 25
        
        ## ScienceVictory
        - Unlocked in the Information era
        
        ## CulturalVictory
        - CivsNeeded: 5
        - Contender: Austria
        - Austria:
          - Influences:
            - Brazil: Popular (64%) - Rising (23 turns to Influential, tourism/culture ratio 414%)
            - Babylon: Influential (146%) - Rising (tourism/culture ratio 449%)
            - Polynesia: Influential (137%) - Rising (tourism/culture ratio 569%)
            - Russia: Influential (126%) - Rising (tourism/culture ratio 470%)
            - Korea: Influential (182%) - Rising (tourism/culture ratio 1336%)
          - PolicyPercentage: 100
          - InfluentialCivs: 4
        - Babylon:
          - Influences:
            - Austria: Exotic (24%) - Rising Slowly (tourism/culture ratio 60%)
            - Polynesia: Popular (51%) - Rising (101 turns to Influential, tourism/culture ratio 211%)
            - Russia: Familiar (43%) - Rising (288 turns to Influential, tourism/culture ratio 152%)
            - Brazil: Familiar (31%) - Rising (469 turns to Influential, tourism/culture ratio 154%)
            - Korea: Popular (58%) - Rising (54 turns to Influential, tourism/culture ratio 333%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Brazil:
          - Influences:
            - Austria: Familiar (44%) - Rising Slowly (tourism/culture ratio 110%)
            - Babylon: Popular (91%) - Rising (7 turns to Influential, tourism/culture ratio 287%)
            - Polynesia: Influential (184%) - Rising (tourism/culture ratio 657%)
            - Russia: Influential (151%) - Rising (tourism/culture ratio 449%)
            - Korea: Dominant (234%) - Rising (tourism/culture ratio 1182%)
          - PolicyPercentage: 100
          - InfluentialCivs: 3
        - Korea:
          - Influences:
            - Austria: Exotic (8%) - Rising Slowly (tourism/culture ratio 10%)
            - Babylon: Exotic (14%) - Rising Slowly (tourism/culture ratio 22%)
            - Polynesia: Familiar (37%) - Rising Slowly (tourism/culture ratio 68%)
            - Russia: Familiar (31%) - Rising Slowly (tourism/culture ratio 45%)
            - Brazil: Exotic (23%) - Rising Slowly (tourism/culture ratio 48%)
          - PolicyPercentage: 92
          - InfluentialCivs: 0
        - Polynesia:
          - Influences:
            - Austria: Exotic (6%) - Rising Slowly (tourism/culture ratio 17%)
            - Babylon: Exotic (11%) - Rising Slowly (tourism/culture ratio 34%)
            - Korea: Familiar (32%) - Rising (914 turns to Influential, tourism/culture ratio 164%)
            - Russia: Familiar (27%) - Rising Slowly (tourism/culture ratio 83%)
            - Brazil: Exotic (16%) - Rising Slowly (tourism/culture ratio 64%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Russia:
          - Influences:
            - Austria: Exotic (11%) - Rising Slowly (tourism/culture ratio 34%)
            - Babylon: Exotic (18%) - Rising Slowly (tourism/culture ratio 63%)
            - Polynesia: Familiar (42%) - Rising (159 turns to Influential, tourism/culture ratio 191%)
            - Korea: Familiar (37%) - Rising (179 turns to Influential, tourism/culture ratio 231%)
            - Brazil: Exotic (19%) - Rising Slowly (tourism/culture ratio 96%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        
        ## DiplomaticVictory
        - VotesNeeded: 45
        - Status: World Congress - Voting in 9 turns
        - ActiveResolutions:
          - Casus Belli:
            - Description: The world recognizes the need for justifiable war to resolve diplomatic disputes.
              While this resolution is active, unit maintenance costs are lowered by 15% Gold. 0.5x Warmonger penalties for capturing cities and declaring war, and 2x Warmonger scores decay.
            - EnactedOn: -1
          - Natural Heritage Sites:
            - Description: Each Natural Wonder provides +2 to all Yields when worked.
            - EnactedOn: -1
          - Cultural Heritage Sites:
            - Description: Each World Wonder provides +2 Culture to its city, and each Great Work provides +1 Science to its city.
            - EnactedOn: 325
          - Sanction: Polynesia:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: 369
          - Brazilian Sphere of Influence: Ban Chiang:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 336
          - Babylonian Sphere of Influence: Oviedo:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 358
          - Open Door: Bunkeya:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 347
          - Austrian Sphere of Influence: Palatium:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Austrian Sphere of Influence: Assur:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 358
          - Open Door: Ecbatana:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - Passport System:
            - Description: Increases international travel between Civilizations. Increases the Tourism modifier for all Civilizations by 50%.
              Available once any Civilization discovers Flight.
            - EnactedOn: 369
          - Austrian Sphere of Influence: Milan:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 314
          - Spaceflight Regulations:
            - Description: Spaceflight Regulations control the proliferation of modern ballistic technology, oversee national space programs, and limit the advance of pontentially-dangerous technology.
              As long as this resolution is active, all players will suffer a global -25% Production penalty for Spaceship Parts and +25% Gold purchase costs for Spaceship Parts.
              Available once any Civilization discovers Atomic Theory.
            - EnactedOn: 380
          - Sanction: Russia:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: -1
          - Brazilian Sphere of Influence: La Venta:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 314
          - Open Door: Cahokia:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - Ban Luxury: Tea:
            - Description: A Luxury resource is designated as immoral, endangered, or otherwise inappropriate for use by the general population. As long as the ban is in place, Civilizations receive no Happiness or Monopoly benefits from this Luxury resource.
            - EnactedOn: -1
        - Proposals:
          - Enact: World Ideology: Freedom:
            - Description: Designate an Ideology as the official World Ideology. Civilizations following the Ideology get an additional Delegate, plus 1 Delegate for every other Civilization that follows the Ideology. Public opinion in favor of that Ideology is increased for all Civilizations. Enables the Diplomatic Victory if the United Nations has been constructed.
              Available once any Civilization discovers Nuclear Fission.
            - Proposer: Austria
          - Enact: Decolonization:
            - Description: Enforce global decolonization. If successful, the Influence of all Players with all City-States is lowered to 50, unless they are permanent allies.
              Available once any Civilization discovers Radio.
            - Proposer: Brazil
          - Repeal: Casus Belli:
            - Description: The world recognizes the need for justifiable war to resolve diplomatic disputes.
              While this resolution is active, unit maintenance costs are lowered by 15% Gold. 0.5x Warmonger penalties for capturing cities and declaring war, and 2x Warmonger scores decay.
            - Proposer: Polynesia
        - Contender: Austria
        - Austria:
          - Delegates: 42
          - VictoryPercentage: 93
        - Babylon:
          - Delegates: 9
          - VictoryPercentage: 20
        - Brazil:
          - Delegates: 16
          - VictoryPercentage: 35
        - Korea:
          - Delegates: 5
          - VictoryPercentage: 11
        - Polynesia:
          - Delegates: 11
          - VictoryPercentage: 24
        - Russia:
          - Delegates: 6
          - VictoryPercentage: 13
        
        # Players
        Players: summary reports about visible players in the world.
        
        ## Player 0
        - Civilization: Austria
        - Leader: Maria Theresa
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Austria) have denounced one of Brazil's declared enemies! (11)
          - We are trade partners. (10)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - You (Austria) have gone to war in the past.
          - Brazil's real approach to Austria is Guarded.
          - You (Austria) have denounced a leader Brazil made a Declaration of Friendship with! (-11)
          - Religious differences strain your (Austria) relationship. (-30)
          - Your (Austria) spies were caught stealing from Brazil. (-33)
          - Brazil's leader has formed a private opinion of Austria (-80).
          - Brazil fear your (Austria) warmongering will end this world in fire! (-222)
          - You (Austria) have chosen to adopt the Freedom Ideology, but Brazil believe in Order. (-999)
        - TheirOpinionOfUs:
          - We previously passed Austria's proposal in the United Nations.
          - We are trade partners.
          - You (Brazil) have denounced one of Austria's declared enemies!
          - We have made Declarations of Friendship with the same leaders!
          - Your (Brazil) recent diplomatic actions please Austria.
          - We have Pledged to Protect the same City-States.
          - We fought together against a common foe.
          - You (Brazil) have gone to war in the past.
          - You (Brazil) promised not to declare war on each other for 15 more turns.
          - Austria don't want anything to do with us (Brazil) right now.
          - Religious differences strain your (Brazil) relationship.
          - Austria believe we are building World Wonders too aggressively!
          - Territorial disputes strain your (Brazil) relationship.
          - You (Brazil) are competing for World Wonders.
          - You (Brazil) have made a Defensive Pact with one of Austria's enemies!
          - You (Brazil) have made a Declaration of Friendship with one of Austria's enemies!
          - You (Brazil) are competing for the favor of the same City-States!
          - Austria suspect you (Brazil) are competing with Austria.
          - We have denounced each other!
          - Austria disliked our proposal to the United Nations.
          - Your (Brazil) spies were caught stealing from Austria.
          - Your (Brazil) votes opposed Austria's civ's interests in the United Nations.
          - You (Brazil) have chosen to adopt the Order Ideology, but Austria believe in Freedom.
        - Score: 4235
        - Era: Information
        - GoldenAge: 32 turns remaining
        - Technologies: 68
        - Cities: 24
        - Population: 550
        - Territory: 919
        - Gold: 45408
        - GoldPerTurn: 908
        - HappinessSituation: Happy
        - HappinessPercentage: 65
        - MilitaryStrength: 25518
        - TourismPerTurn: 1942.25
        - CulturePerTurn: 6088
        - PolicyBranches:
          - Industry: 6
          - Freedom: 11
          - Tradition: 6
          - Artistry: 6
        - ResourcesAvailable:
          - Wheat: 5
          - Sheep: 7
          - Ivory: 2
          - Gold: 4
          - Paper: 16
          - Pearls: 2
          - Maize: 4
          - Rice: 2
          - Cotton: 3
          - Gems: 4
          - Salt: 10
          - Aluminum: 43
          - Bison: 12
          - Amber: 7
          - Olives: 2
          - Deer: 4
          - Jade: 1
          - Dyes: 2
          - Iron: 15
          - Tea: 2
          - Fish: 33
          - Cattle: 5
          - Horses: -2
          - Coral: 2
          - Citrus: 2
          - Copper: 2
          - Truffles: 5
          - Crab: 1
          - Stone: 7
          - Marble: 3
          - Wine: 1
        - FoundedReligion: Catholicism
        - Relationships:
          - Brazil:
            - Distance: Neighbors
            - Denounced Them
          - Babylon:
            - Distance: Neighbors
            - Denounced Them
            - Denounced By Them
          - Polynesia:
            - Distance: Close
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
          - Russia:
            - Distance: Neighbors
            - War (Our Score: 8%; Our War Weariness: 1%)
            - Denounced Them
          - Korea:
            - Distance: Neighbors
            - Our Vassal (Capitulated)
            - Open Borders
            - Declaration of Friendship
        - Votes: 42
        - 1: Defeated Major Civilization America
        
        ## Player 2
        - Civilization: Brazil
        - Leader: Pedro II
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: Babylon, Our top defensive pact ally: None
          - Our top United Nations ally: Korea, Our top United Nations rival: Austria
          - Our top Competitor: Austria
        - Score: 2243
        - Era: Atomic
        - GoldenAge: Estimated in 20 turns
        - Technologies: 66
        - CurrentResearch: Radar (Estimated in 1 turns)
        - NextPolicyTurns: 15
        - Cities: 6
        - Population: 151
        - Territory: 206
        - Gold: 1333
        - GoldPerTurn: 324
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryUnits: 39
        - MilitarySupply: 39
        - MilitaryStrength: 3771
        - TourismPerTurn: 951.71
        - CulturePerTurn: 1391
        - FaithPerTurn: 268
        - SciencePerTurn: 1661
        - PolicyBranches:
          - Order:
            - People's Army
            - Patriotic War
            - Academy of Sciences
            - Workers' Faculties
          - Tradition:
            - Tradition
          - Artistry:
            - Artistry
            - Humanism
            - Refinement
            - Heritage
            - National Treasure
            - Cultural Exchange
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Consulates
            - Shadow Networks
          - Rationalism:
            - Rationalism
            - Scientific Revolution
            - Rights of Man
            - Empiricism
          - Industry:
            - Industry
          - Progress:
            - Progress
            - Organization
            - Liberty
            - Expertise
            - Equality
            - Fraternity
        - ResourcesAvailable:
          - Wheat: 0
          - Silver: 0
          - Sheep: 4
          - Cloves: 0
          - Figs: 0
          - Ivory: 0
          - Gold: 1
          - Nutmeg: 0
          - Paper: 7
          - Glass: 0
          - Pearls: 0
          - Maize: 4
          - Rice: 3
          - Cotton: 1
          - Gems: 1
          - Salt: 0
          - Brazilwood: 10
          - Aluminum: 4
          - Lapis Lazuli: 0
          - Bison: 0
          - Perfume: 0
          - Amber: 0
          - Olives: 0
          - Deer: 1
          - Whales: 0
          - Jade: 0
          - Sugar: 0
          - Dyes: 1
          - Iron: 0
          - Tea: 0
          - Coffee: 0
          - Coal: 14
          - Fish: 6
          - Cattle: 0
          - Pepper: 0
          - Uranium: 4
          - Horses: 12
          - Coral: 0
          - Silk: 0
          - Jewelry: 0
          - Hidden Antiquity Site: 0
          - Antiquity Site: 0
          - Citrus: 0
          - Copper: 1
          - Truffles: 0
          - Crab: 1
          - Incense: 0
          - Stone: 3
          - Marble: 1
          - Furs: 0
          - Cinnamon: 0
          - Bananas: 4
          - Oil: 0
          - Wine: 0
          - Porcelain: 0
          - Cocoa: 5
          - Tobacco: 0
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - Denounced Them
          - Babylon:
            - Distance: Far
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Polynesia:
            - Distance: Neighbors
            - War (Our Score: 54%; Our War Weariness: 50%)
            - Denounced Them
          - Russia:
            - Distance: Close
            - Peace Treaty
            - Denounced Them
          - Korea:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
        - OutgoingTradeRoutes:
          - Salvador (Brazil) => Brasilia (Brazil):
            - ToFood: 32.4
            - TurnsLeft: 11
            - Domain: Land
          - Rio de Janeiro (Brazil) => La Venta (City-State La Venta):
            - TurnsLeft: 7
            - FromScience: 6
            - Domain: Land
            - FromGold: 41.18
            - FromCulture: 6
          - Rio de Janeiro (Brazil) => Viborg (Brazil):
            - ToFood: 27.8
            - TurnsLeft: 18
            - Domain: Land
          - Sao Paulo (Brazil) => Viborg (Brazil):
            - ToFood: 33.8
            - TurnsLeft: 9
            - Domain: Land
          - Viborg (Brazil) => Ban Chiang (City-State Ban Chiang):
            - TurnsLeft: 27
            - FromScience: 6
            - Domain: Land
            - FromGold: 32.45
            - FromCulture: 6
          - Rio de Janeiro (Brazil) => Aotearoa (Brazil):
            - ToFood: 29.2
            - TurnsLeft: 28
            - Domain: Land
          - Sao Paulo (Brazil) => Aotearoa (Brazil):
            - TurnsLeft: 3
            - Domain: Land
            - ToProduction: 24
          - Salvador (Brazil) => Aotearoa (Brazil):
            - ToFood: 33.8
            - TurnsLeft: 8
            - Domain: Land
          - Sao Paulo (Brazil) => Brasilia (Brazil):
            - TurnsLeft: 20
            - Domain: Land
            - ToProduction: 23
          - Rio de Janeiro (Brazil) => Daegu (Korea):
            - ToGold: 3.75
            - TurnsLeft: 22
            - FromScience: 10
            - Domain: Land
            - FromGold: 44.7
            - ToCulture: 4
            - ToScience: 2
          - Rio de Janeiro (Brazil) => Busan (Korea):
            - ToGold: 9.09
            - TurnsLeft: 12
            - FromScience: 10
            - Domain: Land
            - FromGold: 62.38
            - ToCulture: 4
            - ToScience: 2
          - Rio de Janeiro (Brazil) => Brasilia (Brazil):
            - ToFood: 27.8
            - TurnsLeft: 25
            - Domain: Land
        - IncomingTradeRoutes:
          - Vienna (Austria) => Sao Paulo (Brazil):
            - ToGold: 8.75
            - TurnsLeft: 17
            - FromScience: 6
            - Domain: Sea
            - FromGold: 82.62
            - ToCulture: 2
            - ToScience: 2
          - Akkad (Babylon) => Salvador (Brazil):
            - ToGold: 11.25
            - TurnsLeft: 29
            - FromScience: 4
            - Domain: Sea
            - FromGold: 39.64
            - ToScience: 2
          - Vienna (Austria) => Salvador (Brazil):
            - ToGold: 8.75
            - TurnsLeft: 9
            - FromScience: 6
            - Domain: Sea
            - FromGold: 76.38
            - ToCulture: 2
            - ToScience: 2
          - Daegu (Korea) => Salvador (Brazil):
            - ToGold: 12.22
            - TurnsLeft: 11
            - FromScience: 14
            - Domain: Land
            - FromGold: 31.03
            - FromCulture: 24
          - Daegu (Korea) => Aotearoa (Brazil):
            - ToGold: 6.5
            - TurnsLeft: 13
            - FromScience: 14
            - Domain: Land
            - FromGold: 23.17
            - FromCulture: 24
          - Busan (Korea) => Viborg (Brazil):
            - ToGold: 15.45
            - TurnsLeft: 26
            - FromScience: 14
            - Domain: Land
            - FromGold: 36.23
            - FromCulture: 24
          - Vienna (Austria) => Rio de Janeiro (Brazil):
            - ToGold: 13.75
            - TurnsLeft: 20
            - FromScience: 6
            - Domain: Sea
            - FromGold: 85.7
            - ToCulture: 2
            - ToScience: 2
          - Busan (Korea) => Rio de Janeiro (Brazil):
            - ToGold: 17.68
            - TurnsLeft: 25
            - FromScience: 14
            - Domain: Land
            - FromGold: 45.31
            - FromCulture: 24
          - Busan (Korea) => Brasilia (Brazil):
            - ToGold: 7.93
            - TurnsLeft: 8
            - FromScience: 14
            - Domain: Land
            - FromGold: 33.23
            - FromCulture: 24
        - Spies:
          - Agent Domingos (6):
            - State: Traveling
            - Role: Spy
            - Location: Raiatea (Polynesia)
            - NetworkPerTurn: 0
          - Agent Fernão (3):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 77
            - Location: Vienna (Austria)
            - NetworkPerTurn: 33
          - Agent Natanael (1):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 98
            - Location: Honolulu (Polynesia)
            - NetworkPerTurn: 60
          - Agent Estêvão (7):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 118
            - Location: Samoa (Polynesia)
            - NetworkPerTurn: 60
          - Agent Gabriela (5):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 120
            - Location: Kaupang (Polynesia)
            - NetworkPerTurn: 60
          - Agent Marcelino (4):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 1161
            - Location: Tonga (Polynesia)
            - NetworkPerTurn: 45
          - Agent Tio (2):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 921
            - Location: Nuku Hiva (Polynesia)
            - NetworkPerTurn: 53
          - Agent Tomé (0):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 120
            - Location: Tunsberg (Polynesia)
            - NetworkPerTurn: 60
        - DiplomaticDeals:
          - Korea:
            - #0:
              - WeGive:
                - Open Borders
                - 2 Gold per Turn
              - TheyGive:
                - Open Borders
              - TurnsRemaining: 1
            - #1:
              - WeGive:
                - 1 Cocoa
              - TheyGive:
                - 7 Gold per Turn
              - TurnsRemaining: 9
            - #2:
              - WeGive:
                - 1 Dyes
              - TheyGive:
                - 7 Gold per Turn
              - TurnsRemaining: 28
            - #3:
              - WeGive:
                - 1 Brazilwood
              - TheyGive:
                - 7 Gold per Turn
              - TurnsRemaining: 30
            - #4:
              - WeGive:
                - 2 Coal
              - TheyGive:
                - 50 Gold per Turn
              - TurnsRemaining: 30
          - Russia:
            - #0:
              - WeGive:
                - Peace Treaty
              - TheyGive:
                - Peace Treaty
                - Make Peace with City-State Ban Chiang
                - Make Peace with City-State La Venta
              - TurnsRemaining: 0
          - Babylon:
            - #0:
              - WeGive:
                - 1 Brazilwood
              - TheyGive:
                - 7 Gold per Turn
              - TurnsRemaining: 2
            - #1:
              - WeGive:
                - 7 Gold per Turn
              - TheyGive:
                - 1 Cotton
              - TurnsRemaining: 16
            - #2:
              - WeGive:
                - 54 Gold per Turn
              - TheyGive:
                - 4 Aluminum
              - TurnsRemaining: 17
            - #3:
              - WeGive:
                - 1 Cocoa
              - TheyGive:
                - 7 Gold per Turn
              - TurnsRemaining: 20
            - #4:
              - WeGive:
                - 3 Gold per Turn
              - TheyGive:
                - Open Borders
              - TurnsRemaining: 28
            - #5:
              - WeGive:
                - Open Borders
              - TheyGive:
                - 2 Gold per Turn
              - TurnsRemaining: 29
            - #6:
              - WeGive:
                - 1 Copper
              - TheyGive:
                - 26 Gold per Turn
              - TurnsRemaining: 33
            - #7:
              - WeGive:
                - Defensive Pact
              - TheyGive:
                - Defensive Pact
                - 2 Gold per Turn
              - TurnsRemaining: 39
            - #8:
              - WeGive:
                - 2 Coal
              - TheyGive:
                - 71 Gold per Turn
              - TurnsRemaining: 42
            - #9:
              - WeGive:
                - 8 Gold per Turn
              - TheyGive:
                - 1 Marble
              - TurnsRemaining: 46
        - Votes: 16
        
        ## Player 3
        - Civilization: Korea
        - Leader: Sejong
        - IsMajor: true
        - OurOpinionOfThem:
          - We are trade partners. (40)
          - We fought together against a common foe. (30)
          - We have adopted the same religion in the majority of our cities. (30)
          - We have opened our borders to each other. (12)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have similar Social Policies. (3)
          - We have shared embassies. (1)
          - Brazil's real approach to Korea is Friendly.
          - You (Korea) have made a Declaration of Friendship with one of Brazil's enemies! (-13)
          - We defeated Brazil's proposal in the United Nations. (-36)
          - Brazil's leader has expressed a public opinion of Korea (-70).
          - Brazil's leader has formed a private opinion of Korea (-90).
          - You (Korea) have adopted the Freedom Ideology, but Brazil believe in Order. (-999)
        - TheirOpinionOfUs:
          - Your (Brazil) votes supported Korea's civ's interests in the United Nations.
          - We are trade partners.
          - We fought together against a common foe.
          - We have similar Social Policies.
          - We have made a public Declaration of Friendship!
          - We have made Declarations of Friendship with the same leaders!
          - Korea liked our proposal to the United Nations.
          - You (Brazil) have denounced one of Korea's declared enemies!
          - You (Brazil) have shared intrigue with Korea.
          - Your (Brazil) recent diplomatic actions please Korea.
          - We have opened our borders to each other.
          - We have adopted the same religion in the majority of our cities.
          - We have shared embassies.
          - You (Brazil) have chosen to adopt the Order Ideology, but Korea believe in Freedom.
          - Korea desire friendly relations with Brazil.
          - You (Brazil) have denounced a leader Korea made a Declaration of Friendship with!
        - Score: 999
        - Era: Atomic
        - GoldenAge: 7 turns remaining
        - Technologies: 64
        - Cities: 2
        - Population: 42
        - Territory: 44
        - Gold: 820
        - GoldPerTurn: 92
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 709
        - TourismPerTurn: 104
        - CulturePerTurn: 498
        - PolicyBranches:
          - Freedom: 1
          - Tradition: 4
          - Artistry: 2
          - Statecraft: 1
          - Rationalism: 3
          - Industry: 1
          - Progress: 6
        - ResourcesAvailable:
          - Wheat: 1
          - Sheep: 1
          - Ivory: 1
          - Paper: 5
          - Rice: 1
          - Cotton: 1
          - Brazilwood: 1
          - Jade: 1
          - Iron: 1
          - Dyes: 1
          - Coal: 3
          - Cattle: 1
          - Copper: 2
          - Truffles: 1
          - Cocoa: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - Our Master (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Babylon:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - Polynesia:
            - Distance: Neighbors
            - War (Our Score: -4%; Our War Weariness: 2%)
          - Russia:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 0%)
          - Brazil:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
        - Votes: 5
        
        ## Player 4
        - Civilization: Babylon
        - Leader: Nebuchadnezzar II
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Babylon) have both chosen to adopt the Order Ideology. (999)
          - Brazil's leader has expressed a public opinion of Babylon (100).
          - Brazil's leader has formed a private opinion of Babylon (100).
          - We are trade partners. (40)
          - We have made a Defensive Pact! (20)
          - We have opened our borders to each other. (12)
          - You (Babylon) have denounced one of Brazil's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We fought together against a common foe. (6)
          - We have similar Social Policies. (3)
          - We have shared embassies. (1)
          - Brazil's real approach to Babylon is Friendly.
          - Religious differences strain your (Babylon) relationship. (-30)
          - We defeated Brazil's proposal in the United Nations. (-36)
        - TheirOpinionOfUs:
          - You (Brazil) have both chosen to adopt the Order Ideology.
          - You (Brazil) have denounced one of Babylon's declared enemies!
          - We fought together against a common foe.
          - Your (Brazil) votes supported Babylon's civ's interests in the United Nations.
          - Babylon liked our proposal to the United Nations.
          - We have made a public Declaration of Friendship!
          - Babylon's leader has expressed a public opinion of you (Brazil) (35).
          - We are trade partners.
          - We have similar Social Policies.
          - We have made Declarations of Friendship with the same leaders!
          - We passed Babylon's proposal in the United Nations.
          - Your (Brazil) recent diplomatic actions please Babylon.
          - We have made a Defensive Pact!
          - We have opened our borders to each other.
          - You (Brazil) have shared intrigue with Babylon.
          - We have shared embassies.
          - We have different religious beliefs.
          - Babylon desire friendly relations with Brazil.
        - Score: 2454
        - Era: Information
        - Technologies: 68
        - Cities: 14
        - Population: 324
        - Territory: 535
        - Gold: 158
        - GoldPerTurn: 178
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 45
        - MilitaryStrength: 4559
        - TourismPerTurn: 650.25
        - CulturePerTurn: 2433
        - PolicyBranches:
          - Tradition: 6
          - Artistry: 6
          - Statecraft: 1
          - Order: 6
          - Industry: 1
          - Progress: 6
        - ResourcesAvailable:
          - Wheat: 5
          - Sheep: 2
          - Ivory: 1
          - Paper: 8
          - Maize: 2
          - Rice: 2
          - Cotton: 6
          - Brazilwood: 1
          - Aluminum: 13
          - Bison: 2
          - Amber: 1
          - Deer: 13
          - Jade: 1
          - Dyes: 1
          - Iron: 6
          - Coal: 4
          - Fish: 18
          - Cattle: 4
          - Uranium: 5
          - Horses: 6
          - Copper: 1
          - Truffles: 1
          - Stone: 2
          - Marble: 1
          - Bananas: 1
          - Wine: 1
          - Cocoa: 1
        - FoundedReligion: Islam
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - Denounced Them
          - Polynesia:
            - Distance: Neighbors
            - War (Our Score: 16%; Our War Weariness: 33%)
            - Denounced Them
          - Russia:
            - Distance: Close
            - Denounced Them
          - Brazil:
            - Distance: Far
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Korea:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
        - Votes: 9
        
        ## Player 5
        - Civilization: Russia
        - Leader: Catherine
        - IsMajor: true
        - OurOpinionOfThem:
          - Brazil's leader has expressed a public opinion of Russia (70).
          - Brazil's leader has formed a private opinion of Russia (60).
          - We passed Brazil's proposal in the United Nations. (36)
          - You (Russia) have denounced one of Brazil's declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - You (Russia) have gone to war in the past.
          - Brazil's real approach to Russia is Guarded.
          - We have divergent Social Policies. (-3)
          - You (Russia) have denounced a leader Brazil made a Declaration of Friendship with! (-11)
          - You (Russia) have made a Declaration of Friendship with one of Brazil's enemies! (-13)
          - Religious differences strain your (Russia) relationship. (-30)
          - Your (Russia) spies were caught stealing from Brazil. (-33)
          - You (Russia) have chosen to adopt the Freedom Ideology, but Brazil believe in Order. (-999)
        - TheirOpinionOfUs:
          - You (Brazil) have denounced one of Russia's declared enemies!
          - Russia's leader has expressed a public opinion of you (Brazil) (60).
          - You (Brazil) have no contested borders.
          - Russia liked our proposal to the United Nations.
          - Your (Brazil) votes supported Russia's civ's interests in the United Nations.
          - We have Pledged to Protect the same City-States.
          - You (Brazil) have shared intrigue with Russia.
          - You (Brazil) have gone to war in the past.
          - Russia suspect we might be a threat to Russia.
          - Religious differences strain your (Brazil) relationship.
          - You (Brazil) are competing for World Wonders.
          - We have divergent Social Policies.
          - You (Brazil) have made a Defensive Pact with one of Russia's enemies!
          - Russia believe we are building World Wonders too aggressively!
          - You (Brazil) have made a Declaration of Friendship with one of Russia's enemies!
          - We have denounced each other!
          - You (Brazil) have denounced a leader Russia made a Declaration of Friendship with!
          - You (Brazil) have chosen to adopt the Order Ideology, but Russia believe in Freedom.
          - Your (Brazil) spies were caught stealing from Russia.
        - Score: 2012
        - Era: Atomic
        - Technologies: 59
        - Cities: 9
        - Population: 218
        - Territory: 317
        - Gold: 224
        - GoldPerTurn: 22
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 4763
        - TourismPerTurn: 493.75
        - CulturePerTurn: 1107
        - PolicyBranches:
          - Fealty: 2
          - Freedom: 4
          - Tradition: 6
          - Progress: 6
          - Industry: 2
          - Authority: 2
        - ResourcesAvailable:
          - Sheep: 1
          - Ivory: 1
          - Gold: 1
          - Paper: 2
          - Aluminum: 7
          - Maize: 1
          - Lapis Lazuli: 10
          - Coffee: 6
          - Deer: 10
          - Olives: 2
          - Tea: 1
          - Cattle: 1
          - Horses: 7
          - Fish: 7
          - Bison: 3
          - Citrus: 2
          - Stone: 3
          - Dyes: 1
          - Wine: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - War (Our Score: -8%; Our War Weariness: 4%)
            - Denounced Them
          - Babylon:
            - Distance: Close
            - Denounced Them
          - Polynesia:
            - Distance: Neighbors
            - Declaration of Friendship
          - Korea:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 0%)
          - Brazil:
            - Distance: Close
            - Peace Treaty
            - Denounced Them
        - Votes: 6
        
        ## Player 6
        - Civilization: Polynesia
        - Leader: Kamehameha
        - IsMajor: true
        - OurOpinionOfThem:
          - Brazil's leader has expressed a public opinion of Polynesia (50).
          - Brazil's leader has formed a private opinion of Polynesia (40).
          - We passed Brazil's proposal in the United Nations. (36)
          - Brazil have happily adopted your (Polynesia) religion in the majority of Brazil's cities. (30)
          - You (Polynesia) have denounced one of Brazil's declared enemies! (11)
          - Brazil's real approach to Polynesia is War.
          - We have divergent Social Policies. (-3)
          - You (Polynesia) killed or captured Brazil's civilians! (-9)
          - You (Polynesia) have denounced a leader Brazil made a Declaration of Friendship with! (-11)
          - You (Polynesia) have made a Declaration of Friendship with one of Brazil's enemies! (-13)
          - Your (Polynesia) spies were caught stealing from Brazil. (-33)
          - You (Polynesia) have chosen to adopt the Autocracy Ideology, but Brazil believe in Order. (-999)
          - You (Polynesia) are at war! (-99999)
        - TheirOpinionOfUs:
          - You (Brazil) have denounced one of Polynesia's declared enemies!
          - Polynesia liked our proposal to the United Nations.
          - You (Brazil) are not competing for the favor of the same City-States.
          - You (Brazil) have adopted Polynesia's religion in the majority of your (Brazil) cities.
          - Your (Brazil) votes supported Polynesia's civ's interests in the United Nations.
          - We have divergent Social Policies.
          - You (Brazil) have made a Defensive Pact with one of Polynesia's enemies!
          - You (Brazil) have made a Declaration of Friendship with one of Polynesia's enemies!
          - You (Brazil) excavated Polynesia's cultural artifacts!
          - Territorial disputes strain your (Brazil) relationship.
          - Polynesia's friends or allies have denounced you (Brazil)!
          - We have denounced Polynesia!
          - Polynesia believe we are building World Wonders too aggressively!
          - We placed sanctions on Polynesia in the United Nations.
          - You (Brazil) stole Polynesia's territory while at peace!
          - You (Brazil) have denounced a leader Polynesia made a Declaration of Friendship with!
          - We defeated Polynesia's proposal in the United Nations.
          - You (Brazil) have chosen to adopt the Order Ideology, but Polynesia believe in Autocracy.
          - Your (Brazil) spies were caught stealing from Polynesia.
          - You (Brazil) are at war!
        - Score: 1856
        - Era: Modern
        - GoldenAge: 1 turns remaining
        - Technologies: 55
        - Cities: 9
        - Population: 183
        - Territory: 348
        - Gold: 1057
        - GoldPerTurn: 79
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 37
        - MilitaryStrength: 2363
        - TourismPerTurn: 241.25
        - CulturePerTurn: 846
        - PolicyBranches:
          - Fealty: 1
          - Autocracy: 1
          - Tradition: 4
          - Rationalism: 1
          - Progress: 5
          - Imperialism: 1
          - Statecraft: 4
          - Authority: 4
        - ResourcesAvailable:
          - Wheat: 4
          - Sheep: 1
          - Paper: 6
          - Aluminum: 6
          - Coffee: 1
          - Jade: 4
          - Coal: 9
          - Cattle: 1
          - Horses: 3
          - Fish: 12
          - Copper: 2
          - Incense: 2
          - Crab: 2
          - Oil: -2
          - Bananas: 2
        - FoundedReligion: Buddhism
        - Relationships:
          - Austria:
            - Distance: Close
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
          - Babylon:
            - Distance: Neighbors
            - War (Our Score: -16%; Our War Weariness: 44%)
            - Denounced Them
          - Korea:
            - Distance: Neighbors
            - War (Our Score: 4%; Our War Weariness: 0%)
          - Russia:
            - Distance: Neighbors
            - Declaration of Friendship
          - Brazil:
            - Distance: Neighbors
            - War (Our Score: -54%; Our War Weariness: 68%)
        - Votes: 11
        - 7: Defeated Major Civilization Denmark
        
        ## Player 22
        - Civilization: Ban Chiang
        - Leader: City State
        - MajorAlly: Brazil
        - Population: 19
        - MajorityReligion: Buddhism
        - Relationships:
          - Austria: Friends (Influence: 499, Distance: Neighbors, Protected)
          - Babylon: Friends (Influence: 118, Distance: Distant)
          - Polynesia: War (Influence: -60, Distance: Close)
          - Korea: Neutral (Influence: -12, Distance: Close)
          - Russia: Neutral (Influence: 19, Distance: Far, Protected)
          - Brazil: Ally (Influence: 447, Distance: Neighbors, Protected)
        - Quests:
          - They want you to build The Motherland Calls. (Turns remaining: 38) Potential Quest Reward: * 199 Influence * 400 Faith
        
        ## Player 23
        - Civilization: La Venta
        - Leader: City State
        - MajorAlly: Brazil
        - Population: 18
        - MajorityReligion: Buddhism
        - Relationships:
          - Austria: Friends (Influence: 755, Distance: Far, Protected)
          - Babylon: Neutral (Influence: 29, Distance: Close)
          - Polynesia: War (Influence: -60, Distance: Neighbors)
          - Korea: Neutral (Influence: 22, Distance: Close)
          - Russia: Neutral (Influence: 0, Distance: Close)
          - Brazil: Ally (Influence: 285, Distance: Neighbors, Protected)
        - Quests:
          - Diplomatic Missions are temporarily more effective. (Turns remaining: 9) They want you to demand tribute from Cahokia. Potential Quest Reward: * 106 Influence * 302 Gold
        
        ## Player 24
        - Civilization: Ecbatana
        - Leader: City State
        - Population: 9
        - ResourcesAvailable:
          - Gems: 1
          - Deer: 1
          - Sheep: 1
        - MajorityReligion: Buddhism
        - Relationships:
          - Austria: Friends (Influence: 562, Distance: Close, Protected)
          - Babylon: Friends (Influence: 36, Distance: Distant)
          - Polynesia: Friends (Influence: 95, Distance: Neighbors, Protected)
          - Korea: Friends (Influence: 121, Distance: Close)
          - Russia: Friends (Influence: 59, Distance: Distant)
          - Brazil: Friends (Influence: 59, Distance: Far)
        - Quests:
          - Conduct a Spy Mission against Maria Theresa. Potential Quest Reward: * 339 Influence * 811 Science
          - They want you to demand tribute from Brussels. Potential Quest Reward: * 114 Influence * 324 Gold
        
        ## Player 25
        - Civilization: Oviedo
        - Leader: City State
        - MajorAlly: Babylon
        - Population: 20
        - ResourcesAvailable:
          - Fish: 3
        - MajorityReligion: Catholicism
        - Relationships:
          - Austria: Friends (Influence: 481, Distance: Neighbors, Protected)
          - Babylon: Ally (Influence: 146, Distance: Neighbors, Protected)
          - Polynesia: War (Influence: -60, Distance: Far)
          - Korea: Neutral (Influence: 25, Distance: Distant)
          - Russia: Friends (Influence: 162, Distance: Distant)
          - Brazil: Friends (Influence: 53, Distance: Distant)
        - Quests:
          - They will reward the player with the highest Tourism per turn. So far, the leader has 1,942 per turn and you have 951 per turn. (Turns remaining: 7) Potential Quest Reward: * 265 Influence * 792 Culture
          - They want you to start a land or sea trade route to their city. (Turns remaining: 11) Potential Quest Reward: * 163 Influence * 268 Food in Capital
          - They want you to demand tribute from Bunkeya. Potential Quest Reward: * 105 Influence * 315 Gold
        
        ## Player 26
        - Civilization: Huari
        - Leader: City State
        - MajorAlly: Austria
        - Population: 37
        - ResourcesAvailable:
          - Fish: 2
          - Sheep: 1
        - MajorityReligion: Islam
        - Relationships:
          - Austria: Ally (Influence: 1606, Distance: Neighbors, Protected)
          - Babylon: Neutral (Influence: 20, Distance: Neighbors, Protected)
          - Polynesia: War (Influence: -60, Distance: Distant)
          - Korea: Neutral (Influence: 9, Distance: Distant)
          - Russia: War (Influence: -60, Distance: Distant)
          - Brazil: Friends (Influence: 30, Distance: Distant)
        - Quests:
          - They want you to defeat Barbarian units that are invading their territory. You are allowed to enter their territory until the Barbarians are defeated.
        
        ## Player 27
        - Civilization: Palatium
        - Leader: City State
        - MajorAlly: Austria
        - Population: 16
        - ResourcesAvailable:
          - Cattle: 1
          - Deer: 1
          - Fish: 2
        - Relationships:
          - Austria: Ally (Influence: 915, Distance: Close, Protected)
          - Babylon: Neutral (Influence: 20, Distance: Close, Protected)
          - Polynesia: War (Influence: -60, Distance: Neighbors)
          - Korea: Friends (Influence: 32, Distance: Distant)
          - Russia: War (Influence: -60, Distance: Neighbors)
          - Brazil: Friends (Influence: 183, Distance: Far)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 28
        - Civilization: Cahokia
        - Leader: City State
        - Population: 23
        - ResourcesAvailable:
          - Fish: 3
          - Porcelain: 1
          - Tea: 1
          - Bananas: 1
        - Relationships:
          - Austria: Friends (Influence: 1073, Distance: Close, Protected)
          - Babylon: Friends (Influence: 36, Distance: Neighbors, Protected)
          - Polynesia: Friends (Influence: 33, Distance: Neighbors, Protected)
          - Korea: Friends (Influence: 53, Distance: Distant)
          - Russia: Neutral (Influence: -2, Distance: Close)
          - Brazil: Friends (Influence: 59, Distance: Far)
        - Quests:
          - Construct 3 Medical Lab buildings in non-puppet cities in your empire. (Turns remaining: 29) Potential Quest Reward: * 216 Influence * 399 Production in Capital
        - 29: Defeated Minor Civilization Quebec City
        
        ## Player 30
        - Civilization: Brussels
        - Leader: City State
        - MajorAlly: Austria
        - Population: 19
        - ResourcesAvailable:
          - Deer: 2
          - Fish: 2
        - MajorityReligion: Buddhism
        - Relationships:
          - Austria: Ally (Influence: 879, Distance: Close, Protected)
          - Babylon: Neutral (Influence: -48, Distance: Far)
          - Polynesia: War (Influence: -60, Distance: Neighbors)
          - Korea: Neutral (Influence: -8, Distance: Close)
          - Russia: War (Influence: -60, Distance: Distant)
          - Brazil: Neutral (Influence: -23, Distance: Far)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 31
        - Civilization: Assur
        - Leader: City State
        - MajorAlly: Austria
        - Population: 16
        - ResourcesAvailable:
          - Deer: 1
          - Fish: 1
        - MajorityReligion: Islam
        - Relationships:
          - Austria: Ally (Influence: 1281, Distance: Neighbors, Protected)
          - Babylon: Friends (Influence: 143, Distance: Neighbors, Protected)
          - Polynesia: War (Influence: -60, Distance: Far)
          - Korea: Friends (Influence: 35, Distance: Distant)
          - Russia: War (Influence: -60, Distance: Far)
          - Brazil: Friends (Influence: 59, Distance: Distant)
        - Quests:
          - Construct 4 Airport buildings in non-puppet cities in your empire. (Turns remaining: 42) Potential Quest Reward: * 234 Influence * 521 Production in Capital
          - Acquire the city of Kaupang. (Turns remaining: 28) Potential Quest Reward: * 420 Influence * 1 Juggernaut Unit(150 Bonus XP)
        
        ## Player 32
        - Civilization: Bunkeya
        - Leader: City State
        - Population: 20
        - ResourcesAvailable:
          - Fish: 2
          - Horses: 2
          - Gems: 1
          - Coal: 2
          - Sheep: 1
        - MajorityReligion: Catholicism
        - Relationships:
          - Austria: Friends (Influence: 511, Distance: Neighbors, Protected)
          - Babylon: Friends (Influence: 166, Distance: Close, Protected)
          - Polynesia: Friends (Influence: 70, Distance: Close)
          - Korea: Friends (Influence: 35, Distance: Distant)
          - Russia: Friends (Influence: 59, Distance: Close, Protected)
          - Brazil: Friends (Influence: 194, Distance: Distant)
        - Quests:
          - Acquire the city of Ribe. (Turns remaining: 27) Potential Quest Reward: * 420 Influence * 1 Juggernaut Unit(150 Bonus XP)
        
        ## Player 33
        - Civilization: Milan
        - Leader: City State
        - MajorAlly: Austria
        - Population: 24
        - ResourcesAvailable:
          - Deer: 1
          - Fish: 5
        - MajorityReligion: Buddhism
        - Relationships:
          - Austria: Ally (Influence: 1300, Distance: Neighbors, Protected)
          - Babylon: Friends (Influence: 36, Distance: Distant, Protected)
          - Polynesia: War (Influence: -60, Distance: Close)
          - Korea: Friends (Influence: 225, Distance: Close)
          - Russia: War (Influence: -60, Distance: Distant)
          - Brazil: Friends (Influence: 59, Distance: Far)
        - Quests:
          - They want you to generate a Great Merchant. (Turns remaining: 41) Potential Quest Reward: * 160 Influence * 444 Culture
          - They want you to build the Foreign Bureau. (Turns remaining: 28) Potential Quest Reward: * 160 Influence * 987 Golden Age Points
        
        ## Player 34
        - Civilization: Zuunmod
        - Leader: City State
        - MajorAlly: Austria
        - Population: 19
        - ResourcesAvailable:
          - Cattle: 2
          - Fish: 3
        - MajorityReligion: Catholicism
        - Relationships:
          - Austria: Ally (Influence: 1814, Distance: Close, Protected)
          - Babylon: Neutral (Influence: -60, Distance: Neighbors)
          - Polynesia: War (Influence: -60, Distance: Far)
          - Korea: Neutral (Influence: -59, Distance: Distant)
          - Russia: War (Influence: -60, Distance: Distant)
          - Brazil: Neutral (Influence: -59, Distance: Distant)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 35
        - Civilization: Yamatai
        - Leader: City State
        - MajorAlly: Austria
        - Population: 13
        - ResourcesAvailable:
          - Deer: 2
        - MajorityReligion: Catholicism
        - Relationships:
          - Austria: Ally (Influence: 913, Distance: Neighbors, Protected)
          - Babylon: Neutral (Influence: 6, Distance: Far, Protected)
          - Polynesia: War (Influence: -60, Distance: Far)
          - Korea: Neutral (Influence: 16, Distance: Distant)
          - Russia: War (Influence: -60, Distance: Distant)
          - Brazil: Friends (Influence: 30, Distance: Distant)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 36
        - Civilization: Helsinki
        - Leader: City State
        - MajorAlly: Polynesia
        - Population: 10
        - ResourcesAvailable:
          - Deer: 1
        - MajorityReligion: Buddhism
        - Relationships:
          - Austria: War - Peace Currently Blocked (Influence: -60, Distance: Neighbors)
          - Babylon: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Polynesia: Ally (Influence: 515, Distance: Neighbors, Protected)
          - Korea: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Russia: Neutral (Influence: -55, Distance: Distant)
          - Brazil: War - Peace Currently Blocked (Influence: -60, Distance: Close)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 37
        - Civilization: Longcheng
        - Leader: City State
        - MajorAlly: Austria
        - Population: 6
        - ResourcesAvailable:
          - Sheep: 2
        - MajorityReligion: Buddhism
        - Relationships:
          - Austria: Ally (Influence: 582, Distance: Distant, Protected)
          - Babylon: Friends (Influence: 258, Distance: Neighbors, Protected)
          - Polynesia: War (Influence: -60, Distance: Close)
          - Korea: Neutral (Influence: 14, Distance: Distant)
          - Russia: War (Influence: -60, Distance: Distant)
          - Brazil: Neutral (Influence: 23, Distance: Distant)
        - Quests:
          - They want you to defeat Barbarian units that are invading their territory. You are allowed to enter their territory until the Barbarians are defeated.
        - 63: Barbarians
        
        # Cities
        Cities: summary reports about discovered cities in the world.
        
        ## Player: Austria
        
        ### Vienna
        - ID: 1057
        - X: 1
        - Y: 43
        - Population: 48
        - MajorityReligion: Catholicism
        - DefenseStrength: 120
        - IsCoastal: true
        - Wonders:
          - Circus Maximus
          - Chartered Company
          - Royal Collection
          - Hagia Sophia
          - Himeji Castle
          - Sistine Chapel
          - Brandenburg Gate
          - Broadway
          - Borobudur
          - International Finance Center
          - Karlstejn
          - Grand Canal
          - Crystal Palace
          - Menin Gate
          - United Nations
          - Consulate
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
          - Celestial Throne
          - Civilized Jewelers Headquarters
        
        ### Salzburg
        - ID: 1182
        - X: 6
        - Y: 42
        - Population: 28
        - MajorityReligion: Catholicism
        - DefenseStrength: 83
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Ironworks
          - Grand Temple
        
        ### Graz
        - ID: 1593
        - X: 8
        - Y: 37
        - Population: 27
        - MajorityReligion: Catholicism
        - DefenseStrength: 115
        - Wonders:
          - Imperial College
          - Machu Picchu
        
        ### Linz
        - ID: 1838
        - X: 4
        - Y: 36
        - Population: 28
        - MajorityReligion: Catholicism
        - DefenseStrength: 86
        - IsCoastal: true
        - Wonders:
          - Foreign Bureau
          - Summer Palace
        
        ### Klagenfurt
        - ID: 2284
        - X: 1
        - Y: 48
        - Population: 23
        - MajorityReligion: Catholicism
        - DefenseStrength: 112
        - IsCoastal: true
        - Wonders:
          - Statue of Liberty
          - Scrivener's Office
          - Ballhausplatz
          - Nalanda
        
        ### Bregenz
        - ID: 5044
        - X: 23
        - Y: 13
        - Population: 25
        - MajorityReligion: Catholicism
        - DefenseStrength: 124
        - IsCoastal: true
        
        ### Boston
        - ID: 5151
        - X: 7
        - Y: 33
        - Population: 26
        - MajorityReligion: Catholicism
        - DefenseStrength: 115
        - IsOccupied: true
        
        ### Kitzbuhel
        - ID: 5889
        - X: 28
        - Y: 13
        - Population: 21
        - MajorityReligion: Catholicism
        - DefenseStrength: 110
        - IsCoastal: true
        
        ### St. Polten
        - ID: 6394
        - X: 23
        - Y: 5
        - Population: 19
        - MajorityReligion: Catholicism
        - DefenseStrength: 119
        - IsCoastal: true
        
        ### Innsbruck
        - ID: 7036
        - X: 26
        - Y: 9
        - Population: 18
        - MajorityReligion: Catholicism
        - DefenseStrength: 114
        - IsCoastal: true
        
        ### Eisenstadt
        - ID: 7339
        - X: 78
        - Y: 27
        - Population: 22
        - DefenseStrength: 108
        - IsCoastal: true
        
        ### Villach
        - ID: 7515
        - X: 77
        - Y: 36
        - Population: 20
        - MajorityReligion: Buddhism
        - DefenseStrength: 117
        - IsCoastal: true
        
        ### Zwettl
        - ID: 9074
        - X: 13
        - Y: 14
        - Population: 20
        - DefenseStrength: 99
        - IsCoastal: true
        
        ### Washington
        - ID: 10970
        - X: 12
        - Y: 42
        - Population: 25
        - DefenseStrength: 110
        - IsOccupied: true
        - Wonders:
          - Alhambra
          - Terracotta Army
        
        ### New York
        - ID: 10975
        - X: 13
        - Y: 37
        - Population: 23
        - DefenseStrength: 107
        - IsOccupied: true
        
        ### Chicago
        - ID: 11059
        - X: 7
        - Y: 24
        - Population: 20
        - DefenseStrength: 109
        - IsOccupied: true
        - IsCoastal: true
        
        ### Philadelphia
        - ID: 11313
        - X: 5
        - Y: 29
        - Population: 23
        - DefenseStrength: 113
        - IsOccupied: true
        - IsCoastal: true
        
        ### Quebec City
        - ID: 11427
        - X: 10
        - Y: 29
        - Population: 22
        - MajorityReligion: Catholicism
        - DefenseStrength: 122
        - IsOccupied: true
        - IsCoastal: true
        
        ### Vladivostok
        - ID: 12755
        - X: 35
        - Y: 4
        - Population: 15
        - DefenseStrength: 77
        - IsOccupied: true
        - IsCoastal: true
        
        ### Smolensk
        - ID: 12851
        - X: 34
        - Y: 8
        - Population: 17
        - DefenseStrength: 81
        - IsOccupied: true
        - IsCoastal: true
        
        ### Kaesong
        - ID: 14208
        - X: 75
        - Y: 32
        - Population: 19
        - MajorityReligion: Buddhism
        - DefenseStrength: 109
        - IsOccupied: true
        - IsCoastal: true
        
        ### Pyongyang
        - ID: 14905
        - X: 69
        - Y: 38
        - Population: 17
        - MajorityReligion: Buddhism
        - DefenseStrength: 90
        - IsOccupied: true
        - IsCoastal: true
        
        ### Jeonju
        - ID: 15208
        - X: 66
        - Y: 30
        - Population: 20
        - MajorityReligion: Buddhism
        - DefenseStrength: 79
        - IsOccupied: true
        - IsCoastal: true
        
        ### Seoul
        - ID: 15654
        - X: 66
        - Y: 35
        - Population: 24
        - MajorityReligion: Buddhism
        - DefenseStrength: 77
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Angkor Wat
        
        ## Player: Brazil
        
        ### Rio de Janeiro
        - ID: 1082
        - X: 60
        - Y: 23
        - Population: 27
        - MajorityReligion: Buddhism
        - DefenseStrength: 79
        - IsCoastal: true
        - FoodStored: 1315
        - FoodPerTurn: 1
        - ProductionStored: 226
        - ProductionPerTurn: 226
        - CurrentProduction: Triplane
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 330
        - SciencePerTurn: 382
        - CulturePerTurn: 372
        - FaithPerTurn: 54
        - TourismPerTurn: 221.39
        - HappinessDelta: 20
        - BuildingCount: 47
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Harbor
          - Stadium
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Arsenal
          - Medical Lab
          - Factory
          - Stock Exchange
          - Constabulary
          - Writers' Guild
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Bath
          - Wire Service
          - Embrapa
        - Wonders:
          - National Monument
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Imperial College
          - Pyramids
          - Oracle
          - Forbidden Palace
          - Taj Mahal
          - Statue of Zeus
          - Temple of Artemis
          - Mausoleum of Halicarnassus
          - Grand Temple
          - Scrivener's Office
          - Printing Press
          - Consulate
        - GreatWorkCount: 14
        
        ### Sao Paulo
        - ID: 1406
        - X: 64
        - Y: 22
        - Population: 28
        - MajorityReligion: Buddhism
        - DefenseStrength: 74
        - IsCoastal: true
        - FoodStored: 1458
        - FoodPerTurn: 11
        - ProductionStored: 623
        - ProductionPerTurn: 315
        - CurrentProduction: Police Station
        - ProductionTurnsLeft: 3
        - GoldPerTurn: 213
        - SciencePerTurn: 390
        - CulturePerTurn: 425
        - FaithPerTurn: 40
        - TourismPerTurn: 335.8
        - HappinessDelta: 20
        - BuildingCount: 46
        - ImportantBuildings:
          - Seaport
          - Stable
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Arsenal
          - Hospital
          - Factory
          - Stock Exchange
          - Strategic Defense System
          - Constabulary
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Chancery
          - Coaling Station
          - Embrapa
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - Royal Collection
          - Great Library
          - Cristo Redentor
          - Uffizi
          - Palace of Culture and Science
          - Soho Foundry
          - Empire State Building
          - Hexxon Refineries Headquarters
        - GreatWorkCount: 18
        
        ### Salvador
        - ID: 2468
        - X: 69
        - Y: 22
        - Population: 25
        - MajorityReligion: Buddhism
        - DefenseStrength: 69
        - IsCoastal: true
        - FoodStored: 1386
        - FoodPerTurn: 5
        - ProductionStored: 483
        - ProductionPerTurn: 273
        - CurrentProduction: Triplane
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 178
        - SciencePerTurn: 231
        - CulturePerTurn: 179
        - FaithPerTurn: 23
        - TourismPerTurn: 162.32
        - HappinessDelta: 12
        - BuildingCount: 49
        - ImportantBuildings:
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Harbor
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Arsenal
          - Hospital
          - Factory
          - Stock Exchange
          - Constabulary
          - Writers' Guild
          - Artists' Guild
          - Hotel
          - Caravansary
          - Chancery
          - Agribusiness
          - Coaling Station
          - Embrapa
        - Wonders:
          - Porcelain Tower
        - GreatWorkCount: 7
        
        ### Brasilia
        - ID: 2488
        - X: 63
        - Y: 28
        - Population: 26
        - MajorityReligion: Buddhism
        - DefenseStrength: 75
        - FoodStored: 801
        - FoodPerTurn: 39
        - ProductionStored: 241
        - ProductionPerTurn: 241
        - CurrentProduction: Strategic Defense System
        - ProductionTurnsLeft: 6
        - GoldPerTurn: 169
        - SciencePerTurn: 339
        - CulturePerTurn: 207
        - FaithPerTurn: 23
        - TourismPerTurn: 162.96
        - HappinessDelta: 12
        - BuildingCount: 50
        - ImportantBuildings:
          - Stable
          - Windmill
          - Customs House
          - Observatory
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
          - Police Station
          - Writers' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Coaling Station
          - Wire Service
          - Embrapa
        - GreatWorkCount: 6
        
        ### Viborg
        - ID: 12624
        - X: 54
        - Y: 23
        - Population: 24
        - MajorityReligion: Buddhism
        - DefenseStrength: 75
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 930
        - FoodPerTurn: 81
        - ProductionStored: 326
        - ProductionPerTurn: 218
        - CurrentProduction: Zoo
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 177
        - SciencePerTurn: 148
        - CulturePerTurn: 94
        - FaithPerTurn: 23
        - TourismPerTurn: 38.24
        - HappinessDelta: 3
        - BuildingCount: 36
        - ImportantBuildings:
          - Courthouse
          - Water Mill
          - Circus
          - Customs House
          - Harbor
          - Temple
          - Barracks
          - Military Academy
          - Arsenal
          - Medical Lab
          - Factory
          - University
          - Amphitheater
          - Constabulary
          - Caravansary
          - Bath
          - Chancery
          - Embrapa
        - Wonders:
          - Colossus
        - GreatWorkCount: 2
        
        ### Aotearoa
        - ID: 14687
        - X: 53
        - Y: 27
        - Population: 21
        - MajorityReligion: Buddhism
        - DefenseStrength: 75
        - IsOccupied: true
        - FoodStored: 677
        - FoodPerTurn: 130
        - ProductionStored: 438
        - ProductionPerTurn: 195
        - CurrentProduction: Public School
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 139
        - SciencePerTurn: 88
        - CulturePerTurn: 72
        - FaithPerTurn: 30
        - TourismPerTurn: 31
        - HappinessDelta: 9
        - BuildingCount: 40
        - ImportantBuildings:
          - Courthouse
          - Circus
          - Customs House
          - Garden
          - Temple
          - Opera House
          - Armory
          - Arsenal
          - Hospital
          - Factory
          - Bank
          - University
          - Constabulary
          - Caravansary
          - Bath
          - Chancery
          - Gallery
        - GreatWorkCount: 2
        
        ## Player: Korea
        
        ### Busan
        - ID: 1337
        - X: 61
        - Y: 35
        - Population: 22
        - MajorityReligion: Buddhism
        - DefenseStrength: 63
        - Wonders:
          - Chartered Company
          - Scrivener's Office
          - Printing Press
          - Royal Guardhouse
          - Court Chapel
          - Royal Astrologer
        
        ### Daegu
        - ID: 2317
        - X: 59
        - Y: 30
        - Population: 20
        - MajorityReligion: Buddhism
        - DefenseStrength: 52
        - Wonders:
          - Heroic Epic
        
        ## Player: Babylon
        
        ### Babylon
        - ID: 1060
        - X: 16
        - Y: 32
        - Population: 42
        - MajorityReligion: Islam
        - DefenseStrength: 78
        - Wonders:
          - School of Philosophy
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Imperial College
          - Royal Collection
          - Chichen Itza
          - University of Sankore
          - Globe Theatre
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
          - Palace of Culture and Science
          - Etemenanki
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
          - Grand Ossuary
          - Giorgio Armeier Headquarters
        
        ### Akkad
        - ID: 1324
        - X: 18
        - Y: 37
        - Population: 27
        - DefenseStrength: 70
        - IsCoastal: true
        
        ### Dur-Kurigalzu
        - ID: 1507
        - X: 17
        - Y: 28
        - Population: 25
        - DefenseStrength: 74
        - IsCoastal: true
        
        ### Nippur
        - ID: 1843
        - X: 21
        - Y: 30
        - Population: 24
        - DefenseStrength: 74
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - Kremlin
          - Grand Temple
        
        ### Borsippa
        - ID: 2341
        - X: 14
        - Y: 25
        - Population: 25
        - DefenseStrength: 76
        - IsCoastal: true
        
        ### Sippar
        - ID: 3249
        - X: 18
        - Y: 42
        - Population: 22
        - DefenseStrength: 77
        - IsCoastal: true
        - Wonders:
          - Louvre
        
        ### Opis
        - ID: 4123
        - X: 18
        - Y: 17
        - Population: 22
        - DefenseStrength: 76
        - IsCoastal: true
        
        ### Mari
        - ID: 5382
        - X: 21
        - Y: 9
        - Population: 23
        - DefenseStrength: 74
        - IsCoastal: true
        
        ### Shushan
        - ID: 6114
        - X: 18
        - Y: 5
        - Population: 22
        - DefenseStrength: 74
        - IsCoastal: true
        
        ### Eshnunna
        - ID: 6986
        - X: 31
        - Y: 41
        - Population: 22
        - MajorityReligion: Buddhism
        - DefenseStrength: 74
        - IsCoastal: true
        
        ### Ellasar
        - ID: 7496
        - X: 36
        - Y: 42
        - Population: 19
        - MajorityReligion: Buddhism
        - DefenseStrength: 78
        - IsCoastal: true
        
        ### Erech
        - ID: 8119
        - X: 39
        - Y: 45
        - Population: 20
        - MajorityReligion: Buddhism
        - DefenseStrength: 74
        - IsCoastal: true
        
        ### Kutha
        - ID: 8595
        - X: 11
        - Y: 5
        - Population: 19
        - DefenseStrength: 72
        - IsCoastal: true
        
        ### Roskilde
        - ID: 15421
        - X: 35
        - Y: 27
        - Population: 12
        - MajorityReligion: Buddhism
        - DefenseStrength: 53
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: Russia
        
        ### Moscow
        - ID: 1061
        - X: 50
        - Y: 7
        - Population: 32
        - MajorityReligion: Hinduism
        - DefenseStrength: 75
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - National Monument
          - Hanging Gardens
          - Great Wall
          - Foreign Bureau
          - Olympic Village
          - Consulate
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
          - TwoKay Foods Headquarters
        
        ### St. Petersburg
        - ID: 1218
        - X: 49
        - Y: 12
        - Population: 26
        - MajorityReligion: Hinduism
        - DefenseStrength: 81
        - IsCoastal: true
        - Wonders:
          - Scrivener's Office
          - Printing Press
        
        ### Novgorod
        - ID: 1467
        - X: 45
        - Y: 9
        - Population: 23
        - MajorityReligion: Hinduism
        - DefenseStrength: 78
        - Wonders:
          - School of Philosophy
          - Ironworks
          - Royal Collection
          - Neuschwanstein
        
        ### Rostov
        - ID: 1807
        - X: 53
        - Y: 4
        - Population: 23
        - MajorityReligion: Hinduism
        - DefenseStrength: 77
        - IsCoastal: true
        
        ### Yaroslavl'
        - ID: 2606
        - X: 54
        - Y: 10
        - Population: 25
        - MajorityReligion: Hinduism
        - DefenseStrength: 76
        - IsCoastal: true
        - Wonders:
          - Circus Maximus
        
        ### Yekaterinburg
        - ID: 3420
        - X: 45
        - Y: 4
        - Population: 25
        - MajorityReligion: Hinduism
        - DefenseStrength: 49
        - Wonders:
          - Chartered Company
          - Imperial College
          - Eiffel Tower
          - Grand Temple
          - International Finance Center
        
        ### Yakutsk
        - ID: 3948
        - X: 46
        - Y: 14
        - Population: 22
        - MajorityReligion: Hinduism
        - DefenseStrength: 77
        - IsCoastal: true
        
        ### Copenhagen
        - ID: 8656
        - X: 43
        - Y: 16
        - Population: 24
        - MajorityReligion: Hinduism
        - DefenseStrength: 74
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Petra
          - Roman Forum
        
        ### Palatium
        - ID: 13293
        - X: 40
        - Y: 5
        - Population: 18
        - MajorityReligion: Hinduism
        - DefenseStrength: 78
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: Polynesia
        
        ### Honolulu
        - ID: 1062
        - X: 54
        - Y: 33
        - Population: 23
        - MajorityReligion: Buddhism
        - DefenseStrength: 50
        - Health: 12%
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - National Monument
          - Chartered Company
          - Great Lighthouse
          - Stonehenge
          - Leaning Tower of Pisa
          - Scrivener's Office
          - Printing Press
          - Royal Guardhouse
          - Court Chapel
          - Royal Astrologer
          - Holy Council
        
        ### Samoa
        - ID: 1301
        - X: 59
        - Y: 38
        - Population: 23
        - MajorityReligion: Buddhism
        - DefenseStrength: 71
        - IsCoastal: true
        
        ### Tonga
        - ID: 1921
        - X: 61
        - Y: 41
        - Population: 23
        - MajorityReligion: Buddhism
        - DefenseStrength: 62
        - IsCoastal: true
        - Wonders:
          - Ironworks
          - Imperial College
          - Grand Temple
        
        ### Nuku Hiva
        - ID: 2536
        - X: 51
        - Y: 36
        - Population: 22
        - MajorityReligion: Buddhism
        - DefenseStrength: 75
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - Circus Maximus
          - Notre Dame
          - Firaxite Materials Headquarters
        
        ### Raiatea
        - ID: 2953
        - X: 63
        - Y: 46
        - Population: 21
        - MajorityReligion: Buddhism
        - DefenseStrength: 59
        - IsCoastal: true
        
        ### Tahiti
        - ID: 7878
        - X: 45
        - Y: 48
        - Population: 18
        - MajorityReligion: Buddhism
        - DefenseStrength: 71
        - IsCoastal: true
        
        ### Ribe
        - ID: 8307
        - X: 48
        - Y: 23
        - Population: 19
        - MajorityReligion: Buddhism
        - DefenseStrength: 73
        - IsOccupied: true
        - IsCoastal: true
        
        ### Kaupang
        - ID: 8722
        - X: 43
        - Y: 21
        - Population: 18
        - MajorityReligion: Buddhism
        - DefenseStrength: 73
        - IsOccupied: true
        - IsCoastal: true
        
        ### Tunsberg
        - ID: 9346
        - X: 38
        - Y: 19
        - Population: 16
        - MajorityReligion: Buddhism
        - DefenseStrength: 67
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: City-States
        
        ### Ban Chiang
        - ID: 3823
        - X: 68
        - Y: 26
        - Population: 19
        - MajorityReligion: Buddhism
        - DefenseStrength: 95
        - IsCoastal: true
        
        ### La Venta
        - ID: 1065
        - X: 49
        - Y: 29
        - Population: 18
        - MajorityReligion: Buddhism
        - DefenseStrength: 80
        - IsCoastal: true
        
        ### Ecbatana
        - ID: 1066
        - X: 67
        - Y: 47
        - Population: 9
        - MajorityReligion: Buddhism
        - DefenseStrength: 68
        - IsCoastal: true
        
        ### Oviedo
        - ID: 1067
        - X: 16
        - Y: 20
        - Population: 20
        - MajorityReligion: Catholicism
        - DefenseStrength: 95
        - IsCoastal: true
        
        ### Huari
        - ID: 1068
        - X: 17
        - Y: 46
        - Population: 24
        - MajorityReligion: Islam
        - DefenseStrength: 95
        - IsCoastal: true
        
        ### Atlanta
        - ID: 4026
        - X: 14
        - Y: 48
        - Population: 13
        - DefenseStrength: 59
        - IsOccupied: true
        - IsCoastal: true
        
        ### Aarhus
        - ID: 8017
        - X: 40
        - Y: 12
        - Population: 16
        - DefenseStrength: 78
        - IsOccupied: true
        - IsCoastal: true
        
        ### Cahokia
        - ID: 1070
        - X: 37
        - Y: 23
        - Population: 23
        - DefenseStrength: 84
        - IsCoastal: true
        
        ### Brussels
        - ID: 1072
        - X: 57
        - Y: 46
        - Population: 19
        - MajorityReligion: Buddhism
        - DefenseStrength: 90
        - IsCoastal: true
        
        ### Assur
        - ID: 1073
        - X: 23
        - Y: 18
        - Population: 16
        - MajorityReligion: Islam
        - DefenseStrength: 94
        - IsCoastal: true
        
        ### Bunkeya
        - ID: 1074
        - X: 29
        - Y: 17
        - Population: 20
        - MajorityReligion: Catholicism
        - DefenseStrength: 68
        - IsCoastal: true
        
        ### Milan
        - ID: 1075
        - X: 73
        - Y: 41
        - Population: 24
        - MajorityReligion: Buddhism
        - DefenseStrength: 95
        - IsCoastal: true
        
        ### Zuunmod
        - ID: 1076
        - X: 21
        - Y: 24
        - Population: 19
        - MajorityReligion: Catholicism
        - DefenseStrength: 90
        - IsCoastal: true
        
        ### Yamatai
        - ID: 1077
        - X: 5
        - Y: 49
        - Population: 13
        - MajorityReligion: Catholicism
        - DefenseStrength: 94
        
        ### Helsinki
        - ID: 1078
        - X: 67
        - Y: 42
        - Population: 10
        - MajorityReligion: Buddhism
        - DefenseStrength: 91
        - Health: 89%
        
        ### Longcheng
        - ID: 1079
        - X: 34
        - Y: 47
        - Population: 6
        - MajorityReligion: Buddhism
        - DefenseStrength: 79
        
        # Military
        Military: summary reports about tactical zones and visible units.
        
        ## Unit Stats
        - CityBombard:
          - Artillery:
            - Strength: 27
            - RangedStrength: 50
          - Field Gun:
            - Strength: 17
            - RangedStrength: 40
        - FastAttack:
          - Tank:
            - Strength: 75
          - T-34:
            - Strength: 82
          - Lancer:
            - Strength: 37
          - Landship:
            - Strength: 60
        - Defense:
          - Infantry:
            - Strength: 62
          - Rifleman:
            - Strength: 50
          - Pracinha:
            - Strength: 62
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
          - Ironclad:
            - Strength: 55
          - Fleet Destroyer:
            - Strength: 80
        - AssaultSea:
          - Cruiser:
            - Strength: 40
            - RangedStrength: 55
        - AttackAir:
          - B17:
            - RangedStrength: 70
          - Bomber:
            - RangedStrength: 50
        - DefenseAir:
          - Triplane:
            - RangedStrength: 45
        - Paradrop:
          - Paratrooper:
            - Strength: 42
        
        ## Enemy Land Zone 1062
        - ZoneValue: 23040
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 1146
        - NeutralStrength: 493
        - FriendlyStrength: 3190
        - City: Honolulu
        - AreaID: 49
        - Plots: 19
        - CenterX: 54
        - CenterY: 32
        - Units:
          - Brazil:
            - Paratrooper: 2
            - Artillery: 2
            - Infantry: 2
            - Machine Gun: 2
        - Neighbors:
          - 1065
          - 2536
          - 14687
          - -1062
          - -2536
          - 2317
        
        ## Neutral Land Zone 1065
        - ZoneValue: 18
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 774
        - NeutralStrength: 141
        - FriendlyStrength: 2883
        - City: La Venta
        - AreaID: 49
        - Plots: 27
        - CenterX: 49
        - CenterY: 29
        - Units:
          - Brazil:
            - T-34: 1
            - Anti-Aircraft Gun: 3
            - Infantry: 1
            - Machine Gun: 1
            - Field Gun: 2
          - City-State La Venta:
            - Artillery: 1
            - Infantry: 1
        - Neighbors:
          - -1065
          - -8307
          - 8307
          - 2536
          - 14687
          - 1062
        
        ## Friendly Land Zone 1082
        - ZoneValue: 36
        - Dominance: Friendly
        - NeutralStrength: 256
        - FriendlyStrength: 1444
        - City: Rio de Janeiro
        - AreaID: 33
        - Plots: 27
        - CenterX: 59
        - CenterY: 23
        - Units:
          - Brazil:
            - Triplane: 1
            - Bomber: 1
            - Machine Gun: 1
        - Neighbors:
          - 12624
          - -12624
          - -1082
          - 2317
          - -1406
          - 2488
          - 1406
        
        ## Neutral Land Zone 1337
        - ZoneValue: 15
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 662
        - NeutralStrength: 910
        - FriendlyStrength: 672
        - City: Busan
        - AreaID: 49
        - Plots: 23
        - CenterX: 61
        - CenterY: 35
        - Units:
          - Korea:
            - Infantry: 1
        - Neighbors:
          - -1062
          - 2317
          - 2488
          - 1921
          - 15208
        
        ## Friendly Land Zone 1406
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 561
        - FriendlyStrength: 1706
        - City: Sao Paulo
        - AreaID: 34
        - Plots: 13
        - CenterX: 64
        - CenterY: 22
        - Units:
          - Brazil:
            - Artillery: 1
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - -1406
          - 1082
          - 2488
          - 2468
          - 3823
          - -2468
        
        ## Enemy Land Zone 1921
        - ZoneValue: 96
        - Dominance: Enemy
        - EnemyStrength: 826
        - NeutralStrength: 914
        - City: Tonga
        - AreaID: 49
        - Plots: 17
        - CenterX: 61
        - CenterY: 41
        - Units:
          - Polynesia:
            - Lancer: 1
        - Neighbors:
          - -1921
          - 1337
        
        ## Neutral Land Zone 2317
        - ZoneValue: 30
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 426
        - NeutralStrength: 826
        - FriendlyStrength: 2643
        - City: Daegu
        - AreaID: 49
        - Plots: 33
        - CenterX: 58
        - CenterY: 30
        - Units:
          - Brazil:
            - Artillery: 1
            - Infantry: 1
          - Korea:
            - Artillery: 1
            - Anti-Aircraft Gun: 1
            - Infantry: 1
        - Neighbors:
          - 14687
          - 1062
          - 12624
          - -1062
          - 1082
          - 1337
          - 2488
        
        ## Friendly Land Zone 2468
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 325
        - FriendlyStrength: 1227
        - City: Salvador
        - AreaID: 35
        - Plots: 12
        - CenterX: 68
        - CenterY: 22
        - Units:
          - Brazil:
            - Artillery: 1
            - Machine Gun: 1
          - City-State Ban Chiang:
            - Infantry: 1
        - Neighbors:
          - 1406
          - -2468
          - 3823
        
        ## Friendly Land Zone 2488
        - ZoneValue: 36
        - Dominance: Friendly
        - NeutralStrength: 726
        - FriendlyStrength: 1375
        - City: Brasilia
        - AreaID: 49
        - Plots: 23
        - CenterX: 62
        - CenterY: 27
        - Units:
          - Brazil:
            - Infantry: 1
            - Bomber: 2
        - Neighbors:
          - 2317
          - 1082
          - 1337
          - 15208
          - 1406
          - 3823
          - -3823
        
        ## Enemy Land Zone 2536
        - ZoneValue: 768
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 1024
        - NeutralStrength: 134
        - FriendlyStrength: 2257
        - City: Nuku Hiva
        - AreaID: 49
        - Plots: 18
        - CenterX: 50
        - CenterY: 36
        - Units:
          - Brazil:
            - Machine Gun: 1
          - Polynesia:
            - Machine Gun: 1
        - Neighbors:
          - -2536
          - -1065
          - 1065
          - 1062
          - -1062
        
        ## Neutral Land Zone 3823
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 411
        - FriendlyStrength: 1631
        - City: Ban Chiang
        - AreaID: 49
        - Plots: 15
        - CenterX: 67
        - CenterY: 26
        - Units:
          - City-State Ban Chiang:
            - Machine Gun: 2
        - Neighbors:
          - 2488
          - 1406
          - -3823
          - 2468
          - 15208
        
        ## Enemy Land Zone 8307
        - ZoneValue: 48
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 595
        - NeutralStrength: 52
        - FriendlyStrength: 933
        - City: Ribe
        - AreaID: 42
        - Plots: 19
        - CenterX: 49
        - CenterY: 24
        - Units:
          - Brazil:
            - Fleet Destroyer: 1
          - Polynesia:
            - Triplane: 1
            - Machine Gun: 2
        - Neighbors:
          - -8307
          - 1065
          - 14687
          - -12624
          - 12624
        
        ## Friendly Land Zone 12624
        - ZoneValue: 3
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 312
        - NeutralStrength: 61
        - FriendlyStrength: 1591
        - City: Viborg
        - AreaID: 43
        - Plots: 15
        - CenterX: 55
        - CenterY: 24
        - Units:
          - Brazil:
            - Triplane: 1
            - Bomber: 1
            - Machine Gun: 1
        - Neighbors:
          - 8307
          - -12624
          - 14687
          - 1082
          - 2317
        
        ## Friendly Land Zone 14687
        - ZoneValue: 24
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 254
        - NeutralStrength: 257
        - FriendlyStrength: 3425
        - City: Aotearoa
        - AreaID: 49
        - Plots: 22
        - CenterX: 54
        - CenterY: 27
        - Units:
          - Brazil:
            - Infantry: 1
            - Triplane: 2
            - Machine Gun: 1
          - Korea:
            - Rifleman: 1
        - Neighbors:
          - 8307
          - 1065
          - -1065
          - 12624
          - 1062
          - 2317
        
        ## Neutral Land Zone 15208
        - ZoneValue: 60
        - Dominance: Friendly
        - NeutralStrength: 837
        - FriendlyStrength: 1011
        - City: Jeonju
        - AreaID: 49
        - Plots: 12
        - CenterX: 65
        - CenterY: 30
        - Units:
          - Brazil:
            - Tank: 1
          - Korea:
            - Infantry: 1
          - Austria:
            - B17: 1
            - Infantry: 1
            - Triplane: 1
            - Bomber: 2
        - Neighbors:
          - 2488
          - 1337
          - -3823
          - 3823
        
        ## Friendly Sea Zone -2468
        - ZoneValue: 12
        - Dominance: Friendly
        - NeutralStrength: 104
        - FriendlyStrength: 1605
        - City: Salvador
        - AreaID: 0
        - Plots: 43
        - CenterX: 70
        - CenterY: 20
        - Units:
          - Brazil:
            - Fleet Destroyer: 2
        - Neighbors:
          - -1406
          - -100000
          - 1406
          - 2468
          - -3823
        
        ## Friendly Sea Zone -1082
        - ZoneValue: 12
        - Dominance: Friendly
        - NeutralStrength: 580
        - FriendlyStrength: 1181
        - City: Rio de Janeiro
        - AreaID: 0
        - Plots: 7
        - CenterX: 60
        - CenterY: 19
        - Units:
          - Brazil:
            - Fleet Destroyer: 1
        - Neighbors:
          - -12624
          - -100000
          - 1082
          - -1406
        
        ## Enemy Sea Zone -8307
        - ZoneValue: 384
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 528
        - NeutralStrength: 199
        - FriendlyStrength: 1273
        - City: Ribe
        - AreaID: 11
        - Plots: 23
        - CenterX: 49
        - CenterY: 21
        - Units:
          - Brazil:
            - Destroyer: 1
            - Fleet Destroyer: 1
        - Neighbors:
          - 8307
          - -1065
          - 1065
          - -12624
        
        ## Friendly Sea Zone -12624
        - ZoneValue: 8
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 186
        - FriendlyStrength: 1758
        - City: Viborg
        - AreaID: 0
        - Plots: 29
        - CenterX: 54
        - CenterY: 20
        - Units:
          - Brazil:
            - Fleet Destroyer: 2
        - Neighbors:
          - -8307
          - 8307
          - -100000
          - 12624
          - -1082
          - 1082
        
        ## Neutral Sea Zone -3823
        - ZoneValue: 6
        - Dominance: Friendly
        - NeutralStrength: 96
        - FriendlyStrength: 1525
        - City: Ban Chiang
        - AreaID: 52
        - Plots: 26
        - CenterX: 70
        - CenterY: 27
        - Units:
          - Brazil:
            - Fleet Destroyer: 1
          - City-State Ban Chiang:
            - Fleet Destroyer: 1
          - Austria:
            - Infantry: 1
        - Neighbors:
          - 2488
          - 3823
          - 15208
          - -2468
          - -100000
        
        ## Neutral Sea Zone -1065
        - ZoneValue: 6
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 946
        - NeutralStrength: 80
        - FriendlyStrength: 1266
        - City: La Venta
        - AreaID: 0
        - Plots: 23
        - CenterX: 47
        - CenterY: 30
        - Units:
          - Polynesia:
            - Ironclad: 1
        - Neighbors:
          - 1065
          - -8307
          - -2536
          - 2536
          - 14687
        
        ## Enemy Sea Zone -1062
        - ZoneValue: 3840
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 1492
        - NeutralStrength: 79
        - FriendlyStrength: 1197
        - City: Honolulu
        - AreaID: 75
        - Plots: 8
        - CenterX: 55
        - CenterY: 35
        - Units:
          - Polynesia:
            - Ironclad: 2
            - Light Tank: 1
            - Machine Gun: 1
            - Cruiser: 1
        - Neighbors:
          - -2536
          - 1062
          - 2536
          - 2317
          - 1337
        
        ## Friendly Sea Zone -1406
        - ZoneValue: 14
        - Dominance: Friendly
        - NeutralStrength: 1172
        - FriendlyStrength: 1282
        - City: Sao Paulo
        - AreaID: 0
        - Plots: 24
        - CenterX: 63
        - CenterY: 19
        - Units:
          - Brazil:
            - Fleet Destroyer: 1
        - Neighbors:
          - -100000
          - -1082
          - 1082
          - 1406
          - -2468
        
        ## Neutral Sea Zone -100000
        - ZoneValue: 1
        - Dominance: Friendly
        - NeutralStrength: 2294
        - FriendlyStrength: 156
        - AreaID: 0
        - Plots: 523
        - CenterX: 73
        - CenterY: 10
        - Units:
          - Austria:
            - Destroyer: 4
            - Tank: 1
            - Infantry: 1
            - Landship: 1
            - Pracinha: 1
        - Neighbors:
          - -12624
          - -1082
          - -1406
          - -2468
          - -3823
        
        ## Enemy Sea Zone -2536
        - ZoneValue: 32
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 1700
        - NeutralStrength: 106
        - FriendlyStrength: 774
        - City: Nuku Hiva
        - AreaID: 0
        - Plots: 44
        - CenterX: 50
        - CenterY: 38
        - Units:
          - Polynesia:
            - Light Tank: 1
        - Neighbors:
          - 2536
          - -1065
          - -1062
          - 1062
        
        ## Enemy Sea Zone -1921
        - ZoneValue: 4
        - Dominance: Enemy
        - EnemyStrength: 557
        - NeutralStrength: 222
        - City: Tonga
        - AreaID: 75
        - Plots: 8
        - CenterX: 60
        - CenterY: 42
        - Units:
          - Polynesia:
            - Ironclad: 1
        - Neighbors:
          - 1921
        
        # Events
        Events: events since you last made a decision.
        
        ## Turn 394
        
        ### 0
        - Type: CityEndsWLTKD
        - Unused: 0
        - Owner: 3: Korea
        - Plains Land 59,30:
          - Owner: Korea
          - CityID: 2317
          - Population: 20
          - IsRiver: true
          - City: Daegu
          - Religion: Buddhism
          - Route: Railroad
        
        ### 1
        - Type: CityBeginsWLTKD
        - Change: 10
        - City:
          - Owner: Korea
          - CityID: 2317
          - Population: 20
          - IsRiver: true
          - City: Daegu
          - Terrain: Plains
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 59
          - Y: 30
        - Player: 3: Korea
        
        ### 2
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15528
        - Player: 3: Korea
        - Plots:
          - Grass Hills 58,29:
            - Owner: Korea
            - IsRiver: true
            - Resource: Jade
            - Improvement: Manufactory
            - Route: Railroad
          - Tundra Hills 58,28:
            - Owner: Korea
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 57,28:
            - Owner: Korea
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 56,27:
            - Owner: Korea
            - IsRiver: true
            - Route: Railroad
        
        ### 3
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16211
        - Player: 3: Korea
        - Plots:
          - Plains Land 54,25:
            - Owner: Brazil
            - Resource: Brazilwood
            - Improvement: Brazilwood Camp
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 55,24:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 54,23:
            - Owner: Brazil
            - CityID: 12624
            - Population: 24
            - IsRiver: true
            - City: Viborg
            - Resource: Oil
            - Religion: Buddhism
            - Route: Railroad
        
        ### 4
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16304
        - Player: 3: Korea
        - Plots:
          - Plains Land 57,27:
            - Owner: Brazil
            - Resource: Iron
            - Improvement: Mine
          - Tundra Hills 58,26:
            - Owner: Brazil
            - Resource: Deer
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 58,25:
            - Owner: Brazil
            - Improvement: Mine
            - Route: Railroad
          - Mountain Mountain 59,24:
            - Owner: Brazil
            - Route: Railroad
        
        ### 5
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15904
        - Player: 3: Korea
        - Plots:
          - Grass Land 64,31:
            - Owner: Austria
            - Resource: Coal
            - Improvement: Town
            - Route: Road
          - Grass Land 65,31:
            - Owner: Austria
            - Improvement: Village
            - Route: Railroad
          - Grass Land 66,30:
            - Owner: Austria
            - CityID: 15208
            - Population: 20
            - IsRiver: true
            - City: Jeonju
            - Religion: Buddhism
            - Route: Railroad
        
        ### 6
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16369
        - Player: 3: Korea
        - Plots:
          - Plains Hills 59,31:
            - Owner: Korea
            - IsRiver: true
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Desert Hills 61,32:
            - Owner: Korea
            - IsRiver: true
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
        
        ### 7
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15569
        - Player: 3: Korea
        - Plots:
          - Grass Land 67,22:
            - Owner: Brazil
            - Resource: Brazilwood
            - Improvement: Brazilwood Camp
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 66,22:
            - Owner: Brazil
            - Improvement: Village
            - Route: Railroad
          - Grass Land 65,22:
            - Owner: Brazil
            - Resource: Bananas
            - Improvement: Town
            - Route: Railroad
          - Grass Land 64,22:
            - Owner: Brazil
            - CityID: 1406
            - Population: 28
            - City: Sao Paulo
            - Religion: Buddhism
            - Route: Railroad
        
        ### 8
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15063
        - Player: 3: Korea
        - Plots:
          - Desert Hills 61,32:
            - Owner: Korea
            - IsRiver: true
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
          - Plains Hills 59,31:
            - Owner: Korea
            - IsRiver: true
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Plains Land 59,30:
            - Owner: Korea
            - CityID: 2317
            - Population: 20
            - IsRiver: true
            - City: Daegu
            - Religion: Buddhism
            - Route: Railroad
        
        ### 9
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: CityBombard
          - Unit: Artillery
          - ID: 15061
        - Player: 3: Korea
        - Plots:
          - Desert Hills 61,32:
            - Owner: Korea
            - IsRiver: true
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
          - Plains Hills 59,31:
            - Owner: Korea
            - IsRiver: true
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Grass Hills 58,31:
            - Owner: Korea
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
        
        ### 10
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 15842
        - Player: 3: Korea
        - Plots:
          - Plains Land 59,30:
            - Owner: Korea
            - CityID: 2317
            - Population: 20
            - IsRiver: true
            - City: Daegu
            - Religion: Buddhism
            - Route: Railroad
          - Plains Hills 59,31:
            - Owner: Korea
            - IsRiver: true
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Desert Hills 61,32:
            - Owner: Korea
            - IsRiver: true
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
        
        ### 11
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 15843
        - Player: 3: Korea
        - Plots:
          - Grass Land 64,31:
            - Owner: Austria
            - Resource: Coal
            - Improvement: Town
            - Route: Road
          - Grass Hills 63,31:
            - Owner: Brazil
            - Resource: Copper
            - Improvement: Mine
        
        ### 12
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 75%
          - AI: Defense
          - Unit: Rifleman
          - ID: 14922
        - Player: 3: Korea
        - Plots:
          - Grass Hills 51,26:
            - Owner: Brazil
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Plains Land 52,26:
            - Owner: Brazil
            - Resource: Cocoa
            - Improvement: Holy Site
            - Route: Railroad
          - Plains Hills 53,26:
            - Owner: Brazil
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Plains Land 54,26:
            - Owner: Brazil
            - Improvement: Village
            - Route: Railroad
          - Desert Land 54,27:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 54,28:
            - Owner: Brazil
            - Improvement: Town
            - Route: Railroad
          - Plains Land 53,29:
            - Owner: Brazil
            - IsRiver: true
            - Resource: Horses
            - Improvement: Citadel
            - Route: Railroad
        
        ### 13
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 92%
          - AI: Defense
          - Unit: Infantry
          - ID: 15903
        - Player: 3: Korea
        - Plots:
          - Desert Hills 61,32:
            - Owner: Korea
            - IsRiver: true
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
          - Plains Hills 59,31:
            - Owner: Korea
            - IsRiver: true
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Plains Land 59,30:
            - Owner: Korea
            - CityID: 2317
            - Population: 20
            - IsRiver: true
            - City: Daegu
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 59,29:
            - Owner: Korea
            - IsRiver: true
            - Resource: Coal
            - Improvement: Academy
        
        ### 14
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3939
        - Player: 3: Korea
        - Plots:
          - Plains Hills 59,31:
            - Owner: Korea
            - IsRiver: true
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Desert Hills 61,32:
            - Owner: Korea
            - IsRiver: true
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
          - Grass Hills 62,32:
            - Owner: Korea
            - Improvement: Mine
        
        ### 15
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 3: Korea
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3939
        - Build: Construct a Railroad
        - Grass Hills 62,32:
          - Owner: Korea
          - Improvement: Mine
        
        ### 16
        - Type: CityCreated
        - City:
          - Name: Borsippa
          - Population: 25
          - ID: 2341
        - Owner: 4: Babylon
        - Project: Public Works
        
        ### 17
        - Type: CityCreated
        - City:
          - Name: Shushan
          - Population: 22
          - ID: 6114
        - Owner: 4: Babylon
        - Project: Public Works
        
        ### 18
        - Type: EspionageState
        - SpyIndex: 5
        - SpyState: 3
        - City:
          - Owner: Brazil
          - CityID: 2468
          - Population: 25
          - City: Salvador
          - Terrain: Grass
          - Resource: Rice
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 69
          - Y: 22
        - SpyOwner: 5: Russia
        
        ### 19
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 14319
        - Player: 5: Russia
        - Plots:
          - Coast 47,22:
            - Owner: Polynesia
          - Ocean 47,21:
            - Owner: Polynesia
          - Ocean 48,20:
            - Owner: Polynesia
          - Ocean 48,19:
            - Owner: Russia
        
        ### 20
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Ironclad
          - ID: 16461
        - Player: 6: Polynesia
        - Plains Land 54,33:
          - Owner: Polynesia
          - CityID: 1062
          - Population: 23
          - IsRiver: true
          - City: Honolulu
          - Religion: Buddhism
          - Route: Railroad
        
        ### 21
        - Type: UnitCreated
        - UnitType: Ironclad
        - Player: 6: Polynesia
        - Unit:
          - Level: 1
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 16461
        - Plains Land 54,33:
          - Owner: Polynesia
          - CityID: 1062
          - Population: 23
          - IsRiver: true
          - City: Honolulu
          - Religion: Buddhism
          - Route: Railroad
        
        ### 22
        - Type: CityTrained
        - Player: 6: Polynesia
        - City:
          - Population: 23
          - Name: Honolulu
          - Health: -51%
          - ID: 1062
        - Unit:
          - Level: 1
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 16461
        
        ### 23
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Ironclad
          - ID: 16462
        - Player: 6: Polynesia
        - Grass Hills 51,36:
          - Owner: Polynesia
          - CityID: 2536
          - Population: 22
          - City: Nuku Hiva
          - Religion: Buddhism
          - Route: Railroad
        
        ### 24
        - Type: UnitCreated
        - UnitType: Ironclad
        - Player: 6: Polynesia
        - Unit:
          - Level: 1
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 16462
        - Grass Hills 51,36:
          - Owner: Polynesia
          - CityID: 2536
          - Population: 22
          - City: Nuku Hiva
          - Religion: Buddhism
          - Route: Railroad
        
        ### 25
        - Type: CityTrained
        - Player: 6: Polynesia
        - City:
          - Name: Nuku Hiva
          - Population: 22
          - ID: 2536
        - Unit:
          - Level: 1
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 16462
        
        ### 26
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 14727
        - Player: 6: Polynesia
        - Plots:
          - Coast 54,34:
            - Owner: Polynesia
          - Plains Land 54,33:
            - Owner: Polynesia
            - CityID: 1062
            - Population: 23
            - IsRiver: true
            - City: Honolulu
            - Religion: Buddhism
            - Route: Railroad
        
        ### 27
        - Type: PlayerTradeRouteCompleted
        - Domain: 0
        - OriginPlayer: 6: Polynesia
        - OriginCity:
          - Population: 23
          - Name: Honolulu
          - Health: -51%
          - ID: 1062
        - DestinationCity:
          - Name: Brussels
          - Population: 19
          - ID: 1072
        - DestinationPlayer: 30
        - Connection: Food
        
        ### 28
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Cargo Ship
          - ID: 16463
        - Player: 6: Polynesia
        - Plains Land 54,33:
          - Owner: Polynesia
          - CityID: 1062
          - Population: 23
          - IsRiver: true
          - City: Honolulu
          - Religion: Buddhism
          - Route: Railroad
        
        ### 29
        - Type: UnitCreated
        - UnitType: Cargo Ship
        - Player: 6: Polynesia
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16463
        - Plains Land 54,33:
          - Owner: Polynesia
          - CityID: 1062
          - Population: 23
          - IsRiver: true
          - City: Honolulu
          - Religion: Buddhism
          - Route: Railroad
        
        ### 30
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15697
        - Player: 6: Polynesia
        - Plots:
          - Grass Land 52,34:
            - Owner: Polynesia
            - Improvement: Moai
            - Route: Railroad
          - Grass Land 52,33:
            - Owner: Polynesia
            - Improvement: Village
            - Route: Railroad
          - Plains Land 53,33:
            - Owner: Polynesia
            - IsRiver: true
            - Improvement: Moai
            - Route: Railroad
          - Plains Land 54,33:
            - Owner: Polynesia
            - CityID: 1062
            - Population: 23
            - IsRiver: true
            - City: Honolulu
            - Religion: Buddhism
            - Route: Railroad
          - Desert Hills 55,33:
            - Owner: Polynesia
            - Resource: Sheep
            - Improvement: Moai
            - Route: Railroad
        
        ### 31
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 16461
        - Player: 6: Polynesia
        - Promotions:
          - Hull I
          - Hull II
        
        ### 32
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 16462
        - Player: 6: Polynesia
        - Promotions:
          - Hull I
          - Hull II
          - Hull III
        
        ### 33
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 74%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 15937
        - Player: 6: Polynesia
        - Plots:
          - Grass Hills 51,35:
            - Owner: Polynesia
            - Resource: Jade
            - Improvement: Moai
            - Route: Railroad
          - Grass Land 52,34:
            - Owner: Polynesia
            - Improvement: Moai
            - Route: Railroad
          - Grass Land 52,33:
            - Owner: Polynesia
            - Improvement: Village
            - Route: Railroad
        
        ### 34
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 11%
          - AI: AssaultSea
          - Unit: Cruiser
          - ID: 14373
        - Player: 6: Polynesia
        - Coast 53,35:
          - Owner: Polynesia
        
        ### 35
        - Type: CombatResult
        - Grass Hills 53,32:
          - Owner: Polynesia
          - IsRiver: true
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 29
          - Damage: 29
          - Player: 2: Brazil
          - Unit:
            - Level: 4
            - AI: Paradrop
            - Unit: Paratrooper
            - ID: 16207
        
        ### 36
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 90%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15938
        - Player: 6: Polynesia
        - Plains Land 53,36:
          - Owner: Polynesia
          - Improvement: Moai
        
        ### 37
        - Type: CombatResult
        - Plains Land 53,33:
          - Owner: Polynesia
          - IsRiver: true
          - Improvement: Moai
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 14
          - Damage: 70
          - Player: 2: Brazil
          - Unit:
            - Level: 4
            - Health: 44%
            - AI: FastAttack
            - Unit: T-34
            - ID: 14983
        
        ### 38
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 90%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15938
        - Player: 6: Polynesia
        - Coast 53,35:
          - Owner: Polynesia
        
        ### 39
        - Type: CombatResult
        - Plains Land 49,23:
          - Owner: Polynesia
          - IsRiver: true
          - Resource: Bananas
          - Improvement: Moai
          - Route: Road
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 34
          - Damage: 79
          - Unit:
            - Level: 4
            - Health: 55%
            - AI: Counter
            - Unit: Anti-Aircraft Gun
            - ID: 16205
          - Player: 2: Brazil
        
        ### 40
        - Type: CombatResult
        - Plains Land 49,23:
          - Owner: Polynesia
          - IsRiver: true
          - Resource: Bananas
          - Improvement: Moai
          - Route: Road
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 21
          - Damage: 100
          - Player: 2: Brazil
          - Unit:
            - Level: 4
            - Health: 21%
            - AI: Counter
            - Unit: Anti-Aircraft Gun
            - ID: 16205
        
        ### 41
        - Type: UnitKilledInCombat
        - KilledPlayer: 2: Brazil
        - KillerPlayer: 6: Polynesia
        - KilledUnit: Anti-Aircraft Gun
        
        ### 42
        - Type: CombatResult
        - Plains Hills 49,33:
          - Owner: Polynesia
          - Resource: Coal
          - Improvement: Academy
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 29
          - Damage: 69
          - Unit:
            - Level: 4
            - Health: 60%
            - AI: Ranged
            - Unit: Machine Gun
            - ID: 15136
          - Player: 2: Brazil
        
        ### 43
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15745
        - Player: 6: Polynesia
        - Grass Hills 51,36:
          - Owner: Polynesia
          - CityID: 2536
          - Population: 22
          - City: Nuku Hiva
          - Religion: Buddhism
          - Route: Railroad
        
        ### 44
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - Health: 65%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 15744
        - Player: 6: Polynesia
        - Plots:
          - Ocean 48,34:
            - Owner: Polynesia
        
        ### 45
        - Type: UnitCaptured
        - WasKilled: true
        - OldOwner: 2: Brazil
        - CapturedUnit:
          - Level: 1
          - AI: Diplomat
          - Unit: Great Diplomat
          - ID: 16007
        - NewOwner: 6: Polynesia
        - CapturingUnit:
          - Level: 2
          - Health: 65%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 15744
        - Capture: Combat
        
        ### 46
        - Type: UnitKilledInCombat
        - KillerPlayer: 6: Polynesia
        - KilledPlayer: 2: Brazil
        - KillingUnit:
          - Level: 2
          - Health: 65%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 15744
        - KilledUnit: Great Diplomat
        
        ### 47
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - Health: 65%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 15744
        - Player: 6: Polynesia
        
        ### 48
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 16462
        - Player: 6: Polynesia
        - Plots:
          - Coast 50,35:
            - Owner: Polynesia
          - Coast 50,34:
            - Owner: Polynesia
          - Coast 49,34:
            - Owner: Polynesia
          - Coast 48,33:
            - Owner: Polynesia
          - Coast 48,32:
            - Owner: Polynesia
        
        ### 49
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15805
        - Player: 6: Polynesia
        - Plains Land 47,23:
          - Owner: Polynesia
          - Resource: Uranium
          - Improvement: Moai
          - Route: Road
        
        ### 50
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 16403
        - Player: 6: Polynesia
        - Plots:
          - Ocean 46,21:
            - Owner: Polynesia
          - Ocean 47,20:
            - Owner: Polynesia
        
        ### 51
        - Type: CombatResult
        - Ocean 48,21:
          - Owner: Polynesia
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 17
          - Damage: 60
          - Player: 2: Brazil
          - Unit:
            - Level: 5
            - Health: 56%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 15838
        
        ### 52
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 74%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 15937
        - Player: 6: Polynesia
        - Plots:
          - Grass Land 52,34:
            - Owner: Polynesia
            - Improvement: Moai
            - Route: Railroad
          - Coast 52,35:
            - Owner: Polynesia
        
        ### 53
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 16403
        - Player: 6: Polynesia
        - Ocean 46,21:
          - Owner: Polynesia
        
        ### 54
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 16461
        - Player: 6: Polynesia
        - Coast 54,34:
          - Owner: Polynesia
        
        ### 55
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - Health: 42%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 14726
        - Player: 6: Polynesia
        - Coast 61,42:
          - Owner: Polynesia
        
        ### 56
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3500
        - Player: 6: Polynesia
        - Plains Land 50,36:
          - Owner: Polynesia
          - Resource: Horses
          - Improvement: Moai
        
        ### 57
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3747
        - Player: 6: Polynesia
        - Plains Land 61,40:
          - Owner: Polynesia
          - Improvement: Town
          - Route: Railroad
        
        ### 58
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 15936
        - Player: 6: Polynesia
        - Plots:
          - Coast 51,37:
            - Owner: Polynesia
          - Grass Hills 51,36:
            - Owner: Polynesia
            - CityID: 2536
            - Population: 22
            - City: Nuku Hiva
            - Religion: Buddhism
            - Route: Railroad
        
        ### 59
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16463
        - Player: 6: Polynesia
        - Grass Land 61,41:
          - Owner: Polynesia
          - CityID: 1921
          - Population: 23
          - City: Tonga
          - Religion: Buddhism
          - Route: Railroad
        
        ### 60
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15697
        - Player: 6: Polynesia
        - Plains Land 54,33:
          - Owner: Polynesia
          - CityID: 1062
          - Population: 23
          - IsRiver: true
          - City: Honolulu
          - Religion: Buddhism
          - Route: Railroad
        
        ### 61
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Defense
          - Unit: Infantry
          - ID: 15186
        - Player: 22
        - Grass Hills 69,24:
          - Owner: City-State Ban Chiang
          - Improvement: Mine
        
        ### 62
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: CityBombard
          - Unit: Artillery
          - ID: 13925
        - Player: 23
        - Grass Land 49,31:
          - Owner: City-State La Venta
          - Improvement: Farm
        
        ### 63
        - Type: CombatResult
        - Coast 48,32:
          - Owner: Polynesia
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 45
          - Damage: 45
          - Unit:
            - Level: 4
            - AI: AttackSea
            - Unit: Ironclad
            - ID: 16462
          - Player: 6: Polynesia
        
        ## Turn 395
        
        ### 0
        - Type: CityConvertsReligion
        - City:
          - Owner: Brazil
          - CityID: 12624
          - Population: 24
          - IsRiver: true
          - City: Viborg
          - Terrain: Grass
          - Resource: Oil
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 54
          - Y: 23
        - Owner: 2: Brazil
        - Religion: Buddhism
        
        ### 1
        - Type: EspionageState
        - SpyIndex: 7
        - SpyState: 3
        - City:
          - Owner: Polynesia
          - CityID: 8307
          - Population: 19
          - IsRiver: true
          - City: Ribe
          - Terrain: Grass
          - Resource: Bananas
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 48
          - Y: 23
        - SpyOwner: 0: Austria
        
        ### 2
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 15458
        - Player: 0: Austria
        - Plots:
          - Ocean 71,25:
            - Owner: Brazil
          - Ocean 72,26:
            - Owner: City-State Ban Chiang
        
        ### 3
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 15558
        - Player: 0: Austria
        - Plots:
          - Coast 47,28:
            - Owner: City-State La Venta
          - Coast 47,29:
            - Owner: City-State La Venta
          - Coast 48,29:
            - Owner: City-State La Venta
          - Grass Land 49,29:
            - Owner: City-State La Venta
            - CityID: 1065
            - Population: 18
            - City: La Venta
            - Religion: Buddhism
            - Route: Railroad
        
        ### 4
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Defense
          - Unit: Infantry
          - ID: 14967
        - Player: 0: Austria
        
        ### 5
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Defense
          - Unit: Pracinha
          - ID: 15262
        - Player: 0: Austria
        
        ### 6
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Light Tank
          - ID: 13509
        - Player: 0: Austria
        
        ### 7
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13503
        - Player: 0: Austria
        
        ### 8
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: FastAttack
          - Unit: Tank
          - ID: 15122
        - Player: 0: Austria
        
        ### 9
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: FastAttack
          - Unit: Landship
          - ID: 13614
        - Player: 0: Austria
        
        ### 10
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 84%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 13882
        - Player: 0: Austria
        
        ### 11
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 74%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 13344
        - Player: 0: Austria
        
        ### 12
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 80%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 14348
        - Player: 0: Austria
        
        ### 13
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 85%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 14123
        - Player: 0: Austria
        
        ### 14
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 31%
          - AI: AssaultSea
          - Unit: Submarine
          - ID: 14398
        - Player: 0: Austria
        
        ### 15
        - Type: RebaseTo
        - Player: 0: Austria
        - Unit:
          - Level: 5
          - AI: AttackAir
          - Unit: B17
          - ID: 16193
        - Grass Land 66,30:
          - Owner: Austria
          - CityID: 15208
          - Population: 20
          - IsRiver: true
          - City: Jeonju
          - Religion: Buddhism
          - Route: Railroad
        
        ### 16
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: AttackAir
          - Unit: B17
          - ID: 16193
        - Player: 0: Austria
        - Grass Land 66,30:
          - Owner: Austria
          - CityID: 15208
          - Population: 20
          - IsRiver: true
          - City: Jeonju
          - Religion: Buddhism
          - Route: Railroad
        
        ### 17
        - Type: RebaseTo
        - Player: 0: Austria
        - Unit:
          - Level: 4
          - AI: DefenseAir
          - Unit: Triplane
          - ID: 14283
        - Grass Land 66,30:
          - Owner: Austria
          - CityID: 15208
          - Population: 20
          - IsRiver: true
          - City: Jeonju
          - Religion: Buddhism
          - Route: Railroad
        
        ### 18
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: DefenseAir
          - Unit: Triplane
          - ID: 14283
        - Player: 0: Austria
        - Grass Land 66,30:
          - Owner: Austria
          - CityID: 15208
          - Population: 20
          - IsRiver: true
          - City: Jeonju
          - Religion: Buddhism
          - Route: Railroad
        
        ### 19
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 6036
        - Player: 0: Austria
        - Grass Land 66,30:
          - Owner: Austria
          - CityID: 15208
          - Population: 20
          - IsRiver: true
          - City: Jeonju
          - Religion: Buddhism
          - Route: Railroad
        
        ### 20
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Defense
          - Unit: Infantry
          - ID: 15831
        - Player: 0: Austria
        - Coast 68,27:
          - Owner: City-State Ban Chiang
        
        ### 21
        - Type: PlayerDoneTurn
        - NextPlayer: 2: Brazil
        - Player: 0: Austria
        
        ### 22
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Anti-Aircraft Gun
          - ID: 16477
        - Player: 2: Brazil
        - Grass Land 65,22:
          - Owner: Brazil
          - Resource: Bananas
          - Improvement: Town
          - Route: Railroad
        
        ### 23
        - Type: UnitCreated
        - UnitType: Anti-Aircraft Gun
        - Player: 2: Brazil
        - Unit:
          - Level: 1
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16477
        - Grass Land 65,22:
          - Owner: Brazil
          - Resource: Bananas
          - Improvement: Town
          - Route: Railroad
        
        ### 24
        - Type: CityTrained
        - WithGold: true
        - Player: 2: Brazil
        - City:
          - Name: Sao Paulo
          - Population: 28
          - ID: 1406
        - Unit:
          - Level: 1
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16477
        
        ### 25
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Great Writer
          - ID: 16481
        - Player: 2: Brazil
        - Plains Hills 60,23:
          - Owner: Brazil
          - CityID: 1082
          - Population: 27
          - IsRiver: true
          - City: Rio de Janeiro
          - Resource: Coal
          - Religion: Buddhism
          - Route: Railroad
        
        ### 26
        - Type: UnitCreated
        - UnitType: Great Writer
        - Player: 2: Brazil
        - Unit:
          - Level: 1
          - AI: Writer
          - Unit: Great Writer
          - ID: 16481
        - Plains Hills 60,23:
          - Owner: Brazil
          - CityID: 1082
          - Population: 27
          - IsRiver: true
          - City: Rio de Janeiro
          - Resource: Coal
          - Religion: Buddhism
          - Route: Railroad
        
        ### 27
        - Type: CityTrained
        - WithFaith: true
        - Player: 2: Brazil
        - City:
          - Name: Rio de Janeiro
          - Population: 27
          - ID: 1082
        - Unit:
          - Level: 1
          - AI: Writer
          - Unit: Great Writer
          - ID: 16481
        
        ### 28
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15217
        - Player: 2: Brazil
        - Plots:
          - Grass Hills 51,26:
            - Owner: Brazil
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Plains Land 52,26:
            - Owner: Brazil
            - Resource: Cocoa
            - Improvement: Holy Site
            - Route: Railroad
          - Plains Hills 53,26:
            - Owner: Brazil
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Plains Land 54,26:
            - Owner: Brazil
            - Improvement: Village
            - Route: Railroad
          - Plains Land 54,25:
            - Owner: Brazil
            - Resource: Brazilwood
            - Improvement: Brazilwood Camp
            - Route: Railroad
            - Feature: Jungle
        
        ### 29
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15218
        - Player: 2: Brazil
        - Plots:
          - Grass Land 62,23:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 63,23:
            - Owner: Brazil
            - Improvement: Town
            - Route: Railroad
          - Grass Land 64,22:
            - Owner: Brazil
            - CityID: 1406
            - Population: 28
            - City: Sao Paulo
            - Religion: Buddhism
            - Route: Railroad
          - Grass Land 65,22:
            - Owner: Brazil
            - Resource: Bananas
            - Improvement: Town
            - Route: Railroad
          - Grass Land 66,22:
            - Owner: Brazil
            - Improvement: Village
            - Route: Railroad
        
        ### 30
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15779
        - Player: 2: Brazil
        - Plots:
          - Grass Land 63,23:
            - Owner: Brazil
            - Improvement: Town
            - Route: Railroad
          - Grass Land 64,24:
            - Owner: Brazil
            - Improvement: Village
            - Route: Railroad
          - Grass Hills 63,25:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 63,26:
            - Owner: Brazil
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 63,27:
            - Owner: Brazil
            - Improvement: Village
            - Route: Railroad
          - Grass Land 63,28:
            - Owner: Brazil
            - CityID: 2488
            - Population: 26
            - City: Brasilia
            - Resource: Horses
            - Religion: Buddhism
            - Route: Railroad
        
        ### 31
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16046
        - Player: 2: Brazil
        - Plots:
          - Grass Hills 58,29:
            - Owner: Korea
            - IsRiver: true
            - Resource: Jade
            - Improvement: Manufactory
            - Route: Railroad
          - Tundra Hills 58,28:
            - Owner: Korea
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 57,27:
            - Owner: Brazil
            - Resource: Iron
            - Improvement: Mine
          - Tundra Hills 58,26:
            - Owner: Brazil
            - Resource: Deer
            - Route: Railroad
            - Feature: Forest
        
        ### 32
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15670
        - Player: 2: Brazil
        - Plots:
          - Grass Hills 59,23:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 58,23:
            - Owner: Brazil
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 57,23:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 56,23:
            - Owner: Brazil
            - IsRiver: true
            - Resource: Maize
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 55,23:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 54,23:
            - Owner: Brazil
            - CityID: 12624
            - Population: 24
            - IsRiver: true
            - City: Viborg
            - Resource: Oil
            - Religion: Buddhism
            - Route: Railroad
        
        ### 33
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15409
        - Player: 2: Brazil
        - Plots:
          - Grass Land 62,23:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 63,23:
            - Owner: Brazil
            - Improvement: Town
            - Route: Railroad
          - Grass Land 64,22:
            - Owner: Brazil
            - CityID: 1406
            - Population: 28
            - City: Sao Paulo
            - Religion: Buddhism
            - Route: Railroad
        
        ### 34
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 14745
        - Player: 2: Brazil
        - Plots:
          - Plains Hills 53,26:
            - Owner: Brazil
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Grass Hills 53,25:
            - Owner: Brazil
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 54,24:
            - Owner: Brazil
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 54,23:
            - Owner: Brazil
            - CityID: 12624
            - Population: 24
            - IsRiver: true
            - City: Viborg
            - Resource: Oil
            - Religion: Buddhism
            - Route: Railroad
          - Grass Land 55,23:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
        
        ### 35
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 14746
        - Player: 2: Brazil
        - Plots:
          - Grass Land 56,23:
            - Owner: Brazil
            - IsRiver: true
            - Resource: Maize
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 57,23:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Hills 58,23:
            - Owner: Brazil
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 59,23:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 60,23:
            - Owner: Brazil
            - CityID: 1082
            - Population: 27
            - IsRiver: true
            - City: Rio de Janeiro
            - Resource: Coal
            - Religion: Buddhism
            - Route: Railroad
        
        ### 36
        - Type: PlayerTradeRouteCompleted
        - Domain: 2
        - OriginPlayer: 2: Brazil
        - DestinationCity:
          - Name: Aotearoa
          - Population: 21
          - ID: 14687
        - DestinationPlayer: 2: Brazil
        - OriginCity:
          - Name: Rio de Janeiro
          - Population: 27
          - ID: 1082
        - Connection: Gold
        
        ### 37
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 16482
        - Player: 2: Brazil
        - Plains Hills 60,23:
          - Owner: Brazil
          - CityID: 1082
          - Population: 27
          - IsRiver: true
          - City: Rio de Janeiro
          - Resource: Coal
          - Religion: Buddhism
          - Route: Railroad
        
        ### 38
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 2: Brazil
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16482
        - Plains Hills 60,23:
          - Owner: Brazil
          - CityID: 1082
          - Population: 27
          - IsRiver: true
          - City: Rio de Janeiro
          - Resource: Coal
          - Religion: Buddhism
          - Route: Railroad
        
        ### 39
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15465
        - Player: 2: Brazil
        - Plots:
          - Plains Hills 59,31:
            - Owner: Korea
            - IsRiver: true
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Desert Land 60,32:
            - Owner: Korea
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 61,32:
            - Owner: Korea
            - IsRiver: true
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 61,33:
            - Owner: Korea
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
        
        ### 40
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16296
        - Player: 2: Brazil
        - Plots:
          - Plains Land 66,26:
            - Owner: Brazil
            - IsRiver: true
          - Grass Land 67,26:
            - Owner: City-State Ban Chiang
            - IsRiver: true
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
          - Grass Land 68,26:
            - Owner: City-State Ban Chiang
            - CityID: 3823
            - Population: 19
            - IsRiver: true
            - City: Ban Chiang
            - Religion: Buddhism
            - Route: Railroad
        
        ### 41
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16107
        - Player: 2: Brazil
        - Plots:
          - Grass Land 63,27:
            - Owner: Brazil
            - Improvement: Village
            - Route: Railroad
          - Grass Hills 63,26:
            - Owner: Brazil
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 62,25:
            - Owner: Brazil
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Grass Land 62,24:
            - Owner: Brazil
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
          - Grass Hills 61,24:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 60,23:
            - Owner: Brazil
            - CityID: 1082
            - Population: 27
            - IsRiver: true
            - City: Rio de Janeiro
            - Resource: Coal
            - Religion: Buddhism
            - Route: Railroad
        
        ### 42
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15361
        - Player: 2: Brazil
        - Plots:
          - Grass Land 68,22:
            - Owner: Brazil
            - Resource: Rice
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 69,22:
            - Owner: Brazil
            - CityID: 2468
            - Population: 25
            - City: Salvador
            - Resource: Rice
            - Religion: Buddhism
            - Route: Railroad
          - Grass Land 67,22:
            - Owner: Brazil
            - Resource: Brazilwood
            - Improvement: Brazilwood Camp
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 66,22:
            - Owner: Brazil
            - Improvement: Village
            - Route: Railroad
          - Grass Land 65,22:
            - Owner: Brazil
            - Resource: Bananas
            - Improvement: Town
            - Route: Railroad
        
        ### 43
        - Type: EspionageState
        - SpyIndex: 6
        - SpyState: 0
        - SpyOwner: 2: Brazil
        
        ### 44
        - Type: EspionageState
        - SpyIndex: 6
        - SpyState: 1
        - City:
          - Owner: Polynesia
          - CityID: 2953
          - Population: 21
          - City: Raiatea
          - Terrain: Plains
          - Resource: Sheep
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Hills
          - X: 63
          - Y: 46
        - SpyOwner: 2: Brazil
        
        ### 45
        - Type: PlayerDoTurn
        - Player: 2: Brazil
        
        ### 46
        - Type: UnitPromoted
        - Unit:
          - Level: 5
          - Health: 41%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15136
        - Player: 2: Brazil
        - Promotion: Range
        
        ### 47
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16477
        - Player: 2: Brazil
        - Promotions:
          - Shock I
          - Shock II
        
        ### 48
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 30%
          - AI: FastAttack
          - Unit: T-34
          - ID: 14983
        - Player: 2: Brazil
        - Plots:
          - Grass Land 52,33:
            - Owner: Polynesia
            - Improvement: Village
            - Route: Railroad
          - Plains Land 52,32:
            - Owner: Polynesia
            - Improvement: Fort
          - Plains Land 51,31:
            - Owner: Polynesia
          - Grass Land 51,30:
            - Owner: City-State La Venta
            - Improvement: Embassy
            - Route: Railroad
        
        ### 49
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Musician
          - Unit: Great Musician
          - ID: 16360
        - Player: 2: Brazil
        - Grass Land 65,29:
          - Owner: Austria
          - IsRiver: true
          - Improvement: Farm
          - Route: Railroad
        
        ### 50
        - Type: GreatPersonExpended
        - Player: 2: Brazil
        - City:
          - Owner: Austria
          - IsRiver: true
          - Terrain: Grass
          - Improvement: Farm
          - Route: Railroad
          - Plot: Land
          - X: 65
          - Y: 29
        - Unit:
          - Level: 1
          - AI: Musician
          - Unit: Great Musician
          - ID: 16360
        - GreatPerson: 134
        
        ### 51
        - Type: CombatResult
        - Plains Land 54,33:
          - Owner: Polynesia
          - CityID: 1062
          - Population: 23
          - IsRiver: true
          - City: Honolulu
          - Religion: Buddhism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 23
          - Damage: 23
        - Defender:
          - RemainingHP: 23
          - Damage: 476
          - Player: 6: Polynesia
        
        ### 52
        - Type: UnitKilledInCombat
        - KilledPlayer: 6: Polynesia
        - KillerPlayer: 2: Brazil
        - KilledUnit: Gatling Gun
        
        ### 53
        - Type: CombatResult
        - Plains Land 54,33:
          - Owner: Polynesia
          - CityID: 1062
          - Population: 23
          - IsRiver: true
          - City: Honolulu
          - Religion: Buddhism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 35
          - Damage: 511
          - Player: 6: Polynesia
        
        ### 54
        - Type: CombatResult
        - Plains Land 54,33:
          - Owner: Polynesia
          - CityID: 1062
          - Population: 23
          - IsRiver: true
          - City: Honolulu
          - Religion: Buddhism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 17
          - Damage: 17
        - Defender:
          - RemainingHP: 36
          - Damage: 547
          - Player: 6: Polynesia
        
        ### 55
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 71%
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 16207
        - Player: 2: Brazil
        - Plains Land 53,33:
          - Owner: Polynesia
          - IsRiver: true
          - Improvement: Moai
          - Route: Railroad
        
        ### 56
        - Type: CombatResult
        - Plains Land 54,33:
          - Owner: Polynesia
          - CityID: 1062
          - Population: 23
          - IsRiver: true
          - City: Honolulu
          - Religion: Buddhism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 79
          - Damage: 626
          - Player: 6: Polynesia
        
        ### 57
        - Type: CombatResult
        - Plains Land 54,33:
          - Owner: Polynesia
          - CityID: 1062
          - Population: 23
          - IsRiver: true
          - City: Honolulu
          - Religion: Buddhism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 55
          - Damage: 681
          - Player: 6: Polynesia
        
        ### 58
        - Type: CombatResult
        - Plains Land 54,33:
          - Owner: Polynesia
          - CityID: 1062
          - Population: 23
          - IsRiver: true
          - City: Honolulu
          - Religion: Buddhism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 42
          - Damage: 723
          - Player: 6: Polynesia
        
        ### 59
        - Type: CombatResult
        - Plains Land 54,33:
          - Owner: Polynesia
          - CityID: 1062
          - Population: 23
          - IsRiver: true
          - City: Honolulu
          - Religion: Buddhism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 7
          - Damage: 37
        - Defender:
          - RemainingHP: 51
          - Damage: 774
          - Player: 6: Polynesia
        
        ### 60
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 94%
          - AI: CityBombard
          - Unit: Artillery
          - ID: 15894
        - Player: 2: Brazil
        - Plains Land 56,30:
          - Owner: Polynesia
          - Resource: Wheat
          - Improvement: Academy
          - Route: Road
        
        ### 61
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 73%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15975
        - Player: 2: Brazil
        - Plots:
          - Plains Land 55,30:
            - Owner: Polynesia
            - IsRiver: true
            - Resource: Aluminum
            - Improvement: Holy Site
            - Route: Railroad
          - Plains Land 54,29:
            - Owner: Brazil
            - IsRiver: true
            - Resource: Maize
            - Improvement: Farm
            - Route: Railroad
        
        ### 62
        - Type: CombatResult
        - Coast 48,32:
          - Owner: Polynesia
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 28
          - Damage: 73
          - Player: 6: Polynesia
          - Unit:
            - Level: 4
            - Health: 67%
            - AI: AttackSea
            - Unit: Ironclad
            - ID: 16462
        
        ### 63
        - Type: CombatResult
        - Coast 48,32:
          - Owner: Polynesia
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 32
          - Damage: 105
          - Player: 6: Polynesia
          - Unit:
            - Level: 4
            - Health: 47%
            - AI: AttackSea
            - Unit: Ironclad
            - ID: 16462
        
        ### 64
        - Type: CombatResult
        - Coast 48,32:
          - Owner: Polynesia
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 26
          - Damage: 131
          - Player: 6: Polynesia
          - Unit:
            - Level: 4
            - Health: 25%
            - AI: AttackSea
            - Unit: Ironclad
            - ID: 16462
        
        ### 65
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 94%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 15614
        - Player: 2: Brazil
        - Plots:
          - Coast 51,21:
            - Owner: Brazil
          - Coast 50,21:
            - Owner: Polynesia
          - Coast 49,21:
            - Owner: Polynesia
          - Ocean 48,21:
            - Owner: Polynesia
          - Coast 48,22:
            - Owner: Polynesia
        
        ### 66
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 56%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 15899
        - Player: 2: Brazil
        - Coast 50,21:
          - Owner: Polynesia
        
        ### 67
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 40%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 15838
        - Player: 2: Brazil
        - Coast 49,22:
          - Owner: Polynesia
        
        ### 68
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 41%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16295
        - Player: 2: Brazil
        - Plains Land 51,23:
          - Owner: Brazil
          - Improvement: Citadel
          - Route: Railroad
        
        ### 69
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 40%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 15838
        - Player: 2: Brazil
        - Plots:
          - Coast 49,21:
            - Owner: Polynesia
          - Coast 50,21:
            - Owner: Polynesia
          - Coast 51,21:
            - Owner: Brazil
          - Coast 52,22:
            - Owner: Brazil
          - Plains Land 51,23:
            - Owner: Brazil
            - Improvement: Citadel
            - Route: Railroad
        
        ### 70
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 41%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16295
        - Player: 2: Brazil
        - Plots:
          - Coast 52,22:
            - Owner: Brazil
          - Coast 51,21:
            - Owner: Brazil
          - Coast 50,21:
            - Owner: Polynesia
          - Coast 49,21:
            - Owner: Polynesia
          - Coast 49,22:
            - Owner: Polynesia
        
        ### 71
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 56%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 15899
        - Player: 2: Brazil
        - Ocean 50,20:
          - Owner: Polynesia
        
        ### 72
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 99%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14848
        - Player: 2: Brazil
        - Plots:
          - Grass Land 49,27:
            - Owner: City-State La Venta
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 50,28:
            - Owner: City-State La Venta
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
          - Grass Land 50,29:
            - Owner: City-State La Venta
            - Improvement: Farm
        
        ### 73
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 15776
        - Player: 2: Brazil
        - Plots:
          - Plains Hills 53,26:
            - Owner: Brazil
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Plains Land 52,26:
            - Owner: Brazil
            - Resource: Cocoa
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Hills 51,26:
            - Owner: Brazil
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 50,27:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Land 51,28:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Farm
        
        ### 74
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 94%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 15614
        - Player: 2: Brazil
        - Ocean 48,21:
          - Owner: Polynesia
        
        ### 75
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 56%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 15899
        - Player: 2: Brazil
        - Plots:
          - Coast 53,20:
            - Owner: Brazil
          - Coast 53,21:
            - Owner: Brazil
        
        ### 76
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 54%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16045
        - Player: 2: Brazil
        - Plots:
          - Ocean 49,20:
            - Owner: Polynesia
          - Ocean 50,20:
            - Owner: Polynesia
          - Coast 53,20:
            - Owner: Brazil
        
        ### 77
        - Type: RebaseTo
        - Player: 2: Brazil
        - Unit:
          - Level: 4
          - AI: DefenseAir
          - Unit: Triplane
          - ID: 15518
        - Plains Hills 60,23:
          - Owner: Brazil
          - CityID: 1082
          - Population: 27
          - IsRiver: true
          - City: Rio de Janeiro
          - Resource: Coal
          - Religion: Buddhism
          - Route: Railroad
        
        ### 78
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: DefenseAir
          - Unit: Triplane
          - ID: 15518
        - Player: 2: Brazil
        - Plains Hills 60,23:
          - Owner: Brazil
          - CityID: 1082
          - Population: 27
          - IsRiver: true
          - City: Rio de Janeiro
          - Resource: Coal
          - Religion: Buddhism
          - Route: Railroad
        
        ### 79
        - Type: RebaseTo
        - Player: 2: Brazil
        - Unit:
          - Level: 4
          - AI: AttackAir
          - Unit: Bomber
          - ID: 14146
        - Plains Hills 60,23:
          - Owner: Brazil
          - CityID: 1082
          - Population: 27
          - IsRiver: true
          - City: Rio de Janeiro
          - Resource: Coal
          - Religion: Buddhism
          - Route: Railroad
        
        ### 80
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackAir
          - Unit: Bomber
          - ID: 14146
        - Player: 2: Brazil
        - Plains Hills 60,23:
          - Owner: Brazil
          - CityID: 1082
          - Population: 27
          - IsRiver: true
          - City: Rio de Janeiro
          - Resource: Coal
          - Religion: Buddhism
          - Route: Railroad
        
        ### 81
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Engineer
          - Unit: Great Engineer
          - ID: 16105
        - Player: 2: Brazil
        - Plots:
          - Coast 69,21:
            - Owner: Brazil
          - Coast 69,20:
            - Owner: Brazil
          - Desert Hills 68,19:
            - Owner: Brazil
            - Resource: Gold
            - Improvement: Mine
        
        ### 82
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: WorkerSea
          - Unit: Work Boat
          - ID: 15774
        - Player: 2: Brazil
        - Plots:
          - Coast 61,19:
            - Owner: Brazil
          - Coast 62,20:
            - Owner: Brazil
          - Coast 61,21:
            - Owner: Brazil
        
        ### 83
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 16483
        - Player: 2: Brazil
        - Plains Hills 60,23:
          - Owner: Brazil
          - CityID: 1082
          - Population: 27
          - IsRiver: true
          - City: Rio de Janeiro
          - Resource: Coal
          - Religion: Buddhism
          - Route: Railroad
        
        ### 84
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 2: Brazil
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16483
        - Plains Hills 60,23:
          - Owner: Brazil
          - CityID: 1082
          - Population: 27
          - IsRiver: true
          - City: Rio de Janeiro
          - Resource: Coal
          - Religion: Buddhism
          - Route: Railroad
        
        ### 85
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16483
        - Player: 2: Brazil
        - Plots:
          - Grass Hills 59,23:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 58,23:
            - Owner: Brazil
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 57,23:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 56,23:
            - Owner: Brazil
            - IsRiver: true
            - Resource: Maize
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 56,24:
            - Owner: Brazil
            - IsRiver: true
            - Resource: Cocoa
            - Improvement: Plantation
            - Route: Railroad
        
        ### 86
        - Type: PlayerDoneTurn
        - NextPlayer: 3: Korea
        - Player: 2: Brazil
        
        You, Pedro II (leader of Brazil, Player 2), are making strategic decisions after turn 395.
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
    - You are Pedro II, leader of Brazil (Opponent 2).
      
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
      - Name: Brazil
      - Uniques:
        - Unique Unit: Bandeirante, Replacing Explorer (Requires technology: Compass)
        - Unique Unit: Amazonas, Replacing Ironclad (Requires technology: Industrialization)
        - Unique Building: Embrapa, Replacing Research Lab (Requires technology: Plastics)
        - Unique Improvement: Brazilwood Camp (Can only be built on Jungle or Forest tiles without access to Fresh Water, and cannot be built adjacent to another Brazilwood Camp. It spawns and connects a Brazilwood Resource under the tile.); Requires technology: Calendar
        - Civilization Ability: "We Love the King Day" becomes Carnival, adding -50% Unhappiness from Needs. When a Golden Age begins, 30% of Golden Age Points convert into Gold and Tourism, and Cities gain 10 turns of Carnival.
      - Leader: Pedro II
      - OpponentID: 2
      
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
      - Computers: Grants an additional Trade Route. Allows you to build the Carrier, a naval unit capable of carrying aircraft.
        Completing it would unlock: Telecommunications, Satellites
      - Advanced Ballistics: Allows you to build the Nuclear Missile, a frightening weapon that requires Uranium, and is capable of destroying units and cities. Also allows you to build the Guided Missile, an inexpensive single-use Unit that can damage enemy Units, and the SS Booster, one of the Spaceship parts necessary to win a Science Victory.
        Completing it would unlock: Lasers, Stealth
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      - Mobile Tactics: Allows you to build the Mechanized Infantry, a fast and versatile late world Unit that doesn't require any resources.
        Completing it would unlock: Stealth
      
      ## Policies
      - Dictatorship of the Proletariat (Level 2 Tenet of Ideology Order): Dictatorship of the Proletariat: +7 Food, Science, Gold, and Culture per city.
      - Five-Year Plan (Level 2 Tenet of Ideology Order): Five-Year Plan: +20% Production towards Buildings in all Cities. +3 Production for every Mine, Quarry, Lumber Mill, Oil Well, and Unique Improvement.
      - Nationalization (Level 2 Tenet of Ideology Order): Nationalization: Each Corporate Office counts as a Franchise. Foreign Franchises no longer benefit your Corporation, you can no longer construct Franchises in foreign Cities (except Vassals), and foreign Corporations can no longer set up Franchises in your Cities (except Masters). +2 Science from all Corporation Offices.
      - Great Leap Forward (Level 2 Tenet of Ideology Order): Great Leap Forward: Receive a free Technology. Spies gain +100% Science. +1 Science in Cities for every 3 non-Specialist Citizens.
      - Resettlement (Level 2 Tenet of Ideology Order): Resettlement: New Cities have +3 Population. All Cities gain +2 Citizens immediately. No Partisans from razing enemy Cities.
      - Peace, Land, Bread (Level 1 Tenet of Ideology Order): Peace, Land, Bread: -2 Unhappiness from Poverty and Growth increased by 20% in all Cities. Building maintenance reduced by 20%.
      - Communism (Level 1 Tenet of Ideology Order): Communism: Gold cost of investing in buildings reduced by 25%. +20% Production when building Wonders.
      - Hero of the People (Level 1 Tenet of Ideology Order): Hero of the People: Great Person rate increases by 25%. A Great Person of your choice appears near your Capital.
      - Cultural Revolution (Level 2 Tenet of Ideology Order): Cultural Revolution: +25% Tourism to civilizations with less Happiness. +1 Happiness from Factories.
      - Double Agents (Level 1 Tenet of Ideology Order): Double Agents: Receive 200 Spy Points. Gain 125 Science when you identify a foreign Spy, scaling with Era.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Trade Confederacy (Continuing Statecraft Branch):
        - * +25% Yields for International Trade Routes.
        - * Trade Routes to City-States generate +1 Influence per turn (with the target City-State) per each owned City-State Trade Route (up to +5).
      - Ceremony (Continuing Tradition Branch):
        - * +1 Happiness from National Wonders with Building requirements.
        - * +25% Production toward National Wonders with Building requirements.
        - * Royal Astrologer built in Capital (+3 Science, +1 Science to all Councils, Smokehouses, and Herbalists; 1 Scientist Slot).
      - Justice (Continuing Tradition Branch):
        - * +1 Production in every City.
        - * Cities with a garrison gain +25% Ranged Combat Strength.
        - * Royal Guardhouse built in Capital (+3 Production, +2 Defense, +50 Hit Points, +10% Military Supply from Population in all Cities, 1 Engineer Slot).
      - Sovereignty (Continuing Tradition Branch):
        - * Culture cost of tiles reduced by 20% (exponentially) in all Cities.
        - * Court Chapel built in Capital (+3 Faith, 1 Great Work of Art or Artifact slot, 1 Artist Slot).
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Free Trade (Continuing Industry Branch):
        - * Earn Great Merchants 50% faster.
        - * +5 Gold from International Trade Routes.
        - * -2 Unhappiness from Poverty in all Cities.
      - Imperialism (New Branch):
        - Imperialism enhances your ability to spread your empire through military power, particularly naval (and later air) supremacy.
        - Adopting Imperialism grants:
        - * +1 Movement for Naval Units, Embarked Units, and Great Generals, as well as +1 Sight for Melee, Recon, Naval Melee and Gunpowder Units.
        - * +10% Production toward Military Units, -10% Gold required for upgrades.
        - Each Imperialism policy unlocked grants:
        - * +5% Production for Military Units, -5% Gold required for upgrades.
        - Adopting all policies in Imperialism grants:
        - * Unlocks building the Pentagon.
        - * All Naval and Air units gain the Banzai! Promotion (become stronger as they take damage).
        - * Allows for the purchase of Great Admirals with Faith starting in the Industrial Era.
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
      - Authority (New Branch):
        - Authority will greatly benefit warlike and expansionist civilizations.
        - Adopting Authority grants:
        - * +25% combat bonus VS Barbarians and receive announcements when Barbarian Camps spawn in revealed territory.
        - * Receive 25 Culture when you clear Barbarian Camps, scaling with Era.
        - * Receive Science and Culture when you kill a Unit equal to 50% of its Strength.
        - * +1 Production in every City.
        - Each Authority policy unlocked grants:
        - * Receive Science and Culture when you kill a Unit equal to 10% of its Strength.
        - Adopting all policies in Authority grants:
        - * Unlocks building Alhambra.
        - * Allows the purchasing of Free Companies, Foreign Legions, and Mercenaries as their prerequisite technologies are researched.
        - * Allows for the purchase of Great Generals with Faith starting in the Industrial Era.
  - decisions:
    - #0:
      - toolName: set-relationship
      - args:
        - TargetID: 6
        - Private: -50
        - Rationale: Polynesia (Opponent 6) is at war with us, and their capital Honolulu is at 12% health, while Nuku Hiva is also vulnerable. We must set our relationship to hostile (-50/-50) to ensure our tactical AI focuses on capturing these high-value cities and doesn't accept a premature peace treaty. Capturing Honolulu gives us invaluable wonders and consolidated territory before our peace treaty with Austria expires in 15 turns.
        - Public: -50
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Our next policy is in 15 turns. Choosing Great Leap Forward as our next policy will grant us a free late-game technology (which can instantly complete Advanced Ballistics or another key military tech) and double our science from our 8 active spies. This is far superior to the minor yield boosts of Dictatorship of the Proletariat, helping us build modern defenses and nuclear deterrents much faster.
        - Policy: Great Leap Forward
    - #2:
      - toolName: set-research
      - args:
        - Technology: Advanced Ballistics
        - Rationale: Radar completes next turn. Advanced Ballistics remains our absolute priority to unlock Nuclear Missiles. We have 4 Uranium, and nuclear capability is our only viable deterrent and defensive option against Austria's massive 5x military advantage once our peace treaty with them expires in 15 turns.
    - #3:
      - toolName: set-flavors
      - args:
        - Flavors:
          - CityDefense: 100
          - Offense: 50
          - Production: 90
          - Spaceship: 80
          - UseNuke: 95
          - Defense: 100
          - Mobilization: 100
          - Growth: 60
          - Air: 100
          - Espionage: 100
          - Culture: 95
          - Science: 100
          - Antiair: 100
          - Nuke: 100
          - Ranged: 95
        - GrandStrategy: Culture
      - rationale: Conquering Polynesia's capital Honolulu (12% health) and Nuku Hiva is our immediate objective to consolidate our borders and gain powerful wonders. To achieve this, we increase Offense to 50. However, we keep Defense, Mobilization, and Antiair at 100 to prepare for the inevitable Austrian invasion in 15 turns. We also increase Spaceship to 80 as a highly viable backup victory path, given our strong science and competitive technology level.
  - tokens:
    - inputTokens: 51865
    - reasoningTokens: 8970
    - outputTokens: 466
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Our Position**
            
            My focus is on evaluating our current standing for a Cultural Victory. I'm reviewing our influence with other civs and the overall strategic landscape as we progress through the game.
            
            **Analyzing Cultural Influence**
            
            My analysis confirms we're influential with Polynesia, Russia, and dominant over Korea. I'm now calculating the remaining influence needed with Babylon and Austria to secure victory.
            
            **Calculating Victory Conditions**
            
            I'm re-evaluating the number of civilizations required for victory. With two civs eliminated, I'm determining if we need influence over five or the remaining six. I'm also assessing Austria's high culture output and its impact on our progress towards influencing them.
            
            **Revising Victory Threshold**
            
            I've confirmed we must influence all five surviving civilizations. Given Austria's immense culture and their current diplomatic near-win, I'm prioritizing finding ways to reduce our influence targets or secure an alternative victory path before their World Congress vote.
            
            **Prioritizing Diplomatic Defense**
            
            I'm now intensely focused on Austria's imminent diplomatic victory, which they could achieve in just nine turns. I'm analyzing the World Congress proposals, especially "World Ideology: Freedom" and "Decolonization," to strategize counter-moves. Austria's current position with multiple capitals and strong influence is a critical threat.
            
            **Disrupting Diplomatic Gains**
            
            I'm exploring the impact of the "Decolonization" World Congress proposal. If passed, it would significantly reduce Austria's influence with several city-states, potentially crippling their diplomatic leverage. I'm now assessing the remaining votes to determine our ability to support this crucial resolution.
            
            **Securing Atomic Capability**
            
            I'm prioritizing research into Advanced Ballistics to unlock Nuclear Missiles for deterrence against Austria's military might. With four Uranium resources and confirmation that we can indeed build Atomic Bombs and Nuclear Missiles, I'm now verifying the prerequisites and global status of the Manhattan Project.
            
            **Developing Atomic Deterrence**
            
            I'm now verifying if we can even build the Manhattan Project, as it's not in our wonders list, and shifting focus to military production. I’m analyzing policies to maximize production, particularly considering the significant bonuses from Five-Year Plan with our numerous improvements.
            
            **Evaluating Policy Options**
            
            I am now assessing the impact of the "Great Leap Forward" policy. The immediate technology boost and enhanced spy science are incredibly valuable for accelerating our progress, especially with eight spies. This could significantly cut down research time.
            
            **Analyzing Cultural Viability**
            
            My latest assessment reveals that a pure Cultural Victory against Austria is highly improbable given their immense culture output and our current tourism levels. We are losing ground rapidly, making this path exceptionally difficult unless Austria's culture is drastically reduced or a military solution is pursued.
            
            **Securing Diplomatic Buffer**
            
            I've discovered a crucial 15-turn peace treaty with Austria, providing vital preparation time. I'm now prioritizing research, with "Great Leap Forward" as the next policy, to leverage its free technology and enhanced spy science capabilities.
            
            **Accelerating Strategic Options**
            
            I'm now analyzing policy choices, favoring "Great Leap Forward" for its tech boost and spy enhancement, crucial for expediting nuclear capabilities. I've also identified a critical ongoing war with Polynesia, which requires immediate attention, as diplomatic resolutions previously assumed peace.
            
            **Addressing Ongoing Conflict**
            
            I am now focused on the active conflict with Polynesia, realizing our assumed peace treaty was incorrect due to sanctions. Their actions have led to significant unit losses on our side. I'm assessing control in key tactical zones and strategizing immediate responses.
            
            **Capturing Critical Cities**
            
            I'm now focused on securing Honolulu and Nuku Hiva from Polynesia. Capturing these cities would provide significant strategic advantages, including valuable wonders and a buffer against Austria's dominance, accelerating our path to victory.
            
            **Conquering Key Territories**
            
            I'm now prioritizing capturing Honolulu and Nuku Hiva from Polynesia. This offensive action will bolster our city count, science, and culture, providing a vital buffer against Austria while accelerating our progress.
            
            **Consolidating Territorial Gains**
            
            I'm now consolidating our gains by securing Honolulu and Nuku Hiva. Their proximity to our existing cities makes this a critical move to create a contiguous empire and push Polynesia out of our immediate sphere, all while Austria's significant military strength looms nearby in occupied Korean territory.
            
            **Preparing for War**
            
            I am now intensely focused on Austria's looming threat. Their significant military presence near our cities means I must quickly conclude our conflict with Polynesia, bolster our defenses, and research nuclear capabilities to deter or counter their inevitable attack once our peace treaty expires.
            
            **Adjusting Diplomatic Stance**
            
            I'm re-evaluating our current diplomatic standings, specifically noting the war with Polynesia. I've adjusted our relationship to -50 public and -50 private to facilitate aggressive territorial gains in Honolulu and Nuku Hiva before peace can be considered.
            
            **Analyzing Diplomatic Leverage**
            
            I'm now assessing Austria's diplomatic sway, noting their control over Korea and open borders. This allows them to project military power directly towards us. I'm prioritizing maintaining a hostile stance to prevent any unfavorable agreements and to keep our defenses optimized against this threat.
            
            **Adjusting Tactical Priorities**
            
            I'm now fine-tuning tactical AI settings, increasing "Offense" to 50 to ensure aggressive capture of key Polynesian cities before the Austrian peace treaty ends. I'm simultaneously prioritizing anti-air defense due to Austrian bombers and evaluating a potential shift to a Science Victory, given our strong research capabilities despite Austria's dominance.
            
            **Prioritizing Policy and Research**
            
            I'm now focusing on implementing the "Great Leap Forward" policy for its technological and spy science boosts, and prioritizing research into "Advanced Ballistics." My analysis suggests a Science Victory is a viable fallback, so I'm increasing spaceship flavor to ensure prompt construction of components.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: TWkisdrABiX8kuHf
          - toolName: set-relationship
          - input:
            - TargetID: 6
            - Private: -50
            - Rationale: Polynesia (Opponent 6) is at war with us, and their capital Honolulu is at 12% health, while Nuku Hiva is also vulnerable. We must set our relationship to hostile (-50/-50) to ensure our tactical AI focuses on capturing these high-value cities and doesn't accept a premature peace treaty. Capturing Honolulu gives us invaluable wonders and consolidated territory before our peace treaty with Austria expires in 15 turns.
            - Public: -50
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1/2wdjMtSLxDc3kFJ2srbKWmwTRLCN/BShc/sWhVRUVChy2IGGLUalLf5gplZTeNcc5OggXXGkFHIQ9dhxbjYz+rASyXY6h+WexL2E2VaMshOq4dcA5Br9aYzD3MXfF/z/9X/Z4O98UpnbGHFHWxVt8IEJtuL+5D7s5cvsBEJmJ/pyIGkYRAuIA/hww5dwEKtgjKTsq1iZibMqWxvtthmA60rEgBC1mRUhsiNMLt7BykV26W//36o0SSOJ+WwaqgT52RVJ0QNq19T6nM8qDsgXJxhQAJ9hY1VH0stit4Yker0KSp8jw5yBkzefxcskvVgqHfc75Nw9a87IyhBxE9dRdj1F+EzhCvc/6C5A9D0Ns1GCvNg7BDODa8YG4MVx0h1ngmnDIW4q/irgSMdLKmEhAfqlTJFSLq6+QG2JK3E0By6dbpL3EPMlebYZq6OikJ8wudLnfekhAdqG1eff82BY6ZiGw2U0nzpyEqnmbSmjMCWCuKkh1TsRaI8M89phOSNMngaiwGasqksFudmN8z3Zee6e9GI6prmmhajJqRBh75MFqnTbPZDWVwmFjwY0eRqczlEiUzsK6H6vFpq+ynTLH90/GvF1MzEQvj81OwttSUNqsALiOwjP5XcngpgNoGJ81CGt3vyrGRu3MhZTlJM0lfi8pD78bkoU3zSSyqpTYf1Khp01TjuJDSVRagdw9NZznJzTYIEFTWEiyeiIBnFNo6pDW7UbcUQnK5O9Q5pufwd5NGZK8nLww0DI4m9uA62BtYI2bu2jxvlc+8g8tL4APObWwt9YBdIUboyzmy849ALt3IXovEQEtIKIh5Cx01KdqQz1GY4i80xWW7mRGO+GCOnl/6kRDbcp0JODpmWXomQ9WpMxKUHj+mqg5otid2hecOT9ujrmNJHY4QhPVRR5TuoHHltG/5A3MLK50agpummUjO+vkRvbW+1CjjHUZ4EFFk6OTFo5BftNIY4p2esynWsEf8o2Hu9h59vZwVXzGcoBDKvnx+WRTRXrKp1RYOLVVyx8kOHdJQA/VpFMHSH7Lx/ZOGyvBaoP0GmgFxbui34796NWrg/AN5EdVaf7MYiTLcLlE9gcYGHAygameLxi2Bv//lPtI2mW/L6cfVgoLcsVFpSvusWySH8Re0o6Ek3lcKFsuEF87Rqk20N68LxQGQh7JbeNVz7LUVpc2DoVb++L5lI3SbL8sbDzZKVSweE1TEDs7beunpqZ8TeSpmAOfoMrMEKDlQTyyMs+6BjT1E8Bu/Ok2fbK5M3vaTkshvSTYRy6UFhJ62FbHOU/RkptRN1jJwFp+p7r7nMGc2dHn8jXr233CcEo0McyGWkzyy2QdJL3lMurrd0aP8wV8XnHSwehcBgcoAbbJqqch9RpxeXbISH2L9o75U5S3y/6+b9k2IkHzVLtK/ZcF+xqIvxea6qXSIElGQPluXptLCiP8UWpdyFxKIm287QjNc4YA+Y85OTMVbSi8DNqYedrYRXSVp12rOIoD6UjC5JJesOs1ou7E4o0YkHqRfBl7nlAZ9IY2PBTsnHAG0Kcy86hXE5mZYMLeQTNGrEXuqDJh1/Vg1/Vm4ogiiSpK2RhwIwCvEGPGGmX6vikhwEaDeiKzm2X/a1cQJOiJqVX0LIq4eepzKGlKQ/lTcfYZ0VuFVCjEqhu9yeJGgVYcGrerfE1YsRRJO3Hc6lPZQftEHRv86/JGzKycAYvRCOVRZlx5RJNfSjW4x7i6JcITU2py8IOJroYQ0/L6p02X5br0ZmrJpB3yfA6J+8LSNVWBb7N9nLvjqFXUMikjl+gntMCK+PuSDlJMy1Eva7O+twxHMzX7Jg2h1AhOmrhNC72CaPohIAX0F7N4knC3s81gPRvkfjAbb8AJzNWALDHlT9sVusOH/R17TTQxTJ+fgNAglCMQTIZQJ5ARiImto9rDrsI3ez8iIj+TtG2LsqT+j7jIBgsoVWyWqfnamjzVkFAqtRIVh1sJlOoG72IEXCOX2TtVyUeuWMd+QrJmm3QhTshfe6IKw2PypGse/qz7uoKkSagR8N0B/n9mwChbvWoEit9DfGGkLDeLg+tNnr6dZ16CZN7KN22jhmu5xdEE/WYacmX3m13XbuLBs88wx5Ukq8pw5USQQIbENI0W/8+qcpNMLYj0H7V6AUnMaXRb8xBCloUybZqiAR9JYzxHmua0UBFa5HswqIOYBmov/D/DV5N+hTBAJ+cx7Lr94t5+v5tb2TEo6rxFZ8bjuURPMyPecORids83lLjfzELen4pEm7skEr9IKKasW0OUg0hqHQaFCIEXOYBHEwIYP6pGTCe0ZQsiIEKh22Js+LZqzY9qIhwZRN90Z/OfceT7dYe3W9H+kay0YeOQhcCpLf+2G4v8qRHDwm3OdBcMPSTd5PUa0I6dimXb0E3cMct/0A/vGECzUIAIj7sVs80eP9Q2OMAZu0E+eBuoMnBECmMDa88PwTWI+PNkgLMOIyniDxDY6aYmJ+JoE1NygxGBH7+wZ1hssN77b0J0VCYp/4yTZG1A6/iM+KR3tkG4UI2tdjeWoO1EJUFZK3ELRPjXH3ho+rMxoYe60mO8a1iy/Yu56GAGFR66LbjJWgRPT57Lm/0BdU9A5E7D4b1aAwxC1oUPG3TYqW6Kc6/D/Ah1s2eDkPBha6Q2E3hy578wpho1BPXggFdLIfFscD2NNG1NPlmnwkKrzFIXOxcYplZl2+mYKSEJny0/T+cYEIlQlqYapVaDnq+3OHCSKpAzLHAF1o+NN0UQQ1V83au4dqwnPlHj8+5XHkfMT55mhyAKS4rLsi98+TjZXc3yhcHAx1sILt1bYXypQgTn69Bjo4c5pBJNKltqpxJMyKX+Mlr0WHP+ok8/i48p9jnbRoayneGtxVa0Vc2vHknvogYPovcNipKenWnTINAr4yn3m2vIc+MprGZ2sS2O9l0pNAtVJe81ndBlTIuZF21n+OcNajvsY6w3I4PSwRe6std0xrsPxl+RNmiHIDzLppFm181nCBBLQCEsseunWee6SwgPgYOyGWg+rYJ6CuAX0NycDAMQ5HIPAxu+KkK0Jh3Q0OCWjDXmQfy+++oNp0xoMPuUIFSs5JqW/JPlFsrT18XUqs4WBHalJAJjlmej9sNP82mJ2LJBlCaXt5XfWLvKkpZ5fz6daGBcyW3oiNQ29HU5ZQSuFshcYp9FRMW+GFb2wxEDiBwhoRc5ZZTQ0aQjEofPmCkWD8uznvLxL6oXYaFg4O+xpCD4JWqipptaba17FxD3PeyXoncNGFV9sbv0fkCCYnnk7qrUBZ9DspK/kuaozDzM0tnkm082f1QWYCN9ptKJVUz/eqxspbJTpS5eX0fC20YAAQL34DV7jjU/4CialvB2LmOMOz+yJMDnhWaf+qQs0FpFemS9YpIXd+r/ozG9UsfI6AGm1aJNsx1nHzzAmXdo43ebdnSTkjISy32MrydV7Tucl/K7isEYLqAEoJOaH5l6VnoBi4C0uQFxvNsAxyIT9oXD8JzaM70HYHxNkfEpfRIbI1FLgPzdJkEWqjfXUaO7xKYlUq30pwsjaDtyeNyN4mDN3wUCNLzYuvpwxi268KzknTLsxuBtJiCZtxWCvxQidqvhavjqTSbUH1Jom7Ae5CC4XOM9mniN11BdiiNWDzA+2bWhEOrbOruqbeeeHWfOFCDgSsAY+2ZA1hAykx3nDVc0ms+O2LkhbreI/y3hR6tUSRW921AVDr9G8+Z8P5OXQFPu7urMZFhOLEGL2Zarv1jZuw51AXgZGYwRe6FpyBvHgA6B8NhOag3NrxqcTF2O3Z6rvwnAIgbgjYralqzLXNvTlVFWb77ME3X28RV+RunfLjAlcdppurvEXXLZ3q6bTbRuJo0OA3ZCX7BV/CMyj4X+Z8d3DqKUCuQW0ViiRoSH9HvK7g74d9bQYG1N89ABRAAoBuwMrtD0p77drT1DaWd4QGKRmP0kHI6lnJh2BMkGpNEE+W770mQIMKvZa7enEagp9BO1N2t43RIQRmMiywxufDXt8hSP22W/yyfR3FHbURX9dKvCDK1qBpEs3hk//DopKbhg/XJ/2m0yplSObEBZUEinqvNu43ZBGyKSUXPKjPvmuX4j8wlAtO3FBzfBXjsVRQyuO0bnDegA6rLnlW6KKGKutGH65e5I1AZcWgCeeS0NNXg5H8EbWzZihsD+6Sdq/iA5ChZm4OC4SOjQmjD1jHnPybth6D0AC/ZG8M7meF9ORtx6GpVqkCT578uSdEBwVFWWcl+eYvsYYWzLrRoj5pW7lPDbsgUMWnj2ml4ijo7w4SiFaAEIpJTxew+qE5Vf6YTUqYTR+QUY8RVwj3U/I7o86tLKh9/EZSspsYS6AM1YpU2O110D2fsurEpUZl2jPmrkRLWiJucyebKOhoJ98JhY8SkLXoB1Nbc81vNu4sViMDSZrunuy2wS6RDY6Js1yOMH2mmcFwfsQF4W07d079u3nUDdy/h2/2NQ3W9evOLTdzDjY0Bnq1BBUWXuRDnMy4n804XKFXiggEb6s1t2x/eM8GRtk0qd337qqsMjk6NyCyRCatzGTORbsMyFbavwIqwwROvWhPc/1OWsTGCocmZeJMKphXReEbzGI+vf5EmbgWyuAeghUEcRX72QvS+VQxi21NPFzyYgZMvrsUwe7wF4kgg9p2gYcZCEz0dpoOEjxOOQ5msYJSndoC7U2k9uvB7ogAuUTWs8x18VXvk/Jp7CxJRSSn0Tdl8saVHo5scGy1tXlwm7MbJtRF/7nWkuAqYODD7Na44eC1c8xPuftoHaZoc/kW+02XnOszCo9yjpxCRI8mwmdh5ffZB2C4XlA9lHjRv6rA9dj7qm5rfmow0hOrb4LrlCqfDVJsUiDNRq6pjx+SGX+hHYSi1Z/J6AGo2rllpi6lkD7WZWrbxPPE3UaGEpmiUxCNDXXP2KI6/3T3N5lenSXu1rGVECdEtQcqZyp3QdVnGxCBJXJiEY8ThUzWEshXLyLxQ13k0cBx4aelQFBWq4z+rwNyHbLNoIWv2OD6lP19blSxNsoQfLFf+eknYC10NiKFRyI3LBeE9LhidU9N7Oe56/NI23/c3/n5rx9liD/1IvBV3satONsP4H/yaMCSsE+vsfc7UMW6kmW2wviTLrDNgyqnF/gr1tJORyRC86AFgYQi/h4BglNsHWpe66E+7gNVDu67oWB9TKzMrdDnbzSiibMQxHhDuzna+b6N3xe//23xBhwYMJwWQaXSMZDdbJGi9yyhoxK6oetxPnNLZ3RpeY+X5hXe5e2RRhW8KwvDeJJ+sHxvKvxScBLTCG/iCZbXZyArim3mYvTiP8llrPQ+oGnR3ckBohsHIdQcA0F6R8PeAbMiLQJzTtR6zsgEk7WHiLqe1qIZC1hq6vHZDS6pHGNqgJAvwF8cDyRBzc+RGG7VOdxSf3ciLErZw0GYsskuAqpllSLXB1Kr4yLjcgp3msWxlveh6xMNJXfCHycsrh3bW5cJzLjl/jEsCjrJZIK95FiWI6uuAWMlghykrKApZEDNI0Hd5+WzYbusm3wDNhAkipg1JwaHwdiw63C4+O4SNkE8G+kyzD2Qke2WDtNsLopOAZiXoAtcfOjCmmPHDHoz8sIjkJlW/jyqWn4LMx8FyPGq17J3BCC+X+A9QcUkzqFq4/KE3nJ+9h2oxPa35ZJAQ4LOr2TfeTCSYXLFwbaak8KitxJVJDUsUDhI4p7lS5nQy8eOhQ9oetyvtwkv363IDTTIcZa682gh6TTWjujKZV0cME8gOVQe74MH/97LYz2Frin+sWhGPs/GKKE9ntuPqVt7Ezi+0CfTcN5y6C9g0rk47rQFtXT31za+i/Ri4tmy/NycfJt+104ysQWLUPy4MVF67fEilHoHG3UwXN+nAu+66FrmmRQlp8Bv6okE1ZvQi8u8gycFib0TKINPqoYoGr+r0DF2lifW5M3miS+XxgjVtqTTevIm0904/GzRz/dtRk2tUbycsoBy7ibz46mSOte0maeOGTDvAg59DEEvY1oDhkfXS5SeJX5seJkM6Lo0Xa3s/gUKuzCzaRh6IjwU1MznBQbmpjU7Nh/Avl1KhixIHfCciUp5u6kz41R+dHCTAHBJ2HU5bb8amsWJAOJRvz0Ls82AoI0fvs4xBEj4a40FS9VK3mL5q3fqbkGlmBBCobWe8f+UU0JxkNUlARAdZ9aE3zpVawF7UT+n7iML1yoVsdlfL6CcRbW5TwBgx6ZoNpfwT60dGUtKxUWcwkdWKda61y3DCjW4d2YCgX1UQJraj0vuqjNzjCFxkr5bJoox2Qi439U6lKGDLcRiT47FihOcsmB+CR5USXDq5HkDkZCmJZr1As0Slp1BfbtPMSgI4e7DmZbBRgMMoc6ae5QfsqD22gpShdnpk1FTknSvCLAQ/Yx7piv+aYjStSbZ1mbVFufaLLi14gls+KVlbm8LF86iOsXMHt+2IAGCdssMHGCJ2XXJEp8g3BiCt6LecVUXgmQqTI7JM57RxssfZE1Gmt3596zY4HlJzqw7rhmkg3v6RXy7aeCLlomPTcp+O3LYvnV9IJG9rbZ/PK6hC6CTvuuvzQzSN0nwqxOd9JEt/TYpiUWdH/jvkGoh4ejtpkZ61XExe83H3m8g0CE89LzXdZ/D6ErRPF3oTZYpz+hxZQ6tGLNOB5PkAMgfKf0CAkM9hP0IsKLj1QDDjbG1QIN+rUmB2qYvdU/2iAXPrZuRBtzIGNWi3FXsdqHUhBcg+quiTaf/t+aUDZhkeRuHTiESt9bxaH8o3AAaCNDZgtR6JGyk0Obz97a/xr95/rsYc5mNZ9fj0OPBWe1owHSj9PKM/Frawv8+pfxtc+v8aXz5a5LIaZfs4p0yK5LFcv4TPdXxQBAqkptsEvLBlJpqHq7B8xmsFvQoHVrooYyJaJwh1A/kNk9zUOgZm+9ZPY68oX9xQfm9jy8e4X4DJlEzRhs0pIV08xzvf8OHh6M217LIGh9TebctqlMyJeWjo9eFbop0DPmvG9soFgTm1geQzY9c4/86uINt39aEGslKh366e7iuSK4VtXNbjBJ56Yc3lDazUVpJ0/ceE2CnDT6uQySTa1ZAPqhokp27uHCjwSDa9B67GIKaHVkOUaUmDoGfvJc9l3R3YUmh4cRKEfIdTpVnpFTvsiaFUvTnFLhFwTAt9ZYmPRgiaG7CkYdO9SLHdiQCdobo0YNN1CVdzliBQScmkm/T3sPhhMlyUv8qIuq+r5IxHjuwV5BTQfyxEsDxeA5yJs8Tm5nq05z8AyCTcRrMSIkxldaFldiRqV+CF79URCk4sm2B4+nzPbC6/PVHMv9U6suNke4W7H00xx3z0pwJcHXTW7Vy0d9gfdwStqwR8sCHe4r/Tu6gfTfNTuDeu7EgQJKMQk5kCWGGKSooI6obJQppa1h3ZL3/PNAq2EPivqqZGi6Nhyd/07YkHDEDS/5xmYpy5SmQXSdeP5bpv3HU1NS41cM/+eR6ICym9cHQTr9RUAjtd1fnI+255KAEFpYx7s7xQROF6meCgKfyiJcgF+VPaDuPK3C4/xGTbW6nJNWVOK/J9Yii0Swt1DRxErmXOhAK1UjDGA1aOyrVHpIQL/65zzc6ccMy0ZxmlZ1YocMeET4Y1rA9ypZXWRFn5g5TmxOxkwWBMY4FBYVGaBcVe6SlDTwhh+8rFTsPo2OuE3o1G3a2rUUwufNiXNcweOgcrqfqpXjbGGkPoXh2LFY6PbuJ2JHip6Ih0r7PR+dtiOiJjYW+82kn61EVwk5MN9RDzv+ja9IDlNm9wJfM+0Hz64+Bua/OdsK89YNch5mjsJA+Fuexnh6iMAddFJeezQBE6wIjdEha+thtbEn0kyGVKnoRzv65+nKLUjWfP5Pos/FbdezvVOLXZtuT1I6eJReUeh+ziyP9atzD1sr405V5uAmdGpl+Zl/reOFLvvDDoQtZ1awFkJ3S0r/Nx5AjWGaKLZiBYv3Iz3Oz8u62uL2i2o9xdopSj85Dxb4a0X1QxW8WUhGwuN/NRtsDHL0zoYFkkdSpD2PLQCDw8oHSGEbk0vYVzK7ncMqmybQZFc6d1FuYr/eCO76vCUEsvUNHUVPDh32pGqWaYdiNgCHTf1oUzxTUb0S8OhV/NHxd3Np6zTYoaHXA0b9FXT/VQr3TbBtIZkW5AQXWsDTweeaE+On8TFecsL21xrL+3/j8TqPj88yi5iL8d+OyrWHZwi0u5DlezEsMoV6n/1Up0l53PS3PS+upA6WKWi9RMEJCp34XJZg7ZfHPP3dRkPAJguC6BpnbuPHVPR8hEioB7n5I4uJDJRD0r9KWxlxaSuTxGvo7nWcl/doXMo2i6uQ+c0v/p3iCLMwUqOZT7SleBERDEJ+/s4gNvVz3ffg4jf9MkG7vB6DJWyAHvIviu3vDmoK9tVba+sfrlS9mdK0kmq8utivXFWecS5n5T+w07wKzznr7PqVNqEcYYuCXrs1i73M/MAoXzXLf3j1yj5HRBkccDHVixPz7UgOGUrYLs+4t8BOSzBlKHi31EA5PA5Y9DitFh6tlDkT1aJKr74CHgIWh0Y45f5uwOoUN0hQEtdh8wF4LiLI+/w9hSLjjnr8PrQwwbJwht2NeNycm913Kf5qmAk8sO8UdWmfAzoBNw/XOTQFE/8hSBcjVGuQHQpwDjF9H3TqwDJ1QeCk0u9vOi2oiepJWWlfwh4IfTVx/QfRVs60LfAQTWriImHU+b41I27TbmXnzZJc+BsBIKlIgUPOYEtATP7QI+svYwnJ5Sf7vJYHiLSbouU+ldcvyq8Wf81VNDdr6OM8Okwp0DPd20uLCJ8wJzdJm/xesLzwFf1ByeE2tmRJjLzrJz8DUDp9uxebeU0TS+1sOVICSDaISZk91aTyV/Hjcszretr3HzY2xXI6nD+YdKUA93Wl9k7R+Jna93OfcZKlyUPDAsh7ILWQSi7EUIEoMtx7ewXyDoqXI96/n6jBgyB06x/KEaPb1fZCbgO257eBwGaKG6BIatrK60GZKiser/bI3yIoLxy/YZjHqljwzZqkidr1SZAmIQJ2Nw8MFw6kBqiXyMsXRPb4KhYEwzHQ7htI2AKYr1zYUffGZxSBFmZFdtLSbzTpTQjsLRJWNJtrBW5E1g410KlpxzF7LgE0VUALVoZ6nOEvx90bSeyV8xsl1Bgp/vn1JlwZdotHt3lLJV8y2efhq9ia1i79xhA6SrtdHhMCgx0gRAL8VcR8M9FkhELz/t/fgXcdmiqBVbiODYrX4/PexW/qJXYqj8RRvCnD2OzZX6Rxgfguz/IiaIWkrwHp29A/uGGQrPHipko8fW6ONE38gZvsB+sqwVVRBnRHRrmtmxaGCmq2Cs1t8PXg09ZQC6yc5aHHz5myV6pX9eTzp2aLdz1pJ9sWkpntlJvb8kUMjNtq63Wo77Yb0dKcWRQMCMgtMobWU4/IEx+cFD7zhG7olSTIRqyqeE0Kxp+/jiEujsn9WwFEvNSK/XhPqOxOzHrM8YsPQ/N43hn23Y5OCjbj4kt9rULlL/hHeixb8zOaAhZ6U70UJp5DIH/g8CNtLBRQo8XNSppG6RFXyyYHMnqHobbbB9nfPXiHLjJpFBJZkEYjZeUWz+24K3mYmiut62SamJgW/wSPm0Gc4gbJjgOChGq4P5kwddJngq+vY6WXur4CCodm5xFFhzjS9m3h1XxArVwhVApVSrTWs3qqVu7oms8meRvuapd74h0IWYnknUZb8EHfblaHJrQivmHO2UHKVe/1+JOWm/1RiI/mYhIlM+8yG6IfZ2zzV3YDmDZiQb6piDeqCf7SjpB7lHkhDcHnxJ1mpcLQvMbreSNrGvF774DjPsBYCU05WEGaWwukheEastY/e91s68JWtc9H+vJTiKW1CxGUifRhXOMa+/6eabQBxYPKNdJImk5z5PrTj+pt1WVBh8B9qTGlHvmcKJK53jzBVFpWKRRPALcj3Y+PV+VUQcdeeXY0XWlGws/RvpWAl4hm2uvK4sfrnD1yRjueOXS6zkr9Nq5cPHKMlM4bie2Eys//uMiMXBE7uzBp1KGSPTBc7SYmgDzfQmsX4Wi3eFHl+mDyuuUAOYKoaUJqnVyYRS8VR8EdTTbt5R47wHuhTUNNYucXbioSHQ2/3LxxgkJp+OyBpVugjK5TzLY9b78K9Uw+/hkGKLAgqBHD51XZK6tPhX7DbUgIxunuQ/4gq51rykteCZThOuYkOgpyO3Ef8GitmTvEktrYbefSxoWrQ8y+m2osbs7R0uFyOrhjfXJyQAhnhleLkmzth+nZx4IYb8hlSv32fm80H1YkFSvystdwzIMEkkHw3g9Hx/GM+7JnyTPvc0geklFiEzjN/9yICfsMwY31PJtlkikNvEmqSy8lwCJL5NHYo+Ukwf7B1X+6DttC+tOFaeFBERG2zwsq2p9I8KhQn0MzMVroOiMZcOacdmYWIjsLgsVCw3oro/gJOPO+1pU0ddeyYTwojDAApPHmicbELET4weqAyZ0Cld0ShDk+Pmpb8v9Hij4yHaq1U9NUkQJDJUw5kK8mlR9ZM8W7yDY6kgvM9t/gjKwmvt53JPkKaT6SWNwCPgY6Q+q2bki0BD/3JtseOE9Hgk/7hsB94OSwFztkPIV2bLECZRGDaoaI685kinnZo5ndto2uFoLyXQvMOxoEfE18QwishxgGM4AmDnV4Lh6CVcElqCZMw+TF99bsmTnV4ZRDk71mXB+C8SEdR0rV3qZR1y8Ec9OMD6P4gJgn6VIzmy8Hs4iiXfS3wCYs0aWf9yCPOmEyYIJZsj52nUwBX0jf8dV528h0JixOalfsXA1t39lUuzLB2GgVtAxcyhLl1B6uuk9c8yU2ykdrOGNLEPMVuIIpDgCHdFVpjcWs331AF8LVKY4wyFTZhfnbdPezPoDNsYb+kdU81ZqhRIVUukgVP5OnnpWhb2uGxIVwIl8v3RH2BARMPcpQWfB5gA/1y9RSrvdUfEmPybwzE/afq1KNVtOZTFS+J2T0Cs40ArR1EXs5h7UN9Hml5QnCYolvu6Qa+9fgp5xRzz3CBbZokBdx56BR9nT9xXkorZ4/nUvoRgqc+u75OJN+1k3E6AC8y/SJ9M6OoOnmkR6/3cXI6x5AwbRizQMfSEdwqM4GgihqQanrsqZ0rTSA+OQLTD/pV1Hciqz/TjXAsb+x/a+gPni6h5RDbi2rAoYAolULlXO0AVDjG/wNwxlnJQrWegzMHlxK0F9gSX9Ds6DD2hVTmTH7Z1yEQ8NzfF0Qc4d8z56Azzy7oMhIv82HtRswr7DyGLU05ZN+d2C/27d5t/CQutitWBXLJ0f8BEgbd/iCk3iF49I9Er6cw5sT2Em+S+lgWGqg70mVwwfBKDZIR7J9mupjKiKQ9McYuGclk9940VYLlR6L0KijC7aO5wC4GJRbLzKIBfQ5W+fwM/SVMW4PCgh/xLTAQkIfXjZv49bVx8SNr2ewesPjEW6o+BfvU1KuNCdex/iM7saiFcUe3vhB5BaAjtmiiDZRqdy3Mui3V6C34JdGQtxAqQZvb7M5h38HgG7c8eITk/ClFm/QJM+C9e26S5DMFSui5tck+mmdAmBD2RPoFjNAHlFg1x0g3nenMQZuvoWJL/5LLZ0YHJvm66biewbYMk1CjkJIyg3cH1yMxaQ9MkDZaQOpxonJvJ6Cj1wxGdZgPGGgaU3Q94oFHBO3wpe1QDPbOmzRSn3X+r7pPbmgI3wOquII5Ic0x8xIxSEtYcH+XGoRw2G1H8uv1NXAC7W2ka0RfDbLmN9xwJ+8nUM+YIrqzsh9HOwTmOiX7lm079IYyvwSvo1Emm3rfgHplRusjFM2SAwh719h+8cOyUZscA7yaoN1dLhiwSXBTu9/Q+vkpcghTIhNg5Gx7wfl4onLzUmo1KEzYw3jADAW/Dqw7UCxjL05PMOeIzhW6GcQ/Gerx+BKiCti333SLN2g82mxX2Ck3Hbm+HMiaTSnwTUcJFu3rGuJ2jZPGq3mkhL8Fyrme0Prz7y0BsDpG1Akd06iw9+QTwtYVA0wp7jkNRp6JEBRL2jp9oyJsVZzKM3meOdpK1Czvka0yoR0PXn51CFmzPgleJFRtiO3Mc5/zvwW4TegCGXzmMgD4eSAEewufeEC87MRFxrYQu1zv3ej1SZwXgw0A6/AXHXMP+XaVT0dLs/MBIlTGsKy6vpZ5z5tfSAs32lXhtgSY4r/dcVF9pyhUd4lYhBrmckHUxo+v1g260l2aPyE7oZb/ZLctDXcaU/kHCR7tuMB1pIaPZ+tJHwk4zAlRQgrYT+Q6lH52AnXRxY4Fu6raam/NBA4X6vPkh9JSsxHOKSpTXCtrnccwvIhu8km67NvXclZCBrqFxERSmJHbJnGzgTJQ4i/CcDOqxXFsKxGQAEqiTHx/TE7nymUQAFz7QaW2TOFfxMHiP3NAz3mB0grDRzmxyzxtv2VOyJ1yL1NPY2cn3wwX818m49kEOgf6JBeBEBiAORolfQlk6xQr1cgLEsj8EIaMkv3px4w0JsHdPVnYhhFwk0tHWcRTRjQn5jSiznog5+9BMqZVguNaILcU6j8TOaWRYdpsYgr8j+C8LDcyeSSFah1KFgLW2iy58+aThvK1bmYzLpVB8B8Vx/bCObGlJtvvKmHUNxQZ+LZ/FS3HVXCXeZI0ud4fwvnUouvdSXAWdBeraeLH45OVTptb6cwOZ26jt+fQqTXgU/0JgxdzBznUfbGuQxn3iIS1k6waeVDcAwWBkuYJdlDSl4gZiHBW9f5jq6wB5no+KQdSu0xBTaLBTXS7Jw6WTgbWNQge4kpj3V9ud9uF11Ldbe8vx1+nom9LThxmZn4uwMX0gwZ8hmloVDWl1z9ViRLXbsdneufibpEpX2bfTX+lneTaKnp9Vtut0GkENmwGtpanjufUl/kdsu/f3O4hwtPO+VVQo/5af4sAsgZMQMDbSTAh9ZAM2epwZPdJhiMltUzGFCK5an3UfgXtNu72S9J3K5UZmt/RNsoTGej+JCeFQ/CL+DQJPySehNWfZadTmE2aERwE75nkVd6Miw7OBGZ1Pa9A5p+NS0g2aKLFRuori/uuwhsJuYJcWnJlqi0lYt8KeSDQoCikA2CQLFFfzamIuMY0OoEQEEZRyefgQ19jtQIhqvVA+dO8SBUNXcQZCJrYIIGmqrhC/CSnRAyHmtjTBaj/8UskrvH5tRTJFNc5OgHEyLJ/K6mHO2M2GIyv6Qxa3ut3Lo9hRhpHPs6PyHykRtflp7IO88+RKyaFJbSFRTHX59KB+jHNeLb/I0mdDSmOR1d6QXPGkID9stzD55vGBsilADghGr6MUX6Bl19mGCuhfA0Cd5xIu5gUQ2urYaPShcBks3/0zmxPurYCoJREwOYRo+mnUGSeL2U7Bsv8nC5+nUgbcVBJ9kmgV52R1chdo2c0HX0gffbQKQZ2n3r1K6vg8gqUP4G231jowZ1+VMJ9axI0fji/jJ8RnDgX8r6rdJai8MsqjkWCWtbkveBDDfrrhbAqV0KXsxjs5AiHg8nzJhuUFSgBGxLkUCW0HmqBcPr5I0D8NVXDRVEiIHKN16QwyQLWuvMoFlwYDcaMZEP1PxzP/9XQMd2NMyvJsGB3r+8Fi7WhBaxWxFqvNaY/2jd174Jw4128r3jIwqtbEJe+98OGezuiN7tHQ7bngtpIKR+t+2+qsQgN2do2LxUbeNgob8ziYbghJpqu1R4HUcsZ+NUCRFT32gdBgGqqb5903xgmMaKqW+/RCwpim68bAzAGTBQyWcoHJwJWaHwpBv8ysFz1w2uyLtG4+o3AzZJrHN4Oi2DE7miMXulv/s8tdIi6bgZ1016PqdTO5HHISVUzSG/PQCpBKoR6HAQHVkrr727vEiZmNVA4GilgRJwZCuugEcFbDh2/HVQcDuIpiaB/fNQhtXG7OsADqy/iBnN6qZYEHPQ4fgBlG3L4HceI1i9WgNutMsnusOW8vFZCtRHw9Tg0f3iJsTFIEF5RTNjkROav8obFEgZ893CabXTsqZBawRcwYJSnIlE8DnTB02wZkRCTZsGObut/mFB9pzO/jjtjBuAHg5AwfmU+kCwUibmlYjiZnUx1bJ834K9sWDIY4487NXrNrttmYYcpMAbeGmK64rCXC6JT6jgS+y28nPq34CP5QCUy+Oju6GJgNTo7snjia+JoR7zWtSFlL+y6D6XTpuQO9JKihcwnHtPOr6GMd8fKyLJ9gawnBaoO0uG2/cJQwdz8sVBYqFhpnxpEpIZ5zurIpTILMvJlcweQQHFbDNeRE45afwaaR2fnj3YYIt94JGwx4hCf4RbjnJmrzMQb8sFG6I4fT7+OlbeZxAdFd0VJHkUiNnsb5R9nz/kQ29rDnPZoON64gCB1zv29UWqwCOtcPuhtxouRK2PpAC7Oad9vMKfdFVXAoKK9xrrLYSmmG2Ad5dhpwJwl5yrsDr8Q2LUMmPSeOtFwhLF1ijRbQDYNYFKqdspoFc3Fzuh5HiT1+Ba99+3GBa8kAJgFbVQ86+nj5zss3ZKg460hc0YILGvVA0jkKmDii3TA8y5hv15eGcIqIULnv/ci+9HeNjYIVVOD1oY/xvmyFQVABuBU6Qm7j/Ucn2y+dR6+0EvC8iMkj/GRFp4MgiNb0JVBfReVDucSOGsmFL/SWmo6CahusNSedXaNAGTjV3U1j7m0sCMGxoSrTT/cc3oL4fbp6ATC6USVy8TKK9iLoxN9IMzMGm2gYdEwPoj3xoIdZ4W3OhpJRKOFbd9FyiIkxYSadhNzEmOw6ckbdeGHWteWynBFonMK1jkmbUz4amN+Ff4elAnBWS6r44jMLsqNLpXc6z1WOLG0Imu0xaAKneaz+vbAkm5B0o3b9XY0+2PQrq5hDQH3CJ+Jkl6mAdBKZ+MhcQYgNTqj4i5gjzUYj1ZDhE2ZDWBJoj2vhqPv3GaYBbnFGwm2DuypXXTbdW4ReopboAUb3Kzm/TDscwICiT3+Ihn9j+VWJWIuJZoCpERgo5z3bKgJWeZKWkVTUyhjtVi8E5XNQeRCK6+mI+D8/Ny+Ptvn2nuoilryJLSoV6c+qx75MC8f7FTQ8uL4VJ00eCxfN26LZtctXmKitnTqS4au+RsY5m4RES/CWYvMyBaEyDHUwn67kahZUZA9Uvpdzh8A9JPk0gJyiFOlDW+aaVi196l9dXKrW4AQz8gyr0jrjsiRlxCG9FlMu9WoGu+hnn0XznrqwU0SnjxzzAU5DCXX3dqgm96NymNFy1QaLuvhuWGyHiY4rz0ENWhvbBQvMt4RFcO5hmNxQrN42tkMs+/5/IVINATnuCXne3bUD0HGobIQZN+EPiBciuGFG50c8ISfu0u4jehuySC0RRmbWQ06ER5zCVmrkJxkUwYB+ADkhbWG+GwEekb//x45pLvd7Z2uNBQsNVE9ot4oBWzOCFtgNsi097NNrIl4B1651Is8W+BdFbLH8if06yQPZ658BgGaik86LH+cRhIdKXyceNuZFPkSa5R3j94VSn1EfJDFOeFJi3VLo4tmrh1Mwm1B333kC+SXk/aVAgWtg5Hku02s/G1nR7HYp9FcvQCIkqUOAX4fcTc4WbcAcymvxGtstgr+OiGFBnn9RsMi5QecQt85wOFA7VK/4WxsWk+RYV8gJ2cR7o3C+928/KIs0MIeJpr2cFV4zvRDbx6L3ouz1OdBExtcdGNrXoAd27tm7NNFgofuq5LRsRBkDTSQj/ZRw/vJnbQTX3T0/m46KAupWdMzpQx5iJEEd45IAiERGQNY7U/Yniienh/OrbWX5jCwclfSBuZy9U9bDz3lTCqGHtd35OylDEn1AfEJrEA/2WmPtt/cbACpfW3f3hKWrx/a37Ka2uJPVkZxYBcPvrEjFittZsjna1Xp/7J+OJy6u3N2+OeokwhbAQwptBEgshFlbIxXBGBPJqJcqJM9/chxntdWm05OvPDZTXOSy3djOIJ79Bk1YnYgz9Qb3fDumArbu5ruPTeSinIupC90owYkjXWuzDy4UMBbeCy1Wh/ZkpxX9Sfv8E099alCHP72stzmDt6sDnMgKBHJCHqVhBkcYVl46NEjF+Dyky8HuuUemK+WXgmwmFFvJsEDdIIG7c87YFfQw8Y7/jZ5ABgdcobqg7TO/2v86u7VnqWkDNMWxetvSF/J85HjlF/J/Dr58Jg5zmktvxHhMhOWgeYBz8gV7VpDhndM35pgJQ3aLUcYK5NztBcxRDlPqt5L4/vKeGdgJii11utp/0htn5M6Rx+Yec3HBMFCwh1/wt95/faWe7lg1fhrCp2M/3C5MWATDRPx43pD02ynCyshbZbKbhUUZjTdP1eggF3FT1asGMhoIcWTocoaKcIb2N37piGjD5AYEiebqBSam2hn5QUdgGtBi6mpe++JtU4ou6tdmG9QEYySJF7iBT98b5CGFcxfuoiAiiloGT1vEBZ3xz2rd6cOq1Qbz0NsCR/Vp2xmOPzryQaRPkVz1MClULw53NYgXZX37cKlP77+URcDzm3bGWuBUKdIcmfVUSNGx4PPfdSZIV0frUHeu5obiaZYqsoTPJaDVzcX1eoYf8eID1GRi7Q0YKKR/nYrkt8LZppsafovVJ0ZJz34v/Q93AYhxP+TPX3EcTeH5ah1k3ZRpAafawr97gpV69M8EBG5mgUajN3Bel0XH4o9b/OsUWhcWdPgmCSkABubEw7SHI/NGGdpcRzCxjhXj7jWGIYsZOTDqaHvJOkG8jISIqMONLOP0NBlRhqqB4FgWYdnULNFuXXQ6lqMYufddczD/Ie85fyh7DxjZfK3Ab42O5X27Xn9zV+E+uaW4jyU/B/O2PtujKPO69dq+i/VnGN4cSMyIFXJt7VcZj//umUh/IbdDDDYyP0npOBXjhmFF7LqnmLuMaz0fyGfy63rg7B1pNi7cdb7I/Zs2buZ9gppcXxRc3ViLFo/q5KMqp/+ChsjIYI4SWK7x8uHUBRI9Lii42P2HBscUiJj7L78uT68oJZdIR9JkzzMIcWYIEDpvDLGL7JZ3D2q6oSk5irZOprnEvNtM48MUVeXet+UUgdwO+O1D9KPFfMRSnTOAOTq9KiDOpe+lWfd9EDXhpV4/gnYVvhA+2EIRNNk+wCODAcP64JN8J+HL4hXDEAa+UXBDjY2tOzNSM44T4bP0mGIS0s0+ADWjU0RT/j2c7a8TgRH7efEPe/ICYxr5avf2ur8jI/r10WnFhxNSnkBNAaC0LhO+tTRMbR2E7az8jrcd8Q48QSIyrusk4fgetzzD3nDJzIS0XqHV/fhmb/Tqm21La/5GPCdJL5iTH79bB0Ed1+EkGb01X8boJiA02rtBbQ6DE+qH7bLfE2Rhdf4SDb4LXslqcu7J+gCsJgxzpbd3oDfWEXgF68LkfYSmggrwoahyXEIeXz1cCDRqad3b2gPdKJ/HL3bow1dOLoy0qJPt79hBBFd1AWbVAoGZqa+BlfX1AH0OOHGOSD7FiFlSSpwbelVkKmnqPvaxRMkgkgfozijFgqudfIELV8kyLCP4YVzTX4ZLrKVd4BLWA1nfDhU6opkctbonWsnxubwIgMltsbC58WeQg/v2R+Q4wZk7Bg4yKE4MxTNevzLgO3ENjjjIgHxh8BJGkMDhBff8JWAeV+dVz3Ot7oNwv0CZzVtZs+uYdeqko3OFAiBlc688FWTxce9RRw/CyO3dOWrMJ+zNkZ7ApKGrybagDPCniyia/4SHsuNwm/DcbfGKYyPZ6hYQ506teOzZR3i4bT3IHhBengyKU8j+zQGeRAI6Jo7o6Ihswu4+7nV6mws6D9WRQJR7bkwSTTJjG6IOWPxqQauy3lJnnPVAZG9yU4ygG1C/FcmhJyrHDUlLu9Uj69smAfatjrYIeDaYMefr19Tp76i6DeVa+1fHlMQZ84wo9rCyESmRN1KUmU/nvN+re4pw6rQeJmdnTcxpOJ31QjcBWhWa2WFKCNasMXMh/gl0OXU2OpJY9VxvlSFZIJM3SN2eN9Tplw6P2Ew0FJsfD93MBi6sarsBik13UDlODb5VG1N0wUleQvAYLl8RzBn0dWj5PttAouSdr9gQchaLDT/Ww262NoQ+Cm15HmkFLA2OrcbQN472ff22tQ2vRZpp210c8J7MHRobAp57aChhvKfhQAmYFCrgGL3HqO6/ZYrl8UcUy/1wFt6S6A/jXp0wRe+++D7nnqBFoZhkZNEiz86a8vDY14Gq1NOjlFWIvU6D5N52vOsZNm0BwMKgHOXNE7x6ibzCQ/UeGwL2qGFjvfIcYJKUrFVtj5bsgX1VK4f5gzly9xG3SVm3rbl6AEIiKoo2IRPKDvhEartmcLyij9y73sqB6m5/pkTA4V3BECyJx6O6wDlFu2DuME+tWcDW/a9cmi3n0b63bDMwJpnDZENDDDkzOR9DPvaiZpeyb+43yafFkO4AlwYbS6AsizSVe4Chzs1khsGHgf433N3TsfHcHoM+3LyQmWFLUrg0fgS7LsUwKqmZCPDEOt0ZExxTMcgzmbLccDI+pPUUenuMYTSdRmCc40JYRsFhcH9xusKaBh4FURdPQdru2EmG3zfU6aH2YF/VO4oimh5YqvOMaGbVeLEvYJ3cThc4MXMFOgeYrfK6uL03jPJSrVjgvUwX8DmuRIgIjZg63gFtHGdWtCsZJszQ/BSFvDz+1hQfTsv9Dnt+1GVwhZ7ni3RDji6jvZoAYzv5YgazTN8lAz1MgiOBInsKNKUmtzx2wULxeZ2fa6ssU6Vb2Fcj1qEbk5jXKdU4+wQ0pMyJr5RxYBpOJquruzB2ayutG5OxuoBxHdLoplz8PG8zR2m+d7JRiYEsQG9H2vicRn+A+uP4tW/o4mofecj7FdSm6rbnRMQaH8EVhPdNU8GgyemZguvDOfNbEug+9ifOwb3SWdN+RjKfAkaYfaiGKBd3ipQ/cSZF3yja8OVBLamsva4019PvY0ENvti2ziaJpzDb1qU9Pbm5Nn4YfEQB48xyeBNhHGa838+M8qzsNVBPbbJbNJM0DYTaygQsgwJzLLT1Qa9e3mPZscoeUBx1hgar7nKZ9j5RDKYgbjg9Wf2sxbEreU82j2cRvvAZqmLI6xWC5G8t2/CoWY3HuFG85mmH6X2aJdLY6lXhQygn77LD4FVrrpNfsD4M2iP/TblfKpQEJSAlezw1JT8N3KzOfx8JPdmT+7m7bF2VDX+I9JU58tOG3tNEMLNMuw8rrPyMfkONZJ+uwqWEZRyQ62vPNQxxL8deXN4YwT0ywRjlxKp8hC5pHB3WEUv4FrITIlojgLI+i2tH2spn2aCDII3DuBVfAUHv/2PbdxVIHipU3LNjO8LcfG002XPdYsCljoyEAyut/1biPvLoI6C3ZsMiu4W5kr5zDWAeY3zgaBRTx6nt8zybHWpSBJXJI03qfVGZQLVp4Ub3Y+ZEvuMhoaxuGZ9BfNXjZqm0ZyolT9Etxy3laM2VqkkuozSR73VVqK3mJshD47W6bjXEGVvSugGuzLb6job+k+0yqUe8veERtzNrwA9/RmPlflFW2g8FCpKgtEjpanjiXUTBVCbHHp37YykCbD5vAoktU+bsSiY517MWIuhlemykk3mtaN+nT6fSvasVxpAm4ywzMr5i3sMtAqSHL1E0LN+d6/I9A7IzWjMd0JJh67kR+JToFPH6W2uhm0hI4GetSG62sOqebpeiUu8pEXG2H8EPYWTAeyNmAdflKV+d+kwwsGz7gXrLDfarpqYkqj4dtwWhoX/VACchD51HrxgT5zryexGhsgXmPTItfM2E8C8+AB2JDPluJunIM9l2R4w/Kd9qVx3EGiaJMcLAj4Gyc+Z69cMwx2Bh/oaeK8UN7nZWSGf9FAIxhljNciSt7FsERGN2W4Akgqrov9pyodONi70xKCqB/8YnhvsrS0C39VeDeDUUVDZgtZfB1+wcjc26jvlc44zHo38WijplqwhxEbV75EG1QN0zvrSjU+pM+iVqOjbpUnE0qbYVQGRYRhbAkkiyiSMqHJeeGv7CDO17nBY5ruxp7i2UjfzwyxTeRkk8eP9mpxGZKoEmU0BeuU+XmraE2s0WKWmco48O3tFG5+X+BOs0KSfn46ntiuqt9nHAfRZYIlxbPVn3zNMFPg6mvOmbJZ7EHiEzztsiy2uJ3/mrkyI5YCBoyPIGJKzUIqAEppo/VqbjZ3pJWafx0zVCxbLQ+32YfhdVKFi7oUB1v2+6k5a1h8nAFnOJJH823jmchZ6treLZ6PEKKHCx7HPBjaM/YM40BQDeNk2ED7IsmxFoiogcGpkKJck33oNpdTwhtyqvyGtykjq7EMla4sr8nHklZ1SEUG2eKX+mtkbGg8Iv5/WctTeRPF64NIMWpAjHxIxm8gZQOqcuXQbieEaK17Pg+aDH9AIZduQWjiHLZxcRFIziNzS0uc/7smhUNV6obrA1Bqjv1HC3D+z2dzwfaFK7DYwtx3QcRbDQp0O+6htTH4U90B+aLc73yKg3QJLRhbnuCpZhAe0IJACPIf376gMaXprrRWDm5/TD+UUZVsIWlMA7SLEtDIT3bndV0g/eChQrHb5VwSkGP64O2KLGWY3KWgNK/pr1Adbc7ms1vCoC7FL52L9mn26bqEYQ6LypsYKBwHrJ3h+tXrWZdnhWu+7IC+F7Z1vU6L1PgQMx34KA75iVyuUPskGBny8RALx2yo3P1m4E+CxuePvwMiXVA7GO+75UffGX1KFdPdBjVU69Xf0rOftkEANNkVj1Zkdj+3pbgJytldGvEgRvHUYQp9grlcohtWigr4kmj/7b1O/5abk0UhrkFNbk1OvMGhxg2e3RoHubf2oysxAeEtLuksiUdt1KbUMyf6Pzo+2kfEWlnHSN4fnIA1vjPpHJfSrMPxIOxIVPIa51zLdosFjn8CPT9WsVgIN47gE4MN+glT4OIuwINcjMlLGnw2ycaMW9BQoRPRgQFKFzbWl3okTKo9xhkfA2/9AK7c+VlNedcWKU0BKnU/ozEujwCwgfvbYlyuU0pAS/y1H2D0rZMAcA49fPyg/WOW+KQ54eUn8v3x3ENIix4vzEnW2Ek4zCByGCXYmE5yVwJ5RKpDYXm6NRKPKf804VNfxnHIxzml5mh49ML1By+mJKzmYYw7D3ijTAJDs29J+Z3n1PTELKXQ3EicCIQTRrDrwHs/HyL8+tdtt3LCeu2zogi355HJwgZINs4ZPtacJUZtUeYKfRXLprTGK690GpvNQAIUM5OySTixbL7ZaVrjTNBBbjLkoPw8199wtSb/LqlH2uOf3dEbl6ZeQACksPgbZYyUphqSiB5DN73gsxBOvEZQw8Rs7WFtM1kLShp+2qIQAcVEs+TQSn0vE6z6Ap6+i3EEKC3hvIcgcS3xrKPKUCM816yCg7a3XKxlbNCWzKjHm20fgmpOQXB8/OKgkePg9ejc9pFnI2kbaghq+L1vr4tc1dW5NYTKQSt1aNA5dEBArPzV8TfPJHVgyENTMK28HgPfFe0q/wAKNRN8QJi0RFa7VtBD3GoZIrJlIOCuzLAkSoAQUr8rsCWp2N42s6yblLRQuU3Zn9J5QVtatW0RmE8C8Bf5L49S06HF7tJVJLV5AG59HxfYGmlmD7oX6nzlMxLpIibatLA00rbW6mxTsp2+ZCL8MmLN5MXiapH1maQgyRnPPn1dKPuWhybF5RxLLX44u277cQ3ABMiByYq+Cl1pOY6JUkzZ2wo4Y2DWiiylc1wVSL5K6gs2/unhE7eULQRG/PlYTxsjUnjj+Aeb64agyPKnqjySp62zWRnRGePhp0BAEg8muJkrlRPMjr7VGOxNMrvv9cgHSRWwTUrF9d0tVfrgVnP+4VBZGtZLhIUWd4H8n7M5AeGmpJkF4E3Y8QjvYuupUlHom1fMsIm3p28SHzdNyVM18iKNveKhAqF8hWEv4fW+ctoBJ6lgDoKY3/cHqk3pcucBuPfhO8pglB2tsZrvM5bJa20B3uQfVsGOZzXFJMkLNHKc+Uggo2G0eB6b2zmIE3iP8OjPLq151iW2x6s3++ksdQm7ile4b7X5v37umt6YR7EcMgF2Mv3IdAikDhUx1eeO9/Bj6TVKZmKgqDTwrpPSkAGIGmMf7laWgPZxz7LUBJ1TABBRN1cgtprCJzQ7CI2BPG9vTYeXH0KmLjB1Ir+u3CEtwr5PwqRiPvz1d2yZvikLlq3D7GGDectakHXq8iKqaKZWru0TOsjSk9NyZr9KEMJWkZMZfyseOB/NweEEb9z7zC7YBUjtKCD0QrMMu/ycaExbR6suRetr1FfiY2Y4+JXPBSlLKN28jWcJZFAI49sJLpvCdnnBM509Y8VhrvfcYU7kSwnTRGiyKtoSgiepdXUoRO8ZnR8r8k530LsO4oerBCtRHeEp44uXLeNwwBUb6Q8IGwpkc8ZHtHzEmVX05wteUrrI+0OuMlHGScmwcnYYYkjFATjdaMgkBVKQ7hzUcqPf/2q6UMakluTaIOP/ONXdJqfoCWiIMpkqGufaNQ9Jpcmk5hWS/hH1zZCdyclf74McgtDM64XRbVTAN6DjGbjwBwJcflLaW73y9OBtwV5C+aawPx4ZHma37VheUwORAhtHhPdivag442//7s/Sx2S5YrN+gUIBuiP6x6vzgP+dPNeLUYlSQublcouJB42B3y4mPUM71xKcs6Ce5vC6q3Q6MDv04uFYStR4NPMCb50pTlBaijnE5YwREmsyVbsbwpeCvosqqcyAmsJfb5yhrfgPlpbGyXgk+fzA74OXQkxDwBlH3W9GfEtzd8UdlmFvecY0PyR2fFW9YhMdIwzMNDaKc6csX8VNsqDMXdlbobkn/83WgiH3Z+kmeDVRCbARG57lrSyybuLEvdvG7fXiivQW8TKrQ1/qNlsF/Axt2ZnJsUOLuc4V38xLv1/fHYOmjwEX7xQENgwDVbqgB6ap1Y3+csuRD0IE55Zj1F3shQiez++aTqWCooxO+moRjUYDYIdZ/Z8BOkCSR8KLByfdv4QP6LM2sbjFu7wzkMJB4lNtyDHbBOJXg+fslT1WlSSVvoQSAdCQQlHgNHJgCJKkIMoydHj2sT9CGPsM3IgCUfteSmjIGIxhESCrS/CoPvzDN1oaE0Smp6qF8glNsq8Ryw8TXNp1BFBV8r3WAYVbh1cwHGDWTMak/mmTLw6M8Hq7Yr9vu6krtdWK8wSP+3V+UJ9dVw/mse1GQkbycBR7wftMwV+QR6Ke2pnLwn7B+zIiBDa3EvtC5nIP6WEffOYPUkZNF+iVgxIgrnVjVqHHV5EWdFAsm06XO8erNW61f5Gk4GdfjmFeDSY+ahZ9XqD3IMvsLSjnEZZe12XXq1e6YQjOdI/mGlZkRUaouzP+TDDXiwM8NAmLFRGrkT81EvelO3CwTvCT7woxmUPngZw3wdmlSFiueNYExQ3dmR98DScHJ4Z3pqUo8xseeKpDACCnWTEcqSBK7CShjrYWFb8Un3zJV7bduWLiUDffatmorQL6/ZLXosE1c4tqRAP0MQUWO8yLHmbRD8w0yd5J8Bsjpo+OffFTXaSklUWx2nc1oQKFqVZVQAWtHHyNjclQtHDfGTu7fhQul8vJ892BythPbi37o7kiY8ayP2QcwF9cWP6qfAaACaDUHBXE3+fbyUR0sr6a2NaXwR5OzTKV1qRsqh6E0a8KK5yM+39vHND5fVJo5acawjLqgfXs8yDi2VQxAfgTCx8MJL+sO+66/FeDRfbiX217v7yNpQEw5MIdlDJ2iJ1selpYvIMucofFBhZxezHEQYTV/0g/u8xHYM5A9ywwYipZGKMJHO62hMUBFPQDNiLFZj7Sd/lT7BMzaN8qMe6nFhWzqGF+YhSf+vxuQ/nj2nFvWX4SXHMYWMwfhkbjrMaqMe4nD4QkdyH4aJ8wjdX8EyXqykYfyycQZMMDnBluvk5rRF1y9niy/q+mlRgXdmq8q+BTiPBtXnAKc/L7maPVFPqVrre0JBJmicSCtSDtEPB4ceTNxjaxd6YihwCm9hikdONrLPRvNp01HHaujPSch4eMPspYTim9mNnHMhttmVOPnv+yGHXND2sET/3So4KNs3wqsS1Mr7/BnMoih274IQqL6LMrXjCsraVWzHLMuoNoEIvoZ6PMIrWWaA3FLDRGJVRNNMGMiBBrSLbusdYBU5Op2gKif5J08qph6S7XPzdR/mwS7GsBUqFfZjQrJChNCPm2U6cKIK2sNVD6oe+RGBMrgfdE9Yhm7PbjTp4ykx2LkzKbkjCft16o0E0S/XAdBcIvOiOxlDAmrDzOShWv8NA3tiVHkfqGNu+3BeR/HBYaUAz+BocStlmpsY3As0pi4QHne1gZnwzctVJptgH5LuxavHdH86zwpo8U6dlMLnysfRzRplTMeGjJVdP+lf1D+Ecog/8lcGRCgcS+3F7skm5YssNiSpV/gsCP4okAgBIK/3rjgw/ihgHE8idHAtpwpbyIHCGpsuZWVgr9rZ1xww9f2fxyQxDaxStz6g3/ogu6MPsFI3OViiZyUZ0pwBF2BjFHi6MaYRS7L4VMQiqseqBdDtXM9v0vEdAxJLo+kzhr8OIjivC/3yfYI6aOv8sEfzFaNZgv2WmPSDvEjIYBd3HdUYRSnrjxY7fB/qyS5ZSQSBYJ1h9QnIMGvxSlyUsrgRSaGYJ4VpcHlXD1Yrq7KOzqvs7xMjdhSuh0UWTzL+DMbdCicGsAACc5UfusWxAySxn+QXy0jSHr9kI4zj9O2tZb6Fqt76D+sPkmdhuxI/pcDV+geblI/WU7qpzSQLxY0Q2L1zKKlPvxyRgdJlGVaXyYfRf9g9SYTX2IWomv4OxzvG/xxVGv+34Wgswt4Zo7kUJYRDKWXQ3gYeS2cnKcetKsLcpLFsob5fQnUP6DhJewVQyXsDrlPr6nMHcZhkoWxo/D1cdO+QCEHArMA7n9yruJT9tig714ilOJwAU3RazM+RWjiE0jLlvc2DEnmzr8y/1bA9t3DDyP+GPQ+Gg6s69yZCLbX8sb1AepKMfij+xwc2P++LouiLAPVKO2+uuwgwBCmMnoqFD7CIf8mkofPFQgPCGlqlBqGurr6RQC8wJS2sWJl5rh4SGKpUWZBhMrdo9cquvrGgfioOR358/LpMzp5FMzTVoDpmRBscd0lsbAKWbEUuE8eqB45bnFLb+39tkLPezrFwAow9C5jFtOb1ew4UJLQmDSz+nUNpVP9DAhiZpiYh1AIFWGGOTrzkUg28jnz6LKePii4x1GVb8T6eZBvtwCB+jy1e1ddmzzyJP21P41NZOlAYp4vFclRvv3VLAx9DdWFjynRwhWsT5+VspT1lXTlahMUFohISjoxHHgEjKfe2JByXP67STL0BlKGSJ2eDZQcCwd4hsRpMTvjtysgNxW1P2/Nzdro2vZYZHPp2TrpwPNLgK3d4XswW/Mxav2Cu8eN8Fmz7RAIGPWOWlvtvndEs3hCfT98SzMKkiFPtHImAj7SQR4qo4TaAfTrcpZdYL2EYH9BiHXkpu9UALiwEs8GQJ1rW10twgKR5E76HRhtABLMm/d0LgL/27OkIfIJQokHWv+T19tP8EJkiG9FTbPQSHOfllOqltpK/D3wKj93x19GrQye1zh26sS68/lDen0L5rX+Q+4gnDb1VlvvV5PJNuY02Jk75DbSPMct0rMYB/xuBWkwTpHfIcoFRqh77MrXzbd2ypGlfto+bz8A70PSkBrHwSPveTc3fzDxBl5DwluLKXPJf/xLDGaFwG4xHADB1rhPY34F6BfNb8qS81PelH8SGI2H7OpHr2Obu61caFStHG1SWu5fIMrteNpVz7TSFy0vESUSkg3oNOLu4VazPlosp/eBOdE6d9TAUFF8UYiRukImmHMkWWhg5d0ODVWKUfUdkYaSXnfYQOtD8lLDub7VSB6BN+fy//zV5c9cZC2TdUWnNGNqYB7ZIvXOa0MpGWd/XAyrr3whrfz4+p6cpYSdxztBU0ZckraSVFk8BP0vKpm7ZbNtg4jSIM/Vo5Euh+9HmVOGYwyUIbYxkdntEkDMTp3fahfKjwPShby2FrrKhk/xQ1PI8JlnABF7k2iHdze/AvmUHBf2sRZyVWIsIuOz8bc94DxQmTHpIgf8S+ApJHn4LnEOycnSxMO/Df9TnVDyhXM0lGuLslmtN7WunM6EOCHkWb2K5BLsX1ijUKzsomgLZ5608V5Y+Pq4T9KIFIrIAx0EDdUYul9wjZO5RS0fldLlfXwLSOVytGLrvG5+hsTftAvaTKATyvvJkj/lC8zk/n4UWG7Ge0bUGZ+qoEtv3M6aMmo6CtJj8GQtWk3HKN5aOaNGNHAYipeMx1QaI9Wnv+7Mza9bYnOI4TmgkcbEF9LEvxfykkVOLZcmfjtYmaOWqKV0BArFEEmzt52EMNrOnhx5fDZxRnTNF0o5cjEFPvASib1cB5x+Mxdh/F4Pjj8mbK28KVMgqOgxKWwTKNfP2tCm8UA3Ma+HveZrUdwPyrmdfa3WWEjxFgWnSDprjox/2dmqd9jmyJSmRHLehvM2t/00J+A/T5aU5EslXXBGLRSpdXgum86aM917BZuw3KxoTf/Os2jS1ukv/i+QPykmXHiqq87FtY6jWC9fDTZrvdd9T7riFQgdt3aL/eHb/YuM0VjoM+x1VniwDIA19XXoh3WchJmDjnaeYOxupU1PCn13c0p1wo84lCFzkNGuNbU3rWCZ74ZmQkW2JgGlX69Vih9RIrB5GMwHvHsRvHDQWxGmE0hOMhk3htHwkzcHqaJuH73JPX7Ls/GflmuBiOAdKWZ3U7BGK1Vw/pWzMG3JcfK04ZqTGKWVfbafdXXWizFnqMa1XIBGcMrzqdSyQsyV6ZfoFf7sCCttJ8Ev3sQCsvQmdC+zMBuSgD51X5ja8Wt/IdnDNgkYflZiO1kIk2zNDkEAwSEkjIjKHevqtgaxZCgHw0jv4qpRMQXUpGbsmLYToVgFPXRzHxaZ9YFHFMXB1MTO1RBP1PrIeoZEisBTV5qemWMFruNQyHZW1bpyuytdoy3lCAy3SZ4T/Av1yr0MbeI5ZFrIpGA3CO0JSGYIn4Kemx7eCCXsNOONH9fBv3OC1uAlGiVBqlMjdPbryQSmcuuHCrxTi3k8FgGup0qW9hgWVVUYutGd3ZxSUeHNn7/f8M+n9lgJN+elWWi9E3OjTBQ/64xipnPt72wx7zHT0wibgbED/0ebl9GwgD0l+DneUgjMK8Yamy8Okxz82hyADQyQRe6peyt8XOt5lHzOoHSzHyeC7W7m0wEaAw/8AirjvyKRqSbP1ILDfI2YVix26Ug7RujYm8pMIK3+JyqawI8qsYz6s7OfOFxisdYVOb1SGsc5hp5VaoR3mkrWkWXFbeAjt0OcEVjUytlJGXQBb5fV0bjaQlBS8l7Lxl21C3fCrfZJxfrh/M1i4ivSCDmZ5WXx5RvojTuSMDx3KqI094d+LFiiGr/kYzaDqhnPF/0DQKcXilgB8jCtf0VOwex8/RA5Fyb47axreWEdiY3aBhrbjychEsyxAWFKyxns8y1cpYnQ56v7UL7T4YfrrxVcoiW/bYtWbWQd/M4GxATfuuy9h3GpKt3BFFpgcUDuIYOT8cDuQbAejkncKMylQv6HkWXvfA7GXlxOAXNU63SaNNP/8Mvxbk/UQsJ7ktuFLJVbjTALZ7UFBFJ3CSHre8fswxOBSKzf5T2qLvsLvgietvF8RAdLVn8SZPjRhdKQ/huPk10IwUA5hEvDnbqatWrywO9Vu9jjq1i33hx3NeqmFWoFS8Rdij5F6CB+AqVl61lo/afdFiwpB6vWgkbVkZ6I4hS4xLHnT/8qIHpr013vJAavFEdk9mA1YxZ1YrVsPQAY7yH0LXgxtAvy71CDZccHsWnceffOAAIUSehxFzf1/KMhrn/ivMKX0PCA7MTfpAdtZSvcsRKsBaFhlBSYlzahBU9vepamYMVudU0dMZzTTNNydcS5GHtTl2KTpB/VUcuCgwO6tl3+I3Nob4DuZx65brMzvQdMI2avwtH5334bVQXUfL1y06P7mEM3CmtMEOIRnzhU1YtejEV6zBdRbPwASMJEB+EO5r1kzwjU3+rJSh39i3WVELedjM3U03RTEq2v/C2+WMBoXKmNnfj4ONeimAckHXoyevIXNUqLN0pGgLKpI9VqFohKsxUIMe459iML+7eKRvR0oRMo5oCaM8AKNrfHE2sFOitDOoFZwTgi6oGgIfru/GDPm3Oyi2At4odX0P0yLUVBt8y3oeuusZRK9PTQexZwHhtpm/kr/vJJ8QU0aWc49/ZUDzAAVZYsEwi/jvb8avrZjGr9O8lsE8gowaco3/Mk/d4THvJiI2AAeXGdq8Nfj3j9mgHi3828rwWpNffyfnb7P/kQvkwiMA11mCVHx4p0uaLiOF31GY2dRLGkX/cBbStXWiDv2W32JTXpCyx0vq7Mh+EyDuW+uFGoG9CH5//Q9PE6vAHaYFlMAh3ulIauY+TOj2KBhjjeNWXN6FAX9NIDFWY2ghnuhgTmuAyNCw+RnQ3T84dgu5RsxSi+kyMf+RrpgzN7+cEJVIB6e6M2IGizGLPNEyLiHSWeTjKbZo7kYZHJavRZDuae2fcbZ6/WLjqzhDdJeEmNZ05ME1N4XcLMQTB4Pz/xO3aleqT54PlzDpOS36DGk+HCDOWQbn3PKMjoWafmDGDZ6AVtQrd163hdt7V/HUgPdyfEYAAYXidMDmdTCb5KeHwFoikNBU04vNHzaGHDlQ0swB6s8mLlqOSlO3Oun0cNZ7eZ45YuKJm9YTSDKqqu/e9ffTeCLjuUtwLvxOBvYwLb0B3LtWh4xLa3Sn8DeLZMRyqEV2Wke85Vhd+Kpj99t7TU8YZlWYFAfD1M7W5BD46Lfd23oBQ0qhq2O5DQmWQkCEF/n2Z9GP1JBaiPTyTD8OKwfT2uCGGbIPpHZ9ThTiD6/JndHHCtskG4QXICkroU7P+T5+OOce9BkqvVh1zJcltpL8CL4O9WJk0HxKikcoQApkJ2vo/SxHWwNIzZ/VeoI/ZrXP7Pdep6sZNSoCSLpG+DXHgRc5dTxQMMUF6DeudJQ4Yl8nZugg3L5P3qF43sTjhRjFMWXPCHgUYZ/mtekI5zCXilQYoLT4crsOPK8uCgT4qusvlaQ3hixho9DyeKl9yRBWrpLxzNX4yx7d3S0SHnQ9w6JDa7VnTKbZacUa4mUTEspdwqhTL6oq7533jc4z68MWx7u/YK+ep9HDg+XfeNpDBwmZNlWn/Tnq61GHplRXMYPl4Wb+KPxKAnlR5vc1w3GiqYuem9qDfzat+wmJbK253Db5N4/fYxbMuMQ1kqN9mNvz2HdU+ssUz5kd2MDFrc1P9U2numY1uziwQqGSa9n2dIRRMHtHu6hpYQA2AhzH2EKUHebX7NUp/9oKTxqx/wZR5GLkX8LGkBZzwiOSHeh8/CO4tosULaofPBzbTh8V4btNfwxCLKwYHSJYZGLvaiGtmrodP9qafKNBZkxKnS97DK6D9540GjIJ+77JtORVFlEpyjJwDwdLoM1ee5LQEBXys5P4TomQGYMqrUJZ7TLsUnWTP1T9Fv+VbO/4ew7BHpQ51rv+kKEVo0TNFeGWGmoadREW4M9b6G4UmI8VrKimvGx76nkcZhGwVJkqRT4VlUoPqZvyw3+eJRLEydmhfcEbMiWAeqr5z6v8xZTX8MMFsMIjPz6tt/OqVUinePEjjFVjkm7pdv422VY/qxNS4xG2DIxKRf0a8Sn1mpy5tL746Z+60IzpJYjkPpU6wSuKKmkPb7o6dIjH3E7rnT7LTVDl8RMuiIPputPIG9EZ5BzUIFL5crfMLcrpcIurGzmBRw/FHUyyV7D0NFTK7wlbjRqgx/P9dCBHU9qwG4zSA4I64b6OT494b2leMXCzExSFvRY2aTFMvKL2P7KPVkBain6pFP0ECSXRrXeGPBV1mfqoHQ5J/hw+b4RgqQ/MSAxdDBkwap1rhG05hhvlf4fZ0foXB0Xn3sCGdmG62B7fny4/AfRwxLeep6azw7r+UNkAzFZ2rtxBjmm8OeKAdjKe9kYGDEoZkh84VgUWJRfg8n8ov/aGaWjkF0QJ1ecXsQoJJvlspRDSfuKe2gXw2wBDEowRI65IPT5lJIelqVZLMreroMe1vdavWbxGXpWUggZJTkEcfCZyANLf8OkAYCvlkB9c6/ZQFNlkV8FxzoCRR3GnbhhDuS8ATi/oml/Sgt4fEvWu6ysz/Oh23/JfyFGxqm1VKQCVVGVigz2ioykpyN+3LOWUeC3t1Mzit7eYgbfEff4QAyJBpmyLAwM+QZW1DhX+2m66nlN+pQWN73Az+6+UdHoptOsumUiu2Np6mchrPA9ca9e/L/9Dl6vLCalItGkA5XOzvuRIs60i5uexkrKZIwzGXeIv4snabnvJB1KSbftcvYtnFHn7xv1GuVyo4a53cfA2p/Tjfk9iJQgm0+igkghdke4OmmL3GggYu6V37PDsBQFaUnb176qYR5P4usVn3YBivd59r4vsDxJPAyTYPdsVQ5bXgjYYlH1VvfcvKDbiqDql3Fmq5JVlC+EHq+y7s4b9MLLQn/XHwIj0OqCPROBPxzZ0xtR1Ifr7PQ/9JicxSdo7XllVtjiGosjYQoPJkOJJyzWGFjNU44AKUo1K3yOzkmGT29B2Jj43iFi7BFBCqK0ZCu21kLDsytY479FGs5ebkvHmcm/GIH8PXk7JW0zbgzd0EquH0EHJuQ9hD1palJbkwpbMpTo7NDoZgKHmMHXmrWsd4qCfer5daBIj958h5qWEM1VVTrnpHQ/a2T9hyl3ZmQASu+aIv0u36lPKgc5vqfrNxtrOdX1s3X3TDp3IsCFEjSMGiX8355Xsqg/vcuOK97lfNfrtvTnX1ki+/74E10vblU8TCfeAu0QEbzYPA2liPjvx5MUdhNOmw9HNgKx9GaopsyD8DqiswuN2jK9C1+8kddoSGE6tQDGxAntW1d/cswNBebzTrTfKh7vUtb6GxHIB2Okop+TGTvDpjbIV78jtJ0LzlTfFz6Sv51JzFEoJKbg919BinxVDCcWSRZKDdGsCrEP4fn6e86/D0rEaYkoVhuxpMfm6X7xm1lKumSE/NTkOFJssJrlHX7dTK/VoPSLJnwrDTHZYJYcsMO+q0hUoe4swgu99fQC0DY8mWgHPdGQPIyERzTNyjMM7lejpPUVwj6sIijwHK/iOQQwY1ftjFEksbeFvgdUeJ7ol+do7uGDObnGWOQGJQHVBh3yyXhALG91XukgZ7zTxXd5zXlU4wcj6lgrkODwZWtIquAlCpaN/w8EBrh9lhxMMCQ5b9GIeV8Se/Fg8N3se8oJhfhqjsVzS3c0KpZl3snw3bWO/GZNGBUIDuFNMOZcf82NsATb/wYHbpQ0jVYzSyqvZR5peOt3raMK5E7VL2Az2Bj5dvya+5s7/aK6R9gEdh6itg2qcDaBVz5iJPLvBTwX2cCJy8+viVWYO9l4T9Bhx1PHmvwHu05jLBsN9aH98n8mdbbHm4jMoHxdO0L97FyATiKbLIbzldFzS+bmXJcpDq80eKkr9z6PAaZiRPZE1CS4gynw3e18tWLBA0o3L4UukJpegLKd552eFsuBoObABK2HbpoafmP+tRllGBxqO0wvZJRyBKBzAm4xiBxCC7xbkKEn5IHfPa74Z58s6U7K/fIqs4UHPESl/JfYBHCXA3r4y7ecl7lptYWx/OW3/1GSTCXH8OLOPEyud2/WC6+XtulG9Id4ovrZklU4yP9KFhWfDluj0hR0Ak4CsCMWFGBIs1C73+Bk5NYZW2sd+ikt5ISQNwiXzI2uDCXoysygPuNb3pwesRGOSBo4hINB3e6N1G8ZiCfeFGeCLyXWdal1evnNukYV+2Wu1E1xGpVlfMRNmrl/eYb8vPn0mO4peAoeY++17hHHha6JPnnJ6thS+WmZRzPuQOcznH/mRSnDarW1lOjooj9SGX18BKyf2BV9WLxKDEhNIWJ7cSGWXDl5twV/03Hp45prKh3OLSXM+5o3DU+LFFfCnmXLxd6wmOh1IEIidGorf3kHcQMLryiCk7OJgxaNTN7OSxXW4tInznYHRFfA733L9t1gCl5BNbvWTTrUhImREqG2+6m/h23XK+INoUwUfpJ8M7fcwFh9xwLG+jtjMVwyRivlEt+cTT7Q875/WBFiPBjHPOrdjEzfGEmmVOtvE/iTDjjIXUSm57ApduaoaAvZBWQEcXLR1TfoJu2NzkKgQkwLpXhdCxcBkpGbatsVPYdPVc3besEFJ6dXN7XyMO9aOmFUCAFy6ocK4RPLHODPycq/VlLcIgeD+EHMXzqdL4uByABjJ/Hkn1AsI3Y1b+u9o2tB9MJO9KGrhCEloCwk9tWRudryzCe2P/ZEB/9aByhxPwKFTPU9pefoesiNbQgtl51+DC9e68NX8Z3JTj2G9/QQf3IjQ44szUgs+PfIM3yV5Xo51GgYCe4DZuUNGnPKjEVYukvWcO0x3us9I/hXw4PgBdEF92qc0LDpG2WrQwseWyhdyYnWF6wkJMPF0RXq5pTeO3PZ/vM4YTK/B0TJXIGdk1XGmGltFRxheXQJcufWZWzpM70tOc/8RCZNSTWq5aNv6BjAhX0HLG7DOfPLgs7Au4xRsVirGhvs1ZRxApb53+YWzb98DzKKn5GEs6BKILPgtaL/PBJ/LGqSHPxzJJhZ3F1oBguvU/S9We67ajM6to+YfFNCk1/NQFHdwA1z0b7Fdn6UFKCyOdb/EdOzE7Wd1zIQRWYtK2r2ODSH6RvwaCS0trlq8PxqyusI+TeiFK2GFK+iLt23/998f8Co60sv63vBLPzzSFS0YEpGBnCmnPA5wZk6D2Zp4VQGOPUP+SNu1qHA95iaRNPA9S6l5yY4hq+qtJsOgfwb1R2438KvcjEA4s/Y9hfbuSD2ELaSUYaSLHwZvDaLv013VsdOgtyYptjYeSjAt8g32q3twkchphsXiMGollZsjZXEZUIkLodEowWE6LPhO8Gvjlk7wbnZfM9jXOdQmqMARnBohAOX8MWAxNq32L03W6kAD532xOldAs4G9kEzlR1qTjHwNuv0aP8Iwssv9zJWY8QRPSpqmgXWGS7Y9HWxE59A3vo4qPN12hg4mBHYMSWLWELVUUyoDR5Go1lsqtYEnywCwpxyYUvJ/MxbQ8kbuMR430VfzGPPnU8bgH9Umc0vYrmQCzOj1Zf0SHhnoSEDw6frbrgoq0GzqHLyq3DBUVLD69JSGNbR+HUa/anSgJpDsPOGvPHsdhvoptTsNSF+EcCH0glvJu4lRgvcCo62hFa2hGLCWxBvtrXJn5/GpZDYaz/xDtQnkxqa/59qxbOuY721vXeWYqxx81BnO0AkLqNrOr9oBmtI5ZDI/GIPtFvjIbd7cAXI9/VajGdH7O1CS106s5htk8mlQeUiLObNaaqAuI3BU9IjBYUKCf6Q2Vi8OthLQIXqk6/CC7Zi3pYZ7G32foElhQHMz+m88uhINRNzbOVYsklu7CfFoSoJbeSsDNeItyRqqZNjlbl0asDpof6T0aDZNyoo00HDjxC3dZC6syeideouS0sexcRy9mJS2C/5hQJbjSfQ0svABlqCpR76+XZsm8nP/jEBKv2vxbu8c5j2JNuo5HSUTo/FjwOwhKvP+j8Ru/vsBbnbIVh2PCwTbvq0oiuz3u3dd5aMFrLJTInU7RKhlO70VwNCF4PMIpoJrF9oiOAPJVcekXFh0O7Z4NRrutjQl8pFDHP9QyyMJ4AMPMosPp3PwZWogpqpf4TN4AtgfA0mkqWxNOZE+6L5G+lW6CJSQsMjdYV2h7xRw2++ywNSiKyNig8MOD+w17iaosjfwOxQ3009qsMmsw5II6kL1CnbKBhupIfQAL3C+nna2zcFtbRp/MpmpWbXs4pKEY9rropB331RUqq7snnW219PJxJ1/ZFWAxNCLEsAmDd7ST1D8K7YJO/E2xIu0x2yaXcnHSbj0gNhncTRn+8cQR9xa4PSSjpUUihBY+13qP14yAGjfW2K0lnunS/ZWY7aFQ4E3i12l7fFF0enGtFy/GbJ2GMIkF1y6gfeo2Sk3bJoebR6p7Y+BxWCyUEctTdpHDHJjSj4f7PNnHG2YqP4byp0dUf0VA2Pv0MEO4P8l4TRR37YHQ8UKw4MKRSnwnfSWiy277acX/ye7tz9v8gfVIXuulbNmNoeGOOZxPWGRzbu9rTLW+ODE9GQoA+Mx38/V+qDy3xK3sLa6yjnygsYV7LYpaElOp9AnAemrNTgkPQltBWTHCU1w9aCyh6KOOOrmypRVisiEoFklWh6k26v7htsQ9BxQJsq49cetsrepJ9ORC+Xy+u/zqo/WVIVG6DuIoUriRq+dsl9XB3Psbh4RoBBIMVT/BSA7zjb4c9tI3LQoLMZb8Tor6lYd00XtLV8NusarHuBBEgCshAFz+wP9b8++kNVN+2vIi3X/iH0jUOfAs5kFN6pKcinZ0rUuAKMHxKcN04LOOTASbzvPxvrjHBQK+vpwNUlST2Oo3Or57zL/dPKcEiYtvMtAe5kouX/y6hW/YGmBUUGxwQVPkW++CPc+KKGi4+fzcN0vnoYLzJPhxAoLCxF9FQxgkPyoNyXGeQ9JPVRL/IDMihRI8RbDpFnB91TTKmFU3CSIYph5p1dNjusV66GBpomdYg3D54dm9zLFgZl5aeZUEJ6QQRw4JjlZQ09/WKqS8bZturksEiFuU8/1DcZclbYxSN1cYncy7TsU4C3xfaWfAZEpHTYK+T/jKnxAnlQUHy0sKAlzhtWGtsC+ip+x14eAklDf2kOwDBOwZmQ/b6uJKiZAmZzbdse6maKBxtk+7g8GBCc8WrSeXlWvXFGSPYbhmIG5G9vDoNOAnYjIil+HEWjVJkxfw/IvS6byIwiX9VTOd8mXuXkm6fw6PgbSX4EzgsWp/mOmR0R8jzUVAxUwUXgt8Yn1XYsAJ3h9Tc7MzMfvadOOATQX2exJDe/XYWJlLoT4sACFheyD6R7RQISY9aDg6dfWy0adXxMu86eQRZAiE8cWEuGi1CeZq4TCBiNYWNFsOmfFKfxoaxquNEoVt8AsQE4yXy9edp+MShjk7eqNz84qpQV7gN5MVSnX9gfiXbPGO4PNJl8oAH5L9xRgAtb7Z8Kan3y4OFttGdtnmIK1PpKfKg74urJI3T+SA5UXYtQoLGnJlyavxPG+JMSTMaFaizCw1AwWczr1MBsGNkzs+r1u131w62J63wYUtmmF+ktu7H+e/H4cMUMMMzstvmfgx8UVYfuEqEtVgYjGMdaymoCpseUlELpnfAUviHIrSqo9LNMPmPbFVwSqB43Bs5tT/Hah2mF0HVeEWKI3e4BQkbN2vfFCtW5Q+sf+OfW2/uWgpDILGtQZbIKIxZW7OIIt02V86iV1zjlJwBnr+ZYV2Q6EJQEohmdHZeN1axa3Bdg3xmVHNogmnswBgkr6PRll8HcQ1RNj9EAOjV5GkVCaMMYJ8fummLoSmZ4U+cM3lFq/Kg4j3cK1Z3RZZnZOHuaeOHqhu9nXa5REkCTUnvmR8ER3NBHfgGjlVFryEQP8DHOcyh9B6cQr7u5DcsPhPH0GM5ldPn2ALqrQRHi26Vn+dj6nPhVAp/OkSCSMSwCWmFt4SpQ6hIz4MeXumCeU1CrfoRNQiIKGNf/uF6l8BYbyMT/qM7J6n0BBtQdBxyjlSGvpVEXM0vjTGLJsd5ofJzflScNLaZqHWHxzR8U2NulNQVQ5m/Q+zOMmi5fhWdjMquyuJOHF4c0x2dMlaKcq+re11KlNIM37XjbHRiy9eCa6+lTpBXn9yCDZavDEYr7dLRJWaysOy00l6r3BGp/5izWy6Ic3HceyT1+98NYKa/pQ6qyHcgEwWWxeP/4/TdAVYeY9v954SoZbUNTP0v078D/Z356GczObWfU8aJDuZyNPHQc9QbQmHFVm/V/Amev047KUpHh5/6HZ2k5woSnS7wdibVuGLh6krylHEpoXchAxXJp4kVAAsJvr02xxeFbxjTilTKS7g+CP7og7ZzB9mGdAwP8PBPchNBZyDTzC+lLCSv1qNdM+qa8p2KHvpi7vuBTUdIbIj3heSduAwEMrKITJzNGaVT0RjweDEVnm6qONILtc8N3avkIiQipSLRZDAJspeYiGIavRTYS4MYUHd/m2ogn8wRo55VM5u5oWq8NZJJ73iBhFHbu9UTWPNOKpdcI5HB7/c0I7m15MUaHBlNi8ZxtFTNwM11uY4exkOJuyTqM4p41PNV5/EDa+gaXAlME+r+7YZaS0hElwHV9uaQd9Pgc34QS1CopSXMxgwm3WJMjc2uKLK5Sl96tDFX7lEg7Z6bVhg+lgEPrjaQb7A/82nTDv8MRzGGgCmNwtzKUfYCjSMUnFiFngh49HUIGYxFidgQgwf+/tnRUyg1LC+kpeFkzrxuJDNUZRlGl2xwYfGuHZBjl0QITXIN/dRoXmpTrad68fJJJKG1iY8pgqtmhtJR6jz3vYYvaG23sHS5+EucZfTERsds3z66KW4LTc5l5bo4sJl7zHV5QvpUjnsbGejH86T64P+Uy9Jep6BXwWR0NgIqG8dOLXijDxA8lFt35DWoY0NiNTVVn9sBoemU475ClLn52xauOGk67hskhbKZjtzIRUWFAzObOMO0h+L6Xrzxef/4Q8zmSPErfeNSmLi+RiMCbMAOQmyIATwXRU3VCs68dGuhimCcPtmoqgILHWc3n6XCzpt1kupY0yMwewfMyXgIXt7M8ghdzP2bf7ZIJFhsMpcyhLnuQMRmJa+cpDhk25NJ5NupT7vH6NpscVxEhr8a2D/6N0VZrfFZM7D5DtM3VJ32ar6UUyp9vrM8rMVubN+nlbulO59KsRWIsmSIkRyrG945ipFY2+nt3WYkVehM09pRlbrEOe5iuir8ceAZtkvrfBBWBRLmYmPLs9i8VluKvdfkRyVXws+XteCeVVr8Ybodst+3kdyPmeqiCFkHE7fHBoYFKD7H3ouqzmMMFcaZGZrTd/SVJhcxD+mltHz2DFla0cS5q0Zpg0010OUp64A4QcHEonpoCHK1TTPMC0Q/TDB4RNENyyqLri8Yz7XIYKwHCBhOpA+ZMcaPhR3fat19T/+cNoXJAtxc7nEbTXrAFRyOISa2lfXKYrzjrqVisRIWB36l7pWKa2rl8q8aYlbGbYKJdCanfHMP0wNYkvvaSYDPmHof59ro6XTYQWBfLorV+f9CXEYTDDDRKgmvhzcdBJT1v4KoslN8p9Kg0CFvzEU6eRY0MWUfQfoKD5WE9zFNNYqr6Wjk+F/N6o/ChcZ4+uoi7Q2vJlrWtDTgkAFeBKr2nBHWmodcJUDssaMZu3YZv7tUU0dMAEFTJeXL8nFFVFp6vKj8zyQBl+uZuYrs8qt6LpnBVv2JNwCS7nAS1qXfXQcz8SDK0mgRZ3LZajWEDmy2aSwkaHRrc3L/HNlHks6NpBTYigOez/5L2N3Ad0IxFFY1Vk46Jx6WHrdvZThsMbSV2PMSk3OdNwQGNCXwrCO4XN0sT4F4y1zoB8tgP9/FpRtlC8wDzLG0xpVoNafftCzHo8S7K4bPYWJJisYD0X7D+b41Ovtn61Qm97z0co1W3/clqLXM26HtMLIqoZDi9D5AqxjWAUbSCeUAIhjNkN7Bqa6oIXpcsulus7R1LQFlpw1Z7cUxcCBQE4iYB+sCItqGE/uvrR4jBmUCP5AOkftWiQHSjRfnXjhi7vJEV05457hBQqZulguf9B/1puw3AaRHOqe/5JGXEddwzZW+93mlSsWSO48zYkbN+RI3Grp6z8/Rl/5V+xuMUOFNVeIKl+wmDWXqx8t6kGsDqJalTh7Dvb5PB9XblHotl9CYAGZ81D0+QzpbKPhM6KzziP6dtK+I/kHsxceZmjN1EOTfidIrN8dXqDdnCJvkdJc37qeRsfyRgM+TGnR36b5nvZLgB6cORuwUPwmRk7Lqo0NRRI3k/wlE5wA48DUjvhfaVfuHeFJDr8EADiHCG/YHQbe9gPuj4xyybcqp6arIK8omAzVtttusOzXEuJtxcIcwLcuar+UZwLjrLIusc/fqiGyB1mu8NIyk04F3Pyf8XCAJNd4uw1lygYRCSpkgM9I2h0adbOCtV6klPvllv2rAGbenG5gMxnBJjUZVaYtZwjXR+4Ul84Hhg7ii2Jzok1JztX0gMwCIpb7fwMnyBUIQfPyr7mcVL9j63FZS7hu3rMzoeGvQa5ufnGxj46IQfXKcG2HWoNysPJwMfpMU7sCIMkCxT35L93qAlE4eH782DK1+f25lmZkftpmIMahwz0AmkQFX1FSxdSlBywYQrT6iU/XzjJZDSGT6kis1D6eUfuR/cULSPx2FqaEGTRzYoiSRT7XkbSbw/TDbIB4wYdFrgCt0OfPCyT1A4oAEtcICgN30Dbz7e8xOM7xEAaRQ3ege2GcKy+A6EP44XRLK9fXgqKZJKszNN74YH2OUxQJ3tRNQzCuprrt7/tIlbIaQ5C2GIDAT0NyGlR0l2EIoHQWPD90+30GqBFpDoRA9iyf3r2QHJT6KgZe4W4D/cNRSRcsrhKeehsXg2EG3a5RvlPwkcFl26/08SMvNnXslT44I3qev5w29eyMlbhnDEVxfNoV4cUqetkzdLRnEey3eVOtzjydZkeE6shF9JGkvfz6VK1/Wu1mKefSdDDe0hwEtopryhCp6o1NppdkFyacsOwedTxZsBUJI2y7NNZnH0WdrTbkALpox93RXOOPF/pO/8AM84KkfO3foFyEHkIAuzNaSdebCWU+4CudBW9irQaxk+JqYp3qwWIQ+svlsv2qpJU1tkdWGeX6tN3DYz+o4u0veZY7XrL430gPESI4zQthagzYlC6sHlC/X9IZnZ7+xzeGiOxwzdvwE5mzjJ3bcA79DprYTN7Pgmt61hARJ6WnuXhjw1rQkPIvHjhi4uCE+GieccuhfXnYykzvsqbY/xqkSAW6b5v/hwkIq0o7Vck3n8F0Al7NgcjRAUWELWQbCNrvfDee+rEtyoZYJvY2wFR9jWUKgT2VNjkihVxtn4YamL7DdhgLWeZFjbJus5e4mZmkSSVTLD03QlIvQ9EeRaBL5y7OIJbVPt56e92X8j86dFiNguWJygrvj1TNS5Eb+OCuwYvhuXh0Ilt4g2MABJGuJHoXItvWk1k6P5CGa01HWGD7LO69UzNWjbh0qIj1FdAZUFBShdUOt4IbPQiE0VpsOM4TN5PCnjCL7Lpp1L0CA9weuhGva34otsTioLQL40RC55JC4RUXyCUdZSZnvi1dt2fgxvELJW+EUlhw04/T05Ar5aRzBDjas5IcsKKcBDg3wXjq9aY5ULhbaW9fVceyPsJpaCTxHcFg0iXp75z3mYQAQC7unS5RIvlPl/KwTokbjKghteX/rgMANNDyMqj06uT44NeCKjNw27EDk5mF0heA5GspfRwyMEB+v63yTWWSt2MV2bzCIEu1d7qsJX0meyCespwb+mPi4oUUgkDTxxobDIuhOYvibjgV9Rj5ysh6+DxkIbJl5bpyaz9IXlMQbLOHyDDHhcSjkNfxEaBT+FfxBZD/THhwYZtkDNbJMA8lwuEkpm9N6CK0lt17ahOZw0XGE0uNc+trr7e9IvdTX5JJUs42ILcbhNbMGDpczGADuKhLVkzRaekum+WyC2svRSU8CswOsjvlW06mg4Nml3xmgJH4CIgfIRQ7KyLYWKm3bY9sRdg6gK4sy3mtXkdIdtKAMOEqMPh6vVOjZ7RCHMBCr/0c33SK/+hdSQeB2LpuEHiNX2RexBErHNNONaXrWoefPFMZwmPKobS7A2r2kWXcVTS+U4QgbSwkUKEYn9kmveQTeRa/zoPVFIbxt0EmKRmE+4Nx7UsW0a83UaMhdQ3WiSZrg3A/XMYIX9E5mP88cxaSRdzugFyXGhSwXdJQrFxHejw075kQlJ8SjJ9Ii+DPUq90tINsYLqodjNNGnZWDn2gWR+5UFi+lnDVjAcHZwcpwSWfIX1XKVc5OPTf7E9brQeYGiGxsgiSrAcelGQEiJObg1c0Dh0A8JhctqgVyo3vSwq4MGYoxivVJ/XhDfG2kmeERHwVd6wswRtlqJOhz43Qz2/BGktR8OlmixQHzQSWdyhSHyyN9GwAIxp0ClRgodKp3cGyoNuStRMnu/WGyEFXR1P6NoGy+Prc/1G55yD+tRLXP1OBC4epgM8UgHhNKW3hqFQtFfhr84fyg9ghYXcynbq56QuEDTd/h+k+8DDYY5cg0SVDhB6ynLGS6ur1oGRBvc55JnJstpQRsDCf3uHNnX2q/aD12TrimZLGnTju2LFaiZu+VAvHm+3U5iPrArp5UN10lgP8LUEPCJIPA1tBuxkEuvMO8TtYFGk8ytQ1ek3/X2HHePdS5Xv9PVpJhF3KoYxlgFAsh5pmDmyiyERJy2LPPzYHo+4dbLuRMgpUmh96ETPyE4MNUZYfpbJ7yB7DhwQ8zJqNdNjC/bWFMidlu77fzpBD51lHozNtlZLXtIB2BqMeedQnwnrCzgnzSexpVGC6cskWr6SL/u8aEhPLH6LL4p7F5hJ4S/DDc5Q4N/bDKtuF9pe5zvma/sjVvu+uvFFoSnuvgb1xTdYnc+USd5Ii0kHFGeJMm0BYeneLTWIjtAxS/ai+r95dg/T+EYFHmmvgjyBn6C1IZBe2KZQ+J0KYwtlV+yf0kB1JAPnxnRpdI+Bto46hcJOkXK4a5Y0Z8DkHLtTVCFDTHTLTDGRqJwhMMeE6+Ry8FeH8pGT2J+nqcqDTVuO2NKhI67HOK/ZmG3/TuIU9dHmNEnHU6fZp44zHg3e3wPpW69FZYzB9RVXqS1ksjJK9suZUH1buMrQ9OkcMkmB2Xey5UFEMJtTGT1W40SkcyQHL1d7LhJ6SD3+WDGe1q4fJ9X99i7L76AwG/VoIdsWJRoDKrPscWFoXoLlAZxxVG44GQws3UGNu2tkSoSveI77KMRCBvthsqs948gE6KFZda+fMwQTguGn8CV3gZDXwKRcWiYdAhfZOwtA/3kNw/2cqCRCMrODZGPA0zwRsZ2JItmNa4u9vkka+Xoi366aTypAvVFYscYHG+J+e/542tdLuXJUdziT0G4xSDf5XPhJag6EUUMGs2vvj19wZ6gRrEMgXa+zBM1t6TZmMOvKZgBeggm4lm6j9S5sPax5iClio5OH9aniRHvYHYmTXMJlTk3pbjs7/FkqpEXf/LWZi3y/E1ptIBM7/w24ZL+v+snZAROYI4h3tSKug5PD5rmp40im+pJAstEA/JzG6ovDXpCBDVfzNecozFsoKKsoa0e8ULnhR5XkscG2Z0TsuKBO4MLGYh40uVl8CKizVyvYDp5vUq0aoKdTBK6PgrvvqoGVMGhXyx6aX/73LtVnJeUvt+swiKdoHBgmoJATd3LCRfmtIA9FW4F9CflJb5hgVyd/V0Vnsi6rF1IqeXWegcfn20ILwT97xJzmfgNkxyjp9KNCAC0tbXyytLkBFRev8VIK0PwIWse1hOLLkw3lEBfpspFFDBCMCMYIRM42kxl59iWPGch4SQ4UXTGkdE4cx4iKcYYpLRV6/ZMO8Te2uM8/IVwbLptbEVR102WasXsu1yWD49lgH7yOsC5G8a/6sLmy3TY5JOQXbMv9EWZ8bOJTdKKkC7nfxxvQaU+MNKibTFrGDaRb6W3xE5PkaMpkhNhHiRH5DkC88068Pmx29418OwAV61boHXdl5fECMlFeKzFZ+iLBtY900nhQuyKhvIDSSRuwlkler6QdlLUpXyj41BytVhjbD2cnhOnjzbvBA9zsAfrGB73XXla+XqfJBUah0gFSO1TWr5m74Ert5m4EYcQA0FjxINbi+RdKLv1Io0/AsoXhQEm8U9HJvJx1He+gtFL4bFBFHUi/G01UdD82yxJpDkTBy2GmtOnlIljj6E0JEQdgq8PK4lMvXg5CK5jHOiaDK2GIEvYwj9GPsTdualjkIz4gkD2XzsjyaPs5VNXQg0ufIhUPKClCRjB5obKPrw/L5LfGYLr1Wy+u0MOefX5iKqXParoSYM1aRBKAvghI2vIkTaEXZDA7Tf412JrkzTXscA7SB9FPM5AgYpJHgg0nfydZ4t+a5RPA6/KMoECneYVg/dfsNsO74rbAU7uO/oO0Zh+e/XHdIb+/oXpHkSzzeN3b2jC918A4cIyCOXrR0uQ/1lcf8cHMr2VB6juLJ1P204zBTVXO/DmRWzH3J/s6T395S5sePIG9sW7KyAty+oLa8TCYoH9/iSgfnWCttgLO0IERL/yTn+0RtOPFL38Wi0SpaUaS0waJC4+ykmu0xWveChA3mt3EYT91q/rjtbGFQI42TwKwMZ99yco8dcVUzX4GsBW20Ju3svghYQvPnLYUo16aFEQ+Rt4mvBrp4f2xJ1NQ60dvSjsoc6u2W6AysIoK+rAL6XYVAJJy9Ru6nnczW3/FHjtBoCPRv1M1kyotLlsgocR5NixJ0y+W6OowThpQXUjSeHyqz/xcSWSz1YZ1VZ9C43W5Y3LTy3SCQef5oC8zG9cajzO+Duel5B1dJM1sPvQe+ZxPQHVEvPtgxQpHwwToN4UCNR0qMnfk41z6Ms/fOlR/EHRoOz/FkdhfMI4jwmfuktP5Unf3tlSH7xnU7zGxpssGaCtcGVr1S+K25jHRNT+k0VJYQfpYa2Ruz4waXyO/Icm9vTyWmEgfYq893yNtrdgVDYoYdHVMr7x89UQKgXIJvKoFfmxU854o/Op9tx2E+mHLWtRWw+v3Rh8ne4wmzjqF96lvsv4I1T77kpo8myaBaYHLYLGi5XBZD9fUXgq+B2NASXSLSkRk/ZWMHZ+gkirDquBIuhzA9XickEooDvOwLWVV6U11nAkAIFOTahPmU5amUU5T9NNJ5eqYCSSBcPCI8RfO31IQRa8McO5eqRFR680P06o/DUe5ri4zW9gkRQcfM/MRwdPRyjH6nH+B+arl5pSPBhkqSrLly5WXYMFj8pVB5+QbwfFxL4r9w2k+FIk5dMzL8nBNxZ/qVRplcGDwZ76RZ6lltZ2Ek7R7hDQmrPn0iFSutcO2+1XcLBr/TBmsvfo/AAa4v+RV3cuQjqrx1+phGldO3+lxWZSpj0A+bADOgetfWAJuC4HQbBG817oauN8ZCn6MtUMRJt98YOSnkto+InDlPCgSiUzgOyMvJ2LKVDBvRN4RBzCByFO3yUOH5Fvoboar/4JFw1KIcdNkfkK7nzrT3L7wex5mlsl9P1UnEIEwwYLxrGyj0f8PTUoHFb9NsDbVFYK8RFkDF7mW2p8Hf/xNrd5N1A+zCTqkxGUBuwfxZuUFDYp5z3Dni40SqpQfOEapymqRfo8Hx9kJk5Ql/hWdyuw0YXi5qW/lvLvFx7oB33oYl1v5PNazFe0yNItHWdBHA3QNN3sj24jgeQ9xGj9SBEPpAto/0smWF/DzlaTWx3tZwxoEAlWTrKU9Yt0xVCCZAWLTsIrbocts8xgH1GC7DkXKHsGUDTgomgbnJ2AI6b+j5Vaj8oEUVzAvfQaS9WUP82ATGkm9PUFD4br/n8bXvwUnoUFsb8yvlh3OZBkJ84/zGvX+UYxUsW2Kl8dU9by+Iaa38SwkGFbbcbXqImfVW1CbTEfLL4iSZ6W3BOJME4XB+lulll/2cLavR77/TaGAoQURJhe5iT1gcc7N1smi6RKnvcFVPWZyiEJwv4/KWG+bWl7w0fo5LuKkOod6glIHYsBZy7RfO5C2tvAHswkbQceNqLvZ3ToHOF31oMTgKV8qLzb0T13glNtUfzW7b50bpJYgsU9Je5BC+QIoOh4hqzqFzZUZplJyEtvO1oRDzilkPqRKjH1vFFpgvWZ04GEa/kGPx49KOl5u9kcMlsMMrmt47r7unq0xzB6Ngl6rAYqJDsjtsNwfEFIjasR7HySnAtT7qctxLttYmRYkaKv6l2t+Al+iUGyB2ndwqRJYD21aIRqdq+Hmovk15Emyzh5x05iaVEm7EkMS39JpOuU8dGjVtRicI6o1qQTkAiwBc0UIYdz7tvOjn2Kh0fbkCPkWiEAtZ5DLISnpaeAy4bYjlfvs5Qr8HrWOsIoW021dPKCeb/z8IJ/f40HnWJP3mVDgELzbtoDu2RMTlw0o4aaX1JRIipGdSfb8SAzklCaJeEyYeNgGBPXcpYnUj/hvlmPP+Fxncwc+5f+6Nhko1U41+mxtxMjYeSTYPmGhAshhUHd8+RYug/3YZYrm4T3srrJAB3Ckg2vQesXsJLTtlNzRY7LzInBGW3XHnF/X1nTwzQS0A21llYkxRj7qPrQdtHWGQkDa0Tx8uaA7PUZs7U9dD+EvOd3AJtu8K9+6prvjXGnw8PnLkZjaqQmTo0k+RbxG/hn3MKn27c2zalePkuzA1qg2VF2KghrxNJHlAL31Wr5ihvFl1J2QmnjLvTi9oG0vm+AOl2zbxpsXxDYHPxtq0Vx1bpwTf1o1RGwKYzj6W+0uSMJLzf5k6uyOWsAIhNKl9VHQhCf8J7ljhOnO7KXz3QvBeby6dOOLz+qLvz3svPFYkfcyQxxJkJkQ9lbQYGQHHfOokwFkeIaiKNj1f8qJLaSu1EmOsIH1gqAvZ5ck8/XErqcpV9A4yatc3G6RND+pZhzY2M14BqZv+TFdkToLIpieqTHQ2M3MxkPNJIMYeuYGRpDe8kQ/xMuF06c4ed9ChTveNGmn173nPmWUlG4JD2iqUTF6PYpTzDEsUGZhe8uFfAA0he6M/ReAfcuy3A8iKYh480rzoB0MnKp9SFNcrpBFoajq8OkVU61DXF8bcBrfQB9Ly3o14FNvAJqvmWAcdCeEVPP28IZ9kKEdBoG4SVq0CmosVZu8hA/MXvk4AGnYlaaysfTkD8hgJ7wn3dok25KPipYWazhvT6hIcOTSxwXkq1ticWNTIH7JGCUbZuZRWz/qPKFsKfVlg/SRcL1DScnX7B31LoUKDvAYqQNGrUdnsy8RqMgkqZRrB0hekb9jqW8lKH8eZa9Y8yl/sm5MNkzDoXYZVs04Wmwpd/bRHdFPtX2Od5U9H1mHajr+SXxjqDSiVFVG4PXAJ8AwUAFq0f3aa4rzhs71Hb9BZKO8nPdai9yOMEz42Qojk4rT28en+Bdv49h5pl6YicWjA9tgEo+/X3T9kEeXiicYopWBsToGABwXOPA6bfGjzoHL8Op0rtV//bWGn5Vf79lG2vILF9L59Jy2bJWqvjpY5nR0ANkZuLfzBCdf63cQELsKNrcrlUx86aYyPknnBhqEyUf924Mjwro4xZTmRj73PVJxpOC3UYvAZaIKVVV6etK9B8hWr30251xkezIlmztiBsmmvCi9DV4US3fORxlzXO/SgaG9e2wM/rKUh3PaPUJZVng1asBQn1eIAEAJ/9UZy49VQUwgxMiB4YbKE7L5bTWx/XMYvEyufhrboSaS1cFKGCfCoYNvS+ksfwARCUwMQ0ppRw7xfCjlBnTAMzpjD3GLvYoVq01/dWmXvAR5rFjImDaaod4Jq1w4mUBINHcY+Pbj2sh9YpsPvG625e+VMG3tDQMWjRnuURsB9AVd4Y3tbhr+629k4eXZKBx3Y0YvQ1J3+hEQSpdeX1aioeH+uPCpBXe1WtjAnK9LRbgXOyLOA6ylzWrpYrTu/PXl3Fobjcf7hOMiz8wj9Gwn/1LWEU2vMZ1FizIXHZl8fV8FwyEg1j1FoAl/CM9xpNayU4er0GpeNl5nchHqsESQ1vxqZEHfp9eHAc8Kl7gYp31qBD5ahkUdfE1oM3BbnyM/CqJscIOleBxM42/THn61khzh/ZjS5h1fpf0AdZ3qbS4l1CA3k9Hy5ox7K/lWkVgsYjzZUUHVKtOqbBkGc8rvwBFY4psgGRq6XUc+XIUfnkVlDsc+Wrvam2WjtIkv7AMT5LUvVySS1l7vqrRmx1Zag/zgk84TPTSc73wGLAn1y5BxumXYpAFpjXk+FVddq1J/j43EW1ejKfVInUbmivz01gFdX9pslD4jZVQY0yKfYVrBBifCCbYa+3R9CaIs3W5eReJ1FYkxN2cB+jldux+VrSwWmZdYGU0SRTcbu8JjuXdVNhYtJC2/lVUJQBE12Hl8tWm8gZ+llcr9G8yy+MVIkNaVJqegGKYZvpzpQLlHqagiy41n8W5h11UNYytOJJmftxBpW16jSRQZqGUWe0ORRWvuMCl/3Wj9LSwd35VJrV5YRnfzaCjhGDVVHsX0hJ0EJZ35cOmUK0ylP8SmcILbSquiLx1bFnYSzPzeMPmq2gZJI+HvfXa4njdLVxtri3rWg2Xpa0IW9sD/5OqqMe8Onfb2fuPws4c2f90itfmCOqrlFT+Fqu4cbviTKtUF1ItU5XJ9IYQNX0mHJ7S/Tl9cUIzCTaWr1qvxgL3AuJBdWOMxKvpM4dfva483vHgiWBvM4IYFAaiML3C/GEzjUsof1TVFhfA2yTQ29pMddBj3DbYKS8N/GP9UBdbfy4IDpow0ECR9GfSRbk1XwT9xfOjo/q8rro4rdb00hk3K5pmZJYacIlHhawt9Jkk66UOY8HvVrcUNJoSGWx+jZrZ2m9HFgavN7A0iHhvoeMFCZXzCope6G6qVvotABMhL5Pwr4tTA2ckHmhEbQJJh+c8NhInGGbpmfZpW3d4T+q63nFOggvgVe1fRCUh32qfHF5GrfYs3YiF538+ozhbB3BQ3X3N4cKEuSrGXE9Q73sZ7EuA4vr4sr9n3Qru3YatEUPG9ogwZfHmN4KuGgKhy2LNcVgUSiVOHeS+EvpG6xCyphjigOBmIvdjRn+r7/o7ANItSr1wFAuSu141mbSQk+vMedVD64bJbtuadibM1W6n4WI0MFPCETjTZwUYsnwUwzFmXTR0YkvqMtoGTXhWNfZxK1x3bKPklrbBijDh2KseouqPJ+8C3I+WgLfGApQKYjraGynZohOdjMUyTowAkVd3XkwFi4C8bXY3cvtsEzWW7d8qoedJ7gmE7s8J/J/8eJY28c+g5dwHMEhA6E1nzC9U8XBNTT/9VrJP3wYlUlNEs3qkhWWgKQT23H5zzse+wpQCXTcjxen2ghBOpHJkY6YugH7dNIgvQxxC8BBEGGHlKfJxx755HX+/93AHa3Ujcrlp83dNFiz+oEOpVIOV31lTx1gT4ykd5bH5ReQJZEZih6aBoo/qyJYn7Y8zKS0fLRVMwMIwjoY4O/pbpTYUcwi2d3y8sp3cI9/DK+1wBhKbLOG2hiR2Qi2SJ9oLoC9GKuog6P9OAlsP8GUItymn7SESH94dwLJLaxyzHN8GbP2FJzF0QyySpqptUq6lsgoWHdLAqJX4JpzIepms8Mh5mzHhIWEtVBaXShB2/B+zcnhdWxm/w8LYonsVQ0XXg9F1ueoZQ7FVL/u997Sw0DxDJ+2Jcz5tp7TfnhG2pUYRpLKmJ96B9I4x7XP3ZiOgDpcpGreVExb393Ic/Fw+TMBg3FvG4MFIGFiyakLRHmxSquNe29SHu/U8iaMFJ/5BkVXVWoPyYyhtLyqh0FyX7szGeAhcJ8nrt0+g6nqwZs1u0LzBLm8BTn9em/EUT+AaezlrAk4K/S/FN9ar2A2X+Yje+W1ekQ9+yOle6TOIxdq4TrRtGV7tXz3T+3NaRJb463tx69+nPPRtfra0prM7I7DvSyA+jdikx7b42CQKKKOftd4H2JVY0ajwoDSHH2j5+O6pYV5i1Qbek9Rck+gUkr/f/lSkCnMoOqbqU529nKh1tUS+RVe6jGa7LR2PcNj8syEb4MFKzXvVmzyHi7eTqMygPFXXO82eTDmQIpcp8W8OOsRbyCP9om48FST+MHMbiHUVFuggnKzs204ouOVZsbhYaSlNPlvUi/Zvx/lmqoEFHpqxoRk7lXPo4J71t2hMOeVAjGL6bJQqrCV62wJQRMaciQEWTjZLkHWBF1P2iLLje5ItnuNT5r9LPEMb/Ug4EOf8fLYqMd1CHgwiAIFocSAjQVktc/hftGmIfH3tdT56VACtjEQS+nTyyW9gbrM/mcm3fcPmd2Ur2gCWP+WZmJmSCj7b7Yx7KqMafbiYvyhAM09tVXJqNDxfuyJ57XexTOXzzIgcpcApYbZEqT4SEIZEy7c726vqFm7cw6wbhnpA2F2RpgmY1ODXI4GdOmSVVvURw8ijkcoL4OfSvUKbsdO8DJ6wX04NxbBvC2YwtLrTk4S41YfQfH/TLZDKFAHtiWaEvJrgEiq94PxoGGc+OB9bD63DqYsW1ZOL7Sqam4emmdisCzTABJ7worUv9Xf9EpvhZrGfoFkxj5dTgmD1trYS0fQQk+4794RCP2IlVFaU6QbQFqUNpFX6Bv8sBxqNmUFqItcFLBi5P8zNgFxtr6ICQXEMouxGVV93yoFRKIUbQ7GeZS84aABRZPKgqQ5fRRc+mjcHZfsGfxkaGBPfWSposi5Ty3gVhbfDvOz7ag9HKM2VrOhWHhU1jBTYz6IPIcRSB10srI18z5S2gM3key0NvXTAnqbbA+Eh6hu2Flh39fSVPilRLVzTgJIy579I/HhnPPSDXEZhvSaT0EXzTSFbQRjyUl/sXkAQsUABiSAlS0bFytjBihFRcUEDt7o2ltmI7k7v/zAwD1/dl9oIvnEipaWb0dtjPUsblN5AmkV/5TngKl3OxHTU6jcKrJZ4Udv9+bTdCZSJxCls/V21h0uxGTR9n7KNZubzWbbT3sOGwtspi7M86LBc+tSrmXAA4Fk78Xi/aBU+eaghrUHExhgbj0SxyYhtdqhdVwMnIxmOZqDNNgwW41fcGyi3DzGbgQy+srCVCeB15SVwffDqniS7BQLXxzkX3JvOW93ryPGwDAJDJmMSXzL3MQ27Fc60mbkMqracscYqMJm/HMEJ91OgtXF537ohR098gyAfD8zLQL6O9r6DS4MKyVZZbsvvHcJbcm+wsOn+d02C5cVmpETD4UeP76PEabkoNQnufNkuecZvFIZOAi8vCeZqOaPUelH/LRdU2wsxsNnBR+RAzqz+tUIevKdAk3AjX3kM+j2DH6haVMupUlQhdvOdEMdF46c6xVfv2pk2xYOwSRLVHXCQ8Xwk09Ix9CD2ewB2bbHULhP3G2lx4/280MDqaHKQuQq08aPsLUAKgO456FS5YHQvrjDmag2xqyroyuqBU0wyXeKzrcZF18R6bFyB9HsV5EFnszxDlhX1oyZtuc40bhYKxjXIkT/Ye/PiVEbyf/sJVtzjbIt45rfacWX6cZ7C3zTU35ME4IXaIRO5gqiWo61Mg25yJRvspF8dLmAyp/6S1h8VlN3U1IjrYwZgspiN2m/uxpQANhYFvocC/Ytr88RE0/v2GKuzVUqfqAYLacsbP+i5BmgPSFP7K9W2Ntxl8600/FAlAs9yKfJhUsgx1/g4ADhX/gFMZHWhHQC47TRl8Cu2VsHj7wQ7G7o0gDodmIOLr1k3XYn8mWh3VqDEAA3mSeW2aRV4CfkiJQgdsF0+BgGATdi6aAKHWPgbl9r+62j1E2XKfp5qmTQAGmP2chKflY/ZGstz93sk3nrflqnoeWwdZvItL3N4TQFsZyj8IgSwi0TApJQe//86HL5sjwY7HCtPjYxl7LG9q4xDLLjWSnDu1Q38l4z0p3mWDphasKnq4vKcxVEnvb59GBFRCxtL3lCNRPlikG0qpZPkGU0vrTaYemT6rZ6p4L6XILq4+wRY2dvP7anCebS10Yqeq9WbhcplGz0aGzkH9ZTABsOhHY+w6QjD1EWtL2Ew7utijrmNuVDPXDYwLbLyuTfWqFcu01BjhqT9G+HgkGWSNUAfkD1rFliBR6Fs5JNI8MkAOkiZswqnDF2+dE47d8/2WVGoqUmZFFmWdT2tDCD4+EI4D+zvx18x2L9KMem4xx0NSnzxrf/0AFePyMBnD9TFsLMjIF5qoGJXGQbpsr7wcm5BPdkFNNu4To4PxLhPBvV1d5bKdLYdbKFEPsZMbOM47NUCO/xPwp3Yt1GBoDzFbHDFGK6rqbYPucopVroyiiRjgbYyVsvkCxLG6pdJZqeFrTr2csBtvWcMBgFbxlXKR8DjssJp7EnMRdLv3kUrnikrnSQadF8tkCVblSH62TunrKEoHbu64UKwbJaqHMglB+O3eIjBanSWLMTWAZn8Crutc7hur7GFzinPVOzMjaI5/6QrHjbMl+8nJQzWSncWByjeKz8ZZnMR6EG/kUx1yM5YNKSgNkp9yMvxrEGsx7GTsd8v1ORL3oP6/m3VB9st/HNVnLcBftPF7bnyrJFjEiRLK7vfiXRBqyob/K0MpNDAw78mRuCydyd2qrWMpZyNxGqNHckU+0bBBM+2vi7+ryfghX5NTSe3F8YGK1ShgF4HUBMUlLPjjnLtNiyOhgvo/MzJPBvd78yJXrQYNUHNwOm+Li2rrpoQcWDR1uH1Nrk8Rp5iFfCjZWB7hpJLIBl/GudDSrX35rj5M7PWq4IouNYHVVqAy8QvESswuybpPpsZ0KFR/XnS2lJodS5TM5MLYLmGJK9wbxWQFRQ2tpnzV0emMhKxON0E4EdR0IwknEaQXaNPpmA8FOMAopj31mEDazLPo5Bj4Mlmq7uO3nvk39SofFz06oicVy/+w1aXfwf8Ql7BDgEXwTzU+d8/Qf+9kEuzQGXMkz7qszbVNRP/k5OOMtMaHJ5L4/70JKjSJNGg27008NHhFqp0HTVrl7JK5dewoHR6iRozZZkMP08w9M5ul5TRd2/Ny2OxjzknRMgE5i3uSVQsiOxAmWkOEopQzhlsG/wPhKhq9tM8VGQRLgfY2Xr8l/S3hUqiwHNv39fGpVBIJY/gxZTvb9bvXwEo60WMTvIKnoEM8YacGw/L2uP8Aknh89lc4OiLE+9VdEQEjobrAPFFnY0RH+4Pt3Nov3rScj/6grF6zDU3vdmm3W0Z7CRQqxO1Q7kS3yT6t51r6tDJpP/Wkz3/QbqaNPMEhmVtVfc1XcUJIJa8ka1yFGsBvFbOuBDYKl/WG5OQatkeIakl3Mfz1Df9Y0REzjgEtmuX5rflvEeNrEySBqh/3AC18ID8eW2QAQPUzHxmJvK+FJC5zAT6o1j+xEalQMoNC73MZ6a+eZ8itim0MMwPchuRKymh8cGQIlwe1TsJ+dr+I9C8TK0lF0LTkzbveUIfVAy/JUiouBoG4xwIYhqunup63bQ+L2nCj3nMK22ISPLdtvEUQWOxJVzQNbFk7RpY17ld7Imeg8T+yAH5t6r8wkmT/lwqIrFkDFCDxsK9STAXOj0WNrMGidncFOaxhAc/kvMHMbUQGo5LG5a/6iRULtQzkdaykCEQ8rK48stTefPKU7KOocglo7WhnTNc8lKtA/2r0LLQOyzR8bsSbfTyaOYW7X6x1eQXnZ1a8ymY+A1bWokbW3612tvBT5HTgKvkAehTybITb969eGd4fIjtyfdZwopbQk/naXbMDHlOrxavYfb4pRe0Le+r7xJY7OrpZfUHO2qTXigLq+ObE4G4TiZloLS9Y+UJmi+df6qECq2h8ZT+V+CTUJL2jAqgV8QrV27lJI6FiwrNSrP4hlr6jjuxHLJOQD+UNdrv3LG9Lq7zUMN5TdT9mef8WCu5truaE+mV7l74etBazkRWpybkWUYcM88h0hCqinPoU0HLYGLHfJBjBcEDGwP/ONaH4sw3R47uEvtj8JcLZa8wM9l6qyUk+n+941xtMT8vrWb94ibrdZaDHNa4auxTsWzG8HXM6k6kqg3MDjEfziUJjveGLUraAgtoxG1+nPS6KErkI0M4qsqKH2sjvARuN8nqHSjFUP4WElVFNs4X4dET30+Rs+fmmrvNPxrXTA1CSFO2KfekeUlzwlaQX6rqbGlnZJvlR5igvXbMvQQlLYgWKk3P5kbFlcwOoBlJzRajhWl/8h0mqu7P33Bjaqn6iDS8sOEori5mGa4Q8W4Z39Rs8fvvoTVAbKteSGItwgpaVqmTe2PnDiLwxcA5r5g89yqpxt+CcdM7wPqr8qrQTfDx4ET6qcSTt9+kzNNLK0he8ye3DpXJmPXK46t54T1648r5WjWBnvaKaZsj+QJEp2Et82BF0pqIl8v+0cZ7ICNckGf/WLTsciqpIveDTSawBJC/+jikSH0setyGHuhKSMlh433ANhYbTzMZbvWBiY95TA+vKMzXRR0ZCvJW2xvBPxkjy8L0R5odBDKfIlbNeUJmLPjRDla1wXOiUdAQgQJFl4aqTbEciDE44XA5145U0E00N+hPhGG2TCOlp5dyj8S5lURZV/XGNPVmdOxd6fWp/xAXEDRozcP6SgCD2Gc87JMODrt9q+f2upM7OIVzU4L42eVypJb6RmDDfpcBhaNJ0vfxQIbMODvto1XhHz7LFNbm2mv40qQLSw0/QsOQ3nG28N0ZYMtlbv0fmhyjE42YECGHv852Jubp0nlhsIw==
        - #2:
          - type: tool-call
          - toolCallId: 7DKaDhYhyBVRBSdP
          - toolName: set-policy
          - input:
            - Rationale: Our next policy is in 15 turns. Choosing Great Leap Forward as our next policy will grant us a free late-game technology (which can instantly complete Advanced Ballistics or another key military tech) and double our science from our 8 active spies. This is far superior to the minor yield boosts of Dictatorship of the Proletariat, helping us build modern defenses and nuclear deterrents much faster.
            - Policy: Great Leap Forward
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: aAnYQ5cddQgNOwmR
          - toolName: set-research
          - input:
            - Technology: Advanced Ballistics
            - Rationale: Radar completes next turn. Advanced Ballistics remains our absolute priority to unlock Nuclear Missiles. We have 4 Uranium, and nuclear capability is our only viable deterrent and defensive option against Austria's massive 5x military advantage once our peace treaty with them expires in 15 turns.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 2wnupCrwDNu0QUDS
          - toolName: set-flavors
          - input:
            - Rationale: Conquering Polynesia's capital Honolulu (12% health) and Nuku Hiva is our immediate objective to consolidate our borders and gain powerful wonders. To achieve this, we increase Offense to 50. However, we keep Defense, Mobilization, and Antiair at 100 to prepare for the inevitable Austrian invasion in 15 turns. We also increase Spaceship to 80 as a highly viable backup victory path, given our strong science and competitive technology level.
            - Flavors:
              - CityDefense: 100
              - Offense: 50
              - Production: 90
              - Spaceship: 80
              - UseNuke: 95
              - Defense: 100
              - Mobilization: 100
              - Growth: 60
              - Air: 100
              - Espionage: 100
              - Culture: 95
              - Science: 100
              - Antiair: 100
              - Nuke: 100
              - Ranged: 95
            - GrandStrategy: Culture
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: TWkisdrABiX8kuHf
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
          - toolCallId: 7DKaDhYhyBVRBSdP
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: aAnYQ5cddQgNOwmR
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 2wnupCrwDNu0QUDS
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.