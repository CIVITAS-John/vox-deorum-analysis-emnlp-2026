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
        - Rationale: Adopting Cultural Revolution (Level 2 Order Tenet) will grant us +25% Tourism against civilizations with less Happiness than us. Since Austria (65%), Babylon (45%), and Polynesia (37%) all have significantly less happiness than our 100%, this will provide a massive, immediate boost to our tourism output and accelerate our progress toward a Cultural Victory.
        - Policy: Cultural Revolution
    - #1:
      - toolName: set-research
      - args:
        - Rationale: Computers grants us an additional Trade Route, which is extremely valuable for our cultural victory strategy. In Vox Populi, trade routes provide a direct +25% tourism modifier to the target civilization, helping us become influential over Austria and Babylon much faster, while also providing valuable gold and science.
    - #2:
      - toolName: set-persona
      - args:
        - MinorCivFriendlyBias: 8
        - Rationale: We are adjusting our persona to be much friendlier and less hostile to city-states to help us secure alliances and block Austria's imminent Diplomatic Victory. We also increase our Loyalty to ensure our crucial defensive alliance with Babylon remains secure, and slightly raise Boldness and War Bias to help our tactical AI aggressively capture Honolulu.
        - WarBias: 4
        - Loyalty: 8
        - Boldness: 4
        - MinorCivHostileBias: 2
    - #3:
      - toolName: set-relationship
      - args:
        - Private: -90
        - Rationale: Polynesia is our active war target. Their capital, Honolulu, is down to 12% health and contains several highly valuable World Wonders. We are setting our public and private relationship to extremely hostile to ensure our military focus remains on fully capturing Honolulu and Nuku Hiva.
        - Public: -90
        - TargetID: 6
    - #4:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Offense: 60
          - GreatPeople: 90
          - Diplomacy: 80
          - Defense: 80
          - Espionage: 100
          - Science: 90
          - Culture: 95
          - Production: 90
          - Gold: 80
        - GrandStrategy: Culture
      - rationale: We are adjusting our tactical focus to support our offensive push against Honolulu (increasing Offense to 60) and our diplomatic struggle against Austria (increasing Diplomacy and Gold to 80 to invest in city-states). We maintain a very high focus on Culture, Science, and Espionage to protect our lands and advance our Cultural Victory.
  - tokens:
    - inputTokens: 50723
    - reasoningTokens: 6729
    - outputTokens: 469
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Reviewing Current Goals**
            
            I'm currently assessing our progress towards a cultural victory in Civilization V. We're in the Atomic era, turn 395, and I'm evaluating our strategic positioning and immediate objectives.
            
            **Analyzing Austria's Dominance**
            
            I'm reassessing our path to victory, as Austria is significantly ahead. They're on the verge of both Diplomatic and Cultural wins, holding the United Nations and nearing their delegate count. I'm also reviewing my influence over other civs and their progress towards mine.
            
            **Prioritizing Diplomatic Victory**
            
            My immediate focus is on preventing Austria's diplomatic win. The upcoming World Congress vote on "Decolonization" is critical; if it passes, it will disrupt Austria's city-state alliances and buy us precious time. I'm also considering how to defend our own cultural progress while managing our ongoing conflict with Polynesia.
            
            **Shifting Combat Tactics**
            
            My naval forces are engaged with Polynesia, but the loss of our Great Diplomat is a setback. I've successfully deployed a Great Musician in Austria, aiming to boost tourism. With Radar researching, I'm deciding between Advanced Ballistics, Computers, or Alternative Energy for our next technological pursuit.
            
            **Evaluating Next Tech**
            
            I'm weighing the strategic advantage of researching Computers for an extra trade route to boost our tourism against the defensive power of Advanced Ballistics. Given Brazil's tourism modifiers, a trade route seems more impactful for our current goals. I'm deciding if we should pivot the research queue now.
            
            **Choosing Next Policy**
            
            I am currently evaluating our next ideological policy choice, with "Dictatorship of the Proletariat" being the frontrunner, pending availability within the Order tree. I am cross-referencing this with other available tenets to ensure optimal synergy for our current cultural victory push.
            
            **Selecting Ideology Tenet**
            
            I'm reassessing our ideological choices. "Cultural Revolution" offers a significant tourism boost against unhappy civilizations like Austria and Babylon, which aligns perfectly with our current cultural victory push. I am confirming its availability and potential impact against these specific rivals.
            
            **Choosing Ideology Tenet**
            
            I'm now prioritizing "Cultural Revolution" as the next ideological policy. This tenet offers a crucial 25% tourism boost against less happy civilizations like Austria and Babylon, directly accelerating our cultural victory push against them. This seems more impactful than the flat bonuses of "Dictatorship of the Proletariat."
            
            **Assessing Diplomatic Threats**
            
            I'm analyzing Austria's diplomatic stance and potential aggression, noting their denounced status towards me and our ideological clash. Despite their aggressive military, their current relations with other civs and wars suggest they might not be an immediate land threat, but their influence is concerning.
            
            **Securing Congress Votes**
            
            I'm strategizing to ensure "Decolonization" passes the upcoming World Congress vote to thwart Austria's impending diplomatic victory. Their "World Ideology: Freedom" proposal, bolstered by allies like Korea and Russia, poses a significant threat to our delegate count and overall win condition.
            
            **Adjusting Diplomacy Flavor**
            
            I'm re-evaluating our flavor settings to better influence the upcoming World Congress vote. Increasing our Diplomacy flavor to prioritize diplomatic actions should help secure the necessary votes for "Decolonization" and counter Austria's impending victory.
            
            **Capturing Honolulu Now**
            
            My current focus is on a swift capture of Honolulu. With their defenses at 12% health and my forces in position, victory is imminent. This will be a significant strategic gain, netting us several valuable wonders.
            
            **Capturing Key Capitals**
            
            I'm prioritizing the capture of Honolulu from Polynesia, which is nearly defeated. Following that, I intend to seize Nuku Hiva for its valuable wonders. I will then assess the geopolitical climate, particularly Austria's stance, before deciding whether to pursue peace or continue the offensive.
            
            **Increasing Offensive Flavor**
            
            I am now prioritizing increasing our "Offense" flavor setting. This is to better align the tactical AI with my immediate objective of swiftly capturing Honolulu and Nuku Hiva from Polynesia, ensuring a successful offensive without compromising our long-term cultural victory strategy.
            
            **Balancing Strategic Flavors**
            
            I'm adjusting our strategic flavors, increasing Diplomacy to 80 to secure city-state alliances against Austria, while slightly tempering Offense to 60 to maintain focus on capturing Polynesian cities. Gold is also being boosted to 80 for crucial purchases.
            
            **Prioritizing Computers Tech**
            
            I'm prioritizing researching "Computers" due to the significant tourism boost an extra trade route provides. This will allow for a substantial increase in our influence over key civs like Austria, directly accelerating our cultural victory push.
            
            **Researching Key Technology**
            
            I'm prioritizing "Computers" to unlock an additional trade route, as this significantly bolsters our tourism output, especially with Austria. This choice supersedes other technologies, including "Alternative Energy" and "Advanced Ballistics," for our immediate victory condition.
            
            **Choosing Ideology Tenet**
            
            I am now selecting "Cultural Revolution" as my next ideological tenet. The increased tourism against less happy civilizations, such as Austria, directly supports our cultural victory push, proving more beneficial than earlier options.
            
            **Adjusting Strategic Persona**
            
            I'm reviewing our persona settings to better reflect our current war with Polynesia and our aggressive pursuit of victory. I need to increase our WarBias and Boldness to align with these objectives, as the current low values suggest excessive caution.
            
            **Refining City-State Diplomacy**
            
            I'm adjusting our diplomatic stance towards city-states. My current focus is on increasing our friendliness bias significantly to foster alliances, which is crucial for securing votes for "Decolonization" and countering diplomatic victories. I'm also toning down hostility to maintain better relations.
            
            **Refining Persona Settings**
            
            I'm adjusting our strategic persona to solidify Babylon as a key ally by setting Loyalty to 8, which is critical for their support against Austria. I've also increased MinorCivFriendlyBias and decreased MinorCivHostileBias for city-states, while slightly raising Boldness and WarBias for our offensive operations.
            
            **Updating Diplomatic Relations**
            
            I'm actively adjusting our relationship settings, ensuring Polynesia is marked as intensely hostile to reflect our ongoing war and strategic objective of capturing their cities. I'm also evaluating Russia's complex stance, aiming to maintain a beneficial relationship for their ongoing conflict with Austria.
            
            **Implementing Strategic Changes**
            
            I am now executing the planned adjustments, starting with implementing "Cultural Revolution" for a significant tourism boost against less happy rivals like Austria. Following this, I'm initiating research for "Computers" to unlock a vital extra trade route, bolstering our cultural influence and preparing for the next phase.
            
            **Confirming Technology Choice**
            
            I'm confirming my decision to research "Computers." The additional trade route it provides is crucial for accelerating our tourism output, especially against Austria, and directly supports our immediate cultural victory objective. This research is now prioritized above all other advancements.
            
            **Finalizing Ideology Choice**
            
            I've finalized my choice of ideological tenet: "Cultural Revolution." This selection is driven by its potent +25% tourism bonus against civilizations with lower happiness levels, such as Austria and Babylon, which is a direct advantage for our current cultural victory push.
            
            **Adjusting Strategic Persona**
            
            I'm refining our strategic persona. I'm increasing our WarBias and Boldness to align with the ongoing conflict with Polynesia and our aggressive pursuit of victory, moving away from the previous cautious stance. This will better reflect our current objectives.
            
            **Solidifying City-State Diplomacy**
            
            I'm enhancing our diplomacy with city-states. My focus is on increasing our friendliness bias to secure vital alliances, which is essential for winning upcoming World Congress votes. I'm also dialing back hostility to maintain beneficial relationships with them.
            
            **Refining Persona Settings**
            
            I'm fine-tuning our persona. I've set Babylon's Loyalty to 8 to secure their crucial support against Austria. Additionally, I'm increasing MinorCivFriendlyBias and decreasing MinorCivHostileBias for city-states, while slightly elevating Boldness and WarBias to support our offensive actions.
            
            **Updating Diplomatic Relations**
            
            I am actively adjusting diplomatic settings to reflect ongoing conflicts and alliances. Polynesia is now marked as intensely hostile to facilitate city capture, and Russia's relationship is being managed to leverage their conflict with Austria to our advantage.
            
            **Executing Key Adjustments**
            
            I am proceeding with the planned strategic adjustments. This includes setting Polynesia to hostile (-90/-90) to aid in capturing their cities and increasing Offense flavor, while also prioritizing Diplomacy and Gold to counter Austria and fund crucial city-state interactions.
            
            **Finalizing Strategic Priorities**
            
            I'm consolidating our strategic focus. The technology "Computers" is confirmed for its tourism-boosting trade route, and the policy "Cultural Revolution" is locked in for its significant bonus against rivals. Our GrandStrategy remains firmly set on "Culture."
            
            **Executing Strategic Tweaks**
            
            I'm implementing a series of adjustments: prioritizing the "Computers" technology for its crucial trade route, and locking in "Cultural Revolution" for its significant diplomatic advantage against rivals. My core strategy remains firmly focused on achieving cultural victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: iQmp22Nt8yLGXeo8
          - toolName: set-policy
          - input:
            - Rationale: Adopting Cultural Revolution (Level 2 Order Tenet) will grant us +25% Tourism against civilizations with less Happiness than us. Since Austria (65%), Babylon (45%), and Polynesia (37%) all have significantly less happiness than our 100%, this will provide a massive, immediate boost to our tourism output and accelerate our progress toward a Cultural Victory.
            - Policy: Cultural Revolution
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: ZeJTKhsqiiOwAi2y
          - toolName: set-research
          - input:
            - Rationale: Computers grants us an additional Trade Route, which is extremely valuable for our cultural victory strategy. In Vox Populi, trade routes provide a direct +25% tourism modifier to the target civilization, helping us become influential over Austria and Babylon much faster, while also providing valuable gold and science.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: TPq93QBS5Ah0TZzK
          - toolName: set-persona
          - input:
            - MinorCivFriendlyBias: 8
            - Rationale: We are adjusting our persona to be much friendlier and less hostile to city-states to help us secure alliances and block Austria's imminent Diplomatic Victory. We also increase our Loyalty to ensure our crucial defensive alliance with Babylon remains secure, and slightly raise Boldness and War Bias to help our tactical AI aggressively capture Honolulu.
            - WarBias: 4
            - Loyalty: 8
            - Boldness: 4
            - MinorCivHostileBias: 2
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: QIdGBMVC98bonXcg
          - toolName: set-relationship
          - input:
            - Private: -90
            - Rationale: Polynesia is our active war target. Their capital, Honolulu, is down to 12% health and contains several highly valuable World Wonders. We are setting our public and private relationship to extremely hostile to ensure our military focus remains on fully capturing Honolulu and Nuku Hiva.
            - Public: -90
            - TargetID: 6
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: NuJgxjeEqqPp8Jyq
          - toolName: set-flavors
          - input:
            - Rationale: We are adjusting our tactical focus to support our offensive push against Honolulu (increasing Offense to 60) and our diplomatic struggle against Austria (increasing Diplomacy and Gold to 80 to invest in city-states). We maintain a very high focus on Culture, Science, and Espionage to protect our lands and advance our Cultural Victory.
            - Flavors:
              - Offense: 60
              - GreatPeople: 90
              - Diplomacy: 80
              - Defense: 80
              - Espionage: 100
              - Science: 90
              - Culture: 95
              - Production: 90
              - Gold: 80
            - GrandStrategy: Culture
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: iQmp22Nt8yLGXeo8
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
          - toolCallId: ZeJTKhsqiiOwAi2y
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: TPq93QBS5Ah0TZzK
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: QIdGBMVC98bonXcg
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: NuJgxjeEqqPp8Jyq
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.