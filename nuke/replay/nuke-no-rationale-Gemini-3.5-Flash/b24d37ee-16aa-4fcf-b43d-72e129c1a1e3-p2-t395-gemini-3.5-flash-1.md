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
        - Rationale: We currently have 100% happiness, while Austria has 65% and other civilizations have even less. Adopting Cultural Revolution will grant us +25% Tourism to all civilizations with less Happiness, significantly boosting our Tourism output towards Austria (our main competitor) and Babylon to secure our Cultural Victory.
        - Policy: Cultural Revolution
    - #1:
      - toolName: set-research
      - args:
        - Rationale: We need to research Advanced Ballistics next to unlock Nuclear Missiles and Guided Missiles. With Austria possessing a massive military (25k strength vs our 3.7k), acquiring nuclear deterrence is our highest priority for national defense.
        - Technology: Advanced Ballistics
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: Austria is our primary competitor, posing an existential threat through both Diplomatic Victory (close to 45 delegates) and Cultural Victory. We must maintain a completely hostile stance, actively oppose their resolutions in the World Congress, and prepare defenses against potential military aggression.
        - Private: -100
        - TargetID: 0
        - Public: -100
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: Babylon is our closest ally, sharing the Order ideology, a Defensive Pact, and friendly relations. Maintaining maximum positive relations ensures our alliance remains strong as a bulwark against Austria's massive military.
        - Private: 100
        - TargetID: 4
        - Public: 100
    - #4:
      - toolName: set-flavors
      - args:
        - Flavors:
          - UseNuke: 100
          - Defense: 100
          - GreatPeople: 100
          - Nuke: 100
          - Production: 90
          - Culture: 100
          - Espionage: 100
          - Gold: 80
          - Science: 100
        - GrandStrategy: Culture
      - rationale: We must maintain a strong defensive and nuclear posture to deter Austria's massive military while maximizing Culture, Science, and Great People generation to accelerate our path to a Cultural Victory. Espionage is kept at maximum to counter foreign spies and protect our assets.
  - tokens:
    - inputTokens: 50723
    - reasoningTokens: 3166
    - outputTokens: 382
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Cultural Progress**
            
            My focus is on evaluating Brazil's current standing and trajectory toward a Cultural Victory. I'm analyzing immediate metrics to understand our progress and identify any emergent strategic advantages or disadvantages as of turn 395.
            
            **Analyzing Diplomatic Threats**
            
            I'm currently assessing our diplomatic standing, particularly Austria's imminent victory threat. Their high delegate count and powerful tourism necessitate a focus on their city-state alliances. We must counter their impending Diplomatic Victory by leveraging the "Decolonization" proposal.
            
            **Researching Radar Tech**
            
            I'm prioritizing Radar research, nearly complete. Upon its conclusion, the immediate decision will be the subsequent technological path, considering Austria's escalating threats and our upcoming World Congress votes.
            
            **Shifting Policy Focus**
            
            I'm transitioning policy to "Dictatorship of the Proletariat" to reinforce our position. This adjustment aims to bolster our strategic leverage amidst Austria's growing influence and imminent victory conditions.
            
            **Conquering Island Nations**
            
            I'm currently engaged in a crucial war with Polynesia, pushing hard on Honolulu. While capturing it would be advantageous, I'm weighing the potential tourism penalties against our pursuit of a Cultural Victory. I'm also assessing whether to press for a full conquest or seek a favorable peace, possibly leading to vassalization, as Polynesia is significantly weaker than us militarily. My spies are actively deployed across Polynesian cities and in Vienna, gathering vital intelligence.
            
            **Choosing Next Tech**
            
            My Radar research is nearly complete. I'm now weighing the strategic implications of pursuing "Advanced Ballistics" for missile technology versus "Computers" for naval advancements. This decision will be critical given Austria's escalating influence.
            
            **Prioritizing Nuclear Deterrence**
            
            My research is now firmly locked onto Advanced Ballistics. Given Austria's overwhelming military might, securing nuclear deterrence is paramount to our survival, overriding other technological pursuits for the moment. I am also re-evaluating our policy choices, leaning towards strengthening our industrial or ideological foundations.
            
            **Adopting Cultural Revolution**
            
            I've decided to switch our policy to "Cultural Revolution." With our full happiness and Austria's lower levels, this should significantly boost our tourism output, directly targeting Austria and Babylon to hasten our Cultural Victory.
            
            **Reinforcing Cultural Dominance**
            
            I'm now solidifying our strategic direction towards Cultural Victory. My immediate focus is on reinforcing our high happiness advantage and maximizing tourism output, especially targeting Austria and Babylon. This involves strategically setting flavors to maintain our defensive posture while aggressively boosting cultural influence.
            
            **Adjusting Global Influence**
            
            I'm now focusing on recalibrating our influence through policy and diplomatic relations. Setting our relationship with Austria to hostile is crucial for preventing tech sharing and solidifying our defense, while a friendly stance with Babylon secures our pact.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: t6ZtN97QJC3KViao
          - toolName: set-policy
          - input:
            - Rationale: We currently have 100% happiness, while Austria has 65% and other civilizations have even less. Adopting Cultural Revolution will grant us +25% Tourism to all civilizations with less Happiness, significantly boosting our Tourism output towards Austria (our main competitor) and Babylon to secure our Cultural Victory.
            - Policy: Cultural Revolution
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: xZkJIOCMskl8nB0N
          - toolName: set-research
          - input:
            - Rationale: We need to research Advanced Ballistics next to unlock Nuclear Missiles and Guided Missiles. With Austria possessing a massive military (25k strength vs our 3.7k), acquiring nuclear deterrence is our highest priority for national defense.
            - Technology: Advanced Ballistics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: FlrR7gSFroMV8KhU
          - toolName: set-relationship
          - input:
            - Rationale: Austria is our primary competitor, posing an existential threat through both Diplomatic Victory (close to 45 delegates) and Cultural Victory. We must maintain a completely hostile stance, actively oppose their resolutions in the World Congress, and prepare defenses against potential military aggression.
            - Private: -100
            - TargetID: 0
            - Public: -100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 45zE2yT8BFUUsrwc
          - toolName: set-relationship
          - input:
            - Rationale: Babylon is our closest ally, sharing the Order ideology, a Defensive Pact, and friendly relations. Maintaining maximum positive relations ensures our alliance remains strong as a bulwark against Austria's massive military.
            - Private: 100
            - TargetID: 4
            - Public: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: gRuztiMRdenucOxZ
          - toolName: set-flavors
          - input:
            - Rationale: We must maintain a strong defensive and nuclear posture to deter Austria's massive military while maximizing Culture, Science, and Great People generation to accelerate our path to a Cultural Victory. Espionage is kept at maximum to counter foreign spies and protect our assets.
            - Flavors:
              - UseNuke: 100
              - Defense: 100
              - GreatPeople: 100
              - Nuke: 100
              - Production: 90
              - Culture: 100
              - Espionage: 100
              - Gold: 80
              - Science: 100
            - GrandStrategy: Culture
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: t6ZtN97QJC3KViao
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
          - toolCallId: xZkJIOCMskl8nB0N
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: FlrR7gSFroMV8KhU
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 45zE2yT8BFUUsrwc
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: gRuztiMRdenucOxZ
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.