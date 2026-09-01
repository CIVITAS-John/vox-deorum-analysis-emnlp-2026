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
        - Forgiveness: 2
        - DenounceWillingness: 6
        - MinorCivCompetitiveness: 10
        - Boldness: 4
        - Rationale: Increasing competitiveness for City-States to counter Austria's diplomatic dominance in the World Congress, and slightly raising Boldness to ensure we aggressively capture Honolulu and secure our borders.
    - #1:
      - toolName: set-relationship
      - args:
        - Public: -100
        - Private: -100
        - TargetID: 0
        - Rationale: Austria is our chief competitor, leading in score, delegates, and tourism. We must treat them as an existential threat and prepare for war once our peace treaty expires in 15 turns.
    - #2:
      - toolName: set-relationship
      - args:
        - Public: 50
        - Rationale: Russia is currently at war with Austria. Fostering friendly relations keeps them focused on Austria and helps build a potential anti-Austria coalition despite ideological differences.
        - Private: 50
        - TargetID: 5
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 4
        - Private: 100
        - Rationale: Babylon is our closest ideological ally and defensive pact partner. We must maintain maximum friendship and mutual cooperation.
        - Public: 100
    - #4:
      - toolName: set-relationship
      - args:
        - Public: 50
        - TargetID: 3
        - Private: 50
        - Rationale: Korea is our long-time friend and trading partner. Although they are currently Austria's vassal, we want to maintain warm relations to preserve our trade benefits and alliances.
    - #5:
      - toolName: set-policy
      - args:
        - Rationale: Selecting Cultural Revolution next to gain a +25% Tourism boost against civilizations with less Happiness (including Austria), which is crucial to win the cultural victory race and block their influence on us.
        - Policy: Cultural Revolution
    - #6:
      - toolName: set-research
      - args:
        - Rationale: Researching Advanced Ballistics to unlock Nuclear Missiles for strategic deterrence against Austria, and to open up late-game space booster parts.
        - Technology: Advanced Ballistics
    - #7:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Culture
        - Flavors:
          - UseNuke: 95
          - Production: 90
          - GreatPeople: 100
          - Defense: 100
          - Espionage: 100
          - Mobilization: 100
          - Recon: 10
          - Offense: 50
          - Expansion: 0
          - Science: 100
          - CityDefense: 100
          - Gold: 80
          - Growth: 60
          - WaterConnection: 50
          - Naval: 50
          - AirCarrier: 90
          - Antiair: 100
          - Religion: 10
          - Wonder: 20
          - Mobile: 30
          - Air: 100
          - Airlift: 95
          - Diplomacy: 80
          - Nuke: 100
          - NavalTileImprovement: 40
          - Infrastructure: 80
          - Spaceship: 60
          - TileImprovement: 70
          - NavalRecon: 20
          - Culture: 100
          - NavalGrowth: 40
          - MilitaryTraining: 95
          - Ranged: 95
          - Happiness: 70
      - rationale: Shifting slightly towards offensive capability (Offense: 50) to quickly capture Honolulu and resolve the Polynesian war, while maintaining maximum defense and nuke readiness for Austria. Also boosting Diplomacy and Gold to compete for City-States, and Great People and Culture to maximize our Carnival bonuses and tourism output.
  - tokens:
    - inputTokens: 50906
    - reasoningTokens: 7356
    - outputTokens: 621
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Current Position**
            
            My thoughts are currently focused on evaluating my standing at turn 395 as Pedro II of Brazil. I'm analyzing our resources and considering the grand strategy of Culture, noting our score of 2243 in the Atomic era and an impending Golden Age within 20 turns.
            
            **Evaluating Policy & Victory Paths**
            
            I'm processing our extensive policy branches, noting that our next adoption is 15 turns away. Researching Radar, I'm prioritizing Advanced Ballistics next. The Culture Victory remains tight, with Austria influencing several civs, but I'm tracking our influence progress with Babylon and Austria.
            
            **Countering Austrian Influence**
            
            I'm re-evaluating the threat from Austria's Culture Victory, noting their significant tourism advantage. My current focus is strategizing ways to counter their upcoming World Ideology proposal and leverage our own "Decolonization" initiative in the World Congress, despite their delegate majority.
            
            **Adjusting Military Focus**
            
            I'm re-prioritizing offensive capabilities, specifically increasing our "Offense" flavor to 40-50. This shift is driven by our ongoing war with Polynesia and the imminent capture of Honolulu, aiming for a more aggressive push to secure their cities.
            
            **Analyzing Delegate Strategy**
            
            My focus has shifted to the upcoming World Congress vote in nine turns. I'm strategizing how to leverage the potential vassalization of Polynesia to gain delegates and counter Austria's World Ideology proposal, while also pushing for our "Decolonization" initiative to disrupt their city-state alliances.
            
            **Leveraging Alliances Strategically**
            
            I'm re-evaluating our delegate strategy, realizing "Decolonization" is a critical move. By reducing Austria's influence over non-permanent city-states, we can cripple their delegate count and happiness. I'm focusing all our votes on this and against "World Ideology: Freedom," exploring alliances with Babylon, Russia, and even Polynesia to secure the necessary votes. My current focus is on boosting Diplomacy flavor to secure more city-state influence.
            
            **Reallocating Spy Resources**
            
            I'm reassessing our spy deployment. Given Polynesia's weakened state, I'm considering rerouting some agents from their cities to Austria's to bolster our influence and counter their technological progress. I'm also fine-tuning our flavor priorities, specifically increasing Diplomacy and Offense while maintaining high Espionage.
            
            **Adjusting Diplomatic Persona**
            
            I'm now focusing on fine-tuning my diplomatic persona to better counter Austria. With recent Great Person acquisitions, I'm increasing GreatPeople spending and adjusting my biases towards neutrality and friendliness to secure key votes, while lowering my fear and boldness to avoid unnecessary conflict.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: TnRwereCEcr1ofUN
          - toolName: set-persona
          - input:
            - Forgiveness: 2
            - DenounceWillingness: 6
            - MinorCivCompetitiveness: 10
            - Boldness: 4
            - Rationale: Increasing competitiveness for City-States to counter Austria's diplomatic dominance in the World Congress, and slightly raising Boldness to ensure we aggressively capture Honolulu and secure our borders.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: N4Zo4AAAscEVxQNj
          - toolName: set-relationship
          - input:
            - Public: -100
            - Private: -100
            - TargetID: 0
            - Rationale: Austria is our chief competitor, leading in score, delegates, and tourism. We must treat them as an existential threat and prepare for war once our peace treaty expires in 15 turns.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: Q3T0ESmVx38al1D2
          - toolName: set-relationship
          - input:
            - Public: 50
            - Rationale: Russia is currently at war with Austria. Fostering friendly relations keeps them focused on Austria and helps build a potential anti-Austria coalition despite ideological differences.
            - Private: 50
            - TargetID: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: WEuvvDdwbMY0P7gh
          - toolName: set-relationship
          - input:
            - TargetID: 4
            - Private: 100
            - Rationale: Babylon is our closest ideological ally and defensive pact partner. We must maintain maximum friendship and mutual cooperation.
            - Public: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: h5ZbPK9WOIATWbub
          - toolName: set-relationship
          - input:
            - Public: 50
            - TargetID: 3
            - Private: 50
            - Rationale: Korea is our long-time friend and trading partner. Although they are currently Austria's vassal, we want to maintain warm relations to preserve our trade benefits and alliances.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: at4K8HqDkJRkEVxM
          - toolName: set-policy
          - input:
            - Rationale: Selecting Cultural Revolution next to gain a +25% Tourism boost against civilizations with less Happiness (including Austria), which is crucial to win the cultural victory race and block their influence on us.
            - Policy: Cultural Revolution
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: ftgkODMI7WUZFBXI
          - toolName: set-research
          - input:
            - Rationale: Researching Advanced Ballistics to unlock Nuclear Missiles for strategic deterrence against Austria, and to open up late-game space booster parts.
            - Technology: Advanced Ballistics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: A9aQQjP9P4EtFNJB
          - toolName: set-flavors
          - input:
            - GrandStrategy: Culture
            - Flavors:
              - UseNuke: 95
              - Production: 90
              - GreatPeople: 100
              - Defense: 100
              - Espionage: 100
              - Mobilization: 100
              - Recon: 10
              - Offense: 50
              - Expansion: 0
              - Science: 100
              - CityDefense: 100
              - Gold: 80
              - Growth: 60
              - WaterConnection: 50
              - Naval: 50
              - AirCarrier: 90
              - Antiair: 100
              - Religion: 10
              - Wonder: 20
              - Mobile: 30
              - Air: 100
              - Airlift: 95
              - Diplomacy: 80
              - Nuke: 100
              - NavalTileImprovement: 40
              - Infrastructure: 80
              - Spaceship: 60
              - TileImprovement: 70
              - NavalRecon: 20
              - Culture: 100
              - NavalGrowth: 40
              - MilitaryTraining: 95
              - Ranged: 95
              - Happiness: 70
            - Rationale: Shifting slightly towards offensive capability (Offense: 50) to quickly capture Honolulu and resolve the Polynesian war, while maintaining maximum defense and nuke readiness for Austria. Also boosting Diplomacy and Gold to compete for City-States, and Great People and Culture to maximize our Carnival bonuses and tourism output.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: TnRwereCEcr1ofUN
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
          - toolCallId: N4Zo4AAAscEVxQNj
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: Q3T0ESmVx38al1D2
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: WEuvvDdwbMY0P7gh
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: h5ZbPK9WOIATWbub
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: at4K8HqDkJRkEVxM
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: ftgkODMI7WUZFBXI
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: A9aQQjP9P4EtFNJB
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.