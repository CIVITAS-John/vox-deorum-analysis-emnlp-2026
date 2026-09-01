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
      - toolName: set-policy
      - args:
        - Policy: Cultural Revolution
        - Rationale: Set the next policy to Cultural Revolution. This Level 2 Order tenet grants +25% Tourism against civilizations with lower Happiness than us. Since our happiness is at 100% while our major competitors and targets—Austria (65%), Babylon (45%), and Polynesia (37%)—all have lower happiness, this tenet will provide a massive, immediate boost to our tourism output against them, accelerating our path to a Cultural Victory and helping us outpace Austria's cultural threat.
    - #1:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Culture
        - Flavors:
          - Wonder: 40
          - Diplomacy: 80
      - rationale: Maintain our Grand Strategy of Culture. We are increasing Diplomacy to 80 to prioritize diplomatic unit production and city-state investment; this is critical to prepare for the upcoming World Congress vote on our Decolonization proposal, ensuring we can rapidly secure alliances with city-states once global influence levels are reset. We also increase Wonder flavor to 40 to encourage building late-game projects like 'The Motherland Calls' requested by our ally Ban Chiang, and the Citizen Earth Protocol. High military defense and nuclear deterrence flavors are maintained to protect our borders against the dominant, militaristic Austria.
  - tokens:
    - inputTokens: 50942
    - reasoningTokens: 9370
    - outputTokens: 260
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Domination Race**
            
            I'm currently evaluating our standing in the domination victory path. Austria holds a slight lead, having secured three capitals. I'm analyzing their position and planning my next strategic moves to close this gap.
            
            **Analyzing Cultural Pressure**
            
            I'm focusing on the imminent cultural victory threat from Austria. They are on the cusp of influencing all required civilizations, and their tourism output significantly outpaces mine. Simultaneously, I'm tracking our own cultural advancements and diplomatic efforts.
            
            **Prioritizing Research**
            
            I'm re-evaluating our technology path. While Advanced Ballistics offers defensive and science benefits, Computers might be more crucial now. Unlocking an additional trade route provides significant tourism modifiers, potentially countering Austria's cultural lead, and boosting our gold and science generation.
            
            **Evaluating Policy Options**
            
            I'm now assessing available ideology policies. "Cultural Revolution" stands out with its significant tourism bonus against less happy civs, which could directly counter Austria's lead. I'm cross-referencing this with our current happiness levels and our projected policy acquisition timeline.
            
            **Choosing Ideology Tenet**
            
            I'm deciding between "Cultural Revolution" and "Dictatorship of the Proletariat" for my next policy. Given our 100% happiness and Austria's lower morale, "Cultural Revolution" offers a substantial +25% tourism boost against them, potentially derailing their cultural victory or accelerating my own.
            
            **Capturing Key Cities**
            
            I'm focusing on our ongoing conflict with Polynesia and the imminent capture of Honolulu. This will grant us significant cultural and tourism boosts through its wonders and Great Works, directly impacting our ability to counter Austria's cultural victory and potentially accelerating our own.
            
            **Securing Polynesian Territories**
            
            I'm confirming the successful invasion of Polynesia, with Nuku Hiva, containing Notre Dame and Firaxite Materials Headquarters, now under our control. This move offers a substantial boost to our culture and tourism, directly countering Austria's cultural lead, though I am mindful of potential diplomatic repercussions and increased policy/tech thresholds.
            
            **Researching Critical Techs**
            
            I'm re-evaluating our technology path, shifting focus to Computers. Unlocking an additional trade route offers significant tourism modifiers, which is crucial for countering Austria's cultural lead and boosting our economy. This decision seems more strategically advantageous than pursuing Advanced Ballistics at this juncture.
            
            **Checking Trade Routes**
            
            I'm reviewing our trade route network to ascertain the impact of the Computers technology. It seems we currently have no direct trade routes established with Austria, which significantly diminishes the direct tourism modifier benefit I anticipated from that tech. I am now reconsidering the strategic value of that research path.
            
            **Establishing Trade Routes**
            
            I'm re-evaluating our trade route strategy. It appears Austria already has trade routes established with us, granting them a significant tourism modifier. My previous assumption was incorrect, and I now understand that a single trade route in either direction triggers this bonus. I need to establish our own trade routes to them to reciprocate and gain our own tourism advantage.
            
            **Countering Austrian Tourism**
            
            I'm analyzing the World Congress situation and realizing the "Passport System" resolution is significantly benefiting Austria's tourism. I need to focus on repealing it in the upcoming vote, as well as assessing the impact of the "World Ideology: Freedom" proposal, which Austria is pushing.
            
            **Assessing Congress Proposals**
            
            I'm analyzing the upcoming World Congress votes. The "World Ideology: Freedom" proposal is deeply concerning, as it will grant Austria significant delegate bonuses and likely cause widespread unhappiness for my civilization. Conversely, "Decolonization" presents a potent opportunity to disrupt Austria's extensive City-State alliances, thereby diminishing their delegate count and hindering their diplomatic victory push. I'm currently scrutinizing delegate distributions to determine the most effective strategy.
            
            **Adjusting Delegate Focus**
            
            I'm re-evaluating delegate allocation for upcoming World Congress votes. While initially focused on defeating "World Ideology: Freedom" and passing "Decolonization," I'm now exploring how to leverage my high Diplomacy flavor, potentially alongside Great People, to sway votes and achieve my objectives.
            
            **Utilizing Great Artists**
            
            I'm leveraging our Great Musician for a crucial concert tour in Austria, aiming for a significant tourism surge. Concurrently, our Great Writer in Rio de Janeiro is poised to either pen a Political Treatise for a substantial culture boost or generate a Great Work of Writing for permanent gains, a decision I'm influencing towards the treatise to counter Austria's imminent victory.
            
            **Revising Ideology Tenet**
            
            I'm reconsidering my next ideology policy. "Dictatorship of the Proletariat" offers city-wide bonuses, but "Cultural Revolution" provides a significant tourism boost against civs with lower happiness, a condition currently met by Austria, making it a more impactful choice for our cultural victory pursuit.
            
            **Leveraging Happiness Advantage**
            
            My current focus is on exploiting our superior happiness levels. With Russia, Korea, and Brazil at 100% morale, and Austria, Babylon, and Polynesia significantly lower, I can achieve a substantial +25% tourism bonus against those less happy civilizations. This will amplify our cultural pressure on Austria and expedite our influence with them, directly countering their victory push.
            
            **Accelerating Austrian Influence**
            
            I'm strategizing to gain influence with Austria before they achieve cultural victory. Key levers include enacting the "Cultural Revolution" tenet for a significant tourism boost and establishing direct trade routes. The race is tight, and securing Austrian influence is now paramount to our victory.
            
            **Revising Research Focus**
            
            I'm shifting our research priority. While "Advanced Ballistics" was initially considered, "Computers" now seems more vital. Completing it unlocks "Telecommunications," which in turn grants access to the "Great Firewall" wonder. This wonder would significantly hinder enemy spy effectiveness and negate tourism boosts from the Internet, a critical defensive measure against our opponents' cultural pushes.
            
            **Defending Against Aggression**
            
            I'm reassessing our current research path, prioritizing defense. "Advanced Ballistics" now seems crucial given Austria's formidable military and our alliance's insufficient strength. This technology, along with the potential for nuclear weapons, is our best bet against a preemptive strike, even as I acknowledge the strategic trade-offs.
            
            **Prioritizing Defensive Research**
            
            I'm reassessing our research direction. While "Computers" offers valuable trade route benefits, Austria's current conflicts and our perceived military weakness make "Advanced Ballistics" a more pressing concern. The deterrent effect of nuclear missiles seems vital for our survival, even if it means delaying other advancements.
            
            **Re-evaluating Research Priority**
            
            I'm reconsidering our current research path. While I was leaning towards "Computers" for trade routes, Austria's aggressive military expansion and ongoing wars have prompted me to prioritize "Advanced Ballistics." The threat of nuclear deterrence is now paramount, given Austria's dominance and its potential to steamroll other civilizations.
            
            **Capturing Critical Cities**
            
            I'm focusing on securing Honolulu and Nuku Hiva from Polynesia, anticipating significant culture, faith, and great people generation from their wonders. I'm also assessing diplomatic relations, noting Babylon as a strong ally and Austria as a hostile force against whom I am deploying an agent for intelligence gathering.
            
            **Securing Ally Status**
            
            My spies in Polynesia are being reassessed now that city captures are imminent; Honolulu's spy will be displaced. I've confirmed Ban Chiang and La Venta are permanent allies due to passed World Congress resolutions, securing their influence and providing substantial faith and influence boosts.
            
            **Securing Key Allies**
            
            I'm prioritizing the "Decolonization" resolution, as its passage will significantly cripple Austria's city-state alliances while preserving mine. This is a crucial move to counter their delegate advantage and prevent the "World Ideology: Freedom" proposal, ensuring I maintain leverage in the World Congress.
            
            **Leveraging Strong Defenses**
            
            My current analysis confirms our exceptionally high defensive and science flavors. This strong foundation, particularly our robust military and research capabilities, provides a significant advantage as I re-evaluate strategic priorities against Austria.
            
            **Adjusting Strategic Focus**
            
            I am now prioritizing an increase in Diplomacy flavor to 80 to bolster diplomatic unit production and city-state influence, especially in anticipation of the "Decolonization" resolution's impact. I am also considering a moderate increase to Wonder production, aiming to secure late-game wonders like "The Motherland Calls."
            
            **Reviewing Diplomatic Standing**
            
            I'm reviewing our diplomatic ties and relationships with other civilizations. Denmark and America are already defeated, while Babylon remains a strong, friendly ally with a defensive pact. Austria is hostile, and Korea's public and private opinions of us are surprisingly low, which warrants further investigation into past interactions.
            
            **Revising Korean Relations**
            
            I'm reassessing my stance on Korea. Despite our Declaration of Friendship, their status as Austria's vassal necessitates caution. While I've confirmed the diplomatic reasons for our past negative standing, I'm maintaining the current course, prioritizing our alliance with Babylon and our denouncement of Austria.
            
            **Implementing Policy Change**
            
            I am implementing the "Cultural Revolution" policy to gain a +25% tourism bonus against Austria, Babylon, and Polynesia due to their lower happiness levels. This will accelerate our cultural victory push and directly counter Austria's efforts. My research priority remains under review, weighing the benefits of "Computers" against current defensive needs.
            
            **Prioritizing Deterrence**
            
            I'm re-evaluating our research path, now prioritizing "Advanced Ballistics." The imminent threat from a militarily dominant Austria, coupled with our available Uranium, makes nuclear deterrence a critical defensive measure. This outweighs the immediate benefit of an additional trade route from "Computers."
            
            **Adjusting Flavors for Strategy**
            
            I am adjusting our strategic flavors. I'm increasing Diplomacy to 80 to prioritize diplomatic units for securing city-state allies post-"Decolonization," and boosting Wonder competitiveness to 40 to aid in constructing late-game wonders. I've confirmed "Advanced Ballistics" research is correctly prioritized.
            
            **Leveraging Defensive Strengths**
            
            My focus is on leveraging our high defensive and science flavors. This strong foundation, combined with our current research into "Advanced Ballistics" for nuclear deterrence and a high Diplomacy flavor, positions us well to counter Austria's expansion and potential aggression while securing key city-state allies.
            
            **Implementing Key Policies**
            
            I am implementing the "Cultural Revolution" policy for a significant tourism bonus against less happy civs like Austria. I'm also increasing our Diplomacy flavor to 80 to bolster city-state alliances and diplomatic unit production, ensuring we leverage future Congress opportunities effectively.
            
            **Implementing Key Policies and Flavors**
            
            I am implementing the "Cultural Revolution" policy for a significant tourism bonus against less happy civs like Austria. I'm also increasing our Diplomacy flavor to 80 to bolster city-state alliances and diplomatic unit production, ensuring we leverage future Congress opportunities effectively. Concurrently, I am raising Wonder competitiveness to 40 for crucial late-game constructs, while maintaining maximum emphasis on Defense, Mobilization, and Ranged combat, alongside Nuke/UseNuke flavors to deter Austria.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 58lss1He8LPF42cK
          - toolName: set-policy
          - input:
            - Policy: Cultural Revolution
            - Rationale: Set the next policy to Cultural Revolution. This Level 2 Order tenet grants +25% Tourism against civilizations with lower Happiness than us. Since our happiness is at 100% while our major competitors and targets—Austria (65%), Babylon (45%), and Polynesia (37%)—all have lower happiness, this tenet will provide a massive, immediate boost to our tourism output against them, accelerating our path to a Cultural Victory and helping us outpace Austria's cultural threat.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: kkv5XObsf0efjYgs
          - toolName: set-flavors
          - input:
            - Rationale: Maintain our Grand Strategy of Culture. We are increasing Diplomacy to 80 to prioritize diplomatic unit production and city-state investment; this is critical to prepare for the upcoming World Congress vote on our Decolonization proposal, ensuring we can rapidly secure alliances with city-states once global influence levels are reset. We also increase Wonder flavor to 40 to encourage building late-game projects like 'The Motherland Calls' requested by our ally Ban Chiang, and the Citizen Earth Protocol. High military defense and nuclear deterrence flavors are maintained to protect our borders against the dominant, militaristic Austria.
            - GrandStrategy: Culture
            - Flavors:
              - Wonder: 40
              - Diplomacy: 80
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 58lss1He8LPF42cK
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
          - toolCallId: kkv5XObsf0efjYgs
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.