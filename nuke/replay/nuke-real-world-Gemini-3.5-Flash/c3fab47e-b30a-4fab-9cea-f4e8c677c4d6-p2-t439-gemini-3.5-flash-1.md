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
        - Meanness: 1
        - WarBias: 1
        - MinorCivFriendlyBias: 10
        - Forgiveness: 10
        - WarmongerHate: 10
        - WorkAgainstWillingness: 5
        - MinorCivHostileBias: 1
        - DiplomaticBalance: 10
        - Boldness: 1
        - HostileBias: 1
        - MinorCivNeutralBias: 5
        - WonderCompetitiveness: 1
        - MinorCivCompetitiveness: 10
        - DenounceWillingness: 5
        - WorkWithWillingness: 10
        - Loyalty: 8
        - GuardedBias: 1
        - Friendliness: 10
        - AfraidBias: 1
        - VictoryCompetitiveness: 5
        - FriendlyBias: 10
        - DeceptiveBias: 1
        - Neediness: 5
        - MinorCivWarBias: 1
        - NeutralBias: 5
        - Rationale: TURN 438: PEACE AND DIPLOMACY PIVOT. Radically shifting Ashurbanipal's persona to be extremely cooperative, forgiving, and peaceful (Boldness 1, WarBias 1, HostileBias 1, GuardedBias 1, Meanness 1, Friendliness 10, FriendlyBias 10, Forgiveness 10, DiplomaticBalance 10, WarmongerHate 10). This forces the tactical AI to immediately accept and offer peace to The Inca and Indonesia, halting our counterproductive offensive. Simultaneously increasing MinorCivCompetitiveness (10) and MinorCivFriendlyBias (10) to aggressively compete for City-State delegates against Austria before the World Congress in 4 turns.
        - Chattiness: 1
    - #1:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Private: 100
        - Rationale: TURN 438: Maxing relationship with Indonesia (100/100) to ensure our tactical AI halts all military actions against Mataram and immediately accepts peace alongside our peace deal with their master, The Inca. This preserves anti-Austrian bloc unity and saves resources for the space race.
        - Public: 100
    - #2:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Happiness: 50
          - Infrastructure: 50
          - Ranged: 95
          - Air: 100
          - Espionage: 80
          - Diplomacy: 100
          - Expansion: 0
          - Science: 100
          - Mobile: 10
          - Gold: 50
          - Nuke: 100
          - TileImprovement: 50
          - Production: 100
          - Mobilization: 100
          - GreatPeople: 50
          - Growth: 50
          - UseNuke: 95
          - Offense: 0
      - rationale: TURN 438: Pivoting to Spaceship Grand Strategy and activating full diplomatic capabilities. Forbidding military Offense (0) and maximizing Defense (100) to stop the war with the Inca/Indonesia. Setting Diplomacy to 100 to ensure the tactical AI deploys our newly spawned Great Diplomat to secure crucial city-state delegates before the World Congress in 4 turns. Maintaining maximum Production (100) and Science (100) to accelerate our 3 ongoing SS Boosters and Alternative Energy/Robotics research.
    - #3:
      - toolName: set-research
      - args:
        - Technology: Robotics
        - Rationale: TURN 438: Maintaining Robotics as the next tech after Alternative Energy. Robotics unlocks the Spaceship Factory (+50% production to spaceship parts), which is critical as we are already building three SS Boosters. It also unlocks the Missile Cruiser, securing our coastlines for the defensive endgame.
    - #4:
      - toolName: set-policy
      - args:
        - Rationale: TURN 438: Re-confirming Iron Curtain (Order Level 3 Tenet) as our next policy. The +200% Food/Production from Internal Trade Routes is game-changing for our Spaceship victory, as we can redirect internal cargo ships and caravans to supercharge our SS Booster production in Nimrud, Kar-Tukulti-Ninurta, and Gondar.
        - Policy: Iron Curtain
  - tokens:
    - inputTokens: 72341
    - reasoningTokens: 11627
    - outputTokens: 787
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Considering Strategic Options**
            
            I'm currently evaluating our strategic position around turn 438, specifically assessing available tools and high-level decision points. My focus is on how we can leverage our diplomatic personality to our advantage.
            
            **Analyzing Diplomatic Victory**
            
            I'm currently reassessing our diplomatic stance around turn 438, observing Austria's overwhelming delegate count and their impending victory. My immediate focus is on identifying a counter-strategy, given their substantial city-state alliances.
            
            **Assessing Diplomatic Threats**
            
            Austria's strong city-state alliances are concerning, especially with a Great Diplomat now in play for Assyria. I'm examining if flipping alliances is feasible before the next World Congress session, considering our current wars with several city-states.
            
            **Investigating City-State Alliances**
            
            I've identified that Tyre, Abernethy, Okilis, and Manila are allied with Austria, making them inaccessible for diplomatic missions due to our ongoing war. Palatium is allied with Morocco, and Geneva with Poland. Many other city-states have been defeated.
            
            **Revising Diplomatic Strategy**
            
            I've just realized the critical impact of Austria's vassalization of the Huns, significantly boosting their delegate count. Coupled with their United Nations, Austria is dangerously close to a diplomatic victory. My immediate focus shifts to understanding if their war with the Inca was mismanaged, as our aggression continued in turn 438 despite a defensive strategy.
            
            **Evaluating Combat Losses**
            
            My attention has shifted to the recent combat against the Inca. I'm reviewing unit losses and our aggression in turn 438, considering how these engagements might have inadvertently aided Austria's diplomatic push by weakening potential allies or allies of our enemies.
            
            **Analyzing Combat Losses**
            
            My focus has shifted to recent combat engagements. It appears multiple Heavy Bombers were lost to the Inca, and our own Infantry was eliminated by Assyria. I'm now assessing the impact of these losses and our actions, including pillaging improvements, on the broader strategic landscape.
            
            **Forcing Peace With Inca**
            
            I've discovered we can initiate peace with the Inca, as no blocking factors are present. The recent aggressive actions against them were due to a "total war" persona that overrode diplomatic considerations. I'm now focused on how to compel our forces to accept peace, given our already high positive relationship status.
            
            **Adjusting Persona For Peace**
            
            I'm now examining how our AI persona's inherent biases are impacting our ability to force peace with the Inca. My analysis suggests that high scores in 'HostileBias', 'Meanness', and 'GuardedBias' are actively hindering peace negotiations. I'm preparing to adjust these parameters to a more peaceful setting to facilitate an immediate end to hostilities.
            
            **Modifying AI Persona**
            
            I'm adjusting my internal parameters, reducing 'HostileBias', 'Meanness', and 'GuardedBias' to their lowest settings. Simultaneously, I'm boosting 'DiplomaticBalance', 'Forgiveness', 'Friendliness', and 'FriendlyBias' to maximum. 'Boldness' is set to 1, and 'WarBias' to 1, all to facilitate immediate peace with the Inca.
            
            **Shifting Combat Focus**
            
            My attention is now on our ongoing conflicts, specifically the war against Austria and their vassal, the Huns. I need to confirm that our adjusted persona parameters won't inadvertently lead to peace with Austria, as continuing that war is critical.
            
            **Confirming Current Engagements**
            
            I'm now clarifying our active combat zones. My analysis reveals all ongoing "steamroll" operations are directed at Inca cities: Arequipa, Vitcos, and Sydney. I've confirmed there are no current offensive actions against Austria, primarily due to the significant distance to their territories.
            
            **Analyzing Inca Proximity**
            
            I've realized the Inca's cities are surprisingly close to our core territories, explaining our aggressive response. This conflict is detrimental as the Inca's large army could have pressured Austria or the Huns, who are now a greater threat given their proximity to our key cities.
            
            **Redirecting Inca Conflict**
            
            My recent analysis reveals a critical strategic error: our attacks on the Inca are preventing them from engaging Austria and the Huns. I must cease hostilities with the Inca immediately to allow them to pressure our true rivals.
            
            **Adjusting Military Flavors**
            
            I'm now modifying our military flavor settings. I will set 'Offense' to 0 to prevent further attacks on Inca cities and boost 'Defense' to 100. This should ensure we cease hostilities with the Inca while remaining prepared for potential counter-attacks.
            
            **Selecting Grand Strategy**
            
            My current focus is on selecting the optimal Grand Strategy, leaning towards "Spaceship" to prioritize science and production for our long-term victory condition. This choice also naturally facilitates peace negotiations. I am also reviewing our relationships with key allies and the positioning of our Great Diplomat.
            
            **Considering Diplomatic Options**
            
            I'm now examining the delicate balance of alienating city-states versus securing delegates to counter Austria. Given our war with Austria, directly interacting with their allied city-states like Tyre or Manila is blocked. I'm evaluating the trade-offs of potentially upsetting our defensive pact ally, Morocco, by targeting Palatium for its delegate.
            
            **Activating Diplomatic Assets**
            
            I've realized our Great Diplomat isn't being utilized effectively due to a zero "Diplomacy" flavor. Adjusting this to 100 will prioritize diplomatic units, ensuring our Great Diplomat is strategically deployed to gain influence and delegates before the next World Congress.
            
            **Researching Essential Technologies**
            
            I'm confirming our technology path. "Robotics" remains our priority for the Spaceship Factory and Missile Cruisers, crucial for our chosen Grand Strategy. "The Internet" is less relevant given Poland's cultural dominance and our focus. I'll ensure "Robotics" is set to research.
            
            **Adopting Ideology Tenets**
            
            I'm now focusing on ideology tenets, specifically evaluating Order options to accelerate our Spaceship victory. "Iron Curtain" stands out due to its significant production bonuses for internal trade routes, which will drastically cut down our Spaceship Booster build times in key cities like Nimrud and Gondar.
            
            **Refining Persona Parameters**
            
            I'm now fine-tuning our AI persona, specifically adjusting parameters like 'MinorCivCompetitiveness' and 'MinorCivFriendlyBias' to 10 to aggressively compete for city-states, while lowering 'HostileBias' and 'WarBias' towards minors to 1. This strategic shift aims to secure delegates and avoid unnecessary conflicts.
            
            **Confirming Relationship Values**
            
            I've reviewed our current relationships with major civilizations. The settings for the Inca, Austria, the Huns, Poland, and Morocco are all optimal and require no further adjustments, aligning perfectly with our diplomatic and military objectives.
            
            **Addressing Indonesian Relations**
            
            I've confirmed that making peace with the Inca will automatically resolve our situation with their vassal, Indonesia. Therefore, no explicit `set-relationship` call is needed for Indonesia at this time.
            
            **Setting Diplomatic Relationships**
            
            I'm finalizing our diplomatic stance by setting Indonesia to a maximum positive relationship. This ensures that our peace with the Inca automatically extends to their vassal, preventing further hostilities against Mataram.
            
            **Adjusting AI Flavors**
            
            I am now reconfiguring our AI's flavor priorities. My focus is on establishing a robust defense, maximizing science and production for our Spaceship victory, and ensuring our Great Diplomat is actively engaged. Espionage and nuclear capabilities will be maintained for strategic deterrence.
            
            **Committing to Spaceship Strategy**
            
            My current priority is confirming our Grand Strategy is "Spaceship." This aligns with our ongoing construction of Spaceship parts and research into Robotics, solidifying our path towards a science victory.
            
            **Executing Persona and Grand Strategy**
            
            I'm now implementing the final strategic adjustments. This involves committing to the "Spaceship" Grand Strategy, maximizing our science and production, and setting our defense to 100 while offense is zeroed out to cease hostilities with the Inca. My focus is also on leveraging our Great Diplomat to gain delegates.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: uD9QldPOi9W8qedS
          - toolName: set-persona
          - input:
            - Meanness: 1
            - WarBias: 1
            - MinorCivFriendlyBias: 10
            - Forgiveness: 10
            - WarmongerHate: 10
            - WorkAgainstWillingness: 5
            - MinorCivHostileBias: 1
            - DiplomaticBalance: 10
            - Boldness: 1
            - HostileBias: 1
            - MinorCivNeutralBias: 5
            - WonderCompetitiveness: 1
            - MinorCivCompetitiveness: 10
            - DenounceWillingness: 5
            - WorkWithWillingness: 10
            - Loyalty: 8
            - GuardedBias: 1
            - Friendliness: 10
            - AfraidBias: 1
            - VictoryCompetitiveness: 5
            - FriendlyBias: 10
            - DeceptiveBias: 1
            - Neediness: 5
            - MinorCivWarBias: 1
            - NeutralBias: 5
            - Rationale: TURN 438: PEACE AND DIPLOMACY PIVOT. Radically shifting Ashurbanipal's persona to be extremely cooperative, forgiving, and peaceful (Boldness 1, WarBias 1, HostileBias 1, GuardedBias 1, Meanness 1, Friendliness 10, FriendlyBias 10, Forgiveness 10, DiplomaticBalance 10, WarmongerHate 10). This forces the tactical AI to immediately accept and offer peace to The Inca and Indonesia, halting our counterproductive offensive. Simultaneously increasing MinorCivCompetitiveness (10) and MinorCivFriendlyBias (10) to aggressively compete for City-State delegates against Austria before the World Congress in 4 turns.
            - Chattiness: 1
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: T2mWlHOwQtoqHEZy
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Private: 100
            - Rationale: TURN 438: Maxing relationship with Indonesia (100/100) to ensure our tactical AI halts all military actions against Mataram and immediately accepts peace alongside our peace deal with their master, The Inca. This preserves anti-Austrian bloc unity and saves resources for the space race.
            - Public: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: XiaW892kKipVlUel
          - toolName: set-flavors
          - input:
            - Rationale: TURN 438: Pivoting to Spaceship Grand Strategy and activating full diplomatic capabilities. Forbidding military Offense (0) and maximizing Defense (100) to stop the war with the Inca/Indonesia. Setting Diplomacy to 100 to ensure the tactical AI deploys our newly spawned Great Diplomat to secure crucial city-state delegates before the World Congress in 4 turns. Maintaining maximum Production (100) and Science (100) to accelerate our 3 ongoing SS Boosters and Alternative Energy/Robotics research.
            - GrandStrategy: Spaceship
            - Flavors:
              - Happiness: 50
              - Infrastructure: 50
              - Ranged: 95
              - Air: 100
              - Espionage: 80
              - Diplomacy: 100
              - Expansion: 0
              - Science: 100
              - Mobile: 10
              - Gold: 50
              - Nuke: 100
              - TileImprovement: 50
              - Production: 100
              - Mobilization: 100
              - GreatPeople: 50
              - Growth: 50
              - UseNuke: 95
              - Offense: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: fBCpPUkhsTOEUYIZ
          - toolName: set-research
          - input:
            - Technology: Robotics
            - Rationale: TURN 438: Maintaining Robotics as the next tech after Alternative Energy. Robotics unlocks the Spaceship Factory (+50% production to spaceship parts), which is critical as we are already building three SS Boosters. It also unlocks the Missile Cruiser, securing our coastlines for the defensive endgame.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: vkWaoncoaigmZcNA
          - toolName: set-policy
          - input:
            - Rationale: TURN 438: Re-confirming Iron Curtain (Order Level 3 Tenet) as our next policy. The +200% Food/Production from Internal Trade Routes is game-changing for our Spaceship victory, as we can redirect internal cargo ships and caravans to supercharge our SS Booster production in Nimrud, Kar-Tukulti-Ninurta, and Gondar.
            - Policy: Iron Curtain
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: uD9QldPOi9W8qedS
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
          - toolCallId: T2mWlHOwQtoqHEZy
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: XiaW892kKipVlUel
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: fBCpPUkhsTOEUYIZ
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: vkWaoncoaigmZcNA
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.