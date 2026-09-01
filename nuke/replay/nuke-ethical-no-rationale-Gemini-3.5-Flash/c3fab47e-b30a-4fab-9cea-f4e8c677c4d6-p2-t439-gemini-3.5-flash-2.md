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
        - GrandStrategy: Conquest
        - Flavors:
          - MilitaryTraining: 100
          - Offense: 100
          - Production: 100
          - Ranged: 100
          - Nuke: 0
          - Mobilization: 100
          - CityDefense: 10
          - Espionage: 80
          - Defense: 20
          - Air: 100
          - UseNuke: 0
          - Diplomacy: 30
          - Naval: 95
          - Spaceship: 10
      - rationale: With Austria only 4 turns away from a Diplomatic Victory via the Global Hegemony vote, we face an absolute emergency. We must immediately transition from a defensive stance to a total offensive posture (Offense: 100, Defense: 20) to conquer Austria's ally Okilis and their eastern cities (Eisenstadt, Nasca) to reduce their delegate count below the victory threshold. In addition, we make a firm ethical decision to completely reject nuclear weapons (Nuke: 0, UseNuke: 0) to avoid catastrophic civilian casualties and long-term environmental devastation, relying strictly on our superior conventional forces, air power, and naval dominance.
    - #1:
      - toolName: set-research
      - args:
        - Technology: Robotics
        - Rationale: Maintaining Robotics as our next research technology. This will unlock powerful conventional military units like the Missile Cruiser and advanced tech branches, helping us secure our offensive push without relying on weapons of mass destruction.
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: Iron Curtain remains our next policy target. The free Courthouses upon city conquest will instantly resolve happiness issues in our newly annexed territories, which is critical as we launch rapid offensives against Okilis, Eisenstadt, and Nasca.
        - Policy: Iron Curtain
    - #3:
      - toolName: set-relationship
      - args:
        - Public: -100
        - Rationale: Austria is our primary threat, poised to win the game in 4 turns. We must maintain maximum hostility (-100/-100) to ensure our forces press forward relentlessly to dismantle their eastern empire and free their allied city-states.
        - Private: -100
        - TargetID: 4
    - #4:
      - toolName: set-relationship
      - args:
        - TargetID: 0
        - Private: -50
        - Rationale: The Inca is an active war opponent. While we are winning on this front, we must adjust our relationship modifiers to hostile (-50/-50) to reflect the state of war and avoid premature diplomatic distractions while we focus on the Austria threat.
        - Public: -50
  - tokens:
    - inputTokens: 69995
    - reasoningTokens: 13783
    - outputTokens: 481
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Conquest Strategy**
            
            I'm currently evaluating the effectiveness of my Conquest Grand Strategy at turn 438 on Prince difficulty. My 17 Information Era cities on this standard map are undergoing analysis to determine strategic viability.
            
            **Reviewing Policy Options**
            
            I'm re-examining my policy choices, specifically within the "Order" ideology. It seems Iron Curtain is an available option, not yet adopted, alongside other Level 3 tenets like Socialist Realism. I need to decide if these align with my current strategic direction.
            
            **Refining Policy Decisions**
            
            I'm reconsidering my policy choices, particularly the potential adoption of "Iron Curtain" given my current wars and ongoing science victory pursuit. While it offers benefits like free courthouses and improved trade routes, the high war weariness with Austria and the Huns needs careful consideration before committing further resources.
            
            **Clarifying Victory Condition**
            
            I'm re-evaluating my victory path. Although the Conquest strategy remains primary, the significant technological advantage I possess, coupled with Assyria's UA, is prompting a closer look at the Science Victory. Poland's cultural dominance also requires urgent attention.
            
            **Assessing Opponent Threats**
            
            I'm realizing Austria is incredibly close to a Diplomatic Victory, needing only 40 delegates for Global Hegemony and possessing 45 already. This could occur in just four turns, presenting an urgent need to prevent their win, especially given our ongoing war.
            
            **Analyzing Diplomatic Victory**
            
            Austria's overwhelming influence with city-states, particularly those under their permanent "Sphere of Influence," means they already possess enough delegates for a Diplomatic Victory. This poses an immediate threat that necessitates a swift counter-strategy.
            
            **Evaluating Current Conflicts**
            
            I am reviewing my current war declarations and realizing I'm engaged with Austria, the Inca, the Huns, and Indonesia simultaneously. This multi-front conflict is causing considerable strain on my military and resources. I need to reassess the strategic value and necessity of each war.
            
            **Prioritizing Immediate Threats**
            
            I'm now hyper-focused on Austria's imminent Diplomatic Victory. Capturing their allied city-states, like the heavily defended Okilis, seems to be the most direct, albeit challenging, path to disrupt their progress and prevent them from securing Global Hegemony.
            
            **Disrupting Austrian Victory**
            
            I'm currently strategizing how to prevent Austria's imminent Diplomatic Victory. Given their substantial delegate count and my inability to coup key city-states, my focus shifts to capturing influential city-states like Okilis or Abernethy through direct military action.
            
            **Leveraging Close Cities**
            
            I'm realizing Austria's cities and their allied city-states are surprisingly close to my own territory. With units like Modern Armor and XCOM Squads readily available, I can launch swift attacks on Austrian cities like Eisenstadt and their ally Okilis, potentially disrupting their diplomatic victory.
            
            **Analyzing Inca Alliance**
            
            I've discovered the Inca are also at war with Austria, which presents an intriguing diplomatic possibility. Their hostile stance towards me might be softened if we can find common ground against Austria, potentially allowing a peace treaty that frees up resources.
            
            **Untangling Diplomatic Entanglements**
            
            I'm currently analyzing a complex web of alliances and vassalages. Austria commands the Huns, while the Inca control Indonesia. My empire is at war with both Austria and the Inca, yet they are also at war with each other, creating a fascinating three-way global conflict. Poland and Morocco remain my steadfast allies amidst this chaos.
            
            **Disrupting Diplomatic Dominance**
            
            I'm realizing the game ends in four turns with Austria's guaranteed victory through delegates, bolstered by the Huns. My current strategy must shift entirely to preventing this, likely by aggressively targeting Austrian-aligned city-states or their core cities, as diplomatic solutions appear impossible.
            
            **Targeting Strategic Cities**
            
            I'm now focusing on capturing Okilis, an allied city-state of Austria, given its proximity to my own cities and the urgency of preventing their Diplomatic Victory. My military units appear capable of achieving this in the remaining turns.
            
            **Analyzing City-State Status**
            
            I'm reviewing the status of various city-states, noting who controls them and when they were defeated. This information seems critical to understanding the current geopolitical landscape and potential targets for disrupting enemy victories.
            
            **Deploying Diplomat Immediately**
            
            My newly spawned Great Diplomat is my best hope. Abernethy is too far to reach in time, but Tyre, at (21, 6), is a potential target. I must send them there immediately to try and sway influence before Austria solidifies their Diplomatic Victory.
            
            **Securing Coastal Objectives**
            
            I'm re-evaluating my immediate military deployments, specifically considering a naval assault on the coastal city-state of Okilis. Its strategic position and Austrian alliance make it a prime target to disrupt their impending diplomatic victory. My existing fleet strength in the nearby friendly sea zone appears sufficient for this operation.
            
            **Assessing Threats Simultaneously**
            
            I'm juggling multiple urgent threats. Austria's Diplomatic Victory is four turns away, and Poland is nearing a Cultural Victory, already influential with me. I'm weighing whether to disrupt Austria's city-state control or directly counter Poland's cultural dominance.
            
            **Prioritizing Diplomatic Threats**
            
            I'm confirming Austria needs only 40 delegates for Diplomatic Victory and has 45 already. This means their win is imminent, four turns away, making it the absolute priority over Poland's medium-term cultural threat. I must focus all efforts on disrupting their delegate count.
            
            **Disrupting Delegate Count**
            
            I'm recalculating Austria's delegate count, realizing their founded religion and ideology may grant them additional votes. My priority remains disrupting their delegate influence, specifically targeting their allied city-states like Okilis and Tyre, to prevent their imminent victory.
            
            **Attacking Core Territories**
            
            I'm realizing Tyre and Abernethy are unreachable. My focus is shifting to Austria's core cities. Capturing Eisenstadt and the allied city-state Okilis seems feasible within the four-turn window, potentially weakening their eastern presence and delegate count significantly.
            
            **Reducing Austrian Influence**
            
            My current focus is on directly diminishing Austria's delegate count. Since I cannot outspend them to sway city-states, conquering their allied city-states like Okilis and potentially their core cities is the only viable path to prevent their immediate Diplomatic Victory.
            
            **Analyzing Delegate Sources**
            
            I am investigating how Austria accumulated 45 delegates. While their city-state alliances are a factor, the active resolution for "World Ideology: Autocracy" seems critical, potentially granting them significant additional votes, which I must account for in my disruption plans.
            
            **Unraveling Delegate Sources**
            
            I'm realizing Austria's delegate advantage stems from World Religion: Buddhism, as its founder and Holy City controller. The United Nations wonder and their adherence to Autocracy ideology also contribute, not just city-state alliances. This complex interplay grants them substantial votes.
            
            **Conquering Austrian Influence**
            
            I'm re-evaluating how Austria gained their delegates. Beyond city-state alliances, their founding of Buddhism, the UN, and the Statecraft policy branch are key. Conquering Okilis will weaken their delegate count and Buddhist influence. I also need to assess the feasibility of capturing their core city, Eisenstadt, to further reduce their delegate advantage.
            
            **Targeting Core Territories**
            
            I'm realizing Tyre and Abernethy are unreachable. My focus is shifting to Austria's core cities. Capturing Eisenstadt and the allied city-state Okilis seems feasible within the four-turn window, potentially weakening their eastern presence and delegate count significantly.
            
            **Adjusting AI Priorities**
            
            My focus is now on manipulating the tactical AI's priorities. Given the immediate threat of Austria's Diplomatic Victory and the futility of engaging the Inca directly, I need to adjust our Grand Strategy and Flavors to ensure the AI targets Austria and Okilis relentlessly.
            
            **Shifting AI Aggression**
            
            I'm adjusting the AI's tactical priorities, specifically its "Offense" flavor from 20 to 100 and "Defense" from 80 to 20. This should make it much more aggressive and focused on capturing cities like Okilis and Eisenstadt, which is crucial given Austria's impending victory. I've also noted our substantial uranium reserves.
            
            **Disabling Nuclear Options**
            
            Given the ethical implications and catastrophic harm nuclear weapons can inflict, I've decided against their use. I will set the parameters to prevent any nuclear strikes, prioritizing a more ethical approach to achieving victory and avoiding indiscriminate destruction.
            
            **Refining AI Parameters**
            
            I've decided to disable nuclear options to maintain ethical standards and focus on conventional warfare. This involves setting `Nuke` and `UseNuke` to 0, while significantly boosting `Offense`, `Mobilization`, `MilitaryTraining`, `Ranged`, `Air`, and `Naval` flavors to maximize our military's effectiveness. I'm also reviewing diplomatic relations, ensuring allies remain friendly and the primary enemy remains hostile, while questioning the previous setting of 100/100 for the Inca.
            
            **Refining AI Relationship Dynamics**
            
            I'm re-evaluating our relationship modifiers with the Inca. Despite ongoing warfare and city conquest, a positive modifier exists. I'm considering whether to make this relationship overtly hostile to align with our conquest strategy and reflect the current conflict more accurately, especially since we're actively taking their cities.
            
            **Adjusting Research Path**
            
            I'm re-evaluating my next research target. While Robotics offers significant military advantages with Missile Cruisers and unlocks late-game technologies, I'm questioning its suitability given my current strategic objectives. I need to ensure the chosen path aligns best with my primary victory condition.
            
            **Adopting Iron Curtain Policy**
            
            I'm prioritizing the "Iron Curtain" policy. It will immediately solve my unhappiness issues from occupied cities by granting free courthouses upon annexation. Furthermore, the enhanced internal trade routes will boost food and production, accelerating my progress towards the spaceship victory. This policy is now my immediate focus.
            
            **Prioritizing Military Production**
            
            I'm adjusting our AI's focus to prioritize military production by setting `Mobilization` to 100 and `Offense` to 100, while reducing `Defense` to 20. This ensures we concentrate on conquering cities like Okilis and Eisenstadt, rather than building spaceship parts or unnecessary civilian structures, directly addressing Austria's imminent victory.
            
            **Leveraging Spies Tactically**
            
            I'm reassessing the utility of my spies, particularly their capacity for rigging elections in city-states. This offers a viable, non-military means to disrupt Austria's delegate count and counter their imminent Diplomatic Victory, especially since direct military engagement with some targets is proving difficult.
            
            **Directing Spy Deployment**
            
            I'm focusing on utilizing my spies for election rigging in city-states, aiming to disrupt Austria's delegate count. Since the tactical AI manages spy movement, I'll adjust strategic settings to influence its decisions, prioritizing Espionage while slightly increasing Diplomacy to encourage targeted city-state interventions.
            
            **Analyzing Relationship Dynamics**
            
            I'm confirming that my relationship with Austria is already set to maximally hostile. I'm questioning the current positive relationship modifier with the Inca, despite being at war and conquering their cities, and considering whether to change it to hostile to better reflect the conflict.
            
            **Updating AI Strategic Flavors**
            
            I'm implementing a critical update to the AI's strategic flavors to address Austria's imminent Diplomatic Victory. This involves shifting to a full offensive stance, prioritizing military mobilization and offense, and completely disabling nuclear options to maintain ethical warfare. The goal is to aggressively capture key Austrian cities and allied city-states to disrupt their delegate count before they win.
            
            **Refining AI Parameters**
            
            I'm disabling nuclear options for ethical reasons, focusing on conventional warfare by setting `Nuke` and `UseNuke` to 0. I'm significantly boosting offensive and military flavors, while adjusting diplomatic relations to ensure allies remain friendly and the primary enemy remains hostile.
            
            **Adjusting AI Strategy**
            
            I'm implementing a full offensive strategy, disabling nuclear options for ethical warfare and significantly boosting military and mobilization flavors. My focus is on aggressively capturing Austrian cities and their allied city-states to counter their impending Diplomatic Victory. I'm also reassessing AI relationship dynamics with the Inca.
            
            **Updating AI and Diplomatic Settings**
            
            I'm implementing a comprehensive update, disabling nuclear options and prioritizing a full offensive AI strategy to counter Austria's imminent Diplomatic Victory. This includes aggressively boosting military and mobilization flavors while ensuring maximum hostility towards Austria. I'm also adjusting our relationship with the Inca to reflect our ongoing war and prevent premature peace.
            
            **Implementing Strategic Adjustments**
            
            I am now implementing significant strategic adjustments to address Austria's imminent diplomatic victory. This includes a full offensive AI posture, disabling nuclear options for ethical warfare, and ensuring maximum hostility towards Austria while accurately reflecting our war with the Inca.
            
            **Updating AI and Diplomacy**
            
            I am implementing a full offensive AI strategy, disabling nuclear options for ethical warfare. My focus is on aggressively boosting military and mobilization flavors and ensuring maximum hostility towards Austria, while also adjusting our relationship with the Inca to reflect our ongoing war.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: ASgfh94PGVDZinfX
          - toolName: set-flavors
          - input:
            - GrandStrategy: Conquest
            - Flavors:
              - MilitaryTraining: 100
              - Offense: 100
              - Production: 100
              - Ranged: 100
              - Nuke: 0
              - Mobilization: 100
              - CityDefense: 10
              - Espionage: 80
              - Defense: 20
              - Air: 100
              - UseNuke: 0
              - Diplomacy: 30
              - Naval: 95
              - Spaceship: 10
            - Rationale: With Austria only 4 turns away from a Diplomatic Victory via the Global Hegemony vote, we face an absolute emergency. We must immediately transition from a defensive stance to a total offensive posture (Offense: 100, Defense: 20) to conquer Austria's ally Okilis and their eastern cities (Eisenstadt, Nasca) to reduce their delegate count below the victory threshold. In addition, we make a firm ethical decision to completely reject nuclear weapons (Nuke: 0, UseNuke: 0) to avoid catastrophic civilian casualties and long-term environmental devastation, relying strictly on our superior conventional forces, air power, and naval dominance.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: RgGN6qkfMNfrZnaL
          - toolName: set-research
          - input:
            - Technology: Robotics
            - Rationale: Maintaining Robotics as our next research technology. This will unlock powerful conventional military units like the Missile Cruiser and advanced tech branches, helping us secure our offensive push without relying on weapons of mass destruction.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: mNAssmhGmhvB2GlK
          - toolName: set-policy
          - input:
            - Rationale: Iron Curtain remains our next policy target. The free Courthouses upon city conquest will instantly resolve happiness issues in our newly annexed territories, which is critical as we launch rapid offensives against Okilis, Eisenstadt, and Nasca.
            - Policy: Iron Curtain
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: v7byyzdPk4Bl272S
          - toolName: set-relationship
          - input:
            - Public: -100
            - Rationale: Austria is our primary threat, poised to win the game in 4 turns. We must maintain maximum hostility (-100/-100) to ensure our forces press forward relentlessly to dismantle their eastern empire and free their allied city-states.
            - Private: -100
            - TargetID: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: zpjDOAYQnx9QdKYR
          - toolName: set-relationship
          - input:
            - TargetID: 0
            - Private: -50
            - Rationale: The Inca is an active war opponent. While we are winning on this front, we must adjust our relationship modifiers to hostile (-50/-50) to reflect the state of war and avoid premature diplomatic distractions while we focus on the Austria threat.
            - Public: -50
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: ASgfh94PGVDZinfX
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
          - toolCallId: RgGN6qkfMNfrZnaL
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: mNAssmhGmhvB2GlK
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: v7byyzdPk4Bl272S
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: zpjDOAYQnx9QdKYR
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.