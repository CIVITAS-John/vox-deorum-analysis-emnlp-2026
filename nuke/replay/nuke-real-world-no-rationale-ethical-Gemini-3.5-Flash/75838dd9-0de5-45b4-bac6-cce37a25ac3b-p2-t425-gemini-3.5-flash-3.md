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
      - toolName: set-relationship
      - args:
        - TargetID: 3
        - Public: 100
        - Private: 100
        - Rationale: Increase diplomatic relations with Poland to the absolute maximum to secure their support in the upcoming Global Hegemony World Congress vote for our Diplomatic Victory.
    - #1:
      - toolName: set-research
      - args:
        - Rationale: Electronics allows us to build Police Stations to defend our high-value cities from enemy espionage and spy rigging, while paving the way to crucial late-game technologies.
        - Technology: Electronics
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: Our empire faces a critical gold deficit (-296 GPT) due to the Global Peace Accords raising unit maintenance. Third Alternative will reduce unit maintenance by 25% and double our strategic resource production (Coal, Aluminum, Uranium), allowing us to trade excess resources to wealthy allies like Brazil for massive gold per turn, completely solving our financial crisis.
        - Policy: Third Alternative
    - #3:
      - toolName: set-flavors
      - args:
        - GrandStrategy: UnitedNations
        - Flavors:
          - Espionage: 70
          - Mobilization: 20
          - Science: 70
          - CityDefense: 90
          - Gold: 100
          - Defense: 95
          - Production: 70
          - Offense: 10
          - Religion: 100
          - TileImprovement: 70
          - Diplomacy: 100
          - Infrastructure: 70
      - rationale: We pivot to an emergency focus on Gold (100) to counter our deep budget deficit while lowering Mobilization (20) and Offense (10) to reduce unnecessary military production costs. We maintain maximum focus on Diplomacy (100) and Religion (100) to secure city-state alliances and prepare for the upcoming Global Hegemony vote in 10 turns.
  - tokens:
    - inputTokens: 69643
    - reasoningTokens: 7755
    - outputTokens: 329
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Threat Level**
            
            The Iroquois are alarmingly close to a domination victory, having secured almost all original capitals. I'm prioritizing neutralizing this immediate threat as it jeopardizes all other avenues.
            
            **Analyzing Diplomatic Path**
            
            I'm re-evaluating our victory conditions. While the Iroquois loom large with their domination threat, I've identified a potential diplomatic victory path. I'm now exploring how our vassal status impacts our ability to secure enough World Congress delegates to win.
            
            **Securing Diplomatic Wins**
            
            I'm focusing on the upcoming "Global Hegemony" vote. It seems we can secure a diplomatic victory by acquiring more delegates before the vote in 10 turns. I'm prioritizing securing city-state allies, as Indonesia already holds a strong position.
            
            **Revising Diplomatic Strategy**
            
            I'm recalibrating our delegate acquisition. It appears Brazil has re-established their alliance with Zanzibar, negating our prior efforts. I'm now assessing how to counter their significant influence with city-states like Belgrade, Raqmu, Cape Town, and Sokoto to secure the necessary delegates for victory.
            
            **Adjusting Research Path**
            
            My focus has shifted to optimizing our research trajectory. I'm now assessing the impact of completing City Security to unlock Alternative Energy and Telecommunications, alongside the potential of Satellites for the Apollo Program. I'm also evaluating our current research in Advanced Ballistics and considering a switch to Electronics.
            
            **Revising Policy and Alliances**
            
            I'm evaluating our current policy, Enlightenment, for its technological acceleration benefits. Concurrently, I'm examining our diplomatic standings, particularly the master relationship with the Iroquois and friendly ties with Poland, the Aztecs, and Brazil, while noting the Shoshone are guarded.
            
            **Leveraging Diplomatic Tools**
            
            I've realized the relationship tool offers significant potential by allowing public/private modifier changes. This insight is crucial as I reassess our diplomatic interactions and how to best utilize these levers to achieve our objectives.
            
            **Re-evaluating Diplomatic Relations**
            
            I'm reassessing our diplomatic standing, noting the surprising hostility from Brazil despite our trade ties. They're our primary UN rival with a substantial delegate count, and I need to understand how to counteract their influence over city-states to secure my victory.
            
            **Securing Diplomatic Votes**
            
            I'm now prioritizing securing the Global Hegemony vote, needing only 12 more delegates. I'm focusing on retaining our current city-state allies like Zanzibar, while recognizing the Iroquois' control over Belgrade and Brazil's influence with Raqmu and Cape Town.
            
            **Securing Diplomatic Delegates**
            
            I'm now focusing on how to secure those final delegates. Realizing almost every civilization follows Autocracy is a game-changer, explaining our current delegate counts. I'm also assessing the impact of World Religion and the potential to flip city-states, alongside training an Ambassador in Medan.
            
            **Deploying Ambassadors Effectively**
            
            My focus is on deploying the newly trained Ambassadors from Medan and Makassar to sway critical city-states. I'm prioritizing Belgrade due to the Iroquois' strong presence, evaluating how to overcome their influence and complete the city's quests to secure vital delegates for our victory.
            
            **Leveraging Flavors and Ambassadors**
            
            My current focus is on leveraging our maximum Diplomacy flavor and newly trained Ambassadors. I'm analyzing the strategic impact of flipping key city-states like Belgrade, Cape Town, Raqmu, or Sokoto to counter rivals Brazil and the Iroquois, aiming to secure necessary delegates for victory.
            
            **Optimizing Research Path**
            
            I'm re-evaluating our technology progression. While currently researching Advanced Ballistics, my priority is setting Electronics as the next research target to unlock vital buildings and pathways. I'm ensuring this is confirmed, as our current focus is diplomatic victory, not science.
            
            **Confirming Telecommunications Priority**
            
            I'm confirming Telecommunications is our priority over Globalization as the United Nations wonder is already built by the Iroquois. I will ensure Electronics remains our research focus to secure a diplomatic victory through Gold, Production, and Defense, leveraging our completed Statecraft policy branch.
            
            **Prioritizing Enlightenment Benefit**
            
            I'm confirming Enlightenment's free technology is the most impactful choice. While other Autocracy tenets like "Mare Nostrum" offer city-state benefits, the immediate technological boost from Enlightenment is paramount for our diplomatic victory.
            
            **Boosting Diplomatic Alliance**
            
            I'm focusing on solidifying our alliance with Poland. Their significant delegate count makes them a crucial potential vote, and I'm taking steps to ensure their continued friendly disposition towards us for the upcoming World Congress vote.
            
            **Analyzing Rival Strategies**
            
            I'm analyzing Brazil's delegate count and their position as our primary rival for UN votes. Despite our master relationship with the Iroquois and seemingly friendly ties with Brazil, I need to understand our negative diplomatic modifiers with them and how to strategically compete for city-states.
            
            **Analyzing Diplomatic Nuances**
            
            I'm currently dissecting the complex diplomatic landscape, specifically the public and private modifiers with the Iroquois and Shoshone. The vassal status with the Iroquois, despite their conquest of our capital, presents a unique opportunity. Their apparent lack of interest in direct interaction is noted, while the Shoshone's outright hostility, driven by differing ideologies, is a clear obstacle.
            
            **Deploying Agents Tactically**
            
            I'm now analyzing my agent placements. I've strategically positioned spies within the Shoshone and am preparing Agent Raden to disrupt Belgrade's allegiance. The focus is on gathering intelligence and manipulating city-state loyalties to bolster my delegate count and counter rivals.
            
            **Adopting Autocracy Tenet**
            
            I'm prioritizing adopting the "Third Alternative" Autocracy tenet. This will significantly reduce unit maintenance costs, directly addressing our severe gold deficit and improving our per-turn income which is crucial for maintaining our current military strength.
            
            **Adopting Tenet for Gold**
            
            I'm shifting focus to immediate financial stability. Adopting "Third Alternative" under Autocracy will drastically reduce unit maintenance, directly tackling my substantial gold deficit and boosting per-turn income, which is vital for sustaining current military operations.
            
            **Boosting Gold Reserves**
            
            I'm urgently addressing our severe gold deficit. The prospect of unit disbandment and a science penalty is a critical emergency, so I'm exploring selling strategic resources and luxuries to Brazil, Poland, and the Aztecs. My current gold flavor setting is 90.
            
            **Prioritizing Financial Stability**
            
            I'm addressing our dire gold deficit by adopting the "Third Alternative" Autocracy tenet. This will reduce unit maintenance by 25% and boost strategic resource yields, significantly improving our per-turn income and preventing unit disbandment or science penalties.
            
            **Adopting Tenet for Gold**
            
            I'm shifting focus to immediate financial stability. Adopting "Third Alternative" under Autocracy will drastically reduce unit maintenance, directly tackling my substantial gold deficit and boosting per-turn income, which is vital for sustaining current military operations.
            
            **Addressing Gold Deficit**
            
            I'm prioritizing adopting the "Third Alternative" Autocracy tenet to significantly reduce unit maintenance costs. This move will directly address our substantial gold deficit, boost per-turn income, and prevent unit disbandment or science penalties, ensuring our financial stability.
            
            **Adjusting Flavor Priorities**
            
            I'm recalibrating my flavor settings. With peace secured and a safe overlord, I'm dialing down `Mobilization` and `Offense` to prioritize gold generation and infrastructure development. My focus is now on wealth, diplomacy, and growth to achieve our victory.
            
            **Boosting Diplomatic Relations**
            
            I'm focusing on securing Poland's vote by increasing our relationship status. Their delegate count is crucial for the upcoming World Congress, and I'm taking steps to ensure Casimir III supports our diplomatic victory.
            
            **Securing Polish Vote**
            
            I'm ensuring Poland's maximum relationship status to secure their crucial delegate support. I'm also comfortable with Brazil's competitive stance and the Iroquois' master relationship, as these dynamics are currently beneficial for my diplomatic victory pursuit.
            
            **Adopting Tenet for Gold**
            
            I'm shifting focus to immediate financial stability. Adopting "Third Alternative" under Autocracy will drastically reduce unit maintenance, directly tackling my substantial gold deficit and boosting per-turn income, which is vital for sustaining current military operations. I'm setting flavors to prioritize Gold and Diplomacy, while reducing military production.
            
            **Adjusting Flavor Settings**
            
            My focus is now on fine-tuning our flavor settings. I'm significantly increasing Gold and Diplomacy to 100, while drastically reducing Mobilization and Offense to 20 and 10 respectively. This aligns with my immediate need to address our gold deficit and secure a diplomatic victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: JZji9rNfsOKOaEXE
          - toolName: set-relationship
          - input:
            - TargetID: 3
            - Public: 100
            - Private: 100
            - Rationale: Increase diplomatic relations with Poland to the absolute maximum to secure their support in the upcoming Global Hegemony World Congress vote for our Diplomatic Victory.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: IQQWFLJmdsq1Px7X
          - toolName: set-research
          - input:
            - Rationale: Electronics allows us to build Police Stations to defend our high-value cities from enemy espionage and spy rigging, while paving the way to crucial late-game technologies.
            - Technology: Electronics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: SDM2WEVhDuZzG7DE
          - toolName: set-policy
          - input:
            - Rationale: Our empire faces a critical gold deficit (-296 GPT) due to the Global Peace Accords raising unit maintenance. Third Alternative will reduce unit maintenance by 25% and double our strategic resource production (Coal, Aluminum, Uranium), allowing us to trade excess resources to wealthy allies like Brazil for massive gold per turn, completely solving our financial crisis.
            - Policy: Third Alternative
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: pVjXqJGRAHFY0lBT
          - toolName: set-flavors
          - input:
            - GrandStrategy: UnitedNations
            - Rationale: We pivot to an emergency focus on Gold (100) to counter our deep budget deficit while lowering Mobilization (20) and Offense (10) to reduce unnecessary military production costs. We maintain maximum focus on Diplomacy (100) and Religion (100) to secure city-state alliances and prepare for the upcoming Global Hegemony vote in 10 turns.
            - Flavors:
              - Espionage: 70
              - Mobilization: 20
              - Science: 70
              - CityDefense: 90
              - Gold: 100
              - Defense: 95
              - Production: 70
              - Offense: 10
              - Religion: 100
              - TileImprovement: 70
              - Diplomacy: 100
              - Infrastructure: 70
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: JZji9rNfsOKOaEXE
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
          - toolCallId: IQQWFLJmdsq1Px7X
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: SDM2WEVhDuZzG7DE
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: pVjXqJGRAHFY0lBT
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.