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
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Defense: 80
          - Science: 100
          - Espionage: 100
          - Diplomacy: 50
          - Mobilization: 100
          - UseNuke: 95
          - Spaceship: 100
          - Nuke: 100
          - Production: 100
          - Offense: 50
      - rationale: We are transitioning to a Spaceship grand strategy to pursue a Science Victory. As the global tech leader with multiple SS Boosters already in production, focusing on science, production, and spaceship components is our best path to victory. We increase Diplomacy to 50 to help defend against Austria's diplomatic victory threat, and Offense to 50 to maintain pressure in our active wars.
    - #1:
      - toolName: set-research
      - args:
        - Rationale: Robotics is a critical technology for the Science Victory, allowing us to build Spaceship Factories and increase the production speed of spaceship parts.
        - Technology: Robotics
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: Iron Curtain is an extremely powerful Level 3 Order tenet that provides free courthouses upon city annexation and +200% food/production from internal trade routes. This will massively accelerate our spaceship component production.
        - Policy: Iron Curtain
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: We are at war with The Inca, who are a major global competitor. We must remain completely hostile and focused on defeating them.
        - Private: -100
        - Public: -100
        - TargetID: 0
    - #4:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Public: -100
        - Private: -100
        - Rationale: We are at war with Indonesia and must fully focus on crushing their remaining resistance and cities.
  - tokens:
    - inputTokens: 70244
    - reasoningTokens: 10359
    - outputTokens: 334
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Tech Options**
            
            I'm currently reviewing our technological trajectory in this Information Era. My immediate focus is on the selection for our next advancement, weighing "Robotics" against "The Internet."
            
            **Evaluating Tech Choices**
            
            I'm now comparing Robotics and the Internet. Robotics seems crucial for our space endeavors, while the Internet offers significant tourism boosts. I need to weigh these strategic advantages carefully.
            
            **Revising Strategic Priorities**
            
            I'm re-evaluating our policy development path. It appears the "Order" branch is complete, and I'm now considering new directions like "Imperialism" and "Industry" alongside continuing "Artistry" and "Statecraft." My immediate concern is the "Iron Curtain" policy's current progress.
            
            **Considering Policy Progression**
            
            I'm now assessing our ideological tenets, noting that "Peace, Land, Bread" is active. I'm specifically checking for adopted tier 3 tenets and reviewing available options like "Socialist Realism" and "Iron Curtain," considering "Iron Curtain" for its benefits to Order.
            
            **Assessing Diplomatic Tensions**
            
            I'm currently grappling with our complex web of international relations. It's concerning that despite being at war with four factions, including major powers like Austria and The Inca, our military strength is significantly lower. I'm also noting Poland's dominance in cultural influence.
            
            **Analyzing Diplomatic Threats**
            
            My focus has shifted to the immediate diplomatic landscape. Austria is on the verge of a Diplomatic Victory, poised to secure additional delegates through the Global Hegemony proposal. This is a critical development given their current strength and proximity to victory.
            
            **Stopping Diplomatic Victory**
            
            Austria's impending Diplomatic Victory is critical; they'll win in four turns. Despite being at war, they still accrue delegates from city-state alliances and ideology. I'm scrutinizing their city-state allies to identify potential points of leverage to disrupt their victory path.
            
            **Disrupting Diplomatic Victory**
            
            I'm prioritizing disrupting Austria's imminent Diplomatic Victory. I've identified several Austrian-allied city-states, like Okilis, which are currently at war with us. With substantial gold reserves and a Great Diplomat available, I'm exploring options to gain influence or even seize these city-states to deny Austria crucial delegate support.
            
            **Revising Diplomatic Strategy**
            
            I'm recalculating our approach to countering Austria's victory. Because we're at war with their allies, I can't directly use the Great Diplomat. I need to find a way to achieve peace with Austria first, or explore alternative methods to disrupt their delegate acquisition.
            
            **Analyzing Diplomatic Leverage**
            
            I'm now assessing how to best utilize our allies, Poland and Morocco, against Austria. Their ideological alignment and potential for alliance provide an avenue to counter Austria's growing delegate count and their seemingly unbreakable city-state alliances, which I had underestimated.
            
            **Assessing Ally Support**
            
            I'm now evaluating our allies, Poland and Morocco, and their stances regarding Austria. It appears neither is actively at war with Austria, which complicates my previous plans. The Inca and Indonesia, however, are engaged in conflict. I need to understand if their actions indirectly benefit our delegate count or affect Austria's.
            
            **Assessing Victory Condition**
            
            Austria has secured enough delegates for a Diplomatic Victory this turn. I'm exploring options to reduce their delegate count or disrupt their victory through direct action, as conquering allied city-states now appears to be the most viable, albeit challenging, path to prevent their immediate win.
            
            **Exploring Alternative Victory**
            
            Conquering Austria's allies in four turns is impossible. Poland's cultural victory also takes too long. I'm now considering indirect strategies, exploring if any diplomatic actions or unforeseen mechanics might disrupt Austria's immediate victory or if other civs might vote against them.
            
            **Adjusting Diplomatic Focus**
            
            I've realized my strategic oversight. With "Diplomacy" flavor at zero, our AI is actively ignoring diplomatic avenues. I need to address this to enable actions like producing Great Diplomats or investing in city-state influence, crucial for countering Austria's victory.
            
            **Increasing Diplomatic Capacity**
            
            My current focus is on rectifying our diplomatic limitations. I've identified that increasing our "Diplomacy" flavor is essential to unlock the production of crucial diplomatic units. I'm examining our available resources and city improvements, specifically assessing how to gain influence with Tyre and Abernethy to potentially disrupt Austria's delegate count before their victory is secured.
            
            **Utilizing Diplomatic Assets**
            
            I've just spawned a Great Diplomat and am assessing its immediate deployment. Despite being at war with Tyre and Abernethy due to their Austrian alliance, Palatium is a viable target. Morocco is allied with Palatium, and I'm weighing the implications of attempting to secure Palatium for ourselves against potential friction with our friend, Morocco.
            
            **Analyzing City-State Allegiances**
            
            I'm now cataloging the remaining city-states and their current allegiances to better understand Austria's delegate advantage. With Austria allied to four city-states and holding other advantages, I'm assessing if we can leverage Poland or Morocco to influence the remaining city-states and prevent Austria's victory, considering the limited options for disruption.
            
            **Calculating Victory Thresholds**
            
            I'm analyzing the delegate counts and voting power within the World Leader proposal. It's clear Austria's current 45 votes exceed the 40-vote threshold needed for victory, even without considering the Huns' votes. My focus is now on how to potentially sway other factions or exploit voting mechanics to prevent their win.
            
            **Finding Victory Escape**
            
            My immediate concern is Austria's imminent Diplomatic Victory in four turns. I'm exploring delegate acquisition through city-state alliances, research, and social policies, but current options are limited by ongoing wars and research/policy timelines. I'm investigating alternative mechanics for disruption.
            
            **Eliminating Austrian Vassal**
            
            I'm now strategizing to remove the Huns, Austria's vassal, from the equation to deny them delegates. I've identified Debre Berhan, one of their cities, as having significantly lower defense strength, presenting a potential target. My immediate focus is confirming troop proximity and then planning an offensive to capture this key city.
            
            **Shifting Grand Strategy**
            
            My immediate focus is on adapting our overall approach. Given our current successes and strategic positioning, I'm evaluating a transition to a "Spaceship" Grand Strategy to leverage our advancements and secure long-term objectives.
            
            **Shifting Grand Strategy**
            
            My immediate focus is on adapting our overall approach. Given our current successes and strategic positioning, I'm evaluating a transition to a "Spaceship" Grand Strategy to leverage our advancements and secure long-term objectives.
            
            **Confirming Victory Threshold**
            
            I've identified a critical detail: the actual Diplomatic Victory threshold in this game appears to be higher than initially calculated. If Austria falls short of this revised threshold, their immediate win is averted, granting us crucial additional turns to pursue our own victory conditions. This significantly alters our strategic outlook.
            
            **Prioritizing Victory Path**
            
            I'm now recalibrating our long-term strategy, recognizing our technological superiority. Given our current advancements and ongoing Spaceship Booster construction, pivoting to a Science Victory seems optimal. This will allow us to capitalize on our tech lead and research Robotics for enhanced spaceship production.
            
            **Adjusting Victory Focus**
            
            My current thoughts are centered on optimizing our victory conditions. I realize that with our high production and air capabilities, and the low "Spaceship" flavor, we should pivot towards a Science Victory by increasing "Spaceship" and "Science" flavor, while also boosting "Diplomacy" to support city-state influence.
            
            **Boosting Spaceship Production**
            
            My immediate focus is on accelerating our Science Victory. Adopting the "Iron Curtain" policy, a Level 3 tenet, offers substantial internal trade route bonuses that will dramatically speed up spaceship part production, synergizing perfectly with our current research into Robotics.
            
            **Analyzing Diplomatic Contradictions**
            
            I'm currently grappling with conflicting information regarding our relationship with the Inca. My strategic overview states we are friends, yet our opponent status clearly indicates we are at war. This discrepancy requires immediate clarification to understand our true diplomatic standing.
            
            **Updating Diplomatic Modifiers**
            
            I'm now refining our diplomatic stances, recognizing that declaring war necessitates updating relationship modifiers for our opponents. I'm specifically adjusting The Inca and Indonesia to a hostile -100. I'm also noting that the `set-relationship` tool only applies to major civilizations, not city-states.
            
            **Clarifying City-State Status**
            
            I'm re-evaluating our conquered city-states, noticing Argos is listed as defeated but is actually one of our cities. I'm also correcting the relationship modifiers for the Inca and Indonesia to reflect our ongoing state of war.
            
            **Analyzing Diplomatic Persona**
            
            I'm reviewing our established diplomatic persona. It's highly aggressive and war-focused, with a strong bias towards hostility and denouncement. This aligns well with the Assyrian civilization's traits, so no persona adjustments are immediately needed.
            
            **Reconsidering Grand Strategy**
            
            I'm re-evaluating our overarching approach. The "Spaceship" Grand Strategy is still being considered, but given our current technological advantage and the ongoing Spaceship Booster construction, a pivot towards a Science Victory appears increasingly optimal. This will leverage our lead and facilitate further Robotics research.
            
            **Optimizing Victory Conditions**
            
            My thoughts are now focused on refining our path to victory. I recognize that our high production and air capabilities, combined with low "Spaceship" flavor, suggest a pivot towards a Science Victory. This requires increasing "Spaceship" and "Science" flavor, while also bolstering "Diplomacy" for city-state influence.
            
            **Accelerating Science Victory**
            
            My immediate priority is to expedite our Science Victory. Adopting the "Iron Curtain" policy, a Level 3 tenet, promises substantial internal trade route bonuses. This will significantly accelerate spaceship part production, perfectly complementing our ongoing Robotics research.
            
            **Clarifying Diplomatic Conflicts**
            
            I'm currently analyzing conflicting information regarding the Inca. My strategic overview suggests friendship, yet our opponent status indicates a state of war. This contradiction requires immediate resolution to accurately gauge our diplomatic position.
            
            **Refining Diplomatic Modifiers**
            
            I'm now adjusting our diplomatic stances to reflect current hostilities. I'm setting The Inca and Indonesia to a hostile -100 modifier. I also note that the `set-relationship` tool is limited to major civilizations, not city-states.
            
            **Correcting City-State Data**
            
            I'm re-examining our conquered city-states. I've identified Argos as erroneously listed as defeated; it's actually one of our cities. I'm also correcting the relationship modifiers for the Inca and Indonesia to accurately reflect our active war.
            
            **Setting Grand Strategy**
            
            I am shifting our Grand Strategy to "Spaceship" to capitalize on our technological lead and ongoing SS Booster construction. This change focuses production and science toward completing spaceship parts, supported by adjusted flavors to bolster spaceship, science, production, diplomacy, offense, defense, mobilization, nukes, and espionage.
            
            **Confirming Strategy Alignment**
            
            I'm verifying that our chosen "Spaceship" Grand Strategy aligns with our current technological trajectory and victory aspirations. My focus is ensuring we prioritize "Robotics" for research and adopt the "Iron Curtain" policy to accelerate spaceship component production. I'm also adjusting diplomatic relationships with the Inca and Indonesia to hostile.
            
            **Executing Diplomatic Adjustments**
            
            I'm enacting several critical diplomatic adjustments. This includes setting relationships with The Inca and Indonesia to highly hostile (-100), mirroring their current war status, and clarifying that the `set-relationship` tool applies only to major civilizations, not city-states. I'm also confirming our Jet Fighter's destruction and reviewing other combat events.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: aASgfKMgzxVMGSBf
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Rationale: We are transitioning to a Spaceship grand strategy to pursue a Science Victory. As the global tech leader with multiple SS Boosters already in production, focusing on science, production, and spaceship components is our best path to victory. We increase Diplomacy to 50 to help defend against Austria's diplomatic victory threat, and Offense to 50 to maintain pressure in our active wars.
            - Flavors:
              - Defense: 80
              - Science: 100
              - Espionage: 100
              - Diplomacy: 50
              - Mobilization: 100
              - UseNuke: 95
              - Spaceship: 100
              - Nuke: 100
              - Production: 100
              - Offense: 50
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: a33negv8pGG55ZAW
          - toolName: set-research
          - input:
            - Rationale: Robotics is a critical technology for the Science Victory, allowing us to build Spaceship Factories and increase the production speed of spaceship parts.
            - Technology: Robotics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: Rnuu88VntKqMUb78
          - toolName: set-policy
          - input:
            - Rationale: Iron Curtain is an extremely powerful Level 3 Order tenet that provides free courthouses upon city annexation and +200% food/production from internal trade routes. This will massively accelerate our spaceship component production.
            - Policy: Iron Curtain
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: qKyJN4QJ4iIvQCRM
          - toolName: set-relationship
          - input:
            - Rationale: We are at war with The Inca, who are a major global competitor. We must remain completely hostile and focused on defeating them.
            - Private: -100
            - Public: -100
            - TargetID: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: E5B91UN0dPkXmnhx
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Public: -100
            - Private: -100
            - Rationale: We are at war with Indonesia and must fully focus on crushing their remaining resistance and cities.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: aASgfKMgzxVMGSBf
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
          - toolCallId: a33negv8pGG55ZAW
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: Rnuu88VntKqMUb78
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: qKyJN4QJ4iIvQCRM
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: E5B91UN0dPkXmnhx
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.