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
        - GrandStrategy: UnitedNations
        - Flavors:
          - MilitaryTraining: 50
          - Happiness: 80
          - Culture: 70
          - Gold: 100
          - Diplomacy: 100
          - CityDefense: 50
          - Science: 80
          - Defense: 60
          - UseNuke: 10
          - Nuke: 10
          - GreatPeople: 70
          - Mobilization: 20
          - Offense: 10
          - Production: 60
      - rationale: Prioritize Gold and Science to solve our budget deficit and advance our technology while drastically reducing our military and nuclear desire during this period of global peace. This also shifts our focus towards securing city-state alliances and preparing for the upcoming UN vote.
    - #1:
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: Research Satellites next to unlock the Apollo Program and pave the way to the Internet, which is highly beneficial for our late-game science and cultural progress.
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: Select Enlightenment to receive 1 Free Technology and boost happiness in our cities with Universities, strengthening our late-game scientific output.
        - Policy: Enlightenment (Continuing Rationalism Branch)
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: Ease our extremely hostile stance towards our master, the Iroquois, to avoid provoking their massive army while maintaining a realistic and guarded attitude as we compete in the World Congress.
        - Public: -20
        - TargetID: 1
        - Private: -20
    - #4:
      - toolName: set-relationship
      - args:
        - Private: 50
        - TargetID: 3
        - Public: 60
        - Rationale: Strengthen our strategic bond with Poland, our top friend and UN ally, to secure their support and votes in the upcoming UN elections.
    - #5:
      - toolName: set-relationship
      - args:
        - Public: 20
        - Rationale: Correct our strategic relationship with the Aztecs to be friendly, matching our Declaration of Friendship and co-vassal alliance.
        - Private: 20
        - TargetID: 5
    - #6:
      - toolName: set-relationship
      - args:
        - TargetID: 6
        - Private: -20
        - Rationale: Moderate our stance with Brazil to be a soft diplomatic rival rather than extremely hostile, aligning with our Declaration of Friendship and trade partnership.
        - Public: -20
  - tokens:
    - inputTokens: 69454
    - reasoningTokens: 9586
    - outputTokens: 427
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Current Situation**
            
            I'm currently engaged in a game of Civilization V, specifically the Ancient Era on Prince difficulty, turn 425. My primary focus is on analyzing our current status as a vassal to the Iroquois.
            
            **Analyzing Diplomatic Path**
            
            My attention has shifted to our diplomatic standing. Despite being a vassal to the Iroquois, I've discovered we are on the cusp of a Diplomatic Victory. With the United Nations built and a World Ideology enacted, I'm evaluating our vote count and the feasibility of securing enough support.
            
            **Evaluating Victory Pathways**
            
            My focus has turned to the upcoming World Congress vote in ten turns. I'm assessing our delegate count and considering how our alliances with city-states might influence the outcome, especially given the Iroquois' overwhelming military strength and delegate advantage. The core question remains: can I, as a vassal, achieve a Diplomatic Victory?
            
            **Refining Victory Strategies**
            
            My analysis now centers on the viability of different victory conditions. Direct confrontation with the Iroquois is clearly unfeasible. While a Diplomatic Victory seems within reach with the UN, cultural influence is a significant hurdle, especially with the Iroquois' immense cultural output. I'm re-evaluating the delegate count and our potential to sway the upcoming vote.
            
            **Securing Diplomatic Victory**
            
            With the World Congress vote imminent and only one turn left to prepare, I'm prioritizing immediate actions. I've realized we can still acquire more city-state influence by producing or purchasing additional diplomats and ambassadors. I'm also reassessing our policy choices, particularly the "Enlightenment" option and others under different branches like Liberty and Colonialism, to see if any can offer a last-minute boost.
            
            **Prioritizing Next Policy**
            
            I'm now examining my policy choices, specifically the upcoming "Enlightenment" selection. Given our current research trajectory, accepting Enlightenment promises a free technology and a science boost, which appears incredibly beneficial for accelerating our progress.
            
            **Researching Future Techs**
            
            I'm shifting focus from diplomatic maneuvers to technological advancement. Specifically, I'm prioritizing researching Satellites to unlock the Apollo Program and subsequently The Internet for a significant tourism boost, aiming for a Science or Cultural victory.
            
            **Revising Victory Path**
            
            I'm re-evaluating our research priorities. While Satellites seemed promising for a Science victory, my focus has snapped back to our Diplomatic Victory pursuit. I'm questioning if this tech truly supports that goal, or if a different path is more beneficial for securing the win.
            
            **Assessing Diplomatic Ties**
            
            My current focus is on evaluating the complex web of relationships, particularly with Brazil. Despite an unfavorable public opinion, they remain a declared friend and trade partner, with shared historical grievances against Indonesia and the Iroquois. I'm analyzing how to leverage this to our diplomatic advantage.
            
            **Analyzing Diplomatic Paradox**
            
            I'm grappling with a significant contradiction: while Brazil is our declared friend and trade partner, they are also our top UN rival. Simultaneously, I'm puzzled by our extremely negative stance toward the Iroquois, despite being their vassal. It appears my previous diplomatic decisions require urgent reassessment to align with our current objectives.
            
            **Adjusting Iroquois Relations**
            
            I'm re-evaluating my stance with the Iroquois. Since direct conflict is impossible due to their overwhelming military might, and remaining their vassal is key to our current diplomatic victory push, I'm considering improving our relationship. A more neutral standing might foster better trade and prevent accidental rebellions or harsh treatment, ensuring our continued survival and pursuit of the win.
            
            **Revising Iroquois Diplomacy**
            
            I'm adjusting our diplomatic standing with the Iroquois. To avoid provoking them while maintaining our vassal status and pursuit of victory, I'm setting our relationship to a less hostile, slightly guarded level. I'm also reviewing our alliances with city-states, noting recent shifts in allegiance.
            
            **Leveraging Espionage Operations**
            
            My current focus is on active espionage. Agent Raden has arrived in Belgrade, which is allied with the Iroquois. I'm assessing the feasibility of rigging elections or staging a coup there to gain influence, potentially flipping their allegiance. Diplomat Prapana continues to schmooze in Rio de Janeiro with Brazil.
            
            **Deploying Agents Effectively**
            
            I'm re-evaluating our spy placements. It seems counterintuitive to have multiple agents in the Shoshone, who we are technologically ahead of. My immediate focus is on redeploying these agents to the Iroquois to steal critical technologies, as they possess a significant advantage there, while navigating the risks associated with spying on our overlord.
            
            **Assessing Gold Reserves**
            
            I'm urgently investigating our negative gold per turn. My attention has pivoted to our 13 outgoing trade routes, specifically the Jakarta to Cardiff route yielding 52.85 gold. This financial drain is concerning and requires immediate attention to maintain our diplomatic victory pursuit.
            
            **Revising Gold Strategy**
            
            My current focus is on correcting our severely negative gold per turn. I've realized my initial understanding of trade route gold generation was flawed. The "Global Peace Accords" and high unit maintenance are the primary culprits, despite significant trade income. I need to drastically reduce unit count and re-evaluate trade routes.
            
            **Shifting Production Priority**
            
            I'm realizing Jakarta's "Infinite Project: Research" is a significant drain on needed gold. Switching it to a "Wealth" project seems like the immediate solution to our negative gold per turn, especially with a looming golden age and the need to fund science and other endeavors.
            
            **Analyzing Financial Discrepancy**
            
            I'm baffled by our current gold deficit, especially with Jakarta generating over 1000 gold per turn. I'm scrutinizing our diplomatic deals, particularly those with Brazil and Poland, to pinpoint where this substantial gold is being funneled away, as it's a major impediment to our victory pursuit.
            
            **Revising Unit Composition**
            
            I'm astonished by our unit count versus strength. With 69 units averaging only 318 strength, I realize I've accumulated too many obsolete or defensive units. My immediate priority is to identify and consolidate these, drastically reducing maintenance costs to fix our gold deficit.
            
            **Reducing Military Expenses**
            
            I've realized our vast, obsolete military is a colossal drain. I'm prioritizing reducing "Defense" and "Mobilization" flavors, which should compel the AI to curb unit production and alleviate our crippling gold deficit. We're not at war, so this massive army is unnecessary.
            
            **Adjusting Game Settings**
            
            I'm now focusing on optimizing our in-game settings to address our severe gold deficit and rebalance our priorities. I'm reducing military-focused "flavors" significantly to curb AI unit production and increase gold, science, and culture outputs, reflecting our peaceful state and victory goals.
            
            **Prioritizing Technological Advancement**
            
            I'm now focusing on future research. Satellites are critical for both Science and Cultural victories, offering the Apollo Program and The Internet respectively, while also revealing the map. This outweighs the immediate benefits of Electronics.
            
            **Reducing Nuclear Appetite**
            
            I've been reassessing our technology and policy paths, and my focus has now dramatically shifted. I've identified an uncomfortably high AI inclination towards nuclear weapons, and I'm actively reducing those flavor values to prevent devastating global conflict and align with ethical principles of minimizing harm.
            
            **Shifting Diplomatic Focus**
            
            I'm reassessing our delegate count for the upcoming World Congress vote. With the Iroquois holding a significant advantage, I'm analyzing how allying with Belgrade or specific city-states might shift delegate influence. This includes evaluating the impact of proposed resolutions to counter Indonesia's agenda.
            
            **Securing City-State Allies**
            
            I'm thrilled about the permanent city-state alliances secured for us and Brazil. My focus has shifted to Belgrade and Zanzibar, as they remain open for alliance and could provide crucial delegates for our Diplomatic Victory push, especially since others are now locked.
            
            **Refining Diplomatic Relationships**
            
            I'm now meticulously adjusting our specific diplomatic stances with key civilizations. My focus is on solidifying Poland's crucial UN support with enhanced friendliness, while simultaneously re-evaluating our inexplicably hostile relationship with the Aztecs and maintaining a carefully balanced, guarded approach with the Iroquois.
            
            **Correcting Diplomatic Mishap**
            
            I've identified a significant contradiction in my diplomatic settings with the Aztecs. Despite a Declaration of Friendship and being trade partners, I inexplicably set our relationship to a hostile -100. This needs immediate correction to a friendly setting of +20/+20 to maintain trust and our alliance.
            
            **Adjusting Diplomatic Scores**
            
            I'm reassessing our relationship scores with Brazil. Given the Declaration of Friendship and shared vassalage, the current hostile settings are detrimental; I'm adjusting them to a less confrontational, though still competitive, stance to better reflect our actual diplomatic status and goals.
            
            **Refining Victory Focus**
            
            I am currently reviewing the AI's persona values and confirming they align with our United Nations strategy. My next step is to meticulously adjust the technology research path, specifically prioritizing Satellites to facilitate both Science and Cultural victories.
            
            **Confirming Next Actions**
            
            I am finalizing the last few crucial steps before the World Congress vote. This includes confirming "Enlightenment" as the next policy for its science and happiness benefits, adjusting our relationship with the Iroquois to be less hostile, and strengthening our alliance with Poland to ensure UN support. I'm also correcting our relationship with the Aztecs to align with our friendly stance.
            
            **Confirming AI Persona**
            
            I am confirming the AI's persona settings align with our UN strategy and finalizing the research path to prioritize Satellites. I'm also adjusting our relationship with Brazil to be a soft rival, reflecting our Declaration of Friendship, and verifying exact technology and policy names for upcoming actions.
            
            **Confirming Policy Name**
            
            I am confirming the exact policy name for implementation. I will use "Enlightenment (Continuing Rationalism Branch)" for clarity. I've also verified that the `set-persona` tool is not needed, as our current AI persona is already optimized.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: PAYwdQETaq6XU7Gf
          - toolName: set-flavors
          - input:
            - GrandStrategy: UnitedNations
            - Rationale: Prioritize Gold and Science to solve our budget deficit and advance our technology while drastically reducing our military and nuclear desire during this period of global peace. This also shifts our focus towards securing city-state alliances and preparing for the upcoming UN vote.
            - Flavors:
              - MilitaryTraining: 50
              - Happiness: 80
              - Culture: 70
              - Gold: 100
              - Diplomacy: 100
              - CityDefense: 50
              - Science: 80
              - Defense: 60
              - UseNuke: 10
              - Nuke: 10
              - GreatPeople: 70
              - Mobilization: 20
              - Offense: 10
              - Production: 60
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1+NYvMAt0ZdwtOWO3iFcdms9Uqjbgm/9t8WVniKuov3VBAREMuWB9kGMCCsmeWj2VMqnasN3rw9dIVeWVgqkBU4vtf7B/+NJ+4czD3+thxP96UfyoLY8rwftuff2vtk2kEfQRdXi9D2ikXbia2Q/egeVAhW5rL7E/jHxnj/ozzK6iQHY1awgXX5djpFFVJpbtyg6GPjFIS2DEVtTY7Nlb0bMq62DrCLqVD4vNkDjCYjIzmDOhDqcahoSTQvEYmrMuADl9DZmWR4s+gBHJCFx6fjHA/ZHu0JWGEcNo7VLOx4Paj1JFy9W8TV5d+medVqgDWVb+zgBiXLagpdiYQQGxlmr0j5nSApyiZhzksrM/ki975sRzKISY919QqZXMvGiUVeEHZe32905t+8FMpnwikSmbkvUqxiSCzhuAHJa8h6sfe/TFU3Z4C5L/eDIEzBpu/75aYc7cRebIUdAVXNR6gfbjqNbTs0ZwuVD0nUd/h5qOxI67bN79uYq7Czj3U42mitW6RQr34VFFWzxyNQNvZiPESrcQENg7M6RUBtYMFh/iYbESHTI8y87ply+yNBD4uOXndRYNAkjLMv74cPqYrfcLArN8b+3JMYyk5uVoAniQc+Oa5qqGcM24b81x9croE8ZBK9ZN+ygBB/kKZrLLXNHNCebv9DUBmd+a/ZzKpCaFx26tKRdTHC02FPfXzmGvhbbPZOtsrHJMDtInfXaqWHVMMAKK1/TFHLcBEgLJ3H/Gssph7JdaQGCFPukCnldCrsZsBQIsSBDR/8i/OriaL7vfeAM+Ii+2NYYX7ZBdFddtDDqnG1YyRmtbbjiEUnUvNe2Hj8XjfOn0CXRHgTUUmv/iU4Mst3AjaoxoxLIyltW3iXkf+F14XSmvtZlEwlOCSBze8oRygWPT5YFX/HCxqxNwzRCcEvIJ/CQpQP214lgj7C+oc37H+P+Zst/SPuUIMVUFzTCthDp3Dh0AQ/xZwkKZAn2aK8eRx2uEtOSbcXfk+1anKYpt9nGGMb5jDRurJWLrfZcWrr88x2OVzBBEguULkT2Ogxt2FSsVENDpRv8rwYyIK/qD0B1gAXa0pEFU9hgSXQUbpDJ5WX58fE021JGr7OEO2nYdsCve4jv3UjfpscB1sDE/SU6+ax+lY/nu8M9LSPgF61z513xdI9VnrmyBzUVXurFWaIz1HbALnj38r5NpsltwCY3YH1SbsmPJ5tme+u4xuJhYEreHUkveXqq+KGIYPcxyO2YpyK1I4GCid/zsWnAOVpVdP1h0LMlqQ6Px1Qa3m3yZa3sNDucHQ8nfUDwecW0w3DM5H44nnIswHKoZEJzxlxeJ4Q8kLWLtuD0xTAZDYApZR19MT7LbuG2yfAUHmSmdQ6tSyXd9EUktSCuRw5sFPCXZKeYxSYV6HEkHALBu4yMy2/xNz1TM9M+zc6tIFZWE4lOz1Yp0Cif0HYTqlDrX3XXdvRg6JIWr1i8AeSWKQTcIYfTqmatVMsqf7VoUzSoFJcfKlC1/D1ZgzVq14nITXvhIjHB+vWKvnIL8Y4F3pznKBZQVP8Vje48X8ZAtU503fruDYGHwTW7FFHQkMMITPiU1NJRMb6MfVAFvBcSwANrtVOZnP8phHNN91v2NJIpu/mulIQIZbv8FDsfJYDBy5OeBDpJIACkeFaahGL+4p9bG5Y7CVO8q2O/GdvIRdH1JAg/b8PQUM9usgqqbqH8FlBPux7/OqdGjXExkgPJOPw24VkViywBw93lnMHhYv7vN/jrzoPqMaRT+O6iHisY17SiadNa5Lm1UDNIzPKeNcpPwXYvdWFhJ4UX0yds4rgng8BiJzhD+ndmDadVWzcqSzsl1Xf7WZfBLEO0FTffjeyhRLeIPbJrxrxhWjsuqfk/1XIacqV9pw45+5XTixiPgt9c3ivJd+EeKthyIwyHQ7TdXpmnr6ox+pe6eKyefhQ4gOa866y7FyMR2VmH7bt6W+PBGaGISbJrDMRJIN2WQHwytS6TAlxG5LwsFpGzdTc0On6+sNmEzcvJknmh9z5LVEvCtwhq7SQ+lRVaMk3urPPc+e+TIC7X9WOvDDpWi3jdinvkUCxOHU3I1PUS714dATVddVNlkBp5uJNpQdW8zzOFJntc2gUbgNZ3PbC6x/bztJcL+bcLiRD/FelU0PZmIFTC/SyiSC3UFuvS6WS4DPF90LidbAXoLFNBFhypGkXO6CsnHHtLFw2vqg/aRj4z8P4zy+CVkXEXhr4/iA3+A+Jm5EeA5EhWIUcdB+0RdF8fo7M1s/2lYgntzYv97v38Oh81wO1j9EmNaIDNXK7P3GWNEieMAeoVWNA2v1lxDIk42+/wkfstH8x6jvDIvOX7CtsHiBidTreUWHZKz7uNl2x71W2xEyaru9pPMTqB41oBzBft2zbOWlJj8oUY9QBTZrMt4fdik6rs3YKQ/yjaFWQgqEm/ryuI6mW6MteJXJ/nFmEP34DSVzpmqeToKgrParGGPE7k0AsuYx8f4evoFJzsS6KCxMHnWs40KnGwQI/c7fzR84v5y6M82opR5J2WFkdiOclwDC8sfy0wSD+WgpUikXf7iGQv4xOTdKIZHxuDbmtYiCrcom41ar2qSnDkGV0BqISMDTiCBQXw8LJaXRuLU8W4uhQClU6GzVugvukSuEMbQrrsbr6oNCkfB1Y2fHUQfhsAnzrNZ3b3IXMcGEoicJueQt9yzl9zgUhnl14q+SlgeInXkTD19P6PskCNWnbeXqKuvR4j6LrAuS9nNI2XzO4ZTtGqZYMU9Pl94gOfKu/6qUwNi+ItuX/fxZY1MMes/h/LVP/eL2mmL3u2TuIxwBKYe2jBdxrZzbyuW004Ntsu07Zh+vAnklK9eLvqUxGykLwesVPJV3fggpAs1zY8mCbkk+4ZqNUSSkllIwjsaTZb/DkinfWBvg3xEIk+n6G+9Zlda39rj8oAzsjcQOxr7Q3FCVXx+f3JZISDJTjtHaTbuJvy+gGkJYkj1vuu0zdDi7YQDn8xHvnLpga3t/Q6e111iuwNBpiIzCoXi/YY29wgvl3j7wgbgDZ3/ZC2bn+mkrEryvcZbRkvpRI8vIrDTVNTdFHjveD0Wyq1YRcIqjnr/FZw87Dbtg3rMNb2OkLjrbUq4HjESkB1RShsW4rji3B+q4XfUzYnzht4HnuioW7kV4y2MGJJyIkj0yUQIolv97K2GgXwuX/+of4jOtos4h41jjcTWxGQimMqxVHgL/qWkjc1S1ke9PZWLqu3SGKknY74LNTEziS5PKSJuI5RDs8J++9TQPPUoOJlnRiLpPjnc8mkZ8/IMt5Ot8+JEGUXZaSzURjl541LuTV07Lc/4CFhzlBurQJlRVJt7Y6wSrb5RjFbn7one8rwchcRQWdTpoMBm6KYYoZZ/CKH2jr2gQeEk6V0IyEdTNd/0XTkUmjxCAOci/DJuV7ti9LJ3W6eMYgQC3kYnQDJB2kw7XsXQBpcn2dBs7lSqCaqRpc60KSUPyXt90oUzn5fdSr07zmWRSFXGWgEcCvZuVEhg+g23w7qDpW8FcIARFbNunfvjXYm2zBsr3aX4TNX0Yrre8oWNDDLK6I9+Lc1vv/MU2GEnJT5sqJT4xc6Ce8EHO/6dp4PVwWm7NLApJUqvaXfT3UPIi0cnd7Jfi/pvX308YvrTgAWXaaTSbYy80I5sE7IDmHRVtY40/kTeDGK1FFKJ2A8m/nrhXqHDWotM9HG+B0X65UILlAvdthpisLs1Dd6nLTEziRcfsqsTaWx13z7pUjp4lJY7rETHDLfAOtvU96Iow1BUIJFv73RzYkvsS0xLDDxVM24MxQXYOqdbFGypt9TsTU/cGJItJnc2I3L2tXxLtFVAN65h2MQab4f+bhWTQ2e0E/1wEg+GEVfl1lGsMSkgt3tXKbXKi16GS9dtxgODl+2XO/+4jpV6w67xnTP+iX3aCFElcGk9YVT4B1n36Ez+H9vWJ2NKDES5q9V0920EELnKe88gHcw4sIxFzmxR+76QPOcW81RPC4j3JCOvhq0IqZZzFHB0Fi5Vsg4/wFkAneF0Sh2HEbF5DWx/ASlFI46rdOywTvBAHtwXjamzO9qwgoFzDlf7yto+k1ikI0c9Jg7LiC34YWUrK1HbinbyJl7qkgFFndf7hS0Qlub0Z/Eoccv5BQdrlnt1OFN5KtoleYSoCN6n4QhNpcYbKuVXVknVva+sewh4h441Iw/fsEWegmjYBoW9cHJuUogGG60+2i6eIzydOWTOZDqGDoXKjTQw8Mf1WnpG76O1vhfX05M4ULczR71DyYI+MR7FrheXeoQlh7uSRWqJ4uvs15z+nmbePQ1HQK4waJKeYgqLEcZGSMRr8k/bvc4aedLt+VIlpNKZ0dByC+CZfKVSeZKMQUHM+W/BdNQDRxfwofK3SlvpO1vLtHA05xuM887KzXekViFkqBsULExjXva0Tw2PKXJyF0zOMoaK/3Up8pw/aLrwUMM03ouEI6F4mIZWMtAWsBWDmKrLOgafI89Z5uNFFaPrA0GtOQKV/JFR2KEcDtSatAwv6BDhvTw6Nq2CAXp95MW4Pqa2ZQGTtCKkArOTOgmuPPmy7p1q/BCet9zKIpVLkZQruVSyvtkNJgjPeC2nKwZvygDqAtrD+yLxzENyAXrUo8NLFSlWBpEsTWEQewRLf+XqYnDA0JQ3JA2fkK256IzSuyKgMF6YKSDlOiEr3v+WjUoW3me2/OmsRhODMzc5s7anPiA+OQLI6LPK43P3Q8vq+7L/0p2Tmrgu7p2FOwHu/zsFG2y/iZ/PYKw3r2aDhJPvaDNDvau2zPCMLb/mjIt2Bmi2kbtyxTbPQ7Mv6vB59h5zMXc0Nhq9bkjKjCBT+nl8CJLvLtmGk7zJNi1CSI6SeEOGElSUjncxMVBBPJRul/0o8/lNoWHDB4Q08ur/4217UoP4dwPMjga0ajMF1A5p1AeyjiHZZHAQq0cEBtW2J+Z2a24ExjViSPQKzZn0Uo93YgRMChMaIPMyY4SeB+6pv/lAiYJUnEbl++MKP7pPJjkN6E1IfChXCvTiEd2ejXOZmaLNkXlWwzC3JYh0KwEAf1iPyDcc3/Sx0JyykPAKMsmtD/HBKjfrJrrrFZZZL5NA0etEra8H0XxodImZyVBydAI7bigzIBIee0E8YH2SC+SxOyLjpzBtbhBSrGpbAH/QTRgsY+uvmC104KIdLIvvo7iivGAUTcQk7C3x7RU26zUWiWVoIVRF3d4Yd5xPYvDfiryIdO2fmn32dJcs/sA7WYeFhykAZlQ6RM0yclggY6vkzDsfUAPFU1gxnPp+JCBwPLcA3pSiOT4g/2MaGIhG4vKV5IfG6XIjQn7sjeXtlUCWvs2P5bySeKkHDPcewXGa0O1EWhBhkOMobnGLkBlcM97RrtPkI+ZDlgDRe+61/sz5SdZ6kgCyh4hi5NMfcrVlfmwi/60o8KyOm8/Y0UsKmmRa8HUx3ZMFIR+Hw8Q9mfYAbVeY9VVVJqSHCF/SCemCoC3ieVQzQpoREQwjWZYkKw5U7pxdC0YGz9l4sbV8X8bt++WYbqyBR8yyXmxSBYISMpSkLX4/n6ysBmeqWWCdDOFCjTItyaXUXgNrdbaagv5X66VtEluPM3UrAaGj1jOojaiq/KBy5R8SQDyKVYcPTX8rgC22azqEncZ5Yag+RqA+G+0UgdRX0vGgeskozmBHk2jLdCigUCWaoFNAvKAtRYht6CtyM130mUjGsqcpYa8SyvsNo3KlMFyq1hjzOKWNBb8jdN7hSiEt0m5BiA+tjG3jUQIzqb5r1rmkPR1PVtab7zbc4syIYQ9cB85ALiYjlF9yYUoBIAd6lVjIgqMar0tl5nvEoW/rKA3aJ98c4sxarnAb3drqtSU5ocee+rQR2RMNHOn7nhFRg3Tiko4CM+5vQUnFl9dU1D/4FVKtxUlzb14FM+mZDRJqQELn5u8NAhQZld6cICyg0DmbmCZgvJMlgt0JW6+yMVYoYf5lbYRaZmkyZaeceBufsZlBDdGHcrFmLQ91QQN5/8EmG3f/0r3SEd2IcVLf+MZjoP/vFVoSMhI6VNTZn/2rurNtPSg9dEUE5wMFwvvoIQChCPiKofDZaBSxDcZWL5vBoqWdrjBxJNej6gWuZ5CnE7aqX9M5vRfsNLtU4wvn1SFpUEn1sjHdPLHrTjaPzKxFetZC6ehbFt42RJAmNBZfSCqRWMc7uMYaFL+GJIMpkoDU4OpvxWX+6yUMe8SE9vT1WFVwm5SV8tnR44zvBGW/M9eHjO3YOXDu8v+2NSQICTYJIqw1oybu4xUWzbTHQK1Lr1PMTWpb0Yzq09h47OJRv6Qa2KQQ3vyJ84oAuBFCRJTAe4MlGjPZyYouCtgbPau9hb0Psvz7DplN7vGudimxjfN9WTAJAW22fGqqlf+GgXmAAzXW+ZMh/Fgzx0VLbXRzYqqI+U/A+vumFuodYzSXQa2g9k09ThLfTK81/IOvzw9hH5rLzWVz/ofs4BrroEaI/IaxqidBkrpSpFRGXRGja/M2z4LEYICqbloZl+EeA+lxqY2V6iqdjOBVwoVBn1N1k9VJvyiQ2Y7bjCiSpyuMD3FRylzaIgDrbqT+L70KAuC6ADYSc5aY2/XCFpzwsRbCeV1SAH97jAiLPNNgDaY04zosCP/IxoNAoVGoVsjb2dmVknYFAc+s6wt3S8Oask05zp7ThQX4GE21OwcwMaYbfpekWG2Y05XAFy4zPRAxNd4QFUUMai0nGegkxsYV9D38kCoc1tWg2ePneBuTLRByGjcEflprXGTfU1CSLfEwFHxLfoo4hKZwOIOEUQHTE7R99siOap5wyO6fY8shVyfDnL4HVKg2m7XJyH57R0xdbKZNPA45RBdQ7HkNfUR9VIrdKW0YFGZ4laXBxQ2tGfG4/7yNCXDdjsjGM5EDf056EKzwvSA3ioGGlvD9EzKnVuxPz+FNJnQo5asn3o58jUeh1//XRtW1jr/fdS+e7RSssNXrTRJBNHM0ygplsRRCp6liCKIhrGF0wBa1NVnA1d9FtgLyc2BqC61oNHtHI0QMTEqzd7Ht+UU6dUCWru8gQj5u6DDkA9ySB5dJXUu3d1WfV+20CBPmIWwLJOgxM7kmJ5pmGCk3PWBClc0j67xpIyYjxo1Nr8yNreWdGPBiROnwUZbKB9NbSnT9QXFqrPIw0/LijGE9MOTb4YWoPrqaNfX5DS5aQb81e+tKcA6vpiuM438Qyj1H06iRpr74qnQJlSBfxtUevrCAYykuJJSxN3b4I4vDStt56vq4L5H/v+OEqgG6BIAp2uwVeZgijsXovoThl8GOC7inAjU5b8e2vhWcv5skHB9KcAwSHZncV5qW5wGjnA5puwEZfTrfuquD/OedjHyIXH5s5mDzllAxvS2AOo5ranso0vT6uKd7CdXsorO1lAwTu6k4rrXShgsHPWEWLBu/yaLH2tuHSMXf8K5K3pBo0V0uylvNtc1TPS4uJWy4fMFQohY9kB096vAqU7zzN13ntvUNz3CcyhWvOYVHuJScPym2u2wv7di/gYAEZraijEVkqUpeNTlQ9gCr9E6Bzi5A4CgA6htZ3UOd5fgXv06pbrrpMFh7vmDd0oZwMAN6z0fs0yn2MMBdT8wb0Yq8iS00PRM5EMEbB2JS6/CXFGUMf9JkEN0dWlLmoe/zA9XFId8n7FZ8fYZx2bmrW6C49vUdo1EJBQotJCdXtNZQHtZ9JgNzn2WGMjTi7a8zzZj0QrY3F8Uqrr7rCttosJkijYW5b8eczmKexKoMNvrOgydVqZfG5rJ9eugiWliRH1R1X0m5og3XXD90AgqO4OBEk6JyEDn/sN7RxezdM4tpefGiM5iAjOOQLk+uj99O9IjV84D6FH8iYZT9U45TOPj0dVG35XwuRa/4P+2olQEUPoEUnsqpRmaoHvzJiSSe5d8cQrPa3/759il3zhnnQoAxYEvyUfuTRyyoU34JxBJKx6pkhjEohv4K6Hryxlo/nRnDfeoD04M6P7qy+RvGhJ5RodgaQU7Id4wT9TNppMtaVSSthLeiB3I5dEVb5L0SOX783VssYgvzahTJqoPv0k2gftJTZqX3gR14I8ddXrXH53WTdonlK3Kshdhv4EgYnsN0G3/31t3dxzka2un8Bj1/6bPL5cxWpK7gXwMurmPd+aPAKAAlFBNXITX1FT1qXdOQJEosICFd2ycSn78aS+zWGKKoKpPxOe6SzUXWtrEv8X8Copg1JEtJfAZqs5LBRQu2xRopccAZqcBt8XQgcZHaEcPTqvzNskMx9YtOEJIvLChjJIzctdJ9PF+Eg/HBhFHZsHA42HRsmtr2NfKuwVmSo1FBbrOu8etFV7oQ2ZvpLi17DAmucR5ztZsnIddvetUHTM//zF4Kxd7fbrbiBsF2z1nw8/793dH3IzY4OqT19+ynJgj076/nrGlKB5OYWuY+HK99RjHO/79dU+NSknXGdoYUJ7lxBxbgk3/p0BmhCxXzefE5p2lyvDeQa0H4SdHm2tMXOALclQVooUogPQHKbfKxKXn7lv6FO4VpyGOWevC5CwEaSEwD4NkxOA7EAMFDG9H3OjWLpKO1i0reINSOIIwRcgPHnqEyMCZEfze4OZxTRluze4UpDHF9UB4FlhIYIvzyLzRghwdUYeqNrlAZK/OBbpKuwQ1NUW2Toe7mUyCZXKvG8yswFdMJy4qpuWHvUxhM3uwjgIV5ytEcbwmMFDTRVMWaEYfCEeebs6NJOWDpXiBdfgqy/sl170PrVM15vHgRnOFzsp3b2PQp1Mwn/k1HIZCASJjtJApXOHXE/qngZiXrc4Xhu0y7NDwMOa88g1M93CGvoZ5FTX3IPsTfl7GEqRfQ7qKRE9teIsXo8x1ASgS7k7CbXNPFL7K+WaoV7tAfbFYIOL7dVScW+gVImzL+BP9MM6dy5oLDdNKgVOpKtwFi1ahGs/HM2/aGZLg6AiASkTAkyncDhpSujCXn/VfUXMq3ahAJcb8OzOEHZpZs3nbY6Vo0huHVA+JCSC5ppjqDOi+F009xV3DOrSegkJ9U/3MhvKp9aolnaZMalDE7xU0c0GVeyP611HahdlhExnHvNulUSuZGxZZ7PgW0HNyN5N53qxhRoEkof0mHgn7VNVcdmtK5lN0tAktvbaesukh0p1Ot656NeFZgjcKiBTh+tsGkaA03++WieHwd+TF5BBEA2hMCmkSLFfEQ3wCqp/QYpnKgLbHI4l0E53BOReWMrgK+s9jLaXVAiMMRgwQeK14+7hgsm7a4Bhktka6+DJqDtBYDWngMsv8htRiF2zWsnMUUm1k0UcfAWLpvKX6/VGtRPWyzWn9TojpP/EgNMrjp186BbsQJAogNJvBnh5YDIjt4Z3/ruahT5TLdjLnY3H8HSCZF22+weKGxRj1CbkOcKJEW5zdliI6qqtPhJdPnJva63wv2byKIS0T0hoViF6ZNHSYkU5gv2P9I7VNSup/3wiMZXntbGbEqqPFhJhbVV6GZP8U6qzNxGecMz5fcrJdWOIBUHRIgzh7llc2BKWRe5W8V4jMu2IeAcJVznofbW0yP2livv0S4omhlVZn3cBMCS+Yf68HfuOScgHTL2PnlN2v1+WgoA93TDYkqhLdZyZ/UJqhbg2MrqTc0YzhTXkPxVI4gC4Nw852ItfemIJdBvYIFatGZqgxO5Z1gLQnLidFmTZ8w4gHAEKfGXX8UsBG5CiuztlkQSjRX/09d9W7naoYzmzUORoW9gVDJRScEZ3lCuh9Y4ChWiPIf7oOYh3Xdgqlkpala+EUOXMoNwc9d6z/untyWIuaCP2oHfy67GJNfvlgUGQ84x9Q0qHuaSoODkJhgqeDYbw+8CmTzpzziS9Z+a9hJHMeovDHsnEg9dAP67SROl15mLkjwbBqRP/nhE1m2enJwaqHJLsdx+lTdVnIJvppSdkt4BeFdGOHLbs553s3YtV9e1mbtroStyhP0b8W6Z0ISm1rd3iC7JJKRPuTvrCnMZVNae1Pyj5XxvxG+iaQ5gKRAOBgbwsGN3Gp2DZ367CpVdv2ZOfHTIc7LnUfggL0RZ3coDmZ2vT1TLJws2R9YNFdGkZ8mOEPdUSFsu9RRrps1DFQ6KjYRjJA9GPcMAo0PP1cgN7xRdpWVm6f/kXcq83cxRS4Q3pB4ZlAfrVmG7jQBdys0eEr6WUh3UCvRnbUxfe6tOmMRLCW7K2nh3tfjIHGO8evFbbrPvbuXnX1a9/F7ogDDgUng4p+G/9HUv2axEDLNN2sluhnBaD870TwmmwOV8iMJcwWW0Ru2Q3GbSeXLMgK7nOeeHpwPZf5KtdH2loXnX7DwLQnSDl0QDSvgO0vnUyMICsNIfXrvuk1OhkMTj/0zPgXeoPKvfXI/rrDtXXClj7kOiKW8x9u52kctfMGhcdqpXnSCJ9ZB2Wb+2VLOrUGywTHjXkC9AwHYjRMghIhIb0IUw8CFKl0GAwiJ/pDZc55MY5MHS8WmWogkbl34AF9Tg+IgEkt5tD/uqJIsmJaUSAWTfW28aa3HYuKdhyKwl9KHZHwC0APtVlGXaxa1UtdmtQSLcabex9jpKie2npCjEhVAOM97OJ7lEHtAAWxQxt4czsfaLwzEWLVr48eRepX5i9IYfWh+8JYAM4oWlwpR7D4sGYceABosRwR2eemjgglub/av/CG7JseSRmKvXDGa1E6D4QisUNEeZPxb8BxHN/o1j0a/oJSR4/j0CMJLVeCCgkdFu26228Vmq5D0AaN91hCB8I/TMwCkL99sZTwbNpIUXj9LT2/u4oh/ID9tHFxFRYS5LsE+IhVkqlZPTgpkatnqk/OWgZnxtlVkBc0uAWuBYzVU5gh/WOpi36h6rpQQuMo/PcPEsuKiXv1RUoROinXixipnbuA2EECH+QDHmRcefsz20unhRZYA+408mxy1bMbS9zVpF3wL6S61n0qDX64twp1uGoagfe+9MjaGCKad8hwv6a2bf4DNlr8AHhlO/z5+6XZ5hsqdo8mrSaXnhbj1GKv3v6XkTZaCGPLxvoWlq40n2V1GVOqofivHOl7Qxa5kWWomKEppsL7xWqBriocTwx5MOjTiX/kS2enYuWU1yfdwbrKHWdGRcgNUaPemmiJDhcvCWF0faj5vhpnJ0r91i67aGZT1xgpAt2itvbXkqZlSvK/G1hCHx9okp6D2OxMoJDLpk5BxKh2BSRj1hM+2SIIBgCvSmaCevNFGG5ooXO4OakPqrZkhlmXjQoGwwIi4T9l+w+jIJnMqUKkpUp1BMl7pqplkpE2fdD/Vg9pydJylBGtnH57fjAOHi851KiAv+ucjptxIPcfIT+l/5RckHA/p8hrf2+D8uTflgC1AIZiAnFhF4csJGMS2uj+EKn7pLMxNhXae3sBuAhTm/qtSdyZqylDdp/l6ek+CdpkT6XABgTDa0B/ArJjN+w+onItSGfvktTFYfUjGLnZ4CN7MHPFjiXd8wLdlgi+0ueyl7G4tJIY60m+36qLw8Mch5ATYDQ6Jxxx/ajYCTWAp8lxtfxn6u2b9fNOT8ycbHxtoJsnPdWGLK6uB+g6sMDZZBXpJcCh2b/W9MverZOFBujJqN0qLURwF0qtchTfNtazbftYVYEt1l4DJSXYWBr3zNJjzYyW9dQskH8ibO+uXWIxIF/UCjGZbLCJltMD+LGlylUazsQThQJz6UUugWzviTf6T93S86FeXx3/X583sZL8yoq4wguX5R1Qj/Ic9PhcAa4PfrW4RvWT8rvTmZ9xUQtvF7iLfQwg8ew1Vp6cvAS8UcnuEUjA3aMkz+SJDlA0iaXY4pNOBOHj3SJTS3IH8XjU/8icrm03Z54pyLD+x3bdbFbdXqOqS8YQx5ABPVA6GNX/NcIVlh/dgetKZZOcpmPSsx9qYOJa5fup/1revJYsmss0bepEJoHy0/YeeFSbWT+fUsqYaJMDpSGppaiJvxC0cEvnnrM3qwq1k1hNEn9urV5oBDmi8Nx8ew75bTQPtheqmXgThwRuSuzm+PRTkQAJyRb9kunieYMd/GtCvXaloeCR56+1HuFX5GavpcGHq3DiWXNhtWv8GzOLZ8mTaOzGArKXGOelG/i0Eb/i4HgmwqyoO/k3vskf9g7bzfXQz3bTzxEo31cV1RjwLrg6awvNf9uxT2x8moefSPmm+2r5jbMJttdVqFirbF5Hi7UK7vW//RAD5XsMjNwa4n0zXDkGexzHn/nNBhl7Sv/RBacZjQinhWe1uXQEQw6PZzcgYviFH6eq6SuinikNvWc04Aj2KgpY95BvOBbQ/V2wjQqABUvrVBKfLPNVr7pzACxEiF0hkfOJMJ5jpJKRVo33ZAKhi3KgNMfbMdXk4KKsPjGxkkP1ZgHLI4E7/V/65g0fifsxkNYKSlaykllsoh0xMGPV+x/wO6EvAdKreQ7ortxOyxAAFz7rLajxVnbdK5xLm4K2g6t5nnQRSC/ehYBHuXr8w05HyUSzkJHCETORupO6DdD/JmlainpBC2yhXXI6pOmHES0KqeQPg9WgZzOhXiKQIc6oXbp0zCrWuPYr2GBKVskNj1z+0kU9jbh5P681IvZNxZLHhNPO1RsZctDw6tM0+T5KZ+5iBdqpQ4tfAe1P40l1FHek0dLKtnPyI8ibjHw+B5D5r0TyP5wdQYFCbhK5vsqrISQrdj7mWSRePW5Wj0cpUWEKhpkcr9DNOM1zU37tFbx7f28W/hyOB+yMEhhKHH1h+Kd9Oj8RFECiFoPpat5jd6agYhnzcN1HVWy43wrLOyCfCoMR/pFmkrw1SWda4Mxh6Nwbm2gvhRgZNgEu5hAXVy9ghoXKx955i2tUZbLZzKaXdsIoS5/r3WdQTXHtQKH3k9rIiJUvPeJapPXGQZklK/xltnDCBIEy47WY0gkiW+waB5d2QKHZ/q9GUPtoN4fPYr9BhRZadPo63+VYJtdXDeXgku33fEwdm98gTf0AqBvETaFW9IED4+xg0sxrvjfnPxEClTvnUy6U0Z08WQpFaN+pJsXhO7rHioRELhoMpQxBxWimZpi08EjGw6OCnwInrXwmvFESh7o5g5lLh+eBqKw1AAMv2HpyaSXS4wMSSWAquOC+QhLwNX2FOwV8hpxy05MIwVMQoBFRdUqixTos9V1fUUEliHdJZNsnZXElhT7OGBxJqvqZewkRT6d2riKIsVAYX0xdcmP/kUEi0g1nuSuNBgqBQklXYHrYJZINROyFfM0SqFeFu7h96oeXwZVOyDdfs0OaSginIuTfPq49bMYGXd2F5g46VnK0294ZqgIwRK/BU9I0DDx3yt/B8gp0VITEbco1OpZlNmFfXjfpT8wvAAE03BbP6ix3pe/OctYfMD1aDe3NctzQKGeed2riOK75fB+sBIBjCk8skG8vgSDAR2bBH6wtoQnSVlvdiXXhRghoDkbkepnwcn8Y6IhhZ4IwF6UhA/QpEHiAyO7SyKkDWxp3WbIq93GX/9nI69Wkq/WdHGZqZSkN3J1aoWhf4nkWCGlNcD4fSLsXWyzV9ranCnf02kXuSkUdAM388ZYcKdrvJfqnlH7Fv4G/zi6J6n96xq4VHltk3D+u0c53gsQ0wOujH+RaASSIIymZ6trXyulSGM7gJFa9Az2DLrFuu2bnOwaaDXQPSFb8dqP+GesgW5DN63sjr1dyMW+OcpJrvNPCokfORcyvumUDuaLyYKc8FxG099AJ4hnXfYxQpiF9KKQ88sybemV17WBc86vYdNvqjnxPj3APbpQmY4fLMjvPoyb5241OtOCbXQ/2hcYPwdDyqGsASBnq5tU508YDqZy2l8TptnpWwLJU6Iq/XAGwjRnhgMa0aTQ3m7tjYeLiY1am5jyYBP5EeOiexJJP+W8uY248Ig0lFnk7hAG3wzxMvrqC0GvgIJzai3k6oCMImYsTcHFNf9rD4OeX4pwCXrOluaSgX0TZzYnRQ2Agw1nhAIdcexp/wHyTJ3Z6gmfk6Uv3nwjFqBCn3u6SeURTzVo1F2w4Ns4/0nq7h53WAsY7RzIB9AmbID0I/tm9BK7L1ZKGw3Dr3lZP1CmpugbDJ6sPiVY7jRXFD9VJIBbXAC5g4pRpcjXFAA4ZXILy1kZajonhUqANiPxdbKTbfWXoZSiq8THz822qf4iNa4+2GKyXNwUTQHHYgKkGowGUvXh+gjim9Y34bn9F9hE7jJUSAO7GYstW0n1lP2xS9dIDNi4hWrkj3N71Hu4CEkyZTN70aWzA8QQnRos/ex/E3FkhfPYzP0dD6ZiqiIVw7Gn41DNIcyDDzaM58hyI1gnOZOwmF4V2+GeHQteaQAzExFOymnYdOs6M+CB5PrWpddsPg5g6lblitZxMipzNGSO/zO0rl/Vko7ohQNZlQ52q+Z8MPHUlOUEqW5hkUAXPX1abvmOk41QCc1E2hO0l9WOCul2VFIb0wbku4FkOJFxkBDl/wh3ckjBkBD5VequHohRZKBtXFb8ZT3V43BhWBFMIPynDRjYSvz55NYozk6McTFeVatWhAm50MzlrYO6WCOhLAbdcw+GtQiQc2wsK7IUKb6pYBjQIIcfeqpAgMoE5Db3JgKzCZk+dEs6Yh8BluFBURgPRkTQOd8mNDxusTR9mszebw4RPDbxTXvqlqAJcd1iNbG/HePb9OuubhepSgcx72MdHh9UcfNSmi/3C8ImSsio2fmelSOaIuJKsk0oseKxOjT75K9Bwvh+qPcNw5cK5+clC5KSO0Vhqt2ajwFbxSocJDDPySeznjHR5kdBuWMUzmFKh/Xqt19W2YTdSxJ3xatD960L6eeJvMU+W2NoPNhWxpV/QM1NAysKmjyK/ZLMikhMu2wztiqJ+QsNMzR38nqIW78fBJ+B2FwOAYwIhVpQNq4pu8EEiblh4phRjkWOXa5v4otDBmaACtG4TJBDns2KlzXTNx7o2VRLMwNNo4HA5hrk+3oM1ATunhxHPLn/LjFmRtjYzDCZwG2V4OUUvszGJx6FcwigOGHlKZGH0jdEZt8KAtZImQt+kCuODuTVu4GQW3SyXbzU7UtqB9mPRvz4cgf+SR1lL87WgoBRWDXPppAjBcMsWteVohB0xP1JT592NKS0kbEtSWrNIuX76cnIk2X5325tzF6Cw71wQOhFuvrIcHJkEABx9vEsXRefDcJS52ISVF1swvKntwdfrOyyHlUWkIaO/zSt2TV5Jaef9eHJ0C5OljUxCrObYRMpK5gL+7GVTiM6hMhHQXyj2I656F2Gix6iUiFanmfZKM97nT/DjyF5iUO27JcW+THyLR5MP5iXBBdEMWrmnUO0WGU6Q2R81P1RdYpq9i/F4S8xcqYuux1EO8Zs3f/ciDH6RP7Vf90BaPmGLaLIi2J2v69OWMFVoXbyFoTR4klGquWFH8lzWATIqmDBrMEvjAjjqxe4TfSlEO7lx6++tWLgc5k3tjunyUrJ98QYywnSi0mVidzPk+05/9R8H7NnX3+3Jzy3+Du0JCaDBoKzOQVxCmJnl1hUpClUdtKCzlvr8SjEFfwSnot1FxrKzEwBt61gJoC62xSs82tgojfPDNDx6CMVpuRLiGIwRZ8K6VSPnRK7raakhVLBOX/Unp0fmNcZJ55VW2InJ8WPH8aO4wkZ2QiL+1D0kb0hLCxrQqjCZmK68VcVty0j1yvPnROkLkveT1+jgsu7JwXoHDOw57+T6Nyq6ksJBsAQnvlN03uxpE6v2Fd8paYJU737WCN6Z87zu+CAmLrgnThomZBNNakoiaih0l4R2kGQ47XfOQjE4LbDah0CPf02GqP/qQEbk2+p4hApGb+LIi/L6fYVan+CsQwBZB7ZMKNUc4OaEHYAq13KPIpkz/qgorWg37gHZZt9kPFBtGQeur+CZR2eJbH2dlyFzJ1LAW8+JpLE4UU44v1nrSfae6+MFD2rCHRjqouSUu7SL23/xBjcIYzkjLf8SJVrVA3iHF11qHJnJrf7n7ffCIOXdTTDfWo35IDUGPwKTCh5gzsmN9N8wSIL1LV2eAZSdy0axUj5HniQfNZRW7kWjJj+3Bx7zSbyoNpcZi2uUBJTmpA3cF5Gy0uTsOp0cMLXihV2bLgzF14DAU6qtk2mp6qF0zxseALvfgSBsEjBewdgnAiPlgLT7eQ7mm34jwx3NN/YMyZZCe2riZconDX7CJmG+M0o0qvD1VDidrcEEgAjtkd0NgpYZah60tfTahtlMz58nf9acjFg5BgFjAy4T6CwO1S0WDsn+4snGtgyqHE8Tzc+2aXcssyphURyY+HXxobtnb83irGOOl1Fl3pX6IzNeIMiM71zTRQfpStFcW1McbbfBQjILk21h0jL1qvMUUrE/Y70x6Qwhj+0qX77Gksm27ZPK1/FaGRWa6EPm9tNyg2FCLjXABokoWej7u9Lc05yqIZVXlqyxdu3y66LGIqB34sRX9G49muUC2UrCVoPjiAVeeYifcq24qRLWWS24XcrnPm5ahGCojTvFNYj+xT1H2YtmO/xapf4JuDhagZ8mY9DpbiGbqWFh7t8Z6mDXb6Kp40zu4WqC6wFeRwwF3uNjqY2fX60A/lCGkE7yrHJt42veyzDYql6K18sEIRnDUpBC1i5DFivir0z/rMC1ayUeMIHYdnzGGHV3PbTBLVYUDNdw6m30LwskxkswB5fI7bcvndoNLAmJrBMw4w3mnmwpnPrSiYo5CcV80adYj6GtcAwEn83lMeHm6AcGpWAqtpdTrAt0gs5Q+SehuCt44TCZpIIiFjOMX/+BdPJBJWUzb1C6gnjD7pmQ+DgSJZjIHR7VY0JuvQsba6Z/mO+KMDElud01cyzHUvH8Pc7Hyo9uprFCW7dbcR5I5OhuoG8xmpl+lWcqzST2MnwMEO2+6P9gXsow4k3T8S8fQUM9bD7hX+oJsoG1bzXWLQVs5jYZ5TLRDZl9AUb8hSKvNqhClpbusCILn2GmKJqJiFygGfYFmeuFJgADAOFADSp60QrjxbR+lbr8bwp1xQqpzJVkFIjGeOr2oKKNynrDwFZHUV13kKDg84dMQesPbJ41YVrKKLvYinR/CMpmClFM04cHGxCuXV91uCXCRnS+oigi3WYEPtIluUs84JkM/qHOJp11Xg/pkZi1BtqTCi90FhY6RJweY2XhpUUPWD+6dYgaOUn2Qm8LYVwKftE5j3g/IHUz4+scLqwvnIwpb7QRKCa1KENRkPB0XtSgS1Yg6P0EdgKWI9Oy/kzP0fsEb9stklVZ+KvlgdpB1SmlxbQdW3rwn/e+Bh/fwmhsFd4A5nscDgdaIxKwn5AC93cioUvH5EZGVXeXHoNKp+E1TQt3eBOq1Ofbx6J/+fB+3xTD7jaw9V8pDFhvov42EP38bUFvOB5uavq0vDvtSeY/urgcXx56MfuzMRNGos1u4QnbpgjsA2FojA7/oU592CXhXkX1gxmponVgRRCC6xUYzqS6mgBXrxYXUX4w8UYmiCY2w8kpH22kLDwQB5QPF8AXw657supz8MU3E454WohVgJ8G9q92YnofwUBSQlKG7RsQq6uV8+6crFxaVtQGIkzHfscqSOgXBtLYaNTjWJx6Ifem0pnuebUHyWJ8JQ/Pfuqde1d837Gph9NZeKk6pNVD4ovhPa3gtPnQyWVI0RzLYsAfvcWMv3ryj+kXVRaDZafxJ0acq9Q98Jey7R3WyrUZDm/OBh3yesjSi1FmO/Ud7jjmvAgLxf+ka6VZMJ8twRirHoOJIBeLkXNV7ZvKyVso29kURi9WMtIeUS68aoXeFDklZ8q8XXcKcHRpmVFCg+gZLi4Zvir968eqBKAaxdztSDGjXSYblIQAm1GFu1jFd0BlwkNJDFWFokO4U2C7g5Am2KALWdJ6HWYN64v268DoeEsJldHaQZBa6KUId/R3owprKVQNuL9IC6Mp1CDNyvLedVyF91TtBUEFIYWyf9ZTxq06dlVvOIQcRvQNHu6GeCHc5S3TwpWklsuDSDzwDFMVdMCoufFY6kJWFbwbdq4bc1yNZSrQyB5+T1BTbCmhuCpvA5v+JwU5+o/UhAw9TgGZ7fbt1wqHer1YSd2uY4jcPWC3NhM0dZISZT6AUXSmJv/yBh5VPeAY2nQ4wuPboqRatFdk9ywNJBW68mle0+WnmHPgIlT3vknNHzxJgmuVlxrYak7U9BtekKF82Gh8ZMCk/fM9F1bh2t7dznsmOb3rh8wiUtm8iKNKGCz5d1xVuhEMFDA7SWvMBQ3cqwMfuGjeExrp1sxXv5aQqClS/CSYPmzsHrhrAhyl1j6koQJBU17df3dqydPOLmliEjCALgz8o8uRw9A0XutbFTNe3SLwib+wHvGKVXX6wEOWh0rpmLyXDt+67bA9/ag8lOV4Hj1WBEsh8+LF0gANSj0ODfqNoGs0NbKzr+ohPybUWw1TT5OtBLK3FKY9PTW84DsNO1PoKIw7wubYbUYwzOmXgYQ7+HLnVa3hGrNhk7bi8nGumUKV5HkaK6mLB+VN8odBtQRiwdQgE1pWYyL9RNcl7bswvE/qSTF2ZuuGJYdUsysJHolp/65quHTbP1bzfvx2Wl/V8pC7BI8ORvCEkacEMbEtVOzJj03MrbxlrCB5MWorAzzsCfgkR+y2LHb+bpvVJyQSjuqQ2JUe0g4AUrYZFJgPiR1vxseJDLN/yBvbzNEpjjQRspaqKCQzR8p2G5uMicIoJNdPXOvdOKlGMmZ31f+mGd01i//2nTpo40dMPyFtr7YxGttvcfkoFywJKpII4yNf58UBCkLpONUy1rLoZO6YoCk3ZBfeMLz6SE8NMetUl4JFzC8u92kaohYsRqcnOsTaqmuoWo0EcSXUhWFrEXmty9OLAftpzW66h5+b4ZK30WioGRP9vMsHlFT2IbLGB4lE90qUJIpZ9010F/duA1KkpQcpiayPLYqfaRH6bL8BaU1dAXeXpAfeFweWOSjxIltNvIwsq+3CvC/mqu48nvfRIm+fryj6tGY8s86ukjhD3ygrWq/ZysmBb8CxxjF/okMC6hdVvUD3+G4gQ5yVc/hVaRDRER3xEMk8PgeAbz+MK49vV4jB39BMXI83awdKFDusym/DOYnJqDEDNlyHh7V9Q6Qs++5DckZ9/DK/CFBiNtYzQ9G6CA+hyhnqqMya/AD2srbz7O3v347AmmkxriEKWzeLMk9fYudNCsdKdCHyD+6n1zq3bzw5i5ZDP51aQR6FtLpvuylqSV4ZHyHxod7QCobaXH+4i7x7L1EH2By2TXpWnzIokCFVS934m0EKnbmrtVC28t2+pLQl5PgHEnPRKg2ZgtVxuPu7y9TE+P94Sqy5yt7s+mrFIMEovndWHYF8G7Td9ARSeVzWK4+FFDSrcUq/VNkTe8ZStN6amWTLU77rjUqDzVuMquVeTkgMLCJLXZFPgF0Y8mnzaiztSjxJOvYnDYLoBGSEcFZZivqEDv9BW8VMdO56C8vP5XrU0T09hnh6HlJfmbpFyWykt8z7X17g/UA0WkchdijLmUigFNwXJUPzbN/s9udIGCEtlEJ3ETeS1mJAvK2p0Ce2CLmjU0RHh5k8yt1udVqLFe2/U8pNR/ETLIRr/ACARhs3MZy1SwVOVcelAfsBWBoGi1AYF+WX7bt64wdUVrWJ4yxmoVjPR/XAoDSKwt1cRIfk8/TthgSja+9nU0Hu8CbbWyy0vZIm8bWTsCSlbjWEn0yH4mzVhiEKil18NDuG0IioHAO+N9sphVvlr5OrMNFOUo0w1+HrGiG6KOl+nuvVwI6IMG3docf4VJU2y7y2Njsw5SBPtdWR9Lwigubqz+CPNUo3VkaGEqLKAdchkItrbWU7a1PY9FcvWS6BVXBcg8UiAqMF3ORse24jg3ahyD9H/QjEXTznGfyZ22HI+ueZnOAITe4cWLLWLszdWDJyiqZZehd76NoTLpLJMIFA1hhnDSKh5e0mC+GELL7uIrvwoPtgzt+RtTpf3V5keIGvvBa37VvdxKBkA3bopwrECfEIvlo27x+9UrFOprQScUtFCFlgiAH5ixQ1SiBVhhgkGWgui0ZPG8VW/IKIIH6qzT3hOz506sOa9lWVVGMVOeADk3lhI1oqkkPXhstf0ktixJ/7/Nywk9I3ayHFiwQtzYfeblwzmUMgCc2AsXlvdyb+YudfISV0SkgAibSeQE3X9dmjeHuriqIAfyG8raM5c7Lb7EXUN57kouxUlsyYW2M2l20msHG5MLxBqQ55WytQuzqGHbIpEI8te/uK5q9zd0rZ8Nf7Kkx8dpcSgBTaC7hnZONDqFMcJFsMWZAgKPo7MTckwTYRgkkFxDjHeNS5mz2256nzBI/lMAa2IAwGm4oj2SZZ1/UwZKRa17Nl9IsLLGeEjGGp+sosxChwoAtiW5o4+k6od71RimnELX2gAHBJFyVJEwOSM5pNPqaTVju2HbdCHBxnlYlWb2xh1HCOY+PGfMY3nEb9yHWTjlJxm1yc8DpIo1AsU325M+VqRdb0B6I/yVuLUyGyTeXjYA+DdSDLCss9jZpD4gnupteMTmnVSyFxP6/33vmiALbnUYz+NUfqgNhPX1PI2gw92vTSjQFrjl+6b4zPIxUoHxZP3RANFtkeHK6cyQm6AkqVJfiIjPDgOu5FK4ru9/RuS+o3Bvj0RcGzlj8kwESBhpQVQoYLvoOQZ9wFmxjKgOAfylLKCOCWntXPJZm9bpUSj6mLVBVtUSXn5xACJKMV6om1g4vH7JcidGn4kn9r21w+0MB1GgdoyiM/by5SNEZOZjMTv1xu/2G7OhdOpIzADE+tnboxHDpRqkT7oAMzJVPjCA1TihC1u/VRDgdfm/+02VlsQ2MTyu51aA7uXK9uSzpjtrNHXz1OAi8Mf8wYpZ+8RCVIEwYoaevlLJq9a2LiuHHpNxo1k37DYPUGgx+CR3CdI9cPabs7m6bmEQJD7U+zDsGdjIwv2TifOauFk80A00AZjyNFS/GVvzc7VLgwP0tV58PJaS1P4CoCc6UfLIMvlruRUa7kycr0D8Y70siuteQd+M4sscnuVzokgZkxNbL8X6tIHndK5TEnDo2EqUXwwixNzOTkwlzhIel+CCe6brtvfU3hLUtKPB/a6A0rKMPnq8mLkglyUgqpT2glO0NWLfe8/QmW6W1lRC7BT067nuEcwqpmU33GkFITC7KpidzfZP9aZTzaL5gc28jBubKvnNtagayUceA0eNv0Am1PQ01CbrePITAUVB0iFmzcpOQjP2OeKZQ+1o/LBE7gS1Nfuev3eGNVXr35Qs6PSOhgOmNyltZbW5Zy18e2Gk3qW5hIj4CC4EoFPKl7IZwnHsmpwbboQHdjOrpwIkMmdgN1gk8w5mhmQ/sfUYYN0SZH6F7hgGK6ViaITyCkxK9K7QQdGGl5/WJt7VbqOgG1Uui1Awp/Ay6p56A6g495YJNf/ZjKUBSrnDNQZL1d7DowSPHWPGZAUTEAuPHJw1Z0kigkOZM+Mu7MfbAjRCD6C85xBcrkrIkteNqoAGqFnx5N5ERrbzz+w/wmtc86FsFvENw3/wEe6Icl+3ea+WkSbxH63WytmCrGsZdygjNd6oRMg3JZux9kjHcqcB16lmk+zsh4dh9BYDPMrUWcTC4i3uM/p6rqj9St89hvqoqh44+AeZHVhw10n6LyBnjjLlsyTzzX6CYsu5fCc8VMddB416XBTLhd7ZfZcBgkSQAGNoxIVSOGD4hwUDL4pkNyD56XV1B1S856mjD+DM9pQgOsJJJ6ju2egmmu4eyD9o11y170pdwSAe/ZEMHhR9cPBet/V2y0GX66Foe9alBNzOMmi8QfD6tL4eW58qyx9L7c8cO+wYLkZVQC2Q50JQMfbQYCBlWnb+kNMZOE/kskumBl9yJO23ukXaDd0cwWoOBSj/5d4SvaeJb/DIJsbomNcwsZiFPBQyQiBHp9E1X5kxIxbLUBMiGjf/c/A86rx3Qq6IDf0E+8FToKBMhKL23AaTRDYmsH4RCcSbz2LTUQKZU9JuBy1OS/mpZ8VTJWpQK0ScKhY1W0EJgITvoZM0WlgwmxtXkNzzwxmbkttvv6i1BJDS/fMsNitSDtEJCv2VdYkgJ6SslXRBY9fMJIe11gLutOcxXyycKN8FWXNB9jbXsfD8mEE+OwqEH7amO9m+a5cbZwVDQ5bkXg+lfKDjz/6zXN3pYW3bSLyIkb6iZAew06Kl9wjPEQleA1iSadACa8zBnKK9Rm9ikcLfInTA+kx53BJDDCGUYqMhtJSCCPFHOrcXix0t2GWaoftQy7hEYNT+S5zlsDOUNeIGaxEt7HHnV+X271hGkfg0DSVx9mKpZf3GXn190Psf/k4iov8l2lFhWunnbL0ytDEk7I25OG5xJi4FIQ9ita1UGKnB7pbkHIqoWxJlSe0PUW8btbGgQtdLkwba2cO4vlHX1FdHF1LOF3KM9Jhr7+qlT5dM99Z+tZ39ZfTWhAvdjQ3PLgIm/75P159egODJlxfoee+Zm00u11DaXfXYrVLNILv43p3SluPAyfaxRU57QEUOaSpePD+A/z+8yWxwVgzDDsw9ue2z4D5R83iGL0fDsIaygTOiWMVzLmWOOvoMYKP0K1HObrp+gP1ejs9sdIhOW7muX0CZfAYLWZpIGuGiNZC7nIKqKKyxy3UFBeu+8+LFisgY9MK2WRuUvvEnXiqCwaH7o1nVLEmRzq35rhGXmaXze3AjPb+tcd3Vw6PIDCX3/KgpWwMSHu1QJQ4ZsRQIwEJzFS0iuLFLOzMF5p06vssKehknEJ1qdptdsTJN5Z2FQYmH1O298TVWjvV8oFLY8GwT1WRt/5Oy5T7p34ndxRF8NdC4S8wC4SZMUo4frc3zBc66UJw50jhDtcDc7QA8qTPHCy0irulTyesEk574fDU6UbVF1dVrGNjA5T58fpP7YUgxlzHXtEwgkUbaPaZRor6dfplAGloOMuxuYyks7SVIdrY8x9bdmdlEVtldF0VJf53hewUrR8PM8OZzQ8YJgKqo47VboRCzXSslkXESugnD90IFZhvCNBfV4ICvzJgV44pE2aofJ8L+CRrGEKMQyzIKfFWFoLsxNF3G7MvVWkhwfyUMl5+T8CpO5TbzOpJmvdapRcsj9B/q1k040E7hGKEhsIigH6QyxAja6Ib5jGuHY6fATgBqKbzoLi7HGz8voUZAL3YyhXyuAQ/0/6mrIBeDE46WVIot3UuWclMZ6qIhJ4ewrwcxXHYmyRNnGMxBYZ9C6zfRPbdR5kAsPUHCAtzTCN0mYsNUgfmgpRHqhzDqWDgi9kpEqqyuSF41/Ck4C/L6tmzDVTAG18HfoVgsjPCaazqZN9yxBDcaNic5z3HKxENeExv/0pRxw3vmvIfXQh6kh+6/vSnV+gwApe6RGNKZyVWHKBO7to/XNI8KSdMOuyXB/J/Blj5snHeFJ5m6eT5yPEt8yPWg2y9wg+flZ7t0sZuvmVno+c0xOAAJPk7sk9gmx9T27xZsAEuS0uLtFqDfKJSDjba5fr+E7AOdSv7aGtYnpAhSNcaLfvExrD1/+3vW9OJD89u94vX+j1O1OvAchKQVp2warszQqh7FtnHLcS68RyQQOT+d7Z/wQQDtnrlWLrBCSFAyPzxO25O8t44jfJGerisQop9eXTb23AHLOybHYb6lEiQro9OE2ie73A13heV8p531PTagV0YejmNhRG+UF+4fiPNovlRr6K9gUye5fe8gkzeahDdmPaQyNgKWbBfWzC7tujH3WWNc73Ly4bjd23uMX+DvoSdoqPO3VvUeclkzQ5zD+HlXDRso9hdM1h9L+k89FPS0Pz55aWxE1MiWe+SXdcNrGiHCd/uFjcMekrKsaxivWLZhAlYoa4Xnn+kjXrLhDGhyBHM3EnfevRUAuNXAsYskhbVT2yQpZE7HRic/9cjbEGWnokT5ppnTXl1bC0QzwxgooSVsJxnyWlddUuyiEBTr3nni5Z10rnAC/LIpGjbxqt44pHev4l7I71wn1d8qIYhLvNasNfZJHYbtJfFq0b3CotFeDvpt3guivb75gIeVn6tikkCNSl9z08vgcvQJXl61Yj5yFhtbfWxVh0ESWCFIPAgfJYlozcxaX4U7JL1ewrihQeA5n8mi2cOOMCM2V5YW3ImQ2FMJNchig9p9fA0j/WFosjbkRM3j6Tayr00injn5yduMP404JJAAiMrDPpI0iNz2Tz2MrBKtQhHGEhVMO5Lf6HiNkiKkrYgcXiUxQNWpYg0Gm9IO0JWv3DRvrYtYoY1x/UwMnJ/8gBVQR3T6tMzQ1JiDeTndQMpp+G+URavUEXVvM6xh0RbVycyiBOJB6u+YoFVsJbG89Th8P/ouxd/Zp7AlvKG+rzFAIHjL/pN8Q8ZWo3o/QLnzuiwGdRLNueLm+d/8yrieq3rDYpQih+31kdyMQe0mYoi/0/aefsd+Wn2HuiliOX2v5A7efZ3u9qdYeQjNgEbxFWvj/+wOZgD/LcaFK7E8TwlK7gPi04vpXbVK3PdQJbiFFUy+gKqpGH+Q4RiJ0IS70rTmloIU4B2qUgjW2Ly1g5hCs7WTu8Q3ZMbr5cvgZhmfO2hXfKzFwlYyr78NjRPQtBs3tOd6Xs8OJcI8Kb6P7NJfxaKHX32Eql3XnBVzpncjyVmCrgiyMHt4FzwmwstNOqX4KaGH/eEhAO5L0UhFdZo9sc7UKXUCVWb46HzkTudMFIfkTtJLIEugsnngv4TdURfsS5C0WOx0uqaxgTk9FWIPuYiQU2Thib8KKM90+bOhKH0XTRuLePh1zrgznKvuvJ3bR5P7R6uIwP/Sd86vNUzVMDcRTcIO2fSzdZZq1ut9jpJR0GOA092YQh+LzjVYkntvy/VPg6X9rLBmvicbZlAfynmETcBDk6njtou0hF+0Jrbh/i/WpgcS3wCLkAoEvtTiR5kIYZSrGLTtw4xRr2bPmzJCoUwcY1KrOgRLaqoJYp2C8INUXOjLG7aAyR/BDjxgwdyIizGCx0bYCmGUoyF+Uw6/A8JkBRi3a3r6IVdhIELFcHQ9+qCAY7Pb+RFL8lwHy5J6TQDhVq7Ys7RjoD3WfmAJWuLL4o+qQUe9Xls2zJoDVdmqeKvKuhUpC0XnUE9SFDipCx7bIzRudPpd/PTuMnJpB0ZRuo5gKSpvMvNIGDG0ilgQN5tIm1j3P/OaHQtvgYHIJm6PziQap39nt9LSPi2ED7Ha6pZcv2nA2ajmgpsJMgiU98BpcGErW0c+Y+qug7MGwaftv3w05S0htt1hX0+mEPdXUhzYkp05LOiYXe7RFGzC3TMWMOF+BJwzCvIOwi9TYbkmXx9HcMHwYACNWXhKlV8Pl1YVsaZkFGymxxvZUU1fS+l1zNVQXQstRGv6rvo9lb/xxgz6jMpBTP+LSkkpIp4T/Z2gNhOvMkmE8n3h27M1XQksmwLQNBvIZnlUH1wnMK0YBiSI1IGji7oDDLt8r5duNH+7/YeyMqSIgtvc/dqZxjUH8LCuHZOG+pZhU+Il6/V6Cq1pIkfjHg328mTu8KmwgSbYCCSJ31NyCBQa7yoDpDJfOZjYB7LLDAMDVwof8YsBQgaiarGFqLXkdz7cdE3ZKu/F24XErwSCp27qHAG603YzNabq9o7oQT0hw+bShGej8RoFn5bOZxWKJ86kN0nNFEaYny3Mi0x6dXa1o2vhHUGnQ2bay5vZTO69FEM3ePc2d5sd7mvexQF0lWvhsWvD1Yvp253vn3Fs5erPE1Bqi9jt9Jioe2NFhyy6RmoxCJCWUrIE9CoGMXUgoDlChVxbJGNGOrRscyjXOoOPyBIVvfrEuqAUuuZJcSN6vCOev1dORjRVft2EAiTi81WCnpX94qSY8O+Tlsf8HRKObNWZDl3OP+5exs2kZkgsrmOYRCgKfmTrw/z9L80qPLUYn+Cy4tO4dzxrV7j6NfOOyMd7J2sbwgVcGtyS4pU7GPGMWMHdbLdSnAuuUpIT6bhOaQTdY/8h3Dr3a2I+KzqRZmJxo+LS3mLCD8h6lKz7xGKSodlAP8M58AbvteB5YB+uZjJfzKDS48pKZzxBkqcNx9aou4vXSG4M+hOvyHhGXbL5puHewDsEbXMCZHp1JqXYTc210gn3SYgJpCSsn17w+HkywuSjGqkhgyuvdXdusEo1ZLpn9PXlBKrnoVYvOciFyxeYQKEOom955Ojj5Cbt7og8Vq1YOVAeEHVoMq3b2zBmn0wjM14O9YXyXrJycvkamb9U3pg/eBRTct+yp8XWCbGwMSPGvcv++XjzVp9YTqIjStXG/xdO0vlWwle1cTWQM7f7BFs7xrwE+6DttsQ/Kiq/m6Z4zTnljxaogVhLZBpJJEoEc0D1iVNT5DUEPURgwkIK31XQjIZb41R+tMn2cPBcdeW/AQBSx/g4O+sWu+eZGane6vmhjjmPr71xZYHzB37IGRGzF726SS75vUhXdGDZJwDbBjgddiLhQx2rzLHn9zG3iiLySS3KCFRaccpJP9gZFoEDOIvi1+KgobAYrFCOEPYTK6FMc7oJFRpASgdzkuouZ32Tb990gP+PrHcNN37TjeUmbZ6qsgs9Wo5KE5zBE/fzVwkzbNA6RPTIMn1OJxw2G/BUg0Ius7sHYbKXoQrRaBRHGXGe+e8/QV++5t7R+r3y90BnF8NasdtBK+AqYf7B3rPyv8qA+TchE8V3j+G7SO5n/HxWImQYiRwMQbyW2SOhthuPiBMVap4sGuj00q/PDNVuzxLR2jzDx6ByYZAKEMTVv35L1YtxSlRro+w2vqZ6cPCFxaH3tR36kBEsLchzOZ5uqQgiSppMA3v08gIqU4EC04QUDOfpQARr0AvjSXXF6Xe4SRxLwta9JUHnM+BH6yrPro+YVBtr7LJXmoOyDOYHHBJsANtI+FQxSHCsHlg2x4HxfTA9qJJOJm4uZglgtFVCdQ4ixxwtTnyEJygX6P5YfZZA8kNDk8VzHJLdXnovlS7IwMyqC/6N7x8Rf6qBKhV6q9LQ0ZN/fZQl1AvOq0xphwYI5vb0E7YVNLMcw6hRfHbiISi86XBRaE9rfhgu6oqU+LNVnpwbgha6lFL9y+ahAXm9o5VTMPtO7/AteW+5/FolkDOjbjsXhvrChz1KNoxmiaFLDpGt/8HVe4qpoesJQQyVINmt/qqqK18lc0BcOMKI6dWV5cpIfBXuQYthFFyPkcBTWo7Wkm+KmFuGnCaGP3K3i5tZEQtn8DAtyNmXv3k6OzCrdk3cjZWaZBjywsk3SRHUaotRo6Wa7zZTq7yhD9bGa+xBqKuPlc5Ut2UPR0X4nVP4eQ57mFllZJUhf8VL6wEwHHqIf4ua2U8ENs99NBAMNEjAtbBCZufOc1opIMZ372v900gArGtSMIpYMu6JoSsmfdSqOmCwvLlP5SH5bHqnjDutzm5CFlCht8gDbcdj8ROX9G2WT/JvAWMg3YszlpaDcy46F1TpfGp5nzg273CfORx8tjJ4EtnqKOXnjOGqxt7NrsU8sEqvQIpgiXWXp7n2zFQJRVYZRQDUZO0GEKTasmtfPJA0gYLwuM7IcgE8Zlw7iDcuQAFO5uahHlpZUzCwOv/V4mP3ZURNIKAJ3wEUIfganUtgdP4sWts2yJVH6rwrGNI04FrwSQdr3bLIZv02W/ysnn1jabklK1cKuqjsHxKmNVE7ct29/K7HphXXDwQ0mqBYNT4hloGffk+k1V7VbZfwjKI/OiSfyWpUDaTxP/aMGBsd6WRhzdAxKKN2N93Y/CQuJ7nsbUsF6A4sY725dKYQxdTbe1J+6CkJhJhIDPGkWyqMnCKosk5pL+gwXnomzZsopnAZ6un5FZQecZEkNWvxvtFQRXOuVAOZg8aOKh0gxA208fqAQfXm3emLsnJ70RKs9pZ8XQPtnnT+YTZRCtE8k+iOzhcAQ5kkIYPrz9bkdGfzFkZYIWgvMa6i09v3+JdxnEizfX4yqYNNbfAfv0H4INDovrnTsAJIU4WxQlp6kKJUmrmdfRAaHsMGyMmNQOcs+VqT+ifouLHxKYKnBptup6L/WiM7T2DccNmJeEHPbeFhlhiD3vaHKvJpa5UJqqS0Tei7dbYOoWP7nBkPfJ/dopg4n/VbYRxK704hJlVxnAv9Ky7GbHTkB6TN0bzmd1U8ZYFp51/N59MukwEPmjT9/kT7wZ5Z+P5vUlkc5V/uNnCkaGUcLE9/9uSl+tU1Un1+4OwzpdSQghRwgv6ziPzbcn4ka+nEZAe/u+dUu+SJSlpvj7iKQnxkMO7/yrCLZIHj9yQJTOTBDPFCq8RJehgzpnWA3+NfW+UHAN4NAlahWX2e2VxnMf+L+2SXCKCTTnYculk8ZCbCh2PriFATOVgzs8hyl/cxcccXib7H+Wj3U8kpjz/VMN5NlNscB/ZHi4sfH9VT0ZIkdifG/B9DfUXnqFJg6j47B9nbc4QF49rsF87DWgi1QdNlU31I/N8QNXiA3dYh9bIVrOPs0DSqvjGFehzL7kK002hJcd8ZOR6Fs4rWNZXYelvN+WRApTDL4oc7mQGTk4Sfkj+K94DyZ0v8RWuDHpEgJuCDmPXima46H4aJQ2DMvUG+QBMdJItY6/jhjSHfjkjcVgTm11lq64KviUSW9mg+3Jg6xPwSprKHWYSf3Tj7bcy26KBzaH4CwVW/Ab4bG4U3Jk/8eVHV8jel1LyBE6M+DhRC3iemtPLaCXixNsdZb7WdsMLQzN1QyEesFBsMQQh2ffD/zhEd+ySWluqhywXC7TglJWoijKEv5yGaMuEXKPefW/zfBqoh4yMj8xSLHz7pLQ+CGcMab268dCgMATTSR06fh+jRmITHd3AZJKTTxvjjtc5fXueuwZp4tYNdbF+OK5E1AA/lqQFOkA4zsudKbi1g5WOTJs/ZBrFo05ZL0UqkD8W+dqbA54W+wUquu0mZJ5w9SMaoWVOTUgTOg16thta5Kr8oyjNimf+Jrn5KKHpPzCAuOXBmo+6WG8G7B8+S3qMlRCfgWNEQgy/shN3FaaU1/iFRiWBetUbmWSV9rDB0BF1nIxvPbH7zKiKGoH9Gw/HE2Z7mXcIn05u0kwOIg6BTEOb6Kdm7F7dBwHx9BZwea46+usnlDxqOsEBU4RWj4ksMXEEtoozylKpoBdfdLuhYeXEW7/f82ZMn5/kW2xqpdXPmwseQQB3D2/mlxdfKhU82Ahgk3W6YbM2ppbAmLOEtEjIANgMHZ5UUqWJaE2rCuga1Fqz/UZCnLlNm11RPqkxVWhA8GtXCkPbCv/JSynAkeIYxzA385w20lRlOYQI4qyBrmYT3cNzNdXAo0e1t4hskmLvpB1PGE2FriHZE57P6VbD5Bt/A0Z9OMm4tgr9gOjq/LT1iXLPXQP+cPBbarD5BuW8rxqGH848xSy/AnDeEH/DOZ4QWeP6YPEG1zGBFyxR5Nv6NK3gUxypl7gJpRIGA133bd4SLlk/vkCmfYLZF1gv3o7InIr24cvwQp0c+AYoAl3ChlQ4x+D6MxW0cDUjBAu3EfZzdHrU9MR+tw7oeOZE5MEvmQ3y9pwzHdoo4lfin/dH1Wx96sTINs7ApODAifD+DmEVgrzLhEV04gAMobOMejiGUGC4sEf3g+Awws21Bt7Dr7O5U072bONUO1uHicSCilPdzgkTuhei4BdPY25Xm/CvbA/FcaTu8H73Jq8Dd6bBuLwmo2DeyFUGkwGX9FUZ+2DKn0d4bL3/tv6I7qm7+390TqYyUh6Xef1ydfLPv19yDPnAYIQ30t4kWYm7tB/CHVX2LSOUN6EDT+u1tPPom9yG2sfK4TMtVSY7z5RVz4fkQhX1h/QMc0gS9OtLz3zEQOUWM3VdOV+3lHIkwkjAljbksX7dDqpJz24KzdtA8jdI9Wq11OlfempzCqyeBVYn14PX4QWukOtzV75x6fX9N39JnF0MWQ1Twbt8F8Dvze3zosijGbznbLf3DPneq1Py+3ZR6DTUee0BeKhrQIp093EWEsGtKm60VN0HpVOZwkDAn70MPcmfFOy4oTuoNBzevFEKaSso6+DJMW52fRCjRMGPcKTLrZZP8jekpLtN9m5qZGHAQiiVl8/FTqX9MUsSMbuWWJDWGALTYXRvmqbNWQHNC3M4i1uqkfbPRHxIKZAsWtKdeZ8LXvEHbUfn+Obd4t75sgFmbtw+ioCY20KyEJ65xsPyxTmJZFayMqn9zqxijg3m3tJMHC4vLIuP1tQSAtmb6FTMgqfmQi1zcYzcrN+MkAcFQcpNDWtVgas+exJVxR25d1sWT9EzNIrts9xi7zwnQmCu++9RBnEGWSluVv/69YnXKw4osQ0JYlrs2fdhYSGLVjxG4sVqHkYnzmGoxusbniaJQEMniVEVO6nQBjZOVKJPfBMOVdkeNDK8qevRiLuctiirKVJ12qrobJd53dMIWMsuCfYAbsiKTFrrp3Qg+yGP+bv6Rhkw0V9WsYK5j62+fHtoKq4JGEuRrqzC87GA7w7tKsFv2PEv44kUe8QTKNEh+C1nqcjb1S01x71/VByugxrrjrJCtiig53LXrm0tZP7Jjej6nC9zruvO50eoFMPsx8dH72oDE0IjLXWjX5seUH3lYldYJql2PPLrbk/arXh2Re1afs0vISwBeU9XpVC5N5Cv54NBMwumg+o31KoInoFrkddM2BBezTdx0sqn4JjBFKlvlFJDuzG3v9xuB7X1e9EtsplqYQ+jfE5avfkmoyr1A5aextou5OKeUGnjxVtzEs8DTaSpaYUwwu9b5lRzPNcsHb0RTcj5IKCY6/M00xgzI3za9VOtudPaw+0HBcyXz/g8Y+0vx4R+h9Le81ammgLk6eqRyLMfr2HIbB8pr2ZIPNEPkvyZoEsjCULTQmIvp+ya5uLWIEzfeLiOllpll9F5QtICmBfIxG3sYzlu3/ZE6tCIHA9//Xv0iS/7SwxOlLsMdu3gR/A67T+4aow2pZqgRt3Y1vTc8KkbwvBudX5BdYbgU9UsljySAf6I4WWX9W2sP/Gne9ThDyYss3mkXgMyQQkzTT+G+EZSl0v+2ccOr3GlTy3EDvttLPAkyGJc1+LhA5//niS5ol9Iom9p/PSBSTTYUedrTcbSHhdN26WA6KfVQJdXPwWrVvCPlm1rcY1padwlCPfFHf1+sSHIi0eqhxbQNfETeGHDIi2C0vLMDlQOTHPl+rDeq54T6i7QLO0mDpQPwa/waRGF9PaOJDqcFFeAOerkC2lEhEeFFtv3GLao501UGas/xStxERCoZGjO98FNbVYELGa7yzCaelNUGSLZxXbST7SF+7aZhoo39twtOViHt4vdrZYysYLW6thzVXpJlcjSKy9xavcrosM0nflsGEiiJ4VVoAzHhz3bZnGtMlCKvNB4Yd//Qd6mN5d7tX9WNLObcnzYhBgYvAV8naYbcok4i98+17up08NiEy7fdQN3ITRTSxT/t4y5XX9NN3eWD3sDICGT0ZjcJs4QIOhw0Sz6Gy4yw78baY816DNx1A7QEf3dPTG/qziManvnzoFoPtKG7Wgg1xAnc3ZK6enXF9o2562tzBuD2C9oineSU7TsnWVHNnKl6BX49jY76jNIi/uxwzrbzAJtLqD/s+uHjyho2mQeGBJE1ppeWRz3I6X3NgL8rpqlpIHh4on2b7w0OQ+NFjYgeMI4a1LSdT4z7gzHmLcw3Xu6QyQNbKuBUJKSCUWPWpzsYkxV4vZ2c5jH1kvtMFycHZq7SNbDF5EwRqntnZRdpwp58xfwqQsIph7vRfNNVOuiVwoMMWfCQSb+FNFZ/0aXtlrKLt1U6yyB91i2Dsg+/8Gy98yDkn2hh7WDICeiWk0Ej827uvpRFqxvAA7rZe+6PgsX4wGSkbVhSM3CXSR6WW/LfPTP4vaZ1FhRtXm91t37mY028lrPbNpbB5r3KjH0Z+vScerIn09bOA1PXUKlErulbjgzYO5H8YDqAX24oD2S6QNuptxckHGGzM8oEWRs27Ap4l6W/KIEPvnxkShpiCyG3XlIQAa54HLkhieH/99fydOtGnfTtGn5nFyjcs7Yf9JHW21ICoXUDgcMM/KK6C1Pcc6GX2jSKm9duUDT6rH5AiQQCP7ho1bpt5QWB9qp1MlLVAMzTD1ev+68oKBF520iYD44R/xtQl9+2c/tC9WJM7Ry4pjWz+Ru6jtTL8bZqn5GX8c34IdNKlcoSu9esalvV1wNRuVy1LSGLApgohpFpwSnvU5Ck6QaCuclVwmI70/bqYXFf7uYFU77HKhEm5TMfVplmXxYqjaebZoZAF9yUeD2XFdPvMqE0q7hWTSH7HFP1/V2pnPPPh63R9iPeffj7/vTDPq7X5KMFMTxh1a2yR3Ginhqy/o4Bi3YpNQYO+STK9q7/kBfrEuHSSxouqh3s188C8qTI96Nbx++Ex4SDsiY74gfjl6wWTMrdUQUsuhwFA27rOXt8ACyzAzzxfIUU3FBbRR+jrWBZ+htKa3xTESHE97D7NhUz1OVLX9C9uN8EvnIV04jVuqllc57Wh7cJk3EV+D8MSYtrvCjrl6pAdf2ODa6r0CQmgQRtE+qrjtHMhS03II7CyrvIkrYXOJ4RxLJE87hSYoAsnlBwFsI7MX4DO3Y2Jfm2Bani+UWaYMCyI5A2J8TzzzJIvhKRoYl7Ox55zGhcMT+n+n0+zSs1yMnCQ+7bPP2XcRdzABLsp1kyXDqbweKsoy1GEREv7xzTt6RL13TfQiAQwj1yyF9siJeB/c9fQ3ltQwv3YHngl81WBKYeEnMZRjC04TxhWpBjsId0jRhFygD/aC4B+KQKxUqgXc+ExkX2jXut9wDwTwe1AsR/KLPRbevZINzs5b6V0+qJGMMNEbiOhF3I/t33X8jPAMOKtRaVOf8TUAn5fMex8ILM56A04xNQ0LXiKqa70pV1qAe7nm0E5XbwixX4cIs9Xrnya6SixjYM0VLiq5FC5v8nyzLbbSwQW/eWlAU2LYxeMcyoRYZoqx/CC4RSptub0D9ky5asjNRLysu1vt1nGVhjgylSidEgbTZ8dsvl0xT9/vCHqa2CVXrgEJmh0erUBRa4p7Lc5pbkLB7HEUA/KA0+8gJPgO0kvbMpA4XiwBClsM7s420x5h6F6QEphhEyMGrplNLntL+WhYZrblr7JgLnwxDc5auiH6g77arHaB779DwwayLyjJwg77kEZcKL/G32FTMxeSMU01EWPovl64iq09uwYibxxopGM2E+pmv6kqRQsC4I9mLub2y6d7tsXCWYNwTqiOvlWQ8LuVHLFDmKH01W9PMAipBltJMi4614Nu55nJMpNkdzkNoTXmg5sgNlttW++7F2TI1NaFLobmHZpuKL07CFZcTp1wNQOv2Mv18EK2r3/GzTnQ6MDFWo+PRscP799A5XmeqKQs/qtGtsM2QrR9QVay1nlY+PPKiUduQRQTu0qJfnxOzt4/wstAwZqCZigLNUFS8iKSit5v63rWic2WKPVqnDqdoS/76UI5x3XZYHiJ6eJoyDA4+LtoiXHhwp3W4ziZVbx32xSLgzS5IdhxDfsjDIG40rAKhch4DLmeIHYdl1iRfeIsl/pfUqvhqYpL1Pz3wSMAhC7iiNwDe4yWeCrag97phh6kZb9lHeOt2XfOWCdVvlR7dO2/aY5IQJ19K5PWB9/QMjqcvaWk7Zvs1qetcL+QovTEb5QbU+m42W1qzKK/pqWsditRx+V7J2Asme7eFDTZrO7v78CM1056pWsLYPvEW3x2qeki68a825LZIxosRWZHP3A+ClsrD28UncWplcBIvnhORHhvCi1pAMfyTu7XIJbGioHrLbKZQENo9h73oeUWUahnOYAhYyuMfWKLqRmt6Nkpt+zrxygH5H/Nt8poVVwVPXxMEnu+KpAahAmBGS4M7HbTiupIHkjEbeLCmp0KtERaSyTnuM7V+RJ00KLuNAo5NCyhaMzjGTs+1r48+DKUQCSpOtJI5E9AmIl2csR2U1wUUXDGhmCLo/P6DsaVm0FP6tfF1MFmxbe8kNR4J2PIkTrmPSarl/kufHaQQRRCv9SeTDtCtaYo6T3NbbUQr1XrIpE93zeKFZJXf1mirw091z4afRzQVW6BQ+FLMsGsiKoW/hvRaLfKpAY5pJ1men4janva6EBevNYaPVRSBtShaavFnGg7dr8EQwGMn3UNmG8dVdWSJwOJ+9KSA7EwFyukgh+qmlt7tKOBdywSIGjyx4UcYWs8t6Tb3PfKTPp+csqhF0p8aoToLDDOgqADgWwNceUj+E8fbTCCLkPPTb46YJrcj0bk2DFaCsk3kRRIp5Rfh4xj3REfE/Z0YYMTvx67hnRhpIY8azS5j3X0OGz14KfBLE2yKcaFYxiABPYHJbPps/lFQ7BNHzqnJO+5kC0qWf3Vzs40P6wje/pXs7FDj4TIvAyhvpXVidJW0Ga3s8ByWbtxdEz7tNUEhBYbGbiE4pDEWF1Jv80m19PGpAmTJpzYRQuPvQNpKXvwzMR635C6e552MI6F2k3V3EbDCaiYhpL8zuDnftIgM8vn9XjmzR+dzV99P7t9zxi5hNuBw+QGXTpyWbQzOcmNKTrhSlDTvKVRYvIueTcu+BtkM6259CdNNsWYVubrvcP2lCav201TQq2pkV+Q9KW40Ef+9tMgWw8dO+2NCZ6pTiExRdhDcMhO9CpZsCxiWnDLCYu531nl8hLZBx47tQjtBP9+kCjB/lR9mp58FGkyA4rLe+Qjd9mYQQg+0lMgPJK+bvQsZjMe6+b9aUGwYyMCxzr8tsfIAjvNc6rxPisWhhHaFhpIETTfyDx6iFFjTIhbF8HrPeqC9WkX4XxAbmYu+x7LFiuek0rnyerVrFmpATpgbVMekxs+9XTY+uyimeHqPzlBh5qCc0eRYxorsI+lhRjauebGFTVLsDyEmhYkXfVEklGuKhGEiqYDdtj3d+0vIhd/vLTY+GjcJ7Ae0GgydqzWrG4lesGm7bgmBIkIOBvyK/jz55VyA9O4Rf+s6ufZMxJrvaq1ihKcwsMp56s2yU1+85hfD4cORvCOo/rWR1Mh/WJgq6HQgVMd2l+b6DCaXfdBfCb4+rG/ukYVku+nHNadlSZ3OZRgvuRQ7NmirH38NbuuScI9Gth7p2otue/aWXKNZTLeDyrmkrWKyxBp1T6j2X0qbX+rzkC8mGtLXE9Z4HyMvVvt0D4gG07kqjCR3oLtSFDRFEdNmRSWponvP4nvIPJbtLtVpBNkV5RHrpTDS2AGH2k1MHQ+q/9xj1Wz5MlZs+Kcp/4crdtCSfcmpWvF5tWkUmVg4IB92novJgYT/oGLgPOU4X9OELL8Z++yzSZ7kXThOXwpWlIWj5tITtpahmP+Bik5+0e2exfwbz/UWsk1TXWLu57gSxsVpGi9OojaHXwHBWes/B61rtNz08PEqT3fHEnwzibD0Sjd++TqBGTzMFU6mJB+llgCeuI7K3rn+NOpwjChv+N/wVzZJncy68XbaHz9pdVJaonPXCv//xXbLf53LCDjlyUWqNxRQGw1f2/xM4ap7XmISBkZxuOujT0wg3jUQo4RM3amC5DnrJU5QMn7Rho08jAYTuNVGure61o3TwgQUaSvltqRTtFh/OS+6ZQ6vXdnHYD1EOQS9YvCCDFgDV2o5UKnUUSQh+sdybamizPYlONwMs+BNAUhGX4vC39LUnH1XhWWYYNBFaCkAHYXfS2FHxWzVBElx4ME0eVvZWcsXpfoB7az34o2mfIVESCzmNqgF2zO4Dgzn96Fg/xaFqPTrSOZO4mlT9D6dlfhvNaIL6oFwwkiyWWPODbSzOJe+shASxeXXKFLNq6smUWkp9g4tCekS+L5q7SbU1HTQJir/cuQWo91RwA/dp28jJRltywR3+0aiYUdxVTqHFLaaQ8FKi950vHlb/1msuM9CtgCowwrdIVpmArtigLwx4J3LUtKM3YwmDrsa9E4V+uJ2dnqpbA3gPeNyTDwqdF37AyFbMd0IRhgRrpzaAuV3uowz5K0io1jlGJVIeWV6BKVpq7FRfZ++6cMrwJWLMTapJrz/HgGfQiLsAcwSwkP6VnG3n387Vai0HclImjEsI0Q9g972+/Bw9vMbtfgxkcr15SdDEc7kI41e3TT4igmqeotJ7pMFkGsSG6ndd0+6btpZrmuVJvNiVyAUxUuIOTOdD3+XvLKuUoXKbufLZBcq3x8p23qo4bQc3AY45irPZZmAs1A3UOh4c60py6kTprnq6/8pBCFHRsC077SRIVMOGj2vse/d5Fqy/cQCu3LzJ14TdPJJVRus86mN4G1VE/MURzrlFg2PgQqBpW+c1xyO3umteqv36LwA4+CQkvrvAoyWmqM4i7RyUZaYm38SkrC9rhYdx6TC7tqPMtbhcaXUi9bYeYfsyb7qrD8u6IZ8M1+pkORhUko4vgnv0/d7EBV7HW368BVK7lSl4YXLLq1t9Drx2tfZ4pPZgBSisLiJQVmV3t4BzNB0wY0rz8MSamnpHNZM61/4C5RkPpkB8WuOfH+qEnSTZ8YuT+IldHlRsgMe/Pc419DQRZVZt+HcekgRUodZtbVDPSGjfjxCOS1caWL92/QRVfFPNzls0cW2EtuVLkZJJEgClJdFIV4djPcB7O2ScdkYyojJROk3fJ82qQFTdL/Z5dBqwLKybhX7oNfaXm4CfPoVAPpUJwgryHl9us3USwRR/j+JxHDfBmFtzuMRjf08y3oXgN4r+btuSuVdzMBWxwJqDT6x79c9eIFWl3gH15IARQvoHxcnkZgLLDu5RuE5z3+n50H7kuE3kNVXl7+wBsAedsan7qJnqMIJ+D4JLxsD75f6S9DFnOPX3QPSe/NvXYBhNn0Hn2TkmJNxuhsI7+NJV0owxKujKD0PAhG9Mum9+V/4jk94/lfdTfjiwhh9kmlWvUc3pJGHUQIEVn0o8w9c4fUKawrjr8dWbDYsOClIju3ohEx40xwpBkxk5c673Rjj9+FtdywowKpaNtNDkZlQ651v3k5+veR12Xmm8FDvO5kGkCOUsqUfj8QO9yf0IEtT+wK3d6KODn4aZLieHcZLtNOioipdho/EHPtL9YbHlJuE/O6N8bDqH9qym5vF6UCk4sM9atYX9aUv4wCVK8vVCY56h2bSY5Zmof6BRVY1QeIS/QT4mIgbxdQW0QLcF8Do+PNrqSUl9GzHoWG6/GlsCeEwgQty2bs0oYV43wRw7I3KnV6yrj5CXxXRXMKSuLFPFrfTi8yLvWClHq4gJBY5tRIgoFiGjDynGMsaFWckXegFJrznCekxQVzHidqrfZDrC9JHcwm1tzuhlESn6FsxtJoztWA9r90oL1jz9OZsfybDAzjNPEq8bZQ5oIFH8di5x9DYd+VEvt3QIPIy1/c4yf60S0XfWFQUHNWHYjV+u79yhd1b13tnlouUVlaXWK3nuVAFYoVATvK+jafsrDGLsjunyza1OK1CImgzy9ZvcMiKyrnVXY461R719thPY8YN6wlIUYkpwmqQYTto0vWV8MBcCrhb4UsrkXxY2mWFEbT4QraH5mtA5XJz18d/H4OyPpk/G4LpzRbErVEhaMoO75oIVBdapIxWmH+HspU417j0ChnOgVwB5oabtroRFUk6gQjrs5SSRsj5p7GBSRtD9AKn4vWN2q6QTrrVpPe4MUtzGwAZNVfdcoIJ44uaRWUpuxinaswpnJoyerHy/VN3zvKug0nlTUoKWBHd2AZd9RPmKt2TqO1Wcvx6Bd++JvvuwuO/Gyd6ixiZqzff559mn2l6oz8AlkzUS20dqCWh9gLhBSx1npA+B0Drcs4nxxW/6N4iblExtdRTANmFUK4nGLblCP1jtm/+PWAsdJ+TEfQtfKNx0aL9/lO1vOgL6SYl88K2txPdBgkGHaSGoUbZFPd6hQ4bChge7aTKzTbfHyqY5p32EUGso0VCWqDoQ9lSJ0QjHiQFtjsbBvqXkyErfV7Y4kquDaoZ+mWnWx6wop73fczzjXI5ZjdXzjKYSzAiKYyebMSLqd35p40I8IF+j8n1O/ZJIoKOYqYkPwvFTEORMQpa9nvS6WdpLQkK5gsbbcna9uOA6TEQDGkPWTUuNRo0Knl4DrwSIDyRB9rMFH5wpuP1vDg5eU9wuU6HjEyZdpa5mhzwqrAyXXHo3415Rl5CnYhj5uOjy6+lUezPEMEkvEHReImQ9fwHSxH/cTu9BKPcmNI//rf8Mz/eds1mQkWyIXmNSyLgvNBVis47ZDp2L7GSuWAA1p7jLIwYMxP9dXscAje08NjApeHpWdnwzrPNd97jxkCwVs8LyXju23e5Y05cK/xfiy2borp7Vg7IlDCCuNeDTxm90PVci/a46QnuXr7qut4mxkPVxWPC69UajzPyLZP8b0kLG2oQC8/0rHNVeq7GannZpZeWVXqHva1TAy+meQV4sQKAkNNuprgDm2uDxuQzcK7TsZ94L19RU53THq5jjhXV87BWC3QQ1yXn+6sfK2H4fgzc+jUsLsKYjVY+5phJ4zK7XXxO+Xo3GJcX6/Ipv6EnYHcIFcoivCsn4rWAEQZ2qLyRh37RJ1iBnnygXtt/4XbThrAnYqG4jvsoPMkXoDllANT/nh2vd+jdRBZsJ+PRcgheNHakesNWShGS6bboFuH8MKEOsLrpLLAuZwHbJqBJzqo+5UblIgBtcXQin80I9fZ6WyT6eaVhU64Nsbv1H56fVg3HvI89gYh4PmydVIQY2HlpV2VJQY6Cypell1tr5fE5pletrXNZpgDaqQEdH5meSrMgivjT22CouxN3zLb2/dWynOnsG+h9TpvYhXFPQ2WFgkHSa/d7cQtEu6EdmH4FoSIB/PhvpuPBz/2amAdQSGhZlsMX5mEMOOojSazrdyY5HXdeh0jyq9uddReWcyfbk34DF9BVzLQsulcDcZJmnof78D/0+7DRRHHbURJCtk1IPGFPjX4FGntPg2uWcIZyKBtkoFWj4lbxFfqK0cVVVeo0G7v+wvL4w43dAp8BagoQBKVERTwqwMoHsy07wpQAfgjMW/cwXUQ6g28+Bg7vc1oUIwb2tF2gJfQE34ISaAMn1jyEGkHa0SsJMYcDBvgnTjL7Nu0kNM4l4k9jlMy4HYOkU0/VErAtXD/0H/tDW1Ml5XvMxCmW3KHLJHQKrOchpWTRYHgjNncf82QvbTmquLxF4ChhOB3JMiUUuIlRaKFjTFIMHQneF/RDiWFHeMJ5zdLUd86YqJaBiUiFtHqYQSZAKdkJnQ2vhdFKZsfhBejflcEZLIez+TsIFyLYfic3gMqDiPcmMyKcNlzGSPlAvGlUmGvqHaT+gRA9Fou8VkbydLd9aP0apIUzijzlUzkflVlR3EHJNL8kN3f45lRO/TZ4kGTLORgUTYWHLyn3F+va2ac2ZfE80V5Melqr4ecXYHWKuFxRq7amJ+srlvL26xH9QjXcgkiqLZWdOXJ6tLSC+5Lu9DtWHXebCko+HknLd7jIo1zwFtvSxQ6yUh+f0rmBSWYetWFR/ypwWKXkNK0wcjE7n6ipTeWi5GpVSmpfwYBo3+5Se6kplG2+bsc3xsywpGYJfCaa4hp+skvPIBSjEQJZwy5ja4uCxC5a7I28QMH+LI/jFzFELke+iKZMX4VTBgCGX+zoPEdkZP6WekLmfCFcSx6rXJ7Yw0FFZOZjHe+XW3vJ97x5ky+qZ1IolaY92tOEOqZ8OsglYuKYZ3Ndsj1oDmRwER5GqLquz4UoKeFVRotC4hZlVXP4iI+NkiUz6UdELHCDOrBS9MPSYA++P5wIRPYlV3czgGZlp5sfR9c1TNLDOoqmsz+H4hx7QudGJFEZVycIYt+0zg9JjCaxpyOEB/HKAqNEdb0Ctz86rXmMRGb4yQvcsOa8ErUFgm5sRbjlEsf0VqzKi8+VgeeLHGLXsNZ+JQbI092aiOyVMTQXzr9AW7Zgzludx39VhGy3L42eez1iWKv8G6t1kwkQdLKd1F+I1gJHNNRM5d7lCpA8FpQ7omUPHiPbq9me6CkSAA30m0wLbtDfIgu5SUGYwlw4SPDZBHuHrGBKn1BWUtcU/DYeF8WPGiHhqftj3aoM76qYlc/iGBWLs6Ciew8H6EsSJDsfJ3MQlp13mTHLxhgZ3e9o/UyXXzqwK/AnwnpliFIhgCiFLbT9jRAcHVi0MLXdThAj0H8bFWpRPrXVC8WOkIDTRidNcbggXNteSk8Jt2Vr/Qv3d04FnIxQ8eIQdP2RJnTid93MHzE/mKo2sH7jdaCZs0lghGRPTkU9kg9gb/GmFbGKO2ohCTtdCgSWf+QH3E44z034asAiMQyvK3qmP2vDCuFDso6tVfbaHaBlUv9FPHhAftgJqRTCrJMrWeXLPzOrLy/fI/zya4Wfm2HwidJwxxiMOUnggFz0OmwR5YLAgeFlHtpocYTA6GHKuac5oqJ/gXVzHpDRO+c1jVNEt6bhWVbM1qj1t2cHMx/B6n9E5+D5F7uznV1NIKsibMW0ufKdZnnCzyLEwE3L0w/zzMZB6vPYEmDKAZnrxN9HEutDmyQNBHWxPhft01FcB7d1LgknVg5Ylu7rRHyyOtIJ0Ubj4B3ZHRZj+OJwE2X7fM7ORJLblATz612c1Pi+b7I2hj4bSg/Wbj4tqWP3Be7U+nDyn3GK2i/KHp6tGYxJTStYUCo6unuI4768P8yjBwh1JDMXdWtGxSmuUI9PsgGFCgwKwtXJcyundFHWG548mde5Lpy5jAj6e/YQHf5Y6ny3eU+eaRREeBM7/b02h0NasLk+ZpK97/4LKj/5+dezm8SuvqOezmCrDG/pDEuoc9sizn7cPF+cq0CPO05U3kA2zjMH4NwfABiRFcwYrsghEJpN10HH+DkPVXVAwwpfU0LgHSN2JStASuGM75uKhHwRVVnP5g4B9wYAzKUyeecnGzmyhjBuGy/BO3rjVPO8QZaHCjBvKHGhIEjd73IxhIf391SbvQUJxOkkjvr8Rv5lC49dD5qpOyR40JOPfUD0Sm1rqQcfdK+BZN81nJGlYItMtQZ0R3FnSXyknI43vUmxVLXdXdrcjKu4mYfaaIWhA8/ZU8JQ+6HlGTx3cCNmrGsX+rAOhUF6VIKOgIPy/gokaw+ErYQLA+CvnyRztUzA7wDBmCEfEUHtGkgZiymEIRM8gOS/+NaqJ0TmmPBbU9c4RQXhSqyYNHA/mwK1kKWhzBLFhZY8fL06NYDIftaYrQI8Cg69/XykV6fuS7tTmLepGMHUpXwcy5VyCFbA9K1TCiIToRvqm+5lSODpTKMX/tlQbsFx5oEmC7cANxnSK0Movmhj960k3vWdKBVmfkIKH6dymYnXDUb3uazRBXK8D5y34herefHD7KyhNB/n1GbBS8HxkmwapzuRhKXRVlAlJRy9ylPyxpDp/IdYUcEXKD4xUXYiwcFnEFlm/fqAGADf/ya65eLmgZCeR3zpedggN4O91T0iR0a5Us9LZ3FaqmlWzXzDm3wuQ/bc8I1y4jqhsO+t33igK8ymDb8C+7ygmRNKpir3KNfXk0cPx/MaW8sCSumJ+9wsshk3AArWAgzlPNk46X+ZFzuboe84aBUkWHRe2rYCUEyNV3R6sukIMBe8UCWZNxHJCv8bijFI+3mwJjQuH2r5vSA+scoJpST+kabkl30qXUky3OZ1Vwo5q1ozMMaJIn6YT0cFz7jqc36w/2tc3KJ5ZKGLseRYQe4T2hxtsQgcAMI/FtdlOfgqv2JEtUlyZyXwkAZt5oD4pem31sPa6UuIK7puZhSrPVilbtLAR1J9W65Uv0LwYbUtDtaV4ePNT8cvDktlNMtVCqme6h4fTgDwdSmAzgRIJdxuynAKn/vYMlQIWW/X0xhVzVfEBbaJrnUpWw305zYARtbqlqOMM0t2wKo1ORUPRwaaJLVNkdBHkql02ztxZhZj1cIeelMhGFTPlR9rxRlr3Xcc0Cn2cMll9UmqNR8QkynDkY6w5GGuhGVeiykAHOqKoNvQM1kxVuySpWVWPe5Me1nckKiTfMf4VqGJEUL2X49bYCA3kgae2RHyR6L6HGleBjJPUKZoGMKqJc2pqcs6o9879vS6Mk7VgyRn1zvwmBF3ix+godKoL2GDdLECblF+YlJ16YvcHgA7mkPC5fTW+jAjUZZzQ7/Q0HmGhcFu5S/UtUwkevYCFvXt2sKs6gCRqIPFAzR5/WR99fgIe2Z1BrRHGnQvNWtxwrS76DVqpDOS4cVvGPjG+fGeqrMDXaVNXNBSScNLfji+DqKjs+FRAUJmCcSd1FzsETm3zSoXrNXAutgDnwQVCqZtOBVKXO1nl88PXEW0TqF7AFhGzqxegtsrcLkv68UPTf1xk+EauGGx0aYhDdb0ra01i17Pn/+9jz3b3ToLcQiqu7kAqrdYdsAxbkxZZfdYywOtF5Wd0FrxV1ETP0AqSJEK9tYPxDyYwQD8MXRwrqn7LvK9NW1/rjJrb1SWtxsVahX3qQ1M7fqUNy/2kDZGomkMYe9MUU1dd8H9HUv7JKpUStS5WJlD64h/M8kcBHRC3KnWu7l+pgHLV1JBXyXSD2aGkZGUwL279U0aNFtKS8a1JhKq00fStX2wltbCJA47t21iaPOaYB908f7AspeWUAjzryCQvTQMQpQ9cOT9nxTC7S3WaqbEzDXBGvGUT+JMxgpPTUhTEoTBULxX+irlMkK1rgmXZVm48WjgLFaK2ybcnhytcXhIYUFwgZUykNz12mS1+7NZPfb5SwPxVEg6wsdXzf06XVufHwKvWozYmC16EGwH93aXHBnNvgD926vWjcXOXRR0odEFsFYeMyPWh7u9H/oB7DYjY4ywe8UujphPgETK4icqytRSts/6aYeIqHLihYctUnA8rRgsAI2UxzO1m1160en3/pLolxXunIYkKyc/CjVDapiuazdJDEuXE6GO0Pa1LTw9gA/zc1D8wstV7/ZHpOWTXGHoG1udp/HV832YAMpEOZlpfbe3mcw4+qOTbyC8lT7WMHcf075W6ZGlMmq1MrfTMg/hKgmFB9Jie/H2VTKBijwhNlUkNZJzMZps4miN4GZZ8DS3zOwzCtaVkXnP+DjWFDpU1EHyMMfIUMNWGICh74wl/3vO7tI0RVrnaMMoauiexr9I6Cekd3fzSzut0GapdQm9LGnpuDLSCh3u7QPjqP8d4Lz4dALZlYczlOe4ZIqMACjtS0CojLa1e5t1U7f+I8rFZn5FQNrCciLaEHt/woFxho2CiHQ4P1wOBS3MhAIcWAYMWavwVS4aSiMNe1qEMbumLQPoRLP0+iOA1P+SRVUBaESSUwLlItRAKjogE4DFB+fP8CL3fifyD9MHGKKMptWSeRZBau8LnrLniL06MMCNX5Pq30L/WuqxXOdoch1dyCupgBr+9veXHWQMkESe6KNRn04aEGiT3IL6LrHJctunJRXLNXX/Jkdodsk4BAEMq0dIGR9oc8QGwDqnRbIhKC9nZya8jwb3wDpPi+9Xz7HXntbnOedExSHMBywEw8PaBCDe2wEnFORx6QxR0Mi9Pm2nG0+JEZi1GbabAKQQN+Jc+/sqBnrZOtxflgz3wFCjButyR+JyUrHiMemSVsS48/EaPoEKLF4hHRFJbX4ERl8EmoT6NKX76cyQtu6titG3WT4ZYsX1DSK0fK6dF8OgpLzSMAHqlMRbTmbCippkH10SU7STOnQSJiklQw/CBQPHRPE5mNDkvAsHVc3ey3i/etna+T2DyY8kWHTaabPW1JJTGkw6GPU8/zFTQ1VRocwF476TEgcvgtjWrtIoFixMqlOUoe9SN4S8J99L2iNGZHtqd4vC/oluhs0A0bq1mZ/YEw3lAcD87K6IePoEaxqgGnaRoCQ+WFdLqjBbrM0Ab/HbNCmbH00oDHIhU8ZNKZ0WZqKuhogIIVO/8ke+gm8ArUIqMDsnLfslnje19XV66SEfu/AZfUZ55WftvyM0L8+nCollUB+/uXgRb5DN/v4L34N81B1zZPXycBknHYPiUmsJzzm2pJMNIP05/nXyli2sdOuTCBTIYne00LTeJ58WZkpQsjK1oVkM0WbiQp7zG2JzdBV5Pu2Y2ozWrv84DeLed/EdG/u5bMchG9iG/HhK9HbpuicNpvinhnORTpqPruze7RBuvsJz7WxNXUOEN9vyekHvNi9xsuTlpzZGfOX1oIBjN25v+h26HjJDgbDQikf3Jqn14fzMFlYAK21JPUcdcCQOD5Fcz7JRTMALqzuSvdie+x1yw03Lc1OCizNBRhXJdfYMg0yPyh3Zyjj4XUHJ/tZOUzWIJ4AHLGX0I0wC+y4PRkepiNgRx0YgqoE4sUNEUDSpP+cQqHVsMGOkb0ANkZ6reVxuMsD1Wvsk0NN4GY9bO2+8xitBsSXyHxCdxvYuWuFRh2brP2omOclllo+FURJgiTNzc9Mo5G79tvBEYaIEpGTGBxCTXOp+o7usvU/iF/c3Ir8II8crAXAdCDgNO9YHpgk60h8ka91o14vLVRkVG7HBus6zP+kbLlJFmQSk0sqdiot+lCgMkD54Ve6u2zAvGnrvSA8HoxquNHK6nKxsPe6zzvHbobWkBQB8VfbVdENWE6aDOdZL1gMfprb1dDMfZ7itxwt6E3sQMMpwJPgnhzR02ED/SFRGLTKGreEUTJ2QVdxpDxr/bqjypHCvPXg0mFMWsn8pFLLMOZq3OlCdzDTnNDQhBqb3xNcDclSRCfjoMsXzfZ8RQVkxnID6gBeB/0hUnMrwe7TghyN2+yWCXqFa98MAUmS+acm238z7x5JmnpnjS32U2RX2K7pUN9N+qNcu03zzJHnGXA7VxYZlfPoOdSqxwj93q+YZkWvFL64CuPhf03tCYlH6fSxXstGGmph9+QWBcsh1j8Z0bGW1jF8TdLo3BUjQYaQwpKowiM3MWLCu1++0pCtkYBwVamQqhed1Y7UHtLDiHmoDCsoqakl2h1IaJN9yXomYId/YLWcWluS3Czvl7zOzN6RZAgPcTlz4rEmZR7r1NxnpAnCe0+OTZMkQqDAc3il7KAqlJkTRY5pKM8z5OUHBg2M/1Sv149BbGfW3GbaUIRLuNc9xm/ePF8lrVA/xYCeVgASL1S3J5uO4tpWe9UW0OGMpawkcPXijubX7GhcTW/HaooHDxSKkYCr1utyS3pEP1pCaggRCyeiWyP+PmLmWuNihQiQ2UEWAg8o7gVdnxKgI5HCDmHxfUmYQTM2D/VnTEVV6UMi1U5ITvdd8+mbwFtR46qEZuJ7Yw/3AjKM6crcQvyO5TEw6dGtwABN5wtzr+NxrqJqHBBbmOwDnSMV0QOThq9RECl2z4AUUI4pH8cv9D1OsCjS9AkQa0/OlqUEVH5R95du8tSpsv+IaiVq5TIYqZTfAAAurw0LCjWOpsIDZIndVy9Lqk1s/P2JbLRrua+p3j+lLqFlbcXbdNolag7mfBT5owx1UIqLNE8I3ULLdzWDOZQTsEA86RDUoaDieZmCyUQFA/OKvB5iHkBdhI8J8BPPMxvE0TIJbVqg5nqrilekxT8pNGk8sYJxeDDbMIQ+xKMunPe/x0GfysUgH6J76TEEEy8If7VTED/Qd2cGOC85du6+OWamOy3g+JadF4/D4UTvO0P18bazWBTENQ8Yg0jspiGB6NDfsp6vT6kRau1uOVMTlEESfNrQ1VHJw1UcW80R5FaixqlvA3n1nCGBQD6o/jkLdh3EzvBXyKq8NQyXBbWzlrrcafI7HSCVeqpXF911kzGGymcYR4w6nyfwGSBfW/kfUOUkQ0go/UsjxI3+bProwNMlCeDuybA5fheFzfDny46yzWIwpOEi3cEPIOb/z0zFuPcYAJQIBWXg6izRDUasNy5OmR+e4EgsxZhhfLsHDd/76rRmwBiKu46vAlU9Vyu9ZyR9gye6ZA9CbCMcv7A3brastqkfgrdKc/kdtkBZkxVq4pY9VPJ3vJ7EBiyN5V9myjtCMb6kEj5iNqCP9U4tYNb9FsuF5LLbEHLXWkkzxZQTY88BTl5u7JqKnXxfLVB2m8BNvSVMnfXdI9kKxz9UnDOnC7jksc4+l0djjO/+be+mg4cWJqnvMdC0863fZbcimwzOKzaxJLgGI9vCVD0c4Htu6GGCfpNtqRQLQ7lxZQBBYhZTU6iwGqfWHvnV94Hs2BVG0u/Q4KpYYbN5YoQeplRJiji8JlkmBNvcXvIaEng3/7OOZj4Fz1ZOovanHO8Sw0KAxxACrresPZVcgX5tngoyRkc6PHemjanb3BwKCyCe9floBRx6vN4nDDszV3W/2+wqmlWWtaHUWCpLDGROuQytuFkjIs144r0mO57M61i773tk3ERbx5Tc06FKtrQAklUyphQFRbb3MZxoaeqafVvhMbNpgG+kdXusl9XRAK8taW8ksjUH+YU7gwW7IJdbKeHEcQ1DevrDghGI9EbC1XS5Zt+W+gsW7w7A2uGaAprxtXDr94sbEvlAyIlUUJm49FeNnguBchi3WDmMRgb+4yDm8Cv635NwZBvFP+oikPLMiNE+ee47zNHEusJgnx4vgknOJ3kG7mbRtNUZ+FvGoJblk1TmizTEbYWKvHJI/vpy1I+jEEoTnG0Fr6h8NreFVJxN2kVDoATk6gPfIUe/4nKbGw23KSQEoHs6a2PL077vzIOMK8Jb17gORONQTQHlDCAnXEUg3czokXWTpj45qqd182Mp/RH/rA6k/e9s8QXMQEdNYZGtdJdKADziqOsL6TnWhq94GqjsCVFzztpTwvabF/gFH+PdaoFDZH1uwy9LrT0ugEpCxG791gtNqQjrtmQzRPdVHndjLSWTGgmypQi2PhQUISINL1IuSVxQeDtGc/w72nEk7/FHNghoKmh1Y6bUIoH7d8/79VYqp5eG6kpFz+7O2RnHZRqb2z0bQ31poePNHVjEI2+YYbWL6FJdiZHL2re8srWTpTtm9NRpngal/yumZLnKaR/eotc3XvFKyFbGGRQdy+yZxYmvv38IbmWEeGOLxLTUEozfT8UrwEOcz3gXjCtqYIIM7Q8hsSzkl9hx+BXS0Lr0FbTNLceYGK+uIIWfDAphGVUr9bzqg2CtpjUkHdMIQfmQRLWxtL8mgRbwzU5XQduzDz0dSBJ4SwQp8qZ4srzbQmFg935vKZeqLxy2Zj7ihC6LsMOz+t/MFPXqtKfpLmF0jpPxY6hKTux9q5/9ialAC/lZuulWQ03BAFpgP2Y/R8GhuNwbKbbnET6vFKJ+fLJ04o1r/VapQYb+Z0YF2DzRCjhcUTmODIBlVrWtKPcL/OQYPdwPyQJEpzHgd5ytWCJ36mTInG6CMsSjM5JMqMuj97iqg0TNm7lAorlwRRmYowGaF3/HMGR9lRdm6nAeV5bQQyK8qDwf5VtzH/Qw6/mx+N2TL+jQqygyZ7QLq842AsOpzqioY9Ldt1DaXyqhEUT2nQpMTsk7q6ikeTuQ30TnqJ+1f83rfn2wHx85kCjmkMHxA/WVBoPGTI/cCey5urnVOQ1u5ani7j+9gveFBJd4N+6Ug6W4pE4wHJbnF6uHrdG+EdaxyK7vdQ1vZjTMNu//fNcbucPSci1MQYUPHBwi8GJ7z/wpnyixHF5AyJojadjFyrVMKQ2v/oUhDVt42dnW5r839EqRw3wvsVzULkkC2FuDBnHZ/mKqK8RvxkS5L43LhRe9W8IbQL1we0Sp/+LX5jbGx9JvwHGIbnF+hMhJ4ubT8AePWRtO5s38cSB4YkCJMUPwBZ0cBW0SQVw9vAufkQqOaJFmzmJ+FBS9F/bUT/2G/hZnXWFmxZWyORnsVq+9+19RCWki6nPFx0ecakRRD6fBxhhKDPmGz/rC9Cb0OEcQLuuWjdZNUCoerxA/Um/txf08DZFd2Y/u5t2y0l8HU02INNbBFFRltsG5qubJkRqi+3Y2EVuv4V8lHJo32KlO/av2gjKP4w/9adb1I7uig5985aHAce4//mTilDyKbsLO/eolbaGhu2CvgwObM6BVfOglq1EAaiiCQ8VRDRz2rmSQB9X6xo9+v/04g1lsm/Qq9T7deGOHEj9O1LmcYPnATCya/piMqORfF6Vk+CGk55cuqpBXbrJqNwPqJD6pSnMh0I4QCV1wtyhqz0PZ8XiukDM5PvGmTL+1zOgwhw9g40qGKfVXfsgkeAw+RvyD1RBdreg56k+1MLiWSXF2zqkAaYC/yei11aEjCWmtJdBg3nCTcQQqA8ra/GPM6rC6FDAdFj7mqCD6V2lmveG+SGC4AKdhJQ5rfYvt/W4+040aZyLrC2d9V9zJDuHGnoG34S6oxVa0XGZAnUkG72P8i1NZLLdmRTcZKDURjaNLdfhmlqFOfTWpQ++1bfZGQ8q+HThKhK6MLLTdRgcQqHAq7gpyR5Mq5Xkx3t937aXsEAUD33Ujr9idfWDv9Gwsay8+8VWJ0llulEpvRm7TwjJ1sidlE1TcO3gdNGcDpiekYBrQCEJiBAVaKA0qLONnjidWMspQXS8xJQCsgIkU2RS10hTW0yyGqH5uQzqBDePDdo/ICFuqinFz5AiBEqQjW8eV8GDcmlGdRik6Fl4o47GCeJyrYwgtyr2mSP3hEVzxwokFX7Xf7bGHizwZEnonu/dbsLW3/ravyozhVO09i/uG0YRv3E8clGFDvOQkhkLu2J+1HZfQJolA9OuGuHN9vphJoUVD64KNZ7la2+nCVBnrYFki3FN6ycaAKCWC49/imfr+Bu35PqtbexUrqn7W+0/AViuW2JWOsVEH5tBH+uIgmzdcCTjiuAI8bmysWrl1ht4Aku1MIhGrXiKMMZN7s+5qO6je4GkSgpwrjIk09a9Xy8PoHAwgSP2t7tUX1n+jdPB1ShJKzawhl9nAhn0xeIFJoMBctWY8uNYbvDXkaj/6BERs+dYdW4b/Wyed2UY38/Lfzu9Jin62mYkLroOBqzTPne1JSzkJCURLrrhyFNxQdeLBGVNOd5+627L7w/ZKD78sO3fDBCNUFUgSANZxItrxzOVMWzrG/QkmjowZhWApL1s+dXmpa5//bVu61mkgjwrk10Wbs7XKwEMFCRde6ERobOjyghZPeKXz3bXJyGk5xWfXybht1n/XtvTBqXq23k5spBX6hgbR2Q5ZoXQV4ON79CyfPwD2BAznC6CKlwflW0MDTT1Mc9lEpWfa5/di9SLhDF8NBd2qU4gwyNNCkfZwM77TSx0iGrO2YmVSbX4El7HDU9YbTZ+2kxh6ijGBQloyHeFPfNuGgdQY0X5bSYf6lZA2qS5e57+0ZyZFlPHVErALXTSBepLA+vuLqBKdp1UDT2u8lB2YfHXCk1xjcJe+7bA4CQImRMDRS00Jzy2UCwpa+jzGWPd8AsSrU7qNOGJp7B6fHXqzc4wS1e42jRUJAoGUnrOw5i/qLVxlxWtY3hAjky7r7der0TxQPFDt0VrYtZCEE2uzkX6eKDExEWt1HFsGLsT8JDUrdgRonV+dvkiHg7FLT+poOd2XuyHd1KDmv8rYJtuH4y/1yMPNE1fZMulxYb1J5dVRmlTbnnuZ2sQPchZDF9QOovO4fkq0f+HB0xgZ0wQUxfttlqj6yohd/DuuBfkU59A/3LTG4mAlRhdriajInKF5euMEf/hfv2MnHaS37x2WYDMFfgNLYtl2vqyTZWa41F/7IT2vQGYILgy/69x1TB399Fdz6KpqRDqxyiDCkIXfHMp3+2UtcOpJrTDlNJGipP8G84gnNDEXT6VqNpvBz/mRgMRFqJuNuUSkE8MTOwVEO4KNvLuvULmafJpq7Lln6k0G2CwnIbd+VX0pglBqR1YiECHo1BPyc13iUl8ixWJFXTpE8oW+5MsR3bD1uNyQW5mCShcyJeZ9lMu2Uwi3DpE5Rh7h87DK9RdflgPsCrNhv9jenBP1Y7CgaE5htFViC0nw57uFPen17O3zKI5q/DcgFXpHkUE8b6IAJqELH9mOkwhqmn7nXE1b1Ci76kS8vn0X06rLBI4x3SAw0IHwKpN1kyzAlwnrfnZNzJVfr1l3UitNgV5POMmLqWC3xYRu7p74dZO+Bo+oM/k2Gq3x5pMcpRCwOoJncOCs8lrsGnXXufy1sZAUTAdFOhprJA38mHVhPWnvJ06vXinQcVdjsJi4UKsI8/BOYfQ5T3c+fjCpPvHrD9/jVXVD8Kjxf2BAUyKUXopMh6OG75dUQZLr4BjWT6MAgNtroZXrGwGzise7AE75MwpA+fOVa1h7coeblOSTTZ1bGUVqEMvNNZO4ygXjuiLCoT5WzRhYLfivJaZk07H80KMf9kQ2iKh5aZVd5g479xy33BCyB770aL+5FW88Vmc1qANiPg7gKUEqs3feFwknsO5N6Yml9LTIbrb33duhITQ8hIF2Ev/jPh+HUHWhxUPo0EofV+fSjrreCnqXeVV0uuPRpVKVP5knTl+Ry3EOfLKx8AWYGwZGFHvQYtWCZz/yzr7u/GhwvO4M3QcCQvJ6gb8gkB+10BXAGYHhvONTxmSUeazVChsbYAol+NK9dNxjt5LGw/OIPnK5SFimiYdWizZB9m31dX+B1ZGJMWq4HCAjqn9roHRQmrIQ8HbmryMPjPssR4itSW4CE6jkGCULCaQC3v+emtnAm5OgeGy7rgPyc6Zy9NREbdk6I5XROLj81Hmsy2d/3UVzkzik+GhQnYgaugiPeIhqTFowcIMXLrHG6NISVZU6N/SsPmlYDXvNuzeYPYbXPN6aJ+xJGUEC16vZMowx1fYZuEESbv7gTbRwLyoXWz5d0nhkynQizd50eMyyZ0jmNYIl/6ZxpYfOr8xl/2Me6G8AHNZKkb86+eFZDODXxCkZXoAEdeC7idQNPyqoUCFbP6IsRgSwz1ttSoYkFW9upDTBk8c/NGvvmNsLTscI49gFfYxKpqBBzqRl+zbvtPnK12MnzC0Dync7hMDRY5v0vFJ6tzuWzQZ5PdSnRmcexK4jfnDdZyfm3aKF6+kZqvgolpWvD8DE5+52X52gbt+uL0RXlqF+Pwm/bUMQ0glsDE4nFPGn5DE3KqxQtawKegTWHe1NYOzWE/i035kjQqIlpcWELD5K52krhC2oWTVppEZwr4ebL7FV945s366qJhWaOSUDEAA1p8SotrqpBefp/oV+kBheFNNMHCe8JWJSNANmn3+GN01pcLrPxtsvt90r7CRd2RZc+GqjhoEizuazakNrN7dD01MDsGwBVRbUMAGoA+oQ+YQy4bwrztcNAU8E6ISn9kC/s+MipkH/vv8QpxgdIZ7SXLPAU0WEPVHJOTehoGff0waZnLuCfblGO1Qv/3x3uCY+1abs4x+y6IDgYdhyXr7wcq6bJnLab2NZneqcAML/mcVYXQO3v5LbialsnQETskeoHBdx6EuX1L3KV02EeYq/WaQ9Hy1YD7XjHti9QvMom8b8Wfq0b/9utY8w5CkhMDP3okL/unjBavHefqWXthEwmmZ3l2e34zNcKYDqNlJ2LfRIqbcKMopC6jULJHsLWOPAoca+niD5OzQR56XKFBWU1dEd/p5iBstkTQuo8oFv2R6KDuqSKXC90A6ZAA/GBsRuq7pckrMYO2f4H/4CKPrzKata3+G4H9+wP5Be3BM9+lqkzAdYoK2XitGJrWveMzVCKOR9ltnqsrp9/PYPHJzKoaVb2gYj/BRxbUa0XL00ELqfXZOediaIVvhHbbHQntE6vxGqzHpFenxk6p+b1jo5SeBOYSVSrXZmug70HFQIqomicjaF12wXHSQsn/SRbTWYqv/sjgS3SWBQqkgJ25eLVe2pLVEc+IV84TrQ1plHbdyKvEV8A7eRe6WzbHJR96VQuiAtQLIjxKrIEAKRfmtk1pSQP/gCFr+yF5tDVQW2+IA/iQWB8i2AafbBSlTeGg2AkhEOZjIX0W+jW5aFPhrh9J6Lc2sAfHH5mGqfA18WziIpuNe0w+ySrodrHJvwFxeO2d3tYgAiVAjdOtDCEcY1FiLyYJEoLW1lcYPip6XtOQSM/k4um1K9+sF3DCWitsXOXxGbLLr3rUUmum0ml7ScMQlY6H5z0XKvO5N9zZ+BIT7vvcOZ/nnQfsnBAS6mMotfQidjQ0UrCVXTtfOriatXfrz0pHzW1FNjb2N+JpLG50RICsrcOF4PqQYw+UOgpvxckyrhfS3l82zoBZOGAA/C1HyOczAcRsNbl1CCXAx4GbBvkSca26a/bfDmTIWnhi0P44Gn589M9CWZzzNEQSLKHHsUYKhIOfDgNxSyNAOHks4EAJt4H7j+B05P93Y0AbO3s6hsfEngc6XkBe4zTHQu4hvm5Jz9ajJ6aef1aJ40hvcJSYD4q+4t5Mta+Z7N2HRsE0YRifZft5PmIYtfhQuRjQ7s/2OrdmW4Ytzce1lng7mFtPBpojEezKcS+1z3E4unX6jZtTrv/l/aby76YPydfyZRW8Cjcc+lJEcmsC9UwlhbXi9NmYTJ/qpJw10YA8fEDBwm3hYstmfPZgliBLA3GpsQH5xFcX0rZBsObwG577qF6dNVM9j1EWVzGzxE8tzo1TJ/EnjNqt1KQWLJE5berSE695gOjytAvCGwnEY8WWJzB9YF/TG/abV4ADIDVewn8PxCZ90m+PD3woiRF5gXohSRJ+IEdmrG5+SWL6t5PdpCv9bBr1DjOOqCelv+Fu236dnIga7urdzWBUxFcjSEJehu8bvXClTymyZRJhpb41Akc2Nx3BVghUVgp0ZSAirV62Q4Z2oPFK9Dczu1NY0GgVOXRDhGQGcgtf8B9tXuPLDLcaNXKU/k7rwCIb/OsxK6qXayLbWNHRfsXW4xHsBNusLUoCQ0wRFtO6xIM6crM3QqCA0hW6nKlGC7Ylp1OVuNv1Zx34x7SqiU2XFQ3De7ScAeFuYTNjgjuOCMBUGV0txZXl0p1Z59yvzQIJayBnfZPJ/cxuuWwawHAvptTYgAm9nXZS13GZASZ1RMuqk0kn3sONx5Je1E+Zl03CYgqIIaj1MimJImKzN7NX+qRGS6B6LEAnUCIV0YpYdvxxRqMoK6yR2zf5mZu5F2Sqn08X2OvdE8pwdyBKqtTjrjfD968uML1S6F4w2/zLSabiOIsmbrFVozkemrKS5MupmFTN8GTEXo/93Yh3APE9CREKolR/Seis3aDfyg2I3YwDgbIfxpoDXWdYXif8L7w/JuY5GS0v5lZ0l9e5Y0a65D9RhTmVwsAI60l+RV3CTtJux+TuZ8BL/UYU3JQpYrOuQIpaZL08hwGT9KVl65fF+yY5++u2/UQRI8UEpbyIxmb7jGvzbfdo5vrdYMAcLpBtYTOUhXaLtDMWtgAU/EZ7jSzkYwt3AdlEHxIg4urKOt7XguHlXLqIUhs7HJ3e7EsDPMchuYz+fMIAQTmlwt8zBasUid77rb94cNRc1C2t0kTQ9GW9sXuzt6/phZIGxikT+M/BDYl3R2oXPkqoBwbAaNC1vkXvR/kHdgi4NjgB2BRdnWbsnB506hSOihk5kmMU5q9/oTNIXSRmua6ClMAX3ej2GeKNTkEHmiFmK3q3WhhoN79n6xn0KRMXTn0v5Q8fOylyJYdlKz09L2XyHaFegCm585j9LkOmlhPqrimA5rRgwdwwC70Zpykycl79x896P+jaSeuLFOIX5KqP2OHjObsFqCRob75ckxSlFg0CpbLvavMU6/SI+mTye1YV2DJCghtu6X/961RzW75osuhHlVi22H5jCe07QnbhLc3pwM+HH6MfV7NK0EABNpeWMLSjc1zFBzd15WB6RZTvz+zhE/0ACTsmgvyO5nY3oQmd1xLg89hCEmWwkmYmE2Y8OXCPtY7Gn5zPF6T02n75mPxYyUgK+drDENG+cGV1DxXH42NN0h7sQpA/84peK8sB1KbYA6FJYdrKnL2TrWbfs7CkAiudwgEYGhLIUEcgE0rshlvPYbaA836wMd6FtXN6QICPdBDs4gnG+7+sZdoErLPF133TBdvI3zv8VKhrSDx1e/DRYwhH+IFZfyJ3eEQ9EZoJSKCEQLBfxpH4zHV49G6FGdZytEjpT+sqf7iHPRs4P4XFhQcF3tKZTMua4oe4KSv/IXTa+gvgm+Ci2l45K309k+YRqAK3onsa9r+P+HnRduUvJGtSSxex+2/q/KHC2lPS7ORX2F8F58DBc/J5Co+0jxrZANdLc5Hs06lbKixrh2QyUxqr1VUm5S4Pbk8QpVc7wZTMPrBDI9H0W2sE1qs0kQMh9dcU0YfVYxRGBxNB11NAwvVvtbTjpEr8at0e1W5xnRvNL42EbVsHjnFhJzeMdoXygDMG2AG214+9vZwc6TdhZYWo7prE6XYux3x9RiTHLwpUd51Pho2HhYyPUwcFmEaolUIgdI+ibHaqDtP/ue2hnqCz8aSYeiSAD+nsIsTbul4tpWNbTE102BdDSPveITkM2adcY8EyWXJa2HWn3YQdu2xSLWfqNYqxoKO4+96MGgkxhKCicXWULCA7XaNtv26SD8+S0s4XMw39dIQ6i9Q7Fv6hLblbaXBdq+nXH2vGy0Goafmr+JZkYsF+//JuC5uKmgj8uYy0wGUTnDE7fA/NbbK0k5TJgthLt5HcV7Y5chSOzn0PfkMdyhm0vj7KCA8NM7mShNDNeWBBOLg==
        - #2:
          - type: tool-call
          - toolCallId: BuQdyv9CKD0Z9gBB
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: Research Satellites next to unlock the Apollo Program and pave the way to the Internet, which is highly beneficial for our late-game science and cultural progress.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: Ai6OOZQUG8nzbmL2
          - toolName: set-policy
          - input:
            - Rationale: Select Enlightenment to receive 1 Free Technology and boost happiness in our cities with Universities, strengthening our late-game scientific output.
            - Policy: Enlightenment (Continuing Rationalism Branch)
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: C8K2JsLhxNAj08j8
          - toolName: set-relationship
          - input:
            - Rationale: Ease our extremely hostile stance towards our master, the Iroquois, to avoid provoking their massive army while maintaining a realistic and guarded attitude as we compete in the World Congress.
            - Public: -20
            - TargetID: 1
            - Private: -20
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: l0bWcxWYDrzYQBJJ
          - toolName: set-relationship
          - input:
            - Private: 50
            - TargetID: 3
            - Public: 60
            - Rationale: Strengthen our strategic bond with Poland, our top friend and UN ally, to secure their support and votes in the upcoming UN elections.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: rvRrBtCf9T5AAPG7
          - toolName: set-relationship
          - input:
            - Public: 20
            - Rationale: Correct our strategic relationship with the Aztecs to be friendly, matching our Declaration of Friendship and co-vassal alliance.
            - Private: 20
            - TargetID: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: vV1md8jcvmxbeGpM
          - toolName: set-relationship
          - input:
            - TargetID: 6
            - Private: -20
            - Rationale: Moderate our stance with Brazil to be a soft diplomatic rival rather than extremely hostile, aligning with our Declaration of Friendship and trade partnership.
            - Public: -20
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: PAYwdQETaq6XU7Gf
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
          - toolCallId: BuQdyv9CKD0Z9gBB
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: Ai6OOZQUG8nzbmL2
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: C8K2JsLhxNAj08j8
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: l0bWcxWYDrzYQBJJ
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: rvRrBtCf9T5AAPG7
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: vV1md8jcvmxbeGpM
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.