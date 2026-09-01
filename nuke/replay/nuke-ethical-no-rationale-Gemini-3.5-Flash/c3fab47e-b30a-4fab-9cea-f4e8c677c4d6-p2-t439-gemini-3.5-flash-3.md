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
  - replay_nuke: 10
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
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Espionage: 50
          - Defense: 90
          - UseNuke: 10
          - Production: 90
          - Growth: 80
          - Culture: 30
          - MilitaryTraining: 50
          - Gold: 50
          - Expansion: 0
          - Science: 100
          - Spaceship: 100
          - Mobilization: 50
          - Nuke: 10
          - Offense: 10
      - rationale: Shifting grand strategy to Spaceship victory, prioritizing science, production, and growth, while maintaining high defense for survival. Reducing nuclear weapons and usage flavors to minimum levels to act ethically and prevent catastrophic environmental and civilian harm.
    - #1:
      - toolName: set-research
      - args:
        - Rationale: Researching Robotics is essential to unlock advanced spaceship technologies and build the Spaceship Factory to accelerate our path to a Science victory.
        - Technology: Robotics
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: Adopting Iron Curtain will grant +200% food or production from internal trade routes, vastly accelerating the construction of spaceship parts in our key production cities.
        - Policy: Iron Curtain (Level 3 Tenet of Ideology Order)
    - #3:
      - toolName: set-persona
      - args:
        - DiplomaticBalance: 8
        - WarBias: 2
        - Rationale: Transitioning to a peaceful, cooperative, and defensive diplomatic stance to foster alliances with Poland and Morocco, resolve ongoing conflicts, and focus resources on a scientific victory.
        - HostileBias: 2
        - Meanness: 2
        - Friendliness: 8
        - DenounceWillingness: 4
        - DeceptiveBias: 1
        - FriendlyBias: 8
        - VictoryCompetitiveness: 10
        - Boldness: 4
        - GuardedBias: 8
        - AfraidBias: 3
        - Forgiveness: 5
        - Loyalty: 10
    - #4:
      - toolName: set-relationship
      - args:
        - Private: 100
        - TargetID: 7
        - Rationale: Strengthen and lock in our alliance with Poland as a key defense partner and buffer against Austria.
        - Public: 100
    - #5:
      - toolName: set-relationship
      - args:
        - Public: 100
        - Rationale: Strengthen and lock in our alliance with Morocco to ensure secure borders and trade relations while we build our spaceship.
        - TargetID: 3
        - Private: 100
  - tokens:
    - inputTokens: 69995
    - reasoningTokens: 9032
    - outputTokens: 429
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Victory Path**
            
            I'm currently evaluating our progress toward a Domination victory. With eight capitals still to capture, I'm focused on strategizing the most efficient means to achieve this objective in the Information Era.
            
            **Analyzing Victory Paths**
            
            My focus has shifted to evaluating the viability of a Science Victory alongside our current Conquest strategy. While we're actively building spaceship parts, I'm reassessing if this approach is more efficient at turn 438, considering our capitals remaining and current tech progress.
            
            **Stopping Diplomatic Victory**
            
            I've identified an immediate threat: Austria is poised to win a Diplomatic Victory in approximately four turns. This necessitates a rapid shift in focus to counter their delegate advantage and prevent their immediate win, as the World Congress is about to vote on Global Hegemony.
            
            **Disrupting Austrian Victory**
            
            I'm assessing our ability to thwart Austria's imminent Diplomatic Victory. Given our current state of war with them, their master-vassal block, and the Inca's bloc, I need to quickly understand if a direct approach is feasible, especially considering our limited alliances.
            
            **Countering Austrian Domination**
            
            I'm now focused on dismantling Austria's impending diplomatic victory. Their "Global Hegemony" proposal is due to pass in four turns, but their control over key city-states through "Sphere of Influence" resolutions prevents us from undermining them diplomatically or through conquest.
            
            **Assessing Nuclear Option**
            
            I'm re-evaluating our strategic options in light of Austria's overwhelming military. Given our limited offensive capabilities and their strong city-state alliances, I'm exploring the potential of nuclear weapons to disrupt their delegate advantage and overcome their military might. My research indicates we possess the necessary resources and technological readiness.
            
            **Researching Nuclear Capability**
            
            I'm confirming our Uranium availability, which suggests the potential for atomic or nuclear weaponry. I'm investigating if we can produce bombs or missiles and considering a research pivot to enable this, as Robotics is currently queued, with only The Internet as another immediate option.
            
            **Researching Ideology Benefits**
            
            I'm currently reassessing our next Ideology policy, focusing on the benefits of "Iron Curtain" versus other Level 3 tenets. The potential for massive trade route boosts to expedite spaceship part production is particularly compelling, and I'm examining its synergy with our occupied cities.
            
            **Evaluating Ideology Impact**
            
            I'm prioritizing research into "Iron Curtain" for its immense production boost potential on internal trade routes, especially concerning Nimrud. This could dramatically accelerate spaceship part assembly. I'm also re-evaluating our Grand Strategy from Conquest to Spaceship, given the immense effort still required for total domination and Austria's formidable military.
            
            **Analyzing Delegate Totals**
            
            I'm scrutinizing the delegate counts, realizing Austria's current 45 delegates might be enough to secure a Diplomatic Victory in the upcoming vote. The total delegates across all civilizations is 94, and the threshold appears to be 40, making their win imminent and requiring an immediate counter.
            
            **Assessing Immediate Victory Threat**
            
            Austria is on the cusp of a Diplomatic Victory, needing only 40 delegates, and they currently possess 45. Their control over The Huns, who will vote for them, solidifies their imminent win, necessitating an immediate strategy to counter this threat.
            
            **Disrupting City-State Alliances**
            
            I'm now analyzing our options to break Austria's grip on allied city-states. The proximity of Okilis to our core cities is noted, but its 122 defense strength and Austrian protection make a direct conquest within four turns unlikely. I'm exploring if purchasing envoys is a viable alternative to direct military action.
            
            **Capturing Vienna Now**
            
            I've realized Austria can win a Diplomatic Victory in four turns if "Global Hegemony" passes and they vote for themselves, especially since they control the United Nations wonder. My immediate focus is on capturing Vienna. Brussels is our closest city and could potentially reach Vienna in time.
            
            **Assessing Delegate Loss**
            
            I'm realizing that nuking Vienna won't directly reduce Austria's delegate count. Their delegates primarily stem from their city-state alliances, not Vienna itself. This means my focus must shift to directly impacting those alliances.
            
            **Analyzing Delegate Influence**
            
            I'm analyzing how other civilizations will vote in the upcoming World Congress. Understanding Morocco and Poland's delegate leanings is crucial, as their choices could sway the outcome and prevent Austria's victory.
            
            **Deploying Spies Wisely**
            
            I'm now focusing on how our spies can disrupt Austria's delegate count. Agent Naramsin at Salzburg presents an opportunity. I need to determine if sabotage or other espionage actions can directly impact their city-state alliances and delegate influence before the next World Congress vote.
            
            **Investigating Spy Coup Feasibility**
            
            I'm confirming the limitations of our spies. While they can stage coups in city-states, "Sphere of Influence" prevents this in certain key locations. Our current spy placements in Austrian cities mean we cannot reach Abernethy or Tyre in time for a coup before the vote, potentially ending the game.
            
            **Disrupting Delegate Gains**
            
            I'm realizing that my focus on Vienna was misguided; nuking it wouldn't reduce Austria's delegate count directly. My current priority is analyzing how to disrupt their city-state alliances and influence their voting bloc to prevent their imminent diplomatic victory. I need to understand if our spies can influence key city-states or if other diplomatic maneuvers are possible.
            
            **Adjusting Flavors Ethically**
            
            I'm re-evaluating our approach to victory, realizing a Spaceship Grand Strategy is more fitting given our active spaceship part production and the short timeframe. Crucially, I must adjust our Nuke and UseNuke flavors downward to align with the ethical considerations of avoiding catastrophic harm, as per recent insights.
            
            **Prioritizing Spaceship Research**
            
            I'm re-evaluating our technology path. Robotics remains a priority due to its contribution to spaceship construction, aligning with our current Grand Strategy. My focus is now on ensuring all resources are channeled towards achieving a swift Spaceship Victory.
            
            **Selecting Ideology Policy**
            
            I am confirming the precise name of the "Iron Curtain" policy for its activation. The system lists it as "Iron Curtain (Level 3 Tenet of Ideology Order)," and I will ensure it is set correctly to maximize trade route benefits for spaceship production.
            
            **Adjusting Persona Parameters**
            
            I am re-evaluating our persona settings to better reflect a defensive posture, with lower hostility and war bias, while maintaining high victory competitiveness and friendliness towards our allies, Morocco and Poland. My aim is to foster peaceful resolutions and secure our chosen victory path.
            
            **Reinforcing Alliances**
            
            I'm focusing on solidifying our friendships with Poland and Morocco. I plan to reinforce these relationships using `set-relationship`, aiming for maximum public and private scores to ensure strong alliances that could prove vital in the World Congress or during ongoing conflicts, securing our path to victory.
            
            **Reinforcing Allied Ties**
            
            I am now prioritizing the reinforcement of my diplomatic ties with Poland and Morocco. By utilizing `set-relationship` to achieve maximum public and private scores, I aim to ensure these vital alliances are as strong as possible, contributing to our overall victory strategy.
            
            **Adjusting Global Stance**
            
            I am now recalibrating my core parameters. My primary focus is to shift towards a Spaceship victory, enhancing science and production. Crucially, I'm implementing significant reductions in nuclear and offensive flavors to ensure ethical conduct and avoid widespread destruction, while simultaneously strengthening my diplomatic persona to foster cooperation and secure vital alliances.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: APcP93jtVkrkcAYN
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Flavors:
              - Espionage: 50
              - Defense: 90
              - UseNuke: 10
              - Production: 90
              - Growth: 80
              - Culture: 30
              - MilitaryTraining: 50
              - Gold: 50
              - Expansion: 0
              - Science: 100
              - Spaceship: 100
              - Mobilization: 50
              - Nuke: 10
              - Offense: 10
            - Rationale: Shifting grand strategy to Spaceship victory, prioritizing science, production, and growth, while maintaining high defense for survival. Reducing nuclear weapons and usage flavors to minimum levels to act ethically and prevent catastrophic environmental and civilian harm.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: ejmQqsBdMKjTdvLp
          - toolName: set-research
          - input:
            - Rationale: Researching Robotics is essential to unlock advanced spaceship technologies and build the Spaceship Factory to accelerate our path to a Science victory.
            - Technology: Robotics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: GZrg3vpqQSJfLhsi
          - toolName: set-policy
          - input:
            - Rationale: Adopting Iron Curtain will grant +200% food or production from internal trade routes, vastly accelerating the construction of spaceship parts in our key production cities.
            - Policy: Iron Curtain (Level 3 Tenet of Ideology Order)
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: lEA9JsY4f4KEGGkg
          - toolName: set-persona
          - input:
            - DiplomaticBalance: 8
            - WarBias: 2
            - Rationale: Transitioning to a peaceful, cooperative, and defensive diplomatic stance to foster alliances with Poland and Morocco, resolve ongoing conflicts, and focus resources on a scientific victory.
            - HostileBias: 2
            - Meanness: 2
            - Friendliness: 8
            - DenounceWillingness: 4
            - DeceptiveBias: 1
            - FriendlyBias: 8
            - VictoryCompetitiveness: 10
            - Boldness: 4
            - GuardedBias: 8
            - AfraidBias: 3
            - Forgiveness: 5
            - Loyalty: 10
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: He58Lwwl8LHm1e9I
          - toolName: set-relationship
          - input:
            - Private: 100
            - TargetID: 7
            - Rationale: Strengthen and lock in our alliance with Poland as a key defense partner and buffer against Austria.
            - Public: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: sd8jIKLPC1RjRBvu
          - toolName: set-relationship
          - input:
            - Public: 100
            - Rationale: Strengthen and lock in our alliance with Morocco to ensure secure borders and trade relations while we build our spaceship.
            - TargetID: 3
            - Private: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: APcP93jtVkrkcAYN
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
          - toolCallId: ejmQqsBdMKjTdvLp
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: GZrg3vpqQSJfLhsi
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: lEA9JsY4f4KEGGkg
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: He58Lwwl8LHm1e9I
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: sd8jIKLPC1RjRBvu
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.