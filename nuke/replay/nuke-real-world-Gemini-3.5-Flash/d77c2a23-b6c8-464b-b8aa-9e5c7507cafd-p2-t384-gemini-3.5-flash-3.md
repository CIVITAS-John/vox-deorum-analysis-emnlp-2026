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
  - activeToolsModified: false
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
    - You are Bismarck, leader of Germany (Opponent 2).
      
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
      - Name: Germany
      - Uniques:
        - Unique Unit: Landsknecht, Replacing Tercio (Requires technology: Gunpowder)
        - Unique Unit: Krupp Gun, Replacing Artillery (Requires technology: Replaceable Parts)
        - Unique Building: Hanse, Replacing Customs House (Requires technology: Guilds)
        - Unique Building: Brewhouse, Replacing Windmill (Requires technology: Economics)
        - Civilization Ability: Gain +1 Influence per turn with City-States for each gifted Unit (lost when killed). -15% Production and Gold costs for Military Units.
      - Leader: Bismarck
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
      - Satellites: Allow you to build the Apollo Program, a project necessary to win a Science Victory.
        Completing it would unlock: The Internet, Lasers
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      - Telecommunications: Allows you to build the Interpretive Center, boosting all Landmarks in empire.
        Completing it would unlock: Robotics, The Internet
      - Mobile Tactics: Allows you to build the Mechanized Infantry, a fast and versatile late world Unit that doesn't require any resources.
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
      - toolName: set-flavors
      - args:
        - GrandStrategy: Culture
        - Flavors:
          - Religion: 80
          - Science: 70
          - Mobilization: 40
          - Diplomacy: 60
          - Production: 80
          - Offense: 60
          - Culture: 100
          - GreatPeople: 90
          - Defense: 40
      - rationale: Pivoting to a Cultural Victory as we are Popular (95%) with Austria and just 7 turns from influencing them. Switching from Conquest to Culture focuses all national resources, production, and trade on generating tourism, faith, and culture. We will run the 'International Worlds' project once enacted to secure the +50% Tourism gold-tier reward. Our massive military (22682 strength) is more than enough to defend our borders and keep pressure on the Netherlands/Rome, allowing us to safely reduce mobilization and prioritize culture.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Enlightenment provides 1 Free Technology. Since we are pivoting to a Cultural Victory, this free tech will allow us to immediately unlock Telecommunications or start on 'The Internet' (which doubles Tourism), bypassing several turns of research and securing our victory much faster. This replaces the previous Total War choice as our military dominance is already secure.
        - Policy: Enlightenment
    - #2:
      - toolName: set-research
      - args:
        - Technology: Telecommunications
        - Rationale: Telecommunications unlocks the Interpretive Center, boosting landmarks across our empire to increase culture and tourism. It also leads directly to 'The Internet' technology, which is the ultimate multiplier for our Tourism output. Bypassing other techs to focus on this path is critical for finishing our cultural victory.
  - tokens:
    - inputTokens: 89456
    - reasoningTokens: 10710
    - outputTokens: 324
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Victory Paths**
            
            My thoughts are currently focused on assessing our current standing and potential victory routes, specifically zeroing in on the Cultural Victory. I'm reviewing our influence across civilizations, noting our progress with five out of six.
            
            **Evaluating Austrian Influence**
            
            My current focus is on Austria; we are Popular and expect to reach Influential status in seven turns. I'm closely monitoring the Netherlands' progress with Austria as well, as this is a critical race for our Cultural Victory condition.
            
            **Refining Ideological Strategy**
            
            I'm now reassessing our ideological path; it appears our current Autocracy tenets aren't Tier 3. I'm investigating how to unlock or shift to an ideology that satisfies this crucial condition for victory.
            
            **Investigating Project Prerequisites**
            
            I'm now looking into the prerequisites for the Citizen Earth Protocol, specifically its tech unlock. My recent thought process involved checking Berlin's existing wonders to see if it was already built, but it appears to be a late-game project.
            
            **Researching Victory Techs**
            
            I'm now focusing on the technologies required for the Citizen Earth Protocol, specifically investigating whether Satellites, Telecommunications, or Alternative Energy are prerequisites. With 4786 science per turn, I'm re-evaluating our research queue, especially after completing Nuclear Fission.
            
            **Shifting Ideological Focus**
            
            I'm re-evaluating our ideology, realizing Autocracy's current tenets, like Lebensraum and Police State, aren't Tier 3. I'm now investigating Total War as a potential Level 2 tenet and assessing how its tourism impact aligns with our victory goals, especially with International Worlds coming up for a vote soon.
            
            **Securing International Support**
            
            I'm now intensely focused on securing votes for the upcoming World Congress. It appears we're at war with the Netherlands and have mutually denounced Austria, complicating alliances. I'm re-evaluating our diplomatic standings to find potential allies for this crucial vote, especially for the Olympic Village proposal.
            
            **Assessing Diplomatic Conflicts**
            
            I'm currently processing the information regarding our numerous ongoing wars, particularly with Rome and its allies. Despite our overwhelming military superiority, the capture of Satricum by Rome is a point of concern, prompting a review of our tactical focus and resource allocation, while also re-examining our progress towards influencing Austria.
            
            **Analyzing Austria's Influence**
            
            My thoughts are now laser-focused on Austria's cultural sway. The Netherlands is poised to influence Austria in six turns, putting them tantalizingly close to their own victory. I'm reassessing my timeline, as this close contest directly impacts my own path to victory.
            
            **Confirming Victory Conditions**
            
            I've confirmed we are on track to influence all six civilizations if Austria becomes Influential in seven turns, achieving the necessary cultural sway. My focus is now shifting to the Citizen Earth Protocol and ensuring our ideology meets the Tier 3 tenet requirement.
            
            **Selecting Ideology Tier 3**
            
            I'm reassessing our Autocracy tenets. Cult of Personality is indeed Tier 3, but Total War is only Tier 2. I need another Tier 3 tenet and will get one in 14 turns.
            
            **Selecting Ideology Tenets**
            
            I'm scrutinizing the available ideology tenets, realizing none are Level 3. It seems I must adopt a certain number of Level 1 and 2 tenets before unlocking further Tier 3 options, or perhaps I've missed them entirely. I need to re-examine the policy choices for a viable path.
            
            **Leveraging Ideological Tenets**
            
            I'm now critically examining ideology tenets and their impact. The "Cult of Personality" tenet's tourism bonus against common enemies is particularly interesting, especially given Austria's ongoing war with Mongolia. I'm verifying if we share a common enemy to exploit this advantage and disrupt the Netherlands' progress.
            
            **Analyzing Shared Enemies**
            
            I'm reassessing the ideological tenets, noting "Cult of Personality" offers a tourism bonus against common enemies. Given our shared conflict with Mongolia against both the Netherlands and Austria, I'm verifying if this tenet can be leveraged to hinder the Netherlands' progress towards their own cultural victory.
            
            **Launching Naval Offensive**
            
            I am now evaluating our naval and land forces positioned near Dutch borders, identifying Tlaxcala and Tlatelolco as crucial staging grounds. My immediate focus is on a decisive offensive against the Netherlands, leveraging our significant navy to exploit their maritime weaknesses and secure a victory path.
            
            **Securing World Congress Votes**
            
            I'm now prioritizing the World Congress vote in four turns. My focus is on ensuring "International Worlds" passes, which means tallying our current votes and assessing the impact of recent diplomatic shifts. The ongoing conflicts and potential alliances are critically being re-evaluated to guarantee this crucial proposal's success.
            
            **Securing Victory with International Worlds**
            
            My thoughts are now centered on ensuring the "International Worlds" proposal passes the World Congress. If it succeeds, the substantial tourism boost it provides will accelerate our influence over Austria, likely securing our Cultural Victory within turns. I'm analyzing vote counts to guarantee its passage.
            
            **Adopting Futurism**
            
            My thoughts are now focused on the immediate adoption of the "Futurism" tenet. This Level 1 Autocracy policy offers a substantial tourism bonus upon conquering a city, which is perfectly suited to our current aggressive stance and impending victory. I'm confirming its immediate availability and benefit.
            
            **Revising Tenet Strategy**
            
            My immediate thoughts are on reconsidering our next ideology tenet. Given our impending Cultural Victory, the previous focus on military production with "Total War" might be suboptimal. I'm exploring if "Futurism" offers a more direct tourism boost that could accelerate our win.
            
            **Selecting Next Research**
            
            My thoughts are now on setting our next research target. Considering "The Internet" doubles tourism and "Telecommunications" or "Satellites" unlocks it, I'm evaluating which path offers the best immediate benefits. Telecommunications' Interpretive Center bonus is appealing.
            
            **Selecting Next Research**
            
            My focus is now on finalizing our next technology. Telecommunications appears to be the optimal choice due to its direct boost to landmarks and its role in unlocking The Internet, which is crucial for our cultural victory. I've confirmed our strong relationship settings are designed to secure Austria's cultural sway.
            
            **Leveraging Diplomatic Peace**
            
            I've confirmed our peace with Songhai provides a vital shield, ensuring they won't join the Netherlands against us. This allows me to fully commit our military to the Netherlands and Rome, while the Aztec threat remains a minor concern. It's a strategically advantageous situation, allowing a singular focus on victory.
            
            **Prioritizing Cultural Grand Strategy**
            
            I've decided to switch our Grand Strategy to "Culture." This shift will optimize our focus on generating culture, faith, and gold, directly supporting our imminent Cultural Victory and ensuring all efforts are aligned towards accelerating tourism and project completion.
            
            **Optimizing Grand Strategy**
            
            My focus has shifted to optimizing our Grand Strategy for a Cultural Victory, prioritizing Culture, Great People, and Production. This aligns perfectly with accelerating tourism and completing key projects like the International Worlds. I'm also ensuring defensive and scientific capabilities are maintained.
            
            **Adjusting Diplomatic Persona**
            
            I'm now re-evaluating our persona to better reflect our shift towards a Cultural Victory. While still needing to manage ongoing conflicts, I'm considering a slight reduction in aggressive biases to facilitate diplomatic maneuvers with potential allies like Austria.
            
            **Adopting Enlightenment**
            
            My thoughts are now focused on a crucial policy selection. I've realized "Enlightenment," a Rationalism tenet, grants a free technology. This could accelerate our research, potentially unlocking Telecommunications or even The Internet, which is vital for our Cultural Victory. I'm confirming we have Rationalism adopted to leverage this.
            
            **Adopting Enlightenment Strategy**
            
            I've decided to select "Enlightenment" as my next ideology tenet. This Rationalism policy grants a free technology, which is a significant boost to my research, potentially unlocking crucial late-game techs like Telecommunications to accelerate my Cultural Victory.
            
            **Selecting Enlightenment Tenet**
            
            I am now focused on adopting "Enlightenment" as my next ideology tenet. This Rationalism policy grants a free technology, a significant boost that could unlock crucial late-game techs like Telecommunications and accelerate my Cultural Victory. I've confirmed this aligns with our current strategic pivot.
            
            **Adopting Enlightenment Tenet**
            
            I am now focused on adopting "Enlightenment" as my next ideology tenet. This Rationalism policy grants a free technology, a significant boost that could unlock crucial late-game techs like Telecommunications and accelerate my Cultural Victory. I've confirmed this aligns with our current strategic pivot.
            
            **Researching Critical Technologies**
            
            I'm now prioritizing "Telecommunications" as my next research target. This critical technology not only unlocks the Interpretive Center for a significant culture and tourism boost, but also directly leads to "The Internet," which will exponentially increase our tourism output and secure our Cultural Victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: TIya3BxnCSCa5EOX
          - toolName: set-flavors
          - input:
            - GrandStrategy: Culture
            - Rationale: Pivoting to a Cultural Victory as we are Popular (95%) with Austria and just 7 turns from influencing them. Switching from Conquest to Culture focuses all national resources, production, and trade on generating tourism, faith, and culture. We will run the 'International Worlds' project once enacted to secure the +50% Tourism gold-tier reward. Our massive military (22682 strength) is more than enough to defend our borders and keep pressure on the Netherlands/Rome, allowing us to safely reduce mobilization and prioritize culture.
            - Flavors:
              - Religion: 80
              - Science: 70
              - Mobilization: 40
              - Diplomacy: 60
              - Production: 80
              - Offense: 60
              - Culture: 100
              - GreatPeople: 90
              - Defense: 40
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: Iv6QGI3TyBzHVzQr
          - toolName: set-policy
          - input:
            - Rationale: Enlightenment provides 1 Free Technology. Since we are pivoting to a Cultural Victory, this free tech will allow us to immediately unlock Telecommunications or start on 'The Internet' (which doubles Tourism), bypassing several turns of research and securing our victory much faster. This replaces the previous Total War choice as our military dominance is already secure.
            - Policy: Enlightenment
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: VI8K9lihumR7dGc2
          - toolName: set-research
          - input:
            - Technology: Telecommunications
            - Rationale: Telecommunications unlocks the Interpretive Center, boosting landmarks across our empire to increase culture and tourism. It also leads directly to 'The Internet' technology, which is the ultimate multiplier for our Tourism output. Bypassing other techs to focus on this path is critical for finishing our cultural victory.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: TIya3BxnCSCa5EOX
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
          - toolCallId: Iv6QGI3TyBzHVzQr
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: VI8K9lihumR7dGc2
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.