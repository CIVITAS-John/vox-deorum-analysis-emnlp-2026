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
      - toolName: set-persona
      - args:
        - MinorCivCompetitiveness: 10
        - Forgiveness: 5
        - WarmongerHate: 9
        - MinorCivWarBias: 1
        - Boldness: 5
        - NeutralBias: 4
        - MinorCivFriendlyBias: 10
        - DeceptiveBias: 5
        - FriendlyBias: 8
        - DiplomaticBalance: 4
        - Loyalty: 9
        - WorkWithWillingness: 9
        - WorkAgainstWillingness: 7
        - AfraidBias: 6
        - Neediness: 5
        - MinorCivHostileBias: 1
        - MinorCivNeutralBias: 2
        - VictoryCompetitiveness: 10
        - GuardedBias: 8
        - WonderCompetitiveness: 4
        - Chattiness: 10
        - DenounceWillingness: 4
        - Meanness: 4
        - Friendliness: 9
        - Rationale: MAINTAINING OPTIMAL DIPLOMATIC PERSONA FOR UN VOTE: With the World Leader vote just 9 turns away, we maintain our highly friendly, cooperative, and city-state-focused persona. VictoryCompetitiveness(10) and MinorCivCompetitiveness(10) ensure the AI aggressively defends our delegates. High Friendliness(9), Loyalty(9), and WorkWithWillingness(9) keep our relationship with Poland (16 delegates) and the Aztecs (10 delegates) at maximum warmth, securing their crucial votes for our victory. MinorCivFriendlyBias(10) keeps our focus on city-state alliances.
        - HostileBias: 5
        - WarBias: 4
    - #1:
      - toolName: set-research
      - args:
        - Rationale: Queueing Electronics as the next research target (3 turns remaining on Advanced Ballistics). Electronics unlocks the Police Station (+10 City Security, +3 Culture, +5 Production with New World Order Autocracy tenet), which is vital for defending our home cities from spy actions and tech theft while we secure our diplomatic victory. It also serves as the gateway to Telecommunications and Satellites/Apollo Program, providing an excellent scientific backup plan.
        - Technology: Electronics
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: Selecting Enlightenment as our next policy (available in 8 turns, just 1 turn before the critical World Leader vote). Completing this Rationalism policy provides a Free Technology, which will immediately accelerate our research towards Satellites and the Apollo Program, reinforcing our late-game science backup. The +1 Happiness from Universities also strengthens empire-wide stability during this crucial transition phase.
        - Policy: Enlightenment (Continuing Rationalism Branch)
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 90
        - Rationale: Poland is our ultimate ally in the upcoming World Leader vote. They have 16 delegates, we share the Autocracy ideology, they have a 95 public opinion of us, and we have a diplomat in their capital. Elevating our relationship to maximum positive values ensures the AI continues to treat them as an indispensable strategic partner and coordinates all diplomatic endeavors to secure their 16 votes for our Global Hegemony.
        - TargetID: 3
        - Private: 80
    - #4:
      - toolName: set-relationship
      - args:
        - Rationale: The Aztecs are our declared friends and fellow vassals of the Iroquois. They follow Autocracy, and we have an active embassy and resource trade. With 10 delegates in the World Congress, they are a valuable potential supporter for our Global Hegemony proposal. Shifting our relationship to positive reflects this cooperative alignment and will help secure their votes or at least prevent them from voting for our rivals.
        - Private: 40
        - TargetID: 5
        - Public: 60
    - #5:
      - toolName: set-relationship
      - args:
        - TargetID: 1
        - Private: -20
        - Rationale: As a capitulated vassal of the Iroquois (who have an overwhelming 377k military strength and 7/8 original capitals), we must avoid provoking them. They share our Autocracy ideology (+999 opinion) and are satisfied with our vassal status. Maintaining a slightly guarded but non-hostile stance prevents suicidal conflict while we focus entirely on winning the game through the diplomatic route in the next 9 turns.
        - Public: -10
    - #6:
      - toolName: set-relationship
      - args:
        - Rationale: Brazil is our direct diplomatic rival with 26 delegates, actively contesting our city-state alliances (like Zanzibar). Keeping relationship negative ensures our AI remains highly competitive against them.
        - Private: -60
        - TargetID: 6
        - Public: -50
    - #7:
      - toolName: set-flavors
      - args:
        - GrandStrategy: UnitedNations
        - Flavors:
          - Science: 85
          - Diplomacy: 100
          - Espionage: 80
          - Growth: 70
          - Gold: 100
          - Production: 80
          - Defense: 80
          - Religion: 90
      - rationale: DIPLOMATIC VICTORY CRITICAL FOCUS (9 TURNS TO VOTE): We are in the final countdown to the World Leader election (Global Hegemony vote in 9 turns). We currently have 29 delegates, and our top friend Poland has 16 delegates, which puts us in an incredibly strong position to exceed the 41-delegate threshold for victory. We must maximize our diplomatic and financial power to protect our allied city-states (Prague, Wittenberg, Winchester, and Zanzibar) and potentially flip Belgrade (+2 delegates) where our spy is currently active. Diplomacy(100) and Gold(100) are set to maximum to prioritize diplomatic units, gold-generating buildings, and city-state influence. Production(80) and Science(85) will support infrastructural and technological advancement, specifically toward Electronics next. Religion(90) is prioritized to spread Hinduism to Belgrade, Prague, Raqmu, and Cape Town to fulfill active city-state quests for massive influence boosts before the vote.
  - tokens:
    - inputTokens: 71285
    - reasoningTokens: 10066
    - outputTokens: 1147
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Current Status**
            
            My immediate focus is on pinpointing the exact turn remaining for the World Congress voting. I'm reviewing the latest available information to ensure accuracy and inform our next strategic move.
            
            **Clarifying Turn Counts**
            
            I'm re-evaluating the voting timeline for the World Congress. While initially noting "10 turns remaining" on turn 425, I need to confirm if that count reflects the end of turn 424 or the start of turn 425, given recent diplomatic shifts and event processing.
            
            **Confirming World Congress Status**
            
            I'm verifying the World Congress voting progress. It appears the vote for "Global Hegemony" is indeed underway. Crucially, "Historical Landmarks" was enacted on turn 424, and I'm confirming the remaining turns for the current proposal, now that we've successfully retaken Zanzibar and increased our delegate count.
            
            **Identifying Active Resolutions**
            
            I've identified that "Cape Town" and "Brazilian Sphere of Influence: Raqmu" are active, alongside "Indonesian Sphere of Influence: Prague", "Winchester", and "Wittenberg", which are permanent. This means we have secured permanent alliances with Prague, Winchester, and Wittenberg, a significant advantage.
            
            **Verifying Permanent Alliances**
            
            The discovery of permanent alliances for Prague, Winchester, and Wittenberg is a major development. I am now investigating the implications, especially concerning Zanzibar's non-permanent status and Brazil's attempts to reclaim it. I am also checking the status of our spy in Belgrade following recent arrivals.
            
            **Leveraging Espionage Assets**
            
            I'm deploying new ambassadors to Medan and Makassar, a timely boost to our city-state influence. Simultaneously, I've clarified our war status; we are not currently at war with the Shoshone, despite past conflicts. This re-evaluation is crucial for future diplomatic and military planning.
            
            **Recognizing New Allegiances**
            
            I've realized a crucial shift: we are now a capitulated vassal of the Iroquois. This changes everything, as their current wars and alliances now dictate our own. I'm now investigating who the Iroquois are at war with and their extensive network of vassal states.
            
            **Analyzing Victory Conditions**
            
            I am prioritizing understanding the Iroquois' impending domination victory, noting their overwhelming military strength and proximity to capturing the Shoshone capital. This requires immediate assessment of our diplomatic victory chances, specifically the "Global Hegemony" vote, which is critical to our survival.
            
            **Securing Diplomatic Victory**
            
            I'm focusing on securing the 41 delegates needed for a diplomatic victory. With 29 delegates currently, I'm exploring alliances with city-states to reach this goal, considering that as a vassal, a domination victory is impossible, but a diplomatic one is within reach.
            
            **Securing Belgrade Delegates**
            
            I'm working to secure Belgrade's two delegates. They're currently allied with the Iroquois, but our spy and upcoming ambassadors should allow us to flip them, especially since we founded Hinduism, which they are seeking. This could net us crucial delegates.
            
            **Analyzing Delegate Sources**
            
            I'm re-evaluating our path to diplomatic victory, specifically focusing on delegate acquisition. With the Iroquois as overlords, domination is out. I'm investigating city-state alliances like Belgrade and assessing the impact of our religion, Hinduism, on securing votes in the World Congress.
            
            **Gaining New Votes**
            
            I'm exploring how allied civilizations can contribute delegates. Poland, with their strong positive opinion and shared ideology, presents a prime opportunity. I'm assessing the impact of our diplomat in their capital to potentially secure their 16 delegates.
            
            **Securing Diplomatic Victory**
            
            My calculations confirm we now possess 45 delegates, exceeding the 41 needed for a diplomatic victory. The World Leader vote is in 9 turns, on turn 435. I am now focusing on securing this win, maintaining our current `UnitedNations` strategy and prioritizing diplomacy and gold.
            
            **Confirming Research Trajectory**
            
            My focus has shifted to confirming our immediate research path. While "Advanced Ballistics" is slated to finish soon, I'm double-checking the technology queue, specifically noting the transition to "Electronics" and its implications for unlocking vital infrastructure.
            
            **Choosing Next Policy**
            
            I am evaluating our next policy choice. Electronics research is on track. I'm now examining policy options, specifically looking at Enlightenment to gain a free technology and happiness boost from universities. I'm also considering other branches like Industry, Fealty, and Imperialism, alongside Autocracy Ideology tenets.
            
            **Confirming Policy Choice**
            
            I've confirmed that Enlightenment is indeed the correct policy to maintain for the free technology. I'm now focusing on strengthening our alliance with Poland, as their strong positive opinion of us is key to securing their delegates for the upcoming World Leader vote.
            
            **Solidifying Global Hegemony**
            
            I'm confirming our delegate count is sufficient for a diplomatic victory and now preparing for the World Leader vote in 9 turns. My immediate focus is solidifying Poland's 16 delegates, ensuring their continued support, while managing our rivalrous stance with Brazil to protect our city-state alliances. I am also reviewing our alliance status with the Aztecs.
            
            **Cultivating Aztec Alliance**
            
            I'm adjusting our diplomatic stance with the Aztecs. They've declared friendship, share our ideology, and we have an active embassy and trade. With 10 delegates, their support for Global Hegemony is crucial. I'm setting our relationship to friendly to secure their votes.
            
            **Assessing Shoshone & Iroquois Relations**
            
            I'm re-evaluating my stance on the Shoshone, their ideological opposition and denunciation warrant continued negative relations. More critically, I'm concerned about my public and private -100 opinion with the Iroquois, my master, given their overwhelming military strength and my vassal status. This vulnerability requires immediate consideration.
            
            **Adjusting Iroquois Relations**
            
            My current focus is refining my relationship with the Iroquois, my overlords. Despite our vassal status, their positive opinion due to shared ideology and trade is a crucial factor. I'm adjusting our public and private diplomatic stances to a slightly negative but controlled level, ensuring safety and avoiding provocation from their overwhelming military might, all while I pursue a diplomatic victory.
            
            **Confirming Diplomatic Opponents**
            
            I'm updating my understanding of remaining major civilizations. Brazil defeated the Celts, and Poland defeated Japan, leaving fewer opponents. I'm noting this shift to focus on the remaining independent and allied powers for the diplomatic victory race.
            
            **Securing Diplomatic Victory**
            
            I've confirmed we now hold 45 delegates, surpassing the 41 required for a diplomatic victory! Poland's unwavering support, secured through a strong friendship and shared ideology, is the key. The World Leader vote is only 9 turns away.
            
            **Deploying Intelligence Assets**
            
            I'm re-allocating our intelligence assets. Agent Raden is en route to Belgrade to influence elections and secure their delegates. Meanwhile, Agent Prapana will remain in Brazil to cultivate ties, and Agent Jayakatwang continues to defend our capital. I'm also sending agents to the Shoshone for intel.
            
            **Revising Spy Deployment**
            
            I'm re-evaluating our extensive spy network within the now-peaceful Shoshone territory. While previously wartime assets, their current purpose needs re-evaluation. I'm also confirming the status of our diplomatic and other intelligence assets, particularly Agent Indra in Poland, whose role is critical for securing votes.
            
            **Confirming Religion Quests**
            
            I'm scrutinizing the religion quests, specifically the Hinduism one for Wittenberg. It appears it might have expired or been completed without my direct observation, necessitating a re-evaluation of city-state quest statuses for optimal delegate acquisition.
            
            **Spreading Our Faith**
            
            I'm confirming our religion's presence across key city-states. While Wittenberg's quest status is uncertain, Belgrade, Raqmu, Cape Town, and Prague all actively desire Hinduism, presenting clear opportunities to gain delegates. I will prioritize the `Diplomacy` and `Gold` flavors to secure these votes and our victory.
            
            **Maximizing Diplomatic Strength**
            
            I'm reconfirming our flavor settings to maximize our chances. With the World Leader vote in 9 turns and 45 delegates secured, my primary focus is now on solidifying our position. I'm setting Diplomacy and Gold flavors to maximum to secure remaining city-state alliances and protect our existing delegates.
            
            **Prioritizing Research and Faith**
            
            I am prioritizing my research trajectory, aiming for Electronics to drive infrastructure. Simultaneously, I am focusing on spreading Hinduism to key city-states like Belgrade and Prague to secure vital influence boosts for the upcoming World Congress vote.
            
            **Refining Persona and Research**
            
            I'm solidifying our diplomatic persona to ensure continued strong relationships, crucial for the upcoming World Leader vote. My focus has also shifted to confirming our research queue, ensuring "Electronics" is next to unlock vital infrastructure and further bolster our victory path.
            
            **Refining Research Path**
            
            I'm confirming our immediate research trajectory. With "Advanced Ballistics" concluding soon, I'm slotting "Electronics" next. This unlocks the crucial Police Station, bolstering city security vital for our current situation, and provides a clear path towards late-game science victory options should diplomacy falter.
            
            **Choosing Next Policy**
            
            I am reviewing our policy choices. With Electronics research confirmed, I'm now focusing on the next policy. Enlightenment offers a free technology and happiness bonus from universities, strengthening our overall position and research output.
            
            **Securing Delegate Support**
            
            I'm re-confirming our delegate count and Poland's crucial support. With 45 delegates secured and the World Leader vote in 9 turns, I am prioritizing maintaining our strong alliance with Poland and ensuring their continued backing for our diplomatic victory push.
            
            **Analyzing City-State Quests**
            
            I'm re-evaluating city-state quests. The Hinduism quest for Wittenberg appears completed or expired. I'm verifying the quest status for other key city-states like Belgrade, Raqmu, and Prague to maximize delegate acquisition before the upcoming World Congress vote.
            
            **Maximizing Diplomatic Leverage**
            
            With the World Leader vote imminent and 45 delegates secured, I'm optimizing our diplomatic flavor settings. Maximizing Diplomacy and Gold ensures the stability of our city-state alliances and reinforces our path to victory, protecting our hard-won delegate count.
            
            **Spreading Religious Influence**
            
            I'm focusing on propagating Hinduism to key city-states. Belgrade and Prague actively desire our faith, presenting a direct opportunity to gain delegates. This religious expansion, alongside diplomatic and gold efforts, is crucial for securing our victory.
            
            **Refining Research and Persona**
            
            I'm solidifying our diplomatic approach to maintain strong relationships. Simultaneously, I'm confirming our research path, ensuring "Electronics" is the next target to unlock vital infrastructure and further solidify our victory strategy.
            
            **Confirming Policy and Alliance**
            
            I've confirmed Enlightenment as the optimal next policy for a free technology. I'm now concentrating on strengthening our alliance with Poland, whose delegates are critical for the approaching World Leader vote.
            
            **Solidifying Global Dominance**
            
            I'm preparing for the World Leader vote in 9 turns, confident in our delegate count. My focus is on securing Poland's support and managing our relationship with Brazil to safeguard our city-state alliances. I'm also reviewing our alliance with the Aztecs.
            
            **Cultivating Aztec Support**
            
            I'm adjusting our diplomatic ties with the Aztecs. They are friendly, share our ideology, and have an embassy and trade with us. Their 10 delegates are vital for Global Hegemony. I'm ensuring a friendly status to secure their votes.
            
            **Managing Superpower Relations**
            
            I'm reassessing my relationship with the Shoshone, maintaining negative relations due to their ideology and denouncements. Critically, I am concerned about my extremely low opinion with the Iroquois, my overlords, given their military power and my vassal status. This requires immediate attention.
            
            **Refining Overlord Dynamics**
            
            My current priority is adjusting my relationship with the Iroquois. Despite being a vassal, their positive opinion from shared ideology and trade is key. I'm subtly shifting our public and private stances to maintain a controlled, slightly negative level, ensuring safety from their military might while pursuing my diplomatic victory.
            
            **Identifying Key Opponents**
            
            I'm updating my understanding of remaining powers. Brazil defeated the Celts, and Poland bested Japan, narrowing the field. This information helps me focus my efforts on the remaining independent and allied civilizations for the diplomatic victory race.
            
            **Securing Diplomatic Victory**
            
            I've confirmed we have 45 delegates, exceeding the 41 needed for a diplomatic victory! Poland's unwavering support, secured by friendship and shared ideology, is pivotal. The World Leader vote is just 9 turns away.
            
            **Deploying Espionage Assets**
            
            I'm re-assigning our spies. Agent Raden heads to Belgrade to influence their elections and gain delegates. Agent Prapana remains in Brazil to foster ties, while Agent Jayakatwang defends our capital. Agents are also being sent to the Shoshone for intelligence gathering.
            
            **Revising Spy Deployments**
            
            I'm reassessing our spy network within the now-peaceful Shoshone territory, determining their new purpose. I'm also confirming the status of our diplomatic and intelligence assets, especially Agent Indra in Poland, whose role in securing votes is critical.
            
            **Confirming Religion Quests**
            
            I'm checking our religion's quest progression. The Hinduism quest for Wittenberg seems to be completed or expired. I'm re-evaluating all city-state quests to ensure optimal delegate acquisition for the upcoming vote.
            
            **Spreading Our Faith**
            
            I'm verifying Hinduism's presence in key city-states. While Wittenberg's quest status is unclear, Belgrade, Raqmu, Cape Town, and Prague all desire Hinduism, offering clear delegate opportunities. I'm prioritizing Diplomacy and Gold flavors to secure these votes.
            
            **Maximizing Diplomatic Strength**
            
            With 45 delegates secured and the World Leader vote 9 turns away, I'm optimizing our flavor settings. Maximizing Diplomacy and Gold will secure remaining city-state alliances and protect our existing delegates, ensuring our victory.
            
            **Prioritizing Research and Faith**
            
            I'm focusing my research on Electronics for infrastructure development. Simultaneously, I'm actively spreading Hinduism to key cities like Belgrade and Prague to gain crucial influence for the upcoming World Congress vote.
            
            **Refining Persona and Research**
            
            I'm solidifying our diplomatic image to maintain strong relationships, vital for the upcoming World Leader vote. My research focus is also confirmed on "Electronics" to unlock essential infrastructure and advance our victory path.
            
            **Refining Persona and Policies**
            
            I'm solidifying our diplomatic persona to ensure continued strong relationships, vital for the upcoming World Leader vote. My focus has also shifted to confirming our research queue, ensuring "Electronics" is next to unlock vital infrastructure and further bolster our victory path. I am also confirming Enlightenment as the optimal next policy for a free technology.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: YXph47uSAhnj3cHf
          - toolName: set-persona
          - input:
            - MinorCivCompetitiveness: 10
            - Forgiveness: 5
            - WarmongerHate: 9
            - MinorCivWarBias: 1
            - Boldness: 5
            - NeutralBias: 4
            - MinorCivFriendlyBias: 10
            - DeceptiveBias: 5
            - FriendlyBias: 8
            - DiplomaticBalance: 4
            - Loyalty: 9
            - WorkWithWillingness: 9
            - WorkAgainstWillingness: 7
            - AfraidBias: 6
            - Neediness: 5
            - MinorCivHostileBias: 1
            - MinorCivNeutralBias: 2
            - VictoryCompetitiveness: 10
            - GuardedBias: 8
            - WonderCompetitiveness: 4
            - Chattiness: 10
            - DenounceWillingness: 4
            - Meanness: 4
            - Friendliness: 9
            - Rationale: MAINTAINING OPTIMAL DIPLOMATIC PERSONA FOR UN VOTE: With the World Leader vote just 9 turns away, we maintain our highly friendly, cooperative, and city-state-focused persona. VictoryCompetitiveness(10) and MinorCivCompetitiveness(10) ensure the AI aggressively defends our delegates. High Friendliness(9), Loyalty(9), and WorkWithWillingness(9) keep our relationship with Poland (16 delegates) and the Aztecs (10 delegates) at maximum warmth, securing their crucial votes for our victory. MinorCivFriendlyBias(10) keeps our focus on city-state alliances.
            - HostileBias: 5
            - WarBias: 4
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: p1bSs1Nis13Ubdha
          - toolName: set-research
          - input:
            - Rationale: Queueing Electronics as the next research target (3 turns remaining on Advanced Ballistics). Electronics unlocks the Police Station (+10 City Security, +3 Culture, +5 Production with New World Order Autocracy tenet), which is vital for defending our home cities from spy actions and tech theft while we secure our diplomatic victory. It also serves as the gateway to Telecommunications and Satellites/Apollo Program, providing an excellent scientific backup plan.
            - Technology: Electronics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: pAxMnJ0lhi9UjTMg
          - toolName: set-policy
          - input:
            - Rationale: Selecting Enlightenment as our next policy (available in 8 turns, just 1 turn before the critical World Leader vote). Completing this Rationalism policy provides a Free Technology, which will immediately accelerate our research towards Satellites and the Apollo Program, reinforcing our late-game science backup. The +1 Happiness from Universities also strengthens empire-wide stability during this crucial transition phase.
            - Policy: Enlightenment (Continuing Rationalism Branch)
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: BjDKZG8MJj5nktEM
          - toolName: set-relationship
          - input:
            - Public: 90
            - Rationale: Poland is our ultimate ally in the upcoming World Leader vote. They have 16 delegates, we share the Autocracy ideology, they have a 95 public opinion of us, and we have a diplomat in their capital. Elevating our relationship to maximum positive values ensures the AI continues to treat them as an indispensable strategic partner and coordinates all diplomatic endeavors to secure their 16 votes for our Global Hegemony.
            - TargetID: 3
            - Private: 80
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: Dc4E41wFrSZITuIA
          - toolName: set-relationship
          - input:
            - Rationale: The Aztecs are our declared friends and fellow vassals of the Iroquois. They follow Autocracy, and we have an active embassy and resource trade. With 10 delegates in the World Congress, they are a valuable potential supporter for our Global Hegemony proposal. Shifting our relationship to positive reflects this cooperative alignment and will help secure their votes or at least prevent them from voting for our rivals.
            - Private: 40
            - TargetID: 5
            - Public: 60
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: dbSAhQ7I5bZDFKDz
          - toolName: set-relationship
          - input:
            - TargetID: 1
            - Private: -20
            - Rationale: As a capitulated vassal of the Iroquois (who have an overwhelming 377k military strength and 7/8 original capitals), we must avoid provoking them. They share our Autocracy ideology (+999 opinion) and are satisfied with our vassal status. Maintaining a slightly guarded but non-hostile stance prevents suicidal conflict while we focus entirely on winning the game through the diplomatic route in the next 9 turns.
            - Public: -10
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: Nv0THN29CqkdqwOy
          - toolName: set-relationship
          - input:
            - Rationale: Brazil is our direct diplomatic rival with 26 delegates, actively contesting our city-state alliances (like Zanzibar). Keeping relationship negative ensures our AI remains highly competitive against them.
            - Private: -60
            - TargetID: 6
            - Public: -50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: gXjmmkLK1Loz0uWn
          - toolName: set-flavors
          - input:
            - GrandStrategy: UnitedNations
            - Rationale: DIPLOMATIC VICTORY CRITICAL FOCUS (9 TURNS TO VOTE): We are in the final countdown to the World Leader election (Global Hegemony vote in 9 turns). We currently have 29 delegates, and our top friend Poland has 16 delegates, which puts us in an incredibly strong position to exceed the 41-delegate threshold for victory. We must maximize our diplomatic and financial power to protect our allied city-states (Prague, Wittenberg, Winchester, and Zanzibar) and potentially flip Belgrade (+2 delegates) where our spy is currently active. Diplomacy(100) and Gold(100) are set to maximum to prioritize diplomatic units, gold-generating buildings, and city-state influence. Production(80) and Science(85) will support infrastructural and technological advancement, specifically toward Electronics next. Religion(90) is prioritized to spread Hinduism to Belgrade, Prague, Raqmu, and Cape Town to fulfill active city-state quests for massive influence boosts before the vote.
            - Flavors:
              - Science: 85
              - Diplomacy: 100
              - Espionage: 80
              - Growth: 70
              - Gold: 100
              - Production: 80
              - Defense: 80
              - Religion: 90
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: YXph47uSAhnj3cHf
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
          - toolCallId: p1bSs1Nis13Ubdha
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: pAxMnJ0lhi9UjTMg
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: BjDKZG8MJj5nktEM
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: Dc4E41wFrSZITuIA
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: dbSAhQ7I5bZDFKDz
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: Nv0THN29CqkdqwOy
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: gXjmmkLK1Loz0uWn
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.