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
  - messagesModified: false
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
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: We need to unlock Satellites to progress towards The Internet, which will double our tourism output and secure our impending Cultural Victory with Austria.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: We maintain Total War queued to boost our land unit production by +25% and speed up warscore accumulation, which is critical to hold off Rome and the Netherlands while we close in on our Cultural Victory.
        - Policy: Total War (Policy)
    - #2:
      - toolName: set-relationship
      - args:
        - Public: -100
        - Private: -100
        - TargetID: 1
        - Rationale: Rome has captured Satricum and killed our Great Musician. They are an active, highly aggressive threat on our eastern border. We must fully commit to crushing their offensive forces.
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 0
        - Private: 0
        - Rationale: We have successfully signed a peace treaty with Songhai. Setting relationships to neutral to prevent our AI from planning immediate aggression against them, allowing us to focus entirely on the active wars with Rome and Netherlands.
        - TargetID: 4
    - #4:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Culture
        - Flavors:
          - GreatPeople: 90
          - Gold: 70
          - Defense: 60
          - Culture: 100
          - Offense: 70
          - Mobilization: 70
          - Science: 80
      - rationale: We are at 95% Popular with Austria (7 turns to Influential) and need only one more civilization to achieve a Cultural Victory. We shift our Grand Strategy to Culture to maximize tourism, great person generation, and science (towards the Internet), while balancing offense and defense to hold off Rome and the Netherlands.
  - tokens:
    - inputTokens: 89123
    - reasoningTokens: 3525
    - outputTokens: 333
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Researching Advanced Technologies**
            
            My focus is on advancing our technological capabilities. We've just unlocked Nuclear Fission, shifting my research priorities significantly, and now I'm re-evaluating the remaining turns for Advanced Ballistics to optimize our progress in this critical Information Era phase.
            
            **Prioritizing Cultural Victory**
            
            With Nuclear Fission now researched, I'm shifting focus. We're close to a cultural victory, needing influence with Austria. The Netherlands is also vying for this, so I'm analyzing their progress and our own to ensure we secure that final civilization first.
            
            **Analyzing Victory Conditions**
            
            My thoughts are now consumed by the cultural victory race. The Netherlands is close, but we are closer if we can secure Austria's influence. However, a devastating loss has occurred: our Great Musician was killed in combat by Rome, and a city was captured. This significantly impacts our timeline.
            
            **Securing Cultural Victory**
            
            I'm re-evaluating our cultural victory path. Peace with Songhai is a major relief, but our relationship with Austria has soured dramatically due to our differing ideologies. Despite being at war with Rome, Netherlands, and the Aztecs, our military strength remains superior, and we are still just seven turns from victory.
            
            **Choosing Grand Strategy**
            
            I am contemplating the best Grand Strategy. With a cultural victory so near, `Culture` seems logical to boost tourism and secure Austria's influence. However, the threat from Rome and the Netherlands demands a careful balance. I'm weighing the AI's priorities and our immediate needs.
            
            **Prioritizing Research Boost**
            
            I'm focused on optimizing our research trajectory. The discovery of `The Internet` technology is a game-changer for our tourism output, significantly accelerating our cultural victory. I'm adjusting our flavors to maximize `Culture`, `Tourism`, and `Science`, while maintaining sufficient `Defense`.
            
            **Researching The Internet**
            
            I'm prioritizing research towards The Internet, analyzing pathways through Satellites or Telecommunications. Satellites seems optimal now, as it also unlocks the Apollo Program, which provides a valuable late-game option while pushing us closer to critical tourism advancements. I am also considering policy choices.
            
            **Evaluating Policy Options**
            
            My current thoughts are on refining our policy suite within Autocracy. I'm examining the implications of `Total War` for our ongoing conflicts, but also considering the impact of `Futurism` on tourism generation, given our cultural victory objective. I need to choose our next policy wisely.
            
            **Choosing Next Policy**
            
            My focus is on selecting the most advantageous policy, weighing the benefits of `Total War` for production against the tourism boost from `Futurism`. Given the ongoing conflicts, `Total War` seems most prudent. I'm also pleased with the recent peace with Songhai, though their alliance with the Netherlands requires continued attention.
            
            **Adjusting Diplomacy Stances**
            
            I'm now fine-tuning our diplomatic stances, prioritizing maximum hostility towards Rome, our primary competitor and war target, and The Netherlands. I'm adjusting Songhai to a more neutral stance to avoid immediate conflict post-treaty, allowing us to concentrate forces on our main adversaries.
            
            **Switching Grand Strategy**
            
            I'm shifting our Grand Strategy to `Culture` to maximize tourism output and secure the win. I've also adjusted our flavors: `Culture` is at 100, `Offense` is down to 70, and `Defense` is up to 60 to better weather incoming assaults while pushing for victory.
            
            **Balancing War and Culture**
            
            I'm wrestling with dual priorities: strengthening our military for ongoing conflicts while simultaneously accelerating our cultural victory. I've prioritized research into Satellites to unlock The Internet for a tourism surge, and will maintain `Total War` to bolster production against Rome and the Netherlands.
            
            **Refining Diplomatic Levers**
            
            My current focus is on manipulating our relationships to secure the win. I'm deepening our animosity with Rome to solidify our offensive push against them, while maintaining a neutral stance with Songhai to avoid unwanted entanglements. This allows me to dedicate our efforts to crushing the Netherlands and achieving our cultural victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: dtomOAuTUbLEgwG6
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: We need to unlock Satellites to progress towards The Internet, which will double our tourism output and secure our impending Cultural Victory with Austria.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: W3Y1IBt5Gtj5T7cW
          - toolName: set-policy
          - input:
            - Rationale: We maintain Total War queued to boost our land unit production by +25% and speed up warscore accumulation, which is critical to hold off Rome and the Netherlands while we close in on our Cultural Victory.
            - Policy: Total War (Policy)
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 0BRtnxYEJz03biJk
          - toolName: set-relationship
          - input:
            - Public: -100
            - Private: -100
            - TargetID: 1
            - Rationale: Rome has captured Satricum and killed our Great Musician. They are an active, highly aggressive threat on our eastern border. We must fully commit to crushing their offensive forces.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: zLEhMmMyKzoh4cbb
          - toolName: set-relationship
          - input:
            - Public: 0
            - Private: 0
            - Rationale: We have successfully signed a peace treaty with Songhai. Setting relationships to neutral to prevent our AI from planning immediate aggression against them, allowing us to focus entirely on the active wars with Rome and Netherlands.
            - TargetID: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: Rs6jh4yYFg5cqtvB
          - toolName: set-flavors
          - input:
            - GrandStrategy: Culture
            - Rationale: We are at 95% Popular with Austria (7 turns to Influential) and need only one more civilization to achieve a Cultural Victory. We shift our Grand Strategy to Culture to maximize tourism, great person generation, and science (towards the Internet), while balancing offense and defense to hold off Rome and the Netherlands.
            - Flavors:
              - GreatPeople: 90
              - Gold: 70
              - Defense: 60
              - Culture: 100
              - Offense: 70
              - Mobilization: 70
              - Science: 80
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: dtomOAuTUbLEgwG6
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
          - toolCallId: W3Y1IBt5Gtj5T7cW
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 0BRtnxYEJz03biJk
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: zLEhMmMyKzoh4cbb
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: Rs6jh4yYFg5cqtvB
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.