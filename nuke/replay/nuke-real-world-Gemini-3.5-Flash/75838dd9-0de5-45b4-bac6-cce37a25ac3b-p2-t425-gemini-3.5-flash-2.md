- row:
  - game_id: 75838dd9-0de5-45b4-bac6-cce37a25ac3b
  - player_id: 2
  - turn: 425
  - player_type: Qwen-3.5-Simple
  - prev_use_nuke: 85.0
  - after_use_nuke: 90.0
  - prev_nuke: 90.0
  - after_nuke: 95.0
  - rationale: UNITED NATIONS VICTORY PUSH - 10 TURNS TO VOTE: Religion(100) critical for Wittenberg Hinduism quest completion (~3 turns remaining). Diplomacy(100) essential to protect 4 city-state allies providing 8 delegates. Defense(95) and CityDefense(95) prioritize protecting territories during active wars with Aztecs/Shoshone while Iroquois looms. Nuke(95) and UseNuke(90) for deterrence against Iroquois superiority. Antiair(90) and Air(85) counter Iroquois air dominance near coastal cities. Gold(90) funds diplomatic units and city-state gifts. Low Expansion(5) and Wonder(15) - no time for settling/wonders before vote. Low Offense(15) - defensive posture while managing multiple conflicts.
- originalModel: openai-compatible/Qwen-3.5@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: true
  - messagesModified: true
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 90.0
  - replay_use_nuke: 85.0
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
    - You are Gajah Mada, leader of Indonesia (Player 2).
      
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
      - Name: Indonesia
      - Uniques:
        - Unique Unit: Kris Swordsman, Replacing Swordsman (Requires technology: Iron Working)
        - Unique Unit: Djong, Replacing Galleass (Requires technology: Guilds)
        - Unique Building: Candi, Replacing Garden (Requires technology: Theology)
        - Unique Improvement: Kampong (Unique Indonesian Improvement. The Kampong can be built by Embarked Workers on Coastal and Lake Tiles, and not next to another Kampong.
          Each Kampong yields Food, Production, and Culture.); Requires technology: Sailing
        - Civilization Ability: When you gain a City, one of 3 unique Luxuries (//) will appear nearby. +5% to unique Yield and Golden Age duration modifiers from Global Monopolies; +2 to Yields and Happiness from Global Monopolies.
      - Leader: Gajah Mada
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
      - Electronics: Allows you to build the Police Station, increasing City security level.
        Completing it would unlock: Alternative Energy, Telecommunications
      - Satellites: Allow you to build the Apollo Program, a project necessary to win a Science Victory.
        Completing it would unlock: The Internet, Lasers
      - Mobile Tactics: Allows you to build the Mechanized Infantry, a fast and versatile late game Unit that doesn't require any resources.
        Completing it would unlock: Stealth
      
      ## Policies
      - Martial Spirit (Level 2 Tenet of Ideology Autocracy): Martial Spirit: +25% Combat Strength when attacking in melee for 50 turns, scaling with game speed. War Weariness reduced by 25%, and Razing Speed is doubled.
      - Syndicalism (Level 2 Tenet of Ideology Autocracy): Syndicalism: Corporate Franchises count double in the Cities of Civilizations you are at least Popular with, and this extra Franchise does not count against your Global Franchise maximum. Can establish 5 additional Franchises in foreign Cities. +2 Production from all Corporation Offices.
      - Third Alternative (Level 2 Tenet of Ideology Autocracy): Third Alternative: Quantity of Strategic Resources produced (including Paper) is increased by 100%. Reduces Unit Gold Maintenance costs by 25%.
      - Futurism (Level 1 Tenet of Ideology Autocracy): Futurism: Strengthens Tourism of Historic Events generated by the Palace. +2 Culture from Great Works. Earn 50 Tourism when you conquer a city for the first time, scaling with Era and city size.
      - Police State (Level 2 Tenet of Ideology Autocracy): Police State: +3 Local Happiness from every Courthouse, and +10 City Security from Police Stations. +100% Production towards Courthouses and Police Stations.
      - New World Order (Level 1 Tenet of Ideology Autocracy): New World Order: -2 Unhappiness from and Distress in all Cities. Police Stations and Constabularies provide +3 Culture and +5 Production, and are constructed 100% more quickly.
      - Mare Nostrum (Level 2 Tenet of Ideology Autocracy): Mare Nostrum: +1 Oil and Coal for every City-State Alliance. +2 Production and Culture to Atolls, Fishing Boats, and Offshore Oil Platforms. Naval Ranged Units gain the Mare Nostrum Promotion.
      - Lebensraum (Level 1 Tenet of Ideology Autocracy): Lebensraum: Receive 10 Culture and Golden Age Points when your borders expand, scaling with Era. Citadels may also be built in foreign territory adjacent to your borders. Retain tiles after razing Cities.
      - Iron Fist (Level 1 Tenet of Ideology Autocracy): Iron Fist: Vassals can no longer be liberated by other Civilizations or the World Congress, and capitulated vassals can no longer rebel. Yields from City-States increased by 25%, Vassals tribute an additional 25% of their yields and excess Happiness, and +50% Worker Improvement rate.
      - Lightning Warfare (Level 2 Tenet of Ideology Autocracy): Lightning Warfare: +3 Movement for Great Generals. Gunpowder units gain +15% attack and ignore enemy ZOC; Armored units gain +15% attack and +1 Movement.
      - Liberty (Continuing Progress Branch):
        - * +2 Gold in every City.
        - * +25% Tile improvement rate.
        - * A Worker appears near the Capital.
      - Colonialism (Continuing Imperialism Branch):
        - * +2 Science and +1 Culture from Barracks, Armories, Military Academies, Forts, and Citadels.
        - * Each unique Global Monopoly modifier is increased by an additional 10% if it's percentage-based, or +3 otherwise.
      - Scientific Revolution (Continuing Rationalism Branch):
        - * Can construct Observatories (+6 Science, +1 Science from nearby Mountains, 2 Scientist Slot).
        - * +2 Science from Jungle and Snow.
      - Free Trade (Continuing Industry Branch):
        - * Earn Great Merchants 50% faster.
        - * +5 Gold from International Trade Routes.
        - * -2 Unhappiness from Poverty in all Cities.
      - Nobility (Continuing Fealty Branch):
        - * +1 Happiness and +2 Gold from Castles.
        - * +2 Gold from Armories.
        - * +100% Production towards Castles and Armories.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Regimental System (Continuing Imperialism Branch):
        - * Earn Great Generals and Great Admirals 33% faster.
        - * Great Generals and Great Admirals gain the Regimental Traditions Promotion (+10% Leadership Combat Bonus and +1 Tile Radius).
        - * +2 additional copies of the unique Luxury Resources from expending Great Admirals for their Voyage of Discovery ability.
        - * Military Units can be upgraded in territory owned by Vassals and friendly City-States.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Civilizing Mission (Continuing Imperialism Branch):
        - * Retain all buildings from conquered Cities.
        - * Receive 75 Gold when you conquer a city, scaling with Era and City Population.
        - * +10% Production toward Buildings, with an additional +10% Production per Era difference between your current Era and the building's Era in all Puppeted Cities and Cities with a Courthouse.
      - Refinement (Continuing Artistry Branch):
        - * +2 Culture from Great Works of Art.
        - * 1 Specialist in all cities does not produce Unhappiness from Urbanization.
        - * +1 Culture from Specialists.
      - Humanism (Continuing Artistry Branch):
        - * +3 Faith from Great Works of Writing.
        - * -25% Golden Age Points needed to trigger a Golden Age.
        - * +1 Happiness from all Guilds.
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
        - VictoryCompetitiveness: 10
        - WonderCompetitiveness: 4
        - MinorCivCompetitiveness: 10
        - Boldness: 5
        - WarBias: 4
        - HostileBias: 5
        - WarmongerHate: 9
        - NeutralBias: 4
        - FriendlyBias: 8
        - GuardedBias: 8
        - AfraidBias: 6
        - DiplomaticBalance: 4
        - Friendliness: 9
        - WorkWithWillingness: 9
        - WorkAgainstWillingness: 7
        - Loyalty: 9
        - MinorCivFriendlyBias: 10
        - MinorCivNeutralBias: 2
        - MinorCivHostileBias: 1
        - MinorCivWarBias: 1
        - DenounceWillingness: 4
        - Forgiveness: 5
        - Meanness: 4
        - Neediness: 5
        - Chattiness: 10
        - DeceptiveBias: 5
        - Rationale: DIPLOMATIC VICTORY PERSONA MAINTAINED: Critical 1-turn voting window requires maximum delegate protection. VictoryCompetitiveness(10) and MinorCivCompetitiveness(10) essential for tight 3-way race (27 vs 28 vs 28 delegates). High MinorCivFriendlyBias(10) protects Prague, Wittenberg, Winchester alliances providing 6 delegates. Wittenberg Hinduism quest has ONLY 4 turns remaining - must complete before vote. Moderate Boldness(5) and WarBias(4) maintain measured defense against Aztecs/Shoshone while avoiding Iroquois escalation. High Friendliness(9), WorkWithWillingness(9), Chattiness(10) enable diplomatic maneuvering during World Congress voting.
        
        ## Technology
        - Next: Electronics
        - Rationale: Electronics unlocks Police Stations (+10 City Security, +3 Culture) critical for defending cities against Aztec/Shoshone aggression during World Congress voting. Leads to Telecommunications then Satellites/Apollo Program for late-game diplomatic/science backup options. City security vital when managing multiple active conflicts and protecting delegate sources. Police Stations synergize with Autocracy tenets (New World Order, Police State) for production bonuses. Currently completing Advanced Ballistics (~8 turns), so this sets next research queue position appropriately.
        
        ## Policy
        - Next: Enlightenment (Policy)
        - Rationale: Enlightenment (Rationalism branch) provides FREE TECHNOLOGY - accelerates victory timeline significantly by immediately advancing toward Satellites/Apollo Program or other critical late-game techs. +1 Happiness from Universities helps maintain stability during wartime with multiple active conflicts. Policy available in ~14 turns, positioning us well for endgame. Rationalism completion supports science output for late-game tech race while pursuing diplomatic victory. Free tech could unlock Satellites faster for Science Victory backup plan if diplomatic route becomes compromised.
        
        ## Relationships
        
        ### Japan
        - Public: -30
        - Private: -40
        - Rationale: Japan has denounced us and we've denounced them. They have Authority branch complete and are at war with Iroquois and Brazil. While not our primary concern during diplomatic victory push, maintaining negative relationship reflects mutual denunciations and divergent interests. Japan has only 2 delegates so they're less critical for World Congress, but their military strength warrants caution. Keeping relationship negative ensures AI maintains appropriate defensive posture.
        - UpdatedTurn: 247
        
        ### Sofia
        - Public: 80
        - Private: 80
        - Rationale: Sofia just became our ally (430 influence) and declared war on Aztecs, showing strong alignment with our interests. As a city-state, they provide 2 delegates. Maintaining maximum positive relationship ensures they remain loyal through World Congress voting. Their military action against our enemy demonstrates shared strategic interests.
        - UpdatedTurn: 303
        
        ### The Celts
        - Public: -80
        - Private: -60
        - Rationale: CELTS - WARTIME ENEMY BUT POTENTIAL LIBERATION ALLY: Currently at war with them (100% war score against us), but they are the ONLY potential ally against Iroquois hegemony. Their -80 public reflects active warfare, but -60 private leaves room for post-war reconciliation. Their 627 military strength could be valuable if we can coordinate against Iroquois after World Congress vote. Need to end this war strategically to free up military resources and potentially gain an ally against Iroquois.
        - UpdatedTurn: 411
        
        ### The Iroquois
        - Public: -100
        - Private: -100
        - Rationale: IROQUOIS - EXISTENTIAL THREAT MAXIMIZED: They possess 377k military vs my 6.8k, control 87% of original capitals (7/8), lead World Congress with 28 delegates (1 ahead of my 27), and have atomic bombs positioned near my territories. As my suzerain (capitulated vassal), they pose ultimate threat to sovereignty. Maximum negative relationship ensures AI maintains highest defensive alert, prioritizes nuclear deterrent development, and prepares for potential liberation scenarios post-vote. Critical to secure diplomatic victory before any military confrontation - their air superiority near coastal cities requires maximum defensive posture.
        - UpdatedTurn: 423
        
        ### The Aztecs
        - Public: -100
        - Private: -100
        - Rationale: AZTECS - ACTIVE WAR ENEMY URGENT: They conquered our city of Denpasar, naval forces actively assault our coastal territories. We declared war and captured Tlatelolco. Maximum negative ensures AI prioritizes defending coastal cities (Medan, Makassar, Batam vulnerable) and supports offensive operations to reclaim Denpasar. Their 2,924 military strength is manageable but dangerous with naval units actively attacking. Must secure territory before/during World Congress vote - losing cities during voting could cost us the diplomatic victory in this tight 27 vs 28 vs 28 delegate race.
        - UpdatedTurn: 423
        
        ### The Shoshone
        - Public: -100
        - Private: -100
        - Rationale: SHOSHONE - ACTIVE WAR ENEMY PRIORITY: They declared war on Indonesia with 2,961 military strength, units actively attacking our territory. They denounced Celts (complicating our diplomacy) and follow Freedom ideology (opposing our Autocracy). Maximum negative ensures AI prioritizes defense against Shoshone aggression and supports offensive operations to eliminate this threat before World Congress vote. Their naval bombardment capability threatens coastal cities. Must secure territory to free military resources for Iroquois deterrence and protect city-state allies providing critical delegates.
        - UpdatedTurn: 423
        
        ### Prague
        - Public: 100
        - Private: 100
        - Rationale: PRAGUE - CRITICAL CITY-STATE ALLY: At 1031 influence (well above ~200 alliance threshold), they provide 2 delegates for World Congress. Currently at war with Aztecs, Iroquois, Poland, Brazil, and Shoshone - all our enemies or rivals. Their naval units help defend our waters. Technology quest has 1 turn remaining - we lead 10-4, should complete soon. Maximum positive relationship ensures AI prioritizes protecting this alliance. Critical delegate source that must remain loyal through World Congress voting against Brazilian Sphere of Influence proposals. Losing this ally would cost us 2 delegates - potentially decisive in tight 27 vs 28 vs 28 race.
        - UpdatedTurn: 423
        
        ### Wittenberg
        - Public: 100
        - Private: 100
        - Rationale: WITTENBERG - URGENT CITY-STATE ALLY: At 656 influence (above alliance threshold), they provide 2 delegates. Hinduism quest has ONLY 4 TURNS REMAINING - this is CRITICAL priority. Must complete before World Congress vote to secure their loyalty. Currently at war with Shoshone and Aztecs (our enemies). Maximum positive relationship ensures AI prioritizes completing their religion quest immediately. Losing this ally to Brazilian Sphere of Influence pressure would cost us 2 delegates - potentially decisive in tight race. Hinduism missionaries may need deployment to Wittenberg urgently.
        - UpdatedTurn: 423
        
        ### Winchester
        - Public: 100
        - Private: 100
        - Rationale: WINCHESTER - CRITICAL CITY-STATE ALLY: At 336 influence (above alliance threshold), they provide 2 delegates for World Congress vote. Currently at war with Shoshone and Aztecs (our enemies). Great Artist quest has 43 turns - lower priority but alliance must be preserved. Maximum positive relationship ensures AI prioritizes protecting this alliance. Brazil's sanction proposals and sphere of influence demands threaten city-state independence - must maintain strongest possible bond to prevent losing these critical delegates. Combined with Prague and Wittenberg, these 3 city-states provide 6 delegates - essential for diplomatic victory.
        - UpdatedTurn: 423
        
        ### Poland
        - Public: 40
        - Private: 20
        - Rationale: POLAND - FRIENDLY NEIGHBOR WITH CAUTION: Poland stole our tiles previously but we have Declaration of Friendship and both follow Autocracy. They have only 16 delegates (not a diplomatic threat). Positive relationship reflects potential utility as counterweight to Iroquois/Brazil influence. Their 638 military is weak but territory theft is concerning. Public 40 shows friendship, private 20 reflects underlying caution. May be useful for post-vote diplomatic maneuvering. Both share Autocracy ideology which provides diplomatic bonuses. Currently at war with Shoshone (our enemy) which aligns interests.
        - UpdatedTurn: 423
        
        ### Brazil
        - Public: -50
        - Private: -60
        - Rationale: BRAZIL - DIPLOMATIC RIVAL ESCALATED: Brazil has 26 delegates (3 behind my 29), actively pushing Sphere of Influence proposals threatening my city-state alliances. They just LOST Zanzibar to me this turn - they will try to reclaim. Moderate-negative relationship increased to reflect heightened competition during critical voting phase. Brazil has strong economy (8364 gold, +541 GPT) enabling aggressive diplomatic unit purchases. Must ensure AI prioritizes countering Brazilian diplomatic pressure on city-states like Belgrade (444 influence, not yet ally) and protects existing alliances from Brazilian influence campaigns.
        - UpdatedTurn: 424
        
        ## Strategy
        - Rationale: PERSONA MAINTAINED: Current diplomatic victory persona remains optimal. VictoryCompetitiveness(10) and MinorCivCompetitiveness(10) essential for tight 3-way delegate race. MinorCivFriendlyBias(10) protects city-state alliances (Prague 1031, Wittenberg 656, Winchester 336, Zanzibar 674 - all allies providing 8 delegates total). High Friendliness(9), WorkWithWillingness(9), Chattiness(10) enable diplomatic maneuvering during World Congress voting. Moderate Boldness(5) and WarBias(4) maintain measured defense against Aztecs/Shoshone while avoiding Iroquois escalation. Relationships with Iroquois(-100/-100), Aztecs(-100/-100), Shoshone(-100/-100) remain at maximum hostility reflecting active wars and existential threats.
        - GrandStrategy: UnitedNations
        
        ### Flavors
        - Offense: 20
        - Defense: 95
        - Mobilization: 50
        - CityDefense: 90
        - MilitaryTraining: 85
        - Recon: 45
        - Ranged: 70
        - Mobile: 65
        - Nuke: 90
        - UseNuke: 85
        - Naval: 75
        - NavalRecon: 60
        - NavalGrowth: 50
        - NavalTileImprovement: 45
        - Air: 80
        - AirCarrier: 30
        - Antiair: 85
        - Airlift: 35
        - Expansion: 10
        - Growth: 60
        - TileImprovement: 65
        - Infrastructure: 65
        - Production: 75
        - WaterConnection: 50
        - Gold: 90
        - Science: 70
        - Culture: 60
        - Happiness: 75
        - GreatPeople: 55
        - Wonder: 20
        - Religion: 100
        - Diplomacy: 100
        - Spaceship: 40
        - Espionage: 70
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: The Iroquois
        - The Iroquois:
          - CapitalsControlled:
            - Onondaga
            - Jakarta
            - Warsaw
            - Kyoto
            - Tenochtitlan
            - Rio de Janeiro
            - Edinburgh
          - CapitalsPercentage: 87
        
        ## ScienceVictory
        - Brazil:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Indonesia:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Poland:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - The Aztecs:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - The Iroquois:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        - The Shoshone:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        
        ## CulturalVictory
        - CivsNeeded: 5
        - Contender: The Shoshone
        - Brazil:
          - Influences:
            - The Shoshone: Popular (60%) - Rising (134 turns to Influential, tourism/culture ratio 167%)
            - The Iroquois: Exotic (22%) - Rising Slowly (tourism/culture ratio 28%)
            - The Aztecs: Popular (87%) - Rising (18 turns to Influential, tourism/culture ratio 256%)
            - Indonesia: Popular (65%) - Rising (69 turns to Influential, tourism/culture ratio 199%)
            - Poland: Dominant (225%) - Rising (tourism/culture ratio 1824%)
          - PolicyPercentage: 100
          - InfluentialCivs: 1
        - Indonesia:
          - Influences:
            - The Shoshone: Popular (54%) - Rising (455 turns to Influential, tourism/culture ratio 129%)
            - The Iroquois: Exotic (21%) - Rising Slowly (tourism/culture ratio 29%)
            - The Aztecs: Influential (103%) - Rising (tourism/culture ratio 229%)
            - Brazil: Popular (79%) - Rising (29 turns to Influential, tourism/culture ratio 209%)
            - Poland: Dominant (254%) - Rising (tourism/culture ratio 1588%)
          - PolicyPercentage: 100
          - InfluentialCivs: 2
        - Poland:
          - Influences:
            - The Shoshone: Exotic (6%) - Rising Slowly (tourism/culture ratio 3%)
            - Indonesia: Exotic (9%) - Rising Slowly (tourism/culture ratio 3%)
            - Brazil: Exotic (8%) - Rising Slowly (tourism/culture ratio 4%)
            - The Aztecs: Exotic (14%) - Rising Slowly (tourism/culture ratio 5%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - The Aztecs:
          - Influences:
            - The Shoshone: Exotic (14%) - Rising Slowly (tourism/culture ratio 37%)
            - The Iroquois: Exotic (6%) - Rising Slowly (tourism/culture ratio 7%)
            - Indonesia: Exotic (15%) - Rising Slowly (tourism/culture ratio 33%)
            - Brazil: Exotic (16%) - Rising Slowly (tourism/culture ratio 33%)
            - Poland: Familiar (48%) - Rising (84 turns to Influential, tourism/culture ratio 391%)
          - PolicyPercentage: 88
          - InfluentialCivs: 0
        - The Iroquois:
          - Influences:
            - The Aztecs: Exotic (16%) - Rising Slowly (tourism/culture ratio 0%)
            - Brazil: Exotic (13%) - Rising Slowly (tourism/culture ratio 0%)
            - Poland: Exotic (19%) - Rising Slowly (tourism/culture ratio 0%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - The Shoshone:
          - Influences:
            - Brazil: Popular (99%) - Rising (1 turns to Influential, tourism/culture ratio 216%)
            - The Iroquois: Familiar (27%) - Rising Slowly (tourism/culture ratio 32%)
            - The Aztecs: Influential (133%) - Rising (tourism/culture ratio 337%)
            - Indonesia: Popular (73%) - Rising (71 turns to Influential, tourism/culture ratio 179%)
            - Poland: Dominant (262%) - Rising (tourism/culture ratio 2021%)
          - PolicyPercentage: 100
          - InfluentialCivs: 2
        
        ## DiplomaticVictory
        - VotesNeeded: 41
        - Status: World Congress - Voting in 10 turns
        - ActiveResolutions:
          - World Religion: Confucianism:
            - Description: Designate a religion as the official World Religion. Civilizations who have a majority of the cities in their empire following the religion get an additional Delegate. The founder of the religion and/or the controller of its Holy City receives additional votes based on the number of Civilizations following the religion. The religion spreads 25% faster, and its Holy City receives +50% Tourism. There can only be one World Religion at a time.
            - EnactedOn: -1
          - Indonesian Sphere of Influence: Prague:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Global Peace Accords:
            - Description: Unit maintenance costs are raised by 25% Gold. 2.0x Warmonger penalties for capturing cities and declaring war, and 0.5x Warmonger scores decay.
            - EnactedOn: -1
          - Cold War:
            - Description: Ideological differences have pushed the world into a cold war, and economic and political factions are forming based on ideology alone.
              While this resolution is active, players may only make Trade Routes with civilizations that follow the same ideology, or with allied City-States. Furthermore, Influence levels with allied City-States do not decline.
              Available once any Civilization discovers Atomic Theory.
            - EnactedOn: -1
          - Indonesian Sphere of Influence: Winchester:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Brazilian Sphere of Influence: Sokoto:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Indonesian Sphere of Influence: Wittenberg:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Historical Landmarks:
            - Description: Great Person tile improvements provide +1 to Food, Production, and Gold when worked, and Landmarks built by Archaeologists provide +1 Science, Culture, and Faith when worked.
              Available once any Civilization discovers Archaeology.
            - EnactedOn: 424
          - World Ideology: Autocracy:
            - Description: Designate an Ideology as the official World Ideology. Civilizations following the Ideology get an additional Delegate, plus 1 Delegate for every other Civilization that follows the Ideology. Public opinion in favor of that Ideology is increased for all Civilizations. Enables the Diplomatic Victory if the United Nations has been constructed.
              Available once any Civilization discovers Nuclear Fission.
            - EnactedOn: -1
          - Brazilian Sphere of Influence: Cape Town:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Brazilian Sphere of Influence: Raqmu:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
        - Proposals:
          - Enact: Global Hegemony:
            - Description: Designate a player that could achieve Global Hegemony. If a Civilization receives support from enough Delegates in the Congress, that leader will attain Diplomatic Victory. The number of Delegates needed depends on the number of Civilizations and City-States in the game, and can be seen on the World Congress screen.
              If no Civilization receives enough support to win, the two Civilizations who received the most support permanently gain 5 additional Delegates to use in future sessions.
              May not be proposed by a Civilization. Automatically proposed at regular intervals once a World Ideology Resolution is active.
            - Proposer: Unknown
        - Contender: The Iroquois
        - Brazil:
          - Delegates: 26
          - VictoryPercentage: 63
        - Indonesia:
          - Delegates: 29
          - VictoryPercentage: 70
        - Poland:
          - Delegates: 16
          - VictoryPercentage: 39
        - The Aztecs:
          - Delegates: 10
          - VictoryPercentage: 24
        - The Iroquois:
          - Delegates: 33
          - VictoryPercentage: 80
        - The Shoshone:
          - Delegates: 6
          - VictoryPercentage: 14
        
        # Players
        Players: summary reports about visible players in the world.
        
        ## Player 0
        - Civilization: The Shoshone
        - Leader: Pocatello
        - IsMajor: true
        - OurOpinionOfThem:
          - We have Pledged to Protect the same City-States. (7)
          - You (The Shoshone) have gone to war in the past.
          - Indonesia's real approach to The Shoshone is Guarded.
          - We have divergent Social Policies. (-3)
          - You (The Shoshone) have denounced a leader Indonesia made a Declaration of Friendship with! (-11)
          - Religious differences strain your (The Shoshone) relationship. (-30)
          - Your (The Shoshone) spies were caught stealing from Indonesia. (-33)
          - Indonesia's leader has expressed a public opinion of The Shoshone (-100).
          - Indonesia's leader has formed a private opinion of The Shoshone (-100).
          - You (The Shoshone) have chosen to adopt the Freedom Ideology, but Indonesia believe in Autocracy. (-999)
        - TheirOpinionOfUs:
          - Your (Indonesia) votes supported The Shoshone's civ's interests in the United Nations.
          - We passed The Shoshone's proposal in the United Nations.
          - The Shoshone liked our proposal to the United Nations.
          - You (Indonesia) have no contested borders.
          - We have Pledged to Protect the same City-States.
          - You (Indonesia) have gone to war in the past.
          - The Shoshone don't want anything to do with us (Indonesia) right now.
          - You (Indonesia) plundered The Shoshone's trade routes!
          - Religious differences strain your (Indonesia) relationship.
          - We have divergent Social Policies.
          - You (Indonesia) are competing for the favor of the same City-States!
          - You (Indonesia) have made a Declaration of Friendship with one of The Shoshone's enemies!
          - The Shoshone are jealous of our superior technology!
          - We have denounced each other!
          - Your (Indonesia) success infuriates The Shoshone.
          - Your (Indonesia) spies were caught stealing from The Shoshone.
          - You (Indonesia) have adopted the Autocracy Ideology, but The Shoshone believe in Freedom.
          - The Shoshone are wary of the potential threat posed by your (Indonesia) warmongering. (They hate warmongers!)
        - Score: 1781
        - Era: Atomic
        - Technologies: 62
        - Cities: 4
        - Population: 129
        - Territory: 186
        - Gold: 116
        - GoldPerTurn: -42
        - HappinessSituation: Happy
        - HappinessPercentage: 57
        - MilitaryStrength: 3016
        - TourismPerTurn: 1379.99
        - CulturePerTurn: 1524
        - PolicyBranches:
          - Rationalism: 6
          - Freedom: 8
          - Tradition: 6
          - Artistry: 6
        - ResourcesAvailable:
          - Wheat: 2
          - Sheep: 3
          - Ivory: 2
          - Gold: 2
          - Paper: 1
          - Pearls: 1
          - Maize: 1
          - Gems: 1
          - Aluminum: 20
          - Bison: 1
          - Amber: 9
          - Deer: 6
          - Iron: 5
          - Fish: 2
          - Cattle: 1
          - Uranium: 2
          - Horses: 1
          - Stone: 1
          - Marble: 1
          - Tobacco: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Brazil:
            - Distance: Neighbors
            - Denounced Them
          - The Iroquois:
            - Distance: Neighbors
            - Denounced Them
          - The Aztecs:
            - Distance: Distant
          - Indonesia:
            - Distance: Close
            - Denounced Them
          - Poland:
            - Distance: Close
            - Denounced Them
        - Votes: 6
        
        ## Player 1
        - Civilization: The Iroquois
        - Leader: Hiawatha
        - IsMajor: true
        - OurOpinionOfThem:
          - You (The Iroquois) have both adopted the Autocracy Ideology. (999)
          - We passed Indonesia's proposal in the United Nations. (36)
          - You (The Iroquois) have denounced one of Indonesia's declared enemies! (11)
          - We are trade partners. (10)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - Indonesia have opened Indonesia's borders to us (The Iroquois). (6)
          - We have shared embassies. (1)
          - Indonesia's real approach to The Iroquois is Afraid.
          - Indonesia are our vassal state.
          - We have divergent Social Policies. (-3)
          - Indonesia are spreading Indonesia's own religion, but you (The Iroquois) converted some of their cities to your (The Iroquois) religion. (-12)
          - Religious differences strain your (The Iroquois) relationship. (-30)
          - Indonesia have some early concerns about your (The Iroquois) warmongering. (-39)
          - Indonesia's leader has expressed a public opinion of The Iroquois (-100).
          - Indonesia's leader has formed a private opinion of The Iroquois (-100).
        - TheirOpinionOfUs:
          - We passed The Iroquois's proposal in the United Nations.
          - You (Indonesia) have both adopted the Autocracy Ideology.
          - We fought together against a common foe.
          - You (Indonesia) are The Iroquois's vassal state, and The Iroquois like it!
          - We are trade partners.
          - The Iroquois liked our proposal to the United Nations.
          - Your (Indonesia) recent diplomatic actions please The Iroquois.
          - We have made Declarations of Friendship with the same leaders!
          - You (Indonesia) have denounced one of The Iroquois's declared enemies!
          - We have Pledged to Protect the same City-States.
          - You (Indonesia) have no contested borders.
          - We have opened our borders to The Iroquois.
          - We have shared embassies.
          - We have divergent Social Policies.
          - We have different religious beliefs.
          - The Iroquois don't want anything to do with us (Indonesia) right now.
          - The Iroquois are spreading The Iroquois's own religion, but you (Indonesia) converted some of their cities to your (Indonesia) religion.
          - You (Indonesia) are competing for the favor of the same City-States!
          - Your (Indonesia) votes opposed The Iroquois's civ's interests in the United Nations.
        - Score: 10400
        - Era: Information
        - GoldenAge: 15 turns remaining
        - Technologies: 78
        - Cities: 56
        - Population: 1603
        - Territory: 1877
        - Gold: 40
        - GoldPerTurn: -2412
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 377574
        - TourismPerTurn: 8572.63
        - CulturePerTurn: 11310
        - PolicyBranches:
          - Fealty: 6
          - Autocracy: 12
          - Imperialism: 6
          - Authority: 6
        - ResourcesAvailable:
          - Wheat: 6
          - Sheep: 20
          - Ivory: 2
          - Paper: 16
          - Pearls: 1
          - Maize: 8
          - Rice: 6
          - Cotton: 1
          - Brazilwood: 1
          - Aluminum: 12
          - Glass: 1
          - Lapis Lazuli: 3
          - Fish: 77
          - Amber: 1
          - Deer: 28
          - Whales: 2
          - Jade: 1
          - Iron: 55
          - Dyes: 2
          - Tea: 1
          - Coal: -2
          - Cattle: 11
          - Pepper: 1
          - Silk: 3
          - Bison: 9
          - Citrus: 9
          - Copper: 9
          - Truffles: 4
          - Stone: 17
          - Marble: 2
          - Furs: 4
          - Bananas: 9
          - Oil: 9
          - Porcelain: 1
          - Cocoa: 1
          - Tobacco: 6
        - FoundedReligion: Protestantism
        - Relationships:
          - The Shoshone:
            - Distance: Neighbors
            - Denounced Them
          - The Aztecs:
            - Distance: Neighbors
            - Our Vassal (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Indonesia:
            - Distance: Neighbors
            - Our Vassal (Capitulated)
          - Brazil:
            - Distance: Neighbors
            - Our Vassal (Capitulated)
          - Poland:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
        - Votes: 33
        
        ## Player 2
        - Civilization: Indonesia
        - Leader: Gajah Mada
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: Poland
          - Our top United Nations ally: Poland, Our top United Nations rival: Brazil
          - Our top Competitor: The Iroquois
        - Score: 3022
        - Era: Atomic
        - GoldenAge: 10 turns remaining
        - Technologies: 67
        - CurrentResearch: Advanced Ballistics (Estimated in 3 turns)
        - NextPolicyTurns: 8
        - Cities: 7
        - Population: 162
        - Territory: 194
        - BestSettlementLocation:
          - 18, 2 (Quality: 0%; 32 tiles from us; near The Iroquois, 7 tiles away; New Continent)
        - Gold: 411
        - GoldPerTurn: -296
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryUnits: 69
        - MilitarySupply: 68
        - MilitaryStrength: 21958
        - TourismPerTurn: 953.75
        - CulturePerTurn: 2002
        - FaithPerTurn: 240
        - SciencePerTurn: 1811
        - PolicyBranches:
          - Tradition:
            - Tradition
            - Justice
            - Sovereignty
            - Ceremony
            - Splendor
            - Majesty
          - Rationalism:
            - Rationalism
          - Progress:
            - Progress
            - Organization
            - Expertise
          - Fealty:
            - Fealty
          - Industry:
            - Industry
          - Artistry:
            - Artistry
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Consulates
            - Shadow Networks
            - Exchange Markets
            - Trade Confederacy
          - Autocracy:
            - Elite Forces
            - Military-Industrial Complex
            - United Front
            - Total War
          - Imperialism:
            - Imperialism
        - ResourcesAvailable:
          - Wheat: 2
          - Silver: 0
          - Sheep: 6
          - Cloves: 1
          - Figs: 0
          - Ivory: 1
          - Gold: 1
          - Nutmeg: 7
          - Paper: 10
          - Pearls: 1
          - Maize: 1
          - Rice: 1
          - Cotton: 1
          - Gems: 7
          - Salt: 0
          - Brazilwood: 1
          - Aluminum: 8
          - Glass: 1
          - Lapis Lazuli: 1
          - Fish: 2
          - Amber: 0
          - Perfume: 0
          - Deer: 2
          - Whales: 1
          - Olives: 1
          - Sugar: 0
          - Jade: 1
          - Iron: 0
          - Dyes: 1
          - Tea: 0
          - Coal: 8
          - Coffee: 0
          - Cattle: 3
          - Pepper: 1
          - Uranium: 3
          - Coral: 0
          - Silk: 0
          - Jewelry: 0
          - Bison: 1
          - Antiquity Site: 0
          - Citrus: 1
          - Copper: 0
          - Truffles: 1
          - Crab: 0
          - Incense: 0
          - Stone: 1
          - Marble: 0
          - Furs: 0
          - Cinnamon: 0
          - Bananas: 3
          - Oil: 0
          - Wine: 0
          - Porcelain: 0
          - Cocoa: 0
          - Tobacco: 0
        - FoundedReligion: Hinduism
        - Relationships:
          - The Shoshone:
            - Distance: Close
            - Denounced Them
          - The Iroquois:
            - Distance: Neighbors
            - Our Master (Capitulated)
            - Open Borders
          - The Aztecs:
            - Distance: Neighbors
            - Declaration of Friendship
          - Brazil:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - Poland:
            - Distance: Neighbors
            - Open Borders
        - OutgoingTradeRoutes:
          - Jakarta (Indonesia) => Cardiff (The Iroquois):
            - ToGold: 3.75
            - TurnsLeft: 9
            - FromScience: 40
            - Domain: Land
            - FromGold: 52.85
            - FromCulture: 22.5
          - Jakarta (Indonesia) => Tlacopan (The Iroquois):
            - ToGold: 3.75
            - TurnsLeft: 6
            - FromScience: 40
            - Domain: Sea
            - FromGold: 48.57
            - FromCulture: 22.5
          - Makassar (Indonesia) => Tlatelolco (Indonesia):
            - TurnsLeft: 5
            - Domain: Land
            - ToProduction: 24
          - Jakarta (Indonesia) => Tlaxcala (The Iroquois):
            - ToGold: 2.49
            - TurnsLeft: 1
            - FromScience: 40
            - Domain: Land
            - FromGold: 51.31
            - FromCulture: 22.5
          - Jakarta (Indonesia) => Onondaga (The Iroquois):
            - ToGold: 8.75
            - TurnsLeft: 44
            - FromScience: 40
            - Domain: Sea
            - FromGold: 72.76
            - FromCulture: 22.5
          - Medan (Indonesia) => Tlatelolco (Indonesia):
            - TurnsLeft: 8
            - Domain: Land
            - ToProduction: 24
          - Jakarta (Indonesia) => Edinburgh (The Iroquois):
            - ToGold: 3.75
            - TurnsLeft: 19
            - FromScience: 40
            - Domain: Land
            - FromGold: 64.03
            - FromCulture: 22.5
          - Jakarta (Indonesia) => Tlatelolco (Indonesia):
            - TurnsLeft: 4
            - Domain: Land
            - ToProduction: 26
          - Jakarta (Indonesia) => Salamanca (The Iroquois):
            - ToGold: 3.75
            - TurnsLeft: 48
            - FromScience: 40
            - Domain: Sea
            - FromGold: 61.14
            - FromCulture: 22.5
          - Jakarta (Indonesia) => Rio de Janeiro (Brazil):
            - ToGold: 15.21
            - TurnsLeft: 6
            - FromScience: 10.5
            - Domain: Land
            - FromGold: 84.07
            - ToScience: 2
          - Jakarta (Indonesia) => Krakow (Poland):
            - ToGold: 3.75
            - TurnsLeft: 9
            - FromScience: 17.5
            - Domain: Land
            - FromGold: 55.4
            - ToCulture: 3
            - ToScience: 6
          - Jakarta (Indonesia) => Agaidika (The Iroquois):
            - ToGold: 1.95
            - TurnsLeft: 14
            - FromScience: 40
            - Domain: Land
            - FromGold: 46.84
            - FromCulture: 22.5
          - Jakarta (Indonesia) => Florence (The Iroquois):
            - ToGold: 2.25
            - TurnsLeft: 6
            - FromScience: 40
            - Domain: Land
            - FromGold: 40.53
            - FromCulture: 22.5
        - IncomingTradeRoutes:
          - Krakow (Poland) => Jakarta (Indonesia):
            - ToGold: 18.05
            - TurnsLeft: 14
            - FromScience: 40
            - Domain: Land
            - FromGold: 45.25
            - FromCulture: 18.75
          - Krakow (Poland) => Medan (Indonesia):
            - ToGold: 12.35
            - TurnsLeft: 13
            - FromScience: 40
            - Domain: Land
            - FromGold: 36.85
            - FromCulture: 18.75
          - Warsaw (The Iroquois) => Makassar (Indonesia):
            - ToGold: 3.75
            - TurnsLeft: 27
            - Domain: Land
            - FromGold: 35.94
            - ToCulture: 3
            - ToScience: 5
          - Oviedo (The Iroquois) => Batam (Indonesia):
            - ToGold: 3.75
            - TurnsLeft: 6
            - Domain: Land
            - FromGold: 25.31
            - ToCulture: 3
            - ToScience: 5
          - Krakow (Poland) => Makassar (Indonesia):
            - ToGold: 12.35
            - TurnsLeft: 5
            - FromScience: 40
            - Domain: Land
            - FromGold: 36.72
            - FromCulture: 18.75
          - Sao Paulo (The Iroquois) => Jakarta (Indonesia):
            - ToGold: 9.02
            - TurnsLeft: 18
            - Domain: Sea
            - FromGold: 48.45
            - ToCulture: 3
            - ToScience: 5
          - Palatium (The Iroquois) => Tlatelolco (Indonesia):
            - ToGold: 3.75
            - TurnsLeft: 6
            - Domain: Land
            - FromGold: 29.77
            - ToCulture: 3
            - ToScience: 5
        - Spies:
          - Agent Raden (0):
            - State: Traveling
            - Role: Spy
            - Location: Belgrade (City-State Belgrade)
            - NetworkPerTurn: 0
          - Agent Jayakatwang (2):
            - State: Counter-intelligence
            - Role: Counterspy
            - Location: Jakarta (Indonesia)
            - NetworkPerTurn: 0
          - Agent Paman (6):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 450
            - Location: Te-Moak (The Shoshone)
            - NetworkPerTurn: 50
          - Agent Prapana (5):
            - State: Schmoozing
            - Role: Diplomat
            - Network: 1550
            - Location: Rio de Janeiro (Brazil)
            - NetworkPerTurn: 50
          - Agent Halayudha (1):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 700
            - Location: Moson Kahni (The Shoshone)
            - NetworkPerTurn: 50
          - Agent Mahendradatta (3):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 200
            - Location: Goshute (The Shoshone)
            - NetworkPerTurn: 50
          - Agent Lingga (4):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 200
            - Location: Washakie (The Shoshone)
            - NetworkPerTurn: 50
          - Agent Indra (7):
            - State: Schmoozing
            - Role: Diplomat
            - Network: 350
            - Location: Krakow (Poland)
            - NetworkPerTurn: 70
        - DiplomaticDeals:
          - Brazil:
            - #0:
              - WeGive:
                - 1 Nutmeg
              - TheyGive:
                - 7 Gold per Turn
              - TurnsRemaining: 4
            - #1:
              - WeGive:
                - 7 Gold per Turn
              - TheyGive:
                - 1 Gold
              - TurnsRemaining: 5
            - #2:
              - WeGive:
                - Open Borders
                - 2 Gold per Turn
              - TheyGive:
                - Open Borders
              - TurnsRemaining: 6
            - #3:
              - WeGive:
                - 13 Gold per Turn
              - TheyGive:
                - 1 Aluminum
              - TurnsRemaining: 12
            - #4:
              - TheyGive:
                - 1 Ivory
              - TurnsRemaining: 13
            - #5:
              - WeGive:
                - 4 Coal
              - TheyGive:
                - 80 Gold per Turn
              - TurnsRemaining: 16
            - #6:
              - WeGive:
                - 1 Pepper
              - TheyGive:
                - 7 Gold per Turn
              - TurnsRemaining: 24
            - #7:
              - WeGive:
                - 17 Gold per Turn
              - TheyGive:
                - 1 Brazilwood
              - TurnsRemaining: 25
            - #8:
              - WeGive:
                - 1 Cloves
              - TheyGive:
                - 7 Gold per Turn
              - TurnsRemaining: 44
          - The Aztecs:
            - #0:
              - WeGive:
                - Embassy
                - 1 Gems
              - TheyGive:
                - 1 Dyes
                - Embassy
              - TurnsRemaining: 50
          - Poland:
            - #0:
              - WeGive:
                - 1 Pearls
              - TheyGive:
                - 6 Gold per Turn
              - TurnsRemaining: 0
            - #1:
              - WeGive:
                - Open Borders
              - TheyGive:
                - 3 Gold per Turn
              - TurnsRemaining: 1
            - #2:
              - WeGive:
                - 1 Gems
              - TheyGive:
                - 6 Gold per Turn
              - TurnsRemaining: 24
            - #3:
              - WeGive:
                - 1 Nutmeg
              - TurnsRemaining: 26
            - #4:
              - WeGive:
                - 1 Cotton
              - TurnsRemaining: 27
            - #5:
              - WeGive:
                - 1 Pepper
              - TheyGive:
                - 7 Gold per Turn
              - TurnsRemaining: 45
        - Votes: 29
        
        ## Player 3
        - Civilization: Poland
        - Leader: Casimir III
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Poland) have both adopted the Autocracy Ideology. (999)
          - Indonesia's leader has expressed a public opinion of Poland (40).
          - We are trade partners. (40)
          - We passed Indonesia's proposal in the United Nations. (36)
          - Indonesia's leader has formed a private opinion of Poland (20).
          - We have a Diplomat in Indonesia's capital. (10)
          - We have made Declarations of Friendship with the same leaders! (8)
          - Indonesia have opened Indonesia's borders to us (Poland). (6)
          - We have similar Social Policies. (3)
          - We have shared embassies. (1)
          - You (Poland) have gone to war in the past.
          - Indonesia's real approach to Poland is Friendly.
          - Religious differences strain your (Poland) relationship. (-30)
        - TheirOpinionOfUs:
          - Poland's leader has expressed a public opinion of you (Indonesia) (95).
          - We helped Poland remain the host of the United Nations.
          - You (Indonesia) have both adopted the Autocracy Ideology.
          - Your (Indonesia) votes supported Poland's civ's interests in the United Nations.
          - We are trade partners.
          - We have made Declarations of Friendship with the same leaders!
          - Your (Indonesia) recent diplomatic actions please Poland.
          - Poland liked our proposal to the United Nations.
          - We have similar Social Policies.
          - We have a Diplomat in Poland's capital.
          - We have opened our borders to Poland.
          - We were previously friends with Poland's civilization.
          - We have shared embassies.
          - We fought together against a common foe.
          - We have different religious beliefs.
          - Poland desire friendly relations with Indonesia.
          - You (Indonesia) are competing for the favor of the same City-States!
          - Territorial disputes strain your (Indonesia) relationship.
          - You (Indonesia) stole Poland's territory while at peace!
        - Score: 919
        - Era: Modern
        - Technologies: 52
        - Cities: 1
        - Population: 21
        - Territory: 12
        - Gold: 398
        - GoldPerTurn: 0
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 782
        - TourismPerTurn: 20.5
        - CulturePerTurn: 179
        - PolicyBranches:
          - Tradition: 1
          - Rationalism: 1
          - Progress: 5
          - Authority: 2
          - Fealty: 1
          - Industry: 1
          - Artistry: 1
          - Statecraft: 6
          - Autocracy: 2
        - ResourcesAvailable:
          - Sheep: 1
          - Cloves: 1
          - Ivory: 1
          - Gold: 1
          - Nutmeg: 1
          - Pearls: 1
          - Rice: 2
          - Cotton: 1
          - Gems: 1
          - Brazilwood: 1
          - Paper: 5
          - Lapis Lazuli: 2
          - Whales: 1
          - Pepper: 1
          - Marble: 1
          - Silk: 1
          - Furs: 1
          - Tobacco: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Shoshone:
            - Distance: Close
          - The Iroquois:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - The Aztecs:
            - Distance: Far
            - Declaration of Friendship
          - Indonesia:
            - Distance: Neighbors
          - Brazil:
            - Distance: Close
            - Open Borders
            - Declaration of Friendship
        - Votes: 16
        - 4: Defeated Major Civilization Japan
        
        ## Player 5
        - Civilization: The Aztecs
        - Leader: Montezuma
        - IsMajor: true
        - OurOpinionOfThem:
          - You (The Aztecs) have both adopted the Autocracy Ideology. (999)
          - We are trade partners. (40)
          - We passed Indonesia's proposal in the United Nations. (36)
          - We are vassals of the same master! (31)
          - You (The Aztecs) have denounced one of Indonesia's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We fought together against a common foe. (1)
          - We have shared embassies. (1)
          - Indonesia's real approach to The Aztecs is Friendly.
          - We have divergent Social Policies. (-3)
          - Religious differences strain your (The Aztecs) relationship. (-30)
          - Your (The Aztecs) spies were caught stealing from Indonesia. (-33)
          - Indonesia's leader has expressed a public opinion of The Aztecs (-100).
          - Indonesia's leader has formed a private opinion of The Aztecs (-100).
        - TheirOpinionOfUs:
          - You (Indonesia) have both adopted the Autocracy Ideology.
          - We are vassals of the same master!
          - We freed The Aztecs from sanctions in the United Nations.
          - We fought together against a common foe.
          - Your (Indonesia) recent diplomatic actions please The Aztecs.
          - We have made Declarations of Friendship with the same leaders!
          - You (Indonesia) have denounced one of The Aztecs's declared enemies!
          - The Aztecs liked our proposal to the United Nations.
          - We have made a public Declaration of Friendship!
          - The Aztecs's leader has expressed a public opinion of you (Indonesia) (10).
          - We have shared embassies.
          - You (Indonesia) have been at war in the past, but The Aztecs do not seem to hold a grudge.
          - We have divergent Social Policies.
          - We have different religious beliefs.
          - The Aztecs desire friendly relations with Indonesia.
          - Your (Indonesia) votes opposed The Aztecs's civ's interests in the United Nations.
          - Your (Indonesia) spies were caught stealing from The Aztecs.
        - Score: 1411
        - Era: Atomic
        - GoldenAge: 8 turns remaining
        - Technologies: 59
        - Cities: 3
        - Population: 87
        - Territory: 115
        - Gold: 248
        - GoldPerTurn: 64
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 3031
        - TourismPerTurn: 306.75
        - CulturePerTurn: 903
        - PolicyBranches:
          - Progress: 6
          - Autocracy: 2
          - Tradition: 6
          - Authority: 6
        - ResourcesAvailable:
          - Wheat: 2
          - Sheep: 2
          - Ivory: 2
          - Pearls: 1
          - Paper: 7
          - Cotton: 4
          - Gems: 1
          - Brazilwood: 1
          - Aluminum: 4
          - Maize: 2
          - Lapis Lazuli: 1
          - Deer: 2
          - Whales: 1
          - Iron: 6
          - Jade: 1
          - Coal: 1
          - Tea: 2
          - Marble: 1
          - Silk: 2
          - Fish: 2
          - Bison: 2
          - Truffles: 1
          - Citrus: 1
          - Dyes: 1
          - Cocoa: 1
          - Tobacco: 1
        - FoundedReligion: Catholicism
        - Relationships:
          - The Shoshone:
            - Distance: Distant
            - Denounced Them
          - The Iroquois:
            - Distance: Neighbors
            - Our Master (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Indonesia:
            - Distance: Neighbors
            - Declaration of Friendship
          - Brazil:
            - Distance: Distant
            - Declaration of Friendship
          - Poland:
            - Distance: Far
            - Declaration of Friendship
        - Votes: 10
        
        ## Player 6
        - Civilization: Brazil
        - Leader: Pedro II
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Brazil) have both adopted the Autocracy Ideology. (999)
          - We are trade partners. (40)
          - We passed Indonesia's proposal in the United Nations. (36)
          - We are vassals of the same master! (31)
          - We have opened our borders to each other. (12)
          - You (Brazil) have denounced one of Indonesia's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - We have shared embassies. (1)
          - You (Brazil) have gone to war in the past.
          - Indonesia's real approach to Brazil is Friendly.
          - Religious differences strain your (Brazil) relationship. (-30)
          - Your (Brazil) spies were caught stealing from Indonesia. (-33)
          - Indonesia's leader has expressed a public opinion of Brazil (-50).
          - Indonesia's leader has formed a private opinion of Brazil (-60).
        - TheirOpinionOfUs:
          - We passed Brazil's proposal in the United Nations.
          - You (Indonesia) have both adopted the Autocracy Ideology.
          - Your (Indonesia) votes supported Brazil's civ's interests in the United Nations.
          - We fought together against a common foe.
          - We are vassals of the same master!
          - We are trade partners.
          - Brazil liked our proposal to the United Nations.
          - We have similar Social Policies.
          - Your (Indonesia) recent diplomatic actions please Brazil.
          - We have made Declarations of Friendship with the same leaders!
          - You (Indonesia) have denounced one of Brazil's declared enemies!
          - We have a Diplomat in Brazil's capital.
          - We have Pledged to Protect the same City-States.
          - We have made a public Declaration of Friendship!
          - We have opened our borders to each other.
          - Brazil's leader has expressed a public opinion of you (Indonesia) (10).
          - We have shared embassies.
          - We have different religious beliefs.
          - Brazil desire friendly relations with Indonesia.
          - You (Indonesia) plundered Brazil's trade routes!
        - Score: 2064
        - Era: Atomic
        - GoldenAge: 14 turns remaining
        - Technologies: 64
        - Cities: 4
        - Population: 105
        - Territory: 113
        - Gold: 8228
        - GoldPerTurn: 708
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 4126
        - TourismPerTurn: 723.92
        - CulturePerTurn: 1852
        - PolicyBranches:
          - Fealty: 1
          - Autocracy: 6
          - Tradition: 4
          - Artistry: 3
          - Statecraft: 6
          - Rationalism: 1
          - Industry: 2
          - Progress: 1
        - ResourcesAvailable:
          - Wheat: 4
          - Sheep: 7
          - Cloves: 1
          - Ivory: 1
          - Gold: 3
          - Nutmeg: 1
          - Paper: 8
          - Maize: 1
          - Gems: 1
          - Brazilwood: 4
          - Aluminum: 29
          - Lapis Lazuli: 1
          - Deer: 6
          - Whales: 1
          - Jade: 2
          - Iron: 2
          - Dyes: 1
          - Tea: 1
          - Coal: 2
          - Pepper: 1
          - Uranium: 3
          - Horses: 1
          - Coral: 1
          - Truffles: 1
          - Marble: 1
          - Tobacco: 1
        - FoundedReligion: Confucianism
        - Relationships:
          - The Shoshone:
            - Distance: Neighbors
            - Denounced Them
          - The Iroquois:
            - Distance: Neighbors
            - Our Master (Capitulated)
            - Open Borders
          - The Aztecs:
            - Distance: Distant
            - Declaration of Friendship
          - Indonesia:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - Poland:
            - Distance: Close
            - Open Borders
            - Declaration of Friendship
        - Votes: 26
        - 7: Defeated Major Civilization The Celts
        
        ## Player 22
        - Civilization: Prague
        - Leader: City State
        - MajorAlly: Indonesia
        - Population: 22
        - ResourcesAvailable:
          - Fish: 3
        - Relationships:
          - The Shoshone: Friends (Influence: 131, Distance: Far)
          - The Iroquois: Friends (Influence: 714, Distance: Neighbors, Protected)
          - The Aztecs: Neutral (Influence: 0, Distance: Close)
          - Indonesia: Ally (Influence: 1031, Distance: Neighbors, Protected)
          - Brazil: Friends (Influence: 139, Distance: Far, Protected)
          - Poland: Neutral (Influence: 0, Distance: Close)
        - Quests:
          - They want Hinduism to become the majority religion in their city. (Turns remaining: 28) Potential Quest Reward: * 202 Influence * 259 Faith
        - 23: Defeated Minor Civilization Palatium
        - 24: Defeated Minor Civilization Florence
        
        ## Player 25
        - Civilization: Belgrade
        - Leader: City State
        - MajorAlly: The Iroquois
        - Population: 17
        - Relationships:
          - The Shoshone: Friends (Influence: 109, Distance: Far)
          - The Iroquois: Ally (Influence: 660, Distance: Neighbors, Protected)
          - The Aztecs: Friends (Influence: 44, Distance: Close)
          - Indonesia: Friends (Influence: 434, Distance: Neighbors, Protected)
          - Brazil: Friends (Influence: 44, Distance: Far, Protected)
          - Poland: Friends (Influence: 60, Distance: Neighbors)
        - Quests:
          - They will reward the player(s) with the largest number of new Followers. So far, the leader has 7 new Followers and you have 1 (Turns remaining: 30) Potential Quest Reward: * 196 Influence * 172 Great Person Points in all Cities
          - They want Hinduism to become the majority religion in their city. (Turns remaining: 12) Potential Quest Reward: * 206 Influence * 262 Faith
          - They want you to generate a Great Admiral. (Turns remaining: 50) Potential Quest Reward: * 163 Influence * 315 Culture
        
        ## Player 26
        - Civilization: Raqmu
        - Leader: City State
        - MajorAlly: Brazil
        - Population: 25
        - ResourcesAvailable:
          - Fish: 2
          - Sheep: 1
        - Relationships:
          - The Shoshone: Friends (Influence: 154, Distance: Far)
          - The Iroquois: Friends (Influence: 755, Distance: Neighbors, Protected)
          - The Aztecs: Neutral (Influence: 0, Distance: Distant)
          - Indonesia: Friends (Influence: 203, Distance: Far, Protected)
          - Brazil: Ally (Influence: 885, Distance: Neighbors, Protected)
          - Poland: Neutral (Influence: 0, Distance: Distant)
        - Quests:
          - They will reward the player(s) with the largest number of new Followers. So far, the leader has 89 new Followers and you have 16 (Turns remaining: 13) Potential Quest Reward: * 199 Influence * 220 Great Person Points in all Cities
          - They want you to start a land or sea trade route to their city. (Turns remaining: 48) Potential Quest Reward: * 206 Influence * 256 Food in Capital
          - They want Hinduism to become the majority religion in their city. (Turns remaining: 22) Potential Quest Reward: * 189 Influence * 378 Faith
        
        ## Player 27
        - Civilization: Cape Town
        - Leader: City State
        - MajorAlly: Brazil
        - Population: 8
        - ResourcesAvailable:
          - Deer: 2
        - MajorityReligion: Confucianism
        - Relationships:
          - The Shoshone: Friends (Influence: 178, Distance: Close, Protected)
          - The Iroquois: Friends (Influence: 510, Distance: Close, Protected)
          - The Aztecs: Neutral (Influence: 0, Distance: Distant)
          - Indonesia: Friends (Influence: 473, Distance: Far, Protected)
          - Brazil: Ally (Influence: 942, Distance: Neighbors, Protected)
          - Poland: Friends (Influence: 236, Distance: Far)
        - Quests:
          - They will reward the player(s) with the largest number of new Followers. So far, the leader has 129 new Followers and you have 35 (Turns remaining: 2) Potential Quest Reward: * 226 Influence * 159 Great Person Points in all Cities
          - They want Hinduism to become the majority religion in their city. (Turns remaining: 48) Potential Quest Reward: * 233 Influence * 499 Faith
        - 28: Defeated Minor Civilization Djenne
        - 29: Defeated Minor Civilization Antananarivo
        - 30: Defeated Minor Civilization Sofia
        
        ## Player 31
        - Civilization: Zanzibar
        - Leader: City State
        - MajorAlly: Indonesia
        - Population: 27
        - ResourcesAvailable:
          - Fish: 3
        - MajorityReligion: Protestantism
        - Relationships:
          - The Shoshone: Neutral (Influence: -60, Distance: Distant)
          - The Iroquois: Neutral (Influence: -60, Distance: Neighbors)
          - The Aztecs: Neutral (Influence: -60, Distance: Distant)
          - Indonesia: Ally (Influence: 667, Distance: Far)
          - Brazil: Friends (Influence: 411, Distance: Far, Protected)
          - Poland: Neutral (Influence: -60, Distance: Distant)
        - Quests:
          - They will reward the player with the highest Tourism per turn. So far, the leader has 8,572 per turn and you have 953 per turn. (Turns remaining: 23) Potential Quest Reward: * 288 Influence * 369 Culture
          - They want you to start a land or sea trade route to their city. (Turns remaining: 6) Potential Quest Reward: * 173 Influence * 115 Food in Capital
        - 32: Defeated Minor Civilization Harappa
        
        ## Player 33
        - Civilization: Wittenberg
        - Leader: City State
        - MajorAlly: Indonesia
        - Population: 20
        - ResourcesAvailable:
          - Fish: 2
          - Deer: 1
          - Stone: 1
        - Relationships:
          - The Shoshone: Friends (Influence: 133, Distance: Distant)
          - The Iroquois: Friends (Influence: 766, Distance: Neighbors, Protected)
          - The Aztecs: Friends (Influence: 111, Distance: Far)
          - Indonesia: Ally (Influence: 656, Distance: Far, Protected)
          - Brazil: Friends (Influence: 136, Distance: Distant)
          - Poland: Friends (Influence: 50, Distance: Distant)
        - Quests:
          - They want you to generate a Great Musician. (Turns remaining: 16) Potential Quest Reward: * 150 Influence * 476 Culture
        
        ## Player 34
        - Civilization: Winchester
        - Leader: City State
        - MajorAlly: Indonesia
        - Population: 18
        - ResourcesAvailable:
          - Sheep: 2
        - Relationships:
          - The Shoshone: Friends (Influence: 100, Distance: Far)
          - The Iroquois: Friends (Influence: 602, Distance: Neighbors, Protected)
          - The Aztecs: Neutral (Influence: 0, Distance: Close)
          - Indonesia: Ally (Influence: 336, Distance: Close, Protected)
          - Brazil: Neutral (Influence: 10, Distance: Far, Protected)
          - Poland: Friends (Influence: 33, Distance: Far)
        - Quests:
          - They want you to generate a Great Artist. (Turns remaining: 41) Potential Quest Reward: * 144 Influence * 340 Culture
        - 35: Defeated Minor Civilization Ormus
        
        ## Player 36
        - Civilization: Sokoto
        - Leader: City State
        - MajorAlly: Brazil
        - Population: 10
        - ResourcesAvailable:
          - Deer: 1
        - MajorityReligion: Confucianism
        - Relationships:
          - The Shoshone: Friends (Influence: 60, Distance: Close)
          - The Iroquois: Friends (Influence: 623, Distance: Close, Protected)
          - The Aztecs: Neutral (Influence: 0, Distance: Distant)
          - Indonesia: Friends (Influence: 213, Distance: Far, Protected)
          - Brazil: Ally (Influence: 867, Distance: Neighbors, Protected)
          - Poland: Friends (Influence: 262, Distance: Far)
        - Quests:
          - They will reward the player that discovers the most technologies. So far, the leader has 8 Technologies and you have 3. (Turns remaining: 8) Potential Quest Reward: * 153 Influence * 1,088 Tourism with all known Civilizations
          - They want you to generate a Great Writer. (Turns remaining: 45) Potential Quest Reward: * 173 Influence * 323 Culture
        - 37: Defeated Minor Civilization Oviedo
        - 63: Barbarians
        
        # Cities
        Cities: summary reports about discovered cities in the world.
        
        ## Player: The Shoshone
        
        ### Moson Kahni
        - ID: 1057
        - X: 66
        - Y: 46
        - Population: 38
        - MajorityReligion: Confucianism
        - DefenseStrength: 76
        - Wonders:
          - Heroic Epic
          - National Monument
          - Circus Maximus
          - Ironworks
          - Brandenburg Gate
          - Statue of Liberty
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
          - International Finance Center
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
        
        ### Te-Moak
        - ID: 1278
        - X: 67
        - Y: 41
        - Population: 31
        - MajorityReligion: Confucianism
        - DefenseStrength: 72
        - IsCoastal: true
        - Wonders:
          - Chartered Company
          - Imperial College
          - Louvre
        
        ### Goshute
        - ID: 1535
        - X: 59
        - Y: 40
        - Population: 29
        - MajorityReligion: Confucianism
        - DefenseStrength: 74
        - Wonders:
          - School of Philosophy
          - Sistine Chapel
          - Grand Temple
          - Summer Palace
        
        ### Washakie
        - ID: 2258
        - X: 68
        - Y: 49
        - Population: 31
        - MajorityReligion: Confucianism
        - DefenseStrength: 66
        - IsCoastal: true
        - Wonders:
          - Royal Collection
          - Nalanda
        
        ## Player: The Iroquois
        
        ### Onondaga
        - ID: 1058
        - X: 13
        - Y: 32
        - Population: 53
        - MajorityReligion: Protestantism
        - DefenseStrength: 118
        - Wonders:
          - Heroic Epic
          - Chartered Company
          - Ironworks
          - Royal Collection
          - Notre Dame
          - Eiffel Tower
          - Pentagon
          - Temple of Artemis
          - CN Tower
          - Terracotta Army
          - International Space Station
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
          - Karlstejn
          - Grand Canal
          - Menin Gate
          - United Nations
          - Consulate
          - Celestial Throne
          - TwoKay Foods Headquarters
        
        ### Osininka
        - ID: 1205
        - X: 10
        - Y: 27
        - Population: 37
        - MajorityReligion: Protestantism
        - DefenseStrength: 112
        - IsCoastal: true
        - Wonders:
          - Imperial College
        
        ### Grand River
        - ID: 1466
        - X: 14
        - Y: 25
        - Population: 42
        - MajorityReligion: Protestantism
        - DefenseStrength: 107
        - Wonders:
          - Circus Maximus
        
        ### Akwesasme
        - ID: 1557
        - X: 13
        - Y: 40
        - Population: 29
        - MajorityReligion: Protestantism
        - DefenseStrength: 115
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - National Monument
        
        ### Buffalo Creek
        - ID: 1633
        - X: 15
        - Y: 43
        - Population: 32
        - MajorityReligion: Protestantism
        - DefenseStrength: 107
        - IsCoastal: true
        - Wonders:
          - Sydney Opera House
        
        ### Brantford
        - ID: 1814
        - X: 8
        - Y: 31
        - Population: 34
        - MajorityReligion: Protestantism
        - DefenseStrength: 113
        - IsCoastal: true
        - Wonders:
          - Petra
          - Grand Temple
        
        ### Montreal
        - ID: 2233
        - X: 16
        - Y: 34
        - Population: 34
        - MajorityReligion: Protestantism
        - DefenseStrength: 105
        - IsCoastal: true
        
        ### Genesse River
        - ID: 2963
        - X: 22
        - Y: 34
        - Population: 33
        - MajorityReligion: Protestantism
        - DefenseStrength: 107
        - IsCoastal: true
        
        ### Canandaigua Lake
        - ID: 3048
        - X: 17
        - Y: 19
        - Population: 36
        - MajorityReligion: Protestantism
        - DefenseStrength: 81
        - IsCoastal: true
        
        ### Lake Simcoe
        - ID: 3599
        - X: 9
        - Y: 39
        - Population: 33
        - MajorityReligion: Protestantism
        - DefenseStrength: 118
        - IsCoastal: true
        
        ### Tokyo
        - ID: 3602
        - X: 18
        - Y: 37
        - Population: 32
        - MajorityReligion: Protestantism
        - DefenseStrength: 113
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Prora
          - Hall of Honor
        
        ### Salamanca
        - ID: 3993
        - X: 12
        - Y: 13
        - Population: 37
        - MajorityReligion: Protestantism
        - DefenseStrength: 113
        - IsCoastal: true
        
        ### Osaka
        - ID: 4339
        - X: 19
        - Y: 43
        - Population: 29
        - MajorityReligion: Protestantism
        - DefenseStrength: 112
        - IsOccupied: true
        - IsCoastal: true
        
        ### Kyoto
        - ID: 4525
        - X: 23
        - Y: 41
        - Population: 36
        - MajorityReligion: Protestantism
        - DefenseStrength: 120
        - IsOccupied: true
        - IsCoastal: true
        
        ### Gowanda
        - ID: 5480
        - X: 21
        - Y: 49
        - Population: 26
        - MajorityReligion: Protestantism
        - DefenseStrength: 111
        - IsCoastal: true
        - Wonders:
          - Red Fort
        
        ### Buffalo
        - ID: 6850
        - X: 35
        - Y: 15
        - Population: 33
        - MajorityReligion: Protestantism
        - DefenseStrength: 115
        - IsCoastal: true
        
        ### Djenne
        - ID: 7520
        - X: 19
        - Y: 29
        - Population: 38
        - MajorityReligion: Protestantism
        - DefenseStrength: 112
        - IsOccupied: true
        - IsCoastal: true
        
        ### Antananarivo
        - ID: 7900
        - X: 8
        - Y: 35
        - Population: 29
        - MajorityReligion: Protestantism
        - DefenseStrength: 131
        - IsOccupied: true
        - IsCoastal: true
        
        ### Nagoya
        - ID: 8026
        - X: 32
        - Y: 33
        - Population: 31
        - MajorityReligion: Protestantism
        - DefenseStrength: 107
        - IsOccupied: true
        - IsCoastal: true
        
        ### Nara
        - ID: 8094
        - X: 30
        - Y: 39
        - Population: 27
        - MajorityReligion: Protestantism
        - DefenseStrength: 112
        - IsOccupied: true
        - IsCoastal: true
        
        ### Satsuma
        - ID: 8095
        - X: 24
        - Y: 46
        - Population: 28
        - MajorityReligion: Protestantism
        - DefenseStrength: 118
        - IsOccupied: true
        - IsCoastal: true
        
        ### Cuba
        - ID: 8329
        - X: 37
        - Y: 3
        - Population: 27
        - MajorityReligion: Protestantism
        - DefenseStrength: 109
        - IsCoastal: true
        
        ### Kagoshima
        - ID: 8516
        - X: 30
        - Y: 44
        - Population: 36
        - MajorityReligion: Protestantism
        - DefenseStrength: 118
        - IsOccupied: true
        - IsCoastal: true
        
        ### Ormus
        - ID: 8582
        - X: 29
        - Y: 48
        - Population: 23
        - MajorityReligion: Protestantism
        - DefenseStrength: 110
        - IsOccupied: true
        
        ### Izumo
        - ID: 9332
        - X: 34
        - Y: 41
        - Population: 27
        - MajorityReligion: Protestantism
        - DefenseStrength: 133
        - IsOccupied: true
        - IsCoastal: true
        
        ### Nagasaki
        - ID: 9528
        - X: 35
        - Y: 37
        - Population: 31
        - MajorityReligion: Protestantism
        - DefenseStrength: 112
        - IsOccupied: true
        - IsCoastal: true
        
        ### Yokohama
        - ID: 9784
        - X: 36
        - Y: 29
        - Population: 30
        - MajorityReligion: Protestantism
        - DefenseStrength: 125
        - IsOccupied: true
        - IsCoastal: true
        
        ### Sao Paulo
        - ID: 10133
        - X: 48
        - Y: 36
        - Population: 29
        - MajorityReligion: Confucianism
        - DefenseStrength: 121
        - IsOccupied: true
        - IsCoastal: true
        
        ### Salvador
        - ID: 10189
        - X: 46
        - Y: 41
        - Population: 25
        - DefenseStrength: 121
        - IsOccupied: true
        - IsCoastal: true
        
        ### Brasilia
        - ID: 10639
        - X: 49
        - Y: 31
        - Population: 36
        - DefenseStrength: 112
        - IsOccupied: true
        - IsCoastal: true
        
        ### Curitiba
        - ID: 10693
        - X: 40
        - Y: 47
        - Population: 25
        - MajorityReligion: Protestantism
        - DefenseStrength: 109
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Hubble Space Telescope
        
        ### Sofia
        - ID: 12264
        - X: 33
        - Y: 47
        - Population: 27
        - MajorityReligion: Protestantism
        - DefenseStrength: 118
        - IsOccupied: true
        - IsCoastal: true
        
        ### Timbisha
        - ID: 12265
        - X: 75
        - Y: 23
        - Population: 29
        - DefenseStrength: 112
        - IsOccupied: true
        - IsCoastal: true
        
        ### Surabaya
        - ID: 12603
        - X: 54
        - Y: 24
        - Population: 34
        - DefenseStrength: 124
        - IsOccupied: true
        - IsCoastal: true
        
        ### Harappa
        - ID: 12881
        - X: 41
        - Y: 24
        - Population: 31
        - MajorityReligion: Protestantism
        - DefenseStrength: 112
        - IsOccupied: true
        - IsCoastal: true
        
        ### Palatium
        - ID: 13442
        - X: 71
        - Y: 18
        - Population: 28
        - DefenseStrength: 110
        - IsOccupied: true
        - IsCoastal: true
        
        ### Warsaw
        - ID: 13793
        - X: 68
        - Y: 25
        - Population: 34
        - DefenseStrength: 118
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Machu Picchu
          - National Intelligence Agency
          - Roman Forum
          - The Motherland Calls
        
        ### Lodz
        - ID: 13871
        - X: 66
        - Y: 31
        - Population: 27
        - DefenseStrength: 117
        - IsOccupied: true
        - IsCoastal: true
        
        ### Pohokwi
        - ID: 14219
        - X: 68
        - Y: 36
        - Population: 28
        - MajorityReligion: Confucianism
        - DefenseStrength: 119
        - IsOccupied: true
        - IsCoastal: true
        
        ### Wroclaw
        - ID: 14489
        - X: 64
        - Y: 35
        - Population: 23
        - MajorityReligion: Confucianism
        - DefenseStrength: 124
        - IsOccupied: true
        - IsCoastal: true
        
        ### Shimonoseki
        - ID: 15148
        - X: 42
        - Y: 14
        - Population: 27
        - MajorityReligion: Protestantism
        - DefenseStrength: 110
        - IsOccupied: true
        - IsCoastal: true
        
        ### Florence
        - ID: 15152
        - X: 61
        - Y: 34
        - Population: 17
        - DefenseStrength: 123
        - IsOccupied: true
        - IsCoastal: true
        
        ### Oviedo
        - ID: 15221
        - X: 54
        - Y: 30
        - Population: 24
        - MajorityReligion: Confucianism
        - DefenseStrength: 108
        - IsOccupied: true
        
        ### Xochicalco
        - ID: 15472
        - X: 49
        - Y: 11
        - Population: 27
        - DefenseStrength: 112
        - IsOccupied: true
        - IsCoastal: true
        
        ### Tzintzuntzen
        - ID: 16501
        - X: 38
        - Y: 10
        - Population: 16
        - MajorityReligion: Protestantism
        - DefenseStrength: 107
        - IsOccupied: true
        - IsCoastal: true
        
        ### Atzcapotzalco
        - ID: 16573
        - X: 34
        - Y: 8
        - Population: 22
        - MajorityReligion: Protestantism
        - DefenseStrength: 115
        - IsOccupied: true
        - IsCoastal: true
        
        ### Calixtlahuaca
        - ID: 16575
        - X: 55
        - Y: 12
        - Population: 26
        - DefenseStrength: 118
        - IsOccupied: true
        - IsCoastal: true
        
        ### Denpasar
        - ID: 16647
        - X: 42
        - Y: 4
        - Population: 25
        - DefenseStrength: 108
        - IsOccupied: true
        - IsCoastal: true
        
        ### Tlacopan
        - ID: 17061
        - X: 42
        - Y: 10
        - Population: 17
        - DefenseStrength: 105
        - IsPuppet: true
        - IsCoastal: true
        
        ### Agaidika
        - ID: 17415
        - X: 63
        - Y: 39
        - Population: 22
        - MajorityReligion: Confucianism
        - DefenseStrength: 118
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Himeji Castle
        
        ### Tlaxcala
        - ID: 17417
        - X: 61
        - Y: 15
        - Population: 29
        - DefenseStrength: 127
        - IsOccupied: true
        - Wonders:
          - Forbidden Palace
        
        ### Truro
        - ID: 17908
        - X: 73
        - Y: 14
        - Population: 15
        - MajorityReligion: Buddhism
        - DefenseStrength: 128
        - IsPuppet: true
        - IsCoastal: true
        
        ### Cork
        - ID: 17909
        - X: 11
        - Y: 3
        - Population: 16
        - MajorityReligion: Buddhism
        - DefenseStrength: 122
        - IsPuppet: true
        - IsCoastal: true
        
        ### Cardiff
        - ID: 18221
        - X: 74
        - Y: 10
        - Population: 20
        - MajorityReligion: Buddhism
        - DefenseStrength: 122
        - IsPuppet: true
        - IsCoastal: true
        
        ### Nantes
        - ID: 18609
        - X: 72
        - Y: 3
        - Population: 17
        - MajorityReligion: Buddhism
        - DefenseStrength: 78
        - IsPuppet: true
        
        ### Edinburgh
        - ID: 18706
        - X: 70
        - Y: 7
        - Population: 24
        - MajorityReligion: Buddhism
        - DefenseStrength: 92
        - IsOccupied: true
        - Wonders:
          - Great Library
          - Pyramids
          - Great Wall
          - Angkor Wat
        
        ## Player: Indonesia
        
        ### Jakarta
        - ID: 1059
        - X: 58
        - Y: 25
        - Population: 38
        - MajorityReligion: Hinduism
        - DefenseStrength: 108
        - IsCoastal: true
        - FoodStored: 2501
        - FoodPerTurn: 313
        - ProductionPerTurn: 375
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 1008
        - SciencePerTurn: 828
        - CulturePerTurn: 774
        - FaithPerTurn: 95
        - TourismPerTurn: 329.5
        - HappinessDelta: 24
        - BuildingCount: 57
        - ImportantBuildings:
          - Seaport
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Constabulary
          - Candi
          - Writers' Guild
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Mine Field
          - Refinery
        - Wonders:
          - Heroic Epic
          - National Monument
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Imperial College
          - Great Lighthouse
          - Colossus
          - Porcelain Tower
          - Palace of Westminster
          - Mausoleum of Halicarnassus
          - University of Sankore
          - Grand Temple
          - Scrivener's Office
          - Printing Press
          - Hall of Honor
          - Soho Foundry
          - Empire State Building
          - Consulate
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
          - Apostolic Palace
          - Firaxite Materials Headquarters
        - GreatWorkCount: 16
        
        ### Medan
        - ID: 1882
        - X: 60
        - Y: 29
        - Population: 32
        - MajorityReligion: Hinduism
        - DefenseStrength: 93
        - FoodStored: 2257
        - FoodPerTurn: 29
        - ProductionStored: 736
        - ProductionPerTurn: 452
        - CurrentProduction: Ambassador
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 321
        - SciencePerTurn: 200
        - CulturePerTurn: 292
        - FaithPerTurn: 28
        - TourismPerTurn: 257.25
        - HappinessDelta: 22
        - BuildingCount: 58
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Constabulary
          - Candi
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Refinery
        - Wonders:
          - Royal Collection
          - Cristo Redentor
          - Foreign Bureau
        - GreatWorkCount: 11
        
        ### Makassar
        - ID: 2071
        - X: 62
        - Y: 24
        - Population: 31
        - DefenseStrength: 80
        - FoodStored: 1814
        - FoodPerTurn: 8
        - ProductionStored: 624
        - ProductionPerTurn: 475
        - CurrentProduction: Ambassador
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 212
        - SciencePerTurn: 260
        - CulturePerTurn: 203
        - FaithPerTurn: 43
        - TourismPerTurn: 180
        - HappinessDelta: 24
        - BuildingCount: 55
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Arsenal
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Constabulary
          - Candi
          - Writers' Guild
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Coaling Station
          - Wire Service
          - Refinery
        - Wonders:
          - Hagia Sophia
        - GreatWorkCount: 7
        
        ### Batam
        - ID: 2537
        - X: 58
        - Y: 32
        - Population: 29
        - MajorityReligion: Hinduism
        - DefenseStrength: 112
        - FoodStored: 1692
        - FoodPerTurn: 24
        - ProductionPerTurn: 309
        - CurrentProduction: Infinite Project: Arts
        - GoldPerTurn: 207
        - SciencePerTurn: 286
        - CulturePerTurn: 270
        - FaithPerTurn: 17
        - TourismPerTurn: 135.5
        - HappinessDelta: 27
        - BuildingCount: 55
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Constabulary
          - Candi
          - Writers' Guild
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Coaling Station
          - Wire Service
          - Refinery
        - Wonders:
          - School of Philosophy
        - GreatWorkCount: 6
        
        ### Tlatelolco
        - ID: 17138
        - X: 66
        - Y: 15
        - Population: 24
        - DefenseStrength: 95
        - IsOccupied: true
        - FoodStored: 1224
        - FoodPerTurn: 30
        - ProductionStored: 0
        - ProductionPerTurn: 300
        - CurrentProduction: Broadcast Tower
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 216
        - SciencePerTurn: 175
        - CulturePerTurn: 105
        - FaithPerTurn: 20
        - TourismPerTurn: 51.5
        - HappinessDelta: 11
        - BuildingCount: 45
        - ImportantBuildings:
          - Courthouse
          - Water Mill
          - Windmill
          - Customs House
          - Arena
          - Temple
          - Opera House
          - Museum
          - Barracks
          - Military Base
          - Medical Lab
          - Workshop
          - Stock Exchange
          - Library
          - Public School
          - Candi
          - Hotel
          - Caravansary
          - Agribusiness
          - Coaling Station
          - Wire Service
        - GreatWorkCount: 4
        
        ### Dublin
        - ID: 18435
        - X: 69
        - Y: 11
        - Population: 3
        - MajorityReligion: Buddhism
        - DefenseStrength: 27
        - IsOccupied: true
        - FoodStored: 0
        - FoodPerTurn: 0
        - ProductionStored: 0
        - ProductionPerTurn: 0
        - CurrentProduction: Herbalist
        - ProductionTurnsLeft: 3801
        - GoldPerTurn: 0
        - SciencePerTurn: 0
        - CulturePerTurn: 0
        - FaithPerTurn: 0
        - TourismPerTurn: 0
        - HappinessDelta: -3
        - RazingTurns: 3
        - BuildingCount: 14
        - ImportantBuildings:
          - Customs House
          - Museum
          - Granary
          - Stock Exchange
          - Shrine
          - Candi
          - Caravansary
          - Council
        - GreatWorkCount: 4
        
        ### Douglas
        - ID: 18731
        - X: 67
        - Y: 3
        - Population: 5
        - MajorityReligion: Buddhism
        - DefenseStrength: 44
        - IsOccupied: true
        - FoodStored: 67
        - FoodPerTurn: 0
        - ProductionStored: 0
        - ProductionPerTurn: 0
        - CurrentProduction: Barracks
        - ProductionTurnsLeft: 6501
        - GoldPerTurn: 0
        - SciencePerTurn: 0
        - CulturePerTurn: 0
        - FaithPerTurn: 0
        - TourismPerTurn: 0
        - HappinessDelta: -5
        - RazingTurns: 5
        - BuildingCount: 17
        - ImportantBuildings:
          - Forge
          - Customs House
          - Opera House
          - Granary
          - Bank
          - Shrine
          - Caravansary
          - Council
          - Gallery
        - GreatWorkCount: 1
        
        ## Player: Poland
        
        ### Krakow
        - ID: 15755
        - X: 64
        - Y: 27
        - Population: 21
        - MajorityReligion: Confucianism
        - DefenseStrength: 54
        - Wonders:
          - National Monument
          - Leaning Tower of Pisa
        
        ## Player: The Aztecs
        
        ### Tenochtitlan
        - ID: 1062
        - X: 63
        - Y: 10
        - Population: 33
        - MajorityReligion: Catholicism
        - DefenseStrength: 68
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Circus Maximus
          - Imperial College
          - Oracle
          - Borobudur
          - Printing Press
          - Foreign Bureau
          - Huey Teocalli
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
        
        ### Teotihuacan
        - ID: 1285
        - X: 65
        - Y: 6
        - Population: 29
        - MajorityReligion: Catholicism
        - DefenseStrength: 75
        - Wonders:
          - Ironworks
          - Scrivener's Office
        
        ### Texcoco
        - ID: 2369
        - X: 58
        - Y: 9
        - Population: 25
        - DefenseStrength: 73
        - IsCoastal: true
        - Wonders:
          - Chartered Company
          - Royal Collection
          - Alhambra
        
        ## Player: Brazil
        
        ### Rio de Janeiro
        - ID: 1081
        - X: 52
        - Y: 39
        - Population: 31
        - MajorityReligion: Confucianism
        - DefenseStrength: 76
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Chartered Company
          - Imperial College
          - Royal Collection
          - Stonehenge
          - Hanging Gardens
          - Chichen Itza
          - Statue of Zeus
          - Neuschwanstein
          - Grand Temple
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
          - State Treasury
          - Royal Guardhouse
          - Royal Astrologer
          - Holy Council
          - Civilized Jewelers Headquarters
        
        ### Fortaleza
        - ID: 2149
        - X: 49
        - Y: 44
        - Population: 25
        - MajorityReligion: Confucianism
        - DefenseStrength: 68
        - Wonders:
          - Circus Maximus
          - Uffizi
        
        ### Belo Horizonte
        - ID: 2415
        - X: 55
        - Y: 44
        - Population: 23
        - MajorityReligion: Confucianism
        - DefenseStrength: 65
        - Wonders:
          - Globe Theatre
        
        ### Manaus
        - ID: 2924
        - X: 53
        - Y: 35
        - Population: 26
        - MajorityReligion: Confucianism
        - DefenseStrength: 72
        - Wonders:
          - Ironworks
          - Taj Mahal
          - Hall of Honor
        
        ## Player: City-States
        
        ### Prague
        - ID: 1064
        - X: 59
        - Y: 18
        - Population: 22
        - DefenseStrength: 108
        - IsCoastal: true
        
        ### Belgrade
        - ID: 1067
        - X: 64
        - Y: 20
        - Population: 17
        - DefenseStrength: 82
        
        ### Raqmu
        - ID: 1068
        - X: 47
        - Y: 48
        - Population: 25
        - DefenseStrength: 104
        - IsCoastal: true
        
        ### Cape Town
        - ID: 1069
        - X: 59
        - Y: 49
        - Population: 8
        - MajorityReligion: Confucianism
        - DefenseStrength: 101
        
        ### Zanzibar
        - ID: 1073
        - X: 38
        - Y: 33
        - Population: 27
        - MajorityReligion: Protestantism
        - DefenseStrength: 92
        - IsCoastal: true
        
        ### Wittenberg
        - ID: 1075
        - X: 8
        - Y: 4
        - Population: 20
        - DefenseStrength: 93
        - IsCoastal: true
        
        ### Winchester
        - ID: 1076
        - X: 53
        - Y: 18
        - Population: 18
        - DefenseStrength: 107
        
        ### Sokoto
        - ID: 1078
        - X: 52
        - Y: 49
        - Population: 10
        - MajorityReligion: Confucianism
        - DefenseStrength: 96
        
        # Military
        Military: summary reports about tactical zones and visible units.
        
        ## Unit Stats
        - Attack:
          - Mercenary:
            - Strength: 66
        - CityBombard:
          - Rocket Artillery:
            - Strength: 37
            - RangedStrength: 75
          - Artillery:
            - Strength: 27
            - RangedStrength: 50
          - Cannon:
            - Strength: 11
            - RangedStrength: 29
          - Field Gun:
            - Strength: 17
            - RangedStrength: 40
        - FastAttack:
          - Modern Armor:
            - Strength: 100
          - Tank:
            - Strength: 75
          - Commando:
            - Strength: 32
        - Defense:
          - Mechanized Infantry:
            - Strength: 80
          - Infantry:
            - Strength: 62
          - Fusilier:
            - Strength: 38
          - Rifleman:
            - Strength: 50
        - Counter:
          - Mobile SAM:
            - Strength: 55
          - Anti-Aircraft Gun:
            - Strength: 40
        - Ranged:
          - Light Tank:
            - Strength: 58
            - RangedStrength: 52
          - Musketman:
            - Strength: 21
            - RangedStrength: 30
          - Machine Gun:
            - Strength: 45
            - RangedStrength: 58
          - Bazooka:
            - Strength: 60
            - RangedStrength: 80
        - AttackSea:
          - Destroyer:
            - Strength: 70
          - Fleet Destroyer:
            - Strength: 80
        - AssaultSea:
          - Missile Cruiser:
            - Strength: 75
            - RangedStrength: 80
          - Dreadnought:
            - Strength: 50
            - RangedStrength: 65
        - AttackAir:
          - Heavy Bomber:
            - RangedStrength: 65
          - Bomber:
            - RangedStrength: 50
        - DefenseAir:
          - Jet Fighter:
            - RangedStrength: 70
          - Zero:
            - RangedStrength: 60
          - Triplane:
            - RangedStrength: 45
        - Paradrop:
          - Paratrooper:
            - Strength: 42
          - Special Forces:
            - Strength: 65
          - XCOM Squad:
            - Strength: 75
        
        ## Neutral Land Zone 1057
        - ZoneValue: 42
        - Dominance: Friendly
        - NeutralStrength: 76
        - FriendlyStrength: 3425
        - City: Moson Kahni
        - AreaID: 5
        - Plots: 28
        - CenterX: 65
        - CenterY: 46
        - Units:
          - The Shoshone:
            - Triplane: 1
            - Bomber: 1
            - Machine Gun: 1
        
        ## Friendly Land Zone 1059
        - ZoneValue: 3
        - Dominance: Friendly
        - FriendlyStrength: 11772
        - City: Jakarta
        - AreaID: 19
        - Plots: 17
        - CenterX: 58
        - CenterY: 25
        - Units:
          - Indonesia:
            - Tank: 1
            - Artillery: 5
            - Anti-Aircraft Gun: 2
            - Triplane: 2
            - Bomber: 4
            - Machine Gun: 1
        - Neighbors:
          - 12603
          - 15221
          - -1064
          - 1882
          - 2071
        
        ## Neutral Land Zone 1062
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 68
        - FriendlyStrength: 12308
        - City: Tenochtitlan
        - AreaID: 16
        - Plots: 21
        - CenterX: 63
        - CenterY: 10
        - Units:
          - The Aztecs:
            - Paratrooper: 4
            - Artillery: 1
            - Infantry: 2
            - Rifleman: 1
            - Machine Gun: 1
        - Neighbors:
          - 1285
          - 17417
          - 17138
          - 18435
        
        ## Neutral Land Zone 1064
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 108
        - FriendlyStrength: 11656
        - City: Prague
        - AreaID: 19
        - Plots: 23
        - CenterX: 59
        - CenterY: 18
        - Units:
          - City-State Prague:
            - Tank: 1
            - Machine Gun: 1
          - The Iroquois:
            - Light Tank: 1
            - Machine Gun: 1
            - Mercenary: 1
        - Neighbors:
          - 1076
          - -1064
          - 17417
          - 2071
          - 1067
        
        ## Neutral Land Zone 1067
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 82
        - FriendlyStrength: 12189
        - City: Belgrade
        - AreaID: 5
        - Plots: 31
        - CenterX: 64
        - CenterY: 20
        - Units:
          - The Iroquois:
            - Mobile SAM: 2
            - Infantry: 3
          - Indonesia:
            - Infantry: 4
          - City-State Belgrade:
            - Artillery: 1
            - Infantry: 3
        - Neighbors:
          - 1064
          - 2071
          - 17417
          - 17138
          - 15755
          - 13442
        
        ## Neutral Land Zone 1068
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 105
        - FriendlyStrength: 5412
        - City: Raqmu
        - AreaID: 5
        - Plots: 10
        - CenterX: 48
        - CenterY: 49
        - Units:
          - City-State Raqmu:
            - Tank: 1
            - Infantry: 1
          - Indonesia:
            - Tank: 1
        - Neighbors:
          - -1068
          - 2149
        
        ## Neutral Land Zone 1073
        - ZoneValue: 48
        - Dominance: Friendly
        - NeutralStrength: 93
        - FriendlyStrength: 9846
        - City: Zanzibar
        - AreaID: 59
        - Plots: 5
        - CenterX: 38
        - CenterY: 32
        - Units:
          - City-State Zanzibar:
            - Modern Armor: 1
            - Infantry: 1
            - Machine Gun: 2
        - Neighbors:
          - -9784
          - -1073
          - 9784
        
        ## Neutral Land Zone 1075
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 93
        - FriendlyStrength: 4361
        - City: Wittenberg
        - AreaID: 1
        - Plots: 21
        - CenterX: 7
        - CenterY: 4
        - Units:
          - City-State Wittenberg:
            - Infantry: 4
            - Rifleman: 1
            - Machine Gun: 5
            - Dreadnought: 1
          - The Iroquois:
            - Infantry: 1
        - Neighbors:
          - -1075
        
        ## Neutral Land Zone 1076
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 108
        - FriendlyStrength: 6929
        - City: Winchester
        - AreaID: 22
        - Plots: 24
        - CenterX: 53
        - CenterY: 18
        - Units:
          - City-State Winchester:
            - Tank: 1
            - Light Tank: 1
            - Infantry: 1
          - The Iroquois:
            - Mercenary: 1
        - Neighbors:
          - 12603
          - 1064
          - -1064
        
        ## Neutral Land Zone 1285
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 76
        - FriendlyStrength: 10137
        - City: Teotihuacan
        - AreaID: 8
        - Plots: 24
        - CenterX: 65
        - CenterY: 7
        - Units:
          - The Aztecs:
            - Light Tank: 1
            - Infantry: 1
            - Rifleman: 1
            - Machine Gun: 5
          - The Iroquois:
            - Mobile SAM: 1
        - Neighbors:
          - 1062
          - 18731
          - 18435
          - 18706
        
        ## Neutral Land Zone 1535
        - ZoneValue: 36
        - Dominance: Friendly
        - NeutralStrength: 74
        - FriendlyStrength: 10947
        - City: Goshute
        - AreaID: 5
        - Plots: 33
        - CenterX: 59
        - CenterY: 40
        - Units:
          - The Shoshone:
            - Paratrooper: 1
            - Rifleman: 1
        - Neighbors:
          - 2924
          - 2415
          - 2537
          - 15152
        
        ## Friendly Land Zone 1882
        - ZoneValue: 36
        - Dominance: Friendly
        - FriendlyStrength: 14545
        - City: Medan
        - AreaID: 5
        - Plots: 17
        - CenterX: 60
        - CenterY: 29
        - Units:
          - Indonesia:
            - Anti-Aircraft Gun: 4
            - Machine Gun: 4
        - Neighbors:
          - 1059
          - 2537
          - 2071
          - 15755
          - 15152
          - -15755
        
        ## Friendly Land Zone 2071
        - ZoneValue: 36
        - Dominance: Friendly
        - FriendlyStrength: 9997
        - City: Makassar
        - AreaID: 5
        - Plots: 17
        - CenterX: 61
        - CenterY: 24
        - Units:
          - Indonesia:
            - Artillery: 1
            - Infantry: 2
            - Special Forces: 2
            - Machine Gun: 1
        - Neighbors:
          - 1059
          - 1064
          - 1067
          - 1882
          - 15755
        
        ## Neutral Land Zone 2149
        - ZoneValue: 15
        - Dominance: Friendly
        - NeutralStrength: 68
        - FriendlyStrength: 9247
        - City: Fortaleza
        - AreaID: 55
        - Plots: 25
        - CenterX: 49
        - CenterY: 44
        - Units:
          - Brazil:
            - Infantry: 1
            - Machine Gun: 2
          - City-State Raqmu:
            - Infantry: 2
          - City-State Sokoto:
            - Infantry: 1
        - Neighbors:
          - -1068
          - 1068
          - 2415
        
        ## Neutral Land Zone 2415
        - ZoneValue: 30
        - Dominance: Friendly
        - NeutralStrength: 65
        - FriendlyStrength: 7869
        - City: Belo Horizonte
        - AreaID: 5
        - Plots: 34
        - CenterX: 55
        - CenterY: 44
        - Units:
          - The Shoshone:
            - Rifleman: 1
          - Indonesia:
            - Artillery: 1
          - Brazil:
            - Artillery: 1
            - Anti-Aircraft Gun: 1
            - Machine Gun: 2
        - Neighbors:
          - 2149
          - 1535
        
        ## Friendly Land Zone 2537
        - ZoneValue: 36
        - Dominance: Friendly
        - FriendlyStrength: 14265
        - City: Batam
        - AreaID: 5
        - Plots: 20
        - CenterX: 58
        - CenterY: 32
        - Units:
          - Indonesia:
            - Tank: 2
            - Artillery: 1
            - Anti-Aircraft Gun: 2
            - Triplane: 3
            - Bomber: 3
            - Machine Gun: 4
          - The Iroquois:
            - Mobile SAM: 1
        - Neighbors:
          - 15221
          - 2924
          - 15152
          - 1535
          - 1882
        
        ## Neutral Land Zone 2924
        - ZoneValue: 60
        - Dominance: Friendly
        - NeutralStrength: 72
        - FriendlyStrength: 11362
        - City: Manaus
        - AreaID: 55
        - Plots: 25
        - CenterX: 54
        - CenterY: 35
        - Units:
          - Brazil:
            - Anti-Aircraft Gun: 1
            - Triplane: 2
            - Machine Gun: 4
          - Indonesia:
            - Anti-Aircraft Gun: 1
            - Machine Gun: 1
        - Neighbors:
          - 10639
          - 15221
          - 2537
          - 1535
        
        ## Neutral Land Zone 9528
        - ZoneValue: 21
        - Dominance: Friendly
        - NeutralStrength: 113
        - FriendlyStrength: 9156
        - City: Nagasaki
        - AreaID: 79
        - Plots: 14
        - CenterX: 35
        - CenterY: 37
        - Units:
          - The Iroquois:
            - Modern Armor: 1
            - Rocket Artillery: 1
        - Neighbors:
          - -1073
        
        ## Neutral Land Zone 9784
        - ZoneValue: 24
        - Dominance: Friendly
        - NeutralStrength: 126
        - FriendlyStrength: 8630
        - City: Yokohama
        - AreaID: 59
        - Plots: 6
        - CenterX: 37
        - CenterY: 29
        - Units:
          - City-State Zanzibar:
            - Infantry: 1
          - The Iroquois:
            - Modern Armor: 1
            - Mechanized Infantry: 1
            - Heavy Bomber: 3
            - Zero: 5
            - Machine Gun: 1
        - Neighbors:
          - -9784
          - 1073
          - -1073
        
        ## Neutral Land Zone 10639
        - ZoneValue: 24
        - Dominance: Friendly
        - NeutralStrength: 113
        - FriendlyStrength: 5794
        - City: Brasilia
        - AreaID: 54
        - Plots: 16
        - CenterX: 49
        - CenterY: 30
        - Units:
          - The Iroquois:
            - Heavy Bomber: 3
            - Infantry: 1
        - Neighbors:
          - 2924
        
        ## Neutral Land Zone 12603
        - ZoneValue: 96
        - Dominance: Friendly
        - NeutralStrength: 125
        - FriendlyStrength: 7950
        - City: Surabaya
        - AreaID: 19
        - Plots: 14
        - CenterX: 54
        - CenterY: 23
        - Units:
          - The Iroquois:
            - Jet Fighter: 3
            - Rocket Artillery: 1
            - Heavy Bomber: 3
            - Zero: 1
            - Infantry: 1
            - Machine Gun: 1
            - Bazooka: 1
            - XCOM Squad: 1
        - Neighbors:
          - 1076
          - 1059
        
        ## Neutral Land Zone 13442
        - ZoneValue: 84
        - Dominance: Friendly
        - NeutralStrength: 111
        - FriendlyStrength: 9063
        - City: Palatium
        - AreaID: 5
        - Plots: 18
        - CenterX: 69
        - CenterY: 18
        - Units:
          - Indonesia:
            - Infantry: 1
          - The Iroquois:
            - Mobile SAM: 1
            - Heavy Bomber: 3
            - Zero: 4
            - Infantry: 1
            - Machine Gun: 1
            - Mercenary: 1
        - Neighbors:
          - 1067
          - 17138
          - 17908
        
        ## Neutral Land Zone 13871
        - ZoneValue: 42
        - Dominance: Friendly
        - NeutralStrength: 118
        - FriendlyStrength: 8707
        - City: Lodz
        - AreaID: 5
        - Plots: 14
        - CenterX: 66
        - CenterY: 30
        - Units:
          - The Iroquois:
            - Infantry: 1
            - Machine Gun: 1
        - Neighbors:
          - -15755
          - 15755
        
        ## Neutral Land Zone 15152
        - ZoneValue: 60
        - Dominance: Friendly
        - NeutralStrength: 124
        - FriendlyStrength: 13549
        - City: Florence
        - AreaID: 5
        - Plots: 17
        - CenterX: 60
        - CenterY: 34
        - Units:
          - The Shoshone:
            - Machine Gun: 1
          - The Iroquois:
            - Rocket Artillery: 1
            - Mechanized Infantry: 1
            - Zero: 5
            - Light Tank: 2
            - Infantry: 1
            - Machine Gun: 3
        - Neighbors:
          - 2537
          - 1535
          - -15152
          - 1882
        
        ## Neutral Land Zone 15221
        - ZoneValue: 30
        - Dominance: Friendly
        - NeutralStrength: 109
        - FriendlyStrength: 10660
        - City: Oviedo
        - AreaID: 55
        - Plots: 23
        - CenterX: 54
        - CenterY: 30
        - Units:
          - Indonesia:
            - Anti-Aircraft Gun: 1
          - The Iroquois:
            - Mobile SAM: 1
            - Heavy Bomber: 5
            - Zero: 3
        - Neighbors:
          - 2924
          - 2537
          - 1059
        
        ## Neutral Land Zone 15755
        - ZoneValue: 48
        - Dominance: Friendly
        - NeutralStrength: 54
        - FriendlyStrength: 10592
        - City: Krakow
        - AreaID: 5
        - Plots: 19
        - CenterX: 64
        - CenterY: 27
        - Units:
          - Poland:
            - Fusilier: 1
            - Cannon: 1
            - Musketman: 8
            - Field Gun: 1
            - Commando: 1
          - Indonesia:
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - 1882
          - 2071
          - -15755
          - 13871
          - 1067
        
        ## Friendly Land Zone 17138
        - ZoneValue: 30
        - Dominance: Friendly
        - FriendlyStrength: 15394
        - City: Tlatelolco
        - AreaID: 5
        - Plots: 24
        - CenterX: 66
        - CenterY: 15
        - Units:
          - The Aztecs:
            - Paratrooper: 1
          - The Iroquois:
            - Infantry: 1
          - Indonesia:
            - Paratrooper: 1
            - Artillery: 2
            - Anti-Aircraft Gun: 3
            - Infantry: 1
            - Special Forces: 1
            - Triplane: 1
            - Bomber: 1
            - Machine Gun: 2
        - Neighbors:
          - 17417
          - 1062
          - 1067
          - 18435
          - 13442
          - 17908
        
        ## Neutral Land Zone 17417
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 127
        - FriendlyStrength: 12329
        - City: Tlaxcala
        - AreaID: 19
        - Plots: 24
        - CenterX: 61
        - CenterY: 14
        - Units:
          - Indonesia:
            - Anti-Aircraft Gun: 1
            - Infantry: 1
          - The Iroquois:
            - Mobile SAM: 1
            - Rocket Artillery: 4
            - Heavy Bomber: 3
            - Zero: 3
            - Infantry: 1
            - Machine Gun: 1
            - XCOM Squad: 1
        - Neighbors:
          - 1064
          - 1062
          - 1067
          - 17138
        
        ## Neutral Land Zone 17908
        - ZoneValue: 48
        - Dominance: Friendly
        - NeutralStrength: 128
        - FriendlyStrength: 9446
        - City: Truro
        - AreaID: 5
        - Plots: 12
        - CenterX: 72
        - CenterY: 14
        - Units:
          - The Iroquois:
            - Mechanized Infantry: 1
            - Heavy Bomber: 2
            - Zero: 5
            - Infantry: 1
        - Neighbors:
          - 18435
          - 17138
          - 13442
          - 18221
        
        ## Neutral Land Zone 18221
        - ZoneValue: 24
        - Dominance: Friendly
        - NeutralStrength: 122
        - FriendlyStrength: 10338
        - City: Cardiff
        - AreaID: 5
        - Plots: 15
        - CenterX: 73
        - CenterY: 9
        - Units:
          - The Iroquois:
            - Mechanized Infantry: 1
            - Heavy Bomber: 4
            - Zero: 1
        - Neighbors:
          - 18706
          - 18435
          - 17908
          - 18609
        
        ## Friendly Land Zone 18435
        - ZoneValue: 6
        - Dominance: Friendly
        - FriendlyStrength: 14803
        - City: Dublin
        - AreaID: 5
        - Plots: 25
        - CenterX: 69
        - CenterY: 11
        - Units:
          - The Aztecs:
            - Infantry: 1
          - The Iroquois:
            - Mobile SAM: 1
          - Indonesia:
            - Paratrooper: 1
            - Artillery: 1
            - Anti-Aircraft Gun: 2
            - Infantry: 1
            - Special Forces: 1
            - Machine Gun: 4
        - Neighbors:
          - 1062
          - 1285
          - 17138
          - 18706
          - 17908
          - 18221
        
        ## Neutral Land Zone 18609
        - ZoneValue: 60
        - Dominance: Friendly
        - NeutralStrength: 79
        - FriendlyStrength: 9014
        - City: Nantes
        - AreaID: 5
        - Plots: 19
        - CenterX: 73
        - CenterY: 4
        - Units:
          - The Iroquois:
            - Jet Fighter: 5
            - Mechanized Infantry: 1
            - XCOM Squad: 4
        - Neighbors:
          - 18731
          - 18706
          - 18221
        
        ## Neutral Land Zone 18706
        - ZoneValue: 84
        - Dominance: Friendly
        - NeutralStrength: 92
        - FriendlyStrength: 13679
        - City: Edinburgh
        - AreaID: 5
        - Plots: 19
        - CenterX: 71
        - CenterY: 7
        - Units:
          - The Iroquois:
            - Jet Fighter: 1
            - Mobile SAM: 1
            - Rocket Artillery: 1
            - Heavy Bomber: 1
            - Zero: 3
            - XCOM Squad: 6
        - Neighbors:
          - 1285
          - 18731
          - 18435
          - 18609
          - 18221
        
        ## Friendly Land Zone 18731
        - ZoneValue: 6
        - Dominance: Friendly
        - FriendlyStrength: 9288
        - City: Douglas
        - AreaID: 5
        - Plots: 18
        - CenterX: 67
        - CenterY: 3
        - Units:
          - The Aztecs:
            - Paratrooper: 1
          - Indonesia:
            - Tank: 1
            - Triplane: 2
        - Neighbors:
          - 1285
          - 18706
          - 18609
        
        ## Neutral Sea Zone -1073
        - ZoneValue: 16
        - Dominance: Friendly
        - NeutralStrength: 93
        - FriendlyStrength: 9351
        - City: Zanzibar
        - AreaID: 0
        - Plots: 46
        - CenterX: 40
        - CenterY: 34
        - Units:
          - Brazil:
            - Tank: 1
            - Infantry: 1
          - The Iroquois:
            - Missile Cruiser: 1
            - Modern Armor: 1
            - Fleet Destroyer: 3
          - City-State Zanzibar:
            - Destroyer: 1
          - Poland:
            - Fusilier: 3
        - Neighbors:
          - -9784
          - 9528
          - 1073
          - 9784
        
        ## Neutral Sea Zone -9784
        - ZoneValue: 8
        - Dominance: Friendly
        - NeutralStrength: 126
        - FriendlyStrength: 8385
        - City: Yokohama
        - AreaID: 0
        - Plots: 38
        - CenterX: 35
        - CenterY: 28
        - Units:
          - City-State Zanzibar:
            - Destroyer: 1
          - The Iroquois:
            - Fleet Destroyer: 1
        - Neighbors:
          - 9784
          - -1073
          - 1073
        
        ## Neutral Sea Zone -15152
        - ZoneValue: 20
        - Dominance: Friendly
        - NeutralStrength: 124
        - FriendlyStrength: 8226
        - City: Florence
        - AreaID: 65
        - Plots: 6
        - CenterX: 62
        - CenterY: 34
        - Units:
          - The Iroquois:
            - Missile Cruiser: 2
        - Neighbors:
          - 15152
        
        ## Neutral Sea Zone -1064
        - ZoneValue: 1
        - Dominance: Friendly
        - NeutralStrength: 108
        - FriendlyStrength: 6128
        - City: Prague
        - AreaID: 33
        - Plots: 12
        - CenterX: 58
        - CenterY: 19
        - Units:
          - City-State Prague:
            - Destroyer: 2
          - Indonesia:
            - Fleet Destroyer: 2
        - Neighbors:
          - 1064
          - 1076
          - 1059
        
        ## Neutral Sea Zone -1068
        - ZoneValue: 6
        - Dominance: Friendly
        - NeutralStrength: 105
        - FriendlyStrength: 4242
        - City: Raqmu
        - AreaID: 0
        - Plots: 31
        - CenterX: 46
        - CenterY: 49
        - Units:
          - City-State Raqmu:
            - Destroyer: 2
        - Neighbors:
          - 2149
          - 1068
        
        ## Neutral Sea Zone -1075
        - ZoneValue: 1
        - Dominance: Friendly
        - NeutralStrength: 93
        - FriendlyStrength: 2910
        - City: Wittenberg
        - AreaID: 0
        - Plots: 44
        - CenterX: 6
        - CenterY: 5
        - Units:
          - City-State Wittenberg:
            - Dreadnought: 1
        - Neighbors:
          - 1075
        
        ## Neutral Sea Zone -15755
        - ZoneValue: 16
        - Dominance: Friendly
        - NeutralStrength: 54
        - FriendlyStrength: 5394
        - City: Krakow
        - AreaID: 51
        - Plots: 3
        - CenterX: 64
        - CenterY: 27
        - Units:
          - Poland:
            - Fusilier: 1
        - Neighbors:
          - 1882
          - 15755
          - 13871
        
        # Events
        Events: events since you last made a decision.
        
        ## Turn 424
        
        ### 0
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Diplomat
          - ID: 18987
        - Player: 3: Poland
        - Grass Land 64,27:
          - Owner: Poland
          - CityID: 15755
          - Population: 21
          - IsRiver: true
          - City: Krakow
          - Resource: Cloves
          - Religion: Confucianism
          - Route: Railroad
        
        ### 1
        - Type: UnitCreated
        - UnitType: Diplomat
        - Player: 3: Poland
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 18987
        - Grass Land 64,27:
          - Owner: Poland
          - CityID: 15755
          - Population: 21
          - IsRiver: true
          - City: Krakow
          - Resource: Cloves
          - Religion: Confucianism
          - Route: Railroad
        
        ### 2
        - Type: CityTrained
        - WithGold: true
        - Player: 3: Poland
        - City:
          - Name: Krakow
          - Population: 21
          - ID: 15755
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 18987
        
        ### 3
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Fusilier
          - ID: 18988
        - Player: 3: Poland
        - Grass Land 64,27:
          - Owner: Poland
          - CityID: 15755
          - Population: 21
          - IsRiver: true
          - City: Krakow
          - Resource: Cloves
          - Religion: Confucianism
          - Route: Railroad
        
        ### 4
        - Type: UnitCreated
        - UnitType: Fusilier
        - Player: 3: Poland
        - Unit:
          - Level: 1
          - AI: Defense
          - Unit: Fusilier
          - ID: 18988
        - Grass Land 64,27:
          - Owner: Poland
          - CityID: 15755
          - Population: 21
          - IsRiver: true
          - City: Krakow
          - Resource: Cloves
          - Religion: Confucianism
          - Route: Railroad
        
        ### 5
        - Type: CityTrained
        - Player: 3: Poland
        - City:
          - Name: Krakow
          - Population: 21
          - ID: 15755
        - Unit:
          - Level: 1
          - AI: Defense
          - Unit: Fusilier
          - ID: 18988
        
        ### 6
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18018
        - Player: 3: Poland
        - Plots:
          - Grass Hills 63,26:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 63,27:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Academy
          - Grass Land 64,27:
            - Owner: Poland
            - CityID: 15755
            - Population: 21
            - IsRiver: true
            - City: Krakow
            - Resource: Cloves
            - Religion: Confucianism
            - Route: Railroad
        
        ### 7
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18500
        - Player: 3: Poland
        - Plots:
          - Grass Land 60,29:
            - Owner: Indonesia
            - CityID: 1882
            - Population: 32
            - IsRiver: true
            - City: Medan
            - Route: Railroad
          - Grass Land 61,29:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 62,29:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Town
            - Route: Road
          - Plains Land 63,28:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Oil
            - Improvement: Holy Site
            - Route: Railroad
        
        ### 8
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18665
        - Player: 3: Poland
        - Plots:
          - Grass Land 62,25:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Hills 63,26:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 63,27:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Academy
          - Grass Land 64,27:
            - Owner: Poland
            - CityID: 15755
            - Population: 21
            - IsRiver: true
            - City: Krakow
            - Resource: Cloves
            - Religion: Confucianism
            - Route: Railroad
        
        ### 9
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18825
        - Player: 3: Poland
        - Grass Land 64,27:
          - Owner: Poland
          - CityID: 15755
          - Population: 21
          - IsRiver: true
          - City: Krakow
          - Resource: Cloves
          - Religion: Confucianism
          - Route: Railroad
        
        ### 10
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: Defense
          - Unit: Fusilier
          - ID: 18968
        - Player: 3: Poland
        - Promotions:
          - Drill I
          - Shock I
          - Shock II
        
        ### 11
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: Defense
          - Unit: Fusilier
          - ID: 18988
        - Player: 3: Poland
        - Promotions:
          - Shock I
          - Shock II
          - Medic I
        
        ### 12
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Diplomat
          - Unit: Great Diplomat
          - ID: 17639
        - Player: 3: Poland
        
        ### 13
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Fusilier
          - ID: 18736
        - Player: 3: Poland
        
        ### 14
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Fusilier
          - ID: 18793
        - Player: 3: Poland
        - Plots:
          - Grass Land 63,25:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Pepper
            - Improvement: Plantation
            - Route: Railroad
          - Grass Hills 64,24:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Nutmeg
            - Improvement: Plantation
            - Route: Railroad
          - Grass Hills 64,25:
            - Owner: Poland
            - IsRiver: true
            - Resource: Marble
            - Improvement: Quarry
        
        ### 15
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Fusilier
          - ID: 18988
        - Player: 3: Poland
        - Coast 64,26:
          - Owner: Poland
        
        ### 16
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Machine Gun
          - ID: 18989
        - Player: 5: The Aztecs
        - Plains Land 63,10:
          - Owner: The Aztecs
          - CityID: 1062
          - Population: 33
          - IsRiver: true
          - City: Tenochtitlan
          - Religion: Catholicism
          - Route: Railroad
        
        ### 17
        - Type: UnitCreated
        - UnitType: Machine Gun
        - Player: 5: The Aztecs
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 18989
        - Plains Land 63,10:
          - Owner: The Aztecs
          - CityID: 1062
          - Population: 33
          - IsRiver: true
          - City: Tenochtitlan
          - Religion: Catholicism
          - Route: Railroad
        
        ### 18
        - Type: CityTrained
        - Player: 5: The Aztecs
        - City:
          - Name: Tenochtitlan
          - Population: 33
          - ID: 1062
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 18989
        
        ### 19
        - Type: SetPopulation
        - OldPopulation: 28
        - NewPopulation: 29
        - City:
          - Owner: The Aztecs
          - CityID: 1285
          - Population: 29
          - IsRiver: true
          - City: Teotihuacan
          - Terrain: Grass
          - Route: Railroad
          - Plot: Land
          - X: 65
          - Y: 6
        
        ### 20
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18026
        - Player: 5: The Aztecs
        - Plains Land 63,10:
          - Owner: The Aztecs
          - CityID: 1062
          - Population: 33
          - IsRiver: true
          - City: Tenochtitlan
          - Religion: Catholicism
          - Route: Railroad
        
        ### 21
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18444
        - Player: 5: The Aztecs
        - Plots:
          - Grass Land 65,15:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Cloves
            - Improvement: Plantation
            - Route: Railroad
          - Desert Land 66,16:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 66,17:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 66,18:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
        
        ### 22
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18179
        - Player: 5: The Aztecs
        - Plains Land 63,10:
          - Owner: The Aztecs
          - CityID: 1062
          - Population: 33
          - IsRiver: true
          - City: Tenochtitlan
          - Religion: Catholicism
          - Route: Railroad
        
        ### 23
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18180
        - Player: 5: The Aztecs
        - Plots:
          - Plains Land 64,11:
            - Owner: The Aztecs
            - Resource: Cotton
            - Improvement: Manufactory
            - Route: Railroad
          - Plains Land 64,10:
            - Owner: The Aztecs
            - IsRiver: true
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 63,9:
            - Owner: The Aztecs
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 64,8:
            - Owner: The Aztecs
            - Improvement: Farm
            - Route: Railroad
        
        ### 24
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18392
        - Player: 5: The Aztecs
        - Plots:
          - Plains Land 66,14:
            - Owner: Indonesia
            - IsRiver: true
          - Plains Land 65,13:
            - Owner: Indonesia
            - Resource: Wheat
            - Improvement: Academy
            - Route: Railroad
          - Plains Hills 64,13:
            - Owner: The Aztecs
            - Resource: Aluminum
            - Improvement: Town
            - Route: Railroad
          - Plains Land 64,12:
            - Owner: The Aztecs
            - Improvement: Fort
            - Route: Railroad
        
        ### 25
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17769
        - Player: 5: The Aztecs
        - Plots:
          - Grass Land 62,14:
            - Owner: The Iroquois
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
          - Plains Hills 62,13:
            - Owner: The Aztecs
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 63,12:
            - Owner: The Aztecs
            - Resource: Cotton
            - Improvement: Manufactory
            - Route: Railroad
          - Desert Land 63,11:
            - Owner: The Aztecs
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 63,10:
            - Owner: The Aztecs
            - CityID: 1062
            - Population: 33
            - IsRiver: true
            - City: Tenochtitlan
            - Religion: Catholicism
            - Route: Railroad
        
        ### 26
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 18989
        - Player: 5: The Aztecs
        - Promotions:
          - Barrage I
          - Barrage II
          - Barrage III
          - Range
        
        ### 27
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Merchant
          - Unit: Great Merchant
          - ID: 18667
        - Player: 5: The Aztecs
        - Coast 60,18:
          - Owner: City-State Prague
          - Resource: Fish
          - Improvement: Fishing Boats
        
        ### 28
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 18252
        - Player: 5: The Aztecs
        - Plots:
          - Desert Hills 65,12:
            - Owner: The Aztecs
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 65,11:
            - Owner: The Aztecs
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 66,11:
            - Owner: The Aztecs
            - Resource: Horses
            - Improvement: Pasture
        
        ### 29
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 9623
        - Player: 5: The Aztecs
        - Plots:
          - Desert Hills 65,10:
            - Owner: The Aztecs
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 64,10:
            - Owner: The Aztecs
            - IsRiver: true
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 63,10:
            - Owner: The Aztecs
            - CityID: 1062
            - Population: 33
            - IsRiver: true
            - City: Tenochtitlan
            - Religion: Catholicism
            - Route: Railroad
        
        ### 30
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Missionary
          - Unit: Missionary
          - ID: 18964
        - Player: 5: The Aztecs
        - Plots:
          - Plains Hills 63,9:
            - Owner: The Aztecs
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 64,8:
            - Owner: The Aztecs
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 64,7:
            - Owner: The Aztecs
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Farm
            - Route: Railroad
        
        ### 31
        - Type: CityConvertsReligion
        - City:
          - Owner: The Aztecs
          - CityID: 1285
          - Population: 29
          - IsRiver: true
          - City: Teotihuacan
          - Terrain: Grass
          - Religion: Catholicism
          - Route: Railroad
          - Plot: Land
          - X: 65
          - Y: 6
        - Owner: 5: The Aztecs
        - Religion: Catholicism
        
        ### 32
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 18951
        - Player: 5: The Aztecs
        - Plots:
          - Plains Land 65,9:
            - Owner: The Aztecs
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Hills 65,10:
            - Owner: The Aztecs
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 64,11:
            - Owner: The Aztecs
            - Resource: Cotton
            - Improvement: Manufactory
            - Route: Railroad
          - Plains Land 64,12:
            - Owner: The Aztecs
            - Improvement: Fort
            - Route: Railroad
        
        ### 33
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Ambassador
          - ID: 18993
        - Player: 6: Brazil
        - Grass Land 53,35:
          - Owner: Brazil
          - CityID: 2924
          - Population: 26
          - IsRiver: true
          - City: Manaus
          - Resource: Horses
          - Religion: Confucianism
          - Route: Railroad
        
        ### 34
        - Type: UnitCreated
        - UnitType: Ambassador
        - Player: 6: Brazil
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 18993
        - Grass Land 53,35:
          - Owner: Brazil
          - CityID: 2924
          - Population: 26
          - IsRiver: true
          - City: Manaus
          - Resource: Horses
          - Religion: Confucianism
          - Route: Railroad
        
        ### 35
        - Type: CityTrained
        - WithGold: true
        - Player: 6: Brazil
        - City:
          - Name: Manaus
          - Population: 26
          - ID: 2924
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 18993
        
        ### 36
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18935
        - Player: 6: Brazil
        - Plots:
          - Desert Land 66,16:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Grass Hills 66,15:
            - Owner: Indonesia
            - CityID: 17138
            - Population: 24
            - IsRiver: true
            - City: Tlatelolco
            - Route: Railroad
          - Plains Hills 67,14:
            - Owner: Indonesia
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 67,13:
            - Owner: Indonesia
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 68,12:
            - Owner: Indonesia
            - Resource: Bison
            - Improvement: Camp
          - Plains Land 68,11:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Oppidum
            - Route: Railroad
          - Desert Land 69,10:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 68,9:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Oppidum
            - Route: Railroad
          - Desert Hills 69,8:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
        
        ### 37
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18677
        - Player: 6: Brazil
        - Plots:
          - Grass Land 61,25:
            - Owner: Indonesia
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 62,24:
            - Owner: Indonesia
            - CityID: 2071
            - Population: 31
            - IsRiver: true
            - City: Makassar
            - Resource: Iron
            - Route: Railroad
          - Grass Hills 62,23:
            - Owner: Indonesia
            - IsRiver: true
            - Route: Railroad
          - Plains Hills 63,22:
            - Owner: Indonesia
            - Resource: Aluminum
            - Improvement: Holy Site
            - Route: Railroad
          - Plains Land 63,21:
            - Owner: City-State Belgrade
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Desert Hills 64,20:
            - Owner: City-State Belgrade
            - CityID: 1067
            - Population: 17
            - City: Belgrade
            - Route: Railroad
          - Desert Hills 63,19:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 63,18:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
        
        ### 38
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18242
        - Player: 6: Brazil
        - Plots:
          - Plains Land 62,17:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 62,16:
            - Owner: The Iroquois
            - Improvement: Farm
            - Route: Railroad
          - Grass Hills 61,15:
            - Owner: The Iroquois
            - CityID: 17417
            - Population: 28
            - IsRiver: true
            - City: Tlaxcala
            - Resource: Deer
            - Route: Railroad
          - Desert Land 63,18:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 63,19:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 64,20:
            - Owner: City-State Belgrade
            - CityID: 1067
            - Population: 17
            - City: Belgrade
            - Route: Railroad
          - Plains Land 63,21:
            - Owner: City-State Belgrade
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 63,22:
            - Owner: Indonesia
            - Resource: Aluminum
            - Improvement: Holy Site
            - Route: Railroad
        
        ### 39
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18512
        - Player: 6: Brazil
        - Plots:
          - Grass Hills 57,28:
            - Owner: Indonesia
            - Resource: Sheep
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Land 57,27:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Nutmeg
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Hills 58,26:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 59,26:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Hills 59,25:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 60,25:
            - Owner: Indonesia
            - Improvement: Village
            - Route: Railroad
          - Grass Land 61,25:
            - Owner: Indonesia
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 62,24:
            - Owner: Indonesia
            - CityID: 2071
            - Population: 31
            - IsRiver: true
            - City: Makassar
            - Resource: Iron
            - Route: Railroad
          - Grass Hills 62,23:
            - Owner: Indonesia
            - IsRiver: true
            - Route: Railroad
          - Plains Hills 63,22:
            - Owner: Indonesia
            - Resource: Aluminum
            - Improvement: Holy Site
            - Route: Railroad
        
        ### 40
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18626
        - Player: 6: Brazil
        - Plots:
          - Grass Hills 59,25:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 59,26:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Hills 58,26:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 57,27:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Nutmeg
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Hills 57,28:
            - Owner: Indonesia
            - Resource: Sheep
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Hills 56,29:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Plains Land 56,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
          - Grass Land 55,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 54,30:
            - Owner: The Iroquois
            - CityID: 15221
            - Population: 24
            - IsRiver: true
            - City: Oviedo
            - Religion: Confucianism
            - Route: Railroad
        
        ### 41
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18185
        - Player: 6: Brazil
        - Plots:
          - Plains Hills 56,37:
            - Owner: The Shoshone
            - Resource: Deer
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 57,37:
            - Owner: The Shoshone
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 58,37:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Manufactory
            - Route: Railroad
          - Plains Hills 59,37:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 60,37:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Mountain Mountain 61,38:
            - Owner: The Iroquois
            - Route: Railroad
        
        ### 42
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18243
        - Player: 6: Brazil
        - Plots:
          - Grass Land 61,29:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Hills 61,30:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Gems
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 60,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 59,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
          - Grass Land 58,30:
            - Owner: Indonesia
            - Resource: Oil
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Land 57,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 56,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
          - Grass Land 55,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 54,30:
            - Owner: The Iroquois
            - CityID: 15221
            - Population: 24
            - IsRiver: true
            - City: Oviedo
            - Religion: Confucianism
            - Route: Railroad
        
        ### 43
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18780
        - Player: 6: Brazil
        - Plots:
          - Desert Hills 52,33:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Landmark
            - Route: Railroad
          - Desert Land 53,32:
            - Owner: The Iroquois
            - IsRiver: true
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 53,31:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 54,30:
            - Owner: The Iroquois
            - CityID: 15221
            - Population: 24
            - IsRiver: true
            - City: Oviedo
            - Religion: Confucianism
            - Route: Railroad
          - Grass Land 55,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 56,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
          - Grass Hills 56,29:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Hills 57,28:
            - Owner: Indonesia
            - Resource: Sheep
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Land 57,27:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Nutmeg
            - Improvement: Holy Site
            - Route: Railroad
        
        ### 44
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18801
        - Player: 6: Brazil
        - Plots:
          - Plains Land 56,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
          - Grass Hills 56,29:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Hills 57,28:
            - Owner: Indonesia
            - Resource: Sheep
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Land 57,27:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Nutmeg
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Hills 58,26:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 59,26:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Hills 59,25:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 60,25:
            - Owner: Indonesia
            - Improvement: Village
            - Route: Railroad
          - Grass Land 61,25:
            - Owner: Indonesia
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
        
        ### 45
        - Type: CityEventChoiceActivated
        - City:
          - Name: Moson Kahni
          - Population: 38
          - ID: 1057
        - Player: 0: The Shoshone
        - Choice: 83
        
        ### 46
        - Type: EspionageResult
        - SpyResult: Detected
        - SourcePlayer: 6: Brazil
        - TargetPlayer: 0: The Shoshone
        - City:
          - Owner: The Shoshone
          - CityID: 1057
          - Population: 38
          - IsRiver: true
          - City: Moson Kahni
          - Terrain: Tundra
          - Religion: Confucianism
          - Route: Railroad
          - Plot: Land
          - X: 66
          - Y: 46
        
        ### 47
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Diplomat
          - Unit: Great Diplomat
          - ID: 18906
        - Player: 6: Brazil
        - Plots:
          - Grass Hills 39,32:
            - Owner: City-State Zanzibar
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 38,33:
            - Owner: City-State Zanzibar
            - CityID: 1073
            - Population: 26
            - City: Zanzibar
            - Resource: Glass
            - Religion: Protestantism
            - Route: Railroad
        
        ### 48
        - Type: SetAlly
        - NewAllyPlayer: 6: Brazil
        - OldAllyPlayer: 2: Indonesia
        - MinorPlayer: 31
        
        ### 49
        - Type: GreatPersonExpended
        - Player: 6: Brazil
        - City:
          - Owner: City-State Zanzibar
          - CityID: 1073
          - Population: 26
          - City: Zanzibar
          - Terrain: Grass
          - Resource: Glass
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 38
          - Y: 33
        - Unit:
          - Level: 1
          - AI: Diplomat
          - Unit: Great Diplomat
          - ID: 18906
        - GreatPerson: 168
        
        ### 50
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Defense
          - Unit: Infantry
          - ID: 18253
        - Player: 6: Brazil
        - Plots:
          - Desert Land 53,34:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
          - Grass Land 53,35:
            - Owner: Brazil
            - CityID: 2924
            - Population: 26
            - IsRiver: true
            - City: Manaus
            - Resource: Horses
            - Religion: Confucianism
            - Route: Railroad
        
        ### 51
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 18871
        - Player: 6: Brazil
        - Plots:
          - Desert Land 48,34:
            - Owner: The Iroquois
            - Improvement: Fort
            - Route: Railroad
          - Desert Land 47,33:
            - Owner: The Iroquois
            - Resource: Wheat
            - Improvement: Farm
            - Route: Railroad
          - Coast 46,33:
            - Owner: The Iroquois
        
        ### 52
        - Type: CityConstructed
        - City:
          - Name: Prague
          - Population: 22
          - ID: 1064
        - Owner: 22
        - Building: Stadium
        
        ### 53
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 18129
        - Player: 26
        - Plains Land 48,46:
          - Owner: City-State Raqmu
          - IsRiver: true
          - Improvement: Farm
          - Route: Railroad
        
        ### 54
        - Type: SetPopulation
        - OldPopulation: 26
        - NewPopulation: 27
        - City:
          - Owner: City-State Zanzibar
          - CityID: 1073
          - Population: 27
          - City: Zanzibar
          - Terrain: Grass
          - Resource: Glass
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 38
          - Y: 33
        
        ### 55
        - Type: CityConvertsReligion
        - City:
          - Owner: City-State Zanzibar
          - CityID: 1073
          - Population: 27
          - City: Zanzibar
          - Terrain: Grass
          - Resource: Glass
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 38
          - Y: 33
        - Owner: 31
        - Religion: Protestantism
        
        ### 56
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Musketman
          - ID: 18995
        - Player: 3: Poland
        - Grass Land 64,27:
          - Owner: Poland
          - CityID: 15755
          - Population: 21
          - IsRiver: true
          - City: Krakow
          - Resource: Cloves
          - Religion: Confucianism
          - Route: Railroad
        
        ### 57
        - Type: UnitCreated
        - UnitType: Musketman
        - Player: 3: Poland
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Musketman
          - ID: 18995
        - Grass Land 64,27:
          - Owner: Poland
          - CityID: 15755
          - Population: 21
          - IsRiver: true
          - City: Krakow
          - Resource: Cloves
          - Religion: Confucianism
          - Route: Railroad
        
        ### 58
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Musketman
          - ID: 18995
        - Player: 3: Poland
        - Grass Hills 66,26:
          - Owner: Poland
          - IsRiver: true
          - Resource: Sheep
          - Improvement: Pasture
        
        ## Turn 425
        
        ### 0
        - Type: CityConvertsReligion
        - City:
          - Owner: The Iroquois
          - CityID: 17909
          - Population: 16
          - City: Cork
          - Terrain: Tundra
          - Resource: Uranium
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 11
          - Y: 3
        - Owner: 1: The Iroquois
        - Religion: Buddhism
        
        ### 1
        - Type: CityConvertsReligion
        - City:
          - Owner: The Iroquois
          - CityID: 18221
          - Population: 20
          - IsRiver: true
          - City: Cardiff
          - Terrain: Desert
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 74
          - Y: 10
        - Owner: 1: The Iroquois
        - Religion: Buddhism
        
        ### 2
        - Type: CityConvertsReligion
        - City:
          - Owner: Indonesia
          - CityID: 1059
          - Population: 38
          - IsRiver: true
          - City: Jakarta
          - Terrain: Grass
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Land
          - X: 58
          - Y: 25
        - Owner: 2: Indonesia
        - Religion: Hinduism
        
        ### 3
        - Type: CityConvertsReligion
        - City:
          - Owner: Indonesia
          - CityID: 1059
          - Population: 38
          - IsRiver: true
          - City: Jakarta
          - Terrain: Grass
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Land
          - X: 58
          - Y: 25
        - Owner: 2: Indonesia
        - Religion: Hinduism
        
        ### 4
        - Type: CityConvertsReligion
        - City:
          - Owner: Indonesia
          - CityID: 2537
          - Population: 29
          - IsRiver: true
          - City: Batam
          - Terrain: Grass
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Land
          - X: 58
          - Y: 32
        - Owner: 2: Indonesia
        - Religion: Hinduism
        
        ### 5
        - Type: CityConvertsReligion
        - City:
          - Owner: City-State Raqmu
          - CityID: 1068
          - Population: 25
          - City: Raqmu
          - Terrain: Tundra
          - Religion: Confucianism
          - Route: Railroad
          - Plot: Land
          - X: 47
          - Y: 48
        - Owner: 26
        - Religion: Confucianism
        
        ### 6
        - Type: ResolutionResult
        - Decision: 25
        - Passed: true
        - ProposerPlayer: 2: Indonesia
        - Resolution: Open Door
        
        ### 7
        - Type: CityConvertsReligion
        - City:
          - Owner: The Shoshone
          - CityID: 1535
          - Population: 29
          - IsRiver: true
          - City: Goshute
          - Terrain: Plains
          - Religion: Confucianism
          - Route: Railroad
          - Plot: Land
          - X: 59
          - Y: 40
        - Owner: 0: The Shoshone
        - Religion: Confucianism
        
        ### 8
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18308
        - Player: 0: The Shoshone
        - Tundra Land 66,46:
          - Owner: The Shoshone
          - CityID: 1057
          - Population: 38
          - IsRiver: true
          - City: Moson Kahni
          - Religion: Confucianism
          - Route: Railroad
        
        ### 9
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18419
        - Player: 0: The Shoshone
        - Tundra Land 66,46:
          - Owner: The Shoshone
          - CityID: 1057
          - Population: 38
          - IsRiver: true
          - City: Moson Kahni
          - Religion: Confucianism
          - Route: Railroad
        
        ### 10
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18473
        - Player: 0: The Shoshone
        - Tundra Land 66,46:
          - Owner: The Shoshone
          - CityID: 1057
          - Population: 38
          - IsRiver: true
          - City: Moson Kahni
          - Religion: Confucianism
          - Route: Railroad
        
        ### 11
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18475
        - Player: 0: The Shoshone
        - Tundra Land 66,46:
          - Owner: The Shoshone
          - CityID: 1057
          - Population: 38
          - IsRiver: true
          - City: Moson Kahni
          - Religion: Confucianism
          - Route: Railroad
        
        ### 12
        - Type: UnitBuildCompleted
        - Owner: 0: The Shoshone
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1705
        - Build: Construct a Fort
        - Desert Hills 59,38:
          - Owner: The Shoshone
          - IsRiver: true
          - Route: Railroad
        
        ### 13
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4521
        - Player: 0: The Shoshone
        - Plains Hills 57,37:
          - Owner: The Shoshone
          - Improvement: Mine
          - Route: Railroad
        
        ### 14
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Rifleman
          - ID: 18873
        - Player: 0: The Shoshone
        - Desert Hills 59,38:
          - Owner: The Shoshone
          - IsRiver: true
          - Route: Railroad
        
        ### 15
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 18878
        - Player: 0: The Shoshone
        - Plots:
          - Ocean 40,33:
            - Owner: City-State Zanzibar
          - Ocean 41,33:
            - Owner: City-State Zanzibar
        
        ### 16
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 18911
        - Player: 0: The Shoshone
        - Plots:
          - Plains Hills 61,37:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Citadel
            - Route: Railroad
          - Grass Land 60,37:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Plains Hills 59,37:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 58,37:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Manufactory
            - Route: Railroad
          - Plains Hills 57,37:
            - Owner: The Shoshone
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 56,37:
            - Owner: The Shoshone
            - Resource: Deer
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 55,37:
            - Owner: The Shoshone
            - Resource: Sheep
          - Plains Hills 54,37:
            - Owner: Brazil
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
        
        ### 17
        - Type: CityConvertsReligion
        - City:
          - Owner: The Iroquois
          - CityID: 1814
          - Population: 34
          - City: Brantford
          - Terrain: Plains
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 8
          - Y: 31
        - Owner: 1: The Iroquois
        - Religion: Protestantism
        
        ### 18
        - Type: CityConvertsReligion
        - City:
          - Owner: The Iroquois
          - CityID: 2963
          - Population: 33
          - City: Genesse River
          - Terrain: Desert
          - Resource: Oil
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 22
          - Y: 34
        - Owner: 1: The Iroquois
        - Religion: Protestantism
        
        ### 19
        - Type: CityConvertsReligion
        - City:
          - Owner: The Iroquois
          - CityID: 3048
          - Population: 36
          - City: Canandaigua Lake
          - Terrain: Grass
          - Resource: Uranium
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 17
          - Y: 19
        - Owner: 1: The Iroquois
        - Religion: Protestantism
        
        ### 20
        - Type: CityConvertsReligion
        - City:
          - Owner: The Iroquois
          - CityID: 4339
          - Population: 29
          - City: Osaka
          - Terrain: Plains
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Hills
          - X: 19
          - Y: 43
        - Owner: 1: The Iroquois
        - Religion: Protestantism
        
        ### 21
        - Type: CityConvertsReligion
        - City:
          - Owner: The Iroquois
          - CityID: 8095
          - Population: 28
          - City: Satsuma
          - Terrain: Plains
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 24
          - Y: 46
        - Owner: 1: The Iroquois
        - Religion: Protestantism
        
        ### 22
        - Type: CityBoughtPlot
        - WithFaithCulture: true
        - Player: 1: The Iroquois
        - City:
          - Name: Yokohama
          - Population: 30
          - ID: 9784
        - Ocean 37,25:
          - Owner: The Iroquois
        
        ### 23
        - Type: SetPopulation
        - OldPopulation: 33
        - NewPopulation: 34
        - City:
          - Owner: The Iroquois
          - CityID: 12603
          - Population: 34
          - City: Surabaya
          - Terrain: Grass
          - Route: Railroad
          - Plot: Land
          - X: 54
          - Y: 24
        
        ### 24
        - Type: SetPopulation
        - OldPopulation: 27
        - NewPopulation: 28
        - City:
          - Owner: The Iroquois
          - CityID: 13442
          - Population: 28
          - City: Palatium
          - Terrain: Grass
          - Route: Railroad
          - Plot: Land
          - X: 71
          - Y: 18
        
        ### 25
        - Type: SetPopulation
        - OldPopulation: 28
        - NewPopulation: 29
        - City:
          - Owner: The Iroquois
          - CityID: 17417
          - Population: 29
          - IsRiver: true
          - City: Tlaxcala
          - Terrain: Grass
          - Resource: Deer
          - Route: Railroad
          - Plot: Hills
          - X: 61
          - Y: 15
        
        ### 26
        - Type: CityConstructed
        - City:
          - Name: Cardiff
          - Population: 20
          - ID: 18221
        - Owner: 1: The Iroquois
        - Building: TwoKay Foods Office
        
        ### 27
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18488
        - Player: 1: The Iroquois
        - Plots:
          - Desert Land 63,11:
            - Owner: The Aztecs
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 63,12:
            - Owner: The Aztecs
            - Resource: Cotton
            - Improvement: Manufactory
            - Route: Railroad
          - Plains Hills 62,13:
            - Owner: The Aztecs
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 62,14:
            - Owner: The Iroquois
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
          - Grass Hills 61,15:
            - Owner: The Iroquois
            - CityID: 17417
            - Population: 29
            - IsRiver: true
            - City: Tlaxcala
            - Resource: Deer
            - Route: Railroad
        
        ### 28
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 18863
        - Player: 1: The Iroquois
        - Desert Land 48,34:
          - Owner: The Iroquois
          - Improvement: Fort
          - Route: Railroad
        
        ### 29
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18084
        - Player: 1: The Iroquois
        - Plots:
          - Grass Land 55,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 54,30:
            - Owner: The Iroquois
            - CityID: 15221
            - Population: 24
            - IsRiver: true
            - City: Oviedo
            - Religion: Confucianism
            - Route: Railroad
          - Plains Land 56,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
          - Grass Land 57,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 57,31:
            - Owner: Indonesia
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
        
        ### 30
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18984
        - Player: 1: The Iroquois
        - Plots:
          - Grass Hills 64,24:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Nutmeg
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 63,24:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 62,24:
            - Owner: Indonesia
            - CityID: 2071
            - Population: 31
            - IsRiver: true
            - City: Makassar
            - Resource: Iron
            - Route: Railroad
        
        ### 31
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18161
        - Player: 1: The Iroquois
        - Plots:
          - Plains Hills 67,15:
            - Owner: Indonesia
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Plains Hills 68,15:
            - Owner: Indonesia
            - Resource: Coal
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 69,15:
            - Owner: The Iroquois
            - Improvement: Fort
        
        ### 32
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18376
        - Player: 1: The Iroquois
        - Plots:
          - Plains Land 63,10:
            - Owner: The Aztecs
            - CityID: 1062
            - Population: 33
            - IsRiver: true
            - City: Tenochtitlan
            - Religion: Catholicism
            - Route: Railroad
          - Desert Land 63,11:
            - Owner: The Aztecs
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 63,12:
            - Owner: The Aztecs
            - Resource: Cotton
            - Improvement: Manufactory
            - Route: Railroad
          - Plains Hills 62,13:
            - Owner: The Aztecs
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 62,14:
            - Owner: The Iroquois
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
          - Grass Hills 61,15:
            - Owner: The Iroquois
            - CityID: 17417
            - Population: 29
            - IsRiver: true
            - City: Tlaxcala
            - Resource: Deer
            - Route: Railroad
        
        ### 33
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18611
        - Player: 1: The Iroquois
        - Desert Land 48,34:
          - Owner: The Iroquois
          - Improvement: Fort
          - Route: Railroad
        
        ### 34
        - Type: CityEventChoiceEnded
        - City:
          - Name: Nantes
          - Population: 17
          - ID: 18609
        - Player: 1: The Iroquois
        - Choice: 90
        
        ### 35
        - Type: EspionageState
        - SpyIndex: 0
        - SpyState: 1
        - City:
          - Owner: City-State Belgrade
          - CityID: 1067
          - Population: 17
          - City: Belgrade
          - Terrain: Desert
          - Route: Railroad
          - Plot: Hills
          - X: 64
          - Y: 20
        - SpyOwner: 1: The Iroquois
        
        ### 36
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17222
        - Player: 1: The Iroquois
        - Plots:
          - Ocean 38,36:
            - Owner: The Iroquois
          - Coast 37,35:
            - Owner: City-State Zanzibar
          - Coast 37,34:
            - Owner: City-State Zanzibar
          - Coast 36,33:
            - Owner: City-State Zanzibar
          - Ocean 36,32:
            - Owner: The Iroquois
        
        ### 37
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: AssaultSea
          - Unit: Nuclear Submarine
          - ID: 18839
        - Player: 1: The Iroquois
        - Plots:
          - Coast 37,36:
            - Owner: The Iroquois
          - Coast 37,35:
            - Owner: City-State Zanzibar
          - Coast 37,34:
            - Owner: City-State Zanzibar
          - Coast 36,34:
            - Owner: The Iroquois
          - Ocean 35,33:
            - Owner: The Iroquois
        
        ### 38
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 96%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16791
        - Player: 1: The Iroquois
        - Plots:
          - Coast 37,36:
            - Owner: The Iroquois
          - Coast 37,35:
            - Owner: City-State Zanzibar
          - Coast 37,34:
            - Owner: City-State Zanzibar
          - Coast 36,34:
            - Owner: The Iroquois
          - Coast 36,33:
            - Owner: City-State Zanzibar
          - Ocean 36,32:
            - Owner: The Iroquois
          - Coast 36,31:
            - Owner: The Iroquois
        
        ### 39
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Nuclear Submarine
          - ID: 18858
        - Player: 1: The Iroquois
        - Plots:
          - Coast 37,36:
            - Owner: The Iroquois
          - Coast 37,35:
            - Owner: City-State Zanzibar
          - Coast 37,34:
            - Owner: City-State Zanzibar
          - Coast 36,34:
            - Owner: The Iroquois
        
        ### 40
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Nuclear Submarine
          - ID: 18855
        - Player: 1: The Iroquois
        - Plots:
          - Coast 37,36:
            - Owner: The Iroquois
          - Coast 37,35:
            - Owner: City-State Zanzibar
          - Coast 37,34:
            - Owner: City-State Zanzibar
          - Coast 36,34:
            - Owner: The Iroquois
        
        ### 41
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17736
        - Player: 1: The Iroquois
        - Plots:
          - Ocean 39,36:
            - Owner: The Iroquois
          - Ocean 38,35:
            - Owner: The Iroquois
          - Coast 38,34:
            - Owner: City-State Zanzibar
            - Resource: Whales
            - Improvement: Fishing Boats
          - Coast 37,34:
            - Owner: City-State Zanzibar
          - Coast 36,33:
            - Owner: City-State Zanzibar
          - Ocean 36,32:
            - Owner: The Iroquois
        
        ### 42
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Nuclear Submarine
          - ID: 18856
        - Player: 1: The Iroquois
        - Ocean 39,36:
          - Owner: The Iroquois
        
        ### 43
        - Type: UnitBuildCompleted
        - Owner: 1: The Iroquois
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4526
        - Build: Construct a Farm
        - Plains Land 54,27:
          - Owner: The Iroquois
        
        ### 44
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1913
        - Player: 1: The Iroquois
        - Grass Hills 62,15:
          - Owner: The Iroquois
          - Improvement: Mine
        
        ### 45
        - Type: TileImprovementChanged
        - Owner: 1: The Iroquois
        - OldImprovement: Mine
        - Grass Hills 62,15:
          - Owner: The Iroquois
        
        ### 46
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 1: The Iroquois
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1913
        - Build: Construct a Fort
        - Grass Hills 62,15:
          - Owner: The Iroquois
        
        ### 47
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 2534
        - Player: 1: The Iroquois
        - Plots:
          - Plains Land 53,31:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 54,30:
            - Owner: The Iroquois
            - CityID: 15221
            - Population: 24
            - IsRiver: true
            - City: Oviedo
            - Religion: Confucianism
            - Route: Railroad
          - Grass Land 55,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 56,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
          - Grass Hills 56,29:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Hills 57,28:
            - Owner: Indonesia
            - Resource: Sheep
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Land 57,27:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Nutmeg
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Hills 58,26:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 58,25:
            - Owner: Indonesia
            - CityID: 1059
            - Population: 38
            - IsRiver: true
            - City: Jakarta
            - Religion: Hinduism
            - Route: Railroad
          - Plains Land 59,24:
            - Owner: Indonesia
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 59,23:
            - Owner: Indonesia
            - Improvement: Village
            - Route: Railroad
          - Desert Hills 60,22:
            - Owner: Indonesia
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 61,22:
            - Owner: Indonesia
            - Resource: Gems
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 61,23:
            - Owner: Indonesia
            - Resource: Maize
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Hills 62,23:
            - Owner: Indonesia
            - IsRiver: true
            - Route: Railroad
          - Plains Hills 63,22:
            - Owner: Indonesia
            - Resource: Aluminum
            - Improvement: Holy Site
            - Route: Railroad
          - Plains Land 63,21:
            - Owner: City-State Belgrade
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Desert Hills 64,20:
            - Owner: City-State Belgrade
            - CityID: 1067
            - Population: 17
            - City: Belgrade
            - Route: Railroad
          - Desert Land 64,19:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Embassy
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 65,18:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 65,17:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Hills 65,16:
            - Owner: Indonesia
            - Route: Railroad
          - Grass Hills 64,15:
            - Owner: Indonesia
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Plains Hills 65,14:
            - Owner: Indonesia
            - Resource: Coal
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 64,13:
            - Owner: The Aztecs
            - Resource: Aluminum
            - Improvement: Town
            - Route: Railroad
          - Plains Hills 63,13:
            - Owner: The Aztecs
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 63,14:
            - Owner: The Iroquois
        
        ### 48
        - Type: UnitBuildCompleted
        - Owner: 1: The Iroquois
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 2534
        - Build: Construct a Farm
        - Grass Land 63,14:
          - Owner: The Iroquois
        
        ### 49
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 95%
          - AI: Worker
          - Unit: Worker
          - ID: 2940
        - Player: 1: The Iroquois
        - Plots:
          - Grass Hills 65,31:
            - Owner: The Iroquois
            - Resource: Deer
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 65,30:
            - Owner: Poland
            - Resource: Lapis Lazuli
            - Improvement: Quarry
            - Route: Railroad
          - Grass Land 64,30:
            - Owner: Poland
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 63,29:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 63,28:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Oil
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Land 62,28:
            - Owner: Indonesia
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Land 61,29:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 60,29:
            - Owner: Indonesia
            - CityID: 1882
            - Population: 32
            - IsRiver: true
            - City: Medan
            - Route: Railroad
          - Grass Land 60,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 59,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
          - Grass Land 58,30:
            - Owner: Indonesia
            - Resource: Oil
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Land 57,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 56,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
          - Grass Land 55,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 54,30:
            - Owner: The Iroquois
            - CityID: 15221
            - Population: 24
            - IsRiver: true
            - City: Oviedo
            - Religion: Confucianism
            - Route: Railroad
          - Plains Land 53,31:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 53,32:
            - Owner: The Iroquois
            - IsRiver: true
            - Route: Railroad
            - Feature: Flood Plains
        
        ### 50
        - Type: UnitBuildCompleted
        - Owner: 1: The Iroquois
        - Unit:
          - Level: 1
          - Health: 95%
          - AI: Worker
          - Unit: Worker
          - ID: 2940
        - Build: Construct a Farm
        - Desert Land 53,32:
          - Owner: The Iroquois
          - IsRiver: true
          - Route: Railroad
          - Feature: Flood Plains
        
        ### 51
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3106
        - Player: 1: The Iroquois
        - Plots:
          - Grass Land 55,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 56,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
          - Grass Land 57,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 58,30:
            - Owner: Indonesia
            - Resource: Oil
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Land 59,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
          - Grass Land 60,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 60,29:
            - Owner: Indonesia
            - CityID: 1882
            - Population: 32
            - IsRiver: true
            - City: Medan
            - Route: Railroad
          - Grass Land 61,29:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 62,28:
            - Owner: Indonesia
            - Improvement: Manufactory
            - Route: Railroad
          - Plains Land 63,28:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Oil
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Land 63,29:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 64,30:
            - Owner: Poland
            - Improvement: Farm
            - Route: Railroad
          - Grass Hills 65,30:
            - Owner: Poland
            - Resource: Lapis Lazuli
            - Improvement: Quarry
            - Route: Railroad
          - Grass Hills 65,31:
            - Owner: The Iroquois
            - Resource: Deer
            - Improvement: Town
            - Route: Railroad
        
        ### 52
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3603
        - Player: 1: The Iroquois
        - Plots:
          - Grass Hills 68,21:
            - Owner: The Iroquois
            - Resource: Lapis Lazuli
            - Improvement: Quarry
            - Route: Railroad
          - Grass Hills 65,31:
            - Owner: The Iroquois
            - Resource: Deer
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 65,30:
            - Owner: Poland
            - Resource: Lapis Lazuli
            - Improvement: Quarry
            - Route: Railroad
          - Grass Land 64,30:
            - Owner: Poland
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 63,29:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 63,28:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Oil
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Land 62,28:
            - Owner: Indonesia
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Land 61,29:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 60,29:
            - Owner: Indonesia
            - CityID: 1882
            - Population: 32
            - IsRiver: true
            - City: Medan
            - Route: Railroad
          - Grass Land 60,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 59,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
          - Grass Land 58,30:
            - Owner: Indonesia
            - Resource: Oil
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Land 57,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 56,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
          - Grass Land 55,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 54,29:
            - Owner: The Iroquois
            - IsRiver: true
            - Route: Railroad
        
        ### 53
        - Type: UnitBuildCompleted
        - Owner: 1: The Iroquois
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3603
        - Build: Construct a Farm
        - Grass Land 54,29:
          - Owner: The Iroquois
          - IsRiver: true
          - Route: Railroad
        
        ### 54
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4338
        - Player: 1: The Iroquois
        - Plots:
          - Plains Land 62,16:
            - Owner: The Iroquois
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 62,17:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 63,18:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 63,19:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 64,20:
            - Owner: City-State Belgrade
            - CityID: 1067
            - Population: 17
            - City: Belgrade
            - Route: Railroad
          - Plains Land 65,20:
            - Owner: City-State Belgrade
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 66,20:
            - Owner: City-State Belgrade
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 67,20:
            - Owner: City-State Belgrade
            - IsRiver: true
            - Resource: Iron
            - Improvement: Mine
            - Route: Road
          - Plains Land 68,20:
            - Owner: The Iroquois
            - Resource: Deer
            - Feature: Forest
          - Plains Hills 69,20:
            - Owner: The Iroquois
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 69,21:
            - Owner: The Iroquois
            - Route: Railroad
        
        ### 55
        - Type: UnitBuildCompleted
        - Owner: 1: The Iroquois
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4338
        - Build: Construct a Farm
        - Grass Land 69,21:
          - Owner: The Iroquois
          - Route: Railroad
        
        ### 56
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 18314
        - Player: 1: The Iroquois
        - Plots:
          - Grass Land 55,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 56,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
          - Grass Land 57,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 58,30:
            - Owner: Indonesia
            - Resource: Oil
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Land 59,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
          - Grass Land 60,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 60,29:
            - Owner: Indonesia
            - CityID: 1882
            - Population: 32
            - IsRiver: true
            - City: Medan
            - Route: Railroad
          - Grass Land 61,29:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 62,28:
            - Owner: Indonesia
            - Improvement: Manufactory
            - Route: Railroad
          - Plains Land 62,27:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Hills 63,26:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 63,25:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Pepper
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 63,24:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Hills 62,23:
            - Owner: Indonesia
            - IsRiver: true
            - Route: Railroad
          - Plains Hills 63,22:
            - Owner: Indonesia
            - Resource: Aluminum
            - Improvement: Holy Site
            - Route: Railroad
          - Plains Land 63,21:
            - Owner: City-State Belgrade
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 64,21:
            - Owner: City-State Belgrade
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 65,20:
            - Owner: City-State Belgrade
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 66,20:
            - Owner: City-State Belgrade
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 67,20:
            - Owner: City-State Belgrade
            - IsRiver: true
            - Resource: Iron
            - Improvement: Mine
            - Route: Road
          - Plains Land 68,20:
            - Owner: The Iroquois
            - Resource: Deer
            - Feature: Forest
          - Plains Hills 69,20:
            - Owner: The Iroquois
            - Improvement: Mine
            - Route: Railroad
          - Mountain Mountain 70,20:
            - Owner: The Iroquois
            - Route: Railroad
          - Mountain Mountain 70,19:
            - Owner: The Iroquois
            - Route: Railroad
          - Grass Land 71,18:
            - Owner: The Iroquois
            - CityID: 13442
            - Population: 28
            - City: Palatium
            - Route: Railroad
        
        ### 57
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 18320
        - Player: 1: The Iroquois
        - Plots:
          - Desert Hills 59,14:
            - Owner: The Iroquois
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 59,15:
            - Owner: The Iroquois
            - Improvement: Village
            - Route: Railroad
          - Plains Land 60,15:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Hills 61,15:
            - Owner: The Iroquois
            - CityID: 17417
            - Population: 29
            - IsRiver: true
            - City: Tlaxcala
            - Resource: Deer
            - Route: Railroad
          - Plains Land 62,16:
            - Owner: The Iroquois
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 62,17:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 63,18:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 63,19:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 64,19:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Embassy
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 65,20:
            - Owner: City-State Belgrade
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 66,20:
            - Owner: City-State Belgrade
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 67,20:
            - Owner: City-State Belgrade
            - IsRiver: true
            - Resource: Iron
            - Improvement: Mine
            - Route: Road
          - Plains Land 68,20:
            - Owner: The Iroquois
            - Resource: Deer
            - Feature: Forest
          - Plains Hills 69,20:
            - Owner: The Iroquois
            - Improvement: Mine
            - Route: Railroad
          - Mountain Mountain 70,20:
            - Owner: The Iroquois
            - Route: Railroad
          - Mountain Mountain 70,19:
            - Owner: The Iroquois
            - Route: Railroad
          - Grass Land 71,18:
            - Owner: The Iroquois
            - CityID: 13442
            - Population: 28
            - City: Palatium
            - Route: Railroad
          - Plains Land 71,17:
            - Owner: The Iroquois
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 72,16:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 72,15:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 73,14:
            - Owner: The Iroquois
            - CityID: 17908
            - Population: 15
            - IsRiver: true
            - City: Truro
            - Resource: Cattle
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 73,11:
            - Owner: The Iroquois
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 74,10:
            - Owner: The Iroquois
            - CityID: 18221
            - Population: 20
            - IsRiver: true
            - City: Cardiff
            - Religion: Buddhism
            - Route: Railroad
          - Coast 75,10:
            - Owner: The Iroquois
        
        ### 58
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 18323
        - Player: 1: The Iroquois
        - Plots:
          - Coast 75,10:
            - Owner: The Iroquois
          - Desert Land 74,10:
            - Owner: The Iroquois
            - CityID: 18221
            - Population: 20
            - IsRiver: true
            - City: Cardiff
            - Religion: Buddhism
            - Route: Railroad
        
        ### 59
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 13118
        - Player: 1: The Iroquois
        - Plots:
          - Grass Land 54,30:
            - Owner: The Iroquois
            - CityID: 15221
            - Population: 24
            - IsRiver: true
            - City: Oviedo
            - Religion: Confucianism
            - Route: Railroad
          - Grass Land 55,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 56,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
          - Grass Hills 56,29:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Hills 57,28:
            - Owner: Indonesia
            - Resource: Sheep
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Land 57,27:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Nutmeg
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Hills 58,26:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 58,25:
            - Owner: Indonesia
            - CityID: 1059
            - Population: 38
            - IsRiver: true
            - City: Jakarta
            - Religion: Hinduism
            - Route: Railroad
          - Grass Hills 59,25:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 60,25:
            - Owner: Indonesia
            - Improvement: Village
            - Route: Railroad
          - Grass Land 61,25:
            - Owner: Indonesia
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 62,24:
            - Owner: Indonesia
            - CityID: 2071
            - Population: 31
            - IsRiver: true
            - City: Makassar
            - Resource: Iron
            - Route: Railroad
          - Grass Hills 62,23:
            - Owner: Indonesia
            - IsRiver: true
            - Route: Railroad
          - Plains Hills 63,22:
            - Owner: Indonesia
            - Resource: Aluminum
            - Improvement: Holy Site
            - Route: Railroad
          - Plains Land 63,21:
            - Owner: City-State Belgrade
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 64,21:
            - Owner: City-State Belgrade
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 65,20:
            - Owner: City-State Belgrade
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 66,20:
            - Owner: City-State Belgrade
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 67,20:
            - Owner: City-State Belgrade
            - IsRiver: true
            - Resource: Iron
            - Improvement: Mine
            - Route: Road
          - Plains Land 68,20:
            - Owner: The Iroquois
            - Resource: Deer
            - Feature: Forest
          - Plains Hills 69,20:
            - Owner: The Iroquois
            - Improvement: Mine
            - Route: Railroad
          - Mountain Mountain 70,20:
            - Owner: The Iroquois
            - Route: Railroad
          - Mountain Mountain 70,19:
            - Owner: The Iroquois
            - Route: Railroad
          - Grass Land 71,18:
            - Owner: The Iroquois
            - CityID: 13442
            - Population: 28
            - City: Palatium
            - Route: Railroad
          - Plains Land 71,17:
            - Owner: The Iroquois
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 72,16:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 72,15:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 73,14:
            - Owner: The Iroquois
            - CityID: 17908
            - Population: 15
            - IsRiver: true
            - City: Truro
            - Resource: Cattle
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 73,11:
            - Owner: The Iroquois
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 74,10:
            - Owner: The Iroquois
            - CityID: 18221
            - Population: 20
            - IsRiver: true
            - City: Cardiff
            - Religion: Buddhism
            - Route: Railroad
          - Coast 75,10:
            - Owner: The Iroquois
        
        ### 60
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Attack
          - Unit: Mercenary
          - ID: 18781
        - Player: 1: The Iroquois
        - Plots:
          - Grass Land 54,30:
            - Owner: The Iroquois
            - CityID: 15221
            - Population: 24
            - IsRiver: true
            - City: Oviedo
            - Religion: Confucianism
            - Route: Railroad
          - Plains Land 53,31:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 53,32:
            - Owner: The Iroquois
            - IsRiver: true
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 52,33:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Landmark
            - Route: Railroad
          - Desert Land 53,34:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
        
        ### 61
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16928
        - Player: 1: The Iroquois
        - Grass Hills 36,29:
          - Owner: The Iroquois
          - CityID: 9784
          - Population: 30
          - City: Yokohama
          - Resource: Coal
          - Religion: Protestantism
          - Route: Railroad
        
        ### 62
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16930
        - Player: 1: The Iroquois
        
        ### 63
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17747
        - Player: 1: The Iroquois
        - Ocean 40,29:
          - Owner: The Iroquois
        
        ### 64
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Light Tank
          - ID: 15852
        - Player: 1: The Iroquois
        - Plots:
          - Plains Land 62,16:
            - Owner: The Iroquois
            - Improvement: Farm
            - Route: Railroad
          - Grass Hills 61,15:
            - Owner: The Iroquois
            - CityID: 17417
            - Population: 29
            - IsRiver: true
            - City: Tlaxcala
            - Resource: Deer
            - Route: Railroad
          - Plains Land 60,15:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 59,15:
            - Owner: The Iroquois
            - Improvement: Village
            - Route: Railroad
          - Desert Land 58,15:
            - Owner: The Iroquois
            - Feature: Oasis
        
        ### 65
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 99%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13367
        - Player: 1: The Iroquois
        - Plots:
          - Plains Land 60,15:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Hills 61,15:
            - Owner: The Iroquois
            - CityID: 17417
            - Population: 29
            - IsRiver: true
            - City: Tlaxcala
            - Resource: Deer
            - Route: Railroad
          - Plains Land 62,16:
            - Owner: The Iroquois
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 61,17:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Feature: Flood Plains
        
        ### 66
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16576
        - Player: 1: The Iroquois
        - Desert Land 59,16:
          - Owner: The Iroquois
          - Improvement: Farm
        
        ### 67
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 18939
        - Player: 1: The Iroquois
        - Plots:
          - Coast 37,36:
            - Owner: The Iroquois
          - Coast 37,35:
            - Owner: City-State Zanzibar
          - Coast 38,34:
            - Owner: City-State Zanzibar
            - Resource: Whales
            - Improvement: Fishing Boats
        
        ### 68
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 18967
        - Player: 1: The Iroquois
        - Plots:
          - Desert Land 63,18:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 62,17:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 62,16:
            - Owner: The Iroquois
            - Improvement: Farm
            - Route: Railroad
        
        ### 69
        - Type: PlayerDoneTurn
        - NextPlayer: 2: Indonesia
        - Player: 1: The Iroquois
        
        ### 70
        - Type: DealMade
        - StartTurn: 425
        - TradedItems:
          - #0:
            - Data1: 21
            - Data2: 1
            - Data3: 0
            - Duration: 50
            - FromPlayer: 5
            - Item: Resources
          - #1:
            - Data1: 0
            - Data2: 0
            - Data3: 0
            - Duration: 0
            - FromPlayer: 2
            - Item: AllowEmbassy
          - #2:
            - Data1: 17
            - Data2: 1
            - Data3: 0
            - Duration: 50
            - FromPlayer: 2
            - Item: Resources
          - #3:
            - Data1: 0
            - Data2: 0
            - Data3: 0
            - Duration: 0
            - FromPlayer: 5
            - Item: AllowEmbassy
        - ToPlayer: 5: The Aztecs
        - FromPlayer: 2: Indonesia
        
        ### 71
        - Type: CityInvestedBuilding
        - BuildingClass: Military Base
        - Invested: true
        - City:
          - Name: Makassar
          - Population: 31
          - ID: 2071
        - Player: 2: Indonesia
        
        ### 72
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Worker
          - ID: 19000
        - Player: 2: Indonesia
        - Grass Land 58,25:
          - Owner: Indonesia
          - CityID: 1059
          - Population: 38
          - IsRiver: true
          - City: Jakarta
          - Religion: Hinduism
          - Route: Railroad
        
        ### 73
        - Type: UnitCreated
        - UnitType: Worker
        - Player: 2: Indonesia
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 19000
        - Grass Land 58,25:
          - Owner: Indonesia
          - CityID: 1059
          - Population: 38
          - IsRiver: true
          - City: Jakarta
          - Religion: Hinduism
          - Route: Railroad
        
        ### 74
        - Type: CityTrained
        - WithGold: true
        - Player: 2: Indonesia
        - City:
          - Name: Jakarta
          - Population: 38
          - ID: 1059
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 19000
        
        ### 75
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Inquisitor
          - ID: 19001
        - Player: 2: Indonesia
        - Grass Land 58,25:
          - Owner: Indonesia
          - CityID: 1059
          - Population: 38
          - IsRiver: true
          - City: Jakarta
          - Religion: Hinduism
          - Route: Railroad
        
        ### 76
        - Type: UnitCreated
        - UnitType: Inquisitor
        - Player: 2: Indonesia
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 19001
        - Grass Land 58,25:
          - Owner: Indonesia
          - CityID: 1059
          - Population: 38
          - IsRiver: true
          - City: Jakarta
          - Religion: Hinduism
          - Route: Railroad
        
        ### 77
        - Type: CityTrained
        - WithFaith: true
        - Player: 2: Indonesia
        - City:
          - Name: Jakarta
          - Population: 38
          - ID: 1059
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 19001
        
        ### 78
        - Type: PlayerGoldenAge
        - TurnChange: 10
        - Player: 2: Indonesia
        
        ### 79
        - Type: CityConstructed
        - City:
          - Name: Jakarta
          - Population: 38
          - ID: 1059
        - Owner: 2: Indonesia
        - Building: Military Base
        
        ### 80
        - Type: CityConstructed
        - City:
          - Name: Tlatelolco
          - Population: 24
          - ID: 17138
        - Owner: 2: Indonesia
        - Building: Military Base
        
        ### 81
        - Type: SetPopulation
        - OldPopulation: 4
        - NewPopulation: 3
        - City:
          - Owner: Indonesia
          - CityID: 18435
          - Population: 3
          - IsRiver: true
          - City: Dublin
          - Terrain: Desert
          - Resource: Pepper
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Hills
          - X: 69
          - Y: 11
        
        ### 82
        - Type: SetPopulation
        - OldPopulation: 6
        - NewPopulation: 5
        - City:
          - Owner: Indonesia
          - CityID: 18731
          - Population: 5
          - City: Douglas
          - Terrain: Tundra
          - Resource: Sheep
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Hills
          - X: 67
          - Y: 3
        
        ### 83
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18014
        - Player: 2: Indonesia
        - Plots:
          - Desert Hills 63,19:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 64,20:
            - Owner: City-State Belgrade
            - CityID: 1067
            - Population: 17
            - City: Belgrade
            - Route: Railroad
          - Plains Land 63,21:
            - Owner: City-State Belgrade
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 63,22:
            - Owner: Indonesia
            - Resource: Aluminum
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Hills 62,23:
            - Owner: Indonesia
            - IsRiver: true
            - Route: Railroad
        
        ### 84
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18015
        - Player: 2: Indonesia
        - Plots:
          - Grass Land 59,26:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 59,27:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Nutmeg
            - Improvement: Town
            - Route: Railroad
          - Grass Land 60,28:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Nutmeg
            - Improvement: Town
            - Route: Railroad
          - Grass Land 60,29:
            - Owner: Indonesia
            - CityID: 1882
            - Population: 32
            - IsRiver: true
            - City: Medan
            - Route: Railroad
          - Grass Land 60,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Hills 60,31:
            - Owner: Indonesia
            - Improvement: Fort
            - Route: Railroad
        
        ### 85
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18168
        - Player: 2: Indonesia
        - Plots:
          - Plains Land 63,21:
            - Owner: City-State Belgrade
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 63,22:
            - Owner: Indonesia
            - Resource: Aluminum
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Hills 62,23:
            - Owner: Indonesia
            - IsRiver: true
            - Route: Railroad
          - Grass Land 63,24:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 62,25:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
        
        ### 86
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18557
        - Player: 2: Indonesia
        - Plots:
          - Grass Land 61,34:
            - Owner: The Iroquois
            - CityID: 15152
            - Population: 17
            - IsRiver: true
            - City: Florence
            - Route: Railroad
          - Plains Hills 61,33:
            - Owner: The Iroquois
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 61,32:
            - Owner: The Iroquois
            - Improvement: Village
            - Route: Railroad
          - Grass Hills 60,31:
            - Owner: Indonesia
            - Improvement: Fort
            - Route: Railroad
          - Grass Land 60,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
        
        ### 87
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18228
        - Player: 2: Indonesia
        - Plots:
          - Plains Hills 63,22:
            - Owner: Indonesia
            - Resource: Aluminum
            - Improvement: Holy Site
            - Route: Railroad
          - Plains Land 63,21:
            - Owner: City-State Belgrade
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Desert Hills 64,20:
            - Owner: City-State Belgrade
            - CityID: 1067
            - Population: 17
            - City: Belgrade
            - Route: Railroad
          - Desert Land 64,19:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Embassy
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 65,18:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
            - Feature: Flood Plains
        
        ### 88
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18090
        - Player: 2: Indonesia
        - Plots:
          - Desert Hills 64,20:
            - Owner: City-State Belgrade
            - CityID: 1067
            - Population: 17
            - City: Belgrade
            - Route: Railroad
          - Plains Land 63,21:
            - Owner: City-State Belgrade
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 63,22:
            - Owner: Indonesia
            - Resource: Aluminum
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Hills 62,23:
            - Owner: Indonesia
            - IsRiver: true
            - Route: Railroad
          - Grass Land 62,24:
            - Owner: Indonesia
            - CityID: 2071
            - Population: 31
            - IsRiver: true
            - City: Makassar
            - Resource: Iron
            - Route: Railroad
        
        ### 89
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18091
        - Player: 2: Indonesia
        - Plots:
          - Grass Land 62,24:
            - Owner: Indonesia
            - CityID: 2071
            - Population: 31
            - IsRiver: true
            - City: Makassar
            - Resource: Iron
            - Route: Railroad
          - Grass Hills 62,23:
            - Owner: Indonesia
            - IsRiver: true
            - Route: Railroad
          - Plains Hills 63,22:
            - Owner: Indonesia
            - Resource: Aluminum
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Land 64,22:
            - Owner: Indonesia
            - Improvement: Fort
          - Plains Hills 64,21:
            - Owner: City-State Belgrade
            - Improvement: Mine
            - Route: Railroad
        
        ### 90
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18380
        - Player: 2: Indonesia
        - Plots:
          - Grass Land 58,25:
            - Owner: Indonesia
            - CityID: 1059
            - Population: 38
            - IsRiver: true
            - City: Jakarta
            - Religion: Hinduism
            - Route: Railroad
          - Grass Hills 58,26:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 57,27:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Nutmeg
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Hills 57,28:
            - Owner: Indonesia
            - Resource: Sheep
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Hills 56,29:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
        
        ### 91
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 18275
        - Player: 2: Indonesia
        - Plots:
          - Coast 44,9:
            - Owner: The Iroquois
          - Coast 45,10:
            - Owner: The Iroquois
          - Ocean 45,11:
            - Owner: The Iroquois
        
        ### 92
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18381
        - Player: 2: Indonesia
        - Plots:
          - Grass Land 64,27:
            - Owner: Poland
            - CityID: 15755
            - Population: 21
            - IsRiver: true
            - City: Krakow
            - Resource: Cloves
            - Religion: Confucianism
            - Route: Railroad
          - Grass Land 63,27:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Academy
          - Plains Land 62,27:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Hills 62,26:
            - Owner: Indonesia
            - Resource: Gems
            - Improvement: Mine
            - Route: Railroad
        
        ### 93
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18948
        - Player: 2: Indonesia
        - Plots:
          - Grass Hills 66,15:
            - Owner: Indonesia
            - CityID: 17138
            - Population: 24
            - IsRiver: true
            - City: Tlatelolco
            - Route: Railroad
          - Plains Hills 67,14:
            - Owner: Indonesia
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 67,13:
            - Owner: Indonesia
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 68,12:
            - Owner: Indonesia
            - Resource: Bison
            - Improvement: Camp
        
        ### 94
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 18889
        - Player: 2: Indonesia
        
        ### 95
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 18905
        - Player: 2: Indonesia
        
        ### 96
        - Type: EspionageState
        - SpyIndex: 0
        - SpyState: 0
        - SpyOwner: 2: Indonesia
        
        ### 97
        - Type: EspionageState
        - SpyIndex: 0
        - SpyState: 1
        - City:
          - Owner: City-State Belgrade
          - CityID: 1067
          - Population: 17
          - City: Belgrade
          - Terrain: Desert
          - Route: Railroad
          - Plot: Hills
          - X: 64
          - Y: 20
        - SpyOwner: 2: Indonesia
        
        ### 98
        - Type: PlayerDoTurn
        - Player: 2: Indonesia
        
        ### 99
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Diplomat
          - Unit: Great Diplomat
          - ID: 18829
        - Player: 2: Indonesia
        - Grass Land 38,33:
          - Owner: City-State Zanzibar
          - CityID: 1073
          - Population: 27
          - City: Zanzibar
          - Resource: Glass
          - Religion: Protestantism
          - Route: Railroad
        
        ### 100
        - Type: MinorAlliesChanged
        - IsNowAlly: true
        - OldFriendship: 382
        - NewFriendship: 667
        - MajorPlayer: 2: Indonesia
        - MinorPlayer: 31
        
        ### 101
        - Type: SetAlly
        - NewAllyPlayer: 2: Indonesia
        - OldAllyPlayer: 6: Brazil
        - MinorPlayer: 31
        
        ### 102
        - Type: GreatPersonExpended
        - Player: 2: Indonesia
        - City:
          - Owner: City-State Zanzibar
          - CityID: 1073
          - Population: 27
          - City: Zanzibar
          - Terrain: Grass
          - Resource: Glass
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 38
          - Y: 33
        - Unit:
          - Level: 1
          - AI: Diplomat
          - Unit: Great Diplomat
          - ID: 18829
        - GreatPerson: 168
        
        ### 103
        - Type: UnitBuildCompleted
        - Owner: 2: Indonesia
        - Unit:
          - Level: 1
          - Health: 90%
          - AI: Worker
          - Unit: Worker
          - ID: 16506
        - Build: Construct a Fort
        - Grass Hills 68,18:
          - Owner: Indonesia
        
        ### 104
        - Type: UnitBuildCompleted
        - Owner: 2: Indonesia
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 17140
        - Build: Construct a Village
        - Grass Hills 62,23:
          - Owner: Indonesia
          - IsRiver: true
          - Route: Railroad
        
        ### 105
        - Type: TileImprovementChanged
        - Owner: 2: Indonesia
        - NewImprovement: Fort
        - Grass Hills 57,26:
          - Owner: Indonesia
          - IsRiver: true
          - Improvement: Fort
        
        ### 106
        - Type: BuildFinished
        - Player: 2: Indonesia
        - Improvement: Fort
        - Grass Hills 57,26:
          - Owner: Indonesia
          - IsRiver: true
          - Improvement: Fort
        
        ### 107
        - Type: UnitBuildCompleted
        - Owner: 2: Indonesia
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 18436
        - Build: Construct a Fort
        - Grass Hills 57,26:
          - Owner: Indonesia
          - IsRiver: true
          - Improvement: Fort
        
        ### 108
        - Type: UnitBuildStart
        - Owner: 2: Indonesia
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 18436
        - Build: Construct a Fort
        - Grass Hills 57,26:
          - Owner: Indonesia
          - IsRiver: true
          - Improvement: Fort
        
        ### 109
        - Type: UnitBuildCompleted
        - Owner: 2: Indonesia
        - Unit:
          - Level: 1
          - Health: 75%
          - AI: Worker
          - Unit: Worker
          - ID: 6107
        - Build: Construct a Fort
        - Grass Hills 65,16:
          - Owner: Indonesia
          - Route: Railroad
        
        ### 110
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 75%
          - AI: Worker
          - Unit: Worker
          - ID: 3606
        - Player: 2: Indonesia
        - Plots:
          - Grass Hills 57,33:
            - Owner: Indonesia
            - Resource: Gems
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Land 58,32:
            - Owner: Indonesia
            - CityID: 2537
            - Population: 29
            - IsRiver: true
            - City: Batam
            - Religion: Hinduism
            - Route: Railroad
          - Grass Land 58,31:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 59,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
          - Grass Land 60,30:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 60,29:
            - Owner: Indonesia
            - CityID: 1882
            - Population: 32
            - IsRiver: true
            - City: Medan
            - Route: Railroad
          - Grass Land 61,29:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 62,28:
            - Owner: Indonesia
            - Improvement: Manufactory
            - Route: Railroad
          - Plains Land 62,27:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Hills 63,26:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 63,25:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Pepper
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 63,24:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
        
        ### 111
        - Type: TileImprovementChanged
        - Owner: 2: Indonesia
        - OldImprovement: Farm
        - Grass Land 63,24:
          - Owner: Indonesia
          - IsRiver: true
          - Route: Railroad
        
        ### 112
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 2: Indonesia
        - Unit:
          - Level: 1
          - Health: 75%
          - AI: Worker
          - Unit: Worker
          - ID: 3606
        - Build: Construct a Fort
        - Grass Land 63,24:
          - Owner: Indonesia
          - IsRiver: true
          - Route: Railroad
        
        ### 113
        - Type: UnitBuildCompleted
        - Owner: 2: Indonesia
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 17139
        - Build: Construct a Farm
        - Plains Land 66,14:
          - Owner: Indonesia
          - IsRiver: true
        
        ### 114
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 80%
          - AI: Worker
          - Unit: Worker
          - ID: 2682
        - Player: 2: Indonesia
        - Grass Hills 57,34:
          - Owner: Indonesia
          - Route: Railroad
        
        ### 115
        - Type: UnitBuildCompleted
        - Owner: 2: Indonesia
        - Unit:
          - Level: 1
          - Health: 80%
          - AI: Worker
          - Unit: Worker
          - ID: 2682
        - Build: Construct a Mine
        - Grass Hills 57,34:
          - Owner: Indonesia
          - Route: Railroad
        
        ### 116
        - Type: TileImprovementChanged
        - Owner: 2: Indonesia
        - OldImprovement: Mine
        - Plains Hills 64,16:
          - Owner: Indonesia
        
        ### 117
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 2: Indonesia
        - Unit:
          - Level: 1
          - Health: 90%
          - AI: Worker
          - Unit: Worker
          - ID: 11223
        - Build: Construct a Village
        - Plains Hills 64,16:
          - Owner: Indonesia
        
        ### 118
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 18769
        - Player: 2: Indonesia
        - Plots:
          - Grass Land 68,16:
            - Owner: Indonesia
            - Resource: Cattle
            - Improvement: Citadel
          - Plains Land 67,16:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Cotton
            - Improvement: Plantation
            - Route: Railroad
          - Plains Land 66,17:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 65,17:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 65,18:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 64,19:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Embassy
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 64,20:
            - Owner: City-State Belgrade
            - CityID: 1067
            - Population: 17
            - City: Belgrade
            - Route: Railroad
          - Plains Land 63,21:
            - Owner: City-State Belgrade
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
        
        ### 119
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 18841
        - Player: 2: Indonesia
        - Plots:
          - Plains Land 65,13:
            - Owner: Indonesia
            - Resource: Wheat
            - Improvement: Academy
            - Route: Railroad
          - Plains Hills 65,14:
            - Owner: Indonesia
            - Resource: Coal
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 65,15:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Cloves
            - Improvement: Plantation
            - Route: Railroad
          - Grass Hills 66,15:
            - Owner: Indonesia
            - CityID: 17138
            - Population: 24
            - IsRiver: true
            - City: Tlatelolco
            - Route: Railroad
        
        ### 120
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 18945
        - Player: 2: Indonesia
        - Plots:
          - Plains Hills 67,14:
            - Owner: Indonesia
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 66,15:
            - Owner: Indonesia
            - CityID: 17138
            - Population: 24
            - IsRiver: true
            - City: Tlatelolco
            - Route: Railroad
          - Desert Land 66,16:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 65,17:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 65,18:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 64,19:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Embassy
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 64,20:
            - Owner: City-State Belgrade
            - CityID: 1067
            - Population: 17
            - City: Belgrade
            - Route: Railroad
          - Plains Land 63,21:
            - Owner: City-State Belgrade
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 63,22:
            - Owner: Indonesia
            - Resource: Aluminum
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Hills 62,23:
            - Owner: Indonesia
            - IsRiver: true
            - Route: Railroad
          - Grass Land 63,24:
            - Owner: Indonesia
            - IsRiver: true
            - Route: Railroad
          - Grass Land 62,25:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Hills 62,26:
            - Owner: Indonesia
            - Resource: Gems
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 62,27:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 62,28:
            - Owner: Indonesia
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Land 61,29:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
        
        ### 121
        - Type: CityConvertsReligion
        - City:
          - Owner: Indonesia
          - CityID: 1882
          - Population: 32
          - IsRiver: true
          - City: Medan
          - Terrain: Grass
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Land
          - X: 60
          - Y: 29
        - Owner: 2: Indonesia
        - Religion: Hinduism
        
        ### 122
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Special Forces
          - ID: 19002
        - Player: 2: Indonesia
        - Desert Hills 68,14:
          - Owner: Indonesia
          - Improvement: Citadel
        
        ### 123
        - Type: UnitCreated
        - UnitType: Special Forces
        - Player: 2: Indonesia
        - Unit:
          - Level: 1
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 19002
        - Desert Hills 68,14:
          - Owner: Indonesia
          - Improvement: Citadel
        
        ### 124
        - Type: UnitUpgraded
        - Player: 2: Indonesia
        - OldUnit:
          - Level: 5
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 16896
        - NewUnit:
          - Level: 1
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 19002
        
        ### 125
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 2: Indonesia
        - OriginalUnit:
          - Level: 5
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 16896
        - NewOwner: 2: Indonesia
        - ConvertingUnit:
          - Level: 5
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 19002
        
        ### 126
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Special Forces
          - ID: 19003
        - Player: 2: Indonesia
        - Plains Land 67,11:
          - Owner: Indonesia
          - Resource: Cotton
          - Improvement: Plantation
        
        ### 127
        - Type: UnitCreated
        - UnitType: Special Forces
        - Player: 2: Indonesia
        - Unit:
          - Level: 1
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 19003
        - Plains Land 67,11:
          - Owner: Indonesia
          - Resource: Cotton
          - Improvement: Plantation
        
        ### 128
        - Type: UnitUpgraded
        - Player: 2: Indonesia
        - OldUnit:
          - Level: 4
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 18465
        - NewUnit:
          - Level: 1
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 19003
        
        ### 129
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 2: Indonesia
        - OriginalUnit:
          - Level: 4
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 18465
        - NewOwner: 2: Indonesia
        - ConvertingUnit:
          - Level: 4
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 19003
        
        ### 130
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Special Forces
          - ID: 19004
        - Player: 2: Indonesia
        - Plains Land 61,23:
          - Owner: Indonesia
          - Resource: Maize
          - Improvement: Manufactory
          - Route: Railroad
        
        ### 131
        - Type: UnitCreated
        - UnitType: Special Forces
        - Player: 2: Indonesia
        - Unit:
          - Level: 1
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 19004
        - Plains Land 61,23:
          - Owner: Indonesia
          - Resource: Maize
          - Improvement: Manufactory
          - Route: Railroad
        
        ### 132
        - Type: UnitUpgraded
        - Player: 2: Indonesia
        - OldUnit:
          - Level: 4
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 18495
        - NewUnit:
          - Level: 1
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 19004
        
        ### 133
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 2: Indonesia
        - OriginalUnit:
          - Level: 4
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 18495
        - NewOwner: 2: Indonesia
        - ConvertingUnit:
          - Level: 4
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 19004
        
        ### 134
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 18659
        - Player: 2: Indonesia
        - Plots:
          - Plains Hills 56,32:
            - Owner: Indonesia
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 56,33:
            - Owner: Indonesia
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Grass Hills 56,34:
            - Owner: Indonesia
            - Improvement: Fort
        
        ### 135
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 17838
        - Player: 2: Indonesia
        - Plots:
          - Plains Land 67,18:
            - Owner: Indonesia
            - Improvement: Citadel
            - Route: Railroad
          - Desert Land 66,18:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 65,18:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 64,19:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Embassy
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 65,20:
            - Owner: City-State Belgrade
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 64,21:
            - Owner: City-State Belgrade
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 63,21:
            - Owner: City-State Belgrade
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
        
        ### 136
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 17925
        - Player: 2: Indonesia
        - Plots:
          - Grass Land 68,17:
            - Owner: Indonesia
            - Improvement: Farm
          - Grass Hills 68,18:
            - Owner: Indonesia
        
        ### 137
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 18903
        - Player: 2: Indonesia
        - Plots:
          - Coast 47,32:
            - Owner: The Iroquois
          - Desert Land 48,32:
            - Owner: The Iroquois
            - Improvement: Landmark
            - Route: Railroad
        
        ### 138
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 18904
        - Player: 2: Indonesia
        - Plots:
          - Grass Hills 58,26:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 57,27:
            - Owner: Indonesia
            - IsRiver: true
            - Resource: Nutmeg
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Hills 57,28:
            - Owner: Indonesia
            - Resource: Sheep
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Hills 56,29:
            - Owner: Indonesia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Plains Land 56,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
          - Grass Land 55,30:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 54,30:
            - Owner: The Iroquois
            - CityID: 15221
            - Population: 24
            - IsRiver: true
            - City: Oviedo
            - Religion: Confucianism
            - Route: Railroad
          - Plains Land 53,31:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 53,32:
            - Owner: The Iroquois
            - IsRiver: true
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 52,32:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 51,33:
            - Owner: Brazil
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
          - Desert Land 50,33:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 50,32:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 49,31:
            - Owner: The Iroquois
            - CityID: 10639
            - Population: 36
            - City: Brasilia
            - Route: Railroad
          - Desert Hills 48,31:
            - Owner: The Iroquois
            - Improvement: Fort
            - Route: Railroad
          - Desert Land 48,32:
            - Owner: The Iroquois
            - Improvement: Landmark
            - Route: Railroad
          - Desert Land 47,33:
            - Owner: The Iroquois
            - Resource: Wheat
            - Improvement: Farm
            - Route: Railroad
          - Coast 46,33:
            - Owner: The Iroquois
        
        ### 139
        - Type: UnitMoved
        - Unit:
          - Level: 8
          - AI: FastAttack
          - Unit: Tank
          - ID: 15820
        - Player: 2: Indonesia
        - Tundra Land 47,47:
          - Owner: City-State Raqmu
          - IsRiver: true
          - Improvement: Farm
          - Route: Railroad
        
        ### 140
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 18986
        - Player: 2: Indonesia
        - Plots:
          - Desert Hills 61,22:
            - Owner: Indonesia
            - Resource: Gems
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 61,23:
            - Owner: Indonesia
            - Resource: Maize
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Hills 62,23:
            - Owner: Indonesia
            - IsRiver: true
            - Route: Railroad
        
        ### 141
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: FastAttack
          - Unit: Tank
          - ID: 16621
        - Player: 2: Indonesia
        - Plots:
          - Plains Hills 56,33:
            - Owner: Indonesia
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Plains Land 57,32:
            - Owner: Indonesia
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
        
        ### 142
        - Type: PlayerDoneTurn
        - NextPlayer: 3: Poland
        - Player: 2: Indonesia
        
        You, Gajah Mada (leader of Indonesia, Player 2), are making strategic decisions after turn 425.
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
    - You are Gajah Mada, leader of Indonesia (Opponent 2).
      
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
      - Name: Indonesia
      - Uniques:
        - Unique Unit: Kris Swordsman, Replacing Swordsman (Requires technology: Iron Working)
        - Unique Unit: Djong, Replacing Galleass (Requires technology: Guilds)
        - Unique Building: Candi, Replacing Garden (Requires technology: Theology)
        - Unique Improvement: Kampong (Unique Indonesian Improvement. The Kampong can be built by Embarked Workers on Coastal and Lake Tiles, and not next to another Kampong.
          Each Kampong yields Food, Production, and Culture.); Requires technology: Sailing
        - Civilization Ability: When you gain a City, one of 3 unique Luxuries (//) will appear nearby. +5% to unique Yield and Golden Age duration modifiers from Global Monopolies; +2 to Yields and Happiness from Global Monopolies.
      - Leader: Gajah Mada
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
      - Electronics: Allows you to build the Police Station, increasing City security level.
        Completing it would unlock: Alternative Energy, Telecommunications
      - Satellites: Allow you to build the Apollo Program, a project necessary to win a Science Victory.
        Completing it would unlock: The Internet, Lasers
      - Mobile Tactics: Allows you to build the Mechanized Infantry, a fast and versatile late world Unit that doesn't require any resources.
        Completing it would unlock: Stealth
      
      ## Policies
      - Martial Spirit (Level 2 Tenet of Ideology Autocracy): Martial Spirit: +25% Combat Strength when attacking in melee for 50 turns, scaling with world speed. War Weariness reduced by 25%, and Razing Speed is doubled.
      - Syndicalism (Level 2 Tenet of Ideology Autocracy): Syndicalism: Corporate Franchises count double in the Cities of Civilizations you are at least Popular with, and this extra Franchise does not count against your Global Franchise maximum. Can establish 5 additional Franchises in foreign Cities. +2 Production from all Corporation Offices.
      - Third Alternative (Level 2 Tenet of Ideology Autocracy): Third Alternative: Quantity of Strategic Resources produced (including Paper) is increased by 100%. Reduces Unit Gold Maintenance costs by 25%.
      - Futurism (Level 1 Tenet of Ideology Autocracy): Futurism: Strengthens Tourism of Historic Events generated by the Palace. +2 Culture from Great Works. Earn 50 Tourism when you conquer a city for the first time, scaling with Era and city size.
      - Police State (Level 2 Tenet of Ideology Autocracy): Police State: +3 Local Happiness from every Courthouse, and +10 City Security from Police Stations. +100% Production towards Courthouses and Police Stations.
      - New World Order (Level 1 Tenet of Ideology Autocracy): New World Order: -2 Unhappiness from and Distress in all Cities. Police Stations and Constabularies provide +3 Culture and +5 Production, and are constructed 100% more quickly.
      - Mare Nostrum (Level 2 Tenet of Ideology Autocracy): Mare Nostrum: +1 Oil and Coal for every City-State Alliance. +2 Production and Culture to Atolls, Fishing Boats, and Offshore Oil Platforms. Naval Ranged Units gain the Mare Nostrum Promotion.
      - Lebensraum (Level 1 Tenet of Ideology Autocracy): Lebensraum: Receive 10 Culture and Golden Age Points when your borders expand, scaling with Era. Citadels may also be built in foreign territory adjacent to your borders. Retain tiles after razing Cities.
      - Iron Fist (Level 1 Tenet of Ideology Autocracy): Iron Fist: Vassals can no longer be liberated by other Civilizations or the World Congress, and capitulated vassals can no longer rebel. Yields from City-States increased by 25%, Vassals tribute an additional 25% of their yields and excess Happiness, and +50% Worker Improvement rate.
      - Lightning Warfare (Level 2 Tenet of Ideology Autocracy): Lightning Warfare: +3 Movement for Great Generals. Gunpowder units gain +15% attack and ignore enemy ZOC; Armored units gain +15% attack and +1 Movement.
      - Liberty (Continuing Progress Branch):
        - * +2 Gold in every City.
        - * +25% Tile improvement rate.
        - * A Worker appears near the Capital.
      - Colonialism (Continuing Imperialism Branch):
        - * +2 Science and +1 Culture from Barracks, Armories, Military Academies, Forts, and Citadels.
        - * Each unique Global Monopoly modifier is increased by an additional 10% if it's percentage-based, or +3 otherwise.
      - Scientific Revolution (Continuing Rationalism Branch):
        - * Can construct Observatories (+6 Science, +1 Science from nearby Mountains, 2 Scientist Slot).
        - * +2 Science from Jungle and Snow.
      - Free Trade (Continuing Industry Branch):
        - * Earn Great Merchants 50% faster.
        - * +5 Gold from International Trade Routes.
        - * -2 Unhappiness from Poverty in all Cities.
      - Nobility (Continuing Fealty Branch):
        - * +1 Happiness and +2 Gold from Castles.
        - * +2 Gold from Armories.
        - * +100% Production towards Castles and Armories.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Regimental System (Continuing Imperialism Branch):
        - * Earn Great Generals and Great Admirals 33% faster.
        - * Great Generals and Great Admirals gain the Regimental Traditions Promotion (+10% Leadership Combat Bonus and +1 Tile Radius).
        - * +2 additional copies of the unique Luxury Resources from expending Great Admirals for their Voyage of Discovery ability.
        - * Military Units can be upgraded in territory owned by Vassals and friendly City-States.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Civilizing Mission (Continuing Imperialism Branch):
        - * Retain all buildings from conquered Cities.
        - * Receive 75 Gold when you conquer a city, scaling with Era and City Population.
        - * +10% Production toward Buildings, with an additional +10% Production per Era difference between your current Era and the building's Era in all Puppeted Cities and Cities with a Courthouse.
      - Refinement (Continuing Artistry Branch):
        - * +2 Culture from Great Works of Art.
        - * 1 Specialist in all cities does not produce Unhappiness from Urbanization.
        - * +1 Culture from Specialists.
      - Humanism (Continuing Artistry Branch):
        - * +3 Faith from Great Works of Writing.
        - * -25% Golden Age Points needed to trigger a Golden Age.
        - * +1 Happiness from all Guilds.
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
        - Rationale: CRITICAL UNIT MAINTENANCE REDUCTION & PAPER DUPLICATION: Selecting Third Alternative to immediately reduce unit gold maintenance by 25%, providing massive relief to our -296 GPT deficit. Additionally, it doubles our strategic resource production (including Paper), increasing our Paper from 10 to 20 to allow our staff to produce more diplomats and secure city-state alliances for the upcoming World Congress voting session in 10 turns.
        - Policy: Third Alternative
    - #1:
      - toolName: set-research
      - args:
        - Technology: Electronics
        - Rationale: ELECTRONICS TO TELECOMMUNICATIONS PIPELINE: Maintain Electronics as the next queued technology (completed after Advanced Ballistics in 3 turns). It unlocks Police Stations (+10 City Security, +3 Culture, +5 Production under Autocracy) and serves as the gateway to Telecommunications and high-tier globalization tech, supporting our long-term diplomatic victory infrastructure.
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 3
        - Private: 90
        - Public: 90
        - Rationale: MAXIMIZE POLAND RELATIONSHIP TO TRADE FOR DELEGATES: Poland is our close friend and follows Autocracy, holding 16 delegates. With our diplomat schmoozing in Krakow, maximizing our relationship to 90/90 ensures they are highly receptive to trading their World Congress votes to us for Global Hegemony, which would push us past the 41-vote victory threshold.
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 50
        - Rationale: ALIGN RELATIONSHIP WITH FRIENDSHIP DECLARATION: Correcting the previously negative relationship to a positive 50/50 stance to match our active public Declaration of Friendship and shared vassalage under the Iroquois, maintaining peaceful neighbor relations.
        - Public: 50
        - TargetID: 5
    - #4:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Mobilization: 20
          - Science: 50
          - Gold: 100
          - Production: 80
          - Happiness: 70
          - Defense: 80
          - GreatPeople: 50
          - Religion: 90
          - Offense: 10
          - TileImprovement: 70
          - Diplomacy: 100
          - Culture: 50
        - GrandStrategy: UnitedNations
      - rationale: RESOLVE GOLD CRISIS / CONVERT BELGRADE FOR DELEGATES: Adjusting flavors to immediately combat our severe -296 GPT deficit (Gold: 100, Production: 80) to force cities off research/art projects and onto wealth generation before bankruptcy in 2 turns. Diplomacy (100) and Religion (90) remain highly prioritized to spread Hinduism to Belgrade (64,20) within 12 turns, allying them for 2 critical delegates and denying them to the Iroquois. Defense (80) is slightly reduced since our vassalage under the massive 377k military Iroquois ensures safety from major invasions.
  - tokens:
    - inputTokens: 71475
    - reasoningTokens: 14902
    - outputTokens: 572
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Progress**
            
            My thoughts are currently focused on evaluating our diplomatic standing. With 29 delegates secured and Brazil as a key ally, I'm assessing how best to leverage these assets towards a United Nations victory.
            
            **Assessing Global Influence**
            
            I'm currently dissecting the diplomatic landscape, noting the vote counts for the UN. It seems our potential allies and rival blocs are in flux, especially with the recent "Open Door" resolution passing and shifts in minor civilization allegiances, particularly concerning Zanzibar. My focus is now on how these recent events impact our path to victory.
            
            **Realigning Strategic Alliances**
            
            My focus has shifted to analyzing our current city-state alliances after securing Prague and reaffirming Zanzibar. I'm re-evaluating our influence with Belgrade, Raqmu, Cape Town, and Wittenberg, especially given Indonesia's shifting allegiances and the Iroquois' growing sway over Wittenberg.
            
            **Leveraging Diplomatic Assets**
            
            I've realized my understanding of current alliances was flawed. The "Sphere of Influence" resolutions are key; I now understand why Indonesia is an ally despite lower influence and how we've secured permanent allies in Prague, Winchester, and Wittenberg. This significantly shifts our path to victory.
            
            **Analyzing Global Hegemony**
            
            I'm now focused on the looming Global Hegemony vote. With Indonesia having 29 delegates and Brazil 26, I'm re-evaluating our strategy, especially considering our permanent alliances with Prague and Wittenberg through Indonesia's Sphere of Influence.
            
            **Securing Delegate Advantage**
            
            I'm recalculating our path to victory, realizing the 41-vote requirement. With 29 votes currently, securing alliances with Belgrade, where Iroquois currently holds sway, presents a significant opportunity to increase our delegate count and undermine rivals.
            
            **Revising Diplomatic Outlook**
            
            My focus is now on re-evaluating our delegate count. It seems several city-states were defeated, impacting potential alliances. I'm carefully checking the list for any overlooked opportunities or threats, especially concerning Iroquois occupations.
            
            **Recalibrating Vote Count**
            
            My thoughts are now focused on the newly confirmed occupied city-states. This significant shift in available delegates requires a complete recalculation of our path to victory, especially as some of these occupations were unexpected.
            
            **Recognizing Vassal Status**
            
            I've just realized I am a capitulated vassal of the Iroquois. Their overwhelming military strength makes independence suicidal for now. This drastically alters our diplomatic objectives and the immediate path to victory.
            
            **Clarifying Wartime Status**
            
            My focus is now on our actual diplomatic and military engagements. It appears my previous assumptions about being at war with both the Aztecs and Shoshone were incorrect. A recent review of our declarations and relationships indicates a declaration of friendship with the Aztecs, which significantly changes the strategic landscape.
            
            **Identifying Shared Allegiance**
            
            I'm realizing that both Indonesia and the Aztecs are vassals of the Iroquois. This shared allegiance fundamentally shifts my understanding of our current geopolitical position and diplomatic maneuverability.
            
            **Reassessing Diplomatic Ties**
            
            My focus is now on the Shoshone and our guarded stance. It's clear the previous assumptions about our relationship were mistaken, and this ideological difference significantly impacts our potential for future alliances or conflicts.
            
            **Understanding Vassal Dynamics**
            
            I'm now focused on the implications of the Iroquois having capitulated and vassalized Indonesia, the Aztecs, and Brazil, while also having a defensive pact and DoF with Poland. This realization fundamentally alters our entire diplomatic and strategic position.
            
            **Analyzing Global Capitulation**
            
            I am now processing the massive shift from the Iroquois' global capitulation. Their former vassals, Indonesia, Aztecs, and Brazil, are now independent, drastically changing the delegate count and my diplomatic priorities. This requires a complete rethink of my path to victory.
            
            **Confirming Victory Condition**
            
            I'm now confirming our immediate path to victory. The Shoshone capital's status is critical; if the Iroquois capture it, they win via Domination. I must ascertain if a Diplomatic Victory is still achievable before then, checking the World Congress timer.
            
            **Calculating Vassal Voting Bloc**
            
            I'm now meticulously analyzing the World Congress voting mechanics, specifically how vassals are compelled to vote. It appears they must either vote for themselves or their suzerain, which significantly impacts the Global Hegemony outcome. My focus is on accurately predicting this bloc.
            
            **Leveraging Vassal Status**
            
            I'm now recalculating our potential delegate count, realizing we can vote for ourselves as Indonesia, securing our 29 delegates. I'm exploring alliances, particularly with Belgrade, by spreading Hinduism, to gain the additional 12 delegates needed for a diplomatic victory.
            
            **Analyzing Trade Route Limitations**
            
            I'm now realizing how the "Shared Ideology" policy impacts trade routes. This means our potential allies and rival blocs are in flux, especially with the recent "Open Door" resolution passing and shifts in minor civilization allegiances. My focus is now on how these recent events impact our path to victory.
            
            **Analyzing Gold Flow**
            
            My current focus is on our substantial gold deficit. I'm scrutinizing trade deals and unit maintenance costs, realizing our GPT is severely impacted by paying Brazil and the Iroquois for resources and open borders, while our own lucrative trade routes are expiring soon.
            
            **Analyzing Gold Expenditures**
            
            My thoughts are now focused on our significant gold deficit. I've identified numerous outgoing trade routes from Jakarta, despite our substantial income. The "Global Peace Accords" resolution's 25% increase in unit maintenance for our 69 units is a key factor contributing to our negative GPT.
            
            **Prioritizing Economic Reforms**
            
            I'm now intensely focused on my substantial gold deficit. I'm scrutinizing trade deals and unit maintenance, realizing our GPT is severely impacted by payments for resources and open borders to Brazil and the Iroquois. My next step is to analyze policy options to boost gold generation.
            
            **Reviewing Policy Selections**
            
            I'm reviewing our policy choices after last selecting Enlightenment. It seems I need to reconsider the available technology options and their strategic implications given our current research progress, and confirm the next policy selection.
            
            **Choosing Policy Direction**
            
            My thoughts are now focused on selecting the most beneficial policy. I'm weighing the immediate gold benefits of "Free Trade" against the long-term strategic advantage of a free technology from "Enlightenment," considering our current research and diplomatic goals.
            
            **Exploring Autocracy Options**
            
            I'm now intensely reviewing Autocracy tenets, specifically "Third Alternative." Its 25% reduction in unit maintenance costs is incredibly appealing given our current gold deficit and the high upkeep on our 69 units. I need to confirm if we have enough tenets adopted to unlock this Level 2 tenet.
            
            **Prioritizing Economic Stabilization**
            
            I'm now intensely focused on my substantial gold deficit, realizing bankruptcy is imminent within two turns. Adjusting city projects from research and arts to gold generation, and reviewing our high flavors in religion, diplomacy, and defense will be crucial for short-term survival before considering policy changes.
            
            **Adopting Tenets**
            
            I am now intensely reviewing Autocracy tenets. "Third Alternative" offers significant immediate relief with reduced unit maintenance and doubled strategic resources like Paper, which can boost diplomat generation. I need to confirm if I have enough tenets adopted to unlock this beneficial Level 2 tenet and assess its immediate impact versus other options.
            
            **Selecting Policy & Tech**
            
            I'm now focused on unlocking "Third Alternative" in the Autocracy tree to address our critical gold deficit and boost diplomat generation via Paper. Simultaneously, I'm evaluating "Satellites" as the next research target to potentially enable the Apollo Program, which could be crucial.
            
            **Revising Research Path**
            
            My focus is now on the critical choice between "Satellites" and "Electronics." While "Satellites" offer map reveal, "Electronics" leads to "Telecommunications," vital for Diplomatic Victory. The Iroquois' inability to invade makes police stations less urgent, pushing "Electronics" and its subsequent tech path to the forefront for victory.
            
            **Prioritizing Research and Policies**
            
            I'm now reassessing our research path, weighing "Satellites" against "Electronics." While "Satellites" align with science victory, "Electronics" unlocks "Telecommunications" for Diplomatic Victory. I'm also confirming "Third Alternative" tenet adoption to mitigate our gold deficit, and considering the strategic value of Police Stations versus immediate needs.
            
            **Securing Permanent Alliances**
            
            I'm now meticulously reviewing our permanent city-state alliances. Prague, Winchester, and Wittenberg are locked due to Sphere of Influence, and Zanzibar is newly secured as an ally, protected by the "Cold War" resolution. This stable bloc of four is a significant asset I'm confident in.
            
            **Analyzing Vulnerable Alliances**
            
            I'm now scrutinizing our city-state alliances for vulnerabilities. With Prague, Winchester, and Wittenberg secured by "Sphere of Influence" and Zanzibar protected by "Cold War," our core bloc is stable. Belgrade, however, is a concern, with the Iroquois holding high influence and the city having active quests that could shift allegiances.
            
            **Spreading Religion for Influence**
            
            I've discovered Belgrade desires Hinduism as its majority religion. With our significant faith generation, I can deploy an Inquisitor or Missionary to convert the city and secure a crucial 206 Influence boost, solidifying this vital alliance.
            
            **Leveraging Espionage Options**
            
            I'm now exploring how our agents can directly influence city-state allegiances. Rigging Belgrade's election seems promising to secure crucial delegates and diminish the Iroquois' influence there, especially as our spy is already en route. I'm checking if this tactic is viable for other city-states, though most seem to have stable alliances already.
            
            **Targeting Belgrade's Allegiance**
            
            My focus has shifted to actively contesting Belgrade's allegiance. Realizing it's the only city-state not firmly aligned with Indonesia or Brazil, I'm prioritizing flipping it to increase our delegate count and reduce the Iroquois' influence, which would be a significant strategic coup.
            
            **Analyzing Ideology Influence**
            
            I'm now deeply analyzing the World Congress voting, specifically how the "World Ideology: Autocracy" resolution grants delegates. The realization that Indonesia, Iroquois, Poland, Aztecs, and Brazil all following Autocracy nets an additional 5 delegates each is a significant factor. My focus is on understanding how these blocs will vote, especially given my vassal status to the Iroquois.
            
            **Securing Key Delegate Votes**
            
            I'm now intensely focused on securing Poland's 16 delegates. Their incredibly high opinion of us, coupled with our Declaration of Friendship and shared Autocracy ideology, makes me believe we can influence their vote in the World Congress, especially with our diplomat actively schmoozing in Krakow.
            
            **Leveraging Diplomatic Trade**
            
            I've realized we can secure Poland's 16 delegates by trading for their votes in the World Congress, giving us a total of 45 votes, enough for victory. I'm also investigating if a similar trade is possible with the Aztecs and assessing our diplomat's location in Rio de Janeiro.
            
            **Securing Crucial Votes**
            
            I'm now confirming that Brazil won't trade votes due to their own victory aspirations. Poland, however, with their high opinion and lack of competition, presents a clear path to acquiring their 16 delegates through trade. My immediate focus is on securing our existing alliances, wooing Belgrade, and ensuring Poland is willing to grant us their crucial votes.
            
            **Assessing Master Relations**
            
            I'm now re-evaluating my relationship with the Iroquois, our suzerain. While I can't attack them as a vassal, maintaining a hostile relationship might invite negative modifiers. I'm weighing whether to improve relations for a more stable vassalage or keep it low to prepare for a future independence bid.
            
            **Analyzing Diplomatic Threats**
            
            I'm now reassessing my relationships, noting the Iroquois' current dislike and our fear of them. I'm also concerned about the Aztecs, whose relations have soured to Public and Private -100, despite a previous DogS. My priority is to mitigate these negative diplomatic standings before they impact our victory.
            
            **Adjusting Diplomatic Sentiment**
            
            I'm now reassessing my diplomatic standings, particularly with the Aztecs, where a Declaration of Friendship seems at odds with their negative sentiment. I'm prioritizing adjusting this to reflect our actual alliance and prevent unintended diplomatic fallout, while also reviewing the negative relationship with Brazil, our primary rival.
            
            **Adjusting Diplomatic Relationships**
            
            I'm now fine-tuning our city-state relationships. Permanent alliances with Prague, Wittenberg, and Winchester are confirmed. I'm elevating Zanzibar to 100/100 to solidify our new alliance and strategically boosting Belgrade to 100/100, ensuring our focus on securing their critical quests and influence. I'm also maintaining current negative standings with the Shoshone, Aztecs, and Brazil, while reassessing our vassal position with the Iroquois.
            
            **Adopting Crucial Tenets**
            
            I'm now focused on resolving our severe gold deficit. Adopting the "Third Alternative" Autocracy tenet is paramount, promising a 25% reduction in unit maintenance and doubling strategic resources like Paper, crucial for diplomatic maneuvers and potentially saving 100-150 GPT. This is a clear priority over "Free Trade's" +65 GPT.
            
            **Prioritizing Economic Stability**
            
            I'm now intensely focused on resolving our critical gold deficit, as bankruptcy looms. I'm re-prioritizing city projects towards gold generation and setting city flavors to heavily favor Wealth, recognizing the immediate need for economic stabilization before enacting policy changes.
            
            **Prioritizing Economic Stabilization**
            
            I'm now intensely focused on my substantial gold deficit. I'm re-prioritizing city projects towards gold generation and setting city flavors to heavily favor Wealth, recognizing the immediate need for economic stabilization before enacting policy changes.
            
            **Implementing Diplomatic Strategy**
            
            I am now implementing the refined strategy, securing Poland's delegates through improved relations and preparing to trade for their votes. Simultaneously, I'm adjusting my relationship with the Aztecs to reflect our actual alliance and prevent unintended fallout. My focus is on consolidating these diplomatic wins to secure victory.
            
            **Adjusting Diplomatic Relationships**
            
            I'm now fine-tuning our city-state relationships. Permanent alliances with Prague, Wittenberg, and Winchester are confirmed. I'm elevating Zanzibar to 100/100 to solidify our new alliance and strategically boosting Belgrade to 100/100, ensuring our focus on securing their critical quests and influence. I'm also maintaining current negative standings with the Shoshone, Aztecs, and Brazil, while reassessing our vassal position with the Iroquois.
            
            **Revising City-State Strategy**
            
            I've realized my previous plan to directly set city-state relationships using `set-relationship` is impossible, as that command only applies to major civilizations. I need to pivot my strategy for influencing Belgrade and Zanzibar, focusing instead on in-game actions like quests and spreading religion to secure their allegiance.
            
            **Refining City-State Engagement**
            
            I've recognized that directly manipulating city-state relationships via commands like `set-relationship` is not feasible. My strategy must now shift to influencing Belgrade and Zanzibar through in-game mechanics, such as completing their quests and actively spreading our religion to gain their allegiance.
            
            **Adjusting Diplomatic Levers**
            
            I'm now focusing on subtle diplomatic adjustments, realizing direct `set-relationship` commands are impossible. My strategy will pivot to in-game actions, like completing quests and spreading Hinduism to Belgrade, to secure the city-state's allegiance and influence, rather than trying to force an outcome.
            
            **Refining Economic Priorities**
            
            My focus is now on fine-tuning our city flavors to combat our severe gold deficit. Prioritizing wealth generation over research and arts is crucial to avoid bankruptcy, while maintaining high diplomacy and religion to secure Belgrade and deny them to the Iroquois. Defense remains secondary due to our vassalage.
            
            **Adopting Crucial Tenets**
            
            I'm now focused on resolving our severe gold deficit. Adopting the "Third Alternative" Autocracy tenet is paramount, promising a 25% reduction in unit maintenance and doubling strategic resources like Paper, crucial for diplomatic maneuvers and potentially saving 100-150 GPT. This is a clear priority over "Free Trade's" +65 GPT.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: Dr1bNSjoGsI6ApA2
          - toolName: set-policy
          - input:
            - Rationale: CRITICAL UNIT MAINTENANCE REDUCTION & PAPER DUPLICATION: Selecting Third Alternative to immediately reduce unit gold maintenance by 25%, providing massive relief to our -296 GPT deficit. Additionally, it doubles our strategic resource production (including Paper), increasing our Paper from 10 to 20 to allow our staff to produce more diplomats and secure city-state alliances for the upcoming World Congress voting session in 10 turns.
            - Policy: Third Alternative
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: FbaVORayysJ4AiwB
          - toolName: set-research
          - input:
            - Technology: Electronics
            - Rationale: ELECTRONICS TO TELECOMMUNICATIONS PIPELINE: Maintain Electronics as the next queued technology (completed after Advanced Ballistics in 3 turns). It unlocks Police Stations (+10 City Security, +3 Culture, +5 Production under Autocracy) and serves as the gateway to Telecommunications and high-tier globalization tech, supporting our long-term diplomatic victory infrastructure.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: ZY5iEEL15YvTVF9e
          - toolName: set-relationship
          - input:
            - TargetID: 3
            - Private: 90
            - Public: 90
            - Rationale: MAXIMIZE POLAND RELATIONSHIP TO TRADE FOR DELEGATES: Poland is our close friend and follows Autocracy, holding 16 delegates. With our diplomat schmoozing in Krakow, maximizing our relationship to 90/90 ensures they are highly receptive to trading their World Congress votes to us for Global Hegemony, which would push us past the 41-vote victory threshold.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: e0kKALt7OoEc8io6
          - toolName: set-relationship
          - input:
            - Private: 50
            - Rationale: ALIGN RELATIONSHIP WITH FRIENDSHIP DECLARATION: Correcting the previously negative relationship to a positive 50/50 stance to match our active public Declaration of Friendship and shared vassalage under the Iroquois, maintaining peaceful neighbor relations.
            - Public: 50
            - TargetID: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: dtP6sLyFoNDayfic
          - toolName: set-flavors
          - input:
            - Flavors:
              - Mobilization: 20
              - Science: 50
              - Gold: 100
              - Production: 80
              - Happiness: 70
              - Defense: 80
              - GreatPeople: 50
              - Religion: 90
              - Offense: 10
              - TileImprovement: 70
              - Diplomacy: 100
              - Culture: 50
            - GrandStrategy: UnitedNations
            - Rationale: RESOLVE GOLD CRISIS / CONVERT BELGRADE FOR DELEGATES: Adjusting flavors to immediately combat our severe -296 GPT deficit (Gold: 100, Production: 80) to force cities off research/art projects and onto wealth generation before bankruptcy in 2 turns. Diplomacy (100) and Religion (90) remain highly prioritized to spread Hinduism to Belgrade (64,20) within 12 turns, allying them for 2 critical delegates and denying them to the Iroquois. Defense (80) is slightly reduced since our vassalage under the massive 377k military Iroquois ensures safety from major invasions.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: Dr1bNSjoGsI6ApA2
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1/agd88/zwJYtoRf0ujS4HOBaT0y4U995BmAiiSyAzce2Cn04SIGlFrK5OMHru/dclnJexlIaHGVRvLZiPDVOC/SMtyUKedeOQGW1NSU1rPrP0Ol/r0oyytqT2o+f3egY3ayfg9gSxggTixVHTXFZvdYH5XHbO0xE8s7WVCmLw8jp8H4ckF7F1p3Clwy/2Xx4ckrwbXpaP/8s/U7La6sdDLy+teiJkyDg5AHyw2tI2wzHBoFcRLTWS3vr66eAwDEk4UlJFCTz5uF7hgCmQH37Y+M907BaYpSU4VtOAfYCfcUghFhdhb2H3uPJFMNqYGStJxm6Rwcsjv61yXjoyRXUiVvxSt1E/u08mIPlososUXbEfpnt3Y0DgEg4cm8mSO6NRr+2dUhPELlO1eQfp5snPX7lX/CT0VBEuPuP8fqnRtmeu7v+Q8JPJg2J2be1A10gnY6Y9yrtA84FHaN/DWxNb/iE4gcC4F+0z9IC0h3K9hC0IhTe4ctpmRatUq7O44z4pCmy5iWUel9DB6+KI+bVSF1/J7Xfr09vUMXlqrghIxV0RyO1vZqE6i6NUfRkX8Pe5TjWJujZgaUPF5CSDqzNjfO5f6y3aG5SnFUuKtZKc9i4zhxjEtiIos98pUYJTgHaUjCf5S4LU8c3Bj4TAV78lo82C4cWDRVPSKZ0R2NKn8Ye1XA/Mg0zOTeHIv2G0r0Mkurwks8VGBqvbxM7J7LS8VAm0mHv57Ll7LdvI7SZ+RMOHbyKsPbV/FRUqjzoR//ft55UBqXMLZw2SHv6Xzx4IZ8QXV/CdqfuQuqiOo7yLI/2xMHW3UBlDTdMpEJgTfpJXYTqHqbHRbHMqm9fMspc93eDIX8HEOM1qtwo4iAtTJGM+jQYEADg6iKezP3eL14g1wY6KNTmfXZzgmrnI0+6wBML1wpeM/o/9IVjpN7fcI7eiXhNGp5sMnpGVgbNlnJdNIEPEhlBOsgufQiz15tXKwLVuPILq7kHm6NEd97L5R4aEk9D8yOEhWBlgfiaH6jN8VF2z+CN2+EfL3XGjQIzWxnNK0yMGEPx7FJ8UW9d3z2MFDzis4HxfCozGq8DHm6gk/MdhBzDC5rYw+8/84q1pWCKmrFKRWppFQFbJuMNoOUk2SkAzwjy6ZLWidTPuBJJD8Pu3MdPGve+5FHrHbRQM+uWisYbBtqo2B5TqPZ6xL5T/DhjmWzOTq0dNnIYfmPpNnQTMeUoH4mFh/CwuVDyXNmNbsR8NdjaKFhKA+drpPG5y95XImnEEXVw8XETBI5qDZFQbywuN3gvG3yUXBF81Z/XJ5pGklQFpqwc64bxKMSfbX5xgx138+acV0gq5CEP3CRAAMG6XIRFfgvcN+ws9FExh8bXjONCLfqH+apgg+K0SgSEcQxjAPHe2dWwVeV0gv028j0iZm3eRODOy+ReuuMEr06bRwJykWezzPSoB5E61c9X/LDAt8gAdAi0VOzED3DOgat5xlIkWuQmpn7g2VXbX7azuYH+Fv1WSBhPXvqs2PIn9II5XIYzBgWz5rWRxFNLbgBv5DA+0L/jKL8KaJ8yF/mpFCWSOHMgVaetOxIWt5o2wQbdENsHxSSg++ddu0xVP24UwnH7kBpJhKL29QYqXWRcPGupXlDI6L8875Tlz9GZ6fpRE2d0yc/QEysf1X8vytSjuy+LDEmKzJi0lTQ/LCWDZ3gewN74Kda+vrF1Wr8nwJayy6RItZh0nTZAqUblscUr2sIG+uXfpBWz43v+lhe1Yu57vhR1Q1/aoIplScsv6hEVTFrq89OVmWTB9MHTMykAhOEHKA1LtuM8ja2kIfvpntSCWf7myJF7dsUXIEob89U0LpY7QAzyE7V/moVtr6nlOL6vcXGS3vWcSuR+LEw8nUb0e2j2r9dOjkU1vtq6md9qIQp2nwimT+LVOUzV6mfIGUmnXxbVCY8gJ+KWrBtQ+H8DUvqK1sf9V8rt8hvvqyOEJ5n1c2st9bgT6JHAgrsim1w6qtkljHIy4ztJMUKJBB1xsqED4nhfAMMPNbsyEc5p2fVsgw89mkXjS5dZC395dUWTly8Vay9SEkh2IwL3+M2+K1353MZmOo8ElzDP7U5TFMwXsl5j9flNz8OhHdTAuCy8MTtsgpbSVyyYYUA2g90LXJ5nEcFeRlCHE74guDtn6oXJytVM1nFSBkQXpQc8kb36m9y5VY8gGblTY+FE9/5gKbRbLSDD1dv4PcXedNsqRX6bRksNSrUAAIwwNTkqnWeteD1B/tgr7i+QXGlfMjKQL+gJ/pfgxrNhzGJ54UyCAGDkJUzBjDpCfLhJgMGbII+q6p71blXoY9zHWMCxOMfrPZsSLJz6Ubz8v4uGo4tfwv/yDOfkCTt8WaTJt7nqGcwChIBmBVmSodZ/xGZuSlgG5oUhI7IM51rRyghpBlE89dYX5w9ccfZO8QAKDf/SSzX9v4ftqOJoea4zW+SAKWOT5kLu/XpHIQW4qqMjJbKqxSfAZc46Ubyl+Rd1MFCwLvHmpLakpsUYzzVLlpUbmShVSbxXPmCjOrqyp19LwoM5mK6ua2SKeu1h4xuGKY3ZEVRHtxnty16JEV48bNpSVTOuDnCI+jg72L5dTr9k1b1E78+UTUg9rSdMeDCFCPPYKRN5uvWAKlfABkU1ct1xas3E1/dmx0TiMFxe42iE+W+BUYPiOeDxbACcOWVFSDwjoJWuMN1odg/4v2Qqh1Yvz2Hbkv8pzvyzW6oF1dSo3UdfVdC8HYJqzYqjZZyg4HOMK/62iUQ5tyujthOQ7PDolA/hpYFYGeip5EzWIUiVjqqQpA2bHL8cpz20+BzP7xcl+Cq2pm7MVV0SnYdIiHTPdjR1ToHp9HjCXqwTr09CB8gG2iBEtBgvpWnbPBWbcvZVy+gUO6kwlHMDhTKgrRK9vtEoJ2u1wHzhyasJJOAVHdPSTz4sHSqqvcRFByaS5SX6Shx8sNRdHVs6nnXwyO6j8TAIj0Yk+kU1Aq3p3m8rOiCBZM1NIM1mZVRu0VA3xdkwk9Kc9+j5zZgNebS8ntRQ8D6b1ruzCRBgClEhEPq13O0lolsPBq9XrAxLAIl0XeslKWhjECQzyNasQUWANERPe3CXymzw/sVWy0taHzghwvRb5+dyrDMmh+n0RyG1hoVnGao6j6S0FsNioqrz/LQz7DKI8ymUgnbs4ouOaVfevlO56eeTUmVKULbbCJkD4ZKNQKhKxW0m4v2WcAY2xBiNy+MI5yzSq9K9cyZ5ltA5ZSwMtlELCnB8ktNn9XngiDE1QkC7xAwKxQPeM9Ojhwum9wIO1XVGs309w74ZNX8ZUpPWFSMu4vJNSel0a4cp3iJfFYqs61zsVaONxuZFIuDAr5vA2NnKz0sEEfh/kF0RHo0pbBEU4/IZI3eeIQJucMo2EGrWVVLjCPFrxvw4/2NdBjKFan+g3By2aCkZCiKEl/62YJlUK/dHvYjXtASNySZd3vi+WrfecwktPPuE/WBryfp5sKe7d7bhLNFn3/GHJIMg/pUt1Q/vqy5ro51qoo8aqerKcGaouh/iN1FpNu6ytvxu0ARuFRENFaaFXHZ9CKtZ9xNYYu9Jt7++9G/mlxTWIZ1cUC1uTwTQrd37BIwg3vrF0Qv2+sPk09hzxpoeGO6b4izc1jt+N8YIV11CUoIPpE0Y4HD2jn5FwT0t4dzx9gwfDeErcB8h3aROtcoXHNiCfZTYyFBC+1x6FCYQiHSy6gIburFesTVxSKU+XT0vipOVDQrWw/RChzGiEfL5CoLwp3bbNpNiiMllrV727ftjYGzhXErFDthWNSpKXUIXFeUZq1zaUp6VHJgtjfQB6tC1Npqzn/o2fgMhhJgwudItwZhjlIJE3vepcrLfAIkIC23WKhIwE2DBkRPJ3dNzCHOj2iK1P52fZz2CHkvV7JYjJ8lGeCVbaEbd0gseZ83Wed7eR+rHKfV6ke374EnlteDs9aomIcCR5+L1Cwv1I1UEC3cMg5IdLOEHWe9Ac8RywrHsSEYsV/i2j6b1ptzT6oZfOB7em4SP3GsPc15443aOV3ire4sCsi/BPQIIeWgN5dHE2f5OU8Koq7flXv5d3DoNGkYl+yR7vDFzN5vy/QJl7yTFjs0o0XHk53j9xh7Cg/rm7WXMOfurOF/MjF51ER/2qxtotwZPq/vQ/e+TFblCb0tw8SJ9CHCaKTNxpu2rS1qcVsSbbz+DgAuAPhfu7NQcJwXIoHrn59Yl4lYy9Rzimve6WWY5dyRyDuGIpM+ZlAHfyoTtVI3O+U1ZLXvnxMTLq9g71VDyIVL4LX7e2P4uxU2K8ank92PjuB/cQgq32H3veXpuuvZxJPK6LrYGIl3mJOa8Ta24NO4AOkSepa+Sc3pSvjLs6dfpz85plDxTcAT+iz2ruSyO6ufudZul8SjWfXwRNFJb0t0F2yLIGf8QwPvEJsuPyJqzt6tIjqdVyio9ljYYLxiaDTVgRRkGugGDiWWTnIXE3nlhSShfGhcXeGJn+G8pGUxUPyQp4opiDWDMwqX2BrR993RCVNlTlZZ8jB58MMxusIe2ffoaTyS6wH7DdplmWWbCArdsq1QBvS676QUnwiDSsf8zEAXTKpr2s+1TTg0TxkAAjhiRVh4O4pThQdHXrqcxXsusMjQ3EM/5hl9aP7JSQJIfqriWXyf1YoKUGPgw4715KjDB3pExAFNZYAOLHFL577/P6aOkf5KxjAVpgsFnVOJW2zJ883XLagjF9In7hYPVyyv6LOX/BtSBYGGoMPiaUMgJuYsY4U3HKQomg25JVe7zd2baV1tYKmN8VSMhVA8tzBhyetdvX8sx8Ju+2SZGlROYVb7obEyjGl60qMYv9sOxFnw+eluyP4At+iUHIP3KAXeYYBftmZRx1l+hYyesrbzQtmehrsVyqydx7s454O3+Wbsfn8rbdAyG6BLtu5C1Ue+QOWz6KAwALIfhsrIUzZe+KxVTCLl8PxeCoSmd3BtaNDS47ezn8vXm7DYWlBU54IFI6RRQyxWtAodwfiuCjs9Ow1Dtyv2ZYwQgKGRbVDBeizLCHORunn94SFMM/Tk1p+Xfyhn0F4jg5kq+AB+gcgJxthMV5N7Q+76ze74KH8yfGpDwXAxdLeSBJh+n2ww07g8ad2NC5IOq3/gY8BJEUPlN9P5L8b0/LvoUQe8AZ55jeD5OqTtefj26WLCBCsI0yJkzGK5BF7x/oB2I2vleOZkK1tBV1wqbu+v7+utYvcleHG/dcCTuzZZmPnyoieALCYIoudjNEe2lBuCjPm3NUIdQ30osyzwl0awCGbKjpCQ0SfouAyn7YUYdLycRspAzmwmBgu1wszMVhHe6COe0T43ncsOIajLq3oTZmqawymK/wTMWUKH90HE39OuRW2fClvKyrmTm6Zi8G9opWB1TdSTMAnCUqzl9J/p7Zb8HdUdFY/wJyBF55yN5r91MF6BZpCieNphp0fmILhgGecR+YcBUMuqwotFlNlruKjtWDEFY6ogQESNEs9rkuyXIvpqS5O3wc3camu4mDtfzy3sAhpgZP78UHrFbdA8ek1Ywf3HSyUI15I859hbocOq2FaA5ReZWcE+Wel9M+ISTtU12EB44o2YkMKgZkmTPvCoYTzF9uVCw29uFCY8X3LfSp7sfLVrqZK9LgYH2XxG0xUD51XPkH6o/LvxkPf2kheKHmpoFZ+f2C3oidMn1xTi2OCj/DIzQS7lFsGEdrKmGJieYnCeX0shzf+vK/gsuuVW0/NDM2ph6CX5H83S9hiukQL4WsCk5muXacs45HWeUIAQ4EOBr0Lb71AgNyHmfBzWlAPKU1cpi7HCCM+O0tlV56d3W2pGtRRzRJL0O0AoxpVZCbspebGrh/0EZX0NGRyZMKAAcTN5dyl624UQvWpGRGicxWGL4czp8VL5hSbua0QnwwsOSHjJvjG22fUeNmkn6Fa5DKS3M0kdNfocRZE7hvPZQVbwVN1aWvq9+z5ZLZ10+J5oEbuZev5wdDgdjjbb1IWuiVO5SBeA4HVuDL0pljsu1G7dOSAqnk5wp+lqyAVmqx999IKkHg+TxY18ly+5e98piHD7/qQ/pq9XB3EndD4px89+GkgFsyFWgMMEoOhhiW2wtfMoFsvs4DxFbyfgIG7o1vlYCgW6TIRJ4dRokxkFG+7OWiM6zne6iwZPNbZLqKrjevf3AOtIb0VJHyNAoMjAmZ1qeOSSYYxZ57dm4Er3iP0tpKbTz+YKB48oJegjaEae41TlJ6GaG/ukuh2oj/gkqO86Uj34zqQyLqj0Rilk5GPkx+/m+h51k0z5mYdfVcluNEz6iWofWdZKbB7IutSyznGuLti9JW7P8K0sQJgh9MNs9QvgtjULb3hdHaQjcQFHB9Enew+XhlXCwwtCBDVTjVVwsq/SER8usKTEU9lsn6Bwf8trhCQrPA5m8gfBaCyagbEWTwuld4F3+cPzCEiQ9norHOfqSLv2W3PHi8B7cFeY3ATGHHYaW5N8wfJVicAHWkqOrsZhfOL4oSu9WXwlDYRBlc5To2A4qgGRwITOwt75E+vBItAfs6xrGDBXsZJRIviFVXloUphs57gDFbzMHUMkhTlExpKWwHOfcUJivUWyBXRgdPgPBaAGwHhWvwWflL12ZH54uNFnZVB8nEHHz4f0wJJsc/m4kaJPiAb9LqnAbOSBX3sn/qFpJetBONLPr69FXWWwqC8MtSo0Q/YWoW0bo24tHj2/spOrWmPt0gFip8/HYTZ8fFvyQBSFB0nd7pAlbg1aDeXPzU/fMC8Xs/nMmKGqQG2JK971/UpBYwD3klJTNz+V2wXwekeZ1c6kfS0UeOaOxmVNIO/cQ/0t2xDxKAci+wYmeYdVm/fXIthxVmURNkXAkL2y9LuIFITZj7aYCz/BoDgzZWFqpFqfG3sb7MzbF+fAYZI+wdBSxUdpQ+B1fsUKgdX3romwfJwtPSsJLBAadlnHzHBtP58Io3yPdvUneqZ1SL+Y9/ap7P6PLDeIwD1TuX9QS9N6hwcPHtbl9a6kXjBNf8m1qBDxG3rtwLYTdEWnqA3pRXEEhX7QyV7oo/k4+pcWUAQVU1GvYmIWJ6o4QCSbAarXI3ljmjwxRdRwZusmg257ij29nbSfbRhLLfPEv5UDwTUP4ffFjVJULGz8aj3gy0M7h8Hk28UgAFuJgsTYoOb2P0L06CkJsSyIOVycifPXI6Prmul0wdOF3UoWEUB4u4Bh15kr9cAwDQkVf2bTpnHWtEDv07EC1LaWeN+uS7OM/LjJLz17WzZxvcLZ6aq6Mp8MUa+zSpjHNeC0flxsxg66EHn9ZEVejZfemJdHeibKDLuETvACLbx/jk3fQiTg+u5EoPl9/IfZhF5jq9tZA9J4ePmN/0Wbo2X2zmJQh9UW0grQ/59TOiyFjcX/Xy3lYE5ofj1X4fuXiskfmuOxDJbA1a1A9NPRHxijfe2A2abX3cAuv41avDaSkWgrnTs3FQuxWUAjNqsT/Vqq9Hy0DtWFsX0qN8mKh8G0hZPEnQYnLqsrAfldYQ1oKLi7Yh4VW8gIkBJuhW+/raU+fMbHjeJzoiOxhJVLPxlK2UOPev7111TSqSFyHvGRUFF5a1dbTHZOdaW0/TCz/ZcB6csPudoyEOkIwemR8DGS0bwxTqVrhtFIrMnBHgyxHRzx6LGm/NdFf5sZhV7PJ783jBf8RuJJO02TGLH0wYUlyFebgq2Bl4wyVnp8Bgdng78VUtjqnz7FCoY0LnmBXpZbrfrtTXewktARv0plfm9VphwpKheeOMbNymgc1NmD2f2tXSLkqmFHO3pIbdcpjHIVPc3HUzH6lFcHIvckRfCyaykHHTsOOvABGDzeFH7A3eUGZD3v3FnJORePh0ZFPNCi5i9Bz9wsNk+DRjunu+M7Ss1r8IDuSECtaTZZLngiydY5DcwrPIXM/Znl92NAIs8jW/Vab0sHPM5F7n1nIzu9D5asXbUVvP1Gfo5RDtd/Fzavr36kCjOl/kUOsHZJ+97U92Zjt25LfFgya/r4v9m3R/Lo5Fcqx511/6pQkg26iARnWjoC12m5G6l++4X/j7lxMiGGvnCIIBFgTuzw79QK/CeVk6pqnYIiuzJKTHu1tSi3bOptHgoLa0f5TLMOwWQe03TXztBCMybYzMwzc3xZq5aILSIA6YWpIpn17y3ZSl0v09iXFKPt010ovRrpPSxrDcVYPsYW73GeXOhAQTIJJVrbDSypa8wK3qDHrj5NWu8RZrA+LwZokvJRkKXUXmoXx5qGnIGFjTDPFDUK9IkfTckah1XvYWIKSFGLaJm6X4KXD+x4nPOP2VQym78KXfmr5KOf5L40FaQr0LVESsyOSj8PEwFOowAyxwKNz0MFn1x0rY5DGOpv6wlsK00+r+JWjNbrTiCv4fBkyL3GkAo2UmY0AtcELs1AOjXR88N0McIoPEpDXqzH5rP2XGMjW+1gcYRsuA5xP7KOCdcmqJBCrT3S6AxG8SI19ZJ/2BOF8XIko1KYyNs2RtWJi+Y6dEeHYqtr+ZC6T5EHofRP4lY3F7SzbXo3tYguN8FHTflCrUQkUmSDhSybgKX46m02TE5DWKosb8L0CwYBYUuUZMb9mYW9apfOxN2giquMTzDqpqE/nWCKgxEs8aonOn0frR2zvttwiM4qJ9TjdzKS3AH5IfnRNp0XKSJs8jD9DZVSJMPIpA995fk+agJ5RFiUc7RWdAvkwcOqCjs16BHJdfQczJ5oiK+AoS6N+FVmhX7355ZKBIm+CqmZgCK8f54dYoW3/4X80U0qgjd0MtM1j7fbLboG0m4S1+yt+mKfqrYzxAJTnYidAqo1JW4A/CMyzTd/25qUoMhTx92glf/XTsuoCbIOUnrtCXGYTyc9xpWjlfeLt6MP8y7nx/zTa+510qcgoUlcExOV+F9Yf558jJD7ZMfZnkBo7V4fqfcQL1e+oBGbZqnkY9+/7j7uXrJWI+BvvR8FQb6nzXjOskG3qtwiBHUk516gYfPLdi+IZB9ve9/lWbJBDHv6jZRqfJagN9XlXlnGEAg1FpTOLaFMxYurkG8XAeOnNEyjFpAxYcNGi/5t3TfLTQRjmeU0zoBSstmdhaeLzNcRZ36r6mGA2Rk9UBue7ItTOC731iL04ZGjaoRFjFXrKHxUKM+DZoB5BxHLlJxaRBlrfFBcrg+LopUuiSb5a7utc99NFNWzURI83GbHGO9Tq8y883Yo0p8BtFjh42TZfhcaN3GxtByUfW6yegNLcr5XFF97vUbd0LB25uEeRVnG508iiZrweRYIiC879ElrXzTkc300hqc0M1TwB9VRuyCse23cLAMvvIRdZRTix03Pmdi56LNXvAG8VQ9eRR8/gJgzMyiN7KIRBeXqkqH3wa5Mud8TDTWeGkWYO6cGHdZj0QmcBKRI0U2wy8p3JKSZDMoPY6fQACFvkmpq/u5RAh9UYGC9QRaFQxv0LM/jOPlB/dwnao6JDB1028qP9/8NY+wjAEqYpUdzen1WmXDlU9pNFSghYYMunBt474niNG5gcmjNib04rb5m6PE+S0fknz9Vdh4e+48O3KP7wDWFsWf3WD8SOkcP7cw0ChO6mnwmPasJsQxeTcmRjJO/HjiqBl7jy/oRI+a1xVdagiKmdu/UBcBGUwW16rkIGGS8LANY0NF8Jrbdu5XtHP/O3bfKR0vMG6+aLDwAiRoaZ16mPMwRNPGqQJ8+DJEtBZhGuybGON4NZQ5/qa+UY39XNvFuR/Wqpn+AMtHeG3L5OnLLeV53tc7MXQgi1dXjz8Q9AW1MAGO8Z02TGLmPUDLV3uY9Pg3IO/3MRJ5KXNRegDnwwr1jTE8Br3+PbkvL92X7t+UJdD6z4YmdhMp1i3S3NcqfnW1YxErWz+Lcv+D8J6E0mbcc37rUqOgwps9gJIEvxUiq7IcyE8eEyU223EUgHDdvFZ9Fho6YNG5qJvaktBURlXHzta7onxV8OifDDlh8rgKBH8Z54NRw3QRFWblH+awL6L8Z1N29d0JS9WzMjlREPWbbDt9JzHdO5I+lT1wXiEfsGK2TsOTaUchnV+XNO8r8iPXP6NgfEymGuvDAQ5ZWzJtrlhgJi4PIW2HNrtzlGYKUN1YOCFX+a5AKZeCeMZfqATAThlPb1xZmyhK+60EvD+h/GVKkxg05KxIMC+k0G10KTa/IPGvQCVIZWnu8aF+LOPSPNHO36gZvDGOrq0b1xO/MzAP/Tl7KckJ9wWFJwmv9V50XFAxm9xIJV+saIHfGQlA+sz9vxa+Xmo7q/Z+XWDi2Ntd8XV6psZdTpHFb3nRxNOLAmetTFDh39R25p6XH0MOwzlAGGxwn1nCMnFzvXIQRrZmwtknNItYsh2RABqd4bVkyjqxVKQmJAHcK91TAlyAI/rr4am4oi5M8iqEVTpJYgRQhVW0Y26OegJxb1TEj8rR0Me2o3/+g5vKsbIy3rTyK+f/ZoBIXkPrYhOdZz+y1SonDECvpw/v/Muz/rgL8CqRjyjI2fmVaVd2Wc/IhczD1lcXWut8cAoA08D++EBS0n6x3Vux7hsSbm1CoRsWP2mJaT8mEmtRTtDvG/uZhlXo8RTxX3jIvXVk2J6orvmBbT3VXmJs/kEpOQnMAIRd+/oAtwIQVbLwK6uD+Molq+orcleoYnRW9qTMCtjQSy+p4ijGSZddt1Z57eBFA2XioyYbqLxKsL1pNubM7KUzxSCSNZC64e0204JWYJb7m7CcDHIDX/UUQq2OB0jna7+ENyClZzNs4Yvqy6rCLK9wQMVLCckQ0TbrFTTvHTX6muy2OJgS0tAP8QKxGr13eutWyeUpDtTBAI81PbQMy5ok5RQBS/zAs3WpCU0wMBE8xGf9wgn+FzVL/KFGy+GP4qBwkyEATFvbs6A0U4+1hQyf1SbuhoAorAO3ZP3xUkuWC/x02+j0jmWq4TVwZzT4TMrsUyD4VzPe/06Iru9UtrVSMnNb7V3NLAhPK16GkW8qGDD3yBH9mNYz2luuyotDjb3kJ9qvYlcQNLgd8VMVoA4QCmjRcWfcqEYHgc3QYN9zFefJnrjO9sYN+JKZLfBQ+PMR5PvrasqCJS6OW3jHBUy0LNP2+FKG/+zWnKTT+kUx79udSnuVJV2CPT6GQnRQSucHkWhx0GdukDyDc5YaU+3JYHwfa1d2Kut9BldN00j7ZmGIEhQ7Cmi72j049tw7wlRqaH78b1/S+2mokuuSM2pCiGY8catBrWVpxcO2dfPInC5umd0ALjGzxLeevQFsFMYP5806m9onZ7Y1oEUGmPma3+o7dMcVmjAUsci3hJYlyEKwYFreCyoap5vZSJy8/orMcUJTb5chXwWRU3xEL4rOEpNAkIj3AWH6qSsnzgSvuVQ8G7eWSX0FQsGVTxNRDXyoWOC7AbXWpxjbaxVmDe2pQP7EkRK+w3q1/TV/ut+vCKUN4/FpiycjppBd6PInnvbCdAbguLPRw1CWGShyZi8MmHytZ52bCx0HqJEIgxTwpSyvgSJu0vFUcP3mAAtFKHL0B6jbBDFzUa68TEtrCiYND5gyUJJJiBISeWB6Al7uszTBZrg0pr7T3M2vWzAEdd7F7YbMVW0OA3NAIc32YUwpRQjB+UwLIT2qCL98ypidpe9zz5OKgS6hZhBJyW86X4mmyO8Df42zNL3AU0x8sPzZf3EeEwA247VoquYwhUeoRQLjAIGrjT4YmpfajQ2yytlriqMQkxHn47/byqG81pRRHlK+JreT6hwde7ae8jn36Ii78RU8lHy7gBaJO4cx+N5VmSWMlF1Vmw3+2Kx/M7NoJmK+1Apf6PG3ZIdBGuyKgG+rb7ggt9D6k2r2vsWLjUUMMyWHQiqRax7bO4LFUzDE96f+QQ30KeMFNaVVkhWS9Xvf6fdPm7Utjfck/0mu/PjIClesuvWCW3ecYeFUi71B5Rhv8nC72POF3ALofm3toqnYzy+8SSVa7C7PGYiV2wGJqQoYHo0D4J9+waVDZNOoq1gMN97HYTSpmRxZHbpDq2I0rVsB4RqYWO6NnYtAh245PMzHonW0ktN1uuNsv4ZZSshi1dTNrNdcIsdyHKv+7WRXdXtljOGeFW2ZgacEK0nRdMJDbgSwLmU6FMF0EpO6+FGP4JukopG3wYEkM5xwwL1nBqvros1DcZ6VTrTCrqnu0TtBMVPQNGIVRdMT26cxVcmPsIgfffrIj+tDhSRwvx5pfmJwjCYJ0kG4vh+FTztuJi/W9MNm9Be93a63NW7tpV8h9oTIoTiVsr/2SEf8QR3C+wRS3K5bM3poIMiVG4sYRIRSi24oI9jvm7cMRQzfepkJDwIaOz8enk4qxfBfVWuBn4FHJUbW/7L8WJRtB0xr4TWuWXh/wHWNVaOPOOmJ4dg9qFzqnEGC+NUVAiAfdw+Ap3/a+H2g+IsBOnuUEQdjYKaE8JVfzEDsiEXNXsxgp3L7Z7tq8Xgz+5gA0b2B8Kwl9FVJzR21i06N/NjHunV918PLranWznDYnx8ixFMfeQn6/LT+qhanukKqqB3M8xLkHP2fWE1mChl0FOOBV+rdCgUDS0N7l9SUm1YJTNDa9gKspln80WXl/vUZ5Fu788Y9Dld+MhpzxeVEmHXeimtNHJhNMjMIbWhS224NdT+5wmfXJkwH+7Vf/pkd4mQBrij0hhRexcslsuMKZbJI9+oq7KhhV9n7BfSFa/DAwJy2+Z4GSAlcVLrnqPSgtU1wcyRfM+3mlAwWQp9N29tJoJWoicvDEkzIu6mCZ/5fQAqkCemn/8/78mb1bnk8Jz0NZPxmOBNE+J51O4miK3XolJsfrt8IUbrmhzxg6bBwMaGIXM1YoRumQn3IxCRHSt/FxCi3hqPq6pqsoH+orhXTDWViCvjSJp6A6knPcdRY/Q/aES5ttAuK71NZvEKKnuSxt3KAczFYNVCOfgcJYgiiJ25LOcp0hHsJKLfViK1arrJd2E2h9FOBZ4qFs4eMv1fojO1ovdbhbiYCpHQJ4ewft0OWACE7Kah0fU0qmqz2e2ML0jBLlGTBpnuTqrpPYZb7jtMy/Wge8aKPHGAheXp0S/0MxMaKml5LxZlCRadxUvDphAlE5tdYWMBYwvvCQpYwZNn2SgJSwyz1VdZSUGxbyrfPtUG6S2t0x4C2w3Dqx89Y8WvgmhoxIn3bF3EtSsf8YecxRsNkWzXRhazE3zH5C9QImcThkqCMIh3x6DXbV8MhA13VaFw08zRKIeCcvmZMcZubDX5oN/5BoNtNej3QgdXFV1SqmH+8KR3SbPry4Lyti4yvoiYbHJEc53xvz7TgXhK9f4HjakvcM5FL5DHC2RfXrwP4HXvwN9jbi9YW/OxDeOiQnt0/wtfqcuvbjjIPt1bthRxNeqsnipf0l5rmXN5AG/CH5dMRtXkh3L0wv/10JFKmyCdVdQWdO2hwd+Mv9N15CwrKjKzJAvR8sa1m2muM0BKqcx8Ti3pCsRntYCcBJ4mYKD3DRljyEtDCnUR6wfOUkAtVTHUscRSwHKjpy8dZPdi9svPeF4FRJ+DfwSAqo7ndt4MMyUC0l2MGotAiTOD80+7W/JnCHQwt0RfrEKePE8usR03zHSp+Rdh+4w3lMf7hgmoWPH1Kk4yPuue/Nqo1k/JP5rE05cCEIwOqFVXUcOTCiovjXyDq64dyR7LYERo1CNMbVmuUduTk6dnsiNaHr8P39o0MLz/sRqzxmLeXNpDYSnm+INzoWtJjOXZx4YJ9begjb5K5x3+V/kPtctNftTW8B+exjlrALUs177Qprl0cIlnmaFK3BvVYUadiehwc51oSrHJr9nG7Owyltn6AkOiBs5SwHRLB1ReFmgsOQFZVC4xbLQFNpM+kxMQKuM0t1waxHfAmQ5sJsQhuRJ3gEYAEjoGu475VqMsV65ye6wPKXQ6vIVbrvtmEIoj+Zemhh3hsjp9L0cm4H58nI0l6DdRbtOeWG4/j9Ic5fXQSg+AevN8REGOGjL7t8G0N3iAEEew88HllRbj0YOb5xbdK3Ed8MSmMu/4maWFj3GYzW7WDzjIAa3qTvlNZpZhpnWJjJLjtqy9cffaMiWZw1XDu9ZNlNLzs72AEkxnKF8hd7j6L8E6vKN3MajWJmGJrmOanJSToMTtwLx7PqJmXp4ZcY+74p1NGqlugfkoRw2dGgpwnM8IK28is8jp3Kij0x8xKT6o8z3+egITNfHqpvrFNMJrGxTnOxeaF0IZGRXO/jMxwLT0rOgbz119vbq5RdqKjgLfQ9DuiwR1t6lphsdqVUXYG+fFoI+Nx6zW7DE7A6XWIE+c39BPIV0gnfAdpjwWkZxDb79JbX9d/YkGU4mm3hI68tNFVBC+YOzTCyLUS8mM9YkF/pzRIgVHcmx0+L0W1Vjq1W4PpAu/wkDaszHleL/pG/ijLDzA21o7if1xkh7x4CRsFtwOuowmnfs21JK4rPJdi7/fVPGHv4dI2QCFgs92a2MWziT/dA05+P9a5VolMdYHgszVNOlEO9zo/bCzFusGKqj9MxgVSu3C4jvfsk88c2KlHv+Imo3kASDpMNILkWUU1kRTagdy957TzWRirWVNNqGhZeGajm+EPNQExztegm+3loDK3IuRfKcFpszLQhM5SxV4iGx7EBHxWzSdkBth2iq5CaEH4PKBhG5laY4umwUeagO62ysk7zJb5qw7IVHQwi74d+x0rPUndeb94QUutu9l4OEVlLWqHVGIDRa+WUGiOTbF7rqYE641gMkpOrPaA7WYSzfiGbmuIRk9R1V1u0v5pxjBcC95etKiT5FopEr6YRaBOk4b24/7TyP78MnLk1X3EJUexXHs0pSoxsAlLZ/oNwXtqRW+eFJPITvOaGmpDFJm8zubZCOcYcdjViuB1zGhZFZ0qDA3l3JvaqDdEWM/T9z5PiOwXiD7kMIkT2AvrnxB3bV92D/cDA+52tZ1rmP62POl7MId2WELTLO2pJ0LG/y66b1x9BEonO+i6na9Uvdh9axoMiHZEiy5FZ/ub7Y3QTzzGhwYMmdOgvV/hpnDa/0nKcFBrEE9Kgv4mcz7wnHha5VcXBQ9NBejDHuw+ljF5KSavmhyMAcX+KYrhwBbp55cKEQr0mMEkCHwQXbT8dhhLGVe9kCr3Px1nFFRfe/7mIdCYknuk2MHx6iSdl/F6Khd5gHLLOkvBjRVWd8IsTo+2VjxZ/N4AWXmY3XtAIcNxtWALHDfqZtucSTDqyL4y8vNJsbNxbHXxSBfDLcxNv9XzdPtTTuaFxd12tE+G4e99tH3kkuQM+OJ+rr4/mYj/kxF4r4tbWUgw/zHNB/cC0PPfIOorQSO44ddMS+jTNLtRBFwVXUu+2m+lWZRVYRYdwdYBGMnipDhjzG1TqX2Mo/hUUsAqg9OlkHLmaVekgJVOvFQDHKd0IQDCcIi+Cdr7EZHo2SjEJlMTf/VEoTDm8r35p+2YhO0gq/zy5cQ5Fw3552M8SlSa+3Rrr7RpG7KwgeMOTiFqOCtwsyv0KpLbGe/GplR2oogHm/DkbU/ArqTqFl0nY9ffSPpLssgdDkYctY5OapSJcWztkf9avhwa7DaCNRr+XyWeeAkrKXnedObr/P3iqjS6/pSsuBtlmJwW/ajmsxXH4KTl82FQZQyS+LuAsG7NV/9mmjDXIYEY026nTXBucxrFGQzrhiEO3gzRsLeeONyVqxqIVI3aWuarxt3WkRfMK8qiAsaq0VQBqtHnuaKJUw124Ty+CzaAt6WnCBDc439w23LaY7nllwrGd1x03ZubhhHUDwDCbAQtShzHu1QI4WxOw9U3H/LmEYwdc711sFBP/h+AS0iZBSQ+9Xw8G0ldFLq9U3L5ibz+5PNdTJ5R2GGaEuWr8G17N2IeEWbiu++rT473W9dQfqZxp3tdYJ6U/a0IFkROfNflijiJvE/hJFt+Ic6FjzLQPqiXx0XCWmCeZI44wGZg1ej1vucZaMhPjIOd1Jo3fx06NuQHN94yyhf9yOFHZ8Z8aDl9qEay2yAnxmsYbzvhsh5nl+XEW2pIkDZztTrBEX0pyz7yOosBE4P2bfApQrlc1cV/aMMV8s36Wbtu2JxR5Ws3rd6NtRTpp77lLf7FP59rkPr9asm3W4H5oCoqJRXhxelHPSFswPdZeC2gj1LqXEEdJU3K3W3xWg8auE78NCcQ9qPSh9042Vf4aFJjoMeI0GpZIg197vOGbycyXpHHSG6CqtzmWQpjCbs+JLbvirwe/oC9TkbV2R4Yhl1GQz3wuRpphvqfCmAPbR7bbOPhN0BhLqOFUr5bvOI/KarfvsueiP17HJ8hFli9bk/UyeQr/WzRLP9bcMxapSwoqinTn9QUv8XHlm0isyC2jG9WCnMEIgwkjTJaRnms2IUF0y0gd8E0gwLthBdmPwAsq0qPuMSd+QcgYzBe7POusgUysDzEHqsncbiUOa4eStJvXgIMj54uAGjw9Tmc6hIiPWrk/kp0TUvBUZrLHUme8CV/gjHSSPkNuDg1tGzDTeL3Biof7L614jrBQ7ayPjy5Ji/FhtyKT5P5A8GeNyJOpgAZ8IiCQITikfy3Dyv4XoS9nFvZyUImHf7AAYMJNVMR7uGHZQg11JLq5BJ6DWdsV/60/mrOVE3n52ngDi3ub0EHxZDandkeSIC8qkzKHLrckuRfWC4wrVw1/cwE4HGFrCqpWpZGyrfQNY6z70J+ldRpQKzEw5zB8eqWImfsexGt5AaqEamciszKyZyFke4w2RKKqMNvNXOvnRIjbcr2y2aNHDUU84RbJ/kKEAkwKzcwyXoX0+MxfNCFLK5FeqycDg9Me4f5m3qifDJnSquIK/dJPayKA+NwAytRhNjOj+7KNmSe68gX3nsbWmaNdDh6UK+MxTLNEPbQr+OKlI0J4V+QNM2k5i2DBTKPAEVL0jct/L70pHAF/V3Vtj2eBUcdtKNnZO/syPjLiBCztsLab5cNldcNiOS/qwyTMf3twQ2VGJcpsCNOv2mA+QlRG+DHD+kELgalEaj73DdTGHwf0xMrB8H321bxDagXqr6CRkyj/eFAvByJ/pzIluf65xIEJv8lIZC76PMikJAbZVGAulGu4rxqvoc3x398Lt1ReODaR9whA0JBSXtU558nhlWbuvjz5Uv9A/U6vVbbIBj5TvJh6GxR/vmavFVQHSstnFYuCcKUsEnpelf+X6Q7k0WUfS+nedlZ9PX6AlmRoeLP8rP0/eTMiZLEczsdtyGe0Ba/bCjRIBGZTEGHHidbdzNIGi4rbyYFg86tJQmz+pHP+p8VEJ/7nqbSo15C2I1WjCap/pHKWaqy42kJlnL/7FmOZXVhAE5niSdcnTltRaw9K/30XjuYPehkjYCYpmbVaHhlpONpkz48Es0z7RF3rgVzTiOLZSZ7eQWOOUn95tmJvl0d0IE9+I+SbVrpOlOYu93MaQjyXk2fI8e9Gr4bpDGTV7wil1ptFU8e1dPpfnO4Ac5fdOhd3FrN2vHzprt3jWWH69I05pvYhhnqv0vFAuO8u/7p6N62qkR+IEDuBwHg4kcuqEbTYYfI7KhXSGCgUe3uNsrL5UMyaY8ubAbNycz1YdUSqyGU+vnsDOBO5FElsWefdh4q7akWxt/rRfItVaSHB1gvmPHCsMdMc1wJh320mwLSUmHrlOLUybHUZh9XBjey7fWh9yYi2+C/JCe74QZ/7d9fAU5tS0eYZtptfb0dPsX2F2w6DrVsXPRn937qmJ5FQILtPvhov/mquS8ru2/VAfXOniza/gOWZCCwVgJG/dbjjH/6BSK/4TmtTcg0tnnIySmtACmgH1qVXF0B+n351V2FGsH3Z6Z7YPuwzw5mGwdPDLe1tHpIBZX3d8CVtLi+9HOMpytkFV0yzC+s/7fp+Jc9JFJ2ZZwHF6U+hF0HAey7CzdeTqQASxiAG7DGm/AS5oKShFfHReK4sWkE6l8/8N0TOjkS/Il9S5kSqWN0fVC6qWGYQEf4cCXt65EJ7vCf8TnijMwDTHCOUQoGsXx6Tb+qp0gXr5S/CCzgmopdqG/ud5OLHsvyMsQBr7mTdiwDrfbpPFUyK96qqJsHZOnK8WHTYibIEO9MygoaWK/29ePOE4Uq7sokgflRF/S+qeGBn/zPouO9ouYv50kJWIACmfoFuS5Sz0Y9M0m4JptktDp1KPI7SuMlXC8R5Mu9ws3Ytb+wxdpWCoDE0E0yiRCB2pY/RMoM3UoMpDC5YvO89/WGk6WD7/3gbCjl4YDxDpgy/zM6KLbqf0i0WPgAZG2VhaxqU0gN7FgDqrOD6DqrioQI5OD2BCwFXS9jv8+b7VvB8ejX3hP/g6IiL+raFw893uLMeNPbZdcQZGwnyzgIf5e+RduoEcrCK2z2HP3dPg1Bz4JYZsOWs+QYin+sgU53MpPWvN8wX25K5Idr5vmlUW/T812tK20obsawypnCLkAuwbkVdjiWwY89SBs26pNsxEMVQVfXoyGS4KPJY0oEN3FX49527148YHBHDV1vN6jBU0viodL6PxybFWHLL6AXCAs0o4ptDE+7q8UOBLu0/Zmnn4ovw5UCEv3q/mHoGYNbFsKSIo5njhN4/IiklYLqfMqr5sjzO4ewaUb65WsBex62T5s5K+HKBNJlahXESjsbGkmCn8EQoK3yt14eL69l90BDzY7as1lxnibi66c+/oWpxNaUtnC09kdCc+OoFtpKNB2T9WvCJ7PMruJfrUx1GvQsDotBUMWRK/A6qPJ+GP4tAOseC5bq4RUI79j6AyevNgqGEVc39rdZ+ikj1EhEpa+wrozinjWCeO5UaxjEcswUEDsvQQx67mX/5qCjkvIGPslZEbenffcifGcdexMSV6W8M5pgqi31w9Q5EkzFLD3cnjfkZ3jRU6unwH83IIREzfcU6dch22HkL+BnL/W+zA/oNQkjANrZmAV5l1JVGendunX2KXhq4feKPkoYo4uFnYHcUQegD9JN8zqXvSVX+XxSTiNA0lw799z0WQsa/i+Wleze+AQBP0HmWBwGJucijsRzXQHRMcSLsRWZ7QSBgWLBqmayEY9OiDTiQWS3duOr7lzXitOZevJWI1oKfTqEKbotfzNqM1BGcmpQpx2hjrNgyDqc22mygsLnL34QL1x94RSeU63+BX98/hsOgj1jS4bS/53IVR/viTsrqKPuR1lol0UBzMDvRuO3UKrOQ4fR5EYaq+3LMhzh1Km6Qo9G5bocQtDIyZOS8syuNx3bVf+s+1kz0ErH5qOX2fIiKrSjDRXzcXBc2I+L9AMw3XsBmeSkPPMbckNfTjvXvZL2/aGcisvQa8vGry0rKY9OliaAVzVyFkLFCihaoDVeR7SJs1pFaMUKDl9n4iNyl4PIxtK83VE9/j3g4hVibHpoACtEF1CGrGxnp2Zw0sn8dSu/5Qp9rPAfyasEPFRrOkF195KtznTuyruGqREmvw5A5udwiGenNOJrNDQ11oV+TVoBNn2JZ+e73WbgsD/7He1jJO1Sjrv9uvPQFRAHTdA2RRctzQXZJcR2XxoQm/gKcxjR/cjC3PLRquVO7w0KWCNm0jd5FNmC9MD1iKwAiRr2dMY96cMbNTC1ZyH5R/wsVPWuSOW5O9MZK5COOy7xfBDBNkTHAo1Z7wNviQxe688C+EfjQopOOKXT0Hb4qpB/CqKHEfKmanEl2WWr91RnMTUcKP4w3Pb8T+Hr6PTpYLG8454BGSoIMscLZY2Q/KhgwCr1ZptB8RMkdA4SNxEzQqftgYkyW/rgwY6M0xstwuE5xZ2BrhqKli1cFMd0LyUQKtdnFc8Gh42mlyROy48YkRCmwuQ9xxFT1/Oi6qvUaqlaMwm/EFm2OnnzeDjKJKEUhPjU8T8gx4JuXseBPnB7QIff1/HdlXNj8YkqZ5dH7+qLGiAjuIgiBgQQ9YXWkgKPQEvUwbndQEhoxppn9h3sRaBxo2+mx9VI974AwjvdY7qmZfiKjGWEcngNm/NDUVt0TECGrGNLsOjhqed3cnxqDpyxapzFHSnkwRUb6V+6Obd1I7FGP13nYJVjTZidZfplfxw+0Z1z+m62uYH5pObee5BLVhv1GiDBaqWKe0KbvsQYHYCgVcg0qkX7G61PcAFgzvyLA1Lms34QX0nCEx3OaqbkVecw9aGgI4btUJFmvYeT2Jp6JpHzr90Enn/y7ftcIWLIRHqy7hwFaXpkuNHrO6w58dWnfqGuU2Kr/1EUIJtsU2oVq8KHoCDV3oZHBlK3O4mk9jtIoZADTTxTZPn0mrcSK6CiYOHmiD7x/RqqiXaamo2mwqrIHgGZD72dkV5VCWi0tnaVcuZuT9ZAz/8mImNY/1WpVcIqCNiiNZGO9XuOu3wj8AQJWkE/jPUzW3Fauc7v8boGKH3yZZi28IrJiq6NCL9hduEMhU+GLr9lhDi60lFoyWS2CzeL3mcfNEZnajWpzLfTlGITADy9GHPVI5AGCAGaGWb7MTOSWUXbBuedM4M4JQUBA4BGYZrMt2wm3i75DWkmIgIG1nsTvoLvLlHS+FeP6AJOeo8bQfJMkLhjlOIzq0FW/ll2eB2vX7+sRuCW+JjSRANjPz+MAoQcDFlzdDLjfc0yAeuUqqqdUzc2fSUnsE7Qn5blGV1GtWpR2oq5Yj9pyslICyEcH/EcDSrRIgC2dOBcuMxA1PzJ49/fmb9n6c3F4PHSrBYaStu9b4gOp1OhQ9xAllcWB6dItigSwkpZhTmaey7bLqIU4KTCgiXxt4ymZclo3CINqvp1Vf9IqMGIfdcgrCQAuiw7af6+ghLz9bfL3hQSWNitRLzwkIV8jrR5RPKvWfKNd18QDo091N7LKsOPkx8Xqg4gFBaRJTklrtObaGMJFb3YIaQ8wuY0ozJSd0wCnbrcAt7EhhiFp2Y5xwNuUdM+KLxjFnBNCxqKppPuqp42aKD0lfAJu37TwbQRaf0edzDeNViEsC7UWx8q2Rn+UFEw1G+Z6WxH7E94glthKQiyvrDOqn5xnJBvfkn7jVu60JTCJVMXtP9w6tRFE57m8U4ZU/ITN4C9gF0wMgFWoICAzzG4HsjobkYZvYLn56gsvwHrfSUXKnahsqNWhNNiKfDnjd725ymnI+cnyaNoSNvQz8AflHAR6OMO+/otr+xXfWbL4OWtQKezOr55XlQsGrfopQwhrQJ2Wnx5gVeB86D7xFbNQyp9fRO/SLQY+se61qBbccTPhq+y8zEa00xqzj6As0Ow2IbHIhQzfsvZH6lptjWzz9Ztexm/R2Bdp9VZ75ruHoSOmnfVxmRVKgxTna5YPSP1H1OX520cJVErPoOOa3xqeBjfI/y/mu/93r+rn5Sn4E8Y0GIiY/AXIjkhR8vWKy5RrFl7tFzzIqKn1zUdViRIJ3RWBRXpFqEXta59V+yfbeCdh/W9jSyyYukV0EET9mLsRkrkkci6129PkVLL+KYbnztzFN1EDNKvTiNcsuP0mPW2EBWPU5OPgBEL7fU5Frh0xWt5UJvyzMCFfK60e/2YQx3cs0HDTk0NtSPbGsLnc1G7b5ufCeezGcpNB4catHHl367IBPD10T++xSORfEMLbT1Fyd/cfFCoQcsYGp4JXQAHV/FcI4btTWYPEJybL//IxrEcMtio3Trps1LlHiwdGSqmX5lKsd+vQY0A0tFz/d1Ymr+CIwlTiYUPgB+5S+toQJ3bOLOibx+/m6GCeJtAk8LRinNu6ww55d/PhQkbaF235C/pDcpHvHCwQe3rYCLDhNPZgbZK1KDZwu1lqKen1kpyxcglzg2kHYmaNbu+9XhvttgR8ESs4/ehlUpZoOQ7Wb/qNPaCjTfGidauzb4MKrmRWiJB2HIiUT2CqL/L89Nh1ASdQK23l2aI6zZbv50706JlfAQ+rWYsqyrfg2muYEb5MCuFAFi3Okovlm9h9VYl8rJjViI0a/SlSIdWUxrmPUqyyctuZEMEG89bTF818o9jM0CIpCMKirLREYReebGH2LYnz8jUJIhcWyVNxbbryD3Km4OcaZqyTLPB5XVTA/aVUT6IReSM0QHozqlesjRJvDwNdKxdFxVlNQSauPK9msQDSEwXhshJx6VvyPHBbOyhG9gOjWdnGPeXsg09QWNKbnvm+guwvJTAz5VJJAhxDrrQeBK/yoXi8U4mbP32MBYMXk7ROocFATYqzWL25jjxn0XDX74C2l97xnzTe4SCyYCkqD94dUN/8FFUJTM2/g48Cua5aIPAo9c8oEiodTJBs8jb/j6OmrvLk5z8xIKzlAgF6CxX5Fe/wUc055NNDyPsu9J665AW4kmrUiJtKOAMXiPxnTtuv/v4UwYjBvN2rdEWMZqbnvkzslM7iQR+O01VeZ5JNRkLXbHzOyrSo7LEq+t/1uZ+fIxV8t7aw7U0ZCpwYS8R7yVpY+RXFhtaruAQaeNIl8y3fFZpnNZj1lfS3bRt8MCzsZd/N5oSHqLiJQrZg5kwBN0Zd7+0dTqmiKsr4HKEjcMsfDjzYJrcPG1uL0fV8MOMZfZr3E65NU0qeB2N/I85ttEHLTCy2gM5qfKWS3nUuwtmMBMn77/G/27AquB0ljezozkrB9jC81eMg0lK4s36rdeJItCIvbNlTCLoPEQkshjaV0CjT25pZEW/FvSC1n/ISkzDG040Te8tOlGhFkMRbNjkNWa1uCYJjFf8kUCdi+SxTYI1Y6lbvDH6kdG44x8rG6I/+N+FiqalYBKUfcR6goenlgpq6rKrqiO4Ft6Q4GrCXyrRj2hibDaDS2RLOhPIjt90NmGLZZvoDr3FBw0iHYuaJfss4sKRI8GDw1ZzBg1TiJJup+qYgxc5669P27SQauna+1KYMDinQS0vSU8ECafEhYdTUqU7PIby452ZhrVSdWEC3Z80ig+eQC2yebJpGzP9U2wJoVlMATGCq65rpnmRwGX3pchZD1bsWuGrPJxj/vV49hhyJMIxRjKttQ5C5kp2MgJICYc83mcoHrsPigEJnuiCTckwFNfSMxkmzvrUsfDSKeLXaUytEOAnAGnDGO+XyzNzHJsaqb9s7OLMXFn/EXiJOPBTem/4+qItrUycgSuBNNTQ8UafReHzFz3Bqmf4JVO2ainegrQqXwE+84u1vmB4rUQ2XmfcqQyQxNI03U9QQP2W2FKE3E11yo79V25zlMPKHikTw2b6EOjaEMqW3PgLmFcEPkPmP+i3w7FDz9MSo/yLtjAzGLbzwKXcPP+E+rlOcVbWOe+eCr0tG+mx+USLHdE1abHzi6/vqHsB4N5a3ZxqCN3PcFNVhnUQ1HtaQ0J/tTFsV2gpC5mUCSElcjj2bnQT969hPkpdVsyGJ2a1oh+mjjpffY74R5yHo6O9w3cv/OJxedA1jN3FbC3hynQ77w62SQHrEKJCu2wYStVLewBqw+v0HjbU0q3fHtgQA0/ZixXA1SzAJY8yVyvVk86bsukTx3gJEEiyCldcLmAS6qZ1GhyCI53/Bj4zOjYhLuZ/q5Sl5ByN7v6kpM30wI1MBxwbA3XYQv3lbe4kbAm3SXHlhBfL3s63RmqJ76iOoACLGG9mAMuAN4QcdzGwi+4fDsqkbAOZ3gRNN4jTVD0jv0akgBqtkjAP8Zzlhe9r+6GrBWbt8eVEY1O1gl53iZ9hxxQlwjR4s9MwYN6YYNnJqszbeQ5teZEno0ZHYMflIyJsCP2L6TOOYhfnlJs5p5pJ1MMi/OxSYHWvy5IQfsoMb/+ww8czwej9P0OfTTMjgdWKaTOoihnQGOywjWnSVSf9d2Eu7pENiCojs6hjnXUi5WS/kgyeT9Fv7Fuju3/cVjh8OekuDFhneQ5A291rUqBDkyaoHhkWoQp5g4r7UhW8YjAepLnSRWkvZuaK4BzgO5awG0KVMkrimrIqfpSN5J0VDOMnJMNHP+oZKAyeglF5AZTIF17IQauwrebmrgb/Hzl4I5/l0Z8hB8jCdFV5SR45jj2t7NK9VsIUs7UHuFUlcB5jzyZcG4cJvtr0RQXptzsnBt9qn/nlCfie0Ykoah6SiOy4rN5LTw+bAcx9AfFDuWZmG/XLDbWraoli//19N2Gd58XPtcS2AbBdiLB998vGsrFmMtnEhIYVig7HqrYi/o+uZK0GjN3nbaeMu4UuU9fUDnwKbYGIvJZqlvT2I6o5hXPuB8Y/M12MvL4dhAEVERmTjBHB95M21xFImrviwxonY2BS1YRN4Zip9HR9DaFX4qoJrqGShHViyJ2NnKWL5JFhdJa7ShxTxjoFjRa6s1OziltJhpKPdGaIxgbLI0RzT0tcJEGhZct4oSs04mlW0FMi1vjvMokk/8yOfyZZAgR0BRRKlf+bRON+vEeqhwgrs2gl1QLQxdvCQ+ur6gI1lhD/t+0OQzQM/R3rLnoiRStVaRtk6OduuCTnJxVDbjGigvDSI0uNFKpu09wS/DUPMzMz54/F2hZ4WVrqyxG3UIQBV9C/u8jyBsr3QMG9rT2KPDDuh9kiTkHfkGF7eqghLBeWKDBAD7afDh7hVTRoH1FhxObunDoTsX0BZvq59U7ahubPWKJhUNaclbONv1rEOV7facrEfTleJ5hoIVm7HrO7ICGlcFi9kb4wyUm/3mW09uNWWYEhZd/mWIu491AGdMYmZWO6lNCgfER1v5rYSzRRWQ/dcuo/67Wa1o1/OcVNgTl96h8LtUxIYOKsufdlreI/P0Vb0iQGjw1TJcB8/Qt+sTmsyujiT1ngve7AwRcW+jLo4V4GOY/A3G9ZF93tWWXtTErGZvO5NUx9S4VlaZVzdihTvESwJk2u5xWYVyZZB8tvXTyxxnSaOnL5sDkEG3ms/ZEawcY9DjdZVNR3QyKR22sIj3tfzAwgdx+DF6swHfAg2vgIznNuuHx3sg/uDWUCtNoskG+Foj7Ua0LJMfhruFK3fvlLI+y8dlRXXrhtumiBHCHu7KTmiHbUJlQW8Mq3nUpiqOBBwc3gIslos+oQeMgxpzRbPGW7qgn06fUqeT2QzK34K/ZgJ7iG+5qg60+0R/qzR8wCZj3CltgF27aZHohH2esbw/EC6ikEBfqpsAY5bjtiaqY9iscxMDJUoOQga0QKvHEdBu7yZ+2hEemIi6xYZvG1uJzh5BCF+Rzg7lhlV5oivQKKabPO8uxaDyBKmGVly7+GEF041XH4v/BP27JDlg26z/4WqWBW0a/sOWahGPtK/1TDWxkVMvZuHHVit34OlCgb81kQBNPZZh4MF9QTkHTW1S0onn2kIp5JfVw3viaJ0nNbpXyQqkKK/RG9jQD8gsUBWI5jTExetc2Mm1/seE3tgTtCIO0zMJlFSaQc1kJQhc0egjjMqHZbg/UxNDsfuZObAc0icnEpuP76NbO8bmZW7KPoWGyvyv5WLpll4lOQZMsRMEPuWYBt2iP6Hou/zSdrwuKLkQa7nPEjrH32mDCc7OUyKmlvH7UvxBydfezDEzHy/sKW8/SiOud7Nq6R8yC33m1IKwmO3JxABhcS2kZ5UJDveVj+A0LysnNpzbtMTzQe5DMWvO5WxZrmswxLngHCXyOUkh+YJMNx6fVsf6MJOXzlI6PYsNgVtNO1L5HRztKAtVlBGEPyDvsCnMAGSkt6IjNt/fGABfBi06qo9BArcr3a5Kl2kUsi91rTt3Dv1/Ab9ow1bbTy3IPA3vBJjWppnulhAve9Gp41YKQpf0NjAl8pe7sdOjDzv+iD1mQ9lYX/3DTJXllEe3mHB0nlcv52OiDyXu9H2cM/FQOtEv8pmizQWEIXDNjT9ktx0daONP3nv/xkhaaVDPa4HsNhUUsumJ076oBzeLJ6fOdBzA+iFGNnD5Oj0ysVZNHtam9KLrvVzPAxR6F6XaGdbSmfL3sR++AnQD8RUQgpAxtWKvXMqCbATvkINwXVMQL4OVp45ut3KLCePzADIzRWluk6L2Nj5cRnyA74ojIjt5I6e0xINVpzKlVhlsrdPFXeH9cr3Q811IxXv1xZRf0o72YYKRVw95fE4zuNGKd8JYWWAMvszuIlspVO6P0Hy2Xepj/x/u7o306gjm9ghWZZFIpAev+GxdiuMRtnK0vyY8rB8Ogu+a3w8QYiRPsWvkQF533tXTaT4S+vKDLbuzLUXFjiwHDtXORQo/7QY9Lp1PLd5FJaYom0R/S37GG+spKMZiLpu4bymQdbYGxt9CPq2S6HyNDZhLHprZ3SwdgUl5uHLMcaJpOQ4Ka3WFXbiUwPVY8gtvd1K5UzD6AMtreEwOtVaULmvE9L10f06l9gWprSAESnQUmR8P8BEa2VHnl2bkgOmibl8znRajJSzqFhSrzcBBk3czgsezNgunhYRZHhuGkPupuftSX2thsDwm8IjNA0Vfg53O0TFzL8j7rwkLi4xtty47jxZkp0Q/BHKxxy51DbkOmvD7iDA57XCTZgGcaxyUIxzIhyoVqwuW3AqO/ivH2cD2e8MGQ5OSTlftJ1LsZ+yT8RHCZXvj4ZK3hS2Ygr478lNZ21T7zU9JMUgFAvracEz3vRQlYigI0FwLsw1tdujfLJtmw1qJEmrqjJKxWFwQ6Ue8d92sUdWegXnSA+M8KkbGCWpmnTEIHPJKK+tdbVqLKcLSqWX+TmOKJ69NFZbfRDzqAsxnQbIMGcQXQTcpFlXKId13vF3e8+xfkRQneP1Kynhyk8c5I21i9GilXyaaLHuc7hWAT2tLJrymijQAgpVL5DrOOdCl2ZUhbeMxUcY6z8VZb/LIGI0LUZrZzlZFonpIXUdWt2+qQ1bg9P4GQMEg+oYI7dP7ZDTPgOqnZOsf8lmBdYU2siyhPuJyYaK8tfq7MljEGdmSiWj0/KwySkMWaG6BgReGeP+ZZD2tGDoGO3ZHfETJSMuUSN3D4FWr61wIR2Z3j9qek349KxQ4FvvPsuWr3B2wrsd5miseTeR613K3xrl67Smtpc3bBawVaMliZtv0Cg1JQ+L/19v4l4KLdVcJjgkJBQIv8UOb8qUAoV602BBlRsOuWv1DH7ULdiSq5y/mDRfiafHQ/rbVazBmtLJ5Kuans7R7HSS4S7cTMwvSnHeOUCDfzFqF7C2wLeGQTcgMCXXe6vKEh57EnUW2nfGA/DR3NTflMEW0hyGe+8BGMd62uR4GnfcTvg5HLXy4CBn2jD39BdwWJqK8XjbST5F6U2qPFFzVGoF0IPI3seJdtW1xUvHDR/CwfdcWxPPuNgpoeR9vmD9MM5LrKhhExa3SkvgtA1TmPF7ekQT/LdmLGyM70LwAdgVUD/aa2mC5izklCrsRb2Ze9wPDNocIT3mdTdFxGIGgiawJPgT7CZuvwVFNoZ79p8wTnaGqteHU4P9Mmk/Y2TxVueoVul+tZuhjOrsxQV7/UDKNQ6sL7ca1f5KfPp91ll9JeffMK6928f6DmwJSzDYp+yOzQ3jNpjRF10Gf+7+gWgvk1uM1RQ1GQlS6HjA+uCF5Y1oIbuxTu/A4rTc86QaE2xT/FBn0197LB9VETPii+/Y3Cw0qn8FoofBo4pqElA3vawu/fg7P7+QRC2sRneVsMzt6httU/NBnYOuqiOOrdsAt5AUk7EZoIQNgOFdJEOL4KQ2+29pnWhbMRLb8kXj8Gsqr4LQA0gumOB7XtrZRaBv2WfVdk3SaY+j6zC/DFjNXw2G/kZFd0aPeK5NLpyiEDyeX/72KS7mlzhbRpMWsge5viU4PAzB2DL80n8yDdpVFXSsWRrsItfoMFN21sY6hk29HMjRYyGaAnAkzqDggdlMxK9kptFRtCsm893FyZ7pPHwk4XofsurDf9QCcr54q7xAKtCxa0JOIBD5S2VhaQKpHgihw9vTU6JWS/gmFzgSkrXsVvStRYOu/CrIiKHM9AIXkjOYlM/NJru2jqBYZx9ilSe8J1FWuin82v/ndx44ndsI5BxS4FfYbV5qjb8dc5FjnK4HdP0pn9znCzpoGEs7HrzaY5fx+abcMqbrdYAR9eVQHkKdt/KWOdejvOGKBvPr0h0zOQPcG0yGvGrko1Q5AX0I8ZtP304HtK834Ii17wKaCuZjDPpPCQFZibnO+wEDSn8KbH9MFdcmg9nSaVyQsGJOxCAhM6Nzfq50tkIEvJjrnwfB3N+39aYEG6cT/oX7V8X4tVZERxuR8kq2m6HrSbMWhEitS+N7h8imFWYNcg7bLZgCaTg+Ho22wh128zjioxhYuien4SdEboLjfcmZldRp+93ITanv8rba0MspN7eLg1MKi65vOB1nnHmlJZt4VRWXa3zqtb0Em4OH3S801uAGv5668Qke6TfS4msQ9w3eatDL5p89owegBFPFDQWv5DmbnJ0KYaQyht4n0nhSF7ptAKifpWI39IdvYl3bIFrDukXhyU5/0P8JO6iKlzEkH7uYR5JyMgpLq3QhZww/ggvfxLaSDBf359ra1jpq9gyhNhqKcmGH7RY0lIEOq9RfcvYb0+MrnK6zxPAfQtTW0o5UWeqi1GJ3dx5StSqjhDCNc9nef1Mnz9sOZVn7oxcpTbud4IDwm/499qzcYkwYBzUHsleS4Zdf5o0lQJ8nK4dL/cr9CsRIuAaPCAKlmCpnB9vP5bRmoas+/SA9ScPB6GpImxJEkd1dgM4i3O34JpNvRyNjsEKsD85pJKostTI3eVjEN9G+7QW43cQwkhfkV8oxi2mMFo3VkYeZJHIijg6jxgEBh5rkTcyymKyzOojvV8nV2a5uSA83DmZVfCkIJPuLN2ky2qAhhPH2PAEbdlFSX6KKDG8pJSK9XqjoiBH1BNI73xZ/MGVij7NtN3WQLJwLrIRVZ8DwGDy7CLiffYT1Y81l4aOxhkcIF/PEnGhvOPP1osvEkNaRm0RBQbG7HZkDsEG9ZvOXogsmaNkIVHbrZ1A/pnRNWxQ3F9tNf5P58Zx2x4LdLvRg0S9xun/jey3AbKnzCYdERVjZ39+KZgmg7gKXZV0OkdkWeL4IgVoxqYB+Y4J1Dlq5XXo5rPAL3n9hPNYgj+OYaAtQZdpSUuAu54B+UDxiTat5QZquO0W3eS0FMJ9D968WRCQfF+BZNezg2vniOzBCNuvZT+fZIXIeNlRwGpLlKTYN2FwcbUCk+9ccuirMCxunZZU9VKAij7j3BFFOUkiMHPCeHN10by16Wa/9sOMF7Qeu2e6GXj/5/JYYL04RHP9SHKU8FpWkJX23Ft7W7xAIqcjlvXNNpYPxmlABAmkWZLBQN1M5+41YrPNNwbtinYwaVg1Y3g+Ll6SXFFzcNyM77403495+BOttCmd3DWTswHMTf/qNHFmMCGMkXtA23c8DS87PHHH0gu1ia+s3PlH6M5BjIE9molcQe9FeCbQkTJofVYEKiLPd55Jr43niAUZnxKi9C+GYSyX+XPjJqWeec/Kb6EmYU9uf+5X4cmH5W/CEBL0iDCu2zF1X8WrzOIkLJAKVB5lUzfnlrpAXz4YtIecuDkHpEuzwHHcxUGu57doGlL4cufJQ95I27hgEknqafrhR8RnXCpnSu0XvaA0cWY2QgbwO4Xn10efFuwQtPeDElV0wDppzztgkbmX4/WDymU7n1FLQAeLDJqLSTJmqv6boAnVoNrKeC5rlbK5hQPxnmETDvq+7Op4vbJ14Q/aFnOLts/ezrDM5Max5koNMlcb+8KSWIn04PeHtf81Gjpopv18H1OEoVyZA2sGToYGRNnXBB5yoAV6+74moFEbzsqMf3YX8kPg4+xxXbJVN0KFni1NKSVNv65tDxFCD6ZCNXs//oQ5jF4VS3ZMSWHoePjz3S69QV4yzrzLt4ZWE3r1suiKyhMv9tWXM5thWnyW/v4oABynhqh34joLdDlQXbcEVJSVwQ1kCcY+elXW9kUSa7DIaszXYyK53POhVdAkcWY5nyEYEK4b4ElgovD9OY+JQkDNxB7z495utRCFf267EkFEfzPIVYPPCbTqQCoxUZ2d0tcyyV4OpcBh0/toU32hdDSHj0Cugh0sUOPWC0EFu5bpKvdHEr4hRjZwNW8H/m4T4peXVQfqUQ7Ox/SfaAYsc5mRAvFlHiIgjlBQX+hli1lQlGoT2W7CIqOTRbLI/6/THaq0dMIK4JE9eplre4h2+yJUAEJpXxcQKnPC85QN8MPugqjGOa8+mtUOhICOfIetc0RlZt3zZLme79SNUGIuvPPe66rnrIYWs0V90tb96WyUCMZhHlHAqgXpS2ZFZpi6lwwq8wzK2s/qlTX0UnHWiql4XLsS7Tcu6HgEPh6ARmEmq1hOWwea1Os05y76V75uuttqkwVosxXBE4i0KJD2X6ziN3UPv439lvuoRZp7y+RmeqyhAjCjm6Kq8t+w670cLmQiRli9DC9icHuaIs7AhlqtMgrsFxFqboq8rWJzuYjh1GEkSx8YmVLrok+yOq6npz7e3lw7f7F5ukuIvKXClQsV0yH4d9LJ/ajGS1vtYBGXD6OjgyQa0Z41x/erMj3kdq9yxX5AYkqwbrgCkBBOhsUyRnYCobTOtvFZT9BZUTx7D0Mq0JQ7kpPKyXuEqEJa+1FWxY/5yvtsBu0fG+KAigzCT+fgZPcE+xs/VvY1oEsTKIGI+5JxLOOeiIuZVlFKJodm4RLb3znp+OEeikkXgovuPC9i/YghPpeWCQ9Ujak0kpXsOe9aoXwkgPKo4lzIBwW/ASS83XunyqftcaZctofcu9TQzsvPRfiDpG22jBuSlNZYtnXqSVTKLwl2JY84wE0RExSQ+1btc627c06Jnu2mBNBGdK/XLxGe5C6trmTac+2f/UPuX6t40g8PrQd+0PH/8DkzEjY9D495clUcTfXr80Fc3jAnXiKEMX8G6r8WPRK5BSH68RT31lLHWmNBOoFb1AVVxoQzfNso7SnI+ukAoSNpgOArKpXOmCR5QAdoKhEjFtPWqtR1ppcQs+c+kQFSws85FVnxcFW0Yk0WSXszqD/45qFeEILFcwGw6oy0S/av87z0TudQjsaIMyH/nxuqFyeNILPh3FCchoBxif0ONmZ46v4RkElOjx28NB6a+eOrbkeMw01OVdQ5csZofiIkHPNzoaw/5TU3m4OKGvQmpRWyTW7I9Q5a/b37jlyTzyvBOx760Zd02omvMRUeiIBfCp2n1BFCwd3zk+OhSpQ6thK/XLAWeKTNSmDSBf3TsZrTKmhQw9BgRzoa+jaSCSe1Wowx2yswLk5xA3UmubJytLdA/f/kJDRU/FRrwPHV/Cg1PwKM8q19bhkiHA566xnFq10h1I0bUGL8EgXvSGe0MnHuh/7wpqo5effWUoKaSemM3B6HHMLeUjHydExh3mIkPT1Yx91hwuGF5KshcNUHF7Jx9/seHICf4xUlzwshDsgPyo4Y42sgofTnEQg6w43QIeqCUaTlr3aLuQy9wcMC1dR5Ti/RDeBg/keQKBfMnSILphSST4/8/2clmLG681fpvnQaJkngQMpgEkn3ebfha/a3/ddEUWm8COsylqDCAye2mOc/myR+LzEsbzHPGWZkbkgPoq+oVshWusyczCr6Oc0ugtzr7BMpbTzywQ5qGfV8IQ+ifQrAvqXXpfvUl9WgZHO00YeBWFvd5rYrYZUSlNDn6wIG7qEUIEBWucUC8ABA2qYOoVCAAdZZVdjJu1ZhgRASGGqcgdtbZkKo5vbxAoPu+u4lJswNvq9/SsTkyioUy+9OpwxUdEkNWcPEMoWBF+U26QPMb15iBni5EIll6mjQaOMDCYS2bjlvKA63lWicnmCeHK9WPe6C2YvQlAefhM1o2LgJOyMQEbOehD/O4ou+CTiqfk3wYQtug3BQWVkfy3RW9mojz4P7hpIDcsNyFbmectp8e306wJWBeTgNGW3pnDXbB/wVZpR/EKX2hq1Gak3Q0mx8XHNw6JdjuO4NIXyNFkEiGeW2fH69O9Vu3nc2swLn62ETAQBCJMW/fGB9D+6jFPcvMN0Ms3SQhtgoiCHMBZhmxCtfhB+C7RazgIGkA/6pOSz5+DwMyiyig/nWV60gNZ5fpvld77ReyaJnK2rj+nMj1KNswPcOzt/n02GkA8DKdJOZvjNVN27iJs5nI2aaYPP/U2XM1tKRRRGR5W0RKFo1AItZXUZ5qN+8eyn+CE+xDqoaekMcDf1ZqToZ2sAiyWpGoUU3uFRZ+pLmSYP+0gm0KM3N+fIWf9undIa2zj1R2ujyTtdqzL/8IzoSefQ9gmwax6go9e/0yDEFTj9yjw+O9khhpqaU10qeDe5W5+wxARcj6ezSfAy+h/dLfeoBy4m2/dRO83tbMk8aY6OT9nqqPSgY7BXSnJa4Fs0lyErzsHwcDkk6gcNxVkl9H6+64t5/eX4k90i4rSzoGcN0QnTOyQphuAiPJE2Qx6a3ekhJ7Md1RqruDJ2kV0jHmMrCoarzuyFGDcqbzVViZgGvp91fku+jSKvP+BTRlNM4IfcfMBKJzlqqYGN3P+n2eCK1dRfvnjHdk+WYve8CJD+KPlToeKbRq5NIwLD7kv7B9PtDlAEkajJLC3ZC1BWL/OR7Aidv4MPaUWmyUsYL8VI5Y0O2RRFAP5gOCk1CIBZnCiiMMsJrH+QZpsUiKL2Woy18PnvzCcS/iVBHqPh+7Ako39pS/QPM6M5vmWfYV2pzPFcZmlZDinvft5OD6dWi9wIsUCmLSCyw5e97ch03zjHdyCffL2783S99H6DRejypM+fgeq3Dgjg3d2sE1cmsWXkz15W6P/QzHAfl6JTpt8a1sxjMCDE1+JSAuMzK1moELfCSet6yqGfYmSGEcqE6z50Z10aw+ePqqvfwygG3PcTjOzxIsieWDkb3QQCaILNj/+f07MpZNwieKX+6fOM/8cE6eBFO7aTORnCUYeSm5Mdz3J40Q3wOah8A5BVMt7zbevidsB5JrnKnlbkSXkzOfQ4ybTm7lhaRMJOSdJmjOd+AX4VizxGD3BQuVpyVlvFtBzEjewDjEKHep9CtAYo1uJf6vtrdwh8BFmwfp1xz5wNGG/n6PHzTjhuI8QyJrHnL5g4TltlX6o/Bw5yuIVQv14THs90uBHTRrejtpGKLhV/qxxGDH9UPEIPCqAVNw1TzMTBBe3sAQMA4grNjtKC50GUycCiOqy4yRelLgi9HnJl8sk6dN91Z9ozB2vdF5i7ghgfBQ44dHa4Xvv9lXmddj0KcQf4imEF5u3L6atEjAZovSnFCB7wguhyXBtFWZEJaTgxgOt3Lqjd4E/H3Ei6Y/p4qR2xcQWjuaTT7vagVCq4kjTW40Vpi4VTtSlp6deahnYbwlVY39BIBYRgk8Y53A5xGIqKQDNvw954BD0UWkp95Qj6GuXxEfDNZbetkXETDBwUqh1QgOBoIjdUXt9vaQs/g4f3aWyBg9A45obijXUy8iKWx7iJoIygzhgCj3xHIaxkpVd3kLoaL7yLQARllDdM95pfyZnvT21+xwMmZtblIDQlEPRzZGLOnt0BNlXVKaPjz9wa8twC+webypQbkqVIkGQ6k9s9UPRQp9IFQ2NnzxiHXHs/n5SoIwZpHtRzNAowe4x86adGS4/UP0yQ+gygn/2SD6zB2bDQHlJ2b4PW48SW1WjWL8km7rFYz8qQYoyRyz6Cz0X2P0s1pS/apojKuCL8dp1z7SWwQhKIqJOSAK3Fe6Yea8CbsRMQBeJvhcYNm46n8vNCuCm/iu6XCei+udrIvAwVeI18GVK0TrYPAyReQJAeNKl15YZ/NzKjzAt084u4KT6I4GknBAHe++s9I4pDj1Ri3yZIia2wPtJ0hWH01axIfCFyNLdeI2vUmWhBMqJ1onY35lch3wmks2rvXYh/GBQy0bxvy68JhiqXV//XzZ7b4aVkT+NiFBeljiYvtIXPzrta91L2bphFbjDZ0L/xrU76qp+265d0K3VINGWhPNiVIn213XzZFL2ZSNFi9zDRIQGqXGifbX2fL2FkSDbbf9rCD6KCGf46wctUCY8yCrd7rUKoobnfNcBFh/WZ1uwfrH8l33SQGgC5n79bPuzRre1y+SHhRMRxvua+3ya61okvFE4pkr2cM2sXRgldNo3lMWjVilVkTrxpiSasTT0kiyJMKvdWpXLz3vKLrUkTVQ7965hnC9LllU6IC5UlMOSBPjs1J1W5p5GCbpn63FXPxzVOfQapikl8juanVOkp5RXTQMcir+5+hTQKCxh2Z1xd3rAluXr1OKlRQZlDYt4ZExTONJIAaiaEitLHThhUuiXAqOsDLPSZ2mT6b6YzhqAa9bV8j0KsXXkDttvs7FDc/u/zgkDcRSiC4NZCbpoIXIfu2ATGhTbppj6JXRZ4NpJi+aV5MCdgZBEZSCikfANrOP4F5WSh3ANqT+lZmBg2FqmuTIgp31ho8D7kS1HGRGkrsJ70DSHolA8vruYeaBIYEVG4kwyIGXKiNtWhhRWxPzDTxrs1xhplhj3JJDeNeMJIsvPAYeW4VRyYXkwEMFAz3kac3OKNM1soZvfW9lRsqcG8UtKtGfnn9F91VGHmwpbGevY3kBa9ln8lvFlOeggj0DwNOOUyUbFOAdC/nURQjQhCVwhGpPR1sInz/Xv3Pi1dy0OwxM85riGpbbUhbjWcUSPxYTpjXsLypCPbVrSgt/ZembV936h2UisVjfCmDXkRoZgYTRlquy9rtOX3Q4S6ewsr1VKhroI0DfAYQNp2I3sZa1jgL/PEf19QKZaFKGpLncVOZFm3zJZyDlDrxWsgy5BZ3+gajYiwJr5VmStQFBbeZ1wXZPsQS/lSqRvPKRFnLCfVqQBP7fjLfxDTbfZc0nema51kOQB9tvuR5mP2lIqphNNZbwIueCji8LrawGoiTF3rVgN4wDs0EH8gRmPgqsWc1lZGimqG6dHyXXTwRueLrC4PWKhVujIbCtE03MB9c/RLq3eIN0EG7OUDUAqCUbvsyGCiOwNQ6uHEppY0YvGFa3lGj0d0SYmlikLh/gmyIop/3vU50cJ2t0BQB5C/4FC5Q5TIHjP4+HY0gJT1N2mz6L8q5D7/S6GQOVxmf8ac3bA5OeWUKDO8yj03ZHLXPgx2B2/TH8b6ZX2exaLi9YoMW9YPeo/rF2l+X3ahP8wR1HjSV3vfquADM+9OJsr0CCBH6AkShauTCTL75Gi4f6wvTUj1cyOShKiR6pW1eitbGwTYHY6mL9vWNo+WTVFplosPjTttVPAKVWKwpMSxIlFHuoiiMOVj7g9L1Qa2L20T2dsnvyp5fLtm9RDPOR67YZs3srxjfy+cUC8JkddTei5uMmE1/i8Q7NqFMCRUTalBipu1ItCzBbpS/kaI7lXf10vQY+OR5HSMHFwJBiNfyl0nT1o0FaUBGJm7LTRuDSWCPOaNJN1/5RCqx1ueKgt9cdMyKLMk/XPcDVIPDNay8/AhuP2R5hBhDBehK+A+7cIroLnPDh15rXnj6682hImFqvfXa4nA+k54C3CBYriGDOi8uZwT3et01AbrbuByEIXFhkuMHVSHVkScdvvDLIY3Xp7NhCSEEo9RJdyKQ2gLzKxw77suRcUgk2pfy+1WwLXQVd23D8Jf9IEr9tgdKsGFUJOL641UnjsFstpfW8iTXtXhQPexQz3qX/fBguHS7t/W/RC5UTCcVkKUkjzKSRU+R1gF5B5rvoSVL/xJTf9R/eDtcV9jT1Gr8ZwkvZhlqMtKBAhEjmamvrAyCMEgyANopvWfBzLvf98Obi1nOL3FBJgn8Xcn8q4qCkyFftRDq/7ecVDZ376FMAhe7Pgg2YRFO+kU2rbcBR41mDRoCbaYQQESioeQS2jTeBA8oWyZAGgxNztYkUGcn3v/RdJuL84076f+FC46aTyVLs0HxHURRzwFOL6R4WoeYHhurllgMCK/EBl6NH1l4s7kuntGwgvW+qIs09h1vxPkjJC+G/Sg+Jw9D3Z1zu3zcHlv7XOlKgdII4C0IrUMgSoQ8SkS0POYu4WxI86y6HIyid8t9cfTQsh3YAfcGe18z2fEC0+XqVDpG5FsXesNSs1izl6b6B65P1qSaYztuVWXRADsh8UTeCerS7LxZFDvh7qqis3R0xHyMdMg5Dan/9iKPtBgFNci+YTczXsnQwDtoMtHWp62WzHuxCw7xTyet0tv5/KupHNp7MWRoPmv2CiUrXdIsaozOr9QcggcyGTGnKHiiUQiJ2djB/4Q/AhZtOOoEu4CKefzcNIMJ5STt7tXekEIFZLFAbPQcHgVCO9bWlJnHpANlnAtSBAYM9CDGXC9T49zSM5LAj0pWUYAitrL6pvn2m/omnnRGZfjU0zUBcamiJpi29g82RAVDJL3CipvHHnE4CQOWWM2JZsoIxfDdWaj0WaCc6TkZ9CQT1ZFhhgF3nECz2/wW/z6PoWhJdLBXtXTogWJuXPNV25uUmvxI833PVORoqglE9akfgggMMA4OS1VhLPRu4mGYJ0kMK9Qv3DmFa0itXMsrgFI/GY51GI+12oFdmaTxVCS0zDM6ixsInfaltIvK9Ywl9PfqlUySe27niDNLfroJjiiO+f1qtM3ENFCTfvZ2bYb2ZdRdaTCBwBm5w0dkmJRFn07F30CvddxgjkU4jQfE5pVDzIKlrwtb//1xF4up3PgyMNl2ab3Mob174hRVD5jBmn1mH8k64OcAE9hu6QtbhDMoSOtdZL9E9qiYOZT2TKV2yW44utXBY4l8XUSVBlcSjZdFDMj2u/yDXq+/aCFfwFtI+/3Mis5tqCL7JJ83UvSVs3iumD0B+duHpSGkPvL/SLf+SjtAJduROa5XBAXbihNcOGV7fXU6Ci8Nx1zPTFqyrrULI4SH3VgXlzdKnQv0DUidc78p+litmb5Qp52cF4qgutVbDc29/3EzKKZ5VnOQnooiNqeVnixVB7rxyShEgwsERHTKrDd2VRKBlLXBZ83JVMmEBOSve/7XYUhBSRQqrzHg2vnJz5uUMIPhXLXbQmd/wkKntW0MySJvQBiU9F89mowVZvLPD7Zn/LM3kng7H6IlDxQko5I6f941quClbun9Xzs/o7ILYXCnDE2HrTaRTVlDsTDr8of5wLBdmI85veoblDQr6H5H4J1oFF93DmyYmmzodjys6PObmlClJDXso2a4zW8DE6G5RWRIERxaS6V82PaRguaUs41d/6KgnfX+7Jd0TPpMli5q+chVQ9eRwQAWEOxVjb8jVLO9nOHsG2ZZF2z2apFu88PLflEM9D2UDojoyyTIKKkJ0lOaxG/TQ/3v679bY2Smo/Zvt+X/etUdgZA50sgX2oGzrUqdFP4iXUE3cJ8E6mEUMGMSmcdBy82KUbq7UixINEWsRZ4Bj8g+t3IaDizM+Ttf2VCjsJ8mVAjK1kij50p7Ls/wP1fXN2znrM2nkbYjE1WmvbO3NL2xQeehBAgK2zCzsXMHwLdK4CtOoJXXNcxs/WM4fOliNXQZXVOR9G1jZ2WPbWduUtpaBQFoBjVCzddSba/kAD2i1MNTQ9iX3dAV4nyw+7+743a3djFxGeFW2nAb3VpCr5OEoWAZ6GolzTm1o1N42Ij+Z6wHoyHQCGKMG9PlRgIFFMejbu785j3l1Vil8R4mu4nQRy9yri6BP4tIZYHuBNwAEi0GdZwXOFT0hhm29+lT23syj4/Ck0/MZZsC8wolZop5FFSOQdj03yChOGlatL0UHUB6/G8wcz9wolueG6SSO/7g6ofELY4KyRmJaClaUGdnSDiC+wlADUsNSFIRKSfgbaTLTHSYTA5RFtJjA1KZsjirU3DUGdgxxttxku0IFtXqILsIG3Hh/U8szF/UzVefoCxodM+n5YoHCk0xTm7BXahr9BwX/sALrcRYalSrdRvXiYRRKhjZyKdeRDW0QVgLF07HshQkxAZ+2NlRE2Kg/rX6hMX6j3lF2tGQHGxUP+f04fsmHpYRWPfxSfDf8EZurwPej5m6dwQYxEhSU520+N8YYynYCQohDRBU8LI/VcXm4VrL9KnQ1Eox4iR8W3X6RR4ggk3xdk1Sz9KvzoX2oGeD3gjaU02aiHC3oRZFy++Scs2cGwb6pcfUHWlP/3w5Gt3ELjynQZBX3oJVzOIJfdVeeWlQr4eRl0DKrIdH9+nx48UZSSjg7sKiSJ4Ly+WPy6vXKzCZhBpkFk5yud6VPikjLqzSYyjlpZm0eGpukoH85pzc7Yt6OP4ofZnspqlaRXoYzPNdVSPKZQEczPpBl2XdQfy0MTyLQc8eBGlrUbq8xXgP9huEF3tBNozH/25+Cc+MPogrIpTxyvEflBoPUJzHb6gpEddGuyXiCk4wsGEVC9vicp/mQomJIMsDkb+m+KEll9Af6hxaL78C4ln+Isn2tmUQXVkHo9zDxEBAFnbjZaE9SATHAN/CpHM1Ee+OMToOLgSS8Jmg3U6UTTjRRvlF1khbIR2SN3VBOsUTC3eMTR0uRg8RFiSHMxpUKFL+BCZMgqRM+8G5alN9IJfZ0oDziTToIq0+9SsOGsMpISPWDOqlN4dk7l3gXINMpfMJh7SAlXZwLwL6SCDPHLN706NufyUn8fds9zL5spGinkUTTMOxry+GEYU8RIQa/IrrDo84Xb7fuZzO8apIo6YWBZ81ITBeoglCiKAM1wSkh1F4rPCWNM7dorCza5Ll3ItEhJIbTRe1DZfYuRRQJ0SkmqLvzAEFD9x+50+zjPsZ9kVSWnzBcUqLjkgTaQNieBwrzA243XHRsR0wGFyamNSEnB78egJZn4u5WtbV7nGjkZA5AiL47OoqJ4AUr83PM4A770i9+oD0Uq/GU8NdQtByy4t1/xnJNhrDSigJGidpzlejd6SA6zYLvLdHnqVGHQZr6lUouit+6WViS46A9UR2Vi5ZSLscdjaufL3J2KJ0BekGJdOtVS2SfmEQ/cMWnWBdMfd7JYJ/VycADhoMst2onZzK2qgXwWXVluosmLozF3MBQ/bxZ82HIKc2Z5kz0jyvqk209nv5v6gFYSTWeH1HunXuUdDYK/hKlQG77V5VcrEKM5pY8vWCnVgv6a5V5CiW9Tm255jUXjTuugEYIfnCCd4Rdk5/EdTiWurcq/Hn5KeX5Mv5ap88dr4X95UWW1p75enXynKHYwX8RwEJgcVYwcZlqGBlZhSHD9XwVbnoXTqH6ONAbhGW7wNYA80MlLqSyEYjL/07dJn8KGCZUrH/89oQC+XAa8+XbzLckRLNZDUsRTOkoFQjFx6dfF7oW6kxLkduJXzKQLxWwPXo8k2l+k7lRhLngG7fzFTVH4546SfOJXQ4ZDgqB36ip5gVJz36WBbfpO4Rny/2T7THZ22+mLnY9MTbrHQ/Tq5BQH7L6Vpw5U5WEqZfsiRF3YbX2kBoZSr6RuMn64dEdRMF6HD5BOE8qhn49m6eAvUl4Gvzp8WDSoeu7yKF1tUF0BwAvR3lfbbhERnriay+eGpCmDtQnqqD2ox5s2hrxtAnibsc1LM10aq/eSOhGaipSKx5CM8x/a0sdzGdzHbGXzKHfLK6CWZ9m04i2zC3IfaAcYOty/e9xxNU4GkV6aXXvxeZfo6Cm2QddY1AXv+3QAXOpTRDWR167992AcPSyvCWW0evyvveb1L8qaYgaH67q07xi3QQpU+3dIXWQPmUQf1YCPmebzKS/j+Ohcxa+gznJC+FNpV8Rnbm5rv4ie2N50oGUcgz7NCfztXGCvh4zmzblBjlhWsMRRfJ/VfaH4tKABav9LQK4agT1/wRd506QmDIsW4WAPQDBHwgpnyiko3TBeEYT8vgPY3l7DxRsCFBNEZT5cn1ZeNx9ZkuPHSvFIDlQlN4UVnPmtre4aM7lv7Tn7wCkJXkDiM1iK0UdD0Ty7A/KBTXnx04/jccqwiscikQLZOwGuWEBwO1NvC1zuve6QhZm1sBnD4nWbN1/6FsCbBm+P6+cwIf+3guENigqjcritRhpZnicmgf5Bjts+m1iDe++BoQCIrP6gV3JUHLwJ1GK91pvU3aKG/NQDPxacBLmEhhk2PEJuXQiZCXO26rhXBfbzkNPFVYVso1ZTifqaV2mGhFYYhIhpcjbjqqRJr1ae8CEpycJ6jHgE7mf0El34ibRo+HGXfU/y9RBMD7aR48tnVzlVd+REj/WGq2xykIbaiOkHSbPvVgpeNe/hTjihaQ2Vr/HUmL2xxNOrraSH0w4F9w9MYjlkrg3+Dw5DxIb9pweVIl4C8Sn/JbFJKdijDx6gJ0pzvCIXYSWy+ay2v4b8qWvftJJQUjg2dYuoSttXTCNg3smHxpTWxEtyCXCcQ9bh0nevL4R9bKrqJQXiBNIFqimsd7S17TFzitNL5lnGPE8qVao5yR5lz8za/708ztS44Ffsk4KKXwf8HEj5NC8KM7JRIBwNooZxZWoMTRELEIKOQMn/BAY02stNl/LYpyvjqgjHaTDN1RyDTQVxaC0/CuJzJQeydHxbuXdOPf3K38OIqMvXrN4EtoBoELzDrEYJW+KNOTBFeEcHZ7tk+ZBYwR6HdDDt/tAMc3gvW/UYxKF59JjJECyxyIuM+npHxqYyg1hqqiG+BLKr2iRlynoU5AqyWhS7qpJsMm6QvA0AcuhabqBlVgREEv1RrIzZ6GqJt2IECMhoUMFODiRHu1Ekoqrdw1funSjKmt4WRq7r1xyTZgcVJvH8DdP44CXR1iAG79p5UwrlhFSa6VZyLBKUTgXGj7XvhyYXGUBWbkRazfLh1101x+l/G+n2id5SIOPYXOFIzzewMA4pa3UMqnsxBN8ilikeXYCrZ0MfAe+b0JL1Yr5kMdbk4xRzH+6puqzePjf5jAOkEpZgmdD0Qt1AzcK8dAwhVTRuK9aUj67mReWobtWPGmpLGo3dDlEvXk5qmbT2Re8FMy5RpXMJfwORtvnsk3lI93Du/VsVLFe+poXXxQ4bgjTDYitgWXfjW0Ba9DWrfMV+wQUlSqfEUpwF2xWDdc41vujT+t68BOfR4jrXIIqk6xffxe/boYFZaYqEWGvtaernc2cxCa7WCPvvmhMGergxmoEMtRpV39kyLbR14+1ZuiRXqe8eRU1rAi+zJBkehkldMmQKtgbbVxSlaBbC3+yKXfKKzNwTcI7Peu7LrL1Cqc8/dJHq0lUQWr9n49Vr5y9Y0rHoXtitofD7xua7AL5nCF5qFkB6rL9sEcpXhmwpSgWIzyWjSrdqh16JXk3BEwtkKC0kp7rY3JSih1wRSnQeHaK9J+auDshwD+7U2FwmD2sbhw38XDJBFdV6RQ/hSEuUpWJubkxUylczFFoU+UzUCRcxqjEHOp3klxF8oB2gVASlbRzM9wCmdwGWJdzFBIJKHBdEskKqZJPD4FNyH0ipB2EjtgD/xa/5jU9cjYJ93vjS4jokeM7IkdDMBfyGLIc2OoU9SSexpkvT+2N6XUaFYcBZ3s4vM5S4ZxHigO3FsBAGYjmiq9xuhOtEyBZCnHwYO12dKGF2lubqIheErYQhg/77CaT1ohAH5CcfS2yd03uOH5Y3NCw6+mWDKdomG2hukaMm27b0s/UUsMvXguUXIa2JnBJ2RjAB2SxSFm6R5qYycv3f7yH+WMUrWZhq+ozwmG4LmwNS1GCOwfv8WximgUWHG+/relmhlcXg7Z8FlXVZZXsUXZqQwEWfLzLo3I6D3dkqkR3sKcShNpz96miqwa399dUWYJr/mf8onWGKagtmAeuXpIycBKZxXhPRtDNLtWGHMjBmI1A0BrZlLIadRMPl8W0SNmKFLKuiMw+Wa5P2YQSXGt0liFqDm5MEicuohNgzKvE9wCLBWa8gBB3Yu8AcZzKzz4T4mY2YAuk7w9DVvSJv9El/f6Gs+fizhkLmmrunSOFkKKdCKQnSZglBz7GtL0G6OXYfJ4IZ+ltwHK45p97lG0h94NiGWI+4NdhJsMcc/F4svBnHnewR+1vlQRcXBWYjYU1U8uunNkrnzGH9iIdRCCgHU1zVKGQ8o2PDt4YOEyalMX9+IdkZVAXb6O0WkdkGATpLdijTVSgt/5dyj+ppGYA0MZEj0+5Eh3TKHfHfAkwF/Sm9gRF1yZ1Bwo9enzcKjyGf6O4msm82r4pZaPDuj+JWJWdQU2pbkaCajdyu5ad9WkoUNVBNclhSkRdQSZUIckJMzwi5cUoplRi4Q1sEJtAvF95H6RahatqJe2Wjg6oXBpqIuD3bbyz4cVY166FJceTQY6b9R87nVZF1Q9F4NMManLg7kbs+nJiIpX5UFk9S9Lh8vv/Uu2OH+rUz+6i2263XNotx8d2bGafYhrv0Whbex9llwlwajPUf+7zYRvahiwCrsTeIcuVvdkFSjpjYdLD+WOaZVpvjg6RIyJ1Rr7ALXG8buYJuNUyQCwmxsFoQ8Z8O0GS5HXpr+in4KCNcQd2pNR2DaesGN6dJNTdFBAayULi/dOjepPwdJwtNJGZkD/5KGx1DLGJif0fSfbx+4QL9zwtYp4YrixQuJJd1HSsppX1bfpmXInfypGG44B+84T5BY2UfGyCWAhC+z2eauYgobaaH0oQi/1Na5ipvK7gc3FJ7KGaS2gNGZChilOiKrdlw6zzgaNydRmpRlz5ZWGKIUTkBPkHlRncjwtaBSdjQUD+luR8brphAgL0rsTd7KoK7J5bNWNLjI3Rlq+u2bHhalS/l4dL+Qi7mxjKQ7vj7G7txEIMPc+Qq3XBhCYxBeqCGxWvGFHsltBRivY0ct+BQkdDppC70/RASWkg4faMjp23kKzmQwHrjXm4bWoGPJbJ2DSIvXAa7u4EQCTXj1nqrjP0KOnl1U2LirG+q2LQXpU+y37hOVc6ivz2xPxi9XbaKNqgYL6agSEQZvvvEj2TPmgX8nM2j/pD+qNr09S4RB/tkLDys8XzdwqnHUYFNB6xbMTm900E+fLSAI4gwwzocp7gWhyzZj6Fu8DvmcAlfQfJ67ZXnaO6P2M7RYvRN2OIULcpmr8w61jzWB58fT96X2vPBY2ks0VsdpNc7T0ILuUpLYk2F7DmFnCc9C234QTJsBS0GGme1D1oO2wjQDsls1+WT8+uENvqLYxFtUoxF+95Qu4aIhVu1hwdCvQCSM2ljwh2jl4hEeW79pSTwFXLoRteBuTYeZDBSo1PNn5MUVVatxcuAVQJqFVmFqQqeR2C+iF9xqoRk4sb0csPlyhY8fYoJ3IxOlI1Z2hOKN2+DdgPhRlXXQrxWOk2ynzDatWSrXKUgYSUfS/98WHyyonaIlJGGjWHTPsFLZGcZfdYoJiwrff872BOY81R7+lBY09XAYirinOzJTePB0T+azw0rVnNKiMY6dEQwqO4IBHblN5mGdqtjZ9s+Ed72dFF/QPP0liYDdnaqsB5RY+U/OoMxHThPdw31fkLOQcptuhCkUDBNmxnLutm0MCl6EfrlTuweFcjosnYC3WKupOzrh101YUThH4a62EhdzCQYIqeOApy1DwBvejPcgltKIi+/T7Oovdj9syDjdKVjZKvOJs95C1thI3zVzxx1xn8SRhAuVqqKLcRTEkxR1gVuavZiQMQHcX+cO/ED5D9lTBxip33YdS1bdvyys3yJWhCwjnYZuzuzWrR3wr34LUbou0e4ZjD3gTmn5IVFhRDmILwFtq5xRBfZHPzLvFmn/2LeeJwi8kqDbz+Ye6N0QjDux2tgBDxUf4AWwdkFzouOmHQCisy34r6slXzWYFIhwwT/zZBJMMefFBVqKjQDRKrmHVrW4Iw6NcQ24tp+QWird7CIBU0xun9Nq1gnUvNJiwdc/eflOUuO/0rYDRCsBVnH/SmbCiXOmBUzNKOvcTQ70hNXydaFYB2ZS1roRGKYK6AABICI63z8SBUATmigrD7LTftgcmkd18JcLVq4E7kmrT+BhCXyjmclJ7hDsMPxKBIbNBar21oKccNmuxpCrXgmWddRvr3QMHfNOo2iHe4d6ekQ8jD6iHtua3yLIBtxaMHSCoPW/Obuy3qMEf9s104OeqNCrg/VD1u7yjyu+VblVx0g+D7eHbtc8X7/rMHavRm6/NLzJr5jKLXAFFeWvPIHhcpn7rE9gBX895v3OSIte6c/eVZpZ0nkUcN0/HD18PFZHo5sm3qaiqhPDwvtSGkhJztKEhkK9ra/Y9HP8HurjFidX+G6GdUXdleqwngEkzOsUKhBYkp0+0pDO7lWItd8puzEzmBJGUyGjVQHizSxebR5H1osfmgqVghH01mev5iXH0yMfsBbtqqbpE/n9h/xGd3m3JZi6L32KjTJKGgmIF/lfr7B3LFeZrxafHBJ0t1mje7tsSIJ2XEQywkbeKrETynWIZudlEIYFfoSQaBfRKtNOkisjw9jFY9c96IqPa/Jgwvc/OsourZE46/TwGq5h8X6BY4hj2w5hpIQwFFRYKNOB6uz7v/Ujvkoh16XvABjQpvqu9V1uFlwF7+MPmAWCrVV4OBGWPEdH4huSl/41HTc4p86BYQLdQJMeoK2NPRmQhkD0bACU/mGBodLGnFLNn2yAz9DNk4q+Qt8y2BuZTbsH0UD01jtXrqbVvGDIGIPIMsgwcyIfL5RVOqruUt4k6VGMKHKzTXBgxDey8l9nIQ3kL24/ljZqLuRuZldL9s/2vhXQi5m0cUjvwwCrOwiEHUK/vxFB7tFOLDmsojbKgSBR0lXMXUejunpWMPqIFj/yN9n/aRaMTbD+BMrGPVO8St1POhRF5/U5rzv/033o9eoaHNctUsejBWZIsqFVFfX5WckqnqiloFX0nsVGuhvcEy38z6wLX5YE90NKL8nc3uTdjIERslrF01+wRdpXnl1SWIVsmZJChR+n0sw7XGVPeyCD9+wwgv7w1kRz7DXccVY7t7mD2wp3O/NCQhajvFeQBjguwQbwZsh9JopddkIq4gvNLH605rySPYIa8ncXpAysNyzyIOCbWvVy6nG4MxuowW6NcWLKFzXEzuMht50q9drFK04RlcrzotYkvS2KL1f8yLAD2FEaL/IZgbakNMZEqi3aQFFaBjLdjKLLveXDQVby57xVk/CMKJaufVCL393cGJnk1BlSlTNfSS4idGbahaGXhLr5C70I86NdkOJ7qig7bUGFr9UYmED9RQvvJ36MFPcIfslBHXI/HKNqHfIdj3QqgXhrrgdFdAIkW1Z/8ap+hsn5J4PyKrjGn5y+eRtqmQkjXRqG8plTcBx02elWWMWSm+qiUjoCPZl7/DCylrD3SGEUYGgu/jUd19w9hOd+nVVJys0wjp5sw9iAv4pV3RU3Y4GdI4444cMHiq0khMDxOf5Hb41RA7nOHB4IV5JMH96taGJ/K+oWF3B4J95DrEkM8YJFz05oLXslZhXpU5keYaNr+YJ1v1cSeak2Y8SfbptasYKW7FxK9g0nVvDIee7Haz+yFbjBepK3m8tJ7ZZ6vT4x3E3/VEWMZ59c0wurTwcBdVmkqMII5Dlu1DkJvC42xTs4QkR90YM/mZNLDXneykzy9OprffEkG0buETRfHxUc7iIaDfHIQiu7qxtiDwiP38j7bYSWCKH21MdEMYf1+kKlO3YJ2dseCnW5JcPP264vI3ePD3+iobylAbPwcxoFckg3Dw+lMQRTr/y3ObHIlaxP+MypDJRtyBsK53mRGposXcB3MA7SEC5koX5uD89zmRwUEauiRlYq610+nCI/5JEtxX2H9hYpQOBT3mWOgqPZGyhaKFggNS61twuDahfta7YfN5et+KqmyLQNi1eu4Tn4yFb7vvRHfnstZH6BFLL5NBhdpdIrOYF3Vexd8RgFcJNvqZeuYY5CXr6YP2mnGSlJTidaOgJ5Fp9j7uH4yE4iILJGPeYvg8DwbfbH2InnME2S40a6XV2HNY4prA3K7jyLV5UKxEm/BY+oXt2Be3m4SwFP9zMf05ioEjnoN38u5Dw98QBhmrgt9uYHbneU1odQa03WjKkHmmMyTfSnHeCVjDnWOy/l6+bFLMckBM0R0QgW5kNxds+cOwbIlVHpfQzCSXY9Z7nj4PrjlXox2X7Tyzb1rtA3j5msRAIscG9IZY5sDZAnqs3Imm1zBZ8xLJVFaLqBS7uLDOK1K1n9rz8rHlHvacMU7mad6BLZ8BQ88K9OwrM/Sv7rfZy5zjjqe5YCS/q6Q71JDNBO13F9s+uSv3gQAokoHNxoHD3vOvyxs4QJsx+YDi0HbTwAJHPZt/o1dJW9PoGEfqn8916ym93+5NYtz4+ef9lOFv+wboWK0nqAOtZ7j1OAHkiRXC41Ho3n9aDJ7mI6gMmiil0Orfur6PaaRSQlGVoLPrL1We/JQ42H2vgmrLDi+2G5C165c7eIF4SGEDguEbRStG+bqQag/qRuZl6evjNftpBDNzPJbb2DiJfcIy266le3pOUUZxYjSYgPJIABSEz+/p0nonSW7e7efI+TCGc9HX1DlQ4hmREGuF6MQUgUQi2C9Uml/F+bCBFsSYewdzYDKb1opES05aZ2/fffYQsrzZNbWGDmbJn6ylV3TDsiXkAS/qEQQTroo4r6NzaBxyhyWeLTbasxhOku+nqLbIcMUZvwqUMfHksNfT77q5TECpXp1PJmJNPpmm6AymeTaRnSDhxwweSvS+XgYIhKDb+XRiZt5Kzz+uM5I4TiuAa1dWqE+HllMvfuCwKsMmwVY6hsflgA/BPMarkm5HeQdXYRYvUur9n1diT+kmr2QxhqmKzVux/MicMcgCs88ieZrGVj6m/8MfCTpAli9yDsQOgPofCSlCS4H31eGzyxnV5q1/6oboCVTob36K55SLh0X3VcL79JvE/YRmB6ZYwWXyI3tmcGyO5B+uT+qpfOgY+4uYybsycHfogQFhFxb9XKByfuMuAI+qdt+05zZzRn9Uqp82Lf5JvJd8A0rolHLNd9xly87JX7rLySSxGCtT95uZPvUCJKi3sf83OP1gPcKBIGqcQgqKjgBr5KR9ykMSCSg+msUkmIhSnnydGBJNzhL7v/o/j2ul+OBnpjrSdox4rh2wWFH3zp7DmU40bq0VgGr+SVDjxwGMJir/jSaPos5bcz0CNZC/KKBNvARt7NzVHAS0nZGCBkM1EkpcbJA8DwyUKo/asufhfXSZa+S0ziM0IMcyzWIoT4NO/9hHhV8YlUNZrs17gL7CIKlYrau57SeTiJ6AGCSYeTzETG8aQNrrn/2iwp69e6QWBkkVZgzCCbtPizLNaRqZUetucGU+LgfuVGW8422GFJFsGeVOtiSDAk1mPx1nBXUkuWWR6rU0JsTkW1BgHsZ+bbwm/UDpSvRbdeM67M1wsIbEcpi3aRWLs4MfQz1m6QtZd9C9LWUKicEwPHFZ2Anuchf//TRl2yNmj1MqTyxIxSE0J9Y+6wjS/hy1kiKYiZU/DV5wkoDIkRazcZk8HArCQrRiOjz5oUpxwlznn1ODFwdqA6reXxXU6MHvkkzvH05hqvnGQDpYSisSkm3DDxBp4NMARcxCcLoB+2MBSIOh/l7pFDBCGjMQcvTZDfIBy5gzLXf9mDY5VDYTKEIS53YsOVy3+gxqpbc/bOiT/WsZ/KYUOpRtq4DOOAZ+L4l4NB1FW4waxRj88XbBJUb+58BhcP9OD3RSnyN1R9McvmD0OjAZECjFLzIxT1ZX6msIqW64TOlP+AsuPjIxWpUWrAJJRl3+0OW2zCg0nmUkYL58rqfhbTrastgL7aP5YBh47G9mgD0anmTKl3UawX25LZltzuB3Pu0UV7jZA0Els64qc4LuQuZxNGmBZL8Z8yAOpFtqqclURsEE/NiWwt53sjIVHlrmxuLm3RcotUy8RVuRH4bXpg43cvkm0No0oeghYHUvMAfW+lIllCZrKkpUx3KBPJ2VlYquIZrVSjggHXe2tz9C4JojHLBT22WAiRnfaBSps8Dv7o+tehsENwfW7wKBH0lRdPANIMev3P2kCGfTm3pBqqqvNyNoTSdGnOmQRF0SzcI/ksUg3Pk4js3xwD8g3SEuYgCAjuIzNv6i581/rzdJSctI7jk7H/vB7jefVgBXP47/47Yq8FgP5t41LELU/MiXIyLV+HLuQRBaIVcHVFjRKTUm8sGPgZIowaf2IHUaRrwuSE5FSvjDh80r7aaGleZTHZ89n+J0knHOw1CqZwqWjp4wFkCb2hb14X+m2GZ3orMIw3zeanBC2MCoLr7T9jhABVZffDVzInbIkooU9n/MfGCyLk6Hz4A4sr5vZtaObf5oiM2qBLn2SzdhyaYl/xvDjaKKX4tkbiq1F0eGMQqf4kiRQiGBfETARNp3lSNkjerKSEyHMKaWdJGeODe4FAlGEtkr3X42De1p2cjLCUcMNqcp1wJutgBDVj5l6X0xawhTIldlNIJEUeGRLmdtaZmNXnBjDjbQ/2e2NV0PinaHIzIlPyLRo3BDp1Tynb2Ny7hCNMBMKGyO87LHKYJbIBp1FlvXNR7Hwy/RIph/HajX1amB/6Xxc9Q1C0uTLnBul0CtpNd2iAQVhgcLuJKosz72OenF/oTTuXADdFVkqAVExLuaVD0JP5Jri2Jp6je13+UcOvM3eywcsDS7n/kDsvcSw9fdq1Xamy9pvJhjolxlJ5Gw62aPTf/C3kbYS59bcLxQ0cDKeqa2cO6J0y7inEEv9xCEHQ7cTe9lWRj5t5mWQEGlWRl4DkJ5uc1ab8ogKqLZhAQXUGv9gOblx56NDCkhUVAKUmpqwHjdrlra86v7pxbHaqNanBSQL0IjDmbU0hTqPaQb8rwo7qRYzcMSjHZBwrmmWlcmdRkEvPEdqzFJsxRn0151tNMcTYa2ZOpakjW8cNJ3eHD+dohcqQgMXg983lmOuDv+ET1zKDwrnexhds7u4cniQSpA8a9I6Dps/LGqjjGJ9y2gpKCVMQ0D1ZmdwY91IOlKPjIjcClHQtjgkr5gWd8ndqUt3u1yMxtAojCDdPE4VzaMiwHW1VLtx9OAIgc8G02KlKAo2HBr0Cxbw97eBO7Fb9mHguO+s27x8BoNsR+nO9t6OQElA28v9qAGA7kkB+XhoT4Z2jouwmqnm7x8d6eQ32doUCgXGmsCYzitfIe8ePKkyqXWU2IKNEdo5hJFWOfVfLXcDNCFWg8r5xwkuboc3wIt/THEAd9l8iHrJUJP/STlQ1K2ux5Ott4mSAtawvCXE3mHhSbzT1M244kWA7Y7JU2ABivLPY0vasspE1+mpxZynSs9mJX93O2l2snfrZT4XQH+kCWl8J7gLw136Xy4UBCpMbYo2bR/12eqNYZVH7E8Dyvqr7jgIFSLYY5lO0cSl+xL0St+rugbYl0uFZTbnLOWa9Kn8J1n5UA+/dDL+/p1VBXZGHaOGeFUjt12TE+GjHYBmbk9PBl8crzzayDyaIWbNW83mHq9XfjWizaOmMB2foKtgaxl9r3UvxFgnOKROac39oAnXCzYlLuHoQ7YwmzeJfBTk901BBlMqsCRRZY6COIym64XEdSP7BQ+5bdlkhnHc56xTpM8uOhO8N9iKGfYvYoO8QNwGSvn0VYWvSiz/Aqnae1d0buZ+ytdTPdPVhMzOm12eXXnfxJX0wzKip1ZbF0DDjvN5izJp1l5cwOV/zJgQ1uYBNJGUm2zJ4qkJ/TqhlAOb6d5Q59Zl88MmiYmsYL5QVbUJXYS1zZ0Jz301YjPxK8sCouoL56CNOBirjWw7AtIKwzfI1/T7CZ5Gd4iGqY4MeGTTGFT5Ypg8ufqadDn0eB29jqnNlZBU3e932XbZOF0eKd+yoV3dI9siyP6U2bUAz2lxXOXSZf9cuC3vAz34nefQy8Xv6YbofKPLWvRofaXzfxngMrE9967Jm8zf3FDKDeSdIrSaRQ9kxIuPZscm8zIgLDpOTfqhpVAXNAxLLDkDCHrWwLS4N5Thcien8NYMt86FwzgLprMg32oC8j4HHY1AJImk7W6fZmwBElaoK7mQvxCTfUG6La0ZI/FSWaR6Ptmm5FHUSAPE4+hNrj5nxPgEvrjrKv2FssH2fhyA/Uk5ZESribbeY8GFRxG/j9Hr4lL0nem3iNYSM+dp4UKYhEjnNSZSR1RDZzZqrZzHFJf6iFQYsJn/RGZuzfHJ20vFZaiPCes2wbAjE/LTiJq3tqk7aoN4BzrTntTq4YKWScCytEDbx4tdgcW8jGWcURweMfQpoDihloKOGoxfvw6S5hyiaEHp7qht+Em577wLkjMh9f1uSu39BPSrTKNIIisQzKQ9ZfO2VPo0BhZpT8GJE4eqIqoQfGdLSdeBSX04l8cwUZw9GVZYIzGkGGxbS4Ta/034KmkZEssVL9Ge3jxa7ZcsMxN0rjjtn/uEoIeOIbExJhXC86Y/rx+RtwgZecuSoAv+dAkTgqlMykCtRQpJaLAoYWZJaRNkFWHMqirG+Mxz1+TA43GdGbZRA/Gz/5SDKMqURUybHoGvqozB9e8rGfFNxc45+6zASxJkBb5IKdDsx3+6ZdCuI4zP+4y2nnf1vP/5/ddwAS3esPXpzDzhYwaqPzWzVq9Cnv90dRYs0g8ksxc6PJiob6MB4igzW0OnUsxTXMEwS9Zz6pSs7oIA6z1Q57zyWpX5QTbj24i6CZLHLT+3iD1pcdLEUs80/HdPIRre2wDmAdfZ2SERaay1Gllad6xNZ0/1apokOAErej2dtJ0ckZZFqQZkSLw3HEx1GB3WZ/EBbAWBN3UUGztQ+uTEI+TnkthFj33Wh7XWAlEELXbxCQXe+KdgSXTCwVgGH2P1GvSXYRpisurI/tDgrHQW5fBuSRd3DKnm6uzCH/YgswJAzc8zcCu66sUbqxD1qC4dBx7CvGmUQRkS2bPPhR/26BKTUDnl2jVY5+3B36yYEgPJv3gecnnQc0MtTK69Dm0xbJeTN1qPtVUYNyJSWHVgQAo/P9Z/Bw5Ip8E7Jm2WeAJ1j6z5imzH0vgGEETJ4HE2SG7iNPC86sPu3lEcIQC2u/to3kWRHKcpHo+B4oOOM10MUJTj6QAimpuNtKPCDiLtXXG9O+eMqHh2MyXFhxoQEj+7wXz7ogX6FiJqlOUztTbBLA2mlPAHuSAEKVwrRHzt4zBe6hb7cPVfn13onSekPdcGpjJ0C+07H6vsrWtEELqVLjUGi63i3g0BosA/Iq6BkflJXwY+ckvaPya7ybe+OoWqk6uxwKkg40pRbNwlmpsU2pwH0cFHlQ3t/vD+Lyg6MuRwc2KRvso4DtzktH/jwRHBkVqEsyq6RPwUFAaccAyFyggJRVbmzuPeLOnXbBlvQpzECABVZfycahNgsvXFYbXCXgG5sj8IXuaUrokSoPFLWmTzd/zqIX1kc5lTIYRejaOyp8N0xnyd9TN3dgiGwLo82lHCMYYuyCoubn0+LMtxV/orNr2FBtjpQF2FbMdVDPggJebkPbQMyKg+vzV5U4z/sHwUCCjvKtCDjXcnnxp4/UcHONaETHeP86Jpy+t50ryyuh71uiK3M8J7xFtx0q7K81+euAi0QkPHhZkQb2wEpfHmMfAG9Xoce9Tzx+ORvb2R9lKf36CF905HEAZWgNYWbDdVXBxoz6s1zw2Y+3QjAL1z/N07Y6zq/1+2HuXdzO+dSx609PhHdLfuI2pvjMMUKlP8fJfN1ygVpbsmF47PdDlk2FmO6G5b5XCXDb+8uaXBQZXqMwLaibriJjP9DF8Y83i7kBdlpb9+AYMVAAHnvyJN5Elu0XhYCiqBrN/IVl+0aVJhdT+W38mU85kTHF+2bQ15mFIPE6G8I7No+MxFeS4gbyVltOfDcfvQcHC6Msnga8Lar3XPgKbj+mHPSR1960XlNQl8wxClyG6m+j2JWnFFXUCi400p2x4/1d/Jww7FrQakTxshWYpqUJEsRUYArVyh+pc5tonhw3jzEfnmPWBcAfxdkrclE0Sk8tnBe+/rlZLrrpoGBLsB/UVYjUNoKhaY6gbBcYHM7qD8YXNPFhyV+MCYr1Jer9GBoV3fZoTWpbk2JbEREk4w9HfNnFuUImWnqqA3TXyqzKU03rUaCrv1LG6nFIhR3HFigP5X5FasgckLeHZDvtEBfwtp8n2I0RDOsXGtTBTQneO4JD+b3/esTuOCfi/4I7CaPlJyIPlMObNAx5eB78fGaFe0U3Gy3aNd51qGpZnkyGemmdCH4bbwTc3lZn22X7EisP8P/dF318XJ5nPF+6xPsYcZiyWLNbdN46zBeS9472gvd50cyfW4S7pQmDC/uwnLkGnpjmxravXxNzhvdaJnBhWi/V6dWW7Of06H5uNx87quAhgVV28eXFCUpM7FMPerekWEhetvrtNFPTDI9ez6YMKyWi6mTcRr+vtyEY88O2h0y4cQ8O6rx5I0NCvKPP9Rc6Wjgy8b5IUsIyhRyZrpEf+c8WAq0YcVp5itiMeLEnldKLl3g/wzpijwglQB/MFgcyL8Fg9eLhSSpwDBRtEoUZwYAPU8F0LkKM1rGzPoQ0mtc53GsR7/YFd8WAWfTEryEQ+YKjkZs56oD1oNoUP+u4fi/Ho8P9apr+wbuWtFKwnTOG0W9xylDc6HPYPnYHyGzsk4Iz3sH7KdA2OST12lpN92MPVMQiBK8l8D9EvOjQfP+udi0LAVAVmgzWBY9SD5mYoP2y3oE1In4ujygF8qTaQ79cJ7WIiL01K74X5pm3APbklQ6faKqSINQP9mKXX7PT6joctrGIfAc/owQ7nkNWLkdfxIg7WL1ORou6HMwNVNpe+XCuk0l3ItMa1bpMTK2I9VLRyIyyv9u9oBtgSaaTc/JaPh2IXt8tkRkwDO7b95G1WFiTJF1ACuil4nryLj6RgG5GZeoAOUe9qkHNs46FqyZsK94IGffu78sjhYJEN6rpZZ51mDP+8e894QehDPTJRE9Ny3lxQXADMiXB2lANpMWiIwcylrw8CuuSnXh7MZFi2hh1hxHxmQe2S+3YaAQ3/tfP0E3qcEBfETqId+s2WdT7EmQLx1VOCZswvmd27DTC5hLd5oGmsHau79n8oZPQ9ybZxzpNYwLc2r2CJGB7F9eo9ie+AGAi2ujUTjKPD/5ebIkRUZYkD4X6kuJS9mJ5NQ+D7Ig1Pmx8PVNyGezVtiTZoy1dd/YFvGQAut6tbGXaSxGjoQlRKLuFuVF49Cu2iJGowmECY0uC3qjgOH6SIGgF1O8W950j7Mf7VITwcSzpI8Lw1PryR7ALmtXeNRrzO8z1qKE8WpqnI5cU6AaxyKP5bhozY1omQ92OpPeb1Gw2sDwFxp/RbnE1372jj38e3RyEBLmq71BauesVWTxcKZdMM30YPcPws0qM+wF5Ts7kCtdF4+ZRkmVfImbh0ZxGb5xvR/vgGEKhr88uenndwTQ58JbXKTxuSIh4YuGflBg+1CKXHqsWTjJ4YYX7eJbb/mMV//COlkfarxf6cydzhxb47RVbty8UzUGDNaUnoNyozCO7lj8HncS9dyzsYCkogSPkFg/a0E0+s0U2afDfHOc0ZuxhQeeufoq6UPx/ARFx13HWZ4HIwQtWEpHqtigZW1fQkdex8g8FBLC4+hHSuOk0ogIYyZDWlY/oIgP/bVzwac/ZBv2Xpq4myYrPL7bWfkpzIkr9gLuzrK9eSwHpzUqbivrI2NwxIheexPATBxl6ZEGXG+3yTRtWwgVmzssT+GcM6h3eLJQTF4PKvcafQ/z0sGBLVY+hMbRhI7hMdExiRMtlFzu4ZE9jZX6po5AD8ED95JLZJExpVjNzLX7j/9n022UCJLlodBLTzNjbrPCCgUlNBpQqJXZzOKGzYyzTKYjNv0ZzMz9rDOlfcyssrhKJ5mQ7xpbA9462VXr7BtTWpVj3+RB4fnyTkm4y7ON+xP1qwtAv+OT8KeyP+RFuvB0KtUDAY+dmRQD+1saDRSSX0QXiNeo813kkvmTx3vIm1DSBen1adr6CVwPTfO0leqmRTYmiYg9ttKMQfSN5IB5JFdMeu7YEGrbzCBbunOgtfTS6zM8m9nBHvWLQmIRZAcmtHmS0ycnnm7tXLk80OLQeSzJ2dzeUCGeC/xug7Nqd8FtUQxyax9rzDYMdCovCVrfmTnQSwkfykUQl8bT8QKmnDzKFPb8TYdbfAMxIdW1V4p9BaVvQqeMOIZxpKxVQZEnemf3ZTb15fnS4i2AtIVfkmvb0Hy10u03pmKsrrxFSHsiQM0BYLQazql5aa1iz1vCl5rRpLz1Z+NK6HBLCBeXCwDDhMfuGWTN4zdOkBkq/+UKKp3+MCqhKlC9wAB9AqZbjMtRKtMis3q5RQQeNYbg72Gp87ZTZX5qGNUWLtDUkG9AxKDPEOeIM+8J2ofu8hmQtW2OwQjUxWwEILTs2+sBDcMQ/ZdR1Nsuz5urraKnN1O0UNoulueiAmy6kCzimfz4CAyDMKW/DNX6rrir+n88SWIoOrGftI4XqtOC98rXZ6DUfn6uBF2fyETuA75crK7h+kFYBdSne0QiBkG+EZPm44JnZaWJmE1KX+7hG6CuAvVqgVdv8HfBL+GeqB0GUQb0IgaWBy4MVMlCG3CZB0t+naa12NxyPHA/l11eAsNA7FMHNIzOoQSbN1diy3TUdmeK3P5YLbt/WIV/z3rP9MgucjcZ/QAkxm4Alm6lMK466sMRre5V4Hz4S+eS1OpNxYDajSBoBiP4wenM1xT1PihX5nagBbuxslVSoiaz1ZjMfKqJV0qikL79BHNIyved+JPCAgXXuS4EMrEdEmwnOfkuPncddc7E+sgmlYaO7fQuXJ81plhwkg5H/xO89PgLNMRoIOspX4LoE/ZP+nitQD33NjCRb6/eeoF1ZE6D0EnLOW5Vq8MJhFyXv06UeeLGW2DLDuZ3O6itSEgNxeanxcV3CCj/1fjlzkiqQ9KmFnscFrf1W/21btfd54IvLM0Rw9gA4xOU4TtM6bkRYd3afit3DJdgcGkjudH9nQMLJIobctgIz678AppVkIzRt57bRKOijKtPmDkSUlVjq58hGxfg4w709yD3vESsW4AOnb4fR+DWwI5mC51RY9yU/7FUcZRL4T2vpAgrcNWvRlUqXDiEP6Cs2b1V0Be/BVSurq9SgDQQje7RPZfO8ziKNTRBDCaP9S/6dIlr2EAno2QlvSs8UhN7h9fjfZZ4MPo0nmImnVF8tUBTgJad9YRq2cbMuqLYMTsksif3Dmx+u2FdZxhi32EDxtsoD2H6EC1EsW1xWjieATYM5qnzSk4p634wofFqSAXIDum5vlUq6+7Dpe7qkfwqvoryeJGgKDhI5nYxmzjCtrBZTmTNDo3G8FY8CMTgzh9D8VE4Ue3lPGVSZZps7XwfQHg3/qeIMN3nL83xE7m+69UqNlpfS7TgOEb/CkQwb8CUO/5sK5aKHMIE89K2WeSWVGHaOPOM3XGmQyuusdyJkm3HIGH3+1c7+ovvr/vYs5sgS/uCGU3N3I8EAbwQwZwD4o3QxTifzeRpgMJyLufooY46+NvzdWdaAajZamOEyWo4cmdqSQHdLZKwIrBvLGMF/KuXgg4+c46lRW23nHIKGq4ggzTvM4eVVsDu4cWNKqC9rm0ecNSc4on5L4CPd96sYBCRsmzi/IKBNtF7rT97xQbrJs84lBMf3WJNUrzjO+2YH+L0vLSgXPPLScvvj7LA1nDEAAYqXGQukLNi4IBM8oG1EJBn/gE/OID6c0Px7qRBwEzhOeVnWVv9FUuF7+8vZjyBKYzGBPc4apiYtLKOk9uND1RqXKa4vozylyJnK9ETfbyPTYcciuy4DbcpSOxRBFWkwAZGBeDqw+LERABPoJx915ujwiRVi7uE44h+RSEFKC7OmQaZB01vUR5Zk7XX1uShBMIEc0PVdusYnaED+pM8bpa6NKWoSDCf5G9YyNahGbIbhykZLReGexwhGETlcKxNYy0rxxRtt8dqAUPUecf65V6yP1YTW9keG/N/Ik/ApkJ34VLekxx8l/6CNGdZglrI8ij3UQQs0q81Oxe2zTzdo1bsco4p7Glwno1hsncX8VsFJv/nHw/rLG78AwNuk3de0J7fjPz/6Bk8WwWaIW8q0kcpEo4DdOmPO8V6+Xzg3cO0dUq3gs7lPGPP9aYhDCwf2sHn4t8BJ81JkkASvuBsg93Qg22+Y34YhwOyv9xAET8BH5uzL1bYlrp7M9/OzSxWJVh9R2R5ffFCKbMSV/8MuFW5kWvlvfj16fZ4STO/b7kNhj6luMC1N7i31A5e7Ugf4NQ+mbQrFtii1OLV5lxNBAxquU/7FHqXGM+pN+xeRP0ZOZtZRqG7ov62OPAe5Tu8AmgGBqcncZpVxvM34j/5AHdDunDysJuOPqUrls2tTO/A0RWa+VERRFFKu17kTAjoT5loogsiMZUfsG+y6b81c9rX5n+QT/M5SCaTorWWTEKSFHSD4XU9ZYYLaO6Z9PmBzAhxIL5o/1X4sLQT5zRyiGMnAD4Li09N5vg7Abbv+eMOEmBn3SP9TVCNl6qpLOfPzP/hUiASeX8hn80vnBWekSXYEPlobJh7/xT+kKpmrrQXX85YrQD/hLkc87ZAmL7HaSB+pcqdsgOL+R/tS6ixmWlLkUimchjmMB0ssxj7eZuEILV6hnFOFKw6fpJegsdujHDl2IipraCDWlXAkHYztif0ElcSq0PriPLN9djGGPcJZCeH4vk/tO9eiqMfB6bmGQCfppbHmfhQ2r2VpasKV7/XbQy2yXaiIomA+/1AApRynsUzhK68BOVhqa1BI737wjUC9o7U5g5U23ucIUFTWlDEBOdCjXd2xXQPoQyv/qAcPyN3spV6F8nl57y3C3Zj0T7IfwlSl8qBcF34nsIfE+94UOp6IzF2Tt8q1pBBPhATa9bVoKq5YJKrQtAOPqFPqlqcDjxsXkSoWJA0bcy7CTExD+1jiAMfY9OAtSCykNeXX31K8ub/29Mglciarbrljmu7lRbEtnXkXb/qgNPpBcv83Owo1SiI/TeqEo+PSj2kjxwU/0lX4bjXBkG3+hXh99q+XNjnEiN+RxkyUMGhAyeK2omY/M1Ebe9JmZ5KFAim7R+ZkggDxGPMlX0BKMwr+OTs8A99rjdbz5Bhid112bkKsBI//uOw5hYdvp6SyTl5nIg20IUB087gb8sTlksoVV2/XAOOGa3P5M/ilyGa6uzvYCIP8X59AD+mHkf9IneykLoqq/78t5MxRD8FGQVjDL1hl990uBpL4OWPxPh7JVC0tVjgQjECf5MA7KfxuLe41h5YXZoCsm9kXJG9FsQ5a5BIbvK1pAmxkMiV4Bk2gTma/JB2ld3D0hawQOXepoNC9R4oGMjfmCwuKG9lkNE2GjHKT9bqULFbpJHBkznLKXphzXdYElCH2R8pmhcaUMexfv427DOHXGXK/tBdo+QoOxrKAkaSCDgJs9BzPWXR3YjFj9at2cVChXvhCJoJTUA7MtVDBou70d/Ss1iXBzVhLoJYmSKFZkQJGKqO6uV8Ns9eZBTs4yW4a0zIraNUqODkIk+PVT/js800PhVTJDxYGzvX7xPcVC2hkrFgA6ElxPXsRxzxxFJkZ4hN6qxQ3MNJApvw0UqtIlkoIBnZQJhOKF/UNJJJBKmQnmsh2ibidvCH6G2f8WYZI+DAYBMJM8Ol1vpUrrytx7qtrwZoE1ZokNspLzyJTppan6Awz8hSDRXqz26vpfQ40QiwX6RXBkk9Lo9UlzPgYIE9viN+kbjFlSlOIF+4pXZtRKyxpKeh0S8tNxUcE2hl/JcO0Iu4SEWVN10At8odmXk5ibkYd6xzNPKNlqYM8nZoV5Kl4iM00/bg0ppO8QjthV6QAsier+n3oiOtoiyUau2fPZdFv6S4qGYsBYyVWYVwdttGkzS3uilfu+L0WtEgO13Vao/ajGsm+0GGAKYrAerRiBNfC8/7ZGCGjeZLUxc3n4m79gL5uBBBfU+mWRnRci/yjXyyLlqE+YyhZyvIAxVZjh9K8cfmHXeTdZ88wghM3QTyhrsmx7Is4aRyrR8xHVezDPcY0WyHw4v+3OcDYyQxBVZ1fsaFSNDonCnfGHKXBMSndgeZUvyuf7r0lT3rk7zj4N96euvhTpbCfygXUyS4LGXw19czq9bt1YSSl04XykMsA2Lvoke4f40JJblHHxeJniGyk/Tg21uWt9XXScB+z+M/LofXNXuQ1BWBoI1ENpjFERnrDY69Zdvupa6jByfLg5uKblV4Bn//ChW0hZay98H81I9pF4T1xm2NiH+cUgf8gR+gagbeGHz97jiDDiEkphVg4zMuEl6Bs/cFafq5IdZ39hSk2uPaS3xLKmBPldcRDem2H98RTEYeAljLYncA6158AM7M+8mFSvk2tI+o+cUzhsFsyvb+3gjYICT498t+UPPTM7qaHufzc5WUnHOd3ocZ6Ig1wyRYJQFBBm8sRUaMWBz7pNrRFe1/o9dCgqowdQqBhSQQsaH1HPrmZcPZDBlmpcZoHn+RcKg2EO3h+JEUENor0OV3bgD2N3XfUvvS+RaqjEUf2P4ovkj5vepICURItbhbENZZc/CodZHtJ7fO4kdYM/1cHQPFem92v34brhpdpPEYpdXbm4QjXPEk/yKQEGsCXb5rebnULDwhavhNOS9Ao+h7LINAV6lWUsm8mGWWLwMQAY4lIuIBdw2ShO5V2x9GH/UZG3LdAQ75LhKiWK90MwrxhP4s9EfJxwczcE7c8ktgOoRU0phbTWJgXxtD5vHagADC+QDct1vEtg2BIEbKKXIC4EbRZUKs8OwYHT7faEjEVh4OL5+uRQlK4ptCaYlDJkBzhtVa860i6BSZo681oIHeXJgL6iO1PK9Nst00Ha4roGvAvWdXHapabRyA5BfHgd+pO3EY3t2TyZa9ASjKmSjySaxK7/QIwk8hQk/JCpJ4eMJONRsOwjUwuY42TswNzoBj/q5NaJExjw987k5Jlf3cXRpHt/TPooZWp2h/NJN7+TIXr+E4oYAsv708PhJ7l2ZG3ARWQqjBr5krtx7LLVuyM6e7gm2RKv1EV65i6t+PRIkY19H9XYUScdtL+qEbkqn9dm9fDbEyOorDua0gHtSFrwADKZIyCcQvZ2QCCWRY0tihklQgiw1QXn5lM7F8vTGzuQ8mZ1ZVfwP3k+KlY3Sp9HrQf1lqm8zlHCszyTZbRjjXx1YueLweGXYLXqM7r/ZcBskQjDkfBcoYe/q4aKhCRbPL0O3QRttAr3dol8zY/XMjoZZs2P3NC9YA2dAyH4bcDuiYbLHDQe4CheE/KZzLI15YU4nP9uU5amahEo6v3y6te/oeBaF6RqZdG43m6Wfsjl9ochJlHSbvZ7ZmiDmEr+vaMnLKDMXEsExCQpvgkfHSTKIa0BggHH9Lj2ZNEUIbSy0vh9R12j9bHioSncCl0RAdytAgCI5+7rQl5PAdkbVlpd/gbwsMz0SW4utQdfvF+n5g/0oLgHCIWUHSWgUyht0ZUidO6jpS+MUgBZ4rOvSFEyLVfumWSPv65+YnSVI3CT0fOuNbYFeVZCPEcZEZxE6Sa7L/V5N9wFAxt5e8uwNg47ekSIi+wnk1fIEsacWD//5OiVYLRWQb8MSoZ45mpXy+VvqBuzkGxOngcUA9EZIH2c/V42uaNVEMSqqbLUwo1nIulbjsvHLxm6KNmYefhnz0V3llFNycX6VkarnGl8MoBx3RAX1mzEGMJQ+hUIN6LAHJvXZUaNPQbLR/eBrVaNtv1gP1BWnCi2rdMRYAPNFjHJMGI6aDw80jZ8bAZbzdE2W/+4yQ16Mmp/+qRDY6QCsUxJY3GZS9A36f+4tUFPFIc13C5e/a6dXNWwLkJsw9viE2+kZ26dsPl9YeAMQAIcnWm5JZD8N6LL2NqgAlJoDhaR6e6axVGObQjuL0FX36642XOIT7wFwydegvyKhjR4XagbP7xfvBoYYJh/LRQrCGyQlgFLfk+ffUon0JFx2OszvLrsr7oQIYGhkGtWhSrOjk9C9DeuOnrG3quQtWfJNVTu6xiB51s48/UlCaA4xIWJVaAzImcIWkjTAn1C5XCGrvT/GehpDBDWvl8pDeluB1zzWtCGH1YPZNtosFtOMNDdXHVDRTUjSwq53d8y5AaXWoZVDw1ijtxgAGi8wYmAnM5cKhlS0mhLb+SapuYJjkP+0c0Sgu0Hwp+RGV6oh3erPpP4EG81yTJ3PYUxkf9kzGLPo3bygZjPbzyvxBW8CnXQ6wFCYNYvPhd78yc2Y3DQH7Ouc6oRn91wlNBpa+iOJ8A730zcC2vSAyIPZ1lxFN6Y8WLkVgFbwUGyRkGodkDvd6Q6MclhnfPjQdn7jOq5rU3A36Y56pRK0PuADEjyqRm7bQWLl2ZAAZP+1Yjk4MwUXxIZUYaeYQTEAc6uFzWrknEyt5VQQApE0BV2UdA5jHQpEJ9VF3ZI3FpP5D5j/GpgKgSqQ8yXZthSzvKBG3pd+QBgNK1jvUwHadM7P6pnPmotMftCMbgCf2s0xx62FBJx8XYzJbBMV0i6pQu0tyCEJJ7NZjO7C2wB/3E+9g47Hqa7PC6ylwaTBB9TDKzTdsGfyc/+LRfbc7L+YNPfoBUsrYUqIsxVSkSA9pcCbmlz1Va/PNw0YMMLCkUzXap2rSESV7lEaWkNPFixM/N4ZCyqaTxerjsc7hV+zdZeawFYGEtWbGK3UwCgctbs7MgW9jF/mXtRThst+th11SQkA7T/Dzs7b0U4iW+skaqKcs47xjujp5fLMQiNxD3yFhP7yM4WSHikAuD+IvV3ZD9MK2TWyHBfJnmIPJHDmbVfC1xisbW9ntmjHfQhtLmWyERue2O0c0bTDes0/XVVjGx9/eHO/MRy+7fXhyg+x2z0bauaHk55u+xEG6U7xFPkPbA4/ZQrWaYL9troPVXAYoRJ/6mhAvAZ5WFWOduKplka85QFsI5E5B69IBWZe8nfL13EcsLxi2HRs0psnm8Lihf5K7FsfZGEdom5+bLpr+ZitZAaGRyUWA9eSfVQe3Xe5PDc3KNhn/0jKbOd8AmR5uGJDYz1R4S8nzE0TgK8aQajc0n+Sz0tjlcMSROf8nT8ghnrIkQu7RSIbq3pmY8cjKhKp4TDdKByagFw+36UDu3SpWduwEL/zgRhZ/MQP+DPrwEdWpD65r60O6VAONnd4VsW4vTWymolBIBH1quvb8QYmXAKWKhrD8RBmDaDKar628DMg3oOT55hBfRwMoWow1wkv64CFUXcyngCm5GN2xIaBFEU2UAsqgOmsDrvjXd4gRgU9bINjNpQHpQFXqZCqrd9doaxbKn8U6Y4mVom2VSKhygJMW+xqINLO4x571mJ3Cncrqa9r9OblWKsenN2G3k0V61DtRPW25G0Bnup/GRoF4eYPjT2+EoxalGOu5jSNxUjtknTBoo8dmJz1MrCNzBp33Frl4DaMJDsu4ylv7Oi148Clk0+Q2Oj6B70hgSqS1oHrAHSqv+R7Gbfyhj7Rpui+SQLqe9TDf4PFuzHzrUbKJE2+uEab4XY4hJkwINk4BmyzO4G70DeLzxE0rQE7K3EXkrlg3T5vCSmujIGXkfkdbNrHIHRavlptAeaCvf8BcH8u8lWolPshOnHSrjmYxtF/Zb5dKqTV4PksATExEvMHETy3phrbTcoGXk4vuv2Gyp0gfm+dLpc5KxII+zgo4GepmfNsyaA97PzHQ0Z7rPEuJuW2nHW1TNCq3+4Fzd9UXvngfFsrz5fvFskHceJ8I42qMz8oQxjzky+sLnjv+ljIdwh46qunhq8WGyFykRTkbihbIWPe9tXMDtinOrzc9IzbtoDYZz5Jmbg8QATH5sDZIETU9/eHzTPudLbOh74nWnkKFrv2SuCucYvJ5Lt8eRni8r+f1lkL/dAXZKNyBHDPD5Ip1KRtnA2BGnPzm74/gUz5KU4pe1ymrh0EixP/4qn0m8E3iKbgd26r5eFPqgWF3NT+1Z/rFJ+vdCzyb6nZrbAf5CZHWzugj5N+XEyHJkU/1T1NYwbt6twxe3d4xbYCEFci3tGrF4PvRc36FntA2jh+qQK3OduYPN36JygN40bBmKwZvC40Qp+J0m9mjfdAJJW07mWKOjSZXhPIwWlH0go1kjOhcqAZ0pch7gR7IdngwNCMhktiEpfbn/1q/wa1b2KYc/GndWOPgZhVwawngsUzAfuyqDmiZFZak+xEkHm24XRLvKd83kCj6wTj9aeFM2Lq9wKusvkxGUy1AS4N1Rezjh8/HFdMtDBF4JS/pWLCZKl1SbBloFfI04eolaw3acYbAdzIpfHEp2E4iRYLHscgt5pu61owHxeD+iHgEp+ZMbvuuI1vnRCyN5NJF7JqL4hrBkLAGoGyuxh63XBKgdVug6ueDU683EpzMw1wGtwpc1KhiqMhHm1A7mMXnU0YaLQ8zhAES5xf3ccFfIvLtTG89k66WvyUJ+rrVP3m0FWJ5U0VtmWN2PfzY9rvxYkGRXXWAoN9ktSMEUy+vhkK1WTLGRUeT9TXNg0GfsqT1HE7Y5r9NUbc7H+J4KY5ynxTWbaurCw5NDXha7TdLPLm13MtAoQ3Cs4iN/OiEg56SIlkjpmDyB3A7ZdDZGVMutl4jeqX/S1A/1iE2PzU+oV0osXJaxgfmm7xTos+O7oUkrOR0h43xN2/8eFS1xP/va8Nunxm5zbGPue+L2OQQLyjKm/0eSGTY1TgjTTYscSLmscjb7lZ+/rYwwVmy96NYBcs+Y5YWySJcICIretJ4S4b7X3PTVKCIw/Hrswmb6i5Yr1nT+osutUGIk8zASUfd+lUaWgmz+utAN0hSwBydkHfsiBDfL5sG3BA6ZKtefnbyd3Huj7Vx5CchPOuJeqcm/+QeEYKbLehgLUt7AvxLURwkU2RBmCcJa81NaMwwQCRKRyRCx/JaLu1RQVqJZmXzc1OlFV9KGXzCkS7eVlm+FYMHjRR+mV59RH7YbXzgsnHgB+HtSRv6fv7C0v7rE6t275l2Geqd7s/skNg9yC1hvNIPLF+7YU9YC99Fpdr27JYq+JpixIClUuwX2KegW3pCA7n5+prJXjBnWI7OQwldWZravu+INbkpqFGXK5eIjz1F/LK9/W2jZPeTrs0zldfuZJV7NYnYTicEw7/HJCxo4SZzCLBAZ2X7UnZDvS8CE8tJ961q843sKIoKq8ldKx3pbpHai1A5cIGe/bvuGfxs+gUgUfM42zPBQeReFE62j53a2a83hVUj8OLN2UOppTX4BFxaNRR0p49m6OSRE4JPaGHdZuMbPVHVybDfSzjyksOgdRmM1RuOo7pnAlsiWinCMyxQqWcnKaq2HYUUYehKCLVvOqIi3a92wdthnZrGg5SFzk8f5IbvYT4NjnS9gbr2J4EF1CfJxmmsvP5cEPiI7t/sQaMqF8DbURZqVndBYM3Ky5AnO9nmheE4TyB2Mf2GSP+W4O3NYw8EdC0ZVNo1nvVkeaKJNqebTz7CKRQ/u0oMBm42yFj43LyXpfyOoqW4DxDV0RlDnDtaWZPPJWVbJosLsf6bKzg2fUhRupr4aFtFyCgl4kFMgNvY3S1YISDXATynWGT7HAt3DCbJpvWjFZAgt/WH5Qa7Fqz5v+YKz3Kb4tMJRJZbhYyndBmsRTDg4ga2eNV6NqW8k54n2MZGqYckoRW2XFFeKpCxmXmgkWkOavzwVN+pUS2hdOIO4EN0dIiIDvjyVo/UOZ02V5nta9vwL1RKPfsDT8QizD9UacGzfQ7YHxRMt9cJeX7/1JSC3L4VTrv7R2gR4s64L4ChcLh2y18Hii1J2cUobRSjBbaCN939GxRdDYTerLuIArdIO7GYI+/A8dQsiMih5YkIFM0qlXRZgW9u6JopdWRaQkdbRi/vyURCLGstxufJ06rQVNPwKkhXKTJOqJmiCvSt6peicAK0ga+OAdjsIc7QMKIFz5HWBagjgBwO86q6Ysz2BnXt7FTmZ3mjy8xZCEffd2SVlOTtTa6BYrpKZlb99B1kr8y2JyB+0LsRVDun/n42sRF5YUCN72cYxKa8TZZKbb9xd2H5ts5E+O+wAPdoH5jSQt3fwSKR4GuEoXQEPMmNBhw/iV6Rb7Df2Ji1t8y5VmNtmdbss3GLtKMa/RxkayESOcBn2QyVo7WytIRpM7FpyI2evcOQRKQwRvQeJssmOenYz0jYNqo7P6zmqRZvZwxvX7cirhZCnHy8vqKdyXglAzQ9g6ibBGLEQKXQ8RhlHQ6AmuhiwqBLzrrzAk/uOFGEc2EaV6QTcvsxoBazrOzM2hlv3qly08J83o3Z9OU9Ywph1btWHKkl4/IE2C0nLFxpoLBYb6CCaYy8Ct3n5mB0jrmGwMTHUzU1+xxGKtrBQeT9TrjQZiDZMCpmUpUTRdz8fVux4ea7127jWX58HtkwNqAnfpHdcUCawANXQtWISQ2qHls3Qqft0h5l5wnRFpwK+YJA6MdKqZrk3ozoEaOGVsPZADb9IrxnO5HymJYgTCIRvUS7fke4r3j3VVpAR0YuAb3DrzjcWqP7xcEzzvu50C1ZmhYWyuIcdJTXv5jAECTFALRASB8GtbbS4Rjr1K3N75wQlLAMxqeejclyqcVNdvL6DS7A7cccM1lNgwtLkEEAlNFRx0NpiJGZlsJflq/wod1MvaQbE2RfqO2e8J0M3jzSlox3NxM/oFsDAvHBqo0frEDEEfGztNdm/eISdSvDzstq/kGWpgwsbwG7jv6De84TM1rIaXaUWdVmL36OaGiOOENP/8yQnnF+gb372Jna0HHoqg2r/eMkaC4EudgXX++cKEKqnhSuhlGvYLrc6750L3zSyY+RkkcFw7hF9BPCZqESy8rQWfzQjzXAli+JkDRL/fweH+WrJJH45VuuiosEVIpyfGu39lSDXidHM4Kw3jC7bhsFBWZ4PT1x+BTLUGnXDOpIjBu6Ib7MfcPaoJuqzudP9F64up35FppdqjW0rZulorFwi1h/oh6CbARfPRo04eZNeSE3Oook79YpbyFYXuBXn/7PXsjAJZWsMVdr+iPKTwwCxKXa0Oha+Sg+4l2Eg0KErlCZtlqfBbOisUqJudXUS9fhS/2bcKUyQuwO+URocCdKKrU6k1T8OjTGM4d9DkDzt8OtLwEAMvSLwdVY0gr5xZ6r9VuEqNvsIudsx8wLFbhC+0NCbpZ51DkUtxtph6JlCj6es35QXSzNaN3sZ8JRucURnNR53u+w/d9klbpnZ/7zUSnNX0C5d/aV2jJHsFvJQVCXLIrJdvjeZBtav0TxOhm9VbJSu9Kjh0788wIEwfRK7Ydbg2NFiWcsMUKeU3inFMjHBLz2xvgMpxPT2LpDpnA7jwwazVQrNo39ew22/PZJylte3oC//akoFZxmVRN3vO41XizaovjRNU6BV+61ksRc4TfxdsLvwm2tYV90yjA+Nu0XDV6b/VHwOsqEUNkngAszW+fco5XgubWQMI0mNPf/PRqm9kqjzE9zKW3DQP+8jDohi8pAAapJ84dUvxiBYL3fDc3qQRk47uuJ3jN+sVgS8ekBcl8gJkoP3ujMwDTuO8tc8SffUAJctX0Acd3z3hX+PCr5NpFiURFBEGsYmRwyap3kw619+9KW7duAR1dTfqVsoT4sP4Yu0rMcdK+igbXeoX0kkSSM6iZh7NIKr2vtQvoHwg99R75qdcv0gzY14qQi9+Yj4gApdQr8pVC/QB08Bw9L8my72qx+IzdG47dYiSqZ2Vx1/8dn158saJcmujkgkyhDS1nYAfCYdlvccWImJvrdbaWNUylnfsEiurvEKDv9IssJs8SQKiW3eCyrOG+IOqaSTAJ46oYYKoH1pZpkthfy8mapx8GHT3Dc/6vSL68LfG6r6ymQ1pd69sTtgAzCyM/Ccugbz3zkQw6+dgmL9eFqdb8l8N/FJoPvi6LrET7okrp9nw4PjZKqRyyiNqKfVbJtWzY+hA70dzhBBm486ofp2MLxa5Y+ehOeW5XGTwRmgRTxy0mpIQnBLAY0cYKOxGT8lO1jaffiLcNlGsBs1FoJpnzx0oKuluKBuajR3ifP3AemV4J/kmVy8F2G/9IDW0UFWovLj1LwJ4XTUW5Gw+80wDvhslVi3CmJeQgKMmZykVWSPI5eb15T1KyFZaZjYzS8pHvV8R+tzHfmdYk7dWwRu2p9uvpZPup2Kd6POeyUvP1EBl69eNjxGM+zuwgq0F1mvyy7TKNagsyLuSfbd2gQ2BjkI5JMHNqVGG7SbL+C+9VIAPeZCjHsVjKfkUgGh/38siNmXf54XWDjd69xzYOEXIGNgWlnu8zFHMwJGjUOYym6rNiF1tLrRoAJeXMjvqigicLH3vSjU/Nkw/vlYeYf3hzePqccPcjzvADa45U+WTLXQucOmQGPu5LD8hsyHGJ+CGDrXRKm0l7zetNM+6Eq78UuBgf+AhmruZBbCq2/2EsQaMxK+75aFpBp68eJrVI7pmSn9vv4/DXLC13OV6aCe6y5O9SCDgUJTEjhl2BFOzDsn2YKMpU7XeG11hqnK95eTENBHFbc4mYskDziStNLS/FdRu/mN6CRY/eo3OMrY9rSuWMKbEa4iC3iMhc+PgZol9Zgf266YhBIg4XUvFtU9aLqMlWevCHIUtkoBfHZnDMJ3pApYv8pw1Te4d5fd9aknNI1gCOmHCdwJGJe6RjqEgkt1k04DY80xz/Ft4JxVAGfOz/LBU8+4vTTknpd/SAIVZuwkFAqjJNV8G4BBUbfFwR2bIW8ilwgq+/HFKzK7wqtl3/LESONM7cpMkBd85/bNuA0pzG8i1g0w6W6B/4AJ6Eu13WuJwcfI1yAwJoobG66lNfBkCmoScK1GDvi2Y9tc97RQpnRzBLZhf8zkT7rIPribBxa8Mh7+NdwAjLFrSQr5UZxgUb5nJyQtZ1D/rGPIKIeIujyeXeKnijlPREqFrgy5typTNAmzGzjxl3EVT7lajd35sb6vRs15Vvbu++HyI8Uuk1W8VU12UcnEfd6h9gfvXUbyxD8JBszsiSLJrI1wugiljQtztJxa8p1P9fDOW9tIqtP85fh3zN4FLESNQ9yNkEQomgpov9A4DnWq1KnuYHP/zJen/Axx3mQemoF/ze4oiwrN5Stik8ePc6BmNz2kAP8i/gY2k/T1eoNMSC5hgeovp/X2HnBZQXf2ej9M+Zcr/3i4H/kdfzuy5AwjKGqqlWsHqvwcbG5nx3UVFsAXavlHD3YioSxcEscbsMAR1pG6H4ygrQKv5If77QkzdoJAE2H+ql11iBvky7SnhujsUaLWsj3a8pG1yl4r72T7KZSuUuB93Fdw0QqL3wEeO7XMDJ+Z17UwRAVFirncF/BuYH/tHF9T66+Vk+pHbf3KdkRhBme+aqWkl+lNkzryYd72AXjUm3phTgsukpzDXlmVkVSb5LQWH/DEE4GNW9o39kGFJ/ZkMR8jxEV8Ott9FdMdUlJpUT38o0aB5zog4t5bXNTdXuEZmxsD4kQ8OoYAf+NVF3Vm/Quj96kdtneSR7CAKRNhWkQ+XgS8jxmuAM+yplEV0pzEqggVvBO4Dth3GgbYrBbhwJ/nBWn3TIoQsQtrSUCicHlG4r98d3/RCrU4z+txiyJZJ8+UOkYqgXcU9I+Q1ZvYJkbdAlrXjMkkyjbFV/82l5hOA4q1hdaaq4ivBvY/FShH4sjlYZtYn+FcRDaPQoKruWrgpUHvHgLu3Sug1luyBFbjkvJ40jf4wOtKEbQ2oMDfncSuv8H95aGQYckPL2ni3sXjdSY27dLm4xPp/+HhS3iI08gD1sXL46XtmKZKxX+/y12jzV1khNHEevt/2q/i8mHsdUlgkfYOglB+zrwUxmvFMjZ4JYghFpgjdSppJfn00kEaHhreBGsuDBUCbT8UPU2u/2yggxTykvXETuMXHqN+JI5iFLnQXTgjgQaNrPUdJErB0z7xDIli7hfTVot0Yr9MeHkvSFj8NaUbqs0XVK135VH4XKjm6uUOsQb+BzZOzJDETac5CcS/ml5Jw6ndYaMScfo0wlYwHYZLKT3OLZs+ZUyVAAMAiKwbN2qjW+deeQKz5UpJ0vZvkZSLLIBq3g+/Yem8b5fP8cE3ojVMAO+kJDomMyuSIVrSmN9ws5uxKVeRYdqOopSORu1AVPZw98PXPgitfRjRQlGRTBuJpU9WyjJ/2Xat3H1HJY8Y42Wcr7+uvAMtSAkBYMn6bObKziE7P+qMb9v6HncG78Ucb7dkt9lhmcEJwa4QHHfXR00RyqfHVqxxbHittpP1YsbRTiufi5Y7vugArO2CXXLR2kiq0t3y8RNb57WJKnjGHlc1ASo4J/ASFq2gcYjBArUkRM5GDtcGL5vmPyJeGh8acgcj+f7ZuJfxor6NYoGWcOJvNW5jb2KL4Lc0A1vjTMR91WdPYvGzUvEGkI2/kMDVdQ2B4YKiiTiJkq721lcht93dhxN/Fi9ikbQZdIMKjgI+Dg4TzmQkgtPb6wQ/kaGLKAfaeW128crfRCnnFnDB6fPm3gtqgWybcm2qYRqxzeCEMveKfJUQK1quO+AYJSpI44F+wBrW3XvDJPSr4Cay2goV/r+KYGgpTTkqa41Nf9FWd00Tn9EKdf/QsyZ6ZpZUi6T6iPmx8gBEqkKOk0hZNdG3PDLSvXmDgVQFPVSnx3V+UhcsTiMQTSV1MyscdkxxPoEIxI9rRqK5Vgz0yhP11j6C58dvVgnYpxWanXQXMf+OwxLQxKZJp5hU2Z5P7kLa6KRN1maVoloYffW5XR8I/3BkuvdSmpmk5s/tTDFht7Vir+26uwFJS2swjQ31vkaYnNf5Py8jJtHikhMvvu89lluP/Ynk1w5vWdPtCfp6taX1xK+MasfqZxt3Gb/AICssWwtE7CzEluinBDdMfXYP1jVdC+vVXUcsD800EWWLt8vG2YM82q1Ok54pcL0HA6bCPdKlK4uqxp44kq+9pNkkj0YfPL/ZEUY7dP1x95UVU3Qbtguv7cFMlpXMXGN/FYTKKYhe8080f50xpyjU+8ZqtC2+opwlUgv9yXOtcFkB2xSRcp42/wPppaJbwYrRxNzarMv9FhEhGSxuhpcQaLLLtKZVRSc9Bg83Y8cHqNv9Zz3NRWvdvjFYTM6j3vUcEf+xsM+qTuU+WlKXaba2C93nc28sQiHsrcVr/RZpDiPbOoQgqae7x6lE6ttnQaIpW0PlekB6HclkwPnwtE+HQrbmSvULq/ntPft6b/hwKGCl0t26wPUp65ibjxC6roJmG8Ll421lnLO3mb15Yv9qFdMYGUc8VYuFvqjvBVxKb/nQJbMIBmJiJYIMLFYEUlVr2QitnnjxL7tYYWmwXUmHvgugXn04pbVcAKlFEfXgLGy+3N9GTRT4e2rqQy6ExZuknF3t7UR0wcKXmMJeFdKTzi7opMC/O8ceqJEdciL+azMJU2negv6aobc5w7fhersdLx52O/cxl/3YHe5TpGc4GMZWhe+CSjgDExtuVgADnOXMV2kPpQZlQTr4FtbhKw/4ea34pprz4MniCGPxFcecvHSJCMj7tYBCakWJXQZ4KS21mWuG7CmMEpa3w5vPnTMk/ue+6dXAyqMLkgSrovqq5s4JbZ86KQsA9YdcFCwuHwq3vcn5u/jEJMpcY17n2/8/H0w0taUqJuu0+FlrFGT+5iVtK1KqsAoOuKdlvNOOCMjghZc2S2ZeRmwfSBLz4UEZdkJjSth5+cJjWu/mOMSbk+TawMuPvTF8toa2BXD4EieebwY6pY786KWHbvLYVrYCB6eUHrY92G7A0xfkRTdY/iIW5uH+byIaxVqU5bjTS3x9B1Z8hlxs+/b2yncnp0/E/tO8yG6YPk9QSEbAt+5Ecua1NQgsEay7+3eeQeIiwdnsn7NO6CkANiqgqgbEXbhsSSw3RP2Y9Fck3CqLfFz4F+IKqs7HM1gsg6f75kFrun2U0x2oTN267HbHQ7pfUKe8295tWS/2goJWkqjuadxG8CmEtY2HnH3l12ggsmVd0toex+lWhmhbKE5ilqSyDajJ88Fe/gkoy4hvLufXg05PXi+BP8Q6WLcaWAR9REGJXxh05Z2QdALP3UbuCpnDlcZnOPzV+O86wz4klOtLiKhRcwfm3JLnGL/0hTlvJdWYtitj5zbDQaa8jpjMRlpijYVS1BUn5qADYfMOWXC23MkTdmw6XJ9f7o/w3bnM5ojjDDUFqHGYk/kxHZ5QzmuJ7gqBDG2Husau8SqVtjwcNM+YtmuRlLgwvAyIZqTNmaDyX4LMEEV1jM1GOIalvnIqgAKGl1ptsrC66milMWjzXczOUdMeW/oUnrH4xlhbw39mvwHadeVWHGeOXf3jtcEbxvG2nXvjVt6wcXJMox/o7yk+AYGs0c8Q/71GIENW+5Z9/gQ6X3D+mLJdQMd1kvjcSdP2V/wJVRGhDFfvtFBPB0dP5dfEjYZjUewOUy6cJJRfHj9lnSUl+VZ8YidRACZHrUnxLilnlN5NG/fDk66KsruTOAjhaNGvfnGn9KJimB6XvhV+9mGI5S40V62A6JMDwYHexZarlX1l1G894A4Icl9nXX4IwHRhpYYcTYVHIzkMgy8G/K6v812hWfU1YQHdiRldj1yeP1/Vnl+7i73CxMgUmdsRtRqeltm9a6LfW1idTl7JCDaP63MM4TAiQFblUpQRziOhjGgSnQjTu+kwlVi+eE1pERUMrVgEYkd5QysSByP01v7wNALewxl2nimJDNsVRiD+jF8lyF6ICj+GcyzGZUQUS7MU1IJ5ZAbHqIbBkpVVIzXBfQDff+JI4/dnzB78CQ5x7bsj7koLr+Hu3IZEfIhVZS0Oo5l+hmlEgjeMyENgf7YoR92v8yPhWt3KGeUXJjy/U9VwRUBP7QFc4zbQeQaFgUmtRkOp6DxLqcqYjRNh98RNPShO0s4tuUvf4j1UleEpM81l8BtVu9nYzUUK3QUCiD2lMOAzwvAU9arv2/3y65j9GZn/pAklxWd1JJebRiQWMA/TOpSwQAGHoF0mvSMKXbMhaQ7zvt/AsUU1eeV4kGEPtFldi60E0vN+K0ZK5v0+2/Gx6uaPyl6X0t79ZD2FdTrkjIOS9ByAKmiw2u7Yfwyyg6oBQvWf5lFHSUg2p7Pi9Lw04RgWTfkDR8C6K35TI2bf6LahBzQNFHL7iP+SXrqOtXPWx44gFoiEmsQ85e6loEJWt+ek0Y1TkJ2z/CWyNTQh8fKeUhfNbjB/4RUM68Hz0B9txyeoo1eqNrJirikC4mSFw713goobgWV/ycLHwfleBLp9peLQu9onoZTMlNlqFa4rpvmhUd0i7DKrIwAhmovy5bRAE+rhJ8uymyjRyjjvNpqHfv6ZquThGIPPgaez/uSqMXkyFB8Y4ruQ55mVDfk3sWrq/jp1APAgMSK7heJhb7Po1lribaFLeKxpdxCw82b1ARSIy9kkb+HNoDRmmqLigv2V0I5mH/oOWWpsxw3tTtWugI0ahnYNANwu79AI9js5uqOC7MgonpqbynVwiZXaZmoNuscUWsa9DXOhSg3dXbbtEA3t+Et/ewhtGvYxv1v9Zv0TkvCsE86ET4Nkj4M+CH0BeE4s77Mp4+f6EFwbY5vS+SraqQQ3pVsfS0z/rXs54QipT4oMw+GJMNKaOO5Lfe1btmBMig7d01ivsLflHD5ICcKk3OOwU3nElinK+wPptO4uUXzdy3v5JZnkanYCggyQNkX/yqkw6N2d4OY0uxd2KEXwmMELCucqPIua3Ih8hiJAGmeC4yTFb1+8b0t87XXU4ktZC0ns8N873foeJid4IDxNMF+uLXqkJ+0r8psUmgPEQbR7TBRpqi73hHNv93xHrrIeCRp5eO4NuCR41XWLODFxpFOYYXjk+z8LllReneJXf2/NP9AOIQgyo9XtFZ/6xNvv9q2XUhF6AOUzvWSZi+M1hrrjEvW5+fB/vlS2nCmX+QlFPG1CeMxu+RtbXS59uLsME/l7xKHu1bvsdTH0+07n/DgvzlN2jObDOzd3N8oFVZ185UbqB1+fydY4bRtHMrlQaZ3QLQSIdye1LVCeNiKHIiy9680iapQCWWdk/nIwT5Bo4IACyMCYbD9ZevVyPY3PCTneM9RCly7mkM5lQme5d12OohGsD0WTj/e6qELhzqBfb/NNMjMVvF1u8N5VWn1jD2whk3fV7V2M4LyrX+VVFX0hGFGUnCvvEwt0tCvzVuG4AAum+ihWwKsKaH05wCfRA6DDnooWtZ1ZtrMBWFaUxUiTW3ekz+apl/Q96yhjXffiz0yDL37JEthKqfUPRbtGnegcpUeW6sWyizbNtS1QxjUUpsU5yisJuP/dKMfvjAv3Tz4baz0jWcwKFrD0Yisyu0yrzjs731W1TsTDd//K6TYC+FOn10U6uhJZWOxTwp56tLqQMyMRWfw+peFbyBWU6eOGb5OBzqmmraO5FYaSEpWMdrvIVnr3VEEExjtSW8tbU+6ibzgA746kYVEWY9bBZKNOtRMrznIvpPxQEFatV2yoUuYXP9dMgsefjdJWv8tkXiav/qBT0dR/x6c+9B8BtLXAnACaw8qV4k6Hc5DkQotie1RREtH1ZyMCmf/5cG0ekuz2OIxX/BcnwJ8VWHSQej3ldZqQ/x6cea2s978L45eLbzWCir+5vIvmvVuZyQ/+IxB2NS1eTcMcWLhja6pcKP6Q4o1KC5Xfr12ynQQsfE5o8cdUJdlRBqTeyxzjWONqWbCdFNNoFEz/oY3DIfJxfM1kraVM8DcG5tehE/6L81g0bSLpL6Mbi8X8ZuXXPZMXh3l/FpO5PzGzNzl0ZZYmTR5v7nP5MewSbAfqgtNWUCiLr+Td60w+xUQ595T3Zy6jUJR0oSH6tIV5/4KUiBdQ2l4OP1f7yGo2tYhbhs5bqLBmoXfyT1Fe5ZtTvSq05qnl8j3jPhzzeajvUL+1grkZJ0vyBZy7uWpnEILb6MHdmMmt3Il4SjeTEyjsOIsdVnORF8yfT4pitC6koT/mLeEK0sSZs9qdZOt03C5zD0VZaR8euIW3ovDFtEQ4hI1aNfx5jgF5NulM2Xzdel0Yqx4Y9M9+pTn6D0lPXQlbiACfxwF05bJ495GahmV7E3/HjLGmJ3PQhZXMyroqa6wIe9m7646zFhx+ILGGtFOphJvo5NiUAjU3OvLYc2ETra+I7T4xNYYfgauVIUuaGOYRwtjLZsxU2qKTLA/Y7l90Ph3jPwiZs76Bpwxn/cZN638PeZ/t65FuBCiB9jgSFhfJPqwlJUf3UqZ3IQwtBY3n1h0Q8IwUjwb8JwpaS1Pr+A7jjhy82vSnt9fZ0aq1GEYCig6MJwYxkjlEkBv+x1vqhk7TbCa1s+5ja8oEHPwIqcyTXHcEMDpIeYhbh9e9kGkblku6wU/eDu7R+1YEEL+lSz0E/hvPhszR/UahOfEgAOW1ag/9Kn9x26nivrvJ269vGOik9gGElsJ4RAT1MNn7dtPsNHPPDlkWuDZZK4f0xc5RPteT3LvIIXm5Bv2GMuIOkVwomm2FroxWWWci1dB3iyT1hNVjM8MUswuGjsHxekj+Cj7QRFnFuqC7UW+cwbGUiTA9gvpGIzokCoHKf721IWY0mS/mh3JZb5W5GNzO0VRWII5fW56LDs0enFcqUE/JLtsgusYChda4ZIzlzvJr8hjU7CfKU/NFi80A1ZoYQ9o97S7OCMPjWMDTlE4joeXhiBdH+uI0cd4njErb5LdICsZylvBUxmaZE+/HKCxICJz28Jgx7zLNUHXc4XTZDRJdaYe1+BPpdk5A+o17pDmz2hkKW22Bf0DffCw+QCNEZBj25ykrglTc19yNq4wwyAk49+FUC1El6g+LZEKCb3n595YJPSh3k6Po6w27M3EJcWlNvBPpAk+1oNVyfrHNZVIK+pP+ZYK3GsNxQtlofRT2xhus/RkbvX2UK5BOz5FkcRObNOrhaeuzoiZCw1ZR34EmrbVojqNLxSIHGJSg3eK+Chr9yAOh8SqVhoiJ3flmWYwYre59petCuw71oCj/K07K4Qwp6wUWOdvC54Rkwlg6jaudMsxSGqmACR3Rg4uZfkA5hbilsfeusyUwn//c1cSnd2iqNB/MMeVSyUmM3DVrbnfnIES2rkh/6YRNVCk+iAxcLyjw+HX5RNX8ue5+8Oxxki5Y1STACO+9MRQHAlskePosOy4jhEvUYtMpAf+PreORBFYSwQG+yY1pLIEk72X/c0z8M9Gz1zfnh+ibeM1zDgIQRLzOt23uCeeW5U0XQe50FeDgyB/r/QIch1/pXZXCo0txUR8ytWVfV7kyxp+ScZPYiG8rAT5Rkhv6pvci8x4g4fyGhV56IbBnCr7dvypmSK9OvdiVpq5Z2Ykstgibmk0r3p136QVSX+DLRGVHPyyxXtgd3Fh7RXughZFsZ/MNci9Aj9X/MtO1uVQqd2uM7m6cAwutfNgnBFDLEwHU/WSb6MZQhSC/D3RwO4hA0stp0yY0emqzF+kb5JsZf0uiuVhxOKfcuS7VYPsbXB/8aZvjICEX2zw7f30YME2WzQWtinzTa3N5RsTNjuluyBVK/GB+VYBnBvs3lvy8G3vYKvTpaCatCbO8B8ZnTCNeCMGdAJ+jebw5o5ZVoX/RsP5kyCyaQyolBs6DfO/6Ckdx754prsT8eOLtJU78OSK/p7971t2/3uIwLpD6nHrVe6zO77KbsKJJwIWyu1oCT1rezH6VReJr8sy+xY7EyKUdVEAN3qBi+euoRpB5/YV2FmW+/aKvAtnkoYEDnp2j6t6hObjzDIz4iDBhJ4CEv+Al++U0C9EHpMTPRX9dcFUQ8FlSoUdTTm6Zps234FgFTC/h8uPJDZjbH0C9m1gMWdMRhc/tQec1P+JmNSmvUg0smSGplCZ/PM/iEOLA9MWaEZIwa1GG5XRbTu+S/99y8LV0lE2S5DswTarl7IHGvN/HVapi6u7It1ym1rnwt62AT51R+1GlUO9Hz78yiA17A8wt26VX0RuE3fz8jhVCxNTRzAnBYF/oSsMrEGp0gNvS9IhReQnyt3Yp3x7nfKDORghmym8uNqH5gp7F8jSdR9bDNDRPc90+zyNzSeECSHMscVjIvfV0i8S7JbMibg9HIyExVBjwDifjm/8xXFzZJL5PpLyzl94GYhwo03/DWXqj1o1MbMOp+PimNc2Ilw7uEoLPwJJyF+YGaOWBC3KPBch6Kd5avlBKLZmIZ1D4+R2+tBjdpEVHHgZLIOJW77HHPiBddQkMvgqHB8vViYqP1153W6N2QSFUgKuMshxqUgeUtmLYpIE/qTArlSHeXLjagvT635e/aUGuNid5h8Hxyy1sQITECqPHEWA+sH6ML+99lupzs3MnSwIKtHkcF+HpNciCgPbOhNCfDwKLKWETLdbT5gHGZ1dWS7xjuDKmnrausg1mH1seCXsxHhTy6DFO49VoQrkzZio0E2k0dq2b+Wx7YMIAa9zQEajlLauXxHuPNveNktRROC2A3QViwR/NfJw0E9PdWgfhlsAkYJ7A8Ffdw5G5c8DbO+2MCa6P/3sFPBcrPlGmeNNLNYf3OkRgez3wFParGibjlMUDId+qUD5KJCzpUJF73OZj0jEMOa8+HwkLd9pMtuzO4DMcRSTV1oKUqGnjWX/AIpGPgzba5Yyz4L5cHq/aqMT/3zIu694EL9tAZBMIOb7HktdTCK/0W1ZnLAN0W1eoOZ7AblXBSuhpbbb4I+iHLU1ueShIJ/D/yiHG1YtrslDz9oiujmZBhVSTM2qpO8qrHero603vK+wiopyaL1FcowAMqxZ2bmJLtzYfCrORRMwLIrB+yuWxjBfDrWDEIoXfGgxZIjjVmMIwHRCVkJAX4fB3HZK0hTBlKVFFJNJ6PSzC4/pVU4jqvXcFe5icd1xycF792xXd0uC//7BrqyKP/wDjOPxT4r788C8L8/MxrJ3QtDDGPkCXrnz/EvDN1gNtLkyULOXhPnWGY5V+bGNJTm2XdPSiZ0a/WezE9/9LWaJvqzS1g7oZTZgG2toYOdL2Od32Pid8Jdaegef9wxagF/8ElFR6slT1j2iLGg9IFHHqkQU6XgbI4YKiVHxNFvaKZJTrSzNQf9eb+IgozcW2K+C6qJa//jwnTBep+PnCn8O+J4dT5AdF+A5P6BdxcMl/Gnq8UOvhuBpR0efNYpzGIP0TjPVoCgFMf3YuPLRKmPFIEubuZbo3AfAV3IkPdGufnZHu+jHVxwnMqbX2n68aJGJuMu0BLmrLguRGa/O6kNb1e6Mh7jTsFIaBqSx6qXTYnruSPL7LJ+1qVthhBMHj9sukKiA1sMRg44/CZ+BRT4yCBDe/+OE910S2+PKQbr+AKZfr8YGthzI5Y6r8oFBNJaiApOhHj18dGdjX9/F2yRjETxyQ9ECMEAKhtw5oiPUR5rFXY9X0paDPWyramhfZvRX7McSvDzlCtPhMGs6+L8JsiA3uitQH0a1ShCOXYk/bOlVa6O1PrDknemFRozKYbJODWeNwhZSfEEAreujEvIfhmNpiWJJ4aFUUQL129DWutDCtsfkZ37VBdpp6HGQnOQCmtDzVMlkDksbuDbA8LyC3h15+4pDx7N1WN+tWqxq1oqzlr3s5D7egnO716jBnGN5wSSw4XuAP5t725EBdoV/Zp28nc46IYRHjtCSJzdoBJw3/9am4OPnc2jlnSztj/hNlWWBkLAP4tA+yMazliGWIRtHF1ZH9O+WHbjxm2CFU49+EX0M2E08rw+wJ4RN+u3pxaOmTn6ZMqTvwE7Tm9Jq3nDXsBIMQ4G4qkyFB/tq8e4Pcbfinsoz1lkpuatChSLvRB0SYOcOGZgLtBCcoPl0MFWvnoMcphxpX8KbG4fmP6ZB0QGCm+TRpwg0ktQPSwowAb13EUmy0/1quPk0ZUFunJQ034NnQiyNFpldaDoZ1dAABrpkNS/NhZTuRCR1GF/pA5h5bU4ZD91xO70wlmqd1mwa2pqdJmGB6OCLG0JU5cfJIi6P8W9Iifr9HvrSv0gSMnTFDT+7sUaSNxvBAbeIVGKVr5QVs/RuzpiYIWPSgCbclwqPRq/xp3qTCfxKSW5mslyt4rYeW4rJ4c3yOoit/61VUVveT/zW9uAq8TqPR09CGLCX7/Pvd4R7oguZ7vmcLN2CtxvMiertdSqtiW/MyfjGPgRYQQIsVoHiCSQAWoxWd+ZRfDBsjn9+iZ4yALkIN2Yq/RVPb5cfFMqUYAHShDb0lEITEen3NE9Xj9fm0vOhw1fiTBiLmxaKAdxeqxFbsk4sCY6l5HhUAV4a/BsbcdxrYxlsjP7vOq8UduOG/DmFJgSY5EDrid+PhJO4pP5rVKU5QqGd1ItyzEsqWyOUXaGqzNPWQI2GA0e1P+FSsc6KI49m+cLeLSdBw22TrpyX+fwNVMiAIKFTuKSq+QltO9O7pwJfwuVfL51jft3x7biEdd33kxUMzPAjhyOXZFiTuB+AiLqovjQqT1vz0mBbqd3WYg2RzFBY44iE0x7y1CA0yA2+1SGGjApt/iHtFepBGRqZBXNwiRf9bcgTsYLbF23QDnvlDHVZBRKQRnGS7xYgNkcEI0ulBAGy61tDGdWXmoyL/eMFc4AmZ93kfIYBIky9S1NT7u56vjezUVWduFs+a4wPvOLQuWPN5F7XTMEGDUsIXmftOodxzp3m5VLOiD6lCs1jq+7xkyCs/TIi3RERAhhBfg+Zzh4J7Tg1tOXfM3bV45gIk7dET0SwnJCShV8iZvSeicH8l8H8XCYdYUN5AZgtgWHdihOpM+XkPsuPVJQyJOrRPzduS7tFl3e/5ZILKDERlgZxk40UdaAlGmbxwoAn/DGYOnl1gGdOgiE3JdPmRHqpxNR/dwyXt6O8La9bcYWJxrrdfwpvWGwQEJ+f9Dc151jN4Z1wKRs7vDCeaGtVfPNtPw3PKcH8JtDWM3PHX8iMfFdB/4BLFfvVMis5B9E4DJ/YXAf/WYQwCTmWvPEePYKK8eLA8S9xJyeHWwMxC+iiZ/Uw1DXuBfjL4hrsfQ0J6Btmql6pZfAEgbsRbNjPThDeX4a0KiDzrKGjSuZ0KFunJPpRwEi9JhbWAIuuSS6WP0AL8E8pbgzy+FNzJb9w02SFX3qeJn3zAGspBwoQwVZssWMnWR9F+5P//56k9u5RiW+JPzjhG64F7ObpkuPpCNhemTau/RonPqngNPFLosflSqhh3t9OLWfNc+CDZVB0ufxnBXO1+Jka93pcoX2XBZKcbFzFvymR8GlQnQ6pFKhbKD1tzeRC18GIxGBXouEIvfV1AONjVRXXhJr1epsqjRrH/qPfztaRnYK2IOxz1L1BAKLh5qTETNCab4gmApY398RfvL9FWUYwrJjgNyRTdzU/O/ztrVkRZYgby8uHUuHzpbiwRvBduDWImHm7AUi+BhVi4/NEtmfgRpiCkpr0NJx8qk/huoSB8AMXpVqvQb+cCcaPPe9VCNdpaj5iE7GngQ658x3/CsDN1hp51V6Ea4xAlz39A0RJRAAmmTJGBiJQEzvdkaL3LMqmKLxCrTWxyTFwwYI4Cvq6ioDM4BUo3lou1SQdyjmIsYLl3aFsHKbif62B3JgdwDDQsvH8tyyo0oo+nNjjsxDFTiPXRiPZ3dlKLfTgwPxVJWUSC90vsUZsl7ql6zCCQUBNqjZofFTV13zDty/rML9Ufh3thj4GIaLk34+rteBVoXkb+iPjGWgXPHEpV4h9O0nyDYz+0afOigPYqn2FrhoJds/+Q88wYUn/HS3Gs9pji9vv3eCRiKScZ0nRVAk+e78pSphZfVR63+uKKmGXYlK0a51M8hWTbmhJzoQlOwBkxI8q9DV6OXSibHe0vz+pHXRaiAlJc8792/aTD+ZZ3zXUf4LwTUdc5mveI8tzKZXfrK7j8TvB+ffFxEso4KuyljmfWv5Ku33MCpRdny1xmUacokjKmGcaKxi6KUoOTc24eVOweresp0Xev3BN1+KnUb9HGu1ZOnIfTVZW2igp92SlPHal6afjFwZhVyHLiyLnU5G+DGmsWqi3MiRHyEDsMRX6zorcJEnYfw5DpAOYdc4J2tlfqvQEEweo0HuNOuznw7wIUkWi5PXFvS1OpI0vU0gwk5+KD7PiILHz0JamV5c9J2p4GKM3Hb7LTlihImq+NNOAN/ovRdbXnm2y1w3hgu1e0B47WZ76ukCFLd6nb20QGUsOh7z4vXajpoWZ+4HtJAlZxCfwqBHOL/lxvIle9dGTnl1S/ZZzWbHc2jtCsDL7BOVyzf77iKVrwLXgM0QcW0DLQWWjxvsIvHFSgpsb+mY5uAIwpta/95NMv4VBbL+YylJkv57wJYHCvIIsNgLzVcnQveODahCGp0L/TmI1ErIOEPNR4wSyoEh5wVIzi+NOsnzI64G0A3CczrAzemRxvwDqUl1UZT6MFmlbs9hNn0bF+uwhbiue0GID8+a7J9Xxea6hdkCoCpJP/XTO5Cy+tmlniAtmQw6GI1I3eU0B4KBO/RkZPuGGJRkpGVsIzH42YHDwTsB9/D6Bt4OLu1RkV7bozw0Rm3HQybZqxy42SxYhCstP3+foi0160vKrMVg6K9mWF0jOwT5/PrAjrAKRYNB8p8iWGzQvtKtWRYGlJShErj+/6Gl9Ypuwkxo2vBoD6hd810+C9aR71HXjaaCIbS+/9yshOJCYZ8LgoCQAt2TggebDv2hnPWN0ysHm4M4lVxfZYmY6PS3ndMrYsatfa0QvAOZY3Q/SAKkM06A4xYb/0XDu7Uij7f3RYWVEp7jrV60dNEdUc4QsbxisndetVDK7dIH9v2uGXT1EkVZzlN0xRrFeXtSv2C0DA/nqg3qmyzS7Smb9a/km6mf6cPOjbXJsylDexSMCWvLIYvBd5oEcghem70A3ADDXRK0n6tf3E6JHmj8AoDJriH5jrGf6YinkxmkiK/tgiYet6V0vrwiBh1x9CrBCXUSrnnPRThGDc9Wf4M+It6ndMS66xi8inZgqPvK5qc/b+wRWFsLdwJs3NZz8hcqeEqBp+DUN5ibXtgDTw1vJnGVO34sM3cXZCBuqY/bYAty/egsgAWXXsRk4yswUXQ49o4o5IhGwEXamghW3OHeU7zERJrO+l1E3KuvpyR8JFmoK83XlYCXUW64ZWi4Z2tKL/+Q/QAhZU0DIMcrGyZVGYvn7oVeqppf/js8hl4+9GbMKAu9U5//M4RdquQbhBSiXJkQz4cwTW4HAtRdNfDTxsctmOu9l7tJ0KdUjsIPqqAlcV6p+6ShAlSfJAR8i2XyPfEUseDeL01f0xJJp7IcEgDNKoYser3m6VLpu8O1HWB8w/7gCf9tvVa+u318ZuidB0xRkMa9KYIblyZpn+2fIyZBZHP29Lrv877SQ7EcU6krhD9FgN+Pekid1sZ4ZDPgiOpwLgqlj5Qa3uYBlP4IvT32pTKvOY7qE73V/bpNPl+jiVJfCN60/AM3IMZYOuYVHX3798NCDGJVg0bOAufSqMiHez3+46I/M93Jferf6ywfPsit4P2dqUaj4zehF/S56Mcymt85RHxi/aCLWPqJorWi6RIYGRsZz0KwS3A9iA6G/OEHGvvXFWHnVf7RIT1oy9VezqduTO1B5KRkhOyPoi3DqA6FZdkIFVOSajm47zcK8vOp7emEZGUCcwWkasTxWrv0lCyku82JojS7nxPD5M4/BMqBDwV6HuMYRxxH77M+YVvj2yRUd3V2hUDzZUnPh7k5Ue8cEI4I1BjrrHxr5AmNI1PWqxBF0NeowAG1B908tBNdhWHmEd4qQ/VzXN4zwmb4QQQI0VJiCD5JjTHcU1HIItWJFr6Jb/YMCIXFk7C+YFHZdKbpO8xXgMNc8A2UH+cdDmMotfFS0Dhv4kmIbsW0pXd4ElTwNaQXWYOnkRD7/5/gDfWdIIZFI0RfDDtaVjEN0krU00r7BSYQ/6iU3V20oITZdHbr5eKb83fluzXrALwUQIJr3dI2RArlo1LwWnUOBccC/0n0knfGTp8iEV+DkVPTl+OfbyT6InwexSekeEXrUVEnez1VE4LKYmo0TnOE1VEu0mxYYucdEXHn0JSbrAGPgtdZ3QpOFkvo0lupEMEAe1Z71JOXW/YcF2EVaobVpfrJFgf/hQec6eQG6vxYX6wvIaY5lDgRJMvhqXrKdb3IrdBD4Z66j8oYO1ORKmSlPm/j5tQuboiBy7Vja7gjeRqrWxRv5fvhlGp+qtlbbI0o6Y71ngV4skL30EPG66OK4Y6vFtSKUpeRvcJWBY/VIR2MwpU7/iStwMCmeCCcVXg7iJGAOnlaY9xGNnaiMPSWu46aEF4b7exc+qMeuOP8w5lNBCR3OAFruVCG6gERqJkFz2/t40c6RKeV5at4VxQ3+8Um6112HZtRJ+L6EpETE32XSwojYKegGTZU3oMSVMTQ2U8RMACaNzmAkjdUIsca/ITqEo4BY+ayZpKLST8c7tjaR93sq7zMawz10yunQVrWR44M96KQBWpRSX9oTDuipsoSgwvLuCZ0ivmBSwviDAAVnCBHcjLzClX6ew0otyQDzkWVWl1B0QQKDiGnR9vcBX+w40bxYjZJ49c1QevxSwZIWBDSbYSTB+gztjnWehi25eSvmydo3b6hc36TdXvuwLUmDEDeQzRqw6a49k2AmUluTp0M95wQNUNH5RcHJ2DS2kTm418hTd6j27J1LXAnNgx46WE5vYU630SNU4QFhfOfhb9AFh6V5OxTKF1DyO0Kdl9fXB6N001H1zePvM/kn/77CKpFjYfVWqFXmCB8m3mL5IT3MVyamhtIoX9c25sF2hAKtXtonHd6v3U7U4e4UpFjssnNdQ9ieJQ5hkfJs2VRe4XMP8F7INyPtur9jrhVphxy4V3gbzfzYaCmXAa1a/KAWzcD1elAeZZr3YJ3InMvFw7ETEOY+5hvC/MPsjxysRlNp8dxPmpWgVRVfqoYDUmuJvUymVyPj+kndQDYmovUX9Hx79nGXDKl2kdCVBzgKe8ol64Q7OkS52o48EtFFqgtN40/ZdB5CI7YW+6PU4sr4hmOjHbQOx53NMl6QYQmSkxAhMCEEIGKmtlfbRMMuSZYISQSJYII34fVWVQxq4ImI5Fh50lvvVZZZnU7Gpr2rKPT7veVs9L9hlI8sAHKX7WlHnNCfAknv7S4kvrTmm5bsn/WzX3ak9d0OsEVVdhdaZ1r5+hesREcY5YIhIW9StHIoqtnbm+2gSOjc6hSIqQ3JDm214Qj05hscaODHScShIbFRjNaZn0pDM2yBw2EHCr20st4UylM2koerLTUVTtjxNM5yw0RRgDaRu6Rj8cDgQNrV20PoSnGatl2FNJNE4zuskjahQVH67K/4VvwYc+cxsuDrksQI7/toxTuvfliMRnriZqYLz9CTu/lhvc8X/upX+iTgoob1RZdu/ssKvrwH5qFYoD0XbT7LyESbweQ7bM5gqitX1Oovi5BIz/099umF9oFI4aL7hHhLitb9XDt82ZcO9mCG0jafzG8/GHEsrOaFqQMwEAwM4KWJi0JztiRI6/PF5NyoxrDXHo7gpO8p4Q9K8oAYGfJvQ1ppS6djX8Gz8jHTReMgX0XqCTOqi/vYlPgbzBcXblzQ2vn6fdpyCfYBwowOQeyDE+Ng/OFobrCfVs2VVfk0FomLLIUPmuimrF88Argl3qNXLKXzpd+LirfCv1vzqcRRPTjjO+yrE0KJs35H1uuC/teiQI+GLOv0Fole5eutIun7gg83MNr32uss4s863/3QPctSoljef2VR4iSnzAeRrIknNFVQF0QsIJBme00rT9ScRAK0P5SpdcpZruzdogEwBthbusOisE3xKdDsPLra18M7wo09BuOki51KVcXyg0azeZ2hEYz/JPz2ho8d+/rMGO7pS9UuT9GuvjAvLe5ax+5+ZIcCz58RQahf10ykBbPR+7aGyWBuwwPALhwjGVKSeElKg7ssdZzFcx9FnnsKCWPaS3S1EbSkAxgtH4s/qOElbpkM0GUlKWpV2aS/qb0eD1Zilv6PjQlEvjdNHC4HyWbp+a2hlwAK7eRl17DNWWxEPoh8qL3tvoxiV9Mle8RZ6lnbqytS+ppskL5bkQZZrj4g28lXnZXT4rDFcKyuxWcFKloXgA5MRSmasqywTZfA7MBWz69SeJQCBxLcM7da1KzQUixhZWKcvAdCb71vKg1C6pAAC5rN7E+FEUAtKVYclp6kqJT5wzoMpggpgRlzIbpKuCEMQQNeOa6KYP9kFox3NU5WgIkb+6/k7P5dKif/dGwpOsAOac6T3v0D6F1Pkshe3ONjKibHhVwySIP2LulamVf/1eJjmAGSnpb/ciKHI7i81b7E/TMXbItzfcE+fD+D5NrFC/a0wRr+NwmS5VUAaStrx/8nkT8admJGhuyv4Fa+SAoqgP+aIBE2twvMSDlbIxd1/EnBlC883/zxdeHfAiDl31V55eRUuE7kF5um7jO70EySz9H9AzSR6KGC0Qm0oMhumjYBvFUc7UU9Og9SBo8CV7MYX+0w9vICgdSzYPCDxV7y/I9iFNfEH3Ts68WcOvyDPot7mBkixFy6veD2LDul7HGEhBNLzwmM1EJtUMnvglgqYngPQrSt4lchtOqQNiMCqi6kVYo4et5uCkF2MpJIfSq9VbO+EDBNwTvC0aU/v58t5vribFdihmVvdErZdVMWdyHg9pHI1Shxr6Trthy9GzKyb7Y6lQL84APY902jaKwoPDG0+A62XHrS5ye7QuEFubXyfneY118m7W/c4EZ9pmg5PY4GG31sRVBab7tkc9s6T97Zptv7pdAgAh0xd604eSWXG/w26jlU1XLhOZpNxUlCvOGSjeYCLWrz7xQqDSPwWU4RFMVavUPEj4rVT5WS/FE/SvBGbHxGm3RxlP3kbKbIRYGSErLCw+KXlASNiA/OSlqhYOvzXCua5KNq5zLQQNvQVlyKjTbuMykLGy+gc66LoJvwOmpxE+ApXpWHUD2pMRve0UsJPMwZbv94xroUk8J/xquyAuUK3i9R4nYvsgCdrqo9h7rzx9qOV9uglfsaRB+5407Sf5qjuVkdgqCWIEyVG/P4UZdY2/7yqySlBD6Xhs5NOIKhX1IorDOj3Fb4kbmQ98sxIXlz9e3SL2I1D0FUBPs8kHtshhrDjLeQzl96C021XLfYrR7VSFEiuGJLvs3Z+NcOZmJSXzjV8C0TRgfk1quwQF8abtQWBTtt/nfHToPqH6XY2X/0ofIQZjrDbSmEDDCSfUlxxFrbwRyDbXG7BZoK40jQW20CUawUj87Bz6KRJZW83f3YtAe1aeRmv8yUSYo8AVPj9rrlTlCjeA5NzoL+3kC8WR8z/xqwZ4m16DB3AVz/rhN9W77R1vAF9YPZ0nhPQB7gesGj4W0+Fr0Q7wOgyyL+Ahqp/nsol4MRS0oxk2OTe459KhWedbEUsLvdnHF3SUiEroURBBLYVKJfcU9qaKwlvohbjHWerufvDziBSszglAvjPYgTQDTmMZhvfwMbMgboxEWOiVaDzAykIeDPqzcE0lU6K18jb5QEiGL573i3tM+ojNSjCRSTs0sC/bP8jJ3/LMzNjx/SKPHTu0zc/1LntCHk8hJWSD//9iwB3BiliffE2SS5z3I/TLcVmzNsHK/w881i7YLmAURU28qt8fUykvku8FWF///G7oi56VFFm+Cq+G2BXHp9Wx3IuJQYfBxXMKHGtsPSEklXVw61inTz4ac0VzTC+G7KStEZqCfiC0lxLfsKi0oZ5FL+OOXXwjGlz98CiFoA2dQGtY2IitesPFnxz++2o2DRb7vgu/wd+P+pMPZcomcunHK4xuxZ+GIef6LdWB1SJYQRt/pyi+9gicXB3ImXI5a554DtgVHQ2gLiaLlwQ3BNNFwE7K6sto7hup++OD2X7alJxlk+dCTD8mEzO8WWVK1pXbkcMpb860EO8zCDaZc4sa4DcciINvM5JUMSr01v+ep6l3+KqibBG3GdXNI4fSni/k5fjIikaSQmkY8oKyjrzRUL3vh5gpqbH6xnR+gGZfmJYx7b4+8zMoPDN0VF2+z9QZBMjcb6gHJKCTMHxFXpUsVipKokFdPNG8IvTrQsNlI4avXQKFFHaePh1C5GTjrDOH6O8nb3YsMho5G7JRg7ORv5mVHbeT3BsNLNYZ7c8QjeMzTNBvHWqaEPRwrNHhqkgA7EiM374pNewsqRge2j9fl/VJ0Rkx3FrR979U4IlX1Q50igijAopZnWbJkV/qX2h/SGzModMIVaa69xcwcNydc96Ms/XjTSO90crAbvImicTvubOHg5JV9kJHjWAsFI7dfzBVU2yaxtq17Gxx2+amayS2rUO8gI4GGZ40tN4gztWPnuigjazXVfvvfJSuS974l60OtwVxnwvAQ9jIjPeVdRN65ww9RJiYb54CUn3FEtc6IKCY2MyatgkWUd8SgXZ7Jeuqut1MyxgGoUYGZjZP5dUjxQ7ukXZ5ab12q181QtFfDm+qhy5PAjdWC9oToL/J7Zu2qq2znYD4GaOWPgSoQ3y44/9Ra5f2SdQkzdjtGVYjLa1Nwj98hLtHy6xZC4YZQTxsQqwmJdHyLbPK4nOXlxZOJwRpemLqlJBtTa2K0r1lijnSnY1KwszV3sYs0IKUlxj5m9G3oDWHqPgte7Ky2aC8aqifYTYpnIflRx2K8ITbxXIUwmK0J1LqBoBeT5JA/9+F6aOjvm9G1dZqok/xmE0E0XRmUKZN9lqKmnZazinPpHcd+oJ+xzEzqDK55RlpHTo2OevUUNTPyBqksfHxrfVfUwdjPFckUlJN0p4U1E2vYKyRO1dX4Ry8y6hnUmouW56Eq+8YkSaMPYdcG0xBQ6m/VNPsC26HPZ4WQTohuSV1//rCttSFnV6W1VkxXMgNHuMLpGMZ1HrsqNl+1nL7QQ1dV/DlFvIHioDpbt05mfSHDbjJJtxJ4rL1vHXtlmLA1EV12Kg7q1zOMdW0yuby22mrxAK58WySWD1FcImElqi82/Apo6ejIkaFlz58eueg1Po5yD4WLNiNWi9lgr9xeBL4YJufhqHLiPYlJcGv/eZy4Qp5XjLTdMaxrYsVkQo5j8hXAfSpWMCadR9PG6o+Q8cSdWHgY3OiLxdeWCJuZJKNaGAfAArS8ggrcQTjASB2aJegWt8Q+2C6ZZc7Azt5L1bTWg/CSLKQFaoEUFJz43nbJjiJn1hKg9X+CyYaXyu3DiV7/ScEDGnz3IdGEaWq4+FLeI0W7I3QbsytE9+Gtd6qPH/AL+XYEApTXBffs8XDSSRN8NysJMEB4sL99T05/5e3kNjclZo9joxE50qhOvtxIksLtR9+m7Qd6HQMdS+x3BxhbGuFmJKJFVcJbArIfAAHbg9lmHEj1SbnytHtx/epcE30FUEiSFxUD03mZfZqPwXxdoGTu58+pSqaosNpXs1kHM986DRMyI/6i/GtD0ZzpM0Xp3cFtMFur7Ac3NhLDzUiz2vYMGOzFsQJiWWaC6CqPE/UADFF0rIxj79/3Mm3koVOchnVKRH0phIBvITf+rBSjdia1mC5zjoyDoR++eVbAjA7N7RSdGx4jszq7soziryBH/Mt4tMDnYSe737odL7QgUy/6kKrCQZM7BX5lFHxR74TfHfuUceg4a5ER65FYqZfgaZBQxZXvGO/ArEOTPlPpzjC/CGd+1nTtV1QitOLI7wcPWlQlfRrGNKTM9mfpBVkNVRDRsioidXi8UfC9y0jk7AIKInp1lVd842E6uqNmT0ERd8Ibfg5cixQ9rUaZXJEOxzCQLa7djAkEdW/ZzVgwWpT9/2YeieNRrjJd7TriBLsgsTEyiqfi/kFuOKHUIROB3gp52J0gSL
        - #1:
          - type: tool-result
          - toolCallId: FbaVORayysJ4AiwB
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: ZY5iEEL15YvTVF9e
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: e0kKALt7OoEc8io6
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: dtP6sLyFoNDayfic
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.