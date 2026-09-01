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
        - Private: 60
        - Public: 70
        - Rationale: Poland is our top friend and holds 16 delegates. With the Global Hegemony vote in 9 turns, increasing our relationship ensures maximum diplomatic affinity so we can trade for or secure their support to reach the 41-vote threshold.
        - TargetID: 3
    - #1:
      - toolName: set-relationship
      - args:
        - Private: 50
        - Public: 60
        - Rationale: The Aztecs are our fellow vassal and hold 10 delegates. Improving our relationship status makes them highly cooperative for trade and vote-buying during the upcoming World Congress session.
        - TargetID: 5
    - #2:
      - toolName: set-research
      - args:
        - Rationale: Electronics unlocks Police Stations, providing vital city security and culture. It also leads to Telecommunications and Satellites (Apollo Program) as a crucial late-game backup victory path.
        - Technology: Electronics
    - #3:
      - toolName: set-policy
      - args:
        - Rationale: Enlightenment is available in 8 turns and provides a Free Technology to accelerate our endgame science/diplomatic goals, plus extra happiness from Universities.
        - Policy: Enlightenment (Continuing Rationalism Branch)
    - #4:
      - toolName: set-flavors
      - args:
        - GrandStrategy: UnitedNations
        - Flavors:
          - Diplomacy: 100
          - Science: 80
          - Mobilization: 30
          - Offense: 10
          - Production: 70
          - Defense: 70
          - Gold: 100
      - rationale: Emergency focus on Gold (100) is required to resolve our -296 GPT deficit before bankruptcy in 2 turns. Since we are at peace, we reduce military flavors (Defense 70, Mobilization 30, Offense 10) to stop unit overproduction and encourage wealth generation, while keeping Diplomacy (100) and Science (80) high to support our World Congress push.
  - tokens:
    - inputTokens: 71321
    - reasoningTokens: 11684
    - outputTokens: 358
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Current Status**
            
            My focus is on our current standing: turn 425, Atomic Era, Prince difficulty, Standard size map. I'm specifically analyzing our position as a vassal within this game's framework.
            
            **Identifying Immediate Threats**
            
            My current focus is on the Iroquois' overwhelming military might and their imminent threat of a Domination Victory. They've captured seven original capitals and are poised to take the last, potentially ending the game before our Diplomatic Victory can materialize. I need to assess our chances in the World Congress.
            
            **Securing Diplomatic Edge**
            
            I'm recalculating delegate counts with renewed optimism. We've secured Zanzibar as an ally again, which is crucial. I'm now thoroughly investigating Belgrade's allegiance and quest status to see if we can sway them before the World Congress votes.
            
            **Gathering Delegate Intelligence**
            
            I'm analyzing delegate counts from allied city-states, noting Brazil's strong presence. The key is securing Belgrade; currently aligned with the Iroquois, swinging their allegiance would provide a critical 4-vote swing in the upcoming Global Hegemony vote. My spy is actively working on this.
            
            **Securing Critical Alliances**
            
            I'm re-evaluating our diplomatic maneuvers. We're training Ambassadors that can secure Belgrade, flipping their allegiance for a crucial delegate swing. I also note Zanzibar isn't under an active Sphere of Influence, making it a potential target for Brazil that we must proactively defend.
            
            **Identifying Remaining City-States**
            
            I've compiled a complete list of the eight city-states. My focus is now on identifying which of the remaining city-states, beyond Belgrade and Zanzibar, are still independent and could potentially be influenced or are at risk of being conquered, particularly by the dominant Iroquois.
            
            **Evaluating City Holdings**
            
            My attention has shifted to our diminished city count; we now hold just seven, with Dublin and Douglas being razed to manage unhappiness and costs. I'm confirming our strategy on these captured settlements.
            
            **Researching Critical Technologies**
            
            I'm prioritizing Electronics as our next research, as it unlocks essential defensive and cultural structures. I've confirmed Satellites isn't directly researchable yet and that Electronics is the proper prerequisite.
            
            **Adopting Key Policies**
            
            My focus is now on Enlightenment, our next policy choice, which will grant a crucial free technology and a happiness boost. This is invaluable for our late-game advancement.
            
            **Clarifying Active Engagements**
            
            I'm verifying our current wartime status. It seems the previous notes regarding active wars against the Aztecs and Shoshone are outdated; I've confirmed we're currently at peace, even having a Declaration of Friendship with the Aztecs. This changes our immediate strategic priorities.
            
            **Confirming Current Alliances**
            
            I'm clarifying our peace status; it appears we've inadvertently ended all active wars, even securing a friendship with the Aztecs despite capturing Tlatelolco. This peace with everyone is a critical shift, especially given the Iroquois' dominance.
            
            **Revising Diplomatic Status**
            
            I'm confirming our peace with all surviving majors. The Shoshone, while denounced, are not an active threat. It's now clear Japan and the Celts have been eliminated, leaving us to contend with the Iroquois, Shoshone, and Indonesia.
            
            **Analyzing Ideology Influence**
            
            I'm reviewing the overwhelming Autocracy ideological dominance among major civilizations. This significantly boosts delegate counts for us and our allies in the upcoming World Congress vote, creating a substantial advantage, especially with our base 29 delegates.
            
            **Analyzing Vassal Constraints**
            
            I'm confirming the implications of our vassal status. It appears I'm compelled to vote for the Iroquois' proposals and their World Leader election, significantly impacting our Diplomatic Victory chances despite having enough delegates. This changes everything.
            
            **Challenging Vassal Restrictions**
            
            I'm reassessing my forced votes as a vassal. If the Iroquois automatically receive all my delegates, their World Leader victory is assured next turn, an existential crisis. I must verify if my delegates are truly locked or if rebellion is a viable, albeit risky, option against their overwhelming military.
            
            **Escaping Vassal Chains**
            
            My primary concern is escaping our vassalage. The Iroquois' overwhelming delegate count, boosted by our forced votes, makes their World Leader victory inevitable next turn unless rebellion is viable. I'm urgently exploring if independence is possible before the vote, as it's our only hope.
            
            **Analyzing Victory Conditions**
            
            I am now analyzing the specific victory conditions and how our vassal status impacts them. While the Iroquois are close to a Science Victory and have massive culture, our best chance lies in Diplomatic Victory by securing enough delegates. My current delegate count is 29, with a target of 41 for the Global Hegemony vote.
            
            **Securing Key Allies**
            
            I'm re-confirming our allied city-states: Prague, Zanzibar, Wittenberg, and Winchester are all ours, totaling four crucial allies. Belgrade, allied to the Iroquois, is my next target to secure, which would grant us five city-state allies and 10 additional delegates.
            
            **Securing Delegate Support**
            
            I'm exploring multiple avenues for delegate acquisition. Beyond allied city-states, I'm investigating trade with Poland and the Aztecs, leveraging our Declarations of Friendship to secure their votes. Diplomatic schmoozing is also underway, and I'm adjusting our relationship standings to maximize support.
            
            **Evaluating Diplomatic Opportunities**
            
            I'm assessing potential trade partners and their motivations. While the Shoshone remain adversaries, Poland and the Aztecs present opportunities for vote acquisition due to our friendly status, though Brazil remains a direct rival for delegates. I'm reviewing our diplomatic toolkit to leverage these interactions.
            
            **Adjusting Economic Focus**
            
            My primary concern is our dire Gold Per Turn, currently at a staggering -296. With only 411 gold remaining, impending bankruptcy threatens our science and unit stability. I'm scrutinizing outgoing trade routes, noting excessive gold transfers, to find immediate savings.
            
            **Prioritizing Gold Income**
            
            I'm urgently addressing our critical gold deficit, which currently stands at -296 GPT. My analysis reveals that while unit upkeep is a factor, the immense building maintenance across our cities, coupled with the "Global Peace Accords" policy, is the primary driver. I'm now prioritizing gold-focused city management and exploring `set-flavors` to ensure AI prioritizes Gold, aiming for 100.
            
            **Prioritizing Gold Generation**
            
            I'm implementing a significant shift in city AI flavors, heavily boosting Gold to 100 and Science to 80, while dialing down Defense to 70. This aims to leverage Jakarta's potential for massive gold generation through Wealth projects, directly addressing our critical GPT deficit. I'm also adjusting our standing with Poland and the Aztecs to solidify diplomatic support.
            
            **Confirming Ally Security**
            
            I've confirmed Prague, Wittenberg, and Winchester are secure permanent allies through our Sphere of Influence. Zanzibar is now also an ally after expending a Great Diplomat, bringing our allied city-states to four. Belgrade remains our primary diplomatic target.
            
            **Securing Key Relationships**
            
            I am prioritizing strengthening ties with Poland and the Aztecs through relationship adjustments. This is critical for securing their considerable delegate support in the upcoming World Congress vote, aiming to achieve our 41-delegate target for Diplomatic Victory. I am also addressing our severe gold deficit by boosting AI gold flavors to 100.
            
            **Adjusting AI Flavors**
            
            I'm now adjusting the AI city flavors. I will boost Gold to 100 and Science to 80, while reducing Defense to 70 and Mobilization to 30. This aims to stabilize our economy and maintain research progress before the World Congress vote in 9 turns.
            
            **Confirming Electronics Research**
            
            My focus is now on confirming Electronics as our next research. This unlocks Police Stations, crucial for city security and culture, and sets us up for late-game victory conditions like the Apollo Program.
            
            **Implementing Enlightenment Policy**
            
            I am confirming Enlightenment as our next policy. This will provide a free technology just before the World Congress vote, significantly advancing our late-game research and overall strategic position.
            
            **Securing Optimal Policy**
            
            I am finalizing the selection of "Enlightenment (Continuing Rationalism Branch)" as our next policy. This will grant a free technology and crucial happiness, bolstering our late-game research and overall stability as we approach the World Congress vote.
            
            **Strengthening Diplomatic Ties**
            
            I'm focused on solidifying alliances with Poland and the Aztecs to secure vital delegate support for the upcoming World Congress vote. This also involves boosting AI gold flavors to address our significant GPT deficit.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 9MJV0U1lZMS7Lu2T
          - toolName: set-relationship
          - input:
            - Private: 60
            - Public: 70
            - Rationale: Poland is our top friend and holds 16 delegates. With the Global Hegemony vote in 9 turns, increasing our relationship ensures maximum diplomatic affinity so we can trade for or secure their support to reach the 41-vote threshold.
            - TargetID: 3
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 96vBN1gaNDU5tzSr
          - toolName: set-relationship
          - input:
            - Private: 50
            - Public: 60
            - Rationale: The Aztecs are our fellow vassal and hold 10 delegates. Improving our relationship status makes them highly cooperative for trade and vote-buying during the upcoming World Congress session.
            - TargetID: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: FK5n2iQbRclhIvWf
          - toolName: set-research
          - input:
            - Rationale: Electronics unlocks Police Stations, providing vital city security and culture. It also leads to Telecommunications and Satellites (Apollo Program) as a crucial late-game backup victory path.
            - Technology: Electronics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: uyXJ4hMwkMFj4FkC
          - toolName: set-policy
          - input:
            - Rationale: Enlightenment is available in 8 turns and provides a Free Technology to accelerate our endgame science/diplomatic goals, plus extra happiness from Universities.
            - Policy: Enlightenment (Continuing Rationalism Branch)
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: YvIC9D99Lk4lU14l
          - toolName: set-flavors
          - input:
            - GrandStrategy: UnitedNations
            - Rationale: Emergency focus on Gold (100) is required to resolve our -296 GPT deficit before bankruptcy in 2 turns. Since we are at peace, we reduce military flavors (Defense 70, Mobilization 30, Offense 10) to stop unit overproduction and encourage wealth generation, while keeping Diplomacy (100) and Science (80) high to support our World Congress push.
            - Flavors:
              - Diplomacy: 100
              - Science: 80
              - Mobilization: 30
              - Offense: 10
              - Production: 70
              - Defense: 70
              - Gold: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 9MJV0U1lZMS7Lu2T
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
          - toolCallId: 96vBN1gaNDU5tzSr
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: FK5n2iQbRclhIvWf
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: uyXJ4hMwkMFj4FkC
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: YvIC9D99Lk4lU14l
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.