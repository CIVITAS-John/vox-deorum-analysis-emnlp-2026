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
        - Technology: Advanced Ballistics
        - Rationale: Radar completes in 1 turn. Advanced Ballistics is our top priority next as it unlocks Nuclear Missiles (essential for strategic deterrence against Austria's 7x military superiority) and the SS Booster for a potential Science Victory pivot.
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Cultural Revolution
        - Rationale: With Babylon soon to be influenced, Austria is our final obstacle to Cultural Victory. Since Austria's happiness is at 65% and ours is 100%, adopting Cultural Revolution (+25% Tourism to civilizations with less Happiness) is a massive tourism multiplier directly against Austria, far superior to the raw yields of Dictatorship of the Proletariat.
    - #2:
      - toolName: set-persona
      - args:
        - WarBias: 3
        - Rationale: Increasing Boldness to 4 and WarBias to 3 to ensure the AI aggressively finishes the siege of Honolulu (currently at 12% health) and doesn't prematurely accept a weak peace offer from Polynesia. Maintaining maximum WorkWithWillingness (10) for allied coordination.
        - Boldness: 4
    - #3:
      - toolName: set-relationship
      - args:
        - Public: -80
        - Rationale: Polynesia is at war with us and their capital Honolulu is at 12% health. We must capture Honolulu to secure their wonders, great works, and deny them any threat. No peace until Honolulu is ours.
        - TargetID: 6
        - Private: -100
    - #4:
      - toolName: set-relationship
      - args:
        - Private: -90
        - TargetID: 3
        - Rationale: Korea is an Austrian vassal and our Open Borders with them expires in 1 turn. We must NOT renew Open Borders as it allows Austrian units free passage to our borders. Worsening relationship to ensure the AI rejects renewal.
        - Public: -70
    - #5:
      - toolName: set-relationship
      - args:
        - Rationale: Austria is our existential threat with 25k military power and 4/5 civs influenced. Our peace treaty expires in 15 turns. We must maintain absolute hostility and prepare for total war.
        - Public: -100
        - Private: -100
        - TargetID: 0
    - #6:
      - toolName: set-relationship
      - args:
        - Private: 100
        - TargetID: 4
        - Rationale: Babylon is our key defensive pact ally and fellow Order civilization. We must maintain maximum relations to ensure their full military support when the Austrian peace treaty expires.
        - Public: 100
    - #7:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Private: 80
        - Public: 80
        - Rationale: Russia is fighting Austria and serves as a vital military buffer. We must maintain friendly relations to coordinate anti-Austrian actions.
    - #8:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Infrastructure: 80
          - UseNuke: 95
          - Production: 95
          - Spaceship: 60
          - Offense: 50
          - TileImprovement: 70
          - CityDefense: 100
          - Diplomacy: 50
          - MilitaryTraining: 95
          - Air: 100
          - WaterConnection: 50
          - Airlift: 95
          - Espionage: 100
          - Culture: 100
          - Gold: 60
          - Nuke: 100
          - NavalGrowth: 40
          - Naval: 60
          - AirCarrier: 90
          - Religion: 10
          - Mobilization: 100
          - Defense: 100
          - Expansion: 0
          - Growth: 60
          - Happiness: 70
          - Wonder: 20
          - Recon: 10
          - Mobile: 40
          - NavalTileImprovement: 40
          - Science: 100
          - Antiair: 100
          - NavalRecon: 20
          - GreatPeople: 95
          - Ranged: 95
        - GrandStrategy: Culture
      - rationale: Pivoting flavors to finish the Polynesian war and maximize defensive preparations against Austria. Raised Offense to 50 to ensure the AI captures Honolulu. Kept Defense, Mobilization, and Nuke at 100 for Austrian deterrence. Raised Culture to 100 and Great People to 95 to maximize Great Musician generation for concert tours in Austria.
  - tokens:
    - inputTokens: 51681
    - reasoningTokens: 7429
    - outputTokens: 775
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Cultural Victory**
            
            My focus is on accelerating our path to cultural dominance. Recent progress shows Babylon is nearing influential status, with the current trajectory indicating we'll achieve this in approximately seven turns.
            
            **Refining Cultural Reach**
            
            I'm re-evaluating my cultural victory timeline. It seems my earlier projection for Babylon was slightly optimistic; I need to account for influencing Austria as well, bringing the total to five civs.
            
            **Assessing Competitive Landscape**
            
            I'm reassessing our cultural victory path, identifying Austria as a significant rival nearing victory themselves. They have four influential civs and are poised to win soon, which complicates my own plans and necessitates a defensive strategy against their current aggression.
            
            **Clarifying Diplomatic Alliances**
            
            I'm clarifying our current diplomatic situation. The peace treaty with Austria has fifteen turns remaining, and our defensive pact with the nuclear-capable Babylon lasts for thirty-nine turns. Our research is now focused on Radar.
            
            **Confirming Research Direction**
            
            I'm confirming our research path, ensuring "Advanced Ballistics" is set as the next objective once Radar completes its final turn. I'm also reviewing policy options to optimize our progress.
            
            **Revising War Status**
            
            I'm reviewing our military engagements. It appears my assumption of peace with Polynesia was incorrect; we are still actively at war with them, which significantly impacts my resource allocation and defensive planning against Austria.
            
            **Confirming Ongoing Conflicts**
            
            I'm confirming our active military engagements. It's clear now that the war with Polynesia is ongoing, with units actively engaged and their capital, Honolulu, under siege. This significantly alters resource allocation and defensive priorities against Austria.
            
            **Capturing Honolulu**
            
            I'm focused on the imminent capture of Honolulu, Polynesia's capital, which is critically damaged. This victory would significantly benefit our position, but I need to carefully weigh this against our "Culture" grand strategy and the diplomatic implications, especially concerning Austria's vassal, Korea.
            
            **Severing Diplomatic Ties**
            
            I'm revising our diplomatic approach with Korea. The impending expiration of our open borders necessitates a negative relationship to prevent renewal, thereby hindering Austria's strategic access. I will ensure our opinion remains guarded.
            
            **Adjusting Diplomatic Stance**
            
            I'm recalibrating our diplomatic relationships. With Polynesia, the unexpected ongoing war and imminent capture of their capital necessitate a shift to a hostile stance. This will likely increase their resistance, but it's crucial for securing the victory there before addressing other matters.
            
            **Defeating Austrian Influence**
            
            I'm reassessing the World Congress proposals. Austria's push for Freedom Ideology is a critical threat to our Order and tourism; I must work to block it. Conversely, Brazil's Decolonization proposal offers a significant opportunity to cripple Austria's influence by severing their numerous city-state alliances.
            
            **Securing Diplomatic Wins**
            
            I'm focusing on the World Congress, specifically the "Decolonization" proposal, which is vital for crippling Austria's city-state alliances. My immediate priority is capturing Honolulu from Polynesia before addressing any potential peace negotiations, especially considering Korea's vassal status.
            
            **Prioritizing Offensive Maneuvers**
            
            I'm adjusting our military focus towards capturing Honolulu, setting our offense to 50 while maintaining strong defense. This strategic shift aims to secure a quick victory there before the peace treaty with Austria expires, ensuring we're prepared for their looming aggression and maintaining our current production of triplanes and other key units.
            
            **Prioritizing Deterrence**
            
            I'm prioritizing immediate research into "Advanced Ballistics" to unlock nuclear deterrence against Austria's overwhelming military. With Radar finishing next turn, I'll ensure this critical tech is queued. Our limited Uranium supply will be vital for this strategic shift.
            
            **Choosing Order Tenets**
            
            I'm evaluating our next Order tenets. Dictatorship of the Proletariat offers significant flat yield increases, while Cultural Revolution could boost tourism against less happy civilizations, potentially impacting Austria. I need to confirm Austria's happiness levels to make the optimal choice.
            
            **Boosting Tourism Output**
            
            My current focus is on amplifying our tourism generation to hasten cultural influence over Austria. With Babylon already close to influential status and Polynesia and Korea solidly influenced, securing Austria is key. I'm analyzing potential tourism boosts, especially from capturing Honolulu, and assessing whether Austria's happiness levels allow for a significant gain from the Cultural Revolution tenet.
            
            **Boosting Tourism Output**
            
            My current focus is on amplifying our tourism generation to hasten cultural influence over Austria. With Babylon already close to influential status and Polynesia and Korea solidly influenced, securing Austria is key. I'm analyzing potential tourism boosts, especially from capturing Honolulu, and assessing whether Austria's happiness levels allow for a significant gain from the Cultural Revolution tenet.
            
            **Analyzing Cultural Impact**
            
            I'm analyzing the impact of our Great Musician's concert tour in Austria. This direct tourism boost is significant. I'm now weighing the benefits of the "Cultural Revolution" tenet for its tourism bonus against "Dictatorship of the Proletariat" for faster research towards nuclear deterrence. The decision hinges on Austria's happiness levels and the remaining turns until our next policy choice.
            
            **Choosing Order Tenets**
            
            I've decided to implement the "Cultural Revolution" tenet. The +25% tourism bonus specifically targeting Austria, Babylon, and Polynesia is far more beneficial for my cultural victory goals than the smaller flat yield increases from "Dictatorship of the Proletariat," especially given Austria's current happiness levels.
            
            **Setting Diplomatic Stances**
            
            I'm making crucial adjustments to our diplomatic stances. Polynesia is now marked as extremely hostile to ensure Honolulu's capture, and Korea will be set to hostile to prevent open border renewal, strategically hindering Austria's movement and influence.
            
            **Escalating Hostility Towards Austria**
            
            I'm now escalating our diplomatic stance towards Austria to maximally hostile. This critical decision recognizes their overwhelming military and cultural threat as our peace treaty nears expiration. Simultaneously, I'm cementing our alliance with Babylon and ensuring our support for Russia, who are actively engaged against Austria.
            
            **Adjusting Persona Parameters**
            
            I'm re-evaluating our AI persona settings to better reflect our current strategic situation. Given our active war with Polynesia and impending conflict with Austria, I believe increasing our Boldness and WarBias slightly, perhaps to 4 or 5, will encourage more dynamic unit movement and tactical defense without provoking unnecessary aggression.
            
            **Adjusting Persona Parameters**
            
            I'm re-evaluating our AI persona settings to better reflect our current strategic situation. Given our active war with Polynesia and impending conflict with Austria, I believe increasing our Boldness slightly to 4 and WarBias to 3 will encourage more decisive action while maintaining strong defensive priorities.
            
            **Refining Strategy Flavors**
            
            I'm now fine-tuning our strategy flavors. I'm significantly increasing Offense to 50 to ensure Honolulu's capture, while keeping Defense and Mobilization maxed at 100 to prepare for Austrian aggression. Our core GrandStrategy remains Cultural Victory.
            
            **Updating Strategy Flavors**
            
            I am refining our strategy flavors. Offense is now at 50 for Honolulu's capture, with Defense and Mobilization at 100 for Austrian aggression. Espionage is maxed at 100 to gather intel on Austria, and Great People generation is prioritized for Musicians.
            
            **Executing Strategic Maneuvers**
            
            I am finalizing the execution of several key strategic actions. Research for "Advanced Ballistics" is confirmed to follow "Radar," crucial for nuclear deterrence against Austria. I am also setting the "Cultural Revolution" tenet to boost tourism, alongside critical diplomatic and flavor adjustments to prepare for immediate conflicts and secure our cultural victory.
            
            **Executing Strategic Maneuvers**
            
            I am finalizing the execution of several key strategic actions. Research for "Advanced Ballistics" is confirmed to follow "Radar," crucial for nuclear deterrence against Austria. I am also setting the "Cultural Revolution" tenet to boost tourism, alongside critical diplomatic and flavor adjustments to prepare for immediate conflicts and secure our cultural victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: a3tjmhfUBrILhgzk
          - toolName: set-research
          - input:
            - Technology: Advanced Ballistics
            - Rationale: Radar completes in 1 turn. Advanced Ballistics is our top priority next as it unlocks Nuclear Missiles (essential for strategic deterrence against Austria's 7x military superiority) and the SS Booster for a potential Science Victory pivot.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: c6DbMcy3i0eZzAlA
          - toolName: set-policy
          - input:
            - Policy: Cultural Revolution
            - Rationale: With Babylon soon to be influenced, Austria is our final obstacle to Cultural Victory. Since Austria's happiness is at 65% and ours is 100%, adopting Cultural Revolution (+25% Tourism to civilizations with less Happiness) is a massive tourism multiplier directly against Austria, far superior to the raw yields of Dictatorship of the Proletariat.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: CgIunpC8uL8kgNqg
          - toolName: set-persona
          - input:
            - WarBias: 3
            - Rationale: Increasing Boldness to 4 and WarBias to 3 to ensure the AI aggressively finishes the siege of Honolulu (currently at 12% health) and doesn't prematurely accept a weak peace offer from Polynesia. Maintaining maximum WorkWithWillingness (10) for allied coordination.
            - Boldness: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: UmzW2Efit0aEYnqn
          - toolName: set-relationship
          - input:
            - Public: -80
            - Rationale: Polynesia is at war with us and their capital Honolulu is at 12% health. We must capture Honolulu to secure their wonders, great works, and deny them any threat. No peace until Honolulu is ours.
            - TargetID: 6
            - Private: -100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: PgVVhBjn441G77AE
          - toolName: set-relationship
          - input:
            - Private: -90
            - TargetID: 3
            - Rationale: Korea is an Austrian vassal and our Open Borders with them expires in 1 turn. We must NOT renew Open Borders as it allows Austrian units free passage to our borders. Worsening relationship to ensure the AI rejects renewal.
            - Public: -70
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: Rs8CO2D0pbBGD4NM
          - toolName: set-relationship
          - input:
            - Rationale: Austria is our existential threat with 25k military power and 4/5 civs influenced. Our peace treaty expires in 15 turns. We must maintain absolute hostility and prepare for total war.
            - Public: -100
            - Private: -100
            - TargetID: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: Ff6hvAKc8Q8Fn3I7
          - toolName: set-relationship
          - input:
            - Private: 100
            - TargetID: 4
            - Rationale: Babylon is our key defensive pact ally and fellow Order civilization. We must maintain maximum relations to ensure their full military support when the Austrian peace treaty expires.
            - Public: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: CsbOjLrPbOcveCre
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Private: 80
            - Public: 80
            - Rationale: Russia is fighting Austria and serves as a vital military buffer. We must maintain friendly relations to coordinate anti-Austrian actions.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #9:
          - type: tool-call
          - toolCallId: Fk2KvOH7iJQRNRN2
          - toolName: set-flavors
          - input:
            - Flavors:
              - Infrastructure: 80
              - UseNuke: 95
              - Production: 95
              - Spaceship: 60
              - Offense: 50
              - TileImprovement: 70
              - CityDefense: 100
              - Diplomacy: 50
              - MilitaryTraining: 95
              - Air: 100
              - WaterConnection: 50
              - Airlift: 95
              - Espionage: 100
              - Culture: 100
              - Gold: 60
              - Nuke: 100
              - NavalGrowth: 40
              - Naval: 60
              - AirCarrier: 90
              - Religion: 10
              - Mobilization: 100
              - Defense: 100
              - Expansion: 0
              - Growth: 60
              - Happiness: 70
              - Wonder: 20
              - Recon: 10
              - Mobile: 40
              - NavalTileImprovement: 40
              - Science: 100
              - Antiair: 100
              - NavalRecon: 20
              - GreatPeople: 95
              - Ranged: 95
            - GrandStrategy: Culture
            - Rationale: Pivoting flavors to finish the Polynesian war and maximize defensive preparations against Austria. Raised Offense to 50 to ensure the AI captures Honolulu. Kept Defense, Mobilization, and Nuke at 100 for Austrian deterrence. Raised Culture to 100 and Great People to 95 to maximize Great Musician generation for concert tours in Austria.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: a3tjmhfUBrILhgzk
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
          - toolCallId: c6DbMcy3i0eZzAlA
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: CgIunpC8uL8kgNqg
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: UmzW2Efit0aEYnqn
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: PgVVhBjn441G77AE
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: Rs8CO2D0pbBGD4NM
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: Ff6hvAKc8Q8Fn3I7
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: CsbOjLrPbOcveCre
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #8:
          - type: tool-result
          - toolCallId: Fk2KvOH7iJQRNRN2
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.