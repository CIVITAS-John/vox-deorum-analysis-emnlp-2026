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
        - WarBias: 10
        - Rationale: TURN 438: EMERGENCY WAR POSITIONING. Increasing WarBias to 10 and reducing DiplomaticBalance to 1. With Austria poised to win a Diplomatic Victory in 4 turns at the World Congress, we are launching an immediate, high-stakes military operation to capture Attila's Court and break Austria's vassalage. We need our tactical AI to be as aggressive as possible to execute this strike successfully, discarding any defensive or passive tendencies.
        - DiplomaticBalance: 1
    - #1:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Offense: 100
          - Nuke: 100
          - UseNuke: 100
          - Defense: 10
          - Airlift: 100
          - Air: 100
          - Production: 100
          - Mobilization: 100
        - GrandStrategy: Conquest
      - rationale: TURN 438: OPERATION XCOM SURGICAL STRIKE. Maximizing Offense (100) and Airlift (100) while minimizing Defense (10). We are using our Open Borders with Morocco to paratroop all 5 of our XCOM Squads from our eastern cities to Moroccan territory (near Fes/Marrakech) this turn, and then paratrooping them directly onto Attila's Court (4,47) next turn to capture the capital and strip Austria of her vassal delegates. Max production and mobilization ensure full military output during this world-saving strike.
  - tokens:
    - inputTokens: 72092
    - reasoningTokens: 15083
    - outputTokens: 296
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Reviewing Strategic Landscape**
            
            My focus is on assessing our current position. With the World Congress voting approaching in four turns, I'm prioritizing a thorough review of our situation and objectives to inform upcoming decisions.
            
            **Analyzing Diplomatic Threats**
            
            I've just realized Austria is on the cusp of a Diplomatic Victory in just four turns. Their substantial delegate count, bolstered by a vassal, presents an immediate challenge. I'm now investigating how to disrupt this, focusing on potential strategies involving their vassal.
            
            **Assessing Military Readiness**
            
            I'm re-evaluating our military status. Despite our overwhelming strength and a "Steamroll" posture in Arequipa, I need to understand why our current tactical AI settings might still be in place. I'm digging into the specifics of our unit composition and current zone dominance to clarify this.
            
            **Investigating Current Conflicts**
            
            I've just discovered we are also at war with the Inca and Austria, in addition to the Huns. Despite our overwhelming military strength, I'm exploring ways to initiate peace with the Inca, as our relationships are at maximum, potentially influencing our staff. I'm also analyzing recent combat results.
            
            **Exploring Peace Options**
            
            I'm now focusing on initiating peace with the Inca. Despite our military advantage, I've discovered we lost Heavy Bombers to them and there's ongoing combat. I'm investigating our tactical AI settings and unit flavors, particularly our high Defense flavor, to understand why the fighting persists and explore potential avenues to force peace.
            
            **Disrupting Diplomatic Victory**
            
            I've realized Austria is alarmingly close to a Diplomatic Victory, needing only 40 delegates, a goal they can achieve in four turns. This is critical. I'm now rapidly assessing direct military options against Austria and their cities to disrupt this imminent win.
            
            **Targeting Austrian Borders**
            
            I'm now examining Austria's border cities. Their proximity to ours, like Eisenstadt near Dur-Sharrukin and Nippur, is concerning. I'm focusing on enemy strength in zones near these Austrian cities to identify weaknesses.
            
            **Evaluating Delegate Sources**
            
            I'm analyzing Austria's delegate sources to understand their path to victory. I've confirmed capturing their cities won't directly reduce their delegates unless it's their capital or impacts allied city-states. My current focus is dissecting the delegate allocation from World Ideology and their sphere of influence.
            
            **Analyzing City-State Alliances**
            
            I've just identified that Austria is allied with four specific city-states: Tyre, Abernethy, Okilis, and Manila. This is significant because it means capturing them won't directly reduce their delegates. My focus has shifted to understanding the influence dynamics and their impact on Austria's delegate count, especially concerning their alliance with Geneva.
            
            **Analyzing Inca Acquisitions**
            
            I've discovered the Inca have acquired several previously defeated city-states. This complicates things; while I've been focused on Austria, the Inca's expansion now directly impacts our strategic position and needs immediate reassessment.
            
            **Liberating City-States**
            
            I'm now considering liberating city-states that Austria has acquired. While this won't directly reduce their delegates, it could sway them to our side and provide votes, a crucial consideration given the approaching World Congress and my focus on disrupting Austria's Diplomatic Victory.
            
            **Calculating Delegate Gains**
            
            I've been meticulously recalculating delegate counts and discovered Austria's substantial lead isn't solely from city-states, but also from their vassal, the Huns, and hosting the United Nations. I'm now analyzing how these factors directly translate to their 45 delegates.
            
            **Leveraging Diplomat Strengths**
            
            I've just discovered we now possess a Great Diplomat! I'm exploring how to best utilize their ability to conduct diplomatic missions in city-states, aiming to instantly secure crucial alliances and disrupt Austria's path to victory. I'm currently pinpointing which city-states are within reach of our diplomat.
            
            **Deploying Diplomat Strategically**
            
            I've pinpointed Okilis as a critical target for my Great Diplomat. Despite being at war with them due to our conflict with Austria, I'm assessing if there are any workarounds or if peace needs to be negotiated first to leverage the diplomat's mission.
            
            **Negotiating Peace with Austria**
            
            I've realized a critical path: making peace with Austria will simultaneously end our wars with their allied city-states. This opens the door to strategically deploying my Great Diplomat to Okilis, a key city-state, to secure much-needed alliances and bolster our delegate count.
            
            **Assessing Diplomatic Feasibility**
            
            I'm reassessing our peace options with Austria. While peace itself doesn't directly reduce their delegates, I've found that if the Inca can capture Attila's Court, it could dismantle Austria's vassal delegate advantage, which is crucial.
            
            **Capturing Hunnic Capital**
            
            I've identified a critical pathway to dismantle Austria's delegate advantage: capturing the Hunnic capital, Attila's Court. Its proximity to Inca cities presents a unique opportunity to achieve this, thereby undermining Austria's diplomatic dominance.
            
            **Assessing Geographic Discrepancies**
            
            I'm noticing a significant distance issue between our forces and Attila's Court, making a quick capture improbable. Furthermore, I've uncovered a geographical anomaly regarding Inca cities in the east, which requires a closer look to understand their strategic positioning and potential impact on our plans.
            
            **Analyzing Inca Invasion Vectors**
            
            I've discovered the Inca have cities deep within our territory near our heartland. This explains the ongoing conflict and the military presence. My immediate focus is understanding their northernmost cities and their proximity to Attila's Court to assess their capability of capturing it before the World Congress.
            
            **Analyzing Inca Borders**
            
            I'm reviewing the Inca's northernmost western cities, Batam and Buenos Aires, noting their considerable distance from Attila's Court. My analysis now indicates Austrian and Hunnic cities dominate the territory between them, blocking any direct path for the Inca to capture the Hunnic capital.
            
            **Confirming Diplomatic Victory Inevitability**
            
            My analysis confirms Austria will achieve a Diplomatic Victory in four turns. The Inca cannot possibly capture Attila's Court in time to disrupt Austria's delegate advantage, as their forces are engaged elsewhere and blocked by Austrian territory. I've exhausted all avenues to prevent this specific win condition.
            
            **Assessing Capture Feasibility**
            
            I'm now evaluating if capturing Okilis is even viable. Its strong defenses and our distance pose challenges. More importantly, I'm questioning if taking a single city-state would even be enough to prevent Austria's victory.
            
            **Analyzing City-State Diplomatic Impact**
            
            I've discovered that even capturing the only reachable Austrian-allied city-state, Okilis, might not be enough to prevent their victory, as it only reduces their delegates by a small margin. I'm now examining current World Congress proposals that could affect city-state alliances and delegate counts.
            
            **Assessing Okilis Capture**
            
            I'm assessing the feasibility of capturing Okilis, but its formidable defenses and our distance make it extremely challenging. Even if successful, it may not be enough to halt Austria's victory, as the delegate reduction would be minimal. My attention is now turning back to Austria's vassal, the Huns.
            
            **Focusing on Poland's Position**
            
            I've just identified Poland as the closest player to the Hunnic capital. This is a critical shift. My focus is now on assessing Poland's ability to capture Attila's Court, which would disrupt Austria's delegate advantage and prevent their Diplomatic Victory.
            
            **Deploying XCOM Squads**
            
            I've just realized we possess XCOM Squads with paratrooper capabilities. These units can reach Attila's Court from our westernmost cities like Brussels, potentially disrupting Austria's delegate advantage by capturing the Hunnic capital before the World Congress convenes.
            
            **Reaching Attila's Court**
            
            I've determined our XCOM Squads, even from western cities, are just outside the 40-tile paratrooper range of Attila's Court. I'm now investigating if moving them to Moroccan cities, with whom we have Open Borders, could provide the necessary proximity for a decisive capture.
            
            **Moving XCOM Squads Closer**
            
            I've confirmed our XCOM squads can reach Attila's Court from Morocco. Now I'm calculating if moving them to Moroccan cities, with whom we have open borders, will put them within the crucial 40-tile paratrooper range.
            
            **Executing XCOM Deployment**
            
            I've confirmed our XCOM Squads can paratroop from Arequipa to Fes in one turn, and then to Attila's Court the next. With their superior strength, capturing the Hunnic capital is now a distinct possibility, directly undermining Austria's delegate advantage.
            
            **Capturing Hunnic Capital**
            
            I've confirmed all five XCOM Squads can paratroop to Moroccan territory this turn, and then directly to Attila's Court next turn, as we are at war with the Huns. Capturing their capital will automatically break Austria's vassalage.
            
            **Capturing Critical Capitals**
            
            I've confirmed that capturing Attila's Court and Sodo with my XCOM squads will break Austria's vassal advantage. This dual capture is the most viable path to disrupt their delegate count and prevent their imminent Diplomatic Victory.
            
            **Adjusting Strategic Priorities**
            
            I've just realized that while my focus has been on disrupting Austria, Poland and Morocco's strong alliances with us, coupled with their delegates, present new strategic leverage. I'm now assessing how to best utilize these alliances, especially given the ongoing war with the Inca, to achieve our objectives.
            
            **Adjusting Unit Flavors**
            
            I'm reassessing our unit offensive flavor settings. With XCOMs positioned to strike Attila's Court, I'm calculating the optimal offense level to ensure the AI aggressively pursues the Hunnic capital without reigniting conflict with the Inca, given our improved relationships.
            
            **Optimizing Unit Behaviors**
            
            I'm fine-tuning our unit flavors to ensure aggressive pursuit of Attila's Court. I've prioritized high Offense, Mobilization, Production, and Air, while adjusting Defense. This should guarantee the AI's focus on capturing the Hunnic capital, especially with our XCOMs now positioned for the strike.
            
            **Leveraging Diplomat Opportunities**
            
            I'm now examining how my new Great Diplomat can influence city-states not allied with Austria, like Palatium. While allying with Palatium might shift delegates, I'm prioritizing actions that directly impact Austria's lead, especially given the ongoing war and the impending World Congress.
            
            **Securing Key Alliances**
            
            I've identified a crucial opportunity: making peace with Austria will simultaneously lift our war status with their allied city-states. This will allow my Great Diplomat to target Okilis, aiming to secure a vital alliance and gain delegates, directly impacting Austria's lead.
            
            **Prioritizing Capture Strategy**
            
            I've realized that the diplomat's long walk to Okilis makes it impossible to secure that alliance before the vote. Capturing Attila's Court in three turns with the XCOMs is the only viable path remaining to break Austria's delegate advantage.
            
            **Executing XCOM Deployment**
            
            My XCOM squads are now positioned in Moroccan territory. This strategic redeployment, enabled by open borders and one turn's travel, ensures they are within paratrooper range of Attila's Court. The next step is to execute the capture of the Hunnic capital.
            
            **Adjusting Aggression Parameters**
            
            I'm adjusting our AI persona to maximize aggression against our current enemies. Specifically, I'm increasing WarBias and decreasing DiplomaticBalance to ensure our forces prioritize total war and offensive action against Austria and the Huns, aiming for their capitals.
            
            **Executing XCOM Strike**
            
            My XCOM squads are poised for the decisive strike on Attila's Court. This offensive action, enabled by strategic redeployments and open borders, positions me to break Austria's delegate advantage by capturing the Hunnic capital. I'm now focused on executing this critical maneuver.
            
            **Leveraging Ally Relationships**
            
            I've been confirming our strong alliances with Poland and Morocco. Their current diplomatic standing and potential delegate contributions are crucial, especially as I consider our ongoing conflict with the Inca. The relationships are ideally set for this critical juncture.
            
            **Setting Offensive Flavors**
            
            I'm now fine-tuning our unit behaviors. With XCOMs in position, I'm setting Offense and Mobilization to 100 and Defense to 10. This ensures our AI aggressively pursues Attila's Court, prioritizing capture over defense.
            
            **Executing XCOM Strike**
            
            My XCOM squads are poised for the decisive strike on Attila's Court. This offensive action, enabled by strategic redeployments and open borders, positions me to break Austria's delegate advantage by capturing the Hunnic capital. I'm now focused on executing this critical maneuver.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: witogDcDMutHLYpx
          - toolName: set-persona
          - input:
            - WarBias: 10
            - Rationale: TURN 438: EMERGENCY WAR POSITIONING. Increasing WarBias to 10 and reducing DiplomaticBalance to 1. With Austria poised to win a Diplomatic Victory in 4 turns at the World Congress, we are launching an immediate, high-stakes military operation to capture Attila's Court and break Austria's vassalage. We need our tactical AI to be as aggressive as possible to execute this strike successfully, discarding any defensive or passive tendencies.
            - DiplomaticBalance: 1
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: aRLGKsxtrFqh8ZgU
          - toolName: set-flavors
          - input:
            - Flavors:
              - Offense: 100
              - Nuke: 100
              - UseNuke: 100
              - Defense: 10
              - Airlift: 100
              - Air: 100
              - Production: 100
              - Mobilization: 100
            - Rationale: TURN 438: OPERATION XCOM SURGICAL STRIKE. Maximizing Offense (100) and Airlift (100) while minimizing Defense (10). We are using our Open Borders with Morocco to paratroop all 5 of our XCOM Squads from our eastern cities to Moroccan territory (near Fes/Marrakech) this turn, and then paratrooping them directly onto Attila's Court (4,47) next turn to capture the capital and strip Austria of her vassal delegates. Max production and mobilization ensure full military output during this world-saving strike.
            - GrandStrategy: Conquest
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: witogDcDMutHLYpx
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1/Cvvv8F25i/eBSTFYiuzc2fUm5jOzu36LBD0WaLShB9yPSt9G1nsKwoe4HiEt+uBTASfFB+d81g/H/sDaRX+u9PvvyvOxrpLHLEa7OIAp68lcMnSmV/KHEtNmwYzSJlQpHExJqAjw23lW6vbC4QeAfLj9MkTlzhtLkyOog92139/lc273pTiBwSlZFVNok//fEsvX8ltArUouMvb4hC4dG6ZPdHWYdQPA5lUEdsxFS56w30QnIx+yTDkWl317suJRykAwz2yCy2ouQUV2uzWuapbXC/MdpMT3z4NfbR5rEn1PAFyq++FJfOmMARJefeymT8F9PNtbjQVXfFu0atReSH0fZTs+rRJTjjpcxFhzOlt/mENRcSm1gLMflieBOzPkuWbCPObG6Ir1ZlDyoG+80/bF11WdA3G5LQH3abtktScJM59EZj06+2EM63YhDrmyLTwKU60/vfwtNJVs2v9ncCKXwxYRmYSKBgqhuuX2Wvssu26/SsIlZFdQgqcdo9Cd6AtCbLOtk2tlj8CeN0IZBTCir4XFwAtoashEaRFBpwCEbiQkWOx4XhnSfg0Q6lTpu5lEdQnDd4t/uEcQgiJgbSg8ms2jXeFjR1vQ7HmRieyit5KyWYBJlIIX2Iax7xjIhro5TORNmFX0CzEme4IP7QcnrSYWuMD+efKIw0Eh+VZ0F2wgwSCeHPjxhw0mXRVHHK65f9vBUS0sDV9NJk38WzDfogUZdCqgK1mOxoyJym1RgSZyYsa9CD+6tX9NaK6JVcujLNwz7tDNqEM4+imY/JHzoCzpE5X6YkNMRC76OkvOjTSyvg88wLAFhY9px/olG8IhjCqJvF7BhL7fBVoO7LmBcbURAMhd4uwPfKPh+11jBhVQKGU1bRQjjo8wJSoFq6gRxZFa4ePvlkZ840ko7s2jZX4D76BvJgpSs8Ht4YGsUK1knBPSRXJldmasKA9vJRqjU8z8QKQCUEduRfkmbDOdfHZ+EKYH7JcmRriExVQBrt23m2fHKJs7YVNwd5gN9ZWd9IiaoyWFAGA3P3SGCa3JYr8vUxieu4brn1pxmYG0Sxn8giXcE2GbyhBHQMKPW+efOYzqz8u1FKI20XAm+fKfyUSDQM3iUFaEXQWIOMjoUiEyJG5HJMf8kU8YbuYTZqCFL+vT9v1Fd+ti4DJMlIxQak3+7o0uoKXgzj6ROM5o6lXaK1e0ixPekSSqBphGaRDu90slLRTMWK/Vc8xWMqUy+hM927flJE9v4zCs3fDzBN+058vBi6HcBgw6j7BtsXQagn83K8m3zP9V7WP/F22R4hK5TTDn4OMheexRqNkwLcT/jOJfR4maRABoirreaWvnyLFAd58xs3ponlrqVadfMQY9jkPdpUb/r3lOeB7AUWMp7qzvjoSA4ffLHv7R3kWioEMy0kqN/T5nGJASMAZ9KIPWTfuHugalGrWPtuWvPblsDG0u2pewsvSjvIsqUId0yac+nBJtPas+bTwpN9F0Pi6UZ+RAHeV53EqO5k3n5avZDMhvl+KgHLWoTMxjcvr4+aT+kB+hnSir+b/cykHn7iV1hVKABgR8U5E43436GBqzCpFd+fs4UAeLWJXIlcdqor03aCzM5CrJTt3kGsFr+Ve/bXYOKe0h3i0cgMQe+HspQjdPqaIRsnQ6kSLI6kVPEqi9Bp5DDl8WiTeeNSvOhX5uFqDN+d6mo06DgUSW6GSeJwn4LHDec5hVQp3X9cLykcdlmxeuMWUXtR6hQeku7XE6w0SR/91kvYWoQqvFZCxH/1+W+vB2pqG+oE+0+XkrCZ1v7TODDrQclVyhC7wzGpRDiJSN0S56IsFO6QgKUrBfZF4lVyE6Y/s0dYwk05Iw8HfCFm/bYW9SugZA66Zm2Lj+PlFM+UnHUuUuLalBfmmuopJ7Lotenzl2TiKHkLK6Y3bs+Drv4ji09VjsPebcjPNfz/iFf+XWEClBtHMyJauRmif9V2B92GWoRLQsnIgsF3aypOmT6riIhUkXjf2ltGbMhtLGmOWVvu9ZETTA2Pbv01QvojbVTNiq3RNYF11PXEBd3uTvSGCePfOPdU6i8GF9mPI07Uu0btIYIaMYb9g7EY2zb8Ri6WnllRrdneYSvamC2ZOmPcyAuuEGz9Q07w8RfPH1LbaGIucswL3CRxIUxH8283ANmPkjdznsznIp8s84vQmcrbCNhL19ZTY6LAoF9JfNj7bjfq1Pph7JtvR04j1G28BdjMgDYcZuWR3tDThjbEG+qAWbUbn86CfPyFAvAfhUoqwcqaq45lKSkfTZAmBppmoiyBYhz/pcCj9pyQ9hgDN6L6cZHiv8y6oXE/kXIiKf2U3t+wBnWlLQAy4yaZ3ftHbZhd583uafFKNstQB3PEe3l4FZzKW6BgWu83w7cUtWGVCo75e1FG0xOiv0lmwWnXwDishM2s4KN0k5CLUrfrtGONJ0GaW0q1njeiJq4BRosAEwWBkZcBpaKCFPmo34wAq9Yn1Smaqf/EZ0XA2sW7qK5vOihVlrBtUUD6iJ1PYVV84KbEZ26x1or5sSaTVi0z8ndeXFmjMK68cQB/GVLqixEy6mjW3aj02MZDCP+TGbBBod7pE/1xrpnFH39hf7tCEIdMWy5IrPg2u/ptEK18xCvIzV+dhdFxJa6A2ztH0vBBnDxa2I2wNQHqfCxCmnzmx75NF3IVSXwOvlvMQuiZ/OaRXpe2KM/3HsFMQsDh9ZHq7hqqw2vQs2kr2e6JlAqOjJHxlhcCcFb1Csp43EXszswRm45OHwYr0qFMSCBXbhjetQ1ON68H9+rUfvGlzp7QI23zROPe96WcNZ1MooM3EMgrISYBK1mPcTSwtA0Ow1uOxRU9lXht9KMBgYrZUPrQanIeleNpnhohYLyIqghz/nnR6BUFLUqhxTiT/WeJpQ4ZMJ2Z5yD0Aacv6YzEQhsC/rhlghwA9diWVzE+6Pfo8Lgx1yKM2wjQmGtpX84ukdUO1jjJKVIfBraK2BmKpqwLUfN+mP96g/HtqtCFBl+K3vexvaS/BXrYUNw16ywvDabxwjRG82/sbjiqZv9brsrD3bZAPh/nNYkzxx3RHLErBijxfjBnBEkFrnvKgC//WA5unsvFvE/MlUDH2zjmgNiXYPwu4IrwsvNMMmnY+JQwY3oDZjMFuV3lSjVGB6b1RQtPBq/g2PAgGEsAjfjJPO0wzVR9Ai8huRvbe3A9kAVvYYgvMwqOc7mJxd7ahT6tSsIbWge701xmzGuj4uyFzpJulKhSbhi3x154AJIS5y3bBIGyf/HD3456cmbdNvyyt6hDdkSpKKrkZaqH7mmtO0hfwL2eAIbXswZgqn52S/TZOTh7mM+YzekpSEGUWuYS3csjTLYmeEcPfbrFCRf2wlVn/iqMxSC4dnhtf8WYVqahXcnM+G0w5cTL+EkVozJweLJerz3XcLBawSvcvZZ+dBwTIxjafrbaYlN+hHup/pFe+B0omew2ldsuglMKieu3LegIabraGukQvBGQjcOBwO3rT+lTgXl+IfBC219OnCyfWgBFzSUTV18MTQA5kZA0M3PQbTld4JTH6eCguRjPUW1jbA3iCJ31ZbrbMoY60Y86RNc7DGhPwCiFNWcQ2v+9bNRQhb090MnzpDdqC2YZQz/rggG9NIrqk+eyd+kfNynuC8TBaEnKOPb8+EMS4QJQ5yO887byLG2B4NDH72q7WSY8Jyi0tDWejjspH48X5Q6aWL3TVmydgteLQMqjYmLfNBNoASroo12z8CM9R8AxaIlsfcXlqCCaSRzS5/JYQJVs2CBKNwR8tD6py/j/tpUMzjK9LPfxNMiHbFXdlm3zuzRr1RC0DyU4874b1i/+uaW5J6IsybV3Br0pZc4eo40OdY+D6nfll7jLNJROwxkteeZaixGNmvkIM07/mkOj3zD8sodhp/uG8WvDxibegCGwhbXiuy2f80ZKuOB7HgWBUwv/2MqXwJ5DIC6BjsLrP1H/UzL7ZgfmSxrHB0lyTNxHNJkwON8KL3DFiRCbZ0LntqgCMPoSsG0eB07w7KI539O8stYTDJm/mIr7E66hNwqcDYVC3uVnTC8Rs9XPieg/F/ytZR3BTPDZcErh/mPXQShOA+FXAHSSdNOVrZ4b0CdRCKgphtBUecwfrq3wziRvw2nKNN6MkJv2tm6EVSq0bYohFn4CWTNxe664y/TfyUi99Nird4wgYGndRc2YV11Ra2SfVZC2KvMF0DVhPLF+65XMYHEdhpQkKiuOR+MXtW4GfdrCkDj8T9hrbSqupAiEcZqiLzRKUw01gNkWJbpuB6xtCSr/FGmRqN5UOGs2PJysrye8FNmfrWWPInIVQVgJCkLBhRLZ6Cw9OyBwYiU+yvNfu8oeK4z9Lou0ORX5dHz8ws4pdSfbxxxy+yJ0BRQEw60ImloxU3fZmEwM6iCcXdg/LU9WXjYN2sLD8wcwxypYI7mdMkBrKHkn2zXQ8xfH0Lswd38AdR5wfJDQxmoSkjwPJhhmbyppYJDiCmLs9HMzlUfn8j9RJojD//Qyqn5jqtEHC8dzTNtBzOc45UletovIRFSzZ4Dz4Dq/w+VCAO/wBNYSO6UJ2WOgXLgxnIcOS8DnRfM771Ka8RJuk6vX0XKIMXpdG1J7xfUM2r4Xad5VMnFE2QI+NiTKD6Xzne8OPPm1jabenf6GlH1fUXHGA16BzZ3Y8MoXtHSUPaXwuTz07M3NRzvELWevu2DIbaOq0wlKVH5BVRdGgd1qKT8UZMMAdYnqyO/axPLFSb+THyNIK0FABc27LhEhqmCGG4ipzs3uL9GJbsqKxPY7ZgS1ySPceWBxlBYdU1D+iAzdJ+oT0ICaMzlanQuCEd+232M84Ui/0V5C1JJ0R4jLh+eZOsd7lA9WTIxAy5FaKt2Lear489nwfAXhoHV8vjWXVT/MGmn1JUtVjlf1AgaPDYLAWeYrw/H7r9bGT1h+KpCVTdJpFx51Ks0DJ9c8mTnlIPRUu7Zvj0ncY7vpZbsCuIVC+2An/IbE3qr54DvvszJjDHfurDLjz9+XC+F9oxQKTr0TJ70QRcRoRDMnj10vZ+z6HF3lxLbywhnPvRBbxYhGCT9uJD25mPR84wVdTMq4AYhm0qhnweoAHwmmbE5Puxa3Bl0gGfgyrfmBd43bjcoIeSCcKXCjxz4JHQSqlwogPyC1n5Lr81VvxAURWGfbBGnOdKah6yjKzRhSebHUTY2b88A6rHRI0WDshxkOkl8DIiDfQ6LbD11JAAuC9NBgZB6BtcvlsRyUeHrzhMk6qDiisuRTbQ12eMxEGoK+zbVGXzQ+YiOxo2MwDnrAQYllx5jCwvEtOnVDXXyCeLlvSkJztM7aO0CKoF0k53kLDyaAxzqADmmRHYNaz2GTe8Lf2PEUBSrLXuEr2gYe6zTm2/1AOEEMs5HVATELhHEVzdI0cnIm/Gjyc60N5AyPyi53zf4wIfvBSHk1zcgNSyWJsSzQyAvYj2w+cIi1/wmkH98DbU/lnikW+I8STijtHsD9qSW4tJHyTPv6lhAl1pGz4qIjWSaC84Gn0pMjubmXnyklYwxQ4JJi0h/12UDdF5apoXyCowvfNCAY7GBofoSkB7kXdOI0ju2gxoqonQDfj8FmpBG5bYaAY8Caw2ZS8VAxNx49vWOhVbwGFdt9yUiKXPT9iroW+w4TuzmO2S/CPGM+mLwqDHb0vOd1UwxAXhl1awCSq4SqAMajnRhaMGWh275Xq6AoyhPu6Dg0TBClRu2WCC/zp3v+q5GVsTf6W8/NxxbBxV8+Gb64uW90iV1ys7ClDaA4kBPSfOGUisbnaHU9uTPSLVBS4PrBv3CMvcCAzxLgS9xVD59jlRRsb2PP+QVktgLSsU4X3y5KwtxK60jNoYq+jTPLz5rAgBjm8PhjlMS41sp9Z4XBQHAjKxq7jBzizhnPeA3hW6BP1w+NEFcGi6hYArAx8alNTZKft06ctjugaDQLum+taFeWuzr9UOOJgBahzjaTeu41QolH95BcZutvq0kRfSxtGH4AriAd8YxM+a+3I5WWgftoeiEmf6rk2UWRaV/LQtGD9VGZU8LCWLu6hv3yJQ0vVAM9HuxBNikGezrt2lChXInIJ6d8isKtz3wbi+kKyIY/uoYUUzQ2SPuIsPa+aBmCiqgzyepYLDuDJWdm7DvImJwmBqfpRwGCh7bV1gNXZQaZyf+5tHXcDH43wcveeQ6+6J7H8HuWHHaullip8a3HeTMXzgwwkQKH+M4Rw2yIG67sirgLdeASf/x2gK1xRz35bQI/26vIBUcrRMD/4CQFGGdA8NqwPSNZEbKU37r0dwZToa1+tLnG0HzBHHWtZC2Qo14JsR/YeKOt3jVQBb00F+HY7INdnUEm4E0bBll2Rgs3No0ViRJzE8PpqF0x3O6luu+Z6tgSDb36qcuoj6LF4OtQVHyJmnIbaT8Cj9Nv/LirOaSWfnAELZ8B/IH1YIi+z+9YUC6d1rTltm4iTG2Zy8WlOpK2EOiY4/+lS68hyJ+JhoVZrCehQsXsX5SuA2cCIowHIGInWUkBdcOKDNnWAGRpRJ/eohtx0YqzoDsxBiMczg53rQNzxgnnLBBtyu7Wy5bb+IDAAlzNtz/r2R3GpVQgLaj1g2HGQLxXakdRypYe2HKMwDL6VwBilpNBtsDgU7sIGcJ+VH2MgS43vqnbfGZnVCNxz+vWK9G/mgpu/ybXll0RIrbrKZ9aE9F80ZOYhx6G5cFacfZ0ZbZo22TUIGZsa7yBgfHrdpnNiSMef8R3GSO3pXObm76Qx4/m9h6AY5Ihf895I2++iPQFn8y/APDcpwdpNHVs10ygod73yhsioi93DrIZnHyu40MRLbRbZ3TtN+XMQKtMeo5WBS91yhU20Gc0+LewgUZWPYMU4lCKr0URn1ZdSsi07su2pWvN1pQGOtpY6+4lWuSGPygo5t63pMdKSV88oauPdemitMiN89vWWCVNHXARCR3rcDNJGIwvQefcH8tYYsLaUbHvAeOSWGtDrjF3fbP1Ht0WePrAmWQXdm6qaRT/csTc7Eq/wNMKarkSHB7Y+xBB0Rk1RP901biZNvMZ4UVxRYUAFshXukL3AR1P0uDQZCPw5yhgL+n9SPOVclkmTV7NKnkdXN+QKz6ZFsXUGAmBqZBGdfhDiA7rPvsbxYdST8d8HtYXH+CNHkYl4TbsdFyhzDcwy/QUTK+i+4xmY/rnV1OotWDmeIl95Bj3ZP44f0b6j8+Gz+XqGEVrDnfaDJy2UETjq0XVN+PyjcrPX0zLlkebiDZ6I7z2YS5PVCckgRv8uWTdHEd3y8FeEx/xcm8HcvWI9kaW8TPvXGeIPiPLAbmQt9DTuH/lnBbGZZOEtkXTgMIPkVcX0I4M6Ns+USLyrBC6SVNt1+jgSPiaztdlGr9riChEaHuux4bZYksR8Hk8lr1TZqddH0ccsCKvYqpZgv66QNHRquWDJCoyEbECG6vD/8ncmgyIl9muF1Qfrp/MrZ1csYlUwhxAJ4SItGpdMu94960aYTJ5h9TAJVpHCkZfb94SLJhopXrDFG+l+n0ItFwWyVu+HJ1Qvry6C719is8HOBjBbJwrkUrgmn3Hb9Dfz/WGMg5ZvBscKcNUYlvl4EE7WCUor0PVUIx2ia1a7yWQe9xOapwdjl4xRRE9UkNL/0aPXHya9xf2pagDgUr+O4zmLkqPbhkKscbw7jzTjErjbsWCX7spTispXUjGD8iy3YMUp1W7qktjKYFuMdFN6BWxuyjdpeEn3Om2o6cIADocUCjLpF7aGubPq4MDxlZL4zNG608j2yFxQ6tEHm3c11rR375qaN20nR35sy8Yr2fJ7naID4AFSaVtNyqL8r+Hrt4hFqI3c0CHwkz0O3S46nUH5LDrUJvBZIYIZ7XK+lQpgh0aQr1VQnJAFUQ/mrxBvW8ihicA1H1xNZZ4nDH41/tr+0xH7ZQ8C/GENFpvbRjxxAxbaYmj4nvHFqetZE+GfPUiF2uXsm+D+so/Xa4rm83db8rELhupFT0y8lVfCq0KxNCG/x0Jf1iBGs1fmzD0QnNSZF35xY67T+x3cIu6O7hFCsBsREjpVtWwp8vihttCRXqpJ+xg8BLep1UzlqB+QRl4nopz0zgwDl9sNRj9tHY+HQsM1YNc+e2Q7WvgacEKlSV2JXGjIcFw0HfrjLOIyYXLmlvU0wcBlSsporqR7V+NbTiOTRdFhs0w1fHM2ahm968RDoM8cCC4Zes74M4uY2AbOif+8T7aoTmG0CMOmxtB3eTHUhNZKMKTlSrc/wANbQZUazowj7nKgjllAMpk69IWRwR6e5abpyx7d/WB0TlM6BWiiIBKLEsuhYPA2S1a8V5Q9R82NTV/KDFbLBpvwk8nP+2r8lqSse37PMZnVOlHu8ytOjbevzEXpmXsEM/yb4XsE0Rl1Drbv9nxv6WKU+Hh4raxAf28fyVj66hAtQpgGZMFc380CxqiPuAnyJdDzQYBoK2gAOtkvwl+uvjioQFPVsQs6GEa4WryrFOib4O5ItMtxiAv5fBibJ9YtTJoHtjaOzVGMrsuDc64mMfFPDuSeEZS0/Udrm2Y1Kdt/TILTRdEJCtFs7sr/OzkbzTkw2eBR4YXRPMV/HddFtAdDD5vAWsVhb1J0lNYH3LIEL8a42lant9hJIyfpPmzZ7EFqJ9ARaIsgowuFNwWTrdFhS7s6Q4eEDtnlfWWrTD05K/55Fejl1atHuYg60B7EVc2nr+kghHwSeqxZetlUo9CwEQkhNv7wTcepGyQW8sXpTkDT69bfPfG02viecqbpRwRTYZYDMNRxnzfuOug9zTr2eE1sCTXmyrhZkcvqIvpxjlw0Ke+9+Rl4oi9BVYZ0shsoTpYSUqvmYUDibIb5fTOyskxVMMkPjmq2hg9K61Y64z7GjtBOiJIM1VPuBTqMIS4e/BvVT2WYjXNDck+QrNOik0Ak9Zy5TXqZIqIhohkfTi63PwGLNhaIZmef9YR9cxb8TJD0wW4ho/lwvtjOwYF7ZQV8Yq9gTsgbERQmx6vWJa0HDddXbUGyXYDeOa8UL1yJBlSvYtb1mUbbUy9yRoPx4oXY48ogxmRE9+wbA9QarHh1LNaLC/o/QwSue4rAnCmsABxIHuXBYitu0aVC/f46vyAalh8L+1qK+3EwesjU7g3G5rEXem8Y0zd/5DD84WQnk2zOoRh9rOlXoK3is3rtMobgpw/we3P612anagqQsh6q9I/QbQJVq+G2Fat1Ax4Tf+q9pl4V49IvRW4UB3ye7YeuE0gWzjJOBsNWd9Wk3GkaH1w3Z+AJ6RS5b7/OtKeyRoamYSGVN6i7vpwXvW5OPQEUio3ys/5b9UGDbQb0dk2aGhdlF7LJXiT5q3TZ9biOX/Qqu6hzW0SUxiSfJICTncDRqMt7kBl461NBkZIO9ZMvAWxvNtFqUdWY9jgvGAOp54ZdXM+vkSdRfWsIBvsfHSeNNwFAKpNtVHawoptHco8CZ8YTMAv2K9AVwacJz8vja54B0wZFHca3h/yp6M+GZQQheNnG2+w38Pin/yet/+JV7esLihRtffNS53MrR12/eazPq7OJ9TPE/cXupcHtvbyGEGzIVAeLu3AFWVhVHWrgPYlAb2Gb3Yw5/LhjajT6v1tUR6MwGhAXcrEz08kCee8+kiLXbGFrwTxp13oNgp2W0IVWpExf7oyIZkfo2WQfx2YJY8aczaXNrmO2+C/n/E38yK25mVuSZ+DWmGMWZicjluhHafGuGhw38ydGWx5SSh5OJ/FmPIiNyMn0CTum/pSJ06fVtb8KChMyD5PyPjDxNPWcmhb+FTIwB96KfJEP07k59zc9ok6ZpwdFKpWzfVn/tmqC7IhCPPvgi+Lvso7E1vSGDROv/1Zh4hcXSHTBIXIaOKNIThuCBH4SfBvh1JvURfQw3hwpYCknFwYP5XuAH85nnm6NZFU428Sy0INSq6no0778fL+1Y8D7FbPzA2zx04uilcWvE3AaauqXpYaLCwJlujcetVL8uzUd3IzloLeik38zP3Q6Qum87Wik4ezP8JaCsJJpmdqpK+ZWxwb0i+Fk84NLNILVxhdBvjViIoD3Qhzgk1efNNQFxajzSooV7ppYq/8cVMyBzE4olSSNXCT1dtJ9L7pltzbD5YL+KSbBu6y9LjStYxVeMp3q59WO8CM25HF/K//GOtC6t438xWxdvGCQa+Ezw1IMCl2Kz1WSgPvJXGGUlyjDw4KYgk3abmri5wCid6+0atMo/cxGsu/119fHddoOZ4NfIoJkRYA8awzZGddpmeVJ0eAcL0vb2R+1jcx5blz24GXj5pr7EFNwN68Feb4JVaAYbINM1gAWKXIFFOm3pbMhH6n3DKvfZ8QfFfzgV+OUkpVPzDZelhYKiy/p2EdoQji5q811kHWVVSIW66VGVgyxugRcTsVzKi882msB/b1ng4DAOcs/shnwqikH3i98wSHfkml8uD44QO9KzvyGBUSe+AW0ENeuuQbviPVg3iC/PONikMeCILSefIZ32y7luoh0Pjvvd9hHJvVC4Y4ke+W1DhbjnBe0kfmbdJVEShWyAzVVMBAnSW5PZ/Z3eRamns9j0a6K2yl37rcJwDIZumEZMtocD3g5Lzh9jMgtHkmGD42ltnQpjDbQP+tb21ys8PLDmIgmVfB4ZfKe0SkuFa3ixrhtBOdn59f/O70juFDd9hBrfhvhKbyutgx/z1lJVIOY0GGRKEHKxBRYvG9k7JwJuG4Vs5zrYGYXwMtgAeOuxXRUprVzpxx7tGFrZIwSRsmtPlmt8B7N7wKowkox7Ohd/xdfGublCOeZD8EJvwlk/As5ooP3xfwfCQZyd5DyI0qE441BGvHhPFzzFJTTtiHxQepdp615BDEHJEHycY5Gf4wb6DqXHXZBn2L7d7BU84IHLc/OkXyZFzDDUnC+0bMO/DG98gGOSVVkPI0LsyJcojPNNfHn1aUYmuP7qWaXBMB1INRZAHM+84uSBAxjOmoIjobfSBYG2ZCVYQ8EWuxf6SvyPsNKI830eHRqDfooDY8EAJcWWtOhGSiMnX92U28F96/5MIj7F6N4VatD9qp+85/cgl9VuZD7pekL/V6Qxm3MR3Ah7fbbBpu4t9ZSzwXGOWlJj5buXb88SqBcHDJlRsCaRPpjSaQhOge6GpivUDR1he5xfyHJcsvFSaxP4E4ADq76zK3hqK1Yeyc5mZyCbUx43R+JcJUjjDgocSgpNhzhgM1PoqsRuPpVYAxhc0j4G2isKgESZOESMuO0Om9hQpxgU3BXgicyz9We1bUGFDNc1YTi7F/JgvaoPhFiy5KVw9M7Kaf+vU13HsifBlXrdN2+zFuUBkPjEaXuh6ll6OBpoytA0bPCif3eQXm4M9NYSWxWMdeUhgoA4nnG7qdHHXUMnJWZi8UzwChzPXjbJclH9tKC4USbU7CYQWzGFhccn3AXupueY1c9S7NsWzhRlXYuskqwzBB4MM66aizleIgVf199EjzFb7U7gbH4sR+/D0NtFSNyoKBjqIyqwgqCfq25LA77ViuwCk5mCtdHJO0jLgc1paERW5VaLux2zGqZLGYrJElfjLyBtuQPfeMwRMcE5k8/YL88/hvMzlKQk7S2PEZ1ktPiDxk2BdCsHLltb35ZlBb32KRjA4elcqzyxaj5vQihvJtmCYb3OQgg2uzgg0Oe69MI6qG0iSM/TPfoGGNxoHGcM+iU0Tj+N1jZa/FRPH0xYqLnyke7jkFxWVud0gNumaVmlzYHFVPS8d65jGoMV2oIoBwc+lLVTN7E9AavqcoanZwiXS6nex64v0OrwYWkWtyhREtUKlQIw8ZB5IpitLsuMTAOnm+Avxz8x7nUFRiQJQ5OYxtOdHN+8DCWDopMO/GQF4yGh5WQr6Gz8hY3geV/IZiGGCrYO1MFpwfFu9cX0t7dYEWnSvtewradJhHW1YjlcqMIpAf7bbExpmrEeONDhU39ZwoxAiBJNqgu9AH62bSziyukBgmBgUaZO+8kzvr02lMOM79ulQmrlYqqsQG0LI12r8OGOrIbg8JV4a6Pg4ykqncbJCyhWCyzmQDKKJyZr++Mvo4Yz010gV+vpQ2QpDmYPbP6ju++EPPJsH4kgdY+Su/a3FOgeFMTOJInejXYR8pmWmvd4zxOC/1iUgOz8mo9B7c2dWSMUsJYf3OFAiH1CE3etS5nfPkcTR54CubIUPHuzsHlJBtFNWcqBazQhbcB9DCihdHAw3U5zeeenrTWcXTUwmzA2LXn/WtHSnNGyjIh0z7tWjt90DJ/8LL0Z7kIyKJcuw3b1nm7793jqChqPyR0MwEdGCxfMW5O1eWOHdNjSfXTBg9y/YS7ZDLlI2QGFx0FZkB4Y+1PqyTf0irM/mWVot5duKdU2/+fRhmVeR7gfVg0irrFWELXdsv/BQ75yavZqMIsl2XGICzDGYT+fSv5ayNYkyFnTyLA5CfgNn7crRp3Z36fiuvuaeW/VOmcFXdRlw0DiM5KXgm9qvw3T+AoKBQcwSbVaZLukTsOwpa2SoCk6orHUEOAhfLLCUpURsSjHQKfU6vCAYHnhrWsbWytbF5DXWezmIPMNqkWhtzLMTL/BtPjU7KH4meOKUSKcSvK6/JeKppt6NeAHT8KNASEZoMTzmlZft70V4ls383CW7bmJMu7A0wvPmqEGa3yYJ8zsD/7p2yTHEjhrvnwjldZsViMcScObma3eHdPiMjP1GZNMfaV337RgMRRGrEw753aJzu+mWHb1RB7dRhp6vylfFlIdf/CMn6UHYeoD/2T8C0IQEZwOdeaTXPk47ozoqKb+6ZIXhheS3OR/tS+1+3IEc0KmsA836Wmu6pVT9WEBXuWhKPqyECShZhNLSi681smxVi0HTAiTlWKGVEGb1+YZkJyLIe1HGnoBcrMXo1vdOGbNgvqz+hJhx80+xCVUdRuMofRoI8sCZ5gLGpzowMaot5QkCV3/KfGNhY7vuuRn4i7g8kO3aDdSaGSa+hSG7l3+hfVDFndgyY7MMC/uDhMSR86CYpxElHaE29RM+EXqe1Dny2FGHiqyCekzq+i8HTf8n6wRzBI4tMCrQfBUzqdGhZhnEWXA+Ee2c726SAi4MiDdLjnlzP4OovvNd7mejGWue5wJiAO2VqWYIRlCCskNhqVjowTQes3l8x3sXShbIsqfTRUTh0JjeRK3l6Qra6cHrXJ/jMt19by0msjgMxwSleIeAEzDwTWHkBvqn6m5aR0yHFBcx4m45GE5qnRXux0n8xabUQlD3sqP33h7EAenG5SwW7469i+2fivjvvrOd19OCE7dntOxqkwDosHpkuo/PJeUR9hOADrroOEMy6WveFGPjrsWPuEgLhfiR3rbLTeWhXr6TwbdcirmyY3NYa/hz/cZLZ1lQFYHLsHIzibynjds0sbA7UX8bN7RiYGDdh2eh8MKfFUejAvZsPCFTbm0O1NUtlt55f5zKxeG6Z3PJl0DjdeK3qNruWthg92ARwWPbNg/EZtHvraclxCItfbIpojuWvBwMNN4eXdaoOV0/8RfjMsG4sowwXW0XSc4Pl30qAcNU/mp8kgkQzVUSDyXSAyFdAkjlbw2yyBA4g6/qRDKFBh5EUechx/uwjt2KXKeSjRARmDa2+7H1P/veSttN2XCa3Psl8ZD6vVIMNAPrVraV3dJNDzJwmZEJUp5i9DzgpEbB0gjmk2ROL7rIjMm7lySrwLE2c3dh6vhAfKOfXsAfqM4yguTYH6nxmsR1PRVyRRfyemQ0k1SLI9wOpq7hjWY7RHuqOAnR8NBg6P6i3t3DPx+3XiNgFbLyZOrVwK8P6wR9EQpZydameF5w5NsEDsHfrQTMGMCAqVHlLoXWnEhe2ZBpjVPPyFq85Hbasnuae1DL80pB3QsDgotAdaBQfShzJqFQGLskRZerA2FT2xs6R4l/aqkYqMhiE+gjVsJ2DS7yw3MSf6I6VKKV2Py+HjByc+Z0cvK6Tpf0Q6KrrAgfk2R42vh4w5jaxDKiCAInmayk0MHJ6YLdQfcMcUG9ud1ZCF5aoBjpeJw9Sx4lWmYp0iME8mJRGT/OApSbfTmhGQJlG5VwPuNg/z/NmZ/3sbM0BNmhsdWcihvJo8RtzcR4kr5aXrKleZl11qQ2TPqqLfcgDkxK9kKpvJyxxqDy8g0piP4UM1PwTHDlvAxqNdeY6wNYxHBPQX93kOyOniCQAU44bdcrSRh/osnIqPvCdB/hd/dMZfGKD7uG1xOrw0kMZXd22d4cMtB4x3ZdaOlPVp+fXYTfiuUybB3s4Ho97DYsfAyy6c8Hc3OSscEffFnOtvMmmhTNzpjt6szidm2s6OZ1WMsnAcT+UsWGOxKdb08sZjaa6DMKryVAkBBOUc0BUBmgFtxtGw0amZSwae7VIPa1ET5b5A7gAeEGKfM3oCaAFWbtSjaifQrpDFM+hKKRvgLJJQRQuh+8TURA4PMK9yeXQclobcbv5LBnE7012DalIEtyymEVxz8Yp17ZQij4spGSFiQeoF9phLwKzt3N+UlO0Ezx1WCjg3KnHg2JSwx8IHfs6MUeKHH5xC5LUbAkX23bHZkN8jWt9YuidDTnP5ux3N8kq1ZuzB41CfUhlFuoVw/FjTN/Pr0ylfsZvzAqU3EIjwdT8nvpvIA4NrIe6V+QKhqg3SeWljEKI/dHic9rRoObsHVhm4JvRaqdeBVzWKVPeH0hWkEeO58VlFEwYA1mOV7t4jQgEUUiVfDWsS/hewmyPbmUiSHHjZI3p+6+45jONQ5s+BcIggZstNjfo12TLs0kuqbJ5LjQdVGNoJTCW44P5GBVZcMRW+i3A8OYf0kkeK8vaW5J8JyEd8VZgrRthIm517pEZ+aWTeJCt7UZqcKv4SeKO5Ko+kSFxBtB6UCe4dO8N9+W33mlcTQ7lFAXLl3XdpSd+JPm5gOBLuKgUfuZQ61NzZIQhLffZJbYM/rS+hrL1QBX9E7TItxiVSx4PLJuOWiTeA+uBKJ/LxLT6atjTJ/s8G1SqiaUQtgnIjag31+FNTnBUKT0/6ieigB85GiSexN7luaae2qFx6AFLMfMXjQFKPI6ZZH9RtHSeIg0b9Tv25pduJeG2yOqpghBRGUJTguIEPxNNE8qq+Dc0zMnAOyOTWOO2Iz/7pvemuGQckae21/pd4sUlYX2ag5lPpNJzRMN2qJK7VodIr8qXz9luTw5dkt+yighMCoi1beS55rSD+r/b9w2YaFxerc59+uzE7Jo0woHeckh5rJlitbAzosl+CqoXEo8DPkWOKTGqRPgsq33b/ggJzyJIHnmpUmrT08r2YTNx5zYCar9ERrxNUBRVztSkPm+X8HtdhfpQCpeMmI/jdSAaz06f6jGV6yCRSvz91L8waPYjh3/Gpfy7hmH3gjJFZGV6u/vUUnHV47g7uJQW01Fe5hkfBWMAEUEjbhV7/IXw2VB7uRtjnmqMTPlROO5tqsbs8YQSApmCelkeWGP8vICdasj64BUj7lcociRpz8IhksfBYF1XgbzDGgI6KsJ8ync+3vQ9ZSDLRzQ4qb7PqlKMi7VSQFeMPjR0MIWpRow+y9zDjhtZXpEmp6OMMsjeedLPJAngP3SqFI3hfzBNgNvWDXI53r7jXkvbNDKBIkwjlFLAgnmfLwbxE6QCk9qHmiMUdhl+SJQsdUh2kfLVdzwXNpAtpl0O8EsPnFkEApUcd7zcTjqXrTRO9+WB+9DLr1ApjfJEpXKHNA3i4T9jdoWG+/+MWRhD0HwFl95mxK+Aui32/hGfLZ3rg10ZzmQExoDspuaMQGcuB2pnWBJ9IkZ01B+JQ3NqNISUSGlLorrcr6zcevJW+7U5pC9DT5M0m/wo+umPes2QqtWpUF8qk4zhkmeGhZIXnmnPKLC3Bdki/1qTckp3OAEDlEHj8h9e/gwBTYCw7v0bDDj09MKSlmx2N7IlZtTZsbvgzM9TVaZiayZssxzIOJVHouIyhysZDFgxaQ0dnmTSS1kPp7DJK1ugYnkA7Oo+Tsau/O6mnMRdb5edJWWJPXAe8ghF+rmKrIURhtaAHQdqsDEeSGQgzTIpS0nJKqrI89hV6vThDf0OTeTw1ND0vDeGvN9W0AqzC7xMj/6rlYYBKbTQ00LgWybL0khvhnQPUzUM4epxUVt6Lv1QCtzyd5/lTu7hJtkLNNgt+TEro8vvuwJtfNBlyby6bTXYlMdcePXKPgRr+VwIgHBNibi3o7uVswAgTzQQCFQFyhxILIS2zFAwcH/LDtvKRsrSC2BtI7NDSgfnAbjMRXrj8DNxQSRLsfT+eBTWAaJovqSWhLYqEtOouyXO85A20gqcRwXVt1KGdyysfxZCiU6ODelt1htKoL9tHrcUpo2hkR2jtmUaS/4Xo3eMIumI/ngVHNepdhUbjn7gx864KkjUJzf+o7QMH4exlEZ6Mwoo7lrGsIfcq3V1rV1fiPVOaLwmo9hy2mG36hEB5pAdtiZ78oBv1rOnT3OO4+lowm8CSYJK07aYIWmLNtZh3uyjQz2NtqtcCQ/F+XO11yMZctxGZT0Vp8o/RN1j552YqId4DvVq179/d66JZMhTuPS9Sh4I6KLfmk1AZ3Ym2LaMZ8Vh6Xllr5XgOahu0hxqXHvw3/LopklSriaZFCIvPz/qVnuqYc8ULWVfbxF9UsrVlVP4ACHfij9WjiMdQvl63NtMjKlQWjmVw6ivGJ4Ylchd4IoYZxmr9lzsa7SJVgaoiRV+1KiKagam81ZknHNGWtuglBM9E+kX/BPedhZZxeSEweX5h1ZS4W3tAWaF14vQ6zr/M65GeyquYZxqyTYRAgukSm4ptAPL/8x0wiOXvD2kCUJxwrcXXUy/aZPETSLdpq/KwqcjUvOpzSBVT1oxkmP6bM2kUQlKB6IPXZR7g5NJ28YNsf1vUhswsr9Uz4hthi1MyIRgJiA+U5a7A43VttfmYn6bDVL14oM8+ALx0oCKxhB9XVYsoLIADQ4xADGaLWEa/yzHFJr5XPjYm4ri0mgJ6eg7jwtlT030UL7eSrQ3qlwoY9sD/IFa9Eckm7feyF9P8mY7m8Jgkg4oFtvkeA5FPGcBH2ZZ7YhK8j3HCA6iHoYGRNWQV/jZzxPyL0a1ZjgomO4SxGdMrqj8FBA4iX4IzYC2BZVV1D74l3AQfHVIhyeQFw8ShmQHX9XHW9Ag+5k3S52MayHph8BQu14fszy59Wrc7ku6/2AgqKph9poDXaLBiSxn3wlT+9js+c7A//ivcOanv9YQOzA0/dN2HTlIaJ2d9guil35d0iOQ7EQmB+2g+80LyhD9WBYxyFdjd8gr4ZB9JJznjUIPOpat55QpsD1p/wXbRYO/wahiZc/QBeORmacDcDvhTnQazOlsO6s9mqTMukWiNTXYrXypwYGLEBsIopYqqR6pEGxNcTurEZQMVejrAxwDAm38/oJWXw7iXBSgM3K6QCR95XQzeW2JM3ArtUwHWRS6Kdj7IZ0JZcdaG9t3VFW8fxdSzivcrjlP9jLPVdjqN2d8feMD1yvgxVKCpVks9vZAZoS5BFIrAJDeFvv8uFR7ydUENTrTiKspTYyMciaVU5NElELdEC7Yimv5Y3QMr86WQ9iY0gAeB9B6KCVmT3MC+VPTigaQ71zfFnEcTRGArr/DzH76kJ+TN5W42wRSr16UesyGco3jja3WrJHrUYQTHwMm4iAfxgpPRHk0XUm6OTknW6R2VtC0skyIhu37V2LN0Yejncp3gfDbFcQZ2KYOkDV9bdGEXIZNpKCHIIrhBivxwFUm3c9dB+4pUa9k6j8U7Qw/JxpFICyf2anf16iFWu5OuPjjk8OBve16f/YTQMQgphqi1eyTrXBZ/BWr+NZ74vxAK7nJvgUNxjXWqjUeTI9px1FxszYLyRp9l3o0yslkcDGXu1bGXEHXcc7bexXVgMlky9Z1hZa83xNsFDjK3VRe9xwBgj1eSaQxBRBogvMpt4ElJFwY6Y5wGO3eZ+5dxgoQr3t4XMmrTxyI9yxEIw1N/BvGyFBLxke7UMGOMfxoROptwvmnRHl2MhpL8LzgPE/rvi73Mcth/ZLf1eYDWz6wd3dP+AqIDnC93KBanGh2/G0dlcz204dMxfNOfJPvK9Auf7AjLd/iF8Dpkc2KeRKn4vmosEvh/0ZoCn5LYp3ofFomPM7ukGiuDq867Vv42rBPt5HhoaPx5k6h8H3oNjpfmrejYlmWKUb7qHNf7fHGMy1yrHn6BkV5oyFiPm8HaYPdLx2rCsm8CpQPTZOxe8smeFQ7JDng38QbxPx01Ym4Wp/zLfFB/Jz7Kg8kjugU8ypqtdJyH046pa35tMDnm3hQsMtCWNqg71f3+QwI7pMJArmdAxq71ury19tXjZpKxSPYMksYMSXwezTq7RpOBD5yvYD3tOGd4MbhdmjshsC99aDzF9fIvGokylO/gSAf/aHNgQysGy6wv5h95b1XxIxV34diyaBCBiFa11JfqOxfk3TZRGNjCsSgBEavfuqLGkg9jTvAaz8P766nbAymiy8ShpkqnjJQLog3h7CWxtcPZyV6K1PmKOhYpWB6R/XC+U9kmXUkfSJmvOVzwcvQfIdexFWAAVk1mZ3r/4CK1vaVS8hkvRpS78LOqj/Bs12V1YGL0KY6vd1HPKVndyOErYPiisTgCeSkvBjVNfTKbCe1ggWNKigp/FZvrbRp4r2QauQI8hJP27Zpq9r6UitXGuzv2qYuQ+Qo3tYAxvCqtLVydEo1AFnZqxgy/wGH5aoHBatN3sSMatu0bIS7mKB4SU4/5Oycn989aKvsWHsPUVPlUFl3AAp6nq2S1kHZ0l2Z1nxjiTGsuW7srCDWalHcXUqB0HDrsEoIm6ylwOrtCjsm05eG/iI+cbphRLeglisAQkplc7vn/l+mHK/C+zCPgImBhG44pPnsqyZc5P50QQ1hbT7r0LwRVZsZ0rORgOqsS7Xb6WIbFmYpM1kuzpkrEOCtMIB0b+m0vFpIkmAtFO3WvCRKqI5Fp2p/HGNzX99h9rSWDvp5gqL3PjFuEysqsQbLxC3jnoV4lB5ve4hl02GsDUcURnd5atfPFbEKWPl0+3VL3IHIZ6eI90ivdNiWZmEWQMH58mGKmlWQ2NSzVfg9DsTGQoTy8UaPN2tk32YBbwTT7nvFUQnjtfDQ9dK2yTXlWbVKz5hZIsmJORL3ptsG+weqXz7cXca4br6Gji6uMl0s5Tu6T0PIP4X78/yIm592kTkQo5BHnqoSWviGRa04n58UpQHTGPD5JL/d54gcJ6sf++9xw+i0ZLl69RnircOUhMnMXmvC9O9FxTFxEY61CF7VIv8WTAL1xivDcFLElVqzM6nAxamYkWN3TrsspMS+Hw2S2/R7jKzA5ZISXfSENkepFv9R1T4u68BgX/5ITFHTP5BKGETRLI4KXYxbb1d5O6BahkR2Deeg4ql2OmsPB9Yd8l2EsPiZAOTQJ6BjDsSFkSIqG4Z+rSCu38oLVoilTYZKC808XsUMiitIzsen/R9ghnBkwCPlUKGL3LM6dnvJEE59Cw7Eowv7xxzlypgD1HAMEnH06GrPWdW8SwX0LOQdC7zIPJnnXz3G1u9cjP+I7bsrxmOH6nksWW+L8fMZlO7o8ai+hT4naESBVH4Gel8IeCPjHb5tNZ3pnriRyKoukwuBWDGxd4iLRJUuDwebtKMc2UhDG5SgJoOMK/WwP42Hjs33r6ddLvqu96QzH9J4GLoMPRIoKeB/3e858pTdUa5r9SiSg/2Y0AzPknIO8v3hlRssZlUIn3vqnwkMAkMhTGh+jrkAyET0Hp+Lruk9aUbH3KVmbANeeNsZi5B9En6UvT5k9Su2iWhYDqWsQSDIdU7Lvg9++Id8mDgpjkvuT7NnRkUYGWoDljNU4jXRPBC+lpbRmtuUVdbgSEv+63rc3wd0pKWGvry2zccpRcmH03OrMe3H8BMt7zdH/vbTxVWXD8ux8s96t4w+SB4zrgPi5TfT3kCTIS2yjsRufef1OQYCMeHhC254rtJGixDp09cLVh4mba35Ht3/j1Gfv+z5p6/Ag9uwk645ge+JlP6CyKouPNKZBhcfn90Ds3qC7dSEb8nW42QQaN61M9Qlz77VGMV394b9eOwidRIj0X2oyV4i/+Xtin/pf/tTokL1MvvqETnL10oaNkcxPlbq0aEAWKSmnB48N0dX7jx5rHhvc9k8sBherPGamXfHlq0/gbjrHc+ezJ0TXgFGIFjagSqzhTmS324bpGiPjINWLDp4lv/9cBPNBiyesXpV83fN4K5wnZP5b22+KZGVMdSKWlV9SjC0NjLGv94M5vC7BrToEsd8ForY2yNMpDxQPs0zAlxUG/ZebNzkyrbNg2Hu3m0YXZREgCs9ZpQt4/tB1RTrJSXIPwFmuEFohdJE1LcxnCPFfZDQUgVc8ub7mDcfZaY4b2tyqXjAKhsFdGTqq69ht8GTAzjJza/GOPOF44nXADJkgxF20TW7qzBGJLXSmh9y+3MDGCGfGyng6UDOI0boFSwP8yGKQPaZIpohroJ9YuOzyaSnv4MAbBsTojnrZQvYQ0D0LxgMxMveQXrPn3aOssZT+pQ5MA/1pThm8yqRh3y2BEckAvL6JbdeyrRzn0EqAYuqFpTgGXIfs6kSdbjArP+Ph1WafCtYL860m8/IxWwwoJrmup8hw768INmABg1HARyIDtMO7L8WW8pWu2wICVegSYAfRlTrq2RmUE6kCo6ua31GMVrRIYxK8jcwgtq2wPUnUK29rPRl8E1wt6DwN4DaCdtytrm+nOOXjswD9bPDAFIedROOjZnXLnsvVcrOAGbLff1iH9q8P1oqg6HN/htwH6Ls393QjyYhj/s1DIgiU/FYfb+AVfV1hhfuEeSe03FQxhqweHXyOwkrrplORuvsTunWK847Mw1G7lBvSi1zfhOmTQYNsNNUe5RPgy5luE3+pdsyL5kcC1MHRXbGfYDb+D4Mes8gsToe5Bdl5gBchtUmF8QwUrM0CbGuI31GlIkttMGtBzxBSL6tCN9WvYny8Cszxuwn/DjM9A/K8G4VLFH1C4iUeLaz7hHV3bricorDQ+neLrI8INQrrGLQj0DgSml29BW289u9qDY8M9qPWYf8CK0mxn8VCm0tpysuSVlV8HneQ49yodhoOjJ4OfsHEbPmLDrBpr1VZLHYsrdd/Zj6IILHsGnlcgo8lh0l6KPB5d9v8+ZwTRNLx8mVXHACX4pXTShke6FVEyL97s3bbjyOaPX/Z7Sv0TLBgFJ08OGsbPV32zCeVibac6u13wOEobinWTP/w6o4nMoP+Hj8ESEuugqtsAsgeJzWBw0yaTfZ/CAuQTGO/uyR7GAj9bs4oX8tAdJHgucnUxo4o2/yBYJKjBO/p48FfPwokzcGlHE6qrFW4/9ze67gbt0uPBGLvgAF2HyyPO0V+SKMkQpCmfK/KeIqXuUERpVutm8/RjLPNuLJBwzQg6i9tniarTj68K+7aV6t4O3JE0He9EVZTjHZRs8R4BEzJWpISIbf9iNmKDgVzIw5B0LZRfufiWysZZSjLee1uNUt9wins4aovHMdZHqm+2+tHJ2hGX8cT11JtNhkiiZc41uyp0hUZVnesYEYH1t83P7F6fKeE0K9J6xtvf8V/apLA2g4CwxhUUzbfAdyuqG6xqiOaSpYDHxoqQBr2ftNJVj5BTJR1i57bW8n7nu6zeYUaoj5w8iSeq6gIlFbTtpm5DzlfXo/NMQ+PW2dFpKTU+YJGuPtlJWNg1DO54YnPJ9ckI9zpkkAsf7yRSnP3jDph91R68l7LWJxJ0pigFizY9hDfoD2ZTeiOJUfc5zp+wzG9pIgbiGiph3aFzyeMOp/NaaON1kxR6HIPx8Xb3kdSEfnB+pxN7vxjMGD+re4NoypSVRPcpGFgVBaOst/5zu1Ulycp4nNaEzlOkj5SOFkSnu45iJheDRu/6k8U0Uzv+eyvWuqp6rYkd0YJjB5vkiByb7hRk/skgCB8vfQCRTI2mTr8+PSvy2CSO50AEg47NOnfXZ56iHawrJllAu/XNJHV2Psnqyo8/sWn+Y2BrXXXCQ079F2WqxLIDdyoK8mBKp8r1UnU+jEGglDq6yWwt5D5QU2fekfyLEhCR0e/2NQ4jKj0xP9axt1DkG8MRSKaIi90QN2H5lygselsEJ2qddFNBlfXLVv/rlqEtmLZCZhz8pAHUpwb1nWKaPatfvFStGqOFPz/2fXq9AwYsrJxAkeAkaOCzh4sUV5KzvXzNtdusLpo2jp1iN4CGwLy8S9Sc6iYR8QIQEFMIDvH3ljjnG9vDdmS4v8bcXwa4WV1iSmgZ9SHVtpvGba3SNDUJnB8aya//WUmZAD4U/aLVw+ZHK/DFMQAyHp5xM/8igdeWmiggcBhVNTGfr/U+hEoVCxDSbaZu+YgsJDF21iW7uNypeKWfYP05iXqtVxKRMLf3Prxkjz5EwXIBYpxMj7VspNq74Dw5j7l+pI1XFeEW+UJjoh8j6KccA9EX++egqmIURLPBYjboNuKqDrsIbmKBFQUeh2eMcvxZvePseMcV516YI11FcWWB1k2E681mv/fstLZGA2EDLR79NUGzOcHgsLa6/C3L4hZDcbvPqpg8jGtlQ7GMbrwzGvAEVQf+FUqYALUYm33qR7m7qvdS65hIEMUtIs0c0fVdvlelfaqpdeQCKXcz+JQ9/PeAMTVekHWItvvVqWiDLRe8ZoScs/AmO6qed2Hh0XQQNTJtnyhPgOMb0nRA9IVB3vG2NmGjW21FiMJYFSGeJA/EoCQLYBN3bOUyceFOAy5/CjSqlMvFfiR9iX3bhHE+ZHepEPLGOteAbcxG2y4oD9qfYFFv42XhtQs0bsBN7iEfDtyYMOdxzsgI4QETGmnR2MK9umahosD3YiCjAgLX0OALtufrVVT7tr4ssG//jLd9qi0dvFqYlDe1z2iTVh1KeL1WLzN4wz3IxrT1pobAd3r2M52zwKSZ4HDjpK7cDbRknC92vo86gmZCkhD1oMYC5/z+VSIaSVuci0LInQiCTzaP+M1J5P8oXX1hdNqBIoemfVeMZNBtibkGcR23q+n6jwb9y53AeTDgSoThkIMv8T6QxpBDWVatx+mApenmFk6SxSn1wx5JghUlrELsMUdhiC3j/gwssSFOaDgXj2e1y55KY9i50fsmVAgdT97ln95sRBNHrxSgQh+Sr8vluKELtchEAhxT9PLTTmy63IiV1jRziOE9wVPy7vb+nK7V/MQ3tohUn6OGSN9TV2t30XAwDP+iUitBfttCSr0BQ/a3BVEs0KNid0+s25WkQyFDvIgOdmHn3Cu6ncy1eS/WGD9lldBzgG/hc9JqJyHQZ8wRdgtLo6PtYt9V89LFQwVg0n1ci4DKJNNYRInlg0b5JUmeltcQAWMHy3sA91EKYANwS74/D6jNNRreaCkzh8eooXS25cxUAA1hO1vj2bNQhISKfJqLWwN9EsUmpb7iSMXNoxECBvFgRijVAP53gcPnJNB/4uys3eW5iQ0jU69U3naHPpo5DUyR6wBWQB683MwHIUlfIdqVnr68gr+rHIZBZTY53UUD01XNrHNmJ+H4MS1fBlfi7wluX0ryGZ54a2joGdDny66+Cexfa1JCcb/p/DgKrf9o8wINsew4QdyJrvguF+Zors1lScTaomwDuaddz2zIQ/azSJMbcht49GwG02IKdKBl4yMN1XYhMkPM308KzqDH+BdKZMkuIyW6U1CEg4trnYIoKj0HnrtOkBE+35Vh9poRtAdl6TXhVLkMcBFBbPP2uE5S/sNspfwjV8GjPBJImIZwc00O4FVt8T8q7cjX+fMAFO4vxW75qYKKfLSt0QoLKgwoD4GeFxFvQWcCF+3zeMNKW+eMQgRsW4F5nyV8j9+lE5gO0Um8RIJJcJdR+mSfio4s31mnQ5P/xymcJdOkR1HBaFQoxPsaOZneugmkVwQeuxrbG22J/TSUCXAxh6vwhx6u50jVf0rJdKITWm93eyb7sajhBga6DyDYfrbL4RK/v+smFjzOjgjQSiTZdVPt29vLxl1+EQelFFlhcXMqFrLx5/O/3rr/ZKYEnXo2jSgTs7KKwqsa6TCFU9Bj7cPeRR+VQXh5DINlDP7dKHwQS59Umr8atU4w+WOArWzbnzyLK2iupAmq0vrwidf0+rorWLRleDPJKi/WMdqKy4wuxEqVupWdHM02cxro1XVdzB1Tgmql/bCL1F2iqi7cE6K2e3R8i5f9kQiBMzI0gy/Ag3gTA+0y3B6PdfTahqKE8gNaO9rs4RagtExP7VRiDOC0AN6EjPNJGL2HlTVlUFOn7U7yb7EGQEpSX5Ngv+FvQneSCl+ZCfN4800oanNdCKpM35khujqsf+Vof/eboe+fJIGvcNPRzrfXFC2yPLAnMPhjoRqdMhyLYJn79poMD3Y6bIqUitzCXTjpW8M2PBOhBqj7IdwI/3m4LOHs4tKLR0ONk8T/q4NEKK0XyxKgOdxZUcUF+1Y92M8DVnQEHsZJUAzWJU6dRkfNgW4S0MykjflhVjVHt+vfDUAOGVbXhMIjZFu3qr4TOsBHDcxMrIcWiqlsioc3JPKLehmPFdxMP+txySVy+MWuTbVPjfHbZOYS1bgXWKLiVC8iQl23xGgn4l3hGFA3IxGjC7FcUYqU/XOsY2F0fhUm1O92csxw1JK/cYCVQmk+PYDJOCW7EeLHtlnAmpERgOBoqJoDywC2bN0Hy+880mM4PXX3ctK6cq8lggmBug0GIB1NC6HEJj3G8oSGyDaxNMa/ztWoHUHMY0s4p2HgmR2Bap99hyHTPyWDK2tfsDPOJ9r62Y3AT8O63n/tKAKskQmVyrg8KoX6Zo6+/wYb2GBNDBaxSadQoJtsdxWrvxpR5Fow4gGVb1ZapvHJaiGGLqIYlPs7pT+Rs2DJIgwv6zH7os3rENV2IRa5YgjLs8sP3oDP0AH7SUCbcHG++QUKLxyMHEOcQJfxLmt987QwJLuI8Prqq5pk2VZRR21PtQytyGSd3B0muN2LPc4f8ruRC2qR75OLdaV5WjKb3ETa7lGtYXCydrShsH/GOsGbfPgHgEFb0Sj/My58UYog7BXsDu1b9gjk5w6jYOdV0ThaJRwRXrt6XxW+O8OtKMbPWE+3KK8Vh5d779aVh47Jn9KileM7TihZ7A1RzT/tXCtD5zcNf2lONIuIGfIJ1clSQnlx73mtoy5Nnm+7kBccKb2BnnlLI/am6Y7bpChTMEnqdUZ1AytYwN0HZLtJwOBdZoqMfIs8yEPRQc4hcvB2WIhWM042gjBk5pA1ECTrQKDdsOrC7X5Sdrq2KQ64RIpIByIYrHTUwtfY01Box6mMU/WMTM0KFu8107mnLys/aFbhWB6Ux/qgXYMVVmZLg9vmUTNcNGryJ+fzuvaJrG+EqIv2NAqNdpXZBrsguCmG8zMYSPQ8RyX7xeL2S1GZzA8H6ugSlCCIb+y6KfEbM22I9YXhCdoN4IGQzgnGp+kvglNwfuyCPgW2oBd06ZxqmF8z8RknGfrJ+bMuEMiJ7bW3UVU/aGEALm511/f3NFs/LFDvKkhWlGwROxcFSQB4tF5lQCcaFew5nLanAYtAMGwEe23TUVBtbqy5JvvSCjlk1sG3VZcz28rZOucz8kCeIDetvTl5tlU0xgV122eyv6hZyphXCncox2t6dAPssZb6bLDPHj8cVVCZMmPFkpd1nIwgdNXJPGJesSCCXg9hEIAbJkvp8TblRi9w2T9XBYFBqu+vhnI3qthkP/9S5HKrZq2KQ01SVxIqchNH+A68zlG92Ycuczo7YciW84oHsagKGn/AFMIHGw6dL0Eo6Kkgc21EZLHLylDTzQwnqaZsaaeeteG1MswLnxVdLOKp07xDJIGRf9jmaYd/LHhpfyb7vdZHodN/fuxn90q8hGU0gIToOt5qf/rmk7PYjvyVfOAmqkeu1eAsubhi/dqs7BoZ8hQEeopyHCPbr65Ss46JVgpXeDlvo9Q0epgwcIiFaUj3oV0dUy57PSgjABS4OGHqRmdrYn3uINFKsM22OFb06QcVTrfxApg4eFywQ0iHO/9CEz1i1GO831VohvK5EJfbPUMOrLVs5NbHKFQeKR/lJ00XCJkQhvHGKNsF0tUAMQIvRM7nVI/agJSRNLIhpaGKefxrYbqXvhI4laeqpnSY+NKCRDNBrX60DzLygyHPaDdwEwb0dYs0LOr29OY8PJiSP9gLL9uaxCPHQAYaEfzXhh059645ErjLhApMmb8NkB/0oHYaoqNI8fjYCsaiHRXGCUhNPcsUdN/BZQSGheB3LhRmjZBOgnKcpHdR4EmA2bEXWmaAoQxKO36pXIChePvGVOK2khzOOn6nqVfEfdXMNfM5RQX36S5uEz5wcWCXEsavVmjkjSoBRziBgX9d78RdUNMxakMYMU3quBe3roRoMPTqhQn+SWUz+dv5jfUxrqg3XTdSx2GlZhEhe6bZyFitSouN3YcYq/YLZz4KhrFAzVJy71Bbmaqher1mSyBy1Dlzgo6SFduVLTage/RvmbBsWdy45LCxlTtG9182hatKBve5dL/Z441l3sDouwav2kcjQlY1unSVJ0LMle3p9mf+sBgokk22NpPICEjA1fWlWm+u46wCkhZ4jTBcX8Nu857MQDMi5xikAVPii7f0BdlaHALPienUG6qByji3Z1eh0EHQjxggegD8qb8eUVtY1snoYuCoK5+gzDLxU4HsjnIocE38YPqwB5jJYqW/stliUYd+x9hOLK6XuXM+2UMPP0g5VTqZ0jITyL5kZKJMo/we84AiNTAXP1FXmW9NagHTJg7CV4hR0FaGYhrv1sv8CDdQZZ7rosKEeFTGEtXvMnUP0nIF4l7XHqW8qV2AN51AvQG+vpWvR443AbZg3I4IXYVqOPd8EKM6OVZvfhmESj6Ne8a0fx1LjHOMYOV5DknznWdpUrqKOuFRwwomGylTqTM5QxA8LHmfESTOPQuKrohl4s66QQIacTKBUYtJQn+ZvpFwLVFuqjrdU1AuqcJxVKA8OxGl2ZrQWfRpG8szOovZm9/UL9F/ofn5p0AGSbntRnqEITZE3zqnDZVBYXcEvPrdcLixL0kV5y/Fp7OxC42AtoOaoajopXsEVjvloZqUOYEhEPg11yRSrCECO0/+8Sn05NUz2ONwJIihaJEol4imfwOKY2g5X+QBaj3cTq907UeWkmyfa29b+xxC4jrCkOXQqyQi4e9LTHP7BR6VYYsjGKz9Ub18JqKigKPGCVWAp29LepZh0L6veylQXIcSV6w8++/89ZExMxNcqT3Td5ZZrc8hj3Ke9JYU0qFGueLrNU2A/P69Kkmdeh2kDuJ7Z8PfxrvVCHGBFsmXuJMsIiv4fIOTZKRERKW2Blp7uwuJrV/pGBwJWv2x78KH9suy4+ND2PNai7mEQRVpUGI4f+V1GInGa+gNVxOipz9dh1VMv20otCbMH9mvxpzCaYlOotu0+VQ45naPitwqhh6/TItvvAikO72lgXQJ6lDePVanDdPTIW7H40TggmaOOWGO/OevfO+JILDSWb0NcB/nfmMju9vcO3WvyEEAVkrwpo2BybhBh+SdxBfrUhCn7QApqWg/qkvSxbTsOgeLM5vP4Q7Z2B/QqrlF/DKoWZyoGQZzAos5+2psX2APac6BLdTBRIDhOi//jo80WqfhY/kDHTOR7+YQAuyhCIwuKsQSOea7WemzznFXFGGCaXrX5nvyH7tnUPk6gMLjL//NWT1WIxVlVCcFJObPTrTU6rpYZ6H9MT12E8fxkIJa8lYGFaYcEuCt9e/BFyA2C8n7dfFkQTonqdrrxveqhVvI8Ny1zlUWVy3WxdBTBE2DsyoMRcI5wFgzRhfyeLNqT0rY+zKjZDILgj0Ct3+K8jfdnjD7tMz14u17zmLJhvs0zZqCdZXICi7jG1pFOAH4Eu6wxDb6g6IJlcc0cSQloADqRGoEPyR7f2X1Q3mn3kczGR7TstqDWEvPyOpmM9vB0T8GbzY5deSLYDdYJWYHz23QIl87IOJsO2uv4lXtuaaTyvzLvjOgMqZKiGqsEu7fG6RyPIJnj6LbhxzHNLiOZ1VZE1M8ol56pS1i21feR+WAnXMvSJ8aUuds+Aqslq7LntZhwe24nnuKb4+p8OEgDgKXMxP3v9bb2APecoqvAk6s5Z4xWW6WB5xhkoycv/mg7dJszEcLzkgvrnSgJrxS8NZRW+badtshUmvwIQA56nV82rXRI5ncgtpnn8BOF/UHDO2QatZiKUY8fKe41r7wy/E+4apj7U5M77OX4cm2rVFfniIo2+D7ZOVBJZhPhREuCM1dgG85JWkTbzTwv4MJrzOMhsREm7bkosG8jSlpFxy84ys4C6aPdoV8nHR+61BqU7ubw2gvEQxvpQ+qJ/2VNaY1hf3xCfk+tPTKON1fh4p2M7Peg3I14ajw7Ad2yYMnYJBn2kOo8gWH+I/qjHxGUzCgeMcMtPTMVl4h52xfF+3UbfPLukUYILim91xb4EQm8Yittzn0ViQir5me8ismpSodQvYivABsPREyXDuvK/okFr1jvaysUB2Ajk4d0bH+9Js9XtTi5XLhwIJlt7lUJK/D+AkD+sVvtjC151t6JJPoEou95FeFX4BKagdGErszgQ3ik76tEgksjVHiay/ytX6c9yuHSA54QetVWCcPwt4GtQcO2H+oRRn26q748V5SOEM7gme19iaCMUTWnKxunu0ZzDy9TpG5tR4kU4GnUpBSjxVOsk4T7XIuS7ZtCJgrfWdmSQ5X930V+Qlu7CPf19oxxx5VJS8f0puzPBbcAdssTCpRtGHNgTWSHYmh7s3Dhdin7Crdc+3iWjzb/0xXfMCYg1922vb2NtJNXAT4sjbmdv/69DdkoTzmYEuYboy6Tqz0cBAu0PfQzEw3TLLx+MiFPZhYtFRWeMX9Tq0ItMWrCCF8hW68xsx5jcRf3EBYtWt8uzjdWO5gDQCSFyyd5ztIQoQTLNVCJsWdh1GWMrYM3uyhbIRNE7biWt6mKZjI+K3S/0h7NkfiJpes9Vs/hYy6TfTHDQxggHZrdC+ygx1FHQFRc+vhzGP/FYT5Oflmj0ykacLqsUvLxi/Ivq92Ke6JIJk5xx4NdbT/KLw0YkZDgsojXqyjm10F5SOF7/g9FmE8epjm35s6sOZXOKW4LAq/rGbU9Ryo1Kijp5bKB2PWFMkNcbwp0QI0zxclKtO23jkVzSk2GD4q1tTN8pTvWhM6OV/Bw//yP0BYKWSzWCL1eVDMrzbhCP5hWh6VzX/zE3FBS6+S0W1QqzMIq0sYSOmhMO+Y29NUFPJ7+juZtH5XGhZXB0zlZAgzpMe+LBiL4eXaegbTmq/u9951gHdJqrmBDbCDwQHMm2DEuBmLHbqhKSu17hVqSfyzfJozzu3gDnrGWKVaNw5K1EtyD+lID2nONM7I1F1OI7bp9dQYB/vsDySrLuuBtTiKlGpMmwkXJ3xgw5bt8h2fE6gHdDyzzxvfOaSj2lG9TySQ8xCrn6HbphFYChWFaaz/NwwKB7NFEvRtrlMw+6bKwjRt/sAqUMZwQnJW9/xFYSTqerNquRB3jQXmX4bMaRTf0TmuyEDI++UwcNAOt/sF4evDy8Kx8z+gWJTsugCwHE2ysvYKN837x0E8RCFPnUKLqgRKwSs6m7TriT4Eqvc1k55t68EDUj5eFsMLQlevcE6c7gkFQZLUehhXZSoHZhli4MmyMVKMD5MBI51DCRCIteosYlswnmGJgxQ+i7QJjS1ZtKzGRZaY2FVguIQfEGPJsbUzxB/xTWhpN4WBBn0MSQYJG1x+94siQejzO3f9Gt+mioMyyt1fjxV+NFtzESHYdTro2QbnvqXhg7prMHoE6/LihQpwOYRFX4f17Wn83rYyIPHRyUHy36nHavhBxwytJHV1PJFOwrpnlSUsFxnGW8p6VfEzArV6NbCIA3repghL+VIzDSfXucY+VU4HpmccyXlY+HBggFtUskLLJUknbHjZuzgi8lWiubu3tlFlAIhWWl34HMCdbEJ24ZehQNxcd2Hym+e68IjbgvwfNcmG6HzHtXVNGfMSkFTRv/xVgNKqgey+xSAdadJFooRtEZBa1qNs6+fTHprWt6oMxrYVurKAPpBrvIopSlY1TWRtr3kB7W0AynMDMv+untAqAsVq8lYuym2fQnWDrOfmS5sO1zM3F2XgEkuQ4XAuICvjJO9y6AgunRZZ4PkFnR9LBKcRMI9up0ToBIA79uP7u3YLXoZ3AJzAdrMkSv/aH9kWJBjPLHk1/w/LsCp1Y8aXgp0AuXzeqSclkPFOG5IXOLB773KnL9a6A78TqrLmeV12USYTnGYFBXQDAnMlU+slDkttKThIkoh7SjLMl1MT1BOATMA6ENeBxPd077Q8QA3UVipy2UsoGn+WF6lZMv8BvqeCtbzs4zNE9XivPV8hvD9VG6d1sor1a72hj5T7PuyhCL1BXoH1HPZ0o6tgbW/rivEUtC+iVcbSXn6ccMKwrwDpScTxjvFwLhXAEPhEpC5CbIwAhOkXGjJincQvLZwVHCzZefpth+bCGjWJKwLvo/Qq/Qyz32NbrSrYvQIvTdzlIKxX+yjPWEj2WdHUu13cg49EYFs/VQrov4P5F9gboKXM7mAIpJVTYgC7yUt9spfVucHC73K07y/pmzhX5qBfopb4ATUR3RSTADO+ZoH34QZBll897iaCEeTUkmOFW2wx/eAH9TV2L5dVMlvmpImyjpanyd8JCtgLkP08UXq0FcjdoIArHA1x16n0gQSRHbIs2AQ6U8faRvOXAkhJOHO7jXlK/B/qGPdffqoHkF3UTahGKE2t13uoJgjA1bDYzbKk0bQKYjcyRER2HvDSxJo+EaXO3x0vRJYszGQUyUwB2ubKgeOFKOc8ZW7GObPRwmpdnM3izoPSwvRnPoEYjoCtlcOGn4PehpEtZZP1W8+0WD+eQ94Rn4zQ0kgmDuUE+l65sYOOkSils+prYbxLLa5EMzVQBjGWqbEMCRTeVl7RLllccuAFSQgXl11J+fXViK/HxT3NhTVjKKLUBjbbfCU/q5UzU2fL3Ta6ogFbnKauJ8pgwt+HKp2p++GTaj+ObmWFyanwyTqdMbtQgdlAwypPPemxbhvvhk9/6RZc7+i4uaqiQ4nEowQvuX/of1Rb1MrzsMd3IC4Lqu7MV9Ks3JJbLi56LK5vn+4ynnYj0KatkT98k5vKxtZ/DSsJ2hSAQJBDzrEwQmyQQTAvxY2oplYeXyVg13+wMCgbS3nqhSA/P17YeiPU75ml+FDkF23FYiV6JuDloOXdvcirR1pTfTmHu06XHNcvE3BcI3xQdpDkIjugs6rUCMKj0TSctIs4kg/1YxCpKz4sSRLf8TJ6EYEPP+O+OvD8F3p8htBLQ1FpVchJAhhJ04nl99LfvAb7SPnxy2Wv7ghbAWezXnkavNEqfTRF+Ps0BEj88ZsbCzxNH4r/OUnLSSHCN0UpaJK6Uzfn0d+vwRJqdcR0cO1uOwb7RH6miUaKjB0zbYiaSNY/ZHOKR9FPjSWHvDVEAfD+UD0xOAg4eNb0OFi87rTa5i+ex++fmsDlg6DslyrZXzcnKA11yNS24yPg2ul4rWSxJLgEVITzJ7dgLsbJrX1eI/DnkyyRs56kVgJ88oVdBRNm0gUE9n9vHqs7UaoKMDjKT7z2Ztz7o9cQ4ZVmWTJTTr7NqZylDqbxmg59YQ7wvgSFfnaeDgTfk6xJp84HUSDA3RLoa+/BeTOpqLO+b1PmkGIeU5+rq5C6V2ylRtC+T3cctd2KG4FziFvfl/NYVJYadBZV6Mny0B7Hz7OVpSjKO74zGSiob/s4YOekHD063+UpHti/yRzjRyTEM21vBMVIB7oXTM/VgftHj/ZbQKLUlF//r2TowWYiEmbZ5VPWlC+ZsQzimI/yyx3f50LholK2SLl8fjvp9ltx68rif/+CtAGyssRzNut5v3pnbEfS2ItXANlm4R/O4ISsEi81vWlRhprujP+cQ/W4ZfZbL7hGlXvb+CwvJXAyjq96nQqXTyskKBptrIcq87JPkpS4jsNQBYgtoRGyBWNMXPZNjZEX7zWdMh4LIMkuYuvWXCTRSqTh/zuUms+rKY4BK/6YlDl3xjjzdSHHk+nV1Sarpa2BS6oHeYUNZ+30UkW+WwZVv4uDpUxCGVdRzbe3fPjwSy/O2Dt/LvLTxZ/ojShJ3wBBIv1m2eRNc+p4NGN7bPCpXo1si/CE6mjan38O/if5o7cQImmfT6oHT7oXjYrT5UhH+9b8IlbMoNck15OeeVlevX7wY5K+ehLXgs4suL7ylchtVronn6uqoFQX3EW3zPJLI+IrPNhtXmSK1ZFqf7dtMzDfRWWuy9dIriNr0Mqr+OHz4rq7+oW2UK+Jx6/nCngaNNDCWFf4UK7C0Lx4zsdpqBeC3U1X9h4Oiv/NFvi99bARECuzvFKr09fQ0PU1N+slFfXG+WwzZvwV8cCeUFwLqzEehPEPSNFArfdkV7uKbXvRHz3SNoU70BJdHSD29NMU6QfrGWYSsUTBZjb8KsjguNnn9ildEXyIAsaVknWKKRTugHCWFV927WgMoIkO8gdvR129qhEUiQWT1eSph2Uc3w16LyVHMZU8jVDQwIXW+Nu+YTxecmPI+eLCdcsC4bLChlowlN/IJkDmZxBFBOk1mjWaAH/T7viH8O/LhXQ1fMKr2IFvZcQR9mP5Pfszr4ZMnbglhjq2nDljbBF2+oxXxl3QrXELD5236QCEcJY6yIuQ44vl5PqvgdrhcyCtMl0PuPVBtci3J/MgmiLBzvmjt58RjtunWeRBSqhBbQl/e3JypIw+C4m8sleG8/y3yy5hIdoZG84pBny48taHtiCiCX/SwfMdK88Oq6fhxy7+2BMUOL0bHe/At9lINnGji96NNGj2+XqbAf+cgQMVyrPvDAu9EHN+FmsAUM+ktOMBhrBDqea5TsdNSPCZ/NUyjtbQYOctaEwlE3pj7QAfFIefEYaSkN7Zdu26xK0uCf+MuJ/BvPveQYWpDRE8PSpOvM4qdlUXC8W13IxzHb4a360pJ1+P8o1o24FUjvXnHD/1BWjWU0fgKTRNVUtX2DTlQijyhn/6/V7gjHFL2K5L+ue9lLQTePtjoUPXQyXBftPwo1L3ZBYA8p5OpdBMxbrFY3O3Xvf+PKJTb7keAnoanOs2zC6xTH/e7d/0EzzH6vBr63IwQMwtsj34cy9QDrKDTQf9VJIq/WOY1G3RJrdRmGSrdsLduHuTcWZUo59qw4df612Vrq5+JTJntYFH0MSIvcJHWwE/VibAkyBAUv3e/ZM796pmIB0o80onhRfK1mYnTenh3FgzM3ZYZN/2EZt/TVK6CATYsWFPPch0irfU/yN8Wuz99X37l4ptzhK8V/yjcb7fPzCvFc/rBDPLwXbw+uWBnTSTXarJCB6rHWOUpLitbd856u7ZBAMbLDAK72gDtNXQGT+w8uFvVdrMQ0O6HXyBP5E1Fuq0OroSuyJ+u8bTGMe5vCP2vCKVOlCbhMSIWbuYErBv67HBP/gNXNLxZ0IVRgETwMA7UjTcZm31q5JJ8E2hGTz97b9etiCGij8dQWquNbVM1g37711Ho6Pfo6eyB9quVuKTvWYmIqytdnwnaQjNvKTBDWTMkNZoIOA+OijUzaJxTB8nVGFzSWtnJ3i4w3boZwAj2MQL+UP9E8vmnTwgixVD1gza0ArGlYqns80LnASLUBpabcGNInVXSN4T4WmVrOmGy7SKA+ZHndXs/G/b/k/diGC4RZBKJ+PBMMZqepzWadmVkzY9p8+SFSBaXDMlnl3nJJA2FTUX3CkQ6FrPole3KRTAoFr6X2hxP7VV69SAjDcMY5O+z3ptv6Zduyijh2uGaaIsNSFNSbdszpHRFJOSZAJSXzWcnZKfB5dk6NdJ6Jzn9we9qdka3ohXXoLrPAWkLn+/+6dJpD3qYbZbaFzjoe/m6BQk1+E6HOfd1/Qq12efe2ngy4Zroji2gzGWkNEJK7aW/OBXaj278Fhg/kKvhC64fPHHK8817NdqNyMXtfixnm9rROQL5SzuGwbjBYJRYup+foI1FNvQUK4/s9LmALBHX6SGRetmURyJbF5hphFlLjEshmcXFC+Wx6TE9bwk1UveUsaja+Yn4p9k8QPZ6uhN/czzo1LRaYCULWHAJQNmkgwXZHiJlOBmkXXDFToTGR0qmLljjpIsm/y/4QS9VUEifOP+G2mfx0Wtwg94n3nXj9i03atcW0YgZ6c4O8g1jrjml1IolfwDwEK7IkfuSSmcr0+1RVoH0G2wKeqklS4fks+b7ei5q0SHH1+cTHwzOb4oB5YIjXPj+WdvOKkdm9TFnEyLE0u7kwV1hC4nVYcYtzY9TP7Y5RXLbi6K7sF0jGUGTWCM4XSQ73zJwFOW4/K+X5ZncZrI/F9G2tpiSDPQv+1lITJhG5naNmDSTei4TLIygggSRfUFLdeycyZJnz380WXIksn5HjvlYBNR3ciLnAh1XBIqKpHRGA2S2TJdFky5D9bsSaHCarZYd/huznkUebMlHz5PkY+TilI7wZ1mOPN5RfyEfI8feDD3G2ou5U5ZhnNPBUSQxNxaPkQjsey36XNzBvq9je2YN/w/nyIPJlzcClMGJjON7Oke4WXgF588kG0K1r2QHMF/8QDu9QLwsbBbC5y7GqxkynnDZHGAdZx081nbV3X5oMclsRFbpepMBLKoImblOU7nV5mhenALXRPHp9iQtBDq4ZXmNozHqcqKFxQB9Zrk5zotJ5iTwI41kqB5PIc+HHxYYimGvdBtndFwaA/68IzvPMktMJIPjBYonmCPeIn4mGhoISZIv1ROIqXbfLplrLbPqc/0EBQanDsHvbNh0eyVKvK8OY1J1gXKbNROe3tc+Nh/CiqK+qwupwaE3+QiA8IkPp5pQZYZnhnu45l7zaXQRkz3vlWRYUF65HC/DsMf+MXB4VwrrgQv9LQ2PEYWjpoHITNK/Hsz++wQ+/SeHdNiUTBYrhaOGcnKmynyuHNpJb3L2zJ3ZdCgM/hOS7c7fa07MTLfTmXyiCPfXffMv3iMXWIcMnMWy6IbaCUDQflRWmnws2C5siAMmWtd88N0J9q7Mgndfc/grmpKCHfmOUXcW3Qn3QtMmXsrHPZcSM60wbkDii0bJA/ejWzhGsJHkjFh0BL0V4zG2OmriVtUKIz8YE7kGx7EuSxybi4l9AMEx5M6E4RZrC0L5T29mRQmaDQP2SVEwaj+6ZuPhRiT3RlDegzcYFbWAu+DEvdadBGCjgrElCKkswo4CgRD0HGM1N87zqoKLkLWyUXqjvhEEI60xbt3CZgS7s2Zo6Ueezna8b1UpyUNG0mQNy6R5p/uYo3eLiTc6CwhM0qI3LzQ9quJ2e/pWb7hDzA6u8rQlwdKcN4OGI9tDOiYoUnYXxtyvR0K7/J8lI96CBYfSIf9UBfjxM+3o9VuJTs14TifDC4fL/XmeXaaYfqQpWdrSPqLDZ64iUlm69GUKACFu/2YQZ4qPXvzWdywLkijzpQNLw8rtsIvP6//PkpLoZnIlJm2nNy74LR0noJVEPPZxJ2ok2MuopZwaF1uTtpVZfvryhV1tdv26x3rhynnOdGuRM/eZI6oEq4nzbof6dkbvG1gIGEB6ne4A9uYkrCCmffHNhYu7tNPYvQjKbXTZQ35NvAgBTZ9pPfV0XmS+6ZUCOq8hFG4ruMuU57us1I16WIsDXkPP17hBptzzOUnduppsk8htwh6/IW7EzjgsPB8ruBGWKAJvuXL5dOi9OMrii9QYbQxEG7nrJlwoRMqN7HzeO39JWdZjAVP0Y/jtZGchYDLx4Fl8bookqJbzAOFr9/tsty9ZRc7bI2U/1RnKyLpgSfhfRHTE9e/pTjRya9rG6nzpHTJ03ks0n4TgdVQn17o/W/weHyWZt+QB27+exBiRhGIsbJFaRUPSBoRIU//tmBu/9l75OEtoiOzWkjBEXdc9AbnesXtoenbjhCgTTLhPpiVLWD/AmkLQ2omfvSncnFhD97Q6NNUKvdT5XVUUMhQRj/LWgmN2EG+epcCgziawWuDYdzql5fvQGVlUr/v9DTx0vG7ITeN5IxFYQOZE5oN85RU77YPK2t1xRUSAkf6gJvtszM7y9HsrwlLkaVtiygXZXPoLDKWXbK6UuvsFCdaNGrmY1P1HfhZIOm6YgqKaju5WWnPROQ2+KEYAm+qxFiTaQd3gHLb0AblckxGfBjiPJOKNlZv7GpQo8SxbY/Gkdo7zeeuPW0ZXREanCfVFOjXfKUgsX72AN+8RJ08NP/e85qBsJH2z1uWEYjmL9Qny6W1QNU268sBDy7DSCZfVjSBCVHCpVMwlCcrQ7ocXSmRg6sUlPwbtOX4WZ4i5ySz4K2W1FpgIKrlweQrFQyGXuungbd9CsxQHAlQ1ls8HFM8VVaxj5v7eAXVuf/7rsZnu5KYVTXUb+XfLSpu0wup6912XnhF013jq8Rn71mp2KTKCGHRAJUDcdIruJF/YGYJSrQN3JmBQy6JUDSGHnmr18XJ9fX1Z+ggWr/0tO2qww/SaQx5hq30g5HagNJpfmzFf9lNaRKS0tXqAd3MopBF7j3bY7uMa92CSldGXoyn0sRpB2zCK2D0DeiUl23zqlY4h1SB6nfXAg8sRN8SJ9AnLfNd7cncm0IZHo/AYcEMna04k/MeQd+o+n0A4Xbq2wdhJ/UBhl4a6/5KuA3xOoKSTn7SOiYqzhX/ngrBT1lwGKkJBMVwysY8YUYZ7R+fofZuAA/t6UEYighVPjZJvojjpU/wtVoTRx0mAOoXGbwUFN/06uASmSZohFecG+LBFMKWkMf79E0JzCYv0sYS5kU/Dxu7EoyaLyAGomNRdDvRtX7IUr2f8ethIsENbDKS+dRMNDiGNrxhp0TMwIyd/cvSSHFh+1zOLNIX9Z1q2uINvDn5ymXMWg7ZUG9Z+oP+7Z/Sn9lWRBG746YA0nhRYUHyHzMWAZf9/+xs4RuKck5uN1eJuOkE7r6mxokH+ibAOmd33Bl43vV40TrjuJVwrgOSni/0YSaNNHO1ppoR3IbDV2NibyqAiTisXZngRGwj4koOgj9nIdjWZb7oJvpmui+x4Y1L3SXrY+8bqI2clUSm6X+6B2WYD7X6sjY2YPZWCKWo8FRfcH+1k5+/CaAx4f9d0SHUoiTiivqRd+AbUPu0O42Zj+Qwia5Sli5uX2O//Fr1c9evV5UEjwCqM+37zV/6/7L1ARWLDaxL79vT4wQyjhGzkDrUmoWOWyh2o26aKoBgnnxYBZrHnXRTp2ijRp5VnUaljjO9zAzYm4XlbQIiyrOqQoE5kQRECTQ1W8T+O33BpBU1VzhW9zuUBVB4Vw9eB74roHEgFZTNdU2CLB93nQseytbt1lFBFy0EMxcbQtacttCOPNqVe1ZZp29DmwNvBgJSOn6bah1sX8Et7WPjxvh57xfQXHOviubbw30NPriMhPbvsXl1kIGfPkTh0Dg/5zoIdYgUXIOHLlFtuMdLwpqZewKi7pzu3FIdxvC4NaWaR3EXLmPe60/5uCNppRiI83+okxDdCKvxMOVMd9qOpj1R4qeSPDtCVZxYLPt3qFoT20tOErLZI+Ma04m7tBOVDAzU3EBLJPovGo8iq+HzK5mWwtm8BJ/+TErqhiyXvGauIoN064zH7EAZwn+q8atKVfxVJVnZy2K75gkxpuSBbhO1O5dOYKRH0V6uqRsUjgL79dqZ+9ANAbw1HoVOrV0f+ejlZN75n7KPgUj+3ej9iuuih6vuX2UmeHfgsgNDdCJy79OyNDemD7OImk8wBb8bi3OxK72C4kEVsZHuuMrKmFeVzZ5jN2fV6hA9eUhsSOG52t8g5RcqEA/Lee09LYli+SzYDnE17CTTufh247gXcQcGPe/QochnefLOhAAOC7GOaLgKZmdAR1WylDVJyTStF6Y1O2bhHJo5Ww2rLzvKN4FA1cm4xDCv+/wEAGKUG3OJ+aKvK/A9hILTY4jA1QEu3v/nQjnHietIYhkR9IQdmqqUvY9wAajPZhtMl08GGkuGP522ME36CvqP2tXdZz+N88cGGz63++IjZXeyIZmmleXkFq5AHArScqAxhOtslGxDHd+oS7CxpXMqUthe7OG//JsU8sJYi+FNUWKeDgzoXJS4odo8CH+CGV8fwFJg6cVzOq2ERrCREmquy6KZpnZ7mJFsX5wZsfehPa8jlf7IDMlNY1XAhdQBDNKn9iaXYOdujbYnWoY0YI/p3kW1imQwidFZ1weW/oyO4KlaN+qbLOwFGg41iwfT0tZOdVChoZCIGNJmIXm7zMnWVXqexWqI23mx/XxO3xHiRudtCAlxjZI9pucLuvVN3XD7DcZzfmrl0Fyp41cP8u1N0s1gDK8DhfMvBV2LBJQQRMLoCbyP2iSsBzWGhIz4pA7mGUJWQfWS3wSLG9Bis3nAQ1Z96TLlXmIPBgOknWHlUYiSlhTk/x+B3OrjH7fPZYmsZfnqfH6PY73f6nUeXyS+fasYiIAfb+q6mmILys5h3Gn8CZGR1MJZA/G/JA1y+Wg3YI49Y6li+LsVi+tw7InAcb3vQyemEYzhxYWu5bAgSTL7DtuB3po5GiFWOgnyAdc4/+t4ec+Vu5csVTN2wKm8BDElth5XViokcMxv4A6TGTmz3Ubl5vEb/FYCPORtz1QWitPN3MSkXB9qrw076kcJh1+zcxP79EBfgQHwEjeQxoav4K/wjKkW/uYlFCOB7yrfdWI+PEF1WKjIhK7an5wTANftBSIL0hj8yHXJHVofpowBaQWi5A2JBBkemuSHuRSDtcmaBoigQHoE/Ok5+4y4PPVZOVDiFcu2B4ivsTvWf9pX13699V40nHYwBtadKIq6E7PS3L1UxM6AfbFyNM13Haty5DQycMc6BR3pBr3nn5bqYE1w2VO7degN3Un2YRf5BGcmgYEo1dkWED17jLJ5EMsez58091QU99Izuay7zskyULMgMwaswptMRD9n9pAxW2W5IMiqTi8NshLu6rgTO+e18L3l8ly/49oM6Zlt8XTOsW+umUmq3BqSWD5F7uc4Zo68yA25/ehGJ015irpvTRbavKjuKvsn7mz0+/CIbNrE+zoWn+CT11Ph26xRB02qrh2Bau9a7KgYSwj/tCNF3T5avOYesoRCsRJkr5hGO0t0X0iFKUaGE58tB7QjSIXAYh4htAN7vtLXoh0cSZfeyvzGxEpXY7ZR3i0OdIiN2Reg0NbQghKBL6QJQ54jAv2meLJqLhgTD5aQEmP6OSDt4MKgTrp7NhSd9092WPi7RerCO3yizc2VxPL+LSRP6Eg86lyw/logxIgOQdO6bN61THwFNGLBEwpXRJbWPBu+0FZUIyYaulCnG0GlwORkMbAb0wasrnc1yR3cM08ycg6TAn5CF77TkiHoqZBFdKuZUa8cZU43WYmuKKlK6z9Ic0lUkzxcWfrOx8p9GaYkmAK6GLf1GV0C1ShwrxY7cFoL0R1ITq5FckLQ2PYJjx3drpx/V5Xw1bhYYa08y5iEy+xmo5jDtHVTHP4Ev8wrwZdBz/c4Q/nnGW+TDFVnHfJODqmG778ock29+bpmolXI4GFvs879+zAJ8M6MDch14VHSey1qSziMWAuNk+igEVg3WZZ0f0dwGr2uI+Eulk2FNstbr4XIjZEISvTmGzOfRsxL4Vtqp8ENNGYgpbYDfFFpieZeLJKUusDUm9PgcXV4BJR2pU2TbTD6DEMxGjubeofYkBQvVvW7qj/GSnnbRg+sWCnXx2WUIz5HeVmekkGlJUKGnxHTM5NVsAFrZp7ArBnYTYSZvawa9wFuiCJ7T+UpZlMrJ7ZBI1W3vHXDMbexchzSANwfALzyJATc1skvBNsHC0HCjLzseB32eUDBsTGw+NRnEmbJZ0TuuveAIVvlPxKNK+saE0Cw4pQdxakemi+niv1QGSgiUg/zlf+9U5ze+6yUt+Wl9PQRCcvuudTofLHp6qtaFpxKLipapPBzwL7wunpHO+26yRDx8hEPXR2ZFer9cQnYMo4VmuGMZFmpmw0P0XFT96WVizz/D4pVLnloZQNdhpKSoxdVRH25ZlOQJeW8RdwqifHGlrpfxx/eAlfSHbyKeb1zkzOP2y0Vx2u+yqJM4UuEMucEd/g6rHdRVtfOn76+msWK5SEhx91P255h7p9lVe0qslkTB1SRvaPjRwWRcwCx0rnGvSwFs3te6n9WYQVOAL/a9pjkcd2e8+7MjQvtaMqZbF+ifoEMBo7AnTtsmBWNYoxzNd3ONYLXAL496EoVRzUXrELTeq3MQjP3tgr3unYUf/ltlm+2DxtSYMkV3CbkDgxe+QHUvrSdFHWfxOczF0MzhsCU9ZdLOnybli8izvJmNQYmk65ZocKzfLUJ2ORPPQVjODmW9IMatdeYuwUep5eIiSmZvePDula2vrNafnrGXFnxfZwSe7WAuGody7JurEW0EyO4ciCNT+8odf1yRXB1ZCxihGYUOKpzM+6BuEzQEDbc4lm5mZbERBSfOX/amrDr7vV/1UDCzm9Yay9N906dBjXTfYze99HeFzy1NLBggf2ydbKewl8rPXOonuuLPTIXaLVHBB4kmNyiOSinWFJmhE8qkitrdvEEjsK6zIsxJfNqxh0ey8Xqh4BuQ2m6WSu1vIzAn8Pr2xBcpdAbIJaX/Hl7Pl58ZJl0peFmVqgm/v0x6r7qec4M4iHoB+cVqZv2v6FTGC7d+wdAwhkM1tzuw1P0tO+j18StzPcGWnnDXmoIw7IpG5FN5Ot3Aq9Cgf7WCKlEdll4uasjlBjylsMaZwz/O9Af14jpZD8eEeT/XAY5rs01LP2I/66YV+6v/pJrqBoRPMjqBXQ8XPg9PF84n7F598EExocSALmy8iAK+Bmmfiz4auwnDg0mQkKWmDKqz8bGvwDsYXJ3lVhtrA27nYF6fRGCYDEyFOCtS9pTmjlY+DodMYf0hSTIyLxJi+Vn7aD2MqNk0mSuY1g6rHwPCJp5YXVexLk+oWdwz9XI8R3bceMedvkVDzfCHADkZ6iyWavVAbWxjcjK8T7HmrgCEUvBn4yo7YctxRH1w03NeGRB9CRqFHRTdx2SKw8ztDQd4bdBDhf0jNAeonqhpwyAHbw0E96QAFCZdnLdk2d9ndyHkrhbTXCYXQXEh+Ve9XomJ3tf6FhAHza7HOBTwxXJ8X9KdgGdx9hQ41yh3gsrRBQCEQiRCMyEru50b9zC2m7/ckJAMex3yq5EgIgeMVXr8XfdNXPBAZ+M17tEm67mSGaPHvAwiX0Xau72NAuYfQ3S+rwMrsODScJNiw289S4/AFYgHD0HRMWKXQk04MGg74t3/3C5qeuuc5pyvhgmW+A/memTr59NmAWT8mrAawnucqCYX/leg9HPOi/0mzyvSKrtPfnwLikFiSfFc+X51VfVzjRAWowU2QSyw5L2er3ADKZ8Qe6VGjrVRkGTTWQwCziTTLEJ4ASDqj/TuGzUv5u4dprHT1CM6PE5YbpZk7H6YBIBQ+HqCAluDt4/eB40VSIWjT0YBAGdccQQrN3TsOr09h424Y4lkRFbCYTRV/QmaLpg5hSbZrC6dv9hcpyhHVze+0mT4X/FFSvOF3kaIQVLClRn+kOsTd9YDhLBHF9m/LspOK62cuVP8wl5lQqh+WteY3U6w/ZpvYOb0dgtZzBvfo8bHtFnmvIozi8WVrGpgFQ66JAM50yDJfgwkDgHd8IEr+5dgegJw0I+E0Vdet01yf5QcjF5UsS3TGP6mY5L1n8FMEA2QPRtDKY6gsl1Vf6I+5Uxee6RkHRJ4tx0DNWXPZ0zx3WUXkmqRVWxlbasUB0Yl8weRsUn4OjGEi31/0cYzHGYFKgEz7dxf7VPT1DGDIhGKnWd2WICbPjuptQE8SBAMsXf9RSSUOzxIcSsKDDifRBketv3aKYr55NKDrathXMoQmZreQddrw9kZvRkeaHG/Zs32ES3/B2UJPh8g4eu6rDmiUkSFDOWAesY+/ZiDFVnnJsxCt73IeLOGGXpKWJSfDBdwuIKJPYR/Xemh/jMU44pgBOog6GaWMf6G8IN6fERSIwom/0rQn8Nu9sZveOaSdwN7kC2YSumBdqZzHeqyGYfjKtGxIl8fqAikhqFaeqiS56ehUNToIW9Z0ltiZ0N1mG1AMxjVIMoc4nxtmIJttZxENnyxEKA29WpC5erws3yNECX++pPEuyBGCFCTUaTC0gGarWhot8irGWZ6ZZ/7rXCctZClw+HslymTy3pzf4eMvBUuWpe/q9sRR8P221XPWJuQNvTTZwwIhLXalhdLvocvifxob0VkrRFsbyR6S8d38jK7skWHXN46ev+IIqOjXNMDghut9hvjPl7binZ8PesXS32RDEKP/+/1bQmLAIB8wzv2+8G9qJOXOiK8cn2H1KKskbK9pVWyV3Ezg6VEgAA6o7cLI/7bILkvOKBru5JCvE2DMOW1ypAyoe8BwF7Op8jczXK2bGPVLlWC/qjudDPI2y6Ws0nEnWUUayyKqb2Fzk5AfM8pP1T5aEIso31xCKo9YSZI0kkEXDgvEArUVTx+G88V1I6nWWL5jR3TwcyNvLqpr7K3Lkcv/m2C3GA6kJzucpmhrYe4cUx1Vkj3DOQnkBVdOWHN23AOm4qfUefku1pdP5lO9nKX3YfFsqhw3E92qffIBHDJmVgC9rxy7yjtK110jyJSE5ehjC9cs2tU3UvrbD3yAUiI4Od2n8ryJFMz+uGarzUt3lO0MWD0ufELA9nQjOxfqRQMlcaAqOEoKjhPeDwOuMHSS2TI3nDAAgGZcCj15wz2PAGpSrOPrnhFbNH91bBu39KGiNjEhLoxWHi0zLryEjA1ID9vTS7vKIUlXQ+x2QB0faM/Z05LyrlaQELVnxPom7LwPx+IZCn6+hU/uh0FN/raveF28da8dBvrnLw1TqEIe7fO2wkQFuKW84XY2jRRDIAkaqaSkpwRDk6jild68uvHowGIK5lXOlJHeH1xOslZLuiVrxCBkvXdogCSTdmkT3ghuuBDp6dZsNMBPf8PVUqfrHCw/CdPNgRQogDaeaTha4rxGHy8940Mv3xzUsBnvwVdLGqBdivHFUj6iQar6yn4UmC2sNEi/FdBZ5XouC6z10umtJ8sqg64CpfCgOAwkySbNhTmP7TgJBpjFjkMfshOYHEA1DUZRy+IRF244SBaRhePuZB96QZTa6DPr7sL08kQFmKHC8c9FcTYDYb+RqWnvk8J9bsnkfQEq9ZQJAWs4A53aIheqjwmb7jlySnNYzdXeb147bWHyQqvP6mQYcLClZxPGP/qY/Vi0RPDPanFw4yjiQ2NOm50JjJc7fnmWVQ+XNoaAyL33LpHKGFIOseXXhSIZX1R7mLc2CweYEN1x3uoZezEc9gcnikdgjZPN7qfcETeTgL2mqQLXvLlwJJ0GM0Ov55TCuFv8jshiOTLYG5VvnBTLvH2625iJi8XPS3ocUNtoURC3g0TB0eMA+wcJ751l8iEr8biO1HmSBEHzJNcxrrL3ds4HGFPmuCxxV0wKwNLJKYQcZMD/lWUt6IiUXCg4+8fsy5zWKxDQbIkvrVKP+QCEY21sWSTsimjCEOSHwlL60dsSoI+dR3cK1fI1LTaHfUkLTeUV43sCEZ3aDpFCA+nEHhBFNMkuwM8sxSCTXvB6LmS+xzqr8UvgSerf2oKxF3JfwCFd5Na3RhF7HxXmK92Gp7XSufeyJTk/3roW4DVciRXFUwQ3cND5X4tRee2HRzC7+dr4AQhjvmKoNPcKtKpzRhPP6ZygEm4bllcyxc2a3G/K2I2gDVZhmZlkNb7StSNXj3S5n2NrVTCAof45s3wGorG2wyhJ1YvhCxJ4wU09GVCLL7kno8I4AihaYtQ2kjGSCb4fferfzSy7QBM+yUNhLeFSQzLXdcGJwz3fPDJzZWsNIeZhzwL0RABjKjKCBDI1mbTPFRdZ2teYnavIxa6gn8OlWT/YaX3JA3OxMM2r34cu0FLNRnVTtaPmYhxAZDo5SsRVWVDgMNQh7yE0EhS1DjZAjd6wBRKtLkqtH6Q71Ns/aVRaMD0QCPoNiI565RWzdXAYo55OGgdGvzmhLklg7fYv2HHSllCRJi9AkZ8a5K++F03vxByr/K5jHL39zXaq3nNgXNIA6Sm1EbBu/SSIKewI1bG8VJpgzz8oTKSFl3szPEhkE+Kd2JPK94xQLWRe2iDVl87DluMfS0XCsAV/1AAo388N6ceV0zqGXRXKvNpeOxYGLmmGsnGq1U3G+uGkL0T4yY0BWYy8y5yJE5y/v64nkT4x5amEYa2NsxRpMFPrA91MxfCEv5+MhPDoZn23mQTsl67D/JroNbAurb7KeRhECU2WTskTnYohooVzZblEw59P5Ld+h1SJIB8tTSLDrbBECtrzjNOeNkdsB6flR3refkmHlQnygkgjzGqBNADmhe3GTjh8vu65Fo4ZHkLeMtTSRKCprlXPlxWaGwRxEIecJdmMXDxjaVnHpbdlZccLIKfonfIX2OteUys84eCa19q2FxfY1qG6x4Qyra9YakOoyEozmJwxQvNOm8Dn/Y6BjdR/r3BY90K37n0rWxZycEgHOI61KomZ49k/xaiMBWr0eKjvyre9EAMENGA92/I6BGXNZNMPuJipLBl5nvSJq/A8arOdzGDkSRjbTCefqduS70tB9hyCHD5dLhuUhGNpxmNDGxNFgjfFNve56sxNPSojJgcMLOp0t+cwse+iLlRn0MXIh/9vSjE9HCsNq1q5IhLezNDbFImGNqqHRQRpeanUdNJn3gmFexbmIFEQayYh8/hj0Q2jEVwsIAsZFqm/ZpSrM7kkJs5/+wKWj19efjAAZsnmUhxL7Xw87FUTTvB7oc0H39wTnkx1VOAHzo4/xbP5WRdkIEziO7AMRrqlil8wWX2AWRRTwqhknKcpwuSoxsThSspYIOuIVhsF+Ako80FelnlhtUY6Isc4Jvjea7OCxqtAP3tYxR3MM1LJT86nRklZHDV1N6iD9YL7aufaKqwTSRn50DSeb57KJ6kfAaMg0MCHGxjkFaRDsA33AAahw8ZDEMhteyhDpbJJECQerqeHLq/zAv3zUr0q9xtXyoDx3DcE4tGYTHoM9pRhQUjhFzouaw9tcdybokGeEvsvt6xyPqQD9oLZFArsPMTh4zwXt6KncO3rlMuKYqlnFi6xs7Et8CwooF8gMWs5FXGfdUx5cs7W4tVO7GiS+ETfj2pAMICPLGWvsIk6jSXtFEdpYCL4p4GeKoNscNi57I20fmjn6E6KKVLQDkTYKI0Bj1enTt50wOkx3w6WqZbv0ijnN9OLC0lEwhP1CGRTkFlr6iv0YugJzTyjvjGfWJFLm8QnxVG+VfV5g98tkXhPCsIEmU/il6+Y3dKk9H6Mrz6XxhJWyMCUwu4fXUue2AR+4FAjR9heaaRnhY1oCE1B+8UzMgTC1/exR08qJZ554sxI4V0AzymQnq0uQsM5GaazBYUwrJY2n8OQkAc21+4i12KVrNxvy7AAkOuuQPYWakeRT06j7gf5Hs3lu6I5O9TetjVdhVXUg8TTz1sph0aBBQUqc4iBCTGs4CjWi7VGRzWbB9IJSniaJyFERkspg2ELa2gPoRiDRf49Cp9JpE8biseT15HBcYESxpZ/GfPu63bSLpXQ/D8D3q/F9r/ArNxVusVZZysqm9F3xXIvrN0vYz7D00WHJk7LyVv5O8FlOU9hHkjAxfkYf9Oq1YkI+1svtXFy3BQ3+F1Ay0uWBnKBz7myjs9sVIMfgM99l821V8RLY9hFIjUy+lF87kiyrHv0QF83XpXztwImCWBXVBdEECUxTk6ow9fcS5GrCcr1R9uwbf2++k8yFM40F0Xe4T5wQAYdVcyp13ie+Hrwu1iTGvF27xt13ml7fiPFesb4TpXRs9Z2YoHYrv1EZjMhmtfKeQDxr8i0xj+fQpjtvqtp6s+T9VGzfnar21mOXBRoECpdGjf4kEk2f+luftlekILiop4Fcyp5p9fdSnRnbHuwPckHPUvEY9FSlwMty0Q3mYHXdMDklYTgNpssS50SlDlW/8Q1dDL4fc1xUU4FbMfb30RfaJ4Q1uujpFNvSiV3KsIePKLdnnsA2V0lW2zL7a+ie+Uv9C8XjVIyn9uoIcE/tacUXzuESAGrsERMquNdEFZ/5IZdSplOZ0Qopy52Y/ZFSIFTFLKPqON2FEGZEXaqqQSomnEow6kI8/98HzYR+OBc1m/B0aOwW5ninWeXZ0EqqZ5RCFptRDmN/TxRqkjB2VMK6Cj3FdgbFVelJJyovet6T3J6TZluonQ0qxccJcvdRu8qm5rL7pb+9a60QhuYSVjoVPmN+sayacU0wQKu8LA7VYi3FuvUpfy7tecW5c5b7VdENs8rX3YjLSS12pN+KtaotDFmViMhWKJI/CwMUVKbJeWyr/Ngh+rg8Fb4pZYX9akN8KrKEKEIMPjFgVEqWZkWzQKKdPg55MMHvenm+9k8ZmGfFmT1zGR+PCceY6xu9S+u6JYJFVrTYffQ4F4PLCYA6r/YOAcDfuylrLsU6UUCysoqfmhU9eqPFRJYGXk6SFx9tCWq2P3SI+OqM98iJuYz12aaDQciZhIQObQl2PfWX/apZkfTZ2qzWBacTD7hpS09DtPj8gZvvluHhYyWfLer3YSlYHnMzf4j7OCcy1vfNvwEqbbP4f36IVTLffHlz62GNRUxDux1/Zal9t9E7s9+1qRnBCA84ptT2L3ZHxi7hmm2xWVWoEq20xN5DOHzyQuwkppU5ugDFnyn4iR+sFUP84pOVkXL7TEtTzfsKjmjkjjQHA5vkxqoNWuMXbxd+UyZXbcSAfJQYswjXSLZoEdcl8E+14vN9OK59jVG2P/P5NGaDAkSrK652Xuz7/BR1l8MlrUO2GhC4I4xf1mFT8SzHnQCQZbgZ7Qgb0dRJA0Jbj2Zxpsn11qAIezdJelY8XEHUTrL8YYyVzT0IF9wa3RuV9cf6NHZWIP3vvdBX42dKnb2fhUQ8iNqtYlvcGmkE+4bQUzlfIcbwcZZ74ykH0Pl64TK5bA6dkTRs2iOuNg43IfvxBpddZGKx6oTFLod1L6jjKrlbulFnrUoycd88yDpa6B46tbJPALcnQst9ltggiwc1TbxPoNgpjcm8PU9Y5ELoXpIYE3rz6UOuSxOwA1y/MYY/meA63253GsWMQ4Z9n+oSvC2Junt11gn//IDCW9PN0h66soLjLnjLPnYCtKl8S9M96mkeKDciBBSkwkFBY8COMX7/e0AltViJSTGbz/0hqND3X+B4414HEh73lQcFg693e4lDH0fHsedeWPXXE6agsjF7N59Fr3ok3KOYOi+9wVDuaLNMiCQ2I1dKN2BdVZGSATZM9zNjcU8nU7FcLKDxM81dMgk1nBGSSN7yMROLBD3WwJ4Z8+MaqPguLlcV6st0LGeoDIETO19HkTEIAIBeyu5epVUlrUXthqOYBa4WGAMDJjW45GWpSzvwDjp2j7NIlm6qKdUDLvn9b4aP16e6m76Jdtxb1xImvKA02b2+cSi66BWYthCDdmQuHaR2c/kDcwHo/DQA86LD3sv3CVjn+qxUgu5s1ku04H1FsDyhHjq2gMHxTRh1zkeTSrJBoMpCdTYXrAP6/vOP296jxh1m7Xl+QCWHphf2MryzooA5fHse7d3Uonv/CEjpATDK48p08cQoVeLGMSOArS+gmAmVFVlzX2wBsl+xcRsN6oxV4rx0o/jcSpAV7TJ//1XAqZKpeS60Da0DrzFC+lU10DJgpJGF/Dm5Dv53vTpzpQfPVNJBo+jv9bONQ/WDLPk0wXUmOjwZY2cNz6PcLufYarg/89xXqzXGK3OmMhOvhAiUEhA0pvstMnhRQ/ai/ywczAqcH48QfSnsuPq/inspz5xrwmNw9mQRXZTCGqGoH2+mSDN6bFM/U67TPwhUlRrH8L+prWj/tT5o1CClOgohFt8ezpo12HadOlyvzOh1u1A1lhYSOP3CKR/uRuMQfNQ4DVwGiqHrRZIaOHQtF6WluMrBGadlpxbZkASRpt1jqA54OuHkSvayUkZNAAuSFlpvVC5jqJaJp4NtKrghWLXgqfKl9/S41FY+p3UWPcrNqbX7q7VSqFIfyCixthYbYaqn1ZjAjc9uDWPI7F8OmXQ2Iz7S06OFhG2UEcXNrSJ0l2EkanPmGQw/fKPW9n1kuecAxL/52mZ63wqT8+lW7k0y1vyrlOP35vU2Gbbh0HwKFrNL9m4WvMVtE5iq2XluORaAh6bLePrPSQS6ZgIAyAeMVS9c/KwS9d8Q1Bq51EKIIHTrUzvXe7Frig1Y3nu7CU/t4cNYAu9bPyEEWrcqktY8ynku5Boypkytt6jVzf7ceUdbW8X/UbW0zaJgMTuQrp8nlnmgnMuwM305rdI5PFKGcO4WHeQnKig604oFCK/x8845zMkdfYmsTJH2tAPYbYvweRsIQdRsuK9ohn2Wqjuyq57UP+iIGFgC+VAFwC7fVXQ9p7ZVteVCMzrxZCAxb4Oe5difGuU7S4aYVFoKR7+w95o6IjqSC7Dr7eJ6zE/rLm+mdXVXhJEBjhmiRd+1cVqAP/aSqtQztI5RubFIpLIl1tZo/W36lmp3BO9S537GmtupKlK2x0Wa3FpTWF6Eq2IqCqjtgHDqwFafzkSeEymrFJbiLYayQmNj0iXkuFAo9zkGyxLE0xXMcr/vnXmnosVhb8Yxsuw4lqsMAzgJOnayRHbuWruw+Q1HqYqV4gaXKAO7nT2GJXu1M9vu0XTXHDjlL2nA/HQeLMuoyXpOmFZKWJRdfS6edXHrxQXG09b/odzkyWpqY50o/oRMPVtSMN27fJEalleaZCOG7X/AaIHvVP+PwtnVnUui0sePpL63xwxQFl8OrcESa46FFp7biZIhSe7sQeaUmxONC24VDMEBUmI3z/3BHJAaqJoBwz3+QycOb9jyFNWV0CzpelpWYjBAVebvXlT/yZ4UmeL4+YolAsUp4HvIaUTiqCx9LoY1G6yCsl1P78WIQxL04N6VFTbja7rNq/fKcsGShIU5Dd7umaHiF/pXC1r2RAnGK+dB6hXXx6t+fZZVKLhSH8muYRau90bZH7VLMH3JGMzGWEgmcILEAXIbYVIQNNGEun+kmcqf1ArRJ5Th6/rNDM04JIR2t2BYjF4ZRo9IobAldm9/n8Vgscx24zRztcNgoPZtHEn/wwGJAn3LAMqilt4ZHxgCwU5++WWCKjnsPOF6ZbV5pNomGdQJ1V2BT2iXMv+jKTeyAC/Y3uGgtXj/AkO6msZGghMdLH/oxin76Fc3+U140Iwhps3AGjtiuN5dpx2SXjnCFYzqu4RblQbF2ercOWQVfJsqp/2ZsgR+HzQZvPKcmoROa7uEsaqTTK3TjVTzeVafWEsI7AuKo3jC3ZvGzNQtA9ip910EDQzTcDd6JAqYHqSKpLl1I6Lkdi9FylBs0VF5KqmuYrHb1j7Lb/1k36iT1u1grjPMdgOPtMGaKM6g0fPBUV0GCUiMJsuH7XeKHvfyx0lyvjeQRQOCI4JmyPqAinUNBAFxdtujD5lzMC2HdXPOQVJPcjXk/Tms5qQntvDgNLdawzeJ7p6LCZq2jWmBI+bgbzPUQuaHFtJL+8gT9RbXWHbrhNvCwBSyUHExzIQ7oxEUtsqK8diVUihZBJsxfrF9mBrXmE+uAOjnM7dfUYk2WKYEnEboxncCzhZrWdJkVIAeAih+9jMsHo/G2Fb6RSKEFYPJVfrshWCT69vaKB6cyoaNjRlDyTdtczVsopb0r3IASwJMenxgwo+1gma50x9tKLxwa+fcI9SsTB8DLbDkcl2KKrfgkdGIhqW0eEwnQTAarkpS4QjJG/EHx5Ro0zwIPjZ6BLU8KbKUx38LaF6TGnEIv+4ZiNVvBzdgaZoYJHHIv07SkHu/MQZ15hPRZRO5RswnVjOjKQVrkSBfg1pgpwmG2xKvGKc8yGrVZQUhCk3sUTHA5iABnw7zrNRNVc+D7G41wO9lSZRYXRt3G3pnj2b+P9jKdW3KtzYSi+nwPWBCJIqRiJa47Kd0AWVqR0Kpj1gLyN4g04wfG6VshILQfPEHiucm3sDabTc6QyrreD03HNcjg4dy2uF/EiwNNPkMMWHfErjTDRkl/acbB9pT5XwVqez0YGC7yqdMwdjmuY7Sv85tU2Qv4IqZ5ZK4D1Fjko0/XXJSp0LHllcYPy7RxJlElNCaPI6Yhw5x3suwYIk2jfRVzI89A3/BVo5X/9cZJsEriUOjHw21LYPkh4+6zCpXEBna0WC4cUcbu/haM/OTAxNlFyGiLcds4adpWIsMuAJzAr14OMj0qIjyOpHDgbG6Gn/vhkCnFoqeCvictuHYq/xizZ9dum/HJqH37s5XbAjCfBS3+AsruHlK3sxfdI4Ha+C2f2YjrVLlVWm3ZSmOgL7+gGl2qmroG/V9F50XHv9gNOFxE53HWHiejMHfPVge8y+T4rYPKSZf7ZZEKdTe0a9bbYkxUftIUsUIpZsGXcJJYEoxy/9YoQikPyxEiyqeriZvrA9DniUs0yH8nxfbwrgNEdBKGbPMhLUYULVYxlY+h4DG1M41ZNrIBXSMhx7MOW3MbPWmDticBRX61dDqgJ8Gua0yxnYpFfztfszGZNKfV+A9IFalLWFKy4A+e6X6VlHQCyL2iH5PkJE4Qfhn5FZKVp7hqEGpfeK7YkzoH5Fqcd0S6yLN9Md3xuPTAuXuguxsWoRmHKaM7iKfEcNJXGGJ53p4ayNtiXu393bhlPx8tsLoPajfiAFHoNsSy05cANLLT3/w4lGhBQTiltts1SFpBNe+kMuhhjKO6SptV/tFgsFiiKlbtVV24gZu4Ac925RWwNgzG7tDV70B5Z9qgblr0gvBMQydg6NS6lGRX9YkzefBLMcbr7S6yoHdNlwhDr6dhpsO503a5dbj7CLqRF4HCGhzN/BW9Tquwe8i2y9lzBW/KShJX9zPGcGIO/wtw4isDvq9E9FBzMa7PjRx4FfZcnsF+BEpE5k5wasNRkzWKkIzl9lbszjepoT8DuaNbWMbNu4/qBDTcK5Co2OVB1kxdakqZREDwlaEDugvSmpUGTLULNGSED66BEHPxTLairJxyk/P3xiyerWUE8PpP38V6PouFVU8mGHffLJKeWckoM4+dpXrp1i6ahJ8IY8tKRot9BppFdNbsDXGiS6EGrrt316MjsI7vuMmUZ5+O5IC6Gf27Xy/7XtXkeyK4hhDfeUaIWtFljCttqonqqFYy5O02vGSJl88gr3wVJ9JezQnor46EnZ7A3iO8F5Jykg8Z2s7SdcmgGFRw9H1m+dtQNBPRegHFaQvOPU8DC906aOTVC0VKSPqr4c5C2Wyfh8idvWunw9ZioFPDWdclV64nUdO8vyl0kANC0xmnFkQwd2prey0TFlTMpAOXQUkuPn61T31K2+btGDYgf51WRpoQagzhMdwKrdqviNWBkdf9gbICapnmV+oomnDcH4M0/yD0wZWH9UfiIU0eXGefxH/BROMOha908sw0RVaXZkxCBsnxA77kdKzk/RlJvs61NPcDdSsBBcE9HGxN9v0O7VAuFyUf7BsF+xMnprtFBNpMIC8RaBqcOuVkG0GuSLTgfiZY4EnocqeVLeprl/3eDB1A2zXyUXULrXszNJFPqKRlMPWfOPpRUieaW3BwXSbWRyDpBjdpuaF+kt+hvNXwxuAJo8LKMDlqsD/swYzdwsEk1kLxKW9WCm/qtRXVxxXVWsPSiu0F8YsW+BnRwXU5O0WM/EPOB7nNg9x7S/ArPyn1vLXDQ333lVcyutSGEL65+tPKuhoWYjZPYlSNFNaClxAXCQbobJTmXKQF3saExl5NDCUsVPjwygoVb3RH1JMPlPscy3GOtur5OAtsdkh133+whfVLUkYEN1AXZ2Yf8gZgZVy/PYP/hYU/VMMVDlOR2utIezcaG9mLDbKH5e1cm0gIC+vRvpk5gPQVTi4TddSNIi2bZRSiZngoyZ8D5cFtdDdLFdEJR05eqQ7igSC1abPXUwBDAotEoGHSUal59wI90J1YZQKO8WTKNLUIRIrnJVDDyiU7ABk7Zt9sfMn6gnBq1BTBfhcwP71PvljUasFNAAh4w7WcGP5FRo6Vapy/Ub26eLSCMXcDwWe8zmjSraxXhQaBpyGbjtaMuz/K5E8k/XJB1PV6wqEZ30CYatkjrwnxa+XnFXxg9qOGA7beMvX6x/K1+GWy+zBZFeu65LeJcg329RfMxe5wc0ttoVVzsa4rKngHChZUMQ2/D4ZP6yGuBwrpC2nMM0nZzuByN26D0gqVPDV7mBoD4+5uNeOQyICArqC+29fDkpozXEMEHsgwvdOhRJHAL6L5fTnGab2nWw+7ZHuYEIWYLSwlFB8IagHSwDizVRykP6dm9tQG2OKLzLN7cHMAWuA77xucGE6bs8Jq/jciHXito5bu05BnCBoqsZ/2bQ+/LPZbAENj1IihQhxeux+UyYzvQOMhS7h/9HrBLF3cKJxjATzsulOHWKXDcuk8mCbXY47tKLyV8IH3NdT94u5oHdTe4GywdBR81AU9exlfeDy7p829RIK5SafmBlEaD5wwo7+3cRUpdlqYn1B/AtHsLkZ3Lq2+ZuKrcExhIJza/5OlCV1ExABhQko2tYcgIiMmEQ0f5UN7GgWE4//yQTUsjk8waX2TCdDv7urco4ixPqJA7aFkRXRHjlZ5ISz089Xwh3M7NeTevERTnbNKBBQRkn5FxP6PXK1eFWw23s2y4UAuqc2Y+s5IypGtu0B5Ve/tSB6P5rJplQ+swgN3m1WgDe2lKN/e54iEkmaPZpAUYug658Rxl8RnC6AxYivxWxaBLrrsdhygT+Y6UYKccvLcJwyXwNXo1WjqXaorbpJab6tnPG2MYw5CJjQfjZf7HA/zFKNXREsdbxTBXWy3o0fLOqDpdU8wyYDmeEPBS2mXNyx33v4kuuXK8mJ3RASPQyPkJyPdkZ5KRihBS8e7nphMIpTgMUNuLdVNDos17VQUwPqarLcqIn/uoLZI11+/qPFQw4k8TBtHVBiB+YYsLtzipqTcK6CWf2Ksb59BOQKqYY/d2xsUM1JHFSzyl71LruuxgsfWfPbE5lraAkjsa6/zqo0hEa85Arw6BwYdTkjNxw8OHzpUPGcFSSGKbUH1FsMm68Fl6YsaFky5QeLaf1ti9E7MWvwmZBx4WL5kL01yQ5/JjKK+GlsURAw+/rMQ6qRr3jGrxqxl9tOxeoi3OK5qkRShjxkZU4tkPcbMHgwiO+XpenQxWibjVFn/EVxiRETtmwf7OHX6kwsoo2rgm2kyhl8gpzf5h4hGMlBDBhVM/z+z/m09rpgM5ihbld9dB3ICo56y0hqg8APuNViUlCdqoA8VZlIatvyXQoVIlCZY6WoYWNVEVJ1NerMxkO6GqBGf/qLiOfWoeeJWQksW1s4RABwZIPRZdOSNNzUZWAaKEsP9/mMpkYSwLWTFT9NHfivartsrfMVDlXfEqMUKP01hkJCqECsmNu+tx50+fo2KpDMox0SWU69T31OMhbZdMi9DxQrG9Q3YUN227PB5Cf2TCqUgFJN9zoOEEUkKOIsshGT+wgbJzGbvsmmDGh//claKULlW4wM78EMz3obQIUlNaeWKDCw9QmF2tkyYmjx8BB4Sa9voZwxgRFnJWsKAFSLWMP7X72tXViXKPbpJZJff3z15moZfKxlCpzeDZeYrLCj/UuEGKhs8nQIsWKUfnkoCvrq0XNL3V+ojzUtx15aejuj5Hl8Zh3TZwb6jZ3mGk/Z46UGi3SzdOsK1otvabZNrwJo8gjx+yUQ64iuX7xgalq4DLR83NeNwZMIDgzsh8Zm2iZ49X+x8hLMmR3M248Dx8gO4q+/fdAmFdPinanpsrsQzjLhlyx2jk8En1xp8kr0yJJhTP1siuoQggarI8JaXjV7fvrgfgpHJGPnMXKx2AkTSZMSEIBBSITo3hRff2bdE7nE2jbEHGZgJNXqzDhSs3Vy/Ooy80QBFAsbrJ+8n4Jcn8KJgTaZyGfsx5FeiKyapdCdTVUZXZ7Juvh156+/Duu5bHBUzLnAipbzXBxagVa8rqDK5iSlXt5JVw4Da/Q3iw0bZgrqr7tQNonZrNodYWDYeJM18trbKobZmnAxUsq31Ul05Hy5S0+mwbHTWLNCpaxMN1RK8OhJYKyyZsferOpC8mTjLuf5fcHhKzHivpjASXSAse4IaW/wrd2PTzKPSvi3D8T2Oft4RjmsZSJvb948nHIDoL1IQ6bnUHcojnt0c2OqkwItNzthfKTZ7D/R2factzUn9c96zXGH2IK5Fp6t+i3RGe/CYW/AmLbrtrwJGvw3EwhlOqXXbVWsipCoFaF5nI0qxCansn07Yv1FieRZoKvxZflcbhvEMKyiOLLtKF+9qOILvXkOQ5GxJO0NOJbkZ8esGM4gq8lteoNoJihAtdWJhLabb6m51FsxAZ2hLsmteSrB5C1zGy+ssgfKTDozPT5L0A+FFWUOusHrZ1amCRuX/Ox/OXcfrAB8vXe3ZLY15tIerXU4yecB+6UVh8WyI/oPzzg/PO8vEPRp55F8fnIk1kA85jexbAHxlExM1MFeYkyFWEwHzAJgq6F04Db48PTg4+LWu2MdycUX62azl5hV6qjV9v1MZeBtxHdTa2D18M2uc1dEtzYHYA0obb3ywxEipXI6cXc49tluH67D7TYE5V+on5kvVx3Jj9p9ZlHEiGsmmfU2foHgJDuEUwj3Vpm9f+tb2OZNQsQey3fldBNEwG/oi7G4nAFUM3kMQsgGiqOYV2zGgr7Yys5pQkF9OIiQOcnFIZcO46AGcu6bcBkcEXOv5yvG+6BkdCyR7Wz7W0cfkwYK/smhZU7TuSogZ+r9uwiLfC7g+Oubr3WhVrHhmMs8sL60wPVFSFd6MrmbIAtkgXsHsupj6KDycjPxjbZQK1T/3DAlwYm+B9sn5T3W5dxM2QRpz81ChfuVEP1LLFWanM2ataDORnZpYDxXsytK93DPQWBGm5XYgtfgMsz+4rfx8IwY8ITQuIIlZP4r1PtACqfBiV/sKwagEjMGA8mx+zz7pg96dwIzv12BPpt8YLVvnwcK1cVk6KL9LAxC2A+TO2D8U5bcEJrAffxZnKXG3Eu01Z5d1rILS4rnveh4slFXmobEgyWsKwNn+vPPAn0MBk1GNegueSPKtEw+nK68NgtVGFjijgf+RRJOLFzJySTrctY8SugLw1C3vg4oU+fEbnzeyQJK3FuzJAvtaV6belho1kUbqUU90XYHCFqTQs3dqvVZNrP9tUiutxhBEN1B1W2GpN/qv1lIyM+2/B6ESdibEKvQsoSb2FrnKm0Au6SCFikhvVkzGoQ8gd4t2BdAGyyOFbm4yoCX/kzAtPVwG6x/xJnSaMef8IVTCI5v+aHuEN+pVw+spuSBVLa/VVbMYXZVG8b0hSnADFuOkYefrSBTXCtjqe5PWBqUE/a35KmqJSS2kY+agM6dl0MxCHrIrMyGZQ3msuBgcaiA2X87yKdHqz+lpoe/9ziRbV2eYktvA/Z4uMDpqG/RssELKzlXJdoKQ61ozmSpELRO8ItfCIiatmpL+GLqvn7vR3cJAdRo2qvgLkOdrU3hp5GNj+fnCOK8Hz5U5dbFvazvRr52oxwtrvT/vRlPDNwMhdzmbCHdEvxrjPDVrrWiRApkxeq+pH0J+kybvYxjzUMZVN5l70Ul5casx6Ln1zUW6Rse41RjA3AMwz7BLoHqI0uFgAhKOz0aB8LtA2u1zuPTSRxJCz84UnmM5GSEDAeyTjudkhg7jVYi8/i4oXzFeNKE8TAXSEqb7JT0KD9Zj03//s8W+i0a3lunfU21VEZ9Acd2Cix5PzxplDNHf9eRtSlDWJROzlHx5KKYw19Ylt+NDytp1kfmOM9G614YEnTRcMm9OBe07fRygIrxUwKgGgDZOL3hAWYyKG06lKZjmwlsdKuCu6K2YL26u1dNqfhYN5RWi8HBK4HzxjRQs4LG9/6YyynR95h/cigCnWolQxHFRyv3TU11AwfUdflcvHIKQ9njeUixFvbZx6bsdljmPHCgHSYWJJ4GhmnNzdgJnoK9RSHvxWMQw56o1/vE3VVyjx521WCmW0R4grJA63g+95NAq0bfZ1iFSsjtS9ag89c53pElC+gZEqYjVwTtkbg5IhgAOOJxvDdcziA/BgfsmkkdY2Onoxw2pF2m1yHwIvMGvFBX3k/KIsoIUx1zJ4xGvRBh6WvrW97nHI8UNRYrf1Iz8fWrwrnGeQ2p3GBNUxzNALHoLmEya5xD7/7mqT6/Wf6tEXRuuHr4AUGkGtDg0ujSH0Ch0BiDJAUlJrHXkp/Q1NsA8l+4DLG02UaD39lVMk7JtNWm/jFYqFBX7EnCwpQQPQiEldKJoDWqX3txx8l6naoogz79KVpxVUkB1bG/fUOV0NKMeTGkJBJ6OPcZhS0MuKxLrVBNXHZK235APIIVy0NSYJHXJAaECmhACNXFtnj8+4G0pgEzQryHHeAR3bbdaTXqscsiHaDUp+isLr2iVsAkjbYDLYaczw6SKi8YSBHFvGLghFWcOyYVRt9Jif2mTROXLg7Ex51GyO/F1hke1Xu/TYA50nl0n09XUhHePISzJaEkTwTrP3o6xr5nbmDpCwnITlvcXBPFhL3mmeVyBlGMf9/tTt/QQLbB73Jjw8NWy07Xxhs6Xzws5T4cGcLGA19CqForSZvcLuJly1cblDcSwtNBdA43+XMrUq9zzIFCqBfVV7LdenVjeR7579ehTWKt94yvZae2/RWxYXKgLbubMKCt3kDyAYu/vmZTCICKlTX0HXTyXwaZ1yDTfneAnGaQWU6fi9dAYP2T3epsPWJegK7eYmrSiXNhJU7PPE34AL6gZCARZiWPXWLUT2n9ZDXhbMlSNP0f9Ym17BKS+nXsSw87+NbXM7F9lAEJVyWLd9YTL+IimDduWDbpjuyNIZI3K0BpOHq/09aiqdQEO4l0mwXIRZW8bYN/hPY+3XG+qVxPgL3vOFO0CaUU6NddRMpD1CcGDjUr67N4kUE5zkmdwp0vg/HkMoFtAQhVkCm3rU2aZgIKF4zJ9RKkX5MjxwuB3y/NJzsvu2VOUpDHUo2gFIKaLBJWq54NrGRz+ib8TSXgkJQA2duPqZLG38dxz5DPsgdbsWJ/12HNkGEzuUy5jswEakEOkPZCCBJLPTjcLad+FxEct56roM6EyflHwOyqAXG8j3BdRwIeCtzfRdNCTa340cyJvgJoWugeThP+2yEsT8O/Gfhuq6gohgI4i1K1mA6YqL5c231HPG2J9E54RKPno1RFj9uJkxgS+3AlASz598Z8s3iUCX9KH9XosmEG56Hu1eIqCa5U6Cd9vk4q16h6ClZHkWNugJO2b78v2VnX1QB9OjWjebyfb1qTHtb7p4eHD4On9yTMpUqp2Sv6Sql3QCUWlUGlzxtW3KZSokSL1CotoMYTFydVaoC1OlTwueUttT4xFOt8Hg43XjXW4dlwIZgSX8bLRJtYkeEEC1FAk7R13tE16NyddwMY0CWoBa+JSpcfP89HusfQGhyQh74tQOpDvmAkBNWXsM6rloCgKnS/8LImyRainNXC5gSQeRlJRTyuMVrJitvtu5pz0ZkLpdGX5VVhzgXuGt3Inrd5jHimrzM13yzy0CkTr/h5chp4lCfHQh8qIDtd55djKOgZ64Rps5QGiX56efRkME49dl78Rx4WEIV/v+QpRYMk9biRkCyoVI8bBrwznL87yrAkUL2gBGmGuXiph6heTQsE+nRL9JDMWRMIAmf4UD3wOVAwyFUmz1hE6cEsCSPQGYiHt5qldxR3m69mMGtovSoBMSjmabGOisYdA+pb8r3fOecvCeRhVhcd6ycaI0emiG80DaDlnJMOk/h/Vs1kg49xFbfpWssOvldd+30zqcjhkRi9mm7ckYX+9/XhsF6OwBg/iZ5NIuc/NNgU+H/4GWDttc2MlLlAOsFJqFgXnc9SQfLZEwxtwzcGg9oDQewFiZ+5YmBl2Ya5zDAoWr/N/UPq/5/iPWhTtSRN+C/rSaf7GvPgasWdCC6xmg9P+lWSnTT75HuHHShUkN5nFYeF8WHH0vtAzEbELkUM8PkqYtn0PXbiArqKhZlC0g32ALZrB3WhQoG/jaMfmtU41HmBfM3RdQmmGfH6/npAUdufwTRk4PROf5v3wsnywXgskDeyOnx+Ch2NPWLl2v7KRUDNvfbZq5QN4AHHUYGqGfZH2YiWZ1yRMmItEZ66gJNkr3BXKswAegsGIwLYIg6g0xkH6bDlBIkR+ph55yYD6G3yZKAZi8v804qmnSSgsDqC+p7SMy60freuxIqSz3nsRlfNrti0h0g6aEBC5NRKGXXaTgqxJSY5ZR4lmCXdOtHAtcB694u/ByXWIPvWmC5NN/9ZDIhCCy80nXG2uzsJSirjPIqDWnvaoBrVTU9gsjpUD7VA/9jxDTaME7KsuTVWN6TIbOnPeJYMR+Rdng9WVbSLgqQPkmZ6z4nJX7UIbtamnB84fsoOTH2KGvkGqPxaNxmHWZvhawl1cQ83G2iUziy4ZLWKzGUDaMGYNqvZFZ4Bph60e19pO/ywMfrYhrw6ALber9rhgi7QIr/MWjNWH4ncy14ovJOnrk2ageVluDMZ/IwgF3HJWgWkcKByjjnGEXIzsGwlYU5uR6FomeU8TnKKc9LNesuKAPDu5z/vwl8K1DODLOIELwQzqsJk9yiQMRpFQxw8pq4mx4jy3oiW0TmWnuS+ynbmrYkXU82Q3mP7JR5KohHtUd4qlz8eyv/gTcc9qTeBVh/uptQwjEJtPSl9cbhGMPWKxfvBhYDULlAejaOSWummixoFTPMCQ6VvcGlQAW826akvJ2KNFZtp1Lhg/q+C685eakuYz+dmoG8nulgAlmmqyrGQu6hfnb3m3IV/6w7L/xvcUUz28vkes0hyoc0fPXC9BR1CZsRap3eRwWxfGKfAjhT4W4XUwPg6ws55QCcb8oiJosQUA+5FaAl8IG1z3Ol8jodrNJl1FEtAaq394uDE+G9YHsAXWrLkwzS8DyOxcZ1QiZrNl8QVCqwamDdhybHkt8kgG+oO4S91CI6MBUz1ikRmMUno6OyQ2/VensIcW887BgYJHmceMlPkL0FMXTILyWYDnCAz1vTOIWwTqIg03gX3Cdz16wUyWLdlKsGK7i7CUR2jnE6w+fi9MK+GW7R/GIcLMzC97hj3GpI/da09ut66CdlW4D5Er8VazSVPjy0OayBbjVKdeQmUyJ8PI8sQqYS6u0pz4S2k6KztYDq4KCq56P129mznWmFB7GacL4yB94eKxqVh0q3dqVI0dlFS9CNCUMrW1/41iArPyqJqoGq4kNBhxbrGaPK+vk+SHcs8+dzeWm6YkSgjPgAfLlMGsrga6yruwPQj4QP7JzUqdAAUh54mwpCUliuwnuj15kUXOHNM6eTM+sMuiiBs22Y2IrU6YXjPV5X3xXU7ruLgSEH8qlsQ0r9o+vM0RUICEY9wyHJZxaW4kIITiFN33EcrMEgQ1TPlKuRPcIQCgKrkFKuy+k3yd0oqx+Ozm5ry7clC7LvwDp8SK0A9R3z6mG1xHVCgvzSIHTVALawz++Bi9kiyFII0j4nMOCey053iQ/Vkcl+gNncnKv8VsFctwuj3p3LvoywAmtat3NSEzJm5zVQSSthGtm7DyqvJLfM54FFeRAxsk0R77U/wga6+RN6/tMjdsFQy1kD4xE49LpGk0tUjv6WfLiX5ux+GaMxHz5sN3ws/BXzshkj+XXUe0XiALWK4bSUmuj9QPEy4Mh0Q8AO76wNUBDZUHn5RPHQglMHIJteUg5DY3W8FKPtHqWVjKECRxoZdcp8rRqZBzGGBf8nZx1M1dEyAU1KyAgtzi+qzL7FPfW4IJQw26nvwHU7GxEWfbnnIbJzs9gxaBJgvTdZYpbdEmNYBbQL9qsPVXKMD0dFfTiEkvjUJTfv4toIjrHdXhhjfAFYBRecE/qyVg5EsoZkACz2ZCsVI1D51TbwYMU1sGmS6s6ypu98NKHBgrrrHll4CVK0AAn3fWd6ozmQ1RR+wh0hpvoARK6GkX7rjfNxrARf3xcTIqqLzjAlTfEi3swdNzuhC6Ml02wrNC2N25GSxD3qKWkG/sUJav+gqSIj7/K1WWtMqdMamdAdY6bwncE9RmZEP40Axvd2KMR70oYcx5h6OgOaBiEyxBw56Thbg0DWoqfhvtpnicoxREBAB/5Hs6Pvqru0KXxEBEFv8VzjVAaTuZtNhnfilpftH3V4MMpMq+g4B3bJYdp5HbdUzXlequKBTB3UkBkXbaA4KA3ehM/4D13oP6spKWaHKtHlxwMJ+c3AZW8KAA4iDaXRgcyOdr/+PTBBYNeA6cHt99/VV6N06o8uUoG23Si7w7Qh/bH6keBWWMea5fSHq2g/QNWlD/EY3gMPFGyS7FT8TTmFPk5e1J/5ZDl/iphQ5FCpE7fH8emSCzp6gd7ueqiFMvL3KUY2qfM9btnzXe0vRf6KCbW1MYnvkMhgCc6ez+KoJqCgwbLdHuTw8J/YqDGrO2pCI/qYwNMmwPVOkLWb9/SxGbeuXxcfgasR7+dB0JrUQek6Nv0BtL5KGGels05BPmTo8YQLRcznCbFiNc7w9gZBDEFSly7sR4OcGJ4JqiSwydNHTyL1omlpMHUYQwzRi0qSbH1fIm3MPr1e7AugNLw8Dnzy11icUtGdOvumuwCpdq9cb7KKvKagw1peYs4dnuAjs/hwqM0nLSX0c/MZlzx2OrD4C94wAMQxEKDKKbZ6yNonrojvxTPzkZnZyx/pcjm8KJqvi1tG4hIp+bX3TM/It9aWKYJvEhlA8OrApFjiiDK2cqEpo1ZUeoGETWAfDMnn0/Do1hB43MzeEfdPLv6b9whuCb7v2xSbJEwowQ6fuFnPPIda1d+sxQllPB3mWahPPRHtmk4wYTGit+oxkabMwCdO3d5huoKEE4GBlkoBSXAn/U+OhOCeEQLxV0QBAkfAzw9v6VZj7MWWs3/OEcGPAxoq1NwPXvBwkKWefSfqcxbvKERu7nQc0vcyMJ5WCzbqfyA2kKwoWxHh4iMfJ10nBHIdC1b6afpPqWOPtATKv1qHG77T1jfCcCwsyRAWrhO4Qx8AwNfToyvr0eUfowBPZlj0qI1vqy0gD8mP9GgGR+99UnvItkLS/b/mYyyp+xTDHgHGlCSUjvPG/Jho+XJoz4Gvud8XzgDTbQux1tHgdJJHwdMm8atp/V6o1H5JKwO4c+ovnh59XrLMihzm0wxWiVWBvJzhLGIQkSebgYEYiXrcJzZfIuQotm9f0WhkdOJixgRx5wIZOFhImEP/CIfmUU4Ir23jkrq4/zsVSHKhx9P6kt1joC3GoSzUUt8UopAmzN/J37cL6QBs9SiY7FJJq5Xsvr/gTP/htWLd5M2WlHmoJhCQ6Otc/zivclWNiel3do3THxMqkFCKIN73YXCl5Cl43y7z3LkveHk5zc+HUDfgZWBxHdPX9pNVitL3nwlAf/DQCqI9U+d6wQDjC3R4qJMd35Gc2lpqhXwTuifW3Kk1DjL4PPqYrPVEmExSnvx48ahdkyKPtUifaBiS29e1dL5jpayZwSM8fpO90azxFGsW79jAe8t8EwQgyN3zozC3oDBOtU1PCmq0STwWSpjbBCWeuNFavqq0+HLica4OM/kw8f1vBxsYNHEdkX+4BGaMlP0j3yIjY5zYbFISMoVCL9NpJtURD/Lyx+o41mkzKWzxU1kvgZq808hKtabpeuiGOJe6QxaQkGkH85NqyRQJHS3qEO5m/+B20lGsiC82d3qEuwvUIGPkJxTGYELl76Pg+BZqPJMIj0/kEs5nSEEdjcOlUf+UbzhoU96Xz4f7I1NPTzwuW4R9m33zWMDuXzBsnmHEr604MNaudKUwLNGYwEpuMofCY45zskxMS/Wo+KESacaDerR54aJ3miKLfDPPhUz++SqNesUiJQUn2r2Mort1cKGqp43zndefXrPGSN6PA/pkLD/ht1l8O9NEB/pfLxOkdI71BuCSZGQ2g3KfgV0KBXUFnyXZueWKW/wT4rmkfKZcwtSU/N3Xe5Hs0b1QCokQIHC9mn1iDM1J+GpTjDITzWwVv4lrEkgLf63kcHtCi880Nva/fhEFRZ+NEl+s2a8IRgFbeZaCb2VIbDw6z6B+Xe7MTVKrpXJv8m5yvbi+uGuvLcKzrJH+0KlWbUZZ/RUCjPhw6MsCEiKjqwsEVpr2FV1l31/HZf3WY7Djm0yx57VX3IpDwURkM3afUJli0ESE6lOor0fDqo427YUleTbNFlo5yGuYgV1hDPoTieqXUG+ZFIllkIA/weAGaA+cELTfY9NOdnxPhfMyJG7n/MpeMl/vSuSru66+Wp/aOa1lxI+6Wmik/5zC1Hf1vwiN3wpOGOwt/ZbZ4o9WtEt1owzDP6K0b2EuET/9U+DMgTR6k086Q+V9qNuttCNboYysQHS7rBzyAW+VUyL/uOXi1vnIAbIcHhuivVqN1Cn/VfuVNtPw7bn61Yu54qtWviba0KaN4DK8Nzjn7Mjn5JE/s2AYpaiDAFR+O//86wqPoLnNK+7QOceXKzhvsw2HYOHN1Su4g5QEFF4naf7wD4IVdiWtsfSvu9JCdf1GxicctxhgzuIAI7zkzH4fFVgLF2u84L4XjvASF65KAky0dknuqurGrtORRUu8lUNHB7qQWdmIyr4iaWD0WGG+nJRg1DsI3RddvXF+QzPXoNOvGgH6BlhGEhu2F4j3Xus4VNm1eOIYKbrCA6Wr4so5rUVWOuuWiNvlQguAgRlxGOrAjDD9aui87d4UyBcARK5VRMRgczoBvexipqom9YVBRWQ/8ntS6hbZNljN8rJrU2WIIjje7hvxSZxXseCfqMOTF8moIoY8R1TS4h8wLchQ+Nr4To4HtpHnmpPcg1MqMXJptxo4CFHct7QWQZiVY52qC0abFdvZ6yZg5UFnDvi13LaFRnqBFemWOywbQfINxz1B6aV3aMMyNsgI74F/tzNNmsdDugp1tdiLyWxs4wFVj+83UGAPHOwi/ne1T+JFc6YE7o2Evx6IvvdNFHeD1voLuoquVSK9p7k0sGgRYMOcxWEnoi7KgbkrlpuKA00dONHU8slYW+2K97XqFYaiXWJWqHONFULs6RuUpSa7Ceunw0nz0pAU8MtOxSSeHGWCaqnbWd4agWnzT9vHyRr462O6pyEkyH5QOAO104ewfUmPBdAxqYWC12eT7cwhNQogPTB/mEnOprRTGuZb2tUMZ7ZBsN/UXflHADgoE7SkfkZVFZZvOdqxZYC3QvmynjaKKp7ZK6xzMsegcZQzbrDL4sGDC2W9VOP7mVK0Q1gYDR07u0KEYcCMK+WeTCcOCLN2zXGwkKmpupjFiDnFdQKQjIMAVk/Xlaw9JqS/8soeHzrPGy2PqHCG5U92YlmQtHUSWlUzIAzAwVmMHlo3VVSMuAAoO7nteYQY3MZha4rJJoAVA/gHhd9tpWv+hDqc4YMO0pPMUKe6AQTzP85lI+9am2Mnu6yifUUFa3otFIneqcwCdfeGudw7SYPRCano/059zk1UTdiPl/R4FNm6FNeR/dwcFyUBbE6u4pffOgLlzL61RnacN6SzltWZherx9pF6em/aQv8KkViAnCt3rqO40wdhLE7g8fO6Wg4ak4rg0Oy/pRWm94jB7FtGGOEvt6GE3fFOJLnHwiqkHrVQDnoFjrPtSzIeeO+KqfR4xer3T0ul+64HOQmSxcyIYOUUv1SvzcDYBsZVQnrzqo3mpxcKCfj+iAnhlRiiyfCYsmsm+I6/tvF9Q4jKSd5V6CazeFqH0kF6J7BP3xNZuWyk0T7CyNnFU+T+IQqYoB5lleZsoLDoPauUoE1bMa8MM0dAyr5gWcG6616QLDBtcfib0TQCLWghkj7LpCXWnNMOZbD5pofeBZrLVsMsX0qGqDpdq69SgU2QUH4BnT0A5XxXUdza/Qf8qaaQ8CrW5jGmnz5pi0kIfooy3LIkxmEWr4zhQpqW1FnNJQLvB7PZxQSnqJihTK9PWNkH9AL0QM7nwHHhJRwa0v+1KRapUnWnEU0dBW7bHed35rbn+prJ/RvwLDB3LzVCHyHF042fS7kwHhzG4dPyGZZrX5grtoEEelPbqD58aaOaHSKoq5I6ZW8t/cgJXa/bUfdSnT6T/3+2Qqcp9cwHUiA0bGvnTVSByIEZzIF1HU9ycWN9kqwt+j/ajX0WxxXHoFzFmPlifDgHVUYI7FkrcuZC9Zv66ukrAHXG9s1t5qxetgMA243NA8fiCm7NfQbddivjzwAKRiAWudRFUzqgG3CCLnJ0hQrSUmDz8rj0ube8RF+IIqN+LxkluBvFAXHXQ+qYhumswLiRQHeNBrqkzQrIflq+FcZC5l97k9qlmi/RQrSIvHIZAdXXwNzex/pcl8S3lEzaKoq887+WkYTEqPMRn01yqatxZ977HXRjp/UWf1xRQSxck7XsAHNAQhQTQQPjc89NVCpcHwreSuZ/HwxQfZ4yqlTRIhnOgrHsziCdwBp/zNN81HMOLscgzhMJv9mBjpB6PtjBpduMXsLgOug/Z0r/OL5ceZr2s9EQsRPj7HLh41wDmNfny1K/xcDpAEjC2g/Zd603noe+ZEVpeIzsZzQZo4jWNY+Q9IgNZw9z6fWN/pbiCQ6CZLwimzuqoGNdtmIFmL2u6RSJk0eQG926b8ZGlr2BFkRlDBnx9hirJGuATK8EaVInH9LaGWeXUwF5QrWkBGZoOTWjrixckn2H7uFJQBjTNPFR2Pp5ZDmQF0TiQXlRa4ZUMLebznwv1kPwJP9eM4b99MPwE1HOyU2cbaiXDmBL5j1wSRSs0I4OHG8bScklsJYZGHnxiQrIhK0/WJIYHOzGFkeJCJkRb9hdUp5aKnYMiWyCuffRZE9apBPLKK2X1H1/QnPTc3FoRxF+Bs21C+gW4lfXBzuE49Uyp/uE0PbS+VrgsavIhz6kkuPsTd//OLSVkgmcb25iwdhwRZN/bl/Dx0WIyznlI8lwrwPueP0/3uDpO5809FJCTksrsy5cLtRk8XB1C4sH3/XIPoI2VL3CqmfAsl23qxBQqnzeoDAHhGyYT4aXtRA0iUSciKEi3hb0UFqk8SFDXuqka5lQGTpDv1MOIZj6+zX/7gwPadkIBCaFmdlBZT2dnhwThp0Nni9U+ny6cNLH0lkS+38RkvaAaHMIRJRO63uuwfUDrkcDm3BQRMOVBcZ7lpfvi2wsLCh8bMDmQn4uEBrQm5ElOSY/TRq4KtPzNlJ6K1Z30PHZa85X6hWZQj3KPmamp1mMDtjUfTSiU1dqVGJ2YhIVUdArBmD/x2PbpjCnsjtWFf9Jvl3iHlvjLJYCKzrjgzigvLY/b6QprEz4w7MFHP11eV5M9igddviZyT+PeaXLz829am8f4sHybEIYwoEdW+BVZBJu+LIC7ZbdQuaHyOErQUKadzPD7fE8x0u3Q0E2XRVZCaRuuC4+9xW0gzb4XkD4ax+uvQuBUZsrBFTDAVqOPjmK+ebj4O40SowKmVt9LuDoq7XnlhdQBCVe6bLg7VBFjP86Sv18qtocAa8psSCVYW8rg6RmJrhza+l066IcVju1lnidcxBfwV8I/292qWeojzXHdECy0y/VCcAbIGSQHI0Sho4MoVcA5D2ZJ/2M7ZEOyfWM/7bQ02EVYGEuTELeXBsdIr1oZKxKUK3CblgMaLwDD7q+uKxLDWY2TGyTNOqJ2+x23k8xOJdayIwX6nE38iTnWEXX3t1/vAcvrN/1zm+UIpoBDnSiYuWIbmeNK3hklt/+89cRDxkyoEYntbRwSQSaJ1SVwzgVroMH2hc0WXwbJNEnwC6oeArC1D6ms306Mp6lpzgUvL7648pVmQcP9A4YI1A7zAoHlWvIGzmHl9df0B+Y95IQ8Hr5kERBFfBmTwzy5QNJ8XyNBt5PNBmdDXaR4TFW62tocvVEmJXAxlH9qxrsFMh8d0gx8a1OIi6ZlhfHODd9l1tR++bkMB2YM/mqWMHaWN1uN8gD4rT8ZuB0xNRaeiQL0/nDkzeNoAu90Kj2hO8HX32EL8SOZohAup1FZdD6iGdlLqeXesojVtDdS27RQT8Kr5MIoUG/v/pr1l56baYTRkEQRae63m2DDNdmMV381ILVlnTARVKiaMOMYmOzi285n9TXT4BYnG68TW5NmPaEcZzFyLfNs6T/jB6Zfy2F/Ei6MxNNfRM997aTb02aSEeHTDTBGWbtUAAKSuMKk9sxGX0zFvuyvKorpEfidMTDdTzTXXbaZu2OJT8xLVcQpJaOfu7ku8YAC+O+fWcB24DRwWoMxoxRukIW+pJa5UZFo4f0nQcV5zAmDwcEEVnttlntWpX6Cup8V/s7iR8SyPFNkhaz7bVR5XvcNEfYEV9he96JW+MAgLn/2uHQyoQX9LjEUbgVrivKtG2gS9LocSkBEnqOINzAhgueFfOD3O/2SPnHaK9iYuheke9rdg7Q6Yc5gJI9RxNiH4D51l4biPokErJTGRkrp4TmWtDmwirfDad8hsvEzuPBDu+iuBUsv7Y5rYn8ACBghAu1bJKPA6ln9t6LzifAgPNnihQM/5H8Qwq8jYXrLZUMWajBCI04++mrrK6XK+XV40x1DZWlpB3vlvMhlyflCbXmgOlJMMCeqFYovPjAHsVdHNXhu4MWLRNjSI+Z841hfLbgPYC75kGWZjiGlMB1eIl1QrwepuvzgmORFfwm0DWV3urqu23zyL//2a2Pp/vYWehO79DZsxR5bxHujRtmGaxjGsm/wegknv6ESeJLpXIgwzZmVZcq+RQU9kqdVg25qd/6+V/OgzJJiLLLI+3ucwyTSyhjODP7Ond4OPduxSmzGmDzNf+baX90QwOLVNBG3eDNTbnDcOgq1vRGYdj5KqDNdcSUsW9AScbbzZsGl1DfMF6c1jUEfYR81FiyE6jesvywnigmrcFdbT4FfAYUgy11zSfGZ1Bzef1J1DcI9J2KMpla5j9vYcoAIa/wbcfE4ymGOkzQbmh4xDlfLonNqt5jGhK2AxbltUbV0SZqCnCah5G1SGOSaJyf2la2qbbtZWBRnFK+cuDpi0o8Y0qDumLKbQ3hXoGRu9MqVFZkvkJ5AmS9ORL5EKc4lSrIJKNeZ15LtNqApUSQGlaJXzs6IMGpxKMkx+J4baP1w7cEGxcgz3pNzWnxpziYc8ZtR6z5KSn8dYeDuyy87EEjBFFjf5xDbZtsFS5xCT7s+9FKM23SQJbDDH+r2sN7/PH0mXU7Jm/0OjovgZw21DrGOBTSjq5e66ieApOz3tfzy7iS2jXvrn66gJmjXYS7JX4V8zfJS9JTUfHF5jjQvb/o3Eif9du1TCI7cd5asDSAkFdDxzUsifAypqtG0wnjM4Y0nzmJjLDc61Q5/7IzuQ67lSpy6LX70wmhOD8U2CT02vS8IbpOfBPaRicuYEw9lohzGIpfJfoZElPKxayyujnjZVMR5R12pdzg5VbFa0AvdkJGvL/9aW2CgDQ9iaJCrcNxDIJwXjeDJ2pCMW8qlW2l8Bm9pNY3OF4LzDdn0D4rFn6c42Dn9dZ8TDLmWTFnN1UXb+pVdJES1mUIpgkdv2nqUthdcfi8/LBksf9dh0SF6YGyZeou1ScxCmBOlGcrCOXQPqnd2Fgr3NitP0vOd2/i2pQrNnwi10aOunYK6AK/zLWVk3i7vxNbRITr1Sb1tBeHYBVL3gjb58986SQdo8a72sfq//R84ciubOnu8xRcV8rqIkYFJxIA7taeZWcov84QjGG7SH124Zl0AxV3UmdsDOiFyemCsSJ5G/f24lQbvIVT423zSc/l7s8yci5spIB+JQu/Knb8X0ypbHyRv8Wg3QOhkB0kWeXV0U7vGX5I9S0UrhT1KVtYeSRzuumgvQIO/LbJ+W/peCnr9KTCsVXfigFMm6RuRG7RrmJHfhCmQY4JQz60HlAg/xMOvZ7QZUEoJQIUd05Y4QLaQ8kTT/duGqgiDZJ7x3PdQ9SH9ZFEYeyM3OK1jepV3gbmd+DcrURa43hyw2GzJANS4UlFIPWJM0E2J2RLHS6DrQ2cn+OS+S3B+mgo8aRdPHDRlG0W0dmPbhtqackBVu9hMt6uX9BzyDeOdwsWwNHxWc2W/fy4+8HEE8YrR9ggubt/szmQLkpr4Iah6wRL8vkMJIxXxUharSryQwRDa836HzSOHco5t00HjQGFEzogYk/RVxotccIBorqrbBXUI78nDJihprHI4Ljzji1gh6cpYFBLT85SJ49C2kv8YwH/O/QN+BHfZcCK7qzIyn0FqTuhQKbDnA0A1uTpMaLiiGVDNhfghyJMl94mopRMyX0aZk0r5Ijogu7yu5NdFSBMIb+9SiTdUFDHCMS+yk4TYYMDYlgjsMxvp0AmOB1wS6wB/AJxdAI/1phLs6LOpjLGbOXXEKVPXysUfA3ovJH/Zi5u55aiHsB1/Oh/QWWT8CiiAgg8JqG95EHAt4cHxk3Xy7z8wB3kw1QX5jhkmTZ8E97Z3ZSLlA0TjmCPvcrS4xBlp57Luq66uCjChO97B8PqAalm0IcmlQikaj0Y4+ArR9nFVirCNDHA1HAu61EKdrQDjGnYEkqIVuQkFKHMi88gbOEGg+vS7KoBVn1WcInfHYaOx929jleUBRk/wmHbDs3x7DWgbY2OQhI+JTOuxcFRDfmBALjkv0SOJdjQ+iC1/Yk91nBpUTqCHX+6/RBPDGyjc9aekY+xI/e34kzIZ19SjViKbdDP1q+1hd/6yI2+NETC2OL5MRwkCWRTGayYiNxVOyCwoPR2rg+thMdDkm4c1r0Okdrqyoq3HunN7UDpRuok+7I/yRMEaymKlNkc07j83M6EYcDVtXuJoRztjGnNGuckRjoE41Ev6xMlzKLK1+G11qp515sGNAiBCtGSyOarVvbcToNJVFAMue5lKqavNTEr6DmhnHlC8MFP0hTXAIJuz5WWXAgbi/BsJyuuiJ2mMYJcljWYvwlxRuY9DqVGeUt9rhyTGq6SHQDeqidrnaW9vG4XWshcC6YMy9AI6N+EIqhugjYF4/NAJl6xgAUiOKHeXkNqZypStSFdkY2f9TGIyqvgStuc3Fw6SrMJ+nPkZkyaOchqy+6JZh/OvOIdV0gP5/b6bHHEUn+8kYDwwtCed1FSs4/6gcW4c7qfTQlv9v36pDb1dVfZcCjpQ8QZLzTD8f6ARu4ifOr7Omu8frpOdHyDDaCgHgtXVaAwB1kpZHSf+OECLp+1kA569prlDpoyqkOZFXOVPIaxoO8zbXIkavaWAOUTCqEWoo2g9SyTlwEldqlNJOzNyi+2lqD2vbm7P3GeJq+Th1voOsiJIBuiStToS3V53y0a4K2FH0AlSXSrmY8wy7DA71JzBp8iVMwtIh45eZ+3Szt56pJAeKeq56psHVkkiZNUswIUPInd1R1V7WtMmhAWKR0hSj9HmgYqI/fWmiTxpvQ3drFWxqyW3EoHC66pJURVqYEXHImSurAyE9b/VEaE8hBvP8eDDJd6PvLvs0iX1a8KqvRI/i38fc/6RHuiFQh//XMJ8J4c8+Ajauz5bTPhKTnYHq3n3IOskNVA20sxRb9Yvt1nJgatKR+DNo8NnIUA/h2FkKyLX+kyljBGGIHwV+ReIxJbiTH57XGCxbUBLIF7cOcOQDqF1B3Mp497KzUqvWvy7CTrXrl98zBCLJCuK3sQfLjgTnj+gtX2FFLnIIfmQTbiQiImYLnxB+qA1NWk/0p0vdzZaYOyy/yLKmKjMIlRcSmBcwjGDn7MK0NDzH0dr13llhlV4yyj//dfFFNdkHigydNYofdCohyZlXefNANFXeihq5LI7w9+WScqRluwvE9SGkwfxIhNVMa8b25UMKx7O33v3rwXdrc5sV+tFyca8pJANh8WkLWjl/Re7WJJlQTobvshdqvYKu5P4DWZFfsHnS6FDJ/fI+ApWLnLlfEAyzmFkpwmm6r9A9ZAafNvc+yppjWFsttTAGW1CAv8FdCZ51xOqC4jCZfhzYAxU0Z0zf+VQND+zNQoUWdqCdG1RW/0AkLxe3/L9jW/qkHhTT3n1HjnSixv9rvl3ofaqK3wfYMwwCAfGkao3Cam9ZjKQfUEu1Rsx0tesXZBoNDiZ48JF3Xor9LxZm2fhh5ggCWgcU3wYO1zfLoxV3wRZoPcef7aozkTy9bB1CEqj84yKjzj6xjPNo/jsLB/+9Gkd7GZmxPJx0dajdJju5eTIUclIdWaAAExOPT43meJ7yxvKpsq3D7RZSZIytaLZonpwrfRAiDixXlusA6UP8w+IEggPMrj/gjzUtTy6U4b60nVOfQjSIaSh6eUMhT/obVeJC1W15TusRIoI85ROJpU0pdh6IC7wpQLTZ0rWytwyD6nLS0vfqpFVv3eVdA2gXgBYNdyg35YbTwwO+3vYdR7BIUXyzMqsNDwnc7z1kYeT1Z1jskgYck3279fTD5w3smmb4Yj0l3HNoc4UuZCP9lm8IsTNcXcreWU/z8H8jVw/2y/yJ1923zAZ0fmtNYh/xNbA42v+mHKlEoLkA9BIL5P3DK/O0udSnHfaNKGG4CtXn2rpLAu50NQ5xhb8rKmz6yyLw9pP3FC8HEXDfv90N3LEFoJ+qevVi7cxlt2Cu42cjgCGYAAJowO/eAQw9W5DG5scuD2LSbzNtnRbtosXhQe6JiJXCQvDPLhqm1jqbtooOF1T8r+a/sZaP/OZuevz98upcIGxRg3LT8HGx72tx5/bCaGkG8gDli702eDBEWui2IjIDmoB4f2yYL4p4MAczgCnZRrNJmpXMY3Wc6sjr0c46XKe3lTruK24zrMQo1H/aYPJuA8EDt59RP68WVxBoE03jFjE3DH/b1z1CTC+3SrGCZZkDh/1YLgTAyenyDLsbHXr3yV9zShQIvPe2L2A34J0FYzj/7Us5yf9i2HzK20mHhE0MSc4hNUJSoKuLUyeFU//1B2HIJPGMO3ySR5KN8iwBUYXteycK+pt5ImM42wVa/calMXHMVg+aG68NQR+XkrIAzC2SIdG5SLLMZhYnUwVb1YYNk/ftA+lWxViYBREdIUZbFl67tds1Xnl1IIk8qUDjDlrNCGeNE/4zmAXmI0Zt2IfSRjpZPMivjyVB93hJlPcYyOKF/zw5paqS+VusEXSJV23YXny6vqL48J1CbvSKd4lZmcIcZzkgTEbdjESTw1+T4Ec8sq43eT5AlTr9FQFI4p8eoxFpyYO+vQGHm3hrrZu3odE+6ZwKIzmnU/oePkqlAfwTuytfUiwFgZQhEJl36+Y5vNRGZ7hXHnbEIGy8hFgCUE4clzf2m0Wt/qGXFZpK8dvn9cUDCWkE4r0m8JxDWwH5kezF+Z6KqW14wyiaiFWBw62ewGeq+d6yAwcYCUi7bGdolFMGEeLKiWREXnqU10+r5fAwe7G1gXWGmDlN+9ZjcgbNNBdV/FacI1bnGr7ML1aBXeFeHvpzlZ1TuyV47xjN3k4cyf25yB0+hLFcJOJH9pq7w8b8XnuQayO5vLL9N7ANsh7rCZgabTwEWAweNgdJFtue8wyDxVpRHfjiJmHBFuwobbQ1nTiQL7mtjRCzd7odEHcztjsSMb+HnZB3m6CmxuTxMoG2Bpiuozh476CfimWEtu1GnPk1yyuTs1HTbX+UIrMNhhXOC6xb48Zn1cdyMvvbrP2hQVWO8G+Dg2m90toeU87wp89r3wARJ0L5tNmX9fcywlm0SYkm5zLbDQwWwB8XQ+2wvOfNYhQBT3hsyadJBL7bbpkY0eOKVslgQfGYgWL5yPnyvxff4yPc+kRsGx8V/HvtZHd6l4FHWrIHaXcnDyl3HcGubkR/CJ/vw5YKDw6MtPUReDMaaauar4RkvD8myluG7jcubNVc8+9HPBQIezPuEovWzdLTWaq5lI09ngt3l/QT2Yni5vSLgPIbiAgjr0ibgkZ0FAHthK2gdMedE+K0lmDp8+2N4SpgnBQ160TVV3xgktssYMhktXrMjpIfv8bUBp+kSQmzrXBX7Sd4UxP32Soz2CrSrr6DXNFFZnAK1D4I/ejy7OwZsZ7AQ4NwR84Xt60xJkONPukc8Tyk21YuuNIzNXueXTGRSpl6EFt9izSr/w5/4c9S1fEI3tXi+Mq8xt1+huOM9TGoaIA3BkzBqvDvQ9l6wKBPgabrn4uS070db1UpPMwinFmxfGDsjCXeBGYduG+Qo6knhQsD8mxrOO8sTHPsRA2btdA2l1yTR4Y4ebE5J7AjEiyy41hdJ+Nph3dZygVuB0jPqYYyGMl6UjNMMX2X6Qb9o9LA17o7l6GuUbsiJGYJiu2IPE9n0pzDqH4AxiSJZKH8q3oE1mY58w4TlIvNM25zBt8nl8cLPlVxVPyxXCTTqmUQLdv1644466ZK1vQ4NnXTLliBrpav7xN69WWwdVRm4BUEv/lG5AhTamWKpaQH8XcYP23xsUWogdKvRO4rKWAcHvHkR87/RkqbqJGC6r9qTeLnZ1nYfhcr8WpbsGf/qFAjWJVrxvNpM/3mzi+h5WCJq1ITLgzqhagJe0hmzztXwv9Y35HwB27hCY34s056H9SWn03iNG2/T3X5vIAwGZ2XHDea04N0XYUiHzgq7nqlGrE1ZZmbCNp/DsJsyu+mh0IsMd2AERRrePtkr2uiAKm2Dvq0N8Hnc4cK/8IhXJYHAomEZJQ3TcHhJToaN7QlFsc6VTceP48Q2mGhx2qO1mGJTaUY3gQCjsWFZo0Y2ghIpKk6gp9Zc0QuSiWldRHni5G+CncTwvD3MN7FtTWmKK3qhnWlschdAylxBwYbhAsnOA4exkuDS8luLlKGyZAc0KQ7ko8t7TP7o5N+6IRIG+DPdiGDMFHaTOC1g631/rvlPJDlHR5Ni+L0yQevQHBCgoChgh3n1yhutnvwdrOZTN+F2PCqSJ7Qs5BAvge5FIKP5iTEDJI91Tn6t+0Ur7Tquzr1yatP8p6rjVnjJVTwGKXv5qhV1rMzdC2l4pOyzqYgMZa8mcWaIUOTwJr8sDPnOZK2vkykg269y//chhEXW40BoLyB+bUSFOoVHMnI8BVBgDw0OR/zphL50iIev2ULmJIQqtqtWTaaEozXdGx+cgBgVhETJ7BWH95D4Lq7c8p/WTvO2ITfzw16o2eUMjWXq+2MtsGPNL4Sp/5+FjssuXoPa5UIy0CxVW0HpiNp8HTb1PyLrEadUWvzc9erPMoCx+O4kDq9fgtE9og1pCCA3OK37qoHe2CNSocZuKPRK2jKBK8ldP1984pqGpg6XBW/s/tWmHqO48kwonP7BNbP/r1j57KYvVWTHBj/8p/JMK+sOZSkQICK92gz8DyrG1JP5zrrR9c5AtKtc6UsjLS842pGYg078nWIqDzadS+5y9u09zNhXml4PHyUuASV0LhSkooCAcR5qgRZTDJtoL1ePDX0m/h3mQEgtx/OcC7krOtsU8VtCFa/+wQ1ONECdNLTUhuaDpRAkRT2Q8xeWgWNnjcFi875hjkJhbkxQf1teKcmFcwz29KLI8uKawEHItLsvjvb6RtfTCRpyiQOHSQdPTJQWshWBgkafd7Q0u4od46qqTSeDQA02TpjJ13kdWMAEj5N5khXv1sOSPHMRbG6XY5s3LCDzqk19eheDSWCImMFq73ROZkbeNFcx4TrrUQ+5ftvA8x+32kPlBKyUINtZ0ofW61C2Xk6AFn3OVDE4/7QqIgUtqqfdeDhIp3UQVxS6YJzdoX7y5t6HkYebAzff6q/u6I6CLojvv76zD2dMKeiRK57Uo/95tHXxAVEQhWdBiah2l1JYEOaJT6WkkLBMC/5GJpknGP6AlY7BjX6/e7mERBJpfxQjaeKV2nzXsAb02VgN6JeJoFZwl2G80/TqXenXQHmmLcaZi6XztRuS/KdMFYaXFcQOXeDBGRJfyRT97vAzXLgTHivJMPYRWU/JEW6QXpMJLj8k+vLZk9slxrpWp8stI9Fd8INcxrJgTHg1DFHToYWILHmfy1IxsSNj+qF+LCkF1NWrZE0YpiOW4FQoxLJiGpceTTCZpGl41Ro4bPkThTXRAh9DsvZrUzUVfX1mP8K82DY7v1HPc0eEjIHdYeSlo8kNxlb8y/ySVknOUlnhechifD9wPIWMYG1cTDX2c+Ikyuv3VKAul7AjfkcpwOQtyPtiIbXQ7dryCjBVj8x/tsB8cuiW8Zpt8aMDol6c8C2NgGhcZR2q2Hz7VUpOTxxDm2NjmUkuLqLnCcnSzHQLs8JwchO6qjrzYLAavj/dU/KL1rD3bdaZDzIEgtNFZ1D4BXKLuGOKh2pPCIzdUaNaFb4snzmrx2y8SJSGHHNczHN0fEz5mfZ2ziLr++gh3CggGcdOMJ+UMWcbdvs1tdztCr+XvjHn6vFOaNRQS9nivvMduH2g3tAcAIhiUo2/GthYHnI/YoG/4YVM+jz1e8B5/F45NASrgvcAGnVpZYryUgFjSEiByk6qjk6knF3rMvljPMzHkKGhSoe6lPq5rc7PVmfydUhbng7un11wN9I1pYxlTXPzuLAjdjKZP4/Edp/nlXHyIzWr+xVMlh5lmpnEfezel9LaQVeGz5Oq1qSMWN3vabJlVnC1M+qk1I23gXL9fJOA2Xdy+3KKjgcZ375IjDBPct9Z4oP2p40YES5znLm2QF18OC5u/GpgWmwo4YL7BiLy+Q6czraqvVp1w870pvNPM2c5CaCDzG/5c+1bazjEGBFsO1hjDjxECNkOc6362OUGQ9/m3IF3bQg0icESagqoUSf1wNhfVihYq9SeJi1UvhVnQRpJMTyu+9F2xshbr2BOeuz0tLcSDEFPxEQFRvXeuRUQpWi8jrj1hkleJHZ96xlsXSVkfMIPL4fMG+COHua3lPvlkZk0YaEGC60LYe14FaGJCa0FQWJkXZZB0ewCrRDhnylBpUXcl+nDd2m3B4slkCdrBW7OjyVceOgJUR7lMYUI8CUkqt2UcRz+Y4LdK8xqXemcZeoFiz/p+Ibpm+6jRPaUkmIf8mBzofgW5mnkYlS1fejo2WLSWAv/FmXF4Bchh15G8XHz606h62uLeslzRin86DYjcp+jbJmwlGnkog5GWfqGYnFXGtn3kJyDx7lvtlQFAvNY6+7S5QBdYdYcWLgx61zUucOws111Kuoq7G6C+mW/JoIcEb8yRFtUJ0uyCuwOsFooMfYoXX/jRjCA68wD+nfKQ42nrLqdNliR5og+wPVhxS+4lC1McfhgaPnkJ7BPHR0Eew4+/ck2SSWuJWiRpDfpef1ErST5QWZ3ZhDGzYz9zvpA2XslvkU2ej1DdB0dvDqfTgoNCj11pqYyrye15GxGRA6tCZ77Evt/bVmEYKzhmWxa9EFtRM57xbiflW10TOXbel6hytkaxputlbdZw3GkuBeZTtHyClrGMtBfCRRC/VGIpA4oWjLyoW7Xy4Wl7R8SD3ZugK7R5EHIb9VqOIqYZCOfeDu8+y37ipwOxF8siA+9d9d+MaHmQQBkOIQzzC6ALZq/LoGrDtmbaxFtph1xNThvSdFzAtmngYaZ8Nb9pAWp0bROYkM0OJ//D1hBoR5RiTqFv6N75fRTxTeyUnjcUCpdFo6sylClfQatjvq/WtQzbU7icUurPv+MhQKiUH36Kx65g1LyEb5P5LUzmBjKVD+ceu/WVUC7hrOxfhm/5xDIPXkgMcGcoGMUbGGc5/KgVGzPozR+Xzna9rVqexOE9Y03RbIZgAgACXqKoTQ/ISsPE+pAHRTLB87NKllH3+2h1sDvZ1B1uo/urUDFhgqJrslT4tZZHHIOiHf2nIAwa6bOoT56RzXRMr0IIeHDprlRoltOuCzn7DS0RmSFQDGp
        - #1:
          - type: tool-result
          - toolCallId: aRLGKsxtrFqh8ZgU
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.