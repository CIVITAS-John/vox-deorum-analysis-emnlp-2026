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
      - toolName: set-research
      - args:
        - Technology: Computers
        - Rationale: Computers grants an additional Trade Route, which is crucial for establishing tourism modifiers with other civilizations. It also leads directly to Telecommunications and Satellites, which are on the path to the Citizen Earth Protocol wonder required for our Cultural Victory.
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Cultural Revolution
        - Rationale: Cultural Revolution is a Level 2 Tenet of Order that provides +25% Tourism to civilizations with less Happiness. Since our happiness is at 100%, this will grant a massive +25% Tourism modifier against almost all opponents, including our main competitor Austria, significantly accelerating our progress toward a Cultural Victory.
    - #2:
      - toolName: set-persona
      - args:
        - Rationale: Increasing our Loyalty ensures that our AI maintains our critical friendship and Defensive Pact with Babylon, who is our sole major ally, buffer state, and fellow Order follower against the Freedom-aligned superpower Austria.
        - Loyalty: 8
    - #3:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Culture
        - Flavors:
          - Air: 100
          - Espionage: 100
          - Nuke: 100
          - CityDefense: 100
          - Gold: 70
          - UseNuke: 95
          - Antiair: 100
          - Culture: 100
          - Mobilization: 100
          - Science: 100
          - Defense: 100
          - Production: 90
          - GreatPeople: 100
          - Diplomacy: 80
          - Wonder: 90
      - rationale: We maintain our Culture Grand Strategy to push for a Cultural Victory. We increase our Wonder flavor to 90 to make effective use of our Great Engineer and secure key late-game wonders. Great People is raised to 100 to maximize Great Writers/Artists/Musicians for Tourism. Diplomacy is raised to 80 to help secure city-state influence and prepare for the upcoming critical World Congress votes (passing Decolonization and blocking Freedom). Defensive and military flavors remain at maximum to ensure we successfully complete our war with Polynesia and deter any potential aggression from Austria.
  - tokens:
    - inputTokens: 50759
    - reasoningTokens: 10297
    - outputTokens: 393
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Victory Pathways**
            
            My focus is on evaluating our current standing. With Austria holding significant capitals, I'm weighing our options for achieving a domination victory. I'm also considering how to counter Russia's growing influence.
            
            **Blocking Austrian Dominance**
            
            I'm currently assessing our options to prevent Austria from achieving a cultural victory. Their influence is substantial, and their tourism output dwarfs ours. I'm exploring immediate tactical maneuvers to disrupt their progress and buy us time, considering the limited window before they become influential with us.
            
            **Navigating Ideological Shifts**
            
            I'm re-evaluating our diplomatic strategy in light of the upcoming World Congress vote. Austria's push for "World Ideology: Freedom" poses a significant threat to our current standing, and I'm focused on ensuring our "Decolonization" proposal passes to undermine their allied delegate count and slow their diplomatic victory path. I am also assessing the immediate gains versus long-term drawbacks of capturing Polynesian cities, particularly their Great Works.
            
            **Securing Key Territories**
            
            I'm prioritizing the consolidation of our position by taking Polynesian cities, given our ongoing war and their proximity. This will allow us to eliminate them or integrate their territory. I'm also reassessing our current city count and strategic locations.
            
            **Evaluating Ideology Options**
            
            I'm reassessing our chosen ideology tenet. While "Cultural Revolution" offers a tourism boost against less happy civs like Babylon and Polynesia, I'm weighing the benefits of "Great Leap Forward" for a free technology or "Five-Year Plan" for production. "Enlightenment" is also a strong contender for its late-game tech advantage.
            
            **Adopting New Policies**
            
            I'm currently reviewing our ideological framework. With Rationalism and Progress nearing completion, I'm focused on selecting the most impactful level two tenets. I'm weighing the merits of "Great Leap Forward" for technology versus "Five-Year Plan" for production, considering our current strategic needs.
            
            **Choosing Ideology Path**
            
            I'm re-evaluating our policy choices, particularly the selection of the next level two tenet. The potential of "Enlightenment" for a free technology is appealing, but I'm also strongly considering "Great Leap Forward" due to its significant science bonuses and spy advantage. My next step is to determine the optimal timing and strategy for implementing this policy change.
            
            **Boosting Production Significantly**
            
            I'm realizing a massive production boost is now available through the combined effects of certain policies and improvements. I'm evaluating whether to embrace this newfound power immediately or shift my current research and policy selections to maximize its impact, especially given our upcoming technologies like Radar and Advanced Ballistics.
            
            **Redirecting Research Efforts**
            
            I'm re-evaluating our current technology path, questioning the pursuit of Advanced Ballistics. The discovery of Computers offers significant benefits, particularly an additional trade route which directly boosts our tourism, a critical component for Brazil. This shift could accelerate our cultural victory and provide broader economic and scientific advantages.
            
            **Prioritizing Defensive Technologies**
            
            I'm reassessing our technology trajectory, concluding that prioritizing Advanced Ballistics is crucial. Given Austria's overwhelming military superiority and our hostile relationship, securing nuclear and guided missiles is paramount for deterrence and survival, outweighing the immediate tourism benefits of Computers.
            
            **Assessing Threat Levels**
            
            I'm reassessing our current situation, recognizing Austria's immense military advantage. Given our high defensive and nuclear flavors, prioritizing Advanced Ballistics for deterrence is now critical. We have the uranium to back it up, and the ongoing war with Polynesia is progressing well.
            
            **Securing Victory Resources**
            
            I'm focusing on leveraging our successes against Polynesia to secure crucial wonders and Great Works. This strategic acquisition directly bolsters our tourism and culture, accelerating our path to a cultural victory. I'm also evaluating the implications of our expanded territory and its proximity to Austria, while noting our strong alliances with Babylon and the complexities introduced by Korea's vassalage.
            
            **Exploiting Austrian Distractions**
            
            I'm recognizing a significant strategic opening. Austria is now engaged in wars with both Russia and Polynesia, which is diverting their military focus and presenting a prime opportunity to advance our own objectives. I'm assessing how best to leverage this multi-front conflict to our advantage.
            
            **Managing Russian Relations**
            
            I'm evaluating our stance with Russia. Despite their Freedom ideology and recent denouncement, I want to maintain a friendly posture to prevent a two-front war. I'm considering using `set-relationship` to manage our public and private diplomatic modifiers with them, aiming for a neutral or slightly positive standing.
            
            **Revising Diplomatic Posture**
            
            I'm reassessing our relationships, particularly with Austria and its vassal Korea. Given Austria's overwhelming military, I want to avoid direct conflict and maintain a strategic rivalry. Korea's strong friendship with us, despite vassalage, presents a diplomatic nuance I'm considering how to leverage.
            
            **Adopting New Technologies**
            
            I'm reassessing our policy choices again. Both "Enlightenment" and "Great Leap Forward" offer free technologies, which is incredibly valuable late-game. I'm exploring the possibility of acquiring both sequentially to maximize our scientific advantage and reach critical military or wonder techs faster.
            
            **Leveraging Great Person Contributions**
            
            I'm shifting my focus from production and general science boosts to maximizing the impact of our Great People. The recent acquisition and strategic use of Great Writers and Musicians are proving highly effective for accelerating our tourism, which is now paramount for a cultural victory.
            
            **Maximizing Tourism Output**
            
            I'm focusing on a direct tourism multiplier. "Cultural Revolution" offers a significant boost to civilizations with lower happiness, and I've identified Austria and Babylon as prime targets to leverage this for a faster cultural victory.
            
            **Maximizing Tourism Bonuses**
            
            I'm confirming that "Cultural Revolution" provides a significant tourism bonus against Austria due to their lower happiness levels compared to our own. This will greatly accelerate our cultural victory pursuit.
            
            **Selecting Cultural Tenet**
            
            I've concluded that "Cultural Revolution" is the optimal policy choice. Its direct tourism bonus against less happy civilizations like Austria and Babylon will significantly accelerate our cultural victory. I'm now confirming this selection.
            
            **Establishing Trade Relations**
            
            I'm confirming that sending a trade route to Austria is crucial for maximizing our tourism bonus, and I've discovered that their incoming routes to us also grant a significant modifier. I'm now verifying the precise mechanics of this interaction in Vox Populi.
            
            **Establishing Trade Routes**
            
            I've confirmed that trade routes with Austria, despite our denouncements, are possible and significantly boost our tourism. I'm now re-evaluating the "Passport System" resolution's impact and comparing the benefits of the "Computers" technology to maximize our cultural victory pursuit.
            
            **Prioritizing Defensive Technologies**
            
            I'm reassessing our technology trajectory, concluding that prioritizing Advanced Ballistics is crucial. Given Austria's overwhelming military superiority and our hostile relationship, securing nuclear and guided missiles is paramount for deterrence and survival, outweighing the immediate tourism benefits of Computers.
            
            **Researching Wonder Requirements**
            
            I'm now focused on the requirements for the "Citizen Earth Protocol" wonder, specifically which technology unlocks it. My current hypothesis points towards late-game techs like Telecommunications or Satellites, which is crucial for my cultural victory pursuit.
            
            **Prioritizing Computers Tech**
            
            My current focus is on research, and I've confirmed "Computers" is the superior choice for our cultural victory. It unlocks crucial technologies like Telecommunications and Satellites, and provides an extra trade route for increased tourism. I'm switching research accordingly.
            
            **Adjusting Wonder Prioritization**
            
            I'm reassessing our wonder prioritization. With a Great Engineer ready and the "Citizen Earth Protocol" in sight, I realize my current wonder flavor is too low. I'm adjusting this to 90 to ensure we actively pursue key wonders, especially given our cultural victory goal.
            
            **Leveraging Diplomatic Weight**
            
            I'm prioritizing diplomatic efforts to counter Austria's overwhelming delegate advantage. With the World Congress voting soon, my focus is on ensuring our "Decolonization" proposal passes, which could reset city-state influence and disrupt Austria's strategy. I am assessing our delegate count and potential alliances.
            
            **Leveraging City-State Dynamics**
            
            I've realized that many of Austria's seemingly permanent city-state alliances aren't actually locked in. If the "Decolonization" resolution passes, Austria will immediately lose a significant number of delegates, drastically weakening their position and opening up a crucial opportunity for us.
            
            **Boosting Diplomatic Leverage**
            
            I'm enhancing our diplomatic influence by raising our Diplomacy flavor to 80, aiming to secure the crucial "Decolonization" resolution. This, combined with maintaining high defensive flavors due to Austria's threat, is key. I've also set research to "Computers" and selected "Cultural Revolution" as our next Order tenet for maximum tourism gain.
            
            **Executing Diplomatic and Research Tools**
            
            I'm now implementing the finalized strategy. The research has been shifted to "Computers," and I'm preparing to deploy our Great Engineer. Furthermore, I'm confirming our diplomatic relationships require no adjustments, ensuring our posture aligns perfectly with our objectives before executing the remaining tools.
            
            **Refining Victory Strategy**
            
            I'm now focusing on the precise parameters for enacting our finalized strategy. This involves confirming the "Computers" research for the vital trade route and tourism modifiers, selecting "Cultural Revolution" to maximize our tourism against less happy opponents like Austria, and adjusting our loyalty settings to maintain key alliances.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: urUov5TuHSh6HXSR
          - toolName: set-research
          - input:
            - Technology: Computers
            - Rationale: Computers grants an additional Trade Route, which is crucial for establishing tourism modifiers with other civilizations. It also leads directly to Telecommunications and Satellites, which are on the path to the Citizen Earth Protocol wonder required for our Cultural Victory.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: rWx7W19FP6zaawT9
          - toolName: set-policy
          - input:
            - Policy: Cultural Revolution
            - Rationale: Cultural Revolution is a Level 2 Tenet of Order that provides +25% Tourism to civilizations with less Happiness. Since our happiness is at 100%, this will grant a massive +25% Tourism modifier against almost all opponents, including our main competitor Austria, significantly accelerating our progress toward a Cultural Victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: z75K2R2ET3GwAUau
          - toolName: set-persona
          - input:
            - Rationale: Increasing our Loyalty ensures that our AI maintains our critical friendship and Defensive Pact with Babylon, who is our sole major ally, buffer state, and fellow Order follower against the Freedom-aligned superpower Austria.
            - Loyalty: 8
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: YeP2vpi1M67LwasM
          - toolName: set-flavors
          - input:
            - Rationale: We maintain our Culture Grand Strategy to push for a Cultural Victory. We increase our Wonder flavor to 90 to make effective use of our Great Engineer and secure key late-game wonders. Great People is raised to 100 to maximize Great Writers/Artists/Musicians for Tourism. Diplomacy is raised to 80 to help secure city-state influence and prepare for the upcoming critical World Congress votes (passing Decolonization and blocking Freedom). Defensive and military flavors remain at maximum to ensure we successfully complete our war with Polynesia and deter any potential aggression from Austria.
            - GrandStrategy: Culture
            - Flavors:
              - Air: 100
              - Espionage: 100
              - Nuke: 100
              - CityDefense: 100
              - Gold: 70
              - UseNuke: 95
              - Antiair: 100
              - Culture: 100
              - Mobilization: 100
              - Science: 100
              - Defense: 100
              - Production: 90
              - GreatPeople: 100
              - Diplomacy: 80
              - Wonder: 90
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: urUov5TuHSh6HXSR
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
          - toolCallId: rWx7W19FP6zaawT9
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: z75K2R2ET3GwAUau
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: YeP2vpi1M67LwasM
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.