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
      - toolName: set-persona
      - args:
        - Boldness: 5
        - FriendlyBias: 8
        - Meanness: 2
        - WonderCompetitiveness: 10
        - Rationale: Pivoting to a peaceful posture to secure peace treaties, while maximizing wonder competitiveness to ensure we build the Citizen Earth Protocol as soon as it is unlocked.
        - WarBias: 2
        - HostileBias: 2
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: Encouraging the staff members to seek peace with Rome to stabilize our borders and focus production on the final victory wonder.
        - Private: 0
        - Public: 0
        - TargetID: 1
    - #2:
      - toolName: set-relationship
      - args:
        - Private: 0
        - Public: 0
        - TargetID: 6
        - Rationale: Encouraging the staff members to seek peace with our main competitor, the Netherlands, to secure our borders for the final cultural push.
    - #3:
      - toolName: set-research
      - args:
        - Rationale: Telecommunications is the crucial technology that unlocks the Citizen Earth Protocol wonder, which is required to complete our Cultural Victory.
        - Technology: Telecommunications
    - #4:
      - toolName: set-policy
      - args:
        - Rationale: Adopting the Level 2 Autocracy tenet Total War to progress our tenets toward unlocking a second Level 3 tenet, which is required for Cultural Victory.
        - Policy: Total War
    - #5:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Culture
        - Flavors:
          - GreatPeople: 80
          - Defense: 50
          - Science: 80
          - Production: 100
          - Culture: 100
          - Offense: 50
          - Happiness: 60
          - Mobilization: 50
          - Wonder: 100
      - rationale: Setting the grand strategy to Culture and maximizing culture, wonders, science, and great people generation to accelerate our progress toward the Citizen Earth Protocol wonder and final victory.
  - tokens:
    - inputTokens: 88701
    - reasoningTokens: 9270
    - outputTokens: 340
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Advancing Through Eras**
            
            I've just propelled us into the Information Era at turn 384, a significant leap. With a golden age winding down and a strong global standing, my focus is now on optimizing our technological and policy development to maintain this lead.
            
            **Selecting Next Policy**
            
            My current focus is on selecting the next policy to adopt. I've confirmed that "Total War" remains a valid choice within the fully adopted Autocracy branch. My analysis also suggests a strong lead in Domination Victory, with Germany and Rome holding a significant number of capitals.
            
            **Securing Cultural Victory**
            
            My immediate focus has shifted. I've discovered we are on the cusp of a Cultural Victory, needing only to influence Austria, which is just 7 turns away. I'm now verifying if we meet the other victory conditions, particularly regarding ideology tenets and wonder completion.
            
            **Shifting Victory Focus**
            
            I've identified that we are unexpectedly close to a Cultural Victory, just 7 turns from influencing Austria. This has prompted me to re-evaluate our grand strategy. While Conquest remains a valid option, securing this Cultural win quickly seems more pragmatic given our current progress and tourism output.
            
            **Prioritizing Cultural Acceleration**
            
            My thoughts are now centered on the World Congress. I've confirmed the "International Worlds" proposal is up for vote and carries immense potential for accelerating our Cultural Victory by boosting tourism significantly for 20 turns. I'm also evaluating whether switching our Grand Strategy to "Culture" aligns best with this immediate goal, even while engaged in a large-scale war.
            
            **Evaluating Diplomatic Status**
            
            My current analysis is focused on our diplomatic standings, particularly with Austria, given our nearing Cultural Victory. I'm reconciling our previously set high public and private opinion values with the current "Hostile" status and mutual denouncement. This contradiction needs clarification to ensure our victory path.
            
            **Reassessing Victory Conditions**
            
            My focus has abruptly shifted. Despite my prior calculations, Rome has recaptured Satricum, a Roman city I had taken. This event, coupled with my immense military advantage and cities churning out infinite projects, makes me question our current victory trajectory and potential vulnerabilities, even with our overwhelming strength.
            
            **Reconsidering City Destruction**
            
            My focus has shifted to unexpected city razing. Ardea and Tlaxcala are being destroyed, which was not my intention. I need to understand why these cities were captured and marked for razing, and if this action aligns with our current strategic goals.
            
            **Analyzing Tenets for Victory**
            
            I'm now scrutinizing our adopted Autocracy tenets. I need to confirm if "Cult of Personality" and another, yet unidentified, Tier 3 tenet are in place, as this is critical for achieving the Cultural Victory we are so close to securing.
            
            **Confirming Tenet Requirements**
            
            I'm verifying our Autocracy tenets to ensure we have the necessary two Tier 3 tenets for a Cultural Victory. It appears "Cult of Personality" is secured, but I need to confirm the second required Tier 3 tenet, as this is critical to our current victory path.
            
            **Confirming Tenet Tier**
            
            I'm re-evaluating our Autocracy tenets. It seems "Total War" is a Tier 2, not Tier 3, tenet as I initially thought. My current focus is on understanding why no Tier 3 options are appearing, as this is crucial for our Cultural Victory condition.
            
            **Selecting Artistry Branch**
            
            I've identified that "Artistry" is a new branch and would be highly beneficial for our Cultural Victory. I'm now assessing its potential impact and deciding if it's the optimal path forward, especially considering our existing Autocracy tenets and the imminent victory conditions.
            
            **Researching Wonder Unlock**
            
            My focus is on identifying the technology that unlocks the "Citizen Earth Protocol" wonder. I need to determine if it's immediately available in the Information Era or if a specific research path is required before construction can begin.
            
            **Researching Internet Access**
            
            I'm prioritizing research toward "The Internet," which offers a significant tourism boost crucial for our Cultural Victory. Both "Satellites" and "Telecommunications" unlock this. My current research is "Advanced Ballistics," and I need to pivot to one of those faster paths.
            
            **Researching Internet Access**
            
            My immediate focus is on accelerating our path to "The Internet" by prioritizing "Satellites" in our research queue. I'm also re-evaluating our next policy adoption, as "Artistry" appears to be a strong contender for boosting tourism, despite our current Autocracy tenets and ongoing conflict.
            
            **Confirming Tier 3 Tenets**
            
            I'm re-examining our Autocracy tenets. While "Cult of Personality" is indeed a Tier 3, the requirements for a second Tier 3 tenet in VP are now my central focus. I'm verifying if additional Tier 2 tenets are prerequisites for unlocking another Tier 3 option.
            
            **Selecting Next Tenet**
            
            I'm confirming that "Total War," a Level 2 tenet, is already selected as my next policy. This is crucial, as acquiring it will give me four Level 2 tenets, which should unlock a second Level 3 tenet in Autocracy for our Cultural Victory.
            
            **Confirming Policy Choice**
            
            I'm verifying my decision to adopt "Total War." Its benefits for production and warscore are essential for our current conflicts, especially given Rome's recent capture of Satricum and their significant military presence. I will ensure this policy is actively set.
            
            **Adjusting War Strategy**
            
            I'm reassessing our current military situation, particularly the disparity in strength around Medan. Despite our overall military might, localized weaknesses necessitate adjusting our flavors to bolster combat effectiveness and secure this crucial city, while still pursuing our Cultural Victory goals.
            
            **Adjusting Flavor Focus**
            
            I've realized our current flavors are heavily skewed towards military and production. With a Cultural Victory imminent, I'm considering if increasing Culture and Great People flavors would accelerate our tourism output, and if switching our Grand Strategy to Culture is indeed the most efficient path to securing this victory swiftly.
            
            **Securing Citizen Earth Protocol**
            
            I've realized the "Citizen Earth Protocol" wonder is crucial for our Cultural Victory. It seems unlocked by "Telecommunications" or "Satellites," and I'm now prioritizing research to ensure we can build it before Austria becomes fully influential, which is only 7 turns away.
            
            **Prioritizing Telecommunications Research**
            
            My focus is now on accelerating research towards "Telecommunications." This technology is vital as it unlocks the "Citizen Earth Protocol" wonder, which is critical for our imminent Cultural Victory. I'm ensuring this research is prioritized over other paths to secure the wonder before Austria's influence solidifies.
            
            **Switching Grand Strategy**
            
            I've decided to switch our Grand Strategy to "Culture" and significantly boost Culture, Great People, and Wonder construction flavors. This will align our efforts to rapidly build the "Citizen Earth Protocol" wonder and accelerate our tourism output towards an imminent Cultural Victory.
            
            **Balancing Flavors for Victory**
            
            I'm now considering the delicate balance required to secure our imminent Cultural Victory while simultaneously maintaining a strong military. My plan is to boost Culture, Wonder construction, and Great People flavors to 100, while prioritizing Science and Espionage at 80. Crucially, I will maintain high Offense and Mobilization at 70, and Defense at 40, to protect our empire and prevent losses during this critical period.
            
            **Clarifying Diplomatic Stance**
            
            I'm trying to make sense of our diplomatic situation with Austria. Despite previously setting high public and private opinions, and even having trade agreements and a defensive pact, our current "denounced" status is confusing. I need to resolve this contradiction to ensure our tourism and victory path remain clear.
            
            **Establishing Trade Routes**
            
            My current focus is on establishing trade routes with Austria to boost our tourism. I'm confirming that despite our denouncements, we can still initiate trade, which is crucial for securing our Cultural Victory within the remaining turns.
            
            **Resolving Diplomatic Conflicts**
            
            My current thoughts are focused on resolving our ongoing wars with Rome and the Netherlands. I am considering using `set-relationship` to improve our diplomatic standing with them, as this is essential to accepting peace treaties and fully dedicating our attention to securing the Cultural Victory and completing the "Citizen Earth Protocol" wonder.
            
            **Adjusting Persona Values**
            
            I'm now reviewing our persona values. Given our imminent Cultural Victory and need for peace, I'm considering reducing WarBias and HostileBias, and increasing FriendlyBias and DiplomaticBalance to facilitate peace with Rome and the Netherlands. This adjustment should aid in securing treaties and focusing on wonder construction.
            
            **Refining Persona for Peace**
            
            I'm adjusting our persona values significantly. To secure our Cultural Victory and facilitate peace with Rome and the Netherlands, I'm reducing WarBias and HostileBias, while increasing FriendlyBias and WonderCompetitiveness. This strategic recalibration aims to foster diplomacy and ensure the successful construction of the "Citizen Earth Protocol" wonder.
            
            **Shifting to Peace**
            
            I'm adjusting our persona to foster peace, aiming to secure treaties with Rome and the Netherlands. My focus is on increasing friendly biases and wonder competitiveness to facilitate the completion of the "Citizen Earth Protocol" wonder and secure our imminent Cultural Victory.
            
            **Adopting Peaceful Posture**
            
            I'm adjusting our persona values, significantly reducing War and Hostile biases while increasing Friendly and Wonder Competitiveness. This shift aims to facilitate peace treaties with Rome and the Netherlands, ensuring focus on the "Citizen Earth Protocol" wonder and securing our Cultural Victory.
            
            **Verifying Policy Name**
            
            I am confirming that "Total War" is indeed the correct nomenclature for the Level 2 Autocracy tenet, which is essential for unlocking the next stage of our tenet progression towards a Cultural Victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: mlEV3NfBopvKRNfb
          - toolName: set-persona
          - input:
            - Boldness: 5
            - FriendlyBias: 8
            - Meanness: 2
            - WonderCompetitiveness: 10
            - Rationale: Pivoting to a peaceful posture to secure peace treaties, while maximizing wonder competitiveness to ensure we build the Citizen Earth Protocol as soon as it is unlocked.
            - WarBias: 2
            - HostileBias: 2
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 4jXSMpv1dzzVpM3V
          - toolName: set-relationship
          - input:
            - Rationale: Encouraging the staff members to seek peace with Rome to stabilize our borders and focus production on the final victory wonder.
            - Private: 0
            - Public: 0
            - TargetID: 1
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: mrdo9rzAWOmj30Wu
          - toolName: set-relationship
          - input:
            - Private: 0
            - Public: 0
            - TargetID: 6
            - Rationale: Encouraging the staff members to seek peace with our main competitor, the Netherlands, to secure our borders for the final cultural push.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: terUnvgjg4QbcQTF
          - toolName: set-research
          - input:
            - Rationale: Telecommunications is the crucial technology that unlocks the Citizen Earth Protocol wonder, which is required to complete our Cultural Victory.
            - Technology: Telecommunications
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: X9McWUq8HgH06cPG
          - toolName: set-policy
          - input:
            - Rationale: Adopting the Level 2 Autocracy tenet Total War to progress our tenets toward unlocking a second Level 3 tenet, which is required for Cultural Victory.
            - Policy: Total War
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: YpfmfwF3fdHw6NpF
          - toolName: set-flavors
          - input:
            - GrandStrategy: Culture
            - Rationale: Setting the grand strategy to Culture and maximizing culture, wonders, science, and great people generation to accelerate our progress toward the Citizen Earth Protocol wonder and final victory.
            - Flavors:
              - GreatPeople: 80
              - Defense: 50
              - Science: 80
              - Production: 100
              - Culture: 100
              - Offense: 50
              - Happiness: 60
              - Mobilization: 50
              - Wonder: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: mlEV3NfBopvKRNfb
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
          - toolCallId: 4jXSMpv1dzzVpM3V
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: mrdo9rzAWOmj30Wu
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: terUnvgjg4QbcQTF
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: X9McWUq8HgH06cPG
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: YpfmfwF3fdHw6NpF
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.