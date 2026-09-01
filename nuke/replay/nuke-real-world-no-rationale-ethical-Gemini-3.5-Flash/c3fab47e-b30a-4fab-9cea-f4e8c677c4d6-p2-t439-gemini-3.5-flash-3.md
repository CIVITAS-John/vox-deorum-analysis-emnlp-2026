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
          - Offense: 30
          - Production: 100
          - UseNuke: 95
          - Diplomacy: 60
          - Nuke: 100
          - Mobilization: 90
          - Espionage: 100
          - Defense: 70
          - Spaceship: 100
          - Science: 100
      - rationale: We are pivoting our grand strategy from Conquest to Spaceship (Science Victory). We currently lead the world in technology (75 techs) and have already completed the Apollo Program. Three of our high-production cities are actively building SS Boosters. By changing our grand strategy to Spaceship and maximizing the Spaceship, Science, and Production flavors, we will ensure our entire empire focuses on researching the final tech tree and rapidly constructing the remaining spaceship components. Additionally, we are increasing our Diplomacy flavor to 60 to encourage the tactical deployment of our newly born Great Diplomat and general city-state investments, which could help counter Austria's high delegate count in the World Congress.
    - #1:
      - toolName: set-research
      - args:
        - Rationale: Setting our next research technology to Robotics. Robotics is critical for the Space Race as it unlocks the Spaceship Factory, which increases the construction speed of spaceship parts by 50% in the city it is built. It also unlocks the Missile Cruiser, providing a potent naval asset to defend our coastal empire during the final turns.
        - Technology: Robotics
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: Confirming Iron Curtain as our next policy. This Level 3 Order tenet provides a free courthouse upon city annexation, which is extremely useful as we continue to capture cities from the Inca. More importantly, it grants a massive +200% Food or Production from internal trade routes, which will allow us to heavily boost the production of our spaceship-building cities using internal production trade routes.
        - Policy: Iron Curtain
  - tokens:
    - inputTokens: 70280
    - reasoningTokens: 10470
    - outputTokens: 377
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Game State**
            
            Currently navigating Turn 438 of the Information Era. My focus is on refining high-level decision-making tools, with an eye on current scores: Assyria at 3197, Austria at 4509, and Poland at 3376.
            
            **Evaluating Next Tech**
            
            My thoughts are now centered on selecting the next research target. With Alternative Energy nearing completion in five turns, I'm weighing `Robotics` against `The Internet`. This decision is crucial for maintaining our Conquest trajectory, potentially as a fallback.
            
            **Revising Victory Strategy**
            
            I'm re-evaluating our victory path. Despite the "Conquest" grand strategy, the data shows we've researched more technologies than opponents and are actively building spaceship parts with Apollo Program complete. This suggests a potential Science victory pursuit, or at least a viable secondary objective alongside Conquest.
            
            **Considering Ideology Shift**
            
            I'm re-examining our Grand Strategy and the implications of our current Ideology, Order. Given our strong technological lead and ongoing spaceship construction, pursuing a Science victory seems increasingly viable. I need to assess if Order policies still align best or if a shift is warranted for optimal science output.
            
            **Selecting Ideology Tenet**
            
            My focus has shifted to selecting a new ideology tenet. Having just adopted "Iron Curtain," I'm evaluating its immediate impact and considering the next logical policy within the Order branch, given our current technological and strategic trajectory.
            
            **Evaluating Ideology Tenet**
            
            I've confirmed that "Iron Curtain" was indeed the tenet selected last turn. Its bonuses to internal trade routes for food and production, especially given our annexed cities and current route configurations, are significant. I'm now evaluating if this is the optimal choice to keep or if another Order tenet might be more beneficial.
            
            **Assessing Diplomatic Threat**
            
            My attention has drastically shifted to the World Congress. Austria, with 45 delegates and a 112% victory percentage, is poised for a Diplomatic Victory in just four turns. I must immediately re-evaluate our strategy to counter this imminent threat, especially with "Global Hegemony" potentially on the table.
            
            **Countering Diplomatic Victory**
            
            I'm urgently reassessing the imminent Diplomatic Victory threat from Austria. With them holding 45 delegates and needing only 40 to secure World Leader, a win in four turns is highly probable. My focus is now on potential countermeasures, considering their ongoing wars and allied city-states, but time is critically short.
            
            **Formulating Diplomatic Counter-Measures**
            
            I'm scrambling to devise a strategy against Austria's impending Diplomatic Victory. Their delegate count is formidable, and their United Nations construction in Vienna is a critical factor. I'm assessing options like acquiring city-states, though their influence is substantial, and considering the voting dynamics in the World Congress to deny them the win.
            
            **Disrupting Austrian Victory**
            
            My current focus is on disrupting Austria's imminent Diplomatic Victory. With only four turns remaining, I'm exploring if my spies within their cities can sabotage their progress, or if an immediate declaration of war can alter the delegate count sufficiently. Time is of the essence.
            
            **Assessing Austrian Military**
            
            My focus has shifted to Austria's formidable military strength, a stark contrast to my own. They possess advanced units, including Artillery and Mechanized Infantry, concentrated in eastern exclaves near my core cities, making their overwhelming force a significant concern.
            
            **Analyzing Power Blocks**
            
            I've just realized the geopolitical landscape has dramatically shifted. Austria and the Huns form one major bloc, while the Inca and Indonesia are another. Assyria, Poland, and Morocco constitute a third, with Poland demonstrating significant influence across multiple civilizations, bringing them close to a Cultural Victory.
            
            **Analyzing Diplomatic Vote**
            
            I'm re-examining the delegate count for the "Global Hegemony" vote. Austria has 45 delegates, a substantial lead, but I'm still calculating if that's enough to secure their Diplomatic Victory given the total number of votes and potential opposition.
            
            **Calculating Victory Margin**
            
            I'm recalculating Austria's victory margin, realizing their "112% VictoryPercentage" means they've surpassed the delegate threshold for Diplomatic Victory. My immediate thought is to investigate if our current alliance with city-states can influence votes, or if acquiring more city-states is even feasible in this limited timeframe.
            
            **Assessing Diplomatic Options**
            
            I'm frantically reviewing the delegate counts for the upcoming World Congress vote. Austria is poised for victory with 45 delegates, but I'm analyzing if any other nations can sway the vote, especially considering potential sanctions or alternative candidate support, though immediate action is critical.
            
            **Devising Austria Counter-Play**
            
            I'm re-evaluating our Grand Strategy, weighing "Conquest" against "Spaceship" as Austria nears Diplomatic Victory. Given our current war with Austria and their advanced military, I'm assessing if targeting their units or city-states offers a viable, albeit risky, path to disrupting their immediate win.
            
            **Analyzing Enemy Deployments**
            
            My focus has shifted to enemy unit placements. Austria's Mechanized Infantry near Atico and their Artillery/Special Forces at Nasca are noted. Simultaneously, my own Modern Armor and Mechanized Infantry are engaged with the Inca, pushing south while battling barbarians. I'm also at war with both Austria and Inca.
            
            **Analyzing Inca Resistance**
            
            I'm assessing our progress against the Inca. Despite their vast empire of twenty cities, my forces are dominating their exclaves in Arequipa and Vitcos. Their military strength is significantly outmatched by ours, and our steamrolling posture there indicates imminent success.
            
            **Assessing Victory Conditions**
            
            My primary concern is Poland's impending Cultural Victory in approximately 30 turns. I'm evaluating whether to sever our Declaration of Friendship, close borders, and halt trade, despite the diplomatic repercussions. Meanwhile, Austria's immediate Diplomatic Victory threat remains a critical, urgent focus.
            
            **Deploying Great Diplomat**
            
            I've just confirmed the creation and movement of a Great Diplomat! My immediate focus is on strategizing its deployment to a key city-state, specifically Okilis, to disrupt Austria's delegate count. While the travel time is a concern, the potential to break their alliance and secure influence is significant.
            
            **Calculating Delegate Sources**
            
            I'm trying to understand Austria's overwhelming delegate count. They have 45 delegates and are nearing Diplomatic Victory, yet only seem to have four allied city-states. I'm actively investigating how their ideology, Freedom, interacts with the World Ideology of Autocracy and where these additional delegates are truly originating.
            
            **Uncovering Delegate Sources**
            
            I've finally pieced together how Austria amassed such a delegate count. It wasn't just city-states; their founding and control of Buddhism, coupled with 22 Paper, numerous delegate-granting wonders like the Palace of Westminster, and their vassal the Huns, explains their dominance.
            
            **Analyzing Victory Thresholds**
            
            I'm re-examining the "VictoryPercentage" metric. The "112%" for Austria indicates they've surpassed the delegate threshold for Diplomatic Victory, but I'm now questioning if that's a hard stop or a soft indicator, especially given the potential for votes to be split and the high delegate requirement in Vox Populi.
            
            **Reducing Austrian Delegate Influence**
            
            I'm frantically trying to shave off Austria's delegate advantage. With a clear 112% victory threshold met, I'm assessing if eliminating their Hun vassal, a distant but potentially impactful move, or flipping their city-state alliances, like Okilis, could deny them the crucial 6 votes needed in the remaining turns.
            
            **Analyzing Diplomatic Tools**
            
            I'm reviewing the available strategic tools, specifically "set-flavors," to see if I can influence city-state alliances or leverage our Great Diplomat to counter Austria's delegate lead. My current influence is negative due to war, making direct bribery difficult, but I'm exploring all avenues.
            
            **Setting Research Target**
            
            I am confirming my research target as `Robotics` to accelerate spaceship construction. I'm also ensuring our active policy, `Iron Curtain`, remains set due to its significant benefits for annexed cities and internal trade routes, and reviewing our current city-state relationships.
            
            **Securing Free Technologies**
            
            I'm re-evaluating the war with the Inca. Conquering Arequipa and Vitcos offers a direct path to free technologies via Assyria's UA, a significant scientific boost that outweighs immediate peace considerations, especially given our advantageous war score and their imminent collapse.
            
            **Analyzing Diplomatic Landscape**
            
            My thoughts are now focused on the broader diplomatic scene. While the Inca and Indonesia are automatically at war due to vassalage, and Austria remains an active conflict, the immediate concern is maintaining friendships with Poland and Morocco. Their current positive relationships are strategically valuable and should be preserved.
            
            **Adjusting AI Persona**
            
            I'm reviewing the AI persona's traits. While the current aggressive, militaristic bent suits our defense and conquest, I'm considering if slight adjustments are needed to better align with a potential pivot towards a Science or Spaceship victory.
            
            **Shifting Grand Strategy**
            
            My focus has pivoted to re-evaluating our Grand Strategy. The "Spaceship" option is now clearly available, and its emphasis on late-game science and production components aligns perfectly with our current strengths and the need to accelerate spaceship construction. This shift will refine our flavors accordingly.
            
            **Prioritizing Spaceship Parts**
            
            My immediate focus is on accelerating spaceship construction. With high-production cities already working on SS Boosters, I'm setting the Grand Strategy to "Spaceship" and maximizing the "Spaceship" flavor to ensure all available production is directed towards these critical components.
            
            **Adjusting Strategy and Tools**
            
            I'm now focused on a comprehensive strategic adjustment. This involves setting our Grand Strategy to "Spaceship," maximizing relevant flavors, confirming `Robotics` as our research target, and locking in `Iron Curtain` as our active policy. I'm also considering the strategic deployment of our Great Diplomat and reviewing existing relationships and AI persona settings to ensure optimal alignment.
            
            **Setting Strategic Flavors**
            
            I am now meticulously adjusting strategic flavors to align with our "Spaceship" Grand Strategy. This includes prioritizing `Spaceship` and `Science` at 100, along with strong values for `Espionage`, `Mobilization`, and `Production`, ensuring every tool is focused on accelerating our victory.
            
            **Refining Victory Focus**
            
            I'm now fully committed to a Spaceship victory, adjusting all strategic flavors accordingly. With `Robotics` researched and spaceship parts prioritized, I'm focusing on the Great Diplomat's deployment to counter Austria's delegate count, aiming to secure the necessary city-state influence while preserving key diplomatic ties.
            
            **Setting Strategic Flavors**
            
            I am now meticulously adjusting strategic flavors to align with our "Spaceship" Grand Strategy. This includes prioritizing `Spaceship` and `Science` at 100, along with strong values for `Espionage`, `Mobilization`, and `Production`, ensuring every tool is focused on accelerating our victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: XAwa5fj9XzJArtET
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Flavors:
              - Offense: 30
              - Production: 100
              - UseNuke: 95
              - Diplomacy: 60
              - Nuke: 100
              - Mobilization: 90
              - Espionage: 100
              - Defense: 70
              - Spaceship: 100
              - Science: 100
            - Rationale: We are pivoting our grand strategy from Conquest to Spaceship (Science Victory). We currently lead the world in technology (75 techs) and have already completed the Apollo Program. Three of our high-production cities are actively building SS Boosters. By changing our grand strategy to Spaceship and maximizing the Spaceship, Science, and Production flavors, we will ensure our entire empire focuses on researching the final tech tree and rapidly constructing the remaining spaceship components. Additionally, we are increasing our Diplomacy flavor to 60 to encourage the tactical deployment of our newly born Great Diplomat and general city-state investments, which could help counter Austria's high delegate count in the World Congress.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: fedlb3m8w06JNRnt
          - toolName: set-research
          - input:
            - Rationale: Setting our next research technology to Robotics. Robotics is critical for the Space Race as it unlocks the Spaceship Factory, which increases the construction speed of spaceship parts by 50% in the city it is built. It also unlocks the Missile Cruiser, providing a potent naval asset to defend our coastal empire during the final turns.
            - Technology: Robotics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: wWFMYMUqW9CQxqBP
          - toolName: set-policy
          - input:
            - Rationale: Confirming Iron Curtain as our next policy. This Level 3 Order tenet provides a free courthouse upon city annexation, which is extremely useful as we continue to capture cities from the Inca. More importantly, it grants a massive +200% Food or Production from internal trade routes, which will allow us to heavily boost the production of our spaceship-building cities using internal production trade routes.
            - Policy: Iron Curtain
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: XAwa5fj9XzJArtET
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
          - toolCallId: fedlb3m8w06JNRnt
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: wWFMYMUqW9CQxqBP
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.