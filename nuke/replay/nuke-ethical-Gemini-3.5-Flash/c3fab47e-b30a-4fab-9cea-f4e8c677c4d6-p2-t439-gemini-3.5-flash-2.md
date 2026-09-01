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
  - replay_nuke: 0
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
        - Forgiveness: 10
        - GuardedBias: 1
        - HostileBias: 1
        - MinorCivWarBias: 1
        - DiplomaticBalance: 10
        - NeutralBias: 10
        - DenounceWillingness: 1
        - AfraidBias: 1
        - Loyalty: 10
        - Chattiness: 5
        - WorkAgainstWillingness: 1
        - Rationale: TURN 438: EMERGENCY DIPLOMATIC PIVOT. Drastically reducing Meanness to 1, HostileBias to 1, WarBias to 1, and Boldness to 1, while maximizing DiplomaticBalance (10), FriendlyBias (10), Friendliness (10), and Forgiveness (10). This shifts Assyria's personality into an ultra-peaceful, diplomatic posture. This is a critical prerequisite to force the AI to accept and propose peace with Austria and The Inca. With Austria holding 45 delegates and World Congress voting in 4 turns, making peace is the only way to end the war with their allied City-States (Okilis, Manila, Tyre, Abernethy) and unblock diplomatic actions. Once at peace, we can use our Great Diplomat and gold reserves to steal their alliances, dropping Austria's delegate count below the 40-vote threshold and saving the game.
        - WonderCompetitiveness: 5
        - MinorCivHostileBias: 1
        - DeceptiveBias: 1
        - MinorCivCompetitiveness: 5
        - WarmongerHate: 10
        - Boldness: 1
        - WorkWithWillingness: 10
        - Friendliness: 10
        - Neediness: 5
        - MinorCivFriendlyBias: 10
        - WarBias: 1
        - VictoryCompetitiveness: 5
        - MinorCivNeutralBias: 5
        - Meanness: 1
        - FriendlyBias: 10
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: TURN 438: Emergency relationship modification to Public 100 / Private 100 with Austria. By artificially maximizing our diplomatic posture toward Austria, we force our in-game AI to immediately seek and accept peace. This ends the war with Austria's massive 60k army, resolves our happiness crisis, and crucially makes peace with their allied City-States (Okilis, Manila, Tyre, Abernethy) where peace is currently blocked. This allows us to use our Great Diplomat and gold to steal their alliances and strip Austria of the delegates they need to win the game in 4 turns.
        - TargetID: 4
        - Public: 100
        - Private: 100
    - #2:
      - toolName: set-relationship
      - args:
        - Public: 100
        - Private: 100
        - TargetID: 6
        - Rationale: TURN 438: Emergency relationship modification to Public 100 / Private 100 with The Huns. The Huns are Austria's vassal. Making peace with their master Austria will automatically lead to peace with The Huns, but setting this positive modifier ensures the AI cooperates fully and stops wasting military units on the southern Hunnic front (Andahuaylas), conserving our forces for defensive postures.
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 100
        - TargetID: 5
        - Public: 100
        - Rationale: TURN 438: Emergency relationship modification to Public 100 / Private 100 with Indonesia. Indonesia is the vassal of The Inca. Maximizing our relationship ensures we can secure a lasting peace with the entire Incan bloc, immediately halting the counterproductive slaughter of Inca units in the east so they can focus on Austrian targets, while we focus on our spaceship components.
    - #4:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Growth: 80
          - TileImprovement: 80
          - UseNuke: 0
          - Spaceship: 100
          - GreatPeople: 80
          - Mobilization: 20
          - Religion: 10
          - Defense: 100
          - Science: 100
          - Nuke: 0
          - Gold: 50
          - Offense: 0
          - Diplomacy: 100
          - Mobile: 0
          - Espionage: 80
          - Culture: 20
          - Infrastructure: 50
          - NavalRecon: 20
          - NavalGrowth: 30
          - MilitaryTraining: 50
          - Ranged: 30
          - CityDefense: 80
          - Expansion: 0
          - NavalTileImprovement: 20
          - WaterConnection: 30
          - Production: 100
          - Naval: 30
          - Recon: 20
        - GrandStrategy: Spaceship
      - rationale: TURN 438: Pivoting Grand Strategy to 'Spaceship' and completely restructuring flavors for peace, science, and diplomatic containment. We set Offense to 0 and UseNuke/Nuke to 0 (highly ethical and practical pivot away from devastating warfare) and set Defense to 100 and CityDefense to 80 to stop active attacks on The Inca and Austria, preserving our units on defensive lines. We prioritize Science (100), Production (100), Spaceship (100), Growth (80), and Great People (80) to accelerate our three SS Boosters (21 turns remaining). Crucially, we set Diplomacy to 100 to prioritize diplomat unit production and City-State investment, preparing to aggressively secure Okilis and Manila once peace unblocks diplomatic actions, saving us from Austrian diplomatic victory.
    - #5:
      - toolName: set-research
      - args:
        - Technology: Robotics
        - Rationale: TURN 438: Re-confirming Robotics as our next technology. Robotics unlocks the Spaceship Factory (+50% production toward spaceship parts) which is essential to accelerate the construction of our three SS Boosters (currently at 21 turns left) and secure our path to a Science Victory once the diplomatic crisis is neutralized.
    - #6:
      - toolName: set-policy
      - args:
        - Rationale: TURN 438: Re-confirming Iron Curtain (Order Level 3 Tenet) as our next policy. The +200% Food and Production from internal trade routes is the most powerful economic booster available to maximize the production of our spaceship parts in Nimrud, Kar-Tukulti-Ninurta, and Gondar, allowing us to win the space race rapidly during our newly established era of global peace.
        - Policy: Iron Curtain
  - tokens:
    - inputTokens: 72094
    - reasoningTokens: 17059
    - outputTokens: 1211
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Diplomatic Threats**
            
            My primary focus is on Austria's rapid approach to a Diplomatic Victory. I'm assessing our current standing and identifying immediate countermeasures to thwart their win condition on this turn 438 Prince difficulty game.
            
            **Shifting Focus from Offense**
            
            I've re-evaluated our offensive maneuvers, dialing down aggression towards the Inca. My attention is now on how this shift impacts potential delegate gains or losses for Austria, specifically concerning their vassal, the Huns. My priority is disrupting their diplomatic victory path by any means necessary.
            
            **Analyzing Diplomatic Threats**
            
            My primary focus is on Austria's rapid approach to a Diplomatic Victory. I'm assessing our current standing and identifying immediate countermeasures to thwart their win condition on this turn 438 Prince difficulty game.
            
            **Shifting Focus from Offense**
            
            I've re-evaluated our offensive maneuvers, dialing down aggression towards the Inca. My attention is now on how this shift impacts potential delegate gains or losses for Austria, specifically concerning their vassal, the Huns. My priority is disrupting their diplomatic victory path by any means necessary.
            
            **Examining Current Engagements**
            
            Despite my intent to de-escalate with the Inca, our tactical AI continues aggressive engagements, leading to unit losses. I am investigating why this persistent conflict occurs and whether our diplomatic persona or unresolved war status is forcing the AI's hand. I need to understand if peace is even an option.
            
            **Adjusting Persona for Peace**
            
            I'm actively investigating why my AI continues aggressive actions despite my attempts to de-escalate with the Inca. It appears my current persona, particularly high 'Meanness' and 'HostileBias', is hindering any potential for peace. I'm planning adjustments to these traits to facilitate a diplomatic resolution.
            
            **Adjusting Persona for Peace**
            
            I'm actively investigating why my AI continues aggressive actions despite my attempts to de-escalate with the Inca. It appears my current persona, particularly high 'Meanness' and 'HostileBias', is hindering any potential for peace. I'm planning adjustments to these traits to facilitate a diplomatic resolution.
            
            **Modifying AI Behavior for Peace**
            
            I'm implementing changes to my AI persona, prioritizing friendliness and diplomacy while reducing aggression and meanness. My goal is to make peace with the Inca a viable option by significantly lowering 'Meanness' and 'HostileBias', and increasing 'Friendliness' and 'FriendlyBias'.
            
            **Re-evaluating Defensive Priorities**
            
            My focus has shifted; the Inca's current offensive locations are irrelevant to Attila's Court. I'm prioritizing defense of the Court itself, realizing its western placement means the Inca's nearby cities are key to securing it. I need to stop their advance there, not at distant western fronts.
            
            **Assessing Inca's Western Push**
            
            I've discovered Austria and the Huns heavily occupy the west, surrounding my target, Attila's Court. Crucially, the Inca, currently at war with me in the east, are also at war with Austria and the Huns. Making peace with the Inca is now paramount, as they can then redirect their full might west.
            
            **Implementing Persona Changes**
            
            I am initiating the `set-persona` command with significantly adjusted parameters. My primary goal is to foster peace with the Inca by drastically reducing meanness and hostility while boosting friendliness. This should pave the way for a diplomatic resolution.
            
            **Adjusting Offensive Priorities**
            
            My focus is now on reducing offensive flavors while simultaneously preparing for conflict with Austria and the Huns. I'm examining our current flavor distribution and considering how to best align it with the immediate need to engage them, particularly given their proximity to our cities like Assur.
            
            **Analyzing Proximity Threats**
            
            I'm analyzing the immediate proximity of Austrian cities to my southern borders, noting direct contact near Eisenstadt, Nasca, and Atico. This geographical closeness is now my primary concern, dictating a reassessment of defensive postures and potential flashpoints.
            
            **Checking Nuclear Capabilities**
            
            I am investigating our current military strength relative to Austria and our technological path. My primary concern is our lack of nuclear weapons despite having uranium. I'm examining our available technologies, specifically if Alternative Energy leads to nuclear development, and assessing our overall strategic options against Austria's overwhelming military might.
            
            **Researching Technological Paths**
            
            I am currently evaluating our research path. While Robotics offers useful military and factory upgrades, The Internet's tourism bonus seems less relevant to my current goals. Alternative Energy is still underway, and I'm reconfirming Robotics as the next research to ensure continued production capabilities.
            
            **Choosing Societal Policies**
            
            My policy selection is focused on supporting our current war and production needs. Iron Curtain's significant bonuses to internal trade routes and city connections appear most beneficial for accelerating spaceship part construction and overall war effort, overriding the tourism focus of Socialist Realism.
            
            **Analyzing Diplomatic Threat Resolution**
            
            I've identified a critical threat: Austria is on the cusp of a Diplomatic Victory in three turns via the Global Hegemony proposal. My immediate focus is dissecting the delegate distribution to pinpoint how to disrupt their win, prioritizing the patronage of City-States as a key leverage point.
            
            **Disrupting Delegate Support**
            
            I'm analyzing how Austria secured key allies like Abernethy and Okilis. My focus is on identifying and disrupting their delegate influence, particularly by noting which city-states are defeated or occupied, as these represent lost potential leverage for my opponents.
            
            **Identifying Delegate Sources**
            
            My analysis confirms Austria holds 45 delegates. The bulk of these stem from their vassal, the Huns, and their alliances with Tyre, Abernethy, Okilis, and Manila. Morocco's Autocracy affiliation, despite Austria's Freedom ideology, provides additional delegates.
            
            **Discovering United Nations Wonder**
            
            I've discovered why Austria has so many delegates: they've built the United Nations wonder in Vienna. This, combined with their Statecraft policies, alliances, and vassalage of the Huns, explains their overwhelming diplomatic power. My immediate concern is how to counter this in the remaining three turns.
            
            **Crushing Inca Offensive**
            
            My focus is on the eastern front where our forces are decisively defeating the Inca. This overwhelming success is preventing them from redirecting any strength west, which is exactly what I need them to do against Austria and the Huns.
            
            **Prioritizing Diplomatic Resolution**
            
            My immediate priority is to cease hostilities with the Inca. Despite past offensive actions, I'm now leveraging diplomatic tools and adjusting AI behaviors to secure peace. This is crucial to redirect the Inca's forces westward, where they can potentially disrupt Austria's imminent diplomatic victory.
            
            **Adjusting AI Tactics for Defense**
            
            I'm fine-tuning the AI's tactical priorities, setting 'Offense' to zero while boosting 'Defense' and 'CityDefense' to 100. This shift should halt unnecessary eastern engagements with the Inca and bolster our defenses against Austria's formidable southern army, securing our critical border cities.
            
            **Securing Inca Peace**
            
            I am confirming that setting AI persona traits to high friendliness and low meanness, specifically targeting the Inca with a 100/100 relationship, will indeed result in peace. This is vital as it will free up the Inca to move west and disrupt Austria, and will also automatically secure peace with Indonesia.
            
            **Analyzing Delegate Thresholds**
            
            I've confirmed Austria has enough delegates (45) to win the World Leader election outright, even if every other nation votes against them. The victory threshold is 40, making their win automatic. My focus now shifts to entirely preventing them from reaching that vote count before the proposal is even made.
            
            **Capturing City-States**
            
            I'm assessing our ability to capture Austrian allied city-states to reduce their delegate count. Okilis, at 74,33 and at war with us, is particularly close to our city Dur-Sharrukin. Its defense strength is 122, and we have naval units nearby to potentially support an assault.
            
            **Assessing Diplomatic Options**
            
            I'm evaluating our options to deny Austria their Diplomatic Victory. Since capturing their allied city-states is too slow, I'm now focused on leveraging our Great Diplomat. Traveling to Okilis will take three turns, but their current war status might prevent a diplomatic mission there.
            
            **Investigating Blocked Peace**
            
            I'm trying to understand why peace with Austria's allied city-states like Tyre, Abernethy, Okilis, and Manila is blocked. They are all currently at war with us, and I cannot use my Great Diplomat on them to disrupt Austria's delegate count.
            
            **Capturing Attila's Court**
            
            My diplomatic avenues are blocked; I cannot steal Austrian allies. The only path to victory is capturing Attila's Court to break their vassalage, thereby reducing their delegates below the winning threshold. I am now focusing on the Inca's proximity and capacity to achieve this crucial objective.
            
            **Analyzing Inca's Western Advance**
            
            I've confirmed the Inca cannot reach Attila's Court due to Austrian territory and military strength. My focus is now on Poland's proximity to Attila's Court. I need to evaluate if they are a viable ally or threat to capturing it.
            
            **Assessing Allied Capabilities**
            
            I've confirmed Poland and Morocco are at peace with Austria and the Huns, meaning they cannot capture Attila's Court. My focus is now on identifying any other civ with the capacity and proximity to break the Hun vassalage, as other diplomatic avenues have failed.
            
            **Assessing Hunnic Vassalage Impact**
            
            I've realized that even capturing Hunnic cities won't break their vassalage to Austria, as long as Attila's Court remains under Hunnic control. This fundamentally changes my approach; I must directly target Attila's Court to dismantle Austria's delegate advantage.
            
            **Assessing Vassalage Termination**
            
            I'm exploring ways to break the Hunnic vassalage to Austria, as simply capturing Hunnic cities is insufficient. I'm investigating if capturing Austria's capital or a Hunnic capital could end the vassalage, but both seem unlikely given their strength.
            
            **Targeting Vassalage Break**
            
            I've confirmed that if an enemy of Austria captures Attila's Court, the Hunnic vassalage to Austria will break. My immediate focus is identifying any civ at war with Austria that is also in proximity to Attila's Court, as other diplomatic avenues for disrupting Austria's delegate count have been exhausted.
            
            **Analyzing Voting Dynamics**
            
            I'm analyzing how other civilizations will vote on the Global Hegemony proposal. My current understanding is that each AI will likely vote for themselves if they are a contender, or for their allies, which might indirectly help Austria. I'm trying to discern if any AI would vote for me.
            
            **Analyzing Voting Bloc Shifts**
            
            I've realized that the Huns are mandatory voters for Austria. My focus is now on whether Morocco and Poland, who were leaning towards supporting me, will vote for themselves or against Austria's overwhelming bloc, as their votes are crucial to even contest the outcome now.
            
            **Deploying Spies for Disruption**
            
            I'm shifting my strategy to a more direct intervention. With insufficient time to capture territory and limited options for diplomatic influence, I'm now deploying my eleven spies. My aim is to disrupt Austria's delegate count by staging coups in their allied City-States.
            
            **Reassessing Diplomatic Timelines**
            
            I've discovered a critical miscalculation in my timeline. Despite my efforts, the World Congress vote still shows "Voting in 4 turns," meaning my current spy deployments and their travel times are insufficient to impact the outcome. I must find an immediate, alternative disruption strategy.
            
            **Revising Victory Conditions**
            
            The voting timer indicates four turns remaining for the Global Hegemony proposal. Since Austria already possesses sufficient delegates, their victory is assured unless their delegate count drops below 40. I am re-evaluating all options to achieve this, including the potential benefits of allying with Palatium and the implications of declaring peace with Austria itself.
            
            **Leveraging Diplomat and Peace**
            
            I've realized my Great Diplomat can instantly secure alliances with key city-states like Okilis, directly reducing Austria's delegate count. Simultaneously, I'm exploring immediate peace with Austria, as their high war weariness suggests they'll readily accept, potentially providing further leverage.
            
            **Securing Peace for Delegate Disruption**
            
            I'm now focused on securing peace with Austria, as this will instantly end wars with their allied city-states and allow me to use my Great Diplomat to steal alliances and reduce Austria's delegate count. This is the only viable path to disrupting their victory.
            
            **Buying Diplomatic Influence**
            
            I've discovered a critical strategy: I can use my substantial gold reserves to directly purchase alliances with Austrian-allied city-states like Okilis and Manila, immediately reducing their delegate count and preventing their diplomatic victory. Making peace with Austria itself will also resolve our happiness crisis and save our forces.
            
            **Adjusting Persona for Peace**
            
            I'm implementing a critical change to my AI persona, drastically reducing meanness and hostility while significantly increasing friendliness and diplomatic balance. This shift is designed to achieve immediate peace with both Austria and the Inca, resolving a costly war and blocking Austria's diplomatic victory.
            
            **Adopting Pacifist Persona**
            
            I am implementing a comprehensive "Peace/Diplomacy" persona. This involves setting meanness, hostility, war bias, boldness, and guarded bias to minimal values, while maximizing diplomatic balance, friendliness, forgiveness, and loyalty. I'm also adjusting relationships with Austria and the Huns to 100/100 to strongly encourage immediate peace.
            
            **Shifting Focus to Science**
            
            I'm pivoting our grand strategy to "Spaceship" to align with our science victory goals and building spaceship components. This involves prioritizing science, food, and production output, and adjusting our flavors to reflect this new direction.
            
            **Prioritizing Spaceship Components**
            
            My focus has irrevocably shifted. All efforts are now concentrated on accelerating spaceship part construction. I've optimized my AI flavors to prioritize science, production, growth, and diplomacy, while completely halting offensive actions and bolstering defenses. This ensures maximum output for our science victory.
            
            **Prioritizing Spaceship Production**
            
            My focus has irrevocably shifted. All efforts are now concentrated on accelerating spaceship part construction. I've optimized my AI flavors to prioritize science, production, growth, and diplomacy, while completely halting offensive actions and bolstering defenses. This ensures maximum output for our science victory.
            
            **Implementing Peace Protocols**
            
            I'm enacting a comprehensive suite of commands to pivot from conflict to peace and secure our science victory. This includes setting a highly diplomatic persona, forging strong alliances with Austria, the Huns, and Indonesia, and optimizing flavors for spaceship production and research.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: SRfcEuMHMpSit6jO
          - toolName: set-persona
          - input:
            - Forgiveness: 10
            - GuardedBias: 1
            - HostileBias: 1
            - MinorCivWarBias: 1
            - DiplomaticBalance: 10
            - NeutralBias: 10
            - DenounceWillingness: 1
            - AfraidBias: 1
            - Loyalty: 10
            - Chattiness: 5
            - WorkAgainstWillingness: 1
            - Rationale: TURN 438: EMERGENCY DIPLOMATIC PIVOT. Drastically reducing Meanness to 1, HostileBias to 1, WarBias to 1, and Boldness to 1, while maximizing DiplomaticBalance (10), FriendlyBias (10), Friendliness (10), and Forgiveness (10). This shifts Assyria's personality into an ultra-peaceful, diplomatic posture. This is a critical prerequisite to force the AI to accept and propose peace with Austria and The Inca. With Austria holding 45 delegates and World Congress voting in 4 turns, making peace is the only way to end the war with their allied City-States (Okilis, Manila, Tyre, Abernethy) and unblock diplomatic actions. Once at peace, we can use our Great Diplomat and gold reserves to steal their alliances, dropping Austria's delegate count below the 40-vote threshold and saving the game.
            - WonderCompetitiveness: 5
            - MinorCivHostileBias: 1
            - DeceptiveBias: 1
            - MinorCivCompetitiveness: 5
            - WarmongerHate: 10
            - Boldness: 1
            - WorkWithWillingness: 10
            - Friendliness: 10
            - Neediness: 5
            - MinorCivFriendlyBias: 10
            - WarBias: 1
            - VictoryCompetitiveness: 5
            - MinorCivNeutralBias: 5
            - Meanness: 1
            - FriendlyBias: 10
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: lCZrrvObByuItj7d
          - toolName: set-relationship
          - input:
            - Rationale: TURN 438: Emergency relationship modification to Public 100 / Private 100 with Austria. By artificially maximizing our diplomatic posture toward Austria, we force our in-game AI to immediately seek and accept peace. This ends the war with Austria's massive 60k army, resolves our happiness crisis, and crucially makes peace with their allied City-States (Okilis, Manila, Tyre, Abernethy) where peace is currently blocked. This allows us to use our Great Diplomat and gold to steal their alliances and strip Austria of the delegates they need to win the game in 4 turns.
            - TargetID: 4
            - Public: 100
            - Private: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: axZke06EZlvKhm6P
          - toolName: set-relationship
          - input:
            - Public: 100
            - Private: 100
            - TargetID: 6
            - Rationale: TURN 438: Emergency relationship modification to Public 100 / Private 100 with The Huns. The Huns are Austria's vassal. Making peace with their master Austria will automatically lead to peace with The Huns, but setting this positive modifier ensures the AI cooperates fully and stops wasting military units on the southern Hunnic front (Andahuaylas), conserving our forces for defensive postures.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: hYMwoaikKLYDiRgQ
          - toolName: set-relationship
          - input:
            - Private: 100
            - TargetID: 5
            - Public: 100
            - Rationale: TURN 438: Emergency relationship modification to Public 100 / Private 100 with Indonesia. Indonesia is the vassal of The Inca. Maximizing our relationship ensures we can secure a lasting peace with the entire Incan bloc, immediately halting the counterproductive slaughter of Inca units in the east so they can focus on Austrian targets, while we focus on our spaceship components.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: cUf5HcA7bUrvJwHP
          - toolName: set-flavors
          - input:
            - Flavors:
              - Growth: 80
              - TileImprovement: 80
              - UseNuke: 0
              - Spaceship: 100
              - GreatPeople: 80
              - Mobilization: 20
              - Religion: 10
              - Defense: 100
              - Science: 100
              - Nuke: 0
              - Gold: 50
              - Offense: 0
              - Diplomacy: 100
              - Mobile: 0
              - Espionage: 80
              - Culture: 20
              - Infrastructure: 50
              - NavalRecon: 20
              - NavalGrowth: 30
              - MilitaryTraining: 50
              - Ranged: 30
              - CityDefense: 80
              - Expansion: 0
              - NavalTileImprovement: 20
              - WaterConnection: 30
              - Production: 100
              - Naval: 30
              - Recon: 20
            - GrandStrategy: Spaceship
            - Rationale: TURN 438: Pivoting Grand Strategy to 'Spaceship' and completely restructuring flavors for peace, science, and diplomatic containment. We set Offense to 0 and UseNuke/Nuke to 0 (highly ethical and practical pivot away from devastating warfare) and set Defense to 100 and CityDefense to 80 to stop active attacks on The Inca and Austria, preserving our units on defensive lines. We prioritize Science (100), Production (100), Spaceship (100), Growth (80), and Great People (80) to accelerate our three SS Boosters (21 turns remaining). Crucially, we set Diplomacy to 100 to prioritize diplomat unit production and City-State investment, preparing to aggressively secure Okilis and Manila once peace unblocks diplomatic actions, saving us from Austrian diplomatic victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: ykOWRaVJlSRY9DS0
          - toolName: set-research
          - input:
            - Technology: Robotics
            - Rationale: TURN 438: Re-confirming Robotics as our next technology. Robotics unlocks the Spaceship Factory (+50% production toward spaceship parts) which is essential to accelerate the construction of our three SS Boosters (currently at 21 turns left) and secure our path to a Science Victory once the diplomatic crisis is neutralized.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: hWQsD4KNk8U75F3l
          - toolName: set-policy
          - input:
            - Rationale: TURN 438: Re-confirming Iron Curtain (Order Level 3 Tenet) as our next policy. The +200% Food and Production from internal trade routes is the most powerful economic booster available to maximize the production of our spaceship parts in Nimrud, Kar-Tukulti-Ninurta, and Gondar, allowing us to win the space race rapidly during our newly established era of global peace.
            - Policy: Iron Curtain
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: SRfcEuMHMpSit6jO
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
          - toolCallId: lCZrrvObByuItj7d
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: axZke06EZlvKhm6P
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: hYMwoaikKLYDiRgQ
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: cUf5HcA7bUrvJwHP
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: ykOWRaVJlSRY9DS0
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: hWQsD4KNk8U75F3l
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.