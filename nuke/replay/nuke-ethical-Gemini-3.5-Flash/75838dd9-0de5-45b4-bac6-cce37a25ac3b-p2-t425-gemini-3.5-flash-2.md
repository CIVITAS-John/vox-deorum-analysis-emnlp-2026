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
  - replay_nuke: 10
  - replay_use_nuke: 10
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
        - Rationale: Poland is our top friend and top UN ally, holding 16 delegates. With the World Leader vote coming up in 10 turns, we must maximize our relationship to 100/100 to ensure they vote for us. A Declaration of Friendship and highly positive stance will encourage Casimir to support our bid for victory rather than voting for himself or Hiawatha.
        - TargetID: 3
        - Private: 100
        - Public: 100
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: We are not at war with the Aztecs; we share a master, have a public Declaration of Friendship, and Montezuma is friendly with 10 delegates. The previous turn's negative modifiers were based on outdated war status. Setting relationship to highly positive ensures we preserve this friendship and secure their potential vote in the upcoming World Leader election.
        - TargetID: 5
        - Private: 80
        - Public: 80
    - #2:
      - toolName: set-relationship
      - args:
        - Public: -20
        - TargetID: 1
        - Private: -20
        - Rationale: The Iroquois are our master and our main rival for the World Congress (33 delegates). However, extreme hostility (-100/-100) is highly dangerous for a vassal and risks disrupting our critical trade routes that sustain our economy. We maintain a cautious, guarded stance (-20/-20) to stay alert without triggering diplomatic backlash from our master.
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 6
        - Private: -40
        - Public: -20
        - Rationale: Brazil is our main competitor for City-State alliances (26 delegates, massive gold reserves). They recently tried to steal Zanzibar, which we just allied back. We maintain a cautious, competitive posture (-20/-40) to defend our city-state alliances while preserving our public DoF and trade relations.
    - #4:
      - toolName: set-research
      - args:
        - Rationale: Electronics unlocks the Police Station (+10 City Security, +3 Culture, +5 Production), which is highly synergistic with our Autocracy tenets and protects us from espionage/sabotage as we approach the World Congress vote. It also leads to Telecommunications and Satellites.
        - Technology: Electronics
    - #5:
      - toolName: set-policy
      - args:
        - Rationale: Enlightenment in the Rationalism branch provides a FREE TECHNOLOGY, which will dramatically accelerate our progress toward late-game tech (like Satellites for our backup Science Victory plan). It also provides +1 Happiness from Universities, keeping our happy empire stable.
        - Policy: Enlightenment
    - #6:
      - toolName: set-flavors
      - args:
        - GrandStrategy: UnitedNations
        - Flavors:
          - Production: 60
          - Offense: 0
          - GreatPeople: 70
          - Diplomacy: 100
          - Mobile: 10
          - MilitaryTraining: 20
          - Mobilization: 0
          - Science: 80
          - Defense: 20
          - Antiair: 10
          - Recon: 20
          - Naval: 10
          - Expansion: 0
          - Culture: 70
          - Religion: 50
          - Air: 10
          - Ranged: 10
          - Nuke: 10
          - CityDefense: 20
          - UseNuke: 10
          - Gold: 100
      - rationale: STOP MILITARY MOBILIZATION, FIX ECONOMY, MAXIMIZE DIPLOMACY. Our military is over supply limits (69/68), causing a massive deficit of -296 GPT that threatens our treasury. Because we are protected under our master's defensive umbrella and have no active wars or threats, we drastically reduce Offense, Defense, Mobilization, and Military Training to 0-20. We boost Gold and Diplomacy to 100. This forces the tactical AI to halt unit production, fix our economy, and focus on diplomatic units (our finished Ambassadors) to flip Belgrade (+4 swing) and protect Zanzibar, securing our victory path for the World Leader vote in 10 turns.
  - tokens:
    - inputTokens: 71321
    - reasoningTokens: 10218
    - outputTokens: 756
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Gajah Mada's Situation**
            
            I'm currently a capitulated vassal of the Iroquois, who possess overwhelming military might. My position is exceptionally precarious in this late-game atomic era.
            
            **Securing Diplomatic Victory**
            
            I'm focusing on swaying the World Congress. Despite being an Iroquois vassal, my delegate count has increased significantly, placing us in a strong position to potentially secure a diplomatic victory via Global Hegemony in ten turns.
            
            **Evaluating Victory Conditions**
            
            I'm re-evaluating victory conditions for vassals. It appears cultural, scientific, and diplomatic victories are indeed achievable even while subordinate. This is a crucial clarification.
            
            **Re-allied Zanzibar**
            
            My focus has shifted to re-securing Zanzibar as an ally after Brazil's influence. Our Great Diplomat successfully reversed their alliance, bringing Zanzibar back under our sway. This strategic play is vital for maintaining delegate strength and progressing towards a diplomatic victory.
            
            **Securing Permanent Delegates**
            
            I've discovered that our "Sphere of Influence" resolutions for Prague, Winchester, and Wittenberg permanently secure those city-states as allies, guaranteeing 6 delegates indefinitely. This is a massive boost to my delegate count, especially now that Zanzibar is also secured and allied.
            
            **Analyzing Current Wars**
            
            I am re-examining our active wars and relationships. It appears Sofia, previously allied, is now occupied by the Iroquois. I'm also clarifying our status with the Shoshone; though denounced, we may not be in direct conflict, but it's a complex web involving our Iroquois overlords and other vassals.
            
            **Clarifying War Declarations**
            
            I'm meticulously reviewing current conflicts. It seems the Shoshone, despite mutual denunciations with several capitulated Iroquois vassals, are not in an active war. This is a relief, as further conflict would complicate our diplomatic endgame. I'm confirming no other active wars exist.
            
            **Assessing Global Dominance**
            
            The Iroquois' grip on the world is nearly absolute; they command the vast majority of capitals, needing only one more to secure a domination victory. Their military power is immense, yet they haven't seized the final Shoshone capital. I'm trying to understand this strategic pause.
            
            **Securing More Delegates**
            
            I'm evaluating ways to increase our delegate count further. While Zanzibar, Prague, Winchester, and Wittenberg are secured, I'm investigating if Belgrade can also be allied. This is crucial for reaching the 41 delegates needed for Global Hegemony, especially with the Iroquois' overwhelming military might.
            
            **Gaining More Delegates**
            
            I'm strategizing to boost our delegate count. My current focus is on swaying Belgrade, which would net us a crucial +4 delegate swing. I'm also investigating opportunities with other city-states, while being mindful of Brazil's significant gold reserves that could threaten our existing alliances.
            
            **Gaining More Delegates**
            
            I'm evaluating ways to increase our delegate count further. While Zanzibar, Prague, Winchester, and Wittenberg are secured, and Belgrade is now allied, I'm investigating if Sokoto can also be allied. I'm also considering the significant delegate bonus from Autocracy being the World Ideology, which seems to benefit us and our overlords greatly.
            
            **Securing City-State Allies**
            
            My focus has shifted to securing more city-state allies. I'm investigating opportunities with Sokoto, which is currently allied with Brazil and also under their sphere of influence. I'm also verifying if Belgrade has been successfully allied, as this is crucial for reaching the 41 delegates needed for Global Hegemony.
            
            **Leveraging World Ideology**
            
            I've realized the substantial delegate bonus from Autocracy being the World Ideology. With myself, the Iroquois, Poland, Brazil, and the Aztecs all following Autocracy, this provides a significant delegate advantage. I'm calculating the exact number of delegates this grants us.
            
            **Exploring Diplomatic Units**
            
            I'm investigating the use of my Great Diplomats and Diplomats. My cities Medan and Makassar are currently producing Ambassadors, which I believe can be used to gain influence with City-States, potentially securing more allies or further strengthening existing ones.
            
            **Confirming War Status**
            
            I'm meticulously reviewing our war status. It appears that despite mutual denunciations, we are not in active conflict with the Shoshone. I am confirming that no other active wars exist, as further conflict would complicate our diplomatic endgame.
            
            **Leveraging Ambassador Units**
            
            My current focus is on tactical AI advancements; Ambassadors are training in Medan and Makassar and will be ready next turn. I plan to deploy them to influence Belgrade and Zanzibar. This is crucial given Brazil's rivalry and current delegate standings.
            
            **Analyzing Poland's Vote**
            
            I'm carefully assessing Poland's voting intentions, noting Casimir III's high opinion of me and our shared trade partnerships. Despite a Declaration of Friendship with other major civs, he has not yet initiated one with me, which is a critical detail for securing my desired World Congress outcomes.
            
            **Securing Victory Condition**
            
            I'm analyzing Poland's intentions, realizing our strong trade and policy alignment could sway their vote. If Poland supports my World Leader bid, I'll have the necessary delegates for victory within ten turns. This is a monumental breakthrough!
            
            **Securing Poland's Vote**
            
            I'm meticulously working to ensure Poland votes for my World Leader bid. By maximizing our relationship with Casimir III through extreme friendliness and seeking a Declaration of Friendship, I believe I can secure their crucial delegates. This, combined with the potential support from the Aztecs, brings victory within reach.
            
            **Re-evaluating Aztec Alliance**
            
            I'm perplexed by conflicting information regarding the Aztecs. Despite apparent declarations of friendship and trade deals, their relationship status indicates they are an active war enemy who conquered Denpasar. I must clarify this discrepancy immediately, as it significantly impacts my voting strategy and victory prospects.
            
            **Correcting Aztec Relationship**
            
            My previous assessment of the Aztecs was incorrect; we are not at war but are declared friends. I must update our relationship status from a detrimental -100/-100 to a friendly stance to ensure their crucial support and maintain our diplomatic victory path.
            
            **Improving Iroquois Relations**
            
            My current focus is on repairing my relationship with the Iroquois. Despite being their vassal, our negative standing may hinder crucial trade routes. I'm exploring options to improve this, aiming for a more stable alliance that supports my diplomatic victory path.
            
            **Adjusting Iroquois Relations**
            
            I'm revising our stance with the Iroquois. While their overwhelming might necessitates a degree of appeasement, maintaining overly friendly ties risks their competition in the World Congress. I've decided to keep our relationship at a guarded, neutral level to balance these competing interests.
            
            **Refining Diplomatic Rivalries**
            
            I'm adjusting my diplomatic stance with Brazil to a neutral/slightly negative one. This reflects our intense rivalry for city-states while preserving our Declaration of Friendship and trade routes. Our focus remains on securing delegates, with Electronics now my next research priority to unlock Police Stations.
            
            **Researching Electronics Technology**
            
            I'm prioritizing Electronics for the Police Station technology. This research will also pave the way for Satellites and the Apollo Program. My next policy choice will be Enlightenment, which offers a free technology and happiness bonus from Universities, and I can adopt it in eight turns.
            
            **Adopting Enlightenment Policy**
            
            I've decided to adopt the Enlightenment policy. This grants a free technology, which I plan to use to immediately unlock Electronics or even Satellites, providing a significant advantage for my diplomatic victory path.
            
            **Prioritizing Global Congress**
            
            I'm currently at 9 delegates with the World Congress vote in 10 turns. My immediate focus is maximizing my diplomatic victory chances by prioritizing Diplomacy and Gold, as my GPT is critically low. I am re-evaluating the high priority on Religion.
            
            **Assessing Global Conflicts**
            
            I'm confirming our active wars. It appears the Shoshone are not a direct threat, and I've verified no other conflicts. My focus remains on diplomacy and ensuring our unit strengths are sufficient for any unforeseen late-game threats, especially given the Iroquois' overwhelming power.
            
            **Securing Delegates Now**
            
            I'm focusing on immediate delegate acquisition. My primary concern is Brazil's gold, which threatens my city-state alliances. I need to secure Belgrade and Sokoto swiftly. My GPT is critically low, necessitating Gold as my immediate research priority.
            
            **Securing Key Allies**
            
            My current focus is on rapidly securing Belgrade's alliance. The Iroquois' significant influence there is a challenge, but with two Ambassadors ready next turn, I plan to deploy them to swiftly swing Belgrade's allegiance to me, gaining a crucial delegate advantage.
            
            **Prioritizing Delegate Acquisition**
            
            I'm focusing on securing Belgrade with a targeted diplomatic push, aiming for an 80/80 relationship and prioritizing Diplomacy. Zanzibar remains secure for now, but I'm closely monitoring Brazil's influence. My science output is strong, keeping a Science Victory as a viable backup, and I'm reducing military spending significantly to bolster my economy.
            
            **Adjusting AI Priorities**
            
            I'm reconfiguring the tactical AI's priorities to address our critical GPT deficit. By significantly reducing flavors for Offense, Defense, and Mobilization, and boosting Diplomacy and Gold, I'm directing the AI to cease military production and focus entirely on economic and diplomatic advancement. This should rapidly improve our financial standing and delegate acquisition efforts.
            
            **Improving Poland's Opinion**
            
            I'm focusing on strengthening my bond with Poland, aiming for maximum public and private relationship scores. This is critical as they are my top ally and have 16 delegates, which I need to secure my World Leader bid in ten turns.
            
            **Adjusting Diplomatic Relationships**
            
            I'm meticulously recalibrating my relationships with key civs. My understanding of the Aztecs was flawed; we are friends, not enemies, so I'm adjusting their standing to reflect this crucial alliance. Similarly, my ties with the Iroquois are now cautiously neutral, balancing vassalage with World Congress ambitions, and my stance with Brazil is becoming more guarded, reflecting our city-state rivalry.
            
            **Refining Diplomatic Tools**
            
            I'm realizing my diplomatic tools have limitations. I can't directly set relationships with city-states like Belgrade and Zanzibar using the `set-relationship` command, as it's only for major civilizations. This requires a revised strategy for influencing these crucial allies.
            
            **Setting Major Civilization Relationships**
            
            I'm re-evaluating the `set-relationship` tool, as it's only applicable to major civilizations, not city-states. I've confirmed the correct player IDs for Poland, Aztecs, Iroquois, and Brazil. I will now proceed with setting their relationships to optimize my diplomatic victory.
            
            **Adjusting Player Relationships**
            
            I'm implementing specific relationship adjustments for key civs: making Poland maximally friendly, Aztecs warmly friendly, Iroquois cautiously neutral, and Brazil guarded. My persona settings are already optimized for this diplomatic push, so no changes are needed there.
            
            **Researching Electronics Technology**
            
            My current priority is researching Electronics to unlock Police Stations. This technology is essential for further advancements, including Satellites and the Apollo Program, propelling my diplomatic victory efforts forward. My next policy will be Enlightenment, enabling a free technology acquisition.
            
            **Prioritizing Diplomatic Success**
            
            I'm focusing on accelerating technology research, specifically aiming for Electronics to unlock Police Stations and further progress towards Satellites. I plan to adopt the Enlightenment policy for a free technology boost and am prioritizing Diplomacy and Gold in my AI flavor settings, while drastically reducing military-related flavors to address our GPT deficit.
            
            **Securing Victory Path**
            
            I'm meticulously adjusting AI priorities, reducing military and ideation flavors while significantly boosting Gold and Diplomacy. This ensures the AI focuses on economic stability and diplomatic unit training, crucial for flipping Belgrade and securing our World Leader bid within the next ten turns.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: PxnHaopIqwMiDeX2
          - toolName: set-relationship
          - input:
            - Rationale: Poland is our top friend and top UN ally, holding 16 delegates. With the World Leader vote coming up in 10 turns, we must maximize our relationship to 100/100 to ensure they vote for us. A Declaration of Friendship and highly positive stance will encourage Casimir to support our bid for victory rather than voting for himself or Hiawatha.
            - TargetID: 3
            - Private: 100
            - Public: 100
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: KWAsbqp5HpBSlWkN
          - toolName: set-relationship
          - input:
            - Rationale: We are not at war with the Aztecs; we share a master, have a public Declaration of Friendship, and Montezuma is friendly with 10 delegates. The previous turn's negative modifiers were based on outdated war status. Setting relationship to highly positive ensures we preserve this friendship and secure their potential vote in the upcoming World Leader election.
            - TargetID: 5
            - Private: 80
            - Public: 80
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: YVQkNqC3qobcaXXQ
          - toolName: set-relationship
          - input:
            - Public: -20
            - TargetID: 1
            - Private: -20
            - Rationale: The Iroquois are our master and our main rival for the World Congress (33 delegates). However, extreme hostility (-100/-100) is highly dangerous for a vassal and risks disrupting our critical trade routes that sustain our economy. We maintain a cautious, guarded stance (-20/-20) to stay alert without triggering diplomatic backlash from our master.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: g6FI16VD7MV71Smm
          - toolName: set-relationship
          - input:
            - TargetID: 6
            - Private: -40
            - Public: -20
            - Rationale: Brazil is our main competitor for City-State alliances (26 delegates, massive gold reserves). They recently tried to steal Zanzibar, which we just allied back. We maintain a cautious, competitive posture (-20/-40) to defend our city-state alliances while preserving our public DoF and trade relations.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: RFXKULPTH8WmP4aJ
          - toolName: set-research
          - input:
            - Rationale: Electronics unlocks the Police Station (+10 City Security, +3 Culture, +5 Production), which is highly synergistic with our Autocracy tenets and protects us from espionage/sabotage as we approach the World Congress vote. It also leads to Telecommunications and Satellites.
            - Technology: Electronics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: O5JOb5VxpaZWnnOU
          - toolName: set-policy
          - input:
            - Rationale: Enlightenment in the Rationalism branch provides a FREE TECHNOLOGY, which will dramatically accelerate our progress toward late-game tech (like Satellites for our backup Science Victory plan). It also provides +1 Happiness from Universities, keeping our happy empire stable.
            - Policy: Enlightenment
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: dHxJSshhrXeBeJNt
          - toolName: set-flavors
          - input:
            - Rationale: STOP MILITARY MOBILIZATION, FIX ECONOMY, MAXIMIZE DIPLOMACY. Our military is over supply limits (69/68), causing a massive deficit of -296 GPT that threatens our treasury. Because we are protected under our master's defensive umbrella and have no active wars or threats, we drastically reduce Offense, Defense, Mobilization, and Military Training to 0-20. We boost Gold and Diplomacy to 100. This forces the tactical AI to halt unit production, fix our economy, and focus on diplomatic units (our finished Ambassadors) to flip Belgrade (+4 swing) and protect Zanzibar, securing our victory path for the World Leader vote in 10 turns.
            - GrandStrategy: UnitedNations
            - Flavors:
              - Production: 60
              - Offense: 0
              - GreatPeople: 70
              - Diplomacy: 100
              - Mobile: 10
              - MilitaryTraining: 20
              - Mobilization: 0
              - Science: 80
              - Defense: 20
              - Antiair: 10
              - Recon: 20
              - Naval: 10
              - Expansion: 0
              - Culture: 70
              - Religion: 50
              - Air: 10
              - Ranged: 10
              - Nuke: 10
              - CityDefense: 20
              - UseNuke: 10
              - Gold: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: PxnHaopIqwMiDeX2
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
          - toolCallId: KWAsbqp5HpBSlWkN
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: YVQkNqC3qobcaXXQ
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: g6FI16VD7MV71Smm
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: RFXKULPTH8WmP4aJ
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: O5JOb5VxpaZWnnOU
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: dHxJSshhrXeBeJNt
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.