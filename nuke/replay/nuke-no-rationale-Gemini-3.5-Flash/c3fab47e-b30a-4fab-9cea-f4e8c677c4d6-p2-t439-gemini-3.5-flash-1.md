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
      - toolName: set-relationship
      - args:
        - Public: -100
        - Rationale: The Inca are our primary competitor. Since we are at war and steamrolling their cities, we must set relationship modifiers to extremely hostile to reject weak peace offers and focus on conquering their capital, Cusco.
        - TargetID: 0
        - Private: -100
    - #1:
      - toolName: set-relationship
      - args:
        - Private: -100
        - TargetID: 5
        - Rationale: Indonesia is a vassal of our enemy, The Inca. We are currently at war and will maintain absolute hostility to crush them.
        - Public: -100
    - #2:
      - toolName: set-persona
      - args:
        - Rationale: Maximizing our WarBias to 10 to force the AI to plan and execute offensive military operations and pursue key capitals aggressively, since we are in a race against other civilizations' victory conditions.
        - WarBias: 10
    - #3:
      - toolName: set-research
      - args:
        - Technology: Robotics
        - Rationale: Researching Robotics to unlock Missile Cruisers for our naval dominance and the Spaceship Factory to further enhance our production capabilities.
    - #4:
      - toolName: set-policy
      - args:
        - Policy: Iron Curtain
        - Rationale: Iron Curtain is highly synergistic with our massive conquest strategy, granting free courthouses on annexation and a massive 200% food/production boost to internal trade routes to power up our empire.
    - #5:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Production: 100
          - Ranged: 95
          - Nuke: 100
          - MilitaryTraining: 95
          - Offense: 80
          - Science: 70
          - Mobilization: 100
          - Defense: 40
          - Air: 100
          - Diplomacy: 40
          - UseNuke: 95
          - Gold: 50
          - Culture: 40
          - AirCarrier: 80
        - GrandStrategy: Conquest
      - rationale: Pivoting our flavors toward a strong offensive military stance while maintaining high mobilization, production, science, and gold to support the late-game war effort.
  - tokens:
    - inputTokens: 69959
    - reasoningTokens: 7497
    - outputTokens: 375
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Reviewing Game Status**
            
            My current focus is on a thorough review of our game status. We are in Turn 438, Prince difficulty, Information Era, on Standard speed with 500 turns maximum. I'm specifically examining victory contenders at this juncture.
            
            **Analyzing Victory Conditions**
            
            I am currently evaluating our progress towards domination, noting the Inca and Austria as primary rivals with multiple capitals. For science, I've confirmed we can pursue either Robotics or The Internet, with Alternative Energy nearing completion. Poland is making a strong push for cultural victory, influencing five other civilizations.
            
            **Stopping Cultural Victory**
            
            I've identified Poland and Austria as immediate cultural victory threats. While Poland is friendly, their impending win necessitates action. Fortunately, they're already sanctioned, hindering their progress. Austria is also very close, making this a critical juncture to pivot strategy and prevent their win.
            
            **Preventing Diplomatic Victory**
            
            My immediate concern is Austria's imminent diplomatic victory, requiring 40 delegates and possessing 45. They are also at war with us and their allied city-states, which blocks peace. I'm considering how to leverage our new Great Diplomat and our current war status to disrupt their delegate count.
            
            **Disrupting Diplomatic Victory**
            
            I'm focused on derailing Austria's imminent diplomatic win. She currently holds 45 delegates and needs only 40, with a crucial vote upcoming in just four turns. While direct diplomatic missions to her allies are blocked by our ongoing war and their city-state status, I'm exploring swift military intervention against her allied city-states to diminish her delegate count.
            
            **Capturing Strategic City-States**
            
            I'm evaluating the feasibility of capturing Austrian allied city-states to curb their delegate count. Okilis, at coordinates (74,33), appears to be the most accessible target, with several of our units in close proximity, including modern armor and rocket artillery stationed at Nippur.
            
            **Securing Incans Territories**
            
            My current priority is neutralizing the Inca threat by steamrolling their territories. Specifically, I'm focusing on Vitcos and Arequipa, where our overwhelming military advantage is already evident. Even Sydney, though currently contested, will soon fall under our control.
            
            **Disrupting Austrian Victory**
            
            My immediate focus is dismantling Austria's victory paths. While military gains against the Inca are solid, Austria's diplomatic win in four turns and potential cultural win require urgent attention. I'm exploring options to block their delegate count, given our ongoing war and limitations on direct diplomatic engagement with their allied city-states.
            
            **Blocking Global Hegemony**
            
            I'm focusing on preventing Austria's "Global Hegemony" proposal from passing in the World Congress. By rallying the other civilizations, whose combined votes far outweigh Austria's, we can defeat this bid. Many are at war with Austria, making their opposition highly probable.
            
            **Analyzing Ideological Alignment**
            
            I'm assessing the current ideological landscape to predict voting patterns in the World Congress. Austria, allied with the Huns via vassalage, aligns with Freedom. The Incas, Indonesia, Poland, and we are all Order, while Morocco leans Autocracy. This distribution suggests that the "Global Hegemony" proposal should face significant opposition.
            
            **Reassessing Grand Strategy**
            
            I'm reassessing our overall strategy, questioning whether our focus on a powerful military aligns with a Domination victory or if we should pivot towards Science. Currently, our grand strategy is set to Conquest. I'm examining Order policies like Socialist Realism and Iron Curtain alongside existing ones to see which best supports our chosen path.
            
            **Selecting Ideology Tenet**
            
            I'm confirming my choice for the next ideology tenet. "Iron Curtain" from the Order tree offers substantial benefits for our wide, conquest-focused empire, providing free courthouses and significant internal trade route bonuses. This aligns perfectly with our current expansionist strategy and will greatly boost our city growth and production.
            
            **Evaluating Offensive Strength**
            
            My current thinking is focused on a discrepancy I've identified. Despite being at war with multiple major powers and experiencing significant battlefield success, my "Offense" flavor score remains surprisingly low at 20. This warrants further investigation into what contributes to this metric.
            
            **Investigating Offensive Score**
            
            I am perplexed by our low "Offense" flavor score of 20, especially given our ongoing wars and battlefield successes. This feels counterintuitive, as our goal is clear: securing nine capitals for domination. I am actively trying to understand the mechanics behind this metric and how to improve it to better reflect our aggressive posture.
            
            **Boosting Offensive Flavor**
            
            I am now prioritizing increasing our "Offense" flavor score to 80, while reducing "Defense" to 4. This adjustment aims to better align our in-game mechanics with our strategic goal of domination, especially considering the vast distances and scattered enemy strongholds we need to conquer.
            
            **Adjusting Ideology Balance**
            
            I'm focusing on refining our ideology tenets to better support our domination goals. While "Iron Curtain" is strong for city growth, I'm re-evaluating "Mobilization," "MilitaryTraining," and "Espionage" flavors, aiming to increase science and culture slightly for faster tech and policy acquisition. Gold and diplomacy also need attention to counter Austria.
            
            **Correcting Diplomatic Settings**
            
            I'm reviewing our diplomatic settings, specifically the relationship modifiers with the Inca. It's illogical that our modifier is set to 100/100 while we're at war and actively crushing them; this needs correction to ensure we don't accidentally pursue peace or unfavorable terms.
            
            **Setting Diplomatic Stances**
            
            I'm finalizing our diplomatic stance towards belligerent nations. I'm setting relationships with Austria, the Huns, and Indonesia to hostile (-100) to ensure we press our advantage and achieve domination without premature peace offers. Poland's stance is still under review.
            
            **Adjusting Diplomatic Relations**
            
            I'm reassessing diplomatic relationships and my immediate priority is to ensure hostile stances with Indonesia and the Inca, as our current alignment doesn't reflect our active conflict. I'm maintaining a friendly stance with Poland despite their looming cultural victory, as it allows us to focus on other threats. My persona's WarBias is also being adjusted.
            
            **Adjusting War Bias**
            
            I am now focusing on fine-tuning our persona settings to better align with our current aggressive strategy. Specifically, I am increasing the `WarBias` to 10 to ensure the AI prioritizes offensive actions, which is critical for our domination victory pursuit while simultaneously countering Austria's diplomatic and Poland's cultural threats.
            
            **Increasing War Bias**
            
            My focus is on solidifying our aggressive posture by increasing the `WarBias` to 10. This will ensure we prioritize offensive actions, crucial for achieving domination while simultaneously counteracting Austria's diplomatic and Poland's cultural threats.
            
            **Adjusting Player Stances**
            
            I'm now reviewing and adjusting diplomatic stances with the Inca, ensuring a hostile relationship reflecting our ongoing war. This is crucial to prevent any accidental peace offers, allowing us to fully commit to our domination victory.
            
            **Refining AI Stances**
            
            I'm confirming AI stances and persona settings. I've set relations with the Inca and Indonesia to hostile and am increasing our persona's `WarBias` to 10 to ensure aggressive AI play and prevent premature peace, vital for domination. I'm also verifying flavor key capitalization.
            
            **Setting Diplomatic Relationships**
            
            I am finalizing the diplomatic settings, ensuring hostile relationships with the Inca and Indonesia to prevent premature peace and secure our domination victory. My focus is also on confirming the exact parameters for all relevant commands.
            
            **Updating AI Persona**
            
            I am now confirming the final persona settings, particularly focusing on the `WarBias`, which has been set to 10. This adjustment is crucial to ensure aggressive AI planning and execution of offensive operations, vital for achieving our domination victory while managing rival victory conditions. I am also verifying all flavor key capitalization.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: DvYSfGBDrhAa2SFN
          - toolName: set-relationship
          - input:
            - Public: -100
            - Rationale: The Inca are our primary competitor. Since we are at war and steamrolling their cities, we must set relationship modifiers to extremely hostile to reject weak peace offers and focus on conquering their capital, Cusco.
            - TargetID: 0
            - Private: -100
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: c97OaQnGpCUsnwoT
          - toolName: set-relationship
          - input:
            - Private: -100
            - TargetID: 5
            - Rationale: Indonesia is a vassal of our enemy, The Inca. We are currently at war and will maintain absolute hostility to crush them.
            - Public: -100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: xkniAWH8F1IDrUkq
          - toolName: set-persona
          - input:
            - Rationale: Maximizing our WarBias to 10 to force the AI to plan and execute offensive military operations and pursue key capitals aggressively, since we are in a race against other civilizations' victory conditions.
            - WarBias: 10
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: syAEi9Y6JY829gtF
          - toolName: set-research
          - input:
            - Technology: Robotics
            - Rationale: Researching Robotics to unlock Missile Cruisers for our naval dominance and the Spaceship Factory to further enhance our production capabilities.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 3TWuAlUtjx186sbP
          - toolName: set-policy
          - input:
            - Policy: Iron Curtain
            - Rationale: Iron Curtain is highly synergistic with our massive conquest strategy, granting free courthouses on annexation and a massive 200% food/production boost to internal trade routes to power up our empire.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: vRRGbgjeL5fehc0Z
          - toolName: set-flavors
          - input:
            - Rationale: Pivoting our flavors toward a strong offensive military stance while maintaining high mobilization, production, science, and gold to support the late-game war effort.
            - Flavors:
              - Production: 100
              - Ranged: 95
              - Nuke: 100
              - MilitaryTraining: 95
              - Offense: 80
              - Science: 70
              - Mobilization: 100
              - Defense: 40
              - Air: 100
              - Diplomacy: 40
              - UseNuke: 95
              - Gold: 50
              - Culture: 40
              - AirCarrier: 80
            - GrandStrategy: Conquest
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: DvYSfGBDrhAa2SFN
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: c97OaQnGpCUsnwoT
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: xkniAWH8F1IDrUkq
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: syAEi9Y6JY829gtF
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 3TWuAlUtjx186sbP
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: vRRGbgjeL5fehc0Z
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.