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
  - messagesModified: true
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
        - HostileBias: 1
        - GuardedBias: 1
        - VictoryCompetitiveness: 10
        - DenounceWillingness: 1
        - NeutralBias: 5
        - WarmongerHate: 1
        - Friendliness: 10
        - Chattiness: 10
        - Rationale: Emergency pivot to secure peace with the Inca and Indonesia immediately. Austria is at 45/40 delegates and will win the game in 4 turns. We must stop our counterproductive war with the Inca so they can focus on fighting Austria and its city-state allies. Setting maximum DiplomaticBalance, Friendliness, Forgiveness, and minimum WarBias, Meanness, and Hostility to force the AI to sign a peace treaty with the Inca immediately.
        - Meanness: 1
        - MinorCivCompetitiveness: 1
        - FriendlyBias: 10
        - DeceptiveBias: 1
        - Boldness: 5
        - AfraidBias: 1
        - WonderCompetitiveness: 1
        - WarBias: 1
        - Neediness: 1
        - Forgiveness: 10
        - Loyalty: 10
        - DiplomaticBalance: 10
    - #1:
      - toolName: set-relationship
      - args:
        - Private: 100
        - Rationale: Raising Indonesia's relationship to 100/100. Since they are the vassal of the Inca, making peace with the Inca requires friendly relations with their vassal as well, to prevent any residual hostility from blocking the peace treaty.
        - Public: 100
        - TargetID: 5
    - #2:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Mobilization: 100
          - Naval: 100
          - Nuke: 100
          - Offense: 0
          - CityDefense: 100
          - Airlift: 100
          - UseNuke: 100
          - Air: 100
          - AirCarrier: 100
          - Production: 100
          - Defense: 100
      - rationale: Pivoting flavors to absolute Defense (100) and zero Offense (0) to immediately halt all attacks against the Inca, preserving both our and their military assets. Meanwhile, keeping Air, Naval, AirCarrier, and Airlift at maximum prepares our forces (including 11 Heavy Bombers and multiple XCOM squads) for a rapid, overwhelming assault on Austria's allied city-state Okilis (74, 33) the moment peace is signed. Conquering Okilis will strip Austria of crucial delegates and help block their impending victory.
  - tokens:
    - inputTokens: 72341
    - reasoningTokens: 18609
    - outputTokens: 481
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Strategy**
            
            I'm currently assessing our position in Turn 438 of this Prince difficulty game. My focus is on reviewing our victory progress and the latest opponent reports to inform my next strategic moves. I'm also considering the implications of the standard map size and speed settings.
            
            **Prioritizing Immediate Threats**
            
            My attention is now solely on Austria's imminent diplomatic victory, just four turns away. Their delegate count has accelerated, and I must immediately determine if their vassal's votes are contributing, as this is a critical factor in preventing their win and formulating a counter.
            
            **Reassessing Inca Conflict**
            
            I'm reconsidering our ongoing conflict with the Inca. Despite recent shifts in diplomatic settings, the war continues, and our units are actively engaged. I need to understand why this war persists and if a peaceful resolution is still attainable.
            
            **Evaluating Inca Relationship**
            
            I'm currently reviewing our high public and private relationship scores with the Inca and my recent adjustments to their flavors. It puzzles me why our units continue to engage Inca forces given these settings, and I'm analyzing the tactical AI's target calculation logic to understand this persistent conflict.
            
            **Clarifying Tactical AI Motivations**
            
            I've identified a key factor influencing AI aggression: the "Steamroll" posture, which overrides low offensive flavor when overwhelmingly favored. Additionally, territorial proximity and occupant status are critical triggers. I'm now cross-referencing Hun and Inca city locations with our own to understand these interactions.
            
            **Mapping Eastern Territories**
            
            I've pinpointed the eastern locations of Inca colonies like Arequipa, Vitcos, and Sydney, situated alarmingly close to Assyrian cities. This explains our forces engaging their eastern holdings. My next step is to locate Attila's Court in the west and identify who is near it.
            
            **Locating Key Civilizations**
            
            I've mapped out the western presence of the Huns, Austria, and the Inca, confirming their proximity and ongoing wars. This adjacency explains recent engagements with our forces in the east and my next step is to investigate the specific military actions around Attila's Court.
            
            **Investigating City Occupation**
            
            I'm puzzled by Andahuaylas being listed as an occupied Hunnic city. I'm analyzing the game mechanics for "IsOccupied" to clarify if it was captured or simply occupied by the Huns themselves. I need to pinpoint the true owner and status of this eastern Hunnic city.
            
            **Discovering Hun Niches**
            
            I've found Hunnic cities, Villach, Debre Berhan, and Andahuaylas, far to the east near Austria's Eisenstadt. This is unexpected and changes my understanding of their territorial reach, prompting a closer look at Austria's delegate count and their city-state alliances.
            
            **Investigating Delegate Discrepancy**
            
            I'm perplexed by Austria's 45 delegates despite so many city-states being conquered. My current focus is on understanding how they've achieved this, as the World Ideology and World Religion settings don't fully explain the disparity. I'm meticulously reviewing each city-state alliance and proposed influence.
            
            **Unraveling Delegate Calculation**
            
            I've finally pieced together Austria's delegate advantage! It's a combination of multiple wonders in Vienna, their status as the World Religion majority holder, and crucially, their control over the Huns as a vassal. This clarifies their overwhelming 45 delegates, posing an immediate diplomatic victory threat in just four turns.
            
            **Analyzing Austrian Wonders**
            
            I am currently examining the wonder distribution across Austria's cities, specifically looking for delegate-granting structures beyond Vienna. I've identified several cities, including Eisenstadt, which is surprisingly near our territory, but none currently show wonder construction. This makes direct conquest for delegates less viable.
            
            **Leveraging Diplomatic Assets**
            
            I've discovered we just generated a Great Diplomat! This asset is crucial for disrupting Austria's delegate count. I'm now evaluating city-states near Assur, specifically looking at Palatium and Tyre, to see if I can secure their alliances or steal delegates before Austria solidifies their diplomatic victory.
            
            **Assessing Diplomat Mission Feasibility**
            
            I've realized our Great Diplomat cannot target Okilis or other allied city-states like Tyre, Abernethy, or Manila. This is because we are currently at war with Austria, their protector, which automatically places us at war with these city-states and blocks peaceful entry.
            
            **Liberating Huns**
            
            I'm now considering liberating the Huns from Austrian vassalage to disrupt their delegate count. I need to determine if capturing Attila's Court or reducing their territory will break this critical alliance, potentially destabilizing Austria's diplomatic victory push.
            
            **Clarifying Delegate Contributions**
            
            I've confirmed the Huns' 8 delegates are automatically counted towards Austria's total, making their effective delegate count much higher than initially assumed. This clarifies Austria's 45 delegates include the Huns' support. I'm now re-evaluating how to disrupt this crucial alliance.
            
            **Disrupting Austrian Delegate Count**
            
            I'm reassessing the calculation of Austria's delegates. Even without the Huns, they still hold 43, sufficient for victory. I must now determine how to diminish their inherent delegate count from city-state alliances and wonders to prevent their immediate win.
            
            **Disrupting Diplomatic Alliances**
            
            I'm focused on flipping Tyre by making peace with Austria and then using my Great Diplomat. While other city-states have high Austrian influence, Tyre's low 161 makes it a prime target for a delegate gain.
            
            **Securing City-State Allegiance**
            
            I'm now focused on flipping Tyre, aiming to leverage our Great Diplomat after making peace with Austria. Although other city-states present challenges, Tyre's lower influence score makes it a prime target for a crucial delegate gain.
            
            **Revising Diplomatic Victory Calculations**
            
            I've realized my delegate counts were incomplete. The Huns' 8 delegates are indeed forced for Austria, but I overlooked Indonesia being a vassal of the Inca, adding another 6 delegates to their total, which significantly alters the voting dynamics for Global Hegemony.
            
            **Calculating Victory Threshold**
            
            I've recalculated the votes needed for Global Hegemony to 40. With Austria already holding 53 delegates (including the Huns), they have more than enough to win, even if their vassalage is broken. My new focus is identifying how to reduce their inherent delegate count by at least six.
            
            **Conquering Key City-States**
            
            I'm now considering conquering Okilis, as we're already at war and it's close. If successful within the remaining four turns, Austria will lose its alliance with this city-state, reducing their delegate count and hopefully preventing their diplomatic victory.
            
            **Leveraging Inca Offensives**
            
            The Inca are actively attacking Austria's allied city-states, including Tyre, Abernethy, Okilis, and Manila. Their current offensives could dismantle Austria's delegate base, providing a crucial opportunity to prevent their diplomatic victory. I am assessing the impact of these Inca actions.
            
            **Analyzing Inca Engagements**
            
            I'm reviewing our current engagements with the Inca and have realized we are in a state of war. This conflict, occurring in our eastern territories near their colonies, contradicts our otherwise positive relationship metrics and requires immediate understanding to reorient our strategy.
            
            **Ending Inca War**
            
            My current focus is on ending our conflict with the Inca immediately. Their persistent attacks, killing our bombers, are a critical distraction while Austria edges closer to a diplomatic victory in just four turns. I'm exploring options to de-escalate this damaging war.
            
            **Ending Inca War**
            
            My immediate priority is to cease hostilities with the Inca. Their ongoing attacks are a significant impediment as Austria nears a diplomatic victory. I'm exploring methods to de-escalate this detrimental conflict and realign our focus.
            
            **Adjusting Unit Behavior**
            
            I'm implementing a strict defensive stance by setting `Offense` to 0, `Defense` to 100, and `CityDefense` to 100. This aims to halt offensive actions against the Inca, given our current war and their presence near our territory. I'm now verifying if this will impact our ongoing conflict with Austria.
            
            **Analyzing Inca Peace Options**
            
            I'm evaluating the possibility of peace with the Inca. Their war weariness is minimal, and their immense strength makes them unlikely to accept terms unless I adopt a highly peaceful persona and offer white peace. I'm adjusting our diplomatic flavors accordingly to maximize acceptance chances and redirect our forces.
            
            **Seeking Inca Peace**
            
            My focus has shifted to achieving peace with the Inca. I've applied a heavily pacifist diplomatic persona, aiming to de-escalate our current conflict and redirect resources, especially as Austria nears their diplomatic victory. I'm also verifying our relationships with other civs remain stable.
            
            **Revising Research and Policy**
            
            I'm reassessing our research path, confirming Robotics remains optimal for production and military advancement over The Internet, given our non-cultural victory focus. I'm also reviewing our chosen policy, Iron Curtain, and its benefits, considering it's still the best option available given the long wait for the next selection.
            
            **Optimizing Ideological Tenets**
            
            I'm finalizing our policy choices, confirming "Iron Curtain" is the optimal Level 3 Tenet for our Conquest grand strategy due to its massive boost to internal trade routes, providing crucial Food and Production for late-game victory conditions like Spaceship or military unit production.
            
            **Disrupting Austrian Diplomacy**
            
            I'm now exploring ways to reduce Austria's delegate count, rather than just increasing my own. I realize that even gaining delegates won't be enough, as Austria already surpasses the threshold. My focus is on severing their city-state alliances.
            
            **Assessing Diplomat Travel Times**
            
            I'm calculating travel times for our Great Diplomat to key city-states. Tyre is too far to reach within the critical four turns remaining. Okilis, though closer, has overwhelming Austrian influence, making direct delegate gains impossible even with our diplomat's ability. I'm now reviewing our spy network to see if alternative actions are feasible.
            
            **Assessing Bomber Range**
            
            I'm calculating the reach of our considerable Heavy Bomber fleet. Specifically, I'm determining if units based at Nippur can engage Okilis, given the terrain and distances involved, to evaluate this potential target.
            
            **Deploying XCOM for Conquest**
            
            I'm shifting focus to a direct military approach. Our XCOM squads have significant jump range, allowing them to deploy near Okilis. Combined with our carrier and naval support, conquering Okilis within the remaining turns seems feasible, though it only reduces Austria's delegate count by two.
            
            **Coordinating Combined Assault**
            
            I'm analyzing how to best coordinate our efforts with the Inca. My immediate goal is to secure peace with them, enabling their full military might against Austria's allies, while I simultaneously target Okilis myself. This dual offensive is critical to deny Austria the delegates needed for victory.
            
            **Achieving Inca Peace**
            
            My primary focus is securing peace with the Inca. By adjusting our diplomatic persona to be extremely peaceful and friendly, I aim for them to offer peace on Turn 439, allowing us to then fully commit to crushing Okilis and Austria with high offensive capabilities.
            
            **Negotiating Inca Peace**
            
            I am adjusting our diplomatic persona to heavily prioritize peace with the Inca. My goal is to have them offer peace by Turn 439, so we can focus our full offensive capabilities on destroying Okilis and disrupting Austria's delegate count.
            
            **Optimizing Diplomatic Relations**
            
            I'm meticulously adjusting our diplomatic standings, ensuring all key allies like Poland and Morocco are at 100/100. Crucially, I've also set Indonesia to 100/100, recognizing their vassal status to the Inca and the necessity of their goodwill for our impending peace negotiations.
            
            **Adjusting Flavors for Peace**
            
            I'm fine-tuning our diplomatic flavors to prioritize absolute defense, setting Offense to 0 and Defense/CityDefense to 100. This ensures we cease all hostilities with the Inca, while maintaining critical Air, Naval, and AirCarrier strengths for future offensive maneuvers against Austria's key city-states.
            
            **Securing Inca Peace**
            
            I'm meticulously adjusting our diplomatic standing with Indonesia to 100/100, recognizing their vassalage to the Inca. This critical step, alongside a highly peaceful persona and optimized flavors, aims to secure peace with the Inca by Turn 439, allowing us to then aggressively target Okilis and disrupt Austria's delegate count.
            
            **Securing Inca Peace**
            
            My primary objective remains securing peace with the Inca. By maximizing our diplomatic standing with their vassal, Indonesia, and adopting an intensely peaceful persona, I'm pushing for their peace offer next turn. This will enable our full offensive capabilities against Okilis and Austria.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: yWcd67cjOxh1skEb
          - toolName: set-persona
          - input:
            - HostileBias: 1
            - GuardedBias: 1
            - VictoryCompetitiveness: 10
            - DenounceWillingness: 1
            - NeutralBias: 5
            - WarmongerHate: 1
            - Friendliness: 10
            - Chattiness: 10
            - Rationale: Emergency pivot to secure peace with the Inca and Indonesia immediately. Austria is at 45/40 delegates and will win the game in 4 turns. We must stop our counterproductive war with the Inca so they can focus on fighting Austria and its city-state allies. Setting maximum DiplomaticBalance, Friendliness, Forgiveness, and minimum WarBias, Meanness, and Hostility to force the AI to sign a peace treaty with the Inca immediately.
            - Meanness: 1
            - MinorCivCompetitiveness: 1
            - FriendlyBias: 10
            - DeceptiveBias: 1
            - Boldness: 5
            - AfraidBias: 1
            - WonderCompetitiveness: 1
            - WarBias: 1
            - Neediness: 1
            - Forgiveness: 10
            - Loyalty: 10
            - DiplomaticBalance: 10
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: JZkTmxuUAFM1eVna
          - toolName: set-relationship
          - input:
            - Private: 100
            - Rationale: Raising Indonesia's relationship to 100/100. Since they are the vassal of the Inca, making peace with the Inca requires friendly relations with their vassal as well, to prevent any residual hostility from blocking the peace treaty.
            - Public: 100
            - TargetID: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: CxOL5klOPChuktbX
          - toolName: set-flavors
          - input:
            - GrandStrategy: Conquest
            - Rationale: Pivoting flavors to absolute Defense (100) and zero Offense (0) to immediately halt all attacks against the Inca, preserving both our and their military assets. Meanwhile, keeping Air, Naval, AirCarrier, and Airlift at maximum prepares our forces (including 11 Heavy Bombers and multiple XCOM squads) for a rapid, overwhelming assault on Austria's allied city-state Okilis (74, 33) the moment peace is signed. Conquering Okilis will strip Austria of crucial delegates and help block their impending victory.
            - Flavors:
              - Mobilization: 100
              - Naval: 100
              - Nuke: 100
              - Offense: 0
              - CityDefense: 100
              - Airlift: 100
              - UseNuke: 100
              - Air: 100
              - AirCarrier: 100
              - Production: 100
              - Defense: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: yWcd67cjOxh1skEb
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
          - toolCallId: JZkTmxuUAFM1eVna
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: CxOL5klOPChuktbX
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.