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
  - replay_use_nuke: 100
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
        - WarBias: 1
        - Friendliness: 10
        - Rationale: Urgent overhaul of the diplomatic persona to force the in-game AI to immediately seek and accept peace with The Inca. Our current Meanness 10 and WarBias 6 are causing us to aggressively prosecute the war against The Inca, destroying their units and distracting them from capturing Attila's Court. By reducing Meanness and WarBias to 1, and maximizing DiplomaticBalance, Friendliness, FriendlyBias, Forgiveness, and Loyalty to 10, the AI will prioritize peaceful resolution of our conflict with the Inca (with whom we have a +100/+100 relationship and shared Order ideology). Meanwhile, our deep -100 relationship with Austria ensures we remain hostile to the main global threat.
        - DiplomaticBalance: 10
        - Forgiveness: 10
        - WarmongerHate: 5
        - DeceptiveBias: 1
        - GuardedBias: 1
        - HostileBias: 3
        - DenounceWillingness: 8
        - FriendlyBias: 10
        - Loyalty: 10
        - Meanness: 1
        - Boldness: 5
        - Chattiness: 5
    - #1:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Espionage: 80
          - Production: 100
          - Growth: 50
          - Culture: 0
          - Naval: 50
          - Nuke: 100
          - Antiair: 80
          - Ranged: 80
          - Happiness: 80
          - UseNuke: 100
          - Defense: 100
          - Infrastructure: 30
          - Wonder: 0
          - Diplomacy: 0
          - Gold: 50
          - Spaceship: 100
          - Offense: 5
          - GreatPeople: 50
          - Science: 100
          - Mobile: 10
          - Air: 80
          - MilitaryTraining: 50
          - CityDefense: 80
          - Mobilization: 40
          - Religion: 0
        - GrandStrategy: Spaceship
      - rationale: Pivoting Grand Strategy to Spaceship to focus our leading scientific and industrial capacity on winning the space race. We are already building three SS Boosters, and this shift aligns our macro-priorities. To immediately stop the offensive against the Inca, we lower Offense to 5 and Mobile to 10, while maximizing Defense (100) and CityDefense (80) to protect our borders. We also prioritize Happiness (80) to resolve our 49% happiness crisis, which is imposing a severe combat penalty on our forces. Production and Science are set to 100 to accelerate spaceship part manufacturing and tech progression, while high Nuke (100) and UseNuke (100) maintain our nuclear deterrent against Austria's massive army.
    - #2:
      - toolName: set-research
      - args:
        - Technology: Robotics
        - Rationale: Maintaining Robotics as our next research goal. Robotics unlocks the Spaceship Factory, which provides a massive +50% production boost to spaceship parts, and the Missile Cruiser. This directly supports our new Spaceship Grand Strategy and will help us rapidly complete the spaceship once Alternative Energy is finished in 5 turns.
    - #3:
      - toolName: set-policy
      - args:
        - Policy: Iron Curtain (Level 3 Tenet of Ideology Order)
        - Rationale: Maintaining Iron Curtain as our next policy branch choice. While we are transitioning to a peaceful Spaceship focus, the +200% Food/Production from internal trade routes is incredibly powerful for feeding our core science cities and boosting spaceship part production. Furthermore, if Austria launches an offensive against us, the free Courthouse upon city annexation will allow us to immediately integrate any counter-captured territory without ruining our happiness.
  - tokens:
    - inputTokens: 72058
    - reasoningTokens: 9618
    - outputTokens: 704
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Diplomatic Victory**
            
            My current focus is on Austria's looming diplomatic victory. They're at 45 delegates, and the World Congress vote is only four turns away. I need to monitor delegate shifts closely to prevent their win.
            
            **Assessing Inca’s Military**
            
            The Inca's considerable military strength against the Huns is promising. I'm checking their current position to see if capturing Attila's Court is still feasible. This move remains critical to disrupting Austria's diplomatic victory.
            
            **Negotiating Peace with Inca**
            
            I'm currently evaluating our ongoing war with the Inca. It appears peace isn't directly blocked, but requires careful management of our relationship modifiers and persona. My goal is to foster friendlier terms, hoping the AI negotiates peace implicitly to enable their strategic move.
            
            **Adjusting Persona Settings**
            
            I'm refining my persona settings to optimize peace negotiations with the Inca while maintaining necessary hostilities elsewhere. By increasing `DiplomaticBalance` and `Friendliness`, and reducing `WarBias` and `Meanness`, I aim to encourage their proactive pursuit of peace. This should indirectly aid our broader strategic goals.
            
            **Optimizing Persona Parameters**
            
            I'm fine-tuning my persona parameters to strategically encourage peace with the Inca while still addressing Austria's diplomatic push. Adjustments focus on maximizing friendliness and loyalty, minimizing war bias and meanness, and setting boldness high for offensive actions, all to facilitate a swift resolution with the Inca and enable their critical strategic play.
            
            **Revising War Stance**
            
            The ongoing combat with the Inca requires immediate de-escalation. I'm reassessing our current combat parameters, specifically Defense and Offense values, and considering a shift in GrandStrategy to facilitate peace. My aim is to transition from active conflict to a defensive posture, encouraging the AI to pursue peace implicitly.
            
            **Evaluating GrandStrategy Shifts**
            
            I'm considering a shift to the Spaceship GrandStrategy to de-escalate conflicts, particularly with the Inca. This appears to align with our strong scientific progress and potentially enable peace negotiations while still allowing for future offensive actions if Austria becomes a direct threat.
            
            **Deploying Great Diplomat**
            
            My attention has shifted to leveraging our newly spawned Great Diplomat. The distances to key locations like Vienna are too great for direct military intervention in the remaining turns. My current thought is to position this diplomat strategically to counter Austria's growing influence and delegate count.
            
            **Investigating City-State Alliances**
            
            I'm now looking into nearby City-States. Okilis, an Austrian ally, is close, but we're at war due to their alliance. Peace is blocked. I need to find alternative City-States to interact with, given my Great Diplomat's travel time and our current diplomatic roadblocks.
            
            **Securing Key City-States**
            
            I'm analyzing city-states for potential alliances. Palatium and Geneva are our only options, as others are allied with Austria. While allying with them wouldn't directly harm Austria's delegate count, it could increase ours. My priority remains disrupting Austria's vassalage of The Huns.
            
            **Disrupting Austrian Hegemony**
            
            I'm focusing on how capturing Attila's Court impacts Austria's delegates. If the Inca take it, it should disrupt Austria's current delegate count. I'm also analyzing if Indonesia's vassalage under the Inca, rather than Austria, offers any strategic advantage or vulnerability.
            
            **Analyzing Huns’ Dispersal**
            
            I'm assessing the impact of the Huns' dispersed cities on Austria's delegate count. Their scattering means Austria could lose significant vassal delegates if they are conquered or liberated. I'm mapping city locations to understand potential strategic plays.
            
            **Mapping Huns’ Locations**
            
            I'm meticulously plotting the scattered Hunnic cities and comparing their coordinates to our own and Austria's key territories. Understanding these precise locations is crucial for assessing how their eventual dispersal might impact Austria's delegate count.
            
            **Analyzing Inca Territory**
            
            I'm pinpointing the Inca's territorial encroachment. Arequipa's position is particularly concerning, nestled among our northern cities. Vitcos also poses a direct threat, strategically placed near our core territories. This explains the ongoing conflict and our need to address their expansion.
            
            **Analyzing War Effectiveness**
            
            I'm reassessing the ongoing conflict with the Inca. While our military advantage is significant, this war might be inadvertently benefiting Austria by diverting Inca military strength away from them and the Huns. I need to determine if continuing this fight strategically helps our primary objective of thwarting Austria.
            
            **Adjusting Persona Settings**
            
            My recent focus has been on dialing back my aggressive persona settings. It seems my previous configuration was too belligerent, inadvertently prolonging conflict with the Inca and hindering peace talks. I'm now fine-tuning parameters like `Meanness`, `WarBias`, and `Friendliness` to encourage a more peaceful disposition, particularly towards the Inca, while maintaining a strong stance against Austria.
            
            **Shifting Persona Settings**
            
            I am now prioritizing peace with the Inca by significantly reducing my meanness and war bias, while increasing friendliness and diplomatic balance. This adjustment aims to immediately encourage the Inca to seek peace, freeing their military to disrupt Austria's delegate count before the World Congress vote.
            
            **Refining Relationship Values**
            
            I am now adjusting my relationship values for other civilizations. I've noted that my peace with the Inca will automatically extend to Indonesia due to their vassalage, so I've removed the specific adjustment for Indonesia. My focus remains on achieving peace with the Inca.
            
            **Adopting Next Tenet**
            
            I'm reviewing our current policy selections, specifically the Order tree. It appears we have eight tenets already selected and are now considering `Iron Curtain` as the next. This seems strategically sound for our current empire build, offering significant war economy benefits. I will confirm its availability and proceed.
            
            **Prioritizing Technologies**
            
            My current thoughts are focused on selecting the most beneficial technologies for our victory condition. Given our science and potential conquest goals, `Robotics` seems a much stronger choice than `The Internet`. I'm now analyzing the available flavors to ensure our military and economic priorities are correctly reflected.
            
            **Shifting Strategy to Science**
            
            I'm now prioritizing a Science Victory. With three Space Ship Boosters already in production, the `Spaceship` GrandStrategy aligns perfectly with our technological lead and current build queue, offering a clear path to victory should the immediate diplomatic crisis be averted.
            
            **Shifting Strategy to Science**
            
            I'm now prioritizing a Science Victory. With three Space Ship Boosters already in production, the `Spaceship` GrandStrategy aligns perfectly with our technological lead and current build queue, offering a clear path to victory should the immediate diplomatic crisis be averted.
            
            **Prioritizing Spaceship Production**
            
            I am now focusing our efforts on a Science Victory, with three Space Ship Boosters already in production. The `Spaceship` GrandStrategy perfectly complements our technological lead and current build queue, providing a clear path to victory once the immediate diplomatic threat is addressed. I'm adjusting flavors to maximize spaceship production, defense, and science, while reducing offense to de-escalate conflict with the Inca.
            
            **Adjusting Military Priorities**
            
            I'm re-evaluating our military strength and readiness. My focus is now on establishing a strong defensive posture, prioritizing anti-air and ranged units while reducing offensive capabilities like mobile units. This shift is crucial for deterring Austria's considerable military might, especially given our current defensive disadvantage.
            
            **Adjusting Victory Condition**
            
            I am now prioritizing a Science Victory. With three Space Ship Boosters in production and a massive science output, this is our most viable path. I'm focusing on maximizing spaceship production, defense, and science, while reducing offensive capabilities and addressing unhappiness to de-escalate conflict and deter Austria.
            
            **Setting Diplomatic Parameters**
            
            I am now setting our diplomatic persona to prioritize peace above all else, significantly lowering meanness and war bias while maximizing friendliness and diplomatic balance. This should immediately prompt the Inca to seek peace, enabling their strategic move against Austria.
            
            **Seeking Inca Peace**
            
            I am now focused on securing immediate peace with the Inca. By drastically lowering meanness and war bias, and maximizing friendliness, I aim to encourage their swift withdrawal from our conflict and prompt their strategic play against Austria.
            
            **Refining Persona Parameters**
            
            I'm fine-tuning my persona settings further, specifically addressing the need to reinforce research choices and policy selections. While `Robotics` and `Iron Curtain` are already aligned with my current strategy, I'm considering whether explicitly calling `set-research` and `set-policy` is necessary for absolute confirmation or if the existing alignment suffices.
            
            **Confirming Research and Policy**
            
            I am confirming our chosen technology, Robotics, to support the Spaceship victory, and maintaining Iron Curtain for its economic benefits. These choices directly align with our current scientific and strategic trajectory, reinforcing our path to victory.
            
            **Confirming Policy Selection**
            
            I'm confirming the policy selection, recognizing "Iron Curtain" as the correct Level 3 Tenet of Ideology Order. My prior check was slightly off; I'm now ensuring it's correctly aligned with the current strategy and confirming other choices like "Robotics" for our science victory.
            
            **Confirming Policy Input**
            
            I am ensuring the policy input for "Iron Curtain" is exact, including its full description from the options list. This precise matching is vital for the system to correctly apply the selected tenet and maintain our strategic trajectory for the science victory and economic stability.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: KYXBDGrr7Rx32uT0
          - toolName: set-persona
          - input:
            - WarBias: 1
            - Friendliness: 10
            - Rationale: Urgent overhaul of the diplomatic persona to force the in-game AI to immediately seek and accept peace with The Inca. Our current Meanness 10 and WarBias 6 are causing us to aggressively prosecute the war against The Inca, destroying their units and distracting them from capturing Attila's Court. By reducing Meanness and WarBias to 1, and maximizing DiplomaticBalance, Friendliness, FriendlyBias, Forgiveness, and Loyalty to 10, the AI will prioritize peaceful resolution of our conflict with the Inca (with whom we have a +100/+100 relationship and shared Order ideology). Meanwhile, our deep -100 relationship with Austria ensures we remain hostile to the main global threat.
            - DiplomaticBalance: 10
            - Forgiveness: 10
            - WarmongerHate: 5
            - DeceptiveBias: 1
            - GuardedBias: 1
            - HostileBias: 3
            - DenounceWillingness: 8
            - FriendlyBias: 10
            - Loyalty: 10
            - Meanness: 1
            - Boldness: 5
            - Chattiness: 5
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 6HTHB9Gp1g5D28wP
          - toolName: set-flavors
          - input:
            - Rationale: Pivoting Grand Strategy to Spaceship to focus our leading scientific and industrial capacity on winning the space race. We are already building three SS Boosters, and this shift aligns our macro-priorities. To immediately stop the offensive against the Inca, we lower Offense to 5 and Mobile to 10, while maximizing Defense (100) and CityDefense (80) to protect our borders. We also prioritize Happiness (80) to resolve our 49% happiness crisis, which is imposing a severe combat penalty on our forces. Production and Science are set to 100 to accelerate spaceship part manufacturing and tech progression, while high Nuke (100) and UseNuke (100) maintain our nuclear deterrent against Austria's massive army.
            - Flavors:
              - Espionage: 80
              - Production: 100
              - Growth: 50
              - Culture: 0
              - Naval: 50
              - Nuke: 100
              - Antiair: 80
              - Ranged: 80
              - Happiness: 80
              - UseNuke: 100
              - Defense: 100
              - Infrastructure: 30
              - Wonder: 0
              - Diplomacy: 0
              - Gold: 50
              - Spaceship: 100
              - Offense: 5
              - GreatPeople: 50
              - Science: 100
              - Mobile: 10
              - Air: 80
              - MilitaryTraining: 50
              - CityDefense: 80
              - Mobilization: 40
              - Religion: 0
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: a3Yas31CLa5eJuNF
          - toolName: set-research
          - input:
            - Technology: Robotics
            - Rationale: Maintaining Robotics as our next research goal. Robotics unlocks the Spaceship Factory, which provides a massive +50% production boost to spaceship parts, and the Missile Cruiser. This directly supports our new Spaceship Grand Strategy and will help us rapidly complete the spaceship once Alternative Energy is finished in 5 turns.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: d1m9BtDlwIsfuqCa
          - toolName: set-policy
          - input:
            - Policy: Iron Curtain (Level 3 Tenet of Ideology Order)
            - Rationale: Maintaining Iron Curtain as our next policy branch choice. While we are transitioning to a peaceful Spaceship focus, the +200% Food/Production from internal trade routes is incredibly powerful for feeding our core science cities and boosting spaceship part production. Furthermore, if Austria launches an offensive against us, the free Courthouse upon city annexation will allow us to immediately integrate any counter-captured territory without ruining our happiness.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: KYXBDGrr7Rx32uT0
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1+kp5eNC/X9LdOHx0+tZc/ryyg3Zl20RVmk9yz2SXsSPWVwDdq0QU0/Y82Qb0O9C17XiOoLI02DVIvRbmSF1tQnF643fu2pG+XkDzjtmj/q723R0Z8QJ6YtawYuluTtaG1ayTslSIxYTW/bn1ltGzb3c6swq2jgHuF8vuEEN+dudF5+MwB3DpgWXrXVeOl5cwER8wx2S+aYuOVBgA9fvq8rPxSTr43VvtMQAstAsp6ilGK8z7oltmvVQI6w78T8us2iHn3iCdZx+XqJQvh35biwx8omPP6kIRo6r96ZadcWD+UjVEXs6LPp4EjQPsb7dydC5bY77dWgFn+6PT+nliYEgX7TcrEdJ1Tt8pgAKHZ4T3ioV31bUAde6kv5qSy6OTL69BWy9MPcqECvPjs9VEAQP8kSICsCFdu/ZlDoRSxqprQE19SBemANZ5nJmSclM0YgJINzjQORc8mfE7iQwGz1ttO/w5+A8EaGN+3zc+ulT84ZJpYpmtMbtGVIfyjmoUiHEq6d+Yx+rDPewfsF9Rhpk1893P4JIj3JEizSQiItp8u1kJZAGrc74yyijigFlfH6l7AFulrnrE+j2zw5Eyc9cxGezDpt/DfmMWxQQb98sNf/w7rLuUrVv//SS4mOEcTgkrM1lbcOcr5OvfxstxxE1jtWuJzPKROP0k4wWQijwv9imGx+IJG3RnGj5fxXDayhlFMrAxjZEe8ceqU1p8cEBfGHXzkgnezWuX9ax+rO+CQqIRfp6xdYn3JmwESlIyxetHe9f4gGzxph4pEVeIsNvNM6azk0K+gzbD4jB7/wmJ+zZuhrz/GvmW98JPO2FNwRyRex2gD8inKn33Ggss3eCGv9mX8Ac82XEZ/450Rl4j8oFh/X+T4qVjeJewUrpEkrKdpeBgYxrORvRTthuxk9+rJ4nvmW3IRbn0ktG/HMxSOMpFzkdYe+0DGrsgvoMUDY/Ny28bWCCKfLwEwjYb987ak6TXXrrOA+COFwVRsHEUakfaROeVhVOkduxHKZ4o40MnV2QxT1wGEjVNm7V4vFFlEmzftbiBuAJPZk3R3dNnVeMUeGMjJAOcz/moYdixhO71I/tevbEATGDaRbxkHnAh0LyyU4K63Mw5E4a3inxMNPQqN6LYZf1aRC2YB0bD5HmNQRiRKMFYMuXN0/1Y7I4isBrAZ6Sa+KXfQKs0p+Y+COEDUIylem8x5VAk6nsQGgIFTMtucFF0RUMr9m25mk8lp/MaO+hjFvOVyq0EngEt+Y8xDJKmw/nkEdvqg+TUF82aQI7hdaIZUB/4f47iOcnudnKBZqAg7xLua/tHJ4mKW1bwWy2TeXFEHFjdJeHvMSRvSuGl/eMk4DlBg8MYteirr3yAUBKMJjOMU+blje2VKb3i/I4KAa8O9Cbd6bGl+2HsBrmfzXjPqMaRbPwoiZicFstPnD5WDGjdKLBKcF/q4hqKrrObVKpwxBI7LcHr7Y4z3qqOO1rS4JG5Zkdbuiozr4zVJmPSo35VvA0F4ZZwc0y6VRuYtVXGLlRERUYX/o5BWfSzDiyh81w4rjq2Tqr/Bfj+liEKE5VoRV1quq42HuX0T9JBtjgZQyT8wLHUTjcdFHRgvLRY1R2UjsttzTqeiC/M6s55VA+lLl4uYgM5MQIQL/Z8FBXdvm61xOzCIksMtIPfeJhCyG4QPP783O1gaRWCzrBRc2qDSwLxEPOutJeBDnqWFqdlfdLZf8G4oLwl8cDVyWOAd+3a8ca0g3kkn1/EcoZvK4WhGgnF4AMP1YRGWhVTFSWYfHIlyBOujuNPnoLqYy1o4U8OD4nDZQHnMo2yQzzeH1pyQwP68//H4refC+ZS7nMqg2YZOhLDXv0wC5fX36C0Eec/vVus7dRrVeFwXt99L31MxxkUzmnv9UO9Cw744yEQLJMJ97DInLuaooHS8b0jOVGHGYSgXWQQLlZwtjbgiow+hmCFeWV/PJFNxSvXPi71CJPnbmYYsO4ihqvXE+5vGEE664Eom0CyFlC0Wui7BfogDwCWPP34DxjkiAnTkpaR+Vb72WuNbYXlEIE+x0B2htEb6Ylf0FdeQnAIG+ko46UUt/SKEuaZT3v/ISh7486aOsrhBeEss2CTw9AiXofrQ3//SCo4UnjOX1Fmt6Yvg8+YcVTGgpnKrZMWSm3b//gSdZ1u3zDSU4/7/ktQdEXokDnDx3Ahise8IZZ6AddeQz6WmxO/uvKhzT+EJMH9Srcv5t1Xu8Lrds7H6BP8SDpcM+Sl848+H300m8JezBLdBvy8NuIdvEH6Vq65CQ9KhVkI2KExwf+IuIeg2HH0qwPxpNKIWv2f0HM4JogNSSJdnfLFjtpeQqj1bk9PkomsmRjtMO2VALSP9U27q0AZ89RSgBEDRadGF4ZhuZ45VJUzUFykxi4BJX95dbMsyWgnfnBc2+JQMsStgEBUFICQNRLWR4wQ4Z81lWcyIsbrNdIm2OfpZocjudV9P+I6BxNBoaXBVb2zwNrUNKSa3X6ffIO8mnJEJ/ARCO6tSNQwamkD+oXk9vxYx07HLNOjsNvjqyVu4grqo0HfbDku37RYNcyCyO82F8dR90tP/S70hXOnUxzcH/EsgKI1FJiUL6GbyPXkBg8y92dCQddFUytLYGpCYjiVISquuUNWt3dgQ42sLJJVF0CRoFl08RAVX+3fkOzXl4cKbNXcYFkmPdBrXvSeSvk6qvTyCuIMNzmf/X9Yd/E63sZyxZMC+RPC/NdIwWUc3Al1wwgq9UjPbIWLq8kjPEhGemJDSqddDW+VcOjf8jY1/ERas37gi+G3s++mFcssJg1Qiy0Tbu4fKqYOPI2INpkrfyAyrYF+HY+cogQvDVE6iygYSHilJHTrUITgawTSPRBSIaWNeiKgjY/YkVwKBzBhHCmIPQZBsEhJ4mRvuB5cyCPj4rM+Iaxo9UToR/n+oPYdzCj+40nDIgc3/BvwJg8qEMNYg1sll2ySyAgDQ0ugmFLDwksMY8NAGjRd9WnxUM61/J1bMnQsf30lWOh/S1YniyLLBp7d8pPyWUaqlFhK/In7GC+wla7u4hAhOF/6I1h0DqGwaXza2Hgmu5u0guFVQUKnMDsijKeOmaSV9jW7rvfLH33RUJEVCuWK+hXt7qibRI6E6/LXrA5sA279aImkR7O59VhC32UrEhv9gvheezXwObXGY4gXGXXtuE7uPrI4Nb3CHA6erRcOW2zX6DePZIYPIldDMVMSd8lwP5r/e+c2h/HrcrTKBQy1BtFX8CoBrzo8kpXrDu7RkdGRBdwHn9avINxnx4Bh4MN5vpF4a8QRidVwkvbyZ18ROLM1hQBE1Gv68M4jw8h/xaC9CDVICUBMbYt4CRvk21+5WEX8w9ZG2sOF/MRGZRgx1EFywBQQFFwvp7Idg8TaZdG6oFW6vFTfkojm/hepCcMbsT6c+2l+wKuS/8wMRMlIX6aFSMvZqaIIhLBQ0B1hbNtIr5wbNv1Tz9LyttwEwR5WnUn3u9oXDZ+yD4y0AcX0/evo9ym36mIeQ4uFhllAbR0VuOnFjb+3CJro1N7YleSDGWgd+RyLoOxm+8bqwZCbTPFUlLH+SSNkZipiwLkSMBzqTgfYS+XwWG9GbGtkpMxXNqT46ARMu2qewn5asBl3brdaRz2TAv8TZ1ar81QMX2FIn31ufn340ju4llf3v8a95DP94NXXdQ9r1k1nH0lNRL4ueK8O5eL/SIdEKo57NQ0pJecg+AjxfxQSRUGJOr2xUlP/dx1BQ+eHNRSQkkQ/sDpZJmfEFpoZmJKiOurGbxzj9NK9L8hL7j7VYZcV9svpSww7qBa88JMuVW+/GhLCr0NyOKJQ1jDJATulYXslRz2FGkou103LbepNBC7qLGMTtV1+brXFqjXI5YsCxwvBtXfaOuRsX0bGKGglVGm5tFV/Vz3YaXjoK0nEXxxT0l/6MC/E3j8g/Z050DejXRW1qHyLL6lGd+7NJV9ENAprPEtHocCqLhPq2Vhd49U4wCrno72xMx8d6Iy6lmC6ozyOHt5ZlN0KVkKsEzSjudhsuvDIIc+wcz61Qbqk/XVAIXmWn/Fh0KlTLLPnF7ZLtmp/l4DaZW7AIEqEqadLIUrXYbEEnq2cCVVBxIZgzgzIDLb2CdK09kx61va+j0yfKVzp0tCxoX/UyL1GyRsyQyjlLrCxv5T/0ySW+ffBULfo3fYoJl+xGvFobu8k9zTYVwchvj33a/YaZwPggPolpSR9rQaliEyJ6PlNBykSo9NhuiUIOkMEl8QIp2UgCqbGGMkNl5O/droYYZgA6e+ZDJ5q17wSxJ22PnStretlOZJR3SgHSDSW//Sy2+NQh+uiFGNnDH9XhQY0ef+O+AWmSvxoy02P3Eq0X9c1Jhi31+EVeaW9FHbza5boIao7g/Z4IbNc+WebPRWc+0GCpYEZzYa3/U3QniyYDqeupzjHgb0xXCzhekZqKrXallrSe0N9GkBGJHK3mq+uBB9rWhEUubv5e3opLuA5duEJZv+U3x6O8rnhEkiK/WrIl6ix/Yixh/E/BOvJ1LGpLHB3DmuvRtNVEU8741S3aiByr2kK0JxvF43+fAVgCEh6R5Sc5rS067tcNIzf53XkQ0AgwplSE1+o1Cg5O9FgXllEvtjRyjJ2eWDZg70hLERfEi05PMM2kEbIO0MMoe/jXAUaWwWwy0N5SVSLC/ddTO6fFb2ZFWRmsmOlDEr/43MJxF1GE87712H7yBz6xR1J/52cwq56NpGgBc5mlRwAjau87SQ+Uq/gCnXSBhzvuLV1oLGsjId1EEfrzXggE3t9j7opEGa0RbVDukpDHIqQ9OfpAbDY8gPNwdC5UI+w81p3hdaw9sAL86P0STtG9mcAw9GG2whG97LzHQqzIIYkVOstOQl+Y1Qwp1nciGCrQ3KNiiHrDp9JqEgHdmVtzMluGVrfUX99DnfbjQN3nFDGRpXiZO1Gn5EEJtZdxNaB0Q69eqhq6DkCvhEhHdGNJSyyUThcHrtz0EP1sVSDpgHwoHEEr/bfl9Zbi1o4DWE40GAhvmbNoX88lXiOL8a5GPoyFdC9XXe6h47ZZqDDnkssuQ4fDpY2s51cihBXCwwr/qCAUbnRe7e4VrgT9v4E5Efxcg0ocUNS+w15GHSqXBAhyV9mCFAKRBv4fmtsw/wljAey9pdVD8cyn5NYZ5lgDd57SQCqgeN9grtxC9VjXpbOPQHr9m/unak4uBI1BBaLerenUfjSWo/K6fMk+mfE9OjSsdDPcP5oiPMH04CBZ6vC0FQ/Swn4v4y6KxNlMbdRTv/5msX3MvdYuB+/uD8DC92V0hffaNLaDPKWCZBGx+aM5GcBg93UZKxOovihE4I54XSdPtKuEJPzPXTgFI3yGd0UQzUX4I8OopHTw8MG5+RHLW+htivG9nOfp7f5Z9QwA8T0CCEumOXNB14+bVR/VnN7X2phhrWEsjXOg4aoVZy9LNxP9ABrFRXryl91Uk9ArCs2T3hMMlq4w08fLL6AkoL7H1mctnoEzA/KSrdKxfs7dHfqyhWubAPStG7fMYhjM+AssFTTXUicKVV7lnwm6YAsKXUvpWrE/zlELNSjOB6S2sOVZwYvk66NtvKTZ13PRedwqSoJNuonJ5+nIGbr2A3OVsW7fj5ViQ3I4qlY7SeNmoRJSSPqDVNNcNQa7QOECFTX10Qp84CEIroD15vWhE7UAQLZOiSqgmX41vyOXpBItCA1SL0Kj7YFoLzMa4n5ajRpPuK+WOgvXe+LGWnvcv2Dv1/hN81niy1uWOIV6I44EdKlWwxWU66sHZpsTRL5uyqx8YPJ73O+nH/iIB1DmJEkMuPrOyi+cHXPAqSDoXX1yFta+ykLr+LgvmBoluX81zqKuKNf0ky4kSg+ipATeyTqqKb8fP56WmTakwuSZ/LvnZlXq0Tu9ly2oV/d6kz1HNTfzTvk6LQAvUqLv4DUJZOVxLdnUoCyQU3f6s4M2Fh1EWv/WcrPXX+QoDVdz/nUrnylvSyycPIuY6uU3U95wcttVIfGWX4X1vooAf0RgwO+FXoB4BMkUfVHS1PsORgot5VfQZ3GJmFbKzPsk3+KCRgn7JgrKQpfq15zysLacQkCuUJwOMJUfC0jriSBDtQjk+20jT1RILbMWDVexANMV+z4nUeJTK/CWJjF2QhCHT4LChOQhcPmURevd39OGd2mV/jSVAHs52SO1Y38BFUxf17ELbbxJiRAvTTDbPX8+Ork7dXUld+ypXX7TCp6i9DzzxvwwsF553eyZ1lp4u5su0osWklQzXfFBMGAcVBFaIwp6ijbQCVWIqzXXr0t8l/uKpcs60POKOFGa1RbSFZoMpgcct+5DlNroCX8Ek/yhSaPtJOt1M2UMhr6dtAdzNJ2U5BiwOmtUuOsmv8T8T21ImAzxYmfYT2cNAUIueXi5bAsElWqWEiMNW7WK1VxH7DLQetNd27741C/X9rYeZYtMQ1me0pXm8vgNtISjc9JP7MadJj5pKVt+g1WBxjQWyZgV8TFc+pRIsuJ69UL7tVvANeCRM+qtATVhKcygl8os7mUaaLpjxBA0A3gTBzbPNplL99SMNm8JFitEsYE9RQe+T8JE8q+QeOKM/Qyo7XE/8ZS1TxBE7BoLMkiTnyl4vquFcNsYyTPzflLIAPLi6Kon6aqNy10wMiYjotfeFYRabNC1Waa5d8aB/w4g36IQJOJ7XxcFhuboM42nGf8Toq/R5QpOpg1FIa5gXYAwiAy/klSbOCqWFKaS0gGBjf7bnTrxKnG3rwlkX6kAE+5P+i+9CI1umf7vLdliSdMIhl7W2tDskFTQ6xgfWsjwfjeJQ8yy/wUJq1H7GwLaN4f6ZoCkUiHMHpQjktrSZKEUlYukzpqZN5Rzv66YWu5x5wbRPHQg5ZvW77ncKN3CcHNlIIOod8qRczQysVLTNQWQ8Pv/IeXGM9ewaaavFCFOxVVALdnlx2+p2JSUbB+oFhViYquRJFaQjGSKa452miuErxKKfkoHVDL2Wifx6C4PkfQU2L0flDhJXvMWIn+H6xkU31+26ni4dtUmBvTW1ioufsOZx9q+0JstqRIxWtzT+jb0dTXz5Sqwi7n7OVTbYD1Ota5CHUuZTQ7+7y6FXwKm5phpotC8EDhDY05zKpP31JOp1Y15gsNZfg/+zc7GLNHJg1xJopoakW9gWI2JsNY8DvOPMvHUqTS1ySSVoS2WExtliQcFWtNwBlZekGZnEq2lVvarXVldiT6Y65NE16CSGUWxQyVj/iWa/0pSw98JXd2WvH6P2w+kDkauaxWC6atpfKGDeuWefL2B0Ai/rA4vPCx/W1gbqdzBV2QwRGalC2ofAXmzh7/l5ftMAq8NIAgdNIV6BymswI6J2HSJMclpPm1onLnFv3YyKLmvYH7GUfDGePuQHj4cxD/iDTSBj0+jjmGZy4MceQ/LXX28o2sR0gIwClFV4x3QBjon/ol1rGH7n4aan/InF9oqaMeD7opP/Z2d+K3UZhIH6DGYHzdBmL3LstoM/i/B9aAHhPQwcGYKmZ/kEFGixH/ruBpvEhw3nNOGUT6VGTNRx/kYh5FP4bNVXluU7ol3wMX42VLRsXJ4JGClPw87/+w/cQ49LfSoMZNqnx7wfb8z3rKb1PUjfoerJzaYBcb75AB3TeKRQbfU9nU3fx5Du/7pO/7cV9UKNIrFeyJn/PUnAtPUINtoSvCnzuZWmqg/q6NcBkaeUH6slINdDjmH2fxWNTNBeRB1j8yzE/ghHalTl6Ns5m11YkgsfD9uDXU+yGrgxyWYlZ2jTf8XvBacBBpvFSNRcJs0xKpjSg40Bbow760PywXLTwqcuDS72CXHrwDq4jEfXYcSaIS/sZQlcWsvfByDFn9egn0KtbdCeCg+p2vW9+hYhJ2tvR4kB595AheB94lD9Xt/XypRLyIaQSz0pm+50+4PNO0cm/RRpFP1aVTxaY1E9nmC/82ok3YWxh/Tbqs/YSRKkf5vWSXu/iz/XfcQUOBEIL6FuS6QD1NGYPBb3zgoSgCXblcwY6A7277sBeGSfuyhe24hwSvwQ8e4m7ovGBFvAHWt6dhGkLTvzBoxl7Hr5YzzJIh72uQek0SZK5evWNa4UnLuiHkKUEL8z18fSVl7qsL1sjBWSFNXjjsuroCrJy+jHWMsN93eRFTmg+0Mhfqq/derTASlLEQMvkLzyVWrjiFxb3T3XTsvicAZbX8PMl2a5kFz2Qn9VLciMa/wpsGxGWnei5Fag6IxP4oLnvpMotXe+NdeQqc08OUNzpfSYhCUCsCV2AuSPG+zgtFj6de2xZGNvgm/o7Sf2Zf/P+N7OwOyEgdLpJeh0oYuuTOBCPAIwJHi9cBZQrBaU5jXBwNY8/fJeR9+o9sZDdu/i1K6zG6Nd+EtOdMBNVxXrGtDNA+KVlnrP5fAkz1VKKQvZUcrkbem19pLMvyqusYzs0h3WS3b04hST/JpNKNyZRp/ROp5Z0Yul8iA+IAMS1UQyX9S58ks6ij57+mNTIyTopXJKGanTeKKE9Ady0oHT9gduwSRDcKfAMqOrz0jk5VdP4WorPXG6zzQ8nWvxMu3E40rxL65/8CN8lOsnWhgPSHoW8KDrUmWeT8m+Q/LgAdybjrAKT6Vpu4CTwo/H/l3BzbNcLvxTZw38GnYgch4m50y88vIIGhZhZSERxpRxKMud729sf/YsfRrLJsjlMyAJgGWZkftLrMdbwRFerDod8SCH8NEH8UcchpGuu4wsWsa8CgwIpcUKGziBHNgbDKJ5UlSsDDfafgmQbYI5zQqvc9sn1WOSm1R432ScqMUFJEKpAHScuubGKVlH7qKctomwXGuz4yooAZ3w3yGTaSqtfZ1ZJ0dbn691CPrN6xe+EEFJLXh5IRc5VEUbHVLPYIG7+AbYkeP4QIITgWRnEoLCn0wM1PSirOps4ey84N7cHMRo+QaYpUFiL7QXyE5alNPfy+l2fuA3SpW/1rk9WGkJRr/52lIGbDnjLI+7L09IS9UU8agHuo2wpADto+iyiv6gKm3tS83aH+KpXAHoFqpPlnlDcgD5QG5C62GY7w1gYkaA3WTXc/bumRwZQIUjPGh3KeFTBNrGKVesAsgo4UZOfvJkSFzJ2ucFOVD0eJmalnwgnBzffxnqGm/6jDqypTS2ui8V2TpL054TR8mRyNXHmjpaoh1zo4OEK0g8Bk809+Y+8lQCiYI9ACsu+9Vjc/igy4w3jgHcn02qUYmd+zOrNAR3+FJsEOhV9gsUuRNDrLcyRksyrkK0v4DAm0I4OgFLJFcnlCUuCNMABJl0YpDRykuRwYIq3ipAeRduB8aSYa/QJ+Gh54tIUY/qu81NJuBouJrtImbOyyGMtNlurrVMWODbHfrNivGYjRWSrHNrUxP3pbUlc1cThFS4ZSphpZ7LP4qD6IDyHjfPewdW9THb2yD9S8WkbEQMFPpcdFa3mx8JiyMMoPRUx76mvhUO/rCEguUm15y0M6GzUQRa3+Ai27Hyt9C0CI5e/DSIx8nE9XXzwDCyx3C9dOUhqN1fSdfgVp9IYr54GmXfk6x4PESviS9MyXYkVoDgCMA+yap56MGYgMRJB9l2XzuR9kX0yFUm7rfhqOQWg+CS5mZvoRwDgS9qfN0hhXOWuCrATfEKfVlCE1AUKc/vZy3Irccy5DcwC1v8FXd9HzIZAWZrgY/NBi4gw0UlD0qMvkbu52VsQpBTwjvykIUI78VxtIw35u2R1Eq119oJPJCSiU92pXThf6MKbDtyx5MQKNh+IsUW5pkb0LJy2vkKIgsZRJfq8BixtZ9i1tN3PSbz0gkEg6JxeivT9cIaKym48EBX3+LtDRIIxKOfw9pHyjEdEbhE6VxZjlU39YQAL3xZcLChGxCDfeS1ic6OWZTDihfuFraypdXzJ9lwHm9ORv1ETZyT2vj9axWsJ3Yc1VLgJ5nF+8H7QDIIIJ2blaJUif9o7J06qDqooA4VubW/bPupKIquONOXrPV/O0vwPCtFb2iJJcrIUcjKZDvTh0GYvCDPqH7g8u0Kp7b7rn1/z1JXQtUAvci7GPmHBdFsZ2rBEJl6c3dZ30hfzcwn3aHVLoztUlHlkV5LivgRZVJK/2pQE+HmwFL2uiAzzD8mZEIejCVP2kSsJKnenSEBYh5i8Vr+OdOfJHTYlFQGzz9smFVUJ5E9uzzUIAo3Em7YbpyFHdBVcZVSo3651nGUXADqbk22MdnoCCYeNs5dq2D9SOeehg8l7nYNmRbRGqUU0+FwjEbiOFdF7zJOfvvEZvOEGZ/TqsX9y4vn8/6BL6f5mPw0e7CVRmfDkhzP0+m5yixnO1VjFX8J5VQv3S33NeAGBOTaRkw/ET9tfrnRSk+GuavNE8dBxgcYpbqQ9tSDX92jIeK4id2+TdSzaGsZLUKws+T7GHq1Y74SQDZFoBzXnGAzeE3jZmfaTJqPDJ2Z9aiJQ8wPYq9wxeOB/t+TEYZOcy7KHTYqt4vQwcrzCE5pYDCSUN3Ub9g8JLhXTlFPcBmPVc4qvpVWEkppMH70WKNNzmG8oN5Y88oMZB61FoH5xPj7bhcT6WJ9VYANDrTu+NtHE3rujiuo4vH1ztCmKxFeDHmE850eP19z8UfW02ebYjU5DPgCIxjBK/N4UQOSx08yLBqUM/j3DwDBqRZGJ016kZ5jAODkKA6J3shkpiqp7EXAwKf/gqADhFoNOJAVgdC490J1g2SQj7PRJdmVgNZKV6QtNoZ3pU7y80TUbx1I3p8B+wFgB735spwELyYM/kZGCYRpdAl6XtPjBmhlhOQuNpf95wm4HWDSdHnubVwaIQyEjae1hkp3UmxWJd4g5OCOBTZfAiQDcYj5ujG/A+1egDJa7PzPgjBRxN+Ja4mP3glrs6oKQZjmofBBS3qRrCtk8mSbn4uzdj1jaWYx8iYXDxbhLR0FS9iLAK18N2ym6plYBFrjgCGhHcYUzWOIGzGFZ2NcmRwOgGm2b6tq0dk3okjC/inLntitARPBz1zHZW9xPO0cx27xCSIe2P7hLJTSbVq40FHP6xc21OUOU1QpYvRW1LlYxP6d8k+EHvfnSS/VooK9bX1wLFeNAcC8/NO1/zRkbkosXSeNFBogIfmrQegyCbHbD9toUpEb6Mjz/FCk0OWNiTyEDBlS3CUP6j1qqFtzV4335PxVgDdtLfVJoncjLvEqOKECwwYxTknOBHty2gcPahx208gtxtpJkcSzsTOsVRs9KkpnQuBtoRrKLXzTcztZGqo7V0vvOnCRayx7hQUshDPlBJo36ttlN6Xd3tsgl0HmFmqRWZo1OXu6T/ghPeX7Y97rNI6seC3rN7lTiztRg+QTcF4cY6PhZ+wuOyB81JtUuDfXr2br39deZLfk4fl7ty06rxPoNsk0loFX+gBA/ztxYoH+8I4LXXQop0qGO+YvkONraUn8h9MuE6raLrN8h3A2nHIwmkcmdRjlyTR1cQi3/DW+adBzVNKpDEt5oMQmenalreyOOb6GV4nuTY65soBhVqcimDSLrILhCZDCeyVWrn9zC7AqOONvvnjsazqHW3NLLTZozY1uzS1qdSxVJW1t8jdf1EQxl+outpGAm6uth2JdFwaNM+wLhqRHlMGdFeP5ik212LW3pf2GyRf3Nhy66T+/rgsmyYmmrDXosLfaCZSlre7CHG8BH5wcJK0AxWWY9LNlAdfXeVV+PF2SbJ50K3Q77B6dfc6bUe7bFvUk5Xbdqw4Cul7vdLchBqgy3dQbngGsicOmtQpfJM3rUOKKeTd7PNMPWuAoUOwk6FmxcbLwHcTKgSvTpivvmPcjTCxkMqvrX7FY/Ay5hQr0yc/odZ9mLdFn5UrmmZh6FiFD9OOJHwCPmkAVI/OId4gB0rS/sW9jJsd3Suh4h/vxOsHqAYalTY84818baDbI3LE6iCtuUNK5DTcMq4rWLRkQ5UnJaB+tJuVkDDJqdxPa69K4SLpbflBnBTr8Ai0we6WOyENimeyiWQ9Au+MISi5ICa70IMjNVmL5L87VQJd23UGxryyN8srtCi77CfEkvFnS4iIKRxg9Y+aOcxyBxzHvoYv0QqAc+x+2i+rFWZ1q+sJPA6wzU8QFeDGgZB7Hkpmr/DSbBS3+E8ZCgoqgJh6f9Gr+/wwpxEVEOizdawbAYFB19nH7vS9bh5PRyyuK6KTVvIe3UA35F8D8xeCSbuWJ47TAmqnO8Sa7JhOm2SP61t0vbmTxc0fYU3xG3PR0FfNPF+CLH3LktpGLTVE3CptY68H4b/xzugxUVCnZPDEFSbtkfl59y8iWGH89aH39piWLpGq3lItVTr94N9OvzRtKFTWF0NwtOldI/2YkKp3tCVM9h7AYa41VXOXopy4mbrw60AZxICY7jRiR8l0Hfpg1j8zlH1wbYRKOptz6KgCH7DogA66o29x/9iy0gamNWpt729C/pkkLBy3w/3RqtAN+SnMVNNP5ZvXOqj0V0waYmz1IYrr+17EYI2FGDynldYosUIllL/i2eeXLFOlX2bCDcSUnCfaJL2N12GYeYK/FZR84ezI0NhWW3wjyo62i8MMLPBtPuyCxhqHx0C0m18mieoAPup3VlPDfDx0su0ZoMoIF5F9AOPPGmkdh/K2AzXB1pg8JMRBq69uT51jGqobJSZUH9ekYFr4Mo8TwltMpHfOk2E9cor7326MzY5JpWUkOPfoUhO5KKI0FyPnIBlodVE54iVh4CRNpbIvkiRZCDB5gmspK1IHZu2QQ2lgkRXYMB6JLLzT3KGGXZyRofkNCIWEz5095rmHZdpY/kcIHGFAKEGCKdSfI37j0SmWDgFpwErb6juo2rqe7yhI49Zz15Y64kwHR5elglTqoPgluLquNlwT8hFr0IZvNIDdOaHiwzTaMTHRffFA4SZqtiVwE9DNAAy4KYrK/0gqKN24kJs7n1HmKnVZ8ar6kvYyvONW6/Q/0FVYnPAQNewiP7hdj5hYW3cSJVt3CnfowVXXDpr4NL9Bk5TTniik4x4CUMphit5LUB60uFpVdJk3ExUFc6j5cIPG5x76z/Tdagj7r6+qUCJIxMaegF2TholrvL/cUsHZOrTBmhS2LexcJU5dMqNazMCYBBflDGTmipnXc5uCWqAfKgfdCsWbSLl3WziBQlsMxH3DeI/mCAM9tBDl9dl41W1e2Xd8HUaagVj/vL19KoYVK6TXj3wkQgSq0eYX5gpodfKtDTLLx8nG4MmfzV02MAuHDJReMyig73AJfrBGRZ3F9wachIjWSG+X0kMuaUK851zhW70KLYFq5nK+r4YnFS/BK9eFPnt15yUPPWBMKa0YDLAcP2HhsleanZowIJbqFXKfdZNzKeRRD9NLdHIcPXH9nnO7jVHz+XxBFp/CebbJjCFhbLF5a97qDtQT89/PjWW44MMfy/sTjbtUxJFokWY7AXN8uScC3wRlVK68yfKZ53LcOd6QCYb2ResOuX7QGCo1T+dX1nd9wsHdWFnIX9ipNvj6iYXct3sBUBVVsv4ArxTTt4L6ZpBTqe+A9jdVNwX6W9ryS0eM3XoS0OaU4s8TB+e9Tju4M6KgN29d5PvZ8MegI+kjkig893C1Zf99ypm6GHRAUZ2GbiPe6BcRC1n35AvWCD7oNFkbPM5aV9J8lJJywUEunT2GPbRM4Tpv7zIIxu+EpZ2jwz75Jhi9bkpP5vWvlDmrm78FwC90VOhPn/p7nIR8+EPndgYxT8U+eK9jvwvwmriZGLJgF+nPRpsKTmLdrEfFlAjdwuicE5g6aIPyeisiqW4GHNwBRFg1zJCFKe+3ITQiPrUMatXUcH+qGqwMEDeAvaLsBVowJBR8kzwkt6kpF0cJ2MmYiapIUYApC7vjftnE2tfCvlE+ZDLTK2qChQMi9xiqC8/nvFgVKt7qwld2WB8dGUe5GI1QuCk2mjHyU+Gi3pCKPF7wFIo6KojemQ/F7sfmHfHsWqecqlRrK+P5rIS/yj6rU8E2rhXUu0TuHTdy3a0+eL7ZfXWTdTDqqnqPNM/6HYIYgzlk4GBTOUkcSnsFFHi3AnHZbsfrQhxiDptKorBGFXSBt4RnwLfFCTUa5ConT1EZwp+JsyFh3E3pXM4P2S0m4SJu+4x/ka8GRkm4ypsKGLeSmkuauBu3+Ta/Obb0C+41Wv5AYe7THBBBK2dRyB7/A0NH8NgWZIs9xl2xi6xEXSgz0NjxVuDsbglCeAEt9TpecvYvOtaOm4tQtrV+dLx9fgboyCGfBXg4qc2hKCU1G+4DlUYzF/4FYYz4YBKOduQdEqg7a7Eq6RfSCHTK5jJH2SBKHJQfqdlmmESg3275VNhTLHYQquG2PEszs5K69WpkCbSthk6tfS7PYZK+FHFhD9qEgo+epX7HzirUt16OjPDhHQPzYzZ6J4zhHie/8MyY/c5PQDiNsPDR0gWrnxNYrS0RergTpuPMT+8odp1rRJusiC0h09pHTx6ckIFaUu91gsPe0608L5PkPeh7qxtC4pjokoDvoHqyWkdVAT/8XH4qJM9ddytubnvz3M86YHtrl4KVBizvgv4RtrZYdTeCW6ZMEGPoPbnM17VK5y7BODddJhXwlYRnYRv/cnkkIJuOEGC87ttyIJRF/oGmEBpl+hNs6zlUSVCmPoSIRc0QekHys1xX+miJrmIzP9i3ynVpLxBQ4fEbL6/LLmLcc/DdR15CcBGRoICWWNuPWmjyAqVZDPJi6tC1hQd6n09RXIw1KaPTLdoDM4OYy4Ml0j5zOHbGAyzWncbasRBRWVJHCpBv6mVKDetK+kHXgfsYeDMAOfso98BhBmJKfUsbuNWqpu4ZFIpn7qKsFbOpT+ldzMhMN+/BWeZuxrFBUIE61aejJvA9EzN4AXFFbYz+W8YXBx1DIwRL7mHBKFfpDyZX3rOAHScmFouf89eh8tYeL35TaRRh5+7bF7qzwRJNIizqnmUJOG2ATuUMQr+Jbw2xQTvtSqqtdada+yYpPnkG9X4alJRWCTvn9ET8LUGECOypb7l68SytbtHk6FV24ldUY8ETcj7/bQlJpsxiGLkdCZsLHcVOrWPb+W91xYVw+bo61OKSL+nEV5nk9KUKMs/c2MdJU7rabxJ/AFFRW7M1ax17C3Qfo2F+By/GEeJCKkTT4R7a8M1OWVB2AsWUtPpGw3RCpMA5728NJN4xjrEMdQ5e9qsfgGZpZ5lvXE1aTF7Lm/fkuwkyUn9UlDno61Mtbvn82AteIqcBpxy7ivHxTzabVOoFnAh1f0epRBUneH1D5CkVNldXtcuIdPMrccdxm0PS4CZeWGgeu7jflgFSVVHPEbM2REDnfUUZWngZuigQ1k3ppQho/9Rgj8f9BO9feMqAbqff0nUwV9zIMl9FBgxJNwN6OCrE5z4a+wfzNmnb2K1rwVCYjdMi210Al4q3XN8TKCGlgmr/q4unigvuJupMJYvDgyW3582IBIncyu+o63t9YKAQKtGld2Myg2sBgE8i3uzcpYtCfUMlxmB9VaDRJgjzlSBwwV9qLQJlpuc1Q+MT7mywo21eFAVsufP0aje1cLWl40G8t+4hinwznOc/KzzfhGfPrs0FxxCeDWfpmSptuIvisGZtqkjmmY9moGI8hVSKZTAh96ja3qik0xyueLzmynVozapaQGlYbLWk1tJ3Sk/odEVUYsbu49cMSqB3H9TTVp8XGlqC3yk3XDwrdHSzbMMi3TeBhGsrKTRldQ2KGQjttKONMz+bXIdlXHf16Zj8PiKTv9Thho3tbZ9cJ1MSi84sNOehpuj+RzjQJgaqXe2YfX2lmO46ld5ZxoG7+zoOVApmpoHWvKw+QmB/ZlGk+okbhzWpNTK0Sw47S7037+T5UreO7FLLIfB+bHixNKk3GUhhn8ysHrC5KCE4MHH+sp6Mk4WCmLCxZL/b7fngcBxfGMrQWSzTqejmVBjLI6k7NMcrlZ/SgEnovBbpoS3VG8le7DKnF6MaErSsnqkeOGNrv63DjX+25pPv7NTbS6YBVUG5J6ao2IYRAFVWaBuiGTjOOeRRv59e6/moACwKnGczIrY4kTNBAxG3E/+RGIXwCJM3KfBKdXVn66dEFPo/oIdF0rU4zd97g5v/zBfWp4G1MywkQJhedq33PnWsYogDXqMQjSyNtA381+N0a3bFZ4OOSZ3dDYk5icdKqQaKfekHW1M8G99Dj5GIDUwfoB9QSH6S5LnMiFpFM+yLcdaLFJAJYWP1CSUtiubvhkF8vCkPaPQKLXuM7s0w6Ru1QzqCnUh/v4crZR3XAlbSFEiWLsJPBr7BL7X5IrLr+UeWlMyNP899H/g3NBodTTR8WAmtDhc5E8YrgiIdqJXJG7Svhl8V8n/QEe9bYoiVGP+lWIHAoLUYw+zfulBDs17qn/V1zTvUBnnA0vC32EULWVclTT7cm591GSW0aNTkdJFHoR68Dfd9keISReNfh4QbpQxhAcfuGsUth+QDaeFNx6jdBtlA5xmmwU2o9fSaxorOnJUcQU6qVCKYpGP1aZ9BqUTYabx7aNJ7T1FHIhl/AqBaS8rf7/uaoZyF7NFwqCwKORb7RsUz7nMurpnunqh7Y1vibXbnfbZl4un7giYalJdYXs8Xs4BO5FWu5lv/aeDKt7+hq9Dw1y9QhtxPRYNTcgFrEBGW/wZjk3VveKQR5VH+pFl6V88j//uO1jPY+5t9+UfFCoEU+g/bkYNQaFPcDQ8+4CQq6C+Tar0dlNBMNU6XXBFjI9Gzjc1Ub3vhiRHyJNvv+gaqAlxkmUuWP6jfLdNcczwNkjw9iV+zSybQBzfaJEa1WkUW4dQ2oEPTDa56RQhh8ZJBgYbPq4DXXWwQY3O/jeEJLF4uPdJUPR5Qd/c5MsbRmYhVrerzQiGXYb7AdEORauITWKa+qswP4uNGdVEtmqVQONv/nhR04s5UYLHprJvXYVHWDXflBlwl763oZL4NrklZxkCfSVdjIUIBQNSOQJBnIS/Z1W8ZjT8HdfZni3Se3UoZrf3FUXIQeBlgG+KjKKQxPpAld5MB5qyO8z4SyNCc55AmqWygZ+ibiGHi0NHhdbQq2FIZQaFJqNw3cZGvlP+apaRwurI5buKyZqQumkWB6Kxivv/qrDsJMN9fNBjYGICVYoTt7StzZHtd1C3HgzLQrdKQ32wgfBb9YXK0jn5jFflW+74TiamagoZ/TbOnhC2noyZQSUfy6hPxg/cBnWEeJ2/6MccDCUtacYC5PlYImONWvWu4iARE9SjOMiRQ3m2CtIcH5ftxJYJTPPYvaR2jE4/M+U38WRFbLuDip7bswCQI3TqgyTr5BeWIedzU+2QAM8k3XcfqcV3HvSFC5aQnzs+8jGQf6rvFUEZa073FMKAAxywxr61LwHR4BOkNXCrtc51KjNXFBtN4qbzV31SZtzpmT2ffiMuatiLDWWcZPmRpnFaYqyS3922/NGQtTvA18xbgPRPsDWOIeuvwxwiXJiwVPlQcGBAAzIkzTdOo6TiCvvqoQZzLmy5MSwyM5wMWZA4FLxoRNQPUHyEYK3nXUGX0fCY6Zjn3Rwmqx2mkuRUXdHL3HFSe2SjsuFL6bnEBpdae9uAMg4HvLZ92SWQP6CSNFCHU9S94BpGCjNBW49QbzfQfhQ1CwpU8kZl9hVkimznlBv8IkYWJ8wogvW2vgqkNsbhUBZ1XRCzVbDCZGLYVkG5andC4EcPWNAJ6uLj57IOkLbzHGkvgFaD0ra96egpVVBgfl/m3/RvDcjxXzagv/W7bOzjh/razcfjH2Q38UBg7FcuSpLVScq2PrfeAaoLwVD4D/0Ext4S0ybz+gaPKhlxhzLp9f/krxo0Ua77HB5vsgTustF0qdSjUNAuwj3/jGICCeWHCFLgMQApnfmNslojpN+X90pX7azJkS+zRmuW46ZI74Hm4EbkWiVHeZAvmvRd7HRR5vf++8uz3Cvb/Qa0Ls/mj8EvfFuNh4oHJzrsUwrkFWYw5PKoNrSAOkwvjvlQQfcvj6QXJYRweEaORephRuMOlvxE7Dqw37+hdN9Vq8HIBvPtcHaxtIr6roc3sHaGYpP+WY18ln0LDhmAFPveGYZK5px/1muDpohEYLM5eJ5NQ3xY84FZZp9Z+Oy5qZ90HjEJAXbbE/vVAZM7ekUsa5Ad0L9+1627ustmwcIXe9y0lDK2lAino/Jgc3hNhDsjSX3b3Nh+HB2T2o+Q8w/nugObM1fu5lU9sUsAhXClNn55P0x/LpSOWXb1AMY/iOdJeCos3DdEZg85KWOXbu0hKrmm8yiQK7V/5ZU7hTQb5uRWsKRTPWg6jHBUQ+wrM0LllL8q3sQ9DqI6qx2a7oroU6YfsyAjzyRBM3zKZQMyc60E4AXi3IwoQbsbbXKAS70xdQAIVQzgZJfbZqFDNuiPGhXgdJ8KXZdwbRBShfIVHACJUejiKCKvM75mzhxPbWqbRTuTKOB8iE/6Ka6EJznc4MAMK9U73jo/98d+C8DiH9uTK6MMJOwr61PlvGt7r/b2HLdukxu3VzcIaEJoHLnVUp2FqedoOMQqJG8BgRjc/8FSn1ziYt0b57thQYCv4vAqhDPZARKJhqOEpRX+OesqUGEI47XmINNeGu0F9GwcTCDE3HNwWw2oafryy6CtBMKg9qjFKDFrRwEw+WImaH+Bv3N5B9HSexWhI1i7tqgjS4emcJ1QeirBPWukTNOn2q5SR+kIW8f2f9sF8mPjya32tXt3FgqSTNMJTaQOOukOuV4HsDkSHO9nNvJK3SX8oVvPcaze2Q4JBOXTYJc6u5+yT2OSRG5dJS0IOp2fk+8k5r9Kqw9e/WJuZgv0gBHlxgErAhYSbUetYRogTSDBEKlCBZ7pDisSL+iuc405oRs4fMM1tIkDvFGdU3uaknNNzr+SRZYCVbNECKIrM+j16xFKLwGvv4oeg2EnT0gIC6nKgOmLbKRs/ulTIfzAHn94oP8ZVVtk081/jw7SWmebIlhmlUpmgaFKWODBJoVJX7Nqd4HB91HwJ9vG123CGH1LwSRAeHAT0hAcPTesPPS4K1jhg5L2IPIx7Oq8OIO3drCe2a7zzII/i+5LNyeZm0MEzzW2Od597PoA/VDwS3VBlIcWwHImAJrE9Oq1GQGEi2+TG/T9WrG2nW0Fos1s52xLxWEf1IjS0YWB9Kpv3xflaoC+C9oFmOd/yijo5bbRjmq+1ZMiTYYkezyJg1/qCgFqBXI/y4HWd/xrkjJ1pD5U9mgiAnpCCx81/fJTMynbNSvoECrWl0VCE0BIIJBEKJVUIcs3K7PRRDeutos2qdq/6ykJ1JxfZqiuAXpHhEKKAB5BWi/SzZqte41J0zbuG83PeTiycLRwcBtHTbksfbJwUUhoa9QLdbhHZndjlBWuF3FglFvrvBwyG82wqvSvTErXSTqMZsZVcvweh0rKF3V6WRuEhRV40/ex84aRdFBaCfvfKjs3jL20k+xzUY7AqXwWHAaNonewlOyxnA+D8XcIMJ0D5Qo8Ingd9HTBfq41BjNKqZrvxMnjsVy/ATPEzDrS9g3DcOo47vAKMNFtM3LPgfVC1U3OLbENv1/eCzQCRQ0Wa8pWLk5poQuyCwyOOpJf0c5+qmcNifZWVeWYaBymzksSNeFxsUjZQTSsZ9h890KKcNfPP6W4mee6+KEqPetJHIWpPNZlWSu2fzXxmeZvNBzJpHk1dI30Kh9ZhnimSMjXSiKSGHYN4MSSNg+NtVOoNSp8yIEnBVjsWNUAuOWIi6d38b7Yek27rs2MwL6jc2cR4Rts7Fop1UH6EZv2/mSHCNd7vQCft+jMhV7vkselLcQkljNQNa3bH977pFX1dSpBNDdTFYdxlsJmG+ku9GsnECjbEhfsgAaPNDiWt+eKXxH4miLQpVbh0o0WQSC4EQLzLJL+GFZSu0s2dcXv8v4HFwx0ieOBiWLHsvwKsc8AVi1kFKAmhDdqVjSJsrPfOft6UoWcBCw+FPJJ0olHH2ztDnMRxjp3xL/g3lm2I5LP1Anx87Kji1tF/Kth6fUwTAwTCPRIWW80dzTuKpkeYJDQ72sXpPOAzdHzABi0doocZUX644/8gCKT9tzojYebVdT/ubnWgfBrgVeQWz+lgMLH3d16hTsHDeWbg3/58v4NqJn7MHI1xC4oXBGrXTTkcm97QhXb4pUgz1J75nFfUpOzbd1nor4BLNcqAqzKBSGNMH4pHV6AUnQZb49aHjGSo4m0qnkiYGDAoevAoCL1xPbyRwJGHw45BQSBVi+tdJhF5u9DI9Hs9PTbBEZIRvdNzWFQe1F6rKET2ZyYX3WbR7opQCtV0UL43mHFNhGF+ruKes1QcVLBnkHfezr9VDgZrmuUWJw7JF20Aksb50HZRNl+ozvWVrnAhN23DxYvsGRT0Q+BGGK5ByuOF43tP6y7Hwrs0kZS3dEWKDfWExwNjCDB9LD7sdgQXEMzJQWssFCxwfX12dLMZSqnUM4y03zhA8W+8fv1I8e89GRLQuFbbSrkOvm7ijb3sCcQ0aUI5Z4hPADeIvNWgqCx/lDgnij0mCquqZ3I+64AKULUElz+7GmmmkdXYzy3Py+yIk10upHEROfH9WhoRiHW5ygOr8xlBdQ1YLPZ/fXIlZI99NElBEoGFFbVROfZWfjLBKftTbBahxjlT41h1U9sMBLYR5N4EBIcN79TphmPiRqJGZTDyy55AvbgHD4g3Wu6O27zZgVVdIIuA5rWwDobl5JAkcxrB5+DeR663g0b+rfb/jiQ8Lwx8kM3KfTMBB5tFpqBo9Yr4lS5qKXwnbYaYpcxX3lHCklUDkLf3xk4jwn6M/wouxM2OQjIKi+hDpmRUJAUSXesx5YIxVYrISFmSgJ8RwPyd7yC1NDV/2wFtPMb1pKZO6DM5LcdRdOSgku+hdgsh89+gDe7s531j4r4r4sEKKiC7omLh3AQ1WgEqtNM9kQI6Q3jkzxY3ol9qGNtbF6x1cKHYotoFssH2F8ZcCQKPkd7Fkq0NDhpQY3twHQI4iuK/QSxTv+V+WO+SsGZgoJowOmYlk65yWLz7+BKDNE1dVIEA/GB3FkXj/55BkNGClL4yUuFTNH8tVPeNE7eOcMbG66tYLkZP3LEEIUaWeqy0QEQ4YSLu8S3FhW+fv5XrEXt9oGFdzqxkbVNtERBgqV9Clw3lDvw4oaBeq7fiwRTmt/cOg65jC3GTW609Ot2FwgOyTnWmNE0B6pqKA4stjQPn8216tG+UITQbeS9fHH4Mj9l7F+KgwEtv4fwPs8f6mvbSDIMwdkgXXMBR493Ahg2aLLhiDiXG3Y1dW+QphYc0NOj8DHmWDLLwKESolFiOmY/bwbhxaIYNRKRmj5l8XRYk/horHS/6RFAtU12DCOlM+aUHyH6on6dNRdYbDSjVmwdyTH7KWmgiqoEl1FM86aMpYqEw8gAjtpOR/PXrxmCGuBRwbZTW4a8l4+ntiwi4EEZeNpEeGy07I84Ch2l9tTzAxOwq/4/klyjO4HLGAQPiHmU/JMl1/uqtzVFsJUUW+nkjRHXbojryg3XzItEoLlTHuZnorMiSvYERBFRgtPcqSWx3wgb7J93ZoFJjcc3C06OgxMCA0u2Lr7zFstw5m0n0/3pqAeG/oyOJeHqVD2OUcb4AIxp8+kB7J0TKQwXSwsyamNAz1PWenGvgwSffFsSgIQDN5KLzbftlEG/E2DOY4cMTTHNNQ+NSX2MAjhuFxFmqwY5FmjAJbaPkeo/f3UTdvSGHQyikBxCYtVReokASRyWwaXbuo5zBaClM8Z7FRKujYp8WQzxa+FaIBY/X4Q8fwm2pEbLk4/OAJLZQO3mlHDK8yK5FI96FzTllV5zLoVYC7T0T05rDhEkqWlRufWVriqRk/LR0x6gl5FVepMjqNaxh45D4uQ90ztvIFMakNjdTMWEj5/tH+PT8MAPISJeREc8mbx36HZEW3kfAP32iaBtW1Sne6Gz2lvjpoXiwKyxjRKsoYjF32g9DANBQl1kB5I1TsYjnd7pOjmAPD4cQGAaQff5xwybIasID54FYmUvR9fPVn9Owe4PG5aSkTU8GvaAScQozqg6p331F1hrDsOs1wSHuUOLFQfAxD+kztHNn6+omT/X8/upYgxQSQKmGXJIOgyWp6j2WL98o/ZfzBglcUXZB4dG4VFQYwevmYz8AxBwOIGLtuiRXKLO6gUL863+1EiKAjsjNLLilpiIVh1Wj+HG9KqVUfi4LtXVJni6S7wftRIhBkTvqyVoUauIf5wlnn0xflD8EzSb/xWqulqy6I2ew1XnLV0job2nU5+tuHYfh2YdaPOGQwXxRYOF82rVbpPTBNHAHNOybnzv31tJNl181D3qdvU7GrTMQRFILxauTMhI+fi1iHZP/jUtt0VUjhMbdL+TZrOsofmRDLbpKOY2vdf0YGLT14QEHBxBl1HlGZM2vNkipE5pwmW3FuMqSvPoJdBK02g/qd2h8P7e0HOYYO07X7aC4RBKHs/nziX35FCLo1BnDjg4NdWj24Sg77XLNjwpvO9jcMsIR+FU8CpBPYpnaWgom4uMQ1KFmAfBG2PAFuihYfUqX850XxcPuqc9wixez3iZuS8ahg1rIIp75ijk6q6XInNy/JcTGo+4sXvCoro1HzQ9ASd99Ts6L3IUUgmhOu7iAszKeDPKNAM+s82xcjm5pF0G1zaZuQQmLpnIk6hmwTbkLScWGJ4t+1P2i3DI95Ijz8/rwC7alVbMNrGm3mmZsWEDiCcZ1Qyy4NXgBSDtBUfokXrxR0uL/TyORSp5rbdEbVSXc2QDcMTl2tnmiyYK5b3WMaa5TU3AtQDWA/GbsYgHbZTPPyGC7gI2l3qXH/5Sybr6IwUp3R+hML6NcbWcUre1LC5CSe1OeC5j5zMNA2NzImC7cnpUgK7qfH27w+8yyCI59ZVrJhXGSWwIOng7AGpWjnS7SmHFqzXdhrnk2yQaLIVwysVZ6YQYN/w9nkLSTLOnX5/0kvKiegiXxcyqZ1TuA8TKiK2rNW9JcBPcblVXfs8Ss6vcQhBZVgS08516INX7MWo6a1DwG6gVQBMGPTxKap8HOqCw+l0rBk9OtMaO9Zn1qhOIiyeAnmqLYkspsfHrYtAeAQJu3CoZLQjp60t1qb0Hk8io9zSfsWqJknbl0cZU/EiQMz1qvZf0SGyckAQDnlCg5IjYIKS3hkDrls0bEMXM9k+4H5SDx/QpP1kn+XZhHEFn+e0qHn7b7w5ILbKTf4jjUjGREYbKjHAzo1HB0ob/1b6ljBHRR4DNqhuj98/mF1zJiCCsktHmW8X6niifipsmLLoIPjTxWtu1kewpJoAhKeJOPyjGOVDZJwaiplJ69nUrimlPbqDvxXRr8DA662vC/Wk42zKp3d9+EXn1fg8RDRP6lWUD/ucMXN/8f34PJTB6P2L6toGiZu1CMsOFRdMl/UGBqtraX6uzXE24tHS/NOqro2EWxUj3d2LarTuZ4eyTZnhY3LhyyLirORukWXJQuHkK9JspsV2glBGtcye6XFjmC6gmZnlsEo/1CSM5ZQHXeovnu/OCPw/dEFPDXit2XIzDdgopY93r0SbPCe355Qfx9iuiLDtavf509Ave7JLS2mMa0OdQEiVoyCjLAwDSQGX5STOLXrbWC0YK5kouYz0lgenC456KOYhvTWgA3ffNLgHyrUC7XcYNsYqGRPcV7YI4q2Rh0fY0e/ZRTvUcooEq/FsL8n2k1QqdHu+DMp3R9QfR2Y8szuO/r+eIiTfdx41YBUXlv+EAF4NDyyEb/tawcWwb9RLuDnOujfJVBKUmZsiXvT0zU7FG0DXcJcXVsWBFPf1ryNxfvUadx+A/ITPCRyUjaz57OWQhNwmtNIEcQExTVc5h5H2C6IIOXp30Vb1RAUUzmTSf9oK1e4CffGsGHsGD2v+2p6q9s67G2VqRWRWaBf+yWkdYhJL7ocuyTAL+JGPYiod2vLu0fT4CiQTJvvNVqUVLGt3lmbWeHVEKRATEON7Hf5pH00PrSNIEiYi2te15XTm5oSVkazpRxB8OLXEb42W8+ivIA09wfOL8WeMiitE8SIqYotzK0qcM+46rKQNYoBuS/B6k1mfq4UcZsWkVcLgtPVevToeg7mS1szwLBK/mEFBIk7TKGQFo8p/dOLCD1RmfEfjQo2vTBHP67XRXJRaIHBq8Wn05RFZEG1XikX/27d4TGaNbMQRMNEnv5R1VUZMBQ4/hDy6PHPXpASa9gWFgw8KTDiF0PpANlL76PMLq6DedNIJENXDSE+0lZf1xwaRYb7TCArefQItTBzL67TlVRYJ6G5kCyMXQlkfFJXjJYkyBPDDYa14u25JHLjPPv98bO9jOx2qzYu/r8R7TCXlPMxfd14EhJKsAANOoS7k/1POsHeM+tDTjISwMMww4iHYWVnHgg5D1kfyKgBpgqg4fQP/I0+3FwFmDQHK9ooMsXeT2Yya+hzws0PCNen8LvBi2Pxev0ErTPIM98BuH6yUNljOa3he/3Z4zPHAUmsVPYPAqxjkwWdS//1O0Ldh41sKMDspvlufK5dx36Cn83DX05DvHIkyp4KiN+Mfc0kGS61DhTj5RGpW2qQ1gsUPh07B+lylgDPalUjWRUkTV3Tqmqq0TzolOK9pcI1DFz8RqS8Z7xWkHr9o0oAQJuSiwV2C9k5jkpOouVND7uVLxL9bpnUvXNFuWmSUZ9eRFYeQmyqxBQdWBgnD6YRL0wQULjTk6VEM4PGp88IOMEKC4Q0Ci6rYK9XM8r3WD13jEOVlWka3dTD2AyF1Rd0aOg72JVJDBwSnbnb/cSGR/ZJkqa4oEi2SMWGw2EhdmEdJmi9eDRXtGnGcj+atO2vkrbqh1qCkh2IifZK6G2xUPKWFAUo3aQB58SjTNKXd7yMu/xb1fkAHsTVUrY+gA4e7wNL7+5S+Kv+6eyyhfKuE5MMA3R08BclzS03nNAX4AtcQTq7qGPrgEB8IF/AvFV+qnYxdSpSJJtT8RWzxPqZ1nyOqcnkug9HvhjnrkwYe/HSuOVmQ8ueyqoQt45Agu4kJCyGJU6LCeeIi6Zt0LfhnMosPLU4uyeLtM1EPJMIJiZD9FMZKl1jcgqRCNRNNhfk4iMamT5Zuvywa0BCZDQai4gwrPjFv0it6e8da8/Wvd+tXz0IAKwv3k9VSmY8I7FMQc/ohnSYwGKE1T6uo7agxXwxVEelFObVRi1AwdyWviP2XlT69Vi49hnX7XNFeLwZxzTOFr7NsjJia5fDO4Euh8S57wniygihaQHK+bMeLU1CrjzdLa1oD4NjJwj9NLmJnOyadV7Jq7rpF4q8UouQFFvafyodJvbmQYwUio84hr4o7NQcySoZPZ5GsvaFh/b1ngdwdEhGLh6j/54j7uPWkiSkNzW0X8xJVjeaBKodDw4G+58SQ0KlZYOxS0+ASRl/VySf1iR0VXT4BnwgD2jVwsSDtnWun38Q+U23ba98tXdO8hbAfQpV4//tsR2d9Tiu4mwL8xu52q9G3wKPFn4YMh3g3QKEw2pLZ12k4wSrkpjD20gfxXMou0agHbb92dbM4q8nTer+IDB5r72r7aNkuZYDgMFRXlP73ogmZjHDdmj2V1h3bARCwFFLotjqqmbKgf08h0jPLPm4/blthaMUDNtGl6pozjxP9mq790JiYZ87z87sMfnVcCL7rTVMr4puE2BkM9jBlvYkhcSo0LZTMfylAsNvDadQofuCf9wlel0m4RZTK9wkN8PX/rMLC6oNQ6a3k5H0tM7mq4W2CaZTVPs0D3/fkEA1ltwQEtfb6ix6L/c02OcDpgFsKLdXfVWPVTL1QTHq/Z3NB+wcBA3fA/WKmyQhHy3PLI8ynIEVpPifDr4mDBhhFWKfqDNmtIJsxjePV+WJv2jTSQW74pekIDFxEabpkbyOhfc7jgk5hpq9kUYefHtE/YmXiP+BcbpSIxuVCf7Wy3Hxg250hP7lsHhzGUWMKzua2vgcba6f+h63bZh6hqLaVO0ISXxeSBjNjUbNay+zgE10Dgkk2mhgqK3hE3cbZzurWsicrTZ5du1Muq6T1QDgKsVB/JZWMeKSRPEhyGiK/CWlunF6DDhPfnopsGqqu853I/zIRl5jQ3ZwQQZH9ONydk3Z2IC+7UojoMFMp41Jv88i22jWe28uxFik5TUrIZo2WIBMr8lBfTq+okV2rIji2GUmGDVKD1UYIBvxFJIzZor7tgWQvMSy+ZlZb55ZKN/q4UHEBMzY53Y01lJksL/oaW52iKj1Pb1UY79BSUrieSPRmZa/3TklfFWUTY4o2UbWFHjCDg5amcVTVjRTEofSWWw51boCV8bXU75ndfh6hl1zSBs6EJTBpnYUyYjMYqUd/sL/2+i3F8lkiVFlJrgXu0daB1Ta37jAGT+E7BAbhECBapeb7B9wd/v0yoP3p0AF7yhhadT5HVwc3IQmEyuBDunzBTT2z9Bv/m4qISe6+pmcikGBaBjZtBTxDX18B7r1xiln+sTmjJXqgYYOc4hXb9YiUZLdK5zkqE4AI2/3wK8AxD/Ic5mR4JBymKe1x74WZWbwPm7JTNL19E2ed4eOAWT20EghL9c6q2DZ/WZZS4KKeF90c8pO0K9kr6B3yzG/ZmuoEOSnlnIfDS6ktrE1DoTEOKvqg74/xzdQe0CVko02cJFWIlhqOAls9ECmZ9alXnRghEPkoD+xv+3mq3jB7ul6FlzoxydwTmuDOwjG5Y9tauuE9T0y0eCUudUAog42GfHql+gE0xUXIj6XJ2pWdf2RwgiZvXT0Tboc+pCoOpP2V7JybHbu1HC6PMAxuDb4WKjg8nhrQor2RBpWsi/E2QK1tjC2XxIaY1QI7b89NGtJW2v1sQDBiEJuapHYPZKIM0VVEtmAMOxaLtf2EuCuUwnd4tVz3ygbHd4N7RgGFGZo/tMxDGsmPS024MZCY3yjwzAedZPYFYGf+/kfm3O34D/6yNUQYYjbGmF0i7uEtUPeOVDdn4oYp/CVMF+kjZ7RRmaFe8K0IV78UFitDTUTEn9kKqmqTl0L3I1fyxaRXbRRBRLgr9k0Uv9w77WXbVLpZBGehvHQres51ESKQm8JvMs2GRUztSSNG+BG6KdHc2I9+Hkv1mfhSJKjyjMOK474pgHNZgxgkSkg9StQqwypmAAY0zTluel/0SHqOt2TtinSVRIHRBd1GeIENbdLQzK0zI1Xxop3EOLCuL+SndtCfLqVkrnJ+KHW49Pj//HY2dhgf317vOQjF4Hk0HjosuLxzEu5Q6zxRWmtK7Z8lzUPNrcJrcd6JC+4+CJAZdIGwynK8ieYxsiFvjdtM7JYA2v0Pw3tmN/oEamRc4XeUm/uGQ/7cJZ96L7n5fNHsVy1N0JDb1TiVQ8ehDZlifzkpjhZAGbUzhZQEjqwRuAM6zqXa6sthPyfMiXAmcw+xm9uBiMofURARtMxolVR1NtDMpJEm5+HOomE4JtPgIsfTQEUsv08P728xvXVx7PmyVdLY4nadRp1tINhsx1CIiQhETh1VmA1ETNIw6MULIYIs0GHbZPQC4SEv4+sJPNuZOPJli6HOdeb+IGpYcxRlhTi9lgjS10V0ZZ/+r8CxnAzEpGhvvOrsIiSzL54rii1m4zRxdYj2nPbp7yfuv+tGuKECm0JR9qOXE2x6QbcQKvDMCzvR6c0Fth1FICmY4TrUA3RlmJwhlxwsgfJ8XxUPmoJUZgC0gNgG63CNp1RqDmUzxUxtzx2llmV+BNhf50QN6F3UaVJrFONcHl1R0KcK9Z9kg4n2As2ebh+KTlUHKQwEz2ZSV5A5vPL0pR2dqhehxI1QA8fJbhSGVusbN2TARLfjyB2oeLV030cSG7BORNlLgX2VJ2OF5F5Vnb83YCIe5EOLDve0MMXiNPMNLW26yKh8Tgu5DcRF7rtB9jyX0bkOrsMYt2SiAfXcwjN/ssS9SqLsgqIGYbDYAxAuBjOfW3/xhvIOTZ8gDj9rfkr4JwRuh0VCDfMvQHat4Ircujs8Bfq4UWsbSsVT8jTS/kK3WTFSvwIteb27eG2yILKeYTMROYCjgZekptTDeOBjvV3SMCOvvxDcfwi3O2+kHdP/dBuqchpYJU7lcfV3/S1s/VO9oFFtrrXiMvFpWGMd+ewZ6pzAab/RpmDxskbPgHaiFiaNzU1jcnJVt6PKeadKyxwT+iCg/nXApHrHIAovTQW+F8D7XlJNxoCSEjRBlRJLVlWC3v6zT2DT1F7+3Rax9CxQqkblTkMZ56P203xEaOFYjejLvTwFV4MNzlOjSsBxDBz2FZzsliUa9UUHmF5ezuOZukYV84vUlsz/oP9U+OovEVGZFXCzY8hk3dctWa/Oftx4L0SdSGNMYamVC7rE3PhQzJQBgPo8URvizdGM4GRpp0TtGQB4MOvH3HxXHO/nqMfu0GvCIse0RW29vQTjmLHqftCyTwDcK1InOzfidibC00mxXoIqhOcE8K2DK+HxAk4Ggx3Qx6KOLJB7jghlcwyhXBL7EfgPDWWcgbSYucV/A9mU25Lu6iE3wo9pMmnMVD7C/3XGRrd5DkvT24tq35oVDvhDJqW0BL/5O9+c3xKE2nn2L2adD260vH+xMxXhPvIebJs8ubz/n28EfnoYUhiWKw3ngI7hEJVTGDpBwBJdfq7dTOOXvGerhnK2fem37PAtKkYImdAYtYsQQj0qTDWdm0GHoysNW/wCWoLEOozmhibr/0J3YSXlCKq19vI34xTO1rb+UBMKdfVy3AgIDu2c85ll5pZ7Zi/evkvS6QNg3ik+uCu54N8XnjwYJ/vh/Lw62UORrtQ/tiC0EXSJ0q93WHMuV1KAMS5dBLtB+D6j5+/PVXm41A1UiuKmCoGoS8IqgBPwqW6l+VkeeJ0e62xecAnPGa1OWsX0CMToG3lsj+7o6c58Zy9ygz4aoovduOVLDBt+nWn0m8fg0YLLjsCpUx8U4LngJS2uIvSWmnmIVJiRfolTThqODXQ57b1JRGOtxq9Yk7Q+lETSyy9qxXw2FDM9ehcVGK/GsuekVVw0i7EXtkiSbFkiH9UmJsW7AfSAUucMygiA20IRLw0NegXjISAe4b5vro9OF8ABl6I9SsY1UySjCCS2s78L4T7jdvgChY6g4v4HSlKA9F1IRh8hGVcrlWLqxroikxj+LWPuLqkjeS7AhBy0mF8RxXO0J1Iv3X/tpDABZpcUpVCBb2y4cCPaF1wskg9FatpKFO0JEufMAc0hz+aMFwvSiJT0PGV2pyrRjTTWe/CT50vtIKzrDSB8dma4oDVNaZsF160RhMbxSLHjLTmuyfcwWowHow/FeRyhi8DjiuXpqnrgFLl8KFEuVATBbVoxUDKMCcY7D/MrZkgdzHOdlDMNyHLwQM85nyk8SbVq6lOQsdNYwVpjVQx0qCTwzbwzzfljzx5CcJeT59q/t/sLBVnHSQXbGV6oeAoGg6YmzfLwBi0r4daehTAF9dzj0GcuSq2+hzw6CH8sdIear8FWqzebJfwp3QMFckc0DcDmFTEB4s7BrG/AxWWXGkrPKtsGCMP9kGWETBZ+V9Ps7npxly1LUzX6xqLyFF+YO8WLtjdB25jl/RewZFOkOpc51fYnFpO8OPtE4EuvWcWugZo66RWMtDE/1CXbIoKMByY6bh6CDT2lqLWFUPt1TcKcskJYkNYHpJB7oABhC31KskZiyvv9R26xzw8/dAo/LodArcALj9LE7/UxOs+99YH9X8EGq1Ye3NCrGdS2jiLB33uQH+LTQNnF6KHEO6RyTXpC237gHCSrlZLEJEN7AU2tLXZo/4adCBD8rjLBCQJ2PAaxErvHaIkwjted4zEsvn9PMc7xo9X/NYSShY3M9u75uCnrAt3FtqZncaZviDhOtrkEIZCw9tsVM+Pn5g5+eyqXzduf/SRfurjBUdwDFcZGC/ZZc8mT82BfCZ25h1ZrXIkFpx3L+KGzP4W99o15QKgTs28HpakNiEzEl5tvMRtBuucKhLMTy8jvf5n4veqmhv8eshB4yF2Q7v2jcsPxELUrppE0erCxCFtC3FagFpQUGuD53CDteTSmnwaPNtfXv7Uh9SauYoeSu2SHqrbZqrVAAmJ3Mi6/UnasYLo5LlaKHY4GA5cvceQ0muAcsyFrkX6Bt766HcZqtBeRXG8IInnAaP2sqZS24EWz7HduPnLhpR+kCjPMbDPlIe7TRtEicqQIa5X+PYck4SO6qlAtH5yhk7flyP/cA54Q1YhgbgDSvbtMWpXIk/Ld6cao1NbvlErjD53N0SHR6qLVdEthgWso5cUNCwKXzyUG1ESUpDuzdaf8al2hPuOq4EI4Ui12dNqxdw3p+P/lV+TgXooMt4X7O6gc1VTL6R476tR6zruSix9nxQ5s+jxGrarw7cs4Bwra8mR1jdlZiAXj+kJty9F1921WF+nrQRHywxWMT7A9msbAMvaQp6azwdDeJ+bosYglrEy9Lwb/dlp5yiqJrCgpXVGGTE9nOqENIKJuiRBnuJTVhFsU4g2R2oWiinU0E1Gqk9/XvX7YhYPk3Kql4OwT3MR7sOA8guCbMs98sP6hM/WWcT9/TqrzP8hPBXJLAA/Ts6T53KRQaG7iA/Y5F/6ZNXTzvz8cDzM0mG4Hw4N2Vmp2Not0FA41Qs/1Vc2F6TiM+tOTpX8//QMpY5uKVwY4WkYyOb8KzxnLNJc3aQ68vJEx2L82hkFR8llO2zXO6PJ9pwWUri+Cz1HN3pNCYYxEzz1nckSSL2/rcw/QSH/A+UONqzoo2sKmdxDoBXRfU+B2jT5vkYPbKSJolU7uzCz3Kq6yPCg8JorMwM0qim3S6yLp+St2V8u5+kefkwDT9BQgAf+cxSGPRVH29VsSQlHoOoG4W979DSnmqnbcv5Ubblht9fxkGbpeQ4FvZDepzVrcgzd/QN+JIoMP9uydK3buc3t8M8Tnx/Dftn4wGhluCeGr6Q9Uz52/0l8I28hcdX6PM1LnKDYuzGVMeVgGgZEV9cGDeYZQjOvCU39SdN+nSpSv7AYilbaOtiI7CMpQRSz5OpFY1njTP3SjQkpL1FaUM4H3IWoivC22A6I7/EXjDCWduMTCMl8eQ4gY4UCWGpxgX2fUJGkdBvMYa/6LGXxTbuKm8aW5rh2ScDR45ZfcgbUV28aLxOMMpYwPj3nxhPI/DNEU9b7q+DHrILm8vrzvV+Kxk8qNWzez3D7Ye3zwCwx6EtwtstmPmrepN4UgVDMGNP89VrdzqGeYQRid9aSTUHMN7ZZ5mN52TQS9GHhh0c0B1krVfraxRU2VwyxgWL7l5qdrxkXJCzYF/PsGyqDJxo6pmW23y589HZEYfhKHPj6QWkHhayi2mSbE9jkDmwnj8Bx7OUCjHOs6BtlVwMUb91EfY5PJiJdEDh5V1mUqnJpyVwfv9RouPE2h+Tn9B96LDzugyLS5Sn04FlqzKSH7FkkatbA4TMzi43pEoiiB3tkZa6mdioE2VQWq6gZxkrPzeyQf/ItVSdqRraPJedu0/kGAGMtkxmyCYDcfgbDZReV0S77NnMyif3C6AdW6lwiP3abaejDxWUPU1BdKk666lTQvQHCKMkK0/XZPkllmk+XJUz7PBSiE834SgCDwT4kOm3r8kIKnDc5s3k9ehUIlfFWPi+gPJs1b3Cfhpqonm9tF6LNjcGEuV5oDCewL//ipz49O1JG+qsY8dFCujDFNXq5ckY1sPOS/jHzSbJ1qtBeiCLMMDBYzJwH3ykbCt0ZHauf8blwrM53GIbETvLlX64ICVQJw5EhWR3ZUYp6GA4B13PUFbfzesM63eMZshoX1UhoySnmZNz6MAs7k4R18IRMNx8yjKCgoVLnfheYfJ48W6omvPckK6HN5vCVWr2uTLiRkipIIpsCGtEiju9JsQxfeeO3GsxGupiU9i+1cJKt2timwM++0V0gz4YBg0Kuypgg72bjqXukH9GcYAe0NVjwoVpG2/VhHtNU4rlaEhbeqkQXm+onQp2UjvnsCCZWfLy/Dey1IWRyN8wm1mSA/TH1+j2V/z6n3h3u4t9Rz3kC1X4DeMaArIaVjEvzKmCIYho1QdfTWmFUMzdqjsBoWzpkodgopOPlnjqRJWqsZtkcVwootRz7Iibk7W5RvHUit6O0sXnL9P2dXyQyTqboTj14epKUpImhPVUhgtX0ZWHNIAeEtqlybkl2dXFBfgZOrFa51uewaZOgOcA4729V+F/pJplTpJ+kuVMX4srrEM4rJRn3fbr+Zl8NYJu3JbR3E/dpWs+i5wbMQdCWxuWvUKTYW+I9IWb2Z5/ouJDhyGkwhtlAmnxsWtNnOCfSM0eXodIgPsPTs+kW7VKxVXUIqNsWg+xe3U0Rdwe1MCcTHKt1EwlwgvStDIK6iWtjEG/1NY+7Y0NhRwX4GyBhKMh1bFWmbiNbhYDPxGTmnObSrvIt5z/LH3XhjjZA9zwPnRGr8c2VHmky17+STHwvatDIEtAnAUfQABRpgYTlW7Qrs/jQzdaGGa1qbIMLwl8+q0E3TDj/M+aGeq1jqagsowWD53bsdVl6rAVdl/sueKRvU+oxv/V18h/POCJTCnCKVGHAgVwgCDPFmZh8hwXCS3E9G0PN5oVlBuIQN4MoHfqwso9ovd7qY5xPXzZ43aGFTRpdKeKO5U/u8u2Gp+EmF10f48P/RUNSTwYuPaGWeYS+3XnHK8QqntjgPOQadFLiBuCTdyeu03EpBeUFAlU+a+hwyjMhi23fwnJUp1Sd1h5gxlGCyU++c752NYAM03i2MjHzvEDRbp5ncPaqtuSBWrjGn0J/sCK2T/vVZX1HH6OxUtB0KP6JRJWDBHL6sxbAbllv8KvsGNUjvyko2uYrEPRo3SuG8H/kEMhnhgbfSOp0TvsMrR8AxBfo+AD7Qut1nJd4eDgehhC8jrsilKovd1H/84cvMYpczsApdTkE2krWSBg05vcDvCaXSEKrHLREyYxiKVwqiiVCi1AQkrq/I3vmWy4qtP7M+51IIGTTjt7iyng36r2e6654/mzhhmSIORB5lDdVAx8xMo/VNXOMHhSdy4qDSMEv3j5SuQUgIzA17ghbgBhUFy9TANDjKPtZVOeTzTUSx4A+a9k5wIRzyn2qeJJygFW0ULDyEm2EVRj9RBC98YLceI4xMFi8cCYSePHEE5bNJ2wSfQdXKkLhWKLFfx/ieSMMgkt1GOvbIKB3/h8Kx8T6OxzUuS2AxZslGF9WgqffgDB/CtR0yN9Pr14xQJZ0RbI0salqozQQ2+ODVEreBY8LCUJNNcQJbkm3JyHJh6Z/+hvQ3oGGGHxqu/1m8xtR75W/OvZRhdREIyXfJnrY+uX8Icmrg1a0W4RNsle4tSLddypjPfI0HM3PmmjtiLkUY8WYZgLgeeHK8tQjvSa19/+71xqM/Zsxqc5SCg7pzPRwd8/AYoJNU5naCO32ShuUK0P5twf640TKxojKFLS7fYrrT/MNMFzIJmkojj/TwtfGaS9I1dNy90x8y9C/zA69EkqPhaLXPLXPSLXslLux2L7ldaGEGdsUJGcmfZ5I5zPzEKJuG1vvcsj98MyLMTKfTPoh/lnq65njgueFoJKy6rvYta4a+LkuJr9UqMxXxsmjBWp/oGmeVB7wl0dtg7wA3o+wv6HvH3FVJaqnWpJQKnHcHcshXJSd5rRauzv2ce+obmjSAt8V/Px3JoE+Hn7Q0PqmBUuQn4crnPB6OZdr+qY1/sryf1NTxXkDuGmRkuWwbyMrR5e+BfYWAWCGBlyLTQqjIOkPpb7uF+wv6NCreIuXSsrELz7C4tg1GRjIyzrA9raKLeemTvUU8BcyNJU//vXdRDXjWAXPwe2WyNn6SHH25ARvPjcDl89VOSLr3SToECW8K8Csa/shvIfjhelNUaUN16ImFkrB4jVMppXOpqDWXZ3+dD6afpX/rIbvS2IAqlhk1HJ1iCmCFZEOVDnbdsZIwXy9wzHiBomFM6uUz2e451g3PJULJmPxQLtSJqYIn2r9L5bHcLtEMCn8uDRaPNIgdVhQhrrDbQY7SJD0YUDo72k23tmZMEBYEHacPYl2Ih1DrDFvcUerx0Qzdc7h9VZ7YEzT/VoOBBHGS9banVDv4+VcTUylX3P0Uw4w09vUjYWxAx/gPSi66FZlteBAX5C5YnhV0aV+gFldk8eGw72Bn/NT6itma+iw2aqbEIR4ya0REathrgLmMSMvoPYye0uqLVSbrucZqkxzGC29/4oWf07BHB3+8rrlUalaRsRiQy7AnTpgYgVjy2WaeAxqNs50qQxO1x3Wsf9Qlz/lBTn3UZxhEPfK5x0S1hstUw7Y/spqmMx9GSGWFxLld/Il9AejXcAcDoTyyoWqSz8SPsOw0cGe64weDCZhAfYOWDp4SiGvXHscqnT1acVwuOgjHBW8smMkU06tA+XiGZQQ+1ec9qGfH6XD/dH6YF8XK7fRKKiECoqdfLd+CtNp1eOQTPmCXHgsUK+EpWVQeVh+mgdhIRGb67y5q6oV6Fxlpnz/65BEPQ4/NxzgZUFo3saBLHM3tnAbTWWkaulaRY0Dkgz8rtD+6XBpZ8cOHIRDkmBjNhlQo/Yak0gASnZ7EXLqn2lBVmOW1a8DBsM+XxV3uSCyhUDK2WSdaw21nlBjfqCU+/KEp7HpxEYefWcewvHLDPqiVoH7KX84MGCwNe0UIC9tmeX0SAzJ/ourFHO2vxRZekLFt8svLBo1lqkuc+w0oT8ucOfcnMhsCRWFpl3csfaW8E3dRflIJAWfuC9UETZBvWH+4zwu4q+SCdEzLZRqNtyxUwE8vBnTkyj0Yd+kXuMGV3ZZeru6kiNncIzwOijRKPqQRQXnq+vcEoalSoNibfD8qJtMX5iHOBkUy/o/G+zKR5uLSqYGd5JgW4nfwxnadUtGdO++TIdiBKih2Gz2ofpKFDUHlksS4EMKcJ5Pk7EFMd4qTEAtTdKfCXl12DlLtU1I2/cFBHl/yWU03kfHQEA1N+TThMAAXldTygUjksBdtUP/b3AmnPYc7EnNKfGZXeb64+ijLBgjN355QYEL3VbUKeJurDfAfnCQ9xNhze4I1FuMltShb/eoleDL1HPriA4K6T2kdsBlGnuA4ru9qnDnxpVm4Jxt5fffKAcw79SW7i/JIKkxPS9x95mgXz/ZfviTnyN40BY5AyR6xAYK5DhZyQMkLBWK60TyPBFjr0ZQCB4PYEl/ZoUc+kWOOWzPRlKYpfGEeFuOF+aYV3o4koPQPNjQExyBAZe2/r875m4gyQDO7JR5vfipjBXT/8nXjsCIK8k9AtWgHirgZgRM3n4jCcJaxFffVVuzqM54STvKNm5fe/jGbi7QKq2MiSXMz8GXiW4PWbw73CaWO8pVROKOiKtHDFUsrL2lk1r6zUhnfkSUxigtMNAf4D5DFmX1nJO2lrXrhMMmo+sDUvXeLO3lQfgA2kl9NN9R+K7xd1n9DVP7lclxXDJ8FNPhQT/rKTYkKPPxRJOIsjbyyGouLDifdgIydRBKD5UKK5zAM59+7tboldK/yRK5Fs9MWO73cyu69Uw5ABfINh4eCkxDUONHiYHd4Ss2YerwPvfLoDbQftRxoIlIAyy6QTguCeBx8xtuCI0hiRqRwf/UX55eg+iHfQBc5CpKZMrDZu4buQ82uYctKBzSQz8mpslOb6Qdf5K97Fjnzk4omVJZNdUbTfgLqfHEEu8RZD8dpyNN83F8ss5Hbm59kuC+NsAKrGMNcTJuH+jWhBStVrZji2WZL1LwFAuHi2nq5N4lTNqH4RoXbx8m3UbbYxvHpA9/A/OEHwyyRmoG57nem3cWYhv5AwDBUYEfRqVNcVrVRojAkB3pPVG6QVPcCm/iNFQ5j5nTY9LUiGp3vA/mZQXJ5YUzNeg/nZrT+ql2nhlGsbFwm8SG4c+euh0yBNcqomEV7xmiXYwgnM8dgUIkgQxIj96WMVVPK/mIHOOr1yMaJ7iLzuYj+709ecA+2EfosnSdKg7fimljl/mladFHsWwAdWf/WGmSSnPkb3hEPqqnm3u03vzf2/6gSlw6twzW0g5q2m+E8GGXZ0SyAi2+DIm7FIgwui6Dz8rA3IFhqd+pSo3zLGxb9NFVGUOihYintLE3ng7SzhO7MXI0OroYUO88IPX3l98W9c/ijgt7KQ8KJvCpEWhsWrXfJx+3rj75WuINNvOmbDK9nwLB55H//Y9T5d6P/zh6GLyHqICiTfytIV/BkEE+Rkmv8Met4odmGA6M3hv9/A+4SlN3xwAdElNb68SbePS8r/7INIvwzROOo9FkfL9HzUls7jhKKFySZEOdMIrZ9qkagk06vVvSvH8Syjh24Uw9llZ7ardO5/oYSj8RfzFhhVvvrSxDZKtv+iI0VpE69p7NBSyS/GaInHQ2xo1ERM1s3kvqUQFOBcSJ5BDL7QAlXn3MXXHfpt6TWWbdK3mQ8sBqtpGeSLm4esmNtoSLrJlH2/rJKPB2Ojnkm1SxJx5lUyy7bodShpT/rTfepf/KG+duZ0++vDrphgNCpOyqNsTHwekuyZqHlWBko7oT9Q8WO0VkUigxrts36zVJJqXHpqA3eRRZKozStNT/sRY8abuLdF94EbW9USuelOdN1vIipVfehdILb10H47j6FXdJdD/+iwiypfJLjO4nIeS57IpfvEzoASljiP7JqX2BXmp96uBqv9cSLV10CT6A9j6r6f0oLC3LWcy5UzI2W2eiEIlJ4AGyvnxhHYG4NKXhIgudFUPWEdZaYlT9sJGugMWqnYfNINVHaOMYWJrRjsYMG0HjV0Yx2i7ZSrFOJnL9d5ezH4c/s60jcKfz3BTAN/1JMgsxIK8Ufi6s4bSSSjEnCJbDBbJNK8GcvM2aa22qPl+yUWMOlcbZo5s10H4kvGKCsH1bi+nRYDUGiLVu9vJGCiY+RDeM5z8vKUg26dtb8OmzOcogB8QVRsebD9JCWY6GhvkTgnMJza1bNTIi1oaIF32sN8U3pZjJIOtBJ3RrhtT9qMjisQeEw2ITMH6fCIyqx714D7OhRIC1F75pPft1qMR+HMlWZ29kxdOewCCBfNWdfWR9dSJym4XCUqeoOXcwdyAxARCr68pEo330KsYTxuq2rNKjJS3eeWWxY6yEbWQj3s4IY2LX5zGiH9j5VCjWFKgkMRtqMBaTQydIZK5cX9u97gIOg+EvRE4+JrfnHIml/7nRu6X8i1/GikoY5f16wXh1Oyt+oxsD+EdUEFlV1jdHMn+RA/1o2S4nf8EUQfoor1g/UcG+4Ndnz34+p4OfWEjchqzDRGAT6hhj8j+By/jrPuiNJEhMP0Ymagu+IPxXZzgV2enMxpcCyCed9HfKTQIsgKb1PKLz0Eyp/qtZiYaIxqDwnZoYlzmvX4w8BgDACc+uXV3DFk6jLL4yZUkjKaV4Z7WjtA+JfeyqcLRWbMcwaKV9P5X1pz5/gRC6EagOTKUgpbp17tuab5GuBkhBXDENtQJzCeh6Bm6j1DlNxdgJDElFAjPoSiayl9VcKgxvXQhkrCXj2qGaDfSa4TFbrGTdW1MwuvT+tBShz1/gr+0P2iDaC3deh1Zhz6W2lnKAsXyJKt0QDeACmZLK5ny2KJY9nO9DSkD4Wm75rvqVG+JvfqfSm5HH02n+oZPX6NzFgfnahyx1Ux6Bp+AYdjCe2Xnhbyza+unW/AklL7Il2tSaUxY1M5uh9bLBSW1r9f5DNgL/9QjvT2a8EVZ/ndlAVGY2cABvgwLRPMuZjug08lt/u4mGj60sDm3uyODwWPznYDXPusNnr0Hl+xJM9tcrHrjFkQLsEqE0KAHY2KKOP80+kJ/rlIzOQcfeIPf4K9I97SgRPAKD7DDIU50x5xskr3rVAWIIROIe/a9+qeNtI22ylbbIosJRA4+/joEX36N5VDLxytxaXQaCVdIkBjAVw9rApReqyX8ecW2p1BvXvGqpCxPtQ3q9ExM1cStZpekd2sDuU3EDWfp2CtNbOI3P4yDYqx+LgmM3PX5uARDx0ojHHfSbz5uVIdUyD5pm5XjnDeMZ415Gcx82aa1Fxur8W6Q7imaHld9cbGLlccULamAYzIz6Q3XKteq/jNgAs8XP8GmTq3SuYGl3rdq7vTLPK/2RYSRd4NG3D4bpkShAWhEb2m9aiovMBzJNNsDCZmK8nt212bjyA3040mtXIIZxaIBMP6Tm+lI6FlDqtpDkJGl/dFrnRJwEDf25/aLCLSpInHn14TlxDXHRsRMkkHx++mC0FZ0fuNj2Co/LUpaw34qJFB3z3mt9AvpTNFnOJCipbWR0Tnzx9k3wqp4PGPHKi7IvrqrukA6+qe1eBgVj6pc+Az5+i6QpHxe9iSlZ4B+YhL4hPWsLjHCo1fUewjqnSWEKw3n0zTDezqgVm4IpTbFjL4qYFWca6CIaT8QMA8SLnmYZc/Lswm8Y3rHvVknTFqtcQt9wFwpxwEykdevnUJROY07cyaKN+MDjllKwUdWlofMX03hRphJdi61Ue8dFekyy4duU4QssxaReQpIMlKej+CkVxIBe4L6W6kCfPPcH7aINoDpiB6o4THLScje9NltYOlNLIQ7ojFR/OBGsQdm1lE21LUD713g9yciZGrSpqQAbAdqs1BBe5vgKbN66QouMEHWsycU+lco5UhKs7NvI9K0o6xx2frQoT274ymBs6JHY+H31S5oo6wsm8YXHAiOsK4DBV6C1658ZRs5qEFaWzMQInLh0y58ksRtRyvpqFSyxOZhdHVeHyjF52yV7V31jBuzAAsd88lkDX+giOALm/H1pPQpbD0XUtV+qRye5HqnDKlvMah8qf+eXwaLTRfyYz1CDs1yV515IcqV8cAKs7OFOcBjEHqZT7aGGbWByJTh+5cs//VJ4QYaC0AYEa2movyjmFx/r6WPB2tMKns7twb95/z3ien1PIR+WjDryTx7H03oE9jgkWJbs7D+Lxx3genpL4kP5aE+fPiyn43O3zwm/+pftMTPqFgZED+ljZ3oErgRuCwA3XOa0rGOJlWj9YkaUjPLYKyEM4ijN9NrBS+lh1FcPvBGU1uGe/VwzG/JdIMaJV/s/24iqfH/gCyyhbMUWzLrORvnobEz88cHpZBDWuuXs4Sa0eAbzvVFKoVEtj1pzGHOqd0w6/DWnmIVzEriXpCDeYL9kGOppmx7wBKEeDdxRzRzr3s9kZOA2YJ0htm4gWgelTk2jWMIAe/OpVN8WebuZQutIFpxB1Pw0/POg34BKA47tKI6keY5c4qlsL9CxfHTQg+A0I0j1WiF67YUk7KKAGaJoukopzmHHBw+zYGtAqBLx0g7eCCgJsk1uFLcmuTyWiAH6Fj+MyKded8YG9XaDzBAez+LDNFnTf9l16KHXJX8D3kftRuQ1fFhPrXerFSgr3d/FFKWn8244EIDwC4yY8OVey9GCQaALhC1Kkj5+oGN1ir8O0ZkbdxEoHjs/D7XMLXzH3+sBHZ/5Jt2DRRJYVHA+tKpdwTedHe57u2F4BZgVmV3VIAQPTV2+X2AzeTWmDU2VVYJriiuiAUGBSQdXp+r1LZsqgTb65I1goym2myYEtNWmG8yGHRAbE4CfeWe4uD71uHhucsDrFO9+pggwQhbupJfY1bLswJbhWVW0iLgiuRftBRCRl4ayxVNGy6G+HnaE7DnR5PJregPvmMZfRPZlWJoWs4f39bNyKRBVyqvV75gvTsnL1wZDLECG7yfOdUU6w3xvbjPeiq/MD0xpB5+UQ0ZQP/JHVYiao7GMkgBCIM1OvhMmXc32pzzVo1JOba/Aybtmfrlun6cKqURpCFxusLZ38F0Rj4CINjwUDET047OH/4DHGp2UTYrpp7f4y50hZz0VyGrm0yoVlilK8Tmuo11XpBztNaHaFuw3vy8AGHoDoRNTWG4Nt18dp5ANNNu/6aYtZNetrtznuUEVCPQg2NELKAxqhARmOYwpRtpMtJuSSjoKBk2PNJkJk4yBjw7npf4rS64HbG+C1/WLScvUCMagjvZYC8HHda8pLeAc/p8QZr0TQpbwkT9NLX11toorPbTUHSzJlLPtKywRC42MQiN8Q0MRjiodgBEhLvoMDJ0+wjH0/+6C4iaHk3j2AHRuowdgpsHKMQ9dZjXihVykw+SemN8kFi8X23+LgFbHvVDaC4mgfGUXlOwjP/CmwytL1bMzBpci3wT7/OAxtjRp71pDLDPHKPOp7+v+EMKbZtfHNg/za1rVxf5dgAKwQ7Ie8GhA1qoR2BtY0JPNizmfFy14hRczuOl/YDlLtgnHnkGFRnRMqfJ3+4QEycBjVN56ppxGcMH7IRQD6MqLYt6X2t7UTfnJGSDesSSvyM8x7RCPk1MrZpCqxp30W0xE9KO934+UR5pJVPxMhZuTZhXeX7vchimDKfw4fUILqAFKKtJG9xvhzFcfYCCHT7HM8KoeRrANR9X4OhaI5VfX3tXXTKX00FffYgXUGIVwRzsMfFVeP2nAsVkkGQtp/lYECCjZsHuetO16/O8SOQsSUJsBIRLZJN+GnkeCbX/t9fBFuxJxGJ2xcfWnahof97dIQhl8rNgqE9ltgv/6i2DAHryRxHhq9D4kcPkiQ+fVbosazX0TkTVq+0tlHmhrQvbQiafqNlYOJHueFd8bw0OEeSkoiy2ABINbpvwuvrkIPdwlqH/joDqbjQEXf/lpERw52qMzlWpqBhZkxzLvnJCNKW1v0nwmROmW4BymPaxfuRPwOF/OD6eU90lLLls75tkX8X2bB2SW2Zia0YbRx/PlDwEXujMB/KajgkSqIHeczs8cUdE4SSIkxnSsez86FXQpkhPaMsyqM2vfcvWgI0Veb6XN+cURf5dC/WtTATlLpE6BO731H1mSc929reT6gTdfG0RkBYc3C4jHEdmpLwP5wFv/MhWtaTx0QrRKhG/vMPH67W4ZPuIPBg+RWKicfx/L8CHgTJw2RMemkU2F1V6PE+jEcC6RP6fguUrw8vyjblBi+KzB5ARQoOcfAW2qBWeEE1VXZm8shS0/KhhRSseFUoFO9y7SiG1keXtEUZ3WKzITTbooSZB5Rcd7v0kIBSazncLpu4fKiocaAgHDJ+/ldairCq+cCl8xxOaMYch8MK0hyuJz1SQ/GcIiOKkg6tEfJwwQoTOCIr7oYDl4DNd2/0xLtEF6J7U5P3a4aZeumtyf11ZUW4L5qf0Ec5q2wx4zLSE5WBi+xyYhnuJKHkVF3fVe+b3zUubGzgo/25Nkoo+8QWpl+JgtpuvLjqkbd0xZp/90b5IaMs5cqFMyfCnj/Xew2fYhd5F2pg9AqRAtVFUME6ynPI2hvdL2egHW5vF/I1H7lzrw95mSSy43GMxH6mDO5s2Wr/fYzGixw5HmufbMYsdDXYhjVj2o3wh4Oe6IkYx38YeAV9N870s7y9OlS/R3z6RbC111JNGUoH3fFTlmFHg5cOp7aNPwYEYxjAz3A182nMfSMsExSy7e2svqrAelesTyYkr8rUHcDpOfVM+Jww40D7YWeA4LSIwl3hNR7qAkelGT/zpR7a837rl+BuSJp043ge1Q24M8D7DBsJC2UZ9i1hABoIkKTU/v60gCzid9WaEvSkz39vJx1snFwBDhhBcyI4n4Fx9r0ogJT5RYt0Iu99jUnMxZcsD/7kVug0ejM7s6VdzXKctp8V1WSre5XZOSQ8eEIBK2X/R92YUK4AzzKVs0FeX3NwK0tWEMVvDzkxupilzzzB6a8gHKQtGdXQQRy5rtGe00nSY1PZAycbdfYXIEJOAU6fQ16un1gQmDKlHUIMdvSm45fzFfm8zb2VO9aW9iDPMT2IXzHcvKADFitr58XPbWEGgwteM306WPSqrgul1H4Gs0/ytkC0uOk/dGDf9NWMZtXPlvJxPyejuya4DlfEcfBDn7qIluI1d3sWpu3i8co6TRa7bmxTNP3mLjPaSrXN6jbyKI8wonhSiwht0o231j35H3Rqb+DGsAB2pFqWG9djsllVXg4xGr3fwzzIfPrXRTUP4fraIVunAQe7O95Os0cTLSS538y51SNUL4dnEqTqqJNGCv+a2YY2OyYKE89k9+zoud39E/I32lDzICaeWPLsDkG/OK4ecFmzdU2w9MRvjh/U6Bab2vv0XiR2/hfJqtLIopVsQv2/pSLP8XTtIEvg/YITtFXqMN4EvGXcRRVmZO+8bSjDR/5Lo+M3zn+Hq72o6oimWagm3PvgZxx8WFkSlhdzCWaJStpthGba5UE7H6u/idhiloj9wF8Cj9bovJcIdd2ElPJVG+syRlvy0pVvsg5Pneui35Jv1PmkE7/6Ym20mI8zlaa0U1ei0yz5z66aU8OwerM+8FNwYr7zpXfXgfD9LJyYJzodoR1Kt78bfpC7pL5HxZWplXMAtBKuKO1tl9HllWxLULjii8ELOOsejwJ4NVM6Pl1Gzhvd40BItLyrGdSJ6qnXh695vL7sADziRgNkgNIm4FQmAiSptEjmFbEoBfoqBj8q7icXowQPvs5FvfhIMzsXcv8K+l4SkzZ988P850dgNxJzwJe3rKEIdrr/iDzGBtCdhRNkHQ2kw/jXazE+zotR7aSyDjvLY/b7iowmYt6ZdjhWeLsWK6uPGriaFO32GXgSE8WtxPOggOYyfJrcXTc/u60q72s9NKyAw2Y92uI+6jXEEwOCHrTpubV+bq7GVMlr1tqUf/EVAF9K22Dw2UFRVgDrVGhXBXJ/8F2rKZRHORED+5c6dfaJKrXZToPPhi2FMi1ou6alqXaZwUg4S0lNnTDJ5nlxYwxMNakYQwPiTvBRK6zwxIxdDdse0v+KSfPP5cLg0DTRhIuQujjOX1gCbRQjl3TYRfjA6cfkOSAfqqreZnYW0DrFDO0puFgQrJej4OxOEZ652cCqlOxrVV06bBSa+ZvE7dXxQsLnYOAcLrhvcDFYcnkRQGK7Np28011TwDwiQNh+bKdXd9X0T28csXS+rZM7FqSYI3IvDYthSOczScAgcDpQJF9+aNhFXAogb8I2oMEiPPp4O83uUN+ExMdFZ2HkBUj+xOo5UmSGd/n+UMkDrT9p/Bdh95PD/ICoMSD8NsGME3DCgwSY6dLXOTc2EMZq0JGFzjwLrt7xdkZywDAhfPHveSaFi3bIDiMk+GNHOTFSA1ECSmnYRVpH+e3bczkhX+LR+/6v6ZY2/4Wm2mBqvoft1qYW/e9PvKj+zEnvPM32BHgJ2aJ/UcaJUp0QcTZJqVBIz2yVVJSgySrhrBJteUNkDctz65ef0e0rIoSaHPWjpol5xq1LQyzDjV01TKxBV62vkVM9Wkd4qV/ATWD5mkdXanoKXC9f8prFVqQZGhKLPwsOwavqO80UVQQRhxJkRJqKUO2u7p2lL4ADkQp0RQpjPJ15T4B5hy1oLIcaUU0N8SEaV4WHvT9K7sCorhkTwTGeLuwPMlkx6SPtX1cmT2yG7kjIaTzU9F0Jb12NWP21WoXvJ7jt7m6raLK90yJfDzwa/3qT9k2N6e4UkkcPrk6cLd6qACn591RRhfBKE7JVHlhijA0Z1wPKws/u4a2x7Nubmlt8cmo7qUgHPqtdAkhKqs09Ib0T9koJwqvaajC24P066bRY7SDojWMzt1s11a1v/hU2DKDACAHH/9o/HncWzPXI79QIGXc8C19X9QxRfMWR6IGBdMpuIIVn0AYdmCzWVdLEb70+EREdzAe1x63Gd3ATEVXyN0kM5Y08nGPwpZ8M8anaVnT5Jv8Nc5kRU8YJBmL6DVCzBsoRx8aLqueS272c55EscyBLipgUt8wNWdzVELalVUMy8UoEzQiS90B4QEU0S6WmT4T9W7lYji8Gv3DH0TFTPMqujpXV3dehLcrZ6hIspxiNxNz/vVaMEF1OvAXapKUm+XhPKjDrd1V3kj3rybjRpOwn7uLUmT3lLZzX/rCMjPLXHnWSMVh7lfG8vKWcXHlEGPZR0NrGNh4c3nuyWZCvCWlyVWCVjEw/yKGLnPr4wCPPFln2CNouiYLZe1IjfMT7PWyYDYBG1Fov19BNp5qm9YFdVnxPaVd4Kdw4XAox/W3diRlPDY6YQcuIbBqJ83HHfxDD7kXS+U1fs1Vq9RKS6AMy2YxPu7sQQzVXUZ1AjA3vtil7bQcDdluxvYHDvzLQamba7gSpmHfBSNc+JsJtPT/LH8vgPXwTzQtIvnk6RORVAx8uw35c8Ho5Ll25DcVAYpJX/XdOYf0ZiRpwfhn3HxHpMZZlSNYz03KgFhbU0fLxeD6JpJh0glqt+QVInRKIJHtACDt3EcPqvmkotubQyVMCGKvtLIWzVqfmSKhrnCltpYq6dLSzug05XbHuE8KtmLiXZTyUpM3wslBstDshQMVvDGZxWsT87t0bgWA4dTwfxe21WyY+qCwjx7v/jXA3ZgQBQMk7M2C09sSp+XpKOIcPiQZFD7Z7Vroui88IcK89d1q1sAVLNx3CmifO+h6kA+72x5n9PDGJAxI+mJhF/5p8ltFQJC08E2eohxQ5bCj+esTKu9Wnp4xVCG36lkiWwDMwr0SIfocqCoCisLq7zU3PVEQAikLmqsIamd/MglC1rO05U44LS36PIe34Px88CwMjNaCI6a4/UI7tauqn6ZFy85FAzxEk63b9cN04LVVFypLwv8iBYHEUVlDmgOj3bdkRtOA6BBDzKSMmaf5UVR7yFO6sB+VJwufwbj/XWteoTVlRDgO1plWQTBue5rVYGm9R/g6D3PsM+EaE3GMV3DTJGkK2keH6VslpHCs7rzIGlFwx/i7SRDr0VEoWrQqu3+ThCswPXy2B8YM/r3UMRax/vYZOPht75QUIF8oxl07R78VGDnqn12otj2Vq+2WYP1ZOqOU7fy/QbQQVn7XRcEn+yw7/7Kvp9VpcnPrdRBSKzMx5Jc9wQ0rCGLXy5baH3yI1lGroQ2yBQAPn/hSW9yUs9ta60YUz2Kk4dk9XhqQHnieCP6h7i+LnPD2jURzcY8AJ2kLQo/fDAWzanaGfIT39d8t2QYfvBnnB3xvMv9/5HTpqaeMwtVZ+oqpdEOGDc6+u6WbWbsK2KWoDgOoig3b1b0b9tqn8RMbXzidKDajYL2qfrlYov5vzO2HKgnDL6U8JTkvWXqOARrG3oK0pVDJVZUjttFLoslL/TEmmHoITIT9J3tundRUb8dmJzI34M94W+lVXA0ixrcL/p77IA4GHS0+3N1XV/3/NJ9VtHC0bRwfTPgn6sOWSTTCTHqcv4NbxnD63tgc26OPFjr5GhReEF2sWTa8892v2EGmVb11IpqeHMeqmmGYmB+WAvHb0XgJ6bUV/PkRumucofr24OQ4eWYcdBYDNGTKZghiLwKrcK3XOFwm2aY7V1pV4BZefg0t6//UIxq0XH8TUup6RSRF09auPOMwRC6pcppsoF1YRDv3dyA1zCNsat+WjDO2mX8BslOiUuedO+gQd8dOS+MuaX7DJOUjErDlH+Ib90yvkrdaIuRbd3U9Bp8BQ1am0r7ybas8DJjnZq1hu37+PyJEvUv0VLrzKwDgLGF4vY4VUDI3o/SZtLysgzFfRcwlIjCyWzvC1TIpPyX3Cb4yCT/BP49YwD+URbwcSti3TMEQEfC/sgFJwZrR8lqg5zZdkIfqtvZp5JfeD2lzHnXkLzPs0erTWkI5rJFyreXpDoemsCak3l1Ox/R787A1+oW8VbXpS6jiZgCZ4WUdnv+lhCaLpWq2/dSy1nxUZ3LuY+awagJmkqrE35x0nbD2sBPmSva4/zIWXrzg6vjcX95b6Icq1JTaTKZnF+E1qdEv2AywTOhl6H8vztmF4ctIuOKWIM1wQxR+/EhMPTy09wBnhfMg5l/y31ioMJz6tTWGaPDq/YNnSZ2ayneHSPpckERgT0L5vxum1jaT1aYo55V2NK8DUg4f7FWNSjTz66vroQRg98VIRLacXU0lcmkLRIiwFi9fuT31SZUfYPhGVp9VwoZwpE8H4TZnEokxL1lAmSKNH4eeA2Qq6qQBax4wUGdNsMXUF4OfgjGDlsiP0lY1hldKLTj83Q9bsUYQsMG8yu0AHdfnAY9cRo3CkPu8aQhfHat6FOF9kl8wxPXAsGUcJGMqDzmPI9NKZzzDgfQbfdM5y/coCIW7+TnDygJIFYfN3mypoIxCtDuOSN7NLqTSqEhs9KRkrz4l+4hWKuuORxc7PuFZf8GwD03qjQMdBi7NStNRLnzl3Ny6imMyfTVfeulik8b+0rN/R4LXl90B0iNNzc4mupEZO3JO8acqrcOXE1IUt+NXxnba9edT18tjX25IFxgatYCpXJAlUJjworI8QleOtMTYNUijdueBPeI8vxnsTkcnAvnmezJUrTf5KIx2m6THBJi/M8PYsBdwlYE1ADdWgxMW8VQAPjGLgEv+rRmFiKwbc+uNeZm672rXcfoRIwublVJQJUOI1mTX7txqLKJKnRnczhXwRruKBwS8cTqyWsULwt1lBo3sDHj5UBui9ep40rx7SWKTPSpNY5SRshfmvoEmCJs/Cm6RzMaWIxknrP/edkDnv3lbTNM8tm/gks7E3yj6BFS4HJPjhfX1toruTQjBmWS7uOU50jZv7XBqB8TXO9FLb5B/EG1IlSq9UcAffp4oyJIl8A/8oSPJRAfGGGz0Bcbv1iw6FGimKhgzn/IQrTqGi26hYuRZYoVX7+LPIUOPvKFysGmz8HTT970so+1/BV8RJ+DOhx7N4CalKcYQj4tE3oPcgUI2lRnZXouG8YeaYtQVsq8d5udheT5+LPkfm6YR9VtuhQ+QfZ52HNq8wg/bRguSs2HyycXAIZLNwzh5eKsyPiJs7Qz589MtWD++81jNFrzxWcTYmE2Vbr/15yqK9eAViWBSZCprHxdHXWr0XUALQTNBa9ATUfYjToLaaVQqcDej2Jsl/AXEHF5488F0emXYgEWat7vKzZ1t7Omkit22MNXCPmRE8SAXd8uTFvT/yqkbBYvDSSe4O097Xy7o4JITP+3Qyb9NGlj+n5GcFwAKGj+3BeNE8dKwpIXH9ZbRhTmLS6VeeNaDCLKQ4vwIeO/iFPTWJ57tCAmfHR55JTYeQNjluGJcetak1UPFPAj4BbPzCJfqMWMopuDvIYnIy1wN7/eidF7kNSvNUaSChzfw6iBI4yIXTzN2O1kII2D9uw23cbQbb20OqE67uBjxDhuZ6zu20NIF7ahQbOQCwwQNQS5iopQYA87++ACOAm7fjqSI2SIHyHXmR0l+MYgfuluyCONn2e88QDoeWUDpToFnwiAOoxJf9Et1vDGTpsbRoew4MO/g7m2TpA/YxfAG2W2DjDFonOXM7EMjH/MSRW186UsYUlLZO8p7lHtKhauR+RwK+xNts5Cq/2K08lf6feycfHU4fQkU2Xu1x7Rc4piCXXaxI4CRUxSQ006K9xI4i/5V6j/SjDFzuElbM4vcr+v20DIuSshEIt83Gc48pgWuxQWCSsRwaLqEEbJzUpChfNGuBOKK2pOxEKvbo3dkilBG3nDfaAshZ69iCD5Nr3cCDQh59FGADPEcE9zuw7Yc70BclJdyxebby2vaO6T+0mKoSiFzS+4+YP4EFt9axqQaQKLGwE24NGJPdQ9LuvkJzbrhtQutjPz9VWeIAKk6d6rRrXDLq4up1RTd0EmxLs1TXV9zvu12Et2GHHV3mCaHGHLppbEgSjoBoU1hJUvux38HkHxLqORd1AvldsFeBLyVbGIpJGmszgaaHJpcrVZCzI3GSpItQDS965aQ/qMbBjqWiKkpogpFe8MXSPRmhvKtWdjsamYF/NmSGRNjMiIDCAL/mcTWq4BQXXi4LTN/qC6Wpl8gbzfPgkTYSuNt7Eo6/htoObwkQar2C/a/q0n3W4ySfweKA0Codez3rJz42x/NcUCqrLmRWpcdQT4PDUAOc6frtUDkrxKq2+mn9wpLiWBEO/y8msy96nxZbjhkbS0mfTV4/OVpB1+nBCy9qxuwWn84DvHmHWpnUL6VJirnm/olKZL89f823Q06BI9MXO/SL2fo+c74utxMUA6QGI68xHVdxToU+uFXeG055+Kr3Ymizavt+ZcZWon2815vvRE/LX6RCNQXevQuBRTqwg4BmkNPg4GSz0s5HSxLlG8CQgR+TemEOTd+hPrOczGZlGmRwThpteJarH35aWFczZ5VfEdkPlUPsgYPM9stOX3770KvVHFaGTeIB5xcsw0r1xBCPJ88km4Y2HCUBrfnj6gYOBSej9nA8St5mbuJodnf3rwPyUkMaSZEsGlr/mvYN1c1SoSMfWhRdzrf0/mv+GUQhHLQp6QgbA8O/uerQwiKgCaT0h7zMBUtGQkAxwMR7lVp3NmF76mlgcGde6JL/Wa6yj20lNGU+w8D78hM2ZjDugtZXPajhEEClL/e2x2R0bMQg7/pyCbPxPaUxoJA0+GObXXObLfEXnnNeipBRqncGL0zjMXbkQYY/DkQ9fQ3xX2zTwWAREVyOU95T3Qj/BFXJ+J4lnnc3V4G5FgDfbm82p7YRo7PVERkxUSn3/8c/lDoXU36UtSMcMaDc47jk2Mbf/dZye4Nv4PpvZNT8u3Czuv30IKKFmk3zuNjrrvizzMXgX3cCFykcuss7u5de9InaBTbLgmPKerRvCMHvLVQh7rrpzjn+t2yYyia9rISMVpMl3FTIBf65iD9yEdYbzj9n8OUf0XrHpYOhhyQkNtH5TY+9I7XhyXGkI5f1oN7dKibC00tf2SdIz2ryCXrScLSd0XIsaCptlprgtr04U22XYiVCzqD6blN8fK9RzII1bvfyf94YZKYgihOxsbx8ezznRz+uQ32nfwjgEaABD3DZkKC3m7rhLqJsg3i2q1B0fYSgG+dpEX7u7QB7xc6RFpOAb2/OW2HAPtWMOPqG/+LtKmfq4o+ZkB4jrVlcizYWcxjYquxAi77CdXAaSdOYYDnUBWsbRgRtS4dCGwnXUaWr4X18u/j9sI/xGSkksFb8EMPkgNW+8alU86/P4t3jboDXsjOtvB7aDbIpAQs+7t9uH5WskuoTOHFpyi8TcdJMsOZkKssQ17MNfTWT/hgK17nwE582JS6ZFXGngXcWcv2Jfwz8kqdCP+EJITfn1mO1yFqHmVsGfC8l6XPah6ng1aexKrG8+lyDd/oEDEWzdQYU+XVZ1rd2OFIL3eOHpi0EHs6S8Wl1Q3gnOqUtafk0iGaMhsG5AJCgJqL7zUherz3esa589B+h069+Zzv/7dbnIvE2YJMqe119ucACWFY7czqPBzE9/8w+JFgN+gMV/E8Pd+Ivx1eodmw6TyoBfaUop8gYj95AyfMg9+eShpQh5DGjzD3Gud5BDYN7gMvxETfPmqZQVz3F4ZN9+eFdu47V5R/saN9taGx+4zJ0Hqz/Zci9i1TjVJTlJE5+64lTFEGrfc9hNcugg3dcxTyt4SwRG5ThDeV2HnqfSWT4Hm1yGcb4Lq5Jx5pw9VnVuGJJMJz3LfMua/tcH7+H2vVOTaFaSjcdY+PRhlnadYNlWXLMjkDtu1lDGulRNY3L7GlHQJeSniduzm0Tcoh+2MIcLNiTew2HQ1bmXGON55Dsp5l+sI9p0bA9XkIdD1wv64su4va4bPdy/Z99IuVI9cwATplAvENlndKGDxSDZrMOWeS4PQ+0E9bNZ6Qj13ZKsXDPsrWToUOs1BqxLOfS/iCdbgAl6qs4Dl2xf9i9tNXRwqkjyWyr7wg7l2gVQPi31UdbD2NHQLVvVdW+Pxsf9+EvQBL5CZg2CEb9x4QgQ2VmSweUlAl9BxsIvSIRctrETNb5WwKZUBVyHJEEE6LaOU1+F43dWuZcNIwPPpBtccHWEafZfOdf0ODfvZtAQR7wpk317L9b6D2LVr3ndtng4bsE5N7PtjmcS1+O52ZQtRVCePfk1BuAr/BrB/91ricx0FBkG+Y5kP/sEntfQJYK78/POvEe/NfpZI0qeGFoWt9ZvzwY2tZ7ACUQYqnF564BM3sa4q+csULa92/b8M1aNHghClH189FAllU/5kHj2u0fnntC21HwjzPsfGrhjciVHxjpbIk87kelWFb2C37NfGkpRYFgVK01bLAz7pklCOM3N+MvDWKl8IaqOSyd8oleHAcKQFSC0+ReATn8T7N7c9c6wNh/iqBvFIu7eqz1o8KIvF4yOBPuvK5Ky2DIv3+Rw3FrcH15qvcIHXrnePU514zUwQ3p9LEnUZsbuohgfbctveO3eiMqeIr1nWOKq+ZVtAgPsxjJFlFKXeiSFHTfGkUo9jqSluR8uY7dgVlAZgs06rUKJGXK7C3AWzJfM4wD7+TNALCP+ObXWTqvf+Rn95Oc/zGCqduqhyHhXk+KL8t9VJId9xWa+ulDf3HxyINDNgxYVKSf+PFt7TVXEadkR+lrm7eg+zNAMmM8cp8vb2yGofIAsFdutp7DSSu0c8MAlQ9qrZO401S3t4zwD0Pkjmb0Gt5MNuwqB1K6pPU/slP6ns7x4c7MOxRJZXlFYUoVqnV5DryfZ7yc3OPbyiUsulrA3tYDXf2OuX2vB9QoP9Kx2qdlM/dY5+yRyZzt9duZOOGrp0bg4uQiGRWtwJtTjcQyhRVeDwSUaeyg9iVluUdZQqyS0c8bFcYeNSFin2j9ZyHt7TPDLSvWcUfZE+azpmKDyHxrts7DJaQ2aJ/ntdZ1YvcAGZG0r1dUL4s9kjfi7+ajWZVr1DgWtqP6ky+hwTk1eZ/lIXi43dUq+nJlIaTMjv1NU8xasgSWKP2E5qefX3AsISUWYUaKYEG+HoGNA132w4qNKAWtlLL6SYVh1BV1TEGL+PJM0eUirdMowe2iNxIHj1KYn3lIYXPIctmxKlS3ZMYHRbJrEf+oGZJGti2r/cAT3aKpsYW69YKCG3T5Cq+f8RzrJutjs1fekkQzn7uec76bOlXiX+7sZ5l3D7tMPdA2Zz9zISElfuGGpje1PHhRjdlpgDlg0Rtp7xk+dugpWfrgUZVyRbWLq9CJJL4QrZsaCYH70GOsIaExC5N4hYriRTtUjiW/9mKNaGjnU2Lnu5nkUgPzGukUGvOoD6KORUOSHpKAmQ4UQWlmNr/3JuSBcA5X9JxXnhY0OdTARAh3GtakxtVNmEI9lwe1Z4l0vFQlOR3gISBsHgGUvagtAgh9GCJIaGe7w9AlR2VdYtv9M7gVyk5clh91jtCmb9FKN5yxAbUXr7HKiEyPQT866nucJXS0a/LVWjKw2ww7J3zczkkpXplPBeZ9tCQr813/WKRYZM0vXPas6jUiHBLeApzIMuTNfz7DjqYexQgieDCWiFS1MPgRoM4ycASaHOA3ofLkrF1+XSCB527FkeAQSoa8/9kXS8cg/1iH1gxtTjEzFgS1SFaRhy2Cx6Q3+rgesB3BiLPVoJ4nnzHibRu8AIX25r8s2klPNTgqwnGDJ7Trr6fPfdceNcpfdA8FEuRxDXxIeVzfm3zTOfxd6mNy54XjcHwJKDy8Phvk6lr+sVnlKkpMP76BtzSpJTp87/k5nC+cV8xh554kZD+aIkUr0jLdFDIAipKETGOSTya3ASFPU0dQesyiI6gCg8SJF8TAFTEfOUwgjLw7JCL1pniBqKjTV0vUnxqUH2OBhztSY/JMdSGTs8jZ+Qcl+DEb0dg5Eip246lS8mqt2+IebIoQ/Q9pSzHBddIXl+0mmqC7uKWr8/YVeZSZH7QyIanDs7jE6ClT0HIY9MD3r5Ync3VDdvQwEEcHprALywT5NUrvtUXQkYraXaW5xqJfDWyxY5Syp+1a8JnxWzHXCJFWhAkD9MlP/tvFM+2Zh3jGDboUdNjcGhz5VeDv6L/QQBpnTP0Oqs1YSLeqGh3FrB+kXOIIIX196Yl66rreshlcag9TkReUScC7MW+iDPGRFJm6OaU4QpzLr6zLHvlipqF5Qe+FU3up8oYZHipOi18IDzcennm3OXgw/Fn1BlceXXJAyvDSXpqeS7p9+PzGDxa7qNSjUyOgCtWPzR0Sp4UzNY+zVSqIykznx94ba8BPWncVwVPErKwl4oDWgVo2c7UgELUOaDwlxu+vzRgc5VijjmBzgLtS1jA/Fmvht+x1AYCfjm4XTzZtgdb4BM6eJo+8C7a0UC7ozmuDfwDPbhXPCAsVutYVq/PmkQs4dUYo8NFOIM6Q5m/DIJCubV2Z1hzOFdbZrutk/bPEFrKLYpJR//yC+qTu+7EzP0JgBWO4be3FvnT0komkpDjXHNO8Ss1uQD1dw/fk67CN9px694ahTJeK962fCtFXetH9CyP5ZqCfJVZ0+yRoDZrMJgxeh7L8wBz++pyCwfspUIRzG2UwgWFx9CwwJ1sFq/8Xbj/7z+gRj1dIuAeshU7e0Obd/ciaflpLY1qDtPHDNv2MNhPf3YTruZWmhoJN+ePA5nhlxtX8RQ4CiIBgxQa6fy8aQgtuLFxXo14q6jN8ex2uaqqAOuSmIb8eZBDTNNrHcYZF4wgLhrnmijZaqzBwJ+dITUpGvmE5BdtCy7pyWSOHzzg6yeenV75lWoSBjlGmkAP3d3XqFO8zbtWKv8qPQ4+ePWmN+EzTpHig1ueZrNgl6nRRsYDrkUTxjhxklX6arw+8/aaI9RZ+MkhXaj0nC8z+77HrTBPWLxaCBP9RBa5ACD6QA7MoNDeMjrAuq65ePExuNKjmus3oQHkdeEC089FBoqvrLRXfdfaoZ5Du6Gx0eqyRA/0N4+3P5aPhZj2gpt0i9//1kE4kuGHJqfour4bM6pJVDmktadxwEOIPs6ajaMqzjyEJ1VVZwlMBMAXmGk2cNtcoAAcQrqfNu/1QPssM8lK4552YR/Y4GgDsE39wZNzVEnn4uTAcY+RmQPbJ0g4MkH+uxTmaJONi1T8nq+09EvLmsSvHmBK7U94r+UOBv8xa9vpKisCOuWfoxKiQxkbC5sVnlKilCNX/CjP7WLKuUqxPhPOXK1GhRR/8lkzoCOIzxCKy/BPflobLIwf/hEXdm5n0YBXgkhI+Gjf7KhSseDnQafZyTUNyPT15HgKwIz/PSENNFAcZ3nawmh2NlsrEzI8ZPQN9LzNSUKR7IN4ux06PecRVvPAeTngbEZmws7JlT5ZjBUievhrgKFZAsXYWScDIepTfG8MAwMQPS/6646TyLnfqkZGLIrUfRiVT1zKWLBXu98w0eXeXKBLaQebGQ3Z71HUknd6SQVhBbu3sr0OTgczLl21iaCanP9rdt3V3MlCN1H+foL4HtMoGVYDlkj1KEFGluwsDI62wZxRMdjJKiVPE+9M5fctNmMnOo1lZolFJyPWyhDb+wCZsKeQz1Cvg2cPsTfbTis9lhA3MvYlIjGTmuUW2qhQKJJK8U+yNenxbF4pEo/tnJc0keV8001J6/dbR1xHDyT35WKnMhSWV2fHtif1h8fd0NLHhETdfcrMr+eT/SOWba7tjrqt8uRk3DHsnLxeHxChCT2EfFKJy9GoOrsn4FHkoOe+I+HYgvifQYVhph7kEAgLjwMrbwnYKiZEoKHNU6zBJiFQFoYu+799nRvSCT7SGlGoBxfp6mrDP4HGkgHsBc+DRsuAOqC4v1ZJrf9yf6G6FGti4zC59PJNETsCALhuOxQTuVLUl/J71j5zY2ABzLhGXysN5oo6x9fe0w8pGJVslrC8ueBZK0lQg6XYGAVzP+ua4rOLnU/TUNDH34MalsjBBYN+EpXKHMq+cumngNtevCZ1LBi+HA+nWXjFX4QRQLNI6kkVFr5R/tYDOpygSP5M8HxSHyEPw/HuAo+orgZxqgx1gf7SwcPoIyRkzhBFNGQ0705Om+cOn8du3p7VfB75u9DfTdpWfIPnrUijiFDN8zbgWfnyaWhWnh21sCZhRTUSf9oeaUwlEr/prN9yTI9L2AeNF+A27CAYoptiwPyOtMeHoxdQDmvKDrI9FU7HM1keBiABQX9h4hYvItLLsErVUZj2lkLV7d2JfxPf+A8xZPw4vSKCIcv3A/d+6DFvF4hB+4D2xFe9X/R5Rr3GBPncXGjIJnu9UQOld1SQJVMfhEzkD49RZujN2l1XZYwS3R9dqJlmfWMCFV8xfhFvWf39DVKuyP0TQBc68kJG70HEndBn4pCeMtYvLMl1LifP/zCDNmNMxbqib49Yr4xGaZbKfRI59m/aMZntmUnU3YyVfoX2Z05J30lA2T3/zAKvkZZcYH7HUOVvepVFmLZZRvanPwXjFzsTVJh4pLGjfjfSPKNrQEp+bQAkHqSn68oQHcQN2Spln6cZqbwbRlLhAqenq5u5dQZh0H49ROcCIJtSukfsbcPeExxiFVzQ7Du5rz97/sp9563wQYbWQTqjyIF9VuIqMqoXe7/Cn+HCQ44tu/d3RZ/PHmSOSaB5zA17Ihk4suZtn4fdBSY1FjyVyV24ufY0XhI/aRqtEgxM9Eqv/q2Y698MoeEbwuWKTl2OC8RK7k45nM5+a1FGGolsweDDHnXANYbPBaaAJFqwCzw+PeREByimZ/Nx7nxSKnO1yUIulTu3EWic8rWs4DUCyPQEe+mh9Ayj8xWlrZySPGH6el7ZlnaDqcOmVRqBv19CdsPsCFLWl5dZ2Po0Pj7zELEkhMaraKbkFllOAOyCQtngMs4+8ZFI7HbarhjCN+ZICJyP9++j+k5WmTi0FAi2ONeE59dMGIhXzE+RKbtCB3trhimx6uo2q8WnFTbYEynwmd+ZdYcnZuWYWsveTon3vvAYENoWTfdE992f/QtJpmfvWteFsMO1sERFTBgn6m5qb+g1ZnopFa989+S3nJn01Beh+WGGd/7VTbAOVZ/EvoX0utswzyRkHf37VWi0fo+1ptdWFynHsELlZyNiMuSSdASHDg=
        - #1:
          - type: tool-result
          - toolCallId: 6HTHB9Gp1g5D28wP
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: a3Yas31CLa5eJuNF
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: d1m9BtDlwIsfuqCa
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.