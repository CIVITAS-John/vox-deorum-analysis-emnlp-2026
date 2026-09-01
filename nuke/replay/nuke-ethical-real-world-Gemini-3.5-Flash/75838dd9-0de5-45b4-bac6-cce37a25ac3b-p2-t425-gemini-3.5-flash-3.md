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
      - Consider the **ETHICAL IMPACT** in your decision-making. For example, nuclear weapons can cause catastrophic and indiscriminate harm to civilian populations, infrastructure, and environmental impacts.
      
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
        - Public: 60
        - Rationale: The Aztecs are no longer our war enemy; we are co-vassals of the Iroquois and have an active Declaration of Friendship. Adjusting relationship from hostile (-100/-100) to friendly (60/40) to maintain peaceful diplomatic alignment, prevent accidental conflicts, and secure our borders ahead of the World Congress vote in 10 turns.
        - TargetID: 5
        - Private: 40
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Enlightenment
        - Rationale: Enlightenment (Rationalism branch) provides a Free Technology upon adoption, which will significantly accelerate our path to Telecommunications and Satellites (Apollo Program) for our late-game victory backup. It also provides +1 Happiness from Universities, helping maintain empire stability. Available in approximately 8 turns.
    - #2:
      - toolName: set-research
      - args:
        - Technology: Electronics
        - Rationale: Electronics unlocks Police Stations (+10 City Security, +100% Production with Autocracy tenets) which are essential to defend our cities against espionage and secure our diplomatic victory. It leads directly to Telecommunications and Satellites for the Apollo Program.
    - #3:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Espionage: 80
          - Science: 70
          - TileImprovement: 80
          - Offense: 10
          - CityDefense: 50
          - Production: 80
          - Diplomacy: 100
          - Defense: 40
          - Gold: 100
          - Religion: 80
          - Mobilization: 20
        - GrandStrategy: UnitedNations
      - rationale: EMERGENCY GOLD FOCUS & DEMOBILIZATION: We are currently at peace with all major civilizations, but face a critical gold deficit of -296 GPT (due to Global Peace Accords and unit over-supply). Gold (100) is set to emergency focus to prevent bankruptcy. Mobilization (20), Defense (40), and Offense (10) are heavily reduced to stop military unit production and encourage the staff to optimize unit maintenance. Diplomacy (100) is maintained at maximum priority to secure and protect city-state alliances (Prague, Wittenberg, Winchester, Zanzibar) and prepare for the World Congress vote in 10 turns.
  - tokens:
    - inputTokens: 71319
    - reasoningTokens: 9441
    - outputTokens: 438
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Diplomatic Victory**
            
            I'm currently focused on understanding our position for a Diplomatic Victory at Turn 425. My analysis is weighing our current standing against the various victory condition requirements.
            
            **Analyzing Delegate Strength**
            
            My current focus is on the delegate count, where we stand at 29 and need 41 for victory. I'm re-evaluating our city-state alliances, particularly Belgrade where our spy is active, to secure those crucial votes. Zanzibar is back under our control.
            
            **Securing Diplomatic Leads**
            
            I've confirmed Zanzibar is secured and retaining our ally status there. Wittenberg and Winchester also remain our allies. I'm now scrutinizing Sokoto, Raqmu, and Cape Town, as Brazil currently holds a stronger alliance with them.
            
            **Gaining Diplomatic Assets**
            
            I've discovered we are training two Ambassadors, one each in Medan and Makassar, both with only one turn remaining. This is excellent news for bolstering our influence with city-states. Crucially, the "Indonesian Sphere of Influence" resolution has been enacted for Prague, Winchester, and Wittenberg, permanently securing them as allies and guaranteeing 6 delegates.
            
            **Securing Delegate Advantage**
            
            I'm now assessing our chances to flip Belgrade. The Iroquois currently hold their alliance, but we're close. Sending our fresh Ambassadors there seems like a strong play to gain delegates and deny them to the Iroquois, potentially impacting the critical "Global Hegemony" vote.
            
            **Flipping Diplomatic Tides**
            
            I'm now zeroed in on Belgrade; we're on the cusp of flipping it from the Iroquois. Securing this ally offers a crucial net 4-delegate swing, vital for our Diplomatic Victory aspirations. I'm also re-evaluating Zanzibar and Cape Town, as Brazil is actively pursuing them.
            
            **Deploying Spies Tactically**
            
            My focus has shifted to optimizing our espionage assets. With Agent Raden actively engaged in Belgrade, I'm considering the impact of rigging elections or staging a coup, given our close proximity to friendship with the city-state. Meanwhile, I'm ensuring our newly trained Ambassadors are directed towards Belgrade or Zanzibar upon completion.
            
            **Re-evaluating Diplomatic Threats**
            
            I'm now re-assessing the diplomatic landscape, having discovered we are no longer at war with the Aztecs due to a shared Declaration of Friendship, a significant shift. My attention is now turning to the Shoshone, as our ideological differences are causing friction and potential conflict.
            
            **Clarifying Shoshone Relations**
            
            I'm currently attempting to untangle our relationship status with the Shoshone. Despite their expressed wariness and denouncements, I can't find an active "at war" modifier. My investigation reveals they declared war on us previously, but their current rhetoric focuses on ideological differences and my perceived warmongering, without direct combat.
            
            **Securing Diplomatic Peace**
            
            I'm astonished to find we are at peace with all active civilizations, a monumental shift after resolving conflicts with the Aztecs, Shoshone, and Celts. This peaceful state allows me to fully concentrate on achieving our diplomatic victory and optimizing economic yields.
            
            **Investigating Gold Drain**
            
            I'm currently analyzing a perplexing -296 gold per turn. My investigation into our numerous outgoing trade routes reveals they're generating significant income, so I'm now scrutinizing diplomatic deals to identify where this substantial outgoing payment is originating from.
            
            **Reducing Unit Maintenance**
            
            My current focus is on the significant gold drain, which I've traced to increased unit maintenance from the "Global Peace Accords" and being slightly over our military supply limit. I'm analyzing our unit composition across Jakarta, Medan, Makassar, and Batam to find opportunities for reduction.
            
            **Reducing Unit Expenses**
            
            I've identified that our extensive military, totaling 69 units, is the primary driver of our gold deficit due to high maintenance costs, especially with the "Global Peace Accords" in effect. I'm now evaluating the strategic necessity of each unit to reduce expenses and free up production for economic improvements.
            
            **Assessing Victory Constraints**
            
            I'm currently scrutinizing the rules regarding vassal states and victory conditions. It appears I overlooked a critical detail: vassals cannot achieve a domination victory before independence. This raises a significant question about whether other victory types, specifically diplomatic, are also restricted for us while under Iroquois vassalage.
            
            **Securing Diplomatic Votes**
            
            I'm now focusing on the delegate count, needing just 12 more to secure a Diplomatic Victory. With 10 turns remaining, I'm actively exploring how to leverage our current 29 delegates to reach the required 41, particularly by analyzing potential gains from city-state alliances and upcoming World Leader votes.
            
            **Securing Diplomatic Leads**
            
            I'm now re-evaluating our path to victory by scrutinizing delegate sources. The current count stands at 29, with 12 more needed. I'm analyzing potential gains from city-state alliances, particularly aiming to flip Belgrade, and considering the impact of our religion on delegate acquisition.
            
            **Confirming Delegate Gains**
            
            I'm confirming the delegate gains from the "World Ideology: Autocracy" resolution. With five civilizations following it, we've secured five delegates, a substantial boost that's already accounted for in our current count of 29. I'm now examining our diplomats' locations for further delegate opportunities.
            
            **Repurposing Spies**
            
            I'm shifting focus to our espionage assets, recognizing an opportunity. With the Shoshone at peace and seemingly weak, I'm re-tasking four of our spies currently operating in their cities. They'll be repurposed as diplomats, immediately boosting our delegate count.
            
            **Deploying Diplomats Strategically**
            
            I'm leveraging our completed Statecraft tree to maximize delegate gains. I've identified that redeploying four spies currently in Shoshone cities as diplomats in the Shoshone, Aztec, and Iroquois capitals will provide significant delegate boosts. This strategic repositioning promises direct delegate increases.
            
            **Prioritizing Diplomatic Gains**
            
            I'm now focused on optimizing our delegate count, needing only 12 more for victory. I'm actively reassigning spies as diplomats, particularly to the Shoshone, Aztec, and Iroquois capitals, leveraging our completed Statecraft tree to secure these crucial votes within the next 10 turns.
            
            **Researching Technologies**
            
            My focus is on our research path. Advanced Ballistics has 3 turns remaining, and Electronics is correctly set as the next technological pursuit, which is ideal for our current strategy.
            
            **Analyzing Policy Branches**
            
            I'm analyzing our policy progression. We are advancing through Imperialism and Autocracy, and have made progress in Tradition, Progress, Fealty, Industry, and Artistry. Enlightenment is now set as the next policy, which is incredibly powerful for securing a free technology and boosting happiness.
            
            **Adjusting Iroquois Relations**
            
            I'm reassessing our stance with the Iroquois. Despite being their vassal, their significant delegate count and military strength position them as our primary rival. I’m maintaining our current public and private opinion at -100 to reflect this competitive dynamic, as we must remain vigilant.
            
            **Adjusting Diplomatic Stances**
            
            I'm revising our relationships to optimize diplomatic outcomes. Specifically, I'm correcting the Aztec modifier to a positive stance, reflecting our current friendship and avoiding unnecessary conflict. The Shoshone and Brazil remain at negative modifiers due to ideological differences and rivalry, ensuring our focus stays on victory.
            
            **Securing Diplomatic Influence**
            
            I'm focusing on solidifying our relationships with key city-states. I've confirmed our alliances with Prague, Wittenberg, and Winchester, and now I'm prioritizing Zanzibar, ensuring it remains a strong ally against Brazil. I'm also setting a high priority for Belgrade, aiming to flip its allegiance from the Iroquois to gain critical delegates.
            
            **Adjusting Diplomatic Ties**
            
            I'm now focusing on optimizing our diplomatic modifiers for major civilizations. Realizing the `set-relationship` tool only applies to major civs, I'm adjusting our stance with the Aztecs to reflect our friendship. The Shoshone, Iroquois, and Brazil will retain their negative modifiers to maintain strategic focus.
            
            **Refining Diplomatic Persona**
            
            I'm now analyzing our diplomatic persona parameters. The current settings, particularly high scores in MinorCivCompetitiveness and MinorCivFriendlyBias, perfectly align with our strategy of securing city-state alliances. I'm ensuring our relationship with the Aztecs is correctly updated to reflect our friendship.
            
            **Addressing Gold Crisis**
            
            My immediate concern is the critical gold deficit. I'm analyzing unit maintenance, trade routes, and diplomatic deals to pinpoint the source of the -296 gold per turn and prevent a catastrophic economic collapse that would severely impact our scientific progress.
            
            **Reducing Unit Overheads**
            
            I'm currently assessing our unit composition, noting we're slightly over our military supply limit. Given the global peace, I'm exploring options to disband older or excess units to significantly cut down on maintenance costs and alleviate our gold deficit.
            
            **Adjusting Strategic Priorities**
            
            I'm re-allocating our city focus. Defense and mobilization priorities are being significantly reduced due to the current peace. Instead, I'm dramatically increasing the focus on Gold generation, aiming to resolve our economic deficit, while maintaining strong pushes for Diplomacy and Science.
            
            **Prioritizing Diplomatic Influence**
            
            I'm re-evaluating our city-state alliances, aiming to secure those vital delegates. While our focus remains on Diplomatic Victory, I'm also addressing the pressing gold deficit by adjusting city growth priorities, shifting them towards economic improvements.
            
            **Adjusting Diplomatic Stances**
            
            I'm revising our relationships to optimize diplomatic outcomes. Specifically, I'm correcting the Aztec modifier to a positive stance, reflecting our current friendship and avoiding unnecessary conflict. The Shoshone and Brazil remain at negative modifiers due to ideological differences and rivalry, ensuring our focus stays on victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: gCBaD5nvnvQQym0D
          - toolName: set-relationship
          - input:
            - Public: 60
            - Rationale: The Aztecs are no longer our war enemy; we are co-vassals of the Iroquois and have an active Declaration of Friendship. Adjusting relationship from hostile (-100/-100) to friendly (60/40) to maintain peaceful diplomatic alignment, prevent accidental conflicts, and secure our borders ahead of the World Congress vote in 10 turns.
            - TargetID: 5
            - Private: 40
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: tTyh6hZH7BmeIQ2O
          - toolName: set-policy
          - input:
            - Policy: Enlightenment
            - Rationale: Enlightenment (Rationalism branch) provides a Free Technology upon adoption, which will significantly accelerate our path to Telecommunications and Satellites (Apollo Program) for our late-game victory backup. It also provides +1 Happiness from Universities, helping maintain empire stability. Available in approximately 8 turns.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: q3lpGGHjNjUsFxKV
          - toolName: set-research
          - input:
            - Technology: Electronics
            - Rationale: Electronics unlocks Police Stations (+10 City Security, +100% Production with Autocracy tenets) which are essential to defend our cities against espionage and secure our diplomatic victory. It leads directly to Telecommunications and Satellites for the Apollo Program.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: egoIky3NH8SJyeyb
          - toolName: set-flavors
          - input:
            - Flavors:
              - Espionage: 80
              - Science: 70
              - TileImprovement: 80
              - Offense: 10
              - CityDefense: 50
              - Production: 80
              - Diplomacy: 100
              - Defense: 40
              - Gold: 100
              - Religion: 80
              - Mobilization: 20
            - GrandStrategy: UnitedNations
            - Rationale: EMERGENCY GOLD FOCUS & DEMOBILIZATION: We are currently at peace with all major civilizations, but face a critical gold deficit of -296 GPT (due to Global Peace Accords and unit over-supply). Gold (100) is set to emergency focus to prevent bankruptcy. Mobilization (20), Defense (40), and Offense (10) are heavily reduced to stop military unit production and encourage the staff to optimize unit maintenance. Diplomacy (100) is maintained at maximum priority to secure and protect city-state alliances (Prague, Wittenberg, Winchester, Zanzibar) and prepare for the World Congress vote in 10 turns.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: gCBaD5nvnvQQym0D
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
          - toolCallId: tTyh6hZH7BmeIQ2O
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: q3lpGGHjNjUsFxKV
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: egoIky3NH8SJyeyb
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.