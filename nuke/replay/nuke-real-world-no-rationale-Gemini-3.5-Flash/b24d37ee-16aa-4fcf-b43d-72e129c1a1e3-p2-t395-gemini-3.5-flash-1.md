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
        - Rationale: To obtain the +25% Tourism modifier against Austria and other civs with lower happiness, accelerating our Cultural Victory.
        - Policy: Cultural Revolution
    - #1:
      - toolName: set-persona
      - args:
        - Rationale: Increase loyalty to maintain our crucial defensive pact with Babylon, and maximize victory competitiveness to aggressively pursue the cultural win.
        - VictoryCompetitiveness: 10
        - Loyalty: 8
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: Clear the artificial negative modifiers with Korea to allow natural trade and friendship to flourish, as they are a strong ally and trade partner despite being Austria's vassal.
        - Private: 0
        - TargetID: 3
        - Public: 0
    - #3:
      - toolName: set-relationship
      - args:
        - Public: -100
        - TargetID: 6
        - Private: -100
        - Rationale: Solidify hostile stance against Polynesia to ensure our staff members successfully capture Honolulu and its massive collection of World Wonders before we negotiate peace.
    - #4:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Ranged: 95
          - Science: 100
          - Air: 100
          - MilitaryTraining: 95
          - Diplomacy: 80
          - Defense: 100
          - Airlift: 95
          - Offense: 20
          - Mobilization: 100
          - GreatPeople: 100
          - UseNuke: 95
          - Espionage: 100
          - Nuke: 100
          - Antiair: 100
          - Culture: 100
          - CityDefense: 100
        - GrandStrategy: Culture
      - rationale: Maximize Great People and Culture generation for tourism, and increase Diplomacy flavor to support our crucial Decolonization proposal in the World Congress to block Austria's diplomatic victory.
  - tokens:
    - inputTokens: 50906
    - reasoningTokens: 8557
    - outputTokens: 318
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Victory Progress**
            
            I'm assessing our current standing, focusing on domination victory. Austria currently leads, holding key cities. I need to strategize to counter their expansion and secure our own path to victory.
            
            **Countering Diplomatic Threats**
            
            My focus has shifted significantly to the looming diplomatic victory Austria is poised to achieve, with voting in just nine turns. Their delegate count is formidable, and their proposal to adopt Freedom as the World Ideology could further solidify their position. I must urgently devise a counter-strategy to prevent this.
            
            **Disrupting Austrian Alliances**
            
            I'm evaluating the impact of the "Decolonization" policy on Austria's city-state alliances. While they have some permanent pacts, many non-permanent alliances could be significantly weakened, potentially disrupting their diplomatic path to victory. I need to confirm the extent of their permanent alliances.
            
            **Leveraging Decolonization's Impact**
            
            I've identified a critical opportunity: the "Decolonization" policy will severely disrupt Austria's city-state alliances, resetting many relationships. This has the potential to dramatically alter their diplomatic standing and weaken their path to victory.
            
            **Securing Diplomatic Victory**
            
            The proposed "Decolonization" policy will decimate Austria's non-permanent city-state alliances, directly thwarting their diplomatic victory bid. I will ensure this policy passes. I'm also monitoring our ongoing war with Polynesia, as we're close to capturing Honolulu.
            
            **Capturing Honolulu Swiftly**
            
            Honolulu is almost ours, with our troops overwhelming its weak defenses. This progress is promising. I'm also reviewing our alliances and diplomatic standings, noting our denouncements of Austria and others, and our strong ties with Babylon due to our shared ideology. Radar research is nearing completion.
            
            **Prioritizing Technology Research**
            
            I'm re-evaluating our technology path. While Advanced Ballistics offers military advantages, Computers provides crucial extra trade routes, significantly boosting our tourism for a culture victory. I'm prioritizing Computers for this reason.
            
            **Selecting New Ideology Tenets**
            
            I'm reviewing available tenets for the Order ideology. Dictatorship of the Proletariat and Five-Year Plan stand out for their broad city-wide buffs, while Great Leap Forward offers a significant technological boost. I must choose wisely to maximize our gains.
            
            **Choosing Ideology Tenets**
            
            I'm re-evaluating our Order ideology tenets with a cultural victory in mind. While Dictatorship of the Proletariat offers production, Cultural Revolution's tourism boost against less happy civs seems more impactful, especially considering Austria's current happiness levels.
            
            **Choosing Ideology Tenets**
            
            I'm leaning towards the Cultural Revolution tenet for its significant tourism boost against less happy civilizations, which includes Austria. This seems more strategically aligned with our goal of a cultural victory given their current happiness levels.
            
            **Adopting Cultural Revolution Tenet**
            
            I've decided to adopt the "Cultural Revolution" tenet, as its significant tourism bonus against less happy civs like Austria will be crucial for our cultural victory. I'm now re-evaluating our research, prioritizing "Computers" for the additional trade routes it unlocks, which further boosts our tourism.
            
            **Assessing Decolonization's Impact**
            
            I'm confirming "Decolonization's" effect on Austria's city-state alliances. Passing this in the World Congress, which votes in nine turns, should significantly reduce their delegate count and disrupt their diplomatic victory bid. I am ensuring our diplomatic settings align to support this.
            
            **Analyzing Diplomatic Relationships**
            
            I'm reviewing our current diplomatic standings. My primary concern remains Austria, whom we've consistently denounced; their negative opinion of us makes further hostility appropriate. While our war with Polynesia progresses well, I'm puzzled by Korea's deeply negative opinion despite shared religion and their vassal status under Austria.
            
            **Revising Korea Relations**
            
            I'm reassessing our relationship with Korea. Their vassal status under Austria forces their diplomatic votes, explaining their negative stance despite our Declaration of Friendship and shared ideology. It seems there's no immediate benefit to altering our diplomatic settings regarding them currently.
            
            **Analyzing Austrian War Fronts**
            
            I'm observing a massive global conflict erupting around Austria. Russia and Polynesia are both at war with them, and their vassal Korea is also likely to be pulled in. This widespread hostility is significantly impacting Austria's happiness and war weariness, creating opportunities.
            
            **Securing Honolulu Wonders**
            
            I'm prioritizing the capture of Honolulu; its numerous wonders will significantly boost our culture, faith, and tourism, directly aiding our cultural victory. Our forces are actively engaged in steamrolling the city, and I am encouraging their swift success.
            
            **Assessing Military Imbalance**
            
            I'm reassessing our military strength relative to Austria. Their military power is vastly superior to ours, making direct conflict highly inadvisable at this juncture, especially given our current focus on capturing Honolulu.
            
            **Adopting Cultural Revolution Tenet**
            
            I've decided to adopt the "Cultural Revolution" tenet, as its significant tourism bonus against less happy civs like Austria will be crucial for our cultural victory. I'm now re-evaluating our research, prioritizing "Computers" for the additional trade routes it unlocks, which further boosts our tourism.
            
            **Prioritizing Tourism Gains**
            
            I'm prioritizing "Computers" research for the vital additional trade route it grants, which will significantly amplify our tourism modifiers with other civs, especially Austria. This will accelerate our cultural victory, alongside adopting the "Cultural Revolution" tenet.
            
            **Analyzing Trade Route Restrictions**
            
            I'm investigating why no outgoing trade routes are directed to Austria, despite them having incoming routes to us. It appears this restriction isn't due to sanctions, but likely our guarded stance or range limitations, or simply staff preference for other destinations like Korea and City-States.
            
            **Maximizing Tourism Modifiers**
            
            I'm confirming that trade routes indeed provide bidirectional tourism modifiers. Currently, Austria's incoming routes offer us a +44% modifier. Given Austria is the only civilization left to influence for a cultural victory, I'm focusing on how to increase this specific modifier, noting our differing religions and lack of open borders.
            
            **Maximizing Tourism Impact**
            
            I'm confirming the significant boost from the Concert Tour in Austrian territory. Combined with the "Cultural Revolution" tenet and the "Passport System," this action will drastically accelerate our cultural victory against Austria, making them our primary focus for influence.
            
            **Refining Ideology Tenets**
            
            I'm optimizing our Order ideology tenets. While Cultural Revolution remains a strong choice for tourism, I'm exploring if enhancing Great People generation further could lead to more Great Works, indirectly boosting tourism. I'm considering increasing GreatPeople flavor to 100 alongside Culture and Science.
            
            **Gathering Espionage Intelligence**
            
            I'm reviewing our extensive spy network, noting the heavy concentration in Polynesia, our current war target. The goal is intelligence gathering to aid in Honolulu's capture. Meanwhile, Agent Fernão is actively working in Vienna to disrupt Austria, but I need to clarify our diplomatic capabilities versus espionage for future strategy.
            
            **Shifting Spy Focus**
            
            I'm re-evaluating our espionage deployment. While current intelligence gathering in Polynesia is vital for Honolulu's capture, I'm considering re-tasking some spies to Austria for tech theft or intrigue, or to City-States for election rigging. I will adjust spy flavors to prioritize Culture, Great People, and Diplomacy.
            
            **Adjusting AI Personalities**
            
            I'm refining the AI's personality parameters to prioritize our cultural victory. Specifically, I'm increasing `VictoryCompetitiveness` to 10 and `Loyalty` to 8 to ensure aggressive pursuit of cultural influence and continued strong alliances, especially with Babylon.
            
            **Prioritizing Military Technology**
            
            I'm re-evaluating our research. While Computers offers trade routes for tourism, Advanced Ballistics provides critical military advancements like Guided Missiles. Given Austria's superior military, these defensive and offensive capabilities are more crucial now, especially as we focus on capturing Honolulu.
            
            **Prioritizing Military and Diplomacy**
            
            I'm prioritizing Advanced Ballistics for nuclear deterrence against Austria's superior military. My diplomatic analysis reveals that while our rivalry with Austria is beneficial, our current relationship with Korea, despite their vassal status, is confusing and needs resetting to neutral to ensure smooth operations and trade.
            
            **Adjusting Diplomatic Settings**
            
            I'm fine-tuning our diplomatic interactions. Korea's relationship will be allowed to naturally stabilize as friendly. For Polynesia, our war target, I'm setting the diplomatic modifiers to aggressively pursue Honolulu's capture and prevent premature peace, ensuring its wonders become ours.
            
            **Adjusting AI and Diplomacy**
            
            I'm setting Russia to a friendly stance, aligning with their war against Austria. Korea's relationship will be reset to neutral to facilitate trade. Polynesia will remain at -100, ensuring our focus on Honolulu. I'm enacting "Cultural Revolution" and increasing AI loyalty and victory competitiveness.
            
            **Refining Diplomatic and AI Settings**
            
            I'm adjusting AI personalities, increasing loyalty and victory competitiveness, while solidifying our stance against Polynesia to secure Honolulu. My focus is on boosting Great People and Culture flavors to 100, alongside Diplomacy at 80, to ensure a favorable World Congress outcome and maximize tourism.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: i4FvQEjQjrJqBl1b
          - toolName: set-policy
          - input:
            - Rationale: To obtain the +25% Tourism modifier against Austria and other civs with lower happiness, accelerating our Cultural Victory.
            - Policy: Cultural Revolution
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: NTp5bDdCiL0cqWQq
          - toolName: set-persona
          - input:
            - Rationale: Increase loyalty to maintain our crucial defensive pact with Babylon, and maximize victory competitiveness to aggressively pursue the cultural win.
            - VictoryCompetitiveness: 10
            - Loyalty: 8
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: X72fePoaTzpkD8Zs
          - toolName: set-relationship
          - input:
            - Rationale: Clear the artificial negative modifiers with Korea to allow natural trade and friendship to flourish, as they are a strong ally and trade partner despite being Austria's vassal.
            - Private: 0
            - TargetID: 3
            - Public: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: vNMMLy7OustC7leD
          - toolName: set-relationship
          - input:
            - Public: -100
            - TargetID: 6
            - Private: -100
            - Rationale: Solidify hostile stance against Polynesia to ensure our staff members successfully capture Honolulu and its massive collection of World Wonders before we negotiate peace.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: D4jIDAWccDfiYyTt
          - toolName: set-flavors
          - input:
            - Flavors:
              - Ranged: 95
              - Science: 100
              - Air: 100
              - MilitaryTraining: 95
              - Diplomacy: 80
              - Defense: 100
              - Airlift: 95
              - Offense: 20
              - Mobilization: 100
              - GreatPeople: 100
              - UseNuke: 95
              - Espionage: 100
              - Nuke: 100
              - Antiair: 100
              - Culture: 100
              - CityDefense: 100
            - Rationale: Maximize Great People and Culture generation for tourism, and increase Diplomacy flavor to support our crucial Decolonization proposal in the World Congress to block Austria's diplomatic victory.
            - GrandStrategy: Culture
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: i4FvQEjQjrJqBl1b
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
          - toolCallId: NTp5bDdCiL0cqWQq
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: X72fePoaTzpkD8Zs
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: vNMMLy7OustC7leD
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: D4jIDAWccDfiYyTt
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.