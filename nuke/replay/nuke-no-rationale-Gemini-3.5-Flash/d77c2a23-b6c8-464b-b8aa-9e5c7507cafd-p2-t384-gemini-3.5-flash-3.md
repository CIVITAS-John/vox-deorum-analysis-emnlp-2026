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
      - toolName: set-persona
      - args:
        - Rationale: Pivoting from conquest to a peaceful Cultural Victory. We are lowering military risk-taking and hostility while maximizing friendliness and diplomatic balance to secure peace and prioritize building the Citizen Earth Protocol.
        - DenounceWillingness: 3
        - FriendlyBias: 8
        - VictoryCompetitiveness: 10
        - WarBias: 2
        - HostileBias: 2
        - Boldness: 4
        - Friendliness: 8
        - DiplomaticBalance: 10
        - WonderCompetitiveness: 10
        - Meanness: 2
    - #1:
      - toolName: set-relationship
      - args:
        - TargetID: 1
        - Rationale: Resetting diplomatic modifier with Rome to 0. We want to encourage our AI to accept peace with Rome so we can focus on our imminent Cultural Victory undisturbed.
        - Public: 0
        - Private: 0
    - #2:
      - toolName: set-relationship
      - args:
        - Private: 0
        - Rationale: Resetting diplomatic modifier with The Netherlands to 0 to facilitate peace negotiations, helping us pivot to our peaceful victory condition.
        - Public: 0
        - TargetID: 6
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 0
        - Rationale: Resetting relationship with Songhai to neutral/0 to stabilize our recent peace treaty.
        - Public: 0
        - TargetID: 4
    - #4:
      - toolName: set-research
      - args:
        - Technology: Telecommunications
        - Rationale: Telecommunications is the crucial cultural tech that boosts Landmarks (via Interpretive Center) and unlocks key late-game victory projects like Citizen Earth Protocol.
    - #5:
      - toolName: set-policy
      - args:
        - Policy: Futurism
        - Rationale: Adopting Futurism will directly boost our Tourism output, accelerating our cultural influence over Austria (our final target) and securing our victory.
    - #6:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Wonder: 100
          - Production: 100
          - Religion: 30
          - Mobilization: 40
          - Gold: 60
          - Offense: 50
          - Culture: 100
          - Espionage: 80
          - GreatPeople: 80
          - Defense: 60
          - Happiness: 60
          - Expansion: 0
          - Science: 100
        - GrandStrategy: Culture
      - rationale: We are transitioning our grand strategy to Culture as we are only 7 turns away from being Influential with our final opponent (Austria). We are maximizing Wonder, Science, Culture, and Production flavors to tech to Telecommunications and build the Citizen Earth Protocol immediately.
  - tokens:
    - inputTokens: 88332
    - reasoningTokens: 7468
    - outputTokens: 456
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Discovering Information Era**
            
            It seems I've just entered the Information Era, a bit later than anticipated given my focus on Nuclear Fission. This development requires a swift re-evaluation of my strategic trajectory.
            
            **Analyzing Victory Paths**
            
            My science output is substantial, enabling high-level strategic assessments. Germany currently leads in score, but I'm focusing on our progress towards various victory conditions. Cultural victory is a strong contender, with Germany having significant influence over multiple civilizations. Science victory is now unlocked in this era, requiring satellite deployment.
            
            **Clarifying Victory Conditions**
            
            I've confirmed our influence extends across all six civilizations. While close to a cultural victory, I'm now investigating the specifics for Vox Populi, particularly the requirements for the Citizen Earth Protocol wonder and its prerequisite technology.
            
            **Prioritizing Technologies**
            
            I'm re-evaluating my research path. The Citizen Earth Protocol seems tied to late-game technologies like Telecommunications or The Internet, rather than Robotics. Given our proximity to a cultural victory, I need to select the most advantageous technology next.
            
            **Evaluating Policy Options**
            
            I am reviewing available Autocracy tenets, noting incomplete branches in Fealty, Rationalism, and Authority. My current Grand Strategy is Conquest, but I'm considering switching to Culture given our proximity to a cultural victory. This decision will influence resource prioritization and wonder construction.
            
            **Assessing Global Standing**
            
            My yields are exceptional, but I've just made peace with Songhai. While our military strength is dominant, Rome captured a city. I'm also noting a diplomatic race with the Netherlands, who are currently leading. I need to reassess my priorities based on these new developments.
            
            **Reassessing War Impact**
            
            I'm perplexed by Rome capturing Satricum, especially with my overwhelming military strength. This begs a closer look at Rome's territorial expansion and the strategic implications of our current conflict, particularly how it might hinder my impending cultural victory despite influencing all other civs.
            
            **Achieving Global Influence**
            
            My research confirms we are now influential with five of the six civilizations. With Austria, our tourism is rising rapidly, and we're set to become influential there within seven turns. This means a cultural victory is imminent, requiring only this final step for full global impact.
            
            **Completing Cultural Victory**
            
            I've confirmed that influencing all six civilizations is within reach in just seven turns. My immediate focus is now on securing the Citizen Earth Protocol wonder, which I've identified requires the Telecommunications technology. I'm verifying its availability on my tech tree and its unlock capabilities.
            
            **Researching Telecommunications**
            
            My focus is now squarely on researching Telecommunications. This technology is crucial as it unlocks the Interpretive Center, a vital wonder for boosting my cultural influence, and potentially The Internet, which significantly bolsters tourism. This appears to be the most direct route to securing a cultural victory.
            
            **Selecting Policy Focus**
            
            I've identified Futurism within the Autocracy tree as a direct boost to tourism, and am now evaluating if adopting this Level 1 tenet is more beneficial than the currently selected Level 2 tenet, Total War, or exploring the new "Artistry" policy branch.
            
            **Prioritizing Production Strategies**
            
            I'm now reassessing my Autocracy tenets, weighing "Futurism" for its tourism boost against "Total War" for production, or exploring the new "Artistry" branch. The urgency of securing the Citizen Earth Protocol wonder requires maximizing both production and science, making this policy decision critical.
            
            **Shifting Strategic Focus**
            
            I'm recalculating our approach. With extensive city development and production converting to science and culture, I'm confident we can rapidly construct the Citizen Earth Protocol once Telecommunications is researched. This frees me to reconsider our Grand Strategy beyond conquest.
            
            **Shifting Strategy to Culture**
            
            I'm now setting our Grand Strategy to "Culture" and prioritizing wonders, as this aligns with our imminent cultural victory. My immediate focus is on ensuring we can build the Citizen Earth Protocol swiftly once Telecommunications is researched, which is now my top research priority.
            
            **Securing Culture Wonder**
            
            My primary objective is now to secure the Citizen Earth Protocol wonder. I've confirmed that researching Telecommunications is the prerequisite, so that is my immediate research focus, while I also evaluate policy choices to maximize production for its swift construction.
            
            **Adjusting Diplomatic Ties**
            
            I'm reviewing our current diplomatic modifiers, realizing that to facilitate quicker peace with Rome and the Netherlands, I need to increase our relationship values with them. This shift is crucial for focusing on our cultural victory and preventing further territorial losses.
            
            **Adjusting Diplomatic Settings**
            
            I'm fine-tuning diplomatic relationships, prioritizing peace with Rome and the Netherlands by increasing our standing. My focus remains on securing the imminent cultural victory, ensuring all available diplomatic levers are pulled to facilitate this.
            
            **Rebalancing Aggression Metrics**
            
            My persona's core aggression metrics, like WarBias and HostileBias, are alarmingly high, hindering my peaceful cultural victory aspirations. I'm adjusting these to lower values, emphasizing friendliness and wonder competition to align with my strategic shift.
            
            **Adjusting Diplomatic Approach**
            
            My current diplomatic approach needs refinement to foster peace. I will set Rome, Netherlands, and Songhai's relationship modifiers to zero to facilitate peace negotiations, while maintaining Austria's positive standing to ensure continued influence and open borders crucial for my imminent cultural victory.
            
            **Adjusting Diplomatic Relationships**
            
            My focus has shifted to carefully managing diplomatic ties. I'm adjusting relationships with Rome, the Netherlands, and Songhai to secure peace, while ensuring Austria's positive standing remains, despite their denouncement, as continued influence and open borders are critical for my imminent cultural victory.
            
            **Resetting Diplomatic Bonds**
            
            I'm finalizing diplomatic adjustments, aiming for peace with Rome, the Netherlands, and Songhai by resetting our relationship values to zero. This strategic reset, along with my ongoing focus on Austria's positive standing, is critical for cementing my imminent cultural victory. My research queue is now locked on Telecommunications.
            
            **Prioritizing Technology & Policies**
            
            I'm focusing on researching Telecommunications to unlock key wonders for a cultural victory, while also evaluating policy choices like "Futurism" for tourism and "Artistry" for its potential benefits. My strategic shift to a "Culture" Grand Strategy is confirmed, with emergency priorities on wonders and science.
            
            **Finalizing Diplomatic Reset**
            
            I've confirmed the reset of diplomatic ties with Rome, the Netherlands, and Songhai to zero, solidifying peace. Austria's positive standing is maintained, and my research queue is locked on Telecommunications to secure the cultural victory, completing my persona's diplomatic adjustments.
            
            **Finalizing Diplomatic Settings**
            
            I've reset relationships with Rome, the Netherlands, and Songhai to zero to ensure peace, while maintaining Austria's positive standing. My persona's aggression is being dialed down significantly, and research is locked on Telecommunications. This completes my diplomatic and strategic adjustments for an imminent cultural victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: E5C9ydp04LRujup5
          - toolName: set-persona
          - input:
            - Rationale: Pivoting from conquest to a peaceful Cultural Victory. We are lowering military risk-taking and hostility while maximizing friendliness and diplomatic balance to secure peace and prioritize building the Citizen Earth Protocol.
            - DenounceWillingness: 3
            - FriendlyBias: 8
            - VictoryCompetitiveness: 10
            - WarBias: 2
            - HostileBias: 2
            - Boldness: 4
            - Friendliness: 8
            - DiplomaticBalance: 10
            - WonderCompetitiveness: 10
            - Meanness: 2
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: GeBVUCjU4ePH0dCG
          - toolName: set-relationship
          - input:
            - TargetID: 1
            - Rationale: Resetting diplomatic modifier with Rome to 0. We want to encourage our AI to accept peace with Rome so we can focus on our imminent Cultural Victory undisturbed.
            - Public: 0
            - Private: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: yKDX0jjwRPOhnlBT
          - toolName: set-relationship
          - input:
            - Private: 0
            - Rationale: Resetting diplomatic modifier with The Netherlands to 0 to facilitate peace negotiations, helping us pivot to our peaceful victory condition.
            - Public: 0
            - TargetID: 6
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: H1kIAoSJxt7xMNVi
          - toolName: set-relationship
          - input:
            - Private: 0
            - Rationale: Resetting relationship with Songhai to neutral/0 to stabilize our recent peace treaty.
            - Public: 0
            - TargetID: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: Z4V44U1XCS0yEUmT
          - toolName: set-research
          - input:
            - Technology: Telecommunications
            - Rationale: Telecommunications is the crucial cultural tech that boosts Landmarks (via Interpretive Center) and unlocks key late-game victory projects like Citizen Earth Protocol.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: zRyEINkelqXA6Pah
          - toolName: set-policy
          - input:
            - Policy: Futurism
            - Rationale: Adopting Futurism will directly boost our Tourism output, accelerating our cultural influence over Austria (our final target) and securing our victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: T8bQGJ7YZtTE1hSZ
          - toolName: set-flavors
          - input:
            - Flavors:
              - Wonder: 100
              - Production: 100
              - Religion: 30
              - Mobilization: 40
              - Gold: 60
              - Offense: 50
              - Culture: 100
              - Espionage: 80
              - GreatPeople: 80
              - Defense: 60
              - Happiness: 60
              - Expansion: 0
              - Science: 100
            - GrandStrategy: Culture
            - Rationale: We are transitioning our grand strategy to Culture as we are only 7 turns away from being Influential with our final opponent (Austria). We are maximizing Wonder, Science, Culture, and Production flavors to tech to Telecommunications and build the Citizen Earth Protocol immediately.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: E5C9ydp04LRujup5
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
          - toolCallId: GeBVUCjU4ePH0dCG
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: yKDX0jjwRPOhnlBT
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: H1kIAoSJxt7xMNVi
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: Z4V44U1XCS0yEUmT
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: zRyEINkelqXA6Pah
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: T8bQGJ7YZtTE1hSZ
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.