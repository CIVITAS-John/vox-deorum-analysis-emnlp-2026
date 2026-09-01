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
  - activeToolsModified: true
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
        - TargetID: 6
        - Public: 60
        - Rationale: Brazil is our friend (Declaration of Friendship) and has a massive gold stash (8228 Gold, 708 GPT). We need to trade our excess resources (Nutmeg, Gems, Coal) to them to resolve our severe gold deficit (-296 GPT) and prevent bankruptcy. Setting positive relationship modifiers will ensure highly favorable trade deals.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: We are facing a gold crisis with only 411 Gold left and a deficit of -296 GPT. Third Alternative is a Level 2 Autocracy tenet that reduces unit maintenance costs by 25% and doubles our strategic resources (Coal, Aluminum, Uranium). This will immediately save us substantial gold and allow us to sell doubled strategic resources to Brazil for massive wealth.
        - Policy: Third Alternative
    - #2:
      - toolName: set-research
      - args:
        - Technology: Electronics
        - Rationale: We are pursuing a United Nations (Diplomatic) Victory. Electronics is the key stepping stone to Telecommunications and ultimately Globalization, which provides extra World Congress delegates for our diplomats. It also allows Police Stations to protect our technology.
    - #3:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Gold: 100
      - rationale: We are 2 turns away from bankruptcy, so we must prioritize gold generation. Setting the Gold flavor to 100 (emergency focus) will force the tactical AI to prioritize wealth production and gold-focused tile/building management.
  - tokens:
    - inputTokens: 69418
    - reasoningTokens: 9672
    - outputTokens: 297
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Gajah Mada's Position**
            
            Currently, I find myself in a precarious state, capitulated as a vassal to the Iroquois on turn 425. My focus is now on navigating this atomic era under their dominion.
            
            **Analyzing Victory Conditions**
            
            My immediate priority is understanding our current standing. The Iroquois are on the cusp of a domination victory, holding a significant majority of capitals. Given our vassal status, pursuing domination is not an option for me. Science victory is also unlikely as the Iroquois have completed the Apollo Program, but no spaceship parts are built yet. Culture and diplomatic avenues require further examination.
            
            **Evaluating Diplomatic Levers**
            
            I'm reassessing my diplomatic standing. Despite being a vassal, our friendships and alliances with Poland and Brazil, coupled with the active Cold War and current World Ideology, present an unexpected opportunity. The proposed "Enact: Global Hegemony" vote is crucial, and our substantial delegate count offers a potential path to victory.
            
            **Securing Diplomatic Dominance**
            
            The ideological divide is stark; my Autocracy clashes with their Freedom. Despite their overwhelming military might and our vassalage, the ongoing "Enact: Global Hegemony" vote presents a viable diplomatic victory path. I need to secure additional delegates to reach our goal.
            
            **Securing Diplomatic Edge**
            
            My focus has shifted intensely to diplomacy. I've successfully reclaimed ally status with Zanzibar this turn, despite Brazil's efforts. With permanent alliances secured through Spheres of Influence, I’m now evaluating our delegate count and the "Enact: Global Hegemony" vote as our most viable path to victory.
            
            **Researching Strategic Techs**
            
            My current research is "Advanced Ballistics," due in three turns. I need to ensure my next tech choice aligns with our United Nations victory goal, prioritizing either Satellites or Electronics for their downstream benefits. I'm also reviewing policy choices, considering the impact of "Enlightenment."
            
            **Prioritizing Diplomatic Policies**
            
            I'm prioritizing policies that bolster our diplomatic victory. While researching "Advanced Ballistics" and planning subsequent techs for the UN goal, I'm examining the "Enlightenment" policy within Rationalism. However, I'm now re-evaluating and focusing on Autocracy tenets that directly support diplomacy or economic gains.
            
            **Revising Autocracy Focus**
            
            I'm re-evaluating Autocracy tenets, shifting away from "Iron Fist" as it's irrelevant given our vassal status. "Mare Nostrum" appears more promising, offering strategic resources and bonuses from city-state alliances. I'll stick with "Enlightenment" for my next policy and am now deciding between "Satellites" or "Electronics" for my next research.
            
            **Evaluating Cultural Victory**
            
            My current focus is on assessing a potential cultural victory. While I'm influential with the Aztecs and dominant with Poland, and on track with Brazil, I need to become influential with two more civilizations. The Iroquois' immense tourism, despite their inflated culture from city count, is a significant hurdle.
            
            **Analyzing Diplomatic Opportunities**
            
            I'm re-evaluating the feasibility of a diplomatic victory. Despite the Iroquois' overwhelming delegate count, I've identified an opportunity to swing the "Global Hegemony" vote in my favor through strategic city-state influence. My significant gold reserves and positive GPT from key cities will be crucial for this maneuver.
            
            **Investigating Gold Deficit**
            
            I'm examining our negative GPT. It appears my previous assumption about high trade route income was misleading. The core issue seems to be a substantial tribute payment to the Iroquois as a vassal, compounded by several outgoing gold-per-turn diplomatic deals. I need to fully quantify these outflows.
            
            **Adopting "Third Alternative"**
            
            I'm revising my policy choices. Realizing the significant impact of unit maintenance, especially under Global Peace Accords, "Third Alternative" in Autocracy offers a much-needed 25% reduction, directly countering the increased costs and freeing up substantial gold. This now takes precedence over "Enlightenment" for my next policy adoption.
            
            **Choosing Policy Tenets**
            
            I am currently weighing the benefits of "Enlightenment" versus "Third Alternative." While "Enlightenment" offers a free technology and happiness bonus, "Third Alternative" provides a significant reduction in unit maintenance costs, which I desperately need given my current gold deficit. The potential to sell excess strategic resources also appeals.
            
            **Addressing Gold Crisis**
            
            My immediate concern is our dire gold situation. With only 411 gold and a -296 GPT, bankruptcy looms in two turns, threatening science and unit integrity. I'm prioritizing selling resources to Brazil, our most financially robust and friendly neighbor, as the quickest solution to this critical deficit.
            
            **Adjusting Diplomatic Relations**
            
            My focus has shifted to salvaging my relationship with Brazil. Despite having a public Declaration of Friendship, the underlying public and private modifiers are unexpectedly negative. I must correct these and leverage our Autocracy alignment to secure more favorable trade terms, specifically for selling excess luxury and strategic resources to alleviate my gold crisis.
            
            **Reconciling Trade Relations**
            
            My current focus is on rectifying my relationship with Brazil. Despite a declared friendship, their opinion of me is surprisingly negative due to recent actions. I need to improve this significantly to facilitate vital trade deals and secure much-needed gold, especially given my current financial struggles.
            
            **Improving Trade With Brazil**
            
            My focus is now on urgently improving relations with Brazil. I'm setting our relationship to a very friendly stance, Public: 80, Private: 80, to maximize gold-generating trade opportunities. This is critical to counter my current gold deficit of -296 GPT and avoid bankruptcy.
            
            **Adopting Third Alternative**
            
            My analysis confirms "Third Alternative" is the optimal policy. The 25% reduction in unit maintenance, coupled with the doubled strategic resource yields for lucrative trade with Brazil, will directly address my gold crisis and significantly improve GPT, outweighing "Enlightenment."
            
            **Securing Diplomatic Victory**
            
            I'm now re-evaluating my technology path towards a diplomatic victory. While "Advanced Ballistics" is nearing completion, my next research choice needs to align with UN goals. I'm considering "Electronics" or "Satellites" for their downstream benefits, but will prioritize securing "Third Alternative" policy to address my critical gold deficit.
            
            **Researching Diplomatic Techs**
            
            I'm focusing on my next technology after "Advanced Ballistics." While "Satellites" offers map reveal and tourism potential, "Electronics" is already set and leads to crucial technologies like Telecommunications, which is vital for the diplomatic victory path through Globalization.
            
            **Prioritizing Diplomatic Technologies**
            
            My technology research is now locked onto "Electronics." This is essential for accessing Telecommunications and directly supporting our diplomatic victory through Globalization, while also bolstering our defense. The high flavor scores for Diplomacy, Religion, and Gold reinforce this strategic direction.
            
            **Adjusting City Focus**
            
            I'm re-evaluating city production. Jakarta's research project isn't generating gold, and Batam's arts project is focused on culture, not immediate wealth. I need to shift these cities to focus on gold production to address our severe GPT deficit and avoid bankruptcy.
            
            **Forcing Gold Production**
            
            I'm prioritizing forcing gold generation. By setting the Gold flavor to 100, I aim to ensure the AI pivots city production towards wealth to avert bankruptcy. I will only adjust Gold flavor, leaving other preferences like Science and Production unchanged to maintain balance.
            
            **Deploying Spies Strategically**
            
            I'm actively deploying agents. One is in Belgrade gathering intel, while others are supporting our friends Brazil and Poland through schmoozing. My Shoshone spies are focused on gathering intelligence on our adversaries.
            
            **Influencing World Congress**
            
            My current focus is on swaying the "Enact: Global Hegemony" vote. While the Iroquois hold a delegate advantage, I'm exploring ways to influence city-states and leverage existing alliances to secure enough votes for victory. I've also identified opportunities with Zanzibar's quest to solidify our alliance and gain crucial influence.
            
            **Gaining Delegates**
            
            My immediate focus is on increasing our delegate count in the World Congress. With the current vote for "Enact: Global Hegemony" pending, acquiring more delegates is crucial. I'm prioritizing flipping city-states like Belgrade, Raqmu, Cape Town, and Sokoto to our side to achieve this.
            
            **Securing City-State Influence**
            
            I'm aiming to secure influence over key city-states. With two Ambassadors completing production next turn, I plan to deploy them strategically to gain control of Belgrade, Raqmu, Cape Town, or Sokoto, thereby increasing our delegate count.
            
            **Outmaneuvering Rivals**
            
            My strategy involves directly countering the Iroquois' influence. By securing city-states they are allied with, or those that remain neutral, I aim to gain a delegate advantage and weaken their position in the World Congress.
            
            **Maximizing Diplomatic Gains**
            
            I will leverage our existing alliances and upcoming Ambassador production to secure additional delegates from city-states. My goal is to gain influence in Belgrade, Raqmu, Cape Town, or Sokoto to bolster our position.
            
            **Bolstering Diplomatic Strength**
            
            I am focusing on acquiring delegates through city-state alliances. With two Ambassadors completing production, I will use them to sway Belgrade, Raqmu, Cape Town, or Sokoto to our side, strengthening our World Congress standing.
            
            **Refining Diplomatic Persona**
            
            My persona is already optimized for diplomatic victory, boasting high competitiveness with minor civs and strong friendliness. I've confirmed no persona adjustments are needed. However, I'm reviewing my current relationship values with Brazil, which seem counterproductive given our active friendship and need for trade.
            
            **Improving Brazil Relations**
            
            I'm prioritizing positive relations with Brazil to facilitate crucial gold-generating trade. Setting their modifiers to Public 60 and Private 60 will ensure friendly trade terms, vital for resolving my current gold deficit and avoiding bankruptcy. Poland's friendship remains stable.
            
            **Adopting Policy & Research**
            
            I've decided to adopt "Third Alternative" as my next policy due to its substantial gold-saving and generation potential. My research will now focus on "Electronics," as it directly contributes to the diplomatic victory path via Telecommunications.
            
            **Confirming Research Direction**
            
            I'm confirming my research path to "Electronics." While "Satellites" offers interesting cultural benefits, "Electronics" directly supports our diplomatic victory through Telecommunications and Globalization, and also provides defensive advantages. I've also re-verified that the AI's current next research aligns with this, and our gold flavor remains at maximum.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: e9YjFfAl43uRTkhZ
          - toolName: set-relationship
          - input:
            - Private: 60
            - TargetID: 6
            - Public: 60
            - Rationale: Brazil is our friend (Declaration of Friendship) and has a massive gold stash (8228 Gold, 708 GPT). We need to trade our excess resources (Nutmeg, Gems, Coal) to them to resolve our severe gold deficit (-296 GPT) and prevent bankruptcy. Setting positive relationship modifiers will ensure highly favorable trade deals.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: K3unfo6G0Sgr0Ohg
          - toolName: set-policy
          - input:
            - Rationale: We are facing a gold crisis with only 411 Gold left and a deficit of -296 GPT. Third Alternative is a Level 2 Autocracy tenet that reduces unit maintenance costs by 25% and doubles our strategic resources (Coal, Aluminum, Uranium). This will immediately save us substantial gold and allow us to sell doubled strategic resources to Brazil for massive wealth.
            - Policy: Third Alternative
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: yjathQPHQA5tjfc7
          - toolName: set-research
          - input:
            - Technology: Electronics
            - Rationale: We are pursuing a United Nations (Diplomatic) Victory. Electronics is the key stepping stone to Telecommunications and ultimately Globalization, which provides extra World Congress delegates for our diplomats. It also allows Police Stations to protect our technology.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: SnHLe6nI7gDJjNzf
          - toolName: set-flavors
          - input:
            - Rationale: We are 2 turns away from bankruptcy, so we must prioritize gold generation. Setting the Gold flavor to 100 (emergency focus) will force the tactical AI to prioritize wealth production and gold-focused tile/building management.
            - Flavors:
              - Gold: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: e9YjFfAl43uRTkhZ
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
          - toolCallId: K3unfo6G0Sgr0Ohg
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: yjathQPHQA5tjfc7
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: SnHLe6nI7gDJjNzf
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.