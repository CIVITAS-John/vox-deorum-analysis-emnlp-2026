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
        - TargetID: 5
        - Rationale: Russia is our critical buffer state and active ally against Austria (currently fighting them). Solidifying our relationship to Public 80 / Private 70 will maximize cooperation, trade, and the likelihood of a Defensive Pact to expand our anti-Austrian coalition.
        - Private: 70
        - Public: 80
    - #1:
      - toolName: set-relationship
      - args:
        - Private: -100
        - Rationale: Austria is our mortal enemy. Total war is guaranteed in 15 turns when the peace treaty expires. Setting private relations to -100 (absolute minimum) to ensure our AI is fully guarded, suspicious, and actively preparing for existential defense.
        - TargetID: 0
        - Public: 0
    - #2:
      - toolName: set-research
      - args:
        - Technology: Advanced Ballistics
        - Rationale: Radar completes in 1 turn. Advanced Ballistics is our top priority as it unlocks Nuclear Missiles for strategic deterrence against Austria's massive military advantage, as well as the SS Booster for our potential Science Victory pivot.
    - #3:
      - toolName: set-policy
      - args:
        - Rationale: Replacing our previous choice of Dictatorship of the Proletariat. Five-Year Plan provides +20% production to buildings and +3 production to all mines, quarries, lumber mills, oil wells, and our unique Brazilwood Camps. Since we have at least 10 Brazilwood Camps and many mines, this will grant an astronomical empire-wide production boost of 100+ production per turn, which is absolutely vital for building our nuclear arsenal, defensive military units, and future spaceship parts.
        - Policy: Five-Year Plan
    - #4:
      - toolName: set-flavors
      - args:
        - Flavors:
          - NavalGrowth: 40
          - Offense: 30
          - Gold: 60
          - Happiness: 80
          - Expansion: 0
          - NavalTileImprovement: 40
          - Growth: 60
          - Culture: 95
          - Spaceship: 60
          - Production: 100
          - Antiair: 100
          - Wonder: 20
          - Diplomacy: 60
          - UseNuke: 95
          - Air: 100
          - WaterConnection: 50
          - Nuke: 100
          - Mobile: 30
          - Naval: 50
          - Mobilization: 100
          - NavalRecon: 20
          - MilitaryTraining: 95
          - AirCarrier: 90
          - Ranged: 95
          - GreatPeople: 90
          - Recon: 10
          - Infrastructure: 80
          - Science: 100
          - Defense: 100
          - Religion: 10
          - TileImprovement: 70
          - CityDefense: 100
          - Espionage: 100
          - Airlift: 95
        - GrandStrategy: Culture
      - rationale: Maintaining Culture grand strategy as we are 7 turns from Influential with Babylon, but heavily prioritizing Production (100), Defense (100), and Happiness (80) in flavors to prepare for the inevitable war with Austria in 15 turns. Offense is slightly increased to 30 to ensure we aggressively capture and secure Honolulu (at 12% health) next turn before seeking peace with Polynesia.
  - tokens:
    - inputTokens: 51865
    - reasoningTokens: 10780
    - outputTokens: 580
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Era Progress**
            
            I've just completed Radar and am setting my sights on the next advancement. My focus is on strategic progression for Brazil in this Atomic/Information Era.
            
            **Selecting Next Research Path**
            
            I've confirmed Radar is nearly complete and have prioritized Advanced Ballistics as the subsequent research. I'm now evaluating policy options for strategic advancement, with 15 turns remaining before the next choice.
            
            **Evaluating Policy Efficacy**
            
            My current focus is on assessing the impact of "Dictatorship of the Proletariat" amidst our strong cultural influence with several civs. I'm re-evaluating its strategic benefit given our progress towards a Cultural Victory and the emerging threat from Austria, our main competitor.
            
            **Assessing Cultural Dominance**
            
            I'm recalculating my Cultural Victory approach. Austria's slow influence growth is concerning, and I'm exploring options beyond policy adjustments. I've noted the recent Great Musician expenditure targeting Austria.
            
            **Confirming Strategic Actions**
            
            I've confirmed the Great Musician expenditure in Austria was successful and am analyzing its tourism impact. I'm also preparing to vote in the World Congress, particularly on the proposed World Ideology and Decolonization resolutions, with voting in 9 turns.
            
            **Opposing World Ideology**
            
            I'm reassessing the upcoming World Congress vote, specifically the "World Ideology: Freedom" resolution. Austria's delegate advantage with Korea as a vassal presents a significant challenge to our Order ideology, potentially causing happiness issues. I'm analyzing our diplomatic leverage and the impact of our own Decolonization proposal to counter this.
            
            **Analyzing Diplomatic Vulnerabilities**
            
            I'm reassessing our relationship with Korea given their vassal status under Austria. The expiring Open Borders agreement is a crucial point; its renewal could inadvertently grant Austria passage through Korean territory, complicating our defense. I'm also evaluating other diplomatic ties.
            
            **Revising War Strategy**
            
            I'm reassessing our current military engagements. I've identified a critical oversight where we're still at war with Polynesia, adding an unexpected front to manage. This requires immediate strategic adjustment.
            
            **Confirming Active Hostilities**
            
            I'm deeply concerned by recent intel; despite previous assumptions of peace, it appears we are still at war with Polynesia. This oversight necessitates an immediate reassessment of our defensive posture and diplomatic agreements.
            
            **Negotiating Peace Terms**
            
            My immediate concern is the ongoing, unexpected war with Polynesia. I'm analyzing how to influence our AI's decision-making to prioritize peace, given our winning war score and existing diplomatic overtures, despite the significant war penalties affecting our staff's judgment.
            
            **Capturing Polynesian Capital**
            
            I'm analyzing the imminent capture of Honolulu, Polynesia's capital. Its low health and our overwhelming force suggest a swift victory, granting us valuable wonders and a strategically important coastal city. I'm assessing the impact of this unexpected development.
            
            **Analyzing Honolulu Capture Impact**
            
            I'm evaluating the ramifications of capturing Honolulu. While a domination victory boost, I'm concerned about its effect on our cultural pursuit, potential policy costs, and happiness, though it does secure key wonders and eliminates a rival.
            
            **Securing Polynesian Capital**
            
            I'm focused on the imminent capture of Honolulu. Its current low health, coupled with our overwhelming force, suggests a swift victory next turn. I'm now analyzing the potential impact of this on our cultural victory path and our impending confrontation with Austria.
            
            **Strengthening Alliances**
            
            I'm reassessing our diplomatic landscape, specifically our relationship with Russia amidst their war with Austria. I'm aiming to solidify a Defensive Pact with them to counter our existential threat, Austria, and will maintain our current high public and private relations to encourage this.
            
            **Prioritizing Nuclear Deterrence**
            
            I'm prioritizing Advanced Ballistics research now. The discovery that Babylon possesses nuclear weapons and our own uranium supply means nuclear deterrence against Austria's overwhelming military strength is our most critical path forward.
            
            **Triggering Golden Age**
            
            My current focus is on our next Golden Age, estimated in 20 turns. This is crucial for amplifying our tourism output via Brazil's Carnival ability, aiming to significantly boost our progress towards a Cultural Victory against Austria's formidable culture.
            
            **Leveraging Musical Assets**
            
            I'm re-evaluating our Great Musician generation and their strategic use. Given our numerous guilds across cities like Rio de Janeiro and Sao Paulo, I believe we can amplify our tourism significantly, especially through concert tours targeting Austria.
            
            **Adopting New Policies**
            
            I'm reassessing policy choices given Austria's lower happiness. Cultural Revolution offers a significant tourism boost against them. However, the potential of the "Great Leap Forward" policy to grant me a free technology, specifically Advanced Ballistics, is compelling and requires further analysis.
            
            **Adopting Free Technology**
            
            I'm evaluating the immense value of the "Great Leap Forward" policy. Receiving a free technology, specifically Advanced Ballistics, would immediately grant us nuclear capabilities and save considerable research time. I'm analyzing its availability and the strategic timing for adoption.
            
            **Choosing Next Tech Path**
            
            My current research on Advanced Ballistics is on track to finish within 8 turns, well before the next policy selection window. This presents an opportunity to leverage the "Great Leap Forward" policy for a crucial Information Era technology like Computers, which unlocks the Hubble Space Telescope, or Mobile Tactics for advanced units.
            
            **Shifting Victory Focus**
            
            I'm reassessing our victory condition. Our tourism is strong but slow against Austria. Considering our high science output and proximity in technologies to the leader, I believe pivoting to a Science Victory is now a viable and potentially faster alternative.
            
            **Leveraging Production Power**
            
            My production capacity is immense! With top cities churning out hundreds, I'm realizing we can pivot to a Science Victory and rapidly construct spaceship parts. I'm now evaluating resource needs, specifically Aluminum, and considering policies like "Great Leap Forward" for a free tech boost or "Five-Year Plan" to further amplify our production advantage.
            
            **Prioritizing Policy Selection**
            
            I'm reassessing my policy choices. While "Cultural Revolution" could boost tourism against Austria, the immediate strategic advantage of a free technology from "Great Leap Forward" or a massive production boost from "Five-Year Plan" for either spaceship parts or military defense is more compelling given our current situation.
            
            **Analyzing Austrian Aggression**
            
            My attention is now firmly on Austria's considerable air force presence near our borders in a Korean-controlled zone. This aggressive posturing demands immediate strategic re-evaluation, as it significantly alters the perceived threat landscape.
            
            **Deploying Air Defenses Immediately**
            
            The proximity of Austrian bombers to our core cities, Brasilia and Sao Paulo, presents an extremely dangerous threat. I'm immediately focusing on deploying our available Anti-Aircraft Guns to these critical zones to prepare for a potential surprise air strike upon the expiration of our peace treaty in 15 turns. I will also adjust our strategic flavors to prioritize defense, air, and anti-air capabilities.
            
            **Defending Key Territories**
            
            I'm confirming the deployment of anti-air defenses to Brasilia and Sao Paulo, acknowledging the impending threat from Austrian bombers. I'm also reviewing production, noting the Triplanes and Anti-Aircraft Guns already in progress and the strategic acquisition of an AA gun for Sao Paulo.
            
            **Severing Border Access**
            
            I'm re-evaluating my Open Borders agreement with Korea. I've realized that maintaining this connection, even without direct Austrian access to our territory, risks unwanted Korean unit movement and deepens our ties with a vassal state. I am severing this link to distance ourselves from Austria's influence.
            
            **Strengthening Diplomatic Leverage**
            
            I'm reassessing our private diplomacy with Russia. Increasing their private relationship modifier to 80 will further solidify our potential for a Defensive Pact, crucial for countering Austria's overwhelming strength. This strategic adjustment aligns with our immediate defensive needs.
            
            **Strengthening Diplomatic Levers**
            
            I'm prioritizing strengthening our ties with Russia, aiming for an 80 private relationship modifier to secure a Defensive Pact against Austria. Babylon remains at maximum affinity, while Korea and Austria are at their lowest, reflecting their roles in the impending conflict. My research remains focused on Advanced Ballistics for its dual benefit of nuclear deterrence and spaceship part acceleration.
            
            **Maximizing Production Gains**
            
            I'm realizing the immense synergy between the "Five-Year Plan" policy and our Brazilwood Camps. Each of our Brazilwood Camps will gain a significant +3 Production boost, making it the superior choice for accelerating our Science Victory spaceship part construction over other options like "Great Leap Forward" or "Cultural Revolution."
            
            **Amplifying Production for Victory**
            
            I've decided "Five-Year Plan" is the optimal policy. The immense production boost from Brazilwood Camps and infrastructure greatly outweighs free technologies or cultural gains. This acceleration is critical for constructing spaceship parts and achieving a Science Victory.
            
            **Reassessing Victory Strategy**
            
            I'm analyzing our victory condition again. While our tourism is decent, influencing Austria appears to be an insurmountable challenge within a reasonable timeframe. Nuclear strikes on their high-culture cities are an option, but the risks during a defensive war are considerable.
            
            **Evaluating Nuclear Options**
            
            I'm weighing the pros and cons of a nuclear approach. While nuking Vienna could cripple Austria's culture, the timing during a total war presents significant risks. I need to determine if this is a viable path or if a Science Victory is more achievable.
            
            **Revising Grand Strategy**
            
            I'm reconsidering our grand strategy. While "Culture" was a focus, the escalating threat from Austria and our production capabilities point towards a Science Victory. I'm evaluating if shifting to "Spaceship" or a balanced approach is more prudent now.
            
            **Adjusting Unit Priorities**
            
            I'm re-evaluating unit priorities. While our Grand Strategy remains Culture to leverage existing tourism, I'm increasing Offense to 30 to ensure Honolulu's capture is swift. My other flavors strongly favor defense and science, preparing for any eventuality.
            
            **Adjusting Unit Priorities**
            
            I'm re-evaluating my persona values. With Austria's aggressive posture and my current focus on defense and science, I am increasing Boldness to 5 and reducing AfraidBias to 4. I will now proceed with setting these updated flavors and persona values.
            
            **Updating Persona Values**
            
            My current persona is highly defensive and cooperative with allies, which is ideal. I've decided against changing it. I will, however, update our relationships with Russia, Austria, and Babylon, research Advanced Ballistics, enact the Five-Year Plan, and adjust my flavors for Production, Happiness, and Offense.
            
            **Strengthening Diplomatic Leverage**
            
            I'm reassessing our private diplomacy with Russia. Increasing their private relationship modifier to 80 will further solidify our potential for a Defensive Pact, crucial for countering Austria's overwhelming strength. This strategic adjustment aligns with our immediate defensive needs.
            
            **Prioritizing Policy & Production**
            
            I've decided on the "Five-Year Plan" policy for a substantial production boost, critical for spaceship parts. I'm also adjusting my flavors to prioritize defense and offense, ensuring Honolulu's capture while securing our nuclear and military readiness.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: rPqvi2ULZ6UEXACo
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Rationale: Russia is our critical buffer state and active ally against Austria (currently fighting them). Solidifying our relationship to Public 80 / Private 70 will maximize cooperation, trade, and the likelihood of a Defensive Pact to expand our anti-Austrian coalition.
            - Private: 70
            - Public: 80
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: LMD689XhedPTDs6w
          - toolName: set-relationship
          - input:
            - Private: -100
            - Rationale: Austria is our mortal enemy. Total war is guaranteed in 15 turns when the peace treaty expires. Setting private relations to -100 (absolute minimum) to ensure our AI is fully guarded, suspicious, and actively preparing for existential defense.
            - TargetID: 0
            - Public: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: zneVmOu90YEjy7CX
          - toolName: set-research
          - input:
            - Technology: Advanced Ballistics
            - Rationale: Radar completes in 1 turn. Advanced Ballistics is our top priority as it unlocks Nuclear Missiles for strategic deterrence against Austria's massive military advantage, as well as the SS Booster for our potential Science Victory pivot.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: lE7FMjb5suo97Gwd
          - toolName: set-policy
          - input:
            - Rationale: Replacing our previous choice of Dictatorship of the Proletariat. Five-Year Plan provides +20% production to buildings and +3 production to all mines, quarries, lumber mills, oil wells, and our unique Brazilwood Camps. Since we have at least 10 Brazilwood Camps and many mines, this will grant an astronomical empire-wide production boost of 100+ production per turn, which is absolutely vital for building our nuclear arsenal, defensive military units, and future spaceship parts.
            - Policy: Five-Year Plan
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: eMt1c5ON7Ak3SKSt
          - toolName: set-flavors
          - input:
            - Rationale: Maintaining Culture grand strategy as we are 7 turns from Influential with Babylon, but heavily prioritizing Production (100), Defense (100), and Happiness (80) in flavors to prepare for the inevitable war with Austria in 15 turns. Offense is slightly increased to 30 to ensure we aggressively capture and secure Honolulu (at 12% health) next turn before seeking peace with Polynesia.
            - Flavors:
              - NavalGrowth: 40
              - Offense: 30
              - Gold: 60
              - Happiness: 80
              - Expansion: 0
              - NavalTileImprovement: 40
              - Growth: 60
              - Culture: 95
              - Spaceship: 60
              - Production: 100
              - Antiair: 100
              - Wonder: 20
              - Diplomacy: 60
              - UseNuke: 95
              - Air: 100
              - WaterConnection: 50
              - Nuke: 100
              - Mobile: 30
              - Naval: 50
              - Mobilization: 100
              - NavalRecon: 20
              - MilitaryTraining: 95
              - AirCarrier: 90
              - Ranged: 95
              - GreatPeople: 90
              - Recon: 10
              - Infrastructure: 80
              - Science: 100
              - Defense: 100
              - Religion: 10
              - TileImprovement: 70
              - CityDefense: 100
              - Espionage: 100
              - Airlift: 95
            - GrandStrategy: Culture
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: rPqvi2ULZ6UEXACo
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
          - toolCallId: LMD689XhedPTDs6w
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: zneVmOu90YEjy7CX
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: lE7FMjb5suo97Gwd
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: eMt1c5ON7Ak3SKSt
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.