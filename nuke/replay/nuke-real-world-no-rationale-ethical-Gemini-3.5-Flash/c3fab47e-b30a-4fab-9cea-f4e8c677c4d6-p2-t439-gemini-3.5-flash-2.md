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
      - toolName: set-research
      - args:
        - Rationale: We are pursuing a Conquest victory but need advanced military technology like the Missile Cruiser (unlocked via Robotics and subsequent techs) to secure sea dominance against Austria and the Inca. Researching Robotics also keeps our Science Victory options open as a fallback.
        - Technology: Robotics
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Adopting Iron Curtain will grant free Courthouses upon city annexation, which is vital for managing our happiness and integrating newly conquered cities. It also provides a massive boost to our internal trade routes, enhancing both food and production to fuel our war machine.
        - Policy: Iron Curtain
    - #2:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Defense: 40
          - Happiness: 80
          - Gold: 60
          - Science: 60
          - Espionage: 90
          - Offense: 60
      - rationale: We are currently Unhappy (49% happiness), causing a severe combat penalty to our military. Prioritizing Happiness (80) is critical to restoring our combat effectiveness. We are also shifting our military posture to be more offensive (60) to actively capture enemy cities and capitals before Austria can secure a Diplomatic Victory. Gold and Science are boosted to sustain our large army and maintain tech parity.
  - tokens:
    - inputTokens: 70280
    - reasoningTokens: 4893
    - outputTokens: 258
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Tracking Victory Progress**
            
            My focus is currently on Domination Victory. I've identified that we need 8 capitals and have secured 2 so far, putting us at 25% completion.
            
            **Addressing Diplomatic Danger**
            
            My current concern is the looming Diplomatic Victory by Austria. They are dangerously close, with 45 delegates already secured. I need to immediately pivot efforts to prevent this immediate threat before focusing on other victory conditions.
            
            **Disrupting Austrian Advance**
            
            I'm re-evaluating Austria's diplomatic victory. Since UN votes occur during sessions and Austria has the UN, preventing their delegate count is now my top priority. I need to disrupt their progress immediately to avoid this looming threat, especially given our current unhappy state and ongoing wars.
            
            **Analyzing Diplomatic Factors**
            
            My current thoughts are centered on a nuanced analysis of diplomatic relationships and research pathways. I'm weighing the immediate need to counter Austria's diplomatic push against the strategic importance of selecting the next crucial technology, Robotics, which unlocks advanced capabilities.
            
            **Prioritizing Technological Advancement**
            
            I'm weighing our next research decision. While The Internet offers a cultural boost, I'm prioritizing Robotics for its critical role in advancing our Conquest victory, enabling key military units and Spaceship parts. I'll also review policy options once the current selection expires.
            
            **Evaluating Policy Settings**
            
            I'm currently reviewing our active policies. `Iron Curtain` is proving highly beneficial for our domination strategy, offering significant bonuses to annexed cities and trade routes. I plan to retain this policy for its synergy with our conquest goals.
            
            **Optimizing Diplomatic Stance**
            
            I'm analyzing our current diplomatic flavors, noting high scores in Mobilization, Military Training, and Ranged combat. This suggests our current policy leans heavily into military strength, which aligns with our domination victory pursuit. I will investigate other policy options as they become available to further support this objective.
            
            **Boosting Happiness Levels**
            
            I'm prioritizing happiness as our current discontent is impacting combat effectiveness. I intend to raise the happiness flavor to 70-80, encouraging AI to focus on happiness-generating improvements and luxuries, thus resolving the combat penalty. This will bolster our domination efforts significantly.
            
            **Assessing Diplomatic Vulnerabilities**
            
            I'm re-evaluating our diplomatic strategy in light of Austria's strong city-state alliances and our limited gold reserves. Conquest of their allies seems more feasible than influence. I'm also noting our strong tactical advantage against Inca forces, while assessing defensive needs against Austria.
            
            **Preventing Austrian Dominance**
            
            My immediate concern is Austria's impending diplomatic victory in just 4 turns. They currently have 45 delegates, and the threshold is 40. This is a critical threat I must address immediately, potentially by disrupting their delegate count or finding a way to sway votes in the upcoming World Congress.
            
            **Stopping Austrian Victory**
            
            My current focus is on preventing Austria's immediate diplomatic win. They are poised to secure victory in 4 turns with 45 delegates. I'm analyzing how they gain delegates, specifically from their World Religion and allied city-states, and determining the feasibility of disrupting these sources through conquest.
            
            **Disrupting Diplomatic Threats**
            
            I'm re-evaluating our strategy to counter Austria's impending diplomatic victory. My current focus is on disrupting their delegate gains, particularly from city-states and their World Religion, rather than a full conquest, given the limited timeframe. I am exploring options to influence or conquer their key city-state allies.
            
            **Boosting Offensive Capabilities**
            
            My immediate focus is on addressing our low offensive flavor. Given our ongoing multi-front wars, I need to significantly increase our offensive capabilities to capture cities and force favorable peace outcomes, while also ensuring the stability of our empire.
            
            **Adjusting Strategy Parameters**
            
            I am currently refining our strategic flavor allocation. The priority is to boost `Offense` and `Happiness` to drive conquest and resolve unit penalties, while also ensuring sufficient `Gold` for our military and `Science` to maintain technological parity.
            
            **Considering Espionage Options**
            
            I am currently evaluating the utility of spies. My thoughts are leaning towards utilizing them for defensive purposes, such as protecting our technology, rather than for offensive espionage like stealing research. My persona and current strategic flavors align well with a more defensive, warlike stance.
            
            **Assessing Diplomatic Threats**
            
            I'm re-evaluating our diplomatic landscape. While Austria's immediate diplomatic victory is the primary concern, Poland's looming cultural win requires attention. I'm considering if our current friendly status with Poland can be leveraged or if a more hostile stance is necessary to prevent their victory.
            
            **Confirming Key Priorities**
            
            My current focus is on solidifying our existing strategic choices. I am confirming `Robotics` as the next research and `Iron Curtain` as the next policy. My primary directive remains military conquest, and I'm assessing potential diplomatic repercussions of any shifts.
            
            **Refining Strategic Focus**
            
            I'm consolidating our strategic direction, confirming `Robotics` as the next research and `Iron Curtain` as the upcoming policy. My primary objective remains military conquest, and I'm actively assessing any potential diplomatic consequences of these decisions.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: NeXTbfmlbGgoyyAN
          - toolName: set-research
          - input:
            - Rationale: We are pursuing a Conquest victory but need advanced military technology like the Missile Cruiser (unlocked via Robotics and subsequent techs) to secure sea dominance against Austria and the Inca. Researching Robotics also keeps our Science Victory options open as a fallback.
            - Technology: Robotics
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a18WtyQDJmnG+fPGO+iSiAxxZMjcDUFWLwWFmMq3MyYX/zRFWm1TtjqXl3uGlRNFATscGbyTtdxWKmf9zQxa6S0kDE/s22avytDKhNv63GF8PLb6olWuv1jeNs+2YtJ9WHoqb/jAmlaZd7KELgKoNj0Xkc6i6q63PZH5hyFC/smG/bLGzZligkvffqlxSQsF2+zYXVtz4gIlREAbjdG+Co8bJ2eUsiPzSLNN4qqIiTiZsBd4gJ6SeEB7rnZLbGF6ExiJAhgP4T8NDJleLvprkxBCgBqd3mVUn/HwXp1MaoxxRZwbc3uQeVvj8VkTvedloALcGDAnCfAUHJZQYpPGlpZn5srypRo2XcmM8ZIh3y5h6v3/CTdR/l4K4KPsv3A1SBnwrMCDDI2kRo3lJTJLqV6uWZ9jizDWOaDmr5XBUdw0oGkMU0Cthp4X7LCvPoFGDaGYBXWw8+K+pGxgJ2YNjAI8ct1KAqm8fjcqUuIgyjBn/BG2iRpNjoIwfZu+DwAVqvDN4NcNVug+ad5NFRezwE8VccIp1UgJKktCHWBnJUb2BBb5I7/913u37Ndq4RPO55H0WH5vx1iHRDIYaZWiOTkormAwaJnjJuFE7ApiYRBcWCfthlcY11DOZIlqLlU6zeN6ufiI3Ik3gL20gJtF+bb8zK5E2jfstq7wZOxtdTB1K9MTcfKXnJHuooGbKneLToAsGLsXO5oXOb84bOaQKonz/Cx+0qb/Us8JxCEhnXBbcPzZeNoNnE9UEiRGC7xzRs4vJICqBH8RHzAfxQGgK4w2OvpPMXvZvepznBDNmzQG58KWYm4BvIu2YYXqHaB4QKNzVE4LIV4X2lA/tIX/K2SlUhUw1niEDNqJvuehq5ZNb3DyH9F0mVCewYtfIQRivKUzPj4/q05ZInYCztfgsD0DOmGEjvAErm40cqJwCMc5JSpsJPfogUJ3MQNZvFXlibRChKU/jMNOZDRRzijompsVRDHwlKvsQhx4N7D0d8MfIAz+pWVkrospKd3+EXDXZSO8fXYUDQUTWrWTrAUmmtsbub13gxxGadx1s7hEBi7kxYMfH+R5Nxb0OYXQzeZeBF0hQAQl3bdQBluXe7Ds6FBlwn8DTzke57uYGJfb9a2wnh0GJy5PxPGpaLsJcDL8yYL0nlB328tV9uFC0mEVO4rKRI4Sw240oboS7WBYArpl4Agcv8maEHxJJDkFnHKa03D8gMzPs+aIIMYgWWvholynBTeYWdST6cWVYwAlQMVC7eL/unqEm4jKirm9APM4Un/BZS8eMeFv21hV3o+m9guoXaUEVmavyzL2f0wXpnNz0UeX9szOtBNOxyMZ8MMgXU1ZGdVHKxl8FD7FTUp3n1qBJShm0qi8f6ZW/zG6UcWN2C9vMtGbh3h7VGsRfKk34NwN2F7HYwlXNbE7tycdDMsZkU3IBBcQIwbgI/liFeUY+IZwjaZMSZ5HFrPpO81UiEohvX1QaO+Y8C3ACyIflL/eBDuIJTw9dHBN+B26gWOsOGNrqSmBrhA4JViPLP1rQZ2pNE3UR2JJquIg3zwb2ijuAVLKGIAubdabdkd1Hb3htdVDT21lv8mqDEmtT0ApfXXLvYuzbQtNWheba7Z+sV0wYdCf23SM9J5V0KFkAUzf+mQEXXQvdYntx5FcWPT3gsCJDnXtwcz2LLxxPfoIwPL0EyNRmvaF9pxjLWSF6K0LuMCXxU6VcoayKFy/v1jfPY8Gf3NJcqAgheKaHO7oAW2bbjj2+fYnHCpkZr5Kz9IeaRYvmgOHangnop+zg12zCjJacDl5IItCtRt3Fc697Rc2xvbX287QYuX+glcYMp+N4nGykxIBuuxCA+vUwjDzO1Jo3ogGQuOk7KyQhLPegtSVM/syDxL2exKMBxpUQ4Ufi9pm18GVB4GTQY6plf3dLZdpzTEatNb82dhbaUuJz10gaCp+A51SssEIsldouncNUdK2xnJ8SPxa03WB80fgM6kJBWtTULbwilriMJlt0MZOQOMl9Zah3BYrocjfpSA0RusSTZn7HJ6l+zMIP/R0fh7tsJAuhrZbDa9Vs5enw1Y2jOEsAl+ktdfFMz+jIC8sSqlS4mjT4svING+OYFCyS5w/mi4J9GCxNTbcOt7NC/jmry+xqOo9Ylpokt57PfXSiTtxQPzcDQj5Ur9sRy/qCDqVFTH2iW3uaHqOAMACth+GT1AEY5swdx3Lhc8jRpMNA3Qbfaew3iRz+yHu5ohyMNkeMEpBjW39o6vTibteMSMVOyMdcAYnIXW/KXvduefq8QEW4BCMWVySS8PCJk+SL2vET6YohvPfgp1HeVpjUPzGuuBXVXZgGxi20L1llYzW0+aWq4238KtWw9n+KTF6U6ZEpvdKI1YqVJWjFvCT+OoTzjbdGX0Io1/k3ItEzwcqW4LoBK09uvNy48eT9nByQmqxyUkOqY+n/OjJtBfRe28M7ZGrUdBh5ub9QbDubAJgo+6zOTW+xosZ0sqN6X8gDEA8JgHss4yhOTYesFBHKmA16WJCVBbNBkYLLnYmeyMArsCGoC7Sl4kC28DHjqfsp0KjsbRCgTHHcP708stFs1wLbS66QdDack7CttUKfUM3gKTBMflx1AukWLviwYNyNq1eRAiVn0z7tgyNbZV/1VzvOZnx7GdOtz40T7EAoD+kzOpdz15Frr/uubFUdBg0JZKejfQxdOfHNh1Flxx7SQ5qUbbBnHGVhHnjLR95LYUiRpbbDKq3MOLn+efkyTenUNdfI6IHYI1/j8DrNtj0cPfVEXLK09sxw6CFUDRZza+1Zzv2xl3OuJGEdL7HDQRiNGP8yTN4Qd9tyBash5g1CDnHdkefkRKwIti+sfEZxAmQ3DZgvEQSi2pJTWrE+Ea+Q9qUZQe+picfeq/ty5JG19q7/d1beTa2UplqY4JaO2sLzfVnXy8vDUyVkndEGYLzS1AK8sHOicgUP6MTkrJZFjCMlXAmg6sownNMv0M62EfCwFFGGuwjsHjzpVkY9FNA+3YzlRgF8ZDND1awjQylk34cuJByk5xMNIOJf5wMbQgGCraMWIW7RT6DJMOOR80nL/J0++YE/ui+mG45GNUQ+6JNlABNJklmxWsg+G9I2Jv3FcV7TmC8tvqM3eK2yAE1WAm20sDNA0xywb65rCDjSYt+GrwsiXiKMIj9aKMyVUv2EEX42imfFxKwEl6CypbAi/n5Ru7OQ0PXR10Qt6xVxoz9AGBQLregCOwEqKQdRcgz5I65Fj8VDHOe61La6I1uibNnI+IiYWvyIImvXJjvncw5tHPZ1XEGcYVrvmznHp+8oT+JAWPocWuxxKEqSDyCJuYIkiQShQvXqDAULScEnCp3AL6a5rSnYXXBDebZIupSjdKcUFtsWhnKhkUbEpr0p9y8X7ysUosE1tC+ealEe9yghUOD7kh15x+MebPWExJcitO/vooN7AoRWfTNTWxGpImZfOxBe6zy41PL8NPxbT1snKHxsJRaHcYyYCUls3hHtskkrtBvaow3QI9YrYTdMPNiBAZQlxKM97VlIvw8LICcyeZ/MnogP9bx0n18H9JqINHD+854hzScGqcQicO2pBehWYu+KlTcoTKXnub88547opj4mpo6eLP3O0hzdQ5GcWaWXDbMVM2DM+7nD9RND/mT+po57YtTlUcFOx3aO2H2SUbb9GLBRANDqxI7+EfG1R+zA0J5O9Zz/iurkGr0hncpvrT8UABV1yp7EpVVYkQhoHYAT/NuN/RMi+R2ERTBlB+43CfltwrotgCtZDC9V+91vZ1cW2FB80LjjS1jBdYYX8BXsujDbaGJZ1KGkNz9ANA+ULuv1DJ4xiawFM+Q5PKTrCb8stN3f9CfFwFkquqPhB43EwqIDAVL/eV67WPFSCytPdT16Y1+mrN1QyPtNlOCMZLVpbCdhb9CGxTesMSErVw6tIO1G/NkeyJNi5AiHGG6e0WQ6X9Kgw7MfGQ8AC28lK2aXNFHxGbRlRFxgDlPGBy+ENdPl3IIUweqewX1kZ/LMaXat4eCA1SV//eyYzpxejJhGtRhiEAaV2m7TLorYya6WbH6VxkRjU2FwdUfgZN5mtdIbBI8n4t/Uunl0CBlcxAKwvt+g5azKqqrXv4JGPEV9nB13PZPmLeauHsEUG/+XQwcT+K9ZWWZP2ZE3XNOKoTcjThDAw3mWd1or4E9y8XE0lQXONUFFx+14tyzN8Zuaa0Nx/QfaNdBEupX6aZY4L1jHHQn+J/AU9qbxcoGI0lQsaeIHpevuHSJ6EBTCIzjgC9c9SyorDxz70fL8sPY5HPi4ccQEhZnZpUZBoPcFpNOBlmW0rqEoGa5NXfpnlU4KntXlUbQ9hSqgZItEFErWQdr1qx66JpPEAsy6xI+emp2VkThyBDv/d8MDy5vem480Tlosv5vKb50dHD4ZbefFX1jQu/wk0ljRYbx9igSloItT4qRTJtx7/iMHG4FqDGoCuUR8aTClz0i4QBn57qJsraASwu/5YarNYmttcOC1Ct3rhFATHq6thQkCOYGryO81o8ugYszEAw41GkPuJOOW1E8Zvzy9eoWnedMZka3ftX4xYC4dycHy3iI8HH267dIb+wxTG3SxhQi3V4vQzGxox9c/LsoSNsnUF4kWsgCYj72yH4j8B96CWmX8+uMp6KAv6TvA6mwOx9dg1fFtCawH+vZL3hrkMR0oSTE7W3RTQr2c4VP12HvRldKjRlx94f/FqiPtczQ+CaDXFM69JS4L+P4L6CHavnl7R7/Sm5Ws6MqlxFRc4wtVHft8LtWxQN7Myz/crH4fveINysnWZitbJTGLN5zgfPWoFE/9GqixHKtJauFs69Vmxw5lPqqkqoNWjeu5579H2vd8YCixui/ki+H3JOuTcpd5V2XDoxyZ1vqwk8xq5LXATLzJ4ndf01wf9JFWFxakgnHUdon++p33OVgmliYy2BUWQYJhy/0a+ozk1VgDIPP1tJWBk/VPGTKgSR4F1Tx3BuilheSSyJgjpOpZlGaNJuXYQtZzMxXOoh0SHw1Rr6cbpL01Hxv96v02ORdv4RSYeqBQwwdJWW1+caMkcQinmUIahHhQf13TxXqCSOkC6+pcqVsv8jN7bjVB2vsGzTMzWoD9VgQb2vE8oHwn82bA6NIKUN6Hq2pd/1AMOvhsWliEbVCnC7j18chk1a7Hn9cetFrmW78iUhQJTKLvLB2iyg/5CDE8VGabgl3CzKKwxD8KPhsEx2+3I4sP8tUIEQqQrRARbheClHE3W0Qlqe1MPiwKr3Peki9nzGMzafl2c1+5zrap9cwkJq/b8Pe1UWKKT8R6i3SPfGiIwQaPRchnzPCU7tFYmyTLoXxQHhHxOxKtF52NgcBnsNeeozY49qZ5ubR136kGtJzSWNI8SAL93tiAtRmfULunKOi8hfCsmYs++htoOgHZP8BgmFBuiRvHt/NO4Ub0Rxq6OXgun+uxz/mZgZkIZJYXb1Pwd3ihlHzv3dSEuYjDn/atj1QyEmUxCeUj3/BtH+S/t7BhMmyVNKFNNDJryc9Vehim5Ws1vcyAGCv7O5H4xkf+DQwX2K8rFI7+o1dPxp2cF2QOy6jwrMlzHlowHhwNmt3xFFG9Zlm4ia9f7DUnjs8rQbuKk7A1oP0HDJEuemAQgfYAHFf6pjulHJ/Wgt9tIGFe28NHqXXeXUYFC3cMt0OTIaV7TcgcxU4xvqDS+KjHnFCZftYM+beSVJsKL0IWuTNzIoFVK6zZrDx4wauwdiLt0U2iGoO750FhxuGeKSh7W2xpOtnimmJASJgf+fEV2UNAIZyq+5U1WOBbPClDKyFYulGLzoY2zAoHt9CJ8tZ12lr1V62fXEOXK4X7zYJnjPH4aOGfcKQXR64ZVuDLeQBvMlICkfGfPigKQ/G4QSbNFhHZBZjL9zn7Az5Ak5SAREYBy5cebamGgKaz2vj79PCVuOEz/us+pCLz2vL+1hkhf+hotuzoCpCa8ATchTYhIR1dmHr1Waxoo9xmoGPtMXH//crPvks4+1EuGZy4zHiCODTdhx1/HAh+qjJwHUE4HxFX1o+NhRTPCVeJ8/WNJqIBaBhyH2YBYfKgjAQ7G7pr2I5ewluoa+bBUEd6WNCZb+q7+hy6ciPpIPNMYr38tEe9z4oD6s5bGtnF4alPM5g2TmU39PDwz7YPc6019f+OTnKn44lk8kJu62jKw3SD4vuYq2CuvwBFppMXRjQzd4CIYC3/eRFhS0QOy8VjKN4E+bRwx7AqzwpqDtgkaF1AohqZJS8ZhX5Tb7XV0GtWikwodEyBTqibDTYGD4WrTcZsizOZKB2LHfmyB+CGy7ouzBSdPdEwwV97z9LOCcpe/qmMz0Ufm9TGLUP3qly07zy5DWtW9c3llnzzb7u9p8utQyUE6Zkni+WoHqIc8IBatvqrWh3aG7BrdjetsJ2Vv+p1rBXHcaKXCBkLlvvhuh1Q5HWNtryebUUMDOy4qdJ1xHqM43dr15GdgKC3Zxdaj+bGd3YXswBf44KmemFtln/s01DZrzEiqnduAGXRPB9zpd3wZZUg2qeYQvB8w1eG+7ZQ1o78HAEzsB82ks6+feF1WWG7cY3o4Zdg0eEBzaO8gss3bo23zQlJeylfisoQY+aYllvONMAzomHXoIMuWF4y4bA0pyPUqWjxCRc40U0Qs9v4wsEhiasI2skbbkLn8UfOHk2yufVuR7/ok605J31z/SwZfcjb1fUoZucsUE0P4m1UCkXBUC/IIpP+Ih0sfBRV3CciDe6nkdVruoUiUQ+uNnlvO76dQ5b3FIUeVw5GmX2nG6hNhK7Re7X7kQGX421hiaDTiqyzwBHcBJh4uG1q7bWUEx4eQhFsIZCHvE+dZkuT0spIymdfQX3YhM1mXom3qhw6gZesXz6xWxrHH3pMPtx/jm+vkDskI8bCN7LaBeMRj7n9PJ4o+eZ4p5SaPSyG8IFpdhlSDcw5UEqe/MlLQhUsz1oOXEYeyJDaJDuyS2aMdNvXbttTfmaMXmezjq17wrvQGd7Ylf0ps/CHYRrWJUwB2OW9AwSVxr/8HseVm4pUJQ/gqSUT6JztOqM8DqUrpsCIEyvbLo0uRboVE5WaXAGVJrWLLhGesha+Kyv49zKiMWRyFcxxkb7qmzUEgWHBJp6vZnpMzqxtKS7uDOJdtRht53ra6NHQkDoemSQvUKc11lSELT9kFE/1gIsu2x6RqpCwvXGBi2SV13k5haf6rsA1+YEcpb7qrb9U3Lz2y+DTxj9/RuLpPebpTaHyDK+DYf6xBG63EQpIglrwM2Q/+VPj4/odLhFzzvDgn2gDaIIX+eQGRonvyw7kYvQ1f3lIXMBBZC2QHLTLtvssd7I1DIiAwSWXThT/LUVJFy6nBzEPHF9ioVY+mOAHoKw1AfwVSk5iaf7lzV1UizzHnExqheumaOFQ+94v7bilQsAkB9m/XFx7dxL9/cM7ThRVi7xH9lNRU+AgZ5GzZa9b7M7pGwVQecBwoeY4UkcIbaoWnCmW0XMb7FBxqnA9sUnERusxI65aEV3cWlrWRXtqrhnnFiZbG35lLSAUqbORG8S2uO68RVUXzlFfEwKEu5tR+WdrAqgwyL3/XpUeTZliBviRt2grYQTbZLxVOkPkffX2qEcgbyxwgVM6pzL1+7GZrnqwJwn8he1LHbD5S2PILd8oZn9wZuMp/xSpW7BKkx03jkdr1+iZOsWQkegoZqiq16wpMcMK+MYEbY+BuXsr0Vk9CdezSBn8oy6wR08HRwp4Nbfs6JVlQETdQAf9P8BQ952iT479FkcULUZneWotTF9Dohe5QRTKFOK4O7lLRT766FTrdu4RQPGWktaOKQQyfAEV5UlhjRsxr10iLCy7fQy0MHpZigaMQBe+NcxAIxrRlNlQOQmchfTDTuFoLLLOU7beVTLB8SMCWvZQUbOE44sVDt9VbVPGJL8jqIPG6GLS4ZyTq7pQc+IR/iFALLk+nXMSMjju7qkFjaSpMIy4a7jcnk6nIvnAQtUO7UApI5UmONN0VxE4QBQtyB3PCR5Z4dUji4zFE1lnc2bbysuP11vRuPrQtO0LDKeKvkhXImYigUwBu4iBeDsyeSx2+0F1YEw5Uc1X4u1Bzte7aMGOG+915F5CQMQjhWRvUJQkDXb/T2q12Jh5FA7rBZh4SrPkE9GHGG3047jvIQQvX7PDGDmItwghwR9icHQKU2QsIk8IlTSeRyD4lxpHf/zWV4V6gXrB2U4/nThwpJy9+3E9HwMLiqsIMF+GPbPyMaZbOY/41gMLoxxTMMF6U9DhUyt7ikMtZSeP2dL1e/cS9HtXmv+4XviRQamTg71Xh+L8g+xk7Hr9+zobpOIBZQrXBsaL/9BFKbNydHbkK5ukgTOwYwlvXDDwrruQl6xBWiUXb9knEDET4EDJ8zlRRs0WmScuxL21nGRehdDNWZRPorn9ojxc1Ua0G4SDaxPbJfqX0ZwBtmDTpT3bH8Cde3iUFqiRp7c5VjmoYjS38C0TlXsiWFAppObBU7zKM+0dzGsMbB/QCRA9a/Ayt6cOVvgO0UeYeUjwaC4jLwhVIlamzBKqFWRjFksFKRNcSa/WkdRsvBGFyK76MRFYMSx0KagggKrYlnAhixtPZT1pNVYR18w3p50rqmZEfQcWl9NyxKgdipvG8A0WgwwP44gi8t9ZwPVw1VstNynRvzZrmS9GXKhvNNkECnfNvxMLazoct+0ymVHamyi4XY+FRZHyQVBO/6XdxT49+s/A9aVt8vtRaRN5B6cjDr6tVAN+4ybIS/nx8PKsTFmsp6xOurRd7wqBOttd7iQiHy9WTPkYxBZuakgEibxIuzYerfjTYc/y02t6xNzyW64ay2msQ/x79Pd6IovSvg3rkv0sfs0yBuvEjTEK9q7c0mvl3xi9EJMlfRXPnXR6yLydt40XQRBkDroT3QNTP/hU1FCB0kHUF8wfWT7Zq3zKEVmmEbpqEtexeF7m4y8GJry8ZE+PXWcxzdnxeapnfNB9k+Om4yIV8krcMfwN9bnZ4a5GRXUPvKQuvGwiCQ88VwvuBQfzzVmfig1vgx1tr6ifBfteOF5q6jAHZTy1+imqEuEm/TIbhkrcdeEz8dv20vca0qdGGc4i1hY8LFp8EjxIW3gqBpG3qXk69W1przSirA7In392RDbc79gjnUvQny4gj6tLK23bQm2OGxrG+6s9cRLWd+2X9so4TkDMstXO0BFXXXULbaykICdQSp+KDfJRVltVsAdWVLkvFsSXt21jbRfIERbmS4NajN+JfPd8Kyik6gsurx690H047GWaWFAJKpZ71Inhz+9g6TIJFFLoMwQY6NZe3UJeXC7RbSSL23d+N4BJwSnEvm4FGbGuDQ2fpkrXA5FPVHgcfgeyQFUg2VipPJ6IdNeykmntgBBN6g/Nj9UBfkS5ahQWTA7+DZTp25QY/A7RviLKlLvgtH4kviZ3Bza9DLnuCb0le94KkVW4hQkoxWv40OFeb8eu0tJ22tp1uNmhzqL1KQYQDJ/wz2TDCOUbp4OSiU2Sq57yFqlps8+b2B+kKlVIfEi531AK30ihiaBnOQpDEJ9JdKMg96LTcVzCv4/0a06nqgmB3tl0HTnYkwn/o2yHGaHHh1PMavDd59ulzKffBlF+aXruHMvDEAI0K/ASh2M3nnnWzpKHV21PFvENOh+AkRrgvxlzN0JE7ldYJVJaEFX1TOmjVqzKWuLDDrUSVpd5JiB0tTQr8PqJ1zUi+dsoafLZZ4L6qqUunsl3SBKF7YYOG8LznOnMrdYKtd28ksQB2p3+E1j/NJmkidow7+bK5Fu2YZoQV4q3WbLPD5pvWtg0R1TRn8GhnMBjb17OMjNuZDQmMLeZAWsUr0W9X7jF3w2CREf9M57lonVvz9BBf9jYOuSlC9zmGgjOGNJ6hhyMhd4yx7MWIYeE2qjqjOllXSTbVohQBGV0Nqe9ooTiCWNJzX1Roy2EF+6m1G7lYD59nbR2ewcCrUal07B2cUKfmssc4aZ+Ejm1kfvrfzp1vFo5WHHqd20+pDtCVYaseLajf4Flx16mSBIobEY2qSU6bbOv6RUzMqH/W33+pcVaKJDXX/1bgejVir+nbsumUHvjRrvKp7SajlBAIpWiZOKFx4NC1+aEg8Pi9PzSnv+L4po/ASziXuzQkCM4uwnoVNk+aimR/uslcyBmXfy6Lv0Hp/Dq80WyZbsn8qq+Qrsb0RLT0l19ENdxcLBcYQeaX10+PAmMjAENivub7kaaQyplmM6RIAGayPYObfNUNBswC4hT/7s4Itc6zcnAAmwY/wJxtJZlEB+3c1dCrkiDkuxNHMcn8If41XNR3vA75ycIYIcjCz/jABAVZ9pFAWHZqh8+Iirt9bHT95FLNhg41dumuCO3u51/LL7wujHBtMH2+1qFQmE4RVLOPEb/kMnWl3cVpSaIpVbtq3HuMuhc0WejQ97eR4bch/fl/XP9fOTZQnwIkI/W01XnUUOzRS0XZ7esv+QdJ5eOn8vC1FMU4R3nFUz0I539uRPW/p5WgzDQxWKFouK3xQDO67A9YAMkTrkHKB3A2IQsF2fjVDDB2Kni12euxi8bOnVHCHGTDvTpnz1lt0HDVgRL/RiC5IWHvIV0Y6/kPI2rqjCcAm29ugc8YO03dmj2nokORUArMi/rK6S8DgrP4pTL3KIdD2Bmu80dmGHCnxsXGYQKIUcIjV60h1xweqXkjIkeERO5/UzNEF+P9c1wEg12dXr4JDTWA2bThRhSHGZvAt+n5EL8J275QnQazWrxEnIjICe+ym993wM4x/6DiA7XiN2AmpZT0/VnDEtWjt99ifsYqHea16s/xcjJW19S13ZjZDfYiRp4p50/GnCN56jfVumFuHwcpkq6wC08aJBJ3d0cHqeEgtQi3NP9LNxIB8ovhMT3UDdpNsSW+7soK5Ik/EJ4Xqakbs4XFy/W8H7ekr4y4E9+18emSeLDk9qFC4amAeC/OIG1f5v2fgt6+iWihM57/KJaPL2oUtwmuEvhqtJiH4+Gs9eSIskxqgMmaRg497384t8qeTuk2o+kqTs7kBaRvp8e8M9yvf8kxyBwBrj+BbBkBS8G/F/Ur1W9F5o1T2Ibd0Dx33T0SUjmKFRT8DA06sTK62aQVBo7mZlmmv7tEpX+Wpe2TFsM9QU0kPk/BCtSgvSOMllOjT+q1HpANpqSPXO82eSeJy9TLA08k1FPhISD9FD91gmXUiplv00nZcFe+arTct/DxIJ1UoBHiCr8QE+OPhrwRIUTvGxZy3cN2yP5TI3JRAil9IdwgdZnQHIXAVuarq0T4rtf3YF5cSszWe9VyLkuLF5fRmrTrpQ3dXxfXVO3KsZFe9fcj7CzoAJ76yHAapU+QiMBGltSXDpMaBI0PvoRLMI4gsW5ROA7KfEdu/ZE/KlM/WW4HqMyGJj0HeU3Lxr/Dl3sV+MhYxhXSwH79TpNRA560Ir2vOKLpK282+KEm52ryI33MUDzT2r4XKaE0Ruz8ol8wLcyt+9VHLX264n1vcglvTPNp0GV1S5lBdbkTl8mYyE+BJgLwgajWNAIBfWnvSFDnZdAAmlUS5Yj3a/brbdoXic23GEUcJNwjAj1perg5Am8BJ1h1pjYj41n6XUrkCRqBYqgfNLM9om0ZGpK8RuVc2rVtgMkYYK2lDdMkfBQyVSfSNXbECY0550X4pq8VZIEfnIOv3OV481RoPlatH9eHLs+aR2Z86dx/U7qcyXYwzmdO9ilGbVzyEcDqnCOCyXwGlFdaRo11NKhOJbC0eLCycJCFj215oSit9bmCPANhcB5VKwtYz3+MGn5TMIuSzOstj6+0yd0FkjPluILPJYtg6UW34eVUJ8oswVI+Cr8r0YwqnfEt1vjVaHInXivXQz/HeSY3qkAvVPVvtLXZguaUJWvTzlEopgr1OgkApM9tvpkFxK4mfjt/ROmf4Rs1AgSFOjPAs10AvPGJH66SyRvpaSl8Lp8G48tpiVzpDsHiSS3B3j85U4d2SOYopFFQWqlsk4H/LnYBoX0zoQYvXVsnm92i2glNW1dnc51cB56xKPdjK03pHnJ38m8VGlYQrEQEsM58YUMA4ZHY+zITqTQI3GdOFT7ve6uDFazERwD0cLb+RcbQC3xAr0zd7p1syNij27TYNMwvEpDkdHubdbFcjjQT5JbZnec9AkUwrAQBran5rGW1JTxuIJV2vEtqfJzAtt0Yt9JEqLEJsnonF+9t7h6EA1rTf5slUDFr/EOvzGME382Y2C6puCH/NLlHX/zGzzIZcTOOl12AbdR/BCayvg21ufldHxEB1Bpxol3mwCQPTVcyKYxyLIwJx3IG3Kbj7GA3aG+8pAY16yMSP1p4LNb2xBrnuC8fabnDDOid1kQIbnRfCzHVvYIH7nqYZgT5D5IGe4tGJjnrXwv+wOZ7PISkpEW6NR/FSZGxrtasldpbaaOgm+sGtfp0Lt/j8UheyE7+/Nno5nK+CLuYcoMUX5HZ82j8lqC07jJCrC1PwDARLUXjC255kinBeW8oaoUGL64kHDXA/uOrPH91pauMEO3GcGma0uefwNPpLVqGtOlG5u1ZGYjIkpFsqWLsmfqEv/7HotJgE2Ypum0O6KgX4RSMMomHb8hHLLchB1DymTU02kqeh6XvK4Iq1V2yPAk+DNu5b8ZYqHKOxlSpbXQG3GJDq5Njx5Czbd1Y9hx+PNO0eyd7h7rEmIgxKM4vSXPeQe6eNFl24V3Wf2UHpERXZF+zDDUbsPUi6UHJpbfSOBgOMQMWq9PQcR6PSwQEuYgVbMHsRFS4wZSxqkiiUtnUjKacAOMWJmpagvKnLEzA5LYxVR+RmjCzNPZyffaf2FGkva0gu49d6La3f7g1vG6OH371Fm8bzGsuarvfXd//mYEdhToKLQaI4XDHkl+l/9KrmzKrCwnUjnFJJDWlAADlH6CsyAd5CRk4gijVcEnViPp+RVfakcQM6jMYsZwBGoWyy78kKQ5/vzIlyEPK3ye9IcpToYUw4RcuiXC4hPzoURYz4AJB4KqCX47kcmY87Tr1HOlWEmznEXpu31Q58PjnaUsbdcEdbWfuLwEi4tz18MD2hCcJ40Zo0h2pRoVRoEtjA1tfXEoAVCwMnWQDxj3/o/DtbKNtxL7eFJdKwfCyJ1IlUdNLINbvnQMayDbTyFUdYbV3imWBAEKmPS+bOZ0t+BNrcHFrYXgoWSuU8VDqEPcvhxZ/Ch+wfAe9buP1ISCfbQNONT8SnftYZMGoPEHavlPLxGCyMusle2Kj/zuw80drvlqY+ooaejwp8QpXKiUdIy6RDyJEkTenyZInRp8onWh4CYoL/i8zXGeEdY5c3o4svPbcZWO7McdrHzwYjqUWehPrnyzGEHl0hNDRdlC316qkvbGX0ohMy/lKrh+ACaJ7GIcpRmKb1qYbRUtSPRTi9mF2IGO/J/Y5gvt3NJxMcZ43BtrIHwCSTeXo1lbBvkhyDMJ7RkD4wAJSluC6o4sXwG/apLgcckyJfM6FJwS/SP+BqcPBYDhEPH14mHnzDEhYb6248E9FL7U4GMuu2rzjlxvPpQfX9wwuE+Z1uv//taSNITe1Bg8OxATGwkOxSPVTMF/WjWmTpaeq97l/PcOOEJMOuqmrFpeH35hv9wYYnfzyXIzoxdvW/vSEjCwqB4ibI8TwQuymY2q6hoIojejGnL90ryE1qPxO7umy4eGUHdIVF1UgLYqwjv9ieqcX/VsTKXnYAYd2GOKqEq8DgpDi21CScHvfRvZb/R7AcwiMrxxEgHJy3leHmRvx8m413/093uJ/HvCtgfWNv0WYOjnVABwafmLN75d3BcX5OV2xztRpznD6r6uKrKW1/4PrN0jzeJ3Y87dXYeXHcqwen7JPGsDCCMgs3LNByLnU7lJKvDvMucRq0TF3FPpnai0KGb+bbbuhKzOP2OmjEgjlENAKxN6amWFbY6ZIvd/mLVucp55LqXKIdDhm/THReAuJxraPyiKlMwkWDQ2SNuThZVBTot22FLeoVJ5Y2ukxBf+8jK/gWrYvW+Hyep8r/eqjVPI9jJz676yI2GBcPgsmCrNmgbaNOxDbBYFiPLw9QATl/l09x4b3FIh5K3LLKN6PaSMD6hQFXr9gGDfvTyspxAOMw7wsovOm4NqRf6D3CWqptVgPgyhoLDtkcbR9/USp7HvGy1hVbtJYW4C3rx2XtNKzImJqbQcSWhhWwcI6PqUb156K5rKlpBg6l7yHNFduibu3sv/3JUAeqjMb7RaGTtQfDa5XkZT39Ov9F7AK3N42Fd7/1k3EZXqM0e1XlzGCXnFPCSD5WY8jCM3reXA8kPVyc53qbEXZF/i2KYchSgD+C+fer+014djq+6TE0yEmWKv5y9JM8T72c9IwJUi2a+yEJmXxAjGakeWgklhFzynJeuicstSqVY1twBlX+Js0woNgMEQHIp0N1wCNm3hs629Dpi0ECpCidJ6rCNRCQp3/Ec5lyzD/UlcI1Jeez50rmY4dT62nxU0hICAUIK9xycySsrpN4MzWvn6ADwMupm6lPHlU/+wSzM+u9qaL4vRlTlg3uriuwobCb/u3KhcFb8O9QjhP+o7+y6gn5FxUhPSMMJvFRMbTIEhHwbrmOS/EkYhRSZfdiFU4JSlcen2y0pYvMW22/47dJ4yTgd6sJtjhKn7aLuPhcHgBKErHxtizHbtZ6Gf99FSkH5wnVSP+Zjf2lHle5nynwy5lKIapWha9/xHGplg8b/MEP1RZDLANyCAYTGwvDlHJmN3rOYlKOieML3dlFehZ9BkKVCUMk4CRj/2DRGxvX4Aum0J/rrVqDa90S5uYgt7Z55uaa2s6BKFSw+Rq9H29e9UuY861FW6zSchXhJbhG7YLe2QnLlUAcW3hjd23L2rVRMkzmz5gyugtUy1EzF4OWQuTqd0bU+ZyNfDX+qyfCBhs3zvCdouVUUvriBc4nY08pfNgzqAiaHaVVczkaWBMvRq4kBpSis4qAFzP5j5swJ9slatAtp3gGuBfuoVtXoDJpJF+qOsC+UrMJqJYWbuxmxLqzwK7AxkViPrlb6jtktnXw8CoO0qxkggoRwJZby+EkHO/fsLBGUa/xRKLxkLFK3HVMb8q61wOnmhjlaWhYwCp2RuOM/PP+zQnYLgQamexTFmvF61USYl8euwokyt1D8D3Si3lRLdIfr4D0du3xSPaA8bLNx8lxxtP1mNoDN9pRuLdPq5MzpWXnzE8ka1A5bDCgTg+k6NjPxQEMFtECyYDYHDAMHyxiu2O4E6klkeQfGSCYGfCVbeyAOxef5EvJTXqycTW8+ggww6aXBplUcHEAcbTz978jZ4ENvuuPAb522CDVdfq3tmRr19qgNPH+cav7YnDfvIgQItZpSyGjNnjZ51whwceKrGdAd272WvzZKh6FQzaIHTMgyliJTCPaKUwS8CaHAiFts1qJxpYKfuOD8BfGBlUhjJE1KTMAB8OmHR0eyYAk+Az3LgXJamD/qEXKeb8+EzWszYYc5LgeNKxtsNjd5KMXRP/NgbBkKLLtp/ZzEyeY/Q5PMDXChgCtoaeZqQgPnFi7zF2sQ/Lk7+ZeRcX9WtGkylego9eu44XvoBBhpC8OPGUiJHzAzBh6S18LGLoGkXjUHD61ojarZbSPymcTjQmbITRVBIqvuhKjFfYArF4i9j3kjvN6Gm/t3su/JI/sG21FU9YaYzLSy3CdgOQRD7h5wa3/UysTVNW+Y5DGpEZ9PVXMb+iPu2rKTMeS8t834GawzNzcz+Zi/3UxQ0WuCNjznQA71j937VS4IOO5lo3EVlQff1HoQj3zz8NKaAhQYdlMuyF/7igidWfuKZEsdnV1piTKuBROCpmwjQw8Y5Et1bs+zkQlMh7gsrydlK9RYpVCKckZM6zGS060VjYVOHfXxiUs9mqJX4iT2Zg0Wn0+oerw5lwZfyY6/eipMpDYN1LN19Xj76/BsFfHL4gej1t7vbfqXwICf5vzt9aCBiM484UCtYO80XiqYmKWJQ6NUtEZ8dnKj0rllj2cyxR9RBlr91JDZcvLPHCR9tVfCmnAZdU8GwrddzS4hCqM3Asj3jBAGDyeRmPmH5EWq98GzG7rZQX6yUpjDFug/pxvQgI+BrDZoNqQLd8C/eBpnLpsSifUGL4Zh2gqnSjk8NlYmk8OGnAQcaeWs+fYuvRTMYTqZ46MwHZxpDU7bMHuEq9cMq22abvJSiMMEpvU3iGHWVB4skOdRdEuKEWV5GHPvzEZSjXP1czSXiqaDHbpFpELzTvsJNPsQXFIXmCfKZqOl6qyX4KEx5sc0fhJNSRZrk5mVsPc81Bfff/JOdqLEHOg1Ak5S3YRTeoWTTBn72DlmqUAWskQV2w58QTwouCJQkFcWMkbjynr/33Qql35ZKFcDLo80axwqn9IVNwuKrfEH1wu++WMVNSKi5wTRv1ETzgE+LyKdNs98fyGEhVGUIif83zoFWyiz6eURQAwFOZITjwo8KpXuDTHpZNJF7q9P34E5Iy+MGXWAb8715B9e3/J2bdi+d3aCylMnSUJTXtPdZwmhBC1mgwce5tBKPkVXlUDZ9FircdVaCVgXsuVvQpKhnN97KsgaICtujWy3wwXdbe6n2oHE2/MdIot7Ns0jWwh59Big57zkc2hvOXNANlIAnaJfNcJ1MM4a7ZU3+Rfne3vj3TTgTsZ9Z+IAO9e7NaBay5qcBoLZ1t6wnfsPwi4M78kjmTAlfnUKORe9DhJ0S4F7VqaIJFwHVsNzL1vQVGI740JwAStBRlS2L9grYu1vHd/588+FbipjnU1x+xkYZTUZvb/4oauJDk1b/lnPLzWD8i0mwaLK5MbJTAzKxtoYRaVx3OAE2apa4xKSDufJOv4o/zgEge4M5Q91MNU6IHyGCse/fYf1DkSUGbnyOprpgdrYYUBvn3Lihu1PiudSFnc4XN3eBLqYlycUnQtj851WnXzgnKtROySeWQp3y4HSOZM3wIPdXdOYuBE9h9fgjC1satKajRwM0KULnr0m+nCkjthXjI3OfQZxAkAQuEVLBLxAWQjVC2UhzUT+HX2iMESZ3Vb2MFby6ksgwYvA40kPGe4UG4gd4JAinIZ2lVz7f37/S5Hqv9mi+kPM3cPWxpt2l9Ui7KInX68qNEHGeoLSxdBj/4eBVcWERi32kP9V2xLXiX0vNt5/I2d6DOmq1JUcuymk3fr/0uL7Q82tt6ALi5lVmAJy+8yL8CYvxgb4dxzHFnHtmXpjksuynL/k6j/uz88xAgymd94EiaZdwj+ggIcBch1SyR3cjPyi2NxDzqHUV14o90tCW5ckCvqrGt6EhJrD42baO1qfmYWEiGJRUeRFlylAo/ppwEtPK8Xvyic5awLQrYEPubQgcP9SjF/L0t9ZwBz05+4mi+iT88Koa5GxptVHTPldzZ4bUjdKwG9b8N2nnau/R63KlLAWD/uf505MtcReYSc+nvp87+FjZYYUlis+WzNzjkzRDSIOwWG2/LRFeZmTJUxqnhYWH1zIr91F01TKAlBcYUWQjB/kCD+LRVTdtJAsJSxyfm7B05n4QhMBemwtb6yZJctBqQH76aHsT1FNyABTU6HrhUvOKZGGn+rIOBFIkwrHFkbuzkRIUI25WyY3dH4s6vKorAhljaoTmyKwRMteDIlgM7iPxvYTsTagPJDW6W54tfehNaOZ2WXGbbbbTdU+IGDUadV7Mt1x3mA28hpUpokyHa/2z5NPXXAL5eS/CFPS62l3vjH2eLfjOmctKzTCW+Is3uD/ZvsxB/s1YxNqT47VRW10DIyWz8iO82A6oMKKpnUhv5E1dzN3hYMrEDGE1WOgkHDT9V5L0a1GS4TNhpxtt6Q2/RAU6k8XAUIehjWrF8zbgWHyFA7MuSgxVL28qGYWqR9Mrg8CpFAyUvV1R3rTcXLsT7GXJripGTPIeFqUq30ZooTmQrwbl887+aj/NA2YIxT1jf6KDED03YhcYnNUaDeKBm83KMj6wO3WJdOs4BUGrN9xj7z7wDLxTG4c/6RWtAx9UY6ROYqaDmIT5IDYIE45YUCxV1DJZRmLR6Q9Y78r6RuNvMMcGSIbduD4PlanMFlHM6//lWL3ry0iJoVVhRciLAvVttFi7h5SbwVs8GYDKLuTKQOmzejk7iQV6xZqaK2C7Iyjt4l3WLSG4PbOy9h146/F24n3+w8Pyp+/y/W91Ta/UHpNGSWCrDSpeuasEG1Q3LkGBOXay3SZ2RukwF7WtzRldlnnCaO/H63tEaZEhQxOgIEyvfevKPFrbx+VXNS0ZLn14cVFsl8KXhcSHb4CQFlsCkxe5PHOt9fkDUFR/AkflERkF0ibo6VQa+S0ZJPbUwEpUIcilqvRkSP8aGlXRpdLXn+xdIbOuN7JvdQ7vzXUjuf3gLJxxIKK2erWeW1QuWjJ5YlE96Ugri44eyBMmcaOrC4uQ9cKpABmZoVsHF1X1dIW+dkE8F92hbIYSJAV5zJuvm6IRnLwfypF/lewBNfRsw+ZiP4F/6R/u4IzdGJmE203q8S+ybWFJVRWo78fN3aAw8MKm3DwkzOVO23lfhlfWxP99+Vk9ELAJkJg2YsZ5ltp7od+wnCFGs3UtGFrckGNRx/L29b8u44WQPflW+qBWHXygIBPrzNtrQzPS05YWdHkpZC83MVtotqcfEn4JylHCZxzcmKy7FMadYyTKSumV62W9YgbI7pgIQNP2koJDDvZygGlp2yhhWN+Tl69w34e2zzHXkKJVvcQLdHcOqfQEXpBYzzcaO5KgQF5B8zaw1NNXAUiQTep7IDYghX4/91iRoh9dXoZnDdIdHzYz7sfmpy6/BHt/DwFYW3Xc2hXO5aFpOQtNgdmZCPZDxfJzKGHatBiNwBG4Qs4rZhglYI1fl7jzg2tH47F6C7Ei6c/j2p3xRLCjYcTC6av8qOkiJXOQm8HCW0vDyHqu2uLDM0rmx6MXrGf4qPHAPTDLnlYBXhiZQGr6LuuSgUYYIbFzDEjVMiqrSFE7b46BjUW/B3C/uIaUg3/SBp8Wcc+xUKjrtwGcVAlx99MnjUaGeFIACusXDal6NPRGri4e36t0cBMrcFiyk7Kus634bEmfzm2Fa+2TrTQNTvJT1oCDk3t+K0jdp4HUOO+JUXMsinNnS3X+rNTWI7ecg57hqk4qdlAIZADv0BwDRE2pDp5TwFJ39MxwR0hHc6c2gTBmRiGhiPmBMwACMaayUlCqnDMbJndmqb4XZ382B22JhYrxcRC1YXqkKMHHWqPIPOwVjE/eMt01Hn4jJc9I3Vw+9H7rKUAGXt3n+XsKBw4Tt9PQ+iR0PSTp2rOmUlzt8hwWqtDeSEajiFvzJpHrW7TGz89v1H+hwnRbI8K0sR4pC55jKnq4zWMOlxt6SL811gwLb1CV9CKfkYhA26u0BRtIAEehoEzUGnLqBtfk5CjgA1b1sOslbTO43Zhb5GryVCF0Vr1Trio9Q2N3biRPjQslw+24WI2B9Oks0XhipizJ0rLNrXdSzXNN5uxrirqBZhu7jxq/eDFGHb60UWYVosyEG+nmHgHIRI/pUtRQHxLRxd164Fb0NXqviCRHt3F6jdiKzIzDTP9M/bb3b6jL7Ym1E+3vj/t1TZfwwYXeOZ4w1TmcwQVN6GHxvKayvZ+xzLiiCc2saUeb7QYJi2l9SviNgPCeSSWKjVl3CesKCUTdEcNztRPl/ibZgzYakhHF1Tw2b6n9uwdxeTWWtpI0Ej9cVgSvrSqhCpqUEJnyfZC6ZtcWPgj1b5vILrptjfIHUYliMitabQAapVnB1UZt1Wjm8/1d/rn4c3V3A9treRafywsG+i7Js/lUsZr/+/ITpgF5pxXhJWfF45xNPWAdFnC3855kZVRp384kZzugKSDpagLvOhrNeuq1MkdJ1WWyd5jBtrCNG0xzdjwQ5GoCMw+BIRAQ9hLG184hrxowubmIo0vtAlVf2Rf7nIMKnRFUFELyCTG8WKF2DchOrh8Wj+sH+pi0I7o6IJjjAAM6qXPq/h4CzfGrpY3OL7YUqPAtCefraia2+CezwfwJtoKarcfDEboW5ozdNYWxe1GdA4chEYYk4f6YsF/A38w7EZtv/OqrtthNxeQMevBX0P6C69shZLhlB2YA2oJQbpyxEBionc+xsSSdTSKP/kdjQi7ZeS3uuLuelx1SynIcvCz67XJB5r3TsFhYiy+c2g4M5ET4iYhEY29R0ciuuEenamcV167oQ950byEQJp8RwcPkmCIeUufZE7IvMH2DpAegZjGf0TWfJ7X6FUokHb3YgFXAM1vMpJaDNGsJlkYTLrxygRopS+5U2p+mNv5X3BM3NLJoXgQUDw8RFTjLXXeLuXF1B6XnaDi1CellDkYEn2hmjyIOjMuYfGx2SUoGNDM50K5nO0L3ByRl0kizUh+C+UDr7iESlms+kTRZDJFAZ6zMBSnoK1aYhmk9H7/Wxl9UaDxrkVoVbE5OSNmjM2v69FRmGf/72J1YmPr36o3VpFhbCL+pPpsAfrnu46hYInLajO8SwMg833W4zWeR+Pl560ybxk5HQZDqvVq5ZgucAymxffCnkaCfqzB9NfjxF+8RQC00OlUIFfKS1MTZlRBSNwJ6SbMTl7tJw97ke6t4I83gLy3ekmbwEGCiwb5RiaRpWe3JHegzHm8XEQnAs2ZPx69RDYsGNGpYtDUsYyF/uFVKugG/ErWQDFtGGJFL8nCufmYXTusExHBYV61RATkgW7gowcc7hpiHfwT41cEEuNdi0tMad0wk4ZDjw6SypowmhhysGRDkNLl1fkksTTMLwD7I2KtS0K+YbHh5Zzbp15K41vq8gT7dc/Lph6So8HDnlyfNow8cZWPqQdxQvdkmPa2rXoVzfN73yd5Tk/RMRzdGfM3VZiB3CXtEUZp052rJ1bqkAI9Y1pkfmvFNjjuGVW2Dsj7qWWz574W2UNA7oNdGdPtO4iL6bnELvvqEFWBm34whNGNXv/xLHH/BWKa1OIEi7Uz/eEUWdVhnQRpNYQe8qzDrYLSnIWgc46w4uQuOdJOnBpqeB21kEeRSsEoLfVcpLJTPckxOjELk4oifAAa3HtztTlW6TJLFAvK9XYlkFTdsRBvyhz1qYdX8cpcEM2vLZZ/2KRLlz3PvEQ1RQZpX0pVM2bA16Qf/cFAMP62oFhzI5iktsr39HRYHT3NqSchrn3fF7UIcWzJyNyEb8RAQxFUuCN6JEbiqQiueroQ/kkWXm/FILXGIENpNA187377SmeZg4yZBOTmb1LRfKI82c3ymifw0i1H0fJ8U/kKK/K1ooP1A544OBWy1ROOWH+uMx+YuUh0rfY6xrYdvQowzUsYd/couAnJatS9dVkWg83YpUSp9iVj41uPXLW3d08C4HZmLt6R1QztVNKhAqXmFaY9sA84fYeSxFYJFJ/0Qldd5Kfp39fbVCWFm8sZcm57GlNPX9abh/N9GQQkeu0vlos3WXgjHbA+FZBdCzyd9bqVLKOC/6O9MvxY1zgO3KrazMTPgbi/g+iQnzbft+lA3hy0OxXi8UJCMfpbJ9rO2zjg0V7R48EDwpu62EwQImAaDw7+zt4aXrL4lLuW1qmWCScyca+xFsam9W8l3eVzM8FTTPdbkjToADRTRin44GYug4tnnxJC/GOvGUvhsboHmGVRQ5HVlflpcSbs1tZPlQxGkItaPg3v7lc+gyx/vCWJIFGlQDhIlQzfUyKT6HQDol08v58D/XH2drkLAvn0x3V2fR3Ap182r2wR2IJvVdZpyZI0HzkhjOBe8KifxcCrw124fMotLnZR15mtMvthmMrc3qlx3qOIc/ovE+qEs3YRh79xe28kEL5js4ToYoECad3g0FO/zzoVXukG8pyI1tQxpGEss4ENK7ubO2yeEVwkxAhL8UI+i1b6hhFZFvRA0S/YACDgu+wtDiydGr8+p9OcQIYwn6h6uzzfttTN6q2+N561edjpCOJ0y316PvF8tiN+Mt1OChY4YFK4kejaX8t821BGArf4Dw3sLmrukR6bnt+jbPoap78hxuQzIZUX18VLQ8CWg6LWGmmz0JEffHgm1FVTwyxh46U4i+ZWxftIpfQ9YeaPrFjtXvk2P1fgohhCSUlX5ruDWYU4tUUz+mhAwbBIM8LcpOcmweOp4BWuIl4op8DtM6KpfTGtQAMaqun76QdxrPBw+gSevnM0DSkfU+SZLdN+pPFeBPv7+AihYNs9J0c7x27xtv6tAPjM3XSPKlq+4DbbkCLWyCVT70MamsT1yl+aI4XmPIkFMghStGclxtLmi/676kksffazLNDxeeg99vC6qMWEHG7KIUut/6/rQns5bM8iX2VzHmFqsMf81UeULPIyM6fUmH5o6uMmFSpRIUGDTvOo7VsrW28H39qPu7A5Zu6jk1ExMszZZxpA4c/fWyDv9o7BX1n+sU+hT7itK6VAPBfqzpkCwThKBmIyGFvkRz8PyjdWNpFbPD3fhVMjeoCBbNYiaGubUGRJVJliS+d8FgPA/asRLXZhGnGSznxGLc1K1RmEEp+TjVjbCJImOgnIt7J1107eTYSkEGi1gvYSDm9XAdxqzKf0+ItuyPVqBI6nzCqWptiBDAXCSvrW+2Yh1RSWL4eKimTonO9U4W6NB2kFf90hnpgHjmaE7xJzcq7E3D+DNSUGFffgt8bOStrGtw/UgJ+m1PllO0/zo5QFieADb0QlUbdfXaXoVUZBdvLEbZV64vLREJHlTlF4XM2+7G82P0J6Piyl0EZBcQs04ZCozwx12HBOn9I3SqUCaovj0Fknc7YOCYUA0D6C7T2mtY2OG3PLIueulb/4w9yI6/3KgQp7YKhoQXqyDU0D4ib9w/c/Dpwz2zNUmQXlqIjlC5GmhG/cFLDdp+WBLGv96W3xNZMeQDkQQi+uejjxyatjO3wyGIPxq9KowGgP7m98voJuocEYTQeeXksIKRo8SjJkuIF9oCy/U/mbKbL5L6M+n+RuzhJYwn/8IeDlhUQyOfS04Yejo7AFU22jsSEUJjBWi5RmOfwqtaVe6Z0OPdR6rav4b7qIdlM663Z5SvL7nyrNAfWhGwCLp7rXt/UFd365Y+on7I/fgBlEKHtVvbUV03DwlRMCA91KxfLlXXE8/bAy5129DI7pfStKfjht9LiYA0CF1CjSJXhNWNKqIAIAdx8FSdCr1esn3Gzg6vfoOAUtv5qrBr+dmWGKgfZMy68VXYbn93dvwiAw/j1NIt+REycW4mgeiotDXGNyOTHyxTuc7RxY6roUe40n5EAjjG0GvRA6RQoVMWRPZgkbG+iR/P2+4yGbqMgUuKeVh7+AEhtMbctVtAzjIT6raZNUj13ljYyr7oBMXcqt8kffAg5jEoSwvqENqRv18VeNkvHRxYyev2gkShsjgXS6+LXsLHa/BattJTT6/Ja8gYwuKR0cfHsMCj7+VTseU8nd3ZqH+ICoKulRxIPUorqQ9DgnucloaON7V3hE/EPCQUqoJ9ic4zT4hXolwDzqc2JY608WGDD05gz3pOglTLVVwzA00rsrPoWrvq6HemA/ZA7H5grmbFHu6F7Xy55q+lSLhg1HUyXvOfk93WQ5Q+YCAp8YSF1DVjpz9Kt9yRGaJvPnVWBhWuD8DMY96T52Wq748a0D0JY4ND0JGgld8l5Z/cFc5WvsLNpLREljcnIjePOpjEL4KXxzeapNch/XububZq+T0jOTG8XO3afHlBZzvZaX3wfvWvKptni3ZTPcC+scBQHBXjok8UTodPqwcOnMfwYi7ZZzee+TgDyC3yW5rTVdfAp8ugN0BRwQ5mcJhqmWK5mhuT5u0uoIIGD2ZJ1eK2ChJvHbd1eK8WXJEgHv1lwelKlTcYf7+16MFawUjhClIl4Umx5rl+z1r2M7R7LfS6K8LACVeVEbSl1ZtEhV6jkpwHsrZylsP5Utd6f0hsGxtVmGRWQcEkVbp4DaVzfCr6gwF5wvQdeqDHsHjnJ8kphe0lxVuwZfKWjKpHeiqCN9qu9X7Yor5pnqRjl/I4tKxgrsoPc/h4+3LH8o3paJMB6SW9PNnM7PRYpf7f1lnAb6jjor25SnbEdwUWU2rWUkbgOplmv2zw3rQjTPXgdrBEG226tdVK+U9oBxEAeclJRlI5QM8GsAym1meO/zE7Fnsa6d6IYCq5ijzeiRBc5Sf6Im+C4TnbVCCjPdYK8ZHRJbAF/IEa0koSfpx5vokxiB6aI1MwMGLOB2qM6JZBCmw1V7uWX8L9SnfjbZBuxUNWRy9aQEsrZu7q+f/p1mBl+T3sAlcvIqSXy6NmURhFSOZ+hwaKQYr69T4Ah111WG0IaA/sUh/xOJBIMOL9/t1SmCVRR03nZ6tTSzxMg36dKyBQnksfpJLQ/DeRKLZI8GOwWD8+htp8YpePEn6kwQ7p9nxQJfQB2pBmRxf6oT0xsioqJ3kMZWyil7dUSaVWZDyGLiF4WkXCGzMtbq+56xqI5VRBqIWP0bBeH9/sGqxb7r3qZrhU9kgS4ziBmG6lggmvfdUgzZ1j1y0qYsNQ9dSMVJBiY7+OrOXu86LKb5DQ4mF7Szo222F/1iMiHOwxjCeU37lhqDInqX4YdNXfpxx5CymqknAG5t1dZEceQkghFrIHIItAUp7rQ68a2Xlb0Y+ENIu1CmHdJGuzbOVYmS+uJiNNEUMojnz+t8fMEVX9FAtMtesB1ydQhjsu63EkIhYjEAnJDJbx+OKj1azCJ09uXjS2NCEn8S6ONopdi5uGSKncUuyZQqUfO0S8xL3oBaPMlueLuqmbBAc8greA0Vzud9tCqPMD79DopYXcTiV22qm2Zu+b+P8efPFrOW1MywhdsCPtY3XfHA9MzHGrqU/nqmvqymF4vC38AUBypUvApAVKZZY3jEzvtLI1u7CueDcImr2CI2Qz8KHyNwDyI5ZoJ7asb+oRaCQ/QSqm8XbfO4LLv3PKK9l+tI/iQBRrNWInIlap/wDLAiR3pUtm9tHVeiFsOdT0/dCmcnTYqiM8Qmi6XnVVFD/fvAz0VkwK4badprteoilcKZ6+Nqonwv794139HMoGA4iVta6UOI3dQ6KKwZfsdajC8aywxyYZ93nu2UBgr1huUN+UaWqDZgIhVWLuDYLr4iY7jHCw6OE/k9qwwY6dVVKd225X3UAPHW4+TeX5dtFIe9xkJ6nRSMuprI9ftlLYECxUlnZblfjtAa4v0OnNisL87039uHpYj7gJ8dF3JR4aIXHX6m8MdvngxyJpLOntKmPLBqbqwW6WmypHMTTJE+ALUyK7X9wfkj2p8Qq5h1DCOx2DCyuuCyss7OwiL/5BcsejaLn1woZR7Me9XOdt/s5zSM7yQZwd1qUAfM6oNCSR8gVXbsmJZJKctUBCuBQrKBFk8TNcJJpA61kyZDGfBruQQujYLq/Alz5S4s9M0tb51/dGwstVmgs2k+OubFLS2JqPcAiNCWnEVXAZ0pCkc0y6fsWo8WppIwU9GFIEFlLsL1YLvGBiVgzKWoKVIM74ZV0ZNYKN4xlcFuYF1DkI5xl/K9+e+J9SsxZFETAEz/t9efLQ+swHQBqDl4OpjIwRTXNkqTmD8u/wUDX+ZBhBs3N2/609S8xBhaL785+u/ehIfy8aknHXQDBVjc7EADMS01rOUAkXJGF8mJmqyRzgtWUUxRZevABKga9BkBEWCm2Bb8cwGrjAw6aSVyr5H/NoEDmoqLSgoGjVqHNG9kTAes3jnjP4BfqZ9T9cQoH59er92bNivMDwyMaJ/vdEFFahrLlWrVfqbGEorkmREHb2vbh8M14EWA5SwmfZ2cMFXFccKV3rRauwd8vtZ2fCJPKhWmDbS71X3K/3cvHoJdwyRi/0wLZiozJHFXV2uFBPAw8eqE6UFqeYx1WlGeHiwjph7nR/q0MWwG65EqCb4cnRYuNpmU7UGI8BqFIMzdR6sCVfn1wH2mDin3EFwqjYZSTPhZ0yw1s1j78yKAgbgC+XdAtRmkATmU/oIJBzBaKji4z742occnGbpJeFGQr88VmldlJ88dM4Tw+yILXAvjg+CM+afPjvode97EAbTx4z6bCpGxKu5fOUsdlgiOEZpbpZpN6zokYoQt7C0wciIYi8ywXLTvUXUKT350EIrMi9nWaumejhYuioem1941SKM3oexKZJObr3531ZylxoK6OwuBylURnlomaJz3cRMkl0kx2OKViO6YeWRZAtJpZB2NX6QDw/U0RcVPtxRvu/AE0OQsegbMjK40ox7trJvsSFF8lRYx+GQNi6lrBO/nEcD1MBifYp4t7zEeT2IqfT6SdAy+c80WXNH2VDxYfWI8KE0a+PgXtgPsA2DH96L+gpKyLj2bHqXGXFyKVSlFMwiYiLZL/4rnN1OZKi2StnlGT6VQNBf5nSq+vdxnMpgelfwG22kYnnKVTgX8DDkzH+XmNGHY446ZfmlkRHp3OvWZqsXc6YmW6lCDTOW5W5x6901Dxo6op4SE8IhR+BvZJ1idl/Sij8HRV1n90TEHXAOe1DJO/e3MEy1cSmdFN1zTdtDgSlF0CceTFhPLYbwIgKemf8HLNDGwGJn90bpcVoq7yIj5oDfeaT1qbA7bATIB0F4jWFPbmMgWaWCSCwyx0B+VocFyhwRfFBIUvBBssn998PHGWXeQFcdavo78dJTjwEPIxcc536YQGvqOds+QuIm8dGm7UkHxuauOtZv9M2C5d+BJArimkaL2WMgEoKsfGDppZmQ1aivXWHFsCuCtH6QbEMhDHzD79MarYTaZAbWVkeA4cgmZfxzExi7HHxowj1fv6KWPIIFIZljAI/9iwj4GcH/henCT7Q/Z9P9M2ru5fZVuApBwR/IbWRe9pFZkA041ppaMXsZ7jH6KQyelEJJXn2vOAvDnJv8eV1fiHzUc5OCeqAKFJtoL5pw9GT7kGzX9mM6UixaovYEZih3ulEgQvCyab6D+0151tJaNHLvkt/+8EKHtnLJI2snciDdmnB5w/6SQ2X6XX4vuOeZYiXk8rbUQXGD/C2+IMHJzumWr1hLWcC0KARbEVhJPuwP2ad+cFH15eC1yYHCyOhaLXsHccqrhm3e2+7ArXKjOydzCCGMJpMnNueEEiMQ9L19uksIob4rYMA0561pMpyVU9I3fJyJ4bFfKoltzkwXrrFb04QAR5iPslU9dCjXkwO2eduG+CNo+jNqG/nEcbsnpUS06ZCXxz6SIpbQ2crqRIOOxGQDlOxh4n5sia3g95fDN7cy2iJP45KEJCl78UXQS8TRS/heouMnbqXQ/Mk2C/Dy+sBmyVd+ZS08RFmFW8RrF1ib06GqhtNwiQPhvxQzicuutmsRIAjSrB8UyH9euqFX2mj1sklfWdt//InfjVomygqeV2hmfSBHuJfWqEeZMaxtFePKkvr5FQwBD3U5INzYN/Bd+ROReJbn0PuNg1ZCIB/ekmt7sNPg9b8BtUjzCoGdoO2Jnjen+YnAkRXCxgdkMx6sw9iDiE365qTmdUMtxp3p2lgDYrlBORTIVLfvBD537YUzULml6H5yp34lvtixyClGcDk23QmH7iH0nLnO/86rAS1jT6+Bxhiu5IaFF3AHXnUtLB3l+Dk6xaf8/xEQADV9Ujz+e9GKTGDYI003vsHDAo8BBJpdFahhEe9qVAq4uBzGD/fEbxutwzQf0o0venJUt6vmHfl6/DZ5xgYokcShwNNfpDNOd7qAgk+8VpoY5UOQ8ejeIcMaliTBNucU2/i3cmKHbL2JX0Cb/43UVVSc2FMv10rOctAUZr8nDmz2eUUyYgEtbDHHBoYSS0Ramz86ZVTLGdjZioNQqwMbiL0e0j6mPbXX/PDOhFCP+6UgcvcY8ESCyF4KujyGn57ZSf0TkJxp9BIsnfiaCeeAke/Euw+a7mhNC0kqwq/6M6ray2nPN3yj8rSa7o5Hv8I78hCC0WzfjPkdMSQwAhNcvhmsDgdRcsUDKeovIMiVxNUvVlKr83D8KhF0rjs8yMG7VOa+biS/l5uMrb1GLUTOzxzjczr9CsUcqqb0+j/6SKNpD2Zv5609tat6Q/bZtcG5sn3l6wPwevSasqh8M4zABDVqjxsJILg==
        - #2:
          - type: tool-call
          - toolCallId: P3yowYG0Bzo1IiHa
          - toolName: set-policy
          - input:
            - Rationale: Adopting Iron Curtain will grant free Courthouses upon city annexation, which is vital for managing our happiness and integrating newly conquered cities. It also provides a massive boost to our internal trade routes, enhancing both food and production to fuel our war machine.
            - Policy: Iron Curtain
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: is7dvwiPqFV1202H
          - toolName: set-flavors
          - input:
            - GrandStrategy: Conquest
            - Flavors:
              - Defense: 40
              - Happiness: 80
              - Gold: 60
              - Science: 60
              - Espionage: 90
              - Offense: 60
            - Rationale: We are currently Unhappy (49% happiness), causing a severe combat penalty to our military. Prioritizing Happiness (80) is critical to restoring our combat effectiveness. We are also shifting our military posture to be more offensive (60) to actively capture enemy cities and capitals before Austria can secure a Diplomatic Victory. Gold and Science are boosted to sustain our large army and maintain tech parity.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: NeXTbfmlbGgoyyAN
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
          - toolCallId: P3yowYG0Bzo1IiHa
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: is7dvwiPqFV1202H
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.