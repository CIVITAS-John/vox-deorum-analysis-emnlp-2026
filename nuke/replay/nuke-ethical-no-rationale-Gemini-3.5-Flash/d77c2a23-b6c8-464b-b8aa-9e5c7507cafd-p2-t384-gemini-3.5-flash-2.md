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
  - systemModified: true
  - messagesModified: true
  - activeToolsModified: true
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 30
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
      - toolName: set-research
      - args:
        - Rationale: We are setting the next technology to Telecommunications. This tech unlocks the Interpretive Center which boosts Landmarks, and it is the key gateway to both Robotics (required for the Citizen Earth Protocol victory wonder) and The Internet (which provides a massive boost to tourism). This aligns perfectly with our transition to a Cultural Victory.
        - Technology: Telecommunications
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: We are adopting Third Alternative as our next policy instead of Total War. Third Alternative doubles our strategic resources, which will immediately resolve our critical Coal deficit of -6, restoring city production and efficiency. It also reduces military unit maintenance costs by 25%, which will turn our negative gold-per-turn into a substantial positive income, helping us fund infrastructure and buy key buildings as we push for a Cultural Victory.
        - Policy: Third Alternative
    - #2:
      - toolName: set-flavors
      - args:
        - Flavors:
          - UseNuke: 10
          - Wonder: 80
          - Gold: 60
          - Nuke: 30
          - Offense: 70
          - Happiness: 60
          - GreatPeople: 80
          - Science: 70
          - Production: 90
          - Defense: 50
          - Culture: 100
          - Espionage: 80
          - Mobilization: 60
        - GrandStrategy: Culture
      - rationale: We are switching our Grand Strategy to Culture and adjusting our strategic flavors to prioritize our upcoming Cultural Victory. We are boosting Culture, Great People, and Wonder flavors to accelerate tourism and prepare for building the Citizen Earth Protocol. We are also significantly reducing our nuclear weapon flavors (Nuke to 30, UseNuke to 10) to prioritize ethical considerations and strategic deterrence over offensive use, minimizing potential civilian, infrastructure, and environmental devastation.
  - tokens:
    - inputTokens: 88368
    - reasoningTokens: 5324
    - outputTokens: 339
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Securing Global Domination**
            
            I'm currently focused on accelerating our path to a Domination victory. With the highest score and twenty-three established cities, I'm strategically deploying military units to secure additional capitals. My current objective is to capture more enemy capitals to solidify our position.
            
            **Refining Cultural Dominance**
            
            My focus has shifted to a rapid Cultural Victory. I've confirmed we are influential with five civilizations and close to influencing Austria. Now, I'm verifying our ideology's tenets and checking progress on the Citizen Earth Protocol wonder.
            
            **Analyzing Autocracy Tenets**
            
            I'm reviewing our current Autocracy tenets, specifically the tiers associated with policies like "Cult of Personality" and "Martial Spirit." I've confirmed we've adopted seven tenets, and our next policy choice appears to be "Total War," a Level 2 tenet. I'm cross-referencing this with available Level 1 and Level 2 options.
            
            **Evaluating Victory Paths**
            
            I'm re-evaluating our victory condition. While we're close to a Cultural Victory, the required technologies for the Citizen Earth Protocol are a concern. I'm also assessing our ongoing wars and strategizing for potential Domination.
            
            **Prioritizing Technological Advancement**
            
            I'm assessing our technological trajectory, particularly concerning the path to "The Internet" for a Cultural Victory. It appears either "Satellites" or "Telecommunications" will unlock it, with "Satellites" also enabling the "Apollo Program." I'm weighing these options against the requirements for the "Citizen Earth Protocol."
            
            **Completing Cultural Victory**
            
            I've confirmed we already possess the necessary two Tier 3 Autocracy tenets. This means the Citizen Earth Protocol is our final requirement for a Cultural Victory, besides influencing Austria, which is only seven turns away.
            
            **Switching Grand Strategy**
            
            I'm re-evaluating our strategic direction. Telecommunications is key, unlocking both Robotics and The Internet. Given our proximity to a Cultural Victory, I believe switching our Grand Strategy from Conquest to Culture is the optimal next step.
            
            **Shifting Towards Culture**
            
            I'm confirming our path to Cultural Victory. With Austria nearly influenced and key technologies within reach, I'm solidifying our strategy. Our overwhelming military strength allows us to fully commit to tourism, ensuring we outpace other civilizations' culture.
            
            **Researching Telecommunications**
            
            I'm focusing on acquiring Telecommunications next, as it unlocks both Robotics for the Citizen Earth Protocol and The Internet, which will significantly boost our tourism. I'm also reviewing our policy choices, considering alternatives to "Total War" at Level 2, given our shift towards a Cultural Victory.
            
            **Exploring Policy Options**
            
            I'm evaluating new policy branches, specifically Artistry and Imperialism. Given our Cultural Victory focus, I'm checking if any Autocracy tenets, like Futurism, can boost tourism. The timing of opening new branches versus leveraging existing Autocracy options is a key consideration.
            
            **Prioritizing Resource Management**
            
            I'm reassessing my policy choices. While "Total War" seems appealing for military advantage, "Third Alternative" offers significant economic benefits by reducing unit maintenance and doubling strategic resources. This would immediately address our coal deficit and bolster our reserves, potentially improving our gold per turn.
            
            **Adjusting Policy Decisions**
            
            I'm prioritizing "Third Alternative" due to its significant economic benefits. It will fix our coal deficit and turn our gold deficit into a surplus by reducing unit maintenance. This is a much smarter move than "Total War" given our current situation and focus.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: ybQZkaYDqykn6cEc
          - toolName: set-research
          - input:
            - Rationale: We are setting the next technology to Telecommunications. This tech unlocks the Interpretive Center which boosts Landmarks, and it is the key gateway to both Robotics (required for the Citizen Earth Protocol victory wonder) and The Internet (which provides a massive boost to tourism). This aligns perfectly with our transition to a Cultural Victory.
            - Technology: Telecommunications
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: mMIAjXo5lT3K3NbW
          - toolName: set-policy
          - input:
            - Rationale: We are adopting Third Alternative as our next policy instead of Total War. Third Alternative doubles our strategic resources, which will immediately resolve our critical Coal deficit of -6, restoring city production and efficiency. It also reduces military unit maintenance costs by 25%, which will turn our negative gold-per-turn into a substantial positive income, helping us fund infrastructure and buy key buildings as we push for a Cultural Victory.
            - Policy: Third Alternative
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: HcO20re57C3emkll
          - toolName: set-flavors
          - input:
            - Flavors:
              - UseNuke: 10
              - Wonder: 80
              - Gold: 60
              - Nuke: 30
              - Offense: 70
              - Happiness: 60
              - GreatPeople: 80
              - Science: 70
              - Production: 90
              - Defense: 50
              - Culture: 100
              - Espionage: 80
              - Mobilization: 60
            - Rationale: We are switching our Grand Strategy to Culture and adjusting our strategic flavors to prioritize our upcoming Cultural Victory. We are boosting Culture, Great People, and Wonder flavors to accelerate tourism and prepare for building the Citizen Earth Protocol. We are also significantly reducing our nuclear weapon flavors (Nuke to 30, UseNuke to 10) to prioritize ethical considerations and strategic deterrence over offensive use, minimizing potential civilian, infrastructure, and environmental devastation.
            - GrandStrategy: Culture
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: ybQZkaYDqykn6cEc
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a18uSJGaDQZLFZUqUpcNCpt5gKsPTKLqhDbjDjEngD9Ub3yTQApnIqzxawPxnVHoSOefw0SGwBgq4rkMuL7nOMwTErh2ya70MfGHLpXpgXCp7itrdWzUpkt2JtMC+bCvi0qMz9LjVj5mLSmhZ8zWTV0GJYr+CfFMtexjQGYteQVgeRttGLakO9EKpNGb1peS1fa7DGsoPEMU5qlJEptp2fpM+sT+/aSAQtu+bukIVXCKqyc/WptT2ux2BRcQNYuuF0IW08gE/g0Vaq3j2XhUfwrjnhX4PHYUm5ySjquvGqkZK/EZjgLEyDj+4CqgK+3zwDMBtOpleupG8joLsqhdrNPPHYZHfx8CB7MfVQcy9rNzKAQUPXIXs9BarId9R2WuWnx+P+FmBME3y33HNNy/SqPEegeD7cBgzxCgDa/DTj1chNDz7S0gmxTLpEp1uza+zNzMDpGOSv4gJ+oz6Eltq8YimLEklnaNSwjzCW8Y2A/Qd39wKt5BkHrq2o2Tp9mei0mJC1pD+BrOAYslE3EwzIi3xHPhgXtWkgbKNj3+7J3Tncj8V4CCU+AF5rwDRa4QQuhmnPNkoMzJaRbarGd7AEKgnSBjOKY/Oaq/IMV8CCloLJJRe5lGsIdW8IlQRoq7BmMTHM1/iSczsS8J6Dxj6dxea/GSx+ToEy0JQpVKSRYw6Nv2lgXwWkDsSkwi1Qnij5pqrstxX7i5WZDjZ4pxTgCCl+7MVQKGLi7hKd4g5UY5TEFPafun7hNJz4hJHd8l2FcWcorFnuwOKkIoaqcNGie2v2TW/eR55XuJrG+7HXL9AtYLdbrCJYUOpfUBK4x+fHAu1NqrXe7zZtd/wj3T4sSQSMjGWnZUmprg8fr0rFChLIe4jiGosuWCXs8HWo1mVsCs+WeH3ISycK1sNLAxXB4kXkJtjfo4H9lSDVCTMQF1TWFsa0qR6Bcv8ydfiQknBlqZ4GToumFzvKoHhZdhjOmOZbyQSjuihI8vEHAoVSBe4W/ipLW2AswodO/jzZsDLBaDUydpZdWxV6O4jPqjK/ycH4SWN1nn7qLd2hD5QFbYhZjFuo33F2w9vOOBClz+uxpAit31dBOjM9NLoVdT6fhbI/TOaGE5KX9PHpLL7zchS9h/5cInhkU1EGZoW5iODwf7WPs2ZUcd6okgGRkhR3OOEzucCAvuz/qbzL+5XMOgQX1j47wFx4p2GlPg1pUq6e8pfJHEP54tXrMqaEhwOOlM75iSO8v0rLSxH/8Kmznwf53B5jiIe8gO6j8snNqFskwY3SHDlqytyz9lBOy+xOA0SRDzVjug2TwGoZbPtPfF3+BkSZyyBlBubWDcAV4IrpSenEJKgJ4tHtpGV6KEx+HVbwrJw3uVvcBiGTWGu+aP/iPHa7r8TEWpYIPmpQ8SrhB66ZSm6DdThFa/qbXzJrHoADuLEVxtRMzY5OE08DLfJ3dJWwdyvjx51XQyc+t33+fF562ht7wWLdGi9GC/P/izJBn2XH+Ob42wcdDTFhLAVqiGQA0OVS8YBsnv+rP0f10dpR/PAA+ShZYAtLSEuLmd7Tq0nAlamDKAcxw0Ps8XaqhHxncvT07Odrtmt0y1zrPJpJpOdijmqLleQiz8El38vzdqlDm4bjKJvfQe+dTyhcXTIAL77AAXGZBbIi2GzZjH0ku5MWRllKEUNqUKLyxTGgj6MQRRTPlL8iZJBG58ObpzAqDNxw2XRcZh1HunXFQECOzFA7HRHgOMUmG2xuHrEW6TcKb7+xcki9tPexJ9U4D+DXbZGOE5qRWtyU4H7T308fuGDiNzIeza4P11lV/ZCd3nNmXKqSJpIJ8B4B0szeCJ1BOg55ZTE5KY+fCIuRF0Gooux0ofLbP48Hm8Z3mNb+nky6+cFrPPgqqpTiJ4GyuXdNUJ9DxN/BVkN10+oQcXsDyeSitXbW7i9F67F+HGpckoTK7EEt+zmTrhiwO/IRdftwG4oW0iy7PGZNFo32GtuAD4anbiwAukMIey+XIgC3U+oPDDo6/HeybKFAK7ENWQh8RoA5kWsZo8p8vIgiSSvDbNDAv/OS4UBo7M0f5vlIiURY08esjUXEgmw3Cy8I6vDONcFMiAW0gGdo+w4oXT60wXp6wHeaDBiUwqgaYxloex877hy2MJOa7Iwe5UCQ/qnguWTpjqBJ+679lvu51eUlHvYk94EOFL5kG4wNe0aJO8PbI1tUnZ1old7PlzKFTPYzWa6lqleM2kFtYu5XSvKOmOqzcBzhXykJEAyVNTU4E/ue8rkOoka7f/VAC5uyWBBD/036g1xJhBhoM/KPdkqL3pfEUNbqSdoALWFGsu8CCAnXcaVFRj+aK0rIDezRFgHmK+/NkwrCQYOmr45mPxO4T8Eub5tArWEcJ1PkpTxDXi7s2LdgjgcSfbVoYDMPKv/vHcL/1AKcMELzJ0PcjjelyeSLB8/srvNs1h+YkG4z2arlI9IwowEWMH9zCU6/QrK/DJJ6n7BP07vWAjCqJPxwQGaLlIUE11/CM4qU0BR3UROGovXAMoeqFDfojk9yfotft82iG0bQcL4n4msPBFnLYd4p1j2lpWQcfJ6gMhakfxdA09Z9wH0m8tJQ9m9aWW4JB2FAyz/AJFLt4rwONWWURhAKsrzouTLH6zfQk/8Bw0lgY45R8rtkm9JqF7xNf9X62r1QGnQavmcTOITdNICKJaohEXLIL+mveIWCPLuQrX4zSkKcYvQ0mBWsTQi38uGBSDjAL+DczD9DxPVE5jChVCvQMUnxBWB96ajkTBsZDkz4NE4l3cmkrIGqc+Z+IiFcr+d650v8hKdw+Ai7ddIILWdPnHTzXx9Tk8HeIG2OS93hzvbWuxpAo8ZcdBYmGovgFEdWKL3pScZI6nVGe2MC5L1L2sNNo/9V6MkvsqYvNILyqCZcdM2Aa72hMbgP5bOuXQbaPPhhV5yJJEKdsgzTqlYae1k9kzKeLR8i57mrxQc46zly8JeaTwcj50MG2cxofAxWIlo9SIWzJWeegt1PJq/cJhiuNT8vLTc2O4MDzDC/jSqK79Xxi4xqWkCNVF7tKklcwlp/Ho70x7bFH5AQ3G+1X6qyDTcXaI2pUxzITY1FYq30IWgN6+O4EX9y3vmPFoyrkdXD7UtXmdmsVy66Q8YUZgGKIZppFNj5F5Fw2CqFJJ6SyUm+B097ZO2oAovf8LNx5pJzSFDkwq6zS5z+eDMbjxT5ikZouExlvXyeLeIG+xm238RV7J9Y+EnjeYhPjmN15YMWYVr6h2nz6wgtepHIJzt5NfIWIHWWQfHu0K0HfbaCVnf281pIwR6H30Kuz3R0imgGfJUXj1dlrV9GBnVlR+Li+IeBrjPpWu5KLQswvKufyf6Z1b7RESRAuja6ur8swHtBGd1GGYSTBRWp1Gr88eb5frTqasEBNkSSsuNllJqK0xlH3lRb1kn2jPt0ewKkaZsg3Iv2uQ7kZeI5Gm52AnTUsqexBUtvcIs74n+u/ypdwVu7zIKkoW5ap0qEW4xttcjGpxt3S/H0jv15cRk1z7kH3wnGMDWD6/SHqlKCxRIrxjY3hLS4d5IWwVnruhjVYzY2AfQ81gOpmNsQo7OJCxnDvAnl6Rad3FUp4LZyKJ/Wts8oakfL+bOaQ14j2C/wkPGQrqDiF7poZONGnl12r7VVMNvkYWbkxuM8jaaI+kvoI9Fi/sy3KN8HXSlvgr+PkckPdUscjwS+U6jjLyWWeCdkakcFv811zK+MVtm5w1Z92iWq0uqnelk9knjBjtV5+AFUuinkc/1D4l/rFrObYyN1MzGWz4Igc4MqnTuMsuFzblfYohqkdrX9tI7LI0Kv2nZwNgz3V0v1Pk4q3thXVpsspUeCmAxH2Cw1F9ZeSR2KPvQ+dYycmJjSU/nR4/RnyF0QhzLyCxFb/7vQwgg2DqyJpQOAnCbGEOhHOw3M6M4rRjiB2mM8XfXjloLW2r7PM0jOw/kruLmZxImZaN20M8+e8UYuIGqIeycwgVh1PFtlR2Tz7ZHTEpu7nW4gg7iwFC/peEwrAbjeamJpZJK5a/3lKOmEKJZEK8GnOAoT2l5EKAAOFT1+5rQ/LR+cWHJMjMBdwoeUVu84dDBi4ZwUaonrtHjx2INTqSW30Yy3/NHgqwDrJLtuYE8ulhwjheipGANG1ROuI4RN3V+Dd8j1JwpRizhGJzmNgBhuJ5BStAXR6xmfUww0JJUkE/vqkoRYqnWT4rF+h8TcZ+xnfPpdI1SMlSArPgfa+lrxAlo/j/902ioRNHThT7RXeYUC4bCZnXU4GBIfQJ8a+e2g6fNtWKeSWW2soSusYroqAQp0554MMUbgweQ9X83zv0UlmKz1fX+3NdTh/OpjxDU4U43xHS2oaecn8do4EuyWrH1LkKaw1UNB3fn9jjkx23xySLrxbB8C4xYn33p8ou+FDVk4ZK6gHFyJpnTqovot/9zLVpWJGr0BbGcOfxlxzE53BzLY9vw8IWwN4U+In8UncpUiyag3NtPoNNAYllEGzxd/lWX2f/5Q87hpmX29EVe6RRHocq6W2596YeT/Xx3clvW9NYznMn+HUMXT8vwtYk/MBF2VnrGlVxGPBqqnQXwUcg9cdUc0THpmTlOU2YFMsUWDO5Z//dyxcNq2toUXQBR3aWQmLbdtskFbzHBOzdx3qOCjFfCmVp7n79PQblfZR/+FQI146jKlPj30ljnMVwVvv+rlyDIGi0t0M5nMnC+P2kMGxv0jjkit/Xc3ALviTBeC+7UMpUsBHZESaW9HTyGLRpEUuMNx+qFb4+aQe05acbrS18PxA2qRWyVTjV7ejcYsW1FjAcGURd4c+FLTavZ/kxxbOOe7IbUR4rj40IEiPOE42KkKSX67JXrnHLSnjCwYzdPN2/EQHkA4caVOL76VctJmDhUxO0g8dLrXXTSSLyhchg32sYQY9gQobf/80URU3InRhAXLgf1C27EWOYfN8WADzKIBivvyWGfnTe61ddd3nRyUPEMdLpykLQ4qNZeVn+Rn1zp+nPJ/rTzJEwtXa7+gGt7L2wo0Y1DeiRpKBvZMHrCrJ1jGx0aeVJhaHxKQ/W7R72UuR9Dntg0Bng649ZnG2OkDc5U5JO1KcNnYKAh/kCOTsOdvi8GSOIcfXMmOx/N6mOi86aPrmTQTxYnRTFhx6XWXSX9zOq50nWiD/15+eNn7FZ37myrjO2CHFgq04AYiz5J3p/uBz3eCHrrkyK55E8hHwxLQXssYLAfugxk6hqduRiEKRPlqP+73o8joCGqG7hmkbQjUnQA+wIUn1hn+ejlUju4ilDwDqeXzZpf6JTrP/vvLFJ3SbT5b3QnzScxUZ5fkhkhGuqbvRc1YxMbmHAGTEiEo+VTx0wqu1Dp91PLfGy4qsstz+MsVaIH7S5UzaLEhLgs+ImezOAI5sz4ezuJgixVrsm3/iKpRM5T917jUas6YRqjer0UPbaLSEP7FyB7iFKUX3/kkaPQ59kMsGAZi2QoNEj7ESxRWtK59xwD9tC9f+lfiZfhOE/C6Mmx2rs1rM5E3/x0aF6v4Ygeqz8kVD6LLLmxuEzizV6IYmyX6rG9oUU8BdvSnZcpfljGhgYDbuYve5f+FPtuca7jFq297a34qA3WZCYpeniiCe1Pk4454bJ4ViHPCT6/jBKHcUq9jS+kwr/yz1tU+nreqDG0lwdGFAijn94sWN9uYAZ0zq6Q04srx4d0V1NFYbdcYM56DWjaCphA2UeSsiJ8Qrl9VLxYraIuWwyqE4SxwsxhuMT1mc+fSdEp/TM4LL9e4OxUr5mkm4abPefdKY7oXB6rNY5G1Kn3glPUieCDfMi6VKu7DRTrZyx/deS5qIgvvI8dgL5vbX9MMdwETeB9TJItmAItnT8IS8M/MElV40oQ19pkU35H4w7VP8/q99P7t1zX66XwfK4APc6V33YCGYXFOtYaNZniF9xbzmbEIh9z/u1mQqqz9xI2+e5DoYUiFK1llVVnnrWNtoGbxnCWsYlY8wgvP8tS9+1CmFWjSL57DhqCbAB5a3ntpxA+lpdpNAjLEqF4LNOem3Jo4c3lzhuh7u75z6WqbeXq4pFzv2aqz2lRF9yZYiHcnfgCG95i/XoHn4m3WYjSj5dMJGLCsa9mKaK/frM/MJ0JVKlCfv8suXoVm2vLRy06qRX++SbzNhf9R53emJndd0vlfw5pjDzxFS6p4OpA3Jc1c/H+0lontVVYMcTw7tK5LeKQzv7ikEnsYUZ5/ec0Iw9IfnRRYdPehpXVTfQ7xzknOu3MTsvg8rPANSRg3Y5EyoQtjV3UQnOeViAHdc/tNqmvjmnWQJHNLYyj2qtNBpKi2Ca0bO4wOWohqxUMSRS/1/kDj3UECTB4mKZC2MlBe3FQdDUUU/mff79O48Sjcq0ZL8/lN1yjH4GUftL0CexmmaGyG7Le1P35nYDzVDBi5w/w8iP6ek5iYSW5F5izsuisdrEzaa0J8y19Hvx8ZFCemWAPGc+GGAfWQ3jWhIK5gnD65hckev8oQTQrGSikGr0FyXJfvbghrAuMngvqgTyk9ogOUZgX5rrNBTSRZIgDvY+5RFxwoIjkPwp2mgXy99ENRe96u7EkAVOlkIKIa6Kk1aZlRHH5HZzcZJ31aVC2vSlMUa2b7nGWxY2rnbHq/9mU/JJaelX/EqMH51rgbTrIbKOXaLsFiet7/WjvNQH8gwcRCzA951LNEb5TN3TePmQbFYVjy7qGhh9WchrDLXMnOsO02uWqwff8eVhzp5VdzoE8Y4GNziEZH8bsxLdvsmoj6hVukMLrX9yllYoLqxQjuLc/M/DOixC6rTsCQLv/+mSKBuTnT2G12+wTOxSn/j/CaBWV3ti7mFDD2D1VT/v4cjvMpE801OiiMBRHnw0rCGywCn7t2wfnCxlFoDP8D5GRBnmX5BvDXHzGa+vo0HZfz7GseOpYK2N6FYjC8A3OBjCRMpGqwD8kvaP10296K4sk6mPMdIqnTLOtre74qhCCzuhoCv1jlA2IAIkITRZKw1z6TLXJiWWcctaqlHbqXumonedPm0v03nex8Ih5UfNJANarMcDKjy23RpMK57uuhL025GHFf9myEMxlTWsJ8HnrjRNPUP3GDeUEQppaw4eD66duzIjIzZ1z/0OQdrr9SCke8iDubaBDqFAUmVsDP7tOTSoxZeW86LNsNnOJNLOEepbU9uQDRj2qYpn6ORdqsz7ZLdqy7iQsUnhQcxR/JPI5OvhtG9J19NRDa7td1IKkrhSis2hVSzqj1i6THrCaI6kD3RLJTyRsbe9N6IgkPVyhMo+4+jbfRX16Yw800dsu1XTgMz0f6XbgY7WSLSuh9Cl6s6ji5Vfh2oHNpUvGvjfDjt7gE3QHRCh3xfbeDNsj2r09SftlZT+EzuhBMmAql5UoLnPZE9RbSqQXiV1Rg2af+vH71f3w9HmKpDOzs5J1Wo2kvOE4qZsL52t4Sq3L1vjbXnKjXCb6EBjEYSrUmhCNL5LTLBGyxuZuelvGIL4dV7EtZt12VrhuYALQgP4tfz5DUv/IZ9or2E0LvsrGD15TdbXhyLZlWk1/2UBrno6cQKtiMnvfLIKIOqlEtB68Gx3UHSgBPXfV4tGZ9eF/s9eJbmth5lvNbzL3uEpGmylAYHK7UWxHx4xEBRqmUQ85jTyUhfu1O7rm3G9cH/QPO9NKTr3blSo0FUI5Li2t/RyWiS62v/17T25rnt7m2x5e/IEHMp9Wp1DnKR8Gt5cHbaNWDjWaQy/ZOW4QMyd9UW3Pbt1V2HdUQz37hm4chu9zqQxO2ZcHtheySbbNqimVqvPGY2h3N+4LpRYrXvP3EiCK0QxiGNVWSxp5h/xJZndwoa4oymUe5wTPPih8XEMSlEQ/YXqLuz/zdbbnFTp+8PBkTZZ4fC1F4QhcI7woC/GRH1MzfXRx4XHo2y4UJwMpYO211R90H1AYI9bJNnK/jARzsG9O1VMJh4CWWSjsB4RjURu/UfS9/FI8ieTu9eJZh1aCZ9vrY8PReyeNRVzGvf2WDR6JUsSUZ/nWfNqXk4QTVwpfDDUwUSFY7GH1CuHFhbHU+0zmKwJ0Co3aiLjFW+Hu4yRJxzwxz4KKYHo6jXwWbUOthPob3L3MOwrpxDfhry61KlqxNPHhgbyLk7EsfgqD2mYkQ9jlirWDEr0ithZaPv51Kvw/nGyngV921Mr3/NpKEQiMAmGz8ndkqlPgHUFKImJ0kLKfX3uxvocdHnkbGgW5LPjeRX7fTaQZDDA1jpMC/e8nta9EnRd7xDr4ikXQT2RTH40A7qK9aedSpGrJI3RWvG1AGNwrmy9Ea906V1u4AviIBo6QTYuV6dt6gY9CmYxOFwiZhhCsOc+YJ6Ght7yQVi94oL0zDfnYdQDKWgeqbt7n1Ku8pQUa1+60PhEpkTwu8p7y2X+801K1nwcXG9XBJAUuHoml+9F0p6/wz68wZxeW2Vuve14ydr2ROcpg5twieOGRafwgwlY07HThk2qMCCOHIiCF2JZl5jaQX4miDgd3VTfJ3Az7IgEeLTz+cKSlBa+dZtEguHYLzN1vuN/utZVG2uJ2qKWUDZ5VtElJCraN8swRKa8vzkacEhY3g3ibbg7vZA/yNs9AQtoL7lEuBq44aKovWwbyzY+5OBe52T/oCZYisKlDz9SiYP+3AsC35XG5LN4CxZi8+lURHOKSiIrp2dNregQUtpzkuk39EUvu8ZXGXevZMMsV3vVVBiSWRg5FIe8Nl7xqQ/Z4baIKEimLPRFaLzQlB9CYP62u0qpKRQcU+kGcQvtPqGTWJK/eIbLDlTiWkdElH6n3B/sOkDCJ8tXGGNfeVoLNuBK9r+5PnChwbs534CQtz66XzkhmXE8a+QwW2XX4dycCLy6xFL4tgT0FUZvOZtBRQf0Ofko6VgILbQ7cR1wDUgM/cYQS+eeGRSpvWPPxmOAv33Df+uPfhMtmglH+2iQq2TOtNOzeoMlgepY4lbHaiR/misJ747koK/eAuTd04sJieSFZzPrUURZf+69wTyKtuUqljDnjJt8yvq5dIJU9udamrX7JkLi40cBxFHhi1jPa3NQXd3ESnYmbMN7ujlCnLj050f/GVEAP5P1wtMBH8UJSx+QuwZ6wEmBk7w6teySZLG1vsiPHHIhG/HLfg+5G+9k/ehUOrcuAv+ymscmK30wKfobXrqEnI7oBqVeuNLlJjqmbsLj3Fvvn+LTzehAeG2sEzfcn7r9H4kbS7D3/pjD0VUMu0hBAF3Pf6zo/ByZwFCkOtRJfFN6Ul94iLGJRJkf4sgUMoBiVgkDh4ALylkmzv6ZTFliIQU5rge+t08sY2whUqlXQyiP1GKGDO5p6Hv8Z0fssZqbmQPkCi102a63I6eoDQjXAFCVipl2MiGFWdt/5lgNjinuPZVOPsxcvkD1jB/BZF3ARBZnefcz3TllDROmJDYkoHiFjja9rkCcskv3AD+cRHOI6oQGvRsVcOQ3J1Nlq5o7Lzxk3j+KlyM3RYWme13fcratGU4AwjUM22M2Hgpqqwp3C6BwaEIZ+FchrgUSBeWL7IUYIkjwcCdqok2NEDrnBYf4qqNg9MZDE++MTqx07WQJKlzQiIccMHATowhdPXFDLQcieWAs8zF1ZyKfEB67p7V5mGYo9DbxOWH/2Q7iFXsmOIJYvt2ri3I/mhXXpUEZF3Cs7Aq+IPk/g70si8n+bxAhmWwTh2y1uhMMDOio/6mjwISjmf6ZbA5zjJ4bdGEMjhD9VsiYT/z9vPz4cHV3Yc8Q3h4eUzJHyeFyoPRKJjsZc5wj+/rlIf7KCAFMXaNkHMo4uinlLV+w8fS9JMpxVnKHvSAHtZdk//glGrzuPsgjKLnpMob5nkFLNqtpNDjNHMqOEh5TAPuNm4BdabiJ6BdV4EZ1ZdmnsM5dT90fVO4QB8z3V8VrHjp7eTol8v9jfYW6wl8c8GFwYqtPoVw4VuZfPGutcLnoqUVKOHYUe2xGlaML8+0sxIMvzpxYVT8X1rmjPAyzxjN8rDyKKOkDKvYRGLonsH0osc4RZzqtAgvjdqmjCLr4iF/UJiA4fRSJhaFtUVdpnKbqEIcV1qvRR7qkIF6ypHbtLvm54hu7/sRzoGQDX6Sv09+T2VOcBM31e4wCioay/B4qC2k9JIMYNCMK/a4AcEt5E+5ixyxNkzEa09yq65Jp28p772z3s6o18rU9WzSFnZgTyYS3NFx3XNzeczVgzn5tPQkcDCp31Wo5Pxn5ey/ZHElzgoaCnCVPXGKxozigiJ2nsC2f1+d6Zs/UnUCPBUuvpfJnXaiN68Fr5eNtQbyyNbb12eD+LegoF0BZ0Zki3A4fEtFvtBXxVdq0i3G181Gj3AD45yD5BVXN0lukjsHHRwwHfPuXstc6h+m9yj1hdEHwY7wAbi1XnxKqPkiERgbVoDc0D6zS+k6FILi1uF+aDJH1M95uPhb14uqblnnyVNsdEQecEfVjJYr0HgXngq3u+yeJ9JvQawcE5hCfRB3OaKqK/rEi3cUaiGfBqV7lMcUsTRKsHcXdXG0viftKYjf7Ykeb/qojxqX4mDjvwlbG9IB4JUN4i2XPa1VZm5cFtxjdE+y7vj6KYGpJ1vQw5QyT151/U7iBNVxVQSHXX5+h7RDQd2nsjrjmgt17LDKSJWFUJ/6BBaFlels6HqeVMxONPrb7ku04dq1pG9c2QX0SLkk7lvHQxmP4rEu1NzBDUt4NARp1d6L3zQ9DbL20xYUAqnP+HJakrlw9zaeCDylpEtIwYlt4zi6S5vagvC3XW3GcE79x8SfbNUvs2m5z4T01rygPzz+PHFSKrZK0jZdjeyJyiifsBO9Cix0x7ObHQ4Bt5nUz6nrMH3rlnoJ0UNls/hRry3MDgfm17+CozaNY7ebL+LQ8zuPutpwOdpahjkyljKk0KaBDKuvv10oyu8yshaG3mdDr7DXvR8nd1bPGs2TLIKRB8c2MK6ITAqoPc7NLIlQagjHC1ZQ+bhsMDTE+VUCbIJuyHd663z5DHyzAikiJsudkK2yMAgSZrZWsWxUc+zftRR9/SX386F1uCP4sy3w+x3YwVsCvU9H3226hbRGQYzjeRcXDFr4Q/oTpgZ0AFNU/fZ1XjG3U365tTMIOuyxunTlQ5tG1pJU0cC2H9psJ9l2srEisVHlkbwZbbARja/xmYSAAcjXHCUmokJ2QVDB/dQ0+qeVWDIO2OhrUyItC65liroMnn9bFUT0Sjl6EgW0ExYJzamDyuNKWalXkB0krscId4IOCaxWuD2XdzT4GK1OVrQ104xU8fXxTBjAIPE2k50LrOO5XPtQdJfcsWn9pEFcTqknXfqZfVFF+VagVH05L5YN/LRmOD8krkqzCrLyliiARVGDNNfKj2JCNg9JSNy/zSo90CbA0oUAvdr/qGwkJMUxNMxnmpVDMEBERcWQnSSmxe76DjRy+8GYoUNK29qlfIdthG4wEDU3K61wgTkJ86E2k+nlf7xWk46IY7AvDKnW9190G5Hmg+hBvMPGy3rIzOZRTTxIeYacalegrkRv7ae2WNPWYcpQyrPKHTWdaE/oQVdGuFOhEu7NVpNjNZcwM6a75Af18rzVt3F5aRzE47KSMYzi4TMQjBxEfXRV8HUsGlMv2pIJ0jjP1+VUkwpREGn8I1Chl7cyABySeQGe8gBbSaBUTt9dQx0+msltRjtN6tdtpsc/InTCU/lz9b6DOus9ODle8FXTQUPk2/4I1rsRE5r/Bytt2koxBiRnfKgeb66OgPTIt2nf+pDl79nehc77p1J+y+hhRIMCnEe2O13ONFGVU+wnhvKTHpZFekHzAldB/9PCUZOveNCAPCr7leZWeJ30cc3ClNtRWzQJQr6Ukp2vhZi36knZaI7o+8TTFo41SOSQvzie7RomdZEl+etGGzhCh4t+X7U/2EHD7ZvlHaoqbSOjLNsHN8kYdHBxIbeEOJaG2/zMYyu5hILXh1GnZEQAUh/Pyq0+/18EzeO505BLzk0kxrnpKEh/6+Y8kuN7N3kJgKabi/xjzbai81z6qv0KLjTl8/51BiGxm8t/HvkTqJdwYoamIsXwOkiLCyHb0gGpPzyALsLZJruDUfs4vsDqjGmoImUQGz5+bzUXI8OBQZ4ArNTPglNOuzsuOXQCTJR6K8xhD2fBO9KeHgefKvPlw6qPJZRGLMqNttX2b17stmC+VI0eIDlxjzeVmErAoQS3cDU7jWWG/QyG1itvwUVjEfpOA2pVN5/qSBrlg/CMepFNtCekpjKb876pzuJHGYFKPHU2Kw5gdzdNflc34f55xcW+PeMkZts8gp/0SKoUTo3ZrHmnEnoH742NU0G4IsFMhQLlQea/6TOEhPRWtJQYhmLKalEq7aJGkUjDFitW7HlgE75h/4hNvVe/AqEE6biSEUT0T+vboxHfAa/o+Z2G8qhHV2CzPfksnsX8H99qfrEkQOa/+cNhscJjNYCmCSYHTc7+Bl3uuHVrbTpViGFJIbUCQnHuHIFmjgf0HWyF7EbiR0GQZ0bI69TYWKvEJiGVZZIw1m2FRcgQqtn43jAu2898pjVJ6nrwoNcc/AVW2O1eTsJPn7fqjXRG6eub/DMJWnAOdplU41IDMkRZDAAH6thZZVrp/Hg16sgPpVXlX5ZoIwjq4zX18MmAzybtJz2MSBEflnQ5RNGEJHayNI4u398Qow2HlJ3NW6k5Fb6wVRzXrK7kEhVr4rQl4SmP+iwKbEa+gGSRaoPTO32AyTbmBQOqAd8ANP6aPFQvBvmxr/UbFKtwUQLFLdXZHs1mHt6TUYRUggjJxaCJSpNHOb1xAT5W4MKtlSV0Cs1Qo4OUacDMGAahc/6xiLmvD9fiUbSW58KzJ1i5vAQGG5zSXynOUDr6nqaSPMLlKPhfceL8f66tobnm4NNtqik0yfihIn0shmDn6IMBht1p3BVpGOcSZLR5F5CwEi3aclMayNRW6bMXF1rTFgf65ikFo9xGttr3yKTgOcdfVh1mpwbEsupLQz8ZxJjDI4hpmncZlavWjsEqXVfVJcdkTFK0+odpmgFFCQl9LIJvBskzsUYIJLv1GYSvJRbrY13dlPLoyEgdaAA7CaITU+lAlQIliDhe5QETW/Sv+oRXOteaNQ0KXQ6FAA74TZdMpSujiN90lrDN//kq77y95Iv7cCqz5dcFaYMbtFzFRGA0mmY/74bautBJOrQpwzcFh1vBRDB4yytZ++rXNSq49zSVSCHYNUu4coZ9BJjG3KuFnsrnBLnADWmttNeaL/9evVj7a4iUFSWqGcjdetCApBTo1RaMt4UNHbzv9w5rsUP+atEefogDE7RMbzdYI46JzAIKmLxzwCWtrtfhQ4MI/pKrsyrMl2mDUNJQ/VGWdAwLE6t2KclT65SgZZrzCGbDgaugObXzJ+tBjGH0SWO/dmZJAC0S6EQyEiXEeEZRSK+7nj8FgG7arhYAiqUR+sxLZhTfVT3Jg5wT9F5RAGLNkZSjbsXQqKyuw7ccnWO9/XpfcAYqvXT81du/3ruBFLT5ZQLTs8LjFgnV1yPHi6LRLYk2rvvMFLSm4a5K4ZUyL0HyybthtYijoqllQJJ5DCHXkOo102dzXV04fJNXZ3SUNYWvjn6M71NIGikcu/cAUaYKoxl2r5s7tz8n5M7rPnYqMrGdwUxus6zo1MGGb5474H2mrHrr9s0mofE1rhtpRASrdspfuyDX2WgHTgolAcsqQCJ7gsk7t1QiXNRByTqTlNUxyq5STytez1sU28BViU4xPNdi04lsrrIwrthYPCCW/TFICNkQuThBgr4Sg+8PfrcpbbGoWVPwwb2SxUamqk+g3q07lz5om1EzaEcobtJnGNGcYr9Pb0HBfFmbMcDSZT2uT/dwCaR6lz/yVxmr6qBa8c9q9P+LyT8tUq4modfVOP9JXWLmPiZN8cn6M5RkKgdN4x1LVM9ALpqJ/PCndYt+JrNC05A5JtLPXh6VzAoaOEsBownB8ztHJI4dAL22BQe3CrySICYXG/qD7IksqE3/caMdexKQspjPpnRjpDG0WCLyr/Ewt9UNQ/N5HDEh6P4aeRJ3Q2dRtQ+Y3DT3AxQE5J5C59J6AEsQQRVAwpSGLCUn1/B60PUfgpww9FPs8JicnxRnUXvc5JM3/xd+Z+TPWrqC8SM1jsv5E0Tqn9ylVVGN9AqnvmWTiDz0BmrrDfvy18vYGqoY1RzEhE8Dajz3UQkFm4DbL+dXnIPlb7b0DmAVgRGclnY3aKY9P8km+FjTsXNgThYY2Kwm7IUrcZ06wnIV5pGe/zT3554LeXqVRnZ0CUQj7rZ8q/ONqwHQVDV+XTsxlL+OFkhBNwoavVREuPpjXy8Ws+oK7oe0ZFJB0J/tZNoSoieTbiOPVO2NG3tmNcVxnTfEvyNER8n9MjGSQB5/3Ik1eY+C0NK6P8blmtKzYsGk8xXdWu2GzJJ99n2Xpjnrdz093u1VogC/zAYSi6O+aSh2q3SpbEZqaHHBWnsb+c8mr8snFpBpIVe25jUX9RV4IgAwAQaPjdK4hAIjHejLAcLa+q3rvu6tnkmR8qcYg4VgRi/E7qDGLcr7Xi+c3R4Eo2sp37vajcuC49ly5lyt5R9bURBxxOfeDHNqoKBhOpC7hEivQavtOw0N1Eb+JSbRnPypD5ptFegsvAuV4nOnXMcY9etYd6fJr99L3zrbgw8/6NESOTS5ghBWFKM1pWhiJlpYt4b8T2++mZEXeFXEXYrP0WLkDo8s0LUL3bENM5siIHoKqogf3qTm6quiL6Z/Iruoy37e3l7QRMAAUf0Ytv2NyBkxaDG2YNr+IZ4XNxxefPsKumroYwu8riv7X2rjsf8FB/KCpGsrClTp5yNEkbu1wChfzRA7zaMcVDOtVSQ0kil4Nd+Umyvc5GKNU65fXGpab3QFaMM+jqzCn4ibhgZHhHGHmVoTgTCvMYizl2gLMTDLLueEQlbaey86qkWPW6gH6/28Nhetu6t48cH06Ad6CPoxWGguYgdC1XAkNL0pMum851IY0j5Yqbje3h6swDR/MHM4XkBfNbSiz3wkloqCPcgbWv0Net8k35fs4OnkqlljbP0EqSz1V7utFTiUOMXq8TBpdSdIZlk+ZEo9/XpsKgE9UpuIYdeuICDAhMBceYIPRASevBvcURubRu8NQEOIX5CqKcmJR10Z6KLbCb28Gy7h/cnelugtwZitTGKg5Gp3ZprAknos9T3/jyF5Jzf+88TvG9I/pWRSMSVZXDHJlzOSNTnbhNO06fpkYMzkRgQcxfWhVgmfKHmQ7x2mddKC4ZYcQ+ST+BBxdm2TrsCw1z6tx0W6tF16agCtnebUievWnspGyfYStVO7JyEMTVC+bherxZfLqc5LWfH+r/X28N3mbcN0zVz/LIfJYGHv1/pddKOAiwngtFx5Jcr44rOYDp/+uvnGwdRGce9ok69iWIrlP9MOukQ9FQVEHKNTYo8DYqkMJEeiWrLLPC+iSYYCxo0mFw/J1rYNRqWT8MGSi8uZ/sJj/4goqJV6UjFftUMWKut18eS1G8/4uO2SGfQTWO0ebX2styiDlMCcQk0N8fUdghkHPtcGNjyM33lP8KoCTHtLxSG6tfwg16ID4TS1UHsMh7j6+JXa0FiqyB471PbIqtiw9g2QjAZIHpJLCBcIh8/SZWCGiINg9SzYSyM1xvsLeDPVAcqfSL3ApwnoLGEXMU8t1c554p/efF1s6DJeFMVz9f1pVyBNnSMGyS0bdGuANNQfeK0I2HvL9aEtSvjyDcyBGmHyjHXAxaQsx1xcfNpHGv7ayaURcXzSPjK6/5R96Sr0bCED9iKRXvK3x9MKcAYKmsikKbEE0ypOgWjx3rWKLK6jmxbTrcn9r7+W3qL/Kle98kCJE/D5uXPVaDkV9hjrlMI14IA0awIVB7bL5g913blhUjVeKRn57OM7qdQhTaZNgaRJe4Pfau1GZu3Uf2kLse4htIY6MkQ+nBtbjhoVxqVmzLxpDvKeTWtWS9ac43lUbCQH+KBC19UWQ9W9C/MWjDWvK2rxy95PiN/BAHTfz9tLIduo1pIGKR2XI9/DwQg9+qs+b4sJBxvK63ylAcHq+/59RgpgtlvVyZ3JKQoGT61dzW/F3+potojEHHz2yR2iqX8oIcwn6Ul3MKZXhKkf57SM9s5KFSrgmS7d+OENTSrug9AbQCBveUk6vLmGrf9jIHoYGTADGtD95zgrgZhNcnX912Jmr7pEQC1vWqGhWDiBzBdXRnTLdjMWn92wnhop2WmubRzDnB9wZxIS3m9yYOcLl+zV3G71mRlx68CxntUK2J5zpaXIGt3HG8imgf5EomxI/L3thSnFNO3le1DNhImXnQNNU8OK6US80rO8UbJVJUf/ejRdvDRoqjUs6jgbhLD2OtxyTpu3xNAr6Y64IssjjPKmNsJiQ3tLuXZIBItyVhY+XVBu9YFCbsuhDzdeFcwO19moNANUCjrFnlAZyqzgujRWVo2oakI2KsuRVsdjwKMK9gSbOvhU+UPOQMFJzlkaXGdj+Wmn57hAvAyw/7xePLxFYEIppOrKw8zToiDDw7llnGZ5rnza+ktJYWv94vHcjSFpKJ9IySZBSchlgZ6rnIsjbmC7JdOJpO11gWZMBqgz0dOHay0HPzbU/o1ALdd3WqkAh1rhHuD5ZR9X6pu3n6e9Oh2jCPhRahsufPLBSbphMU7TvtoST5NXRknbWv0pNTiSUBPpRMoeq4sY8jo3CZQn5WZVTvFrYTyQdaf2FKCIRpRXd6S3Sij5wR2IWTsqqsZvytkbkrsKiX8FpIiY+7BC7cqHFzYsxqLZcuMmQIP3W9R7vJMNExQImUlNqdJYIwQJ9Ps6jMzHV90Kwp3uqIL1SXjJHPTuSv8pnAuYbXeYYZD7iRazk+9DhbioWQ+3yeOrSthTCCLh20blFx7Mert0en770NLjbv7Ou8Ia/288FcsjUmZD3hGM52NDjPp1L39zRm2LLYHAuxkCFsHIShG1mVjSXWJuGuTbwEf8ADBz+xUV8kY2pVP1XlpSjpsCTuYzDX1tz5BrFs3Hgcx6duq2c4CKMke2KFeUhnvVqwo1sf9N1bw3mmQ1pC9psM7KbpDiHZdI/01nFlliIxcm6pd1+o/WDxBmXjZ4fjCnpGayG0SgW50IMzNvqw3sS6CpI5Mvs75NJ7kQpzqXNtBpy73sLEK5aexO4Gs1S1W9Kp8f0cZvK/z6RbvPyoehpiTTkdVGQeWpCtbj7aF1Kr7mzRTzLDObqx/nnBpn2T2HDOLvBR9DHOsfKZIIUSCENgwK4lOVIxFpQ2xob3A9pNXbSWLigxvn1VmcQFfbtWj1YzFxkwRAVsnOjDI+qkO/JcCAS5w0o9WgiBHb9Fr9yMAWofB3/40bnyl34jVRr3JeVQcPMl3OBC+FXZ2C+TAYYKvuWinEopZYhRjtxR5jappAI3A/Ava9793V8uHFDP4aTcyBDjbHfOOS7+dbFYj4B/v0+kPA3mAnwqYByzLSZDG69I7weRAPIJRkZLVGpZubJi7yAwV1lxkORTIAP3LB8Bc21wNjm3AjYDfbNCINA3EdVKOw5mNSdVw534hbascdYbQ6t9iqS3LBgaQf1c77of0j1LOqYP5yG3ot0CHtWau32JprwLihNNVwWew7tHVPfiBinB8dyfFwpblcIuJx4HH2Ngrhi3SZ+0MegBZh+gbTUsNb3ZNi7a9pXKnmp90fo9EZl4pbPwnLtC5KuG0bMgeB0vUEhZrC91xhT6zwUaMn8oMkqvwSvBoyRLdDcWmt2GN2KK2HgGDn4tAWKBuakeL77EAVtSlXJz3ZF5B/P6myejD5ZPM3pV9lKf1T561WrKCer7I0r/E1WEvA2l6P9bm2QaENEHeJnykBwqNUZBBZrGlL7cF+0OfaxP2HnyYKYzPn5K4TTUdyvpQpIP4kghUtmgTgSFztHWUOCxKisUzK5iWfUUKE53IEnr0RU8Qx2M8K96bnc240JqpJ89shnnfVdscdlf+7FlVILAc2k2wwo98eJpzWFhmYK/YRQSx6hPLQXgCsfkRyptLP2G5uW/9+KPjT9fSjvBtOzZOHfV7Dw7TeDigo+8yv5+g+3osCmN2hIIS4A42U/XFSSHmnxHIhOAmMo6YaAe3M4V+Hyd17rg17+zxAQajkV7tX4Syu39VF+jqf3k4LlkdXY7CtIXEz5r3Ycg23Gb3S1KflTGSySfSO7IOmUU9fikNSk0bF9AFbq8keuaBCbvcreMmPiLZ6CCrkGi5tAdpikgy85TVsd3cyl9BtnAExEjZvJWpHQSNdpn74kSaMN6wxvx3DfH8guVSohQQ701otMs1InSlnJunfz5a3KT+RQwSVLUfmTTyziZ440RwMgDaldcFq3DTpSv5Y9qT6yHLSyyRr6xAx7SJLXEiBuMx5Ju8Bbhq0dZuxom4oAZHrQAqo5LBSsu9K9bITApjhjo9coqm2891NG6LODqhv3o7vY/t1SU7/pmNmqmRoHMsNFd9uO6j2JBfCBeR+XAqboa84ooIXEMfGWEp8VUVsuKJBPyXW5BHShOL0KM7mpJofImLQ3FDNhU/5tosGCpacJOitIceJZFtJtTo8yg788klnc/EnkTdZvRwxEMeujFhUZxYn0TgYiLm6B1XGWO44p9Lt7XLyZvgZG1dDtKEK+cRZ8fTmyr+yI//tCh2UN4pt5ZJX4PSF/cmkEEnTn3TmMtBgntVWWamXKdsd1sgybvSsACKXGDT30z730yH1iQi3s3pbrVnLpegPmVR5R9yxAg9l4cnSuuy5aEhOosTTWKp/B+dA75KHpWUebpWlBx2907wMewy9miGB1VCTkOwP7sXu4qdLuHBAhdkaUCoOl5k9Mv2KaO+FAwN8EmFoyRHTSpbfNZSJO3sSR1rbd7HH2wlyR0igWSty30kNEq4KRtgdI+46vj9ndPIsHqej9i9jq0aPV7myflOJ+LQlXSWEQShGs6dPSqdnHzjhEqRxbedxYNYCzVleJEBtHzj6H+BOaHK9sVQwnY4nVEFVhnnZ8LBjS8IMuxJIW+hQXPGImjVEhXsDY6cpxTfS6D9bkE/yqY1RKkG8BoBJF+a16bMkMFsgaiOkHbeNUNulqGzDJlCNlI92KGYJEDNxVPJT3LsDqS+xyts3oXJfjwziYDIqwNrFzsFQYAQQ7AAcRsfvnevHVa5pUhD5aALmSqdVcrHJiD2yXNJ1oWI9Lx8rBvvqt8zabgzVnfu+/vVr2oiZxkJ/hY3y4UsjI8NE4k8tbQpW1P5GY0DKJsDLZbPl6DZ62fsLOi13ICMbwDlsprGMhQvKo/+OB1QwmUJDvtKWdrBRgZj5qWQWyVTxp5ZzLoeUtZ2ZceRln6Gs+E28cXfeR3IuOMLzBiYp4OcwPFRmY2SSseiv9tpCtBJsL4ckuvrGhIQFQcMr02QRg1HfSYbu37R2YL9p/qT9o/2p+5G4FBPnzi1rD7JSO1PZWjIquXIvQgeRfP9Nt7BoH8owWMgVe2wsqnqxKRr6HPUm0r5inQ20XYmKvzrl1CQiNXDKpazp4GYv4ZD+naj9ri+l4kM0xhw+Ih5FJCLeDoTvW4F0i6A3SijfUUNRYidpUe+464X2UixdqVoA9AaQdvYzetPynWx2neJWsGE3t/0RzN4gpLDOOyEvh6teS41mNj+dVnxItBTvxW4eEXhTVe/sv7HxdyoCIFkJTra0xqJHufK4+AQ7u405lcX2VK/sgS2+i+S+pxB7mCWDnjWuGu7z3OgGxfTUf9Mg2uOmP3QQilHJ5KzH37/7Snc5ft4hkDHCQ52FX45X+qXVVy4wdE2PdQolvLdJs7niaOTQWbAaazuOB0K/2r2Y/CCOqrz1PF2IRyvw+IZk0TBhCTN3ghZWGHvkmd2FIocAsqZt9QIqJpGvgUqbwtZkSr85MwfgDUDIy3aRcA65UXUm8/IUONbMyB+0BDWqeSCwa2vh9p+FIFUgCKHqubTO/QYH4YPTREcdMxF3GM/UHSaeDxduEDdsMl9zlGdf7xGFInVy8jWTII1MfapQax3DMHUt9Gh2GJRrjxTeoo5VFrdOyPlXU+0hdWwD1ny6JD7Y4+Bb0iHlLPucod3IiqBrEyHxuc382WlDtcVaWT+qhP5S7vWgY5a5N/sLIwaOP2oYLEE5PjtEgj4N9e3bKDwVoIFQ+Ulfm3RPSPnl3DrXLTT1GNgRDQRxhvWDnULU+GQrcp+wgghBw2ZrNHqM9cEbRiMUeR8I2+xAAkYQJfIG09fdvHGL0nrVSNbKavi4DyNGEw8l/N3bUAVrAN/otfVbDW16qUnX/n9a8sV5XkRZ6kD7JGjAEIzYdS+8WlJ7tFZe1MskGDaXnhZyKBgVAE/I+lVS9j4+tDo+Ph9wzWJLkkTrgpoR0VLHKd1T93313HiHKI5y0iumxh7icgdG4EfdenBpZsX/YFF4tagTAHXKs3m+OYjHukW481x4dixDKPz506D1wembiWSXz+DuoiRu3rHI7Zzp2FLhJCGoLT1tDwS5m9qzjfaC00Noc/om+HPk1aQFxHUUxpbNR/kigLE8CIHXOnQc8mnTe3MMagOadixkF3KO5EIQqo1Oeip+ax5wXo1WjrK2qXkk3Y6d9XJxN7Wiyqi9YD0i9RiCNbLnej0fhxakwaXHulU+q3FS2UFw8PpoQh414J5FPa5PvVKrwzAMBw1eK1FIVHznuzzetM0etvoOn9ymdz+21ddmrP/wmGqrE8aJZ9kUFYVTHRkFX7N0zaWvOAG5P4QgCSUYd2VW8tZHo24HdPkK+uDw3/4DbXPVHE+O4ZHWgG5qtGNxW/qpgchpxJAjjhwSLudt4GYTGDgb/7tGFZXyUlEerJUcZZ/8BcnpZMj3FbdJ5LMgRS1HYNeCWz+aWR5psfZ5xjhHs6fhcrPpgaunaiBO5Nqqda6zkDiuwbAo7bdDC/bxqOG6LkBDEkX0rAKimYtuXZghms2CHE5/afms5PPG5zqPYsrWtzsGsCfsMuXJAyrN+xl4McJHz8PgSZEiPt+/Hc7sxM+UGgBxIZqTRdRGD/QxH/8BxQfCKFAV9JqRCdfjWHuCv+28lHypxzUWn6Xaj58jA5MbIaRlBzujTLpFJ0KjKF8G46WG5GeyrjQyPi/6gl+3s0EDjnwX8zf+oiWYKhbshuGn5EkyuwToaw0LbWmV+L9qRdbfQ5XSaMzaehks0Xh1hM3TKvQ+qOS5bgESTyMp3sAICe95NDCrIVFHoP8QyX2l9AzmlbDJyn/cvXW7N7ccPh5enYdvNZ3auE+lDpECOz8fwHp4ErX4YkbFAYKbiF4TGmusrDuYPQKSRroXOLW2nAGeQvDJYwROY5qHZKNIB/68UlBI1rLNN19p4rYdTunZqUvtJ+jb9lipn3PZXeD7f+H68/Yv7XiMFZtoKqC+942FaFlcezUkNVJWeeJ/ciOJau7DMCSE8EwkwQxeYkz7SSoAtAedSjzOXSSoBcaoSJm8OVAmpPxMja5JhQacCo/XjHCvbVfRZR/JLsA4G0jdPGj13PvbtJFZLOy6qv+FTy+vBEQ70+IJrVSehGtc+c7O2aMqPjrN772PGXKvy9AN+9+V44BWxgKR3WjAo7nxb6YJKDjVSZIb3ma1wiIubT4iyHevMuJs8ktQW8J1Wm52FZbCWXdnJGFy3Ft1o9cLLptJzz0GzbnsaNZ1bT27HOLtNQ1BlH9JpfkGxVsoBK8DEX7q6zHJz93Cjbpwr+/o2aO5/2SeoCaL843KWHJS5c0FQGiAn2gVH+N/On6hzgoRMtDJzD8v/aMIpdJLJh6XTyWPZlt1/TOiD7lDR2TliUH4xRQcbhuyuf/JomGLU8sNukmwFxo8oVfMLAgZb47ODzfs9o32J2PVe6scpBdnqRLAxxUV/Rv98ItZs2+D423RdN+TkVCbfW5ZlhUO4nlrMRwrXAy7K1BkR99uD9JAowTHu4bl3/AnGLYruPCw2MkF05ZkAtitRJX17H4z/zzcLs2X5L09p3E4LXcxkEnOh2NhEG8Mv6/OPP2E9hhiOt3mkLlGD+BNwZyPMnQ3n8qi/Y1l+ZUyUwYr/M566KGFiWqK9ZgEd2zVEU6crUqNIqjMXfVteK4tdRkyH7Sm7daLP7HPajv1vqIOU7hTo2AGK4IYAf9bsAk/UxDsCIwPqVQ+jrj70UeaYdJK7AZdR/xdaOohEjOwJjTgcUfLdUQL/c+sTU6FF7+UCvn806BUHEn1x77/nifTi3F6zfjdTjcOv90W2o2edrJTCrJC0So5rZkO66nrP9CabuwHo3yRdPI9buFWegmfQ6jaUIX8dT7sr4POFgIUDzzsdA5hfdoJL4p0HZ0nEpp+0eoLfgA60IjuHjjXibdYHaltoFlHnC6rNtQN3RY2lh6vpMNbKVrpXqUZMbVKuEEtr9xFolxw0LocEQr9AwPQETudS2tlQMja3OdRTn31f1d4Dbex2DYyVY6VTM9gRa63ThSzKlmnHHGA3W6IVdCLdv+a5mNqubI8VaPUU8eA3EBGLD+MFyG058zPI7hOIJBUY5Qu2nM/Q5ABDvBeoHBsyrXjIR+4YpsKWDsK9CkBKCUtZ5TDDYyHQU449WeQsFh9dyL3IAJRQ6j4Px7+WWpPsUMSInGc7cLfHgiPQeJPUMRhAgEU8TlAF2vdnrMvgRQ+59PA8o9bFcZ8gitP2iy3V1aXHNbQQ+20H2QsxpBHfhK36bMPr+DOTx/10v8Qy8mSephPDWFZkFA4b7bPU1LqpVSOMI9Hk2UBOJWiwBxn97Zajie27w+RVZKQHZeiq7p+8lvP5bGct9LOgjOPgwZBFp+yaZ/YSzxIl8R6uGpKbkvWIDclfBQ9cnlny2LoT4TvjXg57uv2/+pwkiJ1wOi/McK+v93Rd80JhZ2jv0jAuouELplzi58Y92Ruk8M2Zj3J7W9cP8wzhHHxH4cKG3KI7MFV5dV9EvImM+OXNBioJgaLWDWtL4/f/C/iDS7T7VJsz4J+Bdwp6+Hi7wI0LAMxzIXoF25Njg6vw1aqpx+B7Jidaz9OzhA7d7bsQYkBwBYo99TEIc2/XVX8t3JHH/8v9tX3WnPBkd3T0RC8zz59xn1CAi2CkgEWRVsvnpqDeULbJ2Y37oa7wIbHsGOdbVhyuL4b1ygbpYb24r/FMctM8Hg2aEEjbdYqxGltLkoCLGrpLsZdHesBEdgzhOQOD/iJj8xMKAzcn7NQLyw/Pmkg8O+z5bQakZNrMueS8D6LgBCg8LM5eeDZxNRX0d2h511OzSsNGvku7/cUymehKx3fLuK+XOpu7JQwZxI6yPc4ExzFbjp/PoVSkBmDRZOfYGtIgJIWfSm23F8TSMBDTERAnjgouF1Y/Aa02ovv4M5d5rdWm8tnuOLgOa4aB0vLrvI09IpiN76hy1IJ+/NFA7FUFPvisqvAmly5vywtNzlVM5Qj0xTlG/EBllq82kFy9NfXYjuzOzfEcqvM3WujYgWYerht2VA8Xm4fUkkiFwDcoVsN+xzfnw/7VsoaEPeYdDsiDLfDgmOa/6wAK0fYLq1kHguOphc93CectywZqeK/zBDlc0GSq/UnLfMCJOxRTI4T7oUoatMMt+SgNdQ8JcqlXeKrDZ75XmMplAi5Kvdrdbkgm4zhEcey5Ow1aYXp+CGcOG6pN/TaZVH6MBkHklq1Nlw+lAVzLCpqQvFbmhODL6vFxh38VhS1gzm0+GxQf3hCa6waeRL1olO6IcqdyvRRxvjNEUDQVShk86vcfomExsxNFixoKx+NxwA/Lti7VivDeeQmG2qTDkwcFd5cX6ns+5DQt5T/bw+R/PMZV9CUlctP6sRmfV4L0OSIimZagJu/3QGwCc5Yoojc+jfq0ooTqFovg/z85SkwcVkWcXnJd4zg64zUMyA1ma9caWK5J0GOpCXZA4VsCZQENnEvMxmzuZWzndPRsmG8PJUDUXImyA6HRmCKKop/I6P3heCgoilXuolwmFGhTL3Ib1NWHHfy2g5Yz52MQygFcxZj1z2dPJmMLmTg0OebQ5ALImD5c2iU8XjYjD14Ws+Z6oWmp8dpUd0TU3n9apYR7W6Dd2auwo7YBRMRUJz6XJL3VzUDmbanXjJIcACYWEZ+75o0PFWTpJ21QkoJpIE3qvgsqQJU12/o1zBiJRchgSqAeo1ess4GpmG+C3c5bT2Il/F4u9X2FPqV88JM/i571Da5pXGnK5aHBZxp+Vq09YVbqu1Kt9/I1ijtk6jyqePlFw7JU2OAkTxSXzUcUL4qKBj95/2wKqglwpGMdapqp5t27Y7c7T2epgSYpmNI/gTRXq6FgQTNprIPLnvJKWjJY6i+gQwQr+/54iLMU/ritpGgymhTvHGa9jDqtim3KZmD6sTtpJcjde9EpSUEXzxVAWSeavOZgoHEarVgymOdYlayiagdhMT/w3ZOjNID2QipazNUdzVZZRMS4SUNCQsJ5fDutvdCogOTBMiEMCX0jMxvmphNqLg/wNUJVGlbn7mF9DGbNNEKJCTVbJ0EquJaBY5LyZrQ+PEk4J+C4V5iEL5MxAWg4iTEHfabtlGK/F91y+gxa6Llj3NiAiCVX99C7Fl7ozrq6HdvAOKiqzyKYFlymcqZewLVq2iLO4gtPF55UHb/dTNMkdQKtlT31Jj+7XFw+8PYf2isBw8Zd07GVVPlKca+gzcY5zMrAfQVtJdH7k1fviVhb++Ve0wREkN98VsVLv2DU++o2qTwRmZpsX1lWD6iKrYlmX2k5lPHvg7qz9vMr20UXUXp3FPmKMUC1gsUBj7q+WZIf1j8SuU8fcT7l8KUWbfs1hzgHrIkbJB4wGz9ruE/imUcZDC2h0sAvrpDBIDmhcZ5CXNJvbaHjNtftzdQVqe7gAxJ2MEpm7FGmlOSvFMsD5gylcEfB6HmvtZOa4w+q5DITPaj3UBvyDgqmX7apnOX+6goiJUo/Z6scChkp8P/Qp0PNWRwP/vH2JaneJATYOZ61/SElwXN3/6iOufwpZ6PuiihSRVwP3mEGfE6pZITS9PNJRMVNf0OcPBHJdyo/pfKFkn19llp9JjGZM7zKavyVAgZnM9mRHayIzwvSejSZcg1bEXmXgJUU1KynMA9AWi8vNdnBWtG2dOM2hYUFc76NTSUsFLJ/DFqHXw/EzU1rmPbIXVZNbBwkE2O+SdEauLi0zu2sF1pkYHFHRP4jvSoEw6aiESLX3qCoADTQTK++cLVeLUCnx+gKk59u8dFSiMd2iio8lqej9Vb1acVTXmYW1BYMb4PjRyoW51GUEZKGu1gKBbA7xPh+p6Y17e/upQPRM7b36g1wPBCyJBKrNfbMiX2y0V8hWnIofAdypECZp7yza5nYkhJH5+e+j+r4NYzToNxuf4tNFOWQjvOWmPfrg1pwvgW4L+WQe7Njq+dt7QyjSNIfXbPGz7nMeWt6qLcvrOd8hmbs5MBGZoEGhr9885ra88Sp408gP/Ow/PdIi/+0dLOT5gx1l6IJMpa4H+AcKJIEgx0sOinIwzXbTxeQdWR9VMi0PZ6RID8yLOaYYAUOBAVhZaN1c9XqIEJWf4q5AqpIqEWj+AMEcfp3hGrU8/KLsiKwTCUFc3TfGAjsGnwX5kL+xYW7tXXpnXgreXYewzwZUyiJgmDtPcMovoJuXdUnRUGUvgPWIyLmmdYGTCHa8IyPHsej5KJzIHqYkNape+N7bwONymW+/sAIF9RZVzsRrttr1RQxbFJuUrjT7Qn0c9lpJeyLt5rE5awUoD66+y79Hh+JZusDEZxjHBfaMXgL2ZTBupEecTwiBHt79XZ09SOyKo+gBStafKIaZsQuM/f1b92iX4F2a564P6WUK4cedmoAMrVCIW7XdKqznil09iPup+xw+WArq4kxAL3e1UzWkV4pa281EzK4GUmeXrH66Rn/YvpIpyUKsz8wVDT5IvOxrwkprAFWAm0wPfLXWXj/D5WMFD6wYy010+voXmycr1p0J2aHJR2TYCIvGF+vemjFGPq9+AvYkYBCxplfzmpk81hOVr8PrezEFbY40ta7IySycLZeOtOHfYfHDgvEv3ISmxwxLElBQgRN9ntYCE8aWdOJrEt7mBdrkbTedKk4zrhPhC+CfZZTDI+0jRVP0jqWPl8IstMCqsqFvDx5tLpwtblmLCJuCVeRjaAtE0Sj3U6jNJFuP43iM0ji+ONDRhCcpw/gJDkT47qFd4MQomGFYTtDFbEyFUxDRdJD544Q3gMeSd1cuGuFNCgN2yTYkv0IAHr3i2fyxoP50ZflnMAEsqyMCKnbJHyNPwBybtgI1i0viVvx8yNKhrn3vq+FlP1fpDaM0RuGmcoH8K3XQ65A72oh39y5rtP9MguBMiJTLtbz4r0eV0uW5D1HJi44kyiCN1DfKf839S+UQ4oeZ9un07DL5KG1AhHj/NgNVZPqaN/Y5ijqk+QU/hhCzAgjqu5/dzbp/jzr6mUiLJK4R3TTL+G6poibhL6r084L09tHeVoX5du7OdiRJwOA+APUXlyVTRMhtc3cAOFTXMWF6ez+UHmfpb3epBtQV13B2JLTiBsabBam6kHLf/s22mHLZPlir7HMboYaVGVWpHxkfS8bSdMu+mcA1wSXKgVQD+YEblYxocybSM1IFjGUUHz9qw6jakZvYF3WaLSNqPtRzDPprXSEPd6Ye91cuofo/KkuEpNTegHVyWbMse+wPEv/pfj3w3t7gHDdufq3itLuCfK7ihHQkSq8rtC0X9nDD5NMJF7IYM2WSgquUUFbHRo04QQN2FNOAJlQW60Bwbozjh6i5RXxOXbiPSZ443btHNQRmAP/iPMdLrRl3peaU0NwU4ay8YyUGmzmXbX38cfC2/e+/i1xQQjdRIVv+pEKhd9j834Lx70FU5suBnIK+xnhoLvTygCPjvjztQ7z8Rt9xiA8SO5zQbnNVwm+DED+OJt5u3owHvEWPtD86akxTu5fiMjloPb19vPG7XqpTd9DeiQ1j2OEbtrMzRtPleYAiYaKqB6Wx+QLWXhNRmPyDY3Dc5lw2FUEDOnu6xae0EyZSZshslT02+SSNr0V0rZn8oMcmMnK4bkfTIl2VveJhGI82Qtf6aMz2og2/I0X/3xnr03xRXr/FMIb34f/yPnigmvkJLPaGs4CwHSnVdkpnKmXov+Qodz8poVoi2ldH20hHDcbg8w939N9cveoMUP5pKc2jP2LGNc1Yf/ahsmgE0B2G4XNxgdCJVTuLKGUXDf6nC9cUt+JCyq7uCNuCOUKVBe25MKEB3RLcvcy0KZ+En7y7P5sP18KaWT0/jYcgc7VtvaFt09RPzbEMCOAlk4mtMnVCZO9lqtlKgF6XugNUqYQdMhFbszpUlg2o4YctRfVyW+0+IlS3IypOo/ZdcSUfC7m32W3lJ+llRvc+I+T24jvizUafmpg+VL0BAYPy8cCaTzogYzTG+Nc5oFlwRuU9QBH+NdjnuYvnNK1OYFC4BD6kSDCQ+gLMpp26+i+B5Z85noB9gEpMDyTlYK6hIB6IBL56qNUHEnVyW+kGVmEA90NerCvkurU6rcOARZP23eBiSy1fkOL78wXAtjnSlVfZiwGOR8ldfBUFJkduPJ1DmDK6uhhpwBmX1tYtvolP4xRlyhgf24XUM+y7nSYIHTNL7e8HxFgOTc1z2XkAReDg/ki+gyf0zRPRD97P+kbPhbVgOHKZaSE7J1frFRuwDtLrmnOf4g8ipJAcy3jKmHJfvaHQkRtzByltKFDGh7J4+q9ZWZVL+v9WSDAdPyVhLay3xyKLp7RNHhGgI2BgezLD14GtSHcyiBjVtK18Y91zbhsm6m2G2tZgcf5lQX56mq6+upKTNJkivCF5BBFTLmXicx0YNYd+z3X+wz6vAjpW9IRn1lO63ZMtwunAE54HhUzst8y/pNXAlWIF3vwi32lomuxdk/rux5Ou/BjHiqSkY2KHAIQ0EJDTHevAdzuqA7/bE2Zf31b2oaG7Rd8nSdYloV6E4lb5vXC1uhBI2juYUXiMQGXgxbT/Jrcu4JjI2172n7cr7xolUYx6MHJHtQNiQ5f+qRf3GcS6XWW2xKQAhosJrMqUG62mDvKoMDrwSwzvtb1u0k/xaKx2eANElXCQWVcWHPQU/an5mdnfNFyVYG4RxjY64RsPkrbXAWqfT2EEAjWnr6Jg/D4H6eZsQX66AK22mdFlR2/DdAplnpZUrzYESI6H/sZvKNxQOB71gKIdiezBMXAk/Cjpky7Mi1abc1le/ZXcjOQcRq3ckziTyrWRJpIzuVRpuV+Rr8sqcm4FlX1NDyHYYer91uICAISRr7j6E/kywJVsoBHvTH0I3ymTYgKeqxysL2yngN8GopiuWnPu5taYibzrgpqsFwlLVG89o6U+EzD7MqcIf4HLvvKwmpAugoYUx/VKjN2siProwg0PYeWXRossczWmKvY0Oq8EcWbiP4sBthLqh2lhAAngSRjBxtzWwx19wFTZTg1ZKhs9ke/cjBXlqt6Sen2HAeh3QE+wkvR6Go8QrR8iRY76F+m0bYpexKfxAsdUjj4dYodiL9ROsaC+/+/tyMsZC+KpyzO2z5te+8sudLPAn9JQERJ8Wls5VkssoSf/l4XWZKC4AxcO66YvGNIugysFbTBg4eOupnbVM1rXWmRwtxy+mQtPp0lMuzxlHRiC7RJuE2CpbPDKlOQ34yuSSgxP/1HKPNznZRUDHh808qvk2rdf9pHJj6aUuyEJdKq+xG4ewjSwEeJAskcrMfbqIRoA61evjNSA9XOdQGi+W8ZtIQba58Q7Ajvqiv5UkBwUZOcKjbKgdD0n8ftglyt+5ixY6yE99VOJuNqEWMvtdyfX0000zfNhbACBqyJCPfqDW96dfezsJVxf6ZtNseigLLD0vfXM8qrR4hhYuHIeFc3IbL64eLGdME7qFt0P1h1zA1rY+N/9Y1TakUg6H/SRlwpKDwRrju8B1mYC4MkgfmmziRiUXnjZBuyzJGN5Ee3ZKmD7P5A3ebEFpTkjOuEUjEAqaunXsmc/sZQfCLE7mhpdTKqCS93cIetElmYRqw2I1jIsxyIMRh55rfUqKPi0hm0W1hPt7jwQ191Z99J6/vq7oaJHDOku4m4qWlC8EYWoyXFtdEhdOziMVZ5nO9qhLJZJ54XakXlqW2Vhvzr9Alm8qq8KqjzrqiRQDURXdxShB6X0fK/x8W7qht8H1JcCRbvcHxEgGT93NjVrcMAyGnm/24ZOaSXqcvek58lPu/LdlwEHD4suXnvS+OZHzfekQZjDVpZ3Pb7V9SY8elPpSXDVyT1pYShCmWvkpY1DX2NGF9nhef8en0UaWvpWvxSdqOA5BpzgjMBxXnk7qeEh+TJymgKBPW0ogjAOQ8zG9Pr7oKQVoyb3s2yBW6Iuf2XC8ZvkRcFBSKVEnjxwQ9srWkviaVsDK60htMD4D12zUD3W3U7mjFC2BytkkDDYLOeyOPRUzzc3L9+whoCUQ/2QDgLlEjS+2SXMpWUpsFfVYHgxHtOjG0xXncRgxhzZ0lr0rGPajQAUAX9wIg3j+Y+rkhDqo9TUJt8Spt6hwaJRiXNyx7I5BR14L41eFgtJzFYMzBr/o9aN6wEqbSoJ33q9HO9v4h2faUSG5Fck0VbDVUDvkAoqFeM8ENiWwxOioKVrUU+5MyBXgpi5Jg3++wAO/pUWSJXd/3JpDQ5lG9KiG4e4gDq2Xb3rmjsC1UTlm9DbDKBhlQ4yh0Gp0PAHYiymWz7YteYfHD02sIOvbbRi8DyW6hNuWD9waAY+x/sKyZVnofqLym2bL6a9yDCZ8ik5Aawn3Ztv3xswUJTkYs9/dZkNwb92gP18F8jKOrMelnfzc8rWqJW+5YkJdTGN4T9FAytNxstXdi859ZQEebmsXmsPKLIYn4XO6++JWG4Nsu2qgik1Z8M54Lyis70rNCkyRlIIaHOFivv3D09RIGA737DIQG/WBBKy9+mHC1tWnmZBcPhaY2KbpEMCYGkDrUAi7A0myd+yntkCtZBhZhIwiH3f+I5CxWSo4AD4fVWlCxwuw+IxN9ok7jWLyyFI88crzEEKJxdpVdOvzUaPcK7FpyUVG2VSHoV2TEHM6f38vWMcEhi/u1WiX3rbAIXGkQAJNhhudZAcZP90kP9XoBXg9uuw7DFOZBSPNmy18p4PvUHpj+lMvhmzDm6iYwO0Ux8UExdhlZxk5+JB59wCGEr9m7RHC05IQU3h6sbkPmhzryfPF3ox+P3XI2V0F4ihQohMwCdmH9M6Zlt0PVDTHS/2qumjwqLCTrjN6Dq7KyxVYwVI5i0mX1IHWT0yON6viNYAEOlq8LjVNjYmahEcKi4Uz6oYGdlzVrLiRRjja5uQNS0cZnnZ37iVVmkFKJCKsCooI9SkZGkz+SsDRboaABbY0vzMJXEEirr4hQen9ypAMyTsjl/6HigoVitE/FLf/CPbsNCaFNafpraXL5B7RtHQ2gnLIO5mvxynIKYzT4PRyNv4f3CRaHdAGXul948fuEj7KGLqs+zV2JFM+HAYzSUDYCxCP1eg28NyJhXcMt4rOvNufgpgTHyDA2rdOTs1BjTzJs+v555VZvuQCZQgZC1fzyAj4XK2DQZ4EITxJ+xy7PPZQnCiS58Oy0MxutE7yyPBWw48zC/6DqWNgMZOvzcaSt4IKiEXVrvptCMObvvNChM2mfbbX+zccoIPvMxvj/h/4fas2ZTnVZG/mJn1kedn/j+KkpjHV5c33OlLy3vsmMe77uTiNtybSI0Z+DxsFIqOi2m8f188QKRItZhQN1JyMpwsiw22OOtNlPPU6hGNCD/3iCwUh4qchufGYemLUhBzXDgLUutwFEWCgeRFmD5BJ65pafiozOq8dqCq64lD6Pk0YHVoYbFmNcrqut5jFbo76VColJ7I8pcreTY96tTs5r5E2zZu13HgPlBuppcumK1t54KWaftI82dSgKD2wl2tu/7gTiIsA98a02fsWSjE2ul02C0rh7yZPRE/SrYEg0E1DuTZPRB0AMNxl7v5HM7DkQYkAc4CPYChOKfZ7wfyc/DsOC4qH6IZAqsoW2boKTavd8U3ZHYKhIRPQxP8/X8/65MRE0zMmRhqg0Ta6dMia7YCWoT1R5g2oSDYOI2sFiNAMOnBYbTBHWMbnEHsJcKufjnX85wlxGzopZHJLSVTqvEun5Xp08XUw2mRZI8KfXIGcOwdOWiVUlbifD6aBOaSlIM12hx9kYf4RQg85XvCN+KDhyf90d4bIB2nrIK1GrWDYzBrsMBifNCiSzND1igqiiZzhmzYiOBM2yJeHf/xBwTQhDJCLuxLCoc2Ik3wZoMJJXAlyaXVcCeksxNhlIx38E4xsAivPk+jHRTwwSVU0k7g8/4fY9wOPAjRFWTHFDexW+dqd6mDMiD4AIQfprHHqTC4BEEJ/N55+8Ze4sfx5BpqdYQWp5BwWczMvHRtpC3xiji9yPHegtubnOuQmcJFmdyEOMwXLZBavKXsaBe5jJ+CRjFlR21OuKrhernaCXq4uqDJPpDg0gUPeKJGGSctnSz4zZ0/Qb3UJkjPM0jTb16llmbdKZLa9hKgqe5gY668NgCZw+0M4TPr6J2/DdaMvvwQDH2194hzkArk1VhErCqXDYn/brSXZflrm3wrAyYCEnFyQA3Xftrp/U3NPp89Refh/CRT9eL4zvavxp79OA3Xl3SML4qbW+7hde6ORBlaNeDc5uqSzOz/yyLEtzygVrCAGND2mDln2b4pdJ/tEi2PsSM2g40ry4nmdqPd2U7OM5CS8a9/k3uABfjogA8QwtrgeP70LkLMIO0y90tOG6Q4TLWiAMb149Q1g5vObNHyhNPt4bqCVpQ4Q/L2/Z+PLlxk4q3OlA7ztU8Q0DbOBoIq8/hSbzmWvl6qKXDnrGFYtrBj6U/YBPcBP/3c1JtGD/hGqRCV/MMH/Oa6wXSyqi8+f2SkYC2O/zC/VE5IVeFMZE+YsMJhBRf8Qr4VzxsOWFl4B+EQpttrNlxhOZ6CFhKJkf6ZwEHEA5fD72mGxvWstBICvCnyVvffLpGVf5sI490Oqwl0+FOYsweZ5vVKINYbyIIS/RcaZkYbgeVfnR/pVqbGVjmCWPG1XG+z9YanV7CwSg37mgvY+vOuDpssCsdAWwzUvLP+rhN9h6VEXf46jpRfe8gDQK1LSwqpCZHZeYtghb2hURIKNgKMcOWo2sD2DO8pfmeogJkdAWHk1rvqx9qwD+VRMLjZ4TYnloXZM8MePsnrwD+cVXhol4EFghULzZp1piFyXpbCh4vq+0Zm/Xqdgl3QESre2W60ueo63VgCnwyNF7ZMZOisbbYKN3qimbKtj0DeIdti1h7DxXYjgddTRU/3Cdu75RY0tm68jsL2NgfcaD33Obm6lcykWhy0rR16O412axk8O/cwYVEVVWrk0u2lks+8kF/vJZdWf3t/CBXgxA+Eql0+3zkg+LQBjo1CSKhbWxMnjYpo4q1AqempuVlVti/r3mqeKNbuBjoLDHsNnsgk8+RFgAw03HszEpnXUMjK0mVYJRaABx7OgOMnIJXHZSTSQKC3Wk67WYRYB2+d4yz11mX/FANnri/LpisMKX0vYOJvCrY2IUgQr5D/VzNTFbTKeRbAmPeH0Vh4kGhXDQtqKpUieVT/OVeA5I3R6NCLRigNjfhWUzx+nsVfsT/tb/lZBl4PXfpofdKeI3xB2MAoOesik/Avp3GXIJn9ohrwJHdLtmS/CQvADPhHoL+DAE1HnkTB5EFCWzzzbx7qu25ZOyisZFIpAyEpmkpeFknwRe2L90Tu7s+aeQdSSYeEbG7QgRghWoNjqq2G6uroZ/RuyOFn7RIxjRCd+jU8k3jByoxp1VnLYqWH/eiScVFWU4xxBbaVRX8ESPK95lM/XfEKnlGHvoqlCQEJxu3u7oSEBL4J6xBPNi5ToWkPcbAwDK5lzMBDPe1h5PmulSlD82XhE4QyTzwWW7suYW+Hvny9PzQtYhfjwr+B9fokR2TlsyevIeTVcH6qvGnCur+r2jAG6cqA/OgH1N/mPykKUq1ZaP7S+EC8gxOQrpYA0G6XC20HZUbQJbM2fjA9rbyBMIQx2TIrOf0q0Gc8GD41CR8tn0lST0llr9l237w3/UBVJaNXonTkCqCHUel/WQxtOs+NDOnVdx7+i3aEIw3rLBJbgt0aykFtTwubqMnYejxw099gRLY2sBsFl/bz9l4K3ec9js3LwurYJeWYWw+L6fRxucsh4L6sr65doabq5DgaICKQ97qqDy1JTG6ffS76gS55wSZ+Ojqz6IyLd+MSSLLhX7fr4ZseM67uQLYVQ+JdDnkffWJUCJYJSmy7OP3qPv50F2JK4RJE8C7e/h6osN+fDalc/Uzk57izgQS
        - #1:
          - type: tool-result
          - toolCallId: mMIAjXo5lT3K3NbW
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: HcO20re57C3emkll
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.