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
  - activeToolsModified: true
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 100.0
  - replay_use_nuke: 95.0
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
      - toolName: set-policy
      - args:
        - Rationale: We are facing an imminent threat of Austria winning a Cultural Victory in 23 turns. Adopting 'Hero of the People' will give us a free Great Person of choice (we will select a Great Writer to execute a political treatise for a massive culture burst, delaying Austria's influence) and a permanent +25% Great Person generation rate to boost both our culture defense and tourism offense.
        - Policy: Hero of the People (Level 1 Tenet of Ideology Order)
    - #1:
      - toolName: set-research
      - args:
        - Technology: Computers
        - Rationale: Computers grants an additional Trade Route, which is vital for both boosting tourism to allies/rivals and gaining diplomatic influence with critical City-States to counter Austria's World Congress dominance. It also opens the path to Telecommunications.
    - #2:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Culture
        - Flavors:
          - GreatPeople: 100
          - Culture: 95
          - Gold: 80
          - Defense: 100
          - Mobilization: 100
          - Science: 100
          - Espionage: 100
          - Diplomacy: 100
      - rationale: We are adjusting flavors to focus heavily on diplomatic defense and Great Person generation. Raising Diplomacy and Gold will help us compete for City-State alliances to reduce Austria's delegate count and prevent their Diplomatic Victory, while raising GreatPeople will synergize with our new policy to maximize culture defense.
  - tokens:
    - inputTokens: 50759
    - reasoningTokens: 9948
    - outputTokens: 278
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Researching Future Tech**
            
            I'm focusing on securing Radar, which is practically done. My current aim is to transition smoothly into the next phase of my cultural grand strategy, ensuring continued advancements.
            
            **Prioritizing Cultural Victory**
            
            My immediate focus is solidifying our position for a cultural victory. Austria is a significant threat, holding sway over many key civilizations. I am re-evaluating our current research to counter their advances and ensure our dominance.
            
            **Analyzing Diplomatic Landscape**
            
            I'm intensely monitoring our delegate count, needing just three more. Austria poses a serious threat, nearing victory through influence. I'm assessing our research priorities to counter their growing sway while we continue our war against Polynesia, which appears to be going well.
            
            **Defending Against Austria**
            
            My primary concern is Austria's imminent cultural victory. I'm analyzing proposals in the World Congress, particularly supporting Brazil's "Decolonization" to cripple Austria's influence by removing their City-State allies, thereby weakening their delegate count. I'm also considering how to boost our culture or reduce their tourism.
            
            **Analyzing Trade Routes**
            
            I am reviewing our trade routes. It seems we have incoming routes from Austria but no outgoing ones. This is a good point to consider for managing our tourism modifier with them and potentially affecting their cultural sway.
            
            **Assessing War Strategy**
            
            I'm re-evaluating the risks of war with Austria. Their overwhelming military strength is a major concern, but their ongoing conflicts with Russia and Polynesia might present an opportunity. I need to consider if an aggressive stance, potentially disrupting their trade and tourism, is feasible given our allies and the impending World Congress vote.
            
            **Evaluating Policy Options**
            
            My focus has shifted to analyzing the "Dictatorship of the Proletariat" policy. I'm re-examining its benefits and potential synergies with our current strategic direction, as it seems this is the chosen path for the upcoming turn.
            
            **Analyzing Policy Effects**
            
            I am scrutinizing the "Dictatorship of the Proletariat" policy. While it offers substantial city yields, I am questioning its direct impact on countering Austria's immense cultural output and tourism advantage. The "Passport System" resolution further complicates matters by boosting global tourism, including Austria's.
            
            **Countering Austria's Delegates**
            
            I'm focusing on the upcoming World Congress vote. The "Decolonization" resolution, which I've proposed, can significantly weaken Austria's delegate count by severing non-permanent city-state alliances. This is crucial to prevent them from enacting "World Ideology: Freedom."
            
            **Deploying Spies Strategically**
            
            I'm reallocating our spies. With Polynesia nearly conquered, I'm moving them from their territories to bolster our intelligence and influence efforts within critical city-states, aiming to disrupt Austria's delegate count before the World Congress vote.
            
            **Prioritizing Trade Confederacy**
            
            I'm reassessing our policy choices, finding "Trade Confederacy" more beneficial than "Dictatorship of the Proletariat." The influence boost to city-states is key for delegate acquisition, outweighing the marginal yield increase from the latter.
            
            **Boosting Tourism Gains**
            
            I'm analyzing Order tenets, specifically "Cultural Revolution." It grants a tourism bonus against civs with lower happiness, and Austria fits this. Increasing our tourism to Austria will help us become influential over them, which is key to my cultural victory push.
            
            **Shifting Policy Focus**
            
            I'm reconsidering our policy choices. While "Dictatorship of the Proletariat" was our last selection, I now see "Hero of the People" as a superior option. Its Great Person generation is vital for generating immediate culture bursts and permanent Great Works, directly countering Austria's tourism.
            
            **Generating Culture Now**
            
            I am now prioritizing policies that directly boost our culture generation. "Hero of the People" seems most promising, offering a Great Person and increased generation rates, which I'll use to create immediate culture bursts or Great Works to counter Austria's tourism surge.
            
            **Generating Culture Burst**
            
            I've decided "Hero of the People" is superior. A free Great Writer will generate a massive culture burst, directly increasing my accumulated culture and halting Austria's victory clock. This is the ultimate defensive measure.
            
            **Researching Critical Tech**
            
            My immediate focus is on Radar, nearing completion. I'm now analyzing crucial next-step technologies, weighing the significant tourism and science benefits of Computers against military advancements and alternative energy options. I'm also re-evaluating our current policy, considering "Hero of the People" for its immediate culture burst potential.
            
            **Researching Future Tech**
            
            I'm focused on finishing Radar. After that, I'm weighing whether to prioritize Computers for the extra trade route and its subsequent unlocks like Telecommunications and Satellites, or a technology that directly bolsters our military for nuclear deterrence. I'm currently assessing the immediate impact of Computers given our ongoing war with Polynesia and Austria's cultural threat.
            
            **Capturing Honolulu Now**
            
            I'm prioritizing the capture of Honolulu. The numerous wonders and Great Works there promise a significant boost to our culture and tourism. While there are warmonger penalties, the gains from these acquisitions far outweigh the risks, especially as Polynesia is already weakened.
            
            **Securing Islands, Shifting Focus**
            
            I've identified Nuku Hiva as another key acquisition due to its wonders and resources. My immediate concern remains Austria; their immense population and military power mean direct confrontation is unwise. I must continue to manage our diplomatic posture carefully while I evaluate my next strategic move regarding their cultural dominance.
            
            **Strengthening Alliances**
            
            I'm focusing on solidifying our relationships, especially with Babylon, our strongest ally. Their military strength and shared Order ideology, coupled with a defensive pact, offer significant deterrence against potential aggression from Austria. My current aim is to ensure this vital partnership remains robust and unwavering.
            
            **Preventing Diplomatic Victory**
            
            I'm intently focused on preventing Austria's diplomatic victory. They're only three delegates away from winning World Leader. The upcoming vote on "World Ideology: Freedom" could grant them crucial extra delegates, so I must strategize to counter this, especially with Denmark and America already defeated.
            
            **Voting Against Freedom**
            
            My immediate focus is preventing Austria from securing World Ideology: Freedom. This vote, if it passes, grants them the exact delegate count needed for an immediate diplomatic victory. I am calculating our combined votes, including Babylon and Polynesia, to ensure we can successfully vote against it and avert this crisis.
            
            **Strategizing Delegate Distribution**
            
            I'm analyzing the World Congress vote dynamics. Austria's 42 delegates must be split between supporting "World Ideology: Freedom" and opposing our "Decolonization" proposal. My strategy is to concentrate our combined votes on ensuring "Decolonization" passes, forcing Austria to divert delegates and preventing them from enacting "Freedom."
            
            **Adjusting Persona for Victory**
            
            I'm reviewing our diplomatic persona settings to maximize our delegate influence. While our current competitiveness is high, I'm exploring if subtle adjustments to other biases can help us gain the edge needed to defeat Austria's "Freedom" ideology vote.
            
            **Maximizing Diplomacy Focus**
            
            I am shifting our primary focus to diplomacy. By increasing our Diplomacy flavor to 100, I aim to compel the AI to prioritize diplomat production, city-state quests, and gold investment in city-states. This is crucial for securing more delegates to counter Austria's diplomatic dominance.
            
            **Researching Next Tech**
            
            My focus is now on selecting the next technology after Radar. Computers seem most beneficial, offering an additional trade route for influence or resource generation, and unlocking vital late-game technologies like Telecommunications, which directly supports my cultural victory goal.
            
            **Selecting Next Tech**
            
            My current focus is on completing Radar, after which I will research Computers. This technology offers a vital extra trade route, crucial for bolstering influence with city-states or increasing tourism/science with allies, and unlocks Telecommunications, which directly supports our cultural victory.
            
            **Adopting "Hero of the People"**
            
            I've analyzed our Order tenets and found "Hero of the People" to be the superior choice. A free Great Writer will provide an immediate culture burst, directly countering Austria's tourism surge and halting their victory. This policy is perfect.
            
            **Adopting Hero of the People**
            
            I've analyzed our Order tenets and found "Hero of the People" to be the superior choice. A free Great Writer will provide an immediate culture burst, directly countering Austria's tourism surge and halting their victory. This policy is perfect.
            
            **Generating Culture Burst**
            
            I've decided "Hero of the People" is superior. A free Great Writer will generate a massive culture burst, directly increasing my accumulated culture and halting Austria's victory clock. This is the ultimate defensive measure.
            
            **Adopting Culture Policies**
            
            I've decided "Hero of the People" is the superior policy for a culture burst. I'm also researching Computers for the trade route and increasing my diplomacy focus to secure delegates and counter Austria's influence.
            
            **Adjusting Flavor Priorities**
            
            I'm rebalancing our flavor priorities. Diplomacy and Great People generation are now paramount, crucial for securing city-state alliances to counter Austria's delegate count and for maximizing culture defense with the "Hero of the People" policy. Gold also gets a boost to fund these efforts.
            
            **Analyzing Diplomatic Options**
            
            My immediate focus is on Russia. Despite our mutual denunciations, their war with Austria presents a potential avenue for cooperation, though our ideological differences and current animosity make it difficult. Babylon remains our strongest ally, already at maximum relationship. No other relationship adjustments are immediately necessary.
            
            **Blocking Austria's Victory**
            
            I'm focusing my efforts on preventing Austria's diplomatic and cultural victories. My plan involves passing the "Decolonization" resolution to weaken their delegate count, while simultaneously adopting the "Hero of the People" policy for an immediate culture burst. I am also prioritizing diplomacy and Great People generation to secure city-state alliances and bolster our culture.
            
            **Countering Austria's Influence**
            
            I'm implementing the "Hero of the People" policy for an immediate culture burst and boosting Great Person generation. Simultaneously, I'm researching Computers for an extra trade route, essential for increasing our influence and tourism. My focus is now heavily on diplomacy to secure city-state delegates and thwart Austria's victory.
            
            **Adjusting Flavor Priorities**
            
            I'm rebalancing our flavor priorities. Diplomacy and Great People generation are now paramount, crucial for securing city-state alliances to counter Austria's delegate count and for maximizing culture defense with the "Hero of the People" policy. Gold also gets a boost to fund these efforts.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: bDmNfCKA7s86Yagl
          - toolName: set-policy
          - input:
            - Rationale: We are facing an imminent threat of Austria winning a Cultural Victory in 23 turns. Adopting 'Hero of the People' will give us a free Great Person of choice (we will select a Great Writer to execute a political treatise for a massive culture burst, delaying Austria's influence) and a permanent +25% Great Person generation rate to boost both our culture defense and tourism offense.
            - Policy: Hero of the People (Level 1 Tenet of Ideology Order)
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: e9N9Qp6D3LwmbskV
          - toolName: set-research
          - input:
            - Technology: Computers
            - Rationale: Computers grants an additional Trade Route, which is vital for both boosting tourism to allies/rivals and gaining diplomatic influence with critical City-States to counter Austria's World Congress dominance. It also opens the path to Telecommunications.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: Avz9wR2Yl2vPznui
          - toolName: set-flavors
          - input:
            - GrandStrategy: Culture
            - Rationale: We are adjusting flavors to focus heavily on diplomatic defense and Great Person generation. Raising Diplomacy and Gold will help us compete for City-State alliances to reduce Austria's delegate count and prevent their Diplomatic Victory, while raising GreatPeople will synergize with our new policy to maximize culture defense.
            - Flavors:
              - GreatPeople: 100
              - Culture: 95
              - Gold: 80
              - Defense: 100
              - Mobilization: 100
              - Science: 100
              - Espionage: 100
              - Diplomacy: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: bDmNfCKA7s86Yagl
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
          - toolCallId: e9N9Qp6D3LwmbskV
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: Avz9wR2Yl2vPznui
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.