- row:
  - game_id: 7f219acb-6c23-49dc-bde1-fa1602646bf5
  - player_id: 4
  - turn: 427
  - player_type: GLM-4.7-Simple
  - prev_use_nuke: 85.0
  - after_use_nuke: 90.0
  - rationale: United Nations grand strategy maintained - diplomatic victory in 6 turns (20 delegates vs Siam 17). Increased Gold (95) and Diplomacy (95) focus - need to secure UN delegate lead through city-state investment and diplomatic units. GreatPeople up to 80 for accelerated Great Scientist/Diplomat generation supporting both tech race and UN vote. UseNuke increased to 90 - with 6-7 Atomic Bombs building and Zulu military supremacy (134K vs 9.6K), nuclear deterrence is existential. Offense up to 55 to maintain Japan war momentum for capitulation. Air maintained at 85 for Stealth Bombers and air defense against Zulu threat.
- originalModel: openai-compatible/GLM-4.7@medium
- model: openai-compatible/mistral-small-4
- modifications:
  - systemModified: true
  - messagesModified: true
  - activeToolsModified: true
  - metadata: undefined
- extractedColumns:
  - replay_nuke: undefined
  - replay_use_nuke: 85.0
  - model_friendly: openai-compatible/mistral-small-4
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
    - You are Askia, leader of Songhai (Player 4).
      
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
      - Name: Songhai
      - Uniques:
        - Unique Unit: Mandekalu Cavalry, Replacing Knight (Requires technology: Chivalry)
        - Unique Unit: Sofa, Replacing Crossbowman (Requires technology: Machinery)
        - Unique Building: Tabya, Replacing Stone Works (Requires technology: Construction)
        - Unique Building: Gumey, Replacing Caravansary (Requires technology: Currency)
        - Civilization Ability: Triple Gold from destroying Encampments and plundering Cities. Land Units gain the Amphibious and War Canoes Promotions.
      - Leader: Askia
      - PlayerID: 4
      
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
      - Electronics: Allows you to build the Police Station, increasing City security level.
        Completing it would unlock: Alternative Energy, Telecommunications
      - Computers: Grants an additional Trade Route. Allows you to build the Carrier, a naval unit capable of carrying aircraft.
        Completing it would unlock: Telecommunications, Satellites
      - Stealth: Allows you to build the Stealth Bomber, the most powerful Ranged Unit in the game.
        Completing it would unlock: Globalization, Nuclear Fusion
      
      ## Policies
      - Communism (Level 1 Tenet of Ideology Order): Communism: Gold cost of investing in buildings reduced by 25%. +20% Production when building Wonders.
      - People's Army (Level 1 Tenet of Ideology Order): People's Army: +100% Production towards Military Academies, and receive 5 Free Military Academies in your Empire. Public Schools produce +5 Culture and +2 Happiness.
      - Hero of the People (Level 1 Tenet of Ideology Order): Hero of the People: Great Person rate increases by 25%. A Great Person of your choice appears near your Capital.
      - Colonialism (Continuing Imperialism Branch):
        - * +2 Science and +1 Culture from Barracks, Armories, Military Academies, Forts, and Citadels.
        - * Each unique Global Monopoly modifier is increased by an additional 10% if it's percentage-based, or +3 otherwise.
      - Honor (Continuing Authority Branch):
        - * All Military Units gain the Conscription Promotion (+10% Combat Strength).
        - * Supply-free military Units spawn near Cities that reach (or have already reached) a multiple of 10 Citizens for the first time.
        - * -25% War Weariness.
      - Double Agents (Level 1 Tenet of Ideology Order): Double Agents: Receive 200 Spy Points. Gain 125 Science when you identify a foreign Spy, scaling with Era.
      - Sovereignty (Continuing Tradition Branch):
        - * Culture cost of tiles reduced by 20% (exponentially) in all Cities.
        - * Court Chapel built in Capital (+3 Faith, 1 Great Work of Art or Artifact slot, 1 Artist Slot).
      - Splendor (Continuing Tradition Branch):
        - * Expending a Great Person grants 50 Culture, scaling with Era.
        - * State Treasury built in Capital (+4 Gold, +2 Culture to all Monuments, Gardens, and Baths; 1 Merchant Slot).
      - Liberty (Continuing Progress Branch):
        - * +2 Gold in every City.
        - * +25% Tile improvement rate.
        - * A Worker appears near the Capital.
      - Nobility (Continuing Fealty Branch):
        - * +1 Happiness and +2 Gold from Castles.
        - * +2 Gold from Armories.
        - * +100% Production towards Castles and Armories.
      - Refinement (Continuing Artistry Branch):
        - * +2 Culture from Great Works of Art.
        - * 1 Specialist in all cities does not produce Unhappiness from Urbanization.
        - * +1 Culture from Specialists.
      - Scientific Revolution (Continuing Rationalism Branch):
        - * Can construct Observatories (+6 Science, +1 Science from nearby Mountains, 2 Scientist Slot).
        - * +2 Science from Jungle and Snow.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Free Trade (Continuing Industry Branch):
        - * Earn Great Merchants 50% faster.
        - * +5 Gold from International Trade Routes.
        - * -2 Unhappiness from Poverty in all Cities.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Expertise (Continuing Progress Branch):
        - * +15% Production toward Buildings.
        - * Cities earn +10 Culture when they construct Buildings, scaling with Era.
      - Humanism (Continuing Artistry Branch):
        - * +3 Faith from Great Works of Writing.
        - * -25% Golden Age Points needed to trigger a Golden Age.
        - * +1 Happiness from all Guilds.
      - Trade Confederacy (Continuing Statecraft Branch):
        - * +25% Yields for International Trade Routes.
        - * Trade Routes to City-States generate +1 Influence per turn (with the target City-State) per each owned City-State Trade Route (up to +5).
      - Foreign Service (Continuing Statecraft Branch):
        - * Receive 100 Spy Points.
        - * Earn Great Diplomats 50% faster.
        - * +50% Rewards from City-State Quests.
        - * +1 of every Strategic Resource for every three City-State Alliances you maintain.
  - messages:
    - #0:
      - role: user
      - content: # Strategies
        Strategies: existing strategic decisions from you.
        
        ## Persona
        - VictoryCompetitiveness: 8
        - WonderCompetitiveness: 3
        - MinorCivCompetitiveness: 4
        - Boldness: 6
        - WarBias: 7
        - HostileBias: 5
        - WarmongerHate: 1
        - NeutralBias: 3
        - FriendlyBias: 1
        - GuardedBias: 7
        - AfraidBias: 3
        - DiplomaticBalance: 5
        - Friendliness: 1
        - WorkWithWillingness: 7
        - WorkAgainstWillingness: 8
        - Loyalty: 6
        - MinorCivFriendlyBias: 4
        - MinorCivNeutralBias: 5
        - MinorCivHostileBias: 5
        - MinorCivWarBias: 4
        - DenounceWillingness: 6
        - Forgiveness: 4
        - Meanness: 5
        - Neediness: 5
        - Chattiness: 4
        - DeceptiveBias: 2
        - Rationale: Increased Air (85 from 85 maintained) and Ranged (85 from 80) to capitalize on Heavy Bomber production (Tombouctu, Kukia, Tondibi all building Heavy Bombers) and upcoming Stealth Bombers. Air power proving decisive against Japan (destroyed destroyer, dreadnought, aircraft). Diplomacy (80 from 75) prioritized for UN vote in 7 turns - must secure delegate lead vs Siam (20 vs 19). Defense/CityDefense at 85 remains appropriate given Zulu military supremacy (134K vs 9.6K). Nuke/UseNuke at 100/85 provides existential deterrence. Offensive posture sufficient (45) for Japan steamroll while consolidating gains around Kyoto/Tokyo against counterattacks.
        
        ## Technology
        - Next: Stealth
        - Rationale: Stealth Bombers (135 ranged strength) with first-strike capability are highest military priority. Zulus have Heavy Bombers and Mobile SAMs; Stealth provides decisive air superiority for both Japan war conclusion and Zulu containment. Current Heavy Bomber (event 211-212) in Jenne shows air power is effective. Advanced Ballistics completes in ~3 turns; maintaining Stealth research queue ensures we can counter Zulu air threat when it arrives (they have 68 techs vs our 67).
        
        ## Policy
        - Next: Hero of the People (Policy)
        - Rationale: Order Level 3 Tenet (+25% Great Person rate, free Great Person) optimal timing. Free Great Person provides immediate strategic flexibility for tech acceleration via Great Scientist or military via Great General. Great Engineer also generated in Gao (event 205-206). With UN vote in 7 turns, accelerating Great Scientist helps close tech gap vs Zulus (68 vs 67 techs) and unlock spaceship components if diplomacy fails. Hero of the People synergizes with current GreatPeople flavor (70).
        
        ## Relationships
        
        ### Brazil
        - Public: 0
        - Private: 0
        - Rationale: Brazil capitulated this turn and is now our vassal. Resetting relationship modifier to 0 since vassal status overrides normal diplomatic calculations. Brazil contributes resources, gold per turn (negative will be managed), and provides vote support for diplomatic victory considerations. Their single remaining city (Rio de Janeiro) is effectively under our control.
        - UpdatedTurn: 193
        
        ### The Netherlands
        - Public: 0
        - Private: 0
        - Rationale: Netherlands relationship remains 0/0. Netherlands is effectively defeated - only 1 city remaining (Arnhem) with Breda just captured by Songhai. Maximum hostility served no purpose previously. Netherlands will likely capitulate soon or be eliminated. Strategic focus should remain on primary threats: Zulus (4 capitals, 50% Domination) and Japan (6625 military strength). No need to expend diplomatic resources on a defeated secondary enemy.
        - UpdatedTurn: 353
        
        ### The Zulus
        - Public: -60
        - Private: -60
        - Rationale: Maximum hostility following Zulu war declaration (turn 404 events 141-145). Zulus now the primary existential threat with 18783 military vs my 10089, 5 capitals (62% Domination). Peace treaty expired and they chose aggression - must reflect total war posture despite shared Order ideology.
        - UpdatedTurn: 405
        
        ### Japan
        - Public: -60
        - Private: -60
        - Rationale: Japan hostility maintained at maximum (-60/-60). Despite Japan capitulation events and trade, Japan remains active opponent with 10,878 military, declared war, ideologically incompatible (Autocracy vs Order), and our Japan front war score improved to 56% favorable with steamroll posture near Kyoto. Maximum hostility appropriate for dangerous secondary opponent continuing to resist our advances.
        - UpdatedTurn: 407
        
        ### Korea
        - Public: -10
        - Private: -10
        - Rationale: Korea remains Order-aligned vassal of Zulus (-10/-10 unchanged). Despite shared ideology, Korea is actively opposing war efforts. Zone 1057 shows Korean units coordinating activities; they remain Zulu proxy force. Not worth diplomatic capital to improve relationship while Korea supports primary threat. Low negative acknowledges weak military (1740 strength, reduced from 1800+) but maintains war pressure needed to contain Zulu influence. Focus remains on Japan capitulation and Zulu containment.
        - UpdatedTurn: 423
        
        ### Siam
        - Public: -10
        - Private: -10
        - Rationale: Siam relationship maintained at -10/-10. Despite shared Order ideology and relatively weak military (714 strength), Siam is Zulu proxy with 2 cities remaining. Siam proposes United Nations (could enable diplomatic victory for me if elected). Low hostility acknowledges Siam's weakness (only 0.2x my military) while maintaining war posture. Siam provides 19 delegates - capturing Siam could reduce competing votes vs Zulus for world leader, but Zulu threat (134K military) requires prioritization over secondary conflicts.
        - UpdatedTurn: 426
        
        ## Strategy
        - Rationale: UnitedNations grand strategy remains optimal. Diplomatic victory achievable in 7 turns with current delegate lead (20 vs Siam 19). Gold (1318 at 22 GPT) and city-state alliances (Dublin, Palatium, Antananarivo, Lutetia, Harappa) maintain diplomatic influence. Science (2971/turn) and Stealth research provide military security against Zulus. Japan war progressing favorably (zone 19051 favorable 3:1 strength, captured Kyoto/Tokyo). Strategic Defense Systems completing across major cities strengthen air defense. No strategic changes required - focus is diplomatic vote preparation and military technology advancement.
        - GrandStrategy: UnitedNations
        
        ### Flavors
        - Offense: 45
        - Defense: 85
        - Mobilization: 55
        - CityDefense: 85
        - MilitaryTraining: 75
        - Recon: 30
        - Ranged: 80
        - Mobile: 55
        - Nuke: 100
        - UseNuke: 85
        - Naval: 80
        - NavalRecon: 25
        - NavalGrowth: 25
        - NavalTileImprovement: 20
        - Air: 85
        - AirCarrier: 60
        - Antiair: 80
        - Airlift: 30
        - Expansion: 0
        - Growth: 50
        - TileImprovement: 50
        - Infrastructure: 60
        - Production: 70
        - WaterConnection: 0
        - Gold: 90
        - Science: 90
        - Culture: 35
        - Happiness: 75
        - GreatPeople: 70
        - Wonder: 5
        - Religion: 20
        - Diplomacy: 75
        - Spaceship: 10
        - Espionage: 75
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: The Zulus
        - Songhai:
          - CapitalsControlled:
            - Kyoto
            - Gao
            - Rio de Janeiro
          - CapitalsPercentage: 37
        - The Zulus:
          - CapitalsControlled:
            - Seoul
            - Assur
            - Ulundi
            - Sukhothai
            - Amsterdam
          - CapitalsPercentage: 62
        
        ## ScienceVictory
        - Unlocked in the Information era
        
        ## CulturalVictory
        - CivsNeeded: 4
        - Contender: The Zulus
        - Japan:
          - Influences:
            - Siam: Popular (64%) - Rising (22 turns to Influential, tourism/culture ratio 874%)
            - Korea: Popular (51%) - Rising (61 turns to Influential, tourism/culture ratio 243%)
            - The Zulus: Familiar (39%) - Rising (158 turns to Influential, tourism/culture ratio 193%)
            - Songhai: Popular (58%) - Rising (55 turns to Influential, tourism/culture ratio 237%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Korea:
          - Influences:
            - Siam: Popular (63%) - Rising (32 turns to Influential, tourism/culture ratio 645%)
            - The Zulus: Familiar (46%) - Rising (179 turns to Influential, tourism/culture ratio 180%)
            - Japan: Familiar (29%) - Rising (566 turns to Influential, tourism/culture ratio 154%)
            - Songhai: Familiar (32%) - Rising Slowly (tourism/culture ratio 112%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Siam:
          - Influences:
            - The Zulus: Familiar (35%) - Rising Slowly (tourism/culture ratio 15%)
            - Korea: Familiar (44%) - Rising Slowly (tourism/culture ratio 25%)
            - Japan: Exotic (24%) - Rising Slowly (tourism/culture ratio 17%)
            - Songhai: Familiar (30%) - Rising Slowly (tourism/culture ratio 11%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Songhai:
          - Influences:
            - Siam: Popular (66%) - Rising (28 turns to Influential, tourism/culture ratio 673%)
            - Korea: Familiar (44%) - Rising (135 turns to Influential, tourism/culture ratio 182%)
            - Japan: Popular (55%) - Rising (58 turns to Influential, tourism/culture ratio 280%)
            - The Zulus: Familiar (47%) - Rising (113 turns to Influential, tourism/culture ratio 205%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - The Zulus:
          - Influences:
            - Siam: Influential (104%) - Rising (tourism/culture ratio 1097%)
            - Korea: Popular (92%) - Rising (4 turns to Influential, tourism/culture ratio 449%)
            - Japan: Familiar (37%) - Rising (119 turns to Influential, tourism/culture ratio 233%)
            - Songhai: Familiar (42%) - Rising (119 turns to Influential, tourism/culture ratio 193%)
          - PolicyPercentage: 100
          - InfluentialCivs: 1
        
        ## DiplomaticVictory
        - VotesNeeded: 41
        - Status: World Congress - Voting in 6 turns
        - ActiveResolutions:
          - Global Peace Accords:
            - Description: Unit maintenance costs are raised by 25% Gold. 2.0x Warmonger penalties for capturing cities and declaring war, and 0.5x Warmonger scores decay.
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
          - Songhai Sphere of Influence: Palatium:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Songhai Sphere of Influence: Lutetia:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Siamese Sphere of Influence: Luba:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Scholars In Residence:
            - Description: Civilizations have -20% Research cost for Technologies already discovered by another Civilization. Additional -2% for every City-State Ally, up to -50%.
            - EnactedOn: -1
          - Siamese Sphere of Influence: Jakarta:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Siamese Sphere of Influence: Ecbatana:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - World Ideology: Order:
            - Description: Designate an Ideology as the official World Ideology. Civilizations following the Ideology get an additional Delegate, plus 1 Delegate for every other Civilization that follows the Ideology. Public opinion in favor of that Ideology is increased for all Civilizations. Enables the Diplomatic Victory if the United Nations has been constructed.
              Available once any Civilization discovers Nuclear Fission.
            - EnactedOn: -1
          - Dutch Sphere of Influence: Antananarivo:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - World Religion: Buddhism:
            - Description: Designate a religion as the official World Religion. Civilizations who have a majority of the cities in their empire following the religion get an additional Delegate. The founder of the religion and/or the controller of its Holy City receives additional votes based on the number of Civilizations following the religion. The religion spreads 25% faster, and its Holy City receives +50% Tourism. There can only be one World Religion at a time.
            - EnactedOn: -1
        - Proposals:
          - Enact: Sanction: Songhai:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - Proposer: Japan
          - Enact: United Nations:
            - Description: Begins the United Nations project. Once underway, Civilizations can contribute Production towards its completion by selecting it in the city production list. When complete, Civilizations receive bonuses based on how much they contributed.
              : United Nations wonder appears in Capital. (Receive 1 Additional Delegate in the World Congress for every 8 City-States originally in the World. Also, when you expend a Great Person, earn 25 Influence with all City-States you have met. Triggers a Golden Age, as well as the United Nations Special Session of the World Congress if the world has reached the Atomic Era.)
              : Receive an immediate boost of 25 Influence with all City-States. The Consulate National Wonder appears in Capital. (Receive 1 Additional Delegate in the World Congress for every 8 City-States originally in the World.)
              : Receive a free Great Diplomat.
              Available once any Civilization discovers Atomic Theory.
            - Proposer: Siam
          - Repeal: Global Peace Accords:
            - Description: Unit maintenance costs are raised by 25% Gold. 2.0x Warmonger penalties for capturing cities and declaring war, and 0.5x Warmonger scores decay.
            - Proposer: The Zulus
        - Contender: Songhai
        - Japan:
          - Delegates: 10
          - VictoryPercentage: 24
        - Korea:
          - Delegates: 9
          - VictoryPercentage: 21
        - Siam:
          - Delegates: 17
          - VictoryPercentage: 41
        - Songhai:
          - Delegates: 20
          - VictoryPercentage: 48
        - The Zulus:
          - Delegates: 14
          - VictoryPercentage: 34
        
        # Players
        Players: summary reports about visible players in the world.
        
        ## Player 0
        - Civilization: Korea
        - Leader: Sejong
        - IsMajor: true
        - OurOpinionToThem:
          - You have both adopted the Order Ideology. (999)
          - You have denounced one of their declared enemies! (11)
          - Our real approach is War.
          - We have divergent Social Policies. (-3)
          - Our leader has expressed a public opinion to this player (-10).
          - Our leader has formed a private opinion to this player (-10).
          - Religious differences strain your relationship. (-30)
          - Your spies were caught stealing from them. (-33)
          - We defeated their proposal in the World Congress. (-36)
          - You are at war! (-99999)
        - TheirOpinionToUs:
          - You have both adopted the Order Ideology.
          - You are not competing for cultural advancement.
          - We fought together against a common foe.
          - You have denounced one of their declared enemies!
          - You have no contested borders.
          - They are spreading their own religion, but you converted some of their cities to your religion.
          - They disliked our proposal to the World Congress.
          - We have divergent Social Policies.
          - Religious differences strain your relationship.
          - They fear your warmongering will end this world in fire! (They strongly dislike warmongers.)
          - You are competing for World Wonders.
          - We have denounced them!
          - We defeated their proposal in the World Congress.
          - Your votes opposed their civ's interests in the World Congress.
          - You are at war!
        - Score: 1650
        - Era: Atomic
        - Technologies: 66
        - Cities: 4
        - Population: 104
        - Territory: 142
        - Gold: 720
        - GoldPerTurn: 143
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 2112
        - TourismPerTurn: 813.75
        - CulturePerTurn: 1264
        - PolicyBranches:
          - Progress: 6
          - Order: 5
          - Rationalism: 6
          - Artistry: 6
        - ResourcesAvailable:
          - Wheat: 1
          - Sheep: 1
          - Gold: 5
          - Paper: 9
          - Pearls: 3
          - Cotton: 1
          - Salt: 1
          - Aluminum: 5
          - Bison: 1
          - Perfume: 1
          - Olives: 1
          - Deer: 2
          - Iron: 2
          - Coal: 1
          - Fish: 5
          - Cattle: 1
          - Horses: 8
          - Oil: 1
        - FoundedReligion: Confucianism
        - Relationships:
          - Siam:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 0%)
          - The Zulus:
            - Distance: Neighbors
            - Our Master (Capitulated)
            - Open Borders
          - Japan:
            - Distance: Far
            - Denounced Them
          - Songhai:
            - Distance: Close
            - War (Our Score: -6%; Our War Weariness: 2%)
        - Votes: 9
        
        ## Player 1
        - Civilization: Japan
        - Leader: Oda Nobunaga
        - IsMajor: true
        - OurOpinionToThem:
          - You have adopted their religion in the majority of your cities. (60)
          - We passed their proposal in the World Congress. (36)
          - You have denounced one of their declared enemies! (11)
          - Our real approach is War.
          - We are completely untrustworthy to them.
          - They have some early concerns about your warmongering. (-2)
          - We have divergent Social Policies. (-3)
          - Your spies were caught stealing from them. (-33)
          - You stole their territory! (-50)
          - Our leader has expressed a public opinion to this player (-60).
          - Our leader has formed a private opinion to this player (-60).
          - You have chosen to adopt the Autocracy Ideology, but they believe in Order. (-999)
          - You are at war! (-99999)
        - TheirOpinionToUs:
          - Your votes supported their civ's interests in the World Congress.
          - You have denounced one of their declared enemies!
          - They liked our proposal to the World Congress.
          - They have happily adopted your religion in the majority of their cities.
          - Your recent diplomatic actions please them.
          - We are completely untrustworthy to them.
          - They fear your warmongering will end this world in fire! (They overlook modest warmongering.)
          - We have divergent Social Policies.
          - You plundered their trade routes!
          - We defeated their proposal in the World Congress.
          - Territorial disputes strain your relationship.
          - We have denounced them!
          - Your spies were caught stealing from them.
          - You captured their original capital.
          - You have chosen to adopt the Order Ideology, but they believe in Autocracy.
          - You are at war!
        - Score: 2822
        - Era: Atomic
        - Technologies: 62
        - Cities: 19
        - Population: 410
        - Territory: 656
        - Gold: 7293
        - GoldPerTurn: 69
        - HappinessSituation: Happy
        - HappinessPercentage: 51
        - MilitaryStrength: 13121
        - TourismPerTurn: 958.55
        - CulturePerTurn: 1999
        - PolicyBranches:
          - Fealty: 6
          - Autocracy: 8
          - Imperialism: 6
          - Authority: 6
        - ResourcesAvailable:
          - Wheat: 7
          - Sheep: 7
          - Cloves: 4
          - Ivory: 2
          - Paper: 12
          - Pearls: 1
          - Maize: 5
          - Rice: 4
          - Aluminum: 49
          - Fish: 26
          - Deer: 5
          - Whales: 1
          - Sugar: 4
          - Jade: 4
          - Iron: 17
          - Dyes: 1
          - Tea: 1
          - Coal: 14
          - Cattle: 6
          - Horses: 8
          - Coral: 4
          - Bison: 7
          - Copper: 4
          - Truffles: 4
          - Incense: 2
          - Stone: 6
          - Marble: 2
          - Cinnamon: 2
          - Bananas: 5
          - Oil: 14
          - Wine: 1
          - Tobacco: 2
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Siam:
            - Distance: Neighbors
            - Denounced Them
          - Korea:
            - Distance: Far
          - The Zulus:
            - Distance: Close
            - Denounced Them
          - Songhai:
            - Distance: Neighbors
            - War (Our Score: -54%; Our War Weariness: 41%)
        - Votes: 10
        - 2: Defeated Major Civilization Assyria
        
        ## Player 3
        - Civilization: The Zulus
        - Leader: Shaka
        - IsMajor: true
        - OurOpinionToThem:
          - You have both chosen to adopt the Order Ideology. (999)
          - You have denounced one of their declared enemies! (11)
          - We have similar Social Policies. (3)
          - Our real approach is War.
          - They are spreading their own religion, but you converted some of their cities to your religion. (-6)
          - Religious differences strain your relationship. (-30)
          - Your spies were caught stealing from them. (-33)
          - They fear your warmongering will end this world in fire! (-50)
          - Our leader has expressed a public opinion to this player (-60).
          - Our leader has formed a private opinion to this player (-60).
          - You are at war! (-99999)
        - TheirOpinionToUs:
          - You have both chosen to adopt the Order Ideology.
          - You have no contested borders.
          - Your votes supported their civ's interests in the World Congress.
          - You have denounced one of their declared enemies!
          - We fought together against a common foe.
          - We have similar Social Policies.
          - They fear your warmongering will end this world in fire! (They ignore most warmongering.)
          - Religious differences strain your relationship.
          - They believe we are building World Wonders too aggressively!
          - We placed sanctions on them in the World Congress.
          - They disliked our proposal to the World Congress.
          - We defeated their proposal in the World Congress.
          - We have denounced each other!
          - The leader has expressed a public opinion to you (-100).
          - You are at war!
        - Score: 5882
        - Era: Information
        - Technologies: 68
        - Cities: 25
        - Population: 601
        - Territory: 779
        - Gold: 127
        - GoldPerTurn: -619
        - HappinessSituation: Happy
        - HappinessPercentage: 58
        - MilitaryStrength: 134373
        - TourismPerTurn: 1648.5
        - CulturePerTurn: 2913
        - PolicyBranches:
          - Fealty: 1
          - Order: 7
          - Artistry: 1
          - Progress: 4
          - Rationalism: 1
          - Imperialism: 6
          - Authority: 6
        - ResourcesAvailable:
          - Wheat: 6
          - Sheep: 15
          - Ivory: 2
          - Gold: 4
          - Paper: 8
          - Pearls: 1
          - Maize: 7
          - Rice: 2
          - Cotton: 8
          - Salt: 7
          - Aluminum: 25
          - Fish: 22
          - Amber: 8
          - Perfume: 7
          - Deer: 6
          - Whales: 1
          - Olives: 1
          - Iron: 12
          - Dyes: 1
          - Tea: 1
          - Coal: 18
          - Cattle: 14
          - Horses: -2
          - Coral: 4
          - Bison: 2
          - Incense: 2
          - Stone: 7
          - Marble: 1
          - Furs: 1
          - Cinnamon: 4
          - Bananas: 6
          - Oil: -5
          - Cocoa: 4
          - Tobacco: 3
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Siam:
            - Distance: Far
            - War (Our Score: 2%; Our War Weariness: 0%)
          - Korea:
            - Distance: Neighbors
            - Our Vassal (Capitulated)
            - Open Borders
          - Japan:
            - Distance: Close
            - Denounced Them
          - Songhai:
            - Distance: Close
            - War (Our Score: 6%; Our War Weariness: 12%)
            - Denounced Them
        - Votes: 14
        
        ## Player 4
        - Civilization: Songhai
        - Leader: Askia
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: None, Our top defensive pact ally: None
          - Our top World Congress ally: None, Our top World Congress rival: Siam
          - Our top Competitor: The Zulus
        - Score: 4152
        - Era: Information
        - GoldenAge: Estimated in 13 turns
        - Technologies: 67
        - CurrentResearch: Advanced Ballistics (Estimated in 2 turns)
        - NextPolicyTurns: 8
        - Cities: 19
        - Population: 595
        - Territory: 687
        - BestSettlementLocation:
          - 36, 16 (Quality: 40%; 5 tiles from us)
          - 35, 17 (Quality: 28%; 5 tiles from us)
          - 36, 18 (Quality: 0%; 4 tiles from us)
          - 29, 43 (Quality: 0%; 4 tiles from us)
          - 29, 44 (Quality: 0%; 4 tiles from us)
        - Gold: 914
        - GoldPerTurn: 8
        - HappinessSituation: Happy
        - HappinessPercentage: 56
        - MilitaryUnits: 65
        - MilitarySupply: 123
        - MilitaryStrength: 9649
        - TourismPerTurn: 1362
        - CulturePerTurn: 2246
        - FaithPerTurn: 618
        - SciencePerTurn: 3107
        - PolicyBranches:
          - Tradition:
            - Tradition
            - Justice
            - Ceremony
          - Rationalism:
            - Rationalism
          - Progress:
            - Progress
            - Organization
          - Authority:
            - Authority
            - Tribute
            - Imperium
            - Militarism
            - Dominance
          - Fealty:
            - Fealty
          - Industry:
            - Industry
          - Artistry:
            - Artistry
          - Statecraft:
            - Statecraft
          - Order:
            - Patriotic War
            - Great Leap Forward
            - Academy of Sciences
            - Workers' Faculties
            - Iron Curtain
            - Peace, Land, Bread
          - Imperialism:
            - Imperialism
            - Exploitation
            - Regimental System
            - Civilizing Mission
        - ResourcesAvailable:
          - Wheat: 5
          - Silver: 2
          - Sheep: 8
          - Cloves: 0
          - Figs: 0
          - Ivory: 2
          - Gold: 0
          - Nutmeg: 0
          - Paper: 6
          - Pearls: 2
          - Maize: 3
          - Rice: 4
          - Cotton: 0
          - Gems: 0
          - Salt: 0
          - Brazilwood: 5
          - Aluminum: 40
          - Glass: 1
          - Lapis Lazuli: 9
          - Fish: 19
          - Amber: 0
          - Perfume: 0
          - Deer: 12
          - Whales: 1
          - Olives: 4
          - Sugar: 0
          - Jade: 4
          - Iron: 14
          - Dyes: 2
          - Tea: 0
          - Coal: -3
          - Coffee: 0
          - Cattle: 5
          - Pepper: 0
          - Uranium: 7
          - Horses: 0
          - Coral: 0
          - Silk: 2
          - Jewelry: 2
          - Bison: 5
          - Antiquity Site: 0
          - Citrus: 0
          - Copper: 6
          - Truffles: 0
          - Crab: 0
          - Incense: 2
          - Stone: 10
          - Marble: 3
          - Furs: 2
          - Cinnamon: 0
          - Bananas: 1
          - Oil: 1
          - Wine: 8
          - Porcelain: 1
          - Cocoa: 0
          - Tobacco: 2
        - FoundedReligion: Islam
        - Relationships:
          - Siam:
            - Distance: Far
            - War (Our Score: 2%; Our War Weariness: 12%)
          - Korea:
            - Distance: Close
            - War (Our Score: 6%; Our War Weariness: 12%)
            - Denounced Them
          - Japan:
            - Distance: Neighbors
            - War (Our Score: 54%; Our War Weariness: 49%)
            - Denounced Them
          - The Zulus:
            - Distance: Close
            - War (Our Score: -6%; Our War Weariness: 18%)
            - Denounced Them
        - OutgoingTradeRoutes:
          - Tondibi (Songhai) => Tilburg (Songhai):
            - TurnsLeft: 12
            - Domain: Sea
            - ToProduction: 94.25
          - Gao (Songhai) => Vilnius (Songhai):
            - ToFood: 123
            - TurnsLeft: 8
            - Domain: Land
          - Gao (Songhai) => Shimonoseki (Songhai):
            - ToFood: 123
            - TurnsLeft: 22
            - Domain: Land
          - Kukia (Songhai) => Palatium (City-State Palatium):
            - TurnsLeft: 14
            - FromScience: 7
            - Domain: Land
            - FromGold: 56.44
            - FromCulture: 7
          - Gao (Songhai) => Tokyo (Songhai):
            - TurnsLeft: 1
            - Domain: Land
            - ToProduction: 102
          - Kukia (Songhai) => Lutetia (City-State Lutetia):
            - TurnsLeft: 12
            - FromScience: 7
            - Domain: Land
            - FromGold: 55.14
            - FromCulture: 7
          - Tombouctu (Songhai) => Tokyo (Songhai):
            - TurnsLeft: 1
            - Domain: Land
            - ToProduction: 81
          - Gao (Songhai) => Taghaza (Songhai):
            - ToFood: 114.6
            - TurnsLeft: 12
            - Domain: Land
          - Gao (Songhai) => Tombouctu (Songhai):
            - ToFood: 114.6
            - TurnsLeft: 8
            - Domain: Land
          - Gao (Songhai) => Kukia (Songhai):
            - ToFood: 118.8
            - TurnsLeft: 20
            - Domain: Land
          - Gao (Songhai) => Jenne (Songhai):
            - TurnsLeft: 21
            - Domain: Land
            - ToProduction: 87
          - Kukia (Songhai) => Tokyo (Songhai):
            - TurnsLeft: 27
            - Domain: Land
            - ToProduction: 84
          - Jenne (Songhai) => Tokyo (Songhai):
            - TurnsLeft: 4
            - Domain: Land
            - ToProduction: 81
        - Spies:
          - Agent Laila (5):
            - State: Counter-intelligence
            - Role: Counterspy
            - Location: Gao (Songhai)
            - NetworkPerTurn: 0
          - Agent Guedado (3):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 17
            - Location: Ulundi (The Zulus)
            - NetworkPerTurn: 17
          - Agent Ime (2):
            - State: Traveling
            - Role: Spy
            - Location: Martaban (Siam)
            - NetworkPerTurn: 0
          - Agent Kayode (9):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 1026
            - Location: Nagasaki (Japan)
            - NetworkPerTurn: 45
          - Agent Adhiambo (7):
            - State: Unassigned
            - Role: Vassal Diplomat
            - Location: Unassigned
            - NetworkPerTurn: 0
          - Agent Eniola (0):
            - State: Counter-intelligence
            - Role: Counterspy
            - Location: Kyoto (Songhai)
            - NetworkPerTurn: 0
          - Agent Folami (8):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 1157
            - Location: Hakodate (Japan)
            - NetworkPerTurn: 48
          - Agent Mariama (6):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 658
            - Location: Izumo (Japan)
            - NetworkPerTurn: 31
          - Agent Olabode (4):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 1062
            - Location: Sapporo (Japan)
            - NetworkPerTurn: 50
        - Votes: 20
        
        ## Player 5
        - Civilization: Siam
        - Leader: Ramkhamhaeng
        - IsMajor: true
        - OurOpinionToThem:
          - You have both chosen to adopt the Order Ideology. (999)
          - We passed their proposal in the World Congress. (36)
          - You have denounced one of their declared enemies! (11)
          - We have similar Social Policies. (3)
          - Our real approach is Friendly.
          - Our leader has expressed a public opinion to this player (-10).
          - Our leader has formed a private opinion to this player (-10).
          - Your spies were caught stealing from them. (-33)
          - You are at war! (-99999)
        - TheirOpinionToUs:
          - You have both chosen to adopt the Order Ideology.
          - We fought together against a common foe.
          - You are not competing for technological advancement.
          - We passed their proposal in the World Congress.
          - You have denounced one of their declared enemies!
          - We have similar Social Policies.
          - You have no contested borders.
          - They fear your warmongering will end this world in fire! (They strongly dislike warmongers.)
          - You are competing for World Wonders.
          - The leader has expressed a public opinion to you (-15).
          - They disliked our proposal to the World Congress.
          - Your votes opposed their civ's interests in the World Congress.
          - You are at war!
        - Score: 1207
        - Era: Atomic
        - Technologies: 60
        - Cities: 2
        - Population: 44
        - Territory: 78
        - Gold: 423
        - GoldPerTurn: 0
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 714
        - TourismPerTurn: 79.75
        - CulturePerTurn: 426
        - PolicyBranches:
          - Order: 1
          - Tradition: 2
          - Artistry: 3
          - Statecraft: 6
          - Rationalism: 3
          - Industry: 2
          - Progress: 4
        - ResourcesAvailable:
          - Paper: 7
          - Rice: 1
          - Aluminum: 1
          - Maize: 1
          - Cinnamon: 2
          - Coal: 5
          - Tea: 4
          - Marble: 2
          - Horses: 3
          - Fish: 1
          - Bison: 1
          - Bananas: 2
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Zulus:
            - Distance: Far
            - War (Our Score: -2%; Our War Weariness: 0%)
          - Korea:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 0%)
          - Japan:
            - Distance: Neighbors
            - Denounced Them
          - Songhai:
            - Distance: Far
            - War (Our Score: -2%; Our War Weariness: 0%)
        - Votes: 17
        - 6: Defeated Major Civilization Brazil
        - 7: Defeated Major Civilization The Netherlands
        - 22: Defeated Minor Civilization Geneva
        - 23: Defeated Minor Civilization Sofia
        - 24: Defeated Minor Civilization Ife
        - 25: Defeated Minor Civilization Huari
        
        ## Player 26
        - Civilization: Dublin
        - Leader: City State
        - MajorAlly: Songhai
        - Population: 19
        - Relationships:
          - Siam: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - The Zulus: War - Peace Currently Blocked (Influence: -60, Distance: Neighbors)
          - Songhai: Ally (Influence: 108, Distance: Neighbors, Protected)
          - Korea: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Japan: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
        - Quests:
          -  Acquire the city of Huari. (Turns remaining: 50) Potential Quest Reward: * 448 Influence * 1 Juggernaut Unit(140 Bonus XP)
        - 27: Defeated Minor Civilization Valletta
        - 28: Defeated Minor Civilization Vilnius
        
        ## Player 29
        - Civilization: Palatium
        - Leader: City State
        - MajorAlly: Songhai
        - Population: 21
        - ResourcesAvailable:
          - Deer: 2
          - Fish: 1
        - MajorityReligion: Islam
        - Relationships:
          - Siam: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - The Zulus: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Songhai: Ally (Influence: 383, Distance: Neighbors, Protected)
          - Korea: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Japan: War - Peace Currently Blocked (Influence: -60, Distance: Close)
        - Quests:
          -  They will reward the player with the highest Tourism per turn. So far, you have the lead with 1,362 per turn. (Turns remaining: 8) Potential Quest Reward: * 311 Influence * 386 Culture
          - Conduct a Spy Mission against Shaka. Potential Quest Reward: * 363 Influence * 878 Science
        
        ## Player 30
        - Civilization: Ecbatana
        - Leader: City State
        - MajorAlly: Siam
        - Population: 19
        - ResourcesAvailable:
          - Fish: 1
        - Relationships:
          - Siam: Ally (Influence: 278, Distance: Close)
          - The Zulus: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Songhai: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Korea: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Japan: Friends (Influence: 46, Distance: Neighbors, Protected)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        - 31: Defeated Minor Civilization Wittenberg
        
        ## Player 32
        - Civilization: Antananarivo
        - Leader: City State
        - MajorAlly: Songhai
        - Population: 40
        - ResourcesAvailable:
          - Stone: 1
          - Maize: 2
          - Fish: 4
        - Relationships:
          - Siam: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - The Zulus: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Songhai: Ally (Influence: 123, Distance: Distant, Protected)
          - Korea: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Japan: War - Peace Currently Blocked (Influence: -60, Distance: Neighbors)
        - Quests:
          -  They want you to liberate the city of Ife. (Turns remaining: 50) Potential Quest Reward: * 235 Influence * 4 Happiness in Capital
        
        ## Player 33
        - Civilization: Luba
        - Leader: City State
        - MajorAlly: Siam
        - Population: 23
        - ResourcesAvailable:
          - Fish: 2
        - MajorityReligion: Islam
        - Relationships:
          - Siam: Ally (Influence: 225, Distance: Neighbors)
          - The Zulus: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Songhai: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Korea: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Japan: Neutral (Influence: 18, Distance: Neighbors)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 34
        - Civilization: Lutetia
        - Leader: City State
        - MajorAlly: Songhai
        - Population: 9
        - ResourcesAvailable:
          - Deer: 1
          - Bison: 1
        - MajorityReligion: Islam
        - Relationships:
          - Siam: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - The Zulus: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Songhai: Ally (Influence: 401, Distance: Neighbors, Protected)
          - Korea: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Japan: War - Peace Currently Blocked (Influence: -60, Distance: Far)
        - Quests:
          -  They want you to build the Foreign Bureau. (Turns remaining: 32) Potential Quest Reward: * 200 Influence * 743 Golden Age Points
        - 35: Defeated Minor Civilization Aztlan
        
        ## Player 36
        - Civilization: Jakarta
        - Leader: City State
        - MajorAlly: Siam
        - Population: 23
        - ResourcesAvailable:
          - Fish: 3
          - Sheep: 1
        - MajorityReligion: Islam
        - Relationships:
          - Siam: Ally (Influence: 60, Distance: Neighbors)
          - The Zulus: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Songhai: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Korea: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Japan: Neutral (Influence: -34, Distance: Neighbors)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 37
        - Civilization: Harappa
        - Leader: City State
        - MajorAlly: Songhai
        - Population: 14
        - ResourcesAvailable:
          - Wheat: 1
        - MajorityReligion: Islam
        - Relationships:
          - Siam: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - The Zulus: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Songhai: Ally (Influence: 285, Distance: Neighbors, Protected)
          - Korea: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Japan: War - Peace Currently Blocked (Influence: -60, Distance: Neighbors)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        - 63: Barbarians
        
        # Cities
        Cities: summary reports about discovered cities in the world.
        
        ## Player: Korea
        
        ### Seoul
        - ID: 1057
        - X: 22
        - Y: 29
        - Population: 34
        - DefenseStrength: 73
        - IsCoastal: true
        - Wonders:
          - Circus Maximus
          - Imperial College
          - Great Lighthouse
          - Colossus
          - Grand Temple
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
          - Nalanda
          - Karlstejn
          - Apostolic Palace
        
        ### Jeonju
        - ID: 1484
        - X: 17
        - Y: 31
        - Population: 24
        - MajorityReligion: Buddhism
        - DefenseStrength: 69
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Ironworks
          - Neuschwanstein
          - Uffizi
          - Palace of Culture and Science
          - Civilized Jewelers Headquarters
        
        ### Daegu
        - ID: 2830
        - X: 20
        - Y: 34
        - Population: 24
        - DefenseStrength: 72
        - IsCoastal: true
        - Wonders:
          - Chartered Company
          - Royal Collection
          - Louvre
        
        ### Groningen
        - ID: 11319
        - X: 16
        - Y: 35
        - Population: 22
        - MajorityReligion: Buddhism
        - DefenseStrength: 68
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: Japan
        
        ### Osaka
        - ID: 1361
        - X: 48
        - Y: 36
        - Population: 25
        - MajorityReligion: Islam
        - DefenseStrength: 82
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - National Monument
          - Circus Maximus
          - Chartered Company
          - Scrivener's Office
          - Printing Press
        
        ### Satsuma
        - ID: 2261
        - X: 54
        - Y: 36
        - Population: 29
        - MajorityReligion: Islam
        - DefenseStrength: 49
        - IsCoastal: true
        - Wonders:
          - Imperial College
        
        ### Kagoshima
        - ID: 2913
        - X: 55
        - Y: 41
        - Population: 31
        - MajorityReligion: Islam
        - DefenseStrength: 78
        - IsCoastal: true
        - Wonders:
          - Alhambra
        
        ### Nara
        - ID: 3202
        - X: 53
        - Y: 30
        - Population: 26
        - MajorityReligion: Islam
        - DefenseStrength: 88
        - IsCoastal: true
        
        ### Nagoya
        - ID: 3411
        - X: 48
        - Y: 25
        - Population: 27
        - MajorityReligion: Islam
        - DefenseStrength: 78
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - Royal Collection
          - Prora
          - Firaxite Materials Headquarters
        
        ### Izumo
        - ID: 3641
        - X: 44
        - Y: 26
        - Population: 27
        - MajorityReligion: Islam
        - DefenseStrength: 78
        - Health: 96%
        - Wonders:
          - Ironworks
        
        ### Nagasaki
        - ID: 3937
        - X: 48
        - Y: 20
        - Population: 27
        - MajorityReligion: Islam
        - DefenseStrength: 88
        - IsCoastal: true
        - Wonders:
          - Hall of Honor
        
        ### Valletta
        - ID: 5190
        - X: 48
        - Y: 31
        - Population: 30
        - MajorityReligion: Islam
        - DefenseStrength: 78
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Grand Temple
        
        ### Yokohama
        - ID: 6483
        - X: 45
        - Y: 15
        - Population: 20
        - MajorityReligion: Buddhism
        - DefenseStrength: 83
        - IsCoastal: true
        
        ### Matsuyama
        - ID: 11608
        - X: 45
        - Y: 10
        - Population: 18
        - MajorityReligion: Islam
        - DefenseStrength: 78
        - IsCoastal: true
        
        ### Sapporo
        - ID: 12516
        - X: 49
        - Y: 14
        - Population: 18
        - MajorityReligion: Islam
        - DefenseStrength: 80
        - IsCoastal: true
        
        ### Hakodate
        - ID: 13125
        - X: 55
        - Y: 3
        - Population: 17
        - MajorityReligion: Islam
        - DefenseStrength: 80
        - IsCoastal: true
        
        ### Ise
        - ID: 13938
        - X: 58
        - Y: 37
        - Population: 17
        - MajorityReligion: Islam
        - DefenseStrength: 86
        - IsCoastal: true
        
        ### Eindhoven
        - ID: 13939
        - X: 65
        - Y: 41
        - Population: 18
        - MajorityReligion: Islam
        - DefenseStrength: 82
        - IsOccupied: true
        - IsCoastal: true
        
        ### Maastricht
        - ID: 14253
        - X: 65
        - Y: 31
        - Population: 13
        - DefenseStrength: 77
        - IsOccupied: true
        - IsCoastal: true
        
        ### Zutphen
        - ID: 14631
        - X: 70
        - Y: 32
        - Population: 16
        - DefenseStrength: 77
        - IsOccupied: true
        - IsCoastal: true
        
        ### Chainat
        - ID: 17366
        - X: 60
        - Y: 19
        - Population: 13
        - MajorityReligion: Islam
        - DefenseStrength: 79
        - IsPuppet: true
        - IsCoastal: true
        
        ### Nakhon Si Thammarat
        - ID: 17546
        - X: 67
        - Y: 24
        - Population: 19
        - DefenseStrength: 75
        - IsOccupied: true
        - IsCoastal: true
        
        ### Arnhem
        - ID: 18655
        - X: 76
        - Y: 27
        - Population: 19
        - DefenseStrength: 79
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: The Zulus
        
        ### Ulundi
        - ID: 1060
        - X: 19
        - Y: 20
        - Population: 34
        - MajorityReligion: Buddhism
        - DefenseStrength: 91
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - Menin Gate
        
        ### Umgungundlovu
        - ID: 1302
        - X: 22
        - Y: 23
        - Population: 35
        - MajorityReligion: Buddhism
        - DefenseStrength: 48
        - Wonders:
          - Soho Foundry
        
        ### Nobamba
        - ID: 1583
        - X: 16
        - Y: 22
        - Population: 34
        - MajorityReligion: Buddhism
        - DefenseStrength: 54
        - Wonders:
          - Imperial College
          - Sistine Chapel
        
        ### Bulawayo
        - ID: 1811
        - X: 25
        - Y: 18
        - Population: 30
        - MajorityReligion: Buddhism
        - DefenseStrength: 121
        - IsCoastal: true
        - Wonders:
          - National Monument
          - Circus Maximus
          - Royal Collection
          - Grand Temple
          - Scrivener's Office
          - Printing Press
        
        ### Nineveh
        - ID: 3987
        - X: 15
        - Y: 16
        - Population: 27
        - MajorityReligion: Buddhism
        - DefenseStrength: 52
        - IsOccupied: true
        - Wonders:
          - Ironworks
          - Kremlin
          - Palace of Culture and Science
        
        ### Assur
        - ID: 4662
        - X: 15
        - Y: 11
        - Population: 30
        - MajorityReligion: Buddhism
        - DefenseStrength: 107
        - IsOccupied: true
        - Wonders:
          - Chartered Company
          - Pentagon
          - Foreign Bureau
          - Hexxon Refineries Headquarters
        
        ### Nimrud
        - ID: 5731
        - X: 17
        - Y: 7
        - Population: 23
        - MajorityReligion: Buddhism
        - DefenseStrength: 56
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Summer Palace
        
        ### Busan
        - ID: 7969
        - X: 19
        - Y: 26
        - Population: 25
        - MajorityReligion: Buddhism
        - DefenseStrength: 113
        - IsOccupied: true
        
        ### Rotterdam
        - ID: 10342
        - X: 14
        - Y: 26
        - Population: 27
        - MajorityReligion: Buddhism
        - DefenseStrength: 109
        - IsOccupied: true
        - Wonders:
          - Forbidden Palace
          - Cristo Redentor
        
        ### Ife
        - ID: 11019
        - X: 10
        - Y: 21
        - Population: 23
        - MajorityReligion: Buddhism
        - DefenseStrength: 112
        - IsOccupied: true
        
        ### Utrecht
        - ID: 11144
        - X: 9
        - Y: 26
        - Population: 25
        - MajorityReligion: Buddhism
        - DefenseStrength: 105
        - IsOccupied: true
        - IsCoastal: true
        
        ### Amsterdam
        - ID: 11384
        - X: 12
        - Y: 31
        - Population: 31
        - MajorityReligion: Buddhism
        - DefenseStrength: 110
        - IsOccupied: true
        - Wonders:
          - Chichen Itza
          - Borobudur
        
        ### Nijmegen
        - ID: 11717
        - X: 6
        - Y: 24
        - Population: 23
        - MajorityReligion: Buddhism
        - DefenseStrength: 73
        - IsOccupied: true
        - IsCoastal: true
        
        ### Nakhon Chum
        - ID: 13847
        - X: 20
        - Y: 9
        - Population: 24
        - MajorityReligion: Buddhism
        - DefenseStrength: 105
        - IsOccupied: true
        - IsCoastal: true
        
        ### Muang Saluang
        - ID: 14468
        - X: 12
        - Y: 13
        - Population: 21
        - MajorityReligion: Buddhism
        - DefenseStrength: 106
        - IsOccupied: true
        
        ### Kamphaeng Phet
        - ID: 14559
        - X: 14
        - Y: 5
        - Population: 20
        - MajorityReligion: Buddhism
        - DefenseStrength: 66
        - IsOccupied: true
        - IsCoastal: true
        
        ### Si Satchanalai
        - ID: 15032
        - X: 8
        - Y: 15
        - Population: 23
        - MajorityReligion: Buddhism
        - DefenseStrength: 105
        - IsOccupied: true
        
        ### Aztlan
        - ID: 15197
        - X: 11
        - Y: 6
        - Population: 20
        - MajorityReligion: Buddhism
        - DefenseStrength: 110
        - IsOccupied: true
        
        ### Sukhothai
        - ID: 15837
        - X: 5
        - Y: 9
        - Population: 29
        - MajorityReligion: Buddhism
        - DefenseStrength: 109
        - IsOccupied: true
        - Wonders:
          - Stonehenge
          - Great Library
          - Porcelain Tower
          - Taj Mahal
          - Statue of Liberty
          - Statue of Zeus
          - Globe Theatre
          - Holy Council
        
        ### Lampang
        - ID: 15845
        - X: 3
        - Y: 16
        - Population: 21
        - MajorityReligion: Buddhism
        - DefenseStrength: 110
        - IsOccupied: true
        - IsCoastal: true
        
        ### Phitsanulok
        - ID: 16258
        - X: 4
        - Y: 4
        - Population: 17
        - MajorityReligion: Buddhism
        - DefenseStrength: 112
        - IsOccupied: true
        - IsCoastal: true
        
        ### Geneva
        - ID: 16841
        - X: 6
        - Y: 20
        - Population: 15
        - MajorityReligion: Buddhism
        - DefenseStrength: 67
        - IsOccupied: true
        - IsCoastal: true
        
        ### Huari
        - ID: 17235
        - X: 13
        - Y: 39
        - Population: 16
        - MajorityReligion: Buddhism
        - DefenseStrength: 110
        - IsOccupied: true
        - IsCoastal: true
        
        ### Kwadukuza
        - ID: 17503
        - X: 9
        - Y: 37
        - Population: 16
        - MajorityReligion: Buddhism
        - DefenseStrength: 53
        - IsCoastal: true
        
        ### Sofia
        - ID: 19350
        - X: 23
        - Y: 13
        - Population: 12
        - MajorityReligion: Buddhism
        - DefenseStrength: 82
        - Health: 59%
        - IsOccupied: true
        - IsCoastal: true
        - ResistanceTurns: 3
        
        ## Player: Songhai
        
        ### Gao
        - ID: 1061
        - X: 34
        - Y: 38
        - Population: 52
        - MajorityReligion: Islam
        - DefenseStrength: 86
        - FoodStored: 4923
        - FoodPerTurn: 255
        - ProductionStored: 0
        - ProductionPerTurn: 692
        - CurrentProduction: Strategic Defense System
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 302
        - SciencePerTurn: 261
        - CulturePerTurn: 302
        - FaithPerTurn: 119
        - TourismPerTurn: 179.25
        - HappinessDelta: 19
        - BuildingCount: 50
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Shrine
          - Constabulary
          - Writers' Guild
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Airport
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Refinery
          - Gumey
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Pyramids
          - Hanging Gardens
          - Angkor Wat
          - Hagia Sophia
          - Brandenburg Gate
          - Eiffel Tower
          - Temple of Artemis
          - Leaning Tower of Pisa
          - Petra
          - Printing Press
          - Foreign Bureau
          - Palace of Culture and Science
          - Roman Forum
          - Empire State Building
          - Royal Guardhouse
          - Royal Astrologer
          - Great Altar
        - GreatWorkCount: 6
        
        ### Tombouctu
        - ID: 1276
        - X: 39
        - Y: 38
        - Population: 35
        - MajorityReligion: Islam
        - DefenseStrength: 125
        - FoodStored: 2093
        - FoodPerTurn: 267
        - ProductionStored: 980
        - ProductionPerTurn: 630
        - CurrentProduction: Heavy Bomber
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 160
        - SciencePerTurn: 136
        - CulturePerTurn: 160
        - FaithPerTurn: 36
        - TourismPerTurn: 144
        - HappinessDelta: 9
        - BuildingCount: 53
        - ImportantBuildings:
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Constabulary
          - Artists' Guild
          - Hotel
          - Airport
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Refinery
          - Gumey
        - Wonders:
          - Ironworks
          - Machu Picchu
        - GreatWorkCount: 6
        
        ### Jenne
        - ID: 1543
        - X: 39
        - Y: 43
        - Population: 37
        - MajorityReligion: Islam
        - DefenseStrength: 85
        - FoodStored: 2649
        - FoodPerTurn: 61
        - ProductionPerTurn: 519
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 244
        - SciencePerTurn: 265
        - CulturePerTurn: 187
        - FaithPerTurn: 41
        - TourismPerTurn: 159.25
        - BuildingCount: 53
        - ImportantBuildings:
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Constabulary
          - Musicians' Guild
          - Hotel
          - Airport
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Refinery
          - Gumey
        - Wonders:
          - Mausoleum of Halicarnassus
        - GreatWorkCount: 6
        
        ### Taghaza
        - ID: 1867
        - X: 30
        - Y: 34
        - Population: 36
        - MajorityReligion: Islam
        - DefenseStrength: 125
        - IsCoastal: true
        - FoodStored: 3035
        - FoodPerTurn: 278
        - ProductionStored: 630
        - ProductionPerTurn: 531
        - CurrentProduction: Fleet Destroyer
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 168
        - SciencePerTurn: 144
        - CulturePerTurn: 164
        - FaithPerTurn: 35
        - TourismPerTurn: 144.25
        - HappinessDelta: 3
        - BuildingCount: 55
        - ImportantBuildings:
          - Seaport
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Shrine
          - Strategic Defense System
          - Constabulary
          - Hotel
          - Airport
          - Bath
          - Coaling Station
          - Wire Service
          - Mine Field
          - Gumey
        - Wonders:
          - Circus Maximus
          - Great Wall
          - Notre Dame
          - Scrivener's Office
        - GreatWorkCount: 7
        
        ### Tondibi
        - ID: 2157
        - X: 31
        - Y: 29
        - Population: 40
        - MajorityReligion: Islam
        - DefenseStrength: 123
        - IsCoastal: true
        - FoodStored: 2800
        - FoodPerTurn: 120
        - ProductionStored: 885
        - ProductionPerTurn: 564
        - CurrentProduction: Heavy Bomber
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 149
        - SciencePerTurn: 184
        - CulturePerTurn: 151
        - FaithPerTurn: 32
        - TourismPerTurn: 113.25
        - HappinessDelta: 2
        - BuildingCount: 59
        - ImportantBuildings:
          - Seaport
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Shrine
          - Strategic Defense System
          - Constabulary
          - Artists' Guild
          - Hotel
          - Airport
          - Bath
          - Coaling Station
          - Wire Service
          - Mine Field
          - Gumey
        - GreatWorkCount: 4
        
        ### Kumbi Saleh
        - ID: 2568
        - X: 27
        - Y: 39
        - Population: 35
        - MajorityReligion: Islam
        - DefenseStrength: 123
        - IsCoastal: true
        - FoodStored: 2217
        - FoodPerTurn: 95
        - ProductionStored: 0
        - ProductionPerTurn: 446
        - CurrentProduction: Atomic Bomb
        - ProductionTurnsLeft: 6
        - GoldPerTurn: 175
        - SciencePerTurn: 155
        - CulturePerTurn: 170
        - FaithPerTurn: 32
        - TourismPerTurn: 147.5
        - HappinessDelta: 3
        - BuildingCount: 60
        - ImportantBuildings:
          - Seaport
          - Stable
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Constabulary
          - Hotel
          - Airport
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Mine Field
          - Gumey
        - Wonders:
          - Royal Collection
          - Grand Temple
        - GreatWorkCount: 7
        
        ### Kukia
        - ID: 2951
        - X: 39
        - Y: 32
        - Population: 34
        - MajorityReligion: Islam
        - DefenseStrength: 117
        - FoodStored: 2648
        - FoodPerTurn: 207
        - ProductionStored: 0
        - ProductionPerTurn: 489
        - CurrentProduction: Strategic Defense System
        - ProductionTurnsLeft: 3
        - GoldPerTurn: 307
        - SciencePerTurn: 165
        - CulturePerTurn: 118
        - FaithPerTurn: 34
        - TourismPerTurn: 75.5
        - HappinessDelta: 0
        - BuildingCount: 51
        - ImportantBuildings:
          - Stable
          - Windmill
          - Customs House
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
          - Hotel
          - Airport
          - Coaling Station
          - Wire Service
          - Gumey
        - Wonders:
          - Chartered Company
          - Himeji Castle
          - TwoKay Foods Headquarters
        - GreatWorkCount: 4
        
        ### Walata
        - ID: 4728
        - X: 35
        - Y: 22
        - Population: 35
        - MajorityReligion: Islam
        - DefenseStrength: 99
        - IsCoastal: true
        - FoodStored: 2364
        - FoodPerTurn: 165
        - ProductionStored: 358
        - ProductionPerTurn: 373
        - CurrentProduction: Strategic Defense System
        - ProductionTurnsLeft: 4
        - GoldPerTurn: 176
        - SciencePerTurn: 172
        - CulturePerTurn: 114
        - FaithPerTurn: 22
        - TourismPerTurn: 46.75
        - HappinessDelta: 8
        - BuildingCount: 58
        - ImportantBuildings:
          - Seaport
          - Stable
          - Windmill
          - Customs House
          - Garden
          - Stadium
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
          - Writers' Guild
          - Hotel
          - Airport
          - Coaling Station
          - Wire Service
          - Mine Field
          - Gumey
        - GreatWorkCount: 0
        
        ### Sao Paulo
        - ID: 5558
        - X: 38
        - Y: 27
        - Population: 35
        - MajorityReligion: Islam
        - DefenseStrength: 123
        - IsOccupied: true
        - FoodStored: 1831
        - FoodPerTurn: 78
        - ProductionStored: 0
        - ProductionPerTurn: 526
        - CurrentProduction: Atomic Bomb
        - ProductionTurnsLeft: 5
        - GoldPerTurn: 183
        - SciencePerTurn: 155
        - CulturePerTurn: 155
        - FaithPerTurn: 28
        - TourismPerTurn: 96.25
        - HappinessDelta: 7
        - BuildingCount: 58
        - ImportantBuildings:
          - Courthouse
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Constabulary
          - Writers' Guild
          - Hotel
          - Airport
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Refinery
          - Gumey
        - Wonders:
          - Imperial College
        - GreatWorkCount: 2
        
        ### Vilnius
        - ID: 7795
        - X: 29
        - Y: 48
        - Population: 29
        - MajorityReligion: Islam
        - DefenseStrength: 85
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 1809
        - FoodPerTurn: 106
        - ProductionStored: 407
        - ProductionPerTurn: 246
        - CurrentProduction: Atomic Bomb
        - ProductionTurnsLeft: 9
        - GoldPerTurn: 173
        - SciencePerTurn: 134
        - CulturePerTurn: 97
        - FaithPerTurn: 26
        - TourismPerTurn: 33.5
        - HappinessDelta: -5
        - BuildingCount: 59
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Constabulary
          - Musicians' Guild
          - Hotel
          - Airport
          - Coaling Station
          - Wire Service
          - Mine Field
          - Refinery
          - Gumey
        - GreatWorkCount: 0
        
        ### Shimonoseki
        - ID: 9242
        - X: 40
        - Y: 16
        - Population: 29
        - MajorityReligion: Islam
        - DefenseStrength: 128
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 1382
        - FoodPerTurn: 97
        - ProductionStored: 0
        - ProductionPerTurn: 352
        - CurrentProduction: Heavy Bomber
        - ProductionTurnsLeft: 3
        - GoldPerTurn: 183
        - SciencePerTurn: 160
        - CulturePerTurn: 79
        - FaithPerTurn: 32
        - TourismPerTurn: 31.75
        - HappinessDelta: -5
        - BuildingCount: 61
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Stable
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Constabulary
          - Hotel
          - Airport
          - Coaling Station
          - Wire Service
          - Mine Field
          - Gumey
        - GreatWorkCount: 0
        
        ### Tilburg
        - ID: 11571
        - X: 50
        - Y: 7
        - Population: 23
        - MajorityReligion: Islam
        - DefenseStrength: 125
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 998
        - FoodPerTurn: 139
        - ProductionStored: 1063
        - ProductionPerTurn: 359
        - CurrentProduction: Fleet Destroyer
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 77
        - SciencePerTurn: 94
        - CulturePerTurn: 52
        - FaithPerTurn: 28
        - TourismPerTurn: 16.75
        - HappinessDelta: 3
        - BuildingCount: 48
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Windmill
          - Customs House
          - Garden
          - Zoo
          - Temple
          - Opera House
          - Military Academy
          - Military Base
          - Hospital
          - Workshop
          - Bank
          - Public School
          - Strategic Defense System
          - Constabulary
          - Hotel
          - Chancery
          - Gallery
          - Gumey
        - GreatWorkCount: 0
        
        ### The Hague
        - ID: 11977
        - X: 11
        - Y: 47
        - Population: 27
        - MajorityReligion: Islam
        - DefenseStrength: 107
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 1344
        - FoodPerTurn: 75
        - ProductionStored: 263
        - ProductionPerTurn: 260
        - CurrentProduction: Atomic Bomb
        - ProductionTurnsLeft: 9
        - GoldPerTurn: 172
        - SciencePerTurn: 154
        - CulturePerTurn: 71
        - FaithPerTurn: 23
        - TourismPerTurn: 29
        - BuildingCount: 60
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Constabulary
          - Hotel
          - Airport
          - Coaling Station
          - Wire Service
          - Mine Field
          - Gumey
        - GreatWorkCount: 0
        
        ### Haarlem
        - ID: 12542
        - X: 14
        - Y: 49
        - Population: 22
        - MajorityReligion: Islam
        - DefenseStrength: 123
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 685
        - FoodPerTurn: 36
        - ProductionStored: 827
        - ProductionPerTurn: 274
        - CurrentProduction: Fleet Destroyer
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 139
        - SciencePerTurn: 127
        - CulturePerTurn: 66
        - FaithPerTurn: 23
        - TourismPerTurn: 22.75
        - HappinessDelta: -2
        - BuildingCount: 59
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Armory
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Constabulary
          - Hotel
          - Airport
          - Coaling Station
          - Wire Service
          - Mine Field
          - Gumey
        - GreatWorkCount: 0
        
        ### Wittenberg
        - ID: 13083
        - X: 23
        - Y: 43
        - Population: 25
        - MajorityReligion: Islam
        - DefenseStrength: 117
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 1063
        - FoodPerTurn: 27
        - ProductionStored: 784
        - ProductionPerTurn: 256
        - CurrentProduction: Fleet Destroyer
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 155
        - SciencePerTurn: 141
        - CulturePerTurn: 56
        - FaithPerTurn: 20
        - TourismPerTurn: 15.25
        - HappinessDelta: -3
        - BuildingCount: 56
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Stable
          - Windmill
          - Customs House
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
          - Hotel
          - Airport
          - Wire Service
          - Mine Field
          - Gumey
        - GreatWorkCount: 0
        
        ### Pyongyang
        - ID: 13222
        - X: 22
        - Y: 47
        - Population: 24
        - MajorityReligion: Islam
        - DefenseStrength: 119
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 1116
        - FoodPerTurn: 62
        - ProductionStored: 467
        - ProductionPerTurn: 265
        - CurrentProduction: Fighter
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 131
        - SciencePerTurn: 144
        - CulturePerTurn: 66
        - FaithPerTurn: 19
        - TourismPerTurn: 26
        - BuildingCount: 55
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Armory
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Hotel
          - Airport
          - Wire Service
          - Gumey
        - GreatWorkCount: 0
        
        ### Rio de Janeiro
        - ID: 16272
        - X: 41
        - Y: 22
        - Population: 32
        - MajorityReligion: Islam
        - DefenseStrength: 123
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 1651
        - FoodPerTurn: 69
        - ProductionStored: 0
        - ProductionPerTurn: 312
        - CurrentProduction: Ambassador
        - ProductionTurnsLeft: 4
        - GoldPerTurn: 208
        - SciencePerTurn: 189
        - CulturePerTurn: 102
        - FaithPerTurn: 29
        - TourismPerTurn: 44
        - HappinessDelta: -4
        - BuildingCount: 57
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Hospital
          - Workshop
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Constabulary
          - Hotel
          - Bath
          - Wire Service
          - Mine Field
          - Gumey
        - Wonders:
          - Oracle
        - GreatWorkCount: 0
        
        ### Tokyo
        - ID: 17745
        - X: 44
        - Y: 45
        - Population: 20
        - MajorityReligion: Islam
        - DefenseStrength: 97
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 857
        - FoodPerTurn: 3
        - ProductionStored: 809
        - ProductionPerTurn: 571
        - CurrentProduction: Strategic Defense System
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 161
        - SciencePerTurn: 123
        - CulturePerTurn: 68
        - FaithPerTurn: 19
        - TourismPerTurn: 22.75
        - HappinessDelta: -5
        - BuildingCount: 55
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Workshop
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Hotel
          - Coaling Station
          - Wire Service
          - Gumey
        - GreatWorkCount: 0
        
        ### Kyoto
        - ID: 19051
        - X: 45
        - Y: 40
        - Population: 25
        - MajorityReligion: Islam
        - DefenseStrength: 97
        - Health: 75%
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 304
        - FoodPerTurn: 57
        - ProductionStored: 1057
        - ProductionPerTurn: 349
        - CurrentProduction: Airport
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 122
        - SciencePerTurn: 109
        - CulturePerTurn: 59
        - FaithPerTurn: 20
        - TourismPerTurn: 14.25
        - HappinessDelta: 0
        - BuildingCount: 48
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Arena
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Arsenal
          - Hospital
          - Factory
          - Stock Exchange
          - Public School
          - Constabulary
          - Hotel
          - Bath
          - Coaling Station
          - Wire Service
          - Mine Field
          - Gumey
        - Wonders:
          - Terracotta Army
          - Red Fort
          - Grand Canal
        - GreatWorkCount: 0
        
        ## Player: Siam
        
        ### Martaban
        - ID: 8549
        - X: 63
        - Y: 22
        - Population: 23
        - MajorityReligion: Buddhism
        - DefenseStrength: 72
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Circus Maximus
          - Chartered Company
          - Imperial College
          - Court Chapel
        
        ### Nakhon Sawan
        - ID: 9524
        - X: 59
        - Y: 24
        - Population: 21
        - DefenseStrength: 72
        - IsCoastal: true
        
        ## Player: City-States
        
        ### Dublin
        - ID: 1069
        - X: 16
        - Y: 44
        - Population: 19
        - DefenseStrength: 94
        - Health: 73%
        - IsCoastal: true
        
        ### Palatium
        - ID: 1072
        - X: 39
        - Y: 48
        - Population: 21
        - MajorityReligion: Islam
        - DefenseStrength: 100
        - IsCoastal: true
        
        ### Ecbatana
        - ID: 1073
        - X: 63
        - Y: 35
        - Population: 19
        - DefenseStrength: 90
        - IsCoastal: true
        
        ### Antananarivo
        - ID: 1075
        - X: 74
        - Y: 23
        - Population: 23
        - DefenseStrength: 92
        - Health: 98%
        - IsCoastal: true
        
        ### Vientiane
        - ID: 9692
        - X: 74
        - Y: 30
        - Population: 17
        - DefenseStrength: 81
        - Health: 83%
        - IsOccupied: true
        - IsCoastal: true
        
        ### Luba
        - ID: 1076
        - X: 59
        - Y: 30
        - Population: 23
        - MajorityReligion: Islam
        - DefenseStrength: 91
        - IsCoastal: true
        
        ### Lutetia
        - ID: 16903
        - X: 33
        - Y: 47
        - Population: 9
        - MajorityReligion: Islam
        - DefenseStrength: 80
        
        ### Jakarta
        - ID: 1079
        - X: 55
        - Y: 19
        - Population: 23
        - MajorityReligion: Islam
        - DefenseStrength: 91
        - IsCoastal: true
        
        ### Harappa
        - ID: 1080
        - X: 44
        - Y: 32
        - Population: 14
        - MajorityReligion: Islam
        - DefenseStrength: 93
        - Health: 95%
        
        # Military
        Military: summary reports about tactical zones and visible units.
        
        ## Unit Stats
        - CityBombard:
          - Artillery:
            - Strength: 27
            - RangedStrength: 50
        - FastAttack:
          - Tank:
            - Strength: 75
          - T-34:
            - Strength: 82
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
          - Anti-Aircraft Gun:
            - Strength: 40
        - Ranged:
          - Machine Gun:
            - Strength: 45
            - RangedStrength: 58
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
        - AssaultSea:
          - Battleship:
            - Strength: 60
            - RangedStrength: 75
          - Submarine:
            - Strength: 40
            - RangedStrength: 60
        - AttackAir:
          - Heavy Bomber:
            - RangedStrength: 65
          - Bomber:
            - RangedStrength: 50
        - DefenseAir:
          - Fighter:
            - RangedStrength: 60
          - Triplane:
            - RangedStrength: 45
        
        ## Friendly Land Zone 1061
        - ZoneValue: 66
        - Dominance: Friendly
        - FriendlyStrength: 2593
        - City: Gao
        - AreaID: 25
        - Plots: 37
        - CenterX: 34
        - CenterY: 39
        - Units:
          - Songhai:
            - Heavy Bomber: 3
            - Fighter: 3
        - Neighbors:
          - 2568
          - 1867
          - 16903
          - 2951
          - 1276
          - 1543
        
        ## Neutral Land Zone 1069
        - ZoneValue: 72
        - Dominance: Enemy
        - Posture: Attrition
        - EnemyStrength: 6040
        - NeutralStrength: 65
        - FriendlyStrength: 3264
        - City: Dublin
        - AreaID: 65
        - Plots: 11
        - CenterX: 16
        - CenterY: 43
        - Units:
          - City-State Dublin:
            - Infantry: 1
          - The Zulus:
            - Mechanized Infantry: 5
            - T-34: 1
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - -1069
          - 17235
          - -17235
        
        ## Neutral Land Zone 1072
        - ZoneValue: 24
        - Dominance: Friendly
        - NeutralStrength: 100
        - FriendlyStrength: 2449
        - City: Palatium
        - AreaID: 25
        - Plots: 22
        - CenterX: 39
        - CenterY: 48
        - Units:
          - City-State Palatium:
            - Tank: 1
        - Neighbors:
          - 16903
          - -1072
          - 1543
          - 17745
        
        ## Neutral Land Zone 1075
        - ZoneValue: 24
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 200
        - NeutralStrength: 87
        - FriendlyStrength: 696
        - City: Antananarivo
        - AreaID: 43
        - Plots: 13
        - CenterX: 74
        - CenterY: 24
        - Units:
          - City-State Antananarivo:
            - Fighter: 1
            - Machine Gun: 1
        - Neighbors:
          - -1075
        
        ## Neutral Land Zone 1080
        - ZoneValue: 18
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 4535
        - NeutralStrength: 80
        - FriendlyStrength: 3657
        - City: Harappa
        - AreaID: 25
        - Plots: 38
        - CenterX: 43
        - CenterY: 32
        - Units:
          - City-State Harappa:
            - Machine Gun: 1
          - Songhai:
            - Bazooka: 2
        - Neighbors:
          - 5558
          - 2951
          - 1276
          - 3641
          - 19051
          - 1361
        
        ## Friendly Land Zone 1276
        - ZoneValue: 48
        - Dominance: Friendly
        - FriendlyStrength: 5847
        - City: Tombouctu
        - AreaID: 25
        - Plots: 27
        - CenterX: 39
        - CenterY: 38
        - Units:
          - Songhai:
            - Fighter: 3
            - Bazooka: 2
        - Neighbors:
          - 1061
          - 2951
          - 1543
          - 1080
          - 19051
        
        ## Enemy Land Zone 1361
        - ZoneValue: 168
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 5353
        - FriendlyStrength: 3295
        - City: Osaka
        - AreaID: 25
        - Plots: 16
        - CenterX: 47
        - CenterY: 36
        - Units:
          - Japan:
            - Anti-Aircraft Gun: 1
            - Infantry: 1
        - Neighbors:
          - 19051
          - 1080
          - -1361
        
        ## Friendly Land Zone 1543
        - ZoneValue: 54
        - Dominance: Friendly
        - FriendlyStrength: 5216
        - City: Jenne
        - AreaID: 25
        - Plots: 28
        - CenterX: 39
        - CenterY: 43
        - Units:
          - Songhai:
            - Heavy Bomber: 3
            - Fighter: 3
        - Neighbors:
          - 1061
          - 16903
          - 1276
          - 1072
          - 17745
          - 19051
        
        ## Friendly Land Zone 1867
        - ZoneValue: 48
        - Dominance: Friendly
        - FriendlyStrength: 2568
        - City: Taghaza
        - AreaID: 45
        - Plots: 21
        - CenterX: 31
        - CenterY: 34
        - Units:
          - Songhai:
            - Fighter: 2
            - Bazooka: 1
        - Neighbors:
          - -1867
          - 2568
          - 2157
          - 1061
          - 2951
        
        ## Friendly Land Zone 2157
        - ZoneValue: 48
        - Dominance: Friendly
        - FriendlyStrength: 1616
        - City: Tondibi
        - AreaID: 45
        - Plots: 26
        - CenterX: 33
        - CenterY: 29
        - Units:
          - Songhai:
            - Heavy Bomber: 1
            - Bazooka: 1
        - Neighbors:
          - 1867
          - 4728
          - 5558
          - 2951
        
        ## Friendly Land Zone 2568
        - ZoneValue: 48
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 140
        - FriendlyStrength: 3186
        - City: Kumbi Saleh
        - AreaID: 45
        - Plots: 19
        - CenterX: 29
        - CenterY: 40
        - Units:
          - Songhai:
            - Artillery: 3
            - Bazooka: 1
        - Neighbors:
          - 1867
          - 1061
          - 16903
        
        ## Enemy Land Zone 2830
        - ZoneValue: 24
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 4400
        - FriendlyStrength: 110
        - City: Daegu
        - AreaID: 2
        - Plots: 9
        - CenterX: 20
        - CenterY: 33
        - Units:
          - Korea:
            - Battleship: 1
            - Infantry: 1
        
        ## Friendly Land Zone 2951
        - ZoneValue: 48
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 126
        - FriendlyStrength: 4043
        - City: Kukia
        - AreaID: 25
        - Plots: 35
        - CenterX: 38
        - CenterY: 33
        - Units:
          - Songhai:
            - Heavy Bomber: 1
            - Fighter: 2
            - Bazooka: 3
        - Neighbors:
          - 2157
          - 1867
          - 1061
          - 5558
          - 1276
          - 1080
        
        ## Enemy Land Zone 3641
        - ZoneValue: 12
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 4046
        - FriendlyStrength: 2686
        - City: Izumo
        - AreaID: 31
        - Plots: 28
        - CenterX: 44
        - CenterY: 26
        - Units:
          - Japan:
            - Anti-Aircraft Gun: 1
            - Infantry: 1
            - Triplane: 4
            - Bomber: 1
            - Machine Gun: 1
        - Neighbors:
          - 5558
          - 16272
          - 1080
          - 3937
        
        ## Enemy Land Zone 3937
        - ZoneValue: 42
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 3519
        - FriendlyStrength: 238
        - City: Nagasaki
        - AreaID: 31
        - Plots: 19
        - CenterX: 47
        - CenterY: 20
        - Units:
          - Japan:
            - Infantry: 1
            - Triplane: 3
            - Machine Gun: 1
        - Neighbors:
          - 16272
          - 3641
          - 6483
          - 12516
        
        ## Friendly Land Zone 4728
        - ZoneValue: 48
        - Dominance: Friendly
        - FriendlyStrength: 3145
        - City: Walata
        - AreaID: 27
        - Plots: 23
        - CenterX: 35
        - CenterY: 22
        - Units:
          - Songhai:
            - Heavy Bomber: 1
            - Anti-Aircraft Gun: 1
            - Bazooka: 2
        - Neighbors:
          - -4728
          - 2157
          - 5558
          - 9242
          - 16272
        
        ## Friendly Land Zone 5558
        - ZoneValue: 54
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 715
        - FriendlyStrength: 4294
        - City: Sao Paulo
        - AreaID: 25
        - Plots: 34
        - CenterX: 37
        - CenterY: 27
        - Units:
          - Songhai:
            - Fighter: 1
            - Artillery: 1
            - Anti-Aircraft Gun: 1
            - Bazooka: 2
        - Neighbors:
          - 2157
          - 4728
          - 2951
          - 16272
          - 3641
          - 1080
        
        ## Enemy Land Zone 6483
        - ZoneValue: 60
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 2612
        - FriendlyStrength: 1473
        - City: Yokohama
        - AreaID: 21
        - Plots: 18
        - CenterX: 44
        - CenterY: 16
        - Units:
          - Japan:
            - Infantry: 1
            - Triplane: 1
            - Bomber: 1
        - Neighbors:
          - 9242
          - -11608
          - 12516
          - 3937
        
        ## Friendly Land Zone 9242
        - ZoneValue: 3
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 787
        - FriendlyStrength: 2309
        - City: Shimonoseki
        - AreaID: 24
        - Plots: 24
        - CenterX: 39
        - CenterY: 17
        - Units:
          - Songhai:
            - Heavy Bomber: 1
            - Bazooka: 2
        - Neighbors:
          - 4728
          - 16272
          - 6483
        
        ## Neutral Land Zone 9692
        - ZoneValue: 36
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 612
        - NeutralStrength: 65
        - FriendlyStrength: 594
        - City: Vientiane
        - AreaID: 43
        - Plots: 11
        - CenterX: 73
        - CenterY: 29
        - Units:
          - City-State Antananarivo:
            - Tank: 1
        - Neighbors:
          - -9692
          - -1075
        
        ## Friendly Land Zone 11571
        - ZoneValue: 576
        - Dominance: Enemy
        - Posture: Hedgehog
        - EnemyStrength: 1638
        - FriendlyStrength: 688
        - City: Tilburg
        - AreaID: 6
        - Plots: 21
        - CenterX: 50
        - CenterY: 6
        - Units:
          - Japan:
            - Rifleman: 2
          - Songhai:
            - Mechanized Infantry: 1
            - Fighter: 2
        - Neighbors:
          - 11608
          - -11571
          - 13125
        
        ## Enemy Land Zone 11608
        - ZoneValue: 12
        - Dominance: Even
        - Posture: Withdraw
        - EnemyStrength: 1923
        - FriendlyStrength: 1152
        - City: Matsuyama
        - AreaID: 13
        - Plots: 11
        - CenterX: 46
        - CenterY: 10
        - Units:
          - Japan:
            - Anti-Aircraft Gun: 1
            - Triplane: 1
            - Bomber: 1
            - Machine Gun: 2
        - Neighbors:
          - -11608
          - -11571
          - 11571
          - 12516
        
        ## Friendly Land Zone 11977
        - ZoneValue: 168
        - Dominance: Even
        - Posture: Counterattack
        - EnemyStrength: 2411
        - FriendlyStrength: 3420
        - City: The Hague
        - AreaID: 71
        - Plots: 6
        - CenterX: 11
        - CenterY: 48
        - Units:
          - Songhai:
            - Anti-Aircraft Gun: 1
            - Bazooka: 1
        - Neighbors:
          - -11977
          - -12542
        
        ## Enemy Land Zone 12516
        - ZoneValue: 60
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 2745
        - FriendlyStrength: 660
        - City: Sapporo
        - AreaID: 17
        - Plots: 15
        - CenterX: 48
        - CenterY: 14
        - Units:
          - Japan:
            - Destroyer: 1
            - Infantry: 2
            - Machine Gun: 1
        - Neighbors:
          - 11608
          - 6483
          - 3937
        
        ## Friendly Land Zone 12542
        - ZoneValue: 12
        - Dominance: Even
        - Posture: Counterattack
        - EnemyStrength: 2264
        - FriendlyStrength: 3832
        - City: Haarlem
        - AreaID: 72
        - Plots: 6
        - CenterX: 14
        - CenterY: 49
        - Units:
          - Songhai:
            - Bazooka: 6
        - Neighbors:
          - -11977
          - -12542
        
        ## Friendly Land Zone 13083
        - ZoneValue: 36
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 1089
        - FriendlyStrength: 3094
        - City: Wittenberg
        - AreaID: 66
        - Plots: 4
        - CenterX: 23
        - CenterY: 43
        - Units:
          - Songhai:
            - Bazooka: 3
        - Neighbors:
          - -13083
          - -13222
        
        ## Enemy Land Zone 13125
        - ZoneValue: 30
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 976
        - FriendlyStrength: 422
        - City: Hakodate
        - AreaID: 4
        - Plots: 14
        - CenterX: 54
        - CenterY: 3
        - Units:
          - Japan:
            - Triplane: 2
            - Machine Gun: 2
        - Neighbors:
          - 11571
          - -11571
        
        ## Friendly Land Zone 13222
        - ZoneValue: 36
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 306
        - FriendlyStrength: 2422
        - City: Pyongyang
        - AreaID: 70
        - Plots: 8
        - CenterX: 23
        - CenterY: 48
        - Units:
          - Songhai:
            - Mechanized Infantry: 1
            - Artillery: 1
            - Bazooka: 2
        - Neighbors:
          - -13222
        
        ## Friendly Land Zone 16272
        - ZoneValue: 42
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 1195
        - FriendlyStrength: 3906
        - City: Rio de Janeiro
        - AreaID: 25
        - Plots: 21
        - CenterX: 40
        - CenterY: 21
        - Units:
          - Songhai:
            - Fighter: 2
            - Bazooka: 1
        - Neighbors:
          - 4728
          - 9242
          - 5558
          - 3641
          - 3937
        
        ## Neutral Land Zone 16903
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 80
        - FriendlyStrength: 380
        - City: Lutetia
        - AreaID: 25
        - Plots: 41
        - CenterX: 33
        - CenterY: 46
        - Units:
          - City-State Lutetia:
            - Anti-Aircraft Gun: 2
        - Neighbors:
          - 2568
          - 1061
          - 1543
          - 1072
          - -1072
        
        ## Enemy Land Zone 17235
        - ZoneValue: 15
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 8839
        - FriendlyStrength: 93
        - City: Huari
        - AreaID: 2
        - Plots: 14
        - CenterX: 13
        - CenterY: 38
        - Units:
          - The Zulus:
            - Mobile SAM: 1
        - Neighbors:
          - -17235
          - -1069
          - 1069
        
        ## Friendly Land Zone 17745
        - ZoneValue: 36
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 120
        - FriendlyStrength: 5714
        - City: Tokyo
        - AreaID: 25
        - Plots: 21
        - CenterX: 43
        - CenterY: 46
        - Units:
          - Songhai:
            - Artillery: 2
            - Anti-Aircraft Gun: 1
            - Bazooka: 3
        - Neighbors:
          - 1543
          - 1072
          - -1072
          - 19051
        
        ## Friendly Land Zone 19051
        - ZoneValue: 84
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 1578
        - FriendlyStrength: 6594
        - City: Kyoto
        - AreaID: 25
        - Plots: 24
        - CenterX: 44
        - CenterY: 39
        - Units:
          - Songhai:
            - Bazooka: 9
        - Neighbors:
          - 1276
          - 1543
          - 1080
          - 17745
          - 1361
        
        ## Neutral Sea Zone -1069
        - ZoneValue: 24
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 2862
        - NeutralStrength: 65
        - FriendlyStrength: 2206
        - City: Dublin
        - AreaID: 0
        - Plots: 30
        - CenterX: 17
        - CenterY: 44
        - Units:
          - The Zulus:
            - Mechanized Infantry: 1
          - Korea:
            - Fleet Destroyer: 3
        - Neighbors:
          - -17235
          - -11977
          - 1069
          - 17235
          - -12542
          - -13083
          - -13222
        
        ## Enemy Sea Zone -1361
        - ZoneValue: 14
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 4482
        - FriendlyStrength: 2064
        - City: Osaka
        - AreaID: 54
        - Plots: 15
        - CenterX: 49
        - CenterY: 38
        - Units:
          - Japan:
            - Destroyer: 1
        - Neighbors:
          - 1361
        
        ## Enemy Sea Zone -11608
        - ZoneValue: 20
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 1796
        - FriendlyStrength: 750
        - City: Matsuyama
        - AreaID: 0
        - Plots: 39
        - CenterX: 43
        - CenterY: 8
        - Units:
          - Japan:
            - Destroyer: 1
        - Neighbors:
          - 11608
          - 6483
          - -11571
        
        ## Neutral Sea Zone -9692
        - ZoneValue: 1
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 1973
        - NeutralStrength: 65
        - FriendlyStrength: 156
        - City: Vientiane
        - AreaID: 0
        - Plots: 33
        - CenterX: 74
        - CenterY: 32
        - Units:
          - Japan:
            - Destroyer: 3
        - Neighbors:
          - -1075
          - 9692
        
        ## Friendly Sea Zone -13222
        - ZoneValue: 12
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 644
        - FriendlyStrength: 1573
        - City: Pyongyang
        - AreaID: 0
        - Plots: 40
        - CenterX: 22
        - CenterY: 49
        - Units:
          - Songhai:
            - Destroyer: 1
        - Neighbors:
          - -1069
          - -12542
          - -13083
          - 13222
          - 13083
        
        ## Neutral Sea Zone -1075
        - ZoneValue: 8
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 1654
        - NeutralStrength: 87
        - FriendlyStrength: 252
        - City: Antananarivo
        - AreaID: 0
        - Plots: 51
        - CenterX: 74
        - CenterY: 21
        - Units:
          - Japan:
            - Destroyer: 3
        - Neighbors:
          - 1075
          - -9692
          - 9692
        
        ## Friendly Sea Zone -4728
        - ZoneValue: 16
        - Dominance: Friendly
        - FriendlyStrength: 3102
        - City: Walata
        - AreaID: 0
        - Plots: 34
        - CenterX: 33
        - CenterY: 21
        - Units:
          - Songhai:
            - Submarine: 2
            - Bazooka: 1
            - Fleet Destroyer: 2
        - Neighbors:
          - 4728
        
        ## Friendly Sea Zone -1867
        - ZoneValue: 16
        - Dominance: Friendly
        - FriendlyStrength: 2566
        - City: Taghaza
        - AreaID: 0
        - Plots: 19
        - CenterX: 27
        - CenterY: 33
        - Units:
          - Songhai:
            - Fleet Destroyer: 1
        - Neighbors:
          - 1867
        
        ## Enemy Sea Zone -17235
        - ZoneValue: 1
        - Dominance: Enemy
        - EnemyStrength: 4826
        - City: Huari
        - AreaID: 55
        - Plots: 23
        - CenterX: 13
        - CenterY: 40
        - Units:
          - Japan:
            - Destroyer: 1
        - Neighbors:
          - -11977
          - 17235
          - -1069
          - 1069
        
        ## Neutral Sea Zone -1072
        - ZoneValue: 1
        - Dominance: Friendly
        - NeutralStrength: 100
        - FriendlyStrength: 1985
        - City: Palatium
        - AreaID: 74
        - Plots: 23
        - CenterX: 39
        - CenterY: 50
        - Units:
          - City-State Palatium:
            - Fleet Destroyer: 2
        - Neighbors:
          - 16903
          - 1072
          - 17745
        
        ## Friendly Sea Zone -11571
        - ZoneValue: 8
        - Dominance: Enemy
        - Posture: Hedgehog
        - EnemyStrength: 1529
        - FriendlyStrength: 389
        - City: Tilburg
        - AreaID: 0
        - Plots: 39
        - CenterX: 51
        - CenterY: 7
        - Units:
          - Japan:
            - Destroyer: 2
        - Neighbors:
          - -11608
          - 11608
          - 11571
          - 13125
        
        ## Friendly Sea Zone -12542
        - ZoneValue: 12
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 278
        - FriendlyStrength: 2984
        - City: Haarlem
        - AreaID: 0
        - Plots: 31
        - CenterX: 15
        - CenterY: 50
        - Units:
          - Songhai:
            - Bazooka: 1
        - Neighbors:
          - 11977
          - -11977
          - 12542
          - -1069
          - -13222
        
        ## Friendly Sea Zone -13083
        - ZoneValue: 12
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 936
        - FriendlyStrength: 2164
        - City: Wittenberg
        - AreaID: 0
        - Plots: 40
        - CenterX: 23
        - CenterY: 42
        - Units:
          - Songhai:
            - Submarine: 1
            - Fleet Destroyer: 1
          - The Zulus:
            - Submarine: 1
        - Neighbors:
          - -1069
          - -13222
          - 13083
        
        ## Friendly Sea Zone -11977
        - ZoneValue: 14
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 1345
        - FriendlyStrength: 2485
        - City: The Hague
        - AreaID: 0
        - Plots: 45
        - CenterX: 9
        - CenterY: 47
        - Units:
          - Japan:
            - Ironclad: 1
          - Songhai:
            - Bazooka: 1
        - Neighbors:
          - -17235
          - 11977
          - -12542
          - -1069
          - 12542
        
        # Events
        Events: events since you last made a decision.
        
        ## Turn 426
        
        ### 0
        - Type: CombatResult
        - Plains Land 16,41:
          - Owner: City-State Dublin
          - Improvement: Farm
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 33
          - Damage: 102
          - Unit:
            - Level: 4
            - Health: 44%
            - AI: Counter
            - Unit: Anti-Aircraft Gun
            - ID: 15770
          - Player: 3: The Zulus
        
        ### 1
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1304
        - Player: 29
        - Coast 41,49:
          - Owner: City-State Palatium
        
        ### 2
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19152
        - Player: 29
        - Coast 41,48:
          - Owner: City-State Palatium
          - Resource: Pearls
          - Improvement: Fishing Boats
        
        ### 3
        - Type: CombatResult
        - Coast 75,30:
          - Owner: City-State Antananarivo
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 10
          - Damage: 10
          - Unit:
            - Level: 6
            - AI: AttackSea
            - Unit: Destroyer
            - ID: 18785
          - Player: 1: Japan
        
        ### 4
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 78%
          - AI: Defense
          - Unit: Infantry
          - ID: 17938
        - Player: 32
        - Plots:
          - Grass Land 76,25:
            - Owner: Japan
            - Improvement: Farm
          - Grass Land 75,25:
            - Owner: City-State Antananarivo
            - Route: Road
        
        ### 5
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: WorkerSea
          - Unit: Work Boat
          - ID: 19154
        - Player: 32
        - Coast 72,24:
          - Owner: City-State Antananarivo
          - Resource: Fish
        
        ### 6
        - Type: TileImprovementChanged
        - Owner: 32
        - NewImprovement: Fishing Boats
        - Coast 72,24:
          - Owner: City-State Antananarivo
          - Resource: Fish
          - Improvement: Fishing Boats
        
        ### 7
        - Type: BuildFinished
        - Player: 32
        - Improvement: Fishing Boats
        - Coast 72,24:
          - Owner: City-State Antananarivo
          - Resource: Fish
          - Improvement: Fishing Boats
        
        ### 8
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Unit:
          - Level: 1
          - AI: WorkerSea
          - Unit: Work Boat
          - ID: 19154
        - Owner: 32
        - Build: Create Fishing Boats
        - Coast 72,24:
          - Owner: City-State Antananarivo
          - Resource: Fish
          - Improvement: Fishing Boats
        
        ### 9
        - Type: UnitBuildStart
        - Unit:
          - Level: 1
          - AI: WorkerSea
          - Unit: Work Boat
          - ID: 19154
        - Owner: 32
        - Build: Create Fishing Boats
        - Coast 72,24:
          - Owner: City-State Antananarivo
          - Resource: Fish
          - Improvement: Fishing Boats
        
        ### 10
        - Type: TileImprovementChanged
        - Owner: 34
        - OldImprovement: Mine
        - NewImprovement: Mine
        - Tundra Hills 31,47:
          - Owner: City-State Lutetia
          - Improvement: Mine
        
        ### 11
        - Type: BuildFinished
        - Player: 34
        - Tundra Hills 31,47:
          - Owner: City-State Lutetia
          - Improvement: Mine
        
        ### 12
        - Type: UnitBuildCompleted
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 17271
        - Owner: 34
        - Build: Repair an Improvement
        - Tundra Hills 31,47:
          - Owner: City-State Lutetia
          - Improvement: Mine
        
        ### 13
        - Type: UnitBuildStart
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 17271
        - Owner: 34
        - Build: Repair an Improvement
        - Tundra Hills 31,47:
          - Owner: City-State Lutetia
          - Improvement: Mine
        
        ### 14
        - Type: UnitPromoted
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15891
        - Player: 37
        - Promotion: Firing Doctrine
        
        ### 15
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Battleship
          - ID: 19403
        - Player: 0: Korea
        - Grass Land 22,29:
          - Owner: Korea
          - CityID: 1057
          - Population: 34
          - IsRiver: true
          - City: Seoul
          - Route: Railroad
        
        ### 16
        - Type: UnitCreated
        - UnitType: Battleship
        - Player: 0: Korea
        - Unit:
          - Level: 1
          - AI: AssaultSea
          - Unit: Battleship
          - ID: 19403
        - Grass Land 22,29:
          - Owner: Korea
          - CityID: 1057
          - Population: 34
          - IsRiver: true
          - City: Seoul
          - Route: Railroad
        
        ### 17
        - Type: CityTrained
        - Player: 0: Korea
        - City:
          - Name: Seoul
          - Population: 34
          - ID: 1057
        - Unit:
          - Level: 1
          - AI: AssaultSea
          - Unit: Battleship
          - ID: 19403
        
        ### 18
        - Type: EspionageState
        - SpyIndex: 0
        - SpyState: 5
        - City:
          - Owner: Korea
          - CityID: 1057
          - Population: 34
          - IsRiver: true
          - City: Seoul
          - Terrain: Grass
          - Route: Railroad
          - Plot: Land
          - X: 22
          - Y: 29
        - SpyOwner: 0: Korea
        
        ### 19
        - Type: CityEventChoiceActivated
        - City:
          - Name: Seoul
          - Population: 34
          - ID: 1057
        - Player: 0: Korea
        - Choice: 89
        
        ### 20
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19225
        - Player: 0: Korea
        - Grass Land 22,29:
          - Owner: Korea
          - CityID: 1057
          - Population: 34
          - IsRiver: true
          - City: Seoul
          - Route: Railroad
        
        ### 21
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19026
        - Player: 0: Korea
        - Grass Land 22,29:
          - Owner: Korea
          - CityID: 1057
          - Population: 34
          - IsRiver: true
          - City: Seoul
          - Route: Railroad
        
        ### 22
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18978
        - Player: 0: Korea
        - Grass Land 22,29:
          - Owner: Korea
          - CityID: 1057
          - Population: 34
          - IsRiver: true
          - City: Seoul
          - Route: Railroad
        
        ### 23
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: AssaultSea
          - Unit: Battleship
          - ID: 19403
        - Player: 0: Korea
        - Promotions:
          - Targeting I
          - Air Defense I
          - Air Defense II
        
        ### 24
        - Type: TileImprovementChanged
        - Owner: 26
        - OldImprovement: Fishing Boats
        - Coast 17,44:
          - Owner: City-State Dublin
          - Resource: Fish
        
        ### 25
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 39%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19072
        - Player: 0: Korea
        - Plots:
          - Ocean 18,43:
            - Owner: City-State Dublin
        
        ### 26
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Battleship
          - ID: 19403
        - Player: 0: Korea
        - Plots:
          - Coast 23,30:
            - Owner: Korea
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 22,31:
            - Owner: Korea
            - Resource: Oil
            - Improvement: Offshore Platform
          - Coast 22,32:
            - Owner: Korea
        
        ### 27
        - Type: CityProjectComplete
        - City:
          - Name: Matsuyama
          - Population: 18
          - ID: 11608
        - Player: 1: Japan
        - Project: Public Works
        
        ### 28
        - Type: CityCreated
        - City:
          - Name: Matsuyama
          - Population: 18
          - ID: 11608
        - Owner: 1: Japan
        - Project: Public Works
        
        ### 29
        - Type: CityBoughtPlot
        - WithFaithCulture: true
        - Player: 1: Japan
        - City:
          - Name: Sapporo
          - Population: 18
          - ID: 12516
        - Ocean 52,15:
          - Owner: Japan
        
        ### 30
        - Type: UnitPromoted
        - Unit:
          - Level: 5
          - AI: DefenseAir
          - Unit: Triplane
          - ID: 18114
        - Player: 1: Japan
        - Promotion: Ace Pilot IV
        
        ### 31
        - Type: UnitPromoted
        - Unit:
          - Level: 5
          - Health: 80%
          - AI: DefenseAir
          - Unit: Triplane
          - ID: 18062
        - Player: 1: Japan
        - Promotion: Ace Pilot IV
        
        ### 32
        - Type: UnitPromoted
        - Unit:
          - Level: 7
          - Health: 35%
          - AI: AttackAir
          - Unit: Bomber
          - ID: 17954
        - Player: 1: Japan
        - Promotion: Siege I
        
        ### 33
        - Type: UnitPromoted
        - Unit:
          - Level: 5
          - Health: 73%
          - AI: AttackAir
          - Unit: Bomber
          - ID: 19036
        - Player: 1: Japan
        - Promotion: Air Logistics
        
        ### 34
        - Type: CityBeginsWLTKD
        - Change: 6
        - City:
          - Owner: Japan
          - CityID: 3641
          - Population: 27
          - IsRiver: true
          - City: Izumo
          - Terrain: Grass
          - Religion: Islam
          - Route: Railroad
          - Plot: Land
          - X: 44
          - Y: 26
        - Player: 1: Japan
        
        ### 35
        - Type: CityExtendsWeLoveKingDay
        - Change: 6
        - City:
          - Owner: Japan
          - CityID: 3937
          - Population: 27
          - City: Nagasaki
          - Terrain: Desert
          - Religion: Islam
          - Route: Railroad
          - Plot: Land
          - X: 48
          - Y: 20
        - Player: 1: Japan
        
        ### 36
        - Type: CityBeginsWLTKD
        - Change: 6
        - City:
          - Owner: Japan
          - CityID: 6483
          - Population: 20
          - City: Yokohama
          - Terrain: Grass
          - Resource: Cattle
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 45
          - Y: 15
        - Player: 1: Japan
        
        ### 37
        - Type: CityExtendsWeLoveKingDay
        - Change: 6
        - City:
          - Owner: Japan
          - CityID: 11608
          - Population: 18
          - City: Matsuyama
          - Terrain: Plains
          - Resource: Wheat
          - Religion: Islam
          - Route: Railroad
          - Plot: Land
          - X: 45
          - Y: 10
        - Player: 1: Japan
        
        ### 38
        - Type: CityExtendsWeLoveKingDay
        - Change: 6
        - City:
          - Owner: Japan
          - CityID: 12516
          - Population: 18
          - City: Sapporo
          - Terrain: Plains
          - Resource: Iron
          - Religion: Islam
          - Route: Railroad
          - Plot: Hills
          - X: 49
          - Y: 14
        - Player: 1: Japan
        
        ### 39
        - Type: CityBeginsWLTKD
        - Change: 6
        - City:
          - Owner: Japan
          - CityID: 13125
          - Population: 17
          - City: Hakodate
          - Terrain: Tundra
          - Resource: Sheep
          - Religion: Islam
          - Route: Railroad
          - Plot: Hills
          - X: 55
          - Y: 3
        - Player: 1: Japan
        
        ### 40
        - Type: CombatResult
        - Grass Land 75,25:
          - Owner: City-State Antananarivo
          - Route: Road
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 11
          - Damage: 38
          - Unit:
            - Level: 6
            - Health: 78%
            - AI: Defense
            - Unit: Infantry
            - ID: 17938
          - Player: 32
        
        ### 41
        - Type: CombatResult
        - Desert Land 43,17:
          - Owner: Songhai
          - Resource: Oil
          - Improvement: Oil Well
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 20
          - Damage: 20
          - Unit:
            - Level: 4
            - AI: Ranged
            - Unit: Bazooka
            - ID: 18765
          - Player: 4: Songhai
        
        ### 42
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Light Tank
          - ID: 18654
        - Player: 1: Japan
        - Plots:
          - Plains Land 47,32:
            - Owner: Japan
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Hills 46,33:
            - Owner: Japan
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 46,34:
            - Owner: Japan
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 44,35:
            - Owner: Japan
            - IsRiver: true
            - Route: Railroad
          - Desert Land 44,34:
            - Owner: City-State Harappa
            - IsRiver: true
            - Improvement: Farm
            - Feature: Flood Plains
        
        ### 43
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 62%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18056
        - Player: 1: Japan
        - Plots:
          - Coast 49,13:
            - Owner: Japan
          - Coast 50,12:
            - Owner: Japan
          - Coast 49,11:
            - Owner: Japan
          - Coast 49,10:
            - Owner: Japan
          - Coast 48,9:
            - Owner: Japan
        
        ### 44
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 50%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18272
        - Player: 1: Japan
        - Plots:
          - Coast 49,11:
            - Owner: Japan
          - Coast 49,10:
            - Owner: Japan
          - Coast 48,9:
            - Owner: Japan
          - Coast 49,8:
            - Owner: Songhai
          - Coast 49,7:
            - Owner: Songhai
        
        ### 45
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 62%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18056
        - Player: 1: Japan
        - Coast 48,9:
          - Owner: Japan
        
        ### 46
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 37%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18270
        - Player: 1: Japan
        - Plots:
          - Coast 50,12:
            - Owner: Japan
          - Coast 49,11:
            - Owner: Japan
          - Coast 49,10:
            - Owner: Japan
        
        ### 47
        - Type: CombatResult
        - Desert Land 43,17:
          - Owner: Songhai
          - Resource: Oil
          - Improvement: Oil Well
        - Attacker:
          - RemainingHP: 15
          - Damage: 42
        - Defender:
          - RemainingHP: 29
          - Damage: 49
          - Player: 4: Songhai
          - Unit:
            - Level: 4
            - Health: 80%
            - AI: Ranged
            - Unit: Bazooka
            - ID: 18765
        
        ### 48
        - Type: CombatResult
        - Desert Land 43,17:
          - Owner: Songhai
          - Resource: Oil
          - Improvement: Oil Well
        - Attacker:
          - RemainingHP: 15
          - Damage: 57
        - Defender:
          - RemainingHP: 30
          - Damage: 79
          - Player: 4: Songhai
          - Unit:
            - Level: 4
            - Health: 51%
            - AI: Ranged
            - Unit: Bazooka
            - ID: 18765
        
        ### 49
        - Type: CombatResult
        - Grass Hills 41,15:
          - Owner: Songhai
          - Resource: Sheep
          - Improvement: Citadel
          - Route: Railroad
        - Attacker:
          - RemainingHP: 17
          - Damage: 36
        - Defender:
          - RemainingHP: 7
          - Damage: 7
          - Player: 4: Songhai
          - Unit:
            - Level: 3
            - AI: Ranged
            - Unit: Bazooka
            - ID: 18709
        
        ### 50
        - Type: CombatResult
        - Plains Hills 44,38:
          - Owner: Songhai
          - Improvement: Lumber Mill
          - Route: Railroad
          - Feature: Forest
        - Attacker:
          - RemainingHP: 48
          - Damage: 85
        - Defender:
          - RemainingHP: 20
          - Damage: 20
          - Player: 4: Songhai
          - Unit:
            - Level: 5
            - AI: DefenseAir
            - Unit: Fighter
            - ID: 17389
        
        ### 51
        - Type: CombatResult
        - Plains Land 45,40:
          - Owner: Songhai
          - CityID: 19051
          - Population: 25
          - IsRiver: true
          - City: Kyoto
          - Religion: Islam
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Player: 4: Songhai
        - Interceptor:
          - Damage: 54
          - Unit:
            - Level: 4
            - AI: DefenseAir
            - Unit: Fighter
            - ID: 18870
          - Player: 1: Japan
        
        ### 52
        - Type: UnitKilledInCombat
        - KilledPlayer: 1: Japan
        - KillerPlayer: 4: Songhai
        - KilledUnit: Bomber
        
        ### 53
        - Type: CombatResult
        - Plains Land 45,40:
          - Owner: Songhai
          - CityID: 19051
          - Population: 25
          - IsRiver: true
          - City: Kyoto
          - Religion: Islam
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Player: 4: Songhai
        - Interceptor:
          - Damage: 56
          - Unit:
            - Level: 4
            - AI: DefenseAir
            - Unit: Fighter
            - ID: 18870
          - Player: 1: Japan
        
        ### 54
        - Type: CombatResult
        - Grass Land 75,25:
          - Owner: City-State Antananarivo
          - Route: Road
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Unit:
            - Level: 6
            - Health: 69%
            - AI: Defense
            - Unit: Infantry
            - ID: 17938
          - Player: 32
        - Interceptor:
          - Damage: 84
          - Unit:
            - Level: 3
            - AI: DefenseAir
            - Unit: Fighter
            - ID: 19068
          - Player: 32
        
        ### 55
        - Type: CombatResult
        - Grass Land 75,25:
          - Owner: City-State Antananarivo
          - Route: Road
        - Attacker:
          - RemainingHP: 12
          - Damage: 12
        - Defender:
          - RemainingHP: 18
          - Damage: 31
          - Unit:
            - Level: 6
            - Health: 89%
            - AI: Defense
            - Unit: Infantry
            - ID: 17938
          - Player: 32
        
        ### 56
        - Type: UnitMoved
        - Unit:
          - Level: 7
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18773
        - Player: 1: Japan
        - Plots:
          - Coast 77,23:
            - Owner: Japan
          - Ocean 77,22:
            - Owner: Japan
          - Coast 76,22:
            - Owner: City-State Antananarivo
          - Coast 75,22:
            - Owner: City-State Antananarivo
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 57
        - Type: CombatResult
        - Grass Land 74,23:
          - Owner: City-State Antananarivo
          - CityID: 1075
          - Population: 23
          - City: Antananarivo
          - Resource: Jewelry
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 49
          - Damage: 49
          - Player: 32
        
        ### 58
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18186
        - Player: 1: Japan
        - Coast 77,23:
          - Owner: Japan
        
        ### 59
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 19241
        - Player: 1: Japan
        - Plots:
          - Coast 77,23:
            - Owner: Japan
          - Ocean 77,22:
            - Owner: Japan
          - Coast 76,21:
            - Owner: City-State Antananarivo
            - Feature: Atoll
        
        ### 60
        - Type: CombatResult
        - Grass Land 74,30:
          - Owner: City-State Antananarivo
          - CityID: 9692
          - Population: 17
          - IsRiver: true
          - City: Vientiane
          - Resource: Maize
          - Route: Railroad
        - Attacker:
          - RemainingHP: 22
          - Damage: 28
        - Defender:
          - RemainingHP: 32
          - Damage: 67
          - Player: 32
        
        ### 61
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Submarine
          - ID: 19019
        - Player: 1: Japan
        - Plots:
          - Coast 76,30:
            - Owner: Japan
          - Coast 75,30:
            - Owner: City-State Antananarivo
        
        ### 62
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 90%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18785
        - Player: 1: Japan
        - Coast 76,30:
          - Owner: Japan
        
        ### 63
        - Type: CombatResult
        - Grass Land 74,30:
          - Owner: City-State Antananarivo
          - CityID: 9692
          - Population: 17
          - IsRiver: true
          - City: Vientiane
          - Resource: Maize
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 5
          - Damage: 72
          - Player: 32
        
        ### 64
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Submarine
          - ID: 19019
        - Player: 1: Japan
        - Coast 75,31:
          - Owner: City-State Antananarivo
          - Feature: Atoll
        
        ### 65
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 96%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18117
        - Player: 1: Japan
        - Plots:
          - Coast 75,31:
            - Owner: City-State Antananarivo
            - Feature: Atoll
          - Coast 75,30:
            - Owner: City-State Antananarivo
        
        ### 66
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 81%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18324
        - Player: 1: Japan
        - Coast 74,31:
          - Owner: City-State Antananarivo
        
        ### 67
        - Type: CombatResult
        - Grass Land 74,30:
          - Owner: City-State Antananarivo
          - CityID: 9692
          - Population: 17
          - IsRiver: true
          - City: Vientiane
          - Resource: Maize
          - Route: Railroad
        - Attacker:
          - RemainingHP: 5
          - Damage: 10
        - Defender:
          - RemainingHP: 87
          - Damage: 159
          - Player: 32
        
        ### 68
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 81%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18324
        - Player: 1: Japan
        - Ocean 75,32:
          - Owner: City-State Antananarivo
        
        ### 69
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18659
        - Player: 1: Japan
        - Plots:
          - Ocean 76,31:
            - Owner: Japan
          - Coast 75,31:
            - Owner: City-State Antananarivo
            - Feature: Atoll
          - Coast 74,31:
            - Owner: City-State Antananarivo
        
        ### 70
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Submarine
          - ID: 18769
        - Player: 1: Japan
        - Plots:
          - Ocean 76,32:
            - Owner: Japan
          - Ocean 75,33:
            - Owner: City-State Antananarivo
        
        ### 71
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 81%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18324
        - Player: 1: Japan
        - Ocean 75,33:
          - Owner: City-State Antananarivo
        
        ### 72
        - Type: CombatResult
        - Grass Hills 40,31:
          - Owner: Songhai
          - IsRiver: true
          - Improvement: Holy Site
          - Route: Railroad
        - Attacker:
          - RemainingHP: 35
          - Damage: 35
        - Defender:
          - RemainingHP: 29
          - Damage: 29
          - Player: 4: Songhai
          - Unit:
            - Level: 4
            - AI: DefenseAir
            - Unit: Fighter
            - ID: 19209
        
        ### 73
        - Type: CombatResult
        - Grass Hills 40,31:
          - Owner: Songhai
          - IsRiver: true
          - Improvement: Holy Site
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Player: 4: Songhai
          - Unit:
            - Level: 7
            - AI: CityBombard
            - Unit: Artillery
            - ID: 15779
        - Interceptor:
          - Damage: 214
          - Unit:
            - Level: 6
            - Health: 85%
            - AI: DefenseAir
            - Unit: Fighter
            - ID: 18083
          - Player: 1: Japan
        
        ### 74
        - Type: UnitKilledInCombat
        - KilledPlayer: 1: Japan
        - KillerPlayer: 4: Songhai
        - KilledUnit: Bomber
        
        ### 75
        - Type: CombatResult
        - Grass Hills 40,31:
          - Owner: Songhai
          - IsRiver: true
          - Improvement: Holy Site
          - Route: Railroad
        - Attacker:
          - RemainingHP: 4
          - Damage: 48
        - Defender:
          - RemainingHP: 32
          - Damage: 32
          - Player: 4: Songhai
          - Unit:
            - Level: 7
            - AI: CityBombard
            - Unit: Artillery
            - ID: 15779
        
        ### 76
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Submarine
          - ID: 18653
        - Player: 1: Japan
        - Plots:
          - Coast 47,37:
            - Owner: Japan
          - Coast 48,38:
            - Owner: Japan
          - Coast 48,39:
            - Owner: Japan
            - Resource: Oil
          - Coast 49,39:
            - Owner: Japan
            - Resource: Fish
            - Improvement: Fishing Boats
          - Ocean 50,40:
            - Owner: Japan
          - Coast 49,41:
            - Owner: Songhai
        
        ### 77
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 19235
        - Player: 1: Japan
        - Plots:
          - Coast 50,14:
            - Owner: Japan
          - Plains Hills 49,14:
            - Owner: Japan
            - CityID: 12516
            - Population: 18
            - City: Sapporo
            - Resource: Iron
            - Religion: Islam
            - Route: Railroad
          - Plains Land 48,14:
            - Owner: Japan
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
          - Desert Land 47,13:
            - Owner: Japan
            - Improvement: Fort
            - Route: Railroad
          - Desert Hills 47,12:
            - Owner: Japan
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Desert Land 46,12:
            - Owner: Japan
            - Resource: Aluminum
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 45,11:
            - Owner: Japan
            - Improvement: Village
            - Route: Railroad
          - Plains Land 45,10:
            - Owner: Japan
            - CityID: 11608
            - Population: 18
            - City: Matsuyama
            - Resource: Wheat
            - Religion: Islam
            - Route: Railroad
          - Coast 44,11:
            - Owner: Japan
          - Plains Hills 44,10:
            - Owner: Japan
            - Improvement: Fort
        
        ### 78
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16375
        - Player: 1: Japan
        - Plots:
          - Plains Land 45,10:
            - Owner: Japan
            - CityID: 11608
            - Population: 18
            - City: Matsuyama
            - Resource: Wheat
            - Religion: Islam
            - Route: Railroad
          - Coast 44,11:
            - Owner: Japan
        
        ### 79
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 95%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18274
        - Player: 1: Japan
        - Plots:
          - Coast 46,16:
            - Owner: Japan
          - Grass Land 45,15:
            - Owner: Japan
            - CityID: 6483
            - Population: 20
            - City: Yokohama
            - Resource: Cattle
            - Religion: Buddhism
            - Route: Railroad
          - Coast 44,15:
            - Owner: Japan
          - Coast 44,12:
            - Owner: Japan
          - Coast 44,11:
            - Owner: Japan
        
        ### 80
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18659
        - Player: 1: Japan
        - Plots:
          - Coast 75,31:
            - Owner: City-State Antananarivo
            - Feature: Atoll
          - Coast 76,30:
            - Owner: Japan
        
        ### 81
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 81%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18324
        - Player: 1: Japan
        - Plots:
          - Ocean 76,32:
            - Owner: Japan
          - Ocean 76,31:
            - Owner: Japan
        
        ### 82
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 71%
          - AI: Defense
          - Unit: Infantry
          - ID: 18900
        - Player: 1: Japan
        - Plots:
          - Grass Hills 46,26:
            - Owner: Japan
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 45,26:
            - Owner: Japan
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 44,26:
            - Owner: Japan
            - CityID: 3641
            - Population: 27
            - IsRiver: true
            - City: Izumo
            - Religion: Islam
            - Route: Railroad
          - Grass Land 43,27:
            - Owner: Japan
            - Improvement: Farm
            - Route: Railroad
          - Mountain Mountain 43,28:
            - Owner: Japan
            - Route: Railroad
        
        ### 83
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 19415
        - Player: 1: Japan
        - Plots:
          - Grass Land 48,22:
            - Owner: Japan
            - Resource: Cattle
            - Improvement: Pasture
            - Route: Railroad
          - Plains Land 47,21:
            - Owner: Japan
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 48,20:
            - Owner: Japan
            - CityID: 3937
            - Population: 27
            - City: Nagasaki
            - Religion: Islam
            - Route: Railroad
          - Coast 48,19:
            - Owner: Japan
        
        ### 84
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 37%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18270
        - Player: 1: Japan
        - Plots:
          - Coast 49,11:
            - Owner: Japan
          - Coast 50,12:
            - Owner: Japan
          - Coast 49,13:
            - Owner: Japan
          - Plains Hills 49,14:
            - Owner: Japan
            - CityID: 12516
            - Population: 18
            - City: Sapporo
            - Resource: Iron
            - Religion: Islam
            - Route: Railroad
        
        ### 85
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 16084
        - Player: 1: Japan
        
        ### 86
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18185
        - Player: 1: Japan
        
        ### 87
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Submarine
          - ID: 19019
        - Player: 1: Japan
        - Ocean 76,31:
          - Owner: Japan
        
        ### 88
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16314
        - Player: 1: Japan
        - Plots:
          - Tundra Land 53,3:
            - Owner: Japan
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 54,3:
            - Owner: Japan
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
          - Snow Land 55,2:
            - Owner: Japan
            - Resource: Oil
            - Improvement: Oil Well
        
        ### 89
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 19340
        - Player: 1: Japan
        - Plots:
          - Grass Hills 47,36:
            - Owner: Japan
            - Improvement: Village
            - Route: Railroad
          - Plains Land 46,34:
            - Owner: Japan
            - Improvement: Farm
            - Route: Railroad
          - Desert Hills 46,33:
            - Owner: Japan
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 47,32:
            - Owner: Japan
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
        
        ### 90
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4304
        - Player: 1: Japan
        - Plots:
          - Coast 56,6:
            - Owner: Japan
        
        ### 91
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 5191
        - Player: 1: Japan
        
        ### 92
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Cargo Ship
          - ID: 19419
        - Player: 1: Japan
        - Desert Land 48,20:
          - Owner: Japan
          - CityID: 3937
          - Population: 27
          - City: Nagasaki
          - Religion: Islam
          - Route: Railroad
        
        ### 93
        - Type: UnitCreated
        - UnitType: Cargo Ship
        - Player: 1: Japan
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 19419
        - Desert Land 48,20:
          - Owner: Japan
          - CityID: 3937
          - Population: 27
          - City: Nagasaki
          - Religion: Islam
          - Route: Railroad
        
        ### 94
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 19419
        - Player: 1: Japan
        - Coast 48,19:
          - Owner: Japan
        
        ### 95
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16375
        - Player: 1: Japan
        - Plots:
          - Plains Land 45,10:
            - Owner: Japan
            - CityID: 11608
            - Population: 18
            - City: Matsuyama
            - Resource: Wheat
            - Religion: Islam
            - Route: Railroad
          - Plains Hills 45,9:
            - Owner: Japan
            - Improvement: Fort
            - Route: Railroad
        
        ### 96
        - Type: EspionageState
        - SpyIndex: 2
        - SpyState: 3
        - City:
          - Owner: Songhai
          - CityID: 9242
          - Population: 29
          - City: Shimonoseki
          - Terrain: Desert
          - Religion: Islam
          - Route: Railroad
          - Plot: Land
          - X: 40
          - Y: 16
        - SpyOwner: 3: The Zulus
        
        ### 97
        - Type: EspionageState
        - SpyIndex: 4
        - SpyState: 3
        - City:
          - Owner: Songhai
          - CityID: 7795
          - Population: 29
          - City: Vilnius
          - Terrain: Tundra
          - Resource: Glass
          - Religion: Islam
          - Route: Railroad
          - Plot: Hills
          - X: 29
          - Y: 48
        - SpyOwner: 3: The Zulus
        
        ### 98
        - Type: EspionageState
        - SpyIndex: 7
        - SpyState: 3
        - City:
          - Owner: Songhai
          - CityID: 16272
          - Population: 32
          - IsRiver: true
          - City: Rio de Janeiro
          - Terrain: Grass
          - Religion: Islam
          - Route: Railroad
          - Plot: Land
          - X: 41
          - Y: 22
        - SpyOwner: 3: The Zulus
        
        ### 99
        - Type: EspionageState
        - SpyIndex: 9
        - SpyState: 3
        - City:
          - Owner: Songhai
          - CityID: 11977
          - Population: 27
          - City: The Hague
          - Terrain: Tundra
          - Resource: Iron
          - Religion: Islam
          - Route: Railroad
          - Plot: Hills
          - X: 11
          - Y: 47
        - SpyOwner: 3: The Zulus
        
        ### 100
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 26
        - OldImprovement: Farm
        - NewImprovement: Farm
        - Plains Land 16,41:
          - Owner: City-State Dublin
          - Improvement: Farm
        
        ### 101
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 18339
        - Player: 3: The Zulus
        - Plains Land 15,41:
          - Owner: City-State Dublin
          - Improvement: Farm
        
        ### 102
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 38%
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 15770
        - Player: 3: The Zulus
        - Plots:
          - Plains Land 15,41:
            - Owner: City-State Dublin
            - Improvement: Farm
          - Plains Hills 15,42:
            - Owner: The Zulus
            - Improvement: Mine
        
        ### 103
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 62%
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 18153
        - Player: 3: The Zulus
        - Tundra Hills 15,45:
          - Owner: City-State Dublin
          - Improvement: Mine
        
        ### 104
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 18146
        - Player: 3: The Zulus
        - Plots:
          - Plains Land 16,42:
            - Owner: City-State Dublin
            - Resource: Incense
            - Improvement: Embassy
            - Route: Railroad
          - Tundra Hills 15,43:
            - Owner: City-State Dublin
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Tundra Hills 15,44:
            - Owner: City-State Dublin
            - Resource: Iron
            - Improvement: Mine
        
        ### 105
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 90%
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 18340
        - Player: 3: The Zulus
        - Tundra Hills 15,43:
          - Owner: City-State Dublin
          - Resource: Sheep
          - Improvement: Pasture
          - Route: Railroad
        
        ### 106
        - Type: UnitMoved
        - Unit:
          - Level: 8
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 18133
        - Player: 3: The Zulus
        - Plots:
          - Plains Land 16,42:
            - Owner: City-State Dublin
            - Resource: Incense
            - Improvement: Embassy
            - Route: Railroad
          - Tundra Hills 15,43:
            - Owner: City-State Dublin
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
        
        ### 107
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 90%
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 18340
        - Player: 3: The Zulus
        - Plains Land 16,42:
          - Owner: City-State Dublin
          - Resource: Incense
          - Improvement: Embassy
          - Route: Railroad
        
        ### 108
        - Type: CombatResult
        - Tundra Land 16,44:
          - Owner: City-State Dublin
          - CityID: 1069
          - Population: 19
          - City: Dublin
          - Route: Railroad
        - Attacker:
          - RemainingHP: 9
          - Damage: 9
        - Defender:
          - RemainingHP: 70
          - Damage: 247
          - Player: 26
        
        ### 109
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 90%
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 18340
        - Player: 3: The Zulus
        - Tundra Hills 17,42:
          - Owner: City-State Dublin
          - Improvement: Mine
        
        ### 110
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 18339
        - Player: 3: The Zulus
        - Plains Land 16,42:
          - Owner: City-State Dublin
          - Resource: Incense
          - Improvement: Embassy
          - Route: Railroad
        
        ### 111
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 12%
          - AI: Defense
          - Unit: Mechanized Infantry
          - ID: 18449
        - Player: 3: The Zulus
        - Coast 17,45:
          - Owner: City-State Dublin
        
        ### 112
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Submarine
          - ID: 17671
        - Player: 3: The Zulus
        - Plots:
          - Coast 17,40:
            - Owner: Korea
          - Ocean 18,40:
            - Owner: Korea
          - Coast 22,40:
            - Owner: Songhai
        
        ### 113
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 9%
          - AI: AssaultSea
          - Unit: Battleship
          - ID: 18910
        - Player: 3: The Zulus
        - Coast 15,40:
          - Owner: The Zulus
        
        ### 114
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Prophet
          - Unit: Great Prophet
          - ID: 18955
        - Player: 3: The Zulus
        - Plots:
          - Grass Hills 47,24:
            - Owner: Japan
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 46,23:
            - Owner: Japan
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 47,22:
            - Owner: Japan
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 47,21:
            - Owner: Japan
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 48,20:
            - Owner: Japan
            - CityID: 3937
            - Population: 27
            - City: Nagasaki
            - Religion: Islam
            - Route: Railroad
          - Desert Land 47,19:
            - Owner: Japan
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
        
        ### 115
        - Type: PlayerDoneTurn
        - NextPlayer: 4: Songhai
        - Player: 3: The Zulus
        
        ### 116
        - Type: CityInvestedBuilding
        - BuildingClass: Military Base
        - Invested: true
        - City:
          - Population: 25
          - Name: Kyoto
          - Health: -28%
          - ID: 19051
        - Player: 4: Songhai
        
        ### 117
        - Type: CityConstructed
        - City:
          - Name: Gao
          - Population: 52
          - ID: 1061
        - Owner: 4: Songhai
        - Building: Foreign Bureau
        
        ### 118
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Great Diplomat
          - ID: 19438
        - Player: 4: Songhai
        - Desert Hills 34,38:
          - Owner: Songhai
          - CityID: 1061
          - Population: 52
          - IsRiver: true
          - City: Gao
          - Religion: Islam
          - Route: Railroad
        
        ### 119
        - Type: UnitCreated
        - UnitType: Great Diplomat
        - Player: 4: Songhai
        - Unit:
          - Level: 1
          - AI: Diplomat
          - Unit: Great Diplomat
          - ID: 19438
        - Desert Hills 34,38:
          - Owner: Songhai
          - CityID: 1061
          - Population: 52
          - IsRiver: true
          - City: Gao
          - Religion: Islam
          - Route: Railroad
        
        ### 120
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Ambassador
          - ID: 19439
        - Player: 4: Songhai
        - Desert Land 39,43:
          - Owner: Songhai
          - CityID: 1543
          - Population: 37
          - IsRiver: true
          - City: Jenne
          - Religion: Islam
          - Route: Railroad
        
        ### 121
        - Type: UnitCreated
        - UnitType: Ambassador
        - Player: 4: Songhai
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 19439
        - Desert Land 39,43:
          - Owner: Songhai
          - CityID: 1543
          - Population: 37
          - IsRiver: true
          - City: Jenne
          - Religion: Islam
          - Route: Railroad
        
        ### 122
        - Type: CityTrained
        - Player: 4: Songhai
        - City:
          - Name: Jenne
          - Population: 37
          - ID: 1543
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 19439
        
        ### 123
        - Type: TileOwnershipChanged
        - NewOwner: 4: Songhai
        - Ocean 28,28:
          - Owner: Songhai
        
        ### 124
        - Type: CityBoughtPlot
        - WithFaithCulture: true
        - Player: 4: Songhai
        - City:
          - Name: Tondibi
          - Population: 40
          - ID: 2157
        - Ocean 28,28:
          - Owner: Songhai
        
        ### 125
        - Type: CityConstructed
        - City:
          - Name: Kumbi Saleh
          - Population: 35
          - ID: 2568
        - Owner: 4: Songhai
        - Building: Strategic Defense System
        
        ### 126
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Heavy Bomber
          - ID: 19440
        - Player: 4: Songhai
        - Grass Land 39,32:
          - Owner: Songhai
          - CityID: 2951
          - Population: 34
          - City: Kukia
          - Resource: Coal
          - Religion: Islam
          - Route: Railroad
        
        ### 127
        - Type: UnitCreated
        - UnitType: Heavy Bomber
        - Player: 4: Songhai
        - Unit:
          - Level: 1
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 19440
        - Grass Land 39,32:
          - Owner: Songhai
          - CityID: 2951
          - Population: 34
          - City: Kukia
          - Resource: Coal
          - Religion: Islam
          - Route: Railroad
        
        ### 128
        - Type: CityTrained
        - Player: 4: Songhai
        - City:
          - Name: Kukia
          - Population: 34
          - ID: 2951
        - Unit:
          - Level: 1
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 19440
        
        ### 129
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Fighter
          - ID: 19441
        - Player: 4: Songhai
        - Plains Land 38,27:
          - Owner: Songhai
          - CityID: 5558
          - Population: 35
          - IsRiver: true
          - City: Sao Paulo
          - Religion: Islam
          - Route: Railroad
        
        ### 130
        - Type: UnitCreated
        - UnitType: Fighter
        - Player: 4: Songhai
        - Unit:
          - Level: 1
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 19441
        - Plains Land 38,27:
          - Owner: Songhai
          - CityID: 5558
          - Population: 35
          - IsRiver: true
          - City: Sao Paulo
          - Religion: Islam
          - Route: Railroad
        
        ### 131
        - Type: CityTrained
        - Player: 4: Songhai
        - City:
          - Name: Sao Paulo
          - Population: 35
          - ID: 5558
        - Unit:
          - Level: 1
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 19441
        
        ### 132
        - Type: CityConstructed
        - City:
          - Name: Shimonoseki
          - Population: 29
          - ID: 9242
        - Owner: 4: Songhai
        - Building: Strategic Defense System
        
        ### 133
        - Type: CityConstructed
        - City:
          - Name: Rio de Janeiro
          - Population: 32
          - ID: 16272
        - Owner: 4: Songhai
        - Building: Strategic Defense System
        
        ### 134
        - Type: CityEndsWLTKD
        - Unused: 0
        - Owner: 4: Songhai
        - Tundra Land 44,45:
          - Owner: Songhai
          - CityID: 17745
          - Population: 20
          - City: Tokyo
          - Resource: Aluminum
          - Religion: Islam
          - Route: Railroad
        
        ### 135
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17986
        - Player: 4: Songhai
        - Plots:
          - Plains Land 40,43:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 41,43:
            - Owner: Songhai
            - Resource: Stone
            - Improvement: Citadel
            - Route: Railroad
          - Tundra Hills 42,43:
            - Owner: Songhai
            - Resource: Copper
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 43,43:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Desert Land 44,44:
            - Owner: Songhai
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Tundra Land 44,45:
            - Owner: Songhai
            - CityID: 17745
            - Population: 20
            - City: Tokyo
            - Resource: Aluminum
            - Religion: Islam
            - Route: Railroad
        
        ### 136
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19269
        - Player: 4: Songhai
        - Plots:
          - Desert Land 44,44:
            - Owner: Songhai
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Plains Land 43,43:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Tundra Hills 42,43:
            - Owner: Songhai
            - Resource: Copper
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 41,43:
            - Owner: Songhai
            - Resource: Stone
            - Improvement: Citadel
            - Route: Railroad
          - Plains Land 41,42:
            - Owner: Songhai
            - Improvement: Farm
            - Route: Railroad
        
        ### 137
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17931
        - Player: 4: Songhai
        - Plots:
          - Desert Land 44,44:
            - Owner: Songhai
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Plains Land 43,43:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Tundra Hills 42,43:
            - Owner: Songhai
            - Resource: Copper
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 41,43:
            - Owner: Songhai
            - Resource: Stone
            - Improvement: Citadel
            - Route: Railroad
          - Plains Land 41,42:
            - Owner: Songhai
            - Improvement: Farm
            - Route: Railroad
        
        ### 138
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18296
        - Player: 4: Songhai
        - Plots:
          - Grass Land 37,38:
            - Owner: Songhai
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 36,38:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 35,38:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
          - Desert Hills 34,38:
            - Owner: Songhai
            - CityID: 1061
            - Population: 52
            - IsRiver: true
            - City: Gao
            - Religion: Islam
            - Route: Railroad
        
        ### 139
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17987
        - Player: 4: Songhai
        - Plots:
          - Plains Land 40,43:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 39,43:
            - Owner: Songhai
            - CityID: 1543
            - Population: 37
            - IsRiver: true
            - City: Jenne
            - Religion: Islam
            - Route: Railroad
          - Plains Land 39,42:
            - Owner: Songhai
            - Resource: Wheat
            - Improvement: Town
            - Route: Railroad
          - Desert Hills 38,41:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 38,40:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
        
        ### 140
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18926
        - Player: 4: Songhai
        - Plots:
          - Desert Hills 38,41:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 39,42:
            - Owner: Songhai
            - Resource: Wheat
            - Improvement: Town
            - Route: Railroad
          - Desert Land 39,43:
            - Owner: Songhai
            - CityID: 1543
            - Population: 37
            - IsRiver: true
            - City: Jenne
            - Religion: Islam
            - Route: Railroad
          - Tundra Hills 40,44:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
        
        ### 141
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18458
        - Player: 4: Songhai
        - Plots:
          - Plains Land 33,37:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 33,36:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Hills 32,35:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 32,34:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Plains Land 31,34:
            - Owner: Songhai
            - Resource: Wheat
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 30,34:
            - Owner: Songhai
            - CityID: 1867
            - Population: 36
            - IsRiver: true
            - City: Taghaza
            - Religion: Islam
            - Route: Railroad
        
        ### 142
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18969
        - Player: 4: Songhai
        - Plots:
          - Plains Land 39,36:
            - Owner: Songhai
            - Improvement: Town
            - Route: Railroad
          - Tundra Hills 39,35:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Tundra Hills 39,34:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
        
        ### 143
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19014
        - Player: 4: Songhai
        - Plots:
          - Plains Land 35,38:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
          - Grass Land 36,38:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
          - Grass Land 37,38:
            - Owner: Songhai
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 37,39:
            - Owner: Songhai
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 38,40:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Desert Hills 38,41:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
        
        ### 144
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18243
        - Player: 4: Songhai
        - Plots:
          - Tundra Land 29,42:
            - Owner: Songhai
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Tundra Hills 28,41:
            - Owner: Songhai
            - Resource: Lapis Lazuli
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 28,40:
            - Owner: Songhai
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 28,39:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Desert Hills 29,38:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
        
        ### 145
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 18244
        - Player: 4: Songhai
        - Plots:
          - Coast 42,10:
            - Owner: Japan
            - Resource: Fish
          - Ocean 42,9:
            - Owner: Japan
        
        ### 146
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19015
        - Player: 4: Songhai
        - Plots:
          - Plains Land 35,38:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
          - Grass Land 36,38:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
          - Grass Land 37,38:
            - Owner: Songhai
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 38,38:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 38,37:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
        
        ### 147
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19016
        - Player: 4: Songhai
        - Plots:
          - Desert Land 32,29:
            - Owner: Songhai
            - Resource: Aluminum
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 32,30:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 31,31:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 31,32:
            - Owner: Songhai
            - Route: Railroad
            - Feature: Oasis
          - Plains Hills 31,33:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
        
        ### 148
        - Type: PlayerDoTurn
        - Player: 4: Songhai
        
        ### 149
        - Type: UnitPromoted
        - Unit:
          - Level: 5
          - Health: 31%
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18765
        - Player: 4: Songhai
        - Promotion: Infiltrators
        
        ### 150
        - Type: UnitPromoted
        - Unit:
          - Level: 5
          - Health: 81%
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 19209
        - Player: 4: Songhai
        - Promotion: Air Supremacy II
        
        ### 151
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 19440
        - Player: 4: Songhai
        - Promotions:
          - Air Targeting I
          - Air Targeting II
          - Air Targeting III
        
        ### 152
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 19441
        - Player: 4: Songhai
        - Promotions:
          - Ace Pilot II
          - Ace Pilot III
          - Ace Pilot IV
        
        ### 153
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: Ranged
          - Unit: Bazooka
          - ID: 17929
        - Player: 4: Songhai
        - Plains Land 40,21:
          - Owner: Songhai
          - IsRiver: true
          - Improvement: Village
          - Route: Railroad
        
        ### 154
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 31%
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18765
        - Player: 4: Songhai
        - Plots:
          - Plains Land 43,16:
            - Owner: Songhai
            - Resource: Wine
            - Improvement: Plantation
            - Route: Railroad
          - Desert Hills 42,17:
            - Owner: Songhai
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
          - Desert Land 42,18:
            - Owner: Songhai
            - Improvement: Farm
            - Route: Railroad
          - Desert Hills 41,19:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 41,20:
            - Owner: Songhai
            - Resource: Wine
            - Improvement: Academy
            - Route: Railroad
          - Plains Land 40,21:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 41,22:
            - Owner: Songhai
            - CityID: 16272
            - Population: 32
            - IsRiver: true
            - City: Rio de Janeiro
            - Religion: Islam
            - Route: Railroad
        
        ### 155
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19267
        - Player: 4: Songhai
        - Coast 34,22:
          - Owner: Songhai
        
        ### 156
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19211
        - Player: 4: Songhai
        - Ocean 33,23:
          - Owner: Songhai
        
        ### 157
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Submarine
          - ID: 19048
        - Player: 4: Songhai
        - Ocean 33,23:
          - Owner: Songhai
        
        ### 158
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19211
        - Player: 4: Songhai
        - Coast 34,23:
          - Owner: Songhai
        
        ### 159
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19314
        - Player: 4: Songhai
        - Plots:
          - Ocean 25,33:
            - Owner: Korea
          - Ocean 25,34:
            - Owner: Korea
          - Ocean 24,35:
            - Owner: Korea
          - Coast 24,36:
            - Owner: Korea
          - Ocean 23,37:
            - Owner: Korea
          - Ocean 23,38:
            - Owner: Korea
        
        ### 160
        - Type: CombatResult
        - Tundra Hills 51,6:
          - Owner: Songhai
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 27
          - Damage: 77
          - Unit:
            - Level: 4
            - Health: 58%
            - AI: Defense
            - Unit: Rifleman
            - ID: 18542
          - Player: 1: Japan
        
        ### 161
        - Type: CombatResult
        - Grass Land 46,36:
          - Owner: Japan
          - IsRiver: true
          - Improvement: Academy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 21
          - Damage: 65
          - Unit:
            - Level: 4
            - Health: 64%
            - AI: Defense
            - Unit: Infantry
            - ID: 18901
          - Player: 1: Japan
        
        ### 162
        - Type: CombatResult
        - Coast 22,40:
          - Owner: Songhai
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 35
          - Damage: 35
          - Unit:
            - Level: 4
            - AI: AssaultSea
            - Unit: Submarine
            - ID: 17671
          - Player: 3: The Zulus
        
        ### 163
        - Type: CombatResult
        - Tundra Hills 15,45:
          - Owner: City-State Dublin
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 37
          - Damage: 94
          - Player: 3: The Zulus
          - Unit:
            - Level: 5
            - Health: 62%
            - AI: Defense
            - Unit: Mechanized Infantry
            - ID: 18153
        
        ### 164
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18712
        - Player: 4: Songhai
        - Plots:
          - Grass Land 45,38:
            - Owner: Songhai
            - Resource: Dyes
            - Improvement: Plantation
            - Route: Railroad
          - Plains Hills 44,38:
            - Owner: Songhai
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
        
        ### 165
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18703
        - Player: 4: Songhai
        - Plains Hills 44,39:
          - Owner: Songhai
          - Resource: Deer
          - Improvement: Camp
          - Route: Railroad
          - Feature: Forest
        
        ### 166
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18712
        - Player: 4: Songhai
        - Grass Land 45,38:
          - Owner: Songhai
          - Resource: Dyes
          - Improvement: Plantation
          - Route: Railroad
        
        ### 167
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18587
        - Player: 4: Songhai
        - Plots:
          - Grass Land 45,38:
            - Owner: Songhai
            - Resource: Dyes
            - Improvement: Plantation
            - Route: Railroad
          - Plains Hills 44,38:
            - Owner: Songhai
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
        
        ### 168
        - Type: CombatResult
        - Grass Land 46,36:
          - Owner: Japan
          - IsRiver: true
          - Improvement: Academy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 30
          - Damage: 95
          - Player: 1: Japan
          - Unit:
            - Level: 4
            - Health: 48%
            - AI: Defense
            - Unit: Infantry
            - ID: 18901
        
        ### 169
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18695
        - Player: 4: Songhai
        - Plots:
          - Plains Land 45,40:
            - Owner: Songhai
            - CityID: 19051
            - Population: 25
            - IsRiver: true
            - City: Kyoto
            - Religion: Islam
            - Route: Railroad
          - Grass Land 45,39:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
        
        ### 170
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18712
        - Player: 4: Songhai
        - Plains Hills 44,38:
          - Owner: Songhai
          - Improvement: Lumber Mill
          - Route: Railroad
          - Feature: Forest
        
        ### 171
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18587
        - Player: 4: Songhai
        - Plots:
          - Grass Land 45,38:
            - Owner: Songhai
            - Resource: Dyes
            - Improvement: Plantation
            - Route: Railroad
          - Plains Hills 44,38:
            - Owner: Songhai
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
        
        ### 172
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18712
        - Player: 4: Songhai
        - Grass Land 45,38:
          - Owner: Songhai
          - Resource: Dyes
          - Improvement: Plantation
          - Route: Railroad
        
        ### 173
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18877
        - Player: 4: Songhai
        - Grass Land 41,33:
          - Owner: Songhai
          - IsRiver: true
          - Resource: Bananas
          - Improvement: Plantation
          - Route: Railroad
        
        ### 174
        - Type: UnitMoved
        - Unit:
          - Level: 7
          - Health: 68%
          - AI: CityBombard
          - Unit: Artillery
          - ID: 15779
        - Player: 4: Songhai
        - Plots:
          - Grass Hills 41,32:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 42,32:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
        
        ### 175
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18712
        - Player: 4: Songhai
        - Plains Hills 44,38:
          - Owner: Songhai
          - Improvement: Lumber Mill
          - Route: Railroad
          - Feature: Forest
        
        ### 176
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18587
        - Player: 4: Songhai
        - Grass Land 45,38:
          - Owner: Songhai
          - Resource: Dyes
          - Improvement: Plantation
          - Route: Railroad
        
        ### 177
        - Type: CombatResult
        - Grass Land 46,36:
          - Owner: Japan
          - IsRiver: true
          - Improvement: Academy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 28
          - Damage: 123
          - Player: 1: Japan
          - Unit:
            - Level: 4
            - Health: 24%
            - AI: Defense
            - Unit: Infantry
            - ID: 18901
        
        ### 178
        - Type: CombatResult
        - Tundra Hills 15,45:
          - Owner: City-State Dublin
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 29
          - Damage: 123
          - Player: 3: The Zulus
          - Unit:
            - Level: 5
            - Health: 37%
            - AI: Defense
            - Unit: Mechanized Infantry
            - ID: 18153
        
        ### 179
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18707
        - Player: 4: Songhai
        - Tundra Land 15,48:
          - Owner: Songhai
          - Improvement: Fort
        
        ### 180
        - Type: UnitMoved
        - Unit:
          - Level: 7
          - AI: Ranged
          - Unit: Bazooka
          - ID: 19055
        - Player: 4: Songhai
        - Snow Land 15,49:
          - Owner: Songhai
          - Resource: Stone
          - Improvement: Quarry
        
        ### 181
        - Type: CombatResult
        - Tundra Hills 15,44:
          - Owner: City-State Dublin
          - Resource: Iron
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 36
          - Damage: 36
          - Player: 3: The Zulus
          - Unit:
            - Level: 6
            - AI: Defense
            - Unit: Mechanized Infantry
            - ID: 18146
        
        ### 182
        - Type: CombatResult
        - Tundra Hills 15,45:
          - Owner: City-State Dublin
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 27
          - Damage: 150
          - Player: 3: The Zulus
          - Unit:
            - Level: 5
            - Health: 18%
            - AI: Defense
            - Unit: Mechanized Infantry
            - ID: 18153
        
        ### 183
        - Type: UnitKilledInCombat
        - KilledPlayer: 3: The Zulus
        - KillerPlayer: 4: Songhai
        - KilledUnit: Mechanized Infantry
        
        ### 184
        - Type: CombatResult
        - Tundra Hills 15,44:
          - Owner: City-State Dublin
          - Resource: Iron
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 33
          - Damage: 69
          - Player: 3: The Zulus
          - Unit:
            - Level: 6
            - Health: 76%
            - AI: Defense
            - Unit: Mechanized Infantry
            - ID: 18146
        
        ### 185
        - Type: CombatResult
        - Desert Land 45,20:
          - Owner: Japan
          - Improvement: Citadel
        - Attacker:
          - RemainingHP: 27
          - Damage: 27
        - Defender:
          - RemainingHP: 29
          - Damage: 29
          - Player: 1: Japan
          - Unit:
            - Level: 5
            - AI: DefenseAir
            - Unit: Triplane
            - ID: 19118
        
        ### 186
        - Type: CombatResult
        - Desert Land 45,20:
          - Owner: Japan
          - Improvement: Citadel
        - Attacker:
          - RemainingHP: 29
          - Damage: 29
        - Defender:
          - RemainingHP: 23
          - Damage: 23
          - Player: 1: Japan
          - Unit:
            - Level: 4
            - AI: DefenseAir
            - Unit: Triplane
            - ID: 19037
        
        ### 187
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18699
        - Player: 4: Songhai
        - Plots:
          - Plains Land 41,16:
            - Owner: Songhai
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 42,16:
            - Owner: Songhai
            - Improvement: Farm
            - Route: Railroad
          - Desert Hills 42,17:
            - Owner: Songhai
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
          - Desert Land 43,18:
            - Owner: Songhai
            - Route: Railroad
        
        ### 188
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: Ranged
          - Unit: Bazooka
          - ID: 17929
        - Player: 4: Songhai
        - Plots:
          - Plains Land 41,20:
            - Owner: Songhai
            - Resource: Wine
            - Improvement: Academy
            - Route: Railroad
          - Desert Hills 41,19:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 42,18:
            - Owner: Songhai
            - Improvement: Farm
            - Route: Railroad
          - Desert Hills 42,17:
            - Owner: Songhai
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 43,16:
            - Owner: Songhai
            - Resource: Wine
            - Improvement: Plantation
            - Route: Railroad
          - Desert Land 43,18:
            - Owner: Songhai
            - Route: Railroad
        
        ### 189
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18699
        - Player: 4: Songhai
        - Plots:
          - Desert Hills 42,17:
            - Owner: Songhai
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 43,16:
            - Owner: Songhai
            - Resource: Wine
            - Improvement: Plantation
            - Route: Railroad
          - Desert Land 43,18:
            - Owner: Songhai
            - Route: Railroad
        
        ### 190
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: Ranged
          - Unit: Bazooka
          - ID: 17929
        - Player: 4: Songhai
        - Plots:
          - Desert Hills 42,17:
            - Owner: Songhai
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 43,16:
            - Owner: Songhai
            - Resource: Wine
            - Improvement: Plantation
            - Route: Railroad
          - Desert Land 43,18:
            - Owner: Songhai
            - Route: Railroad
        
        ### 191
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18699
        - Player: 4: Songhai
        - Plots:
          - Desert Hills 42,17:
            - Owner: Songhai
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 43,16:
            - Owner: Songhai
            - Resource: Wine
            - Improvement: Plantation
            - Route: Railroad
        
        ### 192
        - Type: CombatResult
        - Mountain Mountain 43,28:
          - Owner: Japan
          - Route: Railroad
        - Attacker:
          - RemainingHP: 32
          - Damage: 32
        - Defender:
          - RemainingHP: 24
          - Damage: 24
          - Player: 1: Japan
          - Unit:
            - Level: 7
            - AI: DefenseAir
            - Unit: Triplane
            - ID: 17611
        
        ### 193
        - Type: CombatResult
        - Mountain Mountain 43,28:
          - Owner: Japan
          - Route: Railroad
        - Attacker:
          - RemainingHP: 35
          - Damage: 35
        - Defender:
          - RemainingHP: 32
          - Damage: 52
          - Player: 1: Japan
          - Unit:
            - Level: 5
            - Health: 80%
            - AI: DefenseAir
            - Unit: Triplane
            - ID: 18062
        
        ### 194
        - Type: CombatResult
        - Mountain Mountain 43,28:
          - Owner: Japan
          - Route: Railroad
        - Attacker:
          - RemainingHP: 10
          - Damage: 10
        - Defender:
          - RemainingHP: 33
          - Damage: 69
          - Player: 1: Japan
          - Unit:
            - Level: 4
            - Health: 71%
            - AI: Defense
            - Unit: Infantry
            - ID: 18900
        
        ### 195
        - Type: CombatResult
        - Mountain Mountain 43,28:
          - Owner: Japan
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Player: 1: Japan
          - Unit:
            - Level: 4
            - Health: 44%
            - AI: Defense
            - Unit: Infantry
            - ID: 18900
        - Interceptor:
          - Damage: 97
          - Unit:
            - Level: 5
            - Health: 48%
            - AI: DefenseAir
            - Unit: Triplane
            - ID: 18062
          - Player: 4: Songhai
        
        ### 196
        - Type: UnitKilledInCombat
        - KilledPlayer: 4: Songhai
        - KillerPlayer: 1: Japan
        - KilledUnit: Heavy Bomber
        
        ### 197
        - Type: CombatResult
        - Mountain Mountain 43,28:
          - Owner: Japan
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 32
          - Damage: 76
          - Player: 1: Japan
          - Unit:
            - Level: 4
            - Health: 64%
            - AI: Defense
            - Unit: Infantry
            - ID: 18900
        
        ### 198
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18509
        - Player: 4: Songhai
        - Plots:
          - Grass Land 37,25:
            - Owner: Songhai
            - Resource: Rice
            - Improvement: Town
            - Route: Railroad
          - Plains Land 38,26:
            - Owner: Songhai
            - Route: Railroad
            - Feature: El Dorado
          - Plains Land 38,27:
            - Owner: Songhai
            - CityID: 5558
            - Population: 35
            - IsRiver: true
            - City: Sao Paulo
            - Religion: Islam
            - Route: Railroad
          - Plains Land 39,27:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Grass Hills 40,28:
            - Owner: Songhai
            - Resource: Brazilwood
            - Improvement: Brazilwood Camp
            - Feature: Jungle
        
        ### 199
        - Type: UnitMoved
        - Unit:
          - Level: 7
          - Health: 68%
          - AI: CityBombard
          - Unit: Artillery
          - ID: 15779
        - Player: 4: Songhai
        - Plots:
          - Plains Land 41,31:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Hills 40,31:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Holy Site
            - Route: Railroad
          - Plains Hills 40,30:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 40,29:
            - Owner: Songhai
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Grass Land 41,28:
            - Owner: Songhai
            - Resource: Rice
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 40,27:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Land 40,26:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Rice
            - Improvement: Farm
        
        ### 200
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18877
        - Player: 4: Songhai
        - Grass Hills 42,32:
          - Owner: Songhai
          - IsRiver: true
          - Improvement: Mine
          - Route: Railroad
        
        ### 201
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 17299
        - Player: 4: Songhai
        - Plots:
          - Grass Hills 42,32:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 41,31:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Hills 40,31:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Holy Site
            - Route: Railroad
          - Plains Hills 40,30:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 40,29:
            - Owner: Songhai
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Grass Land 41,28:
            - Owner: Songhai
            - Resource: Rice
            - Improvement: Farm
            - Route: Railroad
        
        ### 202
        - Type: CombatResult
        - Grass Land 44,26:
          - Owner: Japan
          - CityID: 3641
          - Population: 27
          - IsRiver: true
          - City: Izumo
          - Religion: Islam
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 34
          - Damage: 34
          - Player: 1: Japan
        
        ### 203
        - Type: CombatResult
        - Mountain Mountain 43,28:
          - Owner: Japan
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 26
          - Damage: 102
          - Player: 1: Japan
          - Unit:
            - Level: 4
            - Health: 39%
            - AI: Defense
            - Unit: Infantry
            - ID: 18900
        
        ### 204
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18701
        - Player: 4: Songhai
        - Plots:
          - Plains Land 39,27:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Grass Land 40,27:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Land 41,28:
            - Owner: Songhai
            - Resource: Rice
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 40,29:
            - Owner: Songhai
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Plains Hills 40,30:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
        
        ### 205
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19320
        - Player: 4: Songhai
        - Plots:
          - Ocean 26,32:
            - Owner: Korea
          - Ocean 27,32:
            - Owner: Songhai
          - Ocean 27,33:
            - Owner: Songhai
        
        ### 206
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Bazooka
          - ID: 19143
        - Player: 4: Songhai
        - Plots:
          - Plains Land 43,41:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
          - Plains Land 42,41:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Citadel
          - Plains Land 42,40:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
          - Plains Hills 41,39:
            - Owner: Songhai
            - Route: Road
        
        ### 207
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18819
        - Player: 4: Songhai
        - Plots:
          - Plains Land 45,41:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Farm
          - Desert Land 44,41:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
        
        ### 208
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 19101
        - Player: 4: Songhai
        - Plots:
          - Plains Land 43,43:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Tundra Hills 42,43:
            - Owner: Songhai
            - Resource: Copper
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 41,43:
            - Owner: Songhai
            - Resource: Stone
            - Improvement: Citadel
            - Route: Railroad
          - Plains Land 41,42:
            - Owner: Songhai
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 40,41:
            - Owner: Songhai
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 40,40:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 39,39:
            - Owner: Songhai
            - Resource: Copper
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 39,38:
            - Owner: Songhai
            - CityID: 1276
            - Population: 35
            - City: Tombouctu
            - Religion: Islam
            - Route: Railroad
          - Plains Hills 39,37:
            - Owner: Songhai
            - Resource: Copper
            - Improvement: Mine
            - Route: Railroad
          - Mountain Mountain 40,37:
            - Owner: Songhai
            - Route: Railroad
          - Plains Hills 41,37:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 42,37:
            - Owner: Songhai
            - Resource: Uranium
            - Improvement: Fort
        
        ### 209
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: Ranged
          - Unit: Bazooka
          - ID: 19212
        - Player: 4: Songhai
        - Plots:
          - Plains Land 45,42:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Farm
          - Plains Land 45,41:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Farm
        
        ### 210
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: Ranged
          - Unit: Bazooka
          - ID: 19100
        - Player: 4: Songhai
        - Plots:
          - Tundra Land 43,44:
            - Owner: Songhai
            - Resource: Uranium
            - Improvement: Quarry
          - Tundra Hills 42,43:
            - Owner: Songhai
            - Resource: Copper
            - Improvement: Mine
            - Route: Railroad
        
        ### 211
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: AssaultSea
          - Unit: Submarine
          - ID: 18291
        - Player: 4: Songhai
        - Plots:
          - Coast 25,38:
            - Owner: Songhai
          - Coast 25,39:
            - Owner: Songhai
          - Ocean 25,40:
            - Owner: Songhai
          - Ocean 25,41:
            - Owner: Songhai
          - Ocean 26,42:
            - Owner: Songhai
        
        ### 212
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 13348
        - Player: 4: Songhai
        - Plains Land 45,40:
          - Owner: Songhai
          - CityID: 19051
          - Population: 25
          - IsRiver: true
          - City: Kyoto
          - Religion: Islam
          - Route: Railroad
        
        ### 213
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: Ranged
          - Unit: Bazooka
          - ID: 17929
        - Player: 4: Songhai
        - Plots:
          - Desert Land 42,18:
            - Owner: Songhai
            - Improvement: Farm
            - Route: Railroad
          - Desert Hills 41,19:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 41,20:
            - Owner: Songhai
            - Resource: Wine
            - Improvement: Academy
            - Route: Railroad
          - Plains Hills 40,20:
            - Owner: Songhai
            - Improvement: Town
            - Route: Railroad
          - Desert Land 39,20:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Desert Land 38,20:
            - Owner: Songhai
            - Resource: Aluminum
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 37,20:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Plains Land 36,21:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 35,21:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
          - Plains Land 35,22:
            - Owner: Songhai
            - CityID: 4728
            - Population: 35
            - City: Walata
            - Religion: Islam
            - Route: Railroad
          - Coast 34,22:
            - Owner: Songhai
        
        ### 214
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18699
        - Player: 4: Songhai
        - Plots:
          - Plains Land 42,16:
            - Owner: Songhai
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 41,16:
            - Owner: Songhai
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 40,16:
            - Owner: Songhai
            - CityID: 9242
            - Population: 29
            - City: Shimonoseki
            - Religion: Islam
            - Route: Railroad
          - Desert Hills 39,17:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 39,18:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 38,18:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 37,19:
            - Owner: Songhai
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 37,20:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Plains Land 36,21:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 35,21:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
          - Plains Land 35,22:
            - Owner: Songhai
            - CityID: 4728
            - Population: 35
            - City: Walata
            - Religion: Islam
            - Route: Railroad
          - Coast 34,23:
            - Owner: Songhai
        
        ### 215
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: CityBombard
          - Unit: Artillery
          - ID: 15571
        - Player: 4: Songhai
        - Plots:
          - Tundra Hills 22,47:
            - Owner: Songhai
            - CityID: 13222
            - Population: 24
            - City: Pyongyang
            - Religion: Islam
            - Route: Railroad
          - Coast 23,47:
            - Owner: Songhai
            - Resource: Pearls
            - Improvement: Fishing Boats
        
        ### 216
        - Type: RebaseTo
        - Player: 4: Songhai
        - Unit:
          - Level: 7
          - Health: 75%
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 18033
        - Desert Hills 34,38:
          - Owner: Songhai
          - CityID: 1061
          - Population: 52
          - IsRiver: true
          - City: Gao
          - Religion: Islam
          - Route: Railroad
        
        ### 217
        - Type: UnitMoved
        - Unit:
          - Level: 7
          - Health: 75%
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 18033
        - Player: 4: Songhai
        - Desert Hills 34,38:
          - Owner: Songhai
          - CityID: 1061
          - Population: 52
          - IsRiver: true
          - City: Gao
          - Religion: Islam
          - Route: Railroad
        
        ### 218
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 2251
        - Player: 4: Songhai
        - Plots:
          - Plains Hills 39,37:
            - Owner: Songhai
            - Resource: Copper
            - Improvement: Mine
            - Route: Railroad
          - Mountain Mountain 40,37:
            - Owner: Songhai
            - Route: Railroad
          - Plains Hills 41,37:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 42,37:
            - Owner: Songhai
            - Resource: Uranium
            - Improvement: Fort
        
        ### 219
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 4: Songhai
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 2251
        - Build: Construct a Railroad
        - Grass Hills 42,37:
          - Owner: Songhai
          - Resource: Uranium
          - Improvement: Fort
        
        ### 220
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 2677
        - Player: 4: Songhai
        - Plots:
          - Plains Land 45,42:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Farm
          - Desert Land 44,41:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 45,40:
            - Owner: Songhai
            - CityID: 19051
            - Population: 25
            - IsRiver: true
            - City: Kyoto
            - Religion: Islam
            - Route: Railroad
          - Plains Hills 44,39:
            - Owner: Songhai
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
        
        ### 221
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3908
        - Player: 4: Songhai
        - Plots:
          - Tundra Hills 42,43:
            - Owner: Songhai
            - Resource: Copper
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 41,43:
            - Owner: Songhai
            - Resource: Stone
            - Improvement: Citadel
            - Route: Railroad
          - Plains Land 41,42:
            - Owner: Songhai
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 40,41:
            - Owner: Songhai
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 40,40:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 39,39:
            - Owner: Songhai
            - Resource: Copper
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 39,38:
            - Owner: Songhai
            - CityID: 1276
            - Population: 35
            - City: Tombouctu
            - Religion: Islam
            - Route: Railroad
          - Plains Hills 39,37:
            - Owner: Songhai
            - Resource: Copper
            - Improvement: Mine
            - Route: Railroad
          - Mountain Mountain 40,37:
            - Owner: Songhai
            - Route: Railroad
          - Plains Hills 41,37:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 42,36:
            - Owner: Songhai
            - Resource: Cattle
        
        ### 222
        - Type: UnitBuildCompleted
        - Owner: 4: Songhai
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3908
        - Build: Construct a Railroad
        - Grass Land 42,36:
          - Owner: Songhai
          - Resource: Cattle
        
        ### 223
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3087
        - Player: 4: Songhai
        - Grass Land 45,39:
          - Owner: Songhai
          - Improvement: Village
          - Route: Railroad
        
        ### 224
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 4: Songhai
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3087
        - Build: Repair an Improvement
        - Grass Land 45,39:
          - Owner: Songhai
          - Improvement: Village
          - Route: Railroad
        
        ### 225
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 5664
        - Player: 4: Songhai
        - Plots:
          - Grass Land 43,37:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 44,38:
            - Owner: Songhai
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Land 45,38:
            - Owner: Songhai
            - Resource: Dyes
            - Improvement: Plantation
            - Route: Railroad
        
        ### 226
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 4: Songhai
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 5664
        - Build: Repair an Improvement
        - Grass Land 45,38:
          - Owner: Songhai
          - Resource: Dyes
          - Improvement: Plantation
          - Route: Railroad
        
        ### 227
        - Type: UnitBuildCompleted
        - Owner: 4: Songhai
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3912
        - Build: Construct a Farm
        - Plains Land 42,39:
          - Owner: Songhai
          - IsRiver: true
        
        ### 228
        - Type: UnitBuildCompleted
        - Owner: 4: Songhai
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 18510
        - Build: Construct a Mine
        - Tundra Hills 51,9:
          - Owner: Songhai
        
        ### 229
        - Type: UnitBuildCompleted
        - Owner: 4: Songhai
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 11738
        - Build: Construct a Farm
        - Plains Land 42,38:
          - Owner: Songhai
        
        ### 230
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 4: Songhai
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 2272
        - Build: Construct a Mine
        - Plains Hills 41,39:
          - Owner: Songhai
          - Route: Road
        
        ### 231
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 7025
        - Player: 4: Songhai
        - Plots:
          - Tundra Hills 38,33:
            - Owner: Songhai
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Tundra Hills 39,34:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Tundra Hills 39,35:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 39,36:
            - Owner: Songhai
            - Improvement: Town
            - Route: Railroad
          - Plains Hills 39,37:
            - Owner: Songhai
            - Resource: Copper
            - Improvement: Mine
            - Route: Railroad
          - Mountain Mountain 40,37:
            - Owner: Songhai
            - Route: Railroad
          - Plains Hills 41,37:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 42,36:
            - Owner: Songhai
            - Resource: Cattle
          - Grass Land 43,36:
            - Owner: Songhai
            - IsRiver: true
            - Route: Railroad
          - Grass Land 43,37:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 44,38:
            - Owner: Songhai
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
        
        ### 232
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 4: Songhai
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 7025
        - Build: Chop Down a Forest
        - Plains Hills 44,38:
          - Owner: Songhai
          - Improvement: Lumber Mill
          - Route: Railroad
          - Feature: Forest
        
        ### 233
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 2870
        - Player: 4: Songhai
        - Plots:
          - Desert Land 40,16:
            - Owner: Songhai
            - CityID: 9242
            - Population: 29
            - City: Shimonoseki
            - Religion: Islam
            - Route: Railroad
          - Desert Hills 39,17:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 39,18:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 39,19:
            - Owner: Songhai
            - Improvement: Academy
            - Route: Railroad
          - Desert Land 39,20:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Desert Land 38,20:
            - Owner: Songhai
            - Resource: Aluminum
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 37,20:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Plains Land 36,21:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 35,21:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
          - Plains Land 35,22:
            - Owner: Songhai
            - CityID: 4728
            - Population: 35
            - City: Walata
            - Religion: Islam
            - Route: Railroad
          - Grass Land 35,23:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Grass Land 36,24:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Cattle
            - Improvement: Pasture
            - Route: Railroad
          - Plains Land 36,25:
            - Owner: Songhai
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 37,25:
            - Owner: Songhai
            - Resource: Rice
            - Improvement: Town
            - Route: Railroad
          - Plains Land 38,26:
            - Owner: Songhai
            - Route: Railroad
            - Feature: El Dorado
          - Plains Land 38,27:
            - Owner: Songhai
            - CityID: 5558
            - Population: 35
            - IsRiver: true
            - City: Sao Paulo
            - Religion: Islam
            - Route: Railroad
          - Plains Land 39,27:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Grass Land 40,27:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Land 41,28:
            - Owner: Songhai
            - Resource: Rice
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 40,29:
            - Owner: Songhai
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Plains Hills 40,30:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 39,31:
            - Owner: Songhai
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
          - Grass Land 39,32:
            - Owner: Songhai
            - CityID: 2951
            - Population: 34
            - City: Kukia
            - Resource: Coal
            - Religion: Islam
            - Route: Railroad
          - Tundra Hills 38,33:
            - Owner: Songhai
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Tundra Hills 39,34:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Tundra Hills 39,35:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 39,36:
            - Owner: Songhai
            - Improvement: Town
            - Route: Railroad
          - Plains Hills 39,37:
            - Owner: Songhai
            - Resource: Copper
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 39,38:
            - Owner: Songhai
            - CityID: 1276
            - Population: 35
            - City: Tombouctu
            - Religion: Islam
            - Route: Railroad
          - Plains Hills 39,39:
            - Owner: Songhai
            - Resource: Copper
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 40,40:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 40,41:
            - Owner: Songhai
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 41,42:
            - Owner: Songhai
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 41,43:
            - Owner: Songhai
            - Resource: Stone
            - Improvement: Citadel
            - Route: Railroad
          - Tundra Hills 42,43:
            - Owner: Songhai
            - Resource: Copper
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 43,43:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Plains Land 44,42:
            - Owner: Songhai
            - Resource: Aluminum
            - Improvement: Mine
            - Route: Railroad
        
        ### 234
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4277
        - Player: 4: Songhai
        - Plots:
          - Grass Land 35,23:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Grass Land 36,24:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Cattle
            - Improvement: Pasture
            - Route: Railroad
          - Plains Land 36,25:
            - Owner: Songhai
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 37,25:
            - Owner: Songhai
            - Resource: Rice
            - Improvement: Town
            - Route: Railroad
          - Plains Land 38,26:
            - Owner: Songhai
            - Route: Railroad
            - Feature: El Dorado
          - Plains Land 38,27:
            - Owner: Songhai
            - CityID: 5558
            - Population: 35
            - IsRiver: true
            - City: Sao Paulo
            - Religion: Islam
            - Route: Railroad
          - Grass Hills 38,28:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 38,29:
            - Owner: Songhai
            - Resource: Brazilwood
            - Improvement: Brazilwood Camp
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 39,30:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 39,31:
            - Owner: Songhai
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
          - Plains Land 40,32:
            - Owner: Songhai
            - Resource: Olives
            - Improvement: Plantation
            - Route: Railroad
          - Plains Hills 40,33:
            - Owner: Songhai
            - Resource: Sheep
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Land 41,33:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 42,33:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Citadel
            - Route: Railroad
          - Plains Land 42,34:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Farm
          - Grass Hills 42,35:
            - Owner: Songhai
            - Feature: Forest
        
        ### 235
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1421
        - Player: 4: Songhai
        - Tundra Land 50,7:
          - Owner: Songhai
          - CityID: 11571
          - Population: 23
          - City: Tilburg
          - Religion: Islam
          - Route: Railroad
        
        ### 236
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 17012
        - Player: 4: Songhai
        - Plots:
          - Ocean 26,41:
            - Owner: Songhai
          - Coast 27,40:
            - Owner: Songhai
          - Desert Land 27,39:
            - Owner: Songhai
            - CityID: 2568
            - Population: 35
            - City: Kumbi Saleh
            - Religion: Islam
            - Route: Railroad
          - Plains Land 28,39:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Desert Hills 29,38:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 30,38:
            - Owner: Songhai
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Desert Hills 31,38:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 32,38:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Lapis Lazuli
            - Improvement: Quarry
            - Route: Railroad
          - Desert Hills 33,38:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 34,38:
            - Owner: Songhai
            - CityID: 1061
            - Population: 52
            - IsRiver: true
            - City: Gao
            - Religion: Islam
            - Route: Railroad
          - Plains Land 35,38:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
          - Grass Land 36,38:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
          - Grass Land 37,38:
            - Owner: Songhai
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 37,39:
            - Owner: Songhai
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 38,40:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Desert Hills 38,41:
            - Owner: Songhai
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 39,42:
            - Owner: Songhai
            - Resource: Wheat
            - Improvement: Town
            - Route: Railroad
          - Desert Land 39,43:
            - Owner: Songhai
            - CityID: 1543
            - Population: 37
            - IsRiver: true
            - City: Jenne
            - Religion: Islam
            - Route: Railroad
        
        ### 237
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 19316
        - Player: 4: Songhai
        - Plots:
          - Plains Land 40,21:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 40,20:
            - Owner: Songhai
            - Improvement: Town
            - Route: Railroad
          - Desert Land 39,20:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Desert Land 38,20:
            - Owner: Songhai
            - Resource: Aluminum
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 37,20:
            - Owner: Songhai
            - Improvement: Village
            - Route: Railroad
          - Plains Land 36,21:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 35,21:
            - Owner: Songhai
            - IsRiver: true
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
          - Plains Land 35,22:
            - Owner: Songhai
            - CityID: 4728
            - Population: 35
            - City: Walata
            - Religion: Islam
            - Route: Railroad
        
        ### 238
        - Type: CombatResult
        - Coast 22,40:
          - Owner: Songhai
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 57
          - Damage: 92
          - Player: 3: The Zulus
          - Unit:
            - Level: 4
            - Health: 65%
            - AI: AssaultSea
            - Unit: Submarine
            - ID: 17671
        
        ### 239
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 77%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18872
        - Player: 4: Songhai
        - Plots:
          - Coast 16,48:
            - Owner: Songhai
          - Ocean 17,48:
            - Owner: Songhai
          - Ocean 18,48:
            - Owner: Songhai
          - Ocean 19,48:
            - Owner: Songhai
          - Ocean 19,47:
            - Owner: Songhai
          - Ocean 20,47:
            - Owner: Songhai
          - Coast 21,47:
            - Owner: Songhai
        
        ### 240
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: Ranged
          - Unit: Bazooka
          - ID: 17929
        - Player: 4: Songhai
        - Coast 33,21:
          - Owner: Songhai
          - Feature: Atoll
        
        ### 241
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Bazooka
          - ID: 18699
        - Player: 4: Songhai
        - Grass Land 35,23:
          - Owner: Songhai
          - Improvement: Village
          - Route: Railroad
        
        ### 242
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: CityBombard
          - Unit: Artillery
          - ID: 15571
        - Player: 4: Songhai
        - Tundra Hills 23,46:
          - Owner: Songhai
          - Improvement: Mine
        
        ### 243
        - Type: PlayerDoneTurn
        - NextPlayer: 5: Siam
        - Player: 4: Songhai
        
        You, Askia (leader of Songhai, Player 4), are making strategic decisions after turn 426.
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
    - You are Askia, leader of Songhai (Player 4).
      
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
      - Name: Songhai
      - Uniques:
        - Unique Unit: Mandekalu Cavalry, Replacing Knight (Requires technology: Chivalry)
        - Unique Unit: Sofa, Replacing Crossbowman (Requires technology: Machinery)
        - Unique Building: Tabya, Replacing Stone Works (Requires technology: Construction)
        - Unique Building: Gumey, Replacing Caravansary (Requires technology: Currency)
        - Civilization Ability: Triple Gold from destroying Encampments and plundering Cities. Land Units gain the Amphibious and War Canoes Promotions.
      - Leader: Askia
      - PlayerID: 4
      
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
      - Electronics: Allows you to build the Police Station, increasing City security level.
        Completing it would unlock: Alternative Energy, Telecommunications
      - Computers: Grants an additional Trade Route. Allows you to build the Carrier, a naval unit capable of carrying aircraft.
        Completing it would unlock: Telecommunications, Satellites
      - Stealth: Allows you to build the Stealth Bomber, the most powerful Ranged Unit in the game.
        Completing it would unlock: Globalization, Nuclear Fusion
      
      ## Policies
      - Communism (Level 1 Tenet of Ideology Order): Communism: Gold cost of investing in buildings reduced by 25%. +20% Production when building Wonders.
      - People's Army (Level 1 Tenet of Ideology Order): People's Army: +100% Production towards Military Academies, and receive 5 Free Military Academies in your Empire. Public Schools produce +5 Culture and +2 Happiness.
      - Hero of the People (Level 1 Tenet of Ideology Order): Hero of the People: Great Person rate increases by 25%. A Great Person of your choice appears near your Capital.
      - Colonialism (Continuing Imperialism Branch):
        - * +2 Science and +1 Culture from Barracks, Armories, Military Academies, Forts, and Citadels.
        - * Each unique Global Monopoly modifier is increased by an additional 10% if it's percentage-based, or +3 otherwise.
      - Honor (Continuing Authority Branch):
        - * All Military Units gain the Conscription Promotion (+10% Combat Strength).
        - * Supply-free military Units spawn near Cities that reach (or have already reached) a multiple of 10 Citizens for the first time.
        - * -25% War Weariness.
      - Double Agents (Level 1 Tenet of Ideology Order): Double Agents: Receive 200 Spy Points. Gain 125 Science when you identify a foreign Spy, scaling with Era.
      - Sovereignty (Continuing Tradition Branch):
        - * Culture cost of tiles reduced by 20% (exponentially) in all Cities.
        - * Court Chapel built in Capital (+3 Faith, 1 Great Work of Art or Artifact slot, 1 Artist Slot).
      - Splendor (Continuing Tradition Branch):
        - * Expending a Great Person grants 50 Culture, scaling with Era.
        - * State Treasury built in Capital (+4 Gold, +2 Culture to all Monuments, Gardens, and Baths; 1 Merchant Slot).
      - Liberty (Continuing Progress Branch):
        - * +2 Gold in every City.
        - * +25% Tile improvement rate.
        - * A Worker appears near the Capital.
      - Nobility (Continuing Fealty Branch):
        - * +1 Happiness and +2 Gold from Castles.
        - * +2 Gold from Armories.
        - * +100% Production towards Castles and Armories.
      - Refinement (Continuing Artistry Branch):
        - * +2 Culture from Great Works of Art.
        - * 1 Specialist in all cities does not produce Unhappiness from Urbanization.
        - * +1 Culture from Specialists.
      - Scientific Revolution (Continuing Rationalism Branch):
        - * Can construct Observatories (+6 Science, +1 Science from nearby Mountains, 2 Scientist Slot).
        - * +2 Science from Jungle and Snow.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Free Trade (Continuing Industry Branch):
        - * Earn Great Merchants 50% faster.
        - * +5 Gold from International Trade Routes.
        - * -2 Unhappiness from Poverty in all Cities.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Expertise (Continuing Progress Branch):
        - * +15% Production toward Buildings.
        - * Cities earn +10 Culture when they construct Buildings, scaling with Era.
      - Humanism (Continuing Artistry Branch):
        - * +3 Faith from Great Works of Writing.
        - * -25% Golden Age Points needed to trigger a Golden Age.
        - * +1 Happiness from all Guilds.
      - Trade Confederacy (Continuing Statecraft Branch):
        - * +25% Yields for International Trade Routes.
        - * Trade Routes to City-States generate +1 Influence per turn (with the target City-State) per each owned City-State Trade Route (up to +5).
      - Foreign Service (Continuing Statecraft Branch):
        - * Receive 100 Spy Points.
        - * Earn Great Diplomats 50% faster.
        - * +50% Rewards from City-State Quests.
        - * +1 of every Strategic Resource for every three City-State Alliances you maintain.
  - decisions:
    - #0:
      - toolName: keep-status-quo
      - rationale: Maintaining UnitedNations grand strategy is optimal as we lead in Diplomatic Victory delegates (20 vs Siam's 17) and have strong city-state alliances. Our position is strong with 20 delegates and growing influence. No need to change current strategic direction.
  - tokens:
    - inputTokens: 59731
    - reasoningTokens: 644
    - outputTokens: 69
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: I need to analyze the current state of the game and make strategic decisions for Songhai. Let me break down the situation:
            
            1. **Current Grand Strategy**: UnitedNations (Diplomatic Victory focus)
            2. **Current Status**:
               - Strong position with 19 cities, 595 population, and high military strength (9649)
               - At war with Japan, The Zulus, Korea, and Siam
               - High gold (914) but low gold per turn (8)
               - Strong science (3107) and culture (2246) output
               - Founded Islam as the majority religion in most cities
               - Multiple city-states allied (Dublin, Palatium, Antananarivo, Luba, Lutetia, Harappa)
               - 20 delegates in World Congress (leading)
               - Nuclear weapons production underway (Atomic Bombs in multiple cities)
            
            3. **Key Observations**:
               - The Zulus are the top competitor for Domination Victory (62% vs our 37%)
               - Siam is leading Diplomatic Victory (17 delegates vs our 20)
               - Japan is a major military threat with 19 cities and strong navy
               - Korea is weakened (vassal of The Zulus)
               - We have strong air power (Fighters, Heavy Bombers)
               - Multiple cities producing Strategic Defense Systems and Heavy Bombers
               - City-states provide strong defensive positions and tourism boosts
            
            4. **Current Research**: Stealth (next after Advanced Ballistics)
            5. **Current Policy**: Hero of the People (next policy choice)
            
            6. **Strategic Considerations**:
               - Diplomatic Victory is within reach (need 41 delegates, currently have 20)
               - Need to maintain relationships with city-states for delegate bonuses
               - Should continue focusing on science and production for spaceship components
               - Need to manage war weariness from multiple conflicts
               - Should consider settling new cities to expand territory and production
               - Need to protect our cities from air attacks (Japan has strong air units)
               - Should continue building defensive infrastructure (Strategic Defense Systems)
            
            7. **Immediate Decisions Needed**:
               - Should I change the grand strategy or keep UnitedNations?
               - Should I adjust flavors for better military/civilian balance?
               - Should I change research direction?
               - Should I change policy direction?
               - Should I adjust diplomatic relationships?
            
            Given our strong position in Diplomatic Victory and the fact that we're leading in delegates (20 vs Siam's 17), I should maintain the UnitedNations focus but adjust flavors to better support our diplomatic push while maintaining military strength.
            
            I'll:
            1. Keep UnitedNations as the grand strategy
            2. Adjust flavors to prioritize Diplomacy, Science, and Gold while maintaining military strength
            3. Keep Stealth as the next research (good for air power and espionage)
            4. Keep Hero of the People as the next policy (supports Great Person generation)
            5. Keep current diplomatic relationships as they are (we're doing well with city-states)
            
            Let me call the appropriate tools to implement these decisions.
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: U06doF6HP
          - toolName: keep-status-quo
          - input:
            - Rationale: Maintaining UnitedNations grand strategy is optimal as we lead in Diplomatic Victory delegates (20 vs Siam's 17) and have strong city-state alliances. Our position is strong with 20 delegates and growing influence. No need to change current strategic direction.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: U06doF6HP
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.