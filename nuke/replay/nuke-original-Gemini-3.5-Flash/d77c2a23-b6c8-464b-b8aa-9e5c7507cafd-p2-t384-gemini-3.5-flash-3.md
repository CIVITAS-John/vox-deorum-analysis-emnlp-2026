- row:
  - game_id: d77c2a23-b6c8-464b-b8aa-9e5c7507cafd
  - player_id: 2
  - turn: 384
  - player_type: Kimi-K2.5-Simple
  - prev_use_nuke: 95.0
  - after_use_nuke: 100.0
  - prev_nuke: 100.0
  - after_nuke: 100.0
  - rationale: Maximum offensive posture for existential cultural war. UseNuke 100 and Nuke 100 authorize nuclear strikes on Dutch cultural centers (Amsterdam/Rotterdam/Utrecht) to destroy tourism buildings before Netherlands influences Austria in 6 turns. Mobile 100 and Air 100 enable rapid strikes. Production 100 and Mobilization 100 ensure nuclear missile replacement. Netherlands at 97% with Austria - only 6 turns left. Must destroy their tourism NOW or lose cultural victory.
- originalModel: openai-compatible/Kimi-K2.5@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: false
  - messagesModified: false
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 95
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
    - You are Bismarck, leader of Germany (Player 2).
      
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
      - Name: Germany
      - Uniques:
        - Unique Unit: Landsknecht, Replacing Tercio (Requires technology: Gunpowder)
        - Unique Unit: Krupp Gun, Replacing Artillery (Requires technology: Replaceable Parts)
        - Unique Building: Hanse, Replacing Customs House (Requires technology: Guilds)
        - Unique Building: Brewhouse, Replacing Windmill (Requires technology: Economics)
        - Civilization Ability: Gain +1 Influence per turn with City-States for each gifted Unit (lost when killed). -15% Production and Gold costs for Military Units.
      - Leader: Bismarck
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
      - Satellites: Allow you to build the Apollo Program, a project necessary to win a Science Victory.
        Completing it would unlock: The Internet, Lasers
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      - Telecommunications: Allows you to build the Interpretive Center, boosting all Landmarks in empire.
        Completing it would unlock: Robotics, The Internet
      - Mobile Tactics: Allows you to build the Mechanized Infantry, a fast and versatile late game Unit that doesn't require any resources.
        Completing it would unlock: Stealth
      
      ## Policies
      - Total War (Level 2 Tenet of Ideology Autocracy): Total War: +25% Production when building Land Units. Warscore increases 25% more quickly, and it is 25% easier to bully City-States.
      - Third Alternative (Level 2 Tenet of Ideology Autocracy): Third Alternative: Quantity of Strategic Resources produced (including Paper) is increased by 100%. Reduces Unit Gold Maintenance costs by 25%.
      - Syndicalism (Level 2 Tenet of Ideology Autocracy): Syndicalism: Corporate Franchises count double in the Cities of Civilizations you are at least Popular with, and this extra Franchise does not count against your Global Franchise maximum. Can establish 5 additional Franchises in foreign Cities. +2 Production from all Corporation Offices.
      - Mare Nostrum (Level 2 Tenet of Ideology Autocracy): Mare Nostrum: +1 Oil and Coal for every City-State Alliance. +2 Production and Culture to Atolls, Fishing Boats, and Offshore Oil Platforms. Naval Ranged Units gain the Mare Nostrum Promotion.
      - Futurism (Level 1 Tenet of Ideology Autocracy): Futurism: Strengthens Tourism of Historic Events generated by the Palace. +2 Culture from Great Works. Earn 50 Tourism when you conquer a city for the first time, scaling with Era and city size.
      - Lebensraum (Level 1 Tenet of Ideology Autocracy): Lebensraum: Receive 10 Culture and Golden Age Points when your borders expand, scaling with Era. Citadels may also be built in foreign territory adjacent to your borders. Retain tiles after razing Cities.
      - Police State (Level 2 Tenet of Ideology Autocracy): Police State: +3 Local Happiness from every Courthouse, and +10 City Security from Police Stations. +100% Production towards Courthouses and Police Stations.
      - Iron Fist (Level 1 Tenet of Ideology Autocracy): Iron Fist: Vassals can no longer be liberated by other Civilizations or the World Congress, and capitulated vassals can no longer rebel. Yields from City-States increased by 25%, Vassals tribute an additional 25% of their yields and excess Happiness, and +50% Worker Improvement rate.
      - Honor (Continuing Authority Branch):
        - * All Military Units gain the Conscription Promotion (+10% Combat Strength).
        - * Supply-free military Units spawn near Cities that reach (or have already reached) a multiple of 10 Citizens for the first time.
        - * -25% War Weariness.
      - Liberty (Continuing Progress Branch):
        - * +2 Gold in every City.
        - * +25% Tile improvement rate.
        - * A Worker appears near the Capital.
      - Organization (Continuing Progress Branch):
        - * +2 Production in every City.
        - * +25% Production toward Workers and Trade Units.
        - * +1 Movement for Workers.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Free Trade (Continuing Industry Branch):
        - * Earn Great Merchants 50% faster.
        - * +5 Gold from International Trade Routes.
        - * -2 Unhappiness from Poverty in all Cities.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Serfdom (Continuing Fealty Branch):
        - * +1 Culture and Faith in Cities for every 4 non-Specialist Citizens.
        - * +2 Production and +1 Gold from Pastures.
      - Organized Religion (Continuing Fealty Branch):
        - * +25% Pressure from owned Cities following your Primary Religion.
        - * +1 Delegate in the World Congress for every 10 Cities following your Primary Religion.
        - * +2 Culture from Shrines and Temples.
      - Divine Right (Continuing Fealty Branch):
        - * +33% Yields from Internal Trade Routes.
        - * Completing an Internal Trade Route triggers a Historic Event as if completing an International Trade Route.
        - * -1 Unhappiness from Boredom in all Cities.
      - Tribute (Continuing Authority Branch):
        - * A Settler appears near the Capital.
        - * Gain Culture in Capital equal to 25% of the Gold Tribute demanded from City-States (50% if all Authority policies are adopted).
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
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
      - Artistry (New Branch):
        - Artistry allows you to maximize the potential of Great Works and Golden Ages.
        - Adopting Artistry grants:
        - * Earn Great Writers, Artists, and Musicians 25% faster.
        - * +10% Culture during Golden Ages.
        - * +100% Production towards all Guilds.
        - Each Artistry policy unlocked grants:
        - * +1 Science in every City.
        - * 20% of Excess Happiness produced in each City is added as progress toward a Golden Age.
        - Adopting all policies in Artistry grants:
        - * Unlocks building the Louvre.
        - * Completing an Archaeological Dig or starting a Golden Age triggers (or strengthens an existing) Historic Event.
        - * Allows you to see Hidden Antiquity Sites.
        - * +3 Science from Landmarks.
        - * Allows for the purchase of Great Musicians with Faith starting in the Industrial Era.
  - messages:
    - #0:
      - role: user
      - content: # Strategies
        Strategies: existing strategic decisions from you.
        
        ## Persona
        - VictoryCompetitiveness: 10
        - WonderCompetitiveness: 5
        - MinorCivCompetitiveness: 10
        - Boldness: 10
        - WarBias: 10
        - HostileBias: 10
        - WarmongerHate: 10
        - NeutralBias: 10
        - FriendlyBias: 1
        - GuardedBias: 10
        - AfraidBias: 3
        - DiplomaticBalance: 8
        - Friendliness: 6
        - WorkWithWillingness: 7
        - WorkAgainstWillingness: 6
        - Loyalty: 9
        - MinorCivFriendlyBias: 10
        - MinorCivNeutralBias: 1
        - MinorCivHostileBias: 1
        - MinorCivWarBias: 2
        - DenounceWillingness: 3
        - Forgiveness: 7
        - Meanness: 9
        - Neediness: 5
        - Chattiness: 4
        - DeceptiveBias: 5
        - Rationale: Total war posture maintained. WarBias 10 ensures immediate declaration of war against Netherlands now that peace treaty expired. HostileBias 10 maintains aggression. Boldness 10 accepts risks to capture Dutch cities quickly. FriendlyBias 1 confirms no mercy for Netherlands - they forced peace while I was winning, now their cultural wonders burn. Loyalty 9 maintains Austria and Mongolia alliances for votes.
        
        ## Technology
        - Next: None
        
        ## Policy
        - Next: Total War (Policy)
        - Rationale: Total War (Autocracy Level 2) provides +25% Production for Land Units and 25% faster warscore accumulation. With 15 turns until next policy, this maximizes military output for the critical campaign against Netherlands. The production bonus stacks with Mobilization flavor to replace losses and build nuclear missile reserves quickly. Warscore bonus helps force peace terms if needed while having destroyed Dutch cultural centers.
        
        ## Relationships
        
        ### Indonesia
        - Public: 0
        - Private: 0
        - Rationale: Indonesia is my capitulated vassal with peace treaty. They have Declaration of Friendship with Netherlands but are weak (1 city) and far from the front. Keeping them neutral prevents another front opening while I focus on Netherlands. They will become Influential by me in 2 turns anyway.
        - UpdatedTurn: 367
        
        ### The Aztecs
        - Public: 0
        - Private: 0
        - Rationale: Aztecs are at 95% Popular with Netherlands and will fall in ~3 turns. They serve as a crucial cultural buffer - every turn they resist helps me. Maintaining neutral stance removes hostility penalties, helping them survive slightly longer. They're weak (1 city) and capitulated to Netherlands anyway.
        - UpdatedTurn: 375
        
        ### Austria
        - Public: 100
        - Private: 100
        - Rationale: Austria remains the decisive prize - last civilization needed for cultural victory at 94% Popular (7 turns to Influential). Netherlands at 96% means this will be extremely close. Maximum relationship maintained to ensure they resist Dutch cultural pressure. Defensive pact provides security against Songhai. Every turn Austria survives independent is a turn closer to my cultural victory.
        - UpdatedTurn: 382
        
        ### The Netherlands
        - Public: -100
        - Private: -100
        - Rationale: Netherlands remains the existential threat at 96% Popular with Austria, 8 turns from Influential. Maximum hostility maintained. They've proven aggressive recapturing Ardea. Nuclear strikes against Amsterdam/Rotterdam/Utrecht's cultural buildings are authorized as soon as Advanced Ballistics completes. Must eliminate their tourism infrastructure before World Congress vote in 6 turns and before they secure Austria's culture.
        - UpdatedTurn: 382
        
        ### Songhai
        - Public: -100
        - Private: -100
        - Rationale: Songhai has defensive pact with Netherlands and will join war against me. Their military (2665) is weak compared to mine (22906) but they could divert attention from the Netherlands front. Maximum hostility ensures AI suppresses them quickly before they can interfere with the critical campaign against Dutch cultural centers.
        - UpdatedTurn: 382
        
        ### Mongolia
        - Public: 100
        - Private: 100
        - Rationale: Mongolia provides 5 crucial delegates for World Congress votes in 7 turns. Already Influential with them culturally. Maintaining alliance denies Netherlands potential votes and preserves my voting bloc for diplomatic backup if cultural victory is delayed.
        - UpdatedTurn: 382
        
        ### Rome
        - Public: -60
        - Private: -55
        - Rationale: Rome captured Satricum from me while I was engaged with Netherlands, but they're about to become Influential to me (99%, 1 turn). Keeping hostile stance maintained but not escalating further - they serve as useful buffer against Netherlands and their Order ideology makes them natural enemy. Their cultural weakness means they'll help my victory once Influential. Need to watch eastern front but main effort remains Netherlands.
        - UpdatedTurn: 382
        
        ## Strategy
        - Rationale: Relationships are optimally configured: Austria at maximum (100/100) to resist Dutch influence, Netherlands at maximum hostility (-100/-100) to ensure total war commitment, Mongolia at 100/100 to preserve 5 crucial World Congress delegates. No changes needed - focus all effort on military destruction of Dutch cultural centers before they influence Austria in 7 turns.
        - GrandStrategy: Conquest
        
        ### Flavors
        - Offense: 95
        - Defense: 15
        - Mobilization: 95
        - CityDefense: 10
        - MilitaryTraining: 85
        - Recon: 5
        - Ranged: 90
        - Mobile: 100
        - Nuke: 100
        - UseNuke: 95
        - Naval: 75
        - NavalRecon: 65
        - NavalGrowth: 45
        - NavalTileImprovement: 40
        - Air: 100
        - AirCarrier: 85
        - Antiair: 55
        - Airlift: 95
        - Expansion: 0
        - Growth: 15
        - TileImprovement: 15
        - Infrastructure: 25
        - Production: 100
        - WaterConnection: 35
        - Gold: 55
        - Science: 35
        - Culture: 60
        - Happiness: 25
        - GreatPeople: 45
        - Wonder: 0
        - Religion: 10
        - Diplomacy: 5
        - Spaceship: 15
        - Espionage: 80
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: Rome
        - Germany:
          - CapitalsControlled:
            - Tenochtitlan
            - Berlin
          - CapitalsPercentage: 25
        - Rome:
          - CapitalsControlled:
            - Rome
            - Jakarta
          - CapitalsPercentage: 25
        
        ## ScienceVictory
        - Unlocked in the Information era
        
        ## CulturalVictory
        - CivsNeeded: 6
        - Contender: Germany
        - Austria:
          - Influences:
            - Rome: Exotic (17%) - Rising Slowly (tourism/culture ratio 53%)
            - Germany: Exotic (6%) - Rising Slowly (tourism/culture ratio 13%)
            - Songhai: Familiar (44%) - Rising (884 turns to Influential, tourism/culture ratio 130%)
            - The Aztecs: Familiar (41%) - Rising (65 turns to Influential, tourism/culture ratio 3429%)
            - Mongolia: Popular (75%) - Rising (18 turns to Influential, tourism/culture ratio 680%)
            - The Netherlands: Familiar (27%) - Rising Slowly (tourism/culture ratio 99%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Germany:
          - Influences:
            - Austria: Popular (95%) - Rising (7 turns to Influential, tourism/culture ratio 190%)
            - Mongolia: Dominant (219%) - Rising (tourism/culture ratio 2999%)
            - Songhai: Influential (136%) - Rising (tourism/culture ratio 538%)
            - The Aztecs: Dominant (264%) - Rising (tourism/culture ratio 22754%)
            - The Netherlands: Influential (121%) - Rising (tourism/culture ratio 616%)
            - Rome: Influential (100%) - Rising (tourism/culture ratio 397%)
          - PolicyPercentage: 100
          - InfluentialCivs: 5
        - Mongolia:
          - Influences:
            - The Aztecs: Exotic (10%) - Rising Slowly (tourism/culture ratio 355%)
            - The Netherlands: Exotic (5%) - Rising Slowly (tourism/culture ratio 10%)
            - Austria: Exotic (8%) - Rising Slowly (tourism/culture ratio 8%)
            - Songhai: Exotic (7%) - Rising Slowly (tourism/culture ratio 11%)
          - PolicyPercentage: 70
          - InfluentialCivs: 0
        - Rome:
          - Influences:
            - Austria: Familiar (46%) - Rising Slowly (tourism/culture ratio 69%)
            - Germany: Exotic (13%) - Rising Slowly (tourism/culture ratio 36%)
            - Songhai: Popular (63%) - Rising (104 turns to Influential, tourism/culture ratio 171%)
            - The Aztecs: Popular (53%) - Rising (66 turns to Influential, tourism/culture ratio 2717%)
            - Mongolia: Popular (67%) - Rising (43 turns to Influential, tourism/culture ratio 433%)
            - The Netherlands: Familiar (39%) - Rising Slowly (tourism/culture ratio 121%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Songhai:
          - Influences:
            - Austria: Familiar (42%) - Rising Slowly (tourism/culture ratio 92%)
            - Germany: Exotic (6%) - Rising Slowly (tourism/culture ratio 13%)
            - The Aztecs: Familiar (39%) - Rising (75 turns to Influential, tourism/culture ratio 3109%)
            - Mongolia: Popular (69%) - Rising (25 turns to Influential, tourism/culture ratio 625%)
            - The Netherlands: Familiar (32%) - Rising Slowly (tourism/culture ratio 116%)
            - Rome: Exotic (18%) - Rising Slowly (tourism/culture ratio 58%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - The Aztecs:
          - Influences:
            - Austria: Exotic (21%) - Rising Slowly (tourism/culture ratio 1%)
            - Germany: Exotic (6%) - Rising Slowly (tourism/culture ratio 0%)
            - Songhai: Exotic (23%) - Rising Slowly (tourism/culture ratio 1%)
            - The Netherlands: Exotic (15%) - Rising Slowly (tourism/culture ratio 1%)
            - Mongolia: Familiar (43%) - Rising Slowly (tourism/culture ratio 8%)
            - Rome: Exotic (10%) - Rising Slowly (tourism/culture ratio 0%)
          - PolicyPercentage: 74
          - InfluentialCivs: 0
        - The Netherlands:
          - Influences:
            - Rome: Familiar (42%) - Rising Slowly (tourism/culture ratio 81%)
            - Germany: Exotic (14%) - Rising Slowly (tourism/culture ratio 25%)
            - Songhai: Influential (119%) - Rising (tourism/culture ratio 255%)
            - The Aztecs: Influential (110%) - Rising (tourism/culture ratio 6660%)
            - Mongolia: Influential (160%) - Rising (tourism/culture ratio 866%)
            - Austria: Popular (97%) - Rising (6 turns to Influential, tourism/culture ratio 151%)
          - PolicyPercentage: 100
          - InfluentialCivs: 3
        
        ## DiplomaticVictory
        - VotesNeeded: 42
        - Status: World Congress - Voting in 4 turns
        - ActiveResolutions:
          - Ban Luxury: Wine:
            - Description: A Luxury resource is designated as immoral, endangered, or otherwise inappropriate for use by the general population. As long as the ban is in place, Civilizations receive no Happiness or Monopoly benefits from this Luxury resource.
            - EnactedOn: -1
          - Dutch Sphere of Influence: Veligrad:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Sanction: Mongolia:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: -1
          - Open Door: Sidon:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - Dutch Sphere of Influence: Shedet:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Dutch Sphere of Influence: Kwa-Bulawayo:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - World Religion: Hinduism:
            - Description: Designate a religion as the official World Religion. Civilizations who have a majority of the cities in their empire following the religion get an additional Delegate. The founder of the religion and/or the controller of its Holy City receives additional votes based on the number of Civilizations following the religion. The religion spreads 25% faster, and its Holy City receives +50% Tourism. There can only be one World Religion at a time.
            - EnactedOn: -1
          - Scholars In Residence:
            - Description: Civilizations have -20% Research cost for Technologies already discovered by another Civilization. Additional -2% for every City-State Ally, up to -50%.
            - EnactedOn: -1
          - Austrian Sphere of Influence: Kyiv:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Austrian Sphere of Influence: Kuala Lumpur:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Dutch Sphere of Influence: Belgrade:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Open Door: Cahokia:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - Endowment for the Arts:
            - Description: Increases up to 33% generation of Great Writers, Artists, and Musicians. Decreases up to 33% generation of Great Scientists, Engineers, and Merchants.
              Civilizations with Scores from Policies and Great Works below the global median will receive a boost to Production and Culture up to 33%.
              Details: The boosts are proportional to the difference between the score of the Civilization and the leader.
            - EnactedOn: -1
        - Proposals:
          - Enact: Sanction: Rome:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - Proposer: The Netherlands
          - Enact: International Games:
            - Description: Begins the International Games project. Once underway, Civilizations can contribute Production towards its completion by selecting it in the city production list. When complete, Civilizations receive bonuses based on how much they contributed.
              : Olympic Village wonder appears in Capital. (Receive +3 Happiness and +3 Culture in the City in which it is built. 25% of the Culture from World Wonders and Tiles is added to the Tourism output of the City. All Stadiums receive +2 Gold and Tourism.)
              : Receive a free Great Person of your choice.
              : Tourism increases by 50% for 20 Turns.
              Available once any Civilization discovers Radio.
            - Proposer: Germany
          - Repeal: Open Door: Cahokia:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - Proposer: Austria
        - Contender: The Netherlands
        - Austria:
          - Delegates: 12
          - VictoryPercentage: 28
        - Germany:
          - Delegates: 18
          - VictoryPercentage: 42
        - Mongolia:
          - Delegates: 5
          - VictoryPercentage: 11
        - Rome:
          - Delegates: 5
          - VictoryPercentage: 11
        - Songhai:
          - Delegates: 8
          - VictoryPercentage: 19
        - The Aztecs:
          - Delegates: 5
          - VictoryPercentage: 11
        - The Netherlands:
          - Delegates: 19
          - VictoryPercentage: 45
        
        # Players
        Players: summary reports about visible players in the world.
        
        ## Player 0
        - Civilization: The Aztecs
        - Leader: Montezuma
        - IsMajor: true
        - OurOpinionToThem:
          - You have denounced one of their declared enemies! (11)
          - Our real approach is War.
          - We have divergent Social Policies. (-3)
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - Your spies were caught stealing from them. (-33)
          - We defeated their proposal in the World Congress. (-36)
          - You are at war! (-99999)
        - TheirOpinionToUs:
          - You have no contested borders.
          - We fought together against a common foe.
          - You have denounced one of their declared enemies!
          - We are completely untrustworthy to them.
          - They have denounced us!
          - You are competing for the favor of the same City-States!
          - They believe your warmongering has become an existential threat. (They are bloodthirsty warmongers!)
          - You made a trade demand of them!
          - You have conquered City-States under their protection!
          - You have denounced a leader they made a Declaration of Friendship with!
          - We have divergent Social Policies.
          - You killed or captured civilians from other civilizations!
          - Their friends or allies have denounced you!
          - They disliked our proposal to the World Congress.
          - Your spies were caught stealing from them.
          - You made a promise not to declare war on them, and then broke it!
          - Your votes opposed their civ's interests in the World Congress.
          - You captured their original capital.
          - You are at war!
        - Score: 737
        - Era: Modern
        - GoldenAge: 10 turns remaining
        - Technologies: 54
        - Cities: 1
        - Population: 10
        - Territory: 22
        - Gold: 1573
        - GoldPerTurn: 97
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 564
        - TourismPerTurn: 0
        - CulturePerTurn: 22
        - PolicyBranches:
          - Statecraft: 6
          - Imperialism: 5
          - Authority: 6
        - ResourcesAvailable:
          - Sheep: 1
          - Paper: 6
          - Cotton: 1
          - Lapis Lazuli: 1
          - Coffee: 1
          - Whales: 1
          - Iron: 3
          - Cattle: 1
          - Copper: 1
          - Truffles: 1
          - Dyes: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Austria:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - Germany:
            - Distance: Close
            - War (Our Score: -100%; Our War Weariness: 7%)
            - Denounced Them
          - Songhai:
            - Distance: Far
            - Open Borders
            - Declaration of Friendship
          - The Netherlands:
            - Distance: Neighbors
            - Our Master (Capitulated)
            - Open Borders
          - Mongolia:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 0%)
          - Rome:
            - Distance: Close
            - War (Our Score: -84%; Our War Weariness: 47%)
            - Denounced Them
        - Votes: 5
        
        ## Player 1
        - Civilization: Rome
        - Leader: Augustus Caesar
        - IsMajor: true
        - OurOpinionToThem:
          - You have denounced one of their declared enemies! (11)
          - Our real approach is War.
          - We have divergent Social Policies. (-3)
          - You killed or captured their civilians! (-9)
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - Religious differences strain your relationship. (-30)
          - We defeated their proposal in the World Congress. (-36)
          - They believe your warmongering has become an existential threat. (-48)
          - Our leader has formed a private opinion to this player (-55).
          - Our leader has expressed a public opinion to this player (-60).
          - You have chosen to adopt the Order Ideology, but they believe in Autocracy. (-999)
          - You are at war! (-99999)
        - TheirOpinionToUs:
          - We passed their proposal in the World Congress.
          - You have denounced one of their declared enemies!
          - You killed or captured their civilians!
          - We have divergent Social Policies.
          - Religious differences strain your relationship.
          - Their friends or allies have denounced you!
          - Your friends found reason to denounce you!
          - They disliked our proposal to the World Congress.
          - You have denounced a leader they made a Declaration of Friendship with!
          - Your spies were caught stealing from them.
          - Territorial disputes strain your relationship.
          - Your success infuriates them.
          - We have denounced each other!
          - They believe your warmongering has become an existential threat. (They strongly dislike warmongers.)
          - Your votes opposed their civ's interests in the World Congress.
          - They believe we are building World Wonders too aggressively!
          - You have chosen to adopt the Autocracy Ideology, but they believe in Order.
          - They believe we are expanding our empire too aggressively!
          - You are at war!
        - Score: 2746
        - Era: Atomic
        - Technologies: 60
        - Cities: 18
        - Population: 433
        - Territory: 471
        - Gold: 6638
        - GoldPerTurn: 1016
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 49
        - MilitaryStrength: 7544
        - TourismPerTurn: 909.75
        - CulturePerTurn: 2043
        - PolicyBranches:
          - Fealty: 6
          - Order: 6
          - Imperialism: 6
          - Authority: 6
        - ResourcesAvailable:
          - Wheat: 8
          - Silver: 1
          - Sheep: 9
          - Cloves: 2
          - Figs: 38
          - Ivory: 1
          - Nutmeg: 3
          - Paper: 4
          - Maize: 3
          - Cotton: 1
          - Salt: 8
          - Aluminum: 14
          - Lapis Lazuli: 1
          - Fish: 1
          - Amber: 1
          - Deer: 12
          - Olives: 1
          - Iron: 4
          - Coffee: 2
          - Cattle: 2
          - Pepper: 3
          - Horses: 6
          - Coral: 1
          - Bison: 4
          - Copper: 3
          - Stone: 5
          - Marble: 1
          - Tobacco: 4
        - FoundedReligion: Buddhism
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - Denounced Them
          - Germany:
            - Distance: Neighbors
            - War (Our Score: -10%; Our War Weariness: 32%)
            - Denounced Them
          - Songhai:
            - Distance: Neighbors
            - War (Our Score: 10%; Our War Weariness: 19%)
            - Denounced Them
          - The Aztecs:
            - Distance: Close
            - War (Our Score: 84%; Our War Weariness: 17%)
          - Mongolia:
            - Distance: Far
            - Declaration of Friendship
          - The Netherlands:
            - Distance: Neighbors
            - War (Our Score: -2%; Our War Weariness: 24%)
            - Denounced Them
        - Votes: 5
        
        ## Player 2
        - Civilization: Germany
        - Leader: Bismarck
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: None, Our top defensive pact ally: None
          - Our top World Congress ally: None, Our top World Congress rival: The Netherlands
          - Our top Competitor: The Netherlands
        - Score: 4509
        - Era: Information
        - GoldenAge: 5 turns remaining
        - Technologies: 68
        - CurrentResearch: Advanced Ballistics (Estimated in 8 turns)
        - NextPolicyTurns: 14
        - Cities: 23
        - Population: 561
        - Territory: 858
        - BestSettlementLocation:
          - 24, 47 (Quality: 0%; 4 tiles from us)
          - 24, 48 (Quality: 0%; 5 tiles from us)
          - 23, 47 (Quality: 0%; 4 tiles from us)
          - 22, 46 (Quality: 0%; 5 tiles from us)
          - 25, 47 (Quality: 0%; 4 tiles from us)
        - Gold: 1591
        - GoldPerTurn: -26
        - HappinessSituation: Happy
        - HappinessPercentage: 64
        - MilitaryUnits: 131
        - MilitarySupply: 149
        - MilitaryStrength: 22682
        - TourismPerTurn: 1719.9
        - CulturePerTurn: 4568
        - FaithPerTurn: 833
        - SciencePerTurn: 4786
        - PolicyBranches:
          - Fealty:
            - Fealty
            - Nobility
          - Autocracy:
            - Elite Forces
            - Military-Industrial Complex
            - United Front
            - New World Order
            - Lightning Warfare
            - Cult of Personality
            - Martial Spirit
          - Tradition:
            - Tradition
            - Justice
            - Sovereignty
            - Ceremony
            - Splendor
            - Majesty
          - Rationalism:
            - Rationalism
            - Scientific Revolution
          - Progress:
            - Progress
          - Industry:
            - Industry
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Consulates
            - Shadow Networks
            - Exchange Markets
            - Trade Confederacy
          - Authority:
            - Authority
            - Imperium
            - Militarism
            - Dominance
        - ResourcesAvailable:
          - Wheat: 8
          - Silver: 0
          - Sheep: 6
          - Cloves: 4
          - Figs: 0
          - Ivory: 2
          - Gold: 0
          - Nutmeg: 0
          - Paper: 16
          - Pearls: 0
          - Maize: 5
          - Rice: 5
          - Cotton: 2
          - Gems: 7
          - Salt: 0
          - Brazilwood: 0
          - Aluminum: 44
          - Glass: 2
          - Lapis Lazuli: 0
          - Fish: 28
          - Amber: 0
          - Perfume: 0
          - Deer: 7
          - Whales: 2
          - Olives: 4
          - Sugar: 0
          - Jade: 0
          - Iron: 9
          - Dyes: 0
          - Tea: 10
          - Coal: -6
          - Coffee: 4
          - Cattle: 2
          - Pepper: 1
          - Uranium: 5
          - Horses: 0
          - Coral: 1
          - Silk: 0
          - Jewelry: 0
          - Bison: 12
          - Antiquity Site: 0
          - Citrus: 0
          - Copper: 1
          - Truffles: 0
          - Crab: 2
          - Incense: 0
          - Stone: 11
          - Marble: 4
          - Furs: 0
          - Cinnamon: 0
          - Bananas: 4
          - Oil: 0
          - Wine: 0
          - Porcelain: 0
          - Cocoa: 0
          - Tobacco: 0
        - FoundedReligion: Protestantism
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - Denounced Them
          - Mongolia:
            - Distance: Close
            - Denounced Them
          - Songhai:
            - Distance: Close
            - Peace Treaty
          - The Aztecs:
            - Distance: Close
            - War (Our Score: 100%; Our War Weariness: 0%)
          - The Netherlands:
            - Distance: Neighbors
            - War (Our Score: 8%; Our War Weariness: 0%)
            - Denounced Them
          - Rome:
            - Distance: Neighbors
            - War (Our Score: 10%; Our War Weariness: 25%)
            - Denounced Them
        - OutgoingTradeRoutes:
          - Berlin (Germany) => Teotihuacan (Germany):
            - TurnsLeft: 16
            - Domain: Land
            - ToProduction: 31
          - Berlin (Germany) => Calixtlahuaca (Germany):
            - ToFood: 45.48
            - TurnsLeft: 21
            - Domain: Land
          - Munich (Germany) => M'banza-Kongo (City-State Cahokia):
            - TurnsLeft: 11
            - Domain: Land
            - FromGold: 39.69
          - Regensburg (Germany) => Mataram (City-State Ouagadougou):
            - TurnsLeft: 9
            - FromScience: 8.75
            - Domain: Sea
            - FromGold: 46.28
            - FromCulture: 8.75
          - Munich (Germany) => Turfan (City-State Kyiv):
            - TurnsLeft: 2
            - Domain: Sea
            - FromGold: 34.69
          - Available: 7
          - Berlin (Germany) => Munich (Germany):
            - TurnsLeft: 10
            - Domain: Land
            - ToProduction: 30
          - Dortmund (Germany) => Sidon (City-State Sidon):
            - TurnsLeft: 51
            - Domain: Sea
            - FromGold: 34.17
          - Berlin (Germany) => Bremen (Germany):
            - ToFood: 41.25
            - TurnsLeft: 24
            - Domain: Land
        - Spies:
          - Agent Horst (10):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 816
            - Location: Rotterdam (The Netherlands)
            - NetworkPerTurn: 55
          - Agent Conrad (5):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 60
            - Location: Tzintzuntzen (The Netherlands)
            - NetworkPerTurn: 60
          - Agent Hanna (2):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 980
            - Location: Gao (Songhai)
            - NetworkPerTurn: 60
          - Agent Anton (7):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 791
            - Location: Tondibi (Songhai)
            - NetworkPerTurn: 57
          - Agent Johann (4):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 600
            - Location: Amsterdam (The Netherlands)
            - NetworkPerTurn: 60
          - Agent Theodor (9):
            - State: Unassigned
            - Role: Vassal Diplomat
            - Location: Unassigned
            - NetworkPerTurn: 0
          - Agent Wolfgang (6):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 60
            - Location: Tlacopan (The Netherlands)
            - NetworkPerTurn: 60
          - Agent Marlene (11):
            - State: Traveling
            - Role: Spy
            - Location: Rome (Rome)
            - NetworkPerTurn: 0
          - Agent Elke (3):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 652
            - Location: Utrecht (The Netherlands)
            - NetworkPerTurn: 58
          - Agent Wilhelm (12):
            - State: Traveling
            - Role: Spy
            - Location: Mediolanum (Rome)
            - NetworkPerTurn: 0
          - Agent Gerhard (1):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 470
            - Location: Old Sarai (The Netherlands)
            - NetworkPerTurn: 60
          - Agent Schimanski (8):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 0
            - Location: Atzcapotzalco (The Netherlands)
            - NetworkPerTurn: 60
        - DiplomaticDeals:
          - Austria:
            - #0:
              - WeGive:
                - 1 Ivory
              - TurnsRemaining: 0
            - #1:
              - WeGive:
                - 17 Gold per Turn
              - TheyGive:
                - 1 Coal
              - TurnsRemaining: 8
            - #2:
              - WeGive:
                - 1 Crab
              - TheyGive:
                - 9 Gold per Turn
              - TurnsRemaining: 19
            - #3:
              - WeGive:
                - Defensive Pact
              - TheyGive:
                - Defensive Pact
                - 15 Gold per Turn
              - TurnsRemaining: 21
          - Songhai:
            - #0:
              - WeGive:
                - Peace Treaty
              - TheyGive:
                - Peace Treaty
                - Make Peace with City-State Ouagadougou
              - TurnsRemaining: 10
        - Votes: 18
        - 3: Defeated Major Civilization Indonesia
        
        ## Player 4
        - Civilization: Songhai
        - Leader: Askia
        - IsMajor: true
        - OurOpinionToThem:
          - You have denounced one of their declared enemies! (11)
          - We have similar Social Policies. (3)
          - Our real approach is Guarded.
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - You have made a Defensive Pact with one of their enemies! (-15)
          - Religious differences strain your relationship. (-30)
          - Your spies were caught stealing from them. (-33)
          - We defeated their proposal in the World Congress. (-36)
          - Our leader has expressed a public opinion to this player (-100).
          - Our leader has formed a private opinion to this player (-100).
          - You have chosen to adopt the Order Ideology, but they believe in Autocracy. (-999)
        - TheirOpinionToUs:
          - You have denounced one of their declared enemies!
          - We have similar Social Policies.
          - You have shared intrigue with them.
          - You have no contested borders.
          - You have gone to war in the past.
          - We are completely untrustworthy to them.
          - They have denounced us!
          - They suspect we might be a threat to them.
          - Your recent diplomatic actions disappoint them.
          - Religious differences strain your relationship.
          - They are jealous of our superior technology!
          - You killed or captured civilians from other civilizations!
          - They believe we are building World Wonders too aggressively!
          - Your spies were caught stealing from them.
          - They disliked our proposal to the World Congress.
          - You made a promise not to declare war on another civilization, and then broke it!
          - Their friends or allies have denounced you!
          - Your votes opposed their civ's interests in the World Congress.
          - You have denounced a leader they made a Declaration of Friendship with!
          - They believe your warmongering has become an existential threat. (They strongly dislike warmongers.)
          - The leader has expressed a public opinion to you (-85).
          - You have chosen to adopt the Autocracy Ideology, but they believe in Order.
        - Score: 1541
        - Era: Modern
        - Technologies: 58
        - Cities: 7
        - Population: 122
        - Territory: 213
        - Gold: 839
        - GoldPerTurn: 21
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 2552
        - TourismPerTurn: 288.75
        - CulturePerTurn: 742
        - PolicyBranches:
          - Tradition: 2
          - Rationalism: 4
          - Imperialism: 1
          - Authority: 5
          - Fealty: 1
          - Artistry: 1
          - Statecraft: 2
          - Order: 1
          - Progress: 2
        - ResourcesAvailable:
          - Sheep: 8
          - Figs: 1
          - Paper: 4
          - Rice: 1
          - Cotton: 1
          - Aluminum: 7
          - Maize: 1
          - Lapis Lazuli: 3
          - Coffee: 1
          - Deer: 1
          - Olives: 1
          - Iron: 5
          - Cattle: 3
          - Horses: 1
          - Bison: 1
          - Truffles: 2
          - Dyes: 1
          - Bananas: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Germany:
            - Distance: Close
            - Peace Treaty
            - Denounced Them
          - The Aztecs:
            - Distance: Far
            - Open Borders
            - Declaration of Friendship
          - Mongolia:
            - Distance: Neighbors
            - War (Our Score: 100%; Our War Weariness: 53%)
            - Denounced Them
          - The Netherlands:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Rome:
            - Distance: Neighbors
            - War (Our Score: -10%; Our War Weariness: 35%)
            - Denounced Them
        - Votes: 8
        
        ## Player 5
        - Civilization: Austria
        - Leader: Maria Theresa
        - IsMajor: true
        - OurOpinionToThem:
          - Our leader has expressed a public opinion to this player (100).
          - Our leader has formed a private opinion to this player (100).
          - We are trade partners. (40)
          - You have denounced one of their declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - Our real approach is Hostile.
          - We are completely untrustworthy to them.
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - Religious differences strain your relationship. (-30)
          - We defeated their proposal in the World Congress. (-36)
          - You have chosen to adopt the Freedom Ideology, but they believe in Autocracy. (-999)
        - TheirOpinionToUs:
          - The leader has expressed a public opinion to you (30).
          - You have denounced one of their declared enemies!
          - We have Pledged to Protect the same City-States.
          - We have similar Social Policies.
          - You have shared intrigue with them.
          - They don't want anything to do with us right now.
          - You plundered their trade routes!
          - Religious differences strain your relationship.
          - Your military deployment is threatening.
          - Territorial disputes strain your relationship.
          - You killed or captured civilians from other civilizations!
          - You are competing for the favor of the same City-States!
          - Their friends or allies have denounced you!
          - They believe we are building World Wonders too aggressively!
          - They believe we are expanding our empire too aggressively!
          - We have denounced each other!
          - They disliked our proposal to the World Congress.
          - They believe your warmongering has become an existential threat. (They strongly dislike warmongers.)
          - You have chosen to adopt the Autocracy Ideology, but they believe in Freedom.
          - Your votes opposed their civ's interests in the World Congress.
        - Score: 1319
        - Era: Modern
        - GoldenAge: 1 turns remaining
        - Technologies: 52
        - Cities: 3
        - Population: 73
        - Territory: 68
        - Gold: 1030
        - GoldPerTurn: 307
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 1840
        - TourismPerTurn: 266
        - CulturePerTurn: 1018
        - PolicyBranches:
          - Freedom: 1
          - Tradition: 5
          - Artistry: 5
          - Statecraft: 5
          - Rationalism: 1
          - Industry: 1
          - Progress: 2
        - ResourcesAvailable:
          - Ivory: 1
          - Paper: 6
          - Rice: 2
          - Cotton: 4
          - Lapis Lazuli: 1
          - Coffee: 3
          - Iron: 1
          - Coal: 3
          - Cattle: 2
          - Horses: 7
          - Copper: 1
          - Truffles: 1
          - Crab: 1
          - Dyes: 1
          - Oil: 6
          - Bananas: 3
          - Wine: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Rome:
            - Distance: Neighbors
            - Denounced Them
          - Germany:
            - Distance: Neighbors
            - Denounced Them
          - Songhai:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - The Aztecs:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - Mongolia:
            - Distance: Close
            - War (Our Score: 100%; Our War Weariness: 62%)
            - Denounced Them
          - The Netherlands:
            - Distance: Close
            - Open Borders
        - Votes: 12
        
        ## Player 6
        - Civilization: The Netherlands
        - Leader: William
        - IsMajor: true
        - OurOpinionToThem:
          - You have denounced one of their declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - Our real approach is War.
          - Religious differences strain your relationship. (-30)
          - Your spies were caught stealing from them. (-33)
          - We defeated their proposal in the World Congress. (-36)
          - Our leader has expressed a public opinion to this player (-100).
          - Our leader has formed a private opinion to this player (-100).
          - You have chosen to adopt the Order Ideology, but they believe in Autocracy. (-999)
          - You are at war! (-99999)
        - TheirOpinionToUs:
          - You have denounced one of their declared enemies!
          - We have similar Social Policies.
          - We have Pledged to Protect the same City-States.
          - You have no contested borders.
          - We are completely untrustworthy to them.
          - You are competing for World Wonders.
          - Religious differences strain your relationship.
          - They believe we are building World Wonders too aggressively!
          - You have conquered City-States under their protection!
          - You are competing for the favor of the same City-States!
          - They disliked our proposal to the World Congress.
          - You made a promise not to declare war on another civilization, and then broke it!
          - Their friends or allies have denounced you!
          - You killed or captured their civilians!
          - We have denounced each other!
          - The leader has expressed a public opinion to you (-100).
          - You have chosen to adopt the Autocracy Ideology, but they believe in Order.
          - They believe we are expanding our empire too aggressively!
          - Your votes opposed their civ's interests in the World Congress.
          - They believe your warmongering has become an existential threat. (They hate warmongers!)
          - You are at war!
        - Score: 2248
        - Era: Atomic
        - Technologies: 60
        - Cities: 11
        - Population: 234
        - Territory: 296
        - Gold: 1896
        - GoldPerTurn: 440
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 49
        - MilitaryStrength: 3495
        - TourismPerTurn: 450.25
        - CulturePerTurn: 1218
        - PolicyBranches:
          - Fealty: 1
          - Order: 3
          - Tradition: 2
          - Rationalism: 1
          - Statecraft: 6
          - Imperialism: 1
          - Industry: 2
          - Progress: 6
        - ResourcesAvailable:
          - Wheat: 1
          - Sheep: 3
          - Figs: 1
          - Ivory: 1
          - Pearls: 1
          - Paper: 6
          - Rice: 1
          - Cotton: 1
          - Gems: 1
          - Aluminum: 9
          - Maize: 4
          - Glass: 1
          - Lapis Lazuli: 1
          - Amber: 1
          - Coffee: 2
          - Deer: 3
          - Whales: 1
          - Iron: 1
          - Coal: 8
          - Cattle: 3
          - Marble: 1
          - Horses: 2
          - Coral: 3
          - Fish: 11
          - Bison: 1
          - Copper: 2
          - Truffles: 6
          - Stone: 4
          - Crab: 1
          - Dyes: 1
          - Oil: 1
          - Bananas: 3
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Rome:
            - Distance: Neighbors
            - War (Our Score: 2%; Our War Weariness: 34%)
            - Denounced Them
          - Germany:
            - Distance: Neighbors
            - War (Our Score: -8%; Our War Weariness: 7%)
            - Denounced Them
          - Songhai:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - The Aztecs:
            - Distance: Neighbors
            - Our Vassal (Capitulated)
            - Open Borders
          - Mongolia:
            - Distance: Neighbors
            - War (Our Score: 24%; Our War Weariness: 3%)
            - Denounced Them
          - Austria:
            - Distance: Close
            - Open Borders
        - Votes: 19
        
        ## Player 7
        - Civilization: Mongolia
        - Leader: Genghis Khan
        - IsMajor: true
        - OurOpinionToThem:
          - Our leader has expressed a public opinion to this player (100).
          - Our leader has formed a private opinion to this player (100).
          - You have denounced one of their declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - We fought together against a common foe. (1)
          - Our real approach is Hostile.
          - We are completely untrustworthy to them.
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - Religious differences strain your relationship. (-30)
          - Your spies were caught stealing from them. (-33)
          - We defeated their proposal in the World Congress. (-36)
        - TheirOpinionToUs:
          - The leader has expressed a public opinion to you (100).
          - You have denounced one of their declared enemies!
          - We have Pledged to Protect the same City-States.
          - We have similar Social Policies.
          - You have shared intrigue with them.
          - We fought together against a common foe.
          - You have no contested borders.
          - You have been at war in the past, but they do not seem to hold a grudge.
          - We are completely untrustworthy to them.
          - They fear our great might!
          - They believe we are building World Wonders too aggressively!
          - They believe your warmongering has become an existential threat. (They overlook modest warmongering.)
          - Religious differences strain your relationship.
          - Their friends or allies have denounced you!
          - Your spies were caught stealing from them.
          - You are competing for the favor of the same City-States!
          - We have denounced each other!
          - They disliked our proposal to the World Congress.
          - You have denounced a leader they made a Declaration of Friendship with!
          - Your votes opposed their civ's interests in the World Congress.
        - Score: 798
        - Era: Industrial
        - Technologies: 42
        - Cities: 2
        - Population: 48
        - Territory: 74
        - Gold: 842
        - GoldPerTurn: 6
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 44
        - MilitaryStrength: 386
        - TourismPerTurn: 34
        - CulturePerTurn: 124
        - PolicyBranches:
          - Progress: 2
          - Statecraft: 5
          - Fealty: 3
          - Authority: 5
        - ResourcesAvailable:
          - Wheat: 1
          - Ivory: 1
          - Paper: 3
          - Maize: 1
          - Deer: 1
          - Whales: 2
          - Horses: 2
          - Stone: 1
          - Wine: 3
        - FoundedReligion: Tengriism
        - Relationships:
          - Rome:
            - Distance: Far
            - Declaration of Friendship
          - Germany:
            - Distance: Close
            - Denounced Them
          - Songhai:
            - Distance: Neighbors
            - War (Our Score: -100%; Our War Weariness: 100%)
          - The Aztecs:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 0%)
          - The Netherlands:
            - Distance: Neighbors
            - War (Our Score: -24%; Our War Weariness: 12%)
            - Denounced Them
          - Austria:
            - Distance: Close
            - War (Our Score: -100%; Our War Weariness: 99%)
        - Votes: 5
        
        ## Player 22
        - Civilization: Ouagadougou
        - Leader: City State
        - MajorAlly: Germany
        - Population: 28
        - ResourcesAvailable:
          - Fish: 4
          - Deer: 3
          - Sheep: 1
        - MajorityReligion: Protestantism
        - Relationships:
          - Rome: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Germany: Ally (Influence: 701, Distance: Far, Protected)
          - Songhai: Neutral (Influence: -58, Distance: Distant)
          - The Aztecs: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Mongolia: Neutral (Influence: -58, Distance: Distant)
          - The Netherlands: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Austria: Friends (Influence: 185, Distance: Distant, Protected)
        - Quests:
          -  They will reward the player that destroys a nearby Barbarian Encampment. Potential Quest Reward: * 178 Influence * 213 Great General Points
          - They want you to defeat Barbarian units that are invading their territory. You are allowed to enter their territory until the Barbarians are defeated.
        - 23: Defeated Minor Civilization Ecbatana
        
        ## Player 24
        - Civilization: Veligrad
        - Leader: City State
        - MajorAlly: The Netherlands
        - Population: 20
        - ResourcesAvailable:
          - Bananas: 1
          - Fish: 3
        - MajorityReligion: Hinduism
        - Relationships:
          - Rome: War (Influence: -60, Distance: Far)
          - Germany: War (Influence: -60, Distance: Far)
          - Songhai: Neutral (Influence: -31, Distance: Neighbors)
          - The Aztecs: Neutral (Influence: 0, Distance: Far)
          - Mongolia: War (Influence: -60, Distance: Distant)
          - The Netherlands: Ally (Influence: 160, Distance: Neighbors, Protected)
          - Austria: Friends (Influence: 86, Distance: Far)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 25
        - Civilization: Kyiv
        - Leader: City State
        - MajorAlly: Austria
        - Population: 38
        - ResourcesAvailable:
          - Fish: 1
          - Stone: 1
          - Bananas: 1
        - MajorityReligion: Protestantism
        - Relationships:
          - Rome: Neutral (Influence: -20, Distance: Close)
          - Germany: Friends (Influence: 118, Distance: Neighbors, Protected)
          - Songhai: Neutral (Influence: 0, Distance: Close)
          - The Aztecs: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: War (Influence: -60, Distance: Neighbors)
          - The Netherlands: Friends (Influence: 67, Distance: Close, Protected)
          - Austria: Ally (Influence: 415, Distance: Neighbors, Protected)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 26
        - Civilization: Belgrade
        - Leader: City State
        - MajorAlly: The Netherlands
        - Population: 24
        - ResourcesAvailable:
          - Fish: 1
        - MajorityReligion: Hinduism
        - Relationships:
          - Rome: War (Influence: -60, Distance: Close)
          - Germany: War (Influence: -60, Distance: Far)
          - Songhai: Friends (Influence: 41, Distance: Neighbors)
          - The Aztecs: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: War (Influence: -60, Distance: Close)
          - The Netherlands: Ally (Influence: 270, Distance: Neighbors, Protected)
          - Austria: Friends (Influence: 70, Distance: Close)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 27
        - Civilization: Sidon
        - Leader: City State
        - Population: 18
        - ResourcesAvailable:
          - Fish: 2
          - Bison: 1
          - Silver: 1
          - Horses: 2
        - Relationships:
          - Rome: Neutral (Influence: -20, Distance: Distant)
          - Germany: Friends (Influence: 171, Distance: Close, Protected)
          - Songhai: Friends (Influence: 44, Distance: Far)
          - The Aztecs: Friends (Influence: 44, Distance: Distant)
          - Mongolia: Neutral (Influence: 29, Distance: Neighbors, Protected)
          - The Netherlands: Friends (Influence: 58, Distance: Neighbors, Protected)
          - Austria: Friends (Influence: 56, Distance: Far)
        - Quests:
          -  They will reward the player(s) with the largest number of new Followers. So far, the leader has 26 new Followers and you have 13 (Turns remaining: 23) Potential Quest Reward: * 224 Influence * 197 Great Person Points in all Cities
          - Acquire the city of Beshbalik. (Turns remaining: 45) Potential Quest Reward: * 528 Influence * 1 Juggernaut Unit(165 Bonus XP)
          - They want Protestantism to become the majority religion in their city. (Turns remaining: 8) Potential Quest Reward: * 227 Influence * 294 Faith
        - 28: Defeated Minor Civilization M'banza-Kongo
        
        ## Player 29
        - Civilization: Shedet
        - Leader: City State
        - MajorAlly: The Netherlands
        - Population: 20
        - ResourcesAvailable:
          - Fish: 2
          - Maize: 1
        - MajorityReligion: Protestantism
        - Relationships:
          - Rome: War (Influence: -60, Distance: Distant)
          - Germany: War (Influence: -60, Distance: Neighbors)
          - Songhai: Neutral (Influence: 22, Distance: Distant)
          - The Aztecs: Friends (Influence: 44, Distance: Distant)
          - Mongolia: War (Influence: -60, Distance: Distant)
          - The Netherlands: Ally (Influence: 145, Distance: Close, Protected)
          - Austria: Friends (Influence: 378, Distance: Distant)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 30
        - Civilization: Cahokia
        - Leader: City State
        - Population: 37
        - ResourcesAvailable:
          - Stone: 1
          - Pearls: 1
          - Rice: 1
          - Coral: 1
          - Jewelry: 1
          - Coal: 6
          - Fish: 6
        - MajorityReligion: Protestantism
        - Relationships:
          - Rome: Friends (Influence: 36, Distance: Far)
          - Germany: Friends (Influence: 242, Distance: Neighbors, Protected)
          - Songhai: Neutral (Influence: 0, Distance: Distant)
          - The Aztecs: Friends (Influence: 41, Distance: Far)
          - Mongolia: Neutral (Influence: 0, Distance: Distant)
          - The Netherlands: Neutral (Influence: 5, Distance: Far, Protected)
          - Austria: Neutral (Influence: 0, Distance: Far)
        - Quests:
          -  They will reward the player with the highest Tourism per turn. So far, you have the lead with 1,719 per turn. (Turns remaining: 4) Potential Quest Reward: * 353 Influence * 563 Culture
          - They want you to liberate the city of Ecbatana. (Turns remaining: 33) Potential Quest Reward: * 297 Influence * 4 Happiness in Capital
          - Conduct a Spy Mission against Maria Theresa. Potential Quest Reward: * 430 Influence * 1,060 Science
          - They want you to defeat Barbarian units that are invading their territory. You are allowed to enter their territory until the Barbarians are defeated.
        - 31: Defeated Minor Civilization Seoul
        
        ## Player 32
        - Civilization: Kwa-Bulawayo
        - Leader: City State
        - MajorAlly: The Netherlands
        - Population: 23
        - ResourcesAvailable:
          - Deer: 1
          - Fish: 4
        - Relationships:
          - Rome: War (Influence: -60, Distance: Far)
          - Germany: War (Influence: -60, Distance: Close)
          - Songhai: Neutral (Influence: 0, Distance: Close)
          - The Aztecs: Neutral (Influence: 0, Distance: Far)
          - Mongolia: War (Influence: -60, Distance: Far)
          - The Netherlands: Ally (Influence: 64, Distance: Neighbors, Protected)
          - Austria: Neutral (Influence: 0, Distance: Far)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        - 33: Defeated Minor Civilization Zurich
        - 34: Defeated Minor Civilization Valletta
        
        ## Player 35
        - Civilization: Ormus
        - Leader: City State
        - MajorAlly: The Netherlands
        - Population: 30
        - ResourcesAvailable:
          - Cattle: 2
          - Fish: 7
          - Sheep: 1
        - MajorityReligion: Protestantism
        - Relationships:
          - Rome: War (Influence: -60, Distance: Far)
          - Germany: War (Influence: -60, Distance: Neighbors)
          - Songhai: War (Influence: -60, Distance: Close)
          - The Aztecs: Neutral (Influence: -48, Distance: Close)
          - Mongolia: War (Influence: -60, Distance: Distant)
          - The Netherlands: Ally (Influence: 385, Distance: Neighbors, Protected)
          - Austria: Friends (Influence: 86, Distance: Distant)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        - 36: Defeated Minor Civilization Ban Chiang
        
        ## Player 37
        - Civilization: Kuala Lumpur
        - Leader: City State
        - MajorAlly: Austria
        - Population: 12
        - ResourcesAvailable:
          - Sheep: 2
        - MajorityReligion: Hinduism
        - Relationships:
          - Rome: Friends (Influence: 36, Distance: Close)
          - Germany: Friends (Influence: 92, Distance: Close, Protected)
          - Songhai: Neutral (Influence: 0, Distance: Neighbors)
          - The Aztecs: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: War (Influence: -60, Distance: Neighbors)
          - The Netherlands: Friends (Influence: 393, Distance: Close)
          - Austria: Ally (Influence: 413, Distance: Neighbors, Protected)
        - Quests:
          -  Conduct a Spy Mission against William. Potential Quest Reward: * 405 Influence * 999 Science
          - They want you to send them an Infantry with at least 90 XP. (Turns remaining: 48) Potential Quest Reward: * 191 Influence * 422 Gold
        - 63: Barbarians
        
        # Cities
        Cities: summary reports about discovered cities in the world.
        
        ## Player: The Aztecs
        
        ### Texcoco
        - ID: 14749
        - X: 28
        - Y: 22
        - Population: 10
        - DefenseStrength: 38
        - IsCoastal: true
        
        ## Player: Rome
        
        ### Rome
        - ID: 1058
        - X: 52
        - Y: 7
        - Population: 38
        - MajorityReligion: Buddhism
        - DefenseStrength: 70
        - Wonders:
          - School of Philosophy
          - National Monument
          - Ironworks
          - Imperial College
          - Kremlin
          - Terracotta Army
          - Scrivener's Office
          - Printing Press
          - Palace of Culture and Science
          - Fornix
          - Holy Council
          - Trader Sid's Headquarters
        
        ### Antium
        - ID: 1295
        - X: 56
        - Y: 10
        - Population: 32
        - MajorityReligion: Hinduism
        - DefenseStrength: 75
        - Wonders:
          - Royal Collection
        
        ### Cumae
        - ID: 1536
        - X: 53
        - Y: 16
        - Population: 27
        - MajorityReligion: Hinduism
        - DefenseStrength: 68
        - Wonders:
          - Chartered Company
        
        ### Neapolis
        - ID: 2078
        - X: 56
        - Y: 20
        - Population: 28
        - MajorityReligion: Hinduism
        - DefenseStrength: 77
        
        ### Ravenna
        - ID: 2343
        - X: 60
        - Y: 8
        - Population: 25
        - MajorityReligion: Hinduism
        - DefenseStrength: 79
        
        ### Arretium
        - ID: 2527
        - X: 52
        - Y: 11
        - Population: 26
        - MajorityReligion: Hinduism
        - DefenseStrength: 77
        - Wonders:
          - Grand Temple
        
        ### Mediolanum
        - ID: 2920
        - X: 49
        - Y: 5
        - Population: 24
        - MajorityReligion: Hinduism
        - DefenseStrength: 77
        - IsCoastal: true
        
        ### Arpinum
        - ID: 3200
        - X: 47
        - Y: 11
        - Population: 29
        - MajorityReligion: Hinduism
        - DefenseStrength: 71
        - IsCoastal: true
        - Wonders:
          - Circus Maximus
          - Fornix
        
        ### Circei
        - ID: 3446
        - X: 56
        - Y: 4
        - Population: 26
        - MajorityReligion: Hinduism
        - DefenseStrength: 77
        - Wonders:
          - Brandenburg Gate
          - Fornix
        
        ### Batam
        - ID: 4800
        - X: 58
        - Y: 13
        - Population: 27
        - MajorityReligion: Hinduism
        - DefenseStrength: 46
        - IsOccupied: true
        
        ### Salzburg
        - ID: 6669
        - X: 59
        - Y: 17
        - Population: 27
        - MajorityReligion: Hinduism
        - DefenseStrength: 77
        - IsOccupied: true
        - Wonders:
          - Red Fort
        
        ### Jakarta
        - ID: 10252
        - X: 63
        - Y: 12
        - Population: 25
        - MajorityReligion: Hinduism
        - DefenseStrength: 73
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Uffizi
        
        ### Surabaya
        - ID: 10721
        - X: 64
        - Y: 17
        - Population: 20
        - MajorityReligion: Hinduism
        - DefenseStrength: 73
        - IsOccupied: true
        - IsCoastal: true
        
        ### Ban Chiang
        - ID: 14864
        - X: 59
        - Y: 3
        - Population: 16
        - MajorityReligion: Hinduism
        - DefenseStrength: 75
        - IsOccupied: true
        
        ### Ecbatana
        - ID: 14865
        - X: 64
        - Y: 4
        - Population: 15
        - MajorityReligion: Hinduism
        - DefenseStrength: 71
        - IsOccupied: true
        - IsCoastal: true
        
        ### Makassar
        - ID: 15485
        - X: 65
        - Y: 9
        - Population: 19
        - MajorityReligion: Hinduism
        - DefenseStrength: 59
        - IsOccupied: true
        - IsCoastal: true
        
        ### Denpasar
        - ID: 16906
        - X: 68
        - Y: 4
        - Population: 20
        - MajorityReligion: Hinduism
        - DefenseStrength: 63
        - Health: 50%
        - IsOccupied: true
        - IsCoastal: true
        - ResistanceTurns: 3
        - Wonders:
          - Forbidden Palace
        
        ### Satricum
        - ID: 16908
        - X: 27
        - Y: 8
        - Population: 9
        - MajorityReligion: Buddhism
        - DefenseStrength: 30
        - Health: 50%
        - IsCoastal: true
        
        ## Player: Germany
        
        ### Berlin
        - ID: 1059
        - X: 14
        - Y: 39
        - Population: 47
        - MajorityReligion: Protestantism
        - DefenseStrength: 109
        - FoodStored: 5146
        - FoodPerTurn: 344
        - ProductionPerTurn: 602
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 614
        - SciencePerTurn: 610
        - CulturePerTurn: 658
        - FaithPerTurn: 173
        - TourismPerTurn: 317.75
        - HappinessDelta: 115
        - BuildingCount: 47
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Observatory
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
          - Recycling Center
          - Police Station
          - Hanse
          - Writers' Guild
          - Artists' Guild
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Refinery
          - Brewhouse
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - Chartered Company
          - Ironworks
          - Imperial College
          - Stonehenge
          - Pyramids
          - Great Wall
          - Chichen Itza
          - Notre Dame
          - Himeji Castle
          - Sistine Chapel
          - Palace of Westminster
          - Eiffel Tower
          - Statue of Zeus
          - Temple of Artemis
          - Mausoleum of Halicarnassus
          - Leaning Tower of Pisa
          - Petra
          - Globe Theatre
          - Foreign Bureau
          - Summer Palace
          - Soho Foundry
          - The Motherland Calls
          - Empire State Building
          - Grand Canal
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
          - Great Altar
          - TwoKay Foods Headquarters
        - GreatWorkCount: 14
        
        ### Hamburg
        - ID: 1193
        - X: 9
        - Y: 39
        - Population: 31
        - MajorityReligion: Protestantism
        - DefenseStrength: 72
        - IsCoastal: true
        - FoodStored: 1764
        - FoodPerTurn: 35
        - ProductionPerTurn: 373
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 262
        - SciencePerTurn: 305
        - CulturePerTurn: 223
        - FaithPerTurn: 45
        - TourismPerTurn: 142.25
        - HappinessDelta: -2
        - BuildingCount: 59
        - ImportantBuildings:
          - Seaport
          - Stable
          - Observatory
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
          - Police Station
          - Hanse
          - Writers' Guild
          - Artists' Guild
          - Hotel
          - Caravansary
          - Airport
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Refinery
          - Brewhouse
        - Wonders:
          - National Monument
          - Colossus
          - Angkor Wat
        - GreatWorkCount: 6
        
        ### Munich
        - ID: 1927
        - X: 11
        - Y: 46
        - Population: 29
        - MajorityReligion: Protestantism
        - DefenseStrength: 101
        - IsCoastal: true
        - FoodStored: 1445
        - FoodPerTurn: 30
        - ProductionPerTurn: 428
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 333
        - SciencePerTurn: 296
        - CulturePerTurn: 233
        - FaithPerTurn: 38
        - TourismPerTurn: 150.75
        - HappinessDelta: 2
        - BuildingCount: 58
        - ImportantBuildings:
          - Seaport
          - Water Mill
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Hospital
          - Factory
          - Stock Exchange
          - Research Lab
          - Recycling Center
          - Police Station
          - Hanse
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Refinery
          - Brewhouse
        - Wonders:
          - Circus Maximus
          - Scrivener's Office
          - Printing Press
          - Hall of Honor
        - GreatWorkCount: 6
        
        ### Cologne
        - ID: 2191
        - X: 7
        - Y: 34
        - Population: 31
        - MajorityReligion: Protestantism
        - DefenseStrength: 103
        - IsCoastal: true
        - FoodStored: 1550
        - FoodPerTurn: 30
        - ProductionPerTurn: 401
        - CurrentProduction: Infinite Project: Arts
        - GoldPerTurn: 295
        - SciencePerTurn: 221
        - CulturePerTurn: 293
        - FaithPerTurn: 44
        - TourismPerTurn: 133
        - BuildingCount: 59
        - ImportantBuildings:
          - Seaport
          - Observatory
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
          - Police Station
          - Hanse
          - Artists' Guild
          - Hotel
          - Caravansary
          - Airport
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Brewhouse
        - Wonders:
          - Neuschwanstein
          - Grand Temple
        - GreatWorkCount: 6
        
        ### Frankfurt
        - ID: 3319
        - X: 1
        - Y: 35
        - Population: 26
        - MajorityReligion: Protestantism
        - DefenseStrength: 63
        - IsCoastal: true
        - FoodStored: 1131
        - FoodPerTurn: 63
        - ProductionPerTurn: 277
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 243
        - SciencePerTurn: 237
        - CulturePerTurn: 249
        - FaithPerTurn: 29
        - TourismPerTurn: 180.75
        - HappinessDelta: 5
        - BuildingCount: 56
        - ImportantBuildings:
          - Seaport
          - Stable
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Hospital
          - Factory
          - Stock Exchange
          - Research Lab
          - Police Station
          - Hanse
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Airport
          - Bastion Fort
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Brewhouse
        - Wonders:
          - Royal Collection
          - Prora
        - GreatWorkCount: 9
        
        ### Aachen
        - ID: 3320
        - X: 11
        - Y: 32
        - Population: 25
        - MajorityReligion: Protestantism
        - DefenseStrength: 61
        - IsCoastal: true
        - FoodStored: 692
        - FoodPerTurn: 6
        - ProductionPerTurn: 359
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 193
        - SciencePerTurn: 281
        - CulturePerTurn: 164
        - FaithPerTurn: 33
        - TourismPerTurn: 101.75
        - HappinessDelta: 0
        - BuildingCount: 56
        - ImportantBuildings:
          - Seaport
          - Stable
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Hospital
          - Factory
          - Stock Exchange
          - Research Lab
          - Recycling Center
          - Police Station
          - Hanse
          - Writers' Guild
          - Hotel
          - Caravansary
          - Airport
          - Bastion Fort
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Brewhouse
        - GreatWorkCount: 5
        
        ### Dortmund
        - ID: 3783
        - X: 18
        - Y: 37
        - Population: 25
        - MajorityReligion: Protestantism
        - DefenseStrength: 32
        - IsCoastal: true
        - FoodStored: 1388
        - FoodPerTurn: 6
        - ProductionPerTurn: 177
        - CurrentProduction: Infinite Project: Arts
        - GoldPerTurn: 231
        - SciencePerTurn: 151
        - CulturePerTurn: 216
        - FaithPerTurn: 26
        - TourismPerTurn: 90.75
        - HappinessDelta: 3
        - BuildingCount: 52
        - ImportantBuildings:
          - Seaport
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Workshop
          - Stock Exchange
          - Research Lab
          - Police Station
          - Hanse
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Airport
          - Grocer
          - Bastion Fort
          - Wire Service
          - Brewhouse
        - GreatWorkCount: 4
        
        ### Stuttgart
        - ID: 4072
        - X: 8
        - Y: 49
        - Population: 22
        - MajorityReligion: Protestantism
        - DefenseStrength: 92
        - IsCoastal: true
        - FoodStored: 628
        - FoodPerTurn: 6
        - ProductionPerTurn: 375
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 128
        - SciencePerTurn: 306
        - CulturePerTurn: 154
        - FaithPerTurn: 37
        - TourismPerTurn: 119.5
        - HappinessDelta: 1
        - BuildingCount: 56
        - ImportantBuildings:
          - Seaport
          - Observatory
          - Garden
          - Stadium
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Factory
          - Stock Exchange
          - Research Lab
          - Shrine
          - Police Station
          - Hanse
          - Hotel
          - Caravansary
          - Airport
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Refinery
          - Brewhouse
        - Wonders:
          - Cristo Redentor
        - GreatWorkCount: 4
        
        ### Dusseldorf
        - ID: 4222
        - X: 8
        - Y: 43
        - Population: 25
        - MajorityReligion: Protestantism
        - DefenseStrength: 103
        - IsCoastal: true
        - FoodStored: 898
        - FoodPerTurn: -7
        - ProductionPerTurn: 316
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 142
        - SciencePerTurn: 262
        - CulturePerTurn: 140
        - FaithPerTurn: 43
        - TourismPerTurn: 79.25
        - HappinessDelta: -7
        - BuildingCount: 56
        - ImportantBuildings:
          - Seaport
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Factory
          - Stock Exchange
          - Research Lab
          - Police Station
          - Hanse
          - Hotel
          - Caravansary
          - Airport
          - Grocer
          - Coaling Station
          - Wire Service
          - Brewhouse
        - Wonders:
          - National Intelligence Agency
        - GreatWorkCount: 3
        
        ### Bremen
        - ID: 4709
        - X: 14
        - Y: 45
        - Population: 24
        - MajorityReligion: Protestantism
        - DefenseStrength: 72
        - FoodStored: 591
        - FoodPerTurn: 40
        - ProductionPerTurn: 365
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 167
        - SciencePerTurn: 269
        - CulturePerTurn: 147
        - FaithPerTurn: 34
        - TourismPerTurn: 61.75
        - BuildingCount: 55
        - ImportantBuildings:
          - Water Mill
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Factory
          - Stock Exchange
          - Research Lab
          - Police Station
          - Hanse
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Brewhouse
        - GreatWorkCount: 2
        
        ### Hanover
        - ID: 5070
        - X: 74
        - Y: 30
        - Population: 26
        - MajorityReligion: Protestantism
        - DefenseStrength: 104
        - IsCoastal: true
        - FoodStored: 1318
        - FoodPerTurn: 20
        - ProductionPerTurn: 381
        - CurrentProduction: Infinite Project: Arts
        - GoldPerTurn: 200
        - SciencePerTurn: 159
        - CulturePerTurn: 242
        - FaithPerTurn: 35
        - TourismPerTurn: 65.75
        - HappinessDelta: 2
        - BuildingCount: 55
        - ImportantBuildings:
          - Seaport
          - Water Mill
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Factory
          - Stock Exchange
          - Public School
          - Police Station
          - Hanse
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Grocer
          - Coaling Station
          - Wire Service
          - Mine Field
          - Brewhouse
        - GreatWorkCount: 2
        
        ### Regensburg
        - ID: 5196
        - X: 70
        - Y: 33
        - Population: 30
        - MajorityReligion: Protestantism
        - DefenseStrength: 104
        - IsCoastal: true
        - FoodStored: 1352
        - FoodPerTurn: 33
        - ProductionStored: 357
        - ProductionPerTurn: 357
        - CurrentProduction: Cargo Ship
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 276
        - SciencePerTurn: 183
        - CulturePerTurn: 155
        - FaithPerTurn: 46
        - TourismPerTurn: 51.75
        - HappinessDelta: -2
        - BuildingCount: 56
        - ImportantBuildings:
          - Seaport
          - Observatory
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
          - Public School
          - Police Station
          - Hanse
          - Hotel
          - Caravansary
          - Airport
          - Coaling Station
          - Wire Service
          - Brewhouse
        - GreatWorkCount: 0
        
        ### Leipzig
        - ID: 5525
        - X: 72
        - Y: 37
        - Population: 29
        - MajorityReligion: Protestantism
        - DefenseStrength: 103
        - IsCoastal: true
        - FoodStored: 1927
        - FoodPerTurn: 24
        - ProductionPerTurn: 351
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 223
        - SciencePerTurn: 293
        - CulturePerTurn: 128
        - FaithPerTurn: 37
        - TourismPerTurn: 33
        - HappinessDelta: -4
        - BuildingCount: 58
        - ImportantBuildings:
          - Seaport
          - Observatory
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
          - Police Station
          - Hanse
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Coaling Station
          - Wire Service
          - Brewhouse
        - GreatWorkCount: 0
        
        ### Samarinda
        - ID: 11109
        - X: 73
        - Y: 25
        - Population: 33
        - MajorityReligion: Protestantism
        - DefenseStrength: 103
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 2061
        - FoodPerTurn: 107
        - ProductionStored: 775
        - ProductionPerTurn: 300
        - CurrentProduction: Airport
        - ProductionTurnsLeft: 3
        - GoldPerTurn: 218
        - SciencePerTurn: 229
        - CulturePerTurn: 126
        - FaithPerTurn: 36
        - TourismPerTurn: 43
        - HappinessDelta: -3
        - BuildingCount: 56
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Stable
          - Observatory
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
          - Hanse
          - Hotel
          - Caravansary
          - Wire Service
          - Brewhouse
        - GreatWorkCount: 0
        
        ### Teotihuacan
        - ID: 12865
        - X: 20
        - Y: 41
        - Population: 26
        - MajorityReligion: Protestantism
        - DefenseStrength: 80
        - IsOccupied: true
        - FoodStored: 1361
        - FoodPerTurn: 69
        - ProductionStored: 1488
        - ProductionPerTurn: 369
        - CurrentProduction: Airport
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 138
        - SciencePerTurn: 208
        - CulturePerTurn: 142
        - FaithPerTurn: 49
        - TourismPerTurn: 52
        - HappinessDelta: 0
        - BuildingCount: 54
        - ImportantBuildings:
          - Courthouse
          - Observatory
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
          - Recycling Center
          - Police Station
          - Hanse
          - Hotel
          - Caravansary
          - Coaling Station
          - Wire Service
          - Refinery
          - Brewhouse
        - GreatWorkCount: 0
        
        ### Tenochtitlan
        - ID: 13509
        - X: 24
        - Y: 43
        - Population: 26
        - MajorityReligion: Protestantism
        - DefenseStrength: 83
        - IsOccupied: true
        - FoodStored: 1218
        - FoodPerTurn: 38
        - ProductionStored: 1216
        - ProductionPerTurn: 378
        - CurrentProduction: Airport
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 183
        - SciencePerTurn: 176
        - CulturePerTurn: 125
        - FaithPerTurn: 47
        - TourismPerTurn: 21
        - HappinessDelta: 1
        - BuildingCount: 53
        - ImportantBuildings:
          - Courthouse
          - Stable
          - Water Mill
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Military Base
          - Hospital
          - Workshop
          - Stock Exchange
          - Research Lab
          - Police Station
          - Hanse
          - Caravansary
          - Bath
          - Coaling Station
          - Wire Service
          - Brewhouse
        - Wonders:
          - Borobudur
          - Karlstejn
        - GreatWorkCount: 0
        
        ### Calixtlahuaca
        - ID: 14127
        - X: 15
        - Y: 32
        - Population: 15
        - MajorityReligion: Protestantism
        - DefenseStrength: 41
        - IsPuppet: true
        - IsCoastal: true
        - FoodStored: 461
        - FoodPerTurn: 26
        - ProductionStored: 485
        - ProductionPerTurn: 154
        - CurrentProduction: Hospital
        - ProductionTurnsLeft: 6
        - GoldPerTurn: 37
        - SciencePerTurn: 33
        - CulturePerTurn: 25
        - FaithPerTurn: 4
        - TourismPerTurn: 2.9
        - HappinessDelta: 0
        - BuildingCount: 37
        - ImportantBuildings:
          - Seaport
          - Stable
          - Observatory
          - Garden
          - Arena
          - Opera House
          - Museum
          - Military Academy
          - Workshop
          - Stock Exchange
          - Public School
          - Shrine
          - Constabulary
          - Hanse
          - Caravansary
          - Chancery
          - Grocer
          - Brewhouse
        - GreatWorkCount: 0
        
        ### Zurich
        - ID: 14242
        - X: 24
        - Y: 36
        - Population: 19
        - MajorityReligion: Protestantism
        - DefenseStrength: 32
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 691
        - FoodPerTurn: 22
        - ProductionStored: 0
        - ProductionPerTurn: 126
        - CurrentProduction: Hospital
        - ProductionTurnsLeft: 4
        - GoldPerTurn: 161
        - SciencePerTurn: 133
        - CulturePerTurn: 73
        - FaithPerTurn: 10
        - TourismPerTurn: 4.75
        - HappinessDelta: 0
        - BuildingCount: 41
        - ImportantBuildings:
          - Courthouse
          - Seaport
          - Observatory
          - Garden
          - Zoo
          - Opera House
          - Military Academy
          - Workshop
          - Stock Exchange
          - Public School
          - Constabulary
          - Hanse
          - Caravansary
          - Bath
          - Chancery
          - Grocer
          - Gallery
          - Bastion Fort
          - Brewhouse
        - GreatWorkCount: 0
        
        ### Medan
        - ID: 14797
        - X: 67
        - Y: 20
        - Population: 22
        - MajorityReligion: Hinduism
        - DefenseStrength: 42
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 537
        - FoodPerTurn: 35
        - ProductionStored: 0
        - ProductionPerTurn: 356
        - CurrentProduction: Hotel
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 87
        - SciencePerTurn: 147
        - CulturePerTurn: 110
        - FaithPerTurn: 30
        - TourismPerTurn: 18
        - HappinessDelta: 0
        - BuildingCount: 41
        - ImportantBuildings:
          - Courthouse
          - Stable
          - Observatory
          - Garden
          - Harbor
          - Zoo
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Factory
          - Bank
          - Public School
          - Constabulary
          - Hanse
          - Caravansary
          - Chancery
          - Grocer
          - Brewhouse
        - Wonders:
          - University of Sankore
        - GreatWorkCount: 0
        
        ### Valletta
        - ID: 14799
        - X: 18
        - Y: 48
        - Population: 14
        - MajorityReligion: Protestantism
        - DefenseStrength: 33
        - IsOccupied: true
        - FoodStored: 454
        - FoodPerTurn: 83
        - ProductionStored: 120
        - ProductionPerTurn: 312
        - CurrentProduction: Bath
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 97
        - SciencePerTurn: 89
        - CulturePerTurn: 69
        - FaithPerTurn: 10
        - TourismPerTurn: 22.25
        - HappinessDelta: 5
        - BuildingCount: 39
        - ImportantBuildings:
          - Courthouse
          - Stable
          - Water Mill
          - Observatory
          - Garden
          - Stadium
          - Museum
          - Broadcast Tower
          - Armory
          - Hospital
          - Workshop
          - Stock Exchange
          - Public School
          - Hanse
          - Hotel
          - Caravansary
          - Wire Service
          - Brewhouse
        - GreatWorkCount: 0
        
        ### Tlatelolco
        - ID: 14971
        - X: 29
        - Y: 44
        - Population: 22
        - MajorityReligion: Protestantism
        - DefenseStrength: 37
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 582
        - FoodPerTurn: 50
        - ProductionStored: 0
        - ProductionPerTurn: 252
        - CurrentProduction: Wire Service
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 167
        - SciencePerTurn: 143
        - CulturePerTurn: 104
        - FaithPerTurn: 21
        - TourismPerTurn: 28
        - HappinessDelta: 1
        - BuildingCount: 44
        - ImportantBuildings:
          - Courthouse
          - Stable
          - Water Mill
          - Garden
          - Harbor
          - Stadium
          - Museum
          - Broadcast Tower
          - Armory
          - Hospital
          - Workshop
          - Stock Exchange
          - Public School
          - Shrine
          - Constabulary
          - Hanse
          - Hotel
          - Caravansary
          - Bath
          - Chancery
          - Brewhouse
        - Wonders:
          - Hagia Sophia
          - Alhambra
        - GreatWorkCount: 0
        
        ### Ardea
        - ID: 16749
        - X: 25
        - Y: 32
        - Population: 3
        - MajorityReligion: Protestantism
        - DefenseStrength: 39
        - Health: 64%
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 0
        - FoodPerTurn: 0
        - ProductionStored: 0
        - ProductionPerTurn: 0
        - CurrentProduction: Library
        - ProductionTurnsLeft: 9401
        - GoldPerTurn: 0
        - SciencePerTurn: 0
        - CulturePerTurn: 0
        - FaithPerTurn: 0
        - TourismPerTurn: 0
        - HappinessDelta: -3
        - RazingTurns: 2
        - BuildingCount: 9
        - ImportantBuildings:
          - Forge
          - Lighthouse
          - Arena
          - Granary
          - Council
          - Chancery
          - Grocer
        - GreatWorkCount: 0
        
        ### Tlaxcala
        - ID: 16835
        - X: 32
        - Y: 40
        - Population: 11
        - MajorityReligion: Protestantism
        - DefenseStrength: 39
        - Health: 66%
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 0
        - FoodPerTurn: 0
        - ProductionStored: 0
        - ProductionPerTurn: 0
        - CurrentProduction: TwoKay Foods Office
        - ProductionTurnsLeft: 55601
        - GoldPerTurn: 0
        - SciencePerTurn: 0
        - CulturePerTurn: 0
        - FaithPerTurn: 0
        - TourismPerTurn: 0
        - HappinessDelta: -11
        - RazingTurns: 6
        - ResistanceTurns: 7
        - BuildingCount: 23
        - ImportantBuildings:
          - Stable
          - Garden
          - Harbor
          - Arena
          - Workshop
          - Bank
          - University
          - Hanse
          - Caravansary
          - Grocer
          - Gallery
          - Brewhouse
        - GreatWorkCount: 0
        
        ## Player: Songhai
        
        ### Gao
        - ID: 1061
        - X: 47
        - Y: 22
        - Population: 20
        - MajorityReligion: Hinduism
        - DefenseStrength: 74
        - Wonders:
          - Heroic Epic
          - National Monument
          - Scrivener's Office
          - Printing Press
          - Palace of Culture and Science
          - Court Chapel
        
        ### Tombouctu
        - ID: 1419
        - X: 48
        - Y: 16
        - Population: 18
        - MajorityReligion: Hinduism
        - DefenseStrength: 70
        
        ### Jenne
        - ID: 1638
        - X: 51
        - Y: 21
        - Population: 18
        - MajorityReligion: Hinduism
        - DefenseStrength: 74
        - Wonders:
          - Ironworks
          - Imperial College
        
        ### Taghaza
        - ID: 2200
        - X: 54
        - Y: 25
        - Population: 19
        - MajorityReligion: Hinduism
        - DefenseStrength: 72
        - Wonders:
          - School of Philosophy
          - Circus Maximus
          - Chartered Company
          - Machu Picchu
        
        ### Kumbi Saleh
        - ID: 3179
        - X: 44
        - Y: 20
        - Population: 19
        - MajorityReligion: Hinduism
        - DefenseStrength: 70
        - IsCoastal: true
        - Wonders:
          - Grand Temple
          - Firaxite Materials Headquarters
        
        ### Tondibi
        - ID: 5139
        - X: 57
        - Y: 30
        - Population: 19
        - MajorityReligion: Hinduism
        - DefenseStrength: 69
        - Wonders:
          - Royal Collection
        
        ### Hsia
        - ID: 16098
        - X: 57
        - Y: 37
        - Population: 10
        - MajorityReligion: Hinduism
        - DefenseStrength: 40
        - IsOccupied: true
        - IsCoastal: true
        - RazingTurns: 10
        
        ## Player: Austria
        
        ### Vienna
        - ID: 1062
        - X: 61
        - Y: 22
        - Population: 24
        - MajorityReligion: Hinduism
        - DefenseStrength: 76
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Chartered Company
          - Hanging Gardens
          - Grand Temple
          - Scrivener's Office
          - Ballhausplatz
          - Roman Forum
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
        
        ### Graz
        - ID: 2223
        - X: 64
        - Y: 23
        - Population: 25
        - MajorityReligion: Hinduism
        - DefenseStrength: 72
        - Wonders:
          - Circus Maximus
          - Ironworks
        
        ### Linz
        - ID: 2224
        - X: 58
        - Y: 26
        - Population: 24
        - MajorityReligion: Hinduism
        - DefenseStrength: 70
        - Wonders:
          - Imperial College
          - Royal Collection
        
        ## Player: The Netherlands
        
        ### Amsterdam
        - ID: 1063
        - X: 47
        - Y: 32
        - Population: 35
        - MajorityReligion: Hinduism
        - DefenseStrength: 79
        - Wonders:
          - National Monument
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Imperial College
          - Royal Collection
          - Porcelain Tower
          - Palace of Culture and Science
          - Royal Guardhouse
        
        ### Rotterdam
        - ID: 1307
        - X: 50
        - Y: 29
        - Population: 25
        - MajorityReligion: Hinduism
        - DefenseStrength: 75
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - Great Library
          - Scrivener's Office
          - Printing Press
          - Civilized Jewelers Headquarters
        
        ### Utrecht
        - ID: 1490
        - X: 49
        - Y: 35
        - Population: 27
        - MajorityReligion: Hinduism
        - DefenseStrength: 71
        - IsCoastal: true
        - Wonders:
          - Oracle
          - Taj Mahal
          - Grand Temple
          - Nalanda
        
        ### Groningen
        - ID: 1977
        - X: 46
        - Y: 38
        - Population: 22
        - MajorityReligion: Hinduism
        - DefenseStrength: 46
        - IsCoastal: true
        - Wonders:
          - Great Lighthouse
        
        ### Breda
        - ID: 2611
        - X: 41
        - Y: 32
        - Population: 25
        - MajorityReligion: Hinduism
        - DefenseStrength: 73
        - IsCoastal: true
        
        ### Old Sarai
        - ID: 8605
        - X: 61
        - Y: 47
        - Population: 21
        - MajorityReligion: Tengriism
        - DefenseStrength: 72
        - IsOccupied: true
        - IsCoastal: true
        
        ### Tzintzuntzen
        - ID: 12892
        - X: 34
        - Y: 27
        - Population: 17
        - MajorityReligion: Hinduism
        - DefenseStrength: 75
        - IsOccupied: true
        - IsCoastal: true
        
        ### Tlacopan
        - ID: 13034
        - X: 35
        - Y: 22
        - Population: 16
        - MajorityReligion: Hinduism
        - DefenseStrength: 79
        - IsOccupied: true
        - IsCoastal: true
        
        ### Atzcapotzalco
        - ID: 13035
        - X: 33
        - Y: 17
        - Population: 16
        - MajorityReligion: Hinduism
        - DefenseStrength: 77
        - IsOccupied: true
        - IsCoastal: true
        
        ### Seoul
        - ID: 13335
        - X: 31
        - Y: 33
        - Population: 17
        - MajorityReligion: Protestantism
        - DefenseStrength: 71
        - Health: 95%
        - IsOccupied: true
        - IsCoastal: true
        
        ### Setia
        - ID: 15969
        - X: 29
        - Y: 15
        - Population: 13
        - MajorityReligion: Hinduism
        - DefenseStrength: 45
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: Mongolia
        
        ### Karakorum
        - ID: 1064
        - X: 62
        - Y: 36
        - Population: 24
        - DefenseStrength: 55
        - Health: 60%
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Scrivener's Office
          - Printing Press
        
        ### Beshbalik
        - ID: 1308
        - X: 64
        - Y: 41
        - Population: 24
        - MajorityReligion: Tengriism
        - DefenseStrength: 51
        - IsCoastal: true
        - Wonders:
          - National Monument
        
        ## Player: City-States
        
        ### Ouagadougou
        - ID: 1065
        - X: 5
        - Y: 8
        - Population: 17
        - MajorityReligion: Protestantism
        - DefenseStrength: 72
        - IsCoastal: true
        
        ### Mataram
        - ID: 14390
        - X: 7
        - Y: 4
        - Population: 11
        - MajorityReligion: Protestantism
        - DefenseStrength: 13
        - IsOccupied: true
        - IsCoastal: true
        
        ### Veligrad
        - ID: 1067
        - X: 42
        - Y: 27
        - Population: 20
        - MajorityReligion: Hinduism
        - DefenseStrength: 90
        - IsCoastal: true
        
        ### Kyiv
        - ID: 1068
        - X: 66
        - Y: 27
        - Population: 20
        - MajorityReligion: Protestantism
        - DefenseStrength: 97
        - IsCoastal: true
        
        ### Turfan
        - ID: 5698
        - X: 64
        - Y: 31
        - Population: 18
        - DefenseStrength: 78
        - IsOccupied: true
        - IsCoastal: true
        
        ### Belgrade
        - ID: 1069
        - X: 55
        - Y: 34
        - Population: 24
        - MajorityReligion: Hinduism
        - DefenseStrength: 92
        - IsCoastal: true
        
        ### Sidon
        - ID: 1070
        - X: 68
        - Y: 47
        - Population: 18
        - DefenseStrength: 80
        - IsCoastal: true
        
        ### Shedet
        - ID: 1072
        - X: 32
        - Y: 48
        - Population: 20
        - MajorityReligion: Protestantism
        - DefenseStrength: 90
        - Health: 64%
        - IsCoastal: true
        
        ### Cahokia
        - ID: 1073
        - X: 5
        - Y: 30
        - Population: 19
        - MajorityReligion: Protestantism
        - DefenseStrength: 68
        - IsCoastal: true
        
        ### M'banza-Kongo
        - ID: 10031
        - X: 11
        - Y: 28
        - Population: 9
        - MajorityReligion: Protestantism
        - DefenseStrength: 44
        - IsOccupied: true
        - IsCoastal: true
        
        ### Ostia
        - ID: 11364
        - X: 10
        - Y: 19
        - Population: 9
        - MajorityReligion: Protestantism
        - DefenseStrength: 30
        - IsOccupied: true
        - IsCoastal: true
        
        ### Kwa-Bulawayo
        - ID: 1075
        - X: 42
        - Y: 37
        - Population: 23
        - DefenseStrength: 86
        - IsCoastal: true
        
        ### Ormus
        - ID: 1078
        - X: 15
        - Y: 26
        - Population: 23
        - MajorityReligion: Protestantism
        - DefenseStrength: 94
        - IsCoastal: true
        
        ### Kukia
        - ID: 15778
        - X: 31
        - Y: 25
        - Population: 7
        - MajorityReligion: Hinduism
        - DefenseStrength: 36
        - IsOccupied: true
        - IsCoastal: true
        
        ### Kuala Lumpur
        - ID: 1080
        - X: 60
        - Y: 29
        - Population: 12
        - MajorityReligion: Hinduism
        - DefenseStrength: 97
        
        # Military
        Military: summary reports about tactical zones and visible units.
        
        ## Unit Stats
        - Attack:
          - Foreign Legion:
            - Strength: 40
        - CityBombard:
          - Artillery:
            - Strength: 27
            - RangedStrength: 50
          - Krupp Gun:
            - Strength: 27
            - RangedStrength: 55
        - FastAttack:
          - Tank:
            - Strength: 75
          - Landship:
            - Strength: 60
          - Commando:
            - Strength: 32
        - Defense:
          - Infantry:
            - Strength: 62
          - Fusilier:
            - Strength: 38
          - Rifleman:
            - Strength: 50
          - Grenzer:
            - Strength: 38
        - Counter:
          - Anti-Aircraft Gun:
            - Strength: 40
        - Ranged:
          - Light Tank:
            - Strength: 58
            - RangedStrength: 52
          - Musketman:
            - Strength: 21
            - RangedStrength: 30
          - Machine Gun:
            - Strength: 45
            - RangedStrength: 58
          - Gatling Gun:
            - Strength: 32
            - RangedStrength: 44
        - AttackSea:
          - Destroyer:
            - Strength: 70
          - Ironclad:
            - Strength: 55
          - Fleet Destroyer:
            - Strength: 80
        - AssaultSea:
          - Cruiser:
            - Strength: 40
            - RangedStrength: 55
          - Dreadnought:
            - Strength: 50
            - RangedStrength: 65
          - Attack Submarine:
            - Strength: 50
            - RangedStrength: 72
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
        - Paradrop:
          - Paratrooper:
            - Strength: 42
          - Special Forces:
            - Strength: 65
        
        ## Friendly Land Zone 1059
        - ZoneValue: 66
        - Dominance: Friendly
        - FriendlyStrength: 2225
        - City: Berlin
        - AreaID: 31
        - Plots: 25
        - CenterX: 14
        - CenterY: 39
        - Units:
          - Germany:
            - Anti-Aircraft Gun: 1
            - Infantry: 1
            - Machine Gun: 1
        - Neighbors:
          - 1193
          - 3320
          - 14127
          - -3783
          - 3783
          - 12865
        
        ## Neutral Land Zone 1061
        - ZoneValue: 30
        - Dominance: Enemy
        - EnemyStrength: 521
        - NeutralStrength: 763
        - City: Gao
        - AreaID: 2
        - Plots: 23
        - CenterX: 47
        - CenterY: 23
        - Units:
          - Songhai:
            - Machine Gun: 3
        - Neighbors:
          - 1307
        
        ## Neutral Land Zone 1062
        - ZoneValue: 72
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 3001
        - NeutralStrength: 1258
        - FriendlyStrength: 324
        - City: Vienna
        - AreaID: 2
        - Plots: 21
        - CenterX: 61
        - CenterY: 22
        - Units:
          - Rome:
            - Machine Gun: 1
          - Austria:
            - Light Tank: 1
            - Rifleman: 2
            - Commando: 1
        - Neighbors:
          - 6669
          - 2223
          - 10721
        
        ## Enemy Land Zone 1063
        - ZoneValue: 168
        - Dominance: Enemy
        - EnemyStrength: 1753
        - City: Amsterdam
        - AreaID: 2
        - Plots: 23
        - CenterX: 46
        - CenterY: 32
        - Units:
          - The Netherlands:
            - Rifleman: 1
        - Neighbors:
          - 1307
          - 1490
        
        ## Neutral Land Zone 1064
        - ZoneValue: 24
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 237
        - NeutralStrength: 1306
        - FriendlyStrength: 85
        - City: Karakorum
        - AreaID: 2
        - Plots: 23
        - CenterX: 62
        - CenterY: 35
        - Units:
          - Mongolia:
            - Musketman: 1
        - Neighbors:
          - 5698
          - -5698
          - -1308
        
        ## Neutral Land Zone 1065
        - ZoneValue: 36
        - Dominance: Friendly
        - NeutralStrength: 72
        - FriendlyStrength: 1809
        - City: Ouagadougou
        - AreaID: 1
        - Plots: 5
        - CenterX: 5
        - CenterY: 9
        - Units:
          - Barbarians:
            - Fusilier: 1
          - City-State Ouagadougou:
            - Ironclad: 1
            - Rifleman: 2
            - Machine Gun: 2
        - Neighbors:
          - -1065
          - 14390
        
        ## Neutral Land Zone 1068
        - ZoneValue: 18
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 80
        - NeutralStrength: 679
        - FriendlyStrength: 1753
        - City: Kyiv
        - AreaID: 2
        - Plots: 15
        - CenterX: 66
        - CenterY: 26
        - Units:
          - City-State Kyiv:
            - Machine Gun: 1
          - Germany:
            - Infantry: 1
            - Machine Gun: 1
        - Neighbors:
          - 2223
          - 5698
          - -14797
        
        ## Enemy Land Zone 1072
        - ZoneValue: 96
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 269
        - FriendlyStrength: 3604
        - City: Shedet
        - AreaID: 31
        - Plots: 20
        - CenterX: 30
        - CenterY: 48
        - Units:
          - City-State Shedet:
            - Machine Gun: 1
          - Germany:
            - Light Tank: 2
            - Infantry: 2
            - Special Forces: 1
            - Machine Gun: 1
            - Krupp Gun: 1
        - Neighbors:
          - 14971
          - 100005
        
        ## Neutral Land Zone 1073
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 526
        - FriendlyStrength: 2689
        - City: Cahokia
        - AreaID: 36
        - Plots: 8
        - CenterX: 5
        - CenterY: 30
        - Units:
          - City-State Cahokia:
            - Rifleman: 2
            - Machine Gun: 4
          - Germany:
            - Infantry: 1
        - Neighbors:
          - -1073
          - 2191
        
        ## Enemy Land Zone 1078
        - ZoneValue: 96
        - Dominance: Friendly
        - Posture: Steamroll
        - EnemyStrength: 298
        - NeutralStrength: 180
        - FriendlyStrength: 2179
        - City: Ormus
        - AreaID: 28
        - Plots: 8
        - CenterX: 14
        - CenterY: 26
        - Units:
          - City-State Ormus:
            - Ironclad: 1
            - Machine Gun: 1
          - Germany:
            - Infantry: 3
            - Special Forces: 1
        - Neighbors:
          - 10031
          - -1078
          - 14127
        
        ## Friendly Land Zone 1193
        - ZoneValue: 42
        - Dominance: Friendly
        - FriendlyStrength: 2817
        - City: Hamburg
        - AreaID: 61
        - Plots: 18
        - CenterX: 10
        - CenterY: 38
        - Units:
          - Germany:
            - Heavy Bomber: 1
            - Triplane: 1
            - Bomber: 1
        - Neighbors:
          - 2191
          - 4222
          - -3320
          - 3320
          - 1059
        
        ## Enemy Land Zone 1307
        - ZoneValue: 120
        - Dominance: Enemy
        - EnemyStrength: 1829
        - NeutralStrength: 25
        - City: Rotterdam
        - AreaID: 2
        - Plots: 37
        - CenterX: 50
        - CenterY: 28
        - Units:
          - The Netherlands:
            - Artillery: 2
            - Anti-Aircraft Gun: 1
            - Light Tank: 1
            - Rifleman: 1
            - Machine Gun: 2
        - Neighbors:
          - 1063
          - 1061
          - 1490
          - 5139
        
        ## Enemy Land Zone 1490
        - ZoneValue: 144
        - Dominance: Enemy
        - EnemyStrength: 1430
        - City: Utrecht
        - AreaID: 2
        - Plots: 14
        - CenterX: 49
        - CenterY: 34
        - Units:
          - The Netherlands:
            - Rifleman: 1
        - Neighbors:
          - 1063
          - 1307
        
        ## Friendly Land Zone 1927
        - ZoneValue: 42
        - Dominance: Friendly
        - FriendlyStrength: 1923
        - City: Munich
        - AreaID: 31
        - Plots: 12
        - CenterX: 12
        - CenterY: 47
        - Units:
          - Germany:
            - Triplane: 1
            - Machine Gun: 1
            - Krupp Gun: 2
        - Neighbors:
          - 4222
          - 4072
          - 14799
        
        ## Friendly Land Zone 2191
        - ZoneValue: 42
        - Dominance: Friendly
        - NeutralStrength: 328
        - FriendlyStrength: 3863
        - City: Cologne
        - AreaID: 46
        - Plots: 11
        - CenterX: 6
        - CenterY: 34
        - Units:
          - Germany:
            - Special Forces: 1
            - Triplane: 1
            - Bomber: 4
            - Machine Gun: 2
        - Neighbors:
          - 3319
          - 1073
          - -1073
          - -3320
          - 1193
        
        ## Neutral Land Zone 2223
        - ZoneValue: 60
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 1963
        - NeutralStrength: 1063
        - FriendlyStrength: 1980
        - City: Graz
        - AreaID: 2
        - Plots: 20
        - CenterX: 64
        - CenterY: 23
        - Units:
          - Rome:
            - Rifleman: 1
          - Germany:
            - Infantry: 1
          - Austria:
            - Rifleman: 1
            - Machine Gun: 1
            - Commando: 1
            - Grenzer: 1
        - Neighbors:
          - 1062
          - 1068
          - 10721
          - 14797
          - -14797
        
        ## Friendly Land Zone 3319
        - ZoneValue: 42
        - Dominance: Friendly
        - NeutralStrength: 195
        - FriendlyStrength: 2808
        - City: Frankfurt
        - AreaID: 44
        - Plots: 11
        - CenterX: 1
        - CenterY: 35
        - Units:
          - Germany:
            - Infantry: 1
            - Triplane: 1
            - Bomber: 4
            - Krupp Gun: 1
        - Neighbors:
          - -1073
          - 2191
        
        ## Friendly Land Zone 3320
        - ZoneValue: 42
        - Dominance: Friendly
        - NeutralStrength: 365
        - FriendlyStrength: 4630
        - City: Aachen
        - AreaID: 31
        - Plots: 15
        - CenterX: 11
        - CenterY: 32
        - Units:
          - Germany:
            - Anti-Aircraft Gun: 1
            - Triplane: 4
            - Bomber: 2
            - Machine Gun: 1
            - Krupp Gun: 1
        - Neighbors:
          - -1073
          - -3320
          - 10031
          - 1193
          - 14127
          - 1059
        
        ## Friendly Land Zone 3783
        - ZoneValue: 3
        - Dominance: Friendly
        - FriendlyStrength: 3974
        - City: Dortmund
        - AreaID: 53
        - Plots: 13
        - CenterX: 18
        - CenterY: 37
        - Units:
          - Germany:
            - Light Tank: 1
            - Infantry: 1
            - Triplane: 2
            - Machine Gun: 1
        - Neighbors:
          - 1059
          - -3783
          - 12865
        
        ## Friendly Land Zone 4072
        - ZoneValue: 42
        - Dominance: Friendly
        - FriendlyStrength: 1293
        - City: Stuttgart
        - AreaID: 77
        - Plots: 13
        - CenterX: 9
        - CenterY: 49
        - Units:
          - Germany:
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - 1927
        
        ## Friendly Land Zone 4222
        - ZoneValue: 3
        - Dominance: Friendly
        - FriendlyStrength: 1696
        - City: Dusseldorf
        - AreaID: 72
        - Plots: 14
        - CenterX: 9
        - CenterY: 42
        - Units:
          - Germany:
            - Anti-Aircraft Gun: 1
            - Infantry: 1
            - Bomber: 3
        - Neighbors:
          - 1193
          - 1927
        
        ## Friendly Land Zone 5070
        - ZoneValue: 36
        - Dominance: Friendly
        - FriendlyStrength: 2787
        - City: Hanover
        - AreaID: 27
        - Plots: 16
        - CenterX: 73
        - CenterY: 30
        - Units:
          - Germany:
            - Special Forces: 1
        - Neighbors:
          - 11109
          - 5196
        
        ## Neutral Land Zone 5139
        - ZoneValue: 30
        - Dominance: Enemy
        - EnemyStrength: 645
        - NeutralStrength: 1396
        - City: Tondibi
        - AreaID: 2
        - Plots: 19
        - CenterX: 56
        - CenterY: 30
        - Units:
          - Songhai:
            - Rifleman: 1
        - Neighbors:
          - 1307
        
        ## Friendly Land Zone 5196
        - ZoneValue: 3
        - Dominance: Friendly
        - FriendlyStrength: 2613
        - City: Regensburg
        - AreaID: 40
        - Plots: 17
        - CenterX: 71
        - CenterY: 33
        - Units:
          - Germany:
            - Heavy Bomber: 1
            - Fighter: 2
            - Anti-Aircraft Gun: 1
            - Special Forces: 2
            - Triplane: 1
            - Bomber: 2
        - Neighbors:
          - 5525
          - 5070
        
        ## Friendly Land Zone 5525
        - ZoneValue: 36
        - Dominance: Friendly
        - FriendlyStrength: 2193
        - City: Leipzig
        - AreaID: 27
        - Plots: 11
        - CenterX: 72
        - CenterY: 37
        - Units:
          - Germany:
            - Special Forces: 1
            - Triplane: 4
            - Bomber: 2
            - Machine Gun: 1
        - Neighbors:
          - 5196
        
        ## Neutral Land Zone 5698
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 1246
        - FriendlyStrength: 349
        - City: Turfan
        - AreaID: 2
        - Plots: 16
        - CenterX: 64
        - CenterY: 31
        - Units:
          - City-State Kyiv:
            - Machine Gun: 3
        - Neighbors:
          - 1064
          - 1068
          - -5698
        
        ## Enemy Land Zone 6669
        - ZoneValue: 72
        - Dominance: Enemy
        - EnemyStrength: 4296
        - NeutralStrength: 559
        - City: Salzburg
        - AreaID: 2
        - Plots: 22
        - CenterX: 59
        - CenterY: 17
        - Units:
          - Rome:
            - Machine Gun: 1
        - Neighbors:
          - 1062
          - 10252
          - 10721
        
        ## Neutral Land Zone 10031
        - ZoneValue: 12
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 135
        - NeutralStrength: 425
        - FriendlyStrength: 3063
        - City: M'banza-Kongo
        - AreaID: 31
        - Plots: 16
        - CenterX: 11
        - CenterY: 27
        - Units:
          - City-State Cahokia:
            - Rifleman: 3
          - Germany:
            - Infantry: 1
        - Neighbors:
          - -1073
          - 3320
          - 1078
          - -1078
        
        ## Enemy Land Zone 10252
        - ZoneValue: 60
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 3822
        - FriendlyStrength: 147
        - City: Jakarta
        - AreaID: 2
        - Plots: 17
        - CenterX: 62
        - CenterY: 12
        - Units:
          - Rome:
            - Machine Gun: 2
        - Neighbors:
          - 6669
          - 10721
          - 15485
          - -10721
        
        ## Enemy Land Zone 10721
        - ZoneValue: 96
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 4805
        - NeutralStrength: 508
        - FriendlyStrength: 1758
        - City: Surabaya
        - AreaID: 2
        - Plots: 15
        - CenterX: 63
        - CenterY: 17
        - Units:
          - Rome:
            - Artillery: 2
            - Anti-Aircraft Gun: 1
            - Machine Gun: 6
            - Dreadnought: 1
        - Neighbors:
          - 10252
          - 6669
          - 1062
          - -10721
          - 14797
          - 2223
        
        ## Friendly Land Zone 11109
        - ZoneValue: 36
        - Dominance: Friendly
        - FriendlyStrength: 3174
        - City: Samarinda
        - AreaID: 27
        - Plots: 16
        - CenterX: 73
        - CenterY: 26
        - Units:
          - Germany:
            - Infantry: 1
            - Triplane: 1
            - Bomber: 1
            - Machine Gun: 2
            - Krupp Gun: 2
        - Neighbors:
          - -11109
          - 5070
        
        ## Friendly Land Zone 12865
        - ZoneValue: 36
        - Dominance: Friendly
        - FriendlyStrength: 3079
        - City: Teotihuacan
        - AreaID: 31
        - Plots: 29
        - CenterX: 20
        - CenterY: 41
        - Units:
          - Germany:
            - Infantry: 1
        - Neighbors:
          - 1059
          - 3783
          - 14799
          - 14242
          - 13509
        
        ## Enemy Land Zone 13335
        - ZoneValue: 48
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 773
        - FriendlyStrength: 1381
        - City: Seoul
        - AreaID: 39
        - Plots: 10
        - CenterX: 31
        - CenterY: 32
        - Units:
          - The Netherlands:
            - Artillery: 1
            - Rifleman: 1
            - Triplane: 1
            - Bomber: 1
          - Germany:
            - Tank: 1
        - Neighbors:
          - -13335
        
        ## Friendly Land Zone 13509
        - ZoneValue: 36
        - Dominance: Friendly
        - FriendlyStrength: 3220
        - City: Tenochtitlan
        - AreaID: 31
        - Plots: 38
        - CenterX: 24
        - CenterY: 44
        - Units:
          - Germany:
            - Infantry: 1
            - Machine Gun: 1
        - Neighbors:
          - 14799
          - 12865
          - 14242
          - 100005
          - 14971
          - -14242
        
        ## Friendly Land Zone 14127
        - ZoneValue: 18
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 135
        - NeutralStrength: 120
        - FriendlyStrength: 3939
        - City: Calixtlahuaca
        - AreaID: 31
        - Plots: 19
        - CenterX: 14
        - CenterY: 33
        - Units:
          - Germany:
            - Anti-Aircraft Gun: 1
            - Infantry: 2
            - Triplane: 2
            - Machine Gun: 2
            - Krupp Gun: 1
        - Neighbors:
          - 3320
          - 1059
          - 1078
          - -3783
        
        ## Friendly Land Zone 14242
        - ZoneValue: 30
        - Dominance: Friendly
        - FriendlyStrength: 4269
        - City: Zurich
        - AreaID: 54
        - Plots: 18
        - CenterX: 23
        - CenterY: 37
        - Units:
          - Germany:
            - Fighter: 2
            - Infantry: 2
            - Krupp Gun: 3
        - Neighbors:
          - -3783
          - -14242
          - 12865
          - -16749
          - 16749
          - 13509
        
        ## Neutral Land Zone 14390
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 14
        - FriendlyStrength: 1173
        - City: Mataram
        - AreaID: 1
        - Plots: 15
        - CenterX: 7
        - CenterY: 4
        - Units:
          - City-State Ouagadougou:
            - Paratrooper: 1
            - Rifleman: 1
            - Machine Gun: 1
        - Neighbors:
          - 1065
          - -1065
        
        ## Friendly Land Zone 14797
        - ZoneValue: 288
        - Dominance: Even
        - Posture: Counterattack
        - EnemyStrength: 2734
        - NeutralStrength: 238
        - FriendlyStrength: 2603
        - City: Medan
        - AreaID: 2
        - Plots: 13
        - CenterX: 67
        - CenterY: 21
        - Units:
          - Rome:
            - Paratrooper: 1
            - Foreign Legion: 1
            - Landship: 1
          - Germany:
            - Fighter: 1
            - Anti-Aircraft Gun: 1
            - Infantry: 2
            - Special Forces: 1
            - Triplane: 1
            - Machine Gun: 1
            - Krupp Gun: 2
        - Neighbors:
          - 10721
          - 2223
          - -10721
          - -14797
        
        ## Friendly Land Zone 14799
        - ZoneValue: 30
        - Dominance: Friendly
        - FriendlyStrength: 1334
        - City: Valletta
        - AreaID: 31
        - Plots: 43
        - CenterX: 18
        - CenterY: 48
        - Units:
          - Germany:
            - Anti-Aircraft Gun: 1
            - Infantry: 1
            - Machine Gun: 3
            - Krupp Gun: 1
        - Neighbors:
          - 1927
          - 12865
          - 13509
          - 100005
        
        ## Friendly Land Zone 14971
        - ZoneValue: 36
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 131
        - FriendlyStrength: 5657
        - City: Tlatelolco
        - AreaID: 31
        - Plots: 27
        - CenterX: 28
        - CenterY: 45
        - Units:
          - Germany:
            - Heavy Bomber: 1
            - Infantry: 3
            - Machine Gun: 4
            - Krupp Gun: 3
        - Neighbors:
          - 13509
          - 100005
          - 1072
          - 16835
        
        ## Enemy Land Zone 15485
        - ZoneValue: 48
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 2617
        - FriendlyStrength: 147
        - City: Makassar
        - AreaID: 2
        - Plots: 12
        - CenterX: 64
        - CenterY: 9
        - Units:
          - Rome:
            - Artillery: 1
            - Rifleman: 1
        - Neighbors:
          - 10252
          - -15485
        
        ## Friendly Land Zone 16749
        - ZoneValue: 48
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 209
        - FriendlyStrength: 3541
        - City: Ardea
        - AreaID: 43
        - Plots: 9
        - CenterX: 25
        - CenterY: 33
        - Units:
          - Germany:
            - Anti-Aircraft Gun: 1
            - Light Tank: 1
            - Infantry: 1
            - Attack Submarine: 1
        - Neighbors:
          - -16749
          - 14242
          - -14242
        
        ## Friendly Land Zone 16835
        - ZoneValue: 90
        - Dominance: Friendly
        - FriendlyStrength: 3427
        - City: Tlaxcala
        - AreaID: 69
        - Plots: 12
        - CenterX: 31
        - CenterY: 41
        - Units:
          - Germany:
            - Anti-Aircraft Gun: 1
            - Infantry: 4
            - Machine Gun: 2
        - Neighbors:
          - 14971
        
        ## Enemy Land Zone 16908
        - ZoneValue: 12
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 594
        - FriendlyStrength: 263
        - City: Satricum
        - AreaID: 7
        - Plots: 11
        - CenterX: 27
        - CenterY: 9
        - Units:
          - Rome:
            - Anti-Aircraft Gun: 2
            - Rifleman: 1
            - Gatling Gun: 1
        - Neighbors:
          - -16908
        
        ## Neutral Land Zone 100005
        - ZoneValue: 3
        - Dominance: Friendly
        - FriendlyStrength: 223
        - AreaID: 31
        - Plots: 8
        - CenterX: 25
        - CenterY: 50
        - Units:
          - Germany:
            - Infantry: 1
        - Neighbors:
          - 14799
          - 13509
          - 14971
          - 1072
        
        ## Enemy Sea Zone -10721
        - ZoneValue: 32
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 3285
        - NeutralStrength: 104
        - FriendlyStrength: 743
        - City: Surabaya
        - AreaID: 0
        - Plots: 14
        - CenterX: 66
        - CenterY: 16
        - Units:
          - Rome:
            - Dreadnought: 1
          - Germany:
            - Destroyer: 1
        - Neighbors:
          - 10721
          - 10252
          - -15485
          - 14797
          - -14797
        
        ## Enemy Sea Zone -16908
        - ZoneValue: 480
        - Dominance: Even
        - Posture: Attrition
        - EnemyStrength: 538
        - FriendlyStrength: 637
        - City: Satricum
        - AreaID: 0
        - Plots: 68
        - CenterX: 26
        - CenterY: 7
        - Units:
          - The Netherlands:
            - Ironclad: 1
          - Germany:
            - Destroyer: 1
            - Attack Submarine: 2
        - Neighbors:
          - 16908
        
        ## Friendly Sea Zone -3320
        - ZoneValue: 14
        - Dominance: Friendly
        - NeutralStrength: 45
        - FriendlyStrength: 2268
        - City: Aachen
        - AreaID: 0
        - Plots: 8
        - CenterX: 10
        - CenterY: 33
        - Units:
          - Germany:
            - Infantry: 1
            - Attack Submarine: 1
        - Neighbors:
          - 3320
          - 2191
          - 1193
        
        ## Friendly Sea Zone -3783
        - ZoneValue: 10
        - Dominance: Friendly
        - FriendlyStrength: 2240
        - City: Dortmund
        - AreaID: 0
        - Plots: 13
        - CenterX: 19
        - CenterY: 35
        - Units:
          - Germany:
            - Infantry: 1
            - Attack Submarine: 1
            - Krupp Gun: 1
        - Neighbors:
          - 1059
          - 14127
          - 3783
          - -16749
          - -14242
          - 14242
        
        ## Enemy Sea Zone -1078
        - ZoneValue: 16
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 748
        - NeutralStrength: 77
        - FriendlyStrength: 619
        - City: Ormus
        - AreaID: 0
        - Plots: 47
        - CenterX: 16
        - CenterY: 25
        - Units:
          - City-State Ormus:
            - Ironclad: 1
        - Neighbors:
          - -11364
          - 1078
          - 10031
        
        ## Neutral Sea Zone -1073
        - ZoneValue: 6
        - Dominance: Friendly
        - NeutralStrength: 249
        - FriendlyStrength: 1791
        - City: Cahokia
        - AreaID: 0
        - Plots: 47
        - CenterX: 4
        - CenterY: 28
        - Units:
          - Germany:
            - Dreadnought: 2
        - Neighbors:
          - -100000
          - 3319
          - 1073
          - 2191
          - 10031
          - 3320
        
        ## Neutral Sea Zone -1065
        - ZoneValue: 12
        - Dominance: Friendly
        - NeutralStrength: 72
        - FriendlyStrength: 3319
        - City: Ouagadougou
        - AreaID: 0
        - Plots: 65
        - CenterX: 4
        - CenterY: 9
        - Units:
          - Barbarians:
            - Ironclad: 1
          - City-State Ouagadougou:
            - Ironclad: 14
            - Rifleman: 2
            - Cruiser: 1
            - Dreadnought: 1
        - Neighbors:
          - -100000
          - 1065
          - 14390
        
        ## Friendly Sea Zone -14797
        - ZoneValue: 96
        - Dominance: Even
        - Posture: Counterattack
        - EnemyStrength: 1470
        - NeutralStrength: 27
        - FriendlyStrength: 1846
        - City: Medan
        - AreaID: 0
        - Plots: 27
        - CenterX: 69
        - CenterY: 19
        - Units:
          - Germany:
            - Destroyer: 1
            - Attack Submarine: 2
        - Neighbors:
          - -10721
          - 14797
          - 2223
          - -15485
          - 1068
          - -100000
          - -11109
        
        ## Enemy Sea Zone -15485
        - ZoneValue: 16
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 2455
        - FriendlyStrength: 220
        - City: Makassar
        - AreaID: 0
        - Plots: 27
        - CenterX: 67
        - CenterY: 10
        - Units:
          - Rome:
            - Dreadnought: 1
          - Germany:
            - Destroyer: 1
        - Neighbors:
          - 15485
          - -10721
          - -100000
          - -14797
        
        ## Friendly Sea Zone -11109
        - ZoneValue: 12
        - Dominance: Friendly
        - FriendlyStrength: 2930
        - City: Samarinda
        - AreaID: 0
        - Plots: 44
        - CenterX: 74
        - CenterY: 23
        - Units:
          - Germany:
            - Fleet Destroyer: 1
            - Attack Submarine: 2
        - Neighbors:
          - -14797
          - 11109
          - -100000
        
        ## Neutral Sea Zone -100000
        - ZoneValue: 1
        - AreaID: 0
        - Plots: 246
        - CenterX: 77
        - CenterY: 13
        - Units:
          - Germany:
            - Tank: 1
            - Dreadnought: 1
            - Attack Submarine: 1
        - Neighbors:
          - -1065
          - -1073
          - -11364
          - -15485
          - -14797
          - -11109
        
        ## Friendly Sea Zone -16749
        - ZoneValue: 16
        - Dominance: Friendly
        - FriendlyStrength: 3280
        - City: Ardea
        - AreaID: 0
        - Plots: 46
        - CenterX: 24
        - CenterY: 30
        - Units:
          - Germany:
            - Destroyer: 2
            - Attack Submarine: 1
        - Neighbors:
          - -3783
          - -14242
          - 16749
          - 14242
          - -13335
        
        ## Enemy Sea Zone -13335
        - ZoneValue: 576
        - Dominance: Friendly
        - Posture: Exploit Flanks
        - EnemyStrength: 442
        - FriendlyStrength: 1598
        - City: Seoul
        - AreaID: 0
        - Plots: 48
        - CenterX: 32
        - CenterY: 33
        - Units:
          - The Netherlands:
            - Paratrooper: 1
          - Germany:
            - Destroyer: 3
            - Dreadnought: 1
            - Attack Submarine: 2
        - Neighbors:
          - -16749
          - 13335
          - -14242
        
        ## Neutral Sea Zone -11364
        - ZoneValue: 2
        - NeutralStrength: 2058
        - City: Ostia
        - AreaID: 0
        - Plots: 75
        - CenterX: 10
        - CenterY: 18
        - Units:
          - City-State Cahokia:
            - Ironclad: 2
          - Germany:
            - Infantry: 1
        - Neighbors:
          - -100000
          - -1078
        
        ## Neutral Sea Zone -1308
        - ZoneValue: 3
        - Dominance: Enemy
        - EnemyStrength: 835
        - NeutralStrength: 455
        - City: Beshbalik
        - AreaID: 0
        - Plots: 37
        - CenterX: 65
        - CenterY: 41
        - Units:
          - Mongolia:
            - Musketman: 1
        - Neighbors:
          - 1064
        
        ## Friendly Sea Zone -14242
        - ZoneValue: 1
        - Dominance: Friendly
        - FriendlyStrength: 3512
        - City: Zurich
        - AreaID: 0
        - Plots: 18
        - CenterX: 25
        - CenterY: 36
        - Units:
          - Germany:
            - Attack Submarine: 1
        - Neighbors:
          - -3783
          - -16749
          - 14242
          - 16749
          - 13509
          - -13335
        
        ## Neutral Sea Zone -5698
        - ZoneValue: 6
        - NeutralStrength: 763
        - City: Turfan
        - AreaID: 0
        - Plots: 14
        - CenterX: 66
        - CenterY: 33
        - Units:
          - City-State Kyiv:
            - Ironclad: 2
          - Germany:
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - 5698
          - 1064
        
        # Events
        Events: events since you last made a decision.
        
        ## Turn 383
        
        ### 0
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 15876
        - Player: 3: Indonesia
        - Plots:
          - Coast 2,31:
            - Owner: Germany
          - Coast 2,30:
            - Owner: Germany
        
        ### 1
        - Type: CityInvestedBuilding
        - BuildingClass: Research Lab
        - Invested: true
        - City:
          - Name: Gao
          - Population: 20
          - ID: 1061
        - Player: 4: Songhai
        
        ### 2
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15100
        - Player: 4: Songhai
        - Plots:
          - Desert Land 48,22:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 47,22:
            - Owner: Songhai
            - CityID: 1061
            - Population: 20
            - IsRiver: true
            - City: Gao
            - Religion: Hinduism
            - Route: Railroad
        
        ### 3
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15101
        - Player: 4: Songhai
        - Plots:
          - Desert Land 48,22:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 47,22:
            - Owner: Songhai
            - CityID: 1061
            - Population: 20
            - IsRiver: true
            - City: Gao
            - Religion: Hinduism
            - Route: Railroad
        
        ### 4
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16027
        - Player: 4: Songhai
        - Desert Land 48,22:
          - Owner: Songhai
          - IsRiver: true
          - Improvement: Village
          - Route: Railroad
          - Feature: Flood Plains
        
        ### 5
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Rifleman
          - ID: 14908
        - Player: 4: Songhai
        - Desert Land 48,22:
          - Owner: Songhai
          - IsRiver: true
          - Improvement: Village
          - Route: Railroad
          - Feature: Flood Plains
        
        ### 6
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15958
        - Player: 4: Songhai
        - Desert Land 47,22:
          - Owner: Songhai
          - CityID: 1061
          - Population: 20
          - IsRiver: true
          - City: Gao
          - Religion: Hinduism
          - Route: Railroad
        
        ### 7
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16025
        - Player: 4: Songhai
        - Desert Land 48,22:
          - Owner: Songhai
          - IsRiver: true
          - Improvement: Village
          - Route: Railroad
          - Feature: Flood Plains
        
        ### 8
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16097
        - Player: 4: Songhai
        - Plots:
          - Desert Land 48,22:
            - Owner: Songhai
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 47,22:
            - Owner: Songhai
            - CityID: 1061
            - Population: 20
            - IsRiver: true
            - City: Gao
            - Religion: Hinduism
            - Route: Railroad
          - Grass Hills 46,22:
            - Owner: Songhai
            - Improvement: Mine
        
        ### 9
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 16100
        - Player: 4: Songhai
        - Grass Land 57,30:
          - Owner: Songhai
          - CityID: 5139
          - Population: 19
          - IsRiver: true
          - City: Tondibi
          - Religion: Hinduism
          - Route: Railroad
        
        ### 10
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16861
        - Player: 4: Songhai
        - Desert Land 47,22:
          - Owner: Songhai
          - CityID: 1061
          - Population: 20
          - IsRiver: true
          - City: Gao
          - Religion: Hinduism
          - Route: Railroad
        
        ### 11
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Diplomat
          - ID: 16862
        - Player: 5: Austria
        - Grass Land 61,22:
          - Owner: Austria
          - CityID: 1062
          - Population: 24
          - IsRiver: true
          - City: Vienna
          - Religion: Hinduism
          - Route: Railroad
        
        ### 12
        - Type: UnitCreated
        - UnitType: Diplomat
        - Player: 5: Austria
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 16862
        - Grass Land 61,22:
          - Owner: Austria
          - CityID: 1062
          - Population: 24
          - IsRiver: true
          - City: Vienna
          - Religion: Hinduism
          - Route: Railroad
        
        ### 13
        - Type: CityTrained
        - WithGold: true
        - Player: 5: Austria
        - City:
          - Name: Vienna
          - Population: 24
          - ID: 1062
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 16862
        
        ### 14
        - Type: CityConstructed
        - City:
          - Name: Vienna
          - Population: 24
          - ID: 1062
        - Owner: 5: Austria
        - Building: Coaling Station
        
        ### 15
        - Type: CityConstructed
        - City:
          - Name: Graz
          - Population: 25
          - ID: 2223
        - Owner: 5: Austria
        - Building: Wire Service
        
        ### 16
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15454
        - Player: 5: Austria
        - Plots:
          - Grass Land 60,23:
            - Owner: Austria
            - IsRiver: true
            - Resource: Cattle
            - Improvement: Pasture
            - Route: Railroad
          - Grass Land 61,22:
            - Owner: Austria
            - CityID: 1062
            - Population: 24
            - IsRiver: true
            - City: Vienna
            - Religion: Hinduism
            - Route: Railroad
        
        ### 17
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 14825
        - Player: 5: Austria
        - Plains Hills 46,23:
          - Owner: Songhai
          - Resource: Sheep
          - Improvement: Pasture
        
        ### 18
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 14911
        - Player: 5: Austria
        - Plots:
          - Grass Land 60,23:
            - Owner: Austria
            - IsRiver: true
            - Resource: Cattle
            - Improvement: Pasture
            - Route: Railroad
          - Grass Land 61,22:
            - Owner: Austria
            - CityID: 1062
            - Population: 24
            - IsRiver: true
            - City: Vienna
            - Religion: Hinduism
            - Route: Railroad
        
        ### 19
        - Type: PlayerTradeRouteCompleted
        - Domain: 2
        - OriginPlayer: 5: Austria
        - OriginCity:
          - Name: Vienna
          - Population: 24
          - ID: 1062
        - DestinationCity:
          - Name: Belgrade
          - Population: 24
          - ID: 1069
        - DestinationPlayer: 26
        - Connection: Food
        
        ### 20
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 16864
        - Player: 5: Austria
        - Grass Land 61,22:
          - Owner: Austria
          - CityID: 1062
          - Population: 24
          - IsRiver: true
          - City: Vienna
          - Religion: Hinduism
          - Route: Railroad
        
        ### 21
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 5: Austria
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16864
        - Grass Land 61,22:
          - Owner: Austria
          - CityID: 1062
          - Population: 24
          - IsRiver: true
          - City: Vienna
          - Religion: Hinduism
          - Route: Railroad
        
        ### 22
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16512
        - Player: 5: Austria
        - Grass Land 60,23:
          - Owner: Austria
          - IsRiver: true
          - Resource: Cattle
          - Improvement: Pasture
          - Route: Railroad
        
        ### 23
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16031
        - Player: 5: Austria
        - Plots:
          - Grass Land 66,27:
            - Owner: City-State Kyiv
            - CityID: 1068
            - Population: 20
            - City: Kyiv
            - Religion: Protestantism
            - Route: Railroad
          - Grass Land 67,26:
            - Owner: City-State Kyiv
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 66,25:
            - Owner: City-State Kyiv
            - IsRiver: true
            - Resource: Coffee
            - Improvement: Embassy
            - Route: Railroad
          - Grass Land 65,25:
            - Owner: Austria
            - IsRiver: true
            - Improvement: Farm
        
        ### 24
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16176
        - Player: 5: Austria
        - Plots:
          - Grass Land 60,23:
            - Owner: Austria
            - IsRiver: true
            - Resource: Cattle
            - Improvement: Pasture
            - Route: Railroad
          - Grass Land 61,22:
            - Owner: Austria
            - CityID: 1062
            - Population: 24
            - IsRiver: true
            - City: Vienna
            - Religion: Hinduism
            - Route: Railroad
        
        ### 25
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15376
        - Player: 5: Austria
        - Plots:
          - Grass Land 62,29:
            - Owner: City-State Kuala Lumpur
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
          - Grass Land 63,30:
            - Owner: City-State Kyiv
            - IsRiver: true
            - Improvement: Farm
          - Grass Land 63,31:
            - Owner: City-State Kyiv
            - IsRiver: true
            - Resource: Wine
            - Improvement: Plantation
            - Route: Railroad
          - Grass Hills 64,31:
            - Owner: City-State Kyiv
            - CityID: 5698
            - Population: 18
            - IsRiver: true
            - City: Turfan
            - Route: Railroad
        
        ### 26
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 15102
        - Player: 5: Austria
        - Plots:
          - Grass Land 60,23:
            - Owner: Austria
            - IsRiver: true
            - Resource: Cattle
            - Improvement: Pasture
            - Route: Railroad
          - Grass Land 61,22:
            - Owner: Austria
            - CityID: 1062
            - Population: 24
            - IsRiver: true
            - City: Vienna
            - Religion: Hinduism
            - Route: Railroad
          - Plains Hills 62,22:
            - Owner: Austria
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 62,23:
            - Owner: Austria
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Hills 63,23:
            - Owner: Austria
            - IsRiver: true
            - Resource: Coal
            - Improvement: Town
            - Route: Railroad
          - Plains Land 64,23:
            - Owner: Austria
            - CityID: 2223
            - Population: 25
            - IsRiver: true
            - City: Graz
            - Resource: Bananas
            - Religion: Hinduism
            - Route: Railroad
        
        ### 27
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Rifleman
          - ID: 14212
        - Player: 5: Austria
        - Grass Land 62,29:
          - Owner: City-State Kuala Lumpur
          - IsRiver: true
          - Improvement: Farm
          - Route: Road
        
        ### 28
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 95%
          - AI: Defense
          - Unit: Grenzer
          - ID: 13989
        - Player: 5: Austria
        - Plots:
          - Grass Land 65,26:
            - Owner: City-State Kyiv
            - IsRiver: true
            - Improvement: Farm
          - Grass Land 64,25:
            - Owner: Austria
            - IsRiver: true
            - Improvement: Farm
        
        ### 29
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Rifleman
          - ID: 14256
        - Player: 5: Austria
        - Plots:
          - Plains Land 62,31:
            - Owner: City-State Kyiv
            - IsRiver: true
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Grass Land 63,30:
            - Owner: City-State Kyiv
            - IsRiver: true
            - Improvement: Farm
        
        ### 30
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Defense
          - Unit: Rifleman
          - ID: 14381
        - Player: 5: Austria
        - Grass Hills 61,31:
          - Owner: City-State Kyiv
          - Improvement: Mine
        
        ### 31
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 16865
        - Player: 5: Austria
        - Grass Land 61,22:
          - Owner: Austria
          - CityID: 1062
          - Population: 24
          - IsRiver: true
          - City: Vienna
          - Religion: Hinduism
          - Route: Railroad
        
        ### 32
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 5: Austria
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16865
        - Grass Land 61,22:
          - Owner: Austria
          - CityID: 1062
          - Population: 24
          - IsRiver: true
          - City: Vienna
          - Religion: Hinduism
          - Route: Railroad
        
        ### 33
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16865
        - Player: 5: Austria
        - Grass Land 60,23:
          - Owner: Austria
          - IsRiver: true
          - Resource: Cattle
          - Improvement: Pasture
          - Route: Railroad
        
        ### 34
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16362
        - Player: 6: The Netherlands
        - Plots:
          - Plains Hills 47,32:
            - Owner: The Netherlands
            - CityID: 1063
            - Population: 35
            - IsRiver: true
            - City: Amsterdam
            - Religion: Hinduism
            - Route: Railroad
          - Desert Land 49,35:
            - Owner: The Netherlands
            - CityID: 1490
            - Population: 27
            - IsRiver: true
            - City: Utrecht
            - Religion: Hinduism
            - Route: Railroad
        
        ### 35
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16524
        - Player: 6: The Netherlands
        - Grass Land 50,29:
          - Owner: The Netherlands
          - CityID: 1307
          - Population: 25
          - IsRiver: true
          - City: Rotterdam
          - Resource: Bananas
          - Religion: Hinduism
          - Route: Railroad
        
        ### 36
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16592
        - Player: 6: The Netherlands
        - Desert Land 49,35:
          - Owner: The Netherlands
          - CityID: 1490
          - Population: 27
          - IsRiver: true
          - City: Utrecht
          - Religion: Hinduism
          - Route: Railroad
        
        ### 37
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15825
        - Player: 6: The Netherlands
        - Plots:
          - Grass Hills 64,32:
            - Owner: City-State Kyiv
            - IsRiver: true
            - Resource: Stone
            - Improvement: Quarry
            - Route: Road
          - Grass Hills 64,31:
            - Owner: City-State Kyiv
            - CityID: 5698
            - Population: 18
            - IsRiver: true
            - City: Turfan
            - Route: Railroad
          - Grass Land 65,30:
            - Owner: City-State Kyiv
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 65,29:
            - Owner: City-State Kyiv
            - Improvement: Village
            - Route: Railroad
          - Grass Hills 66,28:
            - Owner: City-State Kyiv
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 66,27:
            - Owner: City-State Kyiv
            - CityID: 1068
            - Population: 20
            - City: Kyiv
            - Religion: Protestantism
            - Route: Railroad
        
        ### 38
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: CityBombard
          - Unit: Artillery
          - ID: 15679
        - Player: 6: The Netherlands
        - Grass Land 50,29:
          - Owner: The Netherlands
          - CityID: 1307
          - Population: 25
          - IsRiver: true
          - City: Rotterdam
          - Resource: Bananas
          - Religion: Hinduism
          - Route: Railroad
        
        ### 39
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15902
        - Player: 6: The Netherlands
        - Grass Land 50,29:
          - Owner: The Netherlands
          - CityID: 1307
          - Population: 25
          - IsRiver: true
          - City: Rotterdam
          - Resource: Bananas
          - Religion: Hinduism
          - Route: Railroad
        
        ### 40
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: CityBombard
          - Unit: Artillery
          - ID: 16294
        - Player: 6: The Netherlands
        - Grass Land 50,29:
          - Owner: The Netherlands
          - CityID: 1307
          - Population: 25
          - IsRiver: true
          - City: Rotterdam
          - Resource: Bananas
          - Religion: Hinduism
          - Route: Railroad
        
        ### 41
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Rifleman
          - ID: 16683
        - Player: 6: The Netherlands
        - Grass Land 50,29:
          - Owner: The Netherlands
          - CityID: 1307
          - Population: 25
          - IsRiver: true
          - City: Rotterdam
          - Resource: Bananas
          - Religion: Hinduism
          - Route: Railroad
        
        ### 42
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Light Tank
          - ID: 16772
        - Player: 6: The Netherlands
        - Plots:
          - Plains Hills 47,32:
            - Owner: The Netherlands
            - CityID: 1063
            - Population: 35
            - IsRiver: true
            - City: Amsterdam
            - Religion: Hinduism
            - Route: Railroad
          - Grass Land 50,29:
            - Owner: The Netherlands
            - CityID: 1307
            - Population: 25
            - IsRiver: true
            - City: Rotterdam
            - Resource: Bananas
            - Religion: Hinduism
            - Route: Railroad
        
        ### 43
        - Type: CombatResult
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 31
          - Damage: 92
          - Unit:
            - Level: 4
            - Health: 39%
            - AI: AssaultSea
            - Unit: Dreadnought
            - ID: 14868
          - Player: 2: Germany
        
        ### 44
        - Type: CombatResult
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 8
          - Damage: 100
          - Player: 2: Germany
          - Unit:
            - Level: 4
            - Health: 8%
            - AI: AssaultSea
            - Unit: Dreadnought
            - ID: 14868
        
        ### 45
        - Type: UnitKilledInCombat
        - KilledPlayer: 2: Germany
        - KillerPlayer: 6: The Netherlands
        - KilledUnit: Dreadnought
        
        ### 46
        - Type: CombatResult
        - Attacker:
          - RemainingHP: 46
          - Damage: 46
        - Defender:
          - RemainingHP: 19
          - Damage: 19
          - Player: 2: Germany
          - Unit:
            - Level: 4
            - AI: DefenseAir
            - Unit: Fighter
            - ID: 16653
        
        ### 47
        - Type: CombatResult
        - Coast 30,31:
          - Owner: The Netherlands
          - Improvement: Polder
        - Attacker:
          - RemainingHP: 6
          - Damage: 23
        - Defender:
          - RemainingHP: 29
          - Damage: 29
          - Player: 2: Germany
          - Unit:
            - Level: 5
            - AI: Ranged
            - Unit: Light Tank
            - ID: 15259
        
        ### 48
        - Type: UnitMoved
        - Unit:
          - Level: 8
          - Health: 84%
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 14482
        - Player: 6: The Netherlands
        - Desert Hills 30,32:
          - Owner: The Netherlands
          - Resource: Aluminum
          - Improvement: Mine
        
        ### 49
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 81%
          - AI: Defense
          - Unit: Rifleman
          - ID: 13998
        - Player: 6: The Netherlands
        - Desert Land 31,32:
          - Owner: The Netherlands
          - Feature: Oasis
        
        ### 50
        - Type: CombatResult
        - Coast 30,31:
          - Owner: The Netherlands
          - Improvement: Polder
        - Attacker:
          - RemainingHP: 21
          - Damage: 43
        - Defender:
          - RemainingHP: 51
          - Damage: 80
          - Player: 2: Germany
          - Unit:
            - Level: 5
            - Health: 71%
            - AI: Ranged
            - Unit: Light Tank
            - ID: 15259
        
        ### 51
        - Type: CombatResult
        - Coast 30,31:
          - Owner: The Netherlands
          - Improvement: Polder
        - Attacker:
          - RemainingHP: 15
          - Damage: 34
        - Defender:
          - RemainingHP: 28
          - Damage: 108
          - Player: 2: Germany
          - Unit:
            - Level: 5
            - Health: 20%
            - AI: Ranged
            - Unit: Light Tank
            - ID: 15259
        
        ### 52
        - Type: UnitKilledInCombat
        - KilledPlayer: 2: Germany
        - KillerPlayer: 6: The Netherlands
        - KilledUnit: Light Tank
        
        ### 53
        - Type: UnitMoved
        - Unit:
          - Level: 8
          - Health: 72%
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 14482
        - Player: 6: The Netherlands
        - Coast 30,31:
          - Owner: The Netherlands
          - Improvement: Polder
        
        ### 54
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 80%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 10448
        - Player: 6: The Netherlands
        - Plots:
          - Coast 25,9:
            - Owner: Germany
            - Resource: Fish
          - Coast 26,9:
            - Owner: Germany
          - Coast 25,8:
            - Owner: Germany
            - Resource: Fish
          - Coast 25,7:
            - Owner: Germany
        
        ### 55
        - Type: CombatResult
        - Plains Land 26,11:
          - Owner: Germany
          - Resource: Figs
          - Improvement: Plantation
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 19
          - Damage: 37
          - Player: 1: Rome
          - Unit:
            - Level: 4
            - Health: 85%
            - AI: Defense
            - Unit: Rifleman
            - ID: 13275
        
        ### 56
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 80%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 10811
        - Player: 6: The Netherlands
        - Plots:
          - Coast 26,13:
            - Owner: Germany
            - Resource: Fish
          - Coast 28,12:
            - Owner: The Netherlands
        
        ### 57
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - Health: 35%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 15615
        - Player: 6: The Netherlands
        
        ### 58
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 80%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 10448
        - Player: 6: The Netherlands
        
        ### 59
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - Health: 35%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 15615
        - Player: 6: The Netherlands
        
        ### 60
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 13231
        - Player: 6: The Netherlands
        - Plains Hills 47,32:
          - Owner: The Netherlands
          - CityID: 1063
          - Population: 35
          - IsRiver: true
          - City: Amsterdam
          - Religion: Hinduism
          - Route: Railroad
        
        ### 61
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 13406
        - Player: 6: The Netherlands
        - Plains Hills 47,32:
          - Owner: The Netherlands
          - CityID: 1063
          - Population: 35
          - IsRiver: true
          - City: Amsterdam
          - Religion: Hinduism
          - Route: Railroad
        
        ### 62
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 13891
        - Player: 6: The Netherlands
        - Plains Hills 47,32:
          - Owner: The Netherlands
          - CityID: 1063
          - Population: 35
          - IsRiver: true
          - City: Amsterdam
          - Religion: Hinduism
          - Route: Railroad
        
        ### 63
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 15970
        - Player: 6: The Netherlands
        - Plots:
          - Plains Hills 47,32:
            - Owner: The Netherlands
            - CityID: 1063
            - Population: 35
            - IsRiver: true
            - City: Amsterdam
            - Religion: Hinduism
            - Route: Railroad
          - Desert Land 49,35:
            - Owner: The Netherlands
            - CityID: 1490
            - Population: 27
            - IsRiver: true
            - City: Utrecht
            - Religion: Hinduism
            - Route: Railroad
        
        ### 64
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 16867
        - Player: 6: The Netherlands
        - Grass Land 50,29:
          - Owner: The Netherlands
          - CityID: 1307
          - Population: 25
          - IsRiver: true
          - City: Rotterdam
          - Resource: Bananas
          - Religion: Hinduism
          - Route: Railroad
        
        ### 65
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 6: The Netherlands
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16867
        - Grass Land 50,29:
          - Owner: The Netherlands
          - CityID: 1307
          - Population: 25
          - IsRiver: true
          - City: Rotterdam
          - Resource: Bananas
          - Religion: Hinduism
          - Route: Railroad
        
        ### 66
        - Type: EspionageState
        - SpyIndex: 0
        - SpyState: 4
        - City:
          - Owner: City-State Ouagadougou
          - CityID: 1065
          - Population: 17
          - City: Ouagadougou
          - Terrain: Tundra
          - Resource: Glass
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 5
          - Y: 8
        - SpyOwner: 7: Mongolia
        
        ### 67
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Musketman
          - ID: 14388
        - Player: 7: Mongolia
        - Coast 66,38:
          - Owner: Mongolia
        
        ### 68
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 13168
        - Player: 22
        - Plots:
          - Coast 7,11:
            - Owner: City-State Ouagadougou
            - Resource: Fish
        
        ### 69
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 16716
        - Player: 22
        - Plots:
          - Coast 5,12:
            - Owner: City-State Ouagadougou
            - Resource: Fish
        
        ### 70
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 11767
        - Player: 22
        - Plots:
          - Coast 6,7:
            - Owner: City-State Ouagadougou
          - Coast 6,8:
            - Owner: City-State Ouagadougou
          - Coast 5,9:
            - Owner: City-State Ouagadougou
        
        ### 71
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 99%
          - AI: AssaultSea
          - Unit: Cruiser
          - ID: 14561
        - Player: 22
        - Plots:
          - Coast 5,12:
            - Owner: City-State Ouagadougou
            - Resource: Fish
        
        ### 72
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 16716
        - Player: 22
        - Plots:
          - Coast 5,12:
            - Owner: City-State Ouagadougou
            - Resource: Fish
          - Coast 5,11:
            - Owner: City-State Ouagadougou
        
        ### 73
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 11766
        - Player: 22
        - Plots:
          - Coast 7,8:
            - Owner: City-State Ouagadougou
          - Coast 7,9:
            - Owner: City-State Ouagadougou
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 7,11:
            - Owner: City-State Ouagadougou
            - Resource: Fish
        
        ### 74
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 11953
        - Player: 22
        - Plots:
          - Coast 7,8:
            - Owner: City-State Ouagadougou
          - Coast 6,10:
            - Owner: City-State Ouagadougou
        
        ### 75
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 11765
        - Player: 22
        - Plots:
          - Coast 4,8:
            - Owner: City-State Ouagadougou
          - Coast 4,9:
            - Owner: City-State Ouagadougou
        
        ### 76
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 11869
        - Player: 22
        
        ### 77
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 11952
        - Player: 22
        - Plots:
          - Tundra Land 5,8:
            - Owner: City-State Ouagadougou
            - CityID: 1065
            - Population: 17
            - City: Ouagadougou
            - Resource: Glass
            - Religion: Protestantism
            - Route: Railroad
          - Coast 6,8:
            - Owner: City-State Ouagadougou
          - Coast 7,11:
            - Owner: City-State Ouagadougou
            - Resource: Fish
        
        ### 78
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 11954
        - Player: 22
        - Plots:
          - Coast 5,11:
            - Owner: City-State Ouagadougou
          - Coast 5,12:
            - Owner: City-State Ouagadougou
            - Resource: Fish
        
        ### 79
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 11872
        - Player: 22
        - Plots:
          - Coast 7,8:
            - Owner: City-State Ouagadougou
          - Coast 6,10:
            - Owner: City-State Ouagadougou
        
        ### 80
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 10976
        - Player: 22
        - Plots:
          - Coast 4,7:
            - Owner: City-State Ouagadougou
            - Resource: Fish
            - Improvement: Fishing Boats
          - Tundra Land 5,8:
            - Owner: City-State Ouagadougou
            - CityID: 1065
            - Population: 17
            - City: Ouagadougou
            - Resource: Glass
            - Religion: Protestantism
            - Route: Railroad
          - Coast 5,9:
            - Owner: City-State Ouagadougou
          - Coast 6,10:
            - Owner: City-State Ouagadougou
        
        ### 81
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 11870
        - Player: 22
        - Plots:
          - Coast 4,9:
            - Owner: City-State Ouagadougou
          - Coast 4,8:
            - Owner: City-State Ouagadougou
          - Coast 4,7:
            - Owner: City-State Ouagadougou
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 82
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 12092
        - Player: 22
        - Plots:
          - Coast 6,8:
            - Owner: City-State Ouagadougou
          - Tundra Land 5,8:
            - Owner: City-State Ouagadougou
            - CityID: 1065
            - Population: 17
            - City: Ouagadougou
            - Resource: Glass
            - Religion: Protestantism
            - Route: Railroad
          - Coast 4,7:
            - Owner: City-State Ouagadougou
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 83
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 12547
        - Player: 22
        - Plots:
          - Coast 5,4:
            - Owner: City-State Ouagadougou
            - Improvement: Kampong
          - Coast 4,5:
            - Owner: City-State Ouagadougou
          - Coast 4,6:
            - Owner: City-State Ouagadougou
        
        ### 84
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 10815
        - Player: 22
        - Coast 6,7:
          - Owner: City-State Ouagadougou
        
        ### 85
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 11871
        - Player: 22
        - Coast 7,8:
          - Owner: City-State Ouagadougou
        
        ### 86
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 11869
        - Player: 22
        - Plots:
          - Coast 7,9:
            - Owner: City-State Ouagadougou
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 87
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 11872
        - Player: 22
        
        ### 88
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 11953
        - Player: 22
        - Coast 6,10:
          - Owner: City-State Ouagadougou
        
        ### 89
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 11954
        - Player: 22
        
        ### 90
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 99%
          - AI: AssaultSea
          - Unit: Cruiser
          - ID: 14561
        - Player: 22
        - Plots:
          - Coast 5,12:
            - Owner: City-State Ouagadougou
            - Resource: Fish
        
        ### 91
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 95%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16717
        - Player: 25
        - Plots:
          - Plains Land 64,33:
            - Owner: Mongolia
          - Plains Hills 64,34:
            - Owner: Mongolia
            - Improvement: Ordo
        
        ### 92
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 95%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16804
        - Player: 25
        - Plots:
          - Plains Land 62,31:
            - Owner: City-State Kyiv
            - IsRiver: true
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Grass Land 63,31:
            - Owner: City-State Kyiv
            - IsRiver: true
            - Resource: Wine
            - Improvement: Plantation
            - Route: Railroad
          - Grass Hills 64,31:
            - Owner: City-State Kyiv
            - CityID: 5698
            - Population: 18
            - IsRiver: true
            - City: Turfan
            - Route: Railroad
          - Grass Land 65,30:
            - Owner: City-State Kyiv
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 65,29:
            - Owner: City-State Kyiv
            - Improvement: Village
            - Route: Railroad
        
        ### 93
        - Type: CombatResult
        - Tundra Land 30,47:
          - Owner: City-State Shedet
          - IsRiver: true
          - Improvement: Lumber Mill
          - Feature: Forest
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 29
          - Damage: 33
          - Unit:
            - Level: 5
            - Health: 96%
            - AI: Ranged
            - Unit: Machine Gun
            - ID: 15073
          - Player: 2: Germany
        
        ### 94
        - Type: CombatResult
        - Tundra Land 30,47:
          - Owner: City-State Shedet
          - IsRiver: true
          - Improvement: Lumber Mill
          - Feature: Forest
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 35
          - Damage: 68
          - Unit:
            - Level: 5
            - Health: 67%
            - AI: Ranged
            - Unit: Machine Gun
            - ID: 15073
          - Player: 2: Germany
        
        ### 95
        - Type: CombatResult
        - Grass Land 13,26:
          - Owner: City-State Ormus
          - Improvement: Embassy
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 21
          - Damage: 21
          - Unit:
            - Level: 4
            - AI: Defense
            - Unit: Infantry
            - ID: 15727
          - Player: 2: Germany
        
        ### 96
        - Type: CombatResult
        - Grass Land 13,26:
          - Owner: City-State Ormus
          - Improvement: Embassy
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 34
          - Damage: 55
          - Unit:
            - Level: 4
            - Health: 83%
            - AI: Defense
            - Unit: Infantry
            - ID: 15727
          - Player: 2: Germany
        
        ### 97
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 8752
        - Player: 35
        - Plots:
          - Ocean 17,29:
            - Owner: Germany
          - Ocean 18,30:
            - Owner: Germany
          - Ocean 17,28:
            - Owner: Germany
          - Coast 16,27:
            - Owner: City-State Ormus
        
        ### 98
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Ironclad
          - ID: 16884
        - Player: 63: Barbarians
        - Coast 5,12:
          - Owner: City-State Ouagadougou
          - Resource: Fish
        
        ### 99
        - Type: UnitCreated
        - UnitType: Ironclad
        - Player: 63: Barbarians
        - Unit:
          - Level: 1
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 16884
        - Coast 5,12:
          - Owner: City-State Ouagadougou
          - Resource: Fish
        
        ## Turn 384
        
        ### 0
        - Type: CityConvertsReligion
        - City:
          - Owner: Germany
          - CityID: 14799
          - Population: 14
          - IsRiver: true
          - City: Valletta
          - Terrain: Plains
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 18
          - Y: 48
        - Owner: 2: Germany
        - Religion: Protestantism
        
        ### 1
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Foreign Legion
          - ID: 16891
        - Player: 1: Rome
        - Plains Land 65,18:
          - Owner: Rome
          - IsRiver: true
          - Resource: Salt
          - Improvement: Mine
          - Route: Railroad
        
        ### 2
        - Type: UnitCreated
        - UnitType: Foreign Legion
        - Player: 1: Rome
        - Unit:
          - Level: 1
          - AI: Attack
          - Unit: Foreign Legion
          - ID: 16891
        - Plains Land 65,18:
          - Owner: Rome
          - IsRiver: true
          - Resource: Salt
          - Improvement: Mine
          - Route: Railroad
        
        ### 3
        - Type: CityTrained
        - WithGold: true
        - Player: 1: Rome
        - City:
          - Name: Surabaya
          - Population: 20
          - ID: 10721
        - Unit:
          - Level: 1
          - AI: Attack
          - Unit: Foreign Legion
          - ID: 16891
        
        ### 4
        - Type: EspionageState
        - SpyIndex: 1
        - SpyState: 1
        - City:
          - Owner: Germany
          - CityID: 14797
          - Population: 22
          - City: Medan
          - Terrain: Desert
          - Resource: Cloves
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Hills
          - X: 67
          - Y: 20
        - SpyOwner: 1: Rome
        
        ### 5
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: Attack
          - Unit: Foreign Legion
          - ID: 16891
        - Player: 1: Rome
        - Promotions:
          - Shock I
          - Amphibious
          - Shock II
        
        ### 6
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 16726
        - Player: 1: Rome
        - Plots:
          - Ocean 66,13:
            - Owner: Rome
          - Ocean 66,14:
            - Owner: Rome
        
        ### 7
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Admiral
          - Unit: Great Admiral
          - ID: 16258
        - Player: 1: Rome
        - Plots:
          - Ocean 66,13:
            - Owner: Rome
          - Ocean 66,14:
            - Owner: Rome
        
        ### 8
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 55%
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 16820
        - Player: 1: Rome
        - Ocean 66,15:
          - Owner: Rome
        
        ### 9
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Rifleman
          - ID: 16471
        - Player: 1: Rome
        - Plots:
          - Plains Land 65,18:
            - Owner: Rome
            - IsRiver: true
            - Resource: Salt
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 64,19:
            - Owner: Rome
            - IsRiver: true
            - Improvement: Villa
            - Route: Road
          - Plains Land 65,20:
            - Owner: Germany
            - Resource: Figs
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 65,21:
            - Owner: Germany
            - Improvement: Mine
        
        ### 10
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: CityBombard
          - Unit: Artillery
          - ID: 15937
        - Player: 1: Rome
        - Plots:
          - Plains Land 63,15:
            - Owner: Rome
            - Improvement: Town
            - Route: Railroad
          - Plains Land 64,16:
            - Owner: Rome
            - Resource: Nutmeg
            - Improvement: Plantation
            - Route: Railroad
          - Plains Land 64,17:
            - Owner: Rome
            - CityID: 10721
            - Population: 20
            - IsRiver: true
            - City: Surabaya
            - Religion: Hinduism
            - Route: Railroad
        
        ### 11
        - Type: CombatResult
        - Plains Land 66,20:
          - Owner: Germany
          - Resource: Aluminum
          - Improvement: Mine
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 23
          - Damage: 26
          - Player: 2: Germany
          - Unit:
            - Level: 5
            - Health: 97%
            - AI: Defense
            - Unit: Infantry
            - ID: 16457
        
        ### 12
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 55%
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 16820
        - Player: 1: Rome
        - Ocean 65,15:
          - Owner: Rome
        
        ### 13
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15568
        - Player: 1: Rome
        - Plots:
          - Grass Land 63,18:
            - Owner: Rome
            - Improvement: Villa
            - Route: Railroad
          - Plains Hills 63,19:
            - Owner: Rome
            - Route: Railroad
          - Plains Land 64,20:
            - Owner: Germany
            - Resource: Deer
            - Improvement: Camp
            - Feature: Forest
        
        ### 14
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15505
        - Player: 1: Rome
        - Plots:
          - Grass Land 64,19:
            - Owner: Rome
            - IsRiver: true
            - Improvement: Villa
            - Route: Road
          - Plains Hills 63,19:
            - Owner: Rome
            - Route: Railroad
          - Grass Land 63,18:
            - Owner: Rome
            - Improvement: Villa
            - Route: Railroad
          - Grass Land 62,17:
            - Owner: Rome
            - Resource: Uranium
            - Route: Railroad
        
        ### 15
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 14954
        - Player: 1: Rome
        - Plots:
          - Grass Land 64,19:
            - Owner: Rome
            - IsRiver: true
            - Improvement: Villa
            - Route: Road
          - Desert Hills 65,19:
            - Owner: Rome
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
        
        ### 16
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: FastAttack
          - Unit: Landship
          - ID: 16905
        - Player: 1: Rome
        - Plots:
          - Plains Land 61,18:
            - Owner: Rome
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Hills 62,18:
            - Owner: Rome
            - IsRiver: true
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 63,18:
            - Owner: Rome
            - Improvement: Villa
            - Route: Railroad
          - Plains Hills 63,19:
            - Owner: Rome
            - Route: Railroad
          - Grass Land 64,19:
            - Owner: Rome
            - IsRiver: true
            - Improvement: Villa
            - Route: Road
          - Plains Land 65,20:
            - Owner: Germany
            - Resource: Figs
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
        
        ### 17
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 8527
        - Player: 1: Rome
        - Plots:
          - Grass Hills 63,14:
            - Owner: Rome
            - Improvement: Villa
            - Route: Railroad
          - Plains Land 63,15:
            - Owner: Rome
            - Improvement: Town
            - Route: Railroad
          - Plains Land 64,16:
            - Owner: Rome
            - Resource: Nutmeg
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 63,17:
            - Owner: Rome
            - Resource: Pepper
            - Improvement: Plantation
            - Route: Railroad
        
        ### 18
        - Type: CombatResult
        - Plains Land 66,20:
          - Owner: Germany
          - Resource: Aluminum
          - Improvement: Mine
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 14
          - Damage: 40
          - Unit:
            - Level: 5
            - Health: 79%
            - AI: Defense
            - Unit: Infantry
            - ID: 16457
          - Player: 2: Germany
        
        ### 19
        - Type: CombatResult
        - Grass Hills 61,21:
          - Owner: Austria
          - Improvement: Academy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 20
          - Damage: 100
          - Unit:
            - Level: 1
            - Health: 20%
            - AI: Musician
            - Unit: Great Musician
            - ID: 15580
          - Player: 2: Germany
        
        ### 20
        - Type: UnitKilledInCombat
        - KilledPlayer: 2: Germany
        - KillerPlayer: 1: Rome
        - KilledUnit: Great Musician
        
        ### 21
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 35%
          - AI: Defense
          - Unit: Rifleman
          - ID: 16385
        - Player: 1: Rome
        - Plains Land 64,18:
          - Owner: Rome
          - IsRiver: true
          - Resource: Figs
          - Improvement: Farm
          - Route: Railroad
        
        ### 22
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 14954
        - Player: 1: Rome
        - Plains Land 66,19:
          - Owner: Germany
          - Resource: Cloves
          - Improvement: Academy
        
        ### 23
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 86%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 16131
        - Player: 1: Rome
        - Plots:
          - Grass Hills 63,14:
            - Owner: Rome
            - Improvement: Villa
            - Route: Railroad
          - Plains Land 63,15:
            - Owner: Rome
            - Improvement: Town
            - Route: Railroad
          - Plains Land 64,16:
            - Owner: Rome
            - Resource: Nutmeg
            - Improvement: Plantation
            - Route: Railroad
          - Plains Land 64,17:
            - Owner: Rome
            - CityID: 10721
            - Population: 20
            - IsRiver: true
            - City: Surabaya
            - Religion: Hinduism
            - Route: Railroad
          - Plains Land 65,18:
            - Owner: Rome
            - IsRiver: true
            - Resource: Salt
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 65,19:
            - Owner: Rome
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
        
        ### 24
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Attack
          - Unit: Foreign Legion
          - ID: 16891
        - Player: 1: Rome
        - Desert Hills 65,19:
          - Owner: Rome
          - Resource: Sheep
          - Improvement: Pasture
          - Route: Railroad
        
        ### 25
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 86%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 16131
        - Player: 1: Rome
        - Plains Land 65,18:
          - Owner: Rome
          - IsRiver: true
          - Resource: Salt
          - Improvement: Mine
          - Route: Railroad
        
        ### 26
        - Type: CombatResult
        - Plains Land 66,20:
          - Owner: Germany
          - Resource: Aluminum
          - Improvement: Mine
          - Route: Railroad
        - Attacker:
          - RemainingHP: 30
          - Damage: 30
        - Defender:
          - RemainingHP: 23
          - Damage: 63
          - Player: 2: Germany
          - Unit:
            - Level: 5
            - Health: 68%
            - AI: Defense
            - Unit: Infantry
            - ID: 16457
        
        ### 27
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15936
        - Player: 1: Rome
        - Grass Land 63,18:
          - Owner: Rome
          - Improvement: Villa
          - Route: Railroad
        
        ### 28
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15564
        - Player: 1: Rome
        - Plots:
          - Grass Land 63,13:
            - Owner: Rome
            - Resource: Figs
            - Improvement: Lumber Mill
            - Route: Road
            - Feature: Forest
          - Grass Hills 64,14:
            - Owner: Rome
            - Resource: Iron
            - Improvement: Mine
        
        ### 29
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 12398
        - Player: 1: Rome
        - Tundra Land 27,7:
          - Owner: Germany
          - Resource: Stone
          - Improvement: Quarry
        
        ### 30
        - Type: CombatResult
        - Plains Land 27,8:
          - Owner: Germany
          - CityID: 16833
          - Population: 9
          - City: Satricum
          - Religion: Buddhism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 161
          - Damage: 322
          - Player: 2: Germany
        
        ### 31
        - Type: SetPopulation
        - OldPopulation: 9
        - NewPopulation: 0
        - City:
          - Owner: Germany
          - CityID: 16833
          - Population: 0
          - City: Satricum
          - Terrain: Plains
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 27
          - Y: 8
        
        ### 32
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        - Coast 27,5:
          - Resource: Fish
        
        ### 33
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        
        ### 34
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        - Plains Land 27,6:
          - Resource: Wheat
          - Improvement: Farm
        
        ### 35
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        
        ### 36
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        
        ### 37
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        - Tundra Land 26,7:
          - Improvement: Fort
        
        ### 38
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        - Tundra Land 27,7:
          - Resource: Stone
          - Improvement: Quarry
        
        ### 39
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        - Coast 25,8:
          - Resource: Fish
        
        ### 40
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        - Plains Land 26,8:
          - Improvement: Farm
        
        ### 41
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        - Plains Land 27,8:
          - Route: Railroad
        
        ### 42
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        
        ### 43
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        
        ### 44
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        - Coast 25,9:
          - Resource: Fish
        
        ### 45
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        
        ### 46
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        
        ### 47
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        - Plains Land 26,10:
          - Improvement: Villa
        
        ### 48
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        
        ### 49
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        
        ### 50
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        - Plains Land 26,11:
          - Resource: Figs
          - Improvement: Plantation
        
        ### 51
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        - Plains Land 28,11:
          - Feature: Forest
        
        ### 52
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        - Coast 26,12:
          - Resource: Coral
        
        ### 53
        - Type: TileOwnershipChanged
        - OldOwner: 2: Germany
        - Coast 26,13:
          - Resource: Fish
        
        ### 54
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Plains Land 27,8:
          - Owner: Rome
          - Route: Railroad
        
        ### 55
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Plains Land 26,8:
          - Owner: Rome
          - Improvement: Farm
        
        ### 56
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Coast 26,9:
          - Owner: Rome
        
        ### 57
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Tundra Land 26,7:
          - Owner: Rome
          - Improvement: Fort
        
        ### 58
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Coast 27,9:
          - Owner: Rome
        
        ### 59
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Tundra Land 27,7:
          - Owner: Rome
          - Resource: Stone
          - Improvement: Quarry
        
        ### 60
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Coast 28,8:
          - Owner: Rome
        
        ### 61
        - Type: SetPopulation
        - OldPopulation: 0
        - NewPopulation: 1
        - City:
          - Owner: Rome
          - CityID: 16908
          - Population: 1
          - City: Satricum
          - Terrain: Plains
          - Route: Railroad
          - Plot: Land
          - X: 27
          - Y: 8
        
        ### 62
        - Type: SetPopulation
        - OldPopulation: 1
        - NewPopulation: 9
        - City:
          - Owner: Rome
          - CityID: 16908
          - Population: 9
          - City: Satricum
          - Terrain: Plains
          - Route: Railroad
          - Plot: Land
          - X: 27
          - Y: 8
        
        ### 63
        - Type: CityConvertsReligion
        - City:
          - Owner: Rome
          - CityID: 16908
          - Population: 9
          - City: Satricum
          - Terrain: Plains
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 27
          - Y: 8
        - Owner: 1: Rome
        - Religion: Buddhism
        
        ### 64
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Coast 27,5:
          - Owner: Rome
          - Resource: Fish
        
        ### 65
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Coast 26,6:
          - Owner: Rome
        
        ### 66
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Plains Land 27,6:
          - Owner: Rome
          - Resource: Wheat
          - Improvement: Farm
        
        ### 67
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Coast 28,6:
          - Owner: Rome
        
        ### 68
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Coast 25,7:
          - Owner: Rome
        
        ### 69
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Coast 25,8:
          - Owner: Rome
          - Resource: Fish
        
        ### 70
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Coast 29,8:
          - Owner: Rome
        
        ### 71
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Coast 25,9:
          - Owner: Rome
          - Resource: Fish
        
        ### 72
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Plains Land 26,10:
          - Owner: Rome
          - Improvement: Villa
        
        ### 73
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Coast 27,10:
          - Owner: Rome
        
        ### 74
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Coast 28,10:
          - Owner: Rome
        
        ### 75
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Plains Land 26,11:
          - Owner: Rome
          - Resource: Figs
          - Improvement: Plantation
        
        ### 76
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Plains Land 28,11:
          - Owner: Rome
          - Feature: Forest
        
        ### 77
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Coast 26,12:
          - Owner: Rome
          - Resource: Coral
        
        ### 78
        - Type: TileOwnershipChanged
        - NewOwner: 1: Rome
        - Coast 26,13:
          - Owner: Rome
          - Resource: Fish
        
        ### 79
        - Type: CityCaptureComplete
        - Population: 9
        - IsConquest: true
        - TotalGreatWorks: 0
        - CapturedGreatWorks: 0
        - OldOwner: 2: Germany
        - City:
          - Owner: Rome
          - CityID: 16908
          - Population: 9
          - City: Satricum
          - Terrain: Plains
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 27
          - Y: 8
        - NewOwner: 1: Rome
        
        ### 80
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16548
        - Player: 1: Rome
        - Plains Land 27,8:
          - Owner: Rome
          - CityID: 16908
          - Population: 9
          - City: Satricum
          - Religion: Buddhism
          - Route: Railroad
        
        ### 81
        - Type: CombatResult
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 28
          - Damage: 48
          - Player: 6: The Netherlands
          - Unit:
            - Level: 6
            - Health: 80%
            - AI: AttackSea
            - Unit: Ironclad
            - ID: 10811
        
        ### 82
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15505
        - Player: 1: Rome
        - Grass Hills 61,17:
          - Owner: Rome
          - IsRiver: true
          - Improvement: Villa
          - Route: Railroad
        
        ### 83
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15419
        - Player: 1: Rome
        - Grass Hills 62,19:
          - Owner: Rome
          - Resource: Figs
          - Improvement: Mine
        
        ### 84
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 86%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 16131
        - Player: 1: Rome
        - Plots:
          - Plains Land 64,17:
            - Owner: Rome
            - CityID: 10721
            - Population: 20
            - IsRiver: true
            - City: Surabaya
            - Religion: Hinduism
            - Route: Railroad
          - Plains Land 64,16:
            - Owner: Rome
            - Resource: Nutmeg
            - Improvement: Plantation
            - Route: Railroad
          - Plains Land 63,15:
            - Owner: Rome
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 63,14:
            - Owner: Rome
            - Improvement: Villa
            - Route: Railroad
        
        ### 85
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 35%
          - AI: Defense
          - Unit: Rifleman
          - ID: 16385
        - Player: 1: Rome
        - Plots:
          - Plains Land 64,17:
            - Owner: Rome
            - CityID: 10721
            - Population: 20
            - IsRiver: true
            - City: Surabaya
            - Religion: Hinduism
            - Route: Railroad
          - Plains Land 64,16:
            - Owner: Rome
            - Resource: Nutmeg
            - Improvement: Plantation
            - Route: Railroad
          - Plains Land 63,15:
            - Owner: Rome
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 63,14:
            - Owner: Rome
            - Improvement: Villa
            - Route: Railroad
        
        ### 86
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 69%
          - AI: Defense
          - Unit: Rifleman
          - ID: 13275
        - Player: 1: Rome
        - Plots:
          - Plains Land 26,10:
            - Owner: Rome
            - Improvement: Villa
        
        ### 87
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 55%
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 16820
        - Player: 1: Rome
        - Plots:
          - Coast 65,16:
            - Owner: Rome
            - Improvement: Kampong
          - Plains Land 64,17:
            - Owner: Rome
            - CityID: 10721
            - Population: 20
            - IsRiver: true
            - City: Surabaya
            - Religion: Hinduism
            - Route: Railroad
        
        ### 88
        - Type: TileRouteChanged
        - OldRoute: 0
        - NewRoute: 1
        - Owner: 1: Rome
        - Grass Hills 60,18:
          - Owner: Rome
          - Resource: Coal
          - Improvement: Citadel
          - Route: Railroad
        
        ### 89
        - Type: BuildFinished
        - Player: 1: Rome
        - Grass Hills 60,18:
          - Owner: Rome
          - Resource: Coal
          - Improvement: Citadel
          - Route: Railroad
        
        ### 90
        - Type: UnitBuildCompleted
        - Owner: 1: Rome
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 6214
        - Build: Construct a Railroad
        - Grass Hills 60,18:
          - Owner: Rome
          - Resource: Coal
          - Improvement: Citadel
          - Route: Railroad
        
        ### 91
        - Type: UnitBuildStart
        - Owner: 1: Rome
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 6214
        - Build: Construct a Railroad
        - Grass Hills 60,18:
          - Owner: Rome
          - Resource: Coal
          - Improvement: Citadel
          - Route: Railroad
        
        ### 92
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3570
        - Player: 1: Rome
        - Grass Hills 61,17:
          - Owner: Rome
          - IsRiver: true
          - Improvement: Villa
          - Route: Railroad
        
        ### 93
        - Type: PlayerDoneTurn
        - NextPlayer: 2: Germany
        - Player: 1: Rome
        
        ### 94
        - Type: MakePeace
        - PacifierFlag: true
        - OriginatingPlayer: 2: Germany
        - TargetTeam:
          - Player_4: Askia
          - ID: 4
        
        ### 95
        - Type: MakePeace
        - PacifierFlag: true
        - OriginatingPlayer: 2: Germany
        - TargetTeam:
          - Player_4: Askia
          - ID: 4
        
        ### 96
        - Type: DealMade
        - StartTurn: 384
        - TradedItems:
          - #0:
            - Data1: 0
            - Data2: 0
            - Data3: 0
            - Duration: 10
            - FromPlayer: 2
            - Item: PeaceTreaty
          - #1:
            - Data1: 0
            - Data2: 0
            - Data3: 0
            - Duration: 10
            - FromPlayer: 4
            - Item: PeaceTreaty
          - #2:
            - Data1: 22
            - Data2: 0
            - Data3: 0
            - Duration: 10
            - FromPlayer: 4
            - Item: ThirdPartyPeace
        - ToPlayer: 4: Songhai
        - FromPlayer: 2: Germany
        
        ### 97
        - Type: CityInvestedBuilding
        - BuildingClass: Hospital
        - Invested: true
        - City:
          - Name: Zurich
          - Population: 19
          - ID: 14242
        - Player: 2: Germany
        
        ### 98
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Anti-Aircraft Gun
          - ID: 16909
        - Player: 2: Germany
        - Plains Land 15,38:
          - Owner: Germany
          - IsRiver: true
          - Resource: Wheat
          - Improvement: Manufactory
          - Route: Railroad
        
        ### 99
        - Type: UnitCreated
        - UnitType: Anti-Aircraft Gun
        - Player: 2: Germany
        - Unit:
          - Level: 1
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16909
        - Plains Land 15,38:
          - Owner: Germany
          - IsRiver: true
          - Resource: Wheat
          - Improvement: Manufactory
          - Route: Railroad
        
        ### 100
        - Type: CityTrained
        - WithGold: true
        - Player: 2: Germany
        - City:
          - Name: Berlin
          - Population: 47
          - ID: 1059
        - Unit:
          - Level: 1
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16909
        
        ### 101
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 16919
        - Player: 2: Germany
        - Grass Land 14,39:
          - Owner: Germany
          - CityID: 1059
          - Population: 47
          - IsRiver: true
          - City: Berlin
          - Religion: Protestantism
          - Route: Railroad
        
        ### 102
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 2: Germany
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16919
        - Grass Land 14,39:
          - Owner: Germany
          - CityID: 1059
          - Population: 47
          - IsRiver: true
          - City: Berlin
          - Religion: Protestantism
          - Route: Railroad
        
        ### 103
        - Type: CityTrained
        - Player: 2: Germany
        - City:
          - Name: Berlin
          - Population: 47
          - ID: 1059
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16919
        
        ### 104
        - Type: CityEndsWLTKD
        - Unused: 0
        - Owner: 2: Germany
        - Desert Hills 7,34:
          - Owner: Germany
          - CityID: 2191
          - Population: 31
          - City: Cologne
          - Resource: Aluminum
          - Religion: Protestantism
          - Route: Railroad
        
        ### 105
        - Type: SetPopulation
        - OldPopulation: 24
        - NewPopulation: 25
        - City:
          - Owner: Germany
          - CityID: 3320
          - Population: 25
          - City: Aachen
          - Terrain: Desert
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Hills
          - X: 11
          - Y: 32
        
        ### 106
        - Type: CityConvertsReligion
        - City:
          - Owner: Germany
          - CityID: 3320
          - Population: 25
          - City: Aachen
          - Terrain: Desert
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Hills
          - X: 11
          - Y: 32
        - Owner: 2: Germany
        - Religion: Protestantism
        
        ### 107
        - Type: SetPopulation
        - OldPopulation: 23
        - NewPopulation: 24
        - City:
          - Owner: Germany
          - CityID: 4709
          - Population: 24
          - IsRiver: true
          - City: Bremen
          - Terrain: Plains
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 14
          - Y: 45
        
        ### 108
        - Type: CityConvertsReligion
        - City:
          - Owner: Germany
          - CityID: 4709
          - Population: 24
          - IsRiver: true
          - City: Bremen
          - Terrain: Plains
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 14
          - Y: 45
        - Owner: 2: Germany
        - Religion: Protestantism
        
        ### 109
        - Type: CityEndsWLTKD
        - Unused: 0
        - Owner: 2: Germany
        - Plains Hills 72,37:
          - Owner: Germany
          - CityID: 5525
          - Population: 29
          - City: Leipzig
          - Resource: Coal
          - Religion: Protestantism
          - Route: Railroad
        
        ### 110
        - Type: CityBeginsWLTKD
        - Change: 10
        - City:
          - Owner: Germany
          - CityID: 5525
          - Population: 29
          - City: Leipzig
          - Terrain: Plains
          - Resource: Coal
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Hills
          - X: 72
          - Y: 37
        - Player: 2: Germany
        
        ### 111
        - Type: CityEventChoiceEnded
        - City:
          - Name: Samarinda
          - Population: 33
          - ID: 11109
        - Player: 2: Germany
        - Choice: 83
        
        ### 112
        - Type: CityEndsWLTKD
        - Unused: 0
        - Owner: 2: Germany
        - Grass Land 73,25:
          - Owner: Germany
          - CityID: 11109
          - Population: 33
          - City: Samarinda
          - Resource: Rice
          - Religion: Protestantism
          - Route: Railroad
        
        ### 113
        - Type: CityBeginsWLTKD
        - Change: 10
        - City:
          - Owner: Germany
          - CityID: 11109
          - Population: 33
          - City: Samarinda
          - Terrain: Grass
          - Resource: Rice
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 73
          - Y: 25
        - Player: 2: Germany
        
        ### 114
        - Type: CityEndsWLTKD
        - Unused: 0
        - Owner: 2: Germany
        - Plains Hills 20,41:
          - Owner: Germany
          - CityID: 12865
          - Population: 26
          - City: Teotihuacan
          - Religion: Protestantism
          - Route: Railroad
        
        ### 115
        - Type: CityBeginsWLTKD
        - Change: 10
        - City:
          - Owner: Germany
          - CityID: 12865
          - Population: 26
          - City: Teotihuacan
          - Terrain: Plains
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Hills
          - X: 20
          - Y: 41
        - Player: 2: Germany
        
        ### 116
        - Type: CityConstructed
        - City:
          - Name: Zurich
          - Population: 19
          - ID: 14242
        - Owner: 2: Germany
        - Building: Stock Exchange
        
        ### 117
        - Type: CityEndsWLTKD
        - Unused: 0
        - Owner: 2: Germany
        - Plains Land 24,36:
          - Owner: Germany
          - CityID: 14242
          - Population: 19
          - City: Zurich
          - Resource: Glass
          - Religion: Protestantism
          - Route: Railroad
        
        ### 118
        - Type: CityConstructed
        - City:
          - Name: Medan
          - Population: 22
          - ID: 14797
        - Owner: 2: Germany
        - Building: Military Academy
        
        ### 119
        - Type: CityConstructed
        - City:
          - Name: Valletta
          - Population: 14
          - ID: 14799
        - Owner: 2: Germany
        - Building: Herbalist
        
        ### 120
        - Type: TileOwnershipChanged
        - NewOwner: 2: Germany
        - Coast 18,51:
          - Owner: Germany
          - Feature: Ice
        
        ### 121
        - Type: CityBoughtPlot
        - WithFaithCulture: true
        - Player: 2: Germany
        - City:
          - Name: Valletta
          - Population: 14
          - ID: 14799
        - Coast 18,51:
          - Owner: Germany
          - Feature: Ice
        
        ### 122
        - Type: CityConstructed
        - City:
          - Name: Tlatelolco
          - Population: 22
          - ID: 14971
        - Owner: 2: Germany
        - Building: Museum
        
        ### 123
        - Type: SetPopulation
        - OldPopulation: 5
        - NewPopulation: 3
        - City:
          - Owner: Germany
          - CityID: 16749
          - Population: 3
          - City: Ardea
          - Terrain: Desert
          - Resource: Stone
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Hills
          - X: 25
          - Y: 32
        
        ### 124
        - Type: CityConvertsReligion
        - City:
          - Owner: Germany
          - CityID: 16749
          - Population: 3
          - City: Ardea
          - Terrain: Desert
          - Resource: Stone
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Hills
          - X: 25
          - Y: 32
        - Owner: 2: Germany
        - Religion: Protestantism
        
        ### 125
        - Type: SetPopulation
        - OldPopulation: 13
        - NewPopulation: 11
        - City:
          - Owner: Germany
          - CityID: 16835
          - Population: 11
          - City: Tlaxcala
          - Terrain: Plains
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 32
          - Y: 40
        
        ### 126
        - Type: CityConvertsReligion
        - City:
          - Owner: Germany
          - CityID: 16835
          - Population: 11
          - City: Tlaxcala
          - Terrain: Plains
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 32
          - Y: 40
        - Owner: 2: Germany
        - Religion: Protestantism
        
        ### 127
        - Type: TeamTechResearched
        - ChangeAmount: 1
        - Team:
          - Player_2: Bismarck
          - ID: 2
        - Tech: Nuclear Fission
        
        ### 128
        - Type: TeamSetEra
        - NewEra: 7
        - Team:
          - Player_2: Bismarck
          - ID: 2
        
        ### 129
        - Type: EspionageState
        - SpyIndex: 8
        - SpyState: 3
        - City:
          - Owner: The Netherlands
          - CityID: 13035
          - Population: 16
          - IsRiver: true
          - City: Atzcapotzalco
          - Terrain: Desert
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Hills
          - X: 33
          - Y: 17
        - SpyOwner: 2: Germany
        
        ### 130
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 14618
        - Player: 2: Germany
        - Plots:
          - Coast 8,6:
            - Owner: City-State Ouagadougou
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 7,8:
            - Owner: City-State Ouagadougou
          - Coast 6,8:
            - Owner: City-State Ouagadougou
        
        ### 131
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 15175
        - Player: 2: Germany
        - Plots:
          - Coast 10,45:
            - Owner: Germany
          - Grass Land 11,46:
            - Owner: Germany
            - CityID: 1927
            - Population: 29
            - IsRiver: true
            - City: Munich
            - Religion: Protestantism
            - Route: Railroad
        
        ### 132
        - Type: PlayerTradeRouteCompleted
        - Domain: 0
        - OriginPlayer: 2: Germany
        - OriginCity:
          - Name: Munich
          - Population: 29
          - ID: 1927
        - DestinationCity:
          - Name: Ormus
          - Population: 23
          - ID: 1078
        - DestinationPlayer: 35
        - Connection: Food
        
        ### 133
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Cargo Ship
          - ID: 16920
        - Player: 2: Germany
        - Grass Land 11,46:
          - Owner: Germany
          - CityID: 1927
          - Population: 29
          - IsRiver: true
          - City: Munich
          - Religion: Protestantism
          - Route: Railroad
        
        ### 134
        - Type: UnitCreated
        - UnitType: Cargo Ship
        - Player: 2: Germany
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16920
        - Grass Land 11,46:
          - Owner: Germany
          - CityID: 1927
          - Population: 29
          - IsRiver: true
          - City: Munich
          - Religion: Protestantism
          - Route: Railroad
        
        ### 135
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15650
        - Player: 2: Germany
        - Plots:
          - Plains Land 12,44:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 11,45:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 11,46:
            - Owner: Germany
            - CityID: 1927
            - Population: 29
            - IsRiver: true
            - City: Munich
            - Religion: Protestantism
            - Route: Railroad
          - Desert Land 12,43:
            - Owner: Germany
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
        
        ### 136
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16330
        - Player: 2: Germany
        - Plots:
          - Coast 9,33:
            - Owner: Germany
          - Coast 9,34:
            - Owner: Germany
          - Coast 8,34:
            - Owner: Germany
            - Resource: Fish
            - Improvement: Fishing Boats
          - Desert Hills 7,34:
            - Owner: Germany
            - CityID: 2191
            - Population: 31
            - City: Cologne
            - Resource: Aluminum
            - Religion: Protestantism
            - Route: Railroad
        
        ### 137
        - Type: PlayerTradeRouteCompleted
        - Domain: 0
        - OriginPlayer: 2: Germany
        - OriginCity:
          - Name: Cologne
          - Population: 31
          - ID: 2191
        - DestinationCity:
          - Name: Veligrad
          - Population: 20
          - ID: 1067
        - DestinationPlayer: 24
        - Connection: Food
        
        ### 138
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Cargo Ship
          - ID: 16921
        - Player: 2: Germany
        - Desert Hills 7,34:
          - Owner: Germany
          - CityID: 2191
          - Population: 31
          - City: Cologne
          - Resource: Aluminum
          - Religion: Protestantism
          - Route: Railroad
        
        ### 139
        - Type: UnitCreated
        - UnitType: Cargo Ship
        - Player: 2: Germany
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16921
        - Desert Hills 7,34:
          - Owner: Germany
          - CityID: 2191
          - Population: 31
          - City: Cologne
          - Resource: Aluminum
          - Religion: Protestantism
          - Route: Railroad
        
        ### 140
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15352
        - Player: 2: Germany
        - Plots:
          - Desert Hills 17,39:
            - Owner: Germany
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 16,39:
            - Owner: Germany
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Desert Hills 15,39:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Grass Land 14,39:
            - Owner: Germany
            - CityID: 1059
            - Population: 47
            - IsRiver: true
            - City: Berlin
            - Religion: Protestantism
            - Route: Railroad
        
        ### 141
        - Type: PlayerTradeRouteCompleted
        - Domain: 2
        - OriginPlayer: 2: Germany
        - OriginCity:
          - Name: Berlin
          - Population: 47
          - ID: 1059
        - DestinationCity:
          - Population: 20
          - Name: Shedet
          - Health: -18%
          - ID: 1072
        - DestinationPlayer: 29
        - Connection: Food
        
        ### 142
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 16922
        - Player: 2: Germany
        - Grass Land 14,39:
          - Owner: Germany
          - CityID: 1059
          - Population: 47
          - IsRiver: true
          - City: Berlin
          - Religion: Protestantism
          - Route: Railroad
        
        ### 143
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 2: Germany
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16922
        - Grass Land 14,39:
          - Owner: Germany
          - CityID: 1059
          - Population: 47
          - IsRiver: true
          - City: Berlin
          - Religion: Protestantism
          - Route: Railroad
        
        ### 144
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15735
        - Player: 2: Germany
        - Plots:
          - Plains Land 13,39:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 14,40:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Plains Land 13,41:
            - Owner: Germany
            - Resource: Tea
            - Improvement: Town
            - Route: Railroad
          - Plains Land 13,42:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
        
        ### 145
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16407
        - Player: 2: Germany
        - Plots:
          - Desert Hills 16,34:
            - Owner: Germany
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 15,35:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Desert Hills 15,36:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Holy Site
            - Route: Railroad
          - Desert Land 15,37:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 15,38:
            - Owner: Germany
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Land 14,39:
            - Owner: Germany
            - CityID: 1059
            - Population: 47
            - IsRiver: true
            - City: Berlin
            - Religion: Protestantism
            - Route: Railroad
        
        ### 146
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 14438
        - Player: 2: Germany
        - Plots:
          - Coast 6,42:
            - Owner: Germany
          - Coast 7,42:
            - Owner: Germany
          - Coast 7,43:
            - Owner: Germany
          - Coast 8,44:
            - Owner: Germany
        
        ### 147
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16081
        - Player: 2: Germany
        - Plots:
          - Desert Hills 17,39:
            - Owner: Germany
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 16,39:
            - Owner: Germany
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Desert Hills 15,39:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Grass Land 14,39:
            - Owner: Germany
            - CityID: 1059
            - Population: 47
            - IsRiver: true
            - City: Berlin
            - Religion: Protestantism
            - Route: Railroad
        
        ### 148
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16408
        - Player: 2: Germany
        - Plots:
          - Plains Hills 14,40:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Plains Land 13,41:
            - Owner: Germany
            - Resource: Tea
            - Improvement: Town
            - Route: Railroad
          - Plains Land 13,42:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Plains Land 13,43:
            - Owner: Germany
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 14,44:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 14,45:
            - Owner: Germany
            - CityID: 4709
            - Population: 24
            - IsRiver: true
            - City: Bremen
            - Religion: Protestantism
            - Route: Railroad
        
        ### 149
        - Type: EspionageState
        - SpyIndex: 11
        - SpyState: 1
        - City:
          - Owner: Rome
          - CityID: 1058
          - Population: 38
          - IsRiver: true
          - City: Rome
          - Terrain: Plains
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 52
          - Y: 7
        - SpyOwner: 2: Germany
        
        ### 150
        - Type: EspionageState
        - SpyIndex: 12
        - SpyState: 1
        - City:
          - Owner: Rome
          - CityID: 2920
          - Population: 24
          - IsRiver: true
          - City: Mediolanum
          - Terrain: Tundra
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Hills
          - X: 49
          - Y: 5
        - SpyOwner: 2: Germany
        
        ### 151
        - Type: PlayerDoTurn
        - Player: 2: Germany
        
        ### 152
        - Type: UnitPromoted
        - Unit:
          - Level: 6
          - AI: CityBombard
          - Unit: Krupp Gun
          - ID: 13445
        - Player: 2: Germany
        - Promotion: Splash I
        
        ### 153
        - Type: UnitPromoted
        - Unit:
          - Level: 5
          - AI: CityBombard
          - Unit: Krupp Gun
          - ID: 16142
        - Player: 2: Germany
        - Promotion: Field III
        
        ### 154
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16909
        - Player: 2: Germany
        - Promotions:
          - Shock I
          - Amphibious
        
        ### 155
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Defense
          - Unit: Infantry
          - ID: 15718
        - Player: 2: Germany
        - Snow Hills 27,47:
          - Owner: Germany
          - Improvement: Mine
        
        ### 156
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 32%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15073
        - Player: 2: Germany
        - Plots:
          - Tundra Land 29,47:
            - Owner: Germany
          - Snow Hills 28,47:
            - Owner: Germany
            - Improvement: Mine
        
        ### 157
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 14310
        - Player: 2: Germany
        - Plots:
          - Coast 27,32:
            - Owner: Germany
          - Coast 27,33:
            - Owner: Germany
            - Resource: Oil
          - Coast 30,34:
            - Owner: The Netherlands
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 158
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 76%
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 14879
        - Player: 2: Germany
        - Plots:
          - Coast 26,31:
            - Owner: Germany
          - Coast 27,32:
            - Owner: Germany
          - Coast 27,33:
            - Owner: Germany
            - Resource: Oil
        
        ### 159
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 76%
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 14791
        - Player: 2: Germany
        
        ### 160
        - Type: CombatResult
        - Coast 30,31:
          - Owner: The Netherlands
          - Improvement: Polder
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 32
          - Damage: 41
          - Player: 6: The Netherlands
          - Unit:
            - Level: 8
            - Health: 92%
            - AI: Paradrop
            - Unit: Paratrooper
            - ID: 14482
        
        ### 161
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 14362
        - Player: 2: Germany
        - Plots:
          - Coast 28,31:
            - Feature: Atoll
        
        ### 162
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 76%
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 14879
        - Player: 2: Germany
        - Coast 28,34:
          - Owner: Germany
          - Resource: Fish
        
        ### 163
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 14968
        - Player: 2: Germany
        - Coast 27,36:
          - Owner: Germany
          - Resource: Fish
          - Improvement: Fishing Boats
        
        ### 164
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 15342
        - Player: 2: Germany
        - Plots:
          - Desert Hills 25,32:
            - Owner: Germany
            - CityID: 16749
            - Population: 3
            - City: Ardea
            - Resource: Stone
            - Religion: Protestantism
            - Route: Railroad
          - Coast 26,32:
            - Owner: Germany
            - Improvement: Polder
          - Coast 27,32:
            - Owner: Germany
          - Coast 27,33:
            - Owner: Germany
            - Resource: Oil
          - Coast 27,34:
            - Owner: Germany
          - Desert Land 26,35:
            - Owner: Germany
            - Improvement: Fort
        
        ### 165
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Admiral
          - Unit: Great Admiral
          - ID: 14796
        - Player: 2: Germany
        - Plots:
          - Desert Hills 25,32:
            - Owner: Germany
            - CityID: 16749
            - Population: 3
            - City: Ardea
            - Resource: Stone
            - Religion: Protestantism
            - Route: Railroad
          - Coast 26,32:
            - Owner: Germany
            - Improvement: Polder
          - Coast 27,32:
            - Owner: Germany
          - Coast 27,33:
            - Owner: Germany
            - Resource: Oil
          - Coast 27,34:
            - Owner: Germany
          - Desert Land 26,35:
            - Owner: Germany
            - Improvement: Fort
        
        ### 166
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 16483
        - Player: 2: Germany
        - Plots:
          - Coast 25,30:
            - Owner: Germany
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 167
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: Defense
          - Unit: Infantry
          - ID: 15791
        - Player: 2: Germany
        - Plots:
          - Coast 10,24:
            - Resource: Fish
        
        ### 168
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Diplomat
          - Unit: Great Diplomat
          - ID: 16400
        - Player: 2: Germany
        - Plots:
          - Coast 10,24:
            - Resource: Fish
        
        ### 169
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 14437
        - Player: 2: Germany
        - Plots:
          - Coast 73,22:
            - Owner: Germany
            - Resource: Fish
            - Improvement: Fishing Boats
          - Ocean 72,22:
            - Owner: Germany
          - Ocean 71,21:
            - Owner: Germany
        
        ### 170
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 16484
        - Player: 2: Germany
        - Plots:
          - Ocean 75,22:
            - Owner: Germany
          - Ocean 74,21:
            - Owner: Germany
          - Ocean 74,20:
            - Owner: Germany
        
        ### 171
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 16553
        - Player: 2: Germany
        - Plots:
          - Coast 1,31:
            - Owner: Germany
          - Ocean 1,30:
            - Owner: Germany
          - Coast 77,27:
            - Owner: Germany
        
        ### 172
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 16402
        - Player: 2: Germany
        - Plots:
          - Ocean 74,21:
            - Owner: Germany
          - Ocean 73,21:
            - Owner: Germany
          - Ocean 72,21:
            - Owner: Germany
          - Ocean 72,20:
            - Owner: Germany
        
        ### 173
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 16552
        - Player: 2: Germany
        - Plots:
          - Coast 74,23:
            - Owner: Germany
          - Coast 74,22:
            - Owner: Germany
            - Improvement: Kampong
          - Ocean 73,21:
            - Owner: Germany
          - Ocean 73,20:
            - Owner: Germany
        
        ### 174
        - Type: CombatResult
        - Tundra Land 32,48:
          - Owner: City-State Shedet
          - CityID: 1072
          - Population: 20
          - IsRiver: true
          - City: Shedet
          - Religion: Protestantism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 37
          - Damage: 189
          - Player: 29
        
        ### 175
        - Type: TileRouteChanged
        - OldRoute: 1
        - NewRoute: 1
        - IsPillaged: true
        - Owner: 29
        - Tundra Land 31,48:
          - Owner: City-State Shedet
          - IsRiver: true
          - Resource: Deer
          - Improvement: Camp
          - Route: Railroad
          - Feature: Forest
        
        ### 176
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 15725
        - Player: 2: Germany
        - Tundra Hills 32,46:
          - Owner: City-State Shedet
          - Route: Railroad
        
        ### 177
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Light Tank
          - ID: 14955
        - Player: 2: Germany
        - Plots:
          - Tundra Land 32,44:
            - Owner: Germany
            - Improvement: Fort
            - Route: Railroad
          - Tundra Land 32,45:
            - Route: Railroad
          - Tundra Hills 32,46:
            - Owner: City-State Shedet
            - Route: Railroad
          - Plains Land 31,47:
            - Owner: City-State Shedet
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Farm
            - Route: Railroad
        
        ### 178
        - Type: CombatResult
        - Tundra Land 32,48:
          - Owner: City-State Shedet
          - CityID: 1072
          - Population: 20
          - IsRiver: true
          - City: Shedet
          - Religion: Protestantism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 34
          - Damage: 223
          - Player: 29
        
        ### 179
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: CityBombard
          - Unit: Krupp Gun
          - ID: 13750
        - Player: 2: Germany
        - Tundra Land 29,47:
          - Owner: Germany
        
        ### 180
        - Type: CombatResult
        - Tundra Land 32,48:
          - Owner: City-State Shedet
          - CityID: 1072
          - Population: 20
          - IsRiver: true
          - City: Shedet
          - Religion: Protestantism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 33
          - Damage: 256
          - Player: 29
        
        ### 181
        - Type: CombatResult
        - Tundra Land 32,48:
          - Owner: City-State Shedet
          - CityID: 1072
          - Population: 20
          - IsRiver: true
          - City: Shedet
          - Religion: Protestantism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 13
          - Damage: 269
          - Player: 29
        
        ### 182
        - Type: CombatResult
        - Tundra Land 32,48:
          - Owner: City-State Shedet
          - CityID: 1072
          - Population: 20
          - IsRiver: true
          - City: Shedet
          - Religion: Protestantism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 19
          - Damage: 288
          - Player: 29
        
        ### 183
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Light Tank
          - ID: 14955
        - Player: 2: Germany
        - Tundra Hills 32,46:
          - Owner: City-State Shedet
          - Route: Railroad
        
        ### 184
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 15725
        - Player: 2: Germany
        - Plains Land 31,47:
          - Owner: City-State Shedet
          - IsRiver: true
          - Resource: Wheat
          - Improvement: Farm
          - Route: Railroad
        
        ### 185
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: CityBombard
          - Unit: Krupp Gun
          - ID: 13444
        - Player: 2: Germany
        - Plots:
          - Plains Hills 25,45:
            - Owner: Germany
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 25,44:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Manufactory
            - Route: Railroad
          - Desert Hills 24,43:
            - Owner: Germany
            - CityID: 13509
            - Population: 26
            - IsRiver: true
            - City: Tenochtitlan
            - Religion: Protestantism
            - Route: Railroad
          - Plains Land 23,43:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 22,43:
            - Owner: Germany
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 22,42:
            - Owner: Germany
            - Improvement: Town
            - Route: Railroad
          - Plains Hills 21,41:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 20,41:
            - Owner: Germany
            - CityID: 12865
            - Population: 26
            - City: Teotihuacan
            - Religion: Protestantism
            - Route: Railroad
          - Plains Hills 20,40:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Desert Hills 20,39:
            - Owner: Germany
            - Route: Railroad
            - Feature: The Grand Mesa
          - Desert Land 21,38:
            - Owner: Germany
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
          - Coast 20,37:
            - Owner: Germany
        
        ### 186
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 16609
        - Player: 2: Germany
        - Plots:
          - Coast 26,32:
            - Owner: Germany
            - Improvement: Polder
          - Desert Hills 25,32:
            - Owner: Germany
            - CityID: 16749
            - Population: 3
            - City: Ardea
            - Resource: Stone
            - Religion: Protestantism
            - Route: Railroad
          - Coast 24,32:
            - Owner: Germany
          - Coast 23,33:
            - Owner: Germany
          - Coast 22,33:
            - Owner: Germany
          - Ocean 21,33:
            - Owner: Germany
        
        ### 187
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 16648
        - Player: 2: Germany
        - Plots:
          - Coast 7,38:
            - Owner: Germany
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 7,37:
            - Owner: Germany
          - Coast 8,36:
            - Owner: Germany
          - Coast 8,35:
            - Owner: Germany
          - Coast 9,34:
            - Owner: Germany
          - Coast 9,33:
            - Owner: Germany
        
        ### 188
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 15252
        - Player: 2: Germany
        - Plots:
          - Coast 1,31:
            - Owner: Germany
          - Coast 2,31:
            - Owner: Germany
          - Coast 3,30:
            - Owner: City-State Cahokia
          - Coast 3,29:
            - Owner: City-State Cahokia
            - Resource: Coral
            - Improvement: Fishing Boats
          - Coast 4,28:
            - Owner: City-State Cahokia
        
        ### 189
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 14599
        - Player: 2: Germany
        - Plots:
          - Coast 0,31:
            - Owner: Germany
            - Feature: Atoll
          - Coast 1,31:
            - Owner: Germany
          - Coast 2,31:
            - Owner: Germany
          - Coast 3,30:
            - Owner: City-State Cahokia
          - Coast 3,29:
            - Owner: City-State Cahokia
            - Resource: Coral
            - Improvement: Fishing Boats
        
        ### 190
        - Type: CombatResult
        - Plains Land 66,19:
          - Owner: Germany
          - Resource: Cloves
          - Improvement: Academy
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 1
          - Damage: 1
          - Unit:
            - Level: 5
            - AI: Paradrop
            - Unit: Paratrooper
            - ID: 14954
          - Player: 1: Rome
        
        ### 191
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 15710
        - Player: 2: Germany
        - Plots:
          - Desert Hills 25,33:
            - Owner: Germany
            - Improvement: Mine
          - Desert Hills 25,32:
            - Owner: Germany
            - CityID: 16749
            - Population: 3
            - City: Ardea
            - Resource: Stone
            - Religion: Protestantism
            - Route: Railroad
        
        ### 192
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 69%
          - AI: Defense
          - Unit: Infantry
          - ID: 15717
        - Player: 2: Germany
        - Plains Land 32,40:
          - Owner: Germany
          - CityID: 16835
          - Population: 11
          - City: Tlaxcala
          - Religion: Protestantism
          - Route: Railroad
        
        ### 193
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 80%
          - AI: FastAttack
          - Unit: Tank
          - ID: 16079
        - Player: 2: Germany
        - Plots:
          - Desert Hills 30,33:
            - Owner: The Netherlands
            - Resource: Sheep
            - Improvement: Pasture
          - Desert Hills 30,32:
            - Owner: The Netherlands
            - Resource: Aluminum
            - Improvement: Mine
        
        ### 194
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 6: The Netherlands
        - OldImprovement: Mine
        - NewImprovement: Mine
        - Desert Hills 30,32:
          - Owner: The Netherlands
          - Resource: Aluminum
          - Improvement: Mine
        
        ### 195
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 70%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 14703
        - Player: 2: Germany
        - Plots:
          - Coast 30,30:
            - Owner: The Netherlands
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 196
        - Type: CombatResult
        - Coast 30,31:
          - Owner: The Netherlands
          - Improvement: Polder
        - Attacker:
          - RemainingHP: 26
          - Damage: 67
        - Defender:
          - RemainingHP: 35
          - Damage: 76
          - Player: 6: The Netherlands
          - Unit:
            - Level: 8
            - Health: 67%
            - AI: Paradrop
            - Unit: Paratrooper
            - ID: 14482
        
        ### 197
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 75%
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 13932
        - Player: 2: Germany
        - Plots:
          - Coast 29,8:
            - Owner: Rome
        
        ### 198
        - Type: CombatResult
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 52
          - Damage: 100
          - Player: 6: The Netherlands
          - Unit:
            - Level: 6
            - Health: 52%
            - AI: AttackSea
            - Unit: Ironclad
            - ID: 10811
        
        ### 199
        - Type: UnitKilledInCombat
        - KilledPlayer: 6: The Netherlands
        - KillerPlayer: 2: Germany
        - KilledUnit: Ironclad
        
        ### 200
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 49%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 14784
        - Player: 2: Germany
        
        ### 201
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 75%
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 13932
        - Player: 2: Germany
        
        ### 202
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 49%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 14784
        - Player: 2: Germany
        
        ### 203
        - Type: CombatResult
        - Attacker:
          - RemainingHP: 9
          - Damage: 60
        - Defender:
          - RemainingHP: 50
          - Damage: 115
          - Player: 6: The Netherlands
          - Unit:
            - Level: 2
            - Health: 35%
            - AI: AttackSea
            - Unit: Ironclad
            - ID: 15615
        
        ### 204
        - Type: UnitKilledInCombat
        - KilledPlayer: 6: The Netherlands
        - KillerPlayer: 2: Germany
        - KilledUnit: Ironclad
        
        ### 205
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 55%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 14784
        - Player: 2: Germany
        
        ### 206
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 14965
        - Player: 2: Germany
        - Plots:
          - Ocean 67,16:
            - Owner: Rome
          - Ocean 66,17:
            - Owner: Rome
          - Coast 66,18:
            - Owner: Germany
            - Improvement: Kampong
        
        ### 207
        - Type: CombatResult
        - Desert Hills 65,19:
          - Owner: Rome
          - Resource: Sheep
          - Improvement: Pasture
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 35
          - Damage: 65
          - Player: 1: Rome
          - Unit:
            - Level: 4
            - Health: 73%
            - AI: Attack
            - Unit: Foreign Legion
            - ID: 16891
        
        ### 208
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14707
        - Player: 2: Germany
        - Plots:
          - Plains Land 67,23:
            - Owner: Germany
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 67,24:
            - Owner: Germany
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
        
        ### 209
        - Type: CombatResult
        - Plains Hills 65,21:
          - Owner: Germany
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 27
          - Damage: 27
          - Player: 1: Rome
          - Unit:
            - Level: 4
            - AI: Defense
            - Unit: Rifleman
            - ID: 16471
        
        ### 210
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: CityBombard
          - Unit: Krupp Gun
          - ID: 16142
        - Player: 2: Germany
        - Grass Land 68,22:
          - Owner: Germany
          - Resource: Cotton
          - Improvement: Academy
        
        ### 211
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 33%
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 15575
        - Player: 2: Germany
        - Grass Land 67,22:
          - Owner: Germany
          - Resource: Iron
          - Improvement: Mine
          - Route: Railroad
        
        ### 212
        - Type: CombatResult
        - Plains Land 66,19:
          - Owner: Germany
          - Resource: Cloves
          - Improvement: Academy
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 31
          - Damage: 37
          - Player: 1: Rome
          - Unit:
            - Level: 5
            - Health: 94%
            - AI: Paradrop
            - Unit: Paratrooper
            - ID: 14954
        
        ### 213
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16328
        - Player: 2: Germany
        - Grass Land 67,22:
          - Owner: Germany
          - Resource: Iron
          - Improvement: Mine
          - Route: Railroad
        
        ### 214
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 33%
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 15575
        - Player: 2: Germany
        - Plains Land 67,23:
          - Owner: Germany
          - Resource: Uranium
          - Improvement: Quarry
          - Route: Railroad
        
        ### 215
        - Type: CombatResult
        - Plains Hills 65,21:
          - Owner: Germany
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 37
          - Damage: 64
          - Player: 1: Rome
          - Unit:
            - Level: 4
            - Health: 77%
            - AI: Defense
            - Unit: Rifleman
            - ID: 16471
        
        ### 216
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 33%
          - AI: Defense
          - Unit: Infantry
          - ID: 15726
        - Player: 2: Germany
        - Plots:
          - Plains Land 67,21:
            - Owner: Germany
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
          - Grass Land 67,22:
            - Owner: Germany
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 67,23:
            - Owner: Germany
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
        
        ### 217
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 33%
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 15575
        - Player: 2: Germany
        - Plots:
          - Grass Land 67,22:
            - Owner: Germany
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 67,21:
            - Owner: Germany
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
          - Desert Land 68,21:
            - Owner: Germany
            - Resource: Oil
            - Improvement: Oil Well
        
        ### 218
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 78%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 14785
        - Player: 2: Germany
        - Plots:
          - Ocean 70,17:
            - Owner: Germany
          - Ocean 70,16:
            - Owner: Germany
          - Ocean 69,15:
            - Owner: Germany
          - Ocean 68,14:
            - Owner: Rome
          - Ocean 67,13:
            - Owner: Rome
        
        ### 219
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 33%
          - AI: Defense
          - Unit: Infantry
          - ID: 15726
        - Player: 2: Germany
        - Grass Land 68,24:
          - Owner: Germany
        
        ### 220
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 49%
          - AI: Defense
          - Unit: Infantry
          - ID: 16457
        - Player: 2: Germany
        - Plots:
          - Desert Hills 67,20:
            - Owner: Germany
            - CityID: 14797
            - Population: 22
            - City: Medan
            - Resource: Cloves
            - Religion: Hinduism
            - Route: Railroad
          - Plains Land 67,21:
            - Owner: Germany
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
          - Grass Land 67,22:
            - Owner: Germany
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 67,23:
            - Owner: Germany
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
        
        ### 221
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 14965
        - Player: 2: Germany
        - Coast 67,18:
          - Owner: Germany
          - Feature: Atoll
        
        ### 222
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 14610
        - Player: 2: Germany
        - Plots:
          - Coast 69,19:
            - Owner: Germany
          - Coast 69,18:
            - Owner: Germany
            - Feature: Atoll
          - Ocean 68,17:
            - Owner: Germany
          - Ocean 68,16:
            - Owner: Rome
          - Ocean 67,15:
            - Owner: Rome
          - Ocean 67,14:
            - Owner: Rome
        
        ### 223
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 74%
          - AI: Defense
          - Unit: Infantry
          - ID: 15722
        - Player: 2: Germany
        - Grass Hills 14,27:
          - Owner: City-State Ormus
          - Improvement: Mine
        
        ### 224
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 35
        - OldImprovement: Mine
        - NewImprovement: Mine
        - Grass Hills 14,27:
          - Owner: City-State Ormus
          - Improvement: Mine
        
        ### 225
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 56%
          - AI: Defense
          - Unit: Infantry
          - ID: 15727
        - Player: 2: Germany
        - Grass Land 14,26:
          - Owner: City-State Ormus
          - Resource: Amber
          - Improvement: Quarry
        
        ### 226
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 35
        - OldImprovement: Quarry
        - NewImprovement: Quarry
        - Grass Land 14,26:
          - Owner: City-State Ormus
          - Resource: Amber
          - Improvement: Quarry
        
        ### 227
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 15863
        - Player: 2: Germany
        - Plots:
          - Grass Land 13,26:
            - Owner: City-State Ormus
            - Improvement: Embassy
        
        ### 228
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 15869
        - Player: 2: Germany
        - Plains Land 15,28:
          - Owner: City-State Ormus
          - Improvement: Farm
          - Route: Road
        
        ### 229
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 15935
        - Player: 2: Germany
        - Plots:
          - Grass Land 16,30:
            - Owner: Germany
            - Resource: Tea
            - Improvement: Plantation
          - Grass Land 15,29:
            - Owner: City-State Ormus
            - Improvement: Fort
            - Route: Road
          - Plains Land 15,28:
            - Owner: City-State Ormus
            - Improvement: Farm
            - Route: Road
        
        ### 230
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Light Tank
          - ID: 14616
        - Player: 2: Germany
        - Plots:
          - Tundra Hills 29,45:
            - Owner: Germany
            - Resource: Gems
            - Improvement: Mine
          - Tundra Land 30,46:
            - Owner: Germany
            - Improvement: Fort
          - Tundra Land 30,47:
            - Owner: City-State Shedet
            - IsRiver: true
            - Improvement: Lumber Mill
            - Feature: Forest
        
        ### 231
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: CityBombard
          - Unit: Krupp Gun
          - ID: 13821
        - Player: 2: Germany
        - Snow Hills 29,46:
          - Owner: Germany
          - Improvement: Mine
        
        ### 232
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 55%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 14784
        - Player: 2: Germany
        
        ### 233
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 14701
        - Player: 2: Germany
        - Plots:
          - Coast 32,35:
            - Owner: The Netherlands
            - Feature: Atoll
          - Coast 32,34:
            - Owner: The Netherlands
            - Resource: Whales
            - Improvement: Fishing Boats
          - Coast 32,33:
            - Owner: The Netherlands
            - Feature: Atoll
        
        ### 234
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 96%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 14966
        - Player: 2: Germany
        - Plots:
          - Coast 31,39:
            - Owner: Germany
          - Coast 32,38:
            - Owner: Germany
          - Coast 32,35:
            - Owner: The Netherlands
            - Feature: Atoll
          - Coast 32,34:
            - Owner: The Netherlands
            - Resource: Whales
            - Improvement: Fishing Boats
        
        ### 235
        - Type: CombatResult
        - Desert Land 31,33:
          - Owner: The Netherlands
          - CityID: 13335
          - Population: 17
          - City: Seoul
          - Religion: Protestantism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 14
          - Damage: 14
        - Defender:
          - RemainingHP: 39
          - Damage: 39
          - Player: 6: The Netherlands
        
        ### 236
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 14965
        - Player: 2: Germany
        - Plots:
          - Ocean 68,18:
            - Owner: Germany
          - Ocean 68,17:
            - Owner: Germany
        
        ### 237
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 94%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 15343
        - Player: 2: Germany
        - Plots:
          - Ocean 70,21:
            - Owner: Germany
          - Coast 70,20:
            - Owner: Germany
            - Improvement: Kampong
          - Coast 69,19:
            - Owner: Germany
          - Coast 69,18:
            - Owner: Germany
            - Feature: Atoll
          - Ocean 68,17:
            - Owner: Germany
          - Ocean 68,16:
            - Owner: Rome
        
        ### 238
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 15350
        - Player: 2: Germany
        - Tundra Land 30,50:
          - Owner: City-State Shedet
          - Resource: Aluminum
          - Improvement: Mine
        
        ### 239
        - Type: ParadropAt
        - Unit:
          - Level: 4
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 15350
        - Player: 2: Germany
        - To:
          - Owner: City-State Shedet
          - Terrain: Tundra
          - Resource: Aluminum
          - Improvement: Mine
          - Plot: Land
          - X: 30
          - Y: 50
        - From:
          - Owner: Germany
          - Terrain: Plains
          - Plot: Land
          - X: 29
          - Y: 41
        
        ### 240
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 29
        - OldImprovement: Mine
        - NewImprovement: Mine
        - Tundra Land 30,50:
          - Owner: City-State Shedet
          - Resource: Aluminum
          - Improvement: Mine
        
        ### 241
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 10104
        - Player: 2: Germany
        - Desert Hills 67,20:
          - Owner: Germany
          - CityID: 14797
          - Population: 22
          - City: Medan
          - Resource: Cloves
          - Religion: Hinduism
          - Route: Railroad
        
        ### 242
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: FastAttack
          - Unit: Tank
          - ID: 15793
        - Player: 2: Germany
        
        ### 243
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 15350
        - Player: 2: Germany
        - Tundra Land 29,50:
          - Resource: Deer
          - Feature: Forest
        
        ### 244
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: CityBombard
          - Unit: Krupp Gun
          - ID: 13821
        - Player: 2: Germany
        - Tundra Land 28,45:
          - Owner: Germany
          - Resource: Deer
          - Improvement: Camp
          - Route: Road
          - Feature: Forest
        
        ### 245
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 49%
          - AI: ExploreSea
          - Unit: Attack Submarine
          - ID: 14122
        - Player: 2: Germany
        
        ### 246
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 60%
          - AI: Worker
          - Unit: Worker
          - ID: 16654
        - Player: 2: Germany
        - Plots:
          - Tundra Land 30,46:
            - Owner: Germany
            - Improvement: Fort
          - Tundra Hills 29,45:
            - Owner: Germany
            - Resource: Gems
            - Improvement: Mine
        
        ### 247
        - Type: RebaseTo
        - Player: 2: Germany
        - Unit:
          - Level: 4
          - Health: 77%
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 16405
        - Grass Land 9,39:
          - Owner: Germany
          - CityID: 1193
          - Population: 31
          - City: Hamburg
          - Resource: Tea
          - Religion: Protestantism
          - Route: Railroad
        
        ### 248
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 77%
          - AI: AttackAir
          - Unit: Heavy Bomber
          - ID: 16405
        - Player: 2: Germany
        - Grass Land 9,39:
          - Owner: Germany
          - CityID: 1193
          - Population: 31
          - City: Hamburg
          - Resource: Tea
          - Religion: Protestantism
          - Route: Railroad
        
        ### 249
        - Type: TileRouteChanged
        - OldRoute: 1
        - Owner: 2: Germany
        - Desert Land 25,34:
          - Owner: Germany
          - Improvement: Fort
        
        ### 250
        - Type: BuildFinished
        - Player: 2: Germany
        - Desert Land 25,34:
          - Owner: Germany
          - Improvement: Fort
        
        ### 251
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 2: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3978
        - Build: Remove a Road
        - Desert Land 25,34:
          - Owner: Germany
          - Improvement: Fort
        
        ### 252
        - Type: UnitBuildStart
        - Owner: 2: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3978
        - Build: Remove a Road
        - Desert Land 25,34:
          - Owner: Germany
          - Improvement: Fort
        
        ### 253
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 6259
        - Player: 2: Germany
        - Desert Hills 26,34:
          - Owner: Germany
          - Improvement: Mine
          - Route: Railroad
        
        ### 254
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 14128
        - Player: 2: Germany
        - Plains Land 32,42:
          - Owner: Germany
          - Improvement: Lumber Mill
          - Route: Railroad
          - Feature: Forest
        
        ### 255
        - Type: TileImprovementChanged
        - Owner: 2: Germany
        - NewImprovement: Fort
        - Tundra Land 8,50:
          - Owner: Germany
          - Improvement: Fort
        
        ### 256
        - Type: BuildFinished
        - Player: 2: Germany
        - Improvement: Fort
        - Tundra Land 8,50:
          - Owner: Germany
          - Improvement: Fort
        
        ### 257
        - Type: UnitBuildCompleted
        - Owner: 2: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 15072
        - Build: Construct a Fort
        - Tundra Land 8,50:
          - Owner: Germany
          - Improvement: Fort
        
        ### 258
        - Type: UnitBuildStart
        - Owner: 2: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 15072
        - Build: Construct a Fort
        - Tundra Land 8,50:
          - Owner: Germany
          - Improvement: Fort
        
        ### 259
        - Type: TileImprovementChanged
        - Owner: 2: Germany
        - NewImprovement: Fort
        - Tundra Land 10,50:
          - Owner: Germany
          - Improvement: Fort
        
        ### 260
        - Type: BuildFinished
        - Player: 2: Germany
        - Improvement: Fort
        - Tundra Land 10,50:
          - Owner: Germany
          - Improvement: Fort
        
        ### 261
        - Type: UnitBuildCompleted
        - Owner: 2: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 11909
        - Build: Construct a Fort
        - Tundra Land 10,50:
          - Owner: Germany
          - Improvement: Fort
        
        ### 262
        - Type: UnitBuildStart
        - Owner: 2: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 11909
        - Build: Construct a Fort
        - Tundra Land 10,50:
          - Owner: Germany
          - Improvement: Fort
        
        ### 263
        - Type: UnitBuildCompleted
        - Owner: 2: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3318
        - Build: Construct a Farm
        - Plains Land 10,44:
          - Owner: Germany
        
        ### 264
        - Type: TileImprovementChanged
        - Owner: 2: Germany
        - NewImprovement: Fort
        - Desert Land 1,32:
          - Owner: Germany
          - Improvement: Fort
        
        ### 265
        - Type: BuildFinished
        - Player: 2: Germany
        - Improvement: Fort
        - Desert Land 1,32:
          - Owner: Germany
          - Improvement: Fort
        
        ### 266
        - Type: UnitBuildCompleted
        - Owner: 2: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 13599
        - Build: Construct a Fort
        - Desert Land 1,32:
          - Owner: Germany
          - Improvement: Fort
        
        ### 267
        - Type: UnitBuildStart
        - Owner: 2: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 13599
        - Build: Construct a Fort
        - Desert Land 1,32:
          - Owner: Germany
          - Improvement: Fort
        
        ### 268
        - Type: TileImprovementChanged
        - Owner: 2: Germany
        - NewImprovement: Fort
        - Desert Land 7,36:
          - Owner: Germany
          - Improvement: Fort
        
        ### 269
        - Type: BuildFinished
        - Player: 2: Germany
        - Improvement: Fort
        - Desert Land 7,36:
          - Owner: Germany
          - Improvement: Fort
        
        ### 270
        - Type: UnitBuildCompleted
        - Owner: 2: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4847
        - Build: Construct a Fort
        - Desert Land 7,36:
          - Owner: Germany
          - Improvement: Fort
        
        ### 271
        - Type: UnitBuildStart
        - Owner: 2: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4847
        - Build: Construct a Fort
        - Desert Land 7,36:
          - Owner: Germany
          - Improvement: Fort
        
        ### 272
        - Type: UnitBuildCompleted
        - Owner: 2: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 14243
        - Build: Construct a Farm
        - Plains Land 11,43:
          - Owner: Germany
          - Route: Railroad
        
        ### 273
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3060
        - Player: 2: Germany
        - Plots:
          - Plains Land 25,42:
            - Owner: Germany
            - Improvement: Farm
            - Route: Railroad
          - Desert Hills 24,43:
            - Owner: Germany
            - CityID: 13509
            - Population: 26
            - IsRiver: true
            - City: Tenochtitlan
            - Religion: Protestantism
            - Route: Railroad
          - Plains Land 23,43:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 22,43:
            - Owner: Germany
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 21,43:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Plains Land 21,44:
            - Owner: Germany
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
          - Tundra Hills 20,45:
            - Owner: Germany
            - Resource: Gems
            - Improvement: Mine
            - Route: Railroad
          - Tundra Land 20,46:
            - Owner: Germany
            - Route: Railroad
          - Tundra Hills 19,47:
            - Owner: Germany
            - Route: Railroad
          - Tundra Hills 18,47:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Mine
            - Route: Road
        
        ### 274
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 16479
        - Player: 2: Germany
        - Plains Land 29,41:
          - Owner: Germany
        
        ### 275
        - Type: UnitBuildCompleted
        - Owner: 2: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 16479
        - Build: Construct a Village
        - Plains Land 29,41:
          - Owner: Germany
        
        ### 276
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4843
        - Player: 2: Germany
        - Plots:
          - Desert Land 18,37:
            - Owner: Germany
            - CityID: 3783
            - Population: 25
            - City: Dortmund
            - Religion: Protestantism
            - Route: Railroad
          - Plains Land 19,38:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Desert Land 20,38:
            - Owner: Germany
            - Route: Railroad
          - Desert Land 21,38:
            - Owner: Germany
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
          - Desert Hills 21,37:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Desert Land 22,37:
            - Owner: Germany
            - Route: Railroad
          - Plains Land 23,37:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Plains Land 24,36:
            - Owner: Germany
            - CityID: 14242
            - Population: 19
            - City: Zurich
            - Resource: Glass
            - Religion: Protestantism
            - Route: Railroad
          - Desert Land 23,35:
            - Owner: Germany
            - Resource: Oil
            - Improvement: Embassy
            - Route: Railroad
          - Desert Land 23,34:
            - Owner: Germany
        
        ### 277
        - Type: UnitBuildCompleted
        - Owner: 2: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 14798
        - Build: Construct a Village
        - Tundra Hills 19,47:
          - Owner: Germany
          - Route: Railroad
        
        ### 278
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 2: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4008
        - Build: Construct a Mine
        - Snow Hills 20,50:
          - Owner: Germany
        
        ### 279
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3402
        - Player: 2: Germany
        - Plots:
          - Plains Land 18,48:
            - Owner: Germany
            - CityID: 14799
            - Population: 14
            - IsRiver: true
            - City: Valletta
            - Religion: Protestantism
            - Route: Railroad
          - Plains Land 17,47:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 17,46:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Plains Land 17,45:
            - Owner: Germany
            - Resource: Horses
            - Improvement: Embassy
            - Route: Road
          - Tundra Land 18,45:
            - Owner: Germany
        
        ### 280
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 2: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3402
        - Build: Construct a Fort
        - Tundra Land 18,45:
          - Owner: Germany
        
        ### 281
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 5332
        - Player: 2: Germany
        - Plots:
          - Plains Land 16,43:
            - Owner: Germany
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 16,44:
            - Owner: Germany
            - Resource: Wheat
            - Improvement: Academy
            - Route: Railroad
          - Plains Hills 16,45:
            - Owner: Germany
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 17,46:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Plains Land 17,47:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 18,48:
            - Owner: Germany
            - CityID: 14799
            - Population: 14
            - IsRiver: true
            - City: Valletta
            - Religion: Protestantism
            - Route: Railroad
          - Plains Land 19,48:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Tundra Hills 19,47:
            - Owner: Germany
            - Route: Railroad
          - Tundra Land 20,46:
            - Owner: Germany
            - Route: Railroad
        
        ### 282
        - Type: UnitBuildCompleted
        - Owner: 2: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 5332
        - Build: Construct a Fort
        - Tundra Land 20,46:
          - Owner: Germany
          - Route: Railroad
        
        ### 283
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 5192
        - Player: 2: Germany
        - Plots:
          - Coast 7,38:
            - Owner: Germany
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 8,38:
            - Owner: Germany
            - Resource: Crab
            - Improvement: Fishing Boats
          - Coast 8,39:
            - Owner: Germany
            - Resource: Fish
            - Improvement: Fishing Boats
          - Grass Land 9,39:
            - Owner: Germany
            - CityID: 1193
            - Population: 31
            - City: Hamburg
            - Resource: Tea
            - Religion: Protestantism
            - Route: Railroad
          - Grass Land 10,39:
            - Owner: Germany
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
          - Grass Land 11,39:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Grass Land 12,39:
            - Owner: Germany
            - IsRiver: true
            - Resource: Tea
            - Improvement: Plantation
            - Route: Railroad
          - Plains Land 13,39:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 14,39:
            - Owner: Germany
            - CityID: 1059
            - Population: 47
            - IsRiver: true
            - City: Berlin
            - Religion: Protestantism
            - Route: Railroad
          - Desert Hills 15,39:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Plains Land 16,39:
            - Owner: Germany
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Desert Hills 17,39:
            - Owner: Germany
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 18,40:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Desert Hills 19,40:
            - Owner: Germany
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 20,40:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 20,41:
            - Owner: Germany
            - CityID: 12865
            - Population: 26
            - City: Teotihuacan
            - Religion: Protestantism
            - Route: Railroad
        
        ### 284
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 2291
        - Player: 2: Germany
        - Tundra Land 19,49:
          - Owner: Germany
          - IsRiver: true
          - Improvement: Lumber Mill
          - Feature: Forest
        
        ### 285
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 10050
        - Player: 2: Germany
        - Plots:
          - Plains Land 21,39:
            - Owner: Germany
            - Improvement: Farm
            - Route: Road
          - Desert Hills 22,40:
            - Owner: Germany
            - Resource: Gems
            - Improvement: Manufactory
            - Route: Railroad
          - Plains Hills 21,41:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
        
        ### 286
        - Type: TileImprovementChanged
        - Owner: 2: Germany
        - OldImprovement: Village
        - Plains Hills 21,41:
          - Owner: Germany
          - Route: Railroad
        
        ### 287
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 2: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 10050
        - Build: Construct a Mine
        - Plains Hills 21,41:
          - Owner: Germany
          - Route: Railroad
        
        ### 288
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1454
        - Player: 2: Germany
        - Plots:
          - Ocean 76,35:
            - Owner: Germany
          - Ocean 77,35:
            - Owner: Germany
          - Coast 78,35:
            - Owner: Germany
            - Feature: Atoll
          - Coast 0,35:
            - Owner: Germany
          - Grass Land 1,35:
            - Owner: Germany
            - CityID: 3319
            - Population: 26
            - City: Frankfurt
            - Religion: Protestantism
            - Route: Railroad
          - Coast 2,35:
            - Owner: Germany
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 3,36:
            - Owner: Germany
        
        ### 289
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 16652
        - Player: 2: Germany
        - Plots:
          - Plains Land 30,41:
            - Owner: Germany
            - Resource: Wheat
            - Improvement: Farm
          - Plains Land 30,42:
            - Owner: Germany
            - Improvement: Fort
        
        ### 290
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3373
        - Player: 2: Germany
        - Plots:
          - Coast 24,33:
            - Owner: Germany
            - Improvement: Polder
          - Coast 23,33:
            - Owner: Germany
        
        ### 291
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 14029
        - Player: 2: Germany
        - Plots:
          - Coast 74,35:
            - Owner: Germany
            - Feature: Atoll
          - Ocean 75,35:
            - Owner: Germany
          - Ocean 76,35:
            - Owner: Germany
        
        ### 292
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Fleet Destroyer
          - ID: 16923
        - Player: 2: Germany
        - Coast 77,25:
          - Owner: Germany
        
        ### 293
        - Type: UnitCreated
        - UnitType: Fleet Destroyer
        - Player: 2: Germany
        - Unit:
          - Level: 1
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16923
        - Coast 77,25:
          - Owner: Germany
        
        ### 294
        - Type: UnitUpgraded
        - Player: 2: Germany
        - OldUnit:
          - Level: 5
          - Health: 84%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 14612
        - NewUnit:
          - Level: 1
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16923
        
        ### 295
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 2: Germany
        - OriginalUnit:
          - Level: 5
          - Health: 84%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 14612
        - NewOwner: 2: Germany
        - ConvertingUnit:
          - Level: 5
          - Health: 84%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16923
        
        ### 296
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Fighter
          - ID: 16924
        - Player: 2: Germany
        - Plains Land 70,33:
          - Owner: Germany
          - CityID: 5196
          - Population: 30
          - City: Regensburg
          - Religion: Protestantism
          - Route: Railroad
        
        ### 297
        - Type: UnitCreated
        - UnitType: Fighter
        - Player: 2: Germany
        - Unit:
          - Level: 1
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 16924
        - Plains Land 70,33:
          - Owner: Germany
          - CityID: 5196
          - Population: 30
          - City: Regensburg
          - Religion: Protestantism
          - Route: Railroad
        
        ### 298
        - Type: UnitUpgraded
        - Player: 2: Germany
        - OldUnit:
          - Level: 5
          - AI: DefenseAir
          - Unit: Triplane
          - ID: 16325
        - NewUnit:
          - Level: 1
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 16924
        
        ### 299
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 2: Germany
        - OriginalUnit:
          - Level: 5
          - AI: DefenseAir
          - Unit: Triplane
          - ID: 16325
        - NewOwner: 2: Germany
        - ConvertingUnit:
          - Level: 5
          - AI: DefenseAir
          - Unit: Fighter
          - ID: 16924
        
        ### 300
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14973
        - Player: 2: Germany
        - Plots:
          - Grass Land 16,30:
            - Owner: Germany
            - Resource: Tea
            - Improvement: Plantation
          - Grass Land 15,29:
            - Owner: City-State Ormus
            - Improvement: Fort
            - Route: Road
        
        ### 301
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 85%
          - AI: Defense
          - Unit: Infantry
          - ID: 15720
        - Player: 2: Germany
        - Plots:
          - Plains Land 30,41:
            - Owner: Germany
            - Resource: Wheat
            - Improvement: Farm
          - Plains Land 29,41:
            - Owner: Germany
        
        ### 302
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 15724
        - Player: 2: Germany
        - Plots:
          - Plains Hills 25,45:
            - Owner: Germany
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 26,44:
            - Owner: Germany
            - IsRiver: true
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 26,43:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 26,42:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 25,41:
            - Owner: Germany
            - Improvement: Fort
            - Route: Railroad
          - Plains Hills 25,40:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Grass Land 25,39:
            - Owner: Germany
            - Improvement: Fort
            - Route: Railroad
        
        ### 303
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 15794
        - Player: 2: Germany
        - Plots:
          - Grass Land 9,29:
            - Owner: Germany
            - Improvement: Farm
          - Grass Land 8,29:
            - Owner: Germany
            - Feature: Jungle
        
        ### 304
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 15733
        - Player: 2: Germany
        - Plots:
          - Desert Hills 12,35:
            - Owner: Germany
            - Resource: Aluminum
            - Improvement: Town
            - Route: Railroad
          - Desert Land 13,36:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Desert Land 13,37:
            - Owner: Germany
            - Route: Railroad
          - Plains Land 14,38:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 15,38:
            - Owner: Germany
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Manufactory
            - Route: Railroad
          - Desert Land 15,37:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 16,37:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 17,37:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Landmark
            - Route: Railroad
          - Desert Land 18,37:
            - Owner: Germany
            - CityID: 3783
            - Population: 25
            - City: Dortmund
            - Religion: Protestantism
            - Route: Railroad
          - Plains Land 19,38:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Desert Land 20,38:
            - Owner: Germany
            - Route: Railroad
          - Desert Land 21,38:
            - Owner: Germany
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
        
        ### 305
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 14795
        - Player: 2: Germany
        - Snow Hills 21,50:
          - Owner: Germany
          - IsRiver: true
        
        ### 306
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 16080
        - Player: 2: Germany
        - Plots:
          - Coast 10,33:
            - Owner: Germany
            - Resource: Fish
            - Improvement: Fishing Boats
          - Desert Hills 11,32:
            - Owner: Germany
            - CityID: 3320
            - Population: 25
            - City: Aachen
            - Religion: Protestantism
            - Route: Railroad
          - Plains Land 11,33:
            - Owner: Germany
            - Resource: Olives
            - Improvement: Plantation
            - Route: Railroad
          - Plains Land 12,33:
            - Owner: Germany
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
          - Desert Land 13,33:
            - Owner: Germany
            - Route: Railroad
          - Desert Land 14,32:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Desert Land 14,31:
            - Owner: Germany
            - Resource: Iron
            - Improvement: Mine
            - Route: Road
          - Grass Land 14,30:
            - Owner: Germany
            - Resource: Rice
            - Improvement: Farm
        
        ### 307
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 87%
          - AI: Defense
          - Unit: Infantry
          - ID: 15723
        - Player: 2: Germany
        - Plots:
          - Plains Land 32,40:
            - Owner: Germany
            - CityID: 16835
            - Population: 11
            - City: Tlaxcala
            - Religion: Protestantism
            - Route: Railroad
          - Desert Land 31,40:
            - Owner: Germany
            - Improvement: Landmark
        
        ### 308
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 14956
        - Player: 2: Germany
        - Plains Land 4,41:
          - Owner: Germany
          - Resource: Uranium
          - Improvement: Quarry
        
        ### 309
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Defense
          - Unit: Infantry
          - ID: 16269
        - Player: 2: Germany
        
        ### 310
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 16822
        - Player: 2: Germany
        - Plots:
          - Plains Land 15,38:
            - Owner: Germany
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Manufactory
            - Route: Railroad
          - Plains Land 14,38:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Desert Land 13,37:
            - Owner: Germany
            - Route: Railroad
          - Desert Land 13,36:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Desert Hills 12,35:
            - Owner: Germany
            - Resource: Aluminum
            - Improvement: Town
            - Route: Railroad
          - Desert Land 12,34:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Plains Land 11,33:
            - Owner: Germany
            - Resource: Olives
            - Improvement: Plantation
            - Route: Railroad
          - Desert Hills 11,32:
            - Owner: Germany
            - CityID: 3320
            - Population: 25
            - City: Aachen
            - Religion: Protestantism
            - Route: Railroad
          - Coast 10,33:
            - Owner: Germany
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 9,33:
            - Owner: Germany
        
        ### 311
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Defense
          - Unit: Infantry
          - ID: 15868
        - Player: 2: Germany
        - Plots:
          - Tundra Land 22,48:
            - Owner: Germany
        
        ### 312
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 15729
        - Player: 2: Germany
        - Plots:
          - Tundra Hills 25,46:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Mine
          - Plains Hills 25,45:
            - Owner: Germany
            - Improvement: Mine
            - Route: Railroad
        
        ### 313
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Defense
          - Unit: Infantry
          - ID: 15718
        - Player: 2: Germany
        - Snow Land 28,46:
          - Owner: Germany
          - Resource: Oil
          - Improvement: Oil Well
        
        ### 314
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 15705
        - Player: 2: Germany
        - Plots:
          - Coast 71,26:
            - Owner: Germany
            - Improvement: Kampong
          - Coast 70,27:
            - Owner: Germany
            - Resource: Fish
          - Coast 70,28:
            - Owner: Germany
          - Coast 69,29:
            - Owner: Germany
            - Resource: Fish
          - Grass Land 70,30:
            - Owner: Germany
            - Improvement: Fort
          - Coast 69,31:
            - Owner: Germany
          - Grass Land 70,32:
            - Owner: Germany
            - Resource: Stone
            - Improvement: Quarry
        
        ### 315
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14700
        - Player: 2: Germany
        - Plots:
          - Plains Land 24,37:
            - Owner: Germany
            - Resource: Coffee
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 25,38:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Grass Land 25,39:
            - Owner: Germany
            - Improvement: Fort
            - Route: Railroad
          - Plains Hills 25,40:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Plains Land 25,41:
            - Owner: Germany
            - Improvement: Fort
            - Route: Railroad
          - Desert Land 26,42:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 26,43:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 27,43:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
          - Tundra Hills 28,44:
            - Owner: Germany
            - Resource: Gems
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 29,44:
            - Owner: Germany
            - CityID: 14971
            - Population: 22
            - IsRiver: true
            - City: Tlatelolco
            - Religion: Protestantism
            - Route: Railroad
          - Coast 29,43:
            - Owner: Germany
          - Plains Land 30,44:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Fort
          - Plains Land 31,44:
            - Owner: Germany
            - Improvement: Farm
        
        ### 316
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14708
        - Player: 2: Germany
        - Plots:
          - Plains Land 31,42:
            - Owner: Germany
            - Resource: Horses
            - Improvement: Pasture
          - Plains Land 30,43:
            - Owner: Germany
            - Resource: Coal
            - Improvement: Academy
        
        ### 317
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15174
        - Player: 2: Germany
        - Plots:
          - Plains Land 26,43:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 27,43:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
          - Tundra Hills 28,44:
            - Owner: Germany
            - Resource: Gems
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 29,44:
            - Owner: Germany
            - CityID: 14971
            - Population: 22
            - IsRiver: true
            - City: Tlatelolco
            - Religion: Protestantism
            - Route: Railroad
          - Coast 29,43:
            - Owner: Germany
          - Plains Land 30,44:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Fort
          - Tundra Land 30,45:
            - Owner: Germany
          - Tundra Land 31,45:
            - Owner: City-State Shedet
            - Improvement: Lumber Mill
            - Feature: Forest
        
        ### 318
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15344
        - Player: 2: Germany
        - Plots:
          - Grass Land 25,38:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Grass Land 25,39:
            - Owner: Germany
            - Improvement: Fort
            - Route: Railroad
          - Plains Hills 25,40:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Plains Land 25,41:
            - Owner: Germany
            - Improvement: Fort
            - Route: Railroad
          - Desert Land 26,42:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 25,43:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Hills 25,44:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Manufactory
            - Route: Railroad
        
        ### 319
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16921
        - Player: 2: Germany
        - Plains Land 70,33:
          - Owner: Germany
          - CityID: 5196
          - Population: 30
          - City: Regensburg
          - Religion: Protestantism
          - Route: Railroad
        
        ### 320
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Cargo Ship
          - ID: 16925
        - Player: 2: Germany
        - Desert Land 18,37:
          - Owner: Germany
          - CityID: 3783
          - Population: 25
          - City: Dortmund
          - Religion: Protestantism
          - Route: Railroad
        
        ### 321
        - Type: UnitCreated
        - UnitType: Cargo Ship
        - Player: 2: Germany
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16925
        - Desert Land 18,37:
          - Owner: Germany
          - CityID: 3783
          - Population: 25
          - City: Dortmund
          - Religion: Protestantism
          - Route: Railroad
        
        ### 322
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16925
        - Player: 2: Germany
        - Plots:
          - Coast 18,36:
            - Owner: Germany
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 17,35:
            - Owner: Germany
          - Coast 17,34:
            - Owner: Germany
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 16,33:
            - Owner: Germany
        
        ### 323
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16920
        - Player: 2: Germany
        - Grass Land 9,39:
          - Owner: Germany
          - CityID: 1193
          - Population: 31
          - City: Hamburg
          - Resource: Tea
          - Religion: Protestantism
          - Route: Railroad
        
        ### 324
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16734
        - Player: 2: Germany
        - Grass Land 9,39:
          - Owner: Germany
          - CityID: 1193
          - Population: 31
          - City: Hamburg
          - Resource: Tea
          - Religion: Protestantism
          - Route: Railroad
        
        ### 325
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 75%
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 13932
        - Player: 2: Germany
        - Plots:
          - Coast 31,6:
            - Resource: Fish
        
        ### 326
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 15938
        - Player: 2: Germany
        - Plots:
          - Grass Hills 64,32:
            - Owner: City-State Kyiv
            - IsRiver: true
            - Resource: Stone
            - Improvement: Quarry
            - Route: Road
          - Coast 65,32:
            - Owner: City-State Kyiv
        
        ### 327
        - Type: PlayerDoneTurn
        - NextPlayer: 4: Songhai
        - Player: 2: Germany
        
        You, Bismarck (leader of Germany, Player 2), are making strategic decisions after turn 384.
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
    - You are Bismarck, leader of Germany (Player 2).
      
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
      - Name: Germany
      - Uniques:
        - Unique Unit: Landsknecht, Replacing Tercio (Requires technology: Gunpowder)
        - Unique Unit: Krupp Gun, Replacing Artillery (Requires technology: Replaceable Parts)
        - Unique Building: Hanse, Replacing Customs House (Requires technology: Guilds)
        - Unique Building: Brewhouse, Replacing Windmill (Requires technology: Economics)
        - Civilization Ability: Gain +1 Influence per turn with City-States for each gifted Unit (lost when killed). -15% Production and Gold costs for Military Units.
      - Leader: Bismarck
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
      - Satellites: Allow you to build the Apollo Program, a project necessary to win a Science Victory.
        Completing it would unlock: The Internet, Lasers
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      - Telecommunications: Allows you to build the Interpretive Center, boosting all Landmarks in empire.
        Completing it would unlock: Robotics, The Internet
      - Mobile Tactics: Allows you to build the Mechanized Infantry, a fast and versatile late game Unit that doesn't require any resources.
        Completing it would unlock: Stealth
      
      ## Policies
      - Total War (Level 2 Tenet of Ideology Autocracy): Total War: +25% Production when building Land Units. Warscore increases 25% more quickly, and it is 25% easier to bully City-States.
      - Third Alternative (Level 2 Tenet of Ideology Autocracy): Third Alternative: Quantity of Strategic Resources produced (including Paper) is increased by 100%. Reduces Unit Gold Maintenance costs by 25%.
      - Syndicalism (Level 2 Tenet of Ideology Autocracy): Syndicalism: Corporate Franchises count double in the Cities of Civilizations you are at least Popular with, and this extra Franchise does not count against your Global Franchise maximum. Can establish 5 additional Franchises in foreign Cities. +2 Production from all Corporation Offices.
      - Mare Nostrum (Level 2 Tenet of Ideology Autocracy): Mare Nostrum: +1 Oil and Coal for every City-State Alliance. +2 Production and Culture to Atolls, Fishing Boats, and Offshore Oil Platforms. Naval Ranged Units gain the Mare Nostrum Promotion.
      - Futurism (Level 1 Tenet of Ideology Autocracy): Futurism: Strengthens Tourism of Historic Events generated by the Palace. +2 Culture from Great Works. Earn 50 Tourism when you conquer a city for the first time, scaling with Era and city size.
      - Lebensraum (Level 1 Tenet of Ideology Autocracy): Lebensraum: Receive 10 Culture and Golden Age Points when your borders expand, scaling with Era. Citadels may also be built in foreign territory adjacent to your borders. Retain tiles after razing Cities.
      - Police State (Level 2 Tenet of Ideology Autocracy): Police State: +3 Local Happiness from every Courthouse, and +10 City Security from Police Stations. +100% Production towards Courthouses and Police Stations.
      - Iron Fist (Level 1 Tenet of Ideology Autocracy): Iron Fist: Vassals can no longer be liberated by other Civilizations or the World Congress, and capitulated vassals can no longer rebel. Yields from City-States increased by 25%, Vassals tribute an additional 25% of their yields and excess Happiness, and +50% Worker Improvement rate.
      - Honor (Continuing Authority Branch):
        - * All Military Units gain the Conscription Promotion (+10% Combat Strength).
        - * Supply-free military Units spawn near Cities that reach (or have already reached) a multiple of 10 Citizens for the first time.
        - * -25% War Weariness.
      - Liberty (Continuing Progress Branch):
        - * +2 Gold in every City.
        - * +25% Tile improvement rate.
        - * A Worker appears near the Capital.
      - Organization (Continuing Progress Branch):
        - * +2 Production in every City.
        - * +25% Production toward Workers and Trade Units.
        - * +1 Movement for Workers.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Free Trade (Continuing Industry Branch):
        - * Earn Great Merchants 50% faster.
        - * +5 Gold from International Trade Routes.
        - * -2 Unhappiness from Poverty in all Cities.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Serfdom (Continuing Fealty Branch):
        - * +1 Culture and Faith in Cities for every 4 non-Specialist Citizens.
        - * +2 Production and +1 Gold from Pastures.
      - Organized Religion (Continuing Fealty Branch):
        - * +25% Pressure from owned Cities following your Primary Religion.
        - * +1 Delegate in the World Congress for every 10 Cities following your Primary Religion.
        - * +2 Culture from Shrines and Temples.
      - Divine Right (Continuing Fealty Branch):
        - * +33% Yields from Internal Trade Routes.
        - * Completing an Internal Trade Route triggers a Historic Event as if completing an International Trade Route.
        - * -1 Unhappiness from Boredom in all Cities.
      - Tribute (Continuing Authority Branch):
        - * A Settler appears near the Capital.
        - * Gain Culture in Capital equal to 25% of the Gold Tribute demanded from City-States (50% if all Authority policies are adopted).
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
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
      - Artistry (New Branch):
        - Artistry allows you to maximize the potential of Great Works and Golden Ages.
        - Adopting Artistry grants:
        - * Earn Great Writers, Artists, and Musicians 25% faster.
        - * +10% Culture during Golden Ages.
        - * +100% Production towards all Guilds.
        - Each Artistry policy unlocked grants:
        - * +1 Science in every City.
        - * 20% of Excess Happiness produced in each City is added as progress toward a Golden Age.
        - Adopting all policies in Artistry grants:
        - * Unlocks building the Louvre.
        - * Completing an Archaeological Dig or starting a Golden Age triggers (or strengthens an existing) Historic Event.
        - * Allows you to see Hidden Antiquity Sites.
        - * +3 Science from Landmarks.
        - * Allows for the purchase of Great Musicians with Faith starting in the Industrial Era.
  - decisions:
    - #0:
      - toolName: set-persona
      - args:
        - DenounceWillingness: 3
        - GuardedBias: 5
        - Chattiness: 4
        - Friendliness: 5
        - Meanness: 9
        - WarmongerHate: 10
        - MinorCivHostileBias: 1
        - Loyalty: 9
        - DiplomaticBalance: 5
        - WonderCompetitiveness: 5
        - Neediness: 5
        - Forgiveness: 7
        - MinorCivNeutralBias: 1
        - WorkAgainstWillingness: 6
        - VictoryCompetitiveness: 10
        - HostileBias: 10
        - Rationale: Adjusting persona to maximize city-state competitiveness (10) for the crucial upcoming World Congress vote on International Games in 4 turns. Maintaining boldness (10), war bias (10), and meanness (9) to ensure total military focus on capturing Dutch-allied city-states (Shedet, Ormus) and fighting back Rome.
        - MinorCivFriendlyBias: 10
        - WorkWithWillingness: 7
        - NeutralBias: 10
        - DeceptiveBias: 5
        - Boldness: 10
        - MinorCivCompetitiveness: 10
        - FriendlyBias: 1
        - AfraidBias: 3
        - WarBias: 10
        - MinorCivWarBias: 2
    - #1:
      - toolName: set-relationship
      - args:
        - Public: -100
        - TargetID: 1
        - Rationale: Rome captured our city of Satricum. We must execute a total war posture to retake Satricum and defend our borders on the eastern front.
        - Private: -100
    - #2:
      - toolName: set-relationship
      - args:
        - Private: 0
        - Public: 0
        - TargetID: 4
        - Rationale: We just signed a 10-turn peace treaty with Songhai. Setting relationships to neutral allows us to cool down tensions and focus all military assets on the Netherlands and Rome without starting another conflict.
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: Austria is the last remaining civilization we need to influence for our Cultural Victory (currently 95% Popular, 7 turns to Influential). Maintaining a maximum positive stance preserves our Defensive Pact and trade agreements, protecting our cultural progress.
        - Public: 100
        - TargetID: 5
        - Private: 100
    - #4:
      - toolName: set-relationship
      - args:
        - Private: -100
        - Public: -100
        - TargetID: 6
        - Rationale: The Netherlands is our primary rival and a competitor for cultural victory. We must maintain maximum hostility as we push to conquer their allied city-states and reduce their voting power.
    - #5:
      - toolName: set-relationship
      - args:
        - Private: 50
        - Public: 50
        - TargetID: 7
        - Rationale: Soften relations slightly with Mongolia following their denouncement to encourage them to vote in support of our World Congress proposals (International Games) in 4 turns.
    - #6:
      - toolName: set-research
      - args:
        - Rationale: Researching Telecommunications next to unlock the Interpretive Center, which boosts Landmark culture/tourism, and to progress toward 'The Internet' for the ultimate tourism multiplier.
        - Technology: Telecommunications
    - #7:
      - toolName: set-policy
      - args:
        - Rationale: Adopting Futurism (Autocracy Level 1) is a game-winning move. It grants a massive burst of Tourism whenever we conquer a city for the first time, scaling with our current Information Era. Since we are about to conquer Shedet and Ormus, these tourism bombs will immediately push us past the 100% threshold with Austria to secure our Cultural Victory.
        - Policy: Futurism
    - #8:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - GreatPeople: 40
          - Mobile: 80
          - Diplomacy: 85
          - Nuke: 95
          - Ranged: 85
          - Spaceship: 0
          - Naval: 75
          - Expansion: 0
          - Growth: 20
          - Defense: 30
          - Wonder: 40
          - Recon: 5
          - UseNuke: 95
          - Production: 95
          - WaterConnection: 35
          - Gold: 75
          - MilitaryTraining: 85
          - Science: 40
          - Air: 95
          - CityDefense: 30
          - Happiness: 30
          - Infrastructure: 25
          - Offense: 95
          - Religion: 10
          - TileImprovement: 20
          - Culture: 85
          - Mobilization: 90
      - rationale: Pivoting our flavors strongly toward Diplomacy (85) and Gold (75) to maximize City-State influence and secure alliances for the upcoming World Congress vote on the International Games in 4 turns. Culture and Tourism (85) are boosted to speed up our influence over Austria. Conquest grand strategy and high Offense (95) are maintained to leverage the Futurism policy's tourism bombs upon capturing Shedet and Ormus.
  - tokens:
    - inputTokens: 89087
    - reasoningTokens: 7875
    - outputTokens: 904
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Victory Paths**
            
            I'm currently focused on achieving a Cultural Victory. We're very close, needing just one more influential civilization, Austria, to secure it. My immediate thoughts are on how best to achieve this final push.
            
            **Securing Cultural Dominance**
            
            I'm rapidly assessing the race for Austrian influence. It appears Netherlands is a critical competitor, nearing Austrian influence in only six turns compared to my seven. The win condition requires influencing six civilizations, and Austria is our final target. My priority is to solidify this last connection before they do.
            
            **Accelerating Austrian Connection**
            
            My immediate focus is on accelerating our connection with Austria. While they're nearly at 97% influence in six turns, and we're at 95% in seven, Rome's elimination of a Great Musician is a setback. I'm exploring ways to boost our tourism to Austria, considering our current hostile relations and lack of open borders, despite being trade partners.
            
            **Re-evaluating Trade Strategies**
            
            I'm examining our trade route network, specifically noting the absence of any direct links to Austria. This oversight is significant, as such routes offer a substantial tourism boost. I'm now considering how to establish these vital connections to accelerate our progress.
            
            **Establishing Trade Routes**
            
            I'm re-evaluating our trade options with Austria. Despite mutual denunciations, our active defensive pact and existing trade partnership allow for establishing new routes. This is critical, as trade routes directly impact our tourism, which is key to achieving this victory.
            
            **Winning International Games**
            
            My focus has shifted to the upcoming World Congress, specifically the International Games proposal. Winning this vote is paramount, as it offers a significant tourism boost that would secure our Cultural Victory. I'm now strategizing how to garner enough support to pass this critical resolution.
            
            **Securing Congress Votes**
            
            I'm analyzing delegate distribution for the International Games vote. Netherlands has significant leverage through their City-State alliances, which I'm accounting for. My current priority is securing enough votes to pass this key resolution, and I'm investigating potential diplomatic maneuvers to achieve this.
            
            **Conquering Rival Delegates**
            
            I'm now focused on a new strategy to weaken Netherlands' delegate count. By conquering Shedet and Ormus, which are allied with them, I can disrupt their standing in the World Congress. This direct action should directly impact our ability to win the upcoming vote.
            
            **Disrupting Rival Alliances**
            
            I'm shifting focus to directly diminishing Netherlands' influence by targeting their City-State allies. The recent conquest of Shedet and Ormus is a significant step, and I'm now evaluating further opportunities to dismantle their delegate support. Our ongoing war effort provides a strong advantage for this strategy.
            
            **Researching Crucial Technologies**
            
            I'm now prioritizing research towards technologies that will directly amplify our tourism output. My analysis indicates that 'The Internet', unlocked by either 'Satellites' or 'Telecommunications', will double our tourism, which is critical for the Cultural Victory. I'm currently weighing which of these paths is most beneficial.
            
            **Choosing Research Path**
            
            I am currently evaluating research priorities to maximize tourism. Between 'Satellites' and 'Telecommunications', the latter appears more synergistically aligned with our Cultural Victory goals, especially with its boost to cultural buildings and landmarks. Therefore, 'Telecommunications' is my chosen next research target.
            
            **Adopting New Policies**
            
            I'm now focusing on implementing 'Futurism' from the Autocracy tree. This policy offers a substantial boost to tourism from conquered cities, which aligns perfectly with our current military actions. This seems like a game-changer for achieving our Cultural Victory.
            
            **Adopting New Policies**
            
            I am now choosing 'Futurism' from the Autocracy tree. Its immediate tourism bonus from conquered cities, like Shedet and Ormus, will provide a substantial boost and likely secure us the Cultural Victory. This seems to be the most direct path to victory given our current situation.
            
            **Analyzing Diplomatic Levers**
            
            I'm reassessing our standing with Rome. While they captured Satricum, we maintain 100% influence. My current focus is leveraging our peace treaty with Songhai to concentrate efforts on Rome and the Netherlands, and our defensive pact with Austria remains a key asset.
            
            **Adjusting Diplomatic Stance**
            
            I'm re-evaluating my diplomatic stance with Austria. Despite being denounced, our defensive pact remains, and I believe shifting to a friendly posture could bolster our tourism and prevent future conflict. I'm considering the impact of this change on their perception and our overall victory path.
            
            **Refining Diplomatic Alliances**
            
            I'm fine-tuning our diplomatic standings, maintaining Austria at 100/100 despite mutual denunciations, leveraging our defensive pact. Netherlands remains at -100/-100 due to our ongoing war. Rome, despite capturing Satricum, stays at -100/-100, reflecting our current wartime hostility.
            
            **Adjusting Diplomatic Ties**
            
            I'm refining our relationships with various civilizations. Rome will now reflect an aggressive stance due to our ongoing war, ensuring we fight for Satricum. I'm shifting Songhai to a neutral diplomatic position to maintain peace while focusing on our primary adversaries, Netherlands and Rome.
            
            **Refining Influence Goals**
            
            My current priority is solidifying our influence with Austria, which stands at 95% and requires seven turns. While the Aztecs are a weak, one-city vassal of Netherlands and at war with us, I'm maintaining their diplomatic standing at zero. My overarching strategy is still Conquest, as it synergizes with the 'Futurism' policy and directly boosts our tourism by conquering cultural centers.
            
            **Securing Congress Delegate Supremacy**
            
            I am now meticulously analyzing delegate counts for the upcoming World Congress vote on International Games. Netherlands currently holds a slight lead in delegates, but my strategy of conquering their allied City-States, Shedet and Ormus, will significantly disrupt their voting power. I'm also exploring how Germany's UA can be leveraged to boost my own influence with City-States, aiming to secure a decisive advantage in the vote.
            
            **Analyzing Delegate Alliances**
            
            I'm re-examining Mongolia's stance. Despite past alliance discussions, we've mutually denounced each other. This significantly impacts their World Congress delegate count, meaning they won't automatically vote with us. I need to account for this shift and recalculate our delegate advantage, especially regarding the City-State of Ouagadougou and Germany's influence.
            
            **Capturing Key Cities**
            
            I'm focused on capturing Shedet and Ormus before the upcoming vote. This action will significantly reduce Netherlands' delegate count by breaking their City-State alliances and securing my victory.
            
            **Capturing Critical Territories**
            
            I'm actively pushing to capture Shedet, which is nearly defeated. Concurrently, I'm assessing Ormus's defenses, noting our overwhelming strength there. My immediate focus is securing these territories to cripple Netherlands' delegate count before the World Congress. I'm also evaluating the strategic use of my Great Diplomat to secure an immediate alliance with the unaligned City-State Cahokia.
            
            **Boosting Diplomatic Flavors**
            
            I'm raising our Diplomacy flavor to 80. This critical adjustment will prioritize diplomatic units and alliances, especially with key city-states like Cahokia and Sidon, to secure crucial World Congress votes.
            
            **Optimizing Diplomatic and Combat Values**
            
            I'm now focusing on fine-tuning our AI persona values. Increasing Diplomacy and Culture flavors to 80 will bolster our influence and tourism, while maintaining high Offense, Mobilization, and Nuke values ensures our military dominance and security. These adjustments are designed to synergize our diplomatic and combat strengths for victory.
            
            **Securing Austria's Influence**
            
            I'm prioritizing Austria's influence, aiming for 100% despite mutual denunciations, leveraging our defensive pact. I'm ensuring their public and private standings are maxed out, as this is critical for securing the Cultural Victory, especially if the International Games pass. Netherlands and Rome remain at -100.
            
            **Adjusting Diplomatic Stances**
            
            I'm fine-tuning our diplomatic settings, focusing on relationships with Mongolia and the Aztecs. Mongolia, currently at war with rivals, will be set to public and private 50 to gauge their World Congress support, while Aztecs remain at zero. I'm also reviewing available commands to ensure accurate application of technology and policy changes.
            
            **Implementing Autocracy Tenets**
            
            I'm now focusing on integrating key Autocracy tenets to amplify our progress. `Futurism` is the chosen policy due to its synergy with our conquest strategy, providing significant tourism from conquered cities. This, combined with researching `Telecommunications` for its future `The Internet` benefits and landmark tourism, solidifies our path to victory, particularly with Austria.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: IfljUwRLzx2BgwwY
          - toolName: set-persona
          - input:
            - DenounceWillingness: 3
            - GuardedBias: 5
            - Chattiness: 4
            - Friendliness: 5
            - Meanness: 9
            - WarmongerHate: 10
            - MinorCivHostileBias: 1
            - Loyalty: 9
            - DiplomaticBalance: 5
            - WonderCompetitiveness: 5
            - Neediness: 5
            - Forgiveness: 7
            - MinorCivNeutralBias: 1
            - WorkAgainstWillingness: 6
            - VictoryCompetitiveness: 10
            - HostileBias: 10
            - Rationale: Adjusting persona to maximize city-state competitiveness (10) for the crucial upcoming World Congress vote on International Games in 4 turns. Maintaining boldness (10), war bias (10), and meanness (9) to ensure total military focus on capturing Dutch-allied city-states (Shedet, Ormus) and fighting back Rome.
            - MinorCivFriendlyBias: 10
            - WorkWithWillingness: 7
            - NeutralBias: 10
            - DeceptiveBias: 5
            - Boldness: 10
            - MinorCivCompetitiveness: 10
            - FriendlyBias: 1
            - AfraidBias: 3
            - WarBias: 10
            - MinorCivWarBias: 2
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: cPbVoMvr0IuchaqV
          - toolName: set-relationship
          - input:
            - Public: -100
            - TargetID: 1
            - Rationale: Rome captured our city of Satricum. We must execute a total war posture to retake Satricum and defend our borders on the eastern front.
            - Private: -100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: d4Gx5FAhoK1kWqGu
          - toolName: set-relationship
          - input:
            - Private: 0
            - Public: 0
            - TargetID: 4
            - Rationale: We just signed a 10-turn peace treaty with Songhai. Setting relationships to neutral allows us to cool down tensions and focus all military assets on the Netherlands and Rome without starting another conflict.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: rwZB5wJEOYasfAGa
          - toolName: set-relationship
          - input:
            - Rationale: Austria is the last remaining civilization we need to influence for our Cultural Victory (currently 95% Popular, 7 turns to Influential). Maintaining a maximum positive stance preserves our Defensive Pact and trade agreements, protecting our cultural progress.
            - Public: 100
            - TargetID: 5
            - Private: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 06Gimfof7Hs8moeA
          - toolName: set-relationship
          - input:
            - Private: -100
            - Public: -100
            - TargetID: 6
            - Rationale: The Netherlands is our primary rival and a competitor for cultural victory. We must maintain maximum hostility as we push to conquer their allied city-states and reduce their voting power.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: MAWlKuNeXBHAlL7X
          - toolName: set-relationship
          - input:
            - Private: 50
            - Public: 50
            - TargetID: 7
            - Rationale: Soften relations slightly with Mongolia following their denouncement to encourage them to vote in support of our World Congress proposals (International Games) in 4 turns.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: BMIQl7r74CWYb9s0
          - toolName: set-research
          - input:
            - Rationale: Researching Telecommunications next to unlock the Interpretive Center, which boosts Landmark culture/tourism, and to progress toward 'The Internet' for the ultimate tourism multiplier.
            - Technology: Telecommunications
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: W3FgE3OJoSAb8gwO
          - toolName: set-policy
          - input:
            - Rationale: Adopting Futurism (Autocracy Level 1) is a game-winning move. It grants a massive burst of Tourism whenever we conquer a city for the first time, scaling with our current Information Era. Since we are about to conquer Shedet and Ormus, these tourism bombs will immediately push us past the 100% threshold with Austria to secure our Cultural Victory.
            - Policy: Futurism
          - providerExecuted: undefined
          - providerOptions: undefined
        - #9:
          - type: tool-call
          - toolCallId: TBl9V8Cui7jm5hm8
          - toolName: set-flavors
          - input:
            - GrandStrategy: Conquest
            - Rationale: Pivoting our flavors strongly toward Diplomacy (85) and Gold (75) to maximize City-State influence and secure alliances for the upcoming World Congress vote on the International Games in 4 turns. Culture and Tourism (85) are boosted to speed up our influence over Austria. Conquest grand strategy and high Offense (95) are maintained to leverage the Futurism policy's tourism bombs upon capturing Shedet and Ormus.
            - Flavors:
              - GreatPeople: 40
              - Mobile: 80
              - Diplomacy: 85
              - Nuke: 95
              - Ranged: 85
              - Spaceship: 0
              - Naval: 75
              - Expansion: 0
              - Growth: 20
              - Defense: 30
              - Wonder: 40
              - Recon: 5
              - UseNuke: 95
              - Production: 95
              - WaterConnection: 35
              - Gold: 75
              - MilitaryTraining: 85
              - Science: 40
              - Air: 95
              - CityDefense: 30
              - Happiness: 30
              - Infrastructure: 25
              - Offense: 95
              - Religion: 10
              - TileImprovement: 20
              - Culture: 85
              - Mobilization: 90
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: IfljUwRLzx2BgwwY
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: cPbVoMvr0IuchaqV
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: d4Gx5FAhoK1kWqGu
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: rwZB5wJEOYasfAGa
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 06Gimfof7Hs8moeA
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: MAWlKuNeXBHAlL7X
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: BMIQl7r74CWYb9s0
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: W3FgE3OJoSAb8gwO
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #8:
          - type: tool-result
          - toolCallId: TBl9V8Cui7jm5hm8
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.