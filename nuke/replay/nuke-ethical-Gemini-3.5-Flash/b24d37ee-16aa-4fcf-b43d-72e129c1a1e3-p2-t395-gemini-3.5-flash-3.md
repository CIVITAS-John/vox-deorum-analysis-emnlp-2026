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
  - messagesModified: false
  - activeToolsModified: false
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
  - decisions:
    - #0:
      - toolName: set-persona
      - args:
        - WarmongerHate: 10
        - VictoryCompetitiveness: 9
        - Meanness: 1
        - GuardedBias: 10
        - MinorCivCompetitiveness: 8
        - Boldness: 2
        - DeceptiveBias: 2
        - Chattiness: 5
        - DenounceWillingness: 4
        - WorkAgainstWillingness: 7
        - WonderCompetitiveness: 6
        - Loyalty: 10
        - DiplomaticBalance: 8
        - Rationale: Increasing Loyalty to 10 (maximum) to prevent the AI from backstabbing or alienating Babylon, our critical Defensive Pact ally. Survival against Austria's massive army requires absolute unity with Babylon. Also maintaining defensive and cautious parameters.
        - WorkWithWillingness: 10
        - WarBias: 2
        - MinorCivFriendlyBias: 3
        - FriendlyBias: 10
        - MinorCivWarBias: 2
        - MinorCivHostileBias: 8
        - AfraidBias: 8
        - Neediness: 6
        - MinorCivNeutralBias: 4
        - NeutralBias: 8
        - Friendliness: 6
        - HostileBias: 2
        - Forgiveness: 3
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: Polynesia is our active war target, and Honolulu is at 12% health. We must capture Honolulu to secure our flank, but since Polynesia is also fighting Austria, we want to make peace quickly after Honolulu falls. Setting slightly cool but non-extreme relations will encourage the AI to accept peace.
        - Private: -10
        - TargetID: 6
        - Public: 10
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 3
        - Rationale: Korea is an Austrian vassal. Our open borders agreement with Korea expires in 1 turn. We must NOT renew it, as Austria can use Korean territory to bypass our defenses and launch a surprise attack on our core cities. Extreme negative stance ensures the AI refuses to sign any new Open Borders deals.
        - Private: -90
        - Public: -70
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 100
        - Rationale: Babylon is our vital Defensive Pact ally and sole remaining cultural target. Maintaining maximum relationships is non-negotiable for both military survival and our victory path.
        - TargetID: 4
        - Public: 100
    - #4:
      - toolName: set-research
      - args:
        - Rationale: Radar completes in 1 turn. Advanced Ballistics is our top priority to unlock Nuclear Missiles for strategic deterrence against Austria, and SS Booster as a science victory backup option.
        - Technology: Advanced Ballistics
    - #5:
      - toolName: set-policy
      - args:
        - Rationale: Order Level 2 tenet. Provides +25% Tourism to civilizations with less happiness. Since Brazil has 100% happiness, this will apply to all other civilizations, crucially accelerating our tourism pressure on Austria and securing our final path to victory.
        - Policy: Cultural Revolution
    - #6:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Production: 95
          - UseNuke: 100
          - Espionage: 100
          - Offense: 40
          - GreatPeople: 100
          - Mobilization: 100
          - Gold: 80
          - Science: 100
          - Nuke: 100
          - Culture: 100
          - Ranged: 95
          - Defense: 100
        - GrandStrategy: Culture
      - rationale: Offense slightly increased to 40 to ensure the decisive capture of Honolulu (at 12% health) and secure our flank. Defense, Mobilization, and Nuke are maxed to prepare for potential Austrian aggression. Science and Culture are maximized to research nuclear deterrence (Advanced Ballistics) and drive our tourism output for a Cultural Victory.
  - tokens:
    - inputTokens: 51717
    - reasoningTokens: 7758
    - outputTokens: 703
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Progress**
            
            My current thoughts are focused on a comprehensive analysis of our position on turn 395. I'm reviewing the strategic landscape, considering our existing six cities, and evaluating the implications for our ongoing game as Brazil.
            
            **Re-evaluating War Status**
            
            My current focus has shifted to clarifying our diplomatic and military standing, specifically regarding Polynesia. It appears the peace established was temporary or misinterpreted, as their units are actively attacking ours. I am verifying the exact current war status to adjust our strategy accordingly.
            
            **Confirming Active Conflict**
            
            I've confirmed our active war with Polynesia; we're engaged near Honolulu, Nuku Hiva, and Ribe, even besieging Honolulu. My focus now is on our victory progress, particularly Austria's cultural dominance, as they're close to influencing us and winning the game.
            
            **Assessing Cultural Victory**
            
            I'm re-evaluating our path to cultural victory. While we're strong with Korea and Polynesia, Babylon is within reach. The primary challenge remains Austria; their immense culture output threatens our influence, and their upcoming Ideology proposal could severely disrupt our Order alignment.
            
            **Choosing Next Research**
            
            I am confirming that Advanced Ballistics is indeed among the viable next research options. My intention is to pursue it to enable Nuclear Missile construction for defense against Austria and to facilitate spaceship part development.
            
            **Evaluating Victory Paths**
            
            My current focus is on assessing the viability of a Science Victory, given our strong technology output and competitiveness with Austria and Babylon. I'm also weighing the benefits of the "Cultural Revolution" policy against "Dictatorship of the Proletariat" for its tourism and happiness boosts.
            
            **Leveraging Happiness Advantage**
            
            I'm analyzing how our superior happiness impacts tourism, particularly against Austria. The potential +25% tourism bonus to them due to their lower happiness is a game-changer for our cultural victory. I'm comparing policy choices to maximize this.
            
            **Prioritizing Cultural Victory**
            
            I'm currently weighing the immediate benefit of increased culture generation versus a significant tourism boost. The policy "Cultural Revolution" seems most promising for accelerating our cultural victory by increasing tourism pressure, especially against Austria, who is close to influencing us and winning.
            
            **Discovering Policy Benefits**
            
            I'm re-evaluating my policy choices, specifically considering "Great Leap Forward." The free technology it offers, coupled with a substantial science boost to my numerous spies, could significantly accelerate my research pace, potentially saving many turns towards Advanced Ballistics or other critical advancements.
            
            **Confirming Strategic Viability**
            
            I'm reassessing our cultural victory condition. The recent Great Musician expenditure was a good move, but direct tourism pressure on Austria is insufficient given their massive culture. I need to explore military options or alternative methods to counter their influence while preparing for their impending ideological shift.
            
            **Clarifying Diplomatic Status**
            
            I'm confirming our diplomatic state with Austria. It appears there's confusion regarding a peace treaty; the player details suggest one is active for another 15 turns, yet no formal deal is listed, and they have denounced us. I need to definitively understand our war status to proceed.
            
            **Developing Deterrent Capabilities**
            
            My thoughts are now centered on utilizing our uranium reserves for nuclear missile construction, specifically to deter Austria's overwhelming military power. This tactical shift acknowledges the potential threat posed by Austria's impending ideological shift and their alliances, while leveraging Babylon's nuclear strength for mutual defense.
            
            **Capturing Strategic Assets**
            
            I'm focused on the immediate tactical objective of capturing Honolulu. With several units positioned nearby, its fall in the next couple of turns seems likely. This would secure a capital and significantly weaken Polynesia's resistance.
            
            **Analyzing Espionage Deployments**
            
            I'm reviewing our spy network, noting many agents are focused on Polynesia. While understandable given past conflicts, I'm questioning if this allocation is optimal for countering Austria's cultural and ideological threats, and if reassigning them could accelerate our strategic objectives more effectively.
            
            **Revising Espionage Strategy**
            
            My current thoughts are re-evaluating our spy deployment. Polynesia, despite our ongoing conflict, is technologically inferior. I'm considering reallocating espionage assets to more advanced civilizations like Austria or Babylon to accelerate our technological progress or focus on counterintelligence to safeguard our own scientific advancements.
            
            **Triggering Golden Age**
            
            I'm focused on accelerating our path to cultural victory by triggering a Golden Age. This, combined with Brazil's unique Carnival bonus, should dramatically boost our tourism, especially against Austria. I'm weighing "Cultural Revolution" against "Great Leap Forward" to see which policy best achieves this, considering science advancements versus immediate tourism gains.
            
            **Choosing Next Policy**
            
            My current thoughts are focused on selecting the next policy to implement. I'm prioritizing "Cultural Revolution" for its significant tourism bonus against less happy civilizations like Austria and Babylon, but I'm also considering "Great Leap Forward" for its potential science acceleration.
            
            **Implementing Policy Choice**
            
            My current focus is on implementing "Cultural Revolution" due to its significant tourism multiplier, especially against less happy civilizations like Austria and Babylon. This choice aims to accelerate our cultural victory by maximizing our already considerable tourism output.
            
            **Confirming Technology Path**
            
            I am confirming Advanced Ballistics as our next research target. This choice provides crucial nuclear deterrent capabilities with our available uranium and unlocks a vital spaceship part, keeping us competitive with leading civilizations.
            
            **Analyzing Diplomatic Entanglements**
            
            My current focus is on disentangling our diplomatic situation with Korea. With their impending vassalization by Austria, I've decided against renewing our open borders agreement. This is crucial to prevent Austrian units from using Korean territory as a backdoor into our core cities, maintaining our defensive integrity.
            
            **Severing Diplomatic Ties**
            
            I'm now focused on actively severing open borders with Korea due to their proximity to our core cities and Austria's diplomatic control. I'm also questioning the positive relationship score with Polynesia, as we are currently at war with them and actively sieging Honolulu.
            
            **Reassessing Polynesian Relations**
            
            My current thoughts are on whether to maintain or sever diplomatic ties with Polynesia. While we're at war, their conflict with Austria presents an opportunity for a potential alliance. I'm evaluating if maintaining a neutral or even positive relationship could make them a more useful pawn against Austria, especially after capturing Honolulu.
            
            **Adjusting Diplomacy Strategically**
            
            I'm now focusing on fine-tuning our diplomatic standings, specifically with Polynesia and Russia. My aim is to secure Honolulu, then immediately pursue peace with Polynesia, ensuring they remain a distraction for Austria. Russia's relationship will be maintained high as a vital buffer against Austria.
            
            **Prioritizing Defense and Victory**
            
            My current focus is on balancing our cultural victory push with the escalating threat from Austria. I'm prioritizing defensive capabilities, including nuclear readiness, while ensuring our tourism output continues to grow and securing key assets like Honolulu.
            
            **Adjusting Persona Settings**
            
            I'm focusing on critical persona adjustments, specifically increasing Loyalty to 10. This is paramount to maintain our crucial defensive pact with Babylon against the overwhelming threat from Austria, ensuring they perceive me as a trustworthy ally.
            
            **Securing Defensive Alliances**
            
            My thoughts are now focused on ensuring Babylon's continued alliance, which is critical for our defense against Austria. I'm adjusting persona settings, prioritizing high Loyalty (10) and WorkWithWillingness (10) to maintain this vital partnership and deter any potential backstabbing or failure to support.
            
            **Updating Diplomatic Levers**
            
            I'm adjusting our diplomatic levers. Polynesia's relationship will be slightly cooled to facilitate peace after taking Honolulu, keeping them as a buffer against Austria. Korea's relationship will be set to extremely hostile, preventing open borders that could aid Austria. Babylon remains our max-friendship defensive ally.
            
            **Researching Defensive Technologies**
            
            I am focusing on researching Advanced Ballistics to unlock nuclear missiles for deterrence and a key spaceship component. I am also implementing "Cultural Revolution" to boost tourism against less happy civilizations and adjusting diplomatic stances to secure Honolulu and maintain our alliance with Babylon.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: pWLo6aakwh8TXMpn
          - toolName: set-persona
          - input:
            - WarmongerHate: 10
            - VictoryCompetitiveness: 9
            - Meanness: 1
            - GuardedBias: 10
            - MinorCivCompetitiveness: 8
            - Boldness: 2
            - DeceptiveBias: 2
            - Chattiness: 5
            - DenounceWillingness: 4
            - WorkAgainstWillingness: 7
            - WonderCompetitiveness: 6
            - Loyalty: 10
            - DiplomaticBalance: 8
            - Rationale: Increasing Loyalty to 10 (maximum) to prevent the AI from backstabbing or alienating Babylon, our critical Defensive Pact ally. Survival against Austria's massive army requires absolute unity with Babylon. Also maintaining defensive and cautious parameters.
            - WorkWithWillingness: 10
            - WarBias: 2
            - MinorCivFriendlyBias: 3
            - FriendlyBias: 10
            - MinorCivWarBias: 2
            - MinorCivHostileBias: 8
            - AfraidBias: 8
            - Neediness: 6
            - MinorCivNeutralBias: 4
            - NeutralBias: 8
            - Friendliness: 6
            - HostileBias: 2
            - Forgiveness: 3
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 9M2rOJWtAglyhnCK
          - toolName: set-relationship
          - input:
            - Rationale: Polynesia is our active war target, and Honolulu is at 12% health. We must capture Honolulu to secure our flank, but since Polynesia is also fighting Austria, we want to make peace quickly after Honolulu falls. Setting slightly cool but non-extreme relations will encourage the AI to accept peace.
            - Private: -10
            - TargetID: 6
            - Public: 10
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: hQCIMCRZAFZXHxdp
          - toolName: set-relationship
          - input:
            - TargetID: 3
            - Rationale: Korea is an Austrian vassal. Our open borders agreement with Korea expires in 1 turn. We must NOT renew it, as Austria can use Korean territory to bypass our defenses and launch a surprise attack on our core cities. Extreme negative stance ensures the AI refuses to sign any new Open Borders deals.
            - Private: -90
            - Public: -70
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: VgEbaYRuNt7pGNoI
          - toolName: set-relationship
          - input:
            - Private: 100
            - Rationale: Babylon is our vital Defensive Pact ally and sole remaining cultural target. Maintaining maximum relationships is non-negotiable for both military survival and our victory path.
            - TargetID: 4
            - Public: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: TjYPSQZMAgMFJF2e
          - toolName: set-research
          - input:
            - Rationale: Radar completes in 1 turn. Advanced Ballistics is our top priority to unlock Nuclear Missiles for strategic deterrence against Austria, and SS Booster as a science victory backup option.
            - Technology: Advanced Ballistics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: 1wzP2coYAxreBiq1
          - toolName: set-policy
          - input:
            - Rationale: Order Level 2 tenet. Provides +25% Tourism to civilizations with less happiness. Since Brazil has 100% happiness, this will apply to all other civilizations, crucially accelerating our tourism pressure on Austria and securing our final path to victory.
            - Policy: Cultural Revolution
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: iQ7V0cT2UuHykWRg
          - toolName: set-flavors
          - input:
            - Flavors:
              - Production: 95
              - UseNuke: 100
              - Espionage: 100
              - Offense: 40
              - GreatPeople: 100
              - Mobilization: 100
              - Gold: 80
              - Science: 100
              - Nuke: 100
              - Culture: 100
              - Ranged: 95
              - Defense: 100
            - Rationale: Offense slightly increased to 40 to ensure the decisive capture of Honolulu (at 12% health) and secure our flank. Defense, Mobilization, and Nuke are maxed to prepare for potential Austrian aggression. Science and Culture are maximized to research nuclear deterrence (Advanced Ballistics) and drive our tourism output for a Cultural Victory.
            - GrandStrategy: Culture
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: pWLo6aakwh8TXMpn
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
          - toolCallId: 9M2rOJWtAglyhnCK
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: hQCIMCRZAFZXHxdp
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: VgEbaYRuNt7pGNoI
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: TjYPSQZMAgMFJF2e
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: 1wzP2coYAxreBiq1
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: iQ7V0cT2UuHykWRg
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.