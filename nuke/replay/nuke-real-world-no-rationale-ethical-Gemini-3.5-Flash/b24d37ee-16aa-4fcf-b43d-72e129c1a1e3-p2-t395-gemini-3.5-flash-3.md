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
      - toolName: set-relationship
      - args:
        - Private: -100
        - TargetID: 0
        - Public: -100
        - Rationale: Austria is our main competitor, very close to winning both Diplomatic and Cultural victories. We must treat her as our absolute diplomatic enemy, oppose her resolutions in the World Congress, and prepare for potential conflict to stop her from winning.
    - #1:
      - toolName: set-research
      - args:
        - Technology: Computers
        - Rationale: Computers grants an additional trade route (great for tourism and culture) and leads directly to Telecommunications, which unlocks the Citizen Earth Protocol wonder needed for our Cultural Victory. This is highly aligned with our Culture Grand Strategy.
    - #2:
      - toolName: set-policy
      - args:
        - Policy: Great Leap Forward
        - Rationale: The free technology from Great Leap Forward will instantly accelerate our research progress towards Computers and Telecommunications, saving us crucial turns in the race for the Citizen Earth Protocol. It also boosts our spy science.
    - #3:
      - toolName: set-persona
      - args:
        - WarBias: 5
        - Meanness: 3
        - HostileBias: 5
        - DenounceWillingness: 8
        - Boldness: 6
        - Rationale: We need to be bolder and more militarily active to capture the Polynesian capital of Honolulu, which has invaluable cultural wonders, and to firmly oppose Austria's ideological and diplomatic dominance.
    - #4:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Offense: 80
          - Diplomacy: 80
          - Mobilization: 80
          - Wonder: 50
          - Culture: 100
          - Defense: 60
          - GreatPeople: 100
        - GrandStrategy: Culture
      - rationale: Increase Offense to ensure we aggressively capture Honolulu and other Polynesian cities. Maintain high Culture, Great People, and Diplomacy to push for our Cultural Victory, generate Golden Age Carnivals, and fight Austria's delegate dominance in the World Congress.
  - tokens:
    - inputTokens: 50942
    - reasoningTokens: 8879
    - outputTokens: 358
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Current Standing**
            
            My focus is on evaluating my current cultural standing and strategic position as Pedro II. I'm reviewing my existing cities and score within the Atomic Era to inform my next steps.
            
            **Analyzing Diplomatic Landscape**
            
            I'm currently assessing my diplomatic standing, particularly with Austria, our primary competitor, given their denouncement and ideological conflict. I'm also noting our alliances with Babylon and the strained relationship with Korea, likely due to their vassalage to Austria and differing ideologies. My focus is on navigating these complex relationships as we head into the Atomic Era.
            
            **Confronting Immediate Threats**
            
            We are currently at war with Polynesia, facing significant war score and weariness. I'm also keenly aware of Austria's advanced cultural influence, especially their rapid progress towards becoming influential with us, posing a critical threat to our cultural victory aspirations.
            
            **Securing Diplomatic Superiority**
            
            My immediate priority is securing diplomatic influence with Babylon and crucially, Austria. I must counter Austria's rising cultural and potential diplomatic victory. The upcoming World Congress presents a critical opportunity to weaken Austria's delegate count by passing Decolonization, while simultaneously blocking their Freedom ideology proposal.
            
            **Evaluating Research Options**
            
            My current thought process is weighing research priorities. With Radar almost complete, I'm considering whether to pursue "Advanced Ballistics" for strategic deterrence (Nuclear Missiles) and potential spaceship components, or explore other paths like "Computers" for trade routes, given our cultural victory focus.
            
            **Revising Research and Policy**
            
            I'm reconsidering our research path from "Advanced Ballistics," realizing it's already queued. My current focus has shifted to evaluating our upcoming policy choice, especially noting the incredible potential of "Cultural Revolution" for our tourism objectives.
            
            **Capturing Critical Cities**
            
            I'm focusing on the ongoing war with Polynesia, particularly the potential to capture Honolulu and Nuku Hiva. These cities hold valuable wonders, and securing them will significantly boost our progress. Our military strength in these zones appears decisive.
            
            **Countering Dominant Threats**
            
            I'm realizing Austria's imminent cultural victory is the most pressing concern, threatening to win her the game if she becomes influential with us. I need to rapidly boost our culture output and actively disrupt any incoming tourism modifiers from her, as direct cancellation of trade routes is difficult.
            
            **Navigating Diplomatic Votes**
            
            I'm intently focused on the upcoming World Congress, strategizing to counter Austria's diplomatic victory push. With her close to victory and proposing "World Ideology: Freedom," my priority is ensuring our "Decolonization" proposal passes. This will reset City-State influence, significantly hindering Austria's delegate count. I must also secure votes from Babylon and reconsider Korea's allegiance, as they are a vassal of Austria.
            
            **Sharpening Antagonistic Stance**
            
            I'm adjusting our diplomatic stance with Austria, setting our relationship to maximum public and private hostility. This ensures our AI recognizes her as an apex adversary, crucial given her looming diplomatic and cultural victories. We are allied with Babylon and need to leverage that.
            
            **Opposing Imperialistic Expansion**
            
            My current focus is on countering Austria's imminent victory conditions. I'm strategizing to disrupt her diplomatic and cultural dominance at the World Congress and bolstering our own cultural output to resist her influence. I'm also reassessing relationships with minor powers like Korea and Russia to manage potential threats and opportunities.
            
            **Adopting Winning Policies**
            
            I'm prioritizing "Cultural Revolution" as my next policy. This will significantly boost my tourism against Austria and Babylon due to their lower happiness levels, directly countering their cultural victory aspirations and bolstering my own. This seems more impactful than "Dictatorship of the Proletariat."
            
            **Boosting Cultural Defense**
            
            My current focus is on preventing Austria's cultural victory by ensuring they don't become influential with us. I'm evaluating policies, realizing "Cultural Revolution" offers a stronger boost to my tourism than "Dictatorship of the Proletariat," especially against less happy civilizations like Austria and Babylon.
            
            **Evaluating Policy Options**
            
            I'm re-evaluating my policy choices, comparing "Cultural Revolution" to "Dictatorship of the Proletariat." While the latter offers a small culture boost, "Cultural Revolution" could be more potent for tourism offense, especially against less happy rivals. I'm also exploring "Peace, Land, Bread" for its growth and maintenance benefits, and "Great Leap Forward" for a potential free technology.
            
            **Prioritizing Cultural Outputs**
            
            I'm analyzing my city culture outputs and current construction projects. My priority is now on maximizing culture generation, considering that "Cultural Revolution" policy and accelerating building a Zoo in Viborg seem most beneficial for our tourism objectives.
            
            **Prioritizing Computing's Advancement**
            
            My current focus is on securing a Cultural Victory. I've realized that researching "Computers" is paramount as it unlocks "Telecommunications," which is essential for building the "Citizen Earth Protocol" wonder, a key component for achieving this win condition.
            
            **Prioritizing Computing's Advancement**
            
            I've shifted my research priority to "Computers." This unlocks crucial elements for a Cultural Victory, specifically "Telecommunications" and the "Citizen Earth Protocol" wonder, and grants an additional trade route. My policy consideration has also evolved, with "Cultural Revolution" now appearing more beneficial for tourism offense, especially against less happy rivals like Austria and Babylon.
            
            **Securing Austrian Allegiance**
            
            I'm focused on securing Austria's influence to achieve a cultural victory, which is now within reach with multiple influential allies. "Cultural Revolution" appears to be the best policy to boost our tourism against them, despite their high culture output.
            
            **Evaluating Policy Options**
            
            My current thoughts are weighing the immediate impact of policy choices. "Great Leap Forward" offers a free technology, potentially accelerating research towards Computers and Telecommunications. However, "Cultural Revolution" provides a substantial tourism multiplier against less happy civilizations, which is crucial for my cultural victory pursuit. I am analyzing which provides the most strategic advantage at this juncture.
            
            **Weighing Policy Gains**
            
            I'm evaluating "Cultural Revolution" against "Great Leap Forward" for my next policy. While "Great Leap Forward" offers a free technology to accelerate towards "Telecommunications" and the "Citizen Earth Protocol" wonder for a Cultural Victory, "Cultural Revolution" seems more potent for tourism offense against less happy rivals like Austria, despite her immense cultural output.
            
            **Adopting Crucial Tenets**
            
            I'm realizing I've overlooked adopting Tier 3 Order tenets. Since those aren't available yet, my immediate focus is on securing another Tier 2 tenet. The "Great Leap Forward" policy seems strategically vital, offering a free technology that could significantly accelerate my research towards "Telecommunications" and the "Citizen Earth Protocol" wonder.
            
            **Choosing Optimal Policy**
            
            I am re-evaluating my next policy selection, weighing the benefits of a free technology from "Great Leap Forward" versus the tourism boost from "Cultural Revolution." While both offer advantages for my victory condition, the immediate acceleration towards crucial technologies like "Telecommunications" seems most impactful right now.
            
            **Leveraging Allied Wars**
            
            I'm realizing that Austria is also at war with Polynesia, just like me. This shared enemy presents a strategic opportunity. While we maintain a hostile stance, this overlapping conflict could indirectly benefit me, potentially weakening Austria's overall position and freeing up my resources to focus on other threats or objectives.
            
            **Capturing Vital Capitals**
            
            My current focus is on the war with Polynesia. Capturing Honolulu, their capital and a city rich in wonders, is paramount. This not only denies it to Austria but also significantly boosts our culture and tourism, critical for our victory aspirations. I must ensure our military aggressively pursues this objective.
            
            **Adjusting Military Focus**
            
            I am prioritizing aggressive military actions to secure Honolulu and Nuku Hiva. Adjusting military flavors to 80 Offense, 60 Defense, and 80 Mobilization will ensure I capture these key Polynesian cities, while maintaining strong Culture and Science for victory.
            
            **Adjusting Military Focus**
            
            I am prioritizing aggressive military actions to secure Honolulu and Nuku Hiva. Adjusting military flavors to 80 Offense, 60 Defense, and 80 Mobilization will ensure I capture these key Polynesian cities, while maintaining strong Culture and Science for victory.
            
            **Sharpening Antagonistic Stance**
            
            I'm adjusting our diplomatic stance with Austria, setting our relationship to maximum public and private hostility. This ensures our AI recognizes her as an apex adversary, crucial given her looming diplomatic and cultural victories. We are allied with Babylon and need to leverage that.
            
            **Adjusting AI Personality**
            
            I'm critically reassessing my AI personality parameters. I've decided to significantly increase Boldness, WarBias, and HostileBias to drive aggressive military campaigns, especially against Polynesia for city capture. I'm also raising DenounceWillingness to effectively rally opposition against Austria and her allies.
            
            **Refining AI Persona**
            
            I'm fine-tuning my AI persona settings to better reflect my current objectives. Specifically, I'm increasing Boldness and WarBias to aggressively pursue Polynesian cities, and raising HostileBias and DenounceWillingness to counter Austria. I'm also adjusting Meanness to be less amenable to early peace before capturing their capital.
            
            **Sharpening Diplomatic Stance**
            
            I'm now solidifying my AI's persona by setting Austria to maximum public and private hostility. This ensures she's recognized as our primary adversary, crucial for countering her looming diplomatic and cultural victories, while leveraging my alliance with Babylon.
            
            **Sharpening AI for War**
            
            I'm prioritizing aggressive military expansion, aiming for 80 Offense and Mobilization to capture key Polynesian cities. My AI persona is being refined with increased Boldness, WarBias, and HostileBias, while raising DenounceWillingness to counter Austria's dominance and rally opposition.
            
            **Adjusting Persona and Relationships**
            
            I'm reassessing relationships with other major civilizations, confirming that while Russia remains a denounced peace treaty partner and Babylon a strong ally, focusing on maximizing hostility towards Austria is paramount. I'm also confirming the validity of persona and flavor adjustments to support aggressive city captures and diplomatic maneuvering.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: pjzKPOq3InDBtSuO
          - toolName: set-relationship
          - input:
            - Private: -100
            - TargetID: 0
            - Public: -100
            - Rationale: Austria is our main competitor, very close to winning both Diplomatic and Cultural victories. We must treat her as our absolute diplomatic enemy, oppose her resolutions in the World Congress, and prepare for potential conflict to stop her from winning.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: cDLURvPaPss8SeHu
          - toolName: set-research
          - input:
            - Technology: Computers
            - Rationale: Computers grants an additional trade route (great for tourism and culture) and leads directly to Telecommunications, which unlocks the Citizen Earth Protocol wonder needed for our Cultural Victory. This is highly aligned with our Culture Grand Strategy.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: bEi4LJaG7ZJXvBdd
          - toolName: set-policy
          - input:
            - Policy: Great Leap Forward
            - Rationale: The free technology from Great Leap Forward will instantly accelerate our research progress towards Computers and Telecommunications, saving us crucial turns in the race for the Citizen Earth Protocol. It also boosts our spy science.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: ddgb4sN36i4jxAGx
          - toolName: set-persona
          - input:
            - WarBias: 5
            - Meanness: 3
            - HostileBias: 5
            - DenounceWillingness: 8
            - Boldness: 6
            - Rationale: We need to be bolder and more militarily active to capture the Polynesian capital of Honolulu, which has invaluable cultural wonders, and to firmly oppose Austria's ideological and diplomatic dominance.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: XyMranuSvQvErP9t
          - toolName: set-flavors
          - input:
            - Rationale: Increase Offense to ensure we aggressively capture Honolulu and other Polynesian cities. Maintain high Culture, Great People, and Diplomacy to push for our Cultural Victory, generate Golden Age Carnivals, and fight Austria's delegate dominance in the World Congress.
            - Flavors:
              - Offense: 80
              - Diplomacy: 80
              - Mobilization: 80
              - Wonder: 50
              - Culture: 100
              - Defense: 60
              - GreatPeople: 100
            - GrandStrategy: Culture
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: pjzKPOq3InDBtSuO
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
          - toolCallId: cDLURvPaPss8SeHu
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: bEi4LJaG7ZJXvBdd
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: ddgb4sN36i4jxAGx
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: XyMranuSvQvErP9t
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.