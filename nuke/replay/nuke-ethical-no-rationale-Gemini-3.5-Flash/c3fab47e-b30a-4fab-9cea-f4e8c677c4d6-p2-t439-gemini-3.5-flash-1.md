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
  - activeToolsModified: true
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 30
  - replay_use_nuke: 10
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
      - Strategies: existing strategic decisions from you.
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
        - WarBias: 2
        - Rationale: We are pivoting from Conquest to Spaceship victory to secure a peaceful path to win the game. Our military power is heavily outmatched by Austria (60k vs 10k), and we are currently at war with several nations, causing high unhappiness (49%) and combat penalties. To survive and win, we must seek peace immediately. Adjusting our persona parameters (lowering Boldness, HostileBias, WarBias, Meanness; raising FriendlyBias, Loyalty, Forgiveness, DiplomaticBalance) will make our AI much more cooperative, eager to accept peace, and focused on maintaining loyal alliances with our friends Poland and Morocco.
        - FriendlyBias: 6
        - DeceptiveBias: 1
        - Forgiveness: 6
        - Boldness: 4
        - Loyalty: 8
        - DenounceWillingness: 5
        - VictoryCompetitiveness: 10
        - Meanness: 2
        - HostileBias: 2
        - GuardedBias: 5
        - DiplomaticBalance: 10
        - Friendliness: 6
    - #1:
      - toolName: set-relationship
      - args:
        - TargetID: 4
        - Public: 80
        - Rationale: Austria is a major military threat with 60k military power and is close to a Diplomatic Victory with 45 delegates. We are at war with them, but we cannot win a conventional war against their massive army. Setting our relationship to a friendly stance (Public 80, Private 80) will strongly encourage our tactical AI to accept or propose a peace treaty, which will save our empire from destruction, restore our happiness, and allow us to use our Great Diplomat to contest their City-State alliances.
        - Private: 80
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Public: 50
        - Rationale: Indonesia is at war with us as a vassal of The Inca. We want to establish friendly terms (Public 50, Private 50) to facilitate a peace agreement and secure our borders.
        - Private: 50
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 50
        - TargetID: 6
        - Private: 50
        - Rationale: The Huns are at war with us as a vassal of Austria. Setting our relationship to Public 50, Private 50 will facilitate a peace agreement once we make peace with Austria.
    - #4:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Science: 100
          - Defense: 70
          - Production: 90
          - Expansion: 0
          - Growth: 80
          - UseNuke: 10
          - Espionage: 70
          - Gold: 50
          - Infrastructure: 50
          - Nuke: 30
          - Happiness: 80
          - Spaceship: 100
          - Offense: 20
          - GreatPeople: 70
          - Mobilization: 40
        - GrandStrategy: Spaceship
      - rationale: We are changing our Grand Strategy to Spaceship to pursue a Science Victory. We have high science output (3342 SPT) and are already building spaceship parts. We want to maximize Science (100), Spaceship (100), Production (90), and Growth (80) to complete the spaceship quickly. We also increase Happiness (80) to fix our 49% unhappiness, and GreatPeople (70) for Scientists/Engineers. Crucially, we reduce Nuke (30) and UseNuke (10) to align with our ethical principles and avoid devastating civilian and environmental casualties, focusing instead on strong conventional defense (70) and espionage (70) to protect our tech.
    - #5:
      - toolName: set-research
      - args:
        - Technology: Robotics
        - Rationale: Robotics is the next essential technology for our Spaceship victory. It unlocks the Spaceship Factory, which will significantly accelerate the production of spaceship components in our core cities.
    - #6:
      - toolName: set-policy
      - args:
        - Policy: Iron Curtain
        - Rationale: 'Iron Curtain' (Order Level 3 Tenet) is our next policy choice. It is highly synergistic with our Spaceship victory, as it provides a +200% food/production boost from internal trade routes and free courthouses, which will massively accelerate our spaceship part production.
  - tokens:
    - inputTokens: 69995
    - reasoningTokens: 7253
    - outputTokens: 811
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Reviewing My Strategy**
            
            I'm assessing my current position on turn 438 of 500 in this Prince difficulty game on Vox_Deorum. With 17 cities and 75 techs, I'm focusing on the Order policy branch while researching Alternative Energy and planning for Robotics.
            
            **Refining Our Military Goals**
            
            I'm currently evaluating our war progress and strategic objectives. With domination in sight, I'm analyzing our war weariness and relative score against Austria, the primary target, while also keeping an eye on the Inca and Hun threats. Science victory components are progressing as planned.
            
            **Stopping Diplomatic Victory**
            
            I'm urgently assessing ways to counter Austria's imminent Diplomatic Victory. They're close to winning through city-state alliances, and the next World Congress vote is critical. I'm exploring options to disrupt their delegate count or block the "Global Hegemony" resolution.
            
            **Assessing Our Dire Situation**
            
            My immediate focus is acknowledging our current, precarious global standing. I am deeply concerned by Austria's overwhelming military superiority and our simultaneous engagement in a multi-front war against them, the Inca, and Indonesia, especially considering their recent capitulations.
            
            **Analyzing Global Alliances**
            
            I'm re-evaluating Austria's numerous ongoing conflicts. It appears they are engaged in wars with the Inca, Assyria, and Indonesia, while being denounced by Morocco and Poland, suggesting a potential weakening of their forces despite their overall strength.
            
            **Developing Nuclear Option**
            
            I am re-evaluating our conquest strategy given the vast military disparities. I've noted our significant uranium reserves and readiness to employ nuclear weapons, which presents a viable, albeit ethically complex, path to overwhelming our opponents and securing victory.
            
            **Considering Ethical Implications**
            
            I am weighing the ethical ramifications of nuclear use. While a deterrent, I'm re-evaluating our nuclear flavors to favor conventional means or pursue our strong science victory path, which is nearing completion with Apollo Program and SS Booster construction.
            
            **Prioritizing Spaceship Victory**
            
            I'm shifting my focus to a Science Victory. With Apollo already complete for key allies, I'm prioritizing spaceship part production. The "Iron Curtain" policy, once enacted, will significantly boost our internal trade route output, directly aiding this crucial objective.
            
            **Adopting Key Policies**
            
            I'm reviewing the available tenets within the Order policy branch, specifically aiming to adopt "Iron Curtain" for its production benefits. My current research focus is on "Robotics" to accelerate spaceship part construction, aligning with our Science Victory objective.
            
            **Countering Diplomatic Threat**
            
            Austria is dangerously close to a Diplomatic Victory, needing only 40 delegates in the upcoming World Congress. The "Global Hegemony" proposal is their likely path, and I'm assessing how to disrupt their delegate count before the vote in four turns.
            
            **Disrupting Diplomatic Push**
            
            I'm strategizing to prevent Austria's imminent Diplomatic Victory. Their delegate count is concerning, but I've identified a potential loophole: attacking their allied city-states. I'm also evaluating the impact of our Great Diplomat and the implications of our ongoing war on their delegate influence.
            
            **Exploring Diplomatic Levers**
            
            I'm considering how to leverage diplomatic tools to influence peace negotiations with Austria. My current assessment suggests strategically improving our relationship might sway their willingness to cease hostilities, thus potentially enabling the deployment of my Great Diplomat to disrupt their victory path.
            
            **Seeking Peace with Austria**
            
            I'm prioritizing peace with Austria. Our military is vastly outmatched, war weariness is high, and happiness is critically low. Securing a peace treaty is essential to save our empire and allow us to focus on our Science Victory.
            
            **Negotiating Peace With Enemies**
            
            I'm actively pursuing peace with both Austria and the Inca. My priority is to de-escalate conflicts, as our empire is severely strained. I'm adjusting diplomatic stances to facilitate peace treaties, hoping to end these wars and refocus on our spaceship victory.
            
            **Shifting Strategic Focus**
            
            I am re-evaluating our Grand Strategy from Conquest to Spaceship victory. Given our superior science output and ongoing spaceship part construction, this path is far more achievable than our current military engagements suggest. I'm also adjusting diplomatic standings to pave the way for necessary peace.
            
            **Adjusting Victory Priorities**
            
            I am now prioritizing a Science Victory above all else. My focus has shifted entirely to accelerating spaceship part construction and maximizing science, production, and growth outputs. I am significantly reducing offensive and nuclear flavors to align with this new, ethical strategic direction.
            
            **Adjusting Resource Allocation**
            
            I am re-prioritizing resource allocation to strongly favor Espionage and Great People generation. My focus is now on accelerating Spaceship victory components, while significantly reducing the priority for Nuke usage and Mobilization. Expansion and Happiness are also receiving increased attention to support overall empire health.
            
            **Focusing on Technologies**
            
            I'm prioritizing "Robotics" as my next research target. This choice aligns perfectly with my overarching goal of accelerating spaceship part construction for a Science Victory, and I'm ensuring it remains set.
            
            **Adopting Key Policies**
            
            My immediate goal is to adopt "Iron Curtain" as the next policy. This tenet from the Order ideology will significantly boost my internal trade route output, directly aiding spaceship part production for the Science Victory.
            
            **Analyzing Diplomatic Stance**
            
            I am examining our current diplomatic persona, noting high scores in VictoryCompetitiveness, Boldness, and HostileBias. I will need to adjust these to reflect our shift towards a peaceful Science Victory.
            
            **Shaping Diplomatic Persona**
            
            I am actively recalibrating my diplomatic persona to align with our peaceful Science Victory focus. This involves lowering aggression, increasing friendliness, and fostering loyalty with current allies.
            
            **Adjusting Diplomatic Relations**
            
            I'm now focusing on recalibrating our diplomatic relationships with other major powers. This involves setting specific public and private relationship values to encourage peace, particularly with Austria and the Huns, and maintaining strong ties with allies like Poland and Morocco.
            
            **Shifting Strategic Focus**
            
            I'm pivoting from a Conquest to a Spaceship victory. My focus is now on securing peace with Austria and the Inca to stabilize the empire, adjusting diplomatic relations to reflect this peaceful, science-focused approach.
            
            **Adjusting Diplomatic Goals**
            
            I'm recalibrating my diplomatic approach, focusing on securing peace with Austria and the Huns. My aim is to facilitate a stable environment for our science victory, shifting our persona from aggressive to cooperative to achieve these crucial alliances.
            
            **Adjusting AI Parameters**
            
            I am recalibrating the AI's core directives, prioritizing Science, Spaceship construction, Production, and Growth to accelerate our victory. I'm also adjusting Happiness, Great People generation, and conventional defense, while significantly reducing Nuke usage to align with ethical considerations.
            
            **Recalibrating AI Directives**
            
            I am now prioritizing core AI directives to accelerate our Science Victory. This involves a significant boost to Science, Production, Growth, and Spaceship construction, alongside a reduction in offensive actions and Nuke usage, reflecting our ethical shift.
            
            **Revising Victory Pursuits**
            
            I'm confirming "Spaceship" as a valid grand strategy. My focus remains on achieving a Science Victory, and I'm ensuring all AI directives align with this, prioritizing relevant technologies like "Robotics" and policies such as "Iron Curtain."
            
            **Confirming Policy Choice**
            
            I'm verifying that "Iron Curtain" is indeed the correct policy. The system confirms its availability within the Order ideology, and its acquisition is correctly slated within our current strategy, aligning with my Science Victory objectives.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: aptdhUtrlgqvLuRO
          - toolName: set-persona
          - input:
            - WarBias: 2
            - Rationale: We are pivoting from Conquest to Spaceship victory to secure a peaceful path to win the game. Our military power is heavily outmatched by Austria (60k vs 10k), and we are currently at war with several nations, causing high unhappiness (49%) and combat penalties. To survive and win, we must seek peace immediately. Adjusting our persona parameters (lowering Boldness, HostileBias, WarBias, Meanness; raising FriendlyBias, Loyalty, Forgiveness, DiplomaticBalance) will make our AI much more cooperative, eager to accept peace, and focused on maintaining loyal alliances with our friends Poland and Morocco.
            - FriendlyBias: 6
            - DeceptiveBias: 1
            - Forgiveness: 6
            - Boldness: 4
            - Loyalty: 8
            - DenounceWillingness: 5
            - VictoryCompetitiveness: 10
            - Meanness: 2
            - HostileBias: 2
            - GuardedBias: 5
            - DiplomaticBalance: 10
            - Friendliness: 6
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 2sCItIX5PlBQfZqG
          - toolName: set-relationship
          - input:
            - TargetID: 4
            - Public: 80
            - Rationale: Austria is a major military threat with 60k military power and is close to a Diplomatic Victory with 45 delegates. We are at war with them, but we cannot win a conventional war against their massive army. Setting our relationship to a friendly stance (Public 80, Private 80) will strongly encourage our tactical AI to accept or propose a peace treaty, which will save our empire from destruction, restore our happiness, and allow us to use our Great Diplomat to contest their City-State alliances.
            - Private: 80
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: FlCew0bcMeT5w8KY
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Public: 50
            - Rationale: Indonesia is at war with us as a vassal of The Inca. We want to establish friendly terms (Public 50, Private 50) to facilitate a peace agreement and secure our borders.
            - Private: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: QvC2ktmBYBht4uk9
          - toolName: set-relationship
          - input:
            - Public: 50
            - TargetID: 6
            - Private: 50
            - Rationale: The Huns are at war with us as a vassal of Austria. Setting our relationship to Public 50, Private 50 will facilitate a peace agreement once we make peace with Austria.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: v5BsQaND5gK6wBfw
          - toolName: set-flavors
          - input:
            - Flavors:
              - Science: 100
              - Defense: 70
              - Production: 90
              - Expansion: 0
              - Growth: 80
              - UseNuke: 10
              - Espionage: 70
              - Gold: 50
              - Infrastructure: 50
              - Nuke: 30
              - Happiness: 80
              - Spaceship: 100
              - Offense: 20
              - GreatPeople: 70
              - Mobilization: 40
            - Rationale: We are changing our Grand Strategy to Spaceship to pursue a Science Victory. We have high science output (3342 SPT) and are already building spaceship parts. We want to maximize Science (100), Spaceship (100), Production (90), and Growth (80) to complete the spaceship quickly. We also increase Happiness (80) to fix our 49% unhappiness, and GreatPeople (70) for Scientists/Engineers. Crucially, we reduce Nuke (30) and UseNuke (10) to align with our ethical principles and avoid devastating civilian and environmental casualties, focusing instead on strong conventional defense (70) and espionage (70) to protect our tech.
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: kEspejUOzeKgBCnp
          - toolName: set-research
          - input:
            - Technology: Robotics
            - Rationale: Robotics is the next essential technology for our Spaceship victory. It unlocks the Spaceship Factory, which will significantly accelerate the production of spaceship components in our core cities.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: S7quzpw7UF9QfaVD
          - toolName: set-policy
          - input:
            - Policy: Iron Curtain
            - Rationale: 'Iron Curtain' (Order Level 3 Tenet) is our next policy choice. It is highly synergistic with our Spaceship victory, as it provides a +200% food/production boost from internal trade routes and free courthouses, which will massively accelerate our spaceship part production.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: aptdhUtrlgqvLuRO
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a18nx2zpGQbGCg9lRlguuWut32y6aB1ZlXAgunZeoVF0V2fNfBtBTk+y/AhLrxDo26e5MgmZ7tjOkAOBH0pomSd8nSvfR35HAakUrLp9zc2383/Xf58ILtHMIZuWUIeNCNQkOm2hUF122dNOJv613jyNTiG2zHIwOGPFdKEbzYBEkIAmzGTeEoTc9cF/epybIhOrAPTADhZAH8plmVxc/Mixhy+a97QN1XaiWuk2Sd/M+BieqNxFl43jYWdPE8jvu/ytqqQ2/W2lSQeOhwJxjcBw3RG1wuYoDM8w8ysOZ97PvtuJ1yQ+HFgVXPXi37tzEHZ1rPDX8CqwAe/hQB6w89cG8/97u+OKiIqbLyiadNqzPExvLieqq8++my/T4tGiAYV8IBjl/c1LIfIOoQC0+82NMNVPUOB/ettr6vvp0Heb/u+ATxlESKL5e0ojfagIjcbBFzCo39tImALMufFN/io4Nj1yqHBRSjm9aJfDIA/ZFsvBnPqoGpwXYpnfuRDdhui67MdVhYybWkq1cNcNkgUCpkJIjlBE8lhxvMesAqZy7Ox+rtKuHAnzZWKarxwoedFJVNoiK0W4O1DiaeYP+Q7tBcjxRM8K+6MgK+rhtRhdbyc3eMkMKiRSzuahwIoOOlGVwLciTN4Zs7tmJMClpfn1kxJ0sXGwTYmDmA0n4QeECumYXXxx1WseCMc3oMWVoiXAu4yGgoyt19d43lrzg9/cbKnUohF8c9J0yV1txmbtFUEjuX+/0pET6u6CQuw9dcqiTUcOe104yBeriNNWD0vntPZzvJxjr3oIkgmFVtjJnOlFtgHiCSPAbTwEv310u4FWKSY6mZptl3POAmWk2TfyRSV1+kWzp1amwk/ifWgCrEnWxK1VCqr2ZzK49NA9xaOw1rwoqOSR9JuzrPMYMHcCHh4pPP1b6lkLDOLCGHFr9+eiJZJc17iYRuuN0Sb2cpB2uWPjlZ7RgdRhqcACcwHAqLQd6QClbE8uhUGx62bWuvoQ3s9wsAdsjVl8bOAo0bdjB8MQGTE7/YOEpB+CL2YrDQseXDGUo+Fghdeu223Y0l47HMBK/q5g+OC2SFthj6QRENRLgcoRNRAvNxR26Brf9e6dypYMePq9q0BTvCNcRo7TvBM2kSTfkGkGiEEPmjkAlJOOmme/p5FrukFSFcUNLuoIdW7OcHkqFz6Razm6caeBEHl7FkozZaqe1I7lhuE1/DdA+B/bGi5dWlr8+YSav3rulTqxBqGQq28aD1tzt9VlpsL3FdBB3seZnruOaka8+W9dbsFZUlcnl7IO7lFgzckIqVQ2unFJ5zB9KU+v7I2plf57XnYloK66EzlTc4J38Leaz8yduy2J8yUvRqdwl7JN4E6yZTVGCuOLLKjleLW5rfgq4FQpViP1aqmBZR4920Q/GaBzYj5b6vEdP9sRXXfrZq0AC/TX/tYXiMXUdLg99XarR30t0yYsnYJVDR5HjYZKAlcp8xgN/rrNiTBvzkPTnqnDRUvkYgTH7+oPcFplMwIJc9h71xcnfjVf4+tWCJqqn7ZiiBCsEjRERytQDqJ3p8CLk0Ln5yhGYqWZDQpWi8n/0P7A3TBHFNwDTA8WrfcsoabtMqjZNb5oimSZx7wTuq+27H0rg4YqJ3INcYEZfplVPn4msbwyK886CcD/vBgG+/y9KOV0gijdgQBmUPS7GjhDnaOim7pp0Z7Kcof9SBsr4CLot3uWAKDsSPd84YXmO44Mx83nBbhKpH9ti/fCKMLM7seaLKFzA+xRjHLX6fB76PwY3MycyE4Y7g7MPFmsnXAfM64rDQoj8Rb8zrUkT/BwrJKd9Jr4KqCx53Ht1h4SajqfNbdIQoJcEA8wBu5QPGcxO0ICS/okosqp8DdtBcDMyVwDR/5iulHC+DCrfFSSfrDk6iW5xirTaKp5xQogi7fU/PhU0dE7vU7mZmyMhfc7OCjP09Q+1RwOs7PQ5KsWCQ3PeLlg5QKcfS4z+lPCF+Kfr4z4nqP1aedrIGs7DVgFUk5S3FCbXXfyIp6bSB6RCou0Xj4/5VxYqVmL5jLYv+WqvtmXbj6FE/Mq+Mk+9jT4iFXCS/lufVn2A/UVuva/wP76uUn6RpehOyFiM1FBFxdo/Jb1ZwZgooq2+45/V+uhhe8gzkCtUswNdm25AYQRI/DbCQDKR9MlIDk+q8xLjXYIG3fehwkJlRzkKDeYOCanKB6iA1chYk6SCpoKdoqlK7qB+Z58TDiI+IC8xjqQjqjZhomaP3+5+X33yBn/E+c3v8lqBu8wowcjyAZW/T0Z6KS9MaQqKjPglvTJ8QbcQ/Gy5pOk0YUX0KelvNDIyhXjGvCixZ4PNa40hN1yy0sTcjhVMRj1i+Xs1g+7AmJjDB9J38wHhV9zCi7xWH1xb8SWYPviZwPvhosnm+c57r0NCTk98QkFlRQG6a0wfPHE41Alm3/mA+NbRRuU1l8XhV7JFh/FbiaiKoozsOBPvlmfRt6GPUhdCamG9t3RWPs/u6xT6NQ0MBY2WRSju151nMWY/5KRaVc9L1EX8F4o0T9hjP3p+eVG92jjNDhplhOr0lZEYvRmvcsn5ccjbRVPQ06VRj/u/accHMjr3q2KEphpRKYM/CNovbUm050HeSopmthN9tMYAQx26f9FHHoRu2BUfHqJt/+NO5m5DI2I4ti55ejb2tF7O9p6KIAXfYa4MaH21JZH4GJfvXiVCBL1BWWGecJOspT7V4XERzU4gas+TK78RciT7AXLKJ5lqwpR1v5HFd+BBBaAu/9T1Mp7UpYPohgv+0ojEfvnqeXPZbgpuWBzB2ox6+rufw9vdMtc6+JPnGgCPm3OEwjgHYcGCnYQ3+kPkY5MC7IXWynFY6z8PJ2Gl9Xf28YRayptbjLPL1xDEZGaH32JOCLXoJhNDYOq53L4ryo9AbuTjU91OYzYAEzDCcjLGwXGkgSA7mNrSNUCNtLIabVk8UqFo2O/67z5NZrVEMR4QFwExAjVonihEODbZd95lD14Tf/58LFxjoPQPbq60PRBfRuASS4JlOq7plqvhhiJpNVzjXvZwA1kzfMcpfcJ1tRfijxIE66mDjDwA5H2tswIsz7/WM6wPlCGpmypinTFf5MXreaM8tVH9pn6ptX/eCNWNkDJoBIvwFLcMqkZo/tn2Pj2WSp6i6/oRgpTzCot9bQAOs2w5rZ1vhXAjTZDKXURAOTT7ahVcLcmBvQ9AWkNi8Mi0QDV38Zfo0ADgiPvc0Te3o71dxhsBLE0D5WRRhdbFwgjJlMHazmg2MH8Z/sitYz9Ux0tyDd4H0V7qnhMt09yaBGfhOKi6Y1yfMOGXN0BnjHrXJ5L4RUSnW0aQuMxauiQiMz0o+4K5aG57YKW2IF53w7RtxdpG5EYVz02vgrnDRwIbQZZVl1IZxAyThgoVSQh9jQGVrMm5pmZXJo+VpcPIllpPMj7N5mNr7uPErE4vcj3lA+grYCL+YQ4LnJ+2TJC4D54ZAhDpq+KGMC3PUBXnuiMynGt2/O85/ucvncPucmwAP9xAX56FRaNaT95dD517Wc+q9No/QZzoztLCP4HQmMOPSP+8S88nFSJMhj8QGBtDyjPD2wH7iNp7zb/3ypehmY6nnfXCe+FryPhVg98FTcmCwS6XQcV4LsOhE+zdiSGuCa76qnZDXrUny5U92qTRxWZr3//XLz3Mab6w4OQM/k0KEz461ZoNI4XMV0Au+DSc1L4UzeBf5UH33mOlPr25w7VAcSaUUoFoSbz0AeFZ9jPNcAWODBN+07GfeSUC70eL+kvAqEuf2YxqJcZxigdfXJnXAg5chkWLU6p+0JD6Kmaj4rrZfYOYDIPuKoMZRzT9iK5mPWYbkgSEgoAo/ygCyH8EcFzjOlHBvb6QohOc6CCxbAIYzN5tGndvLblmvbViaXKKhehDFnXz2dlSdYhwMC3GT8ULOeH7jrhw6cQ637drLaSyLZRHtlXJ64Ve72D7f7w0TA9+rt9jaWeVeQUYbrh9/t300iwZlnRsK2evS+BIXcReK9MQ5SBLfSoybVxB/WgG7xMPAgW/oMKEqPuZlBXQZPWMYLP5Q6my7SqK/z8r/oRlyLJd4QxZmU+Xdg7+/6EfJHNhPHEKyQKd+hdZ4/XTpGsxywSrbYLmPlss6k3vCS3i2TMzQuOtIssPCDjDMTXiQHYpK2IvTgykrZX4Y0K8NT3IAvYK+wwHXMeyTQWlnHTpovaFXnCixTJhNac3Va0llqPp0Hli1kPn19c5ad0Z5iBDpdgERbUUuozJPoIaqpGpSLwJZvOWeHi4/Tsv2AvWn1yIC+Sg+GbYRZNfu6o2l0AmDRqrKoNGN3S3+FsAMFw9rgvnguymC8ps9cmWYag+hFiUnaqOsxXBK6uflt9Df3ZVrnwZV3vApESos+BmtsLujJenMz0HsuT+v64j1DpAg/o9H9qqMoPAQuZ+20i0rhO5GLY1KllNQTKtUj1ZHAgLkGqq5XVe2BBfZxlFvzDFuI7BcKKz6GjUVorJUCX2e2hzfjpp0kmGCX5BxgjM1xvux1bSdTajTLGZhVqbc/oSIbGqH5yd/esiUrLRgV258sQXtw4lhSNaKpCjKl4NtBkOJpDw3y7MT+hx1A/rKs4L5ZnnI926PFu8wF+M0ucd3o4fmMJhDV7FjjFybQEppwf9ruVoYh/OWBeZK5e3rMedMU+kIbFfq+330dmihwFjHDwxL78lm7s8KFD5Qq5283yBd7flTIdhE8YhT2zYMEm3yylkqNsyyU4JGtz/gfSou/a7RlGCH5btdFjDIUKjhP2eTHNMba7jpmYSOYt7Jj8Owh8gZawaJ96Ds9e1rr1BoT7JW6xh0e2ypXW6S7frqal6zyIw1myqJeexWAakcrnpAQ0DqR4PWeHuPyo2gr2AxIPsKi64Ohr6Rwox4hhmag/4xsi5JhAFVdvWXLok1thr9MGteE71gjcp4rdm6zWXi1zQaAf6WZMk7/elaAE1A8P0XXwcsK2b1eCGNn3T/niOcuERNDK5a16wMrtaxsZfk8pOGxXHt1z4gSdPrstwEfbupx97XUMeI+qNcpfMbfTRpLGI9ARvobd8eVy9E2XD1+qVBY3VogPfWaezLDQ2PzFGtm4mgJD3N3xCrPOvhEGGs1zwOJi2S7eegSf3wk5lULPE0d5hUfFx1HTef75uEpWbUQ2IV1/zy8al9I8DBeTrXnsiHRyD9wO8++NfW1WP+zxJeC+bjNmLbHlzIgsB40zx087o7H1scYDJI6Yiov7DBm1I/0ExrjBL1UsdGkDZVEpkIVI1vaE13k16rJ/6fPaa38ngM/TjdyeH8tIo+EXUWwOE0nd9cvd706iEQnhBikeJo9k1Ft6qRSr94nFAv7v2ZqT3t+4SgUQ5INh/RUpKlP5BR1WzDrz9KMeB+FyJz0wQiMPzILVl4bFYjNJjeXG+lbtnMB3Yt10IMDunEVnwuen2x2WbPZxKN5nWuvrgEzS7+pjz8BuXhkpMX8Zrj2XSgFOj7yk4NK46Br6/aM7tLuJs7m4KLFNSqAEoHr+Ilo6iVa1+/3m5UAbRJs2uSu59ynOwDWMj5y6PKidNKz02pUYVTgm7O+oVtp+s/Q8Mh+bb5oiaDWUQxARgQUWRzoAGDEQvG/cMI8vMkKHHiKks2/TVbxUaFW6ef2X74fWlu1gTIDrsUfY/kiYf8uM5xYv+K5tv3JBKkeshhTjTMiYcI6GCTgRw9boQQl71Yl7rGYAigD88Ey+Br4B3oY/Vf0FvfTdDPuV/tiyooIu6jBcPOeRyg/Om6GaInbGA8o12pgTLI4GBtv29couLuN79gmCttDGYYfpZACD2vQrJGPbWcgJGUGN0+Cbr6BYAGgqdjpFXsV5+LTw1ATPAEfqe+LYl0NJ2cuylUiRxNqRphsP9zE5MPHtqT78oxgAveFkG7IeSqbq2YV36amh+0ABre0u/7VGC0y/BtgQOINJlcx0QRm0D3GpQklCIxhpLXnSxfuLMp5dR83zMF6O/vOaiKBQJNtxgaI6PiXhbYdRKmgAzmKapjWnErmoAzzTiq8pztKS9Fo5P9ktdDOI8b0sCzPJHzVY5ciB9tZUCJLshK1tvpeAJzOhCCuVKFxCMgBJXkPPfrDbT7xycqBPl9YBh2DS5ptlvrWUcedNPB8aLuwhuckaNOYofZBwFddN3jo+w0ep40BE7i1PvexJdWyKLcYeOYfGzIf2jmO8o6QPFj3hkwma7lJEhW6KIfKyWeIm/O9vVUmyiDLfkPufZQ5SoiwobPo1LOrAbQhR7kQbaNCeHlyntnRUAX69pVGy/S+CFxnxnQM40fue2M+lxtCdJ3dnlwLPfrSSVmmS8+mJdLRho3sQtxfY1Wx5Dx4ZYWYpSy4HXeJNhdmslNyIfVXpJfqhRZZPVRfpsWnH8QEdS+ZAmkE2duie8XtdrH+gkh7PSr//DfrYcMwQLho/nHqggfszXqIl+jmp91/M56HfpMPyLT+IU0RxTBXWT8j6jE6GQJ/s+FpNcQNdB5rGSA0TLK/23jrUo8ubA2uZ0UHgVRCK+nWcNQAQyiC8wQmsRAa0jgLMWg0vAGmWIgmwwE12gTws/sxl6C58to6jGoIGHYGxKEpe8wvac74mRAUWGIMylJQ0914S4vlvfUBeNNfgstcicthxNmfjccEwKtKVv3W0IdsFztAyaR03b4op+gmwrPYzL9dRhvX3oGgKvEOPasTHgpQ4HiR8NtHhpcJ/cteLo0ggKIle0hQw7/78VvyxSKBZSPT+i2O6WWvWB+40eZQUraoUhRPo2DGSQYtR85Fc5YMai841ZIDev0sghwAYbUHwU6eLE8VwV09oUvDehONdqhx6gDFR4/1n4TYZoLE2Cz9vBG56kBJ04Ch/ODHGHLDfdlXTuzW7E9ikyXwrzG/Vj1jeLVfc1TVPMfbVHarPklNB4OJCldqpHsPoY+DAcu8pp0VnQJQMDxSmV/icqqMPiZ2/XNjR5iOdMyrMusLoxg/svMYAjqxqedR4k8pwmgSXbDmvaUOxwFcI8dn3S6PGjfrdwISQHC+c12KtlTr/WVBxsGaUEw6fbWUL7omX/KarThz68YOWMqxTMa6YldzBZmc6U2WLHY0gWPDvxs/PKejvsid77WWcxigY7HNkn9vqKsnPFkvC1aV7vEWkewjcfzz1PKv8URoycPv0p1yYHpUNrp6M9EZ1Cs7cF548A3cTwf/viQGp0QxzAkAVNVRTAxpopyU7eImp/w1/O1prReqg2YF5Bp1g/pSV0M8/8Kt+f0jpQ8e28q7opsYFTC0hOmEpohHMRI9xZe5fyuZHkokJicTeZpIrqCoKJfNyXw2lb9AQsgXnEb609bcXEMlCqfdeE41jZeLe9y4RnlRs4ePt5jdkOKw+UqyBpYxzelSEm8EFzMrSvaQuEoBgg5CPbJGNoGdnKhFuzCbNzed9FCKIQbPy2gAdjciNtPlq3kTQGrwRSDAmMv8J7Bw5BVaAZQp53OttOybK5+RfFCLHAN2/zGUj9RqQybKxNcnGqvSB4g/gzTxTUf4mGq4Kqp9/a/+4Kb4bJiirPfZW2q+QYE8U8XCiXJwVN2e1YamC8KeUjZDb8jXROZFlmC37Mv7gQlWxbS45kl0LEjzkBDRZaV3ZvhzySDZrBroMKVTZWWQ8XE9cxYJztA7NXqvluB1dCyrTbPHP1S09/JpsTViCy615xesekKGcNcnGg3EAhvTQP7oJnTNeZsdnnSbhHBKOCsZcl2LTQXYu3BvjptiSxWIt9jASINHFtTwbdLHng5vbNTEkVoyLAa5wfMVQ/rn1UqhkgiCrGaEmSeNBdR3O9sE7n/r/26yV2+iJBKQksJrfg/QIN5LKNSXn3pH08JYN4t+f49msolHQejM9zN/ByTJchObcsNVaUW3A/hRuh0oeZaEkptSmoabFCzXl0u9LwttkHmj23Gm/jTMqWZ5il4Hk+iSrbSij/wlBgrJhsa48PTSNt+vaBG0pS6VISUM64hLOxXwv06kpDIVjS5pXMq5zeKBxgoyNVH87wFxV5PIzlre2AyhXDP7e1I+k7HMwLuDc/38eUnMnzUwjG8c7E4mfHCfS+X7/15h7ijRo9kAkG6J29N74esqDkbG4DZ5A7fIko5dX0kFsOF1wtG8G/+T6+uUVAN5EjvpC94Ve/y3q+tVWs3ZATnKC/4O4ANQtvaqiT1kgSx4jjBLzNjCo9MwdE1pYdB3pF/O0dql8ZeUaZzmEGAWooy1LrLLMmOFFTTT9a7W24tqY4QGEVNVbul5UWgL8vtDOHLe76NcXy+t9XWRwX8qLg59i+Sab6ks22LheYl7ET4ekRSXo/A+5Wuek/HS4+HdExXzKwaOdiN//htwukZP4ODdTBoJsuY2j7wWor3MLpmsc+iULTkaJKzoEsV1NGPyPkwh9gUfxmab70eWUrUXXu1S26EkTJuRHFcGRwwo+nhDOJVQZc4E+mTu/JkNJJXycmjdu9LSEeV5taZ7U286ASGuq/U8Phu+zLwb+GFh9Os5NcaVIXm9+TljF1yBkLxMg2kY6T1eoLOSqKt1qVANMN/d4KmG/TNwCllKQgzcY7zVi14TZCZZIq++CsZHuyBqGqluQfrIyHiD6wJTkSbaMitA5WUyLPKD4+gQ/82gCpJALNe2o06WfJ2TO2pEbq+1yHHG1lZUWd1pPdds7iqboWoL4tCM1m5QMJLaEuClMB3uVLAtpm8tToyDsfHkWON5DCXjvR3lJCg+9EYiVS1Mk+YBJnXjHhYzU75pBgePXYt5mJqfB0s58kBTknqG8lKyLand40napNn0E2RxlgQbrIPeTL/zI/+vEekONkSm7qr6X2iVfJX+I4UKODA2nBLm6MYvaEygKUQdBJu6UVs1VjL96+NvrbOlrhwVFXT8R6eZbBDlDRo7I17wBxtvog4dPwWn/rEwers3D50r8WqT4Cd+BJB3Un4SLauhiGjozODJgL8uJJZQSQ6UQIacXm3tkqVun9lliryZZuzRilcSSdRWU3J0nPB3dDAn66QGd1YdcjoO3yeri3nMKplEDT0DX4ry/GD0OTfKOfUa7twjPkGTzwAvgCNra5Yk+JisQ17GTnKOo/0mRraykeuXg+cCraGYypmEzGll/ITYTO42e5t2BhIkFrNh93lHamzuNbdr0XBwr0tzKTwOjsu7W+fttoHxwKzgl92mOL7BTsbIWk5QIKEcxMpMrSIbPs4UlJsQJyqz+mkW/XhAv4c8L2BbVwUJtzJ4R+4p2BC8KP87dWAO4CMN3R2SMOSONy+NvMX/gGFbjbm5+3L81v/Y8WiCnJmyjN/DMrVgF6Yzsic4k5Pqh4xkQoPCCfGMKf5pg2JpZuh9xdElzYEvbfg8qm/Uyb1bE83zJKHynsPxNQZXhZD6wLOnrd4CfJNSNTjCHuzZ6XSgYbwDHgOLWeGDI4HcJm9HHdnOk6z9R+1x11RSuvk3E6l+B8bdEZtcu2rPhJAHxGktpYLh2veuEb8/JtEtZos+EIKlul43oGJcpG2g5ITjulXlP6rQq5I0UtqPfVtHPp2wlmwNr6n/6YbQZB3CXDh8bEARvo2vZPMTHM1VmZT68DQAR+zgpgYNDNaGuLYf5jdGNcuGwsjOyBujD2UKVskDX81xEr5tNcLryHDEyUudhMobSGmrStyUTzSzZU7vRCpGXb23Fa8hClbsiY9XRlSVtDESmXyW9Ne12aziG90NxtiK4nSCdHoBKtuAqA9KPObWalj7HCejdd2SmFVuzATgsd5Om2SiEiOpulgwD5BAxfObKxi0Yysf2L56QQmQdU6+IEOFUtJuUVMIynd48Lj5UlJQFaiSDeqKBDXn4dpulZ4ymqEJ/Nz+huTTKZkhCt6mDPiH6gCOv9cPVGKEvihOenUgG4mr4nA/IPYsPZTfWTZWj6gRF5M6SQUdUo3DaVS2DhkR2P5PVFbudijTfgGNjW1GV3lBMLS2z338oiPLDxhG5a+/2yRte3fGPpbA/GCK+zxbGypSy+4dRpX6UJK2KQnEaB3n+P0Ifr7JuHKgqkud/nT9EWQL5urW7b8OGoY1Lq3ZEx1fn3hk7nNRQ/ORc698bj+tuJ6RcfYvFSOp/2pfh6jhGaQTaGALKrMuANCZUTDYMQ1t5iH6boqMOrfIQURLB3Ov7TyC4FUP1r7AoYIEr7Udpsz8pNWkYksRZiKbh6fzt3bRFqwaZzA+9DAvfqbA7giFLQlvgr4BErBmQXZzxxDY0ZF0LsOzq6u445nSdkl639+ls9B7Tcw911WFZKXn+ca66EP92b6TV+YjCLSIQMJ8qN6HuoUodLsyWNrhFpdDM5SSDTOLy4La+8ikdtYTgt/T25GRlXHG7tVz+mlm5Ml+kL5SksqUY4yIqNctGhYhYPq5iyafKWElqn3LzzgEaC/As+wUnjgA2KLqeDlzQ6wjPfOpQ1NxOBcLUK1L5c9uWc4/MNpYnfowh1weSppt4pPJQDNt6FZ2HWbSQpU4Mvoi23T/09FsltVQto5znoX52hI2/1+n50Ouwdmh9/wi4duLzfgiKkloMnXTDh8Vv8c4VQ1BjccHkSoXMwJhSoWQXMhWLt/qmMgt40/pzpqSwZndx6lRrz07QS8409FLb5fpjnAfDfj+z0+vzvBXBQbSkHscfPR1LmcHcoRLD6GesekptXCVw8+vux4LwFswTYLsZkDbVT730evd+/+mStkW6Y5BQg1X7btvIvkOK643GBMaTdPyKsLfNQdSCTUHkEMDVPQCAyZOidaABRQxp07bdWDM9ODl/5vtuE2TrJMvoIjzqHURmlx8n7iMIfsdwRkNtTL2e5oSFKcj2a8zq0KYD0g5Y5QuSTqXCI77/7H9CE3KJnxPWhsYjDhbYIXlDDEtYcT0RqoRIjFpZSF0up9rrMOLpKSuim/y7Fgr3U0Y/bZTLbnsH2/zCSv4w2tMNX78eX3zM4JOM9grgI2xk6uJERJhj72oaiLSg+jfLW4GvBNN4zrWMbK4arIJwe924Ob/L6504WrgYPIRYU2gcK73HUi5LN/87svrzUjfUtNliJkCOb5XMUKQmS6Nxn2RyVaeaU+AiLHz3QC6t0jgqHey+Db6nErZ2eU92f4pbBmT090Zt6XITpKB6XTpwcBrgS0wqHMkBi4zQUKImUihpPx9ccDSoz9azyyXPcYmZbtGECdz71gkO7RYJcNPJddrTe1HaFlaGLGesP214PFU+Paxy6sB3cy126soFjYqNjpNqrGNjFeHEmmWfFkMTIEq9bIpbJ1s3dOoUNeP5y3zFDWmzIQx1d4xJtORSI7OjltAHgkzN/2XOW+nS3cIQnxRCRHIFZnZtdwnFoYlNY/6jmFExmD8GR2o30+vj6l4uyTFTuhLXg08A/qqagiqp+ngBc9LiPu+NnHnxCDJ99kBZNRQ5U4w49UdBsbkjuA+9tjZNu/L+UkvVatqBeoAPZ8IViOtzdv8dgnBx3J6qazNrQJx8TIzcV1CQeNpSXYBmuYpoHPY9vlk9hwHip3ZIFJkvwfbZe3STokdKgm2RSX2kqrWw8qX46MWM/L+Xb+mt37jDglXuCGJYiFHmt7G7tV/qMJANJR17huCPButXjs6XaH2lZltyqt1eveFIMNHKooLjCllEKTBEqINBatVhlVhyJxxBgwCW6zCUxGBlhYFTTUpvF6g6CJNw1zse3Zuq96Smq6cbtKusuuNkTcdnvVgVBtzglF8FXfK4tFDdIsHos/AkDL+/pajurN6k95tsUsw9f7//zZ0kSwiu/M+wWBQ1xidsaPewfDfgSNU7m47B3UdUDDATzWW2VaSctLsvckUN+tH2ZyU/zcM6W6geIIzJUoaUNs3ahbyCpLMkb7O9/JnauLolUdCZV4eJERYSakIN8jxts46fQ8w8w2o6xqwmdlbLNmFKIfujkNerFvIQYFMgrZZiE66VaafzL39qu457EG/xqFyzYc/BQRnNvCK0w6nGtgiI2LFKcZX55vcCQeC9RCWxo6IalDbZcfI8ZF0pdnZLWhkaeUKMzQ23cuBDlfkHGwdj75wYxaycX5dlNxGSumklcTpIniysa2v3oaCLvmBhQ93D7RRV4Tft0QeAJl7NUMHl7f8zIbhsVntt7SgfHcP6PTd5DD2aonw22mJXGnFYWVAHtNJLadjZPpP6pMm/otonuPwGSL0wZ119nDniLIPcs2RPQrwH3xsMwi12LWQjvUdXjOKKP8k5VcZ++zbLe7TR+HIzxNMknd0llNyDeiMw9QIv2QuVeNuhXRBL8PzDfSRo9Fm9fitSPLxIzk/8PchuNXBi++1XHv7sGocAgN9dSz+WOjq5qcfB/BvO+GcRh2QdwnI6/a+gih8uQ+h4OGH7UhutIliEnD7BjOSBsp9f0HcOZcfddlxpQc01o1a66ZLhxVqJ4ITke8sLlU39g2Os/VeeLNluRsWzpJA+/VPsImGSn4itqDXpfMOmkOYhnIaN+JrjjA2WeoJEj4lS8KhcGDfVmNqGHY0qS62yhmOqYZ5NMXGznw75sljJps/YXuZFwg+VG+F/etHFc6HPu5mPYxH6RPQnkmSKSoD7AhErwiGSXUS+qC3HDZ7JLwEd43MPyTRiH2UEdhBiPgRYhexlgZzRlOHcmVpTgTX5iAEv6rIJKO+AA/3qRTWPHG/9h4s/DZW0zbHmayhHQStUhzqNGj9u+WbhFANfAQfQaGADxMjQoMXagFsGlxtBlrHjv7kImT+PiGiL4YimMDsW7FEsQvYoJSoR/Z+wHLmddBXElfEn1WxlGnNrMOOsj+3JgCqBLBEuxEQ2rFGxT1/WJ1OcZ7Ze/igYi7GRDfALPBLKsSmeCcpbj1WdDYX4rODzSMaAsRu7tYqrJBN5D3AicCdU8DLzSTvAeOs/ranhhZM1fG3v/24+gyFERZ0n1FO/ZDYwURDERop7hh7opG2UjmzOeawLLrAbXNyV0lUyYn/0Q0nmNceoT61tz8ajkPdAaTqIEuf9HQDKf/mzRemYpgftqAZHVtzpy3bkgmpPBuQE8Y80T4cum4M9MZULjtelU8Gm7mb+bPwy+qI0LEbyMhGTXLYrXM1Ofm8Qi6kbOCEb9eV7/V1HXMqp1cBZrQftPZY0xvqaCofRNERL4zG9TGQxzOqou5FqVWHfv7Stk5731hhk7SOGbF6lGLW0P+MHxg3liwlk36XTMJWOZwT+yNkjLkyIN7nuxux5f+FtU2AEd3vhyqFVtUOVGNL9zszXeiH2dS4XplOv7IDUrzJ5n9WrbuAnga5pNXA3S3sDxJSaTk8OIFDuZwHUwyLRA2+KsuSJy03NOkwxmH14KqHf4akUhCWZ8+05OHvz/jpR7PYLJNE0OGIAXRjA/lPY46iyRuSvF0NvxmiaNyKU5GCN+qrTP76nrvlHBpVe54xdG6NNlfuzdfS9X6dxmRNnadJMhX++3BVSPnD4Ykt7jFBqs9vulyvaOOdZq2LpdpUfqs10xizpfVcJtLchHxeZXtiZvwAf6T/4ATHne/wOW6rdq5L5PIXdoI5EuaUB4LOla8ziiU99g4FTSaZ+EChAWle/78vZ/XEJQEBUB7epNmZUCLowUyCAd788Lua+GhSvw8k7iTaDC24L76fD4C40JWcXIA3M28KPcj9UZlVvKBNI+8zKumO7GeQPpFzuxRNFOox4YJSVHUgBMkxYl2a++DcRyRCyF/gPCshX4Wrc3+FXPZqk+vEfdGscC7P061QzSp2rSJPlayasE0GB6F/jUtCUMHYpazdIOAjI+SYrMj5ljT1pCygc9nw3/aZR5DweSdXVwp1m/9JqxLCIvY+Ub5CD4lNk2FDvJtYrRVqU+bFiVvJTamXkCPr8y8+bVtqhs4UGXbFhusiFByDPeI4KBMD0kkSvvzbsH4S4dzEx1h0pAgJfVOy8Dk2aBcpVdQzWIFL4l4XDWKmFmC7ikhMNv39eZ+qBwTlSjk89WWP3SoQVa6jwTb9v+HOwAPU6p22+Prr9JGo/vBzg3UXbEMkgmE7GoCdyQBXdiZE+Hue0ikL0QSNTM7MLao4U+GPelnC4lFRXyYc7IFM8rNp24GtFHOyALJM/RRqlcL9OdCAVrbrCXpME1FhfRXDNJPM6fe0z18QwhSlhxMp2Z9+vWO4AgVLBLZ9PKK1sDb9w6jh3zbs36UcqehitQ8KQxsaUnya6YmHvWVywAePLnBsNVuVZb65ZIklmKE3gedeVfVc7GpOa6D/DwHKhb3hCYLzWSIWSNkpnFjLAIaLjYbR3aiK5SBx0RA0pEjMMD5MyAZjNF7ky+x3KwWPJDqzfMOFd0uv562pa8N265nXmSSe/WGlmIhZLR6f0zahsBjNSbd1t0nB12HXZyhZavtCAB1Sax+cNdvNNpDNiSQa4rUyQcq6IT3iNpetdA7gWZq3YsKVmCmp5J3CHlFUFL+enTgcumbnSqsvBzo29TTQT9Guu1bhZnVt/5uWuj/LeWm8usESqqo/Jtz1RTk4JUSRKFRwSpdXtPFKuOEFYrHX1r1Rt1Mpz2PsGkdtBG38nYAg66i/iISp61zCApOvfQnjvG4VNot3az3k8EYJgOhkJAzqfloxnlzoZRBp8Ot7Wz/ZxzvIvkc+fqNqX229IGMiZ+8mOvd/GNCzT4212/XQERM9RAIZa314g3WRph0A61GZJ/wqbfio0PrgyJWKraJDprWc+Gc3fNrf1QYtih9qAABTuumks0IjCg+1wN/Bfvy3UVDi5eDjzdDJ1bEOhW/8CcTNe8fSM2s+Rn3maZ29mMpazKtK1ZuPNgp/DAF+OzHFOyFtHf8r3f9VG5ukbEgfgTHeKSQvVCi64tpwgRVO9zFPMSfh3XB0eu0MVYXTWdHi3/a8ZJyDebkA1osYckasoOSUGabFok2UhIuJTASCcXE2a8wrPeaGcYbadB0Jams/Tq9k9vMDo2wz5ftGUzW+bNUmHrUftiP3wkEuPYJkJMPcgRuTK/2PC3Lp6BJ2/sZOE2RNtzAcdXI7aKoB9yJv3eXIEU7ATyFOfvZ7xqtbcTDgOU09QRHzHNo+OvAPgJD4VQxkIw3nAzMI36/0nj2hKL6hNieC7XA+BCb8XI7fM5FSp+o/jbNjTiPpYxN+gsNDipVnNy2D6EnN1N8KSx2dUDYvpO4ypZqLhrRzFke8oSTXkB3pBHexmtiTl27eaEXEgmqi6rwsfzZJuxg934no75UWjMFiZzt05vJoV4cxXxnmkdQ7dCrwokrIcOC6+i9Rn8ci+TOCDVxIHjrcT0s0twKFudfG6AvpsGIO5UKWbINaaee/nZHLSa9rE/PTDHCtujGLe1ADguRs/HRfVS7Bs6uc1f/rMdaDI1PMdXnjEZ/l5nNESoC8sgwg1KpiITRVE0Nt/AwTv8Jh5XvHOMj6zbhaPiNm7rWuSa3RBAUgnGLBNiLtzE7PrOARfE/FiCkHaO03P3qKv9j6tPkdLoSyOT6OsIPZ/bNkqj1189lZ0VY7ylMTbwjUIi5/kmWntgzaHykODg3H1bxA2MOlYdOI0E6IdCWc2OksoKf8Wkzu/hKHuYyXeOL2UqeaBBoLpoczBnD9Dwsb0+hVdzckhYe9kc/8h7Iet4YvdENrLCVHfK7NJWryJfArSblmoZlCwNTqO/IjBYNRg58igCJi9H8gQMj1qBb0qqh0/aLmoLSoLzHj8I4aTlBMseNL/xNHzLRIzlCyZk8N/fauSV4utLkwXtwX7J/zoucwMRLr4TYYYEe6/k5AJlMlRgHUWsLAwRujyf2CxrvshsUekw9/vFEjWhvplTnI/9NWhUn87V/fMAwwrWrXPJ4KH2Si+kNSZNVrNzJ9e9zHuPmpDNcqklTQIrA9iTvseOIAS0+CZOmAbVgbdLG2j4laoQ8sLlAbG9ctXBhbfaKya9jDBly5sO2DAu6cVpQya5RB2ZobgrFHRbppq0C8dJh0Zy5+lhx0Ks/rW8NSmEu0gMH5rJlP45xm2CPFX1BL25/kiEuvP7TCczha5ubGqC5IKX05G3W9lHtMnCsn2O4H1PplfEC7oMRfX/WxZZiqNgCGKQlHxFK077BSb5A1936sfeIPjT16LM9gEooCzTtkwug47BNhzBpou2rpd86XXhswX4YKRlU0xTMvOWE+ua6XBsRIOQBrRl2GMd47s4KTPtOaexxGhwSc4A7ZB+qCr2dAMMuaX52uRKLEpJ7mMJdpwCdPK5LlmZ1CMEOyfCqbtMt0/US7cjrMG028n50Jj4RHGVJdbORnNuujG0HmkGaWrRTo4sEm3GIBFp4TLbAT6qpeo4eVPWeCb40qFtnwnsfAr7HfaRqreEpMZGSuy2+rKSQcv/9dzyz4W5zrZ4dnHKtPCA3/gvtm4pKd+Yw6YtSO8l6Ohj8VgEp66Fhmtufl28FzccaLwDZlgd13G+Jky0OPawIDKV2IaVnY91hZepizczeg0XPqiWIzBiP5vAUUdqUEBgLuZw/D7pWLUggIGLTJ4A4gEpfHQdpyVLAaO5okMxqmxM8eaaviQUD7L0TvfJEF3N29cTxMSgrp5UqDinfIVSILA01MjHRW97jLhvh1DdFIuYSuGeTv5+STuoiqPxAvkvvh91vCgHi8J6v3pPnYnnBsRN7Q1/c92Ek+YG3Dt7hPldDn8VUfQZH2I2tdY1oDIy0cmGOaneCEX4aA9oRBRaBOrm+q92s6iT6hKs7np8a/t5U5g4GsSfiUUXWnKr/9M8sb/LtvLEs4gx6kXHWB+a1tRCMfqhBOaI6wnSol0Ii1bq6bhfdNH/gOrZ/JzxJN6YP/4701a0CP9w+GZNOyFxk6PYtg8tYH25s2mOFrxr/YXp7Yhmw+4mxW/BwT4cfKVUt4unFaAiqN2zTyW3TsDTQXSAP3yLdhlo04SyD2NrmqF9CYthg5LPBaFJl6l8IuEHOhd5K8Ib1SqChg+4gaXxWKf8TW+QcUNIlYhURFef6NcEzCuIU5DKWJwmwFw4LtdwdpI0IyWvVSnRi3dWwOZJuTdQdXPqjDGprPONlbX1qKcEXj+AMLA8SqvjTlQwM8TgXHOqVXg0z+ikWOu724wqX8X0OJkyzKiW5HSyftGygSPU+a8993RXD5Klbk2XOa8txT4KSbQjOafnFhUXhR5X29pK90KXLoEJZUBmMI08dLyurkEqoNRyzq4SWOgSnkHLegQQnZXjAaHIyCM6blprVrIA+KxNJHF7g8lzPou/JLnTYAPiBnUdVkZjF3R47C2zsXpZfa1Imff4TT84rd8fJx0suhZLGRyFnR+NRWu3aSOF/lSjAmQQrArBjGSYWu2HsT0LdtP+hTWJm3E3K7e/nZ9weP7eSBbKlBdmxGHBgf60y121YonAuJ5C7pIbTZJmvIaWC2ZkkZHCvQAGtTFVof+UPyJomwCYzKH9+b4r1kigiZNfTOLFx/Bco+ffIhdrEfdP6DrEsX9UbnrP/AJsl6xRMZk64H4Uh2aTDZXZUxtbHiqpGas2LmBfJtxRCYrZaRHBCfKYG+A1lmfZqSkQ0x6KkE6cmZbqOSUmiX1/IJSpFxzsISNhnjnLHiF20LsMEcwHkOzbVtmh0AwwL16n2cEc0muk3BxaOtjAOSiRbwuIqfCoTU3naj5FdFiYiDP8mRYM83zGS94q4z9mWRBeThm5UZkmrUvrvLyPqXWDze2TxlfGbqWJjt2RpJ9Wtb+bj+5mujpliH/pPYIazoLJo9+XuEw/FK630yxCqf20Fg/23F5Z13JMtda6WMc6SujcMmEOV0TGT865M7Uu1KNeyVaaeJu0y/4ipqX7Nk0Zcn4P+OmDUAaSN2E4bP8d9na+ufB72UM3wSIxGb+2FsGpapi2v4xGhxBFnuTkcmTFi7zBqsUlU51DbAj2UwgQzETGAHa7ljYRIY3/gz+idAppJgRxVCor3hSoUcedbV3o7t6ByOGXKmgYN66w+H9/UGnFLHrY8XSk9W3ptzpuYKpgxynIm2sCvqjVV3DptAVFYomNjsv5rsFzn8G3J78JYp13MFkcJGsoVmFIowBJ4MEFcs2P2b39Zr5AznsPgcLo53SUtNUDcr6gnKdhP7TwH0b2xzsKVwWhKGA9airypWbqbUYdC8Ys7wXswxY5zlseJZgJTsZOZLT/cvr2+5mFRreRFOJhLiELRaS4jNW1c63pC7mC/Xynt6+vtn3IWalAsv0X5kCJePfs7O9xvKGfcpD9N7G1Qu4pjnfI5umyZ8Fkp4keRaplU3sBL7PC1DUmfj6OHePz9aKGPX2vTVxVImYO+JuKuW5ziUCTvcQfBd/rdCSrWQjJsNoID7ZkzOhdMIOCtf64uFyvENmXYWFfM0hv8SSDKNHKT+djGgXnMm43WtoegrSjq8DeMD2HQc1efo/Co4XHM1DJxai45w1KLqr8qF4XlIrp9HPsKmz+Ce/AERsQk+S2lchKczsqdeIfANb68hs8G7i1gJwQTg9iUhiG4dqAjnTNh7tQC1NGN3DAyMUXeJ51nSs9EXffpLxLqOyjrlSg7SfNA8F+pY3inpI+Af/n6QVtzGVLX/48iA3tf9s8q5tJCTwgEeRJgEzyrEjdJwE1V8rEYTEMioHbbrlrLpGDmwLK5Cit7Lk9FkkvR5gCpXKTCyZS3G+S95xFJ4lhUzMH6rWYSZk9IkKrQ5G7DRcaEvI3HX06E/fkkWbpAxv1xF4B8ep4VEQvCJk+b5MYeVZLGmAsOP50hVF/y1Xj56M+ecEYxP1O03Iojkz9R6pxCleK81U0RzhVzGmtye3JLE9MeV0VtLa9rT/a/2cmLb4WkhwKD5hASqMOvaqMEOeZ2qQKAxnVUZZaIyH9Vx5uNUCH4j3S8dDNu4YE/WRLV3IHqQ9V3IHyuMQQ6BDfn0Cac0IgC0hTG35ALvHmMZm676LCR+9aQapPGDDW84SbGi9UwjmEbkxxeV6MmYyVBTx7KKpfEb+GgEF7ZWUgdMe3xD+8oqIMy+/zbYxyWhGpCDYW2jVbWcaeF/SxhWcKU2QvZbVqo9fVyE3SSjqUwsBNHj3hsYUPZ7ScePSfY6D4drVHhp56Nh1jOE7BbaUhsLY7qJPVjpzisUXO8gkjL5gw2/wZJSB6BXMuv5lo4iH3KNe3dedHSXC+tWLFdFYduxuSlfYmwyTlREKKP2Cx9/XPwmsSMP0aaYFCW8JLH1dDEuvY96AZd/tdmcmaETVRAChlemAFmj0f5DiaJOJLdnuicNOAn3SV05Z1Gwelw7jPG1vu77vtaukvAGyardJPCo/ZF5xlSXpRVnKXwGMGcFfbREPEAkKyAnnpvRxwN6Aqya0DnCv8+YxwFFqVxeewEshHWQT5Q9mvtOJmAlGMS/ScWGHUCNlMP9T1h6qDEIwhbB84MhJkeSvhRt6SdQ3dFiH2xMPGUBiq12goOsgdPwG6MIM8xINrNdgxsnMIr/ZQ1PB+NwIIeP6+bCkXrBarV7UddyALw9mLqgwGgTMyvxddSXSKnQBzSuSKVR4E0JPrTV4mIzdHWtENXyReEcc77fKmHlfwHHdQyIkM7Zy0r1272SDomUTmYg1Q/hMd67qIDQAs6GLqUDAKtoYvWK7iTQ1Zqu88RV8NSQ3yVNy1jVZaIAmTukvuPmQFQ9hcdMkWlUBfZiJHfP3MpftRCnPKrS5d6JlyX9jdfYt5OUWIyn1xfGa2kl/uOZHhRmyP8/LJAnbh7gwzYN7PZVEpUVyQx5F8u4DO3uq02ZwpDiK49LZmVCZT2fQy0e1qx1U+Qrn20kStGUgl3zZmJvwYmM9QbTMFfu4/iwfvHSI/gt2cCx+vyv9844dpGxN//66VCIA1KVjOX9LIGY0WRDFjpeHTgMtYKVsDLOY6ntfBqrU4dAUeSITtZdMlmOz2OVcp1XOqGTu3tVLO3mM/ipeXd/GKVYlVRwyFairwIyTEyPwu8skjuUW1+kqwhK8u/6K8MqsDjHCuvw+f1sA1Dotu2qLiRpUX7sxm58G3Bp7XVPkIbhD2DL8NvZ3ZPtEyV1mcDhqp4CZTN/A68HxIT3ySbwc6CskZtWv8D48ZyHihKXnGzsWwIUkPOu9uXHg6MIVDItVsDZNSde6+hlToqU9ZX6vEaCBveHyCX+gM/uOnTYRUvDsRbui/Z5OaZa76n/Almp5L6SBQte4+hV7uM+W+xnxiU/M0m1Bxs1nyjllkNYgxBBaoW56B/L0by79b9c7nPWse0jtaRGXDf8W/wOe2c3oIuA9A5AShdaXL6VUElg4Y/51vy2Fy1PSH/D7ripQ8iV4+u9VuZ2eyg385WZTaL366peQW/eFFPdhd+daBJqlyVhtdpZSu+aQrznU3Rn+Q1zIf14+XuLNB00KISkt0hP3PHicq2gRk7vue7GWFeSwE1JbbHaR83rnWxpcPPW/H8U+ANTgSEwAlUF1CrFlEnPAGiFXRzPu5kgAkeqv7CX3UL4AgEB5Slg9oSfmhz10F+Cfk6DOynk/Mjd+blkYNjK0pAZuF0iuTmxQSYxxzAE/rsY82pCQFNUMCIFu0g+5r1zKYeD8ZgX8of3OHPigXeWbwTxJ+AL0b8Wbr0J9ZfbJLiQ1wVVc6/fXXh1JzYsfl629h1kcH4VYpTzW7LbfD3FmEyWfXj/SlVx3vWaULyJ4fGs/Clu/LEMRXmdp6wxXkOeKxN/VYFSzfTCR2tQ0OTcdySQVDcCDWtqL3Ad82bNKSZKK6UfFq53O7hJdVXzSOC9zLgAgRwoObyD2eLkzwkoVEqYmPlYQatD33lE6Re3rTcg3XhkdbnofYJ8WF3HbJ6h57SODjBLwD4ePo5KxH6/GRMhoXTBVH5YzCA8+d+wwM8EYvX5515D/KNYLgmxC+hh+I7xOOE/umPGOYWAQ+RafZz9+cY1XXulYmh9Y3GByUFZDs0xdh2BVQjh2EUp9wpG2tk88onNM4dmwDEPc5FI1MWY87yChHHTzh9yI8H+WXoFlWtpXupu43H0ARh1TSJDz8qGxv9vJJWNJgxwPUqQBeNgVUdGcQOe3XjInT68HoSWVasXmbvi6aFCqFcWyzvNlf4CRJD51xMGbGtnFUI1m3ECnyQYuYaLH+95+/RtxPriYO17+2R+0V0bM/UjEOfQnT1hbE2InDkasRD8CfLo0FQewu0Af5dFpLDSnpJfPIZbvzXVhEusgLhxYmYYws58VXK9lhD5lJfGqWZVZKwlFOkSNq2GZvD/7SdDC77prqA+8IGJQYsG8txFC+Vv1hZlS6r4WK1HzTlUBT4fcjU1W/Td/ob1rU/7Ch1QTOZUv6/qhugnEns2YH1Btm+f+8OGYW2NaoPW0MP/7cnCciszfXqdffW2JMLaA/mtGnWJY+vVX47lh84vu4dCU5keZBCOHweyFfcNgIwJDqZIbtaLTYBkUlg5X4YOoDK98KhZTcNBcTNSlHRZp5dmu9DuZF/ujYewrn/EC+ZZ3lN4AUVr+5qpTSY6hCDKPC4Z/fWaTN4Oky8OM2lBBzx2OSFyg7xg4yiQ5HA6a/Rat2n+tqF5ZoOKtepNU06c1d4cBkUnupJHedmPPHOsmmFV1bSHd9hMwwNMU39Tw65pekWtiVKKxc9Ukhmc06UZpTLlbjeqMKLXMLlwQFFHelU1nyC4V9Z49zKm2W3rr97s64nr+rntHjqaKOESThQB3/4kJ9Iy9+Th0qXnNLDQq8+Ao3GO1YkMKW5usytkaBeQdeX60mMPwzNkDFMZnxZIppit6SXOcsFx4N0U+hbPnfLbGirTRl6/moQm4Lj1GPCj+jtajZtIL2nQcsoSjohQw2zjrTOFjFGqVamM7Ek1vsYd2nQ1n8FyI+N2+/4mKK1xjBglo289NcARlTQqqQe/TJLWoJZUSGLBM4KKWhx90IcO4sYc3zC3nUZ23Fu38Zeq4HpvayGsnj6pt3mooTHJnCzSeeMQbye9UT3paas0SYA/Y4w9IqKor2uKNYCRmvqy9fAud9saJxHBonCe3GkrZp05IpOi38kh8jnw4Qjy0+C8kyiKsjIo3ul4bjdLrWWyzld/0y2l+ihw/2FVubHHwIuNc4BJeWu38iCkJLPpeHpr+ASjGvwydVJj/jDM+639ju32nfBzU8wz+H80yX7/Wa3MF401h0L0WmWlbX9KUAB+QBY+x2GCdyt7auWBasgOFHzHaPVb4GygHzSMj4xF1J9dkN9/VpowAI+QDr1v13lvbfSdoUXfctnZlp3FS+a40Nj6ER6QbVJovVlFDYtNe6S+6R8DHWWih1AGy19bn9zCXdGgG2nYKn/8cbyGV8IjjCsi37PPoX5oAE6ct4tTCATElScnmuvpX7Ht7zPG00WAFep8d64lJ5T+KuqCZU+fDpJPS8yot3SjdWJS7KVUebFn90v4jYUYHo06zXXI/+r99h5DsiNxlEHu3y/CVXU+tEYHDzqoGpt5cApNTZdH7C4v9eKeDYizRfkNNB0xwJ+nL8Sv3E+Wu9AuNNnuGUgfbanMdqrJfkJHxBq3HFcnn1BW72sLNMZnj5/DYAa79j4Zp/FCn4ku4AElR4+PBX87CWw0okMA/OpzqyDTrYd7f+eav3xc/JXk9e/GiBfX4T1YiJi6MRLfEqxytYQaL1UAZU4uN1FQDsd90H/kyLeabDkLhNHCaI9im/PR21WscDG8AXh29v80eZQeXhutRYZgVww+tblS1UO+8zTWQz+Kz2j5K+CyXonSZ817TTFkWB3vrHSqsXuHSlEuykd87awM6qbrQre9tCHykKI5zPLwLbDvsvOWlmRs+tYnLqNbA3KWwmuVf4WFuDmXhkNV3dwuDebQ6nNHnL206FbcK7EFhHh/A2BeEYBNVziG0/dVGW1VFN5JFshu/BOEPoJJGu/hheR/NsQPVug+CzT87JaiKiAgFQUpv+Sv36lQOiFno8EakmdG3SsnfpxX+rLl358d+mVAfsnTQhrLxGOF8u7Kmof869r2BRAQUpHI4aLm/C4CiiLH6tBUYmqc7YVwSS7D6OM+RVaAiOZPz7qr0sHTGnN84V8zTyS2rkpI80FzdIsW40vWjnjenmScmeZnBD853MgYevaAWPBWomuagjRdMF7HnqlOe8PaNNcWVXTvsVPH6eEXROslllx9h/JVjbCU58jhMo2WmvBpkjknJotwSIVYIREuV64pqMxMTORFa7dD8M7b4ebx+xnO8cppFeT0FVt/Db/zS3oUvcsXjC0kaLONdtkPqRtq15AVaNlTuKQFVV0rkACr46/tFe6tsuwaT2iUoh23k24yH3qlNHJON3Zs4CO+lt8h725R2nrzyCxTxB9f3XACyugpnDObY6iw3beahu58Ro+H3NibIy7bo+eW9gyCkw99UIJvAwaAnPUYf/Wawexf7I0pcidIAGZSt/LkQc7bYX9r1kSvIjBvpQgCZJZHfF6A6m0cH9wLCXiglGaU9No05jC1bALHpTqrFHcSQ50zshIWJcRLHIgtL+p9o1xrJSKAejyb17V9aFPgQunrDvIEIJd++IwuWP6DTaiQUIo6tMUcCykC8gzfHEIxVbrXE4eVg1j5LO7Zdte0mlyEsTLVomFgENMMN23UaO8i0l4lIjjW4e4Uwa0MqYWyoiz2+aN5iOKa2IBdrYdD6Ape6EaBE2GTE4eZ+tFGdB8OJdwP/LrCCyFbWk72DE9z8BVpcKS2/D4m+6TClWdPN7LMHynnz48veJc/XpCRXsr/+0yBvX9qcJna2l+YFB1loQKKcMV6Ii4r21v/Tf+aDD6kiJ5mtJah/rlDhis1M8c9SvkLIHZvzKYF2fUr0RuM9oerclf7eYw0Oc8uxbvu+7j/htmLBOBXSqadCfJ/kSX8Qo0VcbYVJhdAehDQ8ittcNArAbqFq7adWnpbecUj5qpLq9yiIdrTr5zGOp3qzVxNI0xTFHaVaQkt8CBo03k7Eoc8CLD0JlwW2LG3Yyeap/DcCL3ZGp+hbxJMuKp/9h+tpMujvM3yygC78IwUM3ogP/a159H0zvWEcF1boh4qyzBg+ozrXv4Q1hRpxVNgutYHI/2N1OVHHDBfGE8K2+LtRynxsoMX3IlB/iiTUSo/Sz0IxPUTEU3L3ZrPIwr0lLLEdFOnBwTp7qMNgwhoUJys2/MOMTD2IBAVn1bd2Ys+ILzJZsHBt6EkFJHVEtlyEiaIqhT6Kfp9bpQyLTsBmu0+GuOUmgfAlClN0d8NLjywl+OX17TpUI+motNAL8I+hS4y8JuUbEjzb4Dlp8O6bq3xt0hvsYrsZHrBHPMrfL9ALrm+spzhnSe89b2EdOgmq4heBstThh/6WVzWqK/i1PvdHwPwlozE6oka2UuvXf6ZoZjUTfyAjDUJpvJcAX2WiY+Bujbq6wRPAkZFhTJp4/1UOeMVZKnhzx4rwbBL4q2+y3IS4PrzWU+ttrE3paNiAiske9Bk8NcbEtk9IGAWwStBb1Qb3aqO8L7Tbe5iGr3t2hLVKvnhmcTRUppIghXq/UUmTlQMDbuXt65gOY7R23SBqkUjUXLoxrq47uzCVoNZmxAhtzNUdlC6EIoANgVkfyTxKPb1CKTZs29J+DP08URUvXSdUdKO5qlUWYNZmkpykDNT7AvHa7V/TwN3AyoKQ6viV7JIo+zQe0nV6zghNl+ctwqw5Q50VfkpTgkRXpNJa60wm0X58T7rRpyOz7g/+dEkctbqIBxB0X+I5Ol/kAVw1Q9vy0KdW2gLiZ02unld3a1bnc2/WqnCTJlmpWaBWzr5R0mV+O2baxyoj5hrYteIpashtOvpPcF5xQsSLvezS3AFHgkXAcvIaAbs8fC6Is/u0Ym7aiyKShVcpc8jcYRjcJAV4h8XXVVrY1g8OG70X5IRC437AqiUdYqC287sxYjhPZJKUmi06nZbE0Asc/wRzgXi+umNmfEfKHFp2ShgVH7RY8yI5rP734advn+gwYMSJ45C7WK8uEl5oMPH1NF5sQXO4EkzCslV/yNYYrr+TFBuzfuYZwKaWUdNDr0HGj7zbob7NodaAlHkMf8X3ajXM6chGLWBE7Hq6/5Cop6/RvnNe93nMldB5oSBypHA2DeUrPqqNkZt3B+5a8JzJ2YJv37zrYYGJcsSI0NSxGraGFqRfVZ7YXfWSu23MOkJrUKBabunjyDeohCSgbZyrFemMzH5own1qC2xsx5ObSZMHP3NpHuM+FH8zeMV1pKaQSxqQ6jRj5nL3rVSxM3itOAmAGq3QmtTwtVa3MlbuKl0DqL52r/8f8GDUOMmUgYcsmJDGx5df+Y/W7M7HySH6mrwXfLPabdHW6fldVldpTkA6haUwhVCkamABcLXy+xrRq8G67m1ASSR4p/NXEM0nOHYS1gN1o/hoUhhrj4rpyu4MMy5z/3he6tc9WmnYKNhn2CFKQsjUzWb7LTF2joz/hulNqzGgG+qBBcxld0zt4YhFOnzsRdIBsQjtTj2y007qWJgtV0laBZj8wtLGqwfTlM8IrRSyYLApmNICS2JY9ra7MK3g7s5iYc8hQtPs/LVsXwRZAQ9wf8mWHB2fpgy/nAZWNreMZToFijYhPpn2zb48gdmKUc72gnIjFSBLJxo+pa5CwtDGDBxKguuvcGZ6hG6lns/v6qwTVzdirfxLYnPCzRQsDDbCVI8oWBk0zLc3AeN5o1NBFUHYMRh4Laq3iPs5uhPp12LPnGS09BBVNipCL1Z5KaUh1u6IY2sr9XtIELXX5jEORpSvzKBDfIMPEU+b7U3ZYPqUimDEzar1pDedaLSfQXVPWV945DSa5uWRZWtBPYVUf8tCOFZajZo3zqV6omSifSj7O3lxtBnzTFV9VNUkdVHSFBt5fsAWIUqgr1N7QOIFfQItL4hElVewh0yzdGzcG+jUsUrKxlRMeuusvvbBj0cdss61zMrq9Gd19Bjazvaumyf+2UkbGzLLiVdBVn0b8gVmffMK9oJqx80LPb1x/eEen0X2j6qWX/USUcT8+fjzafudOUhERrKcIwlE0r5z78jIq866r6vvUhb0KE4OcfjvB9ByFNwxDSshznDYa6pMMmhSkbetFGhW/OkBjnReHWbx+U+zL35bxBPBJfx9UJPgFaXOCbE/6WqYCVAuWRrl2BiPYFQ6FvPf5mNBnmlP7h/l6vZcDJq/slYzgAZkICcOm/d71viBJg/aC7/S1ClOr5Uyhfg1JNc6MLVmd22JQCdeShZMdYaQuyCby8ko63JXSnF7EmByh4w+G/AozgJgkCU+gYXydgXaUKHvLV7rCTKVaWKhbzmqdKK0ZRGNue/VREZFvcQTz68mJkJhuPkwI9yLQIcTHFkrEsWKPXZn26zLnlRpUZ+15pvg/F283lcWJ9iluv84qH/fgQRwFRS6yAazYSpwyaxa3Wz4epRUYKNrJnQqbkKg+HHhkcJdQoOyb++91xtVlFAl+t6oSglyUmpKmXuY1LuTeNErcPIlTwkzO3yegHXOfByKTL8sKz/Y7nZz0w/PFUQhPcI1JICDiELHWnWwx/zynO+L5iseE2sdU1E99jnVZKoGNSMjbKbO04fDKaDfnWnH+Syhj22wteoU/U9k2vX4f5Jw4iJEqBl6tLAUokFOWN5ZDuQj2nynvvC7Veu1MEC65WsiCTr6BIxYm27XIz2uD2ZKEaS7r3ereyVT/acjIdE0cBYQUph26VGkfUj+VzTIy9kvqhRqaRUD4MA7RXZ1u7nKmOuqOQ1PN9VVCt7qEiDnNHer2vcmDYHt9+m19XEIW2A0VFzc9iW/6B4oLPKkbs23pm0rk52bPf7p0K2POf9Sjdx9g92Wtk1xBWQUz2WbGW6dbJQVQafn9y7VCSs+rnNZWFyiwMeChVKnUFsGAw1DIa4cCqeWyEKi/YSdK27upWr8qtw1nprvU+OOvKCjEC2bSUWWVHQjYXRie7/eRqenQkJ4tnh7uh0/KZPTAcN2er07GFmT0t7VnsodBEWIEOYG3JXRjRr0mcEETe5VCQ4MP7BQBnebtk7FFVMMGp5ODaAPn3cklauECLZCqSRX9HjQYmCsTBXO+whDIvLMlODiwNZf+eMpVTTwqILHIhWLXjy8x9PdLk7rzrtGDiXaOfz8zKfz5oCtx2k4GqOIaL1kr5re42ke/dk66dzhcFUgTyhH8achvL8BIMLZDCNJ0HZyRb6LMRia+Q0RoWlEl8JICYD6nlAJKCvScVMBcqSnhfUMtdQqaDiYG8LA6HgCNhILkYCSo3ErSjc+U8Fg0rgPYhnmIlDhTEC/c/p4VSzHEUuOtg+5LDr3T53ZEQLuFeMuZmDUbpFV/OFt0h9HcAD+TnO8Ik+p11Wf1VUzt0zJNjufxSN78Bdj7kBsoPtupck4jaOy2y6b2kDgbB7YMFJ4xhVC7EidcdB5XtG+L/rGH0EngO20F/oleAErcF/GFtIFTkP8rfsvYXMfsmZ3esZS5ZYUR3n+ZSXraek7EpAdNkUA9HQLpd2NIlRqcutN6oaG/hxb72ck8kQcVIOnPr4pTunorml6XzeY5ivuUCDL4wjXDTGOO5DNY1GoAYBv+bsrcDJzqzcECnYfKBsch79DSTMzhQBXgfMyR9N2etxyXaI2mfCLMD87tTfnAtJVzhyj4Qy2TnFkuJ/ABtmPalABKq1C8U/wIeQIu2BzgBVjvuZE0PRy9kdacT6LEWsvyFt/d7jfuQOTxNT3qUwE8uhroYmrkA1IXzX1R9Lr4vwnggOEFtIRwcLX47QLON+MRA3fER5hXbeFuXwODe6cdMXjyM33pZ88inllWlq6GLiwR63yvUSwVJFvZN/yBRTppkMRDkS4fVvwl/0ST5DRNus5kt5Bnuj7tlCynJy6DzA4DZ6/eFXF+lzEue/Y8w5OlOXt4quszthTqy1UACknRtWxhwcw9oljj6Hp7HQdsR4XgPCwtjhiZpGJunDL7UwlKDPIZ2cRkvrje3nWEm+IeJU3IniKDL2nldctXH3ZvLizffTHgu8SQqjPHwt+OolACHJNSeotUCKKxLX0QBKARsEBxrWR7nijMf0xJZ/bX6y4TKFSv1eN7H2tsw/qiLYAaiNpHN7VnUTPqvzpBxRSZ0cyfOlsaVg/iWtctY1qcKeoiJi3YOsyc1/5/7x8X2Rz2pVlvYMKwyp59aEu7b9SH0WtcKEYLWzRra3Q/twxp1OVlScUOjcAUtIf6dD/b1BTr9ZbrKiCKlwaYaIenveXUI03K2zpeJ58UtHbjF/5+kaYsc/5hKO/tbzr2SuqWsIC4uK0j2hlf+bf3X6PWXfwQFIY44CN9gm1lY1iihIvBa8vpZQ7aUelIdEk6O0l/DsvovxEB/iEFKvTXTpaUDsac7qyvNfz86+fR7lOIReTKrEJa5gzy/W0JkA0gAX04kr6DbuseG113oZg401tR+ta2YZcf1nVEfXIAohpeJ9M9xffGyAe1MB9v/3u8uiYJcuavWuMhh77W2lxtLWaRs/3I2wDhV6CdoYooj2FAuhlC6JlHKpIzh2eHN5XbANsn9BbApzMbLXqa7AAA/AtX5zIa/ScAJDeCenBck/OXRRZTbPKrLNThn+R+XndIaY4zAYMayToXFaCVkmyppWyMjVE/wqP5BercCwZ+Gkfpeo4yFNsbCrR/L3Ilto4mair36VQW/s6hInHva4Riz/eF07chyM6emTmBfSwWSNoA8bdLjA2lIQAbX9Sq/g/WTWkJvcw7M5ngj1TOvEnr+5Ba4c1E4TnlVOnJqXlJJ6yzZT5rz1OTQqiY5zBzk74pZATAMovN4DxAaW4AvgFD4k/kf4RuEKIw+NL010DNhAW0jVjTgKrC+DNxekY6SW00eTO4ovDlh8Ncszer6To6ujsIQ5YdCO/sjCdsdcz6FGKatrLeI+91kUWEdvOYbWfo+qo3y/jqQrFGNmK3q/QvZx225B694oi/e3YrnKrhSYJpATy5wqPh/W/CGjdjv+OrzsiakeDzFCZoKaDisCzrdvxdtK37iJNga/U5Bhg7gaWso1AFnfQID/iG8jm5wVnMYrpy78MuCCEKc+V4A0IXz08ZHmz9zObUURs7n96gm+o05aBMc5gD4jHKtKqyXdj8FOcj+0jjR4yYKgrCe5EQBmONcA/pEZxefwErg7iZF6tzWQhNgjlFHYVCDPz4ZX4D+hjDv+eiSBGP43Yz1JEv/SpCZhG7f2lKvssb4UPxZnNXAETDYu2xTPwqiYQ5Huxfvinsz+g8KopyCf9M1aU4vmEJnQBeNPR+bQHvb1ja5NVMlrGapJD3k6hjDw9y7JWvUu48ODRkXx6Wgg4LSnCtZnx9ze+Kgxq5tiDo+CdfDLdZzZXTfyOMYPsmNv7c5uU0Ttxm26hOf1L9f0SFzyo5pLLa/+oi9PopcZhDHKdI2Fn0A21L0SB3rLpftgBRpEsbfPGiLEts03RNhv5iqOGoW09Ujv9zA2+JczauDfvBM5Ex64F8OafDc1A5AesaJVd3BTkoaA/rItxz80OZNFaUixi6PiL5OXlOg78TJTwa247ojXtBaDD7HS0gzd2o9Ph3lkM8/FzHyfHEQoEohHb0te4B1ojTDyP0mOhYp8tMw4fsGd2fXzKLt9+82/eq9bKEyjRmY+vtUTaUm/fCR19Nf+ULW7x53bgLV4hyIEMXOMI33/2juFMdk0LQI+8kE9BPYTE5NOkEoESfsje7i41G8Boe3wMieoPI9exIctwQHhKEc1FNoIps0wrDm+vZt+N0fxJTVTBMQw++gqLrN9aDdCEStyQKCE6g0qLGrX7M3SJHSuNYqz032SzfIo8WnCOkp+/EutQRzDuFD3rbIxDplyCIbJFPDW/oON8RQoAR2HitrLZfeTlIUBDnCTgGZYbhvWlTpQ32ps8GJe/CzaIh+kGBHi+m8JyVuiihqYKHhk9wTUC78gkQwLyJFjq5yD7IpJIgRpr6igWiOef6fXjGP2Chn4216IPnRZN/Up5yiXT/eeGnYvG/VGNqB0AuCxGJGdui+vhob9kGx2Z1zi1pzQVxW6IqqtwbTW/msBScSlGNHSd1HDtQkTN6yjktEuR6mkKD8fv0qlphvR/fhr9KL9JJVGMuPZYPCv+MiRs23C7I0gp2mAevamNy4Qj1Vo2nQbB4roX6az7c4CgLCORIedYzEqL1EdMep3Xu0wNOTSr2YFzLLnFVEigt20e1Mcj9I+J9KDDPNZC32Vbu0ZqeeiyrcTud3Vh2a++gVdFdpjJOTETRfGP56dwJK9REcfzJZio11dtvTh6yZmbTLbX/81E28oI9TRn3GnEOcQfBECMO2HnpjQ1ofPm0ewL2r+DtZu5/PUGVqKnf4zRWpjHHEuISoRWPXO3N2Op0KZ14aDM8hkegZoixGZSdzmk3OTTPxbki+CtHYeQkc+OWuJvyif/2Oej7frCESHp+G/uYXHk/IEqFlHIWXyhEORvkxaVpYKDqI8Et1d5Sn/TLyQNDwwqx0hFoqim6aeUkrWvzQ0gOWZZvj6BjgjO6cbVHNR7TXYxhiV/Wpyuy7svQiNu0vnUm7JSmmOU7DRJu6hYAu3gkoEDu1h80pNSnmueqGM+15vZM0j7s8He1KHzitKD0vuWUbudncDSdOhw2w1P5F9wYNhRgHV/yqw6e8ivYWCF4PrTnkS32WRaw6M3dDU3SfJkNwUzFz4vZ9LGZyMrSmNA4BZCMq3fp99xaIAuQcQlPGph9rU+BfJRsgIWet0ueLomvqMUtqywGh/9BlRW+czZKrswEhd5VIYacCbSriUSVloBLA1i/bo+mEgMwjrcaWFzvpFnPBlHYwG7URr71EaRbfQ8d+wAwDKvflQjiyvJgsuhNt6dvfiyu5uH6AEkp583tZQqUcR4k/fGuFrG+ERwc1o3GyS+l1cT+fILJgNObH9G7ecIv+fUZcNHv0y4A7AMTgm6Ls3QpZpd/lXKN9mfB3MpBvFSvSveU0hb4SQ0nvPpcMRUpFAYWMbpX7w0/cQ02G0amkCMZHNFRl72sMURP74DH5i6MNS2Ytz2p+PAAZjy56qykKhdMh+ElunFhwOieFm8hUteenrlcE2slI2LVAgOKKafy+vNplGJtR3/Xbz5BFhUjP7C1vFo9gaYF0ZcRUgZTXznp6XiySb56kCyswIlPMW4vQfpbQqfH+VxmSd2koPanYElUx3Uh4R64cyvhnqsH2ceRlUIk/sPAgm//9HGXOmbICaT+zuw+uxFlLA8BZFTo1LZqNWOqn6jANIgaRsQnXD5e9jzrUJvQ5YSlJbdnSqCCgc+Vcy80y/0JX7sBBuChClW5O1CGQm1ViMW5qWsMZCpntuXnvT5tpwpENfOcwVkuP/vocq1eKCXGjKBQOowC98UqymTS1IjRl4vHQR6CLeL/i+3/AP7aeRLoczdeCmiKbhja+nXzADWRrhOgvo/GltZnmRQc37TDf3xsAWWfLOI+04yKIF4mSvtTRA5FnVtTjKf4hdu7TRAcQ7rGYEhnz+aHnExexiqb421B0tZoltWudV2i/bv2LCGgayzUwvhFggDyrcOsY8aioQ1PsLnm6SDILI43nmjIASfzM7F8SzYCLgyRyHtq89E/XtVIJId5eRQtF718HTBVWcqUWT06rf4KTm6WBWP7sXDtmGhz9b6aid7SEbrFDFyx8iagZdxjlP5dsJbEnt9VwaEaxSpro/jjbJcYt3VRqBE+nHIIrRUxCrb8iO8gXmDl6U9oYdrMbT6Kj4ZPpgfKvvOZzNF6+LLj7dESL8MZzZ8sD0ZxsWVIz253XjvM1N1OsJ4wS2di4mAlIV8y/cY8JRmRRT4Bgm6vL4/eymhJAEC7S4O8JQgXvr9dHE3dZ4pa0Ne2t67BuAYvRqjf3f0Yf11/STotS3dJwfYqK7v20OBAW2FkZAAbv8igKZlQjBi1EaBEjiylWeHP4jUsaoG01HgJDMvDxCMVqNgGMQi5mLpmahZ9EtSYUoz5dQP/71dq7JqrpWZaQODWkWaSgtZOi/nJLfu+LoagVRc4yEDjrSKip8lDAp3K2uPmPf554WKEYXxNfqJ9PCaHYUwVgVJ7UY+yP29u9TpUQSc93qfBWnl1nDzcJCrzJVVDbs48NWpFO9fwrZ6Fk96XVJzHAaweZ7DpLCFuYuxv1Iu+9BpHL5lnrs/EdaTUMzFBOUqr+u1JbmKWphQvhAAXwnNbyqCvZpGqiwtHECY5y5oGu4+5v4YD0xTNoidGxpJ4IloCaf+TdV5y5/kegHmyXFfN57OGOZTmTXOW5FXKDbMsLdJ82ZMVTopPOLSiTKWRtfc9FxbTg4cGaqhD0AaMnmu40u44yYiBWafn3WR0vfVksogm8bnGBLPoA/8pAjDtV/B0r1MgnszyFYZrxzL0C8V11nieT6wLAf/wBcUzHveXaEDNYXs2+FONOzt3k4fU2VmoFAn1hOu4nsK5NKKrJm/LayTRfsb/jhzFF9HAkOV3lFNYkSykHCd8ncpLvFITvh41tZbnFZYPW9xf89pKkaqzP8K3P3DR8T2e1H1wIGrx+wR+7WUYgxa8sQczjH6ibJalEzX7VAPf34jStYTDOFTnG8itFBMnlq6fewV+XMecY1Uii59uly/tBp2gvDM2Bz0tulpJBDGCGCG+x0ZMzPA8r82yO/+YcTJ2guFQOEN/2kjAKuKjvtgqVwRcfDot+B3UZVgz0XYdNuqR/9jGfCLeHDg7BNT+MTtyVYQC+smFsWXuJOR3NlMtlVhefz8ZzmrY1LwPkH1Dqykmv9aRW1E7TxkYzSWvw2ol2G0bIRU7FPHs99cPREvwzn3ATnq9H0gDcrwFxRrvRJRxSm56ztUeobDZzelKqMUbPE9AXPj5yXXk3g8eedAl1vUb/qhYrojHRQQBY5+Q0d7TF8g4ZHPus8jng+HekBN4NvdOPWF5toryMkw+IS3QMal18WsySMetMIvJV1HOSmqzDGHCXE6E27NmMUGnPfwHwhOP9VvkqvGh2wdX7+VOFc5OWph9REJopdXvfJ55lq4n7Q4dh9d+DVLPwes/ot+7vvEB79RIgrEnnjpnKWBau+8Iaxf/M6y7moOgdLMidk/kUvGz9j3qUuqdqkTTfH4i4lzjculYWDnBJWR/BsAwnDP/BQnfQDZ3UiLWqWRL5FmA9R036GyUZ3Xq1Ui/0hhjx9KnCD4TDCL3UHr12dFv85eADUTsG2t+KS+OmSu54ODibLvtGLq3g8Q9y5XSpvMRfQxGwoX9Cmk66ZI3wW/Frh0t7VMNq2oi/XfevAtJe02QAC4+2gkMQDN1Mo80MNHM9s32Ko4e1iphPuIY2qk+v/ktPDBl4xH/J8PQUuZJ0LqimyrKw+3bB0poZAf7WHNKfmjquOZDMbDyh8l+OfU/bBma/SZKUHfoV4CBn8uqi94y4WMQ8809iqB7HAoxY3AeR05/zCFSv74Os4ADR24E0Bvecu8Jf7iyk7f/FwvryxeRVTkkhilvWjEveqXjg2Aw7j6OzFgNntelx1xFw+IXqOfYRU6DmN4JGju5cpneys3PLygI2h+0PE2zIgs3M8vlrktLu0956hV7iuyJ0nNrE+HF7lHYUG88OrsDllPXyG+rUCqRea1af+d0oKZiuzEKpfdEw1mId2tpdF1hBkQ8D/M9zshjPDXqLfVeaUOxmNvAY6vNmDWiYDcCfZ9cUBnyAE1ppORcuoPWPPR0zWxVbXdVglo+lXvahbTIANcstC32MeQQQCdfmnoWQWHV2EB3mQ1qZIgrynxQGvYD7ZN8wSmWgJR/3mHLdEOl0jult30vn9h7r5CpSmzYbd599xVYeRFdT9hKQnCAZPZsyaW6rA0GkndEWdDqNfgxLJ/cGRoJb+TQ6LdizYfV/DkZiWf4OPd6iibfDaQEZGEwHXZ6YegV4aYv2j4CfOP5UeAxoUVWOhekqytQ9GTc7W/H/3IMGuNG5sWNs1sAc+kS1F4mlxcSjeMAO1oYpDPk8Sd3QtwNavesIa0mBkvxRKi5h5ouO9hWVrypRt+V/7tZCJCKJpKrXcvOvS48EtNhPvka7B+Vbv6K3JcVYFdM+OmOgy1U/WnBfeHLDY6mTsFdxvzei9L3OemhDBgIJnQIwa/M2xTJte/MFyJPm9BYsqvBfl5N4FIANqscIkQY8kG+AhadbU2M0Se4/C5O3xrMYh1xBy1QcYZaXAikH8O1xBs4U2N7RBEFe+5JgkZsF/MtvAVnM9nOoAR7tqccwMG30eeXyQkeAjgZld2t6m8T4OclfaEyrqjmny5cLSVswPvy389F99L2TtWt74Wa6D4im0wtzq1xagPw5GIyOAZR3g1MTiAfapCes8O94l7BEwnv1If9ZeJ+KaDYAIZvGG6EeFDj1wep93DwNVkT8p5FPW6sMUMb6nJlFer9x95GKVF1stVpyrdZTp7STZDzDBuB9bkgUROYM0e2RbbdJr3X6oXJwiirTzbYrJ7LqyI2Bh08iAZBFHBUrRxj9EDQDvt5HZGX7o36wmaK+RMJEkzAnJ3ZPZ5atpi4cHkJkUjXFctTuy07Zym5nwQUtUQ7rYvO4TIO8lQu4u6Ye2SgMN3n5Df86MHwAp3WzDucHxI1BF7OOncPCTCMStWl3QjBZ4ecEIKfohodJLtB4d7amkc7VBC2lFZ+Z1Bk469ovxXUORZazynKkUobp2PdnZAb6yNnPIVqLXapOi81cnGejc3LkKVw5F3T9wVPRDMnzrFkxNq03uzxReGQ/qsIiovvUaToDJnwOiAs9Ip8NQq1SLR3GepcgUFhJ7k95rDBNKW/DZgZTWGvfa7IesGHKmqkApJhgvDsoZOwMDAxTobAPeaK/Qh0fWS8ZRlQocynf5HX+XXrZ6k2pawfps8DVHb+pJyAEls3PwA8o1ETA0mHC9iMH8GBlX6IRMc/gIVip6jmnSJyQnjSInox/MZnrpQ5fgnwGsi6dc64hKDjGv31yhQ40iQM55xpkC1XahRskpA1ZijNVp+SP0SHpII6io9epXYuSPC/4VlrNGPwlzSTCRo357Liuq+zDRgAz3R9DOJtuRIP27TTp77F5X2nyBzRp4CuOkgjZPvzKvLoTp6nx/FpWz1olxq3KZGCq7Msuhv1Bilo99z+9ZlusbaOFYWXrV7XHJQjYMNQA/2q6Y1ThLnZNzWJhhbG7P4m3sW6T7IQe5d6Wv3A+m3ex2XuiJoU3c7JCODsdQMP6sbhPRfWum8c6K5k/BNWJRB5XBf+E2doFnpGixDW9Wdk+EkB9Y+zpuFHhXU6IYgrEbfqTZr1j3CDhfut6nyoZu0Fir6k4FTppewEMP0frdMv95ZgQnRsRT38ABx2EwcXzPkv0RbiFekA2o7qOf8qXaXECVRBQ7FRrPxw5ldj+hrjYEov1pbnsqhfAbwy/whkiRTc45w+iPugBHWIJhnq8NgO2dE6Bdt8LdbIctNip4b4O7pNSCcwa+GLj3AiuQ1Cvu34ZmEaif9u+WcID18qhCw9T7NVcxNnDUs0bgBG+5E/BjvZwJccV+S3OhY5LvNqQB5UEvD1h5skhVC5VLpLjfDsTmwl/vgWvXtP52XCpwmyZFyoJirthZvleN8FGz6HcIGwapCJuzx3zvkufHUjt7XJ0lDC8HleI8eGJ8uTkEDrGBeyYfPG9LDvohmx3bagUhQnJce9IEBiXwsHdvW+Wd0ySyZ214QbhO9+DfmEuOoW7B4ZSRIGLtsh96zTgFWXeb15mbwQOiJ0xqPN4RkiAyVltTL8UjirHP9c7ARAHfiMAlC2A+USwd6PAs9en1Wr8lR42W3V4OO4A1OVDZ0jeNoyvltE4OpxJQsUF3z2UAczTcNAXtwFEzD3vn7OfTPuWMHG6LUAVnve9J/w2//GSoMhez/s99lftQUILImRBzLIKc8SFS991SiSxIoMpW39+5SvU+/FsYjKOzMUHolFzdEVXPCq3i0GRkBbKkpMBQs7YemvKY6f89FiOJkcraY6Zs/yWZ8oPKQ93t3H8Z8B/Nfq6Af7DKJhgfBAQNv0TRJ03bzofSALcZsEIHM2OKBrjkQNbApC2ETQe7EbGv1a1ZCtVzSonKAL9S1LBGcn4bhWLC3xY3Fq2hK/3si/nQUA5q6aXG05wv274gIAijPfdMoCoQPdGLKtwFqplw4l7wru/mQkNAbnLJoaICTTSfLMj8Df/7Wrd7dKhXE8GZ6fqlzfR0vjtClDnGEFhbup8F9+pN2O/siEPNn9em4bt2ckyT2eJnU9WYSsbikoXGg+XGTP4ygXiiD1A6iRyRiWHY6r/0zzRo2KgnriMv28KeDynFexNIPsct+3pcISeaD5sGsxKqbNqtlAyuIOE0H3pQnSI9TwKN36bOaSaTlKSU6mM/hOfiUDupST9n8hJNMZE6+ws6AhjYSWQD1YVF8I+vu0D6ZTyUr/krA5Yky5U1IQCd+UFPBVxxIlUbY+D4zRNMDLfPDdn/04SukgD+Sv3Mtz/soTiqFpdtc5+4ofceZbmXaBIcBn6/T8FK5CM14WG9KNS73S5lr4aw9OeFsprMq1bXHcRPsLJAauRFrADN8GHVba6sbn54a3guQxZ5AhmltYHiowY8jeH6wDcdWTnyyiZRKFpamUfUwUIq7vCkTyR9vVQgFsj+9dnAOhel+1MiX0fGTEocX5KVLpE3AE0PNXNFRe1K7L3WRnHJWepGepQQFN02PP1YEKG4RSHdfuOuH8xCH2X5k+FeDlm6FIaVsg8pwzFUj/E3vq606O5GcNElx/xyFiYbtw0oauGPVIuvRUCPu1YfreVNFT6eImGucKLDjlGDC+gLeFg2j8fMPp8ncfrMmpyiFUvUNuUdy1V+TabHrIT0+jJuNXSgmvtVOi496jpgdD0k6jMIMaY3qPRDbmFUcx0/521VnWbaJtrv0XRaBNZJx/5P5K2zZLM8xPFELGsYdQUHCdXcL4qXpuTOP+CG0THt1AyjNGrMc1JLsBRuxQXyoPtLQfTI+GxYJ+7p+o68qweHePw1J0TS/BfeAEZrQ49cxWSeTg0GSEXUigC7b+QG6kBhzc1GS3txuy1KqDngaUPRBUye28tn0/Tjoaca5i7EQBWTcTE/DtEyAnfyiY3ap0KhowCUtW8OSRF5n/qALFsbbQ3lwLsL8sOX/XbjssdG3b9sDjrugt8We72OAsPVb0G/ywrD/RDuLDflbVMXjmpggTIiwRukdgDzJu1PBUhES/stQRwTfnA8ISfCO6MmrqFqRhJf/YkzT4kQjvgbmdcsDOotW5nFZq9Y3nxcmjr5qEM6JU5MCbC49EdN4LbdxqFPF3QyL1aqUri4bgGK/7usDWXtDJuLc0beYjfph5w934J88rM46K01aN+yVbttp28ZKahRZXN02LJ7KBxrPWzNNIYhiScTqFey+aO1a68ZQXqrUKnZvCAUii5YiEwypCuZU41vnxsCkSS3MDJEiQcifgvpYgyMbM2zdqkzD4ntFE0YUY1138MEnR3JHqf3zlG1D1TV6ppnnd8upWJsz5qgrrN023+15Z8aS6p7tUr9mjCEaer680SowOfgP6YPfJ20vOV/kVXPGzd2kOAMBuaIizIUH6o5EBCH4dUcQmkL2Mapwhaoo5M9eiE/eVQ0I2Ki6BR6e4D9rocsPlegfAQPI4a29ohC0cI8k6HLKJSFs/6YXq0HaVWBP7LQS+wk6bSu7xXwV/98MilqS8HT3+Ro4tBMgtOQe4GLI6TADJAp3ZEuYCdiarE8dli4BHmPS+duAdBbzzModZNXFKYRoM+mxlN4FJtQv7WJNj/c7FJJxr00AC55tqbwxQ0IWmoi2nG1shzj7nOJQ4X8MUKITFdBtT5ID2h2tOmEiaDWzLP2kRFMriFdEyuYMMBonI8hNC5CKsfWDTwtAY8OGSxyFeDOPZg5T9tqiCW7uU+Rwg1XwuQ95WfmFkZ/TVpfUN4vO8g2P+KMO6dr/tEi6Vh9+eHIFWFXC6iE0GgtCg8Q44xEG83m1OcMYz5I1buue27SIKNWc6gGjfFKPNmrdLn9vabr+jZ/XjkS2TtvCg+eg4gb+9ATjVc3EYUvA4rdNykBByI4ZWy4ucfHZo6wAfTqJhvaTf/l2PG5vatkFbFSDCx/0MglxUg/XSNGHD9OJIzYMzpgGgbBPMC5gEwZ0Q2K3+6z7S8UOzL428Jl4Hb8Xbwr52DB684zHRuDMMxGqgustT8LE/j51CMQgohFjubZcS+eG/CU5LWunyixSwLsRbV0B7Ynb6fmxjNikWZymGcJ6TdO3T4PgUNbyCJ34D9kExBc23TlbaYScUSE6ozSCBVLHTHwZHDGoJ8NUmiiSyWf3bYCEjGPstdOt1fUitSkc9iUA5P2G/XG0bOmgzjvh8j66c5EViyXvKcq4YqaqRqTuyEw84K8vXviT3Ak9nVo1qcDRTKg/Iu9rTb4SroUVtQX7PyYy4LG76bx+GsLFKtYRkC5GMjr3HGFP2Clj423Txks2g4Q9YlC0HUcYnPQqPnDMIMo0lXsU+6rBs4Wi0IC4Tk4yWKi+kSuGTF7x9J8ym4kU5Q3s9dStz2ORal/cjYIzsIORELeU3lxJUn+sVbrT4hDZR7KIivrNI5CE7JgXhsonOq/RxP6ykLNwh/sLfD2PWKOsFTM83i4cWW8qvUrudxw92OEoJqO+YC3UNvWvCcfc3msU0VpF0ukpkBPEyXPWw/C67V3vTfQKkGL3Ou7jqP+3xGcjmz2F7l/yol+mLwj+QL9afEQ93xHwxQnhVKcXA5wwS3QkIGljuf+oqBGbSZHtCsInRSU0flZEvteXZpb58mprCvEHUsoEOEEy++k55qOM2xd3GxTiCgONCO1CGa4/Z5WPirVGehEUvAPcef8j47apZ7ilExkPEKadYJR+KUKaMsh0CuvTTxhi25UPalqNanqVuZ6HPqJ1drIRWdFjTZfvSOD8WCIFJ82wpnH//HfSbPewZ4OvRHhOVkNfwlIZnavNZp9lj4JhbAJ1/UnRMvI+8BlAEk7k6jJHhomCq0OxM661ySwgcoBJ9bH3MagtaRZ0VK9x49XXEyegk52OLgvnriTaUlZMDKojzneFXwSeHBCA9LdiY4L1NSoJgyHPv1svXEN7Xl76EXbx3SnaCyLHNOwYBmiElYwY+R65KO2Tb49I8mhrVEhSb/pvPBjTbaNFaG91vTC7TRtl48v2YvvFT38KHSVZ9XEFI54p3n8s+8hf0sndLlqZH22CxEnRqF42J60LjCVmTdB4HiES4QbAppZ4bMf22vkLzUeetLR/jLDVksMOsb3tmpeXQiozW2HMtHPDEjHRGK7p3jv184Lx8McNDM95/VlfsKprHT0R32pzzim266RqnSDIVf8kUhsbGPdrV0ECe3R0jFL7VHBLaYfC3d7wL91qGICkSdXzj5wBnuIsr5D08W/fsz2yW/rAEfQud5VpjdxMMimlDuxrdjO9BpMygHNA1WI1RDcv/Z2H8dls7rjfaRuI1y2w8T8xaMUjjI+nj0mSzemsYHxaVqJ75fxaH+ig/Afssx7Lgx2RZf3S0n1Iutfve683yroO2YZc2URSkmOOQQSQFxi4HxXkzb+iZUsezmPKc09xnCnDplWOxFRlylj7toFiL12+B2xDNt1zCTOw2QjFZMzmAoZEf2MLgaTXL4VfDUGzWFQJZ3sPanNKaNff1AmA14NwxpMnyPGqTbNGcVhcedLA0aRRqmuJdOLL0PhsraoywZZIrs8ZQOQJi2y7Rx3qLyH8Tb15nyQ/h5B8JCR13ArC4FR0v584wiyX7jee1G1S87hmKugRLuxfVejIGNctakJvXLVQX01KN5uh/13Jz5f+dT/gJ/65oHslgPjbowAdXmJyBaiOd7/KHzOhWg5eY6bar+w3j1i29VrauZ19FG0/HHr8OIjdDoHgCyPcQOVn1vXBtNV1v3QvUz/Zi2atZoa9H45CN7LL84rTlDCrZKofF4B4diZa5WrbpSwNRmxF61P60fZ7JFGnmxHVatNfBweDyjSh2X0dtSZ7W9DRqdLWApQd346XzxrLtdgcaHLbiyrVy2497OR+8M5WeAfdO0rQyUX1dHqhjmQHTP014Fl1KZOog/VZM3hDZmaW+xF3didm+pXCBSEn9WZJa8RBP5wDx3v0YBSBPAiTRVSove7pT1+iAJh+tgXjkg9u9KDbHWMz+JOykyshrSz9bu2vSKCzimDiU1xCyfsOZ9WMGdBvysfCl5TYQ330sdsFEBlXVpzb7h1WfiCv/wfLXM8Q6AQNE97LJ3ZM0zGvu1iJP53wJ3niMvZIsWHsJw8HVzZV1wXPCbQkq8X67gpqnkmUnnVfa3S9yvCmbUt5W6ad7bLcoeoHI0Udz5V7mNtFtDPyDUJZSuZdBBidxax5vrRCKZEf+5VHfh/NXGAsNZBNXLzuAISPNpes1tYEM7ej7T7CgZLEDqcjxEYvXyZ04paM4nsvOh6pjMBKP+tpCuEwJVQUYZsFV5QXafZjKAQVylafQo4D16aJ2SHhGEPSvLA3DZ50pIAI3oceitHnGv55arbRCU549IpjWS9ZJ8inL/ZkM/fxA5DiLBRKrmeUzDQGNG9HMGdKoxKJxfxUBZq6DLogQTjRQdi580YEP/JYHdv7Nc+arc7QIekMqhMgCgzE85uNgcC2VBcTHFLUrekCf3fuaWqjICCfHOSxETpO2BvBM2HAT2aRfZlpfmzppCRCF4ZMohdnuAeDF36hdBUBsHJeRsrzDtFKEeRye2j8ZtnDD/BBUwXQKuwXPLl7i75DA2oQpqIP1H6n72KZzD9FITQtTPxZFOBjvZv7z5kW6EJ+SPiJJgCVU2s8WNVgBRkq78ZPN5/hIeeWjMgZB9drWg7rfVRAFiNrgvVf9hAwWJ8HmRfzZH7Tp738JQ7rWqh/ibSSm0tDrQB7kMawtxFdUIziFHPGhnBXOp6+m45752fG2XKdsBpwJxWaoecRf4o1rh1ZUMGuMRXY6K+DJsVreVgIJFQPRELI400EBrFI9XJYTR53oyADDJvOiq0bg4+3rNBOVZnzUGI3azGNdHdk/+nhY25FDHgk/AQtxHQJJTGLRQ69gh8dAjrfhGlrC992RlGmlNRVzvv9Lv1Trynpbb54fCKdELjohsfPFu0ddRwyBbkCaPd01TXmsgqd14N/uJSDfvSkxRYdhL+DhcDTGx6R5iY8E00YLvqZG7w2qYSDtCRlyZA1eXIkAouBjUiVIEEXM5sZXGe2R+IzG/N2IhwRVYOkl8dLm/Fb+lt/G7dmdB4va55keoZBuCAHrx26vYVQiXGIJCqf5l99IfQ8DvMPZfbb6Acsx/QGXVgYGx5Nu0WLX0EtBxLMy4+LBax/3KkVFC3eymJd0v4RqTBt1LR04WrYckPG/jmWEJ62RGARJDQCKyPIoDOP3ejLDqSW1Z4za5RdhDBSQXo61bo3+3dVKCcIaDMOah4XyjG+vrWzNWBD17FMXtugPlI9CoIsctxQ7ZEfiIlNvuLk0o9fUytLCWhPAkT3I9Z2oIDkgQYmxSaRx0YGYtWlEgIQ9VCIKz4OnH+L+HXoUoSDTnOxbkSmITJz8zfyLcPG/xKXcGCWRTkEckRhpkvCpDruM7GRPyDJ/CiAfyO+nUo0cIWFm1rNV1CAA5ej2oh4yhu7Ojijc3GyYugmXglj44KaazKzWm89pszh8urRfCP81QF2XWBroByb46nLmYlr19FibMUZFBswj/7Hn49jxTW6PK+KN9ubCoZVL990BvVUqYrz+pj8u4VvLQJYMEeywoFpXvrbmwhTnUkAstjebu1GzpbeVYErPYNJoBwXC7PB54QjlmDjYKLQ84UXO02LIGMQC7zDLhP68T23MeOqcbQjjb+b1Fxgkr/pZ4AkvJw7Np50n1hAAEQ=
        - #1:
          - type: tool-result
          - toolCallId: 2sCItIX5PlBQfZqG
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: FlCew0bcMeT5w8KY
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: QvC2ktmBYBht4uk9
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: v5BsQaND5gK6wBfw
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: kEspejUOzeKgBCnp
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: S7quzpw7UF9QfaVD
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.