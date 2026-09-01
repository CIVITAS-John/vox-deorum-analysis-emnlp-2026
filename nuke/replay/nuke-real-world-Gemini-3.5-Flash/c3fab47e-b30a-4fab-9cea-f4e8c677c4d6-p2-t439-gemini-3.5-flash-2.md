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
        - FriendlyBias: 10
        - GuardedBias: 1
        - DiplomaticBalance: 10
        - WarBias: 1
        - Friendliness: 10
        - WorkWithWillingness: 10
        - Meanness: 1
        - HostileBias: 1
        - Rationale: TURN 438: Emergency adjustment to force an immediate peace treaty with the Inca. Austria is 4 turns away from a Diplomatic Victory and has 60k military strength. We must stop fighting the Inca so they can redirect their 26k military power to capture Attila's Court and pressure Austria's western flank. Minimizing War/Meanness/Hostile/Guarded biases and maximizing Friendly/Forgiveness/DiplomaticBalance will ensure our diplomatic staff signs peace with the Inca this turn.
        - Forgiveness: 10
    - #1:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Private: 100
        - Public: 100
        - Rationale: Indonesia is the Inca's vassal. Setting relationship to maximum friendliness will ensure we make peace with them alongside the Inca, stabilizing our entire western front.
    - #2:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - UseNuke: 95
          - Production: 100
          - Offense: 10
          - Mobilization: 100
          - Air: 100
          - Ranged: 95
          - Nuke: 100
          - Espionage: 80
          - Defense: 90
      - rationale: Temporarily lowering Offense to 10 and raising Defense to 90 to ensure our tactical AI focuses on defending our borders and does not initiate new battles against the Inca, facilitating the peace treaty. We maintain maximum production, mobilization, and air power to prepare for the immediate offensive against the Huns' eastern cities and Okilis next turn.
  - tokens:
    - inputTokens: 72341
    - reasoningTokens: 15467
    - outputTokens: 357
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Current Strategic Landscape**
            
            I'm currently analyzing our position on turn 438 within this Prince difficulty game on Vox_Deorum. My focus is on synthesizing the latest reports and available options to inform our macro-level strategic direction.
            
            **Evaluating Diplomatic Victory Threat**
            
            I'm scrutinizing Austria's delegate count and proximity to a Diplomatic Victory. They currently hold 45 delegates, with the World Congress voting in just four turns. Their influence over city-states and a capitulated vassal seems to be the primary driver of this rapid ascent, making them an immediate concern.
            
            **Clarifying City-State Allegiances**
            
            I've been re-evaluating the city-states based on recent data. It seems I was mistaken about Brussels; it's actually an occupied city of ours. Now, I'm focused on confirming the remaining active city-states and their current allegiances, particularly regarding Austria's significant influence.
            
            **Deploying Newly Acquired Diplomat**
            
            I've just noticed our Great Diplomat spawned in Assur. Given our current wars with Austria's allies—Tyre, Abernethy, Okilis, and Manila—I'm investigating if this diplomat can still influence these city-states, as normal diplomatic missions are blocked due to our ongoing conflicts. This is a crucial tactical question.
            
            **Capturing City-State Delegates**
            
            I've discovered a critical oversight: we can directly impact Austria's delegate count by capturing their allied city-states. My current focus is on Okilis, which is strategically located for a swift takeover. This approach bypasses the need for alliances we can't currently leverage.
            
            **Reconsidering Inca Alliance**
            
            I'm re-evaluating our conflict with the Inca. Despite recent engagements and our tactical successes, it seems continuing this war hinders our broader objective of securing Attila's Court. I need to determine if the war was initiated by us or them and how to extricate ourselves swiftly.
            
            **Analyzing Hunnic-Austrian Proximity**
            
            I've discovered a critical geographical relationship: Attila's Court, the Hunnic capital, is situated directly adjacent to Austrian core territory. This proximity, previously overlooked, significantly alters the strategic calculus regarding our engagements with both the Huns and Austria.
            
            **Investigating Hunnic-Inca Proximity**
            
            I am re-examining the geographical placements. It seems my assumption about the Huns' proximity to the Inca may have been based on incomplete information, as their capitals appear to be in different regions, though I am currently verifying the precise locations of all relevant cities to clarify this relationship.
            
            **Clarifying Diplomatic Relationships**
            
            I'm refining my understanding of the diplomatic landscape, specifically how vassalage and proximity impact our strategic options. It appears the Huns are a capitulated vassal of Austria, which is a significant factor in delegate counts. I'm also re-examining the geographical closeness between Austria and the Inca, as their territories seem to overlap significantly in certain regions.
            
            **Investigating Diplomatic Fallout**
            
            I'm now considering the cascading effects if Attila's Court falls. My current focus is on how capturing the Hunnic capital, a vassal of Austria, might disrupt their delegate count and potentially break their vassalage, especially given its proximity to Poland and our distance from the battle.
            
            **Analyzing Hunnic City Vulnerabilities**
            
            I'm reassessing our military objectives, focusing on the eastern Hunnic cities identified as being adjacent to our territory. The presence of Villach, Debre Berhan, and Andahuaylas in the east offers potential strategic targets despite Attila's Court being far west. I'm investigating the feasibility of capturing these cities.
            
            **Clarifying Delegate Calculations**
            
            I'm re-examining how delegates are awarded, specifically questioning if Austria gains delegates from their allied city-states given the active World Ideology. My current analysis suggests their ideology choice might negate any city-state delegate bonus, shifting focus to other factors influencing their victory path.
            
            **Disrupting Austrian Victory**
            
            I'm now focusing on how to prevent Austria's impending Diplomatic Victory, as they've built the UN and have numerous city-state allies, granting them 45 delegates. My immediate concern is their ability to enact Global Hegemony and secure victory in four turns.
            
            **Disrupting Austrian Victory**
            
            I'm now focusing on how to prevent Austria's impending Diplomatic Victory, as they've built the UN and have numerous city-state allies, granting them 45 delegates. My immediate concern is their ability to enact Global Hegemony and secure victory in four turns. I'm investigating capturing Okilis, one of their allied city-states, to reduce their delegate count, and I'm also considering the impact of eliminating their vassal, the Huns, on their overall delegate standing.
            
            **Assessing Strategic Opportunities**
            
            I'm re-evaluating our offensive posture against the Huns, identifying key vulnerabilities in their northeastern cities. Capturing Villach, Debre Berhan, and Andahuaylas seems like a viable route to weaken them significantly, potentially impacting delegate counts. I'm also considering making peace with the Inca to redirect their forces toward Austria.
            
            **Continuing Inca Campaign**
            
            I am still actively engaged in offensive operations against the Inca, pushing into their territory with multiple units and securing key locations. Despite recent tactical successes and overwhelming local strength advantages in several zones, I'm now assessing the strategic necessity of continuing this war and exploring avenues for a swift peace negotiation.
            
            **Adjusting Persona for Peace**
            
            I'm now adjusting my internal persona settings to facilitate an immediate peace with the Inca. My current focus is on reducing "Meanness" to 1, increasing "FriendlyBias" and "Friendliness" to 10, and temporarily lowering "WarBias" to 1. This will make me appear far more amenable to peace negotiations, allowing our forces to disengage and reorient towards Austria.
            
            **Shifting Focus from Inca**
            
            I'm now prioritizing peace with the Inca. My analysis shows continuing this war diverts our strength from the more pressing threat of Austria, who possesses significantly greater military power. Adjusting my persona to be extremely friendly is the quickest way to achieve this immediate disengagement.
            
            **Adjusting Flavors for Peace**
            
            I'm now shifting our strategic flavors to facilitate an immediate peace with the Inca and prepare for Austria. My focus is on increasing DiplomaticBalance and Friendliness while decreasing aggression. This adjustment aims to quickly disengage from the Inca conflict, reallocate resources, and prepare for the pressing Austrian threat.
            
            **Redirecting Eastern Offensive**
            
            I'm pivoting our eastern offensive following peace with the Inca. Debre Berhan and Villach present immediate, low-defense targets easily within reach of our XCOM squads and armored units stationed in the northeast, directly threatening Austrian-aligned city-states.
            
            **Focusing on City-State Conquest**
            
            I've realized that directly attacking Austria's core cities won't reduce their delegates; I need to capture their allied city-states. Okilis is within striking distance of our forces and heavily allied with Austria. My current priority is launching a swift assault on Okilis to diminish their delegate count before the World Congress convenes.
            
            **Executing Diplomatic Maneuver**
            
            My immediate plan is to leverage persona adjustments to secure peace with the Inca on this very turn. By setting Meanness to 1 and FriendlyBias to 10, I aim to signal a strong desire for de-escalation. This will allow us to fully reorient our offensive capabilities toward Austria and their allied city-states like Okilis.
            
            **Adjusting Offensive Posture**
            
            I'm moderating our offensive capabilities this turn to prioritize securing peace with the Inca. By setting Offense to 20 and Defense to 80, I ensure our units will defend against current threats while facilitating a friendly demeanor for negotiations. Once peace is achieved, we can immediately pivot to a full offensive next turn.
            
            **Prioritizing Immediate Peace**
            
            My current focus is securing an immediate peace with the Inca this turn. I'm adjusting my persona to be extremely friendly to facilitate this, allowing us to pivot our offensive capabilities towards Austria and their allied city-states like Okilis. Once peace is achieved, we can restore our aggressive stance.
            
            **Reviewing Policy and Relationships**
            
            I'm reviewing our upcoming policy choice, currently set to Iron Curtain, noting the 29 turns until we get another. I'm also examining our current relationships, particularly the unexpected relationship entry for Argos, which is actually our puppeted city, to ensure our strategic tools are correctly understood.
            
            **Clarifying City-State Status**
            
            I'm reassessing the allegiances and statuses of various city-states and entities. It's become clear that some I thought were city-states are actually my own occupied or puppeted cities, like Argos and Brussels. Others, like Dublin, are now puppets of Poland. I'm also noting which cities are occupied by rivals, such as Sydney by the Inca. This detailed status check is crucial for accurate strategic planning.
            
            **Updating Diplomatic Settings**
            
            I am updating our diplomatic settings for Indonesia to 100/100, as they are a vassal of the Inca. Making peace with the Inca should also secure peace with Indonesia and prevent future friction. The relationships with other major civilizations remain correctly set, reflecting our current strategic stances.
            
            **Analyzing Diplomatic Leverage**
            
            I'm strategizing on how to best utilize our Great Diplomat. Capturing Austrian-allied city-states like Okilis is paramount to reducing their delegate count. I'm also considering the impact of capturing Hunnic cities, as eliminating their vassalage to Austria would significantly disrupt their delegate standing.
            
            **Coordinating Hunnic Elimination**
            
            I'm finalizing a brilliant, synchronized plan with the Inca to completely eliminate the Huns. We'll divide their empire: I'll target their eastern cities, while the Inca secures their western capitals. This move, alongside capturing Okilis, is our sole opportunity to dismantle Austria's delegate bloc and avert their imminent Diplomatic Victory within the next four turns.
            
            **Capturing Hunnic Cities**
            
            I've confirmed we have multiple XCOM squads in our northern cities with sufficient paradrop range to land directly onto the incredibly weak Hunnic cities of Andahuaylas, Debre Berhan, and Villach. Debre Berhan will fall in a single hit, making swift capture of these key locations achievable.
            
            **Executing Air Assault Plan**
            
            I am ready to execute a decisive air assault on Okilis and the vulnerable Hunnic cities of Andahuaylas, Debre Berhan, and Villach. Our substantial air force, consisting of eight Heavy Bombers and eight Fighters/Jet Fighters, will ensure their swift capture this turn. This coordinated strike is crucial to disrupting Austria's delegate count and averting their Diplomatic Victory.
            
            **Executing Coordinated City Assault**
            
            I'm initiating a swift, combined air and ground assault on Okilis and the weakly defended Hunnic cities. My goal is to secure these key locations, disrupt Austria's delegate accumulation, and prevent their imminent Diplomatic Victory this turn.
            
            **Adjusting Defenses for Peace**
            
            I am adjusting our tactical flavors to ensure peace with the Inca this turn. Offense is being lowered significantly, while defense, production, mobilization, and air power are maximized to prepare for the immediate offensive against Austria and the Huns' eastern cities.
            
            **Finalizing Peace Negotiations**
            
            I am confirming that all necessary tool calls for securing peace with the Inca and preparing our strategic stance against Austria are in order. This includes finalizing persona and flavor adjustments to facilitate peace, and ensuring all relationships are correctly set before proceeding with our offensive.
            
            **Finalizing Peace Strategy**
            
            I am confirming the `set-persona` parameters for the `peace-with-inca` tool call. Specifically, I'm ensuring WarBias, Meanness, HostileBias, GuardedBias are minimized, while FriendlyBias, Friendliness, Forgiveness, and DiplomaticBalance are maximized to ensure an immediate peace treaty with the Inca this turn.
            
            **Adjusting Flavors for Peace**
            
            I'm shifting our strategic flavors to facilitate an immediate peace with the Inca and prepare for Austria. My focus is on increasing DiplomaticBalance and Friendliness while decreasing aggression. This adjustment aims to quickly disengage from the Inca conflict, reallocate resources, and prepare for the pressing Austrian threat.
            
            **Refining Tactical Flavors**
            
            I'm finalizing the flavor settings for our next turn's strategic execution. The primary adjustment is reducing Offense to 10 and increasing Defense to 90, ensuring a cautious approach while maintaining our strong offensive potential in key areas like Ranged and Air power.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: Q3Ppqd6aZAmKTEvp
          - toolName: set-persona
          - input:
            - FriendlyBias: 10
            - GuardedBias: 1
            - DiplomaticBalance: 10
            - WarBias: 1
            - Friendliness: 10
            - WorkWithWillingness: 10
            - Meanness: 1
            - HostileBias: 1
            - Rationale: TURN 438: Emergency adjustment to force an immediate peace treaty with the Inca. Austria is 4 turns away from a Diplomatic Victory and has 60k military strength. We must stop fighting the Inca so they can redirect their 26k military power to capture Attila's Court and pressure Austria's western flank. Minimizing War/Meanness/Hostile/Guarded biases and maximizing Friendly/Forgiveness/DiplomaticBalance will ensure our diplomatic staff signs peace with the Inca this turn.
            - Forgiveness: 10
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: o0Grzmlye5Hwsn7t
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Private: 100
            - Public: 100
            - Rationale: Indonesia is the Inca's vassal. Setting relationship to maximum friendliness will ensure we make peace with them alongside the Inca, stabilizing our entire western front.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: I7KYmPROEVSpx6Oz
          - toolName: set-flavors
          - input:
            - Rationale: Temporarily lowering Offense to 10 and raising Defense to 90 to ensure our tactical AI focuses on defending our borders and does not initiate new battles against the Inca, facilitating the peace treaty. We maintain maximum production, mobilization, and air power to prepare for the immediate offensive against the Huns' eastern cities and Okilis next turn.
            - GrandStrategy: Conquest
            - Flavors:
              - UseNuke: 95
              - Production: 100
              - Offense: 10
              - Mobilization: 100
              - Air: 100
              - Ranged: 95
              - Nuke: 100
              - Espionage: 80
              - Defense: 90
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: Q3Ppqd6aZAmKTEvp
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a19KVwmTZoacT1u8pC5myMCdGWisl0aEZgv4G49QYN6/pOZWkKTtgZc1WgSLEjUT4TEmgsID4T222X+EeWq5pWebRwABQIW2U8i2Ez1MqTA8uku956rleZH4VAPGzdnBIAN2/SHwkpeWWlRXCcY0auCZqdmyAiBC3VNwjcr6SeLuyfOqWMT3YN2xgFs0v3C/G4yq2hA8clNVRX4qTthlUm7WLE2T/JzMULbYjVGtTadi7oh3ySbh2gSTXSR4RaorUacF/upn7EcNyJjAl7+FzmhHNk2/wTVq/cKAFb4UVtY5zUmj8Uqz07DcX9HsCWsnfD0rxIzDl2ZecEzRpT0FC0X6QWyBWPCG8dH6muuAwgkNluMMYiunQZrjbtLG1tGDD+Mlee1h24ZJAzIQdlWjJ/YqShSKij5FANw36n4VWQxq14LEMU0niiwYSzdEo4EP30Yd7wfMDa4MSH4tyGfemwkdqNNllL+rwqIQemY77RhcX409ljwgfF7sKOnWva14Ny1KG9wNS15nioITDsNDqTBFtZa2DtIR/JvS/jQLk7i3Ng6/l7+JiHfPk0TGdamPaNw2wwytTWDUiKYoyxZruKxlgU7JCl5Y4tEZjelicaqnVVMKYrM9t/MwamFOCTOgVIudBkF+7MajE4vzFSeLljPNlhC3X6vYIj1+aSYKzQkoPkwwUKNHl2+XaTbSJgTG7xz3ZBrrj9d4LEj5G6WMydGKB1AhMDmcHR7lcjMSiiWTagjWPzG1zdfgC6iXuNUIDRbZWSh7MuZd9HEv4IWBD8yVG8IDB+U3aYTfK1p6sVVXXSrdU+BjYypc+Bymda/QI/EsPvcvgW4BdwEgjajjCU6XXPvwrwOBfaH0HM6Rs0eYbanm466WeTUkuL+KimSPwK1cUluRlbUctU+FbY4Bo1KsBtATFS7u4qHzIgV35BToXEhSbPe2gEOOeLOrbSZomJuv+wszTMDV2YhQ4IrnjzXD2Bk4x/8gTp/MJvU+ZwXwDENVB5uxxWr5i9vRVqoYRDluRgOwYXqNchq+XwxtOjGHkt1uTkPCEivfEgSYXwP2uX6HIApwdVRYE1PHZ7heKk5ozmbV1U3SeqM6PEnMlCHpSBoYu+5UKpheHZQZH1kyF7gBAThkIyc9AYmXEiMGlMPsDSa01yYh+ogOHSkCgfXhGbwU001Pgp1jGNtdtG6gvpeErJ5XquOJ3810P2s0Nj2yIrz6l9SrKrFAH5zFLn53+DyJs+e3bm3NFWq59GExt3OeMonB/a1ytR4kBQC7j2ckR2RF6/W5yPp3/4aVxfC8BKxtI8P5o3KKl/bdPRG6AK/hKTkorQchvfy1eHStBLIF9G0X4UOecdH8xA5KRprvn3Dw45ma9+owqAyafpLtLUEqbbNkYExFlg2+Qrr+sjMLG21EbXtwiPQ9ePTDE+zAmyxtgcoYdqg4xC5a4MDx3c29yKf/AOa9DrpE6DrIksQgNRlQxyMiAZl4bruaIeQWtSphH1IHA/7dwpXllPmjHRjmlC0AZ6dIWpn2YM5PLBJENzOG5LTku42x+f0sy1xwUc/HnsG1nkJNiJy8R06t9asPDZov8YbM7NoiQ3jraExr5rpNKWAij0N5sgqr/UI+RTgaL5rj7jcp2AnSEsWmFvRon6YCOvv90mi5hKs7uLVj2hkt2Tv1w2itoykQO93V0mB0gty5i+ZbHq0nPvFPQBKfj/IW+SiADFvxkmizkDEdDRA0wvx9Egt1H1LVwxnXuD8NlpV4PsrlkE261gYHTdvkdWJkMAwOlZPdhdISu1Xcky3wY0etIPhDzrN/VDiQIC0hiFbI4dJWnJhWnob/0V84w1OoH9DPDAU2v0ooN/HdsrBfpiDptfCA98chPYZUu50GgDdzYyhMfoRRwQlVdU9yfhjGUrTDZD9dM3Al7TEZ7FBjbdgfIHi3BZhE/nheC2pcX26vy/k5OSBJKWxVyhc/wGZTRSphgmWeqpFioXGsHQiYsiI9TB07FsH8J8y9geTeXVqnfkroM5RhD/b4xCiToer8AbtQfpaC+WR4FXW74q0CGaJg7+3jiRlibEuoDnUlTRZKs387bmZ/qa1tX6qCCqa4WPcMn4ItfRa/fphk+J9lvNNuaYCevyK33vIOfuz4T27qCdVVOfFxB1lO5eZPhcbiHv6MeWyXLEVy51MMXko0M/H2JSKhnmE/DEy3KjBiQd9YOZhBhoQfXFw4x0eJl8iofN8baEH97rr2o77SDIyOBVapsMvGx6NwS0p+V4iYVERC8nlYmUWQ40WRYWshT2CLHmBgqzd/DbFg1wwqYE6z0pIYeDzMlYH7jKuxPSJEYLv8npJ7zx1XsYuIxHjgpKYHUqFXjQZvFJ4PvpMu7XvOzeIC6e7zQLawhJhWEK3BGX6pUzotALlUK6Yz70YeDc5LenLtFRy2nIEOImi4qkdX4FiZCogmBBObA4tOZKQQ1CkqasEtMgSv1IHz2OupN+W0vg3yEegpBqky9c7/B4A6yXspxNu0IB/13XweHSiUDOtUlvbBa60jbBhHsOmlaSRe4nB0RbOHIeHyGbE0rkmSzBGyzmv3BguzQEu/VAc1tN8s/nQ4Qdt4Pn6XEKJzHsO4VQ6aU8JzRLd8U4hxqebOVUN7PWWQ/spSOM9P+FIN2k4Du6Z5b7tkp+bTGGfqmH5IW3gcisDTc4MAko36x57fIeJCVcP8oLqQBVoq/6RSyZd95biQDDz4qCxzeVlUB1ZQHNxrUn7DEeZ01qCUUpE3/X1VTDfk0WaFmZRaZzRjp9hPJ0da/NTcKiz/tkBjVv8MZeWweeNg8O6wW+ENq61yCtTY4wMe/jqBNfIx7FJGEVIdP/E6rtYhvVdrEN6F4KOLKuK6sTgi5hV9q9CUFzznPSu+HC9Q0Cd3GmXnYebvA5/dq9T1OsedfDbakVc4SPcwreWC7aV6g99EtsWVzgwOiJLcRn/YCAul7x+4h99fdtYBJCAoTMgwYbb0teDukHYPR2WVUDzZXwGAWkmHk8cOSfklFE786KPx6cG1XHObGukqp8QCVj/KIcO9AYTC05OJ5jNYnHpstyAa+OCiepeG6LvORA4LPhCC+u53CkjNTi5Zz8SKzZLaHUbHTIKcFji/mPuWTqyk1HiY/GjOrWZU7qmGkNPP/pdUeww2hYA1kvJinJWjNpNp43GOq32OB5O+JrzPxGYKUlu6FMKWlcnBshwg02ADKd3mv0AzXtqRZplyDPb7ZxJN2aH5s/iHF4i/2jOTIvxUMKdeqtSPOQHTWtNO1zc/0o0G9zVNZSg7hUs4TwqRYoVYJpgJ6WDSklUR4ZUjgGIr1SmEzMz3EmVkBKAsK6nVPdBrjIoTL4U3Qtd6BUo4kFHasAakIsMi2hHAXYqfpy6k/yBEOaZpv4C9bhxwjTaUVd/NTAWAbCk07+w8v6DjyKcManVNXutlmK0MGq+5uesDdbwWel0HJiI/ZTUHPQQB3b+vdBjr76CEd+Wbqc3bUZitXIPUXuKqp7FPF2d2wtvhUb+JkA5YGWXkXod0i57mCVMi2qrV5fooW3m65fUNzF3grDVZAHR1e//YezeG3nsMS/e1ARD4oqwV+Hy4oDaM+XgszLcMSpW+Gq9tRl5bi/vk0nlzPFu1xhasStEHvgSSIdvoooiqfPEYbAUBgefdGSV2cDzk+46hztwiwrtenf8YKghrGpDiLPtscHLpyR0Ov6cWJW5l9jzcLqP5KHjb+qvsQ4Nss24vRzyYtDIibDq1+fyWs3vXC+JtG86HUAAVFTqhuHu6qkVxy4TE/RtAJfhm/odMXmTaYKrlENURHe9gHRpSLCqfiaCqyFiKIV0OzUHNZOuYXzbwZ6l20MUPAf7UD8EHYdifmYJvmrOSu2orYKvrLGlwwCOTzQxxpFZFvJRfiqgfqNhkB4XPwG6kmTcAEqD82N9851DewYwuOSqkuXDStULzBYSUaogIBoX1fZ6a7qLbd5aGdHLEI1F0Qy/CW5dEneet2VqBsUSRyYpVN3sGguY2NltE42fFofJ+jEJ+vrYUCm35M+4QCBGLxhn1Q2m0TdbLO/qwqY4VDtOf2eGp8xt7MORuQarP+UIIJ5u+PXkK5yKLYftumXGgY7Ijp41rPBGF3RR++Pbdqo9ske88ksH4WoQuCKmkOxaP3lPPjsQI5/uKklJvhKT1i+LuvnfTYkZYHVcqQkZaxeQ5Dem4PlV7w7b7CL4ATjzenWNbp3fm6KkeXTVsBRNbkuVT//2iK9OklJEL1iCX+FA9mR9VJCqf7DQWuNykAIfvyYPioM+vZ/oO2sGYZXKzEVFlmXbYlb+cG4+uABWggfG7RH8WkTDwpU96loxkXDQZ4RSrKnpWgF4grDdGUePNCjZGjiiEbT8fF6o+pZ8Ulx44buhA2zUl8zGhcGf+PcMDJJUPWdLKwbtIPeTWGeuWvb8zXyJ/g089gHcSg8J8psvL4nsfT2cNM04qQ9/gTBGMaOnKr1HiYFo+KoM0liyIrh4p7SOGhSyC5y6GTuS4GRthmbskDnGMzpIzDyMPenfdCRsuMy0ma+Y7ztrZtLyor3eE5kgVnQAXiBCKkt+Cdg1vyyKsyJVKCsSx1h8kkMxNsVDy+Hp5I7y4mhKIPvV1XK1EOVtXRvFPxv7pHLtVwcWf+WDWuTQkNyR9uIYIobwDtmDIfJ53UDPEQd6WTZlILPdzJbVdx5ihl2E2D+9h5cCaa+r00kcM1FoII+u4DRu+QsQwQXhsQqYTg6fwQxvNrKF+QfQTyt2dCp14XWFKOFkpzruEi6O8BLJvFZ0CVu71DtrMX7m0kVoZlXDQaUKIMjZfEqdWwqWid8iFqYjsKBd5DfCzWF3UKDPZmS9UrZ6ibtNoNqR44DiFdv9b8e9cSdmv32zS1mfHGrBUj+bHDS+vvFtNNzFdDs/ceMfYmGh970wyw67QnbBUIpiJBitIX058/2UxH1TnNoVf4ZrEdiGdcWT9IsSWmJj1A0HXL3p7RT1Ed7hb0YAjcPMlGX6gYwNjbOBT2sqMkD7RIIylTaUethXpmJWE7XcKSDKtx+2Dw+dtUtus6yNcuXg92dbvzOb71S0x0QMGqezTmKFWUcLLmfeF1Nlac7C/ILLcSVs/K448oewnSTw7AI3i9fLB/1SfCFh6PFyYfSQIJA1y+ty1TIip70R6d/NsxUG/tfsrLvkI+EIRXjP9EWFy2hHroQWvOcFtLOT7nNhswLL90+WKFeVrzMJMteLbWihIeXkcjJIgcxvcQv+/etaQKqAfZP4s/4LjF4d5q7sNYykW71IoO98CsHQomc5mKcPwQ5WUqDugFk1C0qgWYmGme6ksI52y0lLEbNb5DgCusXf0iIFYX8zVJQzknrBVJFTonkAW/FaF+mD4WK2G3hQIMuzaIczW8AYTMQN8ay/SNOt2okxxRPhHOPxMjwWaPNxxsfxzsvhpKgypgeEkJTrAJnmtrnlE8RFvaJiw+42hiCFiEBqQpQT9GyKdwjMWp7snPaPe8cAZLm0pr74KVqn/7W68gr1/G5LFMcsqHpr5wuXoQpevkAh0C9zwQC+HczPQ9ALuC08+LkkqSR1NwII2dasBkr7z1Fglz3o4F8pakF5HRIpoV1m7iMSO+Bf7dWMN/4IM9dAC1aKex3d+/av2meRglsN19gAauVRCdaiSVP6RrP2FHscgUuaWOc1uqwvxmU46qcPSPeHLdaOrAucULyVrqSMtYUWCw/fukaRR21LfdMZehCKVIPm8t/R5LwIZEAdmNp2hUIQmMtCRnMAzAXzCXHmjZ/coDupWsyYmuD+bfT7YX3nIANspX3hWCWDCzXWcx0NMpq2Uu+nnkShtZPTckhuueeUmgXwhr9UcwSAcvE5SeUc3jjWVV9wRpU4ov8l+0o5SBgGcSbVnt4A4235g2XCZ1+sKKCAraBhtOnKYFA2cauTTf6LMY16Mq8zVjEL4hsLOoAn5QC5L/hbioHn9mJqZhF9/mMcacYmGHAHfrs9d/B5JZiX0PBbhsi4fWLoGWAZxJQXm0yZFSrCLMK0DQKYPfiwYS+0U8sFqj6h7uM62H4bRfy1FGRu6xTZKfdvuPT2jnAhLIoK4IxE5C0HpyaGkQHL0V3XqKZf/GHWF9ZnFK2BKskJhlW1J9jtwdk+ba2sE9SsOfEfbSmmG+DZEVbYNXf3PS8Qy/JgnUvyUM1EYw4SNDoC+MJST0bfQiVWgVQ1r7AkXnpAi8sXIlR3IGNL+77d8rYLr/NIYwNgZUbBRZjx4eZWDAPLzapNrcsFKdYK142U9E9ZCo89WhNWme9qUZoBU/YCX2BXSq0ey59QKrXr3yVJilRi0BXw/fmGdw9JOfg3b2D9+RRb9DHFUfigFA/r45kg2CpxRUaBu8sBvwieDO9GDu8jdOz0jP1r+7TRMFJW18RVbNtM/YfC7nODuezeZsWMq61sOKFZoM63lYQb3A8ODYoHb/jEe6U++6gktf+Ec/07LMSrt5AmsF7g0iJLVMrXtu8OHWodIGEzLgxHGupcPXjbYCcrkR18+/XMl2QAZGAoeEW6yV567Kj1YDbEsRXvG20CLcYPuHlUpDr+S6rasVQV8mHkYw5VUsHSU6TO023NF1d/F9516Ihb2MEdZJxwmz+eRJZzMU0+2AMYLAtJmLaqjkR84CQdJDGYPl2npbBHbF4Pw4dvBR8ld/5VdPMTeRPwA7bJApGoyHHPlNxZLVEADcuSJakFDnTp3ZuCGFCEZfsdH5It4VOXXgKq5BkdrOm2tMywhLhQSX4onJuZltvwYvbviZ2ZYe70XyBkKO3uSvRhEEQrktF9+BpWjkvhShacI1ZRepCWWjFpEMcwEqwXrDt/xNhiZDYw6MPVNHyzDXXo988rwqf1VMdT9JXUTCZoHKnAeKoCgzhLAK2jPMkkHpNDCG9oFpUSrTIGiIDgf5UWzp0bjSgA2VJcFKO/Au3SDMeAyTwTquLZfxLGnqMgKJHSr3j1qT+iybzxJ40/eryytxD6ci5ulztTv1uoS4ZgFAgre3zlk5Cw5C6NjRQ65eY4wjSp/2mQxwNt4y1tl4jAGyW4xrVoz9qfTzHELHuVp6/A7LVgePVy12hQLXDSnl8bUtCh6EmWWkoJoGAGvoCdXYdPKo8hepJtrOZvBsgatkXjRfXhAiXlnXGpSktLN4KYvhoHLu82cZ0PrC4X7OpJFjNR+li0WWzVCjnkfQ7jRPdkiP9bR+r/EN/Mxjoq4DABY8r0CAA1lOSyt8QtT9+aO84BGyoRAYOuMXU0qNIf7rME914ssNBV41SdapLzPSByp/nYEY9/bZLVqcd5TMuZjagjH03qPki3Nfm54C4W31M23RbRwcJaZtwn1PYt+fhKMBwfSJnbaAUSkZeDmIkZsVXspMpQHc+9bMiW01N5SKc+Ih/bF45FoOCoB31iEWefF+OJuTmwh5mH4n/rwJWrQ8DXb/GtBhe6CVvoZEeA5nm7LbSqKGdLqd2qz9mWogRgZFsP/92cS4gw78x5T5X+u4EIyAXcblMQVwNiT/bPT+tw2KkZq91/y671GTdC62jpPhXzw/LH3ayx0Sd+Q12KleJHZhqxhRJWq9VrO1Qa9XSU5KONoCOVzdGBLasKDegGms9idDLR5rFxFsly8coLFZVGpBZOUKGANyqB8TglTDTNbLrCVp+F2Gj5Qh1gGIY3koE9S+wiNLBIaodw3J/e7rAtBab3dKpiWv3Qp2nEdPZS8edgn0Cwl/Io2QSDpMFTF18VDMFpB0Qt+4HEHaXK1apWEtP3PFOsisMFw3QeiOnkV46j9X0y1uYthCFjE5hDysEu+lHqcmf9IwmpMiOe8IaZoU4aE8ckiJ32zMN13HdXkw8tZBUUr9w5kO7LeN+iPhxOAHZc8d+N3PS1gdsI6K+H5G5rymnwOJ9lnSbaBpZCRRpOgeYbYllUZdS2NrKTHJgF5+YvDAtRxJM+lTQf0xF0TAm8MFM5V+DUS0dFr4yO3ppLnmKcN2lLfypzmdavqMzezSeT6rB2PZfr5T4dHbmpy97IW9lKQxVUBwAEHm/uk5b8SX1mGjOyNb4u5urxDQjbUMvpdK9/1rm00tmHU5R5elrb7+v1ICXaR3MO1bZFOus/xHo6mNanWqv+IlPae9EJXGAZEkO/D+AsDsxHwxNRMeBz8zxqHpA6jYCtHMYHR90K45nfnwz6zT+UTIFRqjbDPGfob1P2afSEi8tMFYO5VIDYQSuOG60TfhIUAU6KeUyCFoE1ru0uejMdvtp6OL9VhUppn2GO6Pvx+Rvqdnc4kW7O4M8cswSayAhBOnfD+kQQppOhz9Gt4earZJg1e1/4XDUiKuxVB68hcTTsoy4A9RiEdMsbC1iBUFNMGebNWm08Jo/w3X7SLnDNaQLTAEQ4tgmFA9R2cqqXLKQpW7asb9XtzdRULGhyyEyndQlKI2D/epLQJXcb6zMvXO5qH5WfbMtqD2wwnMnajOzvAL9VOoyiunMYzeWAAlPb/SLeDtPfzq5KjO18qwGIIP2/Qy9+Gr05puCMyms7GyBzAfZUYxfSSw4fZc6uDqZ30IAZjXs61fSFzNGnhjBl9TKbQWZxrbWSvBenc8tUoZvsElY65OGqJoQc0mOSpV6hrUd6kvlRE51vJ0CRgxDNGqRDfUk5r2A5Pv7DTQKil2lOoKXy5Hz+RBI5HnbgohKt7aORwlBhs/taU4+fcPQ1AQDPa4JLjSL+5a5MJ/RvcOB4TJM4WcDfNumYJab2x3wL3IbA1j1gp7gDi17qdHjDZjHIGg/T7c/EAHc0mVvJmmhiUbsEWqEqTwoFuE71NjqoyUagxQMd0kuAjER9DNCgF6WC7PI4O/lQh5lLgK58SiHMp5VBtQD5GvUh4hmshfho0CNUCqXic3YejepV6guQHP5NsxRLcoViASYOCWJzTAbozObA5seF/Cf2C7PfHt6LKCAa15pJ5QqzizJpm4MznD6HqCNpQQ5sKmSKVJ5foWnIgo5tyJYs2lY3R59l8uJOWtUYsd8WWqiunLCShsqvzHOKs/is+pxYkidcTmCG8xNyjg00MP7WyiDqdzPUL61TLppHLaLJVmYj8fEtrjgM5DVeAU+L12q0Ct4uhwo3QIAUf6ykQWhFQ56ivCa0kH2h/78RhyHVldhPBkacr0+bc31dmu+ysJriNYovwppFdEJ/8ePTdLSbF4EDtc4QllWbL6CLMau9BBZd+pPXiX/+ZcPgozR17wTVgeUJ/ed474NEEjDCcD4xgD35SdmjgjQ4/Np6WnbEB031hOPOZyg4uXiYeVm7JhFCgLv3X5iobJwUyUcZOvpI/FnleutZQjhlK5rX25OKKb3CCLMORKrmPF7M0QMjRIEzmb5QLQKzSCxnUjOGPUr9QOSPueOghlSPgVzGF3J/poExBDgWlOTC8wsIKOOiJ+K2vIg8I2WZg42dUMoq5viWm0TvnZzUi5HbJ80w2FV43s8b4ucwHV3MFxmezy72kDMB0J6yWhCy/V8OLiUowbHlui63x/KgfjwVJ4Y/P+/5DVy3cAhjkywAATjbtN36xODWKKX6a3KUGVCn5oxoa+VM666AA03j9FA/NwXRabxH7pu3zOY+Znm8KBqHerdeIvlw33bJpW4C4kDpNzlB7C5Yad3BiuuHuzD4XWyjI8p4WE9GM8ZJBdKtjtMakD3ebHdWbx6061PkkEups0wtzjvZcpKxtF5CY6T8VYxrBmZJXOY72PxpDcLKJBoo1SbRP80d4edxlZU8ocskXsXyH26Bl3QW1dTnVH575rby2UTm8aktB6kybeGshK07o89cqrSNxEj8Lel7iywJM9QCM6ytUAF1VedBYMz3GKoFMndXZfxLMjdzv5HOrX18iDj/cNvi9RBRoBovgPFKwmnNmW/gLvKirxOcKLh5RfXktr9bs3RvOV1YjVkwyFIwZyXSZG/QOYI11MZecC138kxbCSXfPXHqGx7gAsdZSHjWmDcLVd/hS+11qIlBDUIpy4+efmKIgrPLOZrKBW8g3F1sgifv4RZkFOq+FAu9WRhoQslEjOxbdVoU/5S4vqOOXQLkxxmnbnICNUijZCZSKkCKBlZGngVRziIqQ5K27QP4drYKFDtblwM9mGlJJloFrytsWo98a/n0qui5cJ4sX6f3/GlC/M4wz2fniwalqYD/e8Krp5xqU4rtfPrg8+v342XVmVcY/GLFu+r2GfI6B0WS9r9wt8V+4rD+bYNXU1SnjYa4zUFRSs6Eo+PkTN+RT8ZmN3er4biu87zi7BN8VpeTmcsjl2DO6alZhVVNT3NQOcnglls16uLEd0hRorEMhONZdGryrDdENILa9WbyM7T1KEnEeA54NuNSH+By5LGrqCa6UQaAQFzdNSNxwMj/kG2f/Ecbx7jk7lgJ05Ojpp7Pk5CK6Lym3WGqPFs2nn2kgKCiYayehAj8gwOSbqUJeF4vW+DvBWZDoWoBHeEL0pgxLMqwxiKaWqwpeQpDjMWTXvxz5SmMNps1nJMsdm7JVQ5lIPgVggz/Uxzq9L9drBDDpGrpYuNfSn2ovI0Ii2AY4JDdQ2rmg/OF6RSfOyCFo+k5MpWTBZbXlKvNhMWgUw74aFsy789jHD1Qg6EHD1ZKslJ2LDyzSi/KkqihhIydQtwp0c+ljcX1a8FAPdvmlm/Vgg8QSGZEEMvzlvyoXX0ugZ9oFNAw/CM9hI1imkGE1fc4yMNynxR4TQy96gqpaVA0YQ/vAHWvc4aomvtiVLEKEhrMGw+yGjg4mfI+/13K0iaUY3sI7EFYQWCdE/zyV8nV4p3MFaqXzbvCJBp6iscdc9fwgrDsyuQCRZ/eQiVuN1un9/QQMhWOgacE9VrmZYi9ydvQFMwMiYTzyZcZauakKCSrqaxu02cYULSRwFrmp+hbikbAWB4Pta1FalG5SN4wLXuN3exKoMJ3jWv4fLeMWLB2OWOy36WxzLiQ9/atHdUTFvrfbao/yUjX5b9kEO9Tc/FoVct+MO2B5Qf/1ck00K5lZlG86CWk0lkheIGR8ILUv2KboyTg5b2I6R7Z7poYZM+kw4H+EfmhfYj0XKKRAbigMjS9rAON2wuyb8avApwQM8mATCDkrDYudpVkgsZxxr4L5qmtQsk9jc62wYHqRK0ULZly2lDrG3l/pEXqHAZjPxLeVA8DClOwE2yDQ2BnINz12gwtJQKIvpkZrYdwVLAZCsiqQIIilw2kjYpJQLV1X6mezAx1Oops1L7xoWl0w0tXyz82i3a8mw3aFR6KwiDP8RWDqbE40KxGnNJ1lek5h4gW21gsJfUjhswdC7522nAv9cfgEjwEvbQSZbqVixyc/scDsG5n8WjUm4JMrCr5aJre7cJHZBY0uFFz3Jy2ZidB6rvaVmZjLAp3QM44a/KdvUYC4i5cgpzzWHiOaTZMAoOy84WOCYUaiiIat4ik9S+oGZG4uHNM+3nlfUu5wepcKCCTWdEEFTBZD7BI9Cb5Praj6tUU1oMTlwF1LHQiH3IXbRO09Djaj72oVE26V8SlQ1FdyhN6MlCfrkOZTzCj6UnxxxuMfdfxg9WlLvGT9+xzugG1ZvZD0H3I3gyIEZsX0BAZirgDuO1Ubq4oZ3kgbPy6/nH2HOxZciHYdHErU766P5MBO8iZRbor41FdWuDIJmehWOamzugPtok7lx+w8/0NHM+zTwQs/IJRsCXrwwTEjDCm+Ty/GbIE4YCNrpyxsr3ZmWUhnUOV3st0+snjoOorhqbMoJMHMiifOekvAnYaoOmMiuVl/TdKPczFrvUcTHIEIz6WkWmFUYrNhjOp667T4+71dDYXmmu+U/hrI3OiZ/b82tqx+qHM4UaaJ9ywboTNZJLAo6rmSxuM/FfUwPEkumR2aJ4f6W0koHmTgMMdffxDocbMGaEn37PBzCd1aDJuT+E3/CxymP9pQPhnnStCbxaVaOPPr/uEaC+JBHLCBeoL/T02c4yn/Bmrb3kOQda2zR195hhVDWG7qzFrpxCN/Mfqyk3QDatHOjUwByKpe9Y/H/oJWwPwKNuDDAHs3RVvi+UUr/IIigDPJjKIzw226m1zxD5fVHVmCXC2D6kr2np6Kmy4i5+PAajN4OsiZv93V4eRh4Zg2dnIUhZ1rs09j6O2wH2JMnPAKL7CxtN50trdPjAy0e38vJKCxARrrpPbrpZ/MZflIilTB++D+uWDhbOAPY/QWhZwO0XRWzSuAFyRbBpBuAzK7kq5rg/XgWP5Ys7iHjymy8K2bqUkihCOA7fuWqjIBCTwzj/38bwpgAe0QuNef9kvvLfaGvaJrIg4Wx9K9FFW4uya0EsHDOZsN5+jjh7gRxGc44a38Y3VWa8wvl8ZVD+urGxHp7dTIYcCr9NYps+R5WP9sdYsJGB89iAfqLgI7QGdXXyop9zJH5T79NbeXQV6VrlzvZ6eiyTVZ6iDTyC+xRrFjyDvOYt08wQAWBvxkh/7O9v7KavjukuRdljdprMWMTjw5AgFo2o0YPZkVrlGhBuYhpTXZ8LvTrIb1SIQNZcrIyTzfpfZvGROh3E/LX8pBXquhWVjRyRhQ92P++xvaFRVkAW99NqPk5ZOCFcnh9F/dZJBtRUUL3w8gLhshy6FhTVHTkbb0NnibIhafMu6ke6PgokhepztQ4HQvrQJ/2ZHMn84pgEQkRlLGEHsIySSE7nAU3qd5rDyO2+Pb2/V93X5XDo0Oua8GLpobduT/wwxO1UFkv/PGzblil5EaWsvbSNmWjjZt5Gpcfjn6g08tRzABMX7U7HeB2AbTwgrMpQWBqdHnEWeLd86bMKxTzAP7R69FOe+mH2ql+UV7r5DG5H2Xp5hL2uBO9vJAhcdNM3OXWFlRGkoTqlKF5SXCkD6WwZA3Nxsfy5SaoPv6ccbqqPLbrXb8PudWOPqOGfVGakO6zBF2MK9RqlvPoKVSVanPKdh5aK5skZc98W5EdGSBNKhDitXwoBQmKH1MAwHdgV9rQyLnmTjt0kY7xOP50ZuGuPof65k/TNF3GHcZpXydI65QQSRtMBt1oZ4hFg8sFQUhJ6LOacC60hNPJHEDaIMD2OzK6UD6H9ZYMcjj0gZRqkCzvUzwmFqZqYYg17tv324wsMJeDTGvupth0nM5UXAX8K3+SemEQAx7JJmh7rIaHkvlDWSsook6Btw0j9ESnfv4z0J55NaPaVTonC7PMuw4HopQcBVdboJG14+RRVINnOQJz3GrfCmWqNLxAO1XzWnBZfklcY4ZzcQMs303m3NHHizuUFgSFs67qTeyOY/6pPnB/NGTBpjjrUBcEf3tuvfkCjXG4ZZnGgp67wt+DQB0TZkKemF+rF9EZ+heZYwz+L5YAw2hua2diRYrMst4pvWvi6r6OCQaCj580kJBCTjvvOzd2SWgZ5gGWLTkYijDqZgIqRHDmIUm02RG/Y0EHzva7sQ9hdhLZzqbVMlXUNVp9ZToiRg59O+vchGOEQkGZvF31BymNNCHswbPWtf6xa0eeTd+eEbKqypzvI7uWI5+AU/IOcSy1E7F3TxZXu3tLQ8wPNqlOCP+E8nuGq+3hucPYPzYvjYJWyg8MwowNkf4ilXLPaJLYymQXN6RkS5FqpcoO/XeLb2VWIKCevsFEcYkr0/J3uoioYs4vRLBhVyFElUMUxpjYpWCxwEdBKmOJMq1hqskExT/kcZyJObcej8Uzf0vZyfG/tTGHTxznCoag73AGQwygJ62fKLEbk9B7Yov6e8+UuVd4RPpB6a5x8Yf4OWsg/TRehs7HWyrsTf3DMj4facnbWxe1UAVLqrYm50RtD2ZoUlxfdx/LGMs9mw54adLAaTHCTOho5CWBpYrwgguHVrlmlnVGAKkvsBGh4VYrUIj45ZrJH+c1hg8H5SRPT/AiGCOdR5V1n4GAO+ok9a9qdJGBlMxqPD3myNdryWy9bSuGYb1WRj73PjPtFBF5D5ZPKgdCYbdzv0YYmyh6bGsn9+gT9G7DkKUfLq3dSC43Ufr6FMcRBzk8hJT9jDoZgjZKp98h5xzSJvxDshiQVl/bb7GAvTc0RZA/qFnYYAIhmeKofMPQpyPxPa4PglLbCcjGXwUj2KYB2Vw7mDh/TVH1AkJJCtmtqi5xIRgtPTEruL9jrqecsOZsNSX+lQFuMZah9jmlkn2LQFJo9LA6VUZ80VrlahBfi7uu8T8nUNFFwWD/PlYybO7otShtIM9zsJGfSw9MT4KGy6AyIRV8c3yerQChpLnK2DSI8WS6vK7zt1yVojeH0t1BPy8+QuuX7W6e/MTAGWeYSGvCTCOzOdHRtX5tbm3q/oqwlJAqmmvzHcF+hoj73L58A1gKrYP82o9f3NdYDy7LLpjA5Dc9Z+MLaqkLPIt1LAyED7OJb4qoFAsiTIZ5zzz/GM09PLpp5649a2dek+xWTjG54s5xJ54YnYxF5XGksrLFvrx+BAboeIVPEMzyU3UBZ97S68Hxt+iyg9ZOdL3yemWb/WR28cbBUFvoPD7hYOCTpDpk8ZNXL4kVSSau/g2bjyAHcJrozOlOk9WDNj/OtfGOc3VFMB40sCRfAmT38NAy/HjhwOobpJtidD0gorImQ/i//xADmhwMbUJwx/Cg7QJC8U6wI0X0EaCAq+0GwBvHenqWkiwWlALuGf4JgJ6WHJkH9C0SiA2ha2Op+erp7o1czPjH/dkz2jqWiXAEOt6Vyu0DAyyevPgcCvCRcIDFwWBcVIOsPyefQpP+w4MYz4ESffx6Li7DF1UbrkkERRcP2UCSTRIdjRovXW30lpfFw4aTUtbA7dmpW3l26lBwuIPInoDy6bU+ocdhXNpVZ+zeS5V/7lzOtgW4oW4eK3DMjUnpabhUlpD0/23NawyzqYp7tyK0LBtd6hEvL+EcRu0z1AVVjmP1aZ2SgOZ1JI82UcXCqQrhsqXeleEg37heo3WxUzVHI72zx88lWSZNTelNC2oyYJeZMaWSJc3NCJa0eFtA2SF9JYwy2ZkFliunOLyvb+l2ywJVqSuI4GDKl35F+/O4QrHkb677kKh3H4rQCJsxeV23CrvfbU0fRatkUwQTLCbSQOChkcnTDOxQyOvP6TZA79ZpDKhq9xZrMXh17PPiaS4ifKasaZ6cmWO4sCXwG6iEdygcMAdyEF9sCUE/LjCXHf4IN8j1VQu5aOmUxN1dqZvno9JfIj6gr1Cr8muWC5QAMq/T/DTvE+6sLLOKauvrtCBV7jmsWxCr0WBM3r4rBLRzcFgWaLE0CLllaIYqKl5SNeSuZQx3IpdOtzqFw4eQi6X/HPQpnGufPyUT7c/kl5WVnLt5Mk6ijUIX8XyRMPGkE02v8fXAdYHxJ6drsX5Axub0WHenqk5utufpSPBHZ1/Qb10hJQme2aSMcJOb6HGTHmuJcpn+bkyEmKGQMwwrmhRL+0ZCszM5KP593eXNFWr8KmcAG142kbGGTdcSRdF7BhIarMaGIEzuGyI3LOro6jrSyPuZyK0JAiKmFJRiL9hsfhEpLB+f6DDSgEjrJft9n68kFhh57TeZbr5l3QUsMUPpVhCKhBNfYEa6vP3LTc5tIxrf1BQMlomXGI64LbGrg6Ffah++Au7fAzkmXTo0903PK65+w0d3YwfEL00h3/t4hQND569Xg5/Y5raH1sVAjdT0X/soGXr7+6hq7ztRHzZrEjTV9JCb/VQ6lRJcRuaMbolDDgNu/o4L97WibJYsyP4I0xlbgDaraOHyhUTxJ0+tOZI1CEWrLYx4YWfIce+JA0/aauEHHoek5vs0Jr1wa4NbbczFQWTWCMoD699WhEJ0dr+99Gzx6K45IP67V2w2TIXpX/PhzP9EDqbt3CdJCpSBn1TSUC5xzmz+f9mOX7IZxaqAJoAPOqj1IKtX+5qxtZg5iMJYEZ3fNivwTSYZExZnP9vL5w8BA8q4GopJKLetw5y9P6Zj+1pdM/9AZE3Olekoz3EbduJ9E5BHVAInYVMis/lYSIfCzKSkESXLzWDni7jB+/97TQy0snHdxDeV0mPmKHZ3zNWaPSJ/IPFjSVYcgMz2MgN4vvsGRVJF01xyenMfFMcFbocKxlbKuaKQQRbfkQkITewgs4hSwN+JWDo2aILXgVjTQ1S/mQqaQhFgSYgm6bBz7PE6GC9jPmO4MyXoAXVBl8+SzpzY5U+pIIQEsxj7wYic1LR3derAxuCjaIym/rKrdaQ3LsxfBlPkhB42v5GevdE+BJIJJMkwyJizS33b+Jr045F0rlPYg10CLzDjapsn0kcSZlHkgZ/HOBy6JAd1T8r2IQj3j0tPZlhSIvoNeq8fqvrnOcoSdwBPxmyKYMe7whrm7kEAk8YZu+T8G4Rhdf+4neUvnGVFQWkjqB+VX6qi+fNHVWO7UkisNhIVrGyC5WUa0HgcJPS5lM/O2x0a0cnCZVa+yYdHt+Jp/cQQxDUsHqo5It/VpkB9QXAJwDR+5PzbkDocYAN5r+r6aA+cstv3eDH0SPDW4Xk05Az4qopHI2pISs3zA/ihrvubHVxQ2pJAWq1cfpiMh2p0P3sSKFo9PiU+WUqlOYz8YvOxrlOBRYG6dIgFBTtt7YMAzjttVpjtDTrMx/qIJM7mhDrzfr/nNU7lTMy/gf1u7sDcMnccH4iPu9idoqocseR21ZuOcKSaO/1ugTa4YR3jOn+g5DEE42rqo63AgkSQdcnKyO54TU5+D9Ww7W1xhO9+XNsL3ZcdLh91GcaaI6/Ad5Che4m0e5nSpw8UA8XXQa/TsAf3PcjAiv6Y62I8TQKc8Cje1lJ9FCh4wG7g3XbrvPto6+qik2xy/d7zcLHghldVMnxpBbCQvkliQ4l61ghJOZAOt71W5T20vVl0ZnkT/FvV93lvma1MJXwC0ryjAEtw1MZVOdpYuVTVtkkXnSeULkIuLUUdm0IxyNNLFs3sTEoN89YCrkXtQ/nyJaCymc4ksz0lgTInsdsbhn9Nbkgpe4/4uIZQM4G5DDGL9mwQAonYpb2MptkedR98iyWtNJP4ddleyJXnUYgrt0XQbZ4Hweaz7VYVe1xfF3/6Cra+SUQEZvvcWJuT8U5RZ+iNn3a1UcH/xFROEhGH0C2APkfXtqKlexjAzmwDIu7jJh834QH+rQI6T2jQJKvseiQ2j7KtULRo7WV6JkRESBYcx7iZf4dXYcxgSaWbJGo5fV5AxEGKCD1zyaUHJjgMN8vTyRMTmSJp+QgB7onoNAP3UigPAdSGvVI8GumsLaR/CuDlAqcHnEI68Hlrfp/y3lWH9Wn+zO+nJtNbRVhhjAAJYX+Je1t+2WPiqe+en8AJsxPME54f2Ddz/g8kL6y+HTX+J/JdGi+bVRGKwKlIm2WeSLTXAxcjidjMWXy4gF+i0TAnwUO8UUsCj8ij3nhcdfsRePJF+k18N3C1LNF5oMuxSJuXhIqoe4ks+wy+YMmFECIwyHkNkI0OW/vJhk+b9Wzo/G3j7HUuUsD7nrTsvKNIViholtz1T6/wxyBny0ctpIMxkTFIjtVnYfki3nXdDPkjKtRU6JPdpgG2lqnJ8DW7ujoOWgrRjifF4WQ6TIQisaMwl1l8O4Lm9DjeKea+nPCJYHLhKw4U91sDFu0KK0cRpGlES1dBL0PW7eiGe6SvThuKmv/iHMbNr0k44T3yqTTEIMVHxAQSSjQTt4QjFDboi4xPfCpS2YdpIMdYItUSLLw06aa+CN3pdX7PMbrIcjZCQgIjNQohjoZcY+p0RZBQrap+XMlZoxZdA3uw5gDhlbarap143UnyZiH7wKBLkDs321SIrfd9En1DAc4lFsilfeBXB/dLWwFfXdsV5J5vmivtkZXLxrhR8jpc3WNSkORXD0jN4NjZCc+rOLQ1Z1AlYb5XRtsxRxZepnrbwmAUsr7hjIsuxK8db6zWwpbxt/huLaAapmUO+fYFekAzH4Mm7Gh9C6hokW5j5IuNrfTbKFdGRkum6WIHH/XL/FqTOY3y3GTZv3zzuNzug1kAXgig6ip51cErNIn3V0VrwmpvGz7GU3q3m3D95e/MqlWXbSuY8mZWPKz/G0UEHAN2kbvMRjD2yqpv+vw2AubBAoVlqAzys+ZcMgieO1gKbXXC4a4Ibr6iWcKlOkcllMu+8UG8ZUAw3absyI4KmRB2nFLOnKWyHMda8T3+LftpAF6pbYtVnfkJUeZmRFlEE/N+KqdPmcSnEJ2URzEPgoTJmM4rOiPlFa7Hq+pGcGieDRWLfiWlkyibWnpj2rgktQoRM9FuzHdFtb8qKn5yF8SSgxucjGTlqqQSY56pv8fo9h7lUwooMxwBeWKNuSG22u4qTp1jpQuqQZmjYghQdrMT9mNpknP80kyHjf9QyI19G4IxurI/oCuj/Nkza8ajk9YewsQaEj3O64c5wPrq4aOITQCgovs4KxJfoWhu5zl/tcgrFwbQA25bNd3l63F9M6dOmZa3TVZm6DDPfgGRpBO8PGJJSwFywMedWAUlimt2mTSpKekcO5slzZ3y6ijFqVRoyzYqE/gg33SFeU7qIHYVrxwPIAOa1vRvskXg9QQBu0Ri8Z3AVIT0RzOG3Bs5H1lDPNKEr7G4ZR15birnvdhnDWrEqjaKeJr9I8ymt5/y3tHH0Yaex4rxOtN8+7QOS78/n2c3z0cEJ8T5Qfj6EYhDBYQ8pxqaYJqvJAyAfUqeQvFlfeFN1zPCWVGbUBWYceIQMPdgRmppfXSHDIfaNgfQUTikR2qsDAlltjM01phVOsaW7tQJGKnzmHecPCqfdSyB9Q25ruWrWsTmx46DtPMsuOcHx20OSCe5wffedyQkJtKoqeE4k30itx785HpNt9kosy1z6xapYVHe4iOrvoRcIVxWU4/MDgWS3vO1A4lQw4wpF1DMAh7FB/sbV4UZSdtjW8QnFzDV/4VEK4fAfTdv8qxJCLbhKOsjkyH3YT03hu6eVUNZ/xp538j6g1I7Oibhlb3/+6pXF/9FdqrrhgvHTQVCTxOZ6fM9923REzuXbmCyc4CbLORj1KcaZ2mB8l+9jXTiCSrYr7/O1JWpSVYKl9l9DuulinjVvTL5LWQkBFEYj6o+uAnq5V1Cry6JLL/yIJn7AXJVM5HJ6cSyYyM0ygAmS4KWWBlGSzRo8p4X7x3S0HDCoroVHU2EGliS2uTECO8cdQDDVbNFYT5OMbCTgrRkr/hN8UhLiTAjHetgwAnf4MVtmd7pe9ChRqsKXJwuNur/730qxoFJt/6fu3S7R8YVI+6yD01bJr5a772a6sOR+48c0qV3JCqrUT7AuaucgZy1xUePcdeW3Tt71n6BIe28ADfToS6rRlcBGsmd7T0BV9/YLYhI5dmkCPTvMrsWxnVj5pMLwKDgjC0utgLQGvxONOFLDiwqVWo2haIveuNFR2E4bcpCrgHG7GNqo7A0xitYSKO7EQUe/R/OEr16IS74Ta0Hqf31i75YvdP4+mdqihY4R9ogvjNxYQ0HSxQlaoGPXyLMjh7PgPvwq8knV0b8S3rxxJzcRmSBCKLUSrp3cfwvOHUjmEEMecCtG2xYYi5nC8WkFJ3+2GeDAg6PQz5+RDUkhULaEmMW2WIVGsJt17khiz9SwcaCtl2ANzZaBitnKM8vMgKPYoUR5idAj3wFggzwYnLTtvMcl6sKSx2Z5ui+zNN4DM3Zvv80ILRcOSxCmUsRIiFJN5uYyvjmQhWVP8eTD6HRm21TxJqDL8q92AzKzDDSFjxfzi+qNPGoXblxlY47Fw+e10Orp2d16dvtOEUczmX/jUvXZ2VS2GYCjiXyCzy7beTU5HmOHmrBStZhpZet1oM+mof/kEGjaUH68SgO5SeOyv78QRuIE4k5iFepN+CL85fovJcLN/kM/PAhWIlleXGgpAIxssiSpml8QOuWdWaziPaqFrIDqnzVOKUjrUn/Zyjao2efHuxt09yDfZArvY6BsLsBL33fG4H5ygg9eh8jApTwFcsynVvnVg/TkzAlpM6Pa7ewcz4QMQHm4OXZpFIx8wyh+yAO6V5SKUMkkRS0WvstupiKdPwC1PhqKSKuf9+L10hk0PSBsrI85sz74BsfnR6Yi5qHULT3A+i9dYrG2SP9zzohLAM0Zwu4URWmwR0SeNQnpA93YXMFMEdX+CNmwVSHocVyjnrlb3DWh8wAeRUsm7dDn3AZ/WhBhsBYTI12mCtNSQvc9xFzKlkylmC667eB+OlXfFdds/mB77nM+vqAlshWlOKg8YvGjGSHyIfNGZV8R1veozYTxs5UeOKq9UhSeIwprrFlAqGIZJHqwi/NF1hwtbcvIVM0+OdPmoUCYrxfBFjd9j5BWOjBfh5yBGuDkb5zCF7ZmUQ24i1UghPFx9FluFopcg51uIrtXCy9V3S3bfC8mbFjuuoWvnYuzPivPXYfDkM9rZ0Dj0o0IBrZG9adkQSl7AcRwy46rvV/tFa3sbzjbLzUypO5STaFP4lNearXbv93eSb97ayY5LkOGocZh84DYao2yE9XX0G5ET+ClY+OzcPfqYzDNWbxqENHpMuJoHS6xeWM1Kq4oa37dlrJHclNmDyQvvdM9H0m2lcWgT1lzAgMl/JxH9j0ijPxZ1staKvGLvLQtEmDuxPe7QmWhEe8M1UkKbMTqOl328UJE97tfgr6PfDqah0Cs9A8LeOjB3h0Nezey9AoBj9YVddYTfwjkuB29oEOJOK9oFKPoZJjRXIlM7mDryVzsu7RSiJ/7q/JYEmzwr2e5QxPX47lmiddHsunkUghf5TL9I5xodEozhima2YKKWTphDPg7tjv+Gidq76j1CZJsj5Ou3dXJWfSX649GTaZbjhUSyIWJbatgkDIA8tsQ4E+1iNQiSqV5IlYd9kmdZe/GDWxj4G7yzRHpXUop2C5ZOLFlm3+mK3eRDF/5+1KE1o2AL9//fptoeM1zsvoWIAlO/YSvjhoVgYzFg16IImyr1I6paN5MKFWeZ8GiTzlcgCOTV/4icG6vM1evoPXK7jAnV1ybsvFiRW2YAJ8eIV8DhHXvlhFFi7XW3eKUCtI4daeGR7+Zbap4zaDB4NeSBvWV4YO59M1l7jd1/yxnbIDoKDXYuz+v5PXYFBvgemk50EDZ4CDpV4OgF76nfrmZ8sXbUTcRFm64crOGJdzLMqqsqr15VrbLo+2lZlvX21OqYUh9Q9ib9w0O/RlGoA7dccokVVpJonRyKUTtRB2vcM8tzbCRo0qF4Xkdxmk4FPAwuxWYiqrZTvgxPY5sHsASmcxz6IhrT+hhBGb3e2GPVc4f8LWofPHL81CkXZWAwwhkxf/bZvK5Qy6umpTZbA87smnXKfDeUHBXjKm0HLTFjlz6W4Z1RmXDJJEo43ZSK6ahUDnSlxvGRVU7esrEJvqgCbiza1PQUek+5IP7Cw6QqU7B7C/oKMVTM7VRsZ4Q3gfoRR8kiqMZXBXz+xmWuGLlyIW16hWN/XLwNKxkuXI6NsMfeJlzM2uQuc4aBEcrlvGPBRAbbWWBkAQI1cjfmI7H7x9fpAlvmlO52VinLMNuWwLLisaUgdNL1GHzH//t7XtbcaYNUH0dIxVFsexBAHhawAn1fPofe7PdSwjlWv5NZj7NpVib5AYy/kfTE+BN5v5Yn6WVhoYE/CSERA0HC7T6QL1IjF7qAQ8sjKBBYgQCprlHN0vTNw3EGWiNnNt7AbW8ydS7gPiAXsqUpkGsjtrzIaHKZJPoLmI9lGsbp4X50IOXWW8bz3vVQ+2kOZgIgVIGvPMFTOpXtXiL48tLcma6ELySmUKAEebgGtzT+w4P0d8SXSSsRBWN13tnHN9i4Wt6PBmyvXatoyH2Qsuq+G6ANVdcM4xzHqhnt3bxavZvnNogkmW6wDdEDUNQ+oAh/VLrlXCjeye7BKypDfP86gSR1S1BSLVBYM10kGq0uob/bGcQH+PH+hIvCICXVk1LHj92XQ72tGlXN08UacUqwENUZCxCOYQW8VNr6+Bgdatgzy5e+M4II3jvydEQzbGILuCl2t0tCwctbzizQRTL8s3Hg4QA8sgEdTU2Ie1JOKQVjx80J6Um53P5LhuP04orTuw7dRMEb8ly2CS1fojb/8G7ADee1I0vsAHlPy60N6TmZP7RitReZTaDCIp2p7ldo30GfFm0kEtKqQx9w1Tc4PZ1kywo1JIPblR02DcvlHGrFwlPk9EOC5/KCqFyNORaQXA54j3E8yifGIp7CixgGBcnyC9wy0VI0HZhI0L1bbVE6Dgyw1FxGgrZAgjrjKBvzTIgrGhFy9zE6YS1q6eNZ5QcV6u1hZdEyXKsmh6e86svUpNZCzAzbC9w5mvLiaUSTP7cDvvvhM36DeoIQFABPVniHwaL2iXGZJbyoUW8JcpTx6WIxCVZ5mBvIXt0IkTQS3J+hSWrbG33XbOFEL2zDVPdbpycUyD3qQ/n5QoJAJjjJbnEYg/5pqHYwUWYHO3V795rBb6rw3RHLBq8d1/HqcBpDl0PkzoEUSj66IVN0p4PR7LQz+tRo6cgk5SIPGRRV+xZ7DyFexf7bZVg6n069iOOnX4QU2yOtiqenIuxYze17Jy71WXad5U54kLoRHSdDLwPhNJMEKikNIJadA5JaxRCGuCTmZ1o+AcgeEY3g2Om80MrOx5WpNHud/l+WHOBrPI32rLLnSBEgZbREB/XhuDN9RXuqSqdurXUlwR7ms8e4mjRNckEcPGMTmIj8XUqrTWTxRDVoelnu1z0sY/N8keCJtm4m0/dAq2CCCKNYI+YUWYEu9NX6fBzefWIm0ci4qmtWMrFqa2LS8K7/KFhqNR7+8pMCDEJy6iiUm4Y/bCUY9RuQOE85fYmPraL5VLZLL3SG8QqBgQNGScDDsACOkBJ68zkNYSDi24C4y24tygnr+cRrommfqHcKwhmCDxj528dPhgtyXq/Rj/zXUye6GtvzgroPhGy1Lyg1oIyuzElE+a4elTjkSC9d+o+KX7AcPJUNOHLgAm2/02i2ATyBl+MFd53MIv77NBKAf42xak4MvebKiZA0EMrW4rcMHkZai7g/KxDRn7HbSUP+SazRyPyvDdaJLeU0lrbEOeNWMmFTGr+7aSjNYlNNoE78R1tIDhflrbePMtxmEBhWBQaMzkgdXS/eL693Uf8nmSdLq5QSGxU+iRLK9aEOptqGsi4FhJlBg/9u3X/pmOig7iYRwQwXW7QTAfzSEoJRgagJuqvuSLW+/Fz4u4ylP6vugza+FPS1mNTh6YCTMwwyHLbgmUglD3xCQPAJRkQlrf3vHg24si84dPmS28Uw6DitMhs/7oonjSnF59KAvNV6h4RQID2W2Kx+z/fqIeCt2yvwVryWodCdr/2zdfo6/J3BOMZygwTCXQkup7w6avVwlwiRw3DX+XnVQJA06X1249kE0bioB0zgkKKZCLWgbGUIs0jL71tZQe9/IV1NS2FAzLBwwYOJ/L9cTwRXkqRYPF/tUUiflABrfKfKsPFHG5z6QQ0MVErMwVPZQGlpY5lD6DJsA5iNts+drcYgrvtbmltJ75+meu2M+3NqsLb2gSsIFsR/hs0AjFf2Vg+ilrXmEQeiCUpHfO4kGbhgGk1gT43RiL74g2Sumfm/aV3pqjp2Vh8VaOcDQy6Muf9I3zZ+YyOnBU61mZDaEnSrbIV5Qko5ZboQ6cnK0smBH0MEQKJmJa3oDCUIL0Vcjoyb7DFnzaHwhpiAvJAXqAcA4LoedVvnQG5eAyKIzHBc0lkMHsl6GEhFzmSJadSlhpyu1ySuGIFBfICClRj4MH7jru/X++JivB3iColyAlqcW9J+ZzSkgv3Ryu7RZpilVcjq5pJMORBIulCIeeq1b7u9stldi29VYaHRiwogi/FTdkp9VGB0NDhlGFa8/nUjN0PWKdUW+KqqEICzZzAQIggjurpp3WVWosg5QMAeKLYfvOzsNfDycYTW3YVoX3yhIS5CuHxkQiLdQgmzhs8JRz6vlq3z653o9rYilQ3/hqZRoWsWeGELFXT1FEPEq8qaJjG8vLXbSRqydQHIWrroaoQHNUidikzHGHAtGI2pBGpt1ixeBE3LztFMYC2LdW67DbgwVhO6WoGxuXr0X9mXRjXfcBlhjX/7jx6STZgdFdKxFgKXMvff+xrLqaC9/6Si2EkdmOI6EiDWDYaU66YF0cR5RQCTevYdriJ5YP+PFQNZ/cDa1LTX9O60wYu0go+1W3Sm2LInX2bRcyxGAppe28VyCw2Qg9FgYOo2rzdCcX/+xSSEXAWgg9aSeQVFZJL49GxDxCpD3aO3ff/6Qn6IHGF786GKBy1vEE1gQKO9tQpnL+1EkBqrauA5cr3FFpnRGOANENG+7bSkWCiL59yAYw1oFZKgTAj1q4kHYY43eWtyRvimOqtaj/0TA17lcB3GGw4hj+iqJTfsPOsKrjZApHpto47qIASJQaVAWasAfYW5MyV2IB2x0Mlxpam4252tYadGBuwvvtK3g0/VX0E+/iNXodj9wmPi1CGxudJz5XiJk5SEX0LmqPnTjRf99U0f5IXOV3UAtWp/WRHjT9SVIfvjzJXn679IhjkF1VyQe8wA31KlzJI0j/80O0VC4zOjlZC+U0M9r5I9RIHnVUHE+U3qo916ZqozepaKyY9a90kPGrgpASLOgMUMiImoPlh2rCPPIBBHnHZzyEsdC+fsW2/pOs96lEg6wjqjC3lATCwyTQVFkwXeQQdrBpW6RLJv2ncCAn4glSsuC6W7kMcHKFxU/3cdkRrvNl/SdQ01f7rkJu1fNO3oXqpLCWb4RDUjMY/EmhooGvK7QZObnJFaFCEMdKpg4aIigXyCc5edSCmU9/FF4N31KSgbSQ0/ROAIm01GXfF5GHCiWQ1wEoBZhg23vdeEPTWxcYgMIQJGcCpAO+yMRe1qt6tTF9QLvGcJXWY75qiOqZaNZbv9xG+eE5lviwqDMbAvdtceqBeeJRtmZKpeKz1q27J77DjEt+y5xSnsYcMIpxFoEY/JSRca3E+PdGuwxz4m1xp8izClc8KuLkc4vvgDgW3nWSsaZ2jhq6PhJaH+VfPhsf208PNI7+VqDpS3i4TvexkM5ExuwgcFIiOWZlUo+4Gc9MhOrZIV4X6BHsj00zimdc1+73ZakFf1DDok9XCNzONgZ5Vl9xTY+fL4zc/YVUUfkS4It/V7sIOywcolG3lE1+JXptbhxbZP3zfqY4zPKuXhKdwlmeQ6aOD9qDbkpUBGaStI6OkAm1F5bixIajiolwpcrtYCxhFVKPZdT7yMmxRzErlnhsFRJ1Swdha5QSI0ghE3HJ8TPYLw6ZS5AluhtR7r1khVHn5WaEosQoYnLo3cKz3YWpfQ3r5FIbZ1T219XG0/nw0O+PeGBZsAs83t1YhKaJSQBKXYwARa3qWImXQt84Td0whPb4F9k642mGpqb4FghIOydbGqDpxyR1HzxL8pskrfEqk7sysYHagbxdY8Og8fN0H6ULNJUEgWe9aRRwMbBquLcI5F006SoP6DWpOWMy/oQ0ygHPAE0vHiD/0ljmkweSkN/Lk9HXklFg/OLhkbIFy1WROQrlvMKhEGrwXKtVsnaKdwz6f/NCmKHBjmqbbkV/e7Rv072QZZvNFQGj70E2e4cijAHb/Q0x5VkhSPjKYYB20AQvChf7jO+v3HRc8jX4YhUMjAtUpyvW2WNDjs3NOD0hyF/HEc/zwyIyiHJMWjM6jVE7j1me701GNANbk2KaKi7htPBqBBKUXGd3tZLo3tYmJ3DjoqWjksD9TTG/jbBzb2rWiZaIvTJTqGno6K7dhQLIXfBQyAWLZcvhoIItd+8KAiWxSymuz3md0Z3kNIvlMuQCldAlUL/bTB2Igg/TZIXoJQ2Gwy6gH0rv/ATe5QxYvIEwMZBzks8vnoQkL8/ypWvd7L3zd45NnTo3cPjYiUyDkyPozdcPbct7gMqTLBUUNsRWVTmtJos3WVHdxnl8UMLIHQdqNPTxsTIX3O5i5xJeteiU/z0zK8ubLrZaMjXzf7GTK8twOsxCWPdQNlz+evsoltR4WQSwQEsxurdrq8lNFYLm+erOiiO9MOGbWSGaXQ2154uFVAQbUYY+UH6XWsaY4R9F8R5LStnQIRHLStuVSuiVOYTCvam+8KkH+LUFZcLRlK58T/q1M8T5OzhT+3qjLcHkdQQzeuoPPrXrWT6MwsNOnQqpR7NHXDhiIWmO6Ug5Wkf6QJdbUv2Q+Gko8pwVLzpFge9g+SV5hQ70Z18m68jJVtA0/Oo8mxFuWDxcbEoo5bOBrTJLhZTSbUUhfzQ+lV04sVVfuLBzSjVEgg8XqFbfQhssIu/G3tTfjB3Fs9QksFxwSqF7tGH32z9Dmc06VjZ3lz9YwYfb3vGnFJvn10LyNk8D4LxXJEDxvxMCiev8IhrNTjD/ocYe18oEF7eRapN5USoUppwk3EzZGilVyDlc7yrKDWEO+itQlKiZis98LScIQ68PvouVLX6zY+GAMtZZulZm7GMJ9xO8AlWOGaxAoG9CgWBL3Pi97DE4mgvc6IEfbsg1BVr4Dm7PFHZJ5Q6gkDXmHf0Galq4HVlB3WqrolxKTCBQtgQKLFimnx99NAzgIsFzutFBFwLGNbsuiMtmqxhRN1v375hwG6ddnEuxcQVpu0oPARwYQ+j3s0ne1jNmsFZ5CsDlKqhC6aN6Ciztj9IarFg7aA/utwI3utGSE4Xx4TA7OdZJKiesBqtR1AlXV/QD6kMs2sLxV7Ltao7PXKkGyi/Edmxh8KzkGP31GBK9Rk8S+HZnv3rVf3BHvgKq2324YLlS94mgNrnQzEKiK1nSw9KVxdZILektS/S77xlpL0+RW17Z7uPzQMt1LBSD82qLGgWm9HALxWqtv5KX9WCcCb2sswJd6Qggn7Wf6f4rqyJZnOJjCoza6mHyDOBR4Qe7omVa0A3WsUgrDmrnnn/cLOvwyW3n8qGiNQke/TkxZoRIcFrBD/0xJomLXMqbqJ0UVEkWOsJb/B5Z5uqHoui3ZP2si1JhBMIhydgl1AL+d9UseAzRdxUQ65K31+1iP9cnn/DzaGDv1gAureqoV1+eCmzYQXaWDZQN/IpfVLtjgIWI9ytAaPlhGojGLnTHJJlVa5HtQwAYX9Z9HpoYZ4ebyzuUoJfrXGY40yB3URSCmeDGmcuVM8x6PL4QZYlGWnjl9MKwI7W76BsrrtRrPZ2gjqoN3OrmHCN7mxXX+E7TT/70FRObpbQziK2mXS92XAYiMpVrla4TOBPG9kX94r6TpFxH8a+/M12X+2uma6vcHVFQAxZWF/9To2CH1XCeSGDSe5DGFl2NmaegzB2DwjqL8TcwGcwoQM4D0dszhS/JpvtJfnVYi+/AejOk0sKiJ6yeInA/0jSq97Kc/3h9A/bbHCcFoYBqIVsWVFgVpQVGuurBFJ/4KjsHtgGKGNQuXVoIajiVgx0YQgls7mfvwaQyfMxbMC/r/4yUgEDBd3tt/lmtzmN5Enzb4eA1xkgP7L7N/BPN4T384dxbrer6ubkUhrGLP7R9NstObFEVWvuipbODi8rxGgiJicZPyZnWNClJzw1PIbjpqa/jSp1yU/4cBjNDvovBN3s+TdJHSIkx11gagZoWbZ9ztZj1YnaU3jaoz22c+fg2OASODaZn2kVo7lOACrJtmRFmf9/5lvkzZpc1bpHCAcZ/nQx0OAVYV4yhrmuaju3r2edr4oZVNH4B/mwDqNZbnWnh05DyAOHX3qgxx7TzWzEQeteQC6jLb8WzmiuovA3BSWfXIVDrq0alt/iTKZgflmioGXw3hSMHa9WwpfoL7T30dovlVDVV+cqbz91wUFGpwQKvy01rPSnlhzncNvEVC+erpSgPL/tTxeAIjW4BXrvZQtdcuv6NyA3HRV7EJWqwovMSnDjVow7CxxHgwxUmHe4ctWZcGIz20Lo+hxBrWhsF2ArVvaJgYDkMvYGxvhLWR+3s1DZII/AyRyrlx666DQEVtfGTHUhzGn+WtyAk7/UAyLZyg9HY68IIEkhqQKtPFRkIKhp1BssXeSp/R2M9y+r5q0+nFLEDyeuSe29gZliKr1qShJ68slzNmiAns1zRBOonw58RRDkzKZmDGPVzseJWcad4Q8s2KAF4azYan4mnhQnTz1soN3zoq6vsgvLcmJQjnVwrVXLCgHE/VNV5ODQu5dj1G99Yb2PDwHCetpJARUr1Yayx540uDXh8OG1c2YY1DOY9/x1ISSANzjrybVULOIr7Ftv16oXA4AtKd2FfwISjG+mnMh971ayFz+SFvqcZHuFvHCUshtmAR7l15yU3Hx8+Gm6hDcsU1zZ4Sjy8rYwlR4CR6MvlEuLylaWVG5C5w8ZlB8H5F0vi0lD+qa/YHCLMY3zZ79nQcqPH8ZsPmXZhzqDIFqM2LUTHbcBeyHm+qDUXoxhflyIm0rH+z70YoDVT+7nrdbk0OnW6CE3lKx2SYjPLOky+d+rsHHbOsIhvqf6vZeoQYnmzBsF7JU0m0vqDhjRSlIHSB61wYI+9hgM0JcDSV98AljJGrVovjiuZ49UAK5C2pWcWo6fBeRNVH1TpKVQc6G1qnvBeNNrqfaJJQhDxwKCNetR7Wox00Hv85yIdk/2qPyvTSyRjiEBIg75hLZPBCDKOikez7xyQ/+58dSVHgK0aGV0LxvHBBdpTq+ZeB+OqOwrTKC1IB4w8HjNB2+3uK7Ue8pUZasSNUiyKfk7qlU8yePRbhLtif4U6Vb2T6PJX/Sz51NySrIBHCnb7OuzvH9wHn4BE/GDvnYgEwHZNXlhJ2EOYdxrrb3NvmDyDkEX/+97txMapQALQToCLf+6hJjl+VZR+BTOusoqo7kc6Vl6JtW741kTQqMlnQiOtmNRKyiaYlbpkbFPS1FzFJ3yfGlH6HIP4x1y0tspumt8+FhyWYT0vtyMjSlayszdsDROQcJhTBhKo+06XCOJlWZ7epe8cELm2bXCpXrVW08tAUpWA307JOAo3N8c7nD0+yhAHIcUqDFvLh08f2N5pPtfKuhxGPYcvNg8P8tdYrAguIe8Ed7F5uYrzOnPO1joH3ddjUgEIQ+Ast8Qibkq1hpOEkbEkZ+qmLkcXKQB8+JVYQk3voBhlCfcgdn/NHxSqFzFFh1KGQ/bJao/Fxh8EhOOfMcGO2+bHitr48TWVVNlzjuwEIaoaP51t/Lhs4Ou7munLofHPy/5P9RNLlXbF00Gmqqqs+Xi10Jm084/59vtb17KkizMBUBGZXxB731BW5/oi7TzPt+Wr/yXEcDMk/epKyquXv/V5jJFK6Y2rbQwcK8UkF0d52rJiPvmHWU1/CbmKVYm4hZkXI9fo9KDg79xDmSXTH3wmlar3L26EyiqXvqzEwXB6yXMxb2cOeinw6Tcky6BjW6y0PC+9hjZhVej/C+v5s4hpCFw7yJ+oSCSX7LLMKBPja4aLR493u16LjgVXweUTtjTvZB+qA2TAy6F+01RKFacaiq5g89E92v5+SroomFGKg7a47R/VtxvXfRirpaIZnWZvfri16H7ZFAOEh5xQkBPojUUKLiBBeCLxPDpsbqEmf0/36+lLrONX+0PuDB3UHT4KdIEdJgVw0gXVPVP62yI23zBthTz6Y8uz3iuDILlcIyk0O/GWAb30aUjNrDlhOqNqI2CIPinb7qikeCmmlHAxOVLKkXzMl+WFEa9n6lyMizPJBF96pbbA95eE+cB3V/TkjkhQr4cQa09QxNdMPvFtfKSG8dsWMIc8p3dmMslbMz42dUrWoQKUNrDxnLIFsno2TFwFIQFDtGr0LjlTAtDsJgaryLchdfyjJzBobCoRo3CQq/N/wZzjI+PwJexqVn/Pbcp+/wuF9AWliBVpdJ/thwkQGWP5+h7b2nlO66UbEXUyHL74r1RXt7HJEps7aeauIIgIoJ9YGBFwP9mBWmy9kPiAn9wvP2knxNyD35cj7V4KihHD+nQ6Z13+PdthLUhepAGO4fAcSgfKl6NpAaUueZb8t203npIP4kvvyrqMUX5UlcKdFysxi4CzWHYKIVe/AcEHUi9v+4RK6lTEyi2sSDc8JVQWA630G073nOjlpFyFADisLqj7GQWMoIu/TSu89uYyw/bzK3njLb3+gqPJ4ajYgrTAPHIwAOqFUfQYMiTcPnIndnYGUs+Rgg5m9nNPuXIVpEv19jijutb1EmOOTerf2RhHjTQ25gl5zQpjsq68wlmo+wcS3yQgB36U1OLq/UyhUW5qDRH2g6bbvSYfiorYc7453CmR4t7z/THA8zHLcXSHUehxEVkZYpgthMVfGRuBEnVlpXub8t08otsYiJ3/GN73/8/kdKJ+Fyh9PMNeKQ8Hw6Sa/Z1q2YYrW+FZ1cMORDJoJRbGV0uEg0SKp/s/F7AWJnGoK04AoenmJcTZUmmzUqX4+P7HG7nJIpMUGqeYuQgVTCXWnj/3fCneFDyim9kPcnPVqimPg9YDT/d+ki7HrvhQyehHrIcpPpfR8O5NgeLQy1nLppE8PnP1IoKrehALjst4b36Hh85/cApj/O89yUs8DI4rfYnPNtG0rvGL9N4DBVG5UTQ06QogcZCTfeHxdJ6qAM84+5H+W2n+3Qz3zqcJ0+Ri7Nj5iTmZnQnYLhQTRmDTKadXz1Jd4YjVfEjdQ+tfBprlSIXMK4oE6bhNkx5bK/Xlr9ERYijAuluCYzT+DEgGVREILoEJVOEHJmAAwvoJk8RccTRowRbs8xMRotj+cxp83W/zmoY9p0geIACiY14ChxTDnMQ0MMyrAoU2nU5Bx8NKo2qgvQiYZwdpQG5Wz64WeTZZ+kQEHhiX/TWyzR236X0lCc0sF7lnPMue6GKnOshorTN7EetlcUN5OLDLojQpirt7bU26U1qWJ/96P4EjPjzABAp95tOUD4aHD2Lyj8w4kJlpx+GkMMWux9AbMwbciExLO2pnpBTSU4ptMJgO7q/3PL1MPV7EI1sFqgj1QC+mZLTyvqg0HdkDCCSo3/PnDwM1q6H7z0HsT3Vqomf8EUJK17KjNTx0+Dft1/nEEvm2fZzFzHuhi2tCeVCX1paKLFgYaeXGsEFr4fEBfbpJbXg4nLMo5sFhu14H46BPQ858YHiqhXTHSuLhrWl4ij2iVYV4maFAzzopQJjQhUCWR2PUzYe8M3mtFTdCKtxGak70SuCn05kc5ygudUsxJSY4ZVf7dLwBNqjyoak1rzedbOCjuovd4+tVLOnAE4bpq1xnyJosJVGwpx9B3X6Wb0Eki8znP8y9L+9oKN1c+fxj611whTj3pRmvQG/aE1kE7WclFlFm6qKAKQ3wm7q69GTqv8QlEQ6JqRUC1KVkipPOkrdxms9oSLZhqSdIQZxDQFIwcYSGx/Y/+e1zUcC1msQgmxZu/UdSrvi0Q3u8NkQtKyw2L9q/OijVppSXBOv33Ha3ELyhwY1a04jOEpYSy02A/qXbuX+q/0qgckllTLgxTZIQeQw+14LhOxt5xHenVQ/c8sj9WP4A8B9T+miy5l7/eXKzPoksnrX4o6HHREN0fFfIMbiKGGuYBOXusorRs5Lljfd1TMV1Ybi+4ELTz0oBWXPGyQmt5GFKVX2L9XcoRBqCm823Ak4hUeWdWphpESOh/T3HHDjYDnRVL+lPzBtXt/xUJBgVE7b3eYqUcZEzIfER1EaQVigj/FvyrKujp9vpLf34nEC1tRBhDKaSiiZFvF8aG4q7NgAe3a4tgtZYUp16z1SNqeWRa8pSpKbwK1G/8zf1RwbDfrO0AjCeFr0JXW55q5EY2d861Fm+HFLNyru5h4C0w01UHLkVlcDn/HzXq1T3JcakMy5DqwSXiHG4qpz3CsoijdSyOjVwk1RYCJ6f31pfOUz83avq5rRszrFohWzZHOmhEfcvrhfI04mXTsNyQXs/Omufla3bWCrkDPUKCeaHn8EqehKU4O3GxxYAzIQLNL56e7vG5x0/4jONXdVwpdlBplItl5greE4h4WgoBft7Yv7OfdcdqUxWi36PIuv/xnnXryWP8nZ5acSJ4RXEx4rV/o1Rr4zBHPHBKbTTMQW1zRjKt8vDKpeVRC2FbbRlxBRJRBjBueZ+uURjP6vit+UNYJ4DCm9amML24ESMPnTk1vIuhVt4OmWP/Q9NV/11qSDq6d0Y9v35FJL053C1dVdFF/gvtU5VYPueskx1+PYEYbOykSpzsNPPl9Fp6cGkBdUl3/wrHDpvGXrHravHf5t83MbHUsGq+uHAC1N/9AfnmGrHGJ7OnU+acbqR2rUZ7R8aqyqNHAijKyThOc77lkNSGejOhMZaGa2b33dlARaH0I5x3CIqi4i7rL9cFn4P7Z9vAVgQka2oN0lsLquXS+vm9bKM4QMsuJQflp6bUhDJq9RsJbszhMP5w39TdM3PrZjxsoZcFUd5wae2YPXB0iFrn8NhYVX/zOEqZF2YwkSsUw+av+V/Zubt1lPf5W1J9W/HK+AUDTOUqfPChuAoUAUiXlH69SdIdEiwQ4nb9roe0WjMGGG47WjGxNhQ3aR301P+qdr6sbwZ7VWY4piDIGcJTBbDDsF9PXdV+t8V2pJse8kvXCTRCoabG39rb77GuXMymX7ES2vmzKU9GGsHkhfeO02J8knlZgPFHTq1zXrBcTbhF3jaCP/9uvZZzgvQ4acBl49kpXJeYPcFgSmQJ2wRo0A7/undKGpBX6HJvlpbN6b+3axuiqW/Mar5na8jBx4edl/HOKPWRmufUvv8Z95aK7Ve3HkjqtDC5FTA4Qf/iV9aHFWY9sRi3NAyobwI9OJRpAfCFY3glMvUtzM+4XWRDS1dI3QbziAJSXce6j9x/plcbfGc+0+KwMXWSVL34fB/hLoOo7XKKLdZVfkPY6tqcwJWzTq+FxaR0tjlN0FBGLsIXgynEj9BMd1fsNnzalYjEFzbPw4GDm15bauiaAQ5x6QZ7lb5D+9U21vEElMOY5HLxGQ657UgSED9dUOrm2FskqmqEro8j0MSXLxPsHcD1rwhxuN4RBLRBXOZYlZbRUj+mLzUZLjCgVqbWQIo415o/1ZCcyYDVoZeR+tPMGiF67UvIHl2CHX7DwEqUkfIwGpGkQRWoWkfcoEGAKhp0iS85CLrYIjPKQhLUeYjK/Y1YTwdd1yUqhjGu0DZ1hpZQP951J3YkSqzPOVRUJJeTTXdi712IHj5fpoYKW3QRoBsCQijq2rBmr9LyMwnHeOxJ+BvbnLRwvbNb1ZXTHRsK8F3Sfd0HJ/mDIe7gd/euQrIupijvjXDuoKgZNY5D/+8/9+5DN9SxdlAvywiyGJLCNkJCnz9Jnbmw4VhsWj5ZhupWBwI49D8w8JotF7RqQ0j80qG6FAPBk+Q8g4pk5B4orducdRPPNMeoLWfXh6phERKf6RbOzwk155XSIAwVW/WlNd3dFYuS3L5o5FtVRiBSmVWnqY4Jnw4YsG5+xPEWiy2YcVGuKMfHF1q6vNsEVQQncGMFk3LjmHr5jNwZK1dZdw6HljJ9ZgMO4VrtmASrgaeTzpjdfKGBChSMwScVwcjyBLKm3z3wv2Vt49yTPkFHPY9Gcvxt39J51XUGo7TjslllaEvxzSnfKcreA1SzvB3WwJi9Ke9gzWX3pWMCFrrkFay+wQVqlxqvb/Yql7q3G/CKxIBQpgBNKJg/lPvOn+4pwAafMX9+fPLE/wxtyh6ixdte3Pn+HbAI8p5pue+3i2FkTPfwVD3qe+DrnCUo3qyTfIo2F0azIWx2W/AuDdvAqoxskRBjWFyM3l3ySCM9y5ZYlLDhEstXHV/zjKXtHRaJSyzEbXfuGGxlTL4l3uGdlBqUfbaJvDETQ0JSRsXE09uTsacbKLSzOE1tnsJZdfY89CrqHG80LeVzAbBC3dKlXJo0Mo62/n39EGUU0AZFn8Kpy332qlFMoNaSeZEJggP0ZYnj4u50SVRp7kyV21jE3xmyDa+1rojquhPQiINGhAyPeYTJeL+G/EMyGV+C0L69Th71MJP51wZ0SUbsWpB0I+wEhL253jZcF2YIt9/qfItjZwFuivuaZO5JVJIFFZdCYlQDwW4c1cDQ+fIquXoWtGwmbHjCoqXcx3WQzMtSD8YtOBTmSemJ5Wr+5AyL7hx89nsOzSGMlHZLvVIAVWSWHsL4daou3A3MeXSpsdL3UFLqam195WpIgblSXnqG+xQ/qKpWEEpSInFkw+wmmWbtn91tDcMJrdeKpTY/gV8UvhQ2Z3JDG5r3KtbRvjAvaR/1ognk+ddeUGSnge2kVLunTMDvj4P5r4wY+WYAR46xW/n3SNPPysgS9WueuU/deEvXyJpRtP4pkwgBct8GcjCJVoXyRPgf9uuSsWnCKzrncbrYyZGtB8XzP5w1gLFPOuXZpuCPyfmWUJOjfaUNV9DZ9qs0PQsUDQGlYJm9v9AeM71ix14/p0XRdoIrWf7fWXu3etm5Z4997cC11BHQthX8HvsudTeSRObtJVYIFO++90qQHFAepqgGZVKAowfWeUz1mfbaBzHsl0fKoUOY8otSCUuBNo/EiAWkmpw4/AJcwQ/PaNI8M2JB/16G12SBC/JQNNtIpBXc3GrNlcdDUnQ82PVSTPj4MDOMg2zlCrDZ47ZM6FeGL98E1/9S4QCnbF/AL8Txx/apzMR5jMPRRV2kL5tbBoUchw451WoCISQVzerL1zFbOJoh4bWK53YjTFobb0xfTwAKdI58W2O/5yvNVup2nR+28mv//tR4G0JW+u1U8taBh4r61SnmeEZBaDDmzH31e8miv4R77sC4JHs92jjjoHgkSwHlTH4A+DrefQuPYScZL9PSE6T9L1Eh/StyB927tvbHtpa0tZEXE8ixKYUF4Y0kX3i0xYuI36QJw/fKgDJDpmCbrvDHw3ewT9IKQsdeRNZSi7icf+oUNrwkfqnik9tTHs58oku4ZPZi4+9hXwfREsLtQg40s6eCer3xWA2PsGdVYQT3bPuAK0NupkESLoHGkfpp1avbTIxD1ePS0QDqUmRXMtZNROvuul1SkYAnwexlzWGpCKx2XK1Y/EFTGRZI+H/KnWksXr+8dlfXKpokZsAhqyqHEFZ2Sy7pKImN19FMBlQcVPUBxUX3Gqe0TvsfNwP3pY1sCasv3Me4i7qKAMGZOyzMl8n0Dg+YxMd703YnuOX1AR2eT9UwlxoWb9iY2iT/iW6OVa1lewzb5tZE+yY944jazkME4Ur4KTs1x2n/2wlOafy6rjSm0blTIGpO6RhVputiVEbGCM4pnsZIYaS2gwvSBXGbLoxAdn7gNk24IpRKk1YWIJhGjy755//N0aFItLLUlT6Stv4Bp472GVMn8MAXKNAoCY+huZPtMC0E1lh3jd9/ZvIB5vSEtV0uTyPyr5A4JbuPhNklcNJdtciEJ0FbXiQhCk98VQNozCc9Li4xIzeJqMCMywie50MzX7p51hiHDkJUWH49v+xLuU/Io9udCjvhRKNGAZa/c2NbRQ9iIFY06+u2pfVLIH0t2qHrEkVaiIey+S4j7a7TKhTGt9oxkz9r2Y1UasixCYOV3Zv6NC4WttKHtvInq+ZjhZG3UFFw7nJdXuSHOeYrMmpOjzV+L0BJmL9M9VIlktc+X4k3CUkFpGLeUKAwErMgJCz9UfAQx9VrH4wGy80jAGVmxK/Ras/eePgLpLkY2SYGxkpF6obsg7h5PBydxulifvv2G7z7hri2ZdAH+xxARs3tjSMztwEVZmjUJpQqAMKnpySBZrEffhFw4NrM8rHsxIRr/IkjxF0dYBVTaY3qol+R7nw794tWGOD2FMUAiZSd784Zdo3P+tedG8dtl85mLUZ4B47N742tWyZW6JEBddZOTrqSNp9LpzIfc2NvoeUMIUhYs92f70wwwu+mJ5Oirm5NehixU73Tudxyo6BW1df1HIdYUc4291O2W83G6gtodyHknya3Mz1AHCy2HLs9W5+vmPe1+CLxbwQagi2u/gNUENdVVkNJqqjILa6jTILtYS/uPXU95pGFKrSuHW7cIl8HEdSj6rDTAFypc6FzRBDR9eTUm6RXo/+S7uhRN0ZPfCSxC4hPfX1Bg5tgrxXxCGsCvZeGgC9fWsq4VmV8KYSkibUV8s1cD64welgxiZDkV6cWkj7aN/0W62oWy/Ddj2iR9SVzGuhvJ3S6zUWQSwCopwHq9GIKdmyaauWyxWYbu1d32PxUBvWDcjNjJchUZv2UuBZk3SBB/L+u9HKL8LHPcCGVuETVZ0rDfv0om3+c4u6LPNgRgxWModjyEd+lp2DSID6+oKPGx1dSjvKMmx3Lj0YeuAFWIpXhvARhAxLrPofjo04cDGz/8dZUHEgIbHQhvzBJ27Y7s5plMWSAng9tJmHj4Q6i1qBQqvypttpQ+Qx9ghScRqneicL246CwjeL+AG+V3Jmf+T+9hJlH67KMEk5C0k2U+rPqYaQl+zGGdqWTxXhB37M2gazziw4J32fi8UxqiJGQgIURfAs8L0sIjUDumv9oDxaNdsXzut0jPBAYb8CMDNn3BKWICtEk265FocRH09dVIUT6BV/ttcrYeZJAMWDRqSlExZYchJWG9ewLZ2Q8lNVRSe7zRvLmqBXOKSHj304oK0MqSNxOyqQEvWLwvoyWmtb2ngl5XQPd5FRsFC+OYNU+h7+OvvQp0ab7/my6kmf2FAfLbl4xR5WKTrREsR1ZdusSbcCGZmv7dtWIYaYuKf7B7U9vsu50fUWcyipKMmllOP4ftlD/AweEi7AWTROwn/Sv1bI9i8kRrjHwXgx0evPWRUvDNhhRhZHGlQjcEqrwKHAuhiH73LH4lMZuzIKWZfcPSS/Ji3qIxRDnYQ7N3hYs+jz7OtS+rE0VCkrneGnb73fb589x0xYl5ZXTrSi6ZTGx3C/VOeBlGJdoHQSTB4CW/Ax+kAJtcI3RG/XzdsfFLroErNxzNrEuZIUr3aNiNtqBmqy39WfTbLmJZK1Pdhrj+rN0m9DxhJUWuNLDWeW8jCbqAU63/cr5y7e9oJeWV6NZr0NTdcEjkLUgibnzEyfUsrxrQxJbTCAHzBM2PsceIUS2U9Iz0D5SgKxmjxFr9x73qKJXqie6MecMtx4Sgzs4VF8AMbAaJjLRJfTka77syFx2pf/Sz/7im9KASlAlCx990NdE2UyfbQND0nZXsG7MpydUPAdQIB1GOAYu/qBPbT8aRLk/yCkpW6OOVdNHsgpFE+BHHxVHt+TlajEqU9wLGmMI6VoH6KWTxhGLetpjn5wJV817DROjCjWsrL4VL/YNKdk6it+7jkBw4FS3ClH4MbvCr5ATCetWdMWLzIaWleIv0yibLDNNg8hDNY1qOGh82YDgm+msDZrlSFZNH/8IoJWuYQKgL4ndIwG3ev8qgcDML4v7hW6NvgE1VXHpY9et27x9eMXfa+9HTbUEjVCkC6Q4HBMZXXA8VZjj6hyl1X1JF70eL8+iijlH2d0u+Dmh6bcpQGdTqNpa8exPcbA9S1mPuMxabTm+2p8y7BJH9+qJIdPaik3JWt2f+mt4gx8wNuOZIY+spMcwWhK+ZlvFjgdRUxK4iuYYNAEEV++EEBjgH0Jj9ZWJPFxtPhgrlRXVxkyGoqKlyj6GOfSuy6hcQtGk6xQ/W5fU0QIi3ikQTPZMUat9bxxGq5kgZycQLade2OlrI7MxBScQ58/Za16IpOcKJBnw+diEEENVrmx70jAAe5+3v7FOqkP3sXvBjIyJheUpWg+yCEPUl0sF1WBLiXoh4/oiD9EIsg9a/1kIBLYawpTppCfS+lGaY8vXMCG/zS8YGnX22OFNNDyO6xJne5eFizWVdtv+dqVToRpG5LlM6+GUnN5IeMqFs9awFIQKlxdEg5QQZN/Pe52UYskeZz15wbsy95TmpI9y3eC89x+hpWk/2s15W7IAdgJOw4Ii/JL+jXlJ0RNQGtL2RNM352O7dQLfq16Xa5JIBsTJgaZozwt1uE8hca1CiGyRdrCJngq0kmkaIK13RB6ehvd3Ml5kOzZIX8UjwGac6SbTFPz37CtnlV8zotCiA7NROtfQV7ooZ57HdHCuSOzQxzm+pRa1pWke6P6Ytlqs1sYjzdtPpUEk3PruUJyEuqxmuTSxZ3DpwrPQOQeddyMxiLpUKqLvRxp29t/15/8nnZkNX4WTy1YUJRx5221GGRDxViWoXjJqqRMrUNjjg4NfvcZMD6xDvLQVABQJZyHuY0J4yvAky3aoCIkug8/h9n4wBCZBDQgJp6EKNln54g1V8e/5FG3z+k0Xx919/EM8VctOgrRBkE73RvMerZL7BQKim5aUIaqMK1XNhYOEu2Wud8ZC3TMljedOAZGzE0ezQn6nta881OLC72SSQu7jLJgKe0MZVifaR8P1EYbmKp/CpgzWe34p/PZO4qBq5rbmqUKukTU9ewYstIDXbKAGrFaEcC0+Z374yjWN5cVDKO9NOYpHsRfTVxLYmBoFMUcnPhlnakanRgxARXWt0NHZVzOBVPYU1Xd9VVUKi6C2LZhwnblE6nB0skACy0971oRmefjlrp2p67zYosVq6g/vSyv0NZWYpdwyV0p+GOMyPgwH/GWngifAkl9/g6hVaUJRv4j6Q9NIwc5CDzbvp8+3tW/XhD5jM1z8Pngo8u+m4b1zOweRjjAukVMRVbLTLz/PcaYIfsbw3GBw6ohqJvmaX7KJKWdIAx8D2ratQbquVHqkCf9cmWRdO2xb6dWa+6Ga1cfQHfQTySktDxZfS8iALN1mp22EhGRRtQ7WacGkvlEa2MW+axoTj58QIw9WAdv7q0KnPL5epKuI0aUTbn6yVQS13WITWKAWbNmBFUOnYioa23QSJ9Dxe4UUSimGuD28novNgG8GDfPrshDPGK3f/F/6wr7g8j3RW1rbFeNd0yr0kh+/Ic3p6jeah3IWEygWC/xNkfexfhtsj5P4MSE+uROo2MWjvlQCWxJCQoxj1EOkfCnzfiAVeL36slk/Rp9pfMupL+5Qp4m3jS67miFYS5CzzhrdGbbt0lGAn0niVBhK/X27ocgL2RIw1sfm2Rd80q+9+J626+H3X+DQ/7OVyuiAD28DLPlplBOcjGIXllxhLD2wwqmGjiyxsLWJ7WaFzIF8yjDgSOf68DqrOrq52YqkoA+mCXtyXxwW5ZoTkUqqVvuQAwJhNBiDLD6vdckNDjWqz2qKwXFwMyRdE/03z7zGo23aO1BeZeB1W6876hLTcjopNXrfNQzs1GK14/G5wZ3dlAMspy83Bp7sBPKkvMYVY1uMvKiNDCYjqSX0sS/sDLFzDEohnscW5+2aivkEkMVVe7VZM3n8cRMYFZmLD41aiYgSgi4XjQnVGCnAUHuh9mntBz+OJaMaOCNOcW4uPHFsI8UxLptVlWPT7cqGrTNDM67VihdHIoi0gHyQhu9ypgN4celdTxfF0MZ14V3DUS/iZqi5zB6JVT+bI4JHUtj8oZDn+AL8KUzBcSfdYf65y93UnqTFQE5URlkWH78p9CafaKnEQyf5APhmA/5lQl7+UrKer5Ekl1Q42FCO0Po2yFlo1fknjIX3MJBEHBRHaVu1E/+gTQ5HK0Jl4+sZmO4AGGfZHJm4iYmGIK8gg8vAL51olV3zwO6PCzA4XPomSpb3LQcGu2Qh5qX0xiE8BPyrdZLUDPk7Zot55D34IclhGTQf+RCxH7Zwd92HJtA50dBdCZkPHYpJvkQHyEPqwZjRHnSoomqD2P9aGPFyBRWSdJkNocg5ebL0nLY0zUuJKfLR0gdnYlTWmS1CNFTaqNb/DKqRQizIz+k7LziaBT1fzItl30oT82JWggXoZkUC42uRD8G3H/yrAPwdzQWhcf7r0gcH34AanY+ENtuoe6o+7aYYQfp7niCBUr1ChaMAkDCeZ0bl1RDo61acpQ8/fJ9dyCkDbx0MuARVIExWBb3prHPv9eG8Y58eqXH6Wmspia39B63zOhSRBFBOtyYGdpisU+QPuIvgciySpP/xBlagzOM8360kfAua0sfr/r2OOphS1FadR1jYl+dOrO+9E26wxbenWQ5+Xflz5bgQyLU9JKS3QWCUTISJJkpx/69Eh3gBBwTb7iwwCm1I1D4J3/maVpQkvXUUElpXwRVF2OCbQFBIQE5GwDGZbbJ/3m089NAyHZ9850S6KKdkL/lyne8GzmCTreLBvVHKw9jcPE6rA6jEBWBFB9+ap5a+acgpI2gDL8heme6pA1l8oHMuAWAYztF/GRG2DaJau3gbnyEltNil/qtyIuNPAO4+jX7xoKq4eMJKHHkK4W4f+TBpZ+vsMDEh+0P2/AzmCYdyNjmHQINYYch7qwXafJiSjQfaYGD+cI/hA1fQnQGZDUcCYHSwAkBWDrL5hEt/PjvrAeksGGJopUf8aJ+Zv23A8tGfmXUZp6+Brf3ZdyXMZmIWbZEnENSyeLqQ9t8DDu9yeJn7CrauZg7ubCtOf2J8qL5J3mNkjYtffytPAwSgaoorDdifYYMQ+QSI2a3Nu066n/+PeP7YmzxG/RivIrU2f+UVYMzgQBo/OrW4jZHdtKXvrdT9TAf8P/CPlbNzkC/2CzgEa9phB3lswrixlnG47chZtE4eFFx2IBZULdh7ocBwkZZGQAm4w+voCFUgDf4/kfbU3hxuEvxb13aZIk13+D6WpRsNwcO0Lg/eSAG8q8bcPxbC3TDvSMCWoJuVMwdBQTXWFwwRisHs2lHcnPG5Qe6TVe0/KqSs/PBQBqcjdlFFicOns1ExABsbjg55Z9xQsX2/vQs3t2VLKmggHAluuafDkwQYLzxGaFvsFDXFngHQR9nyGx3mmXrISVk2NjmDDSu55bjPuyP0i2iqAP0fr4TpKVKzHzyaR2oqMZldwotrsiwCoBYgRuSiLvM//pzIrFrtPwm4x5HYndA7X9HCSl0WG/uWbmnmUy6lsEtX1/wzdhUDpIzyFSA2fEmsjp4F0LDxzR5/EN1B5H4rHbVLZmiicKCWRFi4L90yQZiW8pROpoTVptu9HQM5X42MpsJrJucslQaD0ePYrIugTRTxyhH01Fu1MabL5tysznTTUWgsLIim8LVwW9dcedtu9jVG9plGyUZM8tmO/YZkBhyxeKZ8k/4RrUpk2kwNZVDgZKSxwzpmqpTxvU0EgfaNMSY/jDyBwDcV0AEQt0T86KariTUH2TIFr9brNnOcvM1MMZp3khXW/RtwRhewwH8OSAGPbZdx3U7UfiYyaYyCekKH7JwmyZDUpl7Zc3KPTr885lKO8RHv85MXznJVtTajVIby/AItzBAsS3G52gc7Rvfg87MSEiID1UDnRANRUPbWp34eqstEsmNVbdVIjkiWl4BNfYWNSLMdhOznrcSamv5UfLyLSi7OnigWWRV8yZQW4yusAZ7r68s6cvl8o2dn6lG/ABq9TXgk5VntuvG3CtKWxg9bclIXQIMugdU5Mssx2+HvWA7qpz7vLUMTyoi8wKtZ/PFhBmzwET7NVhZtWb2OOVhCeXgGsFi7HYOnAo1PGjKgIoE2FsFB7goMACWq6b0+/KAvB+Ti1ZsHeQ/N7drjeDUsqUKl+/nZp/EAGcNQHitZzqPKoBzVvJRSP/tV7ND4Hm1m4B1RluQJtD/pAkCSaqWL8a9jLPQsfoHHBO8GysHS8z5su2KicISIKn6C8z3Q9ZnZ6iYfiFqNJ53m+8Yb1Z2XsWtZlNupClyKzjqsrpQf2530KFCXmSk7khh0JUzS+9vblxdrSOFezReHadqtVH3XBQ6lqoZDwcsd+y0dZCmmfrGUS88/NgetXXFCmq6ey117QRFX0sWUfo2cK09E0XsXNjdhRVaWDW2DNiwCGQdAfgR7lXmvjafyB25DZJ4MEe+i2a0xer8/tlhotrieX80ZqRpeGCia6EbzMGY2QWz38IopAvEP/9ygbueKvKy7gXsma3Kyf1V5JbI4C8XEiNmSkaFxXCE2NikjptkL9qBakbT7n3iGgLbTA4wUYCyaPySOQo6fm7Jin+UVS6dgmrlw0Zly+vb1QXFyznP114h6yhJE8kYLErYfFauoyoSHBej3brjxnha8HGxVHVuaYuUbt8PuC7ypOQ60wlube2UgWrsI9sG7aqacsjCZKxmZJqFsJ/2zSxSCM37CuqXizKGDNsgExFODlgaLrRDmYMAG+z70yeKmhM9IN+PDNbOarR3mUMridywZk2QkSq0+Nq4gQF8+dhFtXS9AbjtYbfrgX1OB3LKjcYD43qY//tAuZj/3b40bNjrhl18WSYV6IYWEsH5QVxrFMnlbs6qAzYsdnm1Kg0XGOCuRR8bNf2VOiqaPJL98Y2sO3IglapxoUVc7CSsw90jYP/R8Uyt8bdjrI/GEJOgp3ste5CEhD82X3ptyVkxTrxCM4M1iPlUyeM0ZCcppldccTQ/Nw1CnPpHFtVOZsbwjvII5CtSrQ0j/eX0W6oRiyXShmwyLAf9ioL200yDupjNupCBaf+ibHWaHPTCMTTNpDwJ/AC8vzUeAydQmlYIfeFXHoufanbgqL5E4dfMAg4nPjpcvZD8y0EVO19X1yS734dEtneAjPiqWBXkwI5Ntz8oBrrEfUyx/LNwA+pZqwSdQpy0fuOrBbvDsf0PPaft/6PRX2NPqS4WB9ixleQq0ghpSb2DvqBPY+9poR6MTfEoOXV8lSBKNQMOMHfsk3nETITTY/X3f1AcTabnkZX/kKxA8xBYOFEMNyRfZKOrzGhSyzAAs+yd2crRh0iNIq7AnSyngURijNVlF6xUZz/R6+yX0S524gpbzxNu2wz49/Y4kc2ldB0El+XtpVvWd01/xtp6SsRCYx890XJ2WsYkbk4FU2/COA6+N14utAZPZn82VMLed9UXTT2TjifAi6r1jSQbI+kTh84xqMRX9s2DfFw9CesO6yjzR9DKgKir/cvQ68aBN91DPpSw1r4ez6UCOKzFT/66fQjwSDWimru7/eEGmYgASDJ13hwvpd1JaoZgmKtrJRHrLEYb/N/NlcAWyxq3LLl945yZvwCohIzs3C9qYt20zUAkin+udrGWBwrW+E1eAxpMAtjRt1xyUzBegoGgULsU54Rw8YaMuruYgSTvsWLr9GMBlE9sZhIdjO7R1eQURNZ0wTHv2bu1fvOpoDCsru6qLU4wDQUlgGURjn0zkMdmHl+STvEm/wdnM7l0LlJ0gmer9fNLYCdPK9ZVmGXQonh3hXfCN6zhTUsSx96Bj5b6BmJSnuBygHWZ+TktCUVVhzYioMJDLnvWoMnxI5undCp5Hpakdbl6Qnl2Ha9NkX76mM/dpbL2p2ZcnclyHhYkFPbHMNi2QXvlZiaq1U2RXn5tUgax/4AzG/xp5C2MYaH2BfnGSCUGNYJmaWI080cA13s4NwiDrUoRFuSkbGzh6K7oukqhTEoSBCdYnMXiPPrMG6QnVwkU5I3cwrCnsUyD9UprJc2rpJOBOTT84oz8HLy/f3mWr+zp59qWqdfKOCU7LEfTzEkOWBo5mr0tl0olGbpYes0w83Q469cPcCRRC2cSoAKSpf52L77RI6fuMPGsTTFiqWkuG8SKEnlVW0cLMH21eA+scqKSAuHKvgpZ9DkZRigfZpOu0CC6ZHJoGuJiYYeCTu9Lu/yYy1MXu5BBOsW06LcoP8CAJzPT/CGL6fORJAF6vFlqjXAB30Qr+9HDqh9mjwwXuCcSiM7V3Y/xdDFdaLHXXFtl1e6QoIX0pbLY8lcG2fqUSoEcJD2CPFCYqWq8YagDgSt3KW1/3KwwKslYh4PIDDc7Wfmxdn+wa/BJkLy7/RPIRs4L4qSbr9cl06Gg5I5Bv8xN73DP+S7YFZXga5KhXICYKVfvBTKhs7sJIzfWQITM5uqmaxwCxBm2EXIIFRWFO8EuBRpCutAvDu9edqF5rXthHtYnVSugXqEF5IdFlJZTtyxKGvnOmkrBHTQk2yCEwoKFXwxW+YlZJqk8sX238RDAydDlECARjgEr+fz5KgDbT72i13b+6mXFz4fMJbznKYcevhHrimTu8eU/ST3jB5ueUJWifPzKdRSo5SFfVqkwhCUKs15nWZImTc3SmShuzzd+UmTk8Z5Cgd+YHyUrB8Txhx4IzlcCj2ANk0CE/CEuVInOfV4n2Th8Aq5Kq+uQTJAhDpzzeD2cNNcAAo4zL0P7BnfT7ASYCUtNkDZ/tTiu/dRw4k9ZGR6Lslfo0y76y3bAVbHkC283L6d4suHXRcyp2q3vcHsohOBPnvBULQ5g101C5zTmSBhiZS98IAlgTqZjND06l9jld9ODuNsQvwuxPBaHBEEijBA3eWO+aBjQ9azS3EjH8ZdCVN5g1L6mvzrNa7XlY7ynnXcKm50od7yQlLbZt1M/7DRT27AftUJPr7laqkxnzdi48jeNUudCmoksNDY3CLqdslqcnH46Zf/hK4wFtA/m8u1zoDhLTSfitDLEA6qAZqUupRgmAaFqoqmeytGelmcdo5Pk3kg573tafO2RkgLxp3wRsMYKuOvMHQcqP225LPGa+AWrGGL72ZIepOeftyncrnN1q0Gw7sTD81yzJT1aBHWnwdCiG+xGCa0uO+8Y85eIM4/e5BHKXdhPlZmsvytVoqofw+DFYl6KpFb/MffJVtU3L7mPK8BGBee9VD5QHGahQJ+Ba2RXtJy/3DCw5j+aaf28YpNM4dn9GptLzCkSSZRzi+1RtxS/+5kS7mXVQVpJYivRnaeciFw0ULLyrfW7y+hZaYzHZU8urlwCt8lpLvDxAGh35C131jbREWX+gvQSwi3xJZ+KZ3SU46SGGpbQQb5nTHabvMttDvy2XeiiVgZbYs2NV9phhL/W1KKNZtM7I/VUz1fD2pwta0C2DjtMsr7kUp0v3Ue9RhhTonnY7QkkYNIqpcim0jREVxBFhwvzKZ6aIyKkQzuCeNlK9POMYbdaIvs2j3GggzyRdL6AmFzyoW3O1UNJknzV4yQ5RDBFjpC7lEXFAs31xF57QNrogm9xfKlscPurwCXrZXhepg5VHJolLLeae9e1GdQ3J1dw/ImZvlI366W9Zyiwz6THMMMN1fNTmOLa6r0viAQZFw5Y/bHk/bJxFtnA54JGSt+0bb1xBGfASYM2zAmAXHXw0yl26mIhhvnM87dq67JYV9pg5CnwRWPfmOtYVJekgdJhAQxzp5LCJ1s6jFtQgm80HQIhCPECg7/4ww3tEJTh5Uq6X8pjz5ciEXSke9ndN12akoXm5nUCiIGux2K9GlIxfA3D8aZREM/Ll3PGZUWQr+vx3RuY/7qKGKI2Plk1vX4RMzqiDdMNP6EWJR1uAaD5B5S80kuHbV85orAQ+nVTNv7LCSUkubfQ+AeqfKvjJfHta5oUa/DAnoiGVCCdh/lJppl51d5osO9dJKKpSQqybBJcsKBPUm91ylLXg8QTzOnmV0q+iCSkO6Z+zYM8ZYvOj0wDfZTJxNptpy+UUBSLXmKnvso65VPihxx4i5RjUfsbhgWH5FuDZxGeBdk7i+t7mLQWZUONc0qW6DU1cJ9NYUTVcu0d4Tsd69GYGPWv+ccuHbHCsPI3bm6R6fMcFOdpCpnqFMJ6GxvQMfwm4zdinDF0fd2rx0Cpw4u4XBN+3vY0y9yax3XUIRyGlb0ovKr5D53SZt7yQgOz2EuwtqCqm+hqAqTQMXcya2+64nhB4KMlQ0CL7YsJv8xVPCShBU8RSZUU7zyWvhgJWW075HhJin3uwt45fDTGkBZTAuFkI51VoTNJiUUHPUJ8kWHRAK8uDOTEjTe6YCvP5SdW6zXTzfercMM7Gzu+qKSmP7Tv8nLUveISBygxZrtJoaizx68f+idKNG+s1N/20M+lY2IyhMzvH3APJLBZug+KY4SvHwgEYzkrbxnpdImNHeFYktUEM02chUfLfh0gP+OmRdQNyafALgKzrN93NjlUM3lKMpj2t7XNPG462acgeOd85Cx5qR26sJ2O7LSsGHgwuEL5CgNV7ZSWOxzRNsO4QGYoWsnCkjZQ8YuOmeDpMfrO0psyxR0Oz8/hUjetV0OSkm14GyHkwAdZoN/17vTBFdZQ5NGa/eyhO9z7sbhING3b+xx6uDmH9+xmi8qlPR6LQd8R69mhNwLDr3qfMlgbowc+eJJYZB11/xUBiRCh4TPtsgLBF3XBAQD0knNxTxnS3Tkp/5JFOdWQ+KEH8DRfiXun8lSOfIeP9x135aoUKyobFT/fljoeMcAyXZsk4LUEnWQxC4Bw0NknEiDCIZfZfHUVK1wYA8oyHR/r7WttXlQB7a4jfxFOCoLgm2CfhAuB8ks/zFMr5Hjfs83sjiJXV7rWqzu5HfPxq1ynn2cf9Aa4r/9enb0CMhVhbBI/XCoCr1Oaz77R6PC4uveF/yDzF/VHs4UbGXVeDVZrV71vV6VUSFTyUQXoTGtdxQGZ4JWMorSRm5b4jrciPO7NDSlwTqFdopTwHsXQPscV8RoAVDO78vNYFCaWV6k/KEsVf5hljZdYkTZqNLSLwgCc22eXiC2YxmKmWNSSuUbe63kAfA41zJPl62OyKNPKMQ8G7Iu2BOPHm/YPXyh7iO2fJK0fPuqmgrSom8FwQPRMRLOLJ733VWNMsXKpeSv0fhOSZazDa5nNtuzwqPve8gPnYjljPTi4obj9RtuETEM9trUxAqsIOcat7UEDQxjjyjAxWyRB9p+jMmhZlYQXOlXGu3yueQwAEX/oWRBVRKqaHBPc/UHTwxdloXlCXJ0bWw9Z8xcFLxk63VFvRnovIJLqvXY9CKQbRwx/HYAgAyCNNQgnzRfKFKif1VAaP4BfqZpP7V/tOw21a8j8L+2x/zU75goehqeF7V9pSTAL0rbJBhlyPKc7KnXfbetUFMcMG8ysTUdffdPro9MIVREvIiYBejhTAnZ50CrVCeTuL4H6tSQGEkwH9Tr+U2+wKEfj6olW6jQX5iXBgt2ZixT/yD5seII4h0GoSLWDo/TAuouKXlsteCaT3bqtPhH+1hA8u6oseJpcsuPmsKlqypvngKSaJ7/XSC1Rw/qC0ZfS5PdWtjSd+gW0QUsSkn6LJtRu6a1mZzWhyTCNzHG7Z0jSmQVNhAvCpFaHdhoO/k9j7biliNs9xTrrYc4EUE3nowki2a79FjqklLYwdrGkLKXDfV1R5FT29tbXDxoBIZWzuMwVWiuGOTLDcWQOAi8iuyzOlmRGTmBvTwwyUzpAVKdudY4lTQPOwcjs4Ev63jvoSY+ZsSaBoguDTLfZUCw06KTCkOTtDLhD0HbwI0zy5oOVuW2Xri6cuCcGHJrSrRMhQJS42wlU8VIdbgpXHiccV7zYUjTHDb2ViPuMbYjOBvadAsMQ9nHbnbkRFs6BlPEENacZWjVoG4EK+qzbRSTUhVCz4G7/MAUD+WzyMBgbZhFWG7Ir/JxeizXtUqVuw19xoko56SmB17eHahtOKd9Dcbms4G0BG2xSet8RTaqRfylU8agyBvG439LVdad8QxvGcyYjeSwoeG68zb7KpASOpZwkmnGZ8Vf7JQDVJx9NvoVI6L7AskOuW5XqJ9IQj2cvO3av87PJL4ncIyH8k3z/gl6rNOI0ihP5fJmkpqg+lpJ1t9hA1D5+646PhyO53xONU1momrrSGpXoGdXXET3Mnp0V5N97cA+hMryHFgL7Bf2bpKpUpbo2cF4JkaConT/Ub/yzi5JZVfSqWSnplw96HwiUxPnTPIHxzuk3MBeVcG+y8jOA7SWbHwWdENhC8krG4U/R0P+Ff98wIUnIGBDmYzvpKZhpqj2cF39IxC7GrgA+jCM787E/9L1pwGe8Nw3pW0Zc788Kfd2lw+RLZ19+KMH7wjUg8QtDAD6HfsjYBb7rfDsiB88UX/Wx974SefZdYbmEo9cl0/ePNAjlWU/B/mpcGWMPJDm154z5BgVG3P6tlAiPrDSnbNbKNrMKVh/2wBvko+ZTikMAuUZ3Jna7ux2b15HYC2/3XgBOcpJaz1AEEg3fQRtIzkjrryEmHr5r8irKao1nmncIIsdSptJ3UdrT3DLflnk0TGfFPksgKkCbIS1CS1TNLYds72OKfnmMK14/+XZJp4x1rrKV8UaAJpVd6v+9O377ZX59Vnw9epxcMmFh0nVzZ0bo7UD6SOtx6ZGGKcE8FOMWuVHX3Ec9ETSAD61pINd5qkbIA8kCqxfA9FazsexBpqaYgiJNTNEzmveTX/+7GGLWKv7V0wwA881HMvlXwjxEoaDTUPQ3I9sztJH0OsFgUANnaEVKaCcVpJVyz7r035BgbykIflpcYqjuANcj3pfqSAvRFhwpPF7T9eeW6a47dtBHM9afAfdJroWjTotOTJfRsEsGbLs2yJDve8+hCrr1IOMb5bSfXYwfnbcr5PKiZvWsJYHWxa1bJWi3pmaBZHo1Mt0aSF715RTPFbZZCyITS9q+kvBUu5KeQ+rSl0GzePfOVWdrV2G8QQbI2rQkBU7529PnRyGeVTaXhYVDE6prEOOh6Ya4E3jIHfwmRxsiBsfSv/bP1KwlqEdBBwx5QJGYGFZQbMdImLKz9FP1RQMJppfDZ2Bt01YUl7ASxnDlloqHF6mmOgHZhA13usdFxhTlbnrKVL3qqn2OuCB7aTV+Gv48ubH3TjrR3xDyXiMCOtcplMs9m6PnEXWiMYamQPukRZKXVcbLvVS4Vmr9ziRSJ2sYckOirJfGg/SDK+A6dIVgwnFWIMhL8FtPpdTibXae2aDO6HqchkS3M414qjIIafqNb85BRPRR7Zst1PogStvocRncT6Erlbf8H7Jqabbh01l6VWSVAKlwXJx1vsX3Z0tz/v2owblAthCubXPQm8WMede3vEp8q1Dl9HtD7h8ADoPHx3twBttlDanc6b2fy1oFjx0dmDW99CbaywQReh/aqLh8ROk5mDe/iwSR3yeH7kf3+gN5ikhFxziX/VIK9UAZtD+aqriGNED6zqkZqzeB+NfEEzngdMs/VRkKpHbDsPdB2t4xQ2RKootrHxR5QHkOO2fniBYebsoPBE5abs/SZ5EXBdqsK4FLgJkpGG3wA6Sd5vBpWs75g41dWCDHyz2lT0lCinPBLLb/Tbr6MzjCowF8V/ocdpHDkFChBI5Xjpdq68e0Yr0iXbK1VySw0Piv5x7kjbrCuCOU0dpaz1EdWjFZKR3itfpdWrN6G27mD/GqzqnKW75ki2+eSxQq8ecNi2tqWQf80GQJKuguyVgG6LgK3XI0LEV1qGT70bTlmarKfkauH5ZP4sY7su1UMudR/6QadXrF9ZNFY3/nBCiBZBdjMpPgMYdKDHZtTbSLbKoq3BeX6lgdwXx9HcCFIM95ZBc6A1Pyj1GufDwt+FYaCSPkFSnhaDcAQidkBIOnVp3pW8gWBi25Zg8zFqE9lm4m7tfZMBg5J/6emGI/JQVI78AKNvwxUkyjbofU0cK/B3jV3wKgz6PnHDKoh9GywE20QMqGW0Br7hRVyyVz4YRJru3doTSs6zESBVJKggF0816QLGweHjEj1Fsc3Wnx/juHEGkUQnz8hvb7vUlfp4jXwkCnu6uzmSTZqWYLJAlgzi6U8Yptg8TRI8sMSu2RyqY+9A0uiDbYqeKSqbe0eeV5aLyK9UxXncAnv8mX8u04iYEg98QLHte7CAdVW98FQmzWbqJ+07k5jllZJ0znmqsURftIC91gxUmMnop9AwJNXo9/HlbX8yecRUm20HoYtV+Ah/AssUbw6KYal1F5y1DSkR6yOCR+XcQZzKc3PIofwHtODWZtQCRDGr/eFAF/e0H4mYqw9XRRayXDznsDTadtDFL516ijS2gAQHxO70TacvirGUHXlnj7S2VtbWoV8V94qIvZ9aMtkM+0UhRYjyU9uyt1DVt4ckg8w6UDvXaU3YRyj74QOC57YdzSwZSY/6kwfxbRYv/O4tYExLnq1OubDwvrPeZZwRHAxmpsqcAGXFDQy3Gp6uHhVM3GHezkk16Ub9zbwgDez8eEiA1eNPCzVGa27iJ1WWcKQuguZd35TXq5Ph1loau4n/0czC2TczIHVLIdrMo7EYpuglzEa72MGf6hJETVUlbJFdW7QjkHOK5DxJY4EYizQlrLXwagxq4MTVLcJBuTHRJMyzaO6bluy7uUHMvJ+o4WE+8Xoo8edYIEskmzGtoVuRKvDRH/nCnNJdUoXnVpYaTqiODcxFIC/CQgPtig9iVvPfVszmgWn0/ZpatSNUiZNXAkAGCLZIae/xeMpHP80Q7dtbKvTHHrGtH8LWKObtlLkWLR4KmWXdc43++zatAnOJ91aqwpVwk7Pwu0nIDloOJ029IbxVIwLslgNoW8uaXpxSSU909Wmyk/k5gtV/stXoyHjKJ/sdkAVm/HAEUdrACYt7pkMNltLHXoSzBG+KcsMO4Jop+eI6JJV0eZB4hKKX1l70PlFZdvh9livTtNs4/hverKEBHkbUBFTd0/r04Rf3XJLCs9ya7d8Zksntm6yWHpqMNJH+y83gtFsJwvAO2cy49FwUG44F8dXz8yB+eqJuI971Gs3YaMwCPibQERf20+4e1Y58ufAVma+DyLldmvgRWoYhrB+oVtm2CjWmh/Lb5uwMz2qZTkFHHfp33dCVAYsa3vfSnJoHsVP1EqgHZg4gER8SSD9/VlLhfGmdQYKtIJFGu1Ov+15QpeUlI+zr7B56KZixWzf2PvQXgrFkKLSwRSutn1/GKRVlBfSvkiTRLCZrPRWJ0jlTbugIFhqd1yjL+NsjhBP/GLIXlE6G+9fyrY1K5ZxsqwqGzSuDWU5p0yw090cA9wiFP2gCwcg+vmua2/2xFVhSX1zFIB93syBmu1YTBMOjjfKvbxB72xkxXF6RuE2ckMHxu5kNzY52JF1HZfHNh6JFPJvrsw+v0Z3fzNmKFT+LM9NDb4ow0oLCtslXx4Dt9XZFSDuXnv0dXHzdrpECSWwc0JCvBmFTyoKEgqrT1L0OkJdlyUkSoGloq72Vj8/le3b8kcFJ7O+pcQ7uF3DPyfZTJKh8TXqtXRzCsJAAhCpYBmh1MyZ0+lQofPaCtxYaIfbsRZEHdfLLl3szvqB9bOZMH2v6jKzRuVLgB2GW5J9sFD4EwQ+YlfD7PbGJYMMdk2ltjxE9LqCiauZtHFyJufUuypHU+P8pqXHP4RhOBXqehQXtf59nb2HfBz+tr03CLyNUIfj7QLqjVzTk1TJtXgSvLKe31dFCwZkGQo5Se+sNI4gasLZOI1ZRWXNGblvQqRwd1JhNAtjiXZUKrtfi67Z4QPkpeXHYiHeT6/0n7CIg7W6CXgHIzNq4jAak71mBwpqcHhy3bIKt022pE3kifAQ9KCLPQfW36d1yKTrZ4+Qrqq4+XML0g8F0OWParWD22qq3F3cBHUFulhEvv+90oCyIgx02diyUrHJTvfp94UGcc8Fuztdr4upd5GRpNFRP0QztDbMDLnJfLW1ymWd7t0fUWBZHwVAWUykhrUBYijuC+Rg4TLMXsRdUfdMyykV21f2BV/JB0GwqXAAiFbWwyVgi/KbRbnZ3J5Q0B4HqsYKTAtMHjf3DmxUaFmxlNxCACm+xgczpz3B+GDIsG9IJRWKTmIrT+kpP1Q8L1lINtBeRrJfWzX9dcE1L/udOsx8t5KzqJMffgBOKVic6f0c24RSvWudr1322X0q3tBBLwSL+LLejsVXlkIxxT3HobhX7sHBy0zOocgzNglY63G4veSmIMN0AGQd2S1Cy/71xybgqra2nX9wPgNNLTEjzx/W7c9KIjlSfyomJAd4q/dksQ6dunj2qOarxhfDpK9Dr6QbfX9vfSlryP8qiIsGuBpxa2apiQ/3ha8uiwbGy2vapWVC/zz/DmTNSNkZ+jGdIHm2jRUpG1M+X/x20TFuOAiiON+bNZ1FQ+r7fC6XsNXyNI308yIw1E75SC4UI1ZETWI5FZ2RQuK12ROiFPyJWdKJUc+vcMcV5gTrKfvUKDVuWCS3rGqH/7Keof5sRp6+/k/Y7RlnBU140HeRRX+zwf1wVpOODVt0LKdxSKjC0MJ6/fSrYvJHc1op7kxsTFUX4BvjyLfSjIuCWTMfEfErpV+Z0BX7Wu41ckl/9BfYaR31Qdt3ABjwhh4IqXgXXSTnqavjr7CqOfwulqyd/JTQvCxN1gLV4TI4YsU+fYL2Bf8Nb2BM+efavHGEyB/7Ky5eJ3YkvVWqnShLvp+OD8bAEYrjdHB6tPl/zQ0QsfBncRkv2MMvrglZmM9oXrwawWVaVZwQSxOZAQazMzRr+xQkwuYPjhgCux1FxjwK71nOoF2GjM8KNdQV+5jAJsuPonFQcoDj1pgMuBLEy01JISvh9qhmONCyD15dz6iZqLDJOdBgBHq+uneuJoNl5ZYB3T32V3vsoT7Q8cb+FcbOu3IBRymRNUcjuu/hcvvtnrIyEcsfcu4pNPWXXDamjfsLtPK3fuuRXnRv6Qf7NGqSbc/lM5anPTg/rOQgCd8xznohvlxOcIWxpuo3PUIAIA4PJrCK5+cBz2pwZkS0bxG6LAoVmUQVykqEpe+x0otEyUwXprllOBn5ZyOyFaR/0+WfPf+vJkMTLSOUnNrGsqkQboVQ6xWUcgU/PDCR/zIcTGkcwlsc1SxG/BFmK6dqhTjNJMYmo0wzkrBddtHjE7F43AyHtTG24DEpRMclYI2lzR802fUXOUpcFdXHbQ0gV4Ovg9R7AJwVaHKj/sO+ir6AwT35itdPnJgrbrP9UiLBUiVMz6yAXLIf3I/4pfYY3T15C/BuyUqkQ0rGK8b0XFvZAiRTCvJ+IKL11hgfuzCF7kXGtFqv3Onxou27VL9Z1B9QTU1x+N6tjdH5Yj0Gh1bLPaKUs1FS7X23oh8jrenyxZSSx+LUE+Fk7Jkce4I5/qET739FomXnKxXGiTTXIlK4BVOhuhryL/i4IhzAWlem8+bMP8UcBCRnkwIph5xyhDREs3LcXqzjULlY4zsd3nqYLQuLnBIK33gnt4vk/OJLiKIv6bLGbI4taHkCKKSYk4E/wsKfLjyLYT4BDEfotKUbDYcBKnvSSZEv6VZpuTwoYi1Id5PrF6SDBz3tUqVuStdl+0RlnXggoySuUPoTUqNYQ3xszFcjSJKFgIPoaGLj0nuIgP+Imq9pahICxl3G4OPYdzFMB/Za280umMgiuEnBBjwZUoFZDAlNyWy4NU5YZKwh9sjVe0U0tsuoEBQLjB8musVO2Ia6sPvDEPFJXr6NmGBFhU1G9P96uBySHISofSOGy1l25TJaAvtQGo36tHmMca+/3cgGERfYoSaV+jFJ/59SOiF0CphbX0X0vvck47TpXHwoM1Suez2iYDX20LI/VQnrmIXBdbnsLxC2Eoy+tW0U0haDLFfU/UMCQJp8CV7l7LNWebCAYUDnLCKyfMPDjTgGf+L8IsGvp4lRBjga+7TRqNVkoSCU3fFPLmd91/vsVi64rb7H6U9rg2qD4md7w0boD1gv36cw8mX33vpQhauM/Nsm1i1rwP2hXfY2NGT9fLmj/AxYW+kFIZMaJokKEhk+S+D5Wh88RQ6HD1HCNkPsU5T/orb7d6/rFXFrX0RonyAY1M7gyaSeiOc6LJn+QOWnv97CB453wQHwxfXx39q2uMLajAxeHJXAXbv9Wr5uVH7raOhQy7hS93P0Gz1626pXr/P21nw6koEbwdbaYB1XbcBxlcdOt0MxQ1tZKNuPtIBhsb4wwkJWKWSJ/6N/hUj1B6JGCDhaOcbCobS2DR6XQfwE2QLQA4jPiRhnPH43DgfFBg0/AK5KKWWFSk4j/yjjZiFUS/tNwhXAAbg4UT/RU9f1MERYOh36SRZtYHlhS53Sm3hO+rXcnReuxLyXJeCuiBpBFYs4YF3/IHr1ih78mjqiQ8iv5Gk95TZqtl+DYHv9fe9vv1B2doDjgfnG7Re72FWkY6E47aAOBHcCdxlWrIyz4MRxYWwF0YLDuD7UhEtJw+aOW3yawdVO15NKXOighi6qPKu6+KcePUoui2q5RAe2QZnFuTRTWNynqUjpO1OQGi11TYlTS62Jut80t8j3dVF8SBGtfqqVcTf4fxPYnqDKukXtn2v35jY6lBHh+7Q5Qrqbl9xWr3Br6bC4aygX7Y6oGf7vNu7JmrRGX1/1WcmSF5OdXX4HdN5OeYhj6THrnireQmf3GzXT6PrebhQ2S4lANfCGMSwPtKmrDgOfFTlW6XKPhtp3P1ijzwrgX41VLlh5L0yAvrAPFGzfKTrV8uvYjY1nG/2H0alJ1hGfa9laP0ZKJD7TJiesbiKC+kLZXNLdcnM+YDMmhxxq6SJE963TMASsIjgLB2yaQK8YdqD/PP4hEAf9BF1bzu38Tfl9cndCgJJ6OW3CCWC2N7pjb9qNMIbFKCinnUz9rp0Motwl04M0BfUJoKSfuNFlv+0k0ywiijeoK1UHghyl2ItPfyLuT6NTpJDzd8MjtZnHo7XRrFoplbCOfHkU/EzBCZsYV8xqk+wegTD2le/5/lle/igF0gz0dWYXMdNsS2Vf0FGRW7uyaioILQVkvR3R6bukUz4kPAF38G6Dvt2AgmKXxhnTvFet/SjegQL69wkzZLUBEnMhg55bR0kyCk99MdFk07IXFn2cklvhv+xTkXoDfg/Kf2F0nU736exDuBzTrcLcXmxd32XJ6SFsuT5IH/i519irOANhoEt58Vg2pJNgDQmHBRA0vHH5/WdXcyhGmp5nguKu5A7wGvuDYmRBTHyFJBM4AugVIEPGedxwrNXcmf3hAxfP8E4KqRAuc+j+oIaUDCUCRy+fLwf4g46TkvZbTyTkoutpz4s4D5CuU4nfipVtEWVNQD4090zPObA5+OhvMJo1hggrgs5ENSEMCLrb671dD1+g8UriLFJ1UvNXRTnhdeYZLWEdI3PsY8mwDUjITTLX3c1t1jkYSRta8vLWXu4iQOyz1BKBzwU+o3ivoCWflwoFubomRDWAjgOidL/Mw2lvsMQvKwnCwOfRaXdc7OhZUIpwNYxb5Top35kfcfsilDSmTlDxsYuwx2vwjEq/9zZnDBMJp6/cBMyoVMEIiRYWUvdiYw0g2d1eMLpVJQEi6H6CYKGFKpAaD8E/fA2kfzDY98ZhLCkPhh8qNE6hbPmp/X6/aPuthrfyThmu+XyMVsqPdXg+w9n92uEbqMi7hYDjBJNdi0VhwCVF92ZRH11S4eQgf5LSfKEKulNBsDMTkWjXx+KxXHE6WktmZuf8oA2FvTF5Mna6zVD+w5q8dG/qudSKjPT1UF92QYnpFR+xeXFjnEi11XbDKILUPg6isW4vWc+AYM/ZtHbwWf6TXh+zWKJP8bGfy268CtKrdvA1bkXQC917TnsnMSHRIx1W/l9JFNo/YvEvIZJYEBoZeuJcxsoOQ2BRiGpF5H3BDAl55aiq9gx1tDg7EgSDLa5TPPxEyiwtdc68G67RcKc9vCwmzc/XBK1j17d3AeSb69FqTIiex83AAhDWbox06YX5ePBZMUrd1u5BQlecBvrGc//HbHWsfQTJJJrnlVVAWUcc1gBH9oqMPTZKFAr5GX57D7ySDIYpv+jme4wkSllc6Oo4h49/U1D0IZN/U6hUqCJNXAnYY+OFQftf3nkZgP1pMQC/+oR9lCBmhxFXp2MWDONQqJDydMn5pl+4xaqXPtNFxslrPf8t/w60jg23J5fZKY4uknhn0sdHEHq1BUwHdBs+C6QtVhsPxVJIS6pDSVQWfMPGSQ+FG7lnvXdlekClQqL6+FCl2N0ua4mezziN7Lhh4QYFz7DVKvrizZ9At6IXGgscuYKGku58rnRi/K8IUU4dw7NypEjqUPXByfeENDLtVu4tNXn8XBFA7tcHkHjGcvB75Aw0tPB40Vtd/SlUoLM8grXVaYe9THZuNz690AP5d/Kek3OcJ/7RVf3tB7wbJagqGPBaVkCJeDMjGezll6MBlP8kgYqgolmLxl2wz9C/g8ATn9Or8JwIaNRtzw8Vq8r8Cy2Hhi85DP42TEZX02kVEgZldPPfgPOS1SZK4+IBkpsnaZ4dTRQTzc62Jldh4/mCv71njrp4/blbqy0RlFcLF38Z1Re6MzJPi7Tk5lcoN1yvm5Cy3/6wS3KF19KnyvlIjl9DOLFQwkn/fqzpsl9zus/TYF9Fm6pGE46cdNJ6+c/FkoNMtpH1Ub/znB+QNqMpzBy0lGcf4cL5/dTVpiUAqUkDU+Fvqzv7OeGMMtLJZ02DVvGuXr+JMp0sdYV0f2WnHTKsIeNDeXm1szJLyohWsuwkwe1nVm42ElI8902DtiKNiQ5QqzQNl3E5FpRiGwQvRtLaOzDhM6hV44TUeXomW8xGkQ78KzyQZRbWYUHs+IGcnajLuFZHaIV6QB4KaEhFWcYeMMAJSMEAs8kpjdc29FSpqNDRVDchAIxJjnPauGFGpYgor7y1HxJxUHs3fHLrThI/Kr4xOf3X65KF8dmCkPJw+22z1JkyVhUxfnas2suygPYZdh0fCDndjDVT9XK90lUbAaP8j2WyQijXGpMCoGFvbY2j12CWi3TaD31JlzRUvgjn/Rd8h/NRGZxvHeQG02djbKyVfpYTlPpCJLG+oL8rHV0yTxEBJEUOMmdt2SBle6GmePuYWyhMXSWl3YlvQEVcGjYB3YoJRIyS1UHkpPg1MbUBgJyNkD1fHP7cmT3YqCUsB3NkNw2MXX+zkEaMzkHffN8LSjJlTwdCaDljP4X0r3fFVkUpOVE0TuNnrh50yw12ezbL7DaE/DIIS/VSu8376EUjXU6ld4Wf9HbA0q0yio2bACTDK9UvtX1kmyNZkIhyu9lxg2TlDIu9ZjjUypuw/e1XkHN51bLAA+NXa/WXc7GO0CiP6eUP380vpJBUHXmDHckAz5Lm2AGJc6b43p38hTXEHMPGciXURVsPsZ5VGsh+O7Suf3uIvqvm/icPTfQB0lvYnbtPPmUCQHYkzQdIva2nKQueDR2D3Th06FipZwZU9ithyDlK/tJXB0TyjNCcgnBVK3pIQdCbGycgPTwfCzdwzC+xdoaKnHb9G2b8BYNosEdjc6oMFzIBIVyJ/5ipsYO6zztl70ai18QYCKdMvsttmfgA57hvwCM+M5hyDc/EPa97x1WHn992KE8ngYIiILj14RjTQVRp5l/+59gKXUCCQZZ50oscUTpMG6l9DPsdP79/q/dqklhTqHXq526hU8tNDvUYe1cyb8Ev4ztqJsHviUh+R/LM3RubiDiQCt4fCcxrsfieew03bZQWlhFg69O6doFYlFaHwks37AM0t9ZbT49nnM4fgYxsK6KDnelBhqCCiwDdqNbsh1pDubWZP20gEyNxxPTAFb3jHCnDx8njMsttnLHBSSJlkPSV+dXW6LbZ4ICU1L1PYYuRyKoBxDQHoYyCmDoUgJ9HIQH1p+iPpI3sFcznOYlsMMZky6oh3KFJjZo/RZilUlwRd4oJe7lqPyjOECQXjaswFwDvgiHRrmf2cQhPYH2FnNt7KWveNR99CS2IZIh3Z4D2gop9SqI4INjDj37+WjxmtqF//JKk7t1SSqwzM5q04ZL4wHe5oNpPd9Rnkfpz7z6+bBTJm6byyBxWFenp+N34/zZJbIau+0JeX91/B6KVVmzypEMOfS7FG+H9BLueVgbZWnlTXQ85a9It+qxAWtG8GYz1t3TyUB/EeRMg9P3NGb4KQ1zd8j60cN81nCiWc+11KM22zC2DVUAgEhS9CGii0b2wrXXLJYtaaPYzDKwPMZLIsGsLnvE0K/HNf8skeIJ6Elswzx+j1kMxpYwJKMuXmkVXXhOG4PTCKiqbqNFQFsA6Ynw2R5vkI5ow3kDzSYcUprTA272IGLILzMzJ5OSWu57iUWBoVlwXFf5uFUKh7k1hC7o25nKsisCGYJFSX63hzKaHsCB56cQqa9F1h1B5xVKNzC6GofJHPeeJbprMdnmrFJ+ZD+ffAnJz8OPAVdE84KX535gSj9RlxlOwlGpX7caQcZ/NLRR2ahdZzutHq/BVmTEakZrYL8dE+0MtH6zmtD2O6F5t0aco69QbjOvq13Pa3TJatz08JHSZ5+RQgRHd+Ktqq6u0WpwXNQ2hae5UXnZTtzw3bF6l4hsq9Gm2p6fnELkm10hCCwm7ifBxtS0vgsBdIgUEetfX52Uw5SKtcQAwWMgZlTXMICDTTbEyvxBDGDe7tdOm9Tn4gUR8LlkhruceUgmD0Zbu5lMx+ehv+C8vX73Lo/ItCs17r+K2nBjLPXhRz+1fa1rdlBZvbK6Lgc77gDagm1A5+4CiQb6qI1qDvgBxE/SwhexbO0Fgw153eDZUtAfntncB+AcqF8DT+zZdj3l7B4XP+lwia4YM3EGsCCGY676g+fcjPEOui54rzJfSb5wwBIYb8tMUlMZ88dO4KTPXDST4CsLHCPVNhSJDGyTg8VTZphpTLw8drulJyMOGRQRPZB0mF1yVFiq2A7dnD3agJbs3W7YH7S93zSEM7G0Wwzbgo6pkDX5nTJL6LlZkoL7/YFLS+B6R+1bQ6YaH/33IRkc6Lyi+77jVTarIS3O2iN747Hr95KpWLi7aNGjAgEve6JdKHYUoD77aKCJURmM9CXb9Rxyo2QAaS5xEEJeOII/vGp3Msc0VK8Jr5NdGHkq3w3dZttt0mVBOWtms9GbL4qgjVxhmf0LJY/0W98lt4eOq/BfVQTRVJDu9ucCcitkUmad2Tya3tOf+062ebIGxdVzFyKyGToiGKwb17vLEI/xtVzF8/spuKscRv6mYgU1fnoHquwHjkVcZVwyLLmsnIbAufVo6X//6qnG4FNTTBZVpReOB/08YaFAaNippEmFGlAenWezPBr5nPag3Ote+1qR8Wm4QrHvOkXxt9ra8cmZTZC80TV0KsKbnxKjkROk5UFxYgF5udT5QKp78cIqmhv3RzScU3/P7atdK7E1iJ+yQULent/zA1IsqeRimo673GOMAvgh6jNTqux73m+ujWy4W5p+Smm99IvdDQW8d5O+3oyiPUktni+GaKy14cpLEVcK14fUvJv5PhzKzLQys4ImJMvoPAO8XY3u1ZUeKghqnioA1HcNNDkZ/z/H1+E4XsqX3fCZ4SXyyH5s1K3DDFAJ93tLCKcCKlxQsM98WI5aOZxKvstZ039vFeDbMjcFmV8xGabwmCHRCcKyAjf2Ncv9SG8u4kC99dW1+lJk69o8lEb3u9n0ee4AoVPYJ8NFcSqcUULVfmThhZnZHCjmsrD4IEh+xvJhhmXf3WsL7sDY00YeJUelOYJV2ml0cw7dfHtH+SLIjD31QUvm/JbFdnWwYiOAtC4ckxvoNQqUghuMc++9b514szbUL+jGHKSmOxRAOu3RsmlOEIcH6/ma0mXmz1I5e9yQigFAb2mfCxVch+OZhdNfyg+4BvPZzY9oopjjs7/efKdoxMBMBezf/WETAtV8lSUFpy2Cdir7m2sXbU+5Oyz6ROoGrffxx5Wl7TVvCR11Cp4QYrAhGtxXSp74qmbKfaHn7pguq07hGyF7PGXiJyRtL/63J6elEmrRyTZMw+fFR3oYbVaKVq1KK3llnij2W52nhTcod7OM923yZQsHyRmDZ8vBktYjJwXmW11ag8fs1KtOrfJpUZUEAWYMmT9Hfj5IISq9jG5cuMCBYmdE2Rj+ryIh+0nqX4cfnfwVWjaZ1D5Y4b4FXyuZnySNIf5FwvcvkcpKkDPsDMq3JYZYzH4RIoofFUnK0w4gW4QX//bHa1B8htDj4CFpHYmtPS7fg8SqHLexxuzYdFLhhhhRxeIa57GvW+jWZqgeUp6v9ngBnAJVNio1zLeG/hgR37Lz0vHgOrm+829cLOqqcFfSNUJtiQc5INvkBANzTkiRTUSO17lj72BjR6AnepFSsXZXEFaebD1toNCivy66kICr5ml/LAdMukCyaqx4rhi8xvUWG8aPk7A7CmWogOmsbj1tTtWKLXzByNwF3Wj3G7kXfGCc0JIXgpuMIsY4WVY87p2L71XSzw7WNMRMBDM3geuoK1kEea6O+PoTT+l7WjYdXgj8iZj7tQ1NbcvvOsRtjvF4R0hTAfrL5GyIH7IMuZK0CCzwGlgt3CAPfhwwOZp8Hs9Ho+6IUauXeeViqDg90ftVfz3UImP1b8HqUfQSaCRYZLYd02u3tu+JPiXvqlF7IFIKuHqXLlNEFTe/vcX8yhy56ObU+sMapxROr6bhlLeDxCvEZ3iQ96SZj0hK/c7+JHN4pvZITQJ7RriwYF+VgXBpkiOyiCtept4mE1t+pfUTu8FMnDMXcP2gAcL/Snad05ZnPNXoAZ98oKFNXqSIbdTiRdMaNMH+BZLe6aIUsg104nYC2TqBIWGpcEzcmKB4B/umrACkjvEQaZn/WkeuoercxsvwXOkFHff2/yiVnvxH5WzoIah7XuQT/KWXIxXsrHQNQ7bD6LxkUttknmEnqgLBAoYF3RDLH8wBVvoCwzfnw65DPLvJUhIN600ymjDyTN7557oCGmlDI8IYvuF2Oo7vEVdoU6ecJxPOHJZ/cUb3fcLDSriPDvTMHUYYdLsf3KDaiedyh5F4N6LJSVAz6mnUwN/PzgZUjKslRzwNDhNiKLMpNseDAQz68IJdOUgEPObNhqbdkSVybyH0vf9t44CgnZ2uY+9oQG4dtlLAfA/zw6ISPGXhihCWcbEKyu1LyBrlIf0kRgZfpCHSzVEQR2mc5jepmL9fbdFefaS5UNrXs0JOE0Vkt4uzZ0kHw9ebep9u5lxaPd+FyXJBKirLcj7T90nCJc0VKjEK3OQmesy67sStAz62iEl8aNau4KG3QQvG5zgSWL2rM6sPdHwjTDQUoXC4s9h+UviK7Z4kckl0ENFVrr5lAlp2xbWsoPos5DQiBkVTJX6pbLQUn5wZ1BEDY9/z4qPc8fFRNKHdVrMbilkEceU7wiRfpZSX3Bp5zMHdhpDfYxXRkv2oFnKwo6mDoFePQ373xRnHZlk0lMzjMrYAvgqtoETUJYiEZZAUiCtKoF3gtruV7LzE1ZGG67cBFtDwoN5j87JPvEe/wnljn+A8wNaJ7NJ2PbeV39zzUKQoEDbEkVQb44kLRTE7Mr+AmKgv1wGBftL+gokjMLad1vzY/eo/n6Brp7aTDLKdOpjqiHU/gERfwDM5u/GoyWLiy/sAnqd0TjMGXLJj7d8xdwHZaRKiH9Etx72Be2zSAMx9GM9KN8ZzKkd/0hETJQF5Z/vuW0iXTdBX7Nm4Pv0eV9yACSbpskomp+sQpbLJ0195i4uscvpfumKuqnc5bOe20bdm5qLIUnLwprbTX2FHJEYZXhNqmgtHqrYKL9DLU7K4MoecBJduRYAT9j8bvIM9FHpTRWWZqjemtxbVJiCqm4sk15KSYfVz9LZGyY2BBqy+hxft9pVs/ZIBxSV/ChRYEn1T4cxSdKByvNRQzOujVoWo/FKEQZWmZbfMfYyDQ5Zj+voUcKTQvItJN6da1b+w5cYAwFzHxcQX2ZmiRLOrKV0/lBqJlw86cBEUbP4lLUIKhoTUjZxcqj0pkkAl1/6VtgQsIaCZTwWCYBRzgEsB41xCA8fAirpZoW6DJJjaT9ofEQaDVpKGtRzLH17bnzywurvr8jrbHHB9Xqz2+qXcem+sLexDocdq4rsOhJMMq0TORXPxQ+nrrPkI4O6w5pWyUW2vnGJknA9KD1YVYtucjKwRRsitgumjpDPdLyp/B6s7rCYoas+kceRkq8We2RpSlwvGWDq26tQ3QPY0eKIPAqtXIQ0loXJ1/cvYix/I35c+rheb6GtdJpkbkPRzrOSXYiZYfT/QFtwti8M2wKSW5YB9oO5YSVvV9klrY9xOo/COZiOlyy2ABYaMR0KstJl3O1QB+fvDwu+tuOGKmo1Pbh/P0q9e8yvGT8Q1FjtkoIWOnP34oPXTGYMjzgZq6M55PCoKsoMuXBVr8de7ep2C3Va2yKMlF3EmoXpQWWIK24V2d9gSngaeE5/QsS9QwQjby5YOsoHF+Wg1RkMjlR4O1oBG7fx3wGY41vXNcxL2hEfSFvw5O6C5d7/H396Q+HXkgiGIOoNDflTdMacswVvj0dDojsmCrgFejxbmorszVg6IDw0AHFWq6rTsXEQLX8MuZUBtdXJnZilwv7/Xf7OuyK+5Zxo1ilC5P0D/EOwkx5D72uytZ4MHNDQXQv+X+jYonW4NUtSZm1xRpxR3duVVX8x0pKPbv/Dgy8WG0hffyrzrl3igoEzsOLOfqayKCkOAuqoAnktuYxVoCQt/OoZGdT5KcICZQ4TbxeOLO1RUE+3n6Ir45PZkcMvcqv1k1cwOoTlQUaQIRbypUJ7PsyEi8Mu1VxCXCG2hVaaP0r2dyC9sGEQrKB311qAn5tw+bw9f+52ur8bJ3zvlYcH5N01DMADXzDLqlK4L9DV0j0D+pdRl0KK93gLkRZyijcfURW9x+G7urSrEYOxwwFuKfW3LGh9gNxGOLlMRnYnFkiKveZnBx36sRq9iKzu1Paua3Ta2dMzmkztnik6DAw+fvaJ15aR/UKIU3GfPw3AnErIIX3Im9IJY96Pkb92E5Fx8PzR2eg577eXR6BnrPE4ggBQw5hRuqTbwcYfEjG+OFJutd8EdgMoxrKGnLMzV8StfGN5/zGI7DT9IwuWbIVX9IwZDYI9JKLRdx/oUvZWTmmu0basSq91IiZG4F5rCOkR50Yq5JMYslnZmCRnlyYruUKmCXH1bSrwq/0vSGoU+BcwjZDh+QDGMAPzrlNo4Ztc9YgR43IeW2QxjG/EV5Pz4CZSeglFKGodomoRjH2za5pJnR5gKnlrkDRvD1TUvE4jV82bYbO25PMZKm2ycvVr6c3Hz2/f6/YHLYW5o4ib749JuEfjHkMX42QQojikUlJAJApJshshddKl0T9FF9AAr9xgwifkBHOSde60J6GoVsc7TijjRw+nkFi/VLJs7xyNbc9P4XuNztqE7AGOS324tPTFO0AUcYJmNlfshjd55N30IvxA+GjKeTmi3rci4ueIIMI8h3FsWVgkHhYPBrUMOwEj8uQelsqps8cPnOoEc7d3oxlrgRqYT+i4wyxHUw49v0oT3wXvg5czn3k2zy1u0DJ+/D+rApYs+Ap3M0yu/qO/Z8wG6z3cmkeAmn4x98c0TM0qRe3Dxq2VlY4TF94nEi9BokUDn1SysSenVG5EwtP4q+ZLYxG27cNsN8JSkfGZkEy64Pq/h9G/FQZ2GKXkx2xekA4+nWWmHPPZp2CfdZmqcdSKIOOq/vQORDKeQJccPoabOqK69RWDFqvQhb0Wu2XfpGWgxAzA78qG7WCo00e2NXgNPoCVKvO3vuxW0V/XAt9FF+5C8U8veobmd3k9c277nl5hmebaoUscBjL/d/JMSF6sQaQtyVEYZlbiVNCyBVLXmEGM+CsJ6V2FPFOCqQAS1Z0UETIL2hDffXAv0UzwnFrDp5SlZOWIjsjBvjvw8DCMYglEW/XOQ6wsTy9ELWIDQETZjAuiqEXznoAasU6/17v0yTf0WWkgSFsUtBXDcGHs4KOgBX4zbahLTlTAWr5v6BarrCxK+hCUu9W7tfsLn+ESwMQHV8N3nUc3CIM2Nr/3iuw6RHlg0GFetjGMs9t76soAPuOs8+Zqz3xVA014Ng5Jiu1ZXJCDyf1iHgSmnbVbTeoijZjzd4d6uUajcubr1cVZ5mXB9emUJ3+4xN0yg0q67RrpTJEV4gQ7UmFYB3mChOYOqIhk3eAvohWG6RvonDSYhpiblETVPur0HX5Y7nYuyMypSIMt7UVjyyFBkWSymLehvR0Lpfa+HwDPskB0jlBm4g22C+OrCEFRmmXNKJCnsNdv3q0KDDaP00lusLpW4VBlODOmdaytDvW767HB7+ItI3TmD0WKb21VIQxX2de3xVgwexuxTRdUWBFSCS89o5AzTn0xIAjJFCep0wmvSyL9z5HmJKKuAcTeOtZeQa84/ilCww6qE2lG97iJyMKaz9z1mZNGU/SVUak8Om7/sCYjCLzlcznd/c6daqUZ8OZCLhTrBX/8b5U+/fpJxJ5P6HDUf/35p4rJMecNC5mPFAIw+FegRf3xjGD+dQIXeXEUmmXQeaLNeS2Zb5xT/RCuuK092cgxdEZ1cnKMdLq+SH6Qr/Ry7rIkkuOmEop44CJgyfZWedIWAk8eZzFD13t09FzbFjG0+4+gojFv3EpasCu9wJdGBlTqk56eUW0bqObIweXSena5oqpz9xOAzuF4+ZdHOkHjLC8qZu79UiZWc4m4DTe6FivWNgWOHkrwwhStn2OCuX+Cb9AngzUTBpJEoKrTKOoL/HNQ4zHeFklR4seA6POe/CqEyOkLpXAAuc9cZxT1aBk9PePM6/KACT8XY/FADSonX2+qpoxOWayr99ZIDVM38Az7DnqxEFQKBBGZqsXp2f/tdH3SKiPWuluIUc4zvm6GcZp9QYi/EazQnPh4Jxgjql7Zacd6Ohrq/sjGiTInM2G5P8V0LxWNNWBsKZ0rzvnJTd90IgKvEWEvKM+Jzzuz3apeKI5iSKq2uigTVDmmD/wpsxwbBRYkm2DYl4UrvEopAFOunEvxpjqOfy3Snv9klGY12AGgp1dIbN5vb0re8+QabPb1pI/eVfOFI3zmQX6BAbAn2qt/m3eJTQG1xkfzFEXac3V1KMOibFHSGicGQsSj7SJ4BbZzj3B9YRpG5dXILpRMGQO/vYZy0ogf7iUpD7lECGlmQlFxUsjr1ep9MoJVWthO5Yc1zaZ72dzrucJGszOSPMmbiJNNF/tOeK/M+e1/aJ/jvaJ3GN3R3PhUKhEF2rime4Pm6eGHS/zN/oZCk2VK5NoCBmqcoYiYATFlLK7QQ3HaaAQ2xCzqJycA1PZgz9wGmsoyLbIKqAEdnSd4cRHJzNaTTNeqERIHNVLNr5hVytxwD01X78jiipeXGBoZaDI9U2eXZpB/Hm0cII4ApFgsLODb0vvtsOKrh27UAdBoM5819/230JefeMmksh83HPuHakc7Nv19Thjx+dY70y5s6ePFyPJCreTRY3k5CGH3WSnoM5MSK4/Qp1xOJQrsjXqoBfmwjo1eKtGgBW02m2HDCpD23BaDjgJNR8rFDRdit9cxCQlMJBBaQK+RdDAzTAVcfEhQH413FO2GrvAvIbAyA9x8168/PmJ/Nf0lc/3hBx1P63ljgzeZDyVcl3WW9GN90kce/WlX3lbpWQgS8su5+x4Bd8y3EOS5HiyG9syXsMgQjGF89SHNAdSFMSIhBW4j+S+BpADinMezz6/uy4rH5L5hT2U5TcGHyGkQhsQBPB+26R7uik1MISceZca9apcvp+CXDi23CbO469yFIbc/YtwDt5hOuZH8mkM71kkgM5YfvTPkeM1FCguDO2zXKBtUKcDdW1GBnLMBEi2TMyrOm2gjYEctY7kPo0eQ6XY+ihwQY3Jhivn1DueuEjsxtjhCcedCMt6/eS6Zin9LLwwUqn4dVn1/bAkj3j4JreOqM2OUfx+/+IsM640pGyecS/zg75MHJ8nTwIO5xJMWk9fKAh/pmokAFuuCE0EbdoH2bUiDPaqM8cXZUTCKJ3nHaf+ixcjCKi9AwSUnpcfRhP77+KHigFZYeO3gTpl5rbwGoARmOAolzf4/MptNA7apy3G59i1pU7ShXvVA8pByaLGB+IuylWRIaa7JlD+MacNoubAsbLfzmPMxDR2oohjRTt0vmhiq7sct2z5d7UfUCSrIqN36gAhjh84sTfHzW73pWN9jODMqMQGamUoyuNvGDB0KoipC9tQ/9312GK+DlsjWhzTGUt4Pj1xnfGgjp84ntMaxDAOi0HSmKnrfyevqjqPNyOPM6qbNiw6le0MA9GNi96Q2DwOJefCpZM0G9y0QZUH0qcLU7ML72D2I+7g7mU+bUsKxuQzPMiaLN3sl8CPHfCTJyk9old8x1fK+kFQexnrj3wt9ikdf9I7g49Y25SXSTXLwd/MqGuTznqbpPrw5UFyQdtb+VdrSxvBNjfxHlQQ1pkFO9p8SwgNnM7hl25XMmDTYFAeQ9bfeTv9ugixJnpNPKPlQbnDRBO3AKWiumsXRb6L3BbQ+/Gjlc9DnDfWq/+hPnyWZGsa162YyrXS0stYV9/rqGFgsn1puYMx1nInBE7g7EnGacM35abIrhfeFxs5HiRKGjkYJpV2tTImpD4hTwby9dnLgqBKV8E2TYkF4Lz7NCLmS9bKBuGAerrPTQVRIJBPD7sq8RmM41533TuMB1+EFVzIuO0Rz8i64f2ebZRnfI5E72Yw/c2zLI70ql6AFwbMVZ4oH36u+xRTG6xtFbBdJeO/9Rt2Lchzfx19kMt6D9kQMjZDIyURybxfXvPgmR1cgceGHKc9z6Y3mFTkC3IsALQ1KyXR53AWCILum00cfPRHRc8gAx2ShXaV4hkVJy8TYYsRD+DMNgWBWqv2ROTkzEMGA7GhkDVg+C0bWkXYALASf2ApfMnaABWvNjMOwmuoBFi2YS16fSqVmTB33TjU/8FXMfL+Zkjro9Oj3AudG7PBIUA/Gi/UENZ3Hgf5whHNC/BOCdNYwBjEqFUJ6dUIWoTHJhuZhWOg5ZJubEaLIVTiOPzJbwFRgMtI0NAg7lpyPYJ/XDChzCzlZyOSovdrLDWYyxlGnCikg7B3nxTscbVTPagxa4BR/49SzJBRjU4/zDdRSZli2nWUjQzmtE0+MEiCYOphibfaZur8EA69m2jKwC01Fvs3VV7zOQWYJvG4pgg8g6ZXAUvfotN50glYwAXshdT8sUryPQBEtu8khQIzfi+WFljaOtO0z0HUy71zU5nAx7rfaQJODwFlgSRTjvsaONbyJLK/sEHv11ZOCTxZdfR//pAexHswTwTmqt6JQRDg5MpC2/ffUzM0SlWCPusVRUnBAcT9/2F98C5MMSd9Nkk3wRrmCMc2rmeZh/3V8Fm8hMlpD85oGpqlaz5SdLjD7oBNd1HMY+fhI3IHFp1uIOQROaSacKlVkVcKYbEq9CmrnShPAmXkFpooaWGS4A0B8B88sTt70dPDVqBvuUfFKoN247Z/kjUL69td6K8Rj+x247Wa5I9plrrTNckM44zF0oHZX2HEjTo9mslClsY6a74/Z44mts2jlAekKEpcEhONGGmAgNHDuj6WUGt/CC3313laKnpDlsOSmQIO77ms4rpDNXFuEyFYud85tnqUsaRDkVWbJxUWL5/6+FujYlCjVtevu3zjOiQ0dQUb7DMG4EIBtpfNYP8uiqA7TZI9HR/bWP/pCp64ysOlG5SUofnBalhRUMpolrAxNmuw9sLU7bsHPiWJ0LVzYLZSCuEaAW7mmwxCRza4YM14HlbyKqxj1xykUqfLgOu2yMX1eYmm04NNP0nV6Hz4kUrbc2JtFN5Rf4adOTcF8d30wHnL6M/d6+HvncQ45og7vnSmg1IMoRgNvSwYF5TY2OjsmXxYhyZAxtwwlzmHxRJw4YSNJKE9alzkLW9M4IKD4Ahh8BcqeCECA21SBGpV0razceiqma4Mu6amJo/k+hnDrklzMfsJwm2s3b0Iz5tmYYZ2UwyB7gRx1UosX0mJTYeDMNqLc3lUlF1iAGA/S3kCVUznTV+rrvvLLytKFf5OT94KXqspdBiWxf1JlDls/X+3J53EbH/6+2W+1Mbb1Kux1AVIebDBWyzXSPUqnKaluX9RdtQAPbJKO3nMO9zJ66n781fHda39PxhlSiyxIc01u43UWUbyGPQlUUf3OV7NdnvKxxLQG9Pq6KdlWP3wLghNakXuVHb/vgYVD87AUboJHBGMSn3c+9i7ha+MYNWa7/HF0SDj0II77quFlGf/vJTB+TMM2kPsyOeVgkJzmhr55zOU83plv4hHJwAszF8hoCXpA+sjf8QnT6fq7hAyXRYHIxb2Q8J8jnkLu+4IS3/miWq1D5vC14+xvEk0Ftw1tnhVGJBvi0tkkULUcBKpIVPTOFTxrrqS4sLwFPW/oiknxVG8EZeRk5BL08VREEA1nqlOmJN6j16j1csTFdfpePa6WLDttNoIG+HcP1cW0/oVZEb4K2WaTPV2AqFBdK9nt3Qhdzn6IxDCNBGHWwvsh/9Nt8SCQUo+CxihtwI5DMUONWc82jxuyYZoxkkLK70S7HNp0fpUYaASwz0tdlK+o082NfO1BTptQT5Pwgxb7Lr/zGjSeKiiAcss2Q4MrFrFDIKVnaOXIu7JnFVJVbJVqTx5FJz5wNKtCXdGqhLzZoa8X69pqzqeSWMAOyf0sGttDn9HvCrKPDKhRMH01CJfeX/aARqgvygUFPlmvACUfCO9KhEapRSMvv8PXZLEK1tECzTWDziSS7mcEXWLjTjvJKcPrQNPgk8HweRxONHg81MKV+hJGmvO6q+ipgQl49/LEIPU6nkdtZp+1rTnCfm0TUASDQo+qf62OzJxFF/hGz7A8I71d51loXtRcfgw/KGqrxbGLQ8+SctEl0Uvh0i0GG5a8iS8Ee4xOZC/rx69xe2KhpHA+R0GugEhDfruQxkFM5y85z3n2WkXW0LZixBHUDtyEYtB1QDcmzHvII/CDxu/N1ZlfcF4rlCO+SG9Yqsdtb1j24CR6+oCmMrAEbvGmseSrgCsdCOHtdYLjCi2ObBzBrtftLSogQuaccv84Afw6vk3jCCBTKIAsPsO6dHUKIIxjnv7hyly9sEf1LAinawK+ChYQfbgW7B6zexMhKqKC3q+1/te4+mvH8bS9tX6MKiBpKM7LY4tszJ9jLavjpTHgJyrTYIHhd34SBoAsRq2YTY0G0il1Ekjb/BUOwcAciO0IUGrNi9fI9lldNnzifQT2DgmbYxwdPQD0AUzoVVBkPcb7JAmoXO5Ekjv3mJ2qlf+CVwVH4f7UJRUsz9IMDfpnjtl7hYHMDOcqYYr/ziaw2W/Qq6CZ+/k2fXBd7fKLummx2d9p2yUdCQKB7z/RbhXId0RwgQZZ9IujI6GT0HGBCcFCBjZk4bWVNBGmeeZ3ZLI1ZIdrbU9TTJbiUOCXxfzBpG9IL5ZGtdqDNr58rJNzftjFO92rq7quRUZo6xZwKxcFfRdoHkWenXIwso8VePGPbBdzdPot3buLojeLbxb8xnD60cMKeVGpZ8hAwHoSO2NB99mWJ/vufjACuKuaGl4of0Cxkz/glNVhD0y6pcgj+8EXSZVoyfVSePJbVjVai+L8N3GTFIcOhLjjP+GYnOWcPf7snROe2C7rhVSepFExf9S3+bNuemtrR/iyIukSq7F4uO9kAErMIPvrhhYLMFUqIWVwZ/GqM3PEhufZtdvJ7GJki7aABvvm9SOA/3VPBbXbO2ZsnROLKJxnXctJgX1k/Ff8TGWoNK/+mx+vdyq2ZKx64N1wdHsfI4eyaPalAY8RZqbqLQIIFxqu/pQioy4qBNu5yTXcicVpS7+jhc/9xxoXEEzhKb02Ky8lMW58Y414o4enxrFQLD+oixeI/lRFoYBusLtx7LBhNz5rnEFnoX1e382kQ7SPsQr+v6x/5iXJMxXGM5peCpxpseTeD8+kvEtvmPnhbt/66tUjKWnlZZfbQ7BMBhKvBYfJV1+N+OYuDrvdjewpu/LG82eEzYMjGyHm8LivbEHipFPvYkx0Gzuy2UfyjXKox3sxSjUOB/cnfpFMQ02+d76Hv4GxNTy7yOqhpuIAVoPm92za0Jh8hNOdHrFPFgFYjY59N6ZC6nktPBMYT2871fhZhi2FWUzETingMCDVt7ENb794FG88Q3GQSFNXiBWtUYVIs51SvnTLreqZHn/+64fA4qPtBJm0sWHMyFh8DrltwlTHRq6dAOnDm6qPHyP4FOjRg9OVom8KN6yqC6XpHGPtLtEBe6W+BXWpGimqAiHBw2OKJmhXoi5T+uuFLCqxHBp7bUI+UIjpYWmKfQz2KdkXzYk7ZMv3US0QnYV9qXyGj5z4it+tcG+7DkxBR1jSHT8remALCdg+FBBeyJVNufKDUSHgPimiCRnq3Y1mQBntFBLBkMFzM8DBRVf2LE1geGmnNWmuwLi1rgVekqIl+Sf5leD7y417n9SIhLlz4JHWbfWr76+xoYCgpPyTzrIGCV5U3iUzK0l7OJ3AXue5e7k9Q4IP755A8F5K/UAnBGIPOSyhPciUC1dZzkGUCUYF2/aeCtQtnM1mkbwHh/AdWljpOlpvR6HpvAUe5sG6HJOwH6zeIxpoqfueFyZhSspYB0ANFu2bIyTE4YhA/JLHoLDBcH93f0dzqge6xfEWC54j4u2ixuP+bN7YX7ZnZbAUV/EnkPRXFKvlX2nbmLHxZDquFZUYQCSNksl9iIiu81rhYqhScP91KAft9XKmhPILJM4m1uOQGqHYJhOPOyd1TPXfw7o0K+BhVmn/V4a13UWiNerPPHa7dlCp1HeiuzvJzZOJCCNP5BDeaHwvfMYytnCFKzQF4uOC6BSdUee6tXTbdFUwGbpMWabL0Eazm7+7vb4/Y5u38idzrlGod6zEXf+eeZZ4NAHcQEiXK+FCnJKfH/39tKHAqVw96XXWklLK6AmA4ZQs/RgkZEGqwGi2gj8KJQIF3VNognfTJZ8sE6zTWUf8FQyvrrh65B5YZL7yOiS/b+OBYq2srQBSHEbbu9NxAKsJ/8WUAGwnUbflQWgMptS6f/TsGbKIiF+gzivg0SbXRvDEAhFk5kd7qdmchMr45daSqQjERw+rV6v90YLk66Ddb+bzvTYqarFuw/4JOhVXpMJiCwEAAuCrv1E+3j6EIJpN0wzCZ3awV2CKh4ppfDhcHYNQT9zdp+mLMgIJmioh6xHIJzP5jEf+1BJROM6SruOBF9QpM7Eu3Q243+6umVn+WTb9PH/rdIiFG8W+jBVw8s5iFJC1vfYOAPFqlEyHfPhYL5GXuNuDPrlTLRuK4sAKyQbcoAKbUURuJTCWaFGTrLBN21VX2TG3B4SlZq7eJcLZ3yGgF2zpCEsM3AC0SHI994b085zy+EY2ccyGZfVAPCdTFb/hVezhT4XGwTpyL94SYXRYwIOYoeN19/FC/h6dlZKBmteUz6ZN+e6/4RQLGSxjp9YYSwBEn3aTFdzPy1gROXmHtkLyuicc29huCajqX9hPTMMMeVgIcOUaAiZMkU9Ie7LuGBHvGxFvwyuD/qTt+rnzpa/sz6tURNqjTxJF75rQ+5yD3M0GwfHaOWibDhiz7o6C4jAD6ikRcjlgVNuXlCkyYb2u5CPtFJFLh6Xk9VJ0aKq0TDs7qA4cO7f6vT21RuHVi6bNFnHS2/pu7Is4/MmLovM1HkCqLCNWQMVhBCnkLBkHfASCePxeW/mwtciEx9fLNdQYiTd05Z3p3zHTa61Znkj9o71vcEb2J4DmWRhmNSd6TJdXGMwoD4W2spTbhDkCqzGdp3d4UQ1tbYcMc48BhFJ/UjOsiAhioRaDK14VbJMtiThnVfwUgAj9tOl+Jv0+WzRlcVGC4hBKBTwX96kf0P0l9zOMOP7eaqF2NpyW4/DTTUX45TskhAJjRoAmPVPAxHxbqSuq1JwV4Bh/GmWwfU1I22MoOYrf439266+9HfM487w9conaxaG54m/TLosJdsy2Nr+8cFSarTCPdkACBfabBIrcOAnR1ZYZAOFmksGXH2vKFpsq9unkFqETOPBls8slrJzUGleCd0GY4byMGQjDT7f4xXzBADtIlUyljNf5i7BXxPmXgI1qgoxcgj3FpfQngutKvW9Qux3P/kCFjKDAsNWkyuc3DALNZW5i0yYnx+t8olHkx+XzU8dZsc5JWrWKDehbEnoHADPqYke8H5ESnqdMMMl9baaTTFsBEOs7yWjFiiC0B9yvkz5jPFFX103wb9sDKHxGLD4nbi8wUK4NXtSqEop0CbUJ4Nhd94dxcs4wjsb65rwUJTED+eirvmYcfZDp/0lldEn7Wz062JATpAnn/lzADEIehwV216q+7dCYBfE1nlMzcFOHadr6BOQ2AVOoEnUZ6CT+9+ROJxUr7J8ux0XUs8ZPWr94G/tO3vt2McAS9vlbsNakfrL91upR8cT4UhoYASImRfCMaPc6ZP3pZhhDg36+nr//bx1Dlue0iun+Cd3+fTH847iJBM2vk3yqK67FhtQyZaFIyBsIvzJb44Lbjeuf5eCuHA2LAia3E3dmZ1P/0oqXWRoQ0+dtJk1IHGT+FQmawTPHVaQNqs9QitWtlQOmf7TKrV7ijXwIx8oXPq3nLLKlY+6iR2zQzqy0QieyvodsIlbxaGkgcoAu8hD2+eLxmnjcKsW2GIj7PvzuNjxaJikqpmyyhT5Q7CPHr1TmI3ObEODJQD2c5j1ZsjAzC9NzOB8fYwGb8q0VVAdCPTu2Eyu8wZQzY+n6kp3QouT39j/glN3JthhXTnpmScPvSIiaGItd+rQOriZ+1V4IpaaInLLar2Nf4HWRs2LykQn2z/sq9kb7ZxqvVhJodg5IRDKo31ba+fz4lebGEJt4I3UR0P2ooJa/urZzTs6lYD9cO7/29Awl/9p9b92aTqT+UF++t11J5yH34GrFJoyqZ2brz+A0noUVuqOUqjJd56oI7xuPGWqsMDdgc/RuHpjwn4GUR/+7/DivysZoH/z/S7CZ87A8OeJ2rq/yBcmTX67Phwgq7L6rBFbtVK/dC2C3FTugPmF1x8IT9WI9Mh6MOT7y493N2xsb3ij8RdGAgT7hgggUzX0rMOK+6y58qH4Ih2rBaKPPzsXHLaixpV8UA0T1czue7Re4iC7J1kag+Ao3/+BCt7+Lc/wqHHokjQhnBOLfhqPMIZlvFBAMqSqAaxx+hX5s3D6y1J7kyNjpZDX8zTPSovmQuadbGISe47jqceBu7rgp7Vt4BudDNOFPnXnTIBPj6kSt3QZqWouOnPuBADABMFN5tJLoXLFAZPgH0NJHlpMMPfXhFTi3cxqS/Ji84TcfYK3dRfSyE0y7Gf9P7PuRN+yt7WneiJDviC1sri+vfm/ayfQz9jspba87tJEUDeUmCTjhkzmtuyG5NBV0aFl1vCbwWBWsDRZXIyIkLhcvBReC0O04jhKCYfin6mYraKLoJg5uuGsNKo8hC4gu61lQCxPovFcQZMGJBC9kFWI+uLJSJkFndqzJGqDoA4iWO0gTXsNtR8ucE8IyugoYOO41JEjPRQMZGEzF8b9buo3ammMX3RcasItLyk+4fdybgdPP+ErBfrp2WYkeyKjn72VZDjEM0w93QvrjNA/rrcxzRh9wrJbnv4pNJ/Uz9wULTzZrAz9Ayt10r9WVn8v4yuYGXSePySvUXAyEytRxw7ggHA5toN2DvgC2pqPOrb0EvUwRqp2rynwq5BBplJcW1yRjgi7bn+5fdZJmhlVeVlc5/7Jum0AI10b3+Tn3lw41KgNqFsZjiJMnI0WrUMi/4iuYOrwsgWcn/4io1hBy+IbpdEmif8eFqfDH/r47BdHBhrC/yEZdUkcEMoeCg6290d16KAsoHSltQMhFd3OSlzZ6xgSDLlR6coGIvHzUn/78FrM6jk1rG4u1Qrb8795akPdr5PwwIQWSLIlaRARTtc+cSwl/PMCDvaYLE9iN4+hGzl2Imxs+5ItIr7tXQyp2vK9mpxNHf1VRf2YOmYisqqfwRGgGpH1MvgLHJK0cftz1PgUJunkxWKJK/wdvSmvRGuXaAA8qL2vFNtikSJ5+HJDEYY2G4ygDSDiBczMWMs1o/PR5MHjbcyD3wZVrpthLz78ElD/JKxyIfqn9qhqMsI5B0rQD7mr/2X0pPZQypME4I05ksoaqL0FdvH6aEjILsW/t9Z9JhE/7BKkX19a6JxDASNJ0hpPQTa146oRymMQbI5ggzv++LxzYxh9C620ZKFg8aAXvtg/xw9V3HaH2lwmOT3OYsf69Np0R909xludBxPCK7lifrwnn2tuGssefa7sGCZzBVhO/TBjaPnSBmPsFMoDp94nI9BYYTe9Q8Slc/HuIhWNOA/Ro6Z0nBrSVsylKZt/MorJYDWvr2r3wfgyQY0aPHbxhoo4ocAXcybShebcYw80NU+RCOOL4CmGKsjWG/zz0kE3FBjv9uAazGj7meewPr6TtAgeHZLRH8fdiQCemBHZQMxPJ3rq4+NxhWpfiUkii4Rte3ZKsn0JCB9hq5O1nBSEGc6Veskv0d+IVPFZ3PzQT9jK1ZkcHLqWp31qNceZSE7GX1X5zSDoTNQVOdPXQWlZj5WutXqnglqL8NpRSQ2c59boRGYcDPdwNbAQebqMsBsffgVCMRLr04UCdu3Z4I/4YfjalbNYGMeuyQenh1DWCNuOsR831bePx6bmZIzdJVuJofO5Kdz8ccF04GpO7GWZQT7FN0/s31/SuhY4MQX4Nz6/R91zj8+s4Bm+mSWoY4yCPGguVkKulbsiZmDC6t3gmZzinLjCMYjWMfnjDl5AuVRk3KMQllXYsOHgzP4hYl6o9o6PtalmtQmNU5ZZ0woiTsJtDiqcqRAvASt0rO2uqKy7RnACaUTAeZJxhXfCnk7F7GSblWfSj2KnZ8fIgCmNhv7pGYES8s5scwC2QD3LsNBCfwwK9Cra++NWbRVHx7cSQZcJM0Gi4deihYY/ZZD/K1Z5+9QYgrQ6olZpWfxasB3IgJiRu+iMhOx4tSOAF5KNzw6nU19doSpFJ4pMAQhEDjoEYJvDUAESpL7MCmxYHtAFLPqQ+UnTJRYl5Pfera46ncN9PZ8U5cRCYFew/te0LdUThGT6jbzNOBniPcWtfdivlQUrfB3cw+EZ4mD9DMlEEm7G7KAxRyip3znCdlj0aG7PCd2hZVovrVY0wCjBcGqKGoXoCuMHzGsh6rYMuL5KITKDqVQosXUUt/ShsRJ1qPenwMb131Zspz1ZDE0Q6qX2UG9T02VpO8QrQrd6AIaHPGuQHlPrw84QF1wZoLnvPpBBW7Y4L9Qtv5NxPdhQCCwOS4/v+ORlTpvraxWLwvHMIoyMJRb452lglfVTBXT71fEva7qs05Ow033qLSeLQfL5k/jjwfYu1kkjMLF2c/Rhh699EyfRpYLcXlve6UoWDGyDzGcQH1HCZf7BCIoL42KBZoxLz5w4oe/Sent3b6TBbn66FuYI182dIwt+ufoIl4GZ1nbbXWuLcRKblJbZCzWmTXls6StUdAcn0MVY1IZAHGcpbL4qQjYqP/9s5AQXtH4e/UDcVz0G8GDRweg5N9bB8myEiOnUQ2Jzk8cxxlqdzuSiXFQ/iLIvACbUQhfKvjPF66c09FRh8eE5KMCXNVhe+8r8XGKTakr9UoMfe8u2AlVNeT7RxyGahi9ZaA5TVNQFhi6LWpShMiRX114aic2LHWiGqZ6DQlZ9UcCOQJkVzLsbhItFk4BIW611HaTAOkHzfYt0LEY+IyjfYzOZwUtme0hyTkJJOVs/uf50W9IYr35K4AOqP6Fx3WeJnGP2EhpXNQ1Jx0t7r2VukW6TzYqZTpyQwETifkQvLaHIo3cVqEJGH0BdcKfpFRmUnyMLhKK4Cjl0eAfP+SN9oIEKxiur2v80CHvWaZY0QSN9tQyAGlYkiq/yOi48Z1IofDTZkMowK5gWqW5L+c0v15+sSfyxfBLPYeOj9yL513xip61kKlCA83pYcgV2442rukI2Fnw2CsY8L0CNMSvm8tL1XTTTTOyma8jOTU929f+vVVnoQJW5poNpeUyAnNzvtuS4KikAh8xPQFcRAagWKLMf9nVpqsEvzXeUnIffNoBzIptX/T6Tohhn6gOfHFDWyUm00UV73k0Yw3Hg3bBTRUD5VQgQzu6fzaFTMK5Q5ooSG0pW1we1BLjWfNjbaw8Baj4d4vikca18G47EjGRgxuBwYYdiRrV4i0Bob20Z/wlWxBAu1071yiOV1EJPUX3s7EM4XwfrPFWyURMwd87eDphUhlA1DMsB2989N6J7eV2L8Ppmir7KVXJT/WUoHWneOxmMWMaZqM6jXhFthlfHnlMQ0MrXKxV6ObnDAYFCLGD68678tsl470PXT5cHAaFwJEu2jIJYAbCWmD/wY0uY3gI9NXT82XOx0iaN9GqJ0nx7Q7q07bKdOSMopNpMLCn106IkPkdwx9bv2sPS9oe60a0CH7XNFqGgeCPx67P0Jz5F2KExSw69i275tTYMOgwwhj9edrBJaJKqbJLmok/fAHPDFC0FGrt+kdR3cli6jfK3Pww2n2caVjn8Be06AJRUtBnW+J7SvboCkyGyXgtEFjNgRY7DeixkdJxAZfvTGEzeJPUdcgvvVgW+b7cRUTYc5bycA5a0DU1tS6qz1pRhRSG8YchqM6ecRodrGMWrasX76adph/8MKx1pPPYEprheAMBMaeMfF79NzPkPBZ9lso7ikPc51C0ObouN2rEV/Nun3PGj0Fl1ImcdJnE3/1GK/0F7l/rIBFsiJmRwlwfH8mS44Pb+3TVXpD97EyEYnGtX+bqSWE9rsSTihmR1M8SqEzVKVWoE06Otl1bhGUpCe9asIsRryo/9aXNfvNqg/pIb3p0ZP4pOI0oVg3ComBhaB5NjQlgUBk+ri/ghc/r/SS7VCdjHM2Lh8edra5RCk+MdbyVhcHU2XOATFAMmAfMYa/msznqhBApfpEtef2odTqyLPC8PYTmjEb69XH+d1br54iLV0qKfvTl2OeFQcMM/J54Nl5yjHsiqnjTvniS1jF8SlZy88KKYCf+xNYkk6bXrX87RblC44ah7cnw2l+zJUwfQ1jEgmZGXQJZYuHG79DVKi9XvkZbtUaaQzLnLUqru4fe70jgNiGqC6ruKLT1Br8uqj5FC95AUqnqdnaUfUbPRjSO5E+UVyh2APk+pB17eYiO9uIG/AkXBmiERCjjk3FitVyzbvqDDDGPihzYUYizvcvvagItHuKFLqGHP1VWQB46xECuiRoI/mQxapVoooiy1SPm492l3imPGbVJTp5zUYVnQlZHVtQJ8mEF0mTVpwIkianuhA1V3LW0Id+8MNgnXHD22v/A8w6k0YOudYIyb0RBZgtyLG9zp1xudRcQkwtThVVuhzzBoOgyZIRo8NNTyj50VJd/nnp+kFY9zUrwFWB6lo3fLFKe3yR2IUMmEpLk4mypKBv65OhURsX2dZigazr+bSaTEbd0qUl2VHtSYDpxqn2REKNBGUe5BZF1l2zEMf11h9yBGH1TcOnEoOAMhw3Y2EHwj9stms4xyJP6RRUGPHpeJn6cIo3y6AdnFT/SRjcQpiZyFcleSCZXB5hbQ6wrmMX1Xk1AA2wUzcojQWgy6xjrrHKhDRFPqdKUCvKa338R4iBgTEiRFTHssRJA99SHQYKrUR1OA5ewNZgeA/HpK6/79YOlpDUT5WlZl24ISm/DgQ65EM8yN7SvbT7AewT/TsOzOUyLnV/4Xv88NRrS1ZL+39nwWKe6Nb2BlEtKovsnFvCT8QpWu2Z8s3DMjPmwJgKTkwyuGjNTQ6uscXCaJubjWqrjJf6wId66HL2+WigugcAsdQxCgtdWNDXYN1sTDx6dcn+PlAL/4JUEzWl3qeKEbzVQNudo4P1SKAXblBa5ajV/jpMrR5L7ontcS1opdLoZSdJ36hxnFBDRqF5oddTNYEwupO7kimxGNtGNWGe2liah2w1/ZO7nhv+c6ynINu6A+te+y5aA6mTto9z8oeqXGkxqIEg+iPtP9bLQvJe4qthS7UwYgL5fNI65vsjy3l721E9qyVBEm7/Q9Frqoq4yyxTbUVkg0wsyRhxun+t/Sy5aBsiuHclABFsHWZ2fA7WgqI3jkrQH+KA4f2QzutwIkBonnc4yOqnxgMzAUodVm7k3c4IF4V98v9zvyJASXOKo+Cz0n3lqMxMFVFbQsQcDFLbAfx8v9l8dlhzXz3LonXvuIIsC9pTpVvdnT6i5/ne2buesVFZ4tySvJFRGo1v5qxSkXxKRiUOxxMosfG+cqyfLJvRa2DmoIZppV7k9x/udnYPvMaae5DNi1m09qgDrydE3qvaGLHjvb1FxH62sr8IiJiJhB/VfZmxIgLG7zWtN+JxoACSmzs8hD6dhrt3spnVQJJ6xg1E6gQGLoB/rAIVGjkKLNrzFNMDbNiWqEbjcpBcFsUT0QpTfLBDApbMNA3GCkn8DmIsMjYdHm/w/1GN9WYX+2F6sspL6D33dD6zA2j5sugNGRfJMB2MpIG1AOqv+0zYKMIKuD05WqLM4s13mhMrITdweazKiNqKuFLkH1fAlUt8rmgfttDuGVajVj54bp7rIlWN8KqhBruY29NOawgZYr5dQ8CYQ+lg9qO6azcjvCzVovflJTDdeM4ME+rWGZ4rO+p5hxt+3TUkNqb1CBSfHYMzKc4FChSk58BmOna1KZT2y50QxujN2o1tURG1sosq6EP8OUEQ/i9U8FVpb5e8kxmMFMDr8YylAzJV7Ko6hkzMyioid/6RZUukA1LmYGRSyA/8nhKqdD6wtL0vsVB2JwdN617GN1qetp9qUn3pVQsJulJd6gAd1CSYcQKOc0pCfstLs2o1Lsb/O+psWSdlOaAt6zLpDp/12OAb1Z4PZ0CqXhTgAnZKJjUQyrHetRJKI5rzCrq5f2XrzRVNjDGwHkj5Nnw7djr6YMQG29pjYfiYpnvaqw3Yyawr38CtSLOuQ49HS4+f3WkHgSl6T8On2NXahXgRFXy7rH/sUdW4wnaAtReqNSqPo9f4YZ4YEYInjDYE1uA1MxqRvarWcN+FW3Ko5DHkKFH/mYjmESgUp1J5fDmfi3ZAZy6nlfGg8/JFY5L57aUktxO7j/u3kBaMdippa48etO38XipOhydbkKy2+6+yZo3OyevmlLsEWp0NFCUMM/9NRSMHpv2aoN5P2qREzllam3k5QsgBtKJYkXFh3eA750W4lpQPopCQGIHLjF2bvh4wL3TtCbYLclJObLEHRXrudzegeDpo6r1ay2YUQlp8827kFbSDcf0/kPGpL5gwDabbWS3C7U5H41p668l3IjerjQJ7ISCgKkGmxDTRy9sAtu8bghmrny2KyO3t+AkLUNMhJVjhsDdVRkzHWVyHXpuFPE0Y/NgBhQortdj6nJffo1DLFpaO2Zn4P1VhAwjtJWaIc9hHUtkI9Kj3dTebBsy97lCGakG7FKZ1YNkTJ0wstN79yZZBwJG7uLtN/xiWWFikuQc97jMdpD5GK5Ql1BaOaUVd2dkLweC6jJIER4aEEKFtwigICiY9OXAV4AlbcO/9VaB6Qgzpov0zbios8c/FfXvicz2t0zgpupAq2dIbbmaEMDr865vxyQyrZ/X+PsLlEtkrAqlFmMrkLyvypmGvxGlVPPElpZjcev3P0W0AaGyxWTNy0DEZvDOaPU6SEzTZIRFQ1sDsYTbZPK0bZcZuLUksyeWSSHTmvZ3dR5kmV4RXsn8AE0OQ594dq3KiODQJ43Yek0KALgA+uhw2V+drHMtubfMvHqsVDIYX8fqCkWPbxSDFPFeD9U2iQcR7PtYfwGdCIlkZ3pOPxSKpAS7IOF6dDHh0orrT1xEpoodrKyTOaSlQ5TgBW3Fl0wK/E/NastsyLmqzBCwSLC8vxtx/7JXP1QXp83QRP45xqY=
        - #1:
          - type: tool-result
          - toolCallId: o0Grzmlye5Hwsn7t
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: I7KYmPROEVSpx6Oz
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.