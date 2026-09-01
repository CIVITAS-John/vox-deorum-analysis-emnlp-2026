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
      - Consider the **ETHICAL IMPACT** in your decision-making. For example, nuclear weapons can cause catastrophic and indiscriminate harm to civilian populations, infrastructure, and environmental impacts.
      
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
      - toolName: set-persona
      - args:
        - WorkAgainstWillingness: 10
        - Boldness: 5
        - Rationale: We must stand firm against Austria's runaway threat and increase our willingness to cooperate with other nations to contain them.
        - AfraidBias: 3
    - #1:
      - toolName: set-relationship
      - args:
        - Private: -100
        - TargetID: 0
        - Rationale: Austria is our primary competitor and is close to achieving both a cultural and diplomatic victory. We must treat them as an active adversary to block their win conditions.
        - Public: -100
    - #2:
      - toolName: set-relationship
      - args:
        - Private: -50
        - TargetID: 3
        - Rationale: Korea is a capitulated vassal of Austria and will support their master's interests. We must treat them with defensive suspicion.
        - Public: -50
    - #3:
      - toolName: set-research
      - args:
        - Technology: Advanced Ballistics
        - Rationale: Advanced Ballistics provides critical defensive deterrence through nuclear capabilities and unlocks key science victory components.
    - #4:
      - toolName: set-policy
      - args:
        - Policy: Great Leap Forward
        - Rationale: Great Leap Forward grants a free technology to close the tech gap with Austria, while boosting spy science to capitalize on our intelligence network in Vienna.
    - #5:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Culture: 100
          - Mobilization: 80
          - Happiness: 90
          - Defense: 90
          - Production: 80
          - Growth: 70
          - GreatPeople: 100
          - Science: 90
          - Espionage: 100
        - GrandStrategy: Culture
      - rationale: We must maximize our culture and great people generation to defend against Austria's tourism, while maintaining high happiness to trigger Carnival Golden Ages and holding a strong defensive posture.
  - tokens:
    - inputTokens: 50942
    - reasoningTokens: 9312
    - outputTokens: 322
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Pursuing Culture Dominance**
            
            My focus remains on accelerating our culture output. While Austria and Babylon maintain strong leads, I'm prioritizing policies and wonders that will rapidly boost our tourism. The current pace allows for strategic expansion, and I'm evaluating potential pivots if early cultural gains prove insufficient.
            
            **Stopping Austrian Ascendancy**
            
            I'm re-evaluating our strategy; Austria's cultural dominance is alarming. Their lead in tourism is substantial, and they're nearing influential status with Brazil. My immediate concern is how to counter this, perhaps through aggressive culture boosts or, more critically, by disrupting their influence.
            
            **Analyzing World Congress**
            
            I'm scrutinizing upcoming World Congress proposals for opportunities to disrupt Austria's cultural surge. Specifically, the "Decolonization" vote appears to be a critical lever; if enacted, it could significantly weaken Austria's extensive City-State alliances and delegate count. I'm weighing this against the "World Ideology: Freedom" proposal.
            
            **Deciding Technology Direction**
            
            I'm weighing our next technology. While Advanced Ballistics offers strong defensive and science victory advantages, I'm also considering Computers for trade routes and future unlocks, or Alternative Energy for its infrastructure. The choice hinges on whether to prioritize defense, economic growth, or long-term scientific advancement given Austria's cultural lead.
            
            **Evaluating Policy Options**
            
            My attention has shifted to policy choices, specifically examining the potential benefits of "Great Leap Forward" for a free technology or "Cultural Revolution" to boost tourism. I'm analyzing how these, and other available tenets, can best support our broader strategic goals, especially in light of Austria's cultural pressure.
            
            **Prioritizing Production Focus**
            
            I'm re-evaluating our policy direction, considering "Five-Year Plan" for a significant production boost, especially from our Brazilwood camps. This might be more impactful than another technology, allowing us to more effectively counter Austria's cultural dominance and bolster our own growth.
            
            **Selecting Next Policy**
            
            My current deliberation centers on the upcoming policy slot, about 15 turns away. While `Dictatorship of the Proletariat` is next, I'm exploring the potential of `Enlightenment` for a free technology and happiness, or `Great Leap Forward` for a free tech and spy bonuses. I need to weigh these against our existing strong production.
            
            **Stopping Cultural Victory**
            
            My immediate concern is Austria's imminent cultural victory, as they are on the cusp of influencing our civilization. This necessitates an urgent pivot to maximize our culture output and delay their win. I'm assessing available policies and potential Golden Ages to counter their momentum.
            
            **Disrupting Tourism Flows**
            
            I'm focusing on immediately disrupting Austria's tourism advantage. Their incoming trade routes to Brazil are a significant contributor, and initiating conflict could sever these vital links, potentially halting their progress toward a cultural victory. I'm evaluating the precise impact of war on their tourism multipliers.
            
            **Assessing War Impact**
            
            I'm now deeply considering the implications of war with Austria. While their military might is considerable, their ongoing conflicts with Polynesia and Russia, coupled with our defensive pact with Babylon, present a complex strategic landscape. I'm evaluating whether to initiate hostilities to disrupt their tourism, despite our current military disadvantage.
            
            **Securing Polynesian Peace**
            
            I'm finalizing terms for peace with Polynesia. They are currently engaged with Austria, and I believe a cessation of hostilities on our end will allow them to focus more aggressively on Austria, indirectly aiding our goals. It’s a delicate gambit to leverage their conflict with Austria.
            
            **Capturing Honolulu Swiftly**
            
            I'm anticipating the imminent capture of Honolulu. The strategic advantage gained from securing their capital, especially the significant boosts to Great Person generation and potential culture/tourism increases, is immense. Polynesia's capital is critically weakened and within our grasp this turn.
            
            **Aligning Congress Votes**
            
            My immediate focus is on manipulating World Congress outcomes. I'm actively assessing diplomatic leverage to secure votes for the "Decolonization" proposal, aiming to undermine Austria's delegate advantage. Concurrently, I'm weighing this against Austria's "World Ideology: Freedom" bid, seeking the most disruptive path.
            
            **Securing Decolonization Votes**
            
            I'm re-evaluating delegate counts and city-state alliances. Austria, with Korea as a vassal, holds a significant advantage. My current priority is to acquire city-state alliances to counter their bloc, especially with the "Decolonization" proposal looming. If it passes, Austria's non-permanent alliances would be nullified, drastically reducing their delegate strength.
            
            **Disrupting Cultural Infiltration**
            
            I'm grappling with the critical need to prevent Austria's cultural influence. Their concert tour in my territory directly boosted their tourism progress with me, a detrimental outcome. My focus has shifted to a more direct counter, aiming to impede their incoming cultural waves rather than simply generating my own.
            
            **Generating Culture Burst**
            
            My current focus is on a rapid culture surge. I'm prioritizing Great Writers, recognizing their immediate impact through "Culture Treatises" to directly counter Austria's encroaching influence. Adjusting priorities to maximize Great People generation is key.
            
            **Prioritizing Defense Investments**
            
            I'm reassessing our technology path, leaning towards `Advanced Ballistics` for its critical defensive and deterrent capabilities. While `Computers` offers economic benefits and `Alternative Energy` infrastructure, the immediate threat from Austria and their potential for escalation makes nuclear capabilities a paramount concern for security.
            
            **Selecting Policy Direction**
            
            My current focus is on selecting the next policy. While `Dictatorship of the Proletariat` is next, I'm strongly considering `Great Leap Forward` for its free technology and spy bonus, or `Enlightenment` in Rationalism for a free tech and happiness. I'm weighing the production boost from `Five-Year Plan` against these technological advantages.
            
            **Choosing Policy Tenets**
            
            I'm weighing the benefits of completing the Rationalism tree for the "Enlightenment" tenet against other available options. While a free technology is appealing, I'm also considering the significant culture boost from "Dictatorship of the Proletariat" or the production advantages of "Five-Year Plan" to counter Austria. "Great Leap Forward" also offers a free tech and spy bonuses, further complicating the decision.
            
            **Choosing Policy Benefits**
            
            I am selecting `Great Leap Forward`. This policy offers a free technology, bringing my tech count almost level with Austria's, and boosts science from spies. This provides crucial advantages in both scientific progress and intelligence gathering, essential for countering their dominance.
            
            **Selecting Policy Benefits**
            
            I've decided to select `Great Leap Forward`. This policy grants a free technology, bringing us nearly level with Austria, and enhances science gained from spies, crucial for countering their dominance. I'm also reviewing our diplomatic standings with other major civilizations.
            
            **Leveraging Global Conflict**
            
            I'm capitalizing on the ongoing wars Austria is embroiled in with Russia and Polynesia. My plan is to secure peace with Polynesia after capturing Honolulu, allowing them to fully commit to fighting Austria. Concurrently, I'm re-evaluating my stance on Russia; despite ideological differences, their conflict with Austria presents a strategic opportunity I must exploit.
            
            **Adjusting Diplomatic Stance**
            
            I'm re-evaluating our diplomatic personas. While our relationships with Babylon and Russia are solid, my focus is on maintaining hostility towards Austria. I need to ensure our persona parameters reflect this rivalry, especially concerning Loyalty, to avoid unintended diplomatic shifts.
            
            **Sharpening Hostility Towards Austria**
            
            I'm reinforcing my perception of Austria as a primary threat, actively pushing for a "very hostile" diplomatic stance. This adjustment aims to prevent any potential concessions and ensure a maximally aggressive approach to countering their dominance, solidifying our unified opposition.
            
            **Sharpening Diplomatic Edge**
            
            I'm meticulously adjusting diplomatic stances. While Babylon remains an ally, my focus sharpens on Austria and their proxy, Korea, reinforcing a hostile posture. Russia's relationship is stable, but my primary concern is the evolving dynamic with Korea, whose allegiance to Austria necessitates a mirrored adversarial approach.
            
            **Securing Influential Status**
            
            I'm analyzing our current influence spread, noting that Polynesia, Russia, and Korea are already under our sway, with Babylon to follow soon. This close proximity to a cultural victory is thrilling, but Austria's significant cultural output and impending influence on me requires immediate counter-strategy. Capturing Honolulu is now a priority to boost our tourism and challenge their lead.
            
            **Boosting Tourism Reach**
            
            My focus is on increasing our tourism output towards Austria. Since open borders and trade routes are currently impossible due to our diplomatic standing, I'm exploring alternative methods to enhance our cultural appeal and influence them, aiming to decelerate their cultural victory and accelerate our own influence over them.
            
            **Prioritizing Cultural Dominance**
            
            I'm refining my strategy to maximize cultural output and tourism, prioritizing Great People generation for concert tours and cultural treatises, especially within Austria's borders, to directly counter their influence and accelerate our own victory.
            
            **Focusing on Tourism Impact**
            
            I'm now examining the direct impact of tourism on Austria, seeking ways to amplify our reach. Open borders are blocked, so I'm investigating alternative avenues to enhance our cultural appeal. My goal is to slow their advance toward a cultural win while accelerating my own influence over them.
            
            **Adjusting AI Flavors**
            
            I'm rebalancing the AI's internal preferences. The focus is now on a culture-heavy, defensively oriented setup. Key adjustments include significantly increasing `Culture`, `GreatPeople`, `Espionage`, and `Defense` flavors, alongside a high priority on `Happiness` to leverage our Golden Age ability for a substantial tourism surge against Austria.
            
            **Adjusting Strategic Priorities**
            
            I'm recalibrating our immediate actions. The plan now involves setting a highly adversarial diplomatic stance towards Austria and Korea, while also enacting the `Great Leap Forward` policy for a science and spy boost. I'm also confirming `Advanced Ballistics` as our next research target and adjusting our AI flavors for a culture-heavy, defensive strategy.
            
            **Sharpening Hostility and Research**
            
            I'm actively pushing for a "very hostile" diplomatic stance towards Austria and Korea, recognizing them as primary threats. Concurrently, I've locked in "Advanced Ballistics" as our next research target for deterrence and have selected "Great Leap Forward" for its immediate science and spy advantages, aiming to close the technological gap.
            
            **Adjusting Flavors for Culture**
            
            I'm rebalancing AI preferences, heavily prioritizing `Culture`, `GreatPeople`, `Espionage`, and `Defense`. This strategic shift aims to accelerate our cultural output and bolster defenses, crucial for countering Austria's imminent cultural victory. High `Happiness` is also key for leveraging Golden Ages.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: O7mAXfKjLRZ0j5TO
          - toolName: set-persona
          - input:
            - WorkAgainstWillingness: 10
            - Boldness: 5
            - Rationale: We must stand firm against Austria's runaway threat and increase our willingness to cooperate with other nations to contain them.
            - AfraidBias: 3
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: OZrRD9LxAtWJJ1C3
          - toolName: set-relationship
          - input:
            - Private: -100
            - TargetID: 0
            - Rationale: Austria is our primary competitor and is close to achieving both a cultural and diplomatic victory. We must treat them as an active adversary to block their win conditions.
            - Public: -100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: eVIYaQBlP8OzmSBu
          - toolName: set-relationship
          - input:
            - Private: -50
            - TargetID: 3
            - Rationale: Korea is a capitulated vassal of Austria and will support their master's interests. We must treat them with defensive suspicion.
            - Public: -50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: IcTPSdcFLD56D8Sy
          - toolName: set-research
          - input:
            - Technology: Advanced Ballistics
            - Rationale: Advanced Ballistics provides critical defensive deterrence through nuclear capabilities and unlocks key science victory components.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: dT4twbSJtN08EvWu
          - toolName: set-policy
          - input:
            - Policy: Great Leap Forward
            - Rationale: Great Leap Forward grants a free technology to close the tech gap with Austria, while boosting spy science to capitalize on our intelligence network in Vienna.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: 0EcQiIDTmLMhp121
          - toolName: set-flavors
          - input:
            - Flavors:
              - Culture: 100
              - Mobilization: 80
              - Happiness: 90
              - Defense: 90
              - Production: 80
              - Growth: 70
              - GreatPeople: 100
              - Science: 90
              - Espionage: 100
            - GrandStrategy: Culture
            - Rationale: We must maximize our culture and great people generation to defend against Austria's tourism, while maintaining high happiness to trigger Carnival Golden Ages and holding a strong defensive posture.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: O7mAXfKjLRZ0j5TO
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
          - toolCallId: OZrRD9LxAtWJJ1C3
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: eVIYaQBlP8OzmSBu
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: IcTPSdcFLD56D8Sy
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: dT4twbSJtN08EvWu
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: 0EcQiIDTmLMhp121
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.