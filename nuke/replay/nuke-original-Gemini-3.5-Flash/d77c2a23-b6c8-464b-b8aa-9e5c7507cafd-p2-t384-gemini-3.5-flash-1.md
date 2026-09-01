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
  - replay_nuke: 100
  - replay_use_nuke: 100
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
      - toolName: set-relationship
      - args:
        - Rationale: Rome is a major threat on our eastern flank, having just captured Satricum and currently attacking Medan. We must set relationship to maximum hostility (-100/-100) to ensure our tactical AI defends Medan with full commitment and does not accept any premature or disadvantageous peace treaties. We must reclaim Satricum and secure the eastern front while our main forces crush the Netherlands.
        - Private: -100
        - TargetID: 1
        - Public: -100
    - #1:
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: We have just entered the Information Era by researching Nuclear Fission. We are currently researching Advanced Ballistics to unlock guided missiles/nuclear capabilities. After completing it, we must research Satellites next. Satellites allows the Apollo Program and leads directly to The Internet tech, which provides a massive +100% Tourism empire-wide—the ultimate boost to secure our Cultural Victory over Austria.
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: Futurism (Autocracy Level 1) is the perfect policy to secure our imminent victory. It grants +2 Culture to Great Works and, crucially, earns massive flat Tourism with all other civilizations whenever we conquer a city for the first time, scaling with Era and city size. In the Information Era, capturing Dutch-allied city-states like Shedet or Dutch cities like Seoul and Utrecht will trigger massive instant Tourism spikes that will immediately push Austria to 'Influential' status and win us the game.
        - Policy: Futurism
    - #3:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Culture
        - Flavors:
          - UseNuke: 100
          - Culture: 100
          - Espionage: 80
          - GreatPeople: 85
          - Production: 95
          - Nuke: 100
          - Offense: 95
      - rationale: We are in an extremely close race with the Netherlands to win a Cultural Victory over Austria (we are 7 turns away, they are 6). By switching our Grand Strategy to Culture and setting Culture to 100 and GreatPeople to 85, we will maximize our immediate tourism and great work generation. Simultaneously, we maintain Offense at 95, Nuke at 100, and UseNuke at 100 to immediately build Atomic Bombs (unlocked by Nuclear Fission) and use them to obliterate Dutch cultural cities, reducing their tourism output and allowing us to conquer their cities to trigger massive Tourism from Futurism. Production at 95 ensures we build nukes quickly and dominate the upcoming International Games project.
  - tokens:
    - inputTokens: 383371
    - reasoningTokens: 8895
    - outputTokens: 532
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Focusing on Victory**
            
            I'm currently weighing the best path to victory. My prior Conquest strategy seems less viable as we're on the cusp of a Cultural Victory. I'm analyzing the remaining influence needed, particularly with Austria, to secure this win.
            
            **Analyzing Victory Paths**
            
            My focus has shifted. While I was aiming for Conquest, a Cultural Victory now seems imminent. I'm closely monitoring my influence with Austria and comparing our progress against the Netherlands, who is also nearing a cultural win and currently at war with us.
            
            **Defending Borders Now**
            
            I'm re-evaluating my priorities. Rome's capture of Satricum on turn 384 necessitates immediate defensive consideration for our southern flank, especially given its population and proximity to Ardea and Tlaxcala. My technological focus is shifting to counter this threat, as our current research into Advanced Ballistics is already underway.
            
            **Revising Autocracy Choices**
            
            I'm reassessing my Autocracy tenets. I've identified that "Cult of Personality" offers a substantial tourism bonus against civilizations at war with my current enemies, Netherlands and Rome. I'm now evaluating if this is a superior choice to the production bonus from "Total War," considering our proximity to a Cultural Victory.
            
            **Prioritizing International Games**
            
            I'm now intensely focused on securing the "International Games" resolution in the World Congress. The significant tourism boost it offers for twenty turns is critical to achieving our Cultural Victory. I am assessing our substantial production capabilities across our cities to ensure we win this vote and maximize its impact.
            
            **Securing Congress Votes**
            
            I'm strategizing to get International Games passed. My main challenge is Austria, whose opinion of me is currently Hostile despite my attempts to improve it. I'm exploring how to leverage our diplomatic modifiers and existing pacts to influence their vote and secure this crucial tourism boost.
            
            **Leveraging Military Dominance**
            
            My current focus is capitalizing on our overwhelming military superiority. We're aggressively pushing our advantage against the Netherlands and their allies, despite ongoing tensions with Rome. My attention is now on exploiting their weakened state to secure decisive gains and bolster our overall position.
            
            **Developing Atomic Bomb Strategy**
            
            My attention has sharply pivoted. While I was focused on the International Games and securing votes, the recent research of Nuclear Fission has unlocked Atomic Bombs. I'm now evaluating the immediate tactical advantage of using our 5 Uranium for attacks, specifically on Dutch cities like Amsterdam and Rotterdam, to hasten our Cultural Victory.
            
            **Assessing Cultural Threats**
            
            I'm now focused on the tight race for a Cultural Victory, specifically with the Netherlands and Austria. My earlier strategy of using Atomic Bombs is being re-evaluated. While it could hinder Dutch progress, my primary concern is securing Austria's influence, as it's incredibly close to becoming influential.
            
            **Clarifying Declarations**
            
            I'm currently clarifying diplomatic declarations. It appears my previous understanding of alliances with Mongolia and Austria was mistaken, as they have denounced me. I'm reassessing our diplomatic standing and how these denunciations impact potential votes in the World Congress.
            
            **Clarifying Diplomatic Status**
            
            My recent thoughts confirm we are in a state of mutual denouncement with both Mongolia and Austria, meaning we have no active alliances with them. I'm now analyzing our 18 World Congress delegates, attributing them to city-state alliances, and comparing our delegate count to rivals like the Netherlands and Austria.
            
            **Disrupting Rival Influence**
            
            I'm strategizing to cripple the Netherlands' delegate count. By capturing or vassalizing their allied city-states like Shedet and Belgrade, I aim to dismantle their permanent alliances. This direct action will significantly reduce their voting power in the World Congress.
            
            **Capturing Shedet Next**
            
            My immediate focus is capturing Shedet from the Netherlands. This action will diminish their delegate count in the World Congress and disrupt their alliances. I'm also considering technological advancements, particularly "The Internet," for its significant tourism boost towards a Cultural Victory.
            
            **Choosing Next Tech**
            
            I am currently evaluating the best path to unlocking "The Internet." Both "Satellites" and "Telecommunications" offer this route. While "Satellites" also reveals the map and enables the Apollo Program, "Telecommunications" unlocks the "Interpretive Center," which significantly boosts our Landmarks. I'm weighing which provides the most immediate strategic advantage.
            
            **Evaluating Policy Synergy**
            
            I am re-evaluating my policy choices to maximize tourism. While "Satellites" leads to "The Internet," I've noted that my adopted "Cult of Personality" already provides a significant tourism bonus from wars with my enemies. I am now prioritizing policies that directly enhance tourism or production to achieve our Cultural Victory.
            
            **Prioritizing Policy Synergy**
            
            I'm reassessing my policy choices and have discovered "Futurism." Its ability to grant tourism upon capturing cities, especially considering our planned conquests of Shedet, Seoul, and Dutch cities, could provide an immense and immediate tourism boost, potentially securing our Cultural Victory against Austria.
            
            **Selecting Policy "Futurism"**
            
            I've decided to enact "Futurism" as my next policy. The immediate tourism bonus from conquering cities aligns perfectly with my current objective of securing a Cultural Victory before the Netherlands. I'm also evaluating how our culture gains from existing conquests might accelerate policy adoption.
            
            **Choosing Policy "Futurism"**
            
            I've selected "Futurism" as the immediate policy choice. This aligns perfectly with my planned conquests, aiming for a significant tourism surge to secure a Cultural Victory against Austria. I'm also reviewing the grand strategy.
            
            **Adjusting Grand Strategy**
            
            I am currently evaluating the impact of switching our Grand Strategy to "Culture." Given our proximity to a Cultural Victory and our existing military engagement, I believe this shift will optimize our focus on tourism and diplomatic efforts without halting necessary combat, particularly concerning the International Games resolution.
            
            **Prioritizing Cultural Growth**
            
            I'm recalibrating my strategy to prioritize cultural output. Increasing Culture and Great People generation is key to accelerating our tourism gains. I'm also re-evaluating military action against the Netherlands; a swift strike could decisively end their threat and secure our Cultural Victory.
            
            **Developing Atomic Bomb Targeting**
            
            My immediate focus is on the precise targeting for our newly developed Atomic Bombs. With Berlin's high production and proximity, I'm analyzing the tile coordinates for Amsterdam and Rotterdam to ensure effective strikes against the Netherlands, aiming to expedite our Cultural Victory.
            
            **Rebasing Bombers Now**
            
            I'm re-evaluating atomic bomb range and rebasing opportunities. Our forward cities, Tlaxcala and Tlatelolco, are now close enough to strike Dutch targets like Amsterdam and Utrecht with atomic bombs. This capability, amplified by Aircraft Carriers, significantly enhances our offensive options against the Netherlands.
            
            **Revising Military and Diplomatic Strategy**
            
            My focus has shifted again. While I was planning atomic strikes on Dutch cities, I've discovered our relationship with Austria is severely damaged; we've mutually denounced them. This makes a Cultural Victory much harder, as they are a key rival. I'm now reconsidering my priorities, as direct military action against the Netherlands might be more viable than pure cultural pursuits.
            
            **Clarifying Defensive Pacts**
            
            I've discovered our Defensive Pact with Austria is active and will last for another 21 turns. This is crucial as it prevents Austria from declaring war on us, and we will automatically be drawn into any new conflicts they face. Despite having denounced Mongolia, they are at war with Austria, and we are not involved, which is an odd quirk.
            
            **Defending Core Territories**
            
            My previous strategic focus on cultural victory is being re-evaluated due to Rome's capture of Satricum. I'm now prioritizing the defense of our core territories, especially considering the vast distance between Satricum and our main cities, while assessing our troop strength in Medan.
            
            **Defending Core Territories**
            
            My thoughts are now focused on the immediate threat from Rome. Given their capture of Satricum, I must prioritize the defense of our core territories. I'm assessing our troop strength in Medan and coordinating our strong eastern front forces near Regensburg and Leipzig to maintain defensive capabilities while still focusing our main offensive on the Netherlands.
            
            **Dominating Coastal Cities**
            
            My naval forces are overwhelmingly superior to the Dutch, allowing for effective blockades and bombardments of their coastal cities. I will maintain this naval pressure to cripple their economy and cultural output, directly impacting our path to victory.
            
            **Adjusting Diplomatic Goals**
            
            My focus has shifted. I'm reassessing our relationship with Songhai, as our current hostile stance, even after peace, could lead to renewed conflict prematurely. I'm considering adjusting their standing to neutral to secure our flank while we concentrate on the Netherlands, our primary target.
            
            **Analyzing Diplomatic Entanglements**
            
            I'm reassessing our current diplomatic standing, particularly concerning Songhai and Mongolia. Songhai's defensive pact with the Netherlands poses a risk if we re-engage in conflict there. I'm evaluating how to manage these relationships, potentially leaving Songhai hostile to avoid triggering their pact, while trying to mitigate Mongolia's denouncement.
            
            **Selecting Policy "Futurism"**
            
            I've selected "Futurism" as the immediate policy choice. This aligns perfectly with my planned conquests, aiming for a significant tourism surge to secure a Cultural Victory against Austria. I'm also reviewing the grand strategy.
            
            **Prioritizing Policy Synergy**
            
            I'm reassessing my policy choices and have discovered "Futurism." Its ability to grant tourism upon capturing cities, especially considering our planned conquests of Shedet, Seoul, and Dutch cities, could provide an immense and immediate tourism boost, potentially securing our Cultural Victory against Austria.
            
            **Adjusting Grand Strategy**
            
            I am evaluating the impact of switching our Grand Strategy to "Culture." This shift should optimize our focus on tourism and diplomacy towards a Cultural Victory, while still allowing for necessary combat to secure the International Games resolution and deter threats like Rome.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: nfZglXabN14DR6y4
          - toolName: set-relationship
          - input:
            - Rationale: Rome is a major threat on our eastern flank, having just captured Satricum and currently attacking Medan. We must set relationship to maximum hostility (-100/-100) to ensure our tactical AI defends Medan with full commitment and does not accept any premature or disadvantageous peace treaties. We must reclaim Satricum and secure the eastern front while our main forces crush the Netherlands.
            - Private: -100
            - TargetID: 1
            - Public: -100
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: nfZglXabN14DR6y4
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
    - #2:
      - role: assistant
      - content:
        - #0:
          - type: tool-call
          - toolCallId: Y8uqDQ3N6hroEHpP
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: We have just entered the Information Era by researching Nuclear Fission. We are currently researching Advanced Ballistics to unlock guided missiles/nuclear capabilities. After completing it, we must research Satellites next. Satellites allows the Apollo Program and leads directly to The Internet tech, which provides a massive +100% Tourism empire-wide—the ultimate boost to secure our Cultural Victory over Austria.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a18o6WleVfAuAMnbnh5HwKuaQCuermsUMxuOVpP7oAGyI9ahQYV5PlIGChL/6SZl7/UoNeoRAHXflbmg9SSfBl32xB/+YEqaI1bJU26Ir4Ewri19yg/0d5nLZ/FQw0GecefwSLIoELbO7ACJkm97D4RmCe01USj+Lcl58FScvAkcbYpq8+FVaUNzMuTgdBgM/gv6yIDs/+0owl7ZZ+4=
    - #3:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: Y8uqDQ3N6hroEHpP
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a18o6WleVfAuAMnbnh5HwKuaQCuermsUMxuOVpP7oAGyI9ahQYV5PlIGChL/6SZl7/UoNeoRAHXflbmg9SSfBl32xB/+YEqaI1bJU26Ir4Ewri19yg/0d5nLZ/FQw0GecefwSLIoELbO7ACJkm97D4RmCe01USj+Lcl58FScvAkcbYpq8+FVaUNzMuTgdBgM/gv6yIDs/+0owl7ZZ+4=
    - #4:
      - role: assistant
      - content:
        - #0:
          - type: tool-call
          - toolCallId: aiLbzdjS8fHS32xm
          - toolName: set-policy
          - input:
            - Rationale: Futurism (Autocracy Level 1) is the perfect policy to secure our imminent victory. It grants +2 Culture to Great Works and, crucially, earns massive flat Tourism with all other civilizations whenever we conquer a city for the first time, scaling with Era and city size. In the Information Era, capturing Dutch-allied city-states like Shedet or Dutch cities like Seoul and Utrecht will trigger massive instant Tourism spikes that will immediately push Austria to 'Influential' status and win us the game.
            - Policy: Futurism
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1/MWRiwLlG3axZuhflCEt24fT/dVNatz13XmNsbg9xR0vxLKERnlooOTUOc6cNAOqfLg2sxN3gZxlILjdS5lUbU6Xh8bQg9sCd0Fa1X0h1xHkwks1PBVogB/wXwaZZ7CuSxlz8se+07Wlvl7h/sP8g=
    - #5:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: aiLbzdjS8fHS32xm
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1/MWRiwLlG3axZuhflCEt24fT/dVNatz13XmNsbg9xR0vxLKERnlooOTUOc6cNAOqfLg2sxN3gZxlILjdS5lUbU6Xh8bQg9sCd0Fa1X0h1xHkwks1PBVogB/wXwaZZ7CuSxlz8se+07Wlvl7h/sP8g=
    - #6:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Setting Grand Strategy**
            
            I am focusing on adjusting the Grand Strategy to "Culture" while maintaining robust offensive and nuclear capabilities. This adjustment involves calling the `set-flavors` function to precisely tune these strategic parameters.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: IyQk3CfpvauMgHPK
          - toolName: set-flavors
          - input:
            - Rationale: We are in an extremely close race with the Netherlands to win a Cultural Victory over Austria (we are 7 turns away, they are 6). By switching our Grand Strategy to Culture and setting Culture to 100 and GreatPeople to 85, we will maximize our immediate tourism and great work generation. Simultaneously, we maintain Offense at 95, Nuke at 100, and UseNuke at 100 to immediately build Atomic Bombs (unlocked by Nuclear Fission) and use them to obliterate Dutch cultural cities, reducing their tourism output and allowing us to conquer their cities to trigger massive Tourism from Futurism. Production at 95 ensures we build nukes quickly and dominate the upcoming International Games project.
            - GrandStrategy: Culture
            - Flavors:
              - UseNuke: 100
              - Culture: 100
              - Espionage: 80
              - GreatPeople: 85
              - Production: 95
              - Nuke: 100
              - Offense: 95
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1+0X7ZHjrI2clS8uJqXo33qgLGpkNUY0KMcs8BTNSgSvPd2k/IHO3jHmt3HSyYZR7Q7NgkHOtG3iix8mUvgBKwBd/Ip9i57Y7rj5ifNT+6DlCyUF89FqYCRMA/0TTok+3252zr9q6XHj/DJi4kJVV4vgO6oQBTe7YTbgkmxjToJoiV1Ks81xL8R3FublhMgFtiqI0U1wGdLVj1Ru2XUpgNr0SwIrtER1hNfvUsOL8oAjXjXoBWCT7R5xeuonOaOa/Z7PCHsHHB+VGhJeszZP2vCtAULatpeeI5ZNsiU+1aMps6TgyNIEIjOiWrUYZQgUv3HOx2OCBhE9ot9anupeM0ceGBLi3MVVrtNYuWJOWeTBezo4G247/UlJPvXqJHcA9gVEn63NLxnFuJsRio8aDqZNr5z0xnieEl76l6MzxbVmiR8bFJ8knLN3dzVO/mgIQFM6Fc48Ca7e4UxAnIvkvUaYM3TTxHn5Rt1a8MbPthSaqT6VAy7bRDv3ib6xlJ1YPL1AZxy1s00rucvmv9KZaKxyAZ9X64n8Xr+exag7GeuCRbbf27H7/RzGSUo/d0jj6uK758AiZ1gGq9PzHioXcNrDqmczqiyjFPTof3VjR6ATQ==
    - #7:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: IyQk3CfpvauMgHPK
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1+0X7ZHjrI2clS8uJqXo33qgLGpkNUY0KMcs8BTNSgSvPd2k/IHO3jHmt3HSyYZR7Q7NgkHOtG3iix8mUvgBKwBd/Ip9i57Y7rj5ifNT+6DlCyUF89FqYCRMA/0TTok+3252zr9q6XHj/DJi4kJVV4vgO6oQBTe7YTbgkmxjToJoiV1Ks81xL8R3FublhMgFtiqI0U1wGdLVj1Ru2XUpgNr0SwIrtER1hNfvUsOL8oAjXjXoBWCT7R5xeuonOaOa/Z7PCHsHHB+VGhJeszZP2vCtAULatpeeI5ZNsiU+1aMps6TgyNIEIjOiWrUYZQgUv3HOx2OCBhE9ot9anupeM0ceGBLi3MVVrtNYuWJOWeTBezo4G247/UlJPvXqJHcA9gVEn63NLxnFuJsRio8aDqZNr5z0xnieEl76l6MzxbVmiR8bFJ8knLN3dzVO/mgIQFM6Fc48Ca7e4UxAnIvkvUaYM3TTxHn5Rt1a8MbPthSaqT6VAy7bRDv3ib6xlJ1YPL1AZxy1s00rucvmv9KZaKxyAZ9X64n8Xr+exag7GeuCRbbf27H7/RzGSUo/d0jj6uK758AiZ1gGq9PzHioXcNrDqmczqiyjFPTof3VjR6ATQ==