- row:
  - game_id: c3fab47e-b30a-4fab-9cea-f4e8c677c4d6
  - player_id: 2
  - turn: 439
  - player_type: Kimi-K2.5-Simple
  - prev_use_nuke: 95.0
  - after_use_nuke: 100.0
  - prev_nuke: 100.0
  - after_nuke: 100.0
  - rationale: FINAL EMERGENCY: World Congress in 4 turns. Austria has 45/40 delegates. Offense reduced to 10 and Mobile to 10 to COMPLETELY STOP attacking The Inca. Defense at 95 for self-protection only. UseNuke at 100 to signal willingness to escalate and force peace negotiations. Maximum Production/Air/Nuke maintained for potential final strike against Austria if The Inca succeeds at Attila's Court. The ONLY priority is ensuring The Inca captures Attila's Court - every Assyrian unit should withdraw from Inca contact and let them pass north to The Huns.
- originalModel: openai-compatible/Kimi-K2.5@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: false
  - messagesModified: false
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 100
  - replay_use_nuke: 95
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
    - You are Ashurbanipal, leader of Assyria (Player 2).
      
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
      - Name: Assyria
      - Uniques:
        - Unique Building: Royal Library, Replacing School of Philosophy (Requires technology: Writing)
        - Unique Building: Lamassu Gate, Replacing Walls (Requires technology: Construction)
        - Civilization Ability: When you conquer a City, gain a Technology already known by the owner, or if impossible, 20 Science, scaling with Era and the City's Population. All Great Works produce +3 Science.
      - Leader: Ashurbanipal
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
      - Robotics: An important technology for the Space Race, Robotics allows you to build the Spaceship Factory, a building which speeds the construction of Spaceship parts. It also allows you to build the Missile Cruiser, a Naval Unit capable of carrying 3 Missiles and spotting enemy Submarines.
        Completing it would unlock: Nanotechnology, Particle Physics
      - The Internet: Increases Tourism output of all cities by 50%, helping you advance toward a Cultural Victory.
        Completing it would unlock: Nanotechnology, Particle Physics, Globalization
      
      ## Policies
      - Socialist Realism (Level 3 Tenet of Ideology Order): Socialist Realism: Unlocks the Propaganda Process (converts 15% of Production into Tourism). +25% Tourism to other Civilizations following Order. +4 Production from all Great Works.
      - Iron Curtain (Level 3 Tenet of Ideology Order): Iron Curtain: Free Courthouse upon immediate City annexation. +200% Food or Production from Internal Trade Routes. City connections generate +5 Gold and Production.
      - Communism (Level 1 Tenet of Ideology Order): Communism: Gold cost of investing in buildings reduced by 25%. +20% Production when building Wonders.
      - Hero of the People (Level 1 Tenet of Ideology Order): Hero of the People: Great Person rate increases by 25%. A Great Person of your choice appears near your Capital.
      - Double Agents (Level 1 Tenet of Ideology Order): Double Agents: Receive 200 Spy Points. Gain 125 Science when you identify a foreign Spy, scaling with Era.
      - Ceremony (Continuing Tradition Branch):
        - * +1 Happiness from National Wonders with Building requirements.
        - * +25% Production toward National Wonders with Building requirements.
        - * Royal Astrologer built in Capital (+3 Science, +1 Science to all Councils, Smokehouses, and Herbalists; 1 Scientist Slot).
      - Liberty (Continuing Progress Branch):
        - * +2 Gold in every City.
        - * +25% Tile improvement rate.
        - * A Worker appears near the Capital.
      - Nobility (Continuing Fealty Branch):
        - * +1 Happiness and +2 Gold from Castles.
        - * +2 Gold from Armories.
        - * +100% Production towards Castles and Armories.
      - Trade Confederacy (Continuing Statecraft Branch):
        - * +25% Yields for International Trade Routes.
        - * Trade Routes to City-States generate +1 Influence per turn (with the target City-State) per each owned City-State Trade Route (up to +5).
      - Organization (Continuing Progress Branch):
        - * +2 Production in every City.
        - * +25% Production toward Workers and Trade Units.
        - * +1 Movement for Workers.
      - Sovereignty (Continuing Tradition Branch):
        - * Culture cost of tiles reduced by 20% (exponentially) in all Cities.
        - * Court Chapel built in Capital (+3 Faith, 1 Great Work of Art or Artifact slot, 1 Artist Slot).
      - Refinement (Continuing Artistry Branch):
        - * +2 Culture from Great Works of Art.
        - * 1 Specialist in all cities does not produce Unhappiness from Urbanization.
        - * +1 Culture from Specialists.
      - Foreign Service (Continuing Statecraft Branch):
        - * Receive 100 Spy Points.
        - * Earn Great Diplomats 50% faster.
        - * +50% Rewards from City-State Quests.
        - * +1 of every Strategic Resource for every three City-State Alliances you maintain.
      - Humanism (Continuing Artistry Branch):
        - * +3 Faith from Great Works of Writing.
        - * -25% Golden Age Points needed to trigger a Golden Age.
        - * +1 Happiness from all Guilds.
      - Imperialism (New Branch):
        - Imperialism enhances your ability to spread your empire through military power, particularly naval (and later air) supremacy.
        - Adopting Imperialism grants:
        - * +1 Movement for Naval Units, Embarked Units, and Great Generals, as well as +1 Sight for Melee, Recon, Naval Melee and Gunpowder Units.
        - * +10% Production toward Military Units, -10% Gold required for upgrades.
        - Each Imperialism policy unlocked grants:
        - * +5% Production for Military Units, -5% Gold required for upgrades.
        - Adopting all policies in Imperialism grants:
        - * Unlocks building the Pentagon.
        - * All Naval and Air units gain the Banzai! Promotion (become stronger as they take damage).
        - * Allows for the purchase of Great Admirals with Faith starting in the Industrial Era.
      - Industry (New Branch):
        - Industry provides bonuses to empires focused on Gold and Production.
        - Adopting Industry grants:
        - * +2 Trade Routes.
        - * -5% Gold needed for purchases.
        - Each Industry policy unlocked grants:
        - * -5% Gold needed for purchases.
        - Adopting all Policies in Industry grants:
        - * Unlocks building Broadway.
        - * +3 Happiness per unique owned Luxury Resource.
        - * +2 Production and Gold from Specialists.
        - * Allows for the purchase of Great Merchants with Faith starting in the Industrial Era.
  - messages:
    - #0:
      - role: user
      - content: # Strategies
        Strategies: existing strategic decisions from you.
        
        ## Persona
        - VictoryCompetitiveness: 10
        - WonderCompetitiveness: 1
        - MinorCivCompetitiveness: 1
        - Boldness: 10
        - WarBias: 6
        - HostileBias: 10
        - WarmongerHate: 1
        - NeutralBias: 1
        - FriendlyBias: 1
        - GuardedBias: 10
        - AfraidBias: 1
        - DiplomaticBalance: 9
        - Friendliness: 1
        - WorkWithWillingness: 1
        - WorkAgainstWillingness: 10
        - Loyalty: 1
        - MinorCivFriendlyBias: 1
        - MinorCivNeutralBias: 1
        - MinorCivHostileBias: 10
        - MinorCivWarBias: 10
        - DenounceWillingness: 10
        - Forgiveness: 1
        - Meanness: 10
        - Neediness: 1
        - Chattiness: 1
        - DeceptiveBias: 1
        - Rationale: Tweaked by In-Game AI (TURN 437: Increasing DiplomaticBalance from 1 to 8 and reducing WarBias from 10 to 6. The previous 'total war' persona with DiplomaticBalance 1 caused Assyria to declare war on The Inca (turn 437, event 22), which is strategically catastrophic as it helps Austria win the diplomatic victory. The Inca are the only civilization capable of capturing Attila's Court and removing Austria's 10 vassal delegates before World Congress in 5 turns. Higher DiplomaticBalance allows for peace negotiations to end this counterproductive war immediately when possible, while lower WarBias reduces aggressive war declarations. Maintained Boldness 10 for decisive action against Austria once The Inca secures Attila's Court.)
        
        ## Technology
        - Next: Robotics
        - Rationale: Setting next research to Robotics after Alternative Energy completes. Robotics unlocks the Spaceship Factory (+50% production to spaceship parts) which also provides general production benefits, and the Missile Cruiser (naval unit with 3 missile capacity and submarine detection). While the immediate crisis is diplomatic/naval, if The Inca captures Attila's Court and prevents Austrian victory in 6 turns, Assyria will need maximum production capacity for the subsequent space race or continued conquest. Robotics also leads to Nanotechnology and Particle Physics (end-game technologies). Given the 7-turn research time for Alternative Energy, this decision prepares for the post-crisis scenario where production supremacy will determine the final victor.
        
        ## Policy
        - Next: Iron Curtain (Policy)
        - Rationale: Adopting Iron Curtain (Order Level 3 Tenet) provides critical war economy bonuses: free courthouse upon immediate city annexation (essential for rapid integration of captured Austrian territory without happiness collapse), +200% Food/Production from internal trade routes (maximizes war production from existing cities), and +5 Gold/Production from city connections. With World Congress in 6 turns, if The Inca succeeds in capturing Attila's Court and preventing Austrian victory, Assyria must be prepared to immediately annex and integrate any captured Austrian cities to maintain momentum. The courthouse bonus eliminates the need to wait for construction, while the internal trade route multiplier maximizes resource extraction for the final push against Austria.
        
        ## Relationships
        
        ### Argos
        - Public: 50
        - Private: 45
        - Rationale: Reducing Argos relationship from 60/55 to 50/45. With 70 influence at Friends and Ethiopia (my vassal) as the ally at 141 influence, Argos alliance is not attainable in the short term. Moderate positive relationship maintains friendly status and potential for future quest completion, without over-investing diplomatic capital. Focus resources on maintaining Sokoto, Nippur, and Okilis alliances.
        - UpdatedTurn: 221
        
        ### Manila
        - Public: 65
        - Private: 60
        - Rationale: Reducing Brussels relationship from 85/80 to 65/60. Tourism quest completes in 5 turns but Poland leads 153 vs 65 tourism - they will win the 151 influence reward and cement their alliance. Poland is current ally at 161, making Brussels alliance unattainable. Moderate positive relationship maintains friendly status with +20 resting influence from shared Eastern Orthodoxy, but reflects realistic assessment that immediate breakthrough unlikely. Resources better focused on Dublin technology quest (12 turns) and maintaining Sokoto/Nippur/Okilis alliances.
        - UpdatedTurn: 223
        
        ### Dublin
        - Public: 80
        - Private: 75
        - Rationale: Reducing Dublin from 90/85 to 80/75. Poland has overwhelming 334 influence and will likely complete windmill quest. Alliance unlikely but maintaining positive relationship for quest completion if opportunity arises. Moderate investment reflects realistic assessment.
        - UpdatedTurn: 258
        
        ### Sokoto
        - Public: -20
        - Private: -30
        - Rationale: Adjusting Sokoto to negative relationship (-20/-30). Austria now controls Sokoto with overwhelming 593 influence vs my 143. The alliance is definitively lost and unrecoverable in the short term. Austria will likely use this delegate against me at World Congress. Negative relationship reflects reality that Sokoto is now hostile territory under Austrian control.
        - UpdatedTurn: 272
        
        ### Nippur
        - Public: 80
        - Private: 75
        - Rationale: Increasing Nippur relationship to 80/75. Just achieved Friends status (58 influence) with successful election rigging. Positioned near my territory and shares Eastern Orthodoxy (+20 resting influence). With proper investment and quest completion, alliance is achievable in the medium term. Critical for rebuilding delegate count after Sokoto loss.
        - UpdatedTurn: 274
        
        ### Okilis
        - Public: 95
        - Private: 90
        - Rationale: Increasing Okilis relationship to 95/90 after losing Nippur to Austria's Great Diplomat (dropped from 57 to -60). Okilis at 219 influence is my best chance for a second delegate before World Congress in 4 turns. A destroy barbarian encampment quest offers 75 influence reward which would push me to Alliance threshold.
        - UpdatedTurn: 277
        
        ### Palatium
        - Public: 85
        - Private: 80
        - Rationale: Palatium at Friends (81 influence) shares my Eastern Orthodoxy (+20 resting influence). Morocco is ally at 599, making alliance unlikely short-term. However, Palatium does not border Austria directly, making it more secure. High relationship maintains position for potential future breakthrough if Morocco's influence decays or Austria attacks them.
        - UpdatedTurn: 287
        
        ### Brussels
        - Public: -70
        - Private: -75
        - Rationale: Brussels just became hostile (dropped from 68 influence to -60) and is now at war with me with Peace Currently Blocked. This is a massive diplomatic setback - I've lost my second city-state delegate and now only have 5 delegates (Sydney) vs Austria's 29 going into World Congress in 9 turns. The relationship must reflect this new hostile reality. Setting to -70/-75 reflects active enemy status while leaving room for potential future reconciliation if I can complete quests or use Great Diplomats to recover influence. For now, Brussels is effectively Austrian-controlled hostile territory and I must focus all diplomatic resources on maintaining Sydney as my sole remaining delegate source.
        - UpdatedTurn: 304
        
        ### Sydney
        - Public: -20
        - Private: -25
        - Rationale: Setting Sydney to -20/-25. Indonesia used Great Diplomat to steal Sydney (dropping my influence from 271 to 33), making Indonesia the new ally. While I'm technically still Friends with 33 influence, Sydney is now effectively controlled by my enemy's vassal and will vote against me at World Congress in 5 turns. This negative relationship reflects the loss of my only city-state delegate and the new hostile reality.
        - UpdatedTurn: 307
        
        ### Tyre
        - Public: -80
        - Private: -85
        - Rationale: Tyre was my last city-state ally but is now at war with me (influence dropped to -60). Austria has stolen this critical alliance using Great Diplomat. Setting to -80/-85 reflects this major diplomatic defeat - I've lost my +1 delegate and now face another hostile city-state bordering my territory. Tyre will vote against me and may attack. Cannot recover this alliance.
        - UpdatedTurn: 373
        
        ### Ethiopia
        - Public: 100
        - Private: 95
        - Rationale: Ethiopia at 100% war score with both capitals captured. Maximizing relationship to signal AI to push for immediate peace treaty and vassalization before the game ends. This provides additional score and formally ends the war.
        - UpdatedTurn: 381
        
        ### Indonesia
        - Public: -60
        - Private: -65
        - Rationale: Indonesia is Inca's vassal and our peace treaty has expired. Their 6 delegates and 899 military strength pose a threat of opening a second front while I focus on Austria. Setting to -60/-65 reflects this hostile reality and prepares AI for defensive positioning if they declare war.
        - UpdatedTurn: 411
        
        ### The Inca
        - Public: 100
        - Private: 100
        - Rationale: Maximum relationship with The Inca maintained at 100/100. They are the only civilization positioned to capture Attila's Court (at 4,47) and potentially disrupt Austria's vassal relationship with The Huns. Their 27,612 military strength versus The Huns' 3,177 should be sufficient. Maximum relationship encourages The Inca to prioritize this critical objective over all others.
        - UpdatedTurn: 432
        
        ### Austria
        - Public: -100
        - Private: -100
        - Rationale: Maximum hostility toward Austria maintained at -100/-100. They have 41/40 delegates needed for diplomatic victory and will win in 10 turns at World Congress if not stopped. They are the ultimate enemy. Total war posture maintained with no diplomatic engagement possible.
        - UpdatedTurn: 432
        
        ### The Huns
        - Public: -100
        - Private: -100
        - Rationale: Maximum hostility toward The Huns maintained at -100/-100. Attila's Court is the critical objective - capturing it may disrupt Austria's vassal relationship and delegate count. The Huns' 3,177 military strength versus The Inca's 27,612 suggests they should fall quickly if The Inca commits fully. Maximum hostility ensures all military assets prioritize operations against The Huns.
        - UpdatedTurn: 432
        
        ### Poland
        - Public: 100
        - Private: 100
        - Rationale: Maximum relationship with Poland maintained at 100/100. They have 8 delegates and their peace treaty with Austria expires soon. Keeping them friendly ensures they remain in the anti-Austrian bloc and don't provide the final votes Austria needs at World Congress. Their delegate support is critical for post-World Congress containment if Austria fails to achieve victory.
        - UpdatedTurn: 432
        
        ### Morocco
        - Public: 100
        - Private: 95
        - Rationale: Maximum relationship with Morocco maintained at 100/95. They are my defensive pact ally with 10 delegates. Their delegate bloc provides critical counterweight to Austria's 41. Morocco's continued hostility toward Austria (they have denounced them) helps block Austrian diplomatic victory even if military operations are limited.
        - UpdatedTurn: 432
        
        ## Strategy
        - Rationale: TURN 437: EMERGENCY CORRECTION. Reduced Offense from 100 to 20 and Mobile from 100 to 20 to immediately halt the counterproductive steamroll against The Inca in zones 8814 and 12172. The aggressive total war posture was diverting The Inca's military strength (26,880) away from capturing Attila's Court from The Huns. With World Congress in 5 turns, The Inca MUST capture Attila's Court to remove Austria's 10 vassal delegates and prevent their diplomatic victory. By switching to defensive posture (Defense 80), Assyria will stop killing Inca units and allow them to focus on The Huns. Maintained maximum Production (100), Air (100), and Nuke (100) for the Austrian front. This is a critical strategic pivot - every Inca unit lost to Assyria is one less unit pressuring The Huns' capital.
        - GrandStrategy: Conquest
        
        ### Flavors
        - Offense: 20
        - Defense: 80
        - Mobilization: 100
        - CityDefense: 30
        - MilitaryTraining: 90
        - Recon: 10
        - Ranged: 95
        - Mobile: 20
        - Nuke: 100
        - UseNuke: 95
        - Naval: 90
        - NavalRecon: 70
        - NavalGrowth: 40
        - NavalTileImprovement: 35
        - Air: 100
        - AirCarrier: 80
        - Antiair: 60
        - Airlift: 100
        - Expansion: 0
        - Growth: 40
        - TileImprovement: 20
        - Infrastructure: 30
        - Production: 100
        - WaterConnection: 30
        - Gold: 30
        - Science: 50
        - Culture: 0
        - Happiness: 30
        - GreatPeople: 50
        - Wonder: 0
        - Religion: 0
        - Diplomacy: 0
        - Spaceship: 0
        - Espionage: 80
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: The Inca
        - Assyria:
          - CapitalsControlled:
            - Addis Ababa
            - Assur
          - CapitalsPercentage: 25
        - Austria:
          - CapitalsControlled:
            - Vienna
            - Attila's Court
          - CapitalsPercentage: 25
        - The Inca:
          - CapitalsControlled:
            - Cusco
            - Jakarta
          - CapitalsPercentage: 25
        
        ## ScienceVictory
        - Assyria:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        - Austria:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        - Indonesia:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Morocco:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        - Poland:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - The Huns:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - The Inca:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        
        ## CulturalVictory
        - CivsNeeded: 6
        - Contender: Poland
        - Assyria:
          - Influences:
            - Austria: Familiar (38%) - Rising Slowly (tourism/culture ratio 72%)
            - The Inca: Familiar (38%) - Rising Slowly (tourism/culture ratio 83%)
            - The Huns: Influential (104%) - Rising (tourism/culture ratio 231%)
            - Indonesia: Popular (92%) - Rising (6 turns to Influential, tourism/culture ratio 792%)
            - Morocco: Popular (85%) - Rising (25 turns to Influential, tourism/culture ratio 206%)
            - Poland: Familiar (37%) - Rising Slowly (tourism/culture ratio 112%)
          - PolicyPercentage: 100
          - InfluentialCivs: 1
        - Austria:
          - Influences:
            - The Inca: Popular (93%) - Rising (8 turns to Influential, tourism/culture ratio 236%)
            - Assyria: Influential (100%) - Rising (tourism/culture ratio 445%)
            - The Huns: Dominant (427%) - Rising (tourism/culture ratio 1401%)
            - Indonesia: Influential (185%) - Rising (tourism/culture ratio 1674%)
            - Morocco: Influential (108%) - Rising (tourism/culture ratio 399%)
            - Poland: Popular (58%) - Rising (66 turns to Influential, tourism/culture ratio 244%)
          - PolicyPercentage: 100
          - InfluentialCivs: 4
        - Indonesia:
          - Influences:
            - Austria: Exotic (7%) - Rising Slowly (tourism/culture ratio 5%)
            - Assyria: Exotic (10%) - Rising Slowly (tourism/culture ratio 19%)
            - The Inca: Exotic (11%) - Rising Slowly (tourism/culture ratio 10%)
            - The Huns: Exotic (24%) - Rising Slowly (tourism/culture ratio 29%)
            - Morocco: Exotic (16%) - Rising Slowly (tourism/culture ratio 21%)
            - Poland: Exotic (7%) - Rising Slowly (tourism/culture ratio 11%)
          - PolicyPercentage: 92
          - InfluentialCivs: 0
        - Morocco:
          - Influences:
            - Austria: Exotic (24%) - Rising Slowly (tourism/culture ratio 46%)
            - Assyria: Familiar (44%) - Rising (570 turns to Influential, tourism/culture ratio 137%)
            - The Inca: Familiar (28%) - Rising Slowly (tourism/culture ratio 55%)
            - Indonesia: Popular (88%) - Rising (11 turns to Influential, tourism/culture ratio 712%)
            - The Huns: Popular (86%) - Rising (20 turns to Influential, tourism/culture ratio 231%)
            - Poland: Familiar (31%) - Rising Slowly (tourism/culture ratio 88%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Poland:
          - Influences:
            - Austria: Popular (86%) - Rising (30 turns to Influential, tourism/culture ratio 166%)
            - Assyria: Influential (157%) - Rising (tourism/culture ratio 504%)
            - The Huns: Dominant (318%) - Rising (tourism/culture ratio 776%)
            - Indonesia: Dominant (308%) - Rising (tourism/culture ratio 2688%)
            - Morocco: Dominant (221%) - Rising (tourism/culture ratio 489%)
            - The Inca: Influential (116%) - Rising (tourism/culture ratio 252%)
          - PolicyPercentage: 100
          - InfluentialCivs: 5
        - The Huns:
          - Influences:
            - Austria: Exotic (10%) - Rising Slowly (tourism/culture ratio 22%)
            - Assyria: Exotic (9%) - Rising Slowly (tourism/culture ratio 35%)
            - The Inca: Exotic (8%) - Rising Slowly (tourism/culture ratio 18%)
            - Indonesia: Exotic (23%) - Rising (508 turns to Influential, tourism/culture ratio 203%)
            - Morocco: Exotic (13%) - Rising Slowly (tourism/culture ratio 42%)
            - Poland: Exotic (7%) - Rising Slowly (tourism/culture ratio 26%)
          - PolicyPercentage: 96
          - InfluentialCivs: 0
        - The Inca:
          - Influences:
            - Austria: Familiar (49%) - Rising Slowly (tourism/culture ratio 109%)
            - Assyria: Popular (68%) - Rising (27 turns to Influential, tourism/culture ratio 342%)
            - The Huns: Influential (111%) - Rising (tourism/culture ratio 331%)
            - Indonesia: Dominant (201%) - Rising (tourism/culture ratio 2338%)
            - Morocco: Popular (68%) - Rising (38 turns to Influential, tourism/culture ratio 237%)
            - Poland: Familiar (35%) - Rising (480 turns to Influential, tourism/culture ratio 144%)
          - PolicyPercentage: 100
          - InfluentialCivs: 2
        
        ## DiplomaticVictory
        - VotesNeeded: 40
        - Status: World Congress - Voting in 4 turns
        - ActiveResolutions:
          - Casus Belli:
            - Description: The world recognizes the need for justifiable war to resolve diplomatic disputes.
              While this resolution is active, unit maintenance costs are lowered by 15% Gold. 0.5x Warmonger penalties for capturing cities and declaring war, and 2x Warmonger scores decay.
            - EnactedOn: -1
          - Natural Heritage Sites:
            - Description: Each Natural Wonder provides +2 to all Yields when worked.
            - EnactedOn: -1
          - World Ideology: Autocracy:
            - Description: Designate an Ideology as the official World Ideology. Civilizations following the Ideology get an additional Delegate, plus 1 Delegate for every other Civilization that follows the Ideology. Public opinion in favor of that Ideology is increased for all Civilizations. Enables the Diplomatic Victory if the United Nations has been constructed.
              Available once any Civilization discovers Nuclear Fission.
            - EnactedOn: -1
          - Sanction: Poland:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: -1
          - Endowment for the Arts:
            - Description: Increases up to 33% generation of Great Writers, Artists, and Musicians. Decreases up to 33% generation of Great Scientists, Engineers, and Merchants.
              Civilizations with Scores from Policies and Great Works below the global median will receive a boost to Production and Culture up to 33%.
              Details: The boosts are proportional to the difference between the score of the Civilization and the leader.
            - EnactedOn: -1
          - Passport System:
            - Description: Increases international travel between Civilizations. Increases the Tourism modifier for all Civilizations by 50%.
              Available once any Civilization discovers Flight.
            - EnactedOn: -1
          - Moroccan Sphere of Influence: Palatium:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Scholars In Residence:
            - Description: Civilizations have -20% Research cost for Technologies already discovered by another Civilization. Additional -2% for every City-State Ally, up to -50%.
            - EnactedOn: -1
          - Sanction: The Inca:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: -1
          - Austrian Sphere of Influence: Okilis:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Austrian Sphere of Influence: Manila:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 431
          - World Religion: Buddhism:
            - Description: Designate a religion as the official World Religion. Civilizations who have a majority of the cities in their empire following the religion get an additional Delegate. The founder of the religion and/or the controller of its Holy City receives additional votes based on the number of Civilizations following the religion. The religion spreads 25% faster, and its Holy City receives +50% Tourism. There can only be one World Religion at a time.
            - EnactedOn: -1
        - Proposals:
          - Enact: Global Hegemony:
            - Description: Designate a player that could achieve Global Hegemony. If a Civilization receives support from enough Delegates in the Congress, that leader will attain Diplomatic Victory. The number of Delegates needed depends on the number of Civilizations and City-States in the game, and can be seen on the World Congress screen.
              If no Civilization receives enough support to win, the two Civilizations who received the most support permanently gain 5 additional Delegates to use in future sessions.
              May not be proposed by a Civilization. Automatically proposed at regular intervals once a World Ideology Resolution is active.
            - Proposer: Unknown
        - Contender: Austria
        - Assyria:
          - Delegates: 4
          - VictoryPercentage: 10
        - Austria:
          - Delegates: 45
          - VictoryPercentage: 112
        - Indonesia:
          - Delegates: 6
          - VictoryPercentage: 15
        - Morocco:
          - Delegates: 10
          - VictoryPercentage: 25
        - Poland:
          - Delegates: 10
          - VictoryPercentage: 25
        - The Huns:
          - Delegates: 8
          - VictoryPercentage: 20
        - The Inca:
          - Delegates: 11
          - VictoryPercentage: 27
        
        # Players
        Players: summary reports about visible players in the world.
        
        ## Player 0
        - Civilization: The Inca
        - Leader: Pachacuti
        - IsMajor: true
        - OurOpinionOfThem:
          - You (The Inca) have both chosen to adopt the Order Ideology. (999)
          - Assyria's leader has expressed a public opinion of The Inca (100).
          - Assyria's leader has formed a private opinion of The Inca (100).
          - We fought together against a common foe. (99)
          - You (The Inca) have denounced one of Assyria's declared enemies! (11)
          - Assyria's real approach to The Inca is Hostile.
          - We have divergent Social Policies. (-3)
          - You (The Inca) have denounced a leader Assyria made a Declaration of Friendship with! (-11)
          - You (The Inca) have made a Declaration of Friendship with one of Assyria's enemies! (-13)
          - Religious differences strain your (The Inca) relationship. (-30)
          - Your (The Inca) spies were caught stealing from Assyria. (-33)
          - Assyria are spreading Assyria's own religion, but you (The Inca) converted some of their cities to your (The Inca) religion. (-78)
          - You (The Inca) are at war! (-99999)
        - TheirOpinionOfUs:
          - You (Assyria) have both chosen to adopt the Order Ideology.
          - Your (Assyria) votes supported The Inca's civ's interests in the United Nations.
          - You (Assyria) have denounced one of The Inca's declared enemies!
          - The Inca fear your (Assyria) warmongering will end this world in fire! (They dislike warmongers.)
          - We have divergent Social Policies.
          - Religious differences strain your (Assyria) relationship.
          - You (Assyria) are competing for World Wonders.
          - You (Assyria) have made a Declaration of Friendship with one of The Inca's enemies!
          - We defeated The Inca's proposal in the United Nations.
          - The Inca are jealous of our superior technology!
          - Territorial disputes strain your (Assyria) relationship.
          - Your (Assyria) spies were caught stealing from The Inca.
          - We have denounced each other!
          - You (Assyria) stole The Inca's territory while at peace!
          - The Inca know you (Assyria) are competing with The Inca, and The Inca hate it!
          - You (Assyria) are at war!
        - Score: 3774
        - Era: Information
        - GoldenAge: 9 turns remaining
        - Technologies: 73
        - Cities: 20
        - Population: 598
        - Territory: 654
        - Gold: 3135
        - GoldPerTurn: 656
        - HappinessSituation: Happy
        - HappinessPercentage: 55
        - MilitaryStrength: 26694
        - TourismPerTurn: 1398
        - CulturePerTurn: 3682
        - PolicyBranches:
          - Fealty: 6
          - Order: 8
          - Progress: 6
          - Rationalism: 6
        - ResourcesAvailable:
          - Wheat: 5
          - Silver: 1
          - Sheep: 8
          - Cloves: 4
          - Ivory: 1
          - Nutmeg: 5
          - Paper: 9
          - Pearls: 2
          - Maize: 4
          - Rice: 1
          - Salt: 8
          - Aluminum: 15
          - Fish: 19
          - Perfume: 2
          - Deer: 4
          - Jade: 9
          - Iron: -2
          - Dyes: 1
          - Cattle: 4
          - Pepper: 2
          - Horses: -2
          - Coral: 2
          - Bison: 4
          - Citrus: 1
          - Truffles: 2
          - Stone: 5
          - Marble: 1
          - Bananas: 1
          - Oil: 1
          - Wine: 3
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - War (Our Score: -2%; Our War Weariness: 26%)
            - Denounced Them
          - Assyria:
            - Distance: Neighbors
            - War (Our Score: 0%; Our War Weariness: 1%)
            - Denounced Them
          - The Huns:
            - Distance: Far
            - War (Our Score: 14%; Our War Weariness: 45%)
            - Denounced Them
          - Indonesia:
            - Distance: Close
            - Our Vassal (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Morocco:
            - Distance: Close
            - Denounced Them
          - Poland:
            - Distance: Far
            - Denounced Them
        - Votes: 11
        - 1: Defeated Major Civilization Ethiopia
        
        ## Player 2
        - Civilization: Assyria
        - Leader: Ashurbanipal
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: Poland, Our top defensive pact ally: None
          - Our top United Nations ally: None, Our top United Nations rival: Austria
          - Our top Competitor: The Inca
        - Score: 3197
        - Era: Information
        - GoldenAge: Estimated in 27 turns
        - Technologies: 75
        - CurrentResearch: Alternative Energy (Estimated in 5 turns)
        - NextPolicyTurns: 29
        - Cities: 17
        - Population: 406
        - Territory: 540
        - BestSettlementLocation:
          - 47, 18 (Quality: 57%; 5 tiles from us)
          - 47, 17 (Quality: 60%; 6 tiles from us)
          - 48, 17 (Quality: 50%; 5 tiles from us)
          - 47, 35 (Quality: 37%; 5 tiles from us; New Continent)
          - 47, 19 (Quality: 0%; 4 tiles from us)
        - Gold: 998
        - GoldPerTurn: 439
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 49
        - MilitaryUnits: 65
        - MilitarySupply: 65
        - MilitaryStrength: 10509
        - TourismPerTurn: 902.25
        - CulturePerTurn: 1795
        - FaithPerTurn: 557
        - SciencePerTurn: 3342
        - PolicyBranches:
          - Fealty:
            - Fealty
          - Order:
            - People's Army
            - Patriotic War
            - Academy of Sciences
            - Dictatorship of the Proletariat
            - Workers' Faculties
            - Five-Year Plan
            - Spaceflight Pioneers
            - Peace, Land, Bread
          - Tradition:
            - Tradition
            - Justice
          - Artistry:
            - Artistry
          - Progress:
            - Progress
          - Rationalism:
            - Rationalism
            - Scientific Revolution
            - Enlightenment
            - Free Thought
            - Rights of Man
            - Empiricism
          - Statecraft:
            - Statecraft
          - Authority:
            - Authority
            - Tribute
            - Imperium
            - Militarism
            - Dominance
            - Honor
        - ResourcesAvailable:
          - Wheat: 0
          - Silver: 0
          - Sheep: 7
          - Cloves: 0
          - Figs: 0
          - Ivory: 1
          - Gold: 0
          - Nutmeg: 0
          - Paper: 6
          - Pearls: 0
          - Maize: 3
          - Rice: 6
          - Cotton: 0
          - Gems: 1
          - Salt: 0
          - Brazilwood: 0
          - Aluminum: 13
          - Glass: 0
          - Lapis Lazuli: 0
          - Fish: 22
          - Amber: 0
          - Perfume: 0
          - Deer: 6
          - Whales: 0
          - Olives: 0
          - Sugar: 0
          - Jade: 0
          - Iron: 7
          - Dyes: 0
          - Tea: 0
          - Coal: 2
          - Coffee: 0
          - Cattle: 3
          - Pepper: 0
          - Uranium: 5
          - Horses: 16
          - Coral: 2
          - Silk: 0
          - Jewelry: 0
          - Bison: 4
          - Antiquity Site: 0
          - Citrus: 1
          - Copper: 2
          - Truffles: 0
          - Crab: 3
          - Incense: 1
          - Stone: 4
          - Marble: 2
          - Furs: 0
          - Cinnamon: 4
          - Bananas: 4
          - Oil: 6
          - Wine: 1
          - Porcelain: 0
          - Cocoa: 7
          - Tobacco: 0
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Austria:
            - Distance: Close
            - War (Our Score: 8%; Our War Weariness: 50%)
            - Denounced Them
          - The Inca:
            - Distance: Neighbors
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
          - The Huns:
            - Distance: Far
            - War (Our Score: 12%; Our War Weariness: 84%)
          - Indonesia:
            - Distance: Neighbors
            - War (Our Score: 0%; Our War Weariness: 0%)
          - Morocco:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - Poland:
            - Distance: Close
            - Declaration of Friendship
        - OutgoingTradeRoutes:
          - Halab (Assyria) => Marrakech (Morocco):
            - ToGold: 13.75
            - TurnsLeft: 18
            - FromScience: 6
            - Domain: Sea
            - FromGold: 55.06
            - ToCulture: 2
            - ToScience: 3
          - Brussels (Assyria) => Bahir Dar (Morocco):
            - ToGold: 7
            - TurnsLeft: 23
            - FromScience: 6
            - Domain: Land
            - FromGold: 33.35
            - ToCulture: 2
            - ToScience: 3
          - Kar-Tukulti-Ninurta (Assyria) => Nippur (Assyria):
            - ToFood: 43.35
            - TurnsLeft: 19
            - Domain: Land
          - Assur (Assyria) => Fes (Morocco):
            - ToGold: 8.75
            - TurnsLeft: 19
            - FromScience: 6
            - Domain: Sea
            - FromGold: 53.91
            - ToCulture: 2
            - ToScience: 3
          - Gondar (Assyria) => Tangier (Morocco):
            - ToGold: 8.75
            - TurnsLeft: 8
            - FromScience: 6
            - Domain: Sea
            - FromGold: 38.82
            - ToCulture: 2
            - ToScience: 3
          - Harar (Assyria) => Casablanca (Morocco):
            - ToGold: 8.75
            - TurnsLeft: 4
            - FromScience: 6
            - Domain: Sea
            - FromGold: 39.52
            - ToCulture: 2
            - ToScience: 3
          - Nineveh (Assyria) => Argos (Assyria):
            - ToFood: 57.81
            - TurnsLeft: 22
            - Domain: Sea
          - Halab (Assyria) => Rabat (Morocco):
            - ToGold: 8.75
            - TurnsLeft: 12
            - FromScience: 6
            - Domain: Sea
            - FromGold: 42.66
            - ToCulture: 2
            - ToScience: 3
          - Addis Ababa (Assyria) => Nimrud (Assyria):
            - TurnsLeft: 18
            - Domain: Land
            - ToProduction: 25
          - Gondar (Assyria) => Sale (Morocco):
            - ToGold: 8.75
            - TurnsLeft: 16
            - FromScience: 6
            - Domain: Sea
            - FromGold: 37.57
            - ToCulture: 2
            - ToScience: 3
          - Available: 2
        - IncomingTradeRoutes:
          - Marrakech (Morocco) => Brussels (Assyria):
            - ToGold: 9
            - TurnsLeft: 9
            - FromScience: 31.25
            - Domain: Land
            - FromGold: 57.52
            - FromCulture: 17.5
          - Marrakech (Morocco) => Harar (Assyria):
            - ToGold: 11.25
            - TurnsLeft: 18
            - FromScience: 31.25
            - Domain: Sea
            - FromGold: 61.09
            - FromCulture: 17.5
        - Spies:
          - Agent Qingu (7):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 1160
            - Location: Salzburg (Austria)
            - NetworkPerTurn: 40
          - Agent Nukimmut (8):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 1129
            - Location: Andahuaylas (The Huns)
            - NetworkPerTurn: 59
          - Agent Naramsin (6):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 1292
            - Location: Vienna (Austria)
            - NetworkPerTurn: 39
          - Agent Asnappar (3):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 240
            - Location: Kaunas (Austria)
            - NetworkPerTurn: 40
          - Agent Seruya (9):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 400
            - Location: Sabata (Austria)
            - NetworkPerTurn: 40
          - Agent Lamashtu (4):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 1900
            - Location: Mataram (Indonesia)
            - NetworkPerTurn: 50
          - Agent Samano (0):
            - State: Counter-intelligence
            - Role: Counterspy
            - Location: Assur (Assyria)
            - NetworkPerTurn: 0
          - Agent Izdubar (11):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 1468
            - Location: Samarinda (Indonesia)
            - NetworkPerTurn: 44
          - Agent Erishum (5):
            - State: Traveling
            - Role: Spy
            - Location: Attila's Court (The Huns)
            - NetworkPerTurn: 0
          - Agent Bilit (10):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 320
            - Location: Kitzbuhel (Austria)
            - NetworkPerTurn: 40
          - Agent Pazuzu (2):
            - State: Traveling
            - Role: Spy
            - Location: Sodo (The Huns)
            - NetworkPerTurn: 0
        - DiplomaticDeals:
          - Morocco:
            - #0:
              - WeGive:
                - 28 Gold per Turn
              - TheyGive:
                - 1 Citrus
              - TurnsRemaining: 7
            - #1:
              - WeGive:
                - 1 Iron
              - TheyGive:
                - 24 Gold per Turn
              - TurnsRemaining: 7
            - #2:
              - WeGive:
                - 28 Gold per Turn
              - TheyGive:
                - 1 Gems
              - TurnsRemaining: 12
            - #3:
              - WeGive:
                - 1 Wine
              - TheyGive:
                - 26 Gold per Turn
              - TurnsRemaining: 14
            - #4:
              - WeGive:
                - Open Borders
              - TheyGive:
                - Open Borders
                - 1 Gold per Turn
              - TurnsRemaining: 20
            - #5:
              - WeGive:
                - 1 Cocoa
              - TheyGive:
                - 27 Gold per Turn
              - TurnsRemaining: 24
            - #6:
              - WeGive:
                - 3 Iron
              - TheyGive:
                - 23 Gold per Turn
              - TurnsRemaining: 27
            - #7:
              - WeGive:
                - 30 Gold per Turn
              - TheyGive:
                - 1 Incense
              - TurnsRemaining: 38
            - #8:
              - WeGive:
                - 1 Coral
              - TheyGive:
                - 8 Gold per Turn
              - TurnsRemaining: 44
            - #9:
              - WeGive:
                - 1 Marble
              - TheyGive:
                - 8 Gold per Turn
              - TurnsRemaining: 45
            - #10:
              - WeGive:
                - 1 Cinnamon
              - TheyGive:
                - 8 Gold per Turn
              - TurnsRemaining: 47
        - Votes: 4
        
        ## Player 3
        - Civilization: Morocco
        - Leader: Ahmad al-Mansur
        - IsMajor: true
        - OurOpinionOfThem:
          - Assyria's leader has expressed a public opinion of Morocco (100).
          - Assyria's leader has formed a private opinion of Morocco (95).
          - We are trade partners. (40)
          - We have opened our borders to each other. (12)
          - You (Morocco) have denounced one of Assyria's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have similar Social Policies. (3)
          - We have shared embassies. (1)
          - Assyria's real approach to Morocco is Friendly.
          - You (Morocco) have made a Declaration of Friendship with one of Assyria's enemies! (-13)
          - Religious differences strain your (Morocco) relationship. (-30)
          - You (Morocco) have chosen to adopt the Autocracy Ideology, but Assyria believe in Order. (-999)
        - TheirOpinionOfUs:
          - Your (Assyria) votes supported Morocco's civ's interests in the United Nations.
          - We passed Morocco's proposal in the United Nations.
          - Morocco's leader has expressed a public opinion of you (Assyria) (100).
          - We fought together against a common foe.
          - You (Assyria) have denounced one of Morocco's declared enemies!
          - We have made Declarations of Friendship with the same leaders!
          - We are trade partners.
          - We have made a public Declaration of Friendship!
          - We have similar Social Policies.
          - We have opened our borders to each other.
          - We have shared embassies.
          - We have different religious beliefs.
          - You (Assyria) have chosen to adopt the Order Ideology, but Morocco believe in Autocracy.
          - Morocco desire friendly relations with Assyria.
          - You (Assyria) have conquered City-States under Morocco's protection!
        - Score: 2101
        - Era: Information
        - Technologies: 70
        - Cities: 7
        - Population: 207
        - Territory: 237
        - Gold: 230
        - GoldPerTurn: 423
        - HappinessSituation: Happy
        - HappinessPercentage: 88
        - MilitaryStrength: 5487
        - TourismPerTurn: 460.9
        - CulturePerTurn: 1332
        - PolicyBranches:
          - Fealty: 1
          - Tradition: 2
          - Rationalism: 6
          - Statecraft: 6
          - Autocracy: 2
          - Industry: 2
          - Progress: 5
        - ResourcesAvailable:
          - Wheat: 2
          - Sheep: 3
          - Ivory: 1
          - Paper: 9
          - Maize: 4
          - Gems: 1
          - Aluminum: 3
          - Glass: 1
          - Fish: 9
          - Amber: 1
          - Jade: 1
          - Iron: 4
          - Tea: 1
          - Cattle: 3
          - Uranium: 7
          - Coral: 1
          - Jewelry: 1
          - Bison: 2
          - Antiquity Site: 1
          - Citrus: 1
          - Copper: 1
          - Crab: 1
          - Incense: 6
          - Stone: 6
          - Marble: 1
          - Cinnamon: 1
          - Bananas: 1
          - Oil: 8
          - Wine: 1
          - Cocoa: 1
          - Tobacco: 1
        - FoundedReligion: Islam
        - Relationships:
          - Austria:
            - Distance: Close
            - Denounced Them
          - Assyria:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - The Inca:
            - Distance: Close
            - Denounced Them
          - Indonesia:
            - Distance: Far
            - Open Borders
            - Declaration of Friendship
          - The Huns:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - Poland:
            - Distance: Neighbors
            - Declaration of Friendship
        - Votes: 10
        
        ## Player 4
        - Civilization: Austria
        - Leader: Maria Theresa
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Austria) have denounced one of Assyria's declared enemies! (11)
          - We have similar Social Policies. (3)
          - Assyria's real approach to Austria is Hostile.
          - You (Austria) have denounced a leader Assyria made a Declaration of Friendship with! (-11)
          - You (Austria) have made a Declaration of Friendship with one of Assyria's enemies! (-13)
          - Religious differences strain your (Austria) relationship. (-30)
          - Your (Austria) spies were caught stealing from Assyria. (-33)
          - Assyria's leader has expressed a public opinion of Austria (-100).
          - Assyria's leader has formed a private opinion of Austria (-100).
          - You (Austria) have chosen to adopt the Freedom Ideology, but Assyria believe in Order. (-999)
          - You (Austria) are at war! (-99999)
        - TheirOpinionOfUs:
          - You (Assyria) have denounced one of Austria's declared enemies!
          - You (Assyria) are not competing for World Wonders.
          - You (Assyria) have no contested borders.
          - We have similar Social Policies.
          - Austria fear your (Assyria) warmongering will end this world in fire! (They hate warmongers!)
          - Austria are spreading Austria's own religion, but you (Assyria) converted some of their cities to your (Assyria) religion.
          - Religious differences strain your (Assyria) relationship.
          - We defeated Austria's proposal in the United Nations.
          - Your (Assyria) spies were caught stealing from Austria.
          - Austria believe we are expanding Assyria too aggressively!
          - You (Assyria) killed or captured Austria's civilians!
          - You (Assyria) have conquered City-States under Austria's protection!
          - You (Assyria) have made a Declaration of Friendship with one of Austria's enemies!
          - We have denounced Austria!
          - Austria are jealous of our superior culture!
          - You (Assyria) have chosen to adopt the Order Ideology, but Austria believe in Freedom.
          - Your (Assyria) votes opposed Austria's civ's interests in the United Nations.
          - You (Assyria) are at war!
        - Score: 4509
        - Era: Information
        - GoldenAge: 7 turns remaining
        - Technologies: 72
        - Cities: 15
        - Population: 443
        - Territory: 640
        - Gold: 7935
        - GoldPerTurn: 974
        - HappinessSituation: Happy
        - HappinessPercentage: 66
        - MilitaryStrength: 60117
        - TourismPerTurn: 1842.5
        - CulturePerTurn: 3647
        - PolicyBranches:
          - Freedom: 9
          - Tradition: 6
          - Artistry: 1
          - Statecraft: 6
          - Progress: 5
        - ResourcesAvailable:
          - Wheat: 4
          - Sheep: 6
          - Ivory: 2
          - Paper: 22
          - Maize: 3
          - Gems: 1
          - Aluminum: 27
          - Glass: 1
          - Fish: 24
          - Deer: 5
          - Iron: 6
          - Dyes: 1
          - Tea: 4
          - Coal: 6
          - Cattle: 1
          - Silk: 9
          - Jewelry: 1
          - Bison: 3
          - Citrus: 1
          - Copper: 1
          - Stone: 2
          - Marble: 1
          - Oil: 1
          - Wine: 3
          - Porcelain: 1
        - FoundedReligion: Buddhism
        - Relationships:
          - The Inca:
            - Distance: Neighbors
            - War (Our Score: 2%; Our War Weariness: 26%)
            - Denounced Them
          - Assyria:
            - Distance: Close
            - War (Our Score: -8%; Our War Weariness: 68%)
          - The Huns:
            - Distance: Neighbors
            - Our Vassal (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Indonesia:
            - Distance: Far
            - War (Our Score: 2%; Our War Weariness: 4%)
            - Denounced Them
          - Morocco:
            - Distance: Close
            - Denounced Them
          - Poland:
            - Distance: Close
            - Denounced Them
        - Votes: 45
        
        ## Player 5
        - Civilization: Indonesia
        - Leader: Gajah Mada
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Indonesia) have both adopted the Order Ideology. (999)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have similar Social Policies. (3)
          - Assyria's real approach to Indonesia is War.
          - You (Indonesia) have made a Declaration of Friendship with one of Assyria's enemies! (-13)
          - Religious differences strain your (Indonesia) relationship. (-30)
          - Your (Indonesia) spies were caught stealing from Assyria. (-33)
          - Assyria's leader has expressed a public opinion of Indonesia (-60).
          - Assyria's leader has formed a private opinion of Indonesia (-65).
          - You (Indonesia) are at war! (-99999)
        - TheirOpinionOfUs:
          - Your (Assyria) votes supported Indonesia's civ's interests in the United Nations.
          - You (Assyria) have denounced one of Indonesia's declared enemies!
          - We have made Declarations of Friendship with the same leaders!
          - Indonesia's leader has expressed a public opinion of you (Assyria) (60).
          - We passed Indonesia's proposal in the United Nations.
          - You (Assyria) have both adopted the Order Ideology.
          - We fought together against a common foe.
          - You (Assyria) are not competing for technological advancement.
          - We have similar Social Policies.
          - You (Assyria) have no contested borders.
          - Indonesia fear your (Assyria) warmongering will end this world in fire! (They strongly dislike warmongers.)
          - Religious differences strain your (Assyria) relationship.
          - You (Assyria) plundered Indonesia's trade routes!
          - You (Assyria) have conquered City-States under Indonesia's protection!
          - Your (Assyria) spies were caught stealing from Indonesia.
          - Indonesia's friends or allies have denounced you (Assyria)!
          - You (Assyria) have denounced a leader Indonesia made a Declaration of Friendship with!
          - You (Assyria) are at war!
        - Score: 972
        - Era: Atomic
        - Technologies: 60
        - Cities: 2
        - Population: 46
        - Territory: 82
        - Gold: 593
        - GoldPerTurn: 30
        - HappinessSituation: Happy
        - HappinessPercentage: 62
        - MilitaryStrength: 650
        - TourismPerTurn: 71
        - CulturePerTurn: 246
        - PolicyBranches:
          - Tradition: 6
          - Rationalism: 6
          - Statecraft: 6
          - Order: 1
          - Progress: 1
        - ResourcesAvailable:
          - Silver: 1
          - Cloves: 2
          - Nutmeg: 1
          - Paper: 8
          - Fish: 4
          - Deer: 2
          - Jade: 1
          - Dyes: 1
          - Cattle: 1
          - Pepper: 2
          - Bison: 1
          - Crab: 1
          - Incense: 1
          - Oil: 1
          - Tobacco: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Austria:
            - Distance: Far
            - War (Our Score: -2%; Our War Weariness: 1%)
          - Assyria:
            - Distance: Neighbors
            - War (Our Score: 0%; Our War Weariness: 2%)
          - The Inca:
            - Distance: Close
            - Our Master (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - The Huns:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 0%)
          - Morocco:
            - Distance: Far
            - Open Borders
            - Declaration of Friendship
          - Poland:
            - Distance: Distant
            - Declaration of Friendship
        - Votes: 6
        
        ## Player 6
        - Civilization: The Huns
        - Leader: Attila
        - IsMajor: true
        - OurOpinionOfThem:
          - You (The Huns) have denounced one of Assyria's declared enemies! (11)
          - We have made Declarations of Friendship with the same leaders! (8)
          - Assyria's real approach to The Huns is War.
          - You (The Huns) have denounced a leader Assyria made a Declaration of Friendship with! (-11)
          - You (The Huns) have made a Declaration of Friendship with one of Assyria's enemies! (-13)
          - Religious differences strain your (The Huns) relationship. (-30)
          - Assyria's leader has expressed a public opinion of The Huns (-100).
          - Assyria's leader has formed a private opinion of The Huns (-100).
          - You (The Huns) have adopted the Freedom Ideology, but Assyria believe in Order. (-999)
          - You (The Huns) are at war! (-99999)
        - TheirOpinionOfUs:
          - The Huns's leader has expressed a public opinion of you (Assyria) (75).
          - We have made Declarations of Friendship with the same leaders!
          - You (Assyria) have denounced one of The Huns's declared enemies!
          - Your (Assyria) votes supported The Huns's civ's interests in the United Nations.
          - You (Assyria) have no contested borders.
          - The Huns fear your (Assyria) warmongering will end this world in fire! (They ignore most warmongering.)
          - Religious differences strain your (Assyria) relationship.
          - We defeated The Huns's proposal in the United Nations.
          - You (Assyria) have made a Declaration of Friendship with one of The Huns's enemies!
          - You (Assyria) have denounced a leader The Huns made a Declaration of Friendship with!
          - Your (Assyria) spies were caught stealing from The Huns.
          - You (Assyria) have chosen to adopt the Order Ideology, but The Huns believe in Freedom.
          - You (Assyria) are at war!
        - Score: 1396
        - Era: Atomic
        - Technologies: 53
        - Cities: 5
        - Population: 113
        - Territory: 171
        - Gold: 306
        - GoldPerTurn: 201
        - HappinessSituation: Happy
        - HappinessPercentage: 56
        - MilitaryStrength: 2509
        - TourismPerTurn: 155.75
        - CulturePerTurn: 771
        - PolicyBranches:
          - Freedom: 2
          - Artistry: 1
          - Statecraft: 2
          - Imperialism: 5
          - Progress: 4
          - Authority: 6
        - ResourcesAvailable:
          - Sheep: 1
          - Gems: 1
          - Aluminum: 9
          - Paper: 6
          - Glass: 2
          - Deer: 5
          - Tea: 3
          - Iron: 1
          - Horses: 1
          - Silk: 1
          - Jewelry: 2
          - Fish: 13
          - Citrus: 2
          - Incense: 1
          - Stone: 1
          - Dyes: 1
          - Oil: 3
          - Wine: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - Our Master (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Assyria:
            - Distance: Far
            - War (Our Score: -12%; Our War Weariness: 3%)
          - The Inca:
            - Distance: Far
            - War (Our Score: -14%; Our War Weariness: 2%)
            - Denounced Them
          - Indonesia:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
          - Morocco:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - Poland:
            - Distance: Close
            - Denounced Them
        - Votes: 8
        
        ## Player 7
        - Civilization: Poland
        - Leader: Casimir III
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Poland) have both chosen to adopt the Order Ideology. (999)
          - Assyria's leader has expressed a public opinion of Poland (100).
          - Assyria's leader has formed a private opinion of Poland (100).
          - You (Poland) have denounced one of Assyria's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have similar Social Policies. (3)
          - We have shared embassies. (1)
          - Assyria's real approach to Poland is Friendly.
          - You (Poland) have made a Declaration of Friendship with one of Assyria's enemies! (-13)
          - Religious differences strain your (Poland) relationship. (-30)
        - TheirOpinionOfUs:
          - Your (Assyria) votes supported Poland's civ's interests in the United Nations.
          - You (Assyria) have both chosen to adopt the Order Ideology.
          - We passed Poland's proposal in the United Nations.
          - Poland's leader has expressed a public opinion of you (Assyria) (75).
          - We have made Declarations of Friendship with the same leaders!
          - You (Assyria) have denounced one of Poland's declared enemies!
          - We have similar Social Policies.
          - We fought together against a common foe.
          - We have made a public Declaration of Friendship!
          - We are trade partners.
          - We have shared embassies.
          - We have different religious beliefs.
          - Poland desire friendly relations with Assyria.
        - Score: 3376
        - Era: Information
        - Technologies: 70
        - Cities: 8
        - Population: 242
        - Territory: 358
        - Gold: 164
        - GoldPerTurn: 37
        - HappinessSituation: Happy
        - HappinessPercentage: 90
        - MilitaryStrength: 25221
        - TourismPerTurn: 1764.6
        - CulturePerTurn: 1880
        - PolicyBranches:
          - Fealty: 2
          - Order: 9
          - Tradition: 5
          - Artistry: 6
          - Statecraft: 5
          - Rationalism: 1
          - Industry: 1
          - Progress: 3
        - ResourcesAvailable:
          - Wheat: 4
          - Sheep: 1
          - Ivory: 1
          - Paper: 10
          - Pearls: 1
          - Gems: 1
          - Aluminum: 10
          - Bison: 1
          - Amber: 7
          - Deer: 7
          - Coal: 6
          - Fish: 8
          - Cattle: 1
          - Uranium: 8
          - Horses: 3
          - Copper: 1
          - Incense: 2
          - Stone: 4
          - Marble: 1
          - Wine: 2
        - FoundedReligion: Catholicism
        - Relationships:
          - Austria:
            - Distance: Close
            - Denounced Them
          - Assyria:
            - Distance: Close
            - Declaration of Friendship
          - The Huns:
            - Distance: Close
          - Indonesia:
            - Distance: Distant
            - Declaration of Friendship
          - Morocco:
            - Distance: Neighbors
            - Declaration of Friendship
          - The Inca:
            - Distance: Far
        - Votes: 10
        
        ## Player 22
        - Civilization: Palatium
        - Leader: City State
        - MajorAlly: Morocco
        - Population: 21
        - ResourcesAvailable:
          - Fish: 1
        - Relationships:
          - Austria: Friends (Influence: 249, Distance: Close, Protected)
          - Assyria: Friends (Influence: 30, Distance: Distant)
          - The Inca: Friends (Influence: 78, Distance: Far)
          - The Huns: Neutral (Influence: 0, Distance: Distant)
          - Indonesia: Neutral (Influence: 0, Distance: Distant)
          - Morocco: Ally (Influence: 327, Distance: Neighbors, Protected)
          - Poland: Friends (Influence: 56, Distance: Close, Protected)
        - Quests:
          - Diplomatic Missions are temporarily more effective. (Turns remaining: 26) They want you to start a land or sea trade route to their city. (Turns remaining: 24) Potential Quest Reward: * 130 Influence * 210 Food in Capital
          - They want you to demand tribute from Geneva. Potential Quest Reward: * 85 Influence * 246 Gold
        - 23: Defeated Minor Civilization Dublin
        
        ## Player 24
        - Civilization: Tyre
        - Leader: City State
        - MajorAlly: Austria
        - Population: 16
        - ResourcesAvailable:
          - Wheat: 1
          - Fish: 1
        - MajorityReligion: Hinduism
        - Relationships:
          - Austria: Ally (Influence: 161, Distance: Distant, Protected)
          - Assyria: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - The Inca: War - Peace Currently Blocked (Influence: -60, Distance: Neighbors)
          - The Huns: Neutral (Influence: -47, Distance: Distant)
          - Indonesia: War - Peace Currently Blocked (Influence: -60, Distance: Neighbors)
          - Morocco: Friends (Influence: 70, Distance: Far, Protected)
          - Poland: Friends (Influence: 44, Distance: Distant)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        - 25: Defeated Minor Civilization Vatican City
        - 26: Defeated Minor Civilization Sokoto
        - 27: Defeated Minor Civilization Buenos Aires
        
        ## Player 28
        - Civilization: Abernethy
        - Leader: City State
        - MajorAlly: Austria
        - Population: 39
        - ResourcesAvailable:
          - Fish: 1
          - Stone: 1
        - MajorityReligion: Buddhism
        - Relationships:
          - Austria: Ally (Influence: 907, Distance: Neighbors, Protected)
          - Assyria: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - The Inca: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - The Huns: Friends (Influence: 214, Distance: Close, Protected)
          - Indonesia: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Morocco: Neutral (Influence: 13, Distance: Distant)
          - Poland: Friends (Influence: 304, Distance: Distant, Protected)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        - 29: Defeated Minor Civilization Nippur
        
        ## Player 30
        - Civilization: Okilis
        - Leader: City State
        - MajorAlly: Austria
        - Population: 27
        - ResourcesAvailable:
          - Fish: 3
        - Relationships:
          - Austria: Ally (Influence: 1255, Distance: Neighbors, Protected)
          - Assyria: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - The Inca: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - The Huns: Neutral (Influence: 0, Distance: Close)
          - Indonesia: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Morocco: Friends (Influence: 72, Distance: Distant)
          - Poland: Friends (Influence: 44, Distance: Distant)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 31
        - Civilization: Manila
        - Leader: City State
        - MajorAlly: Austria
        - Population: 23
        - ResourcesAvailable:
          - Fish: 1
        - MajorityReligion: Buddhism
        - Relationships:
          - Austria: Ally (Influence: 737, Distance: Neighbors, Protected)
          - Assyria: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - The Inca: War - Peace Currently Blocked (Influence: -60, Distance: Neighbors)
          - The Huns: Friends (Influence: 44, Distance: Far)
          - Indonesia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Morocco: Neutral (Influence: -48, Distance: Far)
          - Poland: Friends (Influence: 44, Distance: Far, Protected)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        - 32: Defeated Minor Civilization Argos
        - 33: Defeated Minor Civilization Sydney
        
        ## Player 34
        - Civilization: Geneva
        - Leader: City State
        - MajorAlly: Poland
        - Population: 17
        - ResourcesAvailable:
          - Fish: 2
          - Sheep: 1
        - Relationships:
          - Austria: Friends (Influence: 516, Distance: Close, Protected)
          - Assyria: Neutral (Influence: -51, Distance: Distant)
          - The Inca: Neutral (Influence: 9, Distance: Far)
          - The Huns: Neutral (Influence: -51, Distance: Distant)
          - Indonesia: Neutral (Influence: -51, Distance: Distant)
          - Morocco: Neutral (Influence: -16, Distance: Close)
          - Poland: Ally (Influence: 666, Distance: Neighbors, Protected)
        - Quests:
          - They want Eastern Orthodoxy to become the majority religion in their city. (Turns remaining: 48) Potential Quest Reward: * 157 Influence * 535 Faith
        - 35: Defeated Minor Civilization Brussels
        - 36: Defeated Minor Civilization Salem
        - 37: Defeated Minor Civilization Pago Pago
        - 63: Barbarians
        
        # Cities
        Cities: summary reports about discovered cities in the world.
        
        ## Player: The Inca
        
        ### Cusco
        - ID: 1057
        - X: 10
        - Y: 5
        - Population: 43
        - MajorityReligion: Hinduism
        - DefenseStrength: 121
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Circus Maximus
          - Ironworks
          - Royal Collection
          - Eiffel Tower
          - National Intelligence Agency
          - Grand Temple
          - Palace of Culture and Science
          - Summer Palace
          - Grand Canal
          - Menin Gate
          - Firaxite Materials Headquarters
        
        ### Tiwanaku
        - ID: 1173
        - X: 14
        - Y: 8
        - Population: 37
        - MajorityReligion: Hinduism
        - DefenseStrength: 107
        - Wonders:
          - Chartered Company
          - Machu Picchu
          - Neuschwanstein
        
        ### Machu
        - ID: 1411
        - X: 10
        - Y: 11
        - Population: 32
        - MajorityReligion: Hinduism
        - DefenseStrength: 112
        - Wonders:
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
        
        ### Ollantaytambo
        - ID: 1723
        - X: 6
        - Y: 10
        - Population: 34
        - MajorityReligion: Hinduism
        - DefenseStrength: 78
        - IsCoastal: true
        - Wonders:
          - Sistine Chapel
          - Forbidden Palace
        
        ### Corihuayrachina
        - ID: 2169
        - X: 4
        - Y: 5
        - Population: 33
        - MajorityReligion: Hinduism
        - DefenseStrength: 107
        - IsCoastal: true
        - Wonders:
          - Imperial College
        
        ### Huamanga
        - ID: 2389
        - X: 6
        - Y: 15
        - Population: 36
        - MajorityReligion: Hinduism
        - DefenseStrength: 115
        - IsCoastal: true
        - Wonders:
          - Red Fort
        
        ### Vilcas
        - ID: 2632
        - X: 10
        - Y: 17
        - Population: 32
        - MajorityReligion: Hinduism
        - DefenseStrength: 109
        - IsCoastal: true
        
        ### Surabaya
        - ID: 5703
        - X: 17
        - Y: 11
        - Population: 36
        - MajorityReligion: Hinduism
        - DefenseStrength: 113
        - IsOccupied: true
        - IsCoastal: true
        
        ### Vilcabamba
        - ID: 6018
        - X: 14
        - Y: 3
        - Population: 34
        - MajorityReligion: Hinduism
        - DefenseStrength: 109
        
        ### Arequipa
        - ID: 8814
        - X: 52
        - Y: 5
        - Population: 22
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 113
        - Health: 91%
        
        ### Vitcos
        - ID: 12172
        - X: 66
        - Y: 22
        - Population: 18
        - DefenseStrength: 103
        - Health: 78%
        - IsCoastal: true
        
        ### Vatican City
        - ID: 12788
        - X: 4
        - Y: 19
        - Population: 31
        - MajorityReligion: Hinduism
        - DefenseStrength: 107
        - IsOccupied: true
        - IsCoastal: true
        
        ### Salem
        - ID: 13266
        - X: 22
        - Y: 12
        - Population: 32
        - MajorityReligion: Hinduism
        - DefenseStrength: 110
        - IsOccupied: true
        - IsCoastal: true
        
        ### Buenos Aires
        - ID: 14354
        - X: 10
        - Y: 21
        - Population: 27
        - MajorityReligion: Hinduism
        - DefenseStrength: 105
        - IsOccupied: true
        - IsCoastal: true
        
        ### Jakarta
        - ID: 15779
        - X: 14
        - Y: 14
        - Population: 33
        - MajorityReligion: Hinduism
        - DefenseStrength: 104
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Great Lighthouse
          - Mausoleum
        
        ### Batam
        - ID: 16588
        - X: 14
        - Y: 22
        - Population: 28
        - MajorityReligion: Hinduism
        - DefenseStrength: 76
        - IsOccupied: true
        - IsCoastal: true
        
        ### Medan
        - ID: 17169
        - X: 20
        - Y: 17
        - Population: 28
        - DefenseStrength: 81
        - IsOccupied: true
        - IsCoastal: true
        
        ### Denpasar
        - ID: 17492
        - X: 24
        - Y: 19
        - Population: 28
        - DefenseStrength: 123
        - IsOccupied: true
        - IsCoastal: true
        
        ### Makassar
        - ID: 18656
        - X: 19
        - Y: 23
        - Population: 23
        - MajorityReligion: Hinduism
        - DefenseStrength: 104
        - IsOccupied: true
        - IsCoastal: true
        
        ### Sydney
        - ID: 20646
        - X: 67
        - Y: 4
        - Population: 11
        - DefenseStrength: 65
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: Assyria
        
        ### Assur
        - ID: 1059
        - X: 61
        - Y: 24
        - Population: 34
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 111
        - IsCoastal: true
        - FoodStored: 2785
        - FoodPerTurn: 41
        - ProductionStored: 492
        - ProductionPerTurn: 372
        - CurrentProduction: Strategic Defense System
        - ProductionTurnsLeft: 3
        - GoldPerTurn: 270
        - SciencePerTurn: 343
        - CulturePerTurn: 259
        - FaithPerTurn: 53
        - TourismPerTurn: 104
        - HappinessDelta: 10
        - BuildingCount: 51
        - ImportantBuildings:
          - Seaport
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Writers' Guild
          - Artists' Guild
          - Musicians' Guild
          - Caravansary
          - Bath
          - Chancery
          - Coaling Station
        - Wonders:
          - Heroic Epic
          - National Monument
          - Chartered Company
          - Imperial College
          - Colossus
          - Alhambra
          - Scrivener's Office
          - Printing Press
          - Royal Guardhouse
        - GreatWorkCount: 8
        
        ### Nineveh
        - ID: 1210
        - X: 57
        - Y: 20
        - Population: 33
        - MajorityReligion: Hinduism
        - DefenseStrength: 68
        - IsCoastal: true
        - FoodStored: 1927
        - FoodPerTurn: 48
        - ProductionStored: 535
        - ProductionPerTurn: 381
        - CurrentProduction: Fighter
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 246
        - SciencePerTurn: 311
        - CulturePerTurn: 166
        - FaithPerTurn: 31
        - TourismPerTurn: 94
        - HappinessDelta: 2
        - BuildingCount: 50
        - ImportantBuildings:
          - Seaport
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Bath
          - Chancery
          - Coaling Station
          - Refinery
        - Wonders:
          - Centaurus Extractors Headquarters
        - GreatWorkCount: 6
        
        ### Nimrud
        - ID: 1554
        - X: 58
        - Y: 26
        - Population: 31
        - MajorityReligion: Hinduism
        - DefenseStrength: 105
        - IsCoastal: true
        - FoodStored: 1617
        - FoodPerTurn: 3
        - ProductionStored: 305
        - ProductionPerTurn: 378
        - CurrentProduction: SS Booster
        - ProductionTurnsLeft: 21
        - GoldPerTurn: 184
        - SciencePerTurn: 423
        - CulturePerTurn: 358
        - FaithPerTurn: 72
        - TourismPerTurn: 284.5
        - HappinessDelta: 2
        - BuildingCount: 51
        - ImportantBuildings:
          - Seaport
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Artists' Guild
          - Hotel
          - Caravansary
          - Bath
          - Chancery
          - Agribusiness
          - Coaling Station
        - Wonders:
          - Circus Maximus
          - Ironworks
          - Royal Collection
          - Great Wall
          - Hagia Sophia
          - Kremlin
          - Grand Temple
          - Royal Library
          - Uffizi
        - GreatWorkCount: 18
        
        ### Kar-Tukulti-Ninurta
        - ID: 1757
        - X: 60
        - Y: 19
        - Population: 29
        - MajorityReligion: Hinduism
        - DefenseStrength: 97
        - IsCoastal: true
        - FoodStored: 1388
        - FoodPerTurn: 5
        - ProductionStored: 309
        - ProductionPerTurn: 379
        - CurrentProduction: SS Booster
        - ProductionTurnsLeft: 21
        - GoldPerTurn: 179
        - SciencePerTurn: 243
        - CulturePerTurn: 125
        - FaithPerTurn: 19
        - TourismPerTurn: 69.5
        - BuildingCount: 54
        - ImportantBuildings:
          - Seaport
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Writers' Guild
          - Musicians' Guild
          - Caravansary
          - Bath
          - Chancery
          - Agribusiness
          - Coaling Station
        - Wonders:
          - Petra
          - Bletchley Park
        - GreatWorkCount: 6
        
        ### Halab
        - ID: 5036
        - X: 51
        - Y: 32
        - Population: 24
        - MajorityReligion: Hinduism
        - DefenseStrength: 105
        - IsCoastal: true
        - FoodStored: 1345
        - FoodPerTurn: 19
        - ProductionStored: 405
        - ProductionPerTurn: 202
        - CurrentProduction: Seaport
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 172
        - SciencePerTurn: 311
        - CulturePerTurn: 112
        - FaithPerTurn: 29
        - TourismPerTurn: 59
        - HappinessDelta: 3
        - BuildingCount: 49
        - ImportantBuildings:
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Harbor
          - Zoo
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Writers' Guild
          - Artists' Guild
          - Caravansary
          - Airport
          - Chancery
        - GreatWorkCount: 6
        
        ### Addis Ababa
        - ID: 5040
        - X: 51
        - Y: 21
        - Population: 32
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 70
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 2429
        - FoodPerTurn: 3
        - ProductionStored: 986
        - ProductionPerTurn: 352
        - CurrentProduction: Public Works
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 190
        - SciencePerTurn: 370
        - CulturePerTurn: 190
        - FaithPerTurn: 92
        - TourismPerTurn: 104.25
        - BuildingCount: 54
        - ImportantBuildings:
          - Courthouse
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Harbor
          - Zoo
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Constabulary
          - Hotel
          - Caravansary
          - Bath
          - Chancery
        - Wonders:
          - Nalanda
          - Celestial Throne
        - GreatWorkCount: 8
        
        ### Harar
        - ID: 5416
        - X: 48
        - Y: 23
        - Population: 29
        - MajorityReligion: Hinduism
        - DefenseStrength: 108
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 1208
        - FoodPerTurn: 59
        - ProductionStored: 0
        - ProductionPerTurn: 328
        - CurrentProduction: Seaport
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 206
        - SciencePerTurn: 261
        - CulturePerTurn: 102
        - FaithPerTurn: 24
        - TourismPerTurn: 70.25
        - HappinessDelta: 7
        - BuildingCount: 53
        - ImportantBuildings:
          - Courthouse
          - Stable
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Harbor
          - Zoo
          - Opera House
          - Museum
          - Military Academy
          - Military Base
          - Hospital
          - Factory
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Hotel
          - Caravansary
          - Chancery
          - Coaling Station
        - GreatWorkCount: 5
        
        ### Ica
        - ID: 9139
        - X: 62
        - Y: 6
        - Population: 18
        - MajorityReligion: Hinduism
        - DefenseStrength: 95
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 758
        - FoodPerTurn: 58
        - ProductionStored: 205
        - ProductionPerTurn: 169
        - CurrentProduction: Public Works
        - ProductionTurnsLeft: 6
        - GoldPerTurn: 129
        - SciencePerTurn: 111
        - CulturePerTurn: 63
        - FaithPerTurn: 12
        - TourismPerTurn: 16.5
        - HappinessDelta: 1
        - BuildingCount: 41
        - ImportantBuildings:
          - Courthouse
          - Stable
          - Customs House
          - Harbor
          - Zoo
          - Armory
          - Military Base
          - Hospital
          - Factory
          - Stock Exchange
          - University
          - Amphitheater
          - Shrine
          - Constabulary
          - Caravansary
          - Chancery
        - GreatWorkCount: 2
        
        ### Sokoto
        - ID: 11702
        - X: 52
        - Y: 28
        - Population: 27
        - DefenseStrength: 11
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 1711
        - FoodPerTurn: 60
        - ProductionStored: 0
        - ProductionPerTurn: 485
        - CurrentProduction: Military Academy
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 95
        - SciencePerTurn: 194
        - CulturePerTurn: 76
        - FaithPerTurn: 8
        - TourismPerTurn: 32.5
        - HappinessDelta: 7
        - BuildingCount: 46
        - ImportantBuildings:
          - Courthouse
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Harbor
          - Stadium
          - Opera House
          - Museum
          - Armory
          - Medical Lab
          - Factory
          - Stock Exchange
          - Public School
          - Shrine
          - Constabulary
          - Caravansary
          - Bath
          - Chancery
          - Lamassu Gate
        - GreatWorkCount: 2
        
        ### Dur-Sharrukin
        - ID: 11886
        - X: 62
        - Y: 28
        - Population: 26
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 108
        - IsCoastal: true
        - FoodStored: 902
        - FoodPerTurn: 50
        - ProductionStored: 102
        - ProductionPerTurn: 95
        - CurrentProduction: Public Works
        - ProductionTurnsLeft: 15
        - GoldPerTurn: 74
        - SciencePerTurn: 102
        - CulturePerTurn: 62
        - FaithPerTurn: 37
        - TourismPerTurn: 0
        - BuildingCount: 42
        - ImportantBuildings:
          - Stable
          - Windmill
          - Customs House
          - Harbor
          - Zoo
          - Temple
          - Armory
          - Military Base
          - Hospital
          - Workshop
          - Bank
          - Public School
          - Police Station
          - Caravansary
          - Chancery
          - Gallery
        - Wonders:
          - Notre Dame
        - GreatWorkCount: 2
        
        ### Gondar
        - ID: 17048
        - X: 43
        - Y: 7
        - Population: 21
        - MajorityReligion: Hinduism
        - DefenseStrength: 110
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 664
        - FoodPerTurn: 6
        - ProductionStored: 904
        - ProductionPerTurn: 317
        - CurrentProduction: SS Booster
        - ProductionTurnsLeft: 23
        - GoldPerTurn: 189
        - SciencePerTurn: 113
        - CulturePerTurn: 58
        - FaithPerTurn: 25
        - TourismPerTurn: 21.75
        - HappinessDelta: 3
        - BuildingCount: 52
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Zoo
          - Temple
          - Opera House
          - Museum
          - Armory
          - Military Base
          - Medical Lab
          - Factory
          - Bank
          - Public School
          - Constabulary
          - Hotel
          - Caravansary
          - Bath
          - Chancery
          - Coaling Station
        - GreatWorkCount: 0
        
        ### Brussels
        - ID: 17658
        - X: 41
        - Y: 13
        - Population: 18
        - MajorityReligion: Hinduism
        - DefenseStrength: 41
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 758
        - FoodPerTurn: 48
        - ProductionStored: 111
        - ProductionPerTurn: 111
        - CurrentProduction: Public Works
        - ProductionTurnsLeft: 11
        - GoldPerTurn: 138
        - SciencePerTurn: 100
        - CulturePerTurn: 39
        - FaithPerTurn: 16
        - TourismPerTurn: 9.25
        - HappinessDelta: -3
        - BuildingCount: 38
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Circus
          - Customs House
          - Garden
          - Opera House
          - Barracks
          - Medical Lab
          - Workshop
          - Bank
          - Public School
          - Shrine
          - Hotel
          - Caravansary
          - Chancery
          - Gallery
          - Lamassu Gate
        - GreatWorkCount: 0
        
        ### Lalibela
        - ID: 18054
        - X: 48
        - Y: 10
        - Population: 21
        - MajorityReligion: Hinduism
        - DefenseStrength: 56
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 1028
        - FoodPerTurn: 4
        - ProductionStored: 1233
        - ProductionPerTurn: 322
        - CurrentProduction: Stadium
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 120
        - SciencePerTurn: 98
        - CulturePerTurn: 53
        - FaithPerTurn: 23
        - TourismPerTurn: 6.25
        - HappinessDelta: -3
        - BuildingCount: 41
        - ImportantBuildings:
          - Courthouse
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Harbor
          - Zoo
          - Temple
          - Opera House
          - Barracks
          - Medical Lab
          - Workshop
          - Bank
          - Public School
          - Constabulary
          - Caravansary
          - Bath
          - Chancery
          - Gallery
          - Coaling Station
          - Lamassu Gate
        - GreatWorkCount: 0
        
        ### Axum
        - ID: 18294
        - X: 52
        - Y: 10
        - Population: 18
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 47
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 582
        - FoodPerTurn: 18
        - ProductionStored: 189
        - ProductionPerTurn: 189
        - CurrentProduction: Public Works
        - ProductionTurnsLeft: 6
        - GoldPerTurn: 41
        - SciencePerTurn: 49
        - CulturePerTurn: 26
        - FaithPerTurn: 21
        - TourismPerTurn: 7.75
        - HappinessDelta: -9
        - BuildingCount: 30
        - ImportantBuildings:
          - Courthouse
          - Stable
          - Harbor
          - Arena
          - Temple
          - Barracks
          - Medical Lab
          - Workshop
          - Constabulary
          - Hotel
          - Caravansary
          - Council
          - Chancery
          - Gallery
        - GreatWorkCount: 0
        
        ### Nippur
        - ID: 19027
        - X: 66
        - Y: 18
        - Population: 14
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 117
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 468
        - FoodPerTurn: 73
        - ProductionStored: 0
        - ProductionPerTurn: 117
        - CurrentProduction: Forge
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 84
        - SciencePerTurn: 58
        - CulturePerTurn: 47
        - FaithPerTurn: 16
        - TourismPerTurn: 7
        - HappinessDelta: -8
        - BuildingCount: 31
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Windmill
          - Garden
          - Arena
          - Opera House
          - Museum
          - Barracks
          - Military Base
          - Hospital
          - Stock Exchange
          - University
          - Caravansary
          - Council
          - Bath
        - GreatWorkCount: 0
        
        ### Argos
        - ID: 19028
        - X: 56
        - Y: 7
        - Population: 10
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 68
        - IsPuppet: true
        - IsCoastal: true
        - FoodStored: 200
        - FoodPerTurn: 83
        - ProductionStored: 1351
        - ProductionPerTurn: 154
        - CurrentProduction: Military Base
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 8
        - SciencePerTurn: 13
        - CulturePerTurn: 8
        - FaithPerTurn: 1
        - TourismPerTurn: 0.5
        - HappinessDelta: 0
        - BuildingCount: 25
        - ImportantBuildings:
          - Stable
          - Customs House
          - Garden
          - Harbor
          - Arena
          - Opera House
          - Arsenal
          - Hospital
          - Workshop
          - Bank
          - Library
          - Caravansary
        - GreatWorkCount: 0
        
        ### Dire Dawa
        - ID: 19988
        - X: 47
        - Y: 5
        - Population: 21
        - MajorityReligion: Hinduism
        - DefenseStrength: 63
        - IsOccupied: true
        - FoodStored: 253
        - FoodPerTurn: 16
        - ProductionStored: 746
        - ProductionPerTurn: 162
        - CurrentProduction: Public Works
        - ProductionTurnsLeft: 3
        - GoldPerTurn: 98
        - SciencePerTurn: 150
        - CulturePerTurn: 46
        - FaithPerTurn: 21
        - TourismPerTurn: 15.25
        - HappinessDelta: -11
        - BuildingCount: 36
        - ImportantBuildings:
          - Courthouse
          - Stable
          - Water Mill
          - Customs House
          - Garden
          - Arena
          - Temple
          - Opera House
          - Museum
          - Barracks
          - Castle
          - Granary
          - Medical Lab
          - Factory
          - Bank
          - Public School
          - Constabulary
          - Hotel
          - Caravansary
          - Chancery
        - GreatWorkCount: 0
        
        ## Player: Morocco
        
        ### Marrakech
        - ID: 1060
        - X: 33
        - Y: 30
        - Population: 42
        - MajorityReligion: Hinduism
        - DefenseStrength: 100
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Chartered Company
          - Ironworks
          - Imperial College
          - Stonehenge
          - National Intelligence Agency
          - Prora
          - Scrivener's Office
          - Printing Press
          - Royal Astrologer
          - Hexxon Refineries Headquarters
        
        ### Rabat
        - ID: 1391
        - X: 36
        - Y: 34
        - Population: 28
        - DefenseStrength: 49
        - IsCoastal: true
        - Wonders:
          - Grand Temple
        
        ### Fes
        - ID: 1981
        - X: 40
        - Y: 39
        - Population: 30
        - DefenseStrength: 58
        - IsCoastal: true
        - Wonders:
          - Circus Maximus
        
        ### Casablanca
        - ID: 2906
        - X: 32
        - Y: 24
        - Population: 29
        - DefenseStrength: 62
        - IsCoastal: true
        
        ### Tangier
        - ID: 3505
        - X: 35
        - Y: 19
        - Population: 27
        - DefenseStrength: 41
        - IsCoastal: true
        - Wonders:
          - Royal Collection
        
        ### Sale
        - ID: 5500
        - X: 36
        - Y: 13
        - Population: 28
        - DefenseStrength: 38
        - IsCoastal: true
        
        ### Bahir Dar
        - ID: 16607
        - X: 40
        - Y: 17
        - Population: 23
        - DefenseStrength: 74
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: Austria
        
        ### Vienna
        - ID: 1061
        - X: 12
        - Y: 42
        - Population: 58
        - MajorityReligion: Buddhism
        - DefenseStrength: 85
        - Wonders:
          - School of Philosophy
          - National Monument
          - Chartered Company
          - Imperial College
          - Royal Collection
          - Oracle
          - Himeji Castle
          - Palace of Westminster
          - Brandenburg Gate
          - Statue of Liberty
          - National Intelligence Agency
          - CN Tower
          - Leaning Tower of Pisa
          - University of Sankore
          - Grand Temple
          - Scrivener's Office
          - Foreign Bureau
          - International Finance Center
          - Ballhausplatz
          - Roman Forum
          - Soho Foundry
          - Empire State Building
          - United Nations
          - Consulate
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
          - Holy Council
          - TwoKay Foods Headquarters
        
        ### Salzburg
        - ID: 1239
        - X: 16
        - Y: 39
        - Population: 33
        - MajorityReligion: Buddhism
        - DefenseStrength: 111
        - IsCoastal: true
        
        ### Graz
        - ID: 1344
        - X: 9
        - Y: 47
        - Population: 28
        - MajorityReligion: Buddhism
        - DefenseStrength: 113
        - Wonders:
          - Heroic Epic
          - Angkor Wat
        
        ### Linz
        - ID: 1555
        - X: 14
        - Y: 36
        - Population: 27
        - MajorityReligion: Buddhism
        - DefenseStrength: 76
        - IsCoastal: true
        - Wonders:
          - Circus Maximus
          - Globe Theatre
        
        ### Klagenfurt
        - ID: 1910
        - X: 9
        - Y: 34
        - Population: 29
        - MajorityReligion: Buddhism
        - DefenseStrength: 81
        - IsCoastal: true
        
        ### Bregenz
        - ID: 2312
        - X: 16
        - Y: 32
        - Population: 27
        - MajorityReligion: Buddhism
        - DefenseStrength: 81
        - Wonders:
          - Ironworks
        
        ### Innsbruck
        - ID: 4019
        - X: 19
        - Y: 35
        - Population: 29
        - MajorityReligion: Buddhism
        - DefenseStrength: 98
        - IsCoastal: true
        
        ### Kitzbuhel
        - ID: 6311
        - X: 2
        - Y: 36
        - Population: 33
        - MajorityReligion: Buddhism
        - DefenseStrength: 110
        - IsCoastal: true
        
        ### St. Polten
        - ID: 7059
        - X: 19
        - Y: 47
        - Population: 28
        - MajorityReligion: Buddhism
        - DefenseStrength: 120
        - IsCoastal: true
        
        ### Sabata
        - ID: 8029
        - X: 7
        - Y: 42
        - Population: 29
        - MajorityReligion: Buddhism
        - DefenseStrength: 76
        - IsOccupied: true
        - IsCoastal: true
        
        ### Kaunas
        - ID: 9217
        - X: 1
        - Y: 43
        - Population: 29
        - MajorityReligion: Buddhism
        - DefenseStrength: 74
        - IsOccupied: true
        - IsCoastal: true
        
        ### Eisenstadt
        - ID: 10537
        - X: 71
        - Y: 31
        - Population: 30
        - MajorityReligion: Buddhism
        - DefenseStrength: 101
        - IsCoastal: true
        
        ### Nasca
        - ID: 14230
        - X: 62
        - Y: 37
        - Population: 27
        - DefenseStrength: 106
        - IsOccupied: true
        - IsCoastal: true
        
        ### Atico
        - ID: 17205
        - X: 54
        - Y: 41
        - Population: 22
        - DefenseStrength: 111
        - IsOccupied: true
        - IsCoastal: true
        
        ### Pago Pago
        - ID: 20176
        - X: 21
        - Y: 30
        - Population: 14
        - MajorityReligion: Buddhism
        - DefenseStrength: 83
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: Indonesia
        
        ### Samarinda
        - ID: 5345
        - X: 23
        - Y: 3
        - Population: 26
        - MajorityReligion: Hinduism
        - DefenseStrength: 80
        - IsCoastal: true
        - Wonders:
          - Chartered Company
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
        
        ### Mataram
        - ID: 10815
        - X: 69
        - Y: 12
        - Population: 20
        - DefenseStrength: 62
        - Health: 93%
        - IsCoastal: true
        
        ## Player: The Huns
        
        ### Attila's Court
        - ID: 1063
        - X: 4
        - Y: 47
        - Population: 25
        - MajorityReligion: Buddhism
        - DefenseStrength: 54
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Chartered Company
          - Ironworks
          - Imperial College
          - Pyramids
          - Statue of Zeus
          - Mausoleum of Halicarnassus
          - Terracotta Army
          - Scrivener's Office
          - Printing Press
          - Ulticur
          - Consulate
        
        ### Sodo
        - ID: 1436
        - X: 1
        - Y: 48
        - Population: 21
        - MajorityReligion: Buddhism
        - DefenseStrength: 56
        - IsCoastal: true
        - Wonders:
          - Royal Collection
          - Grand Temple
        
        ### Villach
        - ID: 4973
        - X: 76
        - Y: 44
        - Population: 24
        - MajorityReligion: Buddhism
        - DefenseStrength: 56
        - IsCoastal: true
        
        ### Debre Berhan
        - ID: 10051
        - X: 72
        - Y: 47
        - Population: 22
        - MajorityReligion: Buddhism
        - DefenseStrength: 5
        - IsCoastal: true
        
        ### Andahuaylas
        - ID: 15157
        - X: 62
        - Y: 46
        - Population: 21
        - DefenseStrength: 60
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: Poland
        
        ### Warsaw
        - ID: 1064
        - X: 33
        - Y: 45
        - Population: 31
        - MajorityReligion: Catholicism
        - DefenseStrength: 78
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Circus Maximus
          - Great Library
          - Hanging Gardens
          - Chichen Itza
          - Porcelain Tower
          - Temple of Artemis
          - National Intelligence Agency
          - Borobudur
          - Scrivener's Office
          - Printing Press
          - Palace of Culture and Science
          - Karlstejn
          - Consulate
          - State Treasury
          - Royal Guardhouse
          - Court Chapel
          - Royal Astrologer
          - Grand Ossuary
        
        ### Krakow
        - ID: 1967
        - X: 35
        - Y: 40
        - Population: 33
        - MajorityReligion: Catholicism
        - DefenseStrength: 75
        - Wonders:
          - Chartered Company
        
        ### Lodz
        - ID: 2443
        - X: 27
        - Y: 46
        - Population: 28
        - MajorityReligion: Catholicism
        - DefenseStrength: 77
        - IsCoastal: true
        - Wonders:
          - Taj Mahal
        
        ### Wroclaw
        - ID: 2511
        - X: 38
        - Y: 43
        - Population: 41
        - MajorityReligion: Catholicism
        - DefenseStrength: 71
        - Wonders:
          - Royal Collection
          - Louvre
          - Grand Temple
        
        ### Poznan
        - ID: 4167
        - X: 38
        - Y: 48
        - Population: 34
        - MajorityReligion: Catholicism
        - DefenseStrength: 71
        - Wonders:
          - Ironworks
          - Imperial College
          - Cristo Redentor
          - Foreign Bureau
          - Civilized Jewelers Headquarters
        
        ### Gdansk
        - ID: 5316
        - X: 43
        - Y: 43
        - Population: 25
        - MajorityReligion: Catholicism
        - DefenseStrength: 67
        - IsCoastal: true
        - Wonders:
          - The Motherland Calls
        
        ### Szczecin
        - ID: 7646
        - X: 48
        - Y: 49
        - Population: 26
        - DefenseStrength: 74
        - IsCoastal: true
        
        ### Dublin
        - ID: 18891
        - X: 43
        - Y: 47
        - Population: 24
        - MajorityReligion: Catholicism
        - DefenseStrength: 52
        - IsPuppet: true
        - IsCoastal: true
        
        ## Player: City-States
        
        ### Palatium
        - ID: 1065
        - X: 29
        - Y: 36
        - Population: 21
        - DefenseStrength: 98
        - IsCoastal: true
        
        ### Tyre
        - ID: 1067
        - X: 21
        - Y: 6
        - Population: 16
        - MajorityReligion: Hinduism
        - DefenseStrength: 94
        - Health: 73%
        - IsCoastal: true
        
        ### Abernethy
        - ID: 1071
        - X: 6
        - Y: 28
        - Population: 23
        - MajorityReligion: Buddhism
        - DefenseStrength: 98
        - IsCoastal: true
        
        ### Amstetten
        - ID: 5586
        - X: 2
        - Y: 31
        - Population: 16
        - MajorityReligion: Buddhism
        - DefenseStrength: 73
        - IsOccupied: true
        - IsCoastal: true
        
        ### Okilis
        - ID: 1073
        - X: 74
        - Y: 33
        - Population: 27
        - DefenseStrength: 122
        - IsCoastal: true
        
        ### Manila
        - ID: 1074
        - X: 13
        - Y: 28
        - Population: 23
        - MajorityReligion: Buddhism
        - DefenseStrength: 97
        - IsCoastal: true
        
        ### Geneva
        - ID: 1077
        - X: 28
        - Y: 42
        - Population: 17
        - DefenseStrength: 98
        - IsCoastal: true
        
        # Military
        Military: summary reports about tactical zones and visible units.
        
        ## Unit Stats
        - CityBombard:
          - Rocket Artillery:
            - Strength: 37
            - RangedStrength: 75
          - Artillery:
            - Strength: 27
            - RangedStrength: 50
        - FastAttack:
          - Modern Armor:
            - Strength: 100
          - Landship:
            - Strength: 60
          - Commando:
            - Strength: 32
        - Defense:
          - Mechanized Infantry:
            - Strength: 80
          - Infantry:
            - Strength: 62
          - Rifleman:
            - Strength: 50
        - Counter:
          - Mobile SAM:
            - Strength: 55
        - Ranged:
          - Light Tank:
            - Strength: 58
            - RangedStrength: 52
          - Machine Gun:
            - Strength: 45
            - RangedStrength: 58
          - Berber Cavalry:
            - Strength: 42
            - RangedStrength: 34
          - Bazooka:
            - Strength: 60
            - RangedStrength: 80
        - AttackSea:
          - Destroyer:
            - Strength: 70
          - Ironclad:
            - Strength: 55
          - Fleet Destroyer:
            - Strength: 80
          - Sensor Combat Ship:
            - Strength: 90
        - AssaultSea:
          - Battleship:
            - Strength: 60
            - RangedStrength: 75
          - Cruiser:
            - Strength: 40
            - RangedStrength: 55
        - CarrierSea:
          - Carrier:
            - Strength: 70
            - RangedStrength: 45
        - AttackAir:
          - Heavy Bomber:
            - RangedStrength: 65
          - Bomber:
            - RangedStrength: 50
        - DefenseAir:
          - Jet Fighter:
            - RangedStrength: 70
          - Fighter:
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
        
        ## Friendly Land Zone 1059
        - ZoneValue: 36
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 561
        - FriendlyStrength: 5309
        - City: Assur
        - AreaID: 41
        - Plots: 11
        - CenterX: 61
        - CenterY: 23
        - Units:
          - Assyria:
            - Heavy Bomber: 1
            - Fighter: 1
            - Bazooka: 2
            - XCOM Squad: 1
            - Sensor Combat Ship: 1
        - Neighbors:
          - 1554
          - 1757
          - 11886
          - 12172
          - -12172
        
        ## Friendly Land Zone 1210
        - ZoneValue: 3
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 98
        - FriendlyStrength: 3553
        - City: Nineveh
        - AreaID: 43
        - Plots: 18
        - CenterX: 56
        - CenterY: 20
        - Units:
          - Assyria:
            - Heavy Bomber: 1
        - Neighbors:
          - 5040
          - -5040
          - 1554
          - 1757
        
        ## Enemy Land Zone 1239
        - ZoneValue: 36
        - Dominance: Enemy
        - EnemyStrength: 905
        - City: Salzburg
        - AreaID: 79
        - Plots: 15
        - CenterX: 16
        - CenterY: 39
        - Units:
          - Austria:
            - Mechanized Infantry: 1
        
        ## Friendly Land Zone 1554
        - ZoneValue: 42
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 98
        - FriendlyStrength: 3944
        - City: Nimrud
        - AreaID: 41
        - Plots: 25
        - CenterX: 57
        - CenterY: 25
        - Units:
          - Assyria:
            - Heavy Bomber: 2
            - XCOM Squad: 1
        - Neighbors:
          - 11702
          - 1210
          - 1059
          - 11886
        
        ## Friendly Land Zone 1757
        - ZoneValue: 3
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 378
        - FriendlyStrength: 5110
        - City: Kar-Tukulti-Ninurta
        - AreaID: 34
        - Plots: 20
        - CenterX: 60
        - CenterY: 19
        - Units:
          - Assyria:
            - Mobile SAM: 1
            - Heavy Bomber: 1
            - Fighter: 1
            - Machine Gun: 2
            - Bazooka: 1
        - Neighbors:
          - 1210
          - 1059
          - 19027
          - 12172
        
        ## Neutral Land Zone 3505
        - ZoneValue: 30
        - NeutralStrength: 1521
        - City: Tangier
        - AreaID: 25
        - Plots: 17
        - CenterX: 36
        - CenterY: 20
        - Units:
          - Morocco:
            - Berber Cavalry: 1
        - Neighbors:
          - -5500
          - 5500
          - 16607
          - -16607
        
        ## Friendly Land Zone 5036
        - ZoneValue: 30
        - Dominance: Friendly
        - FriendlyStrength: 1845
        - City: Halab
        - AreaID: 91
        - Plots: 5
        - CenterX: 50
        - CenterY: 32
        - Units:
          - Assyria:
            - Jet Fighter: 1
            - Rocket Artillery: 2
            - Fighter: 3
        - Neighbors:
          - 11702
        
        ## Friendly Land Zone 5040
        - ZoneValue: 36
        - Dominance: Friendly
        - FriendlyStrength: 1428
        - City: Addis Ababa
        - AreaID: 41
        - Plots: 28
        - CenterX: 52
        - CenterY: 21
        - Units:
          - Assyria:
            - Machine Gun: 1
        - Neighbors:
          - 5416
          - -5040
          - 11702
          - 1210
        
        ## Enemy Land Zone 5345
        - ZoneValue: 30
        - Dominance: Enemy
        - EnemyStrength: 1261
        - City: Samarinda
        - AreaID: 1
        - Plots: 11
        - CenterX: 23
        - CenterY: 3
        - Units:
          - Indonesia:
            - Landship: 1
        
        ## Friendly Land Zone 5416
        - ZoneValue: 3
        - Dominance: Friendly
        - FriendlyStrength: 1497
        - City: Harar
        - AreaID: 48
        - Plots: 25
        - CenterX: 48
        - CenterY: 22
        - Units:
          - Assyria:
            - Fighter: 2
            - Bazooka: 1
            - Sensor Combat Ship: 1
        - Neighbors:
          - -16607
          - -5416
          - 5040
          - -5040
          - 11702
        
        ## Neutral Land Zone 5500
        - ZoneValue: 48
        - Dominance: Friendly
        - NeutralStrength: 1491
        - FriendlyStrength: 352
        - City: Sale
        - AreaID: 25
        - Plots: 11
        - CenterX: 37
        - CenterY: 14
        - Units:
          - Morocco:
            - Destroyer: 1
            - Artillery: 1
            - Infantry: 1
            - Rifleman: 1
            - Triplane: 1
            - Bomber: 1
            - Machine Gun: 2
            - Berber Cavalry: 1
        - Neighbors:
          - -5500
          - 3505
          - 16607
          - 17658
        
        ## Enemy Land Zone 8814
        - ZoneValue: 480
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 769
        - FriendlyStrength: 5162
        - City: Arequipa
        - AreaID: 2
        - Plots: 29
        - CenterX: 52
        - CenterY: 4
        - Units:
          - The Inca:
            - Mobile SAM: 1
            - Heavy Bomber: 1
            - Fighter: 1
            - Infantry: 1
          - Assyria:
            - Modern Armor: 1
            - Mobile SAM: 5
            - Mechanized Infantry: 2
            - Paratrooper: 1
            - XCOM Squad: 2
        - Neighbors:
          - 19988
          - 18294
          - 19028
        
        ## Friendly Land Zone 9139
        - ZoneValue: 24
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 349
        - FriendlyStrength: 2361
        - City: Ica
        - AreaID: 2
        - Plots: 20
        - CenterX: 62
        - CenterY: 4
        - Units:
          - Assyria:
            - Mobile SAM: 1
            - Mechanized Infantry: 1
            - Heavy Bomber: 2
        - Neighbors:
          - 19028
          - 20646
        
        ## Enemy Land Zone 10815
        - ZoneValue: 12
        - Dominance: Even
        - Posture: Steamroll
        - EnemyStrength: 1063
        - FriendlyStrength: 1213
        - City: Mataram
        - AreaID: 24
        - Plots: 4
        - CenterX: 69
        - CenterY: 12
        - Units:
          - Indonesia:
            - Rifleman: 1
            - Bomber: 1
            - Landship: 2
        - Neighbors:
          - -10815
        
        ## Friendly Land Zone 11702
        - ZoneValue: 30
        - Dominance: Friendly
        - FriendlyStrength: 2229
        - City: Sokoto
        - AreaID: 41
        - Plots: 25
        - CenterX: 52
        - CenterY: 27
        - Units:
          - Assyria:
            - Heavy Bomber: 1
            - Fighter: 1
        - Neighbors:
          - 5416
          - 5036
          - 5040
          - 1554
        
        ## Friendly Land Zone 11886
        - ZoneValue: 6
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 512
        - FriendlyStrength: 3424
        - City: Dur-Sharrukin
        - AreaID: 41
        - Plots: 7
        - CenterX: 61
        - CenterY: 27
        - Units:
          - Assyria:
            - Mechanized Infantry: 1
            - Heavy Bomber: 1
            - Fighter: 1
            - Machine Gun: 1
            - Bazooka: 2
        - Neighbors:
          - 1554
          - -11886
          - 1059
        
        ## Enemy Land Zone 12172
        - ZoneValue: 288
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 764
        - FriendlyStrength: 4863
        - City: Vitcos
        - AreaID: 50
        - Plots: 9
        - CenterX: 65
        - CenterY: 22
        - Units:
          - The Inca:
            - Fighter: 2
            - Infantry: 1
          - Assyria:
            - Mobile SAM: 1
            - Mechanized Infantry: 1
        - Neighbors:
          - 1757
          - 1059
          - -12172
          - 19027
          - -11886
        
        ## Enemy Land Zone 14230
        - ZoneValue: 48
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 658
        - FriendlyStrength: 77
        - City: Nasca
        - AreaID: 105
        - Plots: 2
        - CenterX: 62
        - CenterY: 37
        - Units:
          - Austria:
            - Artillery: 1
            - Special Forces: 1
        - Neighbors:
          - -14230
        
        ## Enemy Land Zone 15157
        - ZoneValue: 24
        - Dominance: Enemy
        - EnemyStrength: 1101
        - City: Andahuaylas
        - AreaID: 132
        - Plots: 11
        - CenterX: 62
        - CenterY: 47
        - Units:
          - The Huns:
            - Artillery: 1
            - Infantry: 1
            - Commando: 1
        - Neighbors:
          - -15157
        
        ## Neutral Land Zone 16607
        - ZoneValue: 48
        - Dominance: Friendly
        - NeutralStrength: 1722
        - FriendlyStrength: 352
        - City: Bahir Dar
        - AreaID: 25
        - Plots: 18
        - CenterX: 39
        - CenterY: 17
        - Units:
          - Morocco:
            - Infantry: 2
            - Special Forces: 1
            - Triplane: 2
            - Machine Gun: 1
            - Berber Cavalry: 5
        - Neighbors:
          - 3505
          - 5500
          - -16607
          - 17658
        
        ## Friendly Land Zone 17048
        - ZoneValue: 30
        - Dominance: Friendly
        - FriendlyStrength: 1732
        - City: Gondar
        - AreaID: 2
        - Plots: 16
        - CenterX: 44
        - CenterY: 5
        - Units:
          - Assyria:
            - Fighter: 1
            - Bazooka: 1
        - Neighbors:
          - 19988
          - 18054
        
        ## Enemy Land Zone 17205
        - ZoneValue: 48
        - Dominance: Enemy
        - EnemyStrength: 799
        - NeutralStrength: 132
        - City: Atico
        - AreaID: 116
        - Plots: 3
        - CenterX: 54
        - CenterY: 43
        - Units:
          - Austria:
            - Mechanized Infantry: 1
        
        ## Friendly Land Zone 17658
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 1391
        - FriendlyStrength: 921
        - City: Brussels
        - AreaID: 26
        - Plots: 9
        - CenterX: 41
        - CenterY: 13
        - Units:
          - Assyria:
            - Mobile SAM: 1
            - Heavy Bomber: 1
            - Fighter: 1
        - Neighbors:
          - 5500
          - -5500
          - 16607
          - -17658
          - -16607
        
        ## Friendly Land Zone 18054
        - ZoneValue: 24
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 287
        - FriendlyStrength: 3109
        - City: Lalibela
        - AreaID: 2
        - Plots: 12
        - CenterX: 47
        - CenterY: 10
        - Units:
          - Assyria:
            - Mechanized Infantry: 1
            - Heavy Bomber: 1
            - Fighter: 1
        - Neighbors:
          - 17048
          - 19988
          - 18294
        
        ## Friendly Land Zone 18294
        - ZoneValue: 18
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 287
        - FriendlyStrength: 4409
        - City: Axum
        - AreaID: 2
        - Plots: 16
        - CenterX: 52
        - CenterY: 10
        - Units:
          - Assyria:
            - Mechanized Infantry: 1
            - Heavy Bomber: 1
        - Neighbors:
          - 19988
          - 18054
          - 8814
        
        ## Friendly Land Zone 19027
        - ZoneValue: 3
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 915
        - FriendlyStrength: 3217
        - City: Nippur
        - AreaID: 32
        - Plots: 10
        - CenterX: 64
        - CenterY: 18
        - Units:
          - Assyria:
            - Modern Armor: 1
            - Rocket Artillery: 2
            - Heavy Bomber: 1
            - Fighter: 1
            - XCOM Squad: 1
            - Fleet Destroyer: 1
        - Neighbors:
          - 1757
          - -10815
          - 12172
          - -12172
        
        ## Friendly Land Zone 19028
        - ZoneValue: 18
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 502
        - FriendlyStrength: 4309
        - City: Argos
        - AreaID: 2
        - Plots: 33
        - CenterX: 57
        - CenterY: 5
        - Units:
          - Assyria:
            - Modern Armor: 1
            - Mobile SAM: 2
            - Mechanized Infantry: 1
            - Bazooka: 1
        - Neighbors:
          - 8814
          - 9139
        
        ## Friendly Land Zone 19988
        - ZoneValue: 24
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 371
        - FriendlyStrength: 3809
        - City: Dire Dawa
        - AreaID: 2
        - Plots: 31
        - CenterX: 47
        - CenterY: 4
        - Units:
          - Assyria:
            - Mechanized Infantry: 1
            - Heavy Bomber: 1
        - Neighbors:
          - 17048
          - 18054
          - 8814
          - 18294
        
        ## Enemy Land Zone 20646
        - ZoneValue: 216
        - Dominance: Even
        - Posture: Steamroll
        - EnemyStrength: 809
        - FriendlyStrength: 1307
        - City: Sydney
        - AreaID: 2
        - Plots: 13
        - CenterX: 65
        - CenterY: 3
        - Units:
          - The Inca:
            - Mobile SAM: 1
            - Infantry: 1
          - Assyria:
            - Mobile SAM: 2
            - Mechanized Infantry: 2
        - Neighbors:
          - 9139
        
        ## Enemy Sea Zone -10815
        - ZoneValue: 48
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 1188
        - FriendlyStrength: 741
        - City: Mataram
        - AreaID: 0
        - Plots: 61
        - CenterX: 69
        - CenterY: 12
        - Units:
          - Assyria:
            - Sensor Combat Ship: 1
          - Indonesia:
            - Destroyer: 1
            - Rifleman: 1
        - Neighbors:
          - 19027
          - 10815
          - -100000
        
        ## Friendly Sea Zone -17658
        - ZoneValue: 8
        - Dominance: Friendly
        - NeutralStrength: 1726
        - FriendlyStrength: 1343
        - City: Brussels
        - AreaID: 0
        - Plots: 30
        - CenterX: 42
        - CenterY: 12
        - Units:
          - Assyria:
            - Sensor Combat Ship: 2
        - Neighbors:
          - -5500
          - 17658
          - -16607
        
        ## Neutral Sea Zone -5316
        - ZoneValue: 12
        - NeutralStrength: 1684
        - City: Gdansk
        - AreaID: 0
        - Plots: 25
        - CenterX: 46
        - CenterY: 42
        - Units:
          - Poland:
            - Destroyer: 1
            - Fleet Destroyer: 1
        
        ## Neutral Sea Zone -16607
        - ZoneValue: 1
        - Dominance: Friendly
        - NeutralStrength: 1618
        - FriendlyStrength: 796
        - City: Bahir Dar
        - AreaID: 31
        - Plots: 31
        - CenterX: 42
        - CenterY: 19
        - Units:
          - Assyria:
            - Battleship: 1
          - Morocco:
            - Battleship: 1
            - Fleet Destroyer: 1
        - Neighbors:
          - 16607
          - 3505
          - 17658
          - -17658
          - -5416
          - 5416
        
        ## Enemy Sea Zone -14230
        - ZoneValue: 64
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 438
        - FriendlyStrength: 374
        - City: Nasca
        - AreaID: 0
        - Plots: 75
        - CenterX: 62
        - CenterY: 37
        - Units:
          - Assyria:
            - Sensor Combat Ship: 2
        - Neighbors:
          - -11886
          - -15157
          - 14230
          - -100012
        
        ## Friendly Sea Zone -5416
        - ZoneValue: 10
        - Dominance: Friendly
        - FriendlyStrength: 2148
        - City: Harar
        - AreaID: 0
        - Plots: 29
        - CenterX: 46
        - CenterY: 24
        - Units:
          - Assyria:
            - Sensor Combat Ship: 2
        - Neighbors:
          - -16607
          - 5416
        
        ## Neutral Sea Zone -5500
        - ZoneValue: 16
        - Dominance: Friendly
        - NeutralStrength: 1963
        - FriendlyStrength: 596
        - City: Sale
        - AreaID: 0
        - Plots: 43
        - CenterX: 35
        - CenterY: 11
        - Units:
          - Morocco:
            - Carrier: 1
            - Battleship: 1
            - Fleet Destroyer: 4
        - Neighbors:
          - 5500
          - 3505
          - -17658
          - 17658
        
        ## Friendly Sea Zone -5040
        - ZoneValue: 12
        - Dominance: Friendly
        - FriendlyStrength: 1811
        - City: Addis Ababa
        - AreaID: 0
        - Plots: 17
        - CenterX: 51
        - CenterY: 17
        - Units:
          - Assyria:
            - Carrier: 1
        - Neighbors:
          - 5040
          - 5416
          - 1210
        
        ## Neutral Sea Zone -100012
        - ZoneValue: 1
        - Dominance: Enemy
        - Posture: Exploit Flanks
        - EnemyStrength: 281
        - FriendlyStrength: 153
        - AreaID: 0
        - Plots: 40
        - CenterX: 68
        - CenterY: 40
        - Units:
          - Assyria:
            - Machine Gun: 1
        - Neighbors:
          - -11886
          - -14230
          - -15157
        
        ## Neutral Sea Zone -100000
        - ZoneValue: 1
        - Dominance: Enemy
        - EnemyStrength: 1190
        - AreaID: 0
        - Plots: 202
        - CenterX: 76
        - CenterY: 13
        - Units:
          - The Inca:
            - Fleet Destroyer: 2
          - Assyria:
            - Sensor Combat Ship: 1
        - Neighbors:
          - -12172
          - -10815
        
        ## Friendly Sea Zone -11886
        - ZoneValue: 2
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 315
        - FriendlyStrength: 2775
        - City: Dur-Sharrukin
        - AreaID: 63
        - Plots: 45
        - CenterX: 63
        - CenterY: 29
        - Units:
          - Assyria:
            - Mobile SAM: 1
            - Fleet Destroyer: 2
        - Neighbors:
          - -14230
          - 11886
          - -12172
          - -100012
          - 12172
        
        ## Enemy Sea Zone -15157
        - ZoneValue: 8
        - Dominance: Enemy
        - EnemyStrength: 846
        - City: Andahuaylas
        - AreaID: 0
        - Plots: 75
        - CenterX: 62
        - CenterY: 46
        - Units:
          - The Huns:
            - Ironclad: 1
            - Cruiser: 1
        - Neighbors:
          - -14230
          - 15157
          - -100012
        
        ## Enemy Sea Zone -12172
        - ZoneValue: 8
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 629
        - FriendlyStrength: 3388
        - City: Vitcos
        - AreaID: 56
        - Plots: 40
        - CenterX: 67
        - CenterY: 23
        - Units:
          - The Inca:
            - Light Tank: 1
          - Assyria:
            - Infantry: 1
        - Neighbors:
          - 1059
          - 12172
          - -11886
          - 19027
          - -100000
        
        # Events
        Events: events since you last made a decision.
        
        ## Turn 437
        
        ### 0
        - Type: CityConstructed
        - City:
          - Name: Rabat
          - Population: 28
          - ID: 1391
        - Owner: 3: Morocco
        - Building: Factory
        
        ### 1
        - Type: CityConstructed
        - City:
          - Name: Bahir Dar
          - Population: 23
          - ID: 16607
        - Owner: 3: Morocco
        - Building: Constabulary
        
        ### 2
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 20169
        - Player: 3: Morocco
        - Plots:
          - Ocean 34,13:
            - Owner: Morocco
          - Coast 35,13:
            - Owner: Morocco
          - Grass Land 36,13:
            - Owner: Morocco
            - CityID: 5500
            - Population: 28
            - IsRiver: true
            - City: Sale
            - Route: Railroad
        
        ### 3
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 19992
        - Player: 3: Morocco
        
        ### 4
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20664
        - Player: 3: Morocco
        - Plots:
          - Plains Land 36,16:
            - Owner: Morocco
            - Resource: Ivory
            - Improvement: Camp
            - Route: Railroad
          - Grass Land 36,15:
            - Owner: Morocco
            - Improvement: Village
            - Route: Railroad
        
        ### 5
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 20665
        - Player: 3: Morocco
        - Grass Land 34,22:
          - Owner: Morocco
          - Improvement: Fort
          - Route: Railroad
        
        ### 6
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20828
        - Player: 3: Morocco
        - Desert Land 36,34:
          - Owner: Morocco
          - CityID: 1391
          - Population: 28
          - City: Rabat
          - Route: Railroad
        
        ### 7
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 20884
        - Player: 3: Morocco
        - Plots:
          - Coast 55,16:
            - Owner: Assyria
          - Coast 56,16:
            - Owner: Assyria
          - Coast 57,16:
            - Owner: Assyria
          - Coast 57,15:
            - Owner: Assyria
            - Resource: Fish
        
        ### 8
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 93%
          - AI: CarrierSea
          - Unit: Carrier
          - ID: 18769
        - Player: 3: Morocco
        - Coast 35,13:
          - Owner: Morocco
        
        ### 9
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 97%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20974
        - Player: 3: Morocco
        - Coast 35,12:
          - Owner: Morocco
        
        ### 10
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Battleship
          - ID: 20925
        - Player: 3: Morocco
        - Ocean 37,11:
          - Owner: Morocco
        
        ### 11
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Work Boat
          - ID: 21315
        - Player: 4: Austria
        - Grass Land 62,37:
          - Owner: Austria
          - CityID: 14230
          - Population: 26
          - City: Nasca
          - Religion: Buddhism
          - Route: Railroad
        
        ### 12
        - Type: UnitCreated
        - UnitType: Work Boat
        - Player: 4: Austria
        - Unit:
          - Level: 1
          - AI: WorkerSea
          - Unit: Work Boat
          - ID: 21315
        - Grass Land 62,37:
          - Owner: Austria
          - CityID: 14230
          - Population: 26
          - City: Nasca
          - Religion: Buddhism
          - Route: Railroad
        
        ### 13
        - Type: CityTrained
        - WithGold: true
        - Player: 4: Austria
        - City:
          - Name: Nasca
          - Population: 26
          - ID: 14230
        - Unit:
          - Level: 1
          - AI: WorkerSea
          - Unit: Work Boat
          - ID: 21315
        
        ### 14
        - Type: CityInvestedBuilding
        - BuildingClass: Hydroelectric Power Plant
        - Invested: true
        - City:
          - Name: Vienna
          - Population: 58
          - ID: 1061
        - Player: 4: Austria
        
        ### 15
        - Type: CityInvestedBuilding
        - BuildingClass: Hydroelectric Power Plant
        - Invested: true
        - City:
          - Name: Salzburg
          - Population: 33
          - ID: 1239
        - Player: 4: Austria
        
        ### 16
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Ambassador
          - ID: 21317
        - Player: 4: Austria
        - Plains Land 16,39:
          - Owner: Austria
          - CityID: 1239
          - Population: 33
          - IsRiver: true
          - City: Salzburg
          - Resource: Aluminum
          - Religion: Buddhism
          - Route: Railroad
        
        ### 17
        - Type: UnitCreated
        - UnitType: Ambassador
        - Player: 4: Austria
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 21317
        - Plains Land 16,39:
          - Owner: Austria
          - CityID: 1239
          - Population: 33
          - IsRiver: true
          - City: Salzburg
          - Resource: Aluminum
          - Religion: Buddhism
          - Route: Railroad
        
        ### 18
        - Type: CityTrained
        - WithGold: true
        - Player: 4: Austria
        - City:
          - Name: Salzburg
          - Population: 33
          - ID: 1239
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 21317
        
        ### 19
        - Type: CityConstructed
        - City:
          - Name: Vienna
          - Population: 58
          - ID: 1061
        - Owner: 4: Austria
        - Building: Strategic Defense System
        
        ### 20
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Great Writer
          - ID: 21335
        - Player: 4: Austria
        - Plains Hills 12,42:
          - Owner: Austria
          - CityID: 1061
          - Population: 58
          - IsRiver: true
          - City: Vienna
          - Religion: Buddhism
          - Route: Railroad
        
        ### 21
        - Type: UnitCreated
        - UnitType: Great Writer
        - Player: 4: Austria
        - Unit:
          - Level: 1
          - AI: Writer
          - Unit: Great Writer
          - ID: 21335
        - Plains Hills 12,42:
          - Owner: Austria
          - CityID: 1061
          - Population: 58
          - IsRiver: true
          - City: Vienna
          - Religion: Buddhism
          - Route: Railroad
        
        ### 22
        - Type: CityConvertsReligion
        - City:
          - Owner: Austria
          - CityID: 8029
          - Population: 29
          - IsRiver: true
          - City: Sabata
          - Terrain: Grass
          - Resource: Tea
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 7
          - Y: 42
        - Owner: 4: Austria
        - Religion: Buddhism
        
        ### 23
        - Type: CityBoughtPlot
        - WithFaithCulture: true
        - Player: 4: Austria
        - City:
          - Name: Nasca
          - Population: 26
          - ID: 14230
        - Ocean 66,38:
          - Owner: Austria
        
        ### 24
        - Type: SetPopulation
        - OldPopulation: 26
        - NewPopulation: 27
        - City:
          - Owner: Austria
          - CityID: 14230
          - Population: 27
          - City: Nasca
          - Terrain: Grass
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 62
          - Y: 37
        
        ### 25
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 21106
        - Player: 4: Austria
        - Plots:
          - Plains Land 11,43:
            - Owner: Austria
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
          - Plains Hills 12,42:
            - Owner: Austria
            - CityID: 1061
            - Population: 58
            - IsRiver: true
            - City: Vienna
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 11,44:
            - Owner: Austria
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
        
        ### 26
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 21107
        - Player: 4: Austria
        - Plots:
          - Grass Land 13,40:
            - Owner: Austria
            - Improvement: Town
            - Route: Railroad
          - Grass Land 12,41:
            - Owner: Austria
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 12,42:
            - Owner: Austria
            - CityID: 1061
            - Population: 58
            - IsRiver: true
            - City: Vienna
            - Religion: Buddhism
            - Route: Railroad
        
        ### 27
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19686
        - Player: 4: Austria
        - Plots:
          - Grass Land 13,40:
            - Owner: Austria
            - Improvement: Town
            - Route: Railroad
          - Grass Land 12,41:
            - Owner: Austria
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 12,42:
            - Owner: Austria
            - CityID: 1061
            - Population: 58
            - IsRiver: true
            - City: Vienna
            - Religion: Buddhism
            - Route: Railroad
        
        ### 28
        - Type: PlayerTradeRouteCompleted
        - Domain: 2
        - OriginPlayer: 4: Austria
        - OriginCity:
          - Name: Vienna
          - Population: 58
          - ID: 1061
        - DestinationCity:
          - Name: Manila
          - Population: 23
          - ID: 1074
        - DestinationPlayer: 31
        - Connection: Food
        
        ### 29
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 21338
        - Player: 4: Austria
        - Plains Hills 12,42:
          - Owner: Austria
          - CityID: 1061
          - Population: 58
          - IsRiver: true
          - City: Vienna
          - Religion: Buddhism
          - Route: Railroad
        
        ### 30
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 4: Austria
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 21338
        - Plains Hills 12,42:
          - Owner: Austria
          - CityID: 1061
          - Population: 58
          - IsRiver: true
          - City: Vienna
          - Religion: Buddhism
          - Route: Railroad
        
        ### 31
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20890
        - Player: 4: Austria
        - Plots:
          - Desert Hills 15,39:
            - Owner: Austria
            - Improvement: Village
            - Route: Railroad
          - Grass Land 13,40:
            - Owner: Austria
            - Improvement: Town
            - Route: Railroad
          - Grass Land 12,41:
            - Owner: Austria
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 12,42:
            - Owner: Austria
            - CityID: 1061
            - Population: 58
            - IsRiver: true
            - City: Vienna
            - Religion: Buddhism
            - Route: Railroad
        
        ### 32
        - Type: EspionageState
        - SpyIndex: 5
        - SpyState: 1
        - City:
          - Owner: Assyria
          - CityID: 17658
          - Population: 18
          - City: Brussels
          - Terrain: Grass
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Land
          - X: 41
          - Y: 13
        - SpyOwner: 4: Austria
        
        ### 33
        - Type: CombatResult
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Player: 2: Assyria
          - Unit:
            - Level: 6
            - Health: 13%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 20055
        - Interceptor:
          - Damage: 443
          - Unit:
            - Level: 5
            - AI: DefenseAir
            - Unit: Jet Fighter
            - ID: 21228
          - Player: 4: Austria
        
        ### 34
        - Type: UnitKilledInCombat
        - KilledPlayer: 4: Austria
        - KillerPlayer: 2: Assyria
        - KilledUnit: Heavy Bomber
        
        ### 35
        - Type: GreatPersonExpended
        - Player: 4: Austria
        - City:
          - Owner: Austria
          - CityID: 1061
          - Population: 58
          - IsRiver: true
          - City: Vienna
          - Terrain: Plains
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Hills
          - X: 12
          - Y: 42
        - Unit:
          - Level: 1
          - AI: Writer
          - Unit: Great Writer
          - ID: 21335
        - GreatPerson: 133
        
        ### 36
        - Type: GreatWorkCreated
        - Unit:
          - Level: 1
          - AI: Writer
          - Unit: Great Writer
          - ID: 21335
        - Player: 4: Austria
        - GreatWork: Lilac
        
        ### 37
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 19684
        - Player: 4: Austria
        - Plots:
          - Grass Land 13,40:
            - Owner: Austria
            - Improvement: Town
            - Route: Railroad
          - Grass Land 12,41:
            - Owner: Austria
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 12,42:
            - Owner: Austria
            - CityID: 1061
            - Population: 58
            - IsRiver: true
            - City: Vienna
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 11,43:
            - Owner: Austria
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
          - Plains Land 11,44:
            - Owner: Austria
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
        
        ### 38
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 20242
        - Player: 4: Austria
        - Plots:
          - Grass Land 12,41:
            - Owner: Austria
            - Improvement: Village
            - Route: Railroad
          - Grass Land 13,40:
            - Owner: Austria
            - Improvement: Town
            - Route: Railroad
        
        ### 39
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 17940
        - Player: 4: Austria
        - Plots:
          - Grass Land 13,40:
            - Owner: Austria
            - Improvement: Town
            - Route: Railroad
          - Grass Land 12,41:
            - Owner: Austria
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 12,42:
            - Owner: Austria
            - CityID: 1061
            - Population: 58
            - IsRiver: true
            - City: Vienna
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 11,43:
            - Owner: Austria
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
          - Plains Land 11,44:
            - Owner: Austria
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
        
        ### 40
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 21339
        - Player: 4: Austria
        - Plains Hills 12,42:
          - Owner: Austria
          - CityID: 1061
          - Population: 58
          - IsRiver: true
          - City: Vienna
          - Religion: Buddhism
          - Route: Railroad
        
        ### 41
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 4: Austria
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 21339
        - Plains Hills 12,42:
          - Owner: Austria
          - CityID: 1061
          - Population: 58
          - IsRiver: true
          - City: Vienna
          - Religion: Buddhism
          - Route: Railroad
        
        ### 42
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 21339
        - Player: 4: Austria
        - Plots:
          - Grass Land 12,41:
            - Owner: Austria
            - Improvement: Village
            - Route: Railroad
          - Grass Land 13,40:
            - Owner: Austria
            - Improvement: Town
            - Route: Railroad
        
        ### 43
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Defense
          - Unit: Rifleman
          - ID: 16473
        - Player: 5: Indonesia
        - Plots:
          - Grass Land 68,12:
            - Owner: Indonesia
            - Resource: Nutmeg
            - Improvement: Plantation
          - Coast 68,11:
            - Owner: Indonesia
            - Improvement: Kampong
        
        ### 44
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 20737
        - Player: 5: Indonesia
        - Plots:
          - Coast 69,10:
            - Owner: Indonesia
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 69,11:
            - Owner: Indonesia
        
        ### 45
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 2422
        - Player: 5: Indonesia
        - Tundra Hills 23,2:
          - Owner: Indonesia
          - Resource: Jade
          - Improvement: Quarry
          - Route: Road
        
        ### 46
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Rifleman
          - ID: 21112
        - Player: 5: Indonesia
        - Coast 25,4:
          - Owner: Indonesia
          - Resource: Fish
          - Improvement: Fishing Boats
        
        ### 47
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Ironclad
          - ID: 21361
        - Player: 6: The Huns
        - Tundra Land 62,46:
          - Owner: The Huns
          - CityID: 15157
          - Population: 21
          - City: Andahuaylas
          - Route: Railroad
        
        ### 48
        - Type: UnitCreated
        - UnitType: Ironclad
        - Player: 6: The Huns
        - Unit:
          - Level: 1
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 21361
        - Tundra Land 62,46:
          - Owner: The Huns
          - CityID: 15157
          - Population: 21
          - City: Andahuaylas
          - Route: Railroad
        
        ### 49
        - Type: CityTrained
        - Player: 6: The Huns
        - City:
          - Name: Andahuaylas
          - Population: 21
          - ID: 15157
        - Unit:
          - Level: 1
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 21361
        
        ### 50
        - Type: PlayerTradeRouteCompleted
        - Domain: 2
        - OriginPlayer: 6: The Huns
        - DestinationCity:
          - Name: Vienna
          - Population: 58
          - ID: 1061
        - DestinationPlayer: 4: Austria
        - OriginCity:
          - Name: Attila's Court
          - Population: 25
          - ID: 1063
        - Connection: Food
        
        ### 51
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 21361
        - Player: 6: The Huns
        - Promotions:
          - Hull I
          - Hull II
          - Hull III
        
        ### 52
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Cruiser
          - ID: 21198
        - Player: 6: The Huns
        - Coast 61,45:
          - Owner: The Huns
        
        ### 53
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 21361
        - Player: 6: The Huns
        - Coast 62,45:
          - Owner: The Huns
        
        ### 54
        - Type: CityConvertsReligion
        - City:
          - Owner: Poland
          - CityID: 18891
          - Population: 24
          - City: Dublin
          - Terrain: Tundra
          - Religion: Catholicism
          - Route: Railroad
          - Plot: Land
          - X: 43
          - Y: 47
        - Owner: 7: Poland
        - Religion: Catholicism
        
        ### 55
        - Type: CityEventChoiceActivated
        - City:
          - Name: Atico
          - Population: 22
          - ID: 17205
        - Player: 4: Austria
        - Choice: 83
        
        ### 56
        - Type: EspionageResult
        - SpyResult: Detected
        - SourcePlayer: 7: Poland
        - TargetPlayer: 4: Austria
        - City:
          - Owner: Austria
          - CityID: 17205
          - Population: 22
          - City: Atico
          - Terrain: Plains
          - Route: Railroad
          - Plot: Land
          - X: 54
          - Y: 41
        
        ### 57
        - Type: EspionageState
        - SpyIndex: 1
        - SpyState: 1
        - City:
          - Owner: Austria
          - CityID: 1239
          - Population: 33
          - IsRiver: true
          - City: Salzburg
          - Terrain: Plains
          - Resource: Aluminum
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 16
          - Y: 39
        - SpyOwner: 7: Poland
        
        ## Turn 438
        
        ### 0
        - Type: CombatResult
        - Grass Land 61,25:
          - Owner: Assyria
          - IsRiver: true
          - Resource: Cattle
          - Improvement: Pasture
          - Route: Railroad
        - Attacker:
          - RemainingHP: 52
          - Damage: 108
        - Defender:
          - RemainingHP: 14
          - Damage: 14
          - Player: 2: Assyria
          - Unit:
            - Level: 4
            - AI: Ranged
            - Unit: Machine Gun
            - ID: 14535
        
        ### 1
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 2: Assyria
        - OldImprovement: Citadel
        - NewImprovement: Citadel
        - Plains Land 63,28:
          - Owner: Assyria
          - Resource: Cocoa
          - Improvement: Citadel
        
        ### 2
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 2: Assyria
        - OldImprovement: Plantation
        - NewImprovement: Plantation
        - Grass Land 60,28:
          - Owner: Assyria
          - Resource: Cocoa
          - Improvement: Plantation
        
        ### 3
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: FastAttack
          - Unit: Infantry
          - ID: 21246
        - Player: 63: Barbarians
        - Coast 63,27:
          - Owner: Assyria
          - Resource: Fish
          - Improvement: Fishing Boats
        
        ### 4
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: FastAttack
          - Unit: Infantry
          - ID: 21249
        - Player: 63: Barbarians
        - Coast 59,27:
          - Owner: Assyria
        
        ### 5
        - Type: CityConvertsReligion
        - City:
          - Owner: The Inca
          - CityID: 1723
          - Population: 34
          - IsRiver: true
          - City: Ollantaytambo
          - Terrain: Plains
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Land
          - X: 6
          - Y: 10
        - Owner: 0: The Inca
        - Religion: Hinduism
        
        ### 6
        - Type: CityConvertsReligion
        - City:
          - Owner: The Inca
          - CityID: 1723
          - Population: 34
          - IsRiver: true
          - City: Ollantaytambo
          - Terrain: Plains
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Land
          - X: 6
          - Y: 10
        - Owner: 0: The Inca
        - Religion: Hinduism
        
        ### 7
        - Type: CityConvertsReligion
        - City:
          - Owner: Assyria
          - CityID: 11886
          - Population: 26
          - City: Dur-Sharrukin
          - Terrain: Grass
          - Resource: Rice
          - Religion: Eastern Orthodoxy
          - Route: Railroad
          - Plot: Land
          - X: 62
          - Y: 28
        - Owner: 2: Assyria
        - Religion: Eastern Orthodoxy
        
        ### 8
        - Type: CityConvertsReligion
        - City:
          - Owner: Assyria
          - CityID: 11886
          - Population: 26
          - City: Dur-Sharrukin
          - Terrain: Grass
          - Resource: Rice
          - Religion: Eastern Orthodoxy
          - Route: Railroad
          - Plot: Land
          - X: 62
          - Y: 28
        - Owner: 2: Assyria
        - Religion: Eastern Orthodoxy
        
        ### 9
        - Type: CityConvertsReligion
        - City:
          - Owner: Assyria
          - CityID: 11886
          - Population: 26
          - City: Dur-Sharrukin
          - Terrain: Grass
          - Resource: Rice
          - Religion: Eastern Orthodoxy
          - Route: Railroad
          - Plot: Land
          - X: 62
          - Y: 28
        - Owner: 2: Assyria
        - Religion: Eastern Orthodoxy
        
        ### 10
        - Type: CityConvertsReligion
        - City:
          - Owner: Austria
          - CityID: 9217
          - Population: 29
          - City: Kaunas
          - Terrain: Plains
          - Resource: Deer
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 1
          - Y: 43
        - Owner: 4: Austria
        - Religion: Buddhism
        
        ### 11
        - Type: CityConvertsReligion
        - City:
          - Owner: Poland
          - CityID: 2511
          - Population: 41
          - IsRiver: true
          - City: Wroclaw
          - Terrain: Desert
          - Religion: Catholicism
          - Route: Railroad
          - Plot: Land
          - X: 38
          - Y: 43
        - Owner: 7: Poland
        - Religion: Catholicism
        
        ### 12
        - Type: CityConvertsReligion
        - City:
          - Owner: The Inca
          - CityID: 1173
          - Population: 37
          - IsRiver: true
          - City: Tiwanaku
          - Terrain: Plains
          - Resource: Horses
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Land
          - X: 14
          - Y: 8
        - Owner: 0: The Inca
        - Religion: Hinduism
        
        ### 13
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Fighter
          - ID: 21395
        - Player: 0: The Inca
        - Tundra Hills 52,5:
          - Owner: The Inca
          - CityID: 8814
          - Population: 22
          - IsRiver: true
          - City: Arequipa
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 14
        - Type: UnitCreated
        - UnitType: Fighter
        - Player: 0: The Inca
        - Unit:
          - Level: 1
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 21395
        - Tundra Hills 52,5:
          - Owner: The Inca
          - CityID: 8814
          - Population: 22
          - IsRiver: true
          - City: Arequipa
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 15
        - Type: CityTrained
        - Player: 0: The Inca
        - City:
          - Name: Arequipa
          - Population: 22
          - ID: 8814
        - Unit:
          - Level: 1
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 21395
        
        ### 16
        - Type: CityConstructed
        - City:
          - Population: 18
          - Name: Vitcos
          - Health: -9%
          - ID: 12172
        - Owner: 0: The Inca
        - Building: Harbor
        
        ### 17
        - Type: CityConvertsReligion
        - City:
          - Owner: The Inca
          - CityID: 12788
          - Population: 31
          - City: Vatican City
          - Terrain: Desert
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Land
          - X: 4
          - Y: 19
        - Owner: 0: The Inca
        - Religion: Hinduism
        
        ### 18
        - Type: CityConvertsReligion
        - City:
          - Owner: The Inca
          - CityID: 16588
          - Population: 28
          - City: Batam
          - Terrain: Grass
          - Resource: Rice
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Land
          - X: 14
          - Y: 22
        - Owner: 0: The Inca
        - Religion: Hinduism
        
        ### 19
        - Type: EspionageState
        - SpyIndex: 9
        - SpyState: 1
        - City:
          - Owner: Assyria
          - CityID: 19027
          - Population: 14
          - City: Nippur
          - Terrain: Desert
          - Religion: Eastern Orthodoxy
          - Route: Railroad
          - Plot: Hills
          - X: 66
          - Y: 18
        - SpyOwner: 0: The Inca
        
        ### 20
        - Type: UnitPromoted
        - Unit:
          - Level: 5
          - Health: 62%
          - AI: Defense
          - Unit: Infantry
          - ID: 17028
        - Player: 0: The Inca
        - Promotion: March
        
        ### 21
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 21395
        - Player: 0: The Inca
        - Promotions:
          - Ace Pilot II
          - Ace Pilot III
          - Ace Pilot IV
        
        ### 22
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20916
        - Player: 0: The Inca
        - Plots:
          - Ocean 68,5:
            - Owner: The Inca
        
        ### 23
        - Type: CombatResult
        - Coast 67,22:
          - Owner: The Inca
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 26
          - Damage: 32
          - Unit:
            - Level: 5
            - Health: 94%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 18352
          - Player: 2: Assyria
        
        ### 24
        - Type: CombatResult
        - Tundra Land 52,3:
          - Owner: The Inca
          - IsRiver: true
          - Improvement: Farm
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 35
          - Damage: 35
          - Unit:
            - Level: 4
            - AI: Counter
            - Unit: Mobile SAM
            - ID: 19928
          - Player: 2: Assyria
        
        ### 25
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 41%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19127
        - Player: 0: The Inca
        - Plots:
          - Ocean 68,23:
            - Owner: The Inca
        
        ### 26
        - Type: CombatResult
        - Coast 67,22:
          - Owner: The Inca
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 15
          - Damage: 47
          - Player: 2: Assyria
          - Unit:
            - Level: 5
            - Health: 68%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 18352
        
        ### 27
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 62%
          - AI: Defense
          - Unit: Infantry
          - ID: 17028
        - Player: 0: The Inca
        - Plots:
          - Tundra Land 66,4:
            - Owner: The Inca
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
          - Tundra Land 65,3:
            - Owner: The Inca
            - Improvement: Village
            - Route: Railroad
        
        ### 28
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 20640
        - Player: 0: The Inca
        - Plots:
          - Tundra Land 66,4:
            - Owner: The Inca
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
          - Tundra Land 65,3:
            - Owner: The Inca
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 65,2:
            - Owner: The Inca
            - Improvement: Fort
        
        ### 29
        - Type: CombatResult
        - Coast 62,45:
          - Owner: The Huns
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 49
          - Damage: 49
          - Player: 6: The Huns
          - Unit:
            - Level: 4
            - AI: AttackSea
            - Unit: Ironclad
            - ID: 21361
        
        ### 30
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 20461
        - Player: 0: The Inca
        - Plots:
          - Coast 71,11:
            - Owner: Indonesia
          - Coast 71,10:
            - Owner: Indonesia
          - Coast 70,10:
            - Owner: Indonesia
            - Improvement: Kampong
          - Coast 69,10:
            - Owner: Indonesia
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 68,11:
            - Owner: Indonesia
            - Improvement: Kampong
        
        ### 31
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 65%
          - AI: Counter
          - Unit: Mobile SAM
          - ID: 19974
        - Player: 0: The Inca
        - Plots:
          - Tundra Land 53,3:
            - Owner: The Inca
            - IsRiver: true
            - Improvement: Farm
          - Snow Hills 54,2:
            - Owner: The Inca
            - IsRiver: true
            - Improvement: Pata-Pata
          - Tundra Land 55,2:
            - Owner: The Inca
            - IsRiver: true
        
        ### 32
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Ranged
          - Unit: Light Tank
          - ID: 18327
        - Player: 0: The Inca
        - Plots:
          - Grass Land 66,22:
            - Owner: The Inca
            - CityID: 12172
            - Population: 18
            - City: Vitcos
            - Resource: Stone
            - Route: Railroad
          - Coast 65,23:
            - Owner: The Inca
          - Coast 66,24:
            - Owner: The Inca
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 66,25:
            - Owner: The Inca
          - Coast 67,26:
            - Owner: The Inca
        
        ### 33
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Mobile SAM
          - ID: 20767
        - Player: 0: The Inca
        - Tundra Hills 67,3:
          - Owner: The Inca
        
        ### 34
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 62%
          - AI: Defense
          - Unit: Infantry
          - ID: 17028
        - Player: 0: The Inca
        - Tundra Land 66,4:
          - Owner: The Inca
          - Resource: Deer
          - Improvement: Camp
          - Route: Railroad
          - Feature: Forest
        
        ### 35
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 52%
          - AI: Defense
          - Unit: Infantry
          - ID: 17030
        - Player: 0: The Inca
        - Grass Land 63,22:
          - Owner: Assyria
          - Improvement: Village
        
        ### 36
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 2: Assyria
        - OldImprovement: Village
        - NewImprovement: Village
        - Grass Land 63,22:
          - Owner: Assyria
          - Improvement: Village
        
        ### 37
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 19%
          - AI: Defense
          - Unit: Infantry
          - ID: 17026
        - Player: 0: The Inca
        - Snow Hills 53,2:
          - Owner: The Inca
          - IsRiver: true
          - Improvement: Pata-Pata
        
        ### 38
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 41%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19127
        - Player: 0: The Inca
        
        ### 39
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 46%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20547
        - Player: 0: The Inca
        
        ### 40
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 60%
          - AI: Prophet
          - Unit: Great Prophet
          - ID: 19854
        - Player: 0: The Inca
        - Plots:
          - Plains Land 48,21:
            - Owner: Assyria
            - Improvement: Holy Site
            - Route: Railroad
          - Plains Land 49,20:
            - Owner: Assyria
            - Improvement: Village
          - Plains Land 49,19:
            - Owner: Assyria
            - Improvement: Manufactory
            - Route: Road
          - Coast 50,18:
            - Owner: Assyria
        
        ### 41
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 60%
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 19855
        - Player: 0: The Inca
        - Plots:
          - Ocean 69,14:
            - Owner: Indonesia
          - Coast 69,13:
            - Owner: Indonesia
            - Resource: Fish
            - Improvement: Fishing Boats
          - Grass Land 69,12:
            - Owner: Indonesia
            - CityID: 10815
            - Population: 20
            - City: Mataram
            - Resource: Bison
            - Route: Railroad
          - Coast 70,12:
            - Owner: Indonesia
          - Grass Land 70,11:
            - Owner: Indonesia
            - Resource: Deer
            - Improvement: Camp
            - Feature: Forest
        
        ### 42
        - Type: RebaseTo
        - Player: 0: The Inca
        - Unit:
          - Level: 7
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 18036
        - Tundra Hills 52,5:
          - Owner: The Inca
          - CityID: 8814
          - Population: 22
          - IsRiver: true
          - City: Arequipa
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 43
        - Type: UnitMoved
        - Unit:
          - Level: 7
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 18036
        - Player: 0: The Inca
        - Tundra Hills 52,5:
          - Owner: The Inca
          - CityID: 8814
          - Population: 22
          - IsRiver: true
          - City: Arequipa
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 44
        - Type: UnitBuildCompleted
        - Owner: 0: The Inca
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 18658
        - Build: Construct a Pata-Pata
        - Tundra Hills 67,3:
          - Owner: The Inca
        
        ### 45
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 2039
        - Player: 0: The Inca
        - Tundra Land 66,4:
          - Owner: The Inca
          - Resource: Deer
          - Improvement: Camp
          - Route: Railroad
          - Feature: Forest
        
        ### 46
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 9012
        - Player: 0: The Inca
        - Plots:
          - Tundra Land 66,4:
            - Owner: The Inca
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
          - Tundra Hills 67,3:
            - Owner: The Inca
        
        ### 47
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 11491
        - Player: 0: The Inca
        - Plots:
          - Tundra Land 66,2:
            - Owner: The Inca
            - Improvement: Embassy
          - Tundra Land 65,3:
            - Owner: The Inca
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 66,4:
            - Owner: The Inca
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
          - Coast 68,4:
            - Owner: The Inca
            - Resource: Fish
            - Improvement: Fishing Boats
          - Ocean 68,5:
            - Owner: The Inca
        
        ### 48
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 20956
        - Player: 0: The Inca
        
        ### 49
        - Type: PlayerDoneTurn
        - NextPlayer: 2: Assyria
        - Player: 0: The Inca
        
        ### 50
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Great Diplomat
          - ID: 21397
        - Player: 2: Assyria
        - Plains Land 61,24:
          - Owner: Assyria
          - CityID: 1059
          - Population: 34
          - IsRiver: true
          - City: Assur
          - Route: Railroad
        
        ### 51
        - Type: UnitCreated
        - UnitType: Great Diplomat
        - Player: 2: Assyria
        - Unit:
          - Level: 1
          - AI: Diplomat
          - Unit: Great Diplomat
          - ID: 21397
        - Plains Land 61,24:
          - Owner: Assyria
          - CityID: 1059
          - Population: 34
          - IsRiver: true
          - City: Assur
          - Route: Railroad
        
        ### 52
        - Type: CityEventChoiceEnded
        - City:
          - Name: Nineveh
          - Population: 33
          - ID: 1210
        - Player: 2: Assyria
        - Choice: 87
        
        ### 53
        - Type: TileOwnershipChanged
        - NewOwner: 2: Assyria
        - Coast 49,17:
          - Owner: Assyria
        
        ### 54
        - Type: CityBoughtPlot
        - WithFaithCulture: true
        - Player: 2: Assyria
        - City:
          - Name: Addis Ababa
          - Population: 32
          - ID: 5040
        - Coast 49,17:
          - Owner: Assyria
        
        ### 55
        - Type: CityConstructed
        - City:
          - Name: Harar
          - Population: 29
          - ID: 5416
        - Owner: 2: Assyria
        - Building: Research Lab
        
        ### 56
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Heavy Bomber
          - ID: 21398
        - Player: 2: Assyria
        - Grass Land 52,28:
          - Owner: Assyria
          - CityID: 11702
          - Population: 27
          - IsRiver: true
          - City: Sokoto
          - Route: Railroad
        
        ### 57
        - Type: UnitCreated
        - UnitType: Heavy Bomber
        - Player: 2: Assyria
        - Unit:
          - Level: 1
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 21398
        - Grass Land 52,28:
          - Owner: Assyria
          - CityID: 11702
          - Population: 27
          - IsRiver: true
          - City: Sokoto
          - Route: Railroad
        
        ### 58
        - Type: CityTrained
        - Player: 2: Assyria
        - City:
          - Name: Sokoto
          - Population: 27
          - ID: 11702
        - Unit:
          - Level: 1
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 21398
        
        ### 59
        - Type: CityConstructed
        - City:
          - Name: Nippur
          - Population: 14
          - ID: 19027
        - Owner: 2: Assyria
        - Building: Barracks
        
        ### 60
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 20557
        - Player: 2: Assyria
        - Plots:
          - Coast 42,10:
            - Owner: Assyria
          - Coast 42,9:
            - Owner: Assyria
          - Coast 43,8:
            - Owner: Assyria
            - Resource: Fish
            - Improvement: Fishing Boats
          - Plains Land 43,7:
            - Owner: Assyria
            - CityID: 17048
            - Population: 21
            - IsRiver: true
            - City: Gondar
            - Religion: Hinduism
            - Route: Railroad
        
        ### 61
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 21036
        - Player: 2: Assyria
        - Plots:
          - Grass Land 40,15:
            - Owner: Assyria
            - Improvement: Village
            - Route: Road
          - Plains Hills 40,16:
            - Owner: Morocco
            - Improvement: Kasbah
            - Route: Railroad
          - Desert Hills 40,17:
            - Owner: Morocco
            - CityID: 16607
            - Population: 23
            - City: Bahir Dar
            - Resource: Uranium
            - Route: Railroad
        
        ### 62
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 20220
        - Player: 2: Assyria
        - Plots:
          - Coast 40,11:
            - Owner: Assyria
          - Coast 38,11:
            - Owner: Morocco
          - Ocean 37,11:
            - Owner: Morocco
        
        ### 63
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 21090
        - Player: 2: Assyria
        - Plots:
          - Coast 55,11:
            - Owner: Assyria
          - Coast 55,12:
            - Owner: Assyria
        
        ### 64
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 20608
        - Player: 2: Assyria
        - Plots:
          - Ocean 59,31:
            - Owner: Assyria
          - Coast 60,30:
            - Owner: Assyria
        
        ### 65
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19660
        - Player: 2: Assyria
        - Plots:
          - Plains Land 62,21:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 62,22:
            - Owner: Assyria
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 61,23:
            - Owner: Assyria
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Plains Land 61,24:
            - Owner: Assyria
            - CityID: 1059
            - Population: 34
            - IsRiver: true
            - City: Assur
            - Route: Railroad
        
        ### 66
        - Type: PlayerTradeRouteCompleted
        - Domain: 2
        - OriginPlayer: 2: Assyria
        - DestinationCity:
          - Name: Nippur
          - Population: 14
          - ID: 19027
        - DestinationPlayer: 2: Assyria
        - OriginCity:
          - Name: Assur
          - Population: 34
          - ID: 1059
        - Connection: Production
        
        ### 67
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 21399
        - Player: 2: Assyria
        - Plains Land 61,24:
          - Owner: Assyria
          - CityID: 1059
          - Population: 34
          - IsRiver: true
          - City: Assur
          - Route: Railroad
        
        ### 68
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 2: Assyria
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 21399
        - Plains Land 61,24:
          - Owner: Assyria
          - CityID: 1059
          - Population: 34
          - IsRiver: true
          - City: Assur
          - Route: Railroad
        
        ### 69
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 20661
        - Player: 2: Assyria
        - Plots:
          - Coast 37,34:
            - Owner: Morocco
          - Coast 38,34:
            - Owner: Morocco
            - Resource: Oil
            - Improvement: Offshore Platform
          - Coast 39,34:
            - Owner: Morocco
          - Coast 39,33:
            - Owner: Morocco
        
        ### 70
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 20331
        - Player: 2: Assyria
        - Plots:
          - Coast 34,23:
            - Owner: Morocco
          - Coast 36,23:
            - Owner: Morocco
            - Resource: Fish
        
        ### 71
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 20398
        - Player: 2: Assyria
        - Plots:
          - Coast 57,17:
            - Owner: Assyria
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 57,18:
            - Owner: Assyria
          - Coast 56,19:
            - Owner: Assyria
            - Resource: Crab
            - Improvement: Fishing Boats
          - Plains Land 57,20:
            - Owner: Assyria
            - CityID: 1210
            - Population: 33
            - IsRiver: true
            - City: Nineveh
            - Religion: Hinduism
            - Route: Railroad
        
        ### 72
        - Type: PlayerTradeRouteCompleted
        - Domain: 0
        - OriginPlayer: 2: Assyria
        - DestinationCity:
          - Name: Mataram
          - Population: 20
          - ID: 10815
        - DestinationPlayer: 5: Indonesia
        - OriginCity:
          - Name: Nineveh
          - Population: 33
          - ID: 1210
        - Connection: Food
        
        ### 73
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Cargo Ship
          - ID: 21400
        - Player: 2: Assyria
        - Plains Land 57,20:
          - Owner: Assyria
          - CityID: 1210
          - Population: 33
          - IsRiver: true
          - City: Nineveh
          - Religion: Hinduism
          - Route: Railroad
        
        ### 74
        - Type: UnitCreated
        - UnitType: Cargo Ship
        - Player: 2: Assyria
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 21400
        - Plains Land 57,20:
          - Owner: Assyria
          - CityID: 1210
          - Population: 33
          - IsRiver: true
          - City: Nineveh
          - Religion: Hinduism
          - Route: Railroad
        
        ### 75
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20712
        - Player: 2: Assyria
        - Plots:
          - Desert Hills 65,19:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 64,19:
            - Owner: Assyria
            - Resource: Wine
            - Improvement: Embassy
            - Route: Railroad
          - Plains Land 63,19:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Desert Hills 62,19:
            - Owner: Assyria
            - Resource: Marble
            - Improvement: Quarry
            - Route: Railroad
          - Desert Hills 61,19:
            - Owner: Assyria
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 60,19:
            - Owner: Assyria
            - CityID: 1757
            - Population: 29
            - IsRiver: true
            - City: Kar-Tukulti-Ninurta
            - Religion: Hinduism
            - Route: Railroad
        
        ### 76
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 20781
        - Player: 2: Assyria
        - Plots:
          - Coast 48,31:
            - Owner: Assyria
        
        ### 77
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20782
        - Player: 2: Assyria
        - Plots:
          - Grass Land 54,22:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 53,22:
            - Owner: Assyria
            - IsRiver: true
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Grass Land 52,21:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Land 51,21:
            - Owner: Assyria
            - CityID: 5040
            - Population: 32
            - IsRiver: true
            - City: Addis Ababa
            - Religion: Eastern Orthodoxy
            - Route: Railroad
        
        ### 78
        - Type: PlayerDoTurn
        - Player: 2: Assyria
        
        ### 79
        - Type: UnitPromoted
        - Unit:
          - Level: 5
          - Health: 97%
          - AI: Paradrop
          - Unit: XCOM Squad
          - ID: 19738
        - Player: 2: Assyria
        - Promotion: Medic II
        
        ### 80
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 21398
        - Player: 2: Assyria
        - Promotions:
          - Air Targeting I
          - Air Targeting II
          - Air Penetration I
        
        ### 81
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 0: The Inca
        - OldImprovement: Farm
        - NewImprovement: Farm
        - Tundra Land 52,3:
          - Owner: The Inca
          - IsRiver: true
          - Improvement: Farm
          - Route: Railroad
        
        ### 82
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 87%
          - AI: FastAttack
          - Unit: Modern Armor
          - ID: 19408
        - Player: 2: Assyria
        - Snow Land 52,2:
          - Owner: The Inca
          - Resource: Iron
          - Improvement: Mine
        
        ### 83
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 0: The Inca
        - OldImprovement: Pasture
        - NewImprovement: Pasture
        - Tundra Land 52,6:
          - Owner: The Inca
          - Resource: Horses
          - Improvement: Pasture
          - Route: Railroad
        
        ### 84
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 0: The Inca
        - OldImprovement: Mine
        - NewImprovement: Mine
        - Snow Land 52,2:
          - Owner: The Inca
          - Resource: Iron
          - Improvement: Mine
        
        ### 85
        - Type: CombatResult
        - Snow Hills 53,2:
          - Owner: The Inca
          - IsRiver: true
          - Improvement: Pata-Pata
        - Attacker:
          - RemainingHP: 5
          - Damage: 5
        - Defender:
          - RemainingHP: 68
          - Damage: 181
          - Player: 0: The Inca
          - Unit:
            - Level: 5
            - Health: 19%
            - AI: Defense
            - Unit: Infantry
            - ID: 17026
        
        ### 86
        - Type: UnitKilledInCombat
        - KilledPlayer: 0: The Inca
        - KillerPlayer: 2: Assyria
        - KilledUnit: Infantry
        
        ### 87
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: FastAttack
          - Unit: Modern Armor
          - ID: 19408
        - Player: 2: Assyria
        - Snow Hills 53,2:
          - Owner: The Inca
          - IsRiver: true
          - Improvement: Pata-Pata
        
        ### 88
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 0: The Inca
        - OldImprovement: Mine
        - NewImprovement: Mine
        - Tundra Hills 54,5:
          - Owner: The Inca
          - IsRiver: true
          - Resource: Aluminum
          - Improvement: Mine
          - Route: Railroad
        
        ### 89
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 0: The Inca
        - OldImprovement: Quarry
        - NewImprovement: Quarry
        - Tundra Hills 53,6:
          - Owner: The Inca
          - Resource: Stone
          - Improvement: Quarry
          - Route: Railroad
        
        ### 90
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 0: The Inca
        - OldImprovement: Fort
        - NewImprovement: Fort
        - Tundra Land 54,6:
          - Owner: The Inca
          - Improvement: Fort
        
        ### 91
        - Type: UnitMoved
        - Unit:
          - Level: 7
          - AI: Ranged
          - Unit: Bazooka
          - ID: 20063
        - Player: 2: Assyria
        - Plots:
          - Tundra Land 56,7:
            - Owner: Assyria
            - CityID: 19028
            - Population: 10
            - City: Argos
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Tundra Hills 57,6:
            - Owner: Assyria
            - Improvement: Mine
            - Route: Railroad
          - Tundra Hills 56,5:
            - Owner: Assyria
            - Resource: Sheep
            - Improvement: Embassy
        
        ### 92
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Paradrop
          - Unit: XCOM Squad
          - ID: 19738
        - Player: 2: Assyria
        - Plots:
          - Tundra Land 55,4:
            - Owner: The Inca
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
          - Tundra Land 54,3:
            - Owner: The Inca
            - IsRiver: true
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
        
        ### 93
        - Type: CombatResult
        - Tundra Land 55,2:
          - Owner: The Inca
          - IsRiver: true
        - Attacker:
          - RemainingHP: 26
          - Damage: 26
        - Defender:
          - RemainingHP: 44
          - Damage: 79
          - Player: 0: The Inca
          - Unit:
            - Level: 3
            - Health: 65%
            - AI: Counter
            - Unit: Mobile SAM
            - ID: 19974
        
        ### 94
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Paradrop
          - Unit: XCOM Squad
          - ID: 19599
        - Player: 2: Assyria
        - Plots:
          - Plains Land 54,8:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Tundra Hills 54,7:
            - Owner: Assyria
            - Improvement: Mine
            - Route: Railroad
          - Tundra Land 54,6:
            - Owner: The Inca
            - Improvement: Fort
          - Tundra Hills 54,5:
            - Owner: The Inca
            - IsRiver: true
            - Resource: Aluminum
            - Improvement: Mine
            - Route: Railroad
          - Tundra Land 54,4:
            - Owner: The Inca
            - IsRiver: true
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Tundra Hills 53,4:
            - Owner: The Inca
            - IsRiver: true
            - Improvement: Pata-Pata
            - Route: Railroad
        
        ### 95
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Counter
          - Unit: Mobile SAM
          - ID: 19280
        - Player: 2: Assyria
        - Tundra Hills 51,3:
          - Owner: The Inca
          - Improvement: Pata-Pata
          - Route: Railroad
        
        ### 96
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 0: The Inca
        - OldImprovement: Pata-Pata
        - NewImprovement: Pata-Pata
        - Tundra Hills 51,3:
          - Owner: The Inca
          - Improvement: Pata-Pata
          - Route: Railroad
        
        ### 97
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: CitySpecial
          - Unit: Siege Tower
          - ID: 4209
        - Player: 2: Assyria
        - Plains Land 57,20:
          - Owner: Assyria
          - CityID: 1210
          - Population: 33
          - IsRiver: true
          - City: Nineveh
          - Religion: Hinduism
          - Route: Railroad
        
        ### 98
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Battleship
          - ID: 18538
        - Player: 2: Assyria
        - Plots:
          - Coast 47,24:
            - Owner: Assyria
            - Resource: Oil
            - Improvement: Offshore Platform
          - Coast 46,23:
            - Owner: Assyria
          - Coast 46,22:
            - Owner: Assyria
        
        ### 99
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 83%
          - AI: AttackSea
          - Unit: Sensor Combat Ship
          - ID: 21146
        - Player: 2: Assyria
        - Plots:
          - Coast 47,25:
            - Owner: Assyria
          - Coast 47,24:
            - Owner: Assyria
            - Resource: Oil
            - Improvement: Offshore Platform
          - Coast 46,23:
            - Owner: Assyria
          - Coast 46,22:
            - Owner: Assyria
        
        ### 100
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: AttackSea
          - Unit: Sensor Combat Ship
          - ID: 20967
        - Player: 2: Assyria
        - Plots:
          - Coast 48,27:
            - Owner: Assyria
          - Coast 48,26:
            - Owner: Assyria
          - Coast 47,25:
            - Owner: Assyria
          - Coast 47,24:
            - Owner: Assyria
            - Resource: Oil
            - Improvement: Offshore Platform
          - Coast 46,23:
            - Owner: Assyria
          - Coast 46,22:
            - Owner: Assyria
        
        ### 101
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: AttackSea
          - Unit: Sensor Combat Ship
          - ID: 21089
        - Player: 2: Assyria
        - Coast 41,12:
          - Owner: Assyria
        
        ### 102
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: AttackSea
          - Unit: Sensor Combat Ship
          - ID: 20711
        - Player: 2: Assyria
        - Coast 42,12:
          - Owner: Assyria
        
        ### 103
        - Type: CombatResult
        - Grass Land 61,26:
          - Owner: Assyria
          - IsRiver: true
          - Improvement: Village
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 17
          - Damage: 125
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 13%
            - AI: FastAttack
            - Unit: Infantry
            - ID: 21250
        
        ### 104
        - Type: UnitKilledInCombat
        - KilledPlayer: 63: Barbarians
        - KillerPlayer: 2: Assyria
        - KilledUnit: Infantry
        
        ### 105
        - Type: CombatResult
        - Grass Land 66,22:
          - Owner: The Inca
          - CityID: 12172
          - Population: 18
          - City: Vitcos
          - Resource: Stone
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 48
          - Damage: 145
          - Player: 0: The Inca
        
        ### 106
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Paradrop
          - Unit: XCOM Squad
          - ID: 19927
        - Player: 2: Assyria
        - Plots:
          - Grass Hills 58,25:
            - Owner: Assyria
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Plains Land 58,26:
            - Owner: Assyria
            - CityID: 1554
            - Population: 31
            - IsRiver: true
            - City: Nimrud
            - Religion: Hinduism
            - Route: Railroad
        
        ### 107
        - Type: CombatResult
        - Grass Hills 59,26:
          - Owner: Assyria
          - Resource: Iron
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 11
          - Damage: 11
        - Defender:
          - RemainingHP: 64
          - Damage: 70
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 95%
            - AI: FastAttack
            - Unit: Infantry
            - ID: 21255
        
        ### 108
        - Type: CombatResult
        - Grass Land 66,22:
          - Owner: The Inca
          - CityID: 12172
          - Population: 18
          - City: Vitcos
          - Resource: Stone
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 45
          - Damage: 190
          - Player: 0: The Inca
        
        ### 109
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 86%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14535
        - Player: 2: Assyria
        - Plots:
          - Grass Land 61,26:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 61,27:
            - Owner: Assyria
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
        
        ### 110
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 20606
        - Player: 2: Assyria
        - Plots:
          - Plains Land 61,24:
            - Owner: Assyria
            - CityID: 1059
            - Population: 34
            - IsRiver: true
            - City: Assur
            - Route: Railroad
          - Grass Land 61,25:
            - Owner: Assyria
            - IsRiver: true
            - Resource: Cattle
            - Improvement: Pasture
            - Route: Railroad
        
        ### 111
        - Type: CombatResult
        - Coast 63,27:
          - Owner: Assyria
          - Resource: Fish
          - Improvement: Fishing Boats
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 55
          - Damage: 55
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - AI: FastAttack
            - Unit: Infantry
            - ID: 21246
        
        ### 112
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 20606
        - Player: 2: Assyria
        - Grass Land 61,26:
          - Owner: Assyria
          - IsRiver: true
          - Improvement: Village
          - Route: Railroad
        
        ### 113
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 21309
        - Player: 2: Assyria
        - Plots:
          - Desert Land 60,20:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 60,21:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Grass Land 60,22:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
          - Grass Land 60,23:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Plains Land 61,24:
            - Owner: Assyria
            - CityID: 1059
            - Population: 34
            - IsRiver: true
            - City: Assur
            - Route: Railroad
          - Grass Land 61,25:
            - Owner: Assyria
            - IsRiver: true
            - Resource: Cattle
            - Improvement: Pasture
            - Route: Railroad
        
        ### 114
        - Type: CombatResult
        - Coast 63,27:
          - Owner: Assyria
          - Resource: Fish
          - Improvement: Fishing Boats
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 70
          - Damage: 125
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 56%
            - AI: FastAttack
            - Unit: Infantry
            - ID: 21246
        
        ### 115
        - Type: UnitKilledInCombat
        - KilledPlayer: 63: Barbarians
        - KillerPlayer: 2: Assyria
        - KilledUnit: Infantry
        
        ### 116
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Bazooka
          - ID: 20823
        - Player: 2: Assyria
        - Plots:
          - Plains Land 60,21:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Desert Land 60,20:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 60,19:
            - Owner: Assyria
            - CityID: 1757
            - Population: 29
            - IsRiver: true
            - City: Kar-Tukulti-Ninurta
            - Religion: Hinduism
            - Route: Railroad
          - Desert Hills 61,19:
            - Owner: Assyria
            - Improvement: Mine
            - Route: Railroad
        
        ### 117
        - Type: CombatResult
        - Grass Land 63,22:
          - Owner: Assyria
          - Improvement: Village
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 48
          - Damage: 82
          - Player: 0: The Inca
          - Unit:
            - Level: 4
            - Health: 72%
            - AI: Defense
            - Unit: Infantry
            - ID: 17030
        
        ### 118
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 69%
          - AI: Counter
          - Unit: Mobile SAM
          - ID: 19331
        - Player: 2: Assyria
        - Plots:
          - Desert Hills 62,19:
            - Owner: Assyria
            - Resource: Marble
            - Improvement: Quarry
            - Route: Railroad
          - Desert Hills 61,19:
            - Owner: Assyria
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 60,19:
            - Owner: Assyria
            - CityID: 1757
            - Population: 29
            - IsRiver: true
            - City: Kar-Tukulti-Ninurta
            - Religion: Hinduism
            - Route: Railroad
        
        ### 119
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14534
        - Player: 2: Assyria
        - Plots:
          - Grass Land 60,23:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Plains Land 61,23:
            - Owner: Assyria
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 62,22:
            - Owner: Assyria
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 61,21:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 62,21:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 63,20:
            - Owner: Assyria
            - Improvement: Mine
            - Route: Railroad
        
        ### 120
        - Type: CombatResult
        - Grass Land 63,22:
          - Owner: Assyria
          - Improvement: Village
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 27
          - Damage: 109
          - Player: 0: The Inca
          - Unit:
            - Level: 4
            - Health: 34%
            - AI: Defense
            - Unit: Infantry
            - ID: 17030
        
        ### 121
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14536
        - Player: 2: Assyria
        - Plots:
          - Plains Land 61,23:
            - Owner: Assyria
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 62,22:
            - Owner: Assyria
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 61,21:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
        
        ### 122
        - Type: CombatResult
        - Grass Land 63,22:
          - Owner: Assyria
          - Improvement: Village
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 16
          - Damage: 125
          - Player: 0: The Inca
          - Unit:
            - Level: 4
            - Health: 12%
            - AI: Defense
            - Unit: Infantry
            - ID: 17030
        
        ### 123
        - Type: UnitKilledInCombat
        - KilledPlayer: 0: The Inca
        - KillerPlayer: 2: Assyria
        - KilledUnit: Infantry
        
        ### 124
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 57%
          - AI: AttackSea
          - Unit: Sensor Combat Ship
          - ID: 20968
        - Player: 2: Assyria
        - Coast 66,20:
          - Owner: Assyria
        
        ### 125
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Counter
          - Unit: Mobile SAM
          - ID: 18358
        - Player: 2: Assyria
        - Desert Land 65,21:
          - Owner: Assyria
          - Improvement: Fort
          - Route: Railroad
        
        ### 126
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 73%
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 20607
        - Player: 2: Assyria
        - Plots:
          - Desert Land 65,20:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Citadel
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 65,21:
            - Owner: Assyria
            - Improvement: Fort
            - Route: Railroad
          - Desert Land 66,21:
            - Owner: The Inca
            - Improvement: Landmark
        
        ### 127
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Sensor Combat Ship
          - ID: 21035
        - Player: 2: Assyria
        - Plots:
          - Coast 66,16:
            - Owner: Assyria
          - Coast 67,16:
            - Owner: Assyria
            - Feature: Atoll
          - Ocean 67,15:
            - Owner: Indonesia
          - Ocean 68,14:
            - Owner: Indonesia
          - Coast 68,13:
            - Owner: Indonesia
            - Improvement: Kampong
        
        ### 128
        - Type: CombatResult
        - Grass Land 69,12:
          - Owner: Indonesia
          - CityID: 10815
          - Population: 20
          - City: Mataram
          - Resource: Bison
          - Route: Railroad
        - Attacker:
          - RemainingHP: 17
          - Damage: 17
        - Defender:
          - RemainingHP: 36
          - Damage: 36
          - Player: 5: Indonesia
        
        ### 129
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 53%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 18352
        - Player: 2: Assyria
        - Plots:
          - Coast 67,21:
            - Owner: The Inca
            - Feature: Atoll
          - Coast 67,20:
            - Owner: Assyria
          - Coast 67,19:
            - Owner: Assyria
          - Coast 67,18:
            - Owner: Assyria
            - Resource: Fish
            - Improvement: Fishing Boats
          - Desert Hills 66,18:
            - Owner: Assyria
            - CityID: 19027
            - Population: 14
            - City: Nippur
            - Religion: Eastern Orthodoxy
            - Route: Railroad
        
        ### 130
        - Type: CombatResult
        - Coast 59,27:
          - Owner: Assyria
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 65
          - Damage: 65
          - Unit:
            - Level: 1
            - AI: FastAttack
            - Unit: Infantry
            - ID: 21249
          - Player: 63: Barbarians
        
        ### 131
        - Type: CombatResult
        - Coast 59,27:
          - Owner: Assyria
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 60
          - Damage: 125
          - Unit:
            - Level: 1
            - Health: 48%
            - AI: FastAttack
            - Unit: Infantry
            - ID: 21249
          - Player: 63: Barbarians
        
        ### 132
        - Type: UnitKilledInCombat
        - KilledPlayer: 63: Barbarians
        - KillerPlayer: 2: Assyria
        - KilledUnit: Infantry
        
        ### 133
        - Type: CombatResult
        - Tundra Hills 52,5:
          - Owner: The Inca
          - CityID: 8814
          - Population: 22
          - IsRiver: true
          - City: Arequipa
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 29
          - Damage: 29
        - Defender:
          - RemainingHP: 29
          - Damage: 29
          - Player: 0: The Inca
          - Unit:
            - Level: 4
            - AI: DefenseAir
            - Unit: Fighter
            - ID: 21395
        
        ### 134
        - Type: CombatResult
        - Tundra Hills 52,5:
          - Owner: The Inca
          - CityID: 8814
          - Population: 22
          - IsRiver: true
          - City: Arequipa
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 32
          - Damage: 32
        - Defender:
          - RemainingHP: 22
          - Damage: 51
          - Player: 0: The Inca
          - Unit:
            - Level: 4
            - Health: 71%
            - AI: DefenseAir
            - Unit: Fighter
            - ID: 21395
        
        ### 135
        - Type: CombatResult
        - Tundra Hills 52,5:
          - Owner: The Inca
          - CityID: 8814
          - Population: 22
          - IsRiver: true
          - City: Arequipa
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 34
          - Damage: 45
        - Defender:
          - RemainingHP: 31
          - Damage: 31
          - Player: 0: The Inca
        
        ### 136
        - Type: CombatResult
        - Tundra Hills 52,5:
          - Owner: The Inca
          - CityID: 8814
          - Population: 22
          - IsRiver: true
          - City: Arequipa
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 34
          - Damage: 45
        - Defender:
          - RemainingHP: 32
          - Damage: 63
          - Player: 0: The Inca
        
        ### 137
        - Type: CombatResult
        - Tundra Hills 52,5:
          - Owner: The Inca
          - CityID: 8814
          - Population: 22
          - IsRiver: true
          - City: Arequipa
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 34
          - Damage: 96
        - Defender:
          - RemainingHP: 26
          - Damage: 89
          - Player: 0: The Inca
        
        ### 138
        - Type: CombatResult
        - Coast 67,26:
          - Owner: The Inca
        - Attacker:
          - RemainingHP: 31
          - Damage: 31
        - Defender:
          - RemainingHP: 27
          - Damage: 27
          - Player: 4: Austria
          - Unit:
            - Level: 4
            - AI: DefenseAir
            - Unit: Fighter
            - ID: 20009
        
        ### 139
        - Type: CombatResult
        - Coast 67,26:
          - Owner: The Inca
        - Attacker:
          - RemainingHP: 39
          - Damage: 100
        - Defender:
          - RemainingHP: 25
          - Damage: 25
          - Player: 4: Austria
          - Unit:
            - Level: 5
            - AI: DefenseAir
            - Unit: Fighter
            - ID: 19949
        
        ### 140
        - Type: UnitKilledInCombat
        - KilledPlayer: 2: Assyria
        - KillerPlayer: 4: Austria
        - KilledUnit: Jet Fighter
        
        ### 141
        - Type: CombatResult
        - Coast 67,26:
          - Owner: The Inca
        - Attacker:
          - RemainingHP: 5
          - Damage: 18
        - Defender:
          - RemainingHP: 40
          - Damage: 40
          - Player: 0: The Inca
          - Unit:
            - Level: 2
            - AI: Ranged
            - Unit: Light Tank
            - ID: 18327
        
        ### 142
        - Type: CombatResult
        - Coast 67,26:
          - Owner: The Inca
        - Attacker:
          - RemainingHP: 5
          - Damage: 23
        - Defender:
          - RemainingHP: 51
          - Damage: 91
          - Player: 0: The Inca
          - Unit:
            - Level: 2
            - Health: 60%
            - AI: Ranged
            - Unit: Light Tank
            - ID: 18327
        
        ### 143
        - Type: CombatResult
        - Coast 67,26:
          - Owner: The Inca
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Player: 0: The Inca
          - Unit:
            - Level: 2
            - Health: 9%
            - AI: Ranged
            - Unit: Light Tank
            - ID: 18327
        - Interceptor:
          - Damage: 95
          - Unit:
            - Level: 3
            - AI: DefenseAir
            - Unit: Fighter
            - ID: 19644
          - Player: 2: Assyria
        
        ### 144
        - Type: UnitKilledInCombat
        - KilledPlayer: 2: Assyria
        - KillerPlayer: 0: The Inca
        - KilledUnit: Heavy Bomber
        
        ### 145
        - Type: CombatResult
        - Coast 67,26:
          - Owner: The Inca
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Player: 0: The Inca
          - Unit:
            - Level: 2
            - Health: 9%
            - AI: Ranged
            - Unit: Light Tank
            - ID: 18327
        - Interceptor:
          - Damage: 294
          - Unit:
            - Level: 5
            - Health: 75%
            - AI: DefenseAir
            - Unit: Fighter
            - ID: 19949
          - Player: 2: Assyria
        
        ### 146
        - Type: UnitKilledInCombat
        - KilledPlayer: 2: Assyria
        - KillerPlayer: 0: The Inca
        - KilledUnit: Heavy Bomber
        
        ### 147
        - Type: CombatResult
        - Grass Land 66,22:
          - Owner: The Inca
          - CityID: 12172
          - Population: 18
          - City: Vitcos
          - Resource: Stone
          - Route: Railroad
        - Attacker:
          - RemainingHP: 27
          - Damage: 27
        - Defender:
          - RemainingHP: 32
          - Damage: 222
          - Player: 0: The Inca
        
        ### 148
        - Type: CombatResult
        - Tundra Land 65,2:
          - Owner: The Inca
          - Improvement: Fort
        - Attacker:
          - RemainingHP: 8
          - Damage: 17
        - Defender:
          - RemainingHP: 27
          - Damage: 27
          - Player: 0: The Inca
          - Unit:
            - Level: 4
            - AI: Defense
            - Unit: Infantry
            - ID: 20640
        
        ### 149
        - Type: CombatResult
        - Tundra Land 65,2:
          - Owner: The Inca
          - Improvement: Fort
        - Attacker:
          - RemainingHP: 8
          - Damage: 60
        - Defender:
          - RemainingHP: 30
          - Damage: 57
          - Player: 0: The Inca
          - Unit:
            - Level: 4
            - Health: 78%
            - AI: Defense
            - Unit: Infantry
            - ID: 20640
        
        ### 150
        - Type: CombatResult
        - Tundra Land 65,2:
          - Owner: The Inca
          - Improvement: Fort
        - Attacker:
          - RemainingHP: 8
          - Damage: 68
        - Defender:
          - RemainingHP: 26
          - Damage: 83
          - Player: 0: The Inca
          - Unit:
            - Level: 4
            - Health: 54%
            - AI: Defense
            - Unit: Infantry
            - ID: 20640
        
        ### 151
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 80%
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 20281
        - Player: 2: Assyria
        
        ### 152
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 65%
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 20061
        - Player: 2: Assyria
        - Tundra Land 64,3:
          - Owner: The Inca
        
        ### 153
        - Type: CombatResult
        - Tundra Land 65,2:
          - Owner: The Inca
          - Improvement: Fort
        - Attacker:
          - RemainingHP: 23
          - Damage: 66
        - Defender:
          - RemainingHP: 44
          - Damage: 127
          - Player: 0: The Inca
          - Unit:
            - Level: 4
            - Health: 33%
            - AI: Defense
            - Unit: Infantry
            - ID: 20640
        
        ### 154
        - Type: UnitKilledInCombat
        - KilledPlayer: 0: The Inca
        - KillerPlayer: 2: Assyria
        - KilledUnit: Infantry
        
        ### 155
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 59%
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 20061
        - Player: 2: Assyria
        - Tundra Land 65,2:
          - Owner: The Inca
          - Improvement: Fort
        
        ### 156
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Counter
          - Unit: Mobile SAM
          - ID: 18408
        - Player: 2: Assyria
        - Tundra Land 65,4:
          - Owner: The Inca
          - Improvement: Lumber Mill
          - Route: Railroad
          - Feature: Forest
        
        ### 157
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 0: The Inca
        - OldImprovement: Lumber Mill
        - NewImprovement: Lumber Mill
        - Tundra Land 65,4:
          - Owner: The Inca
          - Improvement: Lumber Mill
          - Route: Railroad
          - Feature: Forest
        
        ### 158
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 72%
          - AI: Counter
          - Unit: Mobile SAM
          - ID: 19144
        - Player: 2: Assyria
        - Plots:
          - Tundra Land 64,4:
            - Owner: Assyria
            - Resource: Oil
            - Improvement: Oil Well
          - Tundra Land 64,3:
            - Owner: The Inca
          - Tundra Land 65,3:
            - Owner: The Inca
            - Improvement: Village
            - Route: Railroad
        
        ### 159
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 24%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20055
        - Player: 2: Assyria
        - Plots:
          - Ocean 59,31:
            - Owner: Assyria
        
        ### 160
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 52%
          - AI: AttackSea
          - Unit: Sensor Combat Ship
          - ID: 20660
        - Player: 2: Assyria
        - Plots:
          - Coast 62,30:
            - Owner: Assyria
          - Ocean 62,31:
            - Owner: Assyria
          - Ocean 63,33:
            - Owner: Austria
          - Ocean 64,34:
            - Owner: Austria
          - Coast 63,35:
            - Owner: Austria
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 63,36:
            - Owner: Austria
        
        ### 161
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 18%
          - AI: AttackSea
          - Unit: Sensor Combat Ship
          - ID: 21311
        - Player: 2: Assyria
        - Plots:
          - Ocean 59,35:
            - Owner: Austria
          - Coast 60,36:
            - Owner: Austria
            - Feature: Atoll
        
        ### 162
        - Type: CombatResult
        - Grass Hills 59,26:
          - Owner: Assyria
          - Resource: Iron
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 53
          - Damage: 123
          - Unit:
            - Level: 1
            - Health: 44%
            - AI: FastAttack
            - Unit: Infantry
            - ID: 21255
          - Player: 63: Barbarians
        
        ### 163
        - Type: CombatResult
        - Grass Land 58,27:
          - Owner: Assyria
          - Resource: Rice
          - Improvement: Manufactory
        - Attacker:
          - RemainingHP: 14
          - Damage: 14
        - Defender:
          - RemainingHP: 56
          - Damage: 80
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 76%
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 21256
        
        ### 164
        - Type: CombatResult
        - Grass Land 58,27:
          - Owner: Assyria
          - Resource: Rice
          - Improvement: Manufactory
        - Attacker:
          - RemainingHP: 14
          - Damage: 14
        - Defender:
          - RemainingHP: 20
          - Damage: 100
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 20%
            - AI: FastAttack
            - Unit: Machine Gun
            - ID: 21256
        
        ### 165
        - Type: UnitKilledInCombat
        - KilledPlayer: 63: Barbarians
        - KillerPlayer: 2: Assyria
        - KilledUnit: Machine Gun
        
        ### 166
        - Type: CombatResult
        - Grass Hills 59,26:
          - Owner: Assyria
          - Resource: Iron
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 10
          - Damage: 19
        - Defender:
          - RemainingHP: 2
          - Damage: 125
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 1%
            - AI: FastAttack
            - Unit: Infantry
            - ID: 21255
        
        ### 167
        - Type: UnitKilledInCombat
        - KilledPlayer: 63: Barbarians
        - KillerPlayer: 2: Assyria
        - KilledUnit: Infantry
        
        ### 168
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 57%
          - AI: AttackSea
          - Unit: Sensor Combat Ship
          - ID: 20968
        - Player: 2: Assyria
        - Plots:
          - Coast 67,20:
            - Owner: Assyria
          - Ocean 68,20:
            - Owner: The Inca
        
        ### 169
        - Type: TileRouteChanged
        - OldRoute: 1
        - NewRoute: 1
        - IsPillaged: true
        - Owner: 0: The Inca
        - Tundra Land 55,4:
          - Owner: The Inca
          - IsRiver: true
          - Improvement: Fort
          - Route: Railroad
        
        ### 170
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: FastAttack
          - Unit: Modern Armor
          - ID: 19989
        - Player: 2: Assyria
        - Plots:
          - Tundra Hills 56,4:
            - Owner: The Inca
            - Route: Railroad
          - Tundra Hills 56,5:
            - Owner: Assyria
            - Resource: Sheep
            - Improvement: Embassy
          - Tundra Hills 57,6:
            - Owner: Assyria
            - Improvement: Mine
            - Route: Railroad
        
        ### 171
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 20119
        - Player: 2: Assyria
        - Tundra Land 63,6:
          - Owner: Assyria
          - Resource: Deer
          - Improvement: Camp
          - Route: Railroad
          - Feature: Forest
        
        ### 172
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Counter
          - Unit: Mobile SAM
          - ID: 18732
        - Player: 2: Assyria
        - Plots:
          - Plains Land 49,5:
            - Owner: Assyria
            - Improvement: Manufactory
            - Route: Railroad
          - Plains Land 49,6:
            - Owner: Assyria
            - Improvement: Fort
            - Route: Railroad
          - Plains Hills 49,7:
            - Owner: Assyria
            - Improvement: Monolithic Church
            - Route: Railroad
          - Tundra Hills 50,8:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
          - Tundra Hills 50,9:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Snow Hills 51,9:
            - Owner: Assyria
            - Improvement: Mine
            - Route: Railroad
          - Mountain Mountain 52,9:
            - Owner: Assyria
            - Route: Railroad
          - Tundra Land 53,8:
            - Owner: Assyria
            - Improvement: Fort
            - Route: Railroad
          - Plains Land 54,8:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 55,8:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Tundra Hills 55,7:
            - Owner: Assyria
            - Resource: Copper
            - Improvement: Mine
            - Route: Railroad
          - Tundra Land 56,7:
            - Owner: Assyria
            - CityID: 19028
            - Population: 10
            - City: Argos
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Snow Hills 57,7:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 58,7:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Tundra Hills 59,6:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Landmark
            - Route: Railroad
          - Plains Land 59,5:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Tundra Land 60,4:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 61,4:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Citadel
            - Route: Railroad
          - Tundra Land 61,5:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 62,6:
            - Owner: Assyria
            - CityID: 9139
            - Population: 18
            - City: Ica
            - Religion: Hinduism
            - Route: Railroad
        
        ### 173
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 78%
          - AI: AttackSea
          - Unit: Sensor Combat Ship
          - ID: 20923
        - Player: 2: Assyria
        - Plots:
          - Coast 46,22:
            - Owner: Assyria
          - Coast 47,22:
            - Owner: Assyria
          - Coast 47,23:
            - Owner: Assyria
          - Grass Land 48,23:
            - Owner: Assyria
            - CityID: 5416
            - Population: 29
            - City: Harar
            - Resource: Rice
            - Religion: Hinduism
            - Route: Railroad
        
        ### 174
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 18%
          - AI: AttackSea
          - Unit: Sensor Combat Ship
          - ID: 21311
        - Player: 2: Assyria
        - Plots:
          - Ocean 59,35:
            - Owner: Austria
        
        ### 175
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 20118
        - Player: 2: Assyria
        - Plains Land 63,28:
          - Owner: Assyria
          - Resource: Cocoa
          - Improvement: Citadel
        
        ### 176
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 64%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16751
        - Player: 2: Assyria
        - Plots:
          - Coast 62,29:
            - Owner: Assyria
          - Grass Land 62,28:
            - Owner: Assyria
            - CityID: 11886
            - Population: 26
            - City: Dur-Sharrukin
            - Resource: Rice
            - Religion: Eastern Orthodoxy
            - Route: Railroad
        
        ### 177
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 51%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19141
        - Player: 2: Assyria
        - Plots:
          - Coast 63,29:
            - Owner: Assyria
          - Coast 62,29:
            - Owner: Assyria
          - Coast 61,29:
            - Owner: Assyria
          - Coast 60,29:
            - Owner: Assyria
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 60,30:
            - Owner: Assyria
          - Ocean 59,30:
            - Owner: Assyria
        
        ### 178
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Counter
          - Unit: Mobile SAM
          - ID: 19026
        - Player: 2: Assyria
        - Plots:
          - Tundra Land 49,3:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 50,4:
            - Owner: Assyria
            - IsRiver: true
            - Resource: Aluminum
            - Improvement: Academy
            - Route: Railroad
        
        ### 179
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Mobile SAM
          - ID: 18470
        - Player: 2: Assyria
        - Plots:
          - Tundra Hills 56,5:
            - Owner: Assyria
            - Resource: Sheep
            - Improvement: Embassy
          - Tundra Hills 56,6:
            - Owner: Assyria
            - Resource: Aluminum
            - Improvement: Mine
        
        ### 180
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 3465
        - Player: 2: Assyria
        - Plots:
          - Tundra Land 62,5:
            - Owner: Assyria
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
          - Tundra Land 61,5:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 61,4:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Citadel
            - Route: Railroad
          - Tundra Land 60,4:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 59,5:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Tundra Hills 59,6:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Landmark
            - Route: Railroad
          - Plains Land 58,7:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Snow Hills 57,7:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Tundra Land 56,7:
            - Owner: Assyria
            - CityID: 19028
            - Population: 10
            - City: Argos
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Tundra Hills 55,7:
            - Owner: Assyria
            - Resource: Copper
            - Improvement: Mine
            - Route: Railroad
          - Tundra Hills 54,7:
            - Owner: Assyria
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 54,8:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Tundra Land 53,8:
            - Owner: Assyria
            - Improvement: Fort
            - Route: Railroad
          - Tundra Land 52,8:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Snow Hills 51,9:
            - Owner: Assyria
            - Improvement: Mine
            - Route: Railroad
          - Tundra Hills 50,9:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Tundra Hills 50,8:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
          - Mountain Mountain 49,8:
            - Owner: Assyria
            - Route: Railroad
          - Grass Land 48,8:
            - Owner: Assyria
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 47,8:
            - Owner: Assyria
            - IsRiver: true
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 46,8:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 45,7:
            - Owner: Assyria
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Tundra Hills 44,7:
            - Owner: Assyria
            - Improvement: Monolithic Church
            - Route: Railroad
          - Plains Land 43,7:
            - Owner: Assyria
            - CityID: 17048
            - Population: 21
            - IsRiver: true
            - City: Gondar
            - Religion: Hinduism
            - Route: Railroad
        
        ### 181
        - Type: CombatResult
        - Coast 50,18:
          - Owner: Assyria
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 40
          - Damage: 80
          - Unit:
            - Level: 1
            - Health: 60%
            - AI: Prophet
            - Unit: Great Prophet
            - ID: 19854
          - Player: 0: The Inca
        
        ### 182
        - Type: RebaseTo
        - Player: 2: Assyria
        - Unit:
          - Level: 8
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 17050
        - Desert Hills 66,18:
          - Owner: Assyria
          - CityID: 19027
          - Population: 14
          - City: Nippur
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 183
        - Type: UnitMoved
        - Unit:
          - Level: 8
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 17050
        - Player: 2: Assyria
        - Desert Hills 66,18:
          - Owner: Assyria
          - CityID: 19027
          - Population: 14
          - City: Nippur
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 184
        - Type: RebaseTo
        - Player: 2: Assyria
        - Unit:
          - Level: 8
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 17056
        - Plains Land 61,24:
          - Owner: Assyria
          - CityID: 1059
          - Population: 34
          - IsRiver: true
          - City: Assur
          - Route: Railroad
        
        ### 185
        - Type: UnitMoved
        - Unit:
          - Level: 8
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 17056
        - Player: 2: Assyria
        - Plains Land 61,24:
          - Owner: Assyria
          - CityID: 1059
          - Population: 34
          - IsRiver: true
          - City: Assur
          - Route: Railroad
        
        ### 186
        - Type: RebaseTo
        - Player: 2: Assyria
        - Unit:
          - Level: 4
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 17113
        - Plains Land 61,24:
          - Owner: Assyria
          - CityID: 1059
          - Population: 34
          - IsRiver: true
          - City: Assur
          - Route: Railroad
        
        ### 187
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 17113
        - Player: 2: Assyria
        - Plains Land 61,24:
          - Owner: Assyria
          - CityID: 1059
          - Population: 34
          - IsRiver: true
          - City: Assur
          - Route: Railroad
        
        ### 188
        - Type: RebaseTo
        - Player: 2: Assyria
        - Unit:
          - Level: 5
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 19596
        - Grass Land 41,13:
          - Owner: Assyria
          - CityID: 17658
          - Population: 18
          - City: Brussels
          - Religion: Hinduism
          - Route: Railroad
        
        ### 189
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 19596
        - Player: 2: Assyria
        - Grass Land 41,13:
          - Owner: Assyria
          - CityID: 17658
          - Population: 18
          - City: Brussels
          - Religion: Hinduism
          - Route: Railroad
        
        ### 190
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 17728
        - Player: 2: Assyria
        - Plots:
          - Coast 56,11:
            - Owner: Assyria
          - Coast 56,10:
            - Owner: Assyria
        
        ### 191
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1935
        - Player: 2: Assyria
        - Plots:
          - Desert Land 60,20:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 60,21:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Grass Land 60,22:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
          - Grass Land 60,23:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Plains Land 61,24:
            - Owner: Assyria
            - CityID: 1059
            - Population: 34
            - IsRiver: true
            - City: Assur
            - Route: Railroad
          - Grass Land 61,25:
            - Owner: Assyria
            - IsRiver: true
            - Resource: Cattle
            - Improvement: Pasture
            - Route: Railroad
          - Grass Land 61,26:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 61,27:
            - Owner: Assyria
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 62,28:
            - Owner: Assyria
            - CityID: 11886
            - Population: 26
            - City: Dur-Sharrukin
            - Resource: Rice
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Plains Land 63,28:
            - Owner: Assyria
            - Resource: Cocoa
            - Improvement: Citadel
        
        ### 192
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 2: Assyria
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1935
        - Build: Repair an Improvement
        - Plains Land 63,28:
          - Owner: Assyria
          - Resource: Cocoa
          - Improvement: Citadel
        
        ### 193
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 11704
        - Player: 2: Assyria
        - Plots:
          - Grass Land 61,25:
            - Owner: Assyria
            - IsRiver: true
            - Resource: Cattle
            - Improvement: Pasture
            - Route: Railroad
          - Grass Land 61,26:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 60,27:
            - Owner: Assyria
            - Improvement: Farm
          - Grass Land 60,28:
            - Owner: Assyria
            - Resource: Cocoa
            - Improvement: Plantation
        
        ### 194
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1886
        - Player: 2: Assyria
        - Plots:
          - Tundra Land 61,5:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 61,4:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Citadel
            - Route: Railroad
          - Tundra Land 60,4:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 59,5:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Tundra Hills 59,6:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Landmark
            - Route: Railroad
          - Plains Land 58,7:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Snow Hills 57,7:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Tundra Hills 57,8:
            - Owner: Assyria
            - Resource: Sheep
            - Improvement: Pasture
        
        ### 195
        - Type: TileImprovementChanged
        - Owner: 2: Assyria
        - NewImprovement: Farm
        - Desert Land 48,20:
          - Owner: Assyria
          - Improvement: Farm
        
        ### 196
        - Type: BuildFinished
        - Player: 2: Assyria
        - Improvement: Farm
        - Desert Land 48,20:
          - Owner: Assyria
          - Improvement: Farm
        
        ### 197
        - Type: UnitBuildCompleted
        - Owner: 2: Assyria
        - Unit:
          - Level: 1
          - Health: 75%
          - AI: Worker
          - Unit: Worker
          - ID: 5159
        - Build: Construct a Farm
        - Desert Land 48,20:
          - Owner: Assyria
          - Improvement: Farm
        
        ### 198
        - Type: UnitBuildStart
        - Owner: 2: Assyria
        - Unit:
          - Level: 1
          - Health: 75%
          - AI: Worker
          - Unit: Worker
          - ID: 5159
        - Build: Construct a Farm
        - Desert Land 48,20:
          - Owner: Assyria
          - Improvement: Farm
        
        ### 199
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 18056
        - Player: 2: Assyria
        - Plots:
          - Coast 52,19:
            - Owner: Assyria
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 52,20:
            - Owner: Assyria
          - Grass Land 51,21:
            - Owner: Assyria
            - CityID: 5040
            - Population: 32
            - IsRiver: true
            - City: Addis Ababa
            - Religion: Eastern Orthodoxy
            - Route: Railroad
        
        ### 200
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 21310
        - Player: 2: Assyria
        - Plots:
          - Tundra Land 63,5:
            - Owner: Assyria
            - Improvement: Fort
            - Route: Railroad
          - Tundra Land 62,5:
            - Owner: Assyria
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
          - Tundra Land 62,6:
            - Owner: Assyria
            - CityID: 9139
            - Population: 18
            - City: Ica
            - Religion: Hinduism
            - Route: Railroad
        
        ### 201
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 19922
        - Player: 2: Assyria
        - Plots:
          - Ocean 53,16:
            - Owner: Assyria
          - Coast 52,17:
            - Owner: Assyria
          - Coast 52,18:
            - Owner: Assyria
        
        ### 202
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 20050
        - Player: 2: Assyria
        - Plots:
          - Coast 52,17:
            - Owner: Assyria
          - Ocean 53,16:
            - Owner: Assyria
          - Coast 52,13:
            - Owner: Assyria
        
        ### 203
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 20327
        - Player: 2: Assyria
        - Plots:
          - Ocean 51,14:
            - Owner: Assyria
          - Coast 50,15:
            - Owner: Assyria
            - Feature: Atoll
          - Ocean 50,16:
            - Owner: Assyria
          - Coast 49,17:
            - Owner: Assyria
          - Desert Hills 49,18:
            - Improvement: Monolithic Church
            - Route: Road
        
        ### 204
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 20965
        - Player: 2: Assyria
        - Plots:
          - Coast 54,14:
            - Owner: Assyria
          - Coast 53,13:
            - Owner: Assyria
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 52,13:
            - Owner: Assyria
          - Coast 52,12:
            - Owner: Assyria
            - Resource: Fish
            - Improvement: Fishing Boats
          - Plains Hills 51,11:
            - Owner: Assyria
            - Resource: Sheep
            - Improvement: Manufactory
        
        ### 205
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 21033
        - Player: 2: Assyria
        - Plots:
          - Plains Land 49,19:
            - Owner: Assyria
            - Improvement: Manufactory
            - Route: Road
          - Grass Land 50,20:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 51,20:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 51,21:
            - Owner: Assyria
            - CityID: 5040
            - Population: 32
            - IsRiver: true
            - City: Addis Ababa
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Grass Land 52,21:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Land 53,22:
            - Owner: Assyria
            - IsRiver: true
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Grass Land 54,22:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 55,22:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Land 56,22:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 56,23:
            - Owner: Assyria
            - IsRiver: true
            - Resource: Maize
            - Improvement: Farm
            - Route: Railroad
          - Grass Hills 57,24:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Grass Hills 57,25:
            - Owner: Assyria
            - Improvement: Academy
            - Route: Railroad
          - Grass Hills 58,25:
            - Owner: Assyria
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Plains Land 59,24:
            - Owner: Assyria
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 60,24:
            - Owner: Assyria
            - Resource: Cocoa
            - Improvement: Town
            - Route: Railroad
        
        ### 206
        - Type: CityConvertsReligion
        - City:
          - Owner: Assyria
          - CityID: 1059
          - Population: 34
          - IsRiver: true
          - City: Assur
          - Terrain: Plains
          - Religion: Eastern Orthodoxy
          - Route: Railroad
          - Plot: Land
          - X: 61
          - Y: 24
        - Owner: 2: Assyria
        - Religion: Eastern Orthodoxy
        
        ### 207
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 21144
        - Player: 2: Assyria
        - Plots:
          - Tundra Hills 52,10:
            - Owner: Assyria
            - CityID: 18294
            - Population: 18
            - City: Axum
            - Resource: Uranium
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Coast 52,11:
            - Owner: Assyria
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 52,12:
            - Owner: Assyria
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 51,13:
            - Owner: Assyria
        
        ### 208
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 21227
        - Player: 2: Assyria
        - Plots:
          - Coast 52,13:
            - Owner: Assyria
          - Coast 52,12:
            - Owner: Assyria
            - Resource: Fish
            - Improvement: Fishing Boats
          - Plains Hills 51,11:
            - Owner: Assyria
            - Resource: Sheep
            - Improvement: Manufactory
        
        ### 209
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 6129
        - Player: 2: Assyria
        - Tundra Hills 56,6:
          - Owner: Assyria
          - Resource: Aluminum
          - Improvement: Mine
        
        ### 210
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Bazooka
          - ID: 21401
        - Player: 2: Assyria
        - Grass Land 62,28:
          - Owner: Assyria
          - CityID: 11886
          - Population: 26
          - City: Dur-Sharrukin
          - Resource: Rice
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 211
        - Type: UnitCreated
        - UnitType: Bazooka
        - Player: 2: Assyria
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Bazooka
          - ID: 21401
        - Grass Land 62,28:
          - Owner: Assyria
          - CityID: 11886
          - Population: 26
          - City: Dur-Sharrukin
          - Resource: Rice
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 212
        - Type: UnitUpgraded
        - Player: 2: Assyria
        - OldUnit:
          - Level: 5
          - Health: 64%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16751
        - NewUnit:
          - Level: 1
          - AI: Ranged
          - Unit: Bazooka
          - ID: 21401
        
        ### 213
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 2: Assyria
        - OriginalUnit:
          - Level: 5
          - Health: 64%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16751
        - NewOwner: 2: Assyria
        - ConvertingUnit:
          - Level: 5
          - Health: 64%
          - AI: Ranged
          - Unit: Bazooka
          - ID: 21401
        
        ### 214
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 14730
        - Player: 2: Assyria
        - Coast 65,25:
          - Owner: Assyria
        
        ### 215
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 21400
        - Player: 2: Assyria
        - Grass Land 51,21:
          - Owner: Assyria
          - CityID: 5040
          - Population: 32
          - IsRiver: true
          - City: Addis Ababa
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 216
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 21399
        - Player: 2: Assyria
        - Desert Hills 60,19:
          - Owner: Assyria
          - CityID: 1757
          - Population: 29
          - IsRiver: true
          - City: Kar-Tukulti-Ninurta
          - Religion: Hinduism
          - Route: Railroad
        
        ### 217
        - Type: PlayerDoneTurn
        - NextPlayer: 3: Morocco
        - Player: 2: Assyria
        
        You, Ashurbanipal (leader of Assyria, Player 2), are making strategic decisions after turn 438.
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
    - You are Ashurbanipal, leader of Assyria (Player 2).
      
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
      - Name: Assyria
      - Uniques:
        - Unique Building: Royal Library, Replacing School of Philosophy (Requires technology: Writing)
        - Unique Building: Lamassu Gate, Replacing Walls (Requires technology: Construction)
        - Civilization Ability: When you conquer a City, gain a Technology already known by the owner, or if impossible, 20 Science, scaling with Era and the City's Population. All Great Works produce +3 Science.
      - Leader: Ashurbanipal
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
      - Robotics: An important technology for the Space Race, Robotics allows you to build the Spaceship Factory, a building which speeds the construction of Spaceship parts. It also allows you to build the Missile Cruiser, a Naval Unit capable of carrying 3 Missiles and spotting enemy Submarines.
        Completing it would unlock: Nanotechnology, Particle Physics
      - The Internet: Increases Tourism output of all cities by 50%, helping you advance toward a Cultural Victory.
        Completing it would unlock: Nanotechnology, Particle Physics, Globalization
      
      ## Policies
      - Socialist Realism (Level 3 Tenet of Ideology Order): Socialist Realism: Unlocks the Propaganda Process (converts 15% of Production into Tourism). +25% Tourism to other Civilizations following Order. +4 Production from all Great Works.
      - Iron Curtain (Level 3 Tenet of Ideology Order): Iron Curtain: Free Courthouse upon immediate City annexation. +200% Food or Production from Internal Trade Routes. City connections generate +5 Gold and Production.
      - Communism (Level 1 Tenet of Ideology Order): Communism: Gold cost of investing in buildings reduced by 25%. +20% Production when building Wonders.
      - Hero of the People (Level 1 Tenet of Ideology Order): Hero of the People: Great Person rate increases by 25%. A Great Person of your choice appears near your Capital.
      - Double Agents (Level 1 Tenet of Ideology Order): Double Agents: Receive 200 Spy Points. Gain 125 Science when you identify a foreign Spy, scaling with Era.
      - Ceremony (Continuing Tradition Branch):
        - * +1 Happiness from National Wonders with Building requirements.
        - * +25% Production toward National Wonders with Building requirements.
        - * Royal Astrologer built in Capital (+3 Science, +1 Science to all Councils, Smokehouses, and Herbalists; 1 Scientist Slot).
      - Liberty (Continuing Progress Branch):
        - * +2 Gold in every City.
        - * +25% Tile improvement rate.
        - * A Worker appears near the Capital.
      - Nobility (Continuing Fealty Branch):
        - * +1 Happiness and +2 Gold from Castles.
        - * +2 Gold from Armories.
        - * +100% Production towards Castles and Armories.
      - Trade Confederacy (Continuing Statecraft Branch):
        - * +25% Yields for International Trade Routes.
        - * Trade Routes to City-States generate +1 Influence per turn (with the target City-State) per each owned City-State Trade Route (up to +5).
      - Organization (Continuing Progress Branch):
        - * +2 Production in every City.
        - * +25% Production toward Workers and Trade Units.
        - * +1 Movement for Workers.
      - Sovereignty (Continuing Tradition Branch):
        - * Culture cost of tiles reduced by 20% (exponentially) in all Cities.
        - * Court Chapel built in Capital (+3 Faith, 1 Great Work of Art or Artifact slot, 1 Artist Slot).
      - Refinement (Continuing Artistry Branch):
        - * +2 Culture from Great Works of Art.
        - * 1 Specialist in all cities does not produce Unhappiness from Urbanization.
        - * +1 Culture from Specialists.
      - Foreign Service (Continuing Statecraft Branch):
        - * Receive 100 Spy Points.
        - * Earn Great Diplomats 50% faster.
        - * +50% Rewards from City-State Quests.
        - * +1 of every Strategic Resource for every three City-State Alliances you maintain.
      - Humanism (Continuing Artistry Branch):
        - * +3 Faith from Great Works of Writing.
        - * -25% Golden Age Points needed to trigger a Golden Age.
        - * +1 Happiness from all Guilds.
      - Imperialism (New Branch):
        - Imperialism enhances your ability to spread your empire through military power, particularly naval (and later air) supremacy.
        - Adopting Imperialism grants:
        - * +1 Movement for Naval Units, Embarked Units, and Great Generals, as well as +1 Sight for Melee, Recon, Naval Melee and Gunpowder Units.
        - * +10% Production toward Military Units, -10% Gold required for upgrades.
        - Each Imperialism policy unlocked grants:
        - * +5% Production for Military Units, -5% Gold required for upgrades.
        - Adopting all policies in Imperialism grants:
        - * Unlocks building the Pentagon.
        - * All Naval and Air units gain the Banzai! Promotion (become stronger as they take damage).
        - * Allows for the purchase of Great Admirals with Faith starting in the Industrial Era.
      - Industry (New Branch):
        - Industry provides bonuses to empires focused on Gold and Production.
        - Adopting Industry grants:
        - * +2 Trade Routes.
        - * -5% Gold needed for purchases.
        - Each Industry policy unlocked grants:
        - * -5% Gold needed for purchases.
        - Adopting all Policies in Industry grants:
        - * Unlocks building Broadway.
        - * +3 Happiness per unique owned Luxury Resource.
        - * +2 Production and Gold from Specialists.
        - * Allows for the purchase of Great Merchants with Faith starting in the Industrial Era.
  - decisions:
    - #0:
      - toolName: set-persona
      - args:
        - MinorCivWarBias: 10
        - NeutralBias: 1
        - MinorCivFriendlyBias: 1
        - GuardedBias: 1
        - DenounceWillingness: 5
        - MinorCivCompetitiveness: 1
        - Loyalty: 10
        - Friendliness: 10
        - Boldness: 5
        - WorkAgainstWillingness: 10
        - Rationale: Extremely peaceful and forgiving persona to immediately secure peace with The Inca and Indonesia. This is a critical strategic pivot: we must stop fighting the Inca so they can redirect their 26k military strength against Austria and the Huns, while we focus our offensive military power exclusively on capturing Austria's ally Okilis and attacking the Austrian front.
        - AfraidBias: 1
        - Meanness: 1
        - Chattiness: 5
        - Forgiveness: 10
        - VictoryCompetitiveness: 10
        - DiplomaticBalance: 10
        - FriendlyBias: 10
        - MinorCivNeutralBias: 1
        - WarmongerHate: 1
        - HostileBias: 1
        - WarBias: 1
        - MinorCivHostileBias: 10
        - Neediness: 1
        - WonderCompetitiveness: 1
        - DeceptiveBias: 1
        - WorkWithWillingness: 10
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: Setting maximum friendliness with Indonesia (Player 5), who is The Inca's vassal, to facilitate immediate peace negotiations and end the two-front war, allowing them to focus entirely on Austria and its vassal The Huns.
        - TargetID: 5
        - Private: 100
        - Public: 100
    - #2:
      - toolName: set-flavors
      - args:
        - Flavors:
          - NavalGrowth: 40
          - TileImprovement: 20
          - Ranged: 95
          - Nuke: 100
          - WaterConnection: 30
          - NavalTileImprovement: 35
          - Religion: 0
          - Expansion: 0
          - Espionage: 80
          - CityDefense: 30
          - Air: 100
          - Antiair: 60
          - Diplomacy: 0
          - Naval: 90
          - Gold: 30
          - Culture: 0
          - Spaceship: 0
          - Happiness: 30
          - Recon: 10
          - AirCarrier: 80
          - Wonder: 0
          - Production: 100
          - Mobile: 80
          - MilitaryTraining: 90
          - NavalRecon: 70
          - Offense: 90
          - Infrastructure: 30
          - Growth: 40
          - Science: 50
          - Mobilization: 100
          - Airlift: 100
          - Defense: 30
          - GreatPeople: 50
          - UseNuke: 95
        - GrandStrategy: Conquest
      - rationale: Prioritize high offensive capability (Offense 90, Mobile 80) to rapidly capture the Austrian ally Okilis (74,33) using our XCOM Squads and bombers, and to push into Austrian territory. Since we are securing peace with the Inca, our offensive forces will be fully concentrated on Austria, removing their city-state alliances and stopping their imminent diplomatic victory in 3 turns.
  - tokens:
    - inputTokens: 72058
    - reasoningTokens: 11648
    - outputTokens: 589
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Diplomatic Progress**
            
            My current focus is on the diplomatic victory path. I've identified that 40 votes are needed to secure it. I am actively assessing our standing and considering strategies to reach this target efficiently.
            
            **Assessing Diplomatic Threats**
            
            My immediate concern is Austria's overwhelming delegate count. They're projected to win the diplomatic victory in four turns unless I can somehow disrupt their support before then. My previous plan to involve the Inca seems to be on hold due to Attila's surrender.
            
            **Investigating Diplomatic Dynamics**
            
            I'm scrutinizing Austria's delegate count, specifically how their vassal, the Huns, contributes. If capturing the Huns' capital, Attila's Court, breaks the vassalage, it could remove their 8 votes and significantly alter the diplomatic landscape. I'm checking geographical feasibility for us to achieve this.
            
            **Evaluating Diplomatic Options**
            
            My attention is now on the Inca's strategic position. They are at war with both Austria and the Huns, and possess significant military strength. This presents a new avenue to explore for disrupting Austria's diplomatic lead, possibly by influencing the outcome of the Hunnic conflict.
            
            **Disrupting Austrian Delegates**
            
            I'm re-evaluating my approach. Despite previous attempts to alter AI behavior, Assyria is still attacking the Inca. This conflict is preventing the Inca from capturing the Hunnic capital and removing Austria's crucial delegate advantage. I need a new plan to break this cycle.
            
            **Ending Inca War**
            
            My thoughts are now consumed by ending our current conflict with the Inca. Assyria’s aggressive actions against them are counterproductive, hindering any diplomatic maneuvers. I must find a way to broker peace immediately.
            
            **Negotiating Peace**
            
            My current focus is on initiating peace with the Inca. I've identified that our ongoing war, initiated by a "total war" persona, is hindering diplomatic progress. I'm now exploring AI levers like DiplomaticBalance and Friendliness to encourage a peaceful resolution, aiming to resolve this conflict swiftly.
            
            **Adjusting Diplomatic Levers**
            
            I'm reassessing the AI's disposition towards peace. Despite a seemingly improved diplomatic balance, its extreme meanness and hostility mean it won't yield easily. I need to significantly shift its biases towards friendliness and forgiveness to secure peace with the Inca, which is crucial for our broader diplomatic strategy.
            
            **Revising Delegate Count**
            
            I've discovered a critical oversight in my delegate calculations. The Huns, as Austria's vassal, will indeed vote with them, significantly boosting their total to 53. This changes the entire strategic landscape.
            
            **Recalculating Delegate Totals**
            
            I've been reassessing Austria's delegate count and realized a crucial detail: their reported 45 delegates likely already include their vassal, the Huns. This means they can indeed outvote the combined remaining nations.
            
            **Analyzing City-State Alliances**
            
            I'm now examining Austria's city-state alliances and considering if we or our allies can flip them. The sheer influence Austria holds over Tyre, Abernethy, Okilis, and Manila is concerning. I'm assessing our available agents, Naramsin, Qingu, and Asnappar, for potential espionage missions to counter this.
            
            **Deploying Great Diplomat**
            
            I've just identified the creation of a Great Diplomat in Assur. My immediate priority is to assess if this diplomat can reach and influence Okilis, which is allied with Austria and strategically located near our cities, to counter their city-state control.
            
            **Assessing Diplomat Limitations**
            
            My current thoughts are focused on the Great Diplomat's capabilities. Despite its proximity to Okilis, I've realized we can't use it there because we're at war with the city-state. This significantly limits its immediate strategic value.
            
            **Revising Delegate Count**
            
            I've discovered a crucial oversight regarding Austria's delegate count, realizing their reported total likely includes their vassal, the Huns. This significantly alters the strategic landscape and confirms their ability to outvote us.
            
            **Analyzing Religious Votes**
            
            My current thoughts are focused on a critical detail I've overlooked: Austria, as the founder and controller of Buddhism, receives bonus delegates. Given Buddhism is the world religion, this significantly boosts their total votes.
            
            **Investigating City-State Deaths**
            
            I'm reviewing the status of several city-states, noting many have been conquered by Assyria and the Inca. This significant reduction in available city-states impacts the total delegate count needed for World Leader, yet Austria surprisingly maintains a high delegate count.
            
            **Analyzing Delegate Contributors**
            
            My focus has shifted to precisely quantifying Austria's delegate advantages. I'm calculating the contributions from their city-state alliances, vassal, and control over the world religion. Additionally, I'm analyzing the impact of active resolutions like "Austrian Sphere of Influence" to understand their full delegate potential.
            
            **Disrupting City-State Control**
            
            I've identified that Austria's "Austrian Sphere of Influence" policy has permanently secured their control over Manila and Okilis. This, coupled with their policy choices granting influence and delegate bonuses, solidifies their grip on these city-states. I'm now urgently re-evaluating our options to prevent their imminent victory in three turns.
            
            **Capturing Austrian Cities**
            
            I'm now considering a direct military approach. Several Austrian cities, specifically Eisenstadt, Nasca, and Atico, are geographically very close to our own key locations like Dur-Sharrukin and Halab. I'm investigating whether capturing these Austrian cities would directly reduce their delegate count, potentially disrupting their path to victory.
            
            **Assessing Inca Military Reach**
            
            I'm assessing the Inca's military presence near the Hunnic capital. Despite being at war, their units aren't currently positioned to capture Attila's Court, which is crucial for disrupting Austria's delegate count. I'm investigating if they can redeploy or if I can influence their actions.
            
            **Ending Inca War**
            
            I must immediately cease hostilities with the Inca. Their military is currently occupied fighting us at Arequipa and Vitcos, preventing them from engaging Austria and the Huns. Making peace will allow them to redirect their considerable forces and potentially disrupt Austria's delegate advantage.
            
            **Adjusting Persona For Peace**
            
            I'm now intensely focused on altering our persona to achieve peace with the Inca. By significantly increasing Friendliness, FriendlyBias, and Forgiveness, while drastically reducing Meanness and HostileBias, I aim to create an overwhelmingly inviting stance that the AI can't refuse, finally ending this critical conflict.
            
            **Deploying Spies For Intel**
            
            My current focus is on leveraging my spies within Austrian territory. Naramsin in Vienna and Qingu in Salzburg are positioned to gather critical intelligence, potentially revealing vulnerabilities in their diplomatic strategy or city-state control. I'm assessing what actionable information they can provide.
            
            **Capturing City-States**
            
            I'm now examining the possibility of directly capturing city-states allied with Austria, specifically Okilis. If we can seize control of it, Austria would lose its delegate advantage from that alliance, which is crucial given the impending vote. I'm assessing its defense strength and proximity to our cities.
            
            **Deploying XCOM Units**
            
            I've discovered that our XCOM squads possess the range to paratroop directly to Okilis. This offers a viable path to capture the city-state and disrupt Austria's delegate count, despite its high defense.
            
            **Paratrooping XCOMs to Okilis**
            
            My current focus is on a daring plan: paratrooping XCOM squads to Okilis. While our squad strength is lower than the city's defense, I believe supporting them with heavy bombers from Dur-Sharrukin might offer a path to capture it and deny Austria crucial delegates. I am verifying bomber range and potential city re-basing options.
            
            **Capturing Nearby Austrian Cities**
            
            I'm now evaluating the feasibility of capturing Austrian cities adjacent to our own. Eisenstadt, in particular, appears vulnerable due to its proximity to Okilis and our cities like Dur-Sharrukin, potentially disrupting their delegate count and paving a path for victory.
            
            **Leveraging Inca Offensive**
            
            I've discovered Tyre is at 73% health due to Inca aggression. If the Inca capture Tyre, and we simultaneously seize Okilis, Austria's delegate count will plummet, halting their victory. This synergistic strategy hinges on peace with the Inca first.
            
            **Securing Okilis Peace**
            
            My current focus is on capturing Okilis. With peace secured with the Inca, our high offensive stance will now direct their considerable military might, alongside our own, to take the city-state, denying Austria crucial delegates. I'm finalizing coordination for this combined assault.
            
            **Adjusting Persona and Flavors**
            
            I'm now focusing on simultaneous diplomatic and military adjustments. By shifting our persona to be extremely peaceful towards the Inca and high-handedly offensive in our military flavors, I aim to secure peace and then immediately leverage both sides for maximum impact on Austria and Okilis.
            
            **Shifting Military Flavors**
            
            I'm now ensuring our military units aggressively target Austria and Okilis by setting high Offensive flavors. The critical factor is to simultaneously implement an extremely peaceful persona towards the Inca to ensure peace is signed on the same turn, then immediately redirecting our combined forces. I'm verifying this dual strategy is achievable.
            
            **Adjusting AI Relationships**
            
            I'm now focusing on enhancing relationships with Indonesia. Since they're vassals of the Inca, improving our standing with them is crucial for fostering broader peace. My goal is to set both public and private relationships to 100, mirroring our excellent standing with the Inca, to encourage a more stable diplomatic environment.
            
            **Setting AI Relationships**
            
            I am now meticulously adjusting AI relationships, focusing on Indonesia to maximize friendliness and secure broader peace. Concurrently, I am establishing maximum hostility towards Austria and their vassal, the Huns, while maintaining strong alliances with Poland and Morocco.
            
            **Shifting AI Persona**
            
            My immediate focus is on altering our AI persona. I'm implementing an extremely peaceful and forgiving stance towards the Inca and Indonesia to secure peace, allowing them to redirect their forces against Austria and the Huns. Simultaneously, I am setting high offensive military flavors to aggressively target Okilis and Austria.
            
            **Launching XCOM Assault**
            
            I am now coordinating an immediate assault on Okilis using XCOM squads and nearby mobile units. Capturing this city-state is paramount to stripping Austria of crucial delegates and disrupting their diplomatic victory path. I'm verifying the AI's tactical disposition to ensure a swift and decisive capture.
            
            **Launching Coordinated Strike**
            
            I am now executing a two-pronged strategy. First, I am securing peace with Indonesia via relationship adjustments. Simultaneously, I am launching an all-out assault on Okilis and key Austrian cities with XCOMs and heavy bombers, aiming to cripple their delegate count and avert their imminent victory.
            
            **Refining Persona for Victory**
            
            I am now fine-tuning our persona settings to maximize our chances. With crucial relationships already set, my focus is on pushing other competitive metrics to their highest values and ensuring all biases align for a decisive diplomatic victory.
            
            **Shifting Diplomatic & Military Focus**
            
            I am now implementing the final persona and flavor adjustments. By establishing maximum friendliness with Indonesia and concurrently setting extremely high offensive military flavors, I aim to secure peace with the Inca and immediately launch a coordinated assault on Okilis and Austrian cities to secure a diplomatic victory.
            
            **Launching XCOM and Aircraft Assault**
            
            I'm now executing a high-risk, high-reward strategy. My XCOM squads and heavy bombers are launching directly at Okilis, supported by mobile units. This aggressive paratrooper assault is designed to capture the city-state and cripple Austria's delegate count before their diplomatic victory in three turns.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: nSqeaAO8QwvEzvVv
          - toolName: set-persona
          - input:
            - MinorCivWarBias: 10
            - NeutralBias: 1
            - MinorCivFriendlyBias: 1
            - GuardedBias: 1
            - DenounceWillingness: 5
            - MinorCivCompetitiveness: 1
            - Loyalty: 10
            - Friendliness: 10
            - Boldness: 5
            - WorkAgainstWillingness: 10
            - Rationale: Extremely peaceful and forgiving persona to immediately secure peace with The Inca and Indonesia. This is a critical strategic pivot: we must stop fighting the Inca so they can redirect their 26k military strength against Austria and the Huns, while we focus our offensive military power exclusively on capturing Austria's ally Okilis and attacking the Austrian front.
            - AfraidBias: 1
            - Meanness: 1
            - Chattiness: 5
            - Forgiveness: 10
            - VictoryCompetitiveness: 10
            - DiplomaticBalance: 10
            - FriendlyBias: 10
            - MinorCivNeutralBias: 1
            - WarmongerHate: 1
            - HostileBias: 1
            - WarBias: 1
            - MinorCivHostileBias: 10
            - Neediness: 1
            - WonderCompetitiveness: 1
            - DeceptiveBias: 1
            - WorkWithWillingness: 10
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a18NmhIPfrCTgunyCYFrCY7Q7mYmDcZ1k08oiC5hyatKTvuafK814L31ddc1NL9HaTXDCOj5E6F2lkVYMS7GXgl/qEt/NpFx2Nbl5T3ZOxAFBpu74khYph0xzm+QOEsmuZQiDsjs0I8jbi7mNL4L6L+2Ms1x1mXw+c2EsaBbgg5df/eDBMaKdgauhHNw41N4ugYeHPQhvR4oDuRAZSBxc7pHiXW/ETs94SXtMwgsF1vYNENBNHNWbNgtKRimy2amzzDkh+AHkoiTG+mtqPzcIcX10veSC52nAp1VHHX3UTUmk/tEuNRs/HHk6y15OmphMRVmJQ5zcFHZa5kVhHjax9JNWRqXX8XbNvTP3i3wPuR11SD+XU5Qe17QMj1E6Q92Ton186IyYcnMaqOSODCj2vRZawoQ0CP/WAxDFISkdTRK5kymxD/Mc6duVZdq8Q+OC24ugnLvbB7SrmEQU04P2VXPGx8wc6iHht/lipDpxa6siicq6uTDYMlqD+VC+sU/prjWEO329BgbyPVUftMWqXXKhJTLQV90PnDpa2ioO83OHsVFoRfIs6e+tBWFanJlu5ibW80seH8cESS/SwXOFnuPMkkYaY/jTBGCso51nF6kIaax3pf5lIF3cruJUDuxusbarju81f6DMV2AXA3x6jBr9DhDCEkA8q8wAY9X5ay/07EUDpyYx3xgUUBk5UvVdLJUyqpEBsaVVGwap2vNeTpybFY+k9fDb/MaRdjmzPy5rYN2yCY0ZsRjHaflYqY/meR307t+UepA3Rm53IfXqEvP/9fsOtLN7B8Y7XQH+l5PnaaUjzRRG280lBTvxKuiH2Yd6I1X3yPIf8Y5jYpUQ0D1dnvKDqdVs/yr6KKAYWbrCVXJFC4YQC+iS9WpJ+UNT5nU1KPeMjPmjGb7+ME8tinj1EqYaGlBB4hjIem5c6mjGy2RDQHzOx78qJw2px3WoNZAlLJfbNrHoS96v3vUkGXvW6GbqmSedmGlgHUOema13I2oXzwiePrhacGHrP26oEq2oi7WeiAu2SWdeaRsUpKoAQbIaKeF7pObIUX+oQXDdW7e/0ONAulupleXVsd1+YBDcJTYdaEgpPDVherebXlTe8EP3jduUZPcAeSWVHI6zdjd89B2+ME94U/bboIdT2rVnGbRqJGMPEQpq2vEH4uyKRgjEcxf5hojH9s3aymGYxYEZvhJ2Ux9haTL/cPwrIJE9mO2Aaq5WH9r/9NgIXvqK8tpOnFMDI1nmxqB/GcnjPFm8zCnlL7YNywOEARQLiWkZp6sWAKEoYzLKk85wlIRQG5HGDu7yLbp439eh4r3bxWmtsye38g6Ba5ed3EsD+Yp+FYruse4ytPvbDY7tHjnC2cN6JAXrByKGOhgk0y1Na1XJsuxwtEQBQbzHYRgJA2JhxfotEJi3bNl+mcI3gi3OJumv9/TCjqQHamnq/iXPimPxlbEDbqpGtS3uQxSlB+dUIgoeOk1eF/LwPsoesrzvb0Nk2PE9+O6S057I/tUG/1taUjOy2+sCPqGVKR616NsAfjFFn/Z1rG7Ha13qWBnd63j4P665t3O58V/Ydk6DZ6TsRCBhjECeXa8MbDoAE8zCfZDJMGa4Ney1YQLp5lO73lWYTo/vZ8hag9RkEIvX1cDRJrWUdQ6JXmfmTOjxxOVUemzNzSSMw81CoypSKOunKU1oxqRhNc/hISlAVVGH5B5QTkNxIcAWECj6GI7lYgTE0nV8zNykQOSHqUj2aXsdBD9iKvxguQOdloSyuSAd0W2KqNBhDTqJ/8FRcRlRQqnkxMRc1Wil6v4xwGWIvqDIizKchSsaYQKFP7J2vB2/aASR5W6GW9EHO4Gkx8T1BvtT54cWexmR5/vKAP5xmx2eEiwBNjsZMCvE2ezJhzG6OHNqDZHCfp++bk+8gkBQs7H5ylmeq5SOLv816AGRMU1QkPQc29YTQEl4dxQUPEAujzowB2aHCL2AHpZ/AMyXFv7baCl8k0o2OUPgpQqWDouWErmT+czWB3gT/1adDitG4lHF+IETJlJFs7VXq6k7N3VOWL1EsXTBPGaHMCZPNitkcq4yiDbgfM0t+NhuurklRZheOQ2ju7/AQi2Uxv1bF7ze1Eu3ktiyzGTatJIn3uuQeF4BmT/yH44pJKVhxR3IRsdIe+mjE2uBYCk4TpTNGbMSE0r/Ln14F6ouEANw7jf+mFW8Z3gA2HA80uJ2xuEQjd3GGZtXS6ez6XusebPNv4xouRKqkprws0LnbAQkBay+NQ/aDFEGssPQa3uINmdUxJGh7L/CS6n5eWakUXTVpkUImvXSBdBhVtaacasxSa7pnu0WMA4AtpLtJ8qDv8iTVa8ZDhK3NZ70jpO5SwCGP8sq4Pm/07Qzc1LIWWCsYVLTf7do5TY02kzMWu2TR8U+WnmSsyxfHLm2+c0Q2otC4hz2OCZPD/otVpLLn3bHWpT1FEo3aVjOM2d0qDXvrOCfWwdb58DE4VYF1yGAIy83Hi3J8JFRtXgifG1sZk5fI9ZdfNtg9JWaV1L1+bsWJoTXetlNwveLrS4aP8p7efMHy05yeBgqn7IA4Cn0y1xvfqtmmBLK4vpoKWUMvvMK7/xFOe1cHt6/QgkAE/KPOcbfCVcr+53YlHjRLOLGMRnVCpEBsrsC+1meHqGq3mNmz1jzFR33nU36bIMCOnbO9Pc9lj3eygnrXWC5a2uPffmn5r98poKk49SiY9lBR9eA5Fi7IawMPxrzFZni39IIxCfH/QN6lUWxmICyLyEmKrOC1Kb3zTXqdyFxB0f+OoADpJwPR/njAXnwEIMUVGMAaYOEF7gJ7xatWUwcVJQqbjjV4m5dESMbffSUBcORyTzKoFkqvM+PjwOji+eURPmY2yVLufvYY5EmixaIpAy3g0GLKtehaTfFhGHRCSD0AuvZ/5TEJWkDNW7YoVO/yf01+9cHIuwNftyEqI1CWmDJlgml5rYxjgWEz3XsW2YEdgvGobsJ19ljQxsdqCeAtPzewozLrnXFiyZKhJa3F4rj52L2k+PAcRktTZPwJer9e6/UFILjg7oXqVjklTraHnzvgXFKo/tKSCv8trWmoPWCSPTHpZZwbAhj8gnyob5PWxdsjB1S0jrcubNSo/NswYW4W7r893CSXIblTRAcqeFUD8it94tkdAGmSJkGjWkJm9BFREnql02XPq2MVSuJFkOxpmXNWMavp8C6gEqP+vbOiJQom6mxr5pDzduzAiI9LZEp9o2V0Eztv6aheDJkhtHPVHf+WKJtkhBtf9f4HrSblntAWyG4rqLz84YdNzveeEvhLsK+aUZ9uvzI1CA1rJ+Ul1VpIWkpqTZXOWWFmZsrhj6+RosST+QczGOnyq+gXLB5NDPqGL7xiHopnsOM0De1rJyolDZ4BEkZjhwpoes1imrKY5c147z7GVXUKRAAQVztfLcAx20V/M23OMb1cm/pG4blKIed8bApU9fQe3vqz3gr0o3kkIMfG8mcxr9772bpjskLXjXWlzFEm1LSd5mvNlBJwFnyo334SG1CtsG0qY55iQ+/Kf6aK94XGzbRr/3WrtmCsP+iwfq03/1bpSfFGI4LND+W4rJnDSGmIsgyBt2yl7DW7m+iJSh//gKyGwKOHYSkELf04hfWhjjbh5PKaNfUctJ3QR2XoqdSkpcdWst7AbEfvmW8N48REnUOc5phCUnUFUFItBx+Ef7FBV68dH2NZND2mcQXYK8uou6No4k3LtDDbtbHvHqzuXY8QwuN8wh+GgkRu48vd5WtKDqTEpWNi3YBryvy5GDro1QPxyYXXxGpM42lN7zGBUB9k0cIYmNRQjizg27KUHo8lbuEihuHug86DdbaIaMadMxKBEzNxNGbF0Xq6pQ+gtjtMGYBlNYypyJSmTZd7jUl2zYqeXH5JC0TtISIVHudk05eBnUfAhmY5wu8h+B+aLBtgJcAFtqt1nWOqF/iHzTJcqlcAepY25TsJVjtC7SlfU5CEZ1qycbXosayka8YpMpnGlRU9exFEuHwD3sEdot4+sdHNdlLpy6+Mu/z7+itxR4r0eJyDi7gqzUG8KM4HEWsHe1e7PXIO2PZ739+3kfJx5IA074x/ZNkjj3gGu+UpExiWXckUdnbNGm9KVVaacz468ERxo1/ITEJW7+vv7ta1bJSmM4nTvUBmO4bQ4b6HiT6lmSuaBgvOOrowgEyUMTIgUjNDgbj86KyM0oEBj83vHnltBvs9bwJNQC394sYvtqD2s4yQbmE+JsPTlKpxSr2o6nqwlXquKkYHmJtxAdMvGYGsKqrRwr9+tyWnz5rfC9xvNuE5FhwpuxZRmKRw567XaNjeg70EVQUVSc/DqEx+qe1iWj+ED/1pX7QySz+jupyBHGjIhGjkGS1kOGaDj8Nv+sj5/Jcz9hRiGpGqHjcKd8l8p++54R5uJpTETXk3XM1bP/3hD3vVlWSb+gDi/JtBtIztfE456MG9dxz4XMqoMOPGcZzd+SMAy2ypn9ZW0P+yQeCd8HCu9qBKzsArhTqXSFCCFOr10Kk0lLJF85kX++jA8BERVLPA4w3fRR+xFgkQvc+lhA3YnW6TybN/1ky6UcASN9kXf5ycZseJB2MUY3rE33qOa7+H2GrwgetH8apOkbDm+T84+ZuQ0umJtpmNFKH0TgnJBGZBGWALjXAWORqyeBJESeWdQvyBeGtQw05yYOQCAjItA9eEFcKrjYKmhwtc2FeG819U+nWikb88LC7cqjt/Nj2ML2uDU/DT0QYzMT7un0jpDXgm4/5A/XjH0mNiQ9j9uH8q8zrSZfa1cWmZurjwTQpoWpwnMB5EP0BkHedMear6Vq2GVJlKlSokRfsOGSJflb9qcx5+4P1XOuUtnnsJgddGSGfDCMX7oGKa2ZO+hst016UBJe5IvCZvi/IkeksA0Mx8kxRM8LreupANgCpzwH0lh8QLiGJCoFkTR7oKc9Z50vn9LDqdXeL/lztFeVXEOZB9N7lIq19WQumIOtT5idFWjvhxQQeXlKH+bg4lDjC8Q1r6fTpRboJPul243KntM0fMxz0Ml2+uDXkbbfIFrz1/HI02C6VDRCuDBs09JUPAEOl7i7AtUDMGCxu1cnW4GVAhEBgiakNRyCjnFWY6BQUadYeBveUAPl9zPULL8eS80zLD4GW3MvaJ9NtpkBaRglGPvuNXy4vqzaTV9cpIt882xSD5px7I+scEQqTj0JvfqQN2TFg/Cw9RDVcs/YB8bPYWm7b/hMiB5WtQ32LwziSipE2VdgMVXymIVG2jH8vuD9ApK54sUfCR3bDBK8oiA7tkGUfOlDSQqsii9dZ7ZQcQY+cMZx+QfYSSs6NNnu+SfnYvRK8NAWJ01E5rnSfqcFSpemZxz94QX3QFAIQzefV8Z3lYqJM+ddK0iIsNti00wGE65D+D3QgM/RnTXqcy4iHdmcn5FEKuX8cKJ1VnF5p95tuX13ACRJJ3pMrrngswaGejc5SYjHFqp7P/R0ITLA/pZbZAMFNAftSB5izBEu3przzKRfMlqnD2Icfe+0gOGqc3uL05dH0wQfkxyxjEp3lBOF6E9ANV9js68mFQxQPcl+f1qLHqMBvqzyxow0DXqWD4mAZwwIAjWXxiHnv8m5GRE6S1LiIHtHuBZz/HZ3dXN4lK94yz0Um3+mZa9V6IDBCHfG52109K9ouwVeMpIcCoVLZLnWpjs4oCAVI1ldxoPbjFB9+0mQ8Y4zVWoj1NG98LdSeye/3J2kyrI8Mfyp6qfprCsxxuokhSphRLbD21nk1RhnYUxuZ5ErZozpOFpP/FOHQeQ/gjqRqG8whcU0RyOoVywI9/PmecsR0z7+XxGceM9NTBwXHRzKoncSBj7KOjGal14kur4xyWiLaetRHU0qEh0ao5BWITl/WlYf8ARoySPcHW/k/5bqTKHfNz+Dt1xjkL2Vc2NdZWpN/4xrPqGR/DstpAL/QfIR9DwO2xPmTFKTxYNe4aKCmmpB7r5532hZrbUyHtOT6BZuPqccXEoLSAqReH6JjjB814nb+NRPnLPo1bViQLu9SrESzltBNzng8WYb4uivDxHQZ7HXxW+fwKDekwClBLpvfnASJbTRdrswccyNDtBCaIrnYpRm+K4+kePWAWYT0JFdSYoQFNVfJ2x7zkktkfST27Feh1dqxXZ4qBVoVMEhYUSnVTHM52g5Fjp4OL2bk9rzCWepO/RV/36cUMEY+xW4DqV29pnUJg4IgebDzp1om/N0DHiCA7aMpJkpizGDkSE53YCWcVI8LsPAh37P++24DykMpKd7JrPZXAHgeXNpZu85epdm0NOls4hxjDdWtFnMJ6gsFXbVCknRcwJ7+zPpLJ46gBU53fF4zIyuVbZHYw7R3Gt9Mbl8yDXCr6QHB9XobpEt/Eso+tUoo8cayEzg5BWQhCfH5kQ3DBUAFj6uXbO0juwgs2sXHhKGAgCpSDemCnD1UPTg2gGBOdAf78EXWXzYWUZYU/EEzb4b2akX/BOvp4v+nKq2Dyu9WoF9k5Y207rA1vOkeD583RTWyW3V49KVndTJmqwdUJebDWmk1u7cT8ddCMXwnmb9bB9xPIG4DJOKD37c0/a4jdNE3Qd94G4pzDLuX/aaEpJXErZ9DuviKysNJIHfpmzkCEI2hJCY/rGkTqucxNDK2xMMN6GXOEeq72p65HKyrf9IirtDbjkGkGY5/06Ssob+eCEHj0Y6zuxXZihdwklsmopkkEVJVZOLIFYzMXVEvev4yQCwFDmmeQx0RQCVxbyfBZA5zrBB9kkEc7fT/B1IShkEfaZhYjZvzE6/cvxFEQr2I89UArle2yw3Ln0FT2KdcvqG0Jkw2Le7/S2xGJwvyxGph92i0I1RTVQd9DHEg28D2pb0vdEjbvjURK64+WDvVWyQ7aG7pQcSjkbHzO1cXUI7lXR9P11nwvunRO0mHfhIUf6yD7YNFXGU5xrh5D5BGH0clD7AWVWbme7NFIbnTWLDHEWQkoKqDzf10ZAHCsuyen2Tq8czcs0EbxXPBILK+P/9s535h4B50UOoPAG6GROj7FiMAKb0dafv4sJd8pJEsWOlrrcDrOVIzO4KRTWcHULgcekfTlrLuKKaZMkNvE0X3Ml9fAKpSxS5gGUgHUGw6FUBFt+RNwAKcZd8QYJSOF3UZsDV36eijgiPgtj1SUY3xNPeqA35i9sF2OKjYZXOsrGvdAWoybaQdxcTg/NsCMZXY0m4yNrJX/MH74FLvaqhEouEpXgCQOb1mKoUV08leYBhaHZSOWw/P46Kr4DwKiB4dGiF2jRKSYmKGj53Lybwf2G0xVBaIsSBs4F25gkfdmI3d6S/5rgPrDIl5aLYXfX5XJInpNUe2e92Z0pmj9MtPE9y9uN8Q5yN0SJMyjM0wABb9oW3PGYYbjIZMerI+7kXD1LdVF6a7OnSiKqfsNH7Hcg8J1JmwPP8VoFntedIrJiIxffyKda/eIXCzH9feetRM2ofgumPjWswoPvQFvPuPMorsZjyoAOPzqUPqjzcRCmUKKIaiU+oFWAnGg6dkxkGT8F3woQjkxZjvnwwyu/Fyc3LULQMY1M7Sc0Yx2bY0aPcvUR51SyP4a8vc6eHyV8Z6lB+Eks0jbYXP/OVHc4/uQlzxC/tBZmF1qRCwbkqXmasZba20O1irYX6ESVLSFZ69sCyy6E4tYk+gpTWyGr42gOpqJ2z1BY0uQ+Vb04HOSeEOl+WZNC4rVrdPnFtsMujVR1wZ/ufMWEKAcw7geioTeBaoTJbeVEiZ8rma8VKnbCeCNWWtqwfexGjOMHEJm/rzdEGDWt/v/OACdiedUXW3DbfTiZlr6p6mPNaHAUvRpmto7RRMNSCz3pPDYvXzcn410r/hUSS8L3GV+pw5V7UJVde5iLAu5pq6d8dOFnRWBp3GqybbIPUYGit0xBSYqApLrRy/ksAiZIBKcnIZx1RE3EVLxT0fJ4QwRcbzSS7IJjzepidDYaKVx4x14oLlr2h/e244Le29y4spAg9T81u9SWrH4Yu8EDMC+QnRX/YR+9erY8rWMmwCT2kxcKEE0BJUe+z8su/3lw3sYGc7E2ngNGLXFNyFRAv8/f+iSHd8YwBDkiuFPFUVqDWlc/RdCsBzxWhAD/vEfiMjIDfH6Cfv5SO5iJ+7f2lNlv4bx9D7OqhPE8WMc282Uf6MrFGycEB408sMz7Ae0w4ulK81nKqqmyhW8EO2UwtZSGd+3W/CE1+Fh+mbOsIueByircEtnJWllivHAdXGddaO2Exz2XkDX3JOuWFYtDHW3NaxkzQQCf7aSY5DYLKHNj8QrvQaFM9T3KpL3BzMtYUdsJ8MhWZpFK4P9srXIdOLH5P0NwtIwOKpIMEgxeL7c/mnExLyza3ALiJfjFbY9eWewYKWFCW1WzqDL7rl6t+b8jWQO1HvnMX6wkCbA+4j+SJ9oJlBfX0/A3dywvwYwFK7+ye/Eb7fntOsWNZYb6Ci10diiNhhpjR+wYESIYd++7IZn/ORSimsFRcdOGEaqrSzkgwv1vTsZKRXAM8/Q26akNnxEDkp3+OF2eTYsLNIFP4mvqTULZcfxdkXYEbOr+50ps+Ctsqnx5R2hTj4O0ZQjDHXfyNIkN5jMT1Y7B/0yRxvDT/KYHH2zCjbi9lb1ZdhQA6PpI4PZy4F6LNVh4QsvHKYQz9q8yGBI1hO4Lttp5EpCnsWmystB9TErxVhNO5XLQ9wjGtmgtaSw+PP1AxTOBTe6TEprNQmxlvaMgYf266Kj3NEwQNy+RSOAidh1dXSHUkNkkL/rQoc4/OaIk+hS0u94kCOf+ghM3mrDBhA64xImfUg8jSRuGka4avu+pS7sQZHk1J7+3A/3P7C79WwWjh3roBN6YZH//je621BmH9wQpyRdQ7mf90oHJXwqCTc6nrVGUyxOyP2dfreMiy7Jg3ej6yZKZPNbKnVDEQFRA8o17AeltjxbuF/lrEbc/GiowgyYfAkH3K2D2hCA0DHJ3ONr1JVcXHUg4UV4lRQITMee+tbANJwVoBWuzCpDIMxcUk/ZaRTbjq6hbaKMRgLJV0tQcpJ2ltngxSzTUTmYQo3qPtNvMBli1Cn3dGDbnzObEY3cqXotq1ADLNS8EoMJAsFUclGU0xlY6fUUJjH24LV6wljwfL3YjmlDvwhpWNIZNiszhezFe18eynFSoyuW3apVU2au/NXxZD4Ahbp+Q3OZe/MISiO77e3WvV4qLqygZjBeh3NiO6RHFmGOlF8nXllnTr1rA9wm+WRbDeDgcoROWIGorYKR1DU7OFzkvVzK7EcllLT8tzjio0I7FqPUZzCI3dXBlmSHxmftYfBQyM4qNNfN9sv+zuZYqHI53RfPpHO9QVTGeZvpoSIq0/r90n/xqfPNYt0Q7koGjRI6DjWSclNgM471ABPkPvMXu2BxrhyogLJ3SFc5U5XCEhBN0dCTc+HoX0gTD7PbiKMg4jHUSNdjtHE4nVJu3liQtU3EtMh3RPvlPSAuY7WKD8JqWfHdQg8pAXO4a1MvcYO4rB+etrMi3TBEXhE5sSghS8B+Ve0R+Ep8eNfiE5biS101JdNMQrZ9iuCg2pG7FRn4u/5mszGTrgmCXntOz+6jAYZoYIj2LqSm7HzNEMuWROzSiScDBpw1Iy94BHidcrIyFO8ixROJ+gzVoFwQhjGNZ52Pu88lfuUG8RZyY5wOqJ2MSvmTs1+fAc4rRRP3PuAcii1wwVqWyrh4nhX5HMjzrTgEu3Gu66LqkqVfFT5RWsKVnEx3oNiPQ2AqXjz95rz36Eaefat1owlEH8u8FV1lXy9U3adDYBkQN9r7BhSIc2Wco8fYCH1zQ607q6vrLN8RLv3H7n4kj2o8+ehsbciVFlHVK5pEYYm2TdDiXCbC/2EbZalJr2iTQqGIjYyvQf8AupFacxCi/wCDJASJZcDcpJgpIwkHd+YAU2ZdbEmKR1XQE+wYFP+7lWxYjS6uENQm7QR0f3N841J+0oULIQ+PfUUjZ6X15WmB1+l08AR/fPxTARrzz3cQo+T8fHF/PsV/df3lJDAiy3mfNvrXIGFHZs9xWihcEKlC4IihTUZ03N3VTaNtsoWaAQqYJ1SxAzyZ5Q5NaYX2QtzHxPkyG/nM2DD93+JWig+2iCVtG02QT5MBMIt++tRegKT2uIPl17oYXXjsuaAHbJnCkLbY/5kK0pWr+2BMzO+YfiNhZ0ndwT2uGaes0j15o1Wvc7F3iUxx0fTdWopVpNT7+Nt22KryoOSeH/pneHM2Ueth2iFj0EwwMdbhXUZMO6jlUx2PU2D/1Dkjy6Ah2L6UoM/NskiW+6Bh/oFhuWbhJgxbLud+QW2HH4BAMy0Rvhdgg8CH9jlo2GA6T6TVDIuRWz60LPxf9nR75IJgA2hf55prPk5VxOzMM7/ZpS3NB4I5RBkC5RF16SNrrC5OU7WsWOcdBZ0lTH6+pQoCdpicsnVzGmfZRtOE/hPURjCG6dTGbFd3jHOnwb/iqCn8EFrfxRsP3rDfPzdxMl6U+l/Y+2Fwp4QISaea/WBTH5c9wop5ZQVkH8qQC2Mndx3qOSNFq0EEUQXWnneGxFwlzkiFMUIb0vRci/Hzh+FsrDQcPmkHDNQqkoTMlNF4b34jg0ZPcTs6KXuq2bqrXiUBN+iQti7Aw1NU6kDgZmcNgnWE6boISUtte8LsEANq/Tdzfe0Cq6f1cDN3PPyPF3LHTGRqWiiE4PwSKfeXYLEfj6zoXsv36n9B53sOSfDRT8At3sDFUSNIZLtw9XINi9D+wzSpEUlO8IVxhEjEey74W3u+NG6ZFBIDNqNpflJK8zDAf/C+8vy0bFssWwyhEE3KjYBk1vdCsZC1JCXe2eWYMyWY1wuZD5yq72UE6I/dpWBF2SXbQYJ6BYtaR5jj4J1yPKmiEMMX1xCZUQ8KzWT0DmCWbTsbBR6YRW6wrKzIHgk/DKeuC2VOCoIy+DfyjPG6LHQUbEGrhra8BYAHFF6aYuV8oWxvLuhs8pKajmCs8hBJCxFsJjRa3nISl+kR/RZIkM+Am0Nt2XAjmVZsCe3/2VHJohELlxQy9sjDrtlmlRM/A+hNOBZI9IwQKIEWKWqvdoUcE4IqBJ4zXh1dT5TCixbIRJ9xQgifNJLEqw38NF+aSSjMIGqb7ytJ7hcsJ561o8NrnjIYvDhG/NSGq90ZC1r00QL+AWsgVreAYyGaTNnjJ2+AtU0UjuCDXXoN/vXkqTDpBuze/abcdaktfzw3cmWILt6DcQ1e7IIdhcbnEXRJcbxwDQlhQ+zUy9dCRLo3g8yZz/S0QofGei9Fx1eoxUnUIkedWzEXlNBOWpMmDye/1IRkmJ8b8d6x7UKGAQr3TUvcoy4dmliJ87pyqKQYou5e4lLZvVWEkFzl3GWpWmWHwqK1N1MxHE/JdPcMYri1CqG1N7d+LodASGqEiihXfJQLuoul8NNs2DTNNnGzM9PQck1gUBDxHNKAE8vGhujerUxt49bhIdXLmTYsHTGwzshmwncoOiOrT3Ce1xpyla4o6jSdPac+qRpN+AeNANlZ/h6M5HBFQ9KIm/wTdxHlnIadhstXtowvm9lIkx8pZwoPfeD8dZA+v0ntBRmvvr8xCigOB5XxMcxPGHE+PyCpvSdWoFw3ZRyMKteww7vyB+3+rnj/w41qYq4fSguIq5TqruTOnhA9TGLrGi7gnXE4XgRe9FJ8jlKL9K3tHiQEq5v+gF1YMQGGRNuRjsEfQ5vj86+tMxcKaX6Xw+tprf6jL0g2WJbCwQ+OSwONQRflCZ36DF7q5O0b2cB9Bn6yIUjstCzuX38X9U0B7hOMO4p05feFGcUWyW4LGqo+5ocVPQ7rXq7QFc20eG060DSokO234+dVmmj195J6u92LJuT16o7/Y7pWgQRyo5ny23QN+xSy59LvpVYo2n8vpGqF7/tjl2QTLasC2mmiYmMPCyjae7Mqb4rR63CeV+JdN89jj5d7kNx/vwj0SWyjsDwsAfdp5EgFsDnJFH11vniFaXOMDTZg+6qvGAG67saf1towWQLLzuQ4I4/jtgkL53qSZQ2/UwtR6ItONAekWd5FagDsCXF+LBXNFbXF7C/a/3kphq5dqZNHDJ+VmJyabUwhCLyeTL4jyte4sDrlsACbM5/ekdNl35wDZz8BPyYEuqJZgkdv/l+2DuEL5JkQEi2HlPw2HSMyQghjqNzaP/N/MbtzrZvyo7BRNrHYu62glPzkKT3Ps7o2Wzqy8LUl5QqNRNme5ngLf6Iu+sKLNsanI9hsx2Kbht7AI0mfdzCydMhf1sPiy+8945NLNvvdfBVsyflk65qD0BEnK/hFQ9z9NBzk2/qR0xE/nvoCzcU0LKMsuiYSZduTg4AqbNLID+I3dhrUHQbO+L8PqpicCkZtKl2OV0Xk3zWR2qrBABcim847Y19Ub4pOaTTMyNRcL+jVWy/P/B4R6ZZ003wmYJa6gFtGiEcBGi7LfcrFinu9xspBzm+aiemZGW6x0IrceBNMvPjLB1be+T4l0dsL05PYvbGbTNPSTvksM2IupsmGWXERC0rFVguvRJMqw07JSFB0eGk9jw9JkHGgew16QtG/n6z6IdZnXoP71k49hpXwAC+zqLYS6H9BzMZsJKYSMvwlw+u/5GtdhDWrVZezhOdFCnYYTYfTKZLGl/zAlEHv6mNrGTEgb0obX0g3d9Aq9wy15vwUcaxjx2bl7eNX3bJJ73shQt9py9kxOxqIFHAOZzOYVK9iGxGaJBjt34W4QU2dIcSO1An+FfOQRyGji5tQrs0TL8hFlu/+QG+BVM0ICXAr/wZE4nY9LaLmOISmurAM1XCDs8YJ3sjaOBupqu9exEedMDZqMbU13PJexi5O9bhnCFnsW0HLIpyS5m/hQt+NXDm2/VXTbTCtF5K55kYXwX9r5dywK3af2CivRGsxqDP6RrfVFaFOzwNB584byweAsc6ockpNUHSGF/E2GlLoioxp+B+0H+2x/DxkEW3dmFpUrtNAtfqOfwAmepft3TEwH9Uh/UtVQn13FSlu7w/AXRYjhr/AGGHSu+XppxWT22KGjV9N9Ecwwc6lJ5dOe4SW6ydQ3n86iAxYNqyn7A04pW5Lg3m7qUBmG6eaeL+Mn7Iol0tsOAv2g8xfh0QiNVga9lOZCUHqh6DIdtJ5VVHT2bUt/6uAjsRA4YlQG24hB3ueBVpK/0pwbF+2cF5M6wHS6qZ4GD5j2/oIOMQ9GsT8V1u7nUoQEURwdgiEUyfQq9MJWP3M7eGFIda7VmrEIVve9NERHnRYCi1fNn8KF79jdKquF6Q3DSAQxlwdcONn8u/SZqsCto8+dtfzFIrtn5GVLzdxaya9RRHpBhAFQ8VgqkrS7+EiSksORi2i1IK4THpLpxUkn5JoEDjtjrqIjOytRD4Wu3G1JdUilx5v0tav5nGIF4CUB1bUI/6KvQqy/y7r0iEZ4REfBC6BUCs1g09nuhxc16uSz7ZSZdhgwWszWQLijWjxaVN6JsSpQaGBCvSPDF+jy9jcNupQ11ePJ//Utj2GUyAHz/Z1qf1KWcBHN1surkkh3AWsmn4ck5RLPemMMDmZThBcqJF72GO5FRObLbCPeiPpRB02eh9sIqjSbn/SFTjalcObEjRFxaW+eXoXyeHO5k64VrfYqOAyt4NBnEeaqVAX7pVFxVVymxaKR7Rikv27IrFoV+eRFilEv4sl/Da+ZtJ/yI6L2uMfSJSeMqn24pBQeLuMVcH9sPLsb1G77ikTTmDzEJ8gB0lL02rNeQh94voJ0D6U0hsqz9Khxh3a/QqfuTHJDTE7sEMguERNliuq4GHQKx+q5AVjiXVRPXAqlC7HWv8kySYSYeuARFBNtdLux6rynmKY8rpwjTjNo//RUpnpjNyDDtFr9wsGOdzjej4oyzkP1XbUqX2hoX2yQJZ2w6eLAqN6LBw73pajHmkmp/fQHrqfPBVuoTU1hg9B3WlJmW9NxueK0l6OozmJem8xIh4Vi1w2Sa/drN6HcY3yFyy0/sHQPsRE3s1Q8pepmCNGi0DAY5jFK1qQJdBEgS/sjCowXnQP/HZRhcZo8HGLeFPACH5UeqleRWWhSIKdT2PZy/EdPCzQG5Fzs7bppPBCS1jgxxL8+fOiX76qRE1ZFailf5/QKOmA/eGrhdLEmysLT7NHeSqKkQNCZaxXaNqXNujiO1pvEZfbXHOmecl/F5vxRH2h9lo6Q8FibsS85rY4izOvyxIuQls6e5sMtBRSZJO8xl2bZhojgJoPHvVI5E+IZbwlfni0Dhuel4szf+5r49DM3LNNnKadtlTQ86j1/WPXl/UlcalrVT8OtDuOcyIr2xJLACr5xIK6PgaEoTjwUKP1wArfSDz4S1KW6+WSsgeVTP65aZwwSr3X89ka3X/1eqt+wFpQhKQ1vtwz6BsONopwZh7eCQeV49eIEbcOhPh8vEqL5z/mLpTqmDlsgfPf516HK7OXMIZqki2+VXDyD54yZz/rL8nHDEU565NFTma10SJ8Cvr2S+oe8Z8VHsZRgJNzg+tkMV4GllxxW0itOnhK97WpIckkCpIdlSb5Q0xpnP240ZXjJF6zlV5f0NmudMO1aPl9Wqgn6YymEQU+F5+4AapIMg31RolFLk0YSTy3A5i2qUcmPnGruvBa3L8ZI+FB69QwGxARP3+goXgabVZzqT8Qexj/ByWdMMlQxtgNV0bBptEjtkyjaxDUSWMfoTNz8UiqVxY+5zCWalsfIreGEh+X8Zsy3+f4icC0hPoGjadW4WAJXfOO4LChc1Pp/rXsQPugEMAQdJQPqnFiMvrPsE96JknDbr9vCHi3JntN6+rXRmz9eSBdMA6VkAwM7VWFw7L9WP+V+g3YhbuyZ3CofGpgOhl8tFCBiLMSHL8se37PC6ZAsomgkgUM/r5CkSQYkC1tMqkYUcVKofCLcXbrRil4aW5TsqbqPr1JnqZbwXdhVYaUL4YMQedVE3riNl5Y59mAKEN+mUx/QKk5sA/sYez0AAMMSMPxiTo6KuxmfLNlcp+pLqPjCR1kXQDALHEVdsEMmEJszJOjXihesKg7C/7mz4ZEqZjMomlmlYOhxh7QxHHPo5vhbEgOWRY5sRO6X7hXy+irz1DKMjFM8ZnT3HOZdg0jbpOtGzGDKYV7iQVGj8H6C2wBzUz7UpA5GshUCZKq2qyWkVAUsiByo16zs2bPlc3gV5rw7PJ4sXNB85Z9ED1dzuxiPpX8MJ80BgZMSp8/EnHpx8+AuUJStiKkAgPW1fwpVghrHWkKknVUvQw0LZQ3Q1L5Az4g3fyFwTHfyXZwnvYrk0Pb/MW1bRj+PkCLFAgDSnOfmMiLhYjo0iudPRkTgC9z7QSkyK4pMzgcXzif5rT29SzBIfpQbvYiasOC65c4+28MWBbx0DtEI/48XSG6FrOM8SSwro3UpqQkNLtz5Tw6kY8GdyfuRzSZf2X2GyPcwEHyv/cuFSRFoORPJG1JR7+XkzDK9tnARpahp7ijPEFZJDY7/Ta6dOiYGT2fgBgtsB+s98gquglAwc/3+OjeA8r0+XOLCG8Wdrtr3ymtheSIEbNi9pnGbXmVs3aKIjg9Ba3oV+ioLrUrxGSXbvZM7HG9AbBGDSC7QZd9o/3UpNHkRASj47LQMWXaOK7u2YLgQ2TGT1HFjdazwP1O1l/Vx+zMGm7X8LaWXdJDTHF1Up7RQtwdjCFYmfE7IVDZiVPzL50wEu+Tm1JoCDbMBpFeI5wQnOGX1AeQWjToF+ofeSe++AeG/93sPYwaDGyg3zi0cF3UQjd2n3ypPXP4v4SCkc3ZUGyJaSgs0d+pwUzsyczoYqUG5kqjchnc+VJqTIDNEqZN2XKTdpd3rJjwUybiGo5J3FEOjlFVSPrneKx9t+XaG3i9DJOq2wRXN7N/dJ2fyEMt9q6hS9wowBA2AqVsNGiRxtqNsccus0zF9FUSkS9h88jvRnhpG69IhChu4fhiwmbKqV7bxompM/TZRzQHBuIS3s4W85tBdgF45+8y/YpfZnhgmT8j2+WSXIoV34wgCrb9VjIt/Ey2WJ2o6yehWCPzKl4Ox9STUmuMcrrooMp56EqvuJ+v/OSBSmk7hCyX3HBmLM4OaNtELz6krjCkROk1RE936nHI+w0NBOfnuUI5ovKMmE9Qygr9NjCnwD/yZfHSQbTAInWOeWHGKd85hDbypcEuOouyWS6qvC0rwBtLmp3BN4HRyFNmxl2DMEiVS3yP65QwWyAEFfYGsLmYL1KCeNPqgMs8epU9cPwe1al5NYT8JrwVgFrEProWs+omTPkTobnlROwzOlb+SSp90hsqbXwKUKCgYqn1+blWEdDgddmWr7IeRXOCcz2Fg876HInhlCCq/jaBw81iLYbqw5W3Q7HSaYJRsoFs5LReRcSE6TlN31XLzykRk7dgQFoWJRHcDpxH82UolFacP7eJWHGi56BcEeNWY2PW8B69xgTmSe4fnyTTcFOMVA/es05YrG0jDAUaCzBrrjR9Fx2LjgbA4GUPSIo/MgsyzA5Mv1YtyWVV3GDEhzhcBPNpej94h1kNjj26H2SWIkC00c6SpRZcONftO+yb9b8ZlqRvLzUuDU/OdDALL7YxLzVtMgrJIUiGxtSJaWNDmu6fYLHPDoqqHQv+akBMgzaHtR8oJlmXrai0CeBVZ32TGScs08Wdn9I0ndr5Y73chSD5jwtF03ZPywnFFc2AoI5Plx2YETpCdNoZ7v/H8O7pXctaqX17vqp4SE/wd4Cn50/qQ9tp4GDXSEBMn2QxE6qnlo6417Vx+XfAoyxUQuKS4mqZPE9OAuw+dhZAf/+15VC/KtdWtM/f9UPf8T8T8r+2FaOIgM/ljw0QgC7jAcuMJJ6ob4cBpnL0xWT4Dc3t2kO9p8F9vtlRFkktAqMXMMzZtCLu2W8hMPYm1stpK+alk4JI7Y0aihtOfugetaype3JnPtf8gz+ERe595iKRWSW4zxw66IvjNa8Cs6QX10WHQs7YA/ZkkRP2kpA60CAbi3x7Vq8eL87SMQnQHcLaRFUaVJBdWYqr3Vf4pX4YR6w7db77p9xqSDid38cu3oI14pvWLqZpH7jOUuvOngH9VRkGQk03upG+qe54Q29WhPJ/KmSC0p5bb7ORoDz1mBBantwKg5dE3GSCiKIP9qEjhjCapqbnvjF7PFboYA/Jg1qciWMw1BuPYKxNVtD+Ens5Rx0evPw+FJwGgEoRSLQASvebX6oGBI/flxhnRfz8DaQrG0xIWhmSovIrgkqPvFnUMLPZOdj0bWzuaSmyElFqeFJZzgbG75RzgtJmajd0r6e4YnTNkfLdA0OegOZtanFaQ6k+TwVqJGI4Oy34sDkKH+eJZduwoWEDyW10m4CiuL+59197GS4g51Gkx3JDH3Sxp9Kh0jUqf8b0S/tML8LCI/D4kZ1O9izUtovKjK8UbNbCyVZn7HMpAd/iRSjcqVpKeAzwSV3Pqu0bxB+viLeKOYt7TINZGS9Yv2Rhsfsv64P3HF55nkUukE70ACB7dzqOswTumeLYqqSJTMdEAK9jDVyhyxQU3tNcnXCUrALqjf9/Wwo1BCw8SGnv4W/LsvKRMTAKcYcaqMQ1O6ZMjKgU7DZlwVPTtdV1kL6w1QgEQkFjuAMbiUxN5fPhC9VcDXrGDrxtKAVs1I6HZRhJAfiUDHFSkwQADlFkbCbLGESshOroItB4V2n0CCSODQlgI/VaKK+RSaRAS98SPAC1cmnvXNUD1hw0d2GsIgXus7PoU8lafe32AucwosfkB3WUk8Nq/9SiJgvqvV1rZ3zPQQMsX6BCw7Oc0RXb9GxGZLbpe7sBFLFz3YtIxCUp8a4qhJmAJvARd1CX71GZ0KnMQimzfI3X+CeKmq7AHaxmrfv9BePOSvXQZwSkfgU+t/QyDHOIXj7KHIzHymXoYiiJ4gAT42tW5EkqWmU7nf3ixZa12HVui25hH5N7PEpiUH5cIEPcAnppwUiVFdTNXi1nnLB5E8nF7087uvLd0DLXN/8oret8t35ISW2zBoJuyeqvgKCUCkdPouvY76sbjR+3WcHVM4dpMUqLXGNctYxWNqgNsqdhYRQHqIjBjClPzyIErT8CBydsgNiC7nO0qF1+gOTFAriL5fVor0h5Jl3QTpaogJ3D17DDQSGzfAyaMLL8Sm6v0dhdR2l0vYSLacxJZp1nZMrf75xAo/lzGpqB/56ufbwjiQ0CPLORr2VEIAjBStJ5ek2Z0jzdNxRFNE7jLVsFt463oKXNvfU/UbvpIBuKjXVdCYQk8JYr5AGeEXrRb2C9Yq8zFEISSuroxGDhSwvtfxcMlKHd/5jbCMozTM23GsaSuxZQ44H1Jfp3/OfXfbZV/y5+4nKmf+cEn4ZGiMyYvliVy4gJ94U2zXoirJAEFaUaYzcMNdbst6hyfC56lS7wI3Uoht6KexsXvzv1ppMMcX6KeXSfJ1lxLPchs1BtDYYF/IyC+vIUQxwj3HS9GaetNk+vnVm5MIfjs2/nxizEXATipjFm7RL/fpE0QmpaKGCVd8qZPn6hdfBFjxh7uUusT1t3a7kjiDDBy9ziz1/WQaTANoCC2XzozsdwqJ84905iCYs4LzD13YFCT+BjSE+Yai3QeO36seDWPnTubr4EBe3bCVh/GukUO3z0cqwU+Zsk3oRtg3ZC90Ee5cN4cQt0yQg3GcI8b4VMstinj6/9q2cKhyvMDKfA/iJ6mc2hPbkmFVOBludUQ+E30aEzG1TcNiRfGNqoceInegB3avYG2+M4NTJEL2NpyxLlV+mO9RmVAxvHmlK0GJSp+kCoxbxE5Eulw3ztJcxCWjtAWpNlFc67JxN8J/3dbjnrVMkOdylbKcd4WstUy4f/CjpIYcAwezGae39BRfzfnBk4kHos8bRfrgXFBa2reL6xt7nDfBuszpju43i7A7RQuVajQmjDlO7PFDqsXgkgMPJ5f3Gtm+RL82+OZriKUZnEL7WL6jsAAhHvViB21o8/sgmhAJOX7FFGfNqeAfrGe180LGjf/0GhuPg199bXazN45lmaqc8g82n96M5lal16XyD/VBEAKd/ntgUou+3GgFJGmwmDMdh4/BTYvwyLe5gZKp+9m4TBAmCtnG0x8TBVl22HJ/+Mrixu7FdtSKcjL11SCMkPlLVOvFWxM3JS88foHvpGbXp5pzs5U7f3MjI04qAvfE65LPV6Zk7WSE+ybAUJUuc/9VHVfVjP0vXRF7FLilCfPVEhUfu7X3hD51U5e4PS1y22r1CMp/q9rAskomS8tvY4LF7AMyFZDKwYcWWYq9XxNRI5V3uQ6matiBPcj2d4HTH1Q/OIty4ajABpU6SkKo4Dl65LE9n8wCWLqvpH52ayjpE+hjSghthAKVHJZYSIlWGEh+97r8VVH6GU0/X9PS31WkpuMXllKsF7UMzy38kZ0OroYgJCIvx76mPKFQr0kCNXktbe21sWQUr2typV0ds0n6e2A40mHVjufp7XXY6DR/DPOq6bW18pZmfLLBokyf/p+629e1aGFoXkjc++Ma/RaeSGtN7A65GCGyttnd2saH5jsmfjJbci0cQS+AB/GVyidXrbgYSTMwnDvuuGHeNeuFgsgWYuGeDG+RIy2gGM2Ot+BTS9K2t+r2t0AxYoTu6OvOtJ8GCmsWQyMdmYdzgz8M5oiDd5nkBSm1MyNIlppWIasOUUFJUfVgHd74eJZIR4LzL+xuKKmEoc7J3PXQle+Ltg9gvAKdww28JERQw6Bpp60ujyoOXIp1lxwbdi9WRWRatJ+gZQbX2H68k5KyPn4nGueG6F26eQNmO4G5JJ1KajQEtIkhwPGLgTFIpSqJAF5tWdRperEWo3Y1OGYioSeL+1quEupe0IevixBGll2pnsr3HgU5hCcI0OA15Wm6jcPf8mz26W9WzLIKqlcaiG2mzTWYsaYF/hLC6K2RtxZDml9aj7Ad1x7l+0nsEXei+jelERmehEVuA/MsU3BF4dUMGjAxjGHHZNbTlTDMl0dgVHSpi6cvUyGZ1B3OIf18dXRVyA71hy7pxKuwrsS/sVKtWEvDNQxc4cNTaO96+tMyXEbyPp3ucgu0SGX9HqBMfCmy3NaM9F3nbmOC9VzzRfXcKGGuWhTNpoDIDAWjOWZj2Poluxy/2j1kTSpQO953K0SZ1Wk7EUL8EVad5uU6bFOoebayZ2++7dkgZD6HjcVkp90yQI7r1MNBXzbEZh3W+vlhs6tQb8FZOCuVchNmplqG1QO3mGne20F4oP6g/2sY6GFc2kjJa2HDg2+5fk9Z3kzsvD6r09282X4ebXAeBVgJwcxeiNYR6hMq2z8A5NUi2OHyPopdO4ZtVo4cOnMyiKcDCtBMK6SvldZIP92LO8x6nYXTYnRwIBtoFzHQpzuXvf+X2dbZbX1+ZQyRyIa3oX/kz/ovDYjPL9EwlDL824Vf9WuM8QY1iy6q8yK5sVimLsnIRRFk4oqRgNsS/B+Db9st2359GPyQdMAcjQk+5GK47fRWEaCxUgHd/U3eWVrU6RShyrIb5B9rPxyeQhDJtwQTlj9uOhZCJys1xgR+gE9x1+UZqPYA7RVuR/kKdb0DXCq5rHbdSSJ67IBQneA0UWXt589lOUsIjM+9NSFSSrj+U1ntHl8IzL+nYoE9tpIt7tqTeLJF6CxngnkkcXKYCFe7EYQyqV/hYxMH9PGJtbfy60/4GWHaw4nhjF/dj02RFouOMhZx5S/lKNaQ5bRJ3tea70LTwWySQhgsXXhbGLyrSaGGrlcnwaahmQ9TdhGYazfPzmeBWsTC+4YCfA1QuPl64rMoScifUjiZyhW/fkGB+TqaXcRfsypH3fhqaDTDEh1Rm/tD3V0Z2D9BanZqEHjc/fdkylvOC2Y6Trq9V5HXj7wT1Yw9ZQK3IRo90rfd3ZJfDAqA9TO7VZ9JVhaPZAH0guopQtOflKqYnOB46jJH3VliXhqIvjf9Uw7x/s10FpwRjqUBmRglS9LTW7KFwJAP90Eu0DlOlbT9AfeermO4X4ge0bLnMpOpn0h3daqln6o9zbFKKG5lT8+SQ66kphWqMJ6U+FhxlTKQDYQpFwtXFIFx6raZs6/AwWCM1tVEVaKpQKjjTBwrDANA3t+3hc3mXaHdf0RvOi2ZqN8I4dDhxBeEwbq8hYzFJm2+ZknLiL5N2Y0EeUv/An06haAzq6aX+u0klj8cNYQ4tkmM2fNMTM8R/kDioS9zXArCQZcXeQSLgBeRLyfILQPpifU9p02gHwX1pUVvwJ7JruyHiYA4OocMRCF+cggOZVcMUOsax1qpQMXevdm+4W5pTTudJBoOn6Bk7rrcTAxsQUHz3OXJcwNfTSWBxo/3fWtGyNzWqXO0N0cIWGQLGeNijKvGI8ib7tGMJVAbbp4+aZmWpg+yHN1dJ2YqWUxLRg3RJ++dOD8UmLgzS8B/BqUpnsqBjbo57kYI3nTel6RD7WhNoVA+qUPZL4+oxDoBUnTT9nvClzagwiBA+9ntjTYenuUnvxhpG6AUB9Sm1CVDEcfzagAlavI7Aj5z+fWtajRJ+wHGV9ARjM9l3SNhSnBMk9DCoebBenzxtVnoamc1T7MWknfaGmGaTUmP39eibfrz+avStKguA8MHKkX5O0FafhUYLA2urzKJgbFn7mcp7WpSwerq4EBT7D5nOpUen6Rj42qq8GMOzlUvstetqd6iYTJ6ErzOOBd9ZWEj4ZDgbHdn+ph9la0RQkvIaDIvaVteNwjWFXhwGxDUjfZtwe759lAZwIb3BvEIkc54iDilUXg2jOq+aMpRvXEpCX//mDghO/LfwJXqCFcV8A4FgakDKPppre9vFZG2vQ3HzZCCSZu2e/CdP2j1MUORau1kz/Kdck4SSSk4PHHdHKXwLG4rw9tMYSivuZ5GyXMK9i28Lc7zZousCLyOKOimq9z/940+KHDcc35LxCzexdwH610VjyXxzpmLely6GPi5UY8/GBe3rYcEeIZuXlHZ8V4dBuBcalsRtUjOcfBLFWGGwIpA8g2UUFDxucS9XNABlkYz5sPgpawIwYKjWp+xX6m5TI7Ku+shK9KJOXVoyNb0stTSZwJBw4wP3OB2mc51pe6VWV6SiA83hs/TXERrea+aNkCdE5HPoiecpU4vSP//CgfVVw+6YCJTpQqqOAaeU9PKP7rULJL8eLg128Hi/srG8KRcI9IdXK82ZFD4imrePUuxmDsw1du47Pt1J9hpfMaXZNKUBzprM4qvZab+ZZh1IpW6z3I/CY0Z0uLSZPjPAaSGGFSzjLFaZUdElogyLaoaofMBknYPtrNshHl/2JDu/rrrIriIpy/WjvjFy047+t/JIHZW0ZDo14PxvDeX0SSeQyHQNlS9040xcRXp8/rCqqhQnsyqHGJpAKWV2V/R7DJyaR0Ex8jlNLOrjCwM0B94FjRtbnige0eP1jawSGr4g/hN9nRmSokl+IVhJbAs1leHBi7AZRVNc964fqPdIgKMk8hH4ot1mZfSiAxUC45K1g6NqfKQBVxwt5wsMdBRLW0jvjhKBhXj9usnOqkU2q0l6vwKD/mYQXUnSLgIMOmSRzchAV8qO+o6CLncLs/f8kX97S2/5ifLKp3IlR4tu0ifSWgrW9diA8h8Fyn27JCSJ/wzj2hYInRY07T77fDf3emdbzL0GDFZU/R10CR45HWMqT3lyy68UnXhsd+6lzpVOAFmeGMQws9SGNn3+QNZrubJ65hJKaBqknecPnA0Hv09KnaTE6jkFv8vnMSbU7TsicO0dS+7fK3p/24JkVx4Ruviqe8APJMAUhJmPzkSOWIafnpAb+gSG0h1FELgdD+OhejX/2qveVALCCEr/SDTR064uqoy0wmnRRNc4d7IWgttzfVNHNfIP/Fg1k84pa1lzPMeEiUJ9bmg0IKeZklUPnp7JWrhcJEdnucuExPBcNvNJovqCxCXx5T4Zt9iYx4KFXKCTTlOfjNbeVOv7rUpbgDlYDxQ0dXXX3XAIZ4aZpJklVYWHCnbMgnOkENFcmGYiYBE7pfeIfaiKwgWljmSh9c10s/hD+Ncmuas7IwahWZiWYnktm/Wkle0y63SPNrpEWM4FAvF74ghkBgRO3ctflZyyulxZOdhPJvP+SaLNtqe1fxsEO4DQqj07IyGpSmbzmGEjsunA7GXhji3Kyem1Mr3zju8CLYGKVX5wmwMhaRSne6/wZAnMoqOZsDuTDaPDNrH94bkoueXl7hnpQ9Qnj40glbcNjJf4RfgezrQNmIELFKZZWp8rJAG38krHtvAIfWEioryfTN+JT7CyHYdo7u2lUBG75DEafafaQhkYkquaGFT3ixkfumQ81w+mG/fSkYSmCAXs4A/5JDX+eP7g96o8a0jRDjSUj1f8nsalR4PuqT06W5QZgPGumdzpBCznnBOLl8vzPlxdcAE8XVwpjmm8TEK+hy1MoqNoQMrNrviW4IpdBC4hNN/SjGXHWsD5Q5jyWm313Fg96sC8csP9t4ot5WKO0EBcELfe600uaEpoOhfm7OQgSMs63zSP6tKSHxYV4ejyDXRQpZ/3AMAVw01FfTioTMh+3ez956SncgOTgsGmdfE0Xkl/DJLhD8WroHYyK6kdVuMXs422/Rz1hoH4xOo7lvDys9qH0mLnBBQ+VtdwXshBa4tbANqXCnolIwNJn4CMORxVSQyPRLTZm70skzQp6iLtF4bpknuTNB2eOu1URambyNfT8weUzrx2P2Sox19YaZyZF3BwWxl+0Xhph9DE9EZRxwfgA4aZZ0VLFojSC6FGjOvJ0IaxqezBq4gcMHdPLsAIQ5bKwJtWo6LIC2R/NBclVOKay2t6oob2ZnVVpfJBFiSm/FppnmcKd5RSfqieKHl8LrjcW9D2QMqQoDFn/I5jXtBFoirsX+i6yngv2mgyN79pQff2CUpHTbv0av1pGfjp4lRPKGoc9Wq0INNelAHWQ/FBgDlq/uJIG8tnzRQfBuBQBLPxmUXOqe9Jk6tmqdONRZrsYjnIEnRrF2/9xisLWP6FYUyt5KuEdmnBnZuhpdjK2f52OcKxTFEvQZIZGFWkH2ZxdIn29IsctvpuYcL2SemrZwSYPCE5cgNdaDCAF4qCGcVoxZvJXhJlhadWs9nUXrV1vMRD6VOW6IQG76E8ayuSvkCpcOgpNwu1uRMwnIvx52UQirHWFfuMiwHnMXgoNHDqDdumx43CoB+gEUFS5NL1/rLOE0+vItBynYbHc0WuBeoOlLOwJY0rHqIlBwA7Dbnnm8534tJk/BnjQ0Ij2gD//k7VzmUbem6IXi8hGnMqPhZdn0mRRXXJFWSy9UBJjFgZ4ydJ3WKrfEd+cj4jJ7eLACdaLN1Gkz+t3ak3aJM9FxvqpZo4YLtpqJ9h01fBq4EZjcN4olGf3m5nLwa2J7IHDMgt2qOidQcRLBBqjhFd/+Lyn9CmrY5abTyaWNvAZAZ2k88exvJkR4FFSE+F7Q++bqO3V+A4kF4iuap4TTSaKSwepVb+iqByXU8FS+fPX811qn8KfZBsQTbNXa1wrWcydZHsECFf5YecQm6C8ngiUOg/tNx8IEnYoBKLDVs6jBg53xpT13DDXgu8zhGZcWGNs+7R0fgll6yHwdDRDUypwqamkTAtZDD/+0UtoAur0xF1CVPftTJ9VeeWcVmM3kF29SejQAneSc46eDIQ76i1DNM6LrdzRcrQVp8G1YYTGTi1X9cBvmOBn5tU+AT1xyZAEa9kyHc51HAwKwS3jzXNxoxW/2mpFezKihWKdPGN/5q8tTk36AKJPaWkwavZbQXUx+5pACt4DjIbNQBH2FgsubXX9xSLdr1B9ZRXsOyyqj6P74DnY85IUyH/h0qkR8/hGmQVpMSTx+Ldhife7wcilQiXJu2EJzAiBOO98V1Hbj88iZQIEKEj0pwTfJdDF2woVP90/19fNweOCAKEOvPr/uM2K6XGjTHbN+OJ5rED8s4c0UkgaEHuUXApw+sPrAcYK5OPQDAYhZlbZSYl9DKQRtvS+sVBjA9Qq3u+NlDNF81eTpCRD9egPaSPChmrlOxpxa+Bb/lsxDdmbUEP44kPqtKp6XZUi2dBGi0XrPy4Jq+hDKxnv6ySoZbaR4Pn1rVUgDUNh1h9B5FqfeIpGnkLUZ26z4hUjE17jTdmpn3zfPLzExqp34yjKjQYpONsQ+krQLx1Q7weskV+h0Hr8/Emd1z0KGlUD55aYFbXVconoK31ebpjLEnof6f+z0cirsuhP7yudxQ69TzqML+8FTj0BY57W30+oMAwp3aS0Fb70yEyuoHkBJo8xVYUxWD+YiiC24e+7skvAdpexHPpEC19sgTt4Fv9J7AyuVrhDxV3CMyg6U9aC5CSo0DKqku6nrfe4zo1XZ42FcTnEnecTrYcVNriEHGB8AV79Nv1TENC6Q8vk0D17FYLdjhr2hxWCypyi4XXGpfrsmVWt/HRmb/ttmK6M4obA9j+efK9KDYcLKtK+1sDvSCucHq7bEcZoG9QPY43OARM/xw4Ayn+Qg9UuWLJBHTtGLCwtYX8OwJOjRs8aT+UsMdQYVWc8valL7Pin7ea/jbk7gf669cogzN1PlgV64DDEl0LSGRzaMOCR7fBL3nRlM4vr/N1ZavdliZQPLt3c7VdGBD/QJ3VTc4PrxtjS/5Q+1ODj41jCLOUzxRXseajgHpLKJIbivBeI4QcUIqJjfS1LOZMLE8oNP+qAYDIQ2JBXKE8aToC/DcgXah4Uye4UDDdW2LOgEea32RZGt052/rP8NWmz6oCnEwUr5yoXsR3IsWSNBbRJd6ac/Nf7Q9zWGcvKDeuS/tUg70B4TQRqRFH+Y/uHeZ4rgPYmUvUpgNGTLnksMtZmCevbGMpZCIXHnZGznpw/xsmR5qA2b/Rpeyyk1adIAEFRvJWEb92kkwgDSSwfFI1LFI77I6+w1H3eHB/s8DLe0DfcorkthAW2INXO71c5HPQrSqGfoRop4iHrlED0CDFYCLJekk7r1Qde09wIiljs84ip5GOU9hIFPyKnws1+L+nvAjKMdyYuv1rZpkJNtl2NP2F0BBf+uoK63U8LBxCnqR8j5A2VY19MXC3MUUTdv5nKucUmaXgb7FTrfVjUTRNvj7tQt2tNgK8DeqdRBru9Faov1WNZgqRtNAZgMdAtJbGPVE6PiNVyhNzob7msixOGEPnHdQzQJu5dxnj3B6UEgq66REwx/9uRg63uYZx6aHCQrumJ5mIcaliGdWh74tyN4bn6JFtJ0/706Qze/2Ge8FISFpeklnbzhspP7+Q2W6zcb6BMdCOKsxyz7Om4SNpvmKnBEMvLwLiGNmVZ8psPAq/UAodq+Hyg/NS+qNW+FY6iq9fJUVFJ8sI+PnNt/89pHfgXYN42kGOt4GYk0V4KYLUifcowCV/pBfa1uY2QbXVkPiZXPwN894dnz/k7cgc3uZeI4wl1U8Mh2IwPT7+Z5KDbXzcnKLeo5hwgkZ0UojbR6DMeHrYGm4WRAdfa18KWX6FrZx9yV2npSaRPggqDLew7XIOhGyX4QUiK2fqhvhbQ8cGaA+mTnHQYd57h1QGukaMLzbPb33bPy5YDog9edT8O/mFDH7JNsT/gBn5bFX3pUjZGueBHWOgVvIOYieUzvNnq2uH/gr5cE9MthMF8bW2SlpRAVSogERdQkrrI79oT1KAoqgnUBOZXOobNuAQk6HnFnPjhJcI9kWNlMJLUpxbvJyaItyibEk4yTfjV+EV6uxryjcCcFOiK6ZBa09eFzmKK2ZeS81SqsWjKM+kr9DXczNrH8S7d64rHcfWHvyOStdTLOOww2rZWXFsrg7wopHr/65XUWEYj/yqm5vber9Z+xdDqeu/rIiK/D88hUepmSZLNVqOjWYI09l04UKcQR9rQPt53bKoqhOjfF0uz/ZM4enUZiBAVABRznC1arh9uqt/ofvEVIj/Xsxi8yLZBTyYzPD3GUwK/KMQe3Nr1RwKljCT7HGZ4Heg8btnIxvQC65Qy71V3uqjlTjeV+spljcXy0YauAPdIFAp5A3xNCac40TLSfAUcPGVranz4M4ItbXii03ZNHsu1S6nBCs04PES7yQhJIoFfkUNKnoWBROW4tNF0tppcn04nxhyQ+8ZbeRrIh5a99hUK84s9L0Ojbfo8NiUYgjXzOYVjXnz+MYvZtObJ0yOnlmdRBcHZGAoSq2gPrwzLx4oZB/Yc+kLZZYfxFTUhU2KCX/cEHPBr6sdor225f6ZsulceOq12ijQiFd0K1vecrM4dSMRmjxjHfTV6ENeUnv9BL/7dw4Lb6+qMQjZMAGx9tYDtGF/q5Wl/fPeGDKyGAoskn5xSkaEzpLWAHRsAk9p6r9jKYKElDD0kA+kfX0/dqEMJlFelv334KM9QUty6MwVBbXHNMG2RrZshTqRhPfF9gpGQn6fumQhmNrCCnbHQX441mpB/KsmT661xXYCD+RWMRnBEYdokSJQG8xJ6CabpU1AmnoVGUy9gc7fkFqZomc9fHzjkverRmu/eHZqD+q7FlB6rBjOS3N8EDmrHN13/2sIFfUPn0nZgWL5ValanZz7awOFC+ao9QEuQGOOeALSW+p3adU5aw3GR1h+DYK0bwQV3QTJT7mSAUAZ9hpBCyI3b4V1WoNZA6R1pjEh9hBkeK07eqjOxoWu3v3ZXc6kaiRkUPyqp5gmtA3fZwALbyEN8ovCFs465jv6DqnMSw8y1ZhKJ5BCC10ux98EM31FYZgFuvsHK3g8II1lSyYiCKKbdwdl0Uom17SceofWoATzTsGzh5ZVQXcTsJ7tpxPoS+OWt8JzMfAHFB+Py1MDApblFSZNx4+O4CurPpNEtojUCohK1BWlX3SSuBr73XgbRwraTJY//eDFI7orinpI4/Yl5XZru1QJ6ojDbGrhqGjftZQ5waNR1B3YGczce/J3xrtf5RuOnkC7PAhQAr7fxJSY5jnzf1M7pus/5C7xiNGFqFfWGqG6j2zkKXKpDlNfZHbYX/Nxby51b1+c/oM6pxRdUyhlKuIjHTXdAciXWsKbj9Hs2iskNSNPox0WM+YuAm2r5m1iakNKo/jgF8E88dmfKtE5VSAN+av/4A7hzHDNyET0tYnbc8OmsfBlT+jitDA+97TYB8paoqEgiyKukIcJi4OH3TV2u3xw5LzLZPRxicm7bf4fenCe8oFkhpxaEqeXWiYsvK5tTRG71CFullKtbuSc9GPeWbKlFKhfpet/2BhAUs4OEX9pVVFdzK8IGn/WefD5h5i8vLf6AsnN+OhLZHc6ZFj8nMKpClJUfV4MJGsvWVPu+LOmbM06rpnNQpMCplWGOUrWuDYBGyndnoy39sGnV6/uNuIVbrd0gHggUb1P4/sujOsFw4pVJHNdfLed3+47qwPYVxbg1+7UBSipDTe6PrY+6+5GG4ksALhaRu0gzUrkxuEf9LQSuOjwfSdnJzWCwO74ozLQ/0oFumUyHKBDoNspkZvWawwEDrrL7Wzw0eO0Ez0B55cgSqnG2UQzzWzLMQlGeyIHEv2o2F1twndjv78E+YadKBcBB0O0isjnMaTN9c3LJ33Sto1qn/w+HZmEH8u9GSdxLrLnFazYJ2CNn4vCwBE6+3xqYOkeGSxTHUJ9Bz5rE/eVUMPAvsVDUc6vK49jzgXPyjREG+dL3wg65tsFf8o5gCYwrO+bEtIAbOABr9uE6GPUDv1EDvpLYE9uAZnVfs9ylEAeVIAO6A8HNldVpCTnxwEd7oXWgeC/Kz1JcPTc9s8xB3Wghc6rgXtMX3yXBRiq1d6JR1+X8QSh9J6GXoN8fD7tN4K40zN/tK3wqAufc90v5++vQ1Yc+HiIGBG5r7CNTeCZ+kj7iTTnc2PfkrTYiS0XPMpbdRQ6uaztg53IUwaNyOMJtdk0Y20c6rc0o5YYuivqSUFhrne20d8eS6I/MrgKwgEk3N265kDBHzFxngVKNmxyb+w3DMN55MgbAh7bMv/jpvE93lS3X1yAenWfsGM/zcmgwB4jJJyApiy2tx+MTcntVUBxpLS4qOCcJeMxK2EVPqm+tfN41qQ5IbiItGNRKp5QuEbMmXtc8YGYV5LGXnujOQMtVT6fjw/vPvVwnowYs4wVYYc+hDy1UtVQQB17ROqdaQ/mkvT3MQE9B/Oq9NNW9hL5KN4O7fY4mtXJO83H3bXKYOWozbizSIm+UGUxQQ4pJLTdUSAc80WkDXqKywVhbmG3t3cM0lHM4aq4Hr/WwU/5LuC+pJgB9zAL9o6ucmmiCvQswN7lBzYflpAoinESL+65BwlXp8u2WAkbk0oHz8BGmRoJeJDDLspCYUpP0EEe7sMFUf0uh+oK+7N5ggyHeYKo5K/DqoNr10ebE+HdboPtHseng6hD9lD8bE+QndKNL54xuG4w73DDDFhBiVQckWIDwIZeKQ5woTkIT03XSJAw1OgfFHwwCxKIf68DyeuLmnwcgozy9dsgvi0Dszm+gch9oDBgLcnnsNyoBW5z+GTTtSHzOFRrBhted3A2yVVKaG2V/I8DrD7re3jqAec6i+FsRiXZ+XD/oLtrUz+y138RtvUPSWQP3HHwyOhsApxTBRWlDhh+A/pTqJDyGQ3l+d2OvUM4usNsBZ0Mddv9n+KStiUp9GUuYbnDNZZilLsWGrZUnTNOE+cmyrFhV56zuhe87ucm3BsY8ZLOmMjk//LRqhkz+V5qdWVlEHBC22fbiMr2BjJFAOUYifCLKjkus059jmBakVwNMo5964keZ5UzOigjJ70hl9hYxNDmSIHVq4TKBTq9ns0qkEJQiavJYNxOtjOHc+9Wj/ADLoxtR7ltDLQYFT8G+JZFxKZj2qK8d2BI8pY00ydPZRLqnW90NvnB3+6f0vwRPLvoxdRs3J8UOi7LhSC3lWo24Itz2p3rIA4tBuoo0Z9lkRxy7wR4PgwzDiZIuv00VGk3J/bVrajBxx2AeJhQoJPzEV74Uz/TYndih6O6l2LMsJ2bVesqgjtNrh+HFDnRr4KUliNluC2XaXlce66RIihXkwsJFfatIljvPJB6FmqQlXFidWHsjTPc/I9aw9jsccn/j8KYGwA2Ao++jD/F4h/EXIowkoE1k/5PFgyl3MucGYyoQxEQG5nMV3qUuAyr5cTXgfTY5QEx3gswuSEiwdefPb4DaE/q0Cf0yNUOu8HaIs7hQ/fTcSRVXVkqtXrjdQTtp6hJGfgMmRGmMEix+UDd08Wa4aEfwq9fdfbscl/hC4o72vKIB1sElAqho/nNKakhksDiDmRMfNKOTMtEYunHzcQdqGx2+Tiw8x0C/ktJYb3GIQ+A/GR0pyeNoIhy0PTVY7yQQUYH7RKfQA9z20VdKWIU1u1Ahy5Hpq0pW8UOw6JcOyOTeelsNWgZ21ZXoL6o4tQrTncuozJ+7PvH8U1mS3SObgUtUfySQmXP4zC8TER1yTIOUz3pnHZIvg2jXAtoH5oeBVi+T1N9VpvMts/s8q9LXGFYPTsyJRJvs3pvEmN4GrwB+gZ1prao8uA8LzqnmMAHF55nquyVHDYPglnd+HVoBS0Xx1AIbvLb+VMwal8Y9+IMT4BcA3bu6DtxUaDz6uuvazP6I3O/C3XstUsAvfdTM0ul4emPIEjFPSY8NA7uOoBwlejYNlXl5m92oz4uQUBN/5esqpngKndaRdtfug9wAw+wcFjLjbTnRCeiily9QDPDehpKQiv50loQXRbpI5vfyr6w0Y0ExXgf/krQ9dTVWpaznw+Zh9pTVBLNQfuXXmTFmWihSX/qftQDdP5CIcFThtlLTlJawVojCPflKDpgXydPYYL2P+5Q5P6TOoz4mpYV5WDI+EE4OpNYRU+YkK0ao7IKKNPQtBsognTETONm96dm+CR/3tphQSlTiSvUJSzYhwHuXzi4yvtfMPbAAAJ8IpXYv7O1fF1FH9orVpqtqd5VM5bw+66wl2UiuBoAIyOopCLRO56BQD1AdlkPKoSxLu4F1fGA7tZaOvWkdPHel6ze4606YZIsy1uEQD+nSI8YdjZimEn9/7erjX2kj2NnMY8Gezp06G0YWNf3KNkSV91z8fAZ0x7H96hEaO9GFxqCO5VWqudMGfIJKg/VmpYWlrAjHUrv06fHKEmzSHJ6SYyFwRFFDgzwMbPI7T3Yp9yTiG3vP0ejTP1LGAlUumEOWi352LbHhxWH+kQAVgerWzM3130jsQwUzI95OcJAAjhqP0a8IrMUA4qd/5BGeDDb/AXkCb7ezVP+Hb5ikToAtzyWMeW0nQXtAjY7YDQ9XXLO+viJFW+CMQ0+kQVry9PWr6jvuyBVUpSvZctTHOl4oRYyylvnDREv83QBPgsxrtzSV/yXt48wETTghqwJBJszDsnSS+p+ZYgAAjn5f27XjAlA6ZsyUqvvTBhCKM18vD5M+JpiHvJvLYNFa7LWJMTh7Lz1j/NBlBuOSKO4j7bWtKH1VepAXJTCOizGH2x4kxMECBBhlk88oK7+PnkseiSAnt2SWMx3c+shAPjmjg2vF50Ug/CTM8BzIXBZHIy6jEoR6lzPIqNiaPOMrPbaZKBw9R7Qnqi7voH6ScYQoxVMW6UFsrZE9VdaWq2gjNMOrLBkY9H2LgwNk77cJIZdEK/HYBw9vBuFqPuhnfarQQS8zzC1y5Mf8gtBotMZ4/yM6UxZLZGtH9nR9CGx2gzzkVcw4xW0Ctkxa27Y0fWdN3sRuRetc6kvFsXX4bxGQvRix4/OZI+uNwiXXnhVCUxhouP4xoSdagZ+wCDcDlNuwoyJ/TyQfDqtDk6Io8bVq5zyP7MkXrf4jdJxd8N7dYGEG7eQ6dgyXkRgwQHCwwdY5t0xT18Z7S0L3czxwtbLyoEAlnPZheYdEy9ihL6fqGZ6AuHPnD5DQOrvCqvB4pcaijapdu22XNZ2KsPigsGmX4VLJZx2J0gLpHmCdAS2mD3HXCv8AyLcPpq+V2JFQdZHmV3CLLvsJcqDpHIFyja1bNVyCNSC1wpYH/pqTtSOQJoAKonPBp6o6E6r20ERWUEo8tkjm7a/gpAo2QD1D0mT5XX5Z3KfEV7KdNj9zVo/zJFWe4dGhg0OXFcmFSAQ7x0IdCQ1FKGkhYstvwPw/ApAbZUMXCoRiFWBOh8v02WO25xaWwZ/5vVrIrwWyJCGCCVFvnrQwvXKGQozZ+UXUsXxRie+PpyOnJs6Lseo5hwQA6tzVIKsdppoK9MeDrDGXpeiR/7PndHpzYUc17+vi8SD9Xso1pfRGioLw2bIVJu+yNSyJqFQ0OIH0SD1q4cAc5mpvRcQq3i8hpJCfeGoD84xYh4ssyL4x4clfzSChMvmyAzowf4XC9kKpFk/3+L5PE7+pi5g5ID6DsoHMD7fJCtWSs+59mre7qWY5jTFR86yWcjmNFs9N7K/Re/XTW6Y65+105f0wzFgweNHDdx0D1JwdYChrQAC/1gStP9VmabLF0hCmjsiL7XK1liYH1SvTuweON9lm0Q5wTN1UK1j1Ph0sQcke0HUUVFwY5IOvcdpbLn8/Ym6Kazj+TtkGodD2yNKU8fs8ifjoKh0uDkLPth5EvxPywnBMd9tlUS3wUamUoUNFszMtN0sGJu71S9ZV8DL3AQ4udhCSmhhC3whiRgA5wWJNy1ntOlJXpKgQ4hHc1E0XP542DedpsTgWt1X8Na6+d7yANQiELP0ga2Xm6UkU+Jx8HtSjrFtWOVG8TAOsUWlmbiaPzpTWULZq1MuOTdA5Y/whWS1Rw8EhK9viKVxDR4DXv1RdsQHU/iHCdPRpx7Fis8jbo3vZ7TDdlv3xcMX3FMxFr9eoZGAbTsssqMzAPZM0u5E8Yp4xdLK5rmnDK1s64Krtqxc6L/Hv9ud3r0r98YDQbB9EO29CIl69SOMjPVWbp/B5HJUys94L8IINfyTgWxc07T163vrWoOximStPa1bC5KvFE7PVpcDjh0Bo84Eg3L4rYiDNU3J61A5+/GVP3dxB9bb+vXatY13lvevKZScENVpkWTioxCP0NNDIohj2dpawLqgbIPvGumReFTpJivvK5Tl9DptDeLAZpjRhChX477j+EqPAKPNLXPDspR2d28BLYM9ZfpUimopKFeOZtZwfX5v5oUEga74iT8OPr837HYk1lULlB2WZwUsddp+HS85eJPFI3qk0KnRhX8Z1zMkO9v5YuVU3P8UNTYDKSU30eED7SYlVOBUSX581xhE9Qg/zsFwPul2irTQY/FZ31GESu1yK+h/Eeiahni3HstMbUDk1W3raRDF0DS+LlnPCNoIQAlhcBqpHSZUDf3vKyWkYEpFL+ktLXUjNCG+ehpSEuld5Rzyn2Rs96g4OWKe3chHilVIKJj82boBOgZRUetvwrqxrp+mHNSEMsskZLKCWodQ4jt4s5EM3EYIRlLvmFIi/6R0nCoycLfDd0p+e8c7TtiCfSAG9S1abOSmKIAkV99vD6iZzHcOvFtJdRMMhIBbOV/Qlh69+sctfXCiHtGULADrxdzuac+a4yMr37a8Bu2nwlnTRjFbG99NSoIaL9lDUfimVV5dWXB4N0/hPMVDTJ0hl/XZEaUhm8TjkmcFRuzbI+gNj4J6VoyqmzZE3XHQtchXOXQdGhemVFtxWRtC5X53oejGrUFq/Pw9G4f4okxMJPFbZ8Dc4iTJ1LFhzqvnQ/5nSiuxexJvg0ZEDbsByTVWJXfcZOmCjYmS6cdnR0HUkzeuabBtEQ6D3CUMigxoCI917slmUuWjn3GHWNSpRRaQekQYpX6rV0BekIyDGQVR+HQwKsSM3VaU7R+qh9Zls2G/APj9IjnhLHbn8tkqKPH1g7TKxBtfzzknUqpIHam/k9sEPCMnjcvRUuklf9HKsXuSsLhAMV/eoa+TJGeF483q+Pceu8F+z3qzew0A1zcy+nFTxTYPkow3fBlqrhvLK/hK+MVZvuSOtzt6V5GOQO7rHhd9GxF6mN/08j74K30jV/9lpv6R9/z6utufp9cTrqDA/wgxy6uEmxj9m+6wfamyFJx9klwiPGqkQZrYRmnRvExV7tfpatYEX3+V9FJIyDiQOYtIIXNKTJS48eHNRygx2XaxA75T4CJgTAPirAeXszYQybm/Udq10GtyZPT/mFOEq9UcHj0hI61v/BOg5MMmCGykeB94Gobk4AeekgRYB6W2ntBJOMfZE+yqs2sAI8CtO+0Hpc5ZfTAQVRUw86xZ++wb8shU/29WHhrbkiWQ+mzyNdvhvCyMZUfrGmmGgmm20TszoEWNEPAS3Ytkpgq/vGjwVtUwWXobG7FLloXF20AEZajDh454mPcvrq0KZMob9Z6tlzf9CrIaDDdNZmospdQ2DQTnGG3wt6DaX/HKvgEVHCEqGR9XKdCGhm40phwtXqdG6CIqJYkQzi4tKASXn4qz00bqcUqOl+7ivls+uCOYnYyjv2KLnGVT/DVzAPlQhw4rfc3ZATuSvCxzq8jUcu0M0xPh+aTwAz23fiwkz2xj3O2ncvL8v/1h6KKRE/NfeWfdLktri/wGEJKv67/evTMTpIQJlK6uGHgEGGYez5OUruJMUCozu65rA9nSvsSEvFKlv+M0t0iOotWL5Sc8nNOIfvO4WNbhyOcPHBMtguf6wD3fowy5r6InTBEedSmKx31BVB6cs80a7vlz7YNhs7YAx1sT15Xihq5M2LxAg50tyby/bEYYlDXxfVzyC3t5o4vwStn70j2QMLlnKvz0Tgb0YHmMi4LKkwgkj5HXO6uR5tD3rhbTK6SPSjHckApSif3JrO8II+8yzLS4g5TcIie5ms0tzAKd8Pxjxs25xqZdEauU88zHiskFsNBLcnRVA4g4Nq8PCTsA8f5dxE6TFjX6a8neQgBHFTv9qnR8MwzsmUD1CzCZCtIaGQqFEomLdS2XfrXsa2a2m9GjSEN09kh6FJaInxiveOX8bJWiflMTSwDRgeqBHcN0wM3RFew9imDjQy7uWj0tMhMu+gb2dGLB9ukBgvFS9ZAgnrsdQQaExDAWRxLr7NtiP1Fyw9zX8VnRTNqxMCPd5TMTdG8YOg+fWPQ0o5bORirfTZYoIgMribRJ3DgqFSLj/ahXkay+Eo0zU16IOTmXvvbakdYDzCTv8dCqRqgVSFnPas0HS8E1ametvwYYlJajHN0wrpi/pLBQm3kOTZdnZXcJZ5Brxp3qzDJY0eULKISfeedpfGSdok/ZbLICGn6bd06wV3ZjCJhoRyS+IcgYyEbkCrUS9Ogb/46V9DIxsjaJLmuIMFy3K/RgdyA2agjKkMyMGjcc0suqJfY1O7rr5YRRXZwgLxp8tK8jWREaAqG3hlrG8lE4z+4tkOq3srhwJCR/mkmEFxu0V+qliVMFUsPl0i3wPar4iB3z1zOvvPdyb5g4XWD12VvQhMhuDT3aycSptb8GVXPCrl48CxL6dBNsd5XNBp+OdrkLt5ojnC+YGNj5F5/uRoi82bhgnB6gefo5TbqdtnceIOotFSjKCHaUQzZ2C81m6I+1SGLEjm6TBWDWgGFsd8aarNj3DKp/gmXPN1MdFh83XpRVa8zTMdDdBRNV/dJaO0hJnYi0P6bO3XIQtAltAeRWLVe9VMsC9UPxn/TBsR8mNCOkHEKrYwNB79Tz4/qOv0/RWKdQPmR3yuyOC2Eo63oFJJlqFDHOJo+4LELD0B6OQYMFJ//Y5/njSC9F3KO5/JH+4l0WR2b4kE92eTvVBkhOGEIIisH2kEvqTpTGyXAyVIbzxUIoxMKlg39ZHH68VKL46VBsNBTar2DTmOgLT9TCvTS6Bli1BnffnMDbh2vOgYqYdd60VgnLw4SysTj+ax04CLjOVd3CuiIaKzV9t9FD5N44DDu4VVVMXFoCx8/YRGjCl9K5aPxW6CdjxOQqQqSlDHFZTcdnRkO1SaPniKL9EEJ8n4f0+0XOnqWnFTVnxd/c012h3SMKIE8IS6+06UJc1gbfHhnjiUnMt+iPtjQefoZXesagizH+WI7DR9SYwC1M1YBohokx3EIi0xKU6jUoQoypNlqM2Qi7WYrF6xqv+sJa5AVskOA5WfnnjWJxRLJ1hOt45t5eE/Nsq3ecG9skDhJZcr2qIiHgCF2DRAPnilSixP+S9um21AQ8P4FMdx0Z6Pm5HneFYrUquB7FGgok4u23BEFbPhskYdrGEcxyaQ90KGZ62uSjUmdXzq3ia5J+BFM26qvc2qk9D+mgFJ5yZVAInsHUttQkBsSkyAHm4KiiUzH26V8en3JvFkj3d4/bD3bBF2UL5JvUEWIXh0dGPsnkXXM8ikVSGqNSNUeRSuNXOggoKUQD1DzUUk8LiIn5wyWFWuvh4PmMPahWAFxz2rXOaUdqU3isfNaOEOWpKh3LML6Q5T3mB8MII8tvFUOmgolqwoZf6sodWimS3EpZ1f6a/YQHR/XLztg3sYlW8OYTiCuT9lmQi4avdnX5OPQuRcUI6L2HD841/bN5mbQtrapVcRrfeW2CP5a8O6S9PuNK3Dels4yg9cdNs4upWK9u3PMi8+ibOzUQ4KLm7/enjcg/NU7O16hGuwf1NaIvOiGFB0F1eFDblw1ArjTOEM/ni2uhGSYDXWHdo/YT6q14vQNdXXlKWoXXgkorlH5qwPNTt2ieWD1T0eVnO+2PJybrFXQ9iMWyz2ElXvOT0giYE+WDi8ytvEgDcwas+cuVwuRmszbw0Gyxk19wfeCnB6Ax2aBVVdUPvw883Ry4g8MQhBJg7rCslb6xHdtJWv4TBUpACp+PPF58geslkrn2yQQnIiurkgV3+Njf3WLlSI8tZdMz4jTFXGs3PbNhzE24ipheKAWNXKnDz89tlyYEKJVobyjWAY4HhVOq8jRMFXgIzy7tMQIk45rdt1+Ftqm8hKDsJ3LoLX00xwKnPs+Q60KoP7esmJ6JxcBgJUsJvIHrEDFtlKZK0Dmohy6lb8Puxb3Sbqsub4kmA7Oo8IJUpBmRlPqHyf8YAEIJA2dwqOlXZW4ghq2cXQdeHoOaNQdczt2CACP1imdnjcWB/spFIeTTO0UhzkiqbLxc5kbI0lx8iS4EZ8R6W5zSw+M50x0IBO+H3yrE71Im7NKDXE/uCuO7EgLJP1aXlk1tyLl0HnwOUBgnZhDYkzyblD+JJBlq15CiwLR2lz4bF2WSRNSRL20pUz96aV8YNKNmcjsV9S96S0bPyQCtxFci6mwNGhFSdvA+9ggFl9spYg2CbIjS9mgYB/cUF2zqBTwW0brzAVAjU4ventYUHqVEwZKwFWlt3FuEahnt8T9VaJqdpOOINf/yKZKUNrq/m1nswre4hKWvLA3P/sX55QLg2nwHERPETdLluZksVax9YMwzAYeSgvOztIlJFV21gq6kwT9Nl2pkxE39gMHymh7lPKL75I8mx+62lZdQEmwig4ehSPQpB2s2+9o0rCbpUNltq5M68clo1BJP0J+XaYzgfBjE+O/He0ENLXsBIFBhfyYQ35Vd2snhDdOu7Vtpcd315Vl02cvEw3ztHjcjm8YJCvFNfxgvnExcypbkSjvENVI7So1NmfFJ/1kkrykswRe0YGtYRy+qF2kn1uFpRhLgi2ybIfB3C2deHgCHU/MCDZ1mgMJcsG2Q+8/EVwUrbHzfB3Xj49npNT8oG/agszRgO4LdW7CRbNVCIpoadqEgdfZ57zNe7RuHquCej60wx7fOs4ueORHidSkm2XKk+0i6LxvOf4A3cbD/1MhXCbU2B5DYij4skng7x5hN6VWvt+1797b6AKrGOD7rQ0np9c8Cwdjvj1nuXUudZ1XeCbedbwxNU09/HM20jBVNYtXxRxd+HhKEIFnXh9fFQgCV9W1HuMVWPq18sPP6Mc3vQ07z2fpFEMuZCFroF5hbq2/hKbAsbgHkemq4GgZ10z9bAdrH3YUScwfpPn8j3XppUNBvrqpfITUORBuzWD9Gwx9f+AAdwjL1R5M45Jp4le7qVMRi6dgFOAzOPu970dyofKdn9zsJEda/EsnUyQ5wFaPkQok1RuUOKcYe1n8fptTdxfSfGcGpmKj6dk/py8/Fi7TM/F4jS7VWc+HRTMqjN+ELP5gCGQgESjGmPHFNR+jAHytH5apuMfJ/T3d90+p8b/IhsxzFurZVA+HXLeFxKL/9wPas4xhBkaZxx7goZqNvwVPFQVHcyU4yhvd1lgnlR2dNHZoNZSsL5sxepod0qufpYrolNFbIu60Azmhy7jXrCV0DHhcxZTCQS+net7K6IlFWXuiFBmbHdSvzEjvDNb27v6V8Lfx7BWKO5bvGvumNwk/qlzKrfEz8LVxP+J+7MH5YarqczZNPTHEx6lKkb2DIDoIglpgUsqLPxXLUucRm+Q+fGqzck6D0qyOBvlx7N7xQ6MQogWnulPVBDyYdH834zxuncF0s6HQ8ufaEl4j852xkThxZOn/Qr9rB88ZY92H4aiwVKFWcDTN0afuXBrL/gbV9fWhnSf7+uVEHZgevY3WiEf//HKoGfSJzBLJ/17qEj/guT/b0SCmq+oSM87oxb3pSZ4gpZL/yzRIj1NPqNYe0MdHP7k9oVhHgDWrllfrNeXRi7+PaZUp2xJX2Qn/qYGuTwLOU9vWn0efvPZNWLZyEtZi+ruWwrNGfXi2zCDYyA503NnQyWHdb3rByi29MAYnwDf856a23cLPzFMbFb6hfBxJGWd+cPO/3xm/Y7S2QSbfsrvPHXNzuS1FL4BvgLcvQzV6H3d1bVfV2iHRCIt+lhf/ringlG1ebsWYhV+5l5nGmaIaP0Q3tFEiZ0/fzSlEy5EEaMpHHv5QBq1QmTMbhzGpSPwu7mi6CxuIJUD1cxegCB/KedP0juQ8i/rIEQujKjBNzzWROl7/Yx4k7QexACPfKXPaxLGGGYFypD7rLhjx2GGU2TLALdB4ZzpI4pm9w68qgjNbyZ0PNIY4brCqMQwVg+T5M3G6xDl0goJo+tyg4BxXki/mthk0JkiFwXeEy7bHyuL0WZu8HJimcKuJI1d/laOvkvOg5cyYVDz9i2KPX6PvXi6HYP65wNqUpq7lHwrQ70F6vBHjhYNTffRK2gUaH8AAk/HoT2H/1n6nSICm/ZwHw0HcekgSVqcopTdYX5TQDUTSNfpfMIUOMv1hkBVWVRigfa9BZ06usQvU+tBbNI3xWVwY3wCGIKYZL+0QhV/2nZXEcpB83bXW9Vzyz2Gs59P9SZ7JbecPQ+XrRfKlMUzhZqA3YW3fv/zwpqls4R4L5Gkv0csh4elGfDjpuktDWoyKkVisCKPi/otMCGHKTkm2F4mahpuHze4TYrRN2CEwIJF3zlWCyDIrYOWWD2CJK1tp+cVlcSS2zT5yYdq+D0IuFJfAqep5K+GN5O+JLPK5HrPZcss9AgQrcMXy4bE9sPdqCW3AKkWtDXaYBrPeYTCHHQvD/NrD/ZGjiJs3VzNCpvfeVfDANM7GnRYXDFOAZlaYJ8GHfMainW4qgshfJyr7NSSF5UgTT6M/FojaO/PlAKQODa/0jDNhhfm7RHBB7+AucWhQBUUjhZgbiKKa7LfVmFKvFjSV7TmOqF0tFtRpPhxD6F/d8Noz6s85IK3YHAGZaIUcKQRiP/6zE0UFOJBTII4IkFlW3HaDa9Kt0rFWw6R43+zpiSfSVtAexn5isM0qD7KqIEE3LIgFG6mjdhf0smCZi63RUcI67EIRQPANGQYg5rvNlBsfI1NxsUf5SLDWFR+qmvpxOvNylPuUOoI1ezGrHBalzv8HKak/cTY636WpbYqa2AuB9V4bRmltMduO+ANvMxUexYxeVpURvSTpDCTHhISWvLgW/NUo+HusYf3JPFAzTmyudyIsIPTQXw5V7BZ+bBsFvrCqjdJIbKXDxYS8TezcRvkFe5QNKUfD+tQTFV7Q93ejVMUnsByb9I5fkzn+e0fga+wBJRzVAlOf61yKWe1F9sJRS44o40KDK2oTasRs8wOL0SJWDCHGy33/KaH3uHDmyMMSNITb4/8+sutJf8tcjLAY1xedDRq+Sxt0GLt/bKGNi32g85ubtV+tnmD4bc79WZmnl9qKdxoRIBuclF1Er5PJy5I5d2b/MuKJlfFrJmJ03+OhWHBXk5Ft78eBKlbz9OdFRVRlSCSLBAq5DrKrLRYzF9wh5EGXtggd09FZTanps1uULJNtx0owyA2jbHmIMlfGKKISyJG5fABjNPxzaFplbrmlxFxnrKNNq/YIVA0MNrzuD2rcN7dJy/qP38WFAyaLSlP2ovFT1NNZAxo2P10pPgetE4K73/+jewyAS5iVi/UAgpse79BQd+5xQ+1mII5JF51CYcLqR1q0NfLVR6C2sLs7GayDWJSz7elCy/GqwCg/Fgj/GRx95L9pyQfdFxO58KQGGls11oosdFtSoYWQgtCJVbQbr3pVkGLa0NWUtgMRN7U+AhA+ofDbRVZBC9s8jDNheXuEIv+QIirWMulRHkry9tCJrTWLMWuZaR4mpBd2uYW8M550ZapdMEQx445Q6by5b1ajiuTYm+yvIvvCFDjsVOAWGaP9F7PKHQyXr53LGTiqxGh86Ws+1bsR+5cRoLIPq0IVQl53/wu0Oqg+XYhMBxJO6XIenf3JHsnZg0iBPD4s1GiUuyBNAS3cxCvaR6Om355sgMb1Zl/s7QxDRHPc58TWnCtHA+dTlaSpqJ4vtSxXwmYT11JI6hoC7NtgP5lzPs1wmDmYs7NLiOHkb7UhUKJRmeMI1DOyodSg2LZUz8MQB5AwysSYE6iSHzcEJPaLTze40JXGVPD1CtLVMvPoJYiFTYxTj8UqZrc29mtqqGA3HK7pDncXdU+oyNLx3UpeHdhYsYnAyXaWtDe4tzB49lfvuftk+0aH9SnZc4YoQCEmsyqI+v6XiBlBhxsbM9gcU10LEpChaE6bgUUX2CB2/0IeAL4NS09gxVsBC7SKPdU0QONQke1conEfaYvSRBBZ7Smf13MY9ReUW3a91AjX7bIkztMAfsP9Q3c6uifwpjlry92BtaZlUsFZ2wJ8wE3o/oT4+FgfUSmSu/lSFvjVlbX4U/XCVio1Zgnmm8Nm95jGrxAGFWIwectTJ1y0lctCeO8W4Ha4KIkwoNEDv9vB7qRe0ZaYqghWmzaERzkfRckXJOhhLTmh+QH0y63gXRjqIhRij+U8Cq017YlQaS44TrmiSoOJZ/lXS3U2nm/6UXn9OI5M+mwBjhipWB4zlESfZtbo6SGxAszMy31bGJIHMlxg5vcJFGjMSR8ESgzjMivQdrHL3ME/ZnQNQdOm1tTL1YeSMp5WB8Pcdz7YXmpg83GAYmYnrkeVbT+vZtJvdNwwvgJHLFw0Fco3wvpwMFOOPKLTEp6I5Z7+zejhE1jumdDscxpTQQv3sFcPh7vWttY4e3hFCIXMV0AoSu1p1O1TnBsD8DoNqvOkd0+WVixXhYUZeWOCGomiHvu3+1aXSUU8GGPDELIvGxWIWp9y0/zLwBIHID9i5r4IhiWE76cZu8BPQtdkq66u90/5vQwqpE0FsBxYAIZb2Jjtar25ybrJyHm9NkiCaICiu0Tdqrn9na9V4g/cb2p/8qMkvTyeRvovcoTdP0sB7++ue8jYfdPU5gPOC9IDPlSE5Ymfvu441O3xkYI7F9kO6acaOI23Qchnr20s0uH6kMVU5aj29ylZL3NH85r4huqzR+gDmy0vVjFaykDDCypa73mqbR6YbxHpQI12sbJz9ppUdoyshIsdZggk8t05FZWM+fugt5S3kt2kAm8mxXPGrQGogImFQao0ZTMCe/LKZ7tX+io6lgKi9DR+7Hnw5pblEsKAjsltwOx/d7ht7PLrKmxvqMKmCSVzKsCg9OlMz1OO47pKhZYZG4XkklgpUQMNyb7puIeyevzLv4bzSxnkohIWo9vxMAGt86qqU9W2lT3SZrjydTNdkgYh0hnzQKjgMz+mWtCnsv0jOJOgeHeHx5sBwZA91uBBzPlibm5NAQ7ITAlcc3bfIt1EAIgjngoVsBmJUtIw2V8Z/VC6IjkesU2wrg+PCydSjM7O1Yv/WRQUtp0H1zxdf4LnnJv00qccWDTIbz+T7gJgJp0ZQ+MrhgV9lC1fnF22Z9y4PykIDJX+9lJxexPvCxZWvT6f1u222qEc1GaCPRsR4nuVXAHNJPXBRIZPAM9ndoI0EhNtU7bUf4Lg7QRDICd5zXTlFKWHHeYEAjoDXXUi2hH7wzhqyCRPUe1mt2KNPpGO6fvo7Y0pcnZge9azuj8FsgjHQtb2TWL1WlYleVvfpntQ2AI04tfeTblayh8g3J6fhzK51u3I67Sv6TI1Qaoy5YSCWI4wMvlgDPdYSDYrVzgOnSdbFIWiAibksON6G3gUvdtfUym3Juc4/lk9j/0h+STi4nq0JulBIG5KfusmWjlQRrqsQF/mYi8rBqvNQNiw/U0ACFzJXCd9Bc2kEcuVxNKu21OWPBPjXywQXcTn+DnJw1DXX275ZMXjnsiejE7VFjCdi98KS7kn4o80e797xvQaExLZpErcLMqCS/VRLWdo9ZFfJLznCD3XpVLolK/RJFBO7Yj4uypPcNW43S2ffCSAWefdPabNmKENN70uTTcscaZVkEInXO+TwnfymQqD9WJfedx5y0FHVAF5tRNI+yHDRCkafw7CmWM1x5iaR6pYF4OWMb4rl8ygCab1KWC6fW+N8M2IWPXPj+R8e0yROj7vuAOxcYvqDJuK+o3eRjf6UCJ5+bsQmZVDU25P3t3wA/0ybMjYTDEanMQ64wGicl4lcq0K9DKgVqArmikyILrp7/Hq15G1DnKUf757aULlUXgWqr2b98kYPSfOgXmsuMk/4mVgfTNH4txvxKtok9lQDs9ic6b5J/Pg843/P1uyWC93XGMdJl4QA908y0qFZ44LHtT5uKS8KMFBxs5tJZmM4WP5h+tx7HU9endMLrvOt/sTd4dr3+wpKBHrZgrPzyfnxLVAnuGexQk/Q/8sIqoR1b27XsCc2KRJnZEU3aswZxUafgAIhJqB1Vw28PAuoYXAX0Bn3wwMI07sWHfvTgQAlCdyy7sLI3ZUGKL6kOSkhHbUPMl+QXoLbXMdiGiCSti/BEODBWBfnZryDHK9OJl/Ew/fevXqenIwf+br0peUpkOhMsgSKKgk/5O4hIEchegJSCRk9kgyccFFp8xiXEojrenCN2yMncvVbOd0ogmCay5UPQOKwLGt4nktwQLObFAzoMu5YQF+/KMgOKZ2qgOFAlnjE22zE2n/ZOMewTQquMTWQnb6FmumZ3Hi/nhekjSxEpCOMI7tx7mObnKTBHKO6XywU7x2PH+PUCywNeOaKH7KpRIGdBYvrabGtl3POk68nn2ojtRB5ykCuKCe1K3rj59DqfM68P4fmpWdsH4MhVtDEyNPG+yi7O8YVWIhTi05OQE1aqLRaWdZKKwPPNKvVnNe9cPVLbfVRwCaAsatxyVOzfNjLlaHuE4n+zvj2m1756wRCmCwS5T0hxPwqJqp28KrKKQhQUe8DqS4qZAKokT0jl2nFWyOlfzPUnl2vNo3fBvoSnrlL94nNx3n9TnW5Y1BB99S2PxXSR5rZoU2i5DPNpC7rPL0rMXSe9J0msXBbEu8hVocsdEK8AbSYl8y6MHm32uTcLicaUe22zTCGSdXiJvmkj+RqIO2SLudhZP2iBn6mvG6YlixUD8TCRk1gnioM1+jXnlSxAo3SmZwaE++s80X38yc/YkneMr2fkZlfgJ1HQpxTp/Y0uVxGDUa/zuuvnWgyLIZoeXt9NwbuE1IzTTGDoNd3WAlN8OvWWkYoZF7odh/rjdNLFGMvOCSohc6eEATpXS+h1BqN52cjq1XKwrfUHw7FC4aSQczDjw4xWIfk/6/4vQaSVvG9TEzUobOfndFGv5yA2TMUEkjRGD1qyd2HWp+uWRk1A67H0JLYJEVrVV4bxHzH3B/LECJVne7CzDjFtdKKNuhn3BumPK46uMT0eQNhvJrdb0tmFhfK1AmN0EjwJ7zIZWfkjMmdmESVixNYFfWqtZHYAl4bnhMOBvqWJBhUPaiwwqn9+5+Bo41A4+Qxe1rP+lcINq3esC8JQ1u0ReLwfzJf2T478R5qn7fmEw3AKmig3gKNGi6ZQhs2HVBNE/PdN7Xa1wsdhykdM0Kkzcm7ii0CwEsMqGNcgSTftcYGej7e5mNRquPPIsD8pkLrX4qTEfofe2dAsLDD6zJ5/3WJwoIi+NL6o+IncwczEx2lGey3e3qtaEHSyKZrztiG32W97Uz8kzdi5XKEmt1XRwNonmDsOm/SRPZOcJ2oPvvHdUdsbkq6imnWWcL9v2RPIpv9MlZHCJE993gANXOQQT4+Q5/GagjlYUIjtEQA0TC9p2dI2AnVCSVeW18cFd39KLFFHWyLK6Vh0+VSqaSlbK6TD/rR6Zl1/NdU8tpvH7d88Ygas7H68g+ES6xgDEDcxVX3E/Ch/niQFiboKgkIrKDAn3qoxU9CzzWpoYpaBH8+YeNOWFMnw+EclwP/OS/EC2qIMh8mZwUokli7mGzUPtgkdpvmcEPl3WcKHrWkE9Ibx97w5/5sTctFFVMJz8yPqOkmRmelMHBpwqMk+WC2pQfnULR1Q9cTEbMXzwZtIl+kOvtfpj4AlZxpNqvP0MRQOHz9sy4bfPnJdBWb+v5a0rwDdTgnciwmSFW0tlDOW1zGlJbMNtRjgBBhoyFjfCG6runFYbmDr5JGk3TJk2OF+KUluWrnT9AZndPpJU7B/p7MvA1oDvSq8j3EYcTB9APGasxrChPoCm94GiJg6SvExfnH1MWe2uTyqb6pcjIdsVycglgSAuS1x1JXh6Ujyrf/YhxbDWub+zo01QqZd1toqw8XDXTKrzfKlUnXy2ps+eXRcCfYBpqupRsW9/edrY5OL19ZQkVnx9ZNO+sSrZuoSXJSEvpmOwXHoh08M6hnHtHFF6tuGw9Nd5wcc7k0erRfsgFCVyaFbuMZSjls+bRJ79KIBHANKP1BhRWHBR+ffzRxKFnWwc2Ltspve7dX5/3c2ShjXCLZLkjcXJ0jCNKQjXI4508HitmuqQF4C6j1ImQagorApSubVehAymMDRAr/ZLq7P7qb/dQ067i9OGnUBF0ctiX1ceUI+/Tl8BjVgJVf+KduZm8Y89d+uTDFBuiOSwz8b5+noNWOVbJj2DqyQ7Z5twwNWYbz+TGz7LeI0JQOZMJUE4G84rzd4PdDMGb8D5bJTs5Z6GDhn8EklcXO6CuzilzrV4Ne5mXdWPnxp/2A3fpmZVrjX2Hj9s6gGePsgmGEiKYozhouFyaExBegX2LaDd9YJaoaWgHX58jKAzu7es2FmyPcNWwcN5T/AwjOE0u88eEZ1BmnAkluIliKxknEudFcb6qeaKCqNLIIMazC7dkOlPsyTiGNSR3Qf8SCMDuUDXHpLhssN6r71VO8VMmDQ0eOXHfIQtewa2oEF1hVcPgrvoUzawgBCqjvzGjv4I4tq9fNNVqjHasCTAUz3QCp6M/mfUwxCqnju5VW0m/PDKZd5MJERb9xdQ0A5o2050sZ06Y1NKX7Q9RURPbhHV+Ujua7dhFKG+/uox+/8pIiCCowz7xVWthLP0892R4Tf2kzRyXZoZkHYUIPe6YP5WFI2zsRimd9aI8B8S/mT+3WjuUvWcaqIA2hLQKA07eBKt8xa0LH/G9TShFfFUPzt4OZ22i6Sx8qLnF/EixNjVegHhzW7rH/e+4yE5wwUNg+IaoSO1IW3kUvenLqUiIbpMs2a2T4i3EmrVtL8QsOrUBO4TJf5KW2TLdKJTDHrNXK3ZcUES/BfPWMLTzdb7EmjkX/a+tkRDT45q14P++LdPC0lfvmcpYoGli4Wr5BsZeU0byyShkSQwh22+Ut9T7zqkPyAdUX7AfnrHiVoXYoPuz8Uy4AatdDrRaNUC2BpYXUgvdBSLvpY7bS9GZTJ7ZrcARwHkCkFuJbDRpUfUwZAZ5kwcYj40gaZwUhcbi2pd333qlA2J4NK0UmATHU+nRBKFiH0OsSBwloxw79mlMiWjcLujKxY8k17Y0sQd9EZiDVfPwknk94isdIsj3e5YwjaEp+AiCxVZI0vlFoiDpAbd1tw29jkx67oaWYsiU4HbK496xnRlh0dDN96JCyFbdRB7xntT5XeKOclWHNcj0FEf56s9K0bP3RmXqs9+DfeB3utJo1hW97nHqtv/QfWWKVlA6yrCJvpGPFL33Y9XH6/QRc22dALc/neGxnfWoBfBWLkjGn+dIHHEf0KtxEV1WtTK/8pr2+/+nF3UQNm6VQ+hMNNW+iH4FZa0gI8x4LUgVNBeeNPIHzlQElxPOL6zsRLbsZ62JaxlkjzD3Gwii/IvYRr7H5NGW06COeywnfUFoNFLDVOcPZqP7M/Lnzl5d/3wGRsxdnrmZqe8zF2crjjUjZmPEpEbWrXH+sUzkxgBVuxIjFhUFPc5l7XL3UBZUVn6gpgmG2X8fTv1SbKmF5OPpDYwEmXdue5RiS4Y167pk5kJayirUq7tdGBhyVmMpCWe9cSB87aiYIXEgRTdaQaeeivJVNl5MIckHWJn2YKcf1IiFrUpoRWm9pOGZmiBc5hP+Q8T4BdXrToQPTNnGzrsokH38dGFaEXwo8NYC+kmSH+Y1R3dZx8EFlDcfxuc3dcvbzID6gXeYppDBxyXpnJuu+KR2umkKrd2kUppafyvTsm1g4cEdH2GN+yryu3Lcvk3qLLl4sZz/2HDtAY8EfS85SIW/UCjd0FNFKt0Oa9nu/Trqv9NOevxlOVWpBvqRXWF2VStke3VwXexXxt8wQnPFpM3g9ACHxa+2Jyr0b5ES/C5lk1gNbMFeV30MMUms/moE4jTDXe0P5+3ZSB3fAsr3HXcvfbIX9gUn6LGpf9hPyxNjpkziyopMeIk9usBFCYak/wMNws+0rO6mbtFblTe7oPpnPrY2FjLRK05zSEAMHiy03sfqMhmlnz7mX7JMAP1/UAcFfmMxzcxvYLW/sSo4PAsZOvRlPAb8Zyzj8kirguYX55qmQeLvY4nF/PQGdXsQYzu24RRiAz4Z8xuj9DLppuPunuc3p4aS+X4yzFhM8JltF7Rjh5qpSA2PyNFGMLskZUh0awE2RYGQhDLxSzsxSUAWKvpm3eeJcRphtUQQ5NOfnhwZ0zhBQWq9KK0Xfd7LBInwDbzYkuUugpZqWT1D7U86W+D4kk5Ii0hVJQbKufmFtxKorkFAeqxfhPhH5tiz1j6P9eunFwZyn1JDDyuKkOHR9jJtng1wnFd0SRJa09TPk13tS2ofOGx5WawN+3BK+wWFaLLOg6V3Co/JQIIoWxBNWseBOFWoXirxE/QaC8nqzeumv8XkMaRBQNfwog2a/a05QRfvkmPgmaJv3GNGN1eyTaSW3V2J1Sn6OA5hVV8hQ4RtoqU1q+Mql/N95ynL3Vx9GYFH80E4L1v2DqYHZEBk7lOgdAiiP7GS94q6XEvZikiVLRGyV9ID0PR64FhCUREY0xaqb3bQG0PW5C+CRxzKvY/9SEzszQlDPSBUCPJq+HerZrpN7SrCliQoLq4S0HtVodDT6v7AV24m35uFxB2mPharUJJgmWEN7lS3hGKtIF8vFEkdoBflAjEzPH4MVbEJgqTtF3m1je5GHD4vlt0Eu5pEP9SI8KSeHD3G2vN0LfsTHARpO7GvETbWUmUrezhvgAVYbBBDwPTR/FlGhQmyWmjJUMkJxROgUECls5gOt5uom0kT2UpHy2ZKaul9CHOBEtaTCeDD/oBGloCYMddFZfQlfM8DP+lVOXxkE0K1QjiLeiFmM+YaJ9fjFvfhkMRjKQeWS8kp79aIj0i6I6TbGXkUdS9Z5WzGIAl8v6kd4gKT4/tUzXNmjCT6a+XI1RrwbcnL0PSrZxxObmSHVDLOz3nqZ+FgTX+Z/VwHO7+DaD9Me2QaGyuyPIODAxCQ+tswhue+SlWRL5bXV/U/WvU7eaRMClMHIPOk6bwsFPiWpiMCcO02NJJvl8X55qOnpkXfDSaOmSEmunWcQfnlOD+grBlvvuiR2jvBvjuwmTlSbp1ra8IvEbBPcbkV9T2wHu9JtqeJgW2pgs+Anxi7JIAsv0dkNJ6jBhFec9/zPgLO8g0vgCjxvjmZXLRofbB/FLt8+fn97zncfVE2nu3sV25ihIrtV1LHT5fbeXZV/+sTriDS8aAReqC8FC8WU0NE8955EmFbUMb7YFL5dGgId3K+T1SdzJHdp2mWLzfer1kYpPUdW7NQl5C137iV/nrB+thrZg8so9yXMzD6/zdi+urlXr6u07lRwR5Mk9N2S9x9JbeqVoHac0uh6QKAaR7dA7VyOmrqb04u4/64c3EQ0CLOSKcMHMAB3sDF2Ca1KreWaqKRK54UHUeNs3sk9x5W0zBIOhGLZRQne9aXVEbGVqMMn5W9TSWGd2JCHo8yAH8Kfzjyq2GHt/VJCxNRrIIBCmJg9rDY/YDAbi3DwxUSOcIk0XsdPI1dp4IMGDFYoxWw21gyN8KhBq39hwz1m26O3N7jglxJsAKv69QMKurBTSFSSW4cT0Bg1a8Ndy24tYdVcwyqhpb9gX9c0IT2ZzEYta07G3zLj7+1PJt3tm/lknuMeZiviXoY5lmDXIgEE0JycLmfnZLNMLMlYYworCxB9I4nq8jUqS2T9QY7Mz0yPJHCi4ge7Jfw7J5kjXiRKOa9a1sD3Oonz9z12tcHVZeJ/fjhQoMB4BVC8c/9yloCHgAAEqH+Pa9QBvKgC5GORM1vbj9nAZNTNNmG15Y62U7g6LUXdByUkCCQD1Xw9b0riP2MIqg5u6864DPZqf/aHv4JMn5PiJGwdUqGxtwdcgFXlTwo6fqH45COSXhCRAaU9X5q5L3rSWRp1JqtMgv8yKO5jxXl+pRVMwWAU75efRMoS+EdwwS04Sz7Z7MaQgQsImf2/tj9vtQUheuWxw97x1/i/42CjuHbMUTlSZDT86t13InE4EU1b/683zFQf88IL+Y16+L3iPibL4Nji2K76hDcmLyA/xf7yH3rT7zsZUzL68pFMX7AK5ubtGja+IXK5XbxUHEs6tncJXPC5puBqSuFGIiFPDaa+PXg5l75IaX+uoCDHzrUyiFgrEscMaOXdVUOaREH102Iciq/QzW0vUw2iu6gHzL1KtvGC1g6OelEMH+oxsJop093rLBtsEQ/IJ24jdvg/1acUewfCLtBmNdRGfaBasbyZct4lyHDrh4jC6M6f1xXix/BH8sGizOnHmon69KARQ9ewR05eancTzmjZr+cc9YurO5vmsljTsNk7+5qGdbFNizZ/7cA7Sjp/FgHUajidDHljnrKRI+esEPQLgVi74TWQlJMmZcNvF30b/4bLjbmhWIYSttJGuDYDcJ5ok7ugxRVkiCNBwmJ0bxT7kNhGehSJCUPBZKFmV95z8BZr69VqH1lTW/v7dWDsCkycZ6yNdHi3swj4RWFRE+0l8Ja8N1p7CZEu9nWbdx8uN1DK1Ydl1XJ12gQn9DuaXU8N8hSTbApi9yYlWIFAa7Sv7eYiWFZFh7vINtSVUulZGzMrIHE9bC+95YRlvP/KVP6vESq9xed8mQsrkQbUW9SnVzl4wClmNeWcON2aOSyzw7QkmT5O4dN+3B+iR+s5fcU32QGICLHITgLQMJUu6SpEhjm5v/gzwurX/86mlp9XbqoQEDpXcCBO5d8RosHgMna4Ltd90TEevMjTw0OQrAhWTcONrCi8JJyrssdfI6q5RE9RFd25M6nqsyCdgxKLFqtL1+LTxhF7jR9Uuyb853EPhcPgPG5Kv60hRTLv3/uxP6jJCkqQKKSwRoPUoWqWnlFfYtF3s4Kx6DRmHkOvZnCyp5e3zTpemDnFJZaEIjYFH9FAyqR3UoY9WwatfJult9afJ3pyFrnPucxcmojbKv2FpmeyuM3Bg6Ea+Vck1qbvrYQCYCuF0GL8G4ATaN9Crsiei3On46D6Px1XHkz6EIohiEuLan7jC6KeZJ2VfpkAVArzz6qLhGaocpTGe6gO/FDzY1IZ0ADqPw51SRum4lk8dzmqbm7wFGakNJbaGaAj7ady/o5aFYDfN+LYpv2kRTXQMPL87/njD7X4f1BNTUSZAx037eVVM2pg9xZgziSbJJaoB9dTJU5fNDXy5VAyR+J78PFGJDCsyLaAnHcj1ry5JpfD3xsMQ4eNASiihqy95S776bB6Nf/RhXHW9J0rRGuZ0nCgZMc/SceHigUgCVWSLtsaWl7230AXxw6tun7ymUYp2/fY79R+C5T72MhxO9IQb+vxkX7GUhs8JfKP+nvjB2UzymgBvO1SSQKKNrZcP8Ojg84s+/qBFXCcRg4xqERugYlxCCtcB47C3i9DnbYujXbr83Fl2D/G7VoL8YsxOJ5ipc8kRO+7ZiBeQ6wLt7Ot/r7eBvsv7b827tGoD33Ss6S5STh5QecXIl7daa7p2jJaWhkFEErjMKoabMOFsIFgSC0QdAmy2F0kFeuP4ps2SaHzutMqS5uyxyzfuzQbHxVNA0hZ0Key6OAo9yfqJRd1UggA/D1lWuFzZZ61alE0DlfTk5aS9rHFtj15Ehs4J7LKQXxsXsZetNH5E6/Bysl+aCmXQun6nQrxz5JtPFRe6560ulAUlWS0SdZbR0Kzx7kDNcRFnXsoNLSYR3uXODCUAZSe9CtnoF+kZqRWbu0d6Ib62GiSlIvcECqX9s7goxNp0oTspUYmYs8LPNgxbM1XvTBSzGojZuXIFmWyGFsWhBC/GTU4Qc7JN0ic8yQ1h1qUxGkm+hNZfN9tLSEo4WPqS3Z3gv08CNbM8BsjHsbxc13/VYpFVSKL8jbN51y9Aa9lblAxKyTukjqdbzWq0NlRQUd5UdsWPNb98WlPvjxeZTSsLNJdpNx7dy0/ax3xZ6qr6aTjNGuqaUbv8nXMV3MblSBeeItQYTt6jMJqKPQU3GSQx1hzKLCoVbp3LF05kjfTwG0pWPEMjH6WGDZXt6XcjiB/b2t6DnqezVQIP4x1nc1S4v+E9ibO6Xt8UnB9QxJgHWEUGChOdHTXv/8ivLhIDYMt8r3QiU2zoPSbdjYZsHe6cUW+/8o0JPEu4sEI4FTyQ/TZpY/aEIfdMxpBdCXGiLd6Gwb2qVoIx/jVtItW0f4ljp6Ac3eCv1fXLW/bEfCZmYDrOCGDR8B89cQkA+2yyk4rNaK4XnPIewgxoIjRav5o/KSl9OXCnhOCe2FXHqaaQQGXIDqsfFkqhgRzeNZj5a5DTTD2vo03C6AT4K3myzLUaPpTcPMb/oVo3GWpESr7uidagujbm2YVOnuYxmfjn4tBFgdYlCjjLqNvWQXgttAfwmlCxeJNOtvld1b0WWhrQ+l7kKg58aUO5uBLI/ZMkn3KkhFWPBeAg0S1Es0d1eS9wIM14KrqzHquy9NvGR/tfJEetr0h+yvOxJv3kqqp2TKB4WDKwPWfmdTJ+1Qkpemuzc5EVLtLLbBfwKiHcTi6dIP7g7SykFWR5GI+ZFQUMJmYYbBwcW6Ln6uWZ6il+or5ECqXa48/LUMC13FAi1KjWsziIcECpiL1xEMPhiBPD2D01tHDiAUd3RgxnoWWz8UWDyygLETSqhHsHPz28h5lxYXPymjZaDVpxzJdvGFajzTRSRvXy7vxWMmcIp4PHTSzmLQbgcR4ColRCjQdfDm7/Q4ydxeE3bz4udslT47Lmsyc3Yu9ZK7XZvqZXVNPZ/6vG1mY8KZdhSBZXBCcuXEagvNvLWvuXhtC48Ed3TRBbUn6cE2+vJ/pxdo1EW372TFw4mWeykoTlGaFbe2yu4/rU7Q/ms78UlhIeX/LtV7D451ucbZg4HPMttb71JD8GuMvZ5WnWGtFt+VdzbyO6+8coB/GXpJicvGaGgN/QYvaWTmW8hVaRQgq/DtEemYxyo7iE2DBOa9Ro42yk2ZBPCt9tjOqPGXVAgZAFcFYsk1zufwwarlGHhskcMed59MH2O9/ts8yjZWm+AKHNvbKin2TxtRM/5Hq/bI5Ej51jv0NPMN/ec2yTCimczTapA8dNQxxdtl4S/ReDkLCWpR6ITX/8pqAxP9i7n3u0qbeYAzVkKHsA0YFhHIjgiorwd/cI6lxOGlFR8ORTDPhZDzAy+6vRCio3wSZryOY6/6hOTODvMU87MIZ70NqWaLL+lQYoKJFRzB+E9pBY4N7G3PKtQi1Qu6JpciHlTq3HA6iH+DNYyojZBxf/GSzbpAFgIKIBz8C2zFTYvlD2YmzTYGp0Zo9HTqbhwbfDq+H2JzUHr1WrpM2yJWaWmHFTxwuknAbTawA1HNyxT2T9lFHO6y6pDxkmZBAfSTBfdil3f4sUVYmiEGfnt5ToGUtqo3k1phKOrwLUCkO4V6FMmVJ2fX1+57fPEQmcUW0Tm2jTk6Qc3t2guzNRaF2r2wv24zSeT0YTPPO38Nv4it48M/RYJATqJ+dZd8S5++yhk99B8c1BSZymyCXCvTjWYx7okUNk8uqxb/Ki8dGL6uOqoSM5mgCLjfRGvI8kBV3boiG7U9yZHo6G9B3mkxs/IiNHrlWTwzRE6OIXmR1L1eWh7Iq7JNIwDdDZ+8OBcVVlJt5yzgELeC51K2DUOnhPrQMAXWdJgOWWKvUaZxm9WWWFg2ZPD+3sd4vTAm0jIcKbH+jbAQhEXY343rdZFIdLIHt2JKLjaLtjknsG1vIKleG41KZ5zOHyDoOOXEZB1S1F4FT3w84ynZyBKEP5lp9ie9kayMxJTuxfTVCs7XRXNt1rUcUO/1j0c2lus7sTFJrUkc1G1cg/u+3euF+h4hKkKAHDLRVEcWnHfIuatpDDv77Q38mKDXLYuDfUcj/FHNkaV0PL+akYbUSCb2ezoSNKy3bru7le61fQ1wqQJ9tA7ygYkD8yb3UZIM6NS53RmVUSAJKXEjM3XVLufUvyKWi+kHIBkqrMkw637px90ZDE53vck/MXrjX7GVUVEGfsTUN8kTATdARZ7SNE0TPCATUunIM6WOm1qbekO/Ooix8PJAo7f9JUw4w1YF84bktDn8DlwvPrXrEcdGumjsz2+ah18YQTgRvOX0IhQ0ww0tDAeY/Cpanee0L2a6SknpO9vFwV95gSwi8qBZa4PoiBIhFuTWBS9r0y3BL/K/LYjoaqLeL7nm0MHUo7V5pqOGbb0+/vOH01UfvtZzL0ANjUxootri9LTDVM6DrLE5YkXtMn4+ui3SeqDAUxzXc9SVk4L0nm7qvumF/bPfuevDYwlVCunbqSoOOYa4ZETkOa7khjkPr18xGftdBeONfN7xZ33MNp3r5a7tlr1SET8iTSKnSmmWJspkkowz3MmH1tkiE2/Vv++Srrwhm6hDjNdaWLA7i9x59uUyadIMZYl08sLztsaM1vSkRXSC0u+h3XSvbhh5iq9n1uXfw7w0U8dmL1SzsJoDfe537RQHWTEp2VSe5iBEGcG2jX6jL3Kzx5Sn5V6WF4xjAxLgSRKJRUxjwYrKyFZsRbwLkHw91wiZ04L/yQKzXapDNTZZ71/bUXVx6uAHXABPgipbgExQr7rWS30s8OYb7kWelAgFfViAQ7NgirfBJaRe2VhyxTVPxU0ZOSxXZwBEiHQFCw2G7CskHudc296A9dhbypEFZAsqW7fSChxT1tooYI9SwQcVBSK9aiaiJDbauDckiRSgqWdsQ17YnCueeBEFPqSwi5uOEHPzdi4ZKIfOYXV0x0ZdHab1v9ecLKEZzSXGAKl97XLiFu+PFUup2aoH1RGf1FgIL51VhhfpEw4xMADXW2rIzvANIhNEfgh8BilRRkJ++6i4QJ37UE6UpaRPJXhf37UDzdMgQnCgFtf0SG4HDcA0pLaTDexbn6nUmPNGVtXYm3+3NPCw/JhpLzTNWst2tXumkGM57DO6W+FkbLBmSl9T5XbWz35lgIqgTsA0BMAFXjKJxePmtb3rASwz3HNOZnmq3IAOU1Dmzfk2qFPSTy9kkU4gb+T65CFgm7MWiZZavazhTYgJ0AdyZ0vEP81HhrZXFkodY+4JbNS/Ao1f3daSTqxaxo0qg3y4tUlyD0eGRDtZPafdphRiZktou7Ni6CEcw0Pxv4MWDGLy+1sBOzHq/XLoW8baw6Y4nbbaMySmMmfSNzTZWR3Kkz1/04ET6CwoN6SOnyyqg5EA3xGYLv6p9TZX2I8RJEsDlCqEw2ZYqd1gB0/n/OC3SDSGp0HJNunX+EFRtw6QKnLmPVGUe34YfLLjlmFRkCDeJpwN+3Bzfo9Bo5qKkYGYL31D49KjFlOY9UOjAY0xrHeJunNcN6bHK6F11mys12h1+0VTTc4bhS3lnyYSghVFjuBVc/1yw8/wasYyll0EfhyzPio4UD3/w3Kh1R70Rc7hNLnuatD/lHo0LV/zH/Z4niYd9Ayt7xr1uUwH3cA4SLEOzboMhFdP6j5zBiASS909abyOq0NaepU6ZzBr/aHKRj8WAH8Zj9C/ETUXjl0YZAVUvop/OOFq7OfD6E3J8Y8FrK0V7g7RdA6/c9ctfr9LGhUr6Jd/gnZDBMyQh6N7k60B64UcVvfev6gMSMLxH3kyPWP4pRCR+p1gI7kRd8Bhj+ITk4YsH4CwKT1MZ78dFuqpJyj9+WQw7PioJ7R4a0eJbdJz4b73yUoyB5qvIrmz0ZDAdAjZ33UseZ4UelzfMfuC+ICCXDcB9YZH4DBOmSQ67SICXIfYgQEBYk+US+wrH3wDKj6lIbj50omBcCkA6aq0zjuoi5CmIe/cfI/WYfPc5hwCKimmgYbK4of5Ko7G7NdfDUwgdV964IgHaBcEgQOHapix7B3sZKvmxeCEm+7PaAvruaVyCvisBe6D8vw9dnGd0ZYYPDSktlUsQMYio/qZ0iDCz6cZ8B3a9CHchEswWzdDDDApFFR8xo9xGEFbC+6MEVBNhvAFgWfgfXH7RilJ7kGd6jIoRACOfWU03wPZziugsuRvZ9h2Ok4dLqTw09uTu5GT78lo786lqEESZzLseVXaP6b17H1bYXIg6QprhzixVOHTcDW5In+YY0lDQqSruHgSYAm0+axFtTFnx05/RuHHm2yT+AkBSQ1sOJAfaML4612A3Hbv2+dwovhn/FIsqQk5L7Ltt/4C+OTDRK0fB2rMGbWICnUQ6R86wUYuBXykG5mE0f2zyU0C1NImAcw4df1S7eYEJH4hemEidno8Awk3k0Xg71GbK+5MqjM4Qf8nZQqmVqdMVplqQ6mLNbTJweV35+K9wgRzBF4OnCUub9XMBBctBcOFt0DJuBexzDWS95p8SiQQi2OGP4mbe/U4naP25GTMOTz68mRZbcu8aHM6YY+oQnqFLQPzmGLAOouU+6OpBeLv2H0V9+0JjbI0Z+uODqjDtyy5RivYQGjHY8Sx3TpaApco3GVSgeHM00uX/H9vrUSOx2pFSYgGHfjv3K52tb0lr8Z15otg/b9S+n5t7JbW5X8ep8xwJkaDqEr34YGTdiG4he4zjJsJgsBzUYLVZwXgY9gSHUTXr1UvyUx6bsxPl9yH2Xx5L+WQ0BMmyd1tMemCWvQE6P+S4GJ9i3mo3w2QTCFHWJTs4gUB+BqQQIUrU14LM6lnANHvwyVbFTpfAaLffBS8R9PoBGSCkaDywh54CqhQ1lyI+by+/82OGii9Atrjq/gNPMGcO6JoAlSBBrE/a3mUKom16J+mycBbb0BGMuVMOqV+pUTLSbfMgVJG7smpQuGjyNCmZZff0ryx3d13g951mmbPIe5ecF96iRwiK6oxXN8psa909fnkqdxDrKidjfEw+COUb9ibftt+QnAYp7WweibnPqk/xScwphef5uAlfbCNljTZzqps8aC2UI7bbRk24xvWFJbV4JSfgf7VmI/Mkpb6R/XHiP0wrg7WmgRkpoRuFjAIkXmDlgKvkedD2vzm/qh5AMyz+2ynMS081YFO6k8xj/W4ezo4xrhIVanbMWYXEA6frGMes2ObwLttfvZljPzIATsqZ75ERL0hVudoNXewP6QGjiD3yQXN+rqSe25yVHp6DR1KDNvzt4Lx6vA2JxzBrof9BjXG8PZvMfF5g+mVIsgct+QbB/lHnpK+g08Cfg9kV+SxM40ALsHTBqA2pKaV+OSr3yFCyqVappzv5R+LHuC3Jp5g0eO1Xc/MD4G94I+TDtRFtvtqnowkeB3Ke10J+TmZq8JM/KtFVF/d7ISt8e8zqez+yrt5B5a42ByfSmSHWI0Ck8M3X5TwRJl/r3PmEkTSHHoKJfVDczKhp9DtdRrea5OLpUWMi0WKDZ2a4vt07vIW+2mmS+hq+M5yjxtksBEqblcGX4rtyhAfbwH11ofJsBiXda1zmGXbemKlLqy2rqCNA6JWSEO61b38Qh1WHA3liUKllG3VwtGrWRmgBmFjwQGp3aCldp8klMtjJ0a4Vxsq3wZjvWGBrFUTRCNHraZ2NFcNtxof9pBHXQA0Upf1396/RJ4u4rpPNONr2Ro9RA5tvGfc13ijK26IR7gWhEaQqKqWm1CveygJ+/pzkYIH6ERbi5fnx12QKi/qHobZd/R+k+vpG3jion8lywy9wxXsgLWjiEo+lv+43VqIxE1OLgLYf3EOJKyAXDWcKHi2CAxXt/8Xrf4B58nu7oBf2OayWbHz3Cev3xCMa5B16VshIFgH+FLvD3tiimoftKpl8uhBDyaIMHpXghaxj0CuhkB+UWodCmoX2+NvwmcXA1CiBiJNjO8JXOGJhwwrm2zkrkE/ZFP3oHS/2WOOT9Mu7XGXCIysSQJDVKbyUsuuAnW59hngPxNbTvF72TSXzRsW3hI+pyH+aoGiwy/fRFxo/6MokgN82V/kX5vM+5QLALWj6nsSsO5eIXOECKlXFcMI4htR0wgVXSNAdFUUVL95CAj0FOcKQ+sCGC3IfEXBdmininDvsMf9mSuDgpWAUBsdfHibgH3msFHe2/gduqbv2MKfO+Q5jRhIzEI5sdf1wgcyeFUlueUBoXkFYzzubwYRUmn0Lk9VUjVMeExkEmz6mtaMw8sgIb+UNw3tefEZ8tegKsXz4cqojqmb4kPIA1UAsUw2/uw3r85oyt2dQm8pAM/Q8uo52cJBuOGmzYB4hUxwDJwoYpVoJKZwhXUSNddCoVqt5hWRI3X1oyRptOtg4QlnfbpaDkr8fuT17RBZYOoKu++9NLPF0Vx2u3GmEDgcxmPgJr/+prmXHg3mvpnoQMcxLOspM+wVgwUamMZyIqqxx1mp4GbqpO8n5TIdl/asATo1ReXQZkC3IHOW54zRk9NlvuVio51ZgjtU+aJRaLaAmN2hf5vaabIcwScfYC1076LCogMhrTJlQ6+OV+z0jkwDuWvqnL8w3qKOf10/qCq479AAifVW7m1cUndC3w4VFTTqec3iU0EuCjeJBrdjlDJAhyws0zl0kO/4mB3aiRO1yaeDAE3TQ9PnJKyNUlMR56roG2YBUCLpW3FvV4RkxvyZhQcpHh4+VPHE0z9fS1doJ5usXIY7fNKi7YyZeZNVNtUxG/0E0Zpm3mBhM1c7wtp4NqyIsXWHjn3oMmPz/hy5xIR5FU4rdE7rR8wdhNpn6fZfuYKq7uUHCKLP2UoYaREcfWjY0LH3V+W5GOv//aXQ+Vc8zLzJgH5oStfA8V2Nkml7P9vQXlyHsLtqOlSrYKkZe4GLvjHAtiUp7aBJeiHU/mltw0Ze8rrqLmhfK5PfZk1k98idMeFMt5QwB+eymldCN1PqtoADW7pYF9mRKkeSX9YyIL+Xv83RNhmn0xkDGGEPaMSlqFUu41EBc200HKUuyS/qQXBozPmh4+HG80K4kQCqcL5tx7/JjorupILzQVXVFQIgSOsRPp9dObF3Obdh6IuVxLpc2feW7/4SRsU+4BZ95mFOyOKZ3I8Vgh5HPL5637G3LfihnQE2S5rvwABYJ743lXPqumf6yREV/NJrdryoQUmMUaiKk57kViLti9ReJGxMyV8z6J52iTlXCKUxduMxj/LIjL7k5zKsUHTwpSU1jbCwUOxPI8TWHXRsf7H0Y7ashBD9hZamgxFhakcgQEiJona7jXpRaBZzdFh0o8HQ/fAQWdP3T5cZb1HVfNLG2he0SlF6qiqY4SBJYnnTliBDrFq0XHL+TYlwNKwAjoUzR3bY7ylshgv4vgKMREfx7OfUy6rTBmC/3TWh7CRKlV5xNeBNUmHS1Q8BGeMeKRJVXzAbd9/5Pn9cBU5TGKK9xXhfbakx5TJdMl9Vi70XZNI2XMHrD7DmvtbC/0UqxHSEEuGnj9fcX3hi15oajvDnyrMwsHXbk5klo4b2jf7E6dj8+Rs0Mz2p78cxg6IcAm/5dPxn9StefzhEp9Dl2Naw903ygC9v+4/dFxnFWiueClRoNPxO7NTSbnYx1f3EfF/tf6terhwpNC6jdyzdgs3Qj6PxJjr2uE6v2zT2Ck86iU0EhpXl6txbVNqPXlM3gqLvnOA/LaSiHdevPg6K+5msql2dslUasGrAj7XtjXqtHAhqPbH+19KJr2oBXjfQqnWHwLykj15vshuM5M/TQ0L1gYSH9hfra5ZbVkVxzzZJWND/mhaUrFr5aTHCSCYw2oVg68HmfYosCX49yavoh3tpV35tcKduZavMtQhAikAqIlq4KK/tJszCxrCvY+3sFIcoZbr7uIVk2t9UxDg3lsfrHcLpi9yQqyCh6zvYoTF3sXr2f2wNJYSNS1/uQte1oUS+vZfGTSd98CqzUWEpPtZ2zW3jQdVA+MJb2Q3FCmEDLhzteuhITXoGfZUnzNAR0D2UewUlc9ETzSlwE4fGM0CM7qZCO+dcZJ+Pk9mqVcAqi/ZQv/Mkf4ypFTJ7zfGiLVQND2kRN3ySild3SM6wZId5kA71d3bCGGzSkFsbVNc1SJOnUfzr7a1PX8XRldcI/xJqugHbgLIXwl7MfqQSNNhELItzCnSz6+WlzVhS7OhviIv2m86Xefi/+r60Qf4D83Osh7OGCRiK8mNod5cpeo2JY8HN0XA+BMvVZwuikite61k+OT1IUPiPu+mbskhVYBBmW8o6kUkwPZp3qtrVTbw8f196jGdHc7g1eiXFBz9Ansn522czLagUKHDNU5RRBrzBQmrPNsiqs/9mkxqhbPGVzuU2ElnDDv1KDrWsc5uu7GCzFO3utXjn3utYnNtdfpUN/JkkmgTqxUso5UdvgAIMwwdQL6uUhAd4jhHYdVgq7Qo6/4E6T28L8ocrwPQvpsgdVSBfTos3/3TL8RGNY+kWsDU4apew5xZKWWXk08hYYVqLSyp3sMNzavxeOIuLLIJH4KGo6mGVumsUthGeqMFgpWVSXT0P1mEhbXCfbimPo9RZCEljf+2Es7IHfoWXqNMSvzxK1xckTXSpTlMxh3w9DqM6JVBdGPmHEPvtxnDusUNPlGdp2g6An/tupbz76sdnj997B0xrRshRbJa8o7xFXsikcex2N8kxQkTWp9/g5x7mC/y1rrGZxpFApu6mFkYQoehR1WbX0vcwAlPPx+ZPPxsTRWESrc6gw2LFJ5yTerE7hXLl56BKDIdVL2geXRhjIQ0JcWPHv3jCipHBW6fRKnVzAjP98SYe0XrEqxMc/f+Y6/r8titpcVrlQKE20kJaE7hKr24gxTCGJRfsjlKweoUdgsG4y8N5xo2+g+XOYXKP+Gp/RD1eYYTQ9gBgwJxmmg10ufPBA2pTwjBWFpv11OUFZIB+ttV1Gnz50X6AMiwwAmBrZlpl+POsNpnIZzV/xVfXpgen1TYLvVzp49fDefmYf0RnG2O4WjHRriq6NoJfL2zBo5tgYbrdPMVXuEL8NBvWsspgmkhLV56M31NTGDS2SwftukSiDTt+l9ooljgoc0xJ9erAtFCBYxxeCM2YytfOohsDpyoavTnqvcFEMePAnwcFM4m4rus+rSEHCO+sVWiWwTfij69TO1y+EK5X7HreEmjEnGg9FUX9Lpxdxeh3X+PLyG4eCNvkjozqi2EH06j1oWPV1z34fFCs2YagGrtVHyLziMAYsmHABeJXntCBMzUWQR2eEv8QT8hNGnvR2JtX97V+40aBpA565QhHqHAAY0un+tmYBBl4D3I4NUm7YBiTfERAao3HIRfQO1f1OPYoVKroCAKJwEDUWADn9cgPThaE+58Rv9m261iEPqDFDcLpz2j4zF5k075hucKMRT81s291WCDE1DZqPmKTNEqjHt8YSnEU52NQlea0OM1qQT+cNjRALGYW2Wl1E7+t37WS1zq61pVsynSP+KqMONMQCe/+1qcaw7BsHYmNrFgwyRp4pTyVeb1+Zg4ufnZwcGgpK6GSaPY0FcR6V8xTmSQkk2JYBwo/f9imFq1hQ9B7HpVEFwkoSlMozyKKCiCiQinZ/Qp7LfDUQjRhAQUIACiY/MSPeO3mJ9sSHbp+HfyCBRk94G5Fp8mfofyts0qmNTzljzpnFiSt09GPskjLmPRLojT3pubh/75fVNLWHFICC/CtW/jS/9jrSiXbfiCKKrBWdWNUtUmYziyjjQ4KJCeVJE3Amzr7RHPQNyqXYhnfsL5mdqJb0JLYacAkVl8KkVxqQT3ONVAEwDqrRj6gyg2USxE4Q39T5820D51SX6iult8GfrrRrDbiVdJTcJLhFuDnEYLEs+SM+Yqcp3pQage/KueWvRzPFeevQ3uMwfkEvGrDskiRQ8od8wGBiMRlQ/YFZsVt4n9JnwXCOkheQqFa/ymsgxJmxkwLLD4ANKigElrwo3njOSJIOAgldGD/2Xg9RyztcZOUTdMS91Huu2Ngp0YlrYKggwHMVUowIdgOwrelVnFqYzCfesB+0RFAFWCC8XCSyZ6OnxKU9NLvnhjJ4rfcH/T+ed3WGRMl119wlkiRssUJQ/aCqCVW1V2kisbfNVqOlzRPXCCfmsrlbZHgvpM+RlbeIkrkwas8og6RzWEJlboD4YStHIZLHuKyvoqRRsSWEqKC5TX0zFmHdOSarHrT9IDLKYgiFBiYbbnzGDQhYjozBzKcKsSWnXXygB57aOXULEwJSaDKs+73Z4ctaghzeZ8SVz6XRVaPUQXsHyvGTHQugP9AS2QCJ6cWbrItLRie3WSkR9V6qSHUjwn5IxyPryd2g44jnl2h8ivVio8FQN4Ry0Clqxu2fgLSQ8btfDeiXbCRIjLZCeJY1Ij0Q6vfr9TeR3Sduf8xtplMT3TPzIT+PfPXZyVGCt98bIUK+hhHqrE1cr7cWz7Ie0S5qZ2vGEqRQlsoNs31AZ5kiPOppFt1VXUv1r1u+el2Oed/aa8gd05Ib40NfWkCsC8l+dDgkg+FuP5MJhlZ4i/oSrRm1UN2K+ut7vR5tmbYNStKpYJQv43JlE3mdmrcqhckeXWPaJRlSJjnxCfdfI5XbEAekyQCOVKs5zFZD/jSe8Zb/GvoAl2c0v+0gWIvJBxSOi5IPgF1bd3kESm7nSKMcO7eRi/+DeTi7ocE/1jzI9CnZHD/8UKPFQRZrgC1frkM1l0NrwuX9GgNnpDIY4mFtt6u3P185qzmpKK/mzzgocQ1c9ZKmP6zBCIYcSN9kU8Qa1whX07DY5amUHBqGBPOL16/qbKj29wbDKORurA95IAIpYm5s7i+eWF0iy+y5fJaGveK6qScu95BuYS6uveoqnUJY6ilNUw4LUBk6+dIglcwNJwMphoaW87c6qHGK64lZNOKOJ9Tvf7n0WBl3pKJ8Y8lq0eb74xTcKNb/cbgKAfaOnc83mJXmsEri9cnHeSzMSrUibJLE/4c3rWPYQMzNJAxZTZYZYH5UuOPxrtBgGyJdSdSy7JL0sPx8npe+8F42sXbfGoZ3ikrKHYN75Ms/TaAHHtVIgeMmlF6/iuvA17cn9+uPuhyyTGhGr5KEWgjU9k9M96f9BgN8N0Bo3/y0Qf6mcQBu2WwWGl1RDHIobSsYqzXE7CakevObDUuyMM/5+8EOwjqa1HcN6QBc4mulCMGtlN2ZDoINcz770biKOvAt13itp0VbYZKHckqGrgJBzroVMYAMnpraUcvtO34Ep6wooexDc0EeqW6x3zsD11jM6voddkWLzjADQaKlcwqJhXxpd51bd9AC5QuFbkrKM6m9waEwsVVR47cz8PNTuSlT1P2ph8DxSauSwGDtCImXpptyGm4O1wQFyYtVbEc7KyZvILPDifVaT9BNfZ2KJoibiS6G53+djhni7jZcTlG29lYC1c7tIL+E24bMlnCzS7BZA6HKqoyQDMq4lYTyyYs7LNppPPKtwnskatjxHQOEqp/UZO5pst+y2rnTCzRS9cDzBU69ohNyg5pdBU0PoAE/3bqvlTY1u5AMxTZr9SUYAsbI/ZjBCW+7U9gwgY8hHBRRjb3A7Kl3VhcxV33L4ZezADQBUVMDHqH5hBaNpOUeq6LiFaVIw87NRF4FkqRoQ89Y5Elg6OYrZ/QaMhMBeFvp8yyVvnjGA7R0w5W/HryHOxrEaQUvzZZKFRlpPg162+LTUgc/FrvXYe9wZFRpAMcO+ofSHI5XXRSKeDHcLa8E88EFK7AtTO0McfFwLBOdMOPEJ/12MNUyRyPpTieTZFcm9rOgT3/Nw6XXxoesuHbllmj31ZIQqgMtx4+hAKbcDyPRrsJGbPwoVa46MlmI9dzMOKjz1rVBq/O0/aKkMtlU7gJGMr0bTzusQA9jGeYLq/wAVXgeOvdlNTdJSYAJMmYPnj0IGQT2yD6CkK0L4oD84Px1xEmYn9Pm62rN0LYdA7BildzSJZodwv/K54zY+a4xnxVmeru9g9g4RrM6wVlgQM+FC85zfubwlhb+OiktMuXp5u7DjzpT7DkmCd9NQJVP2kdd3yXpfjiTf7MP63oDyyfGvjxEklZLC8GdqtwAFIJsZ5F4gN9Kp4SK+n4sxaYYd7VUUd5NDgHdp4Hr8vI0c3aEEcE5xhD03RM/NnQ6r4vJ0GjQsF1Q91hQj2K4uAYDLKC6cYJOltlDnxq2RHbtQjeHm9ZcypCqNXXIoqNosPcgT+VM5ojwX5Qats5CNT8bH+crmQdJcBYJgod9phNUAQc02Ol+3Mb3CqcbVATzqch4vD7zx7Rxojpdsr8NFldQAIR9qwtnA/evoMkHw5rlHjw1Mx3J5VDnFrohlPnVnXky7ePLTvnEwS+SAJUA4u3GxPBGeC6Dp+nvirCoeC/Ve76YWhgDPjBUF3o3iuOKgE0iD0s1aMx/mHg6FC5DPIUMxIUSwFljwHIT9WW9w6zdNOTMH8RpPIyuzVrAT9jSJm71c4fGgtRTwvaU8AfExMYW1mfVraCQ9QISRcSZWapAjnjhBSoSTpcWmmAG93pSZQ9VATID8HnU93OnI2HJMDecsjq5jm90HcDydFFhrVJFFAwfZrubx83djAAspcPC8iC+iX5X73crxUg5kSsHDKFcjiIzHg/nG3ZiY/4AHqI1+8voHMmKXK7sqwRxu4RWEpHEOCuy0IEOuqPDkfWT5OyL15/a6rWR9atGhUIUiFUoUUMomxeKxDZm0FJC6jnX6yiWDyqUn7i4CvaL/leO0U9ZbTeFMWtt9G93CenfmHwGRjROeDPY7LZag2yU5I3ddU6q94dOs/wgybcEhd9TOzCzm7NnEpbob3YEhsbkbrtlCjmcPVqzy0ECCuqZ0FcTezoIi1Yyq72kuMfyGoq1BLubyz7cFS0p4v042ckgVyGy2wxGKjGoYYJYxxEHgMmjMXa2VidNXQeGsK7gAMzFJVom4y5aV1QE2l9mxNqg47jJj7YmhRHT6z4oseY1wf9o2lHQcoFPck9IajHbFUcgRSVcd1HkZ8PArNBwihcfQCeufhNR3Xg0A484V4rc/oRalW2qm5PJjl5UMJueqrC36PRYDNH+lmF5zXLTB+aWZQDFB/soHjDPsztwhASriObxv+3GzW9O9Jb8EVnKSH3uU9u0L/OjRkUtrGLJL8Tz8rrUPGQriO/aQn4XgCPXvjR+5h7xfOToPG1RTY7fEMb1aVwr17woEHnnGgcamsp0XnihYNsV2NCUogXIz2GVtKAwwwZ1TgSYt3o/KKauwrrTTYxr+bp9YTrxxgWTLI9tu6eS0sYKCec2Gz5nSmkMUqNzIZ3wp8+2hHfBkH0LC5RDP+JctzJjX+i3kViNEPzz4WpukrHaYeuoyFEvFT8pQXrK2ESKVjfBb9fXVJJEBdZoNPp+sePt9M76rnjJWKMlRKXF3DNS+SM4kJMyUMReNtCKTcNPCCVx8MZK9p1FXiph0DymPk5l1P7yDwqQdERg7NXXZ+0NbCxnDx4vkNvs1VILF0ZkDYdqdz1WdY3nPBRiyuvOGYjifCPLcJ39Z7BnqGTvhbMqZOJ3VxHKrDWP2eEpXTWVq/VdBExa2NXLJMIxQja4LKAcGViIpb+lt7/XDRb0YPuO+3umDTVDCsWRSlQuLDaBTNd0XZ39KY1nH4AQDxf4GfeByLiPTejB+R9RDuo+4hjU3fKtDoYEXz/2lSk5t/tMBcJAvvVSMjy7XaiOEJ9vAVqPbS/a2+kza4BB6PpePSO4WthvkofVWA5AKO2qF6jedkaq52O31p5G34XCEMdkvHGGYk7X6VnifP7cC6feyb2bwrG//VHvNnf8CZgM0jtGg30WtTqaLPrG/p+LWZKoNCTP2NiLdqDpW5hNev8V5S8vi/ghcwvgEINj0je7fcGQjPrLku+8xGSMJrZVX/QormcWHK9vvZmvgy++BM/+JAN6ntULtPMZG+7a92bxqjr3oKfqq1ARq0Yh/WFUGiS8EibBvB2LAxduOX04lhggDmU20kzmAFsIOgtUNDdgL6jpMbfjlhdBxVHNJc6kMUL7xGKbHEOvoPmi8ExrydXNSMO582eu1wBHrHAPwvHQgnNP6dv/5e5VXUuBGcm1jo+jM5GJqP9ryV70JqTstvYQ4LjeGmCJnbHcqEVuHs3ODMNGfQoEtpSUqYYYDxR2WQCdeYX7MCsbPuPSQ3xmoGugartCe4wNCu0urljRsUGrY/p4QKkhyV+XQB3wX0=
        - #2:
          - type: tool-call
          - toolCallId: aFDtTEV0kFpme1bA
          - toolName: set-relationship
          - input:
            - Rationale: Setting maximum friendliness with Indonesia (Player 5), who is The Inca's vassal, to facilitate immediate peace negotiations and end the two-front war, allowing them to focus entirely on Austria and its vassal The Huns.
            - TargetID: 5
            - Private: 100
            - Public: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: ul2cm6ZP3cbHLGzV
          - toolName: set-flavors
          - input:
            - Flavors:
              - NavalGrowth: 40
              - TileImprovement: 20
              - Ranged: 95
              - Nuke: 100
              - WaterConnection: 30
              - NavalTileImprovement: 35
              - Religion: 0
              - Expansion: 0
              - Espionage: 80
              - CityDefense: 30
              - Air: 100
              - Antiair: 60
              - Diplomacy: 0
              - Naval: 90
              - Gold: 30
              - Culture: 0
              - Spaceship: 0
              - Happiness: 30
              - Recon: 10
              - AirCarrier: 80
              - Wonder: 0
              - Production: 100
              - Mobile: 80
              - MilitaryTraining: 90
              - NavalRecon: 70
              - Offense: 90
              - Infrastructure: 30
              - Growth: 40
              - Science: 50
              - Mobilization: 100
              - Airlift: 100
              - Defense: 30
              - GreatPeople: 50
              - UseNuke: 95
            - GrandStrategy: Conquest
            - Rationale: Prioritize high offensive capability (Offense 90, Mobile 80) to rapidly capture the Austrian ally Okilis (74,33) using our XCOM Squads and bombers, and to push into Austrian territory. Since we are securing peace with the Inca, our offensive forces will be fully concentrated on Austria, removing their city-state alliances and stopping their imminent diplomatic victory in 3 turns.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: nSqeaAO8QwvEzvVv
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
          - toolCallId: aFDtTEV0kFpme1bA
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: ul2cm6ZP3cbHLGzV
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.