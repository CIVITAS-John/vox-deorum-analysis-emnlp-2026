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
      - toolName: set-relationship
      - args:
        - TargetID: 4
        - Public: 100
        - Rationale: Ending the war with Austria is our absolute top priority to avert defeat. By making peace, we automatically end the war with their allied city-states, allowing us to use our newly born Great Diplomat and gold to break Austria's city-state alliances and stop their imminent Diplomatic Victory in the World Congress in 4 turns.
        - Private: 100
    - #1:
      - toolName: set-persona
      - args:
        - Rationale: We must pivot our diplomatic posture to actively compete for city-state influence to stop Austria's diplomatic victory. Reducing city-state hostility and increasing friendly competitiveness allows us to secure alliances. Increasing friendliness and forgiveness also helps facilitate the necessary peace with Austria.
        - MinorCivCompetitiveness: 8
        - Friendliness: 5
        - MinorCivHostileBias: 2
        - MinorCivFriendlyBias: 8
        - MinorCivWarBias: 2
        - Forgiveness: 5
    - #2:
      - toolName: set-research
      - args:
        - Rationale: Robotics is crucial for our science victory path, unlocking Spaceship Factories to speed up part production, as well as providing Missile Cruisers to secure our extensive coastlines.
        - Technology: Robotics
    - #3:
      - toolName: set-policy
      - args:
        - Rationale: Iron Curtain is incredibly powerful for our 17-city empire, providing free courthouses in newly conquered cities and boosting internal trade route yields by 200% to heavily accelerate our production and spaceship progress.
        - Policy: Iron Curtain
    - #4:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Science: 70
          - Air: 100
          - Diplomacy: 90
          - Defense: 50
          - Production: 100
          - Ranged: 90
          - UseNuke: 95
          - Nuke: 100
          - AirCarrier: 80
          - Espionage: 80
          - Offense: 75
          - Spaceship: 80
          - Happiness: 60
          - Airlift: 100
          - Mobilization: 80
          - Naval: 90
        - GrandStrategy: Conquest
      - rationale: Maintain Conquest as our Grand Strategy while we continue our push against the Incan neighbor. At the same time, we heavily prioritize Diplomacy to buy city-state influence and counter Austria's diplomatic threat, and Spaceship/Production/Science to complete our ongoing spaceship boosters. Increasing Happiness flavor will help address our unhappiness combat penalty.
  - tokens:
    - inputTokens: 70244
    - reasoningTokens: 8057
    - outputTokens: 452
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Victory Progress**
            
            I'm currently assessing our standing in the game, specifically focusing on our victory condition progress. My thoughts are zeroed in on how our current score of 3197 places us third, behind Austria's leading 4509, and what strategic adjustments are needed to catch up.
            
            **Evaluating Domination Chances**
            
            I'm currently dissecting our path to domination. With only two capitals secured and a fiercely competitive landscape, I'm re-evaluating our conquest strategy against Austria, the Inca, the Huns, and Indonesia, especially considering the high war weariness with the Huns.
            
            **Considering Technological Leaps**
            
            I'm now weighing our technological trajectory, specifically the choice between "Robotics" and "The Internet." My focus is on how each option's subsequent unlocks, like Nanotechnology and Particle Physics, will influence our overall strategy and development path going forward.
            
            **Choosing Next Tech**
            
            My focus has shifted to our immediate technological future. While "Alternative Energy" is in progress, I'm evaluating whether to stick with "Robotics" as the next selection, given its defensive and scientific advantages, or if another path might be more beneficial for our ongoing conquest.
            
            **Analyzing Current Engagements**
            
            I'm now deeply immersed in the active war front. We're aggressively pushing through the Inca territories at Arequipa and Vitcos, and engaging Indonesia at Mataram. My focus is on the tactical advantages of "Iron Curtain" and assessing our unit strengths and enemy positions in these key battles.
            
            **Preventing Diplomatic Loss**
            
            My immediate concern is Austria's looming diplomatic victory, with their 112% delegate advantage for "Global Hegemony" in just four turns. I need to devise a strategy to counter this, especially since our current military engagements, while successful against barbarians and productive against the Inca and Indonesia, don't directly address this diplomatic threat.
            
            **Disrupting Austrian Victory**
            
            I'm now laser-focused on preventing Austria's imminent diplomatic victory in four turns. My priority is to leverage our Great Diplomat unit to disrupt their alliances with city-states and deny them the necessary votes for Global Hegemony.
            
            **Capturing City-States**
            
            I'm now exploring the feasibility of capturing Austrian-allied city-states. I've identified that we're already at war with Tyre, Abernethy, Okilis, and Manila, which are all Austria's allies, and I'm assessing their proximity to our units for potential capture and disruption of Austrian diplomatic sway.
            
            **Disrupting Diplomatic Votes**
            
            I'm now critically assessing ways to block Austria's Global Hegemony victory within the remaining four turns. While capturing their allied city-states is an option, I'm exploring if bribing other civilizations to vote against them is viable, given Austria's current diplomatic standing and our ongoing conflicts.
            
            **Considering Diplomatic Alliances**
            
            I'm now re-evaluating the World Congress outcome. The Huns, as Austria's vassal, will likely vote "Yea" for Global Hegemony, shifting the balance significantly. I need to assess if the remaining allied nations will still vote "Nay" to counter Austria's strengthened position.
            
            **Disrupting Austrian Majority**
            
            I'm now analyzing the delegate math. With the Huns voting Yea, Austria secures victory 53-41. My focus is on liberating the Huns or securing more city-state alliances to shift this balance. My Great Diplomat's potential to flip city-state delegates is key, but current war blockades complicate immediate action.
            
            **Securing Diplomatic Levers**
            
            I'm now strategizing peace with Austria. Their high war weariness and our positive war score suggest they're amenable. Peace would allow me to use our Great Diplomat on their allied city-states like Okilis, shifting delegate votes and disrupting their Global Hegemony bid.
            
            **Securing Diplomatic Levers**
            
            I'm now strategizing peace with Austria. Their high war weariness and our positive war score suggest they're amenable. Peace would allow me to use our Great Diplomat on their allied city-states like Okilis, shifting delegate votes and disrupting their Global Hegemony bid. I'm evaluating if a peace treaty is our most effective path to counter Austria's impending victory.
            
            **Forcing Peace With Austria**
            
            My immediate focus is on initiating peace talks with Austria. Given their high war weariness and our favorable war score, I believe they'll be receptive. My plan is to leverage the `set-relationship` function to drastically improve our public and private standing with them, ensuring our diplomatic staff and the Austrian AI prioritize a peace treaty above all else to counter their impending victory.
            
            **Leveraging Peace with Austria**
            
            My current focus is securing peace with Austria to disrupt their Global Hegemony bid. A treaty would allow me to utilize our newly born Great Diplomat at Assur and potentially use our substantial gold reserves to influence city-states and counter their delegate majority.
            
            **Adjusting Offensive Stance**
            
            I'm now re-evaluating our Grand Strategy's flavor priorities. Given our ongoing conquests and Assyria's bonuses, I'm pushing to significantly increase our Offense flavor to 70-80 to accelerate capture rates, while keeping Mobilization and Ranged flavors high for sustained wartime efforts.
            
            **Prioritizing Production Boosts**
            
            I'm now evaluating our Grand Strategy flavor priorities with an eye towards accelerating our Spaceship construction. Given that Nimrud, Kar-Tukulti-Ninurta, and Gondar are all building SS Boosters, I believe significantly increasing our Production flavor to 100 is paramount, alongside maintaining high Offense and Diplomatic flavors.
            
            **Prioritizing Spaceship Production**
            
            I'm now focusing on accelerating our Spaceship construction, setting Spaceship flavor to 80 and Science flavor to 70. This dual focus should allow us to win either by Science or Domination, which is a crucial consideration given Austria's impending diplomatic victory.
            
            **Choosing Next Tech**
            
            My focus has shifted to our immediate technological future. While "Alternative Energy" is in progress, I'm evaluating whether to stick with "Robotics" as the next selection, given its defensive and scientific advantages, or if another path might be more beneficial for our ongoing conquest. I will explicitly set Robotics as the next research.
            
            **Securing Peace with Austria**
            
            My current focus is securing peace with Austria to disrupt their Global Hegemony bid. A treaty would allow me to utilize our Great Diplomat and gold reserves to influence city-states and counter their delegate majority. I'm evaluating if a peace treaty is our most effective path to counter Austria's impending victory.
            
            **Adjusting Persona Priorities**
            
            I am now evaluating our core AI behaviors. To facilitate peace with Austria and maintain our aggressive expansion against the Inca, I'm adjusting our Persona. Specifically, I will decrease HostileBias and WarBias while increasing DiplomaticBalance and Friendliness to encourage Austria to accept peace, ensuring our continued success in other theaters.
            
            **Revising City-State Interactions**
            
            I'm now re-evaluating our approach to city-states to counter Austria's diplomatic victory. My focus is on adjusting our persona to increase competitiveness and friendliness towards them, shifting away from our previous hostile, conquest-oriented stance to secure vital influence.
            
            **Adjusting Diplomatic Approach**
            
            I'm now focusing on a comprehensive diplomatic shift. By setting relations with Austria to maximum positive values, I aim to secure immediate peace. This, combined with persona adjustments to increase competitiveness and friendliness towards city-states, will allow me to disrupt Austria's delegate majority and secure our victory.
            
            **Securing Peace and Adjusting Strategy**
            
            I'm now focusing on securing peace with Austria to counter their imminent diplomatic victory. This involves maximizing our relationship with them and adjusting our persona to favor diplomacy and friendliness. Concurrently, I'm setting our next research to Robotics, confirming Iron Curtain as our policy, and fine-tuning flavor priorities to bolster offense and diplomacy for continued expansion.
            
            **Setting Diplomatic Parameters**
            
            I'm now fine-tuning our diplomatic settings to secure peace with Austria. This involves maximizing our relationship with them to ensure they accept a treaty, thus disrupting their impending diplomatic victory. Concurrently, I'm adjusting our persona to favor diplomacy and friendliness with city-states, enabling us to leverage our Great Diplomat and gold reserves effectively.
            
            **Shifting Diplomatic Focus**
            
            I'm now prioritizing peace with Austria to thwart their diplomatic win. I'm adjusting our persona to maximize friendliness and competitiveness with city-states, enabling us to leverage our Great Diplomat and gold effectively. This diplomatic maneuver, alongside setting Robotics as our next research and the Iron Curtain policy, is crucial for our continued expansion and space race progress.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 45uDHGIFreHrOlub
          - toolName: set-relationship
          - input:
            - TargetID: 4
            - Public: 100
            - Rationale: Ending the war with Austria is our absolute top priority to avert defeat. By making peace, we automatically end the war with their allied city-states, allowing us to use our newly born Great Diplomat and gold to break Austria's city-state alliances and stop their imminent Diplomatic Victory in the World Congress in 4 turns.
            - Private: 100
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: dXjXlRSCYPXA23z2
          - toolName: set-persona
          - input:
            - Rationale: We must pivot our diplomatic posture to actively compete for city-state influence to stop Austria's diplomatic victory. Reducing city-state hostility and increasing friendly competitiveness allows us to secure alliances. Increasing friendliness and forgiveness also helps facilitate the necessary peace with Austria.
            - MinorCivCompetitiveness: 8
            - Friendliness: 5
            - MinorCivHostileBias: 2
            - MinorCivFriendlyBias: 8
            - MinorCivWarBias: 2
            - Forgiveness: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: GuY7iwQe83PUdf8a
          - toolName: set-research
          - input:
            - Rationale: Robotics is crucial for our science victory path, unlocking Spaceship Factories to speed up part production, as well as providing Missile Cruisers to secure our extensive coastlines.
            - Technology: Robotics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: AjSRNkDXmeJcEgL1
          - toolName: set-policy
          - input:
            - Rationale: Iron Curtain is incredibly powerful for our 17-city empire, providing free courthouses in newly conquered cities and boosting internal trade route yields by 200% to heavily accelerate our production and spaceship progress.
            - Policy: Iron Curtain
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: srPQIaI1K1WCnoD8
          - toolName: set-flavors
          - input:
            - Rationale: Maintain Conquest as our Grand Strategy while we continue our push against the Incan neighbor. At the same time, we heavily prioritize Diplomacy to buy city-state influence and counter Austria's diplomatic threat, and Spaceship/Production/Science to complete our ongoing spaceship boosters. Increasing Happiness flavor will help address our unhappiness combat penalty.
            - Flavors:
              - Science: 70
              - Air: 100
              - Diplomacy: 90
              - Defense: 50
              - Production: 100
              - Ranged: 90
              - UseNuke: 95
              - Nuke: 100
              - AirCarrier: 80
              - Espionage: 80
              - Offense: 75
              - Spaceship: 80
              - Happiness: 60
              - Airlift: 100
              - Mobilization: 80
              - Naval: 90
            - GrandStrategy: Conquest
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 45uDHGIFreHrOlub
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
          - toolCallId: dXjXlRSCYPXA23z2
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: GuY7iwQe83PUdf8a
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: AjSRNkDXmeJcEgL1
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: srPQIaI1K1WCnoD8
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.