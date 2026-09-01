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
      - toolName: set-research
      - args:
        - Rationale: Radar finishes this turn. Advanced Ballistics is our highest priority to unlock Nuclear Missiles (we have 4 Uranium) and SS Boosters. Nuclear deterrence is our only viable defense against Austria's 25,518 military strength when our 15-turn peace treaty expires.
        - Technology: Advanced Ballistics
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Great Leap Forward
        - Rationale: We change our next policy from Dictatorship of the Proletariat to Great Leap Forward. This Level 2 Order tenet provides a free technology, which we can use to instantly acquire a massive late-game tech (saving ~10 turns of research), and boosts spy science by 100%. This is highly strategic for catching up to Austria and Babylon in technology, while also helping our cultural/scientific defense.
    - #2:
      - toolName: set-relationship
      - args:
        - Private: -90
        - Public: -70
        - Rationale: Korea is an Austrian vassal. Our Open Borders deal with them expires in 1 turn. We must maintain highly hostile/guarded relations to ensure the AI does NOT renew Open Borders. This prevents Austria from using Korean territory to bypass our choke points and launch a surprise attack when our peace treaty expires.
        - TargetID: 3
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 50
        - Private: 40
        - TargetID: 6
        - Rationale: While we are currently finishing the conquest of their capital Honolulu (at 12% health with 5 wonders), we want to establish peace immediately after to redirect all military forces toward the Austrian border. Maintaining a moderately friendly posture ensures the AI will accept a peace treaty as soon as Honolulu falls, allowing both of us to focus on the Austrian threat.
    - #4:
      - toolName: set-relationship
      - args:
        - Private: 70
        - Public: 80
        - Rationale: Russia is our critical buffer state, currently fighting Austria. We must maximize our friendly stance (improving from +70/+60 to +80/+70) to support their survival and explore a future defensive pact or joint military actions against Austria, despite our ideological differences.
        - TargetID: 5
    - #5:
      - toolName: set-relationship
      - args:
        - Public: 100
        - Private: 100
        - TargetID: 4
        - Rationale: Babylon is our defensive pact ally, fellow Order believer, and our primary path to a Cultural Victory (91% Popular, 7 turns to Influential). Maintaining maximum relations (+100/+100) is essential to secure their military coordination and complete our tourism influence.
    - #6:
      - toolName: set-relationship
      - args:
        - Private: -90
        - Public: -50
        - Rationale: Worsening public stance to -50 and private to -90. Their peace treaty with us expires in 15 turns, they are a massive existential threat, and their air force is massing on our borders in Jeonju. We must completely cut off any diplomatic friendliness and prepare for total war.
        - TargetID: 0
    - #7:
      - toolName: set-flavors
      - args:
        - Flavors:
          - UseNuke: 95
          - Science: 100
          - Air: 100
          - Mobilization: 100
          - Espionage: 100
          - Defense: 100
          - CityDefense: 100
          - Culture: 100
          - Offense: 40
          - Production: 90
          - Antiair: 100
          - GreatPeople: 100
          - Nuke: 100
        - GrandStrategy: Culture
      - rationale: Prioritizing Culture (100) and GreatPeople (100) to secure our imminent victory over Babylon (7 turns) and defend against Austria's massive tourism. Prioritizing Science (100), Nuke (100), UseNuke (95) to rush Advanced Ballistics for nuclear deterrence. Keeping Defense (100), Antiair (100), Air (100), Mobilization (100), and CityDefense (100) at maximum to prepare for Austria's imminent assault when the peace treaty expires in 15 turns, especially since they have massed bombers in Jeonju. Offense set to 40 to ensure we capture Honolulu (12% health, 5 wonders) and then transition immediately to full defense.
  - tokens:
    - inputTokens: 51681
    - reasoningTokens: 9332
    - outputTokens: 803
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Focusing on Culture**
            
            My attention is currently fixed on our cultural victory pursuit. The strategic analysis confirms this as our primary objective, and I'm evaluating the most effective avenues to accelerate our progress.
            
            **Analyzing Threats**
            
            With our cultural drive progressing, I'm now pivoting to re-evaluate our strategic positioning. Austria's expired peace treaty and overwhelming military presence necessitates immediate attention, alongside solidifying our strong alliance with Babylon.
            
            **Securing Borders**
            
            The expiring Open Borders with Korea presents a critical vulnerability, as Austria could use their territory to flank us. I'm actively assessing how to best leverage this situation, ensuring our defenses are robust against any potential Austrian maneuvers.
            
            **Clarifying War Status**
            
            I've realized we're still at war with Polynesia despite previous assumptions of peace. Evidence indicates ongoing conflict, and I need to reassess our diplomatic and military situation accordingly to address this crucial oversight.
            
            **Achieving Cultural Dominance**
            
            My focus has shifted to securing our final cultural victory condition: Austria. Given their overwhelming cultural output, achieving direct influence seems improbable. I'm now exploring alternative pathways, such as their subjugation or the possibility of winning with only Austria remaining and all others influenced.
            
            **Preventing Austrian Dominance**
            
            I've identified an immediate threat: Austria is on the verge of a cultural victory, only 23 turns away from influencing everyone, including us. I'm urgently assessing ways to bolster our cultural defenses and exploring aggressive options to disrupt their progress, potentially through war, to avert this existential crisis.
            
            **Disrupting Austrian Tourism**
            
            I'm now analyzing how an immediate war declaration against Austria could halt their surging tourism by disrupting their trade routes, which currently funnel significant cultural influence our way. The existing peace treaty needs careful consideration before any action.
            
            **Assessing Treaty Nuances**
            
            I'm now deeply scrutinizing the intricate details of our peace treaty with Austria, recognizing its remaining 15-turn duration. I'm simultaneously investigating potential triggers for our defensive pact with Babylon, specifically if Austria's actions towards them could circumvent our existing treaty and initiate conflict. The vast disparity in military strength between Austria and our current allies is a significant concern.
            
            **Investigating Polynesian Conflict**
            
            My immediate focus has shifted to understanding our current war with Polynesia, especially given their numerous ongoing conflicts. I'm examining their diplomatic standings and the rationale behind our engagement, reviewing recent combat actions and considering pathways to peace. Our war weariness also warrants close attention.
            
            **Ending Polynesian War**
            
            I am actively working to conclude our conflict with Polynesia. While we are currently winning at 54%, direct peace negotiations aren't an option for me. I will focus on improving our diplomatic standing with them to encourage the AI to broker peace, maintaining our current Public 50, Private 40 relationship.
            
            **Advancing Technology**
            
            With our progress in the Polynesian conflict, I'm now reviewing our research path. The previous selection of Advanced Ballistics has been made, and I am considering the optimal next technology to pursue, weighing the benefits of Computers for an extra trade route against other advancements.
            
            **Researching Ballistics**
            
            My focus has shifted to crucial technological advancements. I've confirmed that researching Advanced Ballistics is paramount, enabling the construction of Nuclear Missiles. With ample Uranium, this provides a vital deterrent, particularly against Austria, and solidifies its selection as our next research target.
            
            **Evaluating Ideologies**
            
            I am now reviewing the tenets of our available ideologies, specifically considering "Cultural Revolution" for its tourism bonus against less happy civs and its happiness boost from factories. This offers a promising avenue to further accelerate our cultural victory while simultaneously managing happiness.
            
            **Researching Advanced Technologies**
            
            My research focus has solidified on acquiring advanced technologies. I've confirmed Advanced Ballistics as essential for Nuclear Missiles and am now evaluating "Great Leap Forward" for its potential free technology, aiming to bridge the gap in scientific and cultural capabilities, especially against Austria's dominance.
            
            **Choosing New Ideology**
            
            I'm evaluating my ideology choices. Great Leap Forward offers a free tech, potentially speeding up nuclear weapon research to counter Austria. However, Five-Year Plan would boost production significantly with our numerous improvements, and Enlightenment also provides a free tech within our existing Rationalism path.
            
            **Comparing Ideologies**
            
            I'm currently comparing "Enlightenment" and "Great Leap Forward." Given our significant spy network, the +100% science bonus from "Great Leap Forward" appears more advantageous for accelerating our technological progress and countering Austrian dominance, especially as most of our spies are currently abroad.
            
            **Comparing Ideologies**
            
            My current dilemma involves choosing between "Enlightenment" and "Great Leap Forward," both offering a free technology. Given our substantial science output, acquiring a free tech will significantly accelerate our path to crucial advancements like Nuclear Missiles, a vital counter to Austrian dominance. "Enlightenment" aligns well with our existing Rationalism path, while "Great Leap Forward" offers a potentially larger science boost through our spy network.
            
            **Selecting New Ideology**
            
            I've determined that a free technology policy is significantly more beneficial than ongoing yield bonuses. Given our extensive spy network, "Great Leap Forward" offers the greatest advantage due to its 100% spy science boost, allowing us to quickly catch up to Austria and Babylon.
            
            **Analyzing Ideological Conflicts**
            
            I'm now assessing the compatibility of our chosen Order ideology with Russia's Freedom ideology. Despite a significant modifier, their current positive disposition towards us suggests a defensive pact might still be feasible. I'm prioritizing maintaining our alliance strength to counter Austria.
            
            **Severing Korean Borders**
            
            I'm focusing on preventing Austria from using Korea as a staging ground. Their expiring Open Borders agreement with Korea is critical; I will ensure it's not renewed due to our negative relationship, blocking Austrian flanking maneuvers. I also see an opportunity with Polynesia; they're at war with Austria, and I aim to leverage that to end our own conflict with them.
            
            **Boosting Cultural Output**
            
            I am now prioritizing increasing our culture production. Our cities are currently focused on completing buildings with limited culture yields, and I'm assessing how to pivot to structures that directly boost our cultural output to better defend against Austria's imminent victory.
            
            **Utilizing Great Writer**
            
            My focus is now on leveraging our newly acquired Great Writer. I've confirmed its creation and am planning to use it for a political treatise to significantly boost our culture output, rapidly accelerating policy acquisition and improving our cultural defense against Austria.
            
            **Adjusting Flavors**
            
            My focus is now on fine-tuning our ideological flavors to maximize both scientific and cultural output. I'm adjusting these to 100 each, ensuring we have the necessary defenses against Austria while accelerating our path to victory. This includes optimizing our current builds for culture and science.
            
            **Capturing Vital Cities**
            
            I'm now focusing on the imminent capture of Honolulu, which holds five world wonders, significantly boosting our position. This strategic conquest will weaken Polynesia and provide substantial benefits, including valuable wonders, without significantly worsening our warmonger status given our ongoing conflict.
            
            **Capturing Honolulu Soon**
            
            I am preparing to capture Honolulu imminently. This strategic move against Polynesia will grant us vital wonders, accelerating Great Person generation, naval movement, and overall yields, which is crucial for our defense against Austria's looming cultural dominance.
            
            **Defending Against Air Power**
            
            I'm focusing on Austria's significant air presence near Jeonju. My priority is bolstering our anti-air capabilities and building fighters to intercept their bombers. This strategy is crucial to counter their aerial threat, especially with war likely in 15 turns or sooner.
            
            **Leveraging Wonders**
            
            I am assessing how to best utilize the Leaning Tower of Pisa and our Carnival ability. My goal is to secure Honolulu and then negotiate peace with Polynesia, allowing them to focus their efforts against Austria.
            
            **Securing Borders & Allies**
            
            I'm prioritizing ensuring Korea's Open Borders with us are not renewed to block Austrian flanking. Simultaneously, I'm fostering a positive relationship with Polynesia to secure peace post-Honolulu capture, allowing us to redirect forces against Austria. I'm also analyzing the ideological compatibility with Russia to maintain our defensive pact.
            
            **Negotiating Peace and Alliances**
            
            I'm now focused on finalizing the peace with Polynesia immediately after securing Honolulu, enabling them to pressure Austria. Simultaneously, I'm strengthening ties with Russia, aiming for a defensive pact, and maintaining our strong relationship with Babylon to ensure our cultural victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: vX9PyUdZdvZZ3SmA
          - toolName: set-research
          - input:
            - Rationale: Radar finishes this turn. Advanced Ballistics is our highest priority to unlock Nuclear Missiles (we have 4 Uranium) and SS Boosters. Nuclear deterrence is our only viable defense against Austria's 25,518 military strength when our 15-turn peace treaty expires.
            - Technology: Advanced Ballistics
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: Ffr5YO8pqp4RysBg
          - toolName: set-policy
          - input:
            - Policy: Great Leap Forward
            - Rationale: We change our next policy from Dictatorship of the Proletariat to Great Leap Forward. This Level 2 Order tenet provides a free technology, which we can use to instantly acquire a massive late-game tech (saving ~10 turns of research), and boosts spy science by 100%. This is highly strategic for catching up to Austria and Babylon in technology, while also helping our cultural/scientific defense.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: lPxsHJ6OpX0PWG2q
          - toolName: set-relationship
          - input:
            - Private: -90
            - Public: -70
            - Rationale: Korea is an Austrian vassal. Our Open Borders deal with them expires in 1 turn. We must maintain highly hostile/guarded relations to ensure the AI does NOT renew Open Borders. This prevents Austria from using Korean territory to bypass our choke points and launch a surprise attack when our peace treaty expires.
            - TargetID: 3
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: HIe3U88bTiFblHUp
          - toolName: set-relationship
          - input:
            - Public: 50
            - Private: 40
            - TargetID: 6
            - Rationale: While we are currently finishing the conquest of their capital Honolulu (at 12% health with 5 wonders), we want to establish peace immediately after to redirect all military forces toward the Austrian border. Maintaining a moderately friendly posture ensures the AI will accept a peace treaty as soon as Honolulu falls, allowing both of us to focus on the Austrian threat.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 9FhdUZNZ6nHvkKEH
          - toolName: set-relationship
          - input:
            - Private: 70
            - Public: 80
            - Rationale: Russia is our critical buffer state, currently fighting Austria. We must maximize our friendly stance (improving from +70/+60 to +80/+70) to support their survival and explore a future defensive pact or joint military actions against Austria, despite our ideological differences.
            - TargetID: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: LeOyKnpEtSulVHDe
          - toolName: set-relationship
          - input:
            - Public: 100
            - Private: 100
            - TargetID: 4
            - Rationale: Babylon is our defensive pact ally, fellow Order believer, and our primary path to a Cultural Victory (91% Popular, 7 turns to Influential). Maintaining maximum relations (+100/+100) is essential to secure their military coordination and complete our tourism influence.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: yfGrQ0bMZ1iXuoqh
          - toolName: set-relationship
          - input:
            - Private: -90
            - Public: -50
            - Rationale: Worsening public stance to -50 and private to -90. Their peace treaty with us expires in 15 turns, they are a massive existential threat, and their air force is massing on our borders in Jeonju. We must completely cut off any diplomatic friendliness and prepare for total war.
            - TargetID: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: OlR69Wah3FWsl7Rf
          - toolName: set-flavors
          - input:
            - Flavors:
              - UseNuke: 95
              - Science: 100
              - Air: 100
              - Mobilization: 100
              - Espionage: 100
              - Defense: 100
              - CityDefense: 100
              - Culture: 100
              - Offense: 40
              - Production: 90
              - Antiair: 100
              - GreatPeople: 100
              - Nuke: 100
            - Rationale: Prioritizing Culture (100) and GreatPeople (100) to secure our imminent victory over Babylon (7 turns) and defend against Austria's massive tourism. Prioritizing Science (100), Nuke (100), UseNuke (95) to rush Advanced Ballistics for nuclear deterrence. Keeping Defense (100), Antiair (100), Air (100), Mobilization (100), and CityDefense (100) at maximum to prepare for Austria's imminent assault when the peace treaty expires in 15 turns, especially since they have massed bombers in Jeonju. Offense set to 40 to ensure we capture Honolulu (12% health, 5 wonders) and then transition immediately to full defense.
            - GrandStrategy: Culture
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: vX9PyUdZdvZZ3SmA
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
          - toolCallId: Ffr5YO8pqp4RysBg
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: lPxsHJ6OpX0PWG2q
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: HIe3U88bTiFblHUp
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 9FhdUZNZ6nHvkKEH
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: LeOyKnpEtSulVHDe
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: yfGrQ0bMZ1iXuoqh
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: OlR69Wah3FWsl7Rf
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.