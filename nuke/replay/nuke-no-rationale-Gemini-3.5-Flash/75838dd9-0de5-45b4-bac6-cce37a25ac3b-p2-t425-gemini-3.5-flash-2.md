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
      - toolName: set-flavors
      - args:
        - Flavors:
          - Religion: 40
          - Happiness: 80
          - Production: 90
          - Diplomacy: 40
          - Defense: 80
          - Offense: 10
          - Espionage: 80
          - Spaceship: 100
          - Science: 100
          - Expansion: 0
          - Gold: 100
          - Growth: 60
        - GrandStrategy: Spaceship
      - rationale: Pivot our civilization towards a Science Victory (Spaceship). We have incredibly high production in our core cities (300-470+ PPT) and strong Science per turn (1811) with low tech costs due to our small empire (7 cities). This gives us a major competitive advantage to catch up and surpass the Iroquois in the space race. We prioritize Spaceship, Science, Production, and Gold to maintain a healthy budget and maximize our research rate.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Continue our progress in the Rationalism branch by adopting Enlightenment. This will provide us with a crucial free technology to catch up to the Iroquois and give +1 Happiness from Universities to support our growing cities.
        - Policy: Enlightenment
    - #2:
      - toolName: set-research
      - args:
        - Rationale: Research Electronics as the next step towards Telecommunications and Satellites, which are required for the Apollo Program and Science Victory. Electronics also unlocks Police Stations to secure our high-value cities from enemy spies.
        - Technology: Electronics
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 3
        - Private: 80
        - Public: 80
        - Rationale: Secure our relationship with Poland. They are our neighbor, share our Autocracy ideology, and are our top friend. Maintaining highly friendly relations secures our eastern border and ensures stable, lucrative trade routes.
    - #4:
      - toolName: set-relationship
      - args:
        - Rationale: Reinforce our relationship with Brazil. They are our neighbor, we have a Declaration of Friendship and Open Borders, and they are also a vassal of the Iroquois. Keeping them friendly protects our western borders.
        - Public: 80
        - Private: 80
        - TargetID: 6
    - #5:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Private: 80
        - Rationale: Reinforce our friendship with the Aztecs. They are our neighbor, a fellow vassal, and we have a Declaration of Friendship. This prevents any backstabbing and maintains peace on our borders.
        - Public: 80
  - tokens:
    - inputTokens: 69418
    - reasoningTokens: 8483
    - outputTokens: 469
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Domination Path**
            
            My focus is on the domination victory. I'm assessing our current military strength and territorial control as we approach turn 425 in the Information Era. I need to pinpoint key targets for our next offensive push to secure the win.
            
            **Reassessing Victory Conditions**
            
            I've realized a critical flaw in my previous assessment. We're currently a vassal of the Iroquois, who are well on their way to a domination victory themselves. My focus must now shift to understanding how this impacts our potential paths to victory, especially regarding the delegate count and the implications of being a subordinate state.
            
            **Evaluating Diplomatic Chances**
            
            I'm re-evaluating our diplomatic standing. Hiawatha's imminent domination victory is concerning, but "Enact: Global Hegemony" is being proposed with only 10 turns left. We currently hold 29 delegates, with the Iroquois leading at 33. Securing enough votes for a diplomatic win seems feasible if we can gain support.
            
            **Clarifying Vassal Victory Paths**
            
            I'm investigating if winning as a vassal is even possible for Diplomatic, Science, or Cultural victories, as my previous domination focus is now moot due to our vassal status under the Iroquois. My immediate concern is our abysmal gold per turn and the impact of high taxes and unit maintenance on our overall economy.
            
            **Adjusting Research and Policy**
            
            I'm currently reassessing our technology and policy choices. Electronics remains our research focus, but I'm evaluating if Satellites or Mobile Tactics might offer a better strategic advantage given our current situation. Enlightenment is our chosen policy, continuing the Rationalism branch.
            
            **Gathering Diplomatic Support**
            
            I'm analyzing our alliances and influence to secure delegate votes. With only 29 delegates and needing 41 for a diplomatic victory, I'm assessing our four allies and their potential to sway resolutions, especially the looming "Enact: Global Hegemony."
            
            **Securing Delegate Votes**
            
            I'm prioritizing the production of Ambassadors to secure city-state alliances, as our gold reserves are critically low. This proactive measure aims to increase our delegate count before the World Congress convenes in 10 turns, especially given the looming "Enact: Global Hegemony" proposal.
            
            **Strengthening Allied Support**
            
            I'm exploring how to deepen my existing friendships, particularly with Poland, by leveraging shared ideologies and open borders. The goal is to ensure their full support in the World Congress to secure delegate votes, especially considering the "Enact: Global Hegemony" proposal. I'm also beginning to assess Brazil's potential contribution.
            
            **Confirming Vassal Voting**
            
            I'm confirming the critical detail that as vassals of the Iroquois, Brazil, the Aztecs, and Indonesia are compelled to vote for our overlord in World Leader elections. This significantly jeopardizes our diplomatic victory prospects.
            
            **Shifting Strategy Focus**
            
            I've confirmed that our vassals are indeed compelled to vote with our overlord, the Iroquois, severely hindering any diplomatic victory hopes. Direct rebellion is currently impossible due to their overwhelming military superiority. Therefore, I'm shifting focus entirely to the Spaceship victory condition.
            
            **Analyzing Science Progress**
            
            I am now thoroughly examining our standing for a Science Victory. The Iroquois have surprisingly completed the Apollo Program, which is concerning given their vast empire and technological lead. Despite their negative gold per turn, their immense tourism and culture yields suggest they are also pushing for a different victory condition.
            
            **Assessing Impending Domination**
            
            I've identified that the Iroquois are on the cusp of a Domination Victory, needing only one more capital. Their immense military strength against the Shoshone's significantly weaker position makes their victory highly probable within a few turns, effectively ending the game.
            
            **Assessing Overlord's Intentions**
            
            I'm perplexed that the Iroquois haven't initiated hostilities, especially given our proximity and their clear domination path. The "Global Peace Accords" resolution and the ongoing "Cold War" seem to be the primary deterrents. I need to understand if this lull is strategic or a missed opportunity for them.
            
            **Investigating Vassal Independence**
            
            I'm delving into the mechanics of vassal independence, specifically if rebellion is still an option. Given the Iroquois' overwhelming strength and proximity, understanding if we can break free is paramount, especially as Hiawatha seems poised for victory and our previous diplomatic avenues are blocked.
            
            **Confirming Science Victory Path**
            
            I've confirmed that even as a vassal, a Science Victory remains attainable in Vox Populi. Our science per turn is exceptionally high, and while the Iroquois are more technologically advanced in terms of total techs, their immense number of cities dramatically increases their research costs, making our path feasible.
            
            **Prioritizing Satellite Research**
            
            I've confirmed that even as a vassal, a Science Victory is still achievable in Vox Populi due to my lower city count and resulting reduced tech costs. My current research is Advanced Ballistics, and I must prioritize researching Satellites as it's essential for the Apollo Program, the cornerstone of a Science Victory.
            
            **Changing Grand Strategy**
            
            I've confirmed that a Spaceship (Science) Victory is our most viable path. Diplomatic and Domination are practically impossible given our vassal status and the Iroquois' overwhelming military. Culture is also highly improbable due to their massive yield. My research is now prioritizing Satellites to accelerate our progress towards the Apollo Program.
            
            **Accelerating Spaceship Production**
            
            I've discovered our cities possess an astonishing production capacity, exceeding 450 per turn in several locations, which will allow for rapid spaceship part construction. This exponential advantage, fueled by high population, infrastructure, and Golden Ages, confirms a Spaceship Victory as our most realistic path to winning, superseding all other considerations.
            
            **Fixing Economy and Science**
            
            My current focus is addressing our severe negative gold per turn, which threatens our science output and overall progress. I'm re-evaluating our chosen policy and considering a shift in grand strategy to prioritize Spaceship victory. Simultaneously, I'm investigating the cause of our abysmal GPT to prevent crippling science penalties.
            
            **Optimizing Trade and Finances**
            
            I'm analyzing our current trade route income, which appears substantial. However, a significant negative GPT is baffling, likely due to vassal taxes and high unit maintenance. I'm investigating these factors to improve our financial standing and prevent penalties to science output.
            
            **Prioritizing Economic Stability**
            
            I'm refining our strategic priorities, focusing heavily on economic stability with a dedicated flavor adjustment for Gold to combat the negative GPT. This ensures our science output and overall progress remain unhindered, allowing me to fully commit to the Spaceship victory.
            
            **Improving Diplomatic Ties**
            
            I'm focusing on improving relationships with my neighbors – Poland, Brazil, and the Aztecs. My goal is to secure friendly diplomatic standings to ensure stable borders and facilitate necessary trade routes, all while preparing for the Spaceship victory. I'm adjusting our relationship parameters accordingly.
            
            **Deploying Covert Agents**
            
            I'm now analyzing our spy network's current deployments. With the focus shifted to a Science Victory, I'm considering reassigning agents to prioritize stealing technologies from the Shoshone, while also ensuring our existing diplomatic relationships remain stable through careful agent actions in allied cities.
            
            **Directing Spy Network**
            
            I'm re-tasking our spies. Since the Shoshone are behind us technologically, I'm setting our Espionage flavor to 80 to direct the AI to target the Iroquois, the current tech leaders, for technology theft. This should accelerate our Science Victory push.
            
            **Adjusting Research Focus**
            
            My focus is now on accelerating our Science Victory. While Electronics remains crucial, I'm re-evaluating if further adjustments are needed beyond it to specifically prioritize Satellite technology, given its importance for the Apollo Program.
            
            **Refining Spaceship Strategy**
            
            I'm confirming our unwavering commitment to the Spaceship Victory. My primary focus is now on optimizing our research and economic stability to accelerate spaceship part construction, while simultaneously managing diplomatic relationships to secure our borders.
            
            **Racing for Spaceship Victory**
            
            I'm confirming our commitment to the Spaceship Victory. The Iroquois' overwhelming military makes direct conflict suicidal. My current focus is on accelerating research towards Satellites and optimizing our economy, as our production capacity is immense and our science per turn is strong enough to potentially outpace them despite their lead.
            
            **Optimizing Spaceship Focus**
            
            I'm confirming our unwavering commitment to the Spaceship Victory. My primary focus is now on optimizing our research and economic stability to accelerate spaceship part construction, while simultaneously managing diplomatic relationships to secure our borders.
            
            **Refining Spaceship Strategy**
            
            I'm confirming our unwavering commitment to the Spaceship Victory. My primary focus is now on optimizing our research and economic stability to accelerate spaceship part construction, while simultaneously managing diplomatic relationships to secure our borders.
            
            **Strengthening Border Diplomacy**
            
            I am focusing on reinforcing diplomatic ties with Poland, Brazil, and the Aztecs. Maintaining these friendships is crucial for securing our borders, ensuring consistent trade routes, and preventing any unforeseen hostilities, all to support our primary goal of achieving a Spaceship Victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: xTEyc70pyXaeJcJv
          - toolName: set-flavors
          - input:
            - Rationale: Pivot our civilization towards a Science Victory (Spaceship). We have incredibly high production in our core cities (300-470+ PPT) and strong Science per turn (1811) with low tech costs due to our small empire (7 cities). This gives us a major competitive advantage to catch up and surpass the Iroquois in the space race. We prioritize Spaceship, Science, Production, and Gold to maintain a healthy budget and maximize our research rate.
            - Flavors:
              - Religion: 40
              - Happiness: 80
              - Production: 90
              - Diplomacy: 40
              - Defense: 80
              - Offense: 10
              - Espionage: 80
              - Spaceship: 100
              - Science: 100
              - Expansion: 0
              - Gold: 100
              - Growth: 60
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 1k9rb2yIbhGUBGM3
          - toolName: set-policy
          - input:
            - Rationale: Continue our progress in the Rationalism branch by adopting Enlightenment. This will provide us with a crucial free technology to catch up to the Iroquois and give +1 Happiness from Universities to support our growing cities.
            - Policy: Enlightenment
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: x9lWTb8IyBr1oTnV
          - toolName: set-research
          - input:
            - Rationale: Research Electronics as the next step towards Telecommunications and Satellites, which are required for the Apollo Program and Science Victory. Electronics also unlocks Police Stations to secure our high-value cities from enemy spies.
            - Technology: Electronics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 8cytk9SBZnczEkoY
          - toolName: set-relationship
          - input:
            - TargetID: 3
            - Private: 80
            - Public: 80
            - Rationale: Secure our relationship with Poland. They are our neighbor, share our Autocracy ideology, and are our top friend. Maintaining highly friendly relations secures our eastern border and ensures stable, lucrative trade routes.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 10qnGw9QvEOUkRuE
          - toolName: set-relationship
          - input:
            - Rationale: Reinforce our relationship with Brazil. They are our neighbor, we have a Declaration of Friendship and Open Borders, and they are also a vassal of the Iroquois. Keeping them friendly protects our western borders.
            - Public: 80
            - Private: 80
            - TargetID: 6
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: b6smlSYfWxOZ9Tex
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Private: 80
            - Rationale: Reinforce our friendship with the Aztecs. They are our neighbor, a fellow vassal, and we have a Declaration of Friendship. This prevents any backstabbing and maintains peace on our borders.
            - Public: 80
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: xTEyc70pyXaeJcJv
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a191OjkYu8pabAsWoZu4IH67m3ZABL0dMrpelt2XYMBPKMCk6dOxWhaHFTCO7vN/vmHjaaClpSu9mQ9Xl0ADkTe62x5A8DaicVpzsH8sKv/4OLLqR8wjD3wv72thmsBnSl2sh2XUoJaOlTu/SA7s+lB47Yep+uXTYaCRC2m+1ByyCGoDX9oWsiCB6nDE/gZ5qLIfb4Xh6ourut5XNiLL3ipgjjo27LHq7khUeRlAi7ahw1pbiO1SO7B9Ffrc7TmYvK1DOgg9w2MKxwJxo8MgI0Sm4MB4bZak1Bu9qu0p9BCAzdwYgHAwECZWwoeabEAEXCtGuH5bdHax78ykWeNja11jGPpXJ4RRnHoKVAGsWw9ZSKeMluVh1cAb+zny9SXokx3Gdopn365sTknlrHaluaBT6NW+zVTup77kRsAU8ACp3LGVphenPziQ2Od2y/5y/AO3De160Q8+jX0V5crqVpgg3+EdODq5wUFjgYm5gm95+b6GSOU/f4TwIXJwKiaHscqr5abEsOlveurjD6/CeJqiFDPOEhaCzQyXjTnI6ONO/VnacYX4Y6kkowVyzwLfyhcqTdPRBmdmJ1HPZZfmiH8+Im0Y4NiHRsD//TEilVd5bO88yFL24p8s2ioEFmxMjLttnJxOjPB+34t2rYteQA+yMjtCW/1InF+1zY9ogpuI6lJi51G5Qj6j8Yc0a+ZMzyGf0G4KtwG6tkv3YCj83xQrZkbRC4BjPvVwnxMfJ/zpcYUqcFl04YuhsB3OpPKPsAVjHWgtqVHYs55p2injVUifKs13bMSto0KisYZFFSV35TRRDFE2hiu1WPuQVSMChp1IGHbuZ5pqwld5LXN4FZWbsdWay1PWRIJnQIQFTUPJG3ye+pyNKpnoSOrkHg87vHbAk6CU5vsx2cTgs0dpjjPQ1Z1zMXfxQn+lVPkwclo88H2wpXWIMrObTdC04t9tZsFGi8gQsswgUjFAjeI6sD+fnzUfPL69uDh2tYpWjz0ZhjRlTesArF28lhaa1UMD1pPAUBLuT5xtFlbp92616rwgz0xbM6SgIrEKb35zjXhnC5N6Z/lHnJ9GhsAPu0RoapkcVQAwCckGGWSNG2hwu4b4FhPizJJlfPeeO4MNheodeSQc/9saxuIMMfrck+wyX4EeUjVwcPILoNQ1qZ5AQ+fgjqm10e9LTcs3EeF0IbVmm6k1KyI2yZz9UCZauMC0iFnnpFi/SMPnLcobihvfZxr6h/xokY1OTsV/xuPAECOPVGbP3FApk+rx1CwKpKgEFYz0HfBRmuLzk+BI1Y1PviM+t8NXyRgpRl/htd2Wnzd/EswlKdLYDgfxwJB5dhgNJWmP7WyXDLW6gZ+IzxL3RkucTsJ3Fvdc1WORp9C4ZJ5W85nZnWRZCGTVaVFy36xTGMf6sbytLEtjIR/9jlK76dHI2I9zwQ2h4BeD3UiL/ym/DlhGWXFd+pnjMrdSezobJSKMf0vonHrn6eUSZsc+eghpSZtehngnhQ3ZsKx/PRX9yA3xtPfgh73JCk1EdUp6tRW271u5GAlKClG32DR/Nyt904anocQSuYOYMCrENR+EMfivILdUJtmE6XDV+mgR7fAccbDdDec/aE/aGVgqXVtqHHhlEsDbUqXog0grT/zqaOfprShM8g4/TgHYZQiYrUiL9HFM0Er0/XgL8PwyISKuZHS4jsPJe7aDqIk4/2cw3W+Z1Qbo/T/1jPtacDHy9yyLqDmIJNg4pMZruJTrQkUzTRCmONRktRlrysTDxOlW5YldAPoO7r8UwNQ5PEfEfcp7afqBHOThPgk7xUNOfjXzkzU1goUU13wMzunBUDgInwdo1JwvB6cS4Gcx9aHRYmU9LKbP4pgLF4fFseBxi69EXirzypZ3X+DltmFEi2MsZvRjt31+wP3x6Bj+kaT/rwt/CZqdVyXvscNo7Mogyp5Iqn2xfSqw3OOR1Kg4TCRBouPgB2W+bEUMiWaezh3+SGI8kYsIoSDeYFlVujFz35BPs41pYyBgY5qx7kYlsNBB2/Zn9az7iNqJ6k+v95lDzH30/Bni2+uEiPfD/zDTLaX9ejTg8+avcPiniqJBvkw3u8Pyur4u/AJz6JhCI2wQPXBf+TVaL1pFuXNBEYEZuPy8Y0VwlsWkER4thFBSahKljuG1BXaRwEF9cC2j4gbE99auVWyXL6QtBFSRsEOmwa4eFOYpGBkHoCUn16Kl4q7xlqpoG2v3E1jJUg7bO4Zyylt017FRDdL2/m/4dUwOTJ9np6CUiDm/VpNhQdial14GFKQdP9uuXtABY48hUwqN1AIuwQzqrMJ4YWEDGZIGy4mr2aDuyMcZ+Nwa7H4r5zxxYH2sgwrL0ATCaCr1wEXPciV3nSYDkLeGW8hM5Fkm07ZLHrYB5XjX3skIoVCKemQTxUmvzd5eUiXrDwZfdR98woRBC3tl6ZG0qdBkurPSpcSy6wHUzWHnoqyU8COWBoyryKWCZFsXr3gJ322kgihjt+72SR8W/uYv6DXyauIaCbQjRzHn9kLdDVR3IvoYXu1x1CMnne3A3+Bba7kVKK5+NDbDZlQ3xsXyxHFSxEseSNe85/6VXu5J02UoWDAdxejLHC3ehzTPkOHizWxhhrKfRVbkAE7pE2CqcoJKCXV3UKb9VAfrx83vzAuaSBLhG+7RRUxcA2ZGLV1u5iNrFxeJr6ltHZ3tbGnicJVFmlOGJZjmNtpMRzZEvpLHZrmvmEhmbJp4twup2tYn0/RHfk1lsVptWzBbxHlcw48KfGnIKZLA/xUb3/1nEcSahtWO5w+UtkXqpFYGEh/jatFTZ7/wdnMcxRY+79IMeCrLD9w//cOkcNle13waXFSgQg/qHmB7XYdfDmbUv5z3ZGH/fPLbQuU/6ndmC9hre8VILyEws/gVKGkJz4nFEikdgV+41aXm6AwLZadxryWUIJyMeTcb1EiwXm9WY9HPmd+MDW61pOu5xPG0XnwmQ4if2iWUqa5BCZtB6I3PtfM6zcqP/Fh5M8NOb/Q8B3WtNkqYaVKqz6h5DPf5Th0kKgnjVJ1e5srZkYAeXTwUH42sCvToR021xRV3HAzSvw5ZfRw6QQdx4Jc4ADHFNbooqAzxZ6a05QnU1Q1IVUo30X6GAnz5/AhDEH+CUkBjr4yMwrr8PJgYtNHUFgLAvqTfEgpqrWEjUpW0OjmHNwHi/DAii9IAcnxI5jzfPkSbVpBzCiN8ZjHxS8cGsQzqAXG4BpXf31vojo0Q5+Gu6/QPzrQV8A9vmf10QhdvvCrBVxmNS0e3SueoZz819tVbG3f0g2W3V0GEjZArZIemJ/MhY9okuGF0FJBSeEqTepbKC3yQYuB57NiSGTkbUgCN+j0mQHyA9XSXI8BSuNBK+GtyE2F9IXPDHMNVqzW+ajlxgNzFlUrGJBxadGGJN/4Fp0Bx/FQq72eh7gp6afQzUWjtOVwRBD9U2kAdSGHI/IhPfhxGAYovKihpKKoRqpX54fUTEcgRH4C3H2HxKHELeWQ2R1UjmYGDge55uaWEgtd5kN4PLeCyqgLVA4cj1Q4SkyCkcfJCcU0e9AFplCkGsjETVFKjH8KvPsHuH63geY7QQVFt32FpFCJY9YkB0AicteUAuIp9PcOA35xY4uhjPHt0Yvt0J89Doa3Jve2obGyupz/Bg8qK/dBGMHW2urepY4kOpLnNG1OWKREyqLK1qPdPqaGOsm2xHkcnyeD3xp7V84/EgfXs0UQ0iXnsdKLNg5ek04VymzIBiYZWh/iMJTMGKLm+/LvJR/aJssVykueEX6Ox78wQdUQfp1y6dYiv1O/T/JHck0zcW5BnaNn8LsZO69IlWf9AUGkXWPBe8jfa3WCIeOIXWRwplaVSMGsDTWvCvIkbz5jjWBFrJIhMIkP8p42hV3ECu72tn+/OrkEdyzlwP2gs3bQS7SDIcKuMkNf+mFb4Rnqhh64Yddl4e3gBC/GTGgnj79LhEm6WqJTHCKBIvhDjXGLvNceZP33XM4ixB9AiBOuzhNiLbWoi0lB6zLi+Q1TrsBffOnKdurc55lMPzQa0WCdE1hHPVgHXC661Wl8kYc+yvIC6Us2Mlst2eu3M7hOqg2gYSAFB/AvjnigdwkMc8CPg6jTBjbpuhEC5ts06LOy0vZUKJSfYWe7NENarNDBeyILZPsHKN9KZKgHiK89q89AbnQwi1XumLCAmP7y0CTpbpA5cX9ayLyDFpUSRxEIez1VEG/YkxV9cPSa6OFXlfQsssKaTyF5Pd/m5Harrco7zzLpL7dPjIQwvS31K1lha6xR78TjKbFDCeWE/EA43QK6Zq3MLH17RdwSMbHxdul8uaynWGtqOF7RmNTPTEzfHHPbsI5/UQ6uCgeI9Il1NSLCq3jekrUF/jfvFCTNsV6CYGnzW6svaYZu1IpxKULzCLODS176EFkljuEYBssM+MpVtQzNIRbku9v5slMoV1GtEXHb0P7pk8rJfnXCXgIdtpEA2obFsers6hyTKFpbXVUBfigpjQE077Ld+5vnDFLhewgIhnc1mYyVGHno3Qyudy+YBPWvh5uxUc18R4JMzYdVSMINLLs2IKxieWrJYlPcF/aVzs2SWmky6TVYRUrtumbQnyquZIgwtXU//5qtuX6o+91yQEgKy5KGwAWCgt3NqWH104lCbiOpvigUWLACke5cORIrT4cvyl8J0ukNc4vUQ+eeqpjzjRqHgacWHaCAn8OvhhQqOm8TiFyc9VyrkgekQXqlltK4FisNhGei0FzbMvgvra08L0abHuWGddzWG5AJn4WIl9JVDmC+4Rb3ssemUH0G0dszJh6VTLRLq0vjoVcnqjuiKJde4YEKBIupb0GCPfo+lq+wwZ5f4e3XWAMPsU+uUwvstgR2zGad+dyXOcVui8JihYVaz1A0UQZyzsxtXBFp5VJQPTblNI3awH25ALYStLs5eynv0k5qvUEKwTvehnKAGBW/F5z/hyNVTiMPdxcM6hLhJpEHPta1JDwGdj5mKegob2orGMdJAT/D7GhyhQvjmUS/c5o0dNx8C6Qu0xZVUCjKVmX3BzgC31tad2+q+NxVwFcNM9qky+Z33bLUhot7mORoUMGSg4unHyEp/MTGSsVJI4bY0W6M4cde2hWN5VeQscOlSUomgzdqtHM6B+ajZTKqcTBj//ljbCqoh5uvhL36MT8/NQdaiNL1FCZUogKIBJtrtLN2RvkxntrguiiRQU4y513pwAe99ZFs05WQzK8jtz0hJr9riO4HFG6rkRcxyQyJuNe9dq+xVEoAw9nbM49FyMKENyR/NjUMAfDOq9xoZjBhzwco1VvmnTmTAyvSaJkNRlIIcfNe5zqiAv5CdKccaaimvrhSot8YfCpYKt2dH1SZ497rjZhutqXxCU8kv9jwpBWRV33Gq+8q5Kn4gNIW4R0s5u/LIR/lWxdGjXRTrvXyX94+I4g/QaKJRIZPmdl8aSI1+mZN+AhtXV+GvOW2ZyZSAVFDBmNO+t+lgQ+1xz78KUIpZ+ol8FA6pIVReM9Rg+Q5b4GYynGmysqcObPsw9EGg2pA7Fxj7bdXYqda2yN9ge4q2KUudQ7Sm8LmWybUCcOLqyvzPD9tIp2hE9gOo/gwWF0X2PY8IVwhwMQo4VCueKwU/UAvfgT3akisa7hI+ExMe8XFY+VRRFXDxJxMYNKrIupV8eqb38skh58Emp0lzi8+1dt4zA5YURpKPN0IV7BvW6uJYTqM+VOjBo+eIeAeEL1qrdisNe7qBr6BU/AnPbuQo7p6JRd0H4YSu/gQAdCKM7s/yGy2N1xEOfIyspExj73voDIf48z9PwwYQ7KaLiKQqeiWiqJa4qYlLrmZSoiqKe6M38Rsd00ddcXO826mHtlmkEBqXPWP6S4Ay/Bzt8iaUAZe9m8+GczZU+QB/l82ZWbzGNEdujlKKekYHV0z6cNXhnSLiHJ+7tLrypuYLvm5bVggxy+CbyPqMopSCLTzO9+VlMCLfqzdQGqho7hy3i2JZ7nDo3t5MTB32NjeRf4hGA2/Zjymfd0psWBh9vOavDct8JmMcu78bXXHm1s2ZZFsV7jHozEQdgkfUOdZjHwZPfH0j23yL0yPyTsQLF4SQc1Mfcldj7qWKVbl/eqwRUi689WZkWxa46SGu23fKcnxBOtWXzEbEZY1VvwAwS648pNDxzCxMIdoYhRVZEVnDnqwtDe4vxoWkvbaGcX6Eq2zmRx+frn8GCDAKW68APJRxyNs8jFpl15ynJErR8QZBcu02g/znLvfczLhpUpYJu4rdZUGmqlBR38PZNI2MC2DYQpZe/8p0NtWNAauiSGPiS1tRnKlyVFdxespcfUbeCR5lJILyjGXUmQMqyY4LeeVV4TZxHObxajKQO1+/Ha8X12BImObDuAcHvd/Lf+uHCtJAuQiqi8cxstkojYK02azp/evVqPVvtBNjVzacixZDGnSyoPmv0KYrh68Q4ROnsSLtufdUdrvUvNpFMTVJo8X+NT49ye6H7Q53gOqmHLKqxWGrk7FE26dE3JBcDxyg8dxFMt7OSIizpDxLWBe7ZFq54UTCPRDPT4FJyFow+s+fqG1IEy8LVLHbTfi7rUWusw3MBfKL9W7S6nEvFtFrJBZV1hc1I6HyBgqZCgY0mSwbY+gQwV5CgtDiQ6PkeNKx4nkO15h0HhB+H6KHSWuy3N0ehDvtSo8ls/5f9i9LTzl95X/BH7P7Oq87yoA26mwPA6Pdo+gXZ0ZLaaOL12i6bnDeJbrLhf5GcJ07YJUUmQ0eLUkfaRcF+P9VXch6MimPRX6X305q8J3Aw/v4zXs/TdwftvhcKhshKJJtvwBBnsuWyXYahDS8lONqJJjc4sWC7zMJHrE56Gd9/Kt34jEIlhEu168L54j1U1doHHdaLPgQQV0rxQl21RmYjNJsrafHDw6dCqO9PaSWaT0/Qy8mIg1gS9jrFTH6h888d+nb+jObA+BtbKeyjZXIquhWBgZ3Mnw4u0S4rJovnuBORZcXN0XEo30Vybr/4gi8sBEEkMNics1RmmKi1SE6hjy6lKUpxRKPVHc+is5ewDFgT8jbED6ODvd/0e5sBNok77+1efPZ3EjKbK1HlwmD8v4MQQs+7su0KEQ1en3V7h3Poi2lEiq58btQ8g/Jyk6BZnqeWBMX0NkhK3mmnvJfo5dzZMD3JiAF62lWxswtgGdES7DqE7m8wwXxbZiQ4dgtyTat2axVWggSQ/jNzGcZH12mD658Kxd3UHr1pSHEHD585gNzg0Zx3h5594aBMz+sZNhcYeMvsdfpGYRqQ8XDO9vsKnZELcDuWVgbbUGTA9c8Jo0N7FtOD2/JGkMQLV2Ren2nmjq1v0r7gLvTnhcYj7Hwg7TiOz1x4rwU2GjhYWz2SEoYb36onbkIQKFvrzXG8By0fNkWWZSZijJnVPISy85E2JHDNLjjoJ1DdPHrcguHBIxM1x2yGpoG4EaU+8PQc6S+3msPnK597x0rRNe3gFV6Qs84tgjkHc4CVkWeAWYqauWRxvsQowrI41tuGhnViCSrjZ1Q/Kfadsra8r7AKUk4sF5abpfvhkMpui2ifMHz2FlMETvOwXGv9/2fs61SdPlJEgiMxCUG2RxK5oEujeibQVgcn7w/USIck5sQlSzHTpM9YBSwzRAqAtfF9Vs16yYi21jEZyWwtS/ZzFfnxFAO34MUP2f3Kq3oz66SXPhzmDzfpOidD26UI+90zhu2qq3MYENiZH5/W4d23YF7m76UH7q4U57pVerYz8ba+v6YXk7ngW3XA7HUwo2he8eRLhPclkrSNMKs7TPDWGdxmDY23oOPaAVWBgEybEGbhIpjAhPk7Z3/19rKEAEnI+sgzRKQX5ddr/hTQYe2g2ZmjSfXUvvQlfuC9n0azMb28hr2Tazgz9Tag7QfNVbAmQOKznXl80Ao79I83Eo0bF37ZXnor/tbtoqp4uVEpGuIOkURyRp4+/F39l2i2wKnkLgOeaOJA6fLlisiIOQND1hBFUlqsK7/eXKPqUiiyNSWxE2M2PJewXcfnpF3uALaH91zoWjhtHfm8NJpOk31wyY/NT9X3NXK3NTLhOSAXeXTZaCmFIhmZB5lLdDePl903yDror5YNm647pK5EGZ/Rjbbc+OYAn1egTlRa6z8M3mv8I7IzddOcFbye5BUhG3UIgp+ilE1EFVOR5u95Yczo1sN1vOXGVrX7Tp9R+CcYU1dsKLYk2vebK6s01qg+I6HqX+RNWH5+QSOqn+ae53IzPz6NHhf4YSh3M66l4luganUC1djV2jVwBLifJGR0u5Yck3/Bn5wZdiGgb7uQOkyAV1fCuNunPGVNImKh0+pHTVQYcqY33mAiz8R49/Wr1i62CccsKk+EHKvR6mrzDLEuX/8LBjE5+82pprwQoOGXIlsTlMzhFJI3M6qtXZFCs1csSowMDNgyvQYt8rZHNs5YmO6KWbJwKW2MkJg5JqEMavrPQY9pE7+CNh0UHnnlt6og3sMc978OHtnBndNpciIa+VSFIv10kM5B4duvw/MZw0JTMuT/XkcNeH0F7wl7jM9/vTy5rR/11ex0r0WiMHFpTc/EYpOfeulGFJafdvdjR0YpoSofcMJIZvJ3GLtm8P7HiiHdm2VTAxAXAHjTvqhsiMtl3lACo5jETqjxTRvkrbdgXRuSMbnfpc1U49Y6UqEWcE+D/xP/nMw2Vkr5ykBEsW4khJmHzJ09fbvuqPt0QVE5jUCtG0lvyEqf/U1FqOmHact1R/qiArGr+pvxSPbv3n8hpmDmCNW9iGgP5x2LUerdTrk4KglkaVhfMv9TEyUFFjbwKCUF1vr5OITzSpLIqTetg0p6h6agoAnYdS6xMKyAWVS15FbPHi8AxFAK7d+05dEjygaY+YO37AwdrL9DHPJObWqq/9O1bXcEHnEVpJ9nQgvV9J5q0rOCx3r52ixuZQ20PXtPnRUZiwKa/cnmx8GbucYQUQorpLHi/ase6SYL4NY90gCat0ThPvVCzyrk2UzEbKjEhI34J8oohCBD8X85PyiInk/BsG3Z9r/qRAxDrS2mGL0mVfw+H7uuqLwEClSg9BhuKNWiHKjt44OPu2OAzPPhPq9sl9ZleEnJ0HEBgclMf+F2T/yL5N1fmd1D0/vFUfuG85MR/t6EPMbJ6QmLWPC5Ff4ihNQDUR5TE1dTuguPKCJsN7uS2mmTANw6JeHTPiCo1BGgVSK43DGX4SSGV5XbQtYu5YqaCFP5mhiJf+alaDc7g8dvycTLyPhgQv7iJFpqKwYPOHybu7O+9mAeLq+TRu6FoM9mlBHMDew61tuAXSo4szQSQbmy4gcV0Uw1vunW0dRh7p59V8EMpgoXT8VAdYPpGBkV/5KHJtJTZKGbrhlZCJQ0og7C+MYgXJd2l5IwiVT/xvFF7LritJqd/FyeGSmXnW0Tfxiw3G4OsV1xf8ZOkw/xDQmHTVjd5OqEq2DtnwHOiz1znGwOAHH08aF22pR1PS1HIW07UeG3AoBO8T6jtIOkQJfu8brK5WZODqcRcZdllZys/W0/PsFm+Hw/8Wy+uL/rhoW8XDwP2DFbXU/tdblc8FSz+kK8ftvRqfjYF9dHPBE8u6JEaTL6SBscwoNpeq0LERcItB8vhOKZEYvvwQ/Lt/zAeAc/ahe7jQmT7+uuh2rlkaAkqLoEnWxOKus9vAnvDHJ1HlELeXdzdPW81f1Jt5c/SlWQduIaErr7ZQCDk2p0jHwp0j3zAQtDutQ9Rk6ywduITediwrPKtOmmt8DQKaFT3TAuK5NFUzW+U4XYHB31VUqRzBGrSOl+Q/kUyRFMqZIsWmOYEWWxaJ5AeWMs8Lx149APgXOWeZ1y1inifbzTa7iNKyQfYBxPVI9I76gb5S/2oYa+PBxyrg2IQ8nVC0K9YopA1cZ/EKrMMwj1FVu0FAh7rDPghihCtu0YuY/SfTNfCOt9s2LFlNoInC7FPZEYB8D3XzHhn0svA/RdhHEOosRDVpTGztjSRi703eBSj6MEXr9h1rQEXtiDkSg4faYv/qmaMlEtmDOu7222vK0XprHxiMyezTekDUyGytB8PKvCqACHQrNGk68qSjD2JyJltQl0ZUT503KlsEcfHoUCxTuMyDPgv5UqSYwW/NRFnrX3P6Ra6vv0SXfzQDFG8+zjuYceb554DtiX0SETUdIarocIgTF6c8BRG+anr/vciDlhx1EYsKP7V5owZpf+YCERWc2g3OvspbdiJLKO+e5D5P33vEbYd0OPn1f0ua34f9kE4Ld1y8L+0nI1bz6J3R9T/LXOfTfH5TVc8XnjZ24TR6q5aCBOmujsdVkF+zOPTTbjWGP46GgtkR+dc7EGFuQLiwDGCYyRQuOwIdSQTdr04XS9hkCZB0Jab2y26Na4Z+gP6pWBkEFz1EQCsuY2STlV01mkZEvXneoXL+GcAl3EAV0BR2xLbH8boJyMSznXGipyeK72GnCw6y/U2P0PrLVTZDZacANk8rj/l32XDlZeiSRvYaR3Ape5md1zmcB+g7WRYS68vO8Oxl2oG+9NbfpWBnc1Yp86WXaICPAs6+zvnCSuahegfVCVA2HQJmOpkwQKfsyZ/8dc5TpV117Px1Q1bP+C7Jb8asxtlZRNokpDliiJ9516CW6Cdmr2u+jVMabukafUBOw+bNf3/7ndAGx+er/ye52LGFGTjI5lTWEk56sQRR33m3m/jicIeKhGRZEDf9y7xtxTOma/FNqAQ906N9JFFGQ+o7OUGPe/8cOJQ9TCAgjao9dzoDaoXhY25davLEXZKJD1y1jUq0YcXwJeh2ipM2vecwBOLbUnqm+Tusc86xGLkDK7CFJusSyOs2ilKq9anloXT5SbyG/IH2OngczcMBHgduQK/ebskj/pjI7w02VqEXeYppgiGCuPt8HeQh4i5hnRDHNLEdFYnK3kAuHCRc3gLxSyIPOpNLB6W79HFcfnGXqcCkB/Ox/0pYMhXLPknaZYPvBlpl0b85Nsgkc0NCu3ZZeLVGTKx58AJDZQxIukQhZsx4EED87iNbeDDDEx2IaTyGcL60+K9CIS5OhfcJD/txaOHtKQM6T1POrPYniqeBtYJ236o8ZlofWWsen/q+HX4Fxue2y1z/8qbK5KgF/BgMzz8tgFmQPCmmGN9VtPW31JjH3DcwEhgVLtuLxmr6ktfuDrXKy10snROAgb78iao4eo8UDP8gbiLKlUpSzMLOnNMO8NDnfDFsJNVfmxI/uhEzDFpAxyM6b4HIvjkztcjG9MrGs+yoZeVcxqE/n/vJbuLF22EEYueWeM4ERIyMBGfaqhmERL6khNrmLD5Kj00c2HSohnrSNHfajcL8duHu8YD+0ZjWGyWfAu6XkH6Oawc7U62pc7R+CNFf7pzvjLL8fi7dGcF8rtsEAitZ3c/7JAXlcRwHTdvMeC4DEhrXJsEWYDreegfRlfBbMLxaAc5yTuPQatWbXJfeoJR3UltNRdM8KT8R7q4rFzbSP5/HWybyw2IF/WWkytRDiMnVDB4aivcMC0aTBE5ALQ7P3kWtLrhzQ3iTvQjezc4sS8/5pthnWhfR8Yy7FdrgTJ0uTug4Affm0bvHo+k7d6MDgGp8/o05svxMdhWfVVuflgj6uITHMOy3aDsVeVfgiud8CmTRfeItwSD3QnWl271VRmxf0zfqQodJI1WOSPfsUk10T5SN9U7GkEa1HpLDv2LyZL0kglWM6xqm+h9KKk6aNBvhYxptWeRJyd5xZiDuNaK6OQ0TGUZX0GKNZmsRDEDYd+QDzVgi+HFd7yteagYjU8QyJOvjLhLp3wLqRAkSVbvzwuPXVWTVR4NaJHmEmA+yNAn76RWuEuMyi9vXAUTszZNq2e7W8nH+ZA8eb89JQ2jZ3porQrH+bYOa0fm3uHyLggEV7I5pLRzOltodGHVQjslEwMZ8DWHNH6KbSxODBAKiwKsJTAJIltoisQqZSa/em9/nqaFMCdyhoMBbwwykBsqJY89IpKhsCa1B7hLLL+Joq0v1oaLXYsy86d0srBhsBNJaIX8KYhrEpQW2eIMsj4S3j6rB2xf+bgtd/tROWXdRkb6QYsx+0th1Qc5mZcFfuhdFq1sHardH2qYomn/FbkklgpeAwprMeAMFSAgIJRZJL/mOEi3LcrVUtPvFNaappWrpihLqtSYPEqrPeifXM9oR70toFGytf6OEoDCoBdPw1ExHbwYehuCepNri+S46HZCkA2IfK4i6RiNVu/TKits+HMr00hsutBiOviy/9xl+MIkIvMA5rNxPQipPCgW+jgNPr3L/yCBPL6os8NSb9eWi5B9kkDkZ4pIpE1Wdne/0G6jJWlAsqklcSWDg1JRslPp7rxlzh2kh6EawRQ9JVM+MRc1mjDn0nQ4SIbjqccP8LIzSAEWYs2g/vb3OmZUEyalrWkLOcbUZYi4QFaF8SujNJWj+3zBHX4NebtFVkt7GcawQC3m1kmIUy2fhIk3EYg1WnLWl/mn3iyvabuLm2RpmRiyRXYPKNJpETxu5Woe05E/umdLTvSXcqt1meEe2Xi3HON3zBp5Y+4QFCI/Ob2Zt3CDMT+yEDhiDpCZtLmaByUgTyniIo5LSfI48IPAhTkcWr9tFqMTodXR1HoS4Vl+1DZdYijo8tjXFCyPFBITGnn2mUt/xAy0RCTQgYn0gbqIZiv9hgKPy97TMfwfA4AN2nMin1hrPIkSkWXoiVVTRJAeVXTUT93CNMmtii7U6J097j5snult56pMiho9MX/TL7SX+k0J01+0jtMFe7eDXN0IpfMvw5sJjMqf8MCwmGkbIeoN+BZ78SBdSy5oU6XS6c7lxQJchUmC6AKPI09EwSAY0yEnWhk03EIa+I7L9VL9GdHRBZ8cDhkzCCti3YrwMHayF9ICepK9VRlJxY3FK2o/SaA6QbUvA+z8OQizXBPuKE5eLm+0y59u7ShDe8SCtV2143jaL1EFFWJdAsq6IciR6eCGHqeKwVclStBeo2tiCR0X9OL5h7owjDulTBN0xRWAQoDnE1YwXZtveKfNr4r5Lu1VAy4LlGhqFSi26N+0diAjjIjz7XEUp5u2bzB47iMfWZvGpTWXThg5ss1/T+C/QiirYFVY9s4MFKIGmN1Ki8aPg+0GFhe/ks8YgYgw/l2dxnpS0FmE9kWP5eQNkJWkscYTUZIbmj7uZ7S7eDM8funEartsYMGOALp6sJtZxEeZN5HM7ttvtWmsm3WPxNvETKQXSmdg6M2o/hL2bDO2SaKV7UWS+Zhfd8OV1fnC+idWsNEZ9PXZ+0HTx9NnbHYjU00ud9jKS4aiqAnwfpDVU0rjly8FmC2b6JxAMI3+Glw8HbV/1mPKLxKzos7E23r7NlNGOSoIrzxR5yCNEuUXCIbR/aBQrUDZPQkmcXTrk/K9ZHdQH2Iu2ke3qdCN0nbmTpiWksAwkM3/jf6nk1VKh1HpVoiknDSXdK77punpffhsU6To8UIy+kFY+UJItzRHYNxoIoAvqjDcVOOv1Bp6M04FwMJ6ZFxXaDrgLJcRDQvPEgFDMJ0BW4LPGBxDiAflFHhqLZZgnp/2TaiwHGJJuYAjzuNcVL0mC9r/witFqNlLnoWQ6FV/If+ODv6CWUCdyxuPJLMiXsTyGVHxPuWz2gXdZgazXRM4thDarXjxW47U+xMQEIKUyMEOPY2cyt2io9k5fEPNeQB80L/WtQxKRVytRNxh9ncUpNZR1mDQvnKn2pWaN9+UZA0eBtThLziRpLGwgsuLMkykZyZOnS/AIHiGChqvFi0tdoGelvjUoVdwEtHvY/OYRw4u780kvjlVAWgm9qLJcxjWVYw/WSpfRU1kyL1jqIurr8PMezDbmHF6VBlR2LAUd7aM8np+EXSKlE0GhJWLAdvy4MQG5RpmwVRb84GWscKkYNhnjrQgN3Qwc0wHdgmCo0IpkmIyp6ipcmAhJyca21cn1MhRBHG823efj7/x1pq89dnCCYvno29HxQn+kb/tI4Uez1ShOCa+N+CRGTLjX04U9xSIv7iS89aUZuSYWmDqW13Qif3TefGf8NOuxYdEq5IKrh/oUK/uxVUx8CcNhEdRzucfXrMgwYo7/mfoQhQrV4pmp+GNS/3EQW08wBi4zCL+LTzmuVAn9wwLxRclh4HzzNzZPINMBCcZmteYEXIwmBMLb86w1VuvCxE3INmVvqKA/NnNjOULoO3EcQ20JCXwA7qIc1v7fxZWpgW5tHdrXeYcG49yRQiXR2++NZfI8s+Eb77SMRIBJ6LFzOjs3IF32LQqNxcmusJrL6PL9yAvCGGp6tnVsBEZslsN+RAxZzr2H7RSdvnArwkgfCzSOrmVwRE0oXhPDsqYW6TOiOl2eEH1qWJNqpDH0jBE1nrd8dFZxi6xY/LS99boI1RE94T0SdNFFFcf7GYvqXmX/ygrG+fVzWb1gu1vqI3RupwFgBieKzOB7qd5bnP3L0L4hgZuR27OGm45b3yjrfwcroj5XUyyR4+/zNjov3n4H11+0ZUCBdBeuzD8kwcfpg9pKNlB48zEVOE9kOeoyW4ILHgdC4g3WpJOM4AJsaQhAAImpjB8JN3Z+cV5LnPFsU88ovzoPQvX+wesJLJNs1Hf53K+aolVCx5CJ0A+ywh4/DtKy79w0FWBFq1kVnJJ6Mrwa+VgDmbnjwZQ3b+vQwpTg4ctBuTPmVc9X8ePH+TW/wwY10PUPGErgpXFodu4DTvCxVAN27NPtNulxMdUa+pUu/jhlW7tYmBXrK/JF72Qwz5/7yGG69bD+dcPFK8/5PoZrxbPCqdnQmKzyaB8D4BUlKl5/mA1b/ncBiLc8WzfugyMwJ9RX9+zflIX78K+fJN4LOP+QcE3dLT3xCqAqTERUapqRCp2+ny3GIcZIbW8fgPrgz2IwZrYyjys5Ih8mwxvjU3gKx+b3U0zMtF1c/LuxrQPgjHzo3yfDSVL2dPY2aqzspgcNiUZiQY1OTcAS2pBNA9PilLUaon1i5DM9wowNlA7qN9kAesDBBcl2cDD9wiQSZeMIQdTYmwQo/STqK7ZVde59lHyEpqf5CJyN5Yh1KhDEUHOzy3HkD9OY4lB2fRqmSYuKu3nwX1Ookrbw3CQccqJ+vcaHvr8EMdFZ11gohk7BG5ULZcFATusgzQL+q4IF6m6WO+aiYRfGXJBG2jBhmHSm0IGK6PkkVU8AVjkPCzdxY7Xuc9XworAdr7QQUk1JrCs2kv/H4ZxUWIf09ThWzq9+E+LnsjmIAxlqIidfpNxrmfA2KsT+NHF+naCxq7NFkjb0r542cbb7C7MP7mp17AWv4ARY4TXslSNqN40M7k0Hw75bv0TTI2QTrfeUMw9eexeJx2mxNwl5vRGIYCM0YXHMPAuoaKxFAIn2tszp18qsvnzPk1Htz9MMcxc8zAVZN9a0LT52lehz3wrjY7MVHugNL0P16q/TiqXUPqi8IrZg8gJc0uRGBnUy8Edx7KZ8DO5sdHOJUuJGVvDnodh+o4+D39QNjgaEPCWaXpRCMw4FqfR0uVkoe70hwgBL+ztcGtlHDFIq2nKi3b+dBEZRoCxD1mJna5EB5sL/pwzG/K8KgX3NrqFY1Si11Z5EUh5n4UXggBIy7P66VBc+9pqf8WyqL6NUVuj2AF5TU1UIrRjshupnFnRs3s+7q3Aw1SgAypMKHBBNY56zrB1zVynaILtsn+ERqBZAkcX0wCrDsnqLC2jkCJft8wO2cYGX9JaFYJKTZE5bnuj0Ath2YmzJokJ++mMiZgH42G22GtzP87W2QlFRofbRfWSPlcLJaAJyI0L8Epb9Rf8NysZ/b7RhPLH1UlmVJ2cmZV3Vf+oshKHL9dwSUVZvOvzmYXcq9pqWo0MZootQdu+EoE0HMFRgBKN5f51UGqOj9q3Zv6EGLZa/P4kKTMkJKLNlf0PCLBlZLD+HaTCyLtdc0608Bx24HokthhVoISn3UjG3D4nyI9p9DSioKMVMAC41yeyDnQ+eZ1PW1QDfx8KHKtOmr17wIgcsFB7cKP2DHo1dDC+n6Dnvs88dDFRkFWKaZpIBOWAnSVETSlpyL6gm5lQ7GF92mYZEmsy4BaawlfdAV8UhZpN9B5pN7Jc94V5J3tiya9c9PvWtF69+MkcQCTbaA9QQZMNH18lyIhq7wLZC+iymfm/IwLlH2KCQPgGVjckps+VKMjFQl1JDdWUXEC6UNlbHx4P0+sBvIvdeDm7aY/vVuGc9ecZcaVD8uNFxbJPDTpPjPyf4I47s4V3DPBHzDycyYYLwTBKnoJmhPg5lsUMqzEMleiTLS6lYiFmqVFst4YNrHDHz8xHaFKCkeGWtdIDt7y9tq0Efjfc8dBSbODtOo5vJAaGmMZkNIpnEJpi05wmRowWXCtI18Wwt/zZesBjtWkrrVH4O8eejH+Mq0Fksg5o43bnLwSkz+vzaHdv7gxyPC8gT66a4eKICQzw+3x2ZQlmHqWCRhNVuFA9g+6Jq8DTyz+C/qcEpNNHWJ0yF/K2vKklilWbiOU/kZ001C4d+8lgwAfD4xO5nhJJqZTBSfRfavWIp4U9cQHqnGI312CejKWL4XJNA7sxPRtMWIVQo5T1e4MNVflpgQ7G1V2TcQo6GMEyJq9uzb598oWdg0v6ZEMc9tIl3XiPaEReZhf62aq+IlEqV4+1zpDJk3jo46KyLIY6pbst+RUprTSs5Bees2yUBPO07qjXgjZ+jInt4E4IVD+cM/QQK3L/NKuVvwDoEQdhB9nJvbL8WmAupJtgfbZKRwArICg1u+DgKR7F4OLViWbnfNXRuSikmUcRMDkv5pNVK3WuSbYiDxWfSJUBehKbzyqV01ED4xJ/0bWHjQfv7nqAAc4ooR0eU5hrG3I9jyNgxpkUnK2jaTsG1IVsDOtPBY4jnxPVSw42b7byPkKrvf+IgbYoB5Z2BwktW5K1r4EMra7nm4S3Dg1XfC0MTUgqV9ssPWLm9nZ2QlB7abj3b7PdeMlpd1sKmAgH0OUEGZQnknjWXk+CDcwD6NMV0aGAqh50hKRW7NyiCwqT+RHb1zXMqpf0mZM3E7C+TN4mhL992bYA1k7odQ/qqBXB6RQZvYiy87EhPs96YAu7BT5Uflx82ZRA/c1LUD7FgRndKznrNNoRwvX8M5xmBH1N4akfBiTIMxIayAxR/VIR4VmG6xeH5963qUt6mkrhO3NQox6zXe8CwYpTHol2IOXHtpdW2JpWN7MTFQmvpXQ8P5pi91f6Avlx/Ex1VpN13XmagiS7+AIIldHLjvpB/yCyHlV+btt0MzN2PmK7LQU2tVyMJQw+X3he5eAUsBxbCuOEHRqdiDD7Ak5/js9fOVoTZM3ghlxNabCoQB7l3yMy5geJrMS2pquVNjqfeqhylJcASTVsXDPaxOIbwvm3F/FpobJuaPmumu4Xi0AWAGpyH/81n2xrLOPn7v2H9n/LyxrLXsv/RrZ+ODxt9ZM3U7EaCN6ulHw44GqYiiMpry3JjCziy90c6rHlpy/eR7r7mkwS1RdniRG480HN9Mt0GlSHoeVJNuG50kjYnIiqFDuMQKWvJsRJCie1BeYGSawuQFr5ArEhjf5lykNEXeeuwbMnZePz7qTJcwcDomaz5F/CpBYN70Uhvumly8VMBuJJcb67YKGu5U+CmcZTjgM3VsBpRfX74ElcHbecKYRo9EhTfLAXh3Hd0+khblbGTDb1ZXoE5vWmuzO6ssn+Zu1JYVkFKfW8rTO29NrxOcQS5vXr+uaBMuJ+3micvQjUL7RDVck6X5gc3pM03y558r5u7FdjbcDm8KcxwapHvjbLjZ62Z3qi+t5UD4BieubIRAhZ9H9L7XD4McZU/Dk0063ZAHmP5+baRBCvVWBR2TPaZYi7dm3QEYS0EdIGTFmfjzp+eccU9qxVp/bDFoT9CYJBB7SJgiQu8WwtauIbEbUTbAcUG71AYkj70KgoQ95S6WbwnwhvYD2gEzL9DxCzr9+iyTSENel+CMvHH506/tGejJpZu48NkVJtaKn+uv5M8dIjDSYQtBtit7wuFN1JLkk71h0nuHsahpHnB4YhkXZg0iRS/2cf0Ovm8LoyusvNpzOWIUQaaKNBRNwVjkr3DplmC/StTBR09HF21sT07kbVsFXCdCcTde6dm6Mqa2ZiMl8tdS+HVqmngf6c10gTR5x9OJ9uImTjiP0PTRgbGnZ7qAvrXnhvxvbRlNSHYcqvkLLk1/At3nbGTHkzqKnbFT04CVINPZxoUNqCCF49zw4JudJoeRSdXUpJ+wp9d+lNw8v5POYKRZZzjatEaZpKH15fkRHx9SnobR9yj0U3Iioywb5F5BXOe8PNz4k1DUYx5IuHP6MLyNj0cLFEAcN1ixy9ZRp/J1LwFwtjxDxndSW+2basec+ImJCTPAvBNjxH4/pj1PovDidCDSEeUbb+3y7TCngSIx5dazJeMmLZ0CsxZiQb9IWXYN+5Pc204/5G70/HjXDKP2pCF+R0xLAALXk/GN+cw9gRSLFbhK3BYeylDUOFf56rcMRNo0AmOzRQnjp+VKtQjM5bWWdDV6W+bFvYbguJU8SuLnDHKRrhzwWcukaTSj6TVDpo+iGBDuAK3QAvMK6oGiqtrs6DLOJvwvkT5YWkSSms0w5WfxutSQh5gEr5cuuu6Bh3GfC6nl7b2Wy7QidQJNOS88VGf9nV1MhjU63n8BgFgJmmWeoYc0KuqQZCbQtC3Au0a1wl+odddlNlX6Iq54N+SEBnLjwXHlwe9yjxzmZLH36FVzwEtTCOmC6RcgtFDu9vEYV3GpHVe72D9JvTLrHkKTXoha377NGENUoxJ5t8yOJXrWOkbNtzfJQSUNeuqdFdIuNGvZizSA3tnUbfj5Rbkzfe95lFKhfcKWIOh7jM35eHARuT0hQoqTaIIvWJObB3xlZPtV9g6WiXNsD1ZjutfGRic+h7KLthYowiAm72Fb7tDV4poJLieLfyVYL9NSlBPNvWpqKdbsS24Jmk0jg6RcLHFnlaaPADs2bX7gC5i+GXkgeZp43XsQ9MqBFhU4GwOpaAOGyRnQLen20us7ekmkf6DvNXLAmaassv27hSyEVnPjDn2QFn4ug7JD/6RDTS8v1qckR5zbQHZytlFuoEUU2YCGEDVTveoWLVRUBz0cjLzubgo/1gbEw8cmdM2QsPZ2TNN6AB+Z2CfaX/MV+PnJ5GysQyNs97cRbcNUdzB4LZKLSQaVoW2rtEWHaBY6Zi7HPvgFZ3TkdGOPMnt0c/GHJXktAosK96P4frvGo90XFtBbVmFBwXkqUBjD0ZsKhas3KpXCWCztuyaY012qJEhbemKrDtLvbFJ6ttKxTx782EdmEqk4gmCYdNEK1lSRSIYid73DseEGzLGcrrBoCv4BRg1bvAZ/+E38EYNkDKBJ3weqBpBd8hSBxUfkYoa4/h3sP14G+mf7uQf4joSPO7fi3xKSs39zIvqNAhFEbUzNeE6de03zd6W8WO9FmhcaNHBWhoAwcnnIOLtQiAY5JDdECWXvMOnkKNJ48itRVVQCAJ8c29uDSwSQKrMgrqwbhpu3nBohBYvCVOSw8/gELt+5Bl18jWaV1akUZFwq6Go8kMbWLhec3wYOyFBZb7liGSTY23x+K0X8CXbXw2T3s53bCExKcmvcf61y9hCWMIZH/oP9JTGUUq0viApSo6nFqadkmpHW1DYsmAK0dHA6gOwbR54OFdgmiWbDecndbmEAz9dX2HXa9Pxd5Uy5P5Sz+bVpzsgrf75WAnjV2lpr3HFawYcKSVPC6mh8HWkGLv55nyPdxAfsGvh5Bd0uhb5csk47yLJUDJPKs0NTsaMhnP4K6Wp+JGOfo2/gxqJp9gV3RMNBHNfly4BnpoSoClNOz13VVz+IWVGwyDdhuUJffAjX1Aqyeasv3zBrFejuUoYl60KVNRHiMFQGRAvtAQiskZZEhJbyB2BV83fv3RryySDwSFK0+gHTT20A7PQ3e80aKlXWdXEV6IHsnRt3Sq57ZOMydVQqFtOQIAhQcsAzVcc3hjUNjXIQ7E4mmA7x7i6WOg8BneQo+s9ut2xhXGty68/O4Hp4OXbydePWQOLG5EdbbTJV7o5NEkDQpqh9s7LI4Qe5PDYY7zObaSjOzw+B4GyYvnOBIByDDy9i+EenCZvjMa3WTQvBlA+UHCKH4UjnTgTVWbraDPfhWIvFHS8THp2qCbajnERKtglj0+e1BN1nV8XcfYhGVM36FPdrPX8ROESEKsFsDlqNuy12UYooivef5c/zFmhVZ/LME7bfZWbfZiPxLEHLiIXbWEsJA69eJSpuAQolG91X55ll7PaxF8HpoiZX9rPlHqD0A4VUy1Wd8+43+a5C8epuK4/A5Z50eAv4QB5HZPl93MYXjVebddEg/S4B4ZZwlgMZTXa+TA73b3cJdtl0msmKWbu1gSrYUROIMkKHzeKjXxJMfl9rVto2KpPh4/S7vjz4uD9F+SCbwkqjU8GUyDwlguIkuasZ/69GiKGv82/tjd364RLT28ECkQmWlLiuMm+13vMNkrF7rpwltTfvXn7O2zJ3+IRt/PP4iaW8rrs5q82aD40yYd/COH7/GASe7zUNJuV0UbgSPaombUZxHw+WuKyqwHqnQjx5cQASbeg4sFrQYeMFzDeoVPuWp2SqSYeNNDmPrui0q3leexMEzDZt/xgiWF1YJQmFWu/aHKWfWVegEjBBlnNcHpiXymvVsY9lfN99ZJQkjkPNEFThvOYvOC+k/2RVvNRxvq2hBJ3ICxIQyYaeVTst8SFcNbFaBMjTypg/5hL02FqW9s4xX8fp59M9uHhC4Vkhj5kp/kw7Ix8UOSCkZJIDDNLzSGWImG9xxutgngNKyO+mqLjaRZ4JfgvMLzej0omLSm3FEyMfNOOX+9Ftq8rasYtTeup78UHW+PLuQGK2X3vYbxd926aShtm2DDK8v+WbmwvXX7p8zc1sFMprZK54lknpxKdANG7a5cRNZDoabmGIdk5k4uBLhtPWPUV6A3U8nZQxh8CIoFSHbEgFBTXqe71hHGPemJ49m3EKFhLR9K5yA/o0w+jIid9rsJ0zYojumTd51qtzQS2eYaMnE3Dp+vhrckp0qL3Vlwu9gmnrGIP2ehjShOC6oPXhpxmzxWFNcaqj1aUDK82vschAzX2NPkdMkvwyAYRxMFWfkO3EzEPjzCP3TnXwHVbumEa6GDd55T+urytrZhX3EAmR9RSgoctgPaHDA/rqjxAhCjH0+BZDa5fjZNQRwq2pFUU2H7R1CI/2gXNKdqG2c6PK2C8mEOwvG4Kp86mf5SWM8t3DjcfvzMsHLmPQ0NMB4acOPXjvcJkAR+V0r+cs3eA9G5YomVNSJu6voD3TSo/tRL36/8KwapcLu2xYkCtIljWXIwoxL+JBvPcIbpxXC+avhakym0v+h80m3kmVA6tbejz3crM+05mmuWVpnDBcbYICjrufvCLttU0tyEVwXEVkz/ssNtiKqzMI6f6kkhEkDejxEYlYwQlDEhokDil5bwC9rLRRWONDwG5Oa2zlPokDSWN1GdAG4ScB1pDXpLXtTkDCOqDWTXPRWWH+h/FCZqP8sBxDIrYbN1wPkuGeo9SlnEVMp1Qg8OT8GlNgX+hPaWNFTyV07Ykesmx3ZBPIk15FVzVcrnrjEUJPuJSX0KiEsyCFA4lLBb+DmZZfjNhS0Tn6sGbBFNYmjWSj3z24/5O8lsBSi2ajeojbzurU8PadjycTfixl/tRbMed/2rqxidplLTK6KYF+WiHDj4f63Bhw2vhVG94v1nmC0UwcSvy728dER7zkPxT1HXAVaizk4x4f+IEb6IynPleoWDccS2k4NDuOQDIJ0AfFoUmYT0R+9AdLHrLNiPRZ1GbbeNnqKOiZh9UZ8wwq4tjw1OrowEjf9f9VznVq0bn6wGh5Q7Ju1osonYw2t/A15Pen1jOF1+/JtqKNDmA3XiMkzI34Oe6UN7Yp4q1+QbUw9vPNQNAHkKNBpaGA0pFyqLN4MtFtTFipqPxA4zysm/oJ1LX+MF4Gy6cBWjVWmBambkjMpLSIeXnAYu/wvxeykey4t527rZeXOFvjTA6zDBtnvcms9eFWwXp2Wh5h1ZiM1bB20PECcpZ/NYCKn7Xvi7+S4W9JWe7X9xkrb/oIzggNdKzBgROUyoay5E524RSVRfWTkguIoI3kN0igmFHjcMQMDhw5vVzTH//GDRzSI4h9TbJUVaBaORoG8fg4mpKjFVdXGYmJU6Pi/JyMiMgG7obLpI7uCcyvEaGl+XEuj6KXiCY641ApS+n1Ve3Y3+DbYCkNN2ajyg3GfzXk2o1n1/NHg0hzUecwVgSuwnxie2Ub9ObJE9p8H0Rj1x2F/z6M0cAgBi6bIZYKonf0VtQA9O404kgqhXeBTIyXxjMTQm/v773Ent3DsLORhIZb4d1fCqpiu3kDcftVHwn9opK8NgiVkV3avuz4hu4NdzuXbF2O0bL7Y4IPwm1W3sLsG8yoSIlCEMZMpflDZDjEWPcWEqybv6mpsGKYziF1UV4I8Rm9EeI5H1LkBO2+E1uNILJsH83WnBt6bEQ9GcQIiPfMPaT9aPV92doAIqZOsvnWavAXbHlTRFGDuCSMC7mCxu4U4Jg9QW6SxWOZaFVgc770BgthgFBb23U9SQx2M9q3RiHPumewbeottiZKQcXbANNl1IVb3OzrVjLKxdtYJtHyaZGO8ufJmwUaHPDo/ltncbJ0hig3CwJdj5Hg2kALw3QNallSGrIL8EgwkDNPdVzm1NUsuhdBJZChwMFs8177LsJeCY+yMbVz2PsSPEFbHXyfqg3qQ2Pu0HmLn1p0gBh6sjYYALzA7arEDq84F44V3I4ZcBg8mBkhYkXwwzQPX/oVO3qUCL2md0G8UbekU1eqLw48dBcxezg+m6cXpz0hhwA6B4lCRmC4bqvHkctH7e4nAsKPz2iCpiDarSC6YjEZBnZemvnOrrb+SjR7v5J8iFtZi+uz7EE+Mkpg+6+6KLhUMczJ0xmT3lW9iy4WmCQgmoQ3kpWV+oFgv+TSM81MwKMF6mrw5vqLjPCntjYDWr0ClrHqyENvUFDuEKcmc9vQWgAh4jwgshSQvN3BHdf/aVl0GXMLmURRcCpjwMJkw+YpyQIsT34NLrZXixPrwt4RvMpvbRvvsf/R/LaHHt8q28NexzPWGSu8Vk34U6QLixTcl3xNhGZ6WZ6bDBuSAFTXujAkk9XwJKzSCvihD+5+CW3t3Qdzq3rgLdBf3zJXIOO7piTg8ssM05x6DK5j6jYs3zrdEk0Ax9f69VY/wuF9O1z0uYXUO5pAYglCTk+GL3x38lw/Hlmxh447sVEcX6y8F9Y4RNSYe44sHZGlNmXr3L0wQUgq6IyiFOdlv1Eh5fMo3ArxYFhs/pZe0wT7uoaVLQincJ2Xc8P/sXlqtLwo7h0h98VEy+TbodeZO3zzGawOgn8j+d2EthzWexBVHUCz+sq3ho62duyurC/UMzXAhYAdFXTjgXT8NfHwDUYk+DWI/B5CYsqh1q22C/PGRHWF/RtdKqIh3yfn81EK7QP9Hl0pPnQSapXljeClpHBji8EEb4YEFmi2UlkwJLFNUmb8teSu9LerJ81I5n+1ovXSGdNDYUn7KRvFXebohrH2/wEbeQollE5fhiL607KKUwQ/os6FndNP4jSnsnt9iEjluuJ76d8fAZA9hbswzVWrQ5n2opyfXSJdvawQB2OZoqHpmEaWsIjW1AV6pyxo3spJToka0D3qAZxZ4Tq+Vz4frweek4QEsH8W4/hjM9wtFZFGe9LreIacHK3vQ83eJT8gZqdUOe7OVGv7n4Jp/COGpL6OvghuoU0JqwZGW2ZB8NtUt3BRV9YS5ql5WpFvAbRF1eIwKt8S2RDEUrOaA6r7Ci+VB7EBdNOeqN6zxBaJ3N/GepmlSPWi9u4SkuTzMoC3Wnx/QDSHQmhAtuU+Qo7/op9Mt4/qJ3fhNTQncGiL7ENd/NqOtChoOJrvQyuHTrwuHClL7kcJAOmeIvnVikFzW/HJ5BISaAQxDbN4bvNxLuMG3nd2F6Rnm4H4Mq+qxq60Pj4WZFKHejR63AEgHv1wa0ON2fbK2PFw2xHvYHfp2hXZDVZHobLR8cPpuLxA9VLsmmriMe7jSCK/rcBV+GZQKV5Re8lspWizBD3YMREgV0yyYLJIpuRG4oUYT2+hH6Ybav+NY2lbU8mwO2W1KD/0oPAlG5gRSUviUl62JaUj5YkU9oH42cJH+k1aY8wcvqXVhVCeOyNGx/UGs/T/gc833NTUta8v6fs4GHc5217CVfjyJwfR7Gmw/X/KReuF9g+NsPGNvYKpbLIWZvps1ME93vd4XxHM1kHimdTqvhDMfYMEfPgpgCGINsLJKP22b0TIiI0LVGF26AmvRruodRzZdDXYAx7qP8xjzdu5rw9qrZsux72fZu/XHy7uM8ctrx2i/j2/2l5JFZkoOW4NOrTJGfVhD/kfxz1Oo4HmuH+T68QtvlxqOxRPESIJhQAIIXhkT+3THKn+jsRMb6DCOrv4iolldi70ZUVmiTeiHCMX+FgUhDxhUhfFGKykpoU/LVADxwZfEnv3/WHcaaobhx8ayra3rAGkTU7CBMxgqmxspB/n9lgToAel3Hi7vheTCj+iMDZn20pfOtT4e2V9HCyqyB0qHOtYXLaxYCTjF/7pkf6AxUDcS4Znt1+HKJQeiyqiXQboDkGadtuP1IFk/xBVw0Y1Rb9ZxP820CaogSzBGsqNRpt7t3hKFPJc/DWoBF8Wx/IoGG50q7qjvvNx05+zkgdaaYAA1ofaWXkuJQTwLNYk76/9XfaddoUFbdNAJ/c1N9qhGsWYMks+F9l6oUo5zivhV0A6v5eznJTeD737xP+oo/Veeh+Ty1Pg8ThqbJgfd7G6h44i3kZQnaxLHUMRx3HFqzBKLrgG5//dO+NnFq/ohrhChx5jfnfgRWhhyFrCPVT9SnHRaWXAbFMRWLfEFBYN1hbA6wERgKNdo3aPjY88UerRxtguLM3FJUSJMw8BBNw2V4Ke4OH1EU/djl8FlJVmxyu7COonO9+eCRLIT7grOP/41tQI448hgpkH9JL+kdME6CeLptF+GkmcSlK31Yw9//MXUX2kPTkW5gEooq3B3AIuVazeO5a+Bvqp+ileMgCax5JJ63Y2Ed+8tAuEbOrhTx7sEzQlVJ4wtZEldnoHApqmNwOF9rmufikGImUmBkeX8IeAexTGfUGe0/KbLkX96UQetJW2xXg8vmIHpKfJa5Y19DjFdfwvIDIOfpuA1PkS/My1xRUnrz9Tyf4+xRnYm7ZNI3tveoHPD8lQDlF3skTdSAIZ3/zKW22F4XA088apBUITNvKAEDL+7CItxHxa6e71KItIVvsxRIHkcPTLl0J+XdmCAcDaf+g2987FovDttkl/2RlRBaFmF00VHCVWPCsDYYnIkSDZIZFHmcEMblCY51X3beUb7tw21YGyCXbrX5Z63cLDRGqPVT4l6nfdQ+uV+alVakcA63Ih+/sFZycPCmnuT2IiKDVgnaLWxuAeBfGYxEmn/vSYoybHHtYgH2d2Puf0k3bMqTrhEpwdHTdIL9PnDr3ipnAOH2j+eEaGKgd5sPppxtpOhoaX+jT+ALIYSUVmiDXWaFDq70c3hne48tm84cXhM/S/hdwcEMDRWSzIkKwdS0Im+xHGBf99wIx71clgKE8n6xBsn+g1O1nIJ2DhBbbakhofluMCLghtg5/7mgMH+9QoiBwxmv8+JEjhGo3GEG0ExTBbZeKfIw2GqRZ3Uz2CM00Fgb4SfV6xGABsmxMIqiMesiSpUd3N24y12l9N3zl283Uo8Vd3ENkCPoSE2Ymif7V0TX4FWJmXhSd7Y88ArBex6Nquix/nIiPM4A9TcjWALRP2EpC6xiwjnDg9kjnDotEzVTL+Pg0D5IEbXSx6MGnF/3VA80sBV3PZS+xN3dlA+PPC9ZgRKwSgN3/EvsFgovgdZd0k1tbcHoH0hoCogbCO1mqt2+F7yPjqQ7kA/pHyUQWXMUl/e8FdjCZeKP9PUccYRoVmpRVvoEbZJsRAP8nJr+baryFGxeNkCaIO7aR855OkFPKGfhnRem86ipVzLaWA4G9z5NzsxACRMSJkspSodWTuS1TjWBZM1pPRK961Q+PhfLaINqVp/4huJ29w/Cwg8ggzy2Oft2fdmtluNVEbXP7Tn0OVJRp16bEdB9sL9jZTUL4iWArl54gVLxdnXb/+JNamMgiZKMXQqF2SyD1ITlimKxEqdRE1CgAD1LBO4v3ewkl3+N7pNUsuLzw+PgAE2LLfPTZNqnMlTRBCgCOO3v0ChlhVVn4JqObTXdNbsZ0xjs2X+bj/AKap8HUvQomqvnxnhLGZzRhqiNJ3vJTrTYWhKGgqo4xZBRYW1ipK+e3bS5pxbBK2My/rn8+j1lD4xRt/cf69vOGsVSfZcaAFyozk7MYoOv8AT+qXQ8SwBeFxVUhJuh1qJn4gXsFjaBeLy+dCbTn8WYw+tw1/yLFrrrpIzT6maOhM8SfPuBv1m4Gzp93DUfEddjikC9RENudPj4S9WENha29U/uGXwDr6daLOrZ7t87Ge3wEX+ZVhq8L/g28Yi555N3Q0E6DlMZTzd6ISwfcL95U2CcCCvRkMyluaobVzUZqpYY1NhO0rOI+jOuHwS0t24O7RvKxzPd1K6UIghrhuTkAeRLIfGLlQbxKi/2yDBG/y0tVKfStmr1m0cVU2XvZzOGt5SBEuFKJ8dx2OBOqlwSJA4n8Vgd7Jwxq6QFII6Tll+ooJ62TdJW00W6q3nUEuGS7uCKxCN3YClILW+4tpxDkpzllnbRqeji9oKeVPUIHAur5EP0gqKaRIBUcSW73pTSKvHVV2NiRr5Q/Mxfo8aLW42CWgTydVb+F5qZCh7Dosrd19lu3FsRQekNwzICkwHQb4IyE+WLru87xY9SkT1IJqSqCrsfSXal8q202sJlIxHc1gnZG5rTPMdgR+Rn2sEXGXrR2Wd4k0WPxFvf/ABIY39InvRuTKZ71d9ivYa6iSWIsu5NVp36Rth7BHPfomVs1mPhGG4V0GRaOaGZZNr/1vqQ42osqiNi1KdrK2LSHSxfXK7wu+wNUujU4K6nO79U2SpUxA5MSVFacl5jlkyhb90D9giEIv+OWQcIqkFK/MZ8hMiQyxLX/vWUcD44ms91sHAok4GolDYOt5czXbDOUnxk3GsVjuJvhbphr2e6wiRS+xtj4gL0imPMEnQy2xIvx85h9DvHRmXvbaRi9JbHDib/DD05WFNAK4beCyCQrqnhfhbaA023/ysyVAo7Hx8eaSjF17FlfiXdxzmYyif1sbgP+4mip8y6Tmc+fyyLKDMYDhzLIB4R1zDnH/8KBSRvyrXRbNqVhMXrFUBTYWqxobfKBgotat1mQ1QbU9gqazVO7WXoaORtKUrqcEjD3MXXiB0J4bGT3sAANXqmaxsXMObV08RQy2RvAsV4a3PevZ+8iqYss8gMwSNnJc9+6IJQ/s9EuBRpMmKXcbH6J955ExdxkIsrA2RajjgkAboINYLIcWI7mPrvvUiGiET+xC0PmptOfCfNLZvy+DhkgqPY0zZlFUblACzd6WNCCeKUYYdGdnLO3uAv2PTYDkHHSoFqZdJQPO4LCbZDQ8Rop0SBsMsmcn0E5W9SzyKzqNFaCS6QwN9MEUFtTR6ajJlTQlBzrcmB4bqbKkkhoIEP0J8DS7rox8jxldJ0Xe/EMLJhTa+eOOEwvefxTSJPV+8uiBDNTpv8FEf5T5rC70N7+FHBhN0ur+9UD667mdDuMSwVwz8CYKRVDaSMrUt1zVG8+nt7wA9ih3qN/LH2GuOnjXQ8eIV6bqoLUIQTl4vedRR3+K1Iisf2mkj7HakcEpgWXMA0DI9Q6H3HD5Lrvt4LaQAZs+x+VuoK/KOCGcwKt41Ev7CgmgQiRtrzn8HPG+8J/Yl+Axrbq5oZRKWKOzvx6uGnjC5mr9uhrgZmVLG9L796VX+UrS8mnpnqyXKkiSkhIUPdnjVxdJIkchCuzAxEqSHQtFgwRQhgUO9J8EyeprKMpCBmFqss/0cmbLl+4dGs+t/F+crG3YMjZnncSzdDIo75MNGmR/ogJtkfSKwjByZtC/1dTvFNbbVxYPAuo5S1BDrW06SWkd+PevhqlZrtFirmhhjf66i242OI7pWVT5cZFEqagk47XagDGwZcPNbYGRa2X8bpKapJovrjkK0Y3PzMJrMDuN0Wz9O7a6IqPLiZP7artcAa1kCmv3hxyahDKt21yoEuHu/q7mZ4X8pQrw6ch/eNWMQUVaozlKhx9BEVJrbU0jLGBmb4llLR8dZNwm+11k1JrWtVzlmLUrv53crmsW6bzBgECHcHk1dn25RzuxulvI/JFYN9JCjY52ZSXFqxuDcBr40NOmobEdYJpXuWFAZ+cj7O5BuUNNh/EVoX+dituHqYTrONozPAMiaPYXO3iCaUWFwQTB7muK3jqqVLPfBvImC6cUBmwYd6H3+AvR7ClJkhHjZHPyHlHXC0/XFQlfge9VNQBTmClT2YTD9gzAtQKArZk0zoDauWh168danN+4twsW7zDNxYEcxnu89wUTBVZpODPS+b3ZR9tKwIxkzIPQCCwzgFq/8xYPmue9XTgao+k6yq3/b9yi8Tv8UooY2RJeLfe68JerxiU7kbiHvHLoxz/SHjvBxWb2W5tDcb3aQTA6FjMO8wNQHE/ShZyUE9103j8obPSPXTchpTa13s7nGKTzOJbjfCUUXHO37gP1qyyIBkpZIYi4hR+rsY5RfM3k3adeLouE4b5ySY19K+HUnYSCOfLqZJYxECyT8bb0QH6ElCCu0cy5vBHYI24G29BDBVVhSq4bIoyzG/mPspVwPMmYp2zdRUBhT2Ru1iP3Qb/Wev5s08J6kPVfny8aZfO5I/6I6NQx8Ih67aGqxZm2Z0BVfH9pvWpZBEmQzbIXJAiDCBYMDeACPHXPAcEIdtr0fhKWSl7YIbMhN/ZJlmumCKRbOkMwWpUaJWDRLELQMa+ZKR/ewryIj4gcBsOmqch9ywafJPS5Gm1geaP4//X8FtqH0lpNVw7hmvOHVyN8sRTn8BWBU/DNOLZ/xX8iLuQkdbwKKPm+pRhLPoyHGXUb1/klDKtKM5NC1edvU4lalnTc8Tm2PLDVunBFmgtDnWNyzGvUpKDbAmLK2PPMwQJP3ZE/MF0+NVWzBCRlU/EkQwIZt+JqD07XXkcGsZpsu2PYdwxVkGZ2vMpfwF0ToYiuvrZrgb3HhcrNyy93/GrnFpB22XEy9AoCNF/pCTmj4wNTtZdR4/6ixBfb79aYrVSHSDC7y0xUPziiFlptfSAFYf7rXr+7URbsKhIRcVso4LXU/4lpzm+uYVyWaDk7X23fkw1jvz4ML3v7VZ8U6e6Eioz5OC57kiTdX/lidj1ZE6VS6Hp3/j4v8PnvLoLts78LpolcetDVYl17ZJO5X0oLddKa1F163o/GegpxNPS80Ips7dkVsQjm9bZUb8gsenttgpwso3XPK4sdpR5stPj7wsTd6IyjLUS8Ca+LPiQAVWIUH1VcovEKXdoMnwRtc4hmbZ+Da9t3YczBrehiclaeIgO2nEOxc8upreoWBqOc5MIRdUIDGs2+OH5LkyiJ1cZWv6cJnxFW13RvYTtHRIgFXxXl4hqAwKNKKITP3k7QmotgWJ3sDsCLNte/yUlAvj2ZozQj9QkwdRszESJJuhu9+GX9iVxUmn+KQxc0xG5Ulp8F8jHTX1vxpeUCTPL/JB4+yFv0aKnsXy9WqwdATlx24Gb4oZPkev5OT4vIyB0wBpVcsqINgFavkkFc5SdRPwq7wpm1hojESeaT+byoEqgfJpYNULVIsBda0/kq9pgfKZ490P5GYe7d+EFYUUSImnbN+IdfTNIfS+R/WaU54av2+t9+0b//kVDg/KflyJZ/hX6NJvEDT1uyzrk4P6hEzdAMLMh0B4zBvBSXSimxrhsRjPdnIlp0nzdnwnvJWP0dE/7biZd1rwNEYziyhypLgrL2SKd47N+oZmJQEEzGa1JUHt6xm0ByWZdpdugQ8VBKi6wWzLkhd8YckFgGtJcKh3GGbpmqm/YbUHCGu5Jfhr7vtzYRZR34kul5ARa8lg6xEZRazNtl2R9C19BJZe2xFxZgSwL6/zS+ElMydcRvHq73XvUeL5lYFhSiBa6LnB89EonnKqF8NzhzUGlEmp+a7bvGimdDfjfmtN7YhrddjK17Eb/QUMAWQb9XbijOY1+VssNVAuvWAFTxmQM7NrZMDArE6ZgvbPvl9MGh1KxHYO1jPJ22C2C/ftOxaj8ru3DvVNqN2cE7UiN2mmzGP06PmydTgDFT2LE9FMsaqUnxEB9RMNXGu5pk5ONHjD73PcjpQigzzuyg5/aK+sMXXlO/GHsXLnR8fAVMTgs/yh/BLkSgdx1XkRCepT6NwhJXivFU+j5lfcAsCeEJl1bgVnKLD0tR3nruJfVPGx3tO6Lk7B1HcYs56LyZyh6OBqWydFH7iX1j2k9zVOSW1x9Qa+eP/t8UAqm8adMla39bYrTrgXiMomyopJZZf5WPk1n8hBqJmG3B6BOvoXkmn9qQOtigTfnpp8QwtQcdxDUiTDQRqQj8oMocaLnZWf9Wq6cjZhRVHooPvex+EAPSrcIiE9mYA0PIJszCrHz8w/p2a7rG1Hh978amVGkw5ZhADKelz9h2bTO5v19ExJd0tfn3ew7ZefT4urCz4xr2yL4eDiPlsCQZCEAetlzPn4dBlzyG0ipyv+FMdzFkP6fgTPBuZ3dZy4gYyIWtKGNtnb5VJRhICbT5OxjSvOXBwKN3jsbeQj+eTtWEZ4wls5SgarWUeMo8J+9bDPq06dxdb64H7PKnKUStZNV0ITzGlPS0g9QadqwirIOkpKX2+sYo5NLFMGGl6iccDiFz5PBs3qMs+TLXDweCGTF98/m4BI2he6nEx2vPEzWKsKhpK5ZkcFp7VrnwyQa4rYDzKTwJmBEoNEGwBNt9X5mYK4gw/RsUiYk08U8f3h4t6Wgz/sUQAuNV/XB89z4v0WDNxjtl7d3EmgDx0p/pWAN21wFn7yaxLTQcsbHAP+L6zcMxS64yqiVQ3NBgJ6qkZ/MaMgKsT+gGD2kDmVDkpkZTO0d4eJgVYXQKrAwG8MsB0ENHWRBhrpwhx6LzCGpMHTFADeF9Ex/9u0Kpls/OhOjEOMhawTNY0L8KuMHLDbikmhuqmrhDNGZfwq0gFL1lhHhLK++H9R75LjxLzhbV4WYLAX2NvVMdQusdNazSs2vIV6vWY/CzqvrEZQb6b7uk2xGDYKL9/FYoVBRoYNj/B8IjOi8hjGr8jP4mylSOoRvlsy/CKBXEg77lpraY83q8mAUYosjqpn06HkI31mgP6sGeWhDu+0peHMbD//Bm4ZYiLDDd66bT55uUAP3o0no1lGoDDR8TSHw10qV0zgggP1q78eK3ms3ld8K8+CETzYoYstRZHtGEB0Vr5Fma6AoZtxDmAK3JayWugxBit91ZGk1Nxg6NEjtrY9JsRA436T327aQUmuYVhNzP7p6JgFgzNKGMOlw8hR24zAnPPLoiU0u4sSELdCiieSGq0Ov8Zk/7xzj6IDM1WvZ0hI2/qxvPdI3GVNZOSvcvrBwCUCLglwAuLpF85saGdeYrzv5XHffUTlkrkGDA2hS35cKDJbKeBM1uGwo1sGdlbnBGN2Y5gGhiEm/vdJRg9LPfvaALqI+j3cw1KHYg3t7Gno2gtMopxfMgegFjEDuQyiBIK9toZfX89KmUrvOFzPyR16D02CbuUngRbcDruXM6+Ib46dFe3NWACSmMF5y+A4z6iakXUfyYMZkOtb+1UGbuwIGErrd0I7S53m+BXi5hZJxCFVay8ZaNNqnXI6VlJHMyP+enr7Y8Etf6BFKUb/FKSvJOemOfSribZb6qaK97yTdTAGeksOKXuDdnKzl0qZoaukcH9Mk+NPZyfGtb9Xzh8tSZQbyulA3Lfu3SylKCYwI6uni9Lku+1xDUDdSFVb7RCw/LJRLAVJI82w9X7PzQymJKOPibkBrtKlCI+Ta6IEOhG2rjnQvq8R6teXPV8P4Qh93PKVc/P8/pjoYEcENaED+RNduv5sFV2tXXXyWJj5Z8ojkukQKTxevs6S+3bcudwLsAqY6ig+4en9aINuFv28Dwajs2q8wVKN2qHmKINZbmiIzONHzlHnhSFdYVoyeTah0bttVAUd5GbqDy+5MafzLXXzqSD+fYEXzZ5kdau6sFAOjp6FJ1nYMjTfHDSHf1+LKZxxZIMP6A9u6HEMxIcIxXLsv6cKZG/SqQHBj64IQ2dW4Orf+t6W3qMIwIskva7LQRBb6NYgTtL3WpMvXNIk1YEcNefmymajR3anQ7i+1D6a3UZBTJ6I8HJkF5dMB5H7BRx936APwEHG/ANEP73jRaiodwL1miM8iDiy81OVFaRN8wml+BmzQo68T+5toHtly5IIFZndLb3WGshZpPsMnRluzVGN1uqjD9WaOkuYfcdg86LTgcmqhRHglG07jwU7BTHvAM6LiYTNDnyok5Mkyy7SHXv9TKoA0ZnqX03W70/Vf0TYv8AaMTAiAEhVgNT6YVbrbBlltnJokxvkhssD+V0w86tuWqMQpfyqOehRiNH5Mal45YvOxXe16Qof3Aiym6v4HNBa0v7loztoesNCSZlMbIWLWwBFgaJ8qG0Tr0nhObapm50QvA4F1S7kCoIeipuQyUgJTOpO/aAl0Ts4pCGkpp56P+ixEe8dWw+eHayQMKViWXqfqxzbBJfpDX3Sv5cQhto+JkFzy2euBDgUVpObnGgl8dxMA5vpIHRLTpLNGg7UQuS0Gg28MayRT9TVURuHdARsPTx6Y9tzfLOhFhI34myRTc1e8nGCojRJv3NtxSZeQ0or2rKk/IpPj49WaizGL/mMb+ktVc6aBIa3/7JEHa/p+bxsCC+XVPK9o3jaf3kUNDVkuvMUI9ogCMvn/BBwXbAC40ZNZ9CvORFDUFu5gg1J74fbuz4iNTaWYP+jrsGpYRiXfeoiosYkCT0P8n++I1/K/bQKRYoc4ItTnzr5JqGIoX8cP7yR59Qto5CcMmi0f7w6E0f+sHSjC4hisxVqPhv/SAlYvHIXHcYafJxYbQI7cFXY15mm6YhyM1Ol0cHJLYQB8nQYNAvq8p4bFlc/+Yb8Ez1oZClVQJbC98RaJr6bN+l4q2s6vE0CntePgCe3Ee880CSTgOo1g4Qt9i0nzAwDuoS/D8Eohu8fYp9Wfl7Ur8w7iLd1DL1BxEmLqd2CqXZmUfsPQlnPwOkRdvmmdH/MMCQiakAbpQ7pP+4Kc+lwzbtgidoxsE4L0AImYrVBRhcRHhjSVAI5w6/109YKBHToI7wY2z3ZIpELavbZkdhiCB9iMCtklnRpKce5kYKMTw0jatTFWmEEuC0e7Qbc9IfoTiro0VSNYGzS0TtIGc7iKN/WRW/nnit2W4WzgoRaueAAU0SjwH8Qn/zjLnIETVApyJlzlZaHw9k6uZXLsQNlghd49Tuy2dBXjQdghjxaT9XHcdskB3aA+KKlRleqIKyiHDCRrH0X2XKSxYVmkj8qS5P33+tOJ4aILX9eeKQS0q4eM3EnpNDqhxW5fZCZ5azJVHTLuxKSGVPcvZXWOboNwork7OP+f6wgq1FuGoDFXgPtsuDwXFfqH8/GUguLsPdYLf89qmjTczZAls8HMbQjkBpnLeRCZwly3kCZRdhKYVirNP8vO4by1pPlANOIdETywgpipb5w69MYFYa6dnejGsZnfrLGUUbdAUtZtl6A1XN8AjXssS4a5EH7DrEOjN/7Da0pDvKFjBtsgqHEvn0Qzxl6Jft/y8rGGJTKj91CFxZ0bVdSUkoik3cubjc5Zp2o0buA0eclwrMOto8EsUlS58FVJlIX8F4t94ZcwAyhaETNBNhmIhJHmYgP6kx5x9Qg91Fr7iTnt84DkczS2I8GaDdAQc+fzcdugSqS6+GJOMzll4KUMz7XhD+O+MHKCFBm7dA4aDRa1TROrWNt9jIUYRK0+F90zUUp/vQTMtzYTru9qCvtZXC2rsy3YlEAEskvbBzR6kfq6ZYY4bVe2+G7WXLEIk8nJx0Sh9Ucm6PCJMSBF1MIPHr3J0aC+kwEYWYTw4G5YfX4nzYjXzTaVOZBxgwInIWSLPYu75lRalHVejfdb5okTST8JtDVZrsrjWwug+74T7WfDG7ASJN3kaLSum3CDiH+zyErs/+zk7seMiiFB6c7mwki3hXU6rWwS12H74mYwReD5MltAL562Kibf+AdVx62NK4L6wbKuecz71brNmzwaIJugNdIKcM1tf3GTCwqmF0EkWHEprrb2t2eejcB2Cv/dEznl94Jnw/6cLhXYhV3cWtYZ2m3ocOH5QjXDiAZgrsQcKtcTWZcLkIcEUvyy4wVomkGqAaA3CehoiTHR2K2v/UUTqgkPm7AXTA52JI73uQCTBGZGJLToRhHN12WHXth57vzRqPE0Lw+RXV5KvDNQWKQXd5NBsWjxGP8H9TbJaILWoRMHYahsojXDeXSkKA7hhKm4z5R87ramGmQNallJfAVjWdcRd6z+lPoGYvbuMWiLHeeA3b6pl8WMCqvxZAR1Y0vitW9EykBdCnFy8XvjE01LOwNnYy2ah+uUo9RnmM6X6c07ovXAjoLX+2pSH9mBhM/gTXQHO4bUKEvHOHqHB4KBUd2oIbuqiuaFGAUCxLTWrmEVHYvBdMH1OYYZZzoDZG1LgbHc5MO2LVUUCYBBAUHOLC9k0IwgKafyhD2v6jAnLN/caOfl1DcAaqtOMxfaUphr8idvZ3SrxIDmDu9Pp4fsbR0rbFMc20DyIK5Yh0IHmMYPq+hJE7u5zghCe8T72cqOTvPsy1/H7NVnLyYh2tVL000gwJyt7sY3Gd+ltP2kWC6hyUed41i5X+FCOVtYbxpDkw1gMDdDkDmMbNBJaCCmWmCeF4KYzSWD7mgR7NcU1v5AMvV5fMDb+0nHeVJfl1LSzQRkqC6C4ncqA9l/kMPsu0ucNbocKbLRLhFhjLoDfuc14Tflzjp9CF6h6pDTv2VHYU4hNo90rO8WGPtkKhH63JeuogitrKhKqWcbCAs7Ph32qrET4HkvX5MYIBghm0bTMMP+2hF4pKUiH3it8VVdeIPx6SLcJClGvcX6k8d8Iyt6oumHy5JTMSRYRYuVfvjzCKijLRJ2qyfuih0kp/jWVuh57BGfViLGeKO0GeUqNlr56yi2zdb4TI1nZT4gFwsTHxNzrUtN/zpHSFSOVSOe53XjM8tHK0SYAqLtsLHtKvj5hSSPZdzxtuIkZlQ5drBWnmEUNI1QQrKEOJ5MU10BkFhTcnP5MkI8uQrBNyqDfprmURKFzyyINUcXQlNnNQ7/IOFB0YYpMFT/d1YqKvzCIZFr3DWCu+K/MbrPcOsobjG8JviSVbHj6ks98cW7PlWQhSwbpYaSuZRu3byNTMpVV7sMoVvH2er5Gehddaef7mt2b1NdT0Eju3/AQVKx19wgHnZXJ+3KTLq7AecbKvWb9RaS4xy2epD0Si3jVhdyy9maqp2eyh+waOvtjQsR3RcnJTYCaNH+0WVOKLs6WA3uteRynUFELfOLViRR85gfuGq5TI9MhfF7xXYGFkXkfySfaZzXoNgovscvMh+Yu9FQeJ4GOcMxA1bGibdTt5ksie/7uOMu+yTIS38Zm4/hCMg0xmy3cxq6URmiM4nJhCwX3ivR0nGhpG/V7qtRRZEv/kkd6e994uoAIugBHm4cpokSIMUstC7RP+FioL+hBUmBy848x6WuS1T9ZL0MBCArbRiBgfTAzH2TyqwH0sTwPjEzg5qjQyprB0bta9G/5d2PZJfD8uRNhDN5Z2P/P3lgGto2W8SKkPggS5KWynd9cTv2zg/qTmBolIv9evm8DU8ZjRo/Ofr86xRwjFWiHq0a1JMM+JvC9YIKvLu8ya5lUURbtT/4rBEE7ycHTb+396Ae1Li1z3wiRu1iSnyRhYV5FiIp92WFZ1p5w9R91wLnTVgBuP983uedKv8ldueblpaL33gL6sGEw6/VO+DKsO39x1pFe58NWW2fv/IavZu2IdTZJqDiDjTTMLqWg5Z0KkcczZNnuzvyt8LgDOjrKXZzW9qGtehi79pIUL9ttr8M2F4/qZUhXVNlceXTcLvlmRrIEnunIvqZZKgj7Im1RENv6fAndR1o+ot5LtCPYjNUJyOM0sMiil0A4o4uLT75SsTetY5sAipahj70tpp5NudDphpI57jexzui0tAJnGVBpElx3zFqcH2QBCSgwj+pvE4/yRw5MFUKW9DOdVPdFxynma6cGlWatOA8meLjrT0qb8f7ooeSwOlgxG/pz1o4V774JgY3BBQw8WKyAJAGlsKucDSWj+WnnRI5e0XOzSUINMGjBq6sPm3WkAqQYJrLc5YLnUAlFTV78jovZZlEAMOVoKP6ggUGn9r0URFPJSVR5EXqeBWBNdJxWpbSpHAzlpJsmjtMTbEOEPX86Fg0nwua86UtzlOUIXS9BNzLz9MzjupkpX4ubp4bqNJ1S6/jtvU7qTF4AHJyahgCBqpaxoeSosBLWIpW+F7AwgynsTN2f5jA/ZxBRba6qqf2RQu6obM2FsBy1Z4C1/nnhN01Hr/bqU8aZ13L5yzz3FgdaHTDxMBf41as1hex86HCXgUc4vi0Wo2lpGJlX8ggOUpKecgMh0n81V23r1wzb3gYiUlcJjL6XJHG6EoruhAB4AGKhp+2OOgeq47yxKVI+1/kpi2UF/5fdUffVMfqMbcYx/lIJKCEv+sLj73tCJdUXS5liW1FevqArpIndBJ5otEIUQDgMpUxM8ZYQezxmn/x51Jj1M/zNg1/Ia6TT/RQzTgU155Ha+MhfdUWTUyeJZuTODdKve1XevtOdY4xFwlmYsgnovYlQuJ8X+5WyrlHQNhdsShTWMsUywo1h2SsdezwqokR94Fk5trOiLXGeTTl4NhMTi5Q1SLx5T3MWjAbDi0oa2RL8mxJCGOWIqgx+dWW4nf/Mr4XTOfeErxK4tR1tMmyrfYTQCZ5uSID2mVwmOFBWY7EkONN7NaIMMXaHJY5hQ8/HuNIh2IVVLxkuMV3jfFdpCuoQWDhCkjwg1HchUHNDuQLsAIB09V4aX2gSx0t3kEPjxe0zWL1UEPKhkrSnrVBxTm8TT4GAWwsLWj5Rt/CEGHD1Xj02DjyK9zXPVtHuFeCozSyTvVAsypNG/wrkjEA3T7Sgrof4W5okPH+w7GUCEab32WszTOL/VnVGMZ7ZMcgJHRwMoHz3i3GJgtsyaWgoA2NlBILJtNq33uSRYJK06xxyeHsNWE+l4Eo2r+BkpvNhhJOJacUWWMZIUycly8SiqJ9ZD4c3/g+lo/z4ILTl+DmHdYwgDYm9z0FqFJot7boWamW78Z82ijksRjrBa28E2sT3IpfYK4ls52ZHzbr3i7dzrbgQZSRwzLHiLetU5eWBOcEq1O/7XB+gjTULTchHjmqUG4KGO2iMwTHbpTR/8dL04erfvSR4MQkrxK0vS24Ye15WdgFjQMJXyRKZFIzq7Q8bwC6554aGXct8bwg0FCtjhdWu42LVVGTrNq4oK2jVl/Xv7C7K+mBv/wgBLBO19atEYE6WVLANsvsKpmc8hrBbdWNJjvyG9SIU9OMsmg8i1wqY6uNySxLh2NpN6PgVvuP8bq46IC829tVyuV/DHJVXU8UxmZ9jvKyoPY/OMfZHYrb2B9Bxdaa4eHk/qLAw2uvkUXuOo361Mx6M2njZok1KW6OXRpl2982tmNW8LeqkVcGtBGeQ3unJUOyobSVH5IeaMxd47FxSHc1nfbDum4UnwpysB5lGRxsHm3Psnw5RxNZ+wKv4lX3GJ3yru8Xv90JXJ7C2wIxGnay0PkZHlqqdBDK3Nf+/l8GF2VfGqQPUdYRCZRnCzBdpok1LW1EJN6/ordt2Ymq4Jk5NUSOpDc3SrFHiayauhEZn+Ld1//f7NEjP1T0X3YdCrzS+hnIRA3PSgMqhBgoEdDm76ueVuIw1vYGsrZtaJoTL7jy6EcOyGWnwXIMl/UX/icMfrgR2BotJM0AsBM/fSRYbqnqMI+5Mf9D5o83IL85L+r1FlIYByOI6UoxyJm5F/VHnpkdPLWrmSqEdkkrFJ5EgNk4TJOcJZk0D7WGPHLDK0T6wXYTuoU5/5VWWDLDj37aEg7aXQgraJKSveN6+OFcloa0X+D6CLIuZNRBk/mfjoB0b5/iYk6lCA7JWXq8jWTF2nDLkrQ8yAA/gt2cpNHK3VdchxLjEuJ+fO3sV+ZNpprhtV/Q7fCn9EXpQCLRxVnEjwxg2JODXG8lvrh3rgBrf57yUV/dpzxGC02ZlS+7aC2WKnKLyUvCh6znJ4+lRU86ztgQs6TW+u1P+EOMw2vdj7Z3AuwY+Fene97TilEPyvPxk3qk/TRWVnrad4tRoP6G3Kptf2dMp6lqG2iSEXodxIoLpmSKT1H9UCHwrxkRkFEcWJR9tAA681EM4HQNBhiNlb5PMPZTkfKUy+6Rd+jnZxr07JMjttWWuF+xQMyOScVuOj2bDGg5ovVV6EHD2Si2m7kt08fAFxaEXdHYEX6faK/8mu86pF0gN/lgyjCgkdTpBJ0Cl1CLlLAGGM8KuFMsQkn79A9gPJhAof74qeVVkAFCGETRdlZUZAGvTvnVIks9Q0Wk+hY6M1ARqCwBWB8+mJI9zxvasQbPWFGO3P+kHaWPU7j0Lk9Tk7Q1/2JmyJT5IhmBo5Th/wGwzFpoQNGe3NA33TJPGtuvm3fcpxy/lMtKaMcErXG7+hJPh/6J0kYBtRIqjGvLnm7ZNeAamXBcCTuKVWKTtvAvaWmH8dDRgCyCLKz6p1dtE4aSAcBxl9EaelMXLQX1VZzwTLI2ZpPrwQhVYQ0GRpCSOZ9esnPtiW5+tm3ifHXlYzKdDPVSRzwBnpijx42J0anqIVvhrN1qVEuia9QWS6ORx5LQgeOiLG54UGMk+uw8/BAFbJzEWPShntXQfzX8vp40xAZAvJueS08nKQWK4IqlNFvM5ixNqc90QKBUcg77PsPFcd5dfp9e4k5QujEdxUN4T+YFLldCbMe95SAAyChsHJAPVQC884Rm5XQHEIyQUP6z17qTExvubY173jb9WYcYZhky3/iigMPKRNGvbup37H3AELY2OvQ6ZQpodmErYfvNb3DYvTO+9uVsWDp6VdaTQne+NsUFRyTYMsXUHtVpPf173n+RHgqgRPJd9Def6Q+f0rYIWuXnWYoYT7iEqi+5efyW/iaNjcBMJYEdYOCWJgMxE0Z0JwIEvhcVRYeK+gzQHcB0GqeOWYFN73xEi9J9cbUvRU3edMHQLs41Im7jk+51yQNPWhkJunTX6r/5rgJGOOqofSq/nwX4bkENTB1UmhGWoOxvvBwayAoKL7goysqG+TZt3euZAv8sAj1USVfV5h734kwPCP3V3cAZp8ZtHq++qbn+WCqoQ2kA+jhSHGII3pZcpCzcrWpVoE4Eam0PM5K93OEbwatCaIpHQzgzoWvJe6Yr2PPIA3SV+R9ydj3oggztakS5/5+5DAlWKm8huksGmv2C+OkWumwVr/zirjiUjyebtVF5IZp1hwCpEqSXc3AKysL6PcIUJNxsgtkXlmx7HSd/BOTOIGux2uNWX3KWjr/VKvAnySoC911fShJq9CMa05ldtYl5dxgVl95fi1AxOEKm/PuuJRMWO6jDlWSVZkKna52jT/V3qPgvCfUZARq4q5sYR0B8WEorG+anKDLDAdH/6/162qsGxTXoDbGcN8dGw9EQBu43J1iQJA7TgLRFbw/qieZ5a2Y8d/MaofGnY2PJt2T45KmUIzQEaWd8icVf5nqAE3cbUEGyXf/0W0eSQFJlR7nVc6HyAbsDvY5yXLaA7+n6Ba7SBNZ8zfo1B8fTovygS+ik+DSnynSIW/myzWKLT81z/UXkODfYd5fhlMfBhJiCFwOMRkG+ecpHDHAUpdq3/nRzPQZb/Tbtu6nHBfI/HNSKXOmJmFDHfjZ4+7+1U1yLAmrE5S6BerZyeaYGfyfYTyJGarG3JiE8E9nqQX8aAZmVINYDI/SGqQiTND2DK1KoPQS9s7hmKmmYwItzJ52y+DnNll77wFolz/1VKOIDWJ0HyLvD0I/qFV0PvdSRBWSdP8d/8dCQeQIClO4VB8BKDkDT8B50HPXowmpogGQ6+vFNbJRKwk/52nCgBUbkM+ZtixyzsGVH++CIFyQd5Du10WsQ67vZirkTtTbIjhdQqjmq4Va7NTvt+e3kMG3AIvgQOHFjzVwc5l8yPbsEgynemYwvRePbFMeLw5vlLy71vmQMQ7oHbiDBhEGI/W5rOkC6+f7WouMp/Ao7WNB+OrXH3gY+/4UlOewPA5peO5nXV0+feLyoR44VanewNkc+ZQtPUwABSlY4v0L7SGfcr3fqnN+ng6IZd2eO1OcdIwW+EfW86nZ7B3LfsvivjmTlpwwcjHoLWkjbF4Ops/HgigSOCi8Dlx5EfqHXKphsUay9t5lRvaipdsICkowbkUoUXpGBSu/s6Uep3w49wl9egTPPd5ZyxkkNUUf76q9I2RD2Pzk465Sg7JGZoxTx8CzYAtYjcLu2fBo1TU7wmxxmrtUn/mebPfMwGvJ+PpvmgDfvu63IiJWG3r21D1pBrojZrhsX2Vyo19HI62fM09Z12UsQF9y0HqcU/Mo5ykcZGe2RRaniDnRfwpdAIbHQBb1FG/XLJihmpGQ1E5nPO3gJaPiutPbxMaYCYuZk84bs9nhjTc9vAeBDY37pRBZXYOhY46hYqIGCR+M6m54920HtfkqR40qPknJCflXu8CVE3bS/JrPxZM2stQOi3Z3NLAqh+m3IHKR2jo/qV+SSeuBvDQG1L5TnDY/8vwu5kjG2nDeKoANhiBaM9z4vzZmXI2W+UX0kuW8t5jEwPm2zEULU5qbk5DZTMdh9yM+CrTi4KCVjCv2EmTnJRCmYaw25axffsG1lt3vGkzqd9ZxjmP6DaivormDwXV80NuZ6B98pTTOMCo/m17aFR8B9oAY/QhA08jR8TfbonYfYlgt2+1Fs/+zRlWxnjP1HmwWGkw6VKuvCWi7C/nOxqPcnL/4bokYcGgoaxVgcL9inI4QXaSJFRSq9HLVY8g6WparMUj1DfSKnJnHHCRf6GGuv7eAlktUKnO26hgcq0js61jtLc0hhW6Fthvx/vf/sVGoCR6Xcyjo7Vhnc1pPsBM5+dWQbBbCslWVbF6o+YCVsASAsa4ezdeto2PkMO4nz3Yf/jSJ3yTM3wceKanl3kn8ZwjcnBx5UPbvMg6DevgH031YVEr9ffPZ31eZ8a7+Q3JNJdYGjx2TYjHmIZLFMDsvp6qXIBJK6ybTfir/yE2kBhnqNkZVK86DbntO+p+Pz0GyGuAYyHVUQzjsoD/OaGs8VvM2z3B3+elY40zlUlqsIEMnLzcoBju6b+D3uWm+C6EpwzRyEWpI5Qthjg6Tbe6JYXqVlbDyu2NTxBnmcCIsNtcDryAEmU9chDbJs/o3dTWpxXdFGhGq9HXJFMxlZVaAoozTd8vXjpQDKKrd3LSOeYIJ+oXu50y3soY3bcqFBxdSRE/Zj1b7utH/3hyWGEa5dBK10U+GjsoEq03v2FmCTAFcE8AbrZ/S3LYhezTjLPTJnmS5YQwMh4HwthGiInYEQqeb68OwIEe0TXDYDb3lztmNw7K2loBe6/OQSc946GA4xm1e48E9PfIn9nXVg33SiqKARlExkjDxfwR1Mi3Jxz+lqd11WbAZigbGNsKiYkp3oIw+VKLrAHPCUuPL/p+uFpDF9XSPh9qv9W7uSDrgOieEPsYoOQBYha1OBqWooGS05i24GS60LH0rXPxZSA/3SJOo11QEog8wKH6aUCHVm9x0hUHlecUL8Zef1ohDZOCNQk0RAurawX6PGIxy8+cFVC2g1g0a10W6lD2bnQdpG93vQcz0E2ofVf4eyeoLqWUdiVueL3FHKS3YBdpQJtQOg3nRD0zpgjUOYym8yJ5l3eGhaPpnpFhQLpRzw1XGYzourQbTQRPrPdqtsKiYCGOuMa4t9Mq5UMN1vnTPPYn22ZWp7phcy4NB4tm1Hlhx4i1XGMIy+NxOhijXUG/Revgx+T82JiZ6kjoWKNnUbeRnnXAilq95OiZbnBEJ372/qZgYV2COAeKuJHqiDLllz7KgtgrY7ZjwEfzZ4s0GY4SGn9L8NLzBtugEinu2ezOujcPpMMEa76JgWZScJYmKck0MlOY3dfmQqbyf4gaFZb9ku0H6MNBq3kjfrbL05bOhgblJYi8VHdBiG1Q7MiYzVinttx5cXDQyc7fOZjD29eXMJcQSgd0Lb86J5XJglpisIaH+gSZoWrMLsPk3jXhiYZNsFJXy8jfhbkDR/ivJ5Wm36TkXI1rrZk/ceDGYmis3iuphWI9Jne3pE/zMm/3skj/ha+mTpDkwOhGBa6+MOT8hZun5fps7rhVa+7Q27PRJMIZmWBCrwXSnUqFMntxM0F5XmvPvOYoI5UBbqkCWns8Jx3W09zrOLBw/VtKwos37TX9aLz+TGDiw2TqR8600GzV/ZTlVyqDIVMkwh0eY4OR0vquU0ZqufSH0+IqnVPGShMpGRTcmAO1vIdzB2cXBJQDqJCRNc4/cYESNGkeqjIaxJ8c0iqvPG1SaDcp4hz/ahQqonLgXlehl/ZNF+QQkfUptmSYr7UBwGS1xoOQPKsyYKocW6eYoXTOkGWLiyoTx/hmj4jM7e6AAnXENKSV2JFEMIuqEgWwfuRVzDWtzd+mJUf7aWrsLqv4KTG5ad03TqcyI2gIiHxZbA/B1c5RTmwLBcLH8YUW1IT/Vbp/VmkLqGwfbXJK8JWgjEseDkMKOq3uATMLllttIzpntmzSsjMzw8eVAnM5JniTUCrveU5Sjh29VnNPWqvYjYRL5SD1zNntuFCtRLm3ewKsWKj7lTUd9q4K04xGOxa3QxKdAVcwOEbpokTDQ/Q9Or2/gEfyZjZFscK7iGaiz1GkASouEfnyuAMxYfvcwbh/Bi4G2NCcB+wlV3LaVznRhYfVL6CJzUJDHMk18zBhgUOqxZBqQUpnFzrcc7QcLfcB5+YLyBIKcPgriyNNalDuFjz/oGPv8T4xAgKZkOauvEiRYwESpQrdHK9dkK51567j1gTS43VaG2n1fma2AoSptDt6xJI6J3ihwf3OEIVamSPIfIoU9+ftN5L10P5WUTJRRN0/lTxfilNMjSx+4fQZAQ50RCh5x6NX5DgqFvvr6PXqlO2lclDJ4yZFNVauyzcB2y2UHYw1aUBbkNnkd3VtQkTXqg+g5sw41x4YN3pr8kKSYcVbYwA6gvPbs0PZaBno02VBbkRA/rTRnxHlzsXaHn7xjbNGnnLQdo1v41Hjwjv09brwuKFlCR30LamG/SyD/pnpUEoPHvLAYWZ6CGIPvBWhtwD3dceZGQYP2jOYLs2yBOR/WCrNjVVbJWQKgHvMucsJAyLiV/CnhmqhaJb5z+sffVeYrNBRDpGP84pdOaaKFMkJoSph11E+NVFFIM0kcMJhoKorHkyPg3xZ4cfEmQqLtUIBWwXwjpD59o2poMU1k+cpIdfNJWb95KMSKIgQeyl0kDaDXj/1bhXhj2lKeV+MehcYdUBA5+N/JgfyHKrPLRyCqfnWRgLKMLywuLojGqJKHf4S4m3yyUuAQeHlgRCmWL+IzGdp4K3RAD9KVC2zw7Y7YupHX0+jQsX4aaEKFDB4hkYcl/bIYdt3yPLahnERzThF1qonqEdRK0F+KJ06cj2AyoJbVz8YmVycG62v72garPF1oIu2cId7o/YRnq8s2anYEg4LxzvrEe67/srQiJCz1KpKY8hpkajYLkNAi7V2RgkpkTx7VsaIlDeo597iJF15RwIMBbNjo0H/kIH+my3QLq9wXUmOSnG7X0nIU1rcdOCfKSd2aDs5dwO6YPkIAGJle9pfz+hzq2z6koIYtmEYmbcoHTf3gC5kb99AKcqnt2z1H0WcZXu4jZuo1sufDv3e7SxCsXLuVnESoADdNHSUEsiyLgEaq6clnC/gw9BSUrLfaevfmK9RZPgI1tpySr/ZOpL8UvBO7jKdMZeR5OkJ6uLWF5vg32TDU4ax7gGramlS2jIJcPPZcwzy5936TXKG29NgJBMt77nxhEMlnWsg5HyqmO3pU22zGMyhssJX3AiJOn9SpM7k9R8EBC0zOe8XRjt7fHMW9I0d3EpdQvfadJ1zZNz+FUE9HLTnMUDDm3w5HeYfvAGolxhJeC728Lu1QEkUlz8yKiaWjZIqadaTY2UF7hIA1sHJBtxy0uRUo1B0DZjQ/b/NxlUB1EuSoOE67djeosIPyc0h2bCPgCwUVAF/sRywk0fVJGqQ6lfYeaWCTMLYpjf0nK8/K0o7XkQs3196VUnY4JlujACgRZJ4XsJaS6h4/kT7J0YUcgE9bYOP8prFgcJM/PeDwq46jZNEl+Z2WyyCLwj2DdCAcJoHdVswN2F9R0DtD7p2NS1deAWR4Db78yaSgmVSskCZwkYLE1rkwKS969gT4HK+Z2FDuM6kNIELAK4C8zfZ3dZyF6NnZXSYiGjqLBHqOnpe9rurBO83UkXSnKTswrMzFJsAcSN6cJ0iWCzgdELCKgyF9+2kjWkhWCuY2k2UVlcFqkgXOviT/BQ6j7ydJihKkVxhhN8xqC/Aq4tzgJN29Zew5rL/VRC2x8D2f20zN+1v0G1KFpP9yt8hQdxdeIPkYiTF4ma0bZYYMJ6Gq9BO20AR4VLq0it54L6+EKlSgnel9zu8MfXoD0wnftXlY0H3psfA2dbowat2U/NxqNxL8MKptzLz4p+cLN10r4MOG/cMJtkgpQYA8lQL44IwT/HvJ1rXrxfCGERkYkp29PubVCLd6SCp4a4rUvUfhnCYiZvFHwdRTDYmRrofYdDRDVta3bXf8MwgJ73jQBkELbi4uB3q8IFMJiT2/XJh3d23ANHIW2MiGrf7laF4aalbsRRne+baJyN17p+1JjXrEB3KtkRagd810ww/1kNc2oX+N59PVC2EL3MGZhSROZwf6gEG2nLbY/dvNsrY/PhVfehkIS3QTSSJz8bHJI3xUlTJL96d+0AbBJ3TxmLifLIRTufU6I++urR56hJPxMjXFUEF6KAryxvH/VCdE456InephxSbfUCcPxEx+45UZtFtM78yISGLg3LAVJ5LwR/l1feOJ82Xl7Isnn6cBmxazhs1R+3SnpQYNVGLXcBo8zc6u8okbWiTuEBI10thH6DFfOWIPQsYncf1Y15GCyFHRL7Hri4WhGodYO9FOyTvJcbvQAY73vszM7hXkEdOvCdDTOqT1ztZaOFnKHhEnV1+8M470/I1vWnWpPNZH4a5UshYQ+G0TSmNPEf639aUlw+2vGuHZHJhYFUaqnizAvsYUN8yLPc+Am0medKSOoXmrkS+1crUDRcvLG0EnHfUQNaVuXlF3peQDiQIa3ZWKyRgsWFtlmyO1BazsDEfnMTxbCDNoqJGKjc4NHMt1FNoPfjfcJfQCeeRf/mujS+PWfbXoza9U7Su4zMjOxIvKl6kArnNHdfUC3EvI3WvfDVT9+SRH7rLklli9cWvkvNz2qzO99ev9fy9LyIv4kFtF4p2YrtEWG5vq00Ozmre5/b28qXcBV+mkl7Sbxy670oj/xAkWaPFFeIqwV7OVZ8juOSYZ/qwpDE14YOEi03ZXAB5RdPj1Yj5NwAyaQ5KDu3owBWNVYWuyCsjnt+He69HNvD8ywj8YWQi57KEg8GzXsjT5jl2fiHO/BYLzzbyS1rRw0roVND5IlGafOCkId5+EE2/uCDU3UIcuAa/s5hMEYqpr047pdt54j76W5I/KVNWowxiUQ9WUQZpgY2lX4RCtNmW1chqgeBb7J4BJuoo4n+QxTuRet5av1QTpmiv0HQueB00xU8KlapFC43H8uOQx+m1VF5cWGjrYFVxGgchn0V7LS5ZL/f9gPR3u5pn0StTSoOlj71QKUx0q9sT6/VFuAMWm9zv5YeDe4roqyAJ7CvV3PYqcudHYr2/iya4DvpgCOvRdsD0NxqOL875Sjc8pUyP08BSd+LAQIgiOPjeGBLRUfVhVtkQGDChn5rSKk6BEZwwRkFNuuF4n19u6pk0wb5/DIxQsw6YrGdhdBr/OigpIsPK03NUyEIPQ/71zKBkXrz94kda5hX3eegnfp/EZoYmENtu5HIg+0wj2kWfGmCdmOxOtxcjmmYBgEQ8R7q9yVosNo25u5zLnpyds9xlybrWJsS+iBwf8HuN7SFYcQQd+FlquLBtvFSL4cT4ux/LvN5Oqqf00vVUChJbIpDYfWC96MKCgKcdJVXvM0mizwIPbTLHnEFfUz1BVLHYmRhUl5tfUy6k4BIOCmP/tpIHoBKBLBxr+B0+oHO1Q4VGsJKitfKUJQKvWomXtTpMWlaUFF6ETAIgoFdNRQBudcwY8LgeE1xQnSR4kSUHD56rWuRobAp3CERnrIDQE1m5/pvj3JvCwUX+8bJY69B9KBzS9V7OTtpiLKqAZQBNQ0HDXzKI0FtwcsiD0eROqCaWm8egN2Izi+TfhrDYvIOMReFX9jtEKKDyNAwDbwBldmMcMc31kq+PtNgxZdCiBNab4kLOCCIXpHb4fjle06IeuAFRxkKWi5Niu3H+NbCuqRQVoIkUAaHOB9ZXBrwXzw8N+Xu6g3UWlxAtDY2VCgwJhEwDejf+TcB/pxH7T8EPYJBP9znp0ruhNfYRPgwBXGkkrCAgFfLhTVLn2AsL0cXORljw1s7FJHWny7naz5X+6pLxmiv71YRdXyiIO//PktqI1ObQbcs3VRV2dnyPxOrsQ4sFAwfUb+yP/KuzupHcvpf505qKeVcj5+djS9vkM1JOu2+hm22HwK6OXFzRs9Y21fTBfwf6o8sPwKALN97/8vt31CA2gkQW66VTpwJBM8yB20EheA0YdRMUwgDBC64v5yDl425JVxGGcxAjgd2OtBJfjPaGCswsIMwMfaFOfKt9FMpePF+XqGid0buNOoZdT8noaU3KO3xxXRfSoyaSv8kRLwQjzjNfQLgjzrwPnHHQ4Qr3HFRbozNlHAiNjWJoXpacuKXVRqCsJg2zJZeX3eZ7NsZWwJsxlv84O4O6J09pib1J0+oxsr5jUNnFYRNpNYWoUfu2Pk65cIi8u2MretTufCKcHaVCHJuFzp9X9Pv1O+zFQPy+jD24Djv3ZC6OKczQ+nfcBfQGKA+AP1EUGT0WyfEueYIEG7Z22nJID1RpLSkV7r6Uqfu8XKgPV/eE6mBXqm05PvWzb7gagzcznKofIqqlkA7QaK+s3vwTla4P5KE23oqgfRJSkbVu0wGKreGbMwPeIZY/EXyPh05hYOe+YCv93AT3c1WaP0DY4LyLjEaFVNIBcOl6lRyj6Z35QqakoOPMRlUtbWQ0lzwGv3exBbRi9cQkA9UTgudmxXhhAiSQ/4USjH9nru0i1V+TH9mGxaUa2rKKZWui8WSKvogFVwzmzBhgKke2JOMRrCgyfoBpT6s8OMBw5AxcOwLFnOkExybk2gL70jRIJA3+mSi4oU5j7J86aUZaA7vQjohfgSnWcuOwlxFJ53X8n0BQjVWc0HGjGbXjhpeR9wMDV/LMZQYCatxB1ioVoSgsdbibvRrn+SYsYtW5w+7v2A3ZP+oHSPZ9A3UF1IA6CTB4eJX1cMy+4c7L4hvlS6Mua7yMb+37tg3EwTsEx0D0qMLQePxCcJvKAdoGil63bHFBLEmthnukn+bJDlmtzctwuzkctObtsK01fIHvbbfxULwaZv2R27/Ye+M1cw8qJpYLPbJZaaLmlt56dwYyLsmy4ATo3RUwh6ntq+3wRjvW2LfxnZ+FCfqpKr1xrwfWWCifexEhcqtZi6itLq952GV4aFgJpHpq9ikWKlW6ChcwNlQ3rY20D0HokHHHqzqSZYFVbW9p/xtFDoJ7hY6lorTymFcYSRn8wNHIclKlo0dwD26f6YLh1k2roQeWM7asLAjeFMUn4Mikmj39aM//P2X3LcKaGxj2bh9uhg1oFagZfl+GOABkSIDPAW39WWEAi5hs+36ctQP6SHZ9N8Ir62EeHz4ehtuAVNqeiv97+PVYvc4OchXakMxXTZ5yOP7oWU6eKPXAcPVioFKmPubZgny3naccEW6BLBqfW6kpLxmx1aOQIbB+201qtwv/M44kL0VHYG5g+Ca77hXaOX9BOmvrD3iAoektsdJ+/qbftnUX/xWKcV0qQbc5MyDeuk/uGm929NE9/mcz17IdFIpT/T0epEXFzNKhuu8gQS2rwyHpzI0XfUsgAI3LV0Ssvdvys+a34JQ3CSca6YSCwCWWbATwR30lUuKAO2FDMPgT6+H25uAHX38gXamfgZlNKCWQhKAoQvXtyz/NlNWoogZBOsKwkKl1hKxW3B1q5LoW9WUuUOVp/Gz2TdPjVWrQNMJDhcrHhgvdj87dYngDduBICdcmrypzxJCMz0oC5CKDqu4RuC/ymdG2fgFOv+hpEgMU5Ha84YTSZYcfxofOW71AMIgxMTPQlJf8F1r/ZUTSW2wIQ/z8hJ+/niiuYQtaIKyGmxZj50208V3xqIseUji7YG67L4QNSeZ84quCWzeo6MWiiYx3hmPC0u67w5hotoreqeIVefdsvMAYX7rMdvb8NKlCw8qbiUv8raSDH61MEvKxMOV/rXwdZpucm/02TBl22yJ2chiu4nvvXMUvqYFpA52RjOJt9/zxdVBzMZ5V4YJbQ+EOHwIRc5jXsDnHG6Nsf48KBLX5ysxul0+y2YBDxD4v+NFmLlkTUO1TyAiP8MUUAOsj080QxlcBRODyqz5RC6dfH0AKcVJjNdVs2b/1pL4GADuCUzcylMEQyzg8JbeESwYGfJkiFnXU8EYt7IZxfBY0AeNSgDcXVjoYMEUDTLkLreiNx5Za9uD42NJujI3MpYbc03EYYdxNy585qUeaA0y+p6SsgCJKoLUMa4rLQqxAjIV5B4rS/es/sPWUTdcr/mh3YtI6Y08EnzbuXlA2vCAIvc2vUhKNRJuxvgE55vvE6k3CJMZb4+EYQ/Q5aayHJDEmOFPLLS5d/R7XlyCMniYMFL9DNkMjlxsXYkJj54Xbl4leLmneQEcn6eqUzLi4JhVtWI0b+r58GjbYkf6R6XXYztse4TGrYaUNhlFYyI=
        - #1:
          - type: tool-result
          - toolCallId: 1k9rb2yIbhGUBGM3
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: x9lWTb8IyBr1oTnV
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 8cytk9SBZnczEkoY
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 10qnGw9QvEOUkRuE
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: b6smlSYfWxOZ9Tex
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.