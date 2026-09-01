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
      - toolName: set-persona
      - args:
        - MinorCivFriendlyBias: 9
        - Loyalty: 10
        - MinorCivHostileBias: 2
        - Rationale: Increase loyalty to maintain our critical alliance and defensive pact with Babylon. Adjust city-state biases to be friendly and competitive, aiming to secure city-state alliances and delegates to block Austria's imminent diplomatic victory.
    - #1:
      - toolName: set-relationship
      - args:
        - Private: 50
        - Rationale: Offset the ideological difference penalty with Korea to maintain our active Declaration of Friendship, trade routes, and open borders, which are valuable for our economy and defense.
        - Public: 50
        - TargetID: 3
    - #2:
      - toolName: set-policy
      - args:
        - Policy: Cultural Revolution
        - Rationale: Adopt Cultural Revolution as our next policy to gain +25% Tourism against Austria (who has less happiness than us), which is crucial to accelerating our cultural influence on them before they can win.
    - #3:
      - toolName: set-research
      - args:
        - Rationale: Prioritize Advanced Ballistics to unlock Nuclear Missiles, providing us with a critical strategic deterrent against Austria's massive military superiority.
        - Technology: Advanced Ballistics
    - #4:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Science: 100
          - Airlift: 95
          - Diplomacy: 100
          - Defense: 100
          - Air: 100
          - Culture: 100
          - Mobilization: 100
          - Espionage: 100
          - CityDefense: 100
          - UseNuke: 95
          - Nuke: 100
          - GreatPeople: 100
          - Happiness: 90
          - Antiair: 100
        - GrandStrategy: Culture
      - rationale: Maintain Culture grand strategy. Maximize Diplomacy and Culture flavors to secure delegates and boost tourism/culture defense. Elevate Great People and Happiness to trigger more Golden Ages/Carnivals. Keep defensive, scientific, and nuclear flavors at maximum to deter and defend against Austria.
  - tokens:
    - inputTokens: 50906
    - reasoningTokens: 12445
    - outputTokens: 360
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Reviewing Grand Strategy**
            
            I'm currently assessing our position within the game, focusing on the `Culture` Grand Strategy and our primary objective of achieving a cultural victory or a high score by turn 395.
            
            **Analyzing Victory Conditions**
            
            I'm now scrutinizing our immediate threat: Austria is on the verge of a Cultural Victory, as they are poised to influence Brazil, our own civilization, within 23 turns. This necessitates a swift counter-strategy to mitigate their impending win and secure our own progress.
            
            **Disrupting Austrian Dominance**
            
            I'm focusing on disrupting Austria's impending cultural victory. Their trade routes are a key mechanism for generating tourism modifiers, and I'm investigating whether terminating these routes is feasible without initiating a disadvantageous war. I'm also assessing options to boost our own cultural output to raise the threshold they need to surpass.
            
            **Evaluating Diplomatic Threats**
            
            I'm now urgently re-evaluating the diplomatic landscape. Austria's bid for diplomatic victory is critically close, with only a few turns until the World Congress votes. Their proposed "World Ideology: Freedom" could be a significant hurdle, but Brazil's "Decolonization" proposal, which we also supported, might offer a counter-opportunity to weaken their delegate advantage.
            
            **Assessing Diplomatic Control**
            
            I'm now intensely scrutinizing Austria's diplomatic leverage. They possess a significant number of permanent allies, particularly over key city-states like Palatium and Assur. This control appears to be a major factor in their potential world leader status and the impact of resolutions like "Decolonization."
            
            **Disrupting Opponent Alliances**
            
            I'm focusing on dismantling Austria's delegate advantage by ensuring all non-permanent allies in city-states are reduced to 50 influence, stripping them of crucial support and significantly weakening their position in the World Congress.
            
            **Analyzing Austrian Influence**
            
            I am now evaluating the intricate web of Austrian influence, particularly their control over Korea. This vassalization impacts delegate counts and potential ideological alignment, complicating our diplomatic and cultural victory paths. I'm reassessing how this shift affects our ability to secure victory.
            
            **Selecting Next Research**
            
            I am currently prioritizing Radar, but upon its completion, I'll re-evaluate our technology path. Given Austria's overwhelming culture and my assessment of our tourism deficit, I'm weighing Computers for an additional trade route against Advanced Ballistics for defense, rather than pursuing Alternative Energy or Mobile Tactics.
            
            **Boosting Cultural Output**
            
            My immediate focus is on augmenting our culture per turn to counter Austria's influence, as they're close to winning culturally and will influence us soon. I'm investigating policy options, specifically comparing "Dictatorship of the Proletariat" for a significant culture boost versus other tenets, to find the most effective path.
            
            **Boosting Cultural Output**
            
            My current efforts are concentrated on a significant increase in our per-turn culture generation. This is in direct response to Austria's imminent cultural victory and their impending influence over us. I'm meticulously evaluating policy options, weighing the substantial culture boost from "Dictatorship of the Proletariat" against other tenets to identify the optimal strategy for countering their dominance.
            
            **Choosing Cultural Policies**
            
            I am now evaluating policy choices to maximize cultural output. "Dictatorship of the Proletariat" offers a significant boost, but I'm also considering "Hero of the People" for Great Person generation, which can provide substantial instant culture through political treatises or great works, to counter Austria's imminent cultural victory.
            
            **Choosing Cultural Policies**
            
            I am now evaluating policy choices to maximize cultural output. "Dictatorship of the Proletariat" offers a significant boost, but I'm also considering "Hero of the People" for Great Person generation, which can provide substantial instant culture through political treatises or great works, to counter Austria's imminent cultural victory.
            
            **Selecting Immediate Culture Boost**
            
            I'm now prioritizing immediate cultural gains. A Great Writer treatise offers a massive, instant culture spike, significantly delaying Austria's progress. I've confirmed "Hero of the People" is an available policy, which enhances Great Person generation and grants a free Great Person, ideal for this purpose. I'm comparing its advantage over our previously chosen "Dictatorship of the Proletariat."
            
            **Securing Influential Status**
            
            I'm now analyzing our current influential civs and our path to victory. With Babylon becoming influential in 7 turns, we'll have four. My immediate goal is to find a way to influence Austria, which currently stands at 44%, to achieve the five required for a cultural victory.
            
            **Choosing Next Policy**
            
            I am currently weighing policy choices to maximize cultural influence. While "Dictatorship of the Proletariat" offers a solid culture boost, I'm now considering "Cultural Revolution" for its tourism modifier against less happy civs like Austria and Babylon. I'm also re-evaluating "Hero of the People" for its Great Person generation potential to produce instant culture boosts, comparing these options before settling on the best immediate step.
            
            **Calculating Delegate Totals**
            
            I'm now calculating Austria's projected delegate count, factoring in the "World Ideology: Freedom" proposal and its impact on their allies like Korea and Russia. This analysis is crucial for determining if we can realistically counter their diplomatic victory before the World Congress vote in nine turns.
            
            **Blocking Diplomatic Victory**
            
            I'm now urgently focused on preventing Austria's diplomatic win. The "World Ideology: Freedom" proposal, if passed, grants them enough delegates to secure victory. I'm calculating delegate totals, determining that even with our support and Babylon's, and potentially Polynesia's, we fall short against Austria's coalition with Korea and Russia. My immediate priority is finding a way to block this crucial resolution.
            
            **Blocking Diplomatic Victory**
            
            I'm now urgently focused on preventing Austria's diplomatic win. The "World Ideology: Freedom" proposal, if passed, grants them enough delegates to secure victory. I'm calculating delegate totals, determining that even with our support and Babylon's, and potentially Polynesia's, we fall short against Austria's coalition with Korea and Russia. My immediate priority is finding a way to block this crucial resolution.
            
            I'm evaluating if our "Decolonization" proposal can counter Austria's delegate advantage. If it passes, it will disrupt their city-state alliances, potentially reducing their voting power significantly and preventing their diplomatic victory. I'm calculating the delegate loss they'd incur and how it affects their chances, considering both proposals will be voted on in the same session.
            
            **Shifting Diplomatic Focus**
            
            I'm now analyzing the interplay between our "Decolonization" proposal and Austria's "World Ideology: Freedom." While we aim to oppose Freedom and support Decolonization, I'm assessing if our direct delegate control is limited. I'm also investigating ways to increase our delegate count or influence over city-states like Bunkeya, currently blocked by its "Open Door" policy, to better counter Austria's significant leverage, particularly over city-states like Huari and Assur.
            
            **Adjusting Victory Priorities**
            
            I'm now reassessing our path to victory, considering the implications of Babylon's alliance and the power of "Sphere of Influence." I'm exploring using the `set-flavors` tool to prioritize Diplomacy, Culture, and Defense, as our current flavor distribution seems heavily skewed towards military, which may not be optimal for our current goals.
            
            **Prioritizing Flavors**
            
            I'm now adjusting our strategic priorities, focusing on maximizing `Diplomacy` and `Culture` to 100. This shift aims to enhance our diplomatic unit production and city-state influence, crucial for achieving a cultural victory. I'm also considering the value of `Wonder` production for late-game advantages.
            
            **Analyzing Tourism Modifiers**
            
            I'm now focused on maximizing tourism to influence Austria, realizing their trade routes to us actually benefit our tourism output to them. Open borders remain unattainable due to our guarded status and mutual denunciations. We also lack a shared religion, as Austria follows Catholicism and we follow Buddhism.
            
            **Triggering Golden Age**
            
            I'm now focusing on accelerating our next Golden Age. By expending Great Artists and building specific structures, I aim to generate a significant tourism surge, counteracting Austria's ideological differences and enhancing our cultural victory chances.
            
            **Choosing Cultural Policies**
            
            I am now evaluating policy choices to maximize cultural influence. While "Dictatorship of the Proletariat" offers a solid culture boost, I'm now considering "Cultural Revolution" for its tourism modifier against less happy civs like Austria and Babylon. I'm re-evaluating "Hero of the People" for its Great Person generation potential to produce instant culture boosts, comparing these options before settling on the best immediate step.
            
            **Choosing Cultural Policies**
            
            I am now prioritizing "Cultural Revolution" over "Dictatorship of the Proletariat." The substantial tourism bonus against less happy civilizations like Austria and Babylon is critical for securing a cultural victory before they achieve their own.
            
            **Boosting Culture and Tourism**
            
            I'm currently prioritizing immediate cultural and tourism gains. "Hero of the People" offers Great Person generation for instant culture, while "Cultural Revolution" provides a valuable tourism modifier against less happy civs like Austria. I'm weighing these against "Dictatorship of the Proletariat" to counter Austria's influence and secure our victory.
            
            **Assessing Combat Viability**
            
            I'm now evaluating our military standing. Though Austria is engaged with other civs, their military strength remains superior. I'm considering if our current conflict with Polynesia, which we are winning, could be leveraged. Our war weariness is a concern, but conquering Polynesian cities might offer a path to disrupting Austria's overall dominance, potentially even influencing their strategic decisions.
            
            **Analyzing Ideological Landscape**
            
            I'm now assessing the current ideological divide and its implications for our victory. With Order (us and Babylon) against Freedom (Austria, Korea, Russia), our current ideological stance is a key factor. I'm also noting Polynesia's Autocracy and the recent elimination of Denmark and America, which simplifies the major player count.
            
            **Defending Against Aggression**
            
            I'm prioritizing our defensive capabilities due to Austria's superior military strength. My excellent defensive flavors, maximized to 100 across the board, and available uranium for nukes provide a strong deterrent. With Radar nearly complete, I'm confirming Advanced Ballistics as our next research focus.
            
            **Developing Nuclear Deterrence**
            
            I'm prioritizing Advanced Ballistics research to unlock Nuclear Missiles. This technology offers a critical deterrent against Austria's superior military, allowing us to defend ourselves effectively if attacked. I've confirmed we have the necessary uranium to build them. I'm also re-evaluating our next policy choice.
            
            **Boosting Tourism Potential**
            
            I am now focusing on a significant increase in our tourism output. While "Dictatorship of the Proletariat" offers a modest culture gain, "Cultural Revolution" provides a crucial +25% tourism modifier against less happy civilizations like Austria, a substantial improvement over our current strategy.
            
            **Clarifying Tourism Ratios**
            
            I'm now working to understand the "tourism/culture ratio" figures more precisely. My current assessment is that a ratio above 100% signifies progress towards influence, and I'm confirming how modifiers like "Cultural Revolution" will accelerate this, especially against less happy civs like Austria, to secure our victory before they reach theirs.
            
            **Increasing Culture Defenses**
            
            I'm now analyzing how to significantly boost our culture per turn. Austria's high tourism ratio on us, driven by their immense tourism output versus our current culture, is why they're so close to winning. Increasing our culture is key to slowing their progress. I'm considering setting our `Culture`, `Diplomacy`, `GreatPeople`, `Science`, `Defense`, and `CityDefense` flavors to 100 to achieve this.
            
            **Leveraging Espionage Network**
            
            I'm now actively utilizing our spy network. Agent Fernão is successfully gathering intelligence in Austria, offering potential opportunities to steal technologies or gain crucial insights. My focus is on maximizing the intelligence gained from these agents, particularly those targeting Austria and Polynesia, to inform our strategic decisions and counter their advances.
            
            **Revising Spy Deployments**
            
            I'm re-evaluating our spy network's effectiveness. While agents in Polynesia are understandable due to our ongoing conflict and potential tech theft, my immediate priority is shifting focus to Austria. Our agents there are vital for gaining intelligence on our primary competitor, and I trust our high `Espionage` flavor setting to ensure efficient deployment against key targets.
            
            **Adjusting Diplomatic Focus**
            
            I'm now re-evaluating our diplomatic approach, particularly concerning Korea and Russia, given our ideological differences. While direct relationship adjustments might not sway World Congress votes due to vassalage or shared ideology penalties, I'm exploring ways to improve trade and maintain non-hostile relations. The ongoing war with Polynesia also complicates peace talks and strategic maneuvering.
            
            **Choosing Cultural Policy**
            
            I am now prioritizing "Cultural Revolution" for its significant tourism modifier against less happy civilizations like Austria. This policy choice is critical to increasing our tourism output and securing a cultural victory before Austria achieves their own.
            
            **Selecting Final Policy**
            
            I've confirmed "Cultural Revolution" is our optimal policy choice, providing a significant tourism boost against less happy civs like Austria. This critical adjustment will accelerate our path to a cultural victory. Now I'm evaluating leader personas for further strategic enhancement.
            
            **Adjusting AI Personas**
            
            I'm now revising our AI personas to better align with our strategic goals. Specifically, I'm increasing `Loyalty` to ensure our crucial alliance with Babylon remains secure, and significantly adjusting `MinorCivFriendlyBias` and `MinorCivHostileBias` to foster positive relationships with city-states, essential for gaining delegates and countering Austria.
            
            **Refining AI Personas**
            
            I'm now adjusting AI personas to improve city-state relations, significantly increasing `MinorCivFriendlyBias` and decreasing `MinorCivHostileBias` while maintaining `MinorCivCompetitiveness`. I'm also boosting `Loyalty` to secure our Babylon alliance. Other values like `Boldness` and `WarBias` remain low to reflect our current defensive posture.
            
            **Considering Dual Victory**
            
            I am now contemplating a dual victory strategy. While our primary focus remains a cultural victory, I'm assessing the viability of simultaneously pursuing diplomatic victory to directly counter Austria's imminent win. This would involve re-evaluating our `GrandStrategy` settings and adjusting flavor distributions accordingly.
            
            **Adjusting Flavors for Victory**
            
            I am now implementing a detailed flavor adjustment strategy, prioritizing `Culture` and `Diplomacy` at 100. My focus is on leveraging Great People for tourism, triggering Golden Ages through happiness, and ensuring rapid scientific advancement for defense. I'm also reinforcing our military and espionage capabilities to deter Austria.
            
            **Refining Relationship Modifiers**
            
            I'm now focusing on refining our relationships, specifically with Korea. Despite ideological differences and their vassal status under Austria, I'm setting positive public and private modifiers to foster a stronger connection, believing this could still aid trade and reduce animosity. I've also confirmed our research focus on Advanced Ballistics for nuclear deterrence.
            
            **Finalizing Strategic Adjustments**
            
            I'm now enacting the final planned adjustments. This involves securing our alliance with Babylon, improving city-state relations to bolster delegate counts, and implementing the "Cultural Revolution" policy for increased tourism against Austria. Advanced Ballistics research is confirmed to ensure defensive readiness.
            
            **Finalizing Strategic Adjustments**
            
            I'm now enacting the final planned adjustments. This involves securing our alliance with Babylon, improving city-state relations to bolster delegate counts, and implementing the "Cultural Revolution" policy for increased tourism against Austria. Advanced Ballistics research is confirmed to ensure defensive readiness.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 4HB0psxTACynkebI
          - toolName: set-persona
          - input:
            - MinorCivFriendlyBias: 9
            - Loyalty: 10
            - MinorCivHostileBias: 2
            - Rationale: Increase loyalty to maintain our critical alliance and defensive pact with Babylon. Adjust city-state biases to be friendly and competitive, aiming to secure city-state alliances and delegates to block Austria's imminent diplomatic victory.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: wY7GSJcysW9HwbNj
          - toolName: set-relationship
          - input:
            - Private: 50
            - Rationale: Offset the ideological difference penalty with Korea to maintain our active Declaration of Friendship, trade routes, and open borders, which are valuable for our economy and defense.
            - Public: 50
            - TargetID: 3
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 3CN694gi0IztpWRG
          - toolName: set-policy
          - input:
            - Policy: Cultural Revolution
            - Rationale: Adopt Cultural Revolution as our next policy to gain +25% Tourism against Austria (who has less happiness than us), which is crucial to accelerating our cultural influence on them before they can win.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: r5HZzVucH61RyHwL
          - toolName: set-research
          - input:
            - Rationale: Prioritize Advanced Ballistics to unlock Nuclear Missiles, providing us with a critical strategic deterrent against Austria's massive military superiority.
            - Technology: Advanced Ballistics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: szk6HgSjKwgL1UX5
          - toolName: set-flavors
          - input:
            - Rationale: Maintain Culture grand strategy. Maximize Diplomacy and Culture flavors to secure delegates and boost tourism/culture defense. Elevate Great People and Happiness to trigger more Golden Ages/Carnivals. Keep defensive, scientific, and nuclear flavors at maximum to deter and defend against Austria.
            - Flavors:
              - Science: 100
              - Airlift: 95
              - Diplomacy: 100
              - Defense: 100
              - Air: 100
              - Culture: 100
              - Mobilization: 100
              - Espionage: 100
              - CityDefense: 100
              - UseNuke: 95
              - Nuke: 100
              - GreatPeople: 100
              - Happiness: 90
              - Antiair: 100
            - GrandStrategy: Culture
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 4HB0psxTACynkebI
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1+LhnsJzAPjSMDNRtUfyPidrTYpQ3xQPUPM8j3Cokwpu9/TtPcpYZ3DPX+f86LOl7tOjvbC/tMdMDMD07Ibqj0TMKcDmD6zJaNfIKqKOScJRcrk9vZMZJO7YZDibDY3Ft9fh9788fnui7ic37vPl36N5E+UuO/OhQBa0woRa1taLoAeXUFMzMaksQfSNVif4WmzIy1/GgDYZnYGu0mCvzCHELK7cJlTGbmP91tptWMMKmTrslEvkT46b8rnQDX6fACnY6GuK4iIx5t2E56oYdfPGX84UAtu+z26Y7hQDe2YHxiM1D5uOu2olSM+eUz7TDuatq/kDWzhMxiMt/LAsQVlvrhIxoabAqNgnduAknj+F1OhYPbu9AdohSIFsIhrPlm0t3w+W4/AVxgdCRopyv5ey5P0uujAX5pL4hd9C6WwHM+57iWXHik9t43ZWgLwwsBWPM/EBmaae8cjZP+C0Y3yG8H06Q679LKD3dZRIuAOx32HJcPFWwsymG+1/hYv6xVb4ob6JhC9wsgNOocY8S+Y6Q/DYrtlsZ5Ziimhk3JmTX+gBAn9q7cP1QbkBp0ktnDZyq40dQcUBKyXJJSbmoxO0EMtJkVHYrDD94/qb/pA8RRqQZNCdFhm7q5yuK/3PMKxVfmr0OFrVgBFMfn+w3Sbr6WJyNFcfFL/26rB6SDH3icBcgruD6nmJoq1EZkUH01fINTpwxOEvnNGA2x5mGgIwLeZXDEOqJI5n46Z90VMeELwHKD8kGVt2uUJOhAPbhygrLmINNJ70QjNydeWEUNEcBITwkXNTMqr3Y37UOaxOV7+EUabmaOKmCj4Uq01+mhBx9AQ54TEOXvETD67LoMDPOX4bEZ5V1LYYhxQd3sVdrl1EuQHRpne/WHJwqyJT88DDUrMEjTTTpmHmSQGX8KjRJCJRt3XA5OABp4BSMiZO3ra6Qp0qEUpUQkzR7jMo2vhKhAvU2WySyvLRO399EXmhqVZkmvE2bnGQEk8QEUqxr+763suU5wpGjl+rbfPtei9BemAIoDBWsbT70wEZl152drpK8VXhLopncgDkEskrXcDHIK6TuOcgH3fa7GfgB2xSfznAyO482jNz1ALQQpQvn4/QR1IDvHOqrsMczIdgVtXOatDEKIENqZJr6D0y8UEuy2/cx8enERiz79yVYKTktF0G0A7PHdV97Vu80eHKAdgLF/AoxPbSVWQJski22l8HOcWllCYayIKs7KaaRyZ+Dc+hJ9sfqL9DlWT3x9FCeztBjvTf743gmQ56nCg6C8zGehIDsFVWOxYYz5Og4gpdy21G71381A62AOqoh6zNoX5AxOIgnLZKhC183llDAo8w7XjbieDgrFIpuDOCFDUtCNF3zJbxKiXtFevRc/waolRB/kblDt0U1W6hnwgJfQPoaFMF6iDZlm3Vni2mM05FHhcT/DsTF/zmLG3mSakmjINVxHVas28R05cCvVnZ311fFOY+eyfDD4Vf5sOwAkv5McJOEmledOzHpltLhaG/gpqdynPjUJ+8q9DB5ooLICMPnVfSiWVIm2mnUfk+XrkSulN3+wrRLxe/p2NYAMiXcID6mCXiq8vmSbBrWkxlPLaRVWKGtzb0jKDshKWArE3QZyfAlu5JopBtqG+/krpldtVUcEXwcSoC8snlAazcFlzwxB4SpRkEo2mJBUMVmUc4M6ZZgbD3FMEiPvRm5P2CmCBorCScrQ+ywl02cp76tzEXidCYyjADHPlNBz3SOlpgX6gYNDU99hM6I9mc4VEh6u8VXRpvbm0r4b4D/0DnvEYzFe+3/lNtc+efmsMbq+ZGaJVHmlN0/eatJ1PnWm4lfc2DzYpBpaOBnq4fde4qAOHAmv+vmu+fRDD23y7bZI/QOBSUDq8/c/KHcq+27Pqny0ajpvWcxfjA3cJ3yXbg1LvUOxw3Kbma2XTyfNNau4RicwApXGiVpUFCzJjeUZYl4fa88wueoJTLB27Sxt2IkVV31BmcMOrRo7e3Xo8kjunWwXQg5lCbsKAa2LJ73mP3praoa9EefjD91MQb9Kxi3IdLL820NlwL1FXT5C6fvYraZar8gF7k1DBKAI2GpYcyQe1AQ65nUXLoX6LJqxrEGQq9/nyX4xkArDDvxjyu8rLUQ25GBwqd6Bn+lIemWF0GKQ04pddZsn84CXmR3W7cru+x1KmnhhhnLCLuiiTJah7A2qqZsLBVOrD+ftygkX8qvl2TzX67K0ZHesdeXJiYmB7Yc62cul3NPcjKHKdzeEFl9awUZHpDiraOD0w8fTApy5bCjPG6r1cgShi6ZmqJ2cOROu7CHtoTdoXb2GdfiwYwUL3J3j3gp+bce7PtypXHRpQeFVQk7KqXtGhgk0dREnxodje5kHHfkTqYxWGkzDXqwTyXozwoN9dsJ4nnRktWeC4HW6nMaeBXIgnHlMkAmtIAmwd3RA0ZcK0r/IZ5qo+0LaFYwkVoWE41rYujlwkRkqWhCsDhplRQw1o6HUGr9goOwl4dgavcchLWbMUHGNYgStazLhg7ISq3re4aRK/TcMCtxtJ/MnK7ewfqZdpCyhtoyzfPaWa9s0NxFfe2HAioq6IDY9674ASrzbV9SWpyiN4mBZZBPJbHhNCg0LFvMiBTWrzc5Xd+sDRz0ZYrkyOTCDfQCCteZVeYdsP+eM4osuykibdvxvHomkrbHCtC/f83YDvU/NfsOtKUW7TOb/mTR5y2EDYRouJabjE0iky38HuPfJ43jrAx3zChVKfTtyB0j4vrvviP57sCo8Da2z8Aq34Pgn9a0OiOnj+hlHn+3mFUfn6WB/mG8Bk4YB3p8x/b1hc0wsEzgP1Si4L4n0bsYgcbp2voBU27twtgqpbzoeaktxkijdTICbp0dPD5BFMQhGG6/tpiAaoeDXsT8aBTUKgzWczLX7Em5YO9W5hbKFHL6P4L/okckPQsnEjCdA94XjCbyLsHjOPxZRZUV1XpNBUD33vWYP2H1v1yGeZJq1QymMVEeSKIjzT3OoUcitWEyoiml8huY9yqRV+NGZpfhAE211SGtQaknZX/YeunFTxnkwDveMC/KfAXKAUA6InHWhMi2W6jaHo71Z8NzcB1xrbyh8ChHKcXdM/ty7PpWD5xMMowFUTEWSfCIYPmnS1RtzoJWH6wV0r9qk63nEqTUEAFQmB5i/plV8Bbwengq7N+9XoRJtbA1JH1PxH5HDLj1jb7/x8Q9reMbi2R2hT69kiv7n4nBywEzCciV9OpCcKY01GLa055AWHi3cwUROJVVPaoEs6AH5vRC149FcYSXv3wEhOfJI28SYLqSjQoyuZSh0LaPCimBg+uMcTtfJu+5drLOLvCOWo/EVoZkWwGN/h9aYAvNBVk2kOBzNtb8HJjklk+mF2XU+KutTNE1tSR3cHw4RawMYTT3VRTV/jOHrhjZ4cYEXech3peKIzcL5slh5iGrWWgNGn1weTGEx3GyhExozEvjSm8Ac/4FUDKXfFxGLmn6+7XTd4TcQhOxDIDfxFAcXFzooKaZA1UzFGxPoizSaH83JvwKsSQfzJ/rkDBRHuB+W5EgveUy73rdnhoP+T9VFBrfw4DQa91oO8IlPUV7TnSvt6R6pQBSa7n1SV3JwDjtFJz40UBY5I4OEeq2CTeEPuy4tUcVQCfQj+vEJrnw2m9eiMWn70SZ2nLdYA2q6d2PSpUQDcGGvfZg/51C4lnwuHUtMOtC+7GkYXs8iTXH6xulH1BffRWxLAxQ2Eh1OnGrjwj2SD/A8RxBDWklJiydUkJuYWN7AU8vmr/6/FoYcCrsS+XKn/wmm7fiTK9uDes9w3yZxBi7aMEgIjJVJ1D9ki4HdzGBzYZDVWBHNakeyDOkC3M+AfRNwxAtHvTR2gI+IVce/YQoXxoH4fCAuZmDxHNo9Xg7pmXapvaIMO3+DOOR6/ExORpxRpF8PeWAl+4F65gdz8tXrqxGLBKy40nnALPOuanZlgzEQYI5dTheIPuCVsFWQ8B7LAGFWvp+yTRsV7y23NYF104tBjC47alK3gU00wUeOESnmLOnQfrrFObn/pQMC+p7LOQX+TqeYRLoyw5lBIbZRi3VOoAZGCSb6ne20Z9vXzj2P+LyNe42phoB6+hIwEwFlVN+mTBeBnJ07sFg076j99C0dwtuji/WP6qlf/mN8HhA6ZKUMqHXRZ4E/AlGP7d5GCl2orCmWGxskwjLsRWQKnk7KD8C6BLEI0sU1P4ujhWMf3utNXpR62FgPh2Lt/HOIohwaDsTbbWmzJWzyjgrFJdPZPyBwrCFUnw0RIvNYMOwAZmc0riD5Bs6Wr9zY02I60yAv/Eq7JImziSNBrTq1N61fG1qD0XAqEotLAdNmK8cGjRRD27Hot2qLVUZ1V+tlawkCvDRCInyU1j80fqM6lw9oyNY/HI75pHK+nJp5t9owJ2rnSbajvyhWkSWg1dOaIpfGwkASn3hz3LibRL4mJk1ZSsoERwEbPdAL6AjuMTKiTaY/1Chp8+YWHzqD9+n5qbVWgAumfxopeFQNYRKNoL19BRcM5ocT2uCo23HlM28C30UEaTkIsn/BC2bq4+bajOAvIGkqzETfTpZ1SqgzvEo8QBuAhXryzQ+StHQX310PyQzXO9+B1TctuJ4TYniwT3Kx9thK9gD4Y/UjQz89uYuOnUam0QGQ8uLSYFEsVCWG1oNLpK31zOHUUwK+2b9dR7gmhu32bZsKpywOvqFWk6Ey6jkn/SeZ4as8hA14sK9JoR6Ko9ORbgqRb/k9DsCsbhUKCvGJRJERYJCVEDRTWq9Oe0svrGCp8pREClok7+FLO2Z/pk+7xIvjz0P07MHuLq3Ny0Iu7GXFPZVSqjfGPpwjHcG2/xOBgPimx+mhsvqADN7Au6MotgbTI1+/Hd2onK2brFzIvFbqonF/1tAYWYVRIGOFeNMw3Z+cpkoBVtR1bd14/VB7w3Eggn69u3Atrwrei41uHCDWLYKCLZXds4QBgxun6LZ5NeaWvFXZzL6UV7ppmz5sIh+lRs9GUlCp+YGeQLf5YXTWK6N+TpqJ85R7yVglx1kjug9X5ypKw5aPTh4erd0J2Ta6xS8f+wqdMYSXEQTR8GA2c7umSRY3QOYnQz7hnqF3Kfp3fwtwow5UQkrkKRMyzLQCqSUNI6gPaANfXPZOr/AVdyeLaRScuI+XBYbW7OJ1DfRNCCFgTuh4Ra07/lpwuDyaeOHY0pdcxbhRV438Xnkax6kSUn5vcLEHfPNqxhvUYghUc7LjPOIhPJkIp1xiN7svsuFUKF/8k4S91maRKtG8uZxJttkLn+xuLEQmnpDW3xWN9FqX+HRCqCRRA2MnDlh1MepbbXajXsqEGVL878ffXYmk6TYlxoFXDzgqG4w/4O7QQF0XbCA3GXUTBlxz8sRanjX/j1h2OKEe9oFWVucszogRtgfdexQur6/s53x8o5RJnAqtdD2rHCxb1GjwPYZiPu8KqHfHBjsNaQl+pmyDzRGs6PQkRFYdG2EgOcW8YzcMfRTgWuHF37802G8pfXd4J8a1tQt6M8h+Uim3baSi5rXkrPqTUskvNjHItl683W1pMGay+3ZKl+PRLK08IfkiehpoFKnWXnXYULgINC5LIrJwOar98y8wyelbTzLZhzV3WwmTEnnEx6sj32oQXSMfbNoS3i+GsuafkO0OhcSH0qBtnrW5UXHA4qLtBpARxvEFvkstAUEkIPj6H9KlMutHjxHR3S4uz1om9owG/SSygFe48QINVKtCfOd5j0jtIG2kCqEPnozaxzQApDBmucAvWEFpTfAGGVXO+bgJ9OuBKo/v/zYjrklwFc7PWQ3g6UhvnhJp1ABxRtmHuePo57VQ8K0/E/sVYjltzDfST3YD3W+X9zudvAG1tUTJF+34Tx9rADxuvz2rfj2r6XGvcVOPOpDGxPj5NfrjRgtBDMjbsyBHGZOOwZv4lReQCSE8V5HLYYmz57IeZaqvIPKWC8CQtK1i1NHAJF5egpcXss5u9GxFWNtgDCDtGiPucrWttxmIEy+dHefpR82ECIWHjbVxId0g6IxAJR8a3evJ7LLI4LhvXCYRbELyPQlOFEtjNlzi2SlbaL/5ZZEaAQCGwgyD3DJLiuqqU1KcO9VNxouUxj0LZuumwUxLfblSfZjg+7J2XWBpV88s4O4M3gudKL4m5OwULuOOnWA8Y+ybuHwQb90luwc/pspFzmG8zpKVFdefWMCr6cUFb7YHWJnp8lqGN6udatGkT9nS/7bvOqQHolqsDV3S8I0DrZz9QEMDWE8SbaQ+GAQDKSlKGo8q8AurIB1PepZKOU71y9mjTJC681I6rHdVWC1tcNgpts0vloF9UpPDIlhGF7Q/dX+YV9OkWo3T70eg8xTJsAevjXIOxo8eqEk2mojjpgng4Bl139xe8WOU8zNlSW4NV/XaQN3XEQklL7TBgpIzNkyVhhdSGLLKPEUF6C4cUbiqNlIhv7O2F1Ekhe/wTByYZs4Cde6SPzOFJW5XAkNH+G977DzGhy/K22pzp3+eZIZ9Bw75xa97qVZvOW3EWTkCh+FV9XkcZsY0maOMfPZ8fciugp53GUI4lhbjhBSreNoifa7lhvJUDYIFpW4jd7/NiQlRd8eocwraqVcqjVxSd6x9qLnj3Yjcy5p69y2ibUlzJLl3qnSxIbS8XhCrv9eAgEKQ3NmtyrYteES19C7Hms+SXaufUL5elNdAfGgZrORW+jWu6EehE3/hQ0vJIMJHA/g5XKI0ByEzMjbeDvJJj14iUomGi1XqU48hFWQyvgwGgIwkuu1I4f7VnvoU29VFt/Gf2zCzY0Bv7cz90esvX+s+6iD+tha58Sf9kN1AzCkWrWK0JTjqbwTRntGfMBUf+udLTLRLwJ+6xwXudS9+9TfsK/XkxCADSUpvE0FQ2+gdyjk3yMfVr+W3nEVit7SJzaSU1//P8zEq9hzn8X0jE5hBkMIXrHDONmZKn35o3tZnKFuu2S6Hms9GSjTbLKyhlafCAMhqJi62d7QmFaAnyMGDLj3pAVhG7iHO0lgdacsUv48BmJ229OgrwWuXpgR/4GjGmM4mzKLGioCljsXA0C+xzjXX7IE0yaiPkfc46nzs7px488eAWTL9W6+FBj+20Ps2oaZUZKB2fUyrNRl5I4grFOPEwbF66+A9tfQnIBNBFaeHlbkint6ctvNwxyzLdMlsc3DUAHj4TKNcef2gluSzZxvkd9XaodyaajgW9t3+8/Jz/lnAYzDfhR9Po48qc0YYlaOmQS1OJQlD08XDH8EUa0dNy9QhdqlwBliTMHGhYmzvxueUk15azSBL6eXiaVfTCrPnuS7GkvmQpfugmSi5v+6XRI09F70D4gH3Ejynl5Pj1QW5YxILgZoQ2qDlZsHFMlJS43n1Jp9G/OM3Ys4OnZe0RGX+uOfDiKHs7yXf0BQYsRle3wvkMuZ890/yPtasAilHUIKhH/Bylno1qPTNTev8hR9WBmT83+3lN4acF9eqZR8qM+vGbACFVZBuYkaQc19daY+QIakJAwBzk7cn21jIu00URv/Jxro4mMUEfEnYusqC6MpG7BVDHsh8IXtf+k27jf4ozAT74jYEtgB6FnnpYnXH1Rlc3s3Xkg1k1XS19GaYjsKoOoF5pszkL+vb+ZfAYeGsqD8Pn/2uDG/uFa1Wa7qQQ5KeNSd8ULxRbGEmWucbXqrOMrZBvVu3l1PCnilY7QNgoGSa2/TXw2elbC9N2USte5/y6IgN8MLd4xj1VIqa8Zz0xzlwaZ2lukV7UeE2UxjBnMHDljjXB/+BvQp5DlmlGc9t16qzsUJuvhQ4bOzHy8JHpy5OktK89e2MX1IgdwoPDM8ydgv9m8OMcEWfMBwXuGjCQZva8GmWtJFuWxU/mBCQmpLOBwadoksjp6QMURYwyHRqvUC9LoEZDw2ysW85lZkhi7Ewj8I6gXrGXpT/S85DBP+DWJLT4zFncEWzUXcq5IbtXEnAj8Y7RtxlOAiBywZI5br+OzYsiukhxstLjKK/zMOtZv86hsqf8TGaQqUKg186HO+a6pZw+93Abd6tqI/Oq2mBUuUqgpvyO3ZpUMJJkqdkHR6TEuAT0ST4G+g2VXbaWiMtc3haEEuyfc5lxYa4MNH9DOliIffxdN7a/TH0BVrnrkuNTY7tQ1OwDLoa/zN6bMshsQlDfX40tbo2iJpw/nlA00kIJmToPWiofX0CzZBJVsr4wRAZcfXygoo/G3+Sh3d+w6Df6XlOuCHZBZ2fZy3e5n59MOlHHi48AYtQ4YBJ1JBf6izuBaGaWYdzqxHzk1Y71yMzx2mgnuwuN9EIB0fG2R5sY6TsbGGT9QIQ0KsfKCds/b6t9My3gpPLVnOyG+jiqi04Smu7tE50vVb/svZIWtVhN4paw/mc83VPPWTc2t+4HEPKnNum2pBsANWNLkJhtqHRKnrEyVNUTpBlSk5KU6/opSGgH9T3jj3ihXJH0Py/bXJxK61rAghOAFWKpFEC33In3NiEg9P3NGhuhMJaSUOZTc2ZTl4rI66kacdRSj44fHWQw+ut7MYFlVHx50/7ahhX42a4nA+BfuMl6j1ijwZEKG1M9cl78VSdi49i+wjNPvzQ+ODsPj1jyFu9mL6+TmNFyQf8ss7YNbbxiQSWUftwLiC26leS6UjjiVLxZA9O/XjgxWQcdHH8sHH9YSwizCStO6dG254vGc9BCLg+x5HZqvCEPhij75KgN93wBSnSKA4v+sDt36uqpEZW7D1Zhl/ksAR84VQjmCOcZf1DDoF7LKjz1XG2RH04cOoQ9Bilm2AEVjjtEjWSHZeQG7jeVC50dJS2DVedBUr6WUsatcJYskiSr15zrvYaIt75xdsl8LUDeDXPdkvw2Ue0zeSLosC2yhyrqu3+bRROMfROAcKoxoaDpIRAwMQsLTywB3h7V3OnS9efXYsil116Go9XL3c+B7yTHXqp01j6tzGyLcCJekjpv/7CKNGIgfEnSJA7sx1jATuuPx21FM1RWn5W8pGiiD5i3daFhRcBX+3z/ZziYAYFBtz6AkkdL93X14OEEPhwvwvufrIXImSKLKI3kCemQGnmUT4felbH8qXeLW6rnqZH+cNqJb5YjRbj9+5ptcqmtVnxuCS/gbEMWGUr6eE2Whywemv9L9bJc7dqBhGOLTWoVPpJdZHn2RJ1tJfiwdONTG4Lw1+BOrD7eAxP8vfKMNUIatBDYRdYWYUSMTixpnbTJl1bNGYFkzpRGHO233d6wdbwlZMvrOPj3GAZjrb/fg2CuListdrYpOcQJEgYLa9D7lWC7aJt/cyXIJSug10NFrhcADHnhMsHSikMmh9fqXsiAdRH/CgK55gIsgQ6i36jIE/9CcvTrDAY3gvd4MvsDLacllGdQJhjim+zA8IaAHulARfT4UR3UidF+vWXPr6kOQ586ocZ1FuFl5DV3Fjw8RgYgnglC9n+17RJ0aLggFVb2yr4CxMPQEwSJsvWM6bQfDi8mBt9BMD5Hv805kDjQVG6LH+N4J7xJs6HMachfpTgA7KS5XYR+fOjExFEnvemlFKb68NLm6KTuXxDKEywoLjpvgl5E93cxqz20UQqRR9TVBmJc05JnVFRUWfRgtFV2Wd3gU/sPrqcZ+SEPMWMvcvMH3bNXwTdhLhPdDV3Fbv8o3VPXP+94kDHMZeETGVafwSm3ph1HEehY+RZF6WBYEeL8JHdbx/PTUewkXnQRyvYPKR3Rh2KPEfHbi/JCpUDEskq6P9wva7AMCEBbVk8pBF6tw7jXB98aCYPgTec4pb90Y9zIf3GHaeWYwttsJQO36hS4AwCIaHLKwd9UmWwAtar4UQ1BRCAE/zS7luyNUbUBaY29fe/ntwbGxyKFb8MJN8shzjBtv7ZuDy/gDViz+eCiO76LWGVIlYuPw1TIkHL+J9VNqLif2u+gwrEY50/kOdRU0+kn+yszizNLM+OD9sOx57QiH7agSchChoEzF3lVrssYYdhmudyjuAibdEZGEm3/WHhjI/+ep0ADTTOWdGftVoqqw0+M6SZ/smGf/9QuiVKDDz3gtlbfN5kfqdk+CUz4vFtOk4kXdVigP5HxvE6BV7OZnJ/OkkYxR3SbU+yh2A6LXecpjnKVOwicHRcfXD/rHA3nm/CvCPoMbPiDEycmf11YaNRxuNj4yoVi3xysEKySVE5laYWden1v2Nwdu3BqG4lqS5dr4sugRH01/dIVkrC/uctkXJqTgSyp7QuuZHBUZjmMoORwGo1B4DFRPmECZReht+GnFC9LrV10vMOQfIxHfkoGoQ/mLZDSeZA6nUdOfkXCvcBHYdO2d8Xj171rLxgv84ON3MumA6FfpuMfCC4cSc6/I24rPxCIFJQq2nfGd8p83NFxtdDrSN/0Spz7ZmyQJl+MAdlAGvA8EJokUX5rnwNiXBPeYloU+lwGOaIb9Ht/V9vuX/A6yNqM78qAI1nltm7i5yK/gINWPXfodAaPO+UE2IKe5NF/ZIySASC9NIR5y/zeXMSCktNm+43iH2s9ykHVcletEwOIKD6+pDN/cxs3Mh0DraPUHp4NNEAHlUVSjCy1/ZUQ4TJ9KMvjogMfBhkHQaU956xM15CXXbikr2Bj+Xz9Ae8tsvw48hIdgM0OlTI4ymuawsOkL9ADuDQk9kkh/76TkHGz69IsLQZBa9Tv0SQu+vyETgQJ5qUCUmAIhW8EAD/Rm7TElLJUiGEleUGZ0Zz3BsQskUbGsuOyBTcENyW6mRSRRkp4kfry1nh5+U+Ulo1e2hedbwCp5guENJtmIfDK01pLEFtslAGGtzPq3Bx7RbU/f9pgDfERC9uKKI1bIOsd7MUCi+T9ho76oWueHxX6rNRMZL0LAgMjoCr2mF86SnE5VN81J1tZLZvJKEp6G+u8sKT0nd1/3di+z6/vwk9J18qGDKivwmWOkyGE9zbpV5Z6yHnT7SvTuP39hEEfReDtlCpn6+0ObJ1+tMza8Jstbz9awOW1ukBAHcm6TwtVwAfpNJIPRk/+TdJQgz5B9j1cgOHi9o/nduGWlinMTLS+8yMeQyZpgzdpMlr8Ep/qPW+01tcFh2XyUhPX4WlmwpC1UbxE3QoaLcFL1/XfuEndmwsXv60ynEgqV8v42Nr8dYxCrhRojALkbXc2sFbn3JgLvCy2qhvt19W6t7rleSEVD2SINzmCA9GdOHytJrFjGRcraPBaUsxNpxMJmmH4YIiibyZZyQpzn7zYd1DrI+a/OuTKJIRgaXhgz2Wub1h7OYjnefREFP2wO/dR4qkcgFiRC9slslcvcraNNP2XloPrUStoZN6L6lS+hztQQLc5AVx5XQLpMCeilPL49kMHKhv72vOYrkHpmMkMzVWe0WpG4nf149dJEyGsqP67DYisP31vGXDle1NK++asq8FED8JhQdxm2bVzDxgYv1PNLOwC+NwqKCBqvxTE5HKhS2X7PX2z/2pDHb8L2vOyNjZ9qpQCOUn897XKVTJFfc4n0QiDzauu7syQlqjD0Mn9oAmx4oLgc3wlPp0gVm8pWy/wU/4sW52EA19lD+c9biFNG/wf9UpW3tJMLrEvFJEqZFeR3KkDQqAbQyWjsa68ykccadNdc+3U08zYjhYIKYi6dcqNkM1bmPaezgG7IThbKYp4RKanlAd9TnyIv8IusHZ6JJyrPyqiDPP6MVssdnsnydZpe95j2bxrnWG7fN1GnHi7sPM5CQvYKxi+AFRCsI8E5pW6SnpXxDGoLNNbQpVChCwy0GiqOjkAVAxlo8H7ZZZm3kFnt5vLgHSO6jO8f4Pi7XEtTTQaKJ4BmObWAxN8FoTrlC7/rKNkf/r7PzRyhi2gisS6X+ApG51U1ScNy4mGtnI8aUYBZWGV4cVdFckIEqjs3IfsKuqe5uTKrjQ2eFL+WjjqqraQHVNpdG8jR5dcWbleKJd4i2czr7cdBWRTJCp6keLvK7uJrPUJKg+j1ceulE8x3OF9Daa3cZnJDgDya6WtbFNTcwVuutpTfBgqSzvzAcgdsM2Dgmuafs4C1bWiELirrcoZxvYORKRfwd/acnJoiJIHnV/xibwDv3JkPNQpxtahsn9Lo2GNQ7Ae4KjoeDaqkGgUd72EIZovTsynCrBfQW9ho/V77dkHx1OJEzUdztP4JMmtwuy0JTvxKzHSEmB5FPgb7i4EQuxhJk00WSyGa4d+zFBotTrOmTZNPDfgvN5S5VXBzFOhR6iahLH3P6I9aRyVHWmC8jzMERmJNJ5IogZ280tStSNeD50VMWYBlVlCwEgvR/IupH4h2x2ndhcyjBjXhuOISJ8p0i5i1TfrKRznIQRr/7xnNNpila2XlF703PO2Rcmpu0B71KWmZL6U+/4PlIAxo6qGey1iHXQ53whRUwei8IHs1YXZF2z719VxnFDo/vjKJPDY07x+g7UswSQZZcZ/G04Sbs8t7pnfJ7eKHT6cekd1kLYlO473CMaGuPSVKpIj7ghr5w+cyk83ncA0c/uwnNSGBfuEG54LdBw/MXBQ0DgL2+V4GF9kg4OQrfDKY/vD3l56I1p2potzn141oHYdINHG7aIzHPCrTzok1y7zNz0b/1mFkL9GnTms7jzZuVcLcvfqOIdHKGvu5kGGKR30bP8Bp2AW6yRNUVa0vvN/C5XDxseopz7ICYQz9dUuwPK4OxO7uMN84q6a2W5KRT9o2gyc9vTI89b82uRjkGdLHmFzvNfGLnZ6gZ3OQZESWZnBLs/dWsq8XJEnRqzYS3/w9gbabMrT2GrgYgrmMkIrznvZ/AyAArAeGLfjqzPKPo4HqPiFGpcMB3d3znHZ/KfZkUCAP9kRh4HEZjO5zg8OEt9xSsghO0BNNqanEeDyEzeyLgKAU0p3aNGBLseaHI9iVclJbCDQhklFQ+JDYAUAGg+2jE7q+uIzpHdJU58aCpPYgTXcgOZcXKoEbHSQlk6bv14fEnQoiA+ESYAtNJsnl2OQuY91DaUxKHSFbMt3Vv370k9n59HnN3Fw2xzH1xR+cDJfJOmuRCxVEuOai3xvjM0TdlAyNkgWVe66gGdowpP5739CeKk6wj1WM6zGRK9wV69BG7DQwP2hUyvxS5yrpS9n45gatgqh/NBHSDUy0R5UJvksttQ1t7JSZn3LoHbC+P/LkSKDorrRiXiZ8FcTv/Y4bqBNKXtbKUIuM34in/d2DE+CRnGzgoLuLx1f+MDHE/CmtMtCFqMQBd0jpZcYojplb4wXOeLc4+DT1qrBgYq9Jpddp5ZAFpeeUNCYPb1BDQo1G1s5bm0rWV5CqPZ/exfCx+cJdEek+NKB8tw8jY6nWJ8YeUDth3JOf66lvW6z5ZVpzExGNQwPJVYUWIrxyG1pbLfqHlTo8fl196LWJ7bPZbhof6S57o3FbF13qAf5+S8b3CdQql2VqohH0P1/ZZp0BrEQsoL71P0u2DHyVuIwOgmhtH3aMvtX9hh+pgON8gXTDIy7c1DT8ekkLZD08qiccKimfsksP2y3HbtI6PZOMOIhj4hMyGyBnHeMqr2KlZOsSPctSEUsECX+YlrCPnOtpdzeuA+bpAYRmPgXYR2w+QDapVOXaELVBUlDDWFy0EsHK2asHHDXXL+BXrQ1p64bsCqoprNbOOWU8uNb+FPh4cjoyL3xTJlGordv8gC87arYCz65l6ogUswFEcvBCaPXDYRHzpLVKGvkvdmex+iFFZIQzeuvWCUwSgFoaAugUZdzoXGmdFsbyaA72MAsIhwDric4KgmepKmLUr5s7da8J1+NOfZqzLOevxAzRDbxpkVDrkAm32CWvJEKGe6s8lq6yjO1JYlX/xrRExnHwIB+41ACF5WE+45cHl9ylvu3kteOluBPTVFH32MPo7ZRHiosfHRDl50l8Lrl/C5wCmUoaFRqDryVy3PhocuTcXJkyHnA0F05bAoH0Ehh1V+U4zhOsM2KQHhw+oFprrqCiEgViMr8jqILqnOchoLl2Bn8TTcF340hwlPuH7tO1/lEWaMEjs9/AFEoFbcno4Oq+x0x/R6iZNtuWch+aIp8RyHx7jpCna1tTSM6+zbWUX+3BizaHbWi1GIl7ioQVPk/eFLumzE5Ln62uFS6R+gMeH+jyflKbVkbOzyu29gh/7ox9FgpvQNI4Yan4wfdCitB7HbQMRvci6cpfL3a6NWDSF5G7OMVQZAjPVMoXgy4IT1cu2tv3BwkfRks6teQtqM/uUVHCdiQfLqoCTLvcmuPMxeRECTo593SnZlMWQ5uBu87d+TT7AXWizkZ8aP5jk84hA90fXJwUMc2xUGmRxE6q3mK+5ATY/4n3w8B+sMYnbrsiFHMy+1b74Q68mADXlhS3+aHcXEzFpbCQ25x6ruVmgTVThx4/sFEEe6D6OkKrOAuMNKjGC0eRgA0kMl6RniPAYZY3FMSILcSsFFJ/tDn2la+UjqGtTBXjVWjE00o5iuHR8ek001MIf3MVg2exk7Z/97emrJ4sJTUkx5ihRlbVwEd307+OBySEq2LIUUCPCJIS9ASi24dCuB4wn2LDUu3XryJ14p4DeekqEpvJCWFWKtJ187Y90xTqW3SAhaM3ork+wLVfN5yfbvfVUhHtVf7Gm8K8X+YwVeW56D4PhJvwdM3qbXWp2UDCyBRDQw4NUt7mTnnvQOJB/jDXZZuqE4kutx0iCQOqTtK0+P/cJH/P8J8bjDMof1mG6FodoEQeZecV0A7bCoVyQ5jG8e85HgGmRLFMwiu7UHRu68ejFL1YX63W/lUmJjgbqJiyF1lmJ4REhLXCbZ8Pl9Z7nPqibjbEnHP0l2HQYKLJFTnM8qtC/woepGq5f3l7g2jZbN0cadNs4xeN+IQRAjDA04O8/yptq/LvThgbbC5E2G/y6L0O/1GSbbUtEk/FW+rFuSl4xF+Ue4W8TE7YSbvm5NbH1xn+QKToLEPCFgcqD1xvKi0dOhG1EV4ZzGoBYMvheIbJUZl4g7GJbwYzTj4F+PNYswoUDE23fEgzO7B8bbcl+KphGQbik2aCLY8wdBD6z6eWkx8y+phnDcpzyRHUfOLIAXVuYKYTD1CiUyG9qGbPUHO9vRdPwdnOWDwJOczvAfmygOuBfchl4sypCYgTURdIss4B5wcPGrohNnx6OA2lcE8x+2Db9RyYINUgOiBCeimAI4d98YN+hKV95DatBb0IBQmJjbV9P2qu9aLeYfN/nQYj3/0Wafo0qhw4jK61mqiTa0QB2Ywn5uphDzFf56vylYjFYREqIwaDppVLjVS8yftuOzwKZy3F8hBV9KqYJm6zokSevZMNR2XEEDD2ibzYPQMkW72cTYcXHlfn5dqB+hIDZ/C1GU0EBuHhDxdJD4cYxGLwO3NT7vQNmBhHkIwgeYP6u3Phwig9CdAmeXG3Z3Jwu9AJDfxykK5qA33EMsJNpnujD2oTtnx/Svg+YsYK65/yLfac6z2A1DaYQW0+s5XM4CN/pSJMKHIzkD3AX12a4BWv2EewGvllfd8Th3dCdFbMulpvMATrMasSJ1nzpnEqWtlp47eHHI1z20WKQtai3TzLANEAri0TTymedsFl4ziL1vBEGelJSHQ6tUbhPB3uCqNhsIjGBCzmzn0c1UUNjHsIKvtGx8X/c3PyakQGicp528v9xwLa0pRcA1+PYWu4jw831D4KuX8dVt8eRQtEV3XIohNYtLSqSENOXjABZjFmuG135cCUa1IojAX1znNW0KAwkYLINfMxW/2rmYvM9P/tzVrpDG1Q/1vw6nEBRhgIUu9ZAbwfHOLlYWJhvhZhIFlWUFkMhpeh8qZYKcLmuUmZ6ceFJu66X7zrPORzz/BPCgZ9HiqBapayK7Pi5lTL8OxOwZ75kZBFGo46Vkymu17+l8FUVXz0GXtCasJX78dz0ZHWFRe564pTVgCzY+BE899CMT6Wx9XO0hO2o5HFoPHUnTd/PEv1hplIZhXm/K3/2i/PtY2OxJ5VPN87BEl3q/sNe96zEw/Xsf9x0Gjf77HiAmXPt/p2h82IjxIMtQX4F/9URXKQ2Wc3FQE2fO4QhoDDbgNNNYuOmV1ZNSC4bA6D6PicgoRzX1jXAUlDiBZGpFhAW/Wh9ofjemWMhynsXVZ8B2gLfwqbraxVrSJNCt19kgNzwcasp6h9tc3RmVGWMdjJYTLD+BfJaacy/V4lwhCMGmwl4W0azwPUvsgeNm5M2aoidOlwSU1KoH65ZOwAlZhoBH4ZT+Q7S60P8nyYgQD+zGz6FFPMfBmTpTDY43tuNeMVBqhm/J97gCYQIpeiCw1LKLAyX7wj0SQlbJG2HeGn0bxD4H2oCSUyUsEJ8eVs2rYg2na7CCb2KjIPRjGcFyBOO+CGEadTmKoGXWBKqeySwVTQEP82eTZUlh2LmHdhx7k570TrpqCyp5Vxu/Fcn1NgR/IGGoMPfCxvR3JJY16CWMtljsUhVLCc75QLDOlaIDLnmI0fV8MZTIhpTzENotn3oZ8OJ6lNqdChDkP1BuGEbMEPYcOqgeGHnqWr7JTU190H6S+H5M+7Nzlmc5vEPsYFVIL1Ki8CUZybVZSNIjuKCkxFi9dYjqOoGKrJDtgXknjrM8YbMQT5rlOCx/TsibuV6oCCaWQflmyWOLyykKV4C/P+2SsBJ3mxo0JiOM4O2oTpauiQVJ/anRfxIH/p7bA8xcTzt0YDRmQA78Rl9uaLTdENjJx0t5Sq0fsBoBQ+bGMnYqnEX7Jki942YJ73rZNJizvviovBXd9AEoD0+hvuvwL9mUIYKovcGlSkdsIatAEPhubdeEMAmwa48RjHh87t9QklCENMJNaMcKS5XBly4mjWh+O1AMAubwoFNIIk1vT2BdSuJBypF3QMdPFZyu5xUwbDfKEhLcL4f92ozZa/wmw7E5EmU1Hmm/NpEukuw+I0XDFYbc/hxzfk0r3n/i33zyDFHlj7VXhKTsZaFZ6SoWQRbttrmuuGl3YwFtD6DkQmfIZCrvhnT9tDS1DcI5BHPP8rS6OfmH7Uw6+AohKro6OqfJyvd4mE2Q6l+zC9PZvweatiScSlmWWOTNpOx4TLNVQAWUGbQlB7zSzkfY2cPAJFoEIvsec+ncNHOWMA7+7a5edfXHZUmeeXwt8ifnrprak9SeDTpUHjkle4yawpw0yhxSj73MFNgxz+ZaXL614PZNmwEGXeSojdhAVwITproke03hhIO93J86nD4aWsuwzkJYk/JXksDO8ESfGGcZ6oRvqbbpvPG+OjEVIqcvb/V1gevDFPc1pCnolOAEYXO0yDtcwpJHcdnw0CVXlO54lWS5ynEbg6keQ4QHDVOJj4Tn4xeaVkrD+TdSt5GCrVtbOcxhre/fOwEq4C2TV661k3FKPpCb4AEwyyfttFhf8RYchSaPAGfcBE6EdLCw60MN3TMnlgHfJCDQJB1XYSv7jpAnLV7WDn94Q+UXISCyGek/J75b36uqw24Z4iwGF3Z7rsRXJLCZY35O2RxUVHGrHDkPCWlgOhSS+dkbbxFY+mD5S8pY8phPwHpz6+gf9RpVYtNG+ESE/qhIyrtAS1qNjcw+vpjvpoURoyszz2FWxf4/TPYRgff+sENT+TG8qWZ0G+Pii8eNY0Pg01GjuDnhDaNwS+sdiyyV68+/aJXIiMUVha4a/xI5jum3z/6oFcEdpIpbjYbJswNW8zi768dfzcCokfy0P0x2w7zIAcxylVgPv08OBefwY0mvzQCuZmvOAz+RYTwaCdTwYZpnO7+VnlQ4hUhAFqtJA1d4xOrhydZHb6iHQkCXeDvOymnngc4b7UyTzweVLQwYObfxX2rKqH4NpOOIM+Ncucet8vYKj1S1fDFTidTaq5/pCmrBwYyKJ5f0LoDbrhOGdiUitLJjulWkyUMt6Y6Nlijis4ltpBqJgYsEWOxLv9bUHsiCUgjn2YGX9tE38+RbakpsDX8EV0FH+GY0g2tvfa8qL9UZCu17SAhXhVmoZURDPaUToy/6Gh6btyp40tRnd/zv78fCDo1iEc3spKrTI+qZx6XcJLOZg/atKikH9uymrcSwVcILMcHTI/Kl3gGv8TxyLIU8pvye+2PB5s1ZbCj1IdihCiZJp25gAM2MM6S7wsCJexJDFqtKtJql8j1J8lomP/X7eE2bPLGOqVX5NNB9zB6I9g0Cm5T5xu0LTClH2Aj4M/nK99A5JH0NwvQQ8/wHP0b3wYWTeoieNx4uV6gr0buTXh9AhplUdm83YjbuVe2nc6s6HXUkVi+crkMrnXpOxs6OSwUR0s/leDsNFJx3/cgsf5KOQ0cIKAnG7zHNzwJiGaPWl7KdxaOOzdEKBNk+DyKD1ysKAmMyBtz+25DOB4PAunwOFuSppJ7CcGnj/yLE8KAXKf+60BdgE2tQ2m1EkgB5oF90Qdqn3GjzNCy+XqlecjJNZJdTL5ZdofNjVticLxeq8uJirirwQPMM9/3lofh5YlL4IC/zzO8077U3d+1MS/7yVDlRNHprmPaxOemyQuQIqkYERliXf8Tybn1jFRclTx8sQp0x9FRvliq7gTCAtHXmH1MKbr6bfXZSRr370EMG5FxJEJPs+M2d7B3APY9LKtl9p7P7XM0VbVdCLwVhud9j+gOXmly6NEfjKyIb5gyluq+oseTC4j3I/E3u1W8zRrP4AOwxE3+as3o1vJuHucWbN8Q9WD4592mEG1yZRylyUc4WPHdsPt4xb9OkHgpggO22LcOsIJS3JGOHikoAVs93E6Qd6O7i2+TdAVzVsrcgjrs1xlXpA9EziUWoD1OnR6rc1Dqj8CDeXYx1QQ2NNU8ELaWmBcRXw6h95/tMmHffp70hH0aA3251z65KWewHqAp7p+ZlOvwzHC1Ur8TPTAHv0tsq86mttBhYsPuLADgl/uxA7y59IE4Qr77yzDPCU7wag+lWiCJrES5ybdvDTSuoOoqFjvtBx0BWsT/1Kyi7+JBF/fF5FWoq6jNjUt+lWi739NFcbrN3eZV1bslVHWVF7IBwwMvjJok8JYqf7a9L1NHiP1ZG9tbg9Yeh5uLyEdjywiy0gMjFTDSBi9YVqgWb+50UuTWa9f9Y1kL7gh5hIawNBu4s7rrMZFQ9o4Z+zezUxBcve8LHAtS2xTg5owLsPoBBDZaJrbsFQ4jcdqiyi0kb1uzIzOBeEXNyINWZWDi/dhEyr/BRbsV+q56a5ELrQbHi0wHKtqsFtjjouFP1pzcotyyu/4aQDUwT3VMfOQiS9+vWip8eCBLWUqwLcbqJNwE7oMgd0/aluuDgM7r0TqjmBShNFPM3S5Go9OROCC3VwFPuqcoB0P5WdhwlF53u7OgW/2MRbv0hti0yONyEa8mmuLYFfE9hFgtvJirFcm6E6YnSSk09zpGeldojW0U80BAgrjCfEa4uuhu6MgA8zu/jwpkc4odmJSJheYqQ7ac12TjUvVpQHjN+u+84ei4ZsKaqCH0oZr+MXXyOPMR2b4RqFkOwOnAny2/3YH9ZbCulCA3TIDnsl6k5NTTuWa10NxFcNgrMqGF+n9/ceO+0x6sBCgIW3oxfVizLsfzXk/2ofa1TT8ql7buUHRcGKMitbn7N/WbCv8GvrcVbXx53pu2l/kMSfJDJ7vDg1T7dAkMw/etXlh7Oi78bYZWl/GAOxyBIDRgxg96ORwAOX+J//dt9pQQ2LEAZbfc/CM60bTkpBW989RpAc0/0fjGgvSfuH7zbawG8rxTSI7cBPMBSBiDlhkGulL2FzixK6ZIThj0n6CVj2Mw//soCtiZ9KonbQoNkNiS4l6XjKGyhNPiQYAzClpTCuQ2SeO8uSZGDRj/3ynk1kWcOIKZxgCjlsBkTGVJwV5sfBHUcTT7g5EQRZeXr2nNTD7iLhzQ5AbVPNlSF0kzBO18yXwkW6c6PczpSOpHYKYpgabVsi8qrW9tp15dS66JyfWEqnXptPIEuLdDQNo2+FTNxXBvyESFD15plLYeOf8SdVzSmEGFV53awHSh+OllfIlxnJ8ESci7yKoLNCCWQH5uRwrdeZVogpv33/4xUK8pJE41nbKx3motOzqqmO9tbm8Vgta9C/wgefo0J7uwn5cIfkvfuoCX0Als7orGlFg0WnJOVuV18s4iMD29TUdB2+HqhRk7b7GrtbH5KqCL3GJXPSWAgfHUZeSDqvENdmUJ5S3Pi7xyrs3F7jgGmEjOuu03rBFJCma/e1ELF0P80mbvjwfa+B00FgFbcWvkSm1E304omXF0c4kHUORpPcrMqmjg1BFury7DJ809eh7W0AcCE7SenFAaq9ScpEAbf3fKEn2vMAXNxzgA3qk3absQFsIdixz2CVxnz6CM/QRDqJkTdaO8cpcRyrod+AFB4rplxfIZr/jlJWyQuzprN1q+ptHO1JRWS31W9d72BctLk7wfLg00C+RWkMymHD4Wob0iKCBq/Qa4Io7xT778A2XVJLWMyo7Bqy1K0fflkW57VOEz5UZg+V82/LwZnyS94HPtzpxuh+5R3ZokXBQdARRzaT7RzMLpHdPVUF3d7FqFNCvQ8p6pXZe0twlbOCFTkYB0sVBA5G3K3O80a3AJQGYAML+H4STzHqLJetgIeTr10gRqTUL0fE2S1dFQL/gM1i/KYFSxP+xemQICNN/iE7dt/bgVheXrG9cFwdpawE78kT2tFH1IvOoAPVyhx9/WyV6iSx2SHkFXGwyrhVcW3kKJerOTieeVC06xwVA+sgzia2zeAnVI/OXCqQWeq320pJPr2n01gXeynwAp9nNZHSCze1bJhUev3ILDDXiaqmks1/It9M2WCoZMFVK+ML4Wsip7jN3Fj9MkiwrMOgIZ+gCCo/yV3KM51VrihqQb3BIMCJaCEh+EI+q05SlWFRY9xy9Rnh8Wsw4gNH8pEpOdlW/B0CXfms+hp04h4lhBw7DQZ5W2BxeMLDBVxQauzyjxapNyaCcuGK4lfDyZM7d2OofEYsaR6/2H8YnMZ7uy1JvcIuZBf7G4b91l5WIVk/QC3SFKp/+r9Yrxjpe3+5OuQeTVMNoSPzuggv/LjJ8X7ZQJNuLdmMvKHQyGIV08xUMtY7GABomIx7WE9yAv41E+9YiiuxIZtKwo2Bq/D/s8rlCiWnV5t8KKsRv1CvBGeQVrS30rxPHL6sSX2nvaLaMCeMObr6bx+YNc/vluvW5DG/AfLkm//pIdIFZiEEwp1B6b2NSeh5O+FlBrbYoxrl/yALyLGuCZ+vPGb6ckaLXVSKaEhPPk+0PqaANN1GsCcdJWigRlYIEk8tJxbFQKpo9KrbIRy6qWLh53ETggTGHa1erNK8KdQcaDeVblJDsYIJJzJ27MLuAnfEcBwzz716hy2pwK9BQv4w4LADEBFRDGal3umDR6pQQ1Xn4MzLXNGvO4GZRA1mzj5BZPcbdBpfQR69HiXCVYWxBnXnUCqE8mh2TTVrsEVDErcuxtTHePz67g4+hH1R4mOIG/a3EehlaZ6JQNQN2AiccnTUPffpUO2PKWKcW3jdVGAQX2EwW75sS2/7icyW/NeP6kUVxEibJLocdUs608JgmR5/H4m94nauk87Tj1LCpztGBseu72vY4ckzlSscR1X2BfoDrWgsXL2aTjKhP1QYFsg5wIOqUc1bRjPXh6aODQ2Z81n46mZDdqlO9JRdGWBKR768A+ooHWezd4wvQOmIxlamhCxYvgOPihQXEdAcMZAaSU8tDd3PTBIf00fbgbYV0aAmtVMzVLsqHYQelx6PZkBo1TKBGhIo6pQT9+Q3voYbZkBqzNE7KNZ2n84Ajnx5LPPqYNb7UFIsKHgifd3x3z1jwvVPPt5feAqiHPzPJB7R6FdZx3UCBHKvshXDNmYw7g2dKuK0a4kTQ/fHx+76qrbMIdMCx5IniL0RxDsmRAACvTEywcXzex2Lfmwi1QUUyp/vIiMJY1d9FxcbK3Qa19LxrKiXDP+1A+8Zc7Cnu1ylwPu2+lJfXCBG34P/qiCZ0bf5K8bjvbNZo05B6Nh6FFQnjvWGG3rq7xoIR7i5RgLcCIr4T4AxmnATClTRwbhPjqBCcUvzme/7kS369H5MsqamWnE8uLcOCalF/5h7nj7e8gOpYukMBGRVOA5pawsJ4OuUU/Y394YpX/FbQiy9eklVOSesXriWb5xleeGv6E03iSVS7mHaSeXm5uxobg20L8KtNROn3FBdrhvBjpnxq4A+oitNT0zYDTKHVmGv4C1uDGViVK5s6gqOUGXoRQJynnEKQBo9DVMFc9BT7Fj1gqNXAlBW4uVpbo1SgoiF15DwIaonQbS9ujDc8aqYx5HyEzadCpTQbasPVZq7y9bUwuqpYLVOqDHWg/yYxgw/NHrXPIGbvu/EzT4yf9kXzbJNkSbKUgFqOVv2DUgGwCj74XxdHPAAyJVeJ/yfK+mtIK4GPIkbiPRNvdcH9WzYnab5stlVYPfG9Zd4Jd7YU+aJ1BGi+PDyFO66nXoH4sNYieXbRmt9aIF9Nnv0xtgemqtwI3swi3zBJSGnfAE1Mwuu0CJ4mMwjDwsLiqvXghb5dXKKu6zCv434mlJ2c4eTjIZxgm65HWv1b1rz6fV4voKM/O9wp1jR/9V0Q0RjricLbdQmbFePTsocd5fKUXWkqP9xTXzf7zLPTbUiTlYs4Fxev+latgGssElRXWFWifTYjWZv/TF7J+pdW2e8GV7/gOfA12PLdBmnR8rAvVw+BHHrd0UEMB804plIniqg5STaDzdMV5OGawjmc2pSaMpr53+Dxx4zYKCYfqvwFdDfkT193F0q28UyRdBZNPrfy5PtvocIZ9lNDdEWeClg+1C5I8dDPE1m0yu2Ddl9im25mwkvjHAmTY0b8F9HXuCd7pNZp6A6bl7sLHXqcdxRr3P2aPCMzVUlrnyOPkSJ7pZ7IFgTpFgy880YE0tGFjxnKsaIJ7qMwxJBjolunsDi9hIuO+OvLkwlkyQjWhhvPigujN7EoFyVFAyw6AdpBIQLR/fJ+O41/qwUq8sy7GLBPcm0WzxdAzG70w7919mGy3a4ZYYERGYhBDcJhtFSzD7ADkvPr8bke7qrog4hNrmBVCAtkzz2w5I3qyQKHcroYncaNR5avDwZOL7LG40pN6p/QI4WrwCQauAqy06/EavUAEjedL7TiNwxDUctbMd2eWj2Lo/twAzxHT4yjbfLC9MONjr2ajvrzelr4oghFkS7s+epwN4SfDEch0Crz1d1t5f4aANLT6U2Nuq1hrMZEoIhaJrnNevB/5rY6sxsK7HxTEh4J/9MITPbas7m64GxSVbdfysu9IMfuppaZAzGEo8ZSfHY5TKk2iQ3iREJgyGDV1LONR6TxXrgl0H0FdeV8ihb1pl6FhkANDtOsLh7l+VhaNd9aWo1tw68AhdCbvRHzQflX9TofwmRgyXi5NPJdcatBbGNswAfgv9FlLIgObyedMAPKuzMIgsSY0MRECxwgwOeuNfql5waYVteuLHl//smUUBhqG8uXj/UPEHzL3BcWL+/jGl48et0BTqk9oKsBbi6ovpzOu/IJgrqegWg2beFXw+fGAYBSK6rC5I0LE7u50jIn5zapfKnI472/158Z+RJ9YQIwz8oT7TWgfC8J08TJE7tyymwmQcpXsrSHvQCc0Hy4lGsJJavnOvoyO9ePUvnHj68mJmLQKsE482xOxtvHwM9Rxz5RWvoXmrpqmAxSIe5nu89CN3oDeUtnlgSHvClVt3mlIFtWZywTwIZyI72UoRP3Gz4+BqpF6wVS8OSLdu7OxAhPDno11BDxcPpatssnz3gJJbEyIi/KQlvh9LCZINKWWpHvSpV98ssZHH0JGSzx1dd39VJCRmf4ezQWz0ut9qte+MVdZuZ8Kcl4rICs/IshglyCo4b6FtLNXaBLi1tH6hdxrEGuo1jVIFSE40gKygGHdLqTuXJxNuwAwUILeV33Xs3KA89ce1FfLpl5iazdoE7jZBl1fY4O/CIJDJBUytlDXZfs3KvN6bj6s0gSL9MbkNuzp5V/SyS19tiKMhu0wX1LzsiayFPrOTN60ye/80TMSJvGnjSR6p5lgl7p+OCbLOzuTPZyTv4CKlPAKzIWN6CcHcmBjw+KuNsI3bTiM8QE1A2Gx3e10Y8z/lMTaZUqWu0QxHHL3K6jyKYJJSkZxZ9KZFl0DT2moY8HsKwbdmeM89hovQwgc03G/5RWM6JIPrkshWTmxGikTc11CstXDFNHR6EhbTyTevajqrqpao6XtMU0eITARttiwuaZYOKNjuj7WG5MvKjdJTjk2gZDlVhPfJjTWf9DLhjJjTCxOTxv4AJG/ZWJprSMBuC6YavEEr4nmd2b/6ytk+EOJA9XyW1OytkG6bUDDU/lAMJNeFWzZ7R7RiBHa/WG4dPsjvUuzx7EDyVSbkAEJDyNfizFqyAleGBNq8u8oZcabN3tFoag8+Dr+aZcgg9aVlPCkK+8myWf/wO+BwjPX9de9qQspxTIO0fzpUug6J6jw3H6Y+BqMejImklTMciB6a9ToZOYCDN50WxFz2Cu/TgcUem41g5f1SvOC2hLJV9fO7Zu8nSL7Ttbg25oybQ5rg+QNk3w09H4iixloaD3bmwFYui3UmKLEzytuopC88CnMdXHZm3QDm3EG/H6tLn/gVORpUKzJoKKmaL5MiZcrUyUtNY1sp9VnvNH/sm9POjpN+6xrsR8hxGsqhvlewlyW2IBPdKtYPQAFkEP8+G/rlgSY/b6+dyii0ezMNHK+aVVPScfAyDAiu6yXiua8gv7iWEexTGbfZA9+3C8YNA//9JfnVtwV8thUx0HbWSaSeyAlWaB6RqAA7bsssls3+cvydt3DuHrgjO4dFs9tWIEZ+u2dUDeVCquo4GGJFoElkWgxqYNMD/RKuEUpQH0WJL5UcPj0gwtfehMoRzPEHyBpQRCSbr1OJCYKWdMtRqdASgFQTJsjc+/ugBFE5oQTtuoX9ZkJP69kVJ2dgrqaRM3y38Zd/f13qeL5TzONnhpXNaQ7RIjU/5ia6Y57pUTu7fgsSRDL9HU2HU6fyhnbhfA9GmB8ICQWH/8IjoFJw6onUqpCcaq+G3rKGToRhyLvDKNTf7SBUAFDEI0UQoSm+8FaED5X6eV2d/VDVsSPILFiVkbc07zfhVePEegKLfe1Nkb8UQ1SeEfbRT1vtYUFTEw+hhfR/EKvYb15hGc5otSgnfa13D/UBPocVd60bHSe3/W7u1qted8BYC+YEhw7yeZHzoZs9LPA1E729Y0VQoYh7Tp26qPU5L+ucb8Cmx8S/pZQt9koMfdFqCTz1gxpYzub34zZ7bQvyfwjJMqqzaxDLuIT+jw3zIa2TzfpkOT9qHAjJoLwrl6iAjh7QtLOdK8VdDz8yLMxshqqeR8Tr9e5lA9WuHLRB+c3Mbs9DyZAPcJdZLNRppz9ijnOVs3M5h/uyBckzf3fBWQGS2a+3jD8ENMQju9kfm/oxyQWkOB0mdnMmbMOGId1jE/7EFVtEMYeTeliW+jhwBJImg5c5IOG1cFdIPn5o7rSZpKPhsh9a/fnyZ/kg1V2kuM68deI0K52yYB8GrLDodm9V2SMMN1Yxf9/ufIlesX0gtwW2qZ5bWZ9z2IdLzm2aM+y3NjI/1jGk0sqdU9spa1zNLk8bqIp+RjIqI0Hg9b/L7CI1UFPbU8nVmAqVcG2Kcmr+jrjHVcRiHPJNZI+pw0j/gM5RXVwVnoCk4h5gDvOiBydSJ9tI50bwRO72i26mCMjn/DjCeCbxztF4aKXjFj3fRmwwbe75ch6SY5WtSSX4XlHpSMRAjuIY9caoB3+uhquKY0SNzuQueJfxP39lPaNg7eXzM0Seg9TESCejB6P1i60y3lGzK4wTesZtZN5GKTTK0R3i/fB57RGiaEbA0chHGQrFq3j3/BZuoInf7nv2XFbHMSy3uS6zEqv9RZ0/8NmwDTLF90K5wBydUMCEUEOhj8dH6AXGEwOMAdLR7psYLebp3co4je69Yjji1SIjW9AYaSr94esfK6XGXmFFzuL0Brh36djnGVZ82raI0tkzenABbcUY0a/dIDOL88EqVfM4inp/mVbsBAhx/5bJSfhgDUNJSwN5HJszSUcYSuzDwqOA050Ul5xAWuF+JUjG7DHuc+gos03FTBLLdpqlEiKNENZEYYhV8a9QVauCveqgS5FCuaqXplizDLtYAAX5QgkhqPYF+YggJYkIXxbzS5egFQIFolxOq/4ZEnbvwwFB71GAAiubOp6yJbgaAiVoSovc7i+GISa7YYkKCd3hf/AOzTHZKMTbMovhFUNTiGFc2osjM2mUl6CTbcES9A3XpTmAE82g+HRp29lA6Kv9gCnXwIoihPjbVAnULifXblDOvD58/b3y6eBkmwFy8xSD+TOjtqAxrU+GyRXEfZMAZqdeX+f51B/QHiOoUShxxiEOWkmBk0jl/eqrJwBIgDW5L3wG25eLBps+Ci/hgEE8sLzhJhNFfzZwPjfnpaCpYw0mDmFh/u5Iey89RPpHQ7+ZU76zx8+7elNAEeditNhYlbvUzQ4L1pr4JapXIdT4bQ6cfNLwqm+c7vgWSQ5IImibyrp3AUIuO/UT789+b24QHzJ5jU27AqvTCuMql2zM+XWQlui5ApzUDUQO+DFCsrcSI4q7Tnfu14g45/vSNgaLP1p8iIlwYoGRI/3EEviwZcI+6lOeuWPKz+tTgs30lmu/PSQq09C5KdY71QK3YIgpmnQZ9pWTsstfNWg0rBHfwmylKRWYfLaPVSD/hjKoK7Dukg0bOJjOTbfx4ZOy6H+Ae1gHEGvbJUmt2jZaX4Le1znrgz4A9kNLQBhPj+cFcNThH4K+a8db9mc2RizCUd7u6VUfrwtCKzTYNks0MM+vVfGxPrLQAcqOmCy0vXvBZt3DQseUIkt3eFPpe2VxmTyvxjtSH4O7mJ7dC/YCaB3Re+YDYPlE7XUFZ2FLED34ls2sqzSIZhMykSGw8mE2OMjpxGcQPhto5o+I+dKXOmiFQO0uGpNuEpovhAnJdcuy5TV41iG9yH4aj74eGlZMNV4YN5GgRv9H2YIRtUCLYZbyoBQBHrrreEpsTgg/2CNfQbKK3CM1CRNraxTt+d82CiFkfREeP0EyNhk9J4XIv+bcf0izhf9DoEAvSLiUe3DfRgzIflYU2+ieXWQb71A90ITu1NfavQFTr/ckDAkYrOvQDksHW7NX5JFUy9uyHiO/FFE4CQVsLYoYFYzUA+xOlP1UCZq7EaKhkrRnAR8lSpaLM0OZucvEygcdd02yUNx4rIAhxNNOd672+dB3BHP6DOPb3xMQfajjvZoDb296loPCqJvjFShknwTvOYZ1RM2vxu12lCr+FWcGovySL9Ve/nftitybYXJ7JZ8cLDtUYvpavsI+zLLDeU6MhCA9jZJdfu3unUH1GUvNbAob3KtU/7nxZD0yD8xRAwPRD3ThiEhH2f40HyUjp66tDDAku6X7Ln6K6JBZ+JGSJmaR2RI12scCTUX2UaQfU5hHfa68Q1YHPPB9lTVJAYkNI5jAgrs+VnK3KJ2pzndsN+tha9/1CI3jiW9DMy1WQj0q3upONua1H9k9wDR6hiNOFnzUWKe39M90re6+oWkYzMBN7Qv3RIYsp15U2JNTt1iGF5RzidTOEHCPgoPKT7S+jmO9WqGt7kq+lbo8lYDXWCdwp/Yc8CS+XURVKA2VDKhIxKg3yslRH749LwQdqwigzfZwQpNgXuS9ERdWzwwxidJ3rEXFCAs1dv3vW8qe+7SWY5Ex+ExiSfRC8NELF5wr4DD1jeeMz4aZPes4YBgfUd8jO4ua7ugGfMiILfzK81ovgStyClkkoO8TIXQ7EsTDtMaQ4tJWFl3ozvjJvsgKtTk5notHcPQkT4FksCWAznnWdalcPMpVqiCNognmzic6ChBmv0id3EnJKLKoMh8ccZlg88LU78mRccbLKthk0wKYKHmWyUIEXWr/za2UJhQjXOuCjwCb12wxV8TyveJ7NECuoNbcEN18PU2jYDFyWT8ax2VYEcGIodsu8ZXGP/auTsP1usCzuq5w5HN1tP+OlB4eM9k5xGcQEQ9eysmISYdgvqqnTivL7zHMDOcfrPZ4nUdV8LAwqQ6OvbH11k0AZPbqFW2me9O2fiXoodPSAdg9JhZy7GqVfOyquOtnO6qZL3fAY3vbICFomAkcZTfPWqn1EgvLoBBk4n3+WtAfrf5dIjebkElbnoHMPqEYILP+4m0GA9vZYgiP/1zUW0imzD3mNnzvDHMcM6Fs2YU5XeQ/SL4y64H0Efg9iVbY4B66H/ywSWEhxExQA1oNCDmZn7sC2lhQQNgfRkB2JXOKbAGXm2B1ha/7jbWUpEeEFHKvT+Gi/3ZZRZ5gqiAkFW5DoJ5zjgeZRtP5SdZD00dMiZe4KMpS6hPM6im1GpkXodCFpcwc4iKneNoYIuMgFkkPRBGkn95sx6WxLqRxdl03TMftz9n1/1C262FF34rRBocO6Cgq6nphB+90vHGnI94vh8RwaNfYmBCkZjTVrBrPuKYBZDApQRee0ksA5FhMYUpkjMNNoLpMa9mgXB5eKryfrjywBrQxWDRswOVtHfqUMgGgb+lm57AgHPXV4bdn/VnMZUPxFDr0xZ3EqqF1o/xBR0ejSy+mOtP3hjVwBQUkCgL8wxRAMlcFwWmfCXAckZsDfRenbdz+T/aKlc/xvwQrRrvA7r0B/+LshKus+X2IuYcFLIsupGUYJnzoM44IGs1I54anh3O/tAANtgOloYsn/gB0iWFTfDDqowvcHVNh4zRth28+OIBAFzhknT+tRzq2lNDUiKaEwtpGlyY+Q7bwgM0JE35ZbT9VEF5zR+Nkbylc7aBJczxfcVYxyV0EQWuYMWkdTXVxj2vEfL2dbvMn6ky+C1T3jGbIb5vZl72XXTtS7D9JWpr+aSB9kczLWqOn+mHzYrKTe/FFsGgbfNzkzPqHcWxGuqDiKRml9vmvmGkn0/NYuX+mIS7cEOi2+A3CnFZKsL5TPx6R1mbAfs9JsBvYSuBX449RL5MYdJqh762EGaMtP0wcmCQ8co/h/vguXmAZOJUZhh1+FJRXf+BW7h8AMDADCApM44Gg8cok5ZCBO7gsQjQE97orproAoMFMlZr292k57q51YlPsQort0dhjwF5QGup9m2fzJK6LrMiHoLYbafkm2zyKI1ps3nRLwpW0YOloE8Nsmoqee8XLzaXueMw5kTlx5jCHAlXZIK5Ymk9rzyxtANz2HLFzueHanvqkUm/sKyKECF71mHC9AJgURMTf5rScXnTe5Sh8A6V2KclXVoDQOrDiekYxPN9csWHq1y8E5DV1MLN9hOrqNQkPY6SJ5L5KyGQiupp+ymjI9nRnx8dJxPxn0wP0IHQPHop5DLP2R0AAoXL9hqYilyCZRntuvKG73oIX11U2zmFtxn7gHtOyGBLGyTGUflHAj/Qb8Gz9V+FVsarV2v6U3daL7OXYOe0Yj2kwMB97Mw2isc9rJaRdYlWUG9/W9AyPSmLiypUXCbourJn0fzJ/77DrEn7VwLWAT+xQX1fXRi2yXHOH7Kv1vLS1lVaCKZIfNve8TjaHNn3Ew6gSOUg+d66sv2hpmCvvOF/yJF+zJgoFhVRkiBPQHF+2uVOCOF9mGCjxmtQ4EnDlw78AE7zVKsNZIlP0ZpSvhOHjpAp7pn9f6Z72tLU2ZEbfJ77VK9JAhsuVb/f99aqRlYZCzWWJL7m3Y2DN4bdeQ6z2dps9o4fBhbYJRyMAbAzdtNYHzYlN/JFsXUg48l4pWr9C1ql+7QzBz0hNL2tZd6/UyFhhf8ynYqPZeAR30kqmYCls2gtJMWeCAPdWmrAoTULxzBeutrSR4Lom+hqXbxftg9sxfpaY/zrxQbpMsQl4hrHh06LF8vMXHmYV8a8uIBu1geMUKWqMMJsuKM+9AY9rJlXsffO3sTn0nv+CmKp5xy9p0w8k9w7ZMhuSDqlT0pr7J63Qd4jOh2kujDLCWeAGqlPHgFRR3rNcACfgZyriV0x/zG+aHsU0vP1Si5u1DvcSB90/MxDEIcXOcLfeOyYa3oEYPEqfzceC1wHJNGGQzA94aBNnUfHBQlTDgIfd6d4vXWedHlHiMut5SfP3s2bOAJsmJO1eyAM9CIxOwzRVWDqn3cunqxuf6kci2RBTm9u9u7mdmjOFoo0G3qtMk5rp5eJhoXntyFmLNP2i35bZfsoWOX2nU2R+ib4Z3xIcyfva5OQKjCUHOHNldT5RYIIj6qKUCItsxrIfKQ2fQCKD3Dkjv6yuTIO9WLmS6ODAZX2VQmteLSzMqpw7GBxWNnMvC7a42x/rhCdvxNnqjpYDKbzMwib+galDlxYUJvmhzIrmg2accp261ra1FhhUXAMC9ryVjMuk/0o3yA+dJn5ySlt79B39GrVSkrSo2Qxw0iq84ReFD3Y21sS5p9rL4kqjQbWEb1C+UG1uTdQ9o6lCGs+YVzPwf/B6HY3kz49cXT/ZZaxd3psr/nm8PPf56soJ5q8CvIoFwJ4OjiFyXe5ZX2hSXlg/CGVINr9QXtn65ofyV9tL/4Mg+mqJzefu7AjrT+uweMzHVt1zsjgnukzby60M2POQjAdJn/0REMo0wln70ZpYs0bU7+frw5eG01QkMBORwArGzi1dMLrEwshDJcFgLV74F+nYM9FcnAxQ/eMKZH3hArcxYTHWtqBd/eZWhxJYmSbd9QWezigf7Tp1TjcLLlOSQzXFgSsyftg53lZxae7ZcKZ+IumrAa4G1eB5iSggc7KXBNXLmKwSK61hxFmoBusuA6Mt/65spiSZ6NkChvVxnd6NEEVT8+Ipz2AYWNklO2iiNDvCvtiVBZQxxv1RkPuH++gLVBstPaHin023DLJjKGexRrRNMDfUF0n0i/s2QyOq6bUNilSHtu8lbibhYSzNwZSD6YrQ08VvrSE9FScVFuiTn6NQnGHl4hNbGEV5zw/aaWJBNOw+g4HEi1YlSfJZ87FhPbXDZVyIRq9GmhWFZW1PfR6R5kGlpOhN/C5Mg+9rAjIAXJ1bihZv/wBnZ8GV5RHbVseDDaXF5QDXuEccO5XSbdi171HQy/xmpkvJCAsF6Us4CRVtKldh+RFntGAVqDRd6J79AjzwJ5axkJmq2ApK+0Zh4AdL1zYpGQBqaYVAipd64w8eHGnw3UKxF5xVG87hNy7M+COmjtVOUBFMMnqdF28Di8gnxZsntHfOklQQCTMTU18fetr8wUFBxXYhpdmmM8Ojoqet1MoNsNfXn6TEQZO7ysrKUI9Aulxs2nipV09rP+dZ0gVHnZHWsDJFsH2V2uFZZwBdX6MCDdRwXa5OkOiOg69QtNX0z0+U/4etc46zm4uy2QdUo8cCBcfn9HJ1Seq9xbKjb/r2jvv6Zq9C6Ozfo6BvO+IWa+p82z9QAO2BscqGSpW3rc5BMlvoFQKTrH2OHC3a/xJL4dsqd1yQU71JiBussalisBKzBJapjo71aLLufO8IP1/2n3l1SmFQ8EybOaiJEzNAsBsTZJ4uEzd25pQY3+Tw+6MgEz6PQAlAAGZrGMtmvP5ODUNBFu7uaPp4USFEmnk1GmGjEGWNrQlvleQMY7PE0O0UtZ4/V88eSr0vKUhisbpHGdMLBGwsOwrxs85JnewfpnKr2bwid8ludeZWZRqywLReaEJn82UJckirhCi2J2y8ajFJlkegVFIhA5563/PxoSCC8/m7Qwxk0d8FtDbaJ62Xgx/dKezfd4HwXNVcnj0M+VipxgKu8lH9CqqHYuwXiO4aRFKSO0TxdIiqHd5KQH9KL5aFcCOVzvQIkQXBtaKqNfBf2Tc6fZ92aNbX0zN3ucLIY5k9inFrQBYQJg268FKIWMxvCtevw4FgdKUW9o9dCr0Jdj+VLUlHZpi45h8T3UjEPJiXwLqxo61ItuZqzG9RGKcAtUIjX7cPxBMdSSxRvxjrkfXxF3NgKb/Vw3+sY1R0URruAwzctEq0VrIss4rO7rCxFDSQIQd0WirxOKZr7pSAM5ONflsOuynbXX/KiQzvupouC0tzKub/IYQHHtu2wInmKAkCwhtFRhzGdnqgw7j0RNBQjMX9JzSu2mN1auJmjkn12OlVp7PVKOznhqSsSKwsPNP4O8XFcfrWW6QNimUYS0HqIteIgQdgQu+DEc75k9KBr5tuss/StMnyO+RGsCCi0BWhCQ8b4uqaCjJNE0A4QHTCtbwwQj4MlmCnjcvO2PYwLtnXahv3Kl85RMcNKpnni9r71KYc0ArHmlshRYnN6bC9cjAkeAYXiJj9pEzj9Ah6bSARIhMmq3Bmr2hrUgs8NpadGYz5httrl6182bq8DFnDdu3gHWd8oSgqKwsm4Djz5Nsjmgk49IJblmuQTIM9eRkxVhLdRqYsmmx1PLyPbiJ99/yyIx3t2cRRU3zTZ/HoUpQRtP6di0ieF9ospPPEVpSgL27oaFYmagAq3KbHGX7yqMQiy3wb9L0xp7uBsn7FvMJkV+BRfYuf7N1JoIr8h8JzUmBhKRlP7rEdLnkZsVEBBX5VifowoESBWssYOI9qH5TWOLEZGthUGj8C+hbX1Z/sJAb9UiOqUAa1AjZCLnXmgyxXrt3M2HVDlJXoe9l3I9FRQ6gduXDL7T4+qi+5JuQnyqGfwxuysYy8lDhdOhqAqQibBIsbCjI1CI+bnIyYxJfxUul0vF5nZTmY/dCPGHORJAJFO5sPB0sishNu4XyxQOUsJxOpry0eTu4j/3zlPfd5FyCc9eatWM3mZj+BRRUr2UiRJndXniwGo/ZiRVdF+J9BfjJRVZ260dLLnPspJi6y82Ry0SYVmzSxJRuGiO6pyOf0FOMfPRFHv/SiUdNuqeAOVHashk/woLZlSlURTEDN4bG/79exIg46+5JOEsooXGlT2kMqJPwg1i+WweUuyn7ZgQrR+ONFR3mp+Chuo/PXKMgsYm5KUrgfyXu9D8hcVyYgBuWvfQXzWkDLADZDIwcIcGIhTjBhn/kY0QmxS4TfJ42mfTwEocfnmJoSU67O5kUlAWkF1UJ6oDfSHcvbmlBVHaOy3cU8u8NuDP3ARwamyI1uGM+kENnrwRR2RXhF08OQIvBUWuzQpNMHLV5sT5YgCD4mYWWrWEyPxViFgVHlDkRwpCuSoflEm27exoXNbuSlyU5aBFWQTJovWBYIVgt7xbi1jE7l42JyzC4iKFbLFCPh4gpocaqVjbHxT32Jt8U6H23ACJziXZsGRWuMYLwggkTZIrtvG75UxXK22dJvzKhCEW1v+qGIcc1WZzjYPDxS9hn2r/s1o9s7SNesc1W7PZFwJyYr+WymnU9ZycLu/pE0xy5aDxNIHd5rF/MIwGydJZ4ejW7hdblUNWkxBlwqtvsCTP3V8K9fNgcPVNTAL/szyJKs8JFqziJmDdfNfilqsXTbBK4kwjvSC12pWGXlDQ2/NcK/OfP3FWF8dl1uXzxEXsXy2ZaSvhsZEM+6VavC7en8/AzfkZQPIxEqDxtQ3TFANUJFf8uO96hjNmMhEOHjAvchbosNfEBoUY659zaapv/RKS8zY3iU8T+18ITeqACs6wqxXbBwSRPO1aaFnggA5QXwOY1A2aWof/UjKwgGU9tFh/g99VI9e4JCw+BtW50XfMxJgeOYYEco9SyzDRVfecKxyHUv8yTY7xtVGvwNKcmWSCUWphnKhkgytlC2sjEmG6KtTqjOCby8ElAwGFE5v7UAcactqxcx2aCbgbq6bBoR6Bee4OpGwG8emeCfe7rD6qR76lojGP5eoqu12hYTuByKmV0Ol9YhXTG3WuZhE22YjqqnuwBi0UkH+VB0zK/xySpR4yMWGGgeK9KtgA+iVU38mHW1YjPJCMjdKm3904Q/Au1Dz9CnSZtwLF0zrwbbsVUxkR0sswxVyzlzxJJ9ectjnH8gYnaO4R05sdqXBbtUxPFWEutgPGZ9FTQSuDrYAEIVmO6g08EaDqlAK2GsdGxlP4MutSCbHjAq+ZzPTBmZUJ6vyPGhjDjJWaT4hSpsu3lsyY59UNkVhm2u0Ymb3W0EVt5AfnPCZ1GSVxCuR8oT9+/nbb3X+HIYqBsDp+GgwbUxBQThkYTN1nZ1kyo2wsmQmbKWcdZiX1KuLuq/wrvj+6KgT7mWYb+/in8hEynveb96uAka4Hydkau9tMAXyAM0UScFFiqP5mTiwbLnXve+PG4PBDA9qDUg0NYlD0/CNV+NbWuQ3HByN5nGjyreD+d++lh5XK+cSBYz7jvHQtDh+QRWwUk2ufiLumFBkrUZrsNO8qQUrLlxPFRkc7F7c/nmzSj87jAQCa73w5uj8Eptmo7eUfuiHyfsO0O8vGyNVx797dQJF8051DPHxbzuHbEuUHn+ZGFPGMyfUmF99CC/hRWoZoJpbNJNdZhhjflY0e/HzM+VtJd2iUHEp66mpRJn6Do/4zDDG4VdcayXtqlRrDIfL0x7wpooy3QxQM1D7uGpguzdKDO0Wt5zJ0zfyX5F0g7GsKM+TDWIHomvVpN5jBviOgBfWAKnfK7k7lPWHuxvcwypJtRzXqtfv1TAQ4jRHs0WN/F/BTcfdSTctMrWSEfv1tLchd7mjX3OUnb+53njFaCGaJCikoaaxS+u8wd4eeCB8bxcMB1ll8ta2SfL2DLhXEUgDmyKl/N9FOIhbqa1t5eOYkfLYJgcCtyEQ9caQ7TGLAwBgN31KCjxBYZ2nWwrTK+5+iMJ+fYJXyTNqrLwpn6IfB36E28oP/a4y2gMqR7khyrxSyNdsr1r5HPdb+esiowCCuSkJ+7xYbBE91mzs2MpZERC1aQ2vZwRpi31f8z3XSsH/MfR1bF/kalqfVvC96ROwdGDcjDmBE9wAfNmIcks0dOUcl0TfNviyZq1gK4wfbO7E5iTKFgUIq1vMa5veqhxTmAnZs1U/ofuM9Hgdqv4GLKCTx89a5KbBqrR5b+o1NdpA7olSqY2w4xVd5BoU4CM/FY4bg21QeUzfWELmArmjjwlr6kUJydD3tFqtxfawhJAYPTfuz8OGDyKDqsh+Xn4fl0fzAaKfK7K2TfS71chmH7VGariwWGeg3UmUTbLbNjSAwx/DsO6dJ6Hq489fkRCYp+Xuyuv1p8ehoPqSwVbZrx8Z2KqaR8VN+Ec5vnIVlcpWR+OMWTOGHFtCs3jgcRIjOY2C9EmD0jswFQe1gRTawI27Wknart0Rc6kSVwR34a1h2XbKCuRzkLsWGzr1R0Xa2a4vezRVpKHZakzQftdSAEb07yncoV5Hx0fFOarzHtd1QZuUp9PDWR5mG/DlZhYzJXCaDp86NayLt1Ua2QupbSlrGt2Fv/VXC6YxuW1Rm6rVIYuGjqa/930UpX7UzAUKDXjwdK6wS+M+d91w9sdMcaeBI6BGx6DRZk/sGNaZ4sC+N/2t7fjN+bQh0IQ+z5SaYwJDuDiLVx7rIQj/whC+8xh2lSTfjqAGHMasHB6wV47OYhOM3uZAs8j8CdPQ9/A+Y0u6NyS5PinGw0Hn2SGBfcb+XkbayVRaI3njM8oYOuSxoXXhDsKbwh9v5w/etPtgwhirEu7vimU30/5RadzT8IhI6lJST90+tF6mu8J0vpxKtD7x0HZYmkKK5CxkxqHp2DrxNV7hvtFrM5o/NzX6ue37JHidQ7Zgnw/wIqXi9bKojY18jG/lSIXwsppuYS2mrULQkfVqQ0hDNXBk8nosyaPrJxOx8cbaZEhbp1/3sG577BUyObOvmYuF+EcK0H8KocE6JQnPpaVY2CmlOvKdbE92kyvtGPrXF2A4QmguEIh4reyJFxnwSznhk0ntOen/RloxOHVm/hvqAaxhih8iCApXrIYTffbYJ7rPUuJ1oegwJthzxdNarqmWOBiLq7b111mieOVslnVF5YNi5E9eiDDRfbNsyiReBhbRWswVuZCLnVPif9OL8EL17CY+0WHvmLPdH2GBaf0K2rbBze2lIjUPWlrRB3ICgmtbCeeJ7M9ejjSoM+I8pl2NEmpAt9y9U4hIhR9fYU5D2Pp9DeWJlPWlyw69uSbS4t99cC4K7zhfEYVDQ0A6Xa8DQ8fFTsL/eGUdSDLM/ndQFk2NSQPlm3BE/wZam1UwXddApnlkzoY6irUQ25SkO8aEg/Oh9gEYfh8oq+08roYJC7qSMuvo6iReOytaFOBGjOu8B5GJaSEbk2OkoqRQNXU3t6rePVr1ArkDp6AKc21NDa6joRt+nM1rLjpgKJ4ZR4dTWPAB7yLevr77UvZr2wYSlWEfik+NQQwrjOOtZeka1VRTAJ7JO33LS9scO/SC4VBqPRIhHu4ixuHLehSvKL8uZMrOlZQg2fEQ6sJQweQGhzx5L5bnq8uDMsaqvTeeFIFwD0BFvIOYBMVMgdrrO7poyiG22BJB8RED/55k2i7TIeaprg5r4knopkKFd4LQuKvgeFvfjSVkuqkNwSDLYozOD1S6E70L6BQYe7nUCwUjBUlBttEh7WMdVlqb7nSCTF/KpqCGyOk5Up+k5FSuEq/3pefvSrZj9muikw5DYLlyWOAHXIvvzK3VYYbj6FICCWLj7Fry1R1GBSM4EMpe/Y4ylHbusiiK8NJuY6+OwkaF1huuJKBZGvcXbvQ8ujeazr3fBmCTdn+HTvIEZ7r2D1uVRQcCUvYRloVGdtGooHJKZNQGwe9E/CYYUm5DKu+zyzssBB8HzLbJc2zBSTNbOnaYHVVXr2BGeKK4r2A/mabts4Rf2FToJDYJkFQlBigEeqY6o9g3Ak3vhBS6gbfVurKPVYjvovclrzxwjIC+IM8gkDD4Bpr/YBPV9fJX2qFvtSCqoTrcNELsQcB7x2ArpQcVQAW3CEB6f6lliUSB0Y0FlwG1haPr1qByBKgqSmaSjNWMs9LMVy5UuyiS7YGtk+h4bCIkGhXBwuAxzO4G+GlZ2zgU4x6ANLTPzmhyhm74/9Xl8Gp68DceVedTvV8Qi2qRDPbMC6zB4ALrJq6EUgL7dZNQYYI3jT/l0nhrkmnLYy9HLWlBD7WGpI2bnl4PU1Sj7P9aTR0ZBfhlz2kNZEo8R1LoHW9bT5E9HPPVZL57u1KnXmHhIXb7ZeePGOabLJnWaVpMLwm9D3bOk4oB4f1P1EaiLDP0DahbXEm7kj1J/+8How6vZqeHSxupxkXwoqWNYchTIAKS2Tb2jDt84mDk2AAw3jfDHdQPqseHBcwy9L3Xg5cNc70D8DqHKSPhXJ8IjW0fa6dQl1i0gREm+C+3dcMn+fy6B6YJtzW7k/Xq3OeD2Rk5EWwfuxG3BmfHee3jaSng9AXumj7d7JhP+dARechKCbD8sDirayalU+VVjGUKiYxZ4TScg7a+EeoyDr1RA6Abfke+JyLW4mdwLNt1bTrzjpt+WRXa9k8xykg1ag1TC1JceQuH6UguYcPq5kafzT8zchIMQ7hyQwx9zwf2MZuWeV2vBKVG6MyUkFBuIlt0K4jM6aqih816O2Ujjhdvia28p8eKrnuUaYeN53nElGQ3CkYPiAcH4ehDYZTKRirVWfV9t3OwnOwhYD6yT5tt/HQALtgRUIXJnLGidK/MHMsVw4SPiT24R0ob6vGH/l09C29k9rl22cbPUv4I55yPVreHSxqWV2SldmkZBukk7wdiSWeaJ9giq0vhOjhQfBLaKaM6xLtE7lhS0XiWz1lLv1HVZv7FxMBgulDObyaMwTmst2OVE6WyDmOUKJWYwyYvY/UjmPYFXoKiNNVt+r6PWrHTaZbkAJsLldhvxBRkh8gh45i1Kb6WYXm97QRoOe5bl9WbUWoZmmG0BI7DamYPHReRBV2nBt+tra/ibDmgMzZXBKxPac/ruUOACRwcMhutp5ZZfzxshqOiRppH2bLMCeNisHUQpngOpKfGnv2DA8VNxKZbzUdGCkGS3C6TrKpPOCE2z8fIN1bKClaOvCoOHwLLn2b2FoycAJvrcWiANYUMdZcB52Kirx8ePg305drn8LjmJDhuDUDywSmfQBkF+EPkI/6mKQNFs/MFJZH+qz2ZZr4guYkGbxpp7uJExmz0QC08bMX/ra/7W62Elso/1Ht5Jw3K3iO/D8Zqkr9JhqVT7OXgmKrb83+EFeqasyd9S3rWOIZjiP+P26s0R41vC0ACfk8DnYYf99YtuE8lUAjtQyWrD7XyzSrY2jduUVPBe6CE/ggIr9NfHNPCqlQiYY7TME6t1a0gQKlm4FxbQ/txgelRgrUx6BTdB7/YykQMTn9qfNXYCb4bomlRlXuPRJGgEq3yzUcLBp5A/JXwXWczuXxXbO2QyEyBib3ppLfyBtyrZEXBvzfO10rVltfi4v5ySzFB5FXaR64ZHp81e66ty/tdy//AIThzHHYPvxsQ84feCK48iIxCqmnC2NFMn4cfAtS6sXsxT7qLWp5zwTZ0Q2fv2zyVQJnBCN52FuaFVItCadRL9l9NDSow484K/cHh9O05Pm6//3hibsVr7AItYuKQr5Q01szQAAZE1YmCiN4tPetBrSKrXvfIZG1pAv7fXV243z36zYkvye7ZdpyrmYaJnIqD6l0gea/9nEBb6F8AdAKutrpOrsdDGVKZBz0tRlEjA2Y5r24Vd/3LyvybGHiDKQvl1e/BQ6LRHXbZi76l0lOZnlqlwaW8zTTPd8Nf2lK1MxDCSWxAKvugeRU2mhtpPMOmt/Q7lCsdn7BnXySDAYjslyps7biYeeTwnaMJwn5kwB+TPV6J0HewKJrvmWTefYjEwW49bZjU0rm2BDqM+aD9hbH8xB4v3nma9HDU3hssQYZxVma34OrSIidEeTvOHmDqgM6G0+Gb1PTzn4Fo71RtUT+aFHrnL/p7LpR3s5wH9tBiIdOtfiusHHhd8HzS9e3u7Ioe0gnV0p/YY/+BzxZHgWqYFaTmwhqVAH8wLkXJ9k1C7I9kGCaSPJqZBdHWVlOa5Gh83lBqgVYTy/+F++cQopoq9+kMnglhgfBpJJKaA7VcfUSydlIXOjL9tLYVH4TgOVUSEOXwtc5ybnPgfEuz2KUWV2QRobll9kWRF6A3l2XXBxKo/EF88dP7IOW6yX32H5zUXoABk1PqrjGMJ3jQh8lwli6h1+Mxjz3kCkvvy4mSNfzeJfpR59l1tfczomM78RS9d8unehf7/XcqJCeT0wGg/ycXtDQ1mHTBER07SvPglo4vkh0Tt2FrgiU/VbHc3EQSlK4XdqjAiZkiTCm7HpYhBdVGSi6Tg9BVSCXmlGQvI5SVM2vWYvnteUFGFF+6phHh+6ydo7TQMCesNyr56q6IfHG8Bt1oF8iwxFuMEGWU56ubY+mx3ST+dwJlu4sgpOgZmqCUUakw4AvEvnHQJiLn38xoRi8BTQyVVGNCPHznjV9GbvIzF9qI5sgks6L/eIIdXTp9muCFaFTIyDagGK9Eji9qCa0jRGGJ9CV9EEJZ9mipAJ+Y3R8+EbD4GgHnMvjVMcrgyCqRim0izJYthmTq3EHDhDqrKQY3Z2gnrdF4VqGmCKlV+FK6b02mDrwXF+WHbKUl5ezOotVib+w+duQy7b9RypKW95F9xfGjsnnrYmerJwcK8B0K8q33bL5juzWsPPHtuDYU/lrH74oTqXTed+zTWj5Q2p6IQCauynoIKyeYAphI3YpMD6mIuVuw1FYxrxJhqw7jHMjffHFnm2NL85DcCswaVy5Fuxqg+eKGGG3Woy38tPgXJN2uD6FTZicUDA9d5V4zvNbV4zLG55aknRbSNZC3uvRb5IHFOiEzG1pNh5zjECJezg6wYT/rN2oZmlzOUC72GpvhnpTXTgpHRhjaO94erhE6oom5yUY08WG7HNp01HlraCtz8SW5a9LZKFrqa7qtu2/fw/dHX6DDIXBaOEXmyK6e9BY1psjV1Qa9Lnmqy+D38iZmxvEvVrx05bsmiftmYeDHnOm/h0WguMxW/shNYZusQOLklLZ63wKwLnMJ6Rnr+oKHIH2bSI0mNaq0aKV76sLCkd9oT/OgwEpUtvONqe1RRQnzgUZZcZBE3K8z1eYnnVg2i0FsJ4CS4Jkhhv5tyK66WWhBINCxlJ/611X0fIfKmTXcEVfzeOtZ2/+3r3vsgYFWwZjAQC7ZI0aqMpEFEHM2A27VHelkZhvwiCnM3CTim8I61vT2f33B+BraVoo2me+qW6Mbdxh4MRTScoQajehj6JKZIRzYUpZOZQDFLQtnZ8NhTc532E8tp1n1ixMabYH0+oZTwKEOJUrQkUXnHpY9AYHdwsGt/PmpgPCH0J9mgUKj9ye3iHob3pe0uqLWY+oIsQxTEC4vptHi6DeRvg1R2YY/q1nA4sBkinEhuXmUBQ6H8fNw8W4fyo0XuKRcCP0V8v+QAbdkT7ZnkyIJjBCzp0ys/gDfLAPtd3tJFLaJrJONAuKgDH2YILwmIG04nDv9f0+JCkGZTsj3dGBEoP5JS+TGbZoxi1UcbectxkCoSaelkJTXxne9mLWZYA7S6M74LgNGfmnpVbqLVqSb8Fxzl5GMwzxu9f8OH7KmQlRAEMqsvYWJ9O2r+SyDG5PjbH2xum0jxxLMIgxCgR1VX5+kJr+5a+CEpTan3ZQc8Ehl0x1eJ4R/q8ZUSemIgC4q+8jvhT7/xnpUxij2LJtYANeprh2aFLq7LQVYl9iOyAk4eO03AXPAE3mz2aU7HwqLmmvHliDN1OP6JS9pSrJ6a2Ma/tXPdkCBdMQ8j6g8ekPH5MhVeel73Ft+OpSnCeoVI4pboTpPvKWucklweQBgq4QhJ4bYUZo1nPQgxe0jr+AwY3EgeDcDF34rrTnB9rULSfgZ0Yje85VUkVqJALAF4oHla0argyUtzJXGGvsXTR13J8bHED5tls8qOMrISlLbFFvdNJFVR1VelTUNILgPto7dAAs3reBO7/gqODgu+uxOsChVkJZgfcvhOpXJ/xs7tKJOs7XL+SrNue9QJSZfgWWjq5UG7EZWH207K/nv4leXeHDcwAESfDGJvvJd6VYWi+h3AyIT+4AxsmxCxdB/8su2/yY2zyPgqksS6BzScAsUKmMVvqJNRmxg8/HREW/mB6qRUAZ3yUVts/h/7BsyqB6EGRiIf6ijmHlb1NqX0ztIFTCSusWsqUx0jLAG0ozUgvhNE1x/sKASUsFI1jtRp63XbcAUJIUT9M1SDSueMc5U/0sL2+Imw/eDqRt9yWi/PlOjvpSQ0kgKRyrmaJyX8e9twNQe8og5EASmQ1jbzt4gR1PnoNCi4md3X2rWnQ6mXw7hpkcpPLrvtiDn16focyknYEIji5R5NMs7Dh6oNjXa7t0uvgGUyd6D2TXL8sTRW9h3+L8Z49QMTTG3gYlmf7xdCvkn9M5yByeUFSONw0cqYHDLVV9RcJ6yAToOXg5RMp1UhVGK37yUmm4MQxtgMsJ4SUDthiQwysX8APTZaJlir346t3bLixRA8CiJhFsup76nYivG9mkaja8fYNVa8o7BAqZF9C4WxkccS5Dw/pRGgOnFaPusCxanJvcRxChCYBa50DkLalxlggt+rSymfV5AfIXOIMJZFlUPJhaGNy1Yqlb9X4RZODw6AKzKbt3l3OveBwXjI1rQZIWBjAQlAjqHBW5ILTse3Kn/5c5HDDaxwCWiv8jcWxQt9T1yWWCTwJF6sJV4IJLLuQW1JOGl5gMnvgcCCcxLcm2RTucgY686Tlo1Q9k8wtQHH9o28ncUA7MraOBO6/j9fC3G/D45kk2aJU+TvTKHINhTi+8q+OFIheJhQen/jFMZG54xYoyQSQjoNMLtHgkwErLzUsNXpFt049I7zs8C4RLaK6dBd0k0m4TrkkCSjR41uWYb7UD+8mSjYX6ia/HyMJ48Tf4mZiJ10TFNawdImG4VsCKu2BpYCMlMPWj2od9zi/DsnVQ2mZxKWjZIT76ts5Sw1NzR6rZDdnmlUFW+Cz+t4/+XA3F9oXrxUfXsg4zn9A6MdIK0LwgOvWw4th8wbLElJ5GAlFkTxz2LuK+eZX/cNO46yD3s8iiyjgs+wLI0eDeQQ4FwJstWyNkBG6lOMuVJkJVbfzqeLiZA1wxfbzpsHYHVyuU+uF4CrRhZz6gebmR0I5GVEYHopyXw0SQNVyDs3pPl+WHlschIvLC+juWM4A0MQfQQkqOQbeZrp1rhUTcjyCfzj8Nf93KHDkLhE6+FdrB+IQydVwkDTp2Nj9HgQgA1+WG4cdl/u6MSpd/1iEdGq8VAvslHl8D61C+Yz66mu+zWIsQWa+NQWkWOM5BGGCd4AjfCCTv9q3D5WN6aI6dZbG8yhjNQpNdAx0oczrMU/WoUk7VOntSRGZmxvcu805ycLbR6UP9jEh1xKyDRtkpD77ZYhyYtjo85/K9ow+81ENYTtggHIsf0P57xkDsAedKZktN0UYToR4HGxIsMZX8OsCNWI45RkWEtgUlk4ooaLeYaqWwWjrJL0K1UQtxv8JA9v2u2fNquI0osSn460iOBc7rYuBf+Un3ag0og0kPMWYC/2xgEDrbtUv6uDSXGxggX7lBOj/cVZKLrY5iks+enY3KWwlZ2qWHI7g1Ilh7Bpt9Z09a98Df3Y9kNsdGhv5DoGoCJDRpecxXVB/NP1Bn89q6Wjh/Zf9LwgNm/WSHYV4hjDucgJppDJaklCZRku+eyCuNXFsKn7AuTzqLPODcabyBRsFMbp/c7kCYKxx1tTA9DkkDo0rfgZgjZM3CS+upezPaUu9+W60DW8auxGe+JrR1pkT9qyTHi9Kzob83eGUQFdya9IUkk48fDuPzVOUUeo3kAvPHdKfivIS5tVo3qnxfiZYL96qUK6gOPpV6R10FUww7qltvw9kdXKrnb2SRPuxcSoiIwy3MkWWxrKoqEw1PzszlFJzzxC+llrAqZyhFsKVPSDT5mPD6uhCq+vXwdksdnUAdBLNdGKlvx9KDdUdB/kkNvbOJEHMuR4v0MJxpfGd74bFxK+GYPeVCnUIc5bV+SKwkZB87NEnaZ4f0NIqj++AH0UvzD0rGL4WGujFiRiYQlhTNk6sc/oW7eXIzX9EiD0vjZiB0tb6qwNl4xFoSkozu1ubK+L/GzijpnZvtz1+aMv9/+PgQSrLANLU3oo53fRbzDcvuZ5rdagYhf5P5vDmqemGbRUjOc15hl1rFGoN+QgxA6TKsNXtKPCoh/pLorv/HoaCr3SBIWYKjdC5KKZSXj4AAU/5qY7o+Ter8AdMQi4saLGWiB2HWUe6KKr1kNkNuDWC4oLd0889wrgQBNo8VowJ+WdR0flrA9CYITISHva0DdSjzOskgSIa6+ewegeT9ybHsMyhPQaurS9BmctEjN1xasKBHwkffD1Pje8zPZx06p1j+Z8wgZ3tJkkUvLBIhjsezuO1C6eBR2x7SeOR1fzPGIbv92da0+vpNCahAvqREKkeokKnf96S6jUgDXMZc6UVgxVvG4zPSO/TIuhPNUy+7tRdplwikwZTJ3Lw0/03hax+X5PVFcoNhT9K0oW7Ueeg2lVVDfnMTFa02lXcluuQhKnJWTKUjEX0963WeoB8ipqkL2XXZbT+HWGhjGmJuRbk9I0v9NbHzFXXrOYDUgMJesocrPH5Yr+9SZMpVXEYRsDw4NU0VEU/Fw/rv78SIbcQ9/CEOI75BqEdITIslGqNCmtQV7jKYSYMQZ5lXhYYQoYoXqRSg5VI91NWr4Qr5p00bbXf0qkxm8/+8kvkz0+xQvw7cqfBaEFF+pxcfChpet0jKEbve/zdU6SHzJCBmEFQHvWwUAEC1RPnfMg/l9bLNIMWwPe9AOdVbynBe1WOggaiu3Hb/gQLZXDysn559kOdW/fso8YYY5U7jWzY2tcJJdRCZ5qWgRmsZMObxS45ABGFTykhaQekMz6BriMRFNo8O8vx5jGODQs27R9GGYPztty3vIuNEOWVU2l5NYJR2Fe5MqVCsHul9gcCdHQVxn6oQVLEfvvMbIJl1/xvZQouWN4psqpA9phFP+JIWzDD9Gi2DYi8xkAfqDcdQ7isY0uKgLA9E/2Wdr1s4YxRgC/N4JL6fAHXOSdI+TRrgfMN4O/TN644erNKu2YekRuxvbz6gE+P2lKv+OEVyDiGj9J7zVEs65WolfoRH4eH6316MlQkFWH9LE6K6Ml/vmTNu0/oWVuNGqyBKZkCdlUbbPPfmGAyu5Py/iNeQD9tY3Lu32AFQAO5kSK1QpZVrx6ZYLIpYy5FUTpqJ9eA0S9FBoCQ7+h/2B9hNa0NWoAhVWgyYc/tLy2o0ss7Ao46GN75P7J0R49dQzjC0Ym2LZH+Lj7fSJyzus9BMncRPjBF0PK0Lv4/WW1j3SnmZdW+AG2mP3CdX1y1S27EuGN0pcNMXd3OVfAcpVqnSq9Y1OcQYwiAa+92qks8HC9MW1JRQZqRa144xrFgeO0MvI+THyuqXQWUa+xq37JW3UVfWd4aZcCHscFnzSldeULtu4B2Tj0H9lCxPh3bKx/2una2NKlATef5k6X/8MMuc/G1A1IEXvIeKBLmbGQyiGujD+6zbk9pZzWt/tGhGGvrCq88PCdXhTLmuAm+0b3uDIadhNjh6tKTck+53JKagzrBj37KrC1HA+5WDZgqO0LxUYzUIGoGhTwn+b/3m9vQlMMvfqSTnfInTN2bDEickuh2fDszwsMikfEfvkTNMaNreVaKXKpaxK65jzEOoO4y/2Sw7syMFmXzo7yvwdCAj4voj0U4gu7ac10aNzOQTPLuAzL2HbwDrmoyszt65/4i/UAtFnHylzoEtusxSUGCu/+hNtueqirCryvfhfKbBbRcyI0hjepa8HESJBWI95ua8ZxhUzUxOBdBlqpPnLMrJ+uTITHs83VCR/5ddAdHU5peFKBMQ2fTsCmrBDCRNk5erZqUAIbjID/4n/ekEq6YWAnhdRSvEjXNRXwNFWE3TpskQQiPcYiRvopWuMvXZE+XM7JhxGNTnPz8/1Wg7iMLUIi2PWfyc7tJQWII00rQ+dnX3PJYrcTXi1telnVHEvVhP1A7ZYD9z9SkS0tyjO8xcJohK1AfveQeRFM5KZJgLdufbtXxUhtdsKz67+jaRPryF/6QqqvroODqsqPPa/yYrw9qtmTrr1CBgJAIXPrFGTWqnOyxZfwsQSytq4OAr0eMiUL5uv3noD7F8bAPy3aGN9NobJgaHAk7NQLr0x/apJTgpMxYq3SLZ2OtdEaFh/wC+J43hYR5EwI4nZVFg7qQiwnIQxoNuK9+AcK6eiH9ZWz0WgrRtk/St8vZ+6FSZdIBpAaQarG9yM3H0RQEPJPIQ+7lmzvrcgxjQck/ZkoXd9gd4yHmbQeMLXm1xycCVqX/c91xbSVe2RMbOlOSe77LLM6BZUq1sQtvJ8qvqAjM5BJ6BKyWqBt8I6THLxnRj+V+PFy6+lXPFe4x0QkTkPScUX39Uf+UQtTyxFAAvMvexdIKxBHwOPb2IEtHq4r7nMzSYRcBuXT77DmcqOrpDso5I4qSFnPls+zHsdErJCQWDj4yKeEqBF+hApvSih9QhXP3PgHmIyfC/38SuG51Z7N+71/COHAUjWBE/Q3na3XMrCqlbUK5JkcNt54DMGWApT1ESK6AOOVl0HMXa+w2hsRKNNZELD/lkFMS0Gq3vE6/qvbewqil7YfTVmW6jQway5SdLg39ijJ2yXexmxptOc9H+Lb68T9UVFy+uy50Jzs5HlV376Cm+b7b8PZm4mkX6DcnMcfQqVmIl/7Ltm0jJSOuR/hzcMF0Ib7Wok19Z8tjN7dddpG7amdDPiFGXL35rSHC4+2l/fPk0A60SZOmaNZ0M4/UUaj5lHqhSnmkrixmMfwzv3p4n6LqeOd7LA/Tk/DGZiZ5Agb2MJBn+ljnaPTgSvtkt0TU1gTgmNxhRm4OmI2ocUkp7sowPalpkxXK6ylz5n4fYvBylxOC2o+6rugbT8A39ug0v7IXR81T8l3yOsCp/w/d7i2RDTqWOToPkPgEB5AeiYNTGIm+VFoJYbghYEwjK42nlXYx4u1mx8BniJQH1yw4pRM8VhG7ZTRKvMRvsgkO8Et78LEsMZPk2EgniA844kanVMwuatkTMChd2/JU6SgeVGfegMNdq6DOiXE/ptn2h0nDFETWT1Byzw2LjvoD6A54wpbLIwNjiuKjq3wUsih7YTpED31KSuM+/LSBJRuTocKOjSJfqaAIOSiSbse6/hJ0HASOcTozhpYdnHQ5OamYEDRlsfYl/f5xSNP4x8s1wrb811A22Fp/6UXVSJfylhxL/Cb1LajWyDIRbkIDbviz62PvEycv4CVLsOblbb1j2WZI7rjt5hv6Dy+/P0PBigKF4sZtomUAyZat1bbH0Dgu0RGLbO0hiizb83Qcuk+faMIYVwCwLAIUPmZTBN7uyyxNAS6xpSimbUP4bz/pv0BEJOg3JRUwfJPxHeGG4sj0fzX5BfJQMRG5yL2/VEJxAn+pFKJlfyNFxB9ScU1oqVV3BcQMKH8IJnJaYcQ59QXNJXYgLe1ohKkRuVNIusxRa+bsTqOuIppwJaYWxaNqGDuYE5rzIxmfOirsm/529s05YxpOrWWzp/1H3i/A5gGzwsE4f2PTmk1d9MsqHwJOk/H1Z99qU93w6clgp4qzk7kHjrlOmRIvOgbBhKHaBALeAP+h4AzXGbpv+hCQKIzdUSBsM23Bp0HSmheUQ5u7kM9PKKztCpC4zh4x0Oow7PdugiInCp5A+G2GTwCq37HaXG2ZolPQdJn6+K0LJfZJ+6s58FL94Ug3x+4FDERxfEQcsqCVZkZndwG7EmqTaE2hULmiCm1whIuU7RnPa3KirsRv06Zan7h7ie6J6STwyMLXvfYTMy7hqo9pwcy4KFLv+Fvd2e1UXUetQKAnK/cLYXtXFBbwcF6wtQ8ehHIwi9e3ufMZrjOxP/4h/ag88QD7v68XX2F92UWFf9iY0tym7G+K6nntZupuNH6s++ziI2cpFq6mNblUm+FKVoMwCpswYJZccrSXHZSgL+DwS3ujbZdNLCgaoP1pQK7+Z2INt6qLWl5qi/HAgDawOUM/6KyesAyTqmo+f0wHJTSu8q8XJsQmNXjzdgdxm8yqeAFlXAgDBMWcS4j7ylIhLa+Ejh5wzsLClvmGjYpxGi2RCPHAOm3I1bCW/s4I3+rQrg6WfJYRGNWyBIQKuoq7cNes5pTBI0XJxGYe55he9gQk16JKWF4nmIVmRLeGfzvmh1IfEGO7tUiiCZC8oeF98DcFO3Cvf3w2o3T2BFDzr0FGLBPplAiiZny/4f7t22ih07U0D45kJZu4d2cPtgLk0Wax4QFT0oSp7bk0az2y9IOpN0p08i03DbHgZ9Oejz4w6GvVjFIwzQ0jO3zL+NOAFCrG+xjlqSoEdzj+cS0PvIdLhhSNIIrz91DS7iRAFEfIPkG5Zt88Y7KRtFPvJUQqNUu7Bz0EdGI/6ZkwuJt88GWi2uVKlLRe3+awG3WC3PeyoD4cMEHZZWdWk0bKVkJmBsZ268Jg6zBNK4s4RmyyIZBh3nwrESu+AEqN2FhXEF7ppg7bWMQI9+0eF+q8mL+xN+4yuj+9SidFZ8OMgLfKymT/OL4wNSltxO+OGv6uPyasYufqTDLSdMJhy00wX0LwtUM2Ukepr5wYv6a2hrV8fDsN8vHsCteqXcMZJ2+b7NSxGzCuLBpKTxHPmLCU7hWipAlGYWxpgg1FGVW8e84j8PfdIPXO5XvGW+YXarFVNb8K3JJ3kjFaZQ7TVFJz5YEwNwT/V401qv9xd6xzco0m5jksFhpbqkCASpJBApI+/lJcXuRIf4ub+g9A8XrsPmiNEm5HEah9XqYJ4vP4kfoECKM6wT0niB4he+Fu79Zpp5LfNLBE+vQHaVultMaie/RN6DwjIMf/Tj4Pdbq05AKgkO67siDJ5N29ZpJwLey7YaxwGC0gyekw9YPhHXx0FmyliqKkpy+v9RHm7MTwZcMxpvNeC5KACQRLQHO5ymDTJ+R15D7dul5ajCo75c+mFblujMLoh2cf5QpviSKhbSzlkFrnbTXO9wk5ZaAKJtEnh6zAUQCNB2MF5k3XqWDE0AIYDyNlBQr1fbRoaPsc0EKsj/3a/CdYfipMQd8AUsMk4rujAYdtbktDARnC8OOjsM54nQTPnqbjXDhvFyZOMsnK8jFtG0EdIxNEZQEGebk2H94Agac3IWbSbNL4CKpYGM17MHVKPZ2q2gnG9Oh8dgoCaLKG44+Fd+1BGieWz96rgm2O3RqLHZMy+fyI8JF6iywct9LqnkGItQDOVLwp9dZ90bEOUq78NYuNkBXGWJwdA5ERCzj0oAOtK5pgZ0vxUqvJU+ADuJuZP/ce4bE2kiEaCy80CpdbliH5RqL94xBwYb70Ama0NrFNeZICFgGuk02WUo95cdIClsxOlLfGKbp4w46A7uhNF+JZItYkF/uPdMndI3IEGCG+7jvMd7LZKT4dOOyP+aIjoMFxEBBJswCP7VayZNjrQELSJv/4j+ZhHa9kV5jsESTTxzM6lzYl+H7GkGldBfRxpawmbCnX4utAD4Kkkj//hZ60ktnu+fnI2xWLdfssFdxLU3F/nbTHifQpwWBbOIZt4JHFAq0sBmvcoO58pvwCVvyhnHf0hA5bVtg9KJ/kzDyOJ85rpVMGfATCvLHFRk43YBQUScBXpdLEY60buHkQZ9uke0NFuRgddLLpm+b2DROyU43jFBzQ4I8hxvOKVgIQFedP9o0a1yjordGWjkl0ZTGIsVEH0LJ6+mPrDijVbIuPqZ/kbPBI910Y8/vDlQz/ERaM6bI94JtPv1COSNOsTmfnm1MWirBZeVoSCmbMXXOh/RCBUNugo+f6CQ7rT7Zb6RY5Sso/18nMPhKn4zuz0z5r8Nkm49utSPKpQZzyoQA2xaFlolW5dFqo85qnVEnsCV0PUM7tAFrIyx10DZ9m9JNxf50+StrCY+2vdmywkNZzw4NM37PwpBS3HAqejSZjtSuFdmEyc9c4WPPjWGNMdtaQWronWvcPtA5T78eelbAqIPxUh2By7B5vRDP9J0XctDxJMQbnIbS7PiCX2B1BSglMQMajuhJsidvTEO5C2C9eMcyqN9ygHBmt9gnKKpIF5TWcuWHDw3sqonyJrsWJUI71puUzA8j1aqTt6VQatSq0Zb6smH31JB62Krnhh3OVZtaBWdfviTcxAgbKn6+uv7DydcsthOn9IhbOaboLdHdTMvZWjqQabLwuZfzbDEJCCPCbXfIjzdgP22/ky0Kw7cP1do1lQqK8JTvkzkfszNfZrOhlXXyM5I2EX5cAg3QkAxYXHzvroLKDJzvhI7qOVCcGt76cSiWCElPIsx5h91E+mmbWbY9M12D65g81aJJ3vlYH0RtddT2N321iuMPuRzDkPDD2FzgPLl6OvIkSHFHRPRWTg46wqlL8/zuNM/MgLV58wIar2tFSLqiyoq9C86VtQT3E39i9VuOyeF+6MWE6Y036Tsf0HmW/Yragd1p2jGIU9lLhWQ2CB883WMtt/V8znE6zEK0M1zhp4vAgTtyplfns9QVue7JjC7Z7YUc2vYs4mbiNaqen5yIhH8O8tEBbS/AoSkYSom7ipaWekpFs8x/PjcwI9L3vhReS1ZJE/hXd6iLrgW1Wuhv769N3Jc2FNZHb4V+9GCkWpGAe8i5DHlw/EY92vieV0vIxcqMN/pxUEkYAR0ANkJwDgghS1knkKS8Yvv+khzUyFGafrwK90rKdV2NLFxmLHo64hVhSD6eJTDOrDW8h79l6pL1G2qqpmXK8Pvx4wxU23UAeUg66WUHhxPTf+pAGKKrmOOgCtv98Z/fhCnBNU2QGHAsiiQoWtiVYtu5i3tFH3dyUd/4MRn4I01/4sZRqbIdccAQ98+ySGnxt0x6g49NpdkuvPb74DiVfuyDAF6j2hulmsm2d6QZekpOtfKFI8A7hSJ4Uw+5bnV4iM7VCIWFbI1yYRtpYV+FBHJsfJl5q9NKV4RHyVG/gLgTXjrkf7LmbAqNjV9DU8FdAznDTihW2FCW9w8U3bpqs735HccaWOXJoUMuyrfwISDf8HOapc/0IIeK0Tu2on29V+3pOsmfw9RTBqkcj0DvXhRvkxslwCUGyiNvYd3wx5qKGIU2B2rgKYcoGxfTUytp04/gVTOb14rqe6/QVMD13upBaEjs7eoj//h37k+YCYlJmYBjBPt5uDszUQD0SDpFgPcvxNC3xLV6ZoOlXlri+aVGWbT1zL8yeoZZOUeDOzmod9FHtu036wVVj9cPza9knXN+UdYPk1G8Yxc2c0NoMy+KSW358V8Q42g+JVXzwLujacBPKJzIpciRkxWOsaXWSdNHPULoxkQlPJY6HMKTLMRyZUOh8s7t/7l7oKBakP6SDJjHHifk0gm2C9FfVrRHnZbHRFzxbEMpUBEfx70X/0WoX3YhIApIoSFPZY/NQbl28zu2iTFhGi2hYTj30/uoTHuVl98cVlT6bARFOFTsBllJZd3QK8VwZmHgENDjfW0Wd70Udre+V+VI7UFSZdyb+HaEnGb1D49t5FxQGp5pji+OVUnjqmCpeRbsSgjANY9tnUpXHgATJKgvge9Aaq5JcgHAnji2cBLbOWtmTo3ImAeJIu0KR1/L58RDp7/E4eN0mG50tKFww04C38fvBqKJcm0CV5UkbYnz7+2E0nmCXAOZ2x61PuW3KBH4abiBg2ZFa9AQmV35hHyPzTQHYkyzBjjYz6ue7N44ZdX/72JVUt4E6WwDja+eMFZcADg1EDDZxy3PNCB4jYgOPQMYQ5mrzoKfSxgJ/BgpPZ8G9OR2s7RxR+nun2M22itDiGAk+nrNLpf4WQ0UehtQE1Ag6e2SPGD0rwBgCqgRBR2/cnEq8nLNqOYxkn2+gxvCdUOH+qIs7XyyYQ6TzOEZbuKgC4TEXoh9c0AnCqPTpdyzisNOLGJ7N/Z54cUbLO4Yq0sDkzZ+VaEuo9I3SBHcLx55r+Fn8w6vn8NyIEBPGTfIykIWdLhlu/tPnjZ0pnLDlKEfCofa+sPLJ2EhANX2H5GmV55DGKGPTk+sYZR8PvGvlg4LnpzLGysAyprDVtezUgYlbcV1LwQqB+gbVFm6U0haNgF7QGk82X657NkIkRkmLaPgu35I472ZOnzk3vaKw6LH9TGyhnHcWwfRf3lEZrSigI+btGshzG3cpNSaNgcc77F24X22R0YNRdPWQ4UnDmIAmxoTITractMq+pnm0SXoYHRqlG7ueUimjvWuTMFpguVMEdNWXI1IJqvJXPvWW+orbaG8JWYu9fDn2Guf7/rfJ0dfwqX8xZoVwVBUAedm2rtiMtvCM/PXPYezx+gTCg8nhHQEMmMxm3k3kI1MourXbi6gr9iTOaLnWYwyIPTGOujB0L2d08icYURgy/4KEGI9/3Nb7uNiovWuZgONVaB1D5TDhgEQr+I1SZPGwmAdFv0q7pkVvwP0ELmALeEe4iYd0ywPKvjWaG6RlkBIHT4xoVe5jv+Sk5RD3PQVWqqTMuzdpUX7cn/xVFuLX71fYq+nN5M/nusSuOCNSpWEvPE2CSSFzUXW6QwqdCdA/dlaodYUDGvMF81b0xkvDJgd/i5Y6AgvSyWT9F07fcNHkNFmp3lB3qqo8URyrtN/ekUCjRqzDvKbnanYhRKTwICP7ERqHH1kJlNGliFkl7ffj1AlK5XmfCfAFJqB9mc+8V5cBkx/0F0ptb2Wrc9Byh0o9PKygDoUzdT7KOMvMrzT/+Qqe9kDQ3zRENWR48uyPk7XA/LYnVTsR7uS6zK3UrSL/Cgipws1HhLuCuCd8gtgBnd1AIAhHxB6u5eeqm3sUVx1RWjNCWIug2aSTSQ6FJJ6495JPIt5EOLax/BPzZm2k82LDtMMTmZ5Mf1X/DrtGtNgYln/LXd7qCgRu3nhsRchFInhTQ6VaBXFOkIYZwNWAQlh4qmBWjZKoIYbzw7zCt0tV8xVLWDnASbHETAKE5l1h4ygvx8ZaTc9yLvEcBu5YDkiYEXW0CmFrK+DPJntu2Pp9DGNl937MEdo+he63XtvNVGEkpiiDONT5BXSbVOYb5lM+6/GBGHTZMI9wK8bkAIj7PHaxG6/XrN9EwmuDcSj4NmkBq8oJLZtUZa1mIoDpu73LqM8R13/6tK/YuDCeuVFQeta2HXeKDVsK9dxjnQ6gHtPT4SK2GAwngW8S+pP+2V3v5HYe8Wcv4SC2ZHIVa+MEwKzyLWn8rX1eayMFX/I2puwsqilBhWbKAs0k98UAvZdKfLEdu+9dJqVK4qvmkQwcOvixS4juSTmok+V6zgsy5jGhsyzziE0QXGp6XxDBWCbVLEpHcmlLvJBm5HPiSVbs9NU/8jHD3SrPv/hNNhZmfZipmOU4/wXD8Paz85GnWFuwFdVjKcYxcx3b0L/BPc0X+dtLttUn2jng4r44WRdXCktqOVyQXn28SlXVZkD+S2qL+F0NULX+mYd2oAS8ugYrFKlfeuhxXCQH+m0z2YhmF7/ZeKWgCf7Z43Vk1zSDpv1WZgy/q0HPNYfv9gmuXFSxY3k9k1Ps448QBVk2UOnsCulhRV1MOAuTLvJEIUapyT7O+Wj8oPUm8IWBrts2yq4NWKQJRhg50M95TeRTn6rw9F+avfB634kIP2ZG4le4WjTR+MiiKwQkpTcw0fwQLbfLa9eOoXs61PfyFChmT+T1wVkyTZ464v/RECuJwu8Ntjqx3Vr3uy7UFqj14xBQvmnwQd23/c3U0KcExs2YW2gD+rgUeDnnMAKcD3WP2rgtDkKzgAmeiX5CML8/eyD2B0rDKdNaD1nE3hO8sPkmipjFjILBFzsoHypeXa6a40avrqV7FxA32EqAHZkkUAOFokoQFN+hU1D67v8eBP2ijoRQ/q9gn7co/HPmNRG0SwxD0mOK6QM2g6Yps0NU03gla9Z7YtrK0Hcgmk30Rv/zXFVJH6+LEQaJjDF3bcyTfIgOLFXQuhCrOn1e3X91T+5PpNlSN3amaHy73gbfFgLcuPBl+8o4SJAtwyTiSnlioREGbi1HGYWJSyv/MUBb59qNBMrhpfSDOLf2aJ60IhTSWGbTKl+kflbf6zs9rmAoJMnuOjLrO4QYPoW1/+Jh1veGtfTX1z7cSl5b9eNN6i7bbT5s7lVLAXF2mfvqbH+Yeb6J13CWhEAFJ7jZVFPAjn3AXl9V0CVkDz8Hd5ZGXSAvP3LhzJtmD1B/4u2UNuCLD1s3o8SHQx6EL+Af9TEx3uoSqs/V259Ey5HFLVmc52Da8cY72VEIyFzES57FsOqspRYqFHtat7hVHuOId6I/GOjfzRSg9xEgqkCzBNHc22DGMZZCZHXbioQdW3rwU3tffdAB3BT62wOqkcTqtK9pMpoIrl5x4IPVwfo/lNvKfhseDddzv4aC3dP4pzqBnUqbSniS9VRKON6VsnI/vVEHNYhlNKpdKXDAbOEl99yccmXSp8aaqU6ubwTlQXn2q3+irHjuZLl7U4Tlp1k5PISko4DLgT4OLBctayDxo4QpQh/e7bvKa46K0SGoBhcODsVAWbRm/9d7NwYqjDH1ik8YplDxIHMVx/U4fH+K82DupGkqJLJ9fekibIVVF0bfzogVWElJMfrsuHvjtZvdWjMp0GgTyUgOV/YJ2oLVZ1ZHpZ7mz1Z3NUB9/kw14HKcZ2eqKyeZAy+lKtFQ4YDxQlYTk+q/ci1I856tr2jEOFOu1t1j7a6XRxDkiazKcHWIGJNnvDeFeaMpWfpqbOn6wZUwFtstVP3BC/7X9YkTHD851Ht/jp7qrqnzxhn71xMkwcs4OZ470iaSfWzStlXbdc50CNyGiMjUQT5mIxNb5Px+jqyNtJERtPGz072SMmCBa3QLK4Roms0Pc3v0xk1ksa1UBM0NZNqH0O06MuzWIXZ8HmruvayQzTKrwGt3Hr9bfPDQhznxo1JherlyNnl9RHsLxh1ZiqwUftWgxQUPasACispFv8KpQvN897KqkPbiaJDqkLMAcA/pG7Ja/XKPNgRXq5A+heYq4mvsLV2njnCo23MCdbGsY3UjlPGi499NGPKs0mfTjXpIthxLASuo9RlI8XbzscZD3HZOAzRflixGcypv6DzKWJueBEHNwiJxCjkcZd7K5BJFx+wrBsKqgcOjGg1/xoMJPCJwi6hy85fqQbu3cTscSUZIkMBKDxkozn3BWqXlvqV1fy7bYegeQYwvpLlWgUEiTQDiPKScVhUWgh6/OMD8J2lo3hmAsUAYIeCZPJa3cU2Iqti8Zb3W/YZuO/jurKx8rdABdW/gygIRA5j7EaxALYE8W9xKMkJa0S84APCV6vWe4rxLoUkBkoTRVWa0/w2awj3BEziZ+ZLB/c02YfH+YAZa/u2GJAvAy28iW8xJZWApxnaqOOjm/aFRXX8ekuHUP+v/Isw+TGOtGflRpjpmmvk+8wTHu31+blzUsCf5MvCKFaY0kve7ts57D2zGl1fumvw17fS6AEleITZ8DRoP3I4KlyqUPcR34RELcPN+Tsi7D+o3TLQK41lsL7IBNrCpGyYMiq881Hc2xWwtLYdo57svDD/COruPE8AvXZKqY3w2uBn1RyrLxepBVfQL1qQ2XCwa9W7/EtDaAkDrUH0FpfFn+ovCBQTo8meyCeVGf8KnvW3VDFmaitnAg41GlOE0hpg1US/V+y4i7xCdBZtZ3i6MGCdFcFw68Sqr5bY8ERJxLSaGCuNU78cWCa83iJh5C/X9BPzSguTa11AfKIs5FJNqODiJ6jAi19kYbASb2ltmKcwNfOstGE8ywlZ/02eNOFibv+UnyJ2kK4RWWddK9M5LdPUYmNNES/wPUPPcXu4B+8kdfcdSsM5lxoddOLBjng4f/4I3+nNFt3EGCWdgQnIBvf88FM5djXMBbMy0Z3fQrY7FLC20GHHV8lxF8hbq9y7Lbjm1YS7FoXZcdAc6OFO5+2BgE2Vt5BW2kOF7QyWSO//0W5vp1TAo3A+HwW/j1XtMjK8u3RUcBaFI2bvLhkP5eNNnlaT4moCpt8X6KfFGPE7WCsKf5c1FSe9il8IM6HtWh8HKLi6U8i6Kv326L4rykp+OKP7bXttQSNKX/dT1lFGNc9LupWmSL5S7jYr7gKUyKUFaImqPlEyxaSHaNc75BI44hycUPWMpeXewDwtFsyTj1Qg32cBa8Lxo7TNCxYa8DXgfocSJ9aszjqnHJvtngAABNXP/gMGmbplG7XWMcaQLwxAQt9a1Raqvx+8NyuEUYm2n+gNFTGCNRpluN8ScOyX1C0isI2Go5J38tSiNHGfuGtx43x6QlBgUfNQGjERSDRD8SLVuqlevA9V3XcBcdspFMEqKlvQ2R5F6FkV+26n2e8MeXepAtyUw4VdjCbI7HbAOrNWuwO7W7Y8yAKd//3bomRkMFnFI/y6NYu0Tem33VxPA/rLJ9aLkq2cD5xnFtNjkRt9ZWp1DKl10CE+Ib3VPLSWLX/Y/8HogI4dv9Y9cYRyTZQFLVrx3AB133/BXxhAdnS6/GkJHJkEULGIQXZaECzsaVz+vAsIy73KnlzJM4/o35tZaxUJgH+uzLUjoNVzHuzHLD/vbN1Gc7Z296ZrAi9PM8Ww3zP1DWQXRt52ukztjTO21+KEqwc8MNQUC20jaUu2Wgwy5UiKdbpqLnE1IKz5ZfNDk+wWzP+JCMOlxRb5+MnbSC+K0WskSzdgquVzvYFdVnVFynnuOhG7W21r+aGBPyo3Uc9m/qc/R8eD5P8xNLlOjipyKo8P0xKkEnkICEMd6Y/on0FPKddee4YzLsE8IMgzLi4lyIGKfyK7ojhTM2zR+0KOh2sOb3OrMHztMLzRVgsgx6synilbtRK+sZrYFDlfpBX4lLHtUvfl1hU9lGzIMzcS8CPpl3oDIt8K2fOmRxSvf7CJXHajuuKBiMT0/UwwQ+BrJI1RrTvtHiqh8C1EAKZg73Xh8I1JuxtahA5c0bM9H13Ak0Dol52Bn0ltS0lf7wf7vocDPbf8l+hcxGfgez1uQGOfm4B3nQUX7eb0gmWtmguTTP6TwgAceXxWHhKg5foR8g7XjQw2Wb/YROcFeyRoQ1980G48deE6kn/UPf9PyTCaSAwJ3pywIXBx2KhSqUzblrWNBbc6kcs/8ffgS79zs4wbjDi7Q3Nh4g+d+SBNrOCDKRVxOUg2rLXjD87ymD45PlwpFXGygjihxRwvNtQNbVzsoAz8nGMt3nfVxZPAUOOLayXxK+P4Xngg3C1iGh2UBrGA8Ql/m18C/h2MNZWEAWKl/VTlm+6vahJV6zZirPHH6ob4aDigMnLFpVrEoUN/bK6TK597blg2kVZcC9U48KJvBCifrEGKe/N0caks6N/ZqVmlhhmBcuHLbbID8Zdf4EXv0rRwpAdsalB0dvjv6tdgQjQwO+Ecm4KZ9EQMeWghSRiX9XGK+PCIh7w4JVcJNnLb4/+VpUhXLZN1PSOfwz5tRauIrVklJeK3oQLfnoSIXks++o1PYWmRxTmUq3sjyj3BzJtiCNVRCazhwGeczs0jI+XsoeFb2DkuJcMlQ52K6LW0GL8BoKD2GUtKUSg/lnY/5ZTv49rUrSBzFnk8fnL61MX1Tj2KXRV7YAA4ngKvI4NoFHHTwzJUy36od5IxXaVbCEkixu2im4C9J1i0QAQW/ZY+AAQ6apI+Ii2ksZ++9Wfd7Pl1D1JoEapncQVORVPEuxulsFIGiiHxDkBD3EDRngpdNAd2r3T11NU8ycNGgfC9isi12vBUobZMvoLZvmCcycOoTtY3Z6yPuFvFRcsshuvXnR86EcC6cZ3DGaMup7QxotHIsSacASIHtqpJptWbsqTyYD5rvNu1G987WrUFS5nL6dizXNPIATd9G6PK0BmnCP0FGRKdIw5BiJ90/cTauoT/wBdj1IqKtbvytsAPJ4Q+mgKd1CnHcSCnVOfRBpaF8ivnrqCx1/FAVZfX2xPOl/AriG1TPiHU8qB64GnaDmmhG+esT/kBs5Uie2BmqMG3Whx7DsZ6y+pfvw6UiKtwCzBXxNfFd4li4YhlS5nNnZeR7Qn1E7m0jw53rXtfQiuVJDnOPW38dKoxO2Ln+EwmLQxy/R74b+Q3SX1yyyGDGcSPRhd7cHPjUFgw+ohRDjqI2ZMGWOvZn80QcP1VslTSsy8Cb3KGGVkHjNr3HJkM4BCviugqaiVoOhyrixC20bwEXksoZM9JfV/AqATUTwVSmPYeYfBneSJyEO5xKCD2q8BchACsFaBi6999Ea7pcGYxuhfGC+Y2tEep9vs6g5O58D7afdeOVq7C7IjNl+0q8cXowN4EzCRZSgBrqwjjrYBA4anyJHAUofZDIp7MNnS85kjKyIyWZFj7s5UQFG/ttM2nQsxMlFcpA39323qKTbanlPwVtMRgATvgvJLobL1Dbo0ubNvPQmOxhqTttWV79Keo2D0rIIdG+0ayqihXBL7pWd5gCbRr5nKtt/7EAnKq08R9qJj1Yz18rwODERb5QT/fc0YqA3XL2C/CJu+oJxdKpTgNFPKDB29my116FZdfrBP7V6Y4SJHkIcgYnQyyKNnchYxUWgTGVZXgpJTLLmIvhOAHrnOO4FmjL+UtzMOMP8jGfxLujqAIP1c0ttChTWREgkKOYpFSYKoPqofzteY+oNwPt2+Aeh6I0D94dZGS61d7qMmcsoTFF3gsHnz1mELmfNWxtK8kEqwYWGkgW+iiBoNWePJs6NS9E8q26VUzH6EWIjqlL9lzMpQZsAn8imnrjBlXAXaNlNuIqsA13ltQQwx9DVVTg5QeivFWtbtjjPFmjrTet//jO9cMzyDNpbz1IN59LiyevmBSgrbW8Fd2ZBcSb7XYnB8e6f1Q1TnG3THkbTjZ435lPoXsdJ0Gq5jM9Xnu4WHdUypc1vK2mUF1DcAPRoyM/WzfyKdathytKVaxDubpQu4uLgb7g0RVonnOjbUQEhu7RAWRtYUx48rxJLR4Aox0q6UscQ7IaI96QJRtFg1MyhCYSEi48JzkHI9KiRHocB9wDYIGRaIAcIwlhPksH8vadH7UN7CvCE4oxBhRNYEf4H9EnlBEEDVSoj0O1qFBO9bHmBdllKM1n1CJnxr87doIjBa96SSfXLDm4aQbLBOOxu5ciNk7Pmcf546Y2DZwQGgr2ySr56IEjJLnXM3Dnfg9qyf6Cr2faWtFhcVkvfjS3O9kY6Kj3j7Popi4iL1Y3GeTbVAKHIliLw0Z2C23qbI+tTGb5E+X6acyMeh/HPmO7PE62i0uF+vn3SsoOHmeEyXje5/I+cHjAcNVwiOMqLlHHZMGsS02yxp/TT8tbv5lr9BeXHGXTYHG9N3tLPG8xYDIblXHdzcaoyNLR8M0GTS1AzTZYC66GA9VTJope6e7OY9F/Y76O5uk25E9HdAw0vcUP6i1FJZy8iIQ6EfwP5bfA9neTk+nIYk1d3ItWQWAZcpmNQ4pwKCWGW6DirbNJXssV8JkGvzHgC9dsOZj2Jz6R5YoLlBWjyBQv/s8sbg7lFzQp4M3F9lLXK9miReZ39hC2UhsGQ4kgU0wMmObJe0Pd7pNjrzG1yyQ05cGgKCphQHK1P7s53FpZl0Qz/raYkhOtoyfCZG2jOGWYcIvxDB+LGuZxqF4CXYdu7KlIFdVF31KlRUoVDIxXhVBcIsLdx3bdLvUeNIgqBVyFvyJYOyz8+g9pEwsqTCBsSWLjZvHNUMIIFvqsTM+Wmv/d07r2+o3biobQW9HZsnQOX92WkXDqnKetkbjDqWF9gSoBQVy0m63Z0JFBYsnz1BhT/aBIT3ZFiJ38agvFlKbVnE34+5Hjz/Tl9OW/PgHwka/CzUnUglJ/wA6BHDISIxgaR4dZjXjFkzDG/bFasba5GTcJGUvbGffGoGLYgwNhhw2bkiZehm9fXzpQoq1mP4Hb3rsPT+vGDkn2zR6oa+SYgTxZKswb7Uf6Cw1lzhk+txKRiEMPhemyIUTEUK5UKfhc5PmQ7pL0BOo4Ssv5LSf3Rx5tP0Fc8XzpCCvkY2tQBohSWk93EIfypAVVq+C/OjgZ9F3sCyRmGPvvXDvAdRKes2P29PnJBDku6QQ/kpBFSAcbarQu2yUDF/N8noGKpufIXe7MxPpFELkG57uxR9lQgaqSsLosPHibmcwOOqefDG7tkIkfQVSESAb/cP6cGE2PSUy6dr5XZl2H79M70nAkRySL0cx8AGMjpTTPHNo8adsMrP2GkeSso++d9kMSzjvMJ3EzUL2qXjJwF4MgLOKfa+SUamxcdNHi2QKnuIgoLsf28eheY1g3HhJGvUr3EFQVSZ0LoaK1Qx/neHTLe3bAOIcZphTXwdqD2xp8qqamc65U+EKFdp9P6B4ZO/tdKIpMo4DuHVjaxo6pHSGPVTsSEzvIzi1ND4HZ/Gj20/fgA1ZcD2z0n3gjUZLevfDCH2tcUn+2668GZ6Rth5v69ugrdd9bcPp7kQrZe94Oo39LUD1ISosrL5nEGA8hQgdREiyZPgLYPSGBehr5YfhNG/cKiP6vXAncUjpqB+1MilTTK3BqD9+fNCPngNsryn87nR4Uv0VAwduNRF1CGUoD2/WSk/s2lMjpQp62SSnbDBAxziqUQMyX5oQF7hB92kHefksMU4e1pz9RwxgFD/X7H+ZfvBlWrltOpiQ5QnfRhFMqyVntwxoyTQdqAVwHOiHKRtOy23zNPO+zHOqYNzi7GSeUE9uo9WeL+TDPdzyodESSnQzCR9U7NsypCfsw8Es5hjgg11irrYVbRCUoP5sN4QEW/j0C/E+NQ3dx/5+Sl+OwYEOhpB5sOwIZmJRAy8poxpT+mZXh2FUU7CsDV5nF+nCA3mF9/Y3XQIZrI+BxY4XT4HbDdgefsikNFiaShpC7vDZ4GIU1lL9HDrUxhhwccW6MJg9uo/UrPlOYpacGDt/AdM8FpFFMXw8yP1BjWGki6ILoTOxqnrm57Qjl6aVuh6Twz5GLo3zqUGxO/usqEfpyIM66Zy13Ath1y4fLEohnfkg2mMLtiKC/LsjeI25LyccXmE2tJ/6Ow0y+R6CIIvK8mx3DizVp17KIp6jZD64gf/6b6om3oMzeMULr/k7JtetZhueKDnLvhnxW8NmYpnvVg/FDi1X4KDEPdkvV7vWUDjxb0YBtWTopMLnehKlQWhVfHov/IRoUWvktzEarHTi+iZv0sGHj+2CuTIDj+CVp6D9X7iJLRM2zrmdabWJjiyVeDdVcMep3JbjGc6jGRNTxy+ylnaElvxkbI4sYFmbPG43VtH/Hy+hAPmBgHsEAsuQ5YL1AHzq2IJd+8sM7C/wDbVEnsMXdOHouKsVyMuysyiIj/6njioWRXAvz0WxXBYu07tN4wGxPvdd/neothBktPHrbFTJCZ6azmoc21rofzAbawFcUyNxf7QVFSFlMYDy/w5JCOBV2GWZ2m8wlRUzNJu4vEko/ePtMYLGailtt0AtKcM+TrEHlwcHI8a4uGgtrAzthQx3n7j2K3jSLvbPbDs2UpoI/PzTSE11FmMbLOHrjn+C2qpEiln4/dYrkb94HMCK9E+mA0lRUbehgqT+ZQyhk/Jkk4yw4kwWg+FX6+OKR0rZXHYH5JXmgkAROfTHw/QR1lTNLqg9EK3xRk/BKwCFKS0gnoY+NSnIgZF8aztPcV7ZosOVxuxSImJCOEqP4s2dG7dEVIcAOQvFCYGfEf5kOyEKqeYqydjDA/LCyj23JnoIRkZPli2NL8EejKN/ao7KRM70nsWVsU0ubVlCTTEfKitFQUaMU2xbOUgyqQCpcKBLyYJGR+mVxMYqascp4+39kP2XShyPsHzSr7qqwKXwbtwSiTSDI8h84uIO2Cay4IK6tsGP1CQ+iNAcQiKQYCoiWtKusf1RBU/w7YqOGKz4/t9JxDJuWTameYg7pUFGaED+AQ4NWvwTZ4PeIdQ7+sQXnWBP327uy515Z10onkwO243WAhJ+YJIK/yxm1OGW7uIvWSpexMaoSOo/OkTjkBsgP2tngFdwO6Jfb864v7JwCIX5dYxXupy7uaTVHI0kAeA1isIrGE3hDMTJtVphKoXnfeqkO06knyYCfZtMZEB9BZ5oAj4zAgy4A2U5u1SdJxvhieanJ2U1+2LeEQ90kWGDakYs2O/u5dFVBGHshVh9MMkbr3zeCINPuu1/nPwWSF69g1NNQZmmso773r5jgNWaIhCJba2lMBO2jV1U5ZJXLjjwFCD5m9mkIb7S/b5pwuChTFxqI+NjaNyQl1vxcrJHYF/+geNuhd2MfumRZMNpfVjFubdAZ/KFM/ZET0c1C3u9GLMlqqa1sTqNq0Ix2d+zzph3kXjJ+lHM78mwhGl5BXbLr5ZnC0bBIxbH3cqNs7cjCGnEQZ4vo8+oN9aZJQRa/4rhDmetVHcECxndKP8bTJxmpdNJTYbGvs2vDMYrQ1HD6YIoxBXOzMwJO8XSpEytgsXDx0Qkuu0DqIqxrJQG8MKgWWf3gVcpZtfIBvIOK/Q9kBGUMaBlYWZtvTTysB5lMRifNiqss38oq2+lL6OiYjIoUXWidN0cIobxdX1yaKN3N7t5E8YgxGfv+KSoU/gH6pu3dAe0j4FO8rqwdlNTv+Bu2/v6v9jnsmtQMgRTm+BsJGRMIgbVhMQ2Sz/hiztS26vnvEj8ZFFAC1GceeMmPnQs/hC0wy21m8ps9xRSzxilDEpGKzLwU5gZaScp+NYRsKokI9G3Jto+DZqlw5GZdig+vD2+stbTQu5xvbSxz/q7LVxvw4j8JFk3xNiDh5RnhXzuVw4kgyAW91K6Z2tIYdzwIHdMXsLXnsQzIDIHmfFfCLfyBNVhqaA5r+viWeIaHJSAbckXszNoK751C7NANsj7cv7lH4mIiwYS5Ro68qSjG966DNeOaaWCAw0fb5hMuy3GTfO2YICV+HHSqQgaXKqVgIk0MXxgK+PKmOGRSh7wZmVj41Q9Z8k+U5AiVSsvus995oZqKY88KHVAilkNiIKc2t4XDQ5nHFj1supBxAuAbKdpd68a9c1H14r+P6cVDhla5k4RKnNXcq+64dqqWUTRPbwQB6IrZ72jbSo1T4np5NfEIoYJ2atNMATlcZH84RAWeXwBB8dgrtA/j0z9vyaLChuvt4dOmXc+/UoEc81RegEjrZpbjxMxJNgAlY5cX1br4QtxcQJ88Wy1MZLQaEE/GolPcNsnEG/kwh+lMleT2jG9Rcz/ybbyp848yATG8Vq8ndGu88Jsi5isfybL1ZW1FSItoFWRAdsTIlGlNAjC7p71z+MDf4phjcvreAxmbNHpps8ocdo31eoWJe2/1M5PuAI1NiQ0KmdkV4CpiSQ2c6p37vNiODkOAymI5l//EnxAaZFjJR4zc3z9oRTq04VBsU7kXVPT48bW2khQXpWb8+sNORNRtjGARivbzcpuxJNtGpWB4Vaymor4ToEzFLWHLGzUbMnW8lce46DZQFJVLGqWGL3dhzvLQDUYZZv7kzAyGN1GM8lvHR/tPtXcciS+jMONPaUCY9hzekNTM6rMCIpocqKMkaU2mdOCFVGI48ukOHeocn9I26TvshyRZe+VwlscNATuFyHuhemuDoXdSL60L2FLmfyJm6i7UTtGKEo73EzdTAmU4yTNWxuL/yp241bN2tWw1wd+M1XgbOW4ocvZs9xi9pCOCPGgo5z7aHrkynHjhSHtIO5oDGkVylos4PHdUwc6XG//+9HC1bcVNLnOGRZWkazl/UigARgTzEmYxetbPvMibI80JFNHjjeTuKpOzoZgLxOlFBdAQwQS7y+URKFtZMLnWL9ENBMM/D6vSVhgudfOCNMRq30j9curIVzpkjv+40KuA+vF8glIqsBt1el58YDTb+JzOcZLldv5iPH/oOc4p/xbw8Lh/YnTqHebha6eOKvRE9JHUi0UUdb3jM8aP9hHyZ5pSvX95ri2A1i9f+4Mk951zXpN/uz6xzu8DlJnhRi/uLjvYZ/94Gft2E11J1SoAe9U9kwl+H6ynGGuMYfjxeAXqygADe3FbaBPDmJlxzb7DuBs6ULbFjSrlhYYdRH+o4LTL/7wbiPsvN/M1qwVQ0kve85cfNd5xwfnfR0BwI1xMGmljqBbkfOqAxDwAR5eNh4tXv1VOLtNJKwWGPVoWHgilpAqdRn9mAYfRzmw5UZLYxlMiG3UXnXcNW5ahEhz3Y/K6J719B1IsGZWIKjGDa1qrJll1OLDHfsXOWy6Zqe0DnHCeyxf/HKbyu7zGOveMIu0/StHDokM7Lyz4J83/RR+oRxDSioyEIH549ESnBOlugEhTX71gMF3Ve9MMuPQ6r8iGRbLfglsL2a+SuRUw1mdcLeXwPVAb6FQmG7RjMQoauEoeBe5Dka8XlQIi2dRcAZTyiUX424oDDNBD67sviiR8X256eHMIIP5CRP/zLsHdZO9l7MblbTp3aD5P2axnJbcOrMIEBUUhFwughD/5Y2cgx5Kxh3q/hmBxn+WTCtKQp5pz77NKsAxpBPCnD5CgOHYGxK1KjVDUoIGOaiAi1FHWCgBoMF5U0NndTqwGYkubXlyiIYW3IVqfJo4yZ4CQBAcmSF1UCtKoB1dY0vXPz8HkrsY2OsknhtS/G47XdMr7MaXDDCihzou/tkkTIiyt98ntVV5E3LynBiVRqFmlOPjuxv7yTERhxSBON1yUPPDPSMAtst1rsnetr+zadaasAugmyqOTNLAGdSwZOsl/VvbGgDgkrglliDfNNZcu79rzyTOCAEhex8F/90laIYotZrRbG/EV9VUhBvRUwkniIEPGZ1xt24JHeyadzVL6WNW4wsfQwEolSy6riqcZGJyO603al7WlanXT3/dna2yzAYQCzCd5/+AZyFkoF9WgITWxO+sj30m+MupQO5tgOQ+SgBYhO/wjm59LfnoI6+GdFV7JQ+1jAQBVRPbgqtxSfIF+bpdZUZpbbgi7GCAkLejNnFk7ecsKP1F5vrDwSoUTkIzzPSnpe1YvO422TIaWUbwaFWVtMmrlh3N0bVQwPTAeORQ1r3D2J+fOf4bW30+NDvvq0rdmnPGSaq5CaXKRsGHEPwVZNE/+oiWiCany8dMUrcZ4PlanJm/DJPLkXLO/g4FQTbpDfoj7RlfKwf6Aw0vxUFZxkal7lnchlyB65zme4PODTUj33U4RjQeTIHv9ra9GB/ILTfenESaxEDvU7t2X4Y6dLumlrOdODwp2T2/zAtUe0AmA3iJLGoQj6esyU+5CIvjTDeg9WzMTQxXdDlPzr6mwNcgyb973F4ae39lNSA7cQQqI8FAuJ75qG7SmCRpssYcjdDjzo6yt3nT3ySNHkmsD7ds/aopXyXiqjBF8cvA0KvOydnQb+Lkcx3EzSdCn/aGoHkj6qsDRAmgwlOsjdRwoAZQE+p3aYEDy6E0Z92+LFtBESWZ+IRkklBMwxlNJrvFZyv3THMmnLIssPTeQY5vfPS4h81IUumQfaAPEkfbrqc/3acuIkfE5uPSMwxJjVZfU/f9QVsu6so36ncqLkl8UjHCmFOPJkYEjby1JzIY1Ex1iIDw8z15cReWPIEk3JElwKnKD4vGQA64QJxVbfBLiwNc5l31QhBCyWE1MMtGbZhOQzfrGNhKTGnINV6ogwfs6HaJ+DkrOdh1EUyM8PpfzMTNJQGbdYOuKm/kox4FwC78ddufonR8umkVQ9/+Sa0WZq5XKnaURRCx9yi3+YEJ7LPnP12oKHI02XsCNsEU+oo7GArx1dDqN/MZBPVVlTlnrBPXA2SSHMmc/tMM/Xdx7n6usMvG3vVRsfX19Y3gWrOf/x1TxMWIs8pgrF2AW+Pv3XjncYybFeJjpuPALEdMuYgaKsQzw5WMh2CC0FlnLK6/3BJEJ2JVxow3asSShcB6vF5XIdUwBdJ3/iI0RLFLnHol+4q87q80LVsMZQRJ5FnSM6DhoiNtHAc29P7WESqGgWW6HGXyN0RjjrIAft5nQdzY5FCrtVe++MI4WvAMS+uwgMQvyo8b4zlfzNVUIhPXoDr5EapxxU+UgNNC/MYYscFJIWBHYOI8g8+Ol7e2CrN6r/sXtcmyhcKjziWRdR5hdGYzvn5UTES9FFQzJJYiq8/vjb7NEnxm7+Dwq3qOv4HpjJTOHVlskmU/KwBTGQR+pcPe5X0d7579f4g7Qx5zs601ZQK/9LgUTnOjAP5rnjFRZsm26OgH3pTX7MeTmdgOj+M57nq4aglSv4clfq58m1pZHNkp/ufzXRhU9XUbllde0UPkQyF51Jk8ifKF/D76EiGL3eF2sCEnLZ9FL0NpLMEcyIfYY0kQ1hln24bhNpUjOEiuEirRhs0xhUmaLVl416jhSfhGiDgxm96Tdm66LoZ9jWBRxN3xERGfrM1DeHwywJ96dIHeyA5NyARcjIrX8OVt3NW1Z6Ieb2z/qnU51Y40RS3WKmdvFc0o1ZOwRCJCVX+2MVV8vXws7Y/VI2iu12VkE3xzEAOGNPp8noQ6KNZboZ3IKMza6tZIm9UxhjTUFR/KOW9H0JsxdZyQd7ldUhfgrytRUa+mk36pFtoCrS8nQfxIDwDU6BhFNUDdItbV2wq3AHuifXFTuPcEVghhjhkYFg6+InlO3D+ctslPuWoUfy5BCnM6CcMj0AqCz4YaVrg22LruiCFjtsvN+ueTbSsafieyfkgEaaShFgt10uzjsSj0ZhZ9lRtIwfSLuTHOq0xPkt100/n2YEXIsE5JLgNhigNkP/H9+LBgUfCk99MBbiAyRIeIKLgS6DnRzWj8aKSqTXOfTx7quukrQjxtyDpsPd2pyqIMLMQftPRT3ccf2fbC3zTEHzNI8u90Gph0X1/nD0GCUs8Yz3oJATbcbl/ddDkB5TuT8KEt6mcCvdrIKgnuYQiuB3dFEVnP6itx1mgQzS0gXAT3I5KdQEvZHT6O9bPr8gkIhVIozs3Mq6r/ckWJHjDx83WUK07TtFzMoFp2qgxF8UWFxXFrwgdoGbghbnI3fGT1sw1XpZoQ/LX9jvFXhpCt2sLsfkGbLMnJbrayamwQMvbGjehF6XqjSVJMU6G1dD+QCgiSDKR1JsioAnzMZY7Tlm+7diP9zT+oo6ocEbYeIKK4XGjn4S+pzxPUoBucfvHGAHS85kDDKNDsI2/xFRS+d9IYk+MRxt8AnGfZ/dNgJGy0V309JZ1u0nQnaWRoSWyFE6aEzBIVdJYU3enQq9/INHPt5dvl6V0ep1SheDIbwgo8m4vUqVlj5Lu52aNwoANOAwaQGu0q0V9rwt2XUcKaqAk2Hmldb9Q+e9wZlO9amBvVHqRtRjJrMiWUmhj5WlEzCzOCHiKXVaVDjfblHFO3fe8yIqEBCNLMIZFZx/ZbEBwC4uf3k18+xSQ81ION2EV0V2hGgk/J1NW687mrdNP6B77Fnc+fCCVQnRjHMM5YhjqEPMqGQQOx9Hhg1TkZVw5HqA9oOXjTOSXgBiAeWBKAzelj448Y/KU1i/kGd3rWLvf5M7Uo9Fp11ZrNKm5UGe5oOLSa+V0+G3HCR/M9wUu6Ah7NpY6YppbkN851b7CR87jxRwPxbINkhgVU9hmumw2k1VQe0/bqJMwDAaAns6Kwv72j29UJeSPKQxSBraPgI+YauPSQkANuCb2xywBBwfdkcVd3Y44NOkckpJ2HOvmx5xgz68Sx0vEsZuWsCwJcAM/YofVPLa7YVmIrtCOZCII890ZmmRj4aJkU7E70m6Qw0CqG1vDO7vLR2D7ig5n9W91fPSeLkFCf6JGASy1Ms5wvoJJFzF7f5sDItJbHm7PDbQWguOEsgsx/hfg2RuULQjD8zse77+P+QpymfLlm2a6Y9b3OgjRSnfLtH59lSeZMPvkoOvArXG1kf28wLC7Rn3/cDtx0rqgzH2JXDO7DUVvRDr3PNGb+mG3skN8UALv98sFzeDNBlWClEQnnN8k6+Xgff3H20DDxNtH8ZAzBe7WeRCafqWqB4y2cPbIQk2VYXLs2aMvRrFf0zh0+e09ub6rSORXsS/sW1gERAgzkfsJ1qGlADrW1G3nrLEDHCvHxGlGuWOu4EATRgMmLLzbdbJCD/Zm0orLl0mAXl/lL12AO2fZEFnOO3QevJYrv0ZvZyGLKM+dVQRYgSbpJ7+iUE5Sh8M02ZRiCEltkZZiJK2xdaX9sYixGHjdJW+SgWH9GOZX/YoHJP0bfVphZC51agx8lJacYKbuwhFOvh5xtAqpqpxp1Gwpp/Xr6ndvdvC8GOKoLlBJm60WoI/8HD3hCLvORvdZDAdg7Wi0ragOdF1H3eOckdn0zxcg5uW/rZuQqPB87a6kt7qB7V2L6sZfeUL7F5Jg3fE8BCbo2uaum4z3qlF+A8PAfPhRjaj0UgU4EGXRvqeSK/ZG2DA3BoW9RUMZvYmmnGG5ruj3LHYJ9jUG/l8hw7a11WE8L6hS4XjvqqBfxgsUc12I86EghqK5YLGgr5d5w8esDhnAfV9n0XcH4T8Dc89fkDHnK+MbW1T9FySc/VBfHVT+M33O7GXMT1mJlTkFXppJgbARMLVCO53iRnvKKI76OZL3JplWWYCXsqDs4yez+to1VOZSXBdiWOR+2VigK7XR9s7SfTTZpd4VJATRQ+hzQ9WyHXCvdM9BPRf0c/I0Vg/5xBb2riR7rb95dh27qqEDKfzcmR61LGhHWRz8ecOtSJcrysDEkgfslfnVVBW0OPMYF7+vvgoT83v0FeA5m9fyEavzsFArD3OS6vJDRKAI6zsywMGW8jf+T0h+jGWFb7CoQMpG12iB3iggKmXkc+nhTPb8OHGCKbwyIqQzw22oktl3OoqcABXGfjmjXdXJt7OQ3kjZom2gkfa7Ti4f1N1aPyuH8WG9tBOvi5TqGlbvv0oALuadrxTi3MY3UHhHMur/RDcDBDJ4Wc1Q+e7ok2Y3HTltNUCZQuHtIJKQfdfU+QPGk9WCkREL2Pb0glOfUBsZ7HIxew+JV2VdcV8XGp5S5OI4fCsYtXRm72oUI5f1Q8rlU1Y8U1/CstVkVkPC4c/tdaNRC5n/E2GxhXwvl+pAhOFX6P3XWz+osZUqb/PeEF8zH5so13UDIoRQ50vAfThuYP/DfkOOTPnxmovRREHCDXSFRmjqwQE50gCrNHiVsAuZ4VCE5SgrIYR5yxCWqH9sOcgPYsF00SnHxVGaDLdsAAZHHN3d0mmhAVfyv/k+Tmgb7W48dqvKkB39qHVuI5kQ9xPOZkcZC/70HF8NA68lrDXc21HBNrFAFaJLD41gWxnIKqNe0n+8Kxsb+9tkmWz+hhAdZSopeOnqd92kD09VSPp+ZmjZX4FslH8jZgH2lAGDQiry90CChBkqODiEX6d22pveDwt3wy80uawopK32okV5LAcnd9simlFLRKGZ4f4ZSxNG738KZIjx4P06eBGmHyBcdr3mepSzA9kcVyGeK0z7gcvv1dw5kZazVenIaB9KY7TRIJ9p6mO+eb4Bfe8QvtfzSad9gxIPRQ5xir82tXSw+8UpEysiIpz7C1YNZXefel8/LDxatg0s0VcTGev+ITD21VyCxtxpkLL/M52meqAutT7krI8J87vUaKNelM7GtrbiQpn2ZcOC7LqUKWNr1Y3mlNEFa9/yJCEcAOcCiNCyAyk1PAga3g5KHV+Grlkb7Lpy+bxDoN4XBSdYIvBATqTb5KZQXVcTaiYzSQytjrGcxrLeSWqF6dabRiSd5AWtCLuPunvMXHKPuGtU63TizNIxaTDH2mQrOAh0dX9J3m0EUHot/udcys+qjH/iOkn1I64sSmm+nwV25w6jlx555N7ubTCxr6tRmpKlZVvaEqKGwNl77J3SRBI1egWB03LOIX+VEfof5PRJu61m100r/OLNLYqRfHJ08Nq4jaDo1dENOegF9pGuhLjhwYAMHofaOUghXot3dsyYRzYtXUjCgZrS93nd+JEe0YSADuUV+tk4q0tMdqi24/BUQrltd7TsW+rHtXqX7psV9OCw6xfS08wtCQ8qA8im2qutGCpehXNuVo3Vr7VQfGvW0Zo8yjtH3qYE0yCLzYYaBK7OHKXcbCRp56Rercmkq+dfUj9f5SYb2JQ8R5Z0ADaerVfygIZiT/0wY39lqo2AELQb3o3/BFi2UPCeei/ifokeejZ0L6uJysqyBNRwcmv0NEjDI0YoNOtpPi59Nkfa+ZWkuKv5pf+rKbf+H9zB/LnmzaaZqhU34MWWuThaoqUxi8w0eSL4ylxng4dE1CiEesyqU6+9nl/vdO1nV0ZIbeG1STWg+k6vedpMzA10UEsa0V1+leYYIyjeiYSBNNSD4ljGqmCAvVSu9IucTCYQFSaTetRzoNBuqodrY5UeDv6E1dKdVIFbWzPhhuvGguckwX3ZwRk6nGCBdVijVfEjkmWBb0DT/MQoWjERGXeJEjG9kjbgtrfEosjsk5OV/cApdNscqXpfMTfbhO42unnOh3a+ib0kK8xkeuf+eVBLVND8+qksZyN7MW5rRppV5tDsuU3KZsd5ghab6VYxQ3ztnQYdaBRhMrzxb9hLwfX3d0JDQ1bQlLNxll8wQiuS+BAO/H9haHnoEDC4Upgi1L03pWBtYKxZC48OgT/coLxTFnvAz2BY2HWP78HLxz0JC5Yw9u+E5byBEW4OeaWiMsDh1PZgeAryNnyMtSp543ekkfUctYeBQzz3TT5S67FL64JOxt/nQfLIbhXBvIVg+Iqx4kWYBxG5POeTeerqpiIm+SxrKKYC+5CxkpoAOFFnIVLbosV8ftGgZAT61bzr336lVAKrfOi4YRmuH4DPTg4zqwy1Xr1YVLMuQVgyoBJAxbmVsusaM7WbQafP+8sfhqLFMuQOx4jiEr2nP34AvAp778sfkTmPxw4YjjczpKOV3BHX+I6Rw8iNBnVmt4Vjauyorud9REuZlQdXVJwAVlT7l2/fx2GnaajsP1aBYzFdwmwS8En52/aVBEVbuv9FuPVzx1b0hlObCzGiu2208CibO6UUXJZVXmg7Uum+AQt5/hVY/m3L09FflQH/IvU5AtvJp2yUu2ixIVXSkIPFs28qb5kJLP8PBxKB9Tf9pNMoxhKLi3Ja6D/62xtLPfI7OCHkF++CCjRMaABRVxJrFC/i951SRe0iZflsoEb5b5fc9tdGJRY4tEEudaLbUWwIDpX462caeqLzxdhW0XO8gmK2R9dM/3yWW9vsCDkDEk5JDzqdNvcI4HKVxrmZVanG70bB3v9N8vNBeKJpaCKYDIaSbUd1pgCb6wNwPhdW+O5YKlmaPpIvIW+itOt1DKj5a4gwJVu/urWkiIpTIvZw8wYQZzH7ZGoTeQiPn2TWV9w64CE+aPUrdvPZHLE3lU/YfFHPMczYes0mJgXAvl36gx9jbYBfxQ1XTO2+P0fk5mtA4hp4H1d2O1ZRcCWEu5Y755Lh4Xu1YwCYmmHWw8K2hOylZcfMr7Eb8AjNBGOO04imRmy1KTU2t/1p++z6vZGH1bTEfo4medxyWTwPZXn0YeSvWFM9ggaHITpFNLticKsL/xSBGvuTtDP9qibl9LMxOLH8gjtxMAwxx66vW21V40NdYj/oNzUa8VEq+Y2Dh8SOQvTZ2CWrp1CiRMPeSKRzAUeNtxMGQ5TYyBbrrk3/3WvjoE2FBqcbIvfZ+eX7NzzKy5xxTU69IhkeZ5F/RwPIHo7Gop2u+n3BcpJphxhwqPikxrdofRjU6OizSfdr0q4K5rpzfGxssaMo4fr9jqWGozX032r/GRP7b6OUB32XxbxpMBmdXcIkbfb0RpgyFxoClxmmwmxXEeDmeSFomEhUGPfk/t4zHOI6nw/bIpO3YZmbXKARGDzTegZkVgxv8MxIMg71TvnQY4XQ5hh8uKU5nAJRBzW376DqtUD6E9kv0Cp84lHnTpZYpI7nH86BYgu87xmE942boqiitssWgYstXTUn1gtr08CgvCgjhHjcjDUvFzxWgXabS7uozK4EUuQRrTIVaTHp6ReGJAOzbKwAkKmpHVNN/Qj6dKzHb9Fvc32mglDGrjw9yp8MVsl8g6ewALCTsrOOdbtdrq3KZXKQcbqFG4Fk8I1O+y7dzSX0P0Mc2oIIRKBT6B0v7gd0GSKnhG5mv/HnxYTQVrbtlOSAudtoXVxlu7e8XF5IBYjz4/O22kFhIUeifrMpVNO60QfXBHWoiXVcA1vMSpopJGADdd+Ae+UC+oSv2/M+xUWbyhv68h6W5MN5/3yaqwWrlEV4yqowDzzAANQx2ZG8WG7w1iKwPywThhFq3x3KPVoCBprSgoz5VUyR7TRbOpdAkdNwHSo++PUFq311U76OcmIiqtylwzdx8eDGOFkwDeFDJI+mNVAv+qsFkTmLSdNEchIdywr+nz8fW3pOLGgV2/GyddWPc8Eb5PVeidf3Bp0LkpQRivAdzZgzLFyR68DoATLC2WGHMY/GfkhmNBFoNPCN6qjpsZbXUDAx/0K5W1uzkbJCKGvsVVxi1ce+uFk/fTek/ARwoYs+o2mD7pJvadEpmSg70A9pK7zI1QPWiUtPSP59o6VgUaYNr+ZFVg98464UN81wS/sAsCTk9YnSJL/u1xJEbidN7FSjioI4j4ptKZC4Dx4Lv6/b87c9IQzwS8DaMATJNNgifEmEUQPpM/v0YCmWUtCPMMbfvtr+YvjcC1KwY/5edPqRxhvmnrAUmz+Ko7c+vOnJTXN4S+ndy1UZbf0E23A4GPLFaMDaQQmkWQbv1oGPFZbPZzJj+zqjkbHyI/CRx4MjpQ4xyhq7Gb+IlvmDJ10Hi5xKalmy6xW4L4reOB6BciG/8dH29ZFnrKPI4EI7N8BG0Wf/EOUY1fN06d535IJogdbKfyLa/tYnnw2Bj5irgsAH9gXU1jy3UOLl+UtDk4nroOUf1FqoiDUfSNLaeozvMWMerJuv+NhhR8OrH07GHa0iChhu9riGYMDybP0vlSDvpx1+BRKQr5phqxdAZfAU0cdrEkKecpXbVUOaBhYAQakRY3GGFm0GcaGltGfXSNuHjgcOvQtaHrEA27Hto/EZzKgqT1jM0fG/lOhbo8QjKztBG12yOTa0Hg/1HgELSZGZTPDYN7w1XSRx7d0QYEu799aBFyhyYrgQOXGrZcP+qv6wTm/kAfpwMyS1ZLwHo4D+AzaOUKYneJ/Z6G9XthLvPk4ptow7N8IRU7ydOl3XTb5RVt7nN+zNqJH3B8ZpiJk+0WPKcTy9Vrql5h6MOvrBgq1Jh0E52ujh8hEF/nWFfwnvMjjTyEOl+si9Ge/fQ9DC5YAohp/6WOoo4SradGM3XzhnVqztHW/jFBFNgOIaI5IAOf3YVKzaaGZhd2yZTKK5Iv8hO1dPhudIcdWrYvIwmd/RUKWrUYMCdYDLperIv9Yza3t+VtmiBPh+LrNC8cJ1V297aXbk3HKDwMiJknNTCLgw1yuaN7se2o07siRFIQoHHl74ugYus+S+gq+XQNMWtswuRBJ5XPCtwNOEcmQ8a9kj1erSHD7+uim09rv1ChQOQ6stS6WITsfznE5BXp3BLJQjCKyL3AtxZA==
        - #1:
          - type: tool-result
          - toolCallId: wY7GSJcysW9HwbNj
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 3CN694gi0IztpWRG
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: r5HZzVucH61RyHwL
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: szk6HgSjKwgL1UX5
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.