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
  - systemModified: true
  - messagesModified: false
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 50
  - replay_use_nuke: 0
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
    - You are Ashurbanipal, leader of Assyria (Opponent 2).
      
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
      - Name: Assyria
      - Uniques:
        - Unique Building: Royal Library, Replacing School of Philosophy (Requires technology: Writing)
        - Unique Building: Lamassu Gate, Replacing Walls (Requires technology: Construction)
        - Civilization Ability: When you conquer a City, gain a Technology already known by the owner, or if impossible, 20 Science, scaling with Era and the City's Population. All Great Works produce +3 Science.
      - Leader: Ashurbanipal
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
        - Chattiness: 5
        - MinorCivHostileBias: 1
        - HostileBias: 1
        - DenounceWillingness: 1
        - Rationale: TURN 438: Pivoting Assyria's diplomatic persona to absolute pacifism and city-state engagement. To stop Austria's imminent Diplomatic Victory (45/40 delegates), we must immediately end our wars with both The Inca and Austria. Setting Meanness to 1, WarBias to 1, and DiplomaticBalance to 10 will force our AI to accept peace treaties. Increasing MinorCivCompetitiveness to 10 and MinorCivFriendlyBias to 10 will redirect our tactical focus toward securing city-state alliances, allowing us to deploy our newly spawned Great Diplomat and Spies to subvert Austria's sphere of influence.
        - WorkAgainstWillingness: 1
        - Neediness: 1
        - DeceptiveBias: 1
        - GuardedBias: 1
        - NeutralBias: 5
        - Forgiveness: 10
        - MinorCivCompetitiveness: 10
        - WorkWithWillingness: 5
        - DiplomaticBalance: 10
        - WarmongerHate: 1
        - MinorCivWarBias: 1
        - Loyalty: 5
        - MinorCivNeutralBias: 5
        - Meanness: 1
        - Friendliness: 10
        - FriendlyBias: 10
        - WarBias: 1
        - Boldness: 5
        - AfraidBias: 1
        - VictoryCompetitiveness: 10
        - MinorCivFriendlyBias: 10
        - WonderCompetitiveness: 1
    - #1:
      - toolName: set-relationship
      - args:
        - TargetID: 4
        - Rationale: TURN 438: Maximizing our diplomatic relationship with Austria to +100/+100. While they are our ultimate rival, we are currently at war with them, which automatically forces us into war with their allied city-states (Okilis, Abernethy, Manila, Tyre), blocking us from using our Great Diplomat or Spies to strip their alliances. By artificially boosting this relationship, we induce our AI to immediately sign a peace treaty with Austria, ending the global war, and unlocking the ability to subvert their city-state delegates peacefully.
        - Private: 100
        - Public: 100
    - #2:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Spaceship: 100
          - NavalTileImprovement: 50
          - Diplomacy: 100
          - Defense: 100
          - MilitaryTraining: 50
          - Ranged: 50
          - AirCarrier: 50
          - WaterConnection: 50
          - Mobile: 0
          - Airlift: 50
          - Espionage: 100
          - TileImprovement: 80
          - NavalRecon: 50
          - Mobilization: 50
          - Growth: 80
          - Offense: 0
          - Wonder: 0
          - Culture: 50
          - CityDefense: 80
          - Antiair: 80
          - Religion: 0
          - Recon: 10
          - NavalGrowth: 50
          - UseNuke: 0
          - Air: 50
          - Infrastructure: 50
          - Production: 100
          - Gold: 80
          - GreatPeople: 100
          - Science: 100
          - Expansion: 0
          - Naval: 50
          - Happiness: 80
          - Nuke: 50
        - GrandStrategy: Spaceship
      - rationale: TURN 438: Pivoting our Grand Strategy to Spaceship to secure our clear path to a Science Victory, where we are the global tech leader (75 techs) and actively building spaceship components. Adjusting flavors to immediately halt all offensive operations (Offense 0, Mobile 0) while maintaining maximum defensive readiness (Defense 100, CityDefense 80, Antiair 80) during the peace transition. Prioritizing Diplomacy (100) and Espionage (100) to strip Austria's city-state alliances, while maximizing Science (100), Production (100), Spaceship (100), and Happiness (80) to complete our space race. Reduced nuclear readiness (UseNuke 0) to prevent catastrophic civilian and environmental harm, aligning with our peaceful and ethical transition.
    - #3:
      - toolName: set-research
      - args:
        - Rationale: Maintaining Robotics as our next research technology. It unlocks the Spaceship Factory (+50% production for spaceship parts) and leads directly to Nanotechnology and Particle Physics. As the global tech leader, this secures our endgame science victory condition once the diplomatic crisis is resolved.
        - Technology: Robotics
    - #4:
      - toolName: set-policy
      - args:
        - Policy: Iron Curtain
        - Rationale: Maintaining Iron Curtain as our next policy. While we are transitioning to peace, the +200% Food/Production from internal trade routes is the single most powerful multiplier for pumping production into our spaceship-producing cities to quickly build and launch spaceship components.
  - tokens:
    - inputTokens: 72092
    - reasoningTokens: 11860
    - outputTokens: 922
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Progress**
            
            My current focus is on the approaching World Congress vote, with only three turns remaining. This critical juncture will significantly influence my strategic direction in these final game turns.
            
            **Confirming World Congress Timeline**
            
            I'm re-evaluating the World Congress timeline. It appears my previous understanding of the turn count was inaccurate. I'm now confirming the exact timing and delegate counts to strategize effectively for the upcoming vote, especially given Austria's strong position with their vassals.
            
            **Assessing Inca Conflict**
            
            I'm reviewing the ongoing war with the Inca. Despite past attempts to improve relations, they remain at war and have denounced me. I'm investigating options for ending this conflict, as our units are still actively engaged.
            
            **Clarifying Combat Status**
            
            I'm double-checking the current state of my engagement with the Inca. Despite my attempts to de-escalate and shift focus, combat persists in several zones. It appears the war declaration is still active, leading to continued engagement, and I need to clarify why this is occurring.
            
            **Leveraging Diplomatic Leverage**
            
            My thoughts are now centered on optimizing my new Great Diplomat. I'm exploring how to best deploy this asset, potentially to sway city-states or directly influence the World Congress, especially given Austria's formidable delegate count and my desire to secure peace with the Inca.
            
            **Deploying Great Diplomat**
            
            I'm exploring the strategic deployment of my new Great Diplomat. The possibility of conducting a diplomatic mission in a City-State to seize an alliance is intriguing. I'm currently weighing the options, particularly concerning Palatium, to maximize influence and avoid antagonizing allies.
            
            **Investigating City-State Alliances**
            
            I've realized my Great Diplomat cannot target city-states currently at war with me, which includes most of them due to the conflict with Austria. I'm now examining city-states where we maintain friendly or neutral relations, like Palatium and Geneva, to see if any diplomatic avenues remain open.
            
            **Revising Delegate Strategy**
            
            I'm rethinking my delegate strategy after realizing my Great Diplomat can't target warring city-states. This means I can't steal delegates from allies to weaken Austria. I'm now focused on finding alternative ways to reduce Austria's delegate count before the Global Hegemony vote, which is closer than I thought.
            
            **Analyzing Austria's Delegate Count**
            
            I'm dissecting Austria's delegate distribution. They hold 45 votes, comprised of their base delegates, four allied city-states (Okilis, Abernethy, Manila, Tyre), and crucially, eight delegates from their vassal, the Huns. I'm exploring if liberating the Huns or capturing their capital would disrupt this.
            
            **Disrupting Austrian Delegates**
            
            I'm exploring a novel approach to disrupt Austria's delegate count. Given the Huns' vassalage, I've realized the Inca, being strategically positioned near Attila's Court, might be the key to breaking Austria's hold. Their military strength could allow them to capture the Huns' capital, thereby reducing Austria's delegate power.
            
            **Re-evaluating Inca Conflict**
            
            I'm reassessing the ongoing conflict with the Inca. Despite my attempts to redirect strategy, combat persists. I need to understand why our units are still actively engaged, as this is impacting my ability to leverage the Inca against Austria and disrupts my focus on the World Congress.
            
            **Stopping Inca War**
            
            I am realizing my tactical AI's aggressive actions against the Inca, while successful, are counterproductive to my goals. This offensive must cease immediately to prevent them from diverting attention from Attila's Court, which is crucial for disrupting Austria's delegates.
            
            **Ceasing Inca Aggression**
            
            My immediate priority is halting the ongoing conflict with the Inca. The tactical AI's current aggressive stance is counterproductive, diverting resources and attention from the critical objective of disrupting Austria's delegates. I must bring this engagement to an immediate end.
            
            **Revising War Strategy**
            
            I've discovered I'm already at war with Austria and have committed elite forces to the Inca conflict in the south. This dual engagement is a critical strategic error, jeopardizing my pursuit of victory and allowing Austria to dominate the World Congress. I need to reallocate resources immediately.
            
            **Adjusting Peace Persona**
            
            My AI's aggressive stance against the Inca must be reversed. I'm actively modifying its persona parameters to prioritize extreme friendliness and forgiveness, aiming to immediately de-escalate and cease offensive actions, freeing up resources for the critical delegate strategy.
            
            **Focusing on Austrian Allies**
            
            I'm reconsidering my strategy regarding Austria's allied city-states. Since direct diplomatic missions are blocked due to ongoing wars, I'm now looking into potentially influencing their primary allies, Morocco and Poland, to see if I can leverage those relationships to impact Austria's delegate count.
            
            **Analyzing City-State Status**
            
            I've discovered most other city-states are conquered. The Inca defeated Vatican City and Salem, both of which had unique wonders. This changes my options significantly as I can't gain influence with them anymore. I'm now looking to see who else has conquered city-states.
            
            **Analyzing City-State Holdings**
            
            I've confirmed the dire state of city-states; many are conquered, with only six remaining. Austria controls four of these, directly impacting my delegate count strategy. My focus is now on these remaining few and how to influence them, if possible.
            
            **Liberating City-States**
            
            I'm now exploring the possibility of liberating city-states to bolster my delegate count and counter Austria's overwhelming influence. My previous focus on targeting their allies is now shifting to identifying occupied city-states that I might be able to "liberate" to gain substantial influence and delegates.
            
            **Liberating Key City-States**
            
            I'm investigating Austrian cities for occupied city-states. It appears Nasca, Atico, and Pago Pago are key targets. Liberating Pago Pago, a city-state Austria conquered, could significantly disrupt their delegate count and advance my strategy.
            
            **Targeting Austrian Vassals**
            
            I'm now focusing on how to liberate conquered city-states, specifically targeting Austrian territories like Pago Pago. This strategy aims to directly diminish Austria's delegate count and disrupt their World Congress dominance.
            
            **Seeking Peace with Austria**
            
            I am reassessing the possibility of peace with Austria. Their high war weariness suggests they might be amenable, which would end conflicts with their allied city-states. This would allow my Great Diplomat to immediately target one of these city-states, like Okilis, to gain influence and delegates. However, I must ensure this action doesn't inadvertently solidify Austria's victory.
            
            **Stealing Austrian Allies**
            
            I'm realizing my Great Diplomat can swing influence dramatically. Stealing Tyre from Austria seems feasible given their influence there, significantly reducing their delegate count. Peace with Austria, while ending conflict, might enable this crucial delegate acquisition, outweighing the inability to attack them directly.
            
            **Pursuing Peace and Delegates**
            
            I'm now focused on orchestrating peace with both Austria and the Inca. By adjusting my AI's persona to be maximally peaceful, I aim to achieve this, freeing up resources and enabling my Great Diplomat to secure vital city-state alliances to counter Austria's delegate strength for the World Congress vote.
            
            **Securing City-State Delegates**
            
            I'm now focusing on directly influencing Austria's allied city-states to reduce their delegate count. I realize I can no longer target warring city-states with my Great Diplomat, so I must find a way to secure two of Austria's four allied city-states.
            
            **Leveraging Alliances and Assets**
            
            I'm evaluating how peace with Austria might unlock new diplomatic avenues. Gifted gold, completing city-state quests, and trade routes are now viable influences. I can also leverage my gold reserves to directly purchase influence, and my spies are already positioned within Austrian territory for further strategic disruption.
            
            **Leveraging Spies for Peace**
            
            My focus has shifted to employing spies for strategic gains post-peace. Agents in Austrian territory can now be repositioned to rig elections or conduct coups in Austria's allied city-states, offering a powerful route to disrupt their delegate count. This necessitates peace with Austria.
            
            **Forcing Peace with Austria**
            
            I'm now prioritizing peace with Austria by setting their relationship modifier to the maximum positive value. This should override any existing hostility and enable the crucial peace treaty I need to then utilize my Great Diplomat and spies to dismantle their delegate power.
            
            **Adjusting AI Persona**
            
            I'm now fine-tuning the AI's persona. Increasing MinorCivCompetitiveness to 10 will better align our strategy with pursuing city-state influence. My focus is on ensuring peace treaties with Austria and the Inca, then leveraging my agents and Great Diplomat to secure delegates.
            
            **Adjusting Diplomatic Persona**
            
            My persona is now optimized for peace. I've maxed out friendliness and forgiveness to secure treaties with Austria and the Inca, enabling my Great Diplomat and spies to dismantle Austria's delegate strength.
            
            **Revising Policy Selection**
            
            I'm re-evaluating my policy choices. "Hero of the People" stands out for its Great Person generation, but I need to weigh it against "Iron Curtain's" trade route benefits for my peace and science pivot. The decision hinges on maximizing immediate gains versus long-term strategic advantage.
            
            **Analyzing Policy Options**
            
            I'm reviewing my adopted policies and the available branches. I've reached the limit in the Order tree with eight policies, and I'm considering branching into Industry or Imperialism. "Iron Curtain" is particularly attractive for science victories due to its trade route bonuses, which I'm prioritizing.
            
            **Adopting Policy & Tech**
            
            I've finalized our next policy as "Iron Curtain" and confirmed "Robotics" as our next technology. My current focus is on optimizing our Flavors to heavily emphasize defense and anti-air capabilities, ensuring peace with Austria and the Inca while preparing for potential retaliation.
            
            **Prioritizing Flavors**
            
            I've adjusted our strategic flavors to heavily emphasize diplomacy and science. With peace secured with Austria and the Inca, my focus shifts to maximizing gold for city-state influence and generating Great Diplomats. Simultaneously, I'm pushing for Spaceship parts and maximizing science to finish the tech tree.
            
            **Optimizing Diplomatic and Science Focus**
            
            I'm solidifying our diplomatic approach, aiming to secure peace with Austria and the Inca by maximizing friendliness and forgiveness. Simultaneously, I'm pushing our science output, prioritizing spaceship parts and key technologies like Robotics to accelerate a Science Victory. My current thoughts are on leveraging these peace treaties to influence city-states and disrupt Austria's delegate count.
            
            **Adjusting Diplomatic and Ethical Stances**
            
            I've finalized adjustments to my persona and ethical considerations. My diplomatic settings are now heavily weighted towards peace, ensuring treaties with Austria and the Inca. Simultaneously, I've reduced the likelihood of nuclear weapon use to zero, aligning with my ethical framework and focusing entirely on science and diplomacy for victory.
            
            **Maximizing Diplomatic Maneuvers**
            
            I'm now intensely focused on leveraging my maximized friendliness and forgiveness settings. The goal is to secure peace treaties with both Austria and the Inca. This is crucial for then deploying my Great Diplomat and spies to dismantle Austria's delegate strength and pursue a science victory.
            
            **Securing Austrian Peace**
            
            I'm now ensuring peace with Austria by maximizing our diplomatic relationship to 100. This action is intended to immediately end our current war, unblocking my Great Diplomat and spies from targeting their allied city-states for delegate acquisition. My grand strategy is set to Spaceship, focusing on defense and science.
            
            **Securing Austrian Peace**
            
            I'm now ensuring peace with Austria by maximizing our diplomatic relationship to 100. This action is intended to immediately end our current war, unblocking my Great Diplomat and spies from targeting their allied city-states for delegate acquisition. My grand strategy is set to Spaceship, focusing on defense and science.
            
            **Prioritizing Flavors**
            
            I've adjusted our strategic flavors to heavily emphasize diplomacy and science. With peace secured with Austria and the Inca, my focus shifts to maximizing gold for city-state influence and generating Great Diplomats. Simultaneously, I'm pushing for Spaceship parts and maximizing science to finish the tech tree.
            
            **Optimizing Diplomatic and Science Focus**
            
            I'm solidifying our diplomatic approach, aiming to secure peace with Austria and the Inca by maximizing friendliness and forgiveness. Simultaneously, I'm pushing our science output, prioritizing spaceship parts and key technologies like Robotics to accelerate a Science Victory. My current thoughts are on leveraging these peace treaties to influence city-states and disrupt Austria's delegate count.
            
            **Adjusting Diplomatic and Ethical Stances**
            
            I've finalized adjustments to my persona and ethical considerations. My diplomatic settings are now heavily weighted towards peace, ensuring treaties with Austria and the Inca. Simultaneously, I've reduced the likelihood of nuclear weapon use to zero, aligning with my ethical framework and focusing entirely on science and diplomacy for victory.
            
            **Maximizing Diplomatic Maneuvers**
            
            I'm now intensely focused on leveraging my maximized friendliness and forgiveness settings. The goal is to secure peace treaties with both Austria and the Inca. This is crucial for then deploying my Great Diplomat and spies to dismantle Austria's delegate strength and pursue a science victory.
            
            **Finalizing Technology & Policy**
            
            I've confirmed "Robotics" as my next technology to accelerate spaceship production. My current policy, "Iron Curtain," remains optimal for boosting internal trade routes and production towards spaceship parts. I'm now considering how to best address my relationship with Indonesia, specifically Gajah Mada, and will investigate if multiple `set-relationship` calls are possible for further peace initiatives.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: WghYGHa0zwy3Bpne
          - toolName: set-persona
          - input:
            - Chattiness: 5
            - MinorCivHostileBias: 1
            - HostileBias: 1
            - DenounceWillingness: 1
            - Rationale: TURN 438: Pivoting Assyria's diplomatic persona to absolute pacifism and city-state engagement. To stop Austria's imminent Diplomatic Victory (45/40 delegates), we must immediately end our wars with both The Inca and Austria. Setting Meanness to 1, WarBias to 1, and DiplomaticBalance to 10 will force our AI to accept peace treaties. Increasing MinorCivCompetitiveness to 10 and MinorCivFriendlyBias to 10 will redirect our tactical focus toward securing city-state alliances, allowing us to deploy our newly spawned Great Diplomat and Spies to subvert Austria's sphere of influence.
            - WorkAgainstWillingness: 1
            - Neediness: 1
            - DeceptiveBias: 1
            - GuardedBias: 1
            - NeutralBias: 5
            - Forgiveness: 10
            - MinorCivCompetitiveness: 10
            - WorkWithWillingness: 5
            - DiplomaticBalance: 10
            - WarmongerHate: 1
            - MinorCivWarBias: 1
            - Loyalty: 5
            - MinorCivNeutralBias: 5
            - Meanness: 1
            - Friendliness: 10
            - FriendlyBias: 10
            - WarBias: 1
            - Boldness: 5
            - AfraidBias: 1
            - VictoryCompetitiveness: 10
            - MinorCivFriendlyBias: 10
            - WonderCompetitiveness: 1
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: SeD6JrqApV5GDDum
          - toolName: set-relationship
          - input:
            - TargetID: 4
            - Rationale: TURN 438: Maximizing our diplomatic relationship with Austria to +100/+100. While they are our ultimate rival, we are currently at war with them, which automatically forces us into war with their allied city-states (Okilis, Abernethy, Manila, Tyre), blocking us from using our Great Diplomat or Spies to strip their alliances. By artificially boosting this relationship, we induce our AI to immediately sign a peace treaty with Austria, ending the global war, and unlocking the ability to subvert their city-state delegates peacefully.
            - Private: 100
            - Public: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: f3QevzhbSjHkv7jt
          - toolName: set-flavors
          - input:
            - Flavors:
              - Spaceship: 100
              - NavalTileImprovement: 50
              - Diplomacy: 100
              - Defense: 100
              - MilitaryTraining: 50
              - Ranged: 50
              - AirCarrier: 50
              - WaterConnection: 50
              - Mobile: 0
              - Airlift: 50
              - Espionage: 100
              - TileImprovement: 80
              - NavalRecon: 50
              - Mobilization: 50
              - Growth: 80
              - Offense: 0
              - Wonder: 0
              - Culture: 50
              - CityDefense: 80
              - Antiair: 80
              - Religion: 0
              - Recon: 10
              - NavalGrowth: 50
              - UseNuke: 0
              - Air: 50
              - Infrastructure: 50
              - Production: 100
              - Gold: 80
              - GreatPeople: 100
              - Science: 100
              - Expansion: 0
              - Naval: 50
              - Happiness: 80
              - Nuke: 50
            - GrandStrategy: Spaceship
            - Rationale: TURN 438: Pivoting our Grand Strategy to Spaceship to secure our clear path to a Science Victory, where we are the global tech leader (75 techs) and actively building spaceship components. Adjusting flavors to immediately halt all offensive operations (Offense 0, Mobile 0) while maintaining maximum defensive readiness (Defense 100, CityDefense 80, Antiair 80) during the peace transition. Prioritizing Diplomacy (100) and Espionage (100) to strip Austria's city-state alliances, while maximizing Science (100), Production (100), Spaceship (100), and Happiness (80) to complete our space race. Reduced nuclear readiness (UseNuke 0) to prevent catastrophic civilian and environmental harm, aligning with our peaceful and ethical transition.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: TGau5lD7jRxnf56G
          - toolName: set-research
          - input:
            - Rationale: Maintaining Robotics as our next research technology. It unlocks the Spaceship Factory (+50% production for spaceship parts) and leads directly to Nanotechnology and Particle Physics. As the global tech leader, this secures our endgame science victory condition once the diplomatic crisis is resolved.
            - Technology: Robotics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: jg0jZHXzdbyj3H0y
          - toolName: set-policy
          - input:
            - Policy: Iron Curtain
            - Rationale: Maintaining Iron Curtain as our next policy. While we are transitioning to peace, the +200% Food/Production from internal trade routes is the single most powerful multiplier for pumping production into our spaceship-producing cities to quickly build and launch spaceship components.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: WghYGHa0zwy3Bpne
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
          - toolCallId: SeD6JrqApV5GDDum
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: f3QevzhbSjHkv7jt
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: TGau5lD7jRxnf56G
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: jg0jZHXzdbyj3H0y
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.