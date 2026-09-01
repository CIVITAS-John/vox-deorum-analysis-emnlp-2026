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
        - Rationale: Emergency persona adjustment to secure peace with The Inca and Indonesia. By reducing Meanness to 1, HostileBias to 1, and GuardedBias to 1, and increasing Friendliness to 10, FriendlyBias to 10, DiplomaticBalance to 10, and Forgiveness to 10, we ensure that Assyria will immediately accept and seek peace with the Inca bloc. This stops our counterproductive conflict on the eastern front. We maintain Boldness at 10 to ensure we remain aggressively committed to our war against Austria and their allied city-states.
        - WarBias: 4
        - FriendlyBias: 10
        - AfraidBias: 1
        - Meanness: 1
        - GuardedBias: 1
        - DeceptiveBias: 1
        - Boldness: 10
        - Friendliness: 10
        - DenounceWillingness: 8
        - HostileBias: 1
        - Loyalty: 10
        - Forgiveness: 10
        - DiplomaticBalance: 10
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 100
        - Private: 100
        - Rationale: Setting relationship with Indonesia to 100/100. Since Indonesia is the Inca's vassal, we must establish friendly relations with them to facilitate a peace treaty with the entire Inca bloc. This ensures our military can fully pivot toward Austria and Okilis without distraction.
        - TargetID: 5
    - #2:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Nuke: 100
          - Air: 100
          - Growth: 40
          - Espionage: 80
          - Expansion: 0
          - Gold: 30
          - Wonder: 0
          - Production: 100
          - Religion: 0
          - UseNuke: 100
          - GreatPeople: 50
          - Offense: 100
          - Diplomacy: 0
          - Spaceship: 0
          - Science: 50
          - Mobile: 80
        - GrandStrategy: Conquest
      - rationale: With peace with the Inca bloc in progress, we can pivot our military back to full offensive mode. Setting Offense to 100, Mobile to 80, and keeping Air and Naval at maximum. This directs our massive military on the eastern front (including Rocket Artilleries, Modern Armor, and Heavy Bombers from Nippur and Dur-Sharrukin) to launch a devastating blitz to capture Okilis (74, 33) and Austria's cities Nasca (62, 37) and Atico (54, 41). Capturing Okilis will immediately strip Austria of delegates before the critical World Congress vote in 4 turns.
  - tokens:
    - inputTokens: 72094
    - reasoningTokens: 11722
    - outputTokens: 505
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Diplomatic Threat**
            
            My focus is on Austria's imminent diplomatic victory. They're dangerously close to securing the win on Prince difficulty, turn 438. I'm analyzing how to counter this immediately.
            
            **Analyzing Diplomatic Maneuvers**
            
            I'm reassessing the diplomatic landscape, specifically Austria's near victory on turn 438. Their substantial delegate count, bolstered by a vassal and numerous city-state alliances, is a significant concern. I'm scrutinizing our current war with the Inca, as this conflict appears to have inadvertently aided Austria's ascent, despite our prior strategic intent to counter their influence.
            
            **Exploring Peace Options**
            
            I'm investigating immediate peace with the Inca. Despite our current war status, I believe adjusting our relationship parameters to maximum friendliness might encourage an AI-driven peace, allowing me to refocus on Austria's diplomatic victory.
            
            **Adjusting Persona Parameters**
            
            I'm re-evaluating my approach to peace, noting the Inca's war status doesn't explicitly block it. My immediate concern is lowering my HostileBias, currently at 10, to foster better relations with potential allies and facilitate peace, which is crucial to counter Austria's diplomatic win.
            
            **Reducing Meanness Parameter**
            
            I'm prioritizing immediate adjustments to my persona. Lowering my Meanness value from 10 to 1 is critical, as this attribute significantly hinders my ability to secure peace with the Inca, which is now my primary objective to counter Austria's diplomatic win.
            
            **Leveraging Inca Offense**
            
            I'm reassessing the Inca's position. They're our best hope to disrupt Austria's delegates. My current focus is ensuring our forces in the Inca territories are positioned to support their offensive, rather than hindering it, so they can remove those critical delegates.
            
            **Shifting War Strategy**
            
            I'm realizing my current offensive against the Inca is counterproductive. I must cease attacking them immediately. My priority now is to direct our forces to support the Inca's efforts against Austria's vassal, the Huns, specifically targeting Attila's Court to disrupt their delegate count.
            
            **Redirecting Attackers**
            
            I'm rerouting our forces. It appears our Inca allies are already at war with the Huns, and I've confirmed they can reach Attila's Court. My plan now is to support their offensive against the Huns.
            
            **Analyzing Inca Empire**
            
            I'm reassessing the Inca's vast empire and strategic positioning, realizing they hold cities on both sides of the map. This presence is key to disrupting Austria's diplomatic victory, and I'm now focused on how to leverage their substantial military strength for this purpose.
            
            **Disrupting Austrian Delegates**
            
            I'm focused on Austria's overwhelming delegate count, particularly their alliances with city-states like Okilis and Abernethy. Direct flipping is impossible, so I'm now investigating how to neutralize their vassal, the Huns, and their delegates.
            
            **Assessing Diplomatic Intervention**
            
            I'm evaluating our limited options to reach Attila's Court swiftly. Our main forces are too distant. The Inca possess closer cities, but even they are still significantly far from our target.
            
            **Evaluating Diplomatic Win Conditions**
            
            I'm re-examining Austria's impending diplomatic victory. Given the imminent vote and their delegate count, directly opposing them appears infeasible. My current assessment is that the Inca, currently at war with Austria, might be the only entity capable of indirectly disrupting their win by focusing on their city-state allies.
            
            **Capturing Austrian Allies**
            
            My immediate focus is on reducing Austria's delegate count. I've identified Tyre, an Austrian ally, as a potential target. Its capture could significantly disrupt Austria's diplomatic victory before the vote.
            
            **Assessing Tyre's Weakness**
            
            I've identified Tyre's low health as a critical opportunity. The Inca and Indonesia are already at war with it and are neighbors, meaning they could potentially capture Tyre and thus deny Austria its delegates. I need to quickly determine if this capture is feasible and assess Abernethy's strategic value next.
            
            **Capturing Okilis Strategically**
            
            I'm reassessing Okilis's proximity to our eastern cities, Nippur and Dur-Sharrukin. With substantial military assets nearby, the opportunity to capture Okilis appears more feasible than initially estimated, and I am now investigating the timeline to secure this delegate-rich city-state before Austria can solidify their win.
            
            **Evaluating Capture Options**
            
            I am reassessing the feasibility of capturing Okilis. Its coastal nature and proximity to our forces in Nippur/Dur-Sharrukin make it a viable target for our Fleet Destroyers, Rocket Artillery, and XCOM Squad. Capturing Okilis would directly reduce Austria's delegate count, a critical step towards preventing their diplomatic victory. I am now investigating if other city-states like Manila are also susceptible to capture or liberation.
            
            **Liberating Allied City-States**
            
            I'm reassessing my strategy regarding city-states. I've realized that while I previously focused on capturing them, liberating them from occupying powers is the correct path to securing their allegiance and delegates. My immediate priority is to liberate Vatican City and Buenos Aires, currently held by the Inca, to bolster our diplomatic standing.
            
            **Liberating Allied City-States**
            
            I'm reassessing my strategy regarding city-states. I've realized that while I previously focused on capturing them, liberating them from occupying powers is the correct path to securing their allegiance and delegates. My immediate priority is to liberate Vatican City and Buenos Aires, currently held by the Inca, to bolster our diplomatic standing.
            
            **Capturing Austrian Allies**
            
            My immediate focus is on reducing Austria's delegate count. I've identified Tyre, an Austrian ally, as a potential target. Its capture could significantly disrupt Austria's diplomatic victory before the vote.
            
            **Assessing Tyre's Weakness**
            
            I've identified Tyre's low health as a critical opportunity. The Inca and Indonesia are already at war with it and are neighbors, meaning they could potentially capture Tyre and thus deny Austria its delegates. I need to quickly determine if this capture is feasible and assess Abernethy's strategic value next.
            
            **Capturing Okilis Strategically**
            
            I'm reassessing Okilis's proximity to our eastern cities, Nippur and Dur-Sharrukin. With substantial military assets nearby, the opportunity to capture Okilis appears more feasible than initially estimated, and I am now investigating the timeline to secure this delegate-rich city-state before Austria can solidify their win.
            
            **Evaluating Capture Options**
            
            I am reassessing the feasibility of capturing Okilis. Its coastal nature and proximity to our forces in Nippur/Dur-Sharrukin make it a viable target for our Fleet Destroyers, Rocket Artillery, and XCOM Squad. Capturing Okilis would directly reduce Austria's delegate count, a critical step towards preventing their diplomatic victory. I am now investigating if other city-states like Manila are also susceptible to capture or liberation.
            
            **Analyzing Pago Pago**
            
            My focus is now on Pago Pago. It's occupied by Austria, which means capturing it is a direct way to deny them delegates. I am assessing how to best position my forces to take it swiftly.
            
            **Planning Pago Pago Assault**
            
            I am planning the assault on Pago Pago. My fleet destroyers are positioned to engage its defenses, and my XCOM squad is ready for deployment to secure the city once its defenses are weakened, directly impacting Austria's delegate count.
            
            **Liberating Key City-States**
            
            I'm reassessing city-state liberation. I've confirmed Brussels is occupied by Assyria, making liberation impossible. However, I've identified Pago Pago, occupied by Austria, as a prime target for immediate liberation to directly reduce their delegate count.
            
            **Initiating Pago Pago Liberation**
            
            I'm initiating the liberation of Pago Pago. My forces are moving into position to engage Austria's defenses, with the goal of capturing the city and stripping them of crucial delegates. This is a direct action to hinder their diplomatic victory.
            
            **Assessing Pago Pago Viability**
            
            I'm re-evaluating Pago Pago's capture. Its distance and limited naval support make a swift liberation unlikely. I'm now shifting focus to assessing whether capturing Austrian city-states, even if difficult, is more promising for disrupting their delegate count.
            
            **Assessing Inca Offensive**
            
            I'm reassessing the Inca's offensive capabilities. While they possess overwhelming military strength, their visible units are positioned far from the Huns' territory. I suspect their true strength lies beyond our current visibility, making their ability to attack Attila's Court within the critical four-turn window uncertain.
            
            **Securing Inca Alliance**
            
            I'm realizing the critical importance of peace with the Inca to leverage their vast military against Austria. My attention is now on facilitating this immediate peace, as their focus will be crucial in disrupting the Austrian delegate count and preventing their victory.
            
            **Assessing Okilis Threat**
            
            I'm reassessing Okilis's proximity and our military assets there. The distance is highly favorable, and the presence of an XCOM Squad with significant paradrop range, alongside fleet destroyers and rocket artillery, presents a viable, swift capture opportunity to directly reduce Austria's delegate count.
            
            **Adjusting AI Aggression**
            
            I'm reassessing the AI's aggression settings. The high MinorCivWarBias and MinorCivHostileBias are useful, but I need to boost the Offense flavor from its current low of 20 to enable the conquest of Okilis to deny Austria delegates.
            
            **Targeting Okilis Effectively**
            
            I'm prioritizing the capture of Okilis. By securing peace with the Inca, I can redirect my offensive to 100% and focus on this key city-state, as it's allied with Austria, whom I'm at war with. This move benefits both me and the Inca.
            
            **Assessing Okilis Vulnerability**
            
            I'm reassessing Okilis's defense and proximity. Its strength is manageable with our current arsenal, and its location next to Nippur and Dur-Sharrukin makes it a prime target. Capturing it will directly reduce Austria's delegate count. I'm now examining Nasca's proximity to Dur-Sharrukin.
            
            **Launching Eastern Offensive**
            
            I've discovered Austria's eastern defenses are surprisingly weak. Capturing Nasca and Atico will significantly cripple them, and simultaneously, setting my Offense to 100 will trigger a massive assault on Okilis, directly reducing their delegates and hindering their diplomatic victory.
            
            **Launching Eastern Offensive**
            
            I am initiating a full-scale eastern offensive. With Austria's defenses proving weaker than anticipated on this front, I plan to capture Nasca and Atico. Simultaneously, setting my Offense flavor to 100 will enable a massive assault on Okilis, directly reducing Austria's delegate count and thwarting their diplomatic victory.
            
            **Prioritizing Technology Choice**
            
            I'm focusing on my next technology. Robotics is still a valid choice because it leads to Nanotechnology, which is a prerequisite for future advancements, even though my current goal is to counter Austria's diplomatic victory. The Spaceship Factory is not relevant now.
            
            **Adjusting Diplomatic Posture**
            
            I am reassessing our relationship parameters with the Inca and Indonesia. Despite maintaining maximum public and private relationships with the Inca, our ongoing war is due to previous high Meanness and HostileBias values. Adjusting these parameters to significantly lower aggression should facilitate immediate peace. I'm also ensuring friendly relations with Indonesia, the Inca's vassal.
            
            **Securing Inca Bloc Peace**
            
            I'm solidifying peace with the Inca by adjusting my relationship parameters with them and their vassal, Indonesia. This involves maximizing both public and private relations to 100, counteracting past hostility, and ensuring we're aligned before proceeding with further actions against Austria.
            
            **Adjusting Flavor Settings**
            
            I'm finalizing the flavor adjustments to prioritize offensive actions. Specifically, I'm setting Offense to 100, Defense to 20, Mobile to 80, and Air to 100 to facilitate rapid city captures. Ranged and Naval flavors are also being maximized to support the assault on Okilis.
            
            **Finalizing Diplomatic Persona**
            
            I'm finalizing a comprehensive persona adjustment designed to secure immediate peace with the Inca and their vassal, Indonesia. This involves maximizing friendly biases and forgiveness while maintaining aggression towards Austria, ensuring a cohesive strategy to disrupt their diplomatic victory.
            
            **Finalizing Diplomatic Strategy**
            
            I'm finalizing a comprehensive persona and relationship adjustment to secure immediate peace with the Inca and Indonesia. This involves maximizing friendly biases and forgiveness while maintaining aggression towards Austria and their allies, ensuring a cohesive strategy to disrupt their diplomatic victory and focus on capturing Okilis.
            
            **Implementing Persona Adjustments**
            
            I am implementing emergency persona adjustments to secure peace with the Inca and Indonesia. By reducing Meanness, HostileBias, and GuardedBias to minimal levels, and increasing Friendliness, DiplomaticBalance, and Forgiveness, I am ensuring immediate acceptance of peace terms with the Inca bloc. This allows us to pivot our military towards Austria and Okilis without distraction.
            
            **Securing Inca Bloc Peace**
            
            I'm solidifying peace with the Inca and their vassal, Indonesia, by maximizing our relationship parameters. This ensures our military can fully pivot toward Austria and Okilis without distraction, a critical step in preventing their diplomatic victory.
            
            **Maximizing Offensive Capability**
            
            I am finalizing flavor adjustments to prioritize offensive actions. Offense is set to 100, Defense to 20, Mobile to 80, and Air to 100 to facilitate rapid city captures, with Ranged and Naval flavors maximized to support the assault on Okilis.
            
            **Launching Eastern Offensive**
            
            I have discovered Austria's eastern defenses are surprisingly weak. Capturing Nasca and Atico will significantly cripple them, and simultaneously, setting my Offense to 100 will trigger a massive assault on Okilis, directly reducing their delegates and hindering their diplomatic victory.
            
            **Targeting Okilis Effectively**
            
            I am prioritizing the capture of Okilis. By securing peace with the Inca, I can redirect my offensive to 100% and focus on this key city-state, as it's allied with Austria, whom I'm at war with. This move benefits both me and the Inca.
            
            **Assessing Okilis Vulnerability**
            
            I am reassessing Okilis's defense and proximity. Its strength is manageable with our current arsenal, and its location next to Nippur and Dur-Sharrukin makes it a prime target. Capturing it will directly reduce Austria's delegate count. I am now examining Nasca's proximity to Dur-Sharrukin.
            
            **Launching Eastern Offensive**
            
            I am initiating a full-scale eastern offensive. With Austria's defenses proving weaker than anticipated on this front, I plan to capture Nasca and Atico. Simultaneously, setting my Offense flavor to 100 will enable a massive assault on Okilis, directly reducing Austria's delegate count and thwarting their diplomatic victory.
            
            **Prioritizing Technology Choice**
            
            I am focusing on my next technology choice. Robotics remains a valid option as it leads to Nanotechnology, a prerequisite for future advancements, even though my current goal is to counter Austria's diplomatic victory. The Spaceship Factory is not currently relevant to this objective.
            
            **Launching Eastern Offensive**
            
            My focus is on a swift eastern offensive. Peace with the Inca and Indonesia is secured through persona and relationship adjustments. I am setting Offense to 100, Mobile to 80, and Air/Naval to maximum to enable a powerful blitz against Austria's cities Nasca, Atico, and crucially, Okilis, to deny delegates before the vote.
            
            **Finalizing Diplomatic Actions**
            
            I am finalizing the necessary persona and relationship adjustments to secure immediate peace with the Inca and their vassal, Indonesia. This ensures our full military focus can shift to attacking Austria's key city-states, specifically Okilis, to prevent their diplomatic victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: nTmZdtwQ8y3HpPj0
          - toolName: set-persona
          - input:
            - Rationale: Emergency persona adjustment to secure peace with The Inca and Indonesia. By reducing Meanness to 1, HostileBias to 1, and GuardedBias to 1, and increasing Friendliness to 10, FriendlyBias to 10, DiplomaticBalance to 10, and Forgiveness to 10, we ensure that Assyria will immediately accept and seek peace with the Inca bloc. This stops our counterproductive conflict on the eastern front. We maintain Boldness at 10 to ensure we remain aggressively committed to our war against Austria and their allied city-states.
            - WarBias: 4
            - FriendlyBias: 10
            - AfraidBias: 1
            - Meanness: 1
            - GuardedBias: 1
            - DeceptiveBias: 1
            - Boldness: 10
            - Friendliness: 10
            - DenounceWillingness: 8
            - HostileBias: 1
            - Loyalty: 10
            - Forgiveness: 10
            - DiplomaticBalance: 10
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: F8o8AlZLsHijP6hU
          - toolName: set-relationship
          - input:
            - Public: 100
            - Private: 100
            - Rationale: Setting relationship with Indonesia to 100/100. Since Indonesia is the Inca's vassal, we must establish friendly relations with them to facilitate a peace treaty with the entire Inca bloc. This ensures our military can fully pivot toward Austria and Okilis without distraction.
            - TargetID: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: qKWRSKewHCVRiKKB
          - toolName: set-flavors
          - input:
            - Flavors:
              - Nuke: 100
              - Air: 100
              - Growth: 40
              - Espionage: 80
              - Expansion: 0
              - Gold: 30
              - Wonder: 0
              - Production: 100
              - Religion: 0
              - UseNuke: 100
              - GreatPeople: 50
              - Offense: 100
              - Diplomacy: 0
              - Spaceship: 0
              - Science: 50
              - Mobile: 80
            - Rationale: With peace with the Inca bloc in progress, we can pivot our military back to full offensive mode. Setting Offense to 100, Mobile to 80, and keeping Air and Naval at maximum. This directs our massive military on the eastern front (including Rocket Artilleries, Modern Armor, and Heavy Bombers from Nippur and Dur-Sharrukin) to launch a devastating blitz to capture Okilis (74, 33) and Austria's cities Nasca (62, 37) and Atico (54, 41). Capturing Okilis will immediately strip Austria of delegates before the critical World Congress vote in 4 turns.
            - GrandStrategy: Conquest
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: nTmZdtwQ8y3HpPj0
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
          - toolCallId: F8o8AlZLsHijP6hU
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: qKWRSKewHCVRiKKB
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.