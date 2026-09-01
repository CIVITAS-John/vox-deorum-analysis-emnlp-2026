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
      - toolName: set-flavors
      - args:
        - GrandStrategy: UnitedNations
        - Flavors:
          - Culture: 40
          - Offense: 0
          - Mobilization: 10
          - Gold: 100
          - Defense: 30
          - Infrastructure: 70
          - Happiness: 60
          - Science: 50
          - Diplomacy: 100
          - Growth: 70
          - Production: 50
          - MilitaryTraining: 30
          - Religion: 60
          - CityDefense: 30
          - TileImprovement: 70
      - rationale: We are facing a severe gold deficit of -296 GPT with only 411 gold in our treasury, putting us two turns away from bankruptcy. To prevent this, we are initiating an emergency financial pivot: maximizing our Gold flavor to 100, heavily deprioritizing military mobilization and training (reducing Defense/CityDefense to 30, Offense to 0, Mobilization to 10) to stop unit production and maintenance, and maintaining high focus on Diplomacy (100) and civilian Growth (70) to stabilize our economy and maintain city-state alliances.
    - #1:
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: We are setting our next technology to Satellites to unlock the Apollo Program and gain complete map visibility. This is vital for keeping our options open for a potential late-game Science Victory and maintaining strategic awareness of global troop movements.
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: Adopting Enlightenment as our next policy will grant us a Free Technology and +1 Happiness from Universities, allowing us to acquire a highly advanced technology instantly and boost our overall empire happiness and scientific growth.
        - Policy: Enlightenment
  - tokens:
    - inputTokens: 69607
    - reasoningTokens: 11816
    - outputTokens: 320
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Current Dominance**
            
            I'm currently analyzing our position as a vassal of the overwhelmingly dominant Iroquois, noting we're at turn 425 of 500. Their score is significantly higher than any other civilization.
            
            **Evaluating Iroquois Ascendancy**
            
            I'm reviewing the current game state, specifically the Iroquois' overwhelming strength as our overlords. They've captured all but one capital and possess immense military power, putting them on the cusp of a Domination Victory. This necessitates a rapid re-evaluation of our strategic options.
            
            **Analyzing Diplomatic Levers**
            
            My focus has shifted to our diplomatic standing and the implications of our vassalage. With the Iroquois on the brink of domination and holding a majority of delegates, I'm exploring the nuances of victory conditions under their rule and reassessing our path to potential Diplomatic success.
            
            **Choosing Future Research**
            
            My thoughts are on the upcoming technology research. `Advanced Ballistics` is nearing completion. I'm weighing whether to prioritize `Satellites` for its strategic benefits or `Electronics` given our current options, especially considering the Iroquois' looming victory.
            
            **Deciding Next Research**
            
            I'm weighing the benefits of `Satellites` for science and vision against its utility for our chosen Diplomatic victory path. I'm also examining policy options under `Enlightenment` to see how they might influence this decision, looking for synergies with our current strategy.
            
            **Adopting Policy Choices**
            
            I'm currently reviewing our policy branches, particularly the `Rationalism` branch. Adopting `Enlightenment` seems beneficial as it grants a free technology, a valuable asset given the current game state and our ongoing research priorities.
            
            **Revising Technology Path**
            
            I'm re-evaluating our technology trajectory, specifically whether to prioritize `Satellites` or `Electronics` next. With `Advanced Ballistics` nearly done, I'm considering the implications of a free technology from `Enlightenment` for a more expensive research, while also strategizing to prevent an Iroquois domination victory or achieve our own Diplomatic win despite vassalage.
            
            **Securing Delegate Votes**
            
            I'm actively working to secure additional delegate votes for the upcoming World Congress. The immediate priority is re-aligning city-states like Cape Town, Sokoto, and Raqmu away from Brazil, and Belgrade from the Iroquois, to bolster our diplomatic strength and prevent an Iroquois win. The recent successful retrieval of Zanzibar is a positive development.
            
            **Securing Delegate Votes**
            
            I'm actively working to secure additional delegate votes for the upcoming World Congress. The immediate priority is re-aligning city-states like Cape Town, Sokoto, and Raqmu away from Brazil, and Belgrade from the Iroquois, to bolster our diplomatic strength and prevent an Iroquois win. The recent successful retrieval of Zanzibar is a positive development.
            
            **Gathering Delegate Votes**
            
            My focus is now on Belgrade. With Agent Raden en route, I see a clear path to securing their allegiance, especially since they are close to our influence. I'm also confirming how our diplomats' "Schmoozing" in Brazil and Poland impacts delegate acquisition in the World Congress, given Poland's friendly status.
            
            **Analyzing Vassal Voting Constraints**
            
            I'm reassessing the Global Hegemony vote mechanics under vassalage. It appears my votes are indeed compelled towards the Iroquois, significantly altering our diplomatic victory projections and necessitating a complete strategic pivot.
            
            **Assessing Diplomatic Stalemate**
            
            I'm grappling with the constraints of our vassalage. It appears my delegate votes will be absorbed by the Iroquois for the Global Hegemony vote, shattering my diplomatic victory hopes and forcing a critical re-evaluation of our independence strategy before the vote concludes.
            
            **Investigating Rebellion Viability**
            
            I'm scrutinizing the feasibility of rebellion, specifically if the Iroquois possess the "Iron Fist" tenet. Their heavily invested Autocracy tree suggests they likely do, which would block both external liberation and internal revolt. This significantly complicates any path to independent victory.
            
            **Pivoting to Science**
            
            My current thoughts are centered on a potential shift towards a Science Victory. I'm evaluating the feasibility of launching a spaceship, as our high science output and the Iroquois' incomplete spaceship progress present a viable, albeit challenging, alternative given our vassal status.
            
            **Prioritizing Satellite Research**
            
            I'm confirming that a Science Victory is achievable as a vassal and the master loses if the vassal wins. My immediate focus is securing `Satellites` for the Apollo Program, so I'll research it after `Advanced Ballistics`. The `Enlightenment` policy in eight turns will then grant a free technology, which I'll use strategically.
            
            **Challenging Vassalage Constraints**
            
            I'm confronting the reality of my forced votes towards the Iroquois for Global Hegemony, which means I cannot achieve a Diplomatic Victory. The immediate challenge is to prevent their victory, which seems inevitable if I'm compelled to support them, forcing a critical strategic pivot.
            
            **Disrupting Delegate Alliances**
            
            I'm focused on severing Hiawatha's delegate advantage by allying with Belgrade, as he currently relies on their support. My analysis indicates he only has one other allied city-state, so this move should significantly cripple his delegate count.
            
            **Assessing Iroquois Victory Threat**
            
            I'm confronting the imminent Diplomatic Victory of the Iroquois due to my compelled votes. My analysis indicates Hiawatha's Autocracy ideology, coupled with his delegate strength, will secure him the win in nine turns unless I can disrupt his alliance with Belgrade. Declaring war is a suicidal option given their overwhelming military might poised at our borders.
            
            **Challenging Diplomatic Constraints**
            
            I'm exploring paths beyond a Diplomatic Victory due to forced voting. My thoughts are now on the possibility of achieving independence through rebellion, assessing if the Iroquois' Autocracy tenets might prevent this. If not, a rapid shift to a Science Victory is being considered, focusing on securing `Satellites` for the Apollo Program and leveraging the upcoming `Enlightenment` policy.
            
            **Analyzing Rebellion Restrictions**
            
            I'm confirming that peaceful independence is impossible. The "Iron Fist" tenet likely prevents liberation via World Congress, making rebellion the sole recourse if Hiawatha has it. I'm investigating alternative victory paths, leaning towards a Science Victory with `Satellites` as the next research priority.
            
            **Challenging Vote Mechanics**
            
            I'm reassessing how my votes are compelled in the World Congress due to vassalage. It seems my votes for Global Hegemony are indeed forced towards the Iroquois, making a Diplomatic Victory impossible and necessitating a pivot.
            
            **Devising Last Ditch Efforts**
            
            I'm contemplating a drastic gambit: if the Iroquois are poised to win, I'll aim to ensure they don't achieve it through a Shoshone conquest. My focus is now on whether I can disrupt their impending domination by potentially sacrificing our own position, especially considering their advanced army and proximity to the Shoshone capital.
            
            **Revising Grand Strategy**
            
            I'm reassessing our grand strategy given the current game state. While `UnitedNations` prioritizes gold, science, food, and city-state alliances, which are generally beneficial, the overwhelming Iroquois dominance might necessitate a more aggressive or specific approach to secure victory or survival.
            
            **Addressing Gold Deficit**
            
            I'm confronting a critical gold deficit, losing 296 gold per turn despite active trade routes and city-state alliances. The extensive military upkeep for 69 units appears to be the primary driver, threatening to deplete our remaining 411 gold within two turns. This requires immediate fiscal restructuring.
            
            **Prioritizing Fiscal Stability**
            
            My current thoughts are consumed by our alarming gold deficit. The rapid depletion of our treasury due to significant military upkeep is an emergency, threatening our science output and unit integrity. I'm focused on immediately adjusting our internal priorities to heavily favor gold generation.
            
            **Adjusting Fiscal Priorities**
            
            My immediate concern is our critical gold deficit. The recent World Congress enactment of "Global Peace Accords" has drastically inflated unit maintenance costs, leading to a per-turn loss of 296 gold. I'm actively reallocating policy points, reducing military production, and prioritizing gold generation to avert financial collapse and maintain our research momentum, with `Satellites` now the chosen next technology.
            
            **Verifying Trade Route Yields**
            
            I'm double-checking how trade route yields are presented, confirming that "From" values represent our income and "To" values are what the recipient receives. This clarifies that some of our trade routes to the Iroquois are indeed costing us significant gold while providing minimal return.
            
            **Investigating Expense Outflow**
            
            I'm puzzled by our massive gold expenditure. My calculations show we have a gross trade income of nearly 2000 gold per turn, yet our net is a deficit of almost 300. I need to pinpoint where the remaining 2300 gold is disappearing each turn.
            
            **Reducing Gold Drain**
            
            I'm analyzing the primary drivers of our current gold deficit, which is substantial due to extensive unit maintenance, numerous late-game building upkeep costs, and a significant 25% tribute to the Iroquois. My immediate focus is on reallocating policy points and drastically reducing military expenditures to stabilize our economy.
            
            **Prioritizing Economic Stability**
            
            I'm drastically re-evaluating our economic priorities, significantly reducing military spending by adjusting policy flavors to favor gold generation. This recalibration aims to halt our severe gold deficit and ensure financial stability, paving the way for our chosen science research path.
            
            **Analyzing Vote Mechanics**
            
            I am analyzing the World Congress mechanics and discovered a crucial detail: if no civilization secures enough support to win, the top two gain permanent delegate bonuses. This provides a glimmer of hope, suggesting the game might not end immediately after the first vote, and there's a chance to influence future sessions.
            
            **Analyzing Victory Thresholds**
            
            I'm assessing the World Congress voting mechanics and have identified that Hiawatha will decisively win the current vote, exceeding the required delegate threshold. I'm exploring if any diplomatic adjustments with Poland could offer a last-ditch alternative for survival or influence.
            
            **Stabilizing Our Economy**
            
            My focus is now on reversing our critical gold deficit. The recent "Global Peace Accords" has drastically increased unit maintenance, resulting in a 296 gold loss per turn. I am actively reallocating policy points and drastically reducing military production to prioritize gold generation and maintain research momentum toward `Satellites`.
            
            **Adjusting Fiscal Flavors**
            
            I'm recalibrating our civilization's policy flavors, significantly reducing military and production priorities to drastically boost gold generation. This adjustment is critical to counter our severe gold deficit and ensure financial stability for our continued research towards `Satellites`.
            
            **Prioritizing Satellite Research**
            
            I'm confirming `Satellites` as the next research target following `Advanced Ballistics` to enable the Apollo Program for a Science Victory. The `Enlightenment` policy branch will be adopted next turn, providing a free technology, which will further accelerate our progress.
            
            **Stabilizing Our Finances**
            
            I'm actively working to reverse our dire gold deficit, which has been exacerbated by the "Global Peace Accords" and high military upkeep. My immediate focus is on reallocating policy points to prioritize gold generation and drastically cutting military production to ensure financial stability and continue our research toward `Satellites`.
            
            **Implementing Economic Recovery**
            
            My focus is on executing a multi-tool strategy to address our gold deficit and secure our research path. I'm implementing a flavor adjustment for maximum gold generation, setting our next research to `Satellites`, and adopting the `Enlightenment` policy to secure a free technology, all crucial steps for our science victory pursuit.
            
            **Prioritizing Fiscal Recovery**
            
            I'm executing an emergency pivot to address our severe gold deficit. Maximizing gold flavor to 100, drastically deprioritizing military production, and focusing on diplomacy and growth are my immediate priorities to prevent bankruptcy and stabilize our economy.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: kdd5nw1nJZcWCoBZ
          - toolName: set-flavors
          - input:
            - GrandStrategy: UnitedNations
            - Flavors:
              - Culture: 40
              - Offense: 0
              - Mobilization: 10
              - Gold: 100
              - Defense: 30
              - Infrastructure: 70
              - Happiness: 60
              - Science: 50
              - Diplomacy: 100
              - Growth: 70
              - Production: 50
              - MilitaryTraining: 30
              - Religion: 60
              - CityDefense: 30
              - TileImprovement: 70
            - Rationale: We are facing a severe gold deficit of -296 GPT with only 411 gold in our treasury, putting us two turns away from bankruptcy. To prevent this, we are initiating an emergency financial pivot: maximizing our Gold flavor to 100, heavily deprioritizing military mobilization and training (reducing Defense/CityDefense to 30, Offense to 0, Mobilization to 10) to stop unit production and maintenance, and maintaining high focus on Diplomacy (100) and civilian Growth (70) to stabilize our economy and maintain city-state alliances.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: RZP3jwIIp116XjkC
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: We are setting our next technology to Satellites to unlock the Apollo Program and gain complete map visibility. This is vital for keeping our options open for a potential late-game Science Victory and maintaining strategic awareness of global troop movements.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: WA89qBk4OirNJukn
          - toolName: set-policy
          - input:
            - Rationale: Adopting Enlightenment as our next policy will grant us a Free Technology and +1 Happiness from Universities, allowing us to acquire a highly advanced technology instantly and boost our overall empire happiness and scientific growth.
            - Policy: Enlightenment
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: kdd5nw1nJZcWCoBZ
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: RZP3jwIIp116XjkC
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: WA89qBk4OirNJukn
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.