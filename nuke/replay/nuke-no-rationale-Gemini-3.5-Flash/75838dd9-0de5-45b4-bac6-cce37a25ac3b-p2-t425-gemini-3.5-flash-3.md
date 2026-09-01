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
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: Researching Satellites next to unlock the Apollo Program, reveal the entire map, and work towards science and technology goals while pursuing Diplomatic Victory.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Enlightenment provides a free technology and happiness from universities, which is critical for staying competitive in science and tech.
        - Policy: Enlightenment
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 3
        - Public: 80
        - Private: 80
        - Rationale: Maximize friendly relations with Poland to secure their votes in the upcoming Global Hegemony World Congress resolution.
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Public: 0
        - Private: 0
        - Rationale: Remove artificial negative relationship modifiers with our friendly Autocracy ally and fellow vassal, the Aztecs.
    - #4:
      - toolName: set-flavors
      - args:
        - GrandStrategy: UnitedNations
        - Flavors:
          - Science: 80
          - Expansion: 0
          - Defense: 90
          - Offense: 10
          - Happiness: 80
          - GreatPeople: 70
          - Production: 80
          - Gold: 100
          - Diplomacy: 100
          - Religion: 90
      - rationale: Focus heavily on Gold to recover from the GPT deficit, maintain maximum Diplomacy and Religion to secure City-State alliances for the Global Hegemony vote, and support science and production for late-game projects.
  - tokens:
    - inputTokens: 69418
    - reasoningTokens: 10401
    - outputTokens: 273
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Our Standing**
            
            My current focus is on understanding the vast score disparity. Hiawatha's dominance at turn 425 with over 10,000 points is a significant challenge I'm trying to reconcile with my own score of 3022.
            
            **Analyzing Iroquois Lead**
            
            I'm grappling with the overwhelming lead the Iroquois have established, particularly their near-certain domination victory. Their city count, population, and immense military strength are staggering, especially given our vassal status. I'm scrutinizing the victory conditions to see if there's any recourse before they secure their final capital.
            
            **Evaluating Diplomatic Options**
            
            I'm now shifting my attention to the diplomatic endgame. While a cultural victory seems unlikely, the upcoming World Congress is critical. I'm analyzing our 29 votes against the Iroquois' 33 for the "Global Hegemony" proposal, which requires 41 to pass. This presents a potential, albeit narrow, opportunity to disrupt their victory.
            
            **Revising Victory Paths**
            
            I'm re-evaluating our victory conditions, specifically Diplomatic. While the Iroquois hold a strong voting bloc, I'm exploring our options for the World Congress, focusing on potential disruption rather than outright victory, as our science and cultural progress is too far behind for those paths.
            
            **Leveraging City-States**
            
            I've been reviewing our city-state alliances, and it appears we've secured a strong position with four key allies: Prague, Zanzibar, Wittenberg, and Winchester. This network of influence offers a valuable resource as I evaluate our remaining strategic options, especially in light of the looming World Congress.
            
            **Considering Policy Shifts**
            
            I am re-evaluating our policy choices, particularly our next selection for Enlightenment. While beneficial for science, I'm exploring alternatives that might more directly support a diplomatic endgame or counter the Iroquois' dominance.
            
            **Selecting Key Technology**
            
            I am focusing on our next research target. Satellites seems like the most impactful choice, as it unlocks crucial advancements like the Apollo Program and reveals more of the map, which could be vital given our current situation.
            
            **Confirming Policy Impact**
            
            I'm confirming that our choice to research "Enlightenment" remains beneficial, providing significant advantages such as a free technology which is critical at this stage of the game.
            
            **Assessing Diplomatic Ties**
            
            I'm analyzing our current relationships, noting our strong existing bonds with Poland and fellow Iroquois vassals, the Aztecs and Brazil. It's perplexing that despite these friendly interactions, I had previously set significant negative modifiers for the Aztecs, which needs immediate clarification and correction.
            
            **Clarifying Diplomatic Relationships**
            
            I'm dissecting my previous diplomatic decisions, particularly the perplexing negative modifiers with the Iroquois and Brazil. Given our vassal status and their overwhelming military, these actions seem counterproductive and warrant immediate correction.
            
            **Preventing Iroquois Victory**
            
            I'm now focused on preventing the Iroquois' immediate victory. Their capture of the Shoshone capital, Moson Kahni, is imminent. My current analysis suggests that if they declare war, my vassal status will automatically drag me into the conflict, forcing me to fight against the Shoshone.
            
            **Disrupting Hegemony Vote**
            
            My focus is now on the upcoming World Congress vote for "Global Hegemony." While the Iroquois are close to victory with 33 delegates, we have 29. My strategy is to secure the necessary 12 additional delegates to prevent their win and potentially achieve our own Diplomatic Victory before they capture the Shoshone capital.
            
            **Securing Allies' Votes**
            
            I'm focused on securing Poland's crucial vote for the "Global Hegemony" proposal. Their 16 delegates, combined with our 29, would give us the win. I'm also assessing Brazil and the Aztecs, hoping they'll support us despite their own friendly relations with the Iroquois.
            
            **Securing Crucial Votes**
            
            I'm now working to secure Poland's vote for the Global Hegemony proposal. While they have a diplomat in my capital, I'm exploring if their AI can be influenced to trade votes. I'm focusing on maximizing our diplomatic relationship with them.
            
            **Refining Diplomatic Influence**
            
            I'm re-evaluating our diplomatic approach, particularly regarding Brazil, our primary UN rival. My previous actions of imposing negative modifiers were to reflect this rivalry, but I'm now considering how to leverage their significant delegate count more effectively for the upcoming Global Hegemony vote.
            
            **Leveraging Permanent Alliances**
            
            My analysis reveals our permanent city-state alliances with Prague, Winchester, and Wittenberg, bolstered by our non-declining alliance with Zanzibar due to the "Cold War" policy. This provides a significant delegate advantage for the upcoming World Congress, especially considering our existing diplomatic ties.
            
            **Gaining Belgrade's Support**
            
            I'm now focusing on Belgrade. While the Iroquois hold influence, my agent is en route. If I can sway them, their delegates could tip the balance in the World Congress, a critical step toward disrupting the Iroquois' victory.
            
            **Securing Belgrade's Influence**
            
            I'm prioritizing Belgrade's quests, specifically converting them to Hinduism. This action could grant me a substantial 206 influence, significantly boosting my delegate count for the World Congress and potentially allowing me to surpass the Iroquois' current standing.
            
            **Gaining Key Delegates**
            
            I'm excited by the prospect of easily gaining more delegates for the World Congress, specifically from Belgrade. With two ambassadors finishing production next turn, I can utilize them to gain alliances and flip city-states, which could significantly bolster our delegate count before the crucial Global Hegemony vote.
            
            **Investigating Gold Drain**
            
            My focus has shifted to a critical economic issue: a significant gold deficit of -296 per turn. Despite substantial income from numerous trade routes, especially those with the Iroquois and Brazil, my gold reserves are rapidly depleting. I am now meticulously examining unit and city building maintenance costs to pinpoint the source of this alarming financial drain, as it severely impacts our scientific progress.
            
            **Addressing Gold Deficit**
            
            My immediate concern is the significant gold deficit. The "Global Peace Accords" is raising unit maintenance by 25%, exacerbating our already high costs from a large military. I'm evaluating whether to adjust our flavors to prioritize gold even higher, aiming for a dramatic shift to solve this issue.
            
            **Securing Key Allies**
            
            I'm actively working to secure Poland's decisive vote for the Global Hegemony proposal. Their diplomat is present, and I'm exploring avenues to influence them through trade or by maximizing our diplomatic standing. Simultaneously, I'm assessing Brazil and the Aztecs for potential support, despite their friendly ties to the Iroquois, to gather enough delegates to prevent their victory.
            
            **Adjusting Diplomatic Leverage**
            
            I'm fine-tuning our diplomatic standing. I've boosted relations with Poland significantly to secure their crucial delegate support. Concurrently, I'm reviewing our antagonistic stance towards Brazil, our primary UN rival, considering a less severe negative modifier given our vassal constraints and their inherent voting self-interest.
            
            **Leveraging Ideological Unity**
            
            I've discovered our strength lies in our shared ideology. Every civilization but the Shoshone follows Autocracy, granting us significant diplomatic and delegate advantages. Maintaining this ideological alignment is paramount, especially with our "World Ideology: Autocracy" policy enacted.
            
            **Analyzing Master's Opinion**
            
            I'm currently reassessing my diplomatic stance with the Iroquois, our overlords. Despite their overwhelming military might and our vassalage, our relationship modifier is a perplexing -100/-100. I need to understand if this extreme hostility poses an immediate threat of integration or increased taxes, or if a less antagonistic but still negative relationship is safer.
            
            **Correcting Diplomatic Missteps**
            
            I'm rectifying my recent diplomatic oversights. I've recognized that imposing severe negative modifiers on the Iroquois and Aztecs was counterproductive, especially given our vassal status. This miscalculation inadvertently increased our "Afraid" posture with the Iroquois, which is beneficial for maintaining peace and avoiding conflict.
            
            **Adjusting Diplomatic Modifiers**
            
            I'm fine-tuning our diplomatic standings. I've corrected my miscalculations with the Aztecs, setting their modifiers to zero to reflect our friendly alliance. Brazil's rivalry, however, remains important, so their negative modifiers are preserved. I am now turning my attention to Poland.
            
            **Adjusting Diplomatic Favor**
            
            I'm now focused on securing Poland's support for the Global Hegemony vote. I'm significantly boosting our diplomatic standing with them, aiming for extreme friendliness to ensure their crucial delegates. I'm also removing the unwarranted negative modifiers with the Aztecs to reflect our current alliance.
            
            **Prioritizing Economic Stability**
            
            I'm now focused on resolving our critical gold deficit. By setting our Gold flavor to 100, I've directed the AI to prioritize generating wealth, forcing a switch from research and arts projects to gold production. This strategic shift should immediately alleviate our financial strain.
            
            **Refining Technological Focus**
            
            My current priority is Advanced Ballistics, appearing in three turns. I am evaluating immediate post-ballistics research options, seeking the most impactful path forward given our current strategic standing.
            
            **Selecting Key Technology**
            
            My current focus is on "Satellites" as our next research target. This unlocks critical advancements like the Apollo Program, reveals the entire map for strategic understanding, and provides access to "The Internet" for tourism boosts and "Lasers" for advanced military capabilities, offering a strong backup path and crucial information.
            
            **Adjusting Diplomatic Standing**
            
            I'm solidifying our diplomatic ties, significantly boosting our standing with Poland to secure their vital votes for the upcoming World Congress. Concurrently, I'm resetting the negative modifiers with the Aztecs to reflect our alliance and am reviewing the strategic implications of our remaining relationships.
            
            **Refining Diplomatic Goals**
            
            I'm prioritizing Poland's crucial votes for the Global Hegemony resolution, aiming for extreme friendliness. I've also removed unwarranted negative modifiers with the Aztecs to reflect our alliance, ensuring our diplomatic efforts align with our strategic objectives.
            
            **Confirming Flavor Validity**
            
            I'm verifying the flavor settings to ensure optimal strategic alignment. All selected flavors, including Gold, Diplomacy, Religion, Production, Science, Defense, GreatPeople, Happiness, Offense, and Expansion, are valid. My current focus is on solidifying our diplomatic standing with Poland and ensuring our ideological unity to maximize delegate support for the crucial World Congress vote.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: d6aF8IXI7QnjE9L0
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: Researching Satellites next to unlock the Apollo Program, reveal the entire map, and work towards science and technology goals while pursuing Diplomatic Victory.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a18ImAGletlcDNIQCyEXq3OjlIQp7JsotOQjMnzMZsfU9nnitLiVtW3H2wsMFMCZnLJ7CEaDccaWYqtlLtWVwrDYQ4t8AXOfL/QPFR9l0ycIqBTtkj0faGC49vD3yp8+tasE8+uYz26ADdrF9Ic7u9lodV73Im+P0Gz6HxXVuHSYJyMq70k3EIi0MY5kdnIf6ShdWB8z6fzzzyHcBNP9r048qiZfh6i1zo5NCJb6wnTJKUz8TUwXGRNtF4Tg2KGgQt6rxBA8Hm3EpWBPOnaAt6NgZ0OSRqgQ4jv6kDuY4u3rPQTX/LYiFLcHG4+hTKVWXUEPHMO9QI30rqgYp2hmOGsHb4oDNG3PAlJv/1k+rTwsOqhArTjlS3tjQck82vmqTiQKaW4PgLr10jvWpf6sJpWICuBRXgEsee1l1gHKW7X6VTkZOcb/EAyB23tLWZ53/fqRo4KaWBRB0yRwWGIBDh5OoqoRV+b2CBXsq/IZ1ft6UrFpXFUCb1rgAt+zUjht72qXp3PYK51McfdnSxUNtnpPKIdG3TLqytm1RalUfe/w7+cpJasEp4T2fo9tgIyS0oXDZf5HnuBhgD0K+UzJOnBClRgPzNgb+CptFD6hdnx8O15fsqQICtdMmIRICXodU3xABkRn9Cx4TT5u8HmQ4sbAKg5DtEUNL3CcdRtC/t8MIP4kMHeZCca8CXHOZcWeleQdMAmO58oL7dMVMsfjJDeq5z5StFOinup4P9gE4aauBkWShARHebARwOmL05QAKv88SFvpZQY2kX2X60ShVBQTJazifPbTdAa1pUU8e4MdfzPgxGP4Fexyzex+/IN+IsRewwkmQYrwidnyqM5ihK57S0Yr0escpCOaJmEaGYFcriy006bkjKBW12F7yU398irPVYYpVfVjynF7vwgQoQbfmtxbjwC8drbCTNvT/piNhgGPC+ncO2+gDyUq+Myr8jfZxvOxo1fjmkpiZV5yLzDUyrNyqfJTWTowhrnB9LTDgs/jpDZzl1zf1WIfbW51FzBPAQ4m8/s2lTLLEZSo+vLFZdVjWweOxNisNwGUWE5R2OA/RTV1bt47mwMFlqhQzEKCnDwUbaDF43sRS/qebPi3bpu7Jg0TWNsmG3BCnYzMBsD2RxFAK0QMhSIhN1KjHI0WMfzOuH88Hh4diR7AAYr6QF9LGVpsAu19gSzbcGhF/b1GgDPLFVNBk6FST+a6880uf3CIJroTpjYcm6WaXV8EijP4B3njANlb8VfcLpTBsE96O8PCyZKysHxsc5foKJhTrPPdcUw5Usokv88vwbw7uFV0AQAZ4qkWDShxqnAPLaXvW+UCez/QRcANL7TJ7diKN6RU2UFPeY++cCFHaV2WuXYLlq9zxt9MZYlijSj8U0K5AEVcOGRnWZ/WFgIlJDaeQ/COgz5VtrxWrbu3peTpLCHJDmpIGiLWte03QodYajtz3sMjOCl7YuMG0idIdSE4mVOQhVZfdXlN4wTJoEKYuMS35i24JfK0nZEQ3crh3rJ2U2CplmWJk/g7IoRVWx1QEawh1x0Vm5HJfcvLp2PglHOkWP4jLLcTBCQlC9p0I88kZU98FrKCABQllXTnHfitzDwL2d6LkI+h8ZdLkp1koBveaLY7aOIiOV0mn3bQ7ArZYJUiCkLJGdc+zhhIkHPig9tuVaEx8j7gNkBeeRPcCocKv/vzcU1DPyam2Efvwd1UGFuS4BCFV69cA4nOapzKrx5snIoj3mj/PIFI2Uqr2fGig82xDdUuUGQRLTo5YVQl4Pew946hRjHN4tx2RiJImRLyRS5Et+wjjFbGyEFpXGeVI0odu+xqnws+0POTW6dsQ8I96oSppyRPlkAMOOLsrjjNxpeSnUk2JoRP3mT4TibkbYyN06cVIjwnovEYvBQqnVCaKvV+tRDTeVd+pJ+Og5KIMECfLdn0RzJ/52HaPWIYwmudyQzEx1vWczNjHtPQNrJV9fufA78Rzk3G1qmLGm+Na2KFd9bdQd24j8qnmjGKFqRD4y3L4wOgd15P0Ru6pQPIQiaYvSCw5ZJ7K1vNX0wXywPr/nk99eFKjMyJCsTGT0gqyQxhaSmfNFHMQkqu60gxTCEqgSYghySUbOQmqG5WgJJ7YLLhwdBeh8NA0GBumpHMPlGgR/N63ChBKzLj9ysb7px5xsgOdflYjrbM/NJ1Odq3FIFM4vHAjSZs/23/yQVCrJRP9mEaQbRACEq46yTt71+hdJKH1EdQHjfC7KuCpeqmZj3CzVdRHAU4da1IbLQ7HMdv7t/baRDrBw4TF3LkxOpjvUuondy4hVxA8S3KcRUvMAWImJwmjtbqR01UXMGNRXugoDzlFS9wYF/NlfVwtlHB+fHGCiw27m+kFSUQcM4IzajuPbBVJa6gSR0rbpDG1fX0TPrfrtkWthjC02Va7tu6lwcALZBw8ThfVY1j0kWQYO3Cqn1sRuLWZHFiYQYQrC2HT88nMc99e6HQ1GHTJab4/wT5qK9Am/S1wUEmZso/pTGAJ+83/46ce2qMn/aWJp68WelhCt7QyQqweacZCPz+4NojiAJrM5ej81YuSDYcgXDF9eQbGh9twsLVtqUapagsJRMQnxkjbvu7SBM3RNd3Be2gV9F4UL1AC0DTn1qX332+j20KoDDlaQAhuy368raiQJCceJMCAF8Sj7RjVBczHo4eWdFU/hqhXEHgdJTfZXWA4rXZaYnMjMwy2OXgnq24HRzxh6zQXUiv/+nSQaQMD1mfX44qhkasdq8QxYA0lyNg1HFzDJN41utPkbhST/6PuJKP8jBx49D1Q2YWcF/7f31qXgJGxn6h9xRskOcwnKbR9w14yeGrDptaGv+VY0WQ4bqwXnMJsYx6ii47DX5FNDD2IX76uWnNsygyO9IUOFzl0VkAuEgBrdSolF4hqo1o5pT/k9xKVhclE+5aRzYpR6e988WRQty0ZSTc43Wats92rj3aDBtJ1C6mnI1s4DcF83qsCX27BRYrgSaq5rxRNxMvOEkSBB5in+IleHs6UHJHbw3EnpEk62891EBO9R7FpuC0HQsktNqm837trkmHSiXVho0jh8uiRny1TH+QRFVBV9Gf5R6yonsggdhncgqrbjIL1ppCfzHl6ejWB8k088DmTmCzZ8rBxyFZBKuWlHtEHyurABXUr6HM2ykp+cRBcBYcoqRB9NrSZCNe/+2DiElUdEkHJEBbwwSXfmr/4MdpkG+RaVmnji2gvUPUVlE5eO8qQz51dJk6txbFx6gVUFYCjm6pxRI9fJIiA7e1MMLOaK5+LU4TgH9/bjbr9CbM78UsNputQIyFe5TBZ32xRKdL3Gfo+zCVCfnSoaJpFELpAPv3EcjL4qqNLsVb+H58pIL9+YzkkK7TYxKcNm0tk6sOzWvny3AHI0XAJjh/TrDzcZIpG/rMuNikQ2bYEr+102XLpe819qmyMPZtzmUTVKfdBuDzDLKoE9K5tsG+FqBtiJls91iqG/SYG0zy9I/wXFSehFCz5d5JJrBGRjrNkPGVmnNdxk7KwKC10iusswjdjHHFAfm6PWnE5TxGynWUUOC8F3K00PWw7LWQGCndIcf7CuxHH6Ts5aRA/f9aD0q4P48mbqd5LE+2k8AheKLCBisKwrkxgbbPD+cO9zSHQQpFsktOW63rgifSE3hkAfXW0CvoJF9zMm5iK/lHqLgR4zvSUJfsJsYSOHXMjixP4NgEYcKSuGUZNyDDSGgqtaFSIIUvv9WDs9QBUP9LyXIFWjfUdYvyHwENLnT9LwSY+jhgy1P0g20/SX7j/iKk69TkQXbFDNBKPQiXw/QQKl+xXK7fIumqhLT2ZlD9dGd1OpUu7Uo/lxaq6ZpyAjAWamRbl7wfF2aOW9x/ODn3vh4+vrsCVNdBAX6eaqoAXKDlse68UgIQKHorxw8DGrB5tVs8YnZvwYfpa5gHGNZLSIK6kkVqt3w1CquXhhPRveMjOssWw2ZCZ3uTyF/J9wh9r7kM/AefVBrrlZ57A259AGo4MpTk3+POg53nhNJKc0gVz4qcjIrIHrDFSXV3GG6W3TRNfwKP5Lzm+dW2EpaemdqNV/aggRZ6ZYeFnh9BOjDK6TuxlZfixLXvw8uZMExF8CICQ/YHYX2360P2Uj/mX7bxk1yrCeg1ia84wMDBvk+4eCbgSFWhmjWxuErShDzMdK8KRoyxaN5NutU79EOcOEAXku4ERf9ebT9INZbt1cmA3BF9heAB+zyRlHukjrLooQXyQe3KZOqV7ZOsTq0Luk7mZb3Tic8YUogIJqo1LbjK7DonZE327hI23GA47DLBN8ePKdBWgb8KxGCNriyR2lU3mcq6AM8n79hg6axTXHNFAouj6Wxohqrey+a1ccqa/4jveNjxWg7X695l8rzdqLTDi/ZZzNYcx845N0h0S3ktKuQL7HXeDawFgT3yblkEbY0hlFQdFbN9BhJNknYxeCs9SDXRonQXJEgb+noGC5nBSmwClqso6v7QPrOVZAsmcHHhtl0yGPXcR0VLiBbfNUrtAzLimzbrNRZvnSQt+3V9HBJT12fnYhSeakOtHtKctAM031rjm59ljRBlhxuUq/MnAUpasYeJfd4fTfEMjQyQw63aNP1ZgtMy5naHW2n5GV5JqMM8ylQjSpHjauHmMVM1RJcknsJqUHX8n8EoM20bq5GCVlQt1Bttthjw0149GKiTduJH6q/6+BtPCkljbCdFOAA43ImQ51Qm/9vcDALy6YAfjRg6c1g7hf892xEhq+G8kL3u7X4zX1mP8iPn1vFogqgRtIRLhiTVdkYffZbe+bIO9fGmxyhxbpMYFwJNO4ihdk09IPuO/c6TmdmPLR75kBJ4Kid54XQCauW/e1Yn8gt9D+SevxEKn5vdaaHaqNmz5OfKRWD336XjKe0MyQvsXvNBttq+1zRSmPsm/UpVCU5pWJNUwzfNBUCJmmrAyFJXbC23+FdqS04VeciRbZXQdKWLlFTQeuuwFxO2f23gvUZIrsrtcH80bWnuzJqexWZUh0sBa+Ze6vEir3mP5P26AEBvv11xRNVN8kAmug/91e5uNVZPnI4lgvogBwu79XMKXhooEyYqE24UKxwFcYtyZ7ytfXGA8kOwxOrE10GEevxWXdc4oQx37bNJhFD57Vzd3U/8IHlLZbWU/UdAHPhfionlr5KpxFxrRZ2Q3jtjHQKZdOkwntaqqQGOfK+OOF2iXwIo4c9AouT8QOqnmEjZ7Nux4gESlW+AZFwzIOXKHagrDpnYwVonvn/X2iQ6mkbbR9F96j+0lpKnTr34ygSObPFlioLonYA48LeWBSqaTXkZgbv6c+985BNv9gSt+dgpxunRgW0IAj3KPnoEBrafNWQvGcPzzQvWsA1jnDSEm6XQOnNUkD7R1YHaLNZZsyzr9YVwtZi+/LOoAyft0mMWr5b/aKyaHXjKueMv0jJidyrzQCjf5BBhTq0DbnZyCZCWKJrB3/f3kc9eOdjM+8GPcBR/DEaA1Cy6TA+/STHCsOWEjeYnEZQKniR17uQpnOdrvPnyjqbzGAgfV8ug6yvIkAS9YRQ96562tnqJmNhEPf+2xmPTGw3y616e/z02fSizpwSGVcOyjcxWP88DcDEvC5n24GuMSRni5IkPeq9ySL+Izgechff+xqMjBvoZV4y6wpv4EVUXSQempkey2DA1bTSTJ34MjAspMOQ/AsYNb8YQzf1UxYwimOQNrtB08KeYQDB5xiP5AZ7lQDkvdBDZJNAu3V2mH3ISnst8Uh4vjoVUJL4Q+Crt4ORayV9bBdmjHORGJdYFsnLb0XY7y1p8Y9FcZ9Dd6Cm2x1gOpiGCAN9UU16eCrr+sxT6qTylId63OjzpOk/Y/4gmyLZ9HljiID/+IUxB1zxgLLaJ3M6lfL0ttU7grizCY2KoGxipBQ3g9ZNfRH8jQmJn7wWeGP1iCwfRlZlGAyTvoqAR3qc79V6YBpiVLg1sVP0UYFw4yEAXwCx5zMh8jL+e+ohiyUIi2/c+JF3WsB+XE1mT1fRN8JdO7xfrY0s9mNBzpkHWfYDmcRLfdWfuOLzHWHuyO4RpwNbtpnfJUkK/0rB+0G1/U9+//sGllbFu3SutlNoec48xOgscxZA2mFfsq12lg9jj9dXwnBtCnOybTAhORvpJ380xImPHWMpuqtOXWPcJinBTP6VRQcZ6IffFqjY1ikmtcIFspcss9Dx8Mg03+J2WMWUS9nMnXS9FcVgwOu7qSQ94vqrr7/hDEph+3YMJi4Q2TKV13z1s7hmxkjgKZWfvB7HsUcnsCz/sYcEN/au8GOS5RgM4RqohZ4zq7/2KMGtdzeIir8mHWncvGqcpyqvaNB2OWBOsrsMQHCeTiIYynSsTAVaaMO+pOFGUmybPs9mDwOXv/gLijgqlXnND5NaXd2I7kV9Dg2KUKZFwSodeLnKqbOpRcxeQm/0XliylYJ7F5biiD6a/1xzKuvRVG5orEzj2HeFMcsPjnzocUVAZCi6jRJnk7WxN7zjWq+R9dmBMRwhmqrHf7uD/hbakEBEGMeN9EFFkps5TG3brFMfyMbcZKGWZRwqhkBDVd5l0clvXLZFj5mWG1GdDk+DvWOql5fOr7K5NJOG/7bkY31VSd6I8zgBnpiH+NBRqCtvViDTHF5hn6vqDE+39hGVv9AqUMmjrOQswhxnNbOjoeQS2fs1azIt4vOiyddAu+TbiW9T0GLqbBCQ1n4cSDwgqBw7X6drNB7KkMfBtPaHSobpeRIIme6H1uSapHFv/f4yIvMlhQy7u9bU8neaiNSZNCSBcG1USagWEYobeBH8aMb3xwXCTyX/LDHeqicji9/35/RpkCL6D5HfvpEV+RhmP0H8cTwo6Wi/QuhiSYg1Fie9+40ZSvkijhk50jczgRg7cH8VHadE1nc+3Mi/9CZ1leZbXzlx3Bb1tfX13CjG/S04gEpR6v16j/NHuL2G/rGZjOvG8Df9lEBma2kIn3efSkbFhY9YwFibVPdiOiUJp7SpYHpzsxSDlXEIWY3QzMmVYzziuvpVcVD8IpplY7lMbCJYY636F4Qq/N7MWrmxRQaydewJy6T3RqbMky4er1U3//CGe+3Vjj5T26Vm6H5fUD0CYVyAS2eZoRsHWNvkbvcqQWcFcAHnMylhmsrV1alumpwRoDeY9ISnDyImZ8FCE5b+17uX6E6wYp5wfAgyIMHm5OliBNqJqHSgt+0wCetUct/n8f0Ug46b6TdglHeu+SCW2HKyszsedhCl2BXefaLUZFCRJV+eKKKr0p1Sjd/swHF7Hv6p28zv9IZGqfaQfOrDE5MShIppiwim7gI8fYDt/f1p/egguutGTQq/wMNAl7A3Jpb6NEkCF2cICoN4p6Dzd4SZff+KdkpSoBguNsfkoYZbhHm3nKz8fKJHcHn0gWbr8qyfpnOXPVUTCEuJrI7Bxh5H/lQ3hsf8pcZv6xVl4s9TyqSFwPtlwhSr2FINfwVfFocMUsIWIDNRZq4olQOHc1LDfJoYEmYOBdlukUNSaCsPaRFFf43CYKAgiuKrl0xm3DXSp6xHpi0U9AxLxtsMROl3JUsis92x4lNAIcnr+Xy0mtJYV60jTm0AnZypV9/Hy1RcEGMTB3LJy5io36aPUutqr9T+8pCi5zjg/C65ibUHLACJ51uehLV1ACf3abHgbUCvSSgmahLZzb600gCBusZ8fjJONcSTlvdf7Y4sQwKDYQWlMo2YOzrGRg1HryxKv/rKIEOTiymKPHPMFK4sDMSu/TYx+omMFZDMfSQgPaUa/KUWSCEzs1cMJ3ocspc9LA90HxerQi8QIMgrN0b+4KZNc4LG6gFLCU6dL+oA41B7oYjLuY6RAgYKih39Tvdto6zNvAdLtgvuAn8A2F4WhPyr5uKnb2rJTZxWqSdoOkmF1ZrpDVlne3sukEJwkCYzsLJloccHDzeN2OsvxxPc8E5/vG1OBYI+YUqx7+C4NLayf2FM1eO49mIRl93hIEfwCHgDoLQgItQqwI1JR832t8pDXOAql+M7fWw6nON+W3hdcmX0Q3WW0p/1eV/nwAphNmkew/fm9on5RbMOWUuSmLEAm87/NGxwlJ4B39HH4UItAHaZecHso8jFMDC7f4K/sBhEB0wqPW8xCDprDVWwW0CE/Iqr43BzLTWbZT2bYpxxDvosSbtkRzMg2J8E74o5mjp10R2VzICSGy32EaWfIbYbN6quExn2XsECZ0GPqjyPcsCf4fnBIioW0+3i54REr4JJQw0FGgQvyBHkX5BlnWpZYFaqkzjaQoYwb1R29Yd3tE15X7Q1OLdroV4jtBGuEYT7+7DlxJxDbcN1Ve2vMEDIJ7eY16z6tjQAAX3cnyi+mTt+2NBCeZ7eOM1cggbjHDjpiNEMb9V14AkI3rLHQyHrWGAelexQqS9X5e+DnhCxlzwK8BZeaksQxlpPFGrxjsdaAY9rzN6n1hz7TdFADMsFjPZyFe0ShnFxNuMHpFexGxVukZ6ZWuWFhKzhvGKOppFDExTxKD7UiALfUJXoUCZhRJGE+FMWEjYxggMgmI1quO7oh8P2YeXk8wS94FRlUfZVn9+mRNKxO5755x0M11Z3zwX5F5Lo22sZci50RoJiMpvl+UnZ6pocz3J+v0mZi015WXYd5T/xZ7ztg+eklrbBBsid2Z4yVHcIX1ge126IglfHnzNJHtuSKhTLVCi2VXWGYPb117Nh5YX/tWQ5gphBXDvNOGostgve1gcGje/WscyzuXxZQdR/pabca4/DQGNjbmRnZ4Uq8McNECyk+xOVZ9shOY0jQr05rq0KBQzaYNlwvOFVnmroImEaAltLbColTAYlyiXyshNOKZnOY1A0YHNgNs/ZgbixzM2lb9YkAzdd97BQ8wCopatJ8w2MCg3v48JtFnoqWxTevX9X9yH+AS6kL/9buba+/WT3RxoGoqwzV4GEdmfRGzI9k6AzN4OfJJNLpoHlHu7pCRSbDB9IYLh0sVOCcl7gVrj2+Zt7PvtY1VEKmiGiYvyLpnDAaUFMYrugLzSMM8a/b7ZwZZgR9Xqoca717PPgYxawg5FtJkRdnPYI8MMbucqt6kqoItobOEAYoswDcHgQER9n+W0PDJeZ9bjezvC2sxSL6qGThCuon5flqKzq/2WKR+oXSnJFYrSRSZKynSLfZ8o3mXc1yYECHBuBv7WYs90CZ5mIkuecdXFojD15XP+Etph0E1/0bfcG6oYC6hHha1eGj/QPeIgEtGHhjUkFr12ZQkHqrhZoGKkR6uYxUImKMwwMyy18zLa9coJ1tFh62wWOOLY6+uSVaU3U9VSRM6806y8EUjI3d+CfCQvMj4g2gOGXLz8ULxSIMLTTZ1G5GawTukwh/YPGqkkzFtKntAg1cVcp97b9y2wqrMkiFVajDBDYwgCnjm4eho1O4C57FyFBlgN6irBljx9DiFqF1lSmldtHRn/3LJnP94qZZIS1loVMG7RrMTNUpJXDKGJyJ3b7Yh8soBhqde6tFc8IjeFU2qItf6aXG18iEPr07p7PcCLfbZcZbRjATQ3L0wCT5qSnzDguR5neKAa9KDtKVXwkgnDks+aTo+Rjv/Mr6MOCNFRB54+EbMuCsAewNMpAWGhdha2eDQWCZlbIpH7JKFh7qgFXV5MUUGeBnHRqkgF1YkMK4NAYUtEIkYmjkerDnhBmyk65ATX6DoMSw4oz7gAF/MnXnjBdCwyGRpkW6q9M9Sa4SY7R/dhbmpfDDKYxzrluIdjlcmlXLgWNLUHNi10hZFn3jiCVh2/zpe9DDhTO2ZGmRzgKWpDp22E5GmIFGBp7yBbr24LN6v5yYjEB7xrfFQ/TS5ejxfNoIIhmAaTmuAkEIiaKRLCjNjy7mCDuLYU+dfXSEbSObsoWWByvXbrfhyc1L+Q18ptJrTq7+dNuS+zbOsojlQTYUzfJvejpqghPwZT4yRdEUjzSXsCnSXIASzrKZk3RcOBvpBRqbEdSCbhe5Tuxsa0OYL5oz4DiAbtLHBR/vws584krURwq3qX9jux/90e3t++Pg5KHhRiiJxzjzph3ArJAeSjTFpoJlqOBASf8rg/i9HjijBi3sAnKPo/HMPMJGFzNsjja+HYJDjOTNqpscMhJCATHZqOU8lLxE0U94/hSzfY/1clSD6EFcaDhd66alrMQbzCjKnh33AqJSp7STjTdM+ZFzRxzSu1yHtncZR6G70J7GDl/IffG90fw20LXy3HhcC5jM4wCtAypohTfhBUcp36UO+Izn+TNhfv0xy6uZqZHGXR96BRPcLmDiOVQhUaGsot2abZTk42zpmtpN7Udyx1fnhGY0gXH/wknVkc+QPPacXf7BReEsgaWxMFA48LJA+u+1kd6txDlYp7IFpVq4Giyq93HcYFzwclxbcrv9kNw8TtcABvjMxrVoHdVJMe98L6z3KZbmKtnw6dlo7tjpRs7b8UTHEGDDlpkrzUbr19ucORXnEdtz2SvaevvkmZUHi+34uUoeKZiWnI/pU8bAvjRtEfLDFQrqLv24dR//vO34skhbzuIZuoqOJsof+musXIKe6uYH8PPSvMCJRZaFrlTxiPmAWMhOCHmIL9+V3zYwLZnqxF+uE1IE0vhIbbTC0qHBJoOsnD6AcyTzVVMzPpnjUUyiR76RU7zWZOso+YuiQYlBNTXVgSThXcrLvtL76izbRVj2w1m66mvs0Xkoas9/RaALLQJ245VWY41HJ2UX7Trixc12RT3GqAUL/pfZ8AmiuVBZeagZsQgpLsugh55qvZlq0B0E6KigawLmlayE2tQDfzSsrC/SaXIA2/WBvkHrXGydjLVILemuFzOSTZD75+s6hxvTNxQmbdpK+DPKmKL0fGj8gGR1uokHm7yx2vn36g4+jiV9pgCFRk3gp2PtGgN/gbrupNi0TnDrCrKEpH7n4fDviDXyk9pcyrdDc4uGw428r+L3ykYV5q03p5P0kn6Eks0rLaaZo3Fe/Cif7z/247kYt1bMo2GQIUbIYoKEthilf7mCOKd+Dgc4BpkO6BsKJL8FZNRc02CNFafexDyhR6bv6p+Xbdr3S2WgRvcxEgxZMP9TaHESARQ+BeVLFGvpp9ytsGP82/pVrNSKPQzZoDTXEg5sOGAFSY43PLT7Ynf4zAbbT8bSROaaML0GpWTxrLahO1Kd/tLcRu0QIdinNSqs6SLRRETTqlzJqBzVIIUYDz5It4WZaxuVU7tLD/w0D+Ls5Gv0m1cEsebq4yhBtWUpJGO/ae4+1z4oQfe+eWx3dibnwExYSXfIRJMZ6rIbsbJgpZU9GoCsrvragc5STUaWaD1DDaRe2wytF8I7auEPQTW1ib34FtTfio+MvNMGuRFc/hxzsgswNpuxE8a5Q+dFp2E5PiHZwjpXnSVFA0IkYOsxuK/ZKNKkottsInZ3t/sS35Uo5WVKexNLJLtmA9gFpH7bQiy2K2tyLuHWGKkxUBuvK6rVCyiE3hXwzbb1hIGXD+tRqd+pSXTr9CcMDgKxymVNcOrEOhKNIR+82vmWkbNhPa4ghuRsIRNNBQqU2b00ED4Xl6vGDLX+H1fN5Vnu0GGMNso73u8aCeHHjQVm5GuQfl4kCl4chXdcP8ko+F8VtXUP5OVLbWacvsgmb91AHkB8SmlWy6CT7lTyTVS/ru40m/IL187OYc8kxLv0oQYEu92duA9Agwxo9frH46afO10ZZGUKCa//OhG1Jpxp2k7bhrH4KCtiSHEskaG7Y0i1av7wZwPy7ESHjIOotyG/95Ze/AECv/a329P0HJMXex3IGiBX1mLsWBhncVjqUj30fofM5kSnl5L8b4n/g5nxHZkre6KuUItzk5eXlmHE//6nYF/5YZ+UOzApDmb2J5c+n7H4PV0UnxbmO+7wPSgg/mcc/f6T/5Dw0H4Uk7wS1Vt5M0KU7VocC/yeAVcjBpa86vYjZGhDIgcEBx8BKBGDhOrSQ3f4uE7+b+F52wMT6MQ2R+xHrJZK4FtfKKBNCk88ebuYZRJi1MCxMT/4AC9z/nq5YZzVpfAw7XJVl12udXYuw/zoyPLz+VGhdcKHkhc8kuoPeLp8H6e3YzLBYmwE0ahiYLvNhEYemV59pHNC6Fb0WjhSqwJrCx1mzEu2p9UvLhVjqag6YNX4MigbG8tpbfKDwC+0Cp3GWYzzpLgd9gGTDEik4umPQh98LoFJPNy2GPxXpvmXfiX0zyr7k1Pi9ZEDgCxhs91w4a4X3+u03xLhitC0QJQ0vqzM2h1CG6pz89Tn6gRCvcWjXi+63+NRTLnd0w72OVW6bjo1L/SRlpRFi2TJQeAas1IZgaV/XvZnYDgWAdNONSGF22chOYqgJZLfoIb+ranE+WriWo8dhBYnq+SuKEqY1JaTHthk3ziNZH0b7eahT/WVGfvbBXk1drqJBaN4ok5cuKCULgBnO7KgeBVeHFaVBfkhVix/TjEr7qajEbpdFQhs3aNQJC04xhCdkdDMAi78ZMiFC1LR06b75NwvUQlwclefCyz+tdcvuMpdlu99Mvv4e/gK228DANhHIUpctkOrypvSq8TawJrQhR0XDkyBCp3ljhTLQrEopghBEHA3b5w5QGPcydEIGxbxB14XIy386wBSWkjNBno4/as+IHB3ilyyVF4QpXHe/LnXXF19SJzlac7Qs0q6Kn0s7BE1VbMUbHTboth/MrL9JQTQuJO+6Fl5OrFMUba34BuoMftKgfe44B4iThk233orL9LUcrdfBHFsTYf3kzH0hS18YvHiF0f4coYh4MPolShN0qYsHiahwtWAdpr7LAJTH17JrIpV6CyARAO4o4HDrBNVckMqD+QvVpbEeOXhdQoIoWizM89oTTPhsd07V9uJqNb7u5tdPiStCUNrlzQE8MwHv5zUnOYHcTU0qzhzBoeE9ncjH6Ir0xmeBjAIBLEG5JX6Rgrtl1H07whNCDRJvrfZ5d5uz7nDxYuLQJSTvJVveEGIn4vIJGZgZySXcD9veTVMXlOLqudjBhCzhPon2bQS6aVChEkORlcPhrGuNoD+2ZMlITF/bMqWlsvPFTR3NsB0YAEUf0WvHX4nUBW6mEudmGnXxCyCbxYdyrUXOH7ijUYVB0MYawDuvaWvMLsindLcFxIVVUhpL8Jp72tK7k9a7J/Y99hWnGER33efCoEUb3vN9Rz0xsKN/XHAiFNbmdUiV67bZ0eDJIdZtX9YRBFCSPgW3n/rvkhpWEnvpgqoca6FueJZ3z7JUWTcU43OfPq6tHjcmFGtx/cdWAc78tpiaH0gqbzLwR0I0X4jgfZoPzyV3mnx66TrRIx2SfmsA1hq0YrtGWAV7sQSJ4o4ZdP1R/l3wCn7LoJbuo7XhRUhUv8JcWQRw77T9x7F4rwuUv6SjyMlHRzv9P6tduCAJV9ksx7FtJdid5nPP+k/fqpFKgJr4wiqhylQ62U4ScPK8e0nAuR33GWK4WwcLdDXS1VOEK6C9C8hkh5nUPihccmkp6mD7DKEFelR6f/oGSH6zYo0xq5SEUmoQZ/MBnngMK9i2B2KX0SiwdKahbaqZgqO1nnIpIKu1HxkNq8IyZs1g/1W/1lzqtlJKFw85C2wYFWXyqoj+v61xKlls1qcfUTOBCNdmx034u8SDZ771AHCZQSGEdWLRBebRpcvTeqmodx5dTT6xRHW2qoSshZzd1GqaxbbL0NtJDtpa7blf4Y7yc0FMcFqBErdiEFDe0/CiBxlWr+GHMu2fjwBusNS6GbJFIHmVvoxeXNrOFa+2F9HS6M0aAWqN/5i2wJPbiau2t6Max7z5obsZUwTVFNcod3kTKQYqpTeqcTUpjRJQT5SoFFT08gxefDrEDEtoWoHg4aVn2Ep7FeBiF1b6IJx1/z40Q4/C+gBnMgORDz3SGTR66qdFJYpb/PQfYqdJu0NuRSriqHa3c7NkvAjsebsPJ0LMNtgfEC0HBsyVbHiWc81WWIKyjx0WvGy5J47GdS4xBePj/TsJYKNvF9HJTZv2rNG7Ui77NV55A+moaUCLmvCLtLXgF8OU8UDvbuluv6NUVa+YpFCvDtPlOzhsM4ui39Pfsem/06h3sYsmOXmC6EFZlU8MSkLlIj/RMPTU2MEUC3CM6HClgUyOC58O1whrwSU5CpQNogOFsmygnl6C51UuSVaWt6i0U7hT/1WBzoFdLPoFxirGc87KME553tab9uiiP8FcxGiLwxhlJQrkaNm2EeJ1iEq7CPEelG+vaLQFsmwtFb9rkwYOe0DEle+dRuS7/1/G7LEb2qcVlPFFOZbm9b4pyyifO0d9NYTbFrz8RxJx2IKNjut7hmtysNteenggec9/XrL8w5aXHI5tFNJZSKRSlSbhNUIuMgiy4m3KXpxs1QLD16tevtjNJbYuN7YPqfx5LsZEVqfpQge3E0BIEOHABmiYuDECD0I7qrzVOk3RAUg7tEBH9QhOrjj6tP1AHXk139XT7ifS/1ECIGlMnJUDaqCX6Se7tumyP7F1QZXJriQtWHZwkc0WdTmBIwAu9H+OzYiDXV5em9RpsP2Stx5VqVWx1m62Yz/Ns80mjwCHlUuaUvns1RHLiSWRIdppOowT2cyNXz4nydrl+3x6bFpcIuWsB6YuCNBH6VkKnt6Xd/RJFmuDH8t1zfLge/2gFKv1j7UDSDKspFXh9NssosFRebhOXgjfUxbVVdJ+jhKfXpaDJ2SokylddrMqcP+/yIfUmhHXjkZvAq8HrPjMPZg1eX2UdAZeVTjW+gGBR1mn1DrEx4LLwwB/KuBGpIPWYZfHYEUrWrLcaVRndftKDpbrOrvQ/towpymQ4Ba5cPbxipwwtQYWOlKTUJ1Jh/W+lX8ktjBzp1LkZaOgDK9c06ZaEFKfmGQJA6VxG8sX6F5cfksAx3/SNjMDMb/lSHbHptKkytZRSjzrm10rkkTZiSOkZ0/VHkO2kINAmXFnAlYz2SI/QdVuN5uy54d2B6KQg0S9m+5aDQysyDE7B4VU9byAm+5kKIWolvNTgIR+WGbyCy8aBjYSE6z/nhFK8DXOK4nOw6pPo/giQhJuBi8I1VGGw+mjWEdZ6Pwq07LVsa9NhitGxKt/1r5JK8dIZfHuCwbGSoZWV3NVhMsoubkZkVy+8qNd9wM2K3zw5tHqsCIbx2Vb9TdlHw6IiGQCoJ+drHCQ09tO2SBAjuZ0K++DNjsyL91ajzUJOzyI5t7Blsq+Jfev4mbHseeTczmuIzfy21SF30wnnk90Br2HbwGLfEpluHXBDE3ftblpsirBirFGkXdKM/P8J/PEMJx5RuNiErStxku8TLhl5JwYcj0YCGsgrCSydsmZQNxl79RE7Y0sEb4uHeWiEiLsOD/fN+yiU+YUU8H5Xn/x4mHEneeU0kNIl3cHkGM52plQUiTJ4iGJLbFhPc3B2oR1Dh2YVnSPPeIL5ragtq8C5SRarTiUU3+RbdYpaeIGf2IHkmigfKOHTFiao7Ei1564uBalz6kJ12fTZ3NmeKTf5/cmBHmoc17ybtB06fNCociRR1qcztMqCb+ZfKw+6obyI7YkAaE4t4hbCLrzrgC/248P77OKfXjsaELfIcHdndmvH089ARCxWauTQf8cKGOMq2df6OhCHXcKQAiuWlIISEl9+L2S4Z96RPtz9v5yKlCZWjA7tXc3VkjQoVN28PrPNH16yuMyCPxgqNkajSWmRNNVkUszu5eivdcma4e0w/xC9hSGGuqY9YdNxXrCCAIg/EUjQ8MdzEPFn37EuzJfogn9Jsq4w0ZCHIL/f7Mihv4IQXFzqfgnTEI1j9vH/X62KNsrEXOJ9GBv5rOM7WQdx0RnEj2RTJBFxDt4i3jTg6y4IvggVI/PX4FlWrLcJioOZfa1fWDpvO3U8ZGCUNz/xlVlalWq7GeDWXbZoj90Uf+oAq2joEfHkKH9PW8HNurHYKg4er7ALJeXG3tQdXEGE9xuFIDI7iLQ8BCbtQV/AaIl8uLmShq8J7t69pERTqG1KNRv6pAvmeGhl6JV6MMNpKbl3Mxhe7YPLZ3h1hQZKXGNGAldvbnOldc4JDO4o3u2YilEJ2kFLF016LVU8UQi6T915fXa0dn+vHIJEM2CQUeC56fY2MOxeChqV9qMXjC7XbfZCXjcGB4fk1iM6s8k/f3VONEL8DTiI6FNYpbL7GVUo2yNy7DNfCeaamJm5o68/Giooo5qxLesuN2Sf4uIdmCfOwToMXudHkeelpEF0Et/uOZvJUSeEm+3gKGh+/dtusG3rQAnW1pzybOpyVcawCfpvkSuqUW/yPhLEyMcxXBOqV5ClpGUmzd2l8oC30691e3DROAQC9vOzSPX2KmQhNDJzaiIwjOOZ6w0fCSNM6c0gf7/atkw8oK7NDkucnNqCVkFvTd1qYMlOG699W1dJ+WMlDAHYqaOVFlXEE230maYEKFhuaeDtWri1DJulNiPj07mBr0u/l20UHEJA6s3XofoYEQfH9ZbWxJyjhaEnahyfqTqmXM9Ja8cQcdJzSZhVZ9wxdbyrOq3dXwwMYHRVfsJc3qEVjnOuFiHobhm4LbVFPTJX9gr838vOgtYaQLhHWTMAKvPE92LzWJCyg0ak/wd3tfIG61iSvTGGclyO0/5Z859Sd0MqLnBC2h0i7hDr14nkqtGb/RvAfP9EQ61qVacpRjPVClHJeRQAeQfSSXvLuVBwdr5rueSECE+lNe5puFXFiaVAhhAK1+aS5CJqB38H3AzmbM6ijSTFrGHzuVudZwuDammPdwGgI1t6KW6z9tAfIapS+9HcXXKZVVXJOu6WmWDAYsQPo4Su5Xnd7U16Q40WtyYcu7odHaqj2dPdoeYjGN5zHcjanJmqOyriwwCyZ/d0iNaCEnC21nSeF6qhabmJEEp443I1nB9DODl70+BN8focpDWI9gBXg8gu5rP3antOYke0VgUFn2mDlU5zbvaEi6O3Gri/mTL8krdBY4ZO3cIJc2Ar+iFbwYAUBS/HpObramRB3W5ZAZm8024C1e4b8XEFGaE7R/7fZFIQZjXgM747EZFJk2aNDLQBtD93GgBLrz+eIjBix0/GeSUuTH8BVnO/28y2IfRGIUcF5soOFuJ1Sus6WwVs0gwTwy6kgvVkNXVWaSCMpB+U8y1voA8FHTpEbt0dgEhgdCOzaXgx94w3ixVkhOicSqIY82AWcjreCJGfMONe6xVHyVpIFHfVqTra5tq4pjLvRT3YVcq8kXPejvFCteQ0cw3smyLzoXveZHoXKm9mbwJTmIUlNyZRLIMhFct7x+jps7UUCq95P6ZiWcZnQoDBdGel3wf0FYV2VKhum3eAz07uHj9sLcwO+o3ElzGLv+8iauBjeGM8ldiMhS7FeR4eMYslj+vGiEP0RoJYjpeLrOvGHGJiSA+zPdNPcwB2V9tcc5zdLkQnX765VfG5IX+w259zqpEeGDHXAnvYd6BJe9XXCPjf922iyv69HSD5sXaEL4o/Qnpj986ei1OCC9kraBYclD3cJAOFpaVqv1AiVJ+ESmPHeaiZY0tm6UO3vWI6zfvX0bxil8colWG1j1/FGTACdAl89YvzKCwKAEVRhgurPuUGyBqVrEUFow11nJ67TcbOwAuwtPgF0xtYawd+rm08iCsVnZ+1JnmR7GL2XaPx6AYbkLLR423DV6TFoDQj4drFt3oECjWhDrfcELIK009bY5Juci/7sSCpTykPF1jiyxexXY/XMGcv4i4zzn6d40uPAvRj/ClHenaqtu8AS7jKOGHozYfVxAN/NW6czEPdBRxgQLzwu1FvjShNSCZn35Lo5qT5P7cqk4LN7tsSFmx2uuBZ+oP080N+Ce3areUIAP8iL7p73F2gzr+/ExqNuPIh3HQdaNajF+Q7O+BlrSaO5L36QQSr9pH63C9XPeP4kPsVfTL7Cdr3iYbMw+S0RhPFkj6q8eMSeuZcdYOfywJu/jcPj6BXlxD9kkCqiI3bXZqdJoWsaGma2WZmYohXDQglII8UE/pS78C0/SRvRAUECE5nGHgP7byrvaCfjUVG0cmnTIgxVQt9wn11081FyJBUqYAEEvvK53jh2rySLB3KnnrNSByv+FxAGcg0onxm9jf0egl4QhcyvuYvUcccW51OnMRNx9ruH6ipxH8k4KTEl5EO/ZTr/x/DWEJaUiCiqa459CO4SPxjuz47bqICBy9Jpwf4FD3hDlT0UjY1tKZ3oaOg3qRBMuxD8jaaklisafR2qG0SuBarGzicazDLmGvgcW9apSW9pSaarqgYPJtbzj+d4C5PQIq8WzrtAT3DNstlmVBPX6aXglhuiQP9gue6j+QGEceoGzOkiM6tYatMYrjsckL8he56deYCSERidX16iP82hCAs0I/FfFyIFEhCBIZLttv2FgDdcH9XIdHQZ/jy695pMkNxMpcNmRbOiiR3DZ7cJbV7y1r1L5DG6Ndn6PmUppaiSfCoSz4DrQ8C9TvgW3Qjj/V8kMHfBpF5MjACdSQkGaN45xaR4qkTH9803GARyelcKYpMbrcNpWOjpJc9an2ASZvyfGXWqrFw0iv36l54ufEzTnml9CPJ+DeqZmn0KHBO4DJ7lv6M6zF5mZ4ZhqQNl5+YfzKZ5Saif3Uo06zGg0cWeuGIdXvMGxmvRidGY2Wdosa2pl3a7r0Yl+9Z2XXXRoVbM5znM6S2C46Z9NzJKd4cf+kGd7bapz10E8ftpKj/tNz/Id1si5+7q5HUV3HseoM6ud9qi7xMiyo9GFI60OzHf9NOD1kTwgKYZKYXIgoSsxMYYy7cm7sogQ+ati+UbAHHVTzAB721DnMxeVYsnvNElaCtApYKE1bwu6DzkmNhLJRxLKAUWXi7Hdr52q/Pu+MTdf7cLM10m+bzRtgvXpyChE4hiW6VXH50pyv5yYL0r6Uvc7yh80rQc1uqwbNPi38qDCQKOBzmg9QBFs+IbVDMGPud5tyrvFyHZtGgLwJT3tmNw64hqopCQSSzfltqy/qh63HP34y8lirEQtaJrRxjKzGVT58UACenWQT4EWzml52BrNRy4NlvPeEptz4bkH40XI/F3bxmuEAFuYQ1/Tp65f2wjQeUoxzXh414GGlBgQp0a2fLZL27EmLZoSx29Xizn4ODuFGL5/Z2wj8PqzDUe20lHp+aRf1KO76sMBhxBfBtf8a3QfHWDcTVLdON/LRab0YS7umajjTahFBHbBmvNSq4zf5hEpCm4AW/MKdAgMYRwxG22TU4vQFcms3ShMWR7EsPhBBmQA1zc3ieG7f0ZrdR1nGaBTjEEup8KfUpXaR8R+dPgBPOZCW6Km+kluOvZh0pCnJvsF8Q9k/P2wA88YnW/Pa3y1ZRDYpt5AFarSYFKY9CahHkNIZuJTbXCCY+ZXzu8rSIlqXFZrJ0EB85u3xji2IprXtjy6M+Wc0O4mz2wZBQCCOWRtZ8hf8iJ+4cjAL3HwyY1z0303sMScMObiGlimulTn33TqjT131/BDoYxQuoSklFn9vWb5lFgik6E8KXiYb+HY1zm35vztkdmuup4jibaatM95zdGvyyZKM7Cj05oLzT7h67ZBINyl0kWoxPmqFPmH+O5PTTRwhM4S6Znnka4g06xKaarRQ3pL2fZNUAOY274fXLpoCTuA3gru3Ce/R06xLVdLOHBII/tsyJztVuPaKRWjHqxkqTUyKTDQPb2dTLXAJjOFh8O89Ywtr+U5hi8Q2IwrpUOVyDaaosxDiY4RcAuaYWRuuidlGZzge1rekFe3wMhcgPzvd4+yivLFrPRzCdkuRcYCozog94onN+Enz1Wg/C90wDqgIqHLYDUcqWdmvgfTIs1CwQdPNxJCgmN3m3lZHz3UjZhxGs7CaSllvQvPecZdl3z3tS1DRskAiVIIHT29CObSa3b6k13MiFRVTJkRZOtbqY4vf+fSdLfQif+j/fKFmWZ2eiz0EwDi/tuYP9NciapIXvdScHe1ybXPF6HaEbBCiC6xj02xe7YBM9SuCgMl1Hw8lwCIOP6SBTCYM9WWcEqXDuDmCDQxifMfFXIqz2p0FaNuy9DnLyGbuGmp69kthZtHvglOG147I/5zL8K0njBZvZBf/NI9QKuX7nwVgeYB3D+YHygGec3LD9rICBLU9jY88jC4aSH0t0n8oaHaQryRqubOf+3mE9vWYE5Tt8QSudzTj9xEmMHi3G7vEqW66B7rZu2a+c5e9Hk/kkTettaol/uNymusLVDlRl3vC6ePm8c3tNpMaPcmmFRQGmtQalJNQcwwSKREjENj6AoTTJFTBuO0gjVJrg8QMiWB59PlSeQLtwEOks6vPDmEcsg4NXUD7vSMw+84ruR9kjBFzfBod52j9FCTF16+GixNDCADVUJjOLDbKayHkGzBgzsBlTpiJSOVDOOGFyrUfCDeUjxxJ0H2Lle8kp5euiVmTGa9L1KyM8MCa0PXgnS77GH3Rt/rfMNpO8+y74B6Ihyu7sOdEhOPoQrtf5sHce84ZZ9F7iVQm9Yi/iwiKsXecAAPiKX7AO55CxB9jKI6IjsaFDaAoSdP/RHmLR8kz4ESvdRHXsxISXkZ/Qzq2+MP5qZAyWFIzHiFc+JqOVbxvPJXfowtPcbSRA0cvdmE9zv0Wjed+Oj1LHdTPCm4EtaDqIhq/onEWcN/Ga4KidPqsi6WrQsyWTqP7tfh4Plw3/Uo/ECkpHgPng/Naklei2B358OkVhVaYiVh8r7PrfRdEJdJdsNw9xMeztVVazYWScvsYlsiGRdHFUqg3Kdj8NgPoljm23NDPY7rwccV7DydYTIPTzgqd0zoa04xrsDWim/DfWNpB2q5feefNoguNE55lXrk3WxfqP4QXKslweEmu4oixQqQPzvBmZTPxfyrsnXieiOR5aj4UH6hXhVB5kkJ0ogETxzg1wkyoeH6rkd7srWAc32Ogyt5oDfnjxC0K01oh4f5QWDNw81Vl+YC0F4XLOSSmAMPEGtteg+rQlUhkx4PfzH4mXdD25SGLw5CPdW4KIFyeFRE/TOX24O+zb411KZVTnbBkn5R9dRwJlUEMDxqBHW0oyomZclfUFsOd/6GbGt0yG9o+VI7VrZ6s56acOaNT6WFlhOtzKWX1MU8q3OKXi8dDt033dw0ovYKJhPuPmExnL9ilKn9E3e1trsVyEUWUxLizbezi4Tbi2ubwoZs/msQ+kUkPbNiGN59Za6+ijZKCsCoW5X6IBJlvMvdubW787KmPMT6d79U66CKY5HaCXzDTn17y3tQE8y3y634lS2jnc3A/DqJt+aEAbE9uAQ5o8HqGozpXOgzm4hiI3V+WHhjXFuvxxB2G5lGIFwZxdOzQ0EIBp9w5c4YmU7OoGfjG3FnkKWSZq9iviq6LkovwzPUJP674saPn0IsJRAz4s6AlHRQDlbxkARJahxesHveaxBidXAeyiqx/CRPv318ZM/GejoLQZg83wpwtphCaWK+sYfIKfRtHkL8mso0/7DD/TV/V6XEcwpzz3qaSc4kYTgOg90pIKhrtYLIGUWTLbu7Alk/GX9nacVCuIA0nT0r9e9M1pZTsO5Jyg2R0bFzvhCA5sJ6+2E43y7Sc8cxuLi8htYakftPB/CyO/lrN+gCgCVeTBHukIcGkh4wZtYZUBsykWaPDVos2v/scejLmA7O20jyzT0f8NYl3eWYrlImYIgo0bvJxLeEr+J6ZUioAwdLSpQwf4Fh+++D9DRta04ukJQIrrfil+3bKibAxWCQpFRRc7TZfpUJ02vzhnQgR9n8FyXwLXa7Kmq6KSFKUlQBKA7tzW3fpneIi38ddkFljxWfPwe1MqfrJ67cDk+CmOpTgbYlgsdIXqfP0kMWoKnQ7j0gL0RIiarRz3jwag5LpOaGUXCOeo6fA2r+WDxNBUXd4V2UQyV8AfR8qunzdgFZD9yRppAB+dqNnYXAeheZNO5nRFmbQGEOPCRCA5Y//SjZI2kiC0unpl8zZSEVIzcfL7jTh3OG6CkKtlK3/HCvOLKDGjktpCU3PF65Co7C8SmvrO4E5EFihEBT4ejB1VlqrhzD7dGgFfzcCEW8tQWMC57z5rlgiOiF8hobPCss3MkEwXf9y09k0VdAuIXhmwETl/B5fOHvpAn3oZxF1vYO3dmNeaQU4oqCbjsxC91ddYFByjKfX4q80ulWXUPYWnjhyLA67oTrb99HTx/Ulnx/tHmPVN3JPM1WeKCnESIHLvUhwpoc3I1ZkxUXh7Saqj67OI3+xHKhd1dVJH8MFFwOkw9iJ585temXT4W9bANUWiCz2dusS+yXCGP1mGoYc5OddRvQAIRP+mqDuGMrSn1GxatYy4SX3eG78JyJuv1aSJN4DDSczfHEACTKzs3G7BtQqFb33LhcGSGl1A4Hcac0M9eXO5/mHKkE8DSBtzGXq+hp3s8IJKNsxuWnRpvFJNJmXzNJ9hNYQ87u09elMdlSwl2jIKvLSGARQcUl5vz+mm0l38M83sPkHnZ3+p3M/kHD9EEfC+ZH+nGVfLcg6nU8PvywUJd0ZQ75uvcLG2BJ0KhdLqrQPv/Yx5snH0WrhQnn2pbvRHbaZ/36tZlpv+9usWY7IEXwS8H2LZE8FYruMLtus2c2zBTwBpyDIdz1G/gK5RBJaFd3BbHi4JgyOe8ROSBV4e62WK1tm7QJBW9vp3O29ZK6WVda8TBA03SzHXLHn6KniQq1Fn60/EXlbbLbJm7UsHB6gJNwXz/xIwLx1EwlPCJON7+KLKCHxcDU76DrCv0fSSPHfGw9QiFqVsAlJTSZSF3ohGXv8kb+Vl9SXFNxj0KJ10j7/lXgdGTd/0fj3NRi1pf4bWtL5u7LVoo8QNmiVGCpRr0d5XadCyqUoQgnudRUNf6GVhWH4MmF6+vG2Gm8RfYWKAySAXMH4OzJooxUdWVXf2gVyEFO2efpj5sYr1djSwiZX93odY4bUZnXj2iSMYjrszRwmagiHzkTR9zmS+AuhB97skCSTAsbbF3eI9ke16o4B1U7hEWboKYoeUtAgsXufvUX+huayuTTw0pOLKA8FgWPRoTtmREyzTCRb4plCd7JKUrfmH8AndtGcQL0gXwyFygRMrS5yapkatiYkwk2IiwUHHvrmoMOvPkWv2waZvYKEeTKo7m94meUBOORIFZkI3rO5CJ4ZqKpgcJvQZwiWtT/6ke+GWSP1n8VzaIq/o+/gJhK3zoU+MituWy9JwKJiZ5l3Z/eQJQ3ZWzi1+lzxHahL5kdo33HuqAydMAnIeB2W7arUcJg6mDIPIapirEOHlii2pq8o0XFVlgqBysdI+o7TBIG3caCqHvHpwrmlOwhYiq+iQiF0e+s09ssuy4lwfJkADsTY1O9H9/ZEe8zHFfp9yuMTZXTVIr6SyDVjxtcNYz2NuJOpSo3PkSh1CrLF1Y1q8tnwuhc2c0UUhzpSM2A387PQkz6Qyl7mVNgY3u3q0afXVTtyv+8w7dTqL9PWp69QLFn0Jgb/hp0SBlUHcJB4x9+5jqx7kk63xnEfJoAU9kQ0WEjpy+ub6aDR8wB6y2MtZBVtS/eIPNU88Ulhh1CPrRPTSmVDbIrs4y9pKfGIMxzBuHumdpr8vDNU7lQV0FobHmb410jFc13zu/IRM6sy6cvVLCDJ14lM8IG0pkjwl4y4kIzcUDjRaNdUfS+MySLk+xXomy6twUU5qO0IYRuEiH8SGgYf6qjVI4mrtINY9lg8A8bfG0CZrtvUkVVOwsMs2pv9IIWbc+KsK8/xjjynTIa37/6IuXee3OQVaDCkGMlZltPraaaRIPWynp86SSQcYCMetrclYZHZ5D1s+Mmlx6hlV7uYVXQksHsv7zmAVh+wQiuFM0An7H97IcC4ZwztSEzV6jjfSNDiP60YTJ7o8kTYsfNgZgsZKVwCKsm9zdrvTaScZNVEt2hNVJvDW9ZExx8i2vVsONv65tXZIEM6YQzmkOLJoyMQxok2k2F9Hpog2bQBK18l8cmyEs5vaCSLqYSegLUS9YHo3nP8y2QgTfPJ7RqM3EvEFXmx8bSIyQUk4JiXEyXX5x2/4RMIW3+vSz7qXtGvQKfePqTW8w6JPeIxfsmy/UQsBosRjGYNky+SjuUMR96KmwLsGp4eum0lC07gLLjpX3kUp+T9ZrkcN5uECbFvaP3EwjDGTi2Ci2F47zEpQHruVuEvA7lbWHolvYTdCjfGDGzipQVpwPvDMf4QkJ5nZr36ow46ArmxdxNmJsxvh4tmNVAjylFNbwRAfjNzUEGGqVyZuZmie5OX88Ktpovl+O/Y9KB/AR650JMy/c2Y5rAjjkPXIbk6jy7RUitBsiEog9LYS9d8Z28e5DrwK+l3GIMGV9Kp9HzzVF4pCoVhLPpAzICgqkz3ge+8kc77FcCPnxW8RG9nGekeLBsQrUaco3OeH5jkYREfSX1qAM73+M7IHAxAts+t7gldZdtWaVGWAOWvwC/YhqWMbixXOewEReeNHzTQ6gMESKtde9poBy4b6PeG7fAccoNZ3AzGlHSc4h7aDqsmaiYoPhx8/xVUehYbbamHSVWP+wH/roFB2bTTRiP45ogFA6uJKpyS+ITudYukoNLJlVD9taPqHJgoWSM58d/UTwe7TEsWw7CUtXv1pL+KCyACyXBmOSqZwiwcREFuhqZgtRilGPzG0UTFvpngqKZWEqgifbX3YBrZPZ7OrxxWgLRR1dWfEBQZ26HA8wNXHvy3MR8OZIy5fRr89FPunaokW7dr6VLgC6LEbdnK4uc8CSexG6WnYMWzKZu7Z16xzT1Pa2Uk4sCtlnSeoDn2N9yhcmdosd+0RtQKgD8aszPC7XE9GO4y3iylkdTVeRO9lt7yD25HYfioH5I+dJ/6ZGqQd0CMZSD5mXe8jpNNxGJukVyyVjUw0EdXJO98wzOBkdW4OHlnlmAR3f6RF3Z7H3MkpycRyoHTpvWOjYnQbvZb02K9ek/7f8omo2odec12vMU+7qcl9uLJznLMVRF2xUqSPHxmKqRUujpra7t5qDUgpumBHzKMtegZ8CoImnmiCYU7fmhyUkKsuxr1faMIgSP/sMQmRHIwIB7tvrtkX3RVn+qAY2pETiRlmiGbaZ4F6eHndI7BKaqlniNREv9nEPFycZUewxvM0oKQmK2MrTzKDoFZaF8V1OAgG4j8eVK3eTdZBUYiL5ss3nkdEzih7o14JoNjKZFVUWMDvYpoE1NLHTE+t96GU3L9YqpCaQxmepLkwWx9mt5uGKlVpBxB4OfeqpN5KwifjP46FwYPLbuZ2xt/OnwY1zDqxB4tW6bN67xmHjer5ZQIrF1cIlSP0BF4hiYpgXs+IYdFykRBmI/GRPVxmVb9oBBCFG86uR6Jukb+zcbqI0Lov+jhUzbFTH0gVHiyvhexQlynlHaLDhzqh+oBvo1bpjPhNPPRoQsQrfxi3kAzKNCUWS5gHB+b6i5eGmFrtK0wyYPFjHR4K8DxQdlo+cfMttX9wxwkuT2VwUTbg88cihS0rSWl+S47T72GeSgmQ0k6d2NDOzohNO8cLaTnk5WT+V5kNa56USPoeF4kK5bl1oohKSui8HFQl0gNSVCeVW9ceXFqxcKqrY+1d9zMkXMsNuEf9SPddlsSxKYIKtF0TG9OzH8vlLlhxIy7kvXIMOt073tCgTd/6tazpS6eEPoh1Kks42ZEV0ThsFULG8Uc0vZozkCFzuulQzqZpxYpjHuWxArWSQw++g9PY2GPq+CCrXdDJCcw0dsSGaFHOESCigWXpb4bG2rrIV5wGY/T6cSOwH5LWYWpomPYtmsz9AA3aJiPCnwhXzcNiM5GIxOjJGiDBURn/CF+oiwuJHK/7/yEJfI1GMxq4bP6FrGulRkXvhY6Oau35Ueez9KHBCl3wzbDJx8J4NyMNlc0YcWepSEw0iVO04H3j/ySYBrtxihMLn02ILesyiapaRQCD3mILS7WMWY4lr5O2dEeMbkmUpInOT6wEwPQn3My9oZqPJFJOPclw3PNAjV9ujg0EQe0jnZcxrDFwcKeeXOCavdr5Lx/9r09uBO1IP4m+PNp+fMA8Ebs+N8BQW9MC5cOoqHHg1ujZ4lv85o3Qhk1ZyFFM2ke7QurRn0lhuN69MZTrtTcVHtLYIpysyfv2KbWWQt9tM/kFne/VGiaTcUXk/3kj1PeMX3HsUJIoJDwCqo8uXgIhVmU2Qip1yiwPRY+rH/loQAPAJHRJc2nO/uk6icjndEo+xmPvsJncdDjsgToSE/TpliLvv7Qc2zHCFNLaHAHx4yOOdAIwK3XTgWDXQHWL8UCKlT9W4b6o/kynoiFB1Bngx3FzKNYz6xdqgAA7V/9OgP5e83ohhdurKY5L4wkojTiB68YmydUAjr5qXqqP2tUeih/gP7iEMWNJIbKE3iW5WNps9LJyNUaUTUn4YSKCGo2Tn8pfC0kGFJ/LgiLRmjbGMRuFTripD+705CRmNLZXl/zb434N1/Ov9DUn8ENd8eGw7oXAdY5Wh2NlzEw5KLayyy5+/bwtu47xXqWLCl8MJLJwnv1NsyK1+ajfGyyqVlEM0Vl+Ky8WV1yIIOI/jOsaS3rcQAPZHi6DInFqWKF3B17QfWHLVeKiGmBvZXboZ76PXx0n2ryNXZfFXYMzUhin5liYsR9/85Fxmi0LgGE3JeqDmfFKdD5UjHjbW4ardoj0Qau00JYJTqa+AZN777tjIkMtboMt/lp3+XwsTNHgFVmIE2uEpK5VM+C7zUi833OQRtRU3Vx750SNAno2vHAzBCoUIXirZwXEgQJYFwWpKuD3LyLMe6S7JlXx+eKmbN4oBOoFfhLwebahXRtBX6ecBbng6EAB8dDYjT/ZUPc3ObgD20QnCZAJqQ8c+NJiqq1nKW6rBvIM8jny0wpjHMUR2ZYUbvHOw9WZqV1qYqxA6Ew1MVbZosgdHBJvcn0jePCnUUEWrK6iw9qmoA5zemKhtdhMiStjTy4CQC83T6Q8n7z4VRb/LoyjH1C3XSEBKfLdH9eWGcFuiMl9pzHDltmAhDF9S6IRGe2eIK68H7wjQ9sW7r+5smw9hSmDhAcHljVHOH0VGM7s+YqNF18vL/KWqV5mA6GiO6n3AGSr+RiA4tt53JCtivt2PAW4LO3RxAuGwFRdJcrc+9cmSPMKJXcfOXtAr24tiK4t0MnpIVtTM+A9Jwi93G5/QS7HIl4ywm+pNQrxDazqqnCJelg95WbGHVThHRIV3aU2mfE3v11oN11N5fOpntieA3d/9esxNV3Cj9fwJVoygFzv1+agmD6VzEoO+qKouI7HrwoS6GgbxeZLHeOj5vnwlniMcWb/j6zBxPvl0OOu7sRjTRIwCKViFA1vooOKK8t+cEbC0dSQldxyaVqCUIdhcu6j+9OAlkCHANgLz2sEk6azUHppzmnqKPIkrRuSPtPxLGgIO4tGej7XfSqSzT3sUdPrkeqf0zjwo6NsHZkvZV0H5Wxp09m46oZdtSoTsnSZpbmNO4s7WLMcILnmgvi46L0y49ieRznzJWVJ/nTw8uXDuVVOVNgP8eLn6TTVqj9AOZ+7CO7d/uP6jPdfK1XQhUjV99simH85nULSF7mmB3dZV1qRjybcF0EDGBgHy0aeLvFOUQWy3OTHHFsGMQd9GmvEZ60KkjbXCDpgkzvcCzCeeVzxixRNYDOJDzGK3Za1Z/NpTy11+AQIax+AQAYACAcR5Hn8wvQHI0lq+ygkPG12Z31KkWb4Rm6i/r9zWV7+bkf5ECsi5LS4Lx/1s2tLs11xKVE96k/AGvdQqwhgbuAyZHI7T7JQC7KuqIWHMEUndj9PM7EgAH48EQpTE7mKfxPg+UCwzvc/wDGmHoJ1zgkHdW/WnBZn9t1I/ILUhPFOc0heyHBXSCQDL1MDeLzeJrP88ry2L0Q2bWqdE+iwLm6J0jAPgd4cJuJE1u7DF8koNK1wTeMxx0aGFjd3KcYxZ3+/1CuusIqiDwbnlQNNmGeDHd8A9dRgit3Y5wMCt0C/O06UkEdkM4YdiJKuIlKXDSFT1IqTp9ZmB/ZkAbWGvvqIjusTkgZ65+Ghk0GOU6lzpgmgKEQrsoUn/xk9OimbtMN2t99SOSnrlSxAkzzXOe6r+rZPLOy2ozha497lyafiP/2HLgyZSMZdoPqPZPyLbAoN1cSaw+CLPfNSYpZCP4+NNTVSwcuksuXpD3KXj+j3IAEijcmOzbU6phxKm4+wx2ITfvMKB3h5KDDrbM8OxuWgm9lo1cBy4mH1nlKzjVZLt0klJf6Y2IaiEr4R7M1VGFTxauti0+jU645XcSxRavWTXyifPGGU9vjIMXqlC8nl0UFCSU5aqp31hn038zqnfcAsqMuswF4w+T7ZeJ1ZwsB55IQoIhmZV1o9RMeUxNrud55M0SYQXbboNYImFVutPZvPisUrjmvhgFhTgOJ2/+/6mVqsTnNdVg4RYIzoMUmrqsSSfA8BohbKSSSQfc8EiuupdUjjJH9KftW0Q60T0RdAKMNPObYkprSf1aOs4aDmmj3yiUrOmIPESfRwR7clExK7qkb4jhAHyzhkg/HfBhfYg5SNjzutAF3LIfypguW5ccAF8mojmmKTIgmuim4awamjJFbrjrERzWJbZUK1oOg5mpgLeiUqdehsVqvOeW4KUMU6vJWGJIkz4etZ+smTQX7djR6QVn+UHolqRla7pNodf3xxmLrBMO1zTvTHTTDAOiFco3DsVsaoy9c+bO6TTZSPgO4eZhqIfbcJd+Cq95VCb2e8URxu1ccXdLjeNSyW4IysCZwowE0X1CJSCKKbgdoyh56ArDVNu9XS+Ove6/vkBhRibMauQbom8nKIdI8/R635V+K+20QTd4ePpPo12ACSkISwST2jzuhkv1x/CA4I3gKh0IstmUtyGqzia3yLyDBP+ey595Ma14HhmuvwrIMmdQnuSsJv6hXAmHYop6DbIgLSxZZ9EyyBLjjVhb7mQkIWp5QU2BHl3prz/I5Ev5Qeq6gjWXJ8Zwm4SnJffZ6YPOEPXKWjGuH5hPLhugwwpazZDdlJVooMR/bPYW4KRYHXN1KoH7POQ8jpbyrDCGGoMygqczBiLePMm2P/o03JJXF/FB/LhjkomGGn+7cAbU4VHE2M+OU3wWzB90+yqHd2onoI5joSUEvxsi4kkKvx260OZROW0OLWDFAKEq+j5KEbnCICfdMXDQSDEhPAC6bn2FL+dJYZF/88N2660wyDKShY5rZbwjf3sefiJPdgeUICnDjTFObCjjMXRqcEc9tzH2LsJwdKSqpI3miiUXyBsJkQtuQK/kY/xIgWK5cMcrX/kBsA5H0kZvBrCyjAwqV3FiaQzKN2uN+hcQT+5OTZwCch5yKo5KXtXHOaGZ7L/1W9aBPYAXus2FnfY0xE2oxJ4586qC9Ej0vt4jfZQ34ZCdPWFm1RaRiJqi618KLLQIcQEHp5u/2lvkyXJiIqf9mm4+CyE2oa8wpxShpZvzbg/3vrcSjne/tG3E5NsBkZUhwYNV7/meoo6vBIHUZpI6AwBsJ48zQ8QHtUkQEkXRkQre7t6OYcJMQuKlBgqK60T7+eZiuqzWRYTAe7jzIoyNSOOhjCLwwFujLv64xufhHbGlJNMLBStbHc0Vl7dfFWGrT1ITEq8KBymkjvIcDWfjcYo1KKeUiHuZL1TYSAW36Ismrpn8icjUyKql8eUUCfukd3riIGjWInKamIUyi6rHC2RiCklSttP6V/L58ClKaxEMm5u+UQcUGVxjPAJckv0m1x5O6ppfs6ZajcLGsO/VwFvcZ9AxeBgq7NiGjUe0teXHwEecFkFDHxYwnjbnxVyWqAVE68JBIUFmA2oDVuJKoAq6i1s24uoIIa2MlAsl25XgzIqkmSaczZBWVbdTShehRFCMeoTdDhJx3GeHe/+ismsO/lzBXuDQmY6lb1RrjznFbz6dZqMHiRJb448C1ulue6ZihkAbxXUuy6UE8di0eDZUjLLTmvxvdcAjJ9iWPyU7QKAD1z3WPqGoqLYEkycBQbZ4vd+TGN0B8Hvy5BrxtlaCrG3pYOUMt908ZICmVuKUUUdgniDYsob8b6Y9Q45ubThIqz6OovcRQSUsCg4l3NvVq+zmZhp7ZA5xaYBMG4chyb/Thr5NIRF3ZSrhltaIQalsEzGT6z50vPcV6MVsGDRESSA3Gv05H2mq5E55o8X4Dt703bKYE5aGFbDzYOBhRW6xZZd38EaKcqYe+0NMyt/v6m+QswesD41+qGxFMbIC6YozQz9WKCFV+L4MkAX5qHhS11fQMdHi5pEO6QV6umvjgkKXOKTG4mqOUFH0snUsXpjxQ0oODL4oURgaHk870rWMvh+itgDRqHvL3Bzb765ZOMS6y0f9MqZtf6XoVi38gTqrvGuYK9fZ+qG0cssoC6Z+g1uV4DiGmkwW6wbEYzgOQFkkWWtzk22LHiysKJ5mxoOk2lWb8vcSSXrNWP3B24nij0v1fuKNyhAnBEK9K9W14JsSourut2zNsq4CPjw9NLD2ByiHENjZAPSsboelsVglJ3yxzdKTKIGSxnWiuk3fR+l7o2qw+RE8MyPvxRr2r63161HDvYZL3fYyY4Z3PYrOQYM1/sqZUDqs+/tbYnrenXxmMBgz1ZGMMA7WHrTENAzdXpESMDvSjfgCZ95xsc2uqrxr8KrO+g9ECe93ZPDi+SKLBhsqj5sCtdFNGe22A/USsQhg6QbiKzVUdf+T15XvjMpI83YRa4XqdtCbBc3rMSl+M8BKYLNbLp0FzE6fG+Xp2qii21QNXht09puuyYZQVWfjXPjMhasFfIWA5t+bXVPNenRHGipGyUi2eR/oeWIYbvYIOLqSVqtgX+Xw3BfVeWYlmKcyULzTx9/suP2PTiyTb/BP1j199/wIjeyZbCaBY4jWBFPq8LKrHQKFqnMh4br4kP1hBzdo2BotdWwUxOAg8SX/p1XGTeB8lKF60qT3ZMC+eZS4PKmLFFjep3PF9Gxwllm92nJIr+CvikP7NFE9+YECUdo54/xp+vrq/6+pTzzoJjksSmM6ffITVbkly5svmdsNu5hOgTB2I4DKQCi6rF164IvFrSaklnxHW8p+3bJJiJvzmmx+/9YRoJt6HHRrYY4Xt+2DbHn4AXIRTWmJqkU9673Mb6wa1josrV+zJ5jmEF30/gw6CFDBb+R+OhaI+bI0wfv9VrHOmzln2vb2wdBHOVaV8DM/KPSndum3lK71qO6TORmoCQQDmVBkcGyfll2tWLmNNy5v3DhBcVVhmELYKa8ffI/zeSi2aBGTqSc7wStRAOpwATbdKL8aQt6xMsPi/esenaWWYA5mmWS+CJVWHbrEV1YfKeVk5vbv4A2xQZ8hl5EDwI9yiUDdDx4/IszU/oIjHPbIRQ+eASpf1shQZznuoYwfP0JgejNmP8BXt8vEC8Cu60SzRwjs1NpEo9tzB+67SxGu90P7l72sd+bJ0MenKsk5k5hOr9ejmUVODdQnmElytWTNcrZdRAjwl0plU68C7uzMltoLosh3buKjlQGTepHgHTj7GPoASWwG4RszgkC2nz8fiNNA5+OSPpXVUKktBX6IzrXPh+93SguhYca+NIdbrlWAQgbsQmsiXGdX5vfG13WYTc044NE3iJz2wRV9Qv3FWZ7y6NtwVwKUyI+p0mlYge5CWIMfvlbTvVTQU8AeeI6azcrq3IromCITB/lN1PPQb0ax+uneNXmJ0g/rIFRZqge3kNR+PtOep4XNjPx7/x4TOVPVYNA0cPVq9hQTXi6CELuo97dS+fwt/NjghV838d6YnUuaPuzBMvp20T1aDGswA4Ofd55FhN5D+V4sQjNU0uCqdYQ2Pne8PdEG5kj0wPH5bGHQh2Ok2ANGQ5dBn/cFWCGouqlgsNhUqbHEzGDDH9rMg0TQeqKa46W/tRCXHq/VeYvjVzQGN9WVXxFxZbuS5y0S3YQNvmV+sLnFo+7Ix7D+NP+29GX97tGFP0Tk7bU1s7VtcE0fzqHgIcLbhxEokeIcaEqWZGUeCDQUyPd2QTwPvWOcRmRCpKaLoTRghFlsqOVIj91vrP/61IsV5pkdER0iW7k9AGmwwHiaFcE/SRBIPAusffiA7zq/TuZr17Pk1Ggdqk+YVtkYX90k5mp4MNmRyUS/kF/7vppaPBxPDe12b1rvQ4rXtnNikjKocE6tIbUalTj25yzEFmmwmD/n3dWHbRwOMktdfQyV++7s0DD7rB3sK1TmrUIyMk3ASH9C8CqirunLKB4tKGDub+/TNq9uVlT8W70nz5mHGqBt2YW34IAODlXVgdgq/yyWcOAamhFYwlHpBe8g7lp+TWa3OAaWwPcVcJtW5Hh6C6Hmww6T1cq0A8hZTna+M5qE+4XAMdECcILqtnlZSN6FomEj53Ne1G2f2E9YIe/ME0edaxBIavpqvIaYqUgoIl0gGoRyu/PKjXCUtBf6oivKLsOofKMwXphLmR1YMsbjBS123Tt6gqX6FLxzdv8WO3eoll5CRf41nCflzmIqBRpkaXkc1AqmEPRCERe9W2TebDsGbr3uS7qRq9orHwWxjO/Xo4yE0dCLj09inQ98ZNx/LjHDSp12AnviZ5+gEH5dQJ5wLKhY9nqlp/bpt639R4J3k6Alt7QCljxyLoByb3o84xmF/wPraLtzg/+RrsoeL77P4dENccArpKs2a7t5lJnFJENZcr6sZNZ89rDijj/vqJ0nOXVDtfkH0O45QVMLZorQAwyUCAxIUXyEQROwAKoByQGd25RJPPbkgxnhdEDBWGUdU3XHxp9ALXSFAkExrtenJkYy44vWf76+TWRs9BPtBdrJd8ceW6cRJGIltmKcNzpcc6njVhHn7s6ZIPeOTvk09rSQSAaQtzW4kYSzhJFP37QUUPEMhIwshuDNkVLZjKNpKkfaQV/RsMwGyrbM83hTiNjsMirbNl0CnYixl/yXcRD6SDpaCLwwfP2LqVwJ7HEZI5Y6turr6vO7ij9CexpIZM73g4r72StiwWVIIpK+BK6G/88Cp5wyUZ1vgrf6Wyia5lHTTymthKx23P2zfBqPv35RAzr7d8KMByfc79GYAhB9eE8d49Gx93hCx1JnEmaygfz+qJs53EexhAQiuiCDhwOiNqaPC7uqAXxs56N+Mgz7Vr/rfEAuYnHHdXZIX6yyWbRzKwo+0tzOc9N+kYwZ3Z0S+6nqsqw9XBl+tPRckdeuiLvlXo+A0Elv+2mIMIvbn/fM43XJzpjj9sIns2GTKYW4Lf1LrxCWxjsl4ilWXMSYs7ZLD+0T5ZQaFVgWlaJf+r/Ul15lmxi21WSnAn01EmwOsn44KuELeOeMi2NHVW/helgfpS6qL8RiIGLCnXTsq7uhShBZaem255qEGQejwtxICrhbPu3NKDQgBHi7eSfs64ZFYV6oz00HfcAARBYo1svINzDECkIh0CeONbu9hbbN/9LfECHecY0OnDgzefGdVBZ/eBuEMmd4s4VSVIJOf3Gy3ujQyuJjeAhqmxWAHqfuPXdDvbFtwSUK/eWOGkCk0Jv/nU+p38crPUpsKAoCIsmis4lrkkA/Vqp9RhD13zht1OT83zPzyTydGXzuXt+Fv1wZ075qb85r4/fxliN/YW++AXOhlq/FyQfTDZQUeM5dKXDSChrC54EI7ZAwqKWHCQ0fiNre/2fr1VwLpacGXjWvBfx1Br1VBda3vUDRq32XjLhDBZ63lzQhL3ZGjZtKCZLLi5zUu8XncIWu4x3b4S/kh+9+t4qR6LTlfPp078fJiABdjPLt9P+nF4Y/tVx+yn5Pg3VeQ095Iffdi6cz5rGarvFkojbHQaAaL82shrYc5x/uKVrV/2klE0C2Dtx81cWggt9j3iMDNg7VywhyF5uoD+Gw8ZAlrMPHTuQf3vZgKsBNm5Q6SKgfp5QGwwe3XvI19wQ7FzLKQ9ZS0W+gmb/Fwmeb4mhuok3Uvezd+ikkQKF0OoHOyq+PslSeBI9MHpWwDv7Ki/fi14PB0KxRA0ath4ZSrlTAz/pgHH5yw7rFng+zS2S1Q1QSG7eN2p+vBHpIgjTL+up4ACcgB65ii4tjB7V9Xx1THGXafOGLqVs7gMPb8OD//+aKJwkiVYjrM4S/Pt+nRNDDy6luFxqVLYnA0u2IMm+l9xifHj4YztXecR+mKpeGJpFJr5dZFVgQgQjheQDy5XMrknvUgVGEoPnIJIeUyZ1Ckwn2OudycN6v0efbp6bc7wUokeVPmch8OIFAuizT/WB1QzIktGQ43+jGmoLdWb6J3328PK0TMNG7xd4+6DQRiXFRZ88hdXbTmvbDuzarJrjy+A+PCbYij1inn4qLnoV4zmVAAdZO/CZtwDBmcaVdIWeWhy9Mzgr1aW31ZJklrQGPRjhW7ve07aXOg5K4t0edKPIJf/ZLqZ4Y9sBuxllXbeKnpMxNZT9owGpFGygi3+JaLLA2hNa/uJT0P+2rheT6d//u3iouFbc4F29OrT3PtGQIoPArk2qn5ZHZsZ6QuqPW6szE00Tjfgxe1GrMKDDeBHQZKlGIxM39+yXSNr4Y3TwleMdk/o8ul6sZKl1WghVtvE+O/dK961MIx2wIccav8yNLr6+ShKPGCRxPAK6HfxrKHgczqVg7hKJJ+9VWsRhcn5qApYvj5/9zQZ2TuwaO69iiegjrdvA460OjGZGVRulcBNYpE+0w2vAdIOp3cFg13cTed1pV2yTQG3KdOsvH4fT9eAQ4d85h8wF003Fdh6CBYGh/E4ZTPrEZL6jYDlXLT+GDZNDWY9WhSEzGEUnJFue5KVvzbXy7UOFbhG7iovqzFzUx9hR5CQXJ4tK99BMncU1dJDYL82himOaZRwWrmx6hztfY1GzdESbv39TbW4wLO3LDAo/V7ya0/QDunfLO2C4I4hzSNrNNhfmHPm7IvHk5UWzVbZc+cpTXT3nPP4oQ4sPDbZJeaA9ci6iKJU80n/3bIi5fCnqjWs71ZX1kUfotkC6pw60q6RnZ/DAHX34nNLaGLeTv/xZ/o2mxFyT837eyFZvH9laYoBjYnyTWWH81CEsBhFiA0w02JUhDDrmiHBBf8GMkZHlk6JVpOdwaOecqYj5PEbDraPIngEbKIP0Nx5kgodWJW3CMCKhfVhSeti+VTgFzWT3CLNeR3gRL9bpBaiGDT4a4E9gSrbEBpTYnQmF3Wx2wzfGI46xDJdjYFTgUld/cU7RGAFVuC2d0mPKqSIZ7bSYKo2xVG2Af9rwx+ozvrAbWxUvTNBkGvRtx3UTybsaJyc2LmjFfNNx+FAltYsGL2SSmqA4ENihdOOm9rFOCbOuAkKk4jIJvDsxA3RhmSmP79bAffP287uObOr3V5hbv73DDuP7+z+/ibLNr4oqQgGIl2nyV2weoBH97DJnw7VrBo1cM0KsvBpxlUJhl8wqERpPLrAiWub84Ou1cGHFagw+iGXkmbLS/WF6m9SDejV4lQ72LJU3gUr2U8PmTkus9vhv9I/1kDVye+FwOan0aqvx5V0m460IJ/pU87bZsR2xdCi16cpOxuglzTP6vCRNS9OYuGy1gtLwxKcv/C2OR2+OPvTeJjDcS9WIxhaDsLkCOEsLyhe9UoUb5p3hyCMXkRgv4miL902JyvxArZaXqetvhNoe4g0HMC1Q/naNJQ9FF2OGwDYKoZlRmPglY7Vyb5BGEtYA+5Eg1FzpGyEfuHo9QcwnvNKuAxv9PZ/j0I5vy31++sp3u3Dij1z1sg3R/cmQMiyW3RreOALcj3+Cl0+6JxbL2kXToDXAL1FuCcc3VAzzgsq12hosV2MAlxd2xTklEx+SJo3SO2Lm/fGxc1aio9jCjDxF2b6W0mOysjlhlaADY8RDJB+SCEMGqR8TgiPl7ae+FeJnU9d1XB/NeB/XUba6ymfnC3IPRrwCz3mSHsmjcOWixAAUttKSY6k6gdLmxtTRn0yFLF2ckmZjh0IsryH1VYmlb97XE9IlVfeAITCLKrM/ykm6IA1BqnHGRXES5HbJ2SEexZKvvFvsqjITecAHhzi6M6SgCc6nZ/iV62i+//l/ZXjbdcD16h95+Hl5uxAunpDPwbO3L7yV2HrAVUuj5XlWEiBCxQephjsVvQThyKzz1qUJvshJD6cG4CEOadEr2NkEA3W9e6wGpzbFhPTAYEGB0HSs779bgutO8scP45mcgVTE+xliBFgtGE26s0ifdZCEtc5WAUXotPdjQc6Dfx1BFpyLw7VqzhnyrLo/iQqK/ymO6+TPPVfvmHdg5oAiNoi8HEcbqe7l/JwOyE9kZSJIc1Z8nFA2Tff5G5xaF0jPN5j7PmkJtjzB21AW4DFdS8dFpCjxfRO768gtnvvGLnyfSyP8UOZD+zzBCLM8oyGgfzayqTOXOkvw1GJHe04aYPnlLs2dMEz6tExLwTi8QXS0CdHyt6XVZ5se0YjWchB8bAGNVj6s+szKmw/hl4btBHEMZTznUkbP6zPPbNO1qMj6eqFyZ+qczrc31ry6oy6MN/q+Gvfogrtnjk/+zGMXqmKy3Rp/FZVZz51I/WttCtQkqtxw6QAQarRPSaq2fubLWbZPo8VgOD6eZHcf5JcAdglcIwqXTMNv8c7ExTFCYj8xTmjrs1kfddYbeusWZL7dAUlJGIBk6wdiekPVsIcdCerZvx7HZhcScOlURI+UWO4718WQyzLyWfWkeVkhHaQ8Gh7cGv9uCQ0+7obl8Yxy/mm1u8o7KEQtwUmtkXGRfN8CuHb542jOZt1ly9cBSE7ji2jgzqkQFkOURO+Nd0TOyXN3N/nOVlahzsXON3IQ7rSrukGNPJ9aS1cfuinwKysIkvv0s43B2lUI9KZcyITLwxsE6wzXuesIS3Tn0NOqZfmB48caQtUfCE+Nww79vtA+SIyPNl9RZMGExclnfhnMuXZPBiVRLxtQG7i531j8jReHKlqHyuiO/QzC11T0DQCSDDBqXvvfCJMGnJ09cNVeID7hRJ3WKgbUVoRs/hZ+gvEO2uyE/JbYbvbZt7TwTqPXfUUdDtvPNJzu/X3zxoX2v65fdAY1n44aQbn6sbuvd/nlDZzVvSRqdXehjbB+DA5025zeEcx/YK8NoXGWqkIr8lfjNgo639Y9NDXWORcJHsW8QEMky2cCD2zufs4nd+vJY6tk0xRYQ6EUL0OkAVLAwKKM1aJiFGYEmrUm81z/mNWphDEbqZj8O7KKetjFx4t2ZDh1/5jonSijo/9L2SPLs9C2h1OoHQBXmugW2fiBBSYTZ8n/kqMjTW07Qrg/W083Reb1+2EGF5/ZzCEvJhttKMww/VzGMzFaKhPg5Bf551kN6nP0JXB2yNTugLteg4zAESYV1xOXqC0vXM+CEVmUUCBylM+2DF1VYY4sYzs3lvsDjthIl6BxGtud3knO+fdG5VSe6EOhSvPhg+ORUVH75j488csvaggkffxTltfXqK09q6aRwYqkYp+D9NQqg5LytT1i0B9sjlMgtkx27K2PNhyhsqYMGbj82o81jQDLTjLv8ac8dRsAInSiT7v2wMlch7NzvQ601Dyz0QQEhV1azwoSMr9wENX1HPuhJ8rgnbqbpbq8ybDYecRXXSKMWQP0G7dD22ALWXctd9+Q0gsuV7STs09UE2/Q7GuftqC5emzOQ5GaIoqi+2Iez3ypG08UY/JIr6ZBtwqt0AMkINv0c/B1fnIBZx06KbbaCO2sSB08v7mBLNF6v4xwcROZ+MNoj28WhiHrYxk2mB7luEcD585w5/RFgoNhun02LLV0pUtwXTuEX41Tk13GhkHDM+9Ytnlhc1x+6WlZPL7JPWwEfGMy5k3/Ss0cGzxhEp+RZ2FIYCTXCDPbqMqmAd6iqtt1yxwZn8//jZQRLCxvI58ug2tYB5mRg1NpGWpNs0cvZQHJ4MazTg86ti/t7+QibS5NiXCj9Ei9Ct4IY1Ll9KV1ph1Or2GnHmtu84jAWzWWXz1IL+6t2RR7u6tRE3ydGfRdtT4CikAzCw9NRZOlF9Yd1yNMw7589dV7b8GUahVm/CzWhHqDZ8QWMLi3dFS5SjVQVXRoOTuiimRodDQw5r7A9zin7h9CDhrLE256rgGadT9oROL37PkXRX5oTXhQboDru+0bqnlAtHkSReVLrLMgP4536YRFzLPzDqVkF8eZ5W379iWqFhZ3DgkCNrzJybyLBG873o69VxY4aa0061A9FPpI2jVB0RWkr21cACDf4s8DawOqF4QtzFoxQl/ZWGeyLVkJ/8c185hegk8OUHcIJxvdxVbsKalldDVPahuggqy6surdHtDg7yzvj33fut+1Nd1aIC8SJqiK/Gbao58Sy5PXiCxT36EQknvUOjox7LY9qIjsyAKAZaNspCB53joG5nNgHIiBQq3T1g2pd1xmkE3bY8YrjKk+K+qla6fWKEtZeWcpR0S7ZgAWriKh9fVLwK2+1facSypUwXvQPTR29irFvjvaAmX9au4RCsP+hV+jbMYpm7QE3im6nOgKf5ywh3PZvTuY2uJQqJPF4Hi+Oq39FRmpqOO6xWD49Yf1Uq1Z9y+Bpn0Cw6A7p+1X6O76lqgBmeAiY6ge4XbI22OyWsf0eK0JmqM9yz+L/K14ltVvJ8QZuDOv/DEy3tbvKeTRaJCSej37k9VbMGnN6ZFZwjND/39/p44+7joN06F43ySZjhyw5il006eV6TEYvuzsiqFFeGswT3nvdrGaq4FKHfjqd7HA/Q4LOcIu9y7eCdtv6JX10pFW1Y5R+Px4/IVJnaa9jzgxg8fyJE2a13a5u9iQWzp+vQYl0/UauVE3/LpkLyI+yYayEfo4tWHnZtaU+YHFxlE/L24aa71sVSAjEQ1KWcTYNvTlnydoGiR9Vdng1SjnpQ6DWcqbEdlpSCta/D7dlSbhK+gcqoAd9ZUy3KodYCnu3vdDWAybVd5iMR9NzDt1LCW0IUybm2UzNFSud5zWvLnmmKu1GrtLxwx9mGiNWraDRZg80KsMiIkmTosBjf2MwIAF5jJVNp/g7rxnqTbk8xdbRrFWxsWqu5p0r+2eB2UN2jQdELeiuF0OD+mQIVJ+Wr+CpDTACXvbtX8F6amrs4CPksw/SF+c2tPIGfRqRYCWwyqZAXuqOWGaYuVhXr2nmEZggmRxu3vFOLs5zPYimh3IBY309KUyM3Fe6g/YAKMcy9aW8MdiECWwAmSfqoDLhJX5kn1+EAiHKjG6FBBdzGdVuN/GjuYcTNcyT3moTuwWt7hJWL60bKMGGtrUxjGlvM5ezIiirv0WTCYRzsZ16SDH39ZpN2aRHLADJzBeXAOC2iLEt4eWaFOQmp88vDYnkO0Cnsj535cm5OZOUgq57ZT7EVMllseeRIgrWPUXULTJVdQa6k3TrzvA64bu7U53/JB3ZIvgtUs5PVdfL2wlk+AixEoo5m91FlkxTsziP/fzqr53Pu28P5Jz5zchNK3eGgkGnFUsd3vndcQnPj6/rHVGSZspPlKLxTmGB8tRDb9QTxkM5TDN0YAeCe/UAHsNAhRP7EbqXnFU3kDZU7I8zxvFmuL7dDqsjUvXk0dXSAgkUf62abDAG48Vs3Jw8UO4XZDf8E0U6ZE3ekgS8KuikWVgw26Mo5AbzOroXMEpMQcUEVg4liFDwoKoL5p+U4QGCBEC5J4gneGjyMnPgQ8tHlvsXEpBk2QTpMf/2LMbMt9wpjJFTwJHOwZLn6tZ3B89illIZ8OGI7ZiwKuZqYgcK8yZs0Qe92j/81pQyNyPdOLGHoZ+HWYVDaLTaJCGMpUDbQVEwTNPBnYQo8AHKERsW29p3rCC0lnQL04Iim3Ey8Gek6Y20Cksf0Z6CScmkPjwA55F9w0CL95Mvhcke2gzPc0YtVXPmjh4nhdViAn5CGTJGgrB8ZpjfgDYdlcd1pMBrxTe8C+BTB5NxuwUiQ3GUpB6vrl9RVK+QVzUD7Mup9LUFwpoR2dYCbW4kS6131YafP0Qk1wNaYJqJVRTSSxPprg5DbiFPB2WALy0Xw7qp0sE2YIRwv5ScGKLe/8YLV541NtKJloejMvGJJsEoJupMS4Y2Jirh+uaOpPysLBW3kXUKvZhRgHtNFltF0Hd5AfovJ/Qvureb7HsIiHFV0hkDCa35wFgQ8gR3h882L6V/ll6HDFuTwFWC3Os0WZzKFUGawnTnj+EHIV02tpe6Gt1E7lvxB5eDmOaM84oOQzFal6H1S6ckugXMdkbaABijOlomYU5ofaAO1528SKmh+cgMFZuq1Q2NpNJIOC3KaghEh85xTTtJZUioeGYTKt90BsN7PW+Yg9XJQ/iirV2g6EZRQI+cuwSZtYq1SvyaM5hdmVlAVT+v/6eazrwdAgkIPMSbUT7L3uP5Q3wAsREFD/WMU8hZ03aJVvPxqASJIIazLq02/JynJx8C2dmYocNDo4JujNE0lOLZe8Brx29a4O7UFAtlemPDbBgqora1ythUyno2fP+dVmVuVxEFdOnd7TpWMdz1RDu3daId1LvEdSbrIACbPs71Oo8LHVtwsb8llcuMVPUxyoOcGYvDSDQEoSEWNtnFTvtOgMhU8G4ApblBOtbIhWOjP3GJNq2InPfeGNVc4JXu+E2T3Q87363EuCahDkYb22nA/EO8LSM6hUgSvaMC2s7YRjTP26Y62qCxiVc/dYennvEKBtad9OkZxQUXlGUPTo9bSXtbE2QtlizMcxWUeg7LK5WcOh8+bwQEFCbNuGbDVOUxpWOH5w69e3YS9Qrb6fibBixpq+GSguTHzsbVpwcpwHO5hIRSAjEnnGIFWx8jOhmtBhTxEyINAnUoSzpkO44UD3lrqfBWo0W7u7k8V2Spq/Z4+LLWT/kHaV5mhuBtzysrgQP8c7oaFXynIe2UnebL+zI2fP/Ycgl8W5nhtBvC2kCSLvSof6KlcxdbgSNRJd7jPjeQK6eDPMFCqDTPzfdQuBXZlYJhENt7m2yB8ne9MFYDt5Lo7hnVzxLQ1pRvVPfVtJFaCnUJ9qMiCEI4+j+E3nWhkG0ePfqYh5UfXydh7Nhsg524XbWjFdJuuFWrf94NmVjEMDCBXg8iKQxwec1a2dGe5gsz8ky7X44dJm/1k/+lrtlHEw0mpeJSF1TAhFyxfyGbtD1vVJfh9+OQfivIZPfZsYlu7uZ0MBLvduyt5QGrqXsebJ8Ey6Ueislands8R+GCybMES7ddLy7un4q5WTks+BUALgw204zwZOkozLXPdHXlPXYtRt9EzDPQboWWHWO9JuvB9Mbr2b8JDFPIbu68/9+eMhyjxKVVrupjEKln9VtxsY5xV5Kqpr+MpqSxAblrdAF1NKPBR4XGmve/sKv+0XKZGjKi+FSdyB2T0AEVNaw5UzQ8SB90l2cD01gGbTtGLiCt5xcnq5Rhu6Q/UYIC/G/lZM9FyHQul+0LTJiGsyy/1Q5PyyPzeyoN0yW2vzeoTlgjtggjcA0HDgEvKOVEgKLCy72gftc0eFac1z630spArQKEG6G6r8CIkphtyDxSN7dOPuWjw/weaRYr6+pD38hHUnSiwXcj8I2C/H6MQXlyfyNm22GCTInbPktZCmvg7pohhn0WvT0o0SeIMdhbrLP590CeE9Kiiw9tvBDTvpyBtRwLgM+7rYcjQYl8ttzgETF2OiXD5g8tZAs5FEBL02g8nnoqZ4gE4dHMuhg7xxADAUIMprYIDI2mNAfY+OnKckjKvoFS1iNx0vAbBoZtkR/p3jzlWEkHfppE+59QuMtbVwLZwiGP4dnb2sjpR+ri+GgSw6Kdz3YJfT+De8t+Bglxtykkc7JOlbZaQ4Ar2x7nMJPcf/d2qFfxD4jcyHjYboARGvpiVfb3zJLBCypedDF8uWa6YNFrMQT9PEW+4qmLwf6/xQApyeNvRnyHLngqdXwY0MJofKsKFGQ/ZxuIa2qmBTBn6ZmI7WxlTfMrEVZbDdZP4PkqV+Ta0YS2305wDdXgiKPUw2Esm3FqMo7DFWeiidxYkrRbLscsUYkC3/Z58HZ4zwnIWu/o6FLgPqxT95UG5Wcjn3UXk6UOqVZveDIfI/soKIU0GfPHa3LMSJqJjLsbc7FXx/Aa3UlRIgkLHnoHhYUnsU+kfUwH2HjrEg4cj6UsQcWNZxbOfp+qWANEhL1WBPTH3Ewt9K4qIrPi6RetJITZOf4gyjSIp6oMqf3vxHvzpokJihfJpJOeoinQXIirbUDkywccccH+6X6ymh8bQZ1R9A3dSmPG8jMdgvM6LEUD5kTaWk3DDixWSVcxD4jXIa27eRmGDYS/FCMvzWMcTt+7q2uOMOccpQUqyNPEOk3hrY3dq4jENZoCHQkPlM7R7fjrC++ZHTsqCa1qjZgwFAkWDtdOxdiqUvz4Dqm9qhlM6YJrz72ftodfGSvUv3oU46T4mZ7dpIc8Y50C0mUqIEtBqSXSN9xEYvGXbYV9AiRw+i+1xxqHdWgaTYx+nEuWJqwTlrkwWuX7tbtVqeHiOye+dtBgLzDVXSAJgmln++y128DkJIkbC/XcYhYSwGBa2twIaM/BUlUwH+7v/99UTR44Ie+JLTJRXehBwuiuQTLXu9FbYDdI4irT1pJa8tBUrI9AfzI0CK5TfpppNaBlnSRXXOzhmt+wSu6V7MtylQva/bqu+y/WLkUaJRSMs2ix5H/4koqmHUaB9YzszOVrhq++5QnaAiYwnDkzUPcEHxHwAFFcuVJaRt69M/9yJ2FpMHNZ9gErrWh8QMclafFMfOuHwG3ulvxbuFwawf8zf6ktW2njGMD4WiEpDbrKKak4IfTlxQrEPDKQQ/J3n+5sA+vs9Nep04hr2FdS/h1ql8wA25gROqUCsZ1kL5U3H484Wq8NM3A6icFYfdOL8t/DXSNRjDsFR2+89mJsCxibjoQhylD8Uhd0bvmWzX6WCX58aiNzjjH+fJjmC7qqQApFYJZYvF6e0TBUtgj6ixK2HiZkBuiHO/HLt+TNqjiRmD1uIvU46/EDmDNGYZAOeXuhf1bTKEAtAhdoOBumeWbnulvfI7bDCH6ta/q51EqfRmGI5FQ7+Q53mXKVTrDdMicHFkEHVKNhl6IIb+V6X7uidmOw6mPtxbBxKMG4sw6L0WQgEbHSPWLK1lWS21A23GMeW2l7WrdA5hGQ/cBdN71qziNK/gqergnoWacbi9SU757ahf9/il3Rx/wdYe0kXSldxUWDJQc3fHOFVL+WYYgpOWDBg4ozF90Z5CTF13W7IYIINkn+5Y252XE8c/HewSlUrUN79Hzv6D3+jXJNbbWC5yGQw+O2h8SlnKg0cB7JElghnr8mP11zbdwxhqKwac2CjDy05wEAzuxeZEaVaRAPNxXOpPKC6MfvSb6q0dJzyPO/CrNl+eL6Q1oaHpDbPhcdLOs+KiWtM85Kinp6LvFjuKZq1NlIr0wB5uHCvzmI4b/8ngUEaZbfO/KNY0nou/9spdZwRsZusjkhJ6KmvhYzv7ow2sk4xJd7k2JlCy1kfsgGQJgl6dkzNOpnnL+jK7jO/0EIGMCnmpc1d4vccFgGmefpiy5wl5tNDEYfsG6UnfYitX1Uw5psGOaNTz/dW4hWR/7SOvnUN6lEPv2ucN0EZWRZpMvO0g+Zj6/aatu2ZkXa0FhZnKn2eJclX45GiEB7fL07zGXUpjf63BZ94arJKQK3YFl0B3kTgCzSGIhZObKCldBdHz4lvq13T3ZooyO6j6QcRlwnaFo5Qt1g7WR4EJL000NDSPyAJp5Cbx5nqT9b3u9bqR+wqG5/B08mY4xRowZdhjgfFwSuhmZluOV0GepNl3eeKBZpHvDpLXWDvL5yUue9OPge4wewLosZHuz8yZpNXC5sQn2EOeiACOhPSiTbw6dJSLwsukogTqfqtm5SvYVqed9GiOv6baohwKceGW4D/UVV2xI5tq97azcVeIIMTCHQCK26r/0Qzg8NQQk4nRIzDpDnhC4/yHl85Evz0HKpwynGJFir1z6tpDm1m0+0jIVh9W8HlsBN+9pMpWbEQZpO096g0dFcESj3hNhIJlZS6AAAcephzBNevT5h4YOq+Lw5jwWeBOyz5cLLG5B7yQ6AZTNpdGoms0vesLqMczTNuuVApeQxsd0webBvnlxoXmlhfPy9Ip5jc6UkGJJdiPWpy80ZNgVs/nYzvFb1epGK9EfUrvCJsQtxuvbw+JXkVlRmXdf9LMJ9fy7zevXNKafsTFjUM1vzIqchK0tgo4IgbXYVdWW/CBucM0Pb2Ri0N7C9nkW8FfcUDIgg1dFDLIG4zwJHhiT9OQo+Y9/6RysEsrAjj/WGuC/OmcUIEQKXsMHPHuCoOrMdRLGrkNNj8lA2J30anViZoBwOYhEzwAayjVbDRKLMWK+Gl9zOYYN77gaCwDtNqEavw4Y6priqJRUvLyLGm6nJMpWolTyKoU/qCGYoDIgcUo5tMAc9pGVFqPz1Qki+GCEjFbHRisc/ucrregZ4TJSAE1c14b7BIt23Hmnw6QXGhSc2n1cg8pkJnBhNu3TBT1Fblr31x+inYaLz5ydPPjFbMhEXiHBaPKkq3RDmBc1UBqoVhRrcq0+ittMp8o7dEXHIpoNQO19AcvOqcLyQD9jD5jFfMJD9cfY0IAOyv/ZeUo7OQcs01jUBRHoFbTgqh67SJfO0tGBOHRZUIl8a4cZc0QFbALsQcMkMqz2Fq3yA5y5fx8kHX33382E+HtxzQKyuQa39wbyWj7lgbaafXGJcxQm9NQvgogD/eooC4/I0+HH+XEv50ilF3dmmcR3DRJ+3kt5TusO3il7ZuWthN7mCV0qMKceGfALHTLtOaF7hzPPPcZfXuAGQKzkeoLQrUYfSzoEfal6C4PI9Lan/pvroeRugBNBn6CDMSMzWsd2HmAo5muKAr6L/WPX/edC2huUOpsp7oGc9tOChJZgzLliUMCtAoeRnixabWiIfL29bfpCWuJwX7w4ij/CGZNH+a71jMQl8z3cWALroKx9WG5SyOnZpjhezt5YVAYTZWYKoglYe/zjA5sKsu2UD0kQH4DQMMDL0d8TFQUHFA5QLgqFsGQBOGV1qqfh8fNRNSFmavio+mwBylNWGKjSKJ1fAEl7skvZqVEeAcFRHwb+PrXlWPtdvwg/Kw5BPJGAONr7DA2+91g8BhgvugpkUnCcLhg4STQLTiIbTl98hbbZlcmpZ41unRm6qXzto7/TZuGGvF9JaPS+O6rlo3sh6igKYI3rWh5fAKbfePmOeCOiqV5CZhDLOlBzKfhPcI0RALrkYnOWlI+pDHINUxIQF6t1FT4RDV5CyHPaMLSYyaEDL/W4DLLKyZn+x5zlALW3ugk24LjNiAFvjc0Oy88mprBkJImONiB/f0nhNeTKDILeCFcM9TRo4OkB+vthimnUHEzO9zRWcJ0eGfhQmvUovOG0BfvyuhH5/SbdACfAlfBOVmsNGZw9t/ZvBxc6Md6blB15H/sYS4EwzJDni1liKngbbB1QRKS1J6zS8S5aWsT/rlGxl+rApfiT306Mi8Ej7oHjdW2I8x/MqwPreVJT29kH8p369AYHncwwvhteRrqQI1b2XVj2tzwZsVznHniBNrjx3wrNdtNpONwxNgKrzXfMeK7y2dcSODOxU5As7Y0gvNf9B/kkIJ1QYSQZoWUGHGUyvcke4Mi/9bNKX24ea/HaSiYot0V/vWmbkeBtC+Od6nerkXyHfhdjI/lvzYpZDelkzaA7SMyI/89gDqzXB7gt2kXZErAXV2FgD4YfXcV0FYXodqQSHQEsAHuTciekUdO5mI63hbA+1S62dBHOT6og5jvVVLQgNwBBTxEnMlfeUDdmiToDnVzbYgvGT0qoY4t+mEbSAyBeQMPMCj1eVDBVO4mtkdwbXxERIkIHgu1ssjfOssRargey69S9ZxDyfps7E+h3Gon/u9ZuFyClxGxgKe5vskqZkEeRn1MMqBgXSw//BZoJGfok7Z05dA5tvYetC0FJSi5mZiFPS/8HF4lzKgLu+K+kLu2xxhGix26010k4r704no9+Lduxtg2oIkfbqPneGhSa1dYNhjSJjth3DsYHRcCr3XH6RV1oDbdRPt+j/ok3YLqMWnPsfYPI1zWG3mU0jTn8zEOgwwsupeueo/xal7n1948I6Tk9sB5yA5buMleRJpSVKiJ4/FrTbmOhHsar7AOI0yrf3x6hfRsGRJw5Iez3vUrZcMLrYY9zF0SLfQE4A5Cucrkv+7a+jkoegWnvVhmKEPiXHJuAPmbWWqlcGJgkbTk8E5LkQ7tgxUJB5xnQPSh7R8O6DPg/y7UkIkWaz5Hv/pA1ZbGhT3GK1o8jlQwVqFn/AeIjGVvD+KrqGCLB5uAuFbrQOhvlPpCGAv+0GZSbNY1VCgqWcAzrEDOppqbvl0E2dRncPzFSroI7OrVcwWS68CnsteZGY8Mz3aMnlw3Mt+08ch6X2/rmiXFYqYF6cSdJvLn1G06VTNVrauSC47OWW/FMnrb6GSgxILc5AdLSt+trrzHW7ldnUTbnJGZJKiK9SvcuHi8R4f+b9LAMmzDKNQpBxt3vdyRqU9xKarqO0lTM/dDoMcxJxTEdXbmbf47aDXD1+5qfWAHKpb7y7SlrLpzgyVVmFYKwe2GO+b074yZX54rYrL07KjSiW25kmlFocmSwc57CSNuemXEPCu3lujQt8lRKiU4clSpzDeA5qwmF1NC5RmF1Welsge0MLBptEkcmbpXr/G7/eSglF1wAqR7NcPmZvXrmtnByhWloLbd6Q8Crqd1nQxtHaLLI7aXiNuU/mTmwpS9stMmFU2pv1RXpDXqDNJ3pUEwjhaA9MwPN+iFuOHxjRv5YWRRi4nn97AjoJjT+NOAPY3EK7aVpSVzJedHfF5zqgb5JahHopaGcTk9lUC0TaGU3MS2x28oe2yMGniSFLTPfUCr4oR2aiWB1n87/hC/B1lawlF75wFrNiVNZUn4gwHrezuJjoyJbKA7B8CIdyHDrUaVorjH/mwkgx4FlsnWE0+IuDj5H9y6nQyJIKS697oi/kBq55nq8u+adgngoQRaMyBgyIDTVAywJ75aF/QRQMHSL5JwpfJGN+uiFfYruXO6u9TkSwdLyYavxFaAoTqJgvi6URQu+oozzyyYLB4vdvMkEavQUbJ59w3qQAV2r9etTM02FptflAlTkp2ui1v/It9a76lHm441VIwfe0+M/Ltb0fgl6RV9VNRJrxBB5tJYX+BAM/AryXB/Z5RZHfoS9mrc8eTzYdCJj3bIQjo7AL5gufpIC934Uf1fIYvVRNuQWkywMxQm8lqWKUxqnYnW9HTV7IGeQU5PTrgPInHXy2XnVoQ+blY8aluj8cHJRCv8LyrQoV4Zr+MCVzq698EXvSECEWK5YposbzxImYsAd4lenxWEMu0yT8yKVGv4WJLIP/plOJiUfquH6a3FWXEP+pSTZ/UEbyhA3ZGxM+L0r8gO2lzjqVcpNsqDLkY3QeeTbgRut1pnSi1vLib+Ebw8PI6BcGr5x4BETcVwE9pwP20NCTuGBnJ1V624cKzu6+JrKt9AAJ2EsEav+iCp9E+QsjmVPlVCKjnr953Lt4sbmSbmDBJ2oU+X83HRbpWSyVuVWi8rwuhRa8d83J8TTy1+nFN/4sM2n8sRoVzz3XDTKUBoXVqhh6eMa8wkU4AAOq4BxR0SuJ8a+HbMl4QxLUo/WRpHNv107/SWSi+jgj4EuVO/5m8UXoI5P/aruW2dSZQDYmpKdcQYRGE10ft21UCdG7uR9sX199fFf+PpJk3fioEcc2e5XQV/9uiini9RaCi7Ag2mG8v1tOe+Nac1eh0fJAA5D2SDyJBoUIMb3ehItGQgJ78ugW8SQlNydNDvK6UmwOSSITeYanISWt5m+M3s4n0xWHMNoY9GSzTpCNaX8301xzxlvtELN6yJhrxvp6CdftWjT/RP1mB0vz4RywYcFxkx96z10Pk7t1ApnmK3QU6V+JAxgbDRLcE6Unv0N7lGW6x634s7w5GakQZWYwuB//LihmyQVSPg8PwuE3xMNRAsFw1uPen0O7vbw3P/LvSj6cG6MZAHHupbXcmDF8kBcnaPrv31BmDHEc5QNFOwfEV3WrmsvyeSVBlefqYaRf5ogzZPHXgWR1AhT3VULHJEYF8Pw3t5IaBVHEuGonMiMqzlgTbF8+LJBKmHQHrRm4ooFkZZh4Ghg/WFfDbU6PuyTW7t6WA3WnVJjJIt2eVqTXeANjejDDKL/FOEbHtw2jAdUHydHgVdYvcOb2No5JrIVPiWBGe1Uobxrp48cAufC9r0h1Yn7TBHigVinLEG+guO3AU8AHdQDU2As+IEG6x7Gd3GeurKmsJRZ4HRPoIaks/IGMA0fl/gD+b9W50QoHUMNtdYcRDiBNASS7TLgYvO9qa/ron7/mFPBXX5zSaRANtL+Jmn5x17W0KiGQh7PsYBKsrqTBD4f2wsoroD5WlKCR4LcKd0cCEKQy7XrohwrrvCsrlN/0vUGIxPkj3dE/AvBS7p4IFj8yS+A0bTLqpAhLaZugIE/C4gjqvfY+crJ0YCdbFgLCi0yqMKZp/Aw6AGmThgPyG1eLhz6deSN3xm/y04Q9kLq8KgcTpzP1vVcxvgH9GA/B0QBmGCbTYboz7SIEmjnFbcJUOK0zboU0Q3K8HHBu/FnTSkTjapKyBkegR++KEBl2/V2X1ZcmsPjAy2oYQidaCapnMUoKou+zLDJwJ+rxTYo2xNcQXAUV4CRfEI5P8DqRJT5ACr1BHLUg8g7JthP8PdDXvbrSSSvEozbAoHCe51Td/fAlyjbfZ6WAbf5D+FntJhLkliapaUqTcKUAHKGQiaMqQhNiweOdGnThdS5E1kwIkCFXdI0kpgNlEqwJEuTtnh/z5PGku6CtRkN8oOqAQoPSIzAVedh+yHAmDp/DCIvKwDpzMpg6rYRi9DUAbVnTWITAsW7Km4iWu1fKW1czh4IGCxZshTQdaON/Jr1kh+u3k6mvB4vAxm66FQOAJXR6ZTAvQM7Sz5FH0nWPTT834N/1XJ6tkbHi927XZnJlZkTLnKh4W7n3w3fS3iBMJ0bw3lId3RTvepBFCTWzpsZKLpSBKKGD53GsF09tm6D8xD9FmA7Z5/xhvpqv+Stgo1zSPGEjLNqxLLqe97np4VChYmGuoNv2bHseMYiH6ZN3wST97MBwFK+Wb1esVAHEw2Ea9fh+14NxhHYo5bSIrCR45tOMN2vfUVrJ01iLZPNR1VkDF2C9P9i8p04ZiyVImHg0/P070G0ANtaU43uMD8+vcBBoWI560j35xNNe0I0zzXCaNaUxlz9CqyWXiMd2PkMuKEL7/o5KN/n2MmxQaWJKLAjT/v3IWcxtLBMKL9OFWDCxa1vYpE7JC3/Y9wlKySz0lSMkYQAHeclex69nVc5R6XXlqvgzDeEqPB4H3RSxOv2QUpNco3QGY1Cz0uyXkbMJheihL/ffDypxhnMy8q0ZKZb/JhDkFLZZxkL1A6ibFX/juPrikobAhqquoOgM4yiEdVfaeeeHALYu4CKeFlA09ni86JI5TfLKyrjN60jr5s5rwspgcnuMmow+1NgaE7FymncET/mtphH38JizzmnZNcMaGo6+90a2gdRoZE3U9o8c5g7IEadYnJmyaJFbyRcXPioBpT7LzKHUyWfcOQYGqSDjHwuBnUsWCYJqx6ZZhFGeclJuZthdIvIxgtkQ0ancJo133fda0gzKVmmPeTkdg/8XANuXP8Uo9d1mKDTMUWDQztzshgrCLHUQ/sLKabt41QG/9ifmENbhNCBOgQWTuMmYyohU9QjVw+v6vTSo9i6hGGvadpQY2LpMNok0EXKJReRpN5IJmV5c2gbHE/JdmFrDbf7LdCMa/Rappc6sgAjOWtfOUSrXbb1Na1mWNKKo0oQNyUnJU4PxwQo2yVsSiJiZxsDUBvhCMj7b7VUOQ0u0LOYQ76kJKFjXT9Qq8xFyprS2OiJDDCSN02zAv0iA96HZ/NMT38UsX5rg4N9jyevVzNaX+wXmGKvtoFN+sCEVO845UCOVwLljw+FXTjvIE53tWSGYXlU2MX8RylBSwD1Oa+koV1PC+Am5hpVPVXsKKW1CmRk1JT5SXaJ3OxEMIZs/l7D+XfcQWAUfRBJiN+gznC93Avn/acBlXO67xPvWci2XED6O6DN0qfyn6Ng7SA0T9+nFdJ6Jidwgb95S7FaKghUpqneJwvN40+2liupVo09u9gHfo+MGMeR/5lmWlwJedvPkXPo+hNIfmIQ6vS+Hqy+YRsffeAcpLF58oryY/QykIwSmNIOpOjBffsoPA/mmlLuHMOvmELuSWfXVNHaEe0NTaLvxpv+tgUbeFwEeJo4JjlFzZfrp+uBlj20zPMPl6xYbVfYIj5IB/ubzfk5q96StAVVYJIawQ0e/ufoGb10hSUDgpUKITlgnZ2jcGYJDNoZR1nAo2hneL/lhfolDnZzknEl/b5Lfu2v11zEukWlK2EDbfm1Gx1xMCjyoVJeW147UlqGq8hJ3xMY4pUX/7HWt8LRux0n5AKWa9Sqkl8z+/ntfG0CWLSfhkk3b0cP7sA8jX9Uamtwe4jNN4aytk9ikPGGPy5jD1GLzQ4a6cPAlMrebofUlh1TolwocoE5z1L2s/8ri3z+d6dsxo8+BwhqWiEnVO1rEEtP02sV5SThmRUZ9s/UoN6rZOffoE+qrszqFq1RGZI/FN5ax+WlyniWhEkr7pha+Ijq4IYJZ3HvggfKA/ojHyoRa1Oz0b9ZeLJrOwKDBEzij6k5be/mccnrwvAN3fpY3ityKdJL+nMWZdWKEkvsCG3NtWkNKBouVSH2BVTr6wpwuR2JJqc8KiucPSF72MRuS8KWr4qpwU6s6QQG0etAibeydAnBOR8IyuBVn1HhLClHFdWEuCISyAZMcghSHkMAwEIlI3wsZSphP2odKSVap50LHbomGehN4mKdgDzM4r4JWZ4kAJsWVmw63rYO/88bj0awi2GkA9cYg/PrXMomNmw0e20tVgjVl519GtS+WrxjwLyf3sA+Ya0SxyBOde1EBOrcE3+CH58J9JTg+DUKuHNNTNiVITt4OfRQozfuTQ13VtEP43QzVc3Pxc1xJ+5toCpO/MmcKEjcXEBxIsH/6L2K7JmkhIQUKrCOUt6YWguNG8gubxOLd0YJW6l8EvgXU3CEmwzh88M7DJMh+26uoR8k7XGiWP5oED5ptcnVSDLTl6hrpjHUz2WUFYNBFWKwXGuUo6BZKTbYozFStTFLjHQVk8N3Bxc6i2SPsgRhyzR4hBGM/zVipXIdGFAQFclx4byACZWzLMVEb5jiC8ZaNVCIgJdSnW6XGKEEaseAGBnvADD3imsjjwCQIB3gGFvTI99JQKRAKc++O/rtR/5+TCjI/Z4hHiV+h6w/TeSOdgPIewORe3HTnOohpyZyzJG1SMN3ErO8vqbK6og1w25Q5SecZv2wCAir8YXntZ2RcXXPi+wjx+EUNaAcW3DZU7cRXHw5LgIEzEYh37ePd1ron5PKkXrAiv0r99DhtEq3Dy0cqhy+Xnol3CvyNq0a4oFdXuVacsEFHTAGPvLgq57Wx+MxQmscQxb69dFasxyPHstW1AIx06TG0MxrnybXGDeRrM3bHr6wOWKeV94iOWtH1VkXKxQcAKTAIW652t7qsoWrns3xyl5NCM0y6dywItxgIzsM54tMWqOHfO8aeZhXapca5z7AViatDl5S6QtJEX6HkGiOO07bFq4TEzdyoH8M+FPkxH+VRTTMpDOtCNL8wePGZeh8zuTQvMWJV9YHI55NutSJhL0de5lkw/7POka/r+k7dgG8K/sLejo87F/VP+QipwIJ3HkwcN81nCbNM739fOSn2y67tu8K55e3vqg3iAAabv0lKyFbZbzHSEHbLOwBfx3rWfLprfcYt3i0/Aolh0p4LZ1yHwwSF/4Xtc5n8UwEKNcJ5NmKa/AZIGfav3DUOYNtoK0+P3NA7LDtFnXK4gS9eyknegkwTWLr3137nlmPNMY7K0VCDpr5cfhCx+eh5q3/Rdt928R34yJHyhXgNkQaTVH2RdgwOgDjD3dsl9RX2VCt8RgVHwOdzAjtn8Zv8I6yK4ZyRJM8/QR1aLoiJaFKqYCFiaqFRDAizo/K4j/T20/kRUa0RpYn6uZ7E7sdmVay3Xnhlve9ejZH0lbwqGXYArbDJo3FCr7Wl7mEtJYHLCVR83ScFipk71srJFeZ0ReNs8iaf8EZJ0yFTbjK5gV6I2x1d5r5Zrr0lks4J6THdKLShfi3Rk0DEeEBfpSUgrHFvucnKWHj/fYJ48k8DEggx9SZZJtC6rrYXSDq/opHGSH8w+IODwCr3B+hio+OEDfzXMw/WvSNYoGmovLczBFmRPWsDmhvdwbBmEYkwdr+iI9ogVpfaiGiPFTNcda7rLalIg3wqtkNI+ujT6pnBLDfHHCxksw8JFh1WAc66bUvvuxgalw1SI/TxIVZTVLSpn+P66KBVTGGekUVxo8Df1quh8qtdX0azaNyi59mA2bfOgkYylcdp7riWetxAr1F4UeIdX5sty5kmnTTCh9Plgf4UI1AlOcKG3bd/Xo4hsGQ++MuXxvqRUUr3YPnoWRI9T5TgsKq0XklHP6OH4PgC2BI7WB+wQ/p9PEfgjXoI9eCAp5kGh5VEuBTve0BUMKj7Ci3Lt/Y43KUhF4FeEY4ilwEnUAbtIUSOWP4Zl4A+ubomSnVranUnUARH0H8014/xcuWE1swgdyDhXpTM3/+XAIHWAcRCAC5KO2uacjMWwycmg23EwHeFIn239AXEZyOd+6Fg6JFyIyhHzVWf0h8JpBPQGYvKRNt2YO1MUGTCPyc7Y6xxnoobC1fGJLUwkHbh4GrLJFDK9z0oFazTstocAAOv6IhOgR+LJ+XwiFDi6Ryp6O76ylwvzwzQJQeH2nrqdDmCBoKuX/LvaPiZ2eX+RJb7zHywxy2g6cLjNyWbRyibUU5D04TztCjpM0xWGtG8NWoZmROWTuEzR2Z38lgheOnDK1kWeexvay5T91MV15wMLKM4vXXeewpa0ZL94X9OVpyduz0NmFT12AxHG7ToyswdXR90rNk+LYwdHf1dUxzPCwKMzPqtIl5s656N9KWsL3craxXXO6RLH8zr8nUGJi57mXNl+0yq6K5t/agxor1ltDjal8V5iePhs/OLnsaEJDN8YdPXPyJbeRvyLSxKmDuUKDgx31yCw4bXOMyGNn70oz4hDpkVen6CE4D7zptW67yl4jAj8msIT+lCxb/iu0dEIyp88oIhmOf/HAN/dJZwLU38p0dAE/uezt1TU9ugQjvIuG/IvyhAntZ47Rg+Q/R7p71jPqfcstLw3E5IzqtSnB93CabjjNoT7K8dDR9ehEHmDJIdE+pMYbyK1UGH7jytITkglGDVr7xAJ42jgRX7p62WC64URc1seJF8wZX+wfmvP4Z4AtKh3Uc5NaZ0VnkKT30Q+7242ECLnn2f6dcXo0I0ckKIjCXzdU/i0MaFnBOHvV3oiX+4BR5Cy99vNd+Dt6bO5ba6k9+29X4+lUJpxO3UeB/C8LW3IUaCdF8lQfywtobXSW77A5vCNKgl2f1QD5ikyAlkbgLpP4KJUdk8KvXxwpID24/Dp2Oe6onKoUAK2pYdf9BK7SwfvVKU3Ht811jXtwbTZY2BhDTH8l/JGtdAURnObhqfAUl+sWcSqn+50PLBAkLHHE5cJRzT60QFEXy/SOrLpqiEYYdi2cwcyesqYB3SkfGNTVehaveU6ijsqAPifeMvtd4XEK0Mx2x5PbzBGlkOcmG8MdrAQdFkpprkxULbq/d5kHD8QS/IWrUa4zCDbEGYOXzSrcAIQWB+j0vTISDSNX+WBCWm3omlGEkv+AvCNyFBhmPJH9qCMdvLPi2fCnK8vXXPWUfQgc3QNPJUtBYBvgiKHEZI2rocRxQC4fn34UGp5DMgLFHzkyMlMzzdQ5UaUCD62sbN4U+ihBOAePgqqT+CF4RksW6J2W3E07xBZkK0w3mhQMcZYFcfBRa1ppDjhvlsiHZpdHn4tpH6KzLzNbjPPXUHCncUO4y0KzKGBvyKUXJJzj05pp5SJdD26hbrU5zKvtt/jP/o0QspISiPHFr4R2dpcggI1qO5UXMPfDOrwBYGLHqpP2/B5RfHDq+0Apz2jnGdl+i6ssU9MXdjq/WdL+2U67MeneAdRGmL6mpHUNoQrbL+5bt/lBfaaXPcGaCpoE1D1I5j5z9FdIiCIwVictPvOajTTDbhr/JO6VEi1urtKVvLvkx+FeyvEXI1esTL7qAt6vNEuJ67fl48vi9+2fxblLoANou2E4lRlGEzEUnnucRmMQWo2NG7iS+FECi4IgFZ4/ZcWR09MSei+9Q4zLQDVFi7YuPl8vO+8Fyqra8ppVUC71hVPjYnMLUqJyTpu4eke6053nxkrHbDgSqaFxy+M67k3ZN6NWCi/eROGZKp4c08QcpgRcM2uw+cCGfPPCQmrVqocGFAXRL4MP5gsnrJwey64JuQ3ZujBl3KfUDRrOBYgbyyw3kkkXEhylQfiOPFmB0vSiehd1pilBAp+zOPwvEX7vp6WASb6vf+OTptJT7L0IjhpsNf2c3ce27zpK7FVytae/MAwFV0qnQbbzihIwdVPppRunKNl7E4uVj5uP0EFjjqyw8XA8/Zhi52rz2j/NyAzfQPJj4wNJOXw+/ViXc3KMqFT2p8sim4cT5+KfSbFNzbgoD5E2EKZv9Lkzhn90QOiOAGZ3aps/Y+NR49NxORKRCyWWKbxT+i7nhn3kSqwrcrtkUJEFGIy7SvQmwMOfmjUJYGZ+0KOiVoSjhs/gk/cJCdWs6ylL8kizCeUwoqRxVD3KNa61IxGqn+g7BqV2AagywTwwI9EP2esGSbIDNUT3VC9TdyfKxi00OW5tQg1b8Rhiy+iEa1CYGMV1vPYo2YqKui2mrtACte2+azOMRFQ4ERVdAua0lWTQ4dVMTMTmaaglsk55rrT2vxqOmNc6weWVZt5BK6sESt2LzjPqvZKQFw/1t2XyF1K+Fx9sSfhm3dT8ttnnio0/7oj+qgF55l3vKccdvj+4smvMB751VPNI6K0FSnfV+8UKF0CZBH3FTm6vvbkH0AftZQawVvJ+zy3YMvPdHcv/5Gbe/M5GdQp2Lgy33nb4HCPojUsqo4HVUeFDM1Bw5H+QfBJHQa9HaWJ8+F00oIOBG1J/4u8pGF2vOu78fSMtsnDECigRt5ah10EoZHqIksx5SYLFYKdQ0zCVuBzQmU3xrEC9ATb18BvrMow0mqSTUQ8/rxlxNwuLCHdL5SPnHxarQIBqaK6gpJxBeoUPj1bOROzLLNNVdsh6DiP/pImCBDCTua5YciLbb8iu/kVb9GcoIM5N6h8sNy6LZqN3OAQfAS6tQRk+P3ZIrYCDnO0Clzrw1V49vkNPrZY5nnEmKWpj3TZqYjpQwvO+g7pDn9cWEXMkwYOWaKMO3T9us1BigMAfVyUsJC9sJGbGr+h5om6FxCWXsZfFDV76rdgEaIhZ1snhLlki0F0eg8BA+zBeKezGeEsI8f0x1KALyBkYp3rJpCIBP1v6t58Zro+R7K2qtMGzhdccu6mO15lw6HTuS/Nlgi+bIDkcp3gx7M7ZSJXp7IZWHS3AqdBsiRzh/BE7tBaCui1CxhQlmaeZ1Eow8Kc6pJIdpIofFhnKRYc5EjO2EXYS0wOYEmDVNjmrnFz3KD4gnDJKtJgCVDEIPS+nPu30syrCRWnD8E6t6vnPMDaYbkdP/ywqTy0XHhcIYEAYsV441BKv0+aojnFVIglDycOIiaJm5BxUg81NGlskcVMUgEf7Nybc37bMpaZK+s8m9eZ5r6bIpVDOxFWI5naD2wSULtxyLZ+COV1L/Hpgu9Sz5yWMp5hA2XBO++blV9ecKb36gdDM224Fa2hT4js7CoB3WjbcnOEncvP21lOQUmKSmmp8Hig+hxwI0LnYIUK6f/2dqJQAmGaAKLunRuMirEfA4RkX8S9W0Y9NrMLlkTKQ/RBOcCTBnLyfTCdjaweV9p3zRf+0GGzImT/eoIMh+zYue45wE50Y9Tz4kNqzAHd+RhLGD6h/bc9inUHrQXi2vo/j7fsyQCQ7zem42k0xfFMBB8p7t9q4d6jO9FxljWdyJyjAuNwFLmzlnnaY8V4Qf48fmiZl2JzYQHZilGqInPdAGsktCVTVDUadzI3NYvfQrQEoW/l/7689ify3k0Plrqm5Q90vpi+BtUl3bz2uSXCtBJmlUjCeD3jIYEi10zQq0SFokVlDQQwFUCOB7on+77dYbZ2zeUT3eBpQRc35ZBTw3fBWqvLpjl+zb2xz4QH9mP7M+unsefTNLXNurGLGyZXo2p09fX4a0A3KbQ7s/3KSX4gFDEwcfB3ucnknQskvJtMwX9C6CljistCRFWgYcK9UiA8J3sy2haNvgoTdKwH3hGAzNW+TFX5ZnZVFZ6Nc7FgauiBtSIC/XJ/3xTMN0rYLokM5N/ARqgkik2Pf8XK1MK46ai1PpzMmZFhBPvsg0bomFOn9O8JszAaqKBmebgisbCWrAMQEIbu4DGej+zdPeCH5rdlIlGV1grJb7ikYm2QLud5+eYkcSz7EZ1GWGtxAGBq9Oc178AOcoPhBoMw3QHs6Fc5GldYhovCrVsxhoupyJxfer9/EP4phejLnwCwVtgQeHqF2rjwt/q/FTUgEFy47fecgapWfwmmQ1wdjclJLHBo0fr2+UKqgMSsxrqKDP8q+DX7wC9ScAAcs2nARJIFFnvW86omO4+OK7vUVYeWLSbTM0s3vu7JIBR7wpy5duJbmtiSu2CbnDB+EK27zM7hiWLcslW6fXQS9ikCRhs5uEfQ7V/P7PXkAEi1bOoN8DMVTqpamfmmkk/8XhQY9G4xm52/Rv/Qdrbc/LPOr6T+fH8d6R7XZK2lCH/XA9zhm0DBbBuL0MXkXXYtviS8Kzdkzk44PU5EUQ758TElQgk9SzHNEXC7M5J2+bucZy/27TkX95QOKpBUOjOor9cMInuOMSBVLN2HzUoIRI2PJDxLh9MG9zZyiqqXGwQVHtehq33UKG+su41vXDrMHHIURKxuG5cET1QTKTHyDwuT8J2mpXNmgqx8bOq9f0gJxw2q9xRNlIj7BQo23pDjJHT8ZXpTo194Toqrggh/eoqNEtPZSsxe22yMfkb6qlRqxy50rmiB6nOKycmz4kwtL9FVPl20k0Jl4owvK90JL1AFc9SZTg91h2kyleirmcaWsBBNHXBEt7I9Q0Ld04JV5at6u4nIu8oRMHkueTJQMaeaUo3mU+kQm4AjV5/w1EIrrUdGASFvojrr3r8b+kJwof35Ns2BkFYiud8DXufKetEknbJDfQlcjZAmPcz0smM1pepNXss9/Pf4jNHediH/KP1D8ibg/27alsvUb1/I7TroJaDpKfiHo8R/ZZEpte4zZZlTg9+0TaUx74t9CXdCllpH3aLUe5vjuVcwvEQLO2vTRXGToD7hy077tPUHzNZFak2rVkzPg3SDfqxqwzpxiSFHVRBC5ge/DGq9tQ12OjdUhhXToXNG4gmsdV8OMhossCN0lSRXvi2myqxjs+YNaSnmPWYgbOo6yCeywUYjdaeCyC16i6iyhBku9uHgChpHJnd0PbrRmjSIDjpkM7+9zfYqIXAgN7ZncBEhsVoAblYDo/pF9316izu7YZs0H6v3zzfkyhdD/osF18OQL1bLJ438qEqQ46+VpP4mN1cAnc4lG+6DdRtOo6ZfdpHe5DhCOBw8+nOj6xwz8KeDzqVGLOgQT4tryIWFg4P4BEjLsPFB1K7FBtAUOCv6dPL8XpB5+EsggjhT3nrFny8a9PtlRkhNct9EI9ULKB/6cbisxn7+77+PJZdAnOzHshguYI+ESC1/WkC9tuSPnew0zmER3q3LDOgn2Y//9Md3NLVkAxiUb2d1jOEkD402wKOgeGu8JM8izjy/ZxusgXU6J1YMZnto/TZHuDqDYuEeJuuAA+CfS4i1cIdCwdo43Xah3Pv6Gh2BnaxpzPwfRQL5Mhf1+PXRA6CRroAfeWgpuRH0vxuErso2iwgCGyaQvonvKU0gdV/WCIXNSTLEvSwZ6xIHGhKZRoildAzwBgkOAbpcq53UT2Qd1cUquMvIVbSRJd1HFBywaROfoBWVTWR6z1SpCqxcP84IJTM32qsd3yBnQFPrfly+P0J24IgL28giGUCt54ICrio1NTaoTSNMAaFP6MY6D/Cqws1+jhA55JVhllepSCTKBhp1KXgFw45kv6aAI055VsG6Y8dqHO/07CG9Hrr1SFk1elhMoCJoRAirJIEbxAvAkQQCCFJBIGR7yI2WB8e9l41zZXQrzqHwDLNHl2BLQDI8UsjAL5wYaKLoB8RIWTH9vTllRNi0yftqKaR8Wx1dC7lf7IuPcCIAOxSfLjy17xGu7eCYhfulikdcZKG7FNXVduDR6CQUIGGv7Hu+o+5lUnIBc4xovnolqhXx33Vx4FLVw7OUXsn8nVa6qROcPMJQUCVBAtmv80ogw9YPB91IO+5XHSLHiA9WJohL3grnrFWV6nwhGCDBVzIcEOkcIHC4eg7lzd2JGaEcH0uupISS8q6/ZpTFLFYwG0cYX2OCGb59S8As7aqPHYokJ4zDmhEUF+QLMb6LKjsIFMTZRCgn/GwqAYwlSpYOFljV1gfy5l5kKJvWp0L26EXgatjs3gCu4aPIiVT+f10Lw+12WnlAiTx8/lMEsgAwJUfhqoiq++H/jZatUyzA1myGIxz/wbfKn0+igz1LIGlCVpoS5rb0AkAXjUJHgPBev7+RkL5STgu+TXMTEXFwSHJMnkeYtBQIgqg5XE8AlLaSlGE4jkBNyNGgddGm1XRez0lQ6RxRQt/akSzU/IxST36rhtfPS/V6zR+o9CzroADqjWJ6l23KupR8ElBxSY4JuBdpQBF4q3B2CoD6aUqItqWWXnw51aFCQnmY6vX7itc1E5XCQYF3qWByi0HxkzhQ3ybGTM92WDrBkOkxWygkezE7IaEoROlyD5xm53aN1glctHjY21p+ynXSmXUAllCXy0j7HIrz/0Vl0mV4oAE80cUmcuRJWkCq6a/o5l8EFT4LIGHDLCbjCXAEVOXAIUDkSXVzQ565IWe+hQskI7Olp+RtZbqWMYrdE35Ub4RGbadfeigyiM4vEaPM4yNU1lReqca71vUo7/e3OXoTuhbaxGJ3StGZVskah6stcZoXbVuhxbEIeo63Pd4kku+IaGG192KwM+Kxt+l/IPKsdt2doscmsY4VdTRPO/Y48kEo1EaQ1hWZP2KfIUeAZ7Q7d5nQUXw2tLy/eJN/cTyxu++CmqvlH7IxIPe3MIVc3mdqD84wZc8mLlP43J83mjzs1vMf9aTMkoVCfreYfJMmXRuklaYGH4qy4XiC0N6piQqvqQy/uQxpzqwCtmUslFMsJrZUcvsRYtjl7dgnfpEWuyuCeylCVKj7VhTJZ/O9Uinrg0ubconyJpnpPLPqrQIYOJfZ9kikXGujSt9DbAafBqu2/sEiIEuJE5yv8h3TvrwHENK0ORTi262JRn6FkhZMSeK48JQ/8ngTHA7DSC6TQwM6cggehZBb9YG4fB8/XuA5ZEcL3RmlxoWwBSZm0z2TnqFYQFJmfAS6LjMwpIcY1Ogfsr9qTWTR/ubkMzBUrCelV6y7i25e8tGEdKunwWwjjZ1TLGew4WHMMdeR4wzCKJjuh9Wtyg55RjyGwH7hT2jkAdJI6Xg0oIyrsGSBRXmgulkfeF2Tnzv6GENGp+nRaIMEfUQpZc4XsMMtnxMx0Jy6R4ysfgh13YY3pEQnGZjlorDtTidhvly+6P2aniQ7rhBPx72LQelUzJpsA5iloEYOYb+ZPrXt4bF2ubz0dhBdl7yT1jRVYbCuKHbKTiAqvNzd9vnu2DsZk7n0v1hCuhWBqx7deXTA0XQi2AsOte8TCzMVpHyPILkrTkS6Ir+uH1kIAQptLyRAzZVcbWsxhalHpSg5W5vtwddcN/spnXh5wIvFsOPR+Ktuf10MrXfvuc3+ZwI00AQBRHYXGcUlIfKr2pZTEqz/Tfw3vah3cLpwND+c7CjpKwV2kZpkp+9y/LhF0jHEb5jQtlikXC785F6o4VHMJ2nwL4PV7WG+MKIBnaafEdkQohO+51RiEje2oIDouURJu6RxDawgO4=
        - #2:
          - type: tool-call
          - toolCallId: N1AlxdNL5psAj1PZ
          - toolName: set-policy
          - input:
            - Rationale: Enlightenment provides a free technology and happiness from universities, which is critical for staying competitive in science and tech.
            - Policy: Enlightenment
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: WDpE1MEpQnq5gl8r
          - toolName: set-relationship
          - input:
            - TargetID: 3
            - Public: 80
            - Private: 80
            - Rationale: Maximize friendly relations with Poland to secure their votes in the upcoming Global Hegemony World Congress resolution.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: KVjFoiddr1ywrB7L
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Public: 0
            - Private: 0
            - Rationale: Remove artificial negative relationship modifiers with our friendly Autocracy ally and fellow vassal, the Aztecs.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: bdIsDIhsK7iXpdzI
          - toolName: set-flavors
          - input:
            - Rationale: Focus heavily on Gold to recover from the GPT deficit, maintain maximum Diplomacy and Religion to secure City-State alliances for the Global Hegemony vote, and support science and production for late-game projects.
            - GrandStrategy: UnitedNations
            - Flavors:
              - Science: 80
              - Expansion: 0
              - Defense: 90
              - Offense: 10
              - Happiness: 80
              - GreatPeople: 70
              - Production: 80
              - Gold: 100
              - Diplomacy: 100
              - Religion: 90
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: d6aF8IXI7QnjE9L0
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a18ImAGletlcDNIQCyEXq3OjlIQp7JsotOQjMnzMZsfU9nnitLiVtW3H2wsMFMCZnLJ7CEaDccaWYqtlLtWVwrDYQ4t8AXOfL/QPFR9l0ycIqBTtkj0faGC49vD3yp8+tasE8+uYz26ADdrF9Ic7u9lodV73Im+P0Gz6HxXVuHSYJyMq70k3EIi0MY5kdnIf6ShdWB8z6fzzzyHcBNP9r048qiZfh6i1zo5NCJb6wnTJKUz8TUwXGRNtF4Tg2KGgQt6rxBA8Hm3EpWBPOnaAt6NgZ0OSRqgQ4jv6kDuY4u3rPQTX/LYiFLcHG4+hTKVWXUEPHMO9QI30rqgYp2hmOGsHb4oDNG3PAlJv/1k+rTwsOqhArTjlS3tjQck82vmqTiQKaW4PgLr10jvWpf6sJpWICuBRXgEsee1l1gHKW7X6VTkZOcb/EAyB23tLWZ53/fqRo4KaWBRB0yRwWGIBDh5OoqoRV+b2CBXsq/IZ1ft6UrFpXFUCb1rgAt+zUjht72qXp3PYK51McfdnSxUNtnpPKIdG3TLqytm1RalUfe/w7+cpJasEp4T2fo9tgIyS0oXDZf5HnuBhgD0K+UzJOnBClRgPzNgb+CptFD6hdnx8O15fsqQICtdMmIRICXodU3xABkRn9Cx4TT5u8HmQ4sbAKg5DtEUNL3CcdRtC/t8MIP4kMHeZCca8CXHOZcWeleQdMAmO58oL7dMVMsfjJDeq5z5StFOinup4P9gE4aauBkWShARHebARwOmL05QAKv88SFvpZQY2kX2X60ShVBQTJazifPbTdAa1pUU8e4MdfzPgxGP4Fexyzex+/IN+IsRewwkmQYrwidnyqM5ihK57S0Yr0escpCOaJmEaGYFcriy006bkjKBW12F7yU398irPVYYpVfVjynF7vwgQoQbfmtxbjwC8drbCTNvT/piNhgGPC+ncO2+gDyUq+Myr8jfZxvOxo1fjmkpiZV5yLzDUyrNyqfJTWTowhrnB9LTDgs/jpDZzl1zf1WIfbW51FzBPAQ4m8/s2lTLLEZSo+vLFZdVjWweOxNisNwGUWE5R2OA/RTV1bt47mwMFlqhQzEKCnDwUbaDF43sRS/qebPi3bpu7Jg0TWNsmG3BCnYzMBsD2RxFAK0QMhSIhN1KjHI0WMfzOuH88Hh4diR7AAYr6QF9LGVpsAu19gSzbcGhF/b1GgDPLFVNBk6FST+a6880uf3CIJroTpjYcm6WaXV8EijP4B3njANlb8VfcLpTBsE96O8PCyZKysHxsc5foKJhTrPPdcUw5Usokv88vwbw7uFV0AQAZ4qkWDShxqnAPLaXvW+UCez/QRcANL7TJ7diKN6RU2UFPeY++cCFHaV2WuXYLlq9zxt9MZYlijSj8U0K5AEVcOGRnWZ/WFgIlJDaeQ/COgz5VtrxWrbu3peTpLCHJDmpIGiLWte03QodYajtz3sMjOCl7YuMG0idIdSE4mVOQhVZfdXlN4wTJoEKYuMS35i24JfK0nZEQ3crh3rJ2U2CplmWJk/g7IoRVWx1QEawh1x0Vm5HJfcvLp2PglHOkWP4jLLcTBCQlC9p0I88kZU98FrKCABQllXTnHfitzDwL2d6LkI+h8ZdLkp1koBveaLY7aOIiOV0mn3bQ7ArZYJUiCkLJGdc+zhhIkHPig9tuVaEx8j7gNkBeeRPcCocKv/vzcU1DPyam2Efvwd1UGFuS4BCFV69cA4nOapzKrx5snIoj3mj/PIFI2Uqr2fGig82xDdUuUGQRLTo5YVQl4Pew946hRjHN4tx2RiJImRLyRS5Et+wjjFbGyEFpXGeVI0odu+xqnws+0POTW6dsQ8I96oSppyRPlkAMOOLsrjjNxpeSnUk2JoRP3mT4TibkbYyN06cVIjwnovEYvBQqnVCaKvV+tRDTeVd+pJ+Og5KIMECfLdn0RzJ/52HaPWIYwmudyQzEx1vWczNjHtPQNrJV9fufA78Rzk3G1qmLGm+Na2KFd9bdQd24j8qnmjGKFqRD4y3L4wOgd15P0Ru6pQPIQiaYvSCw5ZJ7K1vNX0wXywPr/nk99eFKjMyJCsTGT0gqyQxhaSmfNFHMQkqu60gxTCEqgSYghySUbOQmqG5WgJJ7YLLhwdBeh8NA0GBumpHMPlGgR/N63ChBKzLj9ysb7px5xsgOdflYjrbM/NJ1Odq3FIFM4vHAjSZs/23/yQVCrJRP9mEaQbRACEq46yTt71+hdJKH1EdQHjfC7KuCpeqmZj3CzVdRHAU4da1IbLQ7HMdv7t/baRDrBw4TF3LkxOpjvUuondy4hVxA8S3KcRUvMAWImJwmjtbqR01UXMGNRXugoDzlFS9wYF/NlfVwtlHB+fHGCiw27m+kFSUQcM4IzajuPbBVJa6gSR0rbpDG1fX0TPrfrtkWthjC02Va7tu6lwcALZBw8ThfVY1j0kWQYO3Cqn1sRuLWZHFiYQYQrC2HT88nMc99e6HQ1GHTJab4/wT5qK9Am/S1wUEmZso/pTGAJ+83/46ce2qMn/aWJp68WelhCt7QyQqweacZCPz+4NojiAJrM5ej81YuSDYcgXDF9eQbGh9twsLVtqUapagsJRMQnxkjbvu7SBM3RNd3Be2gV9F4UL1AC0DTn1qX332+j20KoDDlaQAhuy368raiQJCceJMCAF8Sj7RjVBczHo4eWdFU/hqhXEHgdJTfZXWA4rXZaYnMjMwy2OXgnq24HRzxh6zQXUiv/+nSQaQMD1mfX44qhkasdq8QxYA0lyNg1HFzDJN41utPkbhST/6PuJKP8jBx49D1Q2YWcF/7f31qXgJGxn6h9xRskOcwnKbR9w14yeGrDptaGv+VY0WQ4bqwXnMJsYx6ii47DX5FNDD2IX76uWnNsygyO9IUOFzl0VkAuEgBrdSolF4hqo1o5pT/k9xKVhclE+5aRzYpR6e988WRQty0ZSTc43Wats92rj3aDBtJ1C6mnI1s4DcF83qsCX27BRYrgSaq5rxRNxMvOEkSBB5in+IleHs6UHJHbw3EnpEk62891EBO9R7FpuC0HQsktNqm837trkmHSiXVho0jh8uiRny1TH+QRFVBV9Gf5R6yonsggdhncgqrbjIL1ppCfzHl6ejWB8k088DmTmCzZ8rBxyFZBKuWlHtEHyurABXUr6HM2ykp+cRBcBYcoqRB9NrSZCNe/+2DiElUdEkHJEBbwwSXfmr/4MdpkG+RaVmnji2gvUPUVlE5eO8qQz51dJk6txbFx6gVUFYCjm6pxRI9fJIiA7e1MMLOaK5+LU4TgH9/bjbr9CbM78UsNputQIyFe5TBZ32xRKdL3Gfo+zCVCfnSoaJpFELpAPv3EcjL4qqNLsVb+H58pIL9+YzkkK7TYxKcNm0tk6sOzWvny3AHI0XAJjh/TrDzcZIpG/rMuNikQ2bYEr+102XLpe819qmyMPZtzmUTVKfdBuDzDLKoE9K5tsG+FqBtiJls91iqG/SYG0zy9I/wXFSehFCz5d5JJrBGRjrNkPGVmnNdxk7KwKC10iusswjdjHHFAfm6PWnE5TxGynWUUOC8F3K00PWw7LWQGCndIcf7CuxHH6Ts5aRA/f9aD0q4P48mbqd5LE+2k8AheKLCBisKwrkxgbbPD+cO9zSHQQpFsktOW63rgifSE3hkAfXW0CvoJF9zMm5iK/lHqLgR4zvSUJfsJsYSOHXMjixP4NgEYcKSuGUZNyDDSGgqtaFSIIUvv9WDs9QBUP9LyXIFWjfUdYvyHwENLnT9LwSY+jhgy1P0g20/SX7j/iKk69TkQXbFDNBKPQiXw/QQKl+xXK7fIumqhLT2ZlD9dGd1OpUu7Uo/lxaq6ZpyAjAWamRbl7wfF2aOW9x/ODn3vh4+vrsCVNdBAX6eaqoAXKDlse68UgIQKHorxw8DGrB5tVs8YnZvwYfpa5gHGNZLSIK6kkVqt3w1CquXhhPRveMjOssWw2ZCZ3uTyF/J9wh9r7kM/AefVBrrlZ57A259AGo4MpTk3+POg53nhNJKc0gVz4qcjIrIHrDFSXV3GG6W3TRNfwKP5Lzm+dW2EpaemdqNV/aggRZ6ZYeFnh9BOjDK6TuxlZfixLXvw8uZMExF8CICQ/YHYX2360P2Uj/mX7bxk1yrCeg1ia84wMDBvk+4eCbgSFWhmjWxuErShDzMdK8KRoyxaN5NutU79EOcOEAXku4ERf9ebT9INZbt1cmA3BF9heAB+zyRlHukjrLooQXyQe3KZOqV7ZOsTq0Luk7mZb3Tic8YUogIJqo1LbjK7DonZE327hI23GA47DLBN8ePKdBWgb8KxGCNriyR2lU3mcq6AM8n79hg6axTXHNFAouj6Wxohqrey+a1ccqa/4jveNjxWg7X695l8rzdqLTDi/ZZzNYcx845N0h0S3ktKuQL7HXeDawFgT3yblkEbY0hlFQdFbN9BhJNknYxeCs9SDXRonQXJEgb+noGC5nBSmwClqso6v7QPrOVZAsmcHHhtl0yGPXcR0VLiBbfNUrtAzLimzbrNRZvnSQt+3V9HBJT12fnYhSeakOtHtKctAM031rjm59ljRBlhxuUq/MnAUpasYeJfd4fTfEMjQyQw63aNP1ZgtMy5naHW2n5GV5JqMM8ylQjSpHjauHmMVM1RJcknsJqUHX8n8EoM20bq5GCVlQt1Bttthjw0149GKiTduJH6q/6+BtPCkljbCdFOAA43ImQ51Qm/9vcDALy6YAfjRg6c1g7hf892xEhq+G8kL3u7X4zX1mP8iPn1vFogqgRtIRLhiTVdkYffZbe+bIO9fGmxyhxbpMYFwJNO4ihdk09IPuO/c6TmdmPLR75kBJ4Kid54XQCauW/e1Yn8gt9D+SevxEKn5vdaaHaqNmz5OfKRWD336XjKe0MyQvsXvNBttq+1zRSmPsm/UpVCU5pWJNUwzfNBUCJmmrAyFJXbC23+FdqS04VeciRbZXQdKWLlFTQeuuwFxO2f23gvUZIrsrtcH80bWnuzJqexWZUh0sBa+Ze6vEir3mP5P26AEBvv11xRNVN8kAmug/91e5uNVZPnI4lgvogBwu79XMKXhooEyYqE24UKxwFcYtyZ7ytfXGA8kOwxOrE10GEevxWXdc4oQx37bNJhFD57Vzd3U/8IHlLZbWU/UdAHPhfionlr5KpxFxrRZ2Q3jtjHQKZdOkwntaqqQGOfK+OOF2iXwIo4c9AouT8QOqnmEjZ7Nux4gESlW+AZFwzIOXKHagrDpnYwVonvn/X2iQ6mkbbR9F96j+0lpKnTr34ygSObPFlioLonYA48LeWBSqaTXkZgbv6c+985BNv9gSt+dgpxunRgW0IAj3KPnoEBrafNWQvGcPzzQvWsA1jnDSEm6XQOnNUkD7R1YHaLNZZsyzr9YVwtZi+/LOoAyft0mMWr5b/aKyaHXjKueMv0jJidyrzQCjf5BBhTq0DbnZyCZCWKJrB3/f3kc9eOdjM+8GPcBR/DEaA1Cy6TA+/STHCsOWEjeYnEZQKniR17uQpnOdrvPnyjqbzGAgfV8ug6yvIkAS9YRQ96562tnqJmNhEPf+2xmPTGw3y616e/z02fSizpwSGVcOyjcxWP88DcDEvC5n24GuMSRni5IkPeq9ySL+Izgechff+xqMjBvoZV4y6wpv4EVUXSQempkey2DA1bTSTJ34MjAspMOQ/AsYNb8YQzf1UxYwimOQNrtB08KeYQDB5xiP5AZ7lQDkvdBDZJNAu3V2mH3ISnst8Uh4vjoVUJL4Q+Crt4ORayV9bBdmjHORGJdYFsnLb0XY7y1p8Y9FcZ9Dd6Cm2x1gOpiGCAN9UU16eCrr+sxT6qTylId63OjzpOk/Y/4gmyLZ9HljiID/+IUxB1zxgLLaJ3M6lfL0ttU7grizCY2KoGxipBQ3g9ZNfRH8jQmJn7wWeGP1iCwfRlZlGAyTvoqAR3qc79V6YBpiVLg1sVP0UYFw4yEAXwCx5zMh8jL+e+ohiyUIi2/c+JF3WsB+XE1mT1fRN8JdO7xfrY0s9mNBzpkHWfYDmcRLfdWfuOLzHWHuyO4RpwNbtpnfJUkK/0rB+0G1/U9+//sGllbFu3SutlNoec48xOgscxZA2mFfsq12lg9jj9dXwnBtCnOybTAhORvpJ380xImPHWMpuqtOXWPcJinBTP6VRQcZ6IffFqjY1ikmtcIFspcss9Dx8Mg03+J2WMWUS9nMnXS9FcVgwOu7qSQ94vqrr7/hDEph+3YMJi4Q2TKV13z1s7hmxkjgKZWfvB7HsUcnsCz/sYcEN/au8GOS5RgM4RqohZ4zq7/2KMGtdzeIir8mHWncvGqcpyqvaNB2OWBOsrsMQHCeTiIYynSsTAVaaMO+pOFGUmybPs9mDwOXv/gLijgqlXnND5NaXd2I7kV9Dg2KUKZFwSodeLnKqbOpRcxeQm/0XliylYJ7F5biiD6a/1xzKuvRVG5orEzj2HeFMcsPjnzocUVAZCi6jRJnk7WxN7zjWq+R9dmBMRwhmqrHf7uD/hbakEBEGMeN9EFFkps5TG3brFMfyMbcZKGWZRwqhkBDVd5l0clvXLZFj5mWG1GdDk+DvWOql5fOr7K5NJOG/7bkY31VSd6I8zgBnpiH+NBRqCtvViDTHF5hn6vqDE+39hGVv9AqUMmjrOQswhxnNbOjoeQS2fs1azIt4vOiyddAu+TbiW9T0GLqbBCQ1n4cSDwgqBw7X6drNB7KkMfBtPaHSobpeRIIme6H1uSapHFv/f4yIvMlhQy7u9bU8neaiNSZNCSBcG1USagWEYobeBH8aMb3xwXCTyX/LDHeqicji9/35/RpkCL6D5HfvpEV+RhmP0H8cTwo6Wi/QuhiSYg1Fie9+40ZSvkijhk50jczgRg7cH8VHadE1nc+3Mi/9CZ1leZbXzlx3Bb1tfX13CjG/S04gEpR6v16j/NHuL2G/rGZjOvG8Df9lEBma2kIn3efSkbFhY9YwFibVPdiOiUJp7SpYHpzsxSDlXEIWY3QzMmVYzziuvpVcVD8IpplY7lMbCJYY636F4Qq/N7MWrmxRQaydewJy6T3RqbMky4er1U3//CGe+3Vjj5T26Vm6H5fUD0CYVyAS2eZoRsHWNvkbvcqQWcFcAHnMylhmsrV1alumpwRoDeY9ISnDyImZ8FCE5b+17uX6E6wYp5wfAgyIMHm5OliBNqJqHSgt+0wCetUct/n8f0Ug46b6TdglHeu+SCW2HKyszsedhCl2BXefaLUZFCRJV+eKKKr0p1Sjd/swHF7Hv6p28zv9IZGqfaQfOrDE5MShIppiwim7gI8fYDt/f1p/egguutGTQq/wMNAl7A3Jpb6NEkCF2cICoN4p6Dzd4SZff+KdkpSoBguNsfkoYZbhHm3nKz8fKJHcHn0gWbr8qyfpnOXPVUTCEuJrI7Bxh5H/lQ3hsf8pcZv6xVl4s9TyqSFwPtlwhSr2FINfwVfFocMUsIWIDNRZq4olQOHc1LDfJoYEmYOBdlukUNSaCsPaRFFf43CYKAgiuKrl0xm3DXSp6xHpi0U9AxLxtsMROl3JUsis92x4lNAIcnr+Xy0mtJYV60jTm0AnZypV9/Hy1RcEGMTB3LJy5io36aPUutqr9T+8pCi5zjg/C65ibUHLACJ51uehLV1ACf3abHgbUCvSSgmahLZzb600gCBusZ8fjJONcSTlvdf7Y4sQwKDYQWlMo2YOzrGRg1HryxKv/rKIEOTiymKPHPMFK4sDMSu/TYx+omMFZDMfSQgPaUa/KUWSCEzs1cMJ3ocspc9LA90HxerQi8QIMgrN0b+4KZNc4LG6gFLCU6dL+oA41B7oYjLuY6RAgYKih39Tvdto6zNvAdLtgvuAn8A2F4WhPyr5uKnb2rJTZxWqSdoOkmF1ZrpDVlne3sukEJwkCYzsLJloccHDzeN2OsvxxPc8E5/vG1OBYI+YUqx7+C4NLayf2FM1eO49mIRl93hIEfwCHgDoLQgItQqwI1JR832t8pDXOAql+M7fWw6nON+W3hdcmX0Q3WW0p/1eV/nwAphNmkew/fm9on5RbMOWUuSmLEAm87/NGxwlJ4B39HH4UItAHaZecHso8jFMDC7f4K/sBhEB0wqPW8xCDprDVWwW0CE/Iqr43BzLTWbZT2bYpxxDvosSbtkRzMg2J8E74o5mjp10R2VzICSGy32EaWfIbYbN6quExn2XsECZ0GPqjyPcsCf4fnBIioW0+3i54REr4JJQw0FGgQvyBHkX5BlnWpZYFaqkzjaQoYwb1R29Yd3tE15X7Q1OLdroV4jtBGuEYT7+7DlxJxDbcN1Ve2vMEDIJ7eY16z6tjQAAX3cnyi+mTt+2NBCeZ7eOM1cggbjHDjpiNEMb9V14AkI3rLHQyHrWGAelexQqS9X5e+DnhCxlzwK8BZeaksQxlpPFGrxjsdaAY9rzN6n1hz7TdFADMsFjPZyFe0ShnFxNuMHpFexGxVukZ6ZWuWFhKzhvGKOppFDExTxKD7UiALfUJXoUCZhRJGE+FMWEjYxggMgmI1quO7oh8P2YeXk8wS94FRlUfZVn9+mRNKxO5755x0M11Z3zwX5F5Lo22sZci50RoJiMpvl+UnZ6pocz3J+v0mZi015WXYd5T/xZ7ztg+eklrbBBsid2Z4yVHcIX1ge126IglfHnzNJHtuSKhTLVCi2VXWGYPb117Nh5YX/tWQ5gphBXDvNOGostgve1gcGje/WscyzuXxZQdR/pabca4/DQGNjbmRnZ4Uq8McNECyk+xOVZ9shOY0jQr05rq0KBQzaYNlwvOFVnmroImEaAltLbColTAYlyiXyshNOKZnOY1A0YHNgNs/ZgbixzM2lb9YkAzdd97BQ8wCopatJ8w2MCg3v48JtFnoqWxTevX9X9yH+AS6kL/9buba+/WT3RxoGoqwzV4GEdmfRGzI9k6AzN4OfJJNLpoHlHu7pCRSbDB9IYLh0sVOCcl7gVrj2+Zt7PvtY1VEKmiGiYvyLpnDAaUFMYrugLzSMM8a/b7ZwZZgR9Xqoca717PPgYxawg5FtJkRdnPYI8MMbucqt6kqoItobOEAYoswDcHgQER9n+W0PDJeZ9bjezvC2sxSL6qGThCuon5flqKzq/2WKR+oXSnJFYrSRSZKynSLfZ8o3mXc1yYECHBuBv7WYs90CZ5mIkuecdXFojD15XP+Etph0E1/0bfcG6oYC6hHha1eGj/QPeIgEtGHhjUkFr12ZQkHqrhZoGKkR6uYxUImKMwwMyy18zLa9coJ1tFh62wWOOLY6+uSVaU3U9VSRM6806y8EUjI3d+CfCQvMj4g2gOGXLz8ULxSIMLTTZ1G5GawTukwh/YPGqkkzFtKntAg1cVcp97b9y2wqrMkiFVajDBDYwgCnjm4eho1O4C57FyFBlgN6irBljx9DiFqF1lSmldtHRn/3LJnP94qZZIS1loVMG7RrMTNUpJXDKGJyJ3b7Yh8soBhqde6tFc8IjeFU2qItf6aXG18iEPr07p7PcCLfbZcZbRjATQ3L0wCT5qSnzDguR5neKAa9KDtKVXwkgnDks+aTo+Rjv/Mr6MOCNFRB54+EbMuCsAewNMpAWGhdha2eDQWCZlbIpH7JKFh7qgFXV5MUUGeBnHRqkgF1YkMK4NAYUtEIkYmjkerDnhBmyk65ATX6DoMSw4oz7gAF/MnXnjBdCwyGRpkW6q9M9Sa4SY7R/dhbmpfDDKYxzrluIdjlcmlXLgWNLUHNi10hZFn3jiCVh2/zpe9DDhTO2ZGmRzgKWpDp22E5GmIFGBp7yBbr24LN6v5yYjEB7xrfFQ/TS5ejxfNoIIhmAaTmuAkEIiaKRLCjNjy7mCDuLYU+dfXSEbSObsoWWByvXbrfhyc1L+Q18ptJrTq7+dNuS+zbOsojlQTYUzfJvejpqghPwZT4yRdEUjzSXsCnSXIASzrKZk3RcOBvpBRqbEdSCbhe5Tuxsa0OYL5oz4DiAbtLHBR/vws584krURwq3qX9jux/90e3t++Pg5KHhRiiJxzjzph3ArJAeSjTFpoJlqOBASf8rg/i9HjijBi3sAnKPo/HMPMJGFzNsjja+HYJDjOTNqpscMhJCATHZqOU8lLxE0U94/hSzfY/1clSD6EFcaDhd66alrMQbzCjKnh33AqJSp7STjTdM+ZFzRxzSu1yHtncZR6G70J7GDl/IffG90fw20LXy3HhcC5jM4wCtAypohTfhBUcp36UO+Izn+TNhfv0xy6uZqZHGXR96BRPcLmDiOVQhUaGsot2abZTk42zpmtpN7Udyx1fnhGY0gXH/wknVkc+QPPacXf7BReEsgaWxMFA48LJA+u+1kd6txDlYp7IFpVq4Giyq93HcYFzwclxbcrv9kNw8TtcABvjMxrVoHdVJMe98L6z3KZbmKtnw6dlo7tjpRs7b8UTHEGDDlpkrzUbr19ucORXnEdtz2SvaevvkmZUHi+34uUoeKZiWnI/pU8bAvjRtEfLDFQrqLv24dR//vO34skhbzuIZuoqOJsof+musXIKe6uYH8PPSvMCJRZaFrlTxiPmAWMhOCHmIL9+V3zYwLZnqxF+uE1IE0vhIbbTC0qHBJoOsnD6AcyTzVVMzPpnjUUyiR76RU7zWZOso+YuiQYlBNTXVgSThXcrLvtL76izbRVj2w1m66mvs0Xkoas9/RaALLQJ245VWY41HJ2UX7Trixc12RT3GqAUL/pfZ8AmiuVBZeagZsQgpLsugh55qvZlq0B0E6KigawLmlayE2tQDfzSsrC/SaXIA2/WBvkHrXGydjLVILemuFzOSTZD75+s6hxvTNxQmbdpK+DPKmKL0fGj8gGR1uokHm7yx2vn36g4+jiV9pgCFRk3gp2PtGgN/gbrupNi0TnDrCrKEpH7n4fDviDXyk9pcyrdDc4uGw428r+L3ykYV5q03p5P0kn6Eks0rLaaZo3Fe/Cif7z/247kYt1bMo2GQIUbIYoKEthilf7mCOKd+Dgc4BpkO6BsKJL8FZNRc02CNFafexDyhR6bv6p+Xbdr3S2WgRvcxEgxZMP9TaHESARQ+BeVLFGvpp9ytsGP82/pVrNSKPQzZoDTXEg5sOGAFSY43PLT7Ynf4zAbbT8bSROaaML0GpWTxrLahO1Kd/tLcRu0QIdinNSqs6SLRRETTqlzJqBzVIIUYDz5It4WZaxuVU7tLD/w0D+Ls5Gv0m1cEsebq4yhBtWUpJGO/ae4+1z4oQfe+eWx3dibnwExYSXfIRJMZ6rIbsbJgpZU9GoCsrvragc5STUaWaD1DDaRe2wytF8I7auEPQTW1ib34FtTfio+MvNMGuRFc/hxzsgswNpuxE8a5Q+dFp2E5PiHZwjpXnSVFA0IkYOsxuK/ZKNKkottsInZ3t/sS35Uo5WVKexNLJLtmA9gFpH7bQiy2K2tyLuHWGKkxUBuvK6rVCyiE3hXwzbb1hIGXD+tRqd+pSXTr9CcMDgKxymVNcOrEOhKNIR+82vmWkbNhPa4ghuRsIRNNBQqU2b00ED4Xl6vGDLX+H1fN5Vnu0GGMNso73u8aCeHHjQVm5GuQfl4kCl4chXdcP8ko+F8VtXUP5OVLbWacvsgmb91AHkB8SmlWy6CT7lTyTVS/ru40m/IL187OYc8kxLv0oQYEu92duA9Agwxo9frH46afO10ZZGUKCa//OhG1Jpxp2k7bhrH4KCtiSHEskaG7Y0i1av7wZwPy7ESHjIOotyG/95Ze/AECv/a329P0HJMXex3IGiBX1mLsWBhncVjqUj30fofM5kSnl5L8b4n/g5nxHZkre6KuUItzk5eXlmHE//6nYF/5YZ+UOzApDmb2J5c+n7H4PV0UnxbmO+7wPSgg/mcc/f6T/5Dw0H4Uk7wS1Vt5M0KU7VocC/yeAVcjBpa86vYjZGhDIgcEBx8BKBGDhOrSQ3f4uE7+b+F52wMT6MQ2R+xHrJZK4FtfKKBNCk88ebuYZRJi1MCxMT/4AC9z/nq5YZzVpfAw7XJVl12udXYuw/zoyPLz+VGhdcKHkhc8kuoPeLp8H6e3YzLBYmwE0ahiYLvNhEYemV59pHNC6Fb0WjhSqwJrCx1mzEu2p9UvLhVjqag6YNX4MigbG8tpbfKDwC+0Cp3GWYzzpLgd9gGTDEik4umPQh98LoFJPNy2GPxXpvmXfiX0zyr7k1Pi9ZEDgCxhs91w4a4X3+u03xLhitC0QJQ0vqzM2h1CG6pz89Tn6gRCvcWjXi+63+NRTLnd0w72OVW6bjo1L/SRlpRFi2TJQeAas1IZgaV/XvZnYDgWAdNONSGF22chOYqgJZLfoIb+ranE+WriWo8dhBYnq+SuKEqY1JaTHthk3ziNZH0b7eahT/WVGfvbBXk1drqJBaN4ok5cuKCULgBnO7KgeBVeHFaVBfkhVix/TjEr7qajEbpdFQhs3aNQJC04xhCdkdDMAi78ZMiFC1LR06b75NwvUQlwclefCyz+tdcvuMpdlu99Mvv4e/gK228DANhHIUpctkOrypvSq8TawJrQhR0XDkyBCp3ljhTLQrEopghBEHA3b5w5QGPcydEIGxbxB14XIy386wBSWkjNBno4/as+IHB3ilyyVF4QpXHe/LnXXF19SJzlac7Qs0q6Kn0s7BE1VbMUbHTboth/MrL9JQTQuJO+6Fl5OrFMUba34BuoMftKgfe44B4iThk233orL9LUcrdfBHFsTYf3kzH0hS18YvHiF0f4coYh4MPolShN0qYsHiahwtWAdpr7LAJTH17JrIpV6CyARAO4o4HDrBNVckMqD+QvVpbEeOXhdQoIoWizM89oTTPhsd07V9uJqNb7u5tdPiStCUNrlzQE8MwHv5zUnOYHcTU0qzhzBoeE9ncjH6Ir0xmeBjAIBLEG5JX6Rgrtl1H07whNCDRJvrfZ5d5uz7nDxYuLQJSTvJVveEGIn4vIJGZgZySXcD9veTVMXlOLqudjBhCzhPon2bQS6aVChEkORlcPhrGuNoD+2ZMlITF/bMqWlsvPFTR3NsB0YAEUf0WvHX4nUBW6mEudmGnXxCyCbxYdyrUXOH7ijUYVB0MYawDuvaWvMLsindLcFxIVVUhpL8Jp72tK7k9a7J/Y99hWnGER33efCoEUb3vN9Rz0xsKN/XHAiFNbmdUiV67bZ0eDJIdZtX9YRBFCSPgW3n/rvkhpWEnvpgqoca6FueJZ3z7JUWTcU43OfPq6tHjcmFGtx/cdWAc78tpiaH0gqbzLwR0I0X4jgfZoPzyV3mnx66TrRIx2SfmsA1hq0YrtGWAV7sQSJ4o4ZdP1R/l3wCn7LoJbuo7XhRUhUv8JcWQRw77T9x7F4rwuUv6SjyMlHRzv9P6tduCAJV9ksx7FtJdid5nPP+k/fqpFKgJr4wiqhylQ62U4ScPK8e0nAuR33GWK4WwcLdDXS1VOEK6C9C8hkh5nUPihccmkp6mD7DKEFelR6f/oGSH6zYo0xq5SEUmoQZ/MBnngMK9i2B2KX0SiwdKahbaqZgqO1nnIpIKu1HxkNq8IyZs1g/1W/1lzqtlJKFw85C2wYFWXyqoj+v61xKlls1qcfUTOBCNdmx034u8SDZ771AHCZQSGEdWLRBebRpcvTeqmodx5dTT6xRHW2qoSshZzd1GqaxbbL0NtJDtpa7blf4Y7yc0FMcFqBErdiEFDe0/CiBxlWr+GHMu2fjwBusNS6GbJFIHmVvoxeXNrOFa+2F9HS6M0aAWqN/5i2wJPbiau2t6Max7z5obsZUwTVFNcod3kTKQYqpTeqcTUpjRJQT5SoFFT08gxefDrEDEtoWoHg4aVn2Ep7FeBiF1b6IJx1/z40Q4/C+gBnMgORDz3SGTR66qdFJYpb/PQfYqdJu0NuRSriqHa3c7NkvAjsebsPJ0LMNtgfEC0HBsyVbHiWc81WWIKyjx0WvGy5J47GdS4xBePj/TsJYKNvF9HJTZv2rNG7Ui77NV55A+moaUCLmvCLtLXgF8OU8UDvbuluv6NUVa+YpFCvDtPlOzhsM4ui39Pfsem/06h3sYsmOXmC6EFZlU8MSkLlIj/RMPTU2MEUC3CM6HClgUyOC58O1whrwSU5CpQNogOFsmygnl6C51UuSVaWt6i0U7hT/1WBzoFdLPoFxirGc87KME553tab9uiiP8FcxGiLwxhlJQrkaNm2EeJ1iEq7CPEelG+vaLQFsmwtFb9rkwYOe0DEle+dRuS7/1/G7LEb2qcVlPFFOZbm9b4pyyifO0d9NYTbFrz8RxJx2IKNjut7hmtysNteenggec9/XrL8w5aXHI5tFNJZSKRSlSbhNUIuMgiy4m3KXpxs1QLD16tevtjNJbYuN7YPqfx5LsZEVqfpQge3E0BIEOHABmiYuDECD0I7qrzVOk3RAUg7tEBH9QhOrjj6tP1AHXk139XT7ifS/1ECIGlMnJUDaqCX6Se7tumyP7F1QZXJriQtWHZwkc0WdTmBIwAu9H+OzYiDXV5em9RpsP2Stx5VqVWx1m62Yz/Ns80mjwCHlUuaUvns1RHLiSWRIdppOowT2cyNXz4nydrl+3x6bFpcIuWsB6YuCNBH6VkKnt6Xd/RJFmuDH8t1zfLge/2gFKv1j7UDSDKspFXh9NssosFRebhOXgjfUxbVVdJ+jhKfXpaDJ2SokylddrMqcP+/yIfUmhHXjkZvAq8HrPjMPZg1eX2UdAZeVTjW+gGBR1mn1DrEx4LLwwB/KuBGpIPWYZfHYEUrWrLcaVRndftKDpbrOrvQ/towpymQ4Ba5cPbxipwwtQYWOlKTUJ1Jh/W+lX8ktjBzp1LkZaOgDK9c06ZaEFKfmGQJA6VxG8sX6F5cfksAx3/SNjMDMb/lSHbHptKkytZRSjzrm10rkkTZiSOkZ0/VHkO2kINAmXFnAlYz2SI/QdVuN5uy54d2B6KQg0S9m+5aDQysyDE7B4VU9byAm+5kKIWolvNTgIR+WGbyCy8aBjYSE6z/nhFK8DXOK4nOw6pPo/giQhJuBi8I1VGGw+mjWEdZ6Pwq07LVsa9NhitGxKt/1r5JK8dIZfHuCwbGSoZWV3NVhMsoubkZkVy+8qNd9wM2K3zw5tHqsCIbx2Vb9TdlHw6IiGQCoJ+drHCQ09tO2SBAjuZ0K++DNjsyL91ajzUJOzyI5t7Blsq+Jfev4mbHseeTczmuIzfy21SF30wnnk90Br2HbwGLfEpluHXBDE3ftblpsirBirFGkXdKM/P8J/PEMJx5RuNiErStxku8TLhl5JwYcj0YCGsgrCSydsmZQNxl79RE7Y0sEb4uHeWiEiLsOD/fN+yiU+YUU8H5Xn/x4mHEneeU0kNIl3cHkGM52plQUiTJ4iGJLbFhPc3B2oR1Dh2YVnSPPeIL5ragtq8C5SRarTiUU3+RbdYpaeIGf2IHkmigfKOHTFiao7Ei1564uBalz6kJ12fTZ3NmeKTf5/cmBHmoc17ybtB06fNCociRR1qcztMqCb+ZfKw+6obyI7YkAaE4t4hbCLrzrgC/248P77OKfXjsaELfIcHdndmvH089ARCxWauTQf8cKGOMq2df6OhCHXcKQAiuWlIISEl9+L2S4Z96RPtz9v5yKlCZWjA7tXc3VkjQoVN28PrPNH16yuMyCPxgqNkajSWmRNNVkUszu5eivdcma4e0w/xC9hSGGuqY9YdNxXrCCAIg/EUjQ8MdzEPFn37EuzJfogn9Jsq4w0ZCHIL/f7Mihv4IQXFzqfgnTEI1j9vH/X62KNsrEXOJ9GBv5rOM7WQdx0RnEj2RTJBFxDt4i3jTg6y4IvggVI/PX4FlWrLcJioOZfa1fWDpvO3U8ZGCUNz/xlVlalWq7GeDWXbZoj90Uf+oAq2joEfHkKH9PW8HNurHYKg4er7ALJeXG3tQdXEGE9xuFIDI7iLQ8BCbtQV/AaIl8uLmShq8J7t69pERTqG1KNRv6pAvmeGhl6JV6MMNpKbl3Mxhe7YPLZ3h1hQZKXGNGAldvbnOldc4JDO4o3u2YilEJ2kFLF016LVU8UQi6T915fXa0dn+vHIJEM2CQUeC56fY2MOxeChqV9qMXjC7XbfZCXjcGB4fk1iM6s8k/f3VONEL8DTiI6FNYpbL7GVUo2yNy7DNfCeaamJm5o68/Giooo5qxLesuN2Sf4uIdmCfOwToMXudHkeelpEF0Et/uOZvJUSeEm+3gKGh+/dtusG3rQAnW1pzybOpyVcawCfpvkSuqUW/yPhLEyMcxXBOqV5ClpGUmzd2l8oC30691e3DROAQC9vOzSPX2KmQhNDJzaiIwjOOZ6w0fCSNM6c0gf7/atkw8oK7NDkucnNqCVkFvTd1qYMlOG699W1dJ+WMlDAHYqaOVFlXEE230maYEKFhuaeDtWri1DJulNiPj07mBr0u/l20UHEJA6s3XofoYEQfH9ZbWxJyjhaEnahyfqTqmXM9Ja8cQcdJzSZhVZ9wxdbyrOq3dXwwMYHRVfsJc3qEVjnOuFiHobhm4LbVFPTJX9gr838vOgtYaQLhHWTMAKvPE92LzWJCyg0ak/wd3tfIG61iSvTGGclyO0/5Z859Sd0MqLnBC2h0i7hDr14nkqtGb/RvAfP9EQ61qVacpRjPVClHJeRQAeQfSSXvLuVBwdr5rueSECE+lNe5puFXFiaVAhhAK1+aS5CJqB38H3AzmbM6ijSTFrGHzuVudZwuDammPdwGgI1t6KW6z9tAfIapS+9HcXXKZVVXJOu6WmWDAYsQPo4Su5Xnd7U16Q40WtyYcu7odHaqj2dPdoeYjGN5zHcjanJmqOyriwwCyZ/d0iNaCEnC21nSeF6qhabmJEEp443I1nB9DODl70+BN8focpDWI9gBXg8gu5rP3antOYke0VgUFn2mDlU5zbvaEi6O3Gri/mTL8krdBY4ZO3cIJc2Ar+iFbwYAUBS/HpObramRB3W5ZAZm8024C1e4b8XEFGaE7R/7fZFIQZjXgM747EZFJk2aNDLQBtD93GgBLrz+eIjBix0/GeSUuTH8BVnO/28y2IfRGIUcF5soOFuJ1Sus6WwVs0gwTwy6kgvVkNXVWaSCMpB+U8y1voA8FHTpEbt0dgEhgdCOzaXgx94w3ixVkhOicSqIY82AWcjreCJGfMONe6xVHyVpIFHfVqTra5tq4pjLvRT3YVcq8kXPejvFCteQ0cw3smyLzoXveZHoXKm9mbwJTmIUlNyZRLIMhFct7x+jps7UUCq95P6ZiWcZnQoDBdGel3wf0FYV2VKhum3eAz07uHj9sLcwO+o3ElzGLv+8iauBjeGM8ldiMhS7FeR4eMYslj+vGiEP0RoJYjpeLrOvGHGJiSA+zPdNPcwB2V9tcc5zdLkQnX765VfG5IX+w259zqpEeGDHXAnvYd6BJe9XXCPjf922iyv69HSD5sXaEL4o/Qnpj986ei1OCC9kraBYclD3cJAOFpaVqv1AiVJ+ESmPHeaiZY0tm6UO3vWI6zfvX0bxil8colWG1j1/FGTACdAl89YvzKCwKAEVRhgurPuUGyBqVrEUFow11nJ67TcbOwAuwtPgF0xtYawd+rm08iCsVnZ+1JnmR7GL2XaPx6AYbkLLR423DV6TFoDQj4drFt3oECjWhDrfcELIK009bY5Juci/7sSCpTykPF1jiyxexXY/XMGcv4i4zzn6d40uPAvRj/ClHenaqtu8AS7jKOGHozYfVxAN/NW6czEPdBRxgQLzwu1FvjShNSCZn35Lo5qT5P7cqk4LN7tsSFmx2uuBZ+oP080N+Ce3areUIAP8iL7p73F2gzr+/ExqNuPIh3HQdaNajF+Q7O+BlrSaO5L36QQSr9pH63C9XPeP4kPsVfTL7Cdr3iYbMw+S0RhPFkj6q8eMSeuZcdYOfywJu/jcPj6BXlxD9kkCqiI3bXZqdJoWsaGma2WZmYohXDQglII8UE/pS78C0/SRvRAUECE5nGHgP7byrvaCfjUVG0cmnTIgxVQt9wn11081FyJBUqYAEEvvK53jh2rySLB3KnnrNSByv+FxAGcg0onxm9jf0egl4QhcyvuYvUcccW51OnMRNx9ruH6ipxH8k4KTEl5EO/ZTr/x/DWEJaUiCiqa459CO4SPxjuz47bqICBy9Jpwf4FD3hDlT0UjY1tKZ3oaOg3qRBMuxD8jaaklisafR2qG0SuBarGzicazDLmGvgcW9apSW9pSaarqgYPJtbzj+d4C5PQIq8WzrtAT3DNstlmVBPX6aXglhuiQP9gue6j+QGEceoGzOkiM6tYatMYrjsckL8he56deYCSERidX16iP82hCAs0I/FfFyIFEhCBIZLttv2FgDdcH9XIdHQZ/jy695pMkNxMpcNmRbOiiR3DZ7cJbV7y1r1L5DG6Ndn6PmUppaiSfCoSz4DrQ8C9TvgW3Qjj/V8kMHfBpF5MjACdSQkGaN45xaR4qkTH9803GARyelcKYpMbrcNpWOjpJc9an2ASZvyfGXWqrFw0iv36l54ufEzTnml9CPJ+DeqZmn0KHBO4DJ7lv6M6zF5mZ4ZhqQNl5+YfzKZ5Saif3Uo06zGg0cWeuGIdXvMGxmvRidGY2Wdosa2pl3a7r0Yl+9Z2XXXRoVbM5znM6S2C46Z9NzJKd4cf+kGd7bapz10E8ftpKj/tNz/Id1si5+7q5HUV3HseoM6ud9qi7xMiyo9GFI60OzHf9NOD1kTwgKYZKYXIgoSsxMYYy7cm7sogQ+ati+UbAHHVTzAB721DnMxeVYsnvNElaCtApYKE1bwu6DzkmNhLJRxLKAUWXi7Hdr52q/Pu+MTdf7cLM10m+bzRtgvXpyChE4hiW6VXH50pyv5yYL0r6Uvc7yh80rQc1uqwbNPi38qDCQKOBzmg9QBFs+IbVDMGPud5tyrvFyHZtGgLwJT3tmNw64hqopCQSSzfltqy/qh63HP34y8lirEQtaJrRxjKzGVT58UACenWQT4EWzml52BrNRy4NlvPeEptz4bkH40XI/F3bxmuEAFuYQ1/Tp65f2wjQeUoxzXh414GGlBgQp0a2fLZL27EmLZoSx29Xizn4ODuFGL5/Z2wj8PqzDUe20lHp+aRf1KO76sMBhxBfBtf8a3QfHWDcTVLdON/LRab0YS7umajjTahFBHbBmvNSq4zf5hEpCm4AW/MKdAgMYRwxG22TU4vQFcms3ShMWR7EsPhBBmQA1zc3ieG7f0ZrdR1nGaBTjEEup8KfUpXaR8R+dPgBPOZCW6Km+kluOvZh0pCnJvsF8Q9k/P2wA88YnW/Pa3y1ZRDYpt5AFarSYFKY9CahHkNIZuJTbXCCY+ZXzu8rSIlqXFZrJ0EB85u3xji2IprXtjy6M+Wc0O4mz2wZBQCCOWRtZ8hf8iJ+4cjAL3HwyY1z0303sMScMObiGlimulTn33TqjT131/BDoYxQuoSklFn9vWb5lFgik6E8KXiYb+HY1zm35vztkdmuup4jibaatM95zdGvyyZKM7Cj05oLzT7h67ZBINyl0kWoxPmqFPmH+O5PTTRwhM4S6Znnka4g06xKaarRQ3pL2fZNUAOY274fXLpoCTuA3gru3Ce/R06xLVdLOHBII/tsyJztVuPaKRWjHqxkqTUyKTDQPb2dTLXAJjOFh8O89Ywtr+U5hi8Q2IwrpUOVyDaaosxDiY4RcAuaYWRuuidlGZzge1rekFe3wMhcgPzvd4+yivLFrPRzCdkuRcYCozog94onN+Enz1Wg/C90wDqgIqHLYDUcqWdmvgfTIs1CwQdPNxJCgmN3m3lZHz3UjZhxGs7CaSllvQvPecZdl3z3tS1DRskAiVIIHT29CObSa3b6k13MiFRVTJkRZOtbqY4vf+fSdLfQif+j/fKFmWZ2eiz0EwDi/tuYP9NciapIXvdScHe1ybXPF6HaEbBCiC6xj02xe7YBM9SuCgMl1Hw8lwCIOP6SBTCYM9WWcEqXDuDmCDQxifMfFXIqz2p0FaNuy9DnLyGbuGmp69kthZtHvglOG147I/5zL8K0njBZvZBf/NI9QKuX7nwVgeYB3D+YHygGec3LD9rICBLU9jY88jC4aSH0t0n8oaHaQryRqubOf+3mE9vWYE5Tt8QSudzTj9xEmMHi3G7vEqW66B7rZu2a+c5e9Hk/kkTettaol/uNymusLVDlRl3vC6ePm8c3tNpMaPcmmFRQGmtQalJNQcwwSKREjENj6AoTTJFTBuO0gjVJrg8QMiWB59PlSeQLtwEOks6vPDmEcsg4NXUD7vSMw+84ruR9kjBFzfBod52j9FCTF16+GixNDCADVUJjOLDbKayHkGzBgzsBlTpiJSOVDOOGFyrUfCDeUjxxJ0H2Lle8kp5euiVmTGa9L1KyM8MCa0PXgnS77GH3Rt/rfMNpO8+y74B6Ihyu7sOdEhOPoQrtf5sHce84ZZ9F7iVQm9Yi/iwiKsXecAAPiKX7AO55CxB9jKI6IjsaFDaAoSdP/RHmLR8kz4ESvdRHXsxISXkZ/Qzq2+MP5qZAyWFIzHiFc+JqOVbxvPJXfowtPcbSRA0cvdmE9zv0Wjed+Oj1LHdTPCm4EtaDqIhq/onEWcN/Ga4KidPqsi6WrQsyWTqP7tfh4Plw3/Uo/ECkpHgPng/Naklei2B358OkVhVaYiVh8r7PrfRdEJdJdsNw9xMeztVVazYWScvsYlsiGRdHFUqg3Kdj8NgPoljm23NDPY7rwccV7DydYTIPTzgqd0zoa04xrsDWim/DfWNpB2q5feefNoguNE55lXrk3WxfqP4QXKslweEmu4oixQqQPzvBmZTPxfyrsnXieiOR5aj4UH6hXhVB5kkJ0ogETxzg1wkyoeH6rkd7srWAc32Ogyt5oDfnjxC0K01oh4f5QWDNw81Vl+YC0F4XLOSSmAMPEGtteg+rQlUhkx4PfzH4mXdD25SGLw5CPdW4KIFyeFRE/TOX24O+zb411KZVTnbBkn5R9dRwJlUEMDxqBHW0oyomZclfUFsOd/6GbGt0yG9o+VI7VrZ6s56acOaNT6WFlhOtzKWX1MU8q3OKXi8dDt033dw0ovYKJhPuPmExnL9ilKn9E3e1trsVyEUWUxLizbezi4Tbi2ubwoZs/msQ+kUkPbNiGN59Za6+ijZKCsCoW5X6IBJlvMvdubW787KmPMT6d79U66CKY5HaCXzDTn17y3tQE8y3y634lS2jnc3A/DqJt+aEAbE9uAQ5o8HqGozpXOgzm4hiI3V+WHhjXFuvxxB2G5lGIFwZxdOzQ0EIBp9w5c4YmU7OoGfjG3FnkKWSZq9iviq6LkovwzPUJP674saPn0IsJRAz4s6AlHRQDlbxkARJahxesHveaxBidXAeyiqx/CRPv318ZM/GejoLQZg83wpwtphCaWK+sYfIKfRtHkL8mso0/7DD/TV/V6XEcwpzz3qaSc4kYTgOg90pIKhrtYLIGUWTLbu7Alk/GX9nacVCuIA0nT0r9e9M1pZTsO5Jyg2R0bFzvhCA5sJ6+2E43y7Sc8cxuLi8htYakftPB/CyO/lrN+gCgCVeTBHukIcGkh4wZtYZUBsykWaPDVos2v/scejLmA7O20jyzT0f8NYl3eWYrlImYIgo0bvJxLeEr+J6ZUioAwdLSpQwf4Fh+++D9DRta04ukJQIrrfil+3bKibAxWCQpFRRc7TZfpUJ02vzhnQgR9n8FyXwLXa7Kmq6KSFKUlQBKA7tzW3fpneIi38ddkFljxWfPwe1MqfrJ67cDk+CmOpTgbYlgsdIXqfP0kMWoKnQ7j0gL0RIiarRz3jwag5LpOaGUXCOeo6fA2r+WDxNBUXd4V2UQyV8AfR8qunzdgFZD9yRppAB+dqNnYXAeheZNO5nRFmbQGEOPCRCA5Y//SjZI2kiC0unpl8zZSEVIzcfL7jTh3OG6CkKtlK3/HCvOLKDGjktpCU3PF65Co7C8SmvrO4E5EFihEBT4ejB1VlqrhzD7dGgFfzcCEW8tQWMC57z5rlgiOiF8hobPCss3MkEwXf9y09k0VdAuIXhmwETl/B5fOHvpAn3oZxF1vYO3dmNeaQU4oqCbjsxC91ddYFByjKfX4q80ulWXUPYWnjhyLA67oTrb99HTx/Ulnx/tHmPVN3JPM1WeKCnESIHLvUhwpoc3I1ZkxUXh7Saqj67OI3+xHKhd1dVJH8MFFwOkw9iJ585temXT4W9bANUWiCz2dusS+yXCGP1mGoYc5OddRvQAIRP+mqDuGMrSn1GxatYy4SX3eG78JyJuv1aSJN4DDSczfHEACTKzs3G7BtQqFb33LhcGSGl1A4Hcac0M9eXO5/mHKkE8DSBtzGXq+hp3s8IJKNsxuWnRpvFJNJmXzNJ9hNYQ87u09elMdlSwl2jIKvLSGARQcUl5vz+mm0l38M83sPkHnZ3+p3M/kHD9EEfC+ZH+nGVfLcg6nU8PvywUJd0ZQ75uvcLG2BJ0KhdLqrQPv/Yx5snH0WrhQnn2pbvRHbaZ/36tZlpv+9usWY7IEXwS8H2LZE8FYruMLtus2c2zBTwBpyDIdz1G/gK5RBJaFd3BbHi4JgyOe8ROSBV4e62WK1tm7QJBW9vp3O29ZK6WVda8TBA03SzHXLHn6KniQq1Fn60/EXlbbLbJm7UsHB6gJNwXz/xIwLx1EwlPCJON7+KLKCHxcDU76DrCv0fSSPHfGw9QiFqVsAlJTSZSF3ohGXv8kb+Vl9SXFNxj0KJ10j7/lXgdGTd/0fj3NRi1pf4bWtL5u7LVoo8QNmiVGCpRr0d5XadCyqUoQgnudRUNf6GVhWH4MmF6+vG2Gm8RfYWKAySAXMH4OzJooxUdWVXf2gVyEFO2efpj5sYr1djSwiZX93odY4bUZnXj2iSMYjrszRwmagiHzkTR9zmS+AuhB97skCSTAsbbF3eI9ke16o4B1U7hEWboKYoeUtAgsXufvUX+huayuTTw0pOLKA8FgWPRoTtmREyzTCRb4plCd7JKUrfmH8AndtGcQL0gXwyFygRMrS5yapkatiYkwk2IiwUHHvrmoMOvPkWv2waZvYKEeTKo7m94meUBOORIFZkI3rO5CJ4ZqKpgcJvQZwiWtT/6ke+GWSP1n8VzaIq/o+/gJhK3zoU+MituWy9JwKJiZ5l3Z/eQJQ3ZWzi1+lzxHahL5kdo33HuqAydMAnIeB2W7arUcJg6mDIPIapirEOHlii2pq8o0XFVlgqBysdI+o7TBIG3caCqHvHpwrmlOwhYiq+iQiF0e+s09ssuy4lwfJkADsTY1O9H9/ZEe8zHFfp9yuMTZXTVIr6SyDVjxtcNYz2NuJOpSo3PkSh1CrLF1Y1q8tnwuhc2c0UUhzpSM2A387PQkz6Qyl7mVNgY3u3q0afXVTtyv+8w7dTqL9PWp69QLFn0Jgb/hp0SBlUHcJB4x9+5jqx7kk63xnEfJoAU9kQ0WEjpy+ub6aDR8wB6y2MtZBVtS/eIPNU88Ulhh1CPrRPTSmVDbIrs4y9pKfGIMxzBuHumdpr8vDNU7lQV0FobHmb410jFc13zu/IRM6sy6cvVLCDJ14lM8IG0pkjwl4y4kIzcUDjRaNdUfS+MySLk+xXomy6twUU5qO0IYRuEiH8SGgYf6qjVI4mrtINY9lg8A8bfG0CZrtvUkVVOwsMs2pv9IIWbc+KsK8/xjjynTIa37/6IuXee3OQVaDCkGMlZltPraaaRIPWynp86SSQcYCMetrclYZHZ5D1s+Mmlx6hlV7uYVXQksHsv7zmAVh+wQiuFM0An7H97IcC4ZwztSEzV6jjfSNDiP60YTJ7o8kTYsfNgZgsZKVwCKsm9zdrvTaScZNVEt2hNVJvDW9ZExx8i2vVsONv65tXZIEM6YQzmkOLJoyMQxok2k2F9Hpog2bQBK18l8cmyEs5vaCSLqYSegLUS9YHo3nP8y2QgTfPJ7RqM3EvEFXmx8bSIyQUk4JiXEyXX5x2/4RMIW3+vSz7qXtGvQKfePqTW8w6JPeIxfsmy/UQsBosRjGYNky+SjuUMR96KmwLsGp4eum0lC07gLLjpX3kUp+T9ZrkcN5uECbFvaP3EwjDGTi2Ci2F47zEpQHruVuEvA7lbWHolvYTdCjfGDGzipQVpwPvDMf4QkJ5nZr36ow46ArmxdxNmJsxvh4tmNVAjylFNbwRAfjNzUEGGqVyZuZmie5OX88Ktpovl+O/Y9KB/AR650JMy/c2Y5rAjjkPXIbk6jy7RUitBsiEog9LYS9d8Z28e5DrwK+l3GIMGV9Kp9HzzVF4pCoVhLPpAzICgqkz3ge+8kc77FcCPnxW8RG9nGekeLBsQrUaco3OeH5jkYREfSX1qAM73+M7IHAxAts+t7gldZdtWaVGWAOWvwC/YhqWMbixXOewEReeNHzTQ6gMESKtde9poBy4b6PeG7fAccoNZ3AzGlHSc4h7aDqsmaiYoPhx8/xVUehYbbamHSVWP+wH/roFB2bTTRiP45ogFA6uJKpyS+ITudYukoNLJlVD9taPqHJgoWSM58d/UTwe7TEsWw7CUtXv1pL+KCyACyXBmOSqZwiwcREFuhqZgtRilGPzG0UTFvpngqKZWEqgifbX3YBrZPZ7OrxxWgLRR1dWfEBQZ26HA8wNXHvy3MR8OZIy5fRr89FPunaokW7dr6VLgC6LEbdnK4uc8CSexG6WnYMWzKZu7Z16xzT1Pa2Uk4sCtlnSeoDn2N9yhcmdosd+0RtQKgD8aszPC7XE9GO4y3iylkdTVeRO9lt7yD25HYfioH5I+dJ/6ZGqQd0CMZSD5mXe8jpNNxGJukVyyVjUw0EdXJO98wzOBkdW4OHlnlmAR3f6RF3Z7H3MkpycRyoHTpvWOjYnQbvZb02K9ek/7f8omo2odec12vMU+7qcl9uLJznLMVRF2xUqSPHxmKqRUujpra7t5qDUgpumBHzKMtegZ8CoImnmiCYU7fmhyUkKsuxr1faMIgSP/sMQmRHIwIB7tvrtkX3RVn+qAY2pETiRlmiGbaZ4F6eHndI7BKaqlniNREv9nEPFycZUewxvM0oKQmK2MrTzKDoFZaF8V1OAgG4j8eVK3eTdZBUYiL5ss3nkdEzih7o14JoNjKZFVUWMDvYpoE1NLHTE+t96GU3L9YqpCaQxmepLkwWx9mt5uGKlVpBxB4OfeqpN5KwifjP46FwYPLbuZ2xt/OnwY1zDqxB4tW6bN67xmHjer5ZQIrF1cIlSP0BF4hiYpgXs+IYdFykRBmI/GRPVxmVb9oBBCFG86uR6Jukb+zcbqI0Lov+jhUzbFTH0gVHiyvhexQlynlHaLDhzqh+oBvo1bpjPhNPPRoQsQrfxi3kAzKNCUWS5gHB+b6i5eGmFrtK0wyYPFjHR4K8DxQdlo+cfMttX9wxwkuT2VwUTbg88cihS0rSWl+S47T72GeSgmQ0k6d2NDOzohNO8cLaTnk5WT+V5kNa56USPoeF4kK5bl1oohKSui8HFQl0gNSVCeVW9ceXFqxcKqrY+1d9zMkXMsNuEf9SPddlsSxKYIKtF0TG9OzH8vlLlhxIy7kvXIMOt073tCgTd/6tazpS6eEPoh1Kks42ZEV0ThsFULG8Uc0vZozkCFzuulQzqZpxYpjHuWxArWSQw++g9PY2GPq+CCrXdDJCcw0dsSGaFHOESCigWXpb4bG2rrIV5wGY/T6cSOwH5LWYWpomPYtmsz9AA3aJiPCnwhXzcNiM5GIxOjJGiDBURn/CF+oiwuJHK/7/yEJfI1GMxq4bP6FrGulRkXvhY6Oau35Ueez9KHBCl3wzbDJx8J4NyMNlc0YcWepSEw0iVO04H3j/ySYBrtxihMLn02ILesyiapaRQCD3mILS7WMWY4lr5O2dEeMbkmUpInOT6wEwPQn3My9oZqPJFJOPclw3PNAjV9ujg0EQe0jnZcxrDFwcKeeXOCavdr5Lx/9r09uBO1IP4m+PNp+fMA8Ebs+N8BQW9MC5cOoqHHg1ujZ4lv85o3Qhk1ZyFFM2ke7QurRn0lhuN69MZTrtTcVHtLYIpysyfv2KbWWQt9tM/kFne/VGiaTcUXk/3kj1PeMX3HsUJIoJDwCqo8uXgIhVmU2Qip1yiwPRY+rH/loQAPAJHRJc2nO/uk6icjndEo+xmPvsJncdDjsgToSE/TpliLvv7Qc2zHCFNLaHAHx4yOOdAIwK3XTgWDXQHWL8UCKlT9W4b6o/kynoiFB1Bngx3FzKNYz6xdqgAA7V/9OgP5e83ohhdurKY5L4wkojTiB68YmydUAjr5qXqqP2tUeih/gP7iEMWNJIbKE3iW5WNps9LJyNUaUTUn4YSKCGo2Tn8pfC0kGFJ/LgiLRmjbGMRuFTripD+705CRmNLZXl/zb434N1/Ov9DUn8ENd8eGw7oXAdY5Wh2NlzEw5KLayyy5+/bwtu47xXqWLCl8MJLJwnv1NsyK1+ajfGyyqVlEM0Vl+Ky8WV1yIIOI/jOsaS3rcQAPZHi6DInFqWKF3B17QfWHLVeKiGmBvZXboZ76PXx0n2ryNXZfFXYMzUhin5liYsR9/85Fxmi0LgGE3JeqDmfFKdD5UjHjbW4ardoj0Qau00JYJTqa+AZN777tjIkMtboMt/lp3+XwsTNHgFVmIE2uEpK5VM+C7zUi833OQRtRU3Vx750SNAno2vHAzBCoUIXirZwXEgQJYFwWpKuD3LyLMe6S7JlXx+eKmbN4oBOoFfhLwebahXRtBX6ecBbng6EAB8dDYjT/ZUPc3ObgD20QnCZAJqQ8c+NJiqq1nKW6rBvIM8jny0wpjHMUR2ZYUbvHOw9WZqV1qYqxA6Ew1MVbZosgdHBJvcn0jePCnUUEWrK6iw9qmoA5zemKhtdhMiStjTy4CQC83T6Q8n7z4VRb/LoyjH1C3XSEBKfLdH9eWGcFuiMl9pzHDltmAhDF9S6IRGe2eIK68H7wjQ9sW7r+5smw9hSmDhAcHljVHOH0VGM7s+YqNF18vL/KWqV5mA6GiO6n3AGSr+RiA4tt53JCtivt2PAW4LO3RxAuGwFRdJcrc+9cmSPMKJXcfOXtAr24tiK4t0MnpIVtTM+A9Jwi93G5/QS7HIl4ywm+pNQrxDazqqnCJelg95WbGHVThHRIV3aU2mfE3v11oN11N5fOpntieA3d/9esxNV3Cj9fwJVoygFzv1+agmD6VzEoO+qKouI7HrwoS6GgbxeZLHeOj5vnwlniMcWb/j6zBxPvl0OOu7sRjTRIwCKViFA1vooOKK8t+cEbC0dSQldxyaVqCUIdhcu6j+9OAlkCHANgLz2sEk6azUHppzmnqKPIkrRuSPtPxLGgIO4tGej7XfSqSzT3sUdPrkeqf0zjwo6NsHZkvZV0H5Wxp09m46oZdtSoTsnSZpbmNO4s7WLMcILnmgvi46L0y49ieRznzJWVJ/nTw8uXDuVVOVNgP8eLn6TTVqj9AOZ+7CO7d/uP6jPdfK1XQhUjV99simH85nULSF7mmB3dZV1qRjybcF0EDGBgHy0aeLvFOUQWy3OTHHFsGMQd9GmvEZ60KkjbXCDpgkzvcCzCeeVzxixRNYDOJDzGK3Za1Z/NpTy11+AQIax+AQAYACAcR5Hn8wvQHI0lq+ygkPG12Z31KkWb4Rm6i/r9zWV7+bkf5ECsi5LS4Lx/1s2tLs11xKVE96k/AGvdQqwhgbuAyZHI7T7JQC7KuqIWHMEUndj9PM7EgAH48EQpTE7mKfxPg+UCwzvc/wDGmHoJ1zgkHdW/WnBZn9t1I/ILUhPFOc0heyHBXSCQDL1MDeLzeJrP88ry2L0Q2bWqdE+iwLm6J0jAPgd4cJuJE1u7DF8koNK1wTeMxx0aGFjd3KcYxZ3+/1CuusIqiDwbnlQNNmGeDHd8A9dRgit3Y5wMCt0C/O06UkEdkM4YdiJKuIlKXDSFT1IqTp9ZmB/ZkAbWGvvqIjusTkgZ65+Ghk0GOU6lzpgmgKEQrsoUn/xk9OimbtMN2t99SOSnrlSxAkzzXOe6r+rZPLOy2ozha497lyafiP/2HLgyZSMZdoPqPZPyLbAoN1cSaw+CLPfNSYpZCP4+NNTVSwcuksuXpD3KXj+j3IAEijcmOzbU6phxKm4+wx2ITfvMKB3h5KDDrbM8OxuWgm9lo1cBy4mH1nlKzjVZLt0klJf6Y2IaiEr4R7M1VGFTxauti0+jU645XcSxRavWTXyifPGGU9vjIMXqlC8nl0UFCSU5aqp31hn038zqnfcAsqMuswF4w+T7ZeJ1ZwsB55IQoIhmZV1o9RMeUxNrud55M0SYQXbboNYImFVutPZvPisUrjmvhgFhTgOJ2/+/6mVqsTnNdVg4RYIzoMUmrqsSSfA8BohbKSSSQfc8EiuupdUjjJH9KftW0Q60T0RdAKMNPObYkprSf1aOs4aDmmj3yiUrOmIPESfRwR7clExK7qkb4jhAHyzhkg/HfBhfYg5SNjzutAF3LIfypguW5ccAF8mojmmKTIgmuim4awamjJFbrjrERzWJbZUK1oOg5mpgLeiUqdehsVqvOeW4KUMU6vJWGJIkz4etZ+smTQX7djR6QVn+UHolqRla7pNodf3xxmLrBMO1zTvTHTTDAOiFco3DsVsaoy9c+bO6TTZSPgO4eZhqIfbcJd+Cq95VCb2e8URxu1ccXdLjeNSyW4IysCZwowE0X1CJSCKKbgdoyh56ArDVNu9XS+Ove6/vkBhRibMauQbom8nKIdI8/R635V+K+20QTd4ePpPo12ACSkISwST2jzuhkv1x/CA4I3gKh0IstmUtyGqzia3yLyDBP+ey595Ma14HhmuvwrIMmdQnuSsJv6hXAmHYop6DbIgLSxZZ9EyyBLjjVhb7mQkIWp5QU2BHl3prz/I5Ev5Qeq6gjWXJ8Zwm4SnJffZ6YPOEPXKWjGuH5hPLhugwwpazZDdlJVooMR/bPYW4KRYHXN1KoH7POQ8jpbyrDCGGoMygqczBiLePMm2P/o03JJXF/FB/LhjkomGGn+7cAbU4VHE2M+OU3wWzB90+yqHd2onoI5joSUEvxsi4kkKvx260OZROW0OLWDFAKEq+j5KEbnCICfdMXDQSDEhPAC6bn2FL+dJYZF/88N2660wyDKShY5rZbwjf3sefiJPdgeUICnDjTFObCjjMXRqcEc9tzH2LsJwdKSqpI3miiUXyBsJkQtuQK/kY/xIgWK5cMcrX/kBsA5H0kZvBrCyjAwqV3FiaQzKN2uN+hcQT+5OTZwCch5yKo5KXtXHOaGZ7L/1W9aBPYAXus2FnfY0xE2oxJ4586qC9Ej0vt4jfZQ34ZCdPWFm1RaRiJqi618KLLQIcQEHp5u/2lvkyXJiIqf9mm4+CyE2oa8wpxShpZvzbg/3vrcSjne/tG3E5NsBkZUhwYNV7/meoo6vBIHUZpI6AwBsJ48zQ8QHtUkQEkXRkQre7t6OYcJMQuKlBgqK60T7+eZiuqzWRYTAe7jzIoyNSOOhjCLwwFujLv64xufhHbGlJNMLBStbHc0Vl7dfFWGrT1ITEq8KBymkjvIcDWfjcYo1KKeUiHuZL1TYSAW36Ismrpn8icjUyKql8eUUCfukd3riIGjWInKamIUyi6rHC2RiCklSttP6V/L58ClKaxEMm5u+UQcUGVxjPAJckv0m1x5O6ppfs6ZajcLGsO/VwFvcZ9AxeBgq7NiGjUe0teXHwEecFkFDHxYwnjbnxVyWqAVE68JBIUFmA2oDVuJKoAq6i1s24uoIIa2MlAsl25XgzIqkmSaczZBWVbdTShehRFCMeoTdDhJx3GeHe/+ismsO/lzBXuDQmY6lb1RrjznFbz6dZqMHiRJb448C1ulue6ZihkAbxXUuy6UE8di0eDZUjLLTmvxvdcAjJ9iWPyU7QKAD1z3WPqGoqLYEkycBQbZ4vd+TGN0B8Hvy5BrxtlaCrG3pYOUMt908ZICmVuKUUUdgniDYsob8b6Y9Q45ubThIqz6OovcRQSUsCg4l3NvVq+zmZhp7ZA5xaYBMG4chyb/Thr5NIRF3ZSrhltaIQalsEzGT6z50vPcV6MVsGDRESSA3Gv05H2mq5E55o8X4Dt703bKYE5aGFbDzYOBhRW6xZZd38EaKcqYe+0NMyt/v6m+QswesD41+qGxFMbIC6YozQz9WKCFV+L4MkAX5qHhS11fQMdHi5pEO6QV6umvjgkKXOKTG4mqOUFH0snUsXpjxQ0oODL4oURgaHk870rWMvh+itgDRqHvL3Bzb765ZOMS6y0f9MqZtf6XoVi38gTqrvGuYK9fZ+qG0cssoC6Z+g1uV4DiGmkwW6wbEYzgOQFkkWWtzk22LHiysKJ5mxoOk2lWb8vcSSXrNWP3B24nij0v1fuKNyhAnBEK9K9W14JsSourut2zNsq4CPjw9NLD2ByiHENjZAPSsboelsVglJ3yxzdKTKIGSxnWiuk3fR+l7o2qw+RE8MyPvxRr2r63161HDvYZL3fYyY4Z3PYrOQYM1/sqZUDqs+/tbYnrenXxmMBgz1ZGMMA7WHrTENAzdXpESMDvSjfgCZ95xsc2uqrxr8KrO+g9ECe93ZPDi+SKLBhsqj5sCtdFNGe22A/USsQhg6QbiKzVUdf+T15XvjMpI83YRa4XqdtCbBc3rMSl+M8BKYLNbLp0FzE6fG+Xp2qii21QNXht09puuyYZQVWfjXPjMhasFfIWA5t+bXVPNenRHGipGyUi2eR/oeWIYbvYIOLqSVqtgX+Xw3BfVeWYlmKcyULzTx9/suP2PTiyTb/BP1j199/wIjeyZbCaBY4jWBFPq8LKrHQKFqnMh4br4kP1hBzdo2BotdWwUxOAg8SX/p1XGTeB8lKF60qT3ZMC+eZS4PKmLFFjep3PF9Gxwllm92nJIr+CvikP7NFE9+YECUdo54/xp+vrq/6+pTzzoJjksSmM6ffITVbkly5svmdsNu5hOgTB2I4DKQCi6rF164IvFrSaklnxHW8p+3bJJiJvzmmx+/9YRoJt6HHRrYY4Xt+2DbHn4AXIRTWmJqkU9673Mb6wa1josrV+zJ5jmEF30/gw6CFDBb+R+OhaI+bI0wfv9VrHOmzln2vb2wdBHOVaV8DM/KPSndum3lK71qO6TORmoCQQDmVBkcGyfll2tWLmNNy5v3DhBcVVhmELYKa8ffI/zeSi2aBGTqSc7wStRAOpwATbdKL8aQt6xMsPi/esenaWWYA5mmWS+CJVWHbrEV1YfKeVk5vbv4A2xQZ8hl5EDwI9yiUDdDx4/IszU/oIjHPbIRQ+eASpf1shQZznuoYwfP0JgejNmP8BXt8vEC8Cu60SzRwjs1NpEo9tzB+67SxGu90P7l72sd+bJ0MenKsk5k5hOr9ejmUVODdQnmElytWTNcrZdRAjwl0plU68C7uzMltoLosh3buKjlQGTepHgHTj7GPoASWwG4RszgkC2nz8fiNNA5+OSPpXVUKktBX6IzrXPh+93SguhYca+NIdbrlWAQgbsQmsiXGdX5vfG13WYTc044NE3iJz2wRV9Qv3FWZ7y6NtwVwKUyI+p0mlYge5CWIMfvlbTvVTQU8AeeI6azcrq3IromCITB/lN1PPQb0ax+uneNXmJ0g/rIFRZqge3kNR+PtOep4XNjPx7/x4TOVPVYNA0cPVq9hQTXi6CELuo97dS+fwt/NjghV838d6YnUuaPuzBMvp20T1aDGswA4Ofd55FhN5D+V4sQjNU0uCqdYQ2Pne8PdEG5kj0wPH5bGHQh2Ok2ANGQ5dBn/cFWCGouqlgsNhUqbHEzGDDH9rMg0TQeqKa46W/tRCXHq/VeYvjVzQGN9WVXxFxZbuS5y0S3YQNvmV+sLnFo+7Ix7D+NP+29GX97tGFP0Tk7bU1s7VtcE0fzqHgIcLbhxEokeIcaEqWZGUeCDQUyPd2QTwPvWOcRmRCpKaLoTRghFlsqOVIj91vrP/61IsV5pkdER0iW7k9AGmwwHiaFcE/SRBIPAusffiA7zq/TuZr17Pk1Ggdqk+YVtkYX90k5mp4MNmRyUS/kF/7vppaPBxPDe12b1rvQ4rXtnNikjKocE6tIbUalTj25yzEFmmwmD/n3dWHbRwOMktdfQyV++7s0DD7rB3sK1TmrUIyMk3ASH9C8CqirunLKB4tKGDub+/TNq9uVlT8W70nz5mHGqBt2YW34IAODlXVgdgq/yyWcOAamhFYwlHpBe8g7lp+TWa3OAaWwPcVcJtW5Hh6C6Hmww6T1cq0A8hZTna+M5qE+4XAMdECcILqtnlZSN6FomEj53Ne1G2f2E9YIe/ME0edaxBIavpqvIaYqUgoIl0gGoRyu/PKjXCUtBf6oivKLsOofKMwXphLmR1YMsbjBS123Tt6gqX6FLxzdv8WO3eoll5CRf41nCflzmIqBRpkaXkc1AqmEPRCERe9W2TebDsGbr3uS7qRq9orHwWxjO/Xo4yE0dCLj09inQ98ZNx/LjHDSp12AnviZ5+gEH5dQJ5wLKhY9nqlp/bpt639R4J3k6Alt7QCljxyLoByb3o84xmF/wPraLtzg/+RrsoeL77P4dENccArpKs2a7t5lJnFJENZcr6sZNZ89rDijj/vqJ0nOXVDtfkH0O45QVMLZorQAwyUCAxIUXyEQROwAKoByQGd25RJPPbkgxnhdEDBWGUdU3XHxp9ALXSFAkExrtenJkYy44vWf76+TWRs9BPtBdrJd8ceW6cRJGIltmKcNzpcc6njVhHn7s6ZIPeOTvk09rSQSAaQtzW4kYSzhJFP37QUUPEMhIwshuDNkVLZjKNpKkfaQV/RsMwGyrbM83hTiNjsMirbNl0CnYixl/yXcRD6SDpaCLwwfP2LqVwJ7HEZI5Y6turr6vO7ij9CexpIZM73g4r72StiwWVIIpK+BK6G/88Cp5wyUZ1vgrf6Wyia5lHTTymthKx23P2zfBqPv35RAzr7d8KMByfc79GYAhB9eE8d49Gx93hCx1JnEmaygfz+qJs53EexhAQiuiCDhwOiNqaPC7uqAXxs56N+Mgz7Vr/rfEAuYnHHdXZIX6yyWbRzKwo+0tzOc9N+kYwZ3Z0S+6nqsqw9XBl+tPRckdeuiLvlXo+A0Elv+2mIMIvbn/fM43XJzpjj9sIns2GTKYW4Lf1LrxCWxjsl4ilWXMSYs7ZLD+0T5ZQaFVgWlaJf+r/Ul15lmxi21WSnAn01EmwOsn44KuELeOeMi2NHVW/helgfpS6qL8RiIGLCnXTsq7uhShBZaem255qEGQejwtxICrhbPu3NKDQgBHi7eSfs64ZFYV6oz00HfcAARBYo1svINzDECkIh0CeONbu9hbbN/9LfECHecY0OnDgzefGdVBZ/eBuEMmd4s4VSVIJOf3Gy3ujQyuJjeAhqmxWAHqfuPXdDvbFtwSUK/eWOGkCk0Jv/nU+p38crPUpsKAoCIsmis4lrkkA/Vqp9RhD13zht1OT83zPzyTydGXzuXt+Fv1wZ075qb85r4/fxliN/YW++AXOhlq/FyQfTDZQUeM5dKXDSChrC54EI7ZAwqKWHCQ0fiNre/2fr1VwLpacGXjWvBfx1Br1VBda3vUDRq32XjLhDBZ63lzQhL3ZGjZtKCZLLi5zUu8XncIWu4x3b4S/kh+9+t4qR6LTlfPp078fJiABdjPLt9P+nF4Y/tVx+yn5Pg3VeQ095Iffdi6cz5rGarvFkojbHQaAaL82shrYc5x/uKVrV/2klE0C2Dtx81cWggt9j3iMDNg7VywhyF5uoD+Gw8ZAlrMPHTuQf3vZgKsBNm5Q6SKgfp5QGwwe3XvI19wQ7FzLKQ9ZS0W+gmb/Fwmeb4mhuok3Uvezd+ikkQKF0OoHOyq+PslSeBI9MHpWwDv7Ki/fi14PB0KxRA0ath4ZSrlTAz/pgHH5yw7rFng+zS2S1Q1QSG7eN2p+vBHpIgjTL+up4ACcgB65ii4tjB7V9Xx1THGXafOGLqVs7gMPb8OD//+aKJwkiVYjrM4S/Pt+nRNDDy6luFxqVLYnA0u2IMm+l9xifHj4YztXecR+mKpeGJpFJr5dZFVgQgQjheQDy5XMrknvUgVGEoPnIJIeUyZ1Ckwn2OudycN6v0efbp6bc7wUokeVPmch8OIFAuizT/WB1QzIktGQ43+jGmoLdWb6J3328PK0TMNG7xd4+6DQRiXFRZ88hdXbTmvbDuzarJrjy+A+PCbYij1inn4qLnoV4zmVAAdZO/CZtwDBmcaVdIWeWhy9Mzgr1aW31ZJklrQGPRjhW7ve07aXOg5K4t0edKPIJf/ZLqZ4Y9sBuxllXbeKnpMxNZT9owGpFGygi3+JaLLA2hNa/uJT0P+2rheT6d//u3iouFbc4F29OrT3PtGQIoPArk2qn5ZHZsZ6QuqPW6szE00Tjfgxe1GrMKDDeBHQZKlGIxM39+yXSNr4Y3TwleMdk/o8ul6sZKl1WghVtvE+O/dK961MIx2wIccav8yNLr6+ShKPGCRxPAK6HfxrKHgczqVg7hKJJ+9VWsRhcn5qApYvj5/9zQZ2TuwaO69iiegjrdvA460OjGZGVRulcBNYpE+0w2vAdIOp3cFg13cTed1pV2yTQG3KdOsvH4fT9eAQ4d85h8wF003Fdh6CBYGh/E4ZTPrEZL6jYDlXLT+GDZNDWY9WhSEzGEUnJFue5KVvzbXy7UOFbhG7iovqzFzUx9hR5CQXJ4tK99BMncU1dJDYL82himOaZRwWrmx6hztfY1GzdESbv39TbW4wLO3LDAo/V7ya0/QDunfLO2C4I4hzSNrNNhfmHPm7IvHk5UWzVbZc+cpTXT3nPP4oQ4sPDbZJeaA9ci6iKJU80n/3bIi5fCnqjWs71ZX1kUfotkC6pw60q6RnZ/DAHX34nNLaGLeTv/xZ/o2mxFyT837eyFZvH9laYoBjYnyTWWH81CEsBhFiA0w02JUhDDrmiHBBf8GMkZHlk6JVpOdwaOecqYj5PEbDraPIngEbKIP0Nx5kgodWJW3CMCKhfVhSeti+VTgFzWT3CLNeR3gRL9bpBaiGDT4a4E9gSrbEBpTYnQmF3Wx2wzfGI46xDJdjYFTgUld/cU7RGAFVuC2d0mPKqSIZ7bSYKo2xVG2Af9rwx+ozvrAbWxUvTNBkGvRtx3UTybsaJyc2LmjFfNNx+FAltYsGL2SSmqA4ENihdOOm9rFOCbOuAkKk4jIJvDsxA3RhmSmP79bAffP287uObOr3V5hbv73DDuP7+z+/ibLNr4oqQgGIl2nyV2weoBH97DJnw7VrBo1cM0KsvBpxlUJhl8wqERpPLrAiWub84Ou1cGHFagw+iGXkmbLS/WF6m9SDejV4lQ72LJU3gUr2U8PmTkus9vhv9I/1kDVye+FwOan0aqvx5V0m460IJ/pU87bZsR2xdCi16cpOxuglzTP6vCRNS9OYuGy1gtLwxKcv/C2OR2+OPvTeJjDcS9WIxhaDsLkCOEsLyhe9UoUb5p3hyCMXkRgv4miL902JyvxArZaXqetvhNoe4g0HMC1Q/naNJQ9FF2OGwDYKoZlRmPglY7Vyb5BGEtYA+5Eg1FzpGyEfuHo9QcwnvNKuAxv9PZ/j0I5vy31++sp3u3Dij1z1sg3R/cmQMiyW3RreOALcj3+Cl0+6JxbL2kXToDXAL1FuCcc3VAzzgsq12hosV2MAlxd2xTklEx+SJo3SO2Lm/fGxc1aio9jCjDxF2b6W0mOysjlhlaADY8RDJB+SCEMGqR8TgiPl7ae+FeJnU9d1XB/NeB/XUba6ymfnC3IPRrwCz3mSHsmjcOWixAAUttKSY6k6gdLmxtTRn0yFLF2ckmZjh0IsryH1VYmlb97XE9IlVfeAITCLKrM/ykm6IA1BqnHGRXES5HbJ2SEexZKvvFvsqjITecAHhzi6M6SgCc6nZ/iV62i+//l/ZXjbdcD16h95+Hl5uxAunpDPwbO3L7yV2HrAVUuj5XlWEiBCxQephjsVvQThyKzz1qUJvshJD6cG4CEOadEr2NkEA3W9e6wGpzbFhPTAYEGB0HSs779bgutO8scP45mcgVTE+xliBFgtGE26s0ifdZCEtc5WAUXotPdjQc6Dfx1BFpyLw7VqzhnyrLo/iQqK/ymO6+TPPVfvmHdg5oAiNoi8HEcbqe7l/JwOyE9kZSJIc1Z8nFA2Tff5G5xaF0jPN5j7PmkJtjzB21AW4DFdS8dFpCjxfRO768gtnvvGLnyfSyP8UOZD+zzBCLM8oyGgfzayqTOXOkvw1GJHe04aYPnlLs2dMEz6tExLwTi8QXS0CdHyt6XVZ5se0YjWchB8bAGNVj6s+szKmw/hl4btBHEMZTznUkbP6zPPbNO1qMj6eqFyZ+qczrc31ry6oy6MN/q+Gvfogrtnjk/+zGMXqmKy3Rp/FZVZz51I/WttCtQkqtxw6QAQarRPSaq2fubLWbZPo8VgOD6eZHcf5JcAdglcIwqXTMNv8c7ExTFCYj8xTmjrs1kfddYbeusWZL7dAUlJGIBk6wdiekPVsIcdCerZvx7HZhcScOlURI+UWO4718WQyzLyWfWkeVkhHaQ8Gh7cGv9uCQ0+7obl8Yxy/mm1u8o7KEQtwUmtkXGRfN8CuHb542jOZt1ly9cBSE7ji2jgzqkQFkOURO+Nd0TOyXN3N/nOVlahzsXON3IQ7rSrukGNPJ9aS1cfuinwKysIkvv0s43B2lUI9KZcyITLwxsE6wzXuesIS3Tn0NOqZfmB48caQtUfCE+Nww79vtA+SIyPNl9RZMGExclnfhnMuXZPBiVRLxtQG7i531j8jReHKlqHyuiO/QzC11T0DQCSDDBqXvvfCJMGnJ09cNVeID7hRJ3WKgbUVoRs/hZ+gvEO2uyE/JbYbvbZt7TwTqPXfUUdDtvPNJzu/X3zxoX2v65fdAY1n44aQbn6sbuvd/nlDZzVvSRqdXehjbB+DA5025zeEcx/YK8NoXGWqkIr8lfjNgo639Y9NDXWORcJHsW8QEMky2cCD2zufs4nd+vJY6tk0xRYQ6EUL0OkAVLAwKKM1aJiFGYEmrUm81z/mNWphDEbqZj8O7KKetjFx4t2ZDh1/5jonSijo/9L2SPLs9C2h1OoHQBXmugW2fiBBSYTZ8n/kqMjTW07Qrg/W083Reb1+2EGF5/ZzCEvJhttKMww/VzGMzFaKhPg5Bf551kN6nP0JXB2yNTugLteg4zAESYV1xOXqC0vXM+CEVmUUCBylM+2DF1VYY4sYzs3lvsDjthIl6BxGtud3knO+fdG5VSe6EOhSvPhg+ORUVH75j488csvaggkffxTltfXqK09q6aRwYqkYp+D9NQqg5LytT1i0B9sjlMgtkx27K2PNhyhsqYMGbj82o81jQDLTjLv8ac8dRsAInSiT7v2wMlch7NzvQ601Dyz0QQEhV1azwoSMr9wENX1HPuhJ8rgnbqbpbq8ybDYecRXXSKMWQP0G7dD22ALWXctd9+Q0gsuV7STs09UE2/Q7GuftqC5emzOQ5GaIoqi+2Iez3ypG08UY/JIr6ZBtwqt0AMkINv0c/B1fnIBZx06KbbaCO2sSB08v7mBLNF6v4xwcROZ+MNoj28WhiHrYxk2mB7luEcD585w5/RFgoNhun02LLV0pUtwXTuEX41Tk13GhkHDM+9Ytnlhc1x+6WlZPL7JPWwEfGMy5k3/Ss0cGzxhEp+RZ2FIYCTXCDPbqMqmAd6iqtt1yxwZn8//jZQRLCxvI58ug2tYB5mRg1NpGWpNs0cvZQHJ4MazTg86ti/t7+QibS5NiXCj9Ei9Ct4IY1Ll9KV1ph1Or2GnHmtu84jAWzWWXz1IL+6t2RR7u6tRE3ydGfRdtT4CikAzCw9NRZOlF9Yd1yNMw7589dV7b8GUahVm/CzWhHqDZ8QWMLi3dFS5SjVQVXRoOTuiimRodDQw5r7A9zin7h9CDhrLE256rgGadT9oROL37PkXRX5oTXhQboDru+0bqnlAtHkSReVLrLMgP4536YRFzLPzDqVkF8eZ5W379iWqFhZ3DgkCNrzJybyLBG873o69VxY4aa0061A9FPpI2jVB0RWkr21cACDf4s8DawOqF4QtzFoxQl/ZWGeyLVkJ/8c185hegk8OUHcIJxvdxVbsKalldDVPahuggqy6surdHtDg7yzvj33fut+1Nd1aIC8SJqiK/Gbao58Sy5PXiCxT36EQknvUOjox7LY9qIjsyAKAZaNspCB53joG5nNgHIiBQq3T1g2pd1xmkE3bY8YrjKk+K+qla6fWKEtZeWcpR0S7ZgAWriKh9fVLwK2+1facSypUwXvQPTR29irFvjvaAmX9au4RCsP+hV+jbMYpm7QE3im6nOgKf5ywh3PZvTuY2uJQqJPF4Hi+Oq39FRmpqOO6xWD49Yf1Uq1Z9y+Bpn0Cw6A7p+1X6O76lqgBmeAiY6ge4XbI22OyWsf0eK0JmqM9yz+L/K14ltVvJ8QZuDOv/DEy3tbvKeTRaJCSej37k9VbMGnN6ZFZwjND/39/p44+7joN06F43ySZjhyw5il006eV6TEYvuzsiqFFeGswT3nvdrGaq4FKHfjqd7HA/Q4LOcIu9y7eCdtv6JX10pFW1Y5R+Px4/IVJnaa9jzgxg8fyJE2a13a5u9iQWzp+vQYl0/UauVE3/LpkLyI+yYayEfo4tWHnZtaU+YHFxlE/L24aa71sVSAjEQ1KWcTYNvTlnydoGiR9Vdng1SjnpQ6DWcqbEdlpSCta/D7dlSbhK+gcqoAd9ZUy3KodYCnu3vdDWAybVd5iMR9NzDt1LCW0IUybm2UzNFSud5zWvLnmmKu1GrtLxwx9mGiNWraDRZg80KsMiIkmTosBjf2MwIAF5jJVNp/g7rxnqTbk8xdbRrFWxsWqu5p0r+2eB2UN2jQdELeiuF0OD+mQIVJ+Wr+CpDTACXvbtX8F6amrs4CPksw/SF+c2tPIGfRqRYCWwyqZAXuqOWGaYuVhXr2nmEZggmRxu3vFOLs5zPYimh3IBY309KUyM3Fe6g/YAKMcy9aW8MdiECWwAmSfqoDLhJX5kn1+EAiHKjG6FBBdzGdVuN/GjuYcTNcyT3moTuwWt7hJWL60bKMGGtrUxjGlvM5ezIiirv0WTCYRzsZ16SDH39ZpN2aRHLADJzBeXAOC2iLEt4eWaFOQmp88vDYnkO0Cnsj535cm5OZOUgq57ZT7EVMllseeRIgrWPUXULTJVdQa6k3TrzvA64bu7U53/JB3ZIvgtUs5PVdfL2wlk+AixEoo5m91FlkxTsziP/fzqr53Pu28P5Jz5zchNK3eGgkGnFUsd3vndcQnPj6/rHVGSZspPlKLxTmGB8tRDb9QTxkM5TDN0YAeCe/UAHsNAhRP7EbqXnFU3kDZU7I8zxvFmuL7dDqsjUvXk0dXSAgkUf62abDAG48Vs3Jw8UO4XZDf8E0U6ZE3ekgS8KuikWVgw26Mo5AbzOroXMEpMQcUEVg4liFDwoKoL5p+U4QGCBEC5J4gneGjyMnPgQ8tHlvsXEpBk2QTpMf/2LMbMt9wpjJFTwJHOwZLn6tZ3B89illIZ8OGI7ZiwKuZqYgcK8yZs0Qe92j/81pQyNyPdOLGHoZ+HWYVDaLTaJCGMpUDbQVEwTNPBnYQo8AHKERsW29p3rCC0lnQL04Iim3Ey8Gek6Y20Cksf0Z6CScmkPjwA55F9w0CL95Mvhcke2gzPc0YtVXPmjh4nhdViAn5CGTJGgrB8ZpjfgDYdlcd1pMBrxTe8C+BTB5NxuwUiQ3GUpB6vrl9RVK+QVzUD7Mup9LUFwpoR2dYCbW4kS6131YafP0Qk1wNaYJqJVRTSSxPprg5DbiFPB2WALy0Xw7qp0sE2YIRwv5ScGKLe/8YLV541NtKJloejMvGJJsEoJupMS4Y2Jirh+uaOpPysLBW3kXUKvZhRgHtNFltF0Hd5AfovJ/Qvureb7HsIiHFV0hkDCa35wFgQ8gR3h882L6V/ll6HDFuTwFWC3Os0WZzKFUGawnTnj+EHIV02tpe6Gt1E7lvxB5eDmOaM84oOQzFal6H1S6ckugXMdkbaABijOlomYU5ofaAO1528SKmh+cgMFZuq1Q2NpNJIOC3KaghEh85xTTtJZUioeGYTKt90BsN7PW+Yg9XJQ/iirV2g6EZRQI+cuwSZtYq1SvyaM5hdmVlAVT+v/6eazrwdAgkIPMSbUT7L3uP5Q3wAsREFD/WMU8hZ03aJVvPxqASJIIazLq02/JynJx8C2dmYocNDo4JujNE0lOLZe8Brx29a4O7UFAtlemPDbBgqora1ythUyno2fP+dVmVuVxEFdOnd7TpWMdz1RDu3daId1LvEdSbrIACbPs71Oo8LHVtwsb8llcuMVPUxyoOcGYvDSDQEoSEWNtnFTvtOgMhU8G4ApblBOtbIhWOjP3GJNq2InPfeGNVc4JXu+E2T3Q87363EuCahDkYb22nA/EO8LSM6hUgSvaMC2s7YRjTP26Y62qCxiVc/dYennvEKBtad9OkZxQUXlGUPTo9bSXtbE2QtlizMcxWUeg7LK5WcOh8+bwQEFCbNuGbDVOUxpWOH5w69e3YS9Qrb6fibBixpq+GSguTHzsbVpwcpwHO5hIRSAjEnnGIFWx8jOhmtBhTxEyINAnUoSzpkO44UD3lrqfBWo0W7u7k8V2Spq/Z4+LLWT/kHaV5mhuBtzysrgQP8c7oaFXynIe2UnebL+zI2fP/Ycgl8W5nhtBvC2kCSLvSof6KlcxdbgSNRJd7jPjeQK6eDPMFCqDTPzfdQuBXZlYJhENt7m2yB8ne9MFYDt5Lo7hnVzxLQ1pRvVPfVtJFaCnUJ9qMiCEI4+j+E3nWhkG0ePfqYh5UfXydh7Nhsg524XbWjFdJuuFWrf94NmVjEMDCBXg8iKQxwec1a2dGe5gsz8ky7X44dJm/1k/+lrtlHEw0mpeJSF1TAhFyxfyGbtD1vVJfh9+OQfivIZPfZsYlu7uZ0MBLvduyt5QGrqXsebJ8Ey6Ueislands8R+GCybMES7ddLy7un4q5WTks+BUALgw204zwZOkozLXPdHXlPXYtRt9EzDPQboWWHWO9JuvB9Mbr2b8JDFPIbu68/9+eMhyjxKVVrupjEKln9VtxsY5xV5Kqpr+MpqSxAblrdAF1NKPBR4XGmve/sKv+0XKZGjKi+FSdyB2T0AEVNaw5UzQ8SB90l2cD01gGbTtGLiCt5xcnq5Rhu6Q/UYIC/G/lZM9FyHQul+0LTJiGsyy/1Q5PyyPzeyoN0yW2vzeoTlgjtggjcA0HDgEvKOVEgKLCy72gftc0eFac1z630spArQKEG6G6r8CIkphtyDxSN7dOPuWjw/weaRYr6+pD38hHUnSiwXcj8I2C/H6MQXlyfyNm22GCTInbPktZCmvg7pohhn0WvT0o0SeIMdhbrLP590CeE9Kiiw9tvBDTvpyBtRwLgM+7rYcjQYl8ttzgETF2OiXD5g8tZAs5FEBL02g8nnoqZ4gE4dHMuhg7xxADAUIMprYIDI2mNAfY+OnKckjKvoFS1iNx0vAbBoZtkR/p3jzlWEkHfppE+59QuMtbVwLZwiGP4dnb2sjpR+ri+GgSw6Kdz3YJfT+De8t+Bglxtykkc7JOlbZaQ4Ar2x7nMJPcf/d2qFfxD4jcyHjYboARGvpiVfb3zJLBCypedDF8uWa6YNFrMQT9PEW+4qmLwf6/xQApyeNvRnyHLngqdXwY0MJofKsKFGQ/ZxuIa2qmBTBn6ZmI7WxlTfMrEVZbDdZP4PkqV+Ta0YS2305wDdXgiKPUw2Esm3FqMo7DFWeiidxYkrRbLscsUYkC3/Z58HZ4zwnIWu/o6FLgPqxT95UG5Wcjn3UXk6UOqVZveDIfI/soKIU0GfPHa3LMSJqJjLsbc7FXx/Aa3UlRIgkLHnoHhYUnsU+kfUwH2HjrEg4cj6UsQcWNZxbOfp+qWANEhL1WBPTH3Ewt9K4qIrPi6RetJITZOf4gyjSIp6oMqf3vxHvzpokJihfJpJOeoinQXIirbUDkywccccH+6X6ymh8bQZ1R9A3dSmPG8jMdgvM6LEUD5kTaWk3DDixWSVcxD4jXIa27eRmGDYS/FCMvzWMcTt+7q2uOMOccpQUqyNPEOk3hrY3dq4jENZoCHQkPlM7R7fjrC++ZHTsqCa1qjZgwFAkWDtdOxdiqUvz4Dqm9qhlM6YJrz72ftodfGSvUv3oU46T4mZ7dpIc8Y50C0mUqIEtBqSXSN9xEYvGXbYV9AiRw+i+1xxqHdWgaTYx+nEuWJqwTlrkwWuX7tbtVqeHiOye+dtBgLzDVXSAJgmln++y128DkJIkbC/XcYhYSwGBa2twIaM/BUlUwH+7v/99UTR44Ie+JLTJRXehBwuiuQTLXu9FbYDdI4irT1pJa8tBUrI9AfzI0CK5TfpppNaBlnSRXXOzhmt+wSu6V7MtylQva/bqu+y/WLkUaJRSMs2ix5H/4koqmHUaB9YzszOVrhq++5QnaAiYwnDkzUPcEHxHwAFFcuVJaRt69M/9yJ2FpMHNZ9gErrWh8QMclafFMfOuHwG3ulvxbuFwawf8zf6ktW2njGMD4WiEpDbrKKak4IfTlxQrEPDKQQ/J3n+5sA+vs9Nep04hr2FdS/h1ql8wA25gROqUCsZ1kL5U3H484Wq8NM3A6icFYfdOL8t/DXSNRjDsFR2+89mJsCxibjoQhylD8Uhd0bvmWzX6WCX58aiNzjjH+fJjmC7qqQApFYJZYvF6e0TBUtgj6ixK2HiZkBuiHO/HLt+TNqjiRmD1uIvU46/EDmDNGYZAOeXuhf1bTKEAtAhdoOBumeWbnulvfI7bDCH6ta/q51EqfRmGI5FQ7+Q53mXKVTrDdMicHFkEHVKNhl6IIb+V6X7uidmOw6mPtxbBxKMG4sw6L0WQgEbHSPWLK1lWS21A23GMeW2l7WrdA5hGQ/cBdN71qziNK/gqergnoWacbi9SU757ahf9/il3Rx/wdYe0kXSldxUWDJQc3fHOFVL+WYYgpOWDBg4ozF90Z5CTF13W7IYIINkn+5Y252XE8c/HewSlUrUN79Hzv6D3+jXJNbbWC5yGQw+O2h8SlnKg0cB7JElghnr8mP11zbdwxhqKwac2CjDy05wEAzuxeZEaVaRAPNxXOpPKC6MfvSb6q0dJzyPO/CrNl+eL6Q1oaHpDbPhcdLOs+KiWtM85Kinp6LvFjuKZq1NlIr0wB5uHCvzmI4b/8ngUEaZbfO/KNY0nou/9spdZwRsZusjkhJ6KmvhYzv7ow2sk4xJd7k2JlCy1kfsgGQJgl6dkzNOpnnL+jK7jO/0EIGMCnmpc1d4vccFgGmefpiy5wl5tNDEYfsG6UnfYitX1Uw5psGOaNTz/dW4hWR/7SOvnUN6lEPv2ucN0EZWRZpMvO0g+Zj6/aatu2ZkXa0FhZnKn2eJclX45GiEB7fL07zGXUpjf63BZ94arJKQK3YFl0B3kTgCzSGIhZObKCldBdHz4lvq13T3ZooyO6j6QcRlwnaFo5Qt1g7WR4EJL000NDSPyAJp5Cbx5nqT9b3u9bqR+wqG5/B08mY4xRowZdhjgfFwSuhmZluOV0GepNl3eeKBZpHvDpLXWDvL5yUue9OPge4wewLosZHuz8yZpNXC5sQn2EOeiACOhPSiTbw6dJSLwsukogTqfqtm5SvYVqed9GiOv6baohwKceGW4D/UVV2xI5tq97azcVeIIMTCHQCK26r/0Qzg8NQQk4nRIzDpDnhC4/yHl85Evz0HKpwynGJFir1z6tpDm1m0+0jIVh9W8HlsBN+9pMpWbEQZpO096g0dFcESj3hNhIJlZS6AAAcephzBNevT5h4YOq+Lw5jwWeBOyz5cLLG5B7yQ6AZTNpdGoms0vesLqMczTNuuVApeQxsd0webBvnlxoXmlhfPy9Ip5jc6UkGJJdiPWpy80ZNgVs/nYzvFb1epGK9EfUrvCJsQtxuvbw+JXkVlRmXdf9LMJ9fy7zevXNKafsTFjUM1vzIqchK0tgo4IgbXYVdWW/CBucM0Pb2Ri0N7C9nkW8FfcUDIgg1dFDLIG4zwJHhiT9OQo+Y9/6RysEsrAjj/WGuC/OmcUIEQKXsMHPHuCoOrMdRLGrkNNj8lA2J30anViZoBwOYhEzwAayjVbDRKLMWK+Gl9zOYYN77gaCwDtNqEavw4Y6priqJRUvLyLGm6nJMpWolTyKoU/qCGYoDIgcUo5tMAc9pGVFqPz1Qki+GCEjFbHRisc/ucrregZ4TJSAE1c14b7BIt23Hmnw6QXGhSc2n1cg8pkJnBhNu3TBT1Fblr31x+inYaLz5ydPPjFbMhEXiHBaPKkq3RDmBc1UBqoVhRrcq0+ittMp8o7dEXHIpoNQO19AcvOqcLyQD9jD5jFfMJD9cfY0IAOyv/ZeUo7OQcs01jUBRHoFbTgqh67SJfO0tGBOHRZUIl8a4cZc0QFbALsQcMkMqz2Fq3yA5y5fx8kHX33382E+HtxzQKyuQa39wbyWj7lgbaafXGJcxQm9NQvgogD/eooC4/I0+HH+XEv50ilF3dmmcR3DRJ+3kt5TusO3il7ZuWthN7mCV0qMKceGfALHTLtOaF7hzPPPcZfXuAGQKzkeoLQrUYfSzoEfal6C4PI9Lan/pvroeRugBNBn6CDMSMzWsd2HmAo5muKAr6L/WPX/edC2huUOpsp7oGc9tOChJZgzLliUMCtAoeRnixabWiIfL29bfpCWuJwX7w4ij/CGZNH+a71jMQl8z3cWALroKx9WG5SyOnZpjhezt5YVAYTZWYKoglYe/zjA5sKsu2UD0kQH4DQMMDL0d8TFQUHFA5QLgqFsGQBOGV1qqfh8fNRNSFmavio+mwBylNWGKjSKJ1fAEl7skvZqVEeAcFRHwb+PrXlWPtdvwg/Kw5BPJGAONr7DA2+91g8BhgvugpkUnCcLhg4STQLTiIbTl98hbbZlcmpZ41unRm6qXzto7/TZuGGvF9JaPS+O6rlo3sh6igKYI3rWh5fAKbfePmOeCOiqV5CZhDLOlBzKfhPcI0RALrkYnOWlI+pDHINUxIQF6t1FT4RDV5CyHPaMLSYyaEDL/W4DLLKyZn+x5zlALW3ugk24LjNiAFvjc0Oy88mprBkJImONiB/f0nhNeTKDILeCFcM9TRo4OkB+vthimnUHEzO9zRWcJ0eGfhQmvUovOG0BfvyuhH5/SbdACfAlfBOVmsNGZw9t/ZvBxc6Md6blB15H/sYS4EwzJDni1liKngbbB1QRKS1J6zS8S5aWsT/rlGxl+rApfiT306Mi8Ej7oHjdW2I8x/MqwPreVJT29kH8p369AYHncwwvhteRrqQI1b2XVj2tzwZsVznHniBNrjx3wrNdtNpONwxNgKrzXfMeK7y2dcSODOxU5As7Y0gvNf9B/kkIJ1QYSQZoWUGHGUyvcke4Mi/9bNKX24ea/HaSiYot0V/vWmbkeBtC+Od6nerkXyHfhdjI/lvzYpZDelkzaA7SMyI/89gDqzXB7gt2kXZErAXV2FgD4YfXcV0FYXodqQSHQEsAHuTciekUdO5mI63hbA+1S62dBHOT6og5jvVVLQgNwBBTxEnMlfeUDdmiToDnVzbYgvGT0qoY4t+mEbSAyBeQMPMCj1eVDBVO4mtkdwbXxERIkIHgu1ssjfOssRargey69S9ZxDyfps7E+h3Gon/u9ZuFyClxGxgKe5vskqZkEeRn1MMqBgXSw//BZoJGfok7Z05dA5tvYetC0FJSi5mZiFPS/8HF4lzKgLu+K+kLu2xxhGix26010k4r704no9+Lduxtg2oIkfbqPneGhSa1dYNhjSJjth3DsYHRcCr3XH6RV1oDbdRPt+j/ok3YLqMWnPsfYPI1zWG3mU0jTn8zEOgwwsupeueo/xal7n1948I6Tk9sB5yA5buMleRJpSVKiJ4/FrTbmOhHsar7AOI0yrf3x6hfRsGRJw5Iez3vUrZcMLrYY9zF0SLfQE4A5Cucrkv+7a+jkoegWnvVhmKEPiXHJuAPmbWWqlcGJgkbTk8E5LkQ7tgxUJB5xnQPSh7R8O6DPg/y7UkIkWaz5Hv/pA1ZbGhT3GK1o8jlQwVqFn/AeIjGVvD+KrqGCLB5uAuFbrQOhvlPpCGAv+0GZSbNY1VCgqWcAzrEDOppqbvl0E2dRncPzFSroI7OrVcwWS68CnsteZGY8Mz3aMnlw3Mt+08ch6X2/rmiXFYqYF6cSdJvLn1G06VTNVrauSC47OWW/FMnrb6GSgxILc5AdLSt+trrzHW7ldnUTbnJGZJKiK9SvcuHi8R4f+b9LAMmzDKNQpBxt3vdyRqU9xKarqO0lTM/dDoMcxJxTEdXbmbf47aDXD1+5qfWAHKpb7y7SlrLpzgyVVmFYKwe2GO+b074yZX54rYrL07KjSiW25kmlFocmSwc57CSNuemXEPCu3lujQt8lRKiU4clSpzDeA5qwmF1NC5RmF1Welsge0MLBptEkcmbpXr/G7/eSglF1wAqR7NcPmZvXrmtnByhWloLbd6Q8Crqd1nQxtHaLLI7aXiNuU/mTmwpS9stMmFU2pv1RXpDXqDNJ3pUEwjhaA9MwPN+iFuOHxjRv5YWRRi4nn97AjoJjT+NOAPY3EK7aVpSVzJedHfF5zqgb5JahHopaGcTk9lUC0TaGU3MS2x28oe2yMGniSFLTPfUCr4oR2aiWB1n87/hC/B1lawlF75wFrNiVNZUn4gwHrezuJjoyJbKA7B8CIdyHDrUaVorjH/mwkgx4FlsnWE0+IuDj5H9y6nQyJIKS697oi/kBq55nq8u+adgngoQRaMyBgyIDTVAywJ75aF/QRQMHSL5JwpfJGN+uiFfYruXO6u9TkSwdLyYavxFaAoTqJgvi6URQu+oozzyyYLB4vdvMkEavQUbJ59w3qQAV2r9etTM02FptflAlTkp2ui1v/It9a76lHm441VIwfe0+M/Ltb0fgl6RV9VNRJrxBB5tJYX+BAM/AryXB/Z5RZHfoS9mrc8eTzYdCJj3bIQjo7AL5gufpIC934Uf1fIYvVRNuQWkywMxQm8lqWKUxqnYnW9HTV7IGeQU5PTrgPInHXy2XnVoQ+blY8aluj8cHJRCv8LyrQoV4Zr+MCVzq698EXvSECEWK5YposbzxImYsAd4lenxWEMu0yT8yKVGv4WJLIP/plOJiUfquH6a3FWXEP+pSTZ/UEbyhA3ZGxM+L0r8gO2lzjqVcpNsqDLkY3QeeTbgRut1pnSi1vLib+Ebw8PI6BcGr5x4BETcVwE9pwP20NCTuGBnJ1V624cKzu6+JrKt9AAJ2EsEav+iCp9E+QsjmVPlVCKjnr953Lt4sbmSbmDBJ2oU+X83HRbpWSyVuVWi8rwuhRa8d83J8TTy1+nFN/4sM2n8sRoVzz3XDTKUBoXVqhh6eMa8wkU4AAOq4BxR0SuJ8a+HbMl4QxLUo/WRpHNv107/SWSi+jgj4EuVO/5m8UXoI5P/aruW2dSZQDYmpKdcQYRGE10ft21UCdG7uR9sX199fFf+PpJk3fioEcc2e5XQV/9uiini9RaCi7Ag2mG8v1tOe+Nac1eh0fJAA5D2SDyJBoUIMb3ehItGQgJ78ugW8SQlNydNDvK6UmwOSSITeYanISWt5m+M3s4n0xWHMNoY9GSzTpCNaX8301xzxlvtELN6yJhrxvp6CdftWjT/RP1mB0vz4RywYcFxkx96z10Pk7t1ApnmK3QU6V+JAxgbDRLcE6Unv0N7lGW6x634s7w5GakQZWYwuB//LihmyQVSPg8PwuE3xMNRAsFw1uPen0O7vbw3P/LvSj6cG6MZAHHupbXcmDF8kBcnaPrv31BmDHEc5QNFOwfEV3WrmsvyeSVBlefqYaRf5ogzZPHXgWR1AhT3VULHJEYF8Pw3t5IaBVHEuGonMiMqzlgTbF8+LJBKmHQHrRm4ooFkZZh4Ghg/WFfDbU6PuyTW7t6WA3WnVJjJIt2eVqTXeANjejDDKL/FOEbHtw2jAdUHydHgVdYvcOb2No5JrIVPiWBGe1Uobxrp48cAufC9r0h1Yn7TBHigVinLEG+guO3AU8AHdQDU2As+IEG6x7Gd3GeurKmsJRZ4HRPoIaks/IGMA0fl/gD+b9W50QoHUMNtdYcRDiBNASS7TLgYvO9qa/ron7/mFPBXX5zSaRANtL+Jmn5x17W0KiGQh7PsYBKsrqTBD4f2wsoroD5WlKCR4LcKd0cCEKQy7XrohwrrvCsrlN/0vUGIxPkj3dE/AvBS7p4IFj8yS+A0bTLqpAhLaZugIE/C4gjqvfY+crJ0YCdbFgLCi0yqMKZp/Aw6AGmThgPyG1eLhz6deSN3xm/y04Q9kLq8KgcTpzP1vVcxvgH9GA/B0QBmGCbTYboz7SIEmjnFbcJUOK0zboU0Q3K8HHBu/FnTSkTjapKyBkegR++KEBl2/V2X1ZcmsPjAy2oYQidaCapnMUoKou+zLDJwJ+rxTYo2xNcQXAUV4CRfEI5P8DqRJT5ACr1BHLUg8g7JthP8PdDXvbrSSSvEozbAoHCe51Td/fAlyjbfZ6WAbf5D+FntJhLkliapaUqTcKUAHKGQiaMqQhNiweOdGnThdS5E1kwIkCFXdI0kpgNlEqwJEuTtnh/z5PGku6CtRkN8oOqAQoPSIzAVedh+yHAmDp/DCIvKwDpzMpg6rYRi9DUAbVnTWITAsW7Km4iWu1fKW1czh4IGCxZshTQdaON/Jr1kh+u3k6mvB4vAxm66FQOAJXR6ZTAvQM7Sz5FH0nWPTT834N/1XJ6tkbHi927XZnJlZkTLnKh4W7n3w3fS3iBMJ0bw3lId3RTvepBFCTWzpsZKLpSBKKGD53GsF09tm6D8xD9FmA7Z5/xhvpqv+Stgo1zSPGEjLNqxLLqe97np4VChYmGuoNv2bHseMYiH6ZN3wST97MBwFK+Wb1esVAHEw2Ea9fh+14NxhHYo5bSIrCR45tOMN2vfUVrJ01iLZPNR1VkDF2C9P9i8p04ZiyVImHg0/P070G0ANtaU43uMD8+vcBBoWI560j35xNNe0I0zzXCaNaUxlz9CqyWXiMd2PkMuKEL7/o5KN/n2MmxQaWJKLAjT/v3IWcxtLBMKL9OFWDCxa1vYpE7JC3/Y9wlKySz0lSMkYQAHeclex69nVc5R6XXlqvgzDeEqPB4H3RSxOv2QUpNco3QGY1Cz0uyXkbMJheihL/ffDypxhnMy8q0ZKZb/JhDkFLZZxkL1A6ibFX/juPrikobAhqquoOgM4yiEdVfaeeeHALYu4CKeFlA09ni86JI5TfLKyrjN60jr5s5rwspgcnuMmow+1NgaE7FymncET/mtphH38JizzmnZNcMaGo6+90a2gdRoZE3U9o8c5g7IEadYnJmyaJFbyRcXPioBpT7LzKHUyWfcOQYGqSDjHwuBnUsWCYJqx6ZZhFGeclJuZthdIvIxgtkQ0ancJo133fda0gzKVmmPeTkdg/8XANuXP8Uo9d1mKDTMUWDQztzshgrCLHUQ/sLKabt41QG/9ifmENbhNCBOgQWTuMmYyohU9QjVw+v6vTSo9i6hGGvadpQY2LpMNok0EXKJReRpN5IJmV5c2gbHE/JdmFrDbf7LdCMa/Rappc6sgAjOWtfOUSrXbb1Na1mWNKKo0oQNyUnJU4PxwQo2yVsSiJiZxsDUBvhCMj7b7VUOQ0u0LOYQ76kJKFjXT9Qq8xFyprS2OiJDDCSN02zAv0iA96HZ/NMT38UsX5rg4N9jyevVzNaX+wXmGKvtoFN+sCEVO845UCOVwLljw+FXTjvIE53tWSGYXlU2MX8RylBSwD1Oa+koV1PC+Am5hpVPVXsKKW1CmRk1JT5SXaJ3OxEMIZs/l7D+XfcQWAUfRBJiN+gznC93Avn/acBlXO67xPvWci2XED6O6DN0qfyn6Ng7SA0T9+nFdJ6Jidwgb95S7FaKghUpqneJwvN40+2liupVo09u9gHfo+MGMeR/5lmWlwJedvPkXPo+hNIfmIQ6vS+Hqy+YRsffeAcpLF58oryY/QykIwSmNIOpOjBffsoPA/mmlLuHMOvmELuSWfXVNHaEe0NTaLvxpv+tgUbeFwEeJo4JjlFzZfrp+uBlj20zPMPl6xYbVfYIj5IB/ubzfk5q96StAVVYJIawQ0e/ufoGb10hSUDgpUKITlgnZ2jcGYJDNoZR1nAo2hneL/lhfolDnZzknEl/b5Lfu2v11zEukWlK2EDbfm1Gx1xMCjyoVJeW147UlqGq8hJ3xMY4pUX/7HWt8LRux0n5AKWa9Sqkl8z+/ntfG0CWLSfhkk3b0cP7sA8jX9Uamtwe4jNN4aytk9ikPGGPy5jD1GLzQ4a6cPAlMrebofUlh1TolwocoE5z1L2s/8ri3z+d6dsxo8+BwhqWiEnVO1rEEtP02sV5SThmRUZ9s/UoN6rZOffoE+qrszqFq1RGZI/FN5ax+WlyniWhEkr7pha+Ijq4IYJZ3HvggfKA/ojHyoRa1Oz0b9ZeLJrOwKDBEzij6k5be/mccnrwvAN3fpY3ityKdJL+nMWZdWKEkvsCG3NtWkNKBouVSH2BVTr6wpwuR2JJqc8KiucPSF72MRuS8KWr4qpwU6s6QQG0etAibeydAnBOR8IyuBVn1HhLClHFdWEuCISyAZMcghSHkMAwEIlI3wsZSphP2odKSVap50LHbomGehN4mKdgDzM4r4JWZ4kAJsWVmw63rYO/88bj0awi2GkA9cYg/PrXMomNmw0e20tVgjVl519GtS+WrxjwLyf3sA+Ya0SxyBOde1EBOrcE3+CH58J9JTg+DUKuHNNTNiVITt4OfRQozfuTQ13VtEP43QzVc3Pxc1xJ+5toCpO/MmcKEjcXEBxIsH/6L2K7JmkhIQUKrCOUt6YWguNG8gubxOLd0YJW6l8EvgXU3CEmwzh88M7DJMh+26uoR8k7XGiWP5oED5ptcnVSDLTl6hrpjHUz2WUFYNBFWKwXGuUo6BZKTbYozFStTFLjHQVk8N3Bxc6i2SPsgRhyzR4hBGM/zVipXIdGFAQFclx4byACZWzLMVEb5jiC8ZaNVCIgJdSnW6XGKEEaseAGBnvADD3imsjjwCQIB3gGFvTI99JQKRAKc++O/rtR/5+TCjI/Z4hHiV+h6w/TeSOdgPIewORe3HTnOohpyZyzJG1SMN3ErO8vqbK6og1w25Q5SecZv2wCAir8YXntZ2RcXXPi+wjx+EUNaAcW3DZU7cRXHw5LgIEzEYh37ePd1ron5PKkXrAiv0r99DhtEq3Dy0cqhy+Xnol3CvyNq0a4oFdXuVacsEFHTAGPvLgq57Wx+MxQmscQxb69dFasxyPHstW1AIx06TG0MxrnybXGDeRrM3bHr6wOWKeV94iOWtH1VkXKxQcAKTAIW652t7qsoWrns3xyl5NCM0y6dywItxgIzsM54tMWqOHfO8aeZhXapca5z7AViatDl5S6QtJEX6HkGiOO07bFq4TEzdyoH8M+FPkxH+VRTTMpDOtCNL8wePGZeh8zuTQvMWJV9YHI55NutSJhL0de5lkw/7POka/r+k7dgG8K/sLejo87F/VP+QipwIJ3HkwcN81nCbNM739fOSn2y67tu8K55e3vqg3iAAabv0lKyFbZbzHSEHbLOwBfx3rWfLprfcYt3i0/Aolh0p4LZ1yHwwSF/4Xtc5n8UwEKNcJ5NmKa/AZIGfav3DUOYNtoK0+P3NA7LDtFnXK4gS9eyknegkwTWLr3137nlmPNMY7K0VCDpr5cfhCx+eh5q3/Rdt928R34yJHyhXgNkQaTVH2RdgwOgDjD3dsl9RX2VCt8RgVHwOdzAjtn8Zv8I6yK4ZyRJM8/QR1aLoiJaFKqYCFiaqFRDAizo/K4j/T20/kRUa0RpYn6uZ7E7sdmVay3Xnhlve9ejZH0lbwqGXYArbDJo3FCr7Wl7mEtJYHLCVR83ScFipk71srJFeZ0ReNs8iaf8EZJ0yFTbjK5gV6I2x1d5r5Zrr0lks4J6THdKLShfi3Rk0DEeEBfpSUgrHFvucnKWHj/fYJ48k8DEggx9SZZJtC6rrYXSDq/opHGSH8w+IODwCr3B+hio+OEDfzXMw/WvSNYoGmovLczBFmRPWsDmhvdwbBmEYkwdr+iI9ogVpfaiGiPFTNcda7rLalIg3wqtkNI+ujT6pnBLDfHHCxksw8JFh1WAc66bUvvuxgalw1SI/TxIVZTVLSpn+P66KBVTGGekUVxo8Df1quh8qtdX0azaNyi59mA2bfOgkYylcdp7riWetxAr1F4UeIdX5sty5kmnTTCh9Plgf4UI1AlOcKG3bd/Xo4hsGQ++MuXxvqRUUr3YPnoWRI9T5TgsKq0XklHP6OH4PgC2BI7WB+wQ/p9PEfgjXoI9eCAp5kGh5VEuBTve0BUMKj7Ci3Lt/Y43KUhF4FeEY4ilwEnUAbtIUSOWP4Zl4A+ubomSnVranUnUARH0H8014/xcuWE1swgdyDhXpTM3/+XAIHWAcRCAC5KO2uacjMWwycmg23EwHeFIn239AXEZyOd+6Fg6JFyIyhHzVWf0h8JpBPQGYvKRNt2YO1MUGTCPyc7Y6xxnoobC1fGJLUwkHbh4GrLJFDK9z0oFazTstocAAOv6IhOgR+LJ+XwiFDi6Ryp6O76ylwvzwzQJQeH2nrqdDmCBoKuX/LvaPiZ2eX+RJb7zHywxy2g6cLjNyWbRyibUU5D04TztCjpM0xWGtG8NWoZmROWTuEzR2Z38lgheOnDK1kWeexvay5T91MV15wMLKM4vXXeewpa0ZL94X9OVpyduz0NmFT12AxHG7ToyswdXR90rNk+LYwdHf1dUxzPCwKMzPqtIl5s656N9KWsL3craxXXO6RLH8zr8nUGJi57mXNl+0yq6K5t/agxor1ltDjal8V5iePhs/OLnsaEJDN8YdPXPyJbeRvyLSxKmDuUKDgx31yCw4bXOMyGNn70oz4hDpkVen6CE4D7zptW67yl4jAj8msIT+lCxb/iu0dEIyp88oIhmOf/HAN/dJZwLU38p0dAE/uezt1TU9ugQjvIuG/IvyhAntZ47Rg+Q/R7p71jPqfcstLw3E5IzqtSnB93CabjjNoT7K8dDR9ehEHmDJIdE+pMYbyK1UGH7jytITkglGDVr7xAJ42jgRX7p62WC64URc1seJF8wZX+wfmvP4Z4AtKh3Uc5NaZ0VnkKT30Q+7242ECLnn2f6dcXo0I0ckKIjCXzdU/i0MaFnBOHvV3oiX+4BR5Cy99vNd+Dt6bO5ba6k9+29X4+lUJpxO3UeB/C8LW3IUaCdF8lQfywtobXSW77A5vCNKgl2f1QD5ikyAlkbgLpP4KJUdk8KvXxwpID24/Dp2Oe6onKoUAK2pYdf9BK7SwfvVKU3Ht811jXtwbTZY2BhDTH8l/JGtdAURnObhqfAUl+sWcSqn+50PLBAkLHHE5cJRzT60QFEXy/SOrLpqiEYYdi2cwcyesqYB3SkfGNTVehaveU6ijsqAPifeMvtd4XEK0Mx2x5PbzBGlkOcmG8MdrAQdFkpprkxULbq/d5kHD8QS/IWrUa4zCDbEGYOXzSrcAIQWB+j0vTISDSNX+WBCWm3omlGEkv+AvCNyFBhmPJH9qCMdvLPi2fCnK8vXXPWUfQgc3QNPJUtBYBvgiKHEZI2rocRxQC4fn34UGp5DMgLFHzkyMlMzzdQ5UaUCD62sbN4U+ihBOAePgqqT+CF4RksW6J2W3E07xBZkK0w3mhQMcZYFcfBRa1ppDjhvlsiHZpdHn4tpH6KzLzNbjPPXUHCncUO4y0KzKGBvyKUXJJzj05pp5SJdD26hbrU5zKvtt/jP/o0QspISiPHFr4R2dpcggI1qO5UXMPfDOrwBYGLHqpP2/B5RfHDq+0Apz2jnGdl+i6ssU9MXdjq/WdL+2U67MeneAdRGmL6mpHUNoQrbL+5bt/lBfaaXPcGaCpoE1D1I5j5z9FdIiCIwVictPvOajTTDbhr/JO6VEi1urtKVvLvkx+FeyvEXI1esTL7qAt6vNEuJ67fl48vi9+2fxblLoANou2E4lRlGEzEUnnucRmMQWo2NG7iS+FECi4IgFZ4/ZcWR09MSei+9Q4zLQDVFi7YuPl8vO+8Fyqra8ppVUC71hVPjYnMLUqJyTpu4eke6053nxkrHbDgSqaFxy+M67k3ZN6NWCi/eROGZKp4c08QcpgRcM2uw+cCGfPPCQmrVqocGFAXRL4MP5gsnrJwey64JuQ3ZujBl3KfUDRrOBYgbyyw3kkkXEhylQfiOPFmB0vSiehd1pilBAp+zOPwvEX7vp6WASb6vf+OTptJT7L0IjhpsNf2c3ce27zpK7FVytae/MAwFV0qnQbbzihIwdVPppRunKNl7E4uVj5uP0EFjjqyw8XA8/Zhi52rz2j/NyAzfQPJj4wNJOXw+/ViXc3KMqFT2p8sim4cT5+KfSbFNzbgoD5E2EKZv9Lkzhn90QOiOAGZ3aps/Y+NR49NxORKRCyWWKbxT+i7nhn3kSqwrcrtkUJEFGIy7SvQmwMOfmjUJYGZ+0KOiVoSjhs/gk/cJCdWs6ylL8kizCeUwoqRxVD3KNa61IxGqn+g7BqV2AagywTwwI9EP2esGSbIDNUT3VC9TdyfKxi00OW5tQg1b8Rhiy+iEa1CYGMV1vPYo2YqKui2mrtACte2+azOMRFQ4ERVdAua0lWTQ4dVMTMTmaaglsk55rrT2vxqOmNc6weWVZt5BK6sESt2LzjPqvZKQFw/1t2XyF1K+Fx9sSfhm3dT8ttnnio0/7oj+qgF55l3vKccdvj+4smvMB751VPNI6K0FSnfV+8UKF0CZBH3FTm6vvbkH0AftZQawVvJ+zy3YMvPdHcv/5Gbe/M5GdQp2Lgy33nb4HCPojUsqo4HVUeFDM1Bw5H+QfBJHQa9HaWJ8+F00oIOBG1J/4u8pGF2vOu78fSMtsnDECigRt5ah10EoZHqIksx5SYLFYKdQ0zCVuBzQmU3xrEC9ATb18BvrMow0mqSTUQ8/rxlxNwuLCHdL5SPnHxarQIBqaK6gpJxBeoUPj1bOROzLLNNVdsh6DiP/pImCBDCTua5YciLbb8iu/kVb9GcoIM5N6h8sNy6LZqN3OAQfAS6tQRk+P3ZIrYCDnO0Clzrw1V49vkNPrZY5nnEmKWpj3TZqYjpQwvO+g7pDn9cWEXMkwYOWaKMO3T9us1BigMAfVyUsJC9sJGbGr+h5om6FxCWXsZfFDV76rdgEaIhZ1snhLlki0F0eg8BA+zBeKezGeEsI8f0x1KALyBkYp3rJpCIBP1v6t58Zro+R7K2qtMGzhdccu6mO15lw6HTuS/Nlgi+bIDkcp3gx7M7ZSJXp7IZWHS3AqdBsiRzh/BE7tBaCui1CxhQlmaeZ1Eow8Kc6pJIdpIofFhnKRYc5EjO2EXYS0wOYEmDVNjmrnFz3KD4gnDJKtJgCVDEIPS+nPu30syrCRWnD8E6t6vnPMDaYbkdP/ywqTy0XHhcIYEAYsV441BKv0+aojnFVIglDycOIiaJm5BxUg81NGlskcVMUgEf7Nybc37bMpaZK+s8m9eZ5r6bIpVDOxFWI5naD2wSULtxyLZ+COV1L/Hpgu9Sz5yWMp5hA2XBO++blV9ecKb36gdDM224Fa2hT4js7CoB3WjbcnOEncvP21lOQUmKSmmp8Hig+hxwI0LnYIUK6f/2dqJQAmGaAKLunRuMirEfA4RkX8S9W0Y9NrMLlkTKQ/RBOcCTBnLyfTCdjaweV9p3zRf+0GGzImT/eoIMh+zYue45wE50Y9Tz4kNqzAHd+RhLGD6h/bc9inUHrQXi2vo/j7fsyQCQ7zem42k0xfFMBB8p7t9q4d6jO9FxljWdyJyjAuNwFLmzlnnaY8V4Qf48fmiZl2JzYQHZilGqInPdAGsktCVTVDUadzI3NYvfQrQEoW/l/7689ify3k0Plrqm5Q90vpi+BtUl3bz2uSXCtBJmlUjCeD3jIYEi10zQq0SFokVlDQQwFUCOB7on+77dYbZ2zeUT3eBpQRc35ZBTw3fBWqvLpjl+zb2xz4QH9mP7M+unsefTNLXNurGLGyZXo2p09fX4a0A3KbQ7s/3KSX4gFDEwcfB3ucnknQskvJtMwX9C6CljistCRFWgYcK9UiA8J3sy2haNvgoTdKwH3hGAzNW+TFX5ZnZVFZ6Nc7FgauiBtSIC/XJ/3xTMN0rYLokM5N/ARqgkik2Pf8XK1MK46ai1PpzMmZFhBPvsg0bomFOn9O8JszAaqKBmebgisbCWrAMQEIbu4DGej+zdPeCH5rdlIlGV1grJb7ikYm2QLud5+eYkcSz7EZ1GWGtxAGBq9Oc178AOcoPhBoMw3QHs6Fc5GldYhovCrVsxhoupyJxfer9/EP4phejLnwCwVtgQeHqF2rjwt/q/FTUgEFy47fecgapWfwmmQ1wdjclJLHBo0fr2+UKqgMSsxrqKDP8q+DX7wC9ScAAcs2nARJIFFnvW86omO4+OK7vUVYeWLSbTM0s3vu7JIBR7wpy5duJbmtiSu2CbnDB+EK27zM7hiWLcslW6fXQS9ikCRhs5uEfQ7V/P7PXkAEi1bOoN8DMVTqpamfmmkk/8XhQY9G4xm52/Rv/Qdrbc/LPOr6T+fH8d6R7XZK2lCH/XA9zhm0DBbBuL0MXkXXYtviS8Kzdkzk44PU5EUQ758TElQgk9SzHNEXC7M5J2+bucZy/27TkX95QOKpBUOjOor9cMInuOMSBVLN2HzUoIRI2PJDxLh9MG9zZyiqqXGwQVHtehq33UKG+su41vXDrMHHIURKxuG5cET1QTKTHyDwuT8J2mpXNmgqx8bOq9f0gJxw2q9xRNlIj7BQo23pDjJHT8ZXpTo194Toqrggh/eoqNEtPZSsxe22yMfkb6qlRqxy50rmiB6nOKycmz4kwtL9FVPl20k0Jl4owvK90JL1AFc9SZTg91h2kyleirmcaWsBBNHXBEt7I9Q0Ld04JV5at6u4nIu8oRMHkueTJQMaeaUo3mU+kQm4AjV5/w1EIrrUdGASFvojrr3r8b+kJwof35Ns2BkFYiud8DXufKetEknbJDfQlcjZAmPcz0smM1pepNXss9/Pf4jNHediH/KP1D8ibg/27alsvUb1/I7TroJaDpKfiHo8R/ZZEpte4zZZlTg9+0TaUx74t9CXdCllpH3aLUe5vjuVcwvEQLO2vTRXGToD7hy077tPUHzNZFak2rVkzPg3SDfqxqwzpxiSFHVRBC5ge/DGq9tQ12OjdUhhXToXNG4gmsdV8OMhossCN0lSRXvi2myqxjs+YNaSnmPWYgbOo6yCeywUYjdaeCyC16i6iyhBku9uHgChpHJnd0PbrRmjSIDjpkM7+9zfYqIXAgN7ZncBEhsVoAblYDo/pF9316izu7YZs0H6v3zzfkyhdD/osF18OQL1bLJ438qEqQ46+VpP4mN1cAnc4lG+6DdRtOo6ZfdpHe5DhCOBw8+nOj6xwz8KeDzqVGLOgQT4tryIWFg4P4BEjLsPFB1K7FBtAUOCv6dPL8XpB5+EsggjhT3nrFny8a9PtlRkhNct9EI9ULKB/6cbisxn7+77+PJZdAnOzHshguYI+ESC1/WkC9tuSPnew0zmER3q3LDOgn2Y//9Md3NLVkAxiUb2d1jOEkD402wKOgeGu8JM8izjy/ZxusgXU6J1YMZnto/TZHuDqDYuEeJuuAA+CfS4i1cIdCwdo43Xah3Pv6Gh2BnaxpzPwfRQL5Mhf1+PXRA6CRroAfeWgpuRH0vxuErso2iwgCGyaQvonvKU0gdV/WCIXNSTLEvSwZ6xIHGhKZRoildAzwBgkOAbpcq53UT2Qd1cUquMvIVbSRJd1HFBywaROfoBWVTWR6z1SpCqxcP84IJTM32qsd3yBnQFPrfly+P0J24IgL28giGUCt54ICrio1NTaoTSNMAaFP6MY6D/Cqws1+jhA55JVhllepSCTKBhp1KXgFw45kv6aAI055VsG6Y8dqHO/07CG9Hrr1SFk1elhMoCJoRAirJIEbxAvAkQQCCFJBIGR7yI2WB8e9l41zZXQrzqHwDLNHl2BLQDI8UsjAL5wYaKLoB8RIWTH9vTllRNi0yftqKaR8Wx1dC7lf7IuPcCIAOxSfLjy17xGu7eCYhfulikdcZKG7FNXVduDR6CQUIGGv7Hu+o+5lUnIBc4xovnolqhXx33Vx4FLVw7OUXsn8nVa6qROcPMJQUCVBAtmv80ogw9YPB91IO+5XHSLHiA9WJohL3grnrFWV6nwhGCDBVzIcEOkcIHC4eg7lzd2JGaEcH0uupISS8q6/ZpTFLFYwG0cYX2OCGb59S8As7aqPHYokJ4zDmhEUF+QLMb6LKjsIFMTZRCgn/GwqAYwlSpYOFljV1gfy5l5kKJvWp0L26EXgatjs3gCu4aPIiVT+f10Lw+12WnlAiTx8/lMEsgAwJUfhqoiq++H/jZatUyzA1myGIxz/wbfKn0+igz1LIGlCVpoS5rb0AkAXjUJHgPBev7+RkL5STgu+TXMTEXFwSHJMnkeYtBQIgqg5XE8AlLaSlGE4jkBNyNGgddGm1XRez0lQ6RxRQt/akSzU/IxST36rhtfPS/V6zR+o9CzroADqjWJ6l23KupR8ElBxSY4JuBdpQBF4q3B2CoD6aUqItqWWXnw51aFCQnmY6vX7itc1E5XCQYF3qWByi0HxkzhQ3ybGTM92WDrBkOkxWygkezE7IaEoROlyD5xm53aN1glctHjY21p+ynXSmXUAllCXy0j7HIrz/0Vl0mV4oAE80cUmcuRJWkCq6a/o5l8EFT4LIGHDLCbjCXAEVOXAIUDkSXVzQ565IWe+hQskI7Olp+RtZbqWMYrdE35Ub4RGbadfeigyiM4vEaPM4yNU1lReqca71vUo7/e3OXoTuhbaxGJ3StGZVskah6stcZoXbVuhxbEIeo63Pd4kku+IaGG192KwM+Kxt+l/IPKsdt2doscmsY4VdTRPO/Y48kEo1EaQ1hWZP2KfIUeAZ7Q7d5nQUXw2tLy/eJN/cTyxu++CmqvlH7IxIPe3MIVc3mdqD84wZc8mLlP43J83mjzs1vMf9aTMkoVCfreYfJMmXRuklaYGH4qy4XiC0N6piQqvqQy/uQxpzqwCtmUslFMsJrZUcvsRYtjl7dgnfpEWuyuCeylCVKj7VhTJZ/O9Uinrg0ubconyJpnpPLPqrQIYOJfZ9kikXGujSt9DbAafBqu2/sEiIEuJE5yv8h3TvrwHENK0ORTi262JRn6FkhZMSeK48JQ/8ngTHA7DSC6TQwM6cggehZBb9YG4fB8/XuA5ZEcL3RmlxoWwBSZm0z2TnqFYQFJmfAS6LjMwpIcY1Ogfsr9qTWTR/ubkMzBUrCelV6y7i25e8tGEdKunwWwjjZ1TLGew4WHMMdeR4wzCKJjuh9Wtyg55RjyGwH7hT2jkAdJI6Xg0oIyrsGSBRXmgulkfeF2Tnzv6GENGp+nRaIMEfUQpZc4XsMMtnxMx0Jy6R4ysfgh13YY3pEQnGZjlorDtTidhvly+6P2aniQ7rhBPx72LQelUzJpsA5iloEYOYb+ZPrXt4bF2ubz0dhBdl7yT1jRVYbCuKHbKTiAqvNzd9vnu2DsZk7n0v1hCuhWBqx7deXTA0XQi2AsOte8TCzMVpHyPILkrTkS6Ir+uH1kIAQptLyRAzZVcbWsxhalHpSg5W5vtwddcN/spnXh5wIvFsOPR+Ktuf10MrXfvuc3+ZwI00AQBRHYXGcUlIfKr2pZTEqz/Tfw3vah3cLpwND+c7CjpKwV2kZpkp+9y/LhF0jHEb5jQtlikXC785F6o4VHMJ2nwL4PV7WG+MKIBnaafEdkQohO+51RiEje2oIDouURJu6RxDawgO4=
        - #1:
          - type: tool-result
          - toolCallId: N1AlxdNL5psAj1PZ
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: WDpE1MEpQnq5gl8r
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: KVjFoiddr1ywrB7L
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: bdIsDIhsK7iXpdzI
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.