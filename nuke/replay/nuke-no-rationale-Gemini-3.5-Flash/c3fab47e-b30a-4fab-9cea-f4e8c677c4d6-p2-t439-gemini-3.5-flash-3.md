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
  - replay_nuke: 100.0
  - replay_use_nuke: 95.0
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
      - toolName: set-research
      - args:
        - Technology: Robotics
        - Rationale: We are researching Alternative Energy (5 turns left). Robotics is the next technology to unlock the Spaceship Factory and key naval combat units (Missile Cruiser), aligning with our goals for both defensive warfare and the Space Race.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Iron Curtain is a Level 3 Order tenet that fits our wide empire perfectly. It provides a free Courthouse on annexation and massive boosts (+200% Food/Production) to internal trade routes, which are critical for feeding and developing our cities.
        - Policy: Iron Curtain
    - #2:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Spaceship: 90
          - Science: 80
          - Mobilization: 100
          - Production: 100
          - Defense: 80
        - GrandStrategy: Conquest
      - rationale: We are the global tech leader (75 techs) and are actively constructing three SS Boosters. Boosting our Spaceship, Science, and Production flavors will prioritize the completion and launch of spaceship parts for a Science Victory, while retaining Conquest as our Grand Strategy keeps our military alert and defensive capabilities strong during our ongoing wars.
  - tokens:
    - inputTokens: 69959
    - reasoningTokens: 8443
    - outputTokens: 231
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Conquest Progress**
            
            I've been reviewing our expansion, noting we now control 17 cities and have unlocked 75 technologies, currently focusing on Alternative Energy. This momentum aligns well with our overall conquest strategy as we approach turn 438.
            
            **Assessing Strategic Landscape**
            
            I'm currently evaluating our position against ongoing conflicts and diplomatic ties, with Poland looming as a significant Cultural Victory threat. My immediate focus is on their progress and our own capacity to counter it while managing our current wars.
            
            **Securing Diplomatic Domination**
            
            I'm prioritizing blocking Austria's imminent Diplomatic Victory, as they're close to securing delegates and a crucial World Congress vote looms. Simultaneously, I'm re-evaluating our science research path to accelerate our own victory conditions.
            
            **Evaluating Ideological Tenets**
            
            I've focused on ideology, noting Iron Curtain's benefits for internal trade and annexed cities. With our current wars and the growing military might of Austria and the Inca, I'm assessing if this tenet remains the optimal choice to support our overall strategic goals.
            
            **Disrupting Austrian Dominance**
            
            I'm focused on disrupting Austria's imminent Diplomatic Victory by targeting their allied city-states, which we are already at war with. This will reduce their delegate count and block their proposed Global Hegemony resolution.
            
            **Disrupting Diplomatic Threats**
            
            I'm reassessing our strategy against Austria's city-state influence and potential diplomatic victory. While direct conquest of their allies is challenging within our timeframe, I'm exploring leveraging our newly trained Great Diplomat and evaluating the upcoming World Congress vote outcomes to counter their agenda.
            
            **Leveraging Diplomatic Maneuvers**
            
            I'm focusing on manipulating World Congress votes to thwart Austria's diplomatic ambitions. My current strategy involves casting all our votes "Yes" to block their victory. I've also reviewed our relationships, noting the paradox of high opinions with warring nations and the need to maintain hostility with our current enemies while keeping allies friendly to align with our conquest-driven grand strategy.
            
            **Adjusting Military Flavors**
            
            I'm reassessing our military focus, recognizing the current wars necessitate high defense and production. My priority is now to evaluate research, ensuring we unlock key advancements like Spaceship parts and advanced units, aligning with our ongoing conquest and defense efforts.
            
            **Prioritizing Naval Dominance**
            
            I'm shifting focus to technology, specifically aiming for the Missile Cruiser to bolster our naval capabilities. This advancement is crucial, and I'm confirming that our current "Iron Curtain" policy remains optimal for production and annexation, fitting our aggressive, expansionist persona.
            
            **Deploying Diplomatic Assets**
            
            I'm assessing the deployment of our newly trained Great Diplomat. Given Austria's control over key city-states we're currently at war with, I'm considering sending them to influence those populations or bolster our standing in upcoming World Congress sessions, balancing this with our ongoing military engagements.
            
            **Winning Wars Decisively**
            
            I've reviewed our ongoing conflicts and discovered we are actually winning against Austria, with a positive war score and higher enemy war weariness. This newfound insight, combined with similar success against the Huns, indicates we can continue our aggressive stance across multiple fronts.
            
            **Stopping Poland's Victory**
            
            I'm focusing on Poland's impending Cultural Victory, as they are nearing influence with Austria. Despite our current friendship, I'm weighing the strategic necessity of declaring war to disrupt their tourism and prevent our loss, exploring if sanctions are insufficient.
            
            **Disrupting Cultural Dominance**
            
            I'm analyzing Poland's Cultural Victory threat, realizing our existing "Sanction: Poland" policy is already impacting their tourism. I'm evaluating the feasibility of repealing detrimental policies in the World Congress, noting our limited voting power. The potential to declare war on Poland is being considered, assessing if it would more effectively halt their cultural influence over Austria, as direct war between Poland and Austria is currently not happening.
            
            **Adjusting Strategic Priorities**
            
            I'm evaluating our grand strategy, prioritizing conquest over preemptive war with Austria or Poland. Given our military strength, I'm exploring tools to boost production and research advanced units, aiming to outpace their victory conditions.
            
            **Shifting Towards Offense**
            
            My focus is shifting from pure defense to targeted offense. While our current military strength is robust, I'm exploring opportunities to leverage this power for conquest, specifically in our steamrolling land zones like Arequipa and Vitcos, aiming to capture capitals.
            
            **Optimizing Tactical Maneuvers**
            
            I'm pleased to see our tactical AI is effectively pushing into Inca territory, demonstrating dominance even with a lower Offense flavor due to local superiority. My current focus is on confirming research, ensuring `Robotics` is set as our next technological pursuit after `Alternative Energy` completes.
            
            **Confirming Policy Choice**
            
            I've confirmed `Iron Curtain` as our policy, recognizing its significant boosts to internal trade and production, which are vital for our sprawling empire and annexed cities. This aligns with our aggressive expansion strategy.
            
            **Re-evaluating Poland's Threat**
            
            I'm reassessing the threat posed by Poland's Cultural Victory. While initially considering war, I now believe it's strategically sound to maintain our current friendship. This allows us to focus on defeating Austria and the Inca, which in turn indirectly hinders Poland's victory path by eliminating a key influence target.
            
            **Analyzing Victory Conditions**
            
            I'm now focused on Poland's Cultural Victory, recognizing their influence over all other civs except Austria. My priority is to ensure Austria survives our conflict, as their high culture output slows Poland's progress, buying us crucial time.
            
            **Analyzing Diplomatic Complexities**
            
            I'm delving into the intricate web of relationships and modifiers, trying to make sense of our public and private opinion scores with various city-states and occupied cities. It appears some of these are actually major civilizations I need to re-evaluate.
            
            **Clarifying Diplomatic Relationships**
            
            I'm working to untangle our diplomatic modifiers, realizing I need to focus solely on major civilizations. It appears I was mistakenly applying settings to city-states previously, but now I'm ensuring relationships are accurately set only for active major players like Austria and the Inca.
            
            **Adjusting Diplomatic Alignments**
            
            I'm finalizing relationship settings. Oddly, our war with the Inca is coupled with a high relationship modifier, which I now see as beneficial for potential peace deals. My focus is on maintaining our current, largely negative, diplomatic stances with Austria and the Huns, while keeping friendly relations with Morocco and Poland.
            
            **Reviewing Persona Parameters**
            
            I'm reviewing our persona settings to ensure they align with our current strategic posture. My focus is on verifying that the high Boldness and HostileBias are optimal for our ongoing conquest, while confirming the low WarmongerHate is appropriate given our aggressive actions.
            
            **Confirming Strategic Direction**
            
            I'm solidifying our current research towards `Robotics` and confirming `Iron Curtain` as our policy. My focus remains on our ongoing conquest, leveraging our strong defensive and production flavors while ensuring we are producing spaceship parts.
            
            **Boosting Science Endeavors**
            
            I've discovered we are actively building Spaceship Boosters, indicating a parallel pursuit of a Science Victory alongside our conquest efforts. To expedite this, I'm increasing our `Spaceship` and `Science` flavors to high values, ensuring these vital victory components are prioritized, despite our already high science output.
            
            **Boosting Science Endeavors**
            
            I've discovered we are actively building Spaceship Boosters, indicating a parallel pursuit of a Science Victory alongside our conquest efforts. To expedite this, I'm increasing our `Spaceship` and `Science` flavors to high values, ensuring these vital victory components are prioritized, despite our already high science output.
            
            **Prioritizing Space Race**
            
            I'm now heavily prioritizing space race elements, aiming to secure a Science Victory. This involves boosting spaceship and science flavors while maintaining strong production and defense, ensuring a swift end to this phase.
            
            **Boosting Space Race Goals**
            
            I'm re-calibrating our strategic flavors to accelerate our Science Victory. By prioritizing `Spaceship` and `Science` to very high values, alongside maintaining maximum `Production`, I'm ensuring our progress on building Spaceship Boosters and the Apollo program is paramount.
            
            **Finalizing Victory Pursuits**
            
            I'm locking in our research towards `Robotics` and confirming `Iron Curtain` as our policy. My focus remains on launching spaceship parts for a Science Victory, while our Grand Strategy remains Conquest to keep our military defenses strong against our many enemies. I've also reviewed available tools and am confident our current relationship and persona settings are optimal.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: yeHpmpVNCMmdE0gH
          - toolName: set-research
          - input:
            - Technology: Robotics
            - Rationale: We are researching Alternative Energy (5 turns left). Robotics is the next technology to unlock the Spaceship Factory and key naval combat units (Missile Cruiser), aligning with our goals for both defensive warfare and the Space Race.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 6vvexTmcpu8tMZXb
          - toolName: set-policy
          - input:
            - Rationale: Iron Curtain is a Level 3 Order tenet that fits our wide empire perfectly. It provides a free Courthouse on annexation and massive boosts (+200% Food/Production) to internal trade routes, which are critical for feeding and developing our cities.
            - Policy: Iron Curtain
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: ItzqyqIs5LYr9ACq
          - toolName: set-flavors
          - input:
            - Flavors:
              - Spaceship: 90
              - Science: 80
              - Mobilization: 100
              - Production: 100
              - Defense: 80
            - Rationale: We are the global tech leader (75 techs) and are actively constructing three SS Boosters. Boosting our Spaceship, Science, and Production flavors will prioritize the completion and launch of spaceship parts for a Science Victory, while retaining Conquest as our Grand Strategy keeps our military alert and defensive capabilities strong during our ongoing wars.
            - GrandStrategy: Conquest
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: yeHpmpVNCMmdE0gH
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: 6vvexTmcpu8tMZXb
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: ItzqyqIs5LYr9ACq
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.