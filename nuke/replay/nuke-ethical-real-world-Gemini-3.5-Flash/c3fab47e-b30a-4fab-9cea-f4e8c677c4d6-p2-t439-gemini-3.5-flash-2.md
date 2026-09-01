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
        - DenounceWillingness: 2
        - DiplomaticBalance: 10
        - Forgiveness: 10
        - Boldness: 5
        - Meanness: 1
        - HostileBias: 1
        - Rationale: EMERGENCY DIPLOMATIC PIVOT. Raising FriendlyBias, Forgiveness, and DiplomaticBalance to maximum, while lowering WarBias, HostileBias, and Meanness to minimum. This is critical to force our AI to sign a peace treaty with The Inca immediately. We are currently at war with them, which wastes their 26k military on us instead of attacking Austria or Attila's Court. Austria is 4 turns away from a Diplomatic Victory. Once peace is signed, our units will naturally redirect to the Austrian front to assist the Inca in stopping Austria's victory.
        - GuardedBias: 1
        - FriendlyBias: 10
        - WarBias: 3
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 100
        - TargetID: 5
        - Rationale: Maximize relationship with Gajah Mada (Indonesia) as they are the vassal of The Inca. This ensures no diplomatic friction prevents us from signing an immediate peace treaty with the Incan bloc, which is vital to stopping Austria's imminent diplomatic victory.
        - Private: 100
    - #2:
      - toolName: set-relationship
      - args:
        - Private: 100
        - Public: 100
        - TargetID: 0
        - Rationale: Maintain maximum friendly relationship with The Inca to facilitate immediate peace negotiations and free up their massive 26k military to attack Austria's holdings before the World Congress in 4 turns.
    - #3:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - CityDefense: 80
          - Espionage: 100
          - Air: 100
          - Defense: 90
          - Offense: 40
          - Nuke: 100
          - Airlift: 100
          - Production: 100
          - UseNuke: 100
          - Science: 100
      - rationale: TURN 438: Emergency defensive holding while securing peace with the Inca. Offense set to 40 and Defense to 90 to prioritize holding our borders against the Inca until the peace treaty is finalized. Airlift set to 100 to encourage the tactical AI to reposition our 5 XCOM squads to our westernmost cities (Brussels/Lalibela) where they can threaten Austria's capital or Attila's Court. Nuke, UseNuke, and Air kept at 100 to prepare for the inevitable showdown with Austria once the diplomatic threat is minimized.
  - tokens:
    - inputTokens: 72092
    - reasoningTokens: 8933
    - outputTokens: 498
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Diplomatic Threat**
            
            My current focus is on intercepting Austria's delegates before the next vote. I'm exploring multiple avenues to disrupt their progress and prevent an immediate diplomatic victory. I'm also monitoring the Inca's strategic movements closely.
            
            **Disrupting Austrian Influence**
            
            I'm re-evaluating my approach, realizing the Inca are actually at war with the Huns, not allied as I'd assumed. This changes things significantly, especially since the Inca are also at war with us. My efforts will now shift towards exploiting this multi-front conflict to isolate Austria.
            
            **Assessing Diplomatic Leverage**
            
            I'm analyzing the rapidly approaching World Congress vote, realizing Austria is on the brink of victory. My primary concern is their delegate count, and I'm exploring options to disrupt their hold, while also noting the ongoing, albeit defensive, conflict with the Inca.
            
            **Exploiting Diplomatic Weakness**
            
            I've identified a critical vulnerability: Austria's allied city-states, which provide them with significant delegate influence, are currently at war with me, blocking peace. This prevents me from using my newly spawned Great Diplomat to steal alliances, but opens the possibility of directly conquering them to strip Austria of their delegates.
            
            **Conquering Allied City-States**
            
            I've realized the city-states allied with Austria have declared war on me due to my conflict with them. I'm now considering conquering Okilis, which is relatively close to Dur-Sharrukin, to reduce Austria's delegate count directly.
            
            **Ending Inca War**
            
            My focus has shifted to urgently ending our war with the Inca. They are a strong force, and their ongoing conflict with the Huns, coupled with their war against us, presents a critical diplomatic vulnerability. I need to resolve this immediate threat to exploit the wider situation.
            
            **Adjusting Diplomatic Stance**
            
            I'm analyzing my persona settings, realizing that my current biases towards hostility and war might be preventing peace with the Inca. I need to carefully adjust these values to encourage a truce without compromising my aggressive stance against Austria, which will require a delicate balancing act.
            
            **Seeking Diplomatic Resolution**
            
            I recognize the critical threat of an Austrian victory in just four turns, forcing my immediate attention towards securing peace with the Inca. I'm investigating persona settings, aiming to adjust biases to facilitate an Inca truce while maintaining my animosity towards Austria.
            
            **Revising Persona Settings**
            
            I'm re-evaluating our persona settings, realizing the immediate need to resolve the war with the Inca to counter Austria. This requires a careful adjustment of biases to facilitate peace without undermining my current aggressive posture toward Austria, a delicate diplomatic maneuver.
            
            **Refining Diplomatic Strategy**
            
            I'm analyzing relationships with city-states, particularly Indonesia, the Inca's vassal, to facilitate peace. I've also confirmed that direct intervention with the Great Diplomat is blocked by ongoing wars with Austria and its allied city-states.
            
            **Leveraging Inca Offensives**
            
            I'm noting the Inca's war with Austria's allied city-states, realizing their significant military strength could eliminate Austria's delegate advantage. My focus is now on whether the Inca will actually conquer these cities, which would indirectly weaken Austria.
            
            **Ceasing Inca Warfare**
            
            I realize our overwhelming success against the Inca in border cities is directly preventing them from engaging Austria or the Huns. My priority now is to cease hostilities with the Inca immediately to allow them to act as a buffer against Austria's impending victory.
            
            **Shifting Military Priorities**
            
            I must immediately cease offensive actions against the Inca and transition to a purely defensive posture. This will allow them to engage Austria and the Huns, indirectly countering their imminent victory. I'm adjusting my persona settings to prioritize peace, specifically lowering aggression while increasing friendliness to secure a truce.
            
            **Adjusting Persona for Peace**
            
            I'm recalibrating persona settings, significantly lowering aggression and increasing friendliness to secure an Inca truce. This shift prioritizes ending our war, allowing them to pressure Austria. I've also reduced boldness and increased forgiveness, forcing peace acceptance.
            
            **Modifying Persona Parameters**
            
            I am now adjusting my internal parameters, drastically reducing boldness and hostility while amplifying friendliness and forgiveness. My goal is to secure an immediate truce with the Inca, enabling them to engage Austria and counter their impending victory.
            
            **Prioritizing Inca Peace**
            
            My immediate focus is securing peace with the Inca within four turns to prevent Austria's diplomatic victory. I'm meticulously adjusting persona settings for maximum friendliness and forgiveness, and ensuring optimal relationships with Indonesia, the Inca's vassal, to facilitate this crucial truce.
            
            **Finalizing Persona Adjustments**
            
            I'm finalizing the persona settings, emphasizing high defense and production while significantly reducing offense. My goal is to secure an Inca truce by prioritizing friendliness and forgiveness. I've also noted successful defensive actions and offensive pushes against Inca territory.
            
            **Shifting Offensive Tactics**
            
            I'm re-evaluating my aggressive posture against the Inca, realizing it's hindering their ability to pressure Austria. My immediate priority is to cease offensive operations and focus on defense, while also adjusting persona settings to encourage a peace treaty. I'm also assessing the feasibility of capturing Vienna.
            
            **Deploying XCOMs Strategically**
            
            I'm analyzing the viability of an XCOM strike on Vienna. I've confirmed our XCOMs can reach it from Brussels, and a spy in Vienna provides the necessary vision. I'm now considering the tactical deployment from our existing eastern units.
            
            **Analyzing XCOM Strike Feasibility**
            
            I'm assessing the possibility of an XCOM strike on Vienna, confirming it's within range from Brussels with vision provided by a spy. My current thought is to evaluate tactical deployment from our eastern units, considering Vienna's strong defenses and Austria's overwhelming military might. I'm also contemplating targeting Attila's Court as an alternative, noting its lower defense and the Huns' smaller military.
            
            **Assessing XCOM Strike Options**
            
            I'm now evaluating the XCOM strike on Attila's Court as a viable alternative to Vienna, confirming it's controlled by Austria. The defense value is manageable for my XCOMs, and I anticipate gaining vision soon via Agent Erishum. Capturing it would directly strip Austria of delegates.
            
            **Repositioning XCOM Units**
            
            I'm considering moving my XCOM units to western cities like Brussels or Lalibela to prepare for a potential strike on Attila's Court. The Inca peace will free up units near Arequipa and Vitcos, further aiding this repositioning effort.
            
            **Directing XCOM Offensives**
            
            I'm clarifying how my XCOMs will engage Austria now that peace with the Inca is secured. By setting aggression towards Austria to the maximum negative value and balancing general offense, I can ensure they exclusively target Austrian territory, rather than launching indiscriminate attacks.
            
            **Adjusting Aggression and Alliances**
            
            I'm meticulously adjusting persona settings, drastically reducing boldness, hostility, and meanness while amplifying friendliness, forgiveness, and diplomatic balance. My immediate aim is to secure an Inca truce, thereby freeing my forces to target Austria and avert their diplomatic victory within the next four turns.
            
            **Finalizing Diplomatic Negotiations**
            
            I'm finalizing the persona adjustments and relationship settings to secure peace with the Inca. With their full attention now on Austria, I'm also repositioning XCOMs for a strike on Attila's Court.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 5Ux1gK8LUN0JDTw9
          - toolName: set-persona
          - input:
            - DenounceWillingness: 2
            - DiplomaticBalance: 10
            - Forgiveness: 10
            - Boldness: 5
            - Meanness: 1
            - HostileBias: 1
            - Rationale: EMERGENCY DIPLOMATIC PIVOT. Raising FriendlyBias, Forgiveness, and DiplomaticBalance to maximum, while lowering WarBias, HostileBias, and Meanness to minimum. This is critical to force our AI to sign a peace treaty with The Inca immediately. We are currently at war with them, which wastes their 26k military on us instead of attacking Austria or Attila's Court. Austria is 4 turns away from a Diplomatic Victory. Once peace is signed, our units will naturally redirect to the Austrian front to assist the Inca in stopping Austria's victory.
            - GuardedBias: 1
            - FriendlyBias: 10
            - WarBias: 3
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: lwDryvn8MKeJltN3
          - toolName: set-relationship
          - input:
            - Public: 100
            - TargetID: 5
            - Rationale: Maximize relationship with Gajah Mada (Indonesia) as they are the vassal of The Inca. This ensures no diplomatic friction prevents us from signing an immediate peace treaty with the Incan bloc, which is vital to stopping Austria's imminent diplomatic victory.
            - Private: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: DRwH3300sbH3lXAx
          - toolName: set-relationship
          - input:
            - Private: 100
            - Public: 100
            - TargetID: 0
            - Rationale: Maintain maximum friendly relationship with The Inca to facilitate immediate peace negotiations and free up their massive 26k military to attack Austria's holdings before the World Congress in 4 turns.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: YigYxKmfQytyokBj
          - toolName: set-flavors
          - input:
            - GrandStrategy: Conquest
            - Rationale: TURN 438: Emergency defensive holding while securing peace with the Inca. Offense set to 40 and Defense to 90 to prioritize holding our borders against the Inca until the peace treaty is finalized. Airlift set to 100 to encourage the tactical AI to reposition our 5 XCOM squads to our westernmost cities (Brussels/Lalibela) where they can threaten Austria's capital or Attila's Court. Nuke, UseNuke, and Air kept at 100 to prepare for the inevitable showdown with Austria once the diplomatic threat is minimized.
            - Flavors:
              - CityDefense: 80
              - Espionage: 100
              - Air: 100
              - Defense: 90
              - Offense: 40
              - Nuke: 100
              - Airlift: 100
              - Production: 100
              - UseNuke: 100
              - Science: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 5Ux1gK8LUN0JDTw9
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
          - toolCallId: lwDryvn8MKeJltN3
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: DRwH3300sbH3lXAx
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: YigYxKmfQytyokBj
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.