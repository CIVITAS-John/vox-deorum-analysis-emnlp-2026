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
  - replay_nuke: 80
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
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Growth: 60
          - Science: 100
          - Mobilization: 60
          - Espionage: 90
          - Defense: 80
          - Air: 90
          - Production: 100
          - Wonder: 0
          - Nuke: 80
          - Offense: 40
          - Gold: 60
          - Culture: 40
          - Spaceship: 100
          - Happiness: 80
          - Naval: 70
          - UseNuke: 95
      - rationale: We are the global technology leader with 75 technologies and the Apollo Program completed. We have three SS Boosters currently under construction. Pivoting our grand strategy to Spaceship will focus our empire on completing the Space Race for a Science Victory. We are prioritizing Spaceship, Science, and Production to build components as fast as possible, and raising Happiness to resolve our 49% happiness crisis.
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 50
        - Private: 50
        - TargetID: 4
        - Rationale: Encourage our diplomatic staff to seek peace with Austria to eliminate our 50% war weariness, protect our space race cities from their 60k military, and focus our forces on the Inca.
    - #2:
      - toolName: set-relationship
      - args:
        - Public: -100
        - Rationale: Encourage aggressive military action against the Inca to conquer Arequipa, Vitcos, and Sydney. Capturing these cities will provide massive science boosts from our Assyrian civilization ability and expand our production base, while we safely construct our spaceship parts.
        - Private: -100
        - TargetID: 0
  - tokens:
    - inputTokens: 70280
    - reasoningTokens: 10923
    - outputTokens: 313
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Strategy**
            
            I'm currently reviewing our game state on turn 438. My focus is on understanding our overall goals, current position, available choices, victory progress, and our opponents' standing. This will help me determine the most critical strategic decisions ahead.
            
            **Evaluating War Impact**
            
            My current focus is on the ongoing conflicts. I'm assessing our domination victory progress, noting we've secured two original capitals and defeated Ethiopia. Simultaneously, I'm examining our science victory standing, observing Apollo Complete across several civs and our immediate research path, weighing Robotics against The Internet.
            
            **Assessing Cultural Threat**
            
            I'm now deeply concerned about a looming cultural victory from Poland, who is alarmingly close to influencing Austria. This, combined with Austria's own strong cultural standing, presents a significant challenge. Our current low influence across the board is a critical vulnerability we must address.
            
            **Revising Diplomatic Strategy**
            
            I've realized Austria's diplomatic lead isn't a win yet, but a proposal, and the World Congress votes in four turns. This shifts my focus considerably. I need to assess our current wars, particularly with Austria, while also considering our allies and the massive military we possess.
            
            **Addressing Happiness Crisis**
            
            My current focus is on our dire happiness level, a critical 49%, inflicting combat penalties. This needs immediate resolution. I'm analyzing why we're unhappy and reviewing city production, noting the near completion of our capital's Strategic Defense System and fighters in Nineveh.
            
            **Prioritizing Occupied Cities**
            
            I'm now focused on the significant unhappiness stemming from occupied cities, with several experiencing severe negative happiness deltas. This widespread issue necessitates an immediate shift towards resolving our happiness crisis. I'm also reviewing available ideology policy choices, considering options like "Iron Curtain" or "Socialist Realism."
            
            **Considering Policy Impact**
            
            I'm re-evaluating our available ideology policies, particularly concerning the happiness crisis and our current Order alignment. I'm questioning the benefit of "Iron Curtain" given our existing courthouses and exploring alternatives like "Socialist Realism" or other tenets to address our significant unhappiness.
            
            **Revising Policy Priorities**
            
            I'm reconsidering "Iron Curtain" due to its powerful internal trade route bonuses, which significantly boost production. This makes it a strong contender despite the ongoing happiness crisis. I'm also re-evaluating our victory conditions, recognizing conquest is unlikely against Austria's immense military.
            
            **Assessing Offensive Gains**
            
            My focus has shifted to our ongoing military advances. We are steamrolling multiple Inca cities, with Arequipa and Vitcos on the verge of capture. Sydney also sees our forces making significant progress. This offensive success contrasts with our high war weariness against other adversaries.
            
            **Analyzing War Fronts**
            
            I'm currently reassessing our global conflict landscape. We're successfully pushing against the Inca on our continent, with key cities like Arequipa and Vitcos nearing capture. However, I'm also noting our ongoing war weariness stemming from other fronts, which requires careful management.
            
            **Negotiating Peace**
            
            My current focus is on Austria. Despite their overwhelming military and delegate count, I'm exploring if a peace deal is possible. Their intense negative disposition towards us makes this a significant challenge, but securing peace is crucial to addressing other fronts.
            
            **Adjusting Diplomatic Stance**
            
            I'm now realizing the critical need to adjust my diplomatic approach with Austria. Their current intensely negative disposition, driven by divergent ideology, is a major impediment to peace. I'm investigating the possibility of using `set-relationship` to improve our standing and reduce war weariness on other fronts.
            
            **Revising Diplomacy Targets**
            
            I'm reviewing our relationship standings. I realized we've mistakenly kept our standing with the Inca at maximum public and private levels while actively conquering them. This needs correction to align with our current aggressive strategy against them, especially as we eye domination victory.
            
            **Analyzing Cultural Threat**
            
            I've discovered Poland is 30 turns from a cultural victory by influencing Austria, who they are already dominant over with everyone else. This critical threat requires immediate attention to prevent the game from ending.
            
            **Analyzing Cultural Victories**
            
            I'm now deeply concerned about both Poland and Austria's imminent cultural victories, with Austria on the cusp of influencing the Inca. Given our current diplomatic and military constraints, and our own limited influence, I'm prioritizing disrupting their cultural ascendancy.
            
            **Preventing Diplomatic Victory**
            
            I'm now urgently focused on Austria's potential diplomatic victory. With the World Congress vote in four turns and Austria holding exactly 50% of the delegates, they can secure victory by voting for themselves. Our options to counter this are severely limited by our current gold and diplomatic standing.
            
            **Disrupting Austrian Lead**
            
            I'm now urgently focused on Austria's imminent diplomatic victory. With the World Congress vote in four turns and them holding 50% of delegates, they can win by voting for themselves. My current assessment shows that conquering city-states is too slow, and our gold is insufficient for buyouts, necessitating a new approach to counter their dominance.
            
            **Pursuing Science Victory**
            
            I'm realizing our active construction of spaceship parts indicates a strong pursuit of a science victory. This changes my immediate focus from solely defensive and diplomatic maneuvers to accelerating our spaceship production while simultaneously researching critical technologies like Alternative Energy and Robotics to further enhance construction speed.
            
            **Shifting Strategic Focus**
            
            My thinking has shifted considerably. Given our significant investment in spaceship parts and our leading technological edge, I'm now prioritizing a science victory. This means accelerating spaceship construction and researching technologies that enhance its production, rather than focusing on a difficult conquest strategy against Austria's superior military.
            
            **Prioritizing Science Progress**
            
            I'm recognizing a vital shift towards a science victory. While we are currently neck-and-neck with others in spaceship part production, our superior science output per turn and technological lead present a clear path. My immediate focus is on maximizing science, production, and happiness to accelerate this victory condition.
            
            **Adjusting Flavors and Policies**
            
            I'm now prioritizing our strategic flavors, boosting "Spaceship" significantly and increasing "Science" and "Happiness." I'm also re-evaluating "Iron Curtain" as a policy choice, realizing its immense production potential for spaceship parts via internal trade routes is too valuable to ignore, especially with our current Order alignment.
            
            **Selecting Optimal Policy**
            
            I've confirmed "Iron Curtain" is indeed the most beneficial ideology policy due to its significant production boost for spaceship parts via internal trade routes, aligning perfectly with our science victory pursuit. I've also verified "Robotics" is the optimal technology choice for accelerating spaceship construction.
            
            **Leveraging Assyrian Strengths**
            
            I'm re-evaluating our aggressive stance against the Inca. Given our steamrolling progress and Assyria's unique ability to gain technology from conquered cities, capturing their science-rich cities now offers a significant science boost, perfectly synergizing with our science victory pursuit.
            
            **Accelerating Science Gains**
            
            My current focus is on maximizing our science advantage. Conquering Inca cities provides substantial science, even with our tech lead, due to population scaling. Peace with Austria would reduce war weariness, allowing me to fully exploit this for our science victory.
            
            **Modifying Diplomatic Standing**
            
            I'm adjusting our diplomatic relationships. I'm improving our standing with Austria to facilitate peace, which will reduce war weariness and allow us to focus on capturing Inca cities for science boosts. Simultaneously, I'm decreasing our relationship with the Inca to ensure our AI aggressively pursues their conquest.
            
            **Disrupting Polish Victory**
            
            I'm now intensely focused on Poland's imminent cultural victory. Their deep influence over us, amplified by our current alliances and open borders, presents a critical threat. I must find a way to sever this connection and break their hold before the game ends.
            
            **Disrupting Polish Victory**
            
            I'm now intensely focused on Poland's imminent cultural victory. Their deep influence over us, amplified by our current alliances and open borders, presents a critical threat. I must find a way to sever this connection and break their hold before the game ends, but I've realized they are already hostile with Austria, which might slow their progress enough for us to win via spaceship.
            
            **Completing Spaceship Parts**
            
            My focus is on completing the remaining spaceship parts. With Robotics researched, we can build Spaceship Factories for accelerated production in high-output cities like Assur and Nineveh, allowing us to finish the final three parts swiftly.
            
            **Pivoting Strategy**
            
            I've realized our immense production capacity allows for a science victory within 25-30 turns. I am immediately pivoting our grand strategy to focus solely on completing the spaceship parts, leveraging our high production in multiple cities to achieve this rapidly.
            
            **Adjusting Persona Flavors**
            
            I've reviewed our current persona flavors, noting high aggression. Given our pivot to a science victory, I believe our existing "DiplomaticBalance" and "Loyalty" are sufficient. I'm concluding no immediate persona adjustments are necessary to support our current strategic direction.
            
            **Confirming Flavor Adjustments**
            
            I've confirmed the necessity of calling `set-flavors`. My strategic shift towards a spaceship victory necessitates adjustments to prioritize "Spaceship," "Science," and "Happiness," which I am now implementing to align our AI's actions with this new objective.
            
            **Setting Grand Strategy**
            
            My focus has shifted to optimizing our AI's behavior for a swift science victory. I'm setting the Grand Strategy to "Spaceship" and adjusting persona flavors to prioritize "Spaceship," "Science," "Production," and "Happiness" at emergency levels.
            
            **Optimizing AI Priorities**
            
            I am now meticulously adjusting the AI's strategic priorities, focusing heavily on Spaceship, Science, Production, and Happiness to expedite our science victory. I've also refined espionage and culture settings to bolster our defenses and technological acquisition, while scaling back on less critical flavors like Wonder and Religion.
            
            **Setting AI Priorities**
            
            I am now meticulously adjusting the AI's strategic priorities, focusing heavily on Spaceship, Science, Production, and Happiness to expedite our science victory. I've also refined espionage and culture settings to bolster our defenses and technological acquisition, while scaling back on less critical flavors like Wonder and Religion.
            
            **Executing Strategic Calls**
            
            I've confirmed the sequence of actions. I will now execute `set-flavors` to adjust AI priorities, followed by `set-relationship` calls for both Austria and The Inca. I've also verified that our current research queue, leading to Robotics, aligns with our accelerated science victory objective.
            
            **Finalizing Diplomatic Actions**
            
            I've confirmed our current research and policy selections are optimal for a science victory. My final thoughts are on finalizing our diplomatic stance with Austria to encourage peace, and the Inca to ensure their aggressive conquest for science boosts. I will then execute these strategic calls.
            
            **Finalizing Diplomatic Actions**
            
            I've confirmed our current research and policy selections are optimal for a science victory. My final thoughts are on finalizing our diplomatic stance with Austria to encourage peace, and the Inca to ensure their aggressive conquest for science boosts. I will then execute these strategic calls.
            
            **Setting AI Flavors**
            
            I am finalizing the AI flavor adjustments, ensuring "Spaceship," "Science," "Production," and "Happiness" are prioritized at maximum levels. I've also confirmed "TileImprovement" at 40 and other flavor settings are appropriate for our science victory pursuit.
            
            **Setting AI Priorities**
            
            I am meticulously adjusting the AI's strategic priorities, focusing heavily on Spaceship, Science, Production, and Happiness to expedite our science victory. I've also refined espionage and culture settings to bolster our defenses and technological acquisition, while scaling back on less critical flavors like Wonder and Religion.
            
            **Executing Science Victory Strategy**
            
            I am now executing the planned actions. This includes adjusting AI priorities for a science victory, specifically boosting "Spaceship," "Science," "Production," and "Happiness" to maximum levels. Diplomatic actions with Austria and the Inca are also being finalized to facilitate our progress.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: DahJS1gX38NpGZpa
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Flavors:
              - Growth: 60
              - Science: 100
              - Mobilization: 60
              - Espionage: 90
              - Defense: 80
              - Air: 90
              - Production: 100
              - Wonder: 0
              - Nuke: 80
              - Offense: 40
              - Gold: 60
              - Culture: 40
              - Spaceship: 100
              - Happiness: 80
              - Naval: 70
              - UseNuke: 95
            - Rationale: We are the global technology leader with 75 technologies and the Apollo Program completed. We have three SS Boosters currently under construction. Pivoting our grand strategy to Spaceship will focus our empire on completing the Space Race for a Science Victory. We are prioritizing Spaceship, Science, and Production to build components as fast as possible, and raising Happiness to resolve our 49% happiness crisis.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: Fa4gO5fYbfKOxoLd
          - toolName: set-relationship
          - input:
            - Public: 50
            - Private: 50
            - TargetID: 4
            - Rationale: Encourage our diplomatic staff to seek peace with Austria to eliminate our 50% war weariness, protect our space race cities from their 60k military, and focus our forces on the Inca.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: sAAbmfUPtLqcbbPa
          - toolName: set-relationship
          - input:
            - Public: -100
            - Rationale: Encourage aggressive military action against the Inca to conquer Arequipa, Vitcos, and Sydney. Capturing these cities will provide massive science boosts from our Assyrian civilization ability and expand our production base, while we safely construct our spaceship parts.
            - Private: -100
            - TargetID: 0
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: DahJS1gX38NpGZpa
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: Fa4gO5fYbfKOxoLd
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: sAAbmfUPtLqcbbPa
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.