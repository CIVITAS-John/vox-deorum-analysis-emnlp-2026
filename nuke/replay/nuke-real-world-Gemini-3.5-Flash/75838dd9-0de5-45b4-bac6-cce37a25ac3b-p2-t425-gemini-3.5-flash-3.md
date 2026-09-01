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
      - toolName: set-relationship
      - args:
        - Public: 90
        - Rationale: POLAND - CRITICAL VOTING ALLY: Poland is our top friend with 16 delegates. We have a Declaration of Friendship and both follow Autocracy. Maximizing relationship ensures they vote for us in the upcoming World Congress Global Hegemony election, which is key to our Diplomatic Victory.
        - Private: 80
        - TargetID: 3
    - #1:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Private: 50
        - Rationale: AZTECS - DOFS AND SHARED VASSALAGE: We have secured a Declaration of Friendship and traded resources with the Aztecs. They follow Autocracy and are also vassals of the Iroquois. Shifting from hostile to friendly ensures we maintain this valuable alliance and potentially secure their 10 votes for the Global Hegemony election.
        - Public: 60
    - #2:
      - toolName: set-relationship
      - args:
        - Private: -40
        - TargetID: 6
        - Rationale: BRAZIL - DIPLOMATIC RIVAL WITH DOFS: Brazil has 26 delegates and is our main competitor for city-state alliances (e.g., Zanzibar). While we have a DoF and shared Autocracy/vassalage, we must maintain a cautiously negative stance to ensure our staff aggressively competes with them for city-state influence, while avoiding diplomatic fallout.
        - Public: -30
    - #3:
      - toolName: set-relationship
      - args:
        - Public: -100
        - TargetID: 1
        - Private: -100
        - Rationale: IROQUOIS - ULTIMATE DOMINATION THREAT: The Iroquois control 7/8 original capitals and have 377k military strength. They only need to conquer Moson Kahni (Shoshone) to win. We must keep our relationship at maximum hostility to ensure our staff maintains a high defensive alert, builds military units, and prepares for any potential endgame scenarios, even while we are their vassal.
    - #4:
      - toolName: set-relationship
      - args:
        - Public: -100
        - Rationale: SHOSHONE - IDEOLOGICAL ENEMY: The Shoshone follow Freedom (opposing our Autocracy), have denounced our friends, and are highly hostile. Maintaining maximum negative relationship keeps our staff alert and defensive against them.
        - TargetID: 0
        - Private: -100
    - #5:
      - toolName: set-research
      - args:
        - Rationale: Electronics unlocks Police Stations (+10 City Security, +3 Culture, +5 Production with Autocracy tenets) critical for defending our core cities against potential aggression and stabilizing our empire during the critical 10-turn World Congress voting countdown. Currently completing Advanced Ballistics in 3 turns.
        - Technology: Electronics
    - #6:
      - toolName: set-policy
      - args:
        - Policy: Enlightenment
        - Rationale: Enlightenment (Rationalism branch) provides a FREE TECHNOLOGY, which will significantly accelerate our path to Satellites/Apollo Program or other critical late-world tech. Also provides +1 Happiness from Universities, improving empire stability during our push for Diplomatic Victory. Available in 8 turns.
    - #7:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Gold: 100
          - Offense: 10
          - Science: 80
          - Religion: 90
          - Diplomacy: 100
          - Espionage: 80
          - Defense: 85
          - Production: 80
          - Growth: 70
        - GrandStrategy: UnitedNations
      - rationale: PEACEFUL STABILIZATION AND DIPLOMACY FOCUS: We have secured peace with everyone (including DoFs with Brazil/Aztecs). We must focus on fixing our gold deficit (-296 GPT) while preparing for the World Congress vote in 10 turns. High Gold (100) and Science (80) prioritize economic recovery and tech, while Diplomacy (100) maintains pressure on city-states. Espionage (80) supports our spy in Belgrade to flip their alliance and secure +2 delegates. Defence (85) keeps us alert against the massive Iroquois empire.
  - tokens:
    - inputTokens: 71475
    - reasoningTokens: 12952
    - outputTokens: 785
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Options**
            
            I'm assessing our current strategic position and weighing the available macro-level choices to guide Indonesia's progress in Civ V's Vox Populi mod. My focus is on the immediate next steps.
            
            **Evaluating Immediate Threats**
            
            My current thinking is focused on the Iroquois' imminent domination victory. They possess almost all original capitals, and we are currently their vassal. This necessitates a shift in priorities.
            
            **Revising Global Strategy**
            
            My immediate focus has shifted. The World Congress is active with Global Hegemony proposed, and crucially, Autocracy is the enacted World Ideology. This means diplomatic victory is now possible, especially with the Iroquois having the UN. Our vassal status complicates things.
            
            **Reassessing Diplomatic Goals**
            
            I'm analyzing the delegate counts. While we are competitive, the Iroquois are the 'Master' and we are their vassal, alongside Brazil and the Aztecs. This changes our approach to the World Congress and the impending diplomatic victory threat.
            
            **Reclaiming Lost Alliances**
            
            I've successfully used a Great Diplomat to re-establish our alliance with Zanzibar. This is a crucial development, especially considering our current vassal status to the Iroquois and the impending threat of their diplomatic victory. We are now allied with Prague, Zanzibar, Wittenberg, and Winchester.
            
            **Securing City-State Influence**
            
            I've confirmed our permanent alliances with Prague, Winchester, and Wittenberg due to enacted Sphere of Influence resolutions. Zanzibar remains contested, with Brazil having previously acquired it. I'm now investigating other city-states to solidify our diplomatic standing.
            
            **Analyzing City-State Control**
            
            I'm updating our understanding of city-state alliances. Brazil now permanently controls Raqmu, Sokoto, and Cape Town. We maintain permanent alliances with Prague, Winchester, and Wittenberg, but Zanzibar remains contested. I'm re-evaluating our spy network's positions.
            
            **Assessing Diplomatic Tensions**
            
            I'm currently evaluating our standing with other nations, noting a complex web of alliances and rivalries. While Poland remains a staunch ally, my attention is drawn to a potential conflict escalation with the Aztecs, despite our shared vassal status under the Iroquois and ideological alignment. I'm reviewing recent war declarations to clarify our exact military engagements.
            
            **Clarifying Aztech Relations**
            
            I've realized my previous assessment of tensions with the Aztecs was mistaken. We currently have a Declaration of Friendship and are active trade partners, not on the brink of conflict. This significantly alters our diplomatic calculations.
            
            **Updating Diplomatic Status**
            
            My recent analysis confirms a Declaration of Friendship with Brazil, solidifying our relationship beyond shared vassalage. It appears the Celts and Japanese civilizations have been eliminated from the game, significantly altering the global landscape.
            
            **Analyzing Shoshone Threat**
            
            My primary focus is now on the Shoshone's sole original capital. The Iroquois, controlling all other seven, are on the cusp of a domination victory. This necessitates an urgent shift in our strategic priorities to prevent their imminent win, as they have overwhelming military strength.
            
            **Securing Diplomatic Victory**
            
            I'm analyzing delegate counts to secure a diplomatic victory. With 29 delegates and the Iroquois at 33, our current path is blocked. I need to find a way to win the World Congress.
            
            **Gathering More Support**
            
            I'm recalculating our delegate count for the diplomatic victory. We currently have 29, but need 41. I'm exploring options to increase this, either by securing votes from other nations or by gaining more city-state influence. Zanzibar is secured, but Belgrade remains under Iroquois influence. I'm deploying a spy there to try and sway its allegiance.
            
            **Securing Victory Through Poland**
            
            I've identified a clear path to diplomatic victory by securing Poland's unwavering support. Their deep affection for us, stemming from trade, shared ideology, and our UN assistance, makes their 16 delegates attainable, pushing our total past the required 41 votes.
            
            **Assessing Diplomatic Alliances**
            
            I'm re-evaluating Poland's stance. While our relationship is strong, their existing pact with the Iroquois poses a dilemma for the upcoming World Congress vote. I'm also re-examining Aztec and Brazilian allegiances in light of their ties to the Iroquois.
            
            **Securing Key Alliances**
            
            I'm confirming our policy choice of Enlightenment for its free technology benefit. To secure crucial votes, I'm boosting our relationship with Poland to ensure their full support in the World Congress and re-evaluating our strained ties with Brazil.
            
            **Adjusting Diplomatic Rankings**
            
            I'm revising my diplomatic assessments, recognizing my previous miscalculations regarding the Aztecs. My current focus is on properly reflecting our Declaration of Friendship and trade partnership, shifting their standing from hostile to friendly to accurately inform our strategy moving forward.
            
            **Securing City-State Support**
            
            I'm focusing on solidifying our existing city-state alliances with Prague, Wittenberg, Winchester, and Zanzibar. I'm also investigating the current status of Wittenberg's Great Musician quest and re-evaluating the Shoshone threat and our relationship with them.
            
            **Deploying Diplomatic Units**
            
            My current focus is on leveraging our producing Ambassadors from Medan and Makassar to secure Belgrade's allegiance. Belgrade is allied with the Iroquois at 660 influence, while we currently stand at 434. With an Ambassador, we can easily sway Belgrade to our side, gaining a crucial 2 delegates. Additionally, I'm ensuring a trade route is sent to Zanzibar to maintain our alliance there.
            
            **Redirecting Trade Routes**
            
            I'm rerouting expiring trade routes from Jakarta to Zanzibar to complete their quest, boosting influence and food. My focus is also on addressing our significant gold deficit by investigating our large military upkeep.
            
            **Analyzing Policy Options**
            
            I am weighing the benefits of the "Third Alternative" Autocracy tenet against "Enlightenment." While the former reduces unit maintenance by 25%, the latter grants a free technology, a critical advantage for accelerating late-game research. I am calculating the precise impact of each.
            
            **Choosing Policy Options**
            
            My current thinking is centered on policy choices, specifically weighing "Third Alternative" against "Enlightenment." While "Third Alternative" offers a unit maintenance reduction, the free technology from "Enlightenment" is critical for late-game research acceleration. I'm confirming "Enlightenment" as our immediate next policy, as it aligns with the Rationalism tree and is crucial for our progress.
            
            **Securing Strategic Dominance**
            
            I'm consolidating our military posture. With no enemy units detected across all friendly zones, and several cities successfully razed, our immediate strategic position is exceptionally secure. Our diplomatic ties are also exceptionally strong, leading to a peaceful global landscape.
            
            **Securing Votes for Victory**
            
            I'm re-evaluating our path to diplomatic victory. While the Iroquois currently lead in delegates, securing Poland and the Aztecs' support would put us well over the required 41 votes. Flipping Belgrade from the Iroquois is a high-priority target to gain crucial delegates and weaken their position.
            
            **Analyzing Delegate Mechanics**
            
            I'm dissecting the delegate mechanics for the World Congress. Brazil, Shoshone, and Poland gain delegates from Confucianism. Crucially, all five Autocracy followers (us, Iroquois, Poland, Aztecs, Brazil) each receive a significant delegate boost due to our shared ideology. This explains my current delegate count of 29.
            
            **Securing Diplomatic Path**
            
            I'm focused on fine-tuning our delegate count for diplomatic victory. Poland and the Aztecs are key, and flipping Belgrade from the Iroquois is essential. My current delegate count is 29, but we need 41, with Autocracy followers receiving a significant boost.
            
            **Researching Advanced Ballistics**
            
            My current focus is on completing our research of Advanced Ballistics, with only three turns remaining. Following this, I intend to immediately begin researching Electronics to unlock Police Stations, which will bolster city security and provide a vital culture boost.
            
            **Choosing Next Research Path**
            
            I am prioritizing Electronics for Police Stations to boost culture, despite the allure of Satellites for a Science Victory. The immediate need is consolidating our diplomatic strength, making Electronics the most pragmatic next step.
            
            **Adjusting Diplomatic Ratings**
            
            I'm rectifying a critical oversight regarding the Aztecs. My previous hostile rating is outdated; they are now friendly, necessitating an immediate adjustment to reflect our Declaration of Friendship and trade partnership. This also impacts my assessment of our alliances.
            
            **Strengthening Diplomatic Ties**
            
            I'm focusing on bolstering our relationship with Poland, aiming for Public 90 and Private 80, to guarantee their critical 16 delegates in the upcoming World Congress vote. I'm also adjusting our relationship with Brazil to Public -30 and Private -40, balancing competition for city-states with our Declaration of Friendship and shared vassal status.
            
            **Adjusting Diplomatic Relationships**
            
            I'm fine-tuning our diplomatic standings. The Aztecs are now firmly friendly due to our shared situation. Brazil remains a cautious rival, vital for city-state competition. The Iroquois and Shoshone are at maximum hostility, reflecting their existential threats and ideological opposition. I'm also prioritizing Electronics research for its immediate strategic benefits.
            
            **Evaluating Policy and Flavors**
            
            I'm confirming "Enlightenment" as our chosen policy for its immediate technology benefit, crucial for late-game research. I've reviewed our existing flavors and find them generally balanced, suggesting we should maintain the status quo rather than adjust them at this moment.
            
            **Adjusting Economic Strategy**
            
            I'm re-evaluating our economic priorities. Our significant gold deficit requires immediate attention, and I'm considering increasing our Gold flavor to 100 or reducing unit production, especially since we're currently at peace and have military bases in progress across several cities.
            
            **Setting Flavors and Research**
            
            I'm implementing flavor adjustments for a Gold boost and prioritizing Electronics research to secure Police Stations. This move aims to address our gold deficit and enhance city security and culture, aligning with our immediate strategic needs.
            
            **Finalizing Diplomatic Actions**
            
            I'm confirming our final diplomatic moves. Relationships with key players are locked in, research for Electronics is queued, and "Enlightenment" is selected. I'm also setting flavors for economic and diplomatic focus, with a final check on the Shoshone's status before committing to our next phase.
            
            **Preventing Shoshone Fall**
            
            I'm racing against the clock to prevent the Shoshone's last capital from falling to the Iroquois and thus averting their domination victory. My immediate focus is on swaying the World Congress votes.
            
            **Executing Diplomatic Maneuvers**
            
            The World Congress votes in 10 turns, giving us a tight window. I'm focused on securing Belgrade and Zanzibar, maximizing Poland and Aztec support, and maintaining cautious competition with Brazil. Our persona is well-tuned for this decisive phase.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: W8CBimo1CKD5HbD3
          - toolName: set-relationship
          - input:
            - Public: 90
            - Rationale: POLAND - CRITICAL VOTING ALLY: Poland is our top friend with 16 delegates. We have a Declaration of Friendship and both follow Autocracy. Maximizing relationship ensures they vote for us in the upcoming World Congress Global Hegemony election, which is key to our Diplomatic Victory.
            - Private: 80
            - TargetID: 3
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: vXDfYM6Bfhb8rbUi
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Private: 50
            - Rationale: AZTECS - DOFS AND SHARED VASSALAGE: We have secured a Declaration of Friendship and traded resources with the Aztecs. They follow Autocracy and are also vassals of the Iroquois. Shifting from hostile to friendly ensures we maintain this valuable alliance and potentially secure their 10 votes for the Global Hegemony election.
            - Public: 60
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: q58qGTNQaeU4jBd2
          - toolName: set-relationship
          - input:
            - Private: -40
            - TargetID: 6
            - Rationale: BRAZIL - DIPLOMATIC RIVAL WITH DOFS: Brazil has 26 delegates and is our main competitor for city-state alliances (e.g., Zanzibar). While we have a DoF and shared Autocracy/vassalage, we must maintain a cautiously negative stance to ensure our staff aggressively competes with them for city-state influence, while avoiding diplomatic fallout.
            - Public: -30
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: mXajyyVEbKd4GBs7
          - toolName: set-relationship
          - input:
            - Public: -100
            - TargetID: 1
            - Private: -100
            - Rationale: IROQUOIS - ULTIMATE DOMINATION THREAT: The Iroquois control 7/8 original capitals and have 377k military strength. They only need to conquer Moson Kahni (Shoshone) to win. We must keep our relationship at maximum hostility to ensure our staff maintains a high defensive alert, builds military units, and prepares for any potential endgame scenarios, even while we are their vassal.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 2qjCjMPOdTXucSHE
          - toolName: set-relationship
          - input:
            - Public: -100
            - Rationale: SHOSHONE - IDEOLOGICAL ENEMY: The Shoshone follow Freedom (opposing our Autocracy), have denounced our friends, and are highly hostile. Maintaining maximum negative relationship keeps our staff alert and defensive against them.
            - TargetID: 0
            - Private: -100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: T5x6v9uL2eHQunPa
          - toolName: set-research
          - input:
            - Rationale: Electronics unlocks Police Stations (+10 City Security, +3 Culture, +5 Production with Autocracy tenets) critical for defending our core cities against potential aggression and stabilizing our empire during the critical 10-turn World Congress voting countdown. Currently completing Advanced Ballistics in 3 turns.
            - Technology: Electronics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: X50pDrYg5Ak1Hfze
          - toolName: set-policy
          - input:
            - Policy: Enlightenment
            - Rationale: Enlightenment (Rationalism branch) provides a FREE TECHNOLOGY, which will significantly accelerate our path to Satellites/Apollo Program or other critical late-world tech. Also provides +1 Happiness from Universities, improving empire stability during our push for Diplomatic Victory. Available in 8 turns.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: jZwzzwpAFSDYMTqv
          - toolName: set-flavors
          - input:
            - Rationale: PEACEFUL STABILIZATION AND DIPLOMACY FOCUS: We have secured peace with everyone (including DoFs with Brazil/Aztecs). We must focus on fixing our gold deficit (-296 GPT) while preparing for the World Congress vote in 10 turns. High Gold (100) and Science (80) prioritize economic recovery and tech, while Diplomacy (100) maintains pressure on city-states. Espionage (80) supports our spy in Belgrade to flip their alliance and secure +2 delegates. Defence (85) keeps us alert against the massive Iroquois empire.
            - Flavors:
              - Gold: 100
              - Offense: 10
              - Science: 80
              - Religion: 90
              - Diplomacy: 100
              - Espionage: 80
              - Defense: 85
              - Production: 80
              - Growth: 70
            - GrandStrategy: UnitedNations
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: W8CBimo1CKD5HbD3
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
          - toolCallId: vXDfYM6Bfhb8rbUi
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: q58qGTNQaeU4jBd2
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: mXajyyVEbKd4GBs7
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 2qjCjMPOdTXucSHE
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: T5x6v9uL2eHQunPa
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: X50pDrYg5Ak1Hfze
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: jZwzzwpAFSDYMTqv
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.