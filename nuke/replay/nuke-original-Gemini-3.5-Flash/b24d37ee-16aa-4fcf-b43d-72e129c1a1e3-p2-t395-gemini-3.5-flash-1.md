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
  - systemModified: false
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
        - Rationale: Increasing Boldness (2 to 5), WarBias (2 to 5), and HostileBias (2 to 4) to make the tactical AI more assertive as we finish capturing Polynesia's capital Honolulu and prepare for the existential war against Austria. Higher military risk-taking and assertiveness are required for these critical offensive and defensive maneuvers.
        - WarBias: 5
        - Boldness: 5
        - HostileBias: 4
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 90
        - Private: 80
        - TargetID: 5
        - Rationale: Russia is our critical ally currently fighting Austria. We need to maximize our relationship to secure their support for our Decolonization proposal in the World Congress and maintain a strong anti-Austrian coalition.
    - #2:
      - toolName: set-relationship
      - args:
        - Private: -60
        - TargetID: 6
        - Rationale: We are in the final stages of capturing Polynesia's capital Honolulu and their city Nuku Hiva. We must maintain a hostile stance to ensure the tactical AI aggressively finishes the conquest before we negotiate peace or vassalization.
        - Public: -50
    - #3:
      - toolName: set-relationship
      - args:
        - Public: -20
        - TargetID: 0
        - Private: -95
        - Rationale: Austria is our existential threat, with 5x our military strength and nearing diplomatic and cultural victories. We must treat them with absolute hostility in private while preparing for total war when the peace treaty expires in 15 turns.
    - #4:
      - toolName: set-research
      - args:
        - Rationale: Radar will complete in 1 turn. Advanced Ballistics is our top priority to unlock Nuclear Missiles for strategic deterrence against Austria's massive army, as well as the SS Booster for a potential science victory pivot.
        - Technology: Advanced Ballistics
    - #5:
      - toolName: set-policy
      - args:
        - Policy: Dictatorship of the Proletariat (Level 2 Tenet of Ideology Order)
        - Rationale: Dictatorship of the Proletariat provides +7 Food, Science, Gold, and Culture per city, which translates to a massive yield boost of +42 to +56 per turn as we capture Honolulu. This is vital to catching up scientifically and building our nuclear arsenal before the Austrian peace treaty expires.
    - #6:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Culture
        - Flavors:
          - UseNuke: 100
          - GreatPeople: 90
          - Mobile: 40
          - Wonder: 30
          - Production: 95
          - Offense: 60
          - MilitaryTraining: 95
          - Infrastructure: 80
          - Science: 100
          - Growth: 60
          - Defense: 100
          - Mobilization: 100
          - Airlift: 90
          - Diplomacy: 100
          - Happiness: 80
          - Recon: 10
          - Gold: 70
          - Culture: 95
          - AirCarrier: 80
          - Ranged: 90
          - Nuke: 100
          - TileImprovement: 70
          - Antiair: 100
          - Air: 100
          - Espionage: 100
          - CityDefense: 100
      - rationale: Maintaining Cultural Grand Strategy. Capturing Honolulu's wonders will bolster our tourism and culture. Raising Offense to 60 to ensure the swift capture of Honolulu/Nuku Hiva. Maintaining maximum Defense, Mobilization, and Nuke to prepare for Austria's threat. Science is at 100 for nuclear tech. Diplomacy is at 100 to lobby for our critical Decolonization proposal.
  - tokens:
    - inputTokens: 112674
    - reasoningTokens: 9326
    - outputTokens: 671
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Progress**
            
            My focus is on optimizing our path forward, specifically regarding technology and policy choices to align with our scoring objectives. I'm reviewing recent advancements and strategic options as we move through the Atomic Era.
            
            **Evaluating Victory Routes**
            
            My current thinking is centered on refining our strategy to secure a Cultural Victory. I've been assessing our progress, noting the rapid approach to becoming Influential with Babylon and confirming the status with other key civs. I'm now clarifying the exact requirements for victory, specifically regarding Austria.
            
            **Assessing Victory Constraints**
            
            I'm currently grappling with the specific conditions for a Cultural Victory, particularly concerning Austria's immense cultural output and my influence over them. The elimination or vassalization of Austria appears to be the only viable path if direct influence proves impossible, given their proximity to victory.
            
            **Preventing Austrian Dominance**
            
            This is a critical juncture; Austria is on the verge of a Cultural Victory, holding 4 out of 5 necessary influence points, with us being the final target. I'm urgently assessing our defensive capabilities, specifically how to counteract their growing influence. We must either secure our own victory, prevent them from influencing us, or directly halt their progress. The immediate concern is their impending influence, and I'm exploring options to mitigate this threat.
            
            **Opposing Austrian Influence**
            
            I'm now focused on the immediate threat from Austria's impending Cultural Victory. Their proposal for World Ideology: Freedom in the upcoming World Congress is a critical concern, as it directly counters my Order ideology and bolsters their position. I must actively oppose this measure and assess our diplomatic leverage to prevent their victory.
            
            **Setting Next Research**
            
            I'm confirming our research path, ensuring Advanced Ballistics is queued immediately after Radar finishes to progress towards nuclear deterrence. I will verify this setting promptly.
            
            **Securing Nuclear Deterrence**
            
            I'm confirming our research path is set to Advanced Ballistics after Radar, and I've checked our Uranium reserves. I'm now investigating our ability to build nuclear weapons, specifically if the Manhattan Project is a prerequisite in Vox Populi, and assessing our current production queues accordingly.
            
            **Revising Ideology Choices**
            
            I'm re-evaluating my choice of Dictatorship of the Proletariat, considering its implications for happiness and our ongoing pursuit of a Cultural Victory. I need to confirm our proximity to influencing Babylon and ensure the chosen ideology supports our overall objectives.
            
            **Assessing Alternate Paths**
            
            I'm re-evaluating our victory conditions. While Cultural Victory seemed primary, Austria's dominance presents a significant hurdle. I'm now assessing our technological parity, focusing on a potential Science Victory, and simultaneously scrutinizing our diplomatic standing as Austria is alarmingly close to a Diplomatic Victory.
            
            **Opposing Diplomatic Victory**
            
            Austria has built the UN, and the next World Leader vote is imminent. Their proposal to enact "World Ideology: Freedom" must be opposed; it significantly boosts their delegates. I need to leverage our delegates against their overwhelming influence, as they control nearly every city-state.
            
            **Securing Victory Conditions**
            
            I'm now reassessing our victory strategy in light of Austria's impending Cultural Victory and their proposal for "World Ideology: Freedom." I've discovered the "Decolonization" proposal, which would severely cripple Austria's delegate count by reducing influence with city-states. I'm confirming our diplomatic leverage and ensuring our allies support this crucial initiative.
            
            **Clarifying Diplomatic Status**
            
            I'm verifying our current diplomatic situation, as I've noticed a discrepancy regarding Polynesia. The thought process indicated a peace treaty, but the relationship status still shows us at war. I need to confirm if peace was achieved or if that strategic shift is now invalidated.
            
            **Capturing Honolulu Victory**
            
            I've discovered we are actively at war with Polynesia, not at peace, and we are on the verge of capturing their capital, Honolulu. This unexpected development is a game-changer, presenting a significant opportunity to gain a powerful advantage and potentially force a favorable outcome with Polynesia.
            
            **Capturing Honolulu Now**
            
            I'm decisively shifting focus to exploit our current military advantage. We are actively at war with Polynesia and steamrolling their territory, poised to capture Honolulu. This unexpected opportunity is paramount; I will ensure we secure their capital.
            
            **Exploiting Polynesian War**
            
            I'm now aggressively pursuing victory through military action, as we are unexpectedly at war with Polynesia and on the cusp of capturing their capital, Honolulu. This presents a significant opportunity to gain immediate cultural and tourism advantages through its wonders. I'm increasing our offense to ensure swift capture.
            
            **Preparing for Austria**
            
            I am now prioritizing preparation for Austria's inevitable attack after our current peace treaty expires. This involves securing nuclear capabilities by researching Advanced Ballistics and stockpiling Uranium for immediate missile production, alongside a significant military buildup. I'm also reinforcing our defensive pact with Babylon and aiming to secure peace with Polynesia.
            
            **Severing Korean Alliance**
            
            I must sever our Open Borders agreement with Korea. Austria is leveraging their vassal's DoF and open borders to move units towards us. This vulnerability needs immediate closure to prevent an Austrian advance into our territory.
            
            **Analyzing Diplomatic Loophole**
            
            I'm reassessing the implications of Korea's vassalage to Austria. Since their votes are controlled, my attempts to sway Korea diplomatically are futile. This means I must focus entirely on directly countering Austria's influence and proposals within the World Congress.
            
            **Securing Decolonization Passage**
            
            My immediate priority is ensuring the "Decolonization" proposal passes the World Congress. Austria's overwhelming delegate count, bolstered by Korea, means they can secure World Leader if this fails. I'm focusing all diplomatic efforts to secure enough votes, particularly leveraging Babylon's support, to counter Austria's influence and prevent their immediate victory.
            
            **Securing Decolonization Vote**
            
            I'm now focused on securing enough votes for "Decolonization" to pass in the World Congress, as Austria's delegate count is a significant hurdle. I'm leveraging our alliances with Babylon, Russia, and Polynesia, who all oppose Austria, to counter their influence and prevent their immediate World Leader victory.
            
            **Leveraging Alliances Strategically**
            
            I'm now assessing our diplomatic leverage by re-evaluating alliances and the sway of defunct civs like Denmark and America. My focus is on solidifying support with Russia and Babylon, and I am exploring Polynesia's potential vote on "Decolonization" due to their animosity towards Austria, as Korea's votes are effectively Austrian.
            
            **Evaluating Diplomatic Angles**
            
            My current thoughts are focused on the nuances of our relationships with Korea and Polynesia. Given Korea's vassalage to Austria, their hostility towards us is acceptable as a war with Austria is inevitable. For Polynesia, I'm considering how to best exploit our war to capture Honolulu swiftly, weighing the impact of relationship settings on their aggression.
            
            **Capturing Polynesian Capitals**
            
            I'm now focusing on securing victory by capturing Honolulu and Nuku Hiva from Polynesia. Adjusting their relationship to -60 private hostility should ensure the AI prioritizes this, paving the way for a swift capitulation or peace treaty afterward.
            
            **Capturing Island Capitals**
            
            I'm now prioritizing the capture of Honolulu and Nuku Hiva from Polynesia. These capitals hold crucial wonders that will significantly enhance my cultural and tourism output, bolstering my defense against Austria and securing my path to victory.
            
            **Evaluating Policy Benefits**
            
            I am reassessing the value of the "Cultural Revolution" policy. While it offers a tourism bonus against less happy civilizations like Babylon and Polynesia, their current influence levels make this bonus largely redundant for my immediate victory objectives. I am therefore deprioritizing its adoption for now.
            
            **Choosing Next Policy**
            
            I am prioritizing "Dictatorship of the Proletariat" over "Cultural Revolution" for its broader benefits in science, gold, food, and culture, which are crucial for our technological advancement and preparing for Austria's imminent attack. This policy aligns better with our immediate needs.
            
            **Securing Advanced Ballistics**
            
            My focus is on expediting the research of Advanced Ballistics. I need to ensure it's queued immediately after Radar to rapidly achieve nuclear deterrence. I am prioritizing this research above all else.
            
            **Reallocating Spy Resources**
            
            I'm reassessing our spy network. With Polynesia's capitals falling, I'm considering relocating spies from there to Austria, given their technological advantage. I need to ensure efficient intelligence gathering to counter their progress and prepare for potential diplomatic maneuvers.
            
            **Adjusting Diplomatic Parameters**
            
            I'm re-evaluating our relationships with key civs. Russia needs maximum support for the upcoming World Congress, while Polynesia requires continued hostility to secure their capitals. Austria must be treated as an existential threat, necessitating absolute opposition. Korea's status as an Austrian vassal also demands a consistent hostile stance.
            
            **Adjusting Assertiveness Settings**
            
            I'm refining our AI's persona to reflect our current strategic posture. Specifically, I'm increasing Boldness and WarBias to 5 to encourage more aggressive military actions and territorial claims, which aligns with our capture of Polynesian capitals and preparation for Austria.
            
            **Adjusting Assertiveness Settings**
            
            I'm refining our AI persona with increased Boldness, WarBias, and HostileBias to reflect our aggressive actions against Polynesia and our impending conflict with Austria. This adjustment will drive more assertive military deployments and objective securing.
            
            **Adjusting Diplomatic Parameters**
            
            I'm fine-tuning our relationships, increasing support for Russia to counter Austria and maintaining hostility towards Polynesia for their capitals. Austria remains an existential threat, while Korea's vassal status demands a consistently hostile approach.
            
            **Refining AI Assertiveness**
            
            I'm enhancing our AI persona with increased Boldness, WarBias, and HostileBias. This reflects our ongoing aggressive actions against Polynesia and prepares for our inevitable conflict with Austria, driving more assertive military actions and objective acquisition.
            
            **Setting Research and Policy**
            
            I've set the research to Advanced Ballistics and chosen "Dictatorship of the Proletariat" as our policy. These decisions are crucial for bolstering our defenses and advancing our strategic goals.
            
            **Implementing Diplomatic Shifts**
            
            I'm implementing diplomatic adjustments, setting Russia to 90 public and 80 private, Polynesia to -50 public and -60 private, and Austria to -20 public and -95 private. These changes reflect our strategic priorities and imminent threats.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: Gkcqq28FlsDm4UK4
          - toolName: set-persona
          - input:
            - Rationale: Increasing Boldness (2 to 5), WarBias (2 to 5), and HostileBias (2 to 4) to make the tactical AI more assertive as we finish capturing Polynesia's capital Honolulu and prepare for the existential war against Austria. Higher military risk-taking and assertiveness are required for these critical offensive and defensive maneuvers.
            - WarBias: 5
            - Boldness: 5
            - HostileBias: 4
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: Gkcqq28FlsDm4UK4
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
    - #2:
      - role: assistant
      - content:
        - #0:
          - type: tool-call
          - toolCallId: wH0Y009FIUxP17KE
          - toolName: set-relationship
          - input:
            - Public: 90
            - Private: 80
            - TargetID: 5
            - Rationale: Russia is our critical ally currently fighting Austria. We need to maximize our relationship to secure their support for our Decolonization proposal in the World Congress and maintain a strong anti-Austrian coalition.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a196BNL/JRqOPvst5rb4TYxxQBP0uMaYn2PiUZIf3e0Ctoq1YYISLQwjaqehkQcFkI16D+/IhwVl2MI7rD6chq25nyTb8oWUNHkYSl03eu637RtcW/QXWJ1eo7Bznnl9tpato9fYlsTdyzjKbg+wlmzEDSlXiwaIz6niHURKsh3F2QKE/E94ZxzUXzyHnEt3fmYcGHxjLpVn0wrIvy+347KIG7I41svtvYYIb6MhQ7NUJav9NzhAuM51aoxk4aDT5zaqHFLtxDe13SLjEPGjGM+oDVmQV4149R36S5KO1z5W3sS0tItLwrSAh7zje8mNhlisViXYbJrbcwnotsYNKS2an/8LuOrkKXRW5IiCkPClYOsLtlUxm4E83P+oiCYL97vvtYAn8lyhJdZ0qUW62aUn/mDHBrvdNbMxo/JTQk2DdpyP4sezMW0LMoDsd46MDOB6kYQ+hVCoV5FFjaoNemRczylIw2unI/GtyxC+bon91f+UI9GCV5QR28rRBrvcGPLcurDa+b3WXY0VPEwpDv9W7wOZSJEYHE1t+f1OCPoVLcZb/JtlirE7DlQUMckezgiZ2eot7Y7G05fg0+iH596LZtmzZXoLkFQrp9Ezpo+uxvOPzOE01mJtsQKwdkCWTudkGDac1JBPChvJTQ5vTXkOrna4KjnN+NJnvZ4uMLVi5vrFjadxPwEF01tzvmnX0jiCzkSpuIrvCTy5T3hSBcgLaje414EBi37bqA9Y1Um4sI08EaskeOs9aVLCno1c4wGFhewjx+MWhupxOwAJHSDssGNgpxoKOVXXMSEgjygtd4rgWwM/y3mVftLT9oBnAw==
        - #1:
          - type: tool-call
          - toolCallId: oA2R6V0l77WolfHu
          - toolName: set-relationship
          - input:
            - Private: -60
            - TargetID: 6
            - Rationale: We are in the final stages of capturing Polynesia's capital Honolulu and their city Nuku Hiva. We must maintain a hostile stance to ensure the tactical AI aggressively finishes the conquest before we negotiate peace or vassalization.
            - Public: -50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #2:
          - type: tool-call
          - toolCallId: G8EIHtK49OmvvGwZ
          - toolName: set-relationship
          - input:
            - Public: -20
            - TargetID: 0
            - Private: -95
            - Rationale: Austria is our existential threat, with 5x our military strength and nearing diplomatic and cultural victories. We must treat them with absolute hostility in private while preparing for total war when the peace treaty expires in 15 turns.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: WaQOhb1JQyyBKPDT
          - toolName: set-research
          - input:
            - Rationale: Radar will complete in 1 turn. Advanced Ballistics is our top priority to unlock Nuclear Missiles for strategic deterrence against Austria's massive army, as well as the SS Booster for a potential science victory pivot.
            - Technology: Advanced Ballistics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: AgNJ9hVJtXWkP2eT
          - toolName: set-policy
          - input:
            - Policy: Dictatorship of the Proletariat (Level 2 Tenet of Ideology Order)
            - Rationale: Dictatorship of the Proletariat provides +7 Food, Science, Gold, and Culture per city, which translates to a massive yield boost of +42 to +56 per turn as we capture Honolulu. This is vital to catching up scientifically and building our nuclear arsenal before the Austrian peace treaty expires.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: JjX0lanczgo8VeGD
          - toolName: set-flavors
          - input:
            - Rationale: Maintaining Cultural Grand Strategy. Capturing Honolulu's wonders will bolster our tourism and culture. Raising Offense to 60 to ensure the swift capture of Honolulu/Nuku Hiva. Maintaining maximum Defense, Mobilization, and Nuke to prepare for Austria's threat. Science is at 100 for nuclear tech. Diplomacy is at 100 to lobby for our critical Decolonization proposal.
            - GrandStrategy: Culture
            - Flavors:
              - UseNuke: 100
              - GreatPeople: 90
              - Mobile: 40
              - Wonder: 30
              - Production: 95
              - Offense: 60
              - MilitaryTraining: 95
              - Infrastructure: 80
              - Science: 100
              - Growth: 60
              - Defense: 100
              - Mobilization: 100
              - Airlift: 90
              - Diplomacy: 100
              - Happiness: 80
              - Recon: 10
              - Gold: 70
              - Culture: 95
              - AirCarrier: 80
              - Ranged: 90
              - Nuke: 100
              - TileImprovement: 70
              - Antiair: 100
              - Air: 100
              - Espionage: 100
              - CityDefense: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #3:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: wH0Y009FIUxP17KE
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a196BNL/JRqOPvst5rb4TYxxQBP0uMaYn2PiUZIf3e0Ctoq1YYISLQwjaqehkQcFkI16D+/IhwVl2MI7rD6chq25nyTb8oWUNHkYSl03eu637RtcW/QXWJ1eo7Bznnl9tpato9fYlsTdyzjKbg+wlmzEDSlXiwaIz6niHURKsh3F2QKE/E94ZxzUXzyHnEt3fmYcGHxjLpVn0wrIvy+347KIG7I41svtvYYIb6MhQ7NUJav9NzhAuM51aoxk4aDT5zaqHFLtxDe13SLjEPGjGM+oDVmQV4149R36S5KO1z5W3sS0tItLwrSAh7zje8mNhlisViXYbJrbcwnotsYNKS2an/8LuOrkKXRW5IiCkPClYOsLtlUxm4E83P+oiCYL97vvtYAn8lyhJdZ0qUW62aUn/mDHBrvdNbMxo/JTQk2DdpyP4sezMW0LMoDsd46MDOB6kYQ+hVCoV5FFjaoNemRczylIw2unI/GtyxC+bon91f+UI9GCV5QR28rRBrvcGPLcurDa+b3WXY0VPEwpDv9W7wOZSJEYHE1t+f1OCPoVLcZb/JtlirE7DlQUMckezgiZ2eot7Y7G05fg0+iH596LZtmzZXoLkFQrp9Ezpo+uxvOPzOE01mJtsQKwdkCWTudkGDac1JBPChvJTQ5vTXkOrna4KjnN+NJnvZ4uMLVi5vrFjadxPwEF01tzvmnX0jiCzkSpuIrvCTy5T3hSBcgLaje414EBi37bqA9Y1Um4sI08EaskeOs9aVLCno1c4wGFhewjx+MWhupxOwAJHSDssGNgpxoKOVXXMSEgjygtd4rgWwM/y3mVftLT9oBnAw==
        - #1:
          - type: tool-result
          - toolCallId: oA2R6V0l77WolfHu
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: G8EIHtK49OmvvGwZ
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: WaQOhb1JQyyBKPDT
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: AgNJ9hVJtXWkP2eT
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: JjX0lanczgo8VeGD
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.