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
  - systemModified: false
  - messagesModified: false
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
  - decisions:
    - #0:
      - toolName: set-relationship
      - args:
        - Private: 80
        - Public: 90
        - TargetID: 3
        - Rationale: Poland is our close friend and Autocracy ally. We must maximize our relationship to secure their 16 votes in the upcoming Global Hegemony (World Leader) election, which would easily push us past the 41-vote threshold.
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: We have a Declaration of Friendship with the Aztecs and are fellow vassals under the Iroquois. Modifying relationship to positive to maintain peaceful cooperation and avoid AI paranoia during the critical World Congress voting phase.
        - TargetID: 5
        - Public: 40
        - Private: 20
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 6
        - Private: -40
        - Public: -30
        - Rationale: Brazil is our chief diplomatic rival for City-State alliances but we are currently at peace and have a Declaration of Friendship. Maintaining slightly negative modifiers to keep our AI guarded against their diplomatic influence campaigns while avoiding conflict.
    - #3:
      - toolName: set-policy
      - args:
        - Rationale: FINANCIAL EMERGENCY: We are facing a severe gold deficit of -296 GPT due to Global Peace Accords (+25% unit maintenance). Third Alternative (Autocracy Level 2 Tenet) will reduce unit gold maintenance by 25% and double our Strategic Resources (including Paper, Aluminum, Coal), which we can sell to Brazil/Aztecs for massive gold. This prevents bankruptcy and science penalties.
        - Policy: Third Alternative
    - #4:
      - toolName: set-research
      - args:
        - Rationale: Electronics unlocks Police Stations (+10 City Security, +3 Culture) to defend our cities against espionage and maintain stability, and leads toward Telecommunications and Satellites. Advanced Ballistics completes in 3 turns.
        - Technology: Electronics
    - #5:
      - toolName: set-flavors
      - args:
        - GrandStrategy: UnitedNations
        - Flavors:
          - Science: 70
          - Mobilization: 30
          - Diplomacy: 100
          - Defense: 80
          - Religion: 80
          - Gold: 100
          - Production: 70
      - rationale: ECONOMIC EMERGENCY & DIPLOMATIC FOCUS: To resolve our -296 GPT deficit, we raise Gold to 100 and lower Mobilization to 30 to shift production from military units to wealth. We maintain Diplomacy at 100 to prioritize our upcoming Ambassadors (finishing next turn) for allying Belgrade, directly weakening our main rival Hiawatha's delegate count.
  - tokens:
    - inputTokens: 71285
    - reasoningTokens: 9362
    - outputTokens: 485
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Diplomatic Path**
            
            My current focus is on navigating the diplomatic landscape. With 29 votes secured, I'm meticulously planning my strategy leading up to the World Congress vote in 9 turns. My primary objective remains achieving a Diplomatic Victory.
            
            **Analyzing Diplomatic Options**
            
            I'm re-evaluating my path to victory, realizing my vassal status with the Iroquois impacts the Diplomatic Victory potential. With 29 delegates secured, I'm assessing if I can still win independently or if this victory must now be achieved by my master. I'm also scrutinizing active resolutions, particularly "Global Hegemony."
            
            **Securing City-State Alliances**
            
            I've successfully reclaimed Zanzibar and confirmed my alliances with Wittenberg and Winchester. I'm now investigating the status of Sofia, as it appears to have been defeated, which may affect my diplomatic options.
            
            **Confirming City-State Status**
            
            I've confirmed Sofia's defeat. My current focus shifts to verifying the ally status and delegate count of Prague, Belgrade, Raqmu, Cape Town, Zanzibar, Wittenberg, Winchester, and Sokoto. I'm tracking Indonesia's spy activity in Belgrade and assessing our current total of 8 delegates from four allied city-states.
            
            **Securing Diplomatic Leads**
            
            I'm focused on maximizing delegate acquisition. With 29 delegates, I'm strategizing to secure additional city-state alliances, particularly aiming to gain influence in Belgrade and other CS contested by Brazil and the Iroquois. My new ambassadors will be deployed strategically next turn.
            
            **Clarifying Wartime Status**
            
            I'm re-evaluating our current military engagements. It appears there's been a misunderstanding; we are not actively at war with the Aztecs or Shoshone, despite past denouncements. My focus is now on confirming diplomatic ties and managing the ongoing vassal relationship with the Iroquois.
            
            **Confirming Global Peace**
            
            I'm verifying our current diplomatic status and realizing we're not at war with anyone. It seems our previous denouncements were just that. My focus has shifted to understanding how our shared vassalage under the Iroquois impacts our relationships with the Aztecs and Brazil, and this has clarified a great deal.
            
            **Investigating Razed Cities**
            
            I'm trying to understand why Dublin and Douglas are being razed, as this activity seems incongruous with my perception of global peace. I'm also examining the specific nature of my relationship with the Iroquois, particularly whether it implies a shared bloc of alliances or an imposed peace.
            
            **Researching Technology Path**
            
            I'm analyzing the technology tree, specifically the prerequisites for satellites. It appears I previously set Electronics as the next research, intending it as a stepping stone to the Apollo Program. I need to confirm if this is the correct sequential path to achieving satellites.
            
            **Selecting New Policies**
            
            I am now considering policy options, particularly "Liberty" within the "Continuing Progress" branch, though I need to confirm if Progress has already been adopted. My focus is on selecting the most advantageous next policy given the diminishing turns remaining for the World Congress vote.
            
            **Selecting Next Policy**
            
            I've confirmed that "Enlightenment" remains a viable policy option and am maintaining it as my next selection to accelerate technological advancement. I'm also re-evaluating diplomatic standings, noting Japan, Sofia, and the Celts are defeated. My focus now turns to understanding our -100 public and private modifiers with the Aztecs, given our shared vassalage.
            
            **Managing Diplomatic Nuances**
            
            I'm grappling with the complexities of our vassalage under the Iroquois. While Hiawatha seems pleased with our relationship, our own fear and significant negative modifiers towards them could trigger erratic AI behavior. This power imbalance demands extreme caution to avoid jeopardizing our current standing.
            
            **Securing World Congress Victory**
            
            I'm re-evaluating the path to a Diplomatic Victory given Hiawatha's delegate count. Brazil remains a close rival. I'm assessing whether to focus on securing enough votes for myself, potentially by gaining more city-state alliances and targeting Poland's delegates, or if Hiawatha voting for himself is a viable, though unlikely, scenario.
            
            **Securing Key City-States**
            
            I'm prioritizing securing Belgrade with my upcoming ambassadors, which would bring us to 31 delegates and neutralize Hiawatha's advantage. I must also defend our existing city-state alliances from Brazil's substantial gold reserves and influence, especially considering the enacted "Indonesian Sphere of Influence" resolutions affecting Prague, Winchester, and Wittenberg.
            
            **Securing Permanent Alliances**
            
            I've secured permanent alliances with Prague, Winchester, and Wittenberg due to the "Indonesian Sphere of Influence" resolutions. I successfully reclaimed Zanzibar this turn. Now, I'm focused on proposing a Sphere of Influence for Zanzibar in the next World Congress session, as the current one is locked in for "Global Hegemony" voting. I'm also considering how to leverage Poland's 16 votes to secure the necessary 41 votes for victory.
            
            **Securing Poland's Vote**
            
            I'm re-evaluating Poland's potential to vote for me in the World Leader election. With their high opinion of me and our Autocracy alliance, securing their 16 votes is crucial. I'm adjusting our relationship modifiers to ensure their support, aiming to easily surpass the 41-vote threshold.
            
            **Adjusting Diplomatic Ties**
            
            I'm refining my diplomatic approach regarding the Aztecs. Given our shared vassalage and a Declaration of Friendship, I'm adjusting our relationship modifiers to a more positive, neutral stance to ensure stability during the crucial World Congress phase. The Shoshone remain hostile, and I'm maintaining a negative relationship there.
            
            **Refining Diplomatic Settings**
            
            I'm adjusting our relationship modifiers with Brazil. While we share a Declaration of Friendship and Autocracy, their rivalry for city-states necessitates a slightly negative stance. I'm setting our public and private modifiers to -30 and -40 respectively to balance peace with strategic caution regarding their influence.
            
            **Assessing Rival Delegate Count**
            
            I'm recalculating Hiawatha's delegate count, realizing his 33 votes are not from city-states or resolutions, but likely due to his 56 cities. This confirms he is a direct competitor, potentially winning the game himself if "Global Hegemony" passes.
            
            **Leveraging Ideology Advantage**
            
            I've realized the "Autocracy" World Ideology is a massive boost, granting me 5 delegates and significantly increasing Hiawatha's count to 33. This revelation clarifies the delegate distribution, making the diplomatic race intense but manageable with careful maneuvering.
            
            **Securing Key City-States**
            
            I'm focusing on securing Belgrade. With two ambassadors arriving next turn and my spy already en route, I'm confident I can gain enough influence to become allies and secure those crucial delegates, shifting the balance of power.
            
            **Reviewing Ideology and Policy**
            
            I'm confirming my ideology is Autocracy, which grants me 5 delegates. I'm also checking that my policy selection remains Enlightenment, as planned, with 8 turns until adoption. This aligns with my goal of accelerating technological advancement while managing diplomatic objectives.
            
            **Confirming Policy and Relationships**
            
            I've confirmed "Enlightenment" remains the optimal policy choice to accelerate my technology, aiming for Satellites and the Apollo Program. I am also finalizing my diplomatic relationships, aiming to secure Poland's crucial 16 votes by maximizing our positive modifiers, and adjusting my stance with the Aztecs for stability.
            
            **Adjusting Relationship Modifiers**
            
            I'm refining my diplomatic approach with Brazil, setting public and private modifiers to -30 and -40 respectively. This nuanced stance balances our Declaration of Friendship with their rivalry for city-states, ensuring strategic caution without inviting conflict. My next research is Electronics, and Enlightenment remains my chosen policy.
            
            **Evaluating Flavor Values**
            
            My current flavor values are strong across the board: Diplomacy and Religion at 100, Gold at 90, Production at 75, Science at 70, and Defense/City Defense at 95/90. I'm deciding whether to use `set-flavors` to reaffirm these or if `keep-status-quo` is sufficient, considering the potential to influence more city-states.
            
            **Prioritizing Diplomatic Units**
            
            My focus is on maximizing diplomatic unit production. With Ambassadors from Makassar and Medan arriving next turn, I'll reallocate their production towards more diplomatic units, prioritizing Ambassadors or Great Diplomats to contest city-states. This aligns with my 100 Diplomacy flavor, ensuring continued influence.
            
            **Addressing Gold Deficit**
            
            I'm in a critical situation with my gold per turn at -296 and only 411 gold remaining. The enacted "Global Peace Accords" are drastically increasing unit maintenance costs. I need to immediately reduce this deficit, potentially by disbanding some of my 69 military units, to avoid severe penalties to science and unit disbandment.
            
            **Adopting Strategic Policy**
            
            I'm re-evaluating my policy choices. While Enlightenment is beneficial for science, Third Alternative offers a critical 25% reduction in unit maintenance costs. Given my severe gold deficit, adopting Third Alternative is now paramount, even if it means temporarily shifting focus from scientific acceleration.
            
            **Adopting Critical Policy**
            
            I'm prioritizing the "Third Alternative" policy to drastically cut unit maintenance costs and address my severe gold deficit. This will also double my strategic resources, allowing for lucrative trades with Brazil and the Aztecs to further boost my gold per turn, ultimately preventing bankruptcy and its negative impact on science.
            
            **Adopting Urgent Policy**
            
            My focus has shifted to an urgent policy change. Given my dire gold deficit and the severe science penalties and unit disbandment it causes, I am adopting "Third Alternative" immediately to slash unit maintenance costs. This will also double strategic resources, enabling crucial trades.
            
            **Adjusting Flavors for Gold**
            
            I'm prioritizing an economic turnaround. By adjusting my flavor settings to drastically increase my focus on Gold (100) and reduce Production, Defense, and Mobilization, I expect the AI to prioritize wealth generation and trade. This should alleviate my current gold deficit and prevent bankruptcy.
            
            **Shifting Production Priorities**
            
            I am prioritizing economic recovery. By drastically increasing my Gold flavor to 100 and reducing Mobilization to 30, I expect a shift towards wealth generation. This aims to combat my severe gold deficit and prevent further science penalties, while still leveraging my 100 Diplomacy flavor to secure critical city-state alliances.
            
            **Adopting Urgent Policy**
            
            I am adopting the "Third Alternative" policy to immediately address my critical gold deficit and prevent devastating science penalties. This policy will slash unit maintenance costs and double strategic resources, enabling much-needed trades to stabilize my economy. I'm also reallocating production and adjusting flavor settings to prioritize gold generation.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: shcRwkGh654EQiog
          - toolName: set-relationship
          - input:
            - Private: 80
            - Public: 90
            - TargetID: 3
            - Rationale: Poland is our close friend and Autocracy ally. We must maximize our relationship to secure their 16 votes in the upcoming Global Hegemony (World Leader) election, which would easily push us past the 41-vote threshold.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 424VArdsRp7fXv5t
          - toolName: set-relationship
          - input:
            - Rationale: We have a Declaration of Friendship with the Aztecs and are fellow vassals under the Iroquois. Modifying relationship to positive to maintain peaceful cooperation and avoid AI paranoia during the critical World Congress voting phase.
            - TargetID: 5
            - Public: 40
            - Private: 20
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: VptHATCk973gETEB
          - toolName: set-relationship
          - input:
            - TargetID: 6
            - Private: -40
            - Public: -30
            - Rationale: Brazil is our chief diplomatic rival for City-State alliances but we are currently at peace and have a Declaration of Friendship. Maintaining slightly negative modifiers to keep our AI guarded against their diplomatic influence campaigns while avoiding conflict.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: XwQuM41y5cl0B2Ef
          - toolName: set-policy
          - input:
            - Rationale: FINANCIAL EMERGENCY: We are facing a severe gold deficit of -296 GPT due to Global Peace Accords (+25% unit maintenance). Third Alternative (Autocracy Level 2 Tenet) will reduce unit gold maintenance by 25% and double our Strategic Resources (including Paper, Aluminum, Coal), which we can sell to Brazil/Aztecs for massive gold. This prevents bankruptcy and science penalties.
            - Policy: Third Alternative
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: t3bdZH5zTfT3vneX
          - toolName: set-research
          - input:
            - Rationale: Electronics unlocks Police Stations (+10 City Security, +3 Culture) to defend our cities against espionage and maintain stability, and leads toward Telecommunications and Satellites. Advanced Ballistics completes in 3 turns.
            - Technology: Electronics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: UJOKArYQV0Qm2pIY
          - toolName: set-flavors
          - input:
            - Rationale: ECONOMIC EMERGENCY & DIPLOMATIC FOCUS: To resolve our -296 GPT deficit, we raise Gold to 100 and lower Mobilization to 30 to shift production from military units to wealth. We maintain Diplomacy at 100 to prioritize our upcoming Ambassadors (finishing next turn) for allying Belgrade, directly weakening our main rival Hiawatha's delegate count.
            - GrandStrategy: UnitedNations
            - Flavors:
              - Science: 70
              - Mobilization: 30
              - Diplomacy: 100
              - Defense: 80
              - Religion: 80
              - Gold: 100
              - Production: 70
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: shcRwkGh654EQiog
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
          - toolCallId: 424VArdsRp7fXv5t
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: VptHATCk973gETEB
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: XwQuM41y5cl0B2Ef
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: t3bdZH5zTfT3vneX
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: UJOKArYQV0Qm2pIY
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.